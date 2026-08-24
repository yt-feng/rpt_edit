import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const htmlPath = new URL("../site_src/index.html", import.meta.url);
const [appSource, htmlSource] = await Promise.all([
  readFile(appPath, "utf8"),
  readFile(htmlPath, "utf8"),
]);

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
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

const context = vm.createContext({ Date, URL });
vm.runInContext(`
  const PAGE_RANGE_FILTERS = [
    { value: "under5", matches: (pages) => pages > 0 && pages <= 5 },
    { value: "5_10", matches: (pages) => pages >= 5 && pages <= 10 },
    { value: "10_20", matches: (pages) => pages >= 10 && pages <= 20 },
    { value: "over20", matches: (pages) => pages >= 20 },
  ];
  const AUTHORITY_PAGE_RANGE_FILTERS = [
    { value: "under5", matches: (pages) => pages > 0 && pages <= 5 },
    { value: "5_10", matches: (pages) => pages >= 6 && pages <= 10 },
    { value: "10_20", matches: (pages) => pages >= 11 && pages <= 20 },
    { value: "over20", matches: (pages) => pages > 20 },
  ];
  ${extractFunction(appSource, "recentMonthCutoff")}
  ${extractFunction(appSource, "itemMatchesRecentMonths")}
  ${extractFunction(appSource, "recentDateBounds")}
  ${extractFunction(appSource, "embeddedSearchRequestUrl")}
  ${extractFunction(appSource, "isExternalHtmlItem")}
  ${extractFunction(appSource, "externalSearchView")}
  ${extractFunction(appSource, "reportPageCountValue")}
  ${extractFunction(appSource, "pageRangeForValue")}
  ${extractFunction(appSource, "authorityPageRangeForValue")}
  ${extractFunction(appSource, "authoritySearchView")}
  globalThis.filters = { externalSearchView, authoritySearchView, embeddedSearchRequestUrl };
`, context);

const now = Date.parse("2026-08-24T12:00:00.000Z");

test("Reportify defaults to PDF-like rows and falls back to HTML only when needed", () => {
  const mixed = [
    { id: "pdf", date: "2026-08-20", file_type: "pdf" },
    { id: "html", date: "2026-08-21", file_type: "html" },
  ];
  const defaultView = context.filters.externalSearchView(mixed, {}, now);
  assert.deepEqual(Array.from(defaultView.items, (item) => item.id), ["pdf"]);
  assert.equal(defaultView.hiddenHtmlCount, 1);
  assert.equal(defaultView.htmlFallback, false);

  const inclusive = context.filters.externalSearchView(mixed, { includeHtml: true }, now);
  assert.deepEqual(Array.from(inclusive.items, (item) => item.id), ["pdf", "html"]);

  const unconfirmedHtmlOnly = context.filters.externalSearchView(
    [{ id: "only-html", date: "2026-08-22", file_type: "text/html" }],
    {},
    now,
  );
  assert.deepEqual(Array.from(unconfirmedHtmlOnly.items, (item) => item.id), []);
  assert.equal(unconfirmedHtmlOnly.htmlFallback, false);

  const confirmedHtmlOnly = context.filters.externalSearchView(
    [{ id: "only-html", date: "2026-08-22", file_type: "text/html" }],
    { allowHtmlFallback: true },
    now,
  );
  assert.deepEqual(Array.from(confirmedHtmlOnly.items, (item) => item.id), ["only-html"]);
  assert.equal(confirmedHtmlOnly.htmlFallback, true);
});

test("Reportify recent-date filters use calendar months", () => {
  const view = context.filters.externalSearchView([
    { id: "inside", date: "2026-07-24", file_type: "pdf" },
    { id: "outside", date: "2026-07-23", file_type: "pdf" },
    { id: "unknown", date: "", file_type: "pdf" },
  ], { recentMonths: 1 }, now);
  assert.deepEqual(Array.from(view.items, (item) => item.id), ["inside"]);
});

test("high-authority filters combine institution, recent date, and page range", () => {
  const items = [
    { id: "match", institution: "Nash AI", date: "2026-08-20", page_count: 18 },
    { id: "wrong-pages", institution: "Nash AI", date: "2026-08-20", page_count: 8 },
    { id: "wrong-institution", institution: "Other", date: "2026-08-20", page_count: 18 },
    { id: "too-old", institution: "Nash AI", date: "2026-01-20", page_count: 18 },
  ];
  const visible = context.filters.authoritySearchView(items, {
    institution: "Nash AI",
    recentMonths: 3,
    pageRange: "10_20",
  }, now);
  assert.deepEqual(Array.from(visible, (item) => item.id), ["match"]);
});

