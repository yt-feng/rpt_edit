import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
const reportId = "1256239582803005440";
const hotId = "hot:0123456789abcdef";
const assetUrl = `https://files.reportify.cn/report/preview/${reportId}.jpeg`;
const png = Uint8Array.from(Buffer.from("iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAQAAAC1HAwCAAAAC0lEQVR42mP8/x8AAusB9Wl6mEIAAAAASUVORK5CYII=", "base64"));
function extract(name) {
  const match = new RegExp(`^(?:async )?function ${name}\\(`, "m").exec(source);
  assert.ok(match, `missing ${name}`);
  const rest = source.slice(match.index);
  const next = /\n(?:async )?function \w+\(/.exec(rest);
  return next ? rest.slice(0, next.index) : rest;
}
function json(_request, _env, status, data) {
  return new Response(JSON.stringify(data), { status, headers: { "Cache-Control": "no-store, private" } });
}
function harness({ signedIn = true, admin = false, previewImage = assetUrl, asset,
  session = null, rowOrigin = "external", objectOrigin = "external", membership = true } = {}) {
  const calls = [];
  const bodyReads = [];
  const finalizations = [];
  const prohibited = (name) => () => { throw new Error(`unexpected ${name}`); };
  const context = {
    URL, Request, Response, Uint8Array, TextDecoder, Date, setTimeout, clearTimeout,
    EXTERNAL_API: "https://api.reportify.cn", EXTERNAL_SITE: "https://reportify.cn", EXTERNAL_UA: "test",
    EXTERNAL_SESSION_KEY: "auth/session.json", HOT_REPORT_REQUIRED_PLAN: "pro", HOT_REPORT_MIN_MONTHS: 3, THINKTANK_SOURCE: "thinktank",
    currentUserFromRequest: async () => { if (!signedIn) throw new Error("Login required"); return { admin }; },
    isSuperAccount: (user) => Boolean(user.admin),
    corsHeaders: () => ({}), privateJsonResponse: json, jsonResponse: json,
    accountDownloadDecision: async () => { calls.push("quota-decision"); return { allowed: true }; },
    finalizeAccountDownloadDecision: async (_env, _request, decision) => { finalizations.push(decision); return { ok: true }; },
    derivedPasswordMatches: async (_env, id, password) => password === `signed:${id}`,
    sharedReportPasswordMatches: async (_env, id, password) => password === `signed:${id}` || password === "shared",
    externalDirectPdfUrl: async () => { calls.push("upstream-full"); return { item: { page_count: 1 }, title: "Research" }; },
    externalObjectKey: (id) => `full/${id}.pdf`,
    externalValidatedPdfMetadata: () => true, externalPdfHasHeader: () => true,
    sanitizePdfExternalLinksBody: async (body) => body,
    externalPdfResponse: (_request, _env, body) => new Response(body, { headers: { "Content-Type": "application/pdf" } }),
    scheduleHotReportArchive: () => { calls.push("archive"); },
    triggerExternalGrab: prohibited("full grab"),
    cleanHotReportId: (id) => id === hotId ? id : "",
    hotReportPdfKey: (id) => `hot/${id}.pdf`,
    hotReportAccessForUser: async () => ({ can_download: membership }),
    accessContactMessage: (_request, message) => message,
    findHotReportRow: async () => ({ row: { origin_source: rowOrigin, origin_report_id: reportId }, item: { filename: "research.pdf" } }),
    contentDisposition: () => 'attachment; filename="research.pdf"',
    fetchWithTimeout: async (url, init) => {
      calls.push({ url, init });
      if (url === `https://api.reportify.cn/reports/${reportId}`) {
        return Response.json({ readable: false, resource_limit: 0, main: { preview_image: previewImage,
          meta_data: { document_total_page: 6 } } });
      }
      return asset ? asset(url, init, calls) : new Response(png, { headers: { "Content-Type": "image/png" } });
    },
  };
  vm.createContext(context);
  for (const name of ["isExternalId", "cleanHotReportOriginSource", "externalHeaders", "reportifyStoredSession", "externalAdminRequest",
    "externalPreviewAssetUrl", "externalPreviewReadBytes", "externalPreviewImageType", "handleExternalPreview",
    "handleExternalConnectionStatus", "handleExternalPdf", "handleHotReportPdf"]) vm.runInContext(extract(name), context);
  const env = { REPORT_BUCKET: {
    async get(key) {
      if (key === "auth/session.json") { calls.push("read-session"); return session ? { text: async () => JSON.stringify(session) } : null; }
      bodyReads.push(key);
      return { body: new TextEncoder().encode("%PDF-verified-complete"), customMetadata: { origin_source: objectOrigin } };
    },
    async head() { return { customMetadata: { origin_source: objectOrigin, origin_report_id: reportId } }; },
    put: prohibited("R2 write"), delete: prohibited("R2 delete"),
  } };
  return { context, env, calls, bodyReads, finalizations };
}
const previewRequest = () => new Request(`https://worker.test/external/preview?id=${reportId}`);
const fullRequest = (id = reportId, password = "") => new Request("https://worker.test/pdf", {
  method: "POST", body: JSON.stringify({ id, password }),
});

test("preview authenticates first and validates the report ID before any upstream or storage request", async () => {
  const anonymous = harness({ signedIn: false });
  assert.equal((await anonymous.context.handleExternalPreview(previewRequest(), anonymous.env)).status, 401);
  const invalid = harness();
  assert.equal((await invalid.context.handleExternalPreview(new Request("https://worker.test/external/preview?id=bad"), invalid.env)).status, 400);
  for (const h of [anonymous, invalid]) { assert.equal(h.calls.length, 0); assert.equal(h.bodyReads.length, 0); }
});

test("member and admin receive exactly the anonymous API image with one-page private headers and no full access side effects", async () => {
  for (const admin of [false, true]) {
    const h = harness({ admin, session: { token: "private-token", updated_at: new Date().toISOString() } });
    const response = await h.context.handleExternalPreview(previewRequest(), h.env);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("Content-Type"), "image/png");
    assert.equal(response.headers.get("X-Portal-Preview-Pages"), "1");
    assert.equal(response.headers.get("Cache-Control"), "no-store, private");
    assert.deepEqual(new Uint8Array(await response.arrayBuffer()), png);
    assert.deepEqual(h.calls.map(({ url }) => url), [`https://api.reportify.cn/reports/${reportId}`, assetUrl]);
    for (const { init } of h.calls) {
      assert.equal(init.redirect, "manual");
      assert.equal(new Headers(init.headers).has("Authorization"), false);
      assert.equal(new Headers(init.headers).has("Cookie"), false);
    }
    assert.equal(h.bodyReads.length, 0);
    assert.equal(h.finalizations.length, 0);
  }
});

