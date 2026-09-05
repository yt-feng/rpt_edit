#!/usr/bin/env python3
"""No-provider end-to-end regressions for bounded history localization."""
from __future__ import annotations

import gzip
import json
from pathlib import Path
import unittest

import test_build_portal_locales as fixtures
import build_portal_locales as builder


class HistoryBuildTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.PortalLocaleBuildTests()
        self.fixture.setUp()
        self.site = self.fixture.site
        self.sources = {}
        for relative, published, title in (
            ("reports/report-ai-1.html", "2026-09-04", "月内研究资产报告"),
            ("blog/history-a.html", "2026-09-03", "月内深入研究文章甲"),
            ("blog/history-b.html", "2026-09-02", "月内深入研究文章乙"),
            ("blog/old.html", "2026-08-04", "月外禁止付费旧文章"),
            ("blog/new.html", "2026-09-05", "上线以后新增研究文章"),
        ):
            canonical = fixtures.SITE_URL + "/" + relative
            kind = "Report" if relative.startswith("reports/") else "BlogPosting"
            source = (
                '<html lang="zh-Hans"><head><meta name="robots" content="index,follow">'
                f'<link rel="canonical" href="{canonical}"><title>{title}</title>'
                '<script type="application/ld+json">' + json.dumps({
                    "@type": kind, "url": canonical, "datePublished": published, "name": title,
                }, ensure_ascii=False) + '</script></head><body>'
                f'<h1>{title}</h1><p>{title}的完整正文内容。</p></body></html>'
            )
            target = self.site / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(source)
            self.sources[canonical] = title
        self.protected = {str(path.relative_to(self.site)): fixtures.body_bytes(path) for path in self.site.rglob("*.html") if b"<body" in path.read_bytes()}
        self.app_bytes = (self.site / "assets/app.js").read_bytes()
        self.ledger = self.fixture.temporary_root / "active-history.json"

    def tearDown(self):
        self.fixture.tearDown()

    def build(self, translator, today="2026-09-05", previous=False, **kwargs):
        return self.fixture._build(
            translator, index_start_date="2026-09-05", history_start_date="2026-08-05",
            history_release_date=today, history_daily_limit=1,
            history_state_in=self.ledger if previous else None, **kwargs,
        )

    def activate_fixture_ledger(self):
        self.ledger.write_bytes((self.site / "data/i18n/history-release.json").read_bytes())
        return json.loads(self.ledger.read_text())

    def set_report_dates(self, catalog_date, publication_date=None, noindex=False):
        for filename in builder.CATALOG_PUBLIC_SOURCES.values():
            path = self.site / "data" / filename
            payload = json.loads(path.read_text())
            for item in payload["items"]:
                if item["id"] == "report-ai-1":
                    item["date_folder"] = catalog_date
            path.write_text(json.dumps(payload, ensure_ascii=False))
        path = self.site / "reports/report-ai-1.html"
        source = path.read_text()
        source = source.replace(', "datePublished": "2026-09-04"', "")
        if publication_date:
            source = source.replace('"@type": "Report"', f'"@type": "Report", "datePublished": "{publication_date}"')
        if noindex:
            source = source.replace('content="index,follow"', 'content="noindex,follow"')
        path.write_text(source)
        return path, source

    def test_recent_catalog_report_without_publication_date_is_pretranslated(self):
        path, source = self.set_report_dates("260904")
        translator = fixtures.RecordingTranslator()
        self.build(translator)
        self.assertIn("月内研究资产报告", "\n".join(translator.sources))
        ledger = self.activate_fixture_ledger()
        self.assertEqual(ledger["pending_count"], 2)
        self.assertNotIn("datePublished", path.read_text())
        self.assertEqual(fixtures.body_bytes(path), source[source.index("<body>"):].encode())
        # With this one-page test quota, two blog rows precede the report.
        reuse = fixtures.RecordingTranslator()
        self.build(reuse, today="2026-09-06", previous=True, cache_in=self.fixture.cache)
        self.activate_fixture_ledger()
        self.build(reuse, today="2026-09-07", previous=True, cache_in=self.fixture.cache)
        self.assertEqual(reuse.calls, [])
        for locale in ("ko", "ja", "ar"):
            page = (self.site / locale / "reports/report-ai-1.html").read_text()
            self.assertNotIn('data-kc-locale-deferred="true"', page)
            self.assertNotIn("datePublished", page)

    def test_catalog_date_controls_schedule_without_rewriting_real_publication(self):
        path, _source = self.set_report_dates("20260905", "2025-01-02")
        self.build(fixtures.RecordingTranslator())
        self.assertIn('"datePublished": "2025-01-02"', path.read_text())
        for locale in ("ko", "ja", "ar"):
            page = (self.site / locale / "reports/report-ai-1.html").read_text()
            self.assertNotIn('content="noindex,follow"', page)
            self.assertIn("2025-01-02", page)
            self.assertNotIn('data-kc-locale-deferred="true"', page)

    def test_missing_catalog_date_falls_back_to_genuine_publication(self):
        self.set_report_dates("2026-02-31", "2026-09-05")
        self.build(fixtures.RecordingTranslator())
        self.assertNotIn('content="noindex,follow"', (self.site / "ko/reports/report-ai-1.html").read_text())

    def test_recent_catalog_never_promotes_source_noindex(self):
        self.set_report_dates("2026-09-05", noindex=True)
        translator = fixtures.RecordingTranslator()
        self.build(translator)
        for locale in ("ko", "ja", "ar"):
            self.assertIn('content="noindex,follow"', (self.site / locale / "reports/report-ai-1.html").read_text())
            self.assertNotIn(f"/{locale}/reports/report-ai-1.html", (self.site / f"sitemap-{locale}.xml").read_text())

    def test_old_catalog_date_does_not_spend_even_with_new_publication_date(self):
        self.set_report_dates("2026-08-04", "2026-09-05")
        translator = fixtures.RecordingTranslator()
        self.build(translator)
        self.assertNotIn("月内研究资产报告", "\n".join(translator.sources))
        self.assertIn('data-kc-locale-deferred="true"', (self.site / "ko/reports/report-ai-1.html").read_text())

    def test_catalog_date_parser_is_strict(self):
        for text in ("260904", "20260904", "2026-09-04"):
            self.assertEqual(builder.parse_catalog_schedule_date(text).isoformat(), "2026-09-04")
        for text in (None, "", "2026-02-31", "260231", "on 2026-09-04", "2026-09-04/other", "99999999"):
            self.assertIsNone(builder.parse_catalog_schedule_date(text))

    def test_entire_month_prepaid_but_only_selected_history_and_new_content_indexed(self):
        translator = fixtures.RecordingTranslator()
        manifest = self.build(translator)
        ledger = self.activate_fixture_ledger()
        self.assertEqual(len(ledger["released"]), 1)
        self.assertEqual(ledger["pending_count"], 2)
        self.assertEqual(manifest["index_policy"]["history_release"]["released_count"], 1)
        all_paid = "\n".join(translator.sources)
        for canonical, title in self.sources.items():
            selected = canonical in ledger["released"] or canonical.endswith("/blog/new.html")
            self.assertEqual(title in all_paid, not canonical.endswith("/blog/old.html"), canonical)
            relative = canonical.removeprefix(fixtures.SITE_URL + "/")
            for locale in ("ko", "ja", "ar"):
                page = (self.site / locale / relative).read_text()
                self.assertEqual('content="noindex,follow"' in page, not selected)
                sitemap = (self.site / f"sitemap-{locale}.xml").read_text()
                self.assertEqual(f"{fixtures.SITE_URL}/{locale}/{relative}" in sitemap, selected)
                self.assertNotIn(title, page)
        for relative, original_body in self.protected.items():
            self.assertEqual(fixtures.body_bytes(self.site / relative), original_body)
        self.assertEqual((self.site / "assets/app.js").read_bytes(), self.app_bytes)
        for locale in ("ko", "ja", "ar"):
            overlay = json.loads((self.site / f"data/i18n/{locale}/catalog-titles.json").read_text())
            self.assertTrue(overlay["scoped"])

    def test_same_day_reuses_cache_tomorrow_releases_one_and_keeps_old_pages(self):
        self.build(fixtures.RecordingTranslator())
        first = self.activate_fixture_ledger()
        translator = fixtures.RecordingTranslator()
        self.build(translator, previous=True, cache_in=self.fixture.cache)
        self.assertEqual(translator.calls, [])
        repeated = self.activate_fixture_ledger()
        self.assertEqual(repeated["released"], first["released"])
        next_day = fixtures.RecordingTranslator()
        self.build(next_day, today="2026-09-09", previous=True, cache_in=self.fixture.cache)
        self.assertEqual(next_day.calls, [])
        later = self.activate_fixture_ledger()
        self.assertEqual(len(later["released"]), 2)
        self.assertTrue(set(first["released"]).issubset(later["released"]))

    def test_pause_does_not_spend_on_pending_history_or_evict_released(self):
        self.build(fixtures.RecordingTranslator())
        previous = self.activate_fixture_ledger()
        translator = fixtures.RecordingTranslator()
        self.build(translator, today="2026-09-06", previous=True, cache_in=self.fixture.cache, history_paused=True)
        self.assertEqual(translator.calls, [])
        paused = self.activate_fixture_ledger()
        self.assertEqual(previous["released"], paused["released"])
        self.assertEqual(previous["last_release_date"], paused["last_release_date"])

    def test_malformed_ledger_stops_before_provider_calls(self):
        self.ledger.write_text('{"schema_version": 999}')
        translator = fixtures.RecordingTranslator()
        with self.assertRaises(ValueError):
            self.build(translator, previous=True)
        self.assertEqual(translator.calls, [])

    def test_prepaid_cache_outside_current_release_is_not_discarded(self):
        self.build(fixtures.RecordingTranslator())
        self.activate_fixture_ledger()
        with gzip.open(self.fixture.cache, "rt", encoding="utf-8") as handle:
            cache = json.load(handle)
        for locale in ("ko", "ja", "ar"):
            cache["locales"][locale]["f" * 64] = {
                "source": "此前已经付费的旧档案内容", "translation": "previously cached public text",
            }
        builder.write_cache(self.fixture.cache, cache)
        translator = fixtures.RecordingTranslator()
        self.build(translator, previous=True, cache_in=self.fixture.cache)
        with gzip.open(self.fixture.cache, "rt", encoding="utf-8") as handle:
            preserved = json.load(handle)
        for locale in ("ko", "ja", "ar"):
            self.assertEqual(preserved["locales"][locale]["f" * 64], cache["locales"][locale]["f" * 64])
        self.assertEqual(translator.calls, [])

    def test_failed_candidate_cannot_advance_active_ledger(self):
        self.build(fixtures.RecordingTranslator())
        self.activate_fixture_ledger()
        previous_bytes = self.ledger.read_bytes()
        # A changed source is the only thing requiring another paid call.
        with (self.site / "blog/new.html").open("a") as handle:
            handle.write("<p>刚刚新增尚未缓存的真实正文。</p>")
        def fail(_locale, _units):
            raise builder.TranslationError("offline intentional translation failure")
        with self.assertRaises(builder.TranslationError):
            self.build(fail, today="2026-09-06", previous=True, cache_in=self.fixture.cache)
        self.assertEqual(self.ledger.read_bytes(), previous_bytes)


if __name__ == "__main__":
    unittest.main()
