import assert from "node:assert/strict";
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
