// Offline VM only: no browser executable, HTTP client, socket or file write.
"use strict";
const assert = require('node:assert/strict');
const test = require('node:test');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const {EventEmitter} = require('node:events');
const code = fs.readFileSync(path.join(__dirname, 'imf_cloud_browser.cjs'), 'utf8');
const landing = 'https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml';
const pdf = 'https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf';

async function simulate(options = {}) {
  const pageLanding = options.originalEdition ? landing.replace('-en.', '-es.') : landing;
  const pagePdf = options.originalEdition ? pdf.replace('-en.', '-es.') : pdf;
  const events = [], output = [], responses = new Map(), signals = new Map(), input = new EventEmitter();
  const frame = {}, timers = new Map();
  const metadata = options.metadata || {'citation_doi': ['10.5089/9798229063937.019'],
    'citation_title': ['Republic of Estonia: Consumer Price Index']};
  let counter = 0;
  const wait = async ({timeout}) => {
    events.push('wait'); assert.equal(timeout, 15000);
    if (options.unready) { const e = new Error('SECRET timeout'); e.name = 'TimeoutError'; throw e; }
  };
  const link = {first: () => link, waitFor: wait, all: async () => [link], getAttribute: async () => pagePdf,
    click: async () => {
      events.push('click'); assert.ok(events.indexOf('decision') < events.indexOf('click'));
      responses.get('response')({url: () => pagePdf, status: () => 200,
        request: () => ({isNavigationRequest: () => !!options.pdfNavigation}), frame: () => frame});
    }};
  const heading = {first: () => heading, waitFor: wait, allTextContents: async () => ['Republic of Estonia: Consumer Price Index']};
  const page = {
    on: (key, fn) => responses.set(key, fn), mainFrame: () => frame,
    goto: async (_, opts) => {
      assert.equal(opts.waitUntil, 'domcontentloaded'); assert.equal(opts.timeout, 45000);
      events.push('goto'); responses.get('response')({url: () => pageLanding, status: () => options.landingStatus ?? 200,
        request: () => ({isNavigationRequest: () => true}), frame: () => frame});
    },
    url: () => options.finalUrl || pageLanding, getByRole: role => role === 'heading' ? heading : link,
    locator: query => ({innerText: async opts => {
      assert.equal(query, 'body'); assert.equal(opts.timeout, 10000); events.push('read-body');
      return options.body || 'ISBN: 9798229063937\nLanguage: Spanish';
    }, evaluateAll: async fn => fn(query === 'a[href]' ?
      (options.doiLinks || ['https://doi.org/10.5089/9798229063937.019']).map(href => ({href})) : query.startsWith('meta') ?
      Object.entries(metadata).flatMap(([key, values]) => values.map(value => ({
        getAttribute: name => name === 'name' ? key : name === 'content' ? value : null
      }))) : [{href: pageLanding}])}),
    waitForEvent: async (name, opts) => {
      assert.equal(name, 'download'); assert.equal(opts.timeout, 45000);
      return {url: () => options.changedUrl || pagePdf, failure: async () => null, path: async () => '/mock/download'};
    }
  };
  const browser = {newContext: async opts => {
    assert.deepEqual(JSON.parse(JSON.stringify(opts)), {acceptDownloads: true}); return {newPage: async () => page};
  }, close: async () => { events.push('close'); }};
  input.close = () => { events.push('input-close'); };
  const processMock = {
    env: {GITHUB_ACTIONS: 'true', EXPLICIT_CLOUD_BROWSER_APPROVAL: options.approval ?? 'true',
          IMF_CLOUD_SOCKS_PORT: options.port ?? '5555', PLAYWRIGHT_PACKAGE_ROOT: '/mock/runtime'},
    platform: options.platform || 'linux', argv: ['node', '/mock/helper', '/mock/request.json'], stdin: {},
    once: (key, fn) => signals.set(key, fn), exit: status => { events.push('exit:' + status); },
    stdout: {write: text => {
      const message = JSON.parse(text); output.push(message);
      assert.ok(!text.includes('SECRET'));
      if (message.stage === 'metadata') {
        events.push('metadata');
        queueMicrotask(async () => {
          if (options.terminate) await signals.get('SIGTERM')();
          if (options.noDecision) { [...timers.values()][0](); return; }
          events.push('decision'); input.emit('line', JSON.stringify({pdf_url: options.decision || pagePdf}));
        });
      }
      if (message.stage === 'download') assert.ok(events.includes('close'));
    }}
  };
  await vm.runInNewContext(code, {require: name => {
    if (name === 'node:fs') return {
      statSync: file => ({size: file.endsWith('request.json') ? 512 : options.size ?? 500}),
      readFileSync: () => JSON.stringify({landing_url: pageLanding, max_bytes: 1024,
        observe_original_edition: options.originalEdition ?? false}), constants: {COPYFILE_EXCL: 1},
      copyFileSync: () => { events.push('copy'); }
    };
    if (name === 'node:path') return path;
    if (name === 'node:readline') return {createInterface: () => input};
    assert.equal(name, '/mock/runtime/node_modules/playwright');
    return {chromium: {launch: async opts => {
      events.push('launch');
      assert.deepEqual(JSON.parse(JSON.stringify(opts)), {headless: false, proxy: {server: 'socks5://127.0.0.1:5555'}});
      return browser;
    }}};
  }, process: processMock, URL, Buffer,
  setTimeout: (fn, ms) => { assert.equal(ms, 20000); timers.set(++counter, fn); return counter; },
  clearTimeout: key => timers.delete(key)});
  return {events, output, processMock};
}

