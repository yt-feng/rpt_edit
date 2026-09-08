import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import test from "node:test";
import { researchNewsEvidence } from "../../workers/portal-suite-worker/src/research-news.js";

const NOW = Date.parse("2026-09-08T02:00:00Z");
const EIA = "https://www.eia.gov/rss/todayinenergy.xml";
const FED = "https://www.federalreserve.gov/feeds/feds_notes.xml";
// Real publisher RSS rows verified with normal HTTPS GET on 2026-09-08.
// EIA uses ISO-8859-1 XML; Fed uses UTF-8, CDATA, HTML and numeric entities.
const EIA_ROW = `<item><title>Weekly average load in ERCOT continues near record high</title>
  <link>https://www.eia.gov/todayinenergy/detail.php?id=68084</link>
  <pubDate>Thu, 03 Sep 2026 09:00:00 EST</pubDate>
  <description>Sustained high temperatures have contributed to persistently high electricity demand in the Electric Reliability Council of Texas (ERCOT), the regional transmission organization for most of the state.</description></item>`;
const FED_ROW = `<item><title>FEDS Note: Technology Shocks, the AI Boom, and the U.S. Current Account</title>
  <link><![CDATA[https://www.federalreserve.gov/econres/notes/feds-notes/technology-shocks-the-ai-boomandthe-u-s-current-account-20260714.html]]></link>
  <pubDate><![CDATA[Tue, 14 Jul 2026 14:05:00 GMT]]></pubDate>
  <description><![CDATA[<a href="https://www.federalreserve.gov/econres/giuseppe-fiori.htm">Giuseppe Fiori</a>, Colleen Lipa, and Erik Nuenninghoff<br><br>The current artificial intelligence (AI) investment boom in the United States provides a powerful boost to imports of high-technology capital goods. The AI buildout bears the hallmarks of an investment-specific technology shock&#8212;a process in which rapid technological progress makes each new generation of capital equipment significantly cheaper and more powerful than the last, but where reaping those efficiency gains requires continuous and substantial investment to acquire and deploy the new vintage of capital goods.]]></description></item>`;
const description = "Electricity investment continues to expand as utilities add new generation capacity and transmission infrastructure to meet growing industrial demand.";
const rss = (rows = "", encoding = "utf-8") => `<?xml version="1.0" encoding="${encoding}"?><rss version="2.0"><channel>${rows}</channel></rss>`;
const item = ({ title = "Electricity investment", url = "https://www.eia.gov/todayinenergy/detail.php?id=123", text = description, date = "Mon, 07 Sep 2026 09:00:00 GMT" } = {}) => `<item><title>${title}</title><link>${url}</link><description><![CDATA[${text}]]></description><pubDate>${date}</pubDate></item>`;
const response = (body, options = {}) => new Response(body, { headers: { "content-type": "text/xml" }, ...options });
const feeds = (eia = rss(), fed = rss()) => async (url) => response(url === EIA ? eia : fed);

test("verified EIA description becomes evidence with distinct retrieval and publication dates", async () => {
  const calls = [], budget = [];
  const output = await researchNewsEvidence({ query: "electricity", now: NOW, consumeBudget: (...args) => budget.push(args), fetchImpl: async (url, options) => {
    calls.push({ url, options });
    return response(url === EIA ? rss(EIA_ROW, "ISO-8859-1") : rss());
  } });
  assert.equal(output.status, "success");
  assert.deepEqual(calls.map((call) => call.url), [EIA, FED]);
  assert.ok(calls.every(({ options }) => options.redirect === "manual" && options.method === "GET"));
  assert.deepEqual(budget, [[1, "research-news-rss"], [1, "research-news-rss"]]);
  assert.equal(output.sources.length, 1);
  const source = output.sources[0];
  assert.equal(source.id, `news:${createHash("sha256").update(source.source_url).digest("hex")}`);
  assert.equal(source.observed_at, "2026-09-08T02:00:00.000Z");
  assert.equal(source.published_at, "2026-09-03T14:00:00.000Z");
  assert.equal(source.evidence_kind, "news_snippet");
  assert.equal(source.text_scope, "rss_description");
  assert.equal(source.publisher, "U.S. Energy Information Administration");
  assert.match(source.evidence[0].text, /^Sustained high temperatures/);
  assert.doesNotMatch(source.evidence[0].text, /^Weekly average load/);
});

