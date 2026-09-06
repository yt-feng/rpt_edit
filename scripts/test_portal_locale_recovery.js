#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "../portal_suite/locale_assets/locale-recovery.js"), "utf8");
const builder = fs.readFileSync(path.join(__dirname, "build_portal_locales.py"), "utf8");
const earlySource = /LOCALE_RECOVERY_EARLY_BOOTSTRAP = r"""([\s\S]*?)"""/.exec(builder)[1];
const reportTemplate = fs.readFileSync(path.join(__dirname, "../portal_suite/site_src/report.html"), "utf8");
const previewSource = /<script id="reportPreviewBootstrap">([\s\S]*?)<\/script>/.exec(reportTemplate)[1];
const appSource = fs.readFileSync(path.join(__dirname, "../portal_suite/site_src/assets/app.js"), "utf8");
const deliveryPasswordSource = /function deliveryPasswordFromLocation\(params\) \{[\s\S]*?\n  \}/.exec(appSource)[0];

function harness({ locale = "ja", pathname, query = "", readyState = "complete", detail = true, page = "report", text = "Loading report...", link = "https://portal.example.invalid/report.html", heading = "", failure = false, preview = false, beforeRecovery = null } = {}) {
  const events = {};
  const domEvents = {};
  const timers = [];
  const observers = [];
  let reads = 0;
  class Element {
    constructor(tag = "div", attributes = {}, content = "") {
      this.tagName = tag.toUpperCase();
      this.attributes = { ...attributes };
      this.children = [];
      this.parentElement = null;
      this.ownText = content;
      this.style = { display: "block", visibility: "visible" };
    }
    get textContent() { return this.ownText + this.children.map((child) => child.textContent).join(""); }
    set textContent(value) { this.ownText = String(value); this.children = []; }
    get className() { return this.getAttribute("class") || ""; }
    set className(value) { this.setAttribute("class", value); }
    get hidden() { return this.getAttribute("hidden") !== null; }
    set hidden(value) { if (value) this.attributes.hidden = ""; else delete this.attributes.hidden; }
    setAttribute(name, value) { this.attributes[name] = String(value); }
    getAttribute(name) { return Object.hasOwn(this.attributes, name) ? this.attributes[name] : null; }
    append(...children) { for (const child of children) { child.parentElement = this; this.children.push(child); } return children[0]; }
    replaceChildren(...children) { this.children = []; this.ownText = ""; this.append(...children); }
    matches(selectors) {
      return selectors.split(",").some((selector) => {
        selector = selector.trim();
        if (selector[0] === "#") return this.getAttribute("id") === selector.slice(1);
        if (selector[0] === ".") return (this.getAttribute("class") || "").split(/\s+/).includes(selector.slice(1));
        const parsed = /^(\w+)?(?:\[([^=\]]+)(?:="([^"]*)")?\])?$/.exec(selector);
        return !!parsed && (!parsed[1] || this.tagName === parsed[1].toUpperCase()) &&
          (!parsed[2] || this.getAttribute(parsed[2]) !== null && (parsed[3] === undefined || this.getAttribute(parsed[2]) === parsed[3]));
      });
    }
    closest(selector) { return this.matches(selector) ? this : this.parentElement && this.parentElement.closest(selector); }
    querySelectorAll(selector) {
      const result = [];
      const visit = (node) => { for (const child of node.children) { if (child.matches(selector)) result.push(child); visit(child); } };
      visit(this);
      return result;
    }
    querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  }
  const body = new Element("body", { "data-page": page });
  const banner = body.append(new Element("aside", { "data-kc-locale-help": "" }));
  const equivalent = banner.append(new Element("a", { "data-kc-chinese-entry": "", "data-kc-chinese-equivalent": "", href: link, hreflang: "zh-Hans" }, "中文对应页"));
  const home = banner.append(new Element("a", { "data-kc-chinese-entry": "", href: "https://portal.example.invalid/" }, "中文首页"));
  const errorBox = banner.append(new Element("p", { "data-kc-locale-error": "", hidden: "" }));
  const main = body.append(new Element("main"));
  const panel = detail ? main.append(new Element("section", { id: "detail" })) : main;
  const initial = panel.append(new Element("p", { class: "subtle", role: "status" }, text));
  if (heading) panel.append(new Element("h1", { class: "detail-title" }, heading));
  if (failure) panel.append(new Element("div", { class: "error-state" }, "404: Report not found."));
  const href = `https://portal.example.invalid${pathname === undefined ? `/${locale}/report.html` : pathname}${query}`;
  const document = {
    readyState, body,
    querySelector(selector) { reads++; return body.querySelector(selector); },
    querySelectorAll(selector) { reads++; return body.querySelectorAll(selector); },
    getElementById(id) { return body.querySelector(`#${id}`); },
    createElement(tag) { return new Element(tag); },
    addEventListener(name, callback) { domEvents[name] = callback; },
  };
  const fetch = () => { throw new Error("Recovery must not request the network"); };
  const window = {
    document, location: Object.freeze(new URL(href)), fetch,
    addEventListener(name, callback, capture) { (events[name] ||= []).push({ callback, capture }); },
    removeEventListener(name, callback, capture) {
      events[name] = (events[name] || []).filter((row) => row.callback !== callback || !!row.capture !== !!capture);
    },
    setTimeout(callback, delay) { timers.push({ callback, delay, cleared: false }); return timers.length - 1; },
    clearTimeout(id) { timers[id].cleared = true; },
    setInterval() { throw new Error("Recovery must not poll"); },
    getComputedStyle(node) { return node.style; },
    MutationObserver: class {
      constructor(callback) { this.callback = callback; this.targets = []; this.active = true; observers.push(this); }
      observe(target, options) { this.targets.push({ target, options }); }
      disconnect() { this.active = false; }
    },
  };
  const context = { window, document, URL, URLSearchParams, encodeURIComponent };
  const emit = (name, event = {}) => { for (const { callback } of events[name] || []) callback(event); };
  const early = () => vm.runInNewContext(earlySource, context, { filename: "locale-early-inline.js" });
  early();
  if (preview) vm.runInNewContext(previewSource, context, { filename: "real-report-preview.js" });
  if (beforeRecovery) beforeRecovery({ window, document, panel, Element, events, emit, early });
  vm.runInNewContext(source, context, { filename: "locale-recovery.js" });
  return {
    window, document, body, banner, equivalent, home, errorBox, main, panel, initial, Element, timers, observers, events, fetch,
    get reads() { return reads; },
    boot() { document.readyState = "complete"; if (domEvents.DOMContentLoaded) domEvents.DOMContentLoaded(); },
    emit,
    mutate() { for (const observer of observers) if (observer.active) observer.callback([]); },
    timeout() { for (const timer of timers) if (!timer.cleared) { timer.cleared = true; timer.callback(); } },
  };
}

