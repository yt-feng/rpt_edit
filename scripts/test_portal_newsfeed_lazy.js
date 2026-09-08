"use strict";

// Exercise the real asynchronous ESM loader and the complete extracted module.
// Only DOM/provider/account boundaries are fixtures; no browser or HTTP is used.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const os = require("node:os");
const path = require("node:path");
const { pathToFileURL } = require("node:url");

const root = path.resolve(__dirname, "..");
const appSource = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const moduleSource = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/newsfeed-app.js"), "utf8");
const loaderStart = appSource.indexOf("  const NEWSFEED_APP_ASSET =");
const loaderEnd = appSource.indexOf("  async function initDelivery(", loaderStart);
assert.ok(loaderStart > 0 && loaderEnd > loaderStart, "app retains its Newsfeed-only loader");
const loader = appSource.slice(loaderStart, loaderEnd);
const entry = appSource.slice(appSource.indexOf("  const boot ="), appSource.lastIndexOf("}());"))
  .replace("  boot().catch(", "  export const bootPromise = boot().catch(");
const dependencyNames = moduleSource.match(/  const \{([\s\S]*?)  \} = dependencies;/)[1]
  .split(",").map((value) => value.trim()).filter(Boolean);

function fixture(locale = "zh-Hans") {
  const nodes = new Map();
  const documentEvents = new Map();
  const calls = { config: 0, account: 0, admin: 0, nav: 0, refresh: 0, fetch: [], analytics: [], login: 0 };
  function node(id) {
    const listeners = new Map();
    return {
      id, innerHTML: "", textContent: "", hidden: false, dataset: {}, listeners,
      classList: { add() {}, remove() {}, toggle() {} },
      setAttribute() {},
      addEventListener(type, listener) {
        const current = listeners.get(type) || [];
        current.push(listener);
        listeners.set(type, current);
      },
    };
  }
  for (const id of ["newsfeedApp", "newsfeedContent", "newsfeedStatus", "newsfeedTitle", "newsfeedTopicList",
    "newsfeedTopicCount", "newsfeedPreferences", "newsfeedPolicyNotice", "newsBriefingButton", "newsfeedSidebar"]) {
    nodes.set(id, node(id));
  }
  const document = {
    baseURI: "", body: { dataset: { page: "newsfeed" } },
    getElementById(id) { return nodes.get(id) || null; },
    querySelector() { return null; },
    querySelectorAll() { return []; },
    addEventListener(type, listener) {
      const current = documentEvents.get(type) || [];
      current.push(listener);
      documentEvents.set(type, current);
    },
  };
  const dependencies = {
    CONTENT_LOCALE: locale,
    CONTENT_INTL_LOCALE: { "zh-Hans": "zh-CN", ko: "ko-KR", ja: "ja-JP", ar: "ar-AE" }[locale],
    authHeaders: () => ({ "X-Test-Session": "current" }),
    authUserLabel: () => "Public reader",
    currentAnalyticsPath: () => "/newsfeed.html",
    escapeHtml: (value) => String(value ?? "").replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll('"', "&quot;"),
    initAccountGate: () => { calls.account += 1; },
    initAdminGate: () => { calls.admin += 1; },
    initNewsfeedNav: () => { calls.nav += 1; },
    isLocalizedContentPage: () => locale !== "zh-Hans",
    isNewsfeedSession: (session) => Boolean(session && session.user),
    isSuperSession: () => false,
    loadAuthSession: () => null,
    loadOptionalJson: async () => { calls.config += 1; return {}; },
    localizedServiceMessage: (message, fallback) => message || fallback,
    refreshAuthSession: async () => { calls.refresh += 1; return null; },
    showAccountModal: () => { calls.login += 1; },
    trackEvent: (...values) => calls.analytics.push(values),
    workerBaseUrl: () => "/api",
  };
  const fetch = async (url, options) => {
    calls.fetch.push({ url, options });
    return {
      ok: true,
      json: async () => ({
        topics: [{ id: "global-daily", title: "Global Daily" }],
        headlines: [{ id: "test-article", title: "Public market headline", category: "Investment" }],
        items: [{ id: "explore-article", title: "Technology headline", category: "Tech" }],
        daily_digest: ["Digest fixture"],
      }),
    };
  };
  return { document, nodes, documentEvents, calls, dependencies, fetch };
}

