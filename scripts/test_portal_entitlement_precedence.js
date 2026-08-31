const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");

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
  const full = extractFunction(source, name);
  return `async ${full}`;
}

const sandbox = {};
vm.runInNewContext(`
  const VID2PPT_GIFT_SOURCES = new Set(["vid2ppt_nova", "vid2ppt_atlas"]);
  const ACTIVE_STATUSES = new Set(["active", "trialing"]);
  const SITE_ORIGIN = "portal";
  const PUBLIC_BRAND = "KC桌面";
  const GIFT_SOURCE_TIME_MARKER = "::grant_at=";
  function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
  function publicBrandText(value, fallback = "") { return String(value || fallback || ""); }
  ${extractFunction(worker, "normalizeGrantOccurredAt")}
  ${extractFunction(worker, "giftSourceReferenceParts")}
  ${extractFunction(worker, "giftSourceReferenceId")}
  ${extractFunction(worker, "giftSourceReferenceOccurredAt")}
  ${extractFunction(worker, "periodIsCurrent")}
  ${extractFunction(worker, "publicEntitlement")}
  function activePeriod(row) {
    return Boolean(row && ACTIVE_STATUSES.has(String(row.status || "inactive"))
      && (row.lifetime || periodIsCurrent(row.current_period_end)));
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
      authority_occurred_at: value.authority_occurred_at || "",
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
  ${extractFunction(worker, "accessChoiceScopeRank")}
  ${extractFunction(worker, "broaderCurrentAccessChoice")}
  ${extractFunction(worker, "accessAuthorityRank")}
  ${extractFunction(worker, "accessChoiceAllowedByAdminDecision")}
  ${extractFunction(worker, "mergedAccessChoiceSource")}
  ${extractFunction(worker, "effectiveAccessChoiceForUser")}
  ${extractFunction(worker, "paddleEntitlementUpdateFields")}

  const isoAfter = (days) => new Date(Date.now() + days * 86400000).toISOString();
  const user = { email: "kris@portal.example.invalid" };
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
  const allSiteAdmin = {
    email: user.email, access_mode: "all", status: "active", lifetime: true,
    duration_value: "lifetime", source: "stored",
  };
  const expiredAdmin = {
    ...admin,
    status: "active",
    current_period_end: isoAfter(-1),
    updated_at: isoAfter(-2),
  };
  const closedAdmin = {
    ...admin,
    access_mode: "none",
    status: "inactive",
    current_period_end: null,
    updated_at: isoAfter(-2),
  };
  const delayedOlderEntitlement = {
    ...monthEntitlement,
    grant_source: "paddle",
    current_period_end: isoAfter(365),
    paddle_last_occurred_at: isoAfter(-3),
    updated_at: isoAfter(-1),
  };
  const newerEntitlement = {
    ...monthEntitlement,
    grant_source: "paddle",
    current_period_end: isoAfter(365),
    paddle_last_occurred_at: isoAfter(-1),
    updated_at: isoAfter(-1),
  };
  const unversionedDelayedEntitlement = {
    ...monthEntitlement,
    grant_source: "paddle",
    current_period_end: isoAfter(365),
    updated_at: isoAfter(-1),
  };
  const mixedOlderGiftWithNewerPaddleResidue = {
    ...monthEntitlement,
    current_period_end: isoAfter(365),
    source_reference: "gift-old::grant_at=" + isoAfter(-3),
    paddle_last_occurred_at: isoAfter(-1),
    updated_at: isoAfter(-1),
  };
  const mixedNewerGiftWithOlderPaddleResidue = {
    ...monthEntitlement,
    current_period_end: isoAfter(365),
    source_reference: "gift-new::grant_at=" + isoAfter(-1),
    paddle_last_occurred_at: isoAfter(-3),
    updated_at: isoAfter(-1),
  };
  const paddleSwitched = paddleEntitlementUpdateFields({
    email: user.email,
    paddle_customer_id: "ctm_123",
    paddle_subscription_id: "sub_123",
  }, {
    eventId: "evt_123",
    occurredAt: isoAfter(-1),
  }, {
    plan: "annual",
    status: "active",
    current_period_end: isoAfter(365),
  });
  result = {
    adminAndTrial: effectiveAccessChoiceForUser(user, null, admin, trial),
    adminAndLongerPurchase: effectiveAccessChoiceForUser(user, { ...monthEntitlement, current_period_end: isoAfter(365) }, admin, trial),
    allSiteAdminAndPurchase: effectiveAccessChoiceForUser(user, monthEntitlement, allSiteAdmin, null),
    longerPurchase: effectiveAccessChoiceForUser(user, monthEntitlement, null, trial),
    longerTrial: effectiveAccessChoiceForUser(user, { ...monthEntitlement, current_period_end: isoAfter(1) }, null, trial),
    lifetimePurchase: effectiveAccessChoiceForUser(user, { ...monthEntitlement, lifetime: true, current_period_end: null }, null, trial),
    expiredAdminBlocksOlderEntitlement: effectiveAccessChoiceForUser(user, delayedOlderEntitlement, expiredAdmin, null),
    closedAdminBlocksOlderEntitlement: effectiveAccessChoiceForUser(user, delayedOlderEntitlement, closedAdmin, null),
    closedAdminBlocksUnversionedDelayedEntitlement: effectiveAccessChoiceForUser(user, unversionedDelayedEntitlement, closedAdmin, null),
    newerEntitlementAfterExpiredAdmin: effectiveAccessChoiceForUser(user, newerEntitlement, expiredAdmin, null),
    mixedOlderGiftBlocked: effectiveAccessChoiceForUser(user, mixedOlderGiftWithNewerPaddleResidue, closedAdmin, null),
    mixedNewerGiftAllowed: effectiveAccessChoiceForUser(user, mixedNewerGiftWithOlderPaddleResidue, closedAdmin, null),
    paddleSwitched,
    paddleSwitchedPublic: publicEntitlement(paddleSwitched),
  };
`, sandbox);

