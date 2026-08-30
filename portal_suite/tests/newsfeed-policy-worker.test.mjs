import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.version = 0;
  }

  seed(key, value) {
    this.version += 1;
    this.rows.set(key, {
      value: typeof value === "string" ? value : JSON.stringify(value),
      etag: `v${this.version}`,
    });
  }

  async get(key) {
    const row = this.rows.get(String(key));
    if (!row) return null;
    return {
      etag: row.etag,
      body: new TextEncoder().encode(row.value),
      size: new TextEncoder().encode(row.value).byteLength,
      async text() { return row.value; },
      async json() { return JSON.parse(row.value); },
    };
  }

  async put(key, value, options = {}) {
    const normalized = String(key);
    const current = this.rows.get(normalized);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && (!current || current.etag !== onlyIf.etagMatches)) return null;
    if (onlyIf.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const text = value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value);
    const row = { value: text, etag: `v${this.version}` };
    this.rows.set(normalized, row);
    return { etag: row.etag };
  }

  async delete(keyOrKeys) {
    for (const key of Array.isArray(keyOrKeys) ? keyOrKeys : [keyOrKeys]) this.rows.delete(String(key));
  }

  async list(options = {}) {
    const prefix = String(options.prefix || "");
    const limit = Math.max(1, Math.min(1000, Math.floor(Number(options.limit) || 1000)));
    const offset = Math.max(0, Math.floor(Number(options.cursor) || 0));
    const keys = [...this.rows.keys()].filter((key) => key.startsWith(prefix)).sort();
    const selected = keys.slice(offset, offset + limit);
    const next = offset + selected.length;
    return {
      objects: selected.map((key) => ({
        key,
        etag: this.rows.get(key).etag,
        size: new TextEncoder().encode(this.rows.get(key).value).byteLength,
      })),
      truncated: next < keys.length,
      cursor: next < keys.length ? String(next) : undefined,
    };
  }
}

function envFor(bucket, extra = {}) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY: "test-master-key",
    PASSWORD_SECRET: "test-password-secret",
    CATALOG_URL: "https://static.example.invalid/catalog.json",
    STATIC_DATA_PREFIX: "edge-static/runtime-data",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
    ...extra,
  };
}

function signedUserToken(user, secret = "test-password-secret") {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    session_epoch: String(user.session_epoch || ""),
    iat: now,
    exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", secret)
    .update(`portal:account-token:v1:${body}`)
    .digest("base64url");
  return `${body}.${signature}`;
}

function seedUser(bucket, overrides = {}) {
  const now = new Date().toISOString();
  const user = {
    id: "newsfeed-user-id",
    username: "newsfeed-reader",
    email: "newsfeed-reader@example.com",
    password_salt: "newsfeed-salt",
    password_hash: `hmac_sha256$${"a".repeat(64)}`,
    email_is_generated: false,
    site_origin: "portal",
    registered_site: "portal",
    source_site: "portal",
    session_epoch: "",
    created_at: now,
    updated_at: now,
    last_login_at: "",
    ...overrides,
  };
  for (const [field, value] of [["id", user.id], ["username", user.username], ["email", user.email]]) {
    bucket.seed(`_account/users/${field}/${encodeURIComponent(value)}`, user);
  }
  return { user, token: signedUserToken(user) };
}

function seedMemberAccess(bucket, user, months) {
  const now = new Date().toISOString();
  bucket.seed(`_account/access/${encodeURIComponent(user.email)}`, {
    id: `member-${months}`,
    email: user.email,
    access_mode: "all",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + Math.max(31, months * 31) * 24 * 60 * 60 * 1000).toISOString(),
    duration_value: String(months),
    download_limit: 0,
    download_count: 0,
    download_items: [],
    institutions: [],
    industries: [],
    page_ranges: [],
    note: "",
    change_id: `member-${months}-change`,
    created_at: now,
    updated_at: now,
  });
}

function seedCustomTopic(bucket, user, id) {
  bucket.seed(`_newsfeed/topics/${encodeURIComponent(user.email)}/${encodeURIComponent(id)}.json`, {
    id,
    kind: "custom",
    title: id,
    description: `Topic ${id}`,
    category: "Tech",
    output_language: "en",
    regions: ["global"],
    queries: [id],
    query_plan: {},
    created_from: id,
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  });
}

function bearer(token) {
  return { Authorization: `Bearer ${token}` };
}

