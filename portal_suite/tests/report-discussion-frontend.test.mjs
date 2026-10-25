import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/report-discussion.js", import.meta.url), "utf8");
class Element {
  constructor(tag) { this.tagName = tag; this.children = []; this.listeners = {}; this.value = ""; this.attributes = {}; this._text = ""; }
  set textContent(value) { this._text = String(value); this.children = []; }
  get textContent() { return this._text + this.children.map((child) => child.textContent).join(""); }
  append(...children) { for (const child of children) { this.children.push(child); child.parentNode = this; } }
  replaceChildren(...children) { this.children = []; this._text = ""; this.append(...children); }
  setAttribute(key, value) { this.attributes[key] = value; }
  addEventListener(key, callback) { this.listeners[key] = callback; }
  remove() { if (this.parentNode) this.parentNode.children = this.parentNode.children.filter((child) => child !== this); }
}
const descendants = (node) => [node, ...node.children.flatMap(descendants)];
const settle = async () => { for (let i = 0; i < 5; i += 1) await new Promise((resolve) => setImmediate(resolve)); };

function setup() {
  const events = new Map(), requests = [], container = new Element("div");
  let signedIn = false, payload = { starter: { kind: "ai", body: "哪些证据会改变这一判断？", text_scope: "partial_excerpt" }, comments: [{ id: "one", display_name: "读者", body: "<script>sample</script>", created_at: "2026-10-25T01:00:00Z" }] };
  const window = {};
  const document = {
    createElement: (tag) => new Element(tag),
    addEventListener: (event, callback) => { const set = events.get(event) || new Set(); set.add(callback); events.set(event, set); },
    removeEventListener: (event, callback) => events.get(event)?.delete(callback),
  };
  let loginCalls = 0;
  const context = vm.createContext({ window, document, URLSearchParams, crypto: { randomUUID: () => "request-stable-id" }, fetch: async (url, options = {}) => {
    requests.push({ url, options });
    return Response.json(options.method === "POST" ? { ok: true } : payload);
  } });
  vm.runInContext(source, context);
  const options = { item: { id: "report-one" }, source: "catalog", workerUrl: "/api", getSession: () => signedIn ? { user: {} } : null, authHeaders: () => signedIn ? { Authorization: "Bearer test" } : {}, onLogin: () => { loginCalls += 1; } };
  return { container, options, requests, events, mount: () => window.PortalDiscussion.mount(container, options), setSignedIn: (value) => { signedIn = value; }, setPayload: (value) => { payload = value; }, loginCalls: () => loginCalls };
}

test("discussion labels AI, counts only genuine comments and renders comments as text", async () => {
  const state = setup(); state.mount(); await settle();
  const nodes = descendants(state.container);
  assert.ok(nodes.find((node) => node.className === "report-discussion-ai-badge" && node.textContent === "AI 导读"));
  assert.ok(nodes.find((node) => node.className === "report-discussion-count" && node.textContent === "1 条评论"));
  assert.ok(nodes.find((node) => node.className === "report-discussion-body" && node.textContent === "<script>sample</script>"));
  assert.equal(nodes.some((node) => node.tagName === "script"), false);
  assert.equal(nodes.find((node) => node.tagName === "form").hidden, true);
  const login = nodes.find((node) => node.tagName === "button" && node.textContent === "登录后参与讨论");
  login.listeners.click(); assert.equal(state.loginCalls(), 1);
  assert.equal(state.requests.length, 1);
  assert.match(state.requests[0].url, /^\/api\/report-discussion\?source=catalog&report_id=report-one$/u);
});

test("successful login reveals comment form and posts actual input with a stable submission identifier", async () => {
  const state = setup(); state.mount(); await settle(); state.setSignedIn(true);
  for (const callback of state.events.get("portal-auth-change")) callback();
  await settle();
  const nodes = descendants(state.container), form = nodes.find((node) => node.tagName === "form"), textarea = nodes.find((node) => node.tagName === "textarea");
  assert.equal(form.hidden, false);
  textarea.value = "我会先观察订单的变化。";
  await form.listeners.submit({ preventDefault() {} });
  const post = state.requests.find((request) => request.options.method === "POST");
  assert.equal(post.options.headers.Authorization, "Bearer test");
  assert.deepEqual(JSON.parse(post.options.body), { source: "catalog", report_id: "report-one", body: "我会先观察订单的变化。", request_id: "request-stable-id" });
  assert.equal(textarea.value, "");
});

test("historical reports retain empty comment space and remount removes stale listeners", async () => {
  const state = setup(); state.setPayload({ starter: null, comments: [] });
  const cleanup = state.mount(); await settle();
  assert.match(state.container.textContent, /还没有读者评论/u);
  assert.equal(descendants(state.container).some((node) => node.className === "report-discussion-ai"), false);
  state.mount(); await settle();
  assert.equal(state.container.children.length, 1);
  assert.equal(state.events.get("portal-auth-change").size, 1);
  cleanup();
  // The superseded cleanup must not clear the newly mounted discussion.
  assert.equal(state.container.children.length, 1);
  state.mount(); await settle();
  assert.equal(state.container.children.length, 1);
  assert.equal(state.events.get("portal-auth-change").size, 1);
});
