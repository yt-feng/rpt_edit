const test = require("node:test");
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const vm = require("node:vm");
const { session, validFull, renderBlocks } = require("../portal_suite/locale_assets/english-commentary.js");
const id = "20261001-aaaaaaaaaaaaaaaa";
const full = () => ({ id, policy: "english-secondary-commentary-v1", access: "free", remaining: 2,
  blocks: [{ tag: "p", text: "Our secondary commentary." }] });

test("reuse only an existing website account session", () => {
  assert.equal(session('not json'), null); assert.equal(session('{}'), null);
  assert.equal(session('{"token":"t"}'), null);
  assert.equal(session('{"token":"t","user":{"id":"account"}}').token, "t");
});
test("full-read display rejects mismatched identity, originals, charts and source-language fallback", () => {
  assert.equal(validFull(full(), id), true);
  for (const changes of [{ id: "wrong" }, { policy: "full-report" }, { access: "public" },
                         { remaining: 4 }, { remaining: null }, { blocks: [] }]) {
    assert.equal(validFull({ ...full(), ...changes }, id), false);
  }
  for (const block of [{ tag: "img", text: "chart" }, { tag: "blockquote", text: "original" },
                       { tag: "p", text: "原文中文" }, { tag: "p", text: "<img src=x>" },
                       { tag: "p", text: "https://example.invalid/original" },
                       { tag: "p", text: "![chart](/chart)" }, { tag: "p", text: "ok", original: true }]) {
    assert.equal(validFull({ ...full(), blocks: [block] }, id), false);
  }
  assert.equal(validFull({ ...full(), access: "member", remaining: null }, id), true);
  assert.equal(validFull({ ...full(), access: "member", remaining: 3 }, id), false);
});
test("approved full text renders only through textContent, not HTML interpolation", () => {
  const doc = { createDocumentFragment: () => ({ children: [], append(node) { this.children.push(node); } }),
    createElement: (tag) => ({ tag, textContent: "" }) };
  const container = { hidden: true, replaceChildren(fragment) { this.children = fragment.children; } };
  renderBlocks(container, full().blocks, doc);
  assert.deepEqual(container.children, [{ tag: "p", textContent: "Our secondary commentary." }]);
  assert.equal(container.hidden, false);
});

function browserFixture(initialSession, fetch) {
  function element(id) {
    return { id, hidden: id !== "englishRead", disabled: false, textContent: "", dataset: { commentaryId: "20261001-aaaaaaaaaaaaaaaa" },
      handlers: {}, children: [], addEventListener(name, handler) { this.handlers[name] = handler; },
      replaceChildren(fragment) { this.children = fragment ? fragment.children : []; } };
  }
  const elements = Object.fromEntries(["englishRead", "englishFullCommentary", "englishReadStatus", "englishMembership"].map((key) => [key, element(key)]));
  const listeners = {}, windowListeners = {}, auth = { value: initialSession };
  const doc = { hidden: false, getElementById: (key) => elements[key],
    addEventListener(name, handler) { listeners[name] = handler; },
    dispatchEvent(event) { this.lastEvent = event; if (listeners[event.type]) listeners[event.type](event); },
    createDocumentFragment: () => ({ children: [], append(node) { this.children.push(node); } }),
    createElement: (tag) => ({ tag, textContent: "" }) };
  const context = vm.createContext({ document: doc, window: { addEventListener(name, handler) { windowListeners[name] = handler; } },
    localStorage: { getItem: () => auth.value }, AbortController, setTimeout, clearTimeout, fetch,
    CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options.detail; } } });
  vm.runInContext(readFileSync(require.resolve("../portal_suite/locale_assets/english-commentary.js"), "utf8"), context);
  return { elements, listeners, windowListeners, doc, auth, click: () => elements.englishRead.handlers.click() };
}
const signedIn = JSON.stringify({ token: "synthetic-session", user: { id: "account" } });

test("anonymous read opens established login and never sends a private-body request", async () => {
  let calls = 0;
  const browser = browserFixture(null, async () => { calls += 1; });
  await browser.click(); assert.equal(calls, 0);
  assert.equal(browser.doc.lastEvent.type, "portal-open-auth"); assert.equal(browser.doc.lastEvent.detail.mode, "login");
  assert.equal(browser.elements.englishFullCommentary.hidden, true);
});
test("authenticated display uses only the authorized commentary endpoint and does not infer membership", async () => {
  const browser = browserFixture(signedIn, async (url, request) => {
    assert.equal(url, "/api/english/commentary/read"); assert.equal(request.method, "POST"); assert.equal(request.cache, "no-store");
    assert.deepEqual(JSON.parse(request.body), { id });
    return { ok: true, status: 200, json: async () => full() };
  });
  await browser.click(); assert.equal(browser.elements.englishFullCommentary.hidden, false);
  assert.equal(browser.elements.englishFullCommentary.children[0].textContent, full().blocks[0].text);
  assert.match(browser.elements.englishReadStatus.textContent, /2 free full reads/);
  browser.listeners["portal-auth-change"]();
  assert.equal(browser.elements.englishFullCommentary.hidden, true); assert.equal(browser.elements.englishFullCommentary.children.length, 0);
});
test("exhausted allowance opens existing membership request action without displaying a body", async () => {
  const browser = browserFixture(signedIn, async () => ({ ok: false, status: 402, json: async () => ({ error: "membership_required" }) }));
  await browser.click(); assert.equal(browser.elements.englishMembership.hidden, false);
  assert.equal(browser.elements.englishFullCommentary.hidden, true); assert.equal(browser.elements.englishRead.disabled, false);
});
test("logout or account switching during an in-flight full read cannot reveal the old account body", async () => {
  let release;
  const browser = browserFixture(signedIn, () => new Promise((resolve) => { release = resolve; }));
  const pending = browser.click(); browser.auth.value = null; browser.listeners["portal-auth-change"]();
  release({ ok: true, status: 200, json: async () => full() }); await pending;
  assert.equal(browser.elements.englishFullCommentary.hidden, true); assert.equal(browser.elements.englishFullCommentary.children.length, 0);
});
test("malformed API body stays undisplayed; hidden/pagehide clears authorized text from the DOM", async () => {
  const browser = browserFixture(signedIn, async () => ({ ok: true, status: 200, json: async () => ({ ...full(), blocks: [{ tag: "img", text: "chart" }] }) }));
  await browser.click(); assert.equal(browser.elements.englishFullCommentary.hidden, true);
  assert.match(browser.elements.englishReadStatus.textContent, /temporarily unavailable/);
  browser.elements.englishFullCommentary.children = [{ textContent: "authorized synthetic text" }]; browser.elements.englishFullCommentary.hidden = false;
  browser.doc.hidden = true; browser.listeners.visibilitychange();
  assert.equal(browser.elements.englishFullCommentary.children.length, 0);
  browser.windowListeners.pagehide(); assert.equal(browser.elements.englishFullCommentary.hidden, true);
});
