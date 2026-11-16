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
function element(hiddenAncestor = false) {
  return { hidden: false, isConnected: true, dataset: {}, textContent: "", listeners: {},
    closest: () => hiddenAncestor ? { hidden: true } : null,
    addEventListener(type, callback) { this.listeners[type] = callback; } };
}

test("account download recovery renders its QR in the visible account status, never the hidden password form", async () => {
  const ids = Object.fromEntries(["accountAccess", "openAccountPanel", "accountDownloadReport", "accountAccessHint", "accountAccessStatus", "externalDetailForm", "externalDetail"]
    .map((id) => [id, element()]));
  ids.externalDetailStatus = element(true);
  const shown = [];
  const context = {
    HOT_REPORT_SOURCE: "hot", EXTERNAL_SOURCE: "external", isContactOnlyItem: () => false,
    document: { getElementById: (id) => ids[id] || null, addEventListener() {} },
    isSuperSession: () => true, loadAuthSession: () => ({ token: "owner" }),
    waitForAuthSessionRefresh: async () => {}, authSessionRequestKey: () => "owner", authUserLabel: () => "owner",
    requestKindForVisibleMessage: () => "", setLineStatus: (target, text) => { target.textContent = text; },
    fetchReportAccess: async () => ({ can_download: true }), accountRightSummary: () => "",
    showExternalLoginQr: (target) => { shown.push(target); return true; },
  };
  vm.createContext(context);
  vm.runInContext(fn("initReportAccessControls"), context);
  context.initReportAccessControls({ id: "1256239582803005440", source: "external" }, "/api", "external", async () => {
    throw Object.assign(new Error("需要连接来源账号"), { login_required: true, qrcode_id: "test-qr" });
  });
  await new Promise(setImmediate);
  await ids.accountDownloadReport.listeners.click();
  assert.equal(ids.externalDetailForm.hidden, true);
  assert.equal(shown.length, 1);
  assert.equal(shown[0], ids.accountAccessStatus);
  assert.equal(shown[0].closest("[hidden]"), null);
  assert.equal(ids.accountDownloadReport.disabled, false);
});

test("pending and ready-download recovery choose a visible status and respect the delivery flow anchor", async () => {
  for (const ready of [false, true]) {
    for (const delivery of [false, true]) {
      const accountStatus = element();
      const deliveryStatus = element(!delivery);
      const shown = [];
      let tick;
      const failure = { login_required: true, qrcode_id: "test-qr", message: "需要连接来源账号" };
      const context = {
        Date, encodeURIComponent,
        window: { setInterval: (callback) => { tick = callback; return 1; }, clearInterval() {} },
        authHeaders: () => ({}),
        fetch: async () => ({ json: async () => ready ? { ready: true } : { status: "failed", ...failure } }),
        document: { getElementById: (id) => id === "accountAccessStatus" ? accountStatus : deliveryStatus },
        showExternalLoginQr: (target) => { shown.push(target); return true; },
      };
      vm.createContext(context);
      vm.runInContext(`${fn("externalPreparationMessage")}\n${fn("pollExternalDetail")}`, context);
      context.pollExternalDetail("/api", "1256239582803005440", delivery ? "delivery-password" : "", () => {},
        async () => { throw failure; }, null, deliveryStatus);
      await tick();
      assert.equal(shown.length, 1);
      assert.equal(shown[0], delivery ? deliveryStatus : accountStatus);
      assert.equal(shown[0].closest("[hidden]"), null);
    }
  }
});

test("account polling passes its own status anchor and delivery polling passes its form status", async () => {
  const accountStatus = element();
  let pollArgs;
  const download = vm.runInNewContext(`(${fn("downloadExternalWithAccount")})`, {
    fetchExternalPdf: async () => ({ pending: true }),
    document: { getElementById: () => accountStatus },
    pollExternalDetail: (...args) => { pollArgs = args; },
  });
  await download("/api", { id: "1256239582803005440" }, () => {});
  assert.equal(pollArgs[6], accountStatus);
  assert.match(fn("initExternalDetail"), /pollExternalDetail\(workerUrl, item\.id, input\.value,[\s\S]*?\), status\);/);
});

test("preparation failure polling stops and displays the server diagnosis and retry delay without account recovery", async () => {
  let tick;
  let stopped = false;
  let downloaded = false;
  let requested = false;
  const statuses = [];
  const context = {
    Date, encodeURIComponent,
    window: { setInterval: (callback) => { tick = callback; return 1; }, clearInterval: () => { stopped = true; } },
    authHeaders: () => ({}),
    fetch: async () => ({ json: async () => ({
      ready: false, status: "failed", error_code: "upstream_unavailable", detail_code: "invalid_asset_url",
      message: "上游文件地址暂不兼容，完整 PDF 尚未生成。", retry_after_seconds: 121, request_required: false,
    }) }),
    document: { getElementById: () => element() },
    showExternalLoginQr: (_target, _worker, failure) => {
      assert.equal(Boolean(failure.login_required || failure.reauth_available), false);
      return false;
    },
  };
  vm.createContext(context);
  vm.runInContext(`${fn("externalPreparationMessage")}\n${fn("pollExternalDetail")}`, context);
  context.pollExternalDetail("/api", "1300546606747226112", "", (message, kind) => statuses.push({ message, kind }),
    () => { downloaded = true; }, () => { requested = true; });
  await tick();
  assert.equal(stopped, true);
  assert.equal(downloaded, false);
  assert.equal(requested, false);
  assert.deepEqual(statuses.at(-1), {
    message: "上游文件地址暂不兼容，完整 PDF 尚未生成。 121 秒后可重试。", kind: "error",
  });
});

test("direct preparation rejection includes a bounded retry delay in the displayed download error", async () => {
  const context = vm.createContext({
    EXTERNAL_SOURCE: "external", URLSearchParams,
    isContactOnlyItem: () => false, docEndpoint: () => "external", authHeaders: () => ({}),
    trackEvent() {}, analyticsReportPayload: () => ({}), downloadErrorMessage: (_status, message) => message,
    fetch: async () => ({ ok: false, status: 503, json: async () => ({
      error: "完整文件暂未生成。", error_code: "upstream_unavailable", retry_after_seconds: 25,
    }) }),
  });
  vm.runInContext(`${fn("externalPreparationMessage")}\n${fn("fetchExternalPdf")}`, context);
  await assert.rejects(context.fetchExternalPdf("/api", { id: "1300546606747226112", source: "external" }, "", () => {}, { auth: true }),
    /完整文件暂未生成。 25 秒后可重试。/);
  for (const retry_after_seconds of [undefined, 0, -1, 601, Infinity, "bad"]) {
    assert.equal(context.externalPreparationMessage("请重新点击下载。", { retry_after_seconds }), "请重新点击下载。");
  }
});
