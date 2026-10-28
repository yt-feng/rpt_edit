import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";
import { ACK_TAG, assertAcknowledgement } from "./form-acknowledgement-fixture.mjs";

const ORIGIN = "https://portal.example.invalid";
const ACK_PREFIX = "_form-acknowledgements/v1/items/";
const OWNER = "owner@example.invalid";
const READER = "reader@example.net";

class MemoryR2 {
  rows = new Map();
  version = 0;
  failAckWrite = false;
  async get(key) {
    const row = this.rows.get(String(key));
    if (!row) return null;
    return { etag: row.etag, async text() { return row.value; }, async json() { return JSON.parse(row.value); } };
  }
  async put(key, value, options = {}) {
    if (this.failAckWrite && String(key).startsWith(ACK_PREFIX)) throw new Error("synthetic acknowledgement storage error");
    const current = this.rows.get(key), onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && current?.etag !== onlyIf.etagMatches) return null;
    if (onlyIf.etagDoesNotMatch === "*" && current) return null;
    const row = { value: typeof value === "string" ? value : new TextDecoder().decode(value), etag: `v${++this.version}`, httpMetadata: options.httpMetadata };
    this.rows.set(key, row);
    return { etag: row.etag };
  }
  async delete(key) { this.rows.delete(key); }
  async list({ prefix = "", limit = 1000, cursor = "0" } = {}) {
    const all = [...this.rows.keys()].filter((key) => key.startsWith(prefix)).sort();
    const start = Number(cursor), keys = all.slice(start, start + limit);
    return { objects: keys.map((key) => ({ key, etag: this.rows.get(key).etag })), truncated: start + keys.length < all.length, cursor: String(start + keys.length) };
  }
  json(prefix) { return [...this.rows].filter(([key]) => key.startsWith(prefix)).map(([key, row]) => ({ key, ...JSON.parse(row.value) })); }
}

function fixture() {
  const bucket = new MemoryR2();
  return { bucket, env: {
    REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", MASTER_KEY: "form-acknowledgement-test-secret",
    ALLOWED_ORIGIN: ORIGIN, NEWSFEED_EMAIL_PROVIDER: "brevo", BREVO_API_KEY: "fixture-only",
    BREVO_SENDER_EMAIL: "owner-notices@example.invalid", BREVO_SENDER_NAME: "Owner notices",
    OWNER_NOTIFICATION_EMAIL: OWNER,
  } };
}

async function request(env, route, body, headers = {}) {
  const pending = [];
  const response = await worker.fetch(new Request(`https://worker.example.invalid${route}`, {
    ...(body === undefined ? {} : { method: "POST", body: JSON.stringify(body) }),
    headers: { "Content-Type": "application/json", Origin: ORIGIN, "CF-Connecting-IP": "203.0.113.89", ...headers },
  }), env, { waitUntil(promise) { pending.push(promise); } });
  await Promise.all(pending);
  return { response, data: await response.json() };
}

function formBody(extra = {}) {
  return { report_id: "report-001", source: "catalog", title: "Example report", page_path: "/report.html?id=report-001", requester_email: READER, honeypot: "", ...extra };
}

function success(id = "fixture-message") { return new Response(JSON.stringify({ messageId: id }), { status: 201 }); }

function mockDelivery(t, handler) {
  const sent = [];
  t.mock.method(globalThis, "fetch", async (url, init = {}) => {
    assert.equal(String(url), "https://api.brevo.com/v3/smtp/email", "all delivery tests must remain offline");
    const body = JSON.parse(String(init.body || "{}"));
    sent.push(body);
    return handler ? handler(body, sent.length) : success(`message-${sent.length}`);
  });
  return sent;
}