async function jsonRequest(env, pathname, options = {}, context = { waitUntil() {} }) {
  const response = await worker.fetch(new Request(`https://worker.test${pathname}`, options), env, context);
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

function installFetchMock(t, controls = {}) {
  const original = globalThis.fetch;
  const state = {
    modelCalls: 0,
    emails: [],
    ...controls,
  };
  globalThis.fetch = async (input, init = {}) => {
    const url = String(input && input.url || input);
    if (url.includes("/chat/completions")) {
      state.modelCalls += 1;
      if (typeof state.onModelCall === "function") await state.onModelCall(state.modelCalls);
      return new Response(JSON.stringify({
        choices: [{
          message: {
            content: JSON.stringify({
              title: `Generated Topic ${state.modelCalls}`,
              description: "Generated topic package",
              category: "Tech",
              queries: ["generated topic news", "generated topic analysis"],
              query_plan: { source_mix: ["Google News RSS"], include_terms: ["generated"], exclude_terms: [] },
            }),
          },
        }],
      }), { status: 200, headers: { "content-type": "application/json" } });
    }
    if (url.includes("api.brevo.com/v3/smtp/email")) {
      const body = JSON.parse(String(init.body || "{}"));
      state.emails.push(body);
      return new Response(JSON.stringify({ messageId: `email-${state.emails.length}` }), {
        status: 201,
        headers: { "content-type": "application/json" },
      });
    }
    if (url.includes("gdeltproject.org")) {
      return new Response(JSON.stringify({ articles: [] }), { status: 200, headers: { "content-type": "application/json" } });
    }
    return new Response("<rss><channel></channel></rss>", { status: 200, headers: { "content-type": "application/rss+xml" } });
  };
  t.after(() => { globalThis.fetch = original; });
  return state;
}

async function createTopic(env, token, topic) {
  return jsonRequest(env, "/newsfeed/topics", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ topic, output_language: "en", preferred_regions: ["global"] }),
  });
}

test("anonymous and free users receive fixed general Newsfeed access without paid generation", async (t) => {
  const fetchState = installFetchMock(t);
  const bucket = new MemoryR2();
  const env = envFor(bucket, { DEEPSEEK_API_KEY: "deepseek-test" });

  const anonymous = await jsonRequest(env, "/newsfeed/home?fast=1&regions=china&language=zh-CN");
  assert.equal(anonymous.response.status, 200, JSON.stringify(anonymous.data));
  assert.equal(anonymous.data.policy.tier, "general");
  assert.equal(anonymous.data.policy.authenticated, false);
  assert.equal(anonymous.data.policy.can_customize, false);
  assert.equal(anonymous.data.policy.can_subscribe, false);
  assert.equal(anonymous.data.custom_topic_count, 0);
  assert.equal(anonymous.data.custom_topic_remaining, 0);
  assert.equal(anonymous.data.settings.interface_language, "en");
  assert.deepEqual(anonymous.data.settings.preferred_regions, ["global"]);
  assert.equal(anonymous.data.topics.length, 5);
  assert.ok(anonymous.data.topics.every((topic) => topic.kind === "system"));

  const invalidBearer = await jsonRequest(env, "/newsfeed/home?fast=1", {
    headers: { Authorization: "Bearer invalid-token" },
  });
  assert.equal(invalidBearer.response.status, 401);

  const missingCustom = await jsonRequest(env, "/newsfeed/topic?id=private-topic");
  assert.equal(missingCustom.response.status, 404);
  const briefing = await jsonRequest(env, "/newsfeed/briefing", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ digest: ["A general headline"], language: "en" }),
  });
  assert.equal(briefing.response.status, 200);
  assert.equal(briefing.data.policy.tier, "general");

  const { token } = seedUser(bucket);
  const freeHome = await jsonRequest(env, "/newsfeed/home?fast=1&regions=china&language=zh-CN", { headers: bearer(token) });
  assert.equal(freeHome.response.status, 200);
  assert.equal(freeHome.data.policy.tier, "general");
  assert.equal(freeHome.data.policy.authenticated, true);
  assert.deepEqual(freeHome.data.settings.preferred_regions, ["global"]);
  assert.equal(freeHome.data.settings.interface_language, "en");

  const deniedCreate = await createTopic(env, token, "Free account topic");
  assert.equal(deniedCreate.response.status, 403);
  assert.equal(deniedCreate.data.code, "NEWSFEED_MEMBERSHIP_REQUIRED");
  const deniedSettings = await jsonRequest(env, "/newsfeed/settings", { headers: bearer(token) });
  assert.equal(deniedSettings.response.status, 403);

  const article = await worker.fetch(new Request("https://worker.test/newsfeed/article", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ article: { title: "General story", source: "Source", summary: "Summary" } }),
  }), env, { waitUntil() {} });
  assert.equal(article.status, 200);
  assert.match(await article.text(), /"type":"done"/u);
  assert.equal(fetchState.modelCalls, 0, "general article fallback and denied custom topics must not call DeepSeek");
});

