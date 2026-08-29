import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

const AUTH_SECRET = "admin-pdf-intake-test-secret";
const STATIC_PREFIX = "edge-static/runtime-data";
const ADMIN = Object.freeze({
  id: "admin-pdf-id",
  username: "admin-a",
  email: "admin-a@users.portal.example.invalid",
});

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.version = 0;
    this.failPutPrefixOnce = "";
    this.failCompletedStatusWrites = 0;
    this.holdListPrefix = "";
    this.listGate = null;
    this.releaseList = null;
    this.getKeys = [];
    this.listCalls = [];
  }

  async seed(key, value, options = {}) {
    return this.put(key, typeof value === "string" ? value : JSON.stringify(value), options);
  }

  holdList(prefix) {
    this.holdListPrefix = prefix;
    this.listGate = new Promise((resolve) => { this.releaseList = resolve; });
  }

  releaseHeldList() {
    if (this.releaseList) this.releaseList();
    this.holdListPrefix = "";
    this.listGate = null;
    this.releaseList = null;
  }

  async bytes(value) {
    if (value instanceof Uint8Array) return value.slice();
    if (value instanceof ArrayBuffer) return new Uint8Array(value.slice(0));
    if (value && typeof value.arrayBuffer === "function") {
      return new Uint8Array(await value.arrayBuffer());
    }
    return new TextEncoder().encode(String(value));
  }

  object(key, row, includeBody = true) {
    if (!row) return null;
    const bytes = row.bytes.slice();
    return {
      key,
      etag: row.etag,
      size: bytes.byteLength,
      uploaded: row.uploaded,
      customMetadata: { ...row.customMetadata },
      httpMetadata: { ...row.httpMetadata },
      ...(includeBody ? { body: bytes } : {}),
      async arrayBuffer() {
        return bytes.buffer.slice(bytes.byteOffset, bytes.byteOffset + bytes.byteLength);
      },
      async text() { return new TextDecoder().decode(bytes); },
      async json() { return JSON.parse(new TextDecoder().decode(bytes)); },
    };
  }

  async get(key) {
    this.getKeys.push(key);
    return this.object(key, this.rows.get(key), true);
  }

  async head(key) {
    return this.object(key, this.rows.get(key), false);
  }

  async put(key, value, options = {}) {
    if (this.failPutPrefixOnce && key.startsWith(this.failPutPrefixOnce)) {
      this.failPutPrefixOnce = "";
      throw new Error("injected R2 write failure");
    }
    if (
      this.failCompletedStatusWrites > 0
      && key.startsWith("_admin-uploads/v1/items/")
      && typeof value === "string"
    ) {
      let status = "";
      try { status = String(JSON.parse(value).status || ""); } catch (_error) { status = ""; }
      if (status === "completed") {
        this.failCompletedStatusWrites -= 1;
        throw new Error("injected completed status write failure");
      }
    }
    const condition = options.onlyIf || {};
    const bytes = await this.bytes(value);
    const current = this.rows.get(key);
    if (condition.etagDoesNotMatch === "*" && current) return null;
    if (condition.etagMatches && (!current || current.etag !== String(condition.etagMatches))) return null;
    this.version += 1;
    const row = {
      bytes,
      etag: `etag-${this.version}`,
      uploaded: new Date(),
      customMetadata: { ...(options.customMetadata || {}) },
      httpMetadata: { ...(options.httpMetadata || {}) },
    };
    this.rows.set(key, row);
    return this.object(key, row, false);
  }

  async delete(key) {
    this.rows.delete(key);
  }

  async list(options = {}) {
    const prefix = String(options.prefix || "");
    this.listCalls.push({ prefix, cursor: String(options.cursor || ""), limit: Number(options.limit || 0) });
    if (this.holdListPrefix && prefix === this.holdListPrefix && this.listGate) await this.listGate;
    const all = [...this.rows.entries()]
      .filter(([key]) => key.startsWith(prefix))
      .sort(([left], [right]) => left.localeCompare(right));
    const offset = Math.max(0, Number.parseInt(String(options.cursor || "0"), 10) || 0);
    const limit = Math.max(1, Math.min(1000, Math.floor(Number(options.limit) || 1000)));
    const page = all.slice(offset, offset + limit);
    const nextOffset = offset + page.length;
    return {
      objects: page.map(([key, row]) => this.object(key, row, false)),
      truncated: nextOffset < all.length,
      cursor: nextOffset < all.length ? String(nextOffset) : undefined,
    };
  }

  json(key) {
    const row = this.rows.get(key);
    return row ? JSON.parse(new TextDecoder().decode(row.bytes)) : null;
  }

  keys(prefix = "") {
    return [...this.rows.keys()].filter((key) => key.startsWith(prefix)).sort();
  }
}

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

function contactTargetKey(source, originId) {
  const digest = createHash("sha256")
    .update(`portal-contact-report:v1:${source}:${originId}`)
    .digest("hex");
  return `_contact-reports/v1/targets/${digest}.json`;
}

async function seedUser(bucket, identity) {
  const now = "2026-08-27T00:00:00.000Z";
  const user = {
    ...identity,
    password_salt: `${identity.id}-salt`,
    password_hash: `hmac_sha256$${"a".repeat(64)}`,
    email_is_generated: false,
    site_origin: "portal",
    registered_site: "portal",
    source_site: "portal",
    created_at: now,
    updated_at: now,
    last_login_at: "",
  };
  for (const [field, value] of [["id", user.id], ["username", user.username], ["email", user.email]]) {
    await bucket.seed(accountKey("users", field, value), user);
  }
  return user;
}

