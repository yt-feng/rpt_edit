import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);
const termsPath = new URL("../site_src/terms.html", import.meta.url);
const privacyPath = new URL("../site_src/privacy.html", import.meta.url);
const [appSource, stylesSource, termsSource, privacySource] = await Promise.all([
  readFile(appPath, "utf8"),
  readFile(stylesPath, "utf8"),
  readFile(termsPath, "utf8"),
  readFile(privacyPath, "utf8"),
]);

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function element(overrides = {}) {
  const listeners = new Map();
  return {
    className: "",
    disabled: false,
    readOnly: false,
    textContent: "",
    value: "",
    focused: false,
    addEventListener(type, listener) { listeners.set(type, listener); },
    focus() { this.focused = true; },
    async submit() {
      const listener = listeners.get("submit");
      assert.ok(listener, "submit listener must be installed");
      await listener({ preventDefault() {} });
    },
    ...overrides,
  };
}

function createHarness(responseFactory, options = {}) {
  const elements = {
    reportRequestForm: element(),
    reportRequesterEmail: element({ value: "reader@example.com" }),
    reportRequestWebsite: element(),
    reportRequestSubmit: element({ textContent: "申请获取报告" }),
    reportRequestStatus: element(),
  };
  const calls = [];
  const tracked = [];
  const publicEmail = ["info", "@", "kc", "desk", ".com"].join("");
  const sandbox = {
    AUTHORITY_SOURCE: "authority",
    CONTACT_EMAIL: publicEmail,
    URLSearchParams,
    document: { getElementById(id) { return elements[id] || null; } },
    async fetch(url, init) {
      calls.push({ url: String(url), init });
      return responseFactory(String(url));
    },
    authHeaders() { return { Authorization: "Bearer member-token" }; },
    currentAnalyticsPath() { return "/doc.html"; },
    analyticsReportPayload(item, source) { return { report_id: item.id, source }; },
    trackEvent(workerUrl, type, data) { tracked.push({ workerUrl, type, data }); },
  };
  const initialize = vm.runInNewContext(`(${extractFunction(appSource, "initReportRequest")})`, sandbox);
  initialize("/api", {
    id: "report-a:0123456789abcdef",
    title: "Example report",
    source: "report-a",
    institution: "Example Bank",
    request_token: options.requestToken === undefined ? "signed-public-target" : options.requestToken,
  });
  return { calls, elements, tracked };
}

test("report request form promises a 24-hour response and keeps email as fallback", () => {
  assert.match(appSource, /提交后无需打开邮件客户端/u);
  assert.match(appSource, /24 小时内/u);
  assert.match(appSource, /id="reportRequestForm"/u);
  assert.match(appSource, /申请获取报告/u);
  assert.match(appSource, /accountEmail \? " readonly"/u);
  assert.match(appSource, /honeypot: website/u);
  assert.match(appSource, /initReportRequest\(workerUrl, item\)/u);
  assert.doesNotMatch(appSource, /id="authorityReportRequest"/u);
  assert.match(stylesSource, /\.report-request-fields\s*\{/u);
  assert.match(stylesSource, /\.report-request-trap\s*\{/u);
  assert.match(termsSource, /normally reviewed within 24 hours/u);
  assert.match(privacySource, /A report request may include/u);
  assert.match(privacySource, /email-delivery providers such as Cloudflare, GitHub, Brevo/u);
});

test("report request posts only report and requester fields, then confirms success", async () => {
  const harness = createHarness(() => ({
    ok: true,
    async json() {
      return { ok: true, detail: "申请已提交。我们会在24小时内通过邮箱回复。", deduplicated: false };
    },
  }));

  await harness.elements.reportRequestForm.submit();

  assert.equal(harness.calls.length, 1);
  assert.equal(harness.calls[0].url, "/api/report-request");
  assert.equal(harness.calls[0].init.headers.Authorization, "Bearer member-token");
  const body = JSON.parse(harness.calls[0].init.body);
  assert.deepEqual(Object.keys(body).sort(), [
    "honeypot", "institution", "page_path", "report_id", "request_token", "requester_email", "source", "title",
  ]);
  assert.equal(body.requester_email, "reader@example.com");
  assert.equal(body.request_token, "signed-public-target");
  assert.equal(body.page_path, "/doc.html");
  assert.equal(harness.elements.reportRequesterEmail.readOnly, true);
  assert.equal(harness.elements.reportRequestSubmit.disabled, true);
  assert.equal(harness.elements.reportRequestSubmit.textContent, "申请已提交");
  assert.match(harness.elements.reportRequestStatus.className, /\bok\b/u);
  assert.deepEqual(harness.tracked.map((entry) => [entry.type, entry.data.action]), [["report_request", "submitted"]]);
});

test("report request remains retryable when automatic delivery fails", async () => {
  const harness = createHarness(() => ({
    ok: false,
    async json() { return { detail: "自动提交暂时未完成，请稍后再试。" }; },
  }));

  await harness.elements.reportRequestForm.submit();

  assert.equal(harness.elements.reportRequestSubmit.disabled, false);
  assert.equal(harness.elements.reportRequestSubmit.textContent, "重新提交申请");
  assert.match(harness.elements.reportRequestStatus.className, /\berror\b/u);
  assert.match(harness.elements.reportRequestStatus.textContent, /稍后再试/u);
  assert.equal(harness.tracked.length, 0);
});

test("a contact report refreshes a missing request token before sending the real application", async () => {
  const harness = createHarness((url) => {
    if (url.startsWith("/api/contact-report/item?")) {
      return {
        ok: true,
        async json() { return { item: { request_token: "fresh-signed-target" } }; },
      };
    }
    return {
      ok: true,
      async json() { return { ok: true, detail: "申请已提交。", deduplicated: false }; },
    };
  }, { requestToken: "" });

  await harness.elements.reportRequestForm.submit();

  assert.equal(harness.calls.length, 2);
  assert.match(harness.calls[0].url, /^\/api\/contact-report\/item\?/u);
  assert.equal(harness.calls[1].url, "/api/report-request");
  assert.equal(JSON.parse(harness.calls[1].init.body).request_token, "fresh-signed-target");
});
