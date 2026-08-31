const assert = require("node:assert/strict");
const { webcrypto } = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const builder = fs.readFileSync(path.join(root, "scripts/build_portal_suite_site.py"), "utf8");
const brandStart = worker.indexOf("const PUBLIC_BRAND");
const brandEnd = worker.indexOf("const ADMIN_TOKEN_TTL_SECONDS", brandStart);
assert.ok(brandStart >= 0 && brandEnd > brandStart, "public brand definitions must exist");
const brandDefinitions = worker.slice(brandStart, brandEnd);

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
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

const planDefinitions = worker.match(/const VID2PPT_PORTAL_GIFT_PLANS = \{[\s\S]*?\n\};/);
assert.ok(planDefinitions, "Vid2PPT plan definitions must exist");

const sandbox = {
  Response,
  Request,
  URL,
  URLSearchParams,
  TextEncoder,
  TextDecoder,
  crypto: webcrypto,
  btoa: (value) => Buffer.from(value, "binary").toString("base64"),
  atob: (value) => Buffer.from(value, "base64").toString("binary"),
  api: null,
};

vm.runInNewContext(`
  ${brandDefinitions}
  const CACHE_TTL_MS = 5 * 60 * 1000;
  const TRIAL_3D_DURATION_VALUE = "trial_3d";
  const TRIAL_3D_DOWNLOAD_LIMIT = 10;
  const REPORT_TEXT_CHUNK_CHARS = 12 * 1024;
  const REPORT_TEXT_CURSOR_TTL_SECONDS = 15 * 60;
  const REPORT_TEXT_CURSOR_MAX_LENGTH = 2048;
  const REPORT_TEXT_SOURCE_LABEL = "提取文本节选";
  ${planDefinitions[0]}

  function corsHeaders() { return { "Access-Control-Allow-Origin": "https://portal.example.invalid" }; }
  function cleanCatalogReportId(value) {
    const id = String(value || "").trim().toLowerCase();
    return /^[a-f0-9]{16,64}$/.test(id) ? id : "";
  }
  function accountDisabled(user) {
    return Boolean(user && (user.disabled || user.account_status === "disabled" || user.status === "disabled"));
  }
  function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
  function accountSecret(env) {
    const secret = String(env.AUTH_SECRET || "").trim();
    if (!secret) throw new Error("Account service is temporarily unavailable.");
    return secret;
  }
  function findReport(catalog, id) {
    return (catalog.items || []).find((item) => item.id === id);
  }
  async function currentUserFromRequest(env) {
    env.calls.currentUser += 1;
    if (env.authError) throw env.authError;
    return env.user;
  }
  async function reportAccessForUser(env, _user, reportId, source) {
    env.calls.reportAccess += 1;
    env.calls.accessArgs.push({ reportId, source });
    if (env.accessError) throw env.accessError;
    return env.access;
  }
  async function loadCatalog(env) {
    env.calls.catalog += 1;
    if (env.catalogError) throw env.catalogError;
    return env.catalog;
  }
  async function catalogReportPdfDescriptor(env, _report, options) {
    env.calls.pdfDescriptor += 1;
    env.calls.pdfOptions.push(options);
    if (env.pdfError) throw env.pdfError;
    return env.pdfDescriptor || null;
  }
  async function loadReportTextHistoryIndex(env) {
    env.calls.history += 1;
    if (env.historyError) throw env.historyError;
    return env.historyIndex;
  }
  async function loadReportTextCurrentIndex(env, _report, date) {
    env.calls.currentIndex += 1;
    env.calls.currentDates.push(date);
    if (env.currentIndexError) throw env.currentIndexError;
    if (env.currentIndexesByDate) return env.currentIndexesByDate[date] || null;
    return env.currentIndex;
  }

  ${extractFunction(worker, "base64UrlEncodeBytes")}
  ${extractFunction(worker, "base64UrlEncodeText")}
  ${extractFunction(worker, "base64UrlDecodeText")}
  ${extractFunction(worker, "constantTimeEqual")}
  ${extractFunction(worker, "hmacSha256Bytes")}
  ${extractFunction(worker, "accessErrorStatus")}
  ${extractFunction(worker, "privateJsonResponse")}
  ${extractFunction(worker, "reportTextCursorSignature")}
  ${extractFunction(worker, "createReportTextCursor")}
  ${extractFunction(worker, "readReportTextCursor")}
  ${extractFunction(worker, "hotReportPlanMonths")}
  ${extractFunction(worker, "hotReportAccessMonths")}
  ${extractFunction(worker, "reportTextAccessQualifies")}
  ${extractFunction(worker, "reportTextHistoryMonth")}
  ${extractFunction(worker, "reportTextCurrentDates")}
  ${extractFunction(worker, "reportTextShardIndexUrl")}
  ${extractFunction(worker, "reportTextHistoryIndexUrl")}
  ${extractFunction(worker, "reportTextCurrentIndexUrl")}
  ${extractFunction(worker, "reportTextWords")}
  ${extractFunction(worker, "reportTextDateToken")}
  ${extractFunction(worker, "reportTextDateKey")}
  ${extractFunction(worker, "reportTextInstitutionPrefixMatches")}
  ${extractFunction(worker, "reportTextCanonicalTitle")}
  ${extractFunction(worker, "reportTextEntryHasBody")}
  ${extractFunction(worker, "findReportTextEntry")}
  ${extractFunction(worker, "resolveReportTextEntry")}
  ${extractFunction(worker, "reportTextIndexVersion")}
  ${extractFunction(worker, "reportTextChunk")}
  ${extractFunction(worker, "handleReportText")}

  api = {
    base64UrlEncodeText,
    reportTextCursorSignature,
    createReportTextCursor,
    readReportTextCursor,
    reportTextAccessQualifies,
    reportTextHistoryMonth,
    reportTextCurrentDates,
    reportTextHistoryIndexUrl,
    reportTextCurrentIndexUrl,
    reportTextCanonicalTitle,
    resolveReportTextEntry,
    reportTextIndexVersion,
    publicBrandDocumentText,
    handleReportText,
  };
`, sandbox);

