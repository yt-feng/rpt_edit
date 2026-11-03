import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";
import { handleReportRefresh, REPORT_REFRESH_EVENT, REPORT_REFRESH_STATE_KEY } from "../../workers/portal-suite-worker/src/report-refresh.js";
import worker from "../../workers/portal-suite-worker/src/index.js";

class Bucket {
  constructor() { this.rows = new Map(); this.serial = 0; }
  seed(key, payload) { this.rows.set(key, { value: JSON.stringify(payload), etag: String(++this.serial) }); }
  async get(key) {
    const row = this.rows.get(key);
    return row ? { etag: row.etag, text: async () => row.value } : null;
  }
  async put(key, value, options = {}) {
    const row = this.rows.get(key);
    const condition = options.onlyIf || {};
    if (condition.etagDoesNotMatch === "*" && row) return null;
    if (Object.hasOwn(condition, "etagMatches") && (!row || row.etag !== condition.etagMatches)) return null;
    const etag = String(++this.serial);
    this.rows.set(key, { value: String(value), etag });
    return { etag };
  }
  read() { return JSON.parse(this.rows.get(REPORT_REFRESH_STATE_KEY).value); }
}

function fixture(options = {}) {
  const bucket = options.bucket || new Bucket();
  const env = { REPORT_BUCKET: bucket, GH_DISPATCH_TOKEN: "private-test-dispatch-token" };
  const calls = [];
  const deps = {
    authorize: async () => {},
    respond: (_request, _env, status, payload) => new Response(JSON.stringify(payload), { status }),
    repository: () => "owner/reports",
    fetchWithTimeout: async (url, init = {}) => {
      calls.push({ url, ...init });
      if (init.method === "POST") {
        if (options.throwDispatch) throw new Error("private upstream body token=secret");
        return new Response(options.rejectDispatch ? "private upstream rejection token=secret" : null, { status: options.rejectDispatch || 204 });
      }
      const status = new URL(url).searchParams.get("status");
      const tokenRejection = options.rejectReadTokens && options.rejectReadTokens[init.headers.Authorization];
      if (tokenRejection) return new Response("private credential permissions", { status: tokenRejection });
      if (options.failRead || options.failStatus === status) return new Response("private upstream status", { status: 503 });
      const rows = status ? [...(options.runs || []), ...(options.activeRuns || [])].filter((run) => run.status === status) : options.runs || [];
      return Response.json({ workflow_runs: rows });
    },
  };
  const invoke = async (method = "GET", payload = {}) => {
    const request = new Request("https://site.invalid/account-admin/report-refresh", { method, ...(method === "POST" ? { body: JSON.stringify(payload) } : {}) });
    const response = await handleReportRefresh(request, env, deps);
    return { status: response.status, body: await response.json() };
  };
  return { bucket, env, deps, calls, invoke };
}

function run(status, extras = {}) {
  return { id: 42, head_branch: "main", event: "schedule", status, conclusion: "", created_at: new Date().toISOString(), updated_at: new Date().toISOString(), ...extras };
}

test("manual refresh dispatches a fixed repository event and stores acceptance without claiming completion", async () => {
  const f = fixture();
  const result = await f.invoke("POST", { ref: "other", workflow: "untrusted.yml", operation: "rehearse" });
  assert.equal(result.status, 202);
  assert.equal(result.body.state, "requested");
  assert.equal(result.body.can_refresh, false);
  assert.equal(result.body.run, null);
  assert.equal(f.bucket.read().state, "accepted");
  const dispatched = f.calls.filter((call) => call.method === "POST");
  assert.equal(dispatched.length, 1);
  assert.equal(dispatched[0].url, "https://api.github.com/repos/owner/reports/dispatches");
  assert.equal(JSON.parse(dispatched[0].body).event_type, REPORT_REFRESH_EVENT);
  assert.deepEqual(Object.keys(JSON.parse(dispatched[0].body).client_payload).sort(), ["request_id", "requested_at"]);
  assert.doesNotMatch(JSON.stringify(result), /private-test|token|untrusted|rehearse/);
});

