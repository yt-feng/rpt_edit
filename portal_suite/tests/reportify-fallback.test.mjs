import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import { reportifyQrDataUrl } from "../../workers/portal-suite-worker/src/reportify-login-qr.js";

const workerSource = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
const appSource = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");

function extractFunction(source, name) {
  const match = new RegExp(`^(?:async )?function ${name}\\(`, "m").exec(source);
  assert.ok(match, `missing ${name}`);
  const rest = source.slice(match.index);
  const next = /\n(?:async )?function \w+\(/.exec(rest);
  return next ? rest.slice(0, next.index) : rest;
}

function fixture(overrides = {}) {
  return { readable: false, resource_limit: 0, type: 7,
    main: { report_id: "1256239582803005440", title: "Example research", render_type: "image", url_pdf: "",
      meta_data: { document_total_page: 6, file_type: "pdf" } }, items: [], ...overrides };
}

function harness({ payload = fixture(), owner = false, session = null, status = null, object = null, failSessionSave = false } = {}) {
  const values = new Map();
  if (session) values.set("reportify-auth/session.json", JSON.stringify(session));
  if (status) values.set("reportify-status/1256239582803005440.json", JSON.stringify(status));
  let finalized = 0;
  const calls = [];
  const bucket = {
    async get(key) {
      if (key === "reportify/1256239582803005440.pdf") return object;
      if (!values.has(key)) return null;
      return { text: async () => values.get(key) };
    },
    async head(key) { return key === "reportify/1256239582803005440.pdf" ? object : null; },
    async put(key, body) {
      if (failSessionSave && key === "reportify-auth/session.json") throw new Error("storage failure");
      values.set(key, body);
    },
    async delete() { throw new Error("legacy PDF must not be deleted"); },
  };
  const context = {
    URL, Request, Response, Uint8Array, Date, console,
    EXTERNAL_API: "https://api.reportify.cn", EXTERNAL_SITE: "https://reportify.cn", EXTERNAL_UA: "test",
    EXTERNAL_SESSION_KEY: "reportify-auth/session.json", EXTERNAL_R2_PREFIX: "reportify", EXTERNAL_STATUS_PREFIX: "reportify-status",
    publicSourceText: (value) => String(value || ""), externalHeaders: () => ({}),
    reportifyQrImageUrl: async (value) => reportifyQrDataUrl(value),
    currentUserFromRequest: async () => owner ? { username: "owner", email: "owner@example.test" } : { username: "member" },
    isSuperAccount: (user) => user.username === "owner" && user.email === "owner@example.test",
    jsonResponse: (_request, _env, statusCode, data) => new Response(JSON.stringify(data), { status: statusCode }),
    privateJsonResponse: (_request, _env, statusCode, data) => new Response(JSON.stringify(data), { status: statusCode }),
    derivedPasswordMatches: async () => false,
    membershipRequestAction: () => ({ kind: "access" }),
    accountDownloadDecision: async () => ({ allowed: true }),
    finalizeAccountDownloadDecision: async () => { finalized += 1; return { ok: true }; },
    scheduleHotReportArchive: () => {},
    externalPdfResponse: (_request, _env, bytes) => new Response(bytes, { headers: { "Content-Type": "application/pdf" } }),
    fetchWithTimeout: async () => ({ ok: true, status: 200, json: async () => payload }),
    fetch: async (url, init = {}) => {
      calls.push({ url, init });
      if (url.includes("/auth/wechat/qrcode/login")) return new Response(JSON.stringify({ token: "test-session-value" }));
      if (url.includes("/auth/wechat/qrcode")) return new Response(JSON.stringify({ qrcode_id: "123456789012", qrcode_url: "http://weixin.qq.com/q/test-login-fixture" }));
      return new Response(null, { status: 204 });
    },
  };
  vm.createContext(context);
  const names = ["isExternalId", "externalObjectKey", "externalStatusKey", "externalStoredStatus", "externalPutStatus",
    "reportifyStoredSession", "reportifyStoredToken", "reportifyStoreToken", "reportifyLoginQr",
    "externalAdminRequest", "externalStatusAgeMs", "externalStatusIsActive", "externalStatusIsRecentFailure", "externalPendingResponse",
    "externalIsoDate", "slimExternalItem", "slimExternalDetailItem", "externalDetailPayload", "externalDetailItem", "externalDirectPdfUrl",
    "bytesToBinaryString", "binaryStringToBytes", "sanitizePdfExternalLinksBytes", "sanitizePdfExternalLinksBody", "externalPdfHasHeader",
    "externalValidatedPdfMetadata", "externalAccessFailure", "triggerExternalGrab", "handleExternalPdf", "handleExternalStatus", "handleReportifyLoginQrStatus"];
  vm.runInContext(names.map((name) => extractFunction(workerSource, name)).join("\n"), context);
  const env = { REPORT_BUCKET: bucket, GH_REPO: "example/repo", GH_DISPATCH_TOKEN: "test-dispatch" };
  const request = new Request("https://worker.example.test/external/pdf?qr_format=inline-v1", { method: "POST", body: JSON.stringify({ id: "1256239582803005440" }) });
  return { context, env, request, calls, values, finalized: () => finalized };
}

const freshSession = () => ({ token: "test-session-value", updated_at: new Date(Date.now() - 1000).toISOString() });

test("real envelope fields override permissive nested fields and retain metadata page counts", () => {
  const { context } = harness();
  for (const pages of [5, 6]) {
    const input = fixture();
    Object.assign(input.main, { readable: true, resource_limit: 100, url_pdf: "https://files.example.test/full.pdf" });
    input.main.meta_data.document_total_page = pages;
    input.main.document_total_page = 99;
    const actual = context.externalDetailPayload(input, "1256239582803005440");
    assert.equal(actual.readable, false);
    assert.equal(actual.resource_limit, 0);
    assert.equal(actual.resource_limit_known, true);
    assert.equal(actual.pdf_url, "");
    assert.equal(actual.item.page_count, pages);
    assert.equal(actual.item.file_type, "pdf");
    assert.equal(actual.access_state, "login_required");
  }
});

test("explicit readability is not overridden by an unrelated zero allowance", () => {
  const { context } = harness();
  const input = fixture({ readable: true });
  input.main.url_pdf = "https://files.example.test/full.pdf";
  assert.equal(context.externalDetailPayload(input, "1256239582803005440", true).pdf_url, input.main.url_pdf);
});

test("public PDF minus-one allowance is accepted only with explicit readability", () => {
  const { context } = harness();
  const input = fixture({ readable: true, resource_limit: -1 });
  Object.assign(input.main, { render_type: "pdf", preview_image: null,
    url_pdf: "https://s.reportify.cn/r/public-report.pdf" });
  input.main.meta_data.document_total_page = 21;
  const actual = context.externalDetailPayload(input, "1283195192727441408");
  assert.equal(actual.readable, true);
  assert.equal(actual.resource_limit, -1);
  assert.equal(actual.resource_limit_known, true);
  assert.equal(actual.pdf_url, input.main.url_pdf);
  assert.equal(actual.item.page_count, 21);
  assert.equal(actual.access_state, "readable");
  const legacy = { main: { ...input.main, readable: true, resource_limit: -1 } };
  assert.equal(context.externalDetailPayload(legacy, "1283195192727441408").readable, true);
  for (const readable of [false, undefined, null, "true", 1]) {
    const result = context.externalDetailPayload({ ...input, readable }, "1283195192727441408");
    assert.equal(result.readable, false);
    assert.equal(result.pdf_url, "");
    assert.equal(result.access_state, "unavailable");
  }
  for (const resource_limit of [-2, -0.5, "-1", null, true, Infinity, NaN]) {
    const result = context.externalDetailPayload({ ...input, resource_limit }, "1283195192727441408");
    assert.equal(result.readable, false);
    assert.equal(result.pdf_url, "");
    assert.equal(result.access_state, "unavailable");
  }
});

test("legacy nested controls work only when envelope controls are absent; malformed data fails closed", () => {
  const { context } = harness();
  const legacy = { main: { readable: true, resource_limit: 1, url_pdf: "https://files.example.test/full.pdf" } };
  assert.equal(context.externalDetailPayload(legacy, "1256239582803005440").readable, true);
  for (const input of [{ main: {} }, fixture({ readable: "false" }), fixture({ resource_limit: "unknown" }),
    { resource_limit: 0, main: { readable: true, url_pdf: "https://files.example.test/full.pdf" } }]) {
    assert.equal(context.externalDetailPayload(input, "1256239582803005440").access_state, "unavailable");
  }
  for (const input of [null, [], {}, { main: [] }]) assert.equal(context.externalDetailPayload(input, "1256239582803005440"), null);
});

test("blocked anonymous source requires owner connection before dispatch", async () => {
  const h = harness({ owner: true });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  const data = await response.json();
  assert.equal(response.status, 409);
  assert.equal(data.error_code, "upstream_login_required");
  assert.equal(data.login_required, true);
  assert.ok(data.qrcode_id);
  assert.equal(h.calls.some(({ url }) => url.includes("api.github.com")), false);
});

test("connected but unreadable source is an access requirement, not an anonymous retry", async () => {
  const h = harness({ owner: true, session: freshSession() });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  const data = await response.json();
  assert.equal(data.error_code, "upstream_access_required");
  assert.equal(data.login_required, false);
  assert.equal(data.reauth_available, true);
  assert.equal(h.calls.some(({ url }) => url.includes("api.github.com")), false);
});

test("member source-access failure offers preview and full-text request without credentials or QR", async () => {
  const h = harness({ session: freshSession() });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  const data = await response.json();
  assert.equal(response.status, 503);
  assert.equal(data.preview_only, true);
  assert.equal(data.request_required, true);
  assert.equal(data.preview_report_id, "1256239582803005440");
  assert.doesNotMatch(JSON.stringify(data), /reportify|qrcode|test-session-value/i);
  assert.equal(h.calls.length, 0);
});

test("malformed source response cannot launch a grab or pretend authentication will fix it", async () => {
  const h = harness({ owner: true, payload: { main: {} } });
  const data = await (await h.context.handleExternalPdf(h.request, h.env)).json();
  assert.equal(data.error_code, "upstream_unavailable");
  assert.equal(h.calls.length, 0);
});

test("new saved session escapes old failure cooldown and dispatch never carries credentials", async () => {
  const session = freshSession();
  const h = harness({ owner: true, session, payload: fixture({ readable: true }),
    status: { status: "failed", updated_at: new Date(Date.now() - 60000).toISOString() } });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  assert.equal(response.status, 202);
  const dispatch = h.calls.find(({ url }) => url.includes("api.github.com"));
  assert.deepEqual(JSON.parse(dispatch.init.body).client_payload, { id: "1256239582803005440" });
  assert.doesNotMatch(dispatch.init.body, /token|cookie|test-session-value/i);
});

test("QR login reports ready only after successful secret storage and readback", async () => {
  for (const failSessionSave of [false, true]) {
    const h = harness({ owner: true, failSessionSave });
    const request = new Request("https://worker.example.test/external/login-qr/status?qrcode_id=123456789012");
    const response = await h.context.handleReportifyLoginQrStatus(request, h.env);
    const data = await response.json();
    assert.equal(data.ready, !failSessionSave);
    assert.equal(response.status, failSessionSave ? 503 : 200);
    assert.doesNotMatch(JSON.stringify(data), /test-session-value|"token"/);
  }
});

test("small complete validated PDFs are ready, while unverified legacy objects are preserved", async () => {
  for (const validated of [true, false]) {
    const object = { size: 1024, customMetadata: validated
      ? { validated: "true", page_count: "6", expected_page_count: "6" } : {} };
    const h = harness({ object, status: { status: "ready", updated_at: new Date().toISOString() } });
    const response = await h.context.handleExternalStatus(new Request("https://worker.example.test/external/status?id=1256239582803005440"), h.env);
    assert.equal((await response.json()).ready, validated);
  }
  const { context } = harness();
  assert.equal(context.externalValidatedPdfMetadata({ customMetadata: { validated: "true", page_count: "5", expected_page_count: "6" } }), false);
  assert.equal(context.externalValidatedPdfMetadata({ customMetadata: { validated: "true", page_count: "6", expected_page_count: "invalid" } }), false);
});

test("legacy bytes are not deleted and unsigned direct URLs never bypass PDF validation", async () => {
  const input = fixture({ readable: true });
  input.main.url_pdf = "https://files.example.test/full.pdf";
  const h = harness({ owner: true, payload: input, object: { body: new TextEncoder().encode("%PDF-legacy"), customMetadata: {} } });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  assert.equal(response.status, 202);
  assert.equal(h.finalized(), 0);
  assert.equal(h.calls.some(({ url }) => url.includes("files.example.test")), false);
});

test("existing cached bytes can be validated without new upstream download permission", async () => {
  const h = harness({ owner: true, payload: fixture(), object: { body: new TextEncoder().encode("%PDF-legacy"), customMetadata: {} } });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  assert.equal(response.status, 202);
  assert.equal(h.finalized(), 0);
  assert.equal(h.calls.some(({ url }) => url.includes("api.github.com")), true);
  assert.equal(h.calls.some(({ url }) => url.includes("/auth/wechat")), false);
});

test("verified complete cache is delivered even when upstream now requires access", async () => {
  const object = { body: new TextEncoder().encode("%PDF-verified-six-pages"), size: 24,
    customMetadata: { validated: "true", page_count: "6", expected_page_count: "6" } };
  const h = harness({ owner: true, object });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  assert.equal(response.status, 200);
  assert.equal(response.headers.get("Content-Type"), "application/pdf");
  assert.equal(h.finalized(), 1);
  assert.equal(h.calls.length, 0);
});

test("eligible member acquisition is queued, not downgraded to preview or charged before delivery", async () => {
  const h = harness({ payload: fixture({ readable: true }) });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  const data = await response.json();
  assert.equal(response.status, 202);
  assert.equal(data.preview_only, undefined);
  assert.equal(h.finalized(), 0);
  assert.equal(h.calls.filter(({ url }) => url.includes("api.github.com")).length, 1);
});

test("failed member acquisition and source timeouts expose preview plus request, never credentials", async () => {
  const h = harness({ status: { status: "failed", updated_at: new Date().toISOString() } });
  const failed = await (await h.context.handleExternalStatus(
    new Request("https://worker.example.test/external/status?id=1256239582803005440"), h.env)).json();
  assert.equal(failed.preview_only, true);
  assert.equal(failed.request_required, true);
  assert.equal(failed.ready, false);
  assert.equal(h.finalized(), 0);
  h.context.externalDirectPdfUrl = async () => { throw new Error("private upstream failure"); };
  const timedOut = await (await h.context.handleExternalPdf(h.request, h.env)).json();
  assert.equal(timedOut.preview_only, true);
  assert.equal(timedOut.request_required, true);
  assert.doesNotMatch(JSON.stringify(timedOut), /private upstream failure|token|qrcode/);
  assert.equal(h.finalized(), 0);
});

test("a revoked member entitlement prevents cache delivery and is not relabeled as preview", async () => {
  const object = { body: new TextEncoder().encode("%PDF-verified-six-pages"),
    customMetadata: { validated: "true", page_count: "6", expected_page_count: "6" } };
  const h = harness({ object });
  h.context.finalizeAccountDownloadDecision = async () => ({ ok: false, status: 403, error: "Access expired" });
  const response = await h.context.handleExternalPdf(h.request, h.env);
  assert.equal(response.status, 403);
  const data = await response.json();
  assert.equal(data.preview_only, undefined);
  assert.equal(data.error, "Access expired");
});

test("upstream authentication rejection prompts owner reconnect even with a stored token", async () => {
  const h = harness({ owner: true, session: freshSession() });
  h.context.fetchWithTimeout = async () => ({ ok: false, status: 401 });
  const data = await (await h.context.handleExternalPdf(h.request, h.env)).json();
  assert.equal(data.error_code, "upstream_login_required");
  assert.equal(data.login_required, true);
  assert.equal(h.calls.some(({ url }) => url.includes("api.github.com")), false);
});

test("upstream 403 with a connected account is classified as unavailable access", async () => {
  const h = harness({ owner: true, session: freshSession() });
  h.context.fetchWithTimeout = async () => ({ ok: false, status: 403 });
  const data = await (await h.context.handleExternalPdf(h.request, h.env)).json();
  assert.equal(data.error_code, "upstream_access_required");
  assert.equal(data.reauth_available, true);
});

test("owner status polling keeps authentication and displays connection recovery", () => {
  const poll = extractFunction(appSource.replace(/^  /gm, ""), "pollExternalDetail");
  assert.match(poll, /headers:\s*authHeaders\(\)/);
  assert.match(poll, /showExternalLoginQr\(statusElement, workerUrl, data, onReady\)/);
  const login = extractFunction(appSource.replace(/^  /gm, ""), "showExternalLoginQr");
  assert.match(login, /error\.reauth_available/);
  assert.match(login, /await onReady\(\)/);
});

test("ready polling awaits download rejection and shows the error or connection recovery", async () => {
  const source = extractFunction(appSource.replace(/^  /gm, ""), "pollExternalDetail");
  for (const mode of ["ordinary", "login", "request"]) {
    let tick;
    let stopped = false;
    const statuses = [];
    const recoveries = [];
    const requests = [];
    const statusElement = {};
    const context = {
      Date, encodeURIComponent,
      window: { setInterval: (callback) => { tick = callback; return 1; }, clearInterval: () => { stopped = true; } },
      authHeaders: () => ({ Authorization: "Bearer account-session" }),
      fetch: async (_url, options) => {
        assert.equal(options.headers.Authorization, "Bearer account-session");
        return { json: async () => ({ ready: true }) };
      },
      document: { getElementById: () => statusElement },
      showExternalLoginQr: (element, _url, error, retry) => {
        recoveries.push({ element, error, retry });
        return Boolean(error.login_required);
      },
    };
    vm.createContext(context);
    vm.runInContext(source, context);
    const failure = Object.assign(new Error(`download rejected: ${mode}`), {
      login_required: mode === "login", request_required: mode === "request",
    });
    const retry = async () => { await Promise.resolve(); throw failure; };
    context.pollExternalDetail("https://worker.example.test", "1256239582803005440", "",
      (message, kind) => statuses.push({ message, kind }), retry,
      (message, error) => requests.push({ message, error }));
    await tick();
    assert.equal(stopped, true);
    assert.equal(statuses.at(-1).message, failure.message);
    assert.equal(statuses.at(-1).kind, "error");
    assert.equal(recoveries.length, 1);
    assert.equal(recoveries[0].error, failure);
    assert.equal(recoveries[0].element, statusElement);
    assert.equal(recoveries[0].retry, retry);
    assert.equal(requests.length, mode === "request" ? 1 : 0);
  }
});