function userToken(user) {
  const now = Math.floor(Date.now() / 1000);
  return signedAccountToken({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    session_epoch: "",
    iat: now,
    exp: now + 3600,
  });
}

function signedAccountToken(payload) {
  const body = Buffer.from(JSON.stringify(payload)).toString("base64url");
  const signature = createHmac("sha256", AUTH_SECRET)
    .update(`portal:account-token:v1:${body}`)
    .digest("base64url");
  return `${body}.${signature}`;
}

function contactTargetToken(source, originId) {
  const now = Math.floor(Date.now() / 1000);
  return signedAccountToken({
    kind: "contact-report-target",
    source,
    origin_id: originId,
    iat: now,
    exp: now + 3600,
  });
}

function envFor(bucket, overrides = {}) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    AUTH_SECRET,
    PASSWORD_SECRET: "admin-pdf-password-secret",
    CATALOG_URL: "https://static.example.invalid/catalog.json",
    STATIC_DATA_PREFIX: STATIC_PREFIX,
    ALLOWED_ORIGIN: "https://portal.example.invalid",
    ...overrides,
  };
}

function authHeaders(token, extra = {}) {
  return { authorization: `Bearer ${token}`, ...extra };
}

function pdfFile(name = "report.pdf", text = "%PDF-1.7\nfixture") {
  return new File([new TextEncoder().encode(text)], name, { type: "application/pdf", lastModified: 1_777_777_777_000 });
}

function uploadForm(fields = {}) {
  const form = new FormData();
  for (const [key, value] of Object.entries(fields)) {
    if (value !== undefined && value !== null) form.set(key, value);
  }
  return form;
}

async function request(env, pathname, options = {}, ctx = { waitUntil() {} }) {
  const response = await worker.fetch(new Request(`https://worker.example.invalid${pathname}`, options), env, ctx);
  const contentType = response.headers.get("content-type") || "";
  const data = contentType.includes("json") ? await response.json() : null;
  return { response, data };
}

async function upload(env, pathname, token, uploadId, fingerprint, fields, ctx) {
  return request(env, pathname, {
    method: "POST",
    headers: authHeaders(token, {
      "x-upload-id": uploadId,
      "x-upload-fingerprint": fingerprint,
    }),
    body: uploadForm({ upload_id: uploadId, upload_fingerprint: fingerprint, ...fields }),
  }, ctx);
}

const UPLOAD_A = "123e4567-e89b-42d3-a456-426614174000";
const UPLOAD_B = "123e4567-e89b-42d3-a456-426614174001";
const UPLOAD_C = "123e4567-e89b-42d3-a456-426614174002";
const UPLOAD_D = "123e4567-e89b-42d3-a456-426614174003";
const UPLOAD_E = "123e4567-e89b-42d3-a456-426614174004";
const UPLOAD_F = "123e4567-e89b-42d3-a456-426614174005";
const UPLOAD_G = "123e4567-e89b-42d3-a456-426614174006";
const UPLOAD_H = "123e4567-e89b-42d3-a456-426614174007";
const UPLOAD_I = "123e4567-e89b-42d3-a456-426614174008";
const UPLOAD_J = "123e4567-e89b-42d3-a456-426614174009";
const FINGERPRINT_A = "a".repeat(64);
const FINGERPRINT_B = "b".repeat(64);
const FINGERPRINT_C = "c".repeat(64);

test("hot upload returns before slow retention, records status, and deduplicates by fingerprint", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const env = envFor(bucket, {
    HOT_REPORT_CLEANUP_ENABLED: "true",
    HOT_REPORT_STORAGE_LIMIT_BYTES: 1,
  });
  const waits = [];
  bucket.holdList("_hot-reports/pdfs/");

  const responsePromise = upload(env, "/account-admin/hot-report", token, UPLOAD_A, FINGERPRINT_A, {
    title: "Slow retention must not block",
    title_cn: "后台清理不阻塞上传",
    pdf: pdfFile("slow-retention.pdf"),
  }, { waitUntil(promise) { waits.push(promise); } });
  const fast = await Promise.race([
    responsePromise,
    new Promise((resolve) => setTimeout(() => resolve(null), 250)),
  ]);
  assert.ok(fast, "the core upload response must not wait for retention");
  assert.equal(fast.response.status, 201);
  assert.equal(fast.data.upload.status, "completed");
  assert.equal(fast.data.retention_cleanup_pending, true);
  assert.equal(waits.length, 1, "maintenance must be attached to waitUntil once");

  const status = await request(env, `/account-admin/upload-status?upload_id=${UPLOAD_A}`, {
    headers: authHeaders(token),
  });
  assert.equal(status.response.status, 200);
  assert.equal(status.data.upload.status, "completed");
  assert.equal(status.data.upload.kind, "hot-report");

  const hidden = await request(env, `/account-admin/upload-status?upload_id=${UPLOAD_A}`);
  assert.equal(hidden.response.status, 403, "upload status is administrator-only");

  const duplicate = await upload(env, "/account-admin/hot-report", token, UPLOAD_A, FINGERPRINT_A, {
    title: "Slow retention must not block",
    pdf: pdfFile("slow-retention.pdf"),
  });
  assert.equal(duplicate.response.status, 200);
  assert.equal(duplicate.data.deduplicated, true);

  const conflict = await upload(env, "/account-admin/hot-report", token, UPLOAD_A, FINGERPRINT_B, {
    title: "Different payload",
    pdf: pdfFile("different.pdf"),
  });
  assert.equal(conflict.response.status, 409, "one upload id cannot identify two payloads");

  const invalid = await upload(env, "/account-admin/hot-report", token, "short-id", FINGERPRINT_A, {
    title: "Invalid id",
    pdf: pdfFile("invalid.pdf"),
  });
  assert.equal(invalid.response.status, 400, "upload ids must be high entropy");

  bucket.releaseHeldList();
  await Promise.all(waits);
});

