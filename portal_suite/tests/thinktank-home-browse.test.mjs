import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { setImmediate } from "node:timers/promises";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const remoteStart = source.indexOf("    const externalUrl = workerUrl;");
const remoteEnd = source.indexOf("    let searchIndexPrunedText = false;", remoteStart);
const inputStart = source.indexOf("    let localSearchTimer = 0;");
const inputEnd = source.indexOf('    pageSize.addEventListener("change"', inputStart);
assert.ok(remoteStart > 0 && remoteEnd > remoteStart && inputStart > 0 && inputEnd > inputStart);

function deferred() {
  let resolve;
  let reject;
  const promise = new Promise((yes, no) => { resolve = yes; reject = no; });
  return { promise, resolve, reject };
}

function control(value = "") {
  const listeners = new Map();
  return {
    value,
    hidden: true,
    textContent: "",
    innerHTML: "",
    className: "",
    style: {},
    classList: { add() {} },
    setAttribute() {},
    addEventListener(name, listener) { listeners.set(name, listener); },
    removeEventListener() {},
    emit(name) { return listeners.get(name)?.({}); },
  };
}

function home({ query = "", scope = "all", ignoreAbort = false } = {}) {
  const elements = new Map();
  const element = (id) => {
    if (!elements.has(id)) elements.set(id, control());
    return elements.get(id);
  };
  const requests = [];
  const events = [];
  const timers = new Map();
  let timerId = 0;
  let now = 0;
  const input = control();
  const scopeFilter = control(scope);
  const chartIndex = deferred();
  const counts = { catalog: 0, hot: 0, thinktank: 0, external: 0, reportA: 0, authority: 0 };
  const context = vm.createContext({
    AbortController,
    URLSearchParams,
    input,
    scopeFilter,
    workerUrl: "https://portal.example.invalid/api",
    THINKTANK_SOURCE: "thinktank",
    EXTERNAL_SOURCE: "external",
    REPORT_A_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    searchResultCounts: counts,
    fullCatalogReady: true,
    items: [],
    searchTextById: new Map(),
    searchSourceProgress: element("searchSourceProgress"),
    searchSourceProgressItems: element("searchSourceProgressItems"),
    searchSourceProgressSummary: element("searchSourceProgressSummary"),
    searchSourceProgressBar: element("searchSourceProgressBar"),
    results: control(),
    bankFilter: control(),
    industryFilter: control(),
    startDate: control(),
    endDate: control(),
    availabilityFilter: control(),
    pageRangeInputs: [],
    externalDateFilter: null,
    externalIncludeHtml: null,
    authorityInstitutionFilter: null,
    authorityDateFilter: null,
    authorityPageFilter: null,
    hotReportsResults: null,
    hotReportsPrev: null,
    hotReportsNext: null,
    hotReportsRetry: null,
    searchRecommendationsResults: null,
    chartSearchSection: control(),
    chartSearchStatus: control(),
    hotReportSearchTimer: 0,
    document: { getElementById: element },
    window: {
      location: { search: query ? `?q=${encodeURIComponent(query)}` : "" },
      setTimeout(fn, delay) { timers.set(++timerId, { fn, due: now + delay }); return timerId; },
      clearTimeout(id) { timers.delete(id); },
    },
    fetch(url, { signal }) {
      const operation = deferred();
      const request = {
        url: new URL(url), signal,
        reply(data, status = 200) {
          operation.resolve({ ok: status < 400, status, json: async () => data });
        },
      };
      if (!ignoreAbort) signal.addEventListener("abort", () => {
        const error = new Error("aborted");
        error.name = "AbortError";
        operation.reject(error);
      });
      requests.push(request);
      return operation.promise;
    },
    trackEvent(worker, name, payload) { events.push({ name, ...payload }); },
    publicMessageText: (text) => String(text || ""),
    localizedServiceMessage: (text) => String(text || ""),
    publicSearchItem: (item, source) => ({ ...item, source }),
    escapeHtml: (text) => String(text || ""),
    thinkTankRow: (item) => `<a class="thinktank-row" data-id="${item.id}">${item.title}</a>`,
    externalSearchView: (items) => ({ items }),
    authoritySearchView: (items) => items,
    embeddedSearchRequestUrl: (base, path, query) => `${base}/${path}?q=${encodeURIComponent(query)}`,
    renderSearchRecommendations() {},
    startCatalogForUserIntent() {},
    render() {},
    renderHotReports() {},
    updateCatalogReadiness() {},
    scheduleHotReportSearch() {},
    captureEarlyInput() {},
    ensureChartSearchIndex: () => chartIndex.promise,
  });
  // Execute the production request pipeline, actual initial scheduling, and
  // actual input/scope listeners; only unrelated catalog rendering is stubbed.
  vm.runInContext(`${source.slice(remoteStart, remoteEnd)}
    ${source.slice(inputStart, inputEnd)}
    globalThis.sourceStates = remoteSourceStates;
  `, context);
  return {
    element, requests, events, counts, input, scopeFilter, chartIndex,
    states: context.sourceStates,
    enter(value) { input.value = value; input.emit("input"); },
    tick(ms) {
      now += ms;
      for (const [id, timer] of [...timers]) {
        if (timer.due <= now && timers.delete(id)) timer.fn();
      }
    },
    thinktank(query = "") {
      return requests.filter((request) => request.url.pathname.endsWith("/thinktank/search")
        && request.url.searchParams.get("q") === query).at(-1);
    },
  };
}

