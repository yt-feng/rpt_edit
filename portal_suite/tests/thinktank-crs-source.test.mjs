import assert from "node:assert/strict";
import cryptoModule from "node:crypto";
import fs from "node:fs";
import vm from "node:vm";
import test from "node:test";
import { fileURLToPath } from "node:url";

const workerPath = fileURLToPath(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url));
const source = fs.readFileSync(workerPath, "utf8")
  .replace(/^import\s*\{[\s\S]*?\}\s*from\s*["']\.\/source-lead-adapter\.js["'];\s*/m, "")
  .replace(/\bexport default\s*\{/, "globalThis.__workerExport = {");
const names = ["parseCrsRssRows", "parseCrsDetailRow", "crsIsoDate", "crsSearchRows", "thinkTankId", "thinkTankDate", "thinkTankObjectKeyForRow", "handleThinkTankSearch", "handleThinkTankItem", "handleThinkTankPdf", "warmThinkTankRows", "searchCacheKey", "fetchCrsMetadataText"];

function harness(fetchImpl) {
  const sandbox = { AbortController, ArrayBuffer, Blob, DOMException, FormData, Headers, Request, Response, TextDecoder, TextEncoder, URL, URLSearchParams, Uint8Array, atob, btoa, clearTimeout, console, crypto: cryptoModule.webcrypto, fetch: fetchImpl, setTimeout };
  vm.createContext(sandbox);
  vm.runInContext(source + `\nglobalThis.api = {${names.join(",")}};`, sandbox, { filename: workerPath });
  return { api: sandbox.api, sandbox, override(name, value) { sandbox.__replacement = value; vm.runInContext(`${name} = globalThis.__replacement`, sandbox); } };
}

class Bucket {
  constructor() { this.values = new Map(); this.writes = []; }
  async put(key, value) {
    this.writes.push(key);
    this.values.set(key, typeof value === "string" ? value : new Uint8Array(await new Response(value).arrayBuffer()));
  }
  async get(key) {
    const value = this.values.get(key);
    if (value === undefined) return null;
    return { text: async () => typeof value === "string" ? value : new TextDecoder().decode(value), body: new Response(value).body };
  }
  async head(key) { return this.values.has(key) ? {} : null; }
  ageJson(hours) {
    for (const [key, value] of this.values) {
      if (!key.endsWith(".json")) continue;
      const data = JSON.parse(value);
      data.cached_at = new Date(Date.now() - hours * 3600000).toISOString();
      this.values.set(key, JSON.stringify(data));
    }
  }
}
const rssItem = (id, title, date, link = `https://www.everycrsreport.com/reports/${id}.html`) => `<item><title>${title}</title><link>${link}</link><pubDate>${date}</pubDate></item>`;
const feed = `<rss><channel>${rssItem("R49001", "Old title", "Wed, 02 Sep 2026 12:00:00 GMT")}${rssItem("IF13121", "China &amp; trade", "Fri, 04 Sep 2026 12:00:00 GMT")}${rssItem("R49001", "Updated title", "Sat, 05 Sep 2026 12:00:00 GMT")}${rssItem("EVIL", "Untrusted locator", "Sun, 06 Sep 2026 12:00:00 GMT", "https://other.invalid/reports/EVIL.html")}</channel></rss>`;
const report = (sha = "a".repeat(40)) => ({ number: "IF13121", versions: [{ date: "2026-09-04", title: "China trade report", formats: [{ format: "PDF", filename: `files/2026-09-04_IF13121_${sha}.pdf`, sha1: sha, url: "https://www.congress.gov/source.pdf" }] }, { date: "2025-01-02", title: "Old edition", formats: [{ format: "PDF", filename: "files/old.pdf", sha1: "b".repeat(40) }] }] });
const configHtml = "var search = instantsearch({ appId: '2C677PFU7I', apiKey: 'aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa', indexName: 'everycrsreport' });";
const json = (value) => new Response(JSON.stringify(value), { headers: { "Content-Type": "application/json" } });
const request = (route) => new Request(`https://api.example.invalid${route}`);

test("CRS metadata discovery, cached search and authorized versioned downloads", async () => {
  const requests = [];
  let unavailable = false;
  const h = harness(async (url, init) => {
    assert.equal(init.redirect, "manual", "workerd rejects redirect:error before issuing an upstream request");
    requests.push(String(url));
    if (unavailable) return new Response("Unavailable", { status: 503 });
    assert.equal(String(url), "https://www.everycrsreport.com/rss.xml");
    return new Response(feed);
  });
  h.override("thinkTankArchiveRows", async () => { throw new Error("Default discovery must not read GitHub"); });
  h.override("thinkTankWechatTitleMap", async () => { throw new Error("Default discovery must not scan WeChat titles"); });
  const rows = h.api.parseCrsRssRows(feed);
  assert.equal(rows.length, 2);
  assert.equal(rows[0].title, "Updated title", "newest duplicate wins even when RSS is ascending");
  assert.equal(h.api.crsIsoDate("Apr. 7, 2008"), "2008-04-07", "upstream display dates must not shift with local timezone");
  assert.equal(h.api.thinkTankDate({ crs_report_id: "95-001", published: "1995-04-07" }), "1995-04-07");
  assert.equal(h.api.thinkTankDate({ crs_report_id: "95-001", published: "1995-04-07T00:00:00" }), "1995-04-07");
  const bucket = new Bucket();
  const env = { REPORT_BUCKET: bucket };
  let scheduled = 0;
  const ctx = { waitUntil() { scheduled += 1; } };
  const first = await (await h.api.handleThinkTankSearch(request("/thinktank/search"), env, ctx)).json();
  assert.equal(first.items[0].id, "thinktank:crs-R49001");
  assert.match(first.items[0].institution, /美国国会研究处/);
  assert.equal(first.total, 2);
  assert.equal(first.has_more, false);
  assert.equal(requests.length, 1, "default discovery makes one upstream metadata request");
  assert.equal(scheduled, 0, "default discovery must not schedule warmers");
  assert.ok(bucket.writes.every((key) => key.endsWith(".json")), "list requests only cache metadata");
  assert.ok(!JSON.stringify(first).includes("pdf_url"));
  const second = await (await h.api.handleThinkTankSearch(request("/thinktank/search"), env, ctx)).json();
  assert.equal(second.cache_status, "fresh");
  assert.equal(requests.length, 1);
  const pageTwo = await (await h.api.handleThinkTankSearch(request("/thinktank/search?page=2"), env)).json();
  assert.equal(pageTwo.items.length, 0);
  assert.equal(requests.length, 1, "RSS metadata is shared across pages");
  bucket.ageJson(1);
  const storedBeforeFailure = [...bucket.values.entries()].map(([key, value]) => [key, value]);
  unavailable = true;
  const stale = await (await h.api.handleThinkTankSearch(request("/thinktank/search"), env)).json();
  assert.equal(stale.items.length, 2);
  assert.match(stale.warning, /缓存/);
  assert.deepEqual([...bucket.values.entries()], storedBeforeFailure, "degraded results never replace the last complete cache");
  bucket.ageJson(8 * 24);
  const expired = await (await h.api.handleThinkTankSearch(request("/thinktank/search"), env)).json();
  assert.equal(expired.items.length, 0, "stale fallback is bounded to seven days");
  assert.equal(expired.cache_status, "miss");
  unavailable = false;
  const noBucket = await (await h.api.handleThinkTankSearch(request("/thinktank/search"), {})).json();
  assert.equal(noBucket.items.length, 2, "metadata still works when cache storage is unavailable");

  let crsDown = true;
  let archiveCalls = 0;
  const searchRequests = [];
  const search = harness(async (value) => {
    const url = new URL(value);
    searchRequests.push(url);
    if (url.pathname === "/search.html") return new Response(configHtml);
    assert.equal(url.host, "2c677pfu7i-dsn.algolia.net");
    assert.equal(url.searchParams.get("query"), "china");
    assert.equal(url.searchParams.get("hitsPerPage"), "30");
    assert.equal(url.searchParams.get("page"), "1");
    assert.ok(!url.searchParams.get("attributesToRetrieve").includes("summary"));
    if (crsDown) return new Response("Unavailable", { status: 503 });
    return json({ hits: Array.from({ length: 30 }, (_, i) => ({ title: `China report ${i + 30}`, url: `/reports/R${49030 + i}.html`, reportNumber: `R${49030 + i}`, date: "Apr. 7, 2008" })), nbHits: 90, nbPages: 3 });
  });
  search.override("thinkTankArchiveSearchPayload", async (_env, query, page) => {
    archiveCalls += 1;
    assert.equal(query, "china");
    assert.equal(page, 2);
    return { items: [{ id: "thinktank:abc123", title: "Archived China report", source: "thinktank" }], total: 31, has_more: false };
  });
  const searchBucket = new Bucket();
  const searchEnv = { REPORT_BUCKET: searchBucket };
  const searchUrl = request("/thinktank/search?q=china&page=2");
  const partial = await (await search.api.handleThinkTankSearch(searchUrl, searchEnv)).json();
  assert.equal(partial.items[0].id, "thinktank:abc123");
  assert.ok(partial.warning);
  assert.equal(partial.cache_status, "partial");
  assert.equal(searchBucket.writes.filter((key) => key.startsWith("_search-cache/")).length, 0);
  crsDown = false;
  const combined = await (await search.api.handleThinkTankSearch(searchUrl, searchEnv)).json();
  assert.equal(combined.items.length, 31);
  assert.equal(combined.items[0].id, "thinktank:crs-R49030");
  assert.equal(combined.items[0].date, "2008-04-07");
  assert.equal(combined.items[30].id, "thinktank:abc123");
  assert.equal(combined.total, 121);
  assert.equal(combined.page_size, 60);
  assert.equal(combined.has_more, true);
  assert.equal(archiveCalls, 2, "partial errors must permit recovery on the next request");
  const callsBeforeCache = searchRequests.length;
  await search.api.handleThinkTankSearch(searchUrl, searchEnv);
  assert.equal(archiveCalls, 2);
  assert.equal(searchRequests.length, callsBeforeCache);
  assert.ok(searchBucket.writes.some((key) => key.startsWith("_search-cache/thinktank-crs-v1/")));

  const downloads = [];
  const downloadBucket = new Bucket();
  let metadataStatus = 200;
  const download = harness(async (url) => {
    downloads.push(String(url));
    if (String(url).endsWith(".json")) return metadataStatus === 200 ? json(report()) : new Response("Unavailable", { status: metadataStatus });
    assert.equal(String(url), `https://www.everycrsreport.com/files/2026-09-04_IF13121_${"a".repeat(40)}.pdf`);
    return new Response("%PDF-1.4\n%%EOF", { headers: { "Content-Type": "application/pdf" } });
  });
  download.override("thinkTankArchiveRows", async () => { throw new Error("CRS detail must not read GitHub"); });
  download.override("thinkTankWechatTitleMap", async () => { throw new Error("CRS detail must not scan WeChat titles"); });
  let allowed = false;
  let finalized = 0;
  let hotArchives = 0;
  download.override("accountDownloadDecision", async () => ({ allowed, status: 402 }));
  download.override("finalizeAccountDownloadDecision", async () => { finalized += 1; return { ok: true }; });
  download.override("scheduleHotReportArchive", () => { hotArchives += 1; });
  const downloadEnv = { REPORT_BUCKET: downloadBucket };
  const detail = await (await download.api.handleThinkTankItem(request("/thinktank/item?id=thinktank:crs-IF13121"), downloadEnv)).json();
  assert.equal(detail.item.id, "thinktank:crs-IF13121");
  assert.equal(downloads.length, 1);
  assert.ok(downloads.every((url) => url.endsWith(".json")));
  const downloadRequest = request("/thinktank/pdf?id=thinktank:crs-IF13121");
  const denied = await download.api.handleThinkTankPdf(downloadRequest, downloadEnv, ctx);
  assert.equal(denied.status, 402);
  assert.equal(downloads.length, 1, "denied downloads must not fetch a PDF");
  assert.equal(finalized, 0);
  allowed = true;
  const delivered = await download.api.handleThinkTankPdf(downloadRequest, downloadEnv, ctx);
  assert.equal(delivered.status, 200);
  assert.equal(delivered.headers.get("content-type"), "application/pdf");
  assert.match(await delivered.text(), /^%PDF/);
  assert.equal(downloads.length, 2, "PDF is fetched only on the first authorized download");
  assert.equal(finalized, 1);
  assert.equal(hotArchives, 1);
  const oldRow = download.api.parseCrsDetailRow(report(), "IF13121");
  const newRow = download.api.parseCrsDetailRow(report("c".repeat(40)), "IF13121");
  assert.equal(download.api.thinkTankId(oldRow), download.api.thinkTankId(newRow), "report identity stays stable across updates");
  assert.notEqual(download.api.thinkTankObjectKeyForRow(oldRow), download.api.thinkTankObjectKeyForRow(newRow), "PDF cache identity follows the source version");
  await download.api.handleThinkTankPdf(downloadRequest, downloadEnv, ctx);
  assert.equal(downloads.length, 2);
  assert.equal(finalized, 2, "cached downloads still pass account finalization");
  const foreignPdf = report();
  foreignPdf.versions[0].formats[0].filename = "https://other.invalid/private.pdf";
  assert.equal(download.api.parseCrsDetailRow(foreignPdf, "IF13121"), null);
  assert.equal(download.api.parseCrsDetailRow(report(), "IF00000"), null);
  metadataStatus = 404;
  assert.equal((await download.api.handleThinkTankItem(request("/thinktank/item?id=thinktank:crs-IF99999"), downloadEnv)).status, 404);
  metadataStatus = 503;
  assert.equal((await download.api.handleThinkTankItem(request("/thinktank/item?id=thinktank:crs-IF99999"), downloadEnv)).status, 503);
  assert.equal((await download.api.handleThinkTankPdf(request("/thinktank/pdf?id=thinktank:crs-IF99999"), downloadEnv)).status, 503);
  downloadBucket.ageJson(1);
  const staleNumberSearch = await download.api.crsSearchRows(downloadEnv, "IF13121", 1);
  assert.equal(staleNumberSearch.rows[0].crs_report_id, "IF13121");
  assert.equal(staleNumberSearch.stale, true, "number lookups must preserve metadata fallback status instead of caching it as fresh search");
  assert.ok(downloads.slice(2).every((url) => url.endsWith(".json")), "number searches only request report metadata");
  let warmCalls = 0;
  download.override("cacheThinkTankPdf", async (_env, row) => { warmCalls += 1; assert.ok(!row.crs_report_id); return { ok: true }; });
  await download.api.warmThinkTankRows(downloadEnv, [oldRow, { title: "Legacy", pdf_url: "https://legacy.invalid/report.pdf" }]);
  assert.equal(warmCalls, 1, "CRS rows never enter PDF warming, including scheduled warmers");

  const huge = harness(async () => new Response("x".repeat(512 * 1024 + 1)));
  await assert.rejects(huge.api.fetchCrsMetadataText("https://www.everycrsreport.com/rss.xml"), /size limit/);
  let redirectRequests = 0;
  const redirected = harness(async (_url, init) => {
    redirectRequests += 1;
    assert.equal(init.redirect, "manual");
    return new Response(null, { status: 302, headers: { Location: "https://other.invalid/feed.xml" } });
  });
  await assert.rejects(redirected.api.fetchCrsMetadataText("https://www.everycrsreport.com/rss.xml"), /302/);
  assert.equal(redirectRequests, 1, "metadata redirects are rejected without following an untrusted destination");
  console.log("CRS source tests passed: bounded RSS/search metadata, caches and fallback, dates and IDs, independent pagination, authorized/versioned PDF downloads, and no CRS warming.");
});
