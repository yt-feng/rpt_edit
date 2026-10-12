/* Single-source cloud diagnostic. Execution requires explicit user approval.
 * No local execution, system networking changes, exported cookies, or login.
 */
"use strict";
const fs = require("node:fs");
const path = require("node:path");
const crypto = require("node:crypto");

const LANDING = "https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml";
const PDF = "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf";
const EXPECTED_SHA = "c31da5c22e845f767b39a0a16679c0f1249ce46b5f60bd0170bdb67964e663b3";
const OUT = "_imf_browser_probe";

async function main() {
  if (process.env.GITHUB_ACTIONS !== "true" || process.platform !== "linux" ||
      process.env.EXPLICIT_CLOUD_BROWSER_APPROVAL !== "true") {
    throw new Error("cloud_browser_not_authorized");
  }
  const root = process.env.PLAYWRIGHT_PACKAGE_ROOT;
  if (!root || !path.isAbsolute(root)) throw new Error("invalid_runtime_path");
  const {chromium} = require(path.join(root, "node_modules", "playwright"));
  fs.mkdirSync(OUT, {recursive: true});
  const report = {landing: LANDING, official_pdf_url: PDF, expected_sha256: EXPECTED_SHA,
    expected_pages: 14, accepted: false, source: "normal_official_browser_download", requests_scope: "one_exact_report"};
  const save = () => fs.writeFileSync(path.join(OUT, "summary.json"), JSON.stringify(report, null, 2) + "\n");
  let browser;
  save();
  try {
    // Uses only Playwright's pinned bundled cloud browser, no executablePath.
    browser = await chromium.launch({headless: true});
    const context = await browser.newContext({acceptDownloads: true});
    const page = await context.newPage();
    const response = await page.goto(LANDING, {waitUntil: "domcontentloaded", timeout: 45000});
    const finalUrl = new URL(page.url());
    Object.assign(report, {landing_status: response ? response.status() : null,
      final_host: finalUrl.hostname, final_path: finalUrl.pathname,
      page_title: (await page.title()).slice(0, 300),
      heading_count: await page.getByRole("heading", {level: 1}).count()});
    const heading = await page.getByRole("heading", {level: 1}).innerText({timeout: 20000});
    report.observed_heading = heading.slice(0, 400);
    if (!heading.includes("Republic of Estonia") || !heading.includes("Consumer Price Index")) {
      throw new Error("source_identity_mismatch");
    }
    const link = page.getByRole("link", {name: /Download PDF/});
    const href = new URL(await link.getAttribute("href"), page.url());
    if (href.href !== PDF) throw new Error("official_pdf_link_mismatch");
    const [download] = await Promise.all([
      page.waitForEvent("download", {timeout: 45000}),
      link.click({timeout: 15000})
    ]);
    if (await download.failure()) throw new Error("download_failed");
    const downloaded = await download.path();
    const size = fs.statSync(downloaded).size;
    if (size !== 365715) throw new Error("pdf_size_mismatch");
    const bytes = fs.readFileSync(downloaded);
    const sha = crypto.createHash("sha256").update(bytes).digest("hex");
    if (bytes.subarray(0, 5).toString() !== "%PDF-" || sha !== EXPECTED_SHA) {
      throw new Error("pdf_bytes_mismatch");
    }
    fs.writeFileSync(path.join(OUT, `${sha}.pdf`), bytes);
    Object.assign(report, {category: "verified_browser_bytes", bytes: size, sha256: sha,
      bytes_verified: true, accepted: false, pdf_parser_validation: "required_next_step"});
  } catch (error) {
    const known = new Set(["source_identity_mismatch", "official_pdf_link_mismatch", "download_failed",
      "pdf_size_mismatch", "pdf_bytes_mismatch"]);
    report.category = known.has(error.message) ? error.message :
      error.name === "TimeoutError" ? "browser_source_timeout" : "browser_probe_failed";
  } finally {
    save();
    if (browser) await browser.close();
  }
  console.log(JSON.stringify(report));
  if (!report.bytes_verified) process.exitCode = 1;
}
main().catch(() => { console.log(JSON.stringify({category: "browser_probe_setup_failed"})); process.exitCode = 1; });
