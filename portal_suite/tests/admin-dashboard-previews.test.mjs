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
    publicBrandText(value, fallback = "") { return String(value || fallback || ""); },
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

function hotReportHarness(responder) {
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
      const payload = await responder(String(url), requests.length);
      return new Response(JSON.stringify(payload), {
        status: Number(payload.status || 200),
        headers: { "content-type": "application/json" },
      });
    },
  });
  vm.runInContext(`
    ${extractFunction(app, "adminHotReportRow")}
    ${extractFunction(app, "fetchAdminHotReportPage")}
    ${extractFunction(app, "loadAdminHotReports")}
    ${extractFunction(app, "openAdminHotReportList")}
  `, sandbox);
  const targets = {
    hotReportSection: { hidden: false },
    hotReportList: { innerHTML: "" },
    hotReportMore: { hidden: true },
    hotReportCount: { textContent: "" },
    hotReportStatus: { textContent: "", className: "" },
  };
  return { sandbox, targets, requests };
}

function hotItems(count) {
  return Array.from({ length: count }, (_, index) => ({
    id: `hot-${String(index).padStart(3, "0")}`,
    title: `Hot ${index}`,
    date: new Date(Date.UTC(2026, 7, 27 - index)).toISOString().slice(0, 10),
  }));
}

function indexedPage(items, url) {
  const params = new URL(url, "https://portal.invalid").searchParams;
  const start = Number(params.get("cursor") || 0);
  const page = items.slice(start, start + 60);
  const hasMore = start + page.length < items.length;
  return { items: page, total: items.length, has_more: hasMore, next_cursor: hasMore ? String(start + page.length) : "" };
}

test("opening a 500-report admin collection reads one page and renders only the newest three", async () => {
  const items = hotItems(500);
  const { sandbox, targets, requests } = hotReportHarness((url) => indexedPage(items, url));
  const loaded = await sandbox.loadAdminHotReports("/api", targets);
  assert.equal(loaded.length, 60);
  assert.equal(sandbox.accountAdminHotReports.length, 60);
  assert.equal(targets.hotReportCount.textContent, "500 条");
  assert.equal(targets.hotReportMore.hidden, false);
  assert.equal((targets.hotReportList.innerHTML.match(/class="account-admin-hot-row"/gu) || []).length, 3);
  assert.match(targets.hotReportList.innerHTML, /Hot 0/u);
  assert.doesNotMatch(targets.hotReportList.innerHTML, /Hot 3</u);
  assert.deepEqual(requests, ["/api/hot-reports?limit=60"]);
});

test("More dialog initially reuses loaded rows and fetches only the page explicitly requested", async () => {
  const items = hotItems(125);
  const { sandbox, targets, requests } = hotReportHarness((url) => indexedPage(items, url));
  await sandbox.loadAdminHotReports("/api", targets);
  let onClick;
  const count = { textContent: "" };
  const list = {
    modal: { querySelector() { return count; } },
    body: { innerHTML: "", addEventListener(_type, handler) { onClick = handler; } },
    status: { textContent: "" },
  };
  sandbox.openAccountAdminListModal = () => list;
  sandbox.openAdminHotReportList("/api", targets);
  assert.equal(requests.length, 1, "opening More is request-free");
  assert.match(list.body.innerHTML, /data-admin-hot-report-more/u);
  const button = { disabled: false };
  await onClick({ target: { closest() { return button; } } });
  assert.equal(requests.length, 2);
  assert.equal(targets.hotReportPageState.items.length, 120);
  assert.match(list.status.textContent, /120/u);
  await onClick({ target: { closest() { return { disabled: false }; } } });
  assert.equal(requests.length, 3);
  assert.equal(targets.hotReportPageState.items.length, 125);
  assert.doesNotMatch(list.body.innerHTML, /data-admin-hot-report-more/u);
  assert.equal(count.textContent, "125 条");
  assert.deepEqual(requests, [
    "/api/hot-reports?limit=60",
    "/api/hot-reports?limit=60&cursor=60",
    "/api/hot-reports?limit=60&cursor=120",
  ]);
});

test("duplicate clicks share one page request, while explicit refresh resets pagination", async () => {
  const items = hotItems(125);
  let release;
  const { sandbox, targets, requests } = hotReportHarness(async (url, call) => {
    if (call === 2) await new Promise((resolve) => { release = resolve; });
    return indexedPage(items, url);
  });
  await sandbox.loadAdminHotReports("/api", targets);
  const first = sandbox.loadAdminHotReports("/api", targets, { append: true });
  const second = sandbox.loadAdminHotReports("/api", targets, { append: true });
  await new Promise(setImmediate);
  assert.equal(requests.length, 2);
  release();
  await Promise.all([first, second]);
  assert.equal(targets.hotReportPageState.items.length, 120);
  await sandbox.loadAdminHotReports("/api", targets);
  assert.equal(requests.length, 3);
  assert.equal(targets.hotReportPageState.items.length, 60);
  assert.equal(requests.at(-1), "/api/hot-reports?limit=60");
});

