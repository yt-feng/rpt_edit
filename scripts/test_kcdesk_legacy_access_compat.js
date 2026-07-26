const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const app = fs.readFileSync(path.join(root, "kc_desk_notes/site_src/assets/app.js"), "utf8");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");

assert.match(app, /function isLegacyKcdeskSession\(/);
assert.match(app, /!origin \|\| origin === "legacy-unknown"/);
assert.match(app, /sponsorLink\.hidden = !showSponsorOptions/);
assert.match(app, /redeemRow\.hidden = !showSponsorOptions/);
assert.match(app, /id="openVid2pptSponsor"[^>]+hidden/);
assert.match(app, /id="vid2pptRedeemRow" hidden/);
assert.match(app, /contactCard\.hidden = signedIn && isLegacyKcdeskSession\(session\)/);

const accessFunction = worker.match(
  /async function reportAccessForUser[\s\S]+?(?=\nasync function accountDownloadDecision)/,
);
assert.ok(accessFunction, "reportAccessForUser must exist");
const accessSource = accessFunction[0];
const customGrantIndex = accessSource.indexOf("customAccess = accessGrantMatchesReport");
const purchaseLookupIndex = accessSource.indexOf("const purchase = reportId && !baseAccess");
assert.ok(customGrantIndex >= 0, "custom grant matching must remain enabled");
assert.ok(
  purchaseLookupIndex > customGrantIndex,
  "optional purchase lookup must happen after legacy custom access is verified",
);
assert.match(worker, /PGRST205\|report_purchases\.\*schema cache/);
assert.match(worker, /accountKey\("purchases", expected\.source, expected\.report_id, expected\.email\)/);

console.log("KCdesk legacy access compatibility checks passed.");
