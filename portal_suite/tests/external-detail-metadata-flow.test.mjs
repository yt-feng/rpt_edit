import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const appSource = await readFile(appPath, "utf8");

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

function extractAsyncFunction(source, name) {
  const extracted = extractFunction(source, name);
  return `async ${extracted}`;
}

function control(value = "") {
  const listeners = new Map();
  return {
    value,
    disabled: false,
    readOnly: false,
    textContent: "",
    className: "",
    addEventListener(type, listener) { listeners.set(type, listener); },
    focus() {},
    async submit() {
      const listener = listeners.get("submit");
      assert.ok(listener, "report request submit listener must be installed");
      await listener({ preventDefault() {} });
    },
  };
}

function createRuntime(apiItem, options = {}) {
  const storage = new Map();
  const calls = [];
  const elements = new Map([
    ["reportRequestForm", control()],
    ["reportRequesterEmail", control("reader@example.com")],
    ["reportRequestWebsite", control()],
    ["reportRequestSubmit", control("申请获取报告")],
    ["reportRequestStatus", control()],
  ]);
  const context = vm.createContext({
    URL,
    URLSearchParams,
    DOC_ITEM_CACHE_KEY: "portal_doc_item_cache",
    EXTERNAL_SOURCE: "external",
    AUTHORITY_SOURCE: "authority",
    REPORT_A_SOURCE: "report-a",
    THINKTANK_SOURCE: "thinktank",
    HOT_REPORT_SOURCE: "hot",
    CONTACT_EMAIL: "support@portal.example.invalid",
    window: { location: { href: "https://portal.example.invalid/", search: "", hash: "" } },
    localStorage: {
      getItem(key) { return storage.has(key) ? storage.get(key) : null; },
      setItem(key, value) { storage.set(key, String(value)); },
    },
    document: { getElementById(id) { return elements.get(id) || null; } },
    isAuthorityItem(item) { return item && item.source === "authority"; },
    isReportAItem(item) { return item && item.source === "report-a"; },
    isHotReportItem(item) { return item && item.source === "hot"; },
    isThinkTankItem(item) { return item && item.source === "thinktank"; },
    isContactOnlyItem(item) { return item && ["authority", "report-a"].includes(item.source); },
    validDocId(item) {
      return item && (/^report-a:[A-Za-z0-9_-]{1,180}$/u.test(item.id)
        || /^(?:foreign|foreign-rt):[0-9]{1,25}$/u.test(item.id));
    },
    loadAuthSession() { return null; },
    authHeaders() { return { Authorization: "Bearer member" }; },
    currentAnalyticsPath() { return "/doc.html"; },
    analyticsReportPayload() { return {}; },
    trackEvent() {},
    async fetch(url, init = {}) {
      calls.push({ url: String(url), init });
      if (String(url).includes("/report-request")) {
        return {
          ok: true,
          status: 200,
          async json() { return { ok: true, detail: "申请已提交。", deduplicated: false }; },
        };
      }
      return {
        ok: options.contactItemOk !== false,
        status: options.contactItemOk === false ? 404 : 200,
        async json() { return { item: { ...apiItem } }; },
      };
    },
  });
  vm.runInContext(`
    ${extractFunction(appSource, "hasMeaningfulDocTitle")}
    ${extractFunction(appSource, "mergeDocItemMetadata")}
    ${extractFunction(appSource, "reportRequestTitle")}
    ${extractFunction(appSource, "docItemCacheKey")}
    ${extractFunction(appSource, "readDocItemCache")}
    ${extractFunction(appSource, "writeDocItemCache")}
    ${extractFunction(appSource, "rememberDocItem")}
    ${extractFunction(appSource, "cachedDocItem")}
    ${extractFunction(appSource, "externalPageUrl")}
    ${extractFunction(appSource, "externalItemFromParams")}
    ${extractAsyncFunction(appSource, "fetchDocDetailItem")}
    ${extractFunction(appSource, "initReportRequest")}
    globalThis.runtime = {
      remember: rememberDocItem,
      cached: cachedDocItem,
      buildUrl: externalPageUrl,
      fromParams: externalItemFromParams,
      fetchDetail: fetchDocDetailItem,
      initRequest: initReportRequest,
      requestTitle: reportRequestTitle,
    };
  `, context);
  return { calls, context, elements, runtime: context.runtime };
}

