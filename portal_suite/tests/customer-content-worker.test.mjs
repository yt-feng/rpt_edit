import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";

// All accounts, content and credentials below are synthetic. Any network call
// fails the test; the real Worker router and auth/data adapters remain intact.
const SECRET = "synthetic-content-api-test-signing-key";
const ADMIN = { id: "content-admin", username: "admin-a", email: "admin-a@users.portal.example.invalid" };
const USER = { id: "content-reader", username: "content-reader", email: "content-reader@example.invalid" };
const REPORT = "a".repeat(24), IMAGE = "b".repeat(64);
const accountKey = (...parts) => ["_account", ...parts.map(value => encodeURIComponent(value))].join("/");
const digest = value => createHash("sha256").update(value).digest("hex");

class Bucket {
  rows = new Map(); serial = 0; reads = []; writes = [];
  seed(key, value) {
    const bytes = Buffer.isBuffer(value) ? value : Buffer.from(typeof value === "string" ? value : JSON.stringify(value));
    this.rows.set(key, { bytes, etag: `fixture-${++this.serial}` });
  }
  async get(key) {
    this.reads.push(key);
    const row = this.rows.get(key);
    if (!row) return null;
    return { etag: row.etag, size: row.bytes.length, body: new Response(row.bytes).body,
      text: async () => row.bytes.toString(), arrayBuffer: async () => Uint8Array.from(row.bytes).buffer };
  }
  async head(key) { const row = this.rows.get(key); return row ? { size: row.bytes.length, etag: row.etag } : null; }
  async put(key, raw, { onlyIf } = {}) {
    const previous = this.rows.get(key);
    if ((onlyIf?.etagMatches && previous?.etag !== onlyIf.etagMatches) || (onlyIf?.etagDoesNotMatch === "*" && previous)) return null;
    this.seed(key, String(raw)); this.writes.push({ key, raw }); return { etag: this.rows.get(key).etag };
  }
}
function token(user) {
  const time = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, iat: time, exp: time + 3600 })).toString("base64url");
  return `${body}.${createHmac("sha256", SECRET).update(`portal:account-token:v1:${body}`).digest("base64url")}`;
}
function seedUser(bucket, user) {
  for (const field of ["id", "username", "email"]) bucket.seed(accountKey("users", field, user[field]), { ...user, site_origin: "portal", disabled: false });
}
function setup(t) {
  t.mock.method(globalThis, "fetch", async () => { assert.fail("Content API fixture must never perform a network request"); });
  const bucket = new Bucket(); seedUser(bucket, ADMIN); seedUser(bucket, USER);
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [{ id: REPORT, title: "合成报告", title_en: "Synthetic report",
    filename: "fixture.pdf", date_folder: "261012", page_count: 2, available: true, private_path: "/private/no-export" }] });
  bucket.seed(`reports/${REPORT}.pdf`, "%PDF-synthetic-fixture");
  bucket.seed("_chart-search/v1/index.json", { reports: [{ report_id: REPORT, title: "合成报告", date_folder: "261012", charts: [{
    id: "chart-fixture", image_id: IMAGE, analysis_version: "chart-search-v2", content_kind: "chart", quality_score: 80,
    title: "Synthetic chart", description: "Synthetic chart description", provider_session: "DO_NOT_EXPORT_PROVIDER_SESSION",
  }] }] });
  bucket.seed(`_chart-search/v1/images/${IMAGE}.jpg`, Buffer.from([0xff, 0xd8, 0xff, 0xd9]));
  const artifacts = [];
  for (const [kind, language, content] of [["text", "zh", "合成中文文本。"], ["translation", "en", "Synthetic English translation."]]) {
    const sha = digest(content), key = `_customer-content-data/v1/blobs/${REPORT}/${sha}.txt`;
    bucket.seed(key, content);
    artifacts.push({ id: sha, report_id: REPORT, kind, language, mime_type: "text/plain", size: Buffer.byteLength(content),
      sha256: sha, object_key: key, filename: `${language}.txt`, text_scope: "full_text" });
  }
  bucket.seed(`_customer-content-data/v1/reports/${REPORT}/manifest.json`, { schema_version: 1, report_id: REPORT, artifacts });
  const env = { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", AUTH_SECRET: SECRET, CATALOG_URL: "https://synthetic.invalid/catalog.json" };
  const call = (path, bearer = token(USER), method = "GET", body) => worker.fetch(new Request(`https://kcdesk.com${path}`, {
    method, headers: { ...(bearer ? { authorization: `Bearer ${bearer}` } : {}), ...(body ? { "content-type": "application/json" } : {}) },
    ...(body ? { body: JSON.stringify(body) } : {}),
  }), env, { waitUntil() {} });
  const grant = (extra = {}) => call("/api/admin/content-api/grant", token(ADMIN), "POST", {
    email: USER.email, enabled: true, access_mode: "granted_corpus", report_ids: [REPORT],
    expires_at: new Date(Date.now() + 86400000).toISOString(), ...extra,
  });
  const key = async () => {
    const response = await call("/api/account/content-api/keys", token(USER), "POST", { name: "Synthetic integration" });
    assert.equal(response.status, 201, await response.clone().text()); return response.json();
  };
  return { bucket, call, grant, key, artifacts };
}

