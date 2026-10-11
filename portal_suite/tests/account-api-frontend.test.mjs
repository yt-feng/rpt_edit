import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const servicesSource = await readFile(new URL("../site_src/assets/account-services.js", import.meta.url), "utf8");
const docs = await readFile(new URL("../site_src/developer-api.html", import.meta.url), "utf8");
function extract(name) {
  const marker = new RegExp(`\\n  (?:async )?function ${name}\\(`, "u");
  const source = marker.test(servicesSource) ? servicesSource : app;
  const start = source.search(marker);
  assert.ok(start >= 0, name);
  const next = source.slice(start + 1).search(/\n  (?:async )?function /u);
  const end = next >= 0 ? start + 1 + next : source.indexOf("\n    return { initAccountApiControls", start);
  assert.ok(end > start, `${name} ends before module exports`);
  return source.slice(start, end);
}
const flush = () => new Promise(setImmediate);
const expiry = new Date(Date.now() + 30 * 86400000).toISOString();
const grant = { enabled: true, access_mode: "membership", report_ids: [], expires_at: expiry,
  scopes: ["reports:read", "reports:download", "artifacts:read"], requests_per_minute: 30, daily_requests: 1000, daily_bytes: 1073741824 };
const key = { id: "key-id", name: "研究工具", scopes: grant.scopes, created_at: new Date().toISOString(), expires_at: expiry };
class Node {
  constructor() { this.handlers = new Map(); this.value = ""; this.textContent = ""; this.innerHTML = ""; this.hidden = false; this.disabled = false; this.open = false; this.dataset = {}; this.isConnected = true; this.children = []; }
  addEventListener(type, callback) { this.handlers.set(type, [...(this.handlers.get(type) || []), callback]); }
  removeEventListener(type, callback) { this.handlers.set(type, (this.handlers.get(type) || []).filter((fn) => fn !== callback)); }
  emit(type, target = this) { for (const fn of this.handlers.get(type) || []) fn({ target, preventDefault() {} }); }
  querySelectorAll() { return this.children; }
  scrollIntoView() {}
}
function setup(admin = false, reminder = false, credit = false) {
  const nodes = new Map();
  const ids = admin
    ? ["accountAdminResearchAccess", "accountAdminAiCreditForm", "accountAdminAiCreditCount", "accountAdminAiCreditReason", "accountAdminAiCreditBalance", "accountAdminAiCreditStatus", "accountAdminApiGrantForm", "accountAdminApiGrantStatus", "accountAdminApiGrantState", "accountAdminApiMode", "accountAdminApiExpiry", "accountAdminApiReportIds", "accountAdminApiGrantRevoke", "accountAdminResearchRefresh", "accountAdminResearchClose", "accountAdminApiReportIdsField", "accountAdminResearchUser", "accountAdminApiReportIdsHint"]
    : ["accountApiPanel", "accountApiGrant", "accountApiKeys", "accountApiCreate", "accountApiKeyName", "accountApiCreateButton", "accountApiRefresh", "accountApiStatus", "accountApiSecretPanel", "accountApiSecret", "accountApiCopy", "accountApiDismiss"];
  ids.push(...(admin ? ["accountAdminReminderSummary", "accountAdminReminderSubject", "accountAdminReminderText", "accountAdminReminderStatus"] : ["accountReminderPanel", "accountReminderEnabled", "accountReminderRefresh", "accountReminderStatus", "accountReminderSummary", "accountReminderSubject", "accountReminderText"]));
  ids.push("accountAiCreditsSummary", "accountAiCreditsRefresh", "accountAiCreditsStatus");
  ids.forEach((id) => nodes.set(id, new Node()));
  const node = (id) => nodes.get(id);
  if (admin) {
    node("accountAdminApiGrantForm").children = grant.scopes.map((value) => Object.assign(new Node(), { value, checked: true }));
    node("accountAdminAiCreditForm").children = [node("accountAdminAiCreditCount"), node("accountAdminAiCreditReason")];
  }
  let session = { token: "session-a", user: { role: admin ? "super" : "user" } };
  const modal = new Node(); modal.querySelector = (selector) => nodes.get(selector.slice(1));
  const document = new Node();
  const requests = [];
  let uuid = 0;
  const context = vm.createContext({
    Date, JSON, AbortController, TypeError, setTimeout, clearTimeout, encodeURIComponent,
    window: { crypto: { randomUUID: () => `test-operation-${++uuid}` } },
    navigator: { clipboard: { async writeText() {} } },
    document,
    escapeHtml: (value) => String(value ?? "").replaceAll("&", "&amp;").replaceAll("<", "&lt;").replaceAll('"', "&quot;"),
    loadAuthSession: () => session,
    isAdminASession: () => session?.user.role === "super",
    authHeaders: () => session ? { Authorization: `Bearer ${session.token}` } : {},
    fetch(url, options) { return new Promise((resolve) => requests.push({ url, options, resolve })); },
  });
  vm.runInContext(["accountToolError", "accountToolRequest", "apiAccessDate", "accountApiKeysMarkup", "initAccountApiControls", "apiGrantLocalDate", "initAdminResearchAccessControls", "renderExpiryReminderDetails", "initAccountReminderControls", "initAccountCreditControls"].map(extract).join("\n"), context);
  const controller = admin ? context.initAdminResearchAccessControls("/api", modal) : credit ? context.initAccountCreditControls("/api", modal) : reminder ? context.initAccountReminderControls("/api", modal) : context.initAccountApiControls("/api", modal);
  const respond = (index, body, status = 200) => requests[index].resolve(new Response(JSON.stringify(body), { status }));
  return { context, node, modal, document, controller, requests, respond,
    login(value) { session = value; document.emit("portal-auth-change"); },
    async open() {
      if (admin) modal.emit("click", { closest: () => ({ dataset: { email: "chosen@example.invalid" } }) });
      else { const panel = node(reminder ? "accountReminderPanel" : "accountApiPanel"); panel.open = true; panel.emit("toggle"); }
      await flush();
    },
  };
}
async function openAccount(ctx, state = grant) {
  await ctx.open(); ctx.respond(0, { ok: true, grant: state, keys: [] }); await flush();
}

