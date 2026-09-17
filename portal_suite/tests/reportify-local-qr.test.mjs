import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";
import { reportifyQrDataUrl } from "../../workers/portal-suite-worker/src/reportify-login-qr.js";

const worker = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
const app = (await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8")).replace(/^  /gm, "");
function fn(source, name) {
  const start = new RegExp(`^(?:async )?function ${name}\\(`, "m").exec(source);
  assert.ok(start, `missing ${name}`);
  const rest = source.slice(start.index);
  const next = /\n(?:async )?function \w+\(/.exec(rest);
  return next ? rest.slice(0, next.index) : rest;
}
const ticket = "http://weixin.qq.com/q/non-secret-fixture";
function workerHarness({ owner = true, payload = ticket } = {}) {
  const requests = [];
  const context = { URL, Response, EXTERNAL_API: "https://api.reportify.cn", EXTERNAL_SITE: "https://reportify.cn",
    externalHeaders: () => ({}), externalAdminRequest: async () => owner,
    reportifyQrImageUrl: async (value) => reportifyQrDataUrl(value),
    jsonResponse: (_request, _env, status, data) => new Response(JSON.stringify(data), { status }),
    privateJsonResponse: (_request, _env, status, data) => new Response(JSON.stringify(data), { status }),
    fetch: async (url) => { requests.push(url); return new Response(JSON.stringify({ qrcode_id: "1234567890", qrcode_url: payload })); },
  };
  vm.createContext(context);
  vm.runInContext(["reportifyLoginQr", "handleReportifyLoginQr", "externalAccessFailure"].map((name) => fn(worker, name)).join("\n"), context);
  return { context, requests };
}

test("source login tickets become self-contained SVG without raw ticket markup or image-service requests", async () => {
  const h = workerHarness();
  const response = await h.context.handleReportifyLoginQr(new Request("https://worker.test/external/login-qr?qr_format=inline-v1"), {});
  assert.equal(response.status, 200);
  const data = await response.json();
  assert.deepEqual(Object.keys(data).sort(), ["qr_image_url", "qrcode_id"]);
  assert.match(data.qr_image_url, /^data:image\/svg\+xml;base64,/);
  const svg = Buffer.from(data.qr_image_url.split(",")[1], "base64").toString("utf8");
  assert.doesNotMatch(svg, /weixin|fixture|https?:\/\/(?!www\.w3\.org)|script|href|foreignObject/i);
  assert.deepEqual(h.requests, ["https://api.reportify.cn/auth/wechat/qrcode"]);
  assert.doesNotMatch(app, /api\.qrserver\.com|qrcode_url/);
});

test("legacy clients get an explicit refresh message before a login ticket is issued, including download recovery", async () => {
  const h = workerHarness();
  const request = new Request("https://worker.test/external/login-qr");
  for (const response of [await h.context.handleReportifyLoginQr(request, {}),
    await h.context.externalAccessFailure(request, {}, "1256239582803005440", "login_required", true)]) {
    assert.equal(response.status, 409);
    const data = await response.json();
    assert.equal(data.client_upgrade_required, true);
    assert.match(data.error, /刷新页面/);
    for (const field of ["qrcode_id", "qrcode_url", "qr_image_url", "token"]) assert.equal(data[field], undefined);
  }
  assert.equal(h.requests.length, 0);
  assert.doesNotMatch(worker, /reportifyLoginQr\(\)/);
});

test("only the owner gets QR payloads; malformed or oversized source payloads fail without returning them", async () => {
  const denied = workerHarness({ owner: false });
  assert.equal((await denied.context.handleReportifyLoginQr(new Request("https://worker.test/external/login-qr?qr_format=inline-v1"), {})).status, 403);
  assert.equal(denied.requests.length, 0);
  const prefix = "http://weixin.qq.com/q/";
  for (const value of ["https://evil.test/q/ticket", "https://weixin.qq.com.evil.test/q/ticket", "http://u:p@weixin.qq.com/q/ticket",
    "http:weixin.qq.com/q/ticket", "http:\\weixin.qq.com\\q\\ticket",
    `${ticket}?state=secret`, `${ticket}#fragment`, `${ticket}\n`, `${prefix}${"a".repeat(257-prefix.length)}`,
    `${prefix}${"票".repeat(100)}`]) {
    assert.throws(() => reportifyQrDataUrl(value), /^Error: Invalid login QR payload\.$/);
    const h = workerHarness({ payload: value });
    const response = await h.context.handleReportifyLoginQr(new Request("https://worker.test/external/login-qr?qr_format=inline-v1"), {});
    assert.equal(response.status, 503);
    assert.equal(JSON.stringify(await response.json()).includes(value), false);
  }
});

test("new frontend accepts only bounded embedded SVG and never falls back to a remote QR renderer", () => {
  for (const value of [reportifyQrDataUrl(ticket), "https://image.example.test/qr.png", "data:text/html;base64,PHN2Zy8+", "data:image/svg+xml;base64,%%%", `data:image/svg+xml;base64,${"A".repeat(80001)}`]) {
    let timerStarted = false;
    const target = { className: "", textContent: "", innerHTML: "" };
    const show = vm.runInNewContext(`(${fn(app, "showExternalLoginQr")})`, {
      escapeHtml: (text) => text, encodeURIComponent,
      window: { setInterval: () => { timerStarted = true; return 1; }, clearInterval() {} },
    });
    assert.equal(show(target, "https://worker.test", { login_required: true, qrcode_id: "1234567890", qr_image_url: value }, () => {}), true);
    if (value === reportifyQrDataUrl(ticket)) {
      assert.match(target.innerHTML, /src="data:image\/svg\+xml;base64,/);
      assert.equal(timerStarted, true);
    } else {
      assert.equal(target.innerHTML, "");
      assert.match(target.textContent, /刷新页面/);
      assert.equal(timerStarted, false);
    }
  }
  for (const name of ["initExternalSourceConnection", "fetchExternalPdf", "pollExternalDetail"]) {
    assert.match(fn(app, name), /qr_format=inline-v1/);
  }
});
