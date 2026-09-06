#!/usr/bin/env node

"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const runtimePath = path.join(root, "portal_suite", "locale_assets", "locale-runtime.js");
const runtimeSource = fs.readFileSync(runtimePath, "utf8");

function cloneJson(value) {
  return JSON.parse(JSON.stringify(value));
}

function createHarness({
  htmlLang = "zh-Hans",
  browserLanguages = ["en-US"],
  browserLanguage = null,
  href = "https://portal.example.invalid/reports/example.html?from=test#summary",
  responsePayload = { items: [] },
  responsePayloads = {},
  titleTranslations = {},
  itemTranslations = {},
  overlayTranslations = {},
  overlayFailures = [],
  initialControls = [],
  headAlternates = [],
  indexUi = false,
} = {}) {
  const observers = [];
  const redirects = [];
  const fetchCalls = [];
  let currentHref = href;
  let document;
  let mutationCount = 0;

  class ElementMock {
    constructor(tagName) {
      this.nodeType = 1;
      this.tagName = String(tagName || "div").toUpperCase();
      this.children = [];
      this.parentNode = null;
      this.attributes = new Map();
      this.dataset = {};
      this.className = "";
      this._textContent = "";
      this.classList = {
        values: new Set(),
        add: (...names) => names.forEach((name) => this.classList.values.add(name)),
        contains: (name) => this.classList.values.has(name),
      };
    }

    setAttribute(name, value) {
      this.attributes.set(String(name), String(value));
    }

    getAttribute(name) {
      const key = String(name);
      return this.attributes.has(key) ? this.attributes.get(key) : null;
    }

    get textContent() { return this._textContent; }

    set textContent(value) {
      this._textContent = String(value);
      if (document) document.notify({ type: "childList", target: this, addedNodes: [] });
    }

    get value() { return this.getAttribute("value") || ""; }
    set value(value) { this.setAttribute("value", value); }

    contains(node) {
      return this === node || this.children.some((child) => child === node || child.contains && child.contains(node));
    }

    querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }

    set href(value) {
      this.setAttribute("href", value);
    }

    get href() {
      return this.getAttribute("href") || "";
    }

    set hreflang(value) {
      this.setAttribute("hreflang", value);
    }

    get hreflang() {
      return this.getAttribute("hreflang") || "";
    }

    set lang(value) {
      this.setAttribute("lang", value);
    }

    get lang() {
      return this.getAttribute("lang") || "";
    }

    append(...nodes) {
      for (const node of nodes) {
        node.parentNode = this;
        this.children.push(node);
        if (document) document.notifyAdded(node);
      }
    }

    matches(selector) {
      if (String(selector).includes(",")) {
        return String(selector).split(",").some((part) => this.matches(part.trim()));
      }
      if (selector === "a[href]") {
        return this.tagName === "A" && this.getAttribute("href") !== null;
      }
      if (selector === 'link[rel~="alternate"][hreflang]') {
        return this.tagName === "LINK"
          && String(this.getAttribute("rel") || "").split(/\s+/).includes("alternate")
          && this.getAttribute("hreflang") !== null;
      }
      if (selector === "textarea") return this.tagName === "TEXTAREA";
      if (/^[a-z]+$/.test(selector)) return this.tagName === selector.toUpperCase();
      const inputType = String(selector).match(/^input\[type=["']([^"']+)["']\]$/);
      return Boolean(
        inputType
        && this.tagName === "INPUT"
        && String(this.getAttribute("type") || "text").toLowerCase() === inputType[1].toLowerCase()
      );
    }

    querySelectorAll(selector) {
      const matches = [];
      const visit = (node) => {
        for (const child of node.children || []) {
          if (child.matches && child.matches(selector)) matches.push(child);
          visit(child);
        }
      };
      visit(this);
      return matches;
    }
  }

  const html = new ElementMock("html");
  html.lang = htmlLang;
  const head = new ElementMock("head");
  const body = new ElementMock("body");
  html.children.push(head, body);
  head.parentNode = html;
  body.parentNode = html;

  document = {
    readyState: "complete",
    documentElement: html,
    head,
    body,
    createElement(tagName) {
      return new ElementMock(tagName);
    },
    addEventListener() {
      throw new Error("DOMContentLoaded listener is unexpected for a complete document");
    },
    querySelector(selector) {
      if (selector !== "[data-kc-locale-switcher]") return null;
      const nodes = [body];
      while (nodes.length) {
        const node = nodes.shift();
        if (Object.prototype.hasOwnProperty.call(node.dataset || {}, "kcLocaleSwitcher")) {
          return node;
        }
        nodes.push(...(node.children || []));
      }
      return null;
    },
    querySelectorAll(selector) {
      return body.querySelectorAll(selector);
    },
    getElementById(id) {
      const nodes = [html];
      while (nodes.length) {
        const node = nodes.shift();
        if (node.getAttribute && node.getAttribute("id") === id) return node;
        nodes.push(...(node.children || []));
      }
      return null;
    },
    notifyAdded(node) {
      this.notify({ type: "childList", target: node.parentNode, addedNodes: [node] });
    },
    notify(record) {
      mutationCount += 1;
      assert.ok(mutationCount < 2000, "UI observer must settle without a mutation loop");
      for (const observer of observers) {
        if (observer.targets.some(({ target, options }) => (
          options[record.type] && (target === record.target || options.subtree && target.contains(record.target))
        ))) observer.callback([record]);
      }
    },
  };
  for (const { hreflang, href: alternateHref } of headAlternates) {
    const alternate = document.createElement("link");
    alternate.setAttribute("rel", "alternate");
    alternate.setAttribute("hreflang", hreflang);
    alternate.setAttribute("href", alternateHref);
    document.head.append(alternate);
  }
  const initialControlNodes = initialControls.map(({ tagName, type }) => {
    const control = document.createElement(tagName);
    if (type) control.setAttribute("type", type);
    document.body.append(control);
    return control;
  });

  if (indexUi) {
    for (const [id, label, tagName] of [
      ["bankFilter", "Institution", "select"], ["industryFilter", "行业", "select"],
      ["startDate", "From", "input"], ["endDate", "To", "input"],
      ["scopeFilter", "Search In", "select"], ["pageSize", "Rows", "select"],
    ]) {
      const wrapper = document.createElement("label");
      const span = document.createElement("span");
      span.textContent = label;
      const control = document.createElement(tagName);
      control.setAttribute("id", id);
      wrapper.append(span, control);
      document.body.append(wrapper);
    }
    const addOption = (id, value, text) => {
      const option = document.createElement("option");
      option.value = value;
      option.textContent = text;
      document.getElementById(id).append(option);
    };
    addOption("bankFilter", "", "All institutions");
    addOption("bankFilter", "jpm", "J.P. Morgan (12)");
    addOption("industryFilter", "", "All industries");
    ["Banks / Financials", "Energy / Utilities", "Equity Strategy", "Healthcare / Biotech", "Metals / Mining"].forEach((name) => {
      addOption("industryFilter", name, `${name} (8)`);
    });
    ["all", "title", "catalog", "fulltext", "charts"].forEach((value) => addOption("scopeFilter", value, value));
    addOption("pageSize", "50", "50");
    for (const [id, text] of [
      ["clearFilters", "Clear"], ["prevPage", "上一个"], ["nextPage", "下一页"],
      ["pageInfo", "Page 1 / 1"], ["resultCount", "40 of 40 reports"], ["activeFilters", "No filters"],
      ["catalogMeta", "14551 reports | Updated 2026-09-06 10:44:48 +0800 | Title and catalog search ready"],
    ]) {
      const node = document.createElement(id.endsWith("Page") || id === "clearFilters" ? "button" : "span");
      node.setAttribute("id", id);
      node.textContent = text;
      document.body.append(node);
    }
  }

  class MutationObserverMock {
    constructor(callback) {
      this.callback = callback;
      this.targets = [];
    }

    observe(target, options) {
      if (!this.targets.length) observers.push(this);
      this.targets.push({ target, options });
    }
  }

  class RequestMock {
    constructor(url, source) {
      this.url = String(url);
      this.source = source;
    }
  }

  const location = {
    get href() {
      return currentHref;
    },
    set href(value) {
      redirects.push({ method: "href", value: String(value) });
      currentHref = new URL(String(value), currentHref).toString();
    },
    get origin() {
      return new URL(currentHref).origin;
    },
    assign(value) {
      redirects.push({ method: "assign", value: String(value) });
      currentHref = new URL(String(value), currentHref).toString();
    },
    replace(value) {
      redirects.push({ method: "replace", value: String(value) });
      currentHref = new URL(String(value), currentHref).toString();
    },
  };

  const navigator = {
    languages: browserLanguages.slice(),
    language: String(browserLanguage === null ? browserLanguages[0] || "" : browserLanguage),
  };

  const originalFetch = async (input) => {
    const requestUrl = typeof input === "string" ? input : input.url;
    fetchCalls.push(requestUrl);
    const resolved = new URL(String(requestUrl), currentHref);
    const overlayMatch = resolved.pathname.match(
      /^\/data\/i18n\/(ko|ja|ar)\/(catalog-titles|catalog-preview|catalog-detail-([a-z0-9_]{2})|chart-content|hot-reports)\.json$/i,
    );
    let payload;
    if (overlayMatch) {
      const locale = overlayMatch[1].toLowerCase();
      const overlayName = overlayMatch[2].toLowerCase();
      const kind = overlayName === "catalog-titles"
        ? "full"
        : overlayName === "catalog-preview" ? "preview"
        : overlayName.startsWith("catalog-detail-") ? `detail:${overlayMatch[3].toLowerCase()}`
        : overlayName === "hot-reports" ? "hot-reports" : "charts";
      if (overlayFailures.includes(kind)) {
        return {
          ok: false,
          status: 503,
          async json() { return {}; },
        };
      }
      const configured = overlayTranslations[kind] || {
        titles: titleTranslations,
        items: itemTranslations,
      };
      const fields = kind === "charts"
        ? [
          "title", "description", "trend_summary",
          "metrics", "entities", "periods", "geographies", "units", "keywords",
        ]
        : kind === "hot-reports" ? ["title", "title_cn", "institution", "description"]
        : ["title", "bank_name", "industry", "sector", "category"];
      const configuredItems = cloneJson(configured.items || {});
      for (const [itemId, title] of Object.entries(configured.titles || {})) {
        configuredItems[itemId] = { ...(configuredItems[itemId] || {}), title };
      }
      const rows = Object.entries(configuredItems).map(([itemId, values]) => [
          itemId,
          ...fields.map((field) => (
            kind === "charts" && ["metrics", "entities", "periods", "geographies", "units", "keywords"].includes(field)
              ? cloneJson(values[field] || [])
              : String(values[field] || "")
          )),
        ]);
      payload = {
        schema_version: 2,
        locale,
        kind,
        source_generation: String(configured.sourceGeneration || ""),
        ...(configured.scoped === undefined ? {} : { scoped: configured.scoped }),
        item_count: rows.length,
        fields,
        rows,
      };
    } else {
      payload = cloneJson(responsePayloads[resolved.pathname] || responsePayload);
    }
    return {
      ok: true,
      status: 200,
      async json() {
        return cloneJson(payload);
      },
    };
  };

  const window = {
    document,
    navigator,
    fetch: originalFetch,
  };
  Object.defineProperty(window, "location", {
    configurable: false,
    enumerable: true,
    get: () => location,
    set: (value) => {
      redirects.push({ method: "window.location", value: String(value) });
      currentHref = new URL(String(value), currentHref).toString();
    },
  });
  window.window = window;

  vm.runInNewContext(runtimeSource, {
    URL,
    Request: RequestMock,
    MutationObserver: MutationObserverMock,
    document,
    navigator,
    window,
  }, { filename: runtimePath });

  function appendAnchor(anchorHref) {
    const anchor = document.createElement("a");
    anchor.setAttribute("href", anchorHref);
    document.body.append(anchor);
    return anchor;
  }

  return {
    appendAnchor,
    document,
    fetchCalls,
    initialControlNodes,
    location,
    redirects,
    window,
    mutationCount: () => mutationCount,
    observerCount: () => observers.length,
  };
}

