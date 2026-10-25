import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa", reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
const passwordA = "PORTAL-TEST-AAAA-AAAA", passwordB = "PORTAL-TEST-BBBB-BBBB";

function extractFunction(name, from = 0) {
  const marker = source.indexOf(`function ${name}(`, from);
  assert.ok(marker >= 0, name);
  const start = source.slice(marker - 6, marker) === "async " ? marker - 6 : marker;
  const body = source.indexOf("{", source.indexOf(")", marker));
  let depth = 0;
  for (let index = body; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    if (source[index] === "}" && --depth === 0) return source.slice(start, index + 1);
  }
  throw new Error(`Unclosed ${name}`);
}

function harness({ query = "", hash = "", local = new Map(), session = new Map() } = {}) {
  const events = new Map(), documentEvents = new Map(), timers = [], statuses = [];
  const storage = (map) => ({ getItem: (key) => map.get(key) || null, setItem: (key, value) => map.set(key, String(value)), removeItem: (key) => map.delete(key) });
  const window = { location: { href: `https://example.invalid/report.html?id=${reportB}${query}`, search: `?id=${reportB}${query}`, hash },
    history: { state: {}, replaceState(state) { this.state = state; } },
    addEventListener(name, callback) { events.set(name, callback); }, setTimeout(callback) { timers.push(callback); },
  };
  const document = { body: { dataset: {} }, hidden: false, addEventListener(name, callback) { documentEvents.set(name, callback); } };
  const context = vm.createContext({ window, document, URL, URLSearchParams,
    localStorage: storage(local), sessionStorage: storage(session), DOWNLOAD_PASSWORD_KEY: "fixture-download-password",
    getAdminToken: () => "fixture-admin-token", canUseDeliveryTools: () => true, authHeaders: () => ({}),
    getAdminPlainKey: () => "fixture-cached-private-key", clearAdminToken() {},
    publicDocItem: (item) => item, reportPreviewItem: () => null, EXTERNAL_SOURCE: "external",
  });
  vm.runInContext("const rejectedDownloadPasswords = new Map();", context);
  for (const name of ["getRememberedDownloadPassword", "setRememberedDownloadPassword", "clearRememberedDownloadPassword",
    "deliveryPasswordFromLocation", "deliveryPasswordFromHistory", "getRecoverableDownloadPassword", "rememberDeliveryPassword",
    "initResilientPasswordInput", "reportPageUrl", "externalPageUrl", "requestReportPassword", "requestExternalPassword"])
    vm.runInContext(extractFunction(name), context);
  return { context, window, local, session, statuses,
    call(name, ...args) { return context[name](...args); },
    input(reportId, explicit = "") { const input = { value: "", isConnected: true }; context.initResilientPasswordInput(input, reportId, explicit, (message) => statuses.push(message)); return input; },
    restore() { for (const callback of timers) callback(); events.get("pageshow")?.(); events.get("focus")?.(); documentEvents.get("visibilitychange")?.(); },
  };
}

test("report-bound passwords never migrate through a global last-used fallback", () => {
  const h = harness();
  h.local.set("fixture-download-password", passwordA); // Old-version global cache.
  assert.equal(h.call("getRecoverableDownloadPassword", reportB, ""), "");
  h.call("rememberDeliveryPassword", reportA, passwordA);
  assert.equal(h.local.has("fixture-download-password"), false);
  assert.equal(h.input(reportB).value, "");
  assert.equal(h.local.has(`fixture-download-password:${reportB}`), false);
  assert.equal(h.call("getRecoverableDownloadPassword", reportA, ""), passwordA);
  assert.equal(h.input(reportB, passwordB).value, passwordB);
  assert.equal(h.call("getRememberedDownloadPassword", reportA), passwordA);
});

test("unscoped history cannot supply a different report's credential", () => {
  const h = harness();
  h.window.history.state = { portalDeliveryPassword: passwordA };
  assert.equal(h.call("getRecoverableDownloadPassword", reportB, ""), "");
  h.window.history.state.portalDeliveryReportId = reportA;
  assert.equal(h.call("getRecoverableDownloadPassword", reportB, ""), "");
});