test("separate read and dispatch credentials keep workflow GETs on the read token", async () => {
  const f = fixture();
  f.env.GH_READ_TOKEN = "private-read-token";
  const result = await f.invoke("POST");
  assert.equal(result.status, 202);
  const reads = f.calls.filter((call) => call.method !== "POST");
  const writes = f.calls.filter((call) => call.method === "POST");
  assert.equal(reads.length, 6);
  assert.ok(reads.every((call) => call.headers.Authorization === "Bearer private-read-token"));
  assert.equal(writes.length, 1);
  assert.equal(writes[0].headers.Authorization, "Bearer private-test-dispatch-token");
  assert.doesNotMatch(JSON.stringify(result), /private-read|private-test/);
});

test("workflow reads fall back once to the dispatch credential after a 401 or 403", async () => {
  for (const rejection of [401, 403]) {
    const f = fixture({ rejectReadTokens: { "Bearer private-read-token": rejection } });
    f.env.GH_READ_TOKEN = "private-read-token";
    const result = await f.invoke("POST");
    assert.equal(result.status, 202);
    const reads = f.calls.filter((call) => call.method !== "POST");
    assert.equal(reads.length, 12);
    const perUrl = new Map();
    for (const call of reads) perUrl.set(call.url, [...(perUrl.get(call.url) || []), call]);
    for (const calls of perUrl.values()) {
      assert.deepEqual(calls.map((call) => call.headers.Authorization), ["Bearer private-read-token", "Bearer private-test-dispatch-token"]);
    }
    assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
  }
});

test("all rejected read credentials fail closed and never dispatch or reserve a receipt", async () => {
  const f = fixture({ rejectReadTokens: {
    "Bearer private-read-token": 403,
    "Bearer private-test-dispatch-token": 401,
  } });
  f.env.GH_READ_TOKEN = "private-read-token";
  const result = await f.invoke("POST");
  assert.equal(result.status, 503);
  assert.equal(result.body.state, "unavailable");
  assert.equal(result.body.can_refresh, false);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
  assert.equal(f.bucket.rows.has(REPORT_REFRESH_STATE_KEY), false);
  assert.ok(f.calls.length <= 12);
  assert.doesNotMatch(JSON.stringify(result), /private|permissions|credential/);
});

test("non-authentication read errors do not try another token or issue a dispatch", async () => {
  const f = fixture({ failRead: true });
  f.env.GH_READ_TOKEN = "private-read-token";
  const result = await f.invoke("POST");
  assert.equal(result.status, 503);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
  assert.ok(f.calls.every((call) => call.headers.Authorization === "Bearer private-read-token"));
});

test("a just-completed earlier manual run cannot be mistaken for the new request", async () => {
  const f = fixture({ runs: [run("completed", { event: "repository_dispatch", conclusion: "success" })] });
  const first = await f.invoke("POST");
  const again = await f.invoke("POST");
  assert.equal(first.body.state, "requested");
  assert.equal(again.body.state, "requested");
  assert.equal(again.body.can_refresh, false);
  assert.deepEqual(f.bucket.read().observed_run_ids, [42]);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
});

test("a repeated click reconciles the durable receipt and never sends another dispatch", async () => {
  const f = fixture();
  await f.invoke("POST");
  const result = await f.invoke("POST");
  assert.equal(result.body.state, "requested");
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
});

test("a refresh already running or pending is returned without issuing a duplicate", async () => {
  for (const status of ["queued", "pending", "in_progress", "waiting", "requested"]) {
    const f = fixture({ runs: [run(status)] });
    const result = await f.invoke("POST");
    assert.equal(result.body.state, status === "in_progress" ? "in_progress" : "pending");
    assert.equal(result.body.can_refresh, false);
    assert.equal(result.body.run.url, "https://github.com/owner/reports/actions/runs/42");
    assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
  }
});

