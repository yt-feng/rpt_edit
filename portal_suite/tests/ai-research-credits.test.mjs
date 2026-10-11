import assert from "node:assert/strict";
import { createHmac, randomUUID } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";

const quota = worker.__aiResearchCreditTest;
const keyFor = (id) => `_account/ai-research-credits-v1/${encodeURIComponent(id)}`;

class MemoryR2 {
  rows = new Map();
  version = 0;
  writes = [];
  throwAfterPutPrefix = "";
  rejectWrites = false;
  seed(key, value) {
    this.rows.set(key, { value: JSON.stringify(value), etag: `v${++this.version}` });
  }
  value(key) { return JSON.parse(this.rows.get(key)?.value || "null"); }
  async get(key) {
    const row = this.rows.get(key);
    return row ? { etag: row.etag, async json() { return JSON.parse(row.value); }, async text() { return row.value; } } : null;
  }
  async put(key, value, options = {}) {
    const old = this.rows.get(key);
    if (this.rejectWrites) return null;
    if (options.onlyIf?.etagMatches && options.onlyIf.etagMatches !== old?.etag) return null;
    if (options.onlyIf?.etagDoesNotMatch === "*" && old) return null;
    const etag = `v${++this.version}`;
    this.rows.set(key, { value: String(value), etag });
    this.writes.push(key);
    if (this.throwAfterPutPrefix && key.startsWith(this.throwAfterPutPrefix)) {
      this.throwAfterPutPrefix = "";
      throw new Error("simulated lost write response");
    }
    return { etag };
  }
  async list({ prefix = "" } = {}) {
    return { objects: [...this.rows.keys()].filter((key) => key.startsWith(prefix)).map((key) => ({ key })), truncated: false };
  }
  async delete(key) { this.rows.delete(key); }
}

function token(user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username,
    email: user.email, session_epoch: "", iat: now, exp: now + 3600 })).toString("base64url");
  return `${body}.${createHmac("sha256", "test-secret").update(`portal:account-token:v1:${body}`).digest("base64url")}`;
}

function setup() {
  const bucket = new MemoryR2();
  const env = { ACCOUNT_STORE_MODE: "r2", REPORT_BUCKET: bucket, PASSWORD_SECRET: "test-secret",
    ALLOWED_ORIGIN: "https://portal.example.invalid", STATIC_DATA_PREFIX: "test-static" };
  const admin = { id: "super-id", username: "admin-a", email: "admin-a@users.portal.example.invalid", session_epoch: "" };
  const user = { id: "reader-id", username: "reader", email: "reader@example.invalid", session_epoch: "" };
  for (const person of [admin, user]) {
    for (const field of ["id", "username", "email"]) bucket.seed(`_account/users/${field}/${encodeURIComponent(person[field])}`, person);
  }
  const request = async (method = "GET", payload = null, actor = admin) => {
    const url = `https://portal.example.invalid/api/account-admin/ai-research-credits${method === "GET" ? `?email=${encodeURIComponent(payload?.email || user.email)}` : ""}`;
    const response = await worker.fetch(new Request(url, { method,
      headers: { "Content-Type": "application/json", ...(actor ? { Authorization: `Bearer ${token(actor)}` } : {}) },
      ...(method === "POST" ? { body: JSON.stringify(payload) } : {}) }), env, { waitUntil() {} });
    return { response, data: await response.json() };
  };
  const grant = (amount, operationId = randomUUID(), extra = {}) => request("POST", {
    email: user.email, amount, reason: "Manual research support", operation_id: operationId, ...extra,
  });
  return { bucket, env, admin, user, request, grant };
}

test("super can add credits to an existing account with an atomic audit and retry idempotency", async () => {
  const h = setup();
  const operation = randomUUID();
  const first = await h.grant(7, operation);
  assert.equal(first.response.status, 200, JSON.stringify(first.data));
  assert.equal(first.data.credits.balance, 7);
  assert.equal(first.data.usage.limit, 1);
  assert.equal(first.data.usage.period, "lifetime");
  assert.equal(first.data.deduplicated, false);
  const retry = await h.grant(7, operation);
  assert.equal(retry.data.deduplicated, true);
  assert.equal(retry.data.credits.balance, 7);
  const conflict = await h.grant(8, operation);
  assert.equal(conflict.response.status, 409);
  assert.equal(conflict.data.code, "CREDIT_OPERATION_CONFLICT");
  const stored = h.bucket.value(keyFor(h.user.id));
  assert.equal(stored.operations[`grant:${operation}`].actor_id, h.admin.id);
  assert.equal(stored.operations[`grant:${operation}`].reason, "Manual research support");
  assert.equal(stored.operations[`grant:${operation}`].target_email, h.user.email);
  assert.equal(h.bucket.writes.filter((key) => key === keyFor(h.user.id)).length, 1);
  assert.equal(JSON.stringify(first.data).includes("actor_email"), false);
});

