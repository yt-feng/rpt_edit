#!/usr/bin/env python3
"""Offline publication tests for new-content-only locale releases."""
from __future__ import annotations

import copy
from dataclasses import replace
import gzip
import json
from pathlib import Path
import unittest
from unittest import mock

import build_portal_locales as builder
import test_build_portal_locales as fixtures
import verify_portal_chinese_parity as parity
from repair_portal_ja_catalog_titles import load_repairs
from verify_portal_locale_routes import verify_locale_routes


class IncrementalBuildTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.PortalLocaleBuildTests()
        self.fixture.setUp()
        self.site = self.fixture.site
        self.write_page("reports/report-ai-1.html", "历史报告不应购买正文", "2026-09-06")
        self.write_page("blog/old.html", "历史文章不应购买正文", "2026-09-04")
        self.write_page("blog/undated.html", "无日期文章不应购买正文")
        self.write_page("research/dated.html", "其他内容类型不应购买正文", "2026-09-06")
        self.write_page("blog/new.html", "新增第五日文章正文", "2026-09-05")
        self.write_page("blog/legacy-hash.html", "旧网址不应购买正文", "2026-09-05",
                        canonical="/blog/new.html", noindex=True)
        self.write_page("charts.html", "图表检索界面")
        self.write_page("account.html", "账户登录界面", noindex=True)
        self.write_page("reports/page-17.html", "旧翻页标题不应购买", links=("/reports/report-ai-1.html",))
        self.write_page("blog/page-2.html", "旧文章翻页不应购买", links=("/blog/old.html",))
        self.add_report("report-new-5", "260905", "新增第五日报告正文")
        detail_links = ("/reports/report-ai-1.html", "/reports/report-new-5.html",
                        "/blog/old.html", "/blog/new.html", "/blog/legacy-hash.html")
        for relative in ("reports/index.html", "blog/index.html"):
            self.write_page(relative, "最新内容目录", links=detail_links)
        self.write_page("reports/topics/new/index.html", "新增报告主题", links=("/reports/report-new-5.html",))
        root = self.site / "index.html"
        root.write_text(root.read_text().replace("</main>",
            ''.join(f'<a href="{href}">目录链接</a>' for href in (*detail_links, "/reports/page-17.html", "/account.html")) + "</main>"))
        discovery_links = [fixtures.SITE_URL + href for href in detail_links]
        self.site.joinpath("feed.xml").write_text(
            '<rss version="2.0"><channel><title>最新文章</title><link>' + fixtures.SITE_URL + '</link>'
            + ''.join(f'<item><title>条目</title><link>{url}</link><guid>{url}</guid></item>' for url in discovery_links)
            + '</channel></rss>')
        self.site.joinpath("llms.txt").write_text("# 公开研究\n" + ''.join(f'- 研究：{url}\n' for url in discovery_links))
        self.site.joinpath("llms-full.txt").write_text("# 公开研究\n" + ''.join(f'## 研究\n{url}\n' for url in discovery_links))
        for name in ("sitemap-baidu.xml", "sitemap-sogou.xml"):
            self.site.joinpath(name).write_bytes(self.site.joinpath("sitemap-pages.xml").read_bytes())
        # Use the same protected Chinese cluster contract as production.
        for path in self.site.rglob("*.html"):
            source = path.read_text()
            canonical = builder.extract_canonical(source)
            if canonical and builder.is_indexable_html(source) and 'hreflang="zh-Hans"' not in source:
                source = source.replace("</head>", ''.join(
                    f'<link rel="alternate" hreflang="{locale}" href="{canonical}">'
                    for locale in ("zh-Hans", "x-default")) + "</head>")
                path.write_text(source)

    def tearDown(self):
        self.fixture.tearDown()

    def write_page(self, relative, title, published=None, *, canonical=None, noindex=False, links=()):
        if canonical is None:
            canonical = "/" + relative.removesuffix("index.html") if relative.endswith("/index.html") else "/" + relative
        canonical = fixtures.SITE_URL + canonical
        entity = {"@type": "Report" if relative.startswith("reports/") else "BlogPosting", "url": canonical, "name": title}
        if published:
            entity["datePublished"] = published
        source = (
            '<html lang="zh-Hans"><head><meta name="robots" content="' + ("noindex" if noindex else "index") + ',follow">'
            f'<link rel="canonical" href="{canonical}"><title>{title}</title>'
            '<script type="application/ld+json">' + json.dumps(entity, ensure_ascii=False) + '</script></head><body>'
            f'<main><h1>{title}</h1><p>{title}的完整内容。</p><ul>'
            + ''.join(f'<li><a href="{href}">相关研究链接</a></li>' for href in links)
            + '</ul></main></body></html>'
        )
        target = self.site / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(source)

    def add_report(self, report_id, catalog_date, title):
        # Catalog date is authoritative for scheduling even without datePublished.
        self.write_page(f"reports/{report_id}.html", title)
        for filename in builder.CATALOG_PUBLIC_SOURCES.values():
            path = self.site / "data" / filename
            payload = json.loads(path.read_text())
            item = {**payload["items"][0], "id": report_id, "title": title, "date_folder": catalog_date}
            payload["items"].append(item)
            payload["item_count"] = len(payload["items"])
            path.write_text(json.dumps(payload, ensure_ascii=False))
        detail = self.site / "data/report_details/re.json"
        payload = json.loads(detail.read_text())
        payload["reports"][report_id] = {"item": item, "related": [payload["reports"]["report-ai-1"]["item"]]}
        detail.write_text(json.dumps(payload, ensure_ascii=False))
        chart = self.site / "data/chart_search_index.json"
        payload = json.loads(chart.read_text())
        report = copy.deepcopy(payload["reports"][0])
        report.update(report_id=report_id, report_ref=report_id + "-ref", title=title, date_folder=catalog_date)
        report["charts"][0]["id"] = report_id + "-chart"
        report["charts"][0]["title"] = title + "图表"
        payload["reports"].append(report)
        chart.write_text(json.dumps(payload, ensure_ascii=False))

    def build(self, translator, **kwargs):
        kwargs.setdefault("index_start_date", "2026-09-05")
        return self.fixture._build(translator, translation_scope="incremental", **kwargs)

    def test_emits_only_new_details_and_useful_hubs_without_history_or_placeholders(self):
        translator = fixtures.RecordingTranslator()
        manifest = self.build(translator)
        included = {"index.html", "reports/index.html", "blog/index.html", "charts.html", "account.html",
                    "reports/topics/new/index.html", "reports/report-new-5.html", "blog/new.html"}
        for locale in builder.LOCALES:
            actual = {path.relative_to(self.site / locale).as_posix() for path in (self.site / locale).rglob("*.html")}
            self.assertEqual(actual, included)
            for path in (self.site / locale).rglob("*.html"):
                self.assertNotIn('data-kc-locale-deferred="true"', path.read_text())
            self.assertIn('content="noindex,follow"', (self.site / locale / "account.html").read_text())
        self.assertEqual(manifest["translation_scope"], "incremental")
        self.assertEqual(manifest["html_page_count"], len(included))
        self.assertEqual(manifest["omitted_html_page_count"], manifest["source_html_page_count"] - len(included))
        self.assertEqual(manifest["deferred_index_page_count"], 0)
        self.assertEqual(manifest["index_policy"]["history_release_count"], 0)
        self.assertNotIn("history_release", manifest["index_policy"])
        self.assertFalse((self.site / "data/i18n/history-release.json").exists())
        paid = "\n".join(translator.sources)
        self.assertIn("新增第五日报告正文", paid)
        self.assertIn("新增第五日文章正文", paid)
        for label in ("历史报告不应购买正文", "历史文章不应购买正文", "无日期文章不应购买正文", "旧网址不应购买正文", "旧翻页标题不应购买", "旧文章翻页不应购买"):
            self.assertNotIn(label, paid)

    def test_all_links_discovery_and_data_use_the_published_cohort(self):
        self.build(fixtures.RecordingTranslator())
        excluded = ("/reports/report-ai-1.html", "/blog/old.html", "/blog/legacy-hash.html", "/reports/page-17.html")
        for locale in builder.LOCALES:
            for path in (self.site / locale).rglob("*.html"):
                source = path.read_text()
                for relative in excluded:
                    self.assertNotIn(f"/{locale}{relative}", source, path)
            home = (self.site / locale / "index.html").read_text()
            self.assertIn(f"/{locale}/account.html", home)
            self.assertNotIn(f"/{locale}/reports/topics/ai/", home)
            for path in (self.site / f"sitemap-{locale}.xml", self.site / locale / "feed.xml", self.site / locale / "llms.txt", self.site / locale / "llms-full.txt"):
                source = path.read_text()
                for relative in excluded:
                    self.assertNotIn(relative, source, path)
                self.assertIn(f"/{locale}/blog/new.html", source, path)
            for filename in builder.CATALOG_OVERLAY_FILES.values():
                overlay = json.loads((self.site / f"data/i18n/{locale}/{filename}").read_text())
                self.assertEqual({row[0] for row in overlay["rows"]}, {"report-new-5"})
                self.assertTrue(overlay["scoped"])
            detail = json.loads((self.site / f"data/i18n/{locale}/catalog-detail-re.json").read_text())
            self.assertEqual({row[0] for row in detail["rows"]}, {"report-new-5"})
            chart = json.loads((self.site / f"data/i18n/{locale}/{builder.CHART_OVERLAY_FILE}").read_text())
            self.assertEqual(chart["report_count"], 1)
            self.assertTrue(chart["scoped"])
            hot = json.loads((self.site / f"data/i18n/{locale}/{builder.HOT_REPORT_OVERLAY_FILE}").read_text())
            self.assertEqual(hot["item_count"], 0)
            self.assertTrue(hot["scoped"])
        for relative in ("reports/report-ai-1.html", "blog/old.html", "reports/page-17.html"):
            self.assertNotIn("ko", fixtures.alternate_links((self.site / relative).read_text()))

    def test_real_uncanonicalized_application_shells_survive_incremental_publication(self):
        template_root = Path(builder.__file__).resolve().parents[1] / "portal_suite/site_src"
        originals = {}
        for name in builder.LOCALE_APPLICATION_SHELLS:
            template = template_root / name
            self.assertTrue(template.is_file(), name)
            originals[name] = template.read_text()
            self.site.joinpath(name).write_text(originals[name])
        self.assertIn("report.html", originals)
        self.assertEqual(builder.extract_canonical(originals["report.html"]), "")
        detail = self.site / "reports/report-new-5.html"
        detail.write_text(detail.read_text().replace("</main>", '<a href="/report.html?id=report-new-5">打开报告</a></main>'))
        manifest = self.build(fixtures.RecordingTranslator())
        for locale in builder.LOCALES:
            for name in originals:
                with self.subTest(locale=locale, shell=name):
                    source = self.site.joinpath(locale, name).read_text()
                    self.assertIn('content="noindex,follow"', source)
                    self.assertIn("data-kc-locale-help", source)
                    self.assertIn("data-kc-chinese-equivalent", source)
                    self.assertIn("mailto:info@kcdesk.com", source)
                    self.assertIn("/assets/locale-recovery.js", source)
                    self.assertEqual(source.count("<script data-kc-locale-early>"), 1)
                    self.assertLess(source.index("<script data-kc-locale-early>"), source.index('<script defer src="/assets/locale-recovery.js'))
                    self.assertLess(source.index("<script data-kc-locale-early>"), source.index('<script src="/assets/locale-runtime.js'))
                    self.assertLess(source.index("<script data-kc-locale-early>"), source.index("assets/app.js"))
                    self.assertEqual(manifest["application_routes"][locale][name]["path"], f"{locale}/{name}")
                    self.assertNotIn(f"/{locale}/{name}", self.site.joinpath(f"sitemap-{locale}.xml").read_text())
            self.assertIn(f'/{locale}/report.html?id=report-new-5', self.site.joinpath(locale, "reports/report-new-5.html").read_text())
        for name, original in originals.items():
            current = self.site.joinpath(name).read_text()
            self.assertEqual(current[current.index("<body"):], original[original.index("<body"):])
            self.assertNotIn("locale-runtime.js", current)
            self.assertNotIn("locale-recovery.js", current)
            self.assertNotIn("data-kc-locale-early", current)
            self.assertNotIn("PortalLocaleEarly", current)
        self.assertTrue(self.site.joinpath("assets/locale-recovery.js").is_file())
        def generated_response(url, timeout):
            relative = url.removeprefix(fixtures.SITE_URL + "/")
            return 200, {"content-language": relative.split("/", 1)[0]}, self.site.joinpath(relative).read_bytes()
        report = verify_locale_routes(manifest, fixtures.SITE_URL, fetcher=generated_response)
        self.assertEqual(report["status"], "passed", report)
        self.assertEqual(report["request_count"], 16)

    def test_next_day_keeps_fixed_cutoff_reuses_paid_cache_and_preserves_chinese(self):
        snapshot = self.fixture.temporary_root / "chinese-before.json"
        snapshot.write_text(json.dumps(parity.create_snapshot(root=self.site, site_origin=fixtures.SITE_URL)))
        self.build(fixtures.RecordingTranslator())
        parity.verify_snapshot(root=self.site, snapshot_path=snapshot)
        with gzip.open(self.fixture.cache, "rt") as handle:
            cache = json.load(handle)
        prepaid = {"source": "此前已经购买的历史内容", "translation": "previously paid text"}
        for locale in builder.LOCALES:
            cache["locales"][locale]["f" * 64] = prepaid
        builder.write_cache(self.fixture.cache, cache)
        self.add_report("report-new-6", "20260906", "新增第六日报告正文")
        self.write_page("blog/new-six.html", "新增第六日文章正文", "2026-09-06")
        translator = fixtures.RecordingTranslator()
        manifest = self.build(translator, cache_in=self.fixture.cache)
        self.assertEqual(manifest["index_policy"]["index_start_date"], "2026-09-05")
        paid = "\n".join(translator.sources)
        self.assertIn("新增第六日报告正文", paid)
        self.assertIn("新增第六日文章正文", paid)
        self.assertNotIn("新增第五日报告正文", paid)
        self.assertNotIn("新增第五日文章正文", paid)
        with gzip.open(self.fixture.cache, "rt") as handle:
            preserved = json.load(handle)
        for locale in builder.LOCALES:
            self.assertEqual(preserved["locales"][locale]["f" * 64], prepaid)
            for relative in ("blog/new.html", "blog/new-six.html", "reports/report-new-5.html", "reports/report-new-6.html"):
                self.assertTrue((self.site / locale / relative).exists())
            self.assertFalse((self.site / locale / "blog/old.html").exists())
        again = fixtures.RecordingTranslator()
        self.build(again, cache_in=self.fixture.cache)
        self.assertEqual(again.calls, [])
        for locale in builder.LOCALES:
            for relative in ("blog/new.html", "blog/new-six.html", "reports/report-new-5.html", "reports/report-new-6.html"):
                source = self.site.joinpath(locale, relative).read_text()
                self.assertEqual(source.count("<script data-kc-locale-early>"), 1)

    def test_cutoff_and_no_history_contract_fail_before_translation(self):
        for kwargs in ({"index_start_date": None}, {"history_start_date": "2026-08-05"},
                       {"history_state_in": Path("missing-ledger.json")}, {"index_allowlist": ("/blog/old.html",)}):
            with self.subTest(kwargs=kwargs):
                translator = fixtures.RecordingTranslator()
                with self.assertRaises(builder.TranslationError):
                    self.build(translator, **kwargs)
                self.assertEqual(translator.calls, [])

    def test_reviewed_japanese_title_repair_is_free_and_preserves_other_locales(self):
        repair = load_repairs()[0]
        report_id = "report-title-repair"  # Fixture detail records belong to shard re.json.
        self.add_report(report_id, "260905", repair["source_title"])
        self.build(fixtures.RecordingTranslator())
        cache = builder.load_cache(self.fixture.cache)
        self.assertIn(repair["unit_key"], cache["locales"]["ja"])
        cache["locales"]["ja"][repair["unit_key"]]["translation"] = repair["observed_translations"][0]
        builder.write_cache(self.fixture.cache, cache)
        protected = {
            self.site / f"{locale}/reports/{report_id}.html": fixtures.body_bytes(self.site / f"{locale}/reports/{report_id}.html")
            for locale in ("ko", "ar")
        }
        chinese = self.site / f"reports/{report_id}.html"
        protected[chinese] = fixtures.body_bytes(chinese)
        translator = fixtures.RecordingTranslator()
        self.build(translator, cache_in=self.fixture.cache)
        self.assertEqual(translator.calls, [])
        corrected = builder.load_cache(self.fixture.cache)
        self.assertEqual(corrected["locales"]["ja"][repair["unit_key"]]["translation"], repair["translation"])
        for locale in ("ko", "ar"):
            self.assertEqual(corrected["locales"][locale], cache["locales"][locale])
        for path, original in protected.items():
            self.assertEqual(fixtures.body_bytes(path), original)
        overlay = json.loads((self.site / "data/i18n/ja/catalog-titles.json").read_text())
        rows = [dict(zip(["id", *overlay["fields"]], row)) for row in overlay["rows"]]
        translated = next(row for row in rows if row["id"] == report_id)
        self.assertEqual(translated["title"], repair["translation_title"])
        self.assertIn(repair["translation_title"], (self.site / f"ja/reports/{report_id}.html").read_text())

    def test_switching_from_history_removes_old_artifacts_and_keeps_paid_cache(self):
        self.fixture._build(fixtures.RecordingTranslator(), index_start_date="2026-09-05",
                            history_start_date="2026-08-05", history_release_date="2026-09-05",
                            history_daily_limit=1, translation_scope="month")
        ledger = self.site / "data/i18n/history-release.json"
        self.assertTrue(ledger.exists())
        self.assertTrue((self.site / "ko/blog/undated.html").exists())
        with gzip.open(self.fixture.cache, "rt") as handle:
            prepaid = json.load(handle)
        old_keys = {key for key, row in prepaid["locales"]["ko"].items()
                    if "历史报告不应购买正文" in row["source"]}
        self.assertTrue(old_keys)
        self.build(fixtures.RecordingTranslator(), cache_in=self.fixture.cache)
        self.assertFalse(ledger.exists())
        self.assertFalse((self.site / "ko/blog/undated.html").exists())
        self.assertFalse((self.site / "ko/blog/old.html").exists())
        with gzip.open(self.fixture.cache, "rt") as handle:
            after = json.load(handle)
        for locale in builder.LOCALES:
            for key in old_keys:
                self.assertEqual(after["locales"][locale][key], prepaid["locales"][locale][key])

    def test_report_publication_fallback_never_promotes_source_noindex(self):
        path = self.site / "data/catalog.json"
        payload = json.loads(path.read_text())
        payload["items"][0]["date_folder"] = "2026-02-31"
        path.write_text(json.dumps(payload, ensure_ascii=False))
        self.build(fixtures.RecordingTranslator())
        self.assertTrue((self.site / "ko/reports/report-ai-1.html").exists())
        source = self.site / "reports/report-ai-1.html"
        source.write_text(source.read_text().replace('content="index,follow"', 'content="noindex,follow"'))
        self.build(fixtures.RecordingTranslator(), cache_in=self.fixture.cache)
        self.assertFalse((self.site / "ko/reports/report-ai-1.html").exists())

    def test_out_of_scope_dated_entity_cannot_advertise_an_omitted_locale_page(self):
        # Even if the general index planner adds another detail type later,
        # incremental rendering and discovery must agree on this MVP cohort.
        original_plan = builder.build_locale_index_plan
        generic = (self.site / "research/dated.html").resolve()
        def dated_plan(*args, **kwargs):
            plan = original_plan(*args, **kwargs)
            plan[generic] = replace(plan[generic], indexable=True, force_noindex_follow=False)
            return plan
        with mock.patch.object(builder, "build_locale_index_plan", side_effect=dated_plan):
            self.build(fixtures.RecordingTranslator())
        self.assertNotIn("ko", fixtures.alternate_links(generic.read_text()))
        for locale in builder.LOCALES:
            self.assertFalse((self.site / locale / "research/dated.html").exists())
            self.assertNotIn("/research/dated.html", (self.site / f"sitemap-{locale}.xml").read_text())

    def test_cli_accepts_incremental(self):
        with mock.patch("sys.argv", ["build_portal_locales.py", "--root", "/tmp/site", "--site-url", fixtures.SITE_URL,
                                    "--cache-out", "/tmp/cache", "--hot-report-index", "/tmp/hot", "--translation-scope", "incremental"]):
            self.assertEqual(builder.parse_args().translation_scope, "incremental")


if __name__ == "__main__":
    unittest.main()
