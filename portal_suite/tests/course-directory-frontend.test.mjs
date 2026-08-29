import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const stylesPath = path.join(root, "portal_suite/site_src/assets/styles.css");
const pagePath = path.join(root, "portal_suite/site_src/courses.html");
const materialsPath = path.join(root, "portal_suite/site_src/data/course-materials.json");

test("course page keeps all member directory records out of static HTML", async () => {
  const html = await readFile(pagePath, "utf8");
  const restrictedMarkers = [
    ["W", "SO"].join(""),
    ["W", "SP"].join(""),
    ["Fundamental", " Edge"].join(""),
  ];
  assert.match(html, /id="courseCatalog"[^>]*hidden/u);
  assert.doesNotMatch(html, /course\/directory|data-directory-file|courseDirectoryPopular/u);
  for (const marker of restrictedMarkers) assert.equal(html.includes(marker), false);
});

test("directory API is authenticated and mounted only after course access succeeds", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /fetch\(requestUrl\(\), \{ cache: "no-store", headers: authHeaders\(\)/u);
  assert.match(source, /`\$\{workerUrl\}\/course\/directory\?\$\{params\.toString\(\)\}`/u);
  assert.match(source, /if \(!data\.can_access\)[\s\S]*?renderCourseCatalog\(data\);/u);
  assert.equal((source.match(/setupCourseDirectoryIndex\(products\)/gu) || []).length, 2);
  assert.doesNotMatch(source, /course\/resources/u);
});

test("member directory supports filters, entity hooks, hierarchy, and pagination", async () => {
  const source = await readFile(appPath, "utf8");
  for (const marker of [
    "courseDirectoryCategory",
    "courseDirectoryProduct",
    "courseDirectorySearch",
    "courseDirectoryFileType",
    "courseDirectoryPopular",
    "courseDirectoryPagination",
    "courseDirectoryExpand",
    "courseDirectoryCollapse",
  ]) assert.match(source, new RegExp(marker, "u"));
  for (const queryField of ["q", "course_id", "category", "file_type", "page", "page_size"]) {
    assert.match(source, new RegExp(`params\\.set\\(\"${queryField}\"`, "u"));
  }
  assert.match(source, /facets\.top_entities/u);
  assert.match(source, /data-directory-entity/u);
  assert.match(source, /Array\.isArray\(value\.folders\)/u);
  assert.match(source, /<details class="course-directory-tree"/u);
  assert.match(source, /escapeHtml\(item\.name\)/u);
  assert.match(source, /entity\.name/u);
});