function assertNoSwitcherForSimplifiedChinese() {
  for (const browserLocale of ["zh-CN", "zh-Hans"]) {
    const originalHref = "https://portal.example.invalid/reports/?q=semiconductor#latest";
    const harness = createHarness({
      htmlLang: "zh-Hans",
      browserLanguages: [browserLocale, "en-US"],
      href: originalHref,
      headAlternates: ["ko", "ja", "ar"].map((hreflang) => ({
        hreflang, href: `https://portal.example.invalid/${hreflang}/reports/`,
      })),
    });
    assert.equal(
      harness.document.querySelector("[data-kc-locale-switcher]"),
      null,
      `${browserLocale} must not create a locale switcher`,
    );
    assert.equal(harness.location.href, originalHref, `${browserLocale} must not navigate`);
    assert.equal(harness.redirects.length, 0, `${browserLocale} must not redirect`);
  }

  const conflictingPreferences = createHarness({
    htmlLang: "zh-Hans",
    browserLanguage: "zh-CN",
    browserLanguages: ["en-US", "ja-JP"],
  });
  assert.equal(
    conflictingPreferences.document.querySelector("[data-kc-locale-switcher]"),
    null,
    "Simplified-Chinese browser UI must hide the switcher even when content preferences start in English",
  );
}