const api = sandbox.api;
const REPORT_A = "c0ba6488e6245a4f042b1ff0";
const REPORT_A_LIVE = "c80b1b45b0d7f8b328e1a63c";
const REPORT_B = "bbbbbbbbbbbbbbbb";
const ARCHIVE_TITLE = "BofA Securities-NVIDIA Corporation（NVDA.OQ）More cores or faster cores？ The NVDA vs AMD agentic CPU debate-260722";
const LIVE_TITLE = "BofA-NVIDIA Corporation（NVDA.OQ）More cores or faster cores？ The NVDA vs AMD agentic CPU debate-260722";
const ARCHIVE_TEXT = "bofa securities nvidia corporation nvda oq more cores or faster cores the nvda vs amd agentic cpu debate 260722";
const LONG_TEXT = `${ARCHIVE_TEXT} <script>alert("xss")</script>${" extracted body".repeat(1800)}`;

function activeEffective(overrides = {}) {
  return { active: true, lifetime: false, source: "stored", duration_value: "1", ...overrides };
}

function adminAccess(overrides = {}) {
  return {
    can_download: true,
    effective_access_kind: "admin",
    effective_access: activeEffective(overrides),
    entitlement: { active: false, plan: "free", source_plan_code: "" },
    custom_access_matched: true,
    entitlement_access_matched: false,
    trial_access_matched: false,
    purchase: null,
  };
}

function entitlementAccess(code = "NOVA-M", overrides = {}) {
  return {
    can_download: true,
    effective_access_kind: "entitlement",
    effective_access: activeEffective({ source: "vid2ppt_nova", duration_value: "", source_plan_code: code, ...overrides }),
    entitlement: { active: true, plan: "annual", source_plan_code: code },
    custom_access_matched: false,
    entitlement_access_matched: true,
    trial_access_matched: false,
    purchase: null,
  };
}