test("report acknowledgements use fixed bilingual contact copy and ignore forged sender and recipients", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t);
  const result = await request(env, "/report-request", formBody({
    sender: { email: "attacker@example.net" }, from: "attacker@example.net", to: "attacker@example.net",
    recipient: "attacker@example.net", cc: "attacker@example.net", bcc: "attacker@example.net",
    subject: "attacker subject", text: "attacker text", html: "<script>attacker</script>",
  }));
  assert.equal(result.response.status, 202);
  assert.equal(sent.length, 2);
  assert.deepEqual(sent[0].to, [{ email: OWNER }]);
  assert.equal(sent[0].sender.email, env.BREVO_SENDER_EMAIL);
  assertAcknowledgement(sent[1], READER);
  assert.doesNotMatch(JSON.stringify(sent[1]), /attacker|<script>/u);
  const ledger = bucket.json(ACK_PREFIX);
  assert.equal(ledger.length, 1);
  assert.equal(ledger[0].status, "sent");
  assert.equal(ledger[0].message_id, "message-2");
  assert.ok(ledger[0].sent_at);
  assert.equal(bucket.rows.get(ledger[0].key).httpMetadata.cacheControl, "private, no-store");
  assert.doesNotMatch(JSON.stringify(result.data), /reader@example|message-2|acknowledgement|brevo/u);
});

test("membership acknowledgement binds authenticated recipient and leaves owner delivery intact", async (t) => {
  const { env, bucket } = fixture();
  const user = { id: "user-1", username: "member", email: "member@example.net", email_is_generated: false, created_at: new Date().toISOString() };
  await bucket.put(`_account/users/username/${user.username}`, JSON.stringify(user));
  const payload = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, session_epoch: "", exp: Math.floor(Date.now() / 1000) + 3600 })).toString("base64url");
  const signature = createHmac("sha256", env.MASTER_KEY).update(`portal:account-token:v1:${payload}`).digest("base64url");
  const sent = mockDelivery(t);
  const result = await request(env, "/membership/request", {
    requester_email: "spoofed@example.net", contact_channel: "wechat", contact_value: "fixture-contact",
    note: "Please help", request_kind: "support", to: "attacker@example.net",
  }, { Authorization: `Bearer ${payload}.${signature}` });
  assert.equal(result.response.status, 202, JSON.stringify(result.data));
  assert.equal(sent.length, 2);
  assert.deepEqual(sent[0].to, [{ email: OWNER }]);
  assertAcknowledgement(sent[1], user.email);
  assert.doesNotMatch(JSON.stringify(sent[1]), /spoofed|attacker/u);
});

test("concurrent and repeated submissions send one owner notification and one acknowledgement", async (t) => {
  const { env, bucket } = fixture();
  let release, started;
  const ackStarted = new Promise((resolve) => { started = resolve; });
  const ackRelease = new Promise((resolve) => { release = resolve; });
  const sent = mockDelivery(t, async (email) => {
    if (email.tags.includes(ACK_TAG)) { started(); await ackRelease; }
    return success();
  });
  const first = request(env, "/report-request", formBody());
  await ackStarted;
  const duplicates = await Promise.all(Array.from({ length: 4 }, () => request(env, "/report-request", formBody())));
  assert.ok(duplicates.every((result) => result.data.deduplicated));
  assert.equal(sent.length, 2);
  assert.equal(bucket.json(ACK_PREFIX)[0].status, "pending");
  release();
  assert.equal((await first).response.status, 202);
  await request(env, "/report-request", formBody());
  assert.equal(sent.length, 2);
  assert.equal(bucket.json(ACK_PREFIX)[0].status, "sent");
});

for (const outcome of ["rejected", "unknown"]) {
  test(`an acknowledgement ${outcome} outcome preserves accepted form and is not automatically repeated`, async (t) => {
    const { env, bucket } = fixture();
    const sent = mockDelivery(t, (email) => {
      if (!email.tags.includes(ACK_TAG)) return success("owner-message");
      if (outcome === "unknown") throw new Error("synthetic network interruption");
      return new Response(JSON.stringify({ message: "synthetic provider rejection" }), { status: 503 });
    });
    const first = await request(env, "/report-request", formBody());
    assert.equal(first.response.status, 202);
    assert.equal(first.data.ok, true);
    assert.equal(bucket.json("_report-requests/v1/items/")[0].status, "sent");
    assert.equal(bucket.json(ACK_PREFIX)[0].status, outcome === "unknown" ? "outcome_unknown" : "failed");
    assert.doesNotMatch(JSON.stringify(first.data), /synthetic|provider|interruption/u);
    const duplicate = await request(env, "/report-request", formBody());
    assert.equal(duplicate.data.deduplicated, true);
    assert.equal(sent.length, 2);
  });
}

