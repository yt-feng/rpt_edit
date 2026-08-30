import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));
const restrictedCourseMarkers = [
  ["W", "SP"],
  ["W", "SO"],
  ["股", "道场"],
  ["并", "购圈"],
  ["Fundamental", " Edge"],
  ["Wall Street", " Prep"],
  ["Wall Street", " Oasis"],
  ["Breaking", " into VC"],
  ["Breaking", "_into_VC"],
  ["Breaking Into", " Wallstreet"],
  ["BI", "WS"],
  ["梧桐", "课堂"],
  ["职", "未来"],
  ["和", "君"],
  ["青年", "金融家"],
  ["i", "banker"],
  ["优", "塾"],
  ["万法", "通"],
  ["法", "询"],
  ["基小", "律"],
  ["林立", "军"],
  ["肖", "星"],
  ["清", "华"],
  ["Wi", "nd"],
  ["Bloom", "berg"],
  ["罗兰", "贝格"],
  ["埃森", "哲"],
  ["MS", " Training"],
  ["101", " primer"],
].map((parts) => parts.join(""));

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.version = 0;
    this.jsonReadKeys = [];
    this.textReadKeys = [];
    this.rangeReadKeys = [];
    this.getKeys = [];
    this.putKeys = [];
    this.deleteKeys = [];
    this.textOnlyKeys = new Set();
    this.failPutPrefixOnce = "";
    this.failGetAfterPutExact = "";
    this.failNextGetExact = "";
  }

  seed(key, value) {
    this.version += 1;
    this.rows.set(key, { value: typeof value === "string" ? value : JSON.stringify(value), etag: `v${this.version}` });
  }

  seedBytes(key, value) {
    this.version += 1;
    this.rows.set(key, { value: new Uint8Array(value), etag: `v${this.version}`, binary: true });
  }

  async get(key, options = {}) {
    this.getKeys.push(key);
    if (this.failNextGetExact && key === this.failNextGetExact) {
      this.failNextGetExact = "";
      throw new Error("injected R2 read failure");
    }
    const row = this.rows.get(key);
    if (!row) return null;
    const range = options && options.range;
  const rangedValue = range && Number.isInteger(range.offset) && Number.isInteger(range.length)
      ? (row.binary ? row.value : new TextEncoder().encode(row.value)).slice(range.offset, range.offset + range.length)
      : null;
    if (range) this.rangeReadKeys.push(key);
    if (range && (!Number.isInteger(range.offset) || !Number.isInteger(range.length)
      || range.offset < 0 || range.length < 0
      || rangedValue.byteLength !== range.length)) return null;
    if (row.binary) {
      const value = rangedValue || row.value;
      return {
        etag: row.etag,
        body: value,
        size: value.byteLength,
        async arrayBuffer() { return value.buffer.slice(value.byteOffset, value.byteOffset + value.byteLength); },
        async text() { return new TextDecoder().decode(value); },
      };
    }
    const bucket = this;
    const object = {
      etag: row.etag,
      body: new TextEncoder().encode(row.value),
      size: new TextEncoder().encode(row.value).byteLength,
      async text() {
        bucket.textReadKeys.push(key);
        return row.value;
      },
    };
    if (!this.textOnlyKeys.has(key)) {
      object.json = async () => {
        bucket.jsonReadKeys.push(key);
        return JSON.parse(row.value);
      };
    }
    return object;
  }

  async head(key) {
    const row = this.rows.get(key);
    if (!row) return null;
    const value = row.binary ? row.value : new TextEncoder().encode(row.value);
    return {
      etag: row.etag,
      size: value.byteLength,
      httpMetadata: row.httpMetadata || {},
    };
  }

  async put(key, value, options = {}) {
    this.putKeys.push(key);
    if (this.failPutPrefixOnce && key.startsWith(this.failPutPrefixOnce)) {
      this.failPutPrefixOnce = "";
      throw new Error("injected R2 write failure");
    }
    const current = this.rows.get(key);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && (!current || current.etag !== onlyIf.etagMatches)) return null;
    if (onlyIf.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const text = value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value);
    const row = { value: text, etag: `v${this.version}` };
    this.rows.set(key, row);
    if (this.failGetAfterPutExact && key === this.failGetAfterPutExact) {
      this.failNextGetExact = key;
      this.failGetAfterPutExact = "";
    }
    return { etag: row.etag };
  }

  async delete(keyOrKeys) {
    const keys = Array.isArray(keyOrKeys) ? keyOrKeys : [keyOrKeys];
    for (const key of keys) {
      this.deleteKeys.push(String(key));
      this.rows.delete(String(key));
    }
  }

  async list(options = {}) {
    const prefix = String(options.prefix || "");
    const limit = Math.max(1, Math.min(1000, Math.floor(Number(options.limit) || 1000)));
    const offset = Math.max(0, Math.floor(Number(options.cursor) || 0));
    const keys = [...this.rows.keys()].filter((key) => key.startsWith(prefix)).sort();
    const selected = keys.slice(offset, offset + limit);
    const nextOffset = offset + selected.length;
    return {
      objects: selected.map((key) => {
        const row = this.rows.get(key);
        const size = row.binary ? row.value.byteLength : new TextEncoder().encode(row.value).byteLength;
        return { key, size, etag: row.etag };
      }),
      truncated: nextOffset < keys.length,
      cursor: nextOffset < keys.length ? String(nextOffset) : undefined,
    };
  }
}

async function directLookupFixture(items, tokenPostings, options = {}) {
  const bucketCount = options.bucketCount || 64;
  const prefix = options.prefix || "_report-chat/v2/releases/test";
  const buildPart = async (entries, name) => {
    const buckets = Array.from({ length: bucketCount }, () => []);
    for (const [key, value] of entries) {
      const digest = new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(key)));
      const bucket = Number(new DataView(digest.buffer).getBigUint64(0, false) % BigInt(bucketCount));
      buckets[bucket].push([key, value]);
    }
    const table = new Uint8Array(bucketCount * 12);
    const chunks = [];
    let offset = 0;
    for (let bucket = 0; bucket < bucketCount; bucket += 1) {
      const entriesInBucket = buckets[bucket].sort((left, right) => left[0].localeCompare(right[0]));
      if (!entriesInBucket.length) continue;
      const bytes = new TextEncoder().encode(JSON.stringify(entriesInBucket));
      const view = new DataView(table.buffer, bucket * 12, 12);
      view.setBigUint64(0, BigInt(offset), false);
      view.setUint32(8, bytes.byteLength, false);
      chunks.push(bytes);
      offset += bytes.byteLength;
    }
    const data = new Uint8Array(offset);
    let cursor = 0;
    for (const chunk of chunks) {
      data.set(chunk, cursor);
      cursor += chunk.byteLength;
    }
    return {
      table,
      data,
      manifest: {
        table_key: `${prefix}/${name}.tbl`,
        data_key: `${prefix}/${name}.dat`,
        bucket_count: bucketCount,
        slot_size: 12,
        data_bytes: data.byteLength,
      },
    };
  };
  const tokenPart = await buildPart(Object.entries(tokenPostings), "tokens");
  const itemPart = await buildPart(items.map((item) => [item.id, item]), "items");
  const evidencePart = Array.isArray(options.evidenceEntries)
    ? await buildPart(options.evidenceEntries, "evidence")
    : null;
  return { tokenPart, itemPart, evidencePart };
}

async function seedReportChatLookup(bucket, items, tokenPostings, defaults = items.slice(0, 12)) {
  const { tokenPart, itemPart } = await directLookupFixture(items, tokenPostings);
  bucket.seedBytes(tokenPart.manifest.table_key, tokenPart.table);
  bucket.seedBytes(tokenPart.manifest.data_key, tokenPart.data);
  bucket.seedBytes(itemPart.manifest.table_key, itemPart.table);
  bucket.seedBytes(itemPart.manifest.data_key, itemPart.data);
  bucket.seed("_report-chat/v2/manifest.json", {
    schema_version: 2,
    index_kind: "report-chat-random-access",
    hash: "sha256-first8-be",
    token_table: tokenPart.manifest,
    item_table: itemPart.manifest,
    default_items: defaults,
  });
}

async function seedCourseChatLookup(bucket, items, tokenPostings, defaults = items.slice(0, 12)) {
  const prefix = "_course-directory/v2/chat-lookup/test";
  const { tokenPart, itemPart } = await directLookupFixture(items, tokenPostings, { prefix });
  bucket.seedBytes(tokenPart.manifest.table_key, tokenPart.table);
  bucket.seedBytes(tokenPart.manifest.data_key, tokenPart.data);
  bucket.seedBytes(itemPart.manifest.table_key, itemPart.table);
  bucket.seedBytes(itemPart.manifest.data_key, itemPart.data);
  bucket.seed("_course-directory/v2/chat-lookup/manifest.json", {
    schema_version: 2,
    format: "course-chat-direct-bucket-v2",
    token_index: { ...tokenPart.manifest, hash: "sha256-first64-be-mod" },
    item_index: { ...itemPart.manifest, hash: "sha256-first64-be-mod" },
    default_items: defaults,
  });
}

async function seedReportResearchLookup(bucket, items, tokenPostings, evidenceEntries) {
  const prefix = "_report-research/v1/releases/test";
  const { tokenPart, itemPart, evidencePart } = await directLookupFixture(items, tokenPostings, {
    prefix,
    evidenceEntries,
  });
  bucket.seedBytes(tokenPart.manifest.table_key, tokenPart.table);
  bucket.seedBytes(tokenPart.manifest.data_key, tokenPart.data);
  bucket.seedBytes(itemPart.manifest.table_key, itemPart.table);
  bucket.seedBytes(itemPart.manifest.data_key, itemPart.data);
  bucket.seedBytes(evidencePart.manifest.table_key, evidencePart.table);
  bucket.seedBytes(evidencePart.manifest.data_key, evidencePart.data);
  bucket.seed("_report-research/v1/manifest.json", {
    schema_version: 1,
    index_kind: "report-research-random-access",
    hash: "sha256-first8-be",
    token_table: tokenPart.manifest,
    item_table: itemPart.manifest,
    // The Worker must bound each range bucket, not reject a growing aggregate
    // evidence object once it crosses the legacy 128 MiB chat-index limit.
    evidence_table: { ...evidencePart.manifest, data_bytes: 256 * 1024 * 1024 },
  });
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY: "test-master-key",
    PASSWORD_SECRET: "test-password-secret",
    CATALOG_URL: "https://static.example.invalid/catalog.json",
    STATIC_DATA_PREFIX: "edge-static/runtime-data",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
    COURSE_DIRECTORY_REDACT_TERMS: restrictedCourseMarkers.join("\n"),
  };
}

async function jsonRequest(env, pathName, options = {}, context = { waitUntil() {} }) {
  const response = await worker.fetch(new Request(`https://worker.test${pathName}`, options), env, context);
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

async function register(env) {
  const captcha = await jsonRequest(env, "/captcha");
  assert.equal(captcha.response.status, 200);
  const svg = Buffer.from(String(captcha.data.image).split(",", 2)[1], "base64").toString("utf8");
  const equation = svg.match(/>(\d+) \+ (\d+) = \?</u);
  assert.ok(equation, "captcha equation must be readable in the fixture");
  const answer = String(Number(equation[1]) + Number(equation[2]));
  const auth = await jsonRequest(env, "/auth", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      action: "register",
      username: "reward-reader",
      email: "reward-reader@example.com",
      password: "test-pass-123",
      captcha_token: captcha.data.token,
      captcha_answer: answer,
    }),
  });
  assert.equal(auth.response.status, 201);
  assert.ok(auth.data.token);
  return auth.data.token;
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

function seedSuperAccount(bucket) {
  const now = new Date().toISOString();
  const user = {
    id: "admin-a-test-id",
    username: "admin-a",
    email: "admin-a@users.portal.example.invalid",
    password_salt: "admin-a-test-salt",
    password_hash: `hmac_sha256$${"a".repeat(64)}`,
    email_is_generated: true,
    site_origin: "portal",
    registered_site: "portal",
    source_site: "portal",
    session_epoch: "",
    created_at: now,
    updated_at: now,
    last_login_at: "",
  };
  for (const [field, value] of [["id", user.id], ["username", user.username], ["email", user.email]]) {
    bucket.seed(`_account/users/${field}/${encodeURIComponent(value)}`, user);
  }
  return { user, token: signedUserToken(user) };
}

function bearer(token) {
  return { Authorization: `Bearer ${token}` };
}

function bjtDateOffset(days = 0) {
  return new Date(Date.now() + 8 * 60 * 60 * 1000 + days * 24 * 60 * 60 * 1000).toISOString().slice(0, 10);
}

function rewardStateKey() {
  return `_account/rewards/${encodeURIComponent("reward-reader@example.com")}`;
}

