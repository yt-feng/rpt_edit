import assert from "node:assert/strict";
import test from "node:test";
import { createCustomerContentApi, CustomerContentApiError } from "../../workers/portal-suite-worker/src/customer-content-api.js";

const START = Date.parse("2026-10-12T12:00:00Z");
const ALL = ["reports:read", "reports:download", "artifacts:read"];

class MemoryR2 {
  rows = new Map(); sequence = 0; reads = []; writes = []; forceConflict = false;
  async get(key) {
    this.reads.push(key);
    const row = this.rows.get(key);
    return row ? { etag: row.etag, size: Buffer.byteLength(row.raw), body: new Response(row.raw).body } : null;
  }
  async put(key, raw, options = {}) {
    const previous = this.rows.get(key), condition = options.onlyIf;
    if (this.forceConflict || (condition?.etagMatches && previous?.etag !== condition.etagMatches)
      || (condition?.etagDoesNotMatch === "*" && previous)) return null;
    const row = { etag: `etag-${++this.sequence}`, raw };
    this.rows.set(key, row); this.writes.push({ key, raw, options });
    return { etag: row.etag };
  }
}

function fixture() {
  const bucket = new MemoryR2(), user = { id: "account-test-001", email: "reader@example.test", disabled: false };
  const other = { id: "account-test-002", email: "other@example.test", disabled: false };
  const f = { bucket, user, other, now: START, calls: [], commits: 0, cancelled: 0, member: true };
  const rows = [{ id: "r1", title: "First report", date: "2026-10-12", object_key: "_private/should-not-escape" }, { id: "r2", title: "Second report" }];
  const memberGate = context => {
    if (context.grant.access_mode === "membership" && !f.member) throw new CustomerContentApiError(403, "membership_required");
  };
  f.adapters = {
    bucket: () => bucket, now: () => f.now,
    currentUser: (_env, request) => request.headers.get("authorization") === "Bearer session" ? user
      : request.headers.get("authorization") === "Bearer other-session" ? other : null,
    requireAdmin: (_env, request) => request.headers.get("authorization") === "Bearer admin" ? { id: "two-tigers" } : null,
    findAccount: (_env, query) => [user, other].find(item => item.email === query.email && (!query.id || query.id === item.id)) || null,
    async listReports(_env, query, context) {
      f.calls.push(["list", query, context.grant]); memberGate(context);
      return { items: rows.slice(0, query.limit), next_cursor: null };
    },
    async getReport(_env, query, context) { memberGate(context); return rows.find(row => row.id === query.reportId); },
    async listArtifacts(_env, query, context) {
      f.calls.push(["artifacts", query]); memberGate(context);
      return { items: [{ id: "zh-text", report_id: query.reportId, kind: "text", language: "zh-Hans", size: 5,
        mime_type: "text/plain", filename: "text.txt", object_key: "_workflow-cache/private.json", secret: "not-public" }], next_cursor: null };
    },
    async downloadReport(_env, query, context) {
      f.calls.push(["download", query]); memberGate(context);
      context.commitDownload = async () => { f.commits++; };
      return new Response(new ReadableStream({ start(controller) { controller.enqueue(new TextEncoder().encode("%PDF-fixture")); },
        pull(controller) { controller.close(); }, cancel() { f.cancelled++; } }),
      { headers: { "content-type": "application/pdf", "content-length": "12", "set-cookie": "private-cookie", "x-storage-key": "private" } });
    },
    async downloadArtifact(_env, query, context) {
      f.calls.push(["artifact-download", query]); memberGate(context);
      return new Response("hello", { headers: { "content-type": "text/plain", "content-length": "5" } });
    },
  };
  f.api = createCustomerContentApi(f.adapters);
  f.request = (path, { method = "GET", body, auth = "session", headers = {} } = {}) => f.api.handle(new Request(`https://kcdesk.com${path}`, {
    method, headers: { ...(auth ? { authorization: `Bearer ${auth}` } : {}), ...(body !== undefined ? { "content-type": "application/json" } : {}), ...headers },
    ...(body !== undefined ? { body: JSON.stringify(body) } : {}),
  }), {});
  f.grant = async (extra = {}) => f.request("/api/admin/content-api/grant", { method: "POST", auth: "admin", body: {
    email: user.email, enabled: true, access_mode: "membership", report_ids: [], scopes: ALL,
    expires_at: "2026-11-12T00:00:00Z", ...extra,
  } });
  f.key = async (extra = {}) => {
    const response = await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "Offline fixture", ...extra } });
    assert.equal(response.status, 201, await response.clone().text());
    return response.json();
  };
  return f;
}

