import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = (await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8")).replace(/^  /gm, "");
function fn(name) {
  const start = new RegExp(`^(?:async )?function ${name}\\(`, "m").exec(app);
  assert.ok(start, `missing ${name}`);
  const rest = app.slice(start.index);
  const next = /\n(?:async )?function \w+\(/.exec(rest);
  return next ? rest.slice(0, next.index) : rest;
}
function node() {
  return { hidden: false, disabled: false, textContent: "", innerHTML: "", className: "", dataset: {},
    listeners: {}, addEventListener(type, callback) { this.listeners[type] = callback; } };
}
const flush = () => new Promise((resolve) => setImmediate(resolve));

test("QR phone-binding and timeout states stop polling with actionable messages", async () => {
  for (const status of ["bind_phone", "waiting"]) {
    let tick;
    let cleared = false;
    let ready = false;
    const context = {
      encodeURIComponent, escapeHtml: (value) => value, authHeaders: () => ({}),
      window: { setInterval: (callback) => { tick = callback; return 7; }, clearInterval: () => { cleared = true; } },
      fetch: async () => ({ ok: true, json: async () => ({ ready: false, status }) }),
    };
    vm.createContext(context);
    vm.runInContext(fn("showExternalLoginQr"), context);
    const target = node();
    context.showExternalLoginQr(target, "https://worker.example.test", {
      login_required: true, qrcode_id: "123456789", qr_image_url: "data:image/svg+xml;base64,PHN2Zy8+",
    }, () => { ready = true; });
    for (let count = 0; count < (status === "waiting" ? 91 : 1); count += 1) await tick();
    assert.equal(cleared, true);
    assert.equal(ready, false);
    assert.equal(target.__externalQrTimer, null);
    assert.match(target.textContent, status === "waiting" ? /二维码已超时/ : /手机号绑定/);
  }
});

function connectionHarness({ owner = true, connected = false, statusFailure = false } = {}) {
  const ids = Object.fromEntries(["accountAdminSourceState", "accountAdminSourceQr", "accountAdminSourceConnect", "accountAdminSourceRefresh"].map((id) => [id, node()]));
  const section = { querySelector: (selector) => ids[selector.slice(1)] };
  const modal = { querySelector: () => section };
  const calls = [];
  let currentConnected = connected;
  let qrOptions;
  let onSaved;
  let cleared;
  const context = {
    isSuperSession: () => owner, authHeaders: () => ({ Authorization: "Bearer owner-session" }),
    formatAdminDateTime: (value) => `date:${value}`,
    window: { clearInterval: (id) => { cleared = id; } },
    fetch: async (url, options) => {
      calls.push({ url, options });
      if (url.endsWith("/external/login-qr?qr_format=inline-v1")) return { ok: true, json: async () => ({ qrcode_id: "123456789", qr_image_url: "data:image/svg+xml;base64,PHN2Zy8+" }) };
      return { ok: !statusFailure, json: async () => statusFailure ? { error: "readback failed" }
        : { connected: currentConnected, updated_at: "2026-09-17T01:00:00Z", expires_at: "2026-09-17T13:00:00Z" } };
    },
    showExternalLoginQr: (target, _url, data, callback, options) => {
      assert.equal(target, ids.accountAdminSourceQr);
      assert.equal(data.login_required, true);
      qrOptions = options;
      onSaved = callback;
      target.__externalQrTimer = 99;
      return true;
    },
  };
  vm.createContext(context);
  vm.runInContext(fn("initExternalSourceConnection"), context);
  const controller = context.initExternalSourceConnection("https://worker.example.test", modal);
  return { ids, calls, controller, setConnected: (value) => { currentConnected = value; }, saved: () => onSaved(), options: () => qrOptions, cleared: () => cleared };
}

test("source connection place is rendered only for the owner management view", () => {
  const markup = vm.runInNewContext(`(${fn("accountAdminModalMarkup")})`, { escapeHtml: (value) => String(value || "") });
  assert.match(markup({ showSourceConnection: true }), /报告来源连接/);
  assert.match(markup({ showSourceConnection: true }), /id="accountAdminSourceConnect"/);
  assert.doesNotMatch(markup({ showSourceConnection: false }), /accountAdminSourceConnection/);
  assert.match(fn("showAccountAdminModal"), /showSourceConnection:\s*isSuperSession\(session\)/);
});

test("non-owner view never reads a source session or creates a QR", async () => {
  const h = connectionHarness({ owner: false });
  await h.controller.refresh();
  assert.equal(h.calls.length, 0);
  assert.equal(h.ids.accountAdminSourceConnect.listeners.click, undefined);
});

test("owner connects through authenticated QR flow and confirms server connection readback", async () => {
  const h = connectionHarness();
  await flush();
  assert.match(h.ids.accountAdminSourceState.textContent, /尚未连接/);
  await h.ids.accountAdminSourceConnect.listeners.click();
  assert.match(h.options().prompt, /扫描二维码/);
  assert.match(h.options().completionMessage, /已保存/);
  h.setConnected(true);
  await h.saved();
  assert.match(h.ids.accountAdminSourceState.textContent, /来源连接已保存/);
  assert.match(h.ids.accountAdminSourceState.textContent, /仍需账号具备下载权益/);
  assert.match(h.ids.accountAdminSourceQr.textContent, /可返回报告页/);
  for (const call of h.calls) {
    assert.equal(call.options.headers.Authorization, "Bearer owner-session");
    assert.equal(call.options.cache, "no-store");
  }
  assert.equal(h.calls.some((call) => call.url.endsWith("/external/login-qr?qr_format=inline-v1")), true);
  h.controller.close();
  assert.equal(h.cleared(), 99);
});

test("unconfirmed connection is not presented as successful", async () => {
  const h = connectionHarness({ statusFailure: true });
  await flush();
  await h.ids.accountAdminSourceConnect.listeners.click();
  await assert.rejects(h.saved(), /来源连接尚未确认/);
  assert.equal(h.ids.accountAdminSourceState.className, "status-line error");
  assert.doesNotMatch(h.ids.accountAdminSourceQr.textContent, /来源连接已保存/);
});

function previewHarness({ mime = "image/jpeg", responseStatus = 200, decodeFailure = false,
  previewPages = "1", blobSize = 4096, pdfPages = 1, pdfWidth = 600, pdfHeight = 800,
  pdfParseFailure = false, pdfRenderFailure = false, pdfBlobFailure = false, canvasFailure = false } = {}) {
  const ids = Object.fromEntries(["externalPreviewOpen", "externalPreviewStatus", "externalPreviewFigure", "externalPreviewImage"].map((id) => [id, node()]));
  ids.externalPreviewImage.decode = async () => { if (decodeFailure) throw new Error("image decode failed"); };
  ids.externalPreviewFigure.hidden = true;
  const calls = [], created = [], revoked = [], pdfCalls = [], canvases = [];
  let blobReads = 0, pdfDestroyed = 0;
  const events = {};
  const context = {
    Uint8Array, encodeURIComponent, authHeaders: () => ({ Authorization: "Bearer member-session" }),
    window: { addEventListener: (name, callback) => { events[name] = callback; } },
    URL: { createObjectURL: (blob) => { created.push(blob); return `blob:preview-${created.length}`; }, revokeObjectURL: (url) => revoked.push(url) },
    document: { createElement: (tag) => {
      assert.equal(tag, "canvas");
      const canvas = { width: 0, height: 0, getContext: () => canvasFailure ? null : {},
        toBlob: (callback, type) => { assert.equal(type, "image/png"); callback(pdfBlobFailure ? null : { type, size: 2048 }); } };
      canvases.push(canvas);
      return canvas;
    } },
    loadPdfJs: async () => ({ getDocument: (options) => {
      pdfCalls.push({ kind: "document", options });
      return { destroy: async () => { pdfDestroyed += 1; }, promise: (async () => {
        if (pdfParseFailure) throw new Error("PDF parse failed");
        return { numPages: pdfPages, getPage: async (page) => {
          pdfCalls.push({ kind: "page", page });
          return { getViewport: ({ scale }) => ({ width: pdfWidth * scale, height: pdfHeight * scale }),
            render: (options) => {
              pdfCalls.push({ kind: "render", options, width: canvases.at(-1).width, height: canvases.at(-1).height });
              return { promise: pdfRenderFailure ? Promise.reject(new Error("PDF render failed")) : Promise.resolve() };
            } };
        } };
      })() };
    } }),
    fetch: async (url, options) => {
      calls.push({ url, options });
      return { ok: responseStatus === 200, status: responseStatus, json: async () => ({ error: "预览暂时不可用" }),
        headers: { get: (name) => name === "X-Portal-Preview-Pages" ? previewPages : null },
        blob: async () => { blobReads += 1; return { type: mime, size: blobSize, arrayBuffer: async () => new Uint8Array([37, 80, 68, 70]).buffer }; } };
    },
  };
  vm.createContext(context);
  vm.runInContext(fn("renderExternalSinglePagePreviewPdf"), context);
  vm.runInContext(fn("initExternalSinglePagePreview"), context);
  const section = { querySelector: (selector) => ids[selector.slice(1)] };
  context.initExternalSinglePagePreview("https://worker.example.test", { id: "1256239582803005440" }, { querySelector: () => section });
  return { ids, calls, created, revoked, events, pdfCalls, canvases, blobReads: () => blobReads, pdfDestroyed: () => pdfDestroyed };
}

test("single-page preview is labeled as partial and displayed as an authenticated image", async () => {
  const markup = vm.runInNewContext(`(${fn("externalSinglePagePreviewMarkup")})`)();
  assert.match(markup, /查看1页预览/);
  assert.match(markup, /非完整报告/);
  assert.doesNotMatch(markup, /Reportify|iframe|\.pdf/i);
  const h = previewHarness();
  await h.ids.externalPreviewOpen.listeners.click();
  assert.equal(h.calls.length, 1);
  assert.match(h.calls[0].url, /\/external\/preview\?id=1256239582803005440$/);
  assert.equal(h.calls[0].options.headers.Authorization, "Bearer member-session");
  assert.equal(h.ids.externalPreviewFigure.hidden, false);
  assert.equal(h.ids.externalPreviewImage.src, "blob:preview-1");
  assert.match(h.ids.externalPreviewStatus.textContent, /不是完整报告/);
  h.events.pagehide();
  assert.deepEqual(h.revoked, ["blob:preview-1"]);
});

test("preview refuses unsupported/error responses and never displays an undecodable image", async () => {
  for (const options of [{ mime: "text/html" }, { responseStatus: 401 }, { decodeFailure: true }, { blobSize: 0 }, { blobSize: 10 * 1024 * 1024 + 1 }]) {
    const h = previewHarness(options);
    await h.ids.externalPreviewOpen.listeners.click();
    assert.equal(h.ids.externalPreviewFigure.hidden, true);
    assert.equal(h.ids.externalPreviewStatus.className, "status-line error");
    assert.equal(h.ids.externalPreviewOpen.disabled, false);
    if (options.responseStatus === 401) assert.match(h.ids.externalPreviewStatus.textContent, /先登录/);
  }
});

test("image and PDF previews require the exact server one-page marker before reading their body", async () => {
  for (const mime of ["image/png", "application/pdf"]) {
    for (const previewPages of [null, "", "0", "2", "01", "1, 2"]) {
      const h = previewHarness({ mime, previewPages });
      await h.ids.externalPreviewOpen.listeners.click();
      assert.equal(h.ids.externalPreviewFigure.hidden, true);
      assert.equal(h.ids.externalPreviewStatus.className, "status-line error");
      assert.equal(h.blobReads(), 0);
      assert.equal(h.pdfCalls.length, 0);
      assert.equal(h.created.length, 0);
    }
  }
});

test("verified one-page PDF renders to a bounded PNG image and releases parser and canvas resources", async () => {
  for (const dimensions of [{ pdfWidth: 600, pdfHeight: 800 }, { pdfWidth: 90000, pdfHeight: 70000 }]) {
    const h = previewHarness({ mime: "application/pdf", ...dimensions });
    await h.ids.externalPreviewOpen.listeners.click();
    assert.equal(h.ids.externalPreviewFigure.hidden, false);
    assert.equal(h.created.length, 1);
    assert.equal(h.created[0].type, "image/png");
    assert.equal(h.pdfCalls[0].options.isEvalSupported, false);
    assert.equal(h.pdfCalls[0].options.maxImageSize, 16000000);
    assert.deepEqual(h.pdfCalls.filter((call) => call.kind === "page").map((call) => call.page), [1]);
    const rendered = h.pdfCalls.find((call) => call.kind === "render");
    assert.ok(rendered.width > 0 && rendered.width <= 1600);
    assert.ok(rendered.height > 0 && rendered.height <= 1600);
    assert.ok(rendered.width * rendered.height <= 2560000);
    assert.equal(h.pdfDestroyed(), 1);
    assert.equal(h.canvases[0].width, 0);
    assert.equal(h.canvases[0].height, 0);
    assert.match(h.ids.externalPreviewStatus.textContent, /不是完整报告/);
    await h.ids.externalPreviewOpen.listeners.click();
    assert.deepEqual(h.revoked, ["blob:preview-1"]);
    h.events.pagehide();
    assert.deepEqual(h.revoked, ["blob:preview-1", "blob:preview-2"]);
  }
});

test("PDF preview rejects multiple or unknown pages before requesting or rendering any page", async () => {
  for (const pdfPages of [0, 2, 57, undefined, "1"]) {
    const h = previewHarness({ mime: "application/pdf", pdfPages: pdfPages === undefined ? null : pdfPages });
    await h.ids.externalPreviewOpen.listeners.click();
    assert.equal(h.ids.externalPreviewFigure.hidden, true);
    assert.equal(h.ids.externalPreviewStatus.className, "status-line error");
    assert.equal(h.pdfCalls.filter((call) => call.kind !== "document").length, 0);
    assert.equal(h.created.length, 0);
    assert.equal(h.pdfDestroyed(), 1);
  }
});

test("PDF parse, invalid geometry, canvas, render and encoding failures release resources and allow retry", async () => {
  for (const options of [{ pdfParseFailure: true }, { pdfWidth: Infinity }, { pdfHeight: 0 },
    { canvasFailure: true }, { pdfRenderFailure: true }, { pdfBlobFailure: true }]) {
    const h = previewHarness({ mime: "application/pdf", ...options });
    await h.ids.externalPreviewOpen.listeners.click();
    assert.equal(h.ids.externalPreviewFigure.hidden, true);
    assert.equal(h.ids.externalPreviewStatus.className, "status-line error");
    assert.equal(h.ids.externalPreviewOpen.disabled, false);
    assert.equal(h.created.length, 0);
    assert.equal(h.pdfDestroyed(), 1);
    for (const canvas of h.canvases) assert.equal(canvas.width + canvas.height, 0);
  }
});

async function accessHarness({ source = "external", owner = false, explicitDelivery = false, downloadError = null, access = { can_download: true } } = {}) {
  const ids = Object.fromEntries(["accountAccess", "openAccountPanel", "accountDownloadReport", "accountAccessHint", "accountAccessStatus", "externalDetailForm"].map((id) => [id, node()]));
  ids.externalDetailForm.dataset.explicitDelivery = String(explicitDelivery);
  let entitlementReads = 0, downloads = 0;
  const previews = [];
  const session = { token: "account-token", user: { role: owner ? "super" : "user" } };
  const context = {
    HOT_REPORT_SOURCE: "hot", EXTERNAL_SOURCE: "external", isContactOnlyItem: () => false,
    document: { getElementById: (id) => ids[id] || null, addEventListener: () => {} },
    isSuperSession: () => owner, loadAuthSession: () => session,
    waitForAuthSessionRefresh: async () => {}, authSessionRequestKey: () => "session-key", authUserLabel: () => "current user",
    requestKindForVisibleMessage: () => "", setLineStatus: (target, text, kind) => { target.textContent = text; target.className = kind || ""; },
    setLineHtmlStatus: (target, html) => { target.innerHTML = html; },
    fetchReportAccess: async () => { entitlementReads += 1; return access; }, accountRightSummary: () => "current membership",
    showExternalPreviewOnlyFallback: (_target, _worker, _item, response) => previews.push(response),
  };
  vm.createContext(context);
  vm.runInContext(fn("initReportAccessControls"), context);
  context.initReportAccessControls({ id: "1256239582803005440", source }, "https://worker.example.test", source, async () => {
    downloads += 1;
    if (downloadError) throw downloadError;
  });
  await flush();
  return { ids, previews, entitlementReads: () => entitlementReads, downloads: () => downloads };
}

test("ordinary source-report members get preview only while owner and other report types keep full action", async () => {
  const member = await accessHarness();
  assert.equal(member.ids.accountDownloadReport.hidden, true);
  assert.equal(member.ids.externalDetailForm.hidden, true);
  assert.match(member.ids.accountAccessHint.textContent, /1页预览/);
  await member.ids.accountDownloadReport.listeners.click();
  assert.equal(member.downloads(), 0);
  assert.equal(member.entitlementReads(), 0);
  for (const options of [{ owner: true }, { source: "catalog" }, { source: "hot" }]) {
    const h = await accessHarness(options);
    assert.equal(h.ids.accountDownloadReport.hidden, false);
    await h.ids.accountDownloadReport.listeners.click();
    assert.equal(h.downloads(), 1);
  }
  const delivered = await accessHarness({ explicitDelivery: true });
  assert.equal(delivered.ids.externalDetailForm.hidden, false);
  assert.equal(delivered.ids.accountDownloadReport.hidden, true);
});

test("external-origin archived reports switch to a one-page preview after a source-policy denial", async () => {
  const response = { preview_only: true, preview_report_id: "1256239582803005440", message: "此类报告普通会员可查看1页预览。" };
  const h = await accessHarness({ source: "hot", downloadError: response });
  await h.ids.accountDownloadReport.listeners.click();
  assert.equal(h.ids.accountDownloadReport.hidden, true);
  assert.equal(h.ids.accountDownloadReport.disabled, false);
  assert.match(h.ids.accountAccessStatus.textContent, /预览不是完整报告/);
  assert.equal(h.previews[0].preview_report_id, "1256239582803005440");
  const access = await accessHarness({ source: "hot", access: { ...response, can_download: false, membership_months: 0 } });
  assert.equal(access.ids.accountDownloadReport.hidden, true);
  assert.match(access.ids.accountAccessHint.textContent, /1页预览/);
  assert.equal(access.previews[0].preview_report_id, "1256239582803005440");
});

test("archived preview uses only the original report id and does not create duplicate preview cards", () => {
  let existing = false;
  const inserted = [], initialized = [];
  const target = {
    querySelector: () => existing,
    insertAdjacentHTML: (position, markup) => { inserted.push({ position, markup }); existing = true; },
  };
  const helper = vm.runInNewContext(`(${fn("showExternalPreviewOnlyFallback")})`, {
    EXTERNAL_SOURCE: "external", externalSinglePagePreviewMarkup: () => "one-page markup",
    initExternalSinglePagePreview: (worker, item) => initialized.push({ worker, item }),
  });
  const item = { id: "hot:abcdefabcdef1234", source: "hot" };
  assert.equal(helper(target, "https://worker.example.test", item, { preview_only: true }), false);
  assert.equal(helper(target, "https://worker.example.test", item, { preview_only: true, preview_report_id: "1256239582803005440" }), true);
  assert.equal(helper(target, "https://worker.example.test", item, { preview_only: true, preview_report_id: "1256239582803005440" }), true);
  assert.equal(inserted.length, 1);
  assert.equal(initialized[0].item.id, "1256239582803005440");
});

test("PDF source-policy response retains the original preview id for the UI", async () => {
  const fetchPdf = vm.runInNewContext(`(${fn("fetchExternalPdf")})`, {
    EXTERNAL_SOURCE: "external", URLSearchParams,
    isContactOnlyItem: () => false, docEndpoint: () => "hot-reports", authHeaders: () => ({}),
    trackEvent: () => {}, analyticsReportPayload: () => ({}), downloadErrorMessage: (_status, message) => message,
    fetch: async () => ({ ok: false, status: 403, json: async () => ({
      error: "此类报告普通会员可查看1页预览。", error_code: "preview_only", preview_report_id: "1256239582803005440",
    }) }),
  });
  await assert.rejects(fetchPdf("https://worker.example.test", { id: "hot:abcdefabcdef1234", source: "hot" }, "", () => {}, { auth: true }), (error) => {
    assert.equal(error.preview_only, true);
    assert.equal(error.preview_report_id, "1256239582803005440");
    return true;
  });
});
