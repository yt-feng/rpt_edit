import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const { default: worker } = await import(workerPath);
const { __analyticsTest } = worker;

function analyticsBrowser({ analyticsAuto = "", readyState = "complete" } = {}) {
  const requests = [];
  const values = new Map();
  const dataset = { page: "test" };
  if (analyticsAuto) dataset.analyticsAuto = analyticsAuto;
  const window = {
    document: {
      readyState,
      body: { dataset },
      referrer: "",
      addEventListener() {},
    },
    location: {
      pathname: "/test.html",
      search: "",
      origin: "https://portal.example.invalid",
    },
    localStorage: {
      getItem(key) { return values.get(key) || null; },
      setItem(key, value) { values.set(key, String(value)); },
    },
    navigator: { language: "zh-CN", userAgent: "test-browser" },
    performance: { getEntriesByType() { return []; } },
    screen: { width: 1440, height: 900 },
    async fetch(url, init = {}) {
      requests.push({ url: String(url), init });
      if (url === "/data/config.json") {
        return { ok: true, async json() { return { worker_base_url: "/api" }; } };
      }
      return { ok: true, async json() { return {}; } };
    },
  };
  return { requests, window };
}

async function settleAnalytics() {
  await new Promise((resolve) => setImmediate(resolve));
  await new Promise((resolve) => setImmediate(resolve));
}

test("analytics client ships session and campaign context on every static page", async () => {
  const analytics = await readFile(path.join(root, "portal_suite/site_src/assets/analytics.js"), "utf8");
  for (const field of [
    "session_id", "first_seen_at", "is_returning", "landing_path",
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "navigation_type", "device_type", "bot_hint",
  ]) assert.match(analytics, new RegExp(field, "u"), `${field} must be collected`);

  const pages = ["index", "report", "doc", "delivery", "newsfeed", "activity", "privacy", "refund", "terms", "courses", "charts", "developer-api"];
  for (const page of pages) {
    const html = await readFile(path.join(root, `portal_suite/site_src/${page}.html`), "utf8");
    assert.match(html, /assets\/analytics\.js/u, `${page}.html must load the shared analytics client`);
  }
});

test("pages with app-managed page views opt out of the shared automatic page view", async () => {
  const manualPages = ["index", "report", "doc", "newsfeed"];
  for (const page of manualPages) {
    const html = await readFile(path.join(root, `portal_suite/site_src/${page}.html`), "utf8");
    assert.match(
      html,
      /<body\b[^>]*\bdata-analytics-auto="manual"/u,
      `${page}.html must leave page_view timing to app.js`,
    );
  }

  const autoPages = ["delivery", "activity", "privacy", "refund", "terms", "courses", "charts", "developer-api"];
  for (const page of autoPages) {
    const html = await readFile(path.join(root, `portal_suite/site_src/${page}.html`), "utf8");
    assert.doesNotMatch(
      html,
      /<body\b[^>]*\bdata-analytics-auto="manual"/u,
      `${page}.html must retain the shared automatic page_view`,
    );
  }
});

test("analytics auto page view honors manual mode without disabling normal pages", async () => {
  const analytics = await readFile(path.join(root, "portal_suite/site_src/assets/analytics.js"), "utf8");

  const manual = analyticsBrowser({ analyticsAuto: "manual" });
  vm.runInNewContext(analytics, { window: manual.window, URL, URLSearchParams, TextEncoder });
  await settleAnalytics();
  assert.equal(manual.requests.length, 0, "manual mode must not emit an automatic page_view");

  const automatic = analyticsBrowser();
  vm.runInNewContext(analytics, { window: automatic.window, URL, URLSearchParams, TextEncoder });
  await settleAnalytics();
  assert.deepEqual(
    automatic.requests.map(({ url }) => url),
    ["/data/config.json", "/api/analytics"],
    "normal pages must still resolve config and emit one automatic page_view",
  );
  const event = JSON.parse(automatic.requests[1].init.body);
  assert.equal(event.type, "page_view");
  assert.equal(event.data.page, "test");
  assert.equal(event.data.referrer, "", "a direct visit must not be rewritten as a self-referral");
  assert.match(event.data.session_started_at, /^\d{4}-\d{2}-\d{2}T/u);
});

