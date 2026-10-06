const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
function extract(name) {
  const expression = new RegExp(`(?:async )?function ${name}\\(`);
  const start = worker.search(expression);
  assert.ok(start >= 0, `${name} exists`);
  const body = worker.indexOf("{", worker.indexOf(")", start));
  let depth = 0;
  for (let i = body; i < worker.length; i++) {
    if (worker[i] === "{") depth++;
    if (worker[i] === "}" && --depth === 0) return worker.slice(start, i + 1);
  }
  throw new Error(`Cannot extract ${name}`);
}
let reads = 0, matches = 0, puts = 0, now = 0;
const stored = new Map();
const cache = {
  async match(request) { matches++; const item = stored.get(request.url); return item && now - item.at < 30000 ? item.response.clone() : undefined; },
  async put(request, response) { puts++; stored.set(request.url, { response: response.clone(), at: now }); },
};
const sandbox = { Request, Response, Headers, URL, caches: { default: cache }, api: null,
  publicSourceText: String, cleanHotReportText: String, safePdfFilename: String, publicBrandText: String,
  listR2JsonObjects: async () => { reads++; return [{ id: "market-view:261005", title: "Market Views", size_bytes: 7500000, private_key: "not-public" }]; },
};
vm.runInNewContext(`
  const MARKET_VIEW_ID_PATTERN = /^market-view:(\\d{6})$/;
  const MARKET_VIEW_ITEM_PREFIX = "_market-views/items";
  const MARKET_VIEW_MAX_ITEMS = 1000;
  const MARKET_VIEW_REQUIRED_PLAN = "至少1个月会员";
  const MARKET_VIEW_MIN_MONTHS = 1;
  ${["allowedOrigin", "corsHeaders", "jsonResponse", "hotReportCacheStorage", "hotReportResponseIsCacheable",
    "marketViewDateKeyFromId", "marketViewDateIso", "publicMarketViewItem", "listMarketViewItems",
    "marketViewsListCacheRequest", "marketViewsListCacheResponse", "handleMarketViewsList"].map(extract).join("\n")}
  api = { handleMarketViewsList, marketViewsListCacheRequest };
`, sandbox);
const env = { ALLOWED_ORIGIN: "https://site.example,https://reader.example" };
const request = (headers = {}, suffix = "") => new Request(`https://site.example/api/market-views${suffix}`, { headers });
const call = (headers, suffix) => sandbox.api.handleMarketViewsList(request(headers, suffix), env);
(async () => {
  const first = await call();
  assert.equal(first.headers.get("X-Portal-Market-Views-Cache"), "MISS");
  assert.equal(first.headers.get("Cache-Control"), "public, max-age=30");
  assert.equal(reads, 1);
  assert.equal(puts, 1);
  const data = await first.json();
  assert.equal(data.items[0].id, "market-view:261005");
  assert.equal(data.items[0].private_key, undefined, "only the existing public item projection is cached");
  const second = await call();
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache"), "HIT");
  assert.equal(reads, 1, "an edge hit must not read R2 again");
  assert.deepEqual(await second.json(), data);
  assert.equal(second.headers.get("Vary"), "Origin");
  assert.equal(second.headers.get("Access-Control-Allow-Origin"), "https://site.example");
  const configured = await sandbox.api.handleMarketViewsList(request(), { ALLOWED_ORIGIN: "https://new.example" });
  assert.equal(configured.headers.get("Access-Control-Allow-Origin"), "https://new.example", "CORS is recomputed on hits");
  for (const headers of [{ Authorization: "Bearer fixture" }, { Cookie: "fixture=1" },
    { Origin: "https://reader.example" }, { Origin: "https://other.example" },
    { "Cache-Control": "no-cache" }, { "Cache-Control": "no-store" },
    { "Cache-Control": "max-age=0" }, { Pragma: "no-cache" }]) {
    const before = { reads, matches, puts };
    const response = await call(headers);
    assert.equal(response.status, 200);
    assert.equal(response.headers.get("Cache-Control"), "no-store");
    assert.equal(response.headers.get("X-Portal-Market-Views-Cache"), "BYPASS");
    assert.equal(reads, before.reads + 1);
    assert.equal(matches, before.matches);
    assert.equal(puts, before.puts);
    if (headers.Origin === "https://reader.example") assert.equal(response.headers.get("Access-Control-Allow-Origin"), headers.Origin);
  }
  assert.equal((await call({}, "?refresh=1")).headers.get("Cache-Control"), "no-store");
  for (const url of ["https://site.example/api/market-views/access", "https://site.example/api/market-views/pdf?id=market-view:261005"]) {
    assert.equal(sandbox.api.marketViewsListCacheRequest(new Request(url)), null);
  }
  assert.equal(sandbox.api.marketViewsListCacheRequest(new Request("https://site.example/api/market-views", { method: "POST" })), null);
  assert.notEqual(sandbox.api.marketViewsListCacheRequest(request()).url,
    sandbox.api.marketViewsListCacheRequest(new Request("https://different.example/api/market-views")).url,
    "different serving origins do not share cache keys");
  now = 30001;
  const beforeExpiry = reads;
  assert.equal((await call()).headers.get("X-Portal-Market-Views-Cache"), "MISS");
  assert.equal(reads, beforeExpiry + 1, "expired cache refreshes from R2");
  const originalR2 = sandbox.listR2JsonObjects;
  stored.clear();
  sandbox.listR2JsonObjects = async () => { throw new Error("unavailable storage"); };
  const beforeFailure = puts;
  const unavailable = await call();
  assert.equal(unavailable.status, 503);
  assert.equal(unavailable.headers.get("Cache-Control"), "no-store");
  assert.equal(puts, beforeFailure, "503 must never be cached");
  sandbox.listR2JsonObjects = originalR2;
  sandbox.caches = undefined;
  assert.equal((await call()).status, 200, "missing Cache API must preserve the directory");
  sandbox.caches = { default: { match: async () => { throw new Error("cache read failed"); }, put: async () => { throw new Error("cache write failed"); } } };
  assert.equal((await call()).status, 200, "cache read/write failures must preserve the directory");
  sandbox.caches = { default: { match: async () => new Response("private", { status: 200, headers: { "Set-Cookie": "fixture=1", "Cache-Control": "public, max-age=30", "Content-Type": "application/json" } }), put: async () => {} } };
  assert.equal((await (await call()).json()).items.length, 1, "untrusted non-public cached response is ignored");
  assert.doesNotMatch(extract("handleMarketViewsAccess"), /CacheRequest|cache\.put|public, max-age/);
  assert.doesNotMatch(extract("handleMarketViewsPdf"), /CacheRequest|cache\.put|public, max-age/);
  assert.match(app, /async function loadMarketViews\(force = false\)[\s\S]*?cache: force \? "no-store" : "default"/);
  const publicList = app.split("async function loadMarketViews(force = false)")[1].split('list.addEventListener("change"')[0];
  assert.match(publicList, /credentials: "omit"/);
  assert.doesNotMatch(publicList, /authHeaders\(/);
  assert.match(app, /data-market-reload[\s\S]*?await loadMarketViews\(true\)/);
  console.log("Market Views public directory cache: miss/hit, TTL, auth/origin/no-cache isolation and failure fallback passed");
})().catch((error) => { console.error(error); process.exitCode = 1; });