const latest = { id: "thinktank:crs-R49338", title: "Latest CRS report" };

test("a blank home immediately requests and displays CRS reports without search accounting", async () => {
  const h = home();
  assert.equal(h.requests.length, 1, "browsing only fetches the think-tank feed");
  assert.equal(h.element("thinkTankSection").hidden, false);
  assert.match(h.element("thinkTankResults").innerHTML, /正在加载美国国会研究处/);
  h.thinktank().reply({ items: [latest], cache_status: "live" });
  await setImmediate();
  assert.match(h.element("thinkTankResults").innerHTML, /Latest CRS report/);
  assert.equal(h.element("thinkTankCount").textContent, "最新 1 条");
  assert.equal(h.counts.thinktank, 0);
  assert.equal(h.states.size, 0);
  assert.equal(h.element("searchSourceProgress").hidden, true);
  assert.equal(h.events.length, 0);
});

test("typing searches all sources and clearing restores latest reports", async () => {
  const h = home();
  h.thinktank().reply({ items: [latest] });
  await setImmediate();
  h.enter("energy");
  h.tick(480);
  assert.equal(h.requests.filter((request) => request.url.searchParams.get("q") === "energy").length, 4);
  h.thinktank("energy").reply({ items: [{ id: "thinktank:energy", title: "Energy results" }] });
  await setImmediate();
  assert.match(h.element("thinkTankResults").innerHTML, /Energy results/);
  assert.equal(h.counts.thinktank, 1);
  assert.equal(h.events.filter((event) => event.source === "thinktank" && event.query === "energy").length, 1);
  h.enter("   ");
  h.thinktank().reply({ items: [latest] });
  await setImmediate();
  assert.match(h.element("thinkTankResults").innerHTML, /Latest CRS report/);
  assert.equal(h.counts.thinktank, 0);
  assert.equal(h.element("searchSourceProgress").hidden, true);
  assert.equal(h.events.some((event) => !event.query), false);
});

test("a late recommendation response cannot overwrite a query result", async () => {
  const h = home({ ignoreAbort: true });
  const oldFeed = h.thinktank();
  h.enter("energy");
  assert.equal(oldFeed.signal.aborted, true);
  h.tick(480);
  h.thinktank("energy").reply({ items: [{ id: "thinktank:energy", title: "Energy results" }] });
  await setImmediate();
  oldFeed.reply({ items: [latest] });
  await setImmediate();
  assert.match(h.element("thinkTankResults").innerHTML, /Energy results/);
  assert.doesNotMatch(h.element("thinkTankResults").innerHTML, /Latest CRS/);
  assert.equal(h.counts.thinktank, 1);
});