test("actual Worker: super grant -> session key creation -> bearer catalog/PDF/Chinese/English/chart delivery -> revoke", async t => {
  const f = setup(t);
  assert.equal((await f.call("/api/account/content-api", null)).status, 401);
  assert.equal((await f.call(`/api/admin/content-api/grant?email=${encodeURIComponent(USER.email)}`)).status, 403);
  assert.equal((await f.grant()).status, 200);
  const key = await f.key();
  const listed = await f.call("/api/content/v1/reports?date=2026-10-12&limit=1", key.secret);
  assert.equal(listed.status, 200, await listed.clone().text());
  const list = await listed.json(); assert.deepEqual(list.items.map(row => row.id), [REPORT]);
  assert.equal(list.items[0].source, "catalog"); assert.equal(list.items[0].pdf_listed, true);
  assert.equal(JSON.stringify(list).includes("private_path"), false);
  const pdf = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(pdf.status, 200, await pdf.clone().text()); assert.equal(await pdf.text(), "%PDF-synthetic-fixture");
  const artifactResponse = await f.call(`/api/content/v1/reports/${REPORT}/artifacts`, key.secret);
  assert.equal(artifactResponse.status, 200, await artifactResponse.clone().text());
  const artifacts = await artifactResponse.json();
  assert.equal(artifacts.items.some(row => row.kind === "translation" && row.language === "en"), true);
  assert.equal(artifacts.items.find(row => row.kind === "chart").size, null);
  assert.equal(JSON.stringify(artifacts).includes("object_key"), false);
  for (const row of f.artifacts) {
    const response = await f.call(`/api/content/v1/reports/${REPORT}/artifacts/${row.id}`, key.secret);
    assert.equal(response.status, 200); assert.equal(digest(await response.text()), row.sha256);
  }
  const metadata = await f.call(`/api/content/v1/reports/${REPORT}/artifacts/chart-meta-${IMAGE}`, key.secret);
  assert.equal(metadata.status, 200); const text = await metadata.text();
  assert.equal(text.includes("Synthetic chart"), true); assert.equal(text.includes("PROVIDER_SESSION"), false);
  const image = await f.call(`/api/content/v1/reports/${REPORT}/artifacts/chart-${IMAGE}`, key.secret);
  assert.equal(image.status, 200); assert.equal(image.headers.get("content-length"), "4"); await image.arrayBuffer();
  assert.equal((await f.call(`/api/account/content-api/keys/${key.key.id}`, token(USER), "DELETE")).status, 200);
  assert.equal((await f.call("/api/content/v1/reports", key.secret)).status, 401);
  assert.equal(f.bucket.writes.some(row => row.raw.includes(key.secret)), false);
  assert.equal(f.bucket.reads.some(path => path.startsWith("_workflow-cache/") || path.includes("/draft")), false);
});

