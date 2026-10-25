import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const runtime = await readFile(new URL("../site_src/assets/site-runtime.js", import.meta.url), "utf8");

function functionSource(source, name) {
  const start = source.indexOf(`  function ${name}(`);
  assert.notEqual(start, -1);
  const end = source.indexOf("\n  }", start);
  assert.notEqual(end, -1);
  return source.slice(start, end + 4);
}

function harness() {
  const appended = [];
  const document = {
    head: { append(element) { appended.push(element); } },
    createElement(tagName) { return { tagName, dataset: {} }; },
    querySelector(selector) {
      const isScript = selector === "script[data-site-feedback-loader]";
      return appended.find((element) => element.tagName === (isScript ? "script" : "link")
        && Object.hasOwn(element.dataset, isScript ? "siteFeedbackLoader" : "siteFeedbackStyle"));
    },
  };
  const window = { location: { href: "https://kcdesk.com/en/blog/example.html" } };
  const context = vm.createContext({ document, window, URL, RUNTIME_SCRIPT_URL: "https://kcdesk.com/assets/site-runtime.js" });
  vm.runInContext(`${functionSource(app, "initSiteFeedback")}\n${functionSource(runtime, "loadFeedback")}`, context);
  return { appended, window, context,
    app() { vm.runInContext("initSiteFeedback()", context); },
    runtime() { vm.runInContext("loadFeedback()", context); },
  };
}

test("shared app mounts feedback assets on preserved English and extended pages without site-runtime", () => {
  const h = harness();
  h.app(); h.app();
  assert.equal(h.appended.length, 2);
  assert.equal(h.appended[0].href, "/assets/site-feedback.css?v=feedback-v1");
  assert.equal(h.appended[1].src, "/assets/site-feedback.js?v=feedback-v1");
  assert.equal(h.appended[1].async, true);
});

test("app and site-runtime share one feedback loader in either startup order", () => {
  for (const order of [["app", "runtime"], ["runtime", "app"]]) {
    const h = harness();
    order.forEach((name) => h[name]());
    h.app(); h.runtime();
    assert.equal(h.appended.length, 2, order.join(" then "));
    assert.equal(h.appended.filter((element) => element.tagName === "script").length, 1);
  }
});

test("already-loaded feedback mounts without reloading assets", () => {
  const h = harness();
  let mounts = 0;
  h.window.PortalFeedback = { mount() { mounts += 1; } };
  h.app();
  assert.equal(mounts, 1);
  assert.equal(h.appended.length, 0);
});

test("common feedback startup runs before every page-specific boot", () => {
  const start = app.lastIndexOf("  initSiteFeedback();");
  const end = app.indexOf("  boot().catch", start);
  assert.ok(start > 0 && end > start);
  const bootstrap = app.slice(start, end) + "\n  boot();";
  const bootFunctions = [...new Set([...bootstrap.matchAll(/\binit[A-Z]\w+/g)].map((match) => match[0]))];
  for (const page of ["english-commentary", "blog-article", "report", "external", "research", "index"]) {
    const calls = [];
    const context = { page, document: { getElementById() { return null; } } };
    for (const name of bootFunctions) context[name] = () => calls.push(name);
    vm.runInNewContext(bootstrap, context);
    assert.equal(calls[0], "initSiteFeedback", page);
    assert.equal(calls.length, 2, page);
    if (page === "english-commentary") assert.equal(calls[1], "initEnglishCommentaryAccount");
    if (page === "blog-article") assert.equal(calls[1], "initContentAccount");
  }
});
