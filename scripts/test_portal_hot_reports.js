const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const indexHtml = fs.readFileSync(path.join(root, "portal_suite/site_src/index.html"), "utf8");
const styles = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/styles.css"), "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
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

function extractAsyncFunction(source, name) {
  return `async ${extractFunction(source, name)}`;
}

const planDefinitions = worker.match(/const VID2PPT_PORTAL_GIFT_PLANS = \{[\s\S]*?\n\};/);
assert.ok(planDefinitions, "Vid2PPT plan definitions must exist");
const publicBrandDefinition = worker.match(/^const PUBLIC_BRAND = .*;$/m);
const publicSourceBrandPatternDefinition = worker.match(/^const PUBLIC_SOURCE_BRAND_PATTERN = .*;$/m);
const publicSourceBrandDetectorDefinition = worker.match(/^const PUBLIC_SOURCE_BRAND_DETECTOR = .*;$/m);
assert.ok(publicBrandDefinition, "public brand definition must exist");
assert.ok(publicSourceBrandPatternDefinition, "public source-brand pattern must exist");
assert.ok(publicSourceBrandDetectorDefinition, "public source-brand detector must exist");

const accessSandbox = {};
vm.runInNewContext(`
  const TRIAL_3D_DOWNLOAD_LIMIT = 10;
  ${planDefinitions[0]}
  const HOT_REPORT_MIN_MONTHS = 3;
  function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
  ${extractFunction(worker, "hotReportPlanMonths")}
  ${extractFunction(worker, "hotReportAccessMonths")}
  ${extractFunction(worker, "hotReportAccessQualifies")}

  const activeAccess = (overrides = {}) => ({ active: true, lifetime: false, ...overrides });
  const accessResult = (kind, effective, entitlement = {}) => ({
    effective_access_kind: kind,
    effective_access: activeAccess(effective),
    entitlement: { active: true, plan: "annual", ...entitlement },
  });
  const staleQuarterEntitlement = { active: true, plan: "annual", source_plan_code: "NOVA-Q" };
  result = {
    adminOneMonthWithStaleQuarter: accessResult(
      "admin",
      { source: "stored", duration_value: "1", source_plan_code: "NOVA-Q" },
      staleQuarterEntitlement,
    ),
    adminThreeMonths: accessResult("admin", { source: "stored", duration_value: "3" }),
    adminLifetime: accessResult("admin", { source: "stored", duration_value: "", lifetime: true }),
    novaMonth: accessResult("entitlement", { source: "vid2ppt_nova", source_plan_code: "NOVA-M" }, { source_plan_code: "NOVA-M" }),
    novaQuarter: accessResult("entitlement", { source: "vid2ppt_nova", source_plan_code: "NOVA-Q" }, { source_plan_code: "NOVA-Q" }),
    novaYear: accessResult("entitlement", { source: "vid2ppt_nova", source_plan_code: "NOVA-Y" }, { source_plan_code: "NOVA-Y" }),
    legacyAnnual: accessResult("entitlement", { source: "entitlement", source_plan_code: "", duration_value: "" }, { source_plan_code: "", plan: "annual" }),
  };
  for (const [key, value] of Object.entries(result)) {
    value.months = hotReportAccessMonths(value);
    value.qualifies = hotReportAccessQualifies({}, value);
  }
  privilegedQualifies = hotReportAccessQualifies({ privileged: true }, {
    effective_access_kind: "none",
    effective_access: { active: false },
    entitlement: { active: false },
  });
`, accessSandbox);