const ordinaryUser = { id: "user-1", email: "reader@example.com", username: "reader" };
assert.equal(api.reportTextAccessQualifies({ ...ordinaryUser, privileged: true }, null), true, "enabled privileged users qualify");
assert.equal(api.reportTextAccessQualifies({ ...ordinaryUser, privileged: true, disabled: true }, null), false, "disabled privileged users do not qualify");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, adminAccess()), true, "a matching one-month administrator grant qualifies");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, adminAccess({ lifetime: true, duration_value: "" })), true, "a matching lifetime grant qualifies");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, adminAccess({ duration_value: "0.5" })), false, "a grant shorter than one month does not qualify");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, entitlementAccess("NOVA-M")), true, "NOVA-M qualifies");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, entitlementAccess("NOVA-Q")), true, "NOVA-Q qualifies");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, entitlementAccess("NOVA-3D")), false, "NOVA-3D is always rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  ...adminAccess({ duration_value: "trial_3d" }),
}), false, "three-day administrator trials are rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  can_download: true,
  effective_access_kind: "none",
  effective_access: { active: false },
  entitlement: { active: false, plan: "free" },
  purchase: { status: "active" },
}), false, "single-report purchases are rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  can_download: false,
  effective_access_kind: "none",
  effective_access: { active: false },
  entitlement: { active: false, plan: "free" },
}), false, "free accounts without a report grant are rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  ...adminAccess(),
  effective_access: activeEffective({ active: false }),
}), false, "expired grants are rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  can_download: true,
  effective_access_kind: "trial",
  effective_access: activeEffective({ source: "vid2ppt_trial", duration_value: "trial_3d", source_plan_code: "NOVA-3D" }),
  entitlement: { active: false, plan: "free" },
  trial_access_matched: true,
}), false, "trial access is rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  ...adminAccess(),
  can_download: false,
  custom_access_matched: false,
}), false, "an institution grant that does not match the requested report is rejected");
assert.equal(api.reportTextAccessQualifies(ordinaryUser, {
  ...adminAccess({ duration_value: "0.5", source_plan_code: "" }),
  entitlement: { active: true, plan: "annual", source_plan_code: "NOVA-Q" },
}), false, "a stale broader entitlement cannot override the authoritative administrator grant");

const archiveReport = {
  id: REPORT_A,
  title: ARCHIVE_TITLE,
  filename: `${ARCHIVE_TITLE}.pdf`,
  bank_code: "BofA",
  bank_name: "BofA",
  date_folder: "260722",
  date_folders: ["260722", "260723"],
  available: false,
};
const liveReport = {
  id: REPORT_A_LIVE,
  title: LIVE_TITLE,
  filename: `${LIVE_TITLE}.pdf`,
  bank_code: "BofA",
  bank_name: "美银",
  date_folder: "260723",
  available: true,
};
const aliasCatalog = { items: [archiveReport, liveReport] };
const aliasIndex = {
  updated_at_bjt: "2026-07-26 03:00:00 +0800",
  items: [
    { id: REPORT_A, text: ARCHIVE_TEXT },
    { id: REPORT_A_LIVE, text: LONG_TEXT },
  ],
};
const aliasResolved = api.resolveReportTextEntry(aliasCatalog, aliasIndex, archiveReport);
assert.equal(aliasResolved.aliased, true, "the exact BofA/BofA Securities duplicate must use the full-text live alias");
assert.equal(aliasResolved.entry.id, REPORT_A_LIVE);
assert.equal(api.reportTextCanonicalTitle(archiveReport), api.reportTextCanonicalTitle(liveReport));
assert.equal(api.reportTextHistoryMonth(archiveReport), "2607");
assert.match(
  api.reportTextHistoryIndexUrl({ CATALOG_URL: "https://portal.example.invalid/data/catalog.json" }, archiveReport),
  /\/data\/search_index_history\/shard_2607\.json$/,
  "Text-only reads must prefer the report's monthly history shard",
);
assert.match(
  api.reportTextCurrentIndexUrl({ CATALOG_URL: "https://portal.example.invalid/data/catalog.json" }, archiveReport),
  /\/data\/search_index_current\/shard_260722\.json$/,
  "the full-text alias fallback must use bounded daily current shards",
);
assert.deepEqual(
  Array.from(api.reportTextCurrentDates(archiveReport)),
  ["260722", "260723"],
  "title/date_folder/date_folders must supply ordered, deduplicated current-shard candidates",
);

