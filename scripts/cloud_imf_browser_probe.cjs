/* One exact PDF main-navigation GET in an explicitly approved cloud browser.
 * No landing request, redirects, challenge resources, login, or second fetch.
 */
"use strict";
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");

const PDF = "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf";
const EXPECTED_SHA = "c31da5c22e845f767b39a0a16679c0f1249ce46b5f60bd0170bdb67964e663b3";
const EXPECTED_BYTES = 365715;
const TOTAL_MS = 60000;
const OUT = "_imf_browser_probe";
const CATEGORIES = new Set([
  "browser_pdf_deadline", "navigation_policy_blocked", "navigation_failed",
  "http_rejected", "non_pdf_content_type", "browser_response_unavailable",
  "pdf_size_mismatch", "pdf_bytes_mismatch"
]);

async function main() {
  if (process.env.GITHUB_ACTIONS !== "true" || process.platform !== "linux" ||
      process.env.EXPLICIT_CLOUD_BROWSER_APPROVAL !== "true") {
    throw new Error("cloud_browser_not_authorized");
  }
  const root = process.env.PLAYWRIGHT_PACKAGE_ROOT;
  if (!root || !path.isAbsolute(root)) throw new Error("invalid_runtime_path");
  const {chromium} = require(path.join(root, "node_modules", "playwright"));
  fs.mkdirSync(OUT, {recursive: true});
  const started = Date.now();
  const deadline = started + TOTAL_MS;
  const report = {
    mode: "direct_exact_pdf", official_pdf_url: PDF, expected_sha256: EXPECTED_SHA,
    expected_bytes: EXPECTED_BYTES, expected_pages: 14, accepted: false, bytes_verified: false,
    identity_basis: "previously_verified_official_pdf_hash", landing_identity_checked: false,
    source: "normal_official_browser_navigation", requests_scope: "one_exact_pdf_navigation_get",
    browser_mode: "headed", total_deadline_ms: TOTAL_MS, navigation_gets: 0,
    blocked_navigation_requests: 0, blocked_other_requests: 0,
    http_status: null, http_status_observed: false, stage: "setup"
  };
  const save = () => fs.writeFileSync(path.join(OUT, "summary.json"), JSON.stringify(report, null, 2) + "\n");
  const remaining = () => Math.max(1, deadline - Date.now() - 1000);
  const bounded = async (promise, category = "browser_pdf_deadline") => {
    let timer;
    try {
      return await Promise.race([promise, new Promise((_, reject) => {
        timer = setTimeout(() => reject(new Error(category)), remaining());
      })]);
    } finally { clearTimeout(timer); }
  };
  let browser, stopped = false;
  const hardDeadline = setTimeout(() => {
    stopped = true;
    Object.assign(report, {category: "browser_pdf_deadline", accepted: false,
      bytes_verified: false, elapsed_ms: Date.now() - started});
    save();
    console.log(JSON.stringify(report));
    if (browser) browser.close().catch(() => {});
    process.exit(1);
  }, TOTAL_MS);
  save();
  try {
    // Only the pinned bundled cloud Chromium; no executablePath, UA, proxy,
    // fingerprint changes, stored session, or challenge interaction.
    browser = await bounded(chromium.launch({headless: false, timeout: remaining()}));
    const context = await bounded(browser.newContext({acceptDownloads: false}));
    const page = await bounded(context.newPage());
    const cdp = await bounded(context.newCDPSession(page));
    const tree = await bounded(cdp.send("Page.getFrameTree"));
    const mainFrame = tree.frameTree.frame.id;
    let firstRequest, resolveResult, rejectResult, settled = false;
    const result = new Promise((resolve, reject) => { resolveResult = resolve; rejectResult = reject; });
    // Attach immediately: a navigation may fail while a paused-response error
    // is already settling the result. Never leave its rejection unhandled.
    result.catch(() => {});
    const fail = category => {
      if (!settled) { settled = true; rejectResult(new Error(category)); }
    };
    const handlePaused = async event => {
      if (stopped || settled) {
        await cdp.send("Fetch.failRequest", {requestId: event.requestId, errorReason: "Aborted"});
        return;
      }
      const isMain = event.frameId === mainFrame && event.resourceType === "Document";
      const responseStage = event.responseStatusCode !== undefined || event.responseErrorReason !== undefined;
      if (!responseStage) {
        if (isMain && event.request.method === "GET" && event.request.url === PDF && report.navigation_gets === 0) {
          firstRequest = event.requestId;
          report.navigation_gets = 1;
          report.stage = "pdf_navigation";
          // Response interception prevents even a redirect from being followed.
          await cdp.send("Fetch.continueRequest", {requestId: event.requestId, interceptResponse: true});
        } else {
          if (isMain) report.blocked_navigation_requests += 1;
          else report.blocked_other_requests += 1;
          if (isMain) fail("navigation_policy_blocked");
          await cdp.send("Fetch.failRequest", {requestId: event.requestId, errorReason: "Aborted"});
        }
        return;
      }
      if (event.requestId !== firstRequest || !isMain || event.request.url !== PDF) {
        await cdp.send("Fetch.failRequest", {requestId: event.requestId, errorReason: "Aborted"});
        fail("navigation_policy_blocked");
        return;
      }
      const status = event.responseStatusCode;
      report.http_status = Number.isInteger(status) ? status : null;
      report.http_status_observed = Number.isInteger(status);
      const headers = event.responseHeaders || [];
      const header = name => headers.find(item => item.name.toLowerCase() === name)?.value || "";
      const mime = header("content-type").split(";", 1)[0].trim().toLowerCase();
      report.content_type = ["application/pdf", "application/octet-stream", "text/html"].includes(mime) ? mime : "other";
      const length = header("content-length");
      report.declared_bytes = /^\d{1,12}$/.test(length) ? Number(length) : null;
      report.stage = "pdf_response";
      let category;
      if (!Number.isInteger(status)) category = "browser_response_unavailable";
      else if (status !== 200) category = "http_rejected";
      else if (!["application/pdf", "application/octet-stream"].includes(mime)) category = "non_pdf_content_type";
      if (category) {
        await cdp.send("Fetch.failRequest", {requestId: event.requestId, errorReason: "Aborted"});
        fail(category);
        return;
      }
      // Read bytes already returned to this exact browser navigation. This is
      // not a second request. Stop the paused navigation after consuming them.
      const body = await cdp.send("Fetch.getResponseBody", {requestId: event.requestId});
      const bytes = Buffer.from(body.body, body.base64Encoded ? "base64" : "utf8");
      await cdp.send("Fetch.failRequest", {requestId: event.requestId, errorReason: "Aborted"});
      if (!settled && !stopped) { settled = true; resolveResult(bytes); }
    };
    cdp.on("Fetch.requestPaused", event => { handlePaused(event).catch(() => fail("browser_response_unavailable")); });
    await bounded(cdp.send("Fetch.enable", {patterns: [{urlPattern: "*", requestStage: "Request"}]}));
    // The expected ERR_ABORTED after consuming/cancelling the intercepted
    // response does not discard its observed HTTP status or original bytes.
    const navigation = page.goto(PDF, {waitUntil: "domcontentloaded", timeout: remaining()});
    navigation.catch(() => { if (!firstRequest) fail("navigation_failed"); });
    const bytes = await bounded(result);
    if (report.navigation_gets !== 1 || report.blocked_navigation_requests !== 0) throw new Error("navigation_policy_blocked");
    if (bytes.length !== EXPECTED_BYTES) throw new Error("pdf_size_mismatch");
    const sha = crypto.createHash("sha256").update(bytes).digest("hex");
    if (bytes.subarray(0, 5).toString() !== "%PDF-" || sha !== EXPECTED_SHA) {
      throw new Error("pdf_bytes_mismatch");
    }
    fs.writeFileSync(path.join(OUT, `${sha}.pdf`), bytes);
    Object.assign(report, {category: "verified_browser_bytes", bytes: bytes.length, sha256: sha,
      delivery: "existing_browser_navigation_response",
      bytes_verified: true, accepted: false, pdf_parser_validation: "required_next_step"});
  } catch (error) {
    report.category = CATEGORIES.has(error.message) ? error.message :
      error.name === "TimeoutError" ? "browser_pdf_deadline" : "browser_probe_failed";
  } finally {
    stopped = true;
    report.elapsed_ms = Date.now() - started;
    save();
    if (browser) {
      try { await bounded(browser.close()); }
      catch (_) { report.cleanup_incomplete = true; save(); }
    }
    clearTimeout(hardDeadline);
  }
  console.log(JSON.stringify(report));
  if (!report.bytes_verified || report.cleanup_incomplete) process.exitCode = 1;
  if (report.cleanup_incomplete) process.exit(1);
}
main().catch(() => { console.log(JSON.stringify({category: "browser_probe_setup_failed"})); process.exitCode = 1; });
