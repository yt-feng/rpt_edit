#!/usr/bin/env python3
"""Offline contracts for generated locale detail hooks and protected Chinese inputs."""
from __future__ import annotations

import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import unittest

from portal_locale_detail_hooks import (
    defer_unverified_report_preview,
    inject_locale_detail_hooks,
)


ROOT = Path(__file__).resolve().parents[1]
APP_PATH = ROOT / "portal_suite/site_src/assets/app.js"
REPORT_PATH = ROOT / "portal_suite/site_src/report.html"
APP = APP_PATH.read_text(encoding="utf-8")
REPORT = REPORT_PATH.read_text(encoding="utf-8")
LOCALES = ("ko", "ja", "ar")
PREVIEW = re.compile(r'(<script id="reportPreviewBootstrap">)(.*?)(</script>)', re.DOTALL)
NODE = shutil.which("node")


def run_node(program: str, payload: dict) -> dict:
    result = subprocess.run(
        [NODE, "-e", program], input=json.dumps(payload), text=True,
        capture_output=True, timeout=15,
    )
    if result.returncode:
        raise AssertionError(result.stderr or result.stdout)
    return json.loads(result.stdout)


def function_source(source: str, name: str) -> str:
    match = re.search(r"^  (?:async )?function " + re.escape(name) + r"\([^\n]*\) \{\n.*?^  \}", source, re.M | re.S)
    if not match:
        raise AssertionError(f"Cannot extract real application function {name}")
    return match.group(0)


NODE_INLINE = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
let reads = 0;
let writes = 0;
class Element {
  constructor(tag) { this.tagName = tag; this.children = []; this.textContent = ''; }
  append(...children) { this.children.push(...children); writes++; }
  replaceChildren(...children) { this.children = children; writes++; }
}
const detail = new Element('section');
detail.textContent = 'Existing loading status';
const document = {
  title: 'Existing title',
  getElementById(id) { reads++; return id === 'detail' ? detail : null; },
  createElement(tag) { writes++; return new Element(tag); },
};
const window = { location: { pathname: input.pathname, search: '?id=ab1&title=' + encodeURIComponent('未经验证的中文标题') } };
if (input.modulePresent) window.PortalLocaleDetail = { prepare() { throw new Error('Inline bootstrap must not initiate details'); } };
new vm.Script(input.script).runInNewContext({ window, document, URLSearchParams, encodeURIComponent });
process.stdout.write(JSON.stringify({ title: document.title, detail, reads, writes }));
"""


NODE_APP = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
async function main() {
  const calls = [];
  const paints = [];
  const timers = [];
  const events = new Map();
  let release;
  const preparation = new Promise(resolve => { release = resolve; });
  const target = { textContent: '', children: [], setAttribute() {}, append(child) { this.children.push(child.textContent); } };
  const document = {
    _title: 'Existing title',
    get title() { return this._title; },
    set title(value) { paints.push(value); this._title = value; },
    getElementById() { return target; },
    createElement() { return { textContent: '', addEventListener() {} }; },
  };
  const translated = { id: 'ab1', source: input.kind === 'report' ? 'catalog' : 'external', title: input.title };
  const module = {
    prepare(item) { calls.push(['prepare', item.source, item.id]); return input.mode === 'pending' ? preparation : Promise.resolve(true); },
    catalogRecord(id) { calls.push(['catalogRecord', id]); return Promise.resolve(input.mode === 'success' ? { item: translated, related: [] } : null); },
    failed() { calls.push(['failed']); },
    apply(item) { calls.push(['apply', item.title]); return { ...item, title: input.title, title_cn: '', title_zh: '' }; },
  };
  const window = {
    location: { search: '?id=ab1&title=' + encodeURIComponent('未经验证的中文标题') },
    addEventListener(name, fn) { events.set(name, fn); },
    removeEventListener(name, fn) { if (events.get(name) === fn) events.delete(name); },
    setTimeout(fn, delay) { timers.push({ fn, delay, cleared: false }); return timers.length - 1; },
    clearTimeout(index) { if (timers[index]) timers[index].cleared = true; },
  };
  if (!['missing-module', 'module-event'].includes(input.mode)) window.PortalLocaleDetail = module;
  const noop = () => {};
  const context = {
    window, document, URLSearchParams, Promise, Map, PUBLIC_BRAND: 'KC桌面', CONTENT_LOCALE: input.locale, EXTERNAL_SOURCE: 'external',
    loadJson: async path => { calls.push(['loadJson', path]); if (path.includes('catalog')) throw new Error('Full catalog fallback is forbidden'); return {}; },
    loadOptionalJson: async path => { calls.push(['loadOptionalJson', path]); return { items: [] }; },
    loadReportDetailRecord() { throw new Error('Unverified base detail fallback is forbidden'); },
    reportPreviewFromParams() { calls.push(['queryPreview']); return { title: '未经验证的中文标题' }; },
    cachedReportPreview() { calls.push(['cachedPreview']); return { title: '浏览器缓存的中文标题' }; },
    externalItemFromParams() { calls.push(['externalParams']); return { id: 'ab1', source: 'external', title: '未经验证的中文标题' }; },
    validDocId: () => true,
    renderReportFirstPaint: item => paints.push(item.title),
    renderExternalDetailFirstPaint: item => paints.push(item.title),
    titleText: item => item.title,
    trackEvent: noop, analyticsReportPayload: () => ({}), initNewsfeedNav: noop,
    rememberReportPreview: item => calls.push(['cache', item.title]), workerBaseUrl: () => '',
    initAccountGate: noop, initAdminGate: noop, deliveryPasswordFromLocation: () => '',
    renderDetail: item => paints.push(item.title), loadCatalogPdfOverrides: async () => [],
    fetchDocDetailItem: async (url, item) => { calls.push(['workerDetail']); return { ...item, title: '未经验证的中文服务端标题' }; },
    shouldDeferLocalizedHomeCatalog: () => true,
  };
  vm.createContext(context);
  new vm.Script(input.require + '\n' + input.function).runInContext(context);
  const run = context[input.kind === 'report' ? 'initReport' : 'initExternalDetail']();
  await new Promise(resolve => setImmediate(resolve));
  const before = { paints: [...paints], calls: [...calls], title: document.title, pending: target.textContent };
  if (input.mode === 'pending') release(false);
  if (input.mode === 'missing-module') timers[0].fn();
  if (input.mode === 'module-event') {
    window.PortalLocaleDetail = module;
    events.get('kc-locale-detail-ready')();
  }
  const result = await run;
  await new Promise(resolve => setImmediate(resolve));
  process.stdout.write(JSON.stringify({ before, paints, calls, title: document.title, target, result,
    timers: timers.map(({ delay, cleared }) => ({ delay, cleared })), eventCount: events.size }));
}
main().catch(error => { process.stderr.write(String(error.stack)); process.exitCode = 1; });
"""


