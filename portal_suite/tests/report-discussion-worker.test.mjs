import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";

const reportId = "a".repeat(24);
const hash = (text) => createHash("sha256").update(text).digest("hex");
const markerKey = `_report-discussions/v1/eligibility/${hash(`catalog:${reportId}`)}.json`;
const reportText = "报告认为新增订单是观察需求恢复的重要线索，库存下降还需要结合后续生产计划进行判断。企业成本变化与产品结构共同影响利润率。".repeat(5);
const answer = {
  body: "报告把订单变化与需求恢复联系起来，但库存下降未必意味着持续的需求扩张，还需要观察后续生产计划。你认为哪些订单或库存指标最能验证这项判断，是否有相反的证据？",
  evidence_quote: "报告认为新增订单是观察需求恢复的重要线索，库存下降还需要结合后续生产计划进行判断。",
};

class Bucket {
  data = new Map(); version = 0;
  seed(key, value) { this.data.set(key, { bytes: Buffer.from(typeof value === "string" ? value : JSON.stringify(value)), etag: String(++this.version) }); }
  async get(key) {
    const row = this.data.get(key);
    return row ? { etag: row.etag, size: row.bytes.length, text: async () => row.bytes.toString(), arrayBuffer: async () => Uint8Array.from(row.bytes).buffer } : null;
  }
  async put(key, value, options = {}) {
    const current = this.data.get(key), condition = options.onlyIf || {};
    if (condition.etagDoesNotMatch === "*" && current) return null;
    if (condition.etagMatches && current?.etag !== condition.etagMatches) return null;
    this.seed(key, value); return { etag: this.data.get(key).etag };
  }
}

function setup() {
  const bucket = new Bucket();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [{ id: reportId, title: "订单与企业盈利观察", bank_name: "Example Research", date_folder: "261025" }] });
  const env = { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", MASTER_KEY: "test-master", OPS_ALERT_SIGNING_KEY: "test-ops-secret", CATALOG_URL: "https://example.invalid/data/catalog.json", DEEPSEEK_API_KEY: "test-provider-key" };
  return { bucket, env };
}

function marker(overrides = {}) {
  return { version: 1, source: "catalog", report_id: reportId, activated_at: new Date(Date.now() - 60000).toISOString(), first_seen_at: new Date(Date.now() - 30000).toISOString(), ...overrides };
}

async function generate(env, { signed = true, timestamp = Math.floor(Date.now() / 1000), body = { source: "catalog", report_id: reportId } } = {}) {
  const raw = JSON.stringify(body), headers = { "Content-Type": "application/json" };
  if (signed) {
    headers["X-Portal-Timestamp"] = String(timestamp);
    headers["X-Portal-Signature"] = "sha256=" + createHmac("sha256", env.OPS_ALERT_SIGNING_KEY).update(`${timestamp}.${raw}`).digest("hex");
  }
  const response = await worker.fetch(new Request("https://example.invalid/api/ops/report-discussions/generate", { method: "POST", headers, body: raw }), env, { waitUntil() {} });
  return { status: response.status, body: await response.json() };
}

async function withFetch(callback, run) {
  const original = globalThis.fetch; globalThis.fetch = callback;
  try { return await run(); } finally { globalThis.fetch = original; }
}

function seedSource(bucket, options = {}) {
  const digest = hash(reportText), blobKey = `_customer-content-data/v1/blobs/${reportId}/${digest}.md`;
  bucket.seed(`_customer-content-data/v1/reports/${reportId}/manifest.json`, {
    schema_version: 1, report_id: reportId,
    artifacts: [{ id: digest, kind: "text", language: "und", filename: "source_clean.md", mime_type: "text/markdown", object_key: blobKey, sha256: digest, size: Buffer.byteLength(reportText) }],
  });
  bucket.seed(blobKey, options.corrupt ? reportText.replace("新增", "减少") : reportText);
}

