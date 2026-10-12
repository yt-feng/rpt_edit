/* Temporary read-only official page observation. No PDF clicks or HTTP fetch API. */
'use strict';
const fs = require('node:fs');
const path = require('node:path');
const known = new Set(['cloud_approval_required', 'request_invalid', 'observation_limit', 'official_redirect_rejected']);
const send = data => {
  const encoded = JSON.stringify(data) + '\n';
  if (Buffer.byteLength(encoded) > 256 * 1024) throw new Error('observation_limit');
  process.stdout.write(encoded);
};
function bounded(values, count, length) {
  const unique = [...new Set(values)];
  if (unique.length > count || unique.some(x => typeof x !== 'string' || x.length > length)) throw new Error('observation_limit');
  return unique;
}
async function main() {
  if (process.platform !== 'linux' || process.env.GITHUB_ACTIONS !== 'true' ||
      process.env.EXPLICIT_CLOUD_BROWSER_APPROVAL !== 'true') throw new Error('cloud_approval_required');
  const port = process.env.IMF_CLOUD_SOCKS_PORT, root = process.env.PLAYWRIGHT_PACKAGE_ROOT;
  if (!/^[1-9][0-9]{0,4}$/.test(port || '') || +port > 65535 || !root || !path.isAbsolute(root)) throw new Error('request_invalid');
  const input = process.argv[2];
  if (!input || !path.isAbsolute(input) || fs.statSync(input).size > 8192) throw new Error('request_invalid');
  const request = JSON.parse(fs.readFileSync(input, 'utf8'));
  const candidate = new URL(request.candidate_url);
  if (candidate.protocol !== 'https:' || !['www.elibrary.imf.org', 'elibrary.imf.org'].includes(candidate.hostname) ||
      candidate.username || candidate.password || candidate.port || candidate.search || candidate.hash ||
      !/^\/view\/journals\/(019|029)\/(20[0-9]{2})\/([0-9]{3})\/\1\.\2\.issue-\3-es\.xml$/.test(candidate.pathname)) throw new Error('request_invalid');
  const {chromium} = require(path.join(root, 'node_modules/playwright'));
  let browser, page, status = null;
  const terminate = async () => { if (browser) await browser.close().catch(() => {}); process.exit(143); };
  process.once('SIGTERM', terminate); process.once('SIGINT', terminate);
  try {
    browser = await chromium.launch({headless: false, proxy: {server: `socks5://127.0.0.1:${port}`}});
    const context = await browser.newContext({acceptDownloads: false});
    page = await context.newPage();
    page.on('response', response => {
      if (response.request().isNavigationRequest() && response.frame() === page.mainFrame()) status = response.status();
    });
    await page.goto(candidate.href, {waitUntil: 'domcontentloaded', timeout: 45000});
    const readiness = await Promise.allSettled([
      page.getByRole('heading', {level: 1}).first().waitFor({state: 'visible', timeout: 15000}),
      page.getByRole('link', {name: /Download PDF/i}).first().waitFor({state: 'visible', timeout: 15000})
    ]);
    const final = new URL(page.url());
    if (final.protocol !== 'https:' || !['www.elibrary.imf.org', 'elibrary.imf.org'].includes(final.hostname) ||
        final.username || final.password || final.port || final.search || final.hash || final.pathname !== candidate.pathname) {
      throw new Error('official_redirect_rejected');
    }
    const meta = await page.locator('meta[name],meta[property]').evaluateAll(nodes => {
      const names = [], values = {};
      const allow = new Set(['citation_doi', 'dc.identifier.doi', 'prism.doi', 'citation_isbn', 'dc.identifier.isbn',
        'citation_title', 'dc.title', 'citation_pdf_url']);
      for (const node of nodes) {
        for (const attr of ['name', 'property']) {
          const name = node.getAttribute(attr);
          if (name === null) continue;
          names.push(name);
          if (allow.has(name.toLowerCase())) (values[name.toLowerCase()] ||= []).push(node.getAttribute('content') || '');
        }
      }
      return {names, values};
    });
    const keys = bounded(meta.names, 128, 128);
    for (const [key, values] of Object.entries(meta.values)) meta.values[key] = bounded(values, 8, 2048);
    const h1s = bounded(await page.getByRole('heading', {level: 1}).allTextContents(), 32, 4096);
    const links = await page.locator('a[href]').evaluateAll(nodes => nodes.map(x => x.href));
    const doiLinks = [], pdfLinks = [];
    for (const href of links) {
      try {
        const u = new URL(href);
        if (u.protocol !== 'https:' || u.username || u.password || u.port || u.hash) continue;
        if (u.hostname === 'doi.org' && /^\/10\.5089\/[0-9]{13}\.[0-9]{3}$/.test(u.pathname) && !u.search) doiLinks.push(u.href);
        if (['www.elibrary.imf.org', 'elibrary.imf.org'].includes(u.hostname) && u.pathname.endsWith('.pdf')) pdfLinks.push(u.href);
      } catch (_) {}
    }
    const body = await page.locator('body').innerText({timeout: 10000});
    const bytes = Buffer.from(body, 'utf8');
    const excerpt = bytes.length <= 81920 ? body : bytes.subarray(0, 81920).toString('utf8').replace(/\uFFFD$/, '');
    const title = await page.title();
    if (title.length > 4096 || page.url().length > 4096) throw new Error('observation_limit');
    const result = {stage: 'observation', accepted: false, landing_status: status, final_url: page.url(), title,
      ready: readiness.every(x => x.status === 'fulfilled'), h1s, metadata_keys: keys, allowed_metadata: meta.values,
      doi_links: bounded(doiLinks, 16, 1024), pdf_links: bounded(pdfLinks, 32, 1024),
      visible_body: excerpt, body_bytes: Buffer.byteLength(excerpt), body_truncated: bytes.length > 81920, pdf_downloads: 0};
    await browser.close(); browser = null;
    send(result);
  } catch (error) {
    send({stage: 'error', category: known.has(error.message) ? error.message : error.name === 'TimeoutError' ? 'observer_timeout' : 'observer_failed',
      landing_status: status, accepted: false, pdf_downloads: 0});
    process.exitCode = 1;
  } finally { if (browser) await browser.close().catch(() => {}); }
}
main().catch(() => { send({stage: 'error', category: 'observer_setup_failed', accepted: false, pdf_downloads: 0}); process.exitCode = 1; });
