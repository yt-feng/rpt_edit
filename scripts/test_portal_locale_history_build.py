#!/usr/bin/env python3
"""No-provider end-to-end regressions for bounded history localization."""
from __future__ import annotations

import gzip
import copy
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
        # Existing prepaid-month regressions remain explicit opt-in coverage.
        kwargs.setdefault("translation_scope", "month")
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

    def test_released_history_does_not_promote_same_canonical_legacy_redirect(self):
        import build_portal_suite_site as site_builder
        import verify_portal_chinese_parity as parity

        # The real canonical article has protected Chinese discovery; its old
        # hash slug is a noindex refresh alias with no hreflang cluster.
        for path in self.site.rglob("*.html"):
            source = path.read_text()
            canonical = builder.extract_canonical(source)
            if canonical and 'hreflang="zh-Hans"' not in source:
                links = "".join(
                    f'<link rel="alternate" hreflang="{language}" href="{canonical}">'
                    for language in ("zh-Hans", "x-default")
                )
                path.write_text(source.replace("</head>", links + "</head>"))
        alias = self.site / "blog/history-old-hash.html"
        original = site_builder.render_blog_legacy_redirect({"slug": "history-a"}, fixtures.SITE_URL)
        alias.write_text(original)
        for name in ("sitemap-baidu.xml", "sitemap-sogou.xml"):
            (self.site / name).write_bytes((self.site / "sitemap-pages.xml").read_bytes())
        snapshot = self.fixture.temporary_root / "legacy-redirect-before.json"
        snapshot.write_text(json.dumps(parity.create_snapshot(root=self.site, site_origin=fixtures.SITE_URL)))

        self.build(fixtures.RecordingTranslator(), translation_scope="release")
        canonical = fixtures.SITE_URL + "/blog/history-a.html"
        ledger = self.activate_fixture_ledger()
        self.assertEqual(ledger["released"], [canonical])
        self.assertNotIn("history-old-hash", json.dumps(ledger))
        self.assertEqual(fixtures.body_bytes(alias), original[original.index("<body>"):].encode())
        self.assertEqual(fixtures.alternate_links(alias.read_text()), {})
        self.assertIn('<meta name="robots" content="noindex,follow">', alias.read_text())
        self.assertIn('<meta http-equiv="refresh" content="0; url=history-a.html">', alias.read_text())
        for locale in builder.LOCALES:
            localized = (self.site / locale / "blog/history-old-hash.html").read_text()
            self.assertFalse(builder.is_indexable_html(localized))
            self.assertEqual(fixtures.alternate_links(localized), {})
            sitemap = (self.site / f"sitemap-{locale}.xml").read_text()
            self.assertNotIn("history-old-hash", sitemap)
            self.assertIn(f"{fixtures.SITE_URL}/{locale}/blog/history-a.html", sitemap)
        # Proves the protected Chinese head as well as body stayed unchanged;
        # only the approved guarded bootstrap is allowed on the old alias.
        parity.verify_snapshot(root=self.site, snapshot_path=snapshot)

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

    def test_release_scope_only_buys_published_cohort_and_preserves_chinese(self):
        translator = fixtures.RecordingTranslator()
        manifest = self.build(translator, translation_scope="release")
        ledger = self.activate_fixture_ledger()
        paid = "\n".join(translator.sources)
        self.assertEqual(manifest["index_policy"]["history_release"]["translation_mode"], "translate-published-cohort")
        self.assertEqual(len(ledger["released"]), 1)
        self.assertEqual(ledger["pending_count"], 2)
        for canonical, title in self.sources.items():
            selected = canonical in ledger["released"] or canonical.endswith("/blog/new.html")
            self.assertEqual(title in paid, selected, canonical)
            relative = canonical.removeprefix(fixtures.SITE_URL + "/")
            for locale in builder.LOCALES:
                page = (self.site / locale / relative).read_text()
                self.assertEqual('data-kc-locale-deferred="true"' in page, not selected)
                self.assertEqual(f"/{locale}/{relative}" in (self.site / f"sitemap-{locale}.xml").read_text(), selected)
        for relative, body in self.protected.items():
            self.assertEqual(fixtures.body_bytes(self.site / relative), body)
        self.assertEqual((self.site / "assets/app.js").read_bytes(), self.app_bytes)

    def test_release_scope_continues_next_batch_without_rebuying_successes(self):
        self.build(fixtures.RecordingTranslator(), translation_scope="release")
        first = self.activate_fixture_ledger()
        same_day = fixtures.RecordingTranslator()
        self.build(same_day, translation_scope="release", previous=True, cache_in=self.fixture.cache)
        self.assertEqual(same_day.calls, [])
        tomorrow = fixtures.RecordingTranslator()
        self.build(tomorrow, translation_scope="release", today="2026-09-06", previous=True, cache_in=self.fixture.cache)
        later = self.activate_fixture_ledger()
        paid = "\n".join(tomorrow.sources)
        self.assertEqual(len(later["released"]), 2)
        for canonical in first["released"]:
            self.assertNotIn(self.sources[canonical], paid)
        newly_released = set(later["released"]) - set(first["released"])
        self.assertEqual(len(newly_released), 1)
        self.assertIn(self.sources[newly_released.pop()], paid)

    def test_unpublished_translation_failure_cannot_block_release_scope(self):
        recorder = fixtures.RecordingTranslator()
        def translator(locale, units):
            if any("月内深入研究文章乙" in unit.source or "月内研究资产报告" in unit.source for unit in units):
                raise builder.TranslationError("An unpublished historical page must not block publication")
            return recorder(locale, units)
        manifest = self.build(translator, translation_scope="release")
        self.assertTrue(all(value == 1 for value in manifest["coverage"].values()))
        self.assertNotIn(fixtures.SITE_URL + "/blog/history-b.html", self.activate_fixture_ledger()["released"])

    def test_standalone_month_metadata_is_prepaid_only_when_requested(self):
        chart_path = self.site / "data/chart_search_index.json"
        chart_payload = json.loads(chart_path.read_text())
        template = copy.deepcopy(chart_payload["reports"][0])
        for day, identity, label in (("260904", "historic", "独立历史图表标题"), ("20260905", "new", "独立新增图表标题")):
            report = copy.deepcopy(template)
            report.pop("report_id")
            report["report_ref"] = identity
            report["date_folder"] = day
            report["title"] = label
            report["charts"][0]["id"] = identity + "-chart"
            chart_payload["reports"].append(report)
        chart_path.write_text(json.dumps(chart_payload, ensure_ascii=False))
        hot_payload = json.loads(self.fixture.hot_report_index.read_text())
        newest = copy.deepcopy(hot_payload["items"][0])
        newest.update(id="hot:fedcba9876543210", title="独立新增热门报告", title_cn="独立新增热门报告", date="2026-09-05")
        hot_payload["items"].append(newest)
        self.fixture.hot_report_index.write_text(json.dumps(hot_payload, ensure_ascii=False))
        release = fixtures.RecordingTranslator()
        self.build(release, translation_scope="release")
        paid = "\n".join(release.sources)
        self.assertNotIn("独立历史图表标题", paid)
        self.assertNotIn("人工智能热门报告中文标题", paid)
        self.assertIn("独立新增图表标题", paid)
        self.assertIn("独立新增热门报告", paid)
        overlay_paths = [self.site / f"data/i18n/{locale}/{filename}" for locale in builder.LOCALES
                         for filename in (builder.CHART_OVERLAY_FILE, builder.HOT_REPORT_OVERLAY_FILE)]
        published_bytes = {path: path.read_bytes() for path in overlay_paths}
        month = fixtures.RecordingTranslator()
        self.build(month, translation_scope="month", cache_in=self.fixture.cache)
        self.assertIn("独立历史图表标题", "\n".join(month.sources))
        self.assertIn("人工智能热门报告中文标题", "\n".join(month.sources))
        for path, before in published_bytes.items():
            self.assertEqual(path.read_bytes(), before, "prepayment must not publish extra historical metadata")
        saved = fixtures.RecordingTranslator()
        self.build(saved, translation_scope="release", cache_in=self.fixture.cache)
        self.assertEqual(saved.calls, [])


if __name__ == "__main__":
    unittest.main()