test("only super may read or grant, invalid users and amounts never create a credit ledger", async () => {
  const h = setup();
  for (const actor of [null, h.user]) {
    for (const method of ["GET", "POST"]) {
      const result = await h.request(method, { email: h.user.email, amount: 1, reason: "x", operation_id: randomUUID() }, actor);
      assert.equal(result.response.status, 403);
    }
  }
  for (const amount of [0, -1, 1.5, "2", 10001, null]) {
    assert.equal((await h.grant(amount)).response.status, 400);
  }
  assert.equal((await h.grant(1, randomUUID(), { reason: "" })).response.status, 400);
  assert.equal((await h.grant(1, "not-an-operation-id")).response.status, 400);
  assert.equal((await h.grant(1, randomUUID(), { email: "unknown@example.invalid" })).response.status, 404);
  assert.equal(h.bucket.value(keyFor(h.user.id)), null);
});

test("concurrent unique and repeated grants cannot lose or duplicate additions", async () => {
  const h = setup();
  const shared = randomUUID();
  const results = await Promise.all([h.grant(3, shared), h.grant(3, shared), h.grant(4), h.grant(5)]);
  assert.ok(results.every((row) => row.response.status === 200));
  assert.equal(results.filter((row) => row.data.deduplicated).length, 1);
  const { data } = await h.request();
  assert.equal(data.credits.balance, 12);
  assert.equal(data.credits.total_granted, 12);
  assert.equal(Object.keys(h.bucket.value(keyFor(h.user.id)).operations).length, 3);
});

test("a grant with a lost success response is recovered by the same operation ID", async () => {
  const h = setup();
  const operation = randomUUID();
  h.bucket.throwAfterPutPrefix = keyFor(h.user.id);
  assert.equal((await h.grant(4, operation)).response.status, 503);
  const retry = await h.grant(4, operation);
  assert.equal(retry.response.status, 200);
  assert.equal(retry.data.deduplicated, true);
  assert.equal(retry.data.credits.balance, 4);
});

test("included allowance is consumed first and extra credits persist independently of daily periods", async () => {
  const h = setup();
  await h.grant(2);
  const policy = await quota.policy(h.env, h.user, "");
  const first = await quota.reserve(h.env, policy);
  assert.equal(first.reservation.source, "included");
  assert.deepEqual(first.usage, { tier: "registered", limit: 1, count: 1, remaining: 0, period: "lifetime" });
  assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 2);
  const second = await quota.reserve(h.env, policy);
  assert.equal(second.usage.debit_source, "credits");
  assert.equal(second.usage.count, 1, "extra consumption must not rewrite the included counter");
  assert.equal(second.usage.extra_credits_remaining, 1);
  const daily = { ...policy, tier: "member", period: "day", limit: 2 };
  assert.equal((await quota.reserve(h.env, daily)).reservation.source, "included");
  assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 1);
});

test("concurrent consumption never exceeds included plus granted credits", async () => {
  const h = setup();
  await h.grant(2);
  const policy = await quota.policy(h.env, h.user, "");
  const results = await Promise.allSettled(Array.from({ length: 8 }, () => quota.reserve(h.env, policy)));
  const successful = results.filter((row) => row.status === "fulfilled").map((row) => row.value);
  assert.equal(successful.length, 3);
  assert.equal(successful.filter((row) => row.reservation.source === "included").length, 1);
  assert.equal(successful.filter((row) => row.usage.debit_source === "credits").length, 2);
  assert.ok(results.filter((row) => row.status === "rejected").every((row) => row.reason.name === "ReportChatLimitError"));
  assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 0);
  assert.equal(h.bucket.value(keyFor(h.user.id)).total_consumed, 2);
});

