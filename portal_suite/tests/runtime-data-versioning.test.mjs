import assert from "node:assert/strict";
import { createHash, webcrypto } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerUrl = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerUrl, "utf8");

function extractFunction(source, name) {
  const syncNeedle = `function ${name}(`;
  const asyncNeedle = `async function ${name}(`;
  const asyncStart = source.indexOf(asyncNeedle);
  const syncStart = source.indexOf(syncNeedle);
  const start = asyncStart >= 0 ? asyncStart : syncStart;
  assert.ok(start >= 0, `${name} must exist`);
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

function runtimeContext(extra = {}) {
  return vm.createContext({
    URL,
    Date,
    Error,
    JSON,
    Map,
    Object,
    Set,
    TextEncoder,
    Uint8Array,
    crypto: webcrypto,
    ...extra,
  });
}

function deferred() {
  let resolve;
  let reject;
  const promise = new Promise((resolvePromise, rejectPromise) => {
    resolve = resolvePromise;
    reject = rejectPromise;
  });
  return { promise, reject, resolve };
}

function canonicalJson(value) {
  if (Array.isArray(value)) return `[${value.map((item) => canonicalJson(item)).join(",")}]`;
  if (value && typeof value === "object") {
    return `{${Object.keys(value).sort().map((key) => `${JSON.stringify(key)}:${canonicalJson(value[key])}`).join(",")}}`;
  }
  return JSON.stringify(value);
}

function runtimeManifest(release, filename, value) {
  const body = JSON.stringify(value);
  const descriptor = {
    cache_control: "no-store",
    content_type: "application/json",
    sha256: createHash("sha256").update(body).digest("hex"),
    size: Buffer.byteLength(body),
  };
  const files = { [filename]: descriptor };
  const tree = `${filename}\0${canonicalJson(descriptor)}\n`;
  return {
    body,
    descriptor,
    manifest: {
      schema_version: 1,
      release_id: release,
      prefix: `edge-static/runtime-data/releases/${release}/`,
      tree_sha256: createHash("sha256").update(tree).digest("hex"),
      file_count: 1,
      files,
    },
  };
}

test("runtime object keys are immutable release namespaces with a true-legacy read path", () => {
  const context = runtimeContext();
  vm.runInContext(`
    const RUNTIME_RELEASE_PATTERN = /^[0-9a-f]{32}$/;
    ${extractFunction(workerSource, "staticDataObjectKey")}
    globalThis.keyFor = staticDataObjectKey;
  `, context);
  const release = "1".repeat(32);
  assert.equal(
    context.keyFor({}, "catalog.json", release),
    `edge-static/runtime-data/releases/${release}/catalog.json`,
  );
  assert.equal(context.keyFor({}, "catalog.json"), "edge-static/runtime-data/catalog.json");
  assert.equal(context.keyFor({}, "catalog.json", "latest"), "");
  assert.equal(context.keyFor({}, "not-allowed.json", release), "");
});

test("concurrent state reads share one request and freshness starts when the response completes", async () => {
  let now = 1_000;
  let fetchCount = 0;
  const timeouts = [];
  const first = deferred();
  const context = runtimeContext({
    Date: { now: () => now },
    fetchTextWithTimeout: async (_url, _init, timeoutMs) => {
      fetchCount += 1;
      timeouts.push(timeoutMs);
      if (fetchCount === 1) return first.promise;
      return {
        ok: true,
        status: 200,
        text: JSON.stringify({ schema_version: 1, slot: "b", release_id: "b".repeat(32) }),
      };
    },
  });
  vm.runInContext(`
    const RUNTIME_RELEASE_REFRESH_MS = 1000;
    const RUNTIME_RELEASE_STATE_TIMEOUT_MS = 1500;
    const RUNTIME_RELEASE_BACKOFF_MS = 4000;
    const RUNTIME_RELEASE_PATTERN = /^[0-9a-f]{32}$/;
    const runtimeReleaseStateCache = new Map();
    ${extractFunction(workerSource, "runtimeDataStateUrl")}
    ${extractFunction(workerSource, "activeRuntimeDataRelease")}
    globalThis.activeRelease = activeRuntimeDataRelease;
  `, context);
  const env = { CATALOG_URL: "https://portal.example.com/data/catalog.json" };
  const pending = Array.from({ length: 12 }, () => context.activeRelease(env));
  assert.equal(fetchCount, 1, "all concurrent callers must share one in-flight request");
  now = 2_000;
  first.resolve({
    ok: true,
    status: 200,
    text: JSON.stringify({ schema_version: 1, slot: "a", release_id: "a".repeat(32) }),
  });
  assert.deepEqual(await Promise.all(pending), Array(12).fill("a".repeat(32)));
  assert.deepEqual(timeouts, [1500]);

  now = 2_500;
  assert.equal(await context.activeRelease(env), "a".repeat(32));
  assert.equal(fetchCount, 1, "a fresh hit must not create a request");
  now = 3_001;
  assert.equal(await context.activeRelease(env), "b".repeat(32));
  assert.equal(fetchCount, 2, "freshness must be measured from completion time");
});

test("state failure clears the old release and applies a four-second unresolved backoff", async () => {
  let now = 10_000;
  let fetchCount = 0;
  let response = {
    ok: true,
    status: 200,
    text: JSON.stringify({ schema_version: 1, slot: "a", release_id: "a".repeat(32) }),
  };
  const context = runtimeContext({
    Date: { now: () => now },
    fetchTextWithTimeout: async () => {
      fetchCount += 1;
      return response;
    },
  });
  vm.runInContext(`
    const RUNTIME_RELEASE_REFRESH_MS = 1000;
    const RUNTIME_RELEASE_STATE_TIMEOUT_MS = 1500;
    const RUNTIME_RELEASE_BACKOFF_MS = 4000;
    const RUNTIME_RELEASE_PATTERN = /^[0-9a-f]{32}$/;
    const runtimeReleaseStateCache = new Map();
    ${extractFunction(workerSource, "runtimeDataStateUrl")}
    ${extractFunction(workerSource, "activeRuntimeDataRelease")}
    globalThis.activeRelease = activeRuntimeDataRelease;
  `, context);
  const env = { CATALOG_URL: "https://portal.example.com/data/catalog.json" };
  assert.equal(await context.activeRelease(env), "a".repeat(32));

  now += 1_001;
  response = { ok: true, status: 200, text: "{malformed" };
  assert.equal(await context.activeRelease(env), "", "malformed state must never return last-known A");
  assert.equal(fetchCount, 2);
  now += 3_999;
  assert.equal(await context.activeRelease(env), "");
  assert.equal(fetchCount, 2, "backoff must return unresolved without another fetch");

  now += 2;
  response = {
    ok: true,
    status: 200,
    text: JSON.stringify({ schema_version: 1, slot: "b", release_id: "b".repeat(32) }),
  };
  assert.equal(await context.activeRelease(env), "b".repeat(32));
  assert.equal(fetchCount, 3);
});

function installDataReaders(context) {
  vm.runInContext(`
    const RUNTIME_RELEASE_PATTERN = /^[0-9a-f]{32}$/;
    const RUNTIME_TREE_PATTERN = /^[0-9a-f]{64}$/;
    ${extractFunction(workerSource, "staticDataObjectKey")}
    ${extractFunction(workerSource, "readStaticDataObject")}
    ${extractFunction(workerSource, "runtimeCanonicalJson")}
    ${extractFunction(workerSource, "runtimeManifestTreeSha256")}
    ${extractFunction(workerSource, "runtimeDataManifestDescriptor")}
    ${extractFunction(workerSource, "readRuntimeDataReleaseObject")}
    ${extractFunction(workerSource, "activeRuntimeDataHttpsUrl")}
    ${extractFunction(workerSource, "fetchStaticDataJson")}
    globalThis.loadData = fetchStaticDataJson;
  `, context);
}

test("a versioned object is read only after its complete manifest and metadata verify", async () => {
  const release = "c".repeat(32);
  const filename = "catalog.json";
  const snapshot = runtimeManifest(release, filename, { source: "versioned" });
  const prefix = `edge-static/runtime-data/releases/${release}/`;
  const reads = [];
  const rows = new Map([
    [`${prefix}manifest.json`, { body: JSON.stringify(snapshot.manifest) }],
    [`${prefix}${filename}`, {
      body: snapshot.body,
      size: snapshot.descriptor.size,
      customMetadata: { sha256: snapshot.descriptor.sha256, "release-id": release },
      httpMetadata: { contentType: "application/json", cacheControl: "no-store" },
    }],
    ["edge-static/runtime-data/catalog.json", { body: JSON.stringify({ source: "legacy" }) }],
  ]);
  const bucket = {
    async get(key) {
      reads.push(key);
      const row = rows.get(key);
      if (!row) return null;
      return { ...row, text: async () => row.body };
    },
  };
  let httpCalls = 0;
  const context = runtimeContext({
    fetchJson: async () => {
      httpCalls += 1;
      return { source: "http" };
    },
  });
  installDataReaders(context);
  const env = { REPORT_BUCKET: bucket };
  const stateUrl = "https://portal.example.com/.well-known/edge-state?runtime-data=1";
  const fallbackUrl = "https://portal.example.com/data/catalog.json";

  assert.equal((await context.loadData(env, filename, fallbackUrl, release, stateUrl)).source, "versioned");
  assert.deepEqual(reads, [`${prefix}manifest.json`, `${prefix}${filename}`]);
  assert.equal(httpCalls, 0);

  rows.delete(`${prefix}manifest.json`);
  reads.length = 0;
  assert.equal((await context.loadData(env, filename, fallbackUrl, release, stateUrl)).source, "http");
  assert.deepEqual(reads, [`${prefix}manifest.json`], "a partial target must not be read without its manifest");

  rows.set(`${prefix}manifest.json`, {
    body: JSON.stringify({ ...snapshot.manifest, tree_sha256: "0".repeat(64) }),
  });
  reads.length = 0;
  assert.equal((await context.loadData(env, filename, fallbackUrl, release, stateUrl)).source, "http");
  assert.deepEqual(reads, [`${prefix}manifest.json`], "a bad manifest tree must not expose its target");
});

test("state-aware unresolved and versioned failures use same-origin HTTPS and never shared data", async () => {
  const release = "d".repeat(32);
  const prefix = `edge-static/runtime-data/releases/${release}/`;
  const reads = [];
  const bucket = {
    async get(key) {
      reads.push(key);
      if (key === "edge-static/runtime-data/catalog.json") {
        const body = JSON.stringify({ source: "legacy" });
        return { body, text: async () => body };
      }
      return null;
    },
  };
  let httpFails = false;
  let requestedUrl = "";
  const context = runtimeContext({
    fetchJson: async (url) => {
      requestedUrl = url;
      if (httpFails) throw new Error("active HTTPS unavailable");
      return { source: "http" };
    },
  });
  installDataReaders(context);
  const env = { REPORT_BUCKET: bucket };
  const stateUrl = "https://portal.example.com/.well-known/edge-state?runtime-data=1";
  const fallbackUrl = "https://portal.example.com/data/catalog.json";

  assert.equal((await context.loadData(env, "catalog.json", fallbackUrl, "", stateUrl)).source, "http");
  assert.equal(requestedUrl, fallbackUrl);
  assert.deepEqual(reads, [], "unresolved mode must not read shared R2");

  httpFails = true;
  await assert.rejects(context.loadData(env, "catalog.json", fallbackUrl, "", stateUrl), /active HTTPS unavailable/u);
  assert.deepEqual(reads, [], "HTTPS failure must fail closed without shared fallback");

  reads.length = 0;
  await assert.rejects(context.loadData(env, "catalog.json", fallbackUrl, release, stateUrl), /active HTTPS unavailable/u);
  assert.deepEqual(reads, [`${prefix}manifest.json`]);
  assert.equal(reads.includes("edge-static/runtime-data/catalog.json"), false);

  await assert.rejects(
    context.loadData(env, "catalog.json", "https://other.example.com/data/catalog.json", "", stateUrl),
    /not same-origin/u,
  );

  httpFails = false;
  reads.length = 0;
  assert.equal(
    (await context.loadData(env, "catalog.json", fallbackUrl, "", "")).source,
    "legacy",
    "only a true old configuration with no state URL may read shared data",
  );
  assert.deepEqual(reads, ["edge-static/runtime-data/catalog.json"]);
});

test("catalog, search, and rules cache identities follow A to B, rollback, and unresolved state", async () => {
  let activeRelease = "a".repeat(32);
  const loads = [];
  const stateUrl = "https://portal.example.com/.well-known/edge-state?runtime-data=1";
  const context = runtimeContext();
  context.activeRuntimeDataRelease = async () => activeRelease;
  context.runtimeDataStateUrl = () => stateUrl;
  context.fetchStaticDataJson = async (_env, filename, _url, release, selectedStateUrl) => {
    loads.push({ filename, release, selectedStateUrl });
    return { filename, release, sequence: loads.length };
  };
  vm.runInContext(`
    const CACHE_TTL_MS = 5 * 60 * 1000;
    let catalogCache = null;
    let catalogFetchedAt = 0;
    let catalogCacheBinding = null;
    let catalogCacheRelease = "";
    let searchIndexCache = null;
    let searchIndexFetchedAt = 0;
    let searchIndexCacheBinding = null;
    let searchIndexCacheRelease = "";
    let rulesCache = null;
    let rulesFetchedAt = 0;
    let rulesCacheBinding = null;
    let rulesCacheRelease = "";
    ${extractFunction(workerSource, "searchIndexUrl")}
    ${extractFunction(workerSource, "loadCatalog")}
    ${extractFunction(workerSource, "loadSearchIndex")}
    ${extractFunction(workerSource, "loadRules")}
    globalThis.catalog = loadCatalog;
    globalThis.search = loadSearchIndex;
    globalThis.rules = loadRules;
  `, context);
  const env = {
    REPORT_BUCKET: {},
    CATALOG_URL: "https://portal.example.com/data/catalog.json",
    SEARCH_INDEX_URL: "https://portal.example.com/data/search_index.json",
    PASSWORD_RULES_URL: "https://portal.example.com/data/password_rules.json",
  };
  const loadAll = async () => Promise.all([context.catalog(env), context.search(env), context.rules(env)]);

  await loadAll();
  await loadAll();
  assert.equal(loads.length, 3, "fresh same-release calls use all three logical caches");
  activeRelease = "b".repeat(32);
  await loadAll();
  activeRelease = "a".repeat(32);
  await loadAll();
  activeRelease = "";
  await loadAll();
  assert.deepEqual(loads.map((row) => row.release), [
    ...Array(3).fill("a".repeat(32)),
    ...Array(3).fill("b".repeat(32)),
    ...Array(3).fill("a".repeat(32)),
    ...Array(3).fill(""),
  ]);
  assert.ok(loads.every((row) => row.selectedStateUrl === stateUrl));
  assert.deepEqual(new Set(loads.map((row) => row.filename)), new Set([
    "catalog.json",
    "search_index.json",
    "password_rules.json",
  ]));
});
