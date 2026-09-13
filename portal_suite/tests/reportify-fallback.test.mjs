import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const workerSource = await readFile(
  new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url),
  "utf8",
);
const appSource = await readFile(
  new URL("../site_src/assets/app.js", import.meta.url),
  "utf8",
);
const grabberSource = await readFile(
  new URL("../../scripts/reportify_pdf_grabber.py", import.meta.url),
  "utf8",
);

test("ordinary Reportify downloads keep the normal path and expose a report request only for upstream failures", () => {
  const handleStart = workerSource.indexOf("async function handleExternalPdf");
  const handleEnd = workerSource.indexOf("async function handleExternalStatus", handleStart);
  assert.ok(handleStart >= 0 && handleEnd > handleStart);
  const handle = workerSource.slice(handleStart, handleEnd);
  assert.match(handle, /accountDownloadDecision\(env, request, id, "external"\)/u);
  assert.doesNotMatch(handle, /if\s*\(\s*!\(await externalAdminRequest/u);
  assert.match(handle, /request_required:\s*true/u);
  assert.match(handle, /request_source:\s*"external"/u);
  assert.match(appSource, /if \(error\.request_required\)/u);
  assert.match(appSource, /showExternalRequestFallback\(/u);
});

test("privileged login recovery uses QR polling and never sends the Reportify token to the browser", () => {
  assert.match(workerSource, /\/external\/login-qr\/status/u);
  assert.match(workerSource, /reportifyStoreToken\(env, token\)/u);
  assert.match(workerSource, /return jsonResponse\(request, env, 200, \{ status: "authenticated", ready: true \}\)/u);
  assert.doesNotMatch(workerSource, /ready:\s*true,\s*token/u);
});

test("the grabber fails closed instead of treating a preview image or printed shell as a PDF", () => {
  const mainStart = grabberSource.indexOf("def main() -> int:");
  assert.ok(mainStart >= 0);
  const main = grabberSource.slice(mainStart);
  assert.match(main, /saved = grabber\.save_result\(\)/u);
  assert.doesNotMatch(main, /try_preview_image_pdf\(/u);
  assert.doesNotMatch(main, /try_print_page_pdf\(/u);
});

test("small cached external PDFs are invalidated instead of reported ready", () => {
  assert.match(workerSource, /function externalPdfLooksLikePreview\(/u);
  assert.match(workerSource, /size < 256 \* 1024 && pages >= 20/u);
  assert.match(workerSource, /REPORT_BUCKET\.delete\(externalObjectKey\(id\)\)/u);
  assert.match(workerSource, /head\.size \|\| 0\) >= 256 \* 1024/u);
});