test("invalid first pages fail visibly instead of claiming a complete collection", async () => {
  for (const page of [
    { items: [{ id: "one" }], total: 2, has_more: true, next_cursor: "" },
    { items: [{ id: "same" }, { id: "same" }], total: 2, has_more: false },
    { items: [{ id: "one" }], total: 2, has_more: false },
    { items: [], total: 500, has_more: true, next_cursor: "repeat" },
    { items: [], total: 501, has_more: false },
  ]) {
    const { sandbox, targets } = hotReportHarness(() => page);
    const result = await sandbox.loadAdminHotReports("/api", targets);
    assert.equal(result.length, 0);
    assert.equal(sandbox.accountAdminHotReports.length, 0);
    assert.equal(targets.hotReportMore.hidden, true);
    assert.match(targets.hotReportStatus.className, /error/u);
  }
});

test("a malformed next page keeps verified rows and its cursor available for retry", async () => {
  const responses = [
    { items: [{ id: "one" }], total: 3, has_more: true, next_cursor: "repeat" },
    { items: [{ id: "two" }], total: 3, has_more: true, next_cursor: "repeat" },
  ];
  const { sandbox, targets, requests } = hotReportHarness((_url, call) => responses[call - 1]);
  await sandbox.loadAdminHotReports("/api", targets);
  const result = await sandbox.loadAdminHotReports("/api", targets, { append: true });
  assert.equal(requests.length, 2);
  assert.deepEqual(Array.from(result, (item) => item.id), ["one"]);
  assert.equal(targets.hotReportPageState.nextCursor, "repeat");
  assert.match(targets.hotReportStatus.textContent, /分页状态异常/u);
});

test("an index-generation conflict restarts only the first page and discards old rows", async () => {
  const responses = [
    { items: [{ id: "old-one" }], total: 2, has_more: true, next_cursor: "old" },
    { status: 409, detail: "Hot report index changed." },
    { items: [{ id: "new-one" }], total: 2, has_more: true, next_cursor: "new" },
    { items: [{ id: "new-two" }], total: 2, has_more: false, next_cursor: "" },
  ];
  const { sandbox, targets, requests } = hotReportHarness((_url, call) => responses[call - 1]);
  await sandbox.loadAdminHotReports("/api", targets);
  await sandbox.loadAdminHotReports("/api", targets, { append: true });
  assert.equal(requests.length, 3);
  assert.equal(requests[2], "/api/hot-reports?limit=60");
  assert.deepEqual(Array.from(targets.hotReportPageState.items, (item) => item.id), ["new-one"]);
  assert.match(targets.hotReportStatus.textContent, /已更新/u);
  await sandbox.loadAdminHotReports("/api", targets, { append: true });
  assert.deepEqual(Array.from(targets.hotReportPageState.items, (item) => item.id), ["new-one", "new-two"]);
  assert.equal(requests.length, 4);
});

test("a persistent generation conflict makes no unbounded retries", async () => {
  const { sandbox, targets, requests } = hotReportHarness(() => ({ status: 409, detail: "changed again" }));
  const result = await sandbox.loadAdminHotReports("/api", targets);
  assert.equal(requests.length, 2);
  assert.equal(result.length, 0);
  assert.match(targets.hotReportStatus.className, /error/u);
});

test("post-upload refresh waits out an earlier preview read and then reads the updated index", async () => {
  let release;
  const { sandbox, targets, requests } = hotReportHarness(async (_url, call) => {
    if (call === 1) await new Promise((resolve) => { release = resolve; });
    return { items: [{ id: call === 1 ? "old" : "uploaded" }], total: 1, has_more: false };
  });
  const initial = sandbox.loadAdminHotReports("/api", targets);
  await new Promise(setImmediate);
  const afterUpload = sandbox.loadAdminHotReports("/api", targets, { forceRefresh: true });
  const concurrentRefresh = sandbox.loadAdminHotReports("/api", targets, { forceRefresh: true });
  assert.equal(requests.length, 1);
  release();
  await Promise.all([initial, afterUpload, concurrentRefresh]);
  assert.equal(requests.length, 2, "one fresh read must follow the completed write");
  assert.deepEqual(Array.from(targets.hotReportPageState.items, (item) => item.id), ["uploaded"]);
  assert.equal(targets.hotReportLoadPromise, null);
  assert.equal(targets.hotReportRefreshPromise, null);
});

test("a second upload during a queued refresh requires another read after that mutation", async () => {
  const releases = [];
  const { sandbox, targets, requests } = hotReportHarness(async (_url, call) => {
    if (call < 3) await new Promise((resolve) => { releases[call - 1] = resolve; });
    return { items: [{ id: `generation-${call}` }], total: 1, has_more: false };
  });
  const initial = sandbox.loadAdminHotReports("/api", targets);
  await new Promise(setImmediate);
  const afterFirstUpload = sandbox.loadAdminHotReports("/api", targets, { forceRefresh: true });
  releases[0]();
  await new Promise(setImmediate);
  assert.equal(requests.length, 2, "first upload's queued refresh is now in flight");
  const afterSecondUpload = sandbox.loadAdminHotReports("/api", targets, { forceRefresh: true });
  const sameMutationRefresh = sandbox.loadAdminHotReports("/api", targets, { forceRefresh: true });
  assert.equal(requests.length, 2, "second upload waits for the older read to finish");
  releases[1]();
  await Promise.all([initial, afterFirstUpload, afterSecondUpload, sameMutationRefresh]);
  assert.equal(requests.length, 3, "the second upload must not reuse a GET started before it");
  assert.deepEqual(Array.from(targets.hotReportPageState.items, (item) => item.id), ["generation-3"]);
  assert.equal(targets.hotReportLoadPromise, null);
  assert.equal(targets.hotReportRefreshPromise, null);
  assert.equal(targets.hotReportRefreshSource, null);
});
