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
  href = "https://kcdesk.com/reports/example.html?from=test#summary",
  responsePayload = { items: [] },
  responsePayloads = {},
  titleTranslations = {},
  itemTranslations = {},
  overlayTranslations = {},
  overlayFailures = [],
  initialControls = [],
} = {}) {
  const observers = [];
  const redirects = [];
  const fetchCalls = [];
  let currentHref = href;
  let document;

  class ElementMock {
    constructor(tagName) {
      this.nodeType = 1;
      this.tagName = String(tagName || "div").toUpperCase();
      this.children = [];
      this.parentNode = null;
      this.attributes = new Map();
      this.dataset = {};
      this.className = "";
      this.textContent = "";
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
      if (selector === "textarea") return this.tagName === "TEXTAREA";
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
  const body = new ElementMock("body");

  document = {
    readyState: "complete",
    documentElement: html,
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
    notifyAdded(node) {
      for (const callback of observers) callback([{ addedNodes: [node] }]);
    },
  };
  const initialControlNodes = initialControls.map(({ tagName, type }) => {
    const control = document.createElement(tagName);
    if (type) control.setAttribute("type", type);
    document.body.append(control);
    return control;
  });

  class MutationObserverMock {
    constructor(callback) {
      this.callback = callback;
    }

    observe() {
      observers.push(this.callback);
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
  };
}

function assertNoSwitcherForSimplifiedChinese() {
  for (const browserLocale of ["zh-CN", "zh-Hans"]) {
    const originalHref = "https://kcdesk.com/reports/?q=semiconductor#latest";
    const harness = createHarness({
      htmlLang: "zh-Hans",
      browserLanguages: [browserLocale, "en-US"],
      href: originalHref,
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
  const source = "https://kcdesk.com/ko/reports/alpha.html?q=bank%20risk#source";
  for (const locale of ["ko", "ja", "ar"]) {
    const mapped = new URL(harness.window.KCDeskLocale.localeUrl(locale, source));
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
    assert.equal(harness.window.KCDeskLocale.contentLocale, htmlLang);
    assert.equal(harness.window.KCDeskLocale.intlLocale, intlLocale);
    assert.equal(harness.window.KCDeskLocale.direction, direction);
  }
}

function assertSwitcherForNonSimplifiedBrowser() {
  const harness = createHarness({
    htmlLang: "ja",
    browserLanguage: "en-US",
    browserLanguages: ["zh-CN", "en-US"],
    href: "https://kcdesk.com/ja/reports/example.html?ref=nav#top",
  });
  const switcher = harness.document.querySelector("[data-kc-locale-switcher]");
  assert.ok(switcher, "a non-Simplified-Chinese browser must create the locale switcher");
  assert.equal(switcher.tagName, "NAV");
  assert.equal(switcher.children.length, 4, "switcher must expose all configured locales");
  const chineseLink = switcher.children.find((link) => link.hreflang === "zh-Hans");
  assert.ok(chineseLink, "switcher must include the Chinese root-site link");
  assert.equal(
    chineseLink.href,
    "https://kcdesk.com/reports/example.html?ref=nav#top",
    "the link observer must not rewrite the switcher's Chinese root-site link back into the current locale",
  );
  assert.equal(harness.redirects.length, 0, "creating the switcher must not navigate");
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
  const localized = await harness.window.KCDeskLocale.localizeHotReports({
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

  const newerGeneration = await harness.window.KCDeskLocale.localizeHotReports({
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

  const missingGeneration = await harness.window.KCDeskLocale.localizeHotReports({
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
  const unavailable = await unavailableHarness.window.KCDeskLocale.localizeHotReports({
    generation: "0123456789abcdef",
    items: [cloneJson(original)],
  });
  assert.equal(unavailable.locale_translation_pending, true);
  assert.deepEqual(Array.from(unavailable.items), [], "an unavailable overlay must not expose source-language list items");

  const chineseHarness = createHarness({ htmlLang: "zh-Hans", browserLanguages: ["zh-CN"] });
  const chinese = await chineseHarness.window.KCDeskLocale.localizeHotReports({
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
      Array.from(await harness.window.KCDeskLocale.matchHotReportLocaleIds(query)),
      [matchingId.slice("hot:".length)],
      `${locale} query folding must match localized public fields`,
    );
    assert.deepEqual(
      Array.from(await harness.window.KCDeskLocale.matchHotReportLocaleIds("definitely absent")),
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
    await unavailable.window.KCDeskLocale.matchHotReportLocaleIds("半導体"),
    null,
    "an unavailable overlay must signal the app to keep the source-only query",
  );
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
    href: "https://kcdesk.com/ar/?campaign=one#home",
  });

  const internal = harness.appendAnchor("/reports/report-1.html?q=energy#summary");
  assert.equal(
    internal.getAttribute("href"),
    "https://kcdesk.com/ar/reports/report-1.html?q=energy#summary",
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
  assert.equal(harness.redirects.length, 0, "link rewriting must not navigate the page");
}

(async () => {
  assertNoSwitcherForSimplifiedChinese();
  assertLocalePathMapping();
  assertLocaleFormattingConfiguration();
  assertSwitcherForNonSimplifiedBrowser();
  await assertCatalogTitleOverlay();
  await assertOverlaySelectionAndUnrelatedJsonIsolation();
  await assertReportDetailUsesPrefixOverlay();
  await assertChartContentOverlay();
  await assertHotReportOverlayIsLazyAndGenerationBound();
  await assertHotReportLocaleQueryFoldingAndFallback();
  assertArabicInputDirection();
  assertDynamicLinkLocalization();
  console.log("portal locale runtime contract: ok");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
