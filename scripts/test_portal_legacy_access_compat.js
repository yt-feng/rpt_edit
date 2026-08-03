const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");

assert.doesNotMatch(app, /Vid2PPT|NOVA|ATLAS|vid2ppt\.com/);
assert.doesNotMatch(app, /openVid2pptSponsor|vid2pptRedeemRow|accountVid2pptRedeemCode/);
assert.match(app, /如需开通或调整下载权限，请联系微信/);
assert.match(app, /To activate or update download access, email/);
assert.match(
  worker,
  /pathname === "\/vid2ppt\/redeem-code"[\s\S]*?jsonResponse\(request, env, 410/,
  "the former redemption route must reject new redemptions",
);
assert.match(
  worker,
  /\["\/vid2ppt\/nova-grant", "\/vid2ppt\/atlas-grant"\][\s\S]*?jsonResponse\(request, env, 410/,
  "the former grant routes must reject new grants",
);

const accessFunction = worker.match(
  /async function reportAccessForUser[\s\S]+?(?=\nasync function accountDownloadDecision)/,
);
assert.ok(accessFunction, "reportAccessForUser must exist");
const accessSource = accessFunction[0];
const customGrantIndex = accessSource.indexOf("customAccess = accessGrantMatchesReport(access");
const purchaseLookupIndex = accessSource.indexOf(
  "const purchase = reportId && !accessVerificationFailed && !baseAccess",
);
assert.ok(customGrantIndex >= 0, "custom grant matching must remain enabled");
assert.ok(
  purchaseLookupIndex > customGrantIndex,
  "optional purchase lookup must happen after legacy custom access is verified",
);
assert.match(worker, /PGRST205\|report_purchases\.\*schema cache/);
assert.match(worker, /accountKey\("purchases", expected\.source, expected\.report_id, expected\.email\)/);

console.log("Portal Suite legacy access and detached-payment compatibility checks passed.");