test("verified Fed CDATA descriptions retain analytical text and decode entities without markup", async () => {
  const output = await researchNewsEvidence({ query: ["artificial intelligence", "investment"], now: NOW, fetchImpl: feeds(rss(), rss(FED_ROW)) });
  assert.equal(output.status, "success");
  assert.equal(output.sources[0].publisher, "Federal Reserve Board");
  assert.match(output.sources[0].evidence[0].text, /technology shock—a process/);
  assert.doesNotMatch(output.sources[0].evidence[0].text, /<|>|CDATA|href=|&#8212;/);
});

test("all core phrases must match and empty or title-repeated descriptions cannot enter evidence", async () => {
  for (const rows of [item({ text: "" }), item({ text: "eia.gov ENGLISH" }), item({ title: description, text: description }), item({ text: ". ".repeat(100) })]) {
    const output = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: feeds(rss(rows)) });
    assert.equal(output.status, "empty");
  }
  const output = await researchNewsEvidence({ query: ["electricity", "data center"], now: NOW, fetchImpl: feeds(rss(item())) });
  assert.equal(output.status, "empty");
  const doc = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: async () => new Response(JSON.stringify({ articles: [{ title: description, url: "https://www.eia.gov/news", domain: "eia.gov" }] }), { headers: { "content-type": "application/json" } }) });
  assert.equal(doc.status, "unavailable");
  assert.deepEqual(doc.sources, []);
});

test("invalid planner syntax does not issue any request", async () => {
  for (const query of ["", "人工智能", "electricity OR oil", "domain:example.com", '"electricity"', "(electricity)", "https://example.com", ["oil", "gas", "coal", "power"]]) {
    const output = await researchNewsEvidence({ query, fetchImpl: () => { throw new Error("must not fetch"); } });
    assert.equal(output.reason, "invalid_query");
  }
});

test("source links are fixed-publisher HTTPS URLs without credentials, private hosts or redirects", async () => {
  const invalid = ["http://www.eia.gov/news", "https://127.0.0.1/a", "https://localhost/a", "https://[::1]/a", "https://www.eia.gov.evil.com/a", "https://evil.com/a", "https://user:pass@www.eia.gov/a", "https://www.eia.gov:8443/a", "javascript:alert(1)", "//www.eia.gov/a", "https://www.eia.gov/todayinenergy/detail.php?id=", "https://www.eia.gov/"];
  const output = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: feeds(rss(invalid.map((url) => item({ url })).join(""))) });
  assert.equal(output.status, "empty");
  let calls = 0;
  const redirected = await researchNewsEvidence({ query: "electricity", fetchImpl: async () => { calls += 1; return response("", { status: 302, headers: { location: "https://evil.com" } }); } });
  assert.equal(redirected.reason, "redirect");
  assert.equal(calls, 2, "no redirect target or article URL may be fetched");
});

test("XSS content is removed, tracking URLs canonicalize and publishers are deduplicated", async () => {
  const eiaRows = Array.from({ length: 8 }, (_, i) => item({ url: `https://www.eia.gov/todayinenergy/detail.php?id=${i + 1}&amp;utm_source=test#fragment`, text: `<script>alert(1)</script><img src=x onerror=alert(1)>&lt;iframe&gt;bad&lt;/iframe&gt;${description}` })).join("");
  const fedRow = item({ url: "https://www.federalreserve.gov/econres/notes/news.html" });
  const output = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: feeds(rss(eiaRows), rss(fedRow)) });
  assert.equal(output.sources.length, 2);
  assert.equal(new Set(output.sources.map((source) => source.publisher)).size, output.sources.length);
  assert.ok(output.sources.length <= 4);
  for (const source of output.sources) {
    assert.doesNotMatch(source.evidence[0].text, /alert|onerror|iframe|<|>|bad/);
    assert.doesNotMatch(source.source_url, /utm_|#/);
  }
});