test("a committed upload reconciles to completed when the final status write is lost", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const env = envFor(bucket);
  const waits = [];
  bucket.failCompletedStatusWrites = 1;

  const created = await upload(env, "/account-admin/hot-report", token, UPLOAD_E, FINGERPRINT_C, {
    title: "Committed before status acknowledgement",
    pdf: pdfFile("status-reconcile.pdf", "%PDF-1.7\ncommitted-core"),
  }, { waitUntil(promise) { waits.push(promise); } });
  assert.equal(created.response.status, 201, "a lost status acknowledgement must not turn a committed PDF into a failed upload");
  assert.equal(created.data.upload.status, "completed");
  assert.equal(created.data.upload.result.item.id, created.data.item.id);

  await Promise.all(waits);
  const status = await request(env, `/account-admin/upload-status?upload_id=${UPLOAD_E}`, {
    headers: authHeaders(token),
  });
  assert.equal(status.response.status, 200);
  assert.equal(status.data.upload.status, "completed");
  assert.equal(status.data.upload.result.item.id, created.data.item.id);

  const replay = await upload(env, "/account-admin/hot-report", token, UPLOAD_E, FINGERPRINT_C, {
    title: "Committed before status acknowledgement",
    pdf: pdfFile("status-reconcile.pdf", "%PDF-1.7\ncommitted-core"),
  });
  assert.equal(replay.response.status, 200);
  assert.equal(replay.data.deduplicated, true);
  assert.equal(replay.data.upload.status, "completed");
});

test("stale active upload leases become retryable failures and old terminal records are cleaned", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const env = envFor(bucket);
  const staleAt = new Date(Date.now() - 31 * 60 * 1000).toISOString();
  const oldAt = new Date(Date.now() - 31 * 86400_000).toISOString();
  await bucket.seed(`_admin-uploads/v1/items/${UPLOAD_A}.json`, {
    version: 1,
    upload_id: UPLOAD_A,
    kind: "hot-report",
    status: "uploading",
    stage: "uploading",
    owner: "stale-owner",
    fingerprint: FINGERPRINT_A,
    created_at: staleAt,
    updated_at: staleAt,
    completed_at: "",
    failed_at: "",
  });
  await bucket.seed(`_admin-uploads/v1/items/${UPLOAD_B}.json`, {
    version: 1,
    upload_id: UPLOAD_B,
    kind: "contact-report",
    status: "completed",
    stage: "completed",
    owner: "old-owner",
    fingerprint: FINGERPRINT_B,
    created_at: oldAt,
    updated_at: oldAt,
    completed_at: oldAt,
    failed_at: "",
    result: { item: { id: "old" } },
  });

  const status = await request(env, `/account-admin/upload-status?upload_id=${UPLOAD_A}`, {
    headers: authHeaders(token),
  });
  assert.equal(status.response.status, 200);
  assert.equal(status.data.upload.status, "failed");
  assert.match(status.data.upload.detail, /长时间未更新/u);

  const maintenance = await worker.__adminPdfIntakeTest.maintainAdminUploadRecords(env);
  assert.ok(maintenance.scanned_count >= 2);
  assert.equal(await bucket.head(`_admin-uploads/v1/items/${UPLOAD_B}.json`), null);
  assert.equal(bucket.json(`_admin-uploads/v1/items/${UPLOAD_A}.json`).status, "failed");
});

