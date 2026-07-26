import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "kc_desk_notes/site_src/assets/app.js");
const activityPath = path.join(root, "kc_desk_notes/site_src/activity.html");
const xlsxPath = path.join(root, "kc_desk_notes/site_src/assets/xlsx-export.js");
const [app, activity] = await Promise.all([
  readFile(appPath, "utf8"),
  readFile(activityPath, "utf8"),
]);

function extractFunction(source, name) {
  const functionStart = source.indexOf(`function ${name}(`);
  assert.ok(functionStart >= 0, `${name} must exist`);
  const start = source.slice(Math.max(0, functionStart - 6), functionStart) === "async "
    ? functionStart - 6
    : functionStart;
  const bodyStart = source.indexOf("{", source.indexOf(")", functionStart));
  assert.ok(bodyStart >= 0, `${name} must have a body`);
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

function adminTargets() {
  return {
    status: { className: "", textContent: "" },
    refresh: { disabled: false },
    picks: { innerHTML: "" },
    wechatSchedule: { innerHTML: "" },
    files: { innerHTML: "" },
    analytics: { innerHTML: "" },
  };
}

function loadSummaryFunction(fetchAccountAdminSummary) {
  const sandbox = {
    accountAdminLastSummary: null,
    accountAdminRefreshTimer: null,
    clearTimeout() {},
    document: { getElementById() { return null; } },
    fetchAccountAdminSummary,
    mergeAccountAdminSummaryWithLast(data) { return data; },
    renderAccountAdminSummary() {},
    setTimeout() { return 1; },
  };
  return vm.runInNewContext(`(${extractFunction(app, "loadAccountAdminSummary")})`, sandbox);
}

function historyCollector() {
  return vm.runInNewContext(`(${extractFunction(app, "collectAnalyticsHistoryPages")})`, {
    ANALYTICS_HISTORY_EXPORT_MAX_PAGES: 10000,
    ANALYTICS_HISTORY_EXPORT_MAX_ROWS: 1048575,
  });
}

test("admin export asset and activity export control are shipped", async () => {
  await access(xlsxPath);
  assert.match(activity, /id="analyticsHistoryExportAll"/u);
  assert.match(app, /import\(versionedSiteAssetUrl\("assets\/xlsx-export\.js"\)\)/u);
  assert.match(app, /account-admin\/users-export/u);
});

test("admin summary loader returns fresh data and propagates export failures", async () => {
  const payload = { module_status: {}, users: [{ email: "fresh@example.com" }] };
  const loadSuccess = loadSummaryFunction(async (_workerUrl, options) => {
    assert.equal(options.forceRefresh, true);
    assert.equal(options.throwOnError, true);
    return payload;
  });
  const targets = adminTargets();
  assert.equal(
    await loadSuccess("https://worker.example", targets, { forceRefresh: true, throwOnError: true }),
    payload,
  );
  assert.equal(targets.refresh.disabled, false);

  const failure = Object.assign(new Error("summary unavailable"), { status: 503 });
  const loadFailure = loadSummaryFunction(async () => { throw failure; });
  await assert.rejects(
    loadFailure("https://worker.example", adminTargets(), { throwOnError: true }),
    /summary unavailable/u,
  );

  const exportFunction = extractFunction(app, "exportAdminUsersToExcel");
  assert.match(exportFunction, /fetchFreshAdminUsers\(workerUrl\)/u);
  assert.doesNotMatch(exportFunction, /loadAccountAdminSummary/u);

  const summaryFunction = extractFunction(app, "loadAccountAdminSummary");
  assert.match(
    summaryFunction,
    /backgroundRetry: true[\s\S]*loadFreshAdminUsers\(workerUrl, targets\)/u,
    "the delayed summary retry must restore live users instead of leaving a stale snapshot",
  );
});

test("full-history export ignores current page filters", () => {
  const createParams = vm.runInNewContext(`(${extractFunction(app, "analyticsHistoryExportParams")})`, {
    URLSearchParams,
  });
  const params = createParams();
  assert.equal(params.toString(), "page_size=200");
  for (const name of ["type", "q", "start_date", "end_date", "cursor"]) {
    assert.equal(params.has(name), false, `${name} must not constrain the all-history export`);
  }
  const exportFunction = extractFunction(app, "exportAllHistory");
  assert.match(exportFunction, /analyticsHistoryExportParams\(\)/u);
  assert.doesNotMatch(exportFunction, /historySearchParams/u);
});

test("full-history collection follows empty filtered pages and removes duplicate event ids", async () => {
  const collect = historyCollector();
  const cursors = [];
  const progress = [];
  const pages = new Map([
    ["", { events: [], scanned_count: 100, has_more: true, next_cursor: "cursor-a" }],
    ["cursor-a", {
      events: [{ id: "event-1" }, { id: "event-2" }],
      scanned_count: 100,
      has_more: true,
      next_cursor: "cursor-b",
    }],
    ["cursor-b", {
      events: [{ id: "event-2" }, { id: "event-3" }],
      scanned_count: 2,
      has_more: false,
      next_cursor: "",
    }],
  ]);

  const result = await collect(async (cursor) => {
    cursors.push(cursor);
    return pages.get(cursor);
  }, {
    onProgress(value) { progress.push({ ...value }); },
  });

  assert.deepEqual(cursors, ["", "cursor-a", "cursor-b"]);
  assert.deepEqual(Array.from(result.events, (event) => event.id), ["event-1", "event-2", "event-3"]);
  assert.equal(result.pageCount, 3);
  assert.equal(result.scannedCount, 202);
  assert.equal(result.duplicateCount, 1);
  assert.deepEqual(Array.from(progress, (value) => value.pageCount), [1, 2, 3]);
});

test("full-history collection rejects cursor loops and inconsistent pagination", async () => {
  const collect = historyCollector();
  await assert.rejects(
    collect(async (cursor) => ({
      events: [],
      scanned_count: 1,
      has_more: true,
      next_cursor: cursor || "cursor-a",
    })),
    /游标发生循环/u,
  );
  await assert.rejects(
    collect(async () => ({ events: [], scanned_count: 1, has_more: true, next_cursor: "" })),
    /没有返回下一页游标/u,
  );
  await assert.rejects(
    collect(async () => ({ events: [], scanned_count: 1, has_more: false, next_cursor: "cursor-a" })),
    /分页状态不一致/u,
  );
});

test("full-history collection fails instead of silently truncating page or row limits", async () => {
  const collect = historyCollector();
  let pageCalls = 0;
  await assert.rejects(
    collect(async () => {
      pageCalls += 1;
      return { events: [], scanned_count: 1, has_more: true, next_cursor: `cursor-${pageCalls}` };
    }, { maxPages: 2 }),
    /已读取 2 批仍未结束/u,
  );
  assert.equal(pageCalls, 2);

  await assert.rejects(
    collect(async () => ({
      events: [{ id: "event-1" }, { id: "event-2" }],
      scanned_count: 2,
      has_more: false,
      next_cursor: "",
    }), { maxRows: 1 }),
    /超过 Excel 的 1 条上限/u,
  );
});