test("worker enriches attribution, device and bot fields without storing a raw IP", async () => {
  const writes = new Map();
  const bucket = {
    async put(key, value) {
      writes.set(key, String(value));
      return { etag: `etag-${writes.size}` };
    },
  };
  const request = new Request("https://worker.test/analytics", {
    method: "POST",
    headers: {
      "content-type": "application/json",
      "Origin": "https://portal.example.invalid",
      "CF-Connecting-IP": "203.0.113.7",
      "User-Agent": "Mozilla/5.0 (iPhone; CPU iPhone OS 18_0 like Mac OS X) Mobile/15E148",
      "Referer": "https://search.example/?q=research",
    },
    body: JSON.stringify({
      type: "page_view",
      visitor_id: "visitor-a",
      session_id: "session-a",
      path: "/reports/example.html?utm_source=newsletter",
      data: {
        page: "seo-report",
        landing_path: "/reports/example.html?utm_source=newsletter",
        session_started_at: "2026-08-09T01:00:00.000Z",
        first_seen_at: "2026-08-09T01:00:00.000Z",
        is_returning: true,
        utm_source: "newsletter",
        utm_medium: "email",
        utm_campaign: "daily-research",
        report_id: "report-b",
        report_title: "目标报告",
        parent_report_id: "report-a",
        placement: "report_related",
      },
    }),
  });
  Object.defineProperty(request, "cf", {
    value: { country: "SG", colo: "SIN", botManagement: { score: 91, verifiedBot: false } },
  });
  const response = await worker.fetch(request, {
    REPORT_BUCKET: bucket,
    MASTER_KEY: "analytics-secret",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  });
  assert.equal(response.status, 204);
  assert.equal(writes.size, 2, "primary and backup event objects must both be written");
  const primary = [...writes.entries()].find(([key]) => key.startsWith("_analytics/events/"));
  assert.ok(primary);
  const event = JSON.parse(primary[1]);
  assert.equal(event.session_id, "session-a");
  assert.equal(event.session_started_at, "2026-08-09T01:00:00.000Z");
  assert.equal(event.utm_source, "newsletter");
  assert.equal(event.referrer_host, "search.example");
  assert.equal(event.parent_report_id, "report-a");
  assert.equal(event.placement, "report_related");
  assert.equal(event.device_type, "mobile");
  assert.equal(event.bot_hint, "likely_human");
  assert.equal(event.bot_score, 91);
  assert.equal(event.ip_hash.length, 24);
  assert.equal(event.path, "/reports/example.html");
  assert.equal(event.landing_path, "/reports/example.html");
  assert.equal(event.referrer, "https://search.example/");
  assert.doesNotMatch(primary[1], /utm_source=newsletter|q=research/u, "URL queries must not be persisted");
  assert.doesNotMatch(primary[1], /203\.0\.113\.7/u, "the raw client IP must never be persisted");
});

test("research diagnostics survive ingestion and export without storing the question", async () => {
  const writes = new Map();
  const response = await worker.fetch(new Request("https://worker.test/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", "Origin": "https://portal.example.invalid" },
    body: JSON.stringify({
      type: "report_chat_interaction", visitor_id: "diagnostic-visitor", session_id: "diagnostic-session",
      path: "/research.html", data: {
        action: "success", placement: "research", context: "report", source_count: 4, chart_count: 0,
        question_length: 34, remaining: 1, current_streak: 3,
        query: "private research question", question: "private research question",
      },
    }),
  }), {
    REPORT_BUCKET: { async put(key, value) { writes.set(key, String(value)); return { etag: "ok" }; } },
    MASTER_KEY: "analytics-secret", ALLOWED_ORIGIN: "https://portal.example.invalid",
  });
  assert.equal(response.status, 204);
  const stored = JSON.parse([...writes.values()][0]);
  const exported = __analyticsTest.publicAnalyticsEvent(stored);
  for (const event of [stored, exported]) {
    assert.equal(event.context, "report");
    assert.equal(event.source_count, 4);
    assert.equal(event.chart_count, 0, "zero charts is a measured absence, not missing instrumentation");
    assert.equal(event.question_length, 34);
    assert.equal(event.remaining, 1);
    assert.equal(event.current_streak, 3);
    assert.doesNotMatch(JSON.stringify(event), /private research question/);
  }
  const legacy = __analyticsTest.publicAnalyticsEvent({ type: "report_chat_interaction" });
  assert.equal(legacy.chart_count, null, "historical missing chart counts must remain unknown");
  const invalid = __analyticsTest.publicAnalyticsEvent({
    type: "report_chat_interaction", context: "private free text", chart_count: -1, source_count: "not-a-count",
    current_streak: true, question_length: 3.5,
  });
  assert.equal(invalid.context, "");
  assert.equal(invalid.chart_count, null);
  assert.equal(invalid.source_count, null);
  assert.equal(invalid.current_streak, null);
  assert.equal(invalid.question_length, 3);
});