test("admin permission and authenticated user grant are mandatory; failed create writes no orphan", async () => {
  const f = fixture();
  assert.equal((await f.request("/api/admin/content-api/grant?email=reader@example.test")).status, 403);
  assert.equal((await f.request("/api/account/content-api", { auth: null })).status, 401);
  assert.equal((await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "denied" } })).status, 403);
  assert.equal(f.bucket.writes.length, 0);
  assert.equal((await f.grant()).status, 200);
  const status = await (await f.request("/api/account/content-api")).json();
  assert.equal(status.grant.access_mode, "membership"); assert.equal(status.grant.daily_bytes, 1024 ** 3); assert.deepEqual(status.keys, []);
});

test("random 256-bit secrets are returned once and only digest is persisted", async () => {
  const f = fixture(); await f.grant();
  const one = await f.key(), two = await f.key();
  assert.match(one.secret, /^kcd_live_[a-f0-9]{24}\.[a-f0-9]{64}$/u);
  assert.notEqual(one.secret, two.secret); assert.notEqual(one.key.id, two.key.id);
  assert.equal(one.key.expires_at, "2026-11-12T00:00:00.000Z");
  const stored = JSON.stringify([...f.bucket.rows.values()]);
  assert.equal(stored.includes(one.secret), false); assert.equal(stored.includes(one.secret.split(".")[1]), false);
  const list = await (await f.request("/api/account/content-api")).text();
  assert.equal(list.includes("secret"), false); assert.equal(list.includes('"hash"'), false);
  assert.equal(list.includes(one.key.id), true);
  assert.equal((await f.request("/api/content/v1/reports", { auth: one.secret })).status, 200);
  assert.equal((await f.request("/api/content/v1/reports", { auth: `${one.secret.slice(0, -1)}z` })).status, 401);
});

test("key scope and current grant scope intersect on every request", async () => {
  const f = fixture(); await f.grant(); const key = await f.key({ scopes: ["reports:read"] });
  assert.equal((await f.request("/api/content/v1/reports/r1/download", { auth: key.secret })).status, 403);
  await f.grant({ scopes: ["artifacts:read"] });
  const response = await f.request("/api/content/v1/reports", { auth: key.secret });
  assert.equal(response.status, 403); assert.equal((await response.json()).error, "scope_denied");
  const escalated = await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "bad", scopes: ALL } });
  assert.equal(escalated.status, 403);
});

test("grant expiry, key expiry, disabled account and identity replacement invalidate keys", async () => {
  const f = fixture(); await f.grant(); const key = await f.key({ expires_at: "2026-10-12T13:00:00Z" });
  f.now += 3600001;
  assert.equal((await (await f.request("/api/content/v1/reports", { auth: key.secret })).json()).error, "key_expired");
  f.now = START; f.user.disabled = true;
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 403);
  f.user.disabled = false; f.user.id = "replacement-account";
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 401);
  f.user.id = "account-test-001";
  const grantPath = [...f.bucket.rows.keys()].find(path => path.includes("/accounts/"));
  const state = JSON.parse(f.bucket.rows.get(grantPath).raw); state.grant.expires_at = "2026-10-11T00:00:00Z";
  await f.bucket.put(grantPath, JSON.stringify(state));
  assert.equal((await (await f.request("/api/content/v1/reports", { auth: key.secret })).json()).error, "api_permission_denied");
});

test("self revocation cannot touch another account and disabling grant permanently revokes prior keys", async () => {
  const f = fixture(); await f.grant(); const key = await f.key();
  const path = `/api/account/content-api/keys/${key.key.id}`;
  assert.equal((await f.request(path, { method: "DELETE", auth: "other-session" })).status, 404);
  assert.equal((await f.request(path, { method: "DELETE" })).status, 200);
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 401);
  const next = await f.key(); await f.grant({ enabled: false }); await f.grant();
  assert.equal((await f.request("/api/content/v1/reports", { auth: next.secret })).status, 401);
  assert.equal((await f.request("/api/content/v1/reports", { auth: (await f.key()).secret })).status, 200);
});

