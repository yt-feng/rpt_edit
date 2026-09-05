#!/usr/bin/env python3
"""Offline regression tests for the static localized static-release builder."""

from __future__ import annotations

import concurrent.futures
from datetime import date
import gzip
import hashlib
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest import mock
import xml.etree.ElementTree as ET


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import build_portal_locales as builder  # noqa: E402


SITE_URL = "https://portal.example.invalid"
FAKE_PREFIX = {
    "ko": "한국어 번역",
    "ja": "日本語の翻訳",
    "ar": "ترجمة عربية",
}
FAKE_COPY = {
    "ko": "검증된 금융 연구 문안입니다",
    "ja": "検証済みの金融リサーチ文です",
    "ar": "هذا نص بحث مالي مترجم وموثوق",
}
XHTML_NAMESPACE = "http://www.w3.org/1999/xhtml"


def body_bytes(path: Path) -> bytes:
    payload = path.read_bytes()
    start = payload.lower().find(b"<body")
    if start < 0:
        raise AssertionError(f"Fixture has no body: {path}")
    return payload[start:]


def alternate_links(source: str) -> dict[str, str]:
    return dict(re.findall(
        r'<link\b(?=[^>]*\brel="alternate")(?=[^>]*\bhreflang="([^"]+)")'
        r'(?=[^>]*\bhref="([^"]+)")[^>]*>',
        source,
        flags=re.I,
    ))


def first_json_ld(source: str) -> dict:
    match = re.search(
        r'<script\b[^>]*type="application/ld\+json"[^>]*>(.*?)</script>',
        source,
        flags=re.I | re.S,
    )
    if not match:
        raise AssertionError("Localized page has no JSON-LD")
    return json.loads(match.group(1))


class RecordingTranslator:
    def __init__(self) -> None:
        self.calls: list[tuple[str, tuple[str, ...]]] = []
        self.sources: set[str] = set()

    def __call__(
        self,
        locale: str,
        units: list[builder.TranslationUnit],
    ) -> dict[str, str]:
        self.calls.append((locale, tuple(unit.key for unit in units)))
        self.sources.update(unit.source for unit in units)
        prefix = FAKE_PREFIX[locale]
        return {
            unit.key: " ".join(
                part for part in (
                    prefix,
                    FAKE_COPY[locale],
                    " ".join(builder.PLACEHOLDER_RE.findall(unit.source)),
                ) if part
            )
            for unit in units
        }


class PortalLocaleBuildTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temporary = tempfile.TemporaryDirectory()
        self.temporary_root = Path(self.temporary.name)
        self.site = self.temporary_root / "site"
        self.assets = self.temporary_root / "locale-assets"
        self.cache = self.temporary_root / "translation-cache-v1.json.gz"
        self.hot_report_index = self.temporary_root / "hot-reports-public-v2.json"
        self._write_fixture()

    def tearDown(self) -> None:
        self.temporary.cleanup()

    def _write_fixture(self) -> None:
        (self.site / "assets").mkdir(parents=True)
        (self.site / "data").mkdir(parents=True)
        (self.site / "reports" / "topics" / "ai").mkdir(parents=True)
        self.assets.mkdir(parents=True)

        (self.site / "index.html").write_text(
            """<!doctype html>
<html lang="zh-Hans">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="index,follow">
    <meta name="description" content="检索全球金融研究报告。">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:site_name" content="KC桌面">
    <meta property="og:url" content="https://portal.example.invalid/">
    <link rel="canonical" href="https://portal.example.invalid/">
    <link rel="alternate" hreflang="zh-Hans" href="https://portal.example.invalid/">
    <link rel="alternate" hreflang="x-default" href="https://portal.example.invalid/">
    <title>中文金融研究报告检索</title>
    <script type="application/ld+json">{"@context":"https://schema.org","@type":"WebSite","name":"KC桌面金融研究","url":"https://portal.example.invalid/","inLanguage":"zh-Hans","potentialAction":{"@type":"SearchAction","target":"https://portal.example.invalid/?q={search_term_string}"}}</script>
  </head>
  <body><main><h1>中文金融研究报告检索</h1><p>KC桌面提供 100% 来源明确的报告。</p><p><span>From</span><span>To</span><span>Rows</span><span>PDF</span></p><select><option value="fulltext">Document text (large index)</option></select><a href="/reports/topics/ai/">人工智能专题研究</a></main><script src="/assets/app.js"></script><script src="/assets/charts.js?v=old"></script><script src="/assets/contact.js?mode=public&v=old"></script><script src="/assets/report-chat.js"></script><script src="/assets/report-research-export.js"></script><script src="/assets/site-runtime.js"></script><script src="/assets/xlsx-export.js"></script></body>
</html>
""",
            encoding="utf-8",
        )
        (self.site / "reports" / "topics" / "ai" / "index.html").write_text(
            """<!doctype html>
<html lang="zh-Hans">
  <head>
    <meta charset="utf-8">
    <meta name="robots" content="index,follow">
    <meta name="description" content="人工智能与半导体研究报告。">
    <meta property="og:locale" content="zh_CN">
    <meta property="og:url" content="https://portal.example.invalid/reports/topics/ai/">
    <link rel="canonical" href="https://portal.example.invalid/reports/topics/ai/">
    <title>人工智能专题研究</title>
    <script type="application/ld+json">{"@context":"https://schema.org","@graph":[{"@type":"WebPage","name":"人工智能专题研究","url":"https://portal.example.invalid/reports/topics/ai/","inLanguage":"zh-Hans"},{"@type":"Report","name":"人工智能行业研究报告","headline":"人工智能行业研究报告","alternateName":"Artificial Intelligence Sector Research Report","genre":"金融研究报告","conditionsOfAccess":"会员可用","url":"https://portal.example.invalid/reports/topics/ai/","inLanguage":["zh-Hans","en"]}]}</script>
  </head>
  <body><nav><a href="/">返回首页</a></nav><main><h1>人工智能专题研究</h1><p>这里汇总人工智能行业研究报告。</p></main><script src="https://portal.example.invalid/assets/app.js?v=abcdef12"></script></body>
</html>
""",
            encoding="utf-8",
        )
        (self.site / "baidu_verify_codeva-FzG1Vh5prB.html").write_text(
            "0123456789abcdef0123456789abcdef\n",
            encoding="utf-8",
        )
        (self.site / "google0123456789abcdef.html").write_text(
            "google-site-verification: google0123456789abcdef.html\n",
            encoding="utf-8",
        )
        (self.site / "assets" / "app.js").write_text(
            """(() => {
  "use strict";
  const label = "搜索报告";
  const endpoint = "/api/report-chat";
  const reportRoute = "report.html?";
  const statusClass = "status-line error";
  const translationPending = "翻译正在更新，请稍后再试。";
  const cancelNode = document.getElementById("Cancel");
  const languageNames = ["English", "中文", "日本語", "한국어", "العربية"];
  globalThis.PORTAL_LOCALE_TEST = { label, endpoint, reportRoute, statusClass, translationPending, cancelNode, languageNames };
})();
""",
            encoding="utf-8",
        )
        for asset_name in builder.LOCALIZED_JS_ASSETS:
            if asset_name == "app.js":
                continue
            (self.site / "assets" / asset_name).write_text(
                f'globalThis.KC_LOCALE_ASSET = "{asset_name}";\n',
                encoding="utf-8",
            )
        (self.site / "assets" / "styles.css").write_text(
            '''body { color: #123; }
.course-material-card.is-cover-missing .course-material-cover::after { content: "封面暂不可用"; }
.decorative::before { content: " ·"; }
@media (max-width: 820px) {
  #accountAdminUsersSection .account-admin-table td:nth-child(1)::before { content: "用户名"; }
}
''',
            encoding="utf-8",
        )
        (self.assets / "locale.css").write_text(
            'html[dir="rtl"] body { direction: rtl; }\n',
            encoding="utf-8",
        )
        (self.assets / "locale-runtime.js").write_text(
            'globalThis.KC_LOCALE_RUNTIME = true;\n',
            encoding="utf-8",
        )

        catalog = {
            "schema_version": 1,
            "updated_at_bjt": "2026-09-04 10:00:00 +0800",
            "item_count": 1,
            "items": [{
                "id": "report-ai-1",
                "title": "人工智能行业研究报告",
                "bank_name": "高盛全球研究",
                "industry": "科技与半导体行业",
                "date_folder": "2026-09-04",
                "available": True,
            }],
        }
        (self.site / "data" / "catalog.json").write_text(
            json.dumps(catalog, ensure_ascii=False),
            encoding="utf-8",
        )
        preview_catalog = {
            **catalog,
            "total_item_count": catalog["item_count"],
        }
        recommendation_catalog = {
            **catalog,
            "items": [
                {
                    key: value
                    for key, value in catalog["items"][0].items()
                    if key in {"id", "title", "bank_name", "industry", "sector", "category", "date_folder", "available"}
                }
            ],
        }
        (self.site / "data" / "catalog_preview.json").write_text(
            json.dumps(preview_catalog, ensure_ascii=False),
            encoding="utf-8",
        )
        (self.site / "data" / "catalog_recommendations.json").write_text(
            json.dumps(recommendation_catalog, ensure_ascii=False),
            encoding="utf-8",
        )
        detail_dir = self.site / "data" / "report_details"
        detail_dir.mkdir()
        (detail_dir / "re.json").write_text(
            json.dumps({
                "schema_version": 1,
                "reports": {
                    "report-ai-1": {
                        "item": catalog["items"][0],
                        "related": [],
                    },
                },
            }, ensure_ascii=False),
            encoding="utf-8",
        )
        chart_index = {
            "schema_version": 1,
            "updated_at_bjt": "2026-09-04 10:00:00 +0800",
            "report_count": 1,
            "item_count": 1,
            "reports": [{
                "report_ref": "0123456789abcdef01234567",
                "report_id": "report-ai-1",
                "title": "人工智能行业研究报告",
                "date_folder": "260904",
                "search_text": "PRIVATE FULL TEXT MUST NEVER LEAVE",
                "charts": [{
                    "id": "chart-ai-1",
                    "analysis_version": "chart-search-v2",
                    "image_id": "a" * 64,
                    "ordinal": 1,
                    "title": "人工智能资本开支趋势",
                    "content_kind": "chart",
                    "chart_type": "line",
                    "description": "图表展示人工智能资本开支持续增长。",
                    "trend_summary": "整体趋势稳步上升。",
                    "metrics": ["资本开支"],
                    "entities": ["人工智能企业"],
                    "periods": ["未来三年"],
                    "geographies": ["全球市场"],
                    "units": ["十亿美元"],
                    "keywords": ["投资周期"],
                }],
            }],
        }
        (self.site / "data" / "chart_search_index.json").write_text(
            json.dumps(chart_index, ensure_ascii=False),
            encoding="utf-8",
        )
        self.hot_report_index.write_text(json.dumps({
            "version": 2,
            "generation": "0123456789abcdef",
            "updated_at": "2026-09-04T10:00:00.000Z",
            "items": [{
                "id": "hot:0123456789abcdef",
                "source": "hot",
                "title": "人工智能热门报告",
                "title_cn": "人工智能热门报告中文标题",
                "institution": "公开研究机构",
                "date": "2026-09-04",
                "description": "公开展示的热门报告简介。",
                "filename": "PRIVATE-FILENAME-MUST-NOT-LEAVE.pdf",
                "size_bytes": 12345,
                "sort_order": 1,
                "created_at": "2026-09-04T10:00:00.000Z",
                "updated_at": "2026-09-04T10:00:00.000Z",
                "required_plan": "3个月会员",
                "required_months": 3,
                "object_key": "PRIVATE-OBJECT-KEY-MUST-NOT-LEAVE",
                "extracted_text": "PRIVATE-HOT-REPORT-TEXT-MUST-NOT-LEAVE",
            }],
        }, ensure_ascii=False), encoding="utf-8")
        courses = {
            "schema_version": 1,
            "items": [{
                "id": "course-ai-1",
                "title": "人工智能行业研究课程",
                "topic": "投资研究方法",
                "summary": "学习如何分析人工智能公司和产业链。",
                "cover": "/assets/course-ai.webp",
            }],
        }
        (self.site / "data" / "course-materials.json").write_text(
            json.dumps(courses, ensure_ascii=False),
            encoding="utf-8",
        )

        (self.site / "sitemap.xml").write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <sitemap><loc>https://portal.example.invalid/sitemap-pages.xml</loc><lastmod>2026-09-04</lastmod></sitemap>
