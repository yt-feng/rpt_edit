import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);
const blogPath = new URL("../site_src/assets/blog.css", import.meta.url);
const chartsPath = new URL("../site_src/assets/charts.css", import.meta.url);
const marker = "/* Automatic device dark mode */";

const [styles, blog, charts] = await Promise.all([
  readFile(stylesPath, "utf8"),
  readFile(blogPath, "utf8"),
  readFile(chartsPath, "utf8"),
]);

function darkSection(source) {
  const start = source.lastIndexOf(marker);
  assert.notEqual(start, -1, "dark-mode marker should exist");
  return source.slice(start);
}

function assertBalanced(source, label) {
  const uncommented = source.replace(/\/\*[\s\S]*?\*\//gu, "");
  let depth = 0;
  for (const character of uncommented) {
    if (character === "{") depth += 1;
    if (character === "}") depth -= 1;
    assert.ok(depth >= 0, `${label} closes a block before it opens`);
  }
  assert.equal(depth, 0, `${label} should have balanced blocks`);
}

function token(section, name) {
  const escaped = name.replace(/[.*+?^${}()|[\]\\]/gu, "\\$&");
  const match = section.match(new RegExp(`${escaped}\\s*:\\s*(#[0-9a-f]{6})`, "iu"));
  assert.ok(match, `missing ${name}`);
  return match[1];
}

function luminance(hex) {
  const channels = [1, 3, 5].map((offset) => Number.parseInt(hex.slice(offset, offset + 2), 16) / 255);
  const linear = channels.map((channel) => (
    channel <= 0.04045 ? channel / 12.92 : ((channel + 0.055) / 1.055) ** 2.4
  ));
  return (0.2126 * linear[0]) + (0.7152 * linear[1]) + (0.0722 * linear[2]);
}

function contrast(left, right) {
  const values = [luminance(left), luminance(right)].sort((a, b) => b - a);
  return (values[0] + 0.05) / (values[1] + 0.05);
}

test("all portal stylesheets opt into automatic device dark mode", () => {
  for (const [label, source] of [["shared", styles], ["blog", blog], ["charts", charts]]) {
    assert.match(source, /@media\s*\(prefers-color-scheme:\s*dark\)/u, `${label} should follow the device preference`);
    assertBalanced(source, label);
  }

  const dark = darkSection(styles);
  assert.match(dark, /:root\s*\{[\s\S]*?color-scheme:\s*dark/u);
  assert.doesNotMatch(dark, /data-theme|theme-toggle/iu, "CSS mode must not depend on a JavaScript toggle");
});

test("shared dark mode covers page, detail, forms, admin, and feature surfaces", () => {
  const dark = darkSection(styles);
  for (const markerText of [
    "body:not(.newsfeed-page)",
    ".detail-field",
    ".text-only-text-content pre",
    ".admin-dialog",
    ".account-admin-table th",
    ".legal-panel",
    ".course-directory",
    ".analytics-day-summary",
    ".chart-search-card",
    ".report-chat-panel",
    ":focus-visible",
    ":disabled",
    "::placeholder",
  ]) {
    assert.ok(dark.includes(markerText), `shared dark mode should cover ${markerText}`);
  }
});

test("Newsfeed retains its dedicated dark visual instead of inheriting portal surfaces", () => {
  assert.match(
    styles,
    /\.newsfeed-page\s*\{\s*color-scheme:\s*dark;\s*background:\s*#050505;\s*color:\s*#f5f7fb;/u,
  );
  const dark = darkSection(styles);
  assert.match(dark, /\.newsfeed-page\s*\{[\s\S]*?--bg:\s*#050505;[\s\S]*?--panel:\s*#101114;/u);
  assert.match(dark, /body:not\(\.newsfeed-page\)/u);
  assert.doesNotMatch(dark, /\.newsfeed-page\s+(?:\.search-panel|\.detail-panel|\.course-directory)/u);
});

test("Blog and Charts define readable dark surfaces and interaction states", () => {
  const blogDark = darkSection(blog);
  const chartsDark = darkSection(charts);

  for (const markerText of [
    ".blog-hero",
    ".blog-market-views",
    ".blog-card",
    ".blog-article-header",
    ".blog-article-content",
    ":focus-visible",
  ]) {
    assert.ok(blogDark.includes(markerText), `Blog dark mode should cover ${markerText}`);
  }

  for (const markerText of [
    ".charts-toolbar",
    ".charts-card",
    ".charts-card-media",
    ".charts-empty",
    ".charts-load-more",
    ":focus-visible",
    ":disabled",
  ]) {
    assert.ok(chartsDark.includes(markerText), `Charts dark mode should cover ${markerText}`);
  }
});

test("core dark tokens keep text and controls above WCAG AA contrast", () => {
  const dark = darkSection(styles);
  const background = token(dark, "--bg");
  const panel = token(dark, "--panel");
  const ink = token(dark, "--ink");
  const muted = token(dark, "--muted");
  const control = token(dark, "--dark-control");
  const accentStrong = token(dark, "--accent-strong");
  const primary = token(dark, "--dark-primary");

  assert.ok(contrast(ink, background) >= 7, "body text should exceed AAA contrast");
  assert.ok(contrast(muted, background) >= 4.5, "muted text should exceed AA contrast");
  assert.ok(contrast(ink, control) >= 7, "form control text should exceed AAA contrast");
  assert.ok(contrast(accentStrong, panel) >= 4.5, "accent links should exceed AA contrast");
  assert.ok(contrast("#ffffff", primary) >= 4.5, "primary buttons should exceed AA contrast");
});
