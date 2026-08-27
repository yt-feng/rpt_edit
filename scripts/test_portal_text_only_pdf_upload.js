const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");

function extractFunction(source, name) {
  const syncNeedle = `function ${name}(`;
  const asyncNeedle = `async function ${name}(`;
  const asyncStart = source.indexOf(asyncNeedle);
  const syncStart = source.indexOf(syncNeedle);
  const start = asyncStart >= 0 ? asyncStart : syncStart;
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

function pdfFile({ name = "history.pdf", type = "application/pdf", bytes = "%PDF-1.7\n" } = {}) {
  const data = Buffer.from(bytes);
  return {
    name,
    type,
    size: data.length,
    async arrayBuffer() {
      return data.buffer.slice(data.byteOffset, data.byteOffset + data.byteLength);
    },
    slice(start, end) {
      const part = data.subarray(start, end);
      return {
        async arrayBuffer() {
          return part.buffer.slice(part.byteOffset, part.byteOffset + part.byteLength);
        },
      };
    },
  };
}

function requestWith(role, fields = {}) {
  return {
    role,
    async formData() {
      return { get: (key) => fields[key] };
    },
  };
}

function createBucket(options = {}) {
  const objects = new Map();
  const deletes = [];
  let etagCounter = 0;
  return {
    objects,
    deletes,
    options,
    async head(key) {
      if (options.failHeadKeys && options.failHeadKeys.has(key)) throw new Error("mock HEAD failed");
      const object = objects.get(key);
      if (!object) return null;
      return {
        key,
        size: object.size,
        etag: object.etag,
        customMetadata: object.customMetadata || {},
      };
    },
    async get(key) {
      const object = objects.get(key);
      if (!object) return null;
      return {
        key,
        size: object.size,
        etag: object.etag,
        customMetadata: object.customMetadata || {},
        body: object.body,
        async text() { return String(object.body || ""); },
      };
    },
    async put(key, value, putOptions = {}) {
      if (putOptions.onlyIf && putOptions.onlyIf.etagDoesNotMatch === "*" && objects.has(key)) return null;
      if (
        putOptions.onlyIf
        && putOptions.onlyIf.etagMatches
        && (!objects.has(key) || objects.get(key).etag !== String(putOptions.onlyIf.etagMatches))
      ) return null;
      if (options.metadataConflict && key.startsWith("_catalog-pdf-overrides/items/")) return null;
      if (options.metadataFailure && key.startsWith("_catalog-pdf-overrides/items/")) throw new Error("metadata write failed");
      etagCounter += 1;
      const isPdf = key.endsWith(".pdf");
      const body = isPdf ? value : String(value);
      const size = isPdf ? Number(value.size || 0) : Buffer.byteLength(body);
      const object = {
        key,
        body,
        size,
        etag: `etag-${etagCounter}`,
        customMetadata: putOptions.customMetadata || {},
      };
      objects.set(key, object);
      if (options.invalidateAfterOverrideCommit && key.startsWith("_catalog-pdf-overrides/items/")) {
        const hotKey = [...objects.keys()].find((candidate) => candidate.startsWith("_hot-reports/items/"));
        if (hotKey) {
          const hotObject = objects.get(hotKey);
          hotObject.body = JSON.stringify({ ...JSON.parse(hotObject.body), retention_state: "deleting" });
          hotObject.etag = `etag-${++etagCounter}`;
        }
      }
      return object;
    },
    async delete(key) {
      deletes.push(key);
      objects.delete(key);
    },
    async list({ prefix }) {
      return {
        objects: [...objects.keys()].filter((key) => key.startsWith(prefix)).map((key) => ({ key })),
        truncated: false,
      };
    },
  };
}

const sandbox = {
  Buffer,
  console,
  result: null,
};

vm.runInNewContext(`
  const CATALOG_PDF_OVERRIDE_PREFIX = "_catalog-pdf-overrides";
  const CATALOG_PDF_OVERRIDE_ITEM_PREFIX = CATALOG_PDF_OVERRIDE_PREFIX + "/items";
  const CATALOG_PDF_OVERRIDE_PDF_PREFIX = CATALOG_PDF_OVERRIDE_PREFIX + "/pdfs";
  const CATALOG_PDF_OVERRIDE_MAX_BYTES = 95 * 1024 * 1024;
  const CATALOG_PDF_OVERRIDE_MAX_ITEMS = 5000;
  const CATALOG_PDF_OVERRIDE_HEAD_CONCURRENCY = 20;
  const HOT_REPORT_PREFIX = "_hot-reports";
  const HOT_REPORT_ITEM_PREFIX = HOT_REPORT_PREFIX + "/items";
  const HOT_REPORT_PDF_PREFIX = HOT_REPORT_PREFIX + "/pdfs";
  const HOT_REPORT_ID_PATTERN = /^hot:[a-f0-9]{16}$/;
  const THINKTANK_SOURCE = "thinktank";
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  let randomHexCounter = 0;
  function randomHex() { randomHexCounter += 1; return randomHexCounter.toString(16).padStart(16, "0"); }
  function objectKeyForReport(_env, report) { return "reports/" + report.id + ".pdf"; }
  let uploadCounter = 0;
  function cleanAdminUploadId(value) {
    const id = String(value || "").trim().toLowerCase();
    return /^upload-[a-f0-9]{32,64}$/.test(id) ? id : "";
  }
  function requestedAdminUploadId(_request, _form, fallback = "") {
    if (fallback) return fallback;
    uploadCounter += 1;
    return "upload-" + uploadCounter.toString(16).padStart(32, "0");
  }
  function requestedAdminUploadFingerprint() { return ""; }
  async function reserveAdminUpload(_env, uploadId, kind) {
    return {
      action: "reserved",
      uploadId,
      owner: "owner-" + uploadId,
      record: { upload_id: uploadId, kind, status: "validating", stage: "validating" },
      startedAt: Date.now(),
    };
  }
  async function acquireCatalogPdfOverrideLock() { return null; }
  function adminUploadReplayResponse() { return null; }
  async function updateAdminUploadRecord(_env, reservation, status, fields = {}) {
    reservation.record = { ...reservation.record, ...fields, status, stage: fields.stage || status };
    return reservation.record;
  }
  async function failAdminUploadRecord(_env, reservation, error, stage = "failed") {
    if (!reservation) return null;
    reservation.record = {
      ...reservation.record,
      status: "failed",
      stage,
      detail: String(error && error.message || error || "failed"),
    };
    return reservation.record;
  }
  async function completeAdminUploadRecord(_env, reservation, result) {
    const record = await updateAdminUploadRecord(_env, reservation, "completed", {
      stage: "completed",
      result,
    });
    return { record, persisted: true };
  }
  async function repairAdminUploadCompletion() { return null; }
  function publicAdminUpload(value) { return value || null; }
  function scheduleAdminUploadMaintenance() { return Promise.resolve([]); }
  function findReport(catalog, id) { return (catalog.items || []).find((item) => item.id === id); }
  function jsonResponse(_request, _env, status, body) { return { status, body }; }
  async function requireSuperUser(request) {
    if (request.role !== "super") throw new Error("Only the admin account can access this area.");
    return { username: "admin-a", email: "admin-a@users.portal.example.invalid", role: "super" };
  }
  async function loadCatalog() {
    return { items: [
      { id: "aaaaaaaaaaaaaaaa", title: "History", filename: "History.pdf", available: false },
      { id: "bbbbbbbbbbbbbbbb", title: "Live", filename: "Live.pdf", available: true },
    ] };
  }
  async function r2GetJsonStrict(env, key) {
    const object = await env.REPORT_BUCKET.get(key);
    return object ? JSON.parse(await object.text()) : null;
  }
  async function r2GetJsonObjectStrict(env, key) {
    const object = await env.REPORT_BUCKET.get(key);
    return object ? { object, value: JSON.parse(await object.text()) } : null;
  }
  async function persistAnalyticsEvent() { return null; }
  async function enforceHotReportStorageLimit(env) {
    if (env.REPORT_BUCKET.options.invalidateDuringRetention) {
      const hotKey = [...env.REPORT_BUCKET.objects.keys()].find((key) => key.startsWith("_hot-reports/items/"));
      const object = hotKey && env.REPORT_BUCKET.objects.get(hotKey);
      if (object) {
        object.body = JSON.stringify({ ...JSON.parse(object.body), retention_state: "deleting" });
        object.etag = "retention-race-etag";
      }
    }
    return { pruned_count: 0 };
  }
  function catalogReportHotArchiveInput(report, descriptor, reason) {
    return {
      origin_source: "catalog",
      origin_report_id: report.id,
      title: report.title,
      filename: descriptor.filename,
      size_bytes: descriptor.size_bytes,
      reason,
    };
  }
  async function archiveReportAsHot(env, input) {
    const id = "hot:0123456789abcdef";
    const pdfKey = "_hot-reports/pdfs/0123456789abcdef.pdf";
    const now = "2026-08-02T00:00:00.000Z";
    let object = await env.REPORT_BUCKET.head(pdfKey);
    if (
      !object
      || object.customMetadata.source !== "catalog-pdf-override"
      || object.customMetadata.upload_id !== input.pdf_custom_metadata.upload_id
      || object.customMetadata.version !== input.pdf_custom_metadata.version
    ) {
      const generation = randomHex();
      await env.REPORT_BUCKET.put(pdfKey, input.body, {
        onlyIf: object ? { etagMatches: object.etag } : { etagDoesNotMatch: "*" },
        customMetadata: {
          ...(input.pdf_custom_metadata || {}),
          source: "catalog-pdf-override",
          report_id: input.origin_report_id,
          hot_report_id: id,
          origin_source: "catalog",
          origin_report_id: input.origin_report_id,
          archive_generation: generation,
        },
      });
      object = await env.REPORT_BUCKET.head(pdfKey);
    }
    const row = {
      id,
      source: "hot",
      title: input.title,
      filename: input.filename,
      size_bytes: object.size,
      hot_added_at: now,
      created_at: now,
      updated_at: now,
      retention_state: "active",
      archive_generation: object.customMetadata.archive_generation,
      pdf_etag: object.etag,
      origin_source: "catalog",
      origin_report_id: input.origin_report_id,
      catalog_pdf_override_id: input.catalog_pdf_override_id,
    };
    const hotItemKey = "_hot-reports/items/0123456789abcdef.json";
    const existingHot = await env.REPORT_BUCKET.head(hotItemKey);
    await env.REPORT_BUCKET.put(hotItemKey, JSON.stringify(row), {
      onlyIf: existingHot ? { etagMatches: existingHot.etag } : { etagDoesNotMatch: "*" },
    });
    return { created: true, item: { id, title: row.title }, row, pdf_key: pdfKey, pdf_object: object };
  }
  async function mapWithConcurrency(rows, _concurrency, mapper) { return Promise.all(rows.map(mapper)); }
  async function listR2JsonObjects(env, prefix) {
    const listed = await env.REPORT_BUCKET.list({ prefix });
    return Promise.all(listed.objects.map(async (object) => r2GetJsonStrict(env, object.key)));
  }
  ${extractFunction(worker, "safeFilename")}
  ${extractFunction(worker, "safePdfFilename")}
  ${extractFunction(worker, "asciiFilename")}
  ${extractFunction(worker, "contentDisposition")}
  ${extractFunction(worker, "cleanCatalogReportId")}
  ${extractFunction(worker, "cleanHotReportId")}
  ${extractFunction(worker, "hotReportSlug")}
  ${extractFunction(worker, "hotReportItemKey")}
  ${extractFunction(worker, "hotReportPdfKey")}
  ${extractFunction(worker, "hotReportPdfObjectMatchesOrigin")}
  ${extractFunction(worker, "cleanHotReportText")}
  ${extractFunction(worker, "cleanHotReportOriginSource")}
  ${extractFunction(worker, "cleanHotReportOriginId")}
  ${extractFunction(worker, "hotReportArchiveGeneration")}
  ${extractFunction(worker, "catalogPdfOverrideItemKey")}
  ${extractFunction(worker, "catalogPdfOverridePdfKey")}
  ${extractFunction(worker, "catalogPdfOverrideStoredObjectKey")}
  ${extractFunction(worker, "validateCatalogPdfOverride")}
  ${extractFunction(worker, "validateCatalogPdfOverrideDeleted")}
  ${extractFunction(worker, "catalogPdfOverrideDeletedRow")}
  ${extractFunction(worker, "catalogPdfOverrideTombstoneMatchesArchive")}
  ${extractFunction(worker, "catalogPdfOverrideObjectMatches")}
  ${extractFunction(worker, "catalogOverridePdfObjectMatches")}
  ${extractFunction(worker, "catalogPdfOverrideArchiveMatches")}
  ${extractFunction(worker, "readCatalogPdfOverride")}
  ${extractFunction(worker, "inspectCatalogPdfOverride")}
  ${extractFunction(worker, "catalogPdfOverrideCommitMatches")}
  ${extractFunction(worker, "verifyCatalogPdfOverrideCommit")}
  ${extractFunction(worker, "cleanupCatalogPdfOverrideCommit")}
  ${extractFunction(worker, "publicCatalogPdfOverride")}
  ${extractFunction(worker, "handleCatalogPdfOverrides")}
  ${extractFunction(worker, "handleAccountAdminTextOnlyPdf")}
  api = {
    handleAccountAdminTextOnlyPdf,
    handleCatalogPdfOverrides,
    readCatalogPdfOverride,
    validateCatalogPdfOverride,
    cleanupCatalogPdfOverrideCommit,
  };
`, sandbox);

const {
  handleAccountAdminTextOnlyPdf,
  handleCatalogPdfOverrides,
  readCatalogPdfOverride,
  validateCatalogPdfOverride,
  cleanupCatalogPdfOverrideCommit,
} = sandbox.api;

async function upload(bucket, role = "super", fields = {}) {
  const request = requestWith(role, {
    id: "aaaaaaaaaaaaaaaa",
    pdf: pdfFile(),
    ...fields,
  });
  return handleAccountAdminTextOnlyPdf(request, { REPORT_BUCKET: bucket });
}

(async () => {
  for (const role of ["anonymous", "operator", "normal", "master"]) {
    const response = await upload(createBucket(), role);
    assert.equal(response.status, 403, `${role} must not upload a Text only PDF`);
  }

  assert.equal((await upload(createBucket(), "super", { id: "bad" })).status, 400);
  assert.equal((await upload(createBucket(), "super", { id: "cccccccccccccccc" })).status, 404);
  const liveBucket = createBucket();
  await liveBucket.put("reports/bbbbbbbbbbbbbbbb.pdf", pdfFile());
  assert.equal((await upload(liveBucket, "super", { id: "bbbbbbbbbbbbbbbb" })).status, 409);
  assert.equal((await upload(createBucket(), "super", {
    pdf: pdfFile({ name: "wrong.txt", type: "text/plain" }),
  })).status, 400);
  assert.equal((await upload(createBucket(), "super", {
    pdf: pdfFile({ name: "wrong.pdf", bytes: "not a pdf" }),
  })).status, 400);
  assert.equal((await upload(createBucket(), "super", {
    pdf: { ...pdfFile(), size: 0 },
  })).status, 413);
  assert.equal((await upload(createBucket(), "super", {
    pdf: { ...pdfFile(), size: 95 * 1024 * 1024 + 1 },
  })).status, 413);

  const bucket = createBucket();
  const success = await upload(bucket);
  assert.equal(success.status, 201);
  assert.equal(success.body.ok, true);
  assert.deepEqual(
    Object.keys(success.body.item).sort(),
    ["available", "id", "manual_pdf", "size_bytes", "uploaded_at"].sort(),
    "upload response must expose only public override fields",
  );
  assert.equal(success.body.hot_report.id, "hot:0123456789abcdef");
  assert.equal([...bucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 1);
  assert.equal([...bucket.objects.keys()].filter((key) => key.includes("/items/")).length, 2);
  assert.equal((await upload(bucket)).status, 409, "a second upload must not overwrite the first PDF");

  const verified = await readCatalogPdfOverride(
    { REPORT_BUCKET: bucket },
    "aaaaaaaaaaaaaaaa",
    { verifyObject: true },
  );
  assert.ok(verified && verified.object, "override metadata and PDF must read back together");
  const verifiedRow = verified.row;
  assert.throws(
    () => validateCatalogPdfOverride({ ...verifiedRow, hot_report_generation: "" }, verifiedRow.id),
    /verification failed/,
    "a hot-linked override must carry its exact archive generation",
  );
  assert.throws(
    () => validateCatalogPdfOverride({
      ...verifiedRow,
      hot_report_id: "",
      object_key: `_catalog-pdf-overrides/pdfs/${verifiedRow.id}/${verifiedRow.version}.pdf`,
    }, verifiedRow.id),
    /verification failed/,
    "an override generation must never be accepted without a hot-report identity",
  );

  const publicList = await handleCatalogPdfOverrides({}, { REPORT_BUCKET: bucket });
  assert.equal(publicList.status, 200);
  assert.equal(publicList.body.total, 1);
  const publicText = JSON.stringify(publicList.body);
  for (const secretField of ["uploaded_by", "object_key", "hot_report_id", "etag", "version"]) {
    assert.ok(!publicText.includes(secretField), `public override list must not expose ${secretField}`);
  }

  const missingObjectBucket = createBucket();
  await upload(missingObjectBucket);
  const pdfKey = [...missingObjectBucket.objects.keys()].find((key) => key.includes("/pdfs/"));
  missingObjectBucket.objects.delete(pdfKey);
  const missingList = await handleCatalogPdfOverrides({}, { REPORT_BUCKET: missingObjectBucket });
  assert.equal(missingList.body.total, 0, "metadata pointing to a missing PDF must not advertise availability");

  const danglingOverrideBucket = createBucket();
  const danglingFirst = await upload(danglingOverrideBucket);
  assert.equal(danglingFirst.status, 201);
  const danglingItemKey = "_catalog-pdf-overrides/items/aaaaaaaaaaaaaaaa.json";
  const danglingPdfKey = [...danglingOverrideBucket.objects.keys()]
    .find((key) => key.startsWith("_hot-reports/pdfs/"));
  const danglingMetadataEtag = danglingOverrideBucket.objects.get(danglingItemKey).etag;
  danglingOverrideBucket.objects.delete(danglingPdfKey);
  const danglingRecovered = await upload(danglingOverrideBucket);
  assert.equal(
    danglingRecovered.status,
    201,
    "an override whose PDF/archive generation is gone must be repaired instead of returning a permanent 409",
  );
  assert.ok(danglingOverrideBucket.objects.has(danglingPdfKey));
  assert.notEqual(
    danglingOverrideBucket.objects.get(danglingItemKey).etag,
    danglingMetadataEtag,
    "dangling override metadata must be replaced under its prior ETag fence",
  );
  const danglingReplacementPut = [...danglingOverrideBucket.objects.values()]
    .find((object) => object.key === danglingItemKey);
  assert.ok(danglingReplacementPut);

  const malformedOverrideBucket = createBucket();
  await malformedOverrideBucket.put(danglingItemKey, "{not-json");
  const malformedEtag = malformedOverrideBucket.objects.get(danglingItemKey).etag;
  const malformedRecovered = await upload(malformedOverrideBucket);
  assert.equal(malformedRecovered.status, 503, "corrupt override JSON must fail closed instead of being treated as dangling");
  assert.equal(malformedOverrideBucket.objects.get(danglingItemKey).etag, malformedEtag);

  const verificationFailureOptions = { failHeadKeys: new Set() };
  const verificationFailureBucket = createBucket(verificationFailureOptions);
  assert.equal((await upload(verificationFailureBucket)).status, 201);
  const verificationPdfKey = [...verificationFailureBucket.objects.keys()]
    .find((key) => key.startsWith("_hot-reports/pdfs/"));
  const verificationMetadataEtag = verificationFailureBucket.objects.get(danglingItemKey).etag;
  verificationFailureOptions.failHeadKeys.add(verificationPdfKey);
  const verificationFailure = await upload(verificationFailureBucket);
  assert.equal(verificationFailure.status, 503, "storage verification errors must fail closed instead of triggering repair");
  assert.equal(verificationFailureBucket.objects.get(danglingItemKey).etag, verificationMetadataEtag);

  const tombstoneRecoveryBucket = createBucket();
  assert.equal((await upload(tombstoneRecoveryBucket)).status, 201);
  const oldMetadataObject = await tombstoneRecoveryBucket.get(danglingItemKey);
  const oldMetadataRow = JSON.parse(await oldMetadataObject.text());
  assert.equal(
    await cleanupCatalogPdfOverrideCommit(
      { REPORT_BUCKET: tombstoneRecoveryBucket },
      oldMetadataRow,
      oldMetadataObject.etag,
    ),
    true,
  );
  const cleanupTombstoneObject = await tombstoneRecoveryBucket.get(danglingItemKey);
  assert.equal(JSON.parse(await cleanupTombstoneObject.text()).state, "deleted");
  assert.equal(
    await readCatalogPdfOverride({ REPORT_BUCKET: tombstoneRecoveryBucket }, "aaaaaaaaaaaaaaaa", { verifyObject: true }),
    null,
    "an override cleanup tombstone must be unreadable",
  );
  assert.equal(
    (await upload(tombstoneRecoveryBucket)).status,
    201,
    "a later upload must CAS-replace the cleanup tombstone rather than remain blocked",
  );
  const replacementMetadataObject = await tombstoneRecoveryBucket.get(danglingItemKey);
  const replacementMetadataRow = JSON.parse(await replacementMetadataObject.text());
  assert.notEqual(replacementMetadataObject.etag, cleanupTombstoneObject.etag);
  assert.notEqual(replacementMetadataRow.state, "deleted");
  assert.equal(
    await cleanupCatalogPdfOverrideCommit(
      { REPORT_BUCKET: tombstoneRecoveryBucket },
      oldMetadataRow,
      oldMetadataObject.etag,
    ),
    true,
    "an old cleanup retry must stop at the metadata ETag mismatch",
  );
  assert.equal(
    (await tombstoneRecoveryBucket.get(danglingItemKey)).etag,
    replacementMetadataObject.etag,
    "old cleanup must not tombstone the newer successful metadata commit",
  );
  assert.equal(tombstoneRecoveryBucket.deletes.filter((key) => key === danglingItemKey).length, 0);

  const commitRaceBucket = createBucket({ invalidateAfterOverrideCommit: true });
  const commitRace = await upload(commitRaceBucket);
  assert.equal(commitRace.status, 503, "a deletion fence racing the override commit must prevent a false 201");
  assert.equal(JSON.parse(commitRaceBucket.objects.get(danglingItemKey).body).state, "deleted");
  assert.equal(
    await readCatalogPdfOverride({ REPORT_BUCKET: commitRaceBucket }, "aaaaaaaaaaaaaaaa", { verifyObject: true }),
    null,
    "a failed post-commit generation verification must leave only an unavailable CAS tombstone",
  );
  assert.equal(commitRaceBucket.deletes.filter((key) => key === danglingItemKey).length, 0);

  const retentionRaceBucket = createBucket({ invalidateDuringRetention: true });
  const retentionRace = await upload(retentionRaceBucket);
  assert.equal(retentionRace.status, 201, "retention is deferred and must not delay or invalidate the core response");
  assert.notEqual(JSON.parse(retentionRaceBucket.objects.get(danglingItemKey).body).state, "deleted");
  assert.equal(retentionRaceBucket.deletes.filter((key) => key === danglingItemKey).length, 0);

  const conflictBucket = createBucket({ metadataConflict: true });
  const conflict = await upload(conflictBucket);
  assert.equal(conflict.status, 409);
  assert.equal([...conflictBucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 1);
  assert.equal([...conflictBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/items/")).length, 1);
  assert.equal([...conflictBucket.objects.keys()].filter((key) => key.startsWith("_catalog-pdf-overrides/items/")).length, 0);

  const failureOptions = { metadataFailure: true };
  const failureBucket = createBucket(failureOptions);
  const failure = await upload(failureBucket);
  assert.equal(failure.status, 503);
  assert.equal([...failureBucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 1);
  assert.equal([...failureBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/items/")).length, 1);
  assert.equal([...failureBucket.objects.keys()].filter((key) => key.startsWith("_catalog-pdf-overrides/items/")).length, 0);
  const retainedPdfKey = [...failureBucket.objects.keys()].find((key) => key.startsWith("_hot-reports/pdfs/"));
  const retainedVersion = failureBucket.objects.get(retainedPdfKey).customMetadata.version;
  failureOptions.metadataFailure = false;
  const retried = await upload(failureBucket);
  assert.equal(retried.status, 201, "retrying after an override metadata failure must replace the orphan in place");
  assert.equal(
    [...failureBucket.objects.keys()].filter((key) => key.startsWith("_hot-reports/pdfs/")).length,
    1,
    "a retry must keep one deterministic hot PDF key rather than duplicate it",
  );
  const retriedOverrideKey = [...failureBucket.objects.keys()].find((key) => key.startsWith("_catalog-pdf-overrides/items/"));
  const retriedOverride = JSON.parse(failureBucket.objects.get(retriedOverrideKey).body);
  assert.notEqual(retriedOverride.version, retainedVersion, "a retry must bind the newly selected upload version");
  assert.equal(
    retriedOverride.version,
    failureBucket.objects.get(retainedPdfKey).customMetadata.version,
    "override metadata must match the final stored PDF version",
  );

  const download = extractFunction(worker, "handleDownload");
  assert.ok(
    download.indexOf("catalogReportPdfObjectMatches") < download.indexOf("finalizeAccountDownloadDecision"),
    "the PDF object must be verified before a limited download is consumed",
  );
  assert.match(download, /derivedPasswordMatches/);
  assert.match(download, /passwordMatches/);
  assert.match(worker, /pathname === "\/catalog-pdf-overrides"[\s\S]*?handleCatalogPdfOverrides/);
  assert.match(worker, /pathname === "\/account-admin\/text-only-pdf"[\s\S]*?handleAccountAdminTextOnlyPdf/);
  assert.match(extractFunction(worker, "handleAccountAdminTextOnlyPdf"), /requireSuperUser\(request, env\)/);
  assert.doesNotMatch(extractFunction(worker, "handleAccountAdminTextOnlyPdf"), /requireOperationsUser/);

  const uiSandbox = {};
  vm.runInNewContext(`
    ${extractFunction(app, "mergeCatalogPdfOverrides")}
    result = mergeCatalogPdfOverrides([
      { id: "text", available: false, pdf_archived: true, size_bytes: 0 },
      { id: "live", available: true, size_bytes: 10 },
    ], [
      { id: "text", available: true, size_bytes: 42, uploaded_at: "2026-07-26T00:00:00Z" },
      { id: "live", available: true, size_bytes: 999 },
    ]);
  `, uiSandbox);
  assert.equal(uiSandbox.result[0].available, true);
  assert.equal(uiSandbox.result[0].manual_pdf, true);
  assert.equal(uiSandbox.result[0].pdf_archived, false);
  assert.equal(uiSandbox.result[0].size_bytes, 42);
  assert.equal(uiSandbox.result[1].size_bytes, 10, "an override must not replace a normal catalog PDF");
  assert.match(app, /function initTextOnlyPdfUpload\([\s\S]*?isSuperSession\(\)/);
  assert.match(app, /url:\s*`\$\{workerUrl\}\/account-admin\/text-only-pdf`/);
  assert.match(app, /name="pdf"[\s\S]*?accept="application\/pdf,\.pdf"/);
  assert.match(app, /loadCatalogPdfOverrides\(workerUrl\)[\s\S]*?mergeCatalogPdfOverrides/);

  console.log("Portal Suite Text only PDF upload checks passed.");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
