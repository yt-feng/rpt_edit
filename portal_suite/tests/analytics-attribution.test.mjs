import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const { default: worker } = await import(workerPath);

test("analytics client ships session and campaign context on every static page", async () => {
  const analytics = await readFile(path.join(root, "portal_suite/site_src/assets/analytics.js"), "utf8");
  for (const field of [
    "session_id", "first_seen_at", "is_returning", "landing_path",
    "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content",
    "navigation_type", "device_type", "bot_hint",
  ]) assert.match(analytics, new RegExp(field, "u"), `${field} must be collected`);

  const pages = ["index", "report", "doc", "delivery", "newsfeed", "activity", "privacy", "refund", "terms", "courses"];
  for (const page of pages) {
    const html = await readFile(path.join(root, `portal_suite/site_src/${page}.html`), "utf8");
    assert.match(html, /assets\/analytics\.js/u, `${page}.html must load the shared analytics client`);
  }
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
        first_seen_at: "2026-08-09T01:00:00.000Z",
        is_returning: true,
        utm_source: "newsletter",
        utm_medium: "email",
        utm_campaign: "daily-research",
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
  assert.equal(event.utm_source, "newsletter");
  assert.equal(event.referrer_host, "search.example");
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
  assert.match(workerSource, /pathname === "\/account-admin\/analytics-day-summary"/u);
  assert.match(workerSource, /unique_visitor_count/u);
  assert.match(workerSource, /top_referrer_hosts/u);
  assert.match(workerSource, /bot_hints/u);
  const start = workerSource.indexOf("function publicAnalyticsDaySummary(");
  const end = workerSource.indexOf("\n}\n\nasync function advanceAnalyticsDaySummary", start);
  const publicContract = workerSource.slice(start, end);
  assert.doesNotMatch(publicContract, /ip_hash|visitor_keys\s*:/u, "the public daily summary must not return identifiers");
});
