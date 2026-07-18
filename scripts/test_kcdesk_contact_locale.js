const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const chineseOnly = { hidden: true };
const nonChineseOnly = { hidden: true };
const documentStub = {
  readyState: "complete",
  documentElement: { dataset: {} },
  querySelectorAll(selector) {
    if (selector === "[data-kc-chinese-only]") return [chineseOnly];
    if (selector === "[data-kc-non-chinese-only]") return [nonChineseOnly];
    return [];
  },
};
const windowStub = {
  navigator: { languages: ["en-US", "zh-CN"], language: "en-US" },
  document: documentStub,
};
const source = fs.readFileSync(
  path.join(__dirname, "..", "kc_desk_notes", "site_src", "assets", "contact.js"),
  "utf8",
);

vm.runInNewContext(source, { window: windowStub });

const contact = windowStub.KCDeskContact;
assert.ok(contact, "contact helper should be exported");
assert.equal(contact.languageIsChinese(["zh-CN"]), true);
assert.equal(contact.languageIsChinese(["zh-Hans-CN"]), true);
assert.equal(contact.languageIsChinese(["en-US", "zh-CN"]), false);
assert.deepEqual(
  JSON.parse(JSON.stringify(contact.detailsForLanguages(["en-US", "zh-CN"]))),
  {
    isChinese: false,
    channel: "email",
    value: "econ.scroll@gmail.com",
    label: "邮箱",
    href: "mailto:econ.scroll@gmail.com",
  },
);
assert.equal(chineseOnly.hidden, true);
assert.equal(nonChineseOnly.hidden, false);
assert.equal(documentStub.documentElement.dataset.contactChannel, "email");

windowStub.navigator.languages = ["zh-CN", "en-US"];
contact.hydrate(documentStub);
assert.equal(chineseOnly.hidden, false);
assert.equal(nonChineseOnly.hidden, true);
assert.equal(documentStub.documentElement.dataset.contactChannel, "wechat");

console.log("KC Desk contact locale tests passed.");