function assertLocalePathMapping() {
  const harness = createHarness({
    htmlLang: "zh-Hans",
    browserLanguages: ["zh-CN"],
  });
  const source = "https://portal.example.invalid/ko/reports/alpha.html?q=bank%20risk#source";
  for (const locale of ["ko", "ja", "ar"]) {
    const mapped = new URL(harness.window.PortalLocale.localeUrl(locale, source));
    assert.equal(mapped.pathname, `/${locale}/reports/alpha.html`);
    assert.equal(mapped.search, "?q=bank%20risk");
    assert.equal(mapped.hash, "#source");
  }
  assert.equal(harness.redirects.length, 0, "locale URL mapping must not navigate");
}

function assertLocaleFormattingConfiguration() {
  const expected = {
    "zh-Hans": ["zh-CN", "ltr"],
    ko: ["ko-KR", "ltr"],
    ja: ["ja-JP", "ltr"],
    ar: ["ar", "rtl"],
  };
  for (const [htmlLang, [intlLocale, direction]] of Object.entries(expected)) {
    const harness = createHarness({ htmlLang, browserLanguages: ["zh-CN"] });
    assert.equal(harness.window.PortalLocale.contentLocale, htmlLang);
    assert.equal(harness.window.PortalLocale.intlLocale, intlLocale);
    assert.equal(harness.window.PortalLocale.direction, direction);
  }
}

function assertSwitcherForEveryLocalizedPage() {
  for (const locale of ["ko", "ja", "ar"]) {
    for (const browserLocale of ["zh-CN", "zh-Hans", "en-US", "ja-JP"]) {
      for (const page of ["", "report.html?id=report-1#download", "reports/example.html", "blog/current.html", "account.html"]) {
        const harness = createHarness({
          htmlLang: locale, browserLanguage: browserLocale, browserLanguages: [browserLocale],
          href: `https://portal.example.invalid/${locale}/${page}`,
        });
        const switcher = harness.document.querySelector("[data-kc-locale-switcher]");
        assert.ok(switcher, `${locale}/${page} keeps Chinese entry for a ${browserLocale} browser`);
        const chineseLink = switcher.children.find((link) => link.hreflang === "zh-Hans");
        assert.equal(chineseLink.href, `https://portal.example.invalid/${page}`);
        assert.equal(chineseLink.getAttribute("data-kc-chinese-entry"), "");
        assert.equal(harness.redirects.length, 0);
        // Moving an existing switcher under newly inserted content must not
        // send its Chinese link back through the current locale.
        const wrapper = harness.document.createElement("section");
        wrapper.append(switcher);
        harness.document.body.append(wrapper);
        assert.equal(chineseLink.href, `https://portal.example.invalid/${page}`);
      }
    }
  }
  const harness = createHarness({
    htmlLang: "ja",
    browserLanguage: "en-US",
    browserLanguages: ["zh-CN", "en-US"],
    href: "https://portal.example.invalid/ja/reports/example.html?ref=nav#top",
  });
  const switcher = harness.document.querySelector("[data-kc-locale-switcher]");
  assert.ok(switcher, "a non-Simplified-Chinese browser must create the locale switcher");
  assert.equal(switcher.tagName, "NAV");
  assert.equal(switcher.children.length, 4, "switcher must expose all configured locales");
  const chineseLink = switcher.children.find((link) => link.hreflang === "zh-Hans");
  assert.ok(chineseLink, "switcher must include the Chinese root-site link");
  assert.equal(
    chineseLink.href,
    "https://portal.example.invalid/reports/example.html?ref=nav#top",
    "the link observer must not rewrite the switcher's Chinese root-site link back into the current locale",
  );
  assert.equal(harness.redirects.length, 0, "creating the switcher must not navigate");
}

function assertChinesePagesNeverShowLanguageSwitcher() {
  const published = ["ko", "ja", "ar"].map((hreflang) => ({
    hreflang, href: `https://portal.example.invalid/${hreflang}/blog/current.html`,
  }));
  for (const headAlternates of [
    [],
    published.slice(0, 2),
    [...published.slice(0, 2), { hreflang: "ar", href: "https://other.example.invalid/ar/blog/current.html" }],
    [...published.slice(0, 2), { hreflang: "ar", href: "/ko/blog/current.html" }],
    [...published, published[0]],
  ]) {
    const harness = createHarness({
      href: "https://portal.example.invalid/blog/old.html", headAlternates,
    });
    assert.equal(harness.document.querySelector("[data-kc-locale-switcher]"), null,
      "Chinese pages without one valid published alternate for every language must not offer missing locale pages");
    assert.deepEqual(harness.fetchCalls, [], "checking published alternates must not make requests");
  }
  for (const browserLocale of ["zh-CN", "en-US", "ja-JP", "ko-KR", "ar"]) {
    const harness = createHarness({
      href: "https://portal.example.invalid/blog/current-alias.html?from=nav#summary",
      browserLanguages: [browserLocale], headAlternates: published,
    });
    assert.equal(harness.document.querySelector("[data-kc-locale-switcher]"), null,
      "even published Chinese pages must not proactively show language choices");
    assert.equal(harness.redirects.length, 0, "Chinese pages must not navigate");
    assert.deepEqual(harness.fetchCalls, [], "Chinese pages must not request locale resources");
  }
  const localizedAccount = createHarness({
    htmlLang: "ko", href: "https://portal.example.invalid/ko/account.html",
  });
  assert.equal(localizedAccount.document.querySelector("[data-kc-locale-switcher]").children.length, 4,
    "localized account pages keep all language choices even without indexable hreflang declarations");
}

async function assertCatalogTitleOverlay() {
  const translated = {
    ko: "번역된 제목",
    ja: "翻訳されたタイトル",
    ar: "العنوان المترجم",
  };
  for (const locale of ["ko", "ja", "ar"]) {
    const originalTitle = "Original catalog title";
    const harness = createHarness({
      htmlLang: locale,
      browserLanguages: ["zh-CN"],
      responsePayload: {
        items: [{
          id: "report-1",
          title: originalTitle,
        }],
      },
      overlayTranslations: {
        preview: {
          items: { "report-1": { title: translated[locale] } },
        },
      },
    });
    assert.deepEqual(harness.fetchCalls, [], "locale runtime startup must not fetch any overlay");
    const response = await harness.window.fetch("data/catalog_preview.json?version=1");
    assert.deepEqual(harness.fetchCalls, [
      "/data/catalog_preview.json?version=1",
      `/data/i18n/${locale}/catalog-preview.json`,
    ], "the preview overlay must start in parallel with the relevant catalog request");
    const payload = await response.json();
    assert.equal(payload.items[0].title, translated[locale]);
    assert.equal(
      payload.items[0].title_zh,
      originalTitle,
      `${locale} overlay must preserve the source title as title_zh`,
    );
  }
}

