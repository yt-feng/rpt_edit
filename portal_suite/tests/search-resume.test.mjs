import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const key = "portal_last_search_v1";
const ttl = 30 * 24 * 60 * 60 * 1000;

function functionSource(name, indent = "  ") {
  const start = source.indexOf(`${indent}function ${name}(`);
  const end = source.indexOf(`\n${indent}}`, start);
  assert.ok(start >= 0 && end > start);
  return source.slice(start, end + indent.length + 2);
}

function element() {
  const listeners = new Map();
  return {
    value: "", hidden: true, textContent: "", focused: false,
    addEventListener(type, fn) { listeners.set(type, [...listeners.get(type) || [], fn]); },
    emit(type) { for (const fn of listeners.get(type) || []) fn(); },
    focus() { this.focused = true; },
  };
}

function setup({ stored, locale = "zh-Hans", value = "", storage: provided } = {}) {
  const rows = new Map(stored ? [[key, JSON.stringify(stored)]] : []);
  const storage = provided || {
    getItem: (name) => rows.get(name) || null,
    setItem: (name, val) => rows.set(name, val),
    removeItem: (name) => rows.delete(name),
  };
  const elements = Object.fromEntries(["searchResume", "resumeLastSearch", "lastSearchQuery", "forgetLastSearch"].map((id) => [id, element()]));
  const input = element();
  input.value = value;
  let restores = 0;
  const context = vm.createContext({
    document: { getElementById: (id) => elements[id] },
    window: { localStorage: storage },
    CONTENT_LOCALE: locale, LAST_SEARCH_KEY: key, LAST_SEARCH_TTL_MS: ttl,
  });
  vm.runInContext(`${functionSource("hotReportLocalStorage")}\n${functionSource("readLastSearch")}\n${functionSource("initSearchResume")}`, context);
  const controller = context.initSearchResume({ input, onRestore: () => { restores += 1; } });
  return { ...elements, input, rows, context, controller, get restores() { return restores; } };
}

test("returning home still starts empty and only a click resumes the previous keyword", () => {
  const ui = setup({ stored: { query: "半导体 <img src=x>", savedAt: Date.now(), locale: "zh-Hans" } });
  assert.equal(ui.input.value, "");
  assert.equal(ui.restores, 0);
  assert.equal(ui.searchResume.hidden, false);
  assert.equal(ui.lastSearchQuery.textContent, "半导体 <img src=x>");
  assert.equal(ui.lastSearchQuery.innerHTML, undefined, "user keywords are rendered as text");
  ui.resumeLastSearch.emit("click");
  assert.equal(ui.input.value, "半导体 <img src=x>");
  assert.equal(ui.restores, 1);
  assert.equal(ui.input.focused, true);
  assert.equal(ui.searchResume.hidden, true);
});

test("an explicit URL query or text already entered takes priority over history", () => {
  const ui = setup({ value: "current query", stored: { query: "old query", savedAt: Date.now(), locale: "zh-Hans" } });
  ui.resumeLastSearch.emit("click");
  assert.equal(ui.searchResume.hidden, true);
  assert.equal(ui.input.value, "current query");
  assert.equal(ui.restores, 0);
  const init = source.slice(source.indexOf("async function initIndex()"), source.indexOf("function filenameFromDisposition"));
  assert.ok(init.indexOf('new URLSearchParams(window.location.search).get("q")') < init.indexOf("searchResume = initSearchResume({"));
  ui.input.value = "";
  ui.input.emit("input");
  assert.equal(ui.searchResume.hidden, false);
});

test("only one bounded keyword is stored, and deleting history does not recreate it during a repeated render", () => {
  const ui = setup();
  ui.controller.remember(" first ");
  ui.controller.remember("second");
  assert.equal(ui.rows.size, 1);
  assert.deepEqual(Object.keys(JSON.parse(ui.rows.get(key))).sort(), ["locale", "query", "savedAt"]);
  assert.equal(JSON.parse(ui.rows.get(key)).query, "second");
  ui.forgetLastSearch.emit("click");
  ui.controller.remember("second");
  assert.equal(ui.rows.size, 0);
  assert.equal(ui.searchResume.hidden, true);
  ui.controller.remember("x".repeat(250));
  assert.equal(JSON.parse(ui.rows.get(key)).query.length, 200);
  ui.controller.remember("");
  assert.equal(ui.rows.size, 1);
});