test("contact-only upload binds a request, exposes availability, enforces three-month access, and never overwrites", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const env = envFor(bucket);
  const requestId = "c".repeat(64);
  const originId = `report-a:${"e".repeat(24)}`;
  await bucket.seed(`_report-requests/v1/items/${requestId}.json`, {
    version: 1,
    report_id: originId,
    source: "report-a",
    title: "Market Outlook 2026",
    institution: "Example Research",
    requester_email: "reader@example.net",
    status: "sent",
    target_verified: true,
    target_verified_at: "2026-08-27T01:00:00.000Z",
    attempted_at: "2026-08-27T01:00:00.000Z",
    updated_at: "2026-08-27T01:00:00.000Z",
  });

  const created = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_B, FINGERPRINT_A, {
    source: "report-a",
    origin_id: originId,
    title: "Market Outlook 2026",
    institution: "Example Research",
    date: "2026-08-27",
    request_id: requestId,
    pdf: pdfFile("market-outlook.pdf"),
  });
  assert.equal(created.response.status, 201);
  assert.equal(created.data.item.available, true);
  assert.equal(bucket.json(`_report-requests/v1/items/${requestId}.json`).fulfillment_status, "available");

  const queue = await request(env, "/account-admin/report-requests?source=report-a", {
    headers: authHeaders(token),
  });
  assert.equal(queue.response.status, 200);
  assert.equal(queue.data.items[0].request_id, requestId);
  assert.equal(queue.data.items[0].available, true);

  const publicItem = await request(env, `/contact-report/item?source=report-a&id=${encodeURIComponent(originId)}`);
  assert.equal(publicItem.response.status, 200);
  assert.equal(publicItem.data.item.availability, "available");
  assert.equal(publicItem.data.item.available, true);
  assert.equal(Object.hasOwn(publicItem.data.item, "object_key"), false);

  const conflictingProof = await worker.__reportRequestTest.createContactReportTargetToken(
    env,
    "report-a",
    originId,
    {
      id: originId,
      source: "report-a",
      title: "New signed but conflicting search title",
      institution: "Conflicting Search Institution",
      date: "2026-08-28",
      page_count: 99,
    },
  );
  const bindingWins = await request(
    env,
    `/contact-report/item?source=report-a&id=${encodeURIComponent(originId)}&request_token=${encodeURIComponent(conflictingProof)}`,
  );
  assert.equal(bindingWins.response.status, 200);
  assert.equal(bindingWins.data.item.title, "Market Outlook 2026", "an uploaded binding remains canonical over token claims");
  assert.equal(bindingWins.data.item.institution, "Example Research");
  assert.equal(bucket.keys("_contact-reports/v1/targets/").length, 0);

  const anonymous = await request(env, `/contact-report/pdf?source=report-a&id=${encodeURIComponent(originId)}`);
  assert.equal(anonymous.response.status, 401);

  const monthly = await seedUser(bucket, {
    id: "monthly-id",
    username: "monthly-user",
    email: "monthly@example.invalid",
  });
  await bucket.seed(accountKey("entitlements", monthly.email), {
    id: "monthly-entitlement",
    email: monthly.email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 86400_000).toISOString(),
    source_plan_code: "NOVA-M",
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const monthlyPdf = await request(env, `/contact-report/pdf?source=report-a&id=${encodeURIComponent(originId)}`, {
    headers: authHeaders(userToken(monthly)),
  });
  assert.equal(monthlyPdf.response.status, 402);
  assert.equal(monthlyPdf.data.required_months, 3);
  const monthlyAccess = await request(
    env,
    `/entitlement?report_id=${encodeURIComponent(originId)}&source=report-a`,
    { headers: authHeaders(userToken(monthly)) },
  );
  assert.equal(monthlyAccess.response.status, 200);
  assert.equal(monthlyAccess.data.can_download, false);
  assert.equal(monthlyAccess.data.required_months, 3);

  const quarterly = await seedUser(bucket, {
    id: "quarterly-id",
    username: "quarterly-user",
    email: "quarterly@example.invalid",
  });
  await bucket.seed(accountKey("entitlements", quarterly.email), {
    id: "quarterly-entitlement",
    email: quarterly.email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 92 * 86400_000).toISOString(),
    source_plan_code: "NOVA-Q",
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const quarterlyPdf = await request(env, `/report-a/pdf?id=${encodeURIComponent(originId)}`, {
    headers: authHeaders(userToken(quarterly)),
  });
  assert.equal(quarterlyPdf.response.status, 200);
  assert.match(quarterlyPdf.response.headers.get("content-type") || "", /application\/pdf/u);
  const quarterlyAccess = await request(
    env,
    `/entitlement?report_id=${encodeURIComponent(originId)}&source=report-a`,
    { headers: authHeaders(userToken(quarterly)) },
  );
  assert.equal(quarterlyAccess.response.status, 200);
  assert.equal(quarterlyAccess.data.can_download, true);
  assert.equal(quarterlyAccess.data.required_months, 3);

  const pdfKeysBefore = bucket.keys("_contact-reports/v1/pdfs/");
  const overwrite = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_C, FINGERPRINT_B, {
    source: "report-a",
    origin_id: originId,
    title: "Attempted overwrite",
    target_token: contactTargetToken("report-a", originId),
    pdf: pdfFile("overwrite.pdf", "%PDF-1.7\ndifferent"),
  });
  assert.equal(overwrite.response.status, 409);
  assert.deepEqual(bucket.keys("_contact-reports/v1/pdfs/"), pdfKeysBefore);

  const invalid = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_D, FINGERPRINT_A, {
    source: "authority",
    origin_id: "invalid-authority-id",
    title: "Invalid authority target",
    pdf: pdfFile("invalid-authority.pdf"),
  });
  assert.equal(invalid.response.status, 400);
  assert.equal(invalid.data.upload.status, "failed");
});

