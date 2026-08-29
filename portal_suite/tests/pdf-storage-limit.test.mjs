import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerPath, "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    if (source[index] === "}") depth -= 1;
    if (depth === 0) return source.slice(start, index + 1);
  }
  throw new Error(`${name} body is incomplete`);
}

const internalPdfStorageLimitBytes = vm.runInNewContext(
  `(${extractFunction(workerSource, "internalPdfStorageLimitBytes")})`,
);

test("internal PDF storage status defaults to the 100 GiB cleanup threshold", () => {
  assert.equal(internalPdfStorageLimitBytes({}), 100 * 1024 ** 3);
  assert.equal(internalPdfStorageLimitBytes({ PDF_STORAGE_LIMIT_GB: "120" }), 120 * 1024 ** 3);
  assert.equal(internalPdfStorageLimitBytes({ PDF_STORAGE_LIMIT_BYTES: "123456" }), 123456);
});
