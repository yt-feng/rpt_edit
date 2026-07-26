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