test("separate corpus grant is explicit and restricted IDs apply to both listings and downloads", async () => {
  const f = fixture(); await f.grant({ report_ids: ["r1"] }); const key = await f.key();
  f.member = false;
  assert.equal((await f.request("/api/content/v1/reports/r1", { auth: key.secret })).status, 403);
  await f.grant({ access_mode: "granted_corpus", report_ids: ["r1"] });
  const listed = await (await f.request("/api/content/v1/reports", { auth: key.secret })).json();
  assert.deepEqual(listed.items.map(row => row.id), ["r1"]); assert.equal(JSON.stringify(listed).includes("object_key"), false);
  assert.equal((await f.request("/api/content/v1/reports/r2/download", { auth: key.secret })).status, 403);
  assert.equal(f.calls.some(call => call[0] === "download"), false);
  assert.equal((await f.request("/api/content/v1/reports/r1", { auth: key.secret })).status, 200);
});

test("listing validates pagination and date, sanitizes descriptors, and never takes storage paths or query secrets", async () => {
  const f = fixture(); await f.grant(); const key = await f.key();
  const response = await f.request("/api/content/v1/reports/r1/artifacts?kind=text&language=zh-Hans&limit=10", { auth: key.secret });
  const listed = await response.json(); assert.equal(response.status, 200);
  assert.deepEqual(listed.items[0], { id: "zh-text", report_id: "r1", kind: "text", language: "zh-Hans", mime_type: "text/plain", size: 5, filename: "text.txt" });
  assert.deepEqual(f.calls.at(-1)[1], { reportId: "r1", kind: "text", language: "zh-Hans", limit: 10, cursor: null });
  for (const path of ["/api/content/v1/reports?limit=101", "/api/content/v1/reports?limit=1&limit=2", "/api/content/v1/reports?date=2026-02-30",
    "/api/content/v1/reports?date=2026-99-99", "/api/content/v1/reports?cursor=../secret", "/api/content/v1/reports?key=_account/secret",
    `/api/content/v1/reports?api_key=${key.secret}`]) {
    assert.equal((await f.request(path, { auth: key.secret })).status, 400, path);
  }
  assert.equal((await f.request("/api/content/v1/reports/r1/artifacts/%2e%2e%2fsecrets", { auth: key.secret })).status, 404);
  assert.equal(f.bucket.reads.every(path => path.startsWith("_customer-content-api/v1/")), true);
});

test("all keys share account request limits; atomic contention cannot double spend", async () => {
  const f = fixture(); await f.grant({ requests_per_minute: 1 }); const first = await f.key(), second = await f.key();
  const results = await Promise.all([first, second].map(key => f.request("/api/content/v1/reports", { auth: key.secret })));
  assert.deepEqual(results.map(response => response.status).sort(), [200, 429]);
  assert.equal((await results.find(response => response.status === 429).json()).error, "rate_limited");
  f.now += 60000;
  assert.equal((await f.request("/api/content/v1/reports", { auth: second.secret })).status, 200);
});

test("daily request allowance resets by UTC day, but not by minute or key rotation", async () => {
  const f = fixture(); await f.grant({ daily_requests: 1 }); const key = await f.key();
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 200);
  f.now += 60000;
  const denied = await f.request("/api/content/v1/reports", { auth: key.secret });
  assert.equal(denied.status, 429); assert.equal((await denied.json()).error, "daily_request_limit");
  f.now += 86400000;
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 200);
});