test("a rejected value is not revived from query, fragment, history or restore callbacks", () => {
  for (const location of [{ query: `&password=${encodeURIComponent(passwordB)}` }, { hash: `#?password=${encodeURIComponent(passwordB)}` }]) {
    const h = harness(location); const input = h.input(reportB, passwordB);
    assert.equal(input.value, passwordB);
    h.call("clearRememberedDownloadPassword", reportB, passwordB);
    input.value = ""; h.restore();
    assert.equal(input.value, "");
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), "");
    assert.equal(h.window.history.state.portalDeliveryPassword, undefined);
    h.call("clearRememberedDownloadPassword", reportB, "second-rejected-value");
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), "");
  }
});

test("rejecting an in-flight value preserves a newer report-scoped replacement", () => {
  const h = harness({ query: `&password=${encodeURIComponent(passwordB)}` });
  const input = h.input(reportB, passwordB);
  const replacement = "manually-entered-replacement";
  h.call("rememberDeliveryPassword", reportB, replacement);
  h.window.history.state.unrelated = "preserved";
  h.call("clearRememberedDownloadPassword", reportB, passwordB);
  assert.equal(h.call("getRememberedDownloadPassword", reportB), replacement);
  assert.equal(h.session.get(`fixture-download-password:${reportB}`), replacement);
  assert.equal(h.window.history.state.portalDeliveryPassword, replacement);
  assert.equal(h.window.history.state.unrelated, "preserved");
  input.value = ""; h.restore();
  assert.equal(input.value, replacement, "a rejected explicit/query value cannot mask a new scoped replacement");
  h.window.location.search = `?id=${reportA}&password=${encodeURIComponent(passwordB)}`;
  assert.equal(h.call("getRecoverableDownloadPassword", reportA, ""), passwordB, "rejection applies only to its report context");
});

test("delivery links roundtrip special characters and preserve explicit password priority", () => {
  const h = harness(); const password = " +/#中文 &?= ";
  const reportUrl = new URL(h.call("reportPageUrl", reportB, { password }));
  assert.equal(reportUrl.searchParams.get("id"), reportB);
  assert.equal(reportUrl.searchParams.get("password"), password);
  assert.equal(reportUrl.hash, "");
  const external = new URL(h.call("externalPageUrl", { id: "thinktank:canonical-01", source: "thinktank" }, password));
  assert.equal(external.searchParams.get("id"), "thinktank:canonical-01");
  assert.equal(external.searchParams.get("password"), password);
  h.window.location.search = reportUrl.search;
  h.call("rememberDeliveryPassword", reportB, "older-scoped-value");
  assert.equal(h.call("getRecoverableDownloadPassword", reportB, ""), password);
  h.window.location.search = `?id=${reportB}`; h.window.location.hash = `#password=${encodeURIComponent(password)}`;
  assert.equal(h.call("deliveryPasswordFromLocation"), password);
});

function catalogSubmission(h, fetch, signedIn = null) {
  const input = { value: passwordB, isConnected: true }, status = { classList: { add() {} } }, button = {};
  Object.assign(h.context, { input, status, button, workerUrl: "/api", item: { id: reportB, filename: "example.pdf" }, fetch,
    loadAuthSession: () => signedIn, trackEvent() {}, analyticsReportPayload: () => ({}),
    downloadErrorMessage: (_code, message) => message, maybeAlertDownloadLimit() {}, requestActionStatusHtml: (message) => message,
    requestKindForVisibleMessage: () => "support", triggerBlobDownload() {}, showDownloadInvitation() {},
  });
  const renderStart = source.indexOf("function renderDetail(");
  assert.ok(renderStart > 0);
  const submit = vm.runInContext(`(${extractFunction("submitDownload", renderStart)})`, h.context);
  return { input, submit };
}

test("catalog 401 cleanup uses the actual submitted password and preserves edits made while waiting", async () => {
  const h = harness({ query: `&password=${encodeURIComponent(passwordB)}` });
  let finish, submitted;
  const { input, submit } = catalogSubmission(h, async (_url, options) => {
    submitted = JSON.parse(options.body).password;
    return new Promise((resolve) => { finish = resolve; });
  });
  h.call("rememberDeliveryPassword", reportB, passwordB);
  const pending = submit();
  input.value = "new-manual-value"; h.call("rememberDeliveryPassword", reportB, input.value);
  finish({ ok: false, status: 401, json: async () => ({ error: "Password is incorrect." }) });
  await pending;
  assert.equal(submitted, passwordB);
  assert.equal(input.value, "new-manual-value");
  assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), "new-manual-value");
});

