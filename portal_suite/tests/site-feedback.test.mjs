import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";
import { assertAcknowledgement } from "./form-acknowledgement-fixture.mjs";

const ORIGIN = "https://portal.example.invalid";
const OWNER = "feedback-owner@example.net";
class MemoryR2 {
  data = new Map(); version = 0;
  async get(key) {
    const row = this.data.get(key);
    return row ? { etag: row.etag, text: async () => row.body, json: async () => JSON.parse(row.body) } : null;
  }
  async put(key, body, options = {}) {
    const prior = this.data.get(key), condition = options.onlyIf || {};
    if (condition.etagDoesNotMatch === "*" && prior) return null;
    if (condition.etagMatches && prior?.etag !== condition.etagMatches) return null;
    const row = { body: String(body), etag: `v${++this.version}`, metadata: options.httpMetadata };
    this.data.set(key, row); return { etag: row.etag };
  }
  rows(prefix) { return [...this.data].filter(([key]) => key.startsWith(prefix)).map(([key, row]) => ({ key, ...JSON.parse(row.body), metadata: row.metadata })); }
}
function fixture(t, handler) {
  const bucket = new MemoryR2(), sent = [];
  const env = { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", MASTER_KEY: "feedback-fixture-secret", ALLOWED_ORIGIN: ORIGIN,
    NEWSFEED_EMAIL_PROVIDER: "brevo", BREVO_API_KEY: "offline-fixture", BREVO_SENDER_EMAIL: "notices@example.invalid", OWNER_NOTIFICATION_EMAIL: OWNER };
  t.mock.method(globalThis, "fetch", async (url, options) => {
    assert.equal(String(url), "https://api.brevo.com/v3/smtp/email", "feedback tests must stay offline");
    const body = JSON.parse(options.body); sent.push(body);
    return handler ? handler(body, sent.length) : new Response(JSON.stringify({ messageId: `mail-${sent.length}` }), { status: 201 });
  });
  return { bucket, sent, env };
}
const body = (override = {}) => ({ category: "bug", message: "The search button did not respond.", requester_email: "guest@example.net", page_path: "/report.html?private=secret#details", honeypot: "", ...override });
async function submit(env, payload = body(), headers = {}, raw) {
  const response = await worker.fetch(new Request(`${ORIGIN}/api/feedback`, { method: "POST", headers: {
    "Content-Type": "application/json", Origin: ORIGIN, "CF-Connecting-IP": "203.0.113.123", ...headers }, body: raw === undefined ? JSON.stringify(payload) : raw }), env, { waitUntil() {} });
  return { status: response.status, headers: response.headers, data: await response.json() };
}

test("feedback persists safely and sends owner notification plus bilingual requester receipt", async (t) => {
  const { env, bucket, sent } = fixture(t);
  const result = await submit(env, body({ message: "Button <script>alert(1)</script> failed", recipient: "attacker@example.net", sender: "attacker@example.net" }));
  assert.equal(result.status, 202); assert.equal(result.data.ok, true);
  assert.equal(result.data.confirmation_email_sent, true);
  assert.equal(sent.length, 2); assert.deepEqual(sent[0].to, [{ email: OWNER }]);
  assert.deepEqual(sent[0].tags, ["portal-feedback"]);
  assert.match(sent[0].htmlContent, /&lt;script&gt;/u); assert.doesNotMatch(sent[0].htmlContent, /<script>|private=secret|attacker/u);
  assertAcknowledgement(sent[1], "guest@example.net");
  const audit = bucket.rows("_analytics/events/").filter(row => row.type === "form_confirmation");
  assert.equal(audit.length, 1); assert.equal(audit[0].status, "provider_accepted");
  assert.equal(audit[0].request_kind, "feedback"); assert.equal(audit[0].action, "provider_result");
  assert.equal(audit[0].user, null); assert.equal(audit[0].session_id, "");
  assert.doesNotMatch(JSON.stringify(audit), /guest@example|Button|script|attacker|mail-[0-9]/u);
  const [saved] = bucket.rows("_feedback/v1/items/");
  assert.equal(saved.status, "sent"); assert.equal(saved.page_path, "/report.html");
  assert.equal(saved.category, "bug"); assert.equal(saved.metadata.cacheControl, "private, no-store");
  assert.match(result.headers.get("Cache-Control"), /no-store/u);
});

test("feedback validates origin, content type, bounded fields, and honeypot without deliveries", async (t) => {
  const { env, sent } = fixture(t);
  assert.equal((await submit(env, body(), { Origin: "https://foreign.example" })).status, 403);
  assert.equal((await submit(env, body(), { "Content-Type": "text/plain" })).status, 415);
  assert.equal((await submit(env, body(), {}, "not-json")).status, 400);
  assert.equal((await submit(env, [])).status, 400);
  assert.equal((await submit(env, body({ category: "admin" }))).status, 400);
  assert.equal((await submit(env, body({ message: "x" }))).status, 400);
  assert.equal((await submit(env, body({ message: "x".repeat(2001) }))).status, 400);
  assert.equal((await submit(env, body({ message: "中".repeat(4000) }))).status, 413);
  assert.equal((await submit(env, body({ requester_email: "invalid" }))).status, 400);
  const trapped = await submit(env, body({ honeypot: "robot" }));
  assert.equal(trapped.status, 202); assert.equal(trapped.data.ok, true); assert.equal(sent.length, 0);
});

