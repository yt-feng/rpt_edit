import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import worker from "../../workers/portal-suite-worker/src/index.js";

const clientSource = await readFile(new URL("../site_src/assets/analytics.js", import.meta.url), "utf8");
const tick = () => new Promise((resolve) => setImmediate(resolve));

function browser({ configPromise, fetchResult } = {}) {
  const calls = [];
  const values = new Map();
  const listeners = new Map();
  const window = {
    document: {
      readyState: "complete",
      body: { dataset: { page: "index", analyticsAuto: "manual" } },
      referrer: "",
      addEventListener(name, fn) { listeners.set(name, fn); },
    },
    addEventListener(name, fn) { listeners.set(name, fn); },
    location: { pathname: "/", search: "", origin: "https://portal.example.invalid" },
    localStorage: {
      getItem(key) { return values.get(key) || null; },
      setItem(key, value) { values.set(key, String(value)); },
    },
    navigator: { language: "zh-CN", userAgent: "test-browser" },
    async fetch(url, init = {}) {
      calls.push({ url, ...init });
      if (url === "/data/config.json") {
        if (configPromise) await configPromise;
        return { ok: true, json: async () => ({ worker_base_url: "/api" }) };
      }
      return fetchResult ? fetchResult() : { ok: true };
    },
  };
  vm.runInNewContext(clientSource, { window, URL, URLSearchParams, TextEncoder });
  return {
    window, calls, values, listeners,
    track: window.PortalSuiteAnalytics.track,
    posts: () => calls.filter((call) => call.method === "POST"),
  };
}

function events(call) {
  const body = JSON.parse(call.body);
  return body.events || [body];
}

test("12 popular impressions use one POST and preserve each event's attribution", async () => {
  const client = browser();
  const outcomes = await Promise.all(Array.from({ length: 12 }, (_, index) => client.track(
    "report_chat_interaction", { action: "popular_impression", question_hash: `question-${index}`, item_count: 12 },
  )));
  assert.ok(outcomes.every(Boolean));
  assert.equal(client.posts().length, 1);
  const sent = events(client.posts()[0]);
  assert.equal(sent.length, 12);
  assert.deepEqual(sent.map((item) => item.data.question_hash), Array.from({ length: 12 }, (_, i) => `question-${i}`));
  assert.equal(new Set(sent.map((item) => item.session_id)).size, 1);
  assert.ok(sent.every((item) => item.visitor_id && item.client_ts && item.path === "/"));
});

test("batching obeys both event-count and UTF-8 body limits without dropping accepted events", async () => {
  const client = browser();
  assert.ok((await Promise.all(Array.from({ length: 45 }, (_, i) => client.track("search", { query: `query-${i}` })))).every(Boolean));
  assert.deepEqual(client.posts().map((call) => events(call).length), [20, 20, 5]);

  const unicode = browser();
  const outcomes = await Promise.all(Array.from({ length: 8 }, () => unicode.track("search", { query: "研究".repeat(500) })));
  assert.ok(outcomes.every(Boolean));
  assert.ok(unicode.posts().length > 1, "byte-size limit must split batches before the 20-event limit");
  assert.equal(unicode.posts().flatMap(events).length, 8);
  assert.ok(unicode.posts().every((call) => new TextEncoder().encode(call.body).byteLength <= 24 * 1024));
});

test("events queued around login and logout never share or change authorization", async () => {
  let resolveConfig;
  const client = browser({ configPromise: new Promise((resolve) => { resolveConfig = resolve; }) });
  const anonymous = client.track("page_view", { page: "index" });
  client.values.set("portal_auth_session", JSON.stringify({ token: "account-a" }));
  const loggedIn = client.track("account_auth", { action: "login" });
  client.values.delete("portal_auth_session");
  const loggedOut = client.track("account_auth", { action: "logout" });
  resolveConfig();
  assert.deepEqual(await Promise.all([anonymous, loggedIn, loggedOut]), [true, true, true]);
  assert.deepEqual(client.posts().map((call) => call.headers.Authorization), [undefined, "Bearer account-a", undefined]);
  assert.equal(await client.track("page_view", { page: "index" }), false, "batching must retain page-view deduplication");
});

