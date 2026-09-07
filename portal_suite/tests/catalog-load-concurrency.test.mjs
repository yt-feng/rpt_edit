import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { setImmediate } from "node:timers/promises";
import vm from "node:vm";

const source = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
const start = source.indexOf("async function loadCatalog(env) {");
const end = source.indexOf("\nfunction searchIndexUrl(", start);
assert.ok(start >= 0 && end > start);
const loadCatalogSource = source.slice(start, end);

function deferred() {
  let resolve;
  let reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
}

function fixture() {
  let release = "a".repeat(32);
  const reads = [];
  const context = vm.createContext({
    Date,
    Map,
    activeRuntimeDataRelease: async () => release,
    runtimeDataStateUrl: () => "https://portal.example.com/.well-known/edge-state",
    fetchStaticDataJson: async (env, filename, url, selectedRelease) => {
      const operation = deferred();
      reads.push({ env, filename, url, release: selectedRelease, ...operation });
      return operation.promise;
    },
  });
  vm.runInContext(`
    const CACHE_TTL_MS = 300000;
    let catalogCache = null;
    let catalogFetchedAt = 0;
    let catalogCacheBinding = null;
    let catalogCacheRelease = "";
    const catalogLoads = new Map();
    let latestCatalogLoad = null;
    ${loadCatalogSource}
    globalThis.load = loadCatalog;
    globalThis.pendingBindings = () => catalogLoads.size;
  `, context);
  const env = { REPORT_BUCKET: {}, CATALOG_URL: "https://portal.example.com/data/catalog.json" };
  return { env, reads, load: context.load, pendingBindings: context.pendingBindings, setRelease: (value) => { release = value; } };
}

test("concurrent cold catalog requests share one read and one parsed object", async () => {
  const f = fixture();
  const calls = Array.from({ length: 12 }, () => f.load(f.env));
  await setImmediate();
  assert.equal(f.reads.length, 1);
  const catalog = { items: [{ id: "report-a" }] };
  f.reads[0].resolve(catalog);
  const values = await Promise.all(calls);
  assert.ok(values.every((value) => value === catalog));
  assert.equal(await f.load(f.env), catalog);
  assert.equal(f.reads.length, 1);
  assert.equal(f.pendingBindings(), 0);
});

test("a failed shared catalog load is released so the next request can recover", async () => {
  const f = fixture();
  const calls = [f.load(f.env), f.load(f.env)];
  const outcomes = Promise.allSettled(calls);
  await setImmediate();
  const failure = new Error("storage unavailable");
  f.reads[0].reject(failure);
  assert.ok((await outcomes).every((result) => result.status === "rejected" && result.reason === failure));
  assert.equal(f.pendingBindings(), 0);
  const retry = f.load(f.env);
  await setImmediate();
  assert.equal(f.reads.length, 2);
  const recovered = { items: [] };
  f.reads[1].resolve(recovered);
  assert.equal(await retry, recovered);
});

test("an older release completing late cannot replace the current catalog cache", async () => {
  const f = fixture();
  const older = f.load(f.env);
  await setImmediate();
  f.setRelease("b".repeat(32));
  const newer = f.load(f.env);
  await setImmediate();
  assert.equal(f.reads.length, 2);
  const oldCatalog = { release: "a" };
  const newCatalog = { release: "b" };
  f.reads[1].resolve(newCatalog);
  assert.equal(await newer, newCatalog);
  f.reads[0].resolve(oldCatalog);
  assert.equal(await older, oldCatalog);
  assert.equal(await f.load(f.env), newCatalog);
  assert.equal(f.reads.length, 2, "late completion must not evict the current release");
  assert.equal(f.pendingBindings(), 0);
  f.setRelease("a".repeat(32));
  const rollback = f.load(f.env);
  await setImmediate();
  assert.equal(f.reads.length, 3, "an actual rollback resolves its own release");
  f.reads[2].resolve(oldCatalog);
  assert.equal(await rollback, oldCatalog);
});

test("different storage bindings never share pending catalog data", async () => {
  const f = fixture();
  const otherEnv = { ...f.env, REPORT_BUCKET: {} };
  const first = f.load(f.env);
  const second = f.load(otherEnv);
  await setImmediate();
  assert.equal(f.reads.length, 2);
  const firstCatalog = { tenant: "first" };
  const secondCatalog = { tenant: "second" };
  f.reads[1].resolve(secondCatalog);
  assert.equal(await second, secondCatalog);
  f.reads[0].resolve(firstCatalog);
  assert.equal(await first, firstCatalog);
  assert.equal(await f.load(otherEnv), secondCatalog);
  assert.equal(f.reads.length, 2);
  assert.equal(f.pendingBindings(), 0);
});