test("page ranges are mutually exclusive at 5, 10, and 20-page boundaries", () => {
  const items = [5, 6, 10, 11, 20, 21].map((page_count) => ({
    id: String(page_count),
    page_count,
    date: "2026-08-20",
  }));
  const ids = (pageRange) => Array.from(
    context.filters.authoritySearchView(items, { pageRange }, now),
    (item) => item.id,
  );
  assert.deepEqual(ids("under5"), ["5"]);
  assert.deepEqual(ids("5_10"), ["6", "10"]);
  assert.deepEqual(ids("10_20"), ["11", "20"]);
  assert.deepEqual(ids("over20"), ["21"]);
});

test("embedded search URLs carry normalized date, HTML, institution, and page filters", () => {
  const externalUrl = new URL(context.filters.embeddedSearchRequestUrl(
    "https://worker.example.test/api",
    "external/search",
    "AI chips",
    { recentMonths: 1, includeHtml: false },
    now,
  ));
  assert.equal(externalUrl.pathname, "/api/external/search");
  assert.equal(externalUrl.searchParams.get("q"), "AI chips");
  assert.equal(externalUrl.searchParams.get("start_date"), "2026-07-24");
  assert.equal(externalUrl.searchParams.get("end_date"), "2026-08-24");
  assert.equal(externalUrl.searchParams.get("include_html"), "0");

  const relativeWorkerUrl = new URL(context.filters.embeddedSearchRequestUrl(
    "/api",
    "external/search",
    "AI chips",
    {},
    now,
    "https://portal.example.invalid/index.html",
  ));
  assert.equal(relativeWorkerUrl.href, "https://portal.example.invalid/api/external/search?q=AI+chips&include_html=0");

  const authorityUrl = new URL(context.filters.embeddedSearchRequestUrl(
    "https://worker.example.test",
    "authority/search",
    "robotics",
    { recentMonths: 3, institution: "Nash AI", pageRange: "10_20" },
    now,
  ));
  assert.equal(authorityUrl.searchParams.get("start_date"), "2026-05-24");
  assert.equal(authorityUrl.searchParams.get("institution"), "Nash AI");
  assert.equal(authorityUrl.searchParams.get("page_range"), "10_20");

  const clearedAuthorityUrl = new URL(context.filters.embeddedSearchRequestUrl(
    "https://worker.example.test",
    "authority/search",
    "robotics",
    {},
    now,
  ));
  assert.equal(clearedAuthorityUrl.searchParams.get("q"), "robotics");
  assert.equal(clearedAuthorityUrl.searchParams.has("start_date"), false);
  assert.equal(clearedAuthorityUrl.searchParams.has("institution"), false);
  assert.equal(clearedAuthorityUrl.searchParams.has("page_range"), false);
});

test("clearing filters preserves the query, rerenders remote rows, and schedules fresh Worker searches", () => {
  const clearAllFilters = extractFunction(appSource, "clearAllFilters");
  assert.doesNotMatch(clearAllFilters, /input\.value\s*=\s*""/u);
  assert.match(clearAllFilters, /renderExternalSearchResults\(\)/u);
  assert.match(clearAllFilters, /renderAuthoritySearchResults\(\)/u);
  assert.match(clearAllFilters, /scheduleExternalSearch\(\)/u);
});

test("home page exposes independent Reportify and high-authority controls", () => {
  for (const id of [
    "externalDateFilter",
    "externalIncludeHtml",
    "authorityInstitutionFilter",
    "authorityDateFilter",
    "authorityPageFilter",
  ]) {
    assert.match(htmlSource, new RegExp(`id="${id}"`));
  }
  assert.match(htmlSource, /最近 1 个月/u);
  assert.match(htmlSource, /最近 3 个月/u);
  assert.match(htmlSource, /最近半年/u);
  assert.match(htmlSource, /包含 HTML 结果/u);
  assert.match(htmlSource, /≤5 页/u);
  assert.match(htmlSource, /6–10 页/u);
  assert.match(htmlSource, /11–20 页/u);
  assert.match(htmlSource, /&gt;20 页/u);
});
