import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const appSource = await readFile(appPath, "utf8");

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function extractAsyncFunction(source, name) {
  return `async ${extractFunction(source, name)}`;
}

function deferred() {
  let resolve;
  let reject;
  const promise = new Promise((resolvePromise, rejectPromise) => {
    resolve = resolvePromise;
    reject = rejectPromise;
  });
  return { promise, reject, resolve };
}

test("report detail shards use the shared prefix algorithm and validate records", async () => {
  const requested = [];
  const reportId = "A:Report";
  const context = vm.createContext({
    loadJson: async (path) => {
      requested.push(path);
      return {
        reports: {
          [reportId]: {
            item: { id: reportId, title: "Primary" },
            related: [
              { id: "related-1", title: "Related" },
              { id: reportId, title: "Self" },
            ],
          },
        },
      };
    },
  });
  vm.runInContext(`
    ${extractFunction(appSource, "reportDetailShardPrefix")}
    ${extractAsyncFunction(appSource, "loadReportDetailRecord")}
    globalThis.testPrefix = reportDetailShardPrefix;
    globalThis.loadRecord = loadReportDetailRecord;
  `, context);

  assert.equal(context.testPrefix(reportId), "a_");
  assert.equal(context.testPrefix("Z"), "z_");
  const record = await context.loadRecord(reportId);
  assert.deepEqual(requested, ["data/report_details/a_.json"]);
  assert.equal(record.item.id, reportId);
  assert.deepEqual(Array.from(record.related, (item) => item.id), ["related-1"]);
});

test("report preview query metadata can paint a directly opened detail page", () => {
  const context = vm.createContext({ URLSearchParams });
  vm.runInContext(`
    ${extractFunction(appSource, "reportPreviewItem")}
    ${extractFunction(appSource, "reportPreviewFromParams")}
    globalThis.readPreview = reportPreviewFromParams;
  `, context);
  const params = new URLSearchParams({
    id: "direct-report",
    title: "Direct title",
    bank_name: "Bernstein Research",
    date_folder: "260819",
    available: "1",
    page_count: "42",
  });
  const preview = context.readPreview(params, "direct-report");
  assert.equal(preview.title, "Direct title");
  assert.equal(preview.bank_name, "Bernstein Research");
  assert.equal(preview.available, true);
  assert.equal(preview.page_count, 42);
});

test("a report detail shard hit renders before PDF overrides and skips the full catalog", async () => {
  const calls = [];
  const rendered = [];
  const firstPaintRelated = [];
  const configGate = deferred();
  const detailRecord = {
    item: { id: "ab-report", title: "Primary", available: true },
    related: [{ id: "related-1", title: "Related", available: true }],
  };
  const context = vm.createContext({
    URLSearchParams,
    Map,
    window: { location: { search: "?id=ab-report" } },
    document: {
      title: "",
      getElementById: () => ({ innerHTML: "" }),
    },
    loadReportDetailRecord: async () => {
      calls.push("shard");
      return detailRecord;
    },
    loadJson: async (path) => {
      calls.push(path);
      if (path === "data/catalog.json") throw new Error("full catalog must not load on a shard hit");
      if (path === "data/config.json") return configGate.promise;
      throw new Error(`unexpected path: ${path}`);
    },
    workerBaseUrl: () => "/api",
    initAccountGate: () => {},
    initAdminGate: () => {},
    initNewsfeedNav: () => {},
    reportPreviewFromParams: () => ({ id: "ab-report", title: "Primary preview" }),
    cachedReportPreview: () => null,
    renderReportFirstPaint: (_item, related = []) => {
      calls.push("first-paint");
      firstPaintRelated.push(Array.from(related, (entry) => entry.id));
    },
    rememberReportPreview: () => {},
    trackEvent: () => calls.push("page-view"),
    analyticsReportPayload: () => ({}),
    titleText: (item) => item.title,
    renderDetail: (_item, _config, items, _searchTextById, options) => {
      calls.push("render");
      rendered.push({ items, options });
    },
    deliveryPasswordFromLocation: () => "",
    loadCatalogPdfOverrides: () => {
      calls.push("overrides");
      return new Promise(() => {});
    },
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "initReport")}
    globalThis.run = initReport;
  `, context);

  const running = context.run();
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(calls.includes("first-paint"), true, "title and metadata must render before config resolves");
  assert.ok(calls.indexOf("page-view") < calls.indexOf("shard"), "page attribution must not wait for the detail shard");
  assert.deepEqual(firstPaintRelated.at(-1), ["related-1"], "local recommendations must render before config resolves");
  assert.equal(calls.includes("render"), false, "interactive controls may wait for config");
  configGate.resolve({ worker_base_url: "/api" });
  await running;
  assert.equal(calls.includes("data/catalog.json"), false);
  assert.ok(calls.indexOf("render") < calls.indexOf("overrides"));
  assert.deepEqual(Array.from(rendered[0].items, (item) => item.id), ["ab-report", "related-1"]);
  assert.deepEqual(Array.from(rendered[0].options.relatedItems, (item) => item.id), ["related-1"]);
});

test("a missing report detail shard falls back to the legacy full catalog", async () => {
  const calls = [];
  let renderedItem = null;
  const context = vm.createContext({
    URLSearchParams,
    Map,
    window: { location: { search: "?id=legacy-report" } },
    document: {
      title: "",
      getElementById: () => ({ innerHTML: "" }),
    },
    loadReportDetailRecord: async () => null,
    loadJson: async (path) => {
      calls.push(path);
      if (path === "data/config.json") return { worker_base_url: "/api" };
      if (path === "data/catalog.json") {
        return { items: [{ id: "legacy-report", title: "Legacy", available: true }] };
      }
      throw new Error(`unexpected path: ${path}`);
    },
    workerBaseUrl: () => "/api",
    initAccountGate: () => {},
    initAdminGate: () => {},
    initNewsfeedNav: () => {},
    reportPreviewFromParams: () => null,
    cachedReportPreview: () => null,
    renderReportFirstPaint: () => {},
    rememberReportPreview: () => {},
    trackEvent: () => {},
    analyticsReportPayload: () => ({}),
    titleText: (item) => item.title,
    renderDetail: (item, _config, _items, _searchTextById, options) => {
      renderedItem = { item, options };
    },
    deliveryPasswordFromLocation: () => "",
    loadCatalogPdfOverrides: () => new Promise(() => {}),
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "initReport")}
    globalThis.run = initReport;
  `, context);

  await context.run();
  assert.equal(calls.includes("data/catalog.json"), true);
  assert.equal(renderedItem.item.id, "legacy-report");
  assert.equal(renderedItem.options.relatedItems, null);
});