test("feedback duplicates and concurrent submissions send each email once", async (t) => {
  const { env, sent, bucket } = fixture(t);
  const results = await Promise.all([submit(env), submit(env)]);
  assert.ok(results.every((result) => result.status === 202));
  const again = await submit(env);
  assert.equal(again.data.deduplicated, true); assert.equal(sent.length, 2);
  assert.equal(bucket.rows("_feedback/v1/items/").length, 1);
  assert.equal(bucket.rows("_form-acknowledgements/v1/items/").length, 1);
  assert.equal(bucket.rows("_analytics/events/").filter(row => row.type === "form_confirmation").length, 1);
});

test("feedback applies the six-per-email limit to distinct requests", async (t) => {
  const { env, sent } = fixture(t);
  for (let i = 0; i < 6; i++) assert.equal((await submit(env, body({ message: `A unique issue number ${i}.` }))).status, 202);
  assert.equal((await submit(env, body({ message: "A seventh unique issue." }))).status, 429);
  assert.equal(sent.length, 12);
});

test("feedback uses authenticated account identity instead of forged guest email", async (t) => {
  const { env, bucket, sent } = fixture(t);
  const user = { id: "feedback-user", username: "feedback-member", email: "member@example.net", email_is_generated: false,
    created_at: new Date().toISOString(), updated_at: new Date().toISOString() };
  await bucket.put(`_account/users/username/${user.username}`, JSON.stringify(user));
  const now = Math.floor(Date.now() / 1000);
  const encoded = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, session_epoch: "", iat: now, exp: now + 3600 })).toString("base64url");
  const signature = createHmac("sha256", env.MASTER_KEY).update(`portal:account-token:v1:${encoded}`).digest("base64url");
  const result = await submit(env, body({ requester_email: "attacker@example.net" }), { Authorization: `Bearer ${encoded}.${signature}` });
  assert.equal(result.status, 202, JSON.stringify(result.data));
  assertAcknowledgement(sent[1], user.email); assert.doesNotMatch(JSON.stringify(sent), /attacker/u);
});

test("feedback owner failure stays retryable while receipt failure does not fail an accepted submission", async (t) => {
  const { env, bucket, sent } = fixture(t, (_body, count) => count === 1 || count === 3
    ? new Response(JSON.stringify({ message: "provider unavailable" }), { status: 503 })
    : new Response(JSON.stringify({ messageId: `mail-${count}` }), { status: 201 }));
  assert.equal((await submit(env)).status, 502);
  assert.equal(bucket.rows("_feedback/v1/items/")[0].status, "failed");
  const retried = await submit(env);
  assert.equal(retried.status, 202); assert.equal(retried.data.ok, true);
  assert.equal(retried.data.confirmation_email_sent, false);
  assert.equal(bucket.rows("_feedback/v1/items/")[0].status, "sent");
  assert.equal(bucket.rows("_form-acknowledgements/v1/items/")[0].status, "failed");
  const audit = bucket.rows("_analytics/events/").filter(row => row.type === "form_confirmation");
  assert.equal(audit.length, 1); assert.equal(audit[0].status, "failed");
  assert.equal((await submit(env)).data.deduplicated, true); assert.equal(sent.length, 3);
});

test("legacy accounts with generated or redacted emails can provide a real reply address", async (t) => {
  const { env, bucket, sent } = fixture(t);
  const legacyEmails = ["legacy@users.portal.example.invalid", "redacted@users.example.invalid"];
  for (const [index, email] of legacyEmails.entries()) {
    const user = { id: `legacy-feedback-${index}`, username: `legacy-feedback-${index}`, email, email_is_generated: true,
      created_at: new Date().toISOString(), updated_at: new Date().toISOString() };
    await bucket.put(`_account/users/username/${user.username}`, JSON.stringify(user));
    const now = Math.floor(Date.now() / 1000);
    const encoded = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email, session_epoch: "", iat: now, exp: now + 3600 })).toString("base64url");
    const signature = createHmac("sha256", env.MASTER_KEY).update(`portal:account-token:v1:${encoded}`).digest("base64url");
    const headers = { Authorization: `Bearer ${encoded}.${signature}` };
    assert.equal((await submit(env, body({ requester_email: email }), headers)).status, 400);
    const reply = `legacy-reply-${index}@example.net`;
    const accepted = await submit(env, body({ requester_email: reply }), headers);
    assert.equal(accepted.status, 202, JSON.stringify(accepted.data));
    assertAcknowledgement(sent.at(-1), reply);
    const saved = bucket.rows("_feedback/v1/items/").find((row) => row.requester_user_id === user.id);
    assert.equal(saved.authenticated, true); assert.equal(saved.requester_email, reply);
  }
});