test("key requests use the existing API base, session header, no cache; create blocks duplicate submissions", async () => {
  const ctx = setup(); await openAccount(ctx);
  assert.equal(ctx.requests[0].url, "/api/account/content-api");
  assert.equal(ctx.requests[0].options.cache, "no-store");
  assert.equal(ctx.requests[0].options.headers.Authorization, "Bearer session-a");
  ctx.node("accountApiKeyName").value = "研究工具";
  ctx.node("accountApiCreate").emit("submit"); ctx.node("accountApiCreate").emit("submit");
  assert.equal(ctx.requests.length, 2); assert.equal(ctx.node("accountApiCreateButton").disabled, true);
  ctx.respond(1, { ok: true, key, secret: "synthetic-one-time-secret" }); await flush();
  assert.equal(ctx.node("accountApiSecret").textContent, "synthetic-one-time-secret");
  assert.equal(ctx.node("accountApiSecretPanel").hidden, false);
  ctx.node("accountApiPanel").open = false; ctx.node("accountApiPanel").emit("toggle");
  assert.equal(ctx.node("accountApiSecret").textContent, "");
  ctx.controller.close();
});

test("late key creation cannot display a secret after the panel closes", async () => {
  const ctx = setup(); await openAccount(ctx);
  ctx.node("accountApiKeyName").value = "tool"; ctx.node("accountApiCreate").emit("submit");
  ctx.node("accountApiPanel").open = false; ctx.node("accountApiPanel").emit("toggle");
  ctx.respond(1, { ok: true, key, secret: "must-not-display" }); await flush();
  assert.equal(ctx.node("accountApiSecret").textContent, ""); assert.equal(ctx.node("accountApiSecretPanel").hidden, true);
  assert.match(ctx.node("accountApiStatus").textContent, /撤销后重新生成/u);
  ctx.controller.close();
});

test("logout clears a visible secret immediately and ignores in-flight response", async () => {
  const ctx = setup(); await openAccount(ctx);
  ctx.node("accountApiKeyName").value = "tool"; ctx.node("accountApiCreate").emit("submit");
  ctx.login(null);
  ctx.respond(1, { ok: true, key, secret: "must-not-display" }); await flush();
  assert.equal(ctx.node("accountApiSecret").textContent, ""); assert.equal(ctx.node("accountApiCreateButton").disabled, true);
  assert.doesNotMatch(ctx.node("accountApiKeys").innerHTML, /key-id/u);
  ctx.controller.close();
});

test("revoking the newly created key clears its visible secret and marks the key revoked", async () => {
  const ctx = setup(); await openAccount(ctx);
  ctx.node("accountApiKeyName").value = "tool"; ctx.node("accountApiCreate").emit("submit");
  ctx.respond(1, { ok: true, key, secret: "secret-to-clear" }); await flush();
  ctx.node("accountApiKeys").emit("click", { closest: () => ({ dataset: { apiRevoke: key.id } }) });
  assert.equal(ctx.node("accountApiSecret").textContent, "");
  assert.equal(ctx.requests[2].url, "/api/account/content-api/keys/key-id"); assert.equal(ctx.requests[2].options.method, "DELETE");
  ctx.respond(2, { ok: true }); await flush();
  assert.match(ctx.node("accountApiKeys").innerHTML, /已撤销/u);
  ctx.controller.close();
});