test("the existing search debounce saves the settled keyword and waits for composition to finish", () => {
  const ui = setup();
  let pending;
  let renders = 0;
  const context = vm.createContext({
    input: ui.input, searchResume: ui.controller, localSearchTimer: 0, inputComposing: false,
    window: { clearTimeout() { pending = null; }, setTimeout(fn) { pending = fn; return 1; } },
    results: { classList: { add() {} }, setAttribute() {} },
    updateCatalogReadiness() {}, scheduleExternalSearch() {}, renderHotReports() {},
    fullCatalogReady: true, items: [], render() { renders += 1; },
  });
  const start = source.indexOf("    const scheduleLocalRender =");
  const end = source.indexOf('    input.addEventListener("compositionstart"', start);
  vm.runInContext(`${source.slice(start, end)}\nthis.schedule = scheduleLocalRender;`, context);
  ui.input.value = "draft";
  context.schedule();
  assert.equal(ui.rows.size, 0);
  ui.input.value = "settled keyword";
  context.schedule();
  pending();
  assert.equal(JSON.parse(ui.rows.get(key)).query, "settled keyword");
  assert.equal(renders, 1);
  context.inputComposing = true;
  ui.input.value = "拼音输入中";
  context.schedule();
  assert.equal(pending, null);
  assert.equal(JSON.parse(ui.rows.get(key)).query, "settled keyword");
});

test("expired, future, malformed and different-language history cannot resume", () => {
  const now = Date.now();
  for (const stored of [
    { query: "expired", savedAt: now - ttl - 1, locale: "zh-Hans" },
    { query: "future", savedAt: now + 600_000, locale: "zh-Hans" },
    { query: { unsafe: "object" }, savedAt: now, locale: "zh-Hans" },
    { query: "x".repeat(201), savedAt: now, locale: "zh-Hans" },
    { query: "日本語", savedAt: now, locale: "ja" },
  ]) {
    const ui = setup({ stored });
    ui.resumeLastSearch.emit("click");
    assert.equal(ui.input.value, "");
    assert.equal(ui.restores, 0);
    assert.equal(ui.searchResume.hidden, true);
  }
  for (const locale of ["ko", "ja", "ar"]) {
    const ui = setup({ locale, stored: { query: "AI 研究", savedAt: now, locale } });
    ui.resumeLastSearch.emit("click");
    assert.equal(ui.input.value, "AI 研究", "locale changes never translate a user's query");
    assert.equal(ui.restores, 1);
  }
});

test("storage failures do not prevent typing, searching, or clearing", () => {
  const disabled = () => { throw new Error("storage disabled"); };
  const ui = setup({ storage: { getItem: disabled, setItem: disabled, removeItem: disabled } });
  assert.doesNotThrow(() => {
    ui.controller.remember("new search");
    ui.forgetLastSearch.emit("click");
    ui.input.value = "new search";
    ui.input.emit("input");
  });
  Object.defineProperty(ui.context.window, "localStorage", { get: disabled });
  assert.equal(ui.context.hotReportLocalStorage(), null);
  assert.equal(ui.input.value, "new search");
  assert.equal(ui.searchResume.hidden, true);
});

test("catalog zero results provide a working clear-filter action that preserves the keyword", () => {
  const input = { value: "NVIDIA" };
  const controlNames = ["bankFilter", "industryFilter", "startDate", "endDate", "scopeFilter", "availabilityFilter", "externalDateFilter", "authorityInstitutionFilter", "authorityDateFilter", "authorityPageFilter"];
  const controls = Object.fromEntries(controlNames.map((id) => [id, { value: "selected" }]));
  const clear = element();
  const pageRangeInputs = [{ checked: true }];
  const externalIncludeHtml = { checked: true };
  let renders = 0;
  const results = { innerHTML: "", querySelector() { return this.innerHTML.includes("data-clear-catalog-filters") ? clear : null; } };
  const context = vm.createContext({
    ...controls, input, pageRangeInputs, externalIncludeHtml,
    startCatalogForUserIntent() {}, render() { renders += 1; }, renderExternalSearchResults() {},
    renderAuthoritySearchResults() {}, scheduleHotReportSearch() {}, renderHotReports() {}, scheduleExternalSearch() {},
  });
  vm.runInContext(`${functionSource("clearAllFilters", "    ")}\n${functionSource("renderCatalogEmptyState")}`, context);
  context.renderCatalogEmptyState(results, { hasFilters: true, hasOtherSources: true, onClearFilters: context.clearAllFilters });
  assert.match(results.innerHTML, /当前目录未找到匹配报告/u);
  assert.match(results.innerHTML, /下方其他来源/u);
  clear.emit("click");
  assert.equal(input.value, "NVIDIA");
  assert.equal(controls.scopeFilter.value, "all");
  for (const [id, control] of Object.entries(controls)) if (id !== "scopeFilter") assert.equal(control.value, "");
  assert.equal(pageRangeInputs[0].checked, false);
  assert.equal(externalIncludeHtml.checked, false);
  assert.equal(renders, 1);
  context.renderCatalogEmptyState(results, { hasFilters: false, hasOtherSources: false, onClearFilters: context.clearAllFilters });
  assert.doesNotMatch(results.innerHTML, /data-clear-catalog-filters|下方其他来源/u);
});
