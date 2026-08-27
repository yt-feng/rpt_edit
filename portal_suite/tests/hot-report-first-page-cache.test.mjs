import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

const INDEX_KEY = "_hot-reports/indexes/public-v2.json";
const STALE_KEY = "_hot-reports/indexes/public-v2-stale.json";

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.getCount = 0;
    this.headCount = 0;
  }

  seedIndex(title) {
    this.rows.set(INDEX_KEY, JSON.stringify({
      version: 2,
      generation: "0123456789abcdef",
      stale_marker: "",
      updated_at: "2026-08-27T12:00:00.000Z",
      items: [{
        id: "hot:0123456789abcdef",
        source: "hot",
        title,
        title_cn: "",
        institution: "KC",
        date: "2026-08-27",
        description: "",
        filename: "report.pdf",
        size_bytes: 42,
        sort_order: 1,
        created_at: "2026-08-27T12:00:00.000Z",
        updated_at: "2026-08-27T12:00:00.000Z",
        required_plan: "member",
        required_months: 3,
      }],
    }));
  }

  seedStaleMarker() {
    this.rows.set(STALE_KEY, JSON.stringify({
      version: 2,
      generation: "fedcba9876543210",
      marked_at: "2026-08-27T12:01:00.000Z",
    }));
  }

  object(body) {
    if (body === undefined) return null;
    return {
      etag: '"memory-index"',
      customMetadata: {},
      async text() { return body; },
    };
  }

  async get(key) {
    this.getCount += 1;
    return this.object(this.rows.get(key));
  }

  async head(key) {
    this.headCount += 1;
    return this.object(this.rows.get(key));
  }
}

class MemoryCache {
  constructor({ throwMatch = false, throwPut = false } = {}) {
    this.rows = new Map();
    this.throwMatch = throwMatch;
    this.throwPut = throwPut;
  }

  async match(request) {
    if (this.throwMatch) throw new Error("cache match unavailable");
    const response = this.rows.get(request.url);
    return response ? response.clone() : undefined;
  }

  put(request, response) {
    if (this.throwPut) throw new Error("cache put unavailable");
    this.rows.set(request.url, response.clone());
    return Promise.resolve();
  }
}

function executionContext() {
  const pending = [];
  return {
    pending,
    waitUntil(promise) { pending.push(promise); },
  };
}

test("the public hot-report first page caches once while forced and filtered requests stay live", async () => {
  const previousCaches = Object.getOwnPropertyDescriptor(globalThis, "caches");
  Object.defineProperty(globalThis, "caches", {
    configurable: true,
    value: { default: new MemoryCache() },
  });
  try {
    const bucket = new MemoryR2();
    bucket.seedIndex("Cached A");
    const env = {
      REPORT_BUCKET: bucket,
      ALLOWED_ORIGIN: "https://portal.example.invalid",
    };
    const ctx = executionContext();
    const first = await worker.fetch(
      new Request("https://www.portal.example.invalid/api/hot-reports?limit=24"),
      env,
      ctx,
    );
    assert.equal(first.status, 200);
    assert.equal(first.headers.get("x-portal-hot-report-cache"), "MISS");
    assert.equal(first.headers.get("cache-control"), "public, max-age=30, stale-while-revalidate=300");
    assert.equal(first.headers.get("access-control-allow-origin"), "https://portal.example.invalid");
    assert.equal((await first.json()).items[0].title, "Cached A");
    await Promise.all(ctx.pending);
    const durableReads = { get: bucket.getCount, head: bucket.headCount };

    const withAdminCookie = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports", {
        headers: { cookie: "portal_admin_token=present" },
      }),
      env,
      executionContext(),
    );
    assert.equal(withAdminCookie.headers.get("x-portal-hot-report-cache"), "HIT");
    assert.equal((await withAdminCookie.json()).items[0].title, "Cached A");
    assert.deepEqual({ get: bucket.getCount, head: bucket.headCount }, durableReads);

    bucket.seedIndex("Live B");
    const forcedByCacheControl = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24", {
        headers: { "cache-control": "no-cache" },
      }),
      env,
      executionContext(),
    );
    assert.equal(forcedByCacheControl.headers.get("x-portal-hot-report-cache"), null);
    assert.equal((await forcedByCacheControl.json()).items[0].title, "Live B");

    bucket.seedIndex("Live C");
    const forcedByPragma = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24", {
        headers: { pragma: "no-cache" },
      }),
      env,
      executionContext(),
    );
    assert.equal(forcedByPragma.headers.get("x-portal-hot-report-cache"), null);
    assert.equal((await forcedByPragma.json()).items[0].title, "Live C");

    bucket.seedIndex("Live D");
    const forcedBySmoke = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24&smoke=release-1"),
      env,
      executionContext(),
    );
    assert.equal(forcedBySmoke.headers.get("x-portal-hot-report-cache"), null);
    assert.equal((await forcedBySmoke.json()).items[0].title, "Live D");

    const cachedAgain = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24"),
      env,
      executionContext(),
    );
    assert.equal(cachedAgain.headers.get("x-portal-hot-report-cache"), "HIT");
    assert.equal((await cachedAgain.json()).items[0].title, "Cached A");

    for (const request of [
      new Request("https://portal.example.invalid/api/hot-reports?limit=24&q=Live"),
      new Request("https://portal.example.invalid/api/hot-reports?limit=24&bootstrap=1"),
      new Request("https://portal.example.invalid/api/hot-reports?limit=24&unknown=1"),
      new Request("https://portal.example.invalid/api/hot-reports?limit=24", { headers: { origin: "https://portal.example.invalid" } }),
      new Request("https://portal.example.invalid/api/hot-reports?limit=24", { headers: { authorization: "Bearer test" } }),
    ]) {
      const live = await worker.fetch(request, env, executionContext());
      assert.equal(live.status, 200);
      assert.equal(live.headers.get("x-portal-hot-report-cache"), null);
      assert.equal((await live.json()).items[0].title, "Live D");
    }
  } finally {
    if (previousCaches) Object.defineProperty(globalThis, "caches", previousCaches);
    else delete globalThis.caches;
  }
});

