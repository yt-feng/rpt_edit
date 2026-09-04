import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const source = await readFile(path.join(root, "portal_suite/site_src/assets/report-chat.js"), "utf8");
const homeSource = await readFile(path.join(root, "portal_suite/site_src/index.html"), "utf8");
const stylesSource = await readFile(path.join(root, "portal_suite/site_src/assets/styles.css"), "utf8");

class FakeElement {
  constructor(id = "") {
    this.id = id;
    this.value = "";
    this.textContent = "";
    this.innerHTML = "";
    this.className = "";
    this.disabled = false;
    this.hidden = false;
    this.removed = false;
    this.style = {};
    this.attributes = new Map();
    this.listeners = new Map();
    this.childrenBySelector = new Map();
    this.submitButton = null;
    this.insertedElement = null;
    this.classList = {
      add: (value) => {
        const values = new Set(this.className.split(/\s+/u).filter(Boolean));
        values.add(value);
        this.className = [...values].join(" ");
      },
      remove: (value) => {
        this.className = this.className.split(/\s+/u).filter((item) => item && item !== value).join(" ");
      },
      contains: (value) => this.className.split(/\s+/u).includes(value),
    };
  }

  addEventListener(type, listener) {
    const values = this.listeners.get(type) || [];
    values.push(listener);
    this.listeners.set(type, values);
  }

  async dispatch(type, event = {}) {
    const normalized = { preventDefault() {}, target: this, ...event };
    return Promise.all((this.listeners.get(type) || []).map((listener) => listener(normalized)));
  }

  querySelector(selector) {
    if (selector === "button[type=submit]") return this.submitButton;
    if (!this.childrenBySelector.has(selector)) this.childrenBySelector.set(selector, new FakeElement(selector));
    return this.childrenBySelector.get(selector);
  }

  insertAdjacentElement(_position, element) {
    this.insertedElement = element;
    return element;
  }

  setAttribute(name, value) {
    this.attributes.set(name, String(value));
  }

  getAttribute(name) {
    return this.attributes.get(name) || null;
  }

  closest(selector) {
    if (selector.startsWith(".")) {
      return this.classList.contains(selector.slice(1)) ? this : null;
    }
    const attribute = selector.match(/^\[([^=\]]+)(?:=[^\]]+)?\]$/u);
    return attribute && this.attributes.has(attribute[1]) ? this : null;
  }

  remove() {
    this.removed = true;
  }
}

function createScheduler() {
  let nextId = 1;
  const timeouts = new Map();
  const intervals = new Map();
  return {
    setTimeout(callback, delay) {
      const id = nextId++;
      timeouts.set(id, { callback, delay });
      return id;
    },
    clearTimeout(id) { timeouts.delete(id); },
    setInterval(callback, delay) {
      const id = nextId++;
      intervals.set(id, { callback, delay });
      return id;
    },
    clearInterval(id) { intervals.delete(id); },
    runTimeout(delay) {
      const entry = [...timeouts.entries()].find(([, value]) => value.delay === delay);
      assert.ok(entry, `missing timeout scheduled for ${delay}ms`);
      timeouts.delete(entry[0]);
      entry[1].callback();
    },
  };
}

