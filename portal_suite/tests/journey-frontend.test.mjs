import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const research = await readFile(new URL("../site_src/research.html", import.meta.url), "utf8");
const home = await readFile(new URL("../site_src/index.html", import.meta.url), "utf8");

function functionSource(name) {
  const asyncStart = app.indexOf(`  async function ${name}(`);
  const start = asyncStart >= 0 ? asyncStart : app.indexOf(`  function ${name}(`);
  const next = app.indexOf("\n  }", start);
  assert.ok(start >= 0 && next > start);
  return app.slice(start, next + 4);
}

test("research and article startup initialize account controls without catalog requests or duplicate article views", async () => {
  for (const page of ["research", "blog-article"]) {
    const calls = [];
    const context = vm.createContext({
      page,
      initAccountGate: (url) => calls.push(["account", url]),
      initNewsfeedNav: () => calls.push(["navigation"]),
      trackEvent: (_url, type, data) => calls.push([type, data.page]),
      initIndex: () => { throw new Error("unexpected catalog initialization"); },
      fetch: () => { throw new Error("unexpected catalog request"); },
    });
    const bootSource = app.slice(app.indexOf("  const boot ="), app.indexOf("  boot().catch"));
    vm.runInContext(`${functionSource("initResearch")}\n${functionSource("initContentAccount")}\n${bootSource}\nthis.bootPromise = boot();`, context);
    await context.bootPromise;
    assert.deepEqual(calls.filter(([kind]) => kind === "account"), [["account", "/api"]]);
    assert.deepEqual(calls.filter(([kind]) => kind === "page_view"), page === "research" ? [["page_view", "research"]] : []);
  }
});

function eventElement(attributes = {}) {
  const listeners = new Map();
  return {
    hidden: false, value: "", validity: { valid: true }, style: {}, dataset: {},
    addEventListener(type, listener) {
      const callbacks = listeners.get(type) || [];
      callbacks.push(listener);
      listeners.set(type, callbacks);
    },
    emit(type, event = {}) { for (const callback of listeners.get(type) || []) callback(event); },
    hasAttribute(name) { return Object.hasOwn(attributes, name); },
    getAttribute(name) { return attributes[name] ?? null; },
    setAttribute(name, value) { attributes[name] = value; },
    removeAttribute(name) { delete attributes[name]; },
    insertBefore() {}, remove() {}, focus() {},
    querySelectorAll() { return []; },
    classList: { add() {}, remove() {}, toggle() {} },
  };
}

test("article research navigation inserted at DOMContentLoaded receives one visible entry impression", () => {
  const document = eventElement();
  const signup = eventElement({ "data-auth-open": "register", "data-auth-placement": "navigation", "data-guest-only": "" });
  const checkin = eventElement({ "data-auth-open": "checkin", "data-auth-placement": "daily_goal", "data-member-only": "" });
  const entries = [signup, checkin];
  document.querySelector = () => ({ querySelector: () => signup });
  document.querySelectorAll = (selector) => entries.filter((element) => (
    selector === "[data-guest-only]" ? element.hasAttribute("data-guest-only") :
    selector === "[data-member-only]" ? element.hasAttribute("data-member-only") : true
  ));
  const observed = new Set();
  const events = [];
  let onIntersection;
  const init = vm.runInNewContext(`(${functionSource("initJourneyEntrypoints")})`, {
    document, page: "blog-article", loadAuthSession: () => null,
    trackEvent: (_url, type, payload) => events.push({ type, ...payload }),
    IntersectionObserver: class {
      constructor(callback) { onIntersection = callback; }
      observe(element) { observed.add(element); }
    },
  });
  init("/api");
  const navigation = eventElement({ "data-research-entry": "navigation" });
  entries.push(navigation);
  assert.equal(observed.has(navigation), false);
  document.emit("DOMContentLoaded");
  assert.equal(observed.has(navigation), true);
  assert.equal(checkin.hidden, true);
  onIntersection([{ target: navigation, isIntersecting: true, intersectionRatio: 0.2 }]);
  assert.equal(events.length, 0, "rendering or partial visibility must not count as exposure");
  onIntersection([{ target: navigation, isIntersecting: true, intersectionRatio: 0.7 }]);
  document.emit("portal-auth-change");
  onIntersection([{ target: navigation, isIntersecting: true, intersectionRatio: 1 }]);
  assert.deepEqual(events.map(({ type, action, placement }) => ({ type, action, placement })), [
    { type: "report_chat_interaction", action: "entry_impression", placement: "navigation" },
  ]);
});