</sitemapindex>
""",
            encoding="utf-8",
        )
        (self.site / "sitemap-pages.xml").write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url><loc>https://portal.example.invalid/</loc><lastmod>2026-09-04</lastmod></url>
  <url><loc>https://portal.example.invalid/reports/topics/ai/</loc><lastmod>2026-09-03</lastmod></url>
</urlset>
""",
            encoding="utf-8",
        )
        (self.site / "robots.txt").write_text(
            "User-agent: *\nAllow: /\nSitemap: https://portal.example.invalid/sitemap.xml\n",
            encoding="utf-8",
        )
        (self.site / "feed.xml").write_text(
            """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <title>KC桌面最新研究报告</title>
  <link>https://portal.example.invalid/</link>
  <description>最新金融研究报告索引。</description>
  <language>zh-Hans</language>
  <item><title>人工智能行业研究报告</title><link>https://portal.example.invalid/reports/topics/ai/</link><guid>https://portal.example.invalid/reports/topics/ai/</guid><description>人工智能行业报告摘要。</description><category>科技研究</category></item>
</channel></rss>
""",
            encoding="utf-8",
        )
        (self.site / "llms.txt").write_text(
            "# KC桌面研究索引\n- 首页：https://portal.example.invalid/\n- 人工智能专题：https://portal.example.invalid/reports/topics/ai/\n",
            encoding="utf-8",
        )
        (self.site / "llms-full.txt").write_text(
            "# KC桌面完整研究索引\n- 报告：https://portal.example.invalid/reports/topics/ai/\n",
            encoding="utf-8",
        )

    def _build(
        self,
        translator: object,
        *,
        cache_in: Path | None = None,
        workers: int = 4,
        index_start_date: str | None = None,
        index_allowlist: tuple[str, ...] = (),
        **options: object,
    ) -> dict:
        return builder.build_localized_release(
            root=self.site,
            site_url=SITE_URL,
            cache_in=cache_in,
            cache_out=self.cache,
            assets_root=self.assets,
            workers=workers,
            model=builder.DEFAULT_DEEPSEEK_MODEL,
            deepseek_base_url="https://api.deepseek.com",
            timeout=1,
            attempts=1,
            hot_report_index_path=self.hot_report_index,
            index_start_date=index_start_date,
            index_allowlist=index_allowlist,
            batch_translator=translator,
            **options,
        )

    @mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "offline-test-key"}, clear=True)
    def test_budget_checkpoint_does_not_render_or_mutate_protected_chinese(self) -> None:
        before = {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()}
        diagnostics = self.temporary_root / "budget-checkpoint.json"
        provider = mock.Mock(side_effect=AssertionError("Insufficient estimate budget must stop before HTTP"))
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
            result = self._build(None, workers=1, checkpoint_on_budget=True,
                                 max_provider_cost_cny="0.000001", diagnostics_out=diagnostics)
        self.assertEqual(result["status"], "checkpointed")
        self.assertFalse(result["ready"])
        self.assertEqual(before, {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()})
        self.assertTrue(self.cache.is_file())
        self.assertFalse((self.site / "ko").exists())
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["stop_category"], "budget")
        self.assertEqual(report["build_error"], report["stop_reason"])
        self.assertEqual(report["provider_requests"], 0)
        provider.assert_not_called()

    def test_checkpoint_flag_does_not_hide_real_translation_or_source_errors(self) -> None:
        diagnostics = self.temporary_root / "real-error.json"
        translator = mock.Mock(side_effect=builder.TranslationError("missing required link placeholder"))
        with self.assertRaisesRegex(builder.TranslationError, "missing required link placeholder"):
            self._build(translator, checkpoint_on_budget=True, diagnostics_out=diagnostics)
        self.assertEqual(json.loads(diagnostics.read_text())["status"], "failed")
        self.assertFalse((self.site / "ko").exists())

    def test_bounded_repair_checkpoint_cannot_be_mistaken_for_a_release(self) -> None:
        diagnostics = self.temporary_root / "repair-checkpoint.json"
        before = {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()}

        def stop_at_repair_limit(**kwargs: object) -> None:
            run_state = kwargs["run_state"]
            run_state.stop("Bounded repair deadline reached", category="repair_limit")
            raise builder.TranslationStopped(run_state.stop_reason)

        with mock.patch.object(builder, "_build_localized_release", side_effect=stop_at_repair_limit):
            result = self._build(None, checkpoint_on_budget=True, diagnostics_out=diagnostics)
        self.assertEqual(result["status"], "checkpointed")
        self.assertFalse(result["ready"])
        self.assertEqual(before, {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()})
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["stop_category"], "repair_limit")
        self.assertFalse(report["ready"])

    def test_hot_report_source_fails_closed_and_uses_only_public_display_fields(self) -> None:
        self.hot_report_index.unlink()
        with self.assertRaisesRegex(builder.TranslationError, "Hot Reports public index"):
            self._build(RecordingTranslator())

        self.hot_report_index.write_text(json.dumps({
            "version": 2,
            "generation": "not-a-generation",
            "items": [],
        }), encoding="utf-8")
        with self.assertRaisesRegex(builder.TranslationError, "invalid generation"):
            self._build(RecordingTranslator())

        self.hot_report_index.write_text(json.dumps({
            "version": 2,
            "generation": "0123456789abcdef",
            "updated_at": "PRIVATE-OBJECT-KEY-MUST-NOT-REACH-OVERLAY",
            "items": [],
        }), encoding="utf-8")
        with self.assertRaisesRegex(builder.TranslationError, "invalid updated_at"):
            self._build(RecordingTranslator())

        self.hot_report_index.write_text(json.dumps({
            "version": 2,
            "generation": "0123456789abcdef",
            "updated_at": "2026-99-99T25:61:61.000Z",
            "items": [],
        }), encoding="utf-8")
        with self.assertRaisesRegex(builder.TranslationError, "invalid updated_at"):
            self._build(RecordingTranslator())

        self.hot_report_index.write_text(json.dumps({
            "version": "2",
            "generation": "0123456789abcdef",
            "items": [],
        }), encoding="utf-8")
        with self.assertRaisesRegex(builder.TranslationError, "unsupported schema"):
            self._build(RecordingTranslator())

    def test_site_verification_filename_cannot_exempt_arbitrary_html(self) -> None:
        path = self.site / "baidu_verify_codeva-FzG1Vh5prB.html"
        path.write_text("<html><head></head><body>fake</body></html>", encoding="utf-8")
        with self.assertRaisesRegex(builder.TranslationError, "token is invalid"):
            self._build(RecordingTranslator())

    def test_google_verification_must_match_its_filename(self) -> None:
        path = self.site / "google0123456789abcdef.html"
        for invalid in (
            "google-site-verification: googleffffffffffffffff.html\n",
            "<html><head></head><body>fake</body></html>",
        ):
            with self.subTest(invalid=invalid):
                path.write_text(invalid, encoding="utf-8")
                translator = RecordingTranslator()
                with self.assertRaisesRegex(builder.TranslationError, "token is invalid"):
                    self._build(translator)
                self.assertFalse(translator.calls)

    def test_real_builder_output_passes_chinese_parity_with_deferred_history(self) -> None:
        import verify_portal_chinese_parity as parity

        topic = self.site / "reports/topics/ai/index.html"
        old = self.site / "blog/old.html"
        old.parent.mkdir()
        old.write_text(topic.read_text(encoding="utf-8").replace(
            "/reports/topics/ai/", "/blog/old.html"
        ), encoding="utf-8")
        for page in (topic, old):
            source = page.read_text(encoding="utf-8")
            canonical = builder.extract_canonical(source)
            links = "".join(
                f'<link rel="alternate" hreflang="{language}" href="{canonical}">'
                for language in ("zh-Hans", "x-default")
            )
            page.write_text(source.replace("</head>", links + "</head>"), encoding="utf-8")
        for name in ("sitemap-baidu.xml", "sitemap-sogou.xml"):
            (self.site / name).write_bytes((self.site / "sitemap-pages.xml").read_bytes())
        snapshot_path = self.temporary_root / "chinese-before.json"
        snapshot_path.write_text(json.dumps(parity.create_snapshot(
            root=self.site, site_origin=SITE_URL,
        )), encoding="utf-8")
        self._build(RecordingTranslator(), index_start_date="2026-09-05")
        report = parity.verify_snapshot(root=self.site, snapshot_path=snapshot_path)
        self.assertEqual(report["counts"]["html"], 3)
        self.assertEqual(report["counts"]["hreflang_clusters"], 2)

    def test_builds_complete_locale_routes_and_preserves_chinese_bodies(self) -> None:
        chinese_pages = [
            self.site / "index.html",
            self.site / "reports" / "topics" / "ai" / "index.html",
        ]
        bodies_before = {path: body_bytes(path) for path in chinese_pages}
        catalog_snapshots = {
            name: (self.site / "data" / name).read_bytes()
            for name in (
                "catalog.json", "catalog_preview.json", "catalog_recommendations.json",
                "chart_search_index.json",
            )
        }
        chinese_css_before = (self.site / "assets" / "styles.css").read_bytes()
        verification_before = (self.site / "baidu_verify_codeva-FzG1Vh5prB.html").read_bytes()
        google_before = (self.site / "google0123456789abcdef.html").read_bytes()
        translator = RecordingTranslator()

        manifest = self._build(translator)

        self.assertTrue(translator.calls)
        self.assertNotIn("PRIVATE FULL TEXT MUST NEVER LEAVE", translator.sources)
        self.assertNotIn("PRIVATE-FILENAME-MUST-NOT-LEAVE.pdf", translator.sources)
        self.assertNotIn("PRIVATE-OBJECT-KEY-MUST-NOT-LEAVE", translator.sources)
        self.assertNotIn("PRIVATE-HOT-REPORT-TEXT-MUST-NOT-LEAVE", translator.sources)
        self.assertNotIn("0123456789abcdef0123456789abcdef", translator.sources)
        self.assertNotIn("google-site-verification: google0123456789abcdef.html", translator.sources)
        self.assertGreater(manifest["source_unit_count"], 0)
        self.assertEqual(manifest["quality_gate_version"], builder.QUALITY_GATE_VERSION)
        cache_text = gzip.decompress(self.cache.read_bytes()).decode("utf-8")
        for private_marker in (
            "PRIVATE FULL TEXT MUST NEVER LEAVE",
            "PRIVATE-FILENAME-MUST-NOT-LEAVE.pdf",
            "PRIVATE-OBJECT-KEY-MUST-NOT-LEAVE",
            "PRIVATE-HOT-REPORT-TEXT-MUST-NOT-LEAVE",
        ):
            self.assertNotIn(private_marker, cache_text)
        cache_payload = json.loads(cache_text)
        for locale in builder.LOCALES:
            self.assertEqual(len(cache_payload["locales"][locale]), manifest["source_unit_count"])
        self.assertEqual(manifest["html_page_count"], 2)
        self.assertEqual(manifest["indexable_page_count"], 2)
        self.assertEqual(manifest["catalog_item_count"], 1)
        for path, expected in bodies_before.items():
            self.assertEqual(body_bytes(path), expected, path)
        for name, expected in catalog_snapshots.items():
            self.assertEqual((self.site / "data" / name).read_bytes(), expected)
        self.assertEqual((self.site / "assets" / "styles.css").read_bytes(), chinese_css_before)
        self.assertEqual(
            (self.site / "baidu_verify_codeva-FzG1Vh5prB.html").read_bytes(),
            verification_before,
        )
        self.assertEqual((self.site / "google0123456789abcdef.html").read_bytes(), google_before)
        self.assertEqual(set(alternate_links((self.site / "index.html").read_text(encoding="utf-8"))), {
            "zh-Hans", "ko", "ja", "ar", "x-default",
        })
        root_home = (self.site / "index.html").read_text(encoding="utf-8")
        self.assertIn('<meta property="og:site_name" content="KC桌面">', root_home)
        self.assertRegex(root_home, r"<script data-kc-locale-bootstrap>.*locale-runtime\.js\?v=[0-9a-f]{12}")
        self.assertIn('n.language||n.languages&&n.languages[0]', root_home)
        self.assertIn('l==="zh"||/^zh-(?:cn|sg|hans)(?:-|$)/.test(l)', root_home)
        self.assertNotRegex(root_home, r'<script defer src="/assets/locale-runtime\.js')
        self.assertNotRegex(root_home, r'<link rel="stylesheet" href="/assets/locale\.css')

        directions = {"ko": "ltr", "ja": "ltr", "ar": "rtl"}
        og_locales = {"ko": "ko_KR", "ja": "ja_JP", "ar": "ar_AE"}
        for locale, direction in directions.items():
            self.assertFalse((self.site / locale / "baidu_verify_codeva-FzG1Vh5prB.html").exists())
            self.assertFalse((self.site / locale / "google0123456789abcdef.html").exists())
            home = (self.site / locale / "index.html").read_text(encoding="utf-8")
            deep = (self.site / locale / "reports" / "topics" / "ai" / "index.html").read_text(encoding="utf-8")
            self.assertRegex(home, rf'<html\b[^>]*\blang="{locale}"[^>]*\bdir="{direction}"')
            self.assertRegex(deep, rf'<html\b[^>]*\blang="{locale}"[^>]*\bdir="{direction}"')
            self.assertIn(f'<meta property="og:locale" content="{og_locales[locale]}">', home)
            self.assertIn(
                '<meta property="og:site_name" content="' + "".join(("KC", "Desk")) + '">',
                home,
            )
            self.assertNotIn('<meta property="og:site_name" content="KC桌面">', home)
            self.assertIn(f'<meta property="og:url" content="{SITE_URL}/{locale}/">', home)
            self.assertIn(
                f'<meta property="og:url" content="{SITE_URL}/{locale}/reports/topics/ai/">',
                deep,
            )
            self.assertEqual(builder.extract_canonical(home), f"{SITE_URL}/{locale}/")
            self.assertEqual(builder.extract_canonical(deep), f"{SITE_URL}/{locale}/reports/topics/ai/")
            home_schema = first_json_ld(home)
            self.assertEqual(
                home_schema["potentialAction"]["target"],
                f"{SITE_URL}/{locale}/?q={{search_term_string}}",
            )
            self.assertEqual(alternate_links(home), {
                "zh-Hans": f"{SITE_URL}/",
                "ko": f"{SITE_URL}/ko/",
                "ja": f"{SITE_URL}/ja/",
                "ar": f"{SITE_URL}/ar/",
                "x-default": f"{SITE_URL}/",
            })
            expected_alternates = {
                "zh-Hans": f"{SITE_URL}/reports/topics/ai/",
                "ko": f"{SITE_URL}/ko/reports/topics/ai/",
                "ja": f"{SITE_URL}/ja/reports/topics/ai/",
                "ar": f"{SITE_URL}/ar/reports/topics/ai/",
                "x-default": f"{SITE_URL}/reports/topics/ai/",
            }
            self.assertEqual(alternate_links(deep), expected_alternates)
            self.assertIn(f'href="/{locale}/reports/topics/ai/"', home)
            self.assertRegex(home, rf'src="/{locale}/assets/app\.js\?v=[0-9a-f]{{12}}"')
            locale_runtime = re.search(
                r'<script src="/assets/locale-runtime\.js\?v=[0-9a-f]{12}"></script>',
                home,
            )
            self.assertIsNotNone(locale_runtime)
            self.assertLess(locale_runtime.start(), home.index(f'src="/{locale}/assets/app.js?v='))
            self.assertRegex(
                deep,
                rf'src="https://portal\.example\.invalid/{locale}/assets/app\.js\?v=[0-9a-f]{{12}}"',
            )
            schema = first_json_ld(deep)
            graph = schema["@graph"]
            page_schema = next(node for node in graph if node["@type"] == "WebPage")
            report_schema = next(node for node in graph if node["@type"] == "Report")
            self.assertEqual(page_schema["inLanguage"], locale)
            self.assertEqual(page_schema["url"], f"{SITE_URL}/{locale}/reports/topics/ai/")
            self.assertTrue(page_schema["name"].startswith(FAKE_PREFIX[locale]))
            self.assertEqual(report_schema["inLanguage"], ["zh-Hans", "en"])
            self.assertEqual(
                report_schema["alternateName"],
                "Artificial Intelligence Sector Research Report",
            )
            self.assertTrue(report_schema["name"].startswith(FAKE_PREFIX[locale]))
            self.assertTrue(report_schema["genre"].startswith(FAKE_PREFIX[locale]))
            self.assertTrue(report_schema["conditionsOfAccess"].startswith(FAKE_PREFIX[locale]))
            self.assertEqual(report_schema["url"], f"{SITE_URL}/{locale}/reports/topics/ai/")

            localized_app = self.site / locale / "assets" / "app.js"
            localized_javascript = localized_app.read_text(encoding="utf-8")
            localized_app_digest = hashlib.sha256(localized_app.read_bytes()).hexdigest()[:12]
            self.assertIn(f'src="/{locale}/assets/app.js?v={localized_app_digest}"', home)
            self.assertIn(
                f'src="https://portal.example.invalid/{locale}/assets/app.js?v={localized_app_digest}"',
                deep,
            )
            for asset_name in builder.LOCALIZED_JS_ASSETS:
                localized_asset = self.site / locale / "assets" / asset_name
                localized_digest = hashlib.sha256(localized_asset.read_bytes()).hexdigest()[:12]
                self.assertRegex(
                    home,
                    rf'src="/{locale}/assets/{re.escape(asset_name)}\?[^"#]*v={localized_digest}(?:&[^"#]*)?"',
                    f"{locale}/{asset_name} must use its own translated-byte digest",
                )
            self.assertIn(FAKE_PREFIX[locale], localized_javascript)
            self.assertIn('"use strict"', localized_javascript)
            self.assertIn('"report.html?"', localized_javascript)
            self.assertIn('"status-line error"', localized_javascript)
            self.assertIn(FAKE_PREFIX[locale], localized_javascript)
            self.assertIn('getElementById("Cancel")', localized_javascript)
            for language_name in ("English", "中文", "日本語", "한국어", "العربية"):
                self.assertIn(f'"{language_name}"', localized_javascript)
            for label in ("From", "To", "Rows"):
                self.assertNotIn(f">{label}<", home)
            # Acronyms stay stable unless explicitly modeled as translatable UI.
            self.assertIn(">PDF<", home)
            self.assertIn(FAKE_PREFIX[locale], home)
            self.assertNotIn("中文金融研究报告检索", home)
            self.assertNotIn(">Document text (large index)<", home)
            if shutil.which("node"):
                checked = subprocess.run(
                    ["node", "--check", str(localized_app)],
                    check=False,
                    capture_output=True,
                    text=True,
                )
                self.assertEqual(checked.returncode, 0, checked.stderr)

            overlay_names = {
                "full": "catalog-titles.json",
                "preview": "catalog-preview.json",
            }
            overlay_sizes: dict[str, int] = {}
            for kind, filename in overlay_names.items():
                overlay_path = self.site / "data" / "i18n" / locale / filename
                overlay = json.loads(overlay_path.read_text(encoding="utf-8"))
                self.assertEqual(overlay["locale"], locale)
                self.assertEqual(overlay["kind"], kind)
                self.assertEqual(overlay["item_count"], 1)
                self.assertEqual(overlay["schema_version"], 2)
                self.assertEqual(overlay["fields"], list(builder.CATALOG_TRANSLATABLE_FIELDS))
                field_values = dict(zip(overlay["fields"], overlay["rows"][0][1:]))
                self.assertEqual(overlay["rows"][0][0], "report-ai-1")
                self.assertTrue(field_values["title"].startswith(FAKE_PREFIX[locale]))
                self.assertTrue(field_values["bank_name"].startswith(FAKE_PREFIX[locale]))
                metadata = manifest["catalog_overlays"][locale][kind]
                self.assertEqual(metadata["path"], f"data/i18n/{locale}/{filename}")
                self.assertEqual(metadata["item_count"], 1)
                self.assertEqual(metadata["byte_size"], overlay_path.stat().st_size)
                self.assertRegex(metadata["sha256"], r"^[0-9a-f]{64}$")
                self.assertIn(metadata["path"], manifest["required_paths"])
                overlay_sizes[kind] = metadata["byte_size"]
            self.assertNotIn("recommendations", manifest["catalog_overlays"][locale])
            detail_path = self.site / "data" / "i18n" / locale / "catalog-detail-re.json"
            detail_overlay = json.loads(detail_path.read_text(encoding="utf-8"))
            self.assertEqual(detail_overlay["kind"], "detail:re")
            self.assertEqual(detail_overlay["item_count"], 1)
            self.assertTrue(detail_overlay["rows"][0][1].startswith(FAKE_PREFIX[locale]))
            detail_metadata = manifest["catalog_detail_overlays"][locale]["re"]
            self.assertEqual(detail_metadata["path"], f"data/i18n/{locale}/catalog-detail-re.json")
            self.assertEqual(detail_metadata["byte_size"], detail_path.stat().st_size)
            self.assertIn(detail_metadata["path"], manifest["required_paths"])
            full_overlay = json.loads(
                (self.site / "data" / "i18n" / locale / "catalog-titles.json").read_text(encoding="utf-8")
            )
            legacy_overlay = {
                "schema_version": 1,
                "locale": locale,
                "kind": "full",
                "item_count": full_overlay["item_count"],
                "titles": {row[0]: row[1] for row in full_overlay["rows"] if row[1]},
                "items": {
                    row[0]: dict(zip(full_overlay["fields"], row[1:]))
                    for row in full_overlay["rows"]
                },
            }
            self.assertLess(
                (self.site / "data" / "i18n" / locale / "catalog-titles.json").stat().st_size,
                len(builder.stable_json_bytes(legacy_overlay)),
            )

            chart_overlay_path = self.site / "data" / "i18n" / locale / builder.CHART_OVERLAY_FILE
            chart_overlay = json.loads(chart_overlay_path.read_text(encoding="utf-8"))
            self.assertEqual(chart_overlay["schema_version"], 2)
            self.assertEqual(chart_overlay["kind"], "charts")
            self.assertEqual(chart_overlay["report_count"], 1)
            self.assertEqual(chart_overlay["chart_count"], 1)
            chart_rows = {row[0]: dict(zip(chart_overlay["fields"], row[1:])) for row in chart_overlay["rows"]}
            self.assertTrue(chart_rows["report:report-ai-1"]["title"].startswith(FAKE_PREFIX[locale]))
            for field in builder.CHART_TRANSLATABLE_LIST_FIELDS:
                self.assertEqual(chart_rows["report:report-ai-1"][field], [])
            chart_fields = chart_rows["chart:chart-ai-1"]
            for field in builder.CHART_TRANSLATABLE_SCALAR_FIELDS:
                self.assertTrue(chart_fields[field].startswith(FAKE_PREFIX[locale]))
            for field in builder.CHART_TRANSLATABLE_LIST_FIELDS:
                self.assertTrue(chart_fields[field][0].startswith(FAKE_PREFIX[locale]))
            chart_metadata = manifest["chart_overlays"][locale]
            self.assertEqual(chart_metadata["path"], f"data/i18n/{locale}/chart-content.json")
            self.assertEqual(chart_metadata["byte_size"], chart_overlay_path.stat().st_size)
            self.assertIn(chart_metadata["path"], manifest["required_paths"])
            hot_overlay_path = self.site / "data" / "i18n" / locale / builder.HOT_REPORT_OVERLAY_FILE
            hot_overlay = json.loads(hot_overlay_path.read_text(encoding="utf-8"))
            self.assertEqual(hot_overlay["schema_version"], 2)
            self.assertEqual(hot_overlay["kind"], "hot-reports")
            self.assertEqual(hot_overlay["source_generation"], "0123456789abcdef")
            self.assertEqual(hot_overlay["fields"], list(builder.HOT_REPORT_TRANSLATABLE_FIELDS))
            self.assertEqual(hot_overlay["item_count"], 1)
            hot_fields = dict(zip(hot_overlay["fields"], hot_overlay["rows"][0][1:]))
            self.assertEqual(hot_overlay["rows"][0][0], "hot:0123456789abcdef")
            for field in builder.HOT_REPORT_TRANSLATABLE_FIELDS:
                self.assertTrue(hot_fields[field].startswith(FAKE_PREFIX[locale]))
            hot_serialized = json.dumps(hot_overlay, ensure_ascii=False)
            self.assertNotIn("filename", hot_serialized)
            self.assertNotIn("object_key", hot_serialized)
            self.assertNotIn("extracted_text", hot_serialized)
            hot_metadata = manifest["hot_report_overlays"][locale]
            self.assertEqual(hot_metadata["path"], f"data/i18n/{locale}/hot-reports.json")
            self.assertEqual(hot_metadata["source_generation"], "0123456789abcdef")
            self.assertEqual(hot_metadata["byte_size"], hot_overlay_path.stat().st_size)
            self.assertIn(hot_metadata["path"], manifest["required_paths"])
            course = json.loads(
                (self.site / locale / "data" / "course-materials.json").read_text(encoding="utf-8")
            )["items"][0]
            self.assertTrue(course["title"].startswith(FAKE_PREFIX[locale]))
            self.assertTrue(course["topic"].startswith(FAKE_PREFIX[locale]))
            self.assertTrue(course["summary"].startswith(FAKE_PREFIX[locale]))
            course_path = self.site / locale / "data" / "course-materials.json"
            course_metadata = manifest["locale_data_files"][locale]["course-materials"]
            self.assertEqual(course_metadata["path"], f"{locale}/data/course-materials.json")
            self.assertEqual(course_metadata["byte_size"], course_path.stat().st_size)
            self.assertEqual(
                course_metadata["sha256"],
                hashlib.sha256(course_path.read_bytes()).hexdigest(),
            )
            self.assertIn(course_metadata["path"], manifest["required_paths"])

            locale_sitemap = ET.parse(self.site / f"sitemap-{locale}.xml").getroot()
            sitemap_rows = locale_sitemap.findall("./{*}url")
            self.assertEqual(len(sitemap_rows), 2)
            sitemap_locations = {str(row.findtext("./{*}loc") or "") for row in sitemap_rows}
            self.assertEqual(sitemap_locations, {
                f"{SITE_URL}/{locale}/",
                f"{SITE_URL}/{locale}/reports/topics/ai/",
            })
            for row in sitemap_rows:
                alternates = row.findall(f"./{{{XHTML_NAMESPACE}}}link")
                self.assertEqual(len(alternates), 5)
                self.assertEqual(
                    {link.attrib.get("hreflang") for link in alternates},
                    {"zh-Hans", "ko", "ja", "ar", "x-default"},
                )

            feed = ET.parse(self.site / locale / "feed.xml").getroot()
            self.assertEqual(feed.findtext("./channel/language"), locale)
            self.assertEqual(feed.findtext("./channel/link"), f"{SITE_URL}/{locale}/")
            self.assertEqual(
                feed.findtext("./channel/item/link"),
                f"{SITE_URL}/{locale}/reports/topics/ai/",
            )
            self.assertEqual(
                feed.findtext("./channel/item/guid"),
                f"{SITE_URL}/{locale}/reports/topics/ai/",
            )
            localized_llms = (self.site / locale / "llms.txt").read_text(encoding="utf-8")
            self.assertIn(f"{SITE_URL}/{locale}/reports/topics/ai/", localized_llms)
            self.assertIn(FAKE_PREFIX[locale], localized_llms)
            localized_llms_full = (self.site / locale / "llms-full.txt").read_text(encoding="utf-8")
            self.assertIn(f"{SITE_URL}/{locale}/reports/topics/ai/", localized_llms_full)
            self.assertIn(FAKE_PREFIX[locale], localized_llms_full)

        locale_css = (self.site / "assets" / "locale.css").read_text(encoding="utf-8")
        rtl_css = (ROOT / "portal_suite" / "locale_assets" / "locale.css").read_text(encoding="utf-8")
        close_rule = re.search(
            r'html\[dir="rtl"\] :is\(\.admin-close, \.account-admin-dialog > \.admin-close\) \{([^}]*)\}',
            rtl_css,
        )
        self.assertIsNotNone(close_rule)
        self.assertIn("inset-inline-end: 10px", close_rule.group(1))
        self.assertIn("right: auto", close_rule.group(1))
        self.assertNotIn("inset-inline-start", close_rule.group(1))
        auto_margin_rule = re.search(
            r'html\[dir="rtl"\] :is\(\.account-admin-more-button, \.hot-comment-order-actions\) \{([^}]*)\}',
            rtl_css,
        )
        self.assertIsNotNone(auto_margin_rule)
        self.assertIn("margin-inline-start: auto", auto_margin_rule.group(1))
        self.assertIn("margin-left: 0", auto_margin_rule.group(1))
        self.assertNotIn("margin-right: 0", auto_margin_rule.group(1))
        self.assertRegex(
            rtl_css,
            r'@media \(min-width: 821px\) \{\s*html\[dir="rtl"\] #accountAdminUserCount \{\s*margin-inline-end: auto;\s*margin-right: 0;',
        )
        self.assertRegex(
            rtl_css,
            r'html\[dir="rtl"\] :is\([^}]*\.account-admin-intake-result[^}]*\.account-admin-table th[^}]*\.account-admin-table td[^}]*\) \{\s*text-align: start;',
        )
        self.assertRegex(
            rtl_css,
            r'html\[dir="rtl"\] \.filter-control select \{\s*padding-inline: 13px 34px;\s*background-position: 18px 18px, 12px 18px;',
        )
        self.assertRegex(
            rtl_css,
            r'html\[dir="rtl"\] :is\(\.embedded-filter-control select, \.account-admin-password-reset select\) \{\s*padding-inline: 11px 34px;',
        )
        sidebar_media = rtl_css.index('@media (max-width: 760px)')
        self.assertNotIn('html[dir="rtl"] .newsfeed-sidebar {\n  transform', rtl_css[:sidebar_media])
        self.assertRegex(
            rtl_css[sidebar_media:],
            r'html\[dir="rtl"\] \.newsfeed-sidebar \{[^}]*transform: translateX\(102%\);[^}]*\}[\s\S]*?html\[dir="rtl"\] \.newsfeed-sidebar\.is-open \{\s*transform: translateX\(0\);',
        )
        self.assertRegex(
            rtl_css[sidebar_media:],
            r'html\[dir="rtl"\] \.news-briefing-panel \{\s*inset-inline: 9px;\s*width: auto;',
        )
        self.assertRegex(
            rtl_css,
            r'html\[dir="rtl"\] \.course-directory-tree-children \{[^}]*padding-inline: 14px 9px;',
        )
        self.assertRegex(
            rtl_css,
            r'@media \(max-width: 820px\) \{\s*html\[dir="rtl"\] \.account-admin-top \{\s*padding: calc\(14px \+ env\(safe-area-inset-top\)\) 14px 13px 52px;',
        )
        self.assertRegex(
            rtl_css,
            r'@media \(max-width: 520px\) \{\s*html\[dir="rtl"\] \.course-directory-tree-children \{\s*padding-inline: 8px 9px;',
        )
        self.assertNotIn('html:lang(zh-Hans)', locale_css)
        self.assertEqual(locale_css.count(".course-material-card.is-cover-missing"), 3)
        self.assertEqual(locale_css.count("td:nth-child(1)::before"), 3)
        self.assertNotIn(".decorative::before", locale_css)
        for locale in builder.LOCALES:
            self.assertIn(f"html:lang({locale}) .course-material-card.is-cover-missing", locale_css)
            self.assertIn(f"html:lang({locale}) #accountAdminUsersSection", locale_css)
            self.assertIn(FAKE_PREFIX[locale], locale_css)

        sitemap_index = ET.parse(self.site / "sitemap.xml").getroot()
        sitemap_entries = {str(row.findtext("./{*}loc") or "") for row in sitemap_index.findall("./{*}sitemap")}
        for locale in builder.LOCALES:
            self.assertIn(f"{SITE_URL}/sitemap-{locale}.xml", sitemap_entries)
        robots = (self.site / "robots.txt").read_text(encoding="utf-8")
        for locale in builder.LOCALES:
            self.assertEqual(robots.count(f"Sitemap: {SITE_URL}/sitemap-{locale}.xml"), 1)

    def test_full_pretranslation_uses_fixed_index_cohort_and_filters_locale_discovery(self) -> None:
        def write_detail(
            relative: str,
            *,
            page_type: str,
            title: str,
            published: str = "",
            body_extra: str = "",
        ) -> None:
            path = self.site / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            canonical = f"{SITE_URL}/{relative}"
            publication = f',"datePublished":"{published}"' if published else ""
            path.write_text(
                f'''<!doctype html>
<html lang="zh-Hans"><head>
  <meta name="robots" content="index,follow,max-snippet:-1">
  <link rel="canonical" href="{canonical}">
  <title>{title}</title>
  <script type="application/ld+json">{{"@context":"https://schema.org","@type":"{page_type}","name":"{title}","url":"{canonical}"{publication}}}</script>
</head><body><main><h1>{title}</h1><p>这是需要完整预翻译的公开详情内容。</p>{body_extra}</main></body></html>
''',
                encoding="utf-8",
            )

        write_detail(
            "reports/recent-report.html",
            page_type="Report",
            title="近期公开报告",
            published="2026-09-02",
        )
        write_detail(
            "reports/old-report.html",
            page_type="Report",
            title="历史公开报告",
            published="2025-01-10",
            body_extra='<img id="report-zsxq" src="https://cdn.zsxq.img/report.png">',
        )
        write_detail(
            "reports/curated-report.html",
            page_type="Report",
            title="人工精选历史报告",
        )
        write_detail(
            "blog/recent-blog.html",
            page_type="BlogPosting",
            title="近期公开文章",
            published="2026-09-01",
            body_extra='<img id="good-blog-image" src="/assets/good.png">',
        )
        write_detail(
            "blog/old-blog.html",
            page_type="BlogPosting",
            title="历史公开文章",
            published="2024-12-01",
            body_extra=(
                '<div id="image-only"><a href="#"><img data-src="https://cdn.zsxq.img/only.png" '
                'alt="仅供知识星球使用的图片说明"></a></div>'
                '<picture id="source-only"><source srcset="https://cdn.example/zsxq_img/a.webp 1x, '
                'https://cdn.example/zsxq_img/b.webp 2x" title="不应发送翻译的图片来源"></picture>'
                '<p id="mixed-copy">必须保留这段正文<img srcset="https://cdn.example/zsxq_img/mixed.png 2x"></p>'
                '<div id="data-srcset-only"><img data-srcset="https://cdn.example/zsxq_img/lazy.webp 2x" '
                'alt="不应发送的延迟图片说明"></div>'
                '<div id="data-original-only"><img data-original="https://cdn.zsxq.img/original.webp" '
                'alt="不应发送的原图说明"></div>'
                '<div id="encoded-only"><img src="https://cdn.example/zsxq%252Eimg/encoded.webp" '
                'alt="不应发送的编码图片说明"></div>'
                '<div id="amp-only"><amp-img src="https://cdn.zsxq.img/amp.webp" '
                'alt="不应发送的 AMP 图片说明"><span>不应发送的 AMP 回退说明</span></amp-img></div>'
                '<div id="background-only" style="background-image:url(https://cdn.zsxq.img/bg.webp)" '
                'aria-label="不应发送的背景图片说明"></div>'
                '<p id="background-copy" style="color:red;background-image:url(https://cdn.zsxq.img/bg-copy.webp)">'
                '背景图删除后仍保留这段正文</p>'
                '<img id="good-blog-image" src="/assets/good.png">'
            ),
        )

        old_blog_path = self.site / "blog" / "old-blog.html"
        deferred_zh = (
            '  <link data-existing="deferred-zh" href="https://portal.example.invalid/blog/old-blog.html" '
            'rel="alternate" hreflang="zh-Hans">'
        )
        deferred_default = (
            '  <link data-existing="deferred-default" hreflang="x-default" '
            'href="https://portal.example.invalid/blog/old-blog.html" rel="alternate">'
        )
        deferred_english = (
            '  <link data-existing="deferred-english" rel="alternate" hreflang="en" '
            'href="https://portal.example.invalid/en/blog/old-blog.html">'
        )
        old_blog_source = old_blog_path.read_text(encoding="utf-8").replace(
            "</head>",
            "\n".join((
                deferred_zh,
                deferred_default,
                deferred_english,
                '  <link data-stale="deferred-ko" rel="alternate" hreflang="ko" '
                'href="https://stale.example/ko/blog/old-blog.html">',
                "</head>",
            )),
        )
        old_blog_path.write_text(old_blog_source, encoding="utf-8")

        home_path = self.site / "index.html"
        home_source = home_path.read_text(encoding="utf-8").replace(
            "</main>",
            '<a href="/reports/old-report.html">历史报告站内入口</a></main>',
        )
        home_path.write_text(home_source, encoding="utf-8")
        chinese_old_blog_body = body_bytes(old_blog_path)

        sitemap_path = self.site / "sitemap-pages.xml"
        sitemap_source = sitemap_path.read_text(encoding="utf-8").replace(
            "</urlset>",
            """  <url><loc>https://portal.example.invalid/reports/recent-report.html</loc><lastmod>2026-09-03</lastmod></url>
  <url><loc>https://portal.example.invalid/reports/old-report.html</loc><lastmod>2026-09-03</lastmod></url>
  <url><loc>https://portal.example.invalid/reports/curated-report.html</loc><lastmod>2026-09-03</lastmod></url>
  <url><loc>https://portal.example.invalid/blog/recent-blog.html</loc><lastmod>2026-09-03</lastmod></url>
  <url><loc>https://portal.example.invalid/blog/old-blog.html</loc><lastmod>2026-09-03</lastmod></url>
</urlset>""",
        )
        sitemap_path.write_text(sitemap_source, encoding="utf-8")

        llms_rows = """- 近期报告：https://portal.example.invalid/reports/recent-report.html
- 历史报告：https://portal.example.invalid/reports/old-report.html
- 精选报告：https://portal.example.invalid/reports/curated-report.html
- 近期文章：https://portal.example.invalid/blog/recent-blog.html
- 历史文章：https://portal.example.invalid/blog/old-blog.html
"""
        (self.site / "llms.txt").write_text(
            (self.site / "llms.txt").read_text(encoding="utf-8") + llms_rows,
            encoding="utf-8",
        )
        full_rows = """
## 近期报告条目
- Canonical URL: https://portal.example.invalid/reports/recent-report.html
- 摘要: 近期报告机器发现条目

## 历史报告条目
- Canonical URL: https://portal.example.invalid/reports/old-report.html
- 摘要: 历史报告机器发现条目

## 精选报告条目
- Canonical URL: https://portal.example.invalid/reports/curated-report.html
- 摘要: 精选历史报告机器发现条目

## 近期文章条目
- Canonical URL: https://portal.example.invalid/blog/recent-blog.html
- 摘要: 近期文章机器发现条目

## 历史文章条目
- Canonical URL: https://portal.example.invalid/blog/old-blog.html
- 摘要: 历史文章机器发现条目
"""
        (self.site / "llms-full.txt").write_text(
            (self.site / "llms-full.txt").read_text(encoding="utf-8") + full_rows,
            encoding="utf-8",
        )
        chinese_llms = {
            name: (self.site / name).read_bytes()
            for name in ("llms.txt", "llms-full.txt")
        }

        catalog_path = self.site / "data" / "catalog.json"
        catalog = json.loads(catalog_path.read_text(encoding="utf-8"))
        catalog["items"].append({
            "id": "old-report",
            "title": "历史公开报告",
            "bank_name": "历史研究机构",
            "industry": "历史研究主题",
            "date_folder": "2025-01-10",
            "available": True,
        })
        catalog["item_count"] = len(catalog["items"])
        catalog_path.write_text(json.dumps(catalog, ensure_ascii=False), encoding="utf-8")

        translator = RecordingTranslator()
        manifest = self._build(
            translator,
            index_start_date="2026-09-01",
            index_allowlist=("/reports/curated-report.html",),
        )

        self.assertNotIn("仅供知识星球使用的图片说明", translator.sources)
        self.assertNotIn("不应发送翻译的图片来源", translator.sources)
        for removed_copy in (
            "不应发送的延迟图片说明",
            "不应发送的原图说明",
            "不应发送的编码图片说明",
            "不应发送的 AMP 图片说明",
            "不应发送的 AMP 回退说明",
            "不应发送的背景图片说明",
        ):
            self.assertNotIn(removed_copy, translator.sources)

        self.assertEqual(manifest["html_page_count"], 7)
        self.assertEqual(manifest["source_indexable_page_count"], 7)
        self.assertEqual(manifest["indexable_page_count"], 5)
        self.assertEqual(manifest["deferred_index_page_count"], 2)
        self.assertEqual(manifest["index_policy"], {
            "mode": "fixed-publication-cutoff",
            "default": "hubs-only",
            "index_start_date": "2026-09-01",
            "allowlist_count": 1,
        })

        expected_indexed = {
            "/",
            "/reports/topics/ai/",
            "/reports/recent-report.html",
            "/reports/curated-report.html",
            "/blog/recent-blog.html",
        }
        deferred = {"/reports/old-report.html", "/blog/old-blog.html"}
        for locale in builder.LOCALES:
            for relative in (
                "reports/recent-report.html",
                "reports/old-report.html",
                "reports/curated-report.html",
                "blog/recent-blog.html",
                "blog/old-blog.html",
            ):
                localized = (self.site / locale / relative).read_text(encoding="utf-8")
                self.assertIn(FAKE_PREFIX[locale], localized)
            for relative in deferred:
                localized = (self.site / locale / relative.lstrip("/")).read_text(encoding="utf-8")
                self.assertIn('<meta name="robots" content="noindex,follow">', localized)
                self.assertNotIn('hreflang="', localized)
            for relative in ("reports/recent-report.html", "reports/curated-report.html", "blog/recent-blog.html"):
                localized = (self.site / locale / relative).read_text(encoding="utf-8")
                self.assertNotIn('content="noindex,follow"', localized)
                self.assertIn('hreflang="', localized)

            old_blog = (self.site / locale / "blog" / "old-blog.html").read_text(encoding="utf-8")
            self.assertNotIn("zsxq.img", old_blog)
            self.assertNotIn("zsxq_img", old_blog)
            self.assertNotIn('id="image-only"', old_blog)
            self.assertNotIn('id="source-only"', old_blog)
            self.assertNotIn('id="data-srcset-only"', old_blog)
            self.assertNotIn('id="data-original-only"', old_blog)
            self.assertNotIn('id="encoded-only"', old_blog)
            self.assertNotIn('id="amp-only"', old_blog)
            self.assertNotIn('id="background-only"', old_blog)
            self.assertIn('id="mixed-copy"', old_blog)
            self.assertIn('id="background-copy"', old_blog)
            self.assertNotIn("background-image", old_blog)
            self.assertIn("color:red", old_blog)
            self.assertIn('id="good-blog-image"', old_blog)
            old_report = (self.site / locale / "reports" / "old-report.html").read_text(encoding="utf-8")
            self.assertIn('id="report-zsxq"', old_report)
            self.assertIn("zsxq.img", old_report)
            home = (self.site / locale / "index.html").read_text(encoding="utf-8")
            self.assertIn(f'href="/{locale}/reports/old-report.html"', home)

            sitemap = ET.parse(self.site / f"sitemap-{locale}.xml").getroot()
            locations = {str(row.findtext("./{*}loc") or "") for row in sitemap.findall("./{*}url")}
            self.assertEqual(locations, {f"{SITE_URL}/{locale}{path}" for path in expected_indexed})

            localized_llms = (self.site / locale / "llms.txt").read_text(encoding="utf-8")
            localized_full = (self.site / locale / "llms-full.txt").read_text(encoding="utf-8")
            for relative in expected_indexed - {"/", "/reports/topics/ai/"}:
                self.assertIn(f"{SITE_URL}/{locale}{relative}", localized_llms)
                self.assertIn(f"{SITE_URL}/{locale}{relative}", localized_full)
            for relative in deferred:
                self.assertNotIn(f"{SITE_URL}/{locale}{relative}", localized_llms)
                self.assertNotIn(f"{SITE_URL}/{locale}{relative}", localized_full)
            overlay = json.loads(
                (self.site / "data" / "i18n" / locale / "catalog-titles.json").read_text(encoding="utf-8")
            )
            self.assertIn("old-report", {row[0] for row in overlay["rows"]})

        self.assertEqual(body_bytes(old_blog_path), chinese_old_blog_body)
        self.assertIn(b"zsxq.img", body_bytes(old_blog_path))
        deferred_root = old_blog_path.read_text(encoding="utf-8")
        for existing in (deferred_zh, deferred_default, deferred_english):
            self.assertEqual(deferred_root.count(existing), 1)
        self.assertNotIn("data-stale=", deferred_root)
        self.assertEqual(alternate_links(deferred_root), {
            "zh-Hans": f"{SITE_URL}/blog/old-blog.html",
            "x-default": f"{SITE_URL}/blog/old-blog.html",
            "en": f"{SITE_URL}/en/blog/old-blog.html",
        })
        for locale in builder.LOCALES:
            self.assertNotIn(f'hreflang="{locale}"', deferred_root)
        self.assertEqual(deferred_root.count("data-kc-locale-bootstrap"), 1)
        for name, before in chinese_llms.items():
            current = (self.site / name).read_bytes()
            self.assertEqual(current, before)
            self.assertIn(b"old-report.html", current)

    def test_index_policy_defaults_to_hubs_and_rejects_bad_configuration(self) -> None:
        self.assertEqual(
            builder.locale_page_kind(f"{SITE_URL}/reports/topics/ai/", SITE_URL),
            "hub",
        )
        self.assertEqual(
            builder.locale_page_kind(f"{SITE_URL}/blog/future-directory-detail/", SITE_URL),
            "detail",
        )
        blog_canonical = f"{SITE_URL}/blog/daily.html"
        visible_time = '<time datetime="2026-09-04">归档日期</time>'
        self.assertIsNone(
            builder.html_publication_date(
                visible_time,
                page_kind="blog-detail",
                canonical=blog_canonical,
            )
        )
        unrelated_schema = (
            '<p>{"datePublished":"2026-09-04"}</p>'
            '<script type="application/ld+json">'
            '{"@type":"BlogPosting","url":"https://portal.example.invalid/blog/other.html",'
            '"datePublished":"2026-09-04"}</script>'
        )
        self.assertIsNone(
            builder.html_publication_date(
                unrelated_schema,
                page_kind="blog-detail",
                canonical=blog_canonical,
            )
        )
        authoritative_schema = (
            '<script type="application/ld+json">'
            '{"@graph":[{"@type":"BlogPosting","@id":"'
            + blog_canonical
            + '#article","url":"'
            + blog_canonical
            + '","datePublished":"2026-09-04"}]}</script>'
        )
        self.assertEqual(
            builder.html_publication_date(
                authoritative_schema,
                page_kind="blog-detail",
                canonical=blog_canonical,
            ).isoformat(),
            "2026-09-04",
        )
        conflicting_schema = (
            authoritative_schema
            + '<script type="application/ld+json">'
            '{"@type":"BlogPosting","url":"https://portal.example.invalid/blog/daily.html",'
            '"datePublished":"2026-09-03"}</script>'
        )
        with self.assertRaisesRegex(builder.TranslationError, "Conflicting datePublished"):
            builder.html_publication_date(
                conflicting_schema,
                page_kind="blog-detail",
                canonical=blog_canonical,
            )

        report = self.site / "reports" / "dated.html"
        report.write_text(
            '<html><head><meta name="robots" content="index,follow">'
            '<link rel="canonical" href="https://portal.example.invalid/reports/dated.html">'
            '<script type="application/ld+json">'
            '{"@type":"Report","url":"https://portal.example.invalid/reports/dated.html",'
            '"datePublished":"2026-09-04"}</script>'
            '</head><body>公开报告</body></html>',
            encoding="utf-8",
        )
        original = {
            self.site / "index.html": (self.site / "index.html").read_text(encoding="utf-8"),
            report: report.read_text(encoding="utf-8"),
        }
        canonicals = {path: builder.extract_canonical(source) for path, source in original.items()}
        plan = builder.build_locale_index_plan(
            original,
            canonicals,
            site_url=SITE_URL,
            index_start_date=None,
        )
        self.assertTrue(plan[self.site / "index.html"].indexable)
        self.assertFalse(plan[report].indexable)
        self.assertTrue(plan[report].force_noindex_follow)
        indexed_plan = builder.build_locale_index_plan(
            original,
            canonicals,
            site_url=SITE_URL,
            index_start_date="2026-09-04",
        )
        self.assertTrue(indexed_plan[report].indexable)
        self.assertEqual(indexed_plan[report].reason, "published-on-or-after-start")
        missing_canonical = self.site / "blog" / "future-without-canonical.html"
        missing_canonical_source = (
            '<html><head><meta name="robots" content="index,follow">'
            '<script type="application/ld+json">'
            '{"@type":"BlogPosting","datePublished":"2026-09-05"}</script>'
            '</head><body>未来公开文章</body></html>'
        )
        missing_decision = builder.locale_index_decision(
            missing_canonical_source,
            "",
            site_url=SITE_URL,
            index_start_date=date.fromisoformat("2026-09-01"),
            index_allowlist=frozenset(),
        )
        self.assertFalse(missing_decision.indexable)
        self.assertTrue(missing_decision.force_noindex_follow)
        self.assertEqual(missing_decision.reason, "missing-canonical")
        with self.assertRaisesRegex(builder.TranslationError, "YYYY-MM-DD"):
            builder.build_locale_index_plan(
                original,
                canonicals,
                site_url=SITE_URL,
                index_start_date="09/04/2026",
            )
        with self.assertRaisesRegex(builder.TranslationError, "no indexable source page"):
            builder.build_locale_index_plan(
                original,
                canonicals,
                site_url=SITE_URL,
                index_start_date=None,
                index_allowlist=("/reports/typo.html",),
            )

    def test_gzip_cache_is_deterministic_and_skips_all_second_build_calls(self) -> None:
        home_path = self.site / "index.html"
        source = home_path.read_text(encoding="utf-8")
        existing_zh = (
            '    <link data-existing="zh" href="https://portal.example.invalid/" '
            'hreflang="zh-Hans" rel="alternate">'
        )
        existing_default = (
            '    <link data-existing="default" rel="alternate" '
            'href="https://portal.example.invalid/" hreflang="x-default">'
        )
        existing_english = (
            '    <link data-existing="english" hreflang="en" '
            'rel="alternate" href="https://portal.example.invalid/en/">'
        )
        stale_locale_rows = "\n".join(
            f'    <link data-stale="{locale}" rel="alternate" hreflang="{locale}" '
            f'href="https://stale.example/{locale}/">'
            for locale in builder.LOCALES
        )
        source = source.replace(
            '    <link rel="alternate" hreflang="zh-Hans" href="https://portal.example.invalid/">\n'
            '    <link rel="alternate" hreflang="x-default" href="https://portal.example.invalid/">',
            "\n".join((existing_zh, existing_default, existing_english, stale_locale_rows)),
        ).replace(
            "  </head>",
            '    <link rel="stylesheet" href="/assets/locale.css?v=stale">\n'
            '    <script src="/assets/locale-runtime.js?v=stale"></script>\n'
            '    <script data-kc-locale-bootstrap>staleBootstrap()</script>\n'
            "  </head>",
        )
        home_path.write_text(source, encoding="utf-8")

        first_translator = RecordingTranslator()
        first_manifest = self._build(first_translator)
        first_cache = self.cache.read_bytes()
        first_home = home_path.read_text(encoding="utf-8")
        cache_payload = json.loads(gzip.decompress(first_cache).decode("utf-8"))
        self.assertEqual(cache_payload["schema_version"], builder.CACHE_SCHEMA_VERSION)
        self.assertTrue(all(cache_payload["locales"][locale] for locale in builder.LOCALES))
        for existing in (existing_zh, existing_default, existing_english):
            self.assertEqual(first_home.count(existing), 1)
        self.assertNotIn("data-stale=", first_home)
        self.assertNotIn("staleBootstrap", first_home)
        self.assertNotIn("?v=stale", first_home)
        self.assertEqual(alternate_links(first_home), {
            "zh-Hans": f"{SITE_URL}/",
            "x-default": f"{SITE_URL}/",
            "en": f"{SITE_URL}/en/",
            "ko": f"{SITE_URL}/ko/",
            "ja": f"{SITE_URL}/ja/",
            "ar": f"{SITE_URL}/ar/",
        })
        self.assertEqual(first_home.count("data-kc-locale-bootstrap"), 1)

        for locale in builder.LOCALES:
            localized_home = (self.site / locale / "index.html").read_text(encoding="utf-8")
            self.assertEqual(alternate_links(localized_home), {
                "zh-Hans": f"{SITE_URL}/",
                "ko": f"{SITE_URL}/ko/",
                "ja": f"{SITE_URL}/ja/",
                "ar": f"{SITE_URL}/ar/",
                "x-default": f"{SITE_URL}/",
            })
            self.assertNotIn('hreflang="en"', localized_home)

        second_translator = mock.Mock(side_effect=AssertionError("cache miss on second build"))
        second_manifest = self._build(second_translator, cache_in=self.cache)

        second_translator.assert_not_called()
        self.assertEqual(self.cache.read_bytes(), first_cache)
        self.assertEqual(first_manifest, second_manifest)
        self.assertEqual(home_path.read_text(encoding="utf-8"), first_home)
        robots = (self.site / "robots.txt").read_text(encoding="utf-8")
        for locale in builder.LOCALES:
            self.assertEqual(robots.count(f"Sitemap: {SITE_URL}/sitemap-{locale}.xml"), 1)

    def test_cache_out_contains_only_current_quality_checked_inventory(self) -> None:
        _protected, unit = builder.unit_for_text("需要翻译的公开研究内容", "html:text:p")
        self.assertIsNotNone(unit)
        assert unit is not None
        translations = {
            "ko": "공개 연구 콘텐츠를 번역했습니다",
            "ja": "公開リサーチ内容を翻訳しました",
            "ar": "تمت ترجمة محتوى البحث العام",
        }
        stale_key = "9" * 64
        cache = builder.empty_cache()
        cache["debug_source_copy"] = "must not survive cache normalization"
        cache["locales"]["obsolete"] = {stale_key: {"source": "old", "translation": "old"}}
        for locale, translation in translations.items():
            cache["locales"][locale][unit.key] = {
                "source": unit.source,
                "translation": translation,
            }
            cache["locales"][locale][stale_key] = {
                "source": "已经撤稿且不再属于公开清单的内容",
                "translation": "stale text that must not ship",
            }

        translator = mock.Mock(side_effect=AssertionError("valid active cache should be reused"))
        missing = builder.translate_missing_units(
            {unit.key: unit},
            cache,
            cache_path=self.cache,
            model=builder.DEFAULT_DEEPSEEK_MODEL,
            base_url="https://api.deepseek.com",
            workers=3,
            timeout=1,
            attempts=1,
            batch_translator=translator,
        )

        translator.assert_not_called()
        self.assertEqual(missing, {locale: 0 for locale in builder.LOCALES})
        stored = json.loads(gzip.decompress(self.cache.read_bytes()).decode("utf-8"))
        self.assertEqual(
            set(stored),
            {"schema_version", "prompt_version", "provider", "model", "locales"},
        )
        self.assertEqual(set(stored["locales"]), set(builder.LOCALES))
        for locale in builder.LOCALES:
            self.assertEqual(set(stored["locales"][locale]), {unit.key})
        self.assertNotIn("已经撤稿", gzip.decompress(self.cache.read_bytes()).decode("utf-8"))

    def test_invalid_active_cache_entry_is_retranslated_before_reuse(self) -> None:
        _protected, unit = builder.unit_for_text("需要翻译的公开研究内容", "html:text:p")
        self.assertIsNotNone(unit)
        assert unit is not None
        cache = builder.empty_cache()
        valid = {
            "ko": "공개 연구 콘텐츠를 번역했습니다",
            "ja": "公開リサーチ内容を翻訳しました",
            "ar": "تمت ترجمة محتوى البحث العام",
        }
        for locale, translation in valid.items():
            cache["locales"][locale][unit.key] = {
                "source": unit.source,
                "translation": unit.source if locale == "ko" else translation,
            }
        calls: list[str] = []

        def translator(locale: str, units: list[builder.TranslationUnit]) -> dict[str, str]:
            calls.append(locale)
            return {current.key: valid[locale] for current in units}

        missing = builder.translate_missing_units(
            {unit.key: unit},
            cache,
            cache_path=self.cache,
            model=builder.DEFAULT_DEEPSEEK_MODEL,
            base_url="https://api.deepseek.com",
            workers=3,
            timeout=1,
            attempts=1,
            batch_translator=translator,
        )

        self.assertEqual(calls, ["ko"])
        self.assertEqual(missing, {"ko": 1, "ja": 0, "ar": 0})
        self.assertEqual(cache["locales"]["ko"][unit.key]["translation"], valid["ko"])

    def test_missing_fake_translations_fail_the_build(self) -> None:
        def missing_translations(
            _locale: str,
            _units: list[builder.TranslationUnit],
        ) -> dict[str, str]:
            return {}

        with self.assertRaisesRegex(builder.TranslationError, "missing batch result"):
            self._build(missing_translations)

    def test_changed_protected_placeholders_fail_the_build(self) -> None:
        def broken_placeholders(
            locale: str,
            units: list[builder.TranslationUnit],
        ) -> dict[str, str]:
            rows = RecordingTranslator()(locale, units)
            return {
                unit.key: builder.PLACEHOLDER_RE.sub("__BROKEN_PLACEHOLDER__", rows[unit.key])
                for unit in units
            }

        with self.assertRaisesRegex(builder.TranslationError, "(?i)placeholder mismatch"):
            self._build(broken_placeholders)

    def test_cache_model_and_prompt_namespaces_cannot_reuse_stale_entries(self) -> None:
        key = "b" * 64
        payload = builder.empty_cache("deepseek-model-a")
        for locale in builder.LOCALES:
            payload["locales"][locale][key] = {
                "source": "需要翻译的中文文本",
                "translation": f"translated-{locale}",
            }
        builder.write_cache(self.cache, payload)

        changed_model = builder.load_cache(self.cache, "deepseek-model-b")
        self.assertEqual(changed_model["model"], "deepseek-model-b")
        self.assertTrue(all(not changed_model["locales"][locale] for locale in builder.LOCALES))

        payload["prompt_version"] = "obsolete-prompt"
        builder.write_cache(self.cache, payload)
        changed_prompt = builder.load_cache(self.cache, "deepseek-model-a")
        self.assertTrue(all(not changed_prompt["locales"][locale] for locale in builder.LOCALES))

    def test_placeholder_validation_handles_large_counts_and_rejects_reserved_source_tokens(self) -> None:
        source = " ".join(["100"] * 1_001) + " 需要翻译"
        protected = builder.protect_text(source)

        self.assertIn("__KC_PH_1000__", protected.canonical)
        self.assertEqual(len(builder.PLACEHOLDER_RE.findall(protected.canonical)), 1_001)
        self.assertEqual(protected.restore(protected.canonical), source)
        with self.assertRaisesRegex(builder.TranslationError, "reserved translation placeholder"):
            builder.protect_text("正文包含 __KC_PH_001__ 保留标记")

        embedded_css = '<style>@page{size:A4}html{direction:ltr}</style><h1>研究报告</h1>'
        protected_css = builder.protect_text(embedded_css)
        self.assertNotIn("@page", protected_css.canonical)
        self.assertEqual(protected_css.restore(protected_css.canonical), embedded_css)

    def test_chinese_adjacent_financial_numbers_and_dates_are_protected_whole(self) -> None:
        source = "营收20.55亿元，同比增长32.2%，净亏损16.2亿元，截至2026-06-30的报告，变动-8.5%。"
        protected = builder.protect_text(source)
        self.assertEqual(protected.replacements, ("20.55", "32.2%", "16.2", "2026-06-30", "-8.5%"))
        self.assertEqual(protected.restore(protected.canonical), source)
        self.assertNotIn("32.", protected.canonical)
        self.assertNotIn("2026", protected.canonical)

    def test_explicit_stock_identifiers_are_whole_without_masking_uppercase_titles(self) -> None:
        source = "证券9660.HK、600000.SH、000001.SZ、$AAPL及NYSE:AAPL；GLOBAL MARKET OUTLOOK"
        protected = builder.protect_text(source)
        self.assertEqual(protected.replacements, ("9660.HK", "600000.SH", "000001.SZ", "$AAPL", "NYSE:AAPL"))
        self.assertIn("GLOBAL MARKET OUTLOOK", protected.canonical)
        self.assertEqual(protected.restore(protected.canonical), source)

    def test_financial_placeholders_preserve_values_without_fidelity_retries(self) -> None:
        source = "营收20.55亿元，同比增长32.2%，净亏损16.2亿元，截至2026-06-30，证券9660.HK。"
        protected, unit = builder.unit_for_text(source, "html:meta:description")
        placeholders = " ".join(builder.PLACEHOLDER_RE.findall(unit.source))
        native = {
            "ko": "매출과 성장률 및 순손실을 집계한 증권 연구 보고서입니다",
            "ja": "売上と成長率および純損失を集計した証券調査レポートです",
            "ar": "هذا تقرير أبحاث الأوراق المالية عن الإيرادات والنمو وصافي الخسائر",
        }
        for locale, text in native.items():
            translated = text + " " + placeholders
            with self.subTest(locale=locale):
                builder.validate_translation_quality(locale, unit, translated)
                self.assertTrue(all(value in protected.restore(translated) for value in protected.replacements))
                first = builder.PLACEHOLDER_RE.findall(unit.source)[0]
                builder.validate_translation_quality(locale, unit, translated.replace(first, ""))
                builder.validate_translation_quality(locale, unit, translated + " " + first)
                with self.assertRaisesRegex(builder.TranslationError, "placeholder mismatch"):
                    builder.validate_translation_quality(locale, unit, translated.replace(first, "__KC_PH_999__"))
        builder.validate_translation_quality("ko", unit, "매출은 99.99억 위안이고 순손실은 88.8억 위안입니다")

    def test_written_chinese_quantity_accepts_natural_korean_digits(self) -> None:
        source = "伯恩斯坦：地平线机器人上半年业绩低于预期，HSD覆盖前五大车企 | " + builder.LATIN_PUBLIC_BRAND
        _protected, unit = builder.unit_for_text(source, "html:title")
        placeholders = " ".join(builder.PLACEHOLDER_RE.findall(unit.source))
        translated = "번스타인: 호라이즌 로보틱스 상반기 실적 기대 이하, HSD가 상위 5대 자동차 제조사 커버 | " + placeholders
        builder.validate_translation_quality("ko", unit, translated)

    def test_written_quantities_accept_native_numeric_formats(self) -> None:
        for locale, source, translated in (
            ("ja", "二分之一年的市场展望", "今後0.5年間の市場見通しです"),
            ("ar", "百分之五点二的增长", "بلغ معدل النمو ٥٫٢ بالمئة خلال الفترة"),
        ):
            with self.subTest(locale=locale):
                _protected, unit = builder.unit_for_text(source, "html:text:p")
                builder.validate_translation_quality(locale, unit, translated)

    def test_deepseek_error_response_does_not_expose_response_body(self) -> None:
        response = mock.Mock(status_code=500, text="private submitted source text")
        response.json.return_value = {"error": "private submitted source text"}

        with self.assertRaisesRegex(builder.TranslationError, "DeepSeek HTTP 500") as raised:
            builder._response_content(response, "ar batch deadbeef")

        self.assertNotIn("private submitted source text", str(raised.exception))

    def test_non_json_deepseek_response_does_not_expose_response_body(self) -> None:
        response = mock.Mock(status_code=200, text="private submitted source text")
        response.json.side_effect = ValueError("not json")

        with self.assertRaisesRegex(builder.TranslationError, "non-JSON DeepSeek response") as raised:
            builder._response_content(response, "ko batch deadbeef")

        self.assertNotIn("private submitted source text", str(raised.exception))

    def test_deepseek_base_url_rejects_embedded_credentials_and_query_secrets(self) -> None:
        for value in (
            "https://user:password@api.deepseek.com",
            "https://api.deepseek.com?api_key=secret",
            "https://api.deepseek.com#secret",
        ):
            with self.subTest(value=value):
                with self.assertRaisesRegex(builder.TranslationError, "allowed DeepSeek host"):
                    builder.validate_deepseek_base_url(value)

    def test_visible_single_word_ui_inventory_is_translated_without_program_tokens(self) -> None:
        labels = (
            "From", "To", "Rows", "Industry", "Contact", "Key", "Unlock",
            "Generate", "Private", "Summary", "Narrative", "Structured",
            "Regions", "Newsletter", "Timezone", "Playlist", "Topic", "Story",
        )
        for label in labels:
            with self.subTest(label=label):
                _protected, html_unit = builder.unit_for_text(label, "html:text:span")
                self.assertIsNotNone(html_unit)
                self.assertTrue(builder.javascript_literal_needs_translation(label))
        for token in ("PDF", "UTM", "POST", "Content-Type", "DOMContentLoaded"):
            with self.subTest(program_token=token):
                self.assertFalse(builder.javascript_literal_needs_translation(token))
                if token.isupper():
                    _protected, html_unit = builder.unit_for_text(token, "html:text:span")
                    self.assertIsNone(html_unit)

    def test_native_language_labels_are_only_preserved_as_complete_values(self) -> None:
        for label in builder.NATIVE_LANGUAGE_LABELS:
            with self.subTest(label=label):
                protected, unit = builder.unit_for_text(label, "html:text:span")
                self.assertIsNone(unit)
                self.assertEqual(protected.restore(protected.canonical), label)

        for phrase in ("中文金融研报", "Read this report in English"):
            with self.subTest(phrase=phrase):
                protected, unit = builder.unit_for_text(phrase, "html:text:title")
                self.assertIsNotNone(unit)
                self.assertIn(phrase, protected.canonical)

    def test_javascript_object_keys_labels_and_ternaries_are_distinguished(self) -> None:
        source = '''
const keyed = { "程序键" /* schema key */ : "internal-token" };
const card = { label: "可见标签", route: "/reports/private.html" };
const first = ready ? "第一分支" /* conditional separator */ : "第二分支";
const joined = ready ? prefix + "拼接分支" : "回退分支";
if (mode === "程序枚举") document.getElementById("中文节点");
'''
        literals = {
            inner: (start, end)
            for start, end, quote, inner in builder.scan_quoted_javascript(source)
            if quote != "`"
        }

        def needs(value: str) -> bool:
            start, end = literals[value]
            return builder.javascript_literal_needs_translation(
                value,
                source=source,
                start=start,
                end=end,
            )

        key_start, key_end = literals["程序键"]
        self.assertTrue(builder.javascript_literal_is_object_key(source, key_start, key_end))
        self.assertFalse(needs("程序键"))
        for label in ("可见标签", "第一分支", "第二分支", "拼接分支", "回退分支"):
            with self.subTest(visible_label=label):
                self.assertTrue(needs(label))
        for token in ("/reports/private.html", "程序枚举", "中文节点"):
            with self.subTest(program_token=token):
                self.assertFalse(needs(token))

    def test_real_javascript_covers_all_211_previously_missed_chinese_ternary_literals(self) -> None:
        expected_by_asset = {
            "app.js": 187,
            "charts.js": 4,
            "contact.js": 0,
            "report-chat.js": 19,
            "report-research-export.js": 1,
            "site-runtime.js": 0,
            "xlsx-export.js": 0,
        }
        observed: dict[str, int] = {}
        for asset_name in builder.LOCALIZED_JS_ASSETS:
            source = (ROOT / "portal_suite" / "site_src" / "assets" / asset_name).read_text(encoding="utf-8")
            count = 0
            for start, end, quote, inner in builder.scan_quoted_javascript(source):
                values = (
                    [part for is_expression, part in builder.template_literal_parts(inner) if not is_expression]
                    if quote == "`"
                    else [inner]
                )
                for value in values:
                    after = builder._javascript_trivia_after(source, end)
                    if not builder.CJK_RE.search(value) or after >= len(source) or source[after] != ":":
                        continue
                    if builder.javascript_literal_is_object_key(source, start, end):
                        continue
                    count += 1
                    self.assertTrue(
                        builder.javascript_literal_needs_translation(
                            value,
                            source=source,
                            start=start,
                            end=end,
                        ),
                        f"{asset_name}:{source.count(chr(10), 0, start) + 1} remains outside translation coverage",
                    )
            observed[asset_name] = count
        self.assertEqual(observed, expected_by_asset)
        self.assertEqual(sum(observed.values()), 211)

    def test_real_javascript_has_no_unclassified_chinese_ui_literals(self) -> None:
        for asset_name in builder.LOCALIZED_JS_ASSETS:
            source = (ROOT / "portal_suite" / "site_src" / "assets" / asset_name).read_text(encoding="utf-8")
            with self.subTest(asset_name=asset_name):
                builder.validate_javascript_translation_coverage(source, asset_name)

    def test_nested_template_expression_strings_are_translated_and_residuals_fail_closed(self) -> None:
        source = '''
const markup = `<section>${ready ? "嵌套第一分支" : `<span aria-label="图表证据">嵌套回退文案</span>`}</section>`;
'''
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_javascript_units(source, "nested.js", units)
        unit_sources = {unit.source for unit in units.values()}
        self.assertIn("嵌套第一分支", unit_sources)
        self.assertIn("图表证据", unit_sources)
        self.assertTrue(any("嵌套回退文案" in value for value in unit_sources))

        def korean(unit: builder.TranslationUnit) -> str:
            return (
                unit.source
                .replace("嵌套第一分支", "중첩 첫 번째 분기")
                .replace("图表证据", "차트 근거")
                .replace("嵌套回退文案", "중첩 대체 문구")
            )

        cache = {
            "locales": {
                "ko": {
                    unit.key: {"source": unit.source, "translation": korean(unit)}
                    for unit in units.values()
                },
            },
        }

        rendered = builder.render_localized_javascript(source, "nested.js", "ko", cache)

        self.assertIn("중첩 첫 번째 분기", rendered)
        self.assertIn('aria-label="차트 근거"', rendered)
        self.assertIn("중첩 대체 문구", rendered)
        builder.validate_localized_javascript_residuals(source, rendered, "nested.js", "ko")
        with self.assertRaisesRegex(builder.TranslationError, "Chinese UI literals remain"):
            builder.validate_localized_javascript_residuals(source, source, "nested.js", "ko")

    def test_javascript_markup_translates_visible_attributes_without_touching_structure(self) -> None:
        source = 'const markup = ready ? `<span aria-label="相关知名机构">标签</span>` : "";\n'
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_javascript_units(source, "fixture.js", units)
        self.assertIn("相关知名机构", {unit.source for unit in units.values()})
        cache = {
            "locales": {
                "ko": {
                    unit.key: {
                        "source": unit.source,
                        "translation": unit.source.replace("相关知名机构", "관련 기관").replace("标签", "레이블"),
                    }
                    for unit in units.values()
                },
            },
        }

        rendered = builder.render_localized_javascript(source, "fixture.js", "ko", cache)

        self.assertIn('aria-label="관련 기관"', rendered)
        self.assertIn(">레이블</span>", rendered)
        self.assertNotIn("相关知名机构", rendered)
        self.assertNotIn("标签", rendered)

    def test_javascript_transport_literals_never_enter_translation_inventory(self) -> None:
        source = r'''
const uiModel = { label: "可见对象标签" };
const payloadPreview = { label: "载荷预览可见标签" };
status.textContent = ready ? "可见保存状态" : "可见失败状态";
const markup = `<button aria-label="可见按钮说明">可见按钮正文</button>`;
fetch("/api/private").catch(() => { node.textContent = "异步可见错误"; });
document.body.append("DOM 可见说明");
const map = new Map();
map.set("label", "Map 可见标签");
function payloadPreviewCard() {
  const payload = { label: "同名作用域可见标签" };
  return payload.label;
}

const payload = { note: "内部请求备注", nested: { label: "内部载荷标签" } };
payload.lateNote = "内部后置属性";
Object.assign(payload, { mergedNote: "内部合并属性" });
const payloadAlias = payload;
const headers = { Authorization: "内部授权头", "X-Trace": "内部追踪头" };
headers["X-Late"] = "内部后置头";
const outgoingHeaders = headers;
const options = {
  headers: outgoingHeaders,
  body: JSON.stringify(payloadAlias),
  audit: "内部选项值",
};
fetch("/api/private", options);
fetch("/api/private", { body: JSON.stringify({ note: "内联请求正文" }) });
new Request("/api/private", { body: "Request 内部正文" });
const serialized = JSON.stringify({ text: "仅序列化内部值" });
const queryParams = new URLSearchParams({ q: "内部查询参数" });
queryParams.set("lang", "内部查询覆盖");
const formData = new FormData();
formData.append("note", "内部表单内容");
const transportHeaders = new Headers({ "X-Mode": "内部头构造值" });
transportHeaders.set("X-Extra", "内部头追加值");
const standaloneAuth = { Authorization: "内部授权常量" };
fetch(`/api/private?q=${encodeURIComponent("内部嵌套查询")}`);
'''
        visible_translations = {
            "可见对象标签": "표시 객체 레이블",
            "载荷预览可见标签": "페이로드 미리보기 레이블",
            "可见保存状态": "표시 저장 상태",
            "可见失败状态": "표시 실패 상태",
            "可见按钮说明": "표시 버튼 설명",
            "可见按钮正文": "표시 버튼 본문",
            "异步可见错误": "비동기 표시 오류",
            "DOM 可见说明": "DOM 표시 설명",
            "Map 可见标签": "Map 표시 레이블",
            "同名作用域可见标签": "동일 이름 범위 표시 레이블",
        }
        transport_values = {
            "内部请求备注",
            "内部载荷标签",
            "内部后置属性",
            "内部合并属性",
            "内部授权头",
            "内部追踪头",
            "内部后置头",
            "内部选项值",
            "内联请求正文",
            "Request 内部正文",
            "仅序列化内部值",
            "内部查询参数",
            "内部查询覆盖",
            "内部表单内容",
            "内部头构造值",
            "内部头追加值",
            "内部授权常量",
            "内部嵌套查询",
        }
        units: dict[str, builder.TranslationUnit] = {}

        builder.collect_javascript_units(source, "transport.js", units)

        unit_sources = {unit.source for unit in units.values()}
        for visible_value in visible_translations:
            self.assertTrue(any(visible_value in unit_source for unit_source in unit_sources))
        self.assertTrue(transport_values.isdisjoint(unit_sources))
        builder.validate_javascript_translation_coverage(source, "transport.js")

        cache = {
            "locales": {
                "ko": {
                    unit.key: {
                        "source": unit.source,
                        "translation": next(
                            (
                                unit.source.replace(chinese, korean)
                                for chinese, korean in visible_translations.items()
                                if chinese in unit.source
                            ),
                            unit.source,
                        ),
                    }
                    for unit in units.values()
                },
            },
        }
        rendered = builder.render_localized_javascript(source, "transport.js", "ko", cache)
        for korean in visible_translations.values():
            self.assertIn(korean, rendered)
        for transport_value in transport_values:
            self.assertIn(transport_value, rendered)
        builder.validate_localized_javascript_residuals(source, rendered, "transport.js", "ko")
        with self.assertRaisesRegex(builder.TranslationError, "unbalanced JavaScript transport call"):
            builder.collect_javascript_units(
                'fetch("/api/private", { body: "内部未闭合正文" ',
                "broken-transport.js",
                {},
            )

    def test_css_content_scanner_covers_course_fallback_and_all_mobile_table_headers(self) -> None:
        styles = (ROOT / "portal_suite" / "site_src" / "assets" / "styles.css").read_text(encoding="utf-8")
        rules = builder.scan_css_content_rules(styles, "styles.css")
        literal_values = {
            inner
            for rule in rules
            for _start, _end, _quote, inner in builder.scan_quoted_css(rule.content_value)
        }
        self.assertEqual(len(rules), 13)
        self.assertEqual(literal_values, {
            "暂无可选机构",
            "封面暂不可用",
            "用户名",
            "邮箱",
            "注册站点",
            "状态",
            "账号",
            "实际下载权限",
            "到期",
            "权限来源",
            "注册",
            "最近登录",
            "操作",
        })
        table_rules = [rule for rule in rules if "account-admin-table" in rule.selector]
        self.assertEqual(len(table_rules), 11)
        self.assertTrue(all(rule.at_rules == ("@media (max-width: 820px)",) for rule in table_rules))

    def test_css_content_overrides_are_locale_scoped_and_preserve_media_queries(self) -> None:
        source = '''
.cover::after { content: "封面暂不可用"; }
.icon::before { content: " ·"; }
@media (max-width: 640px) { .row::before { content: "用户名"; } }
'''
        rules = builder.scan_css_content_rules(source, "fixture.css")
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_css_content_units(rules, units)
        translations = {
            "ko": {"封面暂不可用": "표지를 사용할 수 없음", "用户名": "사용자 이름"},
            "ja": {"封面暂不可用": "表紙を利用できません", "用户名": "ユーザー名"},
            "ar": {"封面暂不可用": "الغلاف غير متاح", "用户名": "اسم المستخدم"},
        }
        cache = {
            "locales": {
                locale: {
                    unit.key: {
                        "source": unit.source,
                        "translation": translations[locale][unit.source],
                    }
                    for unit in units.values()
                }
                for locale in builder.LOCALES
            },
        }

        rendered = builder.render_localized_css_content_overrides(rules, cache)

        self.assertNotIn("html:lang(zh-Hans)", rendered)
        self.assertNotIn(".icon::before", rendered)
        self.assertEqual(rendered.count("@media (max-width: 640px)"), 3)
        for locale in builder.LOCALES:
            self.assertIn(f"html:lang({locale}) .cover::after", rendered)
            self.assertIn(f"html:lang({locale}) .row::before", rendered)
            self.assertIn(translations[locale]["封面暂不可用"], rendered)
            self.assertIn(translations[locale]["用户名"], rendered)

    def test_css_content_translates_only_display_strings_not_function_data(self) -> None:
        source = r'''
.mixed::before { content: "可见前缀" url("/api/private/秘密报告.pdf") "可见后缀"; }
.assets::before { content: image-set(url("秘密一.png") 1x, "秘密二.png" 2x); }
.variable::before { content: var(--empty, "可见变量回退"); }
.attribute::before { content: attr(data-label, "可见属性回退"); }
.attribute-url::before { content: attr(data-src type(<url>), "秘密后备图.png"); }
.chapter::before { content: counters(chapter, "秘密分隔") "可见章节"; }
'''
        rules = builder.scan_css_content_rules(source, "fixture.css")
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_css_content_units(rules, units)
        display_values = {
            "可见前缀",
            "可见后缀",
            "可见变量回退",
            "可见属性回退",
            "可见章节",
        }
        program_values = {
            "/api/private/秘密报告.pdf",
            "秘密一.png",
            "秘密二.png",
            "秘密后备图.png",
            "秘密分隔",
        }

        self.assertEqual({unit.source for unit in units.values()}, display_values)
        self.assertEqual(len(rules), 4)
        self.assertTrue(program_values.isdisjoint({unit.source for unit in units.values()}))

        translations = {
            "ko": {
                "可见前缀": "표시 접두사",
                "可见后缀": "표시 접미사",
                "可见变量回退": "표시 변수 대체 문구",
                "可见属性回退": "표시 속성 대체 문구",
                "可见章节": "표시 장",
            },
            "ja": {
                "可见前缀": "表示する接頭辞",
                "可见后缀": "表示する接尾辞",
                "可见变量回退": "表示する変数の代替文",
                "可见属性回退": "表示する属性の代替文",
                "可见章节": "表示する章",
            },
            "ar": {
                "可见前缀": "بادئة مرئية",
                "可见后缀": "لاحقة مرئية",
                "可见变量回退": "بديل المتغير المرئي",
                "可见属性回退": "بديل السمة المرئية",
                "可见章节": "الفصل المرئي",
            },
        }
        cache = {
            "locales": {
                locale: {
                    unit.key: {
                        "source": unit.source,
                        "translation": translations[locale][unit.source],
                    }
                    for unit in units.values()
                }
                for locale in builder.LOCALES
            },
        }
        rendered = builder.render_localized_css_content_overrides(rules, cache)
        self.assertIn('url("/api/private/秘密报告.pdf")', rendered)
        self.assertIn('counters(chapter, "秘密分隔")', rendered)
        self.assertNotIn(".assets::before", rendered)
        self.assertNotIn(".attribute-url::before", rendered)
        for locale in builder.LOCALES:
            self.assertIn(f"html:lang({locale}) .mixed::before", rendered)
            for display_value in display_values:
                self.assertIn(translations[locale][display_value], rendered)

        with self.assertRaisesRegex(builder.TranslationError, "Cannot classify CSS content text"):
            builder.scan_css_content_rules(
                '.unknown::before { content: mystery("未知中文参数"); }',
                "fixture.css",
            )

    def test_deepseek_requests_json_output_with_thinking_disabled(self) -> None:
        unit = builder.TranslationUnit(
            key="d" * 64,
            context="test:json-output",
            source="需要翻译的完整测试文本",
        )
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "choices": [{
                "message": {
                    "content": json.dumps({
                        "translations": [{"id": "0", "text": "번역 결과"}],
                    }, ensure_ascii=False),
                },
            }],
        }
        request = mock.Mock(return_value=response)
        fake_http_module = mock.Mock(request_with_key_fallback=request)
        with mock.patch.dict(sys.modules, {"deepseek_http": fake_http_module}):
            result = builder.deepseek_translate_batch(
                "ko",
                [unit],
                model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com",
                timeout=1,
                attempts=1,
            )

        self.assertEqual(result, {unit.key: "번역 결과"})
        payload = request.call_args.kwargs["payload"]
        self.assertEqual(payload["response_format"], {"type": "json_object"})
        self.assertEqual(payload["thinking"], {"type": "disabled"})
        message = json.loads(payload["messages"][1]["content"])
        self.assertEqual(message["items"], [{"id": "0", "context": unit.context, "source_text": unit.source}])
        self.assertEqual(message["target_language"], "Korean (한국어)")
        self.assertEqual(message["locale"], "ko")
        self.assertIn("Korean (한국어)", message["task"])
        self.assertNotIn("translations", message)
        self.assertNotIn(unit.key, json.dumps(payload))
        self.assertIn(
            "Do not copy the source or merely add a target-language prefix",
            payload["messages"][0]["content"],
        )

    def test_deepseek_compact_ids_map_unordered_responses_to_cache_keys(self) -> None:
        units = [
            builder.TranslationUnit(key="a" * 64, context="test:first", source="第一段研究报告"),
            builder.TranslationUnit(key="b" * 64, context="test:second", source="第二段研究报告"),
        ]
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "choices": [{"message": {"content": json.dumps({
                "translations": [
                    {"id": "1", "text": "두 번째 연구 보고서"},
                    {"id": "0", "text": "첫 번째 연구 보고서"},
                ],
            }, ensure_ascii=False)}}],
        }
        request = mock.Mock(return_value=response)
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            result = builder.deepseek_translate_batch(
                "ko", units, model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", timeout=1, attempts=1,
            )

        self.assertEqual(result, {
            units[0].key: "첫 번째 연구 보고서",
            units[1].key: "두 번째 연구 보고서",
        })
        payload = request.call_args.kwargs["payload"]
        self.assertEqual(json.loads(payload["messages"][1]["content"])["items"], [
            {"id": str(index), "context": unit.context, "source_text": unit.source} for index, unit in enumerate(units)
        ])
        for unit in units:
            self.assertNotIn(unit.key, json.dumps(payload))

    def test_deepseek_compact_ids_reject_invalid_responses(self) -> None:
        units = [
            builder.TranslationUnit(key="a" * 64, context="test:first", source="第一段研究报告"),
            builder.TranslationUnit(key="b" * 64, context="test:second", source="第二段研究报告"),
        ]
        first = {"id": "0", "text": "첫 번째 연구 보고서"}
        second = {"id": "1", "text": "두 번째 연구 보고서"}
        invalid_rows = {
            "missing": [first],
            "unknown": [first, {**second, "id": "2"}],
            "original_cache_key": [first, {**second, "id": units[1].key}],
            "numeric": [first, {**second, "id": 1}],
            "missing_id": [first, {"text": second["text"]}],
            "invalid_type": [first, {**second, "id": ["1"]}],
            "unchanged_source": [first, {**second, "text": units[1].source}],
        }
        for label, rows in invalid_rows.items():
            with self.subTest(label=label):
                response = mock.Mock(status_code=200)
                response.json.return_value = {
                    "choices": [{"message": {"content": json.dumps({
                        "translations": rows,
                    }, ensure_ascii=False)}}],
                }
                request = mock.Mock(return_value=response)
                with mock.patch.dict(sys.modules, {
                    "deepseek_http": mock.Mock(request_with_key_fallback=request),
                }):
                    with self.assertRaises(builder.TranslationError):
                        builder.deepseek_translate_batch(
                            "ko", units, model=builder.DEFAULT_DEEPSEEK_MODEL,
                            base_url="https://api.deepseek.com", timeout=1, attempts=1,
                        )

    def test_preflight_saves_partial_cache_without_rendering_or_requiring_full_coverage(self) -> None:
        before = {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()}
        diagnostics = self.temporary_root / "preflight.json"
        translator = RecordingTranslator()
        result = self._build(
            translator, preflight_only=True, preflight_batches_per_locale=1,
            diagnostics_out=diagnostics, max_provider_requests=6,
        )
        self.assertTrue(result["preflight_only"])
        self.assertEqual(result["selected_batches"], 3)
        self.assertEqual(len(translator.calls), 3)
        self.assertEqual(before, {path: path.read_bytes() for path in self.site.rglob("*") if path.is_file()})
        cached = builder.load_cache(self.cache, builder.DEFAULT_DEEPSEEK_MODEL)
        for locale in builder.LOCALES:
            self.assertGreater(len(cached["locales"][locale]), 0)
            self.assertLess(len(cached["locales"][locale]), result["source_unit_count"])
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["status"], "passed")
        self.assertEqual(report["workers"], 1)
        self.assertGreater(len(report["selected_contexts"]), 1)

    def test_failed_preflight_stops_after_first_batch_and_does_not_render(self) -> None:
        diagnostics = self.temporary_root / "failed-preflight.json"
        translator = mock.Mock(side_effect=builder.TranslationError("placeholder mismatch"))
        with self.assertRaisesRegex(builder.TranslationError, "placeholder mismatch"):
            self._build(translator, preflight_only=True, diagnostics_out=diagnostics)
        self.assertEqual(translator.call_count, 1)
        self.assertTrue(self.cache.exists())
        self.assertFalse((self.site / "ko").exists())
        self.assertEqual(json.loads(diagnostics.read_text())["status"], "failed")

    def test_preflight_subset_preserves_unreferenced_full_cache(self) -> None:
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        other = builder.TranslationUnit("b" * 64, "html:text:p", "其他公开研究内容")
        cache = builder.empty_cache()
        for locale in builder.LOCALES:
            cache["locales"][locale][other.key] = {
                "source": other.source, "translation": FAKE_COPY[locale],
            }
        builder.translate_missing_units(
            {unit.key: unit}, cache, cache_path=self.cache,
            model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
            workers=50, timeout=1, attempts=3, preflight_only=True,
            batch_translator=RecordingTranslator(),
        )
        stored = builder.load_cache(self.cache, builder.DEFAULT_DEEPSEEK_MODEL)
        for locale in builder.LOCALES:
            self.assertEqual(set(stored["locales"][locale]), {unit.key, other.key})

    @mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "test-primary-secret", "DEEPSEEK_API_KEY_BACKUP": "test-backup-secret"}, clear=True)
    def test_request_budget_includes_output_retries_and_records_usage_before_parse_failure(self) -> None:
        diagnostics = self.temporary_root / "usage.json"
        state = builder.TranslationRun(diagnostics, max_requests=2)
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "choices": [{"finish_reason": "length", "message": {"content": '{"translations":['}}],
            "usage": {"prompt_tokens": 11, "completion_tokens": 7, "total_tokens": 18},
        }
        request = mock.Mock(return_value=response)
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            with self.assertRaisesRegex(builder.TranslationStopped, "limit"):
                builder.deepseek_translate_batch(
                    "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", timeout=1, attempts=5, run_state=state,
                )
        state.write()
        self.assertEqual(request.call_count, 2)
        for call in request.call_args_list:
            self.assertEqual(call.kwargs["max_attempts"], 1)
            self.assertEqual(call.kwargs["api_keys"], [("configured", "test-primary-secret")])
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["provider_requests"], 2)
        self.assertEqual(report["usage_totals"], {"prompt_tokens": 22, "completion_tokens": 14, "total_tokens": 36})
        self.assertEqual([row["finish_reason"] for row in report["responses"]], ["length", "length"])
        self.assertEqual(len(report["failure_samples"]), 2)
        self.assertNotIn("test-primary-secret", diagnostics.read_text())
        self.assertNotIn("test-backup-secret", diagnostics.read_text())

    @mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "fake-key"}, clear=True)
    def test_402_stops_new_batches_without_retry_or_invalid_output_label(self) -> None:
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究内容") for i in range(20)}
        diagnostics = self.temporary_root / "http402.json"
        response = mock.Mock(status_code=402)
        response.json.return_value = {"error": {"message": "Insufficient Balance"}}
        request = mock.Mock(return_value=response)
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}), mock.patch.object(builder, "log") as logger:
            with self.assertRaisesRegex(builder.TranslationError, "HTTP 402"):
                builder.translate_missing_units(
                    units, builder.empty_cache(), cache_path=self.cache,
                    model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                    workers=1, timeout=1, attempts=3, max_batch_items=1, diagnostics_out=diagnostics,
                )
        self.assertEqual(request.call_count, 1)
        self.assertTrue(self.cache.exists())
        self.assertFalse(any("invalid output" in call.args[0] for call in logger.call_args_list))
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["provider_requests"], 1)
        self.assertEqual(report["responses"][0]["usage"], "unknown")
        self.assertEqual(report["usage_unknown_responses"], 1)

    def test_systemic_failures_stop_bounded_queue_and_preserve_completed_cache(self) -> None:
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究内容") for i in range(20)}
        translator = RecordingTranslator()
        calls = 0

        def fail_after_success(locale: str, batch: list[builder.TranslationUnit]) -> dict[str, str]:
            nonlocal calls
            calls += 1
            if calls > 1:
                raise builder.TranslationError("translation has no Hangul")
            return translator(locale, batch)

        with mock.patch.object(builder.concurrent.futures, "ThreadPoolExecutor", wraps=concurrent.futures.ThreadPoolExecutor) as executor:
            with self.assertRaisesRegex(builder.TranslationError, "no Hangul"):
                builder.translate_missing_units(
                    units, builder.empty_cache(), cache_path=self.cache,
                    model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                    workers=1, timeout=1, attempts=1, max_batch_items=1,
                    batch_translator=fail_after_success,
                )
        executor.assert_called_once_with(max_workers=1)
        self.assertEqual(calls, 4, "only one successful batch plus three failures may run, not all 60 jobs")
        cache = builder.load_cache(self.cache, builder.DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(sum(len(rows) for rows in cache["locales"].values()), 1)

    @mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "fake-key"}, clear=True)
    def test_parallel_provider_budget_and_pending_queue_are_bounded(self) -> None:
        units = {f"{i:064x}": builder.TranslationUnit(f"{i:064x}", "html:text:p", "公开研究内容") for i in range(20)}
        diagnostics = self.temporary_root / "parallel-budget.json"

        def provider(_url: str, **kwargs: object) -> mock.Mock:
            payload = kwargs["payload"]
            rows = json.loads(payload["messages"][1]["content"])["items"]
            native_text = FAKE_COPY[kwargs["label"].split()[0]]
            response = mock.Mock(status_code=200)
            response.json.return_value = {
                "choices": [{"finish_reason": "stop", "message": {"content": json.dumps({
                    "translations": [{"id": row["id"], "text": native_text} for row in rows],
                })}}],
                "usage": {"prompt_tokens": 5, "completion_tokens": 4, "total_tokens": 9},
            }
            return response

        request = mock.Mock(side_effect=provider)
        real_wait = concurrent.futures.wait
        observed_pending: list[int] = []

        def check_pending(futures: object, **kwargs: object) -> object:
            observed_pending.append(len(futures))
            return real_wait(futures, **kwargs)

        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}), mock.patch.object(builder.concurrent.futures, "wait", side_effect=check_pending):
            with self.assertRaisesRegex(builder.TranslationError, "limit"):
                builder.translate_missing_units(
                    units, builder.empty_cache(), cache_path=self.cache,
                    model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                    workers=4, timeout=1, attempts=3, max_batch_items=1,
                    max_provider_requests=6, diagnostics_out=diagnostics,
                )
        self.assertEqual(request.call_count, 6)
        self.assertLessEqual(max(observed_pending), 4)
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["provider_requests"], 6)
        self.assertEqual(report["usage_totals"]["total_tokens"], 54)
        self.assertEqual(len(report["responses"]), 6)
        stored = builder.load_cache(self.cache, builder.DEFAULT_DEEPSEEK_MODEL)
        self.assertEqual(sum(len(rows) for rows in stored["locales"].values()), 6)

    def test_partial_usage_and_transport_without_response_are_explicitly_unknown(self) -> None:
        diagnostics = self.temporary_root / "partial-usage.json"
        state = builder.TranslationRun(diagnostics, max_requests=2)
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "choices": [{"message": {"content": json.dumps({
                "translations": [{"id": "0", "text": "공개 연구 내용입니다"}],
            })}}],
            "usage": {"total_tokens": 9},
        }
        request = mock.Mock(side_effect=[response, OSError("private transport request details")])
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            builder.deepseek_translate_batch(
                "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", timeout=1, attempts=3, run_state=state,
            )
            with self.assertRaisesRegex(builder.TranslationError, "transport failed"):
                builder.deepseek_translate_batch(
                    "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", timeout=1, attempts=3, run_state=state,
                )
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["provider_requests"], 2)
        self.assertEqual(report["unobserved_provider_requests"], 1)
        self.assertEqual(report["usage_partial_responses"], 1)
        self.assertEqual(report["usage_complete_responses"], 0)
        self.assertEqual(report["responses"][0]["usage_completeness"], "partial")
        self.assertEqual(report["responses"][0]["missing_usage_fields"], ["prompt_tokens", "completion_tokens"])
        self.assertEqual(report["usage_totals"], {"total_tokens": 9})
        self.assertNotIn("private transport", diagnostics.read_text())

    def test_quality_failure_sample_locates_late_wire_id_and_matching_translation(self) -> None:
        diagnostics = self.temporary_root / "late-row.json"
        state = builder.TranslationRun(diagnostics, max_requests=1)
        units = [builder.TranslationUnit(f"{i:064x}", "html:text:p", f"公开研究内容 {i}") for i in range(32)]
        rows = [{"id": str(i), "text": "검증된 금융 연구 문안입니다 " * 8 + str(i)} for i in range(32)]
        rows[23]["text"] = units[23].source
        response = mock.Mock(status_code=200)
        response.json.return_value = {"choices": [{"message": {"content": json.dumps({
            "translations": rows,
        }, ensure_ascii=False)}}]}
        request = mock.Mock(return_value=response)
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            with self.assertRaisesRegex(builder.TranslationError, "unchanged source text for 23"):
                builder.deepseek_translate_batch(
                    "ko", units, model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", timeout=1, attempts=1, run_state=state,
                )
        sample = json.loads(diagnostics.read_text())["failure_samples"][0]
        self.assertEqual([row["id"] for row in sample["source"]], ["23"])
        self.assertEqual(sample["source"][0]["text"], units[23].source)
        self.assertEqual(sample["translation_rows"], [{"id": "23", "text": units[23].source}])

    def test_structural_failure_sample_keeps_actual_late_response_row(self) -> None:
        units = [builder.TranslationUnit(str(i), "html:text:p", f"公开研究内容 {i}") for i in range(8)]
        cases = (
            ({"id": 3, "text": FAKE_COPY["ko"]}, "3", "failed_row_translation_id"),
            ({"id": "unexpected", "text": FAKE_COPY["ko"]}, "7", "response_row_position_hint"),
            (["malformed row"], "7", "response_row_position_hint"),
        )
        for failed_row, source_id, selection in cases:
            with self.subTest(failed_row=failed_row):
                state = builder.TranslationRun()
                rows = [{"id": str(i), "text": FAKE_COPY["ko"] + f" {i}"} for i in range(8)]
                rows[7] = failed_row
                content = json.dumps({"translations": rows}, ensure_ascii=False)
                with self.assertRaises(builder.TranslationError) as raised:
                    builder.parse_translation_batch(content, units, "ko")
                state.failure("ko", raised.exception, units, request_id=1, content=content)
                sample = state.data["failure_samples"][0]
                self.assertEqual(sample["failed_response_row"]["index"], 7)
                self.assertEqual(json.loads(sample["failed_response_row"]["content"]), failed_row)
                self.assertEqual([row["id"] for row in sample["source"]], [source_id])
                self.assertEqual(sample["source_selection"], selection)
                self.assertTrue(sample["translation_response"])

    def test_omitted_translation_sample_identifies_missing_source(self) -> None:
        units = [builder.TranslationUnit(str(i), "html:text:p", f"公开研究内容 {i}") for i in range(8)]
        state = builder.TranslationRun()
        content = json.dumps({"translations": [
            {"id": str(i), "text": FAKE_COPY["ko"] + f" {i}"} for i in range(7)
        ]}, ensure_ascii=False)
        with self.assertRaises(builder.TranslationError) as raised:
            builder.parse_translation_batch(content, units, "ko")
        state.failure("ko", raised.exception, units, request_id=1, content=content)
        sample = state.data["failure_samples"][0]
        self.assertEqual([row["id"] for row in sample["source"]], ["7"])
        self.assertEqual(sample["source_selection"], "omitted_translation_id")
        self.assertEqual(sample["translation_rows"], [])
        self.assertTrue(sample["translation_response"])

    def test_diagnostics_persist_when_inventory_collection_fails(self) -> None:
        diagnostics = self.temporary_root / "inventory-failure.json"
        (self.site / "index.html").unlink()
        with self.assertRaisesRegex(builder.TranslationError, "incomplete"):
            self._build(RecordingTranslator(), preflight_only=True, diagnostics_out=diagnostics)
        report = json.loads(diagnostics.read_text())
        self.assertEqual(report["status"], "failed")
        self.assertEqual(report["provider_requests"], 0)

    def test_cjk_source_echo_is_rejected(self) -> None:
        _protected, unit = builder.unit_for_text("需要翻译的完整中文文本", "test:echo")
        self.assertIsNotNone(unit)
        assert unit is not None
        response = json.dumps({
            "translations": [{"id": unit.key, "text": unit.source}],
        }, ensure_ascii=False)

        with self.assertRaisesRegex(builder.TranslationError, "(?i)unchanged source text"):
            builder.parse_translation_batch(response, [unit], "ar")

        cache = builder.empty_cache()
        cache["locales"]["ar"][unit.key] = {
            "source": unit.source,
            "translation": unit.source,
        }
        with self.assertRaisesRegex(builder.TranslationError, "(?i)unchanged source text"):
            builder.translated_text("需要翻译的完整中文文本", "test:echo", "ar", cache)

    def test_target_language_quality_gate_accepts_native_copy_and_protected_values(self) -> None:
        source = "人工智能行业研究报告正在持续增长"
        _protected, unit = builder.unit_for_text(source, "html:text:p")
        self.assertIsNotNone(unit)
        assert unit is not None
        valid = {
            "ko": "인공지능 산업 연구 보고서가 계속 성장하고 있습니다",
            "ja": "人工知能業界の調査レポートは成長を続けています",
            "ar": "يواصل تقرير أبحاث قطاع الذكاء الاصطناعي نموه",
        }
        for locale, text in valid.items():
            with self.subTest(locale=locale):
                builder.validate_translation_quality(locale, unit, text)
                parsed = builder.parse_translation_batch(
                    json.dumps({"translations": [{"id": unit.key, "text": text}]}, ensure_ascii=False),
                    [unit],
                    locale,
                )
                self.assertEqual(parsed[unit.key], text)

        # Japanese finance copy can be publication-ready entirely in Han
        # characters when its vocabulary genuinely changes from the source.
        han_source = "人工智能行业研究报告"
        _protected, han_unit = builder.unit_for_text(han_source, "catalog:title")
        self.assertIsNotNone(han_unit)
        assert han_unit is not None
        builder.validate_translation_quality("ja", han_unit, "人工知能産業調査報告")

        protected_source = "Goldman Sachs expects AAPL to gain 12% at https://example.com."
        _protected, protected_unit = builder.unit_for_text(protected_source, "catalog:title")
        self.assertIsNotNone(protected_unit)
        assert protected_unit is not None
        placeholders = " ".join(builder.PLACEHOLDER_RE.findall(protected_unit.source))
        builder.validate_translation_quality(
            "ko",
            protected_unit,
            f"Goldman Sachs는 AAPL의 상승을 전망합니다 {placeholders}",
        )

        official = builder.TranslationUnit(
            key="f" * 64,
            context="catalog:bank_name",
            source="Bank of America Global Research",
        )
        for locale in builder.LOCALES:
            with self.subTest(official_name_locale=locale):
                builder.validate_translation_quality(locale, official, official.source)
        _protected, official_unit = builder.unit_for_text(
            official.source,
            "catalog:bank_name",
        )
        _protected, prose_unit = builder.unit_for_text(
            official.source,
            "catalog:title",
        )
        self.assertIsNotNone(official_unit)
        self.assertIsNotNone(prose_unit)
        self.assertNotEqual(official_unit.key, prose_unit.key)

    def test_target_language_quality_gate_rejects_source_disguised_by_a_prefix(self) -> None:
        english = builder.TranslationUnit(
            key="e" * 64,
            context="catalog:title",
            source="Global market momentum remains strong despite higher interest rates",
        )
        chinese = builder.TranslationUnit(
            key="c" * 64,
            context="html:text:p",
            source="全球市场动能仍然强劲但利率继续上升",
        )
        rejected = (
            ("ko", english, english.source),
            ("ja", english, english.source),
            ("ar", english, english.source),
            ("ko", english, f"한국어 번역 {english.source}"),
            ("ja", chinese, f"日本語の翻訳 {chinese.source}"),
            ("ar", chinese, f"ترجمة عربية {chinese.source}"),
            ("ko", chinese, "Translated financial research content"),
            ("ja", english, "Translated financial research content"),
            ("ar", english, "Translated financial research content"),
        )
        for locale, unit, text in rejected:
            with self.subTest(locale=locale, text=text[:20]):
                with self.assertRaisesRegex(
                    builder.TranslationError,
                    "unchanged|retains|no Hangul|no Japanese|no Arabic|coverage",
                ):
                    builder.validate_translation_quality(locale, unit, text)

    def test_quality_gate_does_not_police_language_overlap_or_vocabulary(self) -> None:
        english = builder.TranslationUnit(
            key="a" * 64,
            context="catalog:title",
            source="Global markets remain strong while interest rates continue rising quickly today worldwide",
        )
        for locale, text in (
            ("ja", "世界市場展望と投資戦略"),
            ("ko", "Bank of America Global Research의 시장 전망"),
            ("ar", "توقعات السوق من Bank of America Global Research"),
        ):
            with self.subTest(locale=locale):
                builder.validate_translation_quality(locale, english, text)

    def test_quality_gate_accepts_common_han_only_japanese_labels(self) -> None:
        translations = (
            ("Chinese financial research", "中国金融研究"),
            ("Investment bank research", "投資銀行研究"),
            ("Global credit market", "世界信用市場"),
            ("机构", "機関"),
            ("确认", "確認"),
            ("美国", "米国"),
            ("半导体", "半導体"),
            ("来源", "出典"),
            ("搜索", "検索"),
            ("人工智能", "人工知能"),
            ("金融市场", "金融市場"),
            ("政府", "政府機関"),
            ("商品", "商品市場"),
            ("信用", "信用市場"),
            ("日本", "日本国"),
            ("中国", "中国"),
            ("日本", "日本"),
            ("政府", "政府"),
            ("商品", "商品"),
        )
        for index, (source, translated) in enumerate(translations):
            unit = builder.TranslationUnit(
                key=f"{index:064x}",
                context="html:text:span",
                source=source,
            )
            with self.subTest(source=source, translated=translated):
                builder.validate_translation_quality("ja", unit, translated)

    def test_official_name_passthrough_does_not_require_a_closed_vocabulary(self) -> None:
        short_generic_english = builder.TranslationUnit(
            key="e" * 64,
            context="catalog:bank_name",
            source="Global Markets",
        )
        for locale in builder.LOCALES:
            with self.subTest(short_generic_locale=locale):
                builder.validate_translation_quality(locale, short_generic_english, short_generic_english.source)

        official = builder.TranslationUnit(
            key="d" * 64,
            context="catalog:bank_name",
            source="中国工商银行股份有限公司",
        )
        for locale in builder.LOCALES:
            with self.subTest(locale=locale):
                builder.validate_translation_quality(locale, official, official.source)

        japanese_shared_han = builder.TranslationUnit(
            key="f" * 64,
            context="catalog:title",
            source="Static market research report",
        )
        builder.validate_translation_quality("ja", japanese_shared_han, "静的市場調査報告")

    def test_build_rejects_prefix_plus_source_before_reporting_complete_coverage(self) -> None:
        def disguised_source(
            locale: str,
            units: list[builder.TranslationUnit],
        ) -> dict[str, str]:
            return {unit.key: f"{FAKE_PREFIX[locale]} {unit.source}" for unit in units}

        with self.assertRaisesRegex(builder.TranslationError, "retains complete source text"):
            self._build(disguised_source)
        self.assertFalse((self.site / "data" / "i18n" / "manifest.json").exists())

    def test_translated_html_text_cannot_inject_markup(self) -> None:
        source_text = "需要翻译的完整中文文本"
        _protected, unit = builder.unit_for_text(source_text, "html:text:p")
        self.assertIsNotNone(unit)
        assert unit is not None
        cache = builder.empty_cache()
        cache["locales"]["ko"][unit.key] = {
            "source": unit.source,
            "translation": '<script data-test="injected">alert("injected")</script> 번역 및 검증이 완료되었습니다',
        }

        rendered = builder.render_localized_html(
            f'<html lang="zh-Hans"><head></head><body><p>{source_text}</p></body></html>',
            locale="ko",
            cache=cache,
            site_url=SITE_URL,
            discovery_markup="",
        )

        self.assertNotIn('<script data-test="injected">', rendered)
        self.assertIn("&lt;script data-test=\"injected\"&gt;", rendered)
        self.assertIn("번역 및 검증이 완료되었습니다", rendered)

    def test_translated_json_ld_text_cannot_close_script_element(self) -> None:
        source_text = "需要翻译的完整中文描述"
        _protected, unit = builder.unit_for_text(source_text, "jsonld:description")
        self.assertIsNotNone(unit)
        assert unit is not None
        malicious = '</script><img data-test="jsonld-injected"> 번역 결과'
        cache = builder.empty_cache()
        cache["locales"]["ko"][unit.key] = {
            "source": unit.source,
            "translation": malicious,
        }
        payload = {
            "@context": "https://schema.org",
            "@type": "WebPage",
            "description": source_text,
            "url": f"{SITE_URL}/",
        }
        source = (
            '<html lang="zh-Hans"><head><script type="application/ld+json">'
            + json.dumps(payload, ensure_ascii=False)
            + "</script></head><body></body></html>"
        )

        rendered = builder.render_localized_html(
            source,
            locale="ko",
            cache=cache,
            site_url=SITE_URL,
            discovery_markup="",
        )

        self.assertEqual(rendered.count("</script>"), 1)
        self.assertNotIn('<img data-test="jsonld-injected">', rendered)
        self.assertIn(r"\u003c/script>\u003cimg data-test=\"jsonld-injected\">", rendered)
        self.assertEqual(
            first_json_ld(rendered)["description"],
            malicious,
        )

    def test_translated_template_text_cannot_create_javascript_expression(self) -> None:
        escaped = builder.escape_javascript_literal("번역 ${globalThis.injected = true}", "`")
        self.assertEqual(escaped, "번역 \\${globalThis.injected = true}")

    @mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY_BACKUP": "backup-only"}, clear=True)
    def test_backup_only_key_configuration_passes_the_builder_precheck(self) -> None:
        unit = builder.TranslationUnit(
            key="c" * 64,
            context="test:backup-only",
            source="需要翻译的完整测试文本",
        )
        translator = RecordingTranslator()

        def translated(locale: str, units: list[builder.TranslationUnit], **_kwargs: object) -> dict[str, str]:
            return translator(locale, units)

        with mock.patch.object(builder, "deepseek_translate_batch", side_effect=translated) as request:
            missing = builder.translate_missing_units(
                {unit.key: unit},
                builder.empty_cache(),
                cache_path=self.cache,
                model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com",
                workers=3,
                timeout=1,
                attempts=1,
            )

        self.assertEqual(request.call_count, len(builder.LOCALES))
        self.assertEqual(missing, {locale: 1 for locale in builder.LOCALES})

    def test_translation_worker_count_is_clamped_to_500(self) -> None:
        unit = builder.TranslationUnit(
            key="a" * 64,
            context="test:worker-clamp",
            source="需要翻译的完整测试文本",
        )
        cache = builder.empty_cache()
        translator = RecordingTranslator()
        observed_workers: list[int] = []
        real_executor = concurrent.futures.ThreadPoolExecutor

        def recording_executor(*args: object, **kwargs: object) -> concurrent.futures.ThreadPoolExecutor:
            requested = int(kwargs.get("max_workers") or args[0])
            observed_workers.append(requested)
            return real_executor(max_workers=min(requested, 4))

        with mock.patch.object(
            builder.concurrent.futures,
            "ThreadPoolExecutor",
            side_effect=recording_executor,
        ):
            missing = builder.translate_missing_units(
                {unit.key: unit},
                cache,
                cache_path=self.cache,
                model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com",
                workers=50_000,
                timeout=1,
                attempts=1,
                batch_translator=translator,
            )

        self.assertEqual(observed_workers, [builder.MAX_TRANSLATION_WORKERS])
        self.assertEqual(missing, {locale: 1 for locale in builder.LOCALES})
        self.assertEqual({locale for locale, _keys in translator.calls}, set(builder.LOCALES))