const differentReport = {
  ...liveReport,
  id: REPORT_B,
  title: "BofA-NVIDIA Corporation A genuinely different report-260722",
  filename: "BofA-NVIDIA Corporation A genuinely different report-260722.pdf",
};
const differentResolved = api.resolveReportTextEntry(
  { items: [archiveReport, differentReport] },
  { items: [{ id: REPORT_A, text: ARCHIVE_TEXT }, { id: REPORT_B, text: `${ARCHIVE_TEXT} unrelated full body` }] },
  archiveReport,
);
assert.equal(differentResolved.aliased, false, "different titles must never be used as text aliases");
assert.equal(differentResolved.entry.id, REPORT_A);
const differentDateResolved = api.resolveReportTextEntry(
  { items: [archiveReport, { ...liveReport, title: LIVE_TITLE.replace("260722", "260721") }] },
  aliasIndex,
  archiveReport,
);
assert.equal(differentDateResolved.aliased, false, "the same normalized title on a different date must not be aliased");
const barelyMoreThanTitle = api.resolveReportTextEntry(
  { items: [archiveReport] },
  { items: [{ id: REPORT_A, text: `${ARCHIVE_TEXT} short metadata only` }] },
  archiveReport,
);
assert.equal(barelyMoreThanTitle.has_body, false, "a few extra metadata words must not be presented as extracted report body");

function makeEnv(overrides = {}) {
  return {
    AUTH_SECRET: "test-report-text-secret",
    calls: {
      currentUser: 0,
      reportAccess: 0,
      accessArgs: [],
      catalog: 0,
      pdfDescriptor: 0,
      pdfOptions: [],
      history: 0,
      currentIndex: 0,
      currentDates: [],
    },
    user: ordinaryUser,
    access: adminAccess(),
    catalog: { items: [archiveReport] },
    historyIndex: { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_A, text: LONG_TEXT }] },
    currentIndex: { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_A, text: LONG_TEXT }] },
    ...overrides,
  };
}

function textRequest(reportId = REPORT_A, cursor = "") {
  const params = new URLSearchParams({ report_id: reportId });
  if (cursor) params.set("cursor", cursor);
  return new Request(`https://worker.example/report-text?${params.toString()}`, {
    headers: { Authorization: "Bearer user-token" },
  });
}

async function responseJson(response) {
  return JSON.parse(await response.text());
}