test("stale or unavailable public indexes are never stored in the first-page cache", async () => {
  const previousCaches = Object.getOwnPropertyDescriptor(globalThis, "caches");
  const cache = new MemoryCache();
  Object.defineProperty(globalThis, "caches", {
    configurable: true,
    value: { default: cache },
  });
  try {
    const staleBucket = new MemoryR2();
    staleBucket.seedIndex("Last good");
    staleBucket.seedStaleMarker();
    const env = {
      REPORT_BUCKET: staleBucket,
      ALLOWED_ORIGIN: "https://portal.example.invalid",
    };
    const stale = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24"),
      env,
    );
    assert.equal(stale.status, 200);
    assert.equal(stale.headers.get("cache-control"), "public, max-age=5, stale-while-revalidate=300");
    assert.equal(stale.headers.get("x-portal-hot-report-cache"), null);
    assert.equal(cache.rows.size, 0);

    const unavailable = await worker.fetch(
      new Request("https://portal.example.invalid/api/hot-reports?limit=24"),
      { REPORT_BUCKET: new MemoryR2(), ALLOWED_ORIGIN: "https://portal.example.invalid" },
    );
    assert.equal(unavailable.status, 503);
    assert.equal(unavailable.headers.get("x-portal-hot-report-cache"), null);
    assert.equal(cache.rows.size, 0);
  } finally {
    if (previousCaches) Object.defineProperty(globalThis, "caches", previousCaches);
    else delete globalThis.caches;
  }
});

test("Cache API failures fall back to a live successful first page", async () => {
  const previousCaches = Object.getOwnPropertyDescriptor(globalThis, "caches");
  try {
    for (const cache of [
      new MemoryCache({ throwMatch: true }),
      new MemoryCache({ throwPut: true }),
    ]) {
      Object.defineProperty(globalThis, "caches", {
        configurable: true,
        value: { default: cache },
      });
      const bucket = new MemoryR2();
      bucket.seedIndex("Live fallback");
      const ctx = executionContext();
      const response = await worker.fetch(
        new Request("https://portal.example.invalid/api/hot-reports?limit=24"),
        { REPORT_BUCKET: bucket, ALLOWED_ORIGIN: "https://portal.example.invalid" },
        ctx,
      );
      assert.equal(response.status, 200);
      assert.equal(response.headers.get("x-portal-hot-report-cache"), "MISS");
      assert.equal((await response.json()).items[0].title, "Live fallback");
      await Promise.all(ctx.pending);
    }
  } finally {
    if (previousCaches) Object.defineProperty(globalThis, "caches", previousCaches);
    else delete globalThis.caches;
  }
});