test("acknowledgement storage failure preserves accepted request and a later duplicate can fill the unsent gap", async (t) => {
  const { env, bucket } = fixture();
  bucket.failAckWrite = true;
  t.mock.method(console, "error", () => {});
  const sent = mockDelivery(t);
  assert.equal((await request(env, "/report-request", formBody())).response.status, 202);
  assert.equal(sent.length, 1, "no acknowledgement may send without a durable reservation");
  assert.equal(bucket.json(ACK_PREFIX).length, 0);
  bucket.failAckWrite = false;
  const duplicate = await request(env, "/report-request", formBody());
  assert.equal(duplicate.data.deduplicated, true);
  assert.equal(sent.length, 2);
  assertAcknowledgement(sent[1], READER);
});

test("invalid, honeypot and owner-rejected forms never send an acknowledgement", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t, () => new Response(JSON.stringify({ message: "owner delivery failed" }), { status: 503 }));
  assert.equal((await request(env, "/report-request", formBody({ requester_email: "invalid" }))).response.status, 400);
  assert.equal((await request(env, "/report-request", formBody({ honeypot: "bot" }))).response.status, 202);
  assert.equal((await request(env, "/report-request", formBody())).response.status, 502);
  assert.equal(sent.length, 1);
  assert.deepEqual(sent[0].to, [{ email: OWNER }]);
  assert.equal(bucket.json(ACK_PREFIX).length, 0);
});

async function auth(env, action = "register", extra = {}, route = "/auth") {
  const captcha = await request(env, "/captcha");
  const svg = Buffer.from(captcha.data.image.split(",")[1], "base64").toString("utf8");
  const [, left, right] = svg.match(/>(\d+) \+ (\d+) = \?</u);
  return request(env, route, { action, username: "new-reader", email: READER, password: "test-password-123", captcha_token: captcha.data.token, captcha_answer: String(Number(left) + Number(right)), ...extra });
}

test("new registration sends one welcome receipt; account recovery and login do not resend it", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t);
  const created = await auth(env);
  assert.equal(created.response.status, 201, JSON.stringify(created.data));
  assert.ok(created.data.token);
  assert.equal(sent.length, 1);
  assertAcknowledgement(sent[0], READER);
  assert.doesNotMatch(JSON.stringify(sent[0]), /test-password|new-reader/u);
  assert.equal((await auth(env)).response.status, 200, "matching account registration recovers existing account");
  assert.equal((await auth(env, "login")).response.status, 200);
  assert.equal((await auth(env, "register", { password: "different-password" })).response.status, 409);
  assert.equal(sent.length, 1);
  assert.equal(bucket.json(ACK_PREFIX).length, 1);
});

test("welcome provider failure never rolls back new registration", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t, () => new Response("{}", { status: 503 }));
  const created = await auth(env);
  assert.equal(created.response.status, 201);
  assert.ok(created.data.token);
  assert.equal(bucket.json(ACK_PREFIX)[0].status, "failed");
  assert.equal((await auth(env, "login")).response.status, 200);
  assert.equal(sent.length, 1);
});


for (const route of ["/auth", "/api/auth"]) {
  test(`${route} refuses new Mailinator accounts without writes or email delivery`, async (t) => {
    const { env, bucket } = fixture();
    const sent = mockDelivery(t);
    for (const email of ["reader@mailinator.com", "  Reader@MAILINATOR.COM  ", "reader@sub.mailinator.com", "reader@mailinator.com."]) {
      const rejected = await auth(env, "register", { email }, route);
      assert.equal(rejected.response.status, 400, JSON.stringify(rejected.data));
      assert.equal(rejected.data.code, "EMAIL_DOMAIN_BLOCKED");
      assert.match(rejected.data.detail, /请使用其他邮箱/u);
      assert.equal(bucket.rows.size, 0, "blocked signup must not create users, acknowledgement reservations, or other records");
      assert.equal(sent.length, 0, "blocked signup must not send verification or welcome email");
      assert.equal(rejected.data.token, undefined);
    }
  });
}

