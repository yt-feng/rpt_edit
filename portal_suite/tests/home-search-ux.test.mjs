import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const htmlPath = new URL("../site_src/index.html", import.meta.url);
const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);

test("home first paint uses a preview and atomically upgrades to the full catalog", async () => {
  const source = await readFile(appPath, "utf8");
  const initIndex = source.slice(source.indexOf("async function initIndex()"), source.indexOf("function filenameFromDisposition"));
  assert.match(source, /loadOptionalJson\("data\/catalog_preview\.json", null\)/);
  assert.ok(
    source.indexOf('loadOptionalJson("data/catalog_preview.json", null)')
      < source.indexOf('const fullCatalogPromise = loadJson("data/catalog.json")'),
    "the small preview must start before the full catalog",
  );
  assert.match(source, /fullCatalogPromise\.then\(async \(fullCatalog\) =>/);
  assert.match(source, /await rebuildCatalogDerivedInChunks\(fullCatalog, catalogPdfOverrides\);\s*fullCatalogReady = true;/);
  assert.match(source, /overrideVersion !== catalogOverrideVersion/);
  assert.match(source, /cache: "reload"/);
  assert.match(source, /loadCatalogPdfOverrides\(workerUrl\)\.then\(\(overrides\) =>/);
  assert.doesNotMatch(initIndex, /const catalogPdfOverrides = await loadCatalogPdfOverrides/);
});

test("home search waits for stable input and cancels superseded remote searches", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /const scheduleLocalRender = \(delay = 240\)/);
  assert.match(source, /compositionstart/);
  assert.match(source, /compositionend/);
  assert.match(source, /remoteSearchController\.abort\(\)/);
  assert.match(source, /remoteSearchGeneration/);
  assert.match(source, /generation === remoteSearchGeneration/);
  assert.match(source, /\}, 480\);/);
});

test("the large full-text corpus is opt-in instead of loading on focus or idle", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /scopeFilter\.value === "fulltext"/);
  assert.match(source, /startTextIndexLoad\(\)/);
  assert.match(source, /loadSearchIndexShards\("data\/search_index_current"\)/);
  assert.doesNotMatch(source, /loadJson\("data\/search_index\.json"\)/);
  assert.doesNotMatch(source, /input\.addEventListener\("focus", startTextIndexLoad\)/);
  assert.doesNotMatch(source, /input\.addEventListener\("input", startTextIndexLoad\)/);
  assert.doesNotMatch(source, /setTimeout\(startTextIndexLoad/);
});

test("loading and multi-source progress are visible without a wait cursor", async () => {
  const [html, styles] = await Promise.all([
    readFile(htmlPath, "utf8"),
    readFile(stylesPath, "utf8"),
  ]);
  assert.match(html, /id="searchReadiness"[^>]*role="status"/);
  assert.match(html, /id="results"[^>]*is-loading[^>]*aria-busy="true"/);
  assert.match(html, /id="searchSourceProgress"[^>]*aria-live="polite"/);
  assert.match(html, /id="searchSourceProgressBar"/);
  assert.match(styles, /\.report-skeleton/);
  assert.match(styles, /\.search-source-progress/);
  assert.doesNotMatch(styles, /cursor:\s*wait/);
});
