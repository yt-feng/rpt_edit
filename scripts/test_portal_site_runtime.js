#!/usr/bin/env node

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

const root = path.resolve(__dirname, "..");
const read = (relative) => fs.readFileSync(path.join(root, relative), "utf8");
const runtime = read("portal_suite/site_src/assets/site-runtime.js");
const styles = read("portal_suite/site_src/assets/styles.css");

assert.match(runtime, /2019-10-03T00:00:00\+08:00/u);
assert.match(runtime, /data-site-runtime-value/u);
assert.match(runtime, /window\.setInterval\(update, SECOND\)/u);
assert.match(runtime, /ensurePrimaryNavigation/u);
assert.match(runtime, /createLink\("courses\.html", "Course"/u);
assert.match(runtime, /createLink\("charts", "Charts"/u);
assert.match(runtime, /\/charts\(\?:\\\.html\)\?\\\/\?\$/u);
assert.match(runtime, /charts\.href = "\/charts"/u);
assert.match(styles, /\.site-runtime-banner/u);

for (const page of [
  "index", "report", "doc", "delivery", "newsfeed", "activity",
  "privacy", "refund", "terms", "courses", "charts",
]) {
  const html = read(`portal_suite/site_src/${page}.html`);
  assert.match(html, /assets\/site-runtime\.js/u, `${page}.html must load the runtime banner`);
}

const builder = read("scripts/build_portal_suite_site.py");
assert.ok((builder.match(/assets\/site-runtime\.js/g) || []).length >= 4,
  "generated Blog and report templates must load the runtime banner");

console.log("portal runtime banner and primary navigation contract: ok");
