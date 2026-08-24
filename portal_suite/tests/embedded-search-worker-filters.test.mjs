import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerPath, "utf8");

function extractFunction(source, name) {
  const markers = [`function ${name}(`, `async function ${name}(`];
  const start = markers.reduce((found, marker) => {
    const index = source.indexOf(marker);
    return index >= 0 && (found < 0 || index < found) ? index : found;
  }, -1);
  assert.notEqual(start, -1, `${name} must exist`);
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

function evaluateFunctions(names, globals = {}) {
  const context = vm.createContext({ ...globals });
  const source = names.map((name) => extractFunction(workerSource, name)).join("\n");
  vm.runInContext(`${source}\nglobalThis.tested = { ${names.join(", ")} };`, context);
  return { context, functions: context.tested };
}

test("Worker normalizes embedded filters and includes every filter in cache identity", async () => {
  const names = [
    "compactSearchQuery",
    "normalizeEmbeddedSearchDate",
    "normalizeEmbeddedSearchInstitution",
    "normalizeEmbeddedPageRange",
    "embeddedPageRangeBounds",
    "embeddedSearchFilters",
    "embeddedSearchCacheQuery",
    "searchCacheKey",
  ];
  const { functions } = evaluateFunctions(names, {
    URL,
    AUTHORITY_SOURCE: "authority",
    SEARCH_CACHE_PREFIX: "_search-cache",
    sha256Hex: async (value) => value,
  });

  const url = new URL("https://worker.example.test/authority/search?q=AI"
    + "&start_date=2026-08-24&end_date=2026-05-24"
    + "&institution=%20Nash%20%20AI%20&page_range=10_20");
  const filters = functions.embeddedSearchFilters(url, "authority");
  assert.equal(filters.startDate, "2026-05-24", "reversed valid dates are normalized");
  assert.equal(filters.endDate, "2026-08-24");
  assert.equal(filters.institution, "Nash AI");
  assert.equal(filters.pageRange, "10_20");
  assert.deepEqual(
    JSON.parse(JSON.stringify(filters.pageBounds)),
    { min: 11, max: 20 },
  );

  const firstKey = functions.embeddedSearchCacheQuery("AI", filters);
  const htmlKey = functions.embeddedSearchCacheQuery("AI", { ...filters, includeHtml: true });
  const institutionKey = functions.embeddedSearchCacheQuery("AI", { ...filters, institution: "Other" });
  assert.notEqual(firstKey, htmlKey);
  assert.notEqual(firstKey, institutionKey);
  assert.match(firstKey, /"start_date":"2026-05-24"/);
  assert.match(firstKey, /"page_range":"10_20"/);

  const longQuery = "q".repeat(160);
  const longHtmlIdentity = functions.embeddedSearchCacheQuery(longQuery, { ...filters, includeHtml: true });
  const longPdfIdentity = functions.embeddedSearchCacheQuery(longQuery, { ...filters, includeHtml: false });
  assert.notEqual(
    await functions.searchCacheKey("external", longHtmlIdentity, 1),
    await functions.searchCacheKey("external", longPdfIdentity, 1),
    "filter identity must survive a maximum-length query",
  );
});

test("authority upstream payload uses supported date and minimum-page fields only", () => {
  const { functions } = evaluateFunctions(["authoritySearchPayload"], {
    AUTHORITY_SEARCH_PAGE_SIZE: 20,
  });
  const payload = functions.authoritySearchPayload("robotics", 2, {
    startDate: "2026-05-24",
    endDate: "2026-08-24",
    institution: "Nash AI",
    pageBounds: { min: 11, max: 20 },
  });
  assert.equal(payload.startDate, "2026-05-24");
  assert.equal(payload.endDate, "2026-08-24");
  assert.equal(payload.minPages, 11);
  assert.equal(payload.pageNum, 2);
  assert.equal(payload.pageSize, 20);
  assert.equal(Object.hasOwn(payload, "institution"), false, "unverified institution params must not be invented");
});

test("authority deadline also covers an upstream JSON body that stalls", async () => {
  let signal;
  const { functions } = evaluateFunctions(["fetchAuthoritySearchJsonWithTimeout"], {
    AbortController,
    clearTimeout,
    setTimeout,
    AUTHORITY_SEARCH_TIMEOUT_MS: 15_000,
    fetch: async (_resource, init) => {
      signal = init.signal;
      return { ok: true, json: () => new Promise(() => {}) };
    },
  });
  await assert.rejects(
    functions.fetchAuthoritySearchJsonWithTimeout("https://authority.example.test/search", {}, 10),
    (error) => error && error.name === "TimeoutError" && /Authority search timed out/u.test(error.message),
  );
  assert.equal(signal.aborted, true);
});

test("Reportify scans at most three pages and never claims HTML-only on an incomplete scan", async () => {
  const calls = [];
  const pageRows = new Map([
    [1, [{ id: "html-1", file_type: "html", date: "2026-08-20" }]],
    [2, [{ id: "html-2", file_type: "html", date: "2026-08-19" }]],
    [3, [{ id: "html-3", file_type: "html", date: "2026-08-18" }]],
  ]);
  const globals = {
    Date,
    EXTERNAL_SEARCH_TIMEOUT_MS: 10_000,
    EXTERNAL_SEARCH_MAX_PAGES: 3,
    fetchExternalSearchPage: async (_query, page) => {
      calls.push(page);
      return { items: pageRows.get(page) || [], page, totalPage: 5 };
    },
  };
  const dependencyNames = [
    "normalizeEmbeddedSearchDate",
    "embeddedItemMatchesDate",
    "externalItemIsHtml",
    "filterExternalSearchItems",
    "dedupeEmbeddedSearchItems",
  ];
  const context = vm.createContext(globals);
  for (const name of dependencyNames) {
    context[name] = vm.runInContext(`(${extractFunction(workerSource, name)})`, context);
  }
  const boundedExternalSearch = vm.runInContext(`(${extractFunction(workerSource, "boundedExternalSearch")})`, context);
  const filters = { startDate: "", endDate: "", includeHtml: false };
  const partial = await boundedExternalSearch("AI", 1, filters);
  assert.deepEqual(calls, [1, 2, 3]);
  assert.equal(partial.filter_complete, false);
  assert.equal(partial.filter_partial, true);
  assert.equal(partial.html_fallback, false);
  assert.equal(partial.html_fallback_unconfirmed, true);
  assert.equal(partial.items.length, 0);

  calls.length = 0;
  context.fetchExternalSearchPage = async (_query, page) => {
    calls.push(page);
    return { items: pageRows.get(page) || [], page, totalPage: 2 };
  };
  // Re-evaluate so the function closes over the replacement fetch stub.
  const completeSearch = vm.runInContext(`(${extractFunction(workerSource, "boundedExternalSearch")})`, context);
  const complete = await completeSearch("AI", 1, filters);
  assert.deepEqual(calls, [1, 2]);
  assert.equal(complete.filter_complete, true);
  assert.equal(complete.html_fallback, true);
  assert.deepEqual(Array.from(complete.items, (item) => item.id), ["html-1", "html-2"]);
});

test("authority Worker applies exact institution and non-overlapping upper page bounds after bounded scan", () => {
  const names = [
    "normalizeEmbeddedSearchDate",
    "normalizeEmbeddedSearchInstitution",
    "embeddedItemMatchesDate",
    "embeddedItemMatchesPageRange",
    "authorityItemMatchesFilters",
    "dedupeEmbeddedSearchItems",
    "completedBoundedAuthorityResult",
  ];
  const { functions } = evaluateFunctions(names, {
    AUTHORITY_SEARCH_PAGE_SIZE: 20,
    AUTHORITY_SEARCH_MAX_PAGES: 3,
  });
  const filters = {
    startDate: "2026-05-24",
    endDate: "2026-08-24",
    institution: "Nash AI",
    pageRange: "10_20",
    pageBounds: { min: 11, max: 20 },
  };
  const result = functions.completedBoundedAuthorityResult("foreign", 1, [
    {
      page: 1,
      total: 80,
      items: [
        { id: "ten", institution: "Nash AI", date: "2026-08-20", page_count: 10 },
        { id: "eleven", institution: "Nash AI", date: "2026-08-20", page_count: 11 },
        { id: "twenty", institution: "Nash AI", date: "2026-08-20", page_count: 20 },
        { id: "twenty-one", institution: "Nash AI", date: "2026-08-20", page_count: 21 },
        { id: "other", institution: "Other", date: "2026-08-20", page_count: 15 },
      ],
    },
    { page: 2, total: 80, items: [] },
    { page: 3, total: 80, items: [] },
  ], filters);
  assert.deepEqual(Array.from(result.items, (item) => item.id), ["eleven", "twenty"]);
  assert.equal(result.filter_complete, false, "a fourth upstream page remains unscanned");
  assert.deepEqual(Array.from(result.scanned_pages), [1, 2, 3]);
});

test("external and authority routes delegate using normalized filter-aware cache keys", async () => {
  const calls = [];
  const shared = {
    URL,
    AUTHORITY_SOURCE: "authority",
    compactSearchQuery: (value) => String(value || "").trim(),
    normalizeEmbeddedSearchDate: (value) => String(value || "").trim(),
    normalizeEmbeddedSearchInstitution: (value) => String(value || "").trim().replace(/\s+/g, " "),
    normalizeEmbeddedPageRange: (value) => ["under5", "5_10", "10_20", "over20"].includes(value) ? value : "",
    embeddedPageRangeBounds: (range) => range === "10_20" ? { min: 11, max: 20 } : { min: 0, max: 0 },
    embeddedSearchFilters: null,
    embeddedSearchCacheQuery: null,
    jsonResponse: () => null,
    handleCachedSearch: (...args) => {
      calls.push(args);
      return { delegated: true };
    },
  };
  const helperContext = vm.createContext(shared);
  shared.embeddedSearchFilters = vm.runInContext(`(${extractFunction(workerSource, "embeddedSearchFilters")})`, helperContext);
  shared.embeddedSearchCacheQuery = vm.runInContext(`(${extractFunction(workerSource, "embeddedSearchCacheQuery")})`, helperContext);

  const externalContext = vm.createContext({
    ...shared,
    boundedExternalSearch: async () => ({ items: [] }),
    externalSearchMirrorFallback: async () => null,
  });
  const handleExternalSearch = vm.runInContext(`(${extractFunction(workerSource, "handleExternalSearch")})`, externalContext);
  await handleExternalSearch({
    url: "https://worker.example.test/external/search?q=AI&include_html=1&start_date=2026-07-24",
  }, {});
  assert.equal(calls[0][2], "external");
  assert.match(calls[0][3], /"include_html":true/);
  assert.match(calls[0][3], /"start_date":"2026-07-24"/);

  const authorityContext = vm.createContext({
    ...shared,
    AUTHORITY_KINDS: { foreign: {} },
    AUTHORITY_DOMESTIC_LEAD_KIND: "domestic-lead",
    authoritySearchKindBounded: async () => ({ items: [] }),
    authorityDomesticLeadSearchBounded: async () => ({ items: [] }),
    sourceLeadAdapterEnabled: () => false,
    dedupeEmbeddedSearchItems: (items) => items,
    authorityInstitutionFacets: () => [],
    authoritySearchMirrorFallback: async () => null,
    AUTHORITY_SEARCH_TIMEOUT_MS: 15_000,
  });
  const handleAuthoritySearch = vm.runInContext(`(${extractFunction(workerSource, "handleAuthoritySearch")})`, authorityContext);
  await handleAuthoritySearch({
    url: "https://worker.example.test/authority/search?q=AI&institution=Nash%20AI&page_range=10_20&start_date=2026-05-24",
  }, {});
  assert.equal(calls[1][2], "authority");
  assert.match(calls[1][3], /"institution":"nash ai"/);
  assert.match(calls[1][3], /"page_range":"10_20"/);
});
