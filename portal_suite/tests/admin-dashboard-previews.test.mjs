import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const app = await readFile(appPath, "utf8");

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
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

function installPreviewHelpers(sandbox = {}) {
  vm.createContext(sandbox);
  vm.runInContext(`
    ${extractFunction(app, "adminItemDateTimestamp")}
    ${extractFunction(app, "adminDatedItemsNewestFirst")}
    ${extractFunction(app, "adminCollectionPreview")}
  `, sandbox);
  return sandbox;
}

test("admin dated previews sort newest first, keep stable ties, and expose only three rows", () => {
  const sandbox = installPreviewHelpers();
  const items = [
    { id: "old", date: "2026-05-01" },
    { id: "new-a", date: "2026-08-24" },
    { id: "middle", date: "2026-07-09" },
    { id: "new-b", date: "2026-08-24" },
    { id: "fallback", created_at: "2026-06-12T12:00:00Z" },
  ];
  const view = sandbox.adminCollectionPreview(items);
  assert.deepEqual(Array.from(view.all, (item) => item.id), ["new-a", "new-b", "middle", "fallback", "old"]);
  assert.deepEqual(Array.from(view.preview, (item) => item.id), ["new-a", "new-b", "middle"]);
  assert.equal(view.hasMore, true);
  assert.deepEqual(items.map((item) => item.id), ["old", "new-a", "middle", "new-b", "fallback"], "source order is not mutated");
});

test("management markup provides hidden More dialog triggers for both compact collections", () => {
  const markup = vm.runInNewContext(`(${extractFunction(app, "accountAdminModalMarkup")})`, {
    escapeHtml(value) { return String(value || ""); },
  })();
  for (const id of ["accountAdminMarketViewsMore", "accountAdminHotReportsMore"]) {
    assert.match(markup, new RegExp(`id="${id}"[^>]*aria-haspopup="dialog"[^>]*hidden`, "u"));
  }
  const listMarkup = vm.runInNewContext(`(${extractFunction(app, "accountAdminListModalMarkup")})`, {
    escapeHtml(value) { return String(value || ""); },
  })({
    title: "全部 Market Views",
    count: 8,
    listClass: "account-admin-files",
    bodyHtml: "<button>下载</button>",
  });
  assert.match(listMarkup, /class="admin-modal account-admin-list-modal"/u);
  assert.match(listMarkup, /class="admin-dialog account-admin-list-dialog"/u);
  assert.match(listMarkup, /role="dialog" aria-modal="true"/u);
  assert.match(listMarkup, /全部 Market Views/u);
  assert.match(listMarkup, /8 条/u);
});

test("More dialog implements Escape, focus trapping, parent isolation, and focus return", () => {
  const source = extractFunction(app, "openAccountAdminListModal");
  assert.match(source, /event\.key === "Escape"/u);
  assert.match(source, /event\.key !== "Tab"/u);
  assert.match(source, /parentModal\.setAttribute\("aria-hidden", "true"\)/u);
  assert.match(source, /parentModal\.inert = true/u);
  assert.match(source, /trigger\.focus\(\{ preventScroll: true \}\)/u);
});