async function assertOverlaySelectionAndUnrelatedJsonIsolation() {
  const originalTitle = "Original title";
  const harness = createHarness({
    htmlLang: "ja",
    browserLanguages: ["zh-CN"],
    responsePayload: { items: [{ id: "report-1", title: originalTitle }] },
    overlayTranslations: {
      preview: { items: { "report-1": { title: "Preview title" } } },
      full: {
        titles: { "report-1": "Full title" },
        items: { "report-1": { title: "Full title" } },
      },
    },
  });

  for (const path of ["data/config.json", "data/password_rules.json", "data/archive_catalog.json"]) {
    const response = await harness.window.fetch(path);
    await response.json();
  }
  assert.deepEqual(harness.fetchCalls, [
    "/data/config.json",
    "/data/password_rules.json",
    "/data/archive_catalog.json",
  ], "unrelated JSON must not trigger any translation overlay");

  const fullCatalog = await (await harness.window.fetch("data/catalog.json")).json();
  assert.equal(fullCatalog.items[0].title, "Full title");
  assert.deepEqual(harness.fetchCalls.slice(-2), [
    "/data/catalog.json",
    "/data/i18n/ja/catalog-titles.json",
  ]);

  await (await harness.window.fetch("data/search_index_current/manifest.json")).json();
  assert.equal(
    harness.fetchCalls.filter((value) => value === "/data/i18n/ja/catalog-titles.json").length,
    1,
    "the full catalog overlay must be memoized",
  );
  assert.equal(
    harness.fetchCalls.at(-1),
    "/data/search_index_current/manifest.json",
    "search shards have no translated visible fields and must not request a catalog overlay",
  );

  await (await harness.window.fetch("data/course-materials.json")).json();
  assert.equal(harness.fetchCalls.at(-1), "/ja/data/course-materials.json");
}

async function assertReportDetailUsesPrefixOverlay() {
  const reportId = "ab-report";
  const relatedId = "cd-related";
  const harness = createHarness({
    htmlLang: "ja",
    browserLanguages: ["zh-CN"],
    responsePayloads: {
      "/data/report_details/ab.json": {
        reports: {
          [reportId]: {
            item: { id: reportId, title: "Original primary" },
            related: [{ id: relatedId, title: "Original related" }],
          },
        },
      },
    },
    overlayTranslations: {
      "detail:ab": {
        items: {
          [reportId]: { title: "翻訳済み主報告" },
          [relatedId]: { title: "翻訳済み関連報告" },
        },
      },
    },
  });
  const payload = await (await harness.window.fetch("data/report_details/ab.json")).json();
  assert.equal(payload.reports[reportId].item.title, "翻訳済み主報告");
  assert.equal(payload.reports[reportId].related[0].title, "翻訳済み関連報告");
  assert.deepEqual(harness.fetchCalls, [
    "/data/report_details/ab.json",
    "/data/i18n/ja/catalog-detail-ab.json",
  ], "a detail shard must load only its matching compact translation overlay");
  assert.equal(
    harness.fetchCalls.includes("/data/i18n/ja/catalog-titles.json"),
    false,
    "a detail shard must not download the full catalog overlay",
  );
}

async function assertChartContentOverlay() {
  const original = {
    reportTitle: "原始报告标题",
    chartTitle: "原始图表标题",
    description: "原始图表描述",
    trend: "原始趋势",
  };
  const harness = createHarness({
    htmlLang: "ar",
    browserLanguages: ["zh-CN"],
    responsePayloads: {
      "/data/chart_search_index.json": {
        reports: [{
          report_id: "report-1",
          report_ref: "report-ref-1",
          title: original.reportTitle,
          search_text: "private searchable source stays unchanged",
          charts: [{
            id: "chart-1",
            analysis_version: "chart-search-v2",
            title: original.chartTitle,
            description: original.description,
            trend_summary: original.trend,
            metrics: ["原始指标"],
            entities: ["原始主体"],
            periods: ["原始期间"],
            geographies: ["原始地区"],
            units: ["原始单位"],
            keywords: ["原始关键词"],
          }],
        }],
      },
    },
    overlayTranslations: {
      charts: {
        items: {
          "report:report-1": { title: "عنوان التقرير" },
          "chart:chart-1": {
            title: "عنوان الرسم البياني",
            description: "وصف الرسم البياني",
            trend_summary: "اتجاه صاعد",
            metrics: ["المؤشر"],
            entities: ["الكيان"],
            periods: ["الفترة"],
            geographies: ["المنطقة"],
            units: ["الوحدة"],
            keywords: ["الكلمة المفتاحية"],
          },
        },
      },
    },
  });

  assert.deepEqual(harness.fetchCalls, [], "chart overlay must not load at locale runtime startup");
  const payload = await (await harness.window.fetch("data/chart_search_index.json")).json();
  assert.deepEqual(harness.fetchCalls, [
    "/data/chart_search_index.json",
    "/data/i18n/ar/chart-content.json",
  ], "chart data and its compact overlay must start together");
  const report = payload.reports[0];
  const chart = report.charts[0];
  assert.equal(report.title, "عنوان التقرير");
  assert.equal(report.title_zh, original.reportTitle);
  assert.equal(report.search_text, "private searchable source stays unchanged");
  assert.equal(chart.title, "عنوان الرسم البياني");
  assert.equal(chart.title_zh, original.chartTitle);
  assert.equal(chart.description, "وصف الرسم البياني");
  assert.equal(chart.trend_summary, "اتجاه صاعد");
  assert.deepEqual(chart.metrics, ["المؤشر"]);
  assert.deepEqual(chart.entities, ["الكيان"]);
  assert.deepEqual(chart.periods, ["الفترة"]);
  assert.deepEqual(chart.geographies, ["المنطقة"]);
  assert.deepEqual(chart.units, ["الوحدة"]);
  assert.deepEqual(chart.keywords, ["الكلمة المفتاحية"]);
}

