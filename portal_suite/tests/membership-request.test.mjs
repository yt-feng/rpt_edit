import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const { default: worker } = await import(workerPath);

const PORTAL_ORIGIN = "https://portal.example.invalid";
const CONTACT_CARD_KEY = "_private-assets/v1/member-contact-card.jpg";
const EXPECTED_CONTACT = ["info", "@", "kc", "desk", ".com"].join("");

class MemoryR2 {
  constructor() {
    this.data = new Map();
    this.version = 0;
    this.getKeys = [];
    this.putKeys = [];
  }

  seedJson(key, value) {
    this.version += 1;
    this.data.set(String(key), {
      value: JSON.stringify(value),
      binary: false,
      etag: `etag-${this.version}`,
      httpMetadata: { contentType: "application/json; charset=utf-8" },
    });
  }

  seedBytes(key, value) {
    this.version += 1;
    this.data.set(String(key), {
      value: new Uint8Array(value),
      binary: true,
      etag: `etag-${this.version}`,
      httpMetadata: { contentType: "image/jpeg" },
    });
  }

  async get(key) {
    this.getKeys.push(String(key));
    const row = this.data.get(String(key));
    if (!row) return null;
    const bytes = row.binary ? row.value : new TextEncoder().encode(row.value);
    return {
      etag: row.etag,
      body: bytes,
      size: bytes.byteLength,
      httpMetadata: row.httpMetadata,
      async text() { return row.binary ? new TextDecoder().decode(row.value) : row.value; },
    };
  }

  async put(key, value, options = {}) {
    const normalizedKey = String(key);
    this.putKeys.push(normalizedKey);
    const current = this.data.get(normalizedKey);
    const condition = options.onlyIf || {};
    if (condition.etagMatches && (!current || current.etag !== condition.etagMatches)) return null;
    if (condition.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const binary = value instanceof Uint8Array;
    const stored = {
      value: binary ? new Uint8Array(value) : String(value),
      binary,
      etag: `etag-${this.version}`,
      httpMetadata: options.httpMetadata || {},
    };
    this.data.set(normalizedKey, stored);
    return { etag: stored.etag };
  }

  jsonRows(prefix) {
    return [...this.data.entries()]
      .filter(([key, row]) => key.startsWith(prefix) && !row.binary)
      .map(([key, row]) => ({ key, value: JSON.parse(row.value), httpMetadata: row.httpMetadata }));
  }
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY: "membership-request-test-secret",
    ALLOWED_ORIGIN: PORTAL_ORIGIN,
    NEWSFEED_EMAIL_PROVIDER: "brevo",
    BREVO_API_KEY: "brevo-test-key",
    BREVO_SENDER_EMAIL: "sender@example.invalid",
    BREVO_SENDER_NAME: "KC桌面",
  };
}

function requestBody(overrides = {}) {
  return {
    requester_email: "reader@example.net",
    contact_channel: "wechat",
    contact_value: "reader-wechat",
    note: "Please contact me about membership.",
    request_kind: "membership",
    page_path: "/?request=membership",
    honeypot: "",
    ...overrides,
  };
}

async function postMembershipRequest(env, body, options = {}) {
  const headers = {
    ...(options.contentType === false ? {} : { "Content-Type": options.contentType || "application/json" }),
    ...(options.origin === false ? {} : { Origin: options.origin || PORTAL_ORIGIN }),
    "CF-Connecting-IP": options.ip || "203.0.113.40",
    ...(options.headers || {}),
  };
  const request = new Request("https://worker.example.invalid/membership/request", {
    method: "POST",
    headers,
    body: options.rawBody === undefined ? JSON.stringify(body) : options.rawBody,
  });
  const response = await worker.fetch(request, env, { waitUntil() {} });
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

async function getContactCard(env, options = {}) {
  const request = new Request("https://worker.example.invalid/membership/contact-card", {
    headers: options.token ? { Authorization: `Bearer ${options.token}` } : {},
  });
  return worker.fetch(request, env, { waitUntil() {} });
}

async function withMockFetch(mock, callback) {
  const original = globalThis.fetch;
  globalThis.fetch = mock;
  try {
    return await callback();
  } finally {
    globalThis.fetch = original;
  }
}

function brevoSuccess(messageId = "membership-message-1") {
  return new Response(JSON.stringify({ messageId }), {
    status: 201,
    headers: { "Content-Type": "application/json" },
  });
}

function seedUser(bucket, overrides = {}) {
  const now = new Date().toISOString();
  const user = {
    id: "member-user-1",
    username: "member-one",
    email: "member-one@example.net",
    email_is_generated: false,
    password_salt: "unused",
    password_hash: "unused",
    created_at: now,
    updated_at: now,
    ...overrides,
  };
  bucket.seedJson(`_account/users/username/${encodeURIComponent(user.username)}`, user);
  return user;
}

async function accountToken(secret, user, overrides = {}) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    session_epoch: "",
    iat: now,
    exp: now + 3600,
    ...overrides,
  })).toString("base64url");
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(`portal:account-token:v1:${body}`),
  );
  return `${body}.${Buffer.from(signature).toString("base64url")}`;
}