test("a late query response cannot replace the feed after clearing", async () => {
  const h = home({ query: "energy", ignoreAbort: true });
  assert.equal(h.requests.length, 0, "an initial query must skip the recommendation request");
  h.tick(480);
  const oldQuery = h.thinktank("energy");
  h.enter("");
  h.thinktank().reply({ items: [latest] });
  await setImmediate();
  oldQuery.reply({ items: [{ id: "thinktank:energy", title: "Outdated search" }] });
  await setImmediate();
  assert.match(h.element("thinkTankResults").innerHTML, /Latest CRS report/);
  assert.equal(h.counts.thinktank, 0);
  assert.equal(h.states.size, 0);
  assert.equal(h.events.length, 0);
});

test("charts hide and cancel recommendations before the chart index completes; leaving charts restores them", async () => {
  const h = home({ ignoreAbort: true });
  const oldFeed = h.thinktank();
  h.scopeFilter.value = "charts";
  const changed = h.scopeFilter.emit("change");
  assert.equal(oldFeed.signal.aborted, true);
  assert.equal(h.element("thinkTankSection").hidden, true);
  oldFeed.reply({ items: [latest] });
  await setImmediate();
  assert.equal(h.element("thinkTankResults").innerHTML, "");
  assert.equal(h.element("thinkTankSection").hidden, true);
  h.chartIndex.resolve();
  await changed;
  h.scopeFilter.value = "all";
  await h.scopeFilter.emit("change");
  assert.equal(h.requests.length, 2);
  h.thinktank().reply({ items: [latest] });
  await setImmediate();
  assert.equal(h.element("thinkTankSection").hidden, false);
  assert.match(h.element("thinkTankResults").innerHTML, /Latest CRS report/);
  assert.equal(home({ scope: "charts" }).requests.length, 0);
});

test("empty, failed, stale and partial feed responses retain distinct visible states", async () => {
  for (const data of [
    { items: [], cache_status: "miss" },
    { items: [], partial_sources: ["crs"] },
    { items: [], warning: "RSS is temporarily unavailable" },
  ]) {
    const h = home();
    h.thinktank().reply(data);
    await setImmediate();
    assert.equal(h.element("thinkTankResults").innerHTML, "");
    assert.match(h.element("thinkTankStatus").className, /error/);
    assert.ok(h.element("thinkTankStatus").textContent);
    assert.equal(h.counts.thinktank, 0);
    assert.equal(h.states.size, 0);
  }
  const stale = home();
  stale.thinktank().reply({ items: [latest], cache_status: "stale", warning: "Showing previously fetched reports" });
  await setImmediate();
  assert.match(stale.element("thinkTankResults").innerHTML, /Latest CRS report/);
  assert.match(stale.element("thinkTankStatus").textContent, /previously fetched/);
  const empty = home();
  empty.thinktank().reply({ items: [], cache_status: "live" });
  await setImmediate();
  assert.match(empty.element("thinkTankResults").innerHTML, /暂无最新报告/);
  assert.doesNotMatch(empty.element("thinkTankStatus").className, /error/);
});

test("recommendation timeouts settle visibly without producing search failure counts", async () => {
  const h = home();
  h.tick(18_000);
  await setImmediate();
  assert.equal(h.thinktank().signal.aborted, true);
  assert.equal(h.element("thinkTankSection").hidden, false);
  assert.equal(h.element("thinkTankResults").innerHTML, "");
  assert.match(h.element("thinkTankStatus").textContent, /最新报告暂时无法加载/);
  assert.equal(h.counts.thinktank, 0);
  assert.equal(h.states.size, 0);
  assert.equal(h.events.length, 0);
});

test("an unavailable source returned with HTTP 200 is a search error, while an HTTP feed error stays outside search accounting", async () => {
  const search = home({ query: "energy" });
  search.tick(480);
  search.thinktank("energy").reply({ items: [], cache_status: "miss" });
  await setImmediate();
  assert.equal(search.counts.thinktank, "error");
  assert.equal(search.states.get("thinktank"), "error");
  assert.match(search.element("thinkTankStatus").textContent, /暂时不可用/);
  assert.equal(search.element("thinkTankResults").innerHTML, "");

  const browse = home();
  browse.thinktank().reply({}, 503);
  await setImmediate();
  assert.match(browse.element("thinkTankStatus").textContent, /最新报告暂时无法加载/);
  assert.equal(browse.counts.thinktank, 0);
  assert.equal(browse.events.length, 0);
  assert.equal(browse.states.size, 0);
});