test("Report A short upstream ids receive signed tokens and pass the request contract", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (url) => {
    if (String(url).startsWith("https://www.hibor.com.cn/")) {
      return new Response(`
        <table><tr><td>
          <div class="tab_divttl"><a href="/data/Ab_7.html" title="Short upstream identifier">Short upstream identifier</a></div>
          <span>分享时间：2026-08-27</span><span>页数：12</span>
        </td></tr></table>
      `, { status: 200, headers: { "content-type": "text/html; charset=utf-8" } });
    }
    throw new Error(`unexpected fetch: ${url}`);
  };
  try {
    const search = await request(env, "/report-a/search?q=Short&page=1");
    assert.equal(search.response.status, 200);
    assert.equal(search.data.items.length, 1);
    const item = search.data.items[0];
    assert.equal(item.id, "report-a:Ab_7");
    assert.ok(item.request_token);
    assert.equal(item.target_token, item.request_token);
    assert.equal(bucket.keys("_contact-reports/v1/targets/").length, 0, "search must only sign metadata claims");

    const arbitraryItem = await request(env, `/contact-report/item?source=report-a&id=${encodeURIComponent(item.id)}`);
    assert.equal(arbitraryItem.response.status, 404, "an unproven search row must not have been persisted");
    const provenItem = await request(
      env,
      `/contact-report/item?source=report-a&id=${encodeURIComponent(item.id)}&request_token=${encodeURIComponent(item.request_token)}`,
    );
    assert.equal(provenItem.response.status, 200);
    assert.equal(provenItem.data.item.title, item.title);
    assert.ok(provenItem.data.item.request_token);
    assert.equal(bucket.keys("_contact-reports/v1/targets/").length, 1, "opening one proven row persists exactly one target");

    const compactItem = await request(env, `/contact-report/item?source=report-a&id=${encodeURIComponent(item.id)}`);
    assert.equal(compactItem.response.status, 200, "the compact id-only URL works after the first detail preheats R2");
    assert.equal(compactItem.data.item.title, item.title);
    assert.equal(bucket.keys("_contact-reports/v1/targets/").length, 1);

    const missingProof = await request(env, "/report-request", {
      method: "POST",
      headers: { "content-type": "application/json", origin: "https://portal.example.invalid" },
      body: JSON.stringify({
        report_id: item.id,
        source: "report-a",
        title: item.title,
        requester_email: "short-id@example.net",
      }),
    });
    assert.equal(missingProof.response.status, 400);

    const acceptedProof = await request(env, "/report-request", {
      method: "POST",
      headers: { "content-type": "application/json", origin: "https://portal.example.invalid" },
      body: JSON.stringify({
        report_id: item.id,
        source: "report-a",
        title: item.title,
        requester_email: "short-id@example.net",
        request_token: item.request_token,
      }),
    });
    assert.equal(acceptedProof.response.status, 502, "the fixture has no email provider, after target validation the notification fails closed");
    const savedKey = bucket.keys("_report-requests/v1/items/")[0];
    assert.ok(savedKey);
    assert.equal(bucket.json(savedKey).report_id, item.id);
    assert.equal(bucket.json(savedKey).target_verified, true);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("search signs canonical metadata without any synchronous target R2 writes", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  bucket.failPutPrefixOnce = "_contact-reports/v1/targets/";
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async () => new Response(`
    <table><tr><td>
      <div class="tab_divttl"><a href="/data/fail_soft_7.html" title="Fail-soft metadata fixture">Fail-soft metadata fixture</a></div>
      <span>分享时间：2026-08-27</span><span>页数：12</span>
    </td></tr></table>
  `, { status: 200 });
  try {
    const search = await request(env, "/report-a/search?q=fail-soft&page=1");
    assert.equal(search.response.status, 200);
    assert.equal(search.data.items.length, 1);
    assert.equal(search.data.items[0].title, "Fail-soft metadata fixture");
    assert.ok(search.data.items[0].request_token);
    assert.equal(bucket.keys("_contact-reports/v1/targets/").length, 0);
    assert.equal(bucket.failPutPrefixOnce, "_contact-reports/v1/targets/", "search must not even attempt a target put");
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("contact upload rejects unsigned phantom targets, enforces quota, and repairs a stale missing-object binding", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const originId = `report-a:${"1".repeat(24)}`;
  const env = envFor(bucket);

  const unsigned = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_E, FINGERPRINT_A, {
    source: "report-a",
    origin_id: originId,
    title: "Unsigned phantom",
    pdf: pdfFile("unsigned.pdf"),
  });
  assert.equal(unsigned.response.status, 400);
  assert.match(unsigned.data.detail, /线索/u);
  assert.equal(bucket.keys("_contact-reports/v1/pdfs/").length, 0);

  const quota = await upload(
    envFor(bucket, { CONTACT_REPORT_STORAGE_LIMIT_BYTES: 6 }),
    "/account-admin/contact-report-pdf",
    token,
    UPLOAD_F,
    FINGERPRINT_B,
    {
      source: "report-a",
      origin_id: originId,
      title: "Quota fixture",
      target_token: contactTargetToken("report-a", originId),
      pdf: pdfFile("quota.pdf"),
    },
  );
  assert.equal(quota.response.status, 507);
  assert.equal(quota.data.storage.limit_bytes, 6);
  assert.equal(bucket.keys("_contact-reports/v1/pdfs/").length, 0);

  const first = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_G, FINGERPRINT_A, {
    source: "report-a",
    origin_id: originId,
    title: "Stale binding repair",
    target_token: contactTargetToken("report-a", originId),
    pdf: pdfFile("first.pdf", "%PDF-1.7\nfirst-contact"),
  });
  assert.equal(first.response.status, 201);
  const pdfKey = bucket.keys("_contact-reports/v1/pdfs/")[0];
  const bindingKey = bucket.keys("_contact-reports/v1/items/")[0];
  const firstBindingEtag = bucket.rows.get(bindingKey).etag;
  await bucket.delete(pdfKey);

  const repaired = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_H, FINGERPRINT_C, {
    source: "report-a",
    origin_id: originId,
    title: "Stale binding repair",
    target_token: contactTargetToken("report-a", originId),
    pdf: pdfFile("second.pdf", "%PDF-1.7\nsecond-contact"),
  });
  assert.equal(repaired.response.status, 201, "a missing object behind stale metadata must be replaceable under its metadata ETag");
  assert.equal(bucket.json(bindingKey).upload_id, UPLOAD_H);
  assert.notEqual(bucket.rows.get(bindingKey).etag, firstBindingEtag);
  assert.equal(await (await bucket.get(pdfKey)).text(), "%PDF-1.7\nsecond-contact");

  await bucket.seed(bindingKey, { ...bucket.json(bindingKey), etag: "stale-object-etag" });
  const replacedOrphan = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_I, FINGERPRINT_B, {
    source: "report-a",
    origin_id: originId,
    title: "Replace inactive orphan",
    target_token: contactTargetToken("report-a", originId),
    pdf: pdfFile("third.pdf", "%PDF-1.7\nthird-contact"),
  });
  assert.equal(replacedOrphan.response.status, 201, "an object owned by a completed non-active upload must not lock stale metadata");
  assert.equal(await (await bucket.get(pdfKey)).text(), "%PDF-1.7\nthird-contact");
  assert.equal(bucket.json(bindingKey).upload_id, UPLOAD_I);
});