async function assertHotReportOverlayIsLazyAndGenerationBound() {
  const original = {
    id: "hot:0123456789abcdef",
    title: "Original hot report",
    title_cn: "中文标题",
    institution: "Original institution",
    description: "Original description",
    filename: "original.pdf",
  };
  const harness = createHarness({
    htmlLang: "ko",
    browserLanguages: ["zh-CN"],
    overlayTranslations: {
      "hot-reports": {
        sourceGeneration: "0123456789abcdef",
        items: {
          [original.id]: {
            title: "번역된 핫 리포트",
            title_cn: "번역된 중국어 제목",
            institution: "번역된 기관",
            description: "번역된 설명",
          },
        },
      },
    },
  });
  assert.deepEqual(harness.fetchCalls, [], "Hot Report overlay must not load during locale startup");
  const localized = await harness.window.PortalLocale.localizeHotReports({
    generation: "0123456789abcdef",
    items: [cloneJson(original)],
  });
  assert.deepEqual(harness.fetchCalls, ["/data/i18n/ko/hot-reports.json"]);
  assert.equal(localized.items[0].title, "번역된 핫 리포트");
  assert.equal(localized.items[0].title_zh, original.title);
  assert.equal(localized.items[0].title_cn, "번역된 중국어 제목");
  assert.equal(localized.items[0].institution, "번역된 기관");
  assert.equal(localized.items[0].description, "번역된 설명");
  assert.equal(localized.items[0].filename, original.filename);

  const newerGeneration = await harness.window.PortalLocale.localizeHotReports({
    generation: "fedcba9876543210",
    items: [
      cloneJson(original),
      { ...cloneJson(original), id: "hot:1111111111111111", title: "Newest untranslated report" },
    ],
  });
  assert.equal(newerGeneration.locale_translation_pending, true);
  assert.deepEqual(Array.from(newerGeneration.items), [], "a stale overlay must not expose source-language list items");
  assert.equal(newerGeneration.total, 0);
  assert.equal(newerGeneration.next_cursor, "");
  assert.equal(newerGeneration.has_more, false);

  const missingGeneration = await harness.window.PortalLocale.localizeHotReports({
    items: [cloneJson(original)],
  });
  assert.equal(missingGeneration.locale_translation_pending, true);
  assert.deepEqual(Array.from(missingGeneration.items), [], "a missing source generation must remain pending");
  assert.equal(
    harness.fetchCalls.filter((value) => value === "/data/i18n/ko/hot-reports.json").length,
    1,
    "Hot Report overlay must be memoized",
  );

  const unavailableHarness = createHarness({
    htmlLang: "ar",
    browserLanguages: ["zh-CN"],
    overlayFailures: ["hot-reports"],
  });
  const unavailable = await unavailableHarness.window.PortalLocale.localizeHotReports({
    generation: "0123456789abcdef",
    items: [cloneJson(original)],
  });
  assert.equal(unavailable.locale_translation_pending, true);
  assert.deepEqual(Array.from(unavailable.items), [], "an unavailable overlay must not expose source-language list items");

  const chineseHarness = createHarness({ htmlLang: "zh-Hans", browserLanguages: ["zh-CN"] });
  const chinese = await chineseHarness.window.PortalLocale.localizeHotReports({
    generation: "fedcba9876543210",
    items: [cloneJson(original)],
  });
  assert.equal(chinese.locale_translation_pending, undefined, "the Chinese source page must not enter locale translation pending state");
  assert.equal(chinese.items[0].title, original.title);
  assert.deepEqual(chineseHarness.fetchCalls, []);
}

async function assertHotReportLocaleQueryFoldingAndFallback() {
  const cases = [
    {
      locale: "ko",
      query: "ai 반도체",
      fields: { title: "ＡＩ　반도체", description: "시장 전망" },
    },
    {
      locale: "ja",
      query: "ai 半導体",
      fields: { title: "ＡＩ・半導体", institution: "調査機関" },
    },
    {
      locale: "ar",
      query: "اسواق علي",
      fields: { title: "ـأَسْوَاق", description: "على" },
    },
  ];
  for (const { locale, query, fields } of cases) {
    const matchingId = "hot:0123456789abcdef";
    const harness = createHarness({
      htmlLang: locale,
      browserLanguages: ["zh-CN"],
      overlayTranslations: {
        "hot-reports": {
          sourceGeneration: "0123456789abcdef",
          items: {
            [matchingId]: fields,
            "hot:1111111111111111": { title: "unrelated localized title" },
          },
        },
      },
    });
    assert.deepEqual(harness.fetchCalls, [], "locale query matching must remain lazy at startup");
    assert.deepEqual(
      Array.from(await harness.window.PortalLocale.matchHotReportLocaleIds(query)),
      [matchingId.slice("hot:".length)],
      `${locale} query folding must match localized public fields`,
    );
    assert.deepEqual(
      Array.from(await harness.window.PortalLocale.matchHotReportLocaleIds("definitely absent")),
      [],
      "an available overlay with no localized match must return an explicit empty ID set",
    );
    assert.equal(
      harness.fetchCalls.filter((value) => value === `/data/i18n/${locale}/hot-reports.json`).length,
      1,
      "locale query matching must reuse the memoized compact overlay",
    );
  }

  const unavailable = createHarness({
    htmlLang: "ja",
    browserLanguages: ["zh-CN"],
    overlayFailures: ["hot-reports"],
  });
  assert.equal(
    await unavailable.window.PortalLocale.matchHotReportLocaleIds("半導体"),
    null,
    "an unavailable overlay must signal the app to keep the source-only query",
  );
}

async function assertScopedCatalogExcludesUnpublishedRowsOnly() {
  const original = {
    item_count: 3, count: 3, total: 3, total_item_count: 14551,
    items: [
      { id: "recent", title: "已选择原文", title_zh: "旧中文副标题" },
      { id: "old", title: "未选择旧原文" },
      { id: "group", title: "Structural group", items: [{ id: "old", title: "未选择旧原文" }] },
    ],
    controls: [{ id: "sort", title: "Sort control" }],
    metadata: { id: "metadata", title: "Structural metadata" },
  };
  const harness = createHarness({
    htmlLang: "ja", browserLanguages: ["zh-CN"], responsePayload: original,
    overlayTranslations: { preview: { scoped: true, items: { recent: { title: "公開済み記事" } } } },
  });
  const localized = await (await harness.window.fetch("data/catalog_preview.json")).json();
  assert.deepEqual(localized.items.map((item) => item.id), ["recent", "group"]);
  assert.equal(localized.items[0].title, "公開済み記事");
  assert.equal(localized.items[0].title_zh, "", "scoped translated cards must not show the Chinese source subtitle");
  assert.equal(localized.items[1].items.length, 0, "unpublished group children must be filtered without deleting the group");
  assert.deepEqual(localized.controls, original.controls);
  assert.deepEqual(localized.metadata, original.metadata);
  assert.equal(localized.item_count, 2);
  assert.equal(localized.count, 2);
  assert.equal(localized.total, 2);
  assert.equal(localized.total_item_count, 2, "the visible locale total must exclude omitted history");
  assert.equal(JSON.stringify(localized).includes("未选择旧原文"), false);
  assert.equal(harness.fetchCalls.length, 2, "scoped catalogs must not add another discovery request");

  const unchanged = cloneJson(original);
  harness.window.PortalLocale.localizePayload(unchanged, "zh-Hans", {}, {}, { scoped: true });
  assert.deepEqual(unchanged, original, "Chinese data must remain byte-equivalent even with scoped metadata");
  const legacy = cloneJson(original);
  harness.window.PortalLocale.localizePayload(legacy, "ja", {}, { recent: { title: "Legacy localized" } });
  assert.equal(legacy.items.length, 3, "unscoped callers must retain their current list behavior");
  assert.equal(legacy.items[0].title_zh, "已选择原文");
  assert.equal(legacy.total_item_count, 14551, "unscoped payload totals remain unchanged");
  const invalid = createHarness({
    htmlLang: "ja", browserLanguages: ["zh-CN"], responsePayload: original,
    overlayTranslations: { preview: { scoped: "true", items: { recent: { title: "公開済み記事" } } } },
  });
  await assert.rejects(
    async () => (await invalid.window.fetch("data/catalog_preview.json")).json(),
    /translation scope is invalid/,
    "malformed scope metadata must not fall back to unfiltered source data",
  );
}

