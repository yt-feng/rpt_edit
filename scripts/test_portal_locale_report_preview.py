"""Real report-template first-paint localization tests, entirely offline."""
from __future__ import annotations

import json
import re
import shutil
import subprocess
import unittest
from pathlib import Path
from urllib.parse import urlencode

from portal_locale_report_preview import localize_report_preview


ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = (ROOT / "portal_suite/site_src/report.html").read_text(encoding="utf-8")
PREVIEW = re.compile(r'(<script id="reportPreviewBootstrap">)(.*?)(</script>)', re.DOTALL)
NODE_HARNESS = r"""
const fs = require('node:fs');
const vm = require('node:vm');
const input = JSON.parse(fs.readFileSync(0, 'utf8'));
class Element {
  constructor(tag) { this.tagName=tag; this.children=[]; this.textContent=''; this.className=''; }
  append(...nodes) { this.children.push(...nodes); }
  replaceChildren(...nodes) { this.children=nodes; }
}
const detail = new Element('section');
const document = {
  title: 'Initial title',
  getElementById: (id) => id === 'detail' && input.hasDetail !== false ? detail : null,
  createElement: (tag) => new Element(tag),
};
const compiled = new vm.Script(input.script);
compiled.runInNewContext({document, window:{location:{search:input.search}}, URLSearchParams, encodeURIComponent});
process.stdout.write(JSON.stringify({title:document.title, detail}));
"""


def run_preview(locale: str, params: dict[str, str], *, has_detail: bool = True) -> dict:
    source = localize_report_preview(TEMPLATE, locale)
    script = PREVIEW.search(source).group(2)
    result = subprocess.run(
        ["node", "-e", NODE_HARNESS],
        input=json.dumps({"script": script, "search": "?" + urlencode(params), "hasDetail": has_detail}),
        text=True, capture_output=True, check=True, timeout=10,
    )
    return json.loads(result.stdout)


def descendants(node: dict) -> list[dict]:
    return [node, *(child for item in node.get("children", []) for child in descendants(item))]