test("actual Worker membership mode preserves current web entitlement and observes later revocation", async t => {
  const f = setup(t); await f.grant({ access_mode: "membership" }); const key = await f.key();
  const denied = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(denied.status, 404);
  f.bucket.seed(accountKey("entitlements", USER.email), { email: USER.email, status: "active", plan: "annual", lifetime: true, current_period_end: null });
  const allowed = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(allowed.status, 200, await allowed.clone().text()); await allowed.text();
  f.bucket.seed(accountKey("entitlements", USER.email), { email: USER.email, status: "canceled", plan: "annual", lifetime: false, current_period_end: null });
  assert.equal((await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret)).status, 404);
});

test("actual Worker denies private object locators, foreign report IDs, and account disable immediately", async t => {
  const f = setup(t); await f.grant(); const key = await f.key();
  assert.equal((await f.call(`/api/content/v1/reports/${"c".repeat(24)}/download`, key.secret)).status, 403);
  assert.equal((await f.call(`/api/content/v1/reports/${REPORT}/artifacts?object_key=_account/private`, key.secret)).status, 400);
  for (const [field, value] of [["id", USER.id], ["email", USER.email]]) f.bucket.seed(accountKey("user-state", field, value),
    { user_id: USER.id, email: USER.email, disabled: true });
  assert.equal((await f.call("/api/content/v1/reports", key.secret)).status, 403);
});

test("actual Worker honors a per-report purchase when bulk membership is absent", async t => {
  const f = setup(t); await f.grant({ access_mode: "membership" }); const key = await f.key();
  f.bucket.seed(accountKey("purchases", "catalog", REPORT, USER.email), {
    email: USER.email, report_id: REPORT, source: "catalog", status: "active",
  });
  const response = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(response.status, 200, await response.clone().text()); await response.text();
  const artifact = await f.call(`/api/content/v1/reports/${REPORT}/artifacts/${f.artifacts[0].id}`, key.secret);
  assert.equal(artifact.status, 200); await artifact.text();
});

test("actual Worker reserves API bytes before web trial count and deduplicates report derivatives", async t => {
  const f = setup(t); await f.grant({ access_mode: "membership", daily_bytes: 1 }); const key = await f.key();
  const accessPath = accountKey("access", USER.email);
  f.bucket.seed(accessPath, { id: "synthetic-trial", email: USER.email, access_mode: "all", status: "active", lifetime: false,
    current_period_end: new Date(Date.now() + 86400000).toISOString(), duration_value: "trial_3d", change_id: "synthetic-change",
    institutions: [], industries: [], page_ranges: [], download_limit: 10, download_count: 9,
    download_items: Array.from({ length: 9 }, (_, index) => `catalog:${String(index).repeat(24)}`) });
  const denied = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(denied.status, 429); assert.equal((await denied.json()).error, "daily_byte_limit");
  assert.equal(JSON.parse(f.bucket.rows.get(accessPath).bytes).download_count, 9);
  await f.grant({ access_mode: "membership", daily_bytes: 10000 });
  const text = await f.call(`/api/content/v1/reports/${REPORT}/artifacts/${f.artifacts[0].id}`, key.secret);
  assert.equal(text.status, 200, await text.clone().text()); await text.text();
  assert.equal(JSON.parse(f.bucket.rows.get(accessPath).bytes).download_count, 10);
  const pdf = await f.call(`/api/content/v1/reports/${REPORT}/download`, key.secret);
  assert.equal(pdf.status, 200, await pdf.clone().text()); await pdf.text();
  assert.equal(JSON.parse(f.bucket.rows.get(accessPath).bytes).download_count, 10);
});

test("actual Worker normalizes direct aliases and returns Response for unmatched content routes", async t => {
  const f = setup(t);
  assert.equal((await f.call("/account/content-api")).status, 200);
  const missing = await f.call("/api/content/v1/unknown", null);
  assert.equal(missing.status, 404); assert.equal((await missing.json()).error, "content_not_found");
});