NODE_RELATED = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
async function main() {
  const remoteCalls = [];
  const rendered = [];
  const catalogCalls = [];
  const section = { hidden: true };
  const status = { textContent: '', className: '' };
  const list = { _html: '', addEventListener() {},
    set innerHTML(value) { this._html = value; rendered.push(value); },
    get innerHTML() { return this._html; } };
  const context = {
    document: { getElementById: id => ({ externalRelatedSection: section, externalRelatedList: list, externalRelatedStatus: status })[id] },
    THINKTANK_SOURCE: 'thinktank', EXTERNAL_SOURCE: 'external', REPORT_A_SOURCE: 'report-a', AUTHORITY_SOURCE: 'authority',
    relatedQueryForDoc: () => 'research',
    catalogRelatedForDoc: (_item, rows) => { catalogCalls.push(rows.map(row => row.id)); return rows.filter(row => row.relevant !== false); },
    docRelatedRow: row => row.title,
    fetchDocRelatedSource: async (workerUrl, endpoint) => { remoteCalls.push([workerUrl, endpoint]); return []; },
    trackEvent() {}, analyticsReportPayload: () => ({}),
  };
  vm.createContext(context);
  new vm.Script(input.function).runInContext(context);
  const initial = [{ id: 'preview', title: 'Translated preview', relevant: !input.fallback }];
  const complete = input.fallback ? [] : [{ id: 'complete', title: 'Translated complete' }];
  const remoteSources = await context.initExternalRelated({ id: 'current' }, 'https://worker.example.invalid', initial, new Map(), Promise.resolve(complete));
  await new Promise(resolve => setImmediate(resolve));
  process.stdout.write(JSON.stringify({ remoteSources, remoteCalls, rendered, catalogCalls, html: list.innerHTML, hidden: section.hidden }));
}
main().catch(error => { process.stderr.write(String(error.stack)); process.exitCode = 1; });
"""


def run_app(locale: str, kind: str, mode: str) -> dict:
    generated = inject_locale_detail_hooks(APP, "app.js", locale)
    function = function_source(generated, "initReport" if kind == "report" else "initExternalDetail")
    if kind == "doc":
        # Execute the real path through both first paint and Worker replacement;
        # downstream access controls are unrelated to the translation gate.
        function = function.split("    const passwordFromLink =", 1)[0] + "    return item;\n  }"
    title = {"ko": "검증된 보고서", "ja": "検証済みレポート", "ar": "تقرير موثق"}[locale]
    return run_node(NODE_APP, {"require": function_source(generated, "requireLocaleDetail"),
        "function": function, "locale": locale, "kind": kind, "mode": mode, "title": title})


class LocaleDetailHookContracts(unittest.TestCase):
    def test_only_supported_locale_app_changes(self):
        for locale in ("zh-Hans", "zh-CN", "zh", "en", "", "ja-JP"):
            with self.subTest(locale=locale):
                self.assertEqual(inject_locale_detail_hooks(APP, "app.js", locale), APP)
                self.assertEqual(defer_unverified_report_preview(REPORT, locale), REPORT)
        for locale in LOCALES:
            for asset in ("contact.js", "site-runtime.js", "locale-runtime.js", "styles.css"):
                with self.subTest(locale=locale, asset=asset):
                    self.assertEqual(inject_locale_detail_hooks(APP, asset, locale), APP)
            changed = inject_locale_detail_hooks(APP, "app.js", locale)
            self.assertNotEqual(changed, APP)
            self.assertEqual(inject_locale_detail_hooks(changed, "app.js", locale), changed)

    def test_small_non_portal_fixtures_remain_unchanged(self):
        for source in ('console.log("fixture");', "", "function sample() { return 1; }"):
            for locale in LOCALES:
                self.assertEqual(inject_locale_detail_hooks(source, "app.js", locale), source)

    def test_real_application_anchors_must_be_unique(self):
        anchors = (
            '  const DOC_ITEM_CACHE_KEY = "portal_doc_item_cache_v2";',
            '  const REPORT_PREVIEW_CACHE_KEY = "portal_report_preview_cache";',
            "  async function initReport() {",
            "  async function initExternalDetail() {",
            "  async function initExternalRelated(item, workerUrl, catalogItems, searchTextById, catalogItemsPromise = null) {",
            "    const detailRecord = await loadReportDetailRecord(id);",
            "    item = await fetchDocDetailItem(workerUrl, item);",
        )
        for anchor in anchors:
            self.assertEqual(APP.count(anchor), 1, anchor)
            for malformed in (APP.replace(anchor, "/* missing anchor */", 1), APP.replace(anchor, anchor + "\n" + anchor, 1)):
                with self.subTest(anchor=anchor, duplicate=malformed.count(anchor) == 2):
                    with self.assertRaises(ValueError):
                        inject_locale_detail_hooks(malformed, "app.js", "ja")

    def test_named_preview_only_changes_and_repeated_transform_is_stable(self):
        other = '<script id="other">window.title = "未经验证的中文标题";</script>'
        misleading = '<script data-id="reportPreviewBootstrap">window.fixture = true;</script>'
        source = REPORT + other + misleading
        for locale in LOCALES:
            changed = defer_unverified_report_preview(source, locale)
            self.assertNotEqual(changed, source)
            self.assertEqual(PREVIEW.sub("PREVIEW", changed), PREVIEW.sub("PREVIEW", source))
            self.assertIn(other, changed)
            self.assertIn(misleading, changed)
            self.assertEqual(defer_unverified_report_preview(changed, locale), changed)
        self.assertEqual(defer_unverified_report_preview(other, "ja"), other)

    def test_ambiguous_named_preview_fails_explicitly(self):
        duplicated = REPORT + PREVIEW.search(REPORT).group(0)
        with self.assertRaises(ValueError):
            defer_unverified_report_preview(duplicated, "ja")

    def test_named_preview_with_missing_or_duplicated_insertion_anchor_fails(self):
        original = PREVIEW.search(REPORT)
        for script in (original.group(2).replace('"use strict";', "", 1),
                       original.group(2).replace('"use strict";', '"use strict";\n"use strict";', 1)):
            malformed = REPORT[:original.start(2)] + script + REPORT[original.end(2):]
            with self.assertRaises(ValueError):
                defer_unverified_report_preview(malformed, "ja")

    def test_cache_namespaces_are_locale_specific(self):
        keys = {"DOC_ITEM_CACHE_KEY": "portal_doc_item_cache_v2", "REPORT_PREVIEW_CACHE_KEY": "portal_report_preview_cache"}
        seen = {name: set() for name in keys}
        for locale in LOCALES:
            generated = inject_locale_detail_hooks(APP, "app.js", locale)
            for name, original in keys.items():
                declaration = re.search(r"const " + name + r' = "([^"]+)";', generated)
                self.assertIsNotNone(declaration)
                value = declaration.group(1)
                self.assertNotEqual(value, original)
                self.assertIn(locale, value)
                seen[name].add(value)
        self.assertTrue(all(len(values) == len(LOCALES) for values in seen.values()))

    def test_transforms_never_write_protected_source_files(self):
        originals = {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in (APP_PATH, REPORT_PATH)}
        for locale in (*LOCALES, "zh-Hans"):
            inject_locale_detail_hooks(APP, "app.js", locale)
            defer_unverified_report_preview(REPORT, locale)
        self.assertEqual(originals, {path: hashlib.sha256(path.read_bytes()).hexdigest() for path in originals})

    @unittest.skipUnless(NODE, "Node.js is required for real generated JavaScript checks")
    def test_all_generated_app_assets_compile_without_execution(self):
        program = "const vm=require('node:vm');const fs=require('node:fs');const v=JSON.parse(fs.readFileSync(0,'utf8'));new vm.Script(v.source);process.stdout.write('{}');"
        for locale in LOCALES:
            with self.subTest(locale=locale):
                run_node(program, {"source": inject_locale_detail_hooks(APP, "app.js", locale)})

    @unittest.skipUnless(NODE, "Node.js is required for inline first-paint execution")
    def test_unverified_inline_query_title_never_paints_even_without_module(self):
        for locale in LOCALES:
            changed = defer_unverified_report_preview(REPORT, locale)
            script = PREVIEW.search(changed).group(2)
            for module_present in (False, True):
                with self.subTest(locale=locale, module_present=module_present):
                    result = run_node(NODE_INLINE, {"script": script, "pathname": f"/{locale}/report.html", "modulePresent": module_present})
                    self.assertEqual(result["title"], "Existing title")
                    self.assertEqual(result["detail"]["children"], [])
                    self.assertEqual(result["detail"]["textContent"], "Existing loading status")
                    self.assertEqual(result["writes"], 0)
                    self.assertNotIn("未经验证的中文标题", json.dumps(result, ensure_ascii=False))

    @unittest.skipUnless(NODE, "Node.js is required for Chinese preview behavior checks")
    def test_chinese_inline_query_preview_behavior_is_preserved(self):
        changed = defer_unverified_report_preview(REPORT, "zh-Hans")
        result = run_node(NODE_INLINE, {"script": PREVIEW.search(changed).group(2), "pathname": "/report.html"})
        self.assertIn("未经验证的中文标题", result["title"])
        self.assertGreater(result["writes"], 0)

    @unittest.skipUnless(NODE, "Node.js is required for asynchronous detail gate checks")
    def test_report_and_doc_do_not_first_paint_while_prepare_is_pending(self):
        for locale in LOCALES:
            for kind in ("report", "doc"):
                with self.subTest(locale=locale, kind=kind):
                    result = run_app(locale, kind, "pending")
                    self.assertEqual(result["before"]["paints"], [])
                    self.assertEqual(result["before"]["title"], "Existing title")
                    self.assertEqual(result["paints"], [])
                    self.assertTrue(any(call[0] == "prepare" for call in result["calls"]))
                    self.assertFalse(any(call[0] in ("queryPreview", "cachedPreview", "catalogRecord", "workerDetail", "apply") for call in result["calls"]))

    @unittest.skipUnless(NODE, "Node.js is required for asynchronous module readiness checks")
    def test_missing_detail_module_waits_then_fails_without_unverified_paint(self):
        for locale in LOCALES:
            for kind in ("report", "doc"):
                with self.subTest(locale=locale, kind=kind):
                    result = run_app(locale, kind, "missing-module")
                    self.assertEqual(result["before"]["paints"], [])
                    self.assertEqual(result["paints"], [])
                    self.assertEqual(result["timers"], [{"delay": 8000, "cleared": True}])
                    self.assertEqual(result["eventCount"], 0)
                    self.assertEqual(len(result["target"]["children"]), 1, "A failed module should provide the retry button")
                    self.assertNotEqual(result["before"]["pending"], result["target"]["textContent"])

    @unittest.skipUnless(NODE, "Node.js is required for verified catalog-record checks")
    def test_missing_verified_report_record_returns_without_full_catalog_fallback(self):
        for locale in LOCALES:
            result = run_app(locale, "report", "missing-record")
            self.assertIn(["prepare", "catalog", "ab1"], result["calls"])
            self.assertIn(["catalogRecord", "ab1"], result["calls"])
            self.assertIn(["failed"], result["calls"])
            self.assertEqual(result["paints"], [])
            self.assertNotIn(["loadJson", "data/catalog.json"], result["calls"])
            self.assertFalse(any(call[0] in ("queryPreview", "cachedPreview") for call in result["calls"]))

    @unittest.skipUnless(NODE, "Node.js is required for verified report first-paint checks")
    def test_report_renders_and_caches_only_the_current_verified_record(self):
        for locale in LOCALES:
            result = run_app(locale, "report", "success")
            self.assertIn(["catalogRecord", "ab1"], result["calls"])
            cached = next(call[1] for call in result["calls"] if call[0] == "cache")
            self.assertGreater(len(result["paints"]), 0)
            self.assertTrue(all(cached in title for title in result["paints"]))
            self.assertNotIn("未经验证", json.dumps(result["paints"], ensure_ascii=False))
            self.assertNotIn(["failed"], result["calls"])

    @unittest.skipUnless(NODE, "Node.js is required for external detail overlay-order checks")
    def test_doc_applies_verified_fields_before_first_paint_and_after_worker_detail(self):
        for locale in LOCALES:
            result = run_app(locale, "doc", "success")
            title = result["result"]["title"]
            self.assertEqual(result["paints"], [title])
            self.assertEqual(result["result"]["title_cn"], "")
            self.assertEqual(result["result"]["title_zh"], "")
            self.assertEqual([call[0] for call in result["calls"] if call[0] in ("prepare", "apply", "workerDetail")],
                             ["prepare", "apply", "workerDetail", "apply"])
            self.assertNotIn("未经验证", title)

    @unittest.skipUnless(NODE, "Node.js is required for deferred-module readiness checks")
    def test_module_ready_event_releases_wait_before_timeout(self):
        result = run_app("ja", "report", "module-event")
        self.assertEqual(result["before"]["paints"], [])
        self.assertIn(["prepare", "catalog", "ab1"], result["calls"])
        self.assertIn(["catalogRecord", "ab1"], result["calls"])
        self.assertEqual(result["timers"], [{"delay": 8000, "cleared": True}])
        self.assertEqual(result["eventCount"], 0)

    def test_related_hook_changes_only_local_worker_parameter_and_preserves_catalog_logic(self):
        original = function_source(APP, "initExternalRelated")
        for locale in LOCALES:
            generated = function_source(inject_locale_detail_hooks(APP, "app.js", locale), "initExternalRelated")
            restored, count = re.subn(r'\n    workerUrl = "";[^\n]*', "", generated, count=1)
            self.assertEqual(count, 1)
            self.assertEqual(restored, original, "All ranking, fallback and deferred catalog logic must remain intact")
        self.assertEqual(function_source(inject_locale_detail_hooks(APP, "app.js", "zh-Hans"), "initExternalRelated"), original)

    @unittest.skipUnless(NODE, "Node.js is required for recommendation-source execution")
    def test_locale_recommendations_keep_catalog_and_disable_all_remote_sources(self):
        for locale in (*LOCALES, "zh-Hans"):
            function = function_source(inject_locale_detail_hooks(APP, "app.js", locale), "initExternalRelated")
            # Observe the real local source selection after the original function
            # has executed; fetchDocRelatedSource itself is a network-free mock.
            function = function[:-1] + "    return remoteSources;\n  }"
            for fallback in (False, True):
                with self.subTest(locale=locale, fallback=fallback):
                    result = run_node(NODE_RELATED, {"function": function, "fallback": fallback})
                    expected_remotes = 4 if locale == "zh-Hans" else 0
                    self.assertEqual(len(result["remoteSources"]), expected_remotes)
                    self.assertEqual(len(result["remoteCalls"]), expected_remotes)
                    self.assertIn("Translated preview", result["rendered"])
                    self.assertEqual(result["html"], "Translated preview" if fallback else "Translated complete")
                    self.assertEqual(result["catalogCalls"], [["preview"], [] if fallback else ["complete"]])
                    self.assertEqual(result["hidden"], False)


if __name__ == "__main__":
    unittest.main()