for (const locale of ["ko", "ja", "ar"]) {
  const h = harness({ locale, failure: true });
  assert.equal(h.window.PortalLocaleRecovery.locale, locale);
  assert.equal(h.window.PortalLocaleRecovery.reason, "error-state");
  assert.equal(h.banner.getAttribute("data-kc-locale-status"), "error");
  assert.equal(h.errorBox.hidden, false);
  assert.equal(h.errorBox.getAttribute("lang"), locale);
  assert.equal(h.errorBox.getAttribute("dir"), locale === "ar" ? "rtl" : "ltr");
  assert.match(h.errorBox.textContent, locale === "ko" ? /중국어/ : locale === "ja" ? /中国語/ : /الصينية/);
  assert.match(h.panel.textContent, /404: Report not found/);
}

for (const pathname of ["/", "/report.html", "/reports/ja-example.html", "/japan/", "/en/report.html"]) {
  const h = harness({ pathname, failure: true });
  assert.equal(h.window.PortalLocaleRecovery, undefined);
  assert.equal(h.reads, 0, "Non-locale pages must not inspect the DOM");
  assert.equal(h.timers.length + h.observers.length + Object.keys(h.events).length, 0);
  assert.equal(h.errorBox.hidden, true);
}

{
  const h = harness({ query: "?id=report%2F42&q=AI+%26+chips&source=authority&title=Test&start_date=2026-09-01&lang=ja&next=https%3A%2F%2Fevil.invalid&token=secret#summary" });
  const target = new URL(h.equivalent.getAttribute("href"));
  assert.equal(target.origin + target.pathname, "https://portal.example.invalid/report.html");
  assert.equal(target.searchParams.get("id"), "report/42");
  assert.equal(target.searchParams.get("q"), "AI & chips");
  assert.equal(target.searchParams.get("source"), "authority");
  assert.equal(target.searchParams.get("start_date"), "2026-09-01");
  assert.equal(target.searchParams.get("title"), "Test");
  for (const key of ["lang", "next", "token"]) assert.equal(target.searchParams.has(key), false);
  assert.equal(h.home.getAttribute("href"), "https://portal.example.invalid/", "The direct Chinese homepage must remain unchanged");
  assert.equal(h.window.fetch, h.fetch, "Do not wrap fetch");
}

