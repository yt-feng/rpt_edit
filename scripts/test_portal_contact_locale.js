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
    if (selector === "[data-portal-chinese-only]") return [chineseOnly];
    if (selector === "[data-portal-non-chinese-only]") return [nonChineseOnly];
    return [];
  },
};
const windowStub = {
  navigator: { languages: ["en-US", "zh-CN"], language: "en-US" },
  document: documentStub,
};
const source = fs.readFileSync(
  path.join(__dirname, "..", "portal_suite", "site_src", "assets", "contact.js"),
  "utf8",
);

vm.runInNewContext(source, { window: windowStub });

const contact = windowStub.PortalSuiteContact;
assert.ok(contact, "contact helper should be exported");
assert.equal(contact.languageIsChinese(["zh-CN"]), true);
assert.equal(contact.languageIsChinese(["zh-Hans-CN"]), true);
assert.equal(contact.languageIsChinese(["en-US", "zh-CN"]), false);
assert.deepEqual(
  JSON.parse(JSON.stringify(contact.detailsForLanguages(["en-US", "zh-CN"]))),
  {
    isChinese: false,
    channel: "request",
    value: "申请加入会员",
    label: "站内申请",
    href: "/?request=membership",
  },
);
assert.equal(chineseOnly.hidden, true);
assert.equal(nonChineseOnly.hidden, false);
assert.equal(documentStub.documentElement.dataset.contactChannel, "request");

windowStub.navigator.languages = ["zh-CN", "en-US"];
contact.hydrate(documentStub);
assert.equal(chineseOnly.hidden, false);
assert.equal(nonChineseOnly.hidden, true);
assert.equal(documentStub.documentElement.dataset.contactChannel, "request");
assert.equal(contact.requestHref("support"), "/?request=support");
assert.equal(contact.requestHref("unexpected"), "/?request=membership");

function publicContactHarness(htmlLang, browserLang = "zh-CN", options = {}) {
  class Element {
    constructor(tagName) {
      this.tagName = tagName;
      this.children = [];
      this.attributes = {};
      this.className = "";
      this.ownText = "";
    }
    setAttribute(name, value) { this.attributes[name] = String(value); }
    getAttribute(name) { return this.attributes[name] ?? null; }
    appendChild(child) { this.children.push(child); return child; }
    set textContent(value) { this.children = []; this.ownText = String(value); }
    get textContent() { return this.ownText + this.children.map((child) => child.textContent).join(""); }
    querySelector(selector) {
      for (const child of this.children) {
        const matches = selector === ".legal-footer"
          ? child.className === "legal-footer"
          : selector === "[data-kc-public-account-contact]"
            && Object.prototype.hasOwnProperty.call(child.attributes, "data-kc-public-account-contact");
        if (matches) return child;
        const nested = child.querySelector(selector);
        if (nested) return nested;
      }
      return null;
    }
  }
  const body = new Element("body");
  const footer = new Element("footer");
  footer.className = "legal-footer";
  const support = new Element("a");
  support.href = "/?request=support";
  support.textContent = "Existing support form";
  footer.appendChild(support);
  if (options.footer !== false) body.appendChild(footer);
  if (options.staticContact) {
    const existing = new Element("span");
    existing.setAttribute("data-kc-public-account-contact", "");
    existing.textContent = "Server-rendered contact";
    body.appendChild(existing);
  }
  const listeners = [];
  const document = {
    documentElement: { lang: htmlLang, dataset: {} },
    readyState: options.loading ? "loading" : "complete",
    querySelector: (selector) => body.querySelector(selector),
    querySelectorAll: () => [],
    createElement: (tagName) => new Element(tagName),
    createTextNode: (text) => { const node = new Element("#text"); node.textContent = text; return node; },
    addEventListener: (event, callback) => { if (event === "DOMContentLoaded") listeners.push(callback); },
  };
  const window = {
    document,
    navigator: { languages: [browserLang], language: browserLang },
    fetch() { throw new Error("Public contact must not make requests"); },
  };
  const context = vm.createContext({ window });
  const run = () => vm.runInContext(source, context);
  run();
  return { window, document, footer, support, run, listeners };
}

for (const [locale, label] of [
  ["zh-CN", "开通账号联系"],
  ["ko-KR", "계정 개설 문의"],
  ["ja-JP", "アカウント開設のお問い合わせ"],
  ["ar", "لفتح حساب، تواصل مع"],
]) {
  const harness = publicContactHarness(locale, locale === "zh-CN" ? "ja-JP" : "zh-CN");
  const node = harness.document.querySelector("[data-kc-public-account-contact]");
  assert.ok(node, `${locale} should expose public account contact`);
  assert.equal(node.textContent, `${label} info@kcdesk.com`, "page language wins over browser preference");
  const mail = node.children[1];
  assert.equal(mail.href, "mailto:info@kcdesk.com");
  assert.equal(mail.getAttribute("dir"), "ltr", "the email remains readable in RTL pages");
  harness.window.PortalSuiteContact.hydrate(harness.document);
  harness.run();
  assert.equal(harness.footer.children.length, 2, "repeat hydration/script execution must be idempotent");
  assert.equal(harness.footer.children[0], harness.support, "existing support entry must be retained");
  assert.equal(harness.support.href, "/?request=support");
  assert.equal(harness.window.PortalSuiteContact.requestHref("access"), "/?request=access");
}

const staticContact = publicContactHarness("ja", "zh-CN", { staticContact: true });
assert.equal(staticContact.footer.children.length, 1, "a static locale help strip must prevent duplicate contact");
assert.equal(staticContact.document.querySelector("[data-kc-public-account-contact]").textContent, "Server-rendered contact");
const loading = publicContactHarness("ko", "ar", { loading: true });
assert.equal(loading.document.querySelector("[data-kc-public-account-contact]"), null);
loading.listeners.forEach((listener) => listener());
assert.equal(loading.document.querySelector("[data-kc-public-account-contact]").textContent, "계정 개설 문의 info@kcdesk.com");
assert.equal(publicContactHarness("ar", "ja", { footer: false }).document.querySelector("[data-kc-public-account-contact]"), null);
assert.equal(publicContactHarness("", "ar").document.querySelector("[data-kc-public-account-contact]").textContent, "开通账号联系 info@kcdesk.com");

console.log("Portal Suite contact locale tests passed.");