(async () => {
  const directory = fs.mkdtempSync(path.join(os.tmpdir(), "portal-newsfeed-lazy-"));
  const previous = { document: global.document, window: global.window, fetch: global.fetch, dependencies: global.__newsfeedDependencies };
  let sequence = 0;
  try {
    fs.writeFileSync(path.join(directory, "package.json"), '{"type":"module"}');
    async function harness(current, { page = "newsfeed", boot = false, missing = false } = {}) {
      const folder = path.join(directory, `case-${sequence++}`);
      const localeFolder = current.dependencies.CONTENT_LOCALE === "zh-Hans" ? "" : current.dependencies.CONTENT_LOCALE;
      const routeFolder = path.join(folder, localeFolder);
      fs.mkdirSync(path.join(routeFolder, "assets"), { recursive: true });
      if (!missing) fs.writeFileSync(path.join(routeFolder, "assets/newsfeed-app.js"), moduleSource);
      current.document.baseURI = pathToFileURL(path.join(routeFolder, "newsfeed.html")).href;
      global.document = current.document;
      global.window = { location: { reload() {} }, PortalLocale: { contentLocale: current.dependencies.CONTENT_LOCALE } };
      global.fetch = current.fetch;
      global.__newsfeedDependencies = current.dependencies;
      const source = `const { ${dependencyNames.join(", ")} } = globalThis.__newsfeedDependencies;\n`
        + loader + "\nexport { initNewsfeed };\n"
        + (boot ? `const page = ${JSON.stringify(page)};\n`
          + "const noop = async () => {};\nconst initResearch = noop, initContentAccount = noop, initReport = noop, initExternalDetail = noop, initDelivery = noop, initAnalyticsHistory = noop, initBlog = noop, initCourse = noop, initIndex = noop;\n"
          + entry : "");
      const file = path.join(folder, "harness.mjs");
      fs.writeFileSync(file, source);
      return import(pathToFileURL(file).href);
    }

    // Importing the common app loader must not load or initialize Newsfeed.
    for (const page of ["research", "report", "blog", "course", "index"]) {
      const current = fixture();
      const loaded = await harness(current, { page, boot: true, missing: true });
      await loaded.bootPromise;
      assert.equal(current.calls.config, 0, `${page} never requests Newsfeed code or config`);
      assert.equal(current.nodes.get("newsfeedApp").innerHTML, "");
    }

    for (const locale of ["zh-Hans", "ko", "ja", "ar"]) {
      const current = fixture(locale);
      const loaded = await harness(current);
      assert.equal(current.calls.config, 0, "module remains unloaded before Newsfeed initialization");
      const first = loaded.initNewsfeed();
      const second = loaded.initNewsfeed();
      assert.strictEqual(second, first, "concurrent initialization shares one import and one mount");
      await first;
      await new Promise((resolve) => setImmediate(resolve));
      assert.strictEqual(loaded.initNewsfeed(), first, "later calls cannot mount the app a second time");
      assert.equal(current.calls.config, 1);
      assert.equal(current.calls.account, 1);
      assert.equal(current.calls.admin, 1);
      assert.equal(current.calls.nav, 1);
      assert.equal(current.calls.refresh, 1);
      assert.match(current.nodes.get("newsfeedApp").innerHTML, /newsfeed-layout/);
      assert.match(current.nodes.get("newsfeedContent").innerHTML, /Public market headline/);
      assert.equal(current.nodes.get("newsfeedApp").listeners.get("click").length, 1);
      assert.equal(current.documentEvents.get("portal-auth-change").length, 1);
      assert.equal(current.calls.fetch.length, 2, "existing fast then full feed journey is retained");
      if (locale !== "zh-Hans") {
        assert.ok(current.calls.fetch.every(({ url }) => url.includes(`language=${locale}`)), "URL locale reaches the loaded module's data requests");
      }
      assert.ok(current.calls.fetch.every(({ options }) => options.headers["X-Test-Session"] === "current"));
      const click = current.nodes.get("newsfeedApp").listeners.get("click")[0];
      await click({ target: { closest: () => ({ dataset: { action: "show-explore" } }) } });
      assert.match(current.nodes.get("newsfeedContent").innerHTML, /Technology headline/);
      assert.match(current.calls.fetch.at(-1).url, /\/newsfeed\/explore\?/);
      await click({ target: { closest: () => ({ dataset: { action: "show-login" } }) } });
      assert.equal(current.calls.login, 1, "lazy module uses the shared account modal");
    }

    const missing = fixture();
    const failedLoad = await harness(missing, { boot: true, missing: true });
    await failedLoad.bootPromise;
    assert.match(missing.nodes.get("newsfeedApp").innerHTML, /class="error-state"/);
    assert.equal(missing.calls.config, 0, "failed module loading cannot partially mount the Newsfeed app");

    const failedApi = fixture();
    failedApi.fetch = async () => ({ ok: false, status: 503, json: async () => ({ detail: "Feed temporarily unavailable" }) });
    const failedBoot = await harness(failedApi, { boot: true });
    await failedBoot.bootPromise;
    assert.match(failedApi.nodes.get("newsfeedApp").innerHTML, /class="error-state">Feed temporarily unavailable/);
    console.log("portal Newsfeed lazy loading tests passed (real ESM, all locales, shared init, errors and interactions)");
  } finally {
    global.document = previous.document;
    global.window = previous.window;
    global.fetch = previous.fetch;
    global.__newsfeedDependencies = previous.dependencies;
    fs.rmSync(directory, { recursive: true, force: true });
  }
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