test("exact Report A result keeps its real title across params, stale cache, blank detail data, compact URL, and request POST", async () => {
  const id = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  const title = "申港证券-电子行业研究周报：MLCC开启新一轮涨价，关注订单溢出和国产替代-260802";
  const liveBlankItem = {
    id,
    source: "report-a",
    title: "",
    institution: "",
    date: "",
    filename: "",
    size_bytes: 0,
    available: false,
    availability: "contact_only",
    request_token: "",
  };
  const { calls, elements, runtime } = createRuntime(liveBlankItem);
  const searchItem = {
    id,
    source: "report-a",
    title,
    institution: "申港证券",
    date: "2026-08-06",
    category: "行业分析",
    author: "王伟",
    page_count: 10,
    request_token: "signed-report-a-target",
  };

  runtime.remember(searchItem);
  runtime.remember(liveBlankItem);
  assert.equal(runtime.cached(searchItem).title, title, "a blank response must not erase a cached search title");

  const resultUrl = new URL(runtime.buildUrl(searchItem, ""));
  assert.equal(resultUrl.searchParams.get("title"), title);
  const pageItem = runtime.fromParams(resultUrl.searchParams);
  const detailItem = await runtime.fetchDetail("/api", pageItem);
  assert.equal(detailItem.title, title);
  assert.equal(detailItem.institution, "申港证券");
  assert.equal(detailItem.date, "2026-08-06");
  assert.equal(detailItem.author, "王伟");
  assert.equal(detailItem.page_count, "10");
  assert.equal(detailItem.request_token, "signed-report-a-target");

  const compactUrl = new URL(runtime.buildUrl(detailItem, "", { compact: true }));
  assert.equal(compactUrl.searchParams.get("id"), id);
  assert.equal(compactUrl.searchParams.get("source"), "report-a");
  assert.equal(compactUrl.searchParams.get("title"), title);
  assert.equal(compactUrl.searchParams.get("institution"), "申港证券");
  assert.equal(compactUrl.searchParams.has("rt"), false, "verified compact URLs must not expose request proof");

  runtime.initRequest("/api", detailItem);
  await elements.get("reportRequestForm").submit();
  const requestCall = calls.find((call) => call.url === "/api/report-request");
  assert.ok(requestCall, "clicking the request button must issue the real POST");
  const body = JSON.parse(requestCall.init.body);
  assert.equal(body.report_id, id);
  assert.equal(body.title, title);
  assert.equal(body.institution, "申港证券");
  assert.equal(body.request_token, "signed-report-a-target");
  assert.match(elements.get("reportRequestStatus").className, /\bok\b/u);
});

test("NashAI authority metadata survives empty cache/API fields and remains in the shareable detail URL", async () => {
  const item = {
    id: "foreign:260827001",
    source: "authority",
    title: "NashAI: AI Infrastructure and Enterprise Adoption Outlook",
    institution: "NashAI",
    date: "2026-08-27",
    kind: "foreign",
    kind_label: "普通外文",
    page_count: 18,
    request_token: "signed-nashai-target",
  };
  const { runtime } = createRuntime({
    id: item.id,
    source: "authority",
    title: "Report",
    institution: "",
    date: "",
    page_count: "",
    availability: "contact_only",
  });

  runtime.remember(item);
  runtime.remember({ ...item, title: "", institution: "", date: "", page_count: "" });
  const pageItem = runtime.fromParams(new URL(runtime.buildUrl(item, "")).searchParams);
  const detailItem = await runtime.fetchDetail("/api", pageItem);
  assert.equal(detailItem.title, item.title);
  assert.equal(detailItem.institution, "NashAI");
  assert.equal(detailItem.date, "2026-08-27");
  assert.equal(detailItem.page_count, "18");

  const canonical = new URL(runtime.buildUrl(detailItem, "", { compact: true }));
  assert.equal(canonical.searchParams.get("title"), item.title);
  assert.equal(canonical.searchParams.get("institution"), "NashAI");
  assert.equal(canonical.searchParams.get("date"), "2026-08-27");
  assert.equal(canonical.searchParams.get("page_count"), "18");
});

test("an id-only contact page self-heals canonical metadata and proof before sending the application", async () => {
  const id = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  const title = "申港证券-电子行业研究周报：MLCC开启新一轮涨价，关注订单溢出和国产替代-260802";
  const { calls, elements, runtime } = createRuntime({
    id,
    source: "report-a",
    title,
    institution: "申港证券",
    date: "2026-08-06",
    request_token: "fresh-id-only-target",
    availability: "contact_only",
  });
  const idOnlyItem = runtime.fromParams(new URLSearchParams({ id }));
  runtime.initRequest("/api", idOnlyItem);
  await elements.get("reportRequestForm").submit();

  assert.equal(calls.filter((call) => call.url === "/api/report-request").length, 1);
  const request = calls.find((call) => call.url === "/api/report-request");
  const body = JSON.parse(request.init.body);
  assert.equal(body.title, title);
  assert.equal(body.report_id, id);
  assert.equal(body.institution, "申港证券");
  assert.equal(body.request_token, "fresh-id-only-target");
  assert.match(elements.get("reportRequestStatus").className, /\bok\b/u);
  assert.equal(elements.get("reportRequestSubmit").textContent, "申请已提交");
});

test("a failed canonical lookup says the application was not sent and never fakes a successful POST", async () => {
  const id = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  const { calls, elements, runtime } = createRuntime({ id, source: "report-a" }, { contactItemOk: false });
  const idOnlyItem = runtime.fromParams(new URLSearchParams({ id }));
  runtime.initRequest("/api", idOnlyItem);
  await elements.get("reportRequestForm").submit();

  assert.equal(calls.filter((call) => call.url === "/api/report-request").length, 0);
  assert.match(elements.get("reportRequestStatus").textContent, /本次申请尚未发送/u);
  assert.match(elements.get("reportRequestStatus").className, /\berror\b/u);
  assert.equal(elements.get("reportRequestSubmit").disabled, false);
});