assert.equal(sandbox.result.adminAndTrial.kind, "trial", "the all-site trial is the broader current summary");
assert.deepEqual(
  Array.from(sandbox.result.adminAndTrial.choices, (choice) => choice.kind),
  ["admin", "trial"],
  "a filtered administrator grant and an all-site trial must both remain usable",
);
assert.equal(sandbox.result.adminAndLongerPurchase.kind, "entitlement");
assert.equal(sandbox.result.adminAndLongerPurchase.access.access_mode, "all");
assert.equal(sandbox.result.adminAndLongerPurchase.access.source, "entitlement+stored");
assert.deepEqual(
  Array.from(sandbox.result.adminAndLongerPurchase.choices, (choice) => choice.kind),
  ["admin", "entitlement", "trial"],
  "a NOVA membership must broaden a filtered administrator grant without deleting it",
);
assert.equal(sandbox.result.allSiteAdminAndPurchase.kind, "admin", "a lifetime all-site administrator grant remains the summary");
assert.deepEqual(
  Array.from(sandbox.result.allSiteAdminAndPurchase.choices, (choice) => choice.kind),
  ["admin", "entitlement"],
  "the shorter membership remains an independent component instead of replacing the administrator grant",
);
assert.equal(sandbox.result.longerPurchase.kind, "entitlement", "unlimited membership is preferred over the limited trial summary");
assert.equal(sandbox.result.longerTrial.kind, "entitlement", "an unlimited membership remains the primary summary while both grants are active");
assert.equal(sandbox.result.lifetimePurchase.kind, "entitlement", "lifetime access is the longest period");
assert.equal(sandbox.result.expiredAdminBlocksOlderEntitlement.kind, "admin", "an expired admin decision must block an older all-site entitlement");
assert.equal(sandbox.result.expiredAdminBlocksOlderEntitlement.access.active, false);
assert.equal(sandbox.result.expiredAdminBlocksOlderEntitlement.choices.length, 0);
assert.equal(sandbox.result.closedAdminBlocksOlderEntitlement.kind, "admin", "an explicit admin closure must block an older all-site entitlement");
assert.equal(
  sandbox.result.closedAdminBlocksUnversionedDelayedEntitlement.kind,
  "admin",
  "processing updated_at without a trusted business-event time must not override an admin decision",
);
assert.equal(sandbox.result.newerEntitlementAfterExpiredAdmin.kind, "entitlement", "a genuinely later purchase may replace an expired admin decision");
assert.equal(
  sandbox.result.mixedOlderGiftBlocked.kind,
  "admin",
  "a delayed old gift must not borrow a newer residual Paddle timestamp",
);
assert.equal(
  sandbox.result.mixedNewerGiftAllowed.kind,
  "entitlement",
  "a genuinely newer gift must not be blocked by an older residual Paddle timestamp",
);
assert.equal(sandbox.result.paddleSwitched.grant_source, "paddle");
assert.equal(sandbox.result.paddleSwitched.source_reference, "");
assert.equal(sandbox.result.paddleSwitched.source_plan_code, "");
assert.equal(
  sandbox.result.paddleSwitchedPublic.authority_occurred_at,
  sandbox.result.paddleSwitched.paddle_last_occurred_at,
  "a Paddle writer must explicitly bind current authority to the Paddle event time",
);