test("analytics endpoint rejects foreign origins and unsupported public event types", async () => {
  const bucket = { async put() { throw new Error("must not write"); } };
  const env = {
    REPORT_BUCKET: bucket,
    MASTER_KEY: "analytics-secret",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  };
  const foreign = await worker.fetch(new Request("https://worker.test/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", "Origin": "https://foreign.example" },
    body: JSON.stringify({ type: "page_view" }),
  }), env);
  assert.equal(foreign.status, 403);

  const unsupported = await worker.fetch(new Request("https://worker.test/analytics", {
    method: "POST",
    headers: { "content-type": "application/json", "Origin": "https://portal.example.invalid" },
    body: JSON.stringify({ type: "invented_event" }),
  }), env);
  assert.equal(unsupported.status, 400);
});

test("daily summary contract returns aggregate dimensions without visitor hashes", async () => {
  const workerSource = await readFile(workerPath, "utf8");
  const appSource = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  assert.match(workerSource, /pathname === "\/account-admin\/analytics-day-summary"/u);
  assert.match(workerSource, /unique_visitor_count/u);
  assert.match(workerSource, /top_referrer_hosts/u);
  assert.match(workerSource, /acquisition_landings/u);
  assert.match(workerSource, /ANALYTICS_ACQUISITION_SCHEMA_VERSION/u);
  assert.match(workerSource, /analyticsBjtDateKey\(sessionStartedAt\)/u);
  assert.match(workerSource, /analyticsAcquisitionSessionKey/u);
  assert.match(workerSource, /session_started_at: event\.session_started_at \|\| ""/u);
  assert.match(appSource, /key: "session_started_at"/u);
  assert.match(workerSource, /bot_hints/u);
  const start = workerSource.indexOf("function publicAnalyticsDaySummary(");
  const end = workerSource.indexOf("\n}\n\nasync function advanceAnalyticsDaySummary", start);
  const publicContract = workerSource.slice(start, end);
  assert.doesNotMatch(publicContract, /ip_hash|visitor_keys\s*:/u, "the public daily summary must not return identifiers");
  assert.match(appSource, /来源 × 具体落地报告 \/ Blog/u);
  assert.match(appSource, /站内热门搜索/u);
});

test("daily acquisition groups the true landing session with source priority and UTM content", () => {
  const accumulator = __analyticsTest.emptyAnalyticsDayAccumulator(
    "2026-08-09",
    "admin@example.invalid",
    "_analytics/events",
    "0123456789abcdef01234567",
  );
  const pageView = (overrides = {}) => ({
    id: crypto.randomUUID(),
    type: "page_view",
    path: "/reports/report-a.html",
    landing_path: "/reports/report-a.html",
    page: "seo-report",
    report_id: "report-a",
    report_title: "报告 A",
    session_started_at: "2026-08-09T01:00:00.000Z",
    session_id: crypto.randomUUID(),
    referrer_host: "google.com",
    bot_hint: "likely_human",
    ...overrides,
  });
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-a",
    utm_source: "newsletter",
    utm_campaign: "daily",
    utm_content: "creative-a",
  }));
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-a",
    path: "/reports/report-b.html",
    report_id: "report-b",
    report_title: "报告 B",
  }));
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-b",
    utm_source: "newsletter",
    utm_campaign: "daily",
    utm_content: "creative-b",
  }));
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-cross-day",
    session_started_at: "2026-08-08T15:30:00.000Z",
  }));
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-bot",
    bot_hint: "user_agent_bot",
  }));
  __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, pageView({
    session_id: "session-direct",
    referrer_host: "",
  }));

  const summary = __analyticsTest.publicAnalyticsDaySummary(accumulator, true);
  assert.equal(summary.acquisition_landings.length, 3);
  assert.deepEqual(
    new Set(summary.acquisition_landings.map((row) => row.source)),
    new Set(["newsletter", "direct_or_unknown"]),
  );
  assert.deepEqual(
    new Set(summary.acquisition_landings.filter((row) => row.source === "newsletter").map((row) => row.utm_content)),
    new Set(["creative-a", "creative-b"]),
  );
  assert.equal(summary.acquisition_landings.some((row) => row.report_id === "report-b"), false);
});