assert.equal(accessSandbox.result.adminOneMonthWithStaleQuarter.months, 1);
assert.equal(
  accessSandbox.result.adminOneMonthWithStaleQuarter.qualifies,
  false,
  "an authoritative one-month administrator grant must not inherit a stale NOVA-Q entitlement",
);
assert.equal(accessSandbox.result.adminThreeMonths.months, 3);
assert.equal(accessSandbox.result.adminThreeMonths.qualifies, true);
assert.equal(accessSandbox.result.adminLifetime.months, Number.POSITIVE_INFINITY);
assert.equal(accessSandbox.result.adminLifetime.qualifies, true);
assert.equal(accessSandbox.result.novaMonth.months, 1);
assert.equal(accessSandbox.result.novaMonth.qualifies, false, "NOVA-M must not unlock hot reports");
assert.equal(accessSandbox.result.novaQuarter.months, 3);
assert.equal(accessSandbox.result.novaQuarter.qualifies, true, "NOVA-Q must unlock hot reports");
assert.equal(accessSandbox.result.novaYear.months, 12);
assert.equal(accessSandbox.result.novaYear.qualifies, true, "NOVA-Y must unlock hot reports");
assert.equal(accessSandbox.result.legacyAnnual.months, 12);
assert.equal(accessSandbox.result.legacyAnnual.qualifies, true, "legacy annual memberships must remain eligible");
assert.equal(accessSandbox.privilegedQualifies, true, "privileged accounts must remain eligible");

const searchSandbox = {};
vm.runInNewContext(`
  const input = { value: "definitely-no-match" };
  const searchRecommendationsSection = { hidden: false };
  const searchRecommendationsResults = { innerHTML: "stale" };
  const searchRecommendationsCount = { textContent: "stale" };
  const fallbackRecommendations = [{ id: "latest-report" }];
  let searchResultCounts = {};
  function relatedRow(item) { return "<article>" + item.id + "</article>"; }
  ${extractFunction(app, "renderSearchRecommendations")}

  function renderWith(counts) {
    searchResultCounts = counts;
    searchRecommendationsSection.hidden = false;
    searchRecommendationsResults.innerHTML = "stale";
    searchRecommendationsCount.textContent = "stale";
    renderSearchRecommendations();
    return {
      hidden: searchRecommendationsSection.hidden,
      html: searchRecommendationsResults.innerHTML,
      count: searchRecommendationsCount.textContent,
    };
  }

  result = {
    allFailed: renderWith({ catalog: 0, hot: "error", thinktank: "error", external: "error", reportA: "error", authority: "error" }),
    pending: renderWith({ catalog: 0, hot: 0, thinktank: null, external: 0, reportA: 0, authority: 0 }),
    oneMatch: renderWith({ catalog: 0, hot: 0, thinktank: 0, external: 1, reportA: 0, authority: 0 }),
    allZero: renderWith({ catalog: 0, hot: 0, thinktank: 0, external: 0, reportA: 0, authority: 0 }),
  };
`, searchSandbox);

assert.equal(searchSandbox.result.allFailed.hidden, false, "failed sources must settle so the page can show useful fallback recommendations");
assert.match(searchSandbox.result.allFailed.html, /latest-report/);
assert.equal(searchSandbox.result.pending.hidden, true, "recommendations must wait for every source to settle");
assert.equal(searchSandbox.result.oneMatch.hidden, true, "recommendations must stay hidden when any source has a match");
assert.equal(searchSandbox.result.allZero.hidden, false, "recommendations may render after every source successfully returns zero");
assert.match(searchSandbox.result.allZero.html, /latest-report/);