function rewriteRegisteredUser(bucket, fields) {
  for (const [key, row] of [...bucket.rows.entries()]) {
    if (!key.startsWith("_account/users/") || row.binary) continue;
    const value = JSON.parse(row.value);
    if (value.email === "reward-reader@example.com") bucket.seed(key, { ...value, ...fields });
  }
}

function v2RewardState(overrides = {}) {
  return {
    schema_version: 2,
    policy_version: 2,
    email: "reward-reader@example.com",
    points: 0,
    current_streak: 0,
    longest_streak: 0,
    last_checkin_date: "",
    checkins: {},
    claims: {},
    grants: {},
    credits: [],
    welcome_credit_issued: true,
    first_d3_credit_issued: false,
    first_d7_freeze_issued: false,
    freeze_cards: 0,
    policy_migrated_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
    ...overrides,
  };
}

test("D1 check-in is idempotent, issues one 72-hour welcome credit, and grants exactly one catalog report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);

  const initial = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(initial.response.status, 200);
  assert.equal(initial.data.points, 0);
  assert.equal(initial.data.checked_in_today, false);
  assert.equal(initial.data.credits_available, 0);
  assert.equal(initial.data.next_milestone.type, "welcome_credit");

  const checkinWaits = [];
  const rewardReadsBefore = bucket.getKeys.filter((key) => key === rewardStateKey()).length;
  const checkedIn = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  }, {
    waitUntil(promise) { checkinWaits.push(promise); },
  });
  assert.equal(checkedIn.response.status, 200);
  assert.equal(checkedIn.data.points, 10);
  assert.equal(checkedIn.data.current_streak, 1);
  assert.equal(checkedIn.data.daily_available, true);
  assert.equal(checkedIn.data.credits_available, 1);
  assert.equal(checkedIn.data.credits[0].reason, "welcome_d1");
  assert.ok(Date.parse(checkedIn.data.credits[0].expires_at) - Date.now() > 71 * 60 * 60 * 1000);
  assert.ok(Date.parse(checkedIn.data.credits[0].expires_at) - Date.now() <= 72 * 60 * 60 * 1000);
  assert.equal(checkedIn.data.next_credit_expiry, checkedIn.data.credits[0].expires_at);
  assert.equal(checkedIn.data.next_milestone.type, "d3_credit");
  assert.equal(checkedIn.data.next_milestone.days, 2);
  assert.equal(checkinWaits.length, 1, "analytics must be deferred with waitUntil");
  await Promise.all(checkinWaits);
  assert.equal(
    bucket.getKeys.filter((key) => key === rewardStateKey()).length - rewardReadsBefore,
    1,
    "a successful check-in must build its status without a second reward-state read",
  );

  const duplicateCheckin = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(duplicateCheckin.response.status, 200);
  assert.equal(duplicateCheckin.data.points, 10, "duplicate check-ins must not add points");
  assert.equal(duplicateCheckin.data.credits_available, 1, "duplicate check-ins must not issue another welcome credit");

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);
  assert.equal(claimed.data.rewards.daily_claimed, true);
  assert.equal(claimed.data.rewards.credits_available, 0);
  assert.equal(claimed.data.rewards.next_credit_expiry, "");

  const accessA = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessA.response.status, 200);
  assert.equal(accessA.data.can_download, true, "the reward must use the existing purchase entitlement path");

  const secondDaily = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(secondDaily.response.status, 200);
  assert.equal(secondDaily.data.claimed, false);
  assert.equal(secondDaily.data.already_claimed_today, true);

  const accessB = await jsonRequest(env, `/entitlement?report_id=${reportB}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessB.response.status, 200);
  assert.equal(accessB.data.can_download, false);

  const insufficient = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "points", report_id: reportB }),
  });
  assert.equal(insufficient.response.status, 409);
  assert.match(insufficient.data.detail, /积分不足/u);
});

test("concurrent D1 check-ins issue one welcome credit and one points award", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  const requests = [1, 2].map(() => jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  }));
  const responses = await Promise.all(requests);
  assert.ok(responses.every(({ response }) => response.status === 200));
  assert.ok(responses.every(({ data }) => data.points === 10));
  assert.ok(responses.every(({ data }) => data.current_streak === 1));
  assert.ok(responses.every(({ data }) => data.credits_available === 1));
  const stored = JSON.parse(bucket.rows.get(rewardStateKey()).value);
  assert.equal(stored.points, 10);
  assert.equal(Object.keys(stored.checkins).length, 1);
  assert.deepEqual(stored.credits.map((credit) => credit.id), ["welcome-v2"]);
});

test("D3 issues one 72-hour credit, D7 records a freeze, and the existing D30 points bonus remains", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  const dayBefore = bjtDateOffset(-2);
  const yesterday = bjtDateOffset(-1);
  bucket.seed(rewardStateKey(), v2RewardState({
    points: 20,
    current_streak: 2,
    longest_streak: 2,
    last_checkin_date: yesterday,
    checkins: {
      [dayBefore]: { base_points: 10, bonus_points: 0, streak_after: 1 },
      [yesterday]: { base_points: 10, bonus_points: 0, streak_after: 2 },
    },
  }));

  const d3 = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(d3.response.status, 200);
  assert.equal(d3.data.current_streak, 3);
  assert.equal(d3.data.points, 35, "D3 keeps the existing +5 milestone bonus");
  assert.equal(d3.data.credits_available, 1);
  assert.equal(d3.data.credits[0].reason, "streak_d3");
  assert.ok(Date.parse(d3.data.credits[0].expires_at) - Date.now() > 71 * 60 * 60 * 1000);
  assert.equal(d3.data.next_milestone.type, "d7_freeze");
  assert.equal(d3.data.next_milestone.days, 4);

  bucket.seed(rewardStateKey(), v2RewardState({
    points: 70,
    current_streak: 6,
    longest_streak: 6,
    last_checkin_date: yesterday,
    checkins: {
      [yesterday]: { base_points: 10, bonus_points: 5, streak_after: 6 },
    },
    first_d3_credit_issued: true,
  }));
  const d7 = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(d7.response.status, 200);
  assert.equal(d7.data.current_streak, 7);
  assert.equal(d7.data.points, 100, "D7 keeps the existing +20 milestone bonus");
  assert.equal(d7.data.freeze_cards, 1);
  assert.equal(d7.data.credits_available, 0, "ordinary post-onboarding check-ins do not issue a daily report");
  assert.equal(d7.data.daily_available, false);
  assert.equal(d7.data.next_milestone.type, "bonus_points");

  bucket.seed(rewardStateKey(), v2RewardState({
    points: 300,
    current_streak: 29,
    longest_streak: 29,
    last_checkin_date: yesterday,
    checkins: {
      [yesterday]: { base_points: 10, bonus_points: 0, streak_after: 29 },
    },
    first_d3_credit_issued: true,
    first_d7_freeze_issued: true,
    freeze_cards: 1,
  }));
  const d30 = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(d30.response.status, 200);
  assert.equal(d30.data.current_streak, 30);
  assert.equal(d30.data.points, 410, "D30 keeps the existing +100 milestone bonus");
  assert.equal(d30.data.credits_available, 0);
});

test("daily claims ignore expired credits and consume the earliest valid credit", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Credit order report", filename: "credit.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  const now = Date.now();
  bucket.seed(rewardStateKey(), v2RewardState({
    first_d3_credit_issued: true,
    credits: [
      { id: "expired", reason: "test", issued_at: new Date(now - 3_600_000).toISOString(), expires_at: new Date(now - 1_000).toISOString() },
      { id: "later", reason: "test", issued_at: new Date(now - 1_000).toISOString(), expires_at: new Date(now + 7_200_000).toISOString() },
      { id: "earlier", reason: "test", issued_at: new Date(now - 2_000).toISOString(), expires_at: new Date(now + 3_600_000).toISOString() },
    ],
  }));

  const before = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(before.data.credits_available, 2);
  assert.equal(before.data.credits[0].id, "earlier");
  assert.equal(before.data.next_credit_expiry, before.data.credits[0].expires_at);
  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);
  assert.equal(claimed.data.rewards.credits_available, 1);
  assert.equal(claimed.data.rewards.credits[0].id, "later");
  const stored = JSON.parse(bucket.rows.get(rewardStateKey()).value);
  assert.equal(stored.credits.find((credit) => credit.id === "earlier").report_id, reportId);
  assert.ok(stored.credits.find((credit) => credit.id === "earlier").claimed_at);
  assert.equal(stored.credits.find((credit) => credit.id === "later").claimed_at, "");
  assert.equal(stored.claims[bjtDateOffset(0)].daily.credit_id, "earlier");
});

test("an expired credit cannot authorize a daily claim", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Expired report", filename: "expired.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  const now = Date.now();
  bucket.seed(rewardStateKey(), v2RewardState({
    credits: [{ id: "expired", reason: "test", issued_at: new Date(now - 7_200_000).toISOString(), expires_at: new Date(now - 1_000).toISOString() }],
  }));
  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  });
  assert.equal(claimed.response.status, 409);
  assert.match(claimed.data.detail, /没有可用报告券/u);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, false);
});

test("legacy reward state migrates lazily without changing balances, streaks, or grants and keeps cutover-day entitlement", async () => {
  const bucket = new MemoryR2();
  const oldGrant = "cccccccccccccccccccccccc";
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  const today = bjtDateOffset(0);
  env.REWARD_POLICY_V2_CUTOVER_AT = `${today}T00:00:00+08:00`;
  rewriteRegisteredUser(bucket, { created_at: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString() });
  bucket.seed(rewardStateKey(), {
    email: "reward-reader@example.com",
    points: 55,
    current_streak: 8,
    longest_streak: 10,
    last_checkin_date: today,
    checkins: { [today]: { base_points: 10, bonus_points: 0, streak_after: 8 } },
    claims: {},
    grants: {
      [oldGrant]: { report_id: oldGrant, report_title: "Previously granted", reward_kind: "daily", granted_at: new Date().toISOString() },
    },
    updated_at: new Date().toISOString(),
  });

  const [status, concurrentStatus] = await Promise.all([
    jsonRequest(env, "/rewards", { headers: bearer(token) }),
    jsonRequest(env, "/rewards", { headers: bearer(token) }),
  ]);
  assert.equal(status.response.status, 200);
  assert.equal(concurrentStatus.response.status, 200);
  assert.equal(status.data.policy_version, 2);
  assert.equal(status.data.points, 55);
  assert.equal(status.data.current_streak, 8);
  assert.equal(status.data.longest_streak, 10);
  assert.equal(status.data.freeze_cards, 1);
  assert.equal(status.data.credits_available, 1);
  assert.equal(status.data.credits[0].reason, "legacy_cutover");
  assert.equal(status.data.credits[0].expires_at, new Date(Date.parse(`${today}T00:00:00+08:00`) + 24 * 60 * 60 * 1000).toISOString());
  const stored = JSON.parse(bucket.rows.get(rewardStateKey()).value);
  assert.equal(stored.policy_version, 2);
  assert.equal(stored.welcome_credit_issued, true, "an old account must not receive a D1 welcome credit");
  assert.equal(stored.first_d3_credit_issued, true);
  assert.equal(stored.first_d7_freeze_issued, true);
  assert.equal(stored.points, 55);
  assert.equal(stored.current_streak, 8);
  assert.deepEqual(stored.grants[oldGrant].report_id, oldGrant);
  assert.equal(stored.credits.some((credit) => credit.reason === "welcome_d1"), false);
  assert.equal(stored.credits.filter((credit) => credit.reason === "legacy_cutover").length, 1);
});

test("an old account without a legacy same-day slot does not receive a D1 welcome credit", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  env.REWARD_POLICY_V2_CUTOVER_AT = `${bjtDateOffset(0)}T00:00:00+08:00`;
  rewriteRegisteredUser(bucket, { created_at: new Date(Date.now() - 30 * 24 * 60 * 60 * 1000).toISOString() });
  const checkedIn = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(checkedIn.response.status, 200);
  assert.equal(checkedIn.data.points, 10);
  assert.equal(checkedIn.data.credits_available, 0);
  assert.equal(checkedIn.data.daily_available, false);
  const stored = JSON.parse(bucket.rows.get(rewardStateKey()).value);
  assert.equal(stored.welcome_credit_issued, true);
  assert.deepEqual(stored.credits, []);
});

test("failed purchase mirroring still grants exactly one report from reward state", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report C", filename: "c.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_available, false);
  assert.equal(status.data.daily_claimed, true);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true, "the atomic reward grant is authoritative when the mirror is unavailable");
});

test("concurrent daily claims grant at most one report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report D", filename: "d.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report E", filename: "e.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  const [left, right] = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  })));
  assert.deepEqual([left, right].map(({ data }) => Boolean(data.claimed)).sort(), [false, true]);
  const access = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(
    env,
    `/entitlement?report_id=${reportId}&source=catalog`,
    { headers: bearer(token) },
  )));
  assert.equal(access.filter(({ data }) => data.can_download).length, 1);
});

test("daily and points claims for the same report consume only one reward", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "One report", filename: "one.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  const now = Date.now();
  bucket.seed(rewardStateKey(), v2RewardState({
    points: 70,
    first_d3_credit_issued: true,
    credits: [{ id: "credit", reason: "test", issued_at: new Date(now - 1_000).toISOString(), expires_at: new Date(now + 3_600_000).toISOString() }],
  }));
  const contexts = [[], []];
  const requests = ["daily", "points"].map((kind, index) => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: kind, report_id: reportId }),
  }, { waitUntil(promise) { contexts[index].push(promise); } }));
  const results = await Promise.all(requests);
  assert.ok(results.every(({ response }) => response.status === 200));
  assert.equal(results.filter(({ data }) => data.claimed).length, 1);
  assert.equal(results.filter(({ data }) => data.already_owned).length, 1);
  const state = JSON.parse(bucket.rows.get(rewardStateKey()).value);
  const creditWasSpent = Boolean(state.credits.find((credit) => credit.id === "credit").claimed_at);
  const pointsWereSpent = state.points === 0;
  assert.notEqual(creditWasSpent, pointsWereSpent, "only the winning reward kind may be consumed");
  assert.equal(Object.keys(state.grants).length, 1);
  await Promise.all(contexts.flat());
});

test("reward status resets a stale streak before the next check-in", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  const staleDate = bjtDateOffset(-2);
  bucket.seed(rewardStateKey(), v2RewardState({
    points: 50,
    current_streak: 5,
    longest_streak: 5,
    last_checkin_date: staleDate,
    checkins: { [staleDate]: { base_points: 10, bonus_points: 0, streak_after: 5 } },
    first_d3_credit_issued: true,
  }));
  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.response.status, 200);
  assert.equal(status.data.current_streak, 0);
  assert.equal(status.data.longest_streak, 5);
  assert.equal(status.data.next_milestone.type, "d7_freeze");
  assert.equal(status.data.next_milestone.days, 7);
  const checkedIn = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(checkedIn.data.current_streak, 1);
});

test("a committed reward never depends on a purchase readback", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failGetAfterPutExact = `_account/purchases/catalog/${reportA}/${encodeURIComponent("reward-reader@example.com")}`;

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const duplicate = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(duplicate.response.status, 200);
  assert.equal(duplicate.data.claimed, false);
  assert.equal(duplicate.data.already_claimed_today, true);

  const access = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.response.status, 200);
  assert.equal(access.data.can_download, true);
  assert.equal(access.data.reward_access_matched, true);
  assert.ok(bucket.failNextGetExact, "purchase readback should remain untouched because reward state authorizes directly");
});

test("same-report retry cannot restore a consumed daily slot when purchase mirroring fails", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";
  const requests = [1, 2].map(() => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  }));
  const results = await Promise.all(requests);
  assert.ok(results.every(({ response }) => response.status === 200));
  assert.equal(results.filter(({ data }) => data.claimed).length, 1);
  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_claimed, true);
  assert.equal(status.data.daily_available, false);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true);
});

test("course API enforces at least 30 remaining days on the server", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);

  const anonymous = await jsonRequest(env, "/course/access");
  assert.equal(anonymous.response.status, 401);
  assert.equal(Object.hasOwn(anonymous.data, "courses"), false);
  assert.equal(Object.hasOwn(anonymous.data, "course_catalog"), false);

  const token = await register(env);
  const email = "reward-reader@example.com";
  const entitlementKey = `_account/entitlements/${encodeURIComponent(email)}`;

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const allowed = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(allowed.response.status, 200);
  assert.equal(allowed.data.can_access, true);
  assert.equal(allowed.data.courses.length, 44);
  assert.equal(allowed.data.course_catalog.length, 44);
  assert.deepEqual(
    allowed.data.courses,
    allowed.data.course_catalog.map((course) => course.title),
    "the legacy title array must stay compatible with the structured catalog",
  );
  assert.equal(new Set(allowed.data.course_catalog.map((course) => course.id)).size, 44);
  assert.deepEqual(
    allowed.data.course_catalog.find((course) => course.id === "str-01"),
    {
      id: "str-01",
      category: "战略咨询",
      title: "麦府学堂｜战略与商业分析方法论",
      summary: "覆盖问题拆解、行业与竞争分析、市场研究、增长战略、创新、组织设计与项目表达。",
      audience: "战略、投资、咨询、企业发展与经营分析人员",
    },
  );
  for (const course of allowed.data.course_catalog) {
    assert.deepEqual(Object.keys(course).sort(), ["audience", "category", "id", "summary", "title"]);
    for (const field of ["id", "category", "title", "summary", "audience"]) {
      assert.equal(typeof course[field], "string");
      assert.ok(course[field].trim(), `${field} must be populated`);
    }
  }
  const serializedCatalog = JSON.stringify(allowed.data.course_catalog).toLowerCase();
  for (const marker of restrictedCourseMarkers) {
    assert.equal(serializedCatalog.includes(marker.toLowerCase()), false, `restricted marker leaked: ${marker}`);
  }

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 29 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const denied = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(denied.response.status, 200);
  assert.equal(denied.data.can_access, false);
  assert.deepEqual(denied.data.courses, []);
  assert.deepEqual(denied.data.course_catalog, []);

  bucket.rows.delete(entitlementKey);
  const accessKey = `_account/access/${encodeURIComponent(email)}`;
  const accessBase = {
    id: "access-1",
    email,
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    duration_value: "1",
    institutions: [],
    industries: [],
    page_ranges: [],
    download_items: [],
    download_limit: 0,
    download_count: 0,
    note: "",
    source: "stored",
  };
  bucket.seed(accessKey, { ...accessBase, access_mode: "filters", institutions: ["NOM"] });
  const filtered = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(filtered.data.can_access, false, "a filtered report grant is not a membership");
  assert.deepEqual(filtered.data.courses, []);
  assert.deepEqual(filtered.data.course_catalog, []);

  bucket.seed(accessKey, {
    ...accessBase,
    access_mode: "all",
    duration_value: "trial_3d",
    download_limit: 10,
  });
  const limited = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(limited.data.can_access, false, "a limited report grant is not a membership");
  assert.deepEqual(limited.data.courses, []);
  assert.deepEqual(limited.data.course_catalog, []);
});

test("course directory stays private, searchable, paginated, and strips storage locators", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const hiddenMarker = restrictedCourseMarkers[0];
  bucket.seed("_course-directory/v1/directory.json", {
    schema_version: 1,
    generated_at: "2026-08-10T12:00:00+08:00",
    items: [
      {
        id: "file-00000001",
        course_id: "cap-03",
        name: "中国证监会 IPO 审核规则与案例",
        folders: ["IPO 上市实务", "监管审核"],
        extension: "pdf",
        size_label: "12.4 MB",
        date: "2026-08-10",
        entities: ["中国证监会", "上交所", "深交所"],
        source_path: "must/not/leave/private/storage",
        object_key: "private-object-key",
        locator: "private-locator",
      },
      {
        id: "file-00000002",
        course_id: "res-02",
        name: "摩根大通全球利率与外汇策略",
        folders: ["全球宏观", "利率与外汇"],
        extension: "pdf",
        size_label: "8.1 MB",
        date: "2026-08-09",
        entities: ["摩根大通", "高盛", "美银", "瑞银"],
      },
      {
        id: "file-00000003",
        course_id: "law-01",
        name: "资本市场尽职调查工作底稿",
        folders: ["非诉项目", "尽职调查"],
        extension: "docx",
        size_label: "980 KB",
        date: "2026-08-08",
        entities: ["金杜", "中伦", "君合", "国浩"],
      },
      {
        id: "file-00000004",
        course_id: "fin-01",
        name: `${hiddenMarker} provider material`,
        folders: ["估值"],
        extension: "xlsx",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000005",
        course_id: "fin-01",
        name: "课程咨询 private.user@example.com",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000006",
        course_id: "fin-01",
        name: "估值案例",
        folders: ["资料 private.example.com"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000007",
        course_id: "fin-01",
        name: "估值案例讲解",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: ["微信 abc123", "13800138000"],
      },
      {
        id: "file-00000008",
        course_id: "fin-01",
        name: "估值资料 private.example.edu",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000009",
        course_id: "fin-01",
        name: "估值资料 ftp : / /private.example.edu",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000010",
        course_id: "fin-01",
        name: "估值资料",
        folders: ["www . private.example.edu"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000011",
        course_id: "fin-01",
        name: "联系abc@example.com资料",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000012",
        course_id: "fin-01",
        name: "网址private.example.edu资料",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
    ],
  });
  const env = envFor(bucket);

  const anonymous = await jsonRequest(env, "/course/directory");
  assert.equal(anonymous.response.status, 401);
  assert.equal(Object.hasOwn(anonymous.data, "items"), false);
  assert.equal(Object.hasOwn(anonymous.data, "facets"), false);

  const token = await register(env);
  const email = "reward-reader@example.com";
  const entitlementKey = `_account/entitlements/${encodeURIComponent(email)}`;
  bucket.seed(entitlementKey, {
    id: "entitlement-course-directory",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });

  const redactionTerms = env.COURSE_DIRECTORY_REDACT_TERMS;
  delete env.COURSE_DIRECTORY_REDACT_TERMS;
  const missingRedactionConfig = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(missingRedactionConfig.response.status, 503);
  assert.equal(Object.hasOwn(missingRedactionConfig.data, "items"), false);
  env.COURSE_DIRECTORY_REDACT_TERMS = redactionTerms;

  const firstPage = await jsonRequest(env, "/course/directory?page=1&page_size=2", { headers: bearer(token) });
  assert.equal(firstPage.response.status, 200);
  assert.equal(firstPage.data.total, 3, "records containing redaction markers or private contacts must be omitted");
  assert.equal(firstPage.data.items.length, 2);
  assert.equal(firstPage.data.has_more, true);
  assert.ok(bucket.jsonReadKeys.includes("_course-directory/v1/directory.json"));
  assert.equal(bucket.textReadKeys.includes("_course-directory/v1/directory.json"), false);
  assert.equal(firstPage.response.headers.get("cache-control"), "private, no-store, max-age=0");
  assert.ok(firstPage.data.facets.courses.some((entry) => entry.id === "cap-03" && entry.count === 1));
  assert.ok(firstPage.data.facets.top_entities.some((entry) => entry.name === "中国证监会"));
  const serialized = JSON.stringify(firstPage.data);
  assert.equal(serialized.includes("must/not/leave"), false);
  assert.equal(serialized.includes("private-object-key"), false);
  assert.equal(serialized.includes("private-locator"), false);
  assert.deepEqual(
    Object.keys(firstPage.data.items[0]).sort(),
    ["category", "course_id", "date", "entities", "extension", "folders", "id", "name", "size_label"],
  );

  const institutionSearch = await jsonRequest(
    env,
    `/course/directory?q=${encodeURIComponent("摩根大通 高盛")}&file_type=pdf`,
    { headers: bearer(token) },
  );
  assert.equal(institutionSearch.response.status, 200);
  assert.equal(institutionSearch.data.total, 1);
  assert.equal(institutionSearch.data.items[0].name, "摩根大通全球利率与外汇策略");
  assert.deepEqual(institutionSearch.data.items[0].entities, ["摩根大通", "高盛", "美银", "瑞银"]);

  const lawCourse = await jsonRequest(env, "/course/directory?course_id=law-01&category=%E8%B5%84%E6%9C%AC%E5%B8%82%E5%9C%BA%E6%B3%95%E5%BE%8B", {
    headers: bearer(token),
  });
  assert.equal(lawCourse.data.total, 1);
  assert.equal(lawCourse.data.items[0].extension, "docx");

  bucket.seed(entitlementKey, {
    id: "entitlement-course-directory",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 29 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const expiredSoon = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(expiredSoon.response.status, 403);
  assert.equal(Object.hasOwn(expiredSoon.data, "items"), false);
  assert.equal(Object.hasOwn(expiredSoon.data, "facets"), false);
});

test("course directory falls back to text parsing when the R2 body has no json method", async () => {
  const bucket = new MemoryR2();
  const directoryKey = "_course-directory/v1/directory.json";
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  bucket.seed(directoryKey, {
    schema_version: 1,
    generated_at: "2026-08-10T12:00:00+08:00",
    items: [{
      id: "file-fallback-01",
      course_id: "cap-03",
      name: "交易所上市审核问答",
      folders: ["上市实务"],
      extension: "pdf",
      size_label: "1 MB",
      date: "2026-08-10",
      entities: ["上交所"],
    }],
  });
  bucket.textOnlyKeys.add(directoryKey);
  const env = envFor(bucket);
  const token = await register(env);
  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-directory-fallback",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });
  const response = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(response.response.status, 200);
  assert.equal(response.data.total, 1);
  assert.ok(bucket.textReadKeys.includes(directoryKey));
  assert.equal(bucket.jsonReadKeys.includes(directoryKey), false);
});

test("course decks never stream from the site and eligible members request each material separately", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  bucket.seed("_course-materials/v1/manifest.json", {
    schema_version: 1,
    course: { id: "str-01", title: "麦府学堂｜战略与商业分析方法论" },
    item_count: 2,
    items: [
      { id: "maifu-01", title: "PPT项目故事线撰写指南", topic: "咨询交付", pages: 24 },
      { id: "maifu-02", title: "从数据到深刻洞察", topic: "数据洞察", pages: 32 },
    ],
  });
  const env = { ...envFor(bucket), BREVO_API_KEY: "brevo-test-key" };
  const materialPath = "/course/material?id=maifu-01";
  const materialKey = "_course-materials/v1/maifu-01.pdf";
  const pdf = new TextEncoder().encode("%PDF-1.7\ncourse-material-body\n%%EOF");
  bucket.seedBytes(materialKey, pdf);

  const anonymous = await jsonRequest(env, materialPath);
  assert.equal(anonymous.response.status, 404);
  assert.equal(anonymous.response.headers.get("cache-control"), "private, no-store, max-age=0");
  assert.equal(JSON.stringify(anonymous.data).includes("_course-materials"), false);

  const token = await register(env);
  const auth = { headers: bearer(token) };
  const stillUnavailable = await jsonRequest(env, materialPath, auth);
  assert.equal(stillUnavailable.response.status, 404);
  assert.equal(bucket.getKeys.includes(materialKey), false, "the revoked route must not touch the private PDF");

  const deniedRequest = await jsonRequest(env, "/course/material-request", {
    method: "POST",
    headers: { "content-type": "application/json", Origin: "https://portal.example.invalid", ...bearer(token) },
    body: JSON.stringify({ material_id: "maifu-01", page_path: "/courses.html", honeypot: "" }),
  });
  assert.equal(deniedRequest.response.status, 403);

  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-material",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });

  const originalFetch = globalThis.fetch;
  const sent = [];
  globalThis.fetch = async (url, options = {}) => {
    sent.push({ url: String(url), body: JSON.parse(String(options.body || "{}")) });
    return new Response(JSON.stringify({ messageId: `course-message-${sent.length}` }), {
      status: 201,
      headers: { "content-type": "application/json" },
    });
  };
  try {
    const submit = async (materialId) => jsonRequest(env, "/course/material-request", {
      method: "POST",
      headers: { "content-type": "application/json", Origin: "https://portal.example.invalid", ...bearer(token) },
      body: JSON.stringify({
        material_id: materialId,
        material_title: "伪造标题",
        recipient: "attacker@example.net",
        page_path: "/courses.html",
        honeypot: "",
      }),
    });
    const first = await submit("maifu-01");
    assert.equal(first.response.status, 202, JSON.stringify(first.data));
    assert.equal(first.data.deduplicated, false);
    assert.deepEqual(sent[0].body.to, [{ email: ["info", "@", "kc", "desk", ".com"].join("") }]);
    const serializedEmail = JSON.stringify(sent[0].body);
    assert.match(serializedEmail, /PPT项目故事线撰写指南/u);
    assert.doesNotMatch(serializedEmail, /伪造标题|attacker@example\.net/u);

    const duplicate = await submit("maifu-01");
    assert.equal(duplicate.response.status, 202);
    assert.equal(duplicate.data.deduplicated, true);
    assert.equal(sent.length, 1);

    const second = await submit("maifu-02");
    assert.equal(second.response.status, 202);
    assert.equal(second.data.deduplicated, false);
    assert.equal(sent.length, 2, "each deck must create its own request");
    const requestRows = [...bucket.rows.entries()].filter(([key]) => key.startsWith("_course-material-requests/v1/items/"));
    assert.equal(requestRows.length, 2);
    assert.ok(requestRows.every(([, row]) => JSON.parse(row.value).status === "sent"));
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report chat gives anonymous devices and registered free accounts one lifetime answer each", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  await seedReportChatLookup(bucket, [{
      id: reportId,
      title: "JPM-AI data center power constraints-260811",
      title_zh: "摩根大通：AI 数据中心电力瓶颈",
      institution: "摩根大通",
      date_folder: "260811",
      page_count: 28,
      available: true,
      attraction_score: 5,
    }], { ai: [reportId], 数据中心: [reportId], 电力: [reportId] });
  const env = envFor(bucket);
  const missingDevice = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 数据中心电力瓶颈" }),
  });
  assert.equal(missingDevice.response.status, 400);
  assert.equal(missingDevice.data.stage_code, "DEVICE_ID_REQUIRED");
  assert.equal(
    [...bucket.rows.keys()].some((key) => key.startsWith("_report-chat-archive/v1/items/")),
    false,
    "an invalid request without a device id is not a usage record",
  );
  const visitorId = "visitor-anon-0001";
  const anonymous = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 数据中心电力瓶颈", visitor_id: visitorId }),
  });
  assert.equal(anonymous.response.status, 200, JSON.stringify(anonymous.data));
  assert.deepEqual(anonymous.data.usage, {
    tier: "guest",
    limit: 1,
    count: 1,
    remaining: 0,
    period: "lifetime",
  });
  assert.match(anonymous.data.archive_id, /^[a-f0-9]{32}$/u);
  assert.match(anonymous.data.question_hash, /^[a-f0-9]{64}$/u);
  const anonymousLimited = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 数据中心电力瓶颈", visitor_id: visitorId }),
  });
  assert.equal(anonymousLimited.response.status, 429);
  assert.equal(anonymousLimited.data.stage_code, "USAGE_LIMIT");
  assert.equal(anonymousLimited.data.request_available, true);
  assert.match(anonymousLimited.data.question_hash, /^[a-f0-9]{64}$/u);
  assert.equal(
    [...bucket.rows.values()].some((row) => !row.binary && String(row.value).includes(visitorId)),
    false,
    "raw visitor ids must never be persisted",
  );
  const token = await register(env);
  const oversized = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI".repeat(9000) }),
  });
  assert.equal(oversized.response.status, 413);
  const result = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "找最近半年AI数据中心电力瓶颈相关的顶级投行报告" }),
  });
  assert.equal(result.response.status, 200, JSON.stringify(result.data));
  assert.deepEqual(result.data.usage, {
    tier: "registered",
    limit: 1,
    count: 1,
    remaining: 0,
    period: "lifetime",
  });
  assert.equal(result.data.recommendations[0].id, reportId);
  assert.equal(result.data.recommendations[0].attraction_score, 5);
  assert.equal(result.data.recommendations[0].available, true);
  assert.match(result.data.answer, /摩根大通/u);
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("tokens.tbl")));
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("items.tbl")));
  assert.equal(bucket.jsonReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
  assert.equal(bucket.jsonReadKeys.includes("edge-static/runtime-data/search_index.json"), false);
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/search_index.json"), false);
  assert.equal(Object.hasOwn(result.data.recommendations[0], "excerpt"), false);
  assert.equal(result.response.headers.get("cache-control"), "private, no-store, max-age=0");
  const registeredLimited = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "再问一次 AI 数据中心" }),
  });
  assert.equal(registeredLimited.response.status, 429);
  assert.equal(registeredLimited.data.usage.tier, "registered");
  assert.equal(registeredLimited.data.usage.period, "lifetime");
});

test("report chat enforces 2 daily turns for short members and 5 for advanced members", async () => {
  const report = { id: "quota-member-report", title: "AI infrastructure member research", attraction_score: 4 };

  const shortBucket = new MemoryR2();
  await seedReportChatLookup(shortBucket, [report], { ai: [report.id] });
  const shortEnv = envFor(shortBucket);
  const shortToken = await register(shortEnv);
  const now = new Date().toISOString();
  shortBucket.seed(`_account/access/${encodeURIComponent("reward-reader@example.com")}`, {
    id: "short-member-access",
    email: "reward-reader@example.com",
    access_mode: "all",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    duration_value: "1",
    download_limit: 0,
    download_count: 0,
    download_items: [],
    institutions: [],
    industries: [],
    page_ranges: [],
    note: "",
    change_id: "short-member-change",
    created_at: now,
    updated_at: now,
  });
  for (let turn = 1; turn <= 2; turn += 1) {
    const result = await jsonRequest(shortEnv, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(shortToken) },
      body: JSON.stringify({ question: `AI 基础设施会员研究 ${turn}` }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.usage.tier, "member");
    assert.equal(result.data.usage.limit, 2);
    assert.equal(result.data.usage.count, turn);
    assert.equal(result.data.usage.remaining, 2 - turn);
    assert.equal(result.data.usage.period, "day");
  }
  const shortLimited = await jsonRequest(shortEnv, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(shortToken) },
    body: JSON.stringify({ question: "AI 基础设施第三次研究" }),
  });
  assert.equal(shortLimited.response.status, 429);
  assert.equal(shortLimited.data.usage.tier, "member");
  assert.equal(shortLimited.data.usage.remaining, 0);

  const advancedBucket = new MemoryR2();
  await seedReportChatLookup(advancedBucket, [report], { ai: [report.id] });
  const advancedEnv = envFor(advancedBucket);
  const advancedToken = await register(advancedEnv);
  advancedBucket.seed(`_account/entitlements/${encodeURIComponent("reward-reader@example.com")}`, {
    id: "advanced-member-entitlement",
    email: "reward-reader@example.com",
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: now,
  });
  for (let turn = 1; turn <= 5; turn += 1) {
    const result = await jsonRequest(advancedEnv, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(advancedToken) },
      body: JSON.stringify({ question: `AI 高阶会员研究 ${turn}` }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.usage.tier, "advanced");
    assert.equal(result.data.usage.limit, 5);
    assert.equal(result.data.usage.count, turn);
    assert.equal(result.data.usage.remaining, 5 - turn);
    assert.equal(result.data.usage.period, "day");
  }
  const advancedLimited = await jsonRequest(advancedEnv, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(advancedToken) },
    body: JSON.stringify({ question: "AI 高阶会员第六次研究" }),
  });
  assert.equal(advancedLimited.response.status, 429);
  assert.equal(advancedLimited.data.usage.tier, "advanced");
  assert.equal(advancedLimited.data.usage.remaining, 0);
});

test("the super account has unlimited report chat", async () => {
  const bucket = new MemoryR2();
  const report = { id: "quota-admin-report", title: "AI infrastructure admin research", attraction_score: 4 };
  await seedReportChatLookup(bucket, [report], { ai: [report.id] });
  const env = envFor(bucket);
  const { token } = seedSuperAccount(bucket);
  for (let turn = 1; turn <= 6; turn += 1) {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: `AI 管理员研究 ${turn}` }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.deepEqual(result.data.usage, {
      tier: "admin",
      limit: null,
      count: 0,
      remaining: null,
      period: "unlimited",
    });
  }
  assert.equal([...bucket.rows.keys()].some((key) => key.startsWith("_account/report-chat-v3/") && key.includes("admin-a")), false);
});

test("report chat archives privately, supports admin curation and public cache reads, and emails only the fixed contact", async () => {
  const bucket = new MemoryR2();
  const report = { id: "archive-public-report", title: "AI infrastructure archive research", attraction_score: 5 };
  await seedReportChatLookup(bucket, [report], { ai: [report.id], 基础设施: [report.id] });
  const env = { ...envFor(bucket), BREVO_API_KEY: "brevo-test-key" };
  const visitorId = "visitor-archive-0001";
  const success = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 基础设施归档研究", visitor_id: visitorId }),
  });
  assert.equal(success.response.status, 200, JSON.stringify(success.data));
  const limited = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 基础设施继续研究", visitor_id: visitorId }),
  });
  assert.equal(limited.response.status, 429, JSON.stringify(limited.data));
  const archiveRows = [...bucket.rows.entries()].filter(([key]) => key.startsWith("_report-chat-archive/v1/items/"));
  assert.equal(archiveRows.length, 2);
  assert.deepEqual(new Set(archiveRows.map(([, row]) => JSON.parse(row.value).status)), new Set(["success", "limit"]));
  assert.equal(archiveRows.some(([, row]) => String(row.value).includes(visitorId)), false);

  const deniedHistory = await jsonRequest(env, "/account-admin/report-chat-history");
  assert.equal(deniedHistory.response.status, 403);
  const { token: adminToken } = seedSuperAccount(bucket);
  const history = await jsonRequest(env, "/account-admin/report-chat-history?limit=20", {
    headers: bearer(adminToken),
  });
  assert.equal(history.response.status, 200, JSON.stringify(history.data));
  assert.equal(history.data.items.length, 2);
  assert.ok(history.data.items.every((item) => item.published === false && item.public_id === ""));

  const curated = await jsonRequest(env, "/account-admin/report-chat-curation", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(adminToken) },
    body: JSON.stringify({ archive_id: success.data.archive_id, published: true, rank: 99 }),
  });
  assert.equal(curated.response.status, 200, JSON.stringify(curated.data));
  assert.equal(curated.data.item.id, success.data.archive_id);
  const publishedHistory = await jsonRequest(env, "/account-admin/report-chat-history?limit=20", {
    headers: bearer(adminToken),
  });
  const publishedArchive = publishedHistory.data.items.find((item) => item.id === success.data.archive_id);
  assert.equal(publishedArchive.published, true);
  assert.equal(publishedArchive.public_id, success.data.archive_id);

  const quotaKeysBeforePopular = [...bucket.rows.keys()].filter((key) => key.startsWith("_account/report-chat-v3/")).sort();
  const rangeReadsBeforePopular = bucket.rangeReadKeys.length;
  const popular = await jsonRequest(env, "/report-chat/popular");
  assert.equal(popular.response.status, 200);
  assert.equal(popular.data.total, 1);
  assert.equal(popular.data.items[0].id, success.data.archive_id);
  const detail = await jsonRequest(env, `/report-chat/popular?id=${success.data.archive_id}`);
  assert.equal(detail.response.status, 200, JSON.stringify(detail.data));
  assert.equal(detail.data.cached, true);
  assert.equal(detail.data.usage.tier, "public_cache");
  assert.match(detail.data.answer, /AI infrastructure archive research/u);
  const exact = await jsonRequest(env, `/report-chat/popular?q=${encodeURIComponent("AI 基础设施归档研究")}`);
  assert.equal(exact.response.status, 200);
  assert.equal(exact.data.id, success.data.archive_id);
  assert.deepEqual(
    [...bucket.rows.keys()].filter((key) => key.startsWith("_account/report-chat-v3/")).sort(),
    quotaKeysBeforePopular,
    "public cache reads must not consume quota",
  );
  assert.equal(bucket.rangeReadKeys.length, rangeReadsBeforePopular, "public cache reads must not perform model lookup reads");
  const publicPayload = JSON.stringify({ list: popular.data, detail: detail.data, exact: exact.data });
  assert.doesNotMatch(publicPayload, /actor|device_hash|curated_by|item_key|requester_email|@users\.portal/iu);

  const originalFetch = globalThis.fetch;
  const sent = [];
  globalThis.fetch = async (url, options = {}) => {
    sent.push({ url: String(url), body: JSON.parse(String(options.body || "{}")) });
    return new Response(JSON.stringify({ messageId: "brevo-message-1" }), {
      status: 201,
      headers: { "content-type": "application/json" },
    });
  };
  try {
    const invalidRequest = await jsonRequest(env, "/report-chat/request", {
      method: "POST",
      headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
      body: JSON.stringify({
        archive_id: success.data.archive_id,
        visitor_id: visitorId,
        requester_email: "guest@example.com",
      }),
    });
    assert.equal(invalidRequest.response.status, 409);

    const requestResult = await jsonRequest(env, "/report-chat/request", {
      method: "POST",
      headers: {
        "content-type": "application/json",
        Origin: "https://portal.example.invalid",
        "CF-Connecting-IP": "203.0.113.8",
      },
      body: JSON.stringify({
        archive_id: limited.data.archive_id,
        visitor_id: visitorId,
        requester_email: "guest@example.com",
        recipient: "attacker@example.net",
        page_path: "/",
      }),
    });
    assert.equal(requestResult.response.status, 202, JSON.stringify(requestResult.data));
    assert.equal(requestResult.data.status, "sent");
    assert.equal(sent.length, 1);
    assert.equal(sent[0].url, "https://api.brevo.com/v3/smtp/email");
    assert.deepEqual(sent[0].body.to, [{ email: ["info", "@", "kc", "desk", ".com"].join("") }]);
    assert.equal(JSON.stringify(sent[0].body).includes("attacker@example.net"), false);
    const persistedRequests = [...bucket.rows.entries()].filter(([key]) => key.startsWith("_report-chat-requests/v1/items/"));
    assert.equal(persistedRequests.length, 1);
    assert.equal(JSON.parse(persistedRequests[0][1].value).status, "sent");

    const duplicate = await jsonRequest(env, "/report-chat/request", {
      method: "POST",
      headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
      body: JSON.stringify({
        archive_id: limited.data.archive_id,
        visitor_id: visitorId,
        requester_email: "guest@example.com",
      }),
    });
    assert.equal(duplicate.response.status, 202);
    assert.equal(duplicate.data.status, "duplicate");
    assert.equal(sent.length, 1);
  } finally {
    globalThis.fetch = originalFetch;
  }

  const unpublished = await jsonRequest(env, "/account-admin/report-chat-curation", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(adminToken) },
    body: JSON.stringify({ archive_id: success.data.archive_id, published: false }),
  });
  assert.equal(unpublished.response.status, 200);
  const removed = await jsonRequest(env, `/report-chat/popular?id=${success.data.archive_id}`);
  assert.equal(removed.response.status, 404);
});

test("public analytics accepts report chat and course material events without storing the raw RAG question", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const waits = [];
  const context = { waitUntil(promise) { waits.push(promise); } };
  const questionHash = "a".repeat(64);
  const rawVisitorId = "visitor-analytics-raw-0001";
  const chat = await jsonRequest(env, "/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
    body: JSON.stringify({
      type: "report_chat_interaction",
      visitor_id: rawVisitorId,
      path: "/",
      data: {
        action: "submit",
        query: "这条原始问题不能进入 analytics",
        question_hash: questionHash,
      },
    }),
  }, context);
  assert.equal(chat.response.status, 204);
  const course = await jsonRequest(env, "/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", Origin: "https://portal.example.invalid" },
    body: JSON.stringify({
      type: "course_material_request",
      path: "/courses.html",
      data: {
        material_id: "maifu-01",
        material_title: "麦府学堂材料一",
        response_status: "requested",
      },
    }),
  }, context);
  assert.equal(course.response.status, 204);
  await Promise.all(waits);
  const events = [...bucket.rows.entries()]
    .filter(([key]) => key.startsWith("_analytics/events/"))
    .map(([, row]) => JSON.parse(row.value));
  const chatEvent = events.find((event) => event.type === "report_chat_interaction");
  assert.equal(chatEvent.question_hash, questionHash);
  assert.equal(chatEvent.query, "");
  assert.match(chatEvent.visitor_id, /^[a-f0-9]{64}$/u);
  assert.notEqual(chatEvent.visitor_id, rawVisitorId);
  assert.equal(JSON.stringify(chatEvent).includes("这条原始问题不能进入 analytics"), false);
  assert.equal(
    [...bucket.rows.entries()]
      .filter(([key]) => key.startsWith("_analytics/"))
      .some(([, row]) => String(row.value).includes(rawVisitorId)),
    false,
    "analytics primary and backup copies must not persist the raw RAG visitor id",
  );
  const courseEvent = events.find((event) => event.type === "course_material_request");
  assert.equal(courseEvent.target, "maifu-01");
  assert.equal(courseEvent.report_title, "麦府学堂材料一");
  assert.equal(courseEvent.status, "requested");
  assert.equal(courseEvent.availability, "requested");
});

test("report chat mixes same-source and topic-matched Charts without unrelated cross-report results", async () => {
  const bucket = new MemoryR2();
  const reportId = "1234567890abcdef12345678";
  const imageId = "c".repeat(64);
  const topicReportId = "fedcba9876543210fedcba98";
  const topicImageId = "d".repeat(64);
  const unrelatedReportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const unrelatedImageId = "e".repeat(64);
  const unresolvedImageId = "f".repeat(64);
  await seedReportResearchLookup(bucket, [{
    id: reportId,
    title: "AI data center power constraints",
    title_en: "AI data center power constraints",
    institution: "JPMorgan",
    industry: "Tech / AI / Semis",
    date_folder: "260829",
    page_count: 42,
    available: true,
  }], {
    ai: [{ id: reportId, tf: 12, chunks: ["c0001"] }],
    data: [{ id: reportId, tf: 8, chunks: ["c0001"] }],
    center: [{ id: reportId, tf: 8, chunks: ["c0001"] }],
    power: [{ id: reportId, tf: 7, chunks: ["c0001"] }],
  }, [[`${reportId}:c0001`, {
    id: "c0001",
    report_id: reportId,
    text: "JPMorgan expects AI data-center electricity demand to rise through 2030, while grid connection delays remain the principal deployment bottleneck.",
  }]]);
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    reports: [
      {
        report_id: reportId,
        title: "AI data center power constraints",
        date_folder: "260829",
        charts: [{
          id: "power-demand-chart",
          image_id: imageId,
          analysis_version: "chart-search-v2",
          title: "AI data-center electricity demand",
          content_kind: "chart",
          quality_score: 95,
          chart_type: "line",
          description: "Electricity demand rises through 2030.",
          trend_summary: "Upward",
          metrics: ["Electricity demand"],
          entities: ["JPMorgan"],
          keywords: ["AI", "data center", "power"],
        }, ...Array.from({ length: 6 }, (_value, index) => ({
          id: `same-source-fallback-${index}`,
          image_id: String(index).repeat(64),
          analysis_version: "chart-search-v2",
          title: `Legacy commodity inventory ${index}`,
          content_kind: "chart",
          quality_score: 90 - index,
          chart_type: "bar",
          description: "Historical commodity inventory levels.",
          trend_summary: "Mixed",
          keywords: ["commodities", "inventory"],
        }))],
      },
      {
        report_id: topicReportId,
        title: "Goldman AI data-center power outlook",
        date_folder: "260828",
        charts: [{
          id: "cross-report-topic-chart",
          image_id: topicImageId,
          analysis_version: "chart-search-v2",
          title: "AI data-center grid capacity",
          content_kind: "chart",
          quality_score: 91,
          chart_type: "line",
          description: "Power bottlenecks constrain new data-center connections.",
          trend_summary: "Grid capacity remains tight.",
          entities: ["Goldman Sachs"],
          keywords: ["AI", "power"],
        }],
      },
      {
        report_id: unrelatedReportId,
        title: "Luxury retail report",
        date_folder: "260829",
        charts: [{
          id: "unrelated-retail-chart",
          image_id: unrelatedImageId,
          analysis_version: "chart-search-v2",
          title: "Luxury retail foot traffic",
          content_kind: "chart",
          quality_score: 100,
          chart_type: "bar",
          description: "Store visits increased during the holiday period.",
          trend_summary: "Seasonal increase.",
          keywords: ["luxury", "retail"],
        }],
      },
      {
        report_id: "unresolved-report",
        title: "Unresolved AI data center report",
        date_folder: "260829",
        charts: [{
          id: "unresolved-topic-chart",
          image_id: unresolvedImageId,
          analysis_version: "chart-search-v2",
          title: "AI data-center capacity",
          content_kind: "chart",
          quality_score: 99,
          chart_type: "line",
          description: "AI data-center power capacity.",
          trend_summary: "Increasing.",
          keywords: ["AI", "data center"],
        }],
      },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  const result = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "研究人工智能数据中心的电力瓶颈" }),
  });

  assert.equal(result.response.status, 200, JSON.stringify(result.data));
  assert.equal(result.data.mode, "research");
  assert.equal(result.data.sources[0].id, reportId);
  assert.deepEqual(result.data.findings[0].source_ids, [reportId]);
  assert.equal(result.data.charts[0].image_id, imageId);
  assert.equal(result.data.charts[0].report_id, reportId);
  assert.equal(result.data.charts[1].image_id, topicImageId);
  assert.equal(result.data.charts[1].report_id, topicReportId);
  assert.equal(result.data.charts[1].report_title, "Goldman AI data-center power outlook");
  assert.equal(result.data.charts[1].date_folder, "260828");
  assert.equal(result.data.charts.some((chart) => chart.image_id === unrelatedImageId), false);
  assert.equal(result.data.charts.some((chart) => chart.image_id === unresolvedImageId), false);
  assert.equal(result.data.charts.length, 2, "irrelevant same-source charts must not be used as filler");
  assert.match(result.data.findings[0].summary, /grid connection delays/u);
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("evidence.tbl")));
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("evidence.dat")));
  const serialized = JSON.stringify(result.data);
  assert.equal(serialized.includes("_report-research"), false);
  assert.equal(serialized.includes("object_key"), false);
  assert.equal(result.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("report research real multi-facet question rejects generic AI, year, import, and SpaceX charts", async () => {
  const bucket = new MemoryR2();
  const sourceReportId = "101010101010101010101010";
  const crossReportId = "202020202020202020202020";
  const irrelevantSourceId = "303030303030303030303030";
  const powerOne = "1".repeat(64);
  const powerTwo = "2".repeat(64);
  const powerThree = "3".repeat(64);
  const capexCross = "4".repeat(64);
  const aiRevenue = "5".repeat(64);
  const yearRevenue = "6".repeat(64);
  const aiImport = "7".repeat(64);
  const spacex = "8".repeat(64);
  const aiCapexOnly = "9".repeat(64);
  const terms = ["ai", "data", "power", "capex", "supply", "center", "electricity"];
  const postings = Object.fromEntries(terms.map((term) => [term, [{
    id: sourceReportId,
    tf: 10,
    chunks: ["c000001"],
  }]]));
  postings.ai.push({ id: irrelevantSourceId, tf: 100, chunks: ["c000002"] });
  postings.capex.push({ id: irrelevantSourceId, tf: 100, chunks: ["c000002"] });
  await seedReportResearchLookup(bucket, [
    {
      id: sourceReportId,
      title: "Global AI data-center power and capex",
      institution: "JPMorgan",
      date_folder: "260830",
      available: true,
    },
    {
      id: irrelevantSourceId,
      title: "AI software capital expenditure",
      institution: "Unrelated Research",
      date_folder: "260830",
      available: true,
    },
  ], postings, [[`${sourceReportId}:c000001`, {
    id: "c000001",
    report_id: sourceReportId,
    text: "The report compares AI data-center power constraints, electricity supply structure, grid access and capital expenditure across the United States and China.",
  }], [`${irrelevantSourceId}:c000002`, {
    id: "c000002",
    report_id: irrelevantSourceId,
    text: "The report discusses AI software capital expenditure without data-center infrastructure.",
  }]]);
  const chart = (id, imageId, title, description, keywords, quality = 90) => ({
    id,
    image_id: imageId,
    analysis_version: "chart-search-v2",
    title,
    content_kind: "chart",
    quality_score: quality,
    chart_type: "bar",
    description,
    trend_summary: description,
    keywords,
  });
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    reports: [
      {
        report_id: sourceReportId,
        title: "Global AI data-center power and capex",
        date_folder: "260830",
        charts: [
          chart("power-one", powerOne, "AI data-center power grid", "Electricity bottlenecks constrain data-center deployment.", ["AI", "data", "center", "power"], 98),
          chart("power-two", powerTwo, "AI data-center electricity supply", "Power supply structures differ across markets.", ["AI", "data", "center", "electricity", "supply"], 97),
          chart("power-three", powerThree, "AI data-center grid queue", "Power grid queues remain a deployment constraint.", ["AI", "data", "center", "power"], 96),
          chart("same-source-ai-revenue", aiRevenue, "AI revenue 2027", "Revenue forecasts for software vendors.", ["AI", "revenue", "2027"], 100),
          chart("same-source-ai-capex-only", aiCapexOnly, "AI capex", "Capital expenditure for AI software vendors.", ["AI", "capex"], 100),
        ],
      },
      {
        report_id: crossReportId,
        title: "Asian technology investment",
        date_folder: "260829",
        charts: [
          chart("capex-cross", capexCross, "AI data-center capex", "Capital expenditure for AI data-center capacity.", ["AI", "data", "center", "capex"], 95),
          chart("year-revenue", yearRevenue, "2027 revenue", "Revenue projections by vendor.", ["2027", "revenue"], 100),
          chart("ai-import", aiImport, "AI imports", "Import volumes for AI devices.", ["AI", "import"], 100),
          chart("spacex", spacex, "SpaceX launches", "Launch cadence by mission.", ["SpaceX", "launch"], 100),
        ],
      },
    ],
  });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (_input, init) => {
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (requestPayload.max_tokens === 400) {
      return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
        core: [
          { name: "AI", required: true, terms: ["ai", "artificial", "intelligence"] },
          { name: "data center", required: true, terms: ["data", "center", "datacenter"] },
        ],
        facets: [
          { name: "power", terms: ["power", "electricity", "grid"] },
          { name: "capital expenditure", terms: ["capex", "capital", "expenditure"] },
          { name: "supply structure", terms: ["supply", "generation"] },
        ],
        terms,
      }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
    }
    const input = JSON.parse(requestPayload.messages[1].content);
    assert.equal(input.query_plan.terms.includes("2027"), false);
    assert.equal(input.query_plan.terms.filter((term) => ["ai", "artificial", "intelligence"].includes(term)).length, 1);
    const candidateIds = input.chart_candidates.map((row) => row.image_id);
    assert.equal(candidateIds.includes(aiRevenue), false);
    assert.equal(candidateIds.includes(yearRevenue), false);
    assert.equal(candidateIds.includes(aiImport), false);
    assert.equal(candidateIds.includes(spacex), false);
    assert.equal(candidateIds.includes(aiCapexOnly), false, "a Chart missing the required data-center core must be rejected");
    assert.equal(candidateIds.filter((id) => [powerOne, powerTwo, powerThree].includes(id)).length, 2);
    assert.equal(candidateIds.includes(capexCross), true);
    return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
      research_title: "AI 数据中心电力与资本开支研究",
      research_scope: "比较中美电力瓶颈、资本开支与供电结构。",
      executive_summary: "证据显示电力接入、供给结构与资本投入需要联合分析。",
      summary_source_ids: [sourceReportId],
      findings: [{ title: "联合约束", summary: "报告把电力接入、供给结构和资本投入视为相互关联的部署约束。", source_ids: [sourceReportId] }],
      data_points: [],
      chart_image_ids: [capexCross, powerTwo, powerOne],
    }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "比较全球主流机构对AI数据中心的判断，重点分析中美电力瓶颈、资本开支、供电结构，以及2027年前后的分歧" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(modelCalls, 2);
    assert.deepEqual(result.data.sources.map((row) => row.id), [sourceReportId], "a source missing one required core must be rejected");
    assert.deepEqual(result.data.charts.map((row) => row.image_id), [capexCross, powerTwo, powerOne]);
    assert.equal(JSON.stringify(result.data).includes(aiRevenue), false);
    assert.equal(JSON.stringify(result.data).includes(yearRevenue), false);
    assert.equal(JSON.stringify(result.data).includes(aiImport), false);
    assert.equal(JSON.stringify(result.data).includes(spacex), false);
    assert.equal(JSON.stringify(result.data).includes(aiCapexOnly), false);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research deterministic fallback preserves real concepts and requires an explicit chart allowlist", async () => {
  const bucket = new MemoryR2();
  const reportId = "404040404040404040404040";
  const chartImageId = "a".repeat(64);
  const lookupTerms = ["ai", "data", "power", "capex", "supply", "china", "center"];
  await seedReportResearchLookup(bucket, [{
    id: reportId,
    title: "AI data-center power, supply and capital expenditure",
    institution: "Research Bank",
    date_folder: "260830",
    available: true,
  }], Object.fromEntries(lookupTerms.map((term) => [term, [{
    id: reportId,
    tf: 10,
    chunks: ["c000001"],
  }]])), [[`${reportId}:c000001`, {
    id: "c000001",
    report_id: reportId,
    text: "The report compares AI data-center power bottlenecks, electricity supply structure and capital expenditure in China and the United States.",
  }]]);
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    reports: [{
      report_id: reportId,
      title: "AI data-center power, supply and capital expenditure",
      date_folder: "260830",
      charts: [{
        id: "relevant-power-chart",
        image_id: chartImageId,
        analysis_version: "chart-search-v2",
        title: "AI data-center power supply",
        content_kind: "chart",
        quality_score: 95,
        chart_type: "bar",
        description: "Power supply for AI data-center capacity.",
        trend_summary: "Electricity remains constrained.",
        keywords: ["AI", "data", "center", "power", "supply"],
      }],
    }],
  });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (_input, init) => {
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (modelCalls === 1) {
      assert.equal(requestPayload.max_tokens, 400);
      return new Response("planner unavailable", { status: 503 });
    }
    assert.equal(requestPayload.max_tokens, 7000);
    const input = JSON.parse(requestPayload.messages[1].content);
    assert.deepEqual(input.query_plan.terms, lookupTerms);
    assert.equal(input.query_plan.terms.some((term) => ["比较全球", "较全球主", "全球主流", "2027"].includes(term)), false);
    assert.equal(input.query_plan.core.filter((group) => group.required).length, 2);
    assert.deepEqual(input.query_plan.core.filter((group) => group.required).map((group) => group.name), ["人工智能", "数据中心"]);
    assert.deepEqual(input.chart_candidates.map((row) => row.image_id), [chartImageId]);
    return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
      research_title: "AI 数据中心跨报告研究",
      research_scope: "比较电力、供电结构和资本开支。",
      executive_summary: "报告同时讨论电力接入、供电结构和资本开支。",
      summary_source_ids: [reportId],
      findings: [{ title: "联合约束", summary: "电力、供电结构和资本开支共同影响部署。", source_ids: [reportId] }],
      data_points: [],
      chart_image_ids: chartImageId,
    }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "比较全球主流机构对AI数据中心的判断，重点分析中美电力瓶颈、资本开支、供电结构，以及2027年前后的分歧" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(modelCalls, 2);
    assert.equal(result.data.mode, "research");
    assert.equal(result.data.charts.length, 0, "a missing or wrong-type model allowlist must not attach every candidate");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research ranks exact ASCII chart terms and honors the model chart whitelist", async () => {
  const bucket = new MemoryR2();
  const sourceReportId = "cccccccccccccccccccccccc";
  const exactReportId = "bbbbbbbbbbbbbbbbbbbbbbbb";
  const genericImageId = "7".repeat(64);
  const exactImageId = "8".repeat(64);
  await seedReportResearchLookup(bucket, [{
    id: sourceReportId,
    title: "Semiconductor capital spending outlook",
    institution: "Research Bank",
    industry: "Semiconductors",
    date_folder: "260829",
    page_count: 36,
    available: true,
  }], {
    semiconductor: [{ id: sourceReportId, tf: 10, chunks: ["c0001"] }],
    capex: [{ id: sourceReportId, tf: 9, chunks: ["c0001"] }],
    forecasts: [{ id: sourceReportId, tf: 8, chunks: ["c0001"] }],
  }, [[`${sourceReportId}:c0001`, {
    id: "c0001",
    report_id: sourceReportId,
    text: "The report compares planned semiconductor investment across leading foundry and memory manufacturers over the forecast period.",
  }]]);
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    reports: [
      {
        report_id: sourceReportId,
        title: "Semiconductor capital spending outlook",
        date_folder: "260829",
        charts: [{
          id: "generic-capex-chart",
          image_id: genericImageId,
          analysis_version: "chart-search-v2",
          title: "Semiconductor capex and capital expenditure",
          content_kind: "chart",
          quality_score: 99,
          chart_type: "bar",
          description: "Capital expenditure by semiconductor category.",
          trend_summary: "Investment remains elevated.",
          keywords: ["capex", "semiconductors"],
        }],
      },
      {
        report_id: exactReportId,
        title: "Asian semiconductor investment",
        date_folder: "260828",
        charts: [{
          id: "exact-capex-forecasts-chart",
          image_id: exactImageId,
          analysis_version: "chart-search-v2",
          title: "Capex Forecasts",
          content_kind: "chart",
          quality_score: 90,
          chart_type: "bar",
          description: "Forecasts for TSMC, Intel, Samsung and SK Hynix.",
          trend_summary: "Manufacturer investment plans diverge.",
          entities: ["TSMC", "Intel", "Samsung", "SK Hynix"],
          keywords: ["semiconductor", "capex", "forecasts"],
        }],
      },
    ],
  });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input, init) => {
    assert.match(String(input), /^https:\/\/api\.deepseek\.com\/chat\/completions$/u);
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (requestPayload.max_tokens === 400) {
      return new Response(JSON.stringify({
        choices: [{ message: { content: JSON.stringify({
          core: [{ name: "semiconductor", terms: ["semiconductor"] }],
          facets: [{ name: "capital spending", terms: ["capex", "capital"] }],
          terms: ["semiconductor", "capex", "forecasts"],
        }) } }],
      }), { status: 200, headers: { "content-type": "application/json" } });
    }
    assert.equal(requestPayload.max_tokens, 7000);
    const modelInput = JSON.parse(requestPayload.messages[1].content);
    assert.equal(modelInput.chart_candidates[0].image_id, exactImageId);
    assert.equal(modelInput.chart_candidates[1].image_id, genericImageId);
    return new Response(JSON.stringify({
      choices: [{ message: { content: JSON.stringify({
        executive_summary: "半导体厂商资本开支计划存在分化。",
        summary_source_ids: [sourceReportId],
        chart_image_ids: [genericImageId],
      }) } }],
    }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "半导体：台积电、英特尔、三星、SK海力士 Capex Forecasts" }),
    });

    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.mode, "research");
    assert.equal(result.data.charts.length, 1);
    assert.equal(result.data.charts[0].image_id, genericImageId);
    assert.equal(result.data.charts[0].report_id, sourceReportId);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research rejects invented source ids and numeric claims absent from evidence", async () => {
  const bucket = new MemoryR2();
  const reportId = "abcdefabcdefabcdefabcdef";
  await seedReportResearchLookup(bucket, [{
    id: reportId,
    title: "AI infrastructure spending",
    institution: "Research Bank",
    date_folder: "260829",
    available: true,
  }], {
    ai: [{ id: reportId, tf: 5, chunks: ["c000001"] }],
    capex: [{ id: reportId, tf: 4, chunks: ["c000001"] }],
  }, [[`${reportId}:c000001`, {
    id: "c000001",
    report_id: reportId,
    text: "AI infrastructure capital expenditure increased 25% in 2026 according to the report evidence.",
  }]]);
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (input, init) => {
    assert.match(String(input), /^https:\/\/api\.deepseek\.com\/chat\/completions$/u);
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (requestPayload.max_tokens === 400) {
      return new Response(JSON.stringify({
        choices: [{ message: { content: JSON.stringify({
          core: [{ name: "AI", terms: ["ai", "artificial", "intelligence"] }],
          facets: [{ name: "capital expenditure", terms: ["capex", "capital", "expenditure"] }],
          terms: ["ai", "capex", "capital", "expenditure", "2027"],
        }) } }],
      }), { status: 200, headers: { "content-type": "application/json" } });
    }
    assert.equal(requestPayload.max_tokens, 7000);
    assert.match(requestPayload.messages[0].content, /5-8 substantive findings/u);
    return new Response(JSON.stringify({
      choices: [{ message: { content: JSON.stringify({
        research_title: "AI 资本开支证据研究",
        research_scope: "比较 AI 资本开支的证据、分歧与边界。",
        executive_summary: "证据显示资本开支增长 25%。虚构增长 99%。定性判断仍需结合报告边界。",
        summary_source_ids: [reportId, "ffffffffffffffffffffffff"],
        findings: [
          { title: "有证据结论", summary: "资本开支增长 25%。虚构情景达到 99%。定性结论仍然成立。", source_ids: [reportId] },
          { title: "伪来源结论", summary: "不存在的结论。", source_ids: ["ffffffffffffffffffffffff"] },
        ],
        data_points: [
          { label: "资本开支增长", value: "25%", context: "2026", source_ids: [reportId] },
          { label: "虚构增长", value: "99%", context: "2026", source_ids: [reportId] },
          { label: "资本开支增长", value: "25%", context: "虚构的 2035 情景", source_ids: [reportId] },
        ],
        chart_image_ids: ["d".repeat(64)],
      }) } }],
    }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "AI 资本开支研究" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(modelCalls, 2);
    assert.equal(result.data.research_title, "AI 资本开支证据研究");
    assert.match(result.data.research_scope, /资本开支/u);
    assert.match(result.data.generated_at, /^\d{4}-\d{2}-\d{2}T/u);
    assert.deepEqual(result.data.summary_source_ids, [reportId]);
    assert.equal(result.data.findings.length, 1);
    assert.deepEqual(result.data.findings[0].source_ids, [reportId]);
    assert.match(result.data.findings[0].summary, /定性结论仍然成立/u);
    assert.equal(result.data.data_points.length, 1);
    assert.equal(result.data.data_points[0].value, "25%");
    assert.equal(JSON.stringify(result.data).includes("99%"), false);
    assert.equal(JSON.stringify(result.data).includes("2035"), false);
    assert.equal(JSON.stringify(result.data).includes("ffffffffffffffffffffffff"), false);
    assert.equal(result.data.charts.length, 0);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research cold-cache worst case stays below the 50-subrequest boundary", async () => {
  const bucket = new MemoryR2();
  const reportIds = ["1", "2", "3", "4"].map((digit) => digit.repeat(24));
  const items = reportIds.map((id, index) => ({
    id,
    title: `AI infrastructure research ${index + 1}`,
    institution: `Research Bank ${index + 1}`,
    date_folder: "260829",
    available: true,
  }));
  const postings = Object.fromEntries(
    ["ai", "data", "center", "power", "electricity", "capital", "expenditure"].map((term) => [
      term,
      reportIds.map((id) => ({ id, tf: 12, chunks: ["c000001", "c000002"] })),
    ]),
  );
  const evidence = reportIds.flatMap((id, index) => [
    [`${id}:c000001`, {
      id: "c000001",
      report_id: id,
      text: `Report ${index + 1} discusses AI data-center power demand and grid connection constraints in detailed evidence.`,
    }],
    [`${id}:c000002`, {
      id: "c000002",
      report_id: id,
      text: `Report ${index + 1} compares capital expenditure, deployment timing, and supplier capacity using sourced evidence.`,
    }],
  ]);
  await seedReportResearchLookup(bucket, items, postings, evidence);
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  bucket.getKeys.length = 0;
  bucket.putKeys.length = 0;
  bucket.rangeReadKeys.length = 0;
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (_input, init) => {
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (requestPayload.max_tokens === 400) {
      return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
        core: [
          { name: "AI", terms: ["ai", "artificial", "intelligence"] },
          { name: "data center", terms: ["data", "center", "datacenter"] },
        ],
        facets: [
          { name: "power", terms: ["power", "electricity", "grid"] },
          { name: "capital expenditure", terms: ["capital", "expenditure", "capex"] },
        ],
        terms: ["ai", "data", "power", "capital", "center", "electricity", "expenditure"],
      }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
    }
    assert.equal(requestPayload.max_tokens, 7000);
    const modelInput = JSON.parse(requestPayload.messages[1].content);
    assert.deepEqual(modelInput.query_plan.terms, ["ai", "data", "power", "capital", "center", "electricity", "expenditure"]);
    assert.equal(new Set(modelInput.query_plan.terms).size, 7);
    assert.deepEqual(modelInput.sources.map((source) => source.evidence.length), [2, 2, 1, 1]);
    return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
      research_title: "AI infrastructure research",
      research_scope: "AI data-center power and capital expenditure",
      executive_summary: "多份报告共同讨论电力约束与资本开支。",
      summary_source_ids: reportIds,
      findings: [{ title: "跨报告结论", summary: "报告共同指出电力接入约束，并比较资本开支与部署节奏。", source_ids: reportIds }],
      data_points: [],
      chart_image_ids: [],
    }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "ai data center power capital expenditure" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.mode, "research");
    assert.equal(result.data.sources.length, 4);
    assert.equal(modelCalls, 2);
    assert.ok(bucket.rangeReadKeys.length <= 34, `unexpected research range reads: ${bucket.rangeReadKeys.length}`);
    const worstCaseSubrequests = bucket.getKeys.length + bucket.putKeys.length + modelCalls;
    assert.ok(
      worstCaseSubrequests <= 50,
      `unexpected research subrequests: ${worstCaseSubrequests} (get=${bucket.getKeys.length}, put=${bucket.putKeys.length}, model=${modelCalls})`,
    );
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research early miss uses only three discovery terms and four items within budget", async () => {
  const bucket = new MemoryR2();
  const researchTerms = ["ai", "data", "power", "capital", "center", "electricity", "expenditure"];
  await seedReportResearchLookup(
    bucket,
    [],
    Object.fromEntries(researchTerms.map((term) => [term, []])),
    [],
  );
  const discoveryItems = Array.from({ length: 6 }, (_value, index) => ({
    id: `discovery-${index}`,
    title: `AI data-center power report ${index}`,
    institution: `Bank ${index}`,
    attraction_score: 4,
  }));
  await seedReportChatLookup(bucket, discoveryItems, {
    ai: discoveryItems.map((item) => item.id),
    data: discoveryItems.map((item) => item.id),
    power: discoveryItems.map((item) => item.id),
  });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  bucket.getKeys.length = 0;
  bucket.putKeys.length = 0;
  bucket.rangeReadKeys.length = 0;
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (_input, init) => {
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    if (requestPayload.max_tokens === 400) {
      return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
        core: [{ name: "AI data center", terms: ["ai", "data", "center"] }],
        facets: [
          { name: "power", terms: ["power", "electricity"] },
          { name: "capital", terms: ["capital", "expenditure"] },
        ],
        terms: researchTerms,
      }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
    }
    assert.equal(requestPayload.max_tokens, 1200);
    const input = JSON.parse(requestPayload.messages[1].content);
    assert.equal(input.candidates.length, 4);
    return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
      answer: "找到 4 份相关报告，可进一步指定机构或指标。",
      recommended_ids: input.candidates.map((item) => item.id),
      follow_up_questions: [],
    }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "AI data center power capital expenditure 2027" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.mode, "discovery");
    assert.equal(result.data.sources.length, 4);
    assert.equal(modelCalls, 2);
    assert.ok(bucket.rangeReadKeys.length <= 28, `unexpected miss range reads: ${bucket.rangeReadKeys.length}`);
    const totalSubrequests = bucket.getKeys.length + bucket.putKeys.length + modelCalls;
    assert.ok(totalSubrequests <= 50, `unexpected miss subrequests: ${totalSubrequests}`);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research partial evidence miss does not cascade into discovery", async () => {
  const bucket = new MemoryR2();
  const reportId = "abababababababababababab";
  await seedReportResearchLookup(bucket, [{
    id: reportId,
    title: "AI capital expenditure outlook",
    institution: "Research Bank",
    available: true,
  }], {
    ai: [{ id: reportId, tf: 8, chunks: ["c000001", "c000002"] }],
    capex: [{ id: reportId, tf: 7, chunks: ["c000001", "c000002"] }],
  }, []);
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  bucket.getKeys.length = 0;
  bucket.putKeys.length = 0;
  const originalFetch = globalThis.fetch;
  let modelCalls = 0;
  globalThis.fetch = async (_input, init) => {
    modelCalls += 1;
    const requestPayload = JSON.parse(String(init && init.body || "{}"));
    assert.equal(requestPayload.max_tokens, 400);
    return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
      core: [{ name: "AI", terms: ["ai"] }],
      facets: [{ name: "capital expenditure", terms: ["capex"] }],
      terms: ["ai", "capex"],
    }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "AI capital expenditure" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.equal(result.data.mode, "research");
    assert.equal(result.data.sources.length, 1);
    assert.equal(result.data.findings.length, 0);
    assert.match(result.data.executive_summary, /未读取到可用的正文证据块/u);
    assert.equal(modelCalls, 1, "partial evidence must not call synthesis or discovery models");
    assert.equal(bucket.getKeys.includes("_report-chat/v2/manifest.json"), false);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("report research item and evidence read failures stay partial instead of cascading to discovery", async (t) => {
  for (const stage of ["items", "evidence"]) {
    await t.test(stage, async () => {
      const bucket = new MemoryR2();
      const reportId = stage === "items" ? "cd".repeat(12) : "ef".repeat(12);
      await seedReportResearchLookup(bucket, [{
        id: reportId,
        title: "AI data-center capital expenditure",
        institution: "Research Bank",
        available: true,
      }], {
        ai: [{ id: reportId, tf: 8, chunks: ["c000001"] }],
        data: [{ id: reportId, tf: 8, chunks: ["c000001"] }],
        capex: [{ id: reportId, tf: 7, chunks: ["c000001"] }],
      }, [[`${reportId}:c000001`, {
        id: "c000001",
        report_id: reportId,
        text: "AI data-center capital expenditure is discussed in the report evidence.",
      }]]);
      const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
      const token = await register(env);
      bucket.getKeys.length = 0;
      bucket.putKeys.length = 0;
      const originalFetch = globalThis.fetch;
      let modelCalls = 0;
      globalThis.fetch = async (_input, init) => {
        modelCalls += 1;
        const requestPayload = JSON.parse(String(init && init.body || "{}"));
        assert.equal(requestPayload.max_tokens, 400, "partial lookup must never reach synthesis or discovery");
        bucket.failNextGetExact = `_report-research/v1/releases/test/${stage}.tbl`;
        return new Response(JSON.stringify({ choices: [{ message: { content: JSON.stringify({
          core: [
            { name: "AI", required: true, terms: ["ai"] },
            { name: "data center", required: true, terms: ["data"] },
          ],
          facets: [{ name: "capital expenditure", terms: ["capex"] }],
          terms: ["ai", "data", "capex"],
        }) } }] }), { status: 200, headers: { "content-type": "application/json" } });
      };
      try {
        const result = await jsonRequest(env, "/report-chat", {
          method: "POST",
          headers: { "content-type": "application/json", ...bearer(token) },
          body: JSON.stringify({ question: "AI data center capital expenditure" }),
        });
        assert.equal(result.response.status, 200, JSON.stringify(result.data));
        assert.equal(result.data.mode, "research");
        assert.equal(modelCalls, 1);
        assert.equal(result.data.findings.length, 0);
        assert.match(result.data.executive_summary, /未读取到可用的正文证据块/u);
        assert.equal(bucket.getKeys.includes("_report-chat/v2/manifest.json"), false);
        assert.equal(result.data.sources.length, stage === "items" ? 0 : 1);
      } finally {
        globalThis.fetch = originalFetch;
      }
    });
  }
});

test("report chat rejects an exhausted registered lifetime limit before lookup or model work", async () => {
  const bucket = new MemoryR2();
  await seedReportChatLookup(bucket, [{ id: "limit-test-report", title: "Limit Test", attraction_score: 2 }], { ai: ["limit-test-report"] });
  const env = envFor(bucket);
  const token = await register(env);
  bucket.seed(`_account/report-chat-v3/lifetime/account/${encodeURIComponent("reward-reader@example.com")}`, {
    version: 3,
    identity_kind: "account",
    identity: "reward-reader@example.com",
    tier: "registered",
    period: "lifetime",
    count: 1,
    updated_at: new Date().toISOString(),
  });
  bucket.textReadKeys.length = 0;
  const limited = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心" }),
  });
  assert.equal(limited.response.status, 429);
  assert.equal(limited.data.stage_code, "USAGE_LIMIT");
  assert.equal(limited.data.usage.tier, "registered");
  assert.equal(limited.data.usage.period, "lifetime");
  assert.match(limited.data.request_hint, /^[A-Z0-9]{10}$/u);
  assert.equal(bucket.rangeReadKeys.some((key) => key.endsWith("tokens.tbl")), false);
  assert.equal(bucket.rangeReadKeys.some((key) => key.endsWith("tokens.dat")), false);
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
});

test("report chat lookup failures return actionable private JSON and do not consume a turn", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const token = await register(env);
  const usageKey = `_account/report-chat-v3/lifetime/account/${encodeURIComponent("reward-reader@example.com")}`;
  const failed = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心" }),
  });
  assert.equal(failed.response.status, 503);
  assert.equal(failed.data.stage_code, "LOOKUP_MANIFEST");
  assert.match(failed.data.request_hint, /^[A-Z0-9]{10}$/u);
  assert.equal(JSON.parse(bucket.rows.get(usageKey).value).count, 0);
  assert.equal(failed.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("report chat reserves before model work so concurrent free requests call the model once", async () => {
  const bucket = new MemoryR2();
  const reportId = "concurrent-model-report";
  await seedReportChatLookup(bucket, [{ id: reportId, title: "AI concurrent model report", attraction_score: 4 }], {
    ai: [reportId],
  });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  let modelCalls = 0;
  let markModelStarted;
  let finishModel;
  const modelStarted = new Promise((resolve) => { markModelStarted = resolve; });
  const modelGate = new Promise((resolve) => { finishModel = resolve; });
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => {
    modelCalls += 1;
    markModelStarted();
    await modelGate;
    return new Response(JSON.stringify({
      choices: [{ message: { content: JSON.stringify({
        answer: "并发请求只允许一次模型调用。",
        recommended_ids: [reportId],
      }) } }],
    }), { status: 200, headers: { "content-type": "application/json" } });
  };
  try {
    const makeRequest = () => jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ question: "AI 并发额度研究" }),
    });
    const firstPromise = makeRequest();
    await modelStarted;
    const second = await makeRequest();
    assert.equal(second.response.status, 429, JSON.stringify(second.data));
    assert.equal(modelCalls, 1);
    finishModel();
    const first = await firstPromise;
    assert.equal(first.response.status, 200, JSON.stringify(first.data));
    assert.equal(first.data.usage.count, 1);
  } finally {
    finishModel();
    globalThis.fetch = originalFetch;
  }
});

test("report chat random-access retrieval stays within the Worker subrequest budget", async () => {
  const bucket = new MemoryR2();
  const items = Array.from({ length: 20 }, (_, index) => ({
    id: `budget-report-${String(index).padStart(2, "0")}`,
    title: `AI data center report ${index}`,
    institution: index === 0 ? "摩根大通" : "Research",
    attraction_score: index === 0 ? 5 : 2,
  }));
  const ids = items.map((item) => item.id);
  await seedReportChatLookup(bucket, items, {
    ai: ids,
    数据中心: ids,
    数据: ids,
    中心: ids,
    电力: ids,
    瓶颈: ids,
    资本: ids,
    开支: ids,
  });
  const env = envFor(bucket);
  const token = await register(env);
  bucket.rangeReadKeys.length = 0;
  const result = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心 电力瓶颈 资本开支" }),
  });
  assert.equal(result.response.status, 200, JSON.stringify(result.data));
  assert.ok(result.data.recommendations.length <= 8);
  assert.ok(
    result.data.recommendations.every((item) => !Object.hasOwn(item, "available")),
    "lookup records without a PDF state must remain unknown",
  );
  assert.ok(bucket.rangeReadKeys.length <= 32, `unexpected lookup range reads: ${bucket.rangeReadKeys.length}`);
});

test("course chat uses the compact private recommendation index, enforces membership, and returns no locators", async () => {
  const bucket = new MemoryR2();
  await seedCourseChatLookup(bucket, [{
      id: "file-course-chat-01",
      course_id: "fin-01",
      name: "摩根大通投行估值与建模案例",
      folders: ["投行面试", "估值建模"],
      extension: "xlsx",
      size_label: "4.2 MB",
      date: "2026-08-12",
      entities: ["摩根大通", "高盛"],
      source_path: "/private/course/source/file.xlsx",
      object_key: "private-course-object",
    }], { 摩根大通: ["file-course-chat-01"], 投行: ["file-course-chat-01"], 建模: ["file-course-chat-01"] });
  const env = envFor(bucket);
  const token = await register(env);
  const denied = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ context: "course", question: "摩根大通 投行 建模" }),
  });
  assert.equal(denied.response.status, 403);
  assert.equal(Object.hasOwn(denied.data, "recommendations"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v2/chat-lookup/manifest.json"), false);

  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-chat",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });
  bucket.jsonReadKeys.length = 0;
  const allowed = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ context: "course", question: "摩根大通 投行 建模" }),
  });
  assert.equal(allowed.response.status, 200, JSON.stringify(allowed.data));
  assert.equal(allowed.data.recommendations[0].id, "file-course-chat-01");
  assert.equal(allowed.data.recommendations[0].kind, "course");
  assert.equal(allowed.data.recommendations[0].attraction_score, 5);
  assert.equal(allowed.data.recommendations[0].title, "摩根大通投行估值与建模案例");
  assert.equal(allowed.data.recommendations[0].course_title, "财务建模与企业估值");
  assert.equal(allowed.data.recommendations[0].category, "金融建模");
  assert.equal(allowed.data.recommendations[0].file_type, "spreadsheet");
  const serialized = JSON.stringify(allowed.data);
  assert.equal(serialized.includes("/private/course"), false);
  assert.equal(serialized.includes("private-course-object"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v2/chat-lookup/manifest.json"), true);
  assert.equal(bucket.jsonReadKeys.includes("_course-directory/v1/chat-index.json"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v1/chat-index.json"), false);
  assert.equal(bucket.jsonReadKeys.includes("_course-directory/v1/directory.json"), false);
  assert.equal(allowed.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("course chat falls back to grounded recommendations when DeepSeek is unavailable", async () => {
  const bucket = new MemoryR2();
  await seedCourseChatLookup(bucket, [{
      id: "file-course-chat-fallback-01",
      course_id: "fin-01",
      name: "高盛并购估值建模案例",
      folders: ["并购", "估值建模"],
      extension: "xlsx",
      size_label: "3.8 MB",
      date: "2026-08-12",
      entities: ["高盛"],
    }], { 高盛: ["file-course-chat-fallback-01"], 并购: ["file-course-chat-fallback-01"], 估值: ["file-course-chat-fallback-01"] });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-chat-fallback",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });

  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input) => {
    assert.match(String(input), /^https:\/\/api\.deepseek\.com\/chat\/completions$/u);
    throw new Error("injected DeepSeek transport failure");
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ context: "course", question: "高盛 并购 估值建模" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.match(result.data.answer, /高盛并购估值建模案例/u);
    assert.equal(result.data.recommendations[0].id, "file-course-chat-fallback-01");
    assert.equal(result.data.recommendations[0].attraction_score, 5);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("chart gallery exposes only opaque image ids and streams immutable images", async () => {
  const bucket = new MemoryR2();
  const imageId = "b".repeat(64);
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    updated_at_bjt: "2026-08-12T10:00:00+08:00",
    reports: [{
      report_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
      title: "摩根大通 AI 数据中心报告",
      date_folder: "260812",
      charts: [{
        id: "chart-1",
        analysis_version: "chart-search-v2",
        image_id: imageId,
        title: "数据中心电力需求",
        content_kind: "chart",
        quality_score: 96,
        chart_type: "line",
        description: "2025-2030 年电力需求持续增长。",
        trend_summary: "上升",
        metrics: ["电力需求"],
        entities: ["摩根大通"],
        periods: ["2025-2030"],
        geographies: ["美国"],
        units: ["GW"],
        keywords: ["AI"],
        private_path: "/must/not/leak.jpg",
      }, {
        id: "legacy-chart",
        image_id: "c".repeat(64),
        title: "旧版未严格复核图片",
        chart_type: "other",
        description: "不应进入图表库。",
        entities: ["AI"],
      }],
    }],
  });
  bucket.seedBytes(`_chart-search/v1/images/${imageId}.jpg`, [255, 216, 255, 217]);
  const env = envFor(bucket);
  const gallery = await jsonRequest(env, "/charts?q=AI");
  assert.equal(gallery.response.status, 200);
  assert.equal(gallery.data.total, 1);
  assert.equal(gallery.data.items[0].image_id, imageId);
  assert.equal(Object.hasOwn(gallery.data.items[0], "private_path"), false);
  const image = await worker.fetch(new Request(`https://worker.test/charts/image?id=${imageId}`), env, { waitUntil() {} });
  assert.equal(image.status, 200);
  assert.equal(image.headers.get("content-type"), "image/jpeg");
  assert.match(image.headers.get("cache-control"), /immutable/u);
  const invalid = await jsonRequest(env, "/charts/image?id=../../private");
  assert.equal(invalid.response.status, 400);
});