test("guest manual success is scoped, while account-authorized success does not validate a password", async () => {
  for (const current of [null, { token: "fixture-session" }]) {
    const h = harness();
    const { input, submit } = catalogSubmission(h, async () => ({ ok: true, status: 200, blob: async () => ({}), headers: { get: () => "" } }), current);
    input.value = "shared-password-entered-manually";
    await submit();
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, ""), current ? "" : input.value);
    assert.equal(h.call("getRememberedDownloadPassword", reportA), "");
    assert.equal(h.local.has("fixture-download-password"), false);
  }
});

test("only a confirmed guest password success releases a previous catalog rejection", async () => {
  for (const current of [null, { token: "fixture-session" }]) {
    const h = harness();
    h.call("clearRememberedDownloadPassword", reportB, passwordB);
    h.call("rememberDeliveryPassword", reportB, passwordB);
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), "", "initialization does not validate a rejected password");
    const { submit } = catalogSubmission(h, async () => ({ ok: true, status: 200, blob: async () => ({}), headers: { get: () => "" } }), current);
    await submit();
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), current ? "" : passwordB);
  }
});

test("external password success releases rejection, but pending, account and contact success do not", async () => {
  for (const mode of ["password", "pending", "account", "contact"]) {
    const h = harness();
    h.call("clearRememberedDownloadPassword", reportB, passwordB);
    Object.assign(h.context, {
      trackEvent() {}, analyticsReportPayload: () => ({}), isContactOnlyItem: () => mode === "contact",
      docEndpoint: () => "external", triggerBlobDownload() {}, showDownloadInvitation() {},
      fetch: async () => ({ ok: true, status: mode === "pending" ? 202 : 200,
        blob: async () => ({}), json: async () => ({ wait_seconds: 30 }), headers: { get: () => "" } }),
    });
    const fetchPdf = vm.runInContext(`(${extractFunction("fetchExternalPdf")})`, h.context);
    await fetchPdf("/api", { id: reportB, source: "external" }, passwordB, () => {}, { auth: mode === "account" });
    assert.equal(h.call("getRecoverableDownloadPassword", reportB, passwordB), mode === "password" ? passwordB : "", mode);
  }
});

test("delivery generation failures never return a cached administrator key", async () => {
  for (const name of ["requestReportPassword", "requestExternalPassword"]) {
    for (const status of [401, 404, 503, 200]) {
      const h = harness();
      h.context.fetch = async () => ({ ok: status === 200, status, json: async () => ({ error: "fixture generation failure" }) });
      await assert.rejects(h.call(name, "/api", reportB), /fixture generation failure/);
    }
    for (const payload of [null, {}, { password: "" }, { password: "   " }, { password: 123 }, { password: {} }]) {
      const h = harness();
      h.context.fetch = async () => ({ ok: true, status: 200, json: async () => payload });
      await assert.rejects(h.call(name, "/api", reportB), /Could not generate delivery link/);
    }
    const malformed = harness();
    malformed.context.fetch = async () => ({ ok: true, status: 200, json: async () => { throw new SyntaxError("fixture malformed JSON"); } });
    await assert.rejects(malformed.call(name, "/api", reportB), /Could not generate delivery link/);
    const h = harness(); h.context.fetch = async () => { throw new Error("fixture network failure"); };
    await assert.rejects(h.call(name, "/api", reportB), /fixture network failure/);
  }
});

test("successful generation retains server-returned canonical external identity and password", async () => {
  const h = harness();
  h.context.fetch = async () => ({ ok: true, status: 200, json: async () => ({ id: "thinktank:canonical-02", password: passwordB }) });
  const result = await h.call("requestExternalPassword", "/api", "thinktank:alias-02", "thinktank");
  assert.equal(result.id, "thinktank:canonical-02");
  assert.equal(result.password, passwordB);
  assert.match(source, /const deliveryItem = data\.id \? \{ \.\.\.item, id: data\.id, source: item\.source \} : item;/);
});