test("generation endpoint rejects unsigned, stale and historical requests before using provider", async () => {
  const { env, bucket } = setup();
  await withFetch(async () => { throw new Error("must not call external provider"); }, async () => {
    assert.equal((await generate(env, { signed: false })).status, 403);
    assert.equal((await generate(env, { timestamp: Math.floor(Date.now() / 1000) - 3600 })).status, 403);
    assert.equal((await generate(env)).status, 403);
    const activated = new Date(Date.now() - 60000).toISOString();
    bucket.seed(markerKey, marker({ activated_at: activated, first_seen_at: activated }));
    assert.equal((await generate(env)).status, 403);
    bucket.seed(markerKey, marker({ report_id: "b".repeat(24) }));
    assert.equal((await generate(env)).status, 403);
    bucket.seed(markerKey, marker({ first_seen_at: new Date(Date.now() + 300000).toISOString() }));
    assert.equal((await generate(env)).status, 403);
    assert.equal((await generate(env, { body: { source: "hot", report_id: "hot:" + "a".repeat(16) } })).status, 400);
  });
  assert.equal([...bucket.data.keys()].some((key) => key.endsWith("/starter.json")), false);
});

test("public report API preserves historical comment positions without calling AI or exposing source text", async () => {
  const { env, bucket } = setup(); seedSource(bucket);
  await withFetch(async () => { throw new Error("public read must not generate"); }, async () => {
    const response = await worker.fetch(new Request(`https://example.invalid/api/report-discussion?source=catalog&report_id=${reportId}`), env, { waitUntil() {} });
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.starter, null); assert.deepEqual(body.comments, []);
    assert.equal(JSON.stringify(body).includes("source_clean"), false);
    assert.equal(JSON.stringify(body).includes(reportText.slice(0, 30)), false);
  });
});

test("signed new-report publication verifies stored text and produces one labeled discussion starter", async () => {
  const { env, bucket } = setup(); bucket.seed(markerKey, marker()); seedSource(bucket);
  let providerCalls = 0;
  await withFetch(async (url, options) => {
    assert.match(String(url), /^https:\/\/api\.deepseek\.com\/chat\/completions$/u);
    providerCalls += 1;
    const body = JSON.parse(options.body);
    assert.match(body.messages[1].content, /新增订单/u);
    return Response.json({ choices: [{ message: { content: JSON.stringify(answer) } }] });
  }, async () => {
    const generated = await generate(env);
    assert.equal(generated.status, 200);
    assert.equal(generated.body.generated, true);
    assert.equal(generated.body.status, "ready");
    assert.equal((await generate(env)).body.deduplicated, true);
    const response = await worker.fetch(new Request(`https://example.invalid/api/report-discussion?source=catalog&report_id=${reportId}`), env, { waitUntil() {} });
    const body = await response.json();
    assert.equal(body.starter.kind, "ai"); assert.equal(body.starter.display_name, "AI 导读");
    assert.equal(body.starter.body, answer.body); assert.deepEqual(body.comments, []);
    assert.equal(JSON.stringify(body).includes("evidence_quote"), false);
  });
  assert.equal(providerCalls, 1);
});

test("source hash mismatch prevents paid generation", async () => {
  const { env, bucket } = setup(); bucket.seed(markerKey, marker()); seedSource(bucket, { corrupt: true });
  let providerCalls = 0;
  await withFetch(async () => { providerCalls += 1; throw new Error("must not call provider"); }, async () => {
    const result = await generate(env);
    assert.equal(result.status, 200);
    assert.equal(result.body.status, "source_unavailable");
  });
  assert.equal(providerCalls, 0);
  assert.equal([...bucket.data.keys()].some((key) => key.endsWith("/starter.json")), false);
});

test("same-title same-date alias text from another report cannot generate a starter", async () => {
  const { env, bucket } = setup(); bucket.seed(markerKey, marker());
  const otherId = "b".repeat(24), title = "Example Research-订单与企业盈利观察-261025";
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [reportId, otherId].map((id) => ({ id, title, bank_name: "Example Research", date_folder: "261025" })) });
  env.SEARCH_INDEX_HISTORY_BASE_URL = "https://example.invalid/discussion-alias/history";
  env.SEARCH_INDEX_CURRENT_BASE_URL = "https://example.invalid/discussion-alias/current";
  let providerCalls = 0, textReads = 0;
  await withFetch(async (url) => {
    if (String(url).startsWith("https://example.invalid/discussion-alias/")) {
      textReads += 1;
      return Response.json({ items: [{ id: otherId, text: reportText }] });
    }
    providerCalls += 1; throw new Error("provider must not receive another report's body");
  }, async () => {
    const result = await generate(env);
    assert.equal(result.status, 200);
    assert.equal(result.body.status, "source_unavailable");
    assert.equal(result.body.generated, false);
  });
  assert.equal(textReads, 2);
  assert.equal(providerCalls, 0);
  assert.equal([...bucket.data.keys()].some((key) => key.endsWith("/starter.json")), false);
});