test("contact upload rolls back an unbound PDF after metadata failure", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const env = envFor(bucket);
  const requestId = "d".repeat(64);
  const originId = `report-a:${"f".repeat(24)}`;
  await bucket.seed(`_report-requests/v1/items/${requestId}.json`, {
    version: 1,
    report_id: originId,
    source: "report-a",
    title: "Rollback fixture",
    requester_email: "reader@example.net",
    status: "sent",
    target_verified: true,
    attempted_at: "2026-08-27T01:00:00.000Z",
    updated_at: "2026-08-27T01:00:00.000Z",
  });
  bucket.failPutPrefixOnce = "_contact-reports/v1/items/";
  const result = await upload(env, "/account-admin/contact-report-pdf", userToken(admin), UPLOAD_A, FINGERPRINT_A, {
    source: "report-a",
    origin_id: originId,
    title: "Rollback fixture",
    request_id: requestId,
    pdf: pdfFile("rollback.pdf"),
  });
  assert.equal(result.response.status, 503);
  assert.equal(result.data.upload.status, "failed");
  assert.equal(bucket.keys("_contact-reports/v1/pdfs/").length, 0, "an unbound object must be removed");
  assert.equal(bucket.keys("_contact-reports/v1/items/").length, 0);
});

test("a contact binding remains successful when its public index write fails and is repaired", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const env = envFor(bucket);
  const originId = "report-a:idx_7";
  const waits = [];
  bucket.failPutPrefixOnce = "_contact-reports/v1/index.json";
  const created = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_J, FINGERPRINT_C, {
    source: "report-a",
    origin_id: originId,
    title: "Index repair fixture",
    target_token: contactTargetToken("report-a", originId),
    pdf: pdfFile("index-repair.pdf"),
  }, { waitUntil(promise) { waits.push(promise); } });
  assert.equal(created.response.status, 201);
  assert.equal(created.data.index_update_pending, true);
  assert.equal(created.data.upload.status, "completed");
  await Promise.all(waits);
  assert.ok(bucket.json("_contact-reports/v1/index.json").items.some((item) => item.origin_id === originId));
  assert.equal(bucket.keys("_contact-reports/v1/index-dirty/").length, 0);
});

test("report request index failures leave a repair marker and recover incrementally", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originId = "report-a:r7";
  await bucket.seed(contactTargetKey("report-a", originId), {
    version: 1,
    id: originId,
    origin_id: originId,
    source: "report-a",
    title: "Dirty queue fixture",
    institution: "Fixture Research",
    date: "2026-08-27",
    page_count: 7,
    file_type: "pdf",
    verified_at: "2026-08-27T00:00:00.000Z",
  });
  bucket.failPutPrefixOnce = "_report-requests/v1/admin-index.json";
  const submitted = await request(env, "/report-request", {
    method: "POST",
    headers: { "content-type": "application/json", origin: "https://portal.example.invalid" },
    body: JSON.stringify({
      report_id: originId,
      source: "report-a",
      title: "Dirty queue fixture",
      requester_email: "dirty-queue@example.net",
      request_token: contactTargetToken("report-a", originId),
    }),
  });
  assert.equal(submitted.response.status, 502);
  assert.equal(bucket.keys("_report-requests/v1/index-dirty/").length, 1);

  const repaired = await worker.__adminPdfIntakeTest.repairReportRequestAdminIndexIfNeeded(env);
  assert.ok(repaired.items.some((item) => item.report_id === originId));
  assert.equal(repaired.migration_complete, true);
  assert.equal(bucket.keys("_report-requests/v1/index-dirty/").length, 0);
});

test("contact storage accounting fails closed when its bounded full scan is truncated", async () => {
  const calls = [];
  const bucket = {
    async list(options = {}) {
      const offset = Number(options.cursor || 0);
      calls.push(offset);
      return {
        objects: Array.from({ length: 1000 }, (_unused, index) => ({
          key: `_contact-reports/v1/pdfs/${String(offset + index).padStart(64, "0")}.pdf`,
          size: 10,
        })),
        truncated: true,
        cursor: String(offset + 1000),
      };
    },
  };
  const stats = await worker.__adminPdfIntakeTest.contactReportStorageStats({ REPORT_BUCKET: bucket });
  assert.equal(stats.item_count, 5000);
  assert.equal(stats.scan_complete, false);
  assert.equal(stats.truncated, true);
  assert.deepEqual(calls, [0, 1000, 2000, 3000, 4000]);
});

