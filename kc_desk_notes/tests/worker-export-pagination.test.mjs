import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/kc-desk-notes-worker/src/index.js");
const worker = await readFile(workerPath, "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.ok(start >= 0, `${name} must exist`);
  const asyncStart = source.slice(Math.max(0, start - 6), start) === "async " ? start - 6 : start;
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(asyncStart, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function loadSupabasePaginator(fetchPage) {
  const sandbox = {
    ACCOUNT_ADMIN_EXPORT_MAX_USERS: 5000,
    ACCOUNT_ADMIN_EXPORT_PAGE_SIZE: 500,
    accountExportRowKey: vm.runInNewContext(`(${extractFunction(worker, "accountExportRowKey")})`),
    queryString(params) { return new URLSearchParams(params).toString(); },
    supabaseRequest: fetchPage,
  };
  return vm.runInNewContext(`(${extractFunction(worker, "listAllSupabaseAccountRows")})`, sandbox);
}

function loadR2Paginator() {
  const sandbox = {
    ACCOUNT_ADMIN_EXPORT_MAX_USERS: 5000,
    ACCOUNT_ADMIN_EXPORT_PAGE_SIZE: 500,
    accountBucket(env) { return env.bucket; },
    async r2GetJsonStrict(env, key) { return env.records.get(key) || null; },
  };
  return vm.runInNewContext(`(${extractFunction(worker, "listAllR2AccountRows")})`, sandbox);
}

function loadAnalyticsExportHandler(options = {}) {
  const sandbox = {
    URL,
    Date,
    Object,
    Set,
    TypeError,
    Error,
    ANALYTICS_PREFIX: "_analytics/events",
    ANALYTICS_BACKUP_PREFIX: "_analytics_backup/events",
    ANALYTICS_HISTORY_DEFAULT_PAGE_SIZE: 100,
    ANALYTICS_HISTORY_MAX_PAGE_SIZE: 200,
    ANALYTICS_HISTORY_READ_BATCH: 30,
    ANALYTICS_EXPORT_CURSOR_VERSION: 1,
    ANALYTICS_EXPORT_CURSOR_MAX_LENGTH: 4096,
    ANALYTICS_EXPORT_NATIVE_CURSOR_MAX_LENGTH: 2048,
    encodeAnalyticsHistoryCursor(value) {
      return Buffer.from(JSON.stringify(value), "utf8").toString("base64url");
    },
    decodeAnalyticsHistoryCursor(value) {
      try {
        return JSON.parse(Buffer.from(String(value || ""), "base64url").toString("utf8"));
      } catch (_error) {
        return null;
      }
    },
    async requireSuperUser() {
      if (options.authorized === false) throw new Error("Admin access denied.");
      return { username: "twotigers" };
    },
    jsonResponse(_request, _env, status, body) {
      return { status, async json() { return body; } };
    },
    async listAnalyticsEventDateRows(env) {
      return env.dateRows || [];
    },
  };
  for (const name of [
    "analyticsExportPhaseForRoot",
    "analyticsExportRootsForDateRow",
    "encodeAnalyticsExportCursor",
    "decodeAnalyticsExportCursor",
    "resolveAnalyticsExportPosition",
    "nextAnalyticsExportPosition",
    "analyticsExportMirrorKey",
    "readAnalyticsExportObject",
    "readAnalyticsExportObjects",
    "listAnalyticsExportPage",
    "publicAnalyticsEvent",
    "handleAccountAdminAnalyticsEventsExport",
  ]) {
    sandbox[name] = vm.runInNewContext(`(${extractFunction(worker, name)})`, sandbox);
  }
  return {
    handle: sandbox.handleAccountAdminAnalyticsEventsExport,
    encode(value) { return sandbox.encodeAnalyticsHistoryCursor(value); },
  };
}

function storedAnalyticsValue(value) {
  return {
    async text() {
      return typeof value === "string" ? value : JSON.stringify(value);
    },
  };
}

function analyticsExportBucket(records, calls = []) {
  return {
    async list({ prefix, limit, cursor }) {
      const keys = [...records.keys()].filter((key) => key.startsWith(prefix)).sort();
      const offset = cursor ? Number(String(cursor).replace(/^offset-/u, "")) : 0;
      const page = keys.slice(offset, offset + limit);
      const nextOffset = offset + page.length;
      const truncated = nextOffset < keys.length;
      calls.push({ prefix, limit, cursor: cursor || "", objectCount: page.length });
      return {
        objects: page.map((key) => ({ key })),
        truncated,
        cursor: truncated ? `offset-${nextOffset}` : undefined,
      };
    },
    async get(key) {
      return records.has(key) ? storedAnalyticsValue(records.get(key)) : null;
    },
  };
}

test("Supabase full-user pagination reads every page and rejects truncation", async () => {
  const calls = [];
  const pages = new Map([
    ["", [{ id: "a" }, { id: "b" }]],
    ["b", [{ id: "c" }]],
  ]);
  const list = loadSupabasePaginator(async (_env, _method, requestPath) => {
    const url = new URL(requestPath, "https://worker.test");
    assert.equal(url.searchParams.has("offset"), false, "user export must use keyset pagination");
    const cursor = String(url.searchParams.get("id") || "").replace(/^gt\./u, "");
    calls.push(cursor);
    return pages.get(cursor) || [];
  });
  const rows = await list({}, "site_users", { order: "id.asc" }, {
    pageSize: 2,
    maxRows: 3,
    keyFields: ["id"],
  });
  assert.deepEqual(calls, ["", "b"]);
  assert.deepEqual(Array.from(rows, (row) => row.id), ["a", "b", "c"]);

  const tooMany = loadSupabasePaginator(async (_env, _method, requestPath) => {
    const cursor = String(new URL(requestPath, "https://worker.test").searchParams.get("id") || "");
    return cursor ? [{ id: "c" }] : [{ id: "a" }, { id: "b" }];
  });
  await assert.rejects(
    tooMany({}, "site_users", {}, { pageSize: 2, maxRows: 2, keyFields: ["id"] }),
    /exceeds the 2-user hard limit/u,
  );
});

test("Supabase full-user pagination rejects a duplicate page with no progress", async () => {
  const list = loadSupabasePaginator(async () => [{ id: "a" }, { id: "b" }]);
  await assert.rejects(
    list({}, "site_users", {}, { pageSize: 2, maxRows: 4, keyFields: ["id"] }),
    /order did not advance/u,
  );
});

test("R2 full-user pagination deduplicates keys and rejects repeated cursors", async () => {
  const list = loadR2Paginator();
  const records = new Map([
    ["users/a", { id: "a" }],
    ["users/b", { id: "b" }],
  ]);
  const env = {
    records,
    bucket: {
      async list({ cursor }) {
        if (!cursor) return { objects: [{ key: "users/a" }], truncated: true, cursor: "next" };
        return { objects: [{ key: "users/a" }, { key: "users/b" }], truncated: false };
      },
    },
  };
  const rows = await list(env, "users/", { pageSize: 2, maxRows: 3 });
  assert.deepEqual(Array.from(rows, (row) => row.id), ["a", "b"]);

  const loopingEnv = {
    records,
    bucket: {
      async list() {
        return { objects: [{ key: "users/a" }], truncated: true, cursor: "next" };
      },
    },
  };
  await assert.rejects(
    list(loopingEnv, "users/", { pageSize: 1, maxRows: 3 }),
    /cursor repeated/u,
  );
});

test("analytics R2 object pagination rejects cursor loops", async () => {
  const list = vm.runInNewContext(`(${extractFunction(worker, "listAnalyticsEventKeysForRoot")})`, {
    ANALYTICS_HISTORY_R2_MAX_LIST_PAGES: 10,
  });
  const env = {
    REPORT_BUCKET: {
      async list() {
        return {
          objects: [{ key: "_analytics/events/2026-07-26/a.json" }],
          truncated: true,
          cursor: "next",
        };
      },
    },
  };
  await assert.rejects(
    list(env, "_analytics/events", "2026-07-26"),
    /cursor repeated/u,
  );
});

test("analytics R2 date pagination rejects cursor loops", async () => {
  const list = vm.runInNewContext(`(${extractFunction(worker, "listAnalyticsEventDatesForRoot")})`, {
    ANALYTICS_HISTORY_R2_MAX_LIST_PAGES: 10,
    analyticsDateFromPrefix: vm.runInNewContext(`(${extractFunction(worker, "analyticsDateFromPrefix")})`),
  });
  const env = {
    REPORT_BUCKET: {
      async list() {
        return {
          delimitedPrefixes: ["_analytics/events/2026-07-26/"],
          truncated: true,
          cursor: "next",
        };
      },
    },
  };
  await assert.rejects(
    list(env, "_analytics/events"),
    /cursor repeated/u,
  );
});

test("filtered analytics history rejects invalid and cross-filter cursors", () => {
  const decodeCursor = vm.runInNewContext(`(${extractFunction(worker, "decodeAnalyticsHistoryRequestCursor")})`, {
    ANALYTICS_HISTORY_CURSOR_MAX_LENGTH: 4096,
    decodeAnalyticsHistoryCursor(value) {
      try {
        return JSON.parse(Buffer.from(String(value || ""), "base64url").toString("utf8"));
      } catch (_error) {
        return null;
      }
    },
    TypeError,
  });
  const encode = (value) => Buffer.from(JSON.stringify(value), "utf8").toString("base64url");
  const signature = "search\u001fxiaoyi\u001fnomura\u001f2026-07-01\u001f2026-07-26";
  const valid = decodeCursor(encode({
    date: "2026-07-26",
    after_key: "2026-07-26T00-00-00.000Z-event.json",
    signature,
  }), signature);
  assert.equal(valid.date, "2026-07-26");
  assert.equal(valid.after_key, "2026-07-26T00-00-00.000Z-event.json");
  assert.equal(valid.signature, signature);

  assert.throws(() => decodeCursor("not-base64-json", signature), /Invalid analytics history cursor/u);
  assert.throws(() => decodeCursor(encode({
    date: "2026-07-26",
    after_key: "event.json",
    signature: `${signature}-different`,
  }), signature), /Invalid analytics history cursor/u);
  assert.throws(() => decodeCursor(encode({ date: "2026-07-26", signature }), signature), /Invalid analytics history cursor/u);
  assert.throws(() => decodeCursor("a".repeat(4097), signature), /Invalid analytics history cursor/u);

  const handler = extractFunction(worker, "handleAccountAdminAnalyticsEvents");
  assert.match(handler, /decodeAnalyticsHistoryRequestCursor/u);
  assert.match(handler, /cursor no longer matches stored history/u);
  assert.match(handler, /error instanceof TypeError \? 400 : 503/u);
});

test("analytics user filter keeps punctuation significant for exact identities", () => {
  const sandbox = {
    normalizeAnalyticsIdentity: vm.runInNewContext(`(${extractFunction(worker, "normalizeAnalyticsIdentity")})`),
    normalizeText(value) { return String(value || "").toLowerCase(); },
  };
  const matches = vm.runInNewContext(`(${extractFunction(worker, "analyticsHistoryEventMatches")})`, sandbox);
  const event = {
    type: "page_view",
    visitor_id: "visitor-1",
    user: { username: "Xiao.Yi", email: "xiao.yi@example.com" },
  };
  const baseFilters = { type: "", query: "" };

  assert.equal(matches(event, { ...baseFilters, user: " XIAO.YI@EXAMPLE.COM " }), true);
  assert.equal(matches(event, { ...baseFilters, user: "xiao-yi@example.com" }), false);
  assert.equal(matches(event, { ...baseFilters, user: "xiao-yi" }), false);
  assert.equal(matches(event, { ...baseFilters, user: "visitor-1" }), true);
});

test("analytics export uses native R2 cursors for more than 2200 events and scans both mirrors", async () => {
  const { handle } = loadAnalyticsExportHandler();
  const primaryRoot = "_analytics/events";
  const backupRoot = "_analytics_backup/events";
  const date = "2026-07-26";
  const records = new Map();
  const primaryCount = 2205;
  for (let index = 0; index < primaryCount; index += 1) {
    const suffix = `${String(index).padStart(5, "0")}.json`;
    const event = {
      id: `event-${index}`,
      ts: `2026-07-26T00:${String(index % 60).padStart(2, "0")}:00.000Z`,
      date,
      type: "page_view",
    };
    records.set(`${primaryRoot}/${date}/${suffix}`, event);
    records.set(`${backupRoot}/${date}/${suffix}`, event);
  }
  records.set(`${backupRoot}/${date}/backup-only.json`, {
    id: "event-backup-only",
    ts: "2026-07-26T23:59:59.000Z",
    date,
    type: "report_open",
  });
  const calls = [];
  const env = {
    dateRows: [{ date, prefix_roots: [primaryRoot, backupRoot] }],
    REPORT_BUCKET: analyticsExportBucket(records, calls),
  };

  const uniqueEvents = new Map();
  let cursor = "";
  let rawCount = 0;
  do {
    const query = new URLSearchParams({ page_size: "200" });
    if (cursor) query.set("cursor", cursor);
    const response = await handle({ url: `https://worker.test/account-admin/analytics-events-export?${query}` }, env);
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.ok(Array.isArray(body.events));
    assert.equal(typeof body.next_cursor, "string");
    assert.equal(typeof body.has_more, "boolean");
    assert.equal(typeof body.scanned_count, "number");
    rawCount += body.events.length;
    for (const event of body.events) uniqueEvents.set(event.id, event);
    cursor = body.next_cursor;
    assert.equal(body.has_more, Boolean(cursor));
  } while (cursor);

  assert.equal(rawCount, primaryCount * 2 + 1, "both mirrors must be scanned");
  assert.equal(uniqueEvents.size, primaryCount + 1, "the client can deduplicate mirrors and keep backup-only events");
  assert.ok(uniqueEvents.has("event-backup-only"));
  assert.equal(calls.length, Math.ceil(primaryCount / 200) + Math.ceil((primaryCount + 1) / 200));
  assert.ok(calls.every((call) => call.limit === 200 && call.objectCount <= 200));
  assert.equal(calls.filter((call) => !call.cursor).length, 2, "each mirror starts once instead of relisting the day");
});

test("analytics export falls back to the mirror and fails explicitly when both copies are unreadable", async () => {
  const { handle } = loadAnalyticsExportHandler();
  const primaryRoot = "_analytics/events";
  const backupRoot = "_analytics_backup/events";
  const date = "2026-07-26";
  const primaryKey = `${primaryRoot}/${date}/one.json`;
  const backupKey = `${backupRoot}/${date}/one.json`;
  const dateRows = [{ date, prefix_roots: [primaryRoot] }];

  const recoveredRecords = new Map([
    [primaryKey, "{not-json"],
    [backupKey, { id: "recovered", ts: "2026-07-26T01:00:00.000Z", date, type: "page_view" }],
  ]);
  const recovered = await handle({
    url: "https://worker.test/account-admin/analytics-events-export?page_size=200",
  }, {
    dateRows,
    REPORT_BUCKET: analyticsExportBucket(recoveredRecords),
  });
  assert.equal(recovered.status, 200);
  assert.deepEqual(Array.from((await recovered.json()).events, (event) => event.id), ["recovered"]);

  const broken = await handle({
    url: "https://worker.test/account-admin/analytics-events-export?page_size=200",
  }, {
    dateRows,
    REPORT_BUCKET: analyticsExportBucket(new Map([
      [primaryKey, "{not-json"],
      [backupKey, "[]"],
    ])),
  });
  assert.equal(broken.status, 503);
  assert.match((await broken.json()).detail, /unreadable in both storage mirrors/u);
});

test("analytics export fails closed for invalid, missing, and repeated cursors", async () => {
  const harness = loadAnalyticsExportHandler();
  const primaryRoot = "_analytics/events";
  const date = "2026-07-26";
  let listCalls = 0;
  const baseEnv = {
    dateRows: [{ date, prefix_roots: [primaryRoot] }],
    REPORT_BUCKET: {
      async list() {
        listCalls += 1;
        return { objects: [], truncated: false };
      },
      async get() { return null; },
    },
  };
  const invalidCursors = [
    harness.encode({ version: 2, date, phase: "primary", root: primaryRoot, native_cursor: "", at_start: true }),
    harness.encode({ version: 1, date, phase: "primary", root: primaryRoot, at_start: true }),
    harness.encode({ version: 1, date, phase: "backup", root: primaryRoot, native_cursor: "", at_start: true }),
    harness.encode({ version: 1, date, phase: "primary", root: primaryRoot, native_cursor: "next", at_start: true }),
  ];
  for (const cursor of invalidCursors) {
    const response = await harness.handle({
      url: `https://worker.test/account-admin/analytics-events-export?cursor=${encodeURIComponent(cursor)}`,
    }, baseEnv);
    assert.equal(response.status, 400);
  }
  assert.equal(listCalls, 0, "invalid cursors must be rejected before any object listing");

  const missing = await harness.handle({
    url: "https://worker.test/account-admin/analytics-events-export",
  }, {
    ...baseEnv,
    REPORT_BUCKET: {
      async list() { return { objects: [], truncated: true }; },
      async get() { return null; },
    },
  });
  assert.equal(missing.status, 503);
  assert.match((await missing.json()).detail, /did not return an R2 cursor/u);

  const repeatedCursor = harness.encode({
    version: 1,
    date,
    phase: "primary",
    root: primaryRoot,
    native_cursor: "loop",
    at_start: false,
  });
  const repeated = await harness.handle({
    url: `https://worker.test/account-admin/analytics-events-export?cursor=${encodeURIComponent(repeatedCursor)}`,
  }, {
    ...baseEnv,
    REPORT_BUCKET: {
      async list() { return { objects: [], truncated: true, cursor: "loop" }; },
      async get() { return null; },
    },
  });
  assert.equal(repeated.status, 503);
  assert.match((await repeated.json()).detail, /cursor repeated without progress/u);
});

test("analytics export route is super-only", async () => {
  assert.match(worker, /pathname === "\/account-admin\/analytics-events-export"/u);
  const handlerSource = extractFunction(worker, "handleAccountAdminAnalyticsEventsExport");
  assert.match(handlerSource, /requireSuperUser/u);
  const { handle } = loadAnalyticsExportHandler({ authorized: false });
  let listed = false;
  const response = await handle({
    url: "https://worker.test/account-admin/analytics-events-export",
  }, {
    dateRows: [],
    REPORT_BUCKET: {
      async list() { listed = true; return { objects: [], truncated: false }; },
      async get() { return null; },
    },
  });
  assert.equal(response.status, 403);
  assert.equal(listed, false);
});

test("worker exposes a super-only live user export route", () => {
  assert.match(worker, /pathname === "\/account-admin\/users-export"/u);
  const handler = extractFunction(worker, "handleAccountAdminUsersExport");
  assert.match(handler, /requireSuperUser/u);
  assert.match(handler, /loadAllAdminUsersForExport/u);
});

test("live user export merges current disabled, entitlement, and access state", async () => {
  const sandbox = {
    ACCOUNT_ADMIN_EXPORT_CONCURRENCY: 2,
    async listAllSiteUsersForExport() {
      return [{ id: "u1", email: "one@example.com" }, { id: "u2", email: "two@example.com" }];
    },
    mapWithConcurrency: vm.runInNewContext(`(${extractFunction(worker, "mapWithConcurrency")})`),
    async mergeSiteUserAdminState(_env, user) { return { ...user, disabled: user.id === "u2" }; },
    async findEntitlement(_env, email) { return { plan: email.startsWith("one") ? "NOVA" : "free" }; },
    async findAccessGrant(_env, email) { return { access_mode: email.startsWith("one") ? "all" : "none" }; },
    adminVisibleUser(user, entitlement, access) { return { user, entitlement, access }; },
  };
  const load = vm.runInNewContext(`(${extractFunction(worker, "loadAllAdminUsersForExport")})`, sandbox);
  const rows = await load({});
  assert.equal(rows.length, 2);
  assert.equal(rows[1].user.disabled, true);
  assert.equal(rows[0].entitlement.plan, "NOVA");
  assert.equal(rows[0].access.access_mode, "all");
});