class ReportPreviewLocalizationTests(unittest.TestCase):
    def test_only_named_inline_script_changes_and_repeat_is_idempotent(self):
        unrelated = '<script id="other">const text = "Institution"; const status = "正在确认";</script>'
        misleading = '<script data-id="reportPreviewBootstrap">const status = "正在确认";</script>'
        source = TEMPLATE + unrelated + misleading
        for locale in ("ko", "ja", "ar"):
            with self.subTest(locale=locale):
                translated = localize_report_preview(source, locale)
                self.assertEqual(PREVIEW.sub("PREVIEW", translated), PREVIEW.sub("PREVIEW", source))
                self.assertIn(unrelated, translated)
                self.assertIn(misleading, translated)
                self.assertEqual(localize_report_preview(translated, locale), translated)

    def test_chinese_unknown_locale_and_pages_without_preview_are_unchanged(self):
        for locale in ("zh-Hans", "zh-CN", "en", ""):
            self.assertEqual(localize_report_preview(TEMPLATE, locale), TEMPLATE)
        self.assertEqual(localize_report_preview('<script>"Institution"</script>', "ja"), '<script>"Institution"</script>')

    def test_sanitizer_and_program_parameter_contract_remain_verbatim(self):
        before = PREVIEW.search(TEMPLATE).group(2)
        sanitizer = before[before.index("const legacyWords"):before.index('const title = value("title");')]
        for locale in ("ko", "ja", "ar"):
            after = PREVIEW.search(localize_report_preview(TEMPLATE, locale)).group(2)
            self.assertIn(sanitizer, after)
            self.assertEqual(re.findall(r'value\("([^"]+)"', after), re.findall(r'value\("([^"]+)"', before))
            self.assertIn('searchLink.href = `./?q=${encodeURIComponent(title.slice(0, 200))}`;', after)
            self.assertIn('rawAvailable === "1" || rawAvailable === "true"', after)
            self.assertIn('rawAvailable === "0" || rawAvailable === "false"', after)
            self.assertIn('element.textContent = text;', after)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for real JavaScript execution")
    def test_three_languages_compile_and_render_complete_text_only_first_paint(self):
        words = {
            "ko": ("기관", "산업", "날짜", "텍스트만", "홈에서 같은 제목의 보고서 검색"),
            "ja": ("機関", "業種", "日付", "テキストのみ", "ホームで同じタイトルのレポートを検索"),
            "ar": ("المؤسسة", "القطاع", "التاريخ", "نص فقط", "ابحث عن التقرير بالعنوان نفسه في الصفحة الرئيسية"),
        }
        for locale, expected in words.items():
            with self.subTest(locale=locale):
                result = run_preview(locale, {"id": "ab-report", "title": "Verified title", "bank_code": "MS",
                    "bank_name": "Morgan Stanley", "industry": "Software", "date_folder": "260906", "available": "0"})
                nodes = descendants(result["detail"])
                texts = [node["textContent"] for node in nodes]
                self.assertEqual(result["title"], "Verified title | KC桌面")
                self.assertIn("Verified title", texts)
                self.assertIn("MS · Morgan Stanley", texts)
                self.assertIn("2026-09-06", texts)
                self.assertIn("Software", texts)
                for word in expected:
                    self.assertIn(word, texts)
                self.assertTrue(any("90%" in text for text in texts))
                link = next(node for node in nodes if node["tagName"] == "a")
                self.assertEqual(link["href"], "./?q=Verified%20title")
                visible = " ".join(texts)
                for original in ("正在确认", "下载权限", "Institution", "Industry", "Date", "Text only", "先搜索", "在首页"):
                    self.assertNotIn(original, visible)

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for real JavaScript execution")
    def test_missing_title_or_target_keeps_existing_first_paint_without_throwing(self):
        for locale in ("ko", "ja", "ar"):
            for params, has_detail in (({}, True), ({"title": ""}, True), ({"title": "Report"}, False)):
                with self.subTest(locale=locale, params=params, has_detail=has_detail):
                    result = run_preview(locale, params, has_detail=has_detail)
                    self.assertEqual(result["title"], "Initial title")
                    self.assertEqual(result["detail"]["children"], [])

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for real JavaScript execution")
    def test_available_pending_and_size_branches_keep_their_original_behavior(self):
        for locale, available, pending in (("ko", "이용 가능", "확인 중"), ("ja", "利用可能", "確認中"), ("ar", "متاح", "جارٍ التحقق")):
            for params, expected in (({"available": "1"}, available), ({}, pending),
                                     ({"available": "true", "size_bytes": "2097152"}, "2.0 MB")):
                with self.subTest(locale=locale, params=params):
                    result = run_preview(locale, {"title": "Title", **params})
                    nodes = descendants(result["detail"])
                    self.assertIn(expected, [node["textContent"] for node in nodes])
                    self.assertFalse(any(node["tagName"] == "aside" for node in nodes))

    @unittest.skipUnless(shutil.which("node"), "Node.js is required for real JavaScript execution")
    def test_privacy_sanitizer_and_safe_text_rendering_still_apply(self):
        legacy = "report" + "ify"
        original = "from " + legacy + ": <img src=x onerror=alert(1)> Research"
        for locale in ("ko", "ja", "ar"):
            result = run_preview(locale, {"title": original, "bank_name": legacy + " Research"})
            nodes = descendants(result["detail"])
            heading = next(node for node in nodes if node["tagName"] == "h1")
            self.assertEqual(heading["textContent"], "<img src=x onerror=alert(1)> Research")
            self.assertFalse(any(node["tagName"] == "img" for node in nodes))
            self.assertNotIn(legacy, json.dumps(result).lower())


if __name__ == "__main__":
    unittest.main()
