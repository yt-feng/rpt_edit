import assert from "node:assert/strict";
import { access, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const activityPath = path.join(root, "portal_suite/site_src/activity.html");
const xlsxPath = path.join(root, "portal_suite/site_src/assets/xlsx-export.js");
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
  assert.match(activity, /id="analyticsHistoryUser"/u);
  assert.match(activity, /id="analyticsHistoryUserOptions"/u);
  assert.match(app, /import\(versionedSiteAssetUrl\("assets\/xlsx-export\.js"\)\)/u);
  assert.match(app, /account-admin\/users-export/u);
  assert.match(app, /account-admin\/analytics-events-export/u);
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
    ANALYTICS_HISTORY_EXPORT_PAGE_SIZE: 50,
  });
  const params = createParams();
  assert.equal(params.toString(), "page_size=50");
  for (const name of ["type", "q", "start_date", "end_date", "cursor"]) {
    assert.equal(params.has(name), false, `${name} must not constrain the all-history export`);
  }
  const exportFunction = extractFunction(app, "exportAllHistory");
  assert.match(exportFunction, /analyticsHistoryExportParams\(\)/u);
  assert.doesNotMatch(exportFunction, /historySearchParams/u);
});

test("activity pagination uses one immutable filter snapshot per load", () => {
  const snapshotFilters = vm.runInNewContext(`(${extractFunction(app, "analyticsHistoryFilterSnapshot")})`);
  const filterKey = vm.runInNewContext(`(${extractFunction(app, "analyticsHistoryFilterKey")})`);
  const searchParams = vm.runInNewContext(`(${extractFunction(app, "analyticsHistorySearchParams")})`, {
    URLSearchParams,
  });
  const fields = {
    type: { value: "search" },
    user: { value: " xiaoyi " },
    query: { value: " Nomura " },
    startDate: { value: "2026-07-01" },
    endDate: { value: "2026-07-26" },
    pageSize: { value: "500.9" },
  };
  const snapshot = snapshotFilters(fields);
  fields.user.value = "another-user";
  fields.query.value = "changed while loading";
  fields.pageSize.value = "1";

  const params = searchParams(snapshot, { cursor: "cursor-a", pageSize: 37.8 });
  assert.equal(params.get("type"), "search");
  assert.equal(params.get("user"), "xiaoyi");
  assert.equal(params.get("q"), "Nomura");
  assert.equal(params.get("start_date"), "2026-07-01");
  assert.equal(params.get("end_date"), "2026-07-26");
  assert.equal(params.get("page_size"), "37");
  assert.equal(params.get("cursor"), "cursor-a");
  assert.equal(snapshot.pageSize, 200, "page size is clamped before the request starts");
  assert.notEqual(filterKey(snapshot), filterKey(snapshotFilters(fields)));

  const loadPage = extractFunction(app, "loadPage");
  assert.match(loadPage, /const loadFilters = \{ \.\.\.activeFilters \}/u);
  assert.match(loadPage, /analyticsHistorySearchParams\(loadFilters/u);
  assert.match(loadPage, /pageLoadController\.abort\(\)/u);
  assert.doesNotMatch(loadPage, /userFilter\.value|query\.value|pageSize\.value/u);

  const exportAll = extractFunction(app, "exportAllHistory");
  assert.match(exportAll, /exportInProgress = true;[\s\S]*updateHistoryNavigation\(\)/u);
  assert.match(exportAll, /exportInProgress = false;[\s\S]*updateHistoryNavigation\(\)/u);
  const init = extractFunction(app, "initAnalyticsHistory");
  assert.match(init, /pageLoadInProgress \|\| exportInProgress \|\| !nextCursor/u);
  assert.match(init, /pageLoadInProgress \|\| exportInProgress \|\| !cursorStack\.length/u);
});

test("activity filtered search returns the first matching batch and bounds empty auto-scan", () => {
  const shouldContinue = vm.runInNewContext(
    `(${extractFunction(app, "shouldContinueAnalyticsHistoryAutoScan")})`,
    { ANALYTICS_HISTORY_AUTO_SCAN_BATCH_LIMIT: 4 },
  );

  assert.equal(shouldContinue({
    autoScan: true,
    batchCount: 1,
    eventCount: 0,
    nextCursor: "cursor-a",
  }), true, "an empty first batch should continue looking for a nearby match");
  assert.equal(shouldContinue({
    autoScan: true,
    batchCount: 2,
    eventCount: 1,
    nextCursor: "cursor-b",
  }), false, "the first matching batch must render immediately instead of filling the requested page size");
  assert.equal(shouldContinue({
    autoScan: true,
    batchCount: 4,
    eventCount: 0,
    nextCursor: "cursor-c",
  }), false, "an empty filtered search must yield after four server batches");
  assert.equal(shouldContinue({
    autoScan: false,
    batchCount: 1,
    eventCount: 0,
    nextCursor: "cursor-d",
  }), false);

  const loadPage = extractFunction(app, "loadPage");
  assert.match(loadPage, /shouldContinueAnalyticsHistoryAutoScan/u);
  assert.doesNotMatch(loadPage, /events\.length >= targetCount \|\| !batchNextCursor/u);
});

test("activity history does not wait for the user-option export before loading events", () => {
  const init = extractFunction(app, "initAnalyticsHistory");
  assert.match(
    init,
    /loadAnalyticsHistoryUserOptions\(workerUrl, userFilter, userOptions\)\.catch[\s\S]*await loadPage\(\{ reset: true \}\)/u,
  );
  assert.doesNotMatch(init, /await loadAnalyticsHistoryUserOptions/u);
});

test("full-history collection follows empty filtered pages and removes duplicate event ids", async () => {
  const collect = historyCollector();
  const cursors = [];
  const progress = [];
  const pages = new Map([
    ["", { events: [], scanned_count: 100, skipped_count: 1, has_more: true, next_cursor: "cursor-a" }],
    ["cursor-a", {
      events: [{ id: "event-1" }, { id: "event-2" }],
      scanned_count: 100,
      has_more: true,
      next_cursor: "cursor-b",
    }],
    ["cursor-b", {
      events: [{ id: "event-2" }, { id: "event-3" }],
      scanned_count: 2,
      skipped_count: 2,
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
  assert.equal(result.skippedCount, 3);
  assert.deepEqual(Array.from(progress, (value) => value.pageCount), [1, 2, 3]);
  assert.deepEqual(Array.from(progress, (value) => value.skippedCount), [1, 1, 3]);
});

test("full-history export preserves a bounded non-JSON Cloudflare diagnostic", () => {
  const createError = vm.runInNewContext(`(${extractFunction(app, "analyticsHistoryExportResponseError")})`, {
    Error,
    Number,
    String,
  });
  const response = {
    status: 503,
    statusText: "Service Unavailable",
    headers: { get(name) { return name === "cf-ray" ? "ray-123-SHA" : ""; } },
  };
  const error = createError(response, "<html><body>upstream temporarily unavailable</body></html>");
  assert.equal(error.status, 503);
  assert.equal(error.retryable, true);
  assert.match(error.message, /503/u);
  assert.match(error.message, /upstream temporarily unavailable/u);
  assert.match(error.message, /CF-Ray ray-123-SHA/u);
  assert.ok(error.message.length < 400);
});

test("full-history collection retries a transient page in place without losing prior rows", async () => {
  const collect = historyCollector();
  const calls = [];
  const retries = [];
  const delays = [];
  let twelfthPageAttempts = 0;

  const result = await collect(async (cursor, pageNumber, attempt) => {
    calls.push({ cursor, pageNumber, attempt });
    if (pageNumber <= 11) {
      return {
        events: Array.from({ length: 200 }, (_value, index) => ({
          id: `event-${(pageNumber - 1) * 200 + index + 1}`,
        })),
        scanned_count: 200,
        has_more: true,
        next_cursor: `cursor-${pageNumber}`,
      };
    }
    twelfthPageAttempts += 1;
    if (twelfthPageAttempts < 3) {
      throw Object.assign(new Error("temporary worker deployment"), { status: 503, retryable: true });
    }
    return {
      events: Array.from({ length: 5 }, (_value, index) => ({ id: `event-${2201 + index}` })),
      scanned_count: 5,
      has_more: false,
      next_cursor: "",
    };
  }, {
    maxAttemptsPerPage: 4,
    retryDelayMs: 800,
    sleep(delay) { delays.push(delay); },
    onRetry(progress) { retries.push({ ...progress, error: undefined }); },
  });

  assert.equal(result.events.length, 2205);
  assert.equal(result.pageCount, 12);
  assert.equal(result.scannedCount, 2205);
  assert.equal(twelfthPageAttempts, 3);
  assert.deepEqual(delays, [800, 1600]);
  assert.deepEqual(retries.map((value) => [value.pageNumber, value.nextAttempt, value.eventCount]), [
    [12, 2, 2200],
    [12, 3, 2200],
  ]);
  assert.equal(calls.filter((value) => value.pageNumber === 1).length, 1, "retry must not restart at page one");
  assert.equal(calls.filter((value) => value.pageNumber === 12).length, 3);
  assert.ok(calls.filter((value) => value.pageNumber === 12).every((value) => value.cursor === "cursor-11"));
});

test("full-history collection does not retry permission failures", async () => {
  const collect = historyCollector();
  let calls = 0;
  await assert.rejects(
    collect(async () => {
      calls += 1;
      throw Object.assign(new Error("Please log in."), { status: 403, retryable: false });
    }, {
      maxAttemptsPerPage: 4,
      sleep() { throw new Error("403 must not sleep or retry"); },
    }),
    /Please log in/u,
  );
  assert.equal(calls, 1);
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