test("a denied or failed permission fetch leaves key generation unavailable and offers refresh", async () => {
  const ctx = setup(); await ctx.open();
  ctx.respond(0, { ok: false, error: "api_permission_denied", detail: "untrusted response" }, 403); await flush();
  assert.equal(ctx.node("accountApiCreateButton").disabled, true);
  assert.equal(ctx.node("accountApiRefresh").disabled, false);
  assert.match(ctx.node("accountApiStatus").textContent, /联系管理员/u);
  assert.doesNotMatch(ctx.node("accountApiStatus").textContent, /untrusted/u);
  ctx.controller.close();
});

test("key names, ids and scope labels are escaped before HTML rendering", () => {
  const ctx = setup();
  const html = ctx.context.accountApiKeysMarkup([{ ...key, id: '\"><img src=x>', name: '<script>bad</script>', scopes: ['<bad>'] }]);
  assert.doesNotMatch(html, /<script>|<img|<bad>/u);
  assert.match(html, /&lt;script>/u); assert.match(html, /&quot;/u);
  ctx.controller.close();
});

async function openAdmin(ctx) {
  await ctx.open();
  ctx.respond(0, { ok: true, credits: { balance: 4, total_granted: 8, total_consumed: 4 } });
  ctx.respond(1, { ok: true, grant });
  ctx.respond(2, { ok: true, preferences: { enabled: true }, reminder: { eligible: false }, preview: null }); await flush();
}

test("admin additive credit retry retains its operation id and blocks concurrent user changes", async () => {
  const ctx = setup(true); await openAdmin(ctx);
  ctx.node("accountAdminAiCreditCount").value = "10"; ctx.node("accountAdminAiCreditReason").value = "research allocation";
  ctx.node("accountAdminAiCreditForm").emit("submit");
  ctx.modal.emit("click", { closest: () => ({ dataset: { email: "other@example.invalid" } }) });
  assert.equal(ctx.requests.length, 4);
  const first = JSON.parse(ctx.requests[3].options.body);
  assert.equal(first.email, "chosen@example.invalid"); assert.equal(first.amount, 10);
  ctx.respond(3, { ok: false, code: "CREDIT_BUSY" }, 409); await flush();
  ctx.node("accountAdminAiCreditForm").emit("submit");
  const retry = JSON.parse(ctx.requests[4].options.body);
  assert.equal(retry.operation_id, first.operation_id);
  ctx.respond(4, { ok: true, credits: { balance: 14, total_granted: 18, total_consumed: 4 }, deduplicated: true }); await flush();
  assert.match(ctx.node("accountAdminAiCreditStatus").textContent, /没有重复添加/u);
  assert.match(ctx.node("accountAdminAiCreditBalance").textContent, /14 次/u);
  ctx.controller.close();
});

test("admin grants preserve configured limits and revocation disables the whole grant", async () => {
  const ctx = setup(true); await openAdmin(ctx);
  ctx.node("accountAdminApiMode").value = "granted_corpus";
  ctx.node("accountAdminApiReportIds").value = "report-one, report-two\nreport-one";
  ctx.node("accountAdminApiGrantForm").emit("submit");
  const payload = JSON.parse(ctx.requests[3].options.body);
  assert.deepEqual(payload.report_ids, ["report-one", "report-two"]);
  assert.equal(payload.access_mode, "granted_corpus"); assert.equal(payload.daily_bytes, grant.daily_bytes);
  assert.equal(ctx.requests[3].url, "/api/admin/content-api/grant");
  ctx.respond(3, { ok: true, grant: payload }); await flush();
  ctx.node("accountAdminApiGrantRevoke").emit("click");
  assert.equal(JSON.parse(ctx.requests[4].options.body).enabled, false);
  ctx.respond(4, { ok: true, grant: { ...payload, enabled: false } }); await flush();
  assert.equal(ctx.node("accountAdminApiGrantRevoke").disabled, true);
  assert.match(ctx.node("accountAdminApiGrantStatus").textContent, /旧密钥已撤销/u);
  ctx.controller.close();
});

