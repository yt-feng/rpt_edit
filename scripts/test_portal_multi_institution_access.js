const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");

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

assert.match(app, /id="accountAdminAccessInstitutions" role="group"/);
assert.doesNotMatch(app, /id="accountAdminAccessInstitutions" multiple/);
assert.match(app, /id="accountAdminAccessInstitutionSearch" type="search"/);
assert.match(app, /selectedAccessCheckboxValues\(targets\.accessInstitutions\)/);
assert.match(app, /loadAdminUserAccess\(workerUrl, email\)/);
assert.match(app, /accountAdminAccessOptions = data\.access_options/);
assert.match(worker, /pathname === "\/account-admin\/user-access" && request\.method === "GET"/);
assert.match(worker, /access_options: accessOptionRowsFromCatalog\(catalog\)/);
assert.match(worker, /\["ACCESS_INVALID_PAYLOAD", "ACCESS_EMPTY_FILTERS"\]\.includes\(error\.code\)/);

const uiSandbox = {};
vm.runInNewContext(`
  ${extractFunction(app, "accessOptionKey")}
  ${extractFunction(app, "mergeAccessOptionRows")}
  ${extractFunction(app, "accessScopeSnapshot")}
  ${extractFunction(app, "accessScopeNeedsConfirmation")}
  result = {
    merged: mergeAccessOptionRows([
      { value: "Nomura · 野村证券", label: "Nomura · 野村证券 (8)" },
      { value: "Citi · 花旗", label: "Citi · 花旗 (5)" },
    ], ["Nomura", "Legacy Bank"]),
    additionNeedsConfirmation: accessScopeNeedsConfirmation(
      { access_mode: "filters", institutions: ["Nomura"] },
      { access_mode: "filters", institutions: ["Nomura", "Citi"] },
    ),
    removalNeedsConfirmation: accessScopeNeedsConfirmation(
      { access_mode: "filters", institutions: ["Nomura", "Citi"] },
      { access_mode: "filters", institutions: ["Nomura"] },
    ),
    allNeedsConfirmation: accessScopeNeedsConfirmation(
      { access_mode: "none" },
      { access_mode: "all" },
    ),
  };
`, uiSandbox);

assert.deepEqual(
  Array.from(uiSandbox.result.merged.slice(0, 2), (row) => row.value),
  ["Nomura", "Legacy Bank"],
  "stored values missing from the current catalog must remain selected and visible",
);
assert.equal(uiSandbox.result.merged[0].legacy, true);
assert.equal(uiSandbox.result.merged[1].legacy, true);
assert.equal(uiSandbox.result.additionNeedsConfirmation, false, "adding an institution is not a narrowing");
assert.equal(uiSandbox.result.removalNeedsConfirmation, true, "removing an institution requires confirmation");
assert.equal(uiSandbox.result.allNeedsConfirmation, true, "switching to full-site access requires confirmation");

const workerSandbox = {};
vm.runInNewContext(`
  const ACCESS_PAGE_RANGE_OPTIONS = [
    { value: "under5" }, { value: "5_10" }, { value: "10_20" }, { value: "over20" },
  ];
  const ACCESS_MODES = new Set(["none", "all", "filters"]);
  function normalizeText(value) {
    return String(value || "").normalize("NFKC").toLowerCase().replace(/[^\\p{L}\\p{N}]+/gu, " ").trim();
  }
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  ${extractFunction(worker, "normalizeAccessList")}
  const TRIAL_3D_DURATION_VALUE = "trial_3d";
  const TRIAL_3D_DOWNLOAD_LIMIT = 10;
  ${extractFunction(worker, "canonicalizeLegacyAccessGrantRow")}
  ${extractFunction(worker, "accessPayloadError")}
  ${extractFunction(worker, "validateAccessListPayload")}
  ${extractFunction(worker, "validateAccessGrantPayloadLists")}
  ${extractFunction(worker, "validateAccessGrantRow")}
  function publicAccessGrant(row) {
    const value = row || {};
    return {
      access_mode: value.access_mode || "none",
      institutions: normalizeAccessList(value.institutions),
      industries: normalizeAccessList(value.industries),
      page_ranges: normalizeAccessList(value.page_ranges, ACCESS_PAGE_RANGE_OPTIONS.length),
    };
  }
  ${extractFunction(worker, "accessScopeChangeNeedsConfirmation")}
  function captureError(callback) {
    try { callback(); return ""; } catch (error) { return error.message; }
  }
  function captureErrorCode(callback) {
    try { callback(); return ""; } catch (error) { return error.code || ""; }
  }
  const validLists = validateAccessGrantPayloadLists({
    institutions: ["Nomura", "Citi"], industries: [], page_ranges: [],
  }, "filters");
  const legacyPlural = canonicalizeLegacyAccessGrantRow({ institutions: "Nomura，Citi", industries: [], page_ranges: [] });
  const legacySingular = canonicalizeLegacyAccessGrantRow({ institution: "Nomura", industries: [], page_ranges: [] });
  const validatedLegacy = validateAccessGrantRow({
    id: "legacy-grant",
    email: "legacy@example.com",
    access_mode: "filters",
    status: "active",
    lifetime: false,
    current_period_end: "2027-07-22T00:00:00.000Z",
    duration_value: "12",
    institutions: "Nomura,Citi",
    industries: [],
    page_ranges: [],
  }, "legacy@example.com");
  result = {
    validLists,
    legacyPlural,
    legacySingular,
    validatedLegacy,
    scalarError: captureError(() => validateAccessGrantPayloadLists({ institutions: "Nomura", industries: [], page_ranges: [] }, "filters")),
    scalarErrorCode: captureErrorCode(() => validateAccessGrantPayloadLists({ institutions: "Nomura", industries: [], page_ranges: [] }, "filters")),
    objectError: captureError(() => validateAccessGrantPayloadLists({ institutions: [{}], industries: [], page_ranges: [] }, "filters")),
    tooManyError: captureError(() => validateAccessGrantPayloadLists({ institutions: Array.from({ length: 61 }, (_, index) => "Bank " + index), industries: [], page_ranges: [] }, "filters")),
    emptyError: captureError(() => validateAccessGrantPayloadLists({ institutions: [], industries: [], page_ranges: [] }, "filters")),
    modePayloadError: captureError(() => validateAccessGrantPayloadLists({ institutions: ["Nomura"], industries: [], page_ranges: [] }, "all")),
    additionNeedsConfirmation: accessScopeChangeNeedsConfirmation(
      { access_mode: "filters", institutions: ["Nomura"], industries: [], page_ranges: [] },
      "filters",
      { institutions: ["Nomura", "Citi"], industries: [], page_ranges: [] },
    ),
    removalNeedsConfirmation: accessScopeChangeNeedsConfirmation(
      { access_mode: "filters", institutions: ["Nomura", "Citi"], industries: [], page_ranges: [] },
      "filters",
      { institutions: ["Nomura"], industries: [], page_ranges: [] },
    ),
  };
`, workerSandbox);