async function assertScopedDetailMapDropsMissingPrimaryAndRelatedRows() {
  const harness = createHarness({
    htmlLang: "ko", browserLanguages: ["zh-CN"],
    responsePayload: {
      item_count: 2,
      reports: {
        "ab-recent": { item: { id: "ab-recent", title: "原文" }, related: [
          { id: "cd-recent", title: "相关原文" }, { id: "ab-old", title: "未发布相关原文" },
        ] },
        "ab-old": { item: { id: "ab-old", title: "未发布主条目" }, related: [{ id: "cd-recent", title: "相关原文" }] },
      },
    },
    overlayTranslations: { "detail:ab": { scoped: true, items: {
      "ab-recent": { title: "공개 보고서" }, "cd-recent": { title: "관련 보고서" },
    } } },
  });
  const localized = await (await harness.window.fetch("data/report_details/ab.json")).json();
  assert.deepEqual(Object.keys(localized.reports), ["ab-recent"]);
  assert.equal(localized.reports["ab-recent"].item.title, "공개 보고서");
  assert.deepEqual(localized.reports["ab-recent"].related.map((item) => item.id), ["cd-recent"]);
  assert.equal(localized.item_count, 1);
  assert.equal(JSON.stringify(localized).includes("未发布"), false);
  const empty = harness.window.PortalLocale.localizePayload(
    { item: { id: "absent", title: "Not published" } }, "ko", {}, {}, { scoped: true },
  );
  assert.deepEqual(cloneJson(empty), {}, "an excluded standalone detail primary must become an empty record");
}

async function assertLocalizedReportShellUsesScopedDetailPayload() {
  for (const locale of ["ko", "ja", "ar"]) {
    const reportId = "ab-published";
    const harness = createHarness({
      htmlLang: locale, browserLanguages: ["zh-CN"],
      href: `https://portal.example.invalid/${locale}/report.html?id=${reportId}#download`,
      responsePayloads: {
        "/data/report_details/ab.json": { reports: {
          [reportId]: { item: { id: reportId, title: "Source report", title_zh: "中文原题" }, related: [] },
          "ab-omitted": { item: { id: "ab-omitted", title: "Old report" }, related: [] },
        } },
      },
      overlayTranslations: { "detail:ab": {
        scoped: true, items: { [reportId]: { title: "Published localized title" } },
      } },
    });
    const response = await harness.window.fetch("data/report_details/ab.json");
    const payload = await response.json();
    assert.deepEqual(Object.keys(payload.reports), [reportId]);
    assert.equal(payload.reports[reportId].item.id, reportId);
    assert.equal(payload.reports[reportId].item.title, "Published localized title");
    assert.equal(payload.reports[reportId].item.title_zh, "");
    assert.deepEqual(harness.fetchCalls, ["/data/report_details/ab.json", `/data/i18n/${locale}/catalog-detail-ab.json`],
      "the noindex report shell loads the shared detail shard and only its matching locale overlay");
    assert.equal(harness.redirects.length, 0);
  }
}

async function assertOnDemandSingleDetailHelpers() {
  for (const locale of ["ko", "ja", "ar"]) {
    const harness = createHarness({
      htmlLang: locale,
      href: `https://portal.example.invalid/${locale}/report.html?id=ab-new`,
      responsePayloads: { "/data/report_details/ab.json": { reports: {
        "ab-new": { item: { id: "ab-new", title: "未发布中文详情" }, related: [
          { id: "ab-published", title: "原关联标题" }, { id: "ab-old", title: "旧内容" },
        ] },
        "ab-old": { item: { id: "ab-old", title: "不得整批放行" }, related: [] },
      } } },
      overlayTranslations: { "detail:ab": { scoped: true, items: {
        "ab-published": { title: "Published related title" },
      } } },
    });
    assert.equal(await harness.window.PortalLocale.detailTranslation("catalog", "ab-new"), null);
    assert.equal((await harness.window.PortalLocale.detailTranslation("catalog", "ab-published")).title, "Published related title");
    const record = await harness.window.PortalLocale.readCatalogDetail("ab-new", { title: "One on-demand title" });
    assert.equal(record.item.id, "ab-new");
    assert.equal(record.item.title, "One on-demand title");
    assert.deepEqual(record.related.map((item) => item.id), ["ab-published"]);
    assert.equal(await harness.window.PortalLocale.readCatalogDetail("../private", { title: "x" }), null);
    assert.equal(await harness.window.PortalLocale.detailTranslation("external", "123456"), null);
    assert.deepEqual(harness.fetchCalls, [`/data/i18n/${locale}/catalog-detail-ab.json`, "/data/report_details/ab.json"],
      "Read only one existing overlay and current detail shard, never the full catalog or provider API");
  }
  const chinese = createHarness({ htmlLang: "zh-Hans" });
  assert.equal(await chinese.window.PortalLocale.detailTranslation("catalog", "ab-new"), null);
  assert.equal(await chinese.window.PortalLocale.readCatalogDetail("ab-new", { title: "x" }), null);
  assert.equal(chinese.fetchCalls.length, 0);
}

