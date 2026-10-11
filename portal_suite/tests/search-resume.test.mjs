import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const extendedSource = await readFile(new URL("../locale_assets/extended-locales.js", import.meta.url), "utf8");
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
    dispatchEvent(event) { for (const fn of listeners.get(event.type) || []) fn(event); return true; },
    emit(type) { for (const fn of listeners.get(type) || []) fn(); },
    focus() { this.focused = true; },
  };
}

function setup({ stored, locale = "zh-Hans", pageLanguage, value = "", storage: provided } = {}) {
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
    document: {
      documentElement: pageLanguage === undefined ? undefined : { lang: pageLanguage },
      getElementById: (id) => elements[id],
    },
    window: { localStorage: storage },
    CONTENT_LOCALE: locale, LAST_SEARCH_KEY: key, LAST_SEARCH_TTL_MS: ttl,
  });
  vm.runInContext(`${functionSource("hotReportLocalStorage")}\n${functionSource("searchResumeLocale")}\n${functionSource("readLastSearch")}\n${functionSource("initSearchResume")}`, context);
  const controller = context.initSearchResume({ input, onRestore: () => { restores += 1; } });
  return { ...elements, input, rows, storage, context, controller, get restores() { return restores; } };
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

test("shared catalog pages keep saved searches within the actual page language", () => {
  const original = setup({ pageLanguage: "fr" });
  original.controller.remember("économie");
  assert.equal(original.context.CONTENT_LOCALE, "zh-Hans", "the source catalog locale stays unchanged");
  assert.equal(JSON.parse(original.rows.get(key)).locale, "fr");
  assert.equal(original.context.readLastSearch(original.storage).query, "économie");

  for (const pageLanguage of ["de", "zh-CN", "zh-Hans"]) {
    const other = setup({ pageLanguage, storage: original.storage });
    assert.equal(other.context.readLastSearch(other.storage), null);
    other.resumeLastSearch.emit("click");
    assert.equal(other.searchResume.hidden, true);
    assert.equal(other.input.value, "");
    assert.equal(other.restores, 0);
  }

  const returning = setup({ pageLanguage: "fr", storage: original.storage });
  assert.equal(returning.searchResume.hidden, false);
  assert.equal(returning.input.value, "", "history never automatically replaces the default home search");
  assert.equal(returning.restores, 0);
  returning.resumeLastSearch.emit("click");
  assert.equal(returning.input.value, "économie");
  assert.equal(returning.restores, 1);
  assert.equal(original.rows.size, 1);
});

test("Traditional Chinese and Cantonese histories remain separate while retaining only one record", () => {
  const traditional = setup({ pageLanguage: "zh-Hant" });
  traditional.controller.remember("繁體關鍵字");
  const cantonese = setup({ pageLanguage: "yue", storage: traditional.storage });
  assert.equal(cantonese.searchResume.hidden, true);
  assert.equal(cantonese.context.readLastSearch(cantonese.storage), null);
  cantonese.controller.remember("粵語關鍵字");
  assert.equal(traditional.rows.size, 1);
  assert.equal(JSON.parse(traditional.rows.get(key)).locale, "yue");
  const traditionalReturn = setup({ pageLanguage: "zh-Hant", storage: traditional.storage });
  assert.equal(traditionalReturn.searchResume.hidden, true);
  assert.equal(traditionalReturn.context.readLastSearch(traditionalReturn.storage), null);
  const cantoneseReturn = setup({ pageLanguage: "yue", storage: traditional.storage });
  cantoneseReturn.resumeLastSearch.emit("click");
  assert.equal(cantoneseReturn.input.value, "粵語關鍵字");
});

test("missing or invalid page language falls back to the content locale for reading and writing", () => {
  for (const pageLanguage of [undefined, null, "", "  ", 17, {}]) {
    const ui = setup({ pageLanguage, locale: "ko" });
    ui.controller.remember("AI 연구");
    assert.equal(JSON.parse(ui.rows.get(key)).locale, "ko");
    assert.equal(ui.context.readLastSearch(ui.storage).query, "AI 연구");
    const returning = setup({ pageLanguage, locale: "ko", storage: ui.storage });
    returning.resumeLastSearch.emit("click");
    assert.equal(returning.input.value, "AI 연구");
    assert.equal(returning.restores, 1);
  }
  for (const pageLanguage of ["ko", "ja", "ar"]) {
    const ui = setup({ pageLanguage: ` ${pageLanguage} ` });
    ui.controller.remember("AI 研究");
    assert.equal(JSON.parse(ui.rows.get(key)).locale, pageLanguage);
    const returning = setup({ pageLanguage, storage: ui.storage });
    returning.resumeLastSearch.emit("click");
    assert.equal(returning.input.value, "AI 研究");
    assert.equal(returning.restores, 1);
  }
});

