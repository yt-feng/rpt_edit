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
  const accessItems = [];
  const elements = new Map([
    ["reportRequestForm", control()],
    ["reportRequesterEmail", control("reader@example.com")],
    ["reportRequestWebsite", control()],
    ["reportRequestSubmit", control("申请获取报告")],
    ["reportRequestStatus", control()],
    ["externalDetail", { innerHTML: "" }],
  ]);
  const context = vm.createContext({
    URL,
    URLSearchParams,
    DOC_ITEM_CACHE_KEY: "portal_doc_item_cache_v2",
    LEGACY_SOURCE_WORDS: [["report", "ify"], ["nash", "ai"]],
    LEGACY_SOURCE_DOMAIN_WORDS: [
      ["report", "ify", "cn"],
      ["nash", "ai", "cn"],
      ["hi", "bor", "com", "cn"],
    ],
    LEGACY_CONTACT_WORDS: [
      ["macro", "gate"],
      ["support", "contact"],
      ["portal", "suite"],
      ["portal", "娱乐"],
      ["kc", "desk", "notes"],
      ["two", "tigers"],
    ],
    EXTERNAL_SOURCE: "external",
    AUTHORITY_SOURCE: "authority",
    REPORT_A_SOURCE: "report-a",
    THINKTANK_SOURCE: "thinktank",
    HOT_REPORT_SOURCE: "hot",
    PUBLIC_BRAND: "KC桌面",
    CONTENT_LOCALE: "zh-Hans",
    CONTACT_EMAIL: "support@portal.example.invalid",
    window: {
      location: { href: `https://portal.example.invalid/doc.html?${options.pageParams || ""}`, search: `?${options.pageParams || ""}`, hash: "" },
      history: { replaceState() {} },
    },
    localStorage: {
      getItem(key) { return storage.has(key) ? storage.get(key) : null; },
      setItem(key, value) { storage.set(key, String(value)); },
    },
    document: { getElementById(id) { return elements.get(id) || null; } },
    isAuthorityItem(item) { return item && item.source === "authority"; },
    isReportAItem(item) { return item && item.source === "report-a"; },
    isHotReportItem(item) { return item && item.source === "hot"; },
    isThinkTankItem(item) { return item && item.source === "thinktank"; },
    validDocId(item) {
      return item && (/^report-a:[A-Za-z0-9_-]{1,180}$/u.test(item.id)
        || /^(?:foreign|foreign-rt):[0-9]{1,25}$/u.test(item.id)
        || /^[0-9]{6,25}$/u.test(item.id)
        || /^hot:[a-f0-9]{16}$/u.test(item.id));
    },
    loadAuthSession() { return null; },
    authHeaders() { return { Authorization: "Bearer member" }; },
    currentAnalyticsPath() { return "/doc.html"; },
    analyticsReportPayload() { return {}; },
    trackEvent() {},
    escapeHtml(value) { return String(value || "").replaceAll("<", "&lt;"); },
    field(label, value) { return `<div>${label}: ${value}</div>`; },
    formatSize(value) { return `${value} B`; },
    async loadOptionalJson(_path, fallback) { return fallback; },
    workerBaseUrl() { return "/api"; },
    initAccountGate() {},
    initAdminGate() {},
    initNewsfeedNav() {},
    deliveryPasswordFromLocation() { return ""; },
    shouldDeferLocalizedHomeCatalog() { return true; },
    initExternalRelated() {},
    externalRelatedMarkup() { return ""; },
    accountAccessMarkup() { return '<div class="account-access">Member download</div>'; },
    initReportAccessControls(item) { accessItems.push(item); },
    triggerBlobDownload() {},
    rememberDeliveryPassword() {},
    async fetch(url, init = {}) {
      calls.push({ url: String(url), init });
      if (String(url).includes("/contact-report/pdf?")) {
        return { ok: true, status: 200, headers: { get() { return ""; } }, async blob() { return new Blob(["%PDF-1.7"]); } };
      }
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
    ${extractFunction(appSource, "legacyBrandPattern")}
    ${extractFunction(appSource, "publicBrandInput")}
    ${extractFunction(appSource, "publicBrandText")}
    ${extractFunction(appSource, "publicDocItem")}
    ${extractFunction(appSource, "publicSearchItem")}
    ${extractFunction(appSource, "isContactOnlyItem")}
    ${extractFunction(appSource, "docSourceLabel")}
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
    ${extractFunction(appSource, "reportRequestMarkup")}
    ${extractFunction(appSource, "renderExternalDetailFirstPaint")}
    ${extractAsyncFunction(appSource, "initExternalDetail")}
    ${extractAsyncFunction(appSource, "fetchExternalPdf")}
    globalThis.runtime = {
      remember: rememberDocItem,
      cached: cachedDocItem,
      buildUrl: externalPageUrl,
      fromParams: externalItemFromParams,
      fetchDetail: fetchDocDetailItem,
      initRequest: initReportRequest,
      requestTitle: reportRequestTitle,
      sanitizeText: publicBrandText,
      sanitizeSearchItem: publicSearchItem,
      isContactOnly: isContactOnlyItem,
      renderDetail: initExternalDetail,
      downloadPdf: fetchExternalPdf,
    };
  `, context);
  return { calls, accessItems, context, elements, runtime: context.runtime };
}

test("public metadata sanitizer removes legacy platform labels without altering the HIBOR rate name", () => {
  const { runtime } = createRuntime({});
  const legacyReportSource = ["report", "ify"].join("");
  const legacyContact = ["macro", "gate"].join("");
  const legacyDomain = [["hi", "bor"].join(""), "com", "cn"].join(".");
  assert.equal(runtime.sanitizeText(`${legacyReportSource}: Global Markets`), "Global Markets");
  assert.equal(runtime.sanitizeText(`${legacyContact} / Research Desk`), "Research Desk");
  assert.equal(runtime.sanitizeText(`mirror ${legacyDomain}`), "mirror");
  assert.equal(runtime.sanitizeText(`From ${legacyDomain} · Rates Outlook`), "Rates Outlook");
  assert.equal(runtime.sanitizeText("HIBOR rates outlook"), "HIBOR rates outlook");
  assert.equal(runtime.sanitizeText(["nash", "\u200b", "ai", ": Cloud Outlook"].join("")), "Cloud Outlook");
  assert.equal(runtime.sanitizeText("Ｎａｓｈ ＡＩ：Cloud Outlook"), "Cloud Outlook");

  const sanitized = runtime.sanitizeSearchItem({
    title: `${legacyReportSource} Technology Outlook`,
    institution: "",
    channel_name: legacyReportSource,
  }, "external");
  assert.equal(sanitized.title, "Technology Outlook");
  assert.equal(sanitized.institution, "");
  assert.equal(Object.hasOwn(sanitized, "channel_name"), false);
});

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

test("legacy source branding is removed from API, cache, and shareable detail URLs", async () => {
  const legacySource = ["nash", "ai"].join("");
  const cleanTitle = "AI Infrastructure and Enterprise Adoption Outlook";
  const item = {
    id: "foreign:260827001",
    source: "authority",
    title: `${legacySource}: ${cleanTitle}`,
    institution: legacySource,
    date: "2026-08-27",
    kind: "foreign",
    kind_label: "普通外文",
    page_count: 18,
    request_token: "signed-legacy-source-target",
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
  assert.equal(detailItem.title, cleanTitle);
  assert.equal(detailItem.institution || "", "");
  assert.equal(detailItem.date, "2026-08-27");
  assert.equal(detailItem.page_count, "18");

  const canonical = new URL(runtime.buildUrl(detailItem, "", { compact: true }));
  assert.equal(canonical.searchParams.get("title"), cleanTitle);
  assert.equal(canonical.searchParams.has("institution"), false);
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

test("an id-only external report loads verified title metadata and submits through the contact request flow", async () => {
  const id = "1295384700889731072";
  const title = "China's Next Industrial Revolution";
  const { calls, elements, runtime } = createRuntime({
    id, source: "external", title, institution: "Research House", date: "2026-09-10",
    available: false, availability: "contact_only", request_token: "external-signed-target",
  });
  const item = runtime.fromParams(new URLSearchParams({ id }));
  assert.equal(runtime.isContactOnly(item), true);
  const detail = await runtime.fetchDetail("/api", item);
  assert.equal(detail.title, title);
  assert.match(calls[0].url, /^\/api\/contact-report\/item\?/u);
  assert.equal(new URL(calls[0].url, "https://portal.example.invalid").searchParams.get("source"), "external");
  assert.equal(new URL(runtime.buildUrl(detail, "")).searchParams.get("rt"), "external-signed-target");
  runtime.initRequest("/api", detail);
  await elements.get("reportRequestForm").submit();
  const posted = JSON.parse(calls.find((call) => call.url === "/api/report-request").init.body);
  assert.equal(posted.report_id, id);
  assert.equal(posted.source, "external");
  assert.equal(posted.title, title);
  assert.equal(posted.request_token, "external-signed-target");
  assert.equal(calls.some((call) => /\/(?:pdf|status)(?:\?|$)/u.test(call.url)), false);
});

test("a retained hot report submits the canonical external request while preserving its hot archive URL", async () => {
  const { calls, elements, runtime } = createRuntime({});
  const hot = {
    id: "hot:0123456789abcdef", source: "hot", title: "Archived industrial report",
    origin_source: "external", origin_report_id: "1295384700889731072",
    request_source: "external", request_report_id: "1295384700889731072",
    request_token: "external-hot-signed-target", contact_only: true, available: false,
    description: "Obsolete generated cover summary",
  };
  const url = new URL(runtime.buildUrl(hot, ""));
  assert.equal(url.searchParams.get("id"), hot.id);
  assert.equal(url.searchParams.get("request_report_id"), hot.request_report_id);
  assert.equal(url.searchParams.has("description"), false);
  const detail = runtime.fromParams(url.searchParams);
  assert.equal(runtime.isContactOnly(detail), true);
  runtime.remember(detail);
  assert.equal(runtime.isContactOnly(runtime.cached(detail)), true);
  runtime.initRequest("/api", detail);
  await elements.get("reportRequestForm").submit();
  const posted = JSON.parse(calls.find((call) => call.url === "/api/report-request").init.body);
  assert.equal(posted.report_id, hot.request_report_id);
  assert.equal(posted.source, "external");
  assert.equal(posted.title, hot.title);
  assert.equal(posted.request_token, hot.request_token);
});

test("external title-only metadata discards stale summaries in search rows, cache, and shared URLs", () => {
  const { runtime } = createRuntime({});
  const item = {
    id: "1295384700889731072", title: "Industrial report", institution: "Research House",
    description: "Obsolete preview description", summary: "Obsolete summary",
  };
  const sanitized = runtime.sanitizeSearchItem(item, "external");
  assert.equal(sanitized.source, "external");
  assert.equal(Object.hasOwn(sanitized, "description"), false);
  assert.equal(Object.hasOwn(sanitized, "summary"), false);
  runtime.remember({ ...item, source: "external" });
  const cached = runtime.cached({ id: item.id, source: "external" });
  assert.equal(Object.hasOwn(cached, "description"), false);
  const url = new URL(runtime.buildUrl({ ...item, source: "external" }, ""));
  assert.equal(url.searchParams.has("description"), false);
  assert.equal(url.searchParams.get("title"), item.title);
});

test("external and historical hot details render a report application without PDF preparation or preview summaries", async () => {
  const originId = "1295384700889731072";
  for (const item of [
    { id: originId, source: "external" },
    { id: "hot:0123456789abcdef", source: "hot", origin_source: "external", request_source: "external", request_report_id: originId },
  ]) {
    const { calls, elements, runtime } = createRuntime({
      ...item, title: "China's Next Industrial Revolution", institution: "Research House", date: "2026-09-10",
      available: false, availability: "contact_only", request_token: "signed-external-target",
      description: "Cover-only preview summary",
    }, { pageParams: new URLSearchParams({ id: item.id }).toString() });
    await runtime.renderDetail();
    const html = elements.get("externalDetail").innerHTML;
    assert.match(html, /China's Next Industrial Revolution/u);
    assert.match(html, /仅提供报告标题/u);
    assert.match(html, /reportRequestForm/u);
    assert.match(html, /24 小时内/u);
    assert.doesNotMatch(html, /PDF Download|externalDetailForm|externalDetailWait|external-admin-tools|Cover-only preview summary/u);
    assert.equal(calls.some((call) => /\/(?:pdf|status)(?:\?|$)/u.test(call.url)), false);
    await elements.get("reportRequestForm").submit();
    const posted = JSON.parse(calls.find((call) => call.url === "/api/report-request").init.body);
    assert.equal(posted.source, "external");
    assert.equal(posted.report_id, originId);
  }
});

test("a fulfilled historical hot request uses the canonical external identity for member access and PDF delivery", async () => {
  const item = {
    id: "hot:0123456789abcdef", source: "hot", title: "Industrial report",
    origin_source: "external", request_source: "external", request_report_id: "1295384700889731072",
    available: true, availability: "available", size_bytes: 2000000,
  };
  const { calls, accessItems, elements, runtime } = createRuntime(item, { pageParams: new URLSearchParams({ id: item.id }).toString() });
  await runtime.renderDetail();
  assert.match(elements.get("externalDetail").innerHTML, /PDF 已补齐/u);
  assert.doesNotMatch(elements.get("externalDetail").innerHTML, /reportRequestForm|externalDetailForm/u);
  assert.equal(accessItems.length, 1);
  assert.equal(accessItems[0].source, "external");
  assert.equal(accessItems[0].id, item.request_report_id);
  await runtime.downloadPdf("/api", item, "", () => {}, { auth: true });
  const download = calls.find((call) => call.url.includes("/contact-report/pdf?"));
  const params = new URL(download.url, "https://portal.example.invalid").searchParams;
  assert.equal(params.get("source"), "external");
  assert.equal(params.get("id"), item.request_report_id);
  assert.equal(download.init.method, "GET");
});