async function assertScopedChartsRequireTheirOwnTranslation() {
  const harness = createHarness({
    htmlLang: "ar", browserLanguages: ["zh-CN"],
    responsePayload: {
      report_count: 2, chart_count: 3,
      reports: [
        { report_id: "selected", title: "原报告", chart_count: 2, charts: [
          { id: "selected-chart", report_id: "selected", analysis_version: "chart-search-v2", title: "原图表" },
          { id: "old-chart", report_id: "selected", analysis_version: "chart-search-v2", title: "未发布图表" },
        ] },
        { report_id: "old-report", title: "未发布报告", charts: [
          { id: "orphan-chart", analysis_version: "chart-search-v2", title: "孤立图表" },
        ] },
      ],
    },
    overlayTranslations: { charts: { scoped: true, items: {
      "report:selected": { title: "التقرير المنشور" },
      "chart:selected-chart": { title: "الرسم المنشور" },
      "chart:orphan-chart": { title: "رسم بلا تقرير" },
    } } },
  });
  const localized = await (await harness.window.fetch("data/chart_search_index.json")).json();
  assert.equal(localized.reports.length, 1);
  assert.equal(localized.reports[0].charts.length, 1, "a translated parent report must not admit an untranslated chart");
  assert.equal(localized.reports[0].charts[0].title, "الرسم المنشور");
  assert.equal(localized.reports[0].chart_count, 1);
  assert.equal(localized.report_count, 1);
  assert.equal(localized.chart_count, 1);
  assert.equal(JSON.stringify(localized).includes("未发布"), false);
}

async function assertScopedHotReportsStayLazyAndDoNotExposeOmissions() {
  const harness = createHarness({
    htmlLang: "ja", browserLanguages: ["zh-CN"],
    overlayTranslations: { "hot-reports": {
      scoped: true, sourceGeneration: "0123456789abcdef",
      items: { "hot:0123456789abcdef": { title: "公開済みホットレポート" } },
    } },
  });
  assert.equal(harness.fetchCalls.length, 0);
  const localized = await harness.window.PortalLocale.localizeHotReports({
    generation: "0123456789abcdef", total: 2,
    items: [
      { id: "hot:0123456789abcdef", title: "原文" },
      { id: "hot:1111111111111111", title: "未发布原文" },
    ],
  });
  assert.equal(localized.items.length, 1);
  assert.equal(localized.total, 1);
  assert.equal(localized.items[0].title_zh, "");
  assert.equal(JSON.stringify(localized).includes("未发布原文"), false);
  assert.deepEqual(harness.fetchCalls, ["/data/i18n/ja/hot-reports.json"]);
}

function assertArabicInputDirection() {
  const harness = createHarness({
    htmlLang: "ar",
    browserLanguages: ["zh-CN"],
    initialControls: [
      { tagName: "input", type: "text" },
      { tagName: "input", type: "search" },
      { tagName: "textarea" },
      { tagName: "input", type: "password" },
    ],
  });
  const [textInput, searchInput, textarea, passwordInput] = harness.initialControlNodes;
  assert.equal(textInput.getAttribute("dir"), "auto");
  assert.equal(searchInput.getAttribute("dir"), "auto");
  assert.equal(textarea.getAttribute("dir"), "auto");
  assert.equal(passwordInput.getAttribute("dir"), null);

  const dynamicText = harness.document.createElement("input");
  dynamicText.setAttribute("type", "text");
  harness.document.body.append(dynamicText);
  assert.equal(dynamicText.getAttribute("dir"), "auto", "dynamic Arabic text inputs must use automatic direction");

  const dynamicTextarea = harness.document.createElement("textarea");
  harness.document.body.append(dynamicTextarea);
  assert.equal(dynamicTextarea.getAttribute("dir"), "auto", "dynamic Arabic textareas must use automatic direction");
}

function assertDynamicLinkLocalization() {
  const harness = createHarness({
    htmlLang: "ar",
    browserLanguages: ["zh-CN"],
    href: "https://portal.example.invalid/ar/?campaign=one#home",
  });

  const internal = harness.appendAnchor("/reports/report-1.html?q=energy#summary");
  assert.equal(
    internal.getAttribute("href"),
    "https://portal.example.invalid/ar/reports/report-1.html?q=energy#summary",
    "a dynamically inserted internal link must inherit the content locale",
  );

  for (const sharedHref of [
    "/data/catalog.json?v=1#items",
    "/api/search?q=energy#results",
    "/assets/app.js?v=2#runtime",
  ]) {
    const shared = harness.appendAnchor(sharedHref);
    assert.equal(
      shared.getAttribute("href"),
      sharedHref,
      `${sharedHref} is shared infrastructure and must not receive a locale prefix`,
    );
  }
  for (const attributes of [
    { "data-kc-chinese-entry": "" },
    { "data-kc-chinese-entry": "true" },
    { hreflang: "zh-Hans" },
    { hreflang: "zh-CN" },
    { hreflang: "zh" },
  ]) {
    const anchor = harness.document.createElement("a");
    const chineseHref = "/report.html?id=report-1&ref=recovery#download";
    anchor.setAttribute("href", chineseHref);
    for (const [name, value] of Object.entries(attributes)) anchor.setAttribute(name, value);
    harness.document.body.append(anchor);
    assert.equal(anchor.getAttribute("href"), chineseHref,
      "an explicitly Chinese recovery link must retain its root path, query and hash");
  }
  const wrapper = harness.document.createElement("section");
  const nested = harness.document.createElement("a");
  nested.setAttribute("href", "https://portal.example.invalid/reports/report-1.html?q=bank#source");
  nested.setAttribute("data-kc-chinese-entry", "");
  wrapper.append(nested);
  harness.document.body.append(wrapper);
  assert.equal(nested.href, "https://portal.example.invalid/reports/report-1.html?q=bank#source",
    "a fallback inside dynamically inserted markup must also remain Chinese");
  assert.equal(harness.redirects.length, 0, "link rewriting must not navigate the page");
}

