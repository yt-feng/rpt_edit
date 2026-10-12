/* Ordinary headed cloud browser. Python validates observed metadata before any
 * download click. Only a per-process cloud SOCKS port enters this subprocess.
 */
"use strict";
const fs = require("node:fs");
const path = require("node:path");
const readline = require("node:readline");

const knownErrors = new Set(["cloud_approval_required", "request_invalid", "page_metadata_limit",
  "download_command_invalid", "download_command_timeout", "download_link_missing", "download_failed",
  "download_url_changed", "download_size_invalid", "page_not_ready"]);
const send = message => process.stdout.write(JSON.stringify(message) + "\n");

function bounded(values, max = 32) {
  if (values.length > max || values.some(x => typeof x !== "string" || x.length > 8192)) {
    throw new Error("page_metadata_limit");
  }
  return values;
}

async function main() {
  if (process.platform !== "linux" || process.env.GITHUB_ACTIONS !== "true" ||
      process.env.EXPLICIT_CLOUD_BROWSER_APPROVAL !== "true") throw new Error("cloud_approval_required");
  const port = process.env.IMF_CLOUD_SOCKS_PORT;
  const root = process.env.PLAYWRIGHT_PACKAGE_ROOT;
  if (!/^[1-9][0-9]{0,4}$/.test(port || "") || +port > 65535 || !root || !path.isAbsolute(root)) {
    throw new Error("request_invalid");
  }
  const requestFile = process.argv[2];
  if (!requestFile || !path.isAbsolute(requestFile) || fs.statSync(requestFile).size > 16384) throw new Error("request_invalid");
  const request = JSON.parse(fs.readFileSync(requestFile, "utf8"));
  const landing = new URL(request.landing_url);
  if (landing.protocol !== "https:" || !["www.elibrary.imf.org", "elibrary.imf.org"].includes(landing.hostname) ||
      landing.username || landing.password || (landing.port && landing.port !== "443") ||
      !Number.isInteger(request.max_bytes) || request.max_bytes < 1 || request.max_bytes > 128 * 1024 * 1024) {
    throw new Error("request_invalid");
  }
  if ("observe_original_edition" in request && typeof request.observe_original_edition !== "boolean") throw new Error("request_invalid");
  if (request.observe_original_edition && !/^\/view\/journals\/(019|029)\/(20\d{2})\/(\d{3})\/\1\.\2\.issue-\3-es\.xml$/.test(landing.pathname)) {
    throw new Error("request_invalid");
  }
  const {chromium} = require(path.join(root, "node_modules", "playwright"));
  let browser, page, landingStatus = null, actualLandingStatus = null, pdfStatus = null, target = null;
  const terminate = async () => {
    if (browser) await browser.close().catch(() => {});
    process.exit(143);
  };
  process.once("SIGTERM", terminate);
  process.once("SIGINT", terminate);
  const input = readline.createInterface({input: process.stdin});
  try {
    browser = await chromium.launch({headless: false, proxy: {server: `socks5://127.0.0.1:${port}`}});
    const context = await browser.newContext({acceptDownloads: true});
    page = await context.newPage();
    page.on("response", response => {
      if (response.request().isNavigationRequest() && response.frame() === page.mainFrame()) landingStatus = response.status();
      if (target && response.url() === target) pdfStatus = response.status();
    });
    await page.goto(request.landing_url, {waitUntil: "domcontentloaded", timeout: 45000});
    const readiness = await Promise.allSettled([
      page.getByRole("heading", {level: 1}).first().waitFor({state: "visible", timeout: 15000}),
      page.getByRole("link", {name: /Download PDF/i}).first().waitFor({state: "visible", timeout: 15000})
    ]);
    const pageReady = readiness.every(result => result.status === "fulfilled");
    // Preserve the same bounded public observation on an unready/challenge page.
    // Neither parent nor child may authorize a download when readiness failed.
    const metaNames = await page.locator("meta[name],meta[property]").evaluateAll(nodes => {
      const names = [], seen = new Set();
      for (const node of nodes) {
        for (const attr of ["name", "property"]) {
          const name = node.getAttribute(attr);
          if (name === null || seen.has(name)) continue;
          if (name.length > 128 || names.length >= 128) return {limit: true};
          seen.add(name); names.push(name);
        }
      }
      return {names};
    });
    if (metaNames.limit) throw new Error("page_metadata_limit");
    const metadata = await page.locator("meta[name],meta[property]").evaluateAll(nodes => {
      const allow = new Set(["citation_doi", "dc.identifier.doi", "prism.doi", "citation_title", "dc.title",
        "citation_isbn", "citation_pdf_url"]);
      const result = {};
      for (const node of nodes) {
        const key = (node.getAttribute("name") || node.getAttribute("property") || "").toLowerCase();
        if (allow.has(key)) (result[key] ||= []).push(node.getAttribute("content") || "");
      }
      return result;
    });
    metadata.canonical_url = await page.locator('link[rel="canonical"]').evaluateAll(nodes => nodes.map(n => n.href));
    for (const values of Object.values(metadata)) bounded(values);
    const h1s = bounded(await page.getByRole("heading", {level: 1}).allTextContents());
    const links = await page.getByRole("link", {name: /Download PDF/i}).all();
    if (links.length > 32) throw new Error("page_metadata_limit");
    const hrefs = [];
    for (const link of links) {
      const href = await link.getAttribute("href");
      if (href) hrefs.push(new URL(href, page.url()).href);
    }
    const downloadHrefs = bounded(hrefs);
    let editionObservation = {};
    if (request.observe_original_edition) {
      const final = new URL(page.url());
      if (final.protocol !== "https:" || !["www.elibrary.imf.org", "elibrary.imf.org"].includes(final.hostname) ||
          final.username || final.password || (final.port && final.port !== "443") ||
          final.pathname !== landing.pathname || final.search || final.hash) throw new Error("page_not_ready");
      const doiLinks = await page.locator('a[href]').evaluateAll(nodes => nodes.map(n => n.href).filter(href =>
        /^https:\/\/doi\.org\/10\.5089\/97[89]\d{10}\.(019|029)$/.test(href)));
      bounded(doiLinks, 16);
      const raw = await page.locator('body').innerText({timeout: 10000});
      const bytes = Buffer.from(raw, 'utf8');
      const truncated = bytes.length > 80 * 1024;
      const body = bytes.subarray(0, 80 * 1024).toString('utf8').replace(/\uFFFD$/, '');
      editionObservation = {doi_links: doiLinks, visible_body: body, body_truncated: truncated};
    }
    // Start waiting before emitting metadata, so a prompt Python reply is kept.
    const command = new Promise((resolve, reject) => {
      const timer = setTimeout(() => reject(new Error("download_command_timeout")), 20000);
      input.once("line", line => {
        clearTimeout(timer);
        try {
          if (Buffer.byteLength(line) > 8192) throw new Error();
          const value = JSON.parse(line);
          if (Object.keys(value).join() !== "pdf_url" || !downloadHrefs.includes(value.pdf_url)) throw new Error();
          resolve(value.pdf_url);
        } catch (_) { reject(new Error("download_command_invalid")); }
      });
    });
    actualLandingStatus = landingStatus;
    send({stage: "metadata", final_url: page.url(), landing_status: actualLandingStatus, ready: pageReady,
      metadata, metadata_keys: metaNames.names, h1s, download_hrefs: downloadHrefs, ...editionObservation});
    target = await command;
    if (!pageReady) throw new Error("page_not_ready");
    // Parent bound this exact observed URL to the DOI and issue/book. Refuse
    // external/downgraded transport even if a caller supplied a bad command.
    const pdf = new URL(target);
    if (pdf.protocol !== "https:" || !["www.elibrary.imf.org", "elibrary.imf.org"].includes(pdf.hostname) ||
        pdf.username || pdf.password || (pdf.port && pdf.port !== "443")) throw new Error("download_command_invalid");
    let chosen;
    for (const link of links) {
      if (new URL(await link.getAttribute("href"), page.url()).href === target) { chosen = link; break; }
    }
    if (!chosen) throw new Error("download_link_missing");
    const [download] = await Promise.all([page.waitForEvent("download", {timeout: 45000}), chosen.click({timeout: 15000})]);
    if (download.url() !== target) throw new Error("download_url_changed");
    if (await download.failure()) throw new Error("download_failed");
    const downloaded = await download.path();
    const size = fs.statSync(downloaded).size;
    if (!(size > 0 && size <= request.max_bytes)) throw new Error("download_size_invalid");
    fs.copyFileSync(downloaded, path.join(path.dirname(requestFile), "download.pdf"), fs.constants.COPYFILE_EXCL);
    await browser.close();
    browser = null;
    send({stage: "download", pdf_url: target, landing_status: actualLandingStatus, pdf_status: pdfStatus});
  } catch (error) {
    send({stage: "error", category: knownErrors.has(error.message) ? error.message :
      error.name === "TimeoutError" ? "browser_timeout" : "browser_failed",
      landing_status: landingStatus, pdf_status: pdfStatus});
    process.exitCode = 1;
  } finally {
    input.close();
    if (browser) await browser.close().catch(() => {});
  }
}
main().catch(() => { send({stage: "error", category: "browser_setup_failed"}); process.exitCode = 1; });