assert.match(indexHtml, /id="hotReportsSection"[\s\S]*?id="hotReportsResults"/, "the home page must expose the hot-report section");
assert.match(indexHtml, /3个月及以上会员可下载全文/);
assert.match(indexHtml, /id="hotReportsPrev"[\s\S]*?id="hotReportsPageInfo"[\s\S]*?id="hotReportsNext"/, "hot reports must expose accessible page navigation");
assert.match(indexHtml, /id="hotReportsRetry"[\s\S]*?重新加载/, "a failed page request must offer an explicit retry action");
assert.match(app, /fetch\(hotReportRequestUrl\(cleanQuery, cursor\), \{ signal: controller\.signal \}\)/, "the home UI must load indexed hot-report pages");
assert.match(extractFunction(app, "loadAdminHotReports"), /URLSearchParams\(\{ limit: "60" \}\)[\s\S]*?params\.set\("cursor", cursor\)/, "the admin UI must follow every indexed hot-report page");
assert.match(app, /const HOT_REPORT_PAGE_SIZE = 24/, "the home page must request a small first page");
assert.match(app, /controller\.abort\(\);[\s\S]*?5_000/, "the first-page deadline must fail fast instead of waiting twelve seconds");
assert.match(app, /hotReportRetryQuery = cleanQuery[\s\S]*?loadHotReports\(hotReportRetryQuery !== null/, "retry must restart the failed query from page one without reusing a stale cursor");
assert.match(app, /params\.set\("q", query\)/, "hot-report searches must be sent to the server instead of filtering one loaded page");
assert.match(app, /params\.set\("cursor", cursor\)/, "later hot-report pages must use the server cursor");
assert.match(app, /hotReportPages\[hotReportPageIndex \+ 1\][\s\S]*?requestHotReportPage/, "cached previous pages and on-demand next pages must coexist");
assert.match(extractFunction(app, "scheduleHotReportSearch"), /hotReportRequestedQuery !== cleanQuery[\s\S]*?hotReportRequestController\.abort\(\)/, "a changed query must cancel an obsolete hot-report page immediately");
assert.doesNotMatch(extractFunction(app, "requestHotReportPage"), /catch \(error\)[\s\S]*?hotReportItems\.clear\(\)/, "a page request failure must preserve already rendered hot reports");
assert.match(app, /id="accountAdminHotReportForm"[\s\S]*?name="pdf"/, "the admin UI must expose PDF upload fields");
assert.match(app, /url:\s*`\$\{workerUrl\}\/account-admin\/hot-report`/, "the admin upload form must call the protected upload endpoint");
assert.match(app, /hot-reports\/access\?report_id=/, "hot-report detail pages must query the dedicated access endpoint");

const pdfHandler = extractFunction(worker, "handleHotReportPdf");
assert.match(pdfHandler, /const password = String\(payload\.password \|\| ""\)/);
assert.match(pdfHandler, /sharedReportPasswordMatches\(env, id, password\)/);
assert.match(pdfHandler, /Password is incorrect\./);
assert.match(pdfHandler, /const access = await hotReportAccessForUser\(env, user\)/);
assert.match(pdfHandler, /if \(!access\.can_download\)/);
assert.match(pdfHandler, /return jsonResponse\(request, env, 402,/);
const passwordHandler = extractFunction(worker, "handleAdminReportPassword");
assert.match(passwordHandler, /source === HOT_REPORT_SOURCE/);
assert.match(passwordHandler, /password: await derivedReportPassword\(env, id\)/);
assert.match(worker, /pathname === "\/account-admin\/hot-report"[\s\S]*?handleAccountAdminHotReportUpload/);
assert.match(worker, /pathname === "\/hot-reports\/pdf"[\s\S]*?handleHotReportPdf/);
assert.match(
  app,
  /isHotReportItem\(item\)[\s\S]*?Delivery link[\s\S]*?requestExternalPassword\(workerUrl, item\.id, HOT_REPORT_SOURCE\)/,
  "hot-report detail pages must expose administrator delivery links",
);

const publicCommentHandler = extractFunction(worker, "publicHotReportComment");
assert.doesNotMatch(publicCommentHandler, /author_email|author_user_id/, "public comments must not expose private author identifiers");
const commentPostHandler = extractFunction(worker, "handleHotReportComments");
assert.match(commentPostHandler, /user = await currentUserFromRequest\(env, request\)/, "commenting must require a registered session");
assert.match(commentPostHandler, /const isSuper = isSuperAccount\(user\)/);
assert.match(commentPostHandler, /const alias = isSuper \?/, "only super may select an alias");
const commentOrderHandler = extractFunction(worker, "handleHotReportCommentOrder");
assert.match(commentOrderHandler, /await requireSuperUser\(request, env\)/, "only super may reorder comments");
assert.doesNotMatch(commentOrderHandler, /Promise\.all|hotReportCommentKey/, "reordering must not rewrite individual comment objects");
assert.match(
  app,
  /isHotReportItem\(item\)[\s\S]*?\$\{hotReportCommentsMarkup\(\)\}[\s\S]*?\$\{externalRelatedMarkup\(\)\}/,
  "hot-report comments must render before Related Reports",
);
assert.match(
  styles,
  /\.hot-comment-owner-alias\[hidden\][\s\S]*?display:\s*none\s*!important/,
  "author CSS must not override the hidden state of administrator-only comment controls",
);
assert.match(
  app,
  /randomAlias\.addEventListener\("click", \(\) => \{\s*if \(!isSuperSession\(\)\) return;/,
  "the random alias action must re-check the administrator session",
);
assert.match(
  extractFunction(app, "updateMeta"),
  /internalStorageMetadata && internalStorageMetadata\.total_size_bytes[\s\S]*?showInternalStorageMetadata && totalSize/,
  "PDF storage capacity must stay out of the public header",
);
assert.match(
  app,
  /showInternalStorageMetadata = isAdminASession\(\)[\s\S]*?\/internal\/pdf-storage/,
  "only the exact admin-a session may reveal storage capacity",
);
const internalStorageHandler = extractFunction(worker, "handleInternalPdfStorage");
assert.match(
  internalStorageHandler,
  /await requireSuperUser\(request, env\)/,
  "storage capacity must be authorized again by the Worker",
);
assert.match(worker, /pathname === "\/internal\/pdf-storage"[\s\S]*?handleInternalPdfStorage/);

const uploadSandbox = {};
const uploadPromise = vm.runInNewContext(`(async () => {
  const HOT_REPORT_MAX_PDF_BYTES = 95 * 1024 * 1024;
  const HOT_REPORT_SOURCE = "hot";
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function jsonResponse(_request, _env, status, payload) { return { status, payload }; }
  async function requireSuperUser() { return { email: "ADMIN@example.com" }; }
  function randomHex() { return "0123456789abcdef"; }
  async function sha256Hex() { return "0123456789abcdef0123456789abcdef0123456789abcdef0123456789abcdef"; }
  function cleanAdminUploadId(value) {
    const id = String(value || "").trim().toLowerCase();
    return /^upload-[a-f0-9]{32,64}$/.test(id) ? id : "";
  }
  function requestedAdminUploadId(_request, _form, fallback = "") {
    return fallback || "upload-00000000000000000000000000000001";
  }
  function requestedAdminUploadFingerprint() { return ""; }
  async function reserveAdminUpload(_env, uploadId, kind) {
    return {
      action: "reserved",
      uploadId,
      owner: "owner",
      startedAt: Date.now(),
      record: { upload_id: uploadId, kind, status: "validating", stage: "validating" },
    };
  }
  function adminUploadReplayResponse() { return null; }
  async function updateAdminUploadRecord(_env, reservation, status, fields = {}) {
    reservation.record = { ...reservation.record, ...fields, status, stage: fields.stage || status };
    return reservation.record;
  }
  async function failAdminUploadRecord(_env, reservation, error, stage = "failed") {
    if (!reservation) return null;
    reservation.record = { ...reservation.record, status: "failed", stage, detail: String(error && error.message || error) };
    return reservation.record;
  }
  async function completeAdminUploadRecord(_env, reservation, result) {
    const record = await updateAdminUploadRecord(_env, reservation, "completed", { stage: "completed", result });
    return { record, persisted: true };
  }
  function publicAdminUpload(value) { return value || null; }
  function hotReportCleanupEnabled() { return false; }
  function scheduleAdminUploadMaintenance() { return Promise.resolve([]); }
  async function repairAdminUploadCompletion() { return null; }
  async function repairHotReportPublicIndexIfNeeded() { return null; }
  function hotReportPdfKey(id) { return "pdf/" + id; }
  function hotReportItemKey(id) { return "item/" + id; }
  function contentDisposition(filename) { return "attachment; filename=" + filename; }
  async function r2PutJson(env, _key, payload) {
    if (env.failMetadata) throw new Error("metadata failed");
    env.metadataRow = payload;
  }
  async function persistAnalyticsEvent() {}
  async function enforceHotReportStorageLimit() { return { total_size_bytes: 42 }; }
  async function upsertHotReportPublicIndexItem() { return null; }
  async function markHotReportPublicIndexStale() { return null; }
  async function markHotReportPublicIndexStaleForError() { return null; }
  async function r2GetJsonObjectStrict(env, key) {
    const object = await env.REPORT_BUCKET.head(key);
    return object ? { object, value: JSON.parse(String(object.body || "{}")) } : null;
  }
  function publicHotReportItem(row) { return row; }
  ${extractFunction(worker, "safeFilename")}
  ${extractFunction(worker, "safePdfFilename")}
  ${extractFunction(worker, "cleanHotReportText")}
  ${extractAsyncFunction(worker, "handleAccountAdminHotReportUpload")}

  function pdfFile(name, type) {
    return {
      name,
      type,
      size: 42,
      async arrayBuffer() { return new ArrayBuffer(0); },
      slice() {
        return { async arrayBuffer() { return new Uint8Array([37, 80, 68, 70, 45]).buffer; } };
      },
    };
  }
  function requestFor(pdf) {
    const values = new Map([["pdf", pdf], ["title", "Test report"]]);
    return { async formData() { return values; } };
  }
  function testEnv(options = {}) {
    const calls = { puts: [], deletes: [] };
    const objects = new Map();
    const env = {
      failMetadata: Boolean(options.failMetadata),
      calls,
      REPORT_BUCKET: {
        async head(key) { return objects.get(key) || null; },
        async put(key, value, putOptions = {}) {
          if (env.failMetadata && key.startsWith("item/")) throw new Error("metadata failed");
          calls.puts.push([key, value, putOptions]);
          const object = {
            key,
            body: value,
            size: key.startsWith("pdf/") ? Number(value.size || 0) : String(value).length,
            etag: "etag-" + calls.puts.length,
            customMetadata: putOptions.customMetadata || {},
          };
          objects.set(key, object);
          return object;
        },
        async delete(...args) { calls.deletes.push(args); objects.delete(args[0]); },
      },
    };
    return env;
  }

  uploadResults = {};
  uploadResults.wrongMimeEnv = testEnv();
  uploadResults.wrongMime = await handleAccountAdminHotReportUpload(
    requestFor(pdfFile("report.pdf", "text/plain")),
    uploadResults.wrongMimeEnv,
  );
  uploadResults.txtNameEnv = testEnv();
  uploadResults.txtName = await handleAccountAdminHotReportUpload(
    requestFor(pdfFile("report.txt", "application/pdf")),
    uploadResults.txtNameEnv,
  );
  uploadResults.emptyMimeEnv = testEnv();
  uploadResults.emptyMime = await handleAccountAdminHotReportUpload(
    requestFor(pdfFile("browser-report.pdf", "")),
    uploadResults.emptyMimeEnv,
  );
  uploadResults.emptyMimeTxtEnv = testEnv();
  uploadResults.emptyMimeTxt = await handleAccountAdminHotReportUpload(
    requestFor(pdfFile("browser-report.txt", "")),
    uploadResults.emptyMimeTxtEnv,
  );
  uploadResults.metadataFailureEnv = testEnv({ failMetadata: true });
  uploadResults.metadataFailure = await handleAccountAdminHotReportUpload(
    requestFor(pdfFile("report.pdf", "application/pdf")),
    uploadResults.metadataFailureEnv,
  );
  return uploadResults;
})()
`, uploadSandbox);

const commentOrderSandbox = { URL };
const commentOrderPromise = vm.runInNewContext(`(async () => {
  ${publicBrandDefinition[0]}
  ${publicSourceBrandPatternDefinition[0]}
  ${publicSourceBrandDetectorDefinition[0]}
  const SUPER_ACCOUNT_EMAILS = new Set(["admin@example.com"]);
  const OPERATOR_ACCOUNT_EMAILS = new Set(["operator@example.com"]);
  const HOT_REPORT_ID_PATTERN = /^hot:[a-f0-9]{16}$/;
  const HOT_REPORT_COMMENT_PREFIX = "_hot-reports/comments";
  const HOT_REPORT_COMMENT_ORDER_PREFIX = "_hot-reports/comment-orders";
  const HOT_REPORT_MAX_COMMENTS = 500;
  function jsonResponse(_request, _env, status, payload) { return { status, payload }; }
  async function requireSuperUser() { return { email: "admin@example.com" }; }
  async function currentUserFromRequest() { return { id: "user-id", username: "reader", email: "reader@example.com" }; }
  function accountDisabled() { return false; }
  async function findHotReportRow() { return { item: { id: reportId } }; }
  async function listR2JsonObjects(env) { return env.commentRows; }
  async function safeR2GetJson(env) { return env.manifest || null; }
  async function r2PutJson(env, key, payload) {
    env.putKeys.push(key);
    if (env.failPut) throw new Error("manifest write failed");
    env.manifest = payload;
  }
  ${extractFunction(worker, "cleanHotReportId")}
  ${extractFunction(worker, "hotReportSlug")}
  ${extractFunction(worker, "cleanHotCommentId")}
  ${extractFunction(worker, "hotReportCommentPrefix")}
  ${extractFunction(worker, "hotReportCommentOrderKey")}
  ${extractFunction(worker, "cleanHotReportText")}
  ${extractFunction(worker, "publicBrandInput")}
  ${extractFunction(worker, "publicBrandText")}
  ${extractFunction(worker, "publicAccountDisplayName")}
  ${extractFunction(worker, "publicHotReportDisplayName")}
  ${extractFunction(worker, "hotReportCommentDisplayName")}
  ${extractFunction(worker, "publicHotReportComment")}
  ${extractAsyncFunction(worker, "listHotReportCommentRows")}
  ${extractAsyncFunction(worker, "handleHotReportComments")}
  ${extractAsyncFunction(worker, "handleHotReportCommentOrder")}

  const reportId = "hot:0123456789abcdef";
  const ids = {
    a: "comment:aaaaaaaaaaaaaaaa",
    b: "comment:bbbbbbbbbbbbbbbb",
    c: "comment:cccccccccccccccc",
  };
  function row(id, sortOrder, createdAt) {
    return {
      id,
      report_id: reportId,
      display_name: "User",
      body: id,
      sort_order: sortOrder,
      created_at: createdAt,
      updated_at: createdAt,
      author_email: "private@example.com",
      author_user_id: "private-user-id",
    };
  }
  function envFor(commentRows, orderedIds = null) {
    return {
      commentRows,
      manifest: orderedIds ? { report_id: reportId, ordered_ids: orderedIds, version: 1 } : null,
      putKeys: [],
      failPut: false,
    };
  }
  const baseRows = [
    row(ids.a, 100, "2026-01-01T00:00:00Z"),
    row(ids.b, 200, "2026-01-02T00:00:00Z"),
    row(ids.c, 300, "2026-01-03T00:00:00Z"),
  ];
  const fullEnv = envFor(baseRows, [ids.c, ids.a, ids.b]);
  const full = await listHotReportCommentRows(fullEnv, reportId);
  const legacyEnv = envFor(baseRows);
  const legacy = await listHotReportCommentRows(legacyEnv, reportId);
  const appendedEnv = envFor([
    baseRows[0],
    baseRows[1],
    row(ids.c, 50, "2025-12-31T00:00:00Z"),
  ], [ids.b, ids.a]);
  const appended = await listHotReportCommentRows(appendedEnv, reportId);

  const failureEnv = envFor(baseRows.slice(0, 2), [ids.a, ids.b]);
  failureEnv.failPut = true;
  const beforeRows = JSON.stringify(failureEnv.commentRows);
  const failure = await handleHotReportCommentOrder({
    async json() { return { report_id: reportId, ordered_ids: [ids.b, ids.a] }; },
  }, failureEnv);

  const cappedRows = Array.from({ length: HOT_REPORT_MAX_COMMENTS }, (_, index) => (
    row("comment:" + index.toString(16).padStart(16, "0"), index * 100, "2026-01-01T00:00:00Z")
  ));
  const cappedEnv = envFor(cappedRows);
  const capped = await handleHotReportComments({
    method: "POST",
    url: "https://worker.example/hot-reports/comments",
    async json() { return { report_id: reportId, body: "one too many" }; },
  }, cappedEnv);

  return {
    ids,
    fullIds: full.map((entry) => entry.item.id),
    legacyIds: legacy.map((entry) => entry.item.id),
    appendedIds: appended.map((entry) => entry.item.id),
    failure,
    failurePutKeys: failureEnv.putKeys,
    failureRowsUnchanged: beforeRows === JSON.stringify(failureEnv.commentRows),
    failureManifestIds: failureEnv.manifest.ordered_ids,
    capped,
    cappedPutKeys: cappedEnv.putKeys,
  };
})()
`, commentOrderSandbox);

assert.match(app, /searchResultCounts\.hot = "error"/);
assert.match(app, /searchResultCounts\.hot = Number\.isFinite\(page && page\.total\) \? page\.total : pageItems\.length/);
for (const source of ["thinktank", "external", "reportA", "authority"]) {
  assert.match(app, new RegExp(`searchResultCounts\\.${source} = "error"`), `${source} failures must remain distinguishable from zero results`);
}

Promise.all([uploadPromise, commentOrderPromise]).then(([uploadResults, commentOrderResults]) => {
  assert.equal(uploadResults.wrongMime.status, 400, "a non-PDF MIME type must be rejected");
  assert.equal(uploadResults.wrongMimeEnv.calls.puts.length, 0, "rejected MIME types must not be stored");
  assert.equal(uploadResults.txtName.status, 201);
  assert.equal(uploadResults.txtName.payload.item.filename, "report.txt.pdf", "stored filenames must end in .pdf");
  assert.equal(uploadResults.emptyMime.status, 201, "an empty browser MIME type may be accepted when magic bytes are valid");
  assert.equal(uploadResults.emptyMimeTxt.status, 400, "an empty MIME type also requires an original .pdf filename");
  assert.equal(uploadResults.emptyMimeTxtEnv.calls.puts.length, 0);
  assert.equal(uploadResults.metadataFailure.status, 503);
  assert.equal(uploadResults.metadataFailureEnv.calls.puts.length, 1, "the PDF is written before metadata");
  assert.equal(uploadResults.metadataFailureEnv.calls.deletes.length, 1);
  assert.equal(
    uploadResults.metadataFailureEnv.calls.deletes[0][0],
    "pdf/hot:0123456789abcdef",
    "a metadata failure must delete the newly written PDF",
  );
  assert.equal(JSON.stringify(commentOrderResults.fullIds), JSON.stringify([
    commentOrderResults.ids.c,
    commentOrderResults.ids.a,
    commentOrderResults.ids.b,
  ]), "a complete manifest must define the whole comment order");
  assert.equal(JSON.stringify(commentOrderResults.legacyIds), JSON.stringify([
    commentOrderResults.ids.a,
    commentOrderResults.ids.b,
    commentOrderResults.ids.c,
  ]), "comments without a manifest must retain their legacy order");
  assert.equal(JSON.stringify(commentOrderResults.appendedIds), JSON.stringify([
    commentOrderResults.ids.b,
    commentOrderResults.ids.a,
    commentOrderResults.ids.c,
  ]), "comments added after a manifest must be appended");
  assert.equal(commentOrderResults.failure.status, 503);
  assert.equal(commentOrderResults.failureRowsUnchanged, true, "a manifest failure must not mutate comment objects");
  assert.equal(commentOrderResults.failurePutKeys.length, 1, "ordering must attempt one manifest write only");
  assert.match(commentOrderResults.failurePutKeys[0], /_hot-reports\/comment-orders\//);
  assert.equal(JSON.stringify(commentOrderResults.failureManifestIds), JSON.stringify([
    commentOrderResults.ids.a,
    commentOrderResults.ids.b,
  ]), "a failed write must leave the old manifest intact");
  assert.equal(commentOrderResults.capped.status, 409, "the 501st comment must be rejected explicitly");
  assert.match(commentOrderResults.capped.payload.detail, /500/);
  assert.equal(commentOrderResults.cappedPutKeys.length, 0, "a rejected over-limit comment must not be stored");
  console.log("Portal Suite hot-report access, upload, comment-order, and search recommendation checks passed.");
}).catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