test("membership request rejects invalid origins, bodies, fields, and silently absorbs honeypots", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess();
  }, async () => {
    assert.equal((await postMembershipRequest(env, requestBody(), { origin: "https://foreign.example" })).response.status, 403);
    assert.equal((await postMembershipRequest(env, requestBody(), { origin: false })).response.status, 403);
    assert.equal((await postMembershipRequest(env, requestBody(), { contentType: "text/plain" })).response.status, 415);
    assert.equal((await postMembershipRequest(env, null, { rawBody: "{" })).response.status, 400);
    assert.equal((await postMembershipRequest(env, [], {})).response.status, 400);
    assert.equal((await postMembershipRequest(env, null, {
      rawBody: JSON.stringify({ note: "x".repeat(9000) }),
    })).response.status, 413);
    assert.equal((await postMembershipRequest(env, requestBody({ request_kind: "billing" }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ contact_channel: "email" }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ requester_email: "invalid" }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ requester_email: `${"x".repeat(250)}@example.net` }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ contact_value: "" }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ contact_value: "x".repeat(161) }))).response.status, 400);
    assert.equal((await postMembershipRequest(env, requestBody({ note: "x".repeat(601) }))).response.status, 400);
    const trapped = await postMembershipRequest(env, requestBody({ honeypot: "bot-filled" }));
    assert.equal(trapped.response.status, 202);
    assert.equal(trapped.data.ok, true);
  });
  assert.equal(sends, 0);
  assert.equal(bucket.jsonRows("_membership-requests/v1/").length, 0);
});

test("guest membership request persists privately before fixed-recipient delivery and never echoes PII", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let delivery = null;
  const body = requestBody({
    requester_email: "guest@example.net",
    contact_value: "guest-<wechat>",
    note: "Need <script>alert('x')</script> & membership",
    request_kind: "privacy",
    page_path: "https://portal.example.invalid/privacy.html?private=secret",
    recipient: "attacker@example.net",
    to: "attacker@example.net",
    subject: "Attacker subject",
  });
  const result = await withMockFetch(async (url, init) => {
    const pending = bucket.jsonRows("_membership-requests/v1/items/");
    assert.equal(pending.length, 1);
    assert.equal(pending[0].value.status, "pending");
    delivery = { url: String(url), body: JSON.parse(String(init.body || "{}")) };
    return brevoSuccess("guest-membership-message");
  }, () => postMembershipRequest(env, body));

  assert.equal(result.response.status, 202);
  assert.equal(result.data.ok, true);
  assert.equal(result.data.deduplicated, false);
  const publicPayload = JSON.stringify(result.data);
  for (const privateValue of [body.requester_email, body.contact_value, body.note, EXPECTED_CONTACT, "attacker@example.net", "brevo"]) {
    assert.equal(publicPayload.includes(privateValue), false, `response leaked ${privateValue}`);
  }
  assert.equal(delivery.url, "https://api.brevo.com/v3/smtp/email");
  assert.deepEqual(delivery.body.to, [{ email: EXPECTED_CONTACT }]);
  assert.deepEqual(delivery.body.tags, ["membership-request"]);
  assert.doesNotMatch(JSON.stringify(delivery.body), /attacker@example\.net|Attacker subject/u);
  assert.match(delivery.body.htmlContent, /guest-&lt;wechat&gt;/u);
  assert.match(delivery.body.htmlContent, /&lt;script&gt;alert\('x'\)&lt;\/script&gt; &amp; membership/u);
  assert.doesNotMatch(delivery.body.htmlContent, /<script>/u);

  const saved = bucket.jsonRows("_membership-requests/v1/items/");
  assert.equal(saved.length, 1);
  assert.equal(saved[0].value.status, "sent");
  assert.equal(saved[0].value.request_kind, "privacy");
  assert.equal(saved[0].value.requester_email, "guest@example.net");
  assert.equal(saved[0].value.contact_value, "guest-<wechat>");
  assert.equal(saved[0].value.page_path, "/privacy.html");
  assert.equal(saved[0].httpMetadata.cacheControl, "private, no-store");
  assert.ok(saved[0].value.sent_at);
  for (const row of bucket.jsonRows("_membership-requests/v1/rate/")) {
    const serialized = `${row.key}\n${JSON.stringify(row.value)}`;
    assert.doesNotMatch(serialized, /203\.0\.113\.40|guest@example\.net|guest-<wechat>/u);
  }
  assert.equal([...bucket.data.keys()].some((key) => key.startsWith("_analytics/")), false);
});