test("member topic limits are atomic, tiered, unlimited for super, and recover expired reservations", async (t) => {
  let enterModel;
  let releaseModel;
  const entered = new Promise((resolve) => { enterModel = resolve; });
  const gate = new Promise((resolve) => { releaseModel = resolve; });
  const fetchState = installFetchMock(t, {
    async onModelCall(call) {
      if (call === 1) {
        enterModel();
        await gate;
      }
    },
  });

  const bucket = new MemoryR2();
  const env = envFor(bucket, { DEEPSEEK_API_KEY: "deepseek-test" });
  const { user, token } = seedUser(bucket);
  seedMemberAccess(bucket, user, 1);
  seedCustomTopic(bucket, user, "existing-one");
  seedCustomTopic(bucket, user, "existing-two");

  const firstPromise = createTopic(env, token, "Atomic final slot A");
  await entered;
  const second = await createTopic(env, token, "Atomic final slot B");
  assert.equal(second.response.status, 409, JSON.stringify(second.data));
  assert.equal(second.data.code, "NEWSFEED_TOPIC_LIMIT");
  assert.equal(second.data.requested_topic, "Atomic final slot B");
  assert.equal(second.data.policy.custom_topic_count, 3);
  assert.equal(second.data.policy.custom_topic_remaining, 0);
  assert.equal(second.data.policy.request_allowed, true);
  releaseModel();
  const first = await firstPromise;
  assert.equal(first.response.status, 201, JSON.stringify(first.data));
  assert.equal(first.data.policy.tier, "member");
  assert.equal(first.data.policy.custom_topic_limit, 3);
  assert.equal(first.data.custom_topic_count, 3);
  assert.equal(first.data.custom_topic_remaining, 0);
  assert.equal(fetchState.modelCalls, 1, "the rejected concurrent request must not reach DeepSeek");

  const advancedBucket = new MemoryR2();
  const advancedEnv = envFor(advancedBucket, { DEEPSEEK_API_KEY: "deepseek-test" });
  const advancedAuth = seedUser(advancedBucket, { id: "advanced-id", username: "advanced", email: "advanced@example.com" });
  seedMemberAccess(advancedBucket, advancedAuth.user, 3);
  for (let index = 1; index <= 4; index += 1) seedCustomTopic(advancedBucket, advancedAuth.user, `advanced-${index}`);
  const advancedCreated = await createTopic(advancedEnv, advancedAuth.token, "Advanced fifth topic");
  assert.equal(advancedCreated.response.status, 201, JSON.stringify(advancedCreated.data));
  assert.equal(advancedCreated.data.policy.tier, "advanced");
  assert.equal(advancedCreated.data.policy.custom_topic_limit, 5);
  const advancedLimited = await createTopic(advancedEnv, advancedAuth.token, "Advanced sixth topic");
  assert.equal(advancedLimited.response.status, 409);
  assert.equal(advancedLimited.data.code, "NEWSFEED_TOPIC_LIMIT");

  const superBucket = new MemoryR2();
  const superEnv = envFor(superBucket, { DEEPSEEK_API_KEY: "deepseek-test" });
  const superAuth = seedUser(superBucket, {
    id: "admin-a-test-id",
    username: "admin-a",
    email: "admin-a@users.portal.example.invalid",
    email_is_generated: true,
  });
  for (let index = 1; index <= 5; index += 1) seedCustomTopic(superBucket, superAuth.user, `admin-${index}`);
  const superCreated = await createTopic(superEnv, superAuth.token, "Admin unlimited topic");
  assert.equal(superCreated.response.status, 201, JSON.stringify(superCreated.data));
  assert.equal(superCreated.data.policy.tier, "admin");
  assert.equal(superCreated.data.policy.custom_topic_limit, null);
  assert.equal(superCreated.data.custom_topic_remaining, null);

  const recoveryBucket = new MemoryR2();
  const recoveryEnv = envFor(recoveryBucket, { DEEPSEEK_API_KEY: "deepseek-test" });
  const recoveryAuth = seedUser(recoveryBucket, { id: "recovery-id", username: "recovery", email: "recovery@example.com" });
  seedMemberAccess(recoveryBucket, recoveryAuth.user, 1);
  seedCustomTopic(recoveryBucket, recoveryAuth.user, "recovery-one");
  seedCustomTopic(recoveryBucket, recoveryAuth.user, "recovery-two");
  recoveryBucket.seed(`_newsfeed/topic-ledger/v1/${encodeURIComponent(recoveryAuth.user.email)}.json`, {
    version: 1,
    user_key: encodeURIComponent(recoveryAuth.user.email),
    pending: [{ id: "a".repeat(32), created_at: "2020-01-01T00:00:00.000Z", expires_at_ms: Date.now() - 1 }],
    updated_at: "2020-01-01T00:00:00.000Z",
  });
  const recovered = await createTopic(recoveryEnv, recoveryAuth.token, "Recovered final slot");
  assert.equal(recovered.response.status, 201, JSON.stringify(recovered.data));
  assert.equal(recovered.data.custom_topic_count, 3, "an expired orphan reservation must not permanently consume capacity");
});

