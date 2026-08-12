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

assert.match(html, /<option value="charts">图表文字<\/option>/);
assert.match(html, /id="chartSearchSection"/);
assert.match(html, /id="chartSearchResults"/);
assert.match(app, /loadOptionalJson\("data\/chart_search_index\.json"/);
assert.match(app, /queryScope === "charts"/);
assert.match(app, /scoreItem\(item, query, scopeFilter\.value, metadataById, searchTextById, chartTextById, titleSearchById\)/);
assert.match(app, /reportPageUrl\(reportId\)/);
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
assert.match(chartsApp, /report\.html\?id=/);
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

console.log("portal chart-search frontend contract: ok");
