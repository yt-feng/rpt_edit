import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerPath, "utf8");

function sourceBetween(startMarker, endMarker) {
  const start = workerSource.indexOf(startMarker);
  const end = workerSource.indexOf(endMarker, start + startMarker.length);
  assert.notEqual(start, -1, `missing source marker: ${startMarker}`);
  assert.notEqual(end, -1, `missing source marker: ${endMarker}`);
  return workerSource.slice(start, end);
}

function evaluateFunctions(source, names, globals = {}) {
  const context = vm.createContext({ ...globals });
  vm.runInContext(`${source}\nglobalThis.__tested = { ${names.join(", ")} };`, context);
  return { context, functions: context.__tested };
}

test("external search uses its full-request 10 second budget without changing the shared budget", async () => {
  const externalTimeout = workerSource.match(/const EXTERNAL_SEARCH_TIMEOUT_MS = (\d+);/);
  assert.ok(externalTimeout, "external search must declare an independent timeout");
  assert.equal(Number(externalTimeout[1]), 10000);
  assert.match(
    workerSource,
    /async function fetchWithTimeout\(resource, init = \{\}, timeoutMs = UPSTREAM_SEARCH_TIMEOUT_MS\)/,
  );
  assert.match(
    workerSource,
    /async function fetchExternalSearchJsonWithTimeout\(resource, init = \{\}, timeoutMs = EXTERNAL_SEARCH_TIMEOUT_MS\)/,
  );
  assert.equal(
    (workerSource.match(/EXTERNAL_SEARCH_TIMEOUT_MS/g) || []).length,
    2,
    "the shorter timeout must remain scoped to external search",
  );

  let cachedSearchArgs;
  let externalJsonRequest;
  const handlerSource = sourceBetween(
    "async function handleExternalSearch",
    "// Fetch the upstream detail",
  );
  const { functions } = evaluateFunctions(handlerSource, ["handleExternalSearch"], {
    URL,
    EXTERNAL_API: "https://reportify.example.test/api",
    EXTERNAL_SEARCH_PAGE_SIZE: 20,
    externalHeaders: () => ({ Accept: "application/json" }),
    slimExternalItem: (item) => ({ id: String(item.report_id || "") }),
    fetchExternalSearchJsonWithTimeout: async (url, init) => {
      externalJsonRequest = { url, init };
      return { items: [{ report_id: "report-1" }], page_num: 1, total_page: 1 };
    },
    handleCachedSearch: (...args) => {
      cachedSearchArgs = args;
      return { delegated: true };
    },
  });

  await functions.handleExternalSearch({
    url: "https://portal.example.invalid/external/search?q=US%20economic&page=1",
  }, {});
  assert.equal(cachedSearchArgs[2], "external");
  assert.equal(cachedSearchArgs.length, 8, "external search must not pass skipFreshCache options");

  const refreshed = await cachedSearchArgs[6]();
  assert.match(externalJsonRequest.url, /^https:\/\/reportify\.example\.test\/api\/reports\?/);
  assert.equal(externalJsonRequest.init.headers.Accept, "application/json");
  assert.equal(refreshed.items[0].id, "report-1");
});

test("external search timeout covers a body read that never completes", async () => {
  let bodyStarted = false;
  let requestSignal;
  const timeoutSource = sourceBetween(
    "async function fetchExternalSearchJsonWithTimeout",
    "function newsfeedUserKey",
  );
  const { functions } = evaluateFunctions(
    timeoutSource,
    ["fetchExternalSearchJsonWithTimeout"],
    {
      AbortController,
      clearTimeout,
      setTimeout,
      fetch: async (_resource, init) => {
        requestSignal = init.signal;
        return {
          ok: true,
          json: () => {
            bodyStarted = true;
            return new Promise(() => {});
          },
        };
      },
    },
  );

  let guardTimer;
  const guard = new Promise((_resolve, reject) => {
    guardTimer = setTimeout(() => reject(new Error("test guard expired")), 250);
  });
  try {
    await assert.rejects(
      Promise.race([
        functions.fetchExternalSearchJsonWithTimeout("https://reportify.example.test/reports", {}, 10),
        guard,
      ]),
      (error) => error && error.name === "TimeoutError" && error.message === "External search timed out.",
    );
  } finally {
    clearTimeout(guardTimer);
  }
  assert.equal(bodyStarted, true);
  assert.equal(requestSignal.aborted, true);
});