test("admin controls hide on auth change and ignore stale selected-user data", async () => {
  const ctx = setup(true); await ctx.open(); ctx.login({ token: "new-user", user: { role: "user" } });
  ctx.respond(0, { ok: true, credits: { balance: 999 } }); ctx.respond(1, { ok: true, grant }); ctx.respond(2, { ok: true, preferences: { enabled: true }, reminder: {} }); await flush();
  assert.equal(ctx.node("accountAdminResearchAccess").hidden, true);
  assert.equal(ctx.node("accountAdminAiCreditBalance").textContent, "");
  ctx.controller.close();
});

test("API docs have an isolated boot path and content endpoints; secret handlers never persist or track keys", () => {
  assert.match(app, /page === "blog-article" \|\| page === "developer-api"\s*\? initContentAccount/u);
  assert.match(docs, /data-page="developer-api"/u);
  for (const path of ["/reports", "/reports/{id}/download", "/reports/{id}/artifacts/{artifactId}"]) assert.ok(docs.includes(path));
  assert.ok(docs.includes("https://kcdesk.com/api/content/v1"));
  const source = extract("initAccountApiControls");
  assert.doesNotMatch(source, /localStorage|sessionStorage|trackEvent|console\./u);
  assert.match(source, /secretNode\.textContent = data\.secret/u);
  assert.match(source, /document\.removeEventListener/u);
});

test("user reminder opt-out posts only own preference, blocks duplicates, and rolls back the checkbox after an error", async () => {
  const ctx = setup(false, true); await ctx.open();
  assert.equal(ctx.requests[0].url, "/api/account/expiry-reminders");
  ctx.respond(0, { ok: true, preferences: { enabled: true }, reminder: { eligible: true, kind: "membership", expires_at: expiry, next_send_at: expiry }, preview: { subject: "test reminder", text: "synthetic preview" } }); await flush();
  assert.equal(ctx.node("accountReminderEnabled").checked, true);
  ctx.node("accountReminderEnabled").checked = false; ctx.node("accountReminderEnabled").emit("change"); ctx.node("accountReminderEnabled").emit("change");
  assert.equal(ctx.requests.length, 2); assert.deepEqual(JSON.parse(ctx.requests[1].options.body), { enabled: false });
  assert.equal(ctx.node("accountReminderEnabled").disabled, true);
  ctx.respond(1, { ok: false, code: "REMINDER_STORAGE" }, 503); await flush();
  assert.equal(ctx.node("accountReminderEnabled").checked, true);
  assert.match(ctx.node("accountReminderStatus").textContent, /稍后刷新/u);
  ctx.node("accountReminderEnabled").checked = false; ctx.node("accountReminderEnabled").emit("change");
  ctx.respond(2, { ok: true, preferences: { enabled: false }, reminder: {}, preview: null }); await flush();
  assert.equal(ctx.node("accountReminderEnabled").checked, false);
  assert.match(ctx.node("accountReminderStatus").textContent, /已关闭/u);
  ctx.controller.close();
});

test("reminder previews render as plain text and stale account responses are discarded", async () => {
  const ctx = setup(false, true); await ctx.open();
  ctx.respond(0, { ok: true, preferences: { enabled: true }, reminder: {}, preview: { subject: "<script>subject</script>", text: "<img src=private>" } }); await flush();
  assert.equal(ctx.node("accountReminderSubject").textContent, "<script>subject</script>");
  assert.equal(ctx.node("accountReminderText").innerHTML, "");
  ctx.node("accountReminderRefresh").emit("click"); ctx.login(null);
  ctx.respond(1, { ok: true, preferences: { enabled: true }, reminder: {}, preview: { text: "old account" } }); await flush();
  assert.equal(ctx.node("accountReminderText").textContent, "");
  assert.equal(ctx.node("accountReminderEnabled").disabled, true);
  ctx.controller.close();
});

