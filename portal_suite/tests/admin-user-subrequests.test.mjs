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
let activeEntitlementRows = [];
let activeExternalRequests = [];
let activePageCap = Number.POSITIVE_INFINITY;

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
      .slice(0, Math.min(limit, activePageCap));
    return jsonResponse(rows);
  }

  if (url.pathname === "/rest/v1/user_entitlements") {
    const select = String(url.searchParams.get("select") || "");
    assert.doesNotMatch(
      select,
      /(?:^|,)paddle_last_(?:event_id|occurred_at)(?:,|$)/u,
      "the admin export must remain compatible with production schemas without Paddle event-version columns",
    );
    assert.match(select, /(?:^|,)id(?:,|$)/u, "the admin export must select a unique pagination key");
    assert.equal(url.searchParams.get("order"), "id.asc");
    const after = String(url.searchParams.get("id") || "").replace(/^gt\./u, "");
    const emailFilter = String(url.searchParams.get("email") || "");
    const emails = emailFilter.startsWith("in.") ? JSON.parse(`[${emailFilter.slice(4, -1)}]`) : null;
    return jsonResponse(activeEntitlementRows.filter((row) =>
      (!after || row.id > after) && (!emails || emails.includes(row.email)),
    ).slice(0, Math.min(Number(url.searchParams.get("limit") || 500), activePageCap)));
  }
  throw new Error(`unexpected Supabase path: ${url.pathname}`);
};

class CountingR2 {
  constructor(rows = new Map(), pageCap = Infinity) {
    this.events = [];
    this.rows = rows;
    this.pageCap = pageCap;
  }

  async get(key) {
    this.events.push({ op: "get", key });
    const value = this.rows.get(key);
    return value ? { etag: `etag-${key}`, text: async () => JSON.stringify(value) } : null;
  }

