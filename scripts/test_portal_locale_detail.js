#!/usr/bin/env node
"use strict";
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "../portal_suite/locale_assets/locale-detail.js"), "utf8");
const FIELDS = ("title title_cn title_zh display_title institution institution_en institution_cn bank_name industry sector category " +
  "kind_label report_type language description summary author rating filename").split(" ");
const fieldValues = (title = "翻訳されたレポート") => Object.fromEntries(FIELDS.map((key) => [key, ["title", "title_cn", "title_zh", "display_title"].includes(key) ? title : ""]));
const payload = (source = "catalog", id = "ab-report", locale = "ja") => ({
  status: "ready", source, id, locale, source_hash: "a".repeat(64), fields: fieldValues(), cached: false,
});
const response = (status, body) => ({ status, text: async () => JSON.stringify(body) });

function harness({ href = "https://portal.example.invalid/ja/report.html?id=ab-report&password=private&rt=private&title=中文旧标题", replies = [], overlay = null, record = null, fetch = null } = {}) {
  const requests = [];
  const timers = new Map();
  const events = [];
  let now = 0, sequence = 0, overlayReads = 0;
  class Element {
    constructor(tag) { this.tagName = tag; this.attributes = {}; this.children = []; this.text = ""; this.listeners = {}; }
    set textContent(value) { this.text = value; this.children = []; }
    get textContent() { return this.text + this.children.map((node) => node.textContent).join(""); }
    setAttribute(key, value) { this.attributes[key] = value; }
    removeAttribute(key) { delete this.attributes[key]; }
    append(node) { this.children.push(node); }
    addEventListener(name, callback) { this.listeners[name] = callback; }
  }
  const target = new Element("section");
  const chineseLink = { href: "https://portal.example.invalid/report.html?id=ab-report" };
  const window = {
    location: new URL(href),
    PortalLocale: {
      detailTranslation: async () => { overlayReads++; return overlay; },
      readCatalogDetail: async (id, translated) => { assert.equal(id, "ab-report"); assert.ok(translated.title); return record; },
    },
    fetch: async (url, init) => {
      requests.push({ url, init });
      if (fetch) return fetch(url, init);
      return replies.shift() || response(202, { status: "pending", retry_after: 3 });
    },
    setTimeout(callback, delay) {
      const id = ++sequence;
      timers.set(id, { callback, delay });
      if (delay <= 5000) queueMicrotask(() => { if (timers.delete(id)) { now += delay; callback(); } });
      return id;
    },
    clearTimeout(id) { timers.delete(id); },
    dispatchEvent(event) { events.push(event.type); },
  };
  const document = { createElement: (tag) => new Element(tag) };
  const context = { window, document, URL, URLSearchParams, AbortController, Event, Date: { now: () => now } };
  vm.runInNewContext(source, context);
  return { window, target, chineseLink, requests, events, timers, get overlayReads() { return overlayReads; },
    reloadScript() { vm.runInNewContext(source, context); },
    expireRequests() { for (const [id, row] of timers) { if (row.delay > 5000) { timers.delete(id); now += row.delay; row.callback(); } } },
  };
}

