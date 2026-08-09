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

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
  assert.ok(start >= 0, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  assert.ok(bodyStart >= 0, `${name} must have a body`);
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function assertSchedulesOnlyAfterFinalize(handlerName, expectedSchedules) {
  const source = extractFunction(worker, handlerName);
  const scheduleIndexes = [];
  let cursor = 0;
  while (true) {
    const index = source.indexOf("scheduleHotReportArchive(", cursor);
    if (index < 0) break;
    scheduleIndexes.push(index);
    cursor = index + 1;
  }
  const finalizeCount = (source.match(/finalizeAccountDownloadDecision\(/g) || []).length;
  assert.equal(scheduleIndexes.length, expectedSchedules, `${handlerName} must schedule every successful PDF branch`);
  assert.equal(finalizeCount, expectedSchedules, `${handlerName} must finalize every scheduled PDF branch exactly once`);
  for (const scheduleIndex of scheduleIndexes) {
    const finalizeIndex = source.lastIndexOf("finalizeAccountDownloadDecision(", scheduleIndex);
    const rejectedIndex = source.lastIndexOf("if (!consumed.ok)", scheduleIndex);
    assert.ok(finalizeIndex >= 0, `${handlerName} must finalize before scheduling an archive`);
    assert.ok(rejectedIndex > finalizeIndex, `${handlerName} must reject failed finalization before scheduling an archive`);
  }
  return source;
}

const catalogDownload = assertSchedulesOnlyAfterFinalize("handleDownload", 1);
const externalDownload = assertSchedulesOnlyAfterFinalize("handleExternalPdf", 2);
const thinkTankDownload = assertSchedulesOnlyAfterFinalize("handleThinkTankPdf", 2);

assert.match(catalogDownload, /function handleDownload\(request, env, ctx = null\)/);
assert.match(externalDownload, /function handleExternalPdf\(request, env, ctx = null\)/);
assert.match(thinkTankDownload, /function handleThinkTankPdf\(request, env, ctx = null\)/);
assert.match(worker, /pathname === "\/download"[\s\S]*?handleDownload\(request, env, ctx\)/);
assert.match(worker, /pathname === "\/external\/pdf"[\s\S]*?handleExternalPdf\(request, env, ctx\)/);
assert.match(worker, /pathname === "\/thinktank\/pdf"[\s\S]*?handleThinkTankPdf\(request, env, ctx\)/);

const externalPendingBranch = externalDownload.slice(externalDownload.indexOf("// 3) Gated and not yet mirrored"));
assert.ok(externalPendingBranch.length > 0, "external 202 branch must remain identifiable");
assert.doesNotMatch(
  externalPendingBranch,
  /scheduleHotReportArchive\(/,
  "queued/202 external reports must not be archived before a PDF is delivered",
);
for (const source of [catalogDownload, externalDownload, thinkTankDownload]) {
  const firstSchedule = source.indexOf("scheduleHotReportArchive(");
  assert.ok(firstSchedule > source.indexOf("if (!consumed.ok)"), "failed finalization must return before archive scheduling");
}

const exposedNames = [
  "automaticHotReportId",
  "archiveReportAsHot",
  "enforceHotReportStorageLimit",
  "publicHotReportItem",
  "hotReportItemKey",
  "hotReportPdfKey",
  "hotReportCommentKey",
  "hotReportCommentOrderKey",
  "catalogPdfOverrideItemKey",
  "deleteLinkedCatalogPdfOverride",
  "deleteHotReportArchive",
  "listHotReportRows",
  "hotReportStorageStats",
];
const runnableWorker = workerWithoutImports.replace(/\bexport default\s*\{/, "globalThis.__workerExport = {")
  + `\nglobalThis.__hotArchiveTestApi = { ${exposedNames.join(", ")} };\n`;
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
const api = sandbox.__hotArchiveTestApi;

function bytesFrom(value) {
  if (typeof value === "string") return Promise.resolve(new Uint8Array(Buffer.from(value)));
  if (value instanceof Uint8Array) return Promise.resolve(value.slice());
  if (value instanceof ArrayBuffer) return Promise.resolve(new Uint8Array(value.slice(0)));
  if (value && typeof value.arrayBuffer === "function") {
    return value.arrayBuffer().then((buffer) => new Uint8Array(buffer));
  }
  if (value && typeof value.getReader === "function") {
    return new Response(value).arrayBuffer().then((buffer) => new Uint8Array(buffer));
  }
  throw new TypeError("Unsupported mock R2 body");
}

class MockR2Bucket {
  constructor() {
    this.objects = new Map();
    this.putCalls = [];
    this.deleteCalls = [];
    this.getCalls = [];
    this.listCalls = [];
    this.failGetKeys = new Set();
    this.conditionalPutConflicts = new Set();
    this.afterDelete = null;
    this.beforeGet = null;
    this.sequence = 0;
  }

  async put(keyValue, body, options = {}) {
    const key = String(keyValue);
    const existing = this.objects.get(key);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && this.conditionalPutConflicts.delete(key)) return null;
    if (onlyIf.etagDoesNotMatch === "*" && existing) return null;
    if (onlyIf.etagMatches && (!existing || existing.etag !== String(onlyIf.etagMatches))) return null;
    const bytes = await bytesFrom(body);
    const stored = {
      key,
      bytes,
      size: bytes.byteLength,
      etag: `mock-etag-${++this.sequence}`,
      uploaded: new Date(),
      customMetadata: options.customMetadata || {},
      httpMetadata: options.httpMetadata || {},
    };
    this.objects.set(key, stored);
    this.putCalls.push({ key, options });
    return this.metadata(stored);
  }

  metadata(stored) {
    return {
      key: stored.key,
      size: stored.size,
      etag: stored.etag,
      uploaded: stored.uploaded,
      customMetadata: stored.customMetadata,
      httpMetadata: stored.httpMetadata,
    };
  }

  async head(keyValue) {
    const stored = this.objects.get(String(keyValue));
    return stored ? this.metadata(stored) : null;
  }

  async get(keyValue) {
    const key = String(keyValue);
    if (typeof this.beforeGet === "function") await this.beforeGet(key, this);
    this.getCalls.push(key);
    if (this.failGetKeys.has(key)) throw new Error(`mock R2 GET failed for ${key}`);
    const stored = this.objects.get(key);
    if (!stored) return null;
    const bytes = stored.bytes.slice();
    return {
      ...this.metadata(stored),
      body: bytes,
      async text() { return Buffer.from(bytes).toString("utf8"); },
      async json() { return JSON.parse(Buffer.from(bytes).toString("utf8")); },
      writeHttpMetadata() {},
    };
  }

  async list(options = {}) {
    const prefix = String(options.prefix || "");
    this.listCalls.push({ ...options, prefix });
    const start = Math.max(0, Number(options.cursor || 0) || 0);
    const limit = Math.max(1, Number(options.limit || 1000) || 1000);
    const objects = [...this.objects.values()]
      .filter((stored) => stored.key.startsWith(prefix))
      .sort((left, right) => left.key.localeCompare(right.key))
      .map((stored) => this.metadata(stored));
    const page = objects.slice(start, start + limit);
    const next = start + page.length;
    return {
      objects: page,
      truncated: next < objects.length,
      cursor: next < objects.length ? String(next) : undefined,
    };
  }

  async delete(keyOrKeys) {
    const keys = Array.isArray(keyOrKeys) ? keyOrKeys : [keyOrKeys];
    for (const keyValue of keys) {
      const key = String(keyValue);
      this.deleteCalls.push(key);
      this.objects.delete(key);
      if (typeof this.afterDelete === "function") await this.afterDelete(key, this);
    }
  }
}

async function putJson(bucket, key, value) {
  await bucket.put(key, JSON.stringify(value), {
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
}

async function readJson(bucket, key) {
  const object = await bucket.get(key);
  return object ? JSON.parse(await object.text()) : null;
}

(async () => {
  const originId = "aaaaaaaaaaaaaaaa";
  const stableId = await api.automaticHotReportId("catalog", originId);
  assert.equal(stableId, await api.automaticHotReportId("catalog", originId));
  assert.notEqual(stableId, await api.automaticHotReportId("external", originId));
  assert.notEqual(stableId, await api.automaticHotReportId("catalog", "bbbbbbbbbbbbbbbb"));

  const archiveBucket = new MockR2Bucket();
  const archiveEnv = { REPORT_BUCKET: archiveBucket, HOT_REPORT_STORAGE_LIMIT_BYTES: 10_000 };
  const sourceKey = "reports/aaaaaaaaaaaaaaaa.pdf";
  await archiveBucket.put(sourceKey, new Uint8Array([37, 80, 68, 70, 45, 49, 50, 51]));
  const baseInput = {
    origin_source: "catalog",
    origin_report_id: originId,
    title: "Valuable old report",
    institution: "NOMURA",
    date: "2026-07-01",
    filename: "valuable.pdf",
    source_object_key: sourceKey,
    catalog_pdf_override_id: originId,
  };
  const first = await api.archiveReportAsHot(archiveEnv, { ...baseInput, reason: "text_only_pdf_upload" });
  const firstRow = await readJson(archiveBucket, api.hotReportItemKey(first.item.id));
  const second = await api.archiveReportAsHot(archiveEnv, { ...baseInput, reason: "successful_download" });
  const secondRow = await readJson(archiveBucket, api.hotReportItemKey(second.item.id));

  assert.equal(first.created, true);
  assert.equal(second.created, false, "a second archive of the same source report must update rather than duplicate");
  assert.equal(second.item.id, first.item.id);
  assert.equal(secondRow.created_at, firstRow.created_at, "created_at must preserve first archival time");
  assert.equal(secondRow.hot_added_at, firstRow.hot_added_at, "hot_added_at must preserve first archival time");
  assert.equal(secondRow.sort_order, firstRow.sort_order, "repeat downloads must not bump administrator ordering");
  assert.equal(secondRow.download_count, 1, "a successful download must increment the archive download counter");
  assert.equal(secondRow.last_downloaded_at, secondRow.updated_at);
  const archivedPdfKeys = [...archiveBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/pdfs/"));
  assert.equal(archivedPdfKeys.length, 1, "a report must have exactly one durable hot-report PDF copy");
  assert.equal(
    archiveBucket.putCalls.filter((call) => call.key === archivedPdfKeys[0]).length,
    1,
    "dedupe must avoid writing the PDF body again",
  );
  assert.equal(archiveBucket.listCalls.length, 0, "a successful download must not run a full retention scan inline");

  const upgradeBucket = new MockR2Bucket();
  const upgradeOrigin = "ababcdabcdabcdab";
  const upgradeSource = `reports/${upgradeOrigin}.pdf`;
  await upgradeBucket.put(upgradeSource, new Uint8Array([37, 80, 68, 70, 45, 79, 76, 68]));
  const normalArchive = await api.archiveReportAsHot({ REPORT_BUCKET: upgradeBucket }, {
    origin_source: "catalog",
    origin_report_id: upgradeOrigin,
    title: "Upgrade in place",
    filename: "upgrade.pdf",
    source_object_key: upgradeSource,
    reason: "successful_download",
  });
  const upgradePdfKey = normalArchive.pdf_key;
  const oldPdf = await upgradeBucket.head(upgradePdfKey);
  assert.equal(oldPdf.customMetadata.source, "hot-report-archive");
  const requestedUpgradeVersion = "1234567890abcdef";
  const upgradedArchive = await api.archiveReportAsHot({ REPORT_BUCKET: upgradeBucket }, {
    origin_source: "catalog",
    origin_report_id: upgradeOrigin,
    title: "Upgrade in place",
    filename: "upgrade.pdf",
    body: new Uint8Array([37, 80, 68, 70, 45, 78, 69, 87]),
    catalog_pdf_override_id: upgradeOrigin,
    reason: "text_only_upload",
    pdf_custom_metadata: {
      source: "catalog-pdf-override",
      report_id: upgradeOrigin,
      version: requestedUpgradeVersion,
    },
  });
  const upgradedPdf = await upgradeBucket.head(upgradePdfKey);
  const upgradedRow = await readJson(upgradeBucket, api.hotReportItemKey(upgradedArchive.item.id));
  const upgradePdfPuts = upgradeBucket.putCalls.filter((call) => call.key === upgradePdfKey);
  assert.equal(
    [...upgradeBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/pdfs/")).length,
    1,
    "a Text Only upload must replace the normal hot copy at the same stable key",
  );
  assert.equal(upgradePdfPuts.length, 2);
  assert.equal(
    upgradePdfPuts[1].options.onlyIf.etagMatches,
    oldPdf.etag,
    "the normal-to-Text-Only PDF upgrade must be fenced by the prior object ETag",
  );
  assert.equal(upgradedPdf.customMetadata.source, "catalog-pdf-override");
  assert.equal(upgradedPdf.customMetadata.origin_source, "catalog");
  assert.equal(upgradedPdf.customMetadata.origin_report_id, upgradeOrigin);
  assert.equal(upgradedPdf.customMetadata.report_id, upgradeOrigin);
  assert.equal(upgradedPdf.customMetadata.version, requestedUpgradeVersion);
  assert.match(upgradedPdf.customMetadata.archive_generation, /^[a-f0-9]{16}$/);
  assert.equal(upgradedRow.archive_generation, upgradedPdf.customMetadata.archive_generation);
  assert.equal(upgradedRow.pdf_etag, upgradedPdf.etag);

  const retryEtag = upgradedPdf.etag;
  await api.archiveReportAsHot({ REPORT_BUCKET: upgradeBucket }, {
    origin_source: "catalog",
    origin_report_id: upgradeOrigin,
    title: "Upgrade retry",
    filename: "upgrade-retry.pdf",
    body: new Uint8Array([37, 80, 68, 70, 45, 82, 69, 84, 82, 89]),
    catalog_pdf_override_id: upgradeOrigin,
    reason: "text_only_upload",
    pdf_custom_metadata: {
      source: "catalog-pdf-override",
      report_id: upgradeOrigin,
      version: "fedcba0987654321",
    },
  });
  const retryPdf = await upgradeBucket.head(upgradePdfKey);
  assert.equal(retryPdf.etag, retryEtag, "a retry must reuse the already upgraded PDF object");
  assert.equal(retryPdf.customMetadata.version, requestedUpgradeVersion, "a retry must reuse the stored version");
  assert.equal(
    upgradeBucket.putCalls.filter((call) => call.key === upgradePdfKey).length,
    2,
    "a retry must not create or rewrite a second PDF",
  );

  const originCollisionBucket = new MockR2Bucket();
  const collisionOrigin = "cdcdcdcdcdcdcdcd";
  const collisionId = await api.automaticHotReportId("catalog", collisionOrigin);
  const collisionKey = api.hotReportPdfKey(collisionId);
  await originCollisionBucket.put(collisionKey, new Uint8Array([37, 80, 68, 70, 45]), {
    customMetadata: {
      source: "hot-report-archive",
      hot_report_id: collisionId,
      origin_source: "catalog",
      origin_report_id: "ffffffffffffffff",
      archive_generation: "aaaaaaaaaaaaaaaa",
    },
  });
  const collisionEtag = (await originCollisionBucket.head(collisionKey)).etag;
  await assert.rejects(
    api.archiveReportAsHot({ REPORT_BUCKET: originCollisionBucket }, {
      origin_source: "catalog",
      origin_report_id: collisionOrigin,
      title: "Must not overwrite",
      filename: "collision.pdf",
      body: new Uint8Array([37, 80, 68, 70, 45, 78, 69, 87]),
      reason: "successful_download",
    }),
    /origin verification failed/,
    "an object with a different exact origin must never be reused or overwritten",
  );
  assert.equal((await originCollisionBucket.head(collisionKey)).etag, collisionEtag);

  const publicItem = api.publicHotReportItem(secondRow);
  for (const privateField of [
    "origin_source",
    "origin_report_id",
    "pdf_etag",
    "pdf_key",
    "object_key",
    "catalog_pdf_override_id",
    "download_count",
  ]) {
    assert.equal(Object.hasOwn(publicItem, privateField), false, `public hot reports must not expose ${privateField}`);
  }

  const retentionBucket = new MockR2Bucket();
  const retentionEnv = { REPORT_BUCKET: retentionBucket, HOT_REPORT_STORAGE_LIMIT_BYTES: 200 };
  const oldestId = "hot:1111111111111111";
  const newerId = "hot:2222222222222222";
  const newestId = "hot:3333333333333333";
  const overrideId = "cccccccccccccccc";
  const oldestPdfKey = api.hotReportPdfKey(oldestId);
  const newerPdfKey = api.hotReportPdfKey(newerId);
  const newestPdfKey = api.hotReportPdfKey(newestId);
  const oldestRow = {
    id: oldestId,
    source: "hot",
    title: "Oldest",
    filename: "oldest.pdf",
    size_bytes: 100,
    sort_order: 300,
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    retention_state: "active",
    archive_generation: "1111111111111111",
    catalog_pdf_override_id: overrideId,
  };
  const newerRow = {
    id: newerId,
    source: "hot",
    title: "Newer",
    filename: "newer.pdf",
    size_bytes: 100,
    sort_order: 100,
    hot_added_at: "2026-02-01T00:00:00.000Z",
    created_at: "2026-02-01T00:00:00.000Z",
    retention_state: "active",
  };
  await retentionBucket.put(oldestPdfKey, new Uint8Array(100));
  await retentionBucket.put(newerPdfKey, new Uint8Array(100));
  await putJson(retentionBucket, api.hotReportItemKey(oldestId), oldestRow);
  await putJson(retentionBucket, api.hotReportItemKey(newerId), newerRow);
  const commentKey = api.hotReportCommentKey(oldestId, "comment:4444444444444444");
  const orderKey = api.hotReportCommentOrderKey(oldestId);
  const overrideKey = api.catalogPdfOverrideItemKey(overrideId);
  await putJson(retentionBucket, commentKey, { id: "comment:4444444444444444", report_id: oldestId });
  await putJson(retentionBucket, orderKey, { report_id: oldestId, ids: ["comment:4444444444444444"] });
  const oldestPdfEtag = (await retentionBucket.head(oldestPdfKey)).etag;
  await putJson(retentionBucket, overrideKey, {
    id: overrideId,
    version: "aaaaaaaaaaaaaaaa",
    hot_report_id: oldestId,
    object_key: oldestPdfKey,
    hot_report_generation: "1111111111111111",
    filename: "oldest.pdf",
    size_bytes: 100,
    etag: oldestPdfEtag,
    uploaded_at: "2026-01-01T00:00:00.000Z",
    uploaded_by: "admin-a@users.portal.example.invalid",
    source: "catalog-pdf-override",
  });
  for (let index = 0; index < 1000; index += 1) {
    await putJson(
      retentionBucket,
      api.hotReportCommentKey(oldestId, `comment:${String(index).padStart(16, "0")}`),
      { id: `comment:${String(index).padStart(16, "0")}`, report_id: oldestId },
    );
  }

  retentionBucket.deleteCalls.length = 0;
  retentionBucket.getCalls.length = 0;
  const equalLimit = await api.enforceHotReportStorageLimit(retentionEnv);
  assert.equal(equalLimit.total_size_bytes, 200);
  assert.equal(equalLimit.pruned_count, 0, "storage exactly at 2 GiB-equivalent limit must not be pruned");
  assert.equal(retentionBucket.deleteCalls.length, 0);
  assert.equal(retentionBucket.getCalls.length, 0, "retention at or below the cap must use PDF LIST metadata only");

  const newestRow = {
    id: newestId,
    source: "hot",
    title: "Newest",
    filename: "newest.pdf",
    size_bytes: 1,
    sort_order: 1,
    hot_added_at: "2026-03-01T00:00:00.000Z",
    created_at: "2026-03-01T00:00:00.000Z",
    retention_state: "active",
  };
  await retentionBucket.put(newestPdfKey, new Uint8Array(1));
  await putJson(retentionBucket, api.hotReportItemKey(newestId), newestRow);
  let injectedOverrideRace = false;
  retentionBucket.afterDelete = async (key, bucket) => {
    if (key !== oldestPdfKey || injectedOverrideRace) return;
    injectedOverrideRace = true;
    await putJson(bucket, overrideKey, {
      id: overrideId,
      version: "aaaaaaaaaaaaaaaa",
      hot_report_id: oldestId,
      object_key: oldestPdfKey,
      hot_report_generation: "1111111111111111",
      filename: "oldest.pdf",
      size_bytes: 100,
      etag: oldestPdfEtag,
      uploaded_at: "2026-01-01T00:00:00.000Z",
      uploaded_by: "admin-a@users.portal.example.invalid",
      source: "catalog-pdf-override",
    });
  };
  retentionBucket.deleteCalls.length = 0;
  const overLimit = await api.enforceHotReportStorageLimit(retentionEnv);
  retentionBucket.afterDelete = null;
  assert.equal(overLimit.pruned_count, 1);
  assert.equal(overLimit.total_size_bytes, 101);
  assert.equal(await retentionBucket.head(oldestPdfKey), null, "oldest hot_added_at PDF must be pruned first");
  const deletedMarker = await readJson(retentionBucket, api.hotReportItemKey(oldestId));
  assert.equal(deletedMarker.retention_state, "deleted", "pruning must retain a CAS-fenced tombstone");
  assert.match(deletedMarker.retention_generation, /^[a-f0-9]{16}$/);
  assert.ok(await retentionBucket.head(newerPdfKey), "newer report must remain even when its display order is lower");
  assert.ok(await retentionBucket.head(newestPdfKey));
  assert.equal(await retentionBucket.head(commentKey), null, "pruned report comments must be deleted");
  assert.equal(
    [...retentionBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/comments/1111111111111111/")).length,
    0,
    "comment cleanup must paginate beyond the public 500-comment limit",
  );
  assert.ok(
    retentionBucket.listCalls.filter((call) => call.prefix === "_hot-reports/comments/1111111111111111/").length >= 2,
    "comment prefix deletion must continue across R2 pages",
  );
  assert.equal(await retentionBucket.head(orderKey), null, "pruned report comment ordering must be deleted");
  const deletedOverride = await readJson(retentionBucket, overrideKey);
  assert.equal(deletedOverride.state, "deleted", "linked Text Only override metadata must become an unavailable tombstone");
  assert.equal(deletedOverride.hot_report_generation, "1111111111111111");
  assert.equal(
    retentionBucket.deleteCalls.filter((key) => key === overrideKey).length,
    0,
    "override cleanup must never use an unconditional object delete",
  );
  assert.ok(
    retentionBucket.putCalls.filter((call) => (
      call.key === overrideKey && call.options.onlyIf && call.options.onlyIf.etagMatches
    )).length >= 2,
    "cleanup must CAS-tombstone an override that appears again after PDF deletion",
  );

  const overrideRaceBucket = new MockR2Bucket();
  const overrideRaceReportId = "6464646464646464";
  const overrideRaceHotId = "hot:6464646464646464";
  const overrideRaceKey = api.catalogPdfOverrideItemKey(overrideRaceReportId);
  const overrideRacePdfKey = api.hotReportPdfKey(overrideRaceHotId);
  const deletionRowA = {
    id: overrideRaceHotId,
    catalog_pdf_override_id: overrideRaceReportId,
    archive_generation: "aaaaaaaaaaaaaaaa",
  };
  const overrideRowA = {
    id: overrideRaceReportId,
    version: "1111111111111111",
    hot_report_id: overrideRaceHotId,
    hot_report_generation: "aaaaaaaaaaaaaaaa",
    object_key: overrideRacePdfKey,
    filename: "a.pdf",
    size_bytes: 10,
    etag: "pdf-a-etag",
    uploaded_at: "2026-01-01T00:00:00.000Z",
    uploaded_by: "admin-a@users.portal.example.invalid",
    source: "catalog-pdf-override",
  };
  await putJson(overrideRaceBucket, overrideRaceKey, overrideRowA);
  assert.equal(
    await api.deleteLinkedCatalogPdfOverride({ REPORT_BUCKET: overrideRaceBucket }, deletionRowA),
    true,
  );
  const overrideTombstoneA = await overrideRaceBucket.head(overrideRaceKey);
  assert.equal((await readJson(overrideRaceBucket, overrideRaceKey)).state, "deleted");
  const overrideRowB = {
    ...overrideRowA,
    version: "2222222222222222",
    hot_report_generation: "bbbbbbbbbbbbbbbb",
    filename: "b.pdf",
    etag: "pdf-b-etag",
    uploaded_at: "2026-02-01T00:00:00.000Z",
  };
  await overrideRaceBucket.put(overrideRaceKey, JSON.stringify(overrideRowB), {
    onlyIf: { etagMatches: overrideTombstoneA.etag },
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  const overrideMetadataB = await overrideRaceBucket.head(overrideRaceKey);
  assert.equal(
    await api.deleteLinkedCatalogPdfOverride({ REPORT_BUCKET: overrideRaceBucket }, deletionRowA),
    false,
    "old generation A cleanup must not tombstone successful generation B metadata",
  );
  assert.equal((await overrideRaceBucket.head(overrideRaceKey)).etag, overrideMetadataB.etag);
  assert.equal((await readJson(overrideRaceBucket, overrideRaceKey)).hot_report_generation, "bbbbbbbbbbbbbbbb");
  assert.equal(overrideRaceBucket.deleteCalls.filter((key) => key === overrideRaceKey).length, 0);

  const readFailureBucket = new MockR2Bucket();
  const readFailureEnv = { REPORT_BUCKET: readFailureBucket, HOT_REPORT_STORAGE_LIMIT_BYTES: 50 };
  const readFailureId = "hot:4444444444444444";
  const readFailurePdf = api.hotReportPdfKey(readFailureId);
  const readFailureItem = api.hotReportItemKey(readFailureId);
  await readFailureBucket.put(readFailurePdf, new Uint8Array(100));
  await putJson(readFailureBucket, readFailureItem, {
    id: readFailureId,
    source: "hot",
    title: "Read failure",
    filename: "read-failure.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    retention_state: "active",
  });
  readFailureBucket.failGetKeys.add(readFailureItem);
  await assert.rejects(
    api.enforceHotReportStorageLimit(readFailureEnv),
    /mock R2 GET failed/,
    "retention must fail closed when candidate metadata cannot be read",
  );
  assert.ok(await readFailureBucket.head(readFailurePdf), "a transient metadata read failure must never delete the PDF");
  assert.equal(readFailureBucket.deleteCalls.length, 0);

  const crashedWriterBucket = new MockR2Bucket();
  const crashedWriterId = "hot:4545454545454545";
  const crashedWriterPdf = api.hotReportPdfKey(crashedWriterId);
  const crashedWriterItem = api.hotReportItemKey(crashedWriterId);
  await crashedWriterBucket.put(crashedWriterPdf, new Uint8Array(100), {
    customMetadata: {
      source: "hot-report-archive",
      hot_report_id: crashedWriterId,
      origin_source: "catalog",
      origin_report_id: "4545454545454545",
      archive_generation: "4545454545454545",
    },
  });
  await putJson(crashedWriterBucket, crashedWriterItem, {
    id: crashedWriterId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: "4545454545454545",
    title: "Writer crashed before active metadata",
    filename: "crashed-writer.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    updated_at: "2026-01-01T00:00:00.000Z",
    deleted_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleted",
    retention_generation: "2323232323232323",
  });
  const crashedWriterCleanup = await api.enforceHotReportStorageLimit({
    REPORT_BUCKET: crashedWriterBucket,
    HOT_REPORT_STORAGE_LIMIT_BYTES: 50,
  });
  assert.equal(crashedWriterCleanup.pruned_count, 1);
  assert.equal(crashedWriterCleanup.total_size_bytes, 0);
  assert.equal(crashedWriterCleanup.item_count, 0);
  assert.equal(crashedWriterCleanup.pdf_count, 0);
  assert.equal(
    await crashedWriterBucket.head(crashedWriterPdf),
    null,
    "retention must physically remove a PDF stranded beside a deleted tombstone",
  );
  const crashedWriterFinal = await readJson(crashedWriterBucket, crashedWriterItem);
  assert.equal(crashedWriterFinal.retention_state, "deleted");
  assert.notEqual(crashedWriterFinal.retention_generation, "2323232323232323");

  const casBucket = new MockR2Bucket();
  const casId = "hot:5555555555555555";
  const casPdf = api.hotReportPdfKey(casId);
  const casItem = api.hotReportItemKey(casId);
  const casRow = {
    id: casId,
    source: "hot",
    title: "CAS conflict",
    filename: "cas.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    retention_state: "active",
  };
  await casBucket.put(casPdf, new Uint8Array(100));
  await putJson(casBucket, casItem, casRow);
  casBucket.conditionalPutConflicts.add(casItem);
  assert.equal(
    await api.deleteHotReportArchive({ REPORT_BUCKET: casBucket }, casRow),
    false,
    "cleanup must stop if its active-to-deleting CAS loses",
  );
  assert.ok(await casBucket.head(casPdf), "a lost deletion CAS must not delete the PDF");
  assert.equal((await readJson(casBucket, casItem)).retention_state, "active");

  const deletingBucket = new MockR2Bucket();
  const deletingOriginId = "dddddddddddddddd";
  const deletingId = await api.automaticHotReportId("catalog", deletingOriginId);
  const deletingPdf = api.hotReportPdfKey(deletingId);
  await deletingBucket.put(deletingPdf, new Uint8Array([37, 80, 68, 70, 45]));
  await putJson(deletingBucket, api.hotReportItemKey(deletingId), {
    id: deletingId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: deletingOriginId,
    title: "Deleting",
    filename: "deleting.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleting",
    retention_generation: "abcdefabcdefabcd",
  });
  await assert.rejects(
    api.archiveReportAsHot({ REPORT_BUCKET: deletingBucket }, {
      origin_source: "catalog",
      origin_report_id: deletingOriginId,
      title: "Deleting",
      filename: "deleting.pdf",
      source_object_key: deletingPdf,
      reason: "successful_download",
    }),
    /retention cleanup is in progress/,
    "writers must never reactivate a deleting generation",
  );
  assert.equal((await readJson(deletingBucket, api.hotReportItemKey(deletingId))).retention_state, "deleting");
  assert.ok(await deletingBucket.head(deletingPdf));

  const fencedWriteBucket = new MockR2Bucket();
  const fencedOriginId = "abababababababab";
  const fencedId = await api.automaticHotReportId("catalog", fencedOriginId);
  const fencedSource = "reports/abababababababab.pdf";
  await fencedWriteBucket.put(fencedSource, new Uint8Array([37, 80, 68, 70, 45]));
  await putJson(fencedWriteBucket, api.hotReportItemKey(fencedId), {
    id: fencedId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: fencedOriginId,
    title: "Fenced write",
    filename: "fenced.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleting",
    retention_generation: "1234567890abcdef",
  });
  await assert.rejects(
    api.archiveReportAsHot({ REPORT_BUCKET: fencedWriteBucket }, {
      origin_source: "catalog",
      origin_report_id: fencedOriginId,
      title: "Fenced write",
      filename: "fenced.pdf",
      source_object_key: fencedSource,
      reason: "successful_download",
    }),
    /retention cleanup is in progress/,
  );
  assert.equal(
    await fencedWriteBucket.head(api.hotReportPdfKey(fencedId)),
    null,
    "a PDF created after the deleting fence must not remain as an orphan",
  );

  const staleDeletingBucket = new MockR2Bucket();
  const staleOrigin = "1212121212121212";
  const staleId = await api.automaticHotReportId("catalog", staleOrigin);
  const staleSource = `reports/${staleOrigin}.pdf`;
  const staleOverrideKey = api.catalogPdfOverrideItemKey(staleOrigin);
  await staleDeletingBucket.put(staleSource, new Uint8Array([37, 80, 68, 70, 45, 78, 69, 87]));
  await putJson(staleDeletingBucket, api.hotReportItemKey(staleId), {
    id: staleId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: staleOrigin,
    title: "Crashed cleanup",
    filename: "crashed.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    updated_at: "2026-01-01T00:00:00.000Z",
    deleting_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleting",
    retention_generation: "1212121212121212",
    archive_generation: "3434343434343434",
    catalog_pdf_override_id: staleOrigin,
  });
  await putJson(staleDeletingBucket, staleOverrideKey, {
    id: staleOrigin,
    version: "5656565656565656",
    hot_report_id: staleId,
    hot_report_generation: "3434343434343434",
    object_key: api.hotReportPdfKey(staleId),
    filename: "crashed.pdf",
    size_bytes: 100,
    etag: "stale-pdf-etag",
    uploaded_at: "2026-01-01T00:00:00.000Z",
    uploaded_by: "admin-a@users.portal.example.invalid",
    source: "catalog-pdf-override",
  });
  const recoveredArchive = await api.archiveReportAsHot({ REPORT_BUCKET: staleDeletingBucket }, {
    origin_source: "catalog",
    origin_report_id: staleOrigin,
    title: "Recovered after crash",
    filename: "recovered.pdf",
    source_object_key: staleSource,
    reason: "successful_download",
  });
  const recoveredRow = await readJson(staleDeletingBucket, api.hotReportItemKey(staleId));
  assert.equal(recoveredArchive.item.id, staleId);
  assert.equal(recoveredRow.retention_state, "active", "a writer must finish a stale crashed deletion before reactivation");
  assert.ok(await staleDeletingBucket.head(api.hotReportPdfKey(staleId)));
  assert.equal((await readJson(staleDeletingBucket, staleOverrideKey)).state, "deleted");

  const doubleRecoveryBucket = new MockR2Bucket();
  const doubleOrigin = "9090909090909090";
  const doubleId = await api.automaticHotReportId("catalog", doubleOrigin);
  const doubleItemKey = api.hotReportItemKey(doubleId);
  const doublePdfKey = api.hotReportPdfKey(doubleId);
  const doubleSource = `reports/${doubleOrigin}.pdf`;
  const staleGenerationA = "9090909090909090";
  const staleRowA = {
    id: doubleId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: doubleOrigin,
    title: "Stale A",
    filename: "stale-a.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    updated_at: "2026-01-01T00:00:00.000Z",
    deleting_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleting",
    retention_generation: staleGenerationA,
  };
  await doubleRecoveryBucket.put(doubleSource, new Uint8Array([37, 80, 68, 70, 45, 66]));
  await putJson(doubleRecoveryBucket, doubleItemKey, staleRowA);
  const staleEtagA = (await doubleRecoveryBucket.head(doubleItemKey)).etag;
  const doubleInput = {
    origin_source: "catalog",
    origin_report_id: doubleOrigin,
    title: "Active B",
    filename: "active-b.pdf",
    source_object_key: doubleSource,
    reason: "successful_download",
  };
  let rebuiltB = null;
  doubleRecoveryBucket.getCalls.length = 0;
  doubleRecoveryBucket.beforeGet = async (key, bucket) => {
    const priorItemReads = bucket.getCalls.filter((candidate) => candidate === doubleItemKey).length;
    if (key !== doubleItemKey || priorItemReads !== 1) return;
    bucket.beforeGet = null;
    assert.equal(
      await api.deleteHotReportArchive({ REPORT_BUCKET: bucket }, staleRowA, {
        expectedStaleEtag: staleEtagA,
        expectedStaleGeneration: staleGenerationA,
      }),
      true,
      "W2 must win the stale-generation CAS and finish A",
    );
    rebuiltB = await api.archiveReportAsHot({ REPORT_BUCKET: bucket }, doubleInput);
  };
  await assert.rejects(
    api.archiveReportAsHot({ REPORT_BUCKET: doubleRecoveryBucket }, doubleInput),
    /retention cleanup is in progress/,
    "W1 must stop when its stale A fence now resolves to rebuilt active B",
  );
  assert.ok(rebuiltB);
  const activeBRow = await readJson(doubleRecoveryBucket, doubleItemKey);
  const activeBPdf = await doubleRecoveryBucket.head(doublePdfKey);
  assert.equal(activeBRow.retention_state, "active");
  assert.notEqual(activeBRow.retention_generation, staleGenerationA);
  assert.ok(activeBPdf, "the losing W1 invocation must not delete B's PDF");
  assert.equal(activeBRow.pdf_etag, activeBPdf.etag);

  const emptyFenceBucket = new MockR2Bucket();
  const emptyFenceId = "hot:7878787878787878";
  const emptyFencePdf = api.hotReportPdfKey(emptyFenceId);
  const emptyFenceRow = {
    id: emptyFenceId,
    source: "hot",
    origin_source: "catalog",
    origin_report_id: "7878787878787878",
    title: "Empty stale fence",
    filename: "empty-fence.pdf",
    hot_added_at: "2026-01-01T00:00:00.000Z",
    created_at: "2026-01-01T00:00:00.000Z",
    deleting_at: "2026-01-01T00:00:00.000Z",
    retention_state: "deleting",
    retention_generation: "7878787878787878",
  };
  await emptyFenceBucket.put(emptyFencePdf, new Uint8Array([37, 80, 68, 70, 45]));
  await putJson(emptyFenceBucket, api.hotReportItemKey(emptyFenceId), emptyFenceRow);
  emptyFenceBucket.deleteCalls.length = 0;
  assert.equal(
    await api.deleteHotReportArchive({ REPORT_BUCKET: emptyFenceBucket }, emptyFenceRow, {
      expectedStaleEtag: "",
      expectedStaleGeneration: emptyFenceRow.retention_generation,
    }),
    false,
    "an explicitly empty stale ETag must fail closed instead of degrading into an unfenced deletion",
  );
  assert.ok(await emptyFenceBucket.head(emptyFencePdf));
  assert.equal(emptyFenceBucket.deleteCalls.length, 0);

  const reactivationBucket = new MockR2Bucket();
  const reactivationOrigin = "eeeeeeeeeeeeeeee";
  const reactivationSource = "reports/eeeeeeeeeeeeeeee.pdf";
  await reactivationBucket.put(reactivationSource, new Uint8Array([37, 80, 68, 70, 45]));
  const reactivationInput = {
    origin_source: "catalog",
    origin_report_id: reactivationOrigin,
    title: "Popular again",
    filename: "popular-again.pdf",
    source_object_key: reactivationSource,
    reason: "successful_download",
  };
  const beforePrune = await api.archiveReportAsHot({ REPORT_BUCKET: reactivationBucket }, reactivationInput);
  assert.equal(await api.deleteHotReportArchive({ REPORT_BUCKET: reactivationBucket }, beforePrune.row), true);
  assert.equal(
    (await readJson(reactivationBucket, api.hotReportItemKey(beforePrune.item.id))).retention_state,
    "deleted",
  );
  const afterPrune = await api.archiveReportAsHot({ REPORT_BUCKET: reactivationBucket }, reactivationInput);
  assert.equal(afterPrune.item.id, beforePrune.item.id);
  assert.equal(
    (await readJson(reactivationBucket, api.hotReportItemKey(afterPrune.item.id))).retention_state,
    "active",
    "a later successful download may safely reactivate a fully deleted generation",
  );
  assert.ok(await reactivationBucket.head(api.hotReportPdfKey(afterPrune.item.id)));

  const listingBucket = new MockR2Bucket();
  for (let index = 0; index < 520; index += 1) {
    const slug = index.toString(16).padStart(16, "0");
    const id = `hot:${slug}`;
    await listingBucket.put(api.hotReportPdfKey(id), new Uint8Array([37]));
    await putJson(listingBucket, api.hotReportItemKey(id), {
      id,
      source: "hot",
      title: `Report ${index}`,
      filename: `${index}.pdf`,
      sort_order: index,
      hot_added_at: "2026-01-01T00:00:00.000Z",
      created_at: "2026-01-01T00:00:00.000Z",
      retention_state: "active",
    });
  }
  listingBucket.getCalls.length = 0;
  const publicRows = await api.listHotReportRows({ REPORT_BUCKET: listingBucket });
  assert.equal(publicRows.length, 500);
  assert.equal(
    listingBucket.getCalls.filter((key) => key.startsWith("_hot-reports/items/")).length,
    500,
    "public listing must fetch metadata only for its bounded PDF candidates",
  );
  listingBucket.getCalls.length = 0;
  const storageStats = await api.hotReportStorageStats({ REPORT_BUCKET: listingBucket });
  assert.equal(storageStats.pdf_count, 520);
  assert.equal(listingBucket.getCalls.length, 0, "storage stats must not scan item JSON objects");

  const boundedCleanup = await api.enforceHotReportStorageLimit({
    REPORT_BUCKET: listingBucket,
    HOT_REPORT_STORAGE_LIMIT_BYTES: 1,
  });
  assert.equal(
    boundedCleanup.pruned_count,
    250,
    "one retention invocation must stay below the Worker subrequest budget",
  );
  assert.equal(boundedCleanup.cleanup_incomplete, true);
  assert.ok(boundedCleanup.total_size_bytes > 1, "later cron runs must continue bounded cleanup");

  console.log("portal hot-report automatic archival tests passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
