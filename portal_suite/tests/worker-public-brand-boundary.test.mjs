import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerPath, "utf8");
const { default: worker } = await import(workerPath);
const { __publicBrandTest } = worker;

function extractFunction(source, name) {
  const markers = [`function ${name}(`, `async function ${name}(`];
  const start = markers.reduce((found, marker) => {
    const index = source.indexOf(marker);
    return index >= 0 && (found < 0 || index < found) ? index : found;
  }, -1);
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

function brandContext(globals = {}) {
  const start = workerSource.indexOf("const PUBLIC_BRAND");
  const end = workerSource.indexOf("const ADMIN_TOKEN_TTL_SECONDS", start);
  assert.notEqual(start, -1);
  assert.notEqual(end, -1);
  const context = vm.createContext({ ...globals });
  vm.runInContext(`${workerSource.slice(start, end)}\nglobalThis.brandFns = { publicBrandText, publicSourceText, publicAccountDisplayName };`, context);
  return context;
}

function addFunctions(context, names) {
  for (const name of names) {
    context[name] = vm.runInContext(`(${extractFunction(workerSource, name)})`, context);
  }
  return context;
}

const oldNotesBrand = ["KC", "Desk", "Notes"].join(" ");
const legacySourcePattern = new RegExp(
  ["Reportify", "Nash[\\s._-]*AI", "Macro[\\s._-]*Gate", "Support[\\s._-]*Contact", "Portal[\\s._-]+Suite", oldNotesBrand, "Two[\\s._-]*tigers", "\\bmaifu\\b", "慧博", "麦府(?:课堂|学堂)", "hibor\\.com\\.cn"].join("|"),
  "iu",
);

test("public report metadata removes aggregator brands while preserving real institutions", () => {
  const context = addFunctions(brandContext(), ["publicSearchItem", "publicSearchPayload", "reportAPublicText"]);
  const payload = context.publicSearchPayload("external", {
    items: [{
      id: "external-1",
      title: "Reportify | AI Infrastructure Outlook",
      title_cn: "NashAI：人工智能基础设施",
      institution: "Nash AI",
      channel_name: "Reportify",
      author: "Goldman Sachs Research",
      summary: "MacroGate - source summary",
    }],
    institutions: [
      { value: "NashAI", label: "NashAI", count: 1 },
      { value: "Morgan Stanley", label: "Morgan Stanley", count: 2 },
    ],
  });

  assert.equal(payload.items[0].title, "AI Infrastructure Outlook");
  assert.equal(payload.items[0].title_cn, "人工智能基础设施");
  assert.equal(payload.items[0].institution, "");
  assert.equal(payload.items[0].author, "Goldman Sachs Research");
  assert.equal(Object.hasOwn(payload.items[0], "channel_name"), false);
  assert.equal(payload.institutions.length, 1);
  assert.equal(payload.institutions[0].label, "Morgan Stanley");
  assert.doesNotMatch(JSON.stringify(payload), legacySourcePattern);
  assert.equal(context.brandFns.publicSourceText("HIBOR rises with funding costs"), "HIBOR rises with funding costs");
  assert.equal(context.brandFns.publicSourceText("Ｎａｓｈ\u200bＡＩ：Full-width source"), "Full-width source");
  assert.equal(context.reportAPublicText("HIBOR rises with funding costs"), "HIBOR rises with funding costs");
  assert.equal(context.reportAPublicText("慧博 | China rates outlook"), "China rates outlook");
  assert.equal(context.brandFns.publicSourceText("Nash\u200bAI: Hidden marker title"), "Hidden marker title");
  assert.equal(context.brandFns.publicSourceText("Portal.Suite: Dotted marker title"), "Dotted marker title");
  assert.equal(context.brandFns.publicSourceText("From reportify.cn · Clean title"), "Clean title");
});

test("fresh, stale and mirror search responses all pass the same public boundary", async () => {
  let cachedPayload = {
    items: [{ id: "fresh", title: "Reportify: Fresh title", institution: "NashAI" }],
  };
  let fresh = true;
  const context = addFunctions(brandContext({
    getSearchCache: async () => ({ cached_at: "2026-08-31T00:00:00.000Z", payload: cachedPayload }),
    cachedPayloadIsFresh: () => fresh,
    jsonResponse: (_request, _env, status, payload) => ({ status, payload }),
    putSearchCache: async () => {},
    searchPayloadHasItems: (payload) => Boolean(payload && payload.items && payload.items.length),
  }), ["publicSearchItem", "publicSearchPayload", "handleCachedSearch"]);

  const fetcher = async () => { throw new Error("upstream unavailable"); };
  const freshResponse = await context.handleCachedSearch({}, {}, "external", "AI", 1, { items: [] }, fetcher);
  assert.equal(freshResponse.payload.items[0].title, "Fresh title");
  assert.equal(freshResponse.payload.items[0].institution, "");

  fresh = false;
  cachedPayload = { items: [{ id: "stale", title: "NashAI - Stale title", institution: "Jefferies" }] };
  const staleResponse = await context.handleCachedSearch({}, {}, "external", "AI", 1, { items: [] }, fetcher);
  assert.equal(staleResponse.payload.cache_status, "stale");
  assert.equal(staleResponse.payload.items[0].title, "Stale title");
  assert.equal(staleResponse.payload.items[0].institution, "Jefferies");

  cachedPayload = { items: [] };
  const mirrorResponse = await context.handleCachedSearch(
    {},
    {},
    "authority",
    "AI",
    1,
    { items: [] },
    fetcher,
    async () => ({ items: [{ id: "mirror", title: `${oldNotesBrand}: Mirror title`, institution: "MacroGate" }] }),
  );
  assert.equal(mirrorResponse.payload.cache_status, "mirror");
  assert.equal(mirrorResponse.payload.items[0].title, "Mirror title");
  assert.equal(mirrorResponse.payload.items[0].institution, "");
  assert.doesNotMatch(JSON.stringify(mirrorResponse.payload), legacySourcePattern);
});

test("stored contact targets are sanitized again on every normalization", () => {
  const context = addFunctions(brandContext({
    CONTACT_REPORT_SOURCES: new Set(["report-a", "authority"]),
    HIBOR_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    Date,
  }), [
    "cleanReportRequestText",
    "cleanPublicReportText",
    "cleanContactReportSource",
    "cleanContactReportOriginId",
    "normalizeHotReportDate",
    "normalizeContactReportTarget",
  ]);

  const target = context.normalizeContactReportTarget({
    source: "report-a",
    id: "report-a:legacy-1",
    title: "Reportify | Global AI Outlook",
    institution: "NashAI",
    author: "MacroGate",
    category: "Technology",
    date: "2026-08-31",
  }, "report-a", "report-a:legacy-1");
  assert.equal(target.title, "Global AI Outlook");
  assert.equal(target.institution, "");
  assert.equal(target.author, "");
  assert.equal(target.category, "Technology");
  assert.doesNotMatch(JSON.stringify(target), legacySourcePattern);
});

test("user-facing brand positions use the canonical public brand", () => {
  const context = brandContext();
  for (const oldBrand of ["Portal Suite", "Portal Alternate", "Portal 娱乐", "Support Contact", "MacroGate", "Twotigers"]) {
    assert.equal(context.brandFns.publicBrandText(oldBrand), "KC桌面");
  }
  assert.doesNotMatch(workerSource, /CONTACT_WECHAT|Contact WeChat|联系微信/u);
  assert.match(workerSource, /embedded-v2:/u);
  assert.doesNotMatch(workerSource, /embedded-v1:/u);
  assert.equal(context.brandFns.publicAccountDisplayName("Twotigers", "super"), "KC桌面管理员");
  assert.equal(context.brandFns.publicAccountDisplayName("Portal Alternate", "operator"), "KC桌面运营");
  assert.equal(context.brandFns.publicAccountDisplayName("reader-one", "user"), "reader-one");
});

test("public account and analytics payloads never expose private account aliases", () => {
  const context = addFunctions(brandContext({
    SITE_ORIGIN: "portal",
    accountRole: (user) => user.role || "user",
    accountDisabled: () => false,
    isGeneratedEmail: () => false,
  }), ["publicUser", "publicAnalyticsEvent"]);

  const account = context.publicUser({
    id: "admin-1",
    username: "Twotigers",
    email: "admin@example.com",
    role: "super",
  });
  assert.equal(account.username, "KC桌面管理员");
  assert.equal(account.email, "admin@example.com");

  const redactedAccount = context.publicUser({
    id: "private-1",
    username: ["two", "tigers"].join(""),
    email: ["two", "tigers", "@example.com"].join(""),
    role: "user",
  });
  assert.equal(redactedAccount.id, "private-1");
  assert.equal(redactedAccount.email, "");

  const analytics = context.publicAnalyticsEvent({
    id: "event-1",
    user: { username: "Portal Alternate", email: "operator@example.com", role: "operator" },
    query: "Reportify market search",
    report_title: "NashAI: Market outlook",
    institution: "MacroGate",
    referrer_host: "reportify.cn",
    utm_campaign: "Portal Suite campaign",
  });
  assert.equal(analytics.user.username, "KC桌面运营");
  assert.equal(analytics.query, "KC桌面 market search");
  assert.equal(analytics.report_title, "Market outlook");
  assert.equal(analytics.institution, "");
  const courseAnalytics = context.publicAnalyticsEvent({
    id: "event-course",
    type: "course_material_request",
    source: "maifu",
    target: "maifu-01",
  });
  assert.equal(courseAnalytics.source, "KC桌面学堂");
  assert.equal(courseAnalytics.target, "课程材料 01");
  assert.doesNotMatch(JSON.stringify({ account, redactedAccount, analytics, courseAnalytics }), legacySourcePattern);
});

test("old dashboard, schedule, settings, and filename records are sanitized again on read", () => {
  const access = __publicBrandTest.publicAccessGrant({
    email: "member@example.com",
    access_mode: "filters",
    status: "active",
    institutions: ["Reportify", "Goldman Sachs"],
    industries: ["NashAI sector"],
    note: "MacroGate migration",
    source: "Portal Suite",
    source_site: "Twotigers",
    updated_by: "private-owner",
  });
  const options = __publicBrandTest.publicAccessOptions({
    modes: [{ value: "all", label: "Portal Suite reports" }],
    institutions: [{ value: "NashAI", label: "NashAI (2)" }, { value: "Jefferies", label: "Jefferies (1)" }],
    industries: [{ value: "MacroGate sector", label: "MacroGate sector (2)" }],
    page_ranges: [],
    durations: [],
  });
  const pick = __publicBrandTest.publicDailyPick({
    id: "pick-1",
    title: "Reportify: Daily report",
    title_zh: "NashAI 每日报告",
    display_title: "MacroGate 精选",
    filename: "Portal Suite.pdf",
    bank: "Twotigers",
    tags: ["Reportify"],
    intro: "Nash AI introduction",
  });
  const schedule = __publicBrandTest.publicWechatSchedule({
    date_label: "Portal Suite 今日",
    source_dates: [{ source_label: "Twotigers", date_folder: "260831" }],
    batches: [{
      source_label: "Reportify",
      batch_label: "NashAI batch",
      day_label: "MacroGate day",
      articles: [{ label: "Portal Suite 头条", title: "Reportify article" }],
    }],
  });
  const settings = __publicBrandTest.publicNewsfeedSettings({
    digest_last_send_result: "NashAI failed",
    digest_last_send_detail: "Reportify provider error via MacroGate",
  }, { email: "member@example.com" }, {});
  const filename = __publicBrandTest.publicDownloadFilename("Portal Suite - NashAI report.pdf");
  const documentText = __publicBrandTest.publicBrandDocumentText("Reportify body from Twotigers, maifu, and 麦府课堂");
  const recursive = __publicBrandTest.publicBrandValue({ title: "MacroGate", values: ["Portal Suite"] });
  const directoryItem = __publicBrandTest.cleanCourseDirectoryItem({
    id: "file-legacy-01",
    course_id: "fin-01",
    name: "Reportify valuation course",
    folders: ["NashAI materials"],
    extension: "pdf",
    size_label: "2 MB",
    date: "2026-08-31",
    entities: ["MacroGate", "Goldman Sachs"],
  }, []);

  const payload = { access, options, pick, schedule, settings, filename, documentText, recursive, directoryItem };
  assert.equal(access.institutions.includes("Goldman Sachs"), true);
  assert.equal(options.institutions.some((option) => option.value === "Jefferies"), true);
  assert.match(filename, /KC桌面/u);
  assert.deepEqual(Array.from(directoryItem.entities), ["Goldman Sachs"]);
  assert.doesNotMatch(JSON.stringify(payload), legacySourcePattern);
});

test("admin file labels are sanitized before the dashboard response", () => {
  const context = addFunctions(brandContext(), ["publicAdminFile"]);
  const row = context.publicAdminFile({
    label: "Portal 娱乐视频",
    name: "Portal Alternate clip.mp4",
    recommended_account: "Portal 娱乐",
    account_label_reason: "Portal 娱乐专属内容",
  });
  assert.equal(row.label, "KC桌面视频");
  assert.equal(row.name, "KC桌面 clip.mp4");
  assert.equal(row.recommended_account, "KC桌面");
  assert.equal(row.account_label_reason, "KC桌面专属内容");
});

test("RAG answers, stored snapshots, and admin history are sanitized on read", () => {
  const response = __publicBrandTest.reportChatSafePublicResponse({
    mode: "research",
    research_title: "Reportify AI outlook",
    research_scope: "NashAI and MacroGate reports",
    executive_summary: "Portal Suite synthesis",
    findings: [{
      title: "Twotigers conclusion",
      summary: "Reportify data supports the finding",
      source_ids: ["report-a"],
    }],
    data_points: [{ label: "Nash AI metric", value: "MacroGate 42", source_ids: ["report-a"] }],
    sources: [{ id: "report-a", title: "Reportify: Clean report", institution: "NashAI" }],
    follow_up_questions: ["What does Portal Suite conclude?"],
  });
  const archive = __publicBrandTest.reportChatSafeArchiveItem({
    version: 1,
    id: "a".repeat(32),
    context: "report",
    question: "Reportify question",
    status: "success",
    actor: { kind: "account", username: "Twotigers", email: "admin@example.com", role: "super" },
    response,
  });
  const index = __publicBrandTest.normalizeReportChatPublicIndex({
    items: [{
      id: "b".repeat(32),
      question: "NashAI popular question",
      question_hash: "c".repeat(64),
      rank: 1,
      published_at: "2026-08-31T00:00:00.000Z",
    }],
  });
  const candidate = __publicBrandTest.chatLookupPublicCandidate({
    id: "report-a",
    title: "MacroGate: Candidate title",
    institution: "Reportify",
  }, "report-a", 1, "report");
  const unknownAdminName = __publicBrandTest.hotReportCommentDisplayName({
    display_name: "private-release-owner",
    author_role: "super",
    admin_alias: false,
  });
  const chart = __publicBrandTest.publicChartGalleryRecord(
    { report_id: "report-a", title: "Reportify: Chart source" },
    {
      analysis_version: "chart-search-v2",
      image_id: "d".repeat(64),
      content_kind: "chart",
      quality_score: 80,
      title: "NashAI capacity chart",
      description: "MacroGate supplied the series",
      trend_summary: "Portal Suite trend",
      entities: ["Twotigers"],
    },
  );
  const marketView = __publicBrandTest.publicMarketViewItem({
    id: "market-view:260831",
    title: "Reportify: Market Views",
    filename: "NashAI-daily.pdf",
  });
  const hotReport = __publicBrandTest.publicHotReportItem({
    id: "hot:0123456789abcdef",
    retention_state: "active",
    title: "Reportify: Featured report",
    institution: "NashAI",
    description: "MacroGate summary",
    filename: "Twotigers-report.pdf",
  });
  const hotComment = __publicBrandTest.publicHotReportComment({
    id: "comment:aaaaaaaaaaaaaaaa",
    report_id: "hot:0123456789abcdef",
    display_name: "private-release-owner",
    author_role: "super",
    body: "Reportify analysis via NashAI",
  });
  const newsItem = __publicBrandTest.publicNewsfeedItem({
    id: "news-a",
    title: "Reportify says AI demand is rising",
    url: "https://reuters.com/example",
    source: "NashAI",
    domain: "reuters.com",
    summary: "MacroGate summary",
    category: "Portal Suite Investment",
  });
  const blockedNewsItem = __publicBrandTest.publicNewsfeedItem({
    id: "news-b",
    title: "Legacy source",
    url: "https://reportify.cn/example",
  });
  const newsTopic = __publicBrandTest.publicNewsfeedTopic({
    id: "topic-a",
    title: "Nash AI watch",
    description: "MacroGate headlines",
    category: "Portal Suite",
    query_plan: { source_mix: ["Reportify", "Reuters"] },
  });
  const oldNewsCache = __publicBrandTest.publicNewsfeedItemsPayload({
    items: [{
      id: "cached-news",
      title: "Reportify cached title",
      url: "https://reuters.com/cached",
      source: "NashAI",
      summary: "MacroGate cached summary",
    }],
  });
  const articleNarrative = __publicBrandTest.fallbackArticleNarrative({
    title: "Reportify article",
    source: "NashAI",
    summary: "MacroGate summary",
    output_language: "zh-CN",
  });
  const briefing = __publicBrandTest.buildNewsfeedBriefingScript({
    language: "zh-CN",
    digest: ["Portal Suite briefing", "Twotigers update"],
  });
  const emailPayload = {
    newsletter_title: "Reportify digest",
    daily_digest: ["NashAI daily"],
    headlines: [{
      id: "email-news",
      title: "MacroGate headline",
      url: "https://reuters.com/email",
      source: "Portal Suite",
    }],
  };
  const emailText = __publicBrandTest.newsfeedEmailText(emailPayload);
  const emailHtml = __publicBrandTest.newsfeedEmailHtml(emailPayload);

  assert.equal(response.sources[0].title, "Clean report");
  assert.equal(response.sources[0].institution, "");
  assert.equal(archive.actor.username, "KC桌面管理员");
  assert.equal(candidate.title, "Candidate title");
  assert.equal(unknownAdminName, "KC桌面管理员");
  assert.equal(marketView.title, "Market Views");
  assert.equal(hotReport.title, "Featured report");
  assert.equal(hotReport.institution, "");
  assert.equal(blockedNewsItem, null);
  assert.doesNotMatch(JSON.stringify({
    response, archive, index, candidate, chart, marketView, hotReport, hotComment, newsItem, newsTopic,
    oldNewsCache, articleNarrative, briefing, emailText, emailHtml,
  }), legacySourcePattern);

  const handlerStart = workerSource.indexOf("async function handleReportChat(");
  const handlerEnd = workerSource.indexOf("\nfunction publicChartGalleryRecord(", handlerStart);
  const handlerSource = workerSource.slice(handlerStart, handlerEnd);
  assert.match(handlerSource, /const publicResponse = reportChatSafePublicResponse\(response\)/u);
  assert.match(handlerSource, /return privateJsonResponse\(request, env, 200, \{\s*\.\.\.publicResponse,/u);
  assert.match(handlerSource, /const answer = publicBrandText\([\s\S]*?fallbackReportChatAnswer/u);
  assert.doesNotMatch(handlerSource, /return privateJsonResponse\(request, env, 200, \{\s*\.\.\.response,/u);
});

test("calculator response never exposes an internal brand namespace", async () => {
  const response = await worker.fetch(new Request(
    "https://worker.test/calc?id=0123456789abcdef&key=calculator-test",
  ), {
    CALC_KEY: "calculator-test",
    PASSWORD_SECRET: "password-test-secret",
    ALLOWED_ORIGIN: "https://worker.test",
  }, { waitUntil() {} });
  assert.equal(response.status, 200);
  const payload = await response.json();
  assert.deepEqual(Object.keys(payload).sort(), ["id", "password"]);
  assert.equal(payload.id, "0123456789abcdef");
  assert.equal(typeof payload.password, "string");
  assert.ok(payload.password.length > 0);
});