test("Market Views loader keeps every item available but renders only the latest three", async () => {
  const items = [
    { id: "mv-1", title: "MV old", date: "2026-01-01", filename: "1.pdf" },
    { id: "mv-5", title: "MV newest", date: "2026-08-24", filename: "5.pdf" },
    { id: "mv-3", title: "MV third", date: "2026-06-01", filename: "3.pdf" },
    { id: "mv-4", title: "MV second", date: "2026-07-01", filename: "4.pdf" },
    { id: "mv-2", title: "MV older", date: "2026-02-01", filename: "2.pdf" },
  ];
  const sandbox = installPreviewHelpers({
    accountAdminMarketViews: new Map(),
    escapeHtml(value) { return String(value || ""); },
    formatSize() { return ""; },
    fetch: async () => new Response(JSON.stringify({ items }), {
      status: 200,
      headers: { "content-type": "application/json" },
    }),
  });
  vm.runInContext(`
    ${extractFunction(app, "adminMarketViewRow")}
    ${extractFunction(app, "loadAccountAdminMarketViews")}
  `, sandbox);
  const targets = {
    marketViewCount: { textContent: "" },
    marketViews: { innerHTML: "" },
    marketViewsMore: { hidden: true },
    marketViewsNotice: { hidden: true, textContent: "", className: "" },
  };
  const sorted = await sandbox.loadAccountAdminMarketViews("/api", targets);
  assert.deepEqual(Array.from(sorted, (item) => item.id), ["mv-5", "mv-4", "mv-3", "mv-2", "mv-1"]);
  assert.equal(targets.marketViewCount.textContent, "5 PDFs");
  assert.equal(targets.marketViewsMore.hidden, false);
  assert.match(targets.marketViews.innerHTML, /MV newest/u);
  assert.match(targets.marketViews.innerHTML, /MV second/u);
  assert.match(targets.marketViews.innerHTML, /MV third/u);
  assert.doesNotMatch(targets.marketViews.innerHTML, /MV older|MV old/u);
  assert.equal(sandbox.accountAdminMarketViews.size, 5);
});

test("hot-report loader sorts all items and renders only the latest three", async () => {
  const items = [
    { id: "hot-1", title: "Hot old", date: "2026-01-01" },
    { id: "hot-5", title: "Hot newest", date: "2026-08-24" },
    { id: "hot-3", title: "Hot third", date: "2026-06-01" },
    { id: "hot-4", title: "Hot second", date: "2026-07-01" },
    { id: "hot-2", title: "Hot older", date: "2026-02-01" },
  ];
  const requests = [];
  const sandbox = installPreviewHelpers({
    accountAdminHotReports: [],
    HOT_REPORT_SOURCE: "hot",
    URLSearchParams,
    escapeHtml(value) { return String(value || ""); },
    externalPageUrl(item) { return `/external.html?id=${item.id}`; },
    formatSize() { return ""; },
    fetch: async (url) => {
      requests.push(String(url));
      return new Response(JSON.stringify({ items, total: 5, has_more: false, next_cursor: "" }), {
        status: 200,
        headers: { "content-type": "application/json" },
      });
    },
  });
  vm.runInContext(`
    ${extractFunction(app, "adminHotReportRow")}
    ${extractFunction(app, "loadAdminHotReports")}
  `, sandbox);
  const targets = {
    hotReportSection: { hidden: false },
    hotReportList: { innerHTML: "" },
    hotReportMore: { hidden: true },
    hotReportCount: { textContent: "" },
    hotReportStatus: { textContent: "", className: "" },
  };
  const sorted = await sandbox.loadAdminHotReports("/api", targets);
  assert.deepEqual(Array.from(sorted, (item) => item.id), ["hot-5", "hot-4", "hot-3", "hot-2", "hot-1"]);
  assert.equal(targets.hotReportCount.textContent, "5 条");
  assert.equal(targets.hotReportMore.hidden, false);
  assert.match(targets.hotReportList.innerHTML, /Hot newest/u);
  assert.match(targets.hotReportList.innerHTML, /Hot second/u);
  assert.match(targets.hotReportList.innerHTML, /Hot third/u);
  assert.doesNotMatch(targets.hotReportList.innerHTML, /Hot older|Hot old/u);
  assert.deepEqual(Array.from(sandbox.accountAdminHotReports, (item) => item.id), ["hot-5", "hot-4", "hot-3", "hot-2", "hot-1"]);
  assert.deepEqual(requests, ["/api/hot-reports?limit=60"]);
});