for (const link of ["https://evil.invalid/report.html", "https://portal.example.invalid.evil.invalid/report.html", "http://portal.example.invalid/report.html", "https://name:password@portal.example.invalid/report.html", "javascript:alert(1)", "https://portal.example.invalid/ja/report.html", "http://["]) {
  const h = harness({ query: "?id=private-id&q=test", link });
  assert.equal(h.equivalent.getAttribute("href"), link, "Untrusted targets must receive no query data");
}

for (const locale of ["ko", "ja", "ar"]) {
  for (const filename of ["report.html", "doc.html", "delivery.html"]) {
    for (const query of [
      "?id=example&password=fixture%2Bvalue&token=omit&rt=omit#password=ignored",
      "?id=example#password=fixture%2Bvalue&token=omit",
      "?id=example&password=#?password=fixture%2Bvalue&rt=omit",
    ]) {
      const h = harness({ locale, pathname: `/${locale}/${filename}`, query, link: `https://portal.example.invalid/${filename}` });
      const target = new URL(h.equivalent.getAttribute("href"));
      const readPassword = vm.runInNewContext(`(${deliveryPasswordSource})`, { window: { location: target }, URLSearchParams });
      const password = readPassword();
      assert.equal(password, "fixture+value", `${locale}/${filename}: the existing access password must survive`);
      assert.equal(target.searchParams.get("id"), "example");
      assert.equal(target.searchParams.has("token") || target.searchParams.has("rt"), false);
      assert.doesNotMatch(target.hash, /token|rt=|ignored/);
      assert.equal(h.home.getAttribute("href"), "https://portal.example.invalid/");
      assert.equal(Object.keys(h.window).some((key) => /password|token/i.test(key)), false);
    }
  }
}

for (const [pathname, destination] of [
  ["/ja/report.html", "/delivery.html"], ["/ja/doc.html", "/report.html"],
  ["/ja/delivery.html", "/doc.html"], ["/ja/report.html", "/"],
  ["/ja/other.html", "/other.html"], ["/ja/nested/report.html", "/report.html"],
  ["/ja/report.html/extra", "/report.html"], ["/ja/report.html", "/nested/report.html"],
  ["/ja/report.html", "https://evil.invalid/report.html"],
  ["/ja/report.html", "http://portal.example.invalid/report.html"],
  ["/ja/report.html", "https://name:fixture@portal.example.invalid/report.html"],
]) {
  const link = destination.startsWith("/") ? `https://portal.example.invalid${destination}` : destination;
  const h = harness({ pathname, link, query: "?id=example&password=fixture&token=omit&rt=omit#password=fixture" });
  const target = new URL(h.equivalent.getAttribute("href"));
  assert.equal(target.searchParams.has("password"), false, `${pathname} -> ${destination}`);
  assert.equal(target.hash, "", `${pathname} -> ${destination}`);
}

for (const [eventName, tag, reason] of [
  ["error", "script", "script-error"], ["error", null, "runtime-error"],
  ["unhandledrejection", null, "unhandled-rejection"],
]) {
  let firstPaint;
  let takeEarly;
  const h = harness({ preview: true, query: "?id=example&title=Actual%20preview%20title", beforeRecovery(context) {
    firstPaint = context.panel.textContent;
    assert.equal(context.panel.querySelector("h1").textContent, "Actual preview title");
    takeEarly = context.window.PortalLocaleEarly;
    context.early();
    assert.equal(context.events.error.length, 1, "Duplicate inline bootstrap must not add listeners");
    const event = { target: tag ? new context.Element(tag) : context.window };
    for (const key of ["message", "filename", "error", "reason"]) {
      Object.defineProperty(event, key, { get() { throw new Error("Never read private event details"); } });
    }
    context.emit(eventName, event);
    // Keep only the first fixed kind, without growing a queue of event objects.
    for (let i = 0; i < 20; i++) context.emit("error", { target: context.window });
  } });
  assert.equal(h.window.PortalLocaleRecovery.reason, reason);
  assert.equal(h.errorBox.hidden, false, "A real preview title must not conceal an earlier application failure");
  assert.equal(h.panel.textContent, firstPaint, "The preview remains readable during recovery");
  assert.equal(h.window.PortalLocaleEarly, undefined);
  assert.equal(h.events.error.length, 1, "Only the permanent error listener remains");
  assert.equal(h.events.unhandledrejection.length, 1);
  assert.equal(takeEarly(), "", "The consumed buffer must no longer retain its error kind");
  h.timeout();
  assert.equal(h.window.PortalLocaleRecovery.reason, reason);
}