class PreflightAttemptLimitTests(unittest.TestCase):
    def test_preflight_respects_requested_attempts_up_to_two(self) -> None:
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        with tempfile.TemporaryDirectory() as folder:
            for requested, expected in ((1, 1), (2, 2), (9, 2)):
                with self.subTest(requested=requested):
                    translator = RecordingTranslator()

                    def translate(locale: str, units: list[builder.TranslationUnit], **kwargs: object) -> dict[str, str]:
                        self.assertEqual(kwargs["attempts"], expected)
                        return translator(locale, units)

                    with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "fake-key"}, clear=True), mock.patch.object(builder, "deepseek_translate_batch", side_effect=translate) as provider:
                        builder.translate_missing_units(
                            {unit.key: unit}, builder.empty_cache(), cache_path=Path(folder) / "cache.json.gz",
                            model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                            workers=99, timeout=1, attempts=requested, preflight_only=True,
                            preflight_batches_per_locale=1, max_provider_requests=6,
                        )
                    self.assertEqual(provider.call_count, 3)


class ProviderCostGuardTests(unittest.TestCase):
    def test_output_retry_gets_validation_feedback_without_extra_request_budget(self) -> None:
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "财报摘要")
        seen = []

        def provider(_url: str, **kwargs: object) -> mock.Mock:
            seen.append(json.loads(json.dumps(kwargs["payload"])))
            text = unit.source if len(seen) == 1 else "재무 보고서 요약"
            return self.response({"prompt_tokens": 5, "completion_tokens": 5, "total_tokens": 10},
                                 json.dumps({"translations": [{"id": "0", "text": text}]}))

        state = builder.TranslationRun(max_requests=2)
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=provider)}):
            result = builder.deepseek_translate_batch(
                "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL,
                base_url="https://api.deepseek.com", timeout=1, attempts=2, run_state=state,
            )
        self.assertEqual(result[unit.key], "재무 보고서 요약")
        self.assertEqual(len(seen[0]["messages"]), 2)
        self.assertEqual(len(seen[1]["messages"]), 2)
        self.assertNotIn("response_format", seen[1])
        self.assertIn("unchanged source text for 0", seen[1]["messages"][0]["content"])
        self.assertEqual(seen[1]["messages"][1]["content"], unit.source)
        self.assertEqual(state.data["provider_requests"], 2)

    @staticmethod
    def payload(max_tokens: int = 1000) -> dict:
        return {
            "model": builder.DEFAULT_DEEPSEEK_MODEL, "thinking": {"type": "disabled"},
            "max_tokens": max_tokens, "messages": [{"role": "user", "content": "公开研究内容"}],
        }

    @staticmethod
    def response(usage: dict | None, content: str = "invalid translation JSON") -> mock.Mock:
        response = mock.Mock(status_code=200)
        response.json.return_value = {
            "usage": usage, "choices": [{"finish_reason": "stop", "message": {"content": content}}],
        }
        return response

    def test_concurrent_reservations_cannot_oversubscribe_the_run_limit(self) -> None:
        state = builder.TranslationRun(max_cost_cny="1")
        payload = self.payload(32_000)

        def reserve(_index: int) -> int | None:
            try:
                return state.reserve(payload)
            except builder.TranslationStopped:
                return None

        with concurrent.futures.ThreadPoolExecutor(max_workers=32) as executor:
            results = list(executor.map(reserve, range(500)))
        admitted = [value for value in results if value is not None]
        self.assertGreater(len(admitted), 0)
        self.assertLess(len(admitted), 500)
        self.assertEqual(len(admitted), len(set(admitted)))
        cost = state.data["cost_guard"]
        self.assertLessEqual(cost["accounted_upper_micro_cny"], 1_000_000)
        self.assertEqual(cost["accounted_upper_micro_cny"], sum(row["micro_cny"] for row in state.cost_reservations.values()))
        self.assertEqual(state.data["provider_requests"], len(admitted))

    def test_complete_usage_settles_at_peak_prices_and_releases_reservation(self) -> None:
        state = builder.TranslationRun(max_cost_cny="1")
        request_id = state.reserve(self.payload())
        state.response(request_id, "ko", self.response({
            "prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15,
            "prompt_cache_hit_tokens": 10, "prompt_cache_miss_tokens": 0,
        }))
        cost = state.data["cost_guard"]
        self.assertEqual(cost["accounted_upper_micro_cny"], 75)
        self.assertEqual(cost["settled_peak_estimate_micro_cny"], 75)
        self.assertEqual(cost["retained_reservations_micro_cny"], 0)
        self.assertEqual(state.reserve(self.payload()), 2)

    def test_partial_and_unobserved_usage_keep_the_full_fee_reservation(self) -> None:
        state = builder.TranslationRun(max_cost_cny="1")
        first = state.reserve(self.payload())
        state.reserve(self.payload())  # Simulates a dispatched request with no response.
        reserved = state.data["cost_guard"]["accounted_upper_micro_cny"]
        state.response(first, "ko", self.response({"total_tokens": 15}))
        self.assertEqual(state.data["cost_guard"]["accounted_upper_micro_cny"], reserved)
        self.assertEqual(state.data["cost_guard"]["retained_reservations_micro_cny"], reserved)
        self.assertEqual(state.data["unobserved_provider_requests"], 1)
        self.assertEqual(state.data["cost_guard"]["settled_peak_estimate_micro_cny"], 0)
        self.assertIn("not an account", state.data["cost_guard"]["assumptions"]["scope"])

    def test_unknown_model_and_thinking_are_rejected_before_paid_call(self) -> None:
        request = mock.Mock()
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            with self.assertRaisesRegex(builder.TranslationStopped, "requires deepseek-v4-flash"):
                builder.deepseek_translate_batch(
                    "ko", [unit], model="other-model", base_url="https://api.deepseek.com",
                    timeout=1, attempts=3, run_state=builder.TranslationRun(max_cost_cny="1"),
                )
        request.assert_not_called()
        with self.assertRaisesRegex(builder.TranslationStopped, "thinking disabled"):
            builder.TranslationRun(max_cost_cny="1").reserve({**self.payload(), "thinking": {"type": "enabled"}})

    def test_invalid_output_still_settles_real_usage_and_retries_reserve_again(self) -> None:
        state = builder.TranslationRun(max_requests=2, max_cost_cny="1")
        request = mock.Mock(return_value=self.response({"prompt_tokens": 10, "completion_tokens": 5, "total_tokens": 15}))
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        with mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
            with self.assertRaisesRegex(builder.TranslationError, "no Hangul"):
                builder.deepseek_translate_batch(
                    "ko", [unit], model=builder.DEFAULT_DEEPSEEK_MODEL,
                    base_url="https://api.deepseek.com", timeout=1, attempts=2, run_state=state,
                )
        self.assertEqual(request.call_count, 2)
        self.assertEqual(state.data["cost_guard"]["settled_peak_estimate_micro_cny"], 150)
        self.assertEqual(state.data["cost_guard"]["retained_reservations_micro_cny"], 0)

    def test_cost_ceiling_stops_before_http_and_saves_cache_and_diagnostics(self) -> None:
        unit = builder.TranslationUnit("a" * 64, "html:text:p", "公开研究内容")
        request = mock.Mock()
        with tempfile.TemporaryDirectory() as folder:
            cache_path = Path(folder) / "cache.json.gz"
            diagnostics = Path(folder) / "diagnostics.json"
            with mock.patch.dict("os.environ", {"DEEPSEEK_API_KEY": "fake-key"}, clear=True), mock.patch.dict(sys.modules, {"deepseek_http": mock.Mock(request_with_key_fallback=request)}):
                with self.assertRaisesRegex(builder.TranslationError, "cost estimate limit"):
                    builder.translate_missing_units(
                        {unit.key: unit}, builder.empty_cache(), cache_path=cache_path,
                        model=builder.DEFAULT_DEEPSEEK_MODEL, base_url="https://api.deepseek.com",
                        workers=4, timeout=1, attempts=3, diagnostics_out=diagnostics,
                        max_provider_cost_cny="0.000001",
                    )
            request.assert_not_called()
            self.assertTrue(cache_path.exists())
            report = json.loads(diagnostics.read_text())
            self.assertEqual(report["status"], "failed")
            self.assertEqual(report["provider_requests"], 0)
            self.assertEqual(report["cost_guard"]["accounted_upper_micro_cny"], 0)

    def test_reservation_bound_violation_stops_new_requests(self) -> None:
        state = builder.TranslationRun(max_cost_cny="1")
        request_id = state.reserve(self.payload(max_tokens=1000))
        state.response(request_id, "ko", self.response({
            "prompt_tokens": 10, "completion_tokens": 1001, "total_tokens": 1011,
        }))
        self.assertTrue(state.data["responses"][0]["cost"]["reservation_bound_exceeded"])
        with self.assertRaisesRegex(builder.TranslationStopped, "reservation assumption"):
            state.reserve(self.payload())