test("active inventory finds a long-running task hidden behind thirty recent completed runs", async () => {
  const recent = Array.from({ length: 30 }, (_, index) => run("completed", {
    id: 100 + index, event: "workflow_run", conclusion: "cancelled",
    created_at: new Date(Date.now() - index * 1000).toISOString(),
  }));
  const f = fixture({ runs: recent, activeRuns: [run("in_progress", { id: 9, created_at: new Date(Date.now() - 4 * 3600000).toISOString() })] });
  const result = await f.invoke("POST");
  assert.equal(result.body.state, "in_progress");
  assert.equal(result.body.run.id, 9);
  assert.equal(result.body.can_refresh, false);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
  const statuses = f.calls.map((call) => new URL(call.url).searchParams.get("status")).filter(Boolean);
  assert.deepEqual(statuses.sort(), ["in_progress", "pending", "queued", "requested", "waiting"]);
});

test("running refresh takes precedence over a newer pending run and superseded queue entries", async () => {
  const f = fixture({ runs: [
    run("completed", { id: 50, event: "workflow_run", conclusion: "cancelled" }),
    run("pending", { id: 49, created_at: new Date(Date.now() - 60000).toISOString() }),
    run("in_progress", { id: 10, created_at: new Date(Date.now() - 4 * 3600000).toISOString() }),
  ] });
  const result = await f.invoke();
  assert.equal(result.body.state, "in_progress");
  assert.equal(result.body.run.id, 10);
});

test("an unavailable active-status inventory prevents dispatch even when recent history has no active runs", async () => {
  for (const status of ["in_progress", "pending", "queued", "requested", "waiting"]) {
    const f = fixture({ failStatus: status });
    const result = await f.invoke("POST");
    assert.equal(result.status, 503);
    assert.equal(result.body.can_refresh, false);
    assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
  }
});

test("superseded automatic queue cancellation does not hide the last completed refresh", async () => {
  const successfulAt = new Date(Date.now() - 60000).toISOString();
  const f = fixture({ runs: [
    run("completed", { id: 50, event: "workflow_run", conclusion: "cancelled" }),
    run("completed", { id: 49, conclusion: "success", created_at: new Date(Date.now() - 120000).toISOString(), updated_at: successfulAt }),
  ] });
  const result = await f.invoke();
  assert.equal(result.body.state, "completed");
  assert.equal(result.body.run.id, 49);
  assert.equal(result.body.last_success_at, successfulAt);
});

test("concurrent clicks across isolated requests win one conditional R2 lease", async () => {
  const f = fixture();
  const results = await Promise.all([f.invoke("POST"), f.invoke("POST")]);
  assert.ok(results.every((result) => result.status === 202));
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
});

test("ambiguous dispatch timeout remains unknown and is not retried automatically", async () => {
  const f = fixture({ throwDispatch: true });
  const first = await f.invoke("POST");
  assert.equal(first.status, 202);
  assert.equal(first.body.state, "unknown");
  const next = await f.invoke("POST");
  assert.equal(next.body.can_refresh, false);
  assert.equal(next.body.state, "unknown");
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
  assert.doesNotMatch(JSON.stringify(next), /secret|token|private upstream/);
});

test("status read failure prevents dispatch rather than assuming there is no active task", async () => {
  const f = fixture({ failRead: true });
  const result = await f.invoke("POST");
  assert.equal(result.status, 503);
  assert.equal(result.body.can_refresh, false);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
});

test("upstream dispatch rejection is bounded and does not disclose provider errors", async () => {
  const f = fixture({ rejectDispatch: 403 });
  const first = await f.invoke("POST");
  assert.equal(first.status, 503);
  assert.equal(first.body.state, "failed");
  const next = await f.invoke("POST");
  assert.equal(next.body.can_refresh, false);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 1);
  assert.doesNotMatch(JSON.stringify(first), /private|token|secret/);
});

