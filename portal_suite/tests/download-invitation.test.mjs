import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";
const source = await readFile(new URL("../site_src/assets/download-invitation.js", import.meta.url), "utf8");

function harness({ signedIn = false, storageThrows = false, observe = false } = {}) {
  let auth = signedIn ? { token: "fixture", user: { id: "member" } } : null;
  const events = new Map(), storage = new Map(), tracks = [], registerCalls = [];
  const document = {
    visibilityState: "visible",
    getElementById: (id) => ["detail", "reportDiscussionHost"].includes(id) ? {} : null,
    addEventListener(name, listener) { if (!events.has(name)) events.set(name, new Set()); events.get(name).add(listener); },
    removeEventListener(name, listener) { events.get(name)?.delete(listener); },
    dispatch(name, detail = {}) { for (const listener of [...events.get(name) || []]) listener({ detail }); },
  };
  class Element {
    children = []; handlers = new Map(); attributes = new Map(); _html = ""; nodes = new Map();
    set innerHTML(html) { this._html = html; this.nodes.clear(); }
    get innerHTML() { return this._html; }
    setAttribute(name, value) { this.attributes.set(name, value); }
    append(child) { child.parent = this; this.children.push(child); }
    remove() { if (this.parent) this.parent.children = this.parent.children.filter((child) => child !== this); }
    addEventListener(name, handler) { this.handlers.set(name, handler); }
    removeEventListener(name, handler) { if (this.handlers.get(name) === handler) this.handlers.delete(name); }
    querySelector(selector) {
      if (selector === "[data-invitation-register]" && !this._html.includes("data-invitation-register")) return null;
      if (!this.nodes.has(selector)) this.nodes.set(selector, { disabled: false, textContent: "" });
      return this.nodes.get(selector);
    }
    focus() { this.focused = true; }
    scrollIntoView() { this.scrolled = true; }
    async click(selector, dataset = {}) {
      const node = { dataset, closest: (target) => target === selector ? node : null };
      return this.handlers.get("click")?.({ target: node, preventDefault() {} });
    }
  }
  document.createElement = () => new Element();
  const window = { document, location: { origin: "https://portal.example.invalid", href: "https://portal.example.invalid/en/report.html?id=one&password=private-secret", pathname: "/en/report.html" },
    sessionStorage: { getItem(key) { if (storageThrows) throw new Error("blocked"); return storage.get(key); }, setItem(key, value) { if (storageThrows) throw new Error("blocked"); storage.set(key, value); } },
  };
  let observer;
  if (observe) window.IntersectionObserver = class {
    constructor(callback) { this.callback = callback; observer = this; }
    observe(target) { this.target = target; }
    disconnect() { this.disconnected = true; }
  };
  vm.runInNewContext(source, { window, document, URL, console });
  const container = new Element();
  const options = { container, item: { id: "one", title: "Current report" }, source: "catalog", getSession: () => auth,
    track: (event, data) => tracks.push({ event, data }), onRegister: async (context) => { registerCalls.push(context); }, related: [] };
  return { window, document, container, options, tracks, registerCalls, storage, events,
    createContainer: () => new Element(),
    show: (overrides = {}) => window.PortalDownloadInvitation.show({ ...options, ...overrides }),
    setAuth(value) { auth = value; document.dispatch("portal-auth-change"); },
    intersect(ratio) { observer.callback([{ target: observer.target, isIntersecting: ratio > 0, intersectionRatio: ratio }]); },
    observer: () => observer,
  };
}

test("invitation mounts only after explicit show with honest receipt and registration benefits", () => {
  const h = harness(); assert.equal(h.container.children.length, 0);
  h.show(); const card = h.container.children[0];
  assert.match(card.innerHTML, /PDF已接收并交给浏览器保存/u);
  assert.match(card.innerHTML, /免费注册，继续探索/u);
  assert.match(card.innerHTML, /AI 研究额度、每日签到与报告券/u);
  assert.match(card.innerHTML, /全文下载以账号权益为准/u);
  assert.doesNotMatch(card.innerHTML, /3天|三天|自动开通|无限下载|<dialog|role="dialog"/u);
  assert.deepEqual(h.tracks.map((entry) => entry.event), ["shown"]);
  assert.equal(h.show(), h.show()); assert.equal(h.container.children.length, 1); assert.equal(h.tracks.length, 1);
});

test("related reports are deduplicated, escaped, limited to three, and carry no secrets", async () => {
  const h = harness();
  h.show({ related: [
    { id: "bad", title: "Off site", href: "https://foreign.example/report.html?id=bad" },
    { id: "blank", title: "Missing URL" },
    { id: "two", title: "<script>unsafe</script>", href: "/report.html?id=two&password=secret&token=bearer&preview=private#key=123" },
    { id: "two", title: "Duplicate", href: "/report.html?id=two" },
    { id: "three", title: "Third report", href: "/report.html?id=three&source=catalog" },
    { id: "four", title: "Fourth report", href: "/report.html?id=four" },
    { id: "five", title: "Should not appear", href: "/report.html?id=five" },
  ] });
  const card = h.container.children[0];
  assert.match(card.innerHTML, /&lt;script&gt;unsafe&lt;\/script&gt;/u);
  assert.doesNotMatch(card.innerHTML, /foreign|Off site|Missing URL|Duplicate|Should not appear|password|secret|token|preview|key=|<script>/u);
  assert.equal((card.innerHTML.match(/data-invitation-related=/g) || []).length, 3);
  await card.click("[data-invitation-related]", { invitationRelated: "1" });
  assert.equal(h.tracks.at(-1).event, "related_open"); assert.equal(h.tracks.at(-1).data.report_id, "three");
  assert.equal(h.tracks.at(-1).data.parent_report_id, "one");
});