const giftReferenceSandbox = {};
vm.runInNewContext(`
  const GIFT_SOURCE_TIME_MARKER = "::grant_at=";
  ${extractFunction(worker, "cleanGrantText")}
  ${extractFunction(worker, "normalizeGrantOccurredAt")}
  ${extractFunction(worker, "encodedGiftSourceReference")}
  ${extractFunction(worker, "giftSourceReferenceParts")}
  ${extractFunction(worker, "giftSourceReferenceId")}
  ${extractFunction(worker, "giftSourceReferenceOccurredAt")}
  encoded = encodedGiftSourceReference("txn_123", "2026-07-27T08:00:00+08:00");
  missingTime = encodedGiftSourceReference("txn_456", "");
  result = {
    id: giftSourceReferenceId(encoded),
    occurredAt: giftSourceReferenceOccurredAt(encoded),
    missingTimeOccurredAt: giftSourceReferenceOccurredAt(missingTime),
  };
`, giftReferenceSandbox);
assert.equal(giftReferenceSandbox.result.id, "txn_123");
assert.equal(giftReferenceSandbox.result.occurredAt, "2026-07-27T00:00:00.000Z");
assert.equal(giftReferenceSandbox.result.missingTimeOccurredAt, "", "missing completed_at must remain untrusted");

const redeemHandler = extractAsyncFunction(worker, "handleVid2PptRedeemCode");
assert.match(redeemHandler, /completedAt:\s*order\.completed_at/);
assert.doesNotMatch(
  redeemHandler,
  /completedAt:\s*order\.completed_at\s*\|\|/,
  "a redemption response without completed_at must not manufacture the current processing time",
);

