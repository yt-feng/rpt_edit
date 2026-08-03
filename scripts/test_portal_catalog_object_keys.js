#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");

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

const sandbox = { result: null };
vm.runInNewContext(`
  const DEFAULT_R2_PREFIX = "reports";
  ${extractFunction(worker, "validatedCatalogR2Prefix")}
  ${extractFunction(worker, "objectKeyForReport")}
  result = { validatedCatalogR2Prefix, objectKeyForReport };
`, sandbox);

const { validatedCatalogR2Prefix, objectKeyForReport } = sandbox.result;
const reportId = "0123456789abcdef01234567";

assert.equal(validatedCatalogR2Prefix("/catalog/reports-v2/"), "catalog/reports-v2");
assert.equal(
  objectKeyForReport({ R2_OBJECT_PREFIX: "reports-new" }, { id: reportId }),
  `reports-new/${reportId}.pdf`,
);
assert.equal(
  objectKeyForReport(
    { R2_OBJECT_PREFIX: "reports-new" },
    { id: reportId, r2_key: `reports-old/${reportId}.pdf` },
  ),
  `reports-old/${reportId}.pdf`,
  "a valid persisted key must survive an old-to-new prefix migration",
);

for (const prefix of [
  "_hot-reports/pdfs",
  "reportify",
  "thinktank/pdfs",
  "reports/../_hot-reports",
  "reports//nested",
  "reports with spaces",
  "reports\nmalformed",
]) {
  assert.throws(
    () => objectKeyForReport({ R2_OBJECT_PREFIX: prefix }, { id: reportId }),
    /prefix is (?:invalid|reserved)/,
    `configured prefix must be rejected: ${JSON.stringify(prefix)}`,
  );
}

for (const persisted of [
  `_hot-reports/pdfs/${reportId}.pdf`,
  `reportify/${reportId}.pdf`,
  `reports/abcdef0123456789abcdef01.pdf`,
  `/reports/${reportId}.pdf`,
  `reports/${reportId}.pdf/extra`,
  `reports/${reportId}.pdf `,
]) {
  assert.throws(
    () => objectKeyForReport(
      { R2_OBJECT_PREFIX: "reports" },
      { id: reportId, r2_key: persisted },
    ),
    /storage (?:key|prefix) is (?:invalid|reserved)/,
    `persisted object key must be rejected: ${JSON.stringify(persisted)}`,
  );
}

assert.throws(
  () => objectKeyForReport(
    { R2_OBJECT_PREFIX: "_hot-reports/pdfs" },
    { id: reportId, r2_key: `reports-old/${reportId}.pdf` },
  ),
  /prefix is (?:invalid|reserved)/,
  "the current environment prefix must be validated even for a persisted old key",
);

const descriptor = extractFunction(worker, "catalogReportPdfDescriptor");
assert.match(descriptor, /objectKeyForReport\(env, report\)/);
assert.doesNotMatch(descriptor, /objectKeyForReport\(env, id\)/);

console.log("portal catalog Worker object-key guards passed");
