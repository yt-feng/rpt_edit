import assert from "node:assert/strict";
import test from "node:test";
import { readResearchNewsSnapshot } from "../../workers/portal-suite-worker/src/research-news-snapshot.js";

const now = Date.parse("2026-09-08T02:00:00Z");
const groups = [{ role: "core", required: true, terms: ["data center", "data centers"] }, { role: "facet", terms: ["power"] }];
const row = (host = "publisher.com", extra = {}) => ({ id: `news:${"a".repeat(64)}`, title: "Data centers need more power", summary: "Data center developers say that access to grid power is slowing their construction plans, while they negotiate new generation capacity with utilities.", source_url: `https://${host}/article`, institution: host, observed_at: "2026-09-08T01:30:00Z", ...extra });
const bucketFor = (items, options = {}) => ({ calls: 0, async get() { this.calls++; const data = { schema_version: 1, updated_at: "2026-09-08T01:45:00Z", items, ...options }; const raw = JSON.stringify(data); return { size: new TextEncoder().encode(raw).length, body: new Response(raw).body }; } });

test("snapshot news uses genuine descriptions, diverse original sources, dates and one budgeted read", async () => {
  const bucket = bucketFor([row(), row(), row("secondpublisher.com"), row("thirdpublisher.com", { title: "Weather report", summary: "This weather forecast discusses rainfall and local temperatures, without any reference to industrial electricity use or infrastructure." })]);
  const spent = [];
  const result = await readResearchNewsSnapshot({ bucket, groups, now, consumeBudget: (...args) => spent.push(args) });
  assert.equal(result.status, "success"); assert.equal(result.sources.length, 2);
  assert.equal(result.sources[0].published_at, ""); assert.match(result.sources[0].observed_at, /^2026-09-08/u);
  assert.equal(result.sources[0].evidence_kind, "news_description");
  assert.match(result.sources[0].evidence[0].text, /negotiate/u);
  assert.deepEqual(spent, [[1, "research-news-snapshot"]]);
  await readResearchNewsSnapshot({ bucket, groups, now: now + 1000 });
  assert.equal(bucket.calls, 1);
});

test("snapshot rejects title-only, unsafe links, stale descriptions and excess size", async () => {
  const bucket = bucketFor([row("publisher.com", { summary: "Short title" }), row("publisher.com", { source_url: "javascript:alert(1)" }), row("publisher.com", { observed_at: "2026-08-01T00:00:00Z" }), row("localhost"), row("publisher.com", { source_url: "https://reader:secret@publisher.com/article" })]);
  assert.equal((await readResearchNewsSnapshot({ bucket, groups, now })).sources.length, 0);
  const oversized = { async get() { return { size: 3 * 1024 * 1024, text() { throw new Error("Must not read"); } }; } };
  assert.equal((await readResearchNewsSnapshot({ bucket: oversized, groups, now })).status, "unavailable");
  const denied = bucketFor([row()]);
  assert.equal((await readResearchNewsSnapshot({ bucket: denied, groups, now, consumeBudget: () => false })).reason, "budget");
  assert.equal(denied.calls, 0);
});

test("stale or malformed snapshots do not pretend news coverage exists", async () => {
  for (const options of [{ updated_at: "2026-08-01T00:00:00Z" }, { schema_version: 2 }]) {
    assert.equal((await readResearchNewsSnapshot({ bucket: bucketFor([row()], options), groups, now })).status, "unavailable");
  }
});
