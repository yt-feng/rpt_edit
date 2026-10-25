import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";

const source = await readFile(new URL("../site_src/assets/site-feedback.js", import.meta.url), "utf8");
function harness(initialSession = null, response = async () => new Response(JSON.stringify({ ok: true }), { status: 202 })) {
  const controls = new Map(), events = new Map(), sent = [], appended = [];
  let stored = initialSession, mounted = false;
  const document = { readyState: "complete", activeElement: null,
    body: { append(node) { appended.push(node); mounted = true; } },
    getElementById(id) { return mounted ? controls.get(`#${id}`) : null; },
    addEventListener(name, callback) { events.set(name, callback); },
  };
  class Element {
    constructor(name) { this.name = name; this.handlers = new Map(); this.dataset = {}; this.value = ""; this.disabled = false; this.readOnly = false; this.tabIndex = 0; this.attributes = new Map(); }
    addEventListener(name, callback) { this.handlers.set(name, callback); }
    async fire(name, detail = {}) { return this.handlers.get(name)?.({ target: this, preventDefault() {}, ...detail }); }
    focus() { document.activeElement = this; }
    setAttribute(key, value) { this.attributes.set(key, value); }
    removeAttribute(key) { this.attributes.delete(key); }
    showModal() { this.open = true; }
    close() { this.open = false; this.handlers.get("close")?.(); }
    getBoundingClientRect() { return { left: 10, right: 500, top: 10, bottom: 600 }; }
    querySelector(selector) { return controls.get(selector); }
    querySelectorAll() { return [controls.get(".site-feedback-close"), controls.get("#siteFeedbackEmail"), controls.get("#siteFeedbackCategory"), controls.get("#siteFeedbackMessage"), controls.get("#siteFeedbackWebsite"), controls.get(".site-feedback-submit")]; }
    reportValidity() { return this.valid !== false; }
    reset() { for (const id of ["#siteFeedbackEmail", "#siteFeedbackMessage", "#siteFeedbackWebsite"]) controls.get(id).value = ""; controls.get("#siteFeedbackCategory").value = "bug"; }
  }
  for (const selector of [".site-feedback-launch", "#siteFeedbackDialog", "form", "#siteFeedbackEmail", "#siteFeedbackCategory", "#siteFeedbackMessage", "#siteFeedbackWebsite", ".site-feedback-submit", ".site-feedback-status", ".site-feedback-close"]) controls.set(selector, new Element(selector));
  controls.get("#siteFeedbackCategory").value = "bug";
  controls.get("#siteFeedbackWebsite").tabIndex = -1;
  document.createElement = () => new Element("container");
  const window = { document, location: { pathname: "/reports/deep/path.html", href: "https://portal.example.invalid/reports/deep/path.html?private=secret" },
    localStorage: { getItem: () => stored ? JSON.stringify(stored) : null },
    addEventListener() {}, setTimeout, clearTimeout,
    async fetch(url, init) { sent.push({ url, init, body: JSON.parse(init.body) }); return response(url, init); },
  };
  vm.runInNewContext(source, { window, document, AbortController, console });
  return { document, window, controls, sent, appended,
    el: (selector) => controls.get(selector),
    setSession(value) { stored = value; events.get("portal-auth-change")?.(); },
    async open() { await controls.get(".site-feedback-launch").fire("click"); },
    async send() { return controls.get("form").fire("submit"); },
  };
}

test("feedback mounts once and guest submission stays same-origin with no query-string data", async () => {
  const h = harness(); h.window.PortalFeedback.mount();
  assert.equal(h.appended.length, 1);
  await h.open(); assert.equal(h.el("#siteFeedbackDialog").open, true);
  assert.equal(h.document.activeElement, h.el("#siteFeedbackEmail"));
  h.el("#siteFeedbackEmail").value = "guest@example.net";
  h.el("#siteFeedbackMessage").value = " Please improve search. ";
  h.el("#siteFeedbackCategory").value = "suggestion";
  await h.send();
  assert.equal(h.sent.length, 1); assert.equal(h.sent[0].url, "/api/feedback");
  assert.equal(h.sent[0].init.headers.Authorization, undefined);
  assert.equal(h.sent[0].body.page_path, "/reports/deep/path.html");
  assert.equal(h.sent[0].body.message, "Please improve search.");
  assert.equal(h.sent[0].body.category, "suggestion");
  assert.match(h.el(".site-feedback-status").textContent, /反馈已收到.*received/u);
  assert.equal(h.el("#siteFeedbackMessage").value, "");
  await h.el(".site-feedback-close").fire("click");
  assert.equal(h.document.activeElement, h.el(".site-feedback-launch"));
});

test("signed-in feedback uses the account email and resets on identity change", async () => {
  const h = harness({ token: "account-token", user: { id: "user-one", email: "member@example.net" } });
  await h.open();
  assert.equal(h.el("#siteFeedbackEmail").readOnly, true);
  h.el("#siteFeedbackEmail").value = "forged@example.net";
  h.el("#siteFeedbackMessage").value = "The report has a typo.";
  await h.send();
  assert.equal(h.sent[0].body.requester_email, "member@example.net");
  assert.equal(h.sent[0].init.headers.Authorization, "Bearer account-token");
  h.el("#siteFeedbackMessage").value = "Private unsent feedback";
  h.setSession(null);
  assert.equal(h.el("#siteFeedbackEmail").readOnly, false);
  assert.equal(h.el("#siteFeedbackEmail").value, ""); assert.equal(h.el("#siteFeedbackMessage").value, "");
});

test("feedback prevents duplicate submits, preserves message on delivery failure, and re-enables controls", async () => {
  let finish;
  const h = harness(null, () => new Promise((resolve) => { finish = resolve; }));
  await h.open();
  h.el("#siteFeedbackEmail").value = "guest@example.net";
  h.el("#siteFeedbackMessage").value = "The button is broken.";
  const first = h.send();
  await h.send();
  assert.equal(h.sent.length, 1); assert.equal(h.el("#siteFeedbackMessage").disabled, true);
  finish(new Response(JSON.stringify({ ok: false, detail: "Please retry later." }), { status: 503 }));
  await first;
  assert.equal(h.el("#siteFeedbackMessage").value, "The button is broken.");
  assert.equal(h.el(".site-feedback-status").dataset.state, "error");
  assert.equal(h.el(".site-feedback-submit").disabled, false);
});

test("feedback respects native validity and closes with Escape while retaining focus", async () => {
  const h = harness(); await h.open(); h.el("form").valid = false;
  await h.send(); assert.equal(h.sent.length, 0);
  await h.el("#siteFeedbackDialog").fire("keydown", { key: "Escape" });
  assert.equal(h.el("#siteFeedbackDialog").open, false);
  assert.equal(h.document.activeElement, h.el(".site-feedback-launch"));
});

test("legacy generated and redacted account emails stay editable and submit the entered reply email", async () => {
  for (const email of ["legacy@users.portal.example.invalid", "redacted@users.example.invalid"]) {
    const h = harness({ token: "legacy-token", user: { id: "legacy-user", email, email_is_generated: true } });
    await h.open();
    assert.equal(h.el("#siteFeedbackEmail").readOnly, false);
    assert.equal(h.el("#siteFeedbackEmail").value, "");
    h.el("#siteFeedbackEmail").value = "real-reply@example.net";
    h.el("#siteFeedbackMessage").value = "Please help with this report.";
    await h.send();
    assert.equal(h.sent[0].body.requester_email, "real-reply@example.net");
    assert.equal(h.sent[0].init.headers.Authorization, "Bearer legacy-token");
  }
});