test("developer documentation emits exactly one automatic landing page view", async () => {
  const html = await readFile(path.join(root, "portal_suite/site_src/developer-api.html"), "utf8");
  const client = analyticsBrowser();
  client.window.document.body.dataset.page = html.match(/data-page="([^"]+)"/u)[1];
  const manual = html.match(/data-analytics-auto="([^"]+)"/u);
  if (manual) client.window.document.body.dataset.analyticsAuto = manual[1];
  client.window.location.pathname = "/developer-api.html";
  vm.runInNewContext(await readFile(path.join(root, "portal_suite/site_src/assets/analytics.js"), "utf8"), {
    window: client.window, URL, URLSearchParams, TextEncoder,
  });
  await settleAnalytics();
  assert.equal(await client.window.PortalSuiteAnalytics.track("page_view", { page: "developer-api" }), false);
  const posts = client.requests.filter(({ init }) => init.method === "POST");
  assert.equal(posts.length, 1);
  const event = JSON.parse(posts[0].init.body);
  assert.equal(event.path, "/developer-api.html");
  assert.equal(event.data.landing_path, "/developer-api.html");
  assert.equal(event.data.page, "developer-api");
});

async function ingestAnalytics(data, type = "page_view") {
  const rows = new Map();
  const response = await worker.fetch(new Request("https://worker.test/analytics", {
    method: "POST",
    headers: { "Content-Type": "application/json", Origin: "https://portal.example.invalid", Referer: "https://portal.example.invalid/report.html?private=secret" },
    body: JSON.stringify({ type, path: "/report.html", data }),
  }), {
    MASTER_KEY: "analytics-fixture", ALLOWED_ORIGIN: "https://portal.example.invalid",
    REPORT_BUCKET: { async put(key, value) { rows.set(key, JSON.parse(value)); } },
  });
  assert.equal(response.status, 204);
  return [...rows.entries()].find(([key]) => key.startsWith("_analytics/events/"))[1];
}

test("explicit empty referrer never becomes the browser fetch self-referral", async () => {
  for (const referrer of ["", null, "javascript:private"]) {
    const event = await ingestAnalytics({ referrer });
    assert.equal(event.referrer, "");
    assert.equal(event.referrer_host, "direct");
  }
  const legacy = await ingestAnalytics({});
  assert.equal(legacy.referrer, "https://portal.example.invalid/report.html", "legacy callers without a referrer field retain the sanitized fallback");
});

test("daily aggregates label legacy self-referrals as unknown while preserving external and campaign evidence", () => {
  const hosts = __analyticsTest.analyticsSiteHosts({ ALLOWED_ORIGIN: "https://published.example, https://preview.example" });
  const accumulator = __analyticsTest.emptyAnalyticsDayAccumulator("2026-11-23", "admin@example.invalid", "_analytics/events", "fixture", ["_analytics/events"], hosts);
  for (const [index, data] of [
    { referrer_host: "published.example" },
    { referrer_host: "www.published.example" },
    { referrer_host: "preview.example" },
    { referrer_host: "portal.example.invalid" },
    { referrer_host: "" },
    { referrer_host: "published.example.foreign.example" },
    { referrer_host: "google.com" },
    { referrer_host: "published.example", utm_source: "newsletter" },
  ].entries()) {
    __analyticsTest.addAnalyticsDaySummaryEvent(accumulator, {
      type: "page_view", path: "/report.html", landing_path: "/report.html", session_id: `session-${index}`, ...data,
    });
  }
  const summary = __analyticsTest.publicAnalyticsDaySummary(accumulator, true);
  const bySource = Object.fromEntries(summary.acquisition_landings.map((row) => [row.source, row.sessions]));
  assert.deepEqual(bySource, { direct_or_unknown: 5, "google.com": 1, newsletter: 1, "published.example.foreign.example": 1 });
  assert.equal(summary.top_referrer_hosts.find((row) => row.label === "direct_or_unknown")?.count, 6);
});

function cachedSummary(date, scan, generated = scan) {
  const accumulator = __analyticsTest.emptyAnalyticsDayAccumulator(date, "admin@example.invalid", "_analytics/events", "fixture");
  return { ...__analyticsTest.publicAnalyticsDaySummary(accumulator, true), scan_started_at: scan, generated_at: generated };
}