test("external related reports render local rows immediately and append remote rows progressively", async () => {
  const sources = new Map([
    ["thinktank", deferred()],
    ["external", deferred()],
    ["report-a", deferred()],
    ["authority", deferred()],
  ]);
  const tracked = [];
  const section = { hidden: true };
  const status = { className: "", textContent: "" };
  const list = {
    innerHTML: "",
    clickHandler: null,
    addEventListener(type, handler) {
      if (type === "click") this.clickHandler = handler;
    },
  };
  const elements = {
    externalRelatedSection: section,
    externalRelatedStatus: status,
    externalRelatedList: list,
  };
  const context = vm.createContext({
    Map,
    Promise,
    document: { getElementById: (id) => elements[id] || null },
    THINKTANK_SOURCE: "thinktank",
    EXTERNAL_SOURCE: "external",
    REPORT_A_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    relatedQueryForDoc: () => "topic",
    catalogRelatedForDoc: () => [{ id: "local-1", title: "Local" }],
    docRelatedRow: (item) => `<a class="related-row" data-id="${item.id}" data-recommendation-source="${item.source}">${item.id}</a>`,
    fetchDocRelatedSource: (_workerUrl, _endpoint, _query, source) => sources.get(source).promise,
    analyticsReportPayload: (item, source) => ({ report_id: item.id, source }),
    trackEvent: (_workerUrl, type, data) => tracked.push({ type, data }),
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "initExternalRelated")}
    globalThis.run = initExternalRelated;
  `, context);

  const pending = context.run({ id: "parent-1" }, "/api", [], new Map());
  assert.match(list.innerHTML, /local-1/);
  assert.doesNotMatch(list.innerHTML, /loading-spinner/);
  assert.equal(status.textContent, "更多相关报告仍在补充…");

  sources.get("external").resolve([{ id: "remote-1", title: "Remote" }]);
  await new Promise((resolve) => setImmediate(resolve));
  assert.match(list.innerHTML, /local-1/);
  assert.match(list.innerHTML, /remote-1/);

  sources.get("thinktank").reject(new Error("unavailable"));
  sources.get("report-a").resolve([]);
  sources.get("authority").resolve([]);
  await pending;
  assert.match(list.innerHTML, /local-1/);
  assert.match(list.innerHTML, /remote-1/);
  assert.equal(status.textContent, "");

  list.clickHandler({
    target: {
      closest: () => ({
        dataset: { id: "remote-1", recommendationSource: "external" },
      }),
    },
  });
  assert.equal(tracked[0].type, "report_open");
  assert.equal(tracked[0].data.placement, "report_related");
  assert.equal(tracked[0].data.parent_report_id, "parent-1");
  assert.equal(tracked[0].data.source, "external");
});

test("external related reports replace preview matches from the compact full candidate pool", async () => {
  const compact = deferred();
  const section = { hidden: true };
  const status = { className: "", textContent: "" };
  const list = { innerHTML: "", addEventListener() {} };
  const context = vm.createContext({
    Map,
    Promise,
    document: {
      getElementById(id) {
        return { externalRelatedSection: section, externalRelatedStatus: status, externalRelatedList: list }[id] || null;
      },
    },
    THINKTANK_SOURCE: "thinktank",
    EXTERNAL_SOURCE: "external",
    REPORT_A_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    relatedQueryForDoc: () => "topic",
    catalogRelatedForDoc: (_item, items) => items.slice(0, 1),
    docRelatedRow: (item) => `<a class="related-row" data-id="${item.id}">${item.id}</a>`,
    analyticsReportPayload: () => ({}),
    trackEvent: () => {},
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "initExternalRelated")}
    globalThis.run = initExternalRelated;
  `, context);

  const pending = context.run(
    { id: "parent-1" },
    "",
    [{ id: "preview-1" }],
    new Map(),
    compact.promise,
  );
  assert.match(list.innerHTML, /preview-1/);
  compact.resolve([{ id: "complete-1" }, { id: "complete-2" }]);
  await pending;
  await new Promise((resolve) => setImmediate(resolve));
  assert.match(list.innerHTML, /complete-1/);
  assert.doesNotMatch(list.innerHTML, /preview-1/);
});

