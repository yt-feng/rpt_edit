// Offline VM observation contracts. No real browser, network, socket or disk write.
'use strict';
const test = require('node:test'), assert = require('node:assert/strict');
const fs = require('node:fs'), path = require('node:path'), vm = require('node:vm');
const code = fs.readFileSync(path.join(__dirname, 'cloud_imf_fiscal_observation.cjs'), 'utf8');
const candidate = 'https://elibrary.imf.org/display/book/9798229056298/9798229056298.xml?cid=578448-com-dsp-crossref';
async function simulate(options = {}) {
  const output = [], events = [], handlers = new Map(), frame = {};
  const waitFor = async opts => { assert.equal(opts.timeout, 15000); if (options.unready) {const e = new Error('SECRET');e.name = 'TimeoutError';throw e;} };
  const locator = {first: () => locator, waitFor, allTextContents: async () => ['Fiscal Monitor, October 2026: Special Edition']};
  const page = {
    on: (k, fn) => handlers.set(k, fn), mainFrame: () => frame,
    goto: async (url, opts) => {
      assert.equal(url, candidate); assert.equal(opts.timeout, 45000); events.push('goto');
      handlers.get('response')({request: () => ({isNavigationRequest: () => true}), frame: () => frame, status: () => options.status || 200});
    },
    getByRole: () => locator, url: () => options.finalUrl || candidate, title: async () => options.unready ? 'Human Verification' : 'Fiscal Monitor',
    locator: query => ({
      evaluateAll: async callback => query.startsWith('meta') ? callback([
        {getAttribute: key => ({name: 'citation_doi', content: '10.5089/9798229056298.089'})[key] ?? null},
        {getAttribute: key => ({name: 'unknown', content: 'SECRET'})[key] ?? null}]) : callback([
          {href: 'https://doi.org/10.5089/9798229056298.089'},
          {href: candidate.replace('/display/', '/downloadpdf/display/').replace('.xml', '.pdf').split('?')[0]},
          {href: 'https://user:SECRET@evil.invalid/private.pdf'}]),
      innerText: async () => options.body || 'DOI: 10.5089/9798229056298.089 ISBN: 9798229056298'
    })
  };
  const browser = {newContext: async opts => {assert.equal(opts.acceptDownloads, false); return {newPage: async () => page};},
    close: async () => events.push('close')};
  const processMock = {platform: options.platform || 'linux', argv: ['node', 'helper', '/mock/request.json'],
    env: {GITHUB_ACTIONS: 'true', EXPLICIT_CLOUD_BROWSER_APPROVAL: options.approval || 'true', IMF_CLOUD_SOCKS_PORT: '5555', PLAYWRIGHT_PACKAGE_ROOT: '/mock/runtime'},
    once: () => {}, exit: () => {}, stdout: {write: text => {assert.ok(!text.includes('SECRET'));output.push(JSON.parse(text));}}};
  await vm.runInNewContext(code, {process: processMock, Buffer, URL, require: name => {
    if (name === 'node:fs') return {statSync: () => ({size: 512}), readFileSync: () => JSON.stringify({candidate_url: options.candidate || candidate})};
    if (name === 'node:path') return path;
    assert.equal(name, '/mock/runtime/node_modules/playwright');
    return {chromium: {launch: async opts => {events.push('launch');assert.equal(opts.headless, false);assert.equal(opts.proxy.server, 'socks5://127.0.0.1:5555');return browser;}}};
  }});
  return {events, output};
}
test('one navigation captures public fields, no PDF acceptance and closes before output', async () => {
  const r = await simulate(); assert.equal(r.events.filter(x => x === 'goto').length, 1);
  const p = r.output[0]; assert.equal(p.stage, 'observation'); assert.equal(p.accepted, false); assert.equal(p.pdf_downloads, 0);
  assert.equal(p.landing_status, 200); assert.equal(p.doi_links.length, 1); assert.equal(p.pdf_links.length, 1);
  assert.equal(p.allowed_metadata.unknown, undefined); assert.ok(p.metadata_keys.includes('unknown')); assert.ok(r.events.includes('close'));
});
test('unready 404/challenge page still yields bounded observation without clicking', async () => {
  const r = await simulate({unready: true, status: 404}); assert.equal(r.output[0].ready, false);
  assert.equal(r.output[0].landing_status, 404); assert.equal(r.output[0].pdf_downloads, 0);
});
test('visible body truncates UTF8 at at most 80KiB', async () => {
  const r = await simulate({body: '中'.repeat(100000)}); const p = r.output[0];
  assert.equal(p.body_truncated, true); assert.ok(p.body_bytes <= 81920);
  assert.equal(Buffer.byteLength(p.visible_body), p.body_bytes);
});
test('disabled approval and arbitrary URL fail before launch', async () => {
  for (const options of [{approval: 'false'}, {platform: 'darwin'}, {candidate: 'https://evil.invalid/page'}, {candidate: candidate.replace('9798229056298', '9798229056299')}]) {
    const r = await simulate(options); assert.ok(!r.events.includes('launch')); assert.equal(r.output[0].stage, 'error');
  }
});
test('unexpected redirect refuses unrelated page content', async () => {
  const r = await simulate({finalUrl: 'https://evil.invalid/login'}); assert.equal(r.output[0].category, 'official_redirect_rejected');
  assert.equal(r.output[0].visible_body, undefined);
});

test('only original official tracking query or its removal is accepted', async () => {
  const removed = await simulate({finalUrl: candidate.split('?')[0]}); assert.equal(removed.output[0].stage, 'observation');
  for (const finalUrl of [candidate + '&x=1', candidate.replace('578448', 'different'), candidate + '#fragment']) {
    const r=await simulate({finalUrl}); assert.equal(r.output[0].category, 'official_redirect_rejected');
  }
  const r=await simulate({candidate: candidate.split('?')[0]}); assert.ok(!r.events.includes('launch'));
});
