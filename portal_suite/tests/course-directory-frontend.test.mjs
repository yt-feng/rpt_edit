import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const stylesPath = path.join(root, "portal_suite/site_src/assets/styles.css");
const pagePath = path.join(root, "portal_suite/site_src/courses.html");
const materialsPath = path.join(root, "portal_suite/site_src/data/course-materials.json");

function extractFunction(source, name) {
  const marker = `async function ${name}(`;
  const start = source.indexOf(marker);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function courseMaterialRequestHarness(response) {
  const calls = [];
  const statuses = [];
  const tracked = [];
  const sandbox = {
    courseMaterialAccess: true,
    workerUrl: "/api",
    gate: { scrollIntoView() {} },
    loadAuthSession() { return { user: { email: "member@example.com" } }; },
    async showAccountModal() {},
    authHeaders() { return { Authorization: "Bearer member-token" }; },
    currentAnalyticsPath() { return "/courses.html"; },
    clearAuthSession() {},
    setCourseMaterialStatus(message, state = "") { statuses.push({ message, state }); },
    trackEvent(workerUrl, type, data) { tracked.push({ workerUrl, type, data }); },
    async fetch(url, init) {
      calls.push({ url: String(url), init });
      return response;
    },
  };
  const request = vm.runInNewContext(`(${extractFunction(appSource, "requestCourseMaterial")})`, sandbox);
  const button = {
    disabled: false,
    textContent: "单独索取",
    dataset: { materialTitle: "示例材料" },
    ariaLabel: "",
    setAttribute(name, value) { if (name === "aria-label") this.ariaLabel = value; },
  };
  return {
    calls,
    statuses,
    tracked,
    button,
    request: () => request({ id: "maifu-01", title: "示例材料" }, button),
  };
}

const appSource = await readFile(appPath, "utf8");

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

test("member-only Maifu carousel shell stays hidden before the Course gate succeeds", async () => {
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
  assert.match(html, /id="courseMaterials"[\s\S]*?hidden/u);
  assert.match(html, /会员封面预览，每份材料均需单独索取/u);
  assert.doesNotMatch(html, /\.pdf|source_filename|sha256|_course-directory|R2/u);
});

test("Maifu publisher manifest keeps twenty canonical records without storage locations", async () => {
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
  const source = appSource;
  const styles = await readFile(stylesPath, "utf8");
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

test("anonymous and ineligible accounts never load or reveal Maifu covers", () => {
  const source = appSource;
  const courseStart = source.indexOf("async function initCourse");
  const refreshStart = source.indexOf("async function refresh()", courseStart);
  const refreshEnd = source.indexOf('login.addEventListener("click"', refreshStart);
  assert.ok(courseStart >= 0 && refreshStart > courseStart && refreshEnd > refreshStart);
  const refresh = source.slice(refreshStart, refreshEnd);
  const deniedAt = refresh.indexOf("if (!data.can_access)");
  const loadAt = refresh.indexOf("await setupCourseMaterials(expectedCourseMaterialEpoch)");
  assert.ok(deniedAt >= 0 && loadAt > deniedAt, "the cover manifest load must follow the access denial branch");
  assert.match(refresh, /if \(!loadAuthSession\(\)\) \{[\s\S]*?locked\([\s\S]*?return;/u);
  assert.match(refresh, /if \(!data\.can_access\) \{[\s\S]*?locked\([\s\S]*?return;/u);
  assert.equal((source.match(/setupCourseMaterials\(/gu) || []).length, 2);
  assert.match(source, /if \(!courseMaterialAccess \|\| expectedEpoch !== courseMaterialEpoch\) return;/u);
  assert.match(refresh, /const data = await response\.json\([\s\S]*?if \(expectedCourseMaterialEpoch !== courseMaterialEpoch\) return;/u);
  assert.match(source, /materials\.hidden = !\(courseMaterialAccess && courseMaterialsInitialized\)/u);
  assert.doesNotMatch(source.slice(refreshEnd, source.indexOf("const boot =", refreshEnd)), /Promise\.all\(\[setupCourseMaterials/u);
});

test("eligible members request one Maifu item without fetching or opening its PDF", async () => {
  const source = appSource;
  const start = source.indexOf("async function requestCourseMaterial");
  const end = source.indexOf("async function setupCourseMaterials", start);
  assert.ok(start >= 0 && end > start);
  const requester = source.slice(start, end);
  assert.match(requester, /fetch\(`\$\{workerUrl\}\/course\/material-request`/u);
  assert.match(requester, /method: "POST",[\s\S]*?"Content-Type": "application\/json"[\s\S]*?authHeaders\(\)/u);
  assert.doesNotMatch(requester, /\/course\/material\?id=|response\.blob|createObjectURL|window\.open|location\.assign/iu);

  const harness = courseMaterialRequestHarness({
    ok: true,
    status: 202,
    async json() { return { ok: true, deduplicated: false, detail: "申请已提交。" }; },
  });
  await harness.request();
  assert.equal(harness.calls.length, 1);
  assert.equal(harness.calls[0].url, "/api/course/material-request");
  assert.equal(harness.calls[0].init.method, "POST");
  assert.equal(harness.calls[0].init.headers.Authorization, "Bearer member-token");
  assert.deepEqual(JSON.parse(harness.calls[0].init.body), {
    material_id: "maifu-01",
    page_path: "/courses.html",
    honeypot: "",
  });
  assert.equal(harness.button.disabled, true);
  assert.equal(harness.button.textContent, "申请已提交");
  assert.match(harness.statuses.at(-1).state, /ok/u);
  assert.deepEqual(harness.tracked.map((entry) => [entry.type, entry.data.action]), [
    ["course_material_request", "submitted"],
  ]);
});

test("Maifu request exposes deduplicated success and retryable failure states with analytics", async () => {
  const duplicate = courseMaterialRequestHarness({
    ok: true,
    status: 200,
    async json() { return { ok: true, deduplicated: true, detail: "该材料申请已收到。" }; },
  });
  await duplicate.request();
  assert.equal(duplicate.button.disabled, true);
  assert.equal(duplicate.button.textContent, "申请已记录");
  assert.equal(duplicate.tracked.at(-1).data.action, "deduplicated");

  const failed = courseMaterialRequestHarness({
    ok: false,
    status: 502,
    async json() { return { ok: false, detail: "申请已保存，但通知发送失败。" }; },
  });
  await failed.request();
  assert.equal(failed.button.disabled, false);
  assert.equal(failed.button.textContent, "重新索取");
  assert.match(failed.button.ariaLabel, /重新索取/u);
  assert.match(failed.statuses.at(-1).state, /error/u);
  assert.match(failed.statuses.at(-1).message, /通知发送失败/u);
  assert.equal(failed.tracked.at(-1).data.action, "failed");
  assert.equal(failed.tracked.at(-1).data.response_status, 502);
});
