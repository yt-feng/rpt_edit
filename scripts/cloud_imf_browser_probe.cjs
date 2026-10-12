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
  const port = process.env.IMF_CLOUD_SOCKS_PORT;
  if (!/^[1-9][0-9]{0,4}$/.test(port || "") || Number(port) > 65535) {
    throw new Error("invalid_cloud_listener");
  }
  const {chromium} = require(path.join(root, "node_modules", "playwright"));
  fs.mkdirSync(OUT, {recursive: true});
  const report = {landing: LANDING, official_pdf_url: PDF, expected_sha256: EXPECTED_SHA,
    expected_pages: 14, accepted: false, source: "normal_official_browser_download", requests_scope: "one_exact_report",
    explicit_cloud_proxy: true, landing_status: null, pdf_status: null};
  const save = () => fs.writeFileSync(path.join(OUT, "browser-summary.json"), JSON.stringify(report, null, 2) + "\n");
  let browser, page;
  const terminate = async () => {
    report.category = "browser_interrupted";
    report.bytes_verified = false;
    save();
    if (browser) await browser.close().catch(() => {});
    process.exit(143);
  };
  process.once("SIGTERM", terminate);
  process.once("SIGINT", terminate);
  save();
  try {
    // Uses only Playwright's pinned bundled cloud browser, no executablePath.
    // Use the normal headed browser on the ephemeral Linux runner display.
    // No fingerprint patches, challenge interaction or exported session state.
    report.browser_mode = "headed";
    browser = await chromium.launch({headless: false,
      proxy: {server: `socks5://127.0.0.1:${port}`}});
    const context = await browser.newContext({acceptDownloads: true});
    page = await context.newPage();
    page.on("response", response => {
      if (response.url() === PDF) report.pdf_status = response.status();
      if (response.request().isNavigationRequest() && response.frame() === page.mainFrame()) {
        report.final_navigation_status = response.status();
      }
    });
    const response = await page.goto(LANDING, {waitUntil: "domcontentloaded", timeout: 45000});
    report.landing_status = response ? response.status() : null;
    report.initial_human_verification_title = (await page.title()).trim().toLowerCase() === "human verification";
    // Wait only for ordinary asynchronous page rendering, within this navigation.
    // No refresh, challenge interaction, session changes or second navigation.
    await Promise.all([
      page.getByRole("heading", {level: 1}).filter({hasText: /Republic of Estonia/})
        .filter({hasText: /Consumer Price Index/}).waitFor({state: "visible", timeout: 15000}),
      page.getByRole("link", {name: /Download PDF/}).waitFor({state: "visible", timeout: 15000})
    ]);
    const finalUrl = new URL(page.url());
    Object.assign(report, {landing_status: response ? response.status() : null,
      official_landing_match: finalUrl.origin === new URL(LANDING).origin &&
        finalUrl.pathname === new URL(LANDING).pathname && !finalUrl.username && !finalUrl.password,
      human_verification_title: (await page.title()).trim().toLowerCase() === "human verification",
      heading_count: await page.getByRole("heading", {level: 1}).count()});
    if (!report.official_landing_match || report.heading_count !== 1) {
      throw new Error("source_identity_mismatch");
    }
    const heading = await page.getByRole("heading", {level: 1}).innerText({timeout: 20000});
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
    if (download.url() !== PDF) throw new Error("official_pdf_link_mismatch");
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
    if (page) {
      try {
        report.human_verification_title = (await page.title()).trim().toLowerCase() === "human verification";
        report.final_human_verification_title = report.human_verification_title;
        if (!report.bytes_verified && report.final_human_verification_title) {
          report.category = "human_verification_not_completed";
        }
      } catch (_) {} // Keep only the last observed fixed classification.
    }
    if (browser) await browser.close().catch(() => {});
    save();
  }
  console.log(JSON.stringify(report));
  if (!report.bytes_verified) process.exitCode = 1;
}
main().catch(() => { console.log(JSON.stringify({category: "browser_probe_setup_failed"})); process.exitCode = 1; });