test("authenticated membership requests bind the current account and reject invalid or disabled sessions", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const user = seedUser(bucket);
  const token = await accountToken(env.MASTER_KEY, user);
  let delivery = null;
  const accepted = await withMockFetch(async (_url, init) => {
    delivery = JSON.parse(String(init.body || "{}"));
    return brevoSuccess("account-membership-message");
  }, () => postMembershipRequest(env, requestBody({
    requester_email: "spoofed@example.net",
    contact_channel: "telegram",
    contact_value: "@member_one",
    requester_user_id: "attacker-id",
    recipient: "attacker@example.net",
  }), { headers: { Authorization: `Bearer ${token}` } }));
  assert.equal(accepted.response.status, 202);
  assert.match(delivery.textContent, /member-one@example\.net/u);
  assert.doesNotMatch(delivery.textContent, /spoofed@example\.net|attacker-id|attacker@example\.net/u);
  const saved = bucket.jsonRows("_membership-requests/v1/items/")[0].value;
  assert.equal(saved.authenticated, true);
  assert.equal(saved.requester_email, user.email);
  assert.equal(saved.requester_user_id, user.id);

  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess();
  }, async () => {
    const invalid = await postMembershipRequest(env, requestBody({ contact_value: "invalid-token-contact" }), {
      headers: { Authorization: "Bearer invalid.token" },
    });
    assert.equal(invalid.response.status, 401);

    const disabledBucket = new MemoryR2();
    const disabledEnv = envFor(disabledBucket);
    const disabledUser = seedUser(disabledBucket, {
      id: "disabled-user-1",
      username: "disabled-one",
      email: "disabled@example.net",
    });
    disabledBucket.seedJson(`_account/user-state/id/${encodeURIComponent(disabledUser.id)}`, {
      user_id: disabledUser.id,
      email: disabledUser.email,
      disabled: true,
      account_status: "disabled",
      updated_at: new Date().toISOString(),
    });
    const disabledToken = await accountToken(disabledEnv.MASTER_KEY, disabledUser);
    const disabled = await postMembershipRequest(disabledEnv, requestBody(), {
      headers: { Authorization: `Bearer ${disabledToken}` },
    });
    assert.equal(disabled.response.status, 403);
    assert.doesNotMatch(JSON.stringify(disabled.data), /@|email|邮箱/iu);
  });
  assert.equal(sends, 0);
});

test("all supported request kinds and contact channels are accepted", async () => {
  const kinds = ["membership", "support", "privacy", "refund", "access"];
  const channels = ["wechat", "whatsapp", "telegram"];
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess(`matrix-${sends}`);
  }, async () => {
    for (const [index, requestKind] of kinds.entries()) {
      const bucket = new MemoryR2();
      const result = await postMembershipRequest(envFor(bucket), requestBody({
        requester_email: `kind-${index}@example.net`,
        contact_value: `kind-contact-${index}`,
        request_kind: requestKind,
      }), { ip: `203.0.113.${60 + index}` });
      assert.equal(result.response.status, 202, requestKind);
    }
    for (const [index, channel] of channels.entries()) {
      const bucket = new MemoryR2();
      const result = await postMembershipRequest(envFor(bucket), requestBody({
        requester_email: `channel-${index}@example.net`,
        contact_channel: channel,
        contact_value: `channel-contact-${index}`,
      }), { ip: `203.0.113.${80 + index}` });
      assert.equal(result.response.status, 202, channel);
    }
  });
  assert.equal(sends, kinds.length + channels.length);
});

