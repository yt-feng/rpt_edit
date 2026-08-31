import assert from "node:assert/strict";
import { readdir, readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";
import vm from "node:vm";

const siteRoot = fileURLToPath(new URL("../site_src/", import.meta.url));
const textExtensions = new Set([".css", ".html", ".js", ".json", ".svg", ".txt", ".xml"]);
const legacyWords = [
  ["report", "ify"],
  ["nash", "ai"],
  ["macro", "gate"],
  ["support", "contact"],
  ["portal", "suite"],
  ["portal", "alternate"],
  ["portal", "娱乐"],
  ["kc", "desk", "notes"],
  ["two", "tigers"],
];

function publicPhrasePattern(parts) {
  return new RegExp(`\\b${parts.join("[\\s._-]*")}\\b`, "iu");
}

async function publicTextFiles(directory) {
  const rows = await readdir(directory, { withFileTypes: true });
  const files = [];
  for (const row of rows) {
    const target = path.join(directory, row.name);
    if (row.isDirectory()) files.push(...await publicTextFiles(target));
    else if (textExtensions.has(path.extname(row.name).toLowerCase())) files.push(target);
  }
  return files;
}

test("public site templates contain only the KC桌面 identity and in-site request actions", async () => {
  const files = await publicTextFiles(siteRoot);
  const htmlFiles = files.filter((file) => path.extname(file) === ".html");
  assert.ok(htmlFiles.length > 0);
  for (const file of files) {
    const source = await readFile(file, "utf8");
    for (const parts of legacyWords) {
      assert.doesNotMatch(source, publicPhrasePattern(parts), `${path.relative(siteRoot, file)} contains a legacy public phrase`);
    }
    assert.doesNotMatch(source, /contact-card\.(?:jpe?g|png|webp)/iu, `${path.relative(siteRoot, file)} exposes a retired contact card`);
  }
  const html = (await Promise.all(htmlFiles.map((file) => readFile(file, "utf8")))).join("\n");
  assert.match(html, /KC桌面/u);
  assert.doesNotMatch(html, /mailto:/iu);
  assert.match(html, /\?request=(?:membership|support|privacy|refund|access)/u);
  assert.doesNotMatch(html, /(?:微信二维码|Contact\s+WeChat)/iu);
});

test("frontend sanitizes old metadata before caching, rendering, and sharing", async () => {
  const app = await readFile(path.join(siteRoot, "assets", "app.js"), "utf8");
  assert.match(app, /const DOC_ITEM_CACHE_KEY = "portal_doc_item_cache_v2"/u);
  assert.match(app, /function publicBrandText\(/u);
  assert.match(app, /function publicDocItem\(/u);
  assert.match(app, /function publicSearchItem\(/u);
  assert.match(app, /item = publicDocItem\(item\) \|\| \{\};/u);
  assert.match(app, /return publicDocItem\(\{/u);
  assert.match(app, /const label = remoteSourceLabels\[source\] \|\| "此来源"/u);
  assert.match(app, /return "账户";/u);
  assert.match(app, /function isAdminASession\(session = loadAuthSession\(\)\) \{\s*return isSuperSession\(session\);\s*\}/u);
  assert.doesNotMatch(app, /["']admin-a["']/iu);
  assert.doesNotMatch(app, /admin-a@users\.portal\.example\.invalid/iu);
  assert.doesNotMatch(app, /two[\s._-]*tigers/iu);
  assert.match(app, /仅 KC桌面管理员/u);
  assert.match(app, /请先登录 KC桌面管理员账号/u);
  assert.match(app, /newsfeed-avatar">KC</u);
  assert.doesNotMatch(app, /newsfeed-avatar">PS</u);
  assert.match(app, /`\$\{PUBLIC_BRAND\}-activity-history-/u);
  assert.match(app, /`\$\{PUBLIC_BRAND\}-users-/u);
  assert.doesNotMatch(app, /portal-(?:activity-history|users)-/u);
  assert.match(app, /function membershipRequestKind\(/u);
  assert.match(app, /data-membership-request-open="access"/u);
  assert.match(app, /\/membership\/request/u);
  assert.doesNotMatch(app, /contact\.wechat/u);
  assert.doesNotMatch(app, /CONTACT_EMAIL/u);
  assert.doesNotMatch(app, /mailto:/iu);
});

test("both Chinese and non-Chinese browsers receive the same in-site membership entry", async () => {
  const source = await readFile(path.join(siteRoot, "assets", "contact.js"), "utf8");
  const window = { navigator: { languages: ["zh-CN"], language: "zh-CN" } };
  vm.runInNewContext(source, { window });
  for (const languages of [["zh-CN"], ["en-US"]]) {
    const details = window.PortalSuiteContact.detailsForLanguages(languages);
    assert.equal(details.channel, "request");
    assert.equal(details.value, "申请加入会员");
    assert.equal(details.href, "/?request=membership");
  }
});
