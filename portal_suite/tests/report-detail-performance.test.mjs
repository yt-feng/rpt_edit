import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const appSource = await readFile(appPath, "utf8");
const reportHtmlPath = new URL("../site_src/report.html", import.meta.url);
const reportHtmlSource = await readFile(reportHtmlPath, "utf8");

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
  const context = vm.createContext({ URLSearchParams, publicDocItem: (item) => item });
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

test("inline report preview paints before the application bundle and preserves unknown PDF state", () => {
  const match = reportHtmlSource.match(/<script id="reportPreviewBootstrap">([\s\S]*?)<\/script>/u);
  assert.ok(match, "report.html must include the inline preview bootstrap");
  assert.ok(
    reportHtmlSource.indexOf('id="reportPreviewBootstrap"') < reportHtmlSource.indexOf('assets/app.js'),
    "the preview bootstrap must execute before the application bundle",
  );
  assert.doesNotMatch(reportHtmlSource, /Loading report/u);
  assert.doesNotMatch(match[1], /innerHTML/u);

  class Element {
    constructor(tag = "") {
      this.tag = tag;
      this.className = "";
      this.textContent = "";
      this.children = [];
    }

    append(...children) {
      this.children.push(...children);
    }

    replaceChildren(...children) {
      this.children = children;
    }
  }

  function paint(search) {
    const detail = new Element("section");
    const document = {
      title: "报告详情 | KC桌面",
      getElementById: (id) => (id === "detail" ? detail : null),
      createElement: (tag) => new Element(tag),
    };
    vm.runInNewContext(match[1], {
      encodeURIComponent,
      URLSearchParams,
      document,
      window: { location: { search } },
    });
    return { detail, document };
  }

  const unknown = paint("?id=chart-report&title=Chart%20Report&bank_name=Bernstein");
  assert.equal(unknown.detail.children[0].children[0].textContent, "Chart Report");
  assert.equal(unknown.detail.children[1].children[3].children[1].textContent, "正在确认");
  assert.equal(unknown.document.title, "Chart Report | KC桌面");

  const textOnly = paint("?id=chat-report&title=Chat%20Report&available=0");
  assert.equal(textOnly.detail.children[1].children[3].children[1].textContent, "Text only");
  assert.equal(textOnly.detail.children[2].className, "text-only-search-guidance");
  assert.match(textOnly.detail.children[2].children[1].textContent, /约 90%/u);
  assert.match(textOnly.detail.children[2].children[1].textContent, /“其他报告”等板块/u);
  assert.equal(textOnly.detail.children[2].children[2].textContent, "在首页搜索同名报告");
  assert.equal(textOnly.detail.children[2].children[2].href, "./?q=Chat%20Report");

  const oldSourceDomain = [["report", "ify"].join(""), "cn"].join(".");
  const sanitized = paint(`?id=old-link&title=${encodeURIComponent(`From ${oldSourceDomain} · Clean Report`)}&bank_name=${encodeURIComponent(oldSourceDomain)}`);
  assert.equal(sanitized.detail.children[0].children[0].textContent, "Clean Report");
  assert.equal(sanitized.detail.children[1].children[0].children[1].textContent, "正在确认");
  assert.equal(sanitized.document.title, "Clean Report | KC桌面");

  const legacyCourse = String.fromCharCode(0x9ea6, 0x5e9c, 0x8bfe, 0x5802);
  const oldCourseLink = paint(`?id=old-course&title=${encodeURIComponent(`${legacyCourse} / maifu：Clean Course Report`)}`);
  assert.equal(oldCourseLink.detail.children[0].children[0].textContent, "Clean Course Report");
  assert.equal(oldCourseLink.document.title, "Clean Course Report | KC桌面");
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
    PUBLIC_BRAND: "KC桌面",
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
    PUBLIC_BRAND: "KC桌面",
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

test("ordinary detail links retain first-paint metadata while delivery generators use the shared URL helpers", () => {
  const reportPageUrl = extractFunction(appSource, "reportPageUrl");
  const externalPageUrl = extractFunction(appSource, "externalPageUrl");
  assert.match(reportPageUrl, /preview/);
  assert.match(externalPageUrl, /"title"/);
  assert.match(externalPageUrl, /"institution"/);
  assert.match(externalPageUrl, /"description"/);
  assert.match(externalPageUrl, /"filename"/);
  assert.match(extractFunction(appSource, "initDetailAdmin"), /deliveryPageUrl\(item\.id, data\.password, item\)/u);
  assert.match(appSource, /externalPageUrl\(deliveryItem, data\.password\)/u);
  assert.match(appSource, /renderExternalDetailFirstPaint\(item, target\)/u);
  assert.match(extractFunction(appSource, "renderReportFirstPaint"), /availabilityKnown/u);
  assert.match(extractFunction(appSource, "renderReportFirstPaint"), /textOnlySearchGuidanceMarkup\(item\)/u);
  assert.match(extractFunction(appSource, "renderDetail"), /textOnlySearchGuidanceMarkup\(item\)/u);
});

test("legacy delivery redirects remain compatible and canonicalize to an id/password-only report URL", async () => {
  const params = new URLSearchParams({
    id: "delivery-report",
    password: "delivery-secret",
    source: "catalog",
    title: "Bernstein delivery report",
    title_zh: "伯恩斯坦交付报告",
    filename: "bernstein-delivery.pdf",
    date_folder: "260819",
    bank_code: "BERN",
    bank_name: "Bernstein",
    industry: "Technology",
    sector: "Semiconductors",
    category: "Equity Research",
    size_bytes: "456789",
    page_count: "31",
    available: "0",
    pdf_archived: "1",
  });
  let redirected = "";
  const target = { innerHTML: "" };
  const context = vm.createContext({
    URL,
    URLSearchParams,
    document: { getElementById: () => target },
    window: {
      location: {
        href: `https://portal.example.invalid/delivery.html?${params.toString()}`,
        search: `?${params.toString()}`,
        replace: (url) => { redirected = url; },
      },
    },
    deliveryPasswordFromLocation: (values) => values.get("password") || "",
    escapeHtml: (value) => String(value),
    publicDocItem: (item) => item,
  });
  vm.runInContext(`
    ${extractFunction(appSource, "reportPreviewItem")}
    ${extractFunction(appSource, "reportPreviewFromParams")}
    ${extractFunction(appSource, "reportPageUrl")}
    ${extractFunction(appSource, "deliveryPageUrl")}
    ${extractAsyncFunction(appSource, "initDelivery")}
    globalThis.run = initDelivery;
  `, context);
  await context.run();
  const forwarded = new URL(redirected);
  assert.equal(forwarded.pathname, "/report.html");
  assert.equal(forwarded.searchParams.get("id"), "delivery-report");
  assert.equal(forwarded.searchParams.get("password"), "delivery-secret");
  assert.deepEqual([...forwarded.searchParams.keys()].sort(), ["id", "password"]);
  assert.match(target.innerHTML, /Open report/u);
});

test("external delivery URLs contain only id/password while ordinary links retain first-paint fields", () => {
  const context = vm.createContext({
    URL,
    window: { location: { href: "https://portal.example.invalid/doc.html" } },
    publicDocItem: (item) => item,
  });
  vm.runInContext(`
    ${extractFunction(appSource, "externalPageUrl")}
    globalThis.build = externalPageUrl;
  `, context);
  const preview = {
    id: "external-123",
    source: "external",
    title: "External title",
    title_cn: "外部报告",
    institution: "Research House",
    date: "2026-08-19",
    file_type: "PDF",
    kind: "research",
    kind_label: "Research",
    page_count: 42,
    size_bytes: 987654,
    report_type: "Equity",
    language: "en",
    category: "Technology",
    author: "Analyst",
    rating: "Outperform",
    description: "Preview summary",
    filename: "external-title.pdf",
    required_plan: "annual",
  };
  const ordinaryUrl = new URL(context.build(preview, ""));
  for (const [key, value] of Object.entries(preview)) {
    assert.equal(ordinaryUrl.searchParams.get(key), String(value), `${key} must be present on ordinary detail links`);
  }
  assert.equal(ordinaryUrl.searchParams.has("password"), false);

  const deliveryUrl = new URL(context.build(preview, "external-secret"));
  assert.equal(deliveryUrl.pathname, "/doc.html");
  assert.equal(deliveryUrl.searchParams.get("id"), "external-123");
  assert.equal(deliveryUrl.searchParams.get("password"), "external-secret");
  assert.deepEqual([...deliveryUrl.searchParams.keys()].sort(), ["id", "password"]);
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
    source.indexOf("shouldDeferLocalizedHomeCatalog(CONTENT_LOCALE)")
      < source.indexOf('loadOptionalJson("data/catalog_recommendations.json"'),
    "localized external detail must stop before fetching the 14k-item recommendation catalog",
  );
  assert.ok(
    source.indexOf('trackEvent("", "page_view"') < source.indexOf("await Promise.all"),
    "doc attribution must not wait for config or preview catalog",
  );
  assert.ok(
    source.indexOf('trackEvent("", "page_view"') < source.indexOf("await fetchDocDetailItem"),
    "doc attribution must be sent before a slow detail lookup",
  );
});