test("pagehide and visibilitychange synchronously flush pending events once before config resolves", async () => {
  let resolveConfig;
  const client = browser({ configPromise: new Promise((resolve) => { resolveConfig = resolve; }) });
  const tracked = [client.track("search", { query: "one" }), client.track("search", { query: "two" })];
  await tick();
  assert.equal(client.posts().length, 0);
  client.listeners.get("pagehide")();
  assert.equal(client.posts().length, 1, "keepalive request must start before the lifecycle callback returns");
  assert.equal(client.posts()[0].keepalive, true);
  client.window.document.visibilityState = "hidden";
  client.listeners.get("visibilitychange")();
  resolveConfig();
  assert.deepEqual(await Promise.all(tracked), [true, true]);
  await tick();
  assert.equal(client.posts().length, 1, "the regular flush must not duplicate the lifecycle flush");
});

test("pending queue is bounded while config stalls and rejected page views can be attempted later", async () => {
  let resolveConfig;
  const client = browser({ configPromise: new Promise((resolve) => { resolveConfig = resolve; }) });
  const tracked = Array.from({ length: 200 }, () => client.track("search", { query: "x".repeat(400) }));
  assert.equal(await client.track("page_view", { page: "index" }), false);
  resolveConfig();
  const results = await Promise.all(tracked);
  const accepted = results.filter(Boolean).length;
  assert.ok(accepted > 0 && accepted <= 100);
  assert.equal(client.posts().flatMap(events).length, accepted);
  assert.equal(await client.track("page_view", { page: "index" }), true);
});

test("oversized events and non-success responses report failure without automatic retries", async () => {
  const client = browser({ fetchResult: () => ({ ok: false }) });
  assert.equal(await client.track("search", { query: "界".repeat(9000) }), false);
  assert.equal(client.posts().length, 0);
  assert.equal(await client.track("search", { query: "normal" }), false);
  await tick();
  assert.equal(client.posts().length, 1);
});

test("unsupported client audit events cannot poison a valid event batch", async () => {
  const client = browser();
  const outcomes = await Promise.all([
    client.track("search", { query: "valid" }),
    client.track("membership_request", { action: "submit" }),
    client.track("page_view", { page: "index" }),
  ]);
  assert.deepEqual(outcomes, [true, false, true]);
  assert.equal(client.posts().length, 1);
  assert.deepEqual(events(client.posts()[0]).map((event) => event.type), ["search", "page_view"]);
  const bucket = storage();
  assert.equal((await post(client.posts()[0].body, bucket)).status, 204);
  assert.equal(bucket.writes.size, 4);
});

test("client event allowlist stays aligned with the Worker's public ingestion contract", async () => {
  const workerSource = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
  const types = [...workerSource.match(/const PUBLIC_ANALYTICS_EVENT_TYPES = new Set\(\[([\s\S]*?)\]\);/u)[1].matchAll(/"([a-z_]+)"/gu)].map((match) => match[1]);
  const client = browser();
  const outcomes = await Promise.all(types.map((type) => client.track(type, { action: "test" })));
  assert.ok(outcomes.every(Boolean));
  assert.deepEqual(client.posts().flatMap(events).map((event) => event.type), types);
});

function storage() {
  const writes = new Map();
  const reads = [];
  const seeded = new Map();
  let active = 0;
  let peak = 0;
  return {
    writes, reads, seeded,
    get peak() { return peak; },
    async get(key) {
      reads.push(key);
      if (!seeded.has(key)) return null;
      return { json: async () => seeded.get(key), text: async () => JSON.stringify(seeded.get(key)) };
    },
    async put(key, value) {
      active += 1;
      peak = Math.max(peak, active);
      await tick();
      writes.set(key, JSON.parse(String(value)));
      active -= 1;
    },
  };
}

function post(body, bucket, { origin = "https://portal.example.invalid", headers = {} } = {}) {
  return worker.fetch(new Request("https://worker.test/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", origin, "CF-Connecting-IP": "203.0.113.8", ...headers },
    body: typeof body === "string" ? body : JSON.stringify(body),
  }), { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", MASTER_KEY: "analytics-test-secret", ALLOWED_ORIGIN: "https://portal.example.invalid" });
}

