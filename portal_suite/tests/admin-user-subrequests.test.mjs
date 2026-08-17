import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const [{ default: worker }, app] = await Promise.all([
  import(workerPath),
  readFile(appPath, "utf8"),
]);

const AUTH_SECRET = "admin-user-subrequest-test-secret";
const SUPABASE_URL = "https://database.admin-user-subrequest.test";
const ADMIN = Object.freeze({
  id: "000-admin",
  username: "admin-a",
  email: "admin-a@users.portal.example.invalid",
  email_is_generated: true,
  site_origin: "portal",
  registered_site: "portal",
  source_site: "portal",
  created_at: "2026-07-01T00:00:00.000Z",
  updated_at: "2026-08-17T00:00:00.000Z",
  last_login_at: "2026-08-17T00:00:00.000Z",
});

let activeSupabaseRows = [];
let activeExternalRequests = [];

function jsonResponse(body) {
  return new Response(JSON.stringify(body), {
    status: 200,
    headers: { "content-type": "application/json" },
  });
}

globalThis.fetch = async (input) => {
  const url = new URL(input instanceof Request ? input.url : String(input));
  activeExternalRequests.push(url.toString());
  assert.equal(url.origin, SUPABASE_URL, `unexpected external request: ${url}`);

  if (url.pathname === "/rest/v1/site_users") {
    const usernameFilter = String(url.searchParams.get("username") || "");
    if (usernameFilter.startsWith("eq.")) {
      const username = usernameFilter.slice(3);
      return jsonResponse(activeSupabaseRows.filter((row) => row.username === username).slice(0, 1));
    }

    const cursorFilter = String(url.searchParams.get("id") || "");
    const cursor = cursorFilter.startsWith("gt.") ? cursorFilter.slice(3) : "";
    const limit = Math.max(1, Number(url.searchParams.get("limit") || 500));
    const rows = activeSupabaseRows
      .filter((row) => !cursor || row.id > cursor)
      .sort((left, right) => left.id.localeCompare(right.id))
      .slice(0, limit);
    return jsonResponse(rows);
  }

  if (url.pathname === "/rest/v1/user_entitlements") {
    assert.doesNotMatch(
      String(url.searchParams.get("select") || ""),
      /(?:^|,)paddle_last_(?:event_id|occurred_at)(?:,|$)/u,
      "the admin export must remain compatible with production schemas without Paddle event-version columns",
    );
    return jsonResponse([]);
  }
  throw new Error(`unexpected Supabase path: ${url.pathname}`);
};

class CountingR2 {
  constructor() {
    this.events = [];
  }

  async get(key) {
    this.events.push({ op: "get", key });
    return null;
  }

  async list(options = {}) {
    this.events.push({ op: "list", key: String(options.prefix || "") });
    return { objects: [], truncated: false };
  }

  async put(key) {
    this.events.push({ op: "put", key });
    return { key, etag: `etag-${key}` };
  }
}

function userRows(total) {
  return [ADMIN, ...Array.from({ length: Math.max(0, total - 1) }, (_value, index) => {
    const suffix = String(index + 1).padStart(4, "0");
    const timestamp = `2026-08-${String((index % 16) + 1).padStart(2, "0")}T00:00:00.000Z`;
    return {
      id: `user-${suffix}`,
      username: `user-${suffix}`,
      email: `user-${suffix}@example.invalid`,
      email_is_generated: false,
      site_origin: "portal",
      registered_site: "portal",
      source_site: "portal",
      created_at: timestamp,
      updated_at: timestamp,
      last_login_at: timestamp,
    };
  })];
}

function userToken(user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    iat: now,
    exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", AUTH_SECRET)
    .update(`portal:account-token:v1:${body}`)
    .digest("base64url");
  return `${body}.${signature}`;
}