  async list(options = {}) {
    this.events.push({ op: "list", key: String(options.prefix || "") });
    const keys = [...this.rows.keys()].filter((key) => key.startsWith(options.prefix)).sort();
    const offset = Number(options.cursor || 0);
    const objects = keys.slice(offset, offset + Math.min(options.limit || 1000, this.pageCap)).map((key) => ({ key }));
    const next = offset + objects.length;
    return next < keys.length ? { objects, truncated: true, cursor: String(next) } : { objects, truncated: false };
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

async function readLiveUsers(total, rows = userRows(total)) {
  activeSupabaseRows = rows;
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

function verificationRenderer() {
  return vm.runInNewContext(`(${extractFunction(app, "renderAdminUsersVerificationState")})`, {
    escapeHtml(value) { return String(value || ""); },
  });
}

test("a failed live verification preserves cached admin user rows", () => {
  const cachedMarkup = "<tr><td>cached-user@example.invalid</td></tr>";
  const targets = {
    userDirectory: new Map([["cached-user@example.invalid", { email: "cached-user@example.invalid" }]]),
    usersComplete: true,
    userCount: { textContent: "全部 1 位用户" },
    users: { innerHTML: cachedMarkup },
    usersNotice: { hidden: true, textContent: "", className: "" },
  };
  const renderVerification = verificationRenderer();

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
  const renderVerification = verificationRenderer();

  renderVerification(targets, "最新用户状态读取失败，请稍后重试。", "error");

  assert.match(targets.users.innerHTML, /读取失败/u);
  assert.equal(targets.userCount.textContent, "未核验");
  assert.equal(targets.usersNotice.hidden, false);
});


async function readPaginatedUsers(total, pageCap = Infinity, rows = userRows(total), objects = new Map()) {
  activeSupabaseRows = rows;
  activePageCap = pageCap;
  const all = [];
  const calls = [];
  let cursor = "";
  let r2Calls = 0;
  do {
    const bucket = new CountingR2(objects);
    activeExternalRequests = [];
    const query = new URLSearchParams({ page_size: "100" });
    if (cursor) query.set("cursor", cursor);
    const response = await worker.fetch(new Request(`https://worker.test/account-admin/users?${query}`, {
      headers: { authorization: `Bearer ${userToken(ADMIN)}` },
    }), {
      REPORT_BUCKET: bucket, AUTH_SECRET, ACCOUNT_STORE_MODE: "supabase", SUPABASE_URL,
      SUPABASE_SERVICE_ROLE_KEY: "test-service-role-key", ALLOWED_ORIGIN: "https://portal.example.invalid",
    }, { waitUntil() {} });
    const body = await response.json();
    assert.equal(response.status, 200, JSON.stringify(body));
    assert.equal(body.verified, true);
    assert.equal(body.complete, !body.has_more);
    assert.equal(Boolean(body.next_cursor), body.has_more);
    r2Calls += bucket.events.length;
    assert.ok(bucket.events.length < 1000, `R2 per-request budget exceeded: ${bucket.events.length}`);
    assert.ok(activeExternalRequests.length < 50);
    assert.ok(body.users.length <= 100);
    all.push(...body.users);
    calls.push({ count: body.users.length, complete: body.complete });
    assert.ok(calls.length < 30, "pagination must terminate");
    assert.notEqual(body.next_cursor || "completed", cursor || "start");
    cursor = body.next_cursor;
  } while (cursor);
  activePageCap = Number.POSITIVE_INFINITY;
  return { all, calls, r2Calls };
}

test("624 live users load completely in bounded requests without stale snapshots", async () => {
  const { all, calls } = await readPaginatedUsers(624);
  assert.equal(all.length, 624);
  assert.equal(new Set(all.map((user) => user.email)).size, 624);
  assert.equal(calls.length, 8, "seven data pages plus an empty completion page");
  assert.equal(calls[0].count, 100);
  assert.equal(calls[0].complete, false);
  assert.equal(calls.at(-1).complete, true);
  assert.ok(all.every((user) => user.newsfeed && user.newsfeed.mode === "auto"));
});

test("a server-clamped short page cannot masquerade as the full user list", async () => {
  const { all, calls } = await readPaginatedUsers(624, 61);
  assert.equal(all.length, 624);
  assert.equal(new Set(all.map((user) => user.id)).size, 624);
  assert.equal(calls[0].count, 61);
  assert.equal(calls[0].complete, false);
  assert.equal(calls.at(-1).count, 0);
});

test("private canonical pagination and export retain distinct legacy-brand account identities", async () => {
  const rows = userRows(125);
  Object.assign(rows[12], { username: "twotigers-reader", email: "twotigers-reader@example.invalid" });
  Object.assign(rows[112], { username: "macro-gate-reader", email: "macro-gate-reader@example.invalid" });
  Object.assign(rows[124], { username: "beta-reader", email: "beta-reader@example.invalid" });
  const { all, calls } = await readPaginatedUsers(rows.length, 61, rows);
  assert.equal(calls.length, 4, "short pages still finish with a verified empty page");
  const byEmail = new Map(all.map((user) => [user.email, user]));
  assert.equal(byEmail.size, rows.length, "public redaction must not collapse private admin identities");
  for (const source of [rows[12], rows[112], rows[124], ADMIN]) {
    const user = byEmail.get(source.email);
    assert.deepEqual({ id: user.id, username: user.username, email: user.email },
      { id: source.id, username: source.username, email: source.email });
  }
  const exported = await readLiveUsers(rows.length, rows);
  assert.equal(exported.response.status, 200);
  assert.match(exported.response.headers.get("Cache-Control"), /no-store/);
  assert.equal(exported.body.complete, true);
  assert.deepEqual(new Set(exported.body.users.map((user) => user.email)), new Set(byEmail.keys()));
});

test("patching one user never promotes a partial snapshot or resets directory freshness", async () => {
  const source = await readFile(workerPath, "utf8");
  const previous = {
    updated_at: "2026-01-01T00:00:00.000Z", partial: true,
    data: { users: [{ email: "cached@example.invalid" }], complete: false },
  };
  let written;
  const patch = vm.runInNewContext(`(${extractFunction(source, "patchAdminUsersSnapshotUser")})`, {
    ADMIN_USERS_SNAPSHOT_KEY: "snapshot", Date,
    async safeR2GetJson() { return previous; },
    hasAdminSnapshot(snapshot) { return Boolean(snapshot && snapshot.data); },
    normalizeEmail(value) { return String(value || "").toLowerCase(); },
    sortAdminVisibleUsers(users) { return users; },
    async writeAdminSnapshot(_env, _key, data, extra) { written = { data, ...extra }; },
  });
  assert.equal(await patch({}, { email: "new@example.invalid" }), true);
  assert.equal(written.partial, true);
  assert.equal(written.data.complete, false);
  assert.equal(written.updated_at, previous.updated_at);
  assert.equal(written.data.users.length, 2);
});

const recordKey = (...parts) => ["_account", ...parts.map(encodeURIComponent)].join("/");

async function readDirectory(bucket, user = ADMIN) {
  return worker.fetch(new Request("https://worker.test/account-admin/users?view=directory", {
    headers: user ? { authorization: `Bearer ${userToken(user)}` } : {},
  }), {
    REPORT_BUCKET: bucket, AUTH_SECRET, ACCOUNT_STORE_MODE: "supabase", SUPABASE_URL,
    SUPABASE_SERVICE_ROLE_KEY: "test-service-role-key", ALLOWED_ORIGIN: "https://portal.example.invalid",
  }, { waitUntil() {} });
}

test("directory returns all live, canonical users with the same rights and far fewer R2 reads", async () => {
  const rows = userRows(647);
  const granted = rows[614], newsfeed = rows[623], disabled = rows[645], legacy = rows[646];
  legacy.email = "twotigers-legacy@example.invalid";
  const updated = "2026-11-24T09:00:00Z";
  const expires = "2099-12-23T15:59:59.999Z";
  const objects = new Map([
    [recordKey("access", granted.email), {
      id: "test-access", email: granted.email, access_mode: "all", status: "active", lifetime: false,
      current_period_end: expires, duration_value: "1", download_limit: 0, download_count: 0, download_items: [],
      institutions: [], industries: [], page_ranges: [], updated_at: updated, change_id: "test-version",
    }],
    [recordKey("newsfeed-access", newsfeed.email), {
      email: newsfeed.email, user_id: newsfeed.id, mode: "enabled", expires_at: expires, updated_at: updated,
    }],
    [recordKey("user-state", "id", disabled.id), { user_id: disabled.id, email: disabled.email, disabled: true, updated_at: updated }],
    // The older disabled record continues to win over a newer active copy.
    [recordKey("user-state", "email", disabled.email), {
      email: disabled.email, user_id: disabled.id, disabled: false, updated_at: "2026-11-25T09:00:00Z",
    }],
    [recordKey("access", legacy.email), {
      id: "legacy-access", email: legacy.email, access_mode: "all", status: "active", lifetime: true,
      current_period_end: null, duration_value: "lifetime", download_limit: 0, download_count: 0, download_items: [],
      institutions: [], industries: [], page_ranges: [], updated_at: updated,
    }],
  ]);
  activeEntitlementRows = [{
    id: "ent-001", email: rows[600].email, plan: "annual", status: "active", lifetime: false, current_period_end: expires, updated_at: updated,
  }];

  try {
    const paginated = await readPaginatedUsers(rows.length, 61, rows, objects);
    activePageCap = 61;
    activeExternalRequests = [];
    const bucket = new CountingR2(objects, 1);
    const result = await readDirectory(bucket);
    const body = await result.json();
    assert.equal(result.status, 200, JSON.stringify(body).slice(0, 180));
    assert.match(result.headers.get("Cache-Control"), /private, no-store/u);
    assert.deepEqual([body.verified, body.complete, body.has_more, body.total], [true, true, false, rows.length]);
    const byEmail = new Map(body.users.map((user) => [user.email, user]));
    assert.equal(byEmail.size, rows.length);
    for (const prior of paginated.all) {
      const current = byEmail.get(prior.email);
      const stableState = (user) => user.role !== "super" ? user : {
        ...user, entitlement: { ...user.entitlement, updated_at: "" },
      };
      assert.deepEqual(stableState(current), stableState(prior), `directory permission mismatch for ${prior.id}`);
    }
    assert.equal(byEmail.get(disabled.email).disabled, true);
    assert.equal(byEmail.get(granted.email).effective_access.active, true);
    assert.equal(byEmail.get(newsfeed.email).newsfeed.source, "admin");
    assert.ok(bucket.events.filter(({ op }) => op === "list").length > 4, "short R2 pages must follow the cursor");
    assert.ok(bucket.events.length < 25, `bulk directory issued ${bucket.events.length} R2 calls`);
    assert.ok(paginated.r2Calls > 2500, `cursor scan issued ${paginated.r2Calls} R2 calls`);
    assert.ok(activeExternalRequests.length < 50);
    assert.ok(bucket.events.every(({ op }) => op !== "put"));
  } finally {
    activePageCap = Infinity;
    activeEntitlementRows = [];
  }
});

test("the fast directory refuses non-admins, corrupt records and a repeated storage cursor", async () => {
  activeSupabaseRows = userRows(5);
  const reader = activeSupabaseRows[1];
  for (const user of [null, reader]) {
    const bucket = new CountingR2();
    const response = await readDirectory(bucket, user);
    assert.equal(response.status, 403);
    assert.ok(!bucket.events.some(({ op }) => op === "list"));
    assert.ok(!Object.hasOwn(await response.json(), "users"));
  }
  const corrupt = new CountingR2(new Map([
    [recordKey("newsfeed-access", reader.email), { mode: "enabled", email: reader.email, user_id: "wrong-id" }],
  ]));
  const looping = new CountingR2();
  looping.list = async ({ prefix }) => ({ objects: [{ key: `${prefix}known` }], truncated: true, cursor: "repeated" });
  for (const bucket of [corrupt, looping]) {
    const response = await readDirectory(bucket);
    assert.equal(response.status, 409);
    assert.deepEqual(await response.json(), { code: "use_user_cursor" });
  }
});


test("a dense directory falls back before hydrating more stored records than fit in one request", async () => {
  activeSupabaseRows = userRows(430);
  const rows = new Map(activeSupabaseRows.slice(1).flatMap((user) =>
    ["id", "email"].map((kind) => [
      recordKey("user-state", kind, user[kind]), { user_id: user.id, email: user.email, disabled: false },
    ]),
  ));
  const bucket = new CountingR2(rows);
  const response = await readDirectory(bucket);
  assert.equal(response.status, 409);
  assert.deepEqual(await response.json(), { code: "use_user_cursor" });
  assert.ok(bucket.events.every(({ op, key }) => op === "list"
    || !key.startsWith("_account/user-state/") || key.endsWith(encodeURIComponent(ADMIN.id)) || key.endsWith(encodeURIComponent(ADMIN.email))));
});