test("admin reminder preview is read-only and never posts or sends mail", async () => {
  const ctx = setup(true); await openAdmin(ctx);
  assert.equal(ctx.requests[2].url, "/api/account-admin/expiry-reminders?email=chosen%40example.invalid");
  assert.equal(ctx.requests[2].options.method, undefined);
  assert.match(ctx.node("accountAdminReminderStatus").textContent, /未发送邮件/u);
  const source = extract("initAdminResearchAccessControls");
  assert.doesNotMatch(source, /mutate\([^;]*expiry-reminders/u);
  ctx.controller.close();
});

test("own research balance shows original and added allowances separately and refreshes without an AI call", async () => {
  const ctx = setup(false, false, true);
  assert.equal(ctx.requests[0].url, "/api/account/ai-research-credits");
  ctx.respond(0, { ok: true, credits: { balance: 17 }, usage: { tier: "standard", period: "daily", limit: 2, remaining: 0 } }); await flush();
  assert.match(ctx.node("accountAiCreditsSummary").textContent, /今日额度剩余 0 次。 额外可用 17 次/u);
  ctx.node("accountAiCreditsRefresh").emit("click"); ctx.login(null);
  ctx.respond(1, { ok: true, credits: { balance: 999 }, usage: { remaining: 0 } }); await flush();
  assert.equal(ctx.node("accountAiCreditsSummary").textContent, "");
  assert.ok(ctx.requests.every((request) => !request.url.includes("report-chat")));
  ctx.controller.close();
});

test("account service module loads without side effects and app only requests it from account tools", () => {
  const context = vm.createContext({ window: {} });
  vm.runInContext(servicesSource, context);
  const exported = context.window.PortalAccountServices({});
  assert.equal(typeof exported.initAccountApiControls, "function");
  assert.equal(typeof exported.initAccountCreditControls, "function");
  assert.equal(typeof exported.initAccountReminderControls, "function");
  assert.equal(typeof exported.initAdminResearchAccessControls, "function");
  assert.doesNotMatch(app, /function initAccountApiControls\(/u);
  assert.match(extract("initLazyAccountServices"), /refresh\(show\) \{ visible = show; if \(!admin && show\) activate\(\); \}/u);
  assert.match(extract("loadAccountServices"), /account-services\.js/u);
});

test("lazy account adapter requests no script for a guest and ignores completion after modal teardown", async () => {
  const scripts = [], initialized = [];
  const modal = new Node(); modal.querySelector = () => new Node();
  const context = vm.createContext({
    window: { setTimeout, clearTimeout },
    document: { createElement: () => ({ remove() {} }), head: { append(script) { scripts.push(script); } } },
    loadAuthSession() {}, authHeaders() {}, escapeHtml() {}, isAdminASession: () => false,
  });
  vm.runInContext(`let accountServicesLoad = null;\n${extract("loadAccountServices")}\n${extract("initLazyAccountServices")}`, context);
  const controls = context.initLazyAccountServices("/api", modal);
  controls.refresh(false); assert.equal(scripts.length, 0);
  controls.refresh(true); assert.equal(scripts.length, 1);
  controls.close();
  context.window.PortalAccountServices = () => { initialized.push(true); return {}; };
  scripts[0].onload(); await flush();
  assert.equal(initialized.length, 0);
});

test("lazy admin adapter honors the most recent selected user while its script loads", async () => {
  const scripts = [], selected = [];
  const modal = new Node(); modal.querySelector = () => new Node();
  const context = vm.createContext({
    window: { setTimeout, clearTimeout },
    document: { createElement: () => ({ remove() {} }), head: { append(script) { scripts.push(script); } } },
    loadAuthSession() {}, authHeaders() {}, escapeHtml() {}, isAdminASession: () => true,
  });
  vm.runInContext(`let accountServicesLoad = null;\n${extract("loadAccountServices")}\n${extract("initLazyAccountServices")}`, context);
  const controls = context.initLazyAccountServices("/api", modal, true);
  const first = { dataset: { email: "one@example.invalid" } }, second = { dataset: { email: "two@example.invalid" } };
  modal.emit("click", { closest: () => first }); modal.emit("click", { closest: () => second });
  assert.equal(scripts.length, 1);
  context.window.PortalAccountServices = () => ({ initAdminResearchAccessControls: () => ({ open: (button) => selected.push(button.dataset.email), close() {} }) });
  scripts[0].onload(); await flush();
  assert.deepEqual(selected, ["two@example.invalid"]);
  controls.close();
});

test("editing a membership-mode API grant preserves an existing report subset", async () => {
  const ctx = setup(true); await ctx.open();
  ctx.respond(0, { ok: true, credits: { balance: 1 } });
  ctx.respond(1, { ok: true, grant: { ...grant, report_ids: ["report-limited"] } });
  ctx.respond(2, { ok: true, preferences: { enabled: false }, reminder: {} }); await flush();
  assert.equal(ctx.node("accountAdminApiMode").value, "membership");
  ctx.node("accountAdminApiGrantForm").emit("submit");
  const payload = JSON.parse(ctx.requests[3].options.body);
  assert.deepEqual(payload.report_ids, ["report-limited"]);
  assert.equal(payload.access_mode, "membership");
  ctx.respond(3, { ok: true, grant: payload }); await flush(); ctx.controller.close();
});