test("admin request queue is cursor-paged from its compact index and migrates a legacy row on upload", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const rows = Array.from({ length: 125 }, (_unused, index) => {
    const requestId = index.toString(16).padStart(64, "0");
    const reportId = `report-a:${index.toString(16).padStart(24, "0")}`;
    return {
      request_id: requestId,
      report_id: reportId,
      source: "report-a",
      title: `Queue fixture ${index}`,
      institution: "Queue Research",
      requester_email: `reader-${index}@example.net`,
      status: "sent",
      attempted_at: new Date(Date.UTC(2026, 7, 27, 0, 0, index)).toISOString(),
      updated_at: new Date(Date.UTC(2026, 7, 27, 0, 0, index)).toISOString(),
      target_verified: index !== 124,
    };
  });
  await bucket.seed("_report-requests/v1/admin-index.json", {
    version: 1,
    updated_at: "2026-08-27T02:30:00.000Z",
    migration_complete: true,
    migration_truncated: false,
    items: rows,
  });
  const legacy = rows[124];
  await bucket.seed(`_report-requests/v1/items/${legacy.request_id}.json`, {
    ...legacy,
    version: 1,
  });
  const env = envFor(bucket);
  bucket.getKeys = [];

  const first = await request(env, "/account-admin/report-requests?limit=40", {
    headers: authHeaders(token),
  });
  assert.equal(first.response.status, 200);
  assert.equal(first.data.items.length, 40);
  assert.equal(first.data.total, 125);
  assert.match(first.data.next_cursor, /^request:[A-Za-z0-9_-]+$/u);
  assert.notEqual(first.data.next_cursor, "request:40", "new cursors must use a stable row anchor rather than an offset");
  assert.equal(first.data.has_more, true);
  assert.equal(first.data.items[0].request_id, legacy.request_id);
  assert.equal(first.data.items[0].needs_verification, true);
  assert.ok(first.data.items[0].target_token, "legacy queue rows must carry an administrator verification token");
  assert.equal(
    bucket.getKeys.filter((key) => key.startsWith("_report-requests/v1/items/")).length,
    0,
    "a page read must not GET every request record",
  );
  assert.ok(
    bucket.getKeys.filter((key) => key.startsWith("_contact-reports/v1/items/")).length <= 40,
    "availability verification must be bounded to the current page",
  );

  const concurrentIndex = bucket.json("_report-requests/v1/admin-index.json");
  concurrentIndex.items.push({
    request_id: "f".repeat(64),
    report_id: "report-a:new_after_page_one",
    source: "report-a",
    title: "Inserted after page one",
    institution: "Queue Research",
    requester_email: "new@example.net",
    status: "sent",
    attempted_at: "2026-08-27T03:00:00.000Z",
    updated_at: "2026-08-27T03:00:00.000Z",
    target_verified: true,
  });
  await bucket.seed("_report-requests/v1/admin-index.json", concurrentIndex);

  const second = await request(env, `/account-admin/report-requests?limit=40&cursor=${encodeURIComponent(first.data.next_cursor)}`, {
    headers: authHeaders(token),
  });
  assert.equal(second.response.status, 200);
  assert.equal(second.data.items.length, 40);
  assert.match(second.data.next_cursor, /^request:[A-Za-z0-9_-]+$/u);
  const firstIds = new Set(first.data.items.map((item) => item.request_id));
  assert.equal(second.data.items.some((item) => firstIds.has(item.request_id)), false, "cursor pages must not repeat rows");

  const filtered = await request(env, "/account-admin/report-requests?q=fixture%20124&limit=10", {
    headers: authHeaders(token),
  });
  assert.equal(filtered.response.status, 200);
  assert.equal(filtered.data.total, 1, "q and limit must arrive in their correct queue arguments");
  assert.equal(filtered.data.items[0].request_id, legacy.request_id);

  const migrated = await upload(env, "/account-admin/contact-report-pdf", token, UPLOAD_A, FINGERPRINT_A, {
    source: legacy.source,
    origin_id: legacy.report_id,
    title: legacy.title,
    request_id: legacy.request_id,
    target_token: first.data.items[0].target_token,
    pdf: pdfFile("legacy-request.pdf"),
  });
  assert.equal(migrated.response.status, 201);
  const migratedRecord = bucket.json(`_report-requests/v1/items/${legacy.request_id}.json`);
  assert.equal(migratedRecord.target_verified, true);
  assert.equal(migratedRecord.target_verification_source, "admin-queue-token");
  assert.equal(migratedRecord.fulfillment_status, "available");
});