test("batch endpoint retains per-event primary and backup records with bounded write concurrency", async () => {
  const bucket = storage();
  const response = await post({ events: Array.from({ length: 12 }, (_, i) => ({
    type: "report_chat_interaction", visitor_id: "visitor-a", session_id: "session-a", path: "/?private=1",
    data: { action: "popular_impression", question_hash: `question-${i}`, query: "private question" },
  })) }, bucket);
  assert.equal(response.status, 204);
  assert.equal(bucket.writes.size, 24);
  const primary = [...bucket.writes].filter(([key]) => key.startsWith("_analytics/events/")).map(([, value]) => value);
  assert.equal(new Set(primary.map((item) => item.id)).size, 12);
  assert.deepEqual(new Set(primary.map((item) => item.question_hash)), new Set(Array.from({ length: 12 }, (_, i) => `question-${i}`)));
  assert.ok(primary.every((event) => event.query === "" && event.path === "/" && event.user === null));
  assert.equal(new Set(primary.map((event) => event.visitor_id)).size, 1);
  assert.notEqual(primary[0].visitor_id, "visitor-a");
  assert.ok(bucket.peak <= 8, "at most four events (two objects each) are written concurrently");
});

test("batch identity is resolved once from the signed request and ignores forged event users", async () => {
  const bucket = storage();
  const user = { id: "user-batch", username: "batch-user", email: "batch@example.invalid", role: "member" };
  bucket.seeded.set("_account/users/username/batch-user", user);
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, iat: now, exp: now + 3600 })).toString("base64url");
  const signature = createHmac("sha256", "analytics-test-secret").update(`portal:account-token:v1:${body}`).digest("base64url");
  const response = await post({ events: Array.from({ length: 12 }, () => ({
    type: "page_view", user: { id: "forged", role: "super" }, data: { page: "index", user: { id: "forged" } },
  })) }, bucket, { headers: { Authorization: `Bearer ${body}.${signature}` } });
  assert.equal(response.status, 204);
  assert.equal(bucket.reads.filter((key) => key === "_account/users/username/batch-user").length, 1);
  assert.ok([...bucket.writes.values()].every((event) => event.user && event.user.id === user.id));
});

test("batch validation rejects all malformed, oversized, unsupported and foreign requests before writes", async () => {
  for (const body of [
    { events: [] }, { events: {} }, { events: [null] }, { events: [[{ type: "page_view" }]] },
    { events: [{ type: "page_view" }, { type: "report_chat" }] },
    { events: [{ type: "page_view", events: [{ type: "page_view" }] }] },
    { events: Array.from({ length: 21 }, () => ({ type: "page_view" })) },
  ]) {
    const bucket = storage();
    assert.equal((await post(body, bucket)).status, 400);
    assert.equal(bucket.writes.size, 0);
    assert.equal(bucket.reads.length, 0);
  }
  const bucket = storage();
  assert.equal((await post({ events: [{ type: "page_view" }] }, bucket, { origin: "https://foreign.invalid" })).status, 403);
  assert.equal((await post({ events: [{ type: "search", data: { query: "界".repeat(9000) } }] }, bucket)).status, 413);
  assert.equal((await post("{}", bucket, { headers: { "Content-Length": String(24 * 1024 + 1) } })).status, 413);
  assert.equal(bucket.writes.size, 0);
});

test("single-event clients remain compatible and invalid authorization cannot inject an identity", async () => {
  const bucket = storage();
  const response = await post({ type: "page_view", visitor_id: "visitor-single", data: { page: "privacy" }, user: { id: "forged" } }, bucket, {
    headers: { Authorization: "Bearer invalid" },
  });
  assert.equal(response.status, 204);
  assert.equal(bucket.writes.size, 2);
  const [event] = bucket.writes.values();
  assert.equal(event.type, "page_view");
  assert.equal(event.page, "privacy");
  assert.equal(event.user, null);
});