test("restricted course catalog and contact are absent from the unauthenticated static page", async () => {
  const { readFile } = await import("node:fs/promises");
  const html = await readFile(path.join(root, "portal_suite/site_src/courses.html"), "utf8");
  const loweredHtml = html.toLowerCase();
  for (const marker of restrictedCourseMarkers) {
    assert.equal(loweredHtml.includes(marker.toLowerCase()), false, `restricted marker leaked: ${marker}`);
  }
  assert.doesNotMatch(html, /Support Contact|support@portal\.example\.invalid|mailto:/u);
  assert.match(html, /id="courseCatalog"[^>]*hidden/u);
});

test("course frontend renders the complete structured catalog with topic filters", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  const chatSource = await readFile(path.join(root, "portal_suite/site_src/assets/report-chat.js"), "utf8");
  const styles = await readFile(path.join(root, "portal_suite/site_src/assets/styles.css"), "utf8");
  assert.match(source, /data\.course_catalog/u);
  assert.match(source, /courseSearchInput/u);
  assert.match(source, /courseCategoryFilter/u);
  assert.match(source, /escapeHtml\(product\.title\)/u);
  assert.match(source, /escapeHtml\(product\.summary\)/u);
  assert.match(source, /escapeHtml\(product\.audience\)/u);
  const courseCatalogSource = source.slice(
    source.indexOf("function renderCourseCatalog"),
    source.indexOf("async function refresh()", source.indexOf("function renderCourseCatalog")),
  );
  assert.match(courseCatalogSource, /filter\(Boolean\)\.slice\(0, 120\)/u);
  assert.doesNotMatch(courseCatalogSource, /filter\(Boolean\)\.slice\(0, 12\)/u);
  assert.match(styles, /\.course-grid\s*\{[\s\S]*?grid-template-columns:\s*repeat\(3,/u);
  assert.match(styles, /\.course-card\[hidden\]\s*\{[\s\S]*?display:\s*none/u);
  assert.match(chatSource, /context:\s*"course"/u);
  assert.match(chatSource, /data-course-query/u);
  assert.match(chatSource, /courseDirectorySearch/u);
  assert.match(chatSource, /AbortController/u);
  assert.match(chatSource, /HTTP \$\{response\.status\}/u);
  assert.match(chatSource, /stage_code/u);
  assert.match(chatSource, /请求超过 20 秒/u);
});

test("frontend distinguishes an already-used daily reward from a successful claim", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  assert.match(source, /if \(data\.already_claimed_today\)/u);
  assert.match(source, /if \(!data\.claimed\) throw new Error/u);
  const duplicateBranch = source.slice(
    source.indexOf("if (data.already_claimed_today)"),
    source.indexOf("if (data.already_owned)"),
  );
  assert.doesNotMatch(duplicateBranch, /portal-reward-change|status:\s*"success"/u);
});
