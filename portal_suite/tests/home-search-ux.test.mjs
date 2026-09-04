import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const htmlPath = new URL("../site_src/index.html", import.meta.url);
const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);

test("localized home first paint defers the full catalog while zh-Hans keeps its established start", async () => {
  const source = await readFile(appPath, "utf8");
  const initIndex = source.slice(source.indexOf("async function initIndex()"), source.indexOf("function filenameFromDisposition"));
  assert.match(source, /loadOptionalJson\("data\/catalog_preview\.json", null\)/);
  assert.ok(
    source.indexOf('loadOptionalJson("data/catalog_preview.json", null)')
      < source.indexOf("const startFullCatalogLoad = () =>"),
    "the small preview must be resolved before the full catalog loader is created",
  );
  assert.match(initIndex, /const deferLocalizedHomeCatalog = shouldDeferLocalizedHomeCatalog\(CONTENT_LOCALE\)/);
  assert.match(initIndex, /function startFullCatalogUpgrade\(\)[\s\S]*const upgrade = startFullCatalogLoad\(\)\.then\(async \(fullCatalog\) =>/);
  assert.match(initIndex, /const initialCatalog = initialHomeCatalog\(previewCatalog, deferLocalizedHomeCatalog\);[\s\S]*if \(initialCatalog\.needsSynchronousFullCatalog\) catalog = await startFullCatalogLoad\(\);/);
  assert.match(initIndex, /fullCatalogRetryAfter = Date\.now\(\) \+ LOCALIZED_FULL_CATALOG_RETRY_COOLDOWN_MS/);
  assert.match(initIndex, /if \(!fullCatalogReady && fullCatalogUpgradePromise === upgrade\) \{\s*fullCatalogUpgradePromise = null;/);
  assert.match(initIndex, /const startedNow = localizedCatalogStarter\.startNow\(\);[\s\S]*const retryDelay = Math\.max\(0, fullCatalogRetryAfter - Date\.now\(\)\);[\s\S]*fullCatalogIntentRetryTimer = window\.setTimeout\([\s\S]*if \(!fullCatalogReady\) void startFullCatalogUpgrade\(\);/);
  assert.match(initIndex, /loadHotReports\(initialHotReportQuery\);[\s\S]*if \(deferLocalizedHomeCatalog\) \{\s*localizedHotOverlayStarter\.schedule\(\);\s*\} else \{\s*localizedCatalogStarter\.startNow\(\);/);
  assert.doesNotMatch(initIndex, /localizedCatalogStarter\.schedule\(\)/);
  assert.match(source, /await rebuildCatalogDerivedInChunks\(fullCatalog, catalogPdfOverrides\);\s*fullCatalogReady = true;/);
  assert.match(initIndex, /render\(\{ resetPage: earlyInputTouched \|\| Boolean\(input\.value\.trim\(\)\) \}\)/);
  assert.match(source, /overrideVersion !== catalogOverrideVersion/);
  assert.match(source, /cache: "reload"/);
  assert.match(source, /loadCatalogPdfOverrides\(workerUrl\)\.then\(\(overrides\) =>/);
  assert.match(initIndex, /const localizedHotOverlayStarter = createIdleOrIntentStarter\(\(\) => \{[\s\S]*const localizeDeferredHotReports = deferredHotReportLocalization;[\s\S]*const localizedCatalogStarter = createIdleOrIntentStarter\(\(\) => \{\s*void startFullCatalogUpgrade\(\);\s*void startCatalogPdfOverridesLoad\(\);/);
  assert.doesNotMatch(initIndex, /const catalogPdfOverrides = await loadCatalogPdfOverrides/);
  assert.doesNotMatch(initIndex, /backgroundFullCatalogPromise/);
});

test("bounded background scheduling is reusable while the full catalog remains intent-only", async () => {
  const source = await readFile(appPath, "utf8");
  const helperStart = source.indexOf("const LOCALIZED_HOME_CATALOG_LOCALES");
  const helperEnd = source.indexOf("const INDUSTRY_RULES", helperStart);
  assert.ok(helperStart >= 0 && helperEnd > helperStart, "localized catalog scheduling helpers must exist");
  const sandbox = {};
  vm.runInNewContext(`
    ${source.slice(helperStart, helperEnd)}
    globalThis.catalogScheduling = {
      locales: [...LOCALIZED_HOME_CATALOG_LOCALES],
      idleTimeout: LOCALIZED_FULL_CATALOG_IDLE_TIMEOUT_MS,
      fallbackDelay: LOCALIZED_FULL_CATALOG_FALLBACK_DELAY_MS,
      retryCooldown: LOCALIZED_FULL_CATALOG_RETRY_COOLDOWN_MS,
      shouldDeferLocalizedHomeCatalog,
      initialHomeCatalog,
      shouldDeferInitialHotOverlay,
      createIdleOrIntentStarter,
    };
  `, sandbox);
  const helpers = sandbox.catalogScheduling;
  assert.deepEqual(Array.from(helpers.locales), ["ko", "ja", "ar"]);
  assert.equal(helpers.idleTimeout, 6_000, "idle work must have a six-second upper bound");
  assert.equal(helpers.fallbackDelay, 3_000, "browsers without requestIdleCallback must still start promptly");
  assert.equal(helpers.retryCooldown, 2_000, "failed full-catalog requests must use a short retry cooldown");
  assert.equal(helpers.shouldDeferLocalizedHomeCatalog("zh-Hans"), false);
  assert.equal(helpers.shouldDeferLocalizedHomeCatalog("ko"), true);
  assert.equal(helpers.shouldDeferLocalizedHomeCatalog("ja"), true);
  assert.equal(helpers.shouldDeferLocalizedHomeCatalog("ar"), true);
  const localizedMissingPreview = helpers.initialHomeCatalog(null, true);
  assert.equal(localizedMissingPreview.needsSynchronousFullCatalog, false);
  assert.deepEqual(Array.from(localizedMissingPreview.catalog.items), []);
  assert.equal(
    helpers.initialHomeCatalog(null, false).needsSynchronousFullCatalog,
    true,
    "zh-Hans keeps its established synchronous fallback when the preview is missing",
  );
  const preview = { items: [{ id: "latest" }] };
  assert.equal(helpers.initialHomeCatalog(preview, true).catalog, preview);
  assert.equal(helpers.shouldDeferInitialHotOverlay("ko", false, "", 0, true), true);
  assert.equal(helpers.shouldDeferInitialHotOverlay("zh-Hans", false, "", 0, true), false);
  assert.equal(helpers.shouldDeferInitialHotOverlay("ko", true, "", 0, true), false);
  assert.equal(helpers.shouldDeferInitialHotOverlay("ko", false, "ai", 0, true), false);

  let startCount = 0;
  let idleCallback = null;
  let idleOptions = null;
  const cancelledIdle = [];
  const idleScheduler = {
    requestIdleCallback(callback, options) {
      idleCallback = callback;
      idleOptions = options;
      return 41;
    },
    cancelIdleCallback(handle) { cancelledIdle.push(handle); },
    setTimeout() { throw new Error("idle-capable scheduler must not use a timer"); },
    clearTimeout() {},
  };
  const starter = helpers.createIdleOrIntentStarter(() => { startCount += 1; }, idleScheduler);
  starter.schedule();
  assert.equal(startCount, 0, "scheduled background work must not start during first-paint setup");
  assert.equal(idleOptions.timeout, 6_000);
  assert.equal(starter.startNow(), true, "explicit intent must start work immediately");
  assert.equal(startCount, 1);
  assert.deepEqual(cancelledIdle, [41]);
  idleCallback();
  assert.equal(startCount, 1, "a later idle callback must not issue a duplicate full-catalog request");
  assert.equal(starter.startNow(), false);

  let fallbackCallback = null;
  let fallbackDelay = null;
  let fallbackStarts = 0;
  const fallbackScheduler = {
    setTimeout(callback, delay) {
      fallbackCallback = callback;
      fallbackDelay = delay;
      return 9;
    },
    clearTimeout() {},
  };
  const fallbackStarter = helpers.createIdleOrIntentStarter(() => { fallbackStarts += 1; }, fallbackScheduler);
  fallbackStarter.schedule();
  assert.equal(fallbackDelay, 3_000);
  assert.equal(fallbackStarts, 0);
  fallbackCallback();
  assert.equal(fallbackStarts, 1, "fallback scheduling must prevent indefinite deferral");
});

test("localized first paint defers the Hot overlay and atomically reapplies it after idle or intent", async () => {
  const source = await readFile(appPath, "utf8");
  const initIndex = source.slice(source.indexOf("async function initIndex()"), source.indexOf("function filenameFromDisposition"));
  assert.match(initIndex, /const deferHotOverlay = shouldDeferInitialHotOverlay\([\s\S]*\) && typeof hotReportLocalizer === "function"/);
  assert.match(initIndex, /if \(deferHotOverlay\) \{[\s\S]*const sourceData = data;[\s\S]*deferredHotReportLocalization = \(\) => \{[\s\S]*hotReportLocalizer\(sourceData\)/);
  assert.match(initIndex, /retainLocalizedPageDuringDeferredOverlay = Boolean\(currentHotReportPage\(\)\)[\s\S]*cleanQuery === hotReportActiveQuery/);
  assert.match(initIndex, /if \(retainLocalizedPageDuringDeferredOverlay\) \{[\s\S]*setHotReportsStatus\("翻译正在更新，请稍后再试。"\)[\s\S]*\} else \{\s*data = \{\s*generation:[\s\S]*items: \[\],\s*total: 0,\s*next_cursor: "",\s*has_more: false,\s*locale_translation_pending: true/);
  assert.match(initIndex, /if \(!retainLocalizedPageDuringDeferredOverlay\) \{\s*applyHotReportPayload\(data, \{[\s\S]*cacheFirstPage: !deferHotOverlay/);
  assert.match(initIndex, /localizedData && localizedData\.locale_translation_pending === true[\s\S]*retainLocalizedPageDuringDeferredOverlay[\s\S]*setHotReportsStatus\("翻译正在更新，请稍后再试。"\)[\s\S]*else \{\s*applyHotReportPayload\(localizedData/);
  assert.match(initIndex, /const localizedHotOverlayStarter = createIdleOrIntentStarter\(\(\) => \{\s*localizedBackgroundStarted = true;\s*const localizeDeferredHotReports = deferredHotReportLocalization;\s*if \(localizeDeferredHotReports\) localizeDeferredHotReports\(\);\s*\}\);/);
  assert.match(initIndex, /const localizedCatalogStarter = createIdleOrIntentStarter\(\(\) => \{\s*void startFullCatalogUpgrade\(\);\s*void startCatalogPdfOverridesLoad\(\);\s*\}\);/);
  assert.match(initIndex, /requestVersion !== hotReportRequestVersion \|\| cleanQuery !== hotReportActiveQuery/);
  assert.doesNotMatch(initIndex, /if \(deferHotOverlay\)[\s\S]{0,1600}applyHotReportPayload\(sourceData/);
});

test("hot reports paint a validated last-good first page before refreshing in the background", async () => {
  const source = await readFile(appPath, "utf8");
  const helperStart = source.indexOf("function normalizeHotReportFirstPageCache(");
  const helperEnd = source.indexOf("function recentDateBounds(", helperStart);
  const brandStart = source.indexOf("const LEGACY_SOURCE_WORDS");
  const brandEnd = source.indexOf("function publicMessageText(", brandStart);
  assert.ok(helperStart >= 0 && helperEnd > helperStart, "the first-page cache helpers must exist");
  assert.ok(brandStart >= 0 && brandEnd > brandStart, "the public brand helper must exist");
  const sandbox = {};
  vm.runInNewContext(`
    const PUBLIC_BRAND = "KC桌面";
    ${source.slice(brandStart, brandEnd)}
    const HOT_REPORT_FIRST_PAGE_CACHE_KEY = "portal_hot_report_first_page_v1";
    const HOT_REPORT_FIRST_PAGE_CACHE_VERSION = 1;
    const HOT_REPORT_FIRST_PAGE_CACHE_MAX_ITEMS = 24;
    const HOT_REPORT_FIRST_PAGE_CACHE_TTL_MS = 24 * 60 * 60 * 1000;
    const HOT_REPORT_SOURCE = "hot";
    ${source.slice(helperStart, helperEnd)}
    globalThis.cacheHelpers = {
      normalizeHotReportFirstPageCache,
      hotReportLocalStorage,
      readHotReportFirstPageCache,
      writeHotReportFirstPageCache,
    };
  `, sandbox);
  const rows = new Map();
  const storage = {
    getItem: (key) => rows.get(key) || null,
    setItem: (key, value) => rows.set(key, String(value)),
    removeItem: (key) => rows.delete(key),
  };
  const now = Date.parse("2026-08-27T12:00:00Z");
  const page = {
    items: [
      {
        id: "hot:0123456789abcdef",
        title: "Reportify: Newest",
        institution: "Nash AI",
        description: "MacroGate cached summary",
        filename: "Portal Suite report.pdf",
        size_bytes: 42,
      },
      { id: "hot:fedcba9876543210", title: "Second", institution: "KC", size_bytes: 21 },
    ],
    nextCursor: "cursor-2",
    hasMore: true,
    total: 500,
  };
  assert.equal(sandbox.cacheHelpers.writeHotReportFirstPageCache(page, storage, now), true);
  const cached = sandbox.cacheHelpers.readHotReportFirstPageCache(storage, now + 1000);
  assert.equal(cached.items.length, 2);
  assert.equal(cached.items[0].source, "hot");
  assert.equal(cached.items[0].title, "Newest");
  assert.equal(cached.items[0].institution, "");
  assert.equal(cached.items[0].filename, "KC桌面 report.pdf");
  assert.doesNotMatch(JSON.stringify(cached), /Reportify|Nash[\s._-]*AI|Macro[\s._-]*Gate|Portal[\s._-]*Suite/iu);
  assert.equal(cached.total, 500);
  assert.equal(cached.nextCursor, "cursor-2");

  assert.equal(
    sandbox.cacheHelpers.readHotReportFirstPageCache(storage, now + 24 * 60 * 60 * 1000 + 1),
    null,
    "expired content must not become a permanent stale home page",
  );
  rows.set("portal_hot_report_first_page_v1", "{broken");
  assert.equal(sandbox.cacheHelpers.readHotReportFirstPageCache(storage, now), null);
  assert.equal(rows.has("portal_hot_report_first_page_v1"), false);
  sandbox.window = {};
  Object.defineProperty(sandbox.window, "localStorage", { get: () => { throw new Error("disabled"); } });
  assert.equal(sandbox.cacheHelpers.hotReportLocalStorage(), null, "disabled browser storage must not abort home initialization");

  const initIndex = source.slice(source.indexOf("async function initIndex()"), source.indexOf("function filenameFromDisposition"));
  assert.match(initIndex, /if \(!initialHotReportQuery\) \{[\s\S]*readHotReportFirstPageCache\(hotReportLocalStorage\(\)\)[\s\S]*hotReportPages = \[cachedFirstPage\]/);
  assert.match(initIndex, /cachedFirstPage\.items\.forEach[\s\S]*renderHotReports\(\);\s*loadHotReports\(initialHotReportQuery\)/);
  assert.match(initIndex, /replace && pageIndex === 0 && !cleanQuery[\s\S]*writeHotReportFirstPageCache\(nextPage, hotReportLocalStorage\(\)\)/);
  assert.match(initIndex, /retainedForSameQuery[\s\S]*hotReportsFailed = replace && !retainedForSameQuery/);
});

test("home search waits for stable input and cancels superseded remote searches", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /const scheduleLocalRender = \(delay = 240\)/);
  assert.match(source, /compositionstart/);
  assert.match(source, /compositionend/);
  assert.match(source, /function abortRemoteSearches\(\)[\s\S]*remoteSearchControllers\.values\(\)[\s\S]*controller\.abort\(\)/);
  assert.match(source, /abortRemoteSearches\(\)/);
  assert.match(source, /remoteSearchGeneration/);
  assert.match(source, /generation === remoteSearchGeneration/);
  assert.match(source, /\}, 480\);/);
});

test("hot-report next-page conflicts preserve the current page and restart the same query", async () => {
  const source = await readFile(appPath, "utf8");
  const requestStart = source.indexOf("async function requestHotReportPage(");
  const requestSource = source.slice(requestStart, source.indexOf("function loadHotReports(", requestStart));
  const retryStart = source.indexOf("if (hotReportsRetry) {", requestStart);
  const retrySource = source.slice(retryStart, source.indexOf("if (searchRecommendationsResults)", retryStart));
  assert.ok(requestStart >= 0, "the hot-report page request function must exist");
  assert.match(requestSource, /failure\.status = response\.status/u);
  assert.match(requestSource, /error && error\.status === 409/u);
  assert.match(requestSource, /currentHotReportPage\(\)\.cursorInvalidated = true/u);
  assert.match(requestSource, /近期热门报告列表已更新，请从第一页重新加载/u);
  assert.match(requestSource, /hotReportRetryQuery = cleanQuery/u);
  assert.doesNotMatch(requestSource, /hotReportPages\.clear|hotReportPages = \[\]/u);
  assert.match(retrySource, /loadHotReports\(hotReportRetryQuery !== null/u);
  assert.doesNotMatch(retrySource, /requestHotReportPage\(hotReportRetry/u);
});

test("remote sources use independent deadlines and generic source fallback warnings", async () => {
  const source = await readFile(appPath, "utf8");
  const remoteSearchStart = source.indexOf("const remoteSearchControllers = new Map()");
  const remoteSearch = source.slice(
    remoteSearchStart,
    source.indexOf("clearFilters.addEventListener", remoteSearchStart),
  );
  assert.ok(remoteSearchStart >= 0, "remote search controller map should exist");
  assert.match(remoteSearch, /const remoteSearchControllers = new Map\(\)/);
  assert.match(remoteSearch, /external:\s*16_000/);
  assert.match(remoteSearch, /thinktank:\s*18_000/);
  assert.match(remoteSearch, /reportA:\s*18_000/);
  assert.match(remoteSearch, /authority:\s*18_000/);
  assert.match(remoteSearch, /runRemoteSearchWithDeadline\("external", query, generation, runExternalSearch\)/);
  assert.match(remoteSearch, /remoteSearchControllers\.set\(source, controller\)/);
  assert.match(remoteSearch, /remoteSearchControllers\.get\(source\) === controller/);
  assert.match(remoteSearch, /const label = remoteSourceLabels\[source\] \|\| "此来源"/);
  assert.match(
    remoteSearch,
    /warning:\s*data\.warning[\s\S]{0,240}localizedServiceMessage\(data\.warning, "The upstream source is temporarily unavailable; cached results may be shown\."\)/,
  );
  assert.match(remoteSearch, /cacheStatus:\s*String\(data\.cache_status \|\| ""\)\.trim\(\)/);
  assert.match(remoteSearch, /externalResponseMeta\.cacheStatus === "miss"/);
  assert.match(remoteSearch, /sourceUnavailable \? "error" : "done"/);
  assert.doesNotMatch(remoteSearch, /let remoteSearchController\s*=/);
  assert.doesNotMatch(remoteSearch, /controller\.abort\(\), 18_000/);
});

test("the large full-text corpus is opt-in instead of loading on focus or idle", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /scopeFilter\.value === "fulltext"/);
  assert.match(source, /startTextIndexLoad\(\)/);
  assert.match(source, /loadSearchIndexShards\("data\/search_index_current"\)/);
  assert.doesNotMatch(source, /loadJson\("data\/search_index\.json"\)/);
  assert.doesNotMatch(source, /input\.addEventListener\("focus", startTextIndexLoad\)/);
  assert.doesNotMatch(source, /input\.addEventListener\("input", startTextIndexLoad\)/);
  assert.doesNotMatch(source, /setTimeout\(startTextIndexLoad/);
});

test("loading and multi-source progress are visible without a wait cursor", async () => {
  const [html, styles] = await Promise.all([
    readFile(htmlPath, "utf8"),
    readFile(stylesPath, "utf8"),
  ]);
  assert.match(html, /id="searchReadiness"[^>]*role="status"/);
  assert.match(html, /id="results"[^>]*is-loading[^>]*aria-busy="true"/);
  assert.match(html, /id="searchSourceProgress"[^>]*aria-live="polite"/);
  assert.match(html, /id="searchSourceProgressBar"/);
  assert.match(styles, /\.report-skeleton/);
  assert.match(styles, /\.search-source-progress/);
  assert.doesNotMatch(styles, /cursor:\s*wait/);
});