test("external related reports show a recent fallback without a spinner when preview matching is empty", async () => {
  const compact = deferred();
  const section = { hidden: true };
  const status = { className: "", textContent: "" };
  const list = { innerHTML: "", addEventListener() {} };
  const context = vm.createContext({
    Map,
    Promise,
    document: {
      getElementById(id) {
        return { externalRelatedSection: section, externalRelatedStatus: status, externalRelatedList: list }[id] || null;
      },
    },
    THINKTANK_SOURCE: "thinktank",
    EXTERNAL_SOURCE: "external",
    REPORT_A_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    relatedQueryForDoc: () => "unmatched topic",
    catalogRelatedForDoc: () => [],
    docRelatedRow: (item) => `<a class="related-row" data-id="${item.id}">${item.id}</a>`,
    analyticsReportPayload: () => ({}),
    trackEvent: () => {},
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "initExternalRelated")}
    globalThis.run = initExternalRelated;
  `, context);

  await context.run(
    { id: "parent-1" },
    "",
    [{ id: "recent-1" }, { id: "recent-2" }],
    new Map(),
    compact.promise,
  );
  assert.match(list.innerHTML, /recent-1/);
  assert.doesNotMatch(list.innerHTML, /loading-spinner/);
  assert.match(status.textContent, /先显示近期报告/);
  compact.resolve([]);
  await new Promise((resolve) => setImmediate(resolve));
  assert.match(status.textContent, /已显示近期报告/);
});

test("each remote related source has an abortable hard timeout", async () => {
  const context = vm.createContext({
    AbortController,
    encodeURIComponent,
    window: { clearTimeout, setTimeout },
    fetch: async (_url, init) => new Promise((_resolve, reject) => {
      init.signal.addEventListener("abort", () => {
        const error = new Error("aborted");
        error.name = "AbortError";
        reject(error);
      });
    }),
  });
  vm.runInContext(`
    ${extractAsyncFunction(appSource, "fetchDocRelatedSource")}
    globalThis.run = fetchDocRelatedSource;
  `, context);

  await assert.rejects(
    context.run("/api", "external/search", "topic", "external", { id: "parent", source: "external" }, 4, 5),
    (error) => error && error.name === "AbortError",
  );
  assert.match(extractAsyncFunction(appSource, "fetchDocRelatedSource"), /timeoutMs = 2500/);
});

test("catalog recommendation clicks include placement and parent report attribution", () => {
  const renderDetail = extractFunction(appSource, "renderDetail");
  assert.match(renderDetail, /placement: "report_related"/);
  assert.match(renderDetail, /parent_report_id: String\(item\.id \|\| ""\)/);
});

test("delivery and external links carry cross-browser first-paint metadata", () => {
  const deliveryPageUrl = extractFunction(appSource, "deliveryPageUrl");
  const externalPageUrl = extractFunction(appSource, "externalPageUrl");
  assert.match(deliveryPageUrl, /preview/);
  assert.match(externalPageUrl, /"title"/);
  assert.match(externalPageUrl, /"institution"/);
  assert.match(appSource, /renderExternalDetailFirstPaint\(item, target\)/u);
  assert.match(extractFunction(appSource, "renderReportFirstPaint"), /availabilityKnown/u);
});

test("external detail first paint uses the preview catalog instead of the full catalog", () => {
  assert.match(appSource, /loadOptionalJson\("data\/catalog_preview\.json", \{ items: \[\] \}\)/u);
  assert.match(appSource, /data\/catalog_recommendations\.json/u);
  const start = appSource.indexOf("async function initExternalDetail(");
  const end = appSource.indexOf("\n  async function ", start + 1);
  const source = appSource.slice(start, end > start ? end : undefined);
  assert.doesNotMatch(source, /data\/catalog\.json/u);
  assert.match(source, /requestAnimationFrame/u);
  assert.ok(
    source.indexOf('trackEvent("", "page_view"') < source.indexOf("await Promise.all"),
    "doc attribution must not wait for config or preview catalog",
  );
  assert.ok(
    source.indexOf('trackEvent("", "page_view"') < source.indexOf("await fetchDocDetailItem"),
    "doc attribution must be sent before a slow detail lookup",
  );
});