test("course directory styles retain the portal layout on desktop and mobile", async () => {
  const styles = await readFile(stylesPath, "utf8");
  assert.match(styles, /\.course-directory-controls\s*\{[\s\S]*?grid-template-columns:/u);
  assert.match(styles, /\.course-directory-popular button/u);
  assert.match(styles, /\.course-directory-tree\s*\{/u);
  assert.match(styles, /\.course-directory-file\s*\{/u);
  assert.match(styles, /@media \(max-width: 520px\)[\s\S]*?\.course-directory-controls\s*\{[\s\S]*?grid-template-columns:\s*1fr/u);
});

test("public Maifu teaser sits between the hero and the protected member catalog", async () => {
  const html = await readFile(pagePath, "utf8");
  const heroAt = html.indexOf('class="course-hero"');
  const materialsAt = html.indexOf('id="courseMaterials"');
  const gateAt = html.indexOf('id="courseGate"');
  assert.ok(heroAt >= 0 && materialsAt > heroAt && gateAt > materialsAt);
  for (const marker of [
    'id="courseMaterialsTitle"',
    'id="courseMaterialsPrevious"',
    'id="courseMaterialsNext"',
    'id="courseMaterialsPosition"',
    'id="courseMaterialsTrack"',
    'aria-roledescription="轮播"',
  ]) assert.ok(html.includes(marker), marker);
  assert.doesNotMatch(html, /\.pdf|source_filename|sha256|_course-directory|R2/u);
});

test("Maifu manifest exposes twenty safe teaser records without storage locations", async () => {
  const manifest = JSON.parse(await readFile(materialsPath, "utf8"));
  assert.equal(manifest.schema_version, 1);
  assert.equal(manifest.course.id, "str-01");
  assert.equal(manifest.items.length, 20);
  assert.equal(new Set(manifest.items.map((item) => item.id)).size, 20);
  assert.ok(manifest.items.some((item) => item.featured === true));
  for (const item of manifest.items) {
    assert.match(item.id, /^maifu-\d{2}$/u);
    assert.match(item.cover, /^assets\/course-covers\/[a-z0-9._-]+\.webp$/u);
    assert.ok(Number.isInteger(item.pages) && item.pages > 0);
    assert.equal(/[\\/]/u.test(item.source_filename), false);
    assert.equal(Object.hasOwn(item, "r2_key"), false);
    assert.equal(Object.hasOwn(item, "source_path"), false);
  }
});

test("Maifu carousel is native, responsive, motion-aware, and keyboard operable", async () => {
  const [source, styles] = await Promise.all([
    readFile(appPath, "utf8"),
    readFile(stylesPath, "utf8"),
  ]);
  assert.match(source, /loadOptionalJson\("data\/course-materials\.json", null\)/u);
  assert.match(source, /loading="\$\{priority \? "eager" : "lazy"\}"/u);
  assert.match(source, /fetchpriority="high"/u);
  assert.match(source, /COURSE_MATERIAL_AUTOPLAY_MS = 6000/u);
  assert.match(source, /matchMedia\("\(prefers-reduced-motion: reduce\)"\)/u);
  for (const eventName of ["pointerenter", "pointerleave", "focusin", "focusout", "keydown"]) {
    assert.match(source, new RegExp(`addEventListener\\("${eventName}"`, "u"));
  }
  assert.match(source, /event\.key === "ArrowLeft" \|\| event\.key === "ArrowRight"/u);
  assert.match(source, /materialsTrack\.scrollTo\(/u);
  assert.match(styles, /\.course-materials-track\s*\{[\s\S]*?grid-auto-columns:\s*calc\(\(100% - 32px\) \/ 3\)[\s\S]*?scroll-snap-type:\s*inline mandatory/u);
  assert.match(styles, /\.course-material-cover\s*\{[\s\S]*?aspect-ratio:\s*16 \/ 9/u);
  assert.match(styles, /\.course-materials-arrow\s*\{[\s\S]*?width:\s*44px;[\s\S]*?height:\s*44px/u);
  assert.match(styles, /@media \(max-width: 520px\)[\s\S]*?\.course-materials-track\s*\{[\s\S]*?grid-auto-columns:\s*90%/u);
  assert.match(styles, /@media \(prefers-reduced-motion: reduce\)[\s\S]*?scroll-behavior:\s*auto/u);
});

test("member material reader opens synchronously and fetches only by public material id", async () => {
  const source = await readFile(appPath, "utf8");
  const start = source.indexOf("async function openCourseMaterial");
  const end = source.indexOf("async function setupCourseMaterials", start);
  assert.ok(start >= 0 && end > start);
  const reader = source.slice(start, end);
  assert.ok(reader.indexOf('window.open("about:blank", "_blank")') < reader.indexOf("await fetch("));
  assert.match(reader, /fetch\(`\$\{workerUrl\}\/course\/material\?id=\$\{encodeURIComponent\(item\.id\)\}`/u);
  assert.match(reader, /method: "GET",[\s\S]*?cache: "no-store",[\s\S]*?headers: authHeaders\(\)/u);
  assert.match(reader, /await response\.blob\(\)/u);
  assert.match(reader, /URL\.createObjectURL\(blob\)/u);
  assert.match(reader, /readerWindow\.location\.replace\(objectUrl\)/u);
  assert.match(reader, /window\.location\.assign\(objectUrl\)/u);
  assert.match(reader, /readerWindow\.close\(\)/u);
  assert.match(reader, /URL\.revokeObjectURL\(objectUrl\)/u);
  assert.match(reader, /showAccountModal\(workerUrl\)/u);
  assert.doesNotMatch(reader, /source_filename|source_path|r2_key|sha256/iu);
});