test("concurrent duplicate refunds and grants return exactly one credit to its source", async () => {
  const h = setup();
  await h.grant(1);
  const policy = await quota.policy(h.env, h.user, "");
  const included = await quota.reserve(h.env, policy);
  const extra = await quota.reserve(h.env, policy);
  await Promise.all([quota.release(h.env, policy, extra.reservation), quota.release(h.env, policy, extra.reservation), h.grant(3)]);
  let stored = h.bucket.value(keyFor(h.user.id));
  assert.equal(stored.balance, 4);
  assert.equal(stored.total_consumed, 0);
  const replacement = await quota.reserve(h.env, policy);
  assert.equal(replacement.usage.debit_source, "credits", "credit refund must not release included allowance");
  await Promise.all([quota.release(h.env, policy, included.reservation), quota.release(h.env, policy, included.reservation)]);
  assert.equal((await quota.reserve(h.env, policy)).reservation.source, "included");
  stored = h.bucket.value(keyFor(h.user.id));
  assert.equal(stored.balance, 3, "included refunds must not mint an extra credit");
});

test("included refunds use the original dated bucket, not the next day's allowance", async () => {
  const h = setup();
  const policy = { ...(await quota.policy(h.env, h.user, "")), period: "day", tier: "member", limit: 2 };
  const day = "2020-01-01";
  const key = `_account/report-chat-v3/daily/account/${encodeURIComponent(h.user.email)}/${day}`;
  const id = randomUUID();
  h.bucket.seed(key, { count: 1, reservations: { [id]: "debited" } });
  const current = await quota.reserve(h.env, policy);
  await quota.release(h.env, policy, { source: "included", id, date: day, key });
  assert.equal(h.bucket.value(key).count, 0);
  assert.equal(h.bucket.value(current.reservation.key).count, 1);
});

test("guest included quota and unlimited super remain separate from manual credits", async () => {
  const h = setup();
  await h.grant(10);
  const guest = await quota.policy(h.env, null, "guest-device-123456");
  await quota.reserve(h.env, guest);
  await assert.rejects(quota.reserve(h.env, guest), { name: "ReportChatLimitError" });
  const superPolicy = await quota.policy(h.env, h.admin, "");
  assert.deepEqual((await quota.reserve(h.env, superPolicy)).usage,
    { tier: "admin", limit: null, count: 0, remaining: null, period: "unlimited" });
  assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 10);
});

test("real report request failures refund included and credit debits, including lost write responses", async () => {
  for (const credit of [false, true]) {
    for (const uncertain of [false, true]) {
      const h = setup();
      await h.grant(1);
      const policy = await quota.policy(h.env, h.user, "");
      if (credit) await quota.reserve(h.env, policy);
      if (uncertain) h.bucket.throwAfterPutPrefix = credit ? keyFor(h.user.id) : "_account/report-chat-v3/";
      const response = await worker.fetch(new Request("https://portal.example.invalid/api/report-chat", {
        method: "POST", headers: { "Content-Type": "application/json", Authorization: `Bearer ${token(h.user)}` },
        body: JSON.stringify({ question: "AI research fixtures" }),
      }), h.env, { waitUntil() {} });
      assert.equal(response.status, 503);
      assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 1);
      const next = await quota.reserve(h.env, policy);
      assert.equal(next.reservation.source, credit ? "credits" : "included");
    }
  }
});

test("corrupt credit state and sustained CAS contention fail closed without modifying balances", async () => {
  const h = setup();
  await h.grant(3);
  h.bucket.rejectWrites = true;
  const busy = await h.grant(2);
  assert.equal(busy.response.status, 409);
  assert.equal(busy.data.code, "CREDIT_BUSY");
  assert.equal(h.bucket.value(keyFor(h.user.id)).balance, 3);
  h.bucket.seed(keyFor(h.user.id), { ...h.bucket.value(keyFor(h.user.id)), balance: 99 });
  const broken = await h.request();
  assert.equal(broken.response.status, 503);
  assert.equal(broken.data.code, "CREDIT_STORAGE");
});

test("a signed-in reader sees only their own balance and included allowance", async () => {
  const h = setup();
  await h.grant(4);
  const url = "https://portal.example.invalid/api/account/ai-research-credits?email=other@example.invalid";
  const response = await worker.fetch(new Request(url, { headers: { Authorization: `Bearer ${token(h.user)}` } }), h.env, { waitUntil() {} });
  assert.equal(response.status, 200);
  const data = await response.json();
  assert.equal(data.credits.balance, 4);
  assert.equal(data.usage.remaining, 1);
  assert.equal(JSON.stringify(data).includes("operations"), false);
  const anonymous = await worker.fetch(new Request(url), h.env, { waitUntil() {} });
  assert.equal(anonymous.status, 401);
  assert.equal((await anonymous.json()).code, "CREDIT_AUTH");
});
