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

const reportSearchUrl = Function(
  "clean",
  `"use strict"; ${extractFunction(chartsApp, "reportSearchUrl")}; return reportSearchUrl;`,
)((value, limit) => String(value || "").trim().slice(0, limit));
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

console.log("portal chart-search frontend contract: ok");
