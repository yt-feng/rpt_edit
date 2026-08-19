import assert from "node:assert/strict";
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

  const pages = ["index", "report", "doc", "delivery", "newsfeed", "activity", "privacy", "refund", "terms", "courses", "charts"];
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

  const autoPages = ["delivery", "activity", "privacy", "refund", "terms", "courses", "charts"];
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
  vm.runInNewContext(analytics, { window: manual.window, URL, URLSearchParams });
  await settleAnalytics();
  assert.equal(manual.requests.length, 0, "manual mode must not emit an automatic page_view");

  const automatic = analyticsBrowser();
  vm.runInNewContext(analytics, { window: automatic.window, URL, URLSearchParams });
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
    new Set(["newsletter", "direct"]),
  );
  assert.deepEqual(
    new Set(summary.acquisition_landings.filter((row) => row.source === "newsletter").map((row) => row.utm_content)),
    new Set(["creative-a", "creative-b"]),
  );
  assert.equal(summary.acquisition_landings.some((row) => row.report_id === "report-b"), false);
});