test("topic-limit requests are member-owned, deduplicated, private, and always email the fixed contact", async (t) => {
  const fetchState = installFetchMock(t);
  const bucket = new MemoryR2();
  const env = envFor(bucket, { BREVO_API_KEY: "brevo-test", NEWSFEED_EMAIL_PROVIDER: "brevo" });
  const { user, token } = seedUser(bucket);
  seedMemberAccess(bucket, user, 1);
  for (let index = 1; index <= 3; index += 1) seedCustomTopic(bucket, user, `member-${index}`);

  const submit = (body) => jsonRequest(env, "/newsfeed/topics/request", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      Origin: "https://portal.example.invalid",
      "CF-Connecting-IP": "203.0.113.90",
      ...bearer(token),
    },
    body: JSON.stringify(body),
  });
  const first = await submit({
    topic: "A fourth member topic",
    output_language: "zh-CN",
    preferred_regions: ["china", "mena"],
    page_path: "/newsfeed.html",
    recipient: "attacker@example.net",
  });
  assert.equal(first.response.status, 202, JSON.stringify(first.data));
  assert.equal(first.data.ok, true);
  assert.equal(first.data.policy.request_allowed, true);
  assert.equal(fetchState.emails.length, 1);
  assert.deepEqual(fetchState.emails[0].to, [{ email: ["info", "@", "kc", "desk", ".com"].join("") }]);
  assert.doesNotMatch(JSON.stringify(fetchState.emails[0]), /attacker@example\.net/u);
  const requestRows = [...bucket.rows.entries()].filter(([key]) => key.startsWith("_newsfeed/topic-requests/v1/items/"));
  assert.equal(requestRows.length, 1);
  const requestRecord = JSON.parse(requestRows[0][1].value);
  assert.equal(requestRecord.status, "sent");
  assert.equal(requestRecord.qualifying_months, 1);
  assert.equal(requestRecord.output_language, "zh-CN");
  assert.deepEqual(requestRecord.preferred_regions, ["china", "mena"]);
  assert.match(fetchState.emails[0].htmlContent, /zh-CN/u);
  assert.match(fetchState.emails[0].htmlContent, /china, mena/u);

  const duplicate = await submit({ topic: "A fourth member topic", page_path: "/newsfeed.html" });
  assert.equal(duplicate.response.status, 202);
  assert.equal(duplicate.data.deduplicated, true);
  assert.equal(fetchState.emails.length, 1);

  const honeypot = await jsonRequest(env, "/newsfeed/topics/request", {
    method: "POST",
    headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
    body: JSON.stringify({ topic: "Bot topic", website: "https://spam.invalid" }),
  });
  assert.equal(honeypot.response.status, 202);
  assert.equal(fetchState.emails.length, 1);

  const belowLimitBucket = new MemoryR2();
  const belowLimitEnv = envFor(belowLimitBucket);
  const belowAuth = seedUser(belowLimitBucket, { id: "below-id", username: "below", email: "below@example.com" });
  seedMemberAccess(belowLimitBucket, belowAuth.user, 1);
  seedCustomTopic(belowLimitBucket, belowAuth.user, "below-one");
  const tooEarly = await jsonRequest(belowLimitEnv, "/newsfeed/topics/request", {
    method: "POST",
    headers: { "content-type": "application/json", Origin: "https://portal.example.invalid", ...bearer(belowAuth.token) },
    body: JSON.stringify({ topic: "Not at limit" }),
  });
  assert.equal(tooEarly.response.status, 409);
  assert.equal(tooEarly.data.code, "NEWSFEED_REQUEST_NOT_AT_LIMIT");
});

