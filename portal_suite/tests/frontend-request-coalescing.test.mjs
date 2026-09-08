import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
function extractFunction(name) {
  const start = Math.min(...[`async function ${name}(`, `function ${name}(`]
    .map((text) => app.indexOf(text)).filter((index) => index >= 0));
  assert.ok(Number.isFinite(start), name);
  const body = app.indexOf("{", app.indexOf(")", start));
  let depth = 0;
  for (let i = body; i < app.length; i += 1) {
    if (app[i] === "{") depth += 1;
    else if (app[i] === "}" && --depth === 0) return app.slice(start, i + 1);
  }
  throw new Error(`Incomplete function ${name}`);
}
const flush = () => new Promise(setImmediate);
const sessionA = { token: "token-a", user: { id: "a", role: "super" } };
const sessionB = { token: "token-b", user: { id: "b", role: "user" } };
function setup() {
  const store = new Map([["session", JSON.stringify(sessionA)]]);
  const requests = [];
  const listeners = new Map();
  const nodes = new Map();
  for (const id of ["accountAccess", "openAccountPanel", "accountDownloadReport", "accountAccessHint", "accountAccessStatus", "unlockForm"]) {
    nodes.set(id, { isConnected: true, hidden: false, textContent: "", innerHTML: "", addEventListener() {} });
  }
  const context = vm.createContext({
    AbortController, setTimeout, clearTimeout,
    AUTH_SESSION_KEY: "session",
    authSessionRefreshes: new Map(),
    HOT_REPORT_SOURCE: "hot",
    localStorage: { getItem: (key) => store.get(key), setItem: (key, value) => store.set(key, value), removeItem: (key) => store.delete(key) },
    CustomEvent: class { constructor(type) { this.type = type; } },
    document: {
      getElementById: (id) => nodes.get(id) || null,
      addEventListener(type, listener) { const list = listeners.get(type) || []; list.push(listener); listeners.set(type, list); },
      dispatchEvent(event) { for (const listener of listeners.get(event.type) || []) listener(event); },
    },
    fetch(url, options) { return new Promise((resolve) => requests.push({ url, options, resolve })); },
    isContactOnlyItem: () => false,
    authUserLabel: (session) => session.user.id,
    accountRightSummary: () => "",
    requestKindForVisibleMessage: () => "",
    accessContactGuidanceHtml: () => "",
    setLineStatus: (node, text) => { node.textContent = text; },
    setLineHtmlStatus: (node, html) => { node.innerHTML = html; },
    showAccountModal() {},
  });
  vm.runInContext([
    "loadAuthSession", "saveAuthSession", "clearAuthSession", "authHeaders", "authSessionRequestKey",
    "waitForAuthSessionRefresh", "refreshAuthSession", "fetchReportAccess", "initReportAccessControls", "adminUsersSnapshotIsFresh",
  ].map(extractFunction).join("\n"), context);
  function respond(index, payload, status = 200) {
    requests[index].resolve(new Response(JSON.stringify(payload), { status, headers: { "content-type": "application/json" } }));
  }
  return { context, requests, nodes, respond };
}

test("initial auth verification and its auth-change event issue only one report access request", async () => {
  const { context, requests, nodes, respond } = setup();
  const firstAuth = context.refreshAuthSession("/api");
  const secondAuth = context.refreshAuthSession("/api");
  context.initReportAccessControls({ id: "report-1" }, "/api", "catalog", () => {});
  await flush();
  assert.deepEqual(requests.map((request) => request.url), ["/api/auth"]);
  respond(0, { token: "rotated-a", user: sessionA.user });
  await Promise.all([firstAuth, secondAuth]);
  await flush();
  assert.equal(requests.length, 2);
  assert.match(requests[1].url, /entitlement\?report_id=report-1&source=catalog/u);
  assert.equal(requests[1].options.headers.Authorization, "Bearer rotated-a");
  respond(1, { can_download: true });
  await flush();
  assert.equal(nodes.get("accountDownloadReport").hidden, false);
});