test("hot-report admin loader follows cursors until all indexed reports are available", async () => {
  const items = Array.from({ length: 125 }, (_, index) => ({
    id: `hot-${String(index).padStart(3, "0")}`,
    title: `Hot ${index}`,
    date: new Date(Date.UTC(2026, 7, 27 - index)).toISOString().slice(0, 10),
  }));
  const requests = [];
  const sandbox = installPreviewHelpers({
    accountAdminHotReports: [],
    HOT_REPORT_SOURCE: "hot",
    URLSearchParams,
    escapeHtml(value) { return String(value || ""); },
    externalPageUrl(item) { return `/external.html?id=${item.id}`; },
    formatSize() { return ""; },
    fetch: async (url) => {
      requests.push(String(url));
      const cursor = new URL(String(url), "https://portal.invalid").searchParams.get("cursor") || "";
      const start = cursor === "page-2" ? 60 : (cursor === "page-3" ? 120 : 0);
      const pageItems = items.slice(start, start + 60);
      const hasMore = start + pageItems.length < items.length;
      const nextCursor = start === 0 ? "page-2" : (start === 60 ? "page-3" : "");
      return new Response(JSON.stringify({
        items: pageItems,
        total: items.length,
        has_more: hasMore,
        next_cursor: nextCursor,
      }), {
        status: 200,
        headers: { "content-type": "application/json" },
      });
    },
  });
  vm.runInContext(`
    ${extractFunction(app, "adminHotReportRow")}
    ${extractFunction(app, "loadAdminHotReports")}
  `, sandbox);
  const targets = {
    hotReportSection: { hidden: false },
    hotReportList: { innerHTML: "" },
    hotReportMore: { hidden: true },
    hotReportCount: { textContent: "" },
    hotReportStatus: { textContent: "", className: "" },
  };
  const sorted = await sandbox.loadAdminHotReports("/api", targets);
  assert.equal(sorted.length, 125);
  assert.equal(sandbox.accountAdminHotReports.length, 125);
  assert.equal(targets.hotReportCount.textContent, "125 条");
  assert.equal(targets.hotReportMore.hidden, false);
  assert.deepEqual(requests, [
    "/api/hot-reports?limit=60",
    "/api/hot-reports?limit=60&cursor=page-2",
    "/api/hot-reports?limit=60&cursor=page-3",
  ]);
});

test("hot-report admin pagination rejects missing or repeated cursors without showing a partial collection", async () => {
  async function runWithPages(pages) {
    let call = 0;
    const sandbox = installPreviewHelpers({
      accountAdminHotReports: [{ id: "stale" }],
      HOT_REPORT_SOURCE: "hot",
      URLSearchParams,
      escapeHtml(value) { return String(value || ""); },
      externalPageUrl(item) { return `/external.html?id=${item.id}`; },
      formatSize() { return ""; },
      fetch: async () => {
        const page = pages[Math.min(call++, pages.length - 1)];
        return new Response(JSON.stringify(page), {
          status: Number(page.status || 200),
          headers: { "content-type": "application/json" },
        });
      },
    });
    vm.runInContext(`
      ${extractFunction(app, "adminHotReportRow")}
      ${extractFunction(app, "loadAdminHotReports")}
    `, sandbox);
    const targets = {
      hotReportSection: { hidden: false },
      hotReportList: { innerHTML: "" },
      hotReportMore: { hidden: true },
      hotReportCount: { textContent: "" },
      hotReportStatus: { textContent: "", className: "" },
    };
    const result = await sandbox.loadAdminHotReports("/api", targets);
    return { result, sandbox, targets, calls: call };
  }

  const missing = await runWithPages([{ items: [{ id: "one" }], total: 2, has_more: true, next_cursor: "" }]);
  assert.equal(missing.result.length, 0);
  assert.equal(missing.sandbox.accountAdminHotReports.length, 0);
  assert.match(missing.targets.hotReportStatus.textContent, /分页数据不完整/u);

  const repeated = await runWithPages([
    { items: [{ id: "one" }], total: 3, has_more: true, next_cursor: "repeat" },
    { items: [{ id: "two" }], total: 3, has_more: true, next_cursor: "repeat" },
  ]);
  assert.equal(repeated.result.length, 0);
  assert.equal(repeated.sandbox.accountAdminHotReports.length, 0);
  assert.match(repeated.targets.hotReportStatus.textContent, /分页状态异常/u);
});