function assertIndexUiLocalization() {
  const expected = {
    ko: {
      labels: ["기관", "산업", "시작일", "종료일", "검색 범위", "표시 행 수"],
      buttons: ["초기화", "이전", "다음"], page: "페이지", reports: "개 보고서", of: "/", updated: "업데이트",
      industries: ["은행 / 금융", "에너지 / 유틸리티", "주식 전략", "헬스케어 / 바이오", "금속 / 광업"],
    },
    ja: {
      labels: ["機関", "業種", "開始日", "終了日", "検索対象", "表示件数"],
      buttons: ["クリア", "前へ", "次へ"], page: "ページ", reports: "件のレポート", of: "/", updated: "更新",
      industries: ["銀行 / 金融", "エネルギー / 公益事業", "株式戦略", "ヘルスケア / バイオ", "金属 / 鉱業"],
    },
    ar: {
      labels: ["المؤسسة", "القطاع", "من تاريخ", "إلى تاريخ", "نطاق البحث", "عدد الصفوف"],
      buttons: ["مسح", "السابق", "التالي"], page: "الصفحة", reports: "تقرير", of: "من", updated: "آخر تحديث",
      industries: ["البنوك / الخدمات المالية", "الطاقة / المرافق", "استراتيجية الأسهم", "الرعاية الصحية / التقنية الحيوية", "المعادن / التعدين"],
    },
  };
  for (const [htmlLang, words] of Object.entries(expected)) {
    const harness = createHarness({ htmlLang, browserLanguages: ["zh-CN"], indexUi: true });
    const get = (id) => harness.document.getElementById(id);
    ["bankFilter", "industryFilter", "startDate", "endDate", "scopeFilter", "pageSize"].forEach((id, i) => {
      assert.equal(get(id).parentNode.querySelector("span").textContent, words.labels[i], `${htmlLang}/${id}`);
    });
    ["clearFilters", "prevPage", "nextPage"].forEach((id, i) => assert.equal(get(id).textContent, words.buttons[i]));
    const options = get("industryFilter").querySelectorAll("option");
    options.slice(1).forEach((option, i) => assert.equal(option.textContent, `${words.industries[i]} (8)`));
    assert.equal(get("bankFilter").querySelectorAll("option")[1].textContent, "J.P. Morgan (12)");
    assert.equal(get("pageSize").querySelectorAll("option")[0].textContent, "50");
    assert.equal(get("pageInfo").textContent, `${words.page} 1 ${words.of} 1`);
    assert.equal(get("resultCount").textContent, `40 ${words.of} 40 ${words.reports}`);
    assert.ok(get("catalogMeta").textContent.startsWith(`14551 ${words.reports} | ${words.updated} 2026-09-06 10:44:48 +0800 | `));
    assert.doesNotMatch(get("catalogMeta").textContent, /reports|Updated|Title and catalog/);
    assert.deepEqual(get("scopeFilter").querySelectorAll("option").map((option) => option.value), ["all", "title", "catalog", "fulltext", "charts"]);
    assert.ok(get("scopeFilter").querySelectorAll("option").every((option) => option.textContent !== option.value));

    get("industryFilter").value = "Banks / Financials";
    options[1].selected = true;
    get("prevPage").disabled = true;
    const click = () => {};
    get("nextPage").onclick = click;
    const before = harness.mutationCount();
    get("pageInfo").textContent = "Page 2 / 7";
    get("resultCount").textContent = "25 of 350 reports";
    get("catalogMeta").textContent = "350 reports | Updated 2026-09-07 10:44:48 +0800 | Text index 90 reports + (recent text)";
    options[1].textContent = "Banks / Financials (12)";
    assert.equal(get("pageInfo").textContent, `${words.page} 2 ${words.of} 7`);
    assert.equal(get("resultCount").textContent, `25 ${words.of} 350 ${words.reports}`);
    assert.doesNotMatch(get("catalogMeta").textContent, /reports|Updated|Text index|recent text/);
    assert.ok(get("catalogMeta").textContent.includes("2026-09-07 10:44:48 +0800"));
    assert.ok(get("catalogMeta").textContent.includes("90"));
    assert.equal(options[1].textContent, `${words.industries[0]} (12)`);
    assert.equal(options[1].value, "Banks / Financials");
    assert.equal(options[1].selected, true);
    assert.equal(get("industryFilter").value, "Banks / Financials");
    assert.equal(get("prevPage").disabled, true);
    assert.equal(get("nextPage").onclick, click);
    assert.ok(harness.mutationCount() - before <= 8, "four external updates require at most four local text writes");
    const inserted = harness.document.createElement("option");
    inserted.value = "Energy / Utilities";
    inserted.textContent = "Energy / Utilities (19)";
    get("industryFilter").append(inserted);
    assert.equal(inserted.textContent, `${words.industries[1]} (19)`, "newly inserted industry options must be translated");
    assert.equal(inserted.value, "Energy / Utilities");
    const properName = harness.document.createElement("option");
    properName.value = "Goldman Sachs";
    properName.textContent = "Goldman Sachs (7)";
    get("bankFilter").append(properName);
    assert.equal(properName.textContent, "Goldman Sachs (7)");

    // A framework may update an existing text node instead of textContent.
    get("pageInfo")._textContent = "Page 0 / 0";
    const textNode = { nodeType: 3, parentNode: get("pageInfo") };
    get("pageInfo").children.push(textNode);
    harness.document.notify({ type: "characterData", target: textNode });
    assert.equal(get("pageInfo").textContent, `${words.page} 0 ${words.of} 0`);
    const settled = harness.mutationCount();
    harness.document.notify({ type: "childList", target: get("industryFilter"), addedNodes: [] });
    assert.equal(harness.mutationCount(), settled + 1, "already localized text must not trigger another mutation");
    assert.equal(harness.fetchCalls.length, 0, "fixed UI localization must not add requests");
    assert.equal(harness.redirects.length, 0);
  }

  const chinese = createHarness({ htmlLang: "zh-Hans", browserLanguages: ["zh-CN"], indexUi: true });
  const get = (id) => chinese.document.getElementById(id);
  assert.equal(get("industryFilter").parentNode.querySelector("span").textContent, "行业");
  assert.equal(get("startDate").parentNode.querySelector("span").textContent, "From");
  assert.equal(get("prevPage").textContent, "上一个");
  assert.equal(get("nextPage").textContent, "下一页");
  get("pageInfo").textContent = "Page 2 / 7";
  get("resultCount").textContent = "25 of 350 reports";
  assert.equal(get("pageInfo").textContent, "Page 2 / 7");
  assert.equal(get("resultCount").textContent, "25 of 350 reports");
  assert.equal(chinese.observerCount(), 0);
  assert.equal(chinese.fetchCalls.length, 0);
  assert.equal(chinese.redirects.length, 0);
  assert.ok(Buffer.byteLength(runtimeSource, "utf8") < 32768, "shared locale runtime must remain within the release byte budget");
}

(async () => {
  assertNoSwitcherForSimplifiedChinese();
  assertLocalePathMapping();
  assertLocaleFormattingConfiguration();
  assertSwitcherForEveryLocalizedPage();
  assertChinesePagesNeverShowLanguageSwitcher();
  await assertCatalogTitleOverlay();
  await assertOverlaySelectionAndUnrelatedJsonIsolation();
  await assertReportDetailUsesPrefixOverlay();
  await assertChartContentOverlay();
  await assertHotReportOverlayIsLazyAndGenerationBound();
  await assertHotReportLocaleQueryFoldingAndFallback();
  await assertScopedCatalogExcludesUnpublishedRowsOnly();
  await assertScopedDetailMapDropsMissingPrimaryAndRelatedRows();
  await assertLocalizedReportShellUsesScopedDetailPayload();
  await assertOnDemandSingleDetailHelpers();
  await assertScopedChartsRequireTheirOwnTranslation();
  await assertScopedHotReportsStayLazyAndDoNotExposeOmissions();
  assertArabicInputDirection();
  assertDynamicLinkLocalization();
  assertIndexUiLocalization();
  console.log("portal locale runtime contract: ok");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
