#!/usr/bin/env node
"use strict";

const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const source = fs.readFileSync(path.join(__dirname, "../portal_suite/locale_assets/locale-recovery.js"), "utf8");

function harness({ locale = "ja", pathname, query = "", readyState = "complete", detail = true, page = "report", text = "Loading report...", link = "https://portal.example.invalid/report.html", heading = "", failure = false } = {}) {
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
    get hidden() { return this.getAttribute("hidden") !== null; }
    set hidden(value) { if (value) this.attributes.hidden = ""; else delete this.attributes.hidden; }
    setAttribute(name, value) { this.attributes[name] = String(value); }
    getAttribute(name) { return Object.hasOwn(this.attributes, name) ? this.attributes[name] : null; }
    append(child) { child.parentElement = this; this.children.push(child); return child; }
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
    addEventListener(name, callback) { domEvents[name] = callback; },
  };
  const fetch = () => { throw new Error("Recovery must not request the network"); };
  const window = {
    document, location: Object.freeze(new URL(href)), fetch,
    addEventListener(name, callback, capture) { (events[name] ||= []).push({ callback, capture }); },
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
  vm.runInNewContext(source, { window, document, URL }, { filename: "locale-recovery.js" });
  return {
    window, document, body, banner, equivalent, home, errorBox, main, panel, initial, Element, timers, observers, events, fetch,
    get reads() { return reads; },
    boot() { document.readyState = "complete"; if (domEvents.DOMContentLoaded) domEvents.DOMContentLoaded(); },
    emit(name, event = {}) { for (const { callback } of events[name] || []) callback(event); },
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