test("catalog intake includes text-only and missing PDFs, repairs missing objects, and refuses valid originals", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const textOnlyId = "a".repeat(24);
  const missingId = "b".repeat(24);
  const zeroByteId = "c".repeat(24);
  const availableId = "d".repeat(24);
  await bucket.seed(`${STATIC_PREFIX}/catalog.json`, {
    items: [
      { id: textOnlyId, title: "Report Text Only", filename: "text-only.pdf", available: false },
      { id: missingId, title: "Report Missing PDF", filename: "missing.pdf", available: true },
      { id: zeroByteId, title: "Report Zero Byte PDF", filename: "zero.pdf", available: true, size_bytes: 999999 },
      { id: availableId, title: "Report Available PDF", filename: "available.pdf", available: true },
    ],
  });
  await bucket.put(`reports/${zeroByteId}.pdf`, new Uint8Array());
  await bucket.put(`reports/${availableId}.pdf`, pdfFile("available.pdf"));
  const env = envFor(bucket);

  const search = await request(env, "/account-admin/pdf-intake-search?source=catalog&q=Report", {
    headers: authHeaders(token),
  });
  assert.equal(search.response.status, 200);
  const availability = new Map(search.data.items.map((item) => [item.id, item.availability]));
  assert.equal(availability.get(textOnlyId), "text_only");
  assert.equal(availability.get(missingId), "missing");
  assert.equal(availability.get(zeroByteId), "missing", "a zero-byte native object must not inherit a stale catalog size");
  assert.equal(availability.get(availableId), "available");

  const repaired = await upload(env, "/account-admin/text-only-pdf", token, UPLOAD_B, FINGERPRINT_A, {
    id: missingId,
    pdf: pdfFile("repaired.pdf"),
  });
  assert.equal(repaired.response.status, 201);
  assert.equal(repaired.data.repair_kind, "missing_pdf");
  assert.equal(repaired.data.upload.status, "completed");

  const validOriginal = await upload(env, "/account-admin/text-only-pdf", token, UPLOAD_C, FINGERPRINT_B, {
    id: availableId,
    pdf: pdfFile("must-not-overwrite.pdf"),
  });
  assert.equal(validOriginal.response.status, 409);
  assert.equal(validOriginal.data.upload.status, "failed");
  assert.ok(await bucket.head(`reports/${availableId}.pdf`), "the valid native object must remain in place");
});

test("text-only retry replaces the first attempt orphan with the second selected PDF", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const reportId = "9".repeat(24);
  await bucket.seed(`${STATIC_PREFIX}/catalog.json`, {
    items: [{ id: reportId, title: "Retry content identity", filename: "retry.pdf", available: false }],
  });
  const env = envFor(bucket);
  bucket.failPutPrefixOnce = "_catalog-pdf-overrides/items/";

  const first = await upload(env, "/account-admin/text-only-pdf", token, UPLOAD_F, FINGERPRINT_A, {
    id: reportId,
    pdf: pdfFile("first-selection.pdf", "%PDF-1.7\nFIRST-SELECTION"),
  });
  assert.equal(first.response.status, 503);
  const pdfKey = bucket.keys("_hot-reports/pdfs/")[0];
  assert.ok(pdfKey, "the first archive write is intentionally durable across a metadata failure");
  assert.equal(await (await bucket.get(pdfKey)).text(), "%PDF-1.7\nFIRST-SELECTION");

  const second = await upload(env, "/account-admin/text-only-pdf", token, UPLOAD_G, FINGERPRINT_B, {
    id: reportId,
    pdf: pdfFile("second-selection.pdf", "%PDF-1.7\nSECOND-SELECTION"),
  });
  assert.equal(second.response.status, 201);
  const finalPdf = await bucket.get(pdfKey);
  assert.equal(await finalPdf.text(), "%PDF-1.7\nSECOND-SELECTION");
  assert.equal(finalPdf.customMetadata.upload_id, UPLOAD_G);
  const override = bucket.json(`_catalog-pdf-overrides/items/${reportId}.json`);
  assert.equal(override.upload_id, UPLOAD_G);
  assert.equal(override.etag, finalPdf.etag);
});

test("two concurrent text-only uploads never bind one upload id to the other PDF", async () => {
  const bucket = new MemoryR2();
  const admin = await seedUser(bucket, ADMIN);
  const token = userToken(admin);
  const reportId = "8".repeat(24);
  await bucket.seed(`${STATIC_PREFIX}/catalog.json`, {
    items: [{ id: reportId, title: "Concurrent content identity", filename: "concurrent.pdf", available: false }],
  });
  const env = envFor(bucket);
  const [left, right] = await Promise.all([
    upload(env, "/account-admin/text-only-pdf", token, UPLOAD_I, FINGERPRINT_A, {
      id: reportId,
      pdf: pdfFile("left.pdf", "%PDF-1.7\nLEFT-CONTENT"),
    }),
    upload(env, "/account-admin/text-only-pdf", token, UPLOAD_J, FINGERPRINT_B, {
      id: reportId,
      pdf: pdfFile("right.pdf", "%PDF-1.7\nRIGHT-CONTENT"),
    }),
  ]);
  const successes = [left, right].filter((result) => result.response.status === 201);
  assert.equal(successes.length, 1, "exactly one concurrent metadata claim should win");
  const winner = successes[0] === left
    ? { uploadId: UPLOAD_I, content: "%PDF-1.7\nLEFT-CONTENT" }
    : { uploadId: UPLOAD_J, content: "%PDF-1.7\nRIGHT-CONTENT" };
  const override = bucket.json(`_catalog-pdf-overrides/items/${reportId}.json`);
  assert.equal(override.upload_id, winner.uploadId);
  const pdf = await bucket.get(override.object_key);
  assert.equal(pdf.customMetadata.upload_id, winner.uploadId);
  assert.equal(pdf.customMetadata.version, override.version);
  assert.equal(pdf.etag, override.etag);
  assert.equal(await pdf.text(), winner.content);
  const loser = successes[0] === left ? right : left;
  assert.ok([409, 503].includes(loser.response.status));
  assert.notEqual(loser.data.upload.status, "completed");
});