test("only the matching later repository dispatch can complete a saved request", async () => {
  const bucket = new Bucket();
  const requested = new Date(Date.now() - 10000).toISOString();
  bucket.seed(REPORT_REFRESH_STATE_KEY, { state: "accepted", requested_at: requested });
  const earlier = new Date(Date.now() - 60000).toISOString();
  const waiting = fixture({ bucket, runs: [run("completed", { created_at: earlier, conclusion: "success" })] });
  assert.equal((await waiting.invoke()).body.state, "requested");
  const done = fixture({ bucket, runs: [run("completed", { event: "repository_dispatch", conclusion: "success" })] });
  const result = await done.invoke();
  assert.equal(result.body.state, "completed");
  assert.equal(result.body.run.conclusion, "success");
  assert.equal(result.body.can_refresh, true);
});

test("storage failure prevents a dispatch without a durable receipt", async () => {
  const f = fixture();
  f.bucket.put = async () => { throw new Error("storage unavailable"); };
  assert.equal((await f.invoke("POST")).status, 503);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
});

test("missing write token disables manual refresh while read-only status remains available", async () => {
  const f = fixture();
  delete f.env.GH_DISPATCH_TOKEN;
  f.env.GH_READ_TOKEN = "read-only";
  const result = await f.invoke("POST");
  assert.equal(result.body.can_refresh, false);
  assert.equal(f.calls.filter((call) => call.method === "POST").length, 0);
});

const AUTH_SECRET = "admin-report-refresh-test-secret";
function seedUser(bucket, username, email) {
  const user = { id: `${username}-id`, username, email, created_at: "2026-08-01T00:00:00Z", site_origin: "portal", registered_site: "portal", source_site: "portal" };
  for (const [field, input] of [["id", user.id], ["username", username], ["email", email]]) {
    bucket.seed(`_account/users/${field}/${encodeURIComponent(input)}`, user);
  }
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username, email, iat: now, exp: now + 3600 })).toString("base64url");
  const signature = createHmac("sha256", AUTH_SECRET).update(`portal:account-token:v1:${body}`).digest("base64url");
  return `${body}.${signature}`;
}

test("actual Worker route rejects anonymous, ordinary, and operator accounts before upstream calls", async () => {
  const bucket = new Bucket();
  const env = { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", AUTH_SECRET, ALLOWED_ORIGIN: "https://site.invalid", GH_DISPATCH_TOKEN: "test" };
  const tokens = ["", seedUser(bucket, "ordinary", "ordinary@example.invalid"), seedUser(bucket, "admin-b", "admin-b@users.portal.example.invalid")];
  const originalFetch = globalThis.fetch;
  let fetches = 0;
  globalThis.fetch = async () => { fetches++; throw new Error("Should not fetch"); };
  try {
    for (const token of tokens) {
      const response = await worker.fetch(new Request("https://worker.invalid/account-admin/report-refresh", { method: "POST", headers: token ? { Authorization: `Bearer ${token}` } : {} }), env, { waitUntil() {} });
      assert.equal(response.status, 403);
    }
    assert.equal(fetches, 0);
  } finally { globalThis.fetch = originalFetch; }
});

test("actual Worker route accepts the configured super account session", async () => {
  const bucket = new Bucket();
  const token = seedUser(bucket, "admin-a", "admin-a@users.portal.example.invalid");
  const env = { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", AUTH_SECRET, ALLOWED_ORIGIN: "https://site.invalid", GH_DISPATCH_TOKEN: "test" };
  const originalFetch = globalThis.fetch;
  let dispatched = 0;
  globalThis.fetch = async (_url, options) => options.method === "POST"
    ? (dispatched++, new Response(null, { status: 204 }))
    : Response.json({ workflow_runs: [] });
  try {
    const response = await worker.fetch(new Request("https://worker.invalid/account-admin/report-refresh", { method: "POST", headers: { Authorization: `Bearer ${token}` } }), env, { waitUntil() {} });
    assert.equal(response.status, 202, await response.text());
    assert.equal(dispatched, 1);
  } finally { globalThis.fetch = originalFetch; }
});