function createHarness({ authenticated = true, includePopular = false, contentLocale = "" } = {}) {
  const form = new FakeElement("homeChatForm");
  const button = new FakeElement("homeChatSubmit");
  button.textContent = "开始查找";
  form.submitButton = button;
  const input = new FakeElement("homeChatInput");
  input.value = "最近的 AI 数据中心报告";
  const status = new FakeElement("homeChatStatus");
  const messages = new FakeElement("homeChatMessages");
  const recommendations = new FakeElement("homeChatRecommendations");
  messages.innerHTML = "旧答案";
  recommendations.innerHTML = "旧推荐";
  const popular = includePopular ? new FakeElement("homeChatPopular") : null;
  const popularList = includePopular ? new FakeElement("homeChatPopularList") : null;
  if (popular) popular.hidden = true;
  const elements = {
    homeChatForm: form,
    homeChatInput: input,
    homeChatStatus: status,
    homeChatMessages: messages,
    homeChatRecommendations: recommendations,
    ...(popular ? { homeChatPopular: popular, homeChatPopularList: popularList } : {}),
  };
  const scheduler = createScheduler();
  const fetches = [];
  const fetch = (url, options = {}) => new Promise((resolve, reject) => {
    const request = {
      url,
      options,
      resolve(payload, init = {}) {
        resolve({ ok: init.ok !== false, status: init.status || 200, json: async () => payload });
      },
    };
    options.signal?.addEventListener("abort", () => reject(new DOMException("Aborted", "AbortError")), { once: true });
    fetches.push(request);
  });
  const document = {
    readyState: "complete",
    getElementById(id) { return elements[id] || null; },
    createElement() { return new FakeElement(); },
    addEventListener() {},
  };
  const window = {
    setTimeout: scheduler.setTimeout,
    clearTimeout: scheduler.clearTimeout,
    setInterval: scheduler.setInterval,
    clearInterval: scheduler.clearInterval,
    location: { pathname: "/" },
  };
  if (contentLocale) window.PortalLocale = { contentLocale };
  const analyticsEvents = [];
  const exportCalls = [];
  window.PortalSuiteAnalytics = {
    visitorId: () => "visitor-test-123",
    track(type, data) {
      analyticsEvents.push({ type, data });
      return Promise.resolve(true);
    },
  };
  window.PortalReportResearchExport = {
    async downloadDocx(payload) {
      exportCalls.push({ kind: "docx", payload });
      return { status: "downloaded" };
    },
    async openPdfPrint(payload) {
      exportCalls.push({ kind: "pdf", payload });
      return { status: "print_dialog_opened" };
    },
  };
  const localStorage = {
    getItem() {
      return authenticated
        ? JSON.stringify({ token: "session-token", user: { email: "reader@example.com" } })
        : null;
    },
  };
  vm.runInNewContext(source, {
    AbortController,
    Date,
    DOMException,
    Event,
    console,
    document,
    encodeURIComponent,
    fetch,
    localStorage,
    window,
  }, { filename: "report-chat.js" });
  return { analyticsEvents, button, exportCalls, fetches, form, input, messages, popular, popularList, recommendations, scheduler, status, window };
}

function analyticsActions(harness) {
  return harness.analyticsEvents.map((entry) => entry.data.action);
}

function assertAnalyticsHasNoQuestionText(harness, question) {
  for (const entry of harness.analyticsEvents) {
    assert.equal(entry.type, "report_chat_interaction");
    assert.doesNotMatch(JSON.stringify(entry.data), new RegExp(question.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "u"));
    assert.equal(Object.hasOwn(entry.data, "question"), false);
  }
}