test("successful requests deduplicate and failed provider attempts remain retryable without leaking provider errors", async () => {
  const dedupeBucket = new MemoryR2();
  const dedupeEnv = envFor(dedupeBucket);
  let dedupeSends = 0;
  await withMockFetch(async () => {
    dedupeSends += 1;
    return brevoSuccess("dedupe-success");
  }, async () => {
    const first = await postMembershipRequest(dedupeEnv, requestBody());
    const duplicate = await postMembershipRequest(dedupeEnv, requestBody({ note: "A changed note" }));
    assert.equal(first.response.status, 202);
    assert.equal(duplicate.response.status, 202);
    assert.equal(duplicate.data.deduplicated, true);
  });
  assert.equal(dedupeSends, 1);

  const retryBucket = new MemoryR2();
  const retryEnv = envFor(retryBucket);
  let attempts = 0;
  await withMockFetch(async () => {
    attempts += 1;
    if (attempts === 1) {
      return new Response(JSON.stringify({ message: "private provider failure" }), {
        status: 503,
        headers: { "Content-Type": "application/json" },
      });
    }
    return brevoSuccess("retry-success");
  }, async () => {
    const failed = await postMembershipRequest(retryEnv, requestBody());
    assert.equal(failed.response.status, 502);
    assert.equal(failed.data.retryable, true);
    assert.doesNotMatch(JSON.stringify(failed.data), /private provider failure|brevo/u);
    assert.equal(retryBucket.jsonRows("_membership-requests/v1/items/")[0].value.status, "failed");

    const retried = await postMembershipRequest(retryEnv, requestBody());
    assert.equal(retried.response.status, 202);
    assert.equal(retried.data.deduplicated, false);
    const completed = retryBucket.jsonRows("_membership-requests/v1/items/")[0].value;
    assert.equal(completed.status, "sent");
    assert.equal(completed.attempt_count, 2);

    const duplicate = await postMembershipRequest(retryEnv, requestBody());
    assert.equal(duplicate.data.deduplicated, true);
  });
  assert.equal(attempts, 2);
});

test("membership requests enforce identity, contact, and IP rolling limits", async () => {
  const identityBucket = new MemoryR2();
  const identityEnv = envFor(identityBucket);
  let identitySends = 0;
  await withMockFetch(async () => {
    identitySends += 1;
    return brevoSuccess(`identity-${identitySends}`);
  }, async () => {
    for (let index = 0; index < 6; index += 1) {
      const accepted = await postMembershipRequest(identityEnv, requestBody({
        contact_value: `identity-contact-${index}`,
      }));
      assert.equal(accepted.response.status, 202);
    }
    const limited = await postMembershipRequest(identityEnv, requestBody({ contact_value: "identity-contact-6" }));
    assert.equal(limited.response.status, 429);
  });
  assert.equal(identitySends, 6);

  const contactBucket = new MemoryR2();
  const contactEnv = envFor(contactBucket);
  let contactSends = 0;
  await withMockFetch(async () => {
    contactSends += 1;
    return brevoSuccess(`contact-${contactSends}`);
  }, async () => {
    for (let index = 0; index < 6; index += 1) {
      const accepted = await postMembershipRequest(contactEnv, requestBody({
        requester_email: `contact-${index}@example.net`,
        contact_value: "shared-contact",
      }));
      assert.equal(accepted.response.status, 202);
    }
    const limited = await postMembershipRequest(contactEnv, requestBody({
      requester_email: "contact-limited@example.net",
      contact_value: "shared-contact",
    }));
    assert.equal(limited.response.status, 429);
  });
  assert.equal(contactSends, 6);

  const ipBucket = new MemoryR2();
  const ipEnv = envFor(ipBucket);
  let ipSends = 0;
  await withMockFetch(async () => {
    ipSends += 1;
    return brevoSuccess(`ip-${ipSends}`);
  }, async () => {
    for (let index = 0; index < 20; index += 1) {
      const accepted = await postMembershipRequest(ipEnv, requestBody({
        requester_email: `ip-${index}@example.net`,
        contact_value: `ip-contact-${index}`,
      }), { ip: "203.0.113.99" });
      assert.equal(accepted.response.status, 202);
    }
    const limited = await postMembershipRequest(ipEnv, requestBody({
      requester_email: "ip-limited@example.net",
      contact_value: "ip-contact-limited",
    }), { ip: "203.0.113.99" });
    assert.equal(limited.response.status, 429);
  });
  assert.equal(ipSends, 20);
});