{
  const h = harness({ preview: true, query: "?id=example&title=Successful%20preview", beforeRecovery({ emit, Element }) {
    emit("error", { target: new Element("img") });
  } });
  h.timeout();
  assert.equal(h.window.PortalLocaleRecovery.status, "ready");
  assert.equal(h.errorBox.hidden, true, "An optional image failure before recovery is still ignored");
  assert.equal(h.window.PortalLocaleEarly, undefined);
}

for (const [event, target, reason] of [["error", "script", "script-error"], ["error", "window", "runtime-error"], ["unhandledrejection", null, "unhandled-rejection"]]) {
  const h = harness({ heading: "Successful report" });
  const before = h.panel.textContent;
  h.emit(event, { target: target === "window" ? h.window : target && new h.Element(target) });
  assert.equal(h.window.PortalLocaleRecovery.reason, reason);
  assert.equal(h.errorBox.hidden, false);
  assert.equal(h.panel.textContent, before, "Failures must not replace successful report content");
  assert.equal(h.events.error[0].capture, true, "Resource errors require capture");
}

{
  const h = harness({ heading: "Successful report" });
  h.emit("error", { target: new h.Element("img") });
  assert.equal(h.errorBox.hidden, true, "An optional image failure is not a script failure");
  h.timeout();
  assert.equal(h.window.PortalLocaleRecovery.status, "ready");
}

for (const text of ["Loading report...", "正在打开报告…", "レポートを読み込み中…", "보고서를 불러오는 중…", "جارٍ تحميل التقرير…", ""]) {
  const h = harness({ text });
  assert.equal(h.timers.length, 1);
  assert.equal(h.timers[0].delay, 9000);
  assert.equal(h.errorBox.hidden, true);
  h.timeout();
  assert.equal(h.window.PortalLocaleRecovery.reason, "loading-timeout", text);
  assert.equal(h.observers[0].active, false);
}

for (const heading of ["Successful report", "Loading AI Models: A Research Report", "Opening New Markets"]) {
  const h = harness({ heading });
  h.panel.setAttribute("aria-busy", "true");
  h.timeout();
  assert.equal(h.errorBox.hidden, true, "A completed title must override stale loading UI");
  assert.equal(h.window.PortalLocaleRecovery.check(), "ready");
}

{
  const h = harness();
  h.panel.textContent = "";
  h.panel.append(new h.Element("h1", {}, "Now successfully loaded"));
  h.mutate();
  h.timeout();
  assert.equal(h.errorBox.hidden, true);
  assert.equal(h.observers.length, 1);
  assert.equal(h.observers[0].targets[0].target, h.panel);
  assert.notEqual(h.observers[0].targets[0].target, h.body);
  const error = h.panel.append(new h.Element("div", { class: "error-state", hidden: "" }, "Not found"));
  h.mutate();
  assert.equal(h.errorBox.hidden, true, "Hidden errors must not be reported");
  error.hidden = false;
  error.style.display = "none";
  h.mutate();
  assert.equal(h.errorBox.hidden, true);
  error.style.display = "block";
  h.mutate();
  assert.equal(h.window.PortalLocaleRecovery.reason, "error-state");
}

{
  const h = harness({ readyState: "loading", query: "?id=early" });
  h.emit("error", { target: new h.Element("script") });
  assert.equal(h.errorBox.hidden, true);
  h.boot();
  assert.equal(h.errorBox.hidden, false, "Retain errors received before DOMContentLoaded");
  assert.equal(h.window.PortalLocaleRecovery.reason, "script-error");
  assert.equal(new URL(h.equivalent.getAttribute("href")).searchParams.get("id"), "early");
}

{
  const h = harness({ detail: false, page: "404", text: "Page not found" });
  assert.equal(h.window.PortalLocaleRecovery.reason, "error-state");
}

{
  const h = harness({ detail: false, text: "Static article" });
  assert.equal(h.timers.length, 0, "Static content does not need a loading deadline");
  assert.equal(h.observers[0].targets[0].target, h.main);
  h.main.append(new h.Element("div", { class: "error-state" }, "404"));
  h.mutate();
  assert.equal(h.window.PortalLocaleRecovery.reason, "error-state");
}

console.log("Locale recovery regression tests passed.");