test("report chat shows immediate staged feedback and atomically replaces old results on success", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");

  assert.equal(harness.fetches.length, 1);
  assert.equal(harness.fetches[0].url, "/api/report-chat");
  assert.equal(harness.fetches[0].options.headers.Authorization, "Bearer session-token");
  assert.equal(JSON.parse(harness.fetches[0].options.body).visitor_id, "visitor-test-123");
  assert.equal(harness.button.disabled, true);
  assert.equal(harness.button.textContent, "正在查找…");
  assert.equal(harness.form.getAttribute("aria-busy"), "true");
  assert.equal(harness.form.insertedElement.getAttribute("aria-live"), null);
  assert.match(source, /data-chat-progress-label role="status" aria-live="polite"/u);
  assert.match(source, /data-chat-progress-time aria-hidden="true"/u);
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-label]").textContent, "检索证据");
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-bar]").style.width, "24%");
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");

  await harness.form.dispatch("submit");
  assert.equal(harness.fetches.length, 1, "a duplicate submit must not start another request");
  assert.match(harness.status.textContent, /仍在进行/u);

  harness.fetches[0].resolve({
    answer: "新答案",
    recommendations: [
      { id: "report-1", title: "新报告", attraction_score: 5, available: false },
      { id: "report-2", title: "状态待确认报告", attraction_score: 4 },
    ],
    usage: { remaining: 2 },
  });
  await submit;

  assert.match(harness.messages.innerHTML, /新答案/u);
  assert.match(harness.recommendations.innerHTML, /新报告/u);
  assert.match(harness.recommendations.innerHTML, /available=false/u);
  const unknownHref = harness.recommendations.innerHTML.match(/href="([^"]*id=report-2[^"]*)"/u);
  assert.ok(unknownHref);
  assert.doesNotMatch(unknownHref[1], /available=/u);
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-label]").textContent, "推荐已生成");
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-bar]").style.width, "100%");
  assert.equal(harness.button.textContent, "开始查找");
  assert.equal(harness.button.disabled, false);
  assert.equal(harness.form.getAttribute("aria-busy"), "false");
  assert.deepEqual(analyticsActions(harness), ["submit", "success"]);
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("report chat cancellation aborts the request and preserves old results", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  const cancel = harness.form.insertedElement.querySelector("[data-chat-cancel]");

  await cancel.dispatch("click");
  await submit;

  assert.equal(harness.fetches[0].options.signal.aborted, true);
  assert.match(harness.status.textContent, /已取消本次查找/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.button.textContent, "开始查找");
  assert.ok(analyticsActions(harness).includes("cancel"));
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("report research allows a 60 second synthesis window and then allows retry", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");

  harness.scheduler.runTimeout(60_000);
  await submit;

  assert.match(harness.status.textContent, /研究请求超过 60 秒/u);
  assert.match(harness.status.textContent, /点击重试/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.button.disabled, false);
  assert.ok(analyticsActions(harness).includes("timeout"));
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("report research renders grounded findings, data, charts, and escaped source content", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  const validImageId = "a".repeat(64);
  const crossReportImageId = "b".repeat(64);
  const titleFallbackImageId = "c".repeat(64);

  harness.fetches[0].resolve({
    mode: "research",
    executive_summary: "跨报告结论 <script>alert(1)</script>",
    summary_source_ids: ["report-1"],
    findings: [{ title: "需求上升", summary: "多家机构判断电力需求增加", source_ids: ["report-1", "unknown"] }],
    data_points: [{ label: "资本开支", value: "+25%", context: "2026E", source_ids: ["report-1"] }],
    sources: [{ id: "report-1", title: "摩根大通 AI 电力报告", institution: "摩根大通", attraction_score: 5 }],
    charts: [
      { image_id: validImageId, report_id: "report-1", title: "数据中心用电", description: "需求上升", metrics: ["TWh"] },
      { image_id: crossReportImageId, report_id: "report-2", report_title: "高盛 AI 电网图表报告", date_folder: "260828", title: "电网容量", description: "并网瓶颈", metrics: ["GW"] },
      { image_id: titleFallbackImageId, report_id: "", report_title: "无 ID 的来源报告", title: "供电缺口", description: "按来源标题回首页搜索" },
      { image_id: "not-an-image", report_id: "report-1", title: "无效图" },
      { image_id: "d".repeat(64), report_id: "", title: "无来源图" },
    ],
    usage: { remaining: 2 },
  });
  await submit;

  assert.match(harness.messages.innerHTML, /研究摘要/u);
  assert.match(harness.messages.innerHTML, /主要发现/u);
  assert.match(harness.messages.innerHTML, /关键数据/u);
  assert.match(harness.messages.innerHTML, /图表证据/u);
  assert.match(harness.messages.innerHTML, /report-research-finding[\s\S]*report-research-chart/u);
  const supplementalIndex = harness.messages.innerHTML.indexOf("补充图表证据");
  assert.ok(supplementalIndex > 0);
  assert.ok(harness.messages.innerHTML.indexOf(validImageId) < supplementalIndex, "same-source chart belongs inside the finding");
  assert.ok(harness.messages.innerHTML.indexOf(crossReportImageId) > supplementalIndex, "unrelated chart belongs in supplemental evidence");
  assert.ok(harness.messages.innerHTML.indexOf(titleFallbackImageId) > supplementalIndex, "title-only chart belongs in supplemental evidence");
  assert.match(harness.messages.innerHTML, /data-chart-lightbox/u);
  assert.match(harness.messages.innerHTML, /aria-haspopup="dialog"/u);
  assert.match(harness.messages.innerHTML, new RegExp(`/api/charts/image\\?id=${validImageId}`, "u"));
  assert.match(harness.messages.innerHTML, new RegExp(`/api/charts/image\\?id=${crossReportImageId}`, "u"));
  assert.match(harness.messages.innerHTML, new RegExp(`/api/charts/image\\?id=${titleFallbackImageId}`, "u"));
  assert.match(harness.messages.innerHTML, /高盛 AI 电网图表报告/u);
  assert.match(harness.messages.innerHTML, /\/report\.html\?id=report-2/u);
  assert.match(harness.messages.innerHTML, /\/\?q=%E6%97%A0%20ID%20%E7%9A%84%E6%9D%A5%E6%BA%90%E6%8A%A5%E5%91%8A/u);
  assert.doesNotMatch(harness.messages.innerHTML, /\/api\/chart-image\?/u);
  assert.match(harness.messages.innerHTML, /来源 · 摩根大通/u);
  assert.doesNotMatch(harness.messages.innerHTML, /<script>/u);
  assert.doesNotMatch(harness.messages.innerHTML, /not-an-image/u);
  assert.doesNotMatch(harness.messages.innerHTML, /无来源图/u);
  assert.doesNotMatch(harness.messages.innerHTML, /undefined/u);
  assert.match(harness.recommendations.innerHTML, /摩根大通 AI 电力报告/u);
  assert.match(harness.messages.innerHTML, /下载 Word \(\.docx\)/u);
  assert.match(harness.messages.innerHTML, /导出 PDF（打开保存界面）/u);
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-label]").textContent, "研究已生成");
});

