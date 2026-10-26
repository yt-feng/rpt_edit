const test = require("node:test");
const assert = require("node:assert/strict");
const { readFileSync } = require("node:fs");
const { execFileSync } = require("node:child_process");
const path = require("node:path");
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

function browserFixture(initialSession, fetch, options = {}) {
  function element(id) {
    return { id, hidden: id !== "englishRead", disabled: false, textContent: "", dataset: { commentaryId: "20261001-aaaaaaaaaaaaaaaa" },
      handlers: {}, children: [], addEventListener(name, handler) { this.handlers[name] = handler; },
      replaceChildren(fragment) { this.children = fragment ? fragment.children : []; } };
  }
  const elements = Object.fromEntries(["englishRead", "englishFullCommentary", "englishReadStatus", "englishMembership"].map((key) => [key, element(key)]));
  const listeners = {}, windowListeners = {}, auth = {};
  const storageKey = options.storageKey || "portal_auth_session";
  const storage = new Map(Object.entries(options.extraStorage || {})), removedKeys = [];
  if (initialSession != null) storage.set(storageKey, initialSession);
  Object.defineProperty(auth, "value", {
    get: () => storage.get(storageKey) || null,
    set: (value) => value == null ? storage.delete(storageKey) : storage.set(storageKey, value),
  });
  const doc = { hidden: false, getElementById: (key) => elements[key],
    addEventListener(name, handler) { listeners[name] = handler; },
    dispatchEvent(event) { this.lastEvent = event; if (listeners[event.type]) listeners[event.type](event); },
    createDocumentFragment: () => ({ children: [], append(node) { this.children.push(node); } }),
    createElement: (tag) => ({ tag, textContent: "" }) };
  const context = vm.createContext({ document: doc, window: { addEventListener(name, handler) { windowListeners[name] = handler; } },
    localStorage: { getItem: (key) => storage.get(key) || null,
      removeItem(key) { removedKeys.push(key); storage.delete(key); } }, AbortController, setTimeout, clearTimeout, fetch,
    CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options?.detail; } } });
  vm.runInContext(options.source || readFileSync(require.resolve("../portal_suite/locale_assets/english-commentary.js"), "utf8"), context);
  return { elements, listeners, windowListeners, doc, auth, storage, removedKeys, click: () => elements.englishRead.handlers.click() };
}
const signedIn = JSON.stringify({ token: "synthetic-session", user: { id: "account" } });

const deployedSessionKey = "synthetic_deployment_auth_session";
let deployedSource;
function deployedFixture(initialSession, fetch, options = {}) {
  if (!deployedSource) {
    // Exercise the real final-asset binder with the same namespace rewrite as
    // deployment. The public source alone cannot expose this integration bug.
    deployedSource = execFileSync("python3", ["-B", "-c", `
import pathlib, re, sys
sys.path.insert(0, sys.argv[1])
from portal_english_ui import bind_account_session
script = pathlib.Path(sys.argv[2]).read_bytes()
app = pathlib.Path(sys.argv[3]).read_bytes()
app, changed = re.subn(rb'const AUTH_SESSION_KEY = "[^"]+";',
                      ('const AUTH_SESSION_KEY = "'+sys.argv[4]+'";').encode(), app)
assert changed == 1
sys.stdout.buffer.write(bind_account_session(script, app))
`, __dirname, require.resolve("../portal_suite/locale_assets/english-commentary.js"),
      path.resolve(__dirname, "../portal_suite/site_src/assets/app.js"), deployedSessionKey], { encoding: "utf8" });
  }
  return browserFixture(initialSession, fetch, { ...options, source: deployedSource, storageKey: deployedSessionKey });
}

test("the final deployment namespace reuses the signed-in account and directly reads full commentary", async () => {
  let calls = 0;
  const browser = deployedFixture(signedIn, async (url, request) => {
    calls++;
    assert.equal(url, "/api/english/commentary/read");
    assert.equal(request.headers.Authorization, "Bearer synthetic-session");
    return { ok: true, status: 200, json: async () => full() };
  });
  await browser.click();
  assert.equal(calls, 1); assert.equal(browser.doc.lastEvent, undefined);
  assert.equal(browser.elements.englishFullCommentary.hidden, false);
  assert.equal(browser.elements.englishFullCommentary.children[0].textContent, full().blocks[0].text);
});

test("a deployment session cannot be substituted by the unbound source namespace", async () => {
  let calls = 0;
  const browser = deployedFixture(null, async () => { calls++; }, { extraStorage: { portal_auth_session: signedIn } });
  await browser.click();
  assert.equal(calls, 0); assert.equal(browser.doc.lastEvent.type, "portal-open-auth");
  assert.equal(browser.elements.englishFullCommentary.hidden, true);
});

test("guest login in the deployment namespace resumes the requested read exactly once", async () => {
  let calls = 0;
  const browser = deployedFixture(null, async () => { calls++; return { ok: true, status: 200, json: async () => full() }; });
  await browser.click(); assert.equal(calls, 0);
  assert.equal(browser.doc.lastEvent.type, "portal-open-auth");
  browser.auth.value = signedIn;
  browser.listeners["portal-auth-change"]();
  browser.listeners["portal-auth-complete"]({ detail: { placement: "english_commentary", resumeIntent: true } });
  await new Promise(setImmediate);
  assert.equal(calls, 1); assert.equal(browser.elements.englishFullCommentary.hidden, false);
});