test("current-day cache expires at five minutes from scan start, not completion", () => {
  const now = Date.parse("2026-11-23T12:00:00+08:00");
  const fresh = cachedSummary("2026-11-23", "2026-11-23T11:55:01+08:00", "2026-11-23T11:59:59+08:00");
  assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(fresh, fresh.date, now), true);
  for (const overrides of [
    { scan_started_at: "2026-11-23T11:55:00+08:00" },
    { scan_started_at: "2026-11-23T11:54:59+08:00" },
    { scan_started_at: "" }, { scan_started_at: "invalid" },
    { scan_started_at: "2026-11-23T12:00:01+08:00" },
    { generated_at: "invalid" }, { generated_at: "2026-11-23T12:00:01+08:00" },
    { acquisition_schema_version: 3 }, { complete: false },
  ]) assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh({ ...fresh, ...overrides }, fresh.date, now), false, JSON.stringify(overrides));
});

test("Beijing midnight requires a new historical scan even when a long job completed after midnight", () => {
  const now = Date.parse("2026-11-24T00:01:00+08:00");
  for (const generated of ["2026-11-23T23:59:30+08:00", "2026-11-24T00:00:30+08:00"]) {
    const partialDay = cachedSummary("2026-11-23", "2026-11-23T23:59:00+08:00", generated);
    assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(partialDay, partialDay.date, now), false);
  }
  const closedDay = cachedSummary("2026-11-23", "2026-11-24T00:00:00+08:00", "2026-11-24T00:00:30+08:00");
  assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(closedDay, closedDay.date, now), true);
  assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(closedDay, closedDay.date, now + 30 * 86400000), true);
  const future = cachedSummary("2026-11-25", "2026-11-24T00:00:00+08:00");
  assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(future, future.date, now), false);
});

test("historical summaries with unreadable events are rebuilt instead of cached indefinitely", () => {
  const now = Date.parse("2026-11-25T12:00:00+08:00");
  const summary = cachedSummary("2026-11-23", "2026-11-24T01:00:00+08:00");
  assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh(summary, summary.date, now), true);
  for (const skipped of [1, 4, undefined, null, "0"]) {
    assert.equal(__analyticsTest.analyticsDaySummaryCacheFresh({ ...summary, skipped_count: skipped }, summary.date, now), false);
  }
});

test("explicit day-summary refresh bypasses a fresh cache", async () => {
  const now = Date.now(), date = new Date(now + 8 * 3600000).toISOString().slice(0, 10);
  const user = { id: "fixture-admin", username: "admin-a", email: "admin-a@users.portal.example.invalid" };
  const secret = "analytics-refresh-fixture";
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, iat: Math.floor(now / 1000), exp: Math.floor(now / 1000) + 3600 })).toString("base64url");
  const signature = createHmac("sha256", secret).update(`portal:account-token:v1:${body}`).digest("base64url");
  const rows = new Map([
    ["_account/users/username/admin-a", user],
    [`_account/analytics-day-summaries/${date}.json`, cachedSummary(date, new Date(now).toISOString())],
  ]);
  let listings = 0;
  const env = { ACCOUNT_STORE_MODE: "r2", MASTER_KEY: secret, REPORT_BUCKET: {
    async get(key) { return rows.has(key) ? { text: async () => JSON.stringify(rows.get(key)), json: async () => rows.get(key) } : null; },
    async put() {},
    async list() { listings += 1; return { objects: [], delimitedPrefixes: [], truncated: false }; },
  } };
  const request = (suffix) => new Request(`https://worker.test/account-admin/analytics-day-summary?date=${date}${suffix}`, { headers: { Authorization: `Bearer ${body}.${signature}` } });
  const cached = await worker.fetch(request(""), env);
  assert.equal(cached.status, 200);
  assert.equal((await cached.json()).cached, true);
  assert.equal(listings, 0);
  const refreshed = await worker.fetch(request("&refresh=1"), env);
  assert.equal(refreshed.status, 404, "the empty live archive must be checked instead of serving the cached count");
  assert.ok(listings > 0);
});

test("report loading diagnostics remain events without inflating report opens", () => {
  const events = ["detail_load_start", "detail_load_fallback", "detail_load_ready", "access_check_error", "", "post_download_related_open"]
    .map((action) => ({ type: "report_open", action, report_id: "report-a", date: "2026-11-23" }));
  events.push({ type: "download_success", report_id: "report-a", date: "2026-11-23" });
  const top = __analyticsTest.analyticsTopReports(events);
  assert.equal(top[0].opens, 2);
  assert.equal(top[0].downloads, 1);
  assert.equal(__analyticsTest.analyticsDailySeries(events)[0].opens, 2);
  assert.equal(__analyticsTest.analyticsDailySeries(events)[0].events, 7);
  assert.equal(events.filter(__analyticsTest.analyticsIsReportOpen).length, 2);
});