test("successful research exports Word and print-PDF from the same response without another RAG request", async () => {
  const harness = createHarness();
  const question = harness.input.value;
  const submit = harness.form.dispatch("submit");
  const response = {
    mode: "research",
    question_hash: "export-hash-01",
    executive_summary: "可导出的来源化研究",
    sources: [{ id: "report-1", title: "来源报告" }],
  };
  harness.fetches[0].resolve(response);
  await submit;
  const fetchCount = harness.fetches.length;

  const docxButton = new FakeElement("docxExport");
  docxButton.textContent = "下载 Word (.docx)";
  docxButton.setAttribute("data-report-research-export", "docx");
  await harness.messages.dispatch("click", { target: docxButton });
  const pdfButton = new FakeElement("pdfExport");
  pdfButton.textContent = "导出 PDF（打开保存界面）";
  pdfButton.setAttribute("data-report-research-export", "pdf");
  await harness.messages.dispatch("click", { target: pdfButton });

  assert.equal(harness.fetches.length, fetchCount, "export must not issue another report-chat request");
  assert.deepEqual(harness.exportCalls.map((item) => item.kind), ["docx", "pdf"]);
  assert.equal(harness.exportCalls[0].payload.response, response);
  assert.equal(harness.exportCalls[0].payload.question, question);
  assert.equal(harness.exportCalls[0].payload.question_hash, "export-hash-01");
  assert.ok(analyticsActions(harness).includes("export_docx_started"));
  assert.ok(analyticsActions(harness).includes("export_docx_ready"));
  assert.ok(analyticsActions(harness).includes("export_pdf_started"));
  assert.ok(analyticsActions(harness).includes("export_pdf_print_opened"));
  assertAnalyticsHasNoQuestionText(harness, question);
});