test("contact card is read only after active account authentication and always uses private response headers", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const anonymous = await getContactCard(env);
  assert.equal(anonymous.status, 401);
  assert.equal(bucket.getKeys.includes(CONTACT_CARD_KEY), false);

  const invalid = await getContactCard(env, { token: "invalid.token" });
  assert.equal(invalid.status, 401);
  assert.equal(bucket.getKeys.includes(CONTACT_CARD_KEY), false);

  const user = seedUser(bucket);
  const expiredToken = await accountToken(env.MASTER_KEY, user, { exp: Math.floor(Date.now() / 1000) - 60 });
  const expired = await getContactCard(env, { token: expiredToken });
  assert.equal(expired.status, 401);
  assert.equal(bucket.getKeys.includes(CONTACT_CARD_KEY), false);

  const token = await accountToken(env.MASTER_KEY, user);
  const missing = await getContactCard(env, { token });
  assert.equal(missing.status, 404);
  bucket.seedBytes(CONTACT_CARD_KEY, [60, 115, 118, 103, 62]);
  const corrupt = await getContactCard(env, { token });
  assert.equal(corrupt.status, 503);
  assert.match(corrupt.headers.get("content-type"), /^application\/json/u);
  assert.doesNotMatch(await corrupt.text(), /<svg>/u);
  bucket.seedBytes(CONTACT_CARD_KEY, [255, 216, 255, 217]);
  const accepted = await getContactCard(env, { token });
  assert.equal(accepted.status, 200);
  assert.equal(accepted.headers.get("content-type"), "image/jpeg");
  assert.equal(accepted.headers.get("cache-control"), "private, no-store, max-age=0");
  assert.equal(accepted.headers.get("pragma"), "no-cache");
  assert.equal(accepted.headers.get("x-content-type-options"), "nosniff");
  assert.equal(accepted.headers.get("content-length"), "4");
  assert.equal(accepted.headers.has("etag"), false);
  assert.deepEqual([...new Uint8Array(await accepted.arrayBuffer())], [255, 216, 255, 217]);
  assert.equal(bucket.getKeys.some((key) => key.includes("/entitlements/")), false);

  const disabledBucket = new MemoryR2();
  const disabledEnv = envFor(disabledBucket);
  const disabledUser = seedUser(disabledBucket, {
    id: "disabled-card-user",
    username: "disabled-card",
    email: "disabled-card@example.net",
  });
  disabledBucket.seedJson(`_account/user-state/id/${encodeURIComponent(disabledUser.id)}`, {
    user_id: disabledUser.id,
    email: disabledUser.email,
    disabled: true,
    account_status: "disabled",
    updated_at: new Date().toISOString(),
  });
  disabledBucket.seedBytes(CONTACT_CARD_KEY, [255, 216, 255, 217]);
  const disabledToken = await accountToken(disabledEnv.MASTER_KEY, disabledUser);
  const disabled = await getContactCard(disabledEnv, { token: disabledToken });
  assert.equal(disabled.status, 403);
  assert.equal(disabledBucket.getKeys.includes(CONTACT_CARD_KEY), false);
});

test("CONTACT_EMAIL is retained only for fixed server-side owner delivery", async () => {
  const source = await readFile(workerPath, "utf8");
  const uses = source.split("\n")
    .map((line, index) => ({ line: index + 1, text: line.trim() }))
    .filter((entry) => entry.text.includes("CONTACT_EMAIL"));
  assert.ok(uses.length >= 2);
  assert.match(uses[0].text, /^const CONTACT_EMAIL =/u);
  for (const use of uses.slice(1)) {
    assert.match(use.text, /^to: CONTACT_EMAIL,$/u, `public CONTACT_EMAIL use at line ${use.line}`);
  }
  assert.doesNotMatch(source, /contact:\s*CONTACT_EMAIL|联系邮箱\s*\$\{CONTACT_EMAIL\}|Contact:\s*\$\{CONTACT_EMAIL\}/u);
});
