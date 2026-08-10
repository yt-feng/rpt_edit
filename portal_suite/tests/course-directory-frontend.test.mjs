import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const stylesPath = path.join(root, "portal_suite/site_src/assets/styles.css");
const pagePath = path.join(root, "portal_suite/site_src/courses.html");

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