test("hot-report admin loading restarts once after an index-generation conflict", async () => {
  const responses = [
    { items: [{ id: "old-one", date: "2026-08-26" }], total: 2, has_more: true, next_cursor: "old-cursor" },
    { status: 409, detail: "Hot report index changed." },
    { items: [{ id: "new-one", date: "2026-08-27" }], total: 2, has_more: true, next_cursor: "new-cursor" },
    { items: [{ id: "new-two", date: "2026-08-26" }], total: 2, has_more: false, next_cursor: "" },
  ];
  let call = 0;
  const sandbox = installPreviewHelpers({
    accountAdminHotReports: [{ id: "stale" }],
    HOT_REPORT_SOURCE: "hot",
    URLSearchParams,
    escapeHtml(value) { return String(value || ""); },
    externalPageUrl(item) { return `/external.html?id=${item.id}`; },
    formatSize() { return ""; },
    fetch: async () => {
      const response = responses[call++];
      return new Response(JSON.stringify(response), {
        status: Number(response.status || 200),
        headers: { "content-type": "application/json" },
      });
    },
  });
  vm.runInContext(`
    ${extractFunction(app, "adminHotReportRow")}
    ${extractFunction(app, "loadAdminHotReports")}
  `, sandbox);
  const targets = {
    hotReportSection: { hidden: false },
    hotReportList: { innerHTML: "" },
    hotReportMore: { hidden: true },
    hotReportCount: { textContent: "" },
    hotReportStatus: { textContent: "", className: "" },
  };
  const result = await sandbox.loadAdminHotReports("/api", targets);
  assert.equal(call, 4, "one 409 must restart the collection from page one exactly once");
  assert.deepEqual(Array.from(result, (item) => item.id), ["new-one", "new-two"]);
  assert.deepEqual(Array.from(sandbox.accountAdminHotReports, (item) => item.id), ["new-one", "new-two"]);
  assert.equal(targets.hotReportCount.textContent, "2 条");
  assert.doesNotMatch(targets.hotReportList.innerHTML, /old-one|stale/u);
});

test("hot-report admin loading rejects a second conflict or a deduplicated count mismatch", async () => {
  async function run(responses) {
    let call = 0;
    const sandbox = installPreviewHelpers({
      accountAdminHotReports: [{ id: "stale" }],
      HOT_REPORT_SOURCE: "hot",
      URLSearchParams,
      escapeHtml(value) { return String(value || ""); },
      externalPageUrl(item) { return `/external.html?id=${item.id}`; },
      formatSize() { return ""; },
      fetch: async () => {
        const response = responses[Math.min(call++, responses.length - 1)];
        return new Response(JSON.stringify(response), {
          status: Number(response.status || 200),
          headers: { "content-type": "application/json" },
        });
      },
    });
    vm.runInContext(`
      ${extractFunction(app, "adminHotReportRow")}
      ${extractFunction(app, "loadAdminHotReports")}
    `, sandbox);
    const targets = {
      hotReportSection: { hidden: false },
      hotReportList: { innerHTML: "" },
      hotReportMore: { hidden: true },
      hotReportCount: { textContent: "" },
      hotReportStatus: { textContent: "", className: "" },
    };
    const result = await sandbox.loadAdminHotReports("/api", targets);
    return { result, sandbox, targets, calls: call };
  }

  const persistentConflict = await run([
    { items: [{ id: "first" }], total: 2, has_more: true, next_cursor: "old" },
    { status: 409, detail: "changed" },
    { items: [{ id: "second" }], total: 2, has_more: true, next_cursor: "new" },
    { status: 409, detail: "changed again" },
  ]);
  assert.equal(persistentConflict.calls, 4);
  assert.equal(persistentConflict.result.length, 0);
  assert.equal(persistentConflict.sandbox.accountAdminHotReports.length, 0);
  assert.equal(persistentConflict.targets.hotReportCount.textContent, "");

  const duplicateMismatch = await run([{
    items: [{ id: "duplicate" }, { id: "duplicate" }],
    total: 2,
    has_more: false,
    next_cursor: "",
  }]);
  assert.equal(duplicateMismatch.result.length, 0);
  assert.equal(duplicateMismatch.sandbox.accountAdminHotReports.length, 0);
  assert.match(duplicateMismatch.targets.hotReportStatus.textContent, /数量校验失败/u);
});