test("resuming runs the real input listeners once and refreshes the approved extended collection", () => {
  for (const extendedFirst of [true, false]) {
    const elements = new Map();
    const get = (id) => {
      if (!elements.has(id)) elements.set(id, element());
      return elements.get(id);
    };
    const input = get("searchInput");
    const rows = [
      { dataset: { kind: "reports", date: "2026-10-01" }, textContent: "Économie française", hidden: false },
      { dataset: { kind: "blog", date: "2026-09-30" }, textContent: "Technologie mondiale", hidden: false },
    ];
    Object.assign(get("extendedResults"), { querySelectorAll: () => rows, append() {} });
    const document = {
      documentElement: { lang: "fr" },
      getElementById: (id) => ["extendedSearch", "extendedFrom", "extendedTo", "extendedClear"].includes(id) ? null : get(id),
    };
    const stored = new Map([[key, JSON.stringify({ query: "économie", locale: "fr", savedAt: Date.now() })]]);
    const timers = new Map();
    let timerId = 0;
    const calls = { intent: 0, external: 0, hot: 0, render: 0, hotRender: 0, input: 0 };
    const context = vm.createContext({
      document, Event, URLSearchParams, location: { search: "" },
      window: {
        localStorage: { getItem: (name) => stored.get(name), setItem: (name, value) => stored.set(name, value), removeItem: (name) => stored.delete(name) },
        clearTimeout: (id) => timers.delete(id),
        setTimeout: (fn, delay) => { timers.set(++timerId, { fn, delay }); return timerId; },
      },
      input, CONTENT_LOCALE: "zh-Hans", LAST_SEARCH_KEY: key, LAST_SEARCH_TTL_MS: ttl,
      scopeFilter: { value: "all" }, hotReportSearchTimer: 0,
      results: { classList: { add() {} }, setAttribute() {} },
      fullCatalogReady: true, items: [], updateCatalogReadiness() {},
      startCatalogForUserIntent() { calls.intent += 1; },
      scheduleExternalSearch() { calls.external += 1; },
      scheduleHotReportSearch(query) { assert.equal(query, "économie"); calls.hot += 1; },
      render() { calls.render += 1; }, renderHotReports() { calls.hotRender += 1; },
    });
    input.addEventListener("input", (event) => { calls.input += 1; assert.equal(event.bubbles, true); });
    vm.runInContext(["hotReportLocalStorage", "searchResumeLocale", "readLastSearch", "initSearchResume"].map((name) => functionSource(name)).join("\n") + "\nlet searchResume = null;", context);
    const listenersStart = source.indexOf("    let localSearchTimer = 0;");
    const listenersEnd = source.indexOf('    input.removeEventListener("input", captureEarlyInput);', listenersStart);
    const resumeStart = source.indexOf("    searchResume = initSearchResume({", source.indexOf("async function initIndex()"));
    const resumeEnd = source.indexOf("    scheduleExternalSearch();", resumeStart);
    if (extendedFirst) vm.runInContext(extendedSource, context);
    vm.runInContext(source.slice(listenersStart, listenersEnd) + source.slice(resumeStart, resumeEnd), context);
    if (!extendedFirst) vm.runInContext(extendedSource, context);
    assert.equal(get("extendedCount").textContent, "2 / 2");
    assert.equal(input.value, "");

    get("resumeLastSearch").emit("click");

    assert.equal(input.value, "économie");
    assert.deepEqual(rows.map((row) => row.hidden), [false, true]);
    assert.equal(get("extendedCount").textContent, "1 / 2");
    assert.equal(get("extendedPage").textContent, "1 / 1");
    assert.equal(get("extendedEmpty").hidden, true);
    assert.deepEqual(calls, { intent: 1, external: 1, hot: 1, render: 0, hotRender: 0, input: 1 });
    assert.equal(timers.size, 1, "only the normal catalog debounce is scheduled");
    const timer = [...timers.values()][0];
    assert.equal(timer.delay, 240);
    timer.fn();
    assert.equal(calls.render, 1);
    assert.equal(calls.hotRender, 1);
    assert.equal(stored.size, 1);
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