test("signup domain matching keeps other email domains and similar names eligible", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t);
  for (const [index, email] of ["reader@example.net", "reader@notmailinator.com", "reader@mailinator.com.example.net"].entries()) {
    const created = await auth(env, "register", { username: `allowed-reader-${index}`, email });
    assert.equal(created.response.status, 201, JSON.stringify(created.data));
    assert.equal(created.data.user.email, email);
    assert.ok(created.data.token);
  }
  assert.equal(sent.length, 3);
  assert.equal(bucket.json(ACK_PREFIX).length, 3);
});

function seedAuthUser(bucket, env, identity, password) {
  const salt = "registration-domain-test-salt";
  const hash = createHmac("sha256", env.MASTER_KEY)
    .update(`user-password:${salt}:${password}`).digest("hex");
  const user = {
    ...identity, email_is_generated: false,
    password_salt: salt, password_hash: `hmac_sha256$${hash}`,
    created_at: "2026-01-01T00:00:00.000Z", updated_at: "2026-01-01T00:00:00.000Z",
  };
  for (const field of ["id", "username", "email"]) {
    bucket.rows.set(`_account/users/${field}/${encodeURIComponent(user[field])}`, {
      value: JSON.stringify(user), etag: `seed-${field}`,
    });
  }
  return user;
}

function authToken(env, user) {
  const now = Math.floor(Date.now() / 1000);
  const payload = Buffer.from(JSON.stringify({
    kind: "user", sub: user.id, username: user.username, email: user.email,
    session_epoch: "", iat: now, exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", env.MASTER_KEY)
    .update(`portal:account-token:v1:${payload}`).digest("base64url");
  return `${payload}.${signature}`;
}

test("an existing Mailinator user can still log in, refresh a session, and recover the same account", async (t) => {
  const { env, bucket } = fixture();
  const sent = mockDelivery(t);
  const user = seedAuthUser(bucket, env, {
    id: "existing-mailinator-id", username: "existing-reader", email: "existing-reader@mailinator.com",
  }, "test-password-123");
  for (const action of ["login", "register"]) {
    const result = await auth(env, action, { username: user.username, email: user.email });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.user.id, user.id);
    assert.ok(result.data.token);
  }
  const refreshed = await request(env, "/api/auth", undefined, { Authorization: `Bearer ${authToken(env, user)}` });
  assert.equal(refreshed.response.status, 200);
  assert.equal(refreshed.data.user.id, user.id);
  assert.equal(sent.length, 0);
  assert.equal(bucket.json(ACK_PREFIX).length, 0);
});

for (const route of ["/account-admin/user", "/api/account-admin/user"]) {
  test(`${route} applies the same new-account email rule`, async (t) => {
    const { env, bucket } = fixture();
    const sent = mockDelivery(t);
    const admin = seedAuthUser(bucket, env, {
      id: "domain-admin-id", username: "admin-a", email: "admin-a@users.portal.example.invalid",
    }, "test-password-123");
    const before = [...bucket.rows.entries()];
    const rejected = await request(env, route, {
      username: "admin-created-reader", email: "reader@SUB.MAILINATOR.COM", password: "test-password-123",
    }, { Authorization: `Bearer ${authToken(env, admin)}` });
    assert.equal(rejected.response.status, 400, JSON.stringify(rejected.data));
    assert.equal(rejected.data.code, "EMAIL_DOMAIN_BLOCKED");
    assert.deepEqual([...bucket.rows.entries()], before, "admin creation rejection must not mutate existing accounts or write new rows");
    assert.equal(sent.length, 0);
  });
}
