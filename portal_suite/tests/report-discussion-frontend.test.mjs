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

function setup(handler = null) {
  const events = new Map(), requests = [], analytics = [], container = new Element("div");
  let signedIn = false, payload = { starter: { kind: "ai", body: "哪些证据会改变这一判断？", text_scope: "partial_excerpt" }, comments: [{ id: "one", display_name: "读者", body: "<script>sample</script>", created_at: "2026-10-25T01:00:00Z" }] };
  const window = { PortalSuiteAnalytics: { track(type, data) { analytics.push({ type, ...JSON.parse(JSON.stringify(data)) }); } } };
  const document = {
    createElement: (tag) => new Element(tag),
    addEventListener: (event, callback) => { const set = events.get(event) || new Set(); set.add(callback); events.set(event, set); },
    removeEventListener: (event, callback) => events.get(event)?.delete(callback),
  };
  let loginCalls = 0;
  const context = vm.createContext({ window, document, URLSearchParams, crypto: { randomUUID: () => "request-stable-id" }, fetch: async (url, options = {}) => {
    requests.push({ url, options });
    if (handler) return handler(url, options, payload);
    return Response.json(options.method === "POST" ? { ok: true } : payload);
  } });
  vm.runInContext(source, context);
  const options = { item: { id: "report-one" }, source: "catalog", workerUrl: "/api", getSession: () => signedIn ? { user: {} } : null, authHeaders: () => signedIn ? { Authorization: "Bearer test" } : {}, onLogin: () => { loginCalls += 1; } };
  return { container, options, requests, events, analytics, mount: () => window.PortalDiscussion.mount(container, options), setSignedIn: (value) => { signedIn = value; }, setPayload: (value) => { payload = value; }, loginCalls: () => loginCalls };
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
  assert.deepEqual(state.analytics.map(({ action }) => action), ["load_result", "login_click"]);
  assert.equal(state.analytics[0].status, "success"); assert.equal(state.analytics[0].count, 1); assert.equal(state.analytics[0].result_count, 1);
  assert.doesNotMatch(JSON.stringify(state.analytics), /哪些证据|读者|<script>|partial_excerpt|"body"|"query"/);
});

test("successful login reveals comment form and posts actual input with a stable submission identifier", async () => {
  const state = setup(); state.mount(); await settle(); state.setSignedIn(true);
  for (const callback of state.events.get("portal-auth-change")) callback();
  await settle();
  const nodes = descendants(state.container), form = nodes.find((node) => node.tagName === "form"), textarea = nodes.find((node) => node.tagName === "textarea");
  assert.equal(form.hidden, false);
  textarea.value = "我会先观察订单的变化。";
  textarea.listeners.input(); textarea.listeners.input();
  assert.equal(state.analytics.filter(({ action }) => action === "form_start").length, 1);
  await form.listeners.submit({ preventDefault() {} });
  const post = state.requests.find((request) => request.options.method === "POST");
  assert.equal(post.options.headers.Authorization, "Bearer test");
  assert.deepEqual(JSON.parse(post.options.body), { source: "catalog", report_id: "report-one", body: "我会先观察订单的变化。", request_id: "request-stable-id" });
  assert.equal(textarea.value, "");
  assert.deepEqual(state.analytics.slice(-3).map(({ action, status }) => [action, status]), [
    ["comment_submit", "pending"], ["comment_result", "success"], ["load_result", "success"],
  ]);
  textarea.value = "第二条评论"; textarea.listeners.input();
  assert.equal(state.analytics.filter(({ action }) => action === "form_start").length, 2);
  assert.ok(state.analytics.every((event) => event.type === "journey_interaction" && event.placement === "report_discussion" && event.measurement_version === "journey-v1" && event.source === "catalog" && event.report_id === "report-one"));
  assert.doesNotMatch(JSON.stringify(state.analytics), /我会先观察|第二条评论|request-stable-id|Bearer test|读者|<script>|"body"|"query"/);
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

test("discussion loading and posting failures emit controlled errors without leaking input or server detail", async () => {
  const state = setup((_url, _options) => Response.json({ detail: "Private backend message for member@example.net" }, { status: 503 }));
  state.setSignedIn(true); state.mount(); await settle();
  const nodes = descendants(state.container), form = nodes.find((node) => node.tagName === "form"), textarea = nodes.find((node) => node.tagName === "textarea");
  assert.equal(state.analytics[0].action, "load_result"); assert.equal(state.analytics[0].status, "error"); assert.equal(state.analytics[0].error, "unavailable");
  textarea.value = "Private commentary contents"; textarea.listeners.input();
  await form.listeners.submit({ preventDefault() {} });
  assert.equal(state.analytics.at(-1).action, "comment_result"); assert.equal(state.analytics.at(-1).status, "error"); assert.equal(state.analytics.at(-1).error, "unavailable");
  assert.equal(textarea.value, "Private commentary contents");
  assert.equal(state.analytics.some(({ status }) => status === "success"), false);
  assert.doesNotMatch(JSON.stringify(state.analytics), /Private|member@example|request-stable-id|Bearer test|"body"|"query"/);
});

test("discussion deletion measures success and failure without recording comment identifiers", async () => {
  let fail = false;
  const state = setup((_url, options, payload) => options.method === "DELETE"
    ? Response.json(fail ? { detail: "Private deletion detail" } : { ok: true }, { status: fail ? 503 : 200 })
    : Response.json(payload));
  state.setPayload({ comments: [{ id: "private-comment-identity", display_name: "Private display name", body: "Private stored comment", can_delete: true }] });
  state.setSignedIn(true); state.mount(); await settle();
  const remove = () => descendants(state.container).find((node) => node.className === "report-discussion-delete");
  await remove().listeners.click(); fail = true; await remove().listeners.click();
  assert.deepEqual(state.analytics.filter(({ action }) => action === "delete_result").map(({ status }) => status), ["success", "error"]);
  assert.doesNotMatch(JSON.stringify(state.analytics), /private-comment-identity|Private|"comment_id"|"body"/);
});
