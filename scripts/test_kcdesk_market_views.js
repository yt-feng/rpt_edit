const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "kc_desk_notes/site_src/assets/app.js"), "utf8");
const workflow = fs.readFileSync(path.join(root, ".github/workflows/market-views-latex-pdf.yml"), "utf8");

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

const planDefinitions = worker.match(/const VID2PPT_KCDESK_GIFT_PLANS = \{[\s\S]*?\n\};/);
assert.ok(planDefinitions, "membership plan definitions must exist");

const sandbox = { api: null };
vm.runInNewContext(`
  const TRIAL_3D_DOWNLOAD_LIMIT = 10;
  ${planDefinitions[0]}
  const TRIAL_3D_DURATION_VALUE = "trial_3d";
  const MARKET_VIEW_ID_PATTERN = /^market-view:(\\d{6})$/;
  const MARKET_VIEW_MIN_MONTHS = 1;
  const MARKET_VIEW_REQUIRED_PLAN = "至少1个月会员";
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function accountDisabled(user) { return Boolean(user && user.disabled); }
  function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
  function publicAccessGrant(row) { return row && typeof row === "object" ? { ...row } : { active: false, source: "none" }; }
  function publicEntitlement(row) { return row && typeof row === "object" ? { ...row } : { active: false, plan: "free" }; }
  function roleAccessForUser() { return { active: true, lifetime: true, source: "role", access_mode: "all" }; }
  function superEntitlement() { return { active: true, plan: "super" }; }
  async function findEntitlement(env) { return env.entitlement || null; }
  async function findAccessGrant(env) { return env.access || null; }
  async function findVid2PptTrialAccess(env) { return env.trial || null; }
  function effectiveAccessChoiceForUser(_user, entitlement, access) {
    const choices = [];
    if (access && access.active) choices.push({ kind: "admin", access });
    if (entitlement && entitlement.active) choices.push({
      kind: "entitlement",
      access: {
        active: true,
        source: entitlement.source || "entitlement",
        source_plan_code: entitlement.source_plan_code || "",
        duration_value: entitlement.duration_value || "",
        access_mode: "all",
      },
    });
    return { choices };
  }
  function broaderCurrentAccessChoice(left, right) { return right || left; }
  ${extractFunction(worker, "hotReportPlanMonths")}
  ${extractFunction(worker, "hotReportAccessMonths")}
  ${extractFunction(worker, "reportTextAccessQualifies")}
  ${extractFunction(worker, "marketViewMembershipAccessForUser")}
  ${extractFunction(worker, "marketViewDateKeyFromId")}
  ${extractFunction(worker, "marketViewDateIso")}
  api = { marketViewMembershipAccessForUser, marketViewDateKeyFromId, marketViewDateIso };
`, sandbox);

const api = sandbox.api;
const reader = { email: "reader@example.com" };

(async () => {
  const cases = {
    filteredMonth: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "filters", duration_value: "1", source: "stored" },
    }, reader),
    novaMonth: await api.marketViewMembershipAccessForUser({
      entitlement: { active: true, plan: "annual", source: "vid2ppt_nova", source_plan_code: "NOVA-M" },
    }, reader),
    annual: await api.marketViewMembershipAccessForUser({
      entitlement: { active: true, plan: "annual", source: "entitlement" },
    }, reader),
    lifetime: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "filters", lifetime: true, source: "stored" },
    }, reader),
    trial: await api.marketViewMembershipAccessForUser({
      access: { active: true, access_mode: "all", duration_value: "trial_3d", source: "stored" },
    }, reader),
    free: await api.marketViewMembershipAccessForUser({}, reader),
    disabled: await api.marketViewMembershipAccessForUser({}, { ...reader, disabled: true }),
    privileged: await api.marketViewMembershipAccessForUser({}, { ...reader, privileged: true }),
  };

  assert.equal(cases.filteredMonth.can_download, true, "a one-month institution-filtered member qualifies");
  assert.equal(cases.novaMonth.can_download, true, "NOVA-M qualifies for Market Views");
  assert.equal(cases.annual.can_download, true, "annual membership qualifies");
  assert.equal(cases.lifetime.can_download, true, "lifetime membership qualifies");
  assert.equal(cases.trial.can_download, false, "the three-day trial does not qualify");
  assert.equal(cases.free.can_download, false, "a free registered account does not qualify");
  assert.equal(cases.disabled.can_download, false, "a disabled account does not qualify");
  assert.equal(cases.privileged.can_download, true, "the administrator qualifies");

  assert.equal(api.marketViewDateKeyFromId("market-view:260801"), "260801");
  assert.equal(api.marketViewDateIso("260229"), "", "invalid calendar dates are rejected");
  assert.equal(api.marketViewDateKeyFromId("market-view:../../secret"), "", "path injection is rejected at the id parser");

  const pdfHandler = extractFunction(worker, "handleMarketViewsPdf");
  assert.match(pdfHandler, /marketViewMembershipAccessForUser\(env, user\)/);
  assert.match(pdfHandler, /env\.REPORT_BUCKET\.get\(key\)/, "paid PDFs must come from private R2");
  assert.doesNotMatch(pdfHandler, /fetchGithubRawFile|market_view_summaries/, "the paid endpoint must not fall back to the public repository");
  assert.doesNotMatch(pdfHandler, /searchParams\.get\("path"\)/, "clients cannot submit a repository or R2 path");
  assert.match(worker, /pathname === "\/market-views\/pdf"[\s\S]*?handleMarketViewsPdf\(request, env\)/);
  assert.doesNotMatch(extractFunction(worker, "listMarketViewItems"), /latestMarketViewFiles|github/i, "the public list must only describe private R2 objects");
  assert.doesNotMatch(workflow, /actions\/upload-artifact/, "paid PDFs must not be exposed as Actions artifacts");
  assert.doesNotMatch(workflow, /commit_output_dir\.sh[\s\S]*market_view_summaries/, "paid PDFs and synthesis output must not be committed");
  assert.match(workflow, /permissions:\s*\n\s*contents: read/, "the private generator must not have repository write permission");
  assert.match(app, /data-market-view-id/);
  assert.match(app, /\/market-views\/access/);
  assert.match(app, /\/market-views\/pdf\?id=/);

  console.log("kcdesk Market Views membership and private-download checks passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
