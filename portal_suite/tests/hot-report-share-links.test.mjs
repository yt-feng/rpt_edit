import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const { default: worker } = await import(workerPath);

const MASTER_KEY = "portal-master-key";
const PASSWORD_SECRET = "portal-password-secret";
const HOT_REPORT_ID = "hot:4923f67d75a90464";
const HOT_REPORT_SLUG = HOT_REPORT_ID.slice("hot:".length);
const HOT_REPORT_ITEM_KEY = `_hot-reports/items/${HOT_REPORT_SLUG}.json`;
const HOT_REPORT_PDF_KEY = `_hot-reports/pdfs/${HOT_REPORT_SLUG}.pdf`;
const HOT_REPORT_PDF = new TextEncoder().encode("%PDF-1.7\nhot report fixture\n%%EOF");

class MemoryR2 {
  constructor() {
    this.data = new Map();
  }

  seed(key, value) {
    this.data.set(key, typeof value === "string" || value instanceof Uint8Array ? value : JSON.stringify(value));
  }

  async get(key) {
    if (!this.data.has(key)) return null;
    const value = this.data.get(key);
    const bytes = value instanceof Uint8Array ? value : new TextEncoder().encode(String(value));
    return {
      body: bytes,
      size: bytes.byteLength,
      etag: `etag-${key}`,
      async text() {
        return value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value);
      },
    };
  }

  async head(key) {
    if (!this.data.has(key)) return null;
    const value = this.data.get(key);
    const bytes = value instanceof Uint8Array ? value : new TextEncoder().encode(String(value));
    return {
      key,
      size: bytes.byteLength,
      etag: `etag-${key}`,
      uploaded: "2026-08-04T01:34:09.548Z",
      customMetadata: {},
    };
  }
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY,
    PASSWORD_SECRET,
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  };
}

function seedHotReport(bucket) {
  bucket.seed(HOT_REPORT_ITEM_KEY, {
    id: HOT_REPORT_ID,
    source: "hot",
    title: "Global EES Tracker July",
    title_cn: "全球ESS追踪器 - 2026年7月",
    institution: "Bern",
    date: "2026-08-04",
    description: "",
    filename: "global-ees-tracker-july.pdf",
    size_bytes: HOT_REPORT_PDF.byteLength,
    sort_order: 1785807249548,
    created_at: "2026-08-04T01:34:09.548Z",
    updated_at: "2026-08-04T01:34:09.548Z",
    retention_state: "active",
  });
  bucket.seed(HOT_REPORT_PDF_KEY, HOT_REPORT_PDF);
}

async function jsonRequest(env, path, body, headers = {}) {
  const response = await worker.fetch(new Request(`https://worker.test${path}`, {
    method: "POST",
    headers: { "content-type": "application/json", ...headers },
    body: JSON.stringify(body),
  }), env, { waitUntil() {} });
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

async function adminToken(env) {
  const { response, data } = await jsonRequest(env, "/admin/login", { key: MASTER_KEY });
  assert.equal(response.status, 200);
  assert.equal(data.ok, true);
  assert.ok(data.token);
  return data.token;
}

test("admin generated hot report password unlocks PDF without an account", async () => {
  const bucket = new MemoryR2();
  seedHotReport(bucket);
  const env = envFor(bucket);
  const token = await adminToken(env);

  const generated = await jsonRequest(env, "/admin/report-password", {
    id: HOT_REPORT_ID,
    source: "hot",
    token,
  });
  assert.equal(generated.response.status, 200);
  assert.equal(generated.data.id, HOT_REPORT_ID);
  assert.equal(generated.data.source, "hot");
  assert.match(generated.data.password, /^PORTAL-[A-Z2-7]{4}-[A-Z2-7]{4}-[A-Z2-7]{4}$/);

  const download = await worker.fetch(new Request("https://worker.test/hot-reports/pdf", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ id: HOT_REPORT_ID, password: generated.data.password }),
  }), env, { waitUntil() {} });
  assert.equal(download.status, 200);
  assert.equal(download.headers.get("content-type"), "application/pdf");
  assert.match(download.headers.get("content-disposition") || "", /global-ees-tracker-july\.pdf/);
  assert.equal(await download.text(), new TextDecoder().decode(HOT_REPORT_PDF));

  const rejected = await jsonRequest(env, "/hot-reports/pdf", {
    id: HOT_REPORT_ID,
    password: "wrong-password",
  });
  assert.equal(rejected.response.status, 401);
  assert.equal(rejected.data.error, "Password is incorrect.");
});


function seedMember(bucket, name) {
  const user = {
    id: `${name}-id`,
    username: name,
    email: `${name}@example.invalid`,
    password_salt: "test-salt",
    password_hash: `hmac_sha256$${"a".repeat(64)}`,
    email_is_generated: false,
    created_at: "2026-01-01T00:00:00.000Z",
    updated_at: "2026-01-01T00:00:00.000Z",
  };
  for (const field of ["id", "username", "email"]) {
    bucket.seed(`_account/users/${field}/${encodeURIComponent(user[field])}`, user);
  }
  return user;
}