test("missing and untrusted API preview URLs never trigger guessed URLs or PDF conversion", async () => {
  for (const previewImage of [null, "", "http://files.reportify.cn/a.png", "https://evil.test/a.png",
    "https://files.reportify.cn.evil.test/a.png", "https://user:pass@files.reportify.cn/a.png",
    "https://files.reportify.cn:8443/a.png", "https://files.reportify.cn/a.png#fragment"]) {
    const h = harness({ previewImage });
    const response = await h.context.handleExternalPreview(previewRequest(), h.env);
    assert.equal(response.status, 503, String(previewImage));
    assert.equal(h.calls.length, 1);
    assert.doesNotMatch(await response.text(), /reportify|evil\.test/i);
  }
});

test("preview redirects are manual, bounded and remain on the same HTTPS image allowlist", async () => {
  const allowed = harness({ asset: (url) => url === assetUrl
    ? new Response(null, { status: 302, headers: { Location: "https://s.reportify.cn/cover.png" } })
    : new Response(png, { headers: { "Content-Type": "image/png" } }) });
  assert.equal((await allowed.context.handleExternalPreview(previewRequest(), allowed.env)).status, 200);
  for (const location of ["https://evil.test/cover.png", "http://files.reportify.cn/cover.png", "/loop.png"]) {
    const h = harness({ asset: () => new Response(null, { status: 302, headers: { Location: location } }) });
    assert.equal((await h.context.handleExternalPreview(previewRequest(), h.env)).status, 503);
    assert.equal(h.calls.length, location === "/loop.png" ? 5 : 2);
  }
});

test("preview rejects PDF, HTML, MIME mismatch, malformed image, and oversized declared or streamed bodies", async () => {
  const fixtures = [
    () => new Response("%PDF-1.7", { headers: { "Content-Type": "application/pdf" } }),
    () => new Response("<html>login</html>", { headers: { "Content-Type": "image/jpeg" } }),
    () => new Response(png, { headers: { "Content-Type": "image/webp" } }),
    () => new Response(png.subarray(0, png.length - 5), { headers: { "Content-Type": "image/png" } }),
    () => new Response(png, { headers: { "Content-Type": "image/png", "Content-Length": String(10 * 1024 * 1024 + 1) } }),
    () => new Response(new Uint8Array(10 * 1024 * 1024 + 1), { headers: { "Content-Type": "image/png" } }),
  ];
  for (const asset of fixtures) {
    const h = harness({ asset });
    const response = await h.context.handleExternalPreview(previewRequest(), h.env);
    assert.equal(response.status, 503);
    assert.equal((await response.json()).error_code, "preview_unavailable");
    assert.equal(h.bodyReads.length, 0);
  }
});

