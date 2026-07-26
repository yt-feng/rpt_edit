const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "kc_desk_notes/site_src/assets/app.js"), "utf8");

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

const sandbox = {};
vm.runInNewContext(`
  const VID2PPT_GIFT_SOURCES = new Set(["vid2ppt_nova", "vid2ppt_atlas"]);
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function activePeriod(row) {
    if (!row || !["active", "trialing"].includes(String(row.status || "inactive"))) return false;
    if (row.lifetime) return true;
    return Number.isFinite(Date.parse(row.current_period_end || "")) && Date.parse(row.current_period_end) > Date.now();
  }
  function publicEntitlement(row) {
    return row ? { ...row, active: row.active === undefined ? activePeriod(row) : Boolean(row.active) } : {
      plan: "free", status: "inactive", lifetime: false, current_period_end: null, active: false,
    };
  }
  function publicAccessGrant(row) {
    const value = row || {};
    return {
      ...value,
      email: value.email || "",
      access_mode: ["all", "filters"].includes(value.access_mode) ? value.access_mode : "none",
      status: value.status || "inactive",
      lifetime: Boolean(value.lifetime),
      current_period_end: value.current_period_end || null,
      active: value.active === undefined ? activePeriod(value) : Boolean(value.active),
      duration_value: String(value.duration_value || ""),
      download_limit: Math.max(0, Number(value.download_limit || 0)),
      institutions: Array.isArray(value.institutions) ? value.institutions : [],
      industries: Array.isArray(value.industries) ? value.industries : [],
      page_ranges: Array.isArray(value.page_ranges) ? value.page_ranges : [],
      source: value.source || "",
      grant_source: value.grant_source || "",
      source_site: value.source_site || "",
      source_plan_code: value.source_plan_code || "",
      source_reference: value.source_reference || "",
      updated_at: value.updated_at || "",
    };
  }
  function accountDisabled(user) { return Boolean(user && user.disabled); }
  function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
  function roleAccessForUser(user) {
    return publicAccessGrant({ email: normalizeEmail(user && user.email), access_mode: "all", status: "active", lifetime: true, source: "role" });
  }
  ${extractFunction(worker, "entitlementAccessForUser")}
  ${extractFunction(worker, "accessGrantExpiryRank")}
  ${extractFunction(worker, "accessChoiceTieRank")}
  ${extractFunction(worker, "longerAccessChoice")}
  ${extractFunction(worker, "effectiveAccessChoiceForUser")}

  const isoAfter = (days) => new Date(Date.now() + days * 86400000).toISOString();
  const user = { email: "kris@kcdesk.com" };
  const admin = {
    email: user.email, access_mode: "filters", status: "active", current_period_end: isoAfter(31),
    duration_value: "1", institutions: ["Bernstein · 伯恩斯坦"], source: "stored",
  };
  const trial = {
    email: user.email, access_mode: "all", status: "active", current_period_end: isoAfter(3),
    duration_value: "trial_3d", download_limit: 10, source: "vid2ppt_trial",
  };
  const monthEntitlement = {
    email: user.email, plan: "annual", status: "active", current_period_end: isoAfter(31),
    grant_source: "vid2ppt_nova", source_plan_code: "NOVA-M",
  };
  result = {
    adminBeatsTrial: effectiveAccessChoiceForUser(user, null, admin, trial),
    adminBeatsLongerPurchase: effectiveAccessChoiceForUser(user, { ...monthEntitlement, current_period_end: isoAfter(365) }, admin, trial),
    longerPurchase: effectiveAccessChoiceForUser(user, monthEntitlement, null, trial),
    longerTrial: effectiveAccessChoiceForUser(user, { ...monthEntitlement, current_period_end: isoAfter(1) }, null, trial),
    lifetimePurchase: effectiveAccessChoiceForUser(user, { ...monthEntitlement, lifetime: true, current_period_end: null }, null, trial),
  };
`, sandbox);

assert.equal(sandbox.result.adminBeatsTrial.kind, "admin");
assert.equal(sandbox.result.adminBeatsTrial.access.access_mode, "filters");
assert.deepEqual(Array.from(sandbox.result.adminBeatsTrial.access.institutions), ["Bernstein · 伯恩斯坦"]);
assert.equal(sandbox.result.adminBeatsLongerPurchase.kind, "admin", "active administrator access is authoritative");
assert.equal(sandbox.result.longerPurchase.kind, "entitlement", "the later purchased membership must beat a shorter trial");
assert.equal(sandbox.result.longerTrial.kind, "trial", "without administrator access, the later valid period wins");
assert.equal(sandbox.result.lifetimePurchase.kind, "entitlement", "lifetime access is the longest period");

const reportAccess = worker.match(/async function reportAccessForUser[\s\S]+?(?=\nasync function accountDownloadDecision)/);
assert.ok(reportAccess, "reportAccessForUser must exist");
assert.match(reportAccess[0], /effectiveChoice\.kind === "admin"/);
assert.match(reportAccess[0], /effectiveChoice\.kind === "entitlement"/);
assert.match(reportAccess[0], /effectiveChoice\.kind === "trial"/);
assert.match(reportAccess[0], /accessGrantMatchesReport\(effectiveAccess/);

assert.match(app, /function accountRightDurationText\(/);
assert.match(app, /return `\$\{institutions\[0\]\}报告下载权限`/);
assert.match(app, /accountRightDurationText\(effective\)/);

const uiSandbox = {};
vm.runInNewContext(`
  ${extractFunction(app, "accountRightLabel")}
  ${extractFunction(app, "accountRightDurationText")}
  ${extractFunction(app, "accountRightExpiryText")}
  ${extractFunction(app, "accountRightUsageText")}
  ${extractFunction(app, "accountRightSummary")}
  summary = accountRightSummary({
    effective_access: {
      active: true,
      access_mode: "filters",
      institutions: ["Bernstein · 伯恩斯坦"],
      industries: [],
      page_ranges: [],
      duration_value: "1",
      current_period_end: "2026-08-26T00:00:00.000Z",
    },
  });
`, uiSandbox);
assert.equal(
  uiSandbox.summary,
  "Bernstein · 伯恩斯坦报告下载权限，1个月，有效期至 2026-08-26",
);

console.log("KCdesk entitlement precedence checks passed.");
