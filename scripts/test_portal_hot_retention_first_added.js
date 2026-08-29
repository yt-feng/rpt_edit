#!/usr/bin/env node

const assert = require("node:assert/strict");
const cryptoModule = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const worker = fs.readFileSync(workerPath, "utf8");
const workerWithoutImports = worker.replace(
  /^import\s*\{[\s\S]*?\}\s*from\s*["']\.\/source-lead-adapter\.js["'];\s*/m,
  `function publicSourceLeadItem() { return {}; }
   async function readStoredSourceLead() { return null; }
   async function searchSourceLeadMetadata() { return { items: [], total: 0 }; }
   function sourceLeadAdapterEnabled() { return false; }
  `,
);
assert.notEqual(workerWithoutImports, worker, "the Worker module import must be replaced for the VM harness");
const runnableWorker = workerWithoutImports.replace(/\bexport default\s*\{/, "globalThis.__workerExport = {")
  + `\nglobalThis.__firstAddedTestApi = {
    ensureHotReportPdf,
    enforceHotReportStorageLimit,
    hotReportObjectFirstAddedAt,
    hotReportItemKey,
    hotReportPdfKey,
  };\n`;
const sandbox = {
  AbortController,
  ArrayBuffer,
  Blob,
  DOMException,
  FormData,
  Headers,
  Request,
  Response,
  TextDecoder,
  TextEncoder,
  URL,
  URLSearchParams,
  Uint8Array,
  atob,
  btoa,
  clearTimeout,
  console,
  crypto: cryptoModule.webcrypto,
  fetch,
  setTimeout,
};
vm.createContext(sandbox);
vm.runInContext(runnableWorker, sandbox, { filename: workerPath });
const api = sandbox.__firstAddedTestApi;

function toBytes(value) {
  if (typeof value === "string") return new Uint8Array(Buffer.from(value));
  if (value instanceof Uint8Array) return value.slice();
  if (value instanceof ArrayBuffer) return new Uint8Array(value.slice(0));
  throw new TypeError("Unsupported mock R2 body");
}

class MockR2Bucket {
  constructor() {
    this.objects = new Map();
    this.listCalls = [];
    this.sequence = 0;
  }

  metadata(stored, includeCustomMetadata = true) {
    return {
      key: stored.key,
      size: stored.size,
      etag: stored.etag,
      uploaded: stored.uploaded,
      customMetadata: includeCustomMetadata ? stored.customMetadata : undefined,
      httpMetadata: stored.httpMetadata,
    };
  }

  async put(keyValue, value, options = {}) {
    const key = String(keyValue);
    const existing = this.objects.get(key);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagDoesNotMatch === "*" && existing) return null;
    if (onlyIf.etagMatches && (!existing || existing.etag !== String(onlyIf.etagMatches))) return null;
    const bytes = toBytes(value);
    const stored = {
      key,
      bytes,
      size: bytes.byteLength,
      etag: `etag-${++this.sequence}`,
      uploaded: new Date(),
      customMetadata: { ...(options.customMetadata || {}) },
      httpMetadata: { ...(options.httpMetadata || {}) },
    };
    this.objects.set(key, stored);
    return this.metadata(stored);
  }

  async head(keyValue) {
    const stored = this.objects.get(String(keyValue));
    return stored ? this.metadata(stored) : null;
  }

  async get(keyValue) {
    const stored = this.objects.get(String(keyValue));
    if (!stored) return null;
    const bytes = stored.bytes.slice();
    return {
      ...this.metadata(stored),
      body: bytes,
      async text() { return Buffer.from(bytes).toString("utf8"); },
    };
  }

  async list(options = {}) {
    const prefix = String(options.prefix || "");
    this.listCalls.push({ ...options, prefix });
    const includeCustomMetadata = Array.isArray(options.include)
      && options.include.includes("customMetadata");
    return {
      objects: [...this.objects.values()]
        .filter((stored) => stored.key.startsWith(prefix))
        .sort((left, right) => left.key.localeCompare(right.key))
        .map((stored) => this.metadata(stored, includeCustomMetadata)),
      truncated: false,
    };
  }

  async delete(keyOrKeys) {
    const keys = Array.isArray(keyOrKeys) ? keyOrKeys : [keyOrKeys];
    keys.forEach((key) => this.objects.delete(String(key)));
  }
}

async function putJson(bucket, key, value) {
  return bucket.put(key, JSON.stringify(value), {
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
}

(async () => {
  const upgradeBucket = new MockR2Bucket();
  const upgradeId = "hot:aaaaaaaaaaaaaaaa";
  const upgradeOrigin = "bbbbbbbbbbbbbbbb";
  const upgradeKey = api.hotReportPdfKey(upgradeId);
  const firstAdded = "2024-01-02T03:04:05.000Z";
  await upgradeBucket.put(upgradeKey, new Uint8Array([37, 80, 68, 70, 45, 79, 76, 68]), {
    customMetadata: {
      source: "hot-report-archive",
      hot_report_id: upgradeId,
      origin_source: "catalog",
      origin_report_id: upgradeOrigin,
      archive_generation: "1111111111111111",
      hot_added_at: firstAdded,
    },
  });
  upgradeBucket.objects.get(upgradeKey).uploaded = new Date("2026-08-02T12:00:00.000Z");
  const upgraded = await api.ensureHotReportPdf(
    { REPORT_BUCKET: upgradeBucket },
    upgradeId,
    {
      origin_source: "catalog",
      origin_report_id: upgradeOrigin,
      filename: "valuable-old-report.pdf",
      body: new Uint8Array([37, 80, 68, 70, 45, 78, 69, 87]),
      pdf_custom_metadata: {
        source: "catalog-pdf-override",
        report_id: upgradeOrigin,
        version: "2222222222222222",
      },
    },
    "2026-08-03T00:00:00.000Z",
  );
  assert.equal(upgraded.replaced, true);
  assert.equal(
    (await upgradeBucket.head(upgradeKey)).customMetadata.hot_added_at,
    firstAdded,
    "normal hot -> Text Only replacement must preserve the PDF's first-added timestamp",
  );

  const retentionBucket = new MockR2Bucket();
  const entries = [
    {
      id: "hot:1111111111111111",
      size: 100,
      hotAddedAt: "2024-01-01T00:00:00.000Z",
      uploaded: "2026-07-01T00:00:00.000Z",
    },
    {
      id: "hot:2222222222222222",
      size: 100,
      hotAddedAt: "2025-01-01T00:00:00.000Z",
      uploaded: "2024-02-01T00:00:00.000Z",
    },
    {
      id: "hot:3333333333333333",
      size: 1,
      hotAddedAt: "2026-01-01T00:00:00.000Z",
      uploaded: "2025-02-01T00:00:00.000Z",
    },
  ];
  for (const entry of entries) {
    const pdfKey = api.hotReportPdfKey(entry.id);
    await retentionBucket.put(pdfKey, new Uint8Array(entry.size), {
      customMetadata: { hot_added_at: entry.hotAddedAt },
    });
    retentionBucket.objects.get(pdfKey).uploaded = new Date(entry.uploaded);
    await putJson(retentionBucket, api.hotReportItemKey(entry.id), {
      id: entry.id,
      source: "hot",
      title: entry.id,
      filename: `${entry.id}.pdf`,
      size_bytes: entry.size,
      hot_added_at: entry.hotAddedAt,
      created_at: entry.hotAddedAt,
      updated_at: entry.hotAddedAt,
      retention_state: "active",
    });
  }

  const result = await api.enforceHotReportStorageLimit({
    REPORT_BUCKET: retentionBucket,
    HOT_REPORT_CLEANUP_ENABLED: "true",
    HOT_REPORT_STORAGE_LIMIT_BYTES: 200,
  });
  assert.equal(result.pruned_count, 1);
  assert.equal(
    await retentionBucket.head(api.hotReportPdfKey(entries[0].id)),
    null,
    "retention must prune by PDF customMetadata.hot_added_at, not the replacement upload time",
  );
  assert.ok(await retentionBucket.head(api.hotReportPdfKey(entries[1].id)));
  assert.ok(await retentionBucket.head(api.hotReportPdfKey(entries[2].id)));
  const pdfList = retentionBucket.listCalls.find((call) => call.prefix === "_hot-reports/pdfs/");
  assert.deepEqual(
    Array.from(pdfList.include || []),
    ["customMetadata"],
    "R2 LIST must explicitly request custom metadata for first-added retention ordering",
  );

  assert.equal(
    api.hotReportObjectFirstAddedAt({
      uploaded: new Date("2023-01-01T00:00:00.000Z"),
      customMetadata: {},
    }),
    Date.parse("2023-01-01T00:00:00.000Z"),
    "legacy PDFs without hot_added_at must fall back to R2 uploaded",
  );

  console.log("portal hot retention first-added ordering checks passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
