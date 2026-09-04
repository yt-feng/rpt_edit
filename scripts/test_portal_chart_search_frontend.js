#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const html = fs.readFileSync(path.join(root, "portal_suite/site_src/index.html"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const chartsHtml = fs.readFileSync(path.join(root, "portal_suite/site_src/charts.html"), "utf8");
const chartsApp = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/charts.js"), "utf8");
const chartsCss = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/charts.css"), "utf8");
const runtime = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/site-runtime.js"), "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    if (source[index] === "}" && --depth === 0) return source.slice(start, index + 1);
  }
  throw new Error(`${name} body is incomplete`);
}

assert.match(html, /<option value="charts">图表文字<\/option>/);
assert.match(html, /id="chartSearchSection"/);
assert.match(html, /id="chartSearchResults"/);
assert.match(app, /loadOptionalJson\("data\/chart_search_index\.json"/);
assert.match(app, /queryScope === "charts"/);
assert.match(app, /scoreItem\(item, query, scopeFilter\.value, metadataById, searchTextById, chartTextById, titleSearchById\)/);
assert.match(app, /reportPageUrl\(reportId, \{ preview:/);
assert.match(app, /catalogItem \|\| \{ \.\.\.report, id: reportId, title: reportTitle \}/);
assert.match(app, /scopeFilter\.value === "charts"/);

assert.match(chartsHtml, /data-page="charts"/);
assert.match(chartsHtml, /canonical" href="https:\/\/portal\.example\.invalid\/charts"/);
assert.match(chartsHtml, /id="chartGallery"/);
assert.match(chartsHtml, /id="chartQuery"/);
assert.match(chartsHtml, /assets\/charts\.js/);
assert.match(chartsHtml, /assets\/charts\.css/);
assert.doesNotMatch(chartsHtml, /assets\/app\.js/);
assert.match(chartsApp, /data\/chart_search_index\.json/);
assert.match(chartsApp, /\/charts\/image\?id=/);
assert.match(chartsApp, /new URLSearchParams\(\{ id:/);
assert.match(chartsApp, /available: typeof report\.available === "boolean"/);
assert.match(chartsApp, /sourceReportUrl\(row\)/);
assert.match(chartsApp, /document\.createElement\("button"\)/);
assert.match(chartsApp, /aria-haspopup/);
assert.match(chartsApp, /openChartLightbox\(row, media\)/);
assert.match(chartsApp, /event\.key === "Escape"/);
assert.match(chartsApp, /在首页搜索来源报告/);
assert.match(chartsApp, /VALID_KINDS/);
assert.match(chartsApp, /INVALID_RE/);
assert.match(chartsApp, /quality_score/);
assert.match(chartsApp, /analysis_version/);
assert.match(chartsApp, /chart-search-v2/);
assert.match(chartsApp, /replaceChildren/);
assert.doesNotMatch(chartsApp, /innerHTML\s*=/);
assert.match(app, /function chartReportText\([\s\S]*?publicBrandText\(row\.title\)[\s\S]*?publicBrandText\(row\.search_text\)/u);
assert.match(app, /function chartSearchRow\([\s\S]*?publicBrandText\(report\.title[\s\S]*?publicBrandText\(chart\.title[\s\S]*?chartDetailChips\(chart\)/u);
assert.match(chartsCss, /\.charts-grid/);
assert.match(runtime, /createLink\("charts", "Charts"/);
assert.match(runtime, /Charts/);
assert.match(runtime, /href = "\/charts"/);

const reportUrl = Function(
  "URLSearchParams",
  `"use strict"; ${extractFunction(chartsApp, "reportUrl")}; return reportUrl;`,
)(URLSearchParams);
const archivedUrl = reportUrl("report-1", {
  title: "Archived report",
  available: false,
  pdf_archived: true,
  page_count: 22,
});
assert.match(archivedUrl, /available=0/);
assert.match(archivedUrl, /pdf_archived=1/);
assert.match(archivedUrl, /page_count=22/);
const unknownUrl = reportUrl("report-2", { title: "Unknown report" });
assert.doesNotMatch(unknownUrl, /available=/);

const publicBoundaryStart = chartsApp.indexOf("const LEGACY_SOURCE_WORDS");
const publicBoundaryEnd = chartsApp.indexOf("function folded", publicBoundaryStart);
assert.ok(publicBoundaryStart >= 0 && publicBoundaryEnd > publicBoundaryStart);
const publicText = Function(
  "PUBLIC_BRAND",
  `"use strict"; ${chartsApp.slice(publicBoundaryStart, publicBoundaryEnd)}; return publicText;`,
)("KC桌面");

for (const source of [app, chartsApp]) {
  const arabicFold = Function(
    "CONTENT_INTL_LOCALE",
    `"use strict"; ${extractFunction(source, "localeSearchText")}; return localeSearchText;`,
  )("ar");
  assert.equal(
    arabicFold("إِمـارات أَسْهُم آفاق ٱستثمار ى"),
    "امارات اسهم افاق استثمار ي",
    "Arabic search must ignore harakat/tatweel and normalize common alef/ya variants",
  );
  const chineseFold = Function(
    "CONTENT_INTL_LOCALE",
    `"use strict"; ${extractFunction(source, "localeSearchText")}; return localeSearchText;`,
  )("zh-CN");
  assert.equal(chineseFold("Ａ股 AI"), "a股 ai", "Chinese-root folding must retain its existing NFKC behavior");
}

const reportSearchUrl = Function(
  "clean",
  "publicText",
  `"use strict"; ${extractFunction(chartsApp, "reportSearchUrl")}; return reportSearchUrl;`,
)((value, limit) => String(value || "").trim().slice(0, limit), publicText);
assert.equal(
  reportSearchUrl("Bernstein HPQ source report"),
  "/?q=Bernstein%20HPQ%20source%20report",
);

const sourceReportUrl = Function(
  "reportUrl",
  "reportSearchUrl",
  `"use strict"; ${extractFunction(chartsApp, "sourceReportUrl")}; return sourceReportUrl;`,
)(reportUrl, reportSearchUrl);
assert.match(sourceReportUrl({ reportId: "report-1", reportPreview: {} }), /report\.html\?id=report-1/u);
assert.equal(
  sourceReportUrl({ reportId: "", reportTitle: "Unlinked source title", reportPreview: {} }),
  "/?q=Unlinked%20source%20title",
);

const publicList = (value) => (Array.isArray(value) ? value.map((item) => publicText(item)).filter(Boolean) : []);
const flattenIndex = Function(
  "clean",
  "publicText",
  "publicList",
  "isValidChart",
  "normalizedKind",
  "searchableText",
  "PUBLIC_BRAND",
  `"use strict"; ${extractFunction(chartsApp, "flattenIndex")}; return flattenIndex;`,
)(
  (value, limit = 1200) => String(value || "").replace(/\s+/gu, " ").trim().slice(0, limit),
  publicText,
  publicList,
  () => true,
  () => "chart",
  (row) => JSON.stringify(row),
  "KC桌面",
);
const legacyRows = flattenIndex({
  reports: [{
    report_id: "report-legacy",
    title: "Reportify: AI source report",
    title_zh: "NashAI 中文标题",
    filename: "MacroGate-report.pdf",
    bank_name: "Portal Suite",
    charts: [{
      id: "chart-legacy",
      analysis_version: "chart-search-v2",
      image_id: "a".repeat(64),
      chart_type: "Reportify chart",
      title: "Nash AI capacity",
      description: "MacroGate supplied this chart",
      trend_summary: "Portal Suite trend",
      metrics: ["Twotigers metric"],
      entities: ["麦府课堂"],
      keywords: ["maifu source"],
    }],
  }],
});
const forbidden = /Reportify|Nash[\s._-]*AI|Macro[\s._-]*Gate|Portal[\s._-]+Suite|Two[\s._-]*tigers|\bmaifu\b|麦府(?:课堂|学堂)/iu;
assert.equal(legacyRows.length, 1);
assert.doesNotMatch(JSON.stringify(legacyRows), forbidden);
assert.equal(legacyRows[0].title, "capacity");
assert.equal(legacyRows[0].reportTitle, "AI source report");

console.log("portal chart-search frontend contract: ok");