function memberHeaders(user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user", sub: user.id, username: user.username, email: user.email,
    session_epoch: "", iat: now, exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", PASSWORD_SECRET)
    .update(`portal:account-token:v1:${body}`).digest("base64url");
  return { authorization: `Bearer ${body}.${signature}` };
}

function seedMemberAccess(bucket, user, kind, overrides = {}) {
  const row = {
    id: `${user.id}-${kind}`,
    email: user.email,
    access_mode: "all",
    status: "active",
    lifetime: false,
    // A paid month remains eligible until expiry, even with less than a day left.
    current_period_end: new Date(Date.now() + 3600_000).toISOString(),
    duration_value: "1",
    download_limit: 0,
    download_count: 0,
    download_items: [],
    institutions: [],
    industries: [],
    page_ranges: [],
    plan: "annual",
    source_plan_code: kind === "entitlements" ? "NOVA-M" : "",
    created_at: "2026-01-01T00:00:00.000Z",
    updated_at: "2026-01-01T00:00:00.000Z",
    ...overrides,
  };
  bucket.seed(`_account/${kind}/${encodeURIComponent(user.email)}`, row);
}

for (const scenario of [
  { name: "administrator one-month all-site membership", kind: "access", allowed: true, months: 1 },
  { name: "NOVA-M membership", kind: "entitlements", allowed: true, months: 1 },
  { name: "NOVA-Q membership", kind: "entitlements", overrides: { source_plan_code: "NOVA-Q" }, allowed: true, months: 3 },
  { name: "expired monthly membership", kind: "entitlements", overrides: { current_period_end: "2020-01-01T00:00:00.000Z" }, allowed: false },
  { name: "three-day trial", kind: "vid2ppt_trial", overrides: { duration_value: "trial_3d", source_plan_code: "NOVA-3D", download_limit: 10 }, allowed: false },
  { name: "filtered administrator membership", kind: "access", overrides: { access_mode: "filters", institutions: ["Bern"] }, allowed: false },
]) {
  test(`hot report access and PDF agree for ${scenario.name}`, async () => {
    const bucket = new MemoryR2();
    seedHotReport(bucket);
    const user = seedMember(bucket, `member-${scenario.kind}`);
    seedMemberAccess(bucket, user, scenario.kind, scenario.overrides);
    const env = envFor(bucket);
    const headers = memberHeaders(user);
    const access = await worker.fetch(new Request(
      `https://worker.test/hot-reports/access?report_id=${encodeURIComponent(HOT_REPORT_ID)}`,
      { headers },
    ), env, { waitUntil() {} });
    assert.equal(access.status, 200);
    const payload = await access.json();
    assert.equal(payload.can_download, scenario.allowed);
    assert.equal(payload.required_months, 1);
    assert.equal(payload.required_plan, "1个月及以上全站会员");
    if (scenario.allowed) assert.equal(payload.qualifying_months, scenario.months);

    const download = await worker.fetch(new Request("https://worker.test/hot-reports/pdf", {
      method: "POST",
      headers: { "content-type": "application/json", ...headers },
      body: JSON.stringify({ id: HOT_REPORT_ID }),
    }), env, { waitUntil() {} });
    if (scenario.allowed) {
      assert.equal(download.status, 200);
      assert.equal(download.headers.get("content-type"), "application/pdf");
      assert.deepEqual(new Uint8Array(await download.arrayBuffer()), HOT_REPORT_PDF);
    } else {
      assert.equal(download.status, 402);
      const denial = await download.json();
      assert.equal(denial.required_months, 1);
      assert.equal(denial.required_plan, "1个月及以上全站会员");
    }
  });
}

test("hot report metadata replaces a persisted three-month requirement with the current membership policy", async () => {
  const bucket = new MemoryR2();
  seedHotReport(bucket);
  const oldItem = JSON.parse(bucket.data.get(HOT_REPORT_ITEM_KEY));
  oldItem.required_plan = "3个月会员";
  oldItem.required_months = 3;
  bucket.seed(HOT_REPORT_ITEM_KEY, oldItem);
  bucket.seed("_hot-reports/indexes/public-v2.json", {
    version: 2,
    generation: "0123456789abcdef",
    stale_marker: "",
    updated_at: "2026-08-04T01:34:09.548Z",
    items: [oldItem],
  });
  const env = envFor(bucket);
  const itemResponse = await worker.fetch(new Request(
    `https://worker.test/hot-reports/item?id=${encodeURIComponent(HOT_REPORT_ID)}`,
  ), env, { waitUntil() {} });
  assert.equal(itemResponse.status, 200);
  const { item } = await itemResponse.json();
  assert.equal(item.required_months, 1);
  assert.equal(item.required_plan, "1个月及以上全站会员");

  const listResponse = await worker.fetch(new Request(
    "https://worker.test/hot-reports?limit=24",
    { headers: { "cache-control": "no-cache" } },
  ), env, { waitUntil() {} });
  assert.equal(listResponse.status, 200);
  const list = await listResponse.json();
  assert.equal(list.required_months, 1);
  assert.equal(list.required_plan, "1个月及以上全站会员");
  assert.equal(list.items[0].required_months, 1);
  assert.equal(list.items[0].required_plan, "1个月及以上全站会员");
});