test("switching from login to registration records each form start once per modal", async () => {
  const elements = new Map();
  const get = (id) => {
    if (!elements.has(id)) elements.set(id, eventElement());
    return elements.get(id);
  };
  const events = [];
  const showAccount = vm.runInNewContext(`(${functionSource("showAccountModal")})`, {
    page: "research",
    document: { body: { insertAdjacentHTML() {} }, getElementById: get, addEventListener() {} },
    window: { alert() {}, clearInterval, setInterval },
    trackEvent: (_url, _type, payload) => events.push({ ...payload }),
    accountModalMarkup: () => "", loadAuthSession: () => null,
    loadAccountCaptcha: () => Promise.resolve("captcha"),
    registrationNoticeText: () => "账号提示", localizedContactText: (value) => String(value || ""),
  });
  await showAccount("/api", { mode: "login", placement: "research_limit" });
  get("accountAuthForm").emit("input");
  get("accountAuthForm").emit("input");
  get("accountModeToggle").emit("click");
  get("accountAuthForm").emit("input");
  get("accountAuthForm").emit("input");
  get("accountModeToggle").emit("click");
  get("accountAuthForm").emit("input");
  assert.deepEqual(events.filter(({ action }) => action === "form_start"), [
    { action: "form_start", placement: "research_limit", status: "login" },
    { action: "form_start", placement: "research_limit", status: "register" },
  ]);
  get("accountClose").emit("click");
  assert.deepEqual(events.filter(({ action }) => action === "form_abandon"), [
    { action: "form_abandon", placement: "research_limit", status: "login" },
  ]);
});

test("captcha HTML errors show a readable retry message and a successful retry clears it", async () => {
  const image = eventElement({ src: "expired-captcha" });
  const refresh = eventElement();
  const status = eventElement();
  const warnings = [];
  let attempts = 0;
  const loadCaptcha = vm.runInNewContext(`(${functionSource("loadAccountCaptcha")})`, {
    document: { getElementById: (id) => id === "accountCaptchaImage" ? image : refresh },
    console: { warn: (...args) => warnings.push(args) },
    fetch: async () => {
      attempts += 1;
      assert.equal(refresh.disabled, true);
      return attempts === 1
        ? { ok: false, json: async () => { throw new SyntaxError("Unexpected token '<', not valid JSON"); } }
        : { ok: true, json: async () => ({ image: "data:image/svg+xml,test", token: "fresh-token" }) };
    },
  });
  assert.equal(await loadCaptcha("/api", status), "");
  assert.equal(status.textContent, "验证码暂时无法加载，请重试。");
  assert.equal(status.className, "status-line error");
  assert.equal(image.getAttribute("src"), null);
  assert.equal(refresh.disabled, false);
  assert.equal(warnings.length, 1);
  assert.match(warnings[0][1].message, /Unexpected token/u);
  assert.equal(await loadCaptcha("/api", status), "fresh-token");
  assert.equal(image.src, "data:image/svg+xml,test");
  assert.equal(status.textContent, "");
  assert.equal(status.className, "status-line");
  assert.equal(refresh.disabled, false);
});

test("AI research is available before the report list and the workspace has an accessible editable composer", () => {
  assert.ok(home.indexOf('data-research-entry="home_hero"') < home.indexOf('id="results"'));
  assert.match(home, /data-auth-open="register" data-auth-placement="home_hero"/u);
  assert.match(research, /data-page="research"/u);
  assert.match(research, /<label[^>]+for="homeChatInput"/u);
  assert.match(research, /id="homeChatInput"[^>]+maxlength="600"/u);
  assert.match(research, /data-research-prompt=/u);
  assert.doesNotMatch(research, /id="results"|catalog\.json/u);
});