async function run() {
  for (const href of ["https://portal.example.invalid/", "https://portal.example.invalid/report.html?id=ab-report", "https://portal.example.invalid/ja/", "https://portal.example.invalid/ja/blog/post.html"]) {
    const h = harness({ href });
    assert.equal(h.window.PortalLocaleDetail, undefined);
    assert.equal(h.requests.length + h.events.length + h.timers.size, 0);
  }
  for (const locale of ["ko", "ja", "ar"]) {
    const body = payload("catalog", "ab-report", locale);
    body.fields.filename = "translated-name.pdf";
    const h = harness({ href: `https://portal.example.invalid/${locale}/report.html?id=ab-report&password=private&rt=private&token=private`, replies: [response(200, body)] });
    const originalFetch = h.window.fetch;
    const item = { id: "ab-report", source: "catalog", title: "中文旧标题", title_cn: "中文旧标题", filename: "original-name.pdf", password: "private", rt: "private" };
    const pending = h.window.PortalLocaleDetail.prepare(item, h.target);
    assert.doesNotMatch(h.target.textContent, /中文旧标题/);
    assert.equal(await pending, true);
    assert.equal(h.requests.length, 1);
    assert.deepEqual(JSON.parse(h.requests[0].init.body), { source: "catalog", id: "ab-report", locale });
    assert.equal(h.requests[0].init.credentials, "omit");
    assert.equal(h.requests[0].url, "/api/locale/report-detail");
    assert.equal(h.window.fetch, originalFetch, "Never patch global fetch or account requests");
    assert.equal(h.target.attributes.dir, locale === "ar" ? "rtl" : "ltr");
    const localized = h.window.PortalLocaleDetail.apply({ ...item, summary: "中文旧正文", available: true });
    assert.equal(localized.title, body.fields.title);
    assert.equal(localized.summary, "");
    assert.equal(localized.available, true);
    assert.equal(localized.password, "private", "Do not change existing download access fields");
    assert.equal(localized.filename, "original-name.pdf", "Translation must not change download filenames");
    assert.equal(await h.window.PortalLocaleDetail.prepare(item, h.target), true);
    assert.equal(h.requests.length, 1, "Repeat rendering reuses the successful translation");
    h.reloadScript();
    assert.deepEqual(h.events, ["kc-locale-detail-ready"]);
  }
  {
    const h = harness({ overlay: { title: "キャッシュ済みタイトル", bank_name: "銀行" }, record: { item: { id: "ab-report", title: "旧中文", filename: "source.pdf", available: true }, related: [] } });
    assert.equal(await h.window.PortalLocaleDetail.prepare({ id: "ab-report" }, h.target), true);
    assert.equal(h.requests.length, 0, "Existing published overlays must cause zero provider API requests");
    const record = await h.window.PortalLocaleDetail.catalogRecord("ab-report");
    assert.equal(record.item.title, "キャッシュ済みタイトル");
    assert.equal(record.item.available, true);
    assert.equal(record.item.filename, "source.pdf", "The overlay fast path preserves download transport metadata");
  }
  {
    const h = harness({ replies: [response(202, { status: "pending", retry_after: 1 }), response(200, payload())] });
    const item = { id: "ab-report", title: "中文不能先显示" };
    assert.deepEqual(await Promise.all([h.window.PortalLocaleDetail.prepare(item, h.target), h.window.PortalLocaleDetail.prepare(item, h.target)]), [true, true]);
    assert.deepEqual(h.requests.map((row) => row.init.method), ["POST", "GET"]);
    const params = new URL(h.requests[1].url, h.window.location).searchParams;
    assert.deepEqual([...params.keys()].sort(), ["id", "locale", "source"]);
    assert.equal(h.overlayReads, 1, "Concurrent detail loads share one in-flight operation");
  }
  {
    let retried = 0;
    const h = harness();
    assert.equal(await h.window.PortalLocaleDetail.prepare({ id: "ab-report" }, h.target, () => { retried++; }), false);
    assert.equal(h.requests.length, 6, "At most one POST and five status polls per user attempt");
    assert.equal(h.requests.filter((row) => row.init.method === "POST").length, 1);
    assert.equal(h.target.attributes["data-kc-locale-translation"], "failed");
    assert.doesNotMatch(h.target.textContent, /中文旧标题|private/);
    h.target.children[0].listeners.click();
    assert.equal(retried, 1);
    assert.equal(h.chineseLink.href, "https://portal.example.invalid/report.html?id=ab-report");
  }
  for (const bad of [
    response(503, { status: "failed", message: "private source" }),
    response(200, { ...payload(), locale: "ko" }),
    response(200, { ...payload(), id: "other" }),
    response(200, { ...payload(), source: "hot" }),
    response(200, { ...payload(), source_hash: "invalid" }),
    response(200, { ...payload(), fields: { title: "翻訳" } }),
    response(200, { ...payload(), fields: { ...fieldValues(), description: "x".repeat(16001) } }),
    { status: 200, text: async () => "not JSON" },
  ]) {
    const h = harness({ replies: [bad] });
    assert.equal(await h.window.PortalLocaleDetail.prepare({ id: "ab-report" }, h.target), false);
    assert.doesNotMatch(h.target.textContent, /private source|中文旧标题/);
    assert.equal(h.requests.length, 1);
  }
  for (const item of [{ id: "other" }, { id: "ab-report", source: "external" }, { id: "../secret", source: "catalog" }, { id: "ab-report", source: "unknown" }]) {
    const h = harness();
    assert.equal(await h.window.PortalLocaleDetail.prepare(item, h.target), false);
    assert.equal(h.requests.length, 0);
  }
  for (const [source, id] of [["external", "123456"], ["hot", "hot:0123456789abcdef"], ["thinktank", "thinktank:report-123"], ["report-a", "report-a:item"], ["authority", "foreign:123"]]) {
    const h = harness({ href: `https://portal.example.invalid/ja/doc.html?id=${id}&source=${source}`, replies: [response(200, payload(source, id))] });
    assert.equal(await h.window.PortalLocaleDetail.prepare({ source, id }, h.target), true, source);
  }
  {
    const h = harness({ fetch: async (_url, init) => new Promise((_resolve, reject) => init.signal.addEventListener("abort", () => reject(new Error("timeout")))) });
    const pending = h.window.PortalLocaleDetail.prepare({ id: "ab-report" }, h.target);
    for (let turn = 0; turn < 20 && !h.requests.length; turn++) await Promise.resolve();
    assert.equal(h.requests.length, 1);
    h.expireRequests();
    assert.equal(await pending, false);
    assert.equal(h.requests.length, 1);
  }
  {
    // Exercise the actual new server handler; storage and the paid provider are
    // in-memory fakes. This catches client/server schema drift without HTTP.
    const serverSource = fs.readFileSync(path.join(__dirname, "../workers/portal-suite-worker/src/locale-report-detail.js"), "utf8");
    const server = await import(`data:text/javascript;base64,${Buffer.from(serverSource).toString("base64")}`);
    assert.deepEqual([...server.LOCALE_DETAIL_FIELDS].sort(), [...FIELDS].sort());
    const objects = new Map();
    let serial = 0, translations = 0;
    const bucket = {
      async get(key) {
        const row = objects.get(key);
        return row ? { etag: row.etag, size: Buffer.byteLength(row.text), text: async () => row.text } : null;
      },
      async put(key, text, { onlyIf }) {
        const prior = objects.get(key);
        if (onlyIf.etagDoesNotMatch === "*" && prior || onlyIf.etagMatches && prior?.etag !== onlyIf.etagMatches) return null;
        const etag = String(++serial); objects.set(key, { etag, text }); return { etag };
      },
    };
    const tasks = [];
    const env = { REPORT_BUCKET: bucket, LOCALE_DETAIL_TRANSLATION_ENABLED: "true", DEEPSEEK_API_KEY: "offline-placeholder" };
    const dependencies = {
      validId: (source, id) => source === "catalog" && id === "ab-report",
      resolve: async () => ({ title: "中文公开标题", summary: "中文公开摘要", filename: "source.pdf", password: "NEVER_SEND" }),
      translate: async (_env, messages) => {
        translations++;
        assert.doesNotMatch(messages[1].content, /NEVER_SEND|filename/);
        return Object.fromEntries(Object.keys(JSON.parse(messages[1].content)).map((key) => [key, "日本語の公開レポート"]));
      },
    };
    const fetch = async (url, init) => {
      if (init.method === "GET") await Promise.all(tasks);
      return server.handleLocaleReportDetail(new Request(new URL(url, "https://portal.example.invalid"), init), env,
        { waitUntil: (task) => tasks.push(task) }, dependencies);
    };
    for (let visit = 0; visit < 2; visit++) {
      const h = harness({ fetch });
      assert.equal(await h.window.PortalLocaleDetail.prepare({ id: "ab-report" }, h.target), true);
      assert.equal(h.window.PortalLocaleDetail.apply({ id: "ab-report", filename: "source.pdf" }).filename, "source.pdf");
    }
    assert.equal(translations, 1, "A fresh page visit reuses the server's successful cache");
  }
  assert.ok(Buffer.byteLength(source) < 32768, "The isolated detail module must remain small");
  console.log("Locale detail on-demand tests passed (offline).");
}
process.exitCode = 1; // An accidentally unresolved test promise must not be green.
run().then(() => { process.exitCode = 0; }).catch((error) => { console.error(error); });