test('ordinary navigation waits, emits metadata, waits decision then clicks and closes before completion', async () => {
  const {events, output} = await simulate();
  assert.equal(events.filter(x => x === 'goto').length, 1);
  assert.equal(events.filter(x => x === 'wait').length, 2);
  assert.equal(events.filter(x => x === 'click').length, 1);
  assert.equal(output.length, 2); assert.equal(output[0].stage, 'metadata');
  assert.equal(output[1].stage, 'download'); assert.equal(output[1].pdf_status, 200);
  assert.equal(output[1].landing_status, 200);
});
test('approval, Linux and exact loopback port are checked before launch', async () => {
  for (const options of [{approval: 'false'}, {platform: 'darwin'}, {port: ''}, {port: '65536'}]) {
    const result = await simulate(options); assert.ok(!result.events.includes('launch'));
    assert.equal(result.output.at(-1).stage, 'error');
  }
});
test('unready page uses no reload, click or external request and closes', async () => {
  const result = await simulate({unready: true});
  assert.equal(result.events.filter(x => x === 'goto').length, 1);
  assert.ok(!result.events.includes('click')); assert.ok(result.events.includes('close'));
  assert.equal(result.output[0].stage, 'metadata');
  assert.equal(result.output[0].ready, false);
  assert.ok(result.output[0].metadata.citation_doi);
  assert.equal(result.output.at(-1).category, 'page_not_ready');
});
test('no parent decision times out before any download and closes', async () => {
  const result = await simulate({noDecision: true});
  assert.equal(result.output.at(-1).category, 'download_command_timeout');
  assert.ok(!result.events.includes('click')); assert.ok(result.events.includes('close'));
});
test('unobserved parent URL is rejected without click', async () => {
  const result = await simulate({decision: 'https://evil.invalid/x.pdf'});
  assert.equal(result.output.at(-1).category, 'download_command_invalid');
  assert.ok(!result.events.includes('click')); assert.ok(result.events.includes('close'));
});
test('changed download URL and oversized bytes are not completed', async () => {
  for (const options of [{changedUrl: 'http://www.elibrary.imf.org/file.pdf'}, {size: 2048}]) {
    const result = await simulate(options); assert.ok(!result.events.includes('copy'));
    assert.equal(result.output.at(-1).stage, 'error'); assert.ok(result.events.includes('close'));
  }
});
test('SIGTERM waits for browser close before exiting', async () => {
  const result = await simulate({terminate: true, decision: 'reject'});
  assert.ok(result.events.indexOf('close') < result.events.indexOf('exit:143'));
  assert.ok(!result.events.includes('click'));
});
test('PDF main-frame 200 never overwrites the actual landing HTTP status', async () => {
  const result = await simulate({landingStatus: 405, pdfNavigation: true});
  assert.equal(result.output[0].landing_status, 405);
  assert.equal(result.output.at(-1).landing_status, 405);
  assert.equal(result.output.at(-1).pdf_status, 200);
});
test('only bounded publication metadata aliases are forwarded to strict parent resolver', async () => {
  const result = await simulate({metadata: {'dc.identifier.doi': ['10.5089/9798229063937.019'],
    'prism.doi': ['10.5089/9798229063937.019'], 'dc.title': ['Republic of Estonia: Consumer Price Index'],
    'description': ['SECRET unrelated document metadata']}});
  assert.deepEqual(Object.keys(result.output[0].metadata).sort(), ['canonical_url', 'dc.identifier.doi', 'dc.title', 'prism.doi']);
  assert.deepEqual([...result.output[0].metadata_keys].sort(), ['dc.identifier.doi', 'dc.title', 'description', 'prism.doi']);
});
test('metadata names are deduplicated and have fixed count and character bounds', async () => {
  const repeated = await simulate({metadata: {'citation_title': ['one', 'two']}});
  assert.deepEqual([...repeated.output[0].metadata_keys], ['citation_title']);
  for (const metadata of [{['x'.repeat(129)]: ['unused']}, Object.fromEntries(Array.from({length: 129}, (_, i) => ['field' + i, ['unused']]))]) {
    const result = await simulate({metadata});
    assert.equal(result.output.at(-1).category, 'page_metadata_limit');
    assert.ok(!result.events.includes('click'));
  }
});
test('edition observation reads bounded public labels and DOI anchors but awaits parent before download', async () => {
  const result = await simulate({originalEdition: true, noDecision: true,
    doiLinks: ['https://doi.org/10.5089/9798229063937.019', 'https://evil.invalid/SECRET']});
  assert.equal(result.events.filter(x => x === 'goto').length, 1);
  assert.equal(result.events.filter(x => x === 'read-body').length, 1);
  assert.ok(!result.events.includes('click'));
  assert.deepEqual([...result.output[0].doi_links], ['https://doi.org/10.5089/9798229063937.019']);
  assert.equal(result.output[0].body_truncated, false);
  assert.match(result.output[0].visible_body, /Language: Spanish/);
  const ordinary = await simulate();
  assert.ok(!ordinary.events.includes('read-body'));
  assert.ok(!('visible_body' in ordinary.output[0]));
});
test('edition truncation remains explicit and unrelated redirects are never read', async () => {
  const bounded = await simulate({originalEdition: true, noDecision: true, body: 'á'.repeat(90000)});
  assert.equal(bounded.output[0].body_truncated, true);
  assert.ok(Buffer.byteLength(bounded.output[0].visible_body) <= 80 * 1024);
  for (const finalUrl of ['https://evil.invalid/page', landing.replace('082', '083'), landing]) {
    const result = await simulate({originalEdition: true, finalUrl});
    assert.ok(!result.events.includes('read-body')); assert.ok(!result.events.includes('click'));
    assert.equal(result.output.at(-1).category, 'page_not_ready');
  }
});
test('edition flag accepts only boolean and extra DOI observations are bounded', async () => {
  const invalid = await simulate({originalEdition: 'true'});
  assert.ok(!invalid.events.includes('launch'));
  const excess = await simulate({originalEdition: true,
    doiLinks: Array(17).fill('https://doi.org/10.5089/9798229063937.019')});
  assert.equal(excess.output.at(-1).category, 'page_metadata_limit');
  assert.ok(!excess.events.includes('click'));
});