class MetaKeywordTranslationTests(unittest.TestCase):
    def test_mixed_keywords_translate_individually_preserving_delimiters_and_original(self) -> None:
        keywords = f"  {builder.LATIN_PUBLIC_BRAND},金融研报， Chinese financial research 、investment bank research,  ,金融研报  "
        source = f'<html lang="zh-Hans"><head><meta name="keywords" content="{keywords}"></head><body></body></html>'
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_html_units(source, units)
        translations = {
            "金融研报": "금융 리서치",
            "Chinese financial research": "중국 금융 리서치",
            "investment bank research": "투자은행 리서치",
        }
        self.assertEqual({unit.source for unit in units.values()}, set(translations))
        self.assertEqual({unit.context for unit in units.values()}, {"html:meta:keyword"})
        self.assertEqual(len(units), 3, "duplicate keywords share the same cache unit")
        cache = builder.empty_cache()
        cache["locales"]["ko"] = {
            unit.key: {"source": unit.source, "translation": translations[unit.source]}
            for unit in units.values()
        }
        with tempfile.TemporaryDirectory() as folder:
            original = Path(folder) / "index.html"
            original.write_text(source, encoding="utf-8")
            before = original.read_bytes()
            localized = builder.render_localized_html(
                original.read_text(encoding="utf-8"), locale="ko", cache=cache,
                site_url=SITE_URL, discovery_markup="",
            )
            self.assertEqual(original.read_bytes(), before)
        expected = f"  {builder.LATIN_PUBLIC_BRAND},금융 리서치， 중국 금융 리서치 、투자은행 리서치,  ,금융 리서치  "
        self.assertIn(f'content="{expected}"', localized)
        self.assertNotIn("Chinese financial research", localized)
        self.assertNotIn("investment bank research", localized)

    def test_keyword_cache_deduplicates_across_pages_but_other_meta_is_not_split(self) -> None:
        units: dict[str, builder.TranslationUnit] = {}
        for keywords in ("金融研报,Chinese financial research", " Chinese financial research 、 金融研报 "):
            builder.collect_html_units(f'<meta name="keywords" content="{keywords}">', units)
        self.assertEqual(len(units), 2)
        prior_keys = set(units)
        builder.collect_html_units('<meta name="description" content="金融研报,Chinese financial research">', units)
        added = [unit for key, unit in units.items() if key not in prior_keys]
        self.assertEqual(len(added), 1)
        self.assertEqual(added[0].source, "金融研报,Chinese financial research")
        self.assertEqual(added[0].context, "html:meta:description")
        parser = builder.PortalHTMLProcessor(units={})
        self.assertEqual(parser.process_text(" ,， 、 ", "html:meta:keywords"), " ,， 、 ")
        self.assertEqual(parser.units, {})

    def test_untranslated_english_keyword_is_rejected_independently(self) -> None:
        source = '<meta name="keywords" content="金融研报,Chinese financial research,investment bank research">'
        units: dict[str, builder.TranslationUnit] = {}
        builder.collect_html_units(source, units)
        cache = builder.empty_cache()
        for unit in units.values():
            cache["locales"]["ko"][unit.key] = {
                "source": unit.source,
                "translation": "금융 리서치" if unit.source == "金融研报" else unit.source,
            }
        with self.assertRaisesRegex(builder.TranslationError, "unchanged source text"):
            builder.render_localized_html(
                source, locale="ko", cache=cache, site_url=SITE_URL, discovery_markup="",
            )
        english = next(unit for unit in units.values() if unit.source == "Chinese financial research")
        with self.assertRaisesRegex(builder.TranslationError, "unchanged source text"):
            builder.parse_translation_batch(json.dumps({
                "translations": [{"id": english.key, "text": english.source}],
            }), [english], "ko")


if __name__ == "__main__":
    unittest.main()