test("connection status is super-only, never returns a token, and expires saved sessions at 12 hours", async () => {
  for (const signedIn of [false, true]) {
    const h = harness({ signedIn });
    assert.equal((await h.context.handleExternalConnectionStatus(previewRequest(), h.env)).status, 403);
    assert.equal(h.calls.length, 0);
  }
  for (const age of [1000, 13 * 60 * 60 * 1000, -60000]) {
    const session = { token: "private-token", updated_at: new Date(Date.now() - age).toISOString() };
    const h = harness({ admin: true, session });
    const response = await h.context.handleExternalConnectionStatus(previewRequest(), h.env);
    const data = await response.json();
    assert.equal(data.connected, age === 1000);
    assert.deepEqual(Object.keys(data).sort(), ["connected", "expires_at", "updated_at"]);
    if (data.connected) assert.equal(Date.parse(data.expires_at) - Date.parse(data.updated_at), 12 * 60 * 60 * 1000);
    assert.doesNotMatch(JSON.stringify(data), /private-token|"token"/);
    assert.equal(h.bodyReads.length, 0);
  }
});

test("ordinary member cannot read a validated full cache or dispatch a grab, including with a shared password", async () => {
  for (const password of ["", "shared", "signed:another-report"]) {
    const h = harness();
    const response = await h.context.handleExternalPdf(fullRequest(reportId, password), h.env);
    assert.equal(response.status, 403);
    const data = await response.json();
    assert.equal(data.preview_only, true);
    assert.equal(data.preview_report_id, reportId);
    assert.equal(h.calls.length, 0);
    assert.equal(h.bodyReads.length, 0);
    assert.equal(h.finalizations.length, 0);
  }
});

test("super account and explicit report-bound delivery retain full access", async () => {
  for (const admin of [false, true]) {
    const h = harness({ admin });
    const response = await h.context.handleExternalPdf(fullRequest(reportId, admin ? "" : `signed:${reportId}`), h.env);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("Content-Type"), "application/pdf");
    assert.equal(h.bodyReads.length, 1);
    assert.equal(h.finalizations.length, 1);
    if (!admin) assert.equal(h.finalizations[0].allowed, false, "delivery does not spend member quota");
  }
});

test("hot archives enforce external preview policy from either row or legacy object metadata before reading PDF body", async () => {
  for (const [rowOrigin, objectOrigin] of [["external", ""], ["", "external"], ["catalog", "external"], [" External ", ""]]) {
    for (const password of ["", "shared"]) {
      const h = harness({ rowOrigin, objectOrigin, membership: false });
      const response = await h.context.handleHotReportPdf(fullRequest(hotId, password), h.env);
      assert.equal(response.status, 403);
      const data = await response.json();
      assert.equal(data.preview_only, true);
      assert.equal(data.preview_report_id, reportId);
      assert.equal(h.bodyReads.length, 0);
    }
  }
});

test("hot archives preserve super access and exact hot-report deliveries without changing other report memberships", async () => {
  const cases = [
    [{ admin: true }, "", 200],
    [{}, `signed:${hotId}`, 200],
    [{ rowOrigin: "catalog", objectOrigin: "catalog" }, "", 200],
    [{ rowOrigin: "thinktank", objectOrigin: "thinktank", membership: false }, "", 402],
    [{ rowOrigin: "catalog", objectOrigin: "catalog", membership: false }, "shared", 200],
  ];
  for (const [options, password, status] of cases) {
    const h = harness(options);
    const response = await h.context.handleHotReportPdf(fullRequest(hotId, password), h.env);
    assert.equal(response.status, status);
    assert.equal(h.bodyReads.length, status === 200 ? 1 : 0);
  }
});

test("production router exposes only the authenticated preview and super connection GET handlers", () => {
  assert.match(source, /pathname === "\/external\/preview" && request.method === "GET"\)\s*\{\s*return handleExternalPreview\(request, env\)/);
  assert.match(source, /pathname === "\/external\/connection-status" && request.method === "GET"\)\s*\{\s*return handleExternalConnectionStatus\(request, env\)/);
});