test("scheduled digest delivery revalidates active membership", async (t) => {
  const fetchState = installFetchMock(t);
  const now = new Date();
  const sendTime = `${String(now.getUTCHours()).padStart(2, "0")}:${String(now.getUTCMinutes()).padStart(2, "0")}`;

  const seedDueSettings = (bucket, user) => bucket.seed(`_newsfeed/settings/${encodeURIComponent(user.email)}.json`, {
    pinned: ["global-daily"],
    user_key: encodeURIComponent(user.email),
    username: user.username,
    user_email: user.email,
    digest_email_enabled: true,
    digest_email: user.email,
    newsletter_topic_id: "global-daily",
    digest_send_time: sendTime,
    digest_timezone: "UTC",
    digest_language: "en",
    digest_last_sent_date: "",
    preferred_regions: ["global"],
    interface_language: "en",
  });

  const freeBucket = new MemoryR2();
  const freeEnv = envFor(freeBucket, { BREVO_API_KEY: "brevo-test", NEWSFEED_EMAIL_PROVIDER: "brevo" });
  const freeAuth = seedUser(freeBucket, { id: "expired-id", username: "expired", email: "expired@example.com" });
  seedDueSettings(freeBucket, freeAuth.user);
  const freeWaits = [];
  await worker.scheduled({ cron: "*/10 23 * * *" }, freeEnv, { waitUntil(promise) { freeWaits.push(promise); } });
  await Promise.all(freeWaits);
  assert.equal(fetchState.emails.length, 0, "a free/expired account's old setting must not continue sending");

  const memberBucket = new MemoryR2();
  const memberEnv = envFor(memberBucket, { BREVO_API_KEY: "brevo-test", NEWSFEED_EMAIL_PROVIDER: "brevo" });
  const memberAuth = seedUser(memberBucket, { id: "scheduled-id", username: "scheduled", email: "scheduled@example.com" });
  seedMemberAccess(memberBucket, memberAuth.user, 1);
  seedDueSettings(memberBucket, memberAuth.user);
  const memberWaits = [];
  await worker.scheduled({ cron: "*/10 23 * * *" }, memberEnv, { waitUntil(promise) { memberWaits.push(promise); } });
  await Promise.all(memberWaits);
  assert.equal(fetchState.emails.length, 1, "an active member remains eligible for scheduled delivery");
  assert.deepEqual(fetchState.emails[0].to, [{ email: memberAuth.user.email }]);
});

test("Newsfeed analytics HMACs page and interaction visitor ids in both mirrors", async (t) => {
  installFetchMock(t);
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const rawVisitor = "visitor-newsfeed-raw-0001";
  const submit = async (payload) => {
    const waits = [];
    const result = await jsonRequest(env, "/analytics", {
      method: "POST",
      headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
      body: JSON.stringify(payload),
    }, { waitUntil(promise) { waits.push(promise); } });
    await Promise.all(waits);
    return result;
  };
  const page = await submit({ type: "page_view", visitor_id: rawVisitor, path: "/newsfeed.html", data: { page: "newsfeed" } });
  assert.equal(page.response.status, 204);
  const interaction = await submit({
    type: "newsfeed_interaction",
    visitor_id: rawVisitor,
    path: "/newsfeed.html",
    data: {
      page: "newsfeed",
      action: "open_topic",
      access_state: "member",
      view: "topic",
      outcome: "success",
      topic_kind: "custom",
      topic_hash: "b".repeat(64),
      topic: "Private plaintext topic must not persist",
      item_count: 12,
      region_count: 2,
      tier: "member",
      count: 3,
      limit: 3,
    },
  });
  assert.equal(interaction.response.status, 204);

  const analyticsRows = [...bucket.rows.entries()].filter(([key]) => key.startsWith("_analytics"));
  assert.equal(analyticsRows.length, 4, "primary and backup copies are written for both events");
  assert.ok(analyticsRows.every(([, row]) => !row.value.includes(rawVisitor)));
  assert.ok(analyticsRows.every(([, row]) => !row.value.includes("Private plaintext topic must not persist")));
  const events = analyticsRows.map(([, row]) => JSON.parse(row.value));
  assert.ok(events.every((event) => /^[a-f0-9]{64}$/u.test(event.visitor_id)));
  assert.equal(new Set(events.map((event) => event.visitor_id)).size, 1, "the stable browser id maps to one stable Newsfeed HMAC");
  const storedInteraction = events.find((event) => event.type === "newsfeed_interaction");
  assert.equal(storedInteraction.access_state, "member");
  assert.equal(storedInteraction.view, "topic");
  assert.equal(storedInteraction.outcome, "success");
  assert.equal(storedInteraction.topic_kind, "custom");
  assert.equal(storedInteraction.topic_hash, "b".repeat(64));
  assert.equal(storedInteraction.item_count, 12);
  assert.equal(storedInteraction.region_count, 2);
  assert.equal(storedInteraction.tier, "member");
  assert.equal(storedInteraction.count, 3);
  assert.equal(storedInteraction.limit, 3);
});