test("unknown publication date stays empty; stale and future publications are excluded", async () => {
  for (const date of ["Mon, 01 Jan 2024 09:00:00 GMT", "Thu, 10 Sep 2026 09:00:00 GMT"]) {
    const output = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: feeds(rss(item({ date }))) });
    assert.equal(output.status, "empty");
  }
  const output = await researchNewsEvidence({ query: "electricity", now: NOW, fetchImpl: feeds(rss(item({ date: "" }))) });
  assert.equal(output.sources[0].published_at, "");
  assert.equal(output.sources[0].observed_at, new Date(NOW).toISOString());
});

test("budget denial prevents upstream calls and one failed feed preserves the other", async () => {
  let calls = 0;
  const denied = await researchNewsEvidence({ query: "electricity", consumeBudget: () => false, fetchImpl: async () => { calls += 1; } });
  assert.equal(denied.reason, "budget_exhausted");
  assert.equal(calls, 0);
  let used = 0;
  const partial = await researchNewsEvidence({ query: "electricity", now: NOW, consumeBudget: () => { if (used++) throw new Error("budget"); }, fetchImpl: feeds(rss(EIA_ROW)) });
  assert.equal(partial.status, "success");
  assert.equal(partial.reason, "partial_feeds");
});

test("429, HTML, malformed XML and external entities fail without retries", async () => {
  for (const [reply, reason] of [
    [() => response("Too many requests", { status: 429 }), "rate_limited"],
    [() => response("<html>gateway failure</html>", { headers: { "content-type": "text/html" } }), "content_type"],
    [() => response("<rss><channel>"), "invalid_xml"],
    [() => response(`<!DOCTYPE rss [<!ENTITY secret SYSTEM "file:///etc/passwd">]>${rss(item())}`), "invalid_xml"],
  ]) {
    let calls = 0;
    const output = await researchNewsEvidence({ query: "electricity", fetchImpl: async () => { calls += 1; return reply(); } });
    assert.equal(output.status, "unavailable");
    assert.equal(output.reason, reason);
    assert.equal(calls, 2);
  }
});

test("declared and streamed oversize bodies are rejected before unbounded buffering", async () => {
  let cancelled = 0;
  const output = await researchNewsEvidence({ query: "electricity", fetchImpl: async () => response(new ReadableStream({
    pull(controller) { controller.enqueue(new Uint8Array(131073)); }, cancel() { cancelled += 1; },
  })) });
  assert.equal(output.reason, "response_too_large");
  assert.equal(cancelled, 2);
  const declared = await researchNewsEvidence({ query: "electricity", fetchImpl: async () => response("", { headers: { "content-type": "text/xml", "content-length": "262145" } }) });
  assert.equal(declared.reason, "response_too_large");
});

test("timeout bounds both a stalled fetch and a stalled response stream", async () => {
  const signals = [];
  const start = Date.now();
  const output = await researchNewsEvidence({ query: "electricity", timeoutMs: 10, fetchImpl: (_url, options) => { signals.push(options.signal); return new Promise(() => {}); } });
  assert.equal(output.reason, "timeout");
  assert.ok(Date.now() - start < 1000);
  assert.ok(signals.every((signal) => signal.aborted));
  let cancelled = 0;
  const body = await researchNewsEvidence({ query: "electricity", timeoutMs: 10, fetchImpl: async () => response(new ReadableStream({ cancel() { cancelled += 1; } })) });
  assert.equal(body.reason, "timeout");
  assert.equal(cancelled, 2);
});