test("logout revokes visible access immediately and late success cannot restore it", async () => {
  const { context, requests, nodes, respond } = setup();
  context.initReportAccessControls({ id: "report-1" }, "/api", "catalog", () => {});
  await flush();
  assert.equal(requests.length, 1);
  nodes.get("accountDownloadReport").hidden = false;
  context.clearAuthSession();
  assert.equal(nodes.get("accountDownloadReport").hidden, true);
  respond(0, { can_download: true });
  await flush();
  assert.equal(nodes.get("accountDownloadReport").hidden, true);
  assert.equal(context.loadAuthSession(), null);
});

test("a late access 401 for a previous account does not clear or paint over a new login", async () => {
  const { context, requests, nodes, respond } = setup();
  context.initReportAccessControls({ id: "report-1" }, "/api", "catalog", () => {});
  await flush();
  context.saveAuthSession(sessionB);
  await flush();
  assert.equal(requests.length, 2);
  assert.equal(requests[0].options.headers.Authorization, "Bearer token-a");
  assert.equal(requests[1].options.headers.Authorization, "Bearer token-b");
  respond(1, { can_download: true });
  await flush();
  respond(0, { detail: "Expired old session" }, 401);
  await flush();
  assert.equal(context.loadAuthSession().user.id, "b");
  assert.equal(nodes.get("accountDownloadReport").hidden, false);
  assert.doesNotMatch(nodes.get("accountAccessStatus").textContent, /Expired/u);
});

test("late auth refresh success and failure cannot overwrite a newer account", async () => {
  for (const status of [200, 401]) {
    const { context, requests, respond } = setup();
    const pending = context.refreshAuthSession("/api");
    await flush();
    context.saveAuthSession(sessionB);
    respond(0, { token: "old-refreshed", user: sessionA.user }, status);
    await pending;
    assert.equal(requests.length, 1);
    assert.equal(context.loadAuthSession().user.id, "b");
    assert.equal(context.loadAuthSession().token, "token-b");
  }
});

test("a reward change performs a fresh access check without caching a previous grant", async () => {
  const { context, requests, nodes, respond } = setup();
  context.initReportAccessControls({ id: "report-1" }, "/api", "catalog", () => {});
  await flush();
  respond(0, { can_download: true });
  await flush();
  assert.equal(nodes.get("accountDownloadReport").hidden, false);
  context.document.dispatchEvent({ type: "portal-reward-change" });
  assert.equal(nodes.get("accountDownloadReport").hidden, true);
  await flush();
  assert.equal(requests.length, 2);
  respond(1, { can_download: false });
  await flush();
  assert.equal(nodes.get("accountDownloadReport").hidden, true);
});

test("public home metadata never fetches internal storage", () => {
  const metadata = extractFunction("updateMeta");
  assert.match(metadata, /visibleTotal/u);
  assert.match(metadata, /updated_at_bjt/u);
  assert.doesNotMatch(metadata, /internalStorage|storage|searchIndexLabel/u);
  assert.doesNotMatch(extractFunction("initIndex"), /internal\/pdf-storage/u);
});

test("only a verified fresh users snapshot avoids the automatic live users export", () => {
  const { context } = setup();
  assert.equal(context.adminUsersSnapshotIsFresh({ users: [], module_status: { users: { state: "fresh", has_data: true } } }), true);
  for (const summary of [null, {}, { users: [] },
    { users: [], module_status: { users: { state: "updating", has_data: true } } },
    { users: [], module_status: { users: { state: "fresh", has_data: false } } },
    { module_status: { users: { state: "fresh", has_data: true } } },
  ]) assert.equal(context.adminUsersSnapshotIsFresh(summary), false);
  assert.match(app, /loadAccountAdminSummary\(workerUrl, targets\)\.then\(\(summary\) => \{\s*if \(!adminUsersSnapshotIsFresh\(summary\)/u);
  assert.match(extractFunction("loadAccountAdminSummary"), /backgroundRetry: true[\s\S]*!adminUsersSnapshotIsFresh\(summary\)[\s\S]*loadFreshAdminUsers/u);
  assert.match(extractFunction("showAccountAdminModal"), /forceRefresh: true[\s\S]*await loadFreshAdminUsers\(workerUrl, targets\)/u);
  assert.match(extractFunction("loadAdminUserAccess"), /cache: "no-store"/u);
  assert.match(extractFunction("exportAdminUsersToExcel"), /fetchFreshAdminUsers\(workerUrl\)/u);
});
