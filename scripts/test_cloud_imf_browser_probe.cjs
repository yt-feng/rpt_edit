// Offline VM tests only: Playwright, filesystem writes and the browser are mocks.
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const code = fs.readFileSync(path.join(__dirname, "cloud_imf_browser_probe.cjs"), "utf8");
const landing = "https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml";
const pdf = "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf";

async function simulate({ready, port = "5555"}) {
  let launchCount = 0, navigationCount = 0, waitCount = 0, closed = false, titleCalls = 0;
  const saved = new Map(), events = new Map(), frame = {};
  const waitFor = async ({timeout}) => {
    waitCount++;
    assert.equal(timeout, 15000);
    if (!ready) { const error = new Error("private simulated timeout"); error.name = "TimeoutError"; throw error; }
  };
  const heading = {filter: () => heading, waitFor, count: async () => 1,
    innerText: async () => "Republic of Estonia Consumer Price Index"};
  const link = {waitFor, getAttribute: async () => pdf, click: async () => {}};
  const page = {
    on: (event, fn) => events.set(event, fn), mainFrame: () => frame,
    goto: async () => {
      navigationCount++;
      events.get("response")({url: () => landing, status: () => 202,
        request: () => ({isNavigationRequest: () => true}), frame: () => frame});
      return {status: () => 202};
    },
    title: async () => (++titleCalls === 1 || !ready) ? "Human Verification" : "Republic of Estonia",
    url: () => landing, getByRole: role => role === "heading" ? heading : link,
    waitForEvent: async () => ({url: () => pdf, failure: async () => "synthetic download failure"})
  };
  const browser = {newContext: async () => ({newPage: async () => page}), close: async () => { closed = true; }};
  const env = {GITHUB_ACTIONS: "true", EXPLICIT_CLOUD_BROWSER_APPROVAL: "true",
    PLAYWRIGHT_PACKAGE_ROOT: "/mock/runtime", IMF_CLOUD_SOCKS_PORT: port};
  const processMock = {env, platform: "linux", once: () => {}, exit: () => { throw new Error("unexpected exit"); }};
  await vm.runInNewContext(code, {
    require: name => {
      if (name === "node:fs") return {mkdirSync: () => {}, writeFileSync: (file, data) => saved.set(file, data)};
      if (name === "node:path" || name === "node:crypto") return require(name);
      assert.equal(name, "/mock/runtime/node_modules/playwright");
      return {chromium: {launch: async options => {
        launchCount++;
        assert.equal(options.headless, false);
        assert.equal(options.proxy.server, "socks5://127.0.0.1:5555");
        return browser;
      }}};
    },
    process: processMock, URL, console: {log: () => {}}
  });
  const report = saved.has("_imf_browser_probe/browser-summary.json")
    ? JSON.parse(saved.get("_imf_browser_probe/browser-summary.json")) : null;
  return {report, launchCount, navigationCount, waitCount, closed};
}

(async () => {
  const ready = await simulate({ready: true});
  assert.equal(ready.report.initial_human_verification_title, true);
  assert.equal(ready.report.final_human_verification_title, false);
  assert.equal(ready.report.category, "download_failed"); // Reached normal download, not early title rejection.
  assert.equal(ready.report.final_navigation_status, 202);
  assert.equal(ready.waitCount, 2);
  assert.equal(ready.navigationCount, 1);
  assert.equal(ready.closed, true);
  const blocked = await simulate({ready: false});
  assert.equal(blocked.report.category, "human_verification_not_completed");
  assert.equal(blocked.report.final_human_verification_title, true);
  assert.equal(blocked.report.accepted, false);
  assert.equal(blocked.navigationCount, 1);
  assert.equal(blocked.closed, true);
  const denied = await simulate({ready: true, port: ""});
  assert.equal(denied.launchCount, 0);
  console.log("3 offline browser VM cases passed; no browser or network started");
})().catch(error => { console.error(error); process.exitCode = 1; });