test("external search can return a fresh six-hour query cache without calling Reportify", async () => {
  assert.match(workerSource, /const SEARCH_CACHE_FRESH_MS = 6 \* 60 \* 60 \* 1000;/);
  let fetcherCalls = 0;
  const cacheSource = sourceBetween(
    "async function handleCachedSearch",
    "function searchMirrorKey",
  );
  const { functions } = evaluateFunctions(cacheSource, ["handleCachedSearch"], {
    getSearchCache: async () => ({
      cached_at: "2026-08-16T08:00:00.000Z",
      payload: { items: [{ id: "cached-report" }], page: 1, total_page: 1 },
    }),
    cachedPayloadIsFresh: () => true,
    jsonResponse: (_request, _env, status, payload) => ({ status, payload }),
    putSearchCache: async () => {},
    searchPayloadHasItems: (payload) => Boolean(payload && payload.items && payload.items.length),
  });

  const response = await functions.handleCachedSearch(
    {},
    {},
    "external",
    "US economic",
    1,
    { items: [] },
    async () => {
      fetcherCalls += 1;
      return { items: [{ id: "live-report" }] };
    },
  );

  assert.equal(fetcherCalls, 0);
  assert.equal(response.status, 200);
  assert.equal(response.payload.cache_status, "fresh");
  assert.equal(response.payload.items[0].id, "cached-report");
});

test("a non-empty stale cache wins before mirror lookup, while an empty cache can use the mirror", async () => {
  let cachedPayload = { items: [{ id: "stale-report" }], page: 1, total_page: 1 };
  let mirrorCalls = 0;
  const cacheSource = sourceBetween(
    "async function handleCachedSearch",
    "function searchMirrorKey",
  );
  const { functions } = evaluateFunctions(cacheSource, ["handleCachedSearch"], {
    getSearchCache: async () => ({
      cached_at: "2026-08-15T08:00:00.000Z",
      payload: cachedPayload,
    }),
    cachedPayloadIsFresh: () => false,
    jsonResponse: (_request, _env, status, payload) => ({ status, payload }),
    putSearchCache: async () => {},
    searchPayloadHasItems: (payload) => Boolean(payload && payload.items && payload.items.length),
  });
  const fetcher = async () => {
    throw new Error("upstream unavailable");
  };
  const mirror = async () => {
    mirrorCalls += 1;
    return { items: [{ id: "mirror-report" }], page: 1, total_page: 1 };
  };

  const stale = await functions.handleCachedSearch(
    {}, {}, "external", "US economic", 1, { items: [] }, fetcher, mirror,
  );
  assert.equal(stale.payload.cache_status, "stale");
  assert.equal(stale.payload.items[0].id, "stale-report");
  assert.equal(mirrorCalls, 0);

  cachedPayload = { items: [], page: 1, total_page: 0 };
  const mirrored = await functions.handleCachedSearch(
    {}, {}, "external", "US economic", 1, { items: [] }, fetcher, mirror,
  );
  assert.equal(mirrored.payload.cache_status, "mirror");
  assert.equal(mirrored.payload.items[0].id, "mirror-report");
  assert.equal(mirrorCalls, 1);
});

test("mirror matching treats Reportify underscores and query punctuation equivalently", () => {
  const mirrorSource = [
    sourceBetween("function compactSearchQuery", "async function searchCacheKey"),
    sourceBetween("function normalizeSearchMirrorText", "async function searchMirrorFallback"),
    sourceBetween("function dateScore", "function sortGithubDirsDesc"),
  ].join("\n");
  const { functions } = evaluateFunctions(
    mirrorSource,
    ["normalizeSearchMirrorText", "searchMirrorPayloadFromItems"],
  );
  const query = "US Economic Viewpoint: K, so what? Implications of a K-shaped economy";
  const report = {
    id: "reportify-k-economy",
    title: "US Economic Viewpoint_ K, so what_ Implications of a K-shaped economy",
    institution: "Morgan Stanley",
    date: "2026-08-15",
  };

  assert.equal(
    functions.normalizeSearchMirrorText(query),
    functions.normalizeSearchMirrorText(report.title),
  );
  const exact = functions.searchMirrorPayloadFromItems([report], query, 1, 20);
  assert.equal(exact.total, 1);
  assert.equal(exact.items[0].id, report.id);

  const broad = functions.searchMirrorPayloadFromItems([report], "US economic", 1, 20);
  assert.equal(broad.total, 1);
  assert.equal(broad.items[0].id, report.id);

  for (const invalidQuery of ["!!!", "📈🚀", "C++"]) {
    const invalid = functions.searchMirrorPayloadFromItems([report], invalidQuery, 1, 20);
    assert.equal(invalid.total, 0, `${invalidQuery} must not return the full mirror`);
    assert.equal(invalid.items.length, 0);
  }
});