const reportAccess = worker.match(/async function reportAccessForUser[\s\S]+?(?=\nasync function accountDownloadDecision)/);
assert.ok(reportAccess, "reportAccessForUser must exist");
assert.match(reportAccess[0], /activeChoices\.some/);
assert.match(reportAccess[0], /accessGrantMatchesReport\(access/);
assert.match(reportAccess[0], /effective_access_components/);
assert.match(reportAccess[0], /custom_access_matched/);
assert.match(reportAccess[0], /entitlement_access_matched/);
assert.match(reportAccess[0], /trial_access_matched/);

const adminSnapshotRefresh = worker.match(/async function refreshAdminUsersSnapshot[\s\S]+?(?=\nfunction refreshAdminUsersSnapshotOnce)/);
assert.ok(adminSnapshotRefresh, "refreshAdminUsersSnapshot must exist");
assert.doesNotMatch(
  adminSnapshotRefresh[0],
  /findAccessGrant[\s\S]*?catch\(\(\) => publicAccessGrant\(null\)\)/,
  "an unreadable admin grant must not be displayed as an entitlement-derived all-site grant",
);
assert.match(
  app,
  /loadAccountAdminSummary\(workerUrl, targets\)\.then\([\s\S]*?canManageUsers[\s\S]*?loadFreshAdminUsers\(workerUrl, targets\)/,
  "opening the super admin panel must replace its cached user list with a live verified list",
);
assert.match(
  app,
  /const canManageUsers = !isOperatorOnly;/,
  "the operations panel must distinguish operator-only sessions from the super administrator",
);
assert.match(
  app,
  /if \(targets\.canManageUsers && targets\.exportUsers && document\.getElementById\("accountAdminModal"\)\)/,
  "background refresh must not call the super-only user export endpoint for an operator",
);
assert.match(
  app,
  /if \(canManageUsers && exportUsers\) \{[\s\S]*?loadFreshAdminUsers\(workerUrl, targets\)/,
  "manual refresh must not call the super-only user export endpoint for an operator",
);

assert.match(app, /function accountRightDurationText\(/);
assert.match(app, /return `\$\{institutions\[0\]\}报告下载权限`/);
assert.match(app, /accountRightDurationText\(effective\)/);

const uiSandbox = {
  publicBrandText(value, fallback = "") { return String(value || fallback || ""); },
};
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

(async () => {
  const mergedAccessResult = await vm.runInNewContext(`
    (async () => {
      const VID2PPT_GIFT_SOURCES = new Set(["vid2ppt_nova", "vid2ppt_atlas"]);
      const ACTIVE_STATUSES = new Set(["active", "trialing"]);
      const SITE_ORIGIN = "portal";
      const PUBLIC_BRAND = "KC桌面";
      const GIFT_SOURCE_TIME_MARKER = "::grant_at=";
      function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
      function publicBrandText(value, fallback = "") { return String(value || fallback || ""); }
      ${extractFunction(worker, "normalizeGrantOccurredAt")}
      ${extractFunction(worker, "giftSourceReferenceParts")}
      ${extractFunction(worker, "giftSourceReferenceId")}
      ${extractFunction(worker, "giftSourceReferenceOccurredAt")}
      ${extractFunction(worker, "periodIsCurrent")}
      ${extractFunction(worker, "publicEntitlement")}
      function activePeriod(row) {
        return Boolean(row && ACTIVE_STATUSES.has(String(row.status || "inactive"))
          && (row.lifetime || periodIsCurrent(row.current_period_end)));
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
          authority_occurred_at: value.authority_occurred_at || "",
          updated_at: value.updated_at || "",
        };
      }
      function accountDisabled(user) { return Boolean(user && user.disabled); }
      function isPrivilegedAccount(user) { return Boolean(user && user.privileged); }
      function roleAccessForUser(user) {
        return publicAccessGrant({ email: normalizeEmail(user && user.email), access_mode: "all", status: "active", lifetime: true, source: "role" });
      }
      function superEntitlement() { return { active: true, lifetime: true }; }
      ${extractFunction(worker, "entitlementAccessForUser")}
      ${extractFunction(worker, "accessGrantExpiryRank")}
      ${extractFunction(worker, "accessChoiceTieRank")}
      ${extractFunction(worker, "longerAccessChoice")}
      ${extractFunction(worker, "accessChoiceScopeRank")}
      ${extractFunction(worker, "broaderCurrentAccessChoice")}
      ${extractFunction(worker, "accessAuthorityRank")}
      ${extractFunction(worker, "accessChoiceAllowedByAdminDecision")}
      ${extractFunction(worker, "mergedAccessChoiceSource")}
      ${extractFunction(worker, "effectiveAccessChoiceForUser")}
      ${extractFunction(worker, "shouldConsumeAccessGrantDownload")}

      const isoAfter = (days) => new Date(Date.now() + days * 86400000).toISOString();
      const user = { email: "banban@portal.example.invalid" };
      let currentEntitlement = {
        email: user.email,
        plan: "annual",
        status: "active",
        current_period_end: isoAfter(31),
        grant_source: "vid2ppt_nova",
        source_site: "vid2ppt",
        source_plan_code: "NOVA-M",
      };
      const currentAccess = {
        email: user.email,
        access_mode: "filters",
        status: "active",
        current_period_end: isoAfter(365),
        duration_value: "12",
        institutions: ["Bernstein · 伯恩斯坦"],
        source: "stored",
      };
      const reports = [
        { id: "bernstein", bank_name: "Bernstein · 伯恩斯坦" },
        { id: "nomura", bank_name: "NOM · 野村" },
      ];
      async function findEntitlement() { return currentEntitlement; }
      async function findAccessGrant() { return currentAccess; }
      async function findVid2PptTrialAccess() { return null; }
      async function loadCatalog() { return reports; }
      function findReport(catalog, id) { return catalog.find((report) => report.id === id) || null; }
      function accessGrantMatchesReport(grant, report, source) {
        const access = publicAccessGrant(grant);
        if (!access.active) return false;
        if (access.access_mode === "all") return true;
        return Boolean(source === "catalog" && report && access.institutions.includes(report.bank_name));
      }
      async function findReportPurchase() { return null; }
      function limitedAccessNeedsConsumption(value) {
        const access = publicAccessGrant(value);
        return access.active && access.download_limit > 0;
      }
      ${extractAsyncFunction(worker, "reportAccessForUser")}

      const whilePaidOther = await reportAccessForUser({}, user, "nomura", "catalog");
      const whilePaidBernstein = await reportAccessForUser({}, user, "bernstein", "catalog");
      currentEntitlement = { ...currentEntitlement, current_period_end: isoAfter(-1) };
      const afterExpiryOther = await reportAccessForUser({}, user, "nomura", "catalog");
      const afterExpiryBernstein = await reportAccessForUser({}, user, "bernstein", "catalog");
      const trial = publicAccessGrant({
        access_mode: "all", status: "active", current_period_end: isoAfter(3),
        download_limit: 10, source: "vid2ppt_trial",
      });
      return {
        whilePaidOther,
        whilePaidBernstein,
        afterExpiryOther,
        afterExpiryBernstein,
        unlimitedMembershipConsumption: shouldConsumeAccessGrantDownload({
          ...whilePaidOther,
          trial_access: trial,
          trial_access_matched: true,
        }),
        unlimitedAdminConsumption: shouldConsumeAccessGrantDownload({
          purchase: null,
          entitlement_access_matched: false,
          custom_access_matched: true,
          access: currentAccess,
          trial_access: trial,
          trial_access_matched: true,
        }),
        trialOnlyConsumption: shouldConsumeAccessGrantDownload({
          purchase: null,
          entitlement_access_matched: false,
          custom_access_matched: false,
          trial_access: trial,
          trial_access_matched: true,
        }),
      };
    })()
  `, {});
  assert.equal(mergedAccessResult.whilePaidOther.can_download, true, "NOVA-M must unlock non-Bernstein reports");
  assert.equal(mergedAccessResult.whilePaidOther.entitlement_access_matched, true);
  assert.equal(mergedAccessResult.whilePaidOther.custom_access_matched, false);
  assert.deepEqual(
    Array.from(mergedAccessResult.whilePaidOther.effective_access_components, (choice) => choice.kind),
    ["admin", "entitlement"],
  );
  assert.equal(mergedAccessResult.whilePaidBernstein.can_download, true);
  assert.equal(mergedAccessResult.whilePaidBernstein.entitlement_access_matched, true);
  assert.equal(mergedAccessResult.whilePaidBernstein.custom_access_matched, true);
  assert.equal(mergedAccessResult.afterExpiryOther.can_download, false, "NOVA expiry must not broaden the stored filtered grant");
  assert.equal(mergedAccessResult.afterExpiryBernstein.can_download, true, "the original Bernstein grant must survive NOVA expiry");
  assert.equal(mergedAccessResult.unlimitedMembershipConsumption, null, "NOVA access must not consume a trial quota");
  assert.equal(mergedAccessResult.unlimitedAdminConsumption, null, "an unlimited administrator grant must not consume a trial quota");
  assert.equal(mergedAccessResult.trialOnlyConsumption.storage_kind, "vid2ppt_trial");

  const persistenceSandbox = {};
  const persistenceResult = await vm.runInNewContext(`
    (async () => {
    const ACTIVE_STATUSES = new Set(["active", "trialing"]);
    const VID2PPT_GIFT_SOURCES = new Set(["vid2ppt_nova", "vid2ppt_atlas"]);
    const VID2PPT_PORTAL_GIFT_PLANS = { "NOVA-Q": { months: 3, label: "NOVA quarter" } };
    const VID2PPT_CODE_PATTERN = /^[A-Z0-9][A-Z0-9-]{7,39}$/;
    const GIFT_SOURCE_TIME_MARKER = "::grant_at=";
    const SITE_ORIGIN = "portal";
    const PUBLIC_BRAND = "KC桌面";
    const VID2PPT_SOURCE_SITE = "vid2ppt";
    const TRIAL_3D_DOWNLOAD_LIMIT = 10;
    function normalizeEmail(value) { return String(value || "").trim().toLowerCase(); }
    function publicBrandText(value, fallback = "") { return String(value || fallback || ""); }
    function cleanAccessCount(value) { return Math.max(0, Number(value || 0)); }
    ${extractFunction(worker, "cleanGrantText")}
    ${extractFunction(worker, "cleanGiftPlanCode")}
    ${extractFunction(worker, "normalizeGrantOccurredAt")}
    ${extractFunction(worker, "encodedGiftSourceReference")}
    ${extractFunction(worker, "giftSourceReferenceParts")}
    ${extractFunction(worker, "giftSourceReferenceId")}
    ${extractFunction(worker, "giftSourceReferenceOccurredAt")}
    ${extractFunction(worker, "giftGrantPeriodEnd")}
    ${extractFunction(worker, "normalizeVid2PptCode")}
    ${extractFunction(worker, "giftGrantStartIso")}
    ${extractFunction(worker, "giftGrantSource")}
    ${extractFunction(worker, "sameVid2PptGift")}
    ${extractFunction(worker, "periodIsCurrent")}
    ${extractFunction(worker, "publicEntitlement")}
    let stored = {
      id: "ent-1",
      email: "mixed@portal.example.invalid",
      plan: "annual",
      status: "active",
      lifetime: false,
      current_period_end: "2027-01-01T00:00:00.000Z",
      grant_source: "paddle",
      paddle_customer_id: "ctm_residual",
      paddle_subscription_id: "sub_residual",
      paddle_last_event_id: "evt_residual",
      paddle_last_occurred_at: "2026-07-25T00:00:00.000Z",
      created_at: "2026-01-01T00:00:00.000Z",
      updated_at: "2026-07-25T01:00:00.000Z",
    };
    let saveCount = 0;
    async function findEntitlement() { return stored; }
    async function saveEntitlement(_env, email, fields) {
      saveCount += 1;
      stored = { ...stored, ...fields, email, updated_at: "2026-07-26T00:00:00.000Z" };
      return stored;
    }
    async function insertUsageEvent() { return null; }
    ${extractAsyncFunction(worker, "applyVid2PptGift")}
    const first = await applyVid2PptGift({}, {
      email: "mixed@portal.example.invalid",
      planCode: "NOVA-Q",
      requestId: "gift-before-admin",
      completedAt: "2026-07-20T00:00:00.000Z",
    });
    const firstPublic = publicEntitlement(first.saved);
    const duplicate = await applyVid2PptGift({}, {
      email: "mixed@portal.example.invalid",
      planCode: "NOVA-Q",
      requestId: "gift-before-admin",
      completedAt: "2026-07-20T00:00:00.000Z",
    });
    stored = {
      ...stored,
      grant_source: "paddle",
      source_plan_code: "",
      source_reference: "",
      paddle_last_occurred_at: "2026-07-25T00:00:00.000Z",
    };
    const missingTime = await applyVid2PptGift({}, {
      email: "mixed@portal.example.invalid",
      planCode: "NOVA-Q",
      requestId: "gift-without-time",
      completedAt: "",
    });
    return {
      first,
      firstPublic,
      duplicate,
      saveCount,
      missingTimePublic: publicEntitlement(missingTime.saved),
    };
    })()
  `, persistenceSandbox);
  assert.equal(persistenceResult.first.saved.grant_source, "vid2ppt_nova");
  assert.equal(
    persistenceResult.firstPublic.authority_occurred_at,
    "2026-07-20T00:00:00.000Z",
    "a persisted gift must use its own completed_at despite newer residual Paddle fields",
  );
  assert.equal(persistenceResult.duplicate.duplicate, true, "replaying the same gift must be idempotent");
  assert.equal(persistenceResult.saveCount, 2, "the duplicate replay must not persist a second update");
  assert.equal(
    persistenceResult.missingTimePublic.authority_occurred_at,
    "",
    "a persisted gift without completed_at must remain unable to cross an administrator decision",
  );
  console.log("Portal Suite entitlement precedence checks passed.");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