test("dismissal and repeated report downloads do not repeat the invitation in a session", async () => {
  const h = harness({ storageThrows: true }); h.show();
  await h.container.children[0].click("[data-invitation-dismiss]");
  assert.equal(h.container.children.length, 0);
  assert.equal(h.show(), null); assert.equal(h.show({ container: h.createContainer() }), null);
  assert.deepEqual(h.tracks.map((entry) => entry.event), ["shown", "viewed", "dismiss"]);
  assert.equal(h.events.get("portal-auth-change").size, 0); assert.equal(h.events.get("portal-auth-complete").size, 0);
  assert.ok(h.show({ item: { id: "another-report" } }));
});

test("signed-in reader sees continuation actions without a registration prompt", () => {
  const h = harness({ signedIn: true }); h.show(); const html = h.container.children[0].innerHTML;
  assert.doesNotMatch(html, /data-invitation-register|免费注册/u);
  assert.match(html, /继续阅读/u); assert.match(html, /参与讨论/u); assert.match(html, /继续 AI 研究/u);
  assert.match(html, /href="\/en\/research.html"/u);
});

test("signup resumes the current report and tracks only a confirmed new registration", async () => {
  const h = harness();
  h.show({ onRegister: async (context) => {
    h.registerCalls.push(context);
    h.setAuth({ token: "member", user: { id: "new-member" } });
    h.document.dispatch("portal-auth-complete", { action: "register", placement: "post_download" });
    h.document.dispatch("portal-auth-complete", { action: "register", placement: "post_download" });
  } });
  const card = h.container.children[0];
  await card.click("[data-invitation-register]");
  assert.equal(h.registerCalls[0].mode, "register"); assert.equal(h.registerCalls[0].resumeIntent, true);
  assert.equal(h.registerCalls[0].item.id, "one");
  assert.deepEqual(h.tracks.map((entry) => entry.event), ["shown", "viewed", "signup_click", "registered"]);
  assert.equal(h.tracks[1].data.access_state, "guest");
  assert.equal(h.tracks.at(-1).data.access_state, "signed_in");
  assert.doesNotMatch(card.innerHTML, /data-invitation-register/u); assert.equal(card.focused, true); assert.equal(card.scrolled, true);
});

test("login recovery and merely closing the registration modal do not count as registrations", async () => {
  const h = harness(); h.show(); const card = h.container.children[0];
  await card.click("[data-invitation-register]");
  assert.deepEqual(h.tracks.map((entry) => entry.event), ["shown", "viewed", "signup_click"]);
  h.setAuth({ token: "existing", user: { id: "old-member" } });
  h.document.dispatch("portal-auth-complete", { action: "login_recovered", placement: "post_download" });
  h.document.dispatch("portal-auth-complete", { action: "register", placement: "navigation" });
  assert.equal(h.tracks.filter((entry) => entry.event === "registered").length, 0);
});

test("rerendering a different report cleans old handlers and maintains one active card", () => {
  const h = harness(); h.show(); const old = h.container.children[0];
  const current = h.show({ item: { id: "new-report" } });
  assert.equal(h.container.children.length, 1); assert.equal(old.handlers.size, 0);
  assert.equal(h.events.get("portal-auth-change").size, 1); assert.equal(h.events.get("portal-auth-complete").size, 1);
  current.destroy(); assert.equal(h.container.children.length, 0);
  assert.equal(h.events.get("portal-auth-change").size, 0);
});

test("viewed requires actual viewport exposure in a visible tab and is emitted once", () => {
  const h = harness({ observe: true }); h.show();
  h.intersect(0); h.intersect(0.2);
  assert.deepEqual(h.tracks.map((row) => row.event), ["shown"]);
  h.document.visibilityState = "hidden"; h.intersect(0.8);
  assert.equal(h.tracks.length, 1);
  h.document.visibilityState = "visible"; h.document.dispatch("visibilitychange");
  h.intersect(1); h.document.dispatch("visibilitychange");
  assert.deepEqual(h.tracks.map((row) => row.event), ["shown", "viewed"]);
  assert.equal(h.observer().disconnected, true);
  h.show().destroy(); assert.equal(h.events.get("visibilitychange").size, 0);
});

test("signed-in continuation actions are measured separately from guest signup", async () => {
  const h = harness({ signedIn: true }); h.show(); const card = h.container.children[0];
  await card.click("[data-invitation-continue]", { invitationContinue: "discussion" });
  assert.deepEqual(h.tracks.map((row) => row.event), ["shown", "viewed", "discussion"]);
  assert.ok(h.tracks.every((row) => row.data.access_state === "signed_in"));
  assert.equal(h.registerCalls.length, 0);
});
