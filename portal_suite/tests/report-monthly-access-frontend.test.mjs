import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");

function extractFunction(name) {
  const start = app.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = app.indexOf("{", app.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < app.length; index += 1) {
    if (app[index] === "{") depth += 1;
    else if (app[index] === "}" && --depth === 0) return app.slice(start, index + 1);
  }
  throw new Error(`${name} body is incomplete`);
}

function control() {
  const listeners = new Map();
  return {
    hidden: false,
    disabled: false,
    isConnected: true,
    textContent: "",
    innerHTML: "",
    dataset: {},
    addEventListener(name, listener) { listeners.set(name, listener); },
    async click() { await listeners.get("click")?.(); },
  };
}

async function accessControls(source, { signedIn = true, canDownload = true } = {}) {
  const elements = new Map([
    "accountAccess", "openAccountPanel", "accountDownloadReport", "accountAccessHint",
    "accountAccessStatus", "externalDetailForm",
  ].map((id) => [id, control()]));
  const session = signedIn ? { token: "monthly-member", user: { id: "monthly-member" } } : null;
  let downloadCount = 0;
  const context = vm.createContext({
    HOT_REPORT_SOURCE: "hot",
    EXTERNAL_SOURCE: "external",
    document: {
      getElementById(id) { return elements.get(id) || null; },
      addEventListener() {},
    },
    isContactOnlyItem(item) { return ["authority", "report-a"].includes(item.source); },
    async waitForAuthSessionRefresh() {},
    loadAuthSession() { return session; },
    authSessionRequestKey() { return session?.token || ""; },
    authUserLabel() { return "monthly-member"; },
    isSuperSession() { return false; },
    async fetchReportAccess() {
      return { can_download: canDownload, effective_access: { active: true, duration_value: "1" } };
    },
    accountRightSummary() { return "1个月全站权限"; },
    accessContactGuidanceHtml() { return "申请开通"; },
    setLineStatus(target, text) { target.textContent = text; },
    setLineHtmlStatus(target, html) { target.innerHTML = html; },
    requestKindForVisibleMessage() { return ""; },
    showAccountModal() {},
    async download() { downloadCount += 1; },
  });
  vm.runInContext(`${extractFunction("initReportAccessControls")};
    initReportAccessControls({ id: "hot:6cc4a2ac5d5b266e", source: ${JSON.stringify(source)}, required_plan: "3个月会员" }, "/api", ${JSON.stringify(source)}, download);
  `, context);
  await new Promise((resolve) => setImmediate(resolve));
  return { elements, downloadCount: () => downloadCount };
}

test("old hot and contact report URLs use the current one-month full-site label", () => {
  const context = vm.createContext({
    URL,
    URLSearchParams,
    AUTHORITY_SOURCE: "authority",
    REPORT_A_SOURCE: "report-a",
    THINKTANK_SOURCE: "thinktank",
    HOT_REPORT_SOURCE: "hot",
    EXTERNAL_SOURCE: "external",
    publicDocItem(item) { return item; },
    window: { location: { href: "https://kcdesk.com/doc.html" } },
  });
  vm.runInContext(`${extractFunction("externalItemFromParams")}
    ${extractFunction("externalPageUrl")}
    globalThis.fromParams = externalItemFromParams;
    globalThis.buildUrl = externalPageUrl;
  `, context);
  for (const [source, id] of [["hot", "hot:6cc4a2ac5d5b266e"], ["authority", "foreign:123"], ["report-a", "report-a:123"]]) {
    const oldItem = { source, id, required_plan: "3个月会员" };
    const item = context.fromParams(new URLSearchParams(oldItem));
    assert.equal(item.required_plan, "1个月及以上全站会员");
    const sharedUrl = new URL(context.buildUrl(oldItem, ""));
    assert.equal(sharedUrl.searchParams.get("required_plan"), "1个月及以上全站会员");
  }
  const ordinary = context.fromParams(new URLSearchParams({ source: "external", id: "123456", required_plan: "annual" }));
  assert.equal(ordinary.required_plan, "annual");
});

for (const source of ["hot", "authority", "report-a"]) {
  test(`${source} monthly full-site grant exposes account download despite legacy URL metadata`, async () => {
    const runtime = await accessControls(source);
    assert.equal(runtime.elements.get("accountDownloadReport").hidden, false);
    assert.equal(runtime.elements.get("externalDetailForm").hidden, true);
    assert.match(runtime.elements.get("accountAccessHint").textContent, /已开通此报告下载权限/u);
    await runtime.elements.get("accountDownloadReport").click();
    assert.equal(runtime.downloadCount(), 1);
  });
}

test("signed-out and denied report controls describe effective one-month full-site membership", async () => {
  const signedOut = await accessControls("hot", { signedIn: false });
  assert.match(signedOut.elements.get("accountAccessHint").innerHTML, /有效的 1 个月及以上全站会员/u);
  assert.equal(signedOut.elements.get("accountDownloadReport").hidden, true);
  const denied = await accessControls("report-a", { canDownload: false });
  assert.equal(denied.elements.get("accountDownloadReport").hidden, true);
  assert.match(denied.elements.get("accountAccessStatus").innerHTML, /有效的 1 个月及以上全站会员/u);
  assert.doesNotMatch(denied.elements.get("accountAccessStatus").innerHTML, /3 个月/u);
});

test("updated application corrects legacy home markup during initialization", () => {
  const hint = { textContent: "精选近期热门 PDF；3个月及以上会员可下载全文。" };
  const update = vm.runInNewContext(`(${extractFunction("updateHotReportMembershipHint")})`);
  update({ querySelector(selector) { assert.equal(selector, ".external-hint"); return hint; } });
  assert.equal(hint.textContent, "精选近期热门 PDF；1个月及以上全站会员可下载全文。");
  assert.doesNotThrow(() => update(null));
  assert.match(app, /const hotReportsSection = document\.getElementById\("hotReportsSection"\);\s+updateHotReportMembershipHint\(hotReportsSection\)/u);
});