test("Newsfeed diagnostics survive storage and export only as bounded values", async () => {
  const allowed = { category: "Tech", provider: "brevo", latency_bucket: "4_15s", reason: "NEWSFEED_TOPIC_LIMIT", custom_topic_remaining: 0 };
  const stored = await ingestAnalytics({ ...allowed, query: "private topic" }, "newsfeed_interaction");
  for (const event of [stored, __analyticsTest.publicAnalyticsEvent(stored)]) {
    for (const [key, value] of Object.entries(allowed)) assert.equal(event[key], value);
    assert.doesNotMatch(JSON.stringify(event), /private topic/u);
  }
  for (const value of ["PRIVATE@example.invalid", "https://private.example", "NEWSFEED_PRIVATE_FREE_TEXT", "newsfeed_topic_limit", "constructor", "__proto__", "x".repeat(1000), 4, null, {}, ["brevo"]]) {
    const data = { category: value, provider: value, latency_bucket: value, reason: value, custom_topic_remaining: -1 };
    const bad = await ingestAnalytics(data, "newsfeed_interaction");
    for (const event of [bad, __analyticsTest.publicAnalyticsEvent({ type: "newsfeed_interaction", ...data })]) {
      for (const key of ["category", "provider", "latency_bucket", "reason"]) assert.equal(event[key], "");
      assert.equal(event.custom_topic_remaining, null);
    }
  }
  assert.equal(__analyticsTest.publicAnalyticsEvent({ type: "newsfeed_interaction", custom_topic_remaining: 1e12 }).custom_topic_remaining, 1e6);
  assert.equal(__analyticsTest.publicAnalyticsEvent({ type: "page_view", ...allowed }).reason, undefined);
});

test("Activity filters expose the already collected journey and subscription events", async () => {
  const html = await readFile(path.join(root, "portal_suite/site_src/activity.html"), "utf8");
  const options = new Set([...html.matchAll(/<option value="([^"]+)"/gu)].map((match) => match[1]));
  for (const type of ["membership_request", "report_request", "newsfeed_interaction", "newsfeed_topic_request", "journey_interaction", "form_confirmation", "report_text_view", "reward_checkin", "reward_claim"]) assert.ok(options.has(type), type);
});

test("stored analytics labels are sanitized at every admin response boundary", () => {
  const legacySourcePattern = new RegExp([
    "reportify",
    "nash[\\s._-]*ai",
    "macro[\\s._-]*gate",
    "portal[\\s._-]+suite",
    "two[\\s._-]*tigers",
  ].join("|"), "iu");
  const accumulator = __analyticsTest.emptyAnalyticsDayAccumulator(
    "2026-08-31",
    "admin@example.invalid",
    "_analytics/events",
    "0123456789abcdef01234567",
  );
  accumulator.referrers = { "reportify.cn": 2 };
  accumulator.utm_sources = { NashAI: 3, MacroGate: 4 };
  accumulator.acquisition_landings = {
    [JSON.stringify({
      source: "Portal Suite",
      landing_path: "/Reportify/research",
      page: "NashAI",
      report_id: "report-a",
      report_title: "MacroGate: Market outlook",
      utm_medium: "email",
      utm_campaign: "Twotigers",
      utm_term: "",
      utm_content: "",
    })]: 1,
  };

  const event = {
    type: "search",
    query: "Reportify market",
    source: "NashAI",
    report_id: "report-a",
    report_title: "MacroGate: Market outlook",
    visitor_id: "visitor-a",
    result_count: 2,
    ts: "2026-08-31T01:00:00.000Z",
  };
  const payload = {
    summary: __analyticsTest.publicAnalyticsDaySummary(accumulator, true),
    top_searches: __analyticsTest.analyticsTopSearches([event]),
    top_reports: __analyticsTest.analyticsTopReports([{ ...event, type: "report_open" }]),
    recent_event: __analyticsTest.publicAnalyticsEvent(event),
  };
  assert.doesNotMatch(JSON.stringify(payload), legacySourcePattern);
  assert.equal(payload.top_searches[0].query, "KC桌面 market");
  assert.equal(payload.top_reports[0].title, "Market outlook");
});
