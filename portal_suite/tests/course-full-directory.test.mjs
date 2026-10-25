import assert from "node:assert/strict";
import test from "node:test";
import {
  COURSE_FULL_DIRECTORY_KEY,
  loadCourseFullDirectory,
  validateCourseFullDirectory,
} from "../../workers/portal-suite-worker/src/course-full-directory.js";

const row = () => ({ id: "original-01", name: "Provider 原始文件 <案例>.pdf", folders: ["Provider 原始目录"], extension: "pdf", size_label: "1 MB", date: "2026-10-25" });
const catalog = () => ({ schema_version: 1, variant: "original_names", complete: true, item_count: 1, generated_at: "2026-10-25T00:00:00Z", items: [row()] });

test("original catalog requires complete exact metadata and refuses locators or malformed identities", () => {
  assert.equal(validateCourseFullDirectory(catalog()).items[0].name, row().name);
  for (const change of [
    { complete: false }, { item_count: 2 }, { item_count: true }, { variant: "sanitized" }, { generated_at: "yesterday" },
    { download_url: "https://private.example/download" },
    { items: [{ ...row(), object_key: "private/material.pdf" }] },
    { items: [{ ...row(), id: "../private/key" }] },
    { items: [{ ...row(), name: "folder/file.pdf" }] },
    { items: [{ ...row(), folders: ["label\nheader"] }] },
    { items: [{ ...row(), folders: Array(33).fill("folder") }] },
    { items: [{ ...row(), name: "x".repeat(501) }] },
    { items: [{ ...row(), extension: "PDF" }] },
    { item_count: 2, items: [row(), row()] },
  ]) assert.throws(() => validateCourseFullDirectory({ ...catalog(), ...change }));
  assert.equal(validateCourseFullDirectory({ ...catalog(), items: [{ ...row(), name: "😀".repeat(500), folders: Array(32).fill("资料") }] }).items.length, 1);
});

test("storage size is bounded before parsing, missing source has no fallback, and failed loads are retryable", async () => {
  let textReads = 0;
  const oversized = { async get(key) {
    assert.equal(key, COURSE_FULL_DIRECTORY_KEY);
    return { size: 32 * 1024 * 1024 + 1, async text() { textReads += 1; return "{}"; } };
  } };
  await assert.rejects(loadCourseFullDirectory(oversized));
  assert.equal(textReads, 0);
  let available = false;
  const source = { async get(key) {
    assert.equal(key, COURSE_FULL_DIRECTORY_KEY);
    return available ? { text: async () => JSON.stringify(catalog()) } : null;
  } };
  await assert.rejects(loadCourseFullDirectory(source));
  available = true;
  assert.equal((await loadCourseFullDirectory(source)).items.length, 1);
});