test("export failure restores the button and emits only privacy-safe error analytics", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  harness.fetches[0].resolve({ mode: "research", question_hash: "export-error-hash", executive_summary: "研究结果" });
  await submit;
  harness.window.PortalReportResearchExport.downloadDocx = async () => { throw new Error("chart failed"); };
  const exportButton = new FakeElement("failedExport");
  exportButton.textContent = "下载 Word (.docx)";
  exportButton.setAttribute("data-report-research-export", "docx");
  await harness.messages.dispatch("click", { target: exportButton });

  assert.equal(exportButton.disabled, false);
  assert.equal(exportButton.textContent, "下载 Word (.docx)");
  assert.match(harness.messages.querySelector("[data-report-research-export-status]").textContent, /生成失败/u);
  assert.ok(analyticsActions(harness).includes("export_docx_error"));
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("report chat shows server diagnostics without discarding the previous result", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  harness.fetches[0].resolve({ detail: "上游服务暂时不可用", stage_code: "MODEL", request_hint: "ABC123" }, { ok: false, status: 503 });
  await submit;

  assert.match(harness.status.textContent, /上游服务暂时不可用/u);
  assert.match(harness.status.textContent, /HTTP 503/u);
  assert.match(harness.status.textContent, /点击重试/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.form.insertedElement.getAttribute("data-state"), "error");
  assert.ok(analyticsActions(harness).includes("error"));
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("anonymous homepage research sends visitor_id without Authorization and reports the one-use tier", async () => {
  const harness = createHarness({ authenticated: false });
  const submit = harness.form.dispatch("submit");

  assert.equal(harness.fetches.length, 1);
  assert.equal(harness.fetches[0].options.method, "POST");
  assert.equal(Object.hasOwn(harness.fetches[0].options.headers, "Authorization"), false);
  const body = JSON.parse(harness.fetches[0].options.body);
  assert.equal(body.visitor_id, "visitor-test-123");
  assert.equal(body.question, harness.input.value);

  harness.fetches[0].resolve({
    answer: "游客研究结果",
    question_hash: "guest-hash-01",
    usage: { tier: "anonymous", limit: 1, remaining: 0, period: "once" },
  });
  await submit;

  assert.match(harness.messages.innerHTML, /游客研究结果/u);
  assert.match(harness.status.textContent, /游客/u);
  assert.match(harness.status.textContent, /当前设备限 1 次，剩余 0 次/u);
  assert.deepEqual(analyticsActions(harness), ["submit", "success"]);
  assert.equal(harness.analyticsEvents.at(-1).data.question_hash, "guest-hash-01");
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("usage copy shows daily member limits, administrator unlimited access, and public cache semantics", async () => {
  const member = createHarness();
  const memberSubmit = member.form.dispatch("submit");
  member.fetches[0].resolve({ answer: "会员结果", usage: { tier: "standard", limit: 2, remaining: 1, period: "daily" } });
  await memberSubmit;
  assert.match(member.status.textContent, /普通会员 · 今日限 2 次，剩余 1 次/u);

  const admin = createHarness();
  const adminSubmit = admin.form.dispatch("submit");
  admin.fetches[0].resolve({ answer: "管理员结果", usage: { tier: "admin", limit: null, remaining: null, period: "daily" } });
  await adminSubmit;
  assert.match(admin.status.textContent, /管理员 · 不限次使用/u);

  const cache = createHarness();
  const cacheSubmit = cache.form.dispatch("submit");
  cache.fetches[0].resolve({ answer: "精选结果", usage: { tier: "public_cache", limit: null, remaining: null, period: "cache" } });
  await cacheSubmit;
  assert.match(cache.status.textContent, /热门问题 · 历史精选结果，不计使用次数/u);
});

test("popular questions load on startup and render cached research through GET only", async () => {
  const harness = createHarness({ authenticated: false, includePopular: true });
  assert.equal(harness.fetches.length, 1);
  assert.equal(harness.fetches[0].url, "/api/report-chat/popular");
  assert.equal(harness.fetches[0].options.method, "GET");

  const question = "AI 数据中心的电力瓶颈是什么？";
  harness.fetches[0].resolve({
    items: [
      { id: "popular-1", question, question_hash: "popular-hash-1" },
      { id: "popular-2", question: "资本开支如何变化？", question_hash: "popular-hash-2" },
    ],
  });
  await new Promise((resolve) => setImmediate(resolve));

  assert.equal(harness.popular.hidden, false);
  assert.match(harness.popularList.innerHTML, /热门研究/u);
  assert.match(harness.popularList.innerHTML, /AI 数据中心的电力瓶颈/u);
  assert.equal(analyticsActions(harness).filter((action) => action === "popular_impression").length, 2);

  const popularButton = new FakeElement("popularButton");
  popularButton.setAttribute("data-popular-id", "popular-1");
  const click = harness.popularList.dispatch("click", { target: popularButton });
  assert.equal(harness.fetches.length, 2);
  assert.match(harness.fetches[1].url, /^\/api\/report-chat\/popular\?id=popular-1$/u);
  assert.equal(harness.fetches[1].options.method, "GET");
  const imageId = "e".repeat(64);
  harness.fetches[1].resolve({
    id: "popular-1",
    question,
    question_hash: "popular-hash-1",
    response: {
      answer: "电网接入与供电容量是关键约束。",
      sources: [{ id: "source-1", title: "电力基础设施研究", institution: "研究机构" }],
      charts: [{ image_id: imageId, report_id: "source-1", title: "数据中心用电需求" }],
    },
    usage: { tier: "public_cache", limit: null, remaining: null, period: "cache" },
    cached: true,
  });
  await click;

  assert.equal(harness.fetches.some((request) => request.options.method === "POST"), false);
  assert.match(harness.messages.innerHTML, /研究摘要/u);
  assert.match(harness.messages.innerHTML, /电网接入与供电容量/u);
  assert.match(harness.messages.innerHTML, /data-chart-lightbox/u);
  assert.match(harness.status.textContent, /不消耗本次生成额度/u);
  assert.ok(analyticsActions(harness).includes("popular_click"));
  assert.ok(analyticsActions(harness).includes("popular_success"));
  const exportButton = new FakeElement("popularExport");
  exportButton.textContent = "下载 Word (.docx)";
  exportButton.setAttribute("data-report-research-export", "docx");
  const fetchCount = harness.fetches.length;
  await harness.messages.dispatch("click", { target: exportButton });
  assert.equal(harness.fetches.length, fetchCount, "cached popular export must not call the model");
  assert.equal(harness.exportCalls.at(-1).payload.question, question);
  assert.equal(harness.exportCalls.at(-1).payload.question_hash, "popular-hash-1");
  assertAnalyticsHasNoQuestionText(harness, question);
});

test("localized popular questions wait for an idle fallback while zh-Hans startup stays immediate", () => {
  const localized = createHarness({ authenticated: false, includePopular: true, contentLocale: "ar" });
  assert.equal(localized.fetches.length, 0, "localized first paint must not request popular research immediately");
  localized.scheduler.runTimeout(3_000);
  assert.equal(localized.fetches.length, 1);
  assert.equal(localized.fetches[0].url, "/api/report-chat/popular");

  const chinese = createHarness({ authenticated: false, includePopular: true });
  assert.equal(chinese.fetches.length, 1, "the Chinese root keeps its established immediate popular request");
  assert.equal(chinese.fetches[0].url, "/api/report-chat/popular");
});

test("429 renders a readonly member request form and submits archive-bound email request", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  harness.fetches[0].resolve({
    detail: "今日研究次数已用完",
    stage_code: "USAGE_LIMIT",
    request_available: true,
    archive_id: "archive-limit-123",
    question_hash: "limit-hash-123",
    usage: { tier: "standard", limit: 2, remaining: 0, period: "daily" },
  }, { ok: false, status: 429 });
  await submit;

  assert.match(harness.messages.innerHTML, /申请继续研究/u);
  assert.match(harness.messages.innerHTML, /value="reader@example\.com"/u);
  assert.match(harness.messages.innerHTML, /readonly/u);
  assert.match(harness.status.textContent, /今日限 2 次，剩余 0 次/u);
  assert.equal(harness.form.insertedElement.getAttribute("data-state"), "limit");
  assert.ok(analyticsActions(harness).includes("limit_reached"));

  const requestForm = new FakeElement("requestForm");
  requestForm.setAttribute("data-report-chat-request", "");
  const email = new FakeElement("requestEmail");
  email.value = "reader@example.com";
  const honeypot = new FakeElement("requestHoneypot");
  honeypot.value = "";
  const requestStatus = new FakeElement("requestStatus");
  const requestButton = new FakeElement("requestButton");
  requestButton.textContent = "申请继续研究";
  requestForm.submitButton = requestButton;
  requestForm.childrenBySelector.set("[name=requester_email]", email);
  requestForm.childrenBySelector.set("[name=honeypot]", honeypot);
  requestForm.childrenBySelector.set("[data-report-chat-request-status]", requestStatus);

  const requestSubmit = harness.messages.dispatch("submit", { target: requestForm });
  assert.equal(harness.fetches.length, 2);
  assert.equal(harness.fetches[1].url, "/api/report-chat/request");
  assert.equal(harness.fetches[1].options.headers.Authorization, "Bearer session-token");
  const body = JSON.parse(harness.fetches[1].options.body);
  assert.deepEqual(body, {
    archive_id: "archive-limit-123",
    question: harness.input.value,
    requester_email: "reader@example.com",
    visitor_id: "visitor-test-123",
    page_path: "/",
    honeypot: "",
  });
  harness.fetches[1].resolve({ ok: true, status: "sent", request_id: "request-1" }, { status: 202 });
  await requestSubmit;

  assert.match(requestStatus.textContent, /申请已发送/u);
  assert.ok(analyticsActions(harness).includes("limit_request_submit"));
  assert.ok(analyticsActions(harness).includes("limit_request_success"));
  assertAnalyticsHasNoQuestionText(harness, harness.input.value);
});

test("429 gives visitors an editable email field", async () => {
  const harness = createHarness({ authenticated: false });
  const submit = harness.form.dispatch("submit");
  harness.fetches[0].resolve({
    archive_id: "archive-guest",
    question_hash: "guest-limit-hash",
    request_available: true,
    usage: { tier: "anonymous", limit: 1, remaining: 0, period: "once" },
  }, { ok: false, status: 429 });
  await submit;

  assert.match(harness.messages.innerHTML, /placeholder="name@example\.com"/u);
  assert.doesNotMatch(harness.messages.innerHTML, /type="email"[^>]*readonly/u);
});

test("home markup and CSS expose the popular and over-limit UX", () => {
  assert.match(homeSource, /id="homeChatPopular"[\s\S]*热门研究问题/u);
  assert.match(homeSource, /id="homeChatPopularList"/u);
  assert.match(homeSource, /assets\/report-research-export\.js/u);
  assert.match(stylesSource, /\.report-chat-popular-question/u);
  assert.match(stylesSource, /\.report-chat-limit-card/u);
  assert.match(stylesSource, /\.report-chat-honeypot/u);
  assert.match(stylesSource, /\.report-research-export-actions/u);
});

test("report chat source contains all three visible progress stages and no wait cursor", () => {
  assert.match(source, /检索目录/u);
  assert.match(source, /整理候选/u);
  assert.match(source, /生成推荐/u);
  assert.match(source, /event\.key === "Escape"/u);
  assert.match(source, /closeChartLightbox/u);
  assert.match(source, /visitor_id: visitorId\(\)/u);
  assert.match(source, /archive_id: limitedArchiveId/u);
  assert.match(source, /PortalSuiteAnalytics/u);
  assert.doesNotMatch(source, /cursor\s*:\s*wait/u);
});