test("known byte allowance precedes web download commit; deny cancels stream and never consumes trial", async () => {
  const f = fixture(); await f.grant({ daily_bytes: 12 }); const key = await f.key();
  const first = await f.request("/api/content/v1/reports/r1/download", { auth: key.secret });
  assert.equal(first.status, 200); assert.equal(await first.text(), "%PDF-fixture"); assert.equal(f.commits, 1);
  assert.equal(first.headers.get("set-cookie"), null); assert.equal(first.headers.get("x-storage-key"), null);
  assert.equal(first.headers.get("content-disposition"), "attachment"); assert.equal(first.headers.get("cache-control"), "private, no-store");
  const second = await f.request("/api/content/v1/reports/r1/download", { auth: key.secret });
  assert.equal(second.status, 429); assert.equal((await second.json()).error, "daily_byte_limit");
  assert.equal(f.commits, 1); assert.equal(f.cancelled, 1);
});

test("concurrent byte reservations enforce a shared account allowance across download kinds", async () => {
  const f = fixture(); await f.grant({ daily_bytes: 5 }); const key = await f.key();
  const results = await Promise.all([1, 2].map(() => f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret })));
  assert.deepEqual(results.map(response => response.status).sort(), [200, 429]);
  assert.equal(await results.find(response => response.status === 200).text(), "hello");
});

test("missing/overlarge declared lengths and source failures fail closed without leaking exception text", async () => {
  const f = fixture(); await f.grant(); const key = await f.key();
  for (const headers of [{}, { "content-length": String(256 * 1024 * 1024 + 1) }, { "content-length": "5", "content-encoding": "gzip" }]) {
    f.adapters.downloadArtifact = async () => new Response("hello", { headers });
    const response = await f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret });
    assert.equal(response.status, 503);
  }
  f.adapters.downloadArtifact = async () => { throw new Error("API_SECRET=private; bucket=_account"); };
  const failed = await f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret });
  assert.deepEqual(await failed.json(), { ok: false, error: "service_unavailable" });
});

test("declared stream size is enforced, including early EOF; never returns extra bytes", async () => {
  const f = fixture(); await f.grant(); const key = await f.key();
  for (const text of ["longer", "no"]) {
    f.adapters.downloadArtifact = async () => new Response(text, { headers: { "content-length": "5" } });
    const response = await f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret });
    assert.equal(response.status, 200);
    await assert.rejects(response.text(), /content_unavailable/u);
  }
});

test("web download commit denial cancels transfer; account bytes remain conservatively reserved", async () => {
  const f = fixture(); await f.grant({ daily_bytes: 5 }); const key = await f.key();
  f.adapters.downloadArtifact = async (_env, _query, context) => {
    context.commitDownload = async () => { throw new CustomerContentApiError(403, "download_limit_reached"); };
    return new Response("hello", { headers: { "content-length": "5" } });
  };
  const denied = await f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret });
  assert.equal(denied.status, 403); assert.equal((await denied.json()).error, "download_limit_reached");
  assert.equal((await f.request("/api/content/v1/reports/r1/artifacts/zh-text", { auth: key.secret })).status, 429);
});

test("grant limits, cross-origin mutations, oversized bodies and five active keys are bounded", async () => {
  const f = fixture();
  assert.equal((await f.grant({ daily_bytes: 101 * 1024 ** 3 })).status, 400);
  assert.equal((await f.grant({ expires_at: "2030-01-01T00:00:00Z" })).status, 400);
  await f.grant();
  assert.equal((await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "CSRF" }, headers: { origin: "https://other.example" } })).status, 403);
  assert.equal((await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "x".repeat(20000) } })).status, 400);
  for (let count = 0; count < 5; count++) await f.key();
  assert.equal((await f.request("/api/account/content-api/keys", { method: "POST", body: { name: "sixth" } })).status, 409);
});

test("storage CAS exhaustion and malformed stored grant fail closed; unrelated paths stay with root router", async () => {
  const f = fixture(); await f.grant(); const key = await f.key();
  assert.equal(await f.request("/api/download", { auth: null }), null);
  assert.equal(f.api.matches("/api/content/v1/reports"), true);
  f.bucket.forceConflict = true;
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 503);
  f.bucket.forceConflict = false;
  const accountPath = [...f.bucket.rows.keys()].find(path => path.includes("/accounts/"));
  const state = JSON.parse(f.bucket.rows.get(accountPath).raw); state.grant.daily_bytes = -1;
  await f.bucket.put(accountPath, JSON.stringify(state));
  assert.equal((await f.request("/api/content/v1/reports", { auth: key.secret })).status, 403);
});
