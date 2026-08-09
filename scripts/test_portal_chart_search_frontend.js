#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const html = fs.readFileSync(path.join(root, "portal_suite/site_src/index.html"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");

assert.match(html, /<option value="charts">图表文字<\/option>/);
assert.match(html, /id="chartSearchSection"/);
assert.match(html, /id="chartSearchResults"/);
assert.match(app, /loadOptionalJson\("data\/chart_search_index\.json"/);
assert.match(app, /queryScope === "charts"/);
assert.match(app, /scoreItem\(item, query, scopeFilter\.value, metadataById, searchTextById, chartTextById\)/);
assert.match(app, /reportPageUrl\(reportId\)/);
assert.match(app, /scopeFilter\.value === "charts"/);

console.log("portal chart-search frontend contract: ok");