assert.deepEqual(Array.from(workerSandbox.result.validLists.institutions), ["Nomura", "Citi"]);
assert.deepEqual(Array.from(workerSandbox.result.legacyPlural.institutions), ["Nomura", "Citi"]);
assert.deepEqual(Array.from(workerSandbox.result.legacySingular.institutions), ["Nomura"]);
assert.deepEqual(Array.from(workerSandbox.result.validatedLegacy.institutions), ["Nomura", "Citi"]);
assert.equal(workerSandbox.result.legacyPlural.download_limit, 0);
assert.equal(workerSandbox.result.legacyPlural.download_count, 0);
assert.deepEqual(Array.from(workerSandbox.result.legacyPlural.download_items), []);
assert.match(workerSandbox.result.scalarError, /字符串数组/);
assert.equal(workerSandbox.result.scalarErrorCode, "ACCESS_INVALID_PAYLOAD");
assert.match(workerSandbox.result.objectError, /字符串数组/);
assert.match(workerSandbox.result.tooManyError, /最多选择 60 项/);
assert.match(workerSandbox.result.emptyError, /至少要选择一个/);
assert.match(workerSandbox.result.modePayloadError, /非筛选模式不能携带/);
assert.equal(workerSandbox.result.additionNeedsConfirmation, false);
assert.equal(workerSandbox.result.removalNeedsConfirmation, true);

const authorizationSandbox = {};
vm.runInNewContext(`
  function normalizeText(value) { return String(value || "").trim().toLowerCase(); }
  function publicAccessGrant(row) { return row; }
  function reportBankLabel(report) { return report.bank_code + " · " + report.bank_name; }
  function inferReportIndustry(report) { return report.industry || ""; }
  function reportPageCount(report) { return Number(report.pages || 0); }
  function accessPageRangeMatches() { return false; }
  ${extractFunction(worker, "accessGrantMatchesReport")}
  const grant = {
    active: true,
    access_mode: "filters",
    institutions: ["Nomura", "Citi"],
    industries: [],
    page_ranges: [],
  };
  result = {
    nomura: accessGrantMatchesReport(grant, { bank_code: "Nomura", bank_name: "野村证券" }, "catalog"),
    citi: accessGrantMatchesReport(grant, { bank_code: "Citi", bank_name: "花旗" }, "catalog"),
    citic: accessGrantMatchesReport(grant, { bank_code: "CITIC", bank_name: "中信证券" }, "catalog"),
    external: accessGrantMatchesReport(grant, { bank_code: "Nomura", bank_name: "野村证券" }, "external"),
  };
`, authorizationSandbox);

assert.equal(authorizationSandbox.result.nomura, true);
assert.equal(authorizationSandbox.result.citi, true);
assert.equal(authorizationSandbox.result.citic, false, "Citi must not prefix-match CITIC");
assert.equal(authorizationSandbox.result.external, false, "institution filters only apply to catalog reports");

console.log("Portal Suite multi-institution access checks passed.");