(async () => {
  const firstEnv = makeEnv();
  const firstResponse = await api.handleReportText(textRequest(), firstEnv);
  assert.equal(firstResponse.status, 200);
  assert.match(firstResponse.headers.get("content-type"), /^application\/json/);
  assert.match(firstResponse.headers.get("cache-control"), /private/);
  assert.match(firstResponse.headers.get("cache-control"), /no-store/);
  assert.equal(firstResponse.headers.get("x-content-type-options"), "nosniff");
  const firstRaw = await firstResponse.text();
  assert.doesNotMatch(firstRaw, /<script/i, "the JSON wire body must escape HTML-significant characters");
  const first = JSON.parse(firstRaw);
  assert.match(first.text, /<script>alert\("xss"\)<\/script>/, "JSON decoding must preserve the source as inert text");
  assert.equal(first.source_label, "提取文本节选");
  assert.equal(first.has_more, true);
  assert.ok(first.next_cursor);
  assert.equal(firstEnv.calls.currentUser, 1);
  assert.equal(firstEnv.calls.reportAccess, 1);
  assert.equal(firstEnv.calls.accessArgs[0].reportId, REPORT_A);
  assert.equal(firstEnv.calls.accessArgs[0].source, "catalog");
  assert.equal(firstEnv.calls.history, 1);
  assert.equal(firstEnv.calls.currentIndex, 0, "a usable monthly history shard must avoid the large current index");
  assert.equal(firstEnv.calls.pdfOptions[0].verifyObject, true, "a verified PDF override must close the Text-only endpoint");

  const secondResponse = await api.handleReportText(textRequest(REPORT_A, first.next_cursor), firstEnv);
  assert.equal(secondResponse.status, 200);
  const second = await responseJson(secondResponse);
  assert.equal(firstEnv.calls.currentUser, 2, "every page must re-authenticate the current session");
  assert.equal(firstEnv.calls.reportAccess, 2, "every page must recompute report-specific access");
  assert.notEqual(second.text, first.text);

  const revokedEnv = makeEnv({
    access: {
      can_download: false,
      effective_access_kind: "none",
      effective_access: { active: false },
      entitlement: { active: false, plan: "free" },
    },
  });
  const revoked = await api.handleReportText(textRequest(REPORT_A, first.next_cursor), revokedEnv);
  assert.equal(revoked.status, 403, "revocation between pages must take effect immediately");
  assert.equal(revokedEnv.calls.currentUser, 1);
  assert.equal(revokedEnv.calls.reportAccess, 1);
  assert.equal(revokedEnv.calls.history, 0, "denied requests must not load report text");

  const tamperedCursor = `${first.next_cursor.slice(0, -1)}${first.next_cursor.endsWith("A") ? "B" : "A"}`;
  const tamperedEnv = makeEnv();
  const tampered = await api.handleReportText(textRequest(REPORT_A, tamperedCursor), tamperedEnv);
  assert.equal(tampered.status, 409, "tampered cursors must be rejected");
  assert.equal(tamperedEnv.calls.currentUser, 1);
  assert.equal(tamperedEnv.calls.reportAccess, 1, "cursor validation must happen only after fresh access validation");

  const reportB = { ...archiveReport, id: REPORT_B, title: "BofA-Different title-260722", filename: "BofA-Different title-260722.pdf" };
  const crossReportEnv = makeEnv({
    catalog: { items: [reportB] },
    historyIndex: { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_B, text: LONG_TEXT }] },
    currentIndex: { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_B, text: LONG_TEXT }] },
  });
  const crossReport = await api.handleReportText(textRequest(REPORT_B, first.next_cursor), crossReportEnv);
  assert.equal(crossReport.status, 409, "a cursor must be bound to its original report_id");
  assert.equal(crossReportEnv.calls.reportAccess, 1);

  const aliasEnv = makeEnv({
    catalog: aliasCatalog,
    historyIndex: { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_A, text: ARCHIVE_TEXT }] },
    currentIndexesByDate: {
      "260722": { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_A, text: ARCHIVE_TEXT }] },
      "260723": { updated_at_bjt: "2026-07-26", items: [{ id: REPORT_A_LIVE, text: LONG_TEXT }] },
    },
  });
  const aliasResponse = await api.handleReportText(textRequest(), aliasEnv);
  assert.equal(aliasResponse.status, 200);
  const aliasBody = await responseJson(aliasResponse);
  assert.match(aliasBody.text, /extracted body/);
  assert.equal(aliasEnv.calls.currentIndex, 2, "title-only history data must scan only the ordered daily current shards needed for an exact alias");
  assert.deepEqual(Array.from(aliasEnv.calls.currentDates), ["260722", "260723"]);
  assert.equal(aliasEnv.calls.accessArgs[0].reportId, REPORT_A, "alias fallback must never change the authorized report id");

  const boundaryText = `${"x".repeat(12 * 1024 - 4)}Reportify NashAI MacroGate Portal Suite extracted body`;
  const legacyBrandEnv = makeEnv({
    historyIndex: { updated_at_bjt: "2026-08-31", items: [{ id: REPORT_A, text: boundaryText }] },
    currentIndex: { updated_at_bjt: "2026-08-31", items: [{ id: REPORT_A, text: boundaryText }] },
  });
  let brandCursor = "";
  let publicText = "";
  do {
    const response = await api.handleReportText(textRequest(REPORT_A, brandCursor), legacyBrandEnv);
    assert.equal(response.status, 200);
    const page = await responseJson(response);
    publicText += page.text;
    brandCursor = page.next_cursor;
  } while (brandCursor);
  assert.match(publicText, /KC桌面/u);
  assert.doesNotMatch(publicText, /Reportify|Nash[\s._-]*AI|Macro[\s._-]*Gate|Portal[\s._-]*Suite/iu);

  const availableEnv = makeEnv({ catalog: { items: [{ ...archiveReport, available: true }] } });
  assert.equal((await api.handleReportText(textRequest(), availableEnv)).status, 409, "available reports are not Text only");
  const overrideEnv = makeEnv({ pdfDescriptor: { id: REPORT_A, available: true, manual_pdf: true } });
  assert.equal((await api.handleReportText(textRequest(), overrideEnv)).status, 409, "verified PDF overrides close Text-only access");

  const authEnv = makeEnv({ authError: new Error("Please log in.") });
  assert.equal((await api.handleReportText(textRequest(), authEnv)).status, 401);
  const disabledEnv = makeEnv({ authError: new Error("账号已禁用") });
  assert.equal((await api.handleReportText(textRequest(), disabledEnv)).status, 403);
  const accessVerificationEnv = makeEnv({
    access: {
      can_download: false,
      effective_access_kind: "error",
      effective_access: { active: false, source: "error" },
    },
  });
  assert.equal((await api.handleReportText(textRequest(), accessVerificationEnv)).status, 503);
  const missingTextEnv = makeEnv({ historyIndex: { items: [] }, currentIndex: { items: [] } });
  assert.equal((await api.handleReportText(textRequest(), missingTextEnv)).status, 404);
  const titleOnlyEnv = makeEnv({
    historyIndex: { items: [{ id: REPORT_A, text: ARCHIVE_TEXT }] },
    currentIndex: { items: [{ id: REPORT_A, text: `${ARCHIVE_TEXT} short metadata only` }] },
  });
  assert.equal(
    (await api.handleReportText(textRequest(), titleOnlyEnv)).status,
    404,
    "title-only index rows must not be wrapped as original report text",
  );
  const indexFailureEnv = makeEnv({ historyError: new Error("timeout"), currentIndexError: new Error("timeout") });
  assert.equal((await api.handleReportText(textRequest(), indexFailureEnv)).status, 503);

  const indexVersion = api.reportTextIndexVersion(firstEnv.historyIndex, firstEnv.historyIndex.items[0]);
  const now = Math.floor(Date.now() / 1000);
  const invalidPayload = {
    v: 1,
    kind: "report-text",
    report_id: REPORT_A,
    offset: 100,
    index_version: indexVersion,
    iat: now,
    exp: now + 15 * 60,
    extra: true,
  };
  const invalidBody = api.base64UrlEncodeText(JSON.stringify(invalidPayload));
  const invalidSigned = `${invalidBody}.${await api.reportTextCursorSignature(firstEnv, invalidBody)}`;
  await assert.rejects(
    api.readReportTextCursor(firstEnv, invalidSigned, REPORT_A, indexVersion),
    /cursor is invalid/i,
    "even correctly signed cursors with unknown claims must be rejected",
  );

  const handlerSource = extractFunction(worker, "handleReportText");
  assert.ok(handlerSource.indexOf("currentUserFromRequest") < handlerSource.indexOf("readReportTextCursor"));
  assert.ok(handlerSource.indexOf("reportAccessForUser") < handlerSource.indexOf("readReportTextCursor"));
  assert.match(handlerSource, /reportAccessForUser\(env, user, reportId, "catalog"\)/);
  assert.match(handlerSource, /catalogReportPdfDescriptor\(env, report, \{ verifyObject: true \}\)/);
  assert.ok(handlerSource.indexOf("loadReportTextHistoryIndex") < handlerSource.indexOf("loadReportTextCurrentIndex"));
  assert.doesNotMatch(handlerSource, /loadSearchIndex\(/, "Text-only reads must not parse the monolithic current index");
  assert.match(worker, /pathname === "\/report-text"[\s\S]*?handleReportText\(request, env\)/);
  assert.match(
    builder,
    /current_manifest = write_search_index_shards\([\s\S]*?output_dir=output_dir \/ "data" \/ "search_index_current",[\s\S]*?partition="day"/,
    "the site build must publish the daily current-text shards used by the Worker",
  );

  const frontendHandler = extractFunction(app, "initTextOnlyTextAccess");
  assert.match(frontendHandler, /\/report-text\?\$\{params\.toString\(\)\}/);
  assert.match(frontendHandler, /headers: \{ "Authorization": `Bearer \$\{requestToken\}` \}/);
  assert.match(frontendHandler, /params\.set\("cursor", requestedCursor\)/);
  assert.match(frontendHandler, /body\.textContent \+= chunk/);
  assert.match(frontendHandler, /source\.textContent =/);
  assert.doesNotMatch(frontendHandler, /body\.innerHTML|source\.innerHTML/, "the frontend must render report text as text, never HTML");

  console.log("Portal Suite Text-only text access tests passed.");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
