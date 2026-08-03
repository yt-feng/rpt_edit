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

const sandbox = {};
vm.runInNewContext(`
  const ACTIVE_STATUSES = new Set(["active", "trialing"]);
  ${extractFunction(worker, "periodIsCurrent")}
  ${extractFunction(worker, "accessGrantActive")}
  ${extractFunction(worker, "shouldRecalculateAccessEnd")}
  const past = new Date(Date.now() - 86400000).toISOString();
  const future = new Date(Date.now() + 86400000).toISOString();
  result = {
    expiredDate: shouldRecalculateAccessEnd({
      activeMode: true, lifetime: false, renew: false, explicitEnd: past,
      existing: { status: "active", lifetime: false, current_period_end: past },
    }),
    futureDate: shouldRecalculateAccessEnd({
      activeMode: true, lifetime: false, renew: false, explicitEnd: future,
      existing: { status: "active", lifetime: false, current_period_end: future },
    }),
    explicitRenew: shouldRecalculateAccessEnd({
      activeMode: true, lifetime: false, renew: true, explicitEnd: future,
      existing: { status: "active", lifetime: false, current_period_end: future },
    }),
    expiredWithoutDate: shouldRecalculateAccessEnd({
      activeMode: true, lifetime: false, renew: false, explicitEnd: null,
      existing: { status: "active", lifetime: false, current_period_end: past },
    }),
    lifetime: shouldRecalculateAccessEnd({
      activeMode: true, lifetime: true, renew: true, explicitEnd: past,
      existing: null,
    }),
  };
`, sandbox);

assert.equal(sandbox.result.expiredDate, true, "an expired explicit date must recalculate from the selected duration");
assert.equal(sandbox.result.futureDate, false, "a future explicit date must be preserved");
assert.equal(sandbox.result.explicitRenew, true, "the renew checkbox must force recalculation");
assert.equal(sandbox.result.expiredWithoutDate, true, "an expired stored grant must not preserve an empty/expired end");
assert.equal(sandbox.result.lifetime, false, "lifetime access does not need a period end");

assert.match(app, /function prepareExpiredAccessRenewal\(/);
assert.match(app, /dataset\.originalAccessActive = access\.active \? "true" : "false"/);
assert.match(app, /targets\.accessExpiry\.value = String\(savedAccess\.current_period_end/);
assert.match(app, /旧权限已过期；保存时将从今天按所选时长重新开通/);

console.log("Portal Suite expired access renewal checks passed.");
