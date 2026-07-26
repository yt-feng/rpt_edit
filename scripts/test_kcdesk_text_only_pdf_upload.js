const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "kc_desk_notes/site_src/assets/app.js"), "utf8");

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
    async head(key) {
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
      if (options.metadataConflict && key.includes("/items/")) return null;
      if (options.metadataFailure && key.includes("/items/")) throw new Error("metadata write failed");
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
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function randomHex() { return "0123456789abcdef"; }
  function findReport(catalog, id) { return (catalog.items || []).find((item) => item.id === id); }
  function jsonResponse(_request, _env, status, body) { return { status, body }; }
  async function requireSuperUser(request) {
    if (request.role !== "super") throw new Error("Only the admin account can access this area.");
    return { username: "twotigers", email: "twotigers@users.kcdesk.com", role: "super" };
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
  async function persistAnalyticsEvent() { return null; }
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
  ${extractFunction(worker, "catalogPdfOverrideItemKey")}
  ${extractFunction(worker, "catalogPdfOverridePdfKey")}
  ${extractFunction(worker, "validateCatalogPdfOverride")}
  ${extractFunction(worker, "catalogPdfOverrideObjectMatches")}
  ${extractFunction(worker, "readCatalogPdfOverride")}
  ${extractFunction(worker, "publicCatalogPdfOverride")}
  ${extractFunction(worker, "handleCatalogPdfOverrides")}
  ${extractFunction(worker, "handleAccountAdminTextOnlyPdf")}
  api = { handleAccountAdminTextOnlyPdf, handleCatalogPdfOverrides, readCatalogPdfOverride };
`, sandbox);

const { handleAccountAdminTextOnlyPdf, handleCatalogPdfOverrides, readCatalogPdfOverride } = sandbox.api;

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
  assert.equal((await upload(createBucket(), "super", { id: "bbbbbbbbbbbbbbbb" })).status, 409);
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
  assert.equal([...bucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 1);
  assert.equal([...bucket.objects.keys()].filter((key) => key.includes("/items/")).length, 1);
  assert.equal((await upload(bucket)).status, 409, "a second upload must not overwrite the first PDF");

  const verified = await readCatalogPdfOverride(
    { REPORT_BUCKET: bucket },
    "aaaaaaaaaaaaaaaa",
    { verifyObject: true },
  );
  assert.ok(verified && verified.object, "override metadata and PDF must read back together");

  const publicList = await handleCatalogPdfOverrides({}, { REPORT_BUCKET: bucket });
  assert.equal(publicList.status, 200);
  assert.equal(publicList.body.total, 1);
  const publicText = JSON.stringify(publicList.body);
  for (const secretField of ["uploaded_by", "object_key", "etag", "version"]) {
    assert.ok(!publicText.includes(secretField), `public override list must not expose ${secretField}`);
  }

  const missingObjectBucket = createBucket();
  await upload(missingObjectBucket);
  const pdfKey = [...missingObjectBucket.objects.keys()].find((key) => key.includes("/pdfs/"));
  missingObjectBucket.objects.delete(pdfKey);
  const missingList = await handleCatalogPdfOverrides({}, { REPORT_BUCKET: missingObjectBucket });
  assert.equal(missingList.body.total, 0, "metadata pointing to a missing PDF must not advertise availability");

  const conflictBucket = createBucket({ metadataConflict: true });
  const conflict = await upload(conflictBucket);
  assert.equal(conflict.status, 409);
  assert.equal([...conflictBucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 0);

  const failureBucket = createBucket({ metadataFailure: true });
  const failure = await upload(failureBucket);
  assert.equal(failure.status, 503);
  assert.equal([...failureBucket.objects.keys()].filter((key) => key.includes("/pdfs/")).length, 0);

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
  assert.match(app, /fetch\(`\$\{workerUrl\}\/account-admin\/text-only-pdf`/);
  assert.match(app, /name="pdf"[\s\S]*?accept="application\/pdf,\.pdf"/);
  assert.match(app, /loadCatalogPdfOverrides\(workerUrl\)[\s\S]*?mergeCatalogPdfOverrides/);

  console.log("KCdesk Text only PDF upload checks passed.");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