async function readLiveUsers(total) {
  activeSupabaseRows = userRows(total);
  activeExternalRequests = [];
  const bucket = new CountingR2();
  const response = await worker.fetch(new Request("https://worker.test/account-admin/users-export", {
    headers: { authorization: `Bearer ${userToken(ADMIN)}` },
  }), {
    REPORT_BUCKET: bucket,
    AUTH_SECRET,
    ACCOUNT_STORE_MODE: "supabase",
    SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY: "test-service-role-key",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  }, { waitUntil() {} });
  const body = await response.json();
  return {
    response,
    body,
    externalRequests: [...activeExternalRequests],
    r2Events: bucket.events,
  };
}

function entitlementRequests(result) {
  return result.externalRequests.filter((value) => new URL(value).pathname === "/rest/v1/user_entitlements");
}

test("live admin users bulk-load entitlements with a constant external request count", async () => {
  const small = await readLiveUsers(5);
  const large = await readLiveUsers(60);

  assert.equal(small.response.status, 200, JSON.stringify(small.body));
  assert.equal(large.response.status, 200, JSON.stringify(large.body));
  assert.ok(Array.isArray(small.body.users));
  assert.ok(Array.isArray(large.body.users));
  assert.equal(small.body.users.length, 5);
  assert.equal(large.body.users.length, 60);
  assert.equal(new Set(large.body.users.map((user) => user.email)).size, 60);

  const smallEntitlements = entitlementRequests(small);
  const largeEntitlements = entitlementRequests(large);
  assert.equal(smallEntitlements.length, 1, "small export must bulk-load entitlements once");
  assert.equal(largeEntitlements.length, 1, "large export must bulk-load entitlements once");
  assert.equal(
    large.externalRequests.length,
    small.externalRequests.length,
    `external calls grew with users: small=${small.externalRequests.length} large=${large.externalRequests.length}`,
  );
  assert.ok(
    large.externalRequests.length < 50,
    `large export exceeded the Workers Free external subrequest budget: ${large.externalRequests.length}`,
  );
  assert.ok(
    large.r2Events.length > small.r2Events.length,
    "canonical disabled/access state must still be verified per user in R2",
  );
  assert.ok(
    large.r2Events.length < 1000,
    `large export exceeded the separate Workers Free internal-service subrequest budget: ${large.r2Events.length}`,
  );
});

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

function verificationRenderer(cachedUsers) {
  return vm.runInNewContext(`(${extractFunction(app, "renderAdminUsersVerificationState")})`, {
    accountAdminUsersByEmail: new Map(cachedUsers.map((user) => [user.email, user])),
    escapeHtml(value) { return String(value || ""); },
  });
}

test("a failed live verification preserves cached admin user rows", () => {
  const cachedMarkup = "<tr><td>cached-user@example.invalid</td></tr>";
  const targets = {
    userCount: { textContent: "1 users" },
    users: { innerHTML: cachedMarkup },
    usersNotice: { hidden: true, textContent: "", className: "" },
  };
  const renderVerification = verificationRenderer([{ email: "cached-user@example.invalid" }]);

  renderVerification(targets, "最新用户状态读取失败，请稍后重试。", "error");

  assert.equal(targets.users.innerHTML, cachedMarkup, "a transient live failure must not erase cached rows");
  assert.match(targets.userCount.textContent, /1/u);
  assert.equal(targets.usersNotice.hidden, false);
  assert.match(targets.usersNotice.textContent, /读取失败/u);
  assert.match(targets.usersNotice.className, /error/u);
});

test("a failed first live verification still renders an actionable empty state", () => {
  const targets = {
    userCount: { textContent: "" },
    users: { innerHTML: "" },
    usersNotice: { hidden: true, textContent: "", className: "" },
  };
  const renderVerification = verificationRenderer([]);

  renderVerification(targets, "最新用户状态读取失败，请稍后重试。", "error");

  assert.match(targets.users.innerHTML, /读取失败/u);
  assert.equal(targets.userCount.textContent, "未核验");
  assert.equal(targets.usersNotice.hidden, false);
});
