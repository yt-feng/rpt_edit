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
const constructedPolicies = [];
class ObservedResponse extends Response {
  constructor(body, init) {
    super(body, init);
    constructedPolicies.push(this.headers.get("Cache-Control"));
  }
}
const stored = new Map();
const cache = {
  async match(request) { matches++; const item = stored.get(request.url); return item && now - item.at < 30000 ? item.response.clone() : undefined; },
  async put(request, response) { puts++; stored.set(request.url, { response: response.clone(), at: now }); },
};
class CacheClock extends Date { static now() { return 1700000000000 + now; } }
const sandbox = { Request, Response: ObservedResponse, Headers, URL, Date: CacheClock, caches: { default: cache }, api: null,
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
    "marketViewsListCacheRequest", "marketViewsListCacheEntryIsValid", "marketViewsListCacheResponse", "handleMarketViewsList"].map(extract).join("\n")}
  api = { handleMarketViewsList, marketViewsListCacheRequest, marketViewsListCacheEntryIsValid };
`, sandbox);
const env = { ALLOWED_ORIGIN: "https://site.example,https://reader.example" };
const request = (headers = {}, suffix = "") => new Request(`https://site.example/api/market-views${suffix}`, { headers });
const call = (headers, suffix) => sandbox.api.handleMarketViewsList(request(headers, suffix), env);
(async () => {
  const first = await call();
  assert.equal(first.headers.get("X-Portal-Market-Views-Cache"), "MISS");
  assert.equal(first.headers.get("Cache-Control"), "public, max-age=30");
  assert.equal(constructedPolicies[0], "public, max-age=30", "the stored response must be constructed with its final public cache policy");
  assert.equal(first.headers.get("X-Portal-Market-Views-Cache-Read"), "miss");
  assert.equal(first.headers.get("X-Portal-Market-Views-Cache-Store"), "put_ok");
  assert.equal(reads, 1);
  assert.equal(puts, 1);
  assert.match(sandbox.api.marketViewsListCacheRequest(request()).url, /public-list-v2/);
  const storedEntry = stored.values().next().value.response;
  assert.equal(storedEntry.headers.get("X-Portal-Market-Views-Cache-Entry"), "public-list-v2");
  assert.equal(storedEntry.headers.get("X-Portal-Market-Views-Cache-Expires"), String(CacheClock.now() + 30000));
  for (const name of ["X-Portal-Market-Views-Cache-Entry", "X-Portal-Market-Views-Cache-Expires"]) {
    assert.equal(first.headers.get(name), null, "cache metadata must not be sent to readers");
  }
  const data = await first.json();
  assert.equal(data.items[0].id, "market-view:261005");
  assert.equal(data.items[0].private_key, undefined, "only the existing public item projection is cached");
  const second = await call();
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache"), "HIT");
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache-Read"), "hit");
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache-Store"), "not_attempted");
  assert.equal(reads, 1, "an edge hit must not read R2 again");
  assert.deepEqual(await second.json(), data);
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache-Entry"), null);
  assert.equal(second.headers.get("X-Portal-Market-Views-Cache-Expires"), null);
  // Real edge caches may omit public or normalize max-age; the private cache
  // marker and exact expiry are the storage contract, not echoed policy text.
  for (const policy of [null, "max-age=25", "max-age=300", "public, max-age=29"]) {
    sandbox.caches = { default: {
      match: async () => { const cached = await cache.match(sandbox.api.marketViewsListCacheRequest(request())); if (policy === null) cached.headers.delete("Cache-Control"); else cached.headers.set("Cache-Control", policy); return cached; },
      put: cache.put,
    } };
    const before = reads;
    const normalized = await call();
    assert.equal(normalized.headers.get("X-Portal-Market-Views-Cache"), "HIT");
    assert.equal(normalized.headers.get("Cache-Control"), "public, max-age=30");
    assert.equal(reads, before, "normalized cache headers must not trigger a fresh R2 read");
  }
  sandbox.caches = { default: cache };
  now = 5000;
  assert.equal((await call()).headers.get("Cache-Control"), "public, max-age=25", "browser freshness must not outlive the original entry");
  now = 0;
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
    assert.equal(response.headers.get("X-Portal-Market-Views-Cache-Read"), "bypass");
    assert.equal(response.headers.get("X-Portal-Market-Views-Cache-Store"), "not_attempted");
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
  const noCache = await call();
  assert.equal(noCache.status, 200, "missing Cache API must preserve the directory");
  assert.equal(noCache.headers.get("X-Portal-Market-Views-Cache-Read"), "bypass");
  assert.equal(noCache.headers.get("X-Portal-Market-Views-Cache-Store"), "not_attempted");
  sandbox.caches = { default: { match: async () => { throw new Error("cache read failed"); }, put: async () => { throw new Error("cache write failed"); } } };
  const failedCache = await call();
  assert.equal(failedCache.status, 200, "cache read/write failures must preserve the directory");
  assert.equal(failedCache.headers.get("X-Portal-Market-Views-Cache-Read"), "read_error");
  assert.equal(failedCache.headers.get("X-Portal-Market-Views-Cache-Store"), "put_error");
  assert.doesNotMatch(JSON.stringify([...failedCache.headers]), /cache read failed|cache write failed/);
  assert.equal((await failedCache.json()).items.length, 1);
  sandbox.caches = { default: { match: async () => undefined, put: async () => {} } };
  const silentNoop = await call();
  assert.equal(silentNoop.headers.get("X-Portal-Market-Views-Cache"), "MISS");
  assert.equal(silentNoop.headers.get("X-Portal-Market-Views-Cache-Store"), "put_ok");
  assert.equal((await call()).headers.get("X-Portal-Market-Views-Cache"), "MISS", "a put that returns successfully must not be described as a hit");
  sandbox.caches = { default: { match: async () => new Response("private", { status: 200, headers: { "Set-Cookie": "fixture=1", "Cache-Control": "public, max-age=30", "Content-Type": "application/json" } }), put: async () => {} } };
  const rejectedCache = await call();
  assert.equal(rejectedCache.headers.get("X-Portal-Market-Views-Cache-Read"), "rejected");
  assert.equal((await rejectedCache.json()).items.length, 1, "untrusted non-public cached response is ignored");
  const makeEntry = (changes = {}, status = 200) => new Response("{}", { status, headers: {
    "Content-Type": "application/json", "Cache-Control": "public, max-age=30",
    "X-Portal-Market-Views-Cache-Entry": "public-list-v2",
    "X-Portal-Market-Views-Cache-Expires": String(CacheClock.now() + 30000), ...changes,
  } });
  assert.equal(sandbox.api.marketViewsListCacheEntryIsValid(makeEntry()), true);
  for (const changes of [
    { "X-Portal-Market-Views-Cache-Entry": "" },
    { "X-Portal-Market-Views-Cache-Entry": "public-list-v1" },
    { "X-Portal-Market-Views-Cache-Expires": String(CacheClock.now()) },
    { "X-Portal-Market-Views-Cache-Expires": String(CacheClock.now() - 1) },
    { "X-Portal-Market-Views-Cache-Expires": String(CacheClock.now() + 30001) },
    { "X-Portal-Market-Views-Cache-Expires": "1700000030junk" },
    { "X-Portal-Market-Views-Cache-Expires": "9007199254740993" },
    { "Cache-Control": "private, max-age=30" },
    { "Cache-Control": "public, no-store" },
    { "Cache-Control": 'private="Set-Cookie"' },
    { "Set-Cookie": "fixture=1" },
    { "Content-Type": "text/html" },
    { "Content-Type": "application/jsonp" },
  ]) {
    const forged = makeEntry(changes);
    assert.equal(sandbox.api.marketViewsListCacheEntryIsValid(forged), false, JSON.stringify(changes));
    sandbox.caches = { default: { match: async () => forged.clone(), put: async () => {} } };
    const rejected = await call();
    assert.equal(rejected.headers.get("X-Portal-Market-Views-Cache-Read"), "rejected");
    assert.equal(rejected.headers.get("X-Portal-Market-Views-Cache"), "MISS");
  }
  assert.equal(sandbox.api.marketViewsListCacheEntryIsValid(makeEntry({}, 503)), false);
  assert.doesNotMatch(extract("handleMarketViewsAccess"), /CacheRequest|cache\.put|public, max-age/);
  assert.doesNotMatch(extract("handleMarketViewsPdf"), /CacheRequest|cache\.put|public, max-age/);
  assert.match(app, /async function loadMarketViews\(force = false\)[\s\S]*?cache: force \? "no-store" : "default"/);
  const publicList = app.split("async function loadMarketViews(force = false)")[1].split('list.addEventListener("change"')[0];
  assert.match(publicList, /credentials: "omit"/);
  assert.doesNotMatch(publicList, /authHeaders\(/);
  assert.match(app, /data-market-reload[\s\S]*?await loadMarketViews\(true\)/);
  console.log("Market Views public directory cache: miss/hit, TTL, auth/origin/no-cache isolation and failure fallback passed");
})().catch((error) => { console.error(error); process.exitCode = 1; });