test("a rejected deployment session clears its actual key while preserving unrelated storage", async () => {
  const browser = deployedFixture(signedIn, async () => ({ ok: false, status: 401, json: async () => ({ error: "unauthorized" }) }),
    { extraStorage: { portal_auth_session: "unrelated-source-value" } });
  await browser.click();
  assert.equal(browser.auth.value, null);
  assert.deepEqual(browser.removedKeys, [deployedSessionKey]);
  assert.equal(browser.storage.get("portal_auth_session"), "unrelated-source-value");
  assert.equal(browser.doc.lastEvent.type, "portal-open-auth");
  assert.equal(browser.elements.englishFullCommentary.hidden, true);
});

test("cross-tab logout under the deployment session key clears previously authorized commentary", async () => {
  const browser = deployedFixture(signedIn, async () => ({ ok: true, status: 200, json: async () => full() }));
  await browser.click(); assert.equal(browser.elements.englishFullCommentary.hidden, false);
  browser.auth.value = null;
  browser.windowListeners.storage({ key: "portal_auth_session" });
  assert.equal(browser.elements.englishFullCommentary.hidden, false);
  browser.windowListeners.storage({ key: deployedSessionKey });
  assert.equal(browser.elements.englishFullCommentary.hidden, true);
  assert.equal(browser.elements.englishFullCommentary.children.length, 0);
});

test("a requested read resumes once after login without requiring a second button click", async () => {
  let calls = 0;
  const browser = browserFixture(null, async () => { calls++; return { ok: true, status: 200, json: async () => full() }; });
  await browser.click();
  assert.equal(browser.doc.lastEvent.detail.resumeIntent, true);
  browser.auth.value = signedIn;
  browser.listeners["portal-auth-change"]();
  browser.listeners["portal-auth-complete"]({ detail: { placement: "english_commentary", resumeIntent: true } });
  await new Promise(setImmediate);
  assert.equal(calls, 1);
  assert.equal(browser.elements.englishFullCommentary.hidden, false);
});

test("same-account token refresh does not abort a pending read or erase an authorized body", async () => {
  let release;
  const browser = browserFixture(signedIn, () => new Promise((resolve) => { release = resolve; }));
  const pending = browser.click();
  browser.auth.value = JSON.stringify({ token: "refreshed", user: { id: "account" } });
  browser.listeners["portal-auth-change"]();
  release({ ok: true, status: 200, json: async () => full() }); await pending;
  assert.equal(browser.elements.englishFullCommentary.hidden, false);
  browser.listeners["portal-auth-change"]();
  assert.equal(browser.elements.englishFullCommentary.hidden, false);
});

test("returning to a hidden tab restores the read through authorization and never across logout", async () => {
  let calls = 0;
  const browser = browserFixture(signedIn, async () => { calls++; return { ok: true, status: 200, json: async () => full() }; });
  await browser.click(); browser.doc.hidden = true; browser.listeners.visibilitychange();
  assert.equal(browser.elements.englishFullCommentary.hidden, true);
  browser.doc.hidden = false; browser.listeners.visibilitychange(); await new Promise(setImmediate);
  assert.equal(calls, 2); assert.equal(browser.elements.englishFullCommentary.hidden, false);
  browser.doc.hidden = true; browser.listeners.visibilitychange();
  browser.auth.value = null; browser.listeners["portal-auth-change"]();
  browser.doc.hidden = false; browser.listeners.visibilitychange(); await new Promise(setImmediate);
  assert.equal(calls, 2); assert.equal(browser.elements.englishFullCommentary.hidden, true);
});

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
  browser.auth.value = null; browser.listeners["portal-auth-change"]();
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


test("an expired session is cleared before login and the requested read resumes", async () => {
  let calls = 0;
  const browser = browserFixture(signedIn, async () => ++calls === 1
    ? { ok: false, status: 401, json: async () => ({ error: "unauthorized" }) }
    : { ok: true, status: 200, json: async () => full() });
  await browser.click();
  assert.equal(browser.auth.value, null);
  assert.equal(browser.doc.lastEvent.type, "portal-open-auth");
  browser.auth.value = signedIn; browser.listeners["portal-auth-change"]();
  await new Promise(setImmediate);
  assert.equal(calls, 2); assert.equal(browser.elements.englishFullCommentary.hidden, false);
});

test("a rejected old token retries the refreshed token without logging out", async () => {
  let release, calls = 0;
  const browser = browserFixture(signedIn, async (_url, options) => ++calls === 1
    ? new Promise(resolve => { release = resolve; })
    : { ok: true, status: 200, json: async () => full() });
  const pending = browser.click();
  browser.auth.value = JSON.stringify({ token: "new-token", user: { id: "account" } });
  browser.listeners["portal-auth-change"]();
  release({ ok: false, status: 401, json: async () => ({}) }); await pending; await new Promise(setImmediate);
  assert.equal(JSON.parse(browser.auth.value).token, "new-token");
  assert.equal(calls, 2); assert.equal(browser.elements.englishFullCommentary.hidden, false);
});
