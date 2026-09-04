#!/usr/bin/env python3
from __future__ import annotations

from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch
from xml.sax.saxutils import escape

import submit_portal_indexnow as indexnow


BASE_URL = "https://portal.example.invalid"


def item(report_id: str, title: str, bank_name: str = "Example Research") -> dict[str, object]:
    return {
        "id": report_id,
        "title": title,
        "title_zh": title,
        "filename": f"{title}.pdf",
        "date_folder": "2026-08-30",
        "bank_code": "EX",
        "bank_name": bank_name,
        "available": True,
        "server_modified": "2026-08-30T01:00:00Z",
    }


def write_page(
    root: Path,
    url: str,
    *,
    canonical: str | None = None,
    robots: str = "index,follow",
    body: str = "page",
) -> None:
    path = indexnow.site_path_for_url(root, url, BASE_URL)
    assert path is not None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "<!doctype html><html><head>"
        f'<meta name="robots" content="{robots}">'
        f'<link rel="canonical" href="{canonical or url}">'
        f"</head><body>{body}</body></html>",
        encoding="utf-8",
    )


def write_sitemap(path: Path, rows: dict[str, str]) -> None:
    body = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
    ]
    for url, lastmod in rows.items():
        body.append(f"<url><loc>{escape(url)}</loc><lastmod>{escape(lastmod)}</lastmod></url>")
    body.append("</urlset>")
    path.write_text("\n".join(body), encoding="utf-8")


class SubmissionPlanTests(unittest.TestCase):
    def test_release_transaction_leaves_indexnow_to_the_durable_tail(self) -> None:
        workflow = (
            Path(__file__).resolve().parents[1] / ".github/workflows/neutral-edge-cutover.yml"
        ).read_text(encoding="utf-8")
        self.assertNotIn("scripts/submit_portal_indexnow.py", workflow)
        self.assertNotIn("Submit changed public URLs to IndexNow", workflow)

    def test_plan_is_a_canonical_delta_and_excludes_legacy_redirects(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            aggregates = [
                f"{BASE_URL}/",
                f"{BASE_URL}/reports/",
                f"{BASE_URL}/reports/topics.html",
                f"{BASE_URL}/reports/institutions/bernstein/",
                f"{BASE_URL}/blog/",
            ]
            for url in aggregates:
                write_page(site, url)

            report_same = f"{BASE_URL}/reports/report-same.html"
            report_updated = f"{BASE_URL}/reports/report-updated.html"
            report_added = f"{BASE_URL}/reports/report-added.html"
            report_retired = f"{BASE_URL}/reports/report-retired.html"
            for url in (report_same, report_updated, report_added):
                write_page(site, url)

            blog_same = f"{BASE_URL}/blog/article-same.html"
            blog_updated = f"{BASE_URL}/blog/article-updated.html"
            blog_added = f"{BASE_URL}/blog/article-added.html"
            blog_retired = f"{BASE_URL}/blog/article-retired.html"
            legacy_redirect = f"{BASE_URL}/blog/article-legacy.html"
            noindex_article = f"{BASE_URL}/blog/article-noindex.html"
            wrong_canonical = f"{BASE_URL}/blog/article-wrong-canonical.html"
            stray_html = f"{BASE_URL}/blog/not-in-sitemap.html"
            for url in (blog_same, blog_updated, blog_added, stray_html):
                write_page(site, url)
            write_page(site, noindex_article, robots="noindex,follow")
            write_page(site, wrong_canonical, canonical=blog_added)
            write_page(site, legacy_redirect, canonical=blog_added, robots="noindex,follow")

            previous_catalog = {
                "items": [
                    item("report-same", "same"),
                    item("report-updated", "old title"),
                    item("report-retired", "retired", "Bernstein Research"),
                ]
            }
            current_catalog = {
                "updated_at_bjt": "2026-08-30 09:30:00 +0800",
                "items": [
                    item("report-same", "same"),
                    item("report-updated", "new title"),
                    item("report-added", "added"),
                ],
            }
            previous_sitemap = {
                **{url: "2026-08-29" for url in aggregates},
                report_same: "2026-08-29",
                report_updated: "2026-08-29",
                report_retired: "2026-08-29",
                blog_same: "2026-08-29",
                blog_updated: "2026-08-29",
                blog_retired: "2026-08-29",
                legacy_redirect: "2026-08-29",
            }
            current_sitemap = {
                **{url: "2026-08-30" for url in aggregates},
                report_same: "2026-08-29",
                report_updated: "2026-08-30",
                report_added: "2026-08-30",
                blog_same: "2026-08-29",
                blog_updated: "2026-08-30",
                blog_added: "2026-08-30",
                noindex_article: "2026-08-30",
                wrong_canonical: "2026-08-30",
            }

            plan = indexnow.build_submission_plan(
                current_catalog,
                previous_catalog,
                current_sitemap,
                previous_sitemap,
                site,
                BASE_URL,
                3,
            )

            self.assertEqual(
                {
                    *aggregates,
                    report_updated,
                    report_added,
                    report_retired,
                    blog_updated,
                    blog_added,
                    blog_retired,
                },
                set(plan.urls),
            )
            self.assertNotIn(report_same, plan.urls)
            self.assertNotIn(blog_same, plan.urls)
            self.assertNotIn(legacy_redirect, plan.urls)
            self.assertNotIn(noindex_article, plan.urls)
            self.assertNotIn(wrong_canonical, plan.urls)
            self.assertNotIn(stray_html, plan.urls)
            self.assertEqual(1, plan.reason_counts["report_added"])
            self.assertEqual(1, plan.reason_counts["report_updated"])
            self.assertEqual(1, plan.reason_counts["report_retired"])
            self.assertEqual(1, plan.reason_counts["blog_added"])
            self.assertEqual(1, plan.reason_counts["blog_updated"])
            self.assertEqual(1, plan.reason_counts["blog_retired"])
            self.assertEqual(2, plan.skipped_reason_counts["current_not_indexable_self_canonical"])
            self.assertEqual(1, plan.skipped_reason_counts["retired_not_301_404_410"])

    def test_no_catalog_or_sitemap_delta_submits_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            report = f"{BASE_URL}/reports/report-same.html"
            write_page(site, report)
            catalog = {"items": [item("report-same", "same")]}
            sitemap = {report: "2026-08-30"}
            plan = indexnow.build_submission_plan(catalog, catalog, sitemap, sitemap, site, BASE_URL, 3)
            self.assertEqual([], plan.urls)
            self.assertEqual({}, plan.reason_counts)

    def test_other_canonical_pages_use_url_and_lastmod_delta(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            hub_added = f"{BASE_URL}/reports/institutions/example/"
            hub_updated = f"{BASE_URL}/reports/topics/artificial-intelligence/"
            hub_retired = f"{BASE_URL}/reports/topics/retired-topic/"
            pagination_stable = f"{BASE_URL}/reports/page-2.html"
            pagination_updated = f"{BASE_URL}/reports/page-3.html"
            legacy_soft_redirect = f"{BASE_URL}/reports/topics/legacy-topic/"
            report = f"{BASE_URL}/reports/report-same.html"
            for url in (hub_added, hub_updated, pagination_stable, pagination_updated, report):
                write_page(site, url)
            write_page(site, legacy_soft_redirect, canonical=hub_updated, robots="noindex,follow")

            catalog = {"items": [item("report-same", "same")]}
            previous_sitemap = {
                hub_updated: "2026-08-29",
                hub_retired: "2026-08-29",
                pagination_stable: "2026-08-29",
                pagination_updated: "2026-08-29",
                legacy_soft_redirect: "2026-08-29",
                report: "2026-08-29",
            }
            current_sitemap = {
                hub_added: "2026-08-30",
                hub_updated: "2026-08-30",
                pagination_stable: "2026-08-29",
                pagination_updated: "2026-08-30",
                report: "2026-08-30",
            }
            plan = indexnow.build_submission_plan(
                catalog,
                catalog,
                current_sitemap,
                previous_sitemap,
                site,
                BASE_URL,
                3,
            )

            self.assertEqual({hub_added, hub_updated, hub_retired, pagination_updated, report}, set(plan.urls))
            self.assertNotIn(pagination_stable, plan.urls)
            self.assertNotIn(legacy_soft_redirect, plan.urls)
            self.assertEqual(1, plan.reason_counts["report_page_updated"])
            self.assertEqual(1, plan.reason_counts["page_added"])
            self.assertEqual(2, plan.reason_counts["page_updated"])
            self.assertEqual(1, plan.reason_counts["page_retired"])
            self.assertEqual(1, plan.skipped_reason_counts["retired_not_301_404_410"])

    def test_load_sitemap_index_uses_only_local_canonical_children(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            child = root / "sitemap-blog-1.xml"
            article = f"{BASE_URL}/blog/article.html"
            write_sitemap(child, {article: "2026-08-30"})
            (root / "sitemap.xml").write_text(
                '<?xml version="1.0"?><sitemapindex xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">'
                f"<sitemap><loc>{BASE_URL}/sitemap-blog-1.xml</loc></sitemap>"
                "</sitemapindex>",
                encoding="utf-8",
            )
            self.assertEqual({article: "2026-08-30"}, indexnow.load_sitemap(root / "sitemap.xml"))

    def test_discovery_includes_only_live_self_canonical_locale_sitemap_urls(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            valid = {
                "ko": f"{BASE_URL}/ko/reports/report-ko.html",
                "ja": f"{BASE_URL}/ja/blog/article-ja.html",
                "ar": f"{BASE_URL}/ar/reports/topics/artificial-intelligence/",
            }
            for url in valid.values():
                write_page(site, url)

            missing = f"{BASE_URL}/ja/reports/missing.html"
            wrong_canonical = f"{BASE_URL}/ar/reports/wrong.html"
            unlisted = f"{BASE_URL}/ko/reports/unlisted.html"
            write_page(site, wrong_canonical, canonical=f"{BASE_URL}/reports/wrong.html")
            write_page(site, unlisted)
            write_sitemap(site / "sitemap-ko.xml", {valid["ko"]: "2026-09-04"})
            write_sitemap(
                site / "sitemap-ja.xml",
                {valid["ja"]: "2026-09-04", missing: "2026-09-04"},
            )
            write_sitemap(
                site / "sitemap-ar.xml",
                {valid["ar"]: "2026-09-04", wrong_canonical: "2026-09-04"},
            )

            urls = indexnow.discover_public_site_urls(site, BASE_URL)

            self.assertTrue(set(valid.values()).issubset(urls))
            self.assertNotIn(missing, urls)
            self.assertNotIn(wrong_canonical, urls)
            self.assertNotIn(unlisted, urls)

    def test_report_delta_submits_all_live_sitemap_listed_locale_variants(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            report_same = f"{BASE_URL}/reports/report-same.html"
            report_added = f"{BASE_URL}/reports/report-added.html"
            write_page(site, report_same)
            write_page(site, report_added)

            localized = {
                locale: f"{BASE_URL}/{locale}/reports/report-added.html"
                for locale in indexnow.LOCALIZED_LOCALES
            }
            for locale, url in localized.items():
                write_page(site, url)
                write_sitemap(site / f"sitemap-{locale}.xml", {url: "2026-09-04"})

            plan = indexnow.build_submission_plan(
                {"items": [item("report-same", "same"), item("report-added", "added")]},
                {"items": [item("report-same", "same")]},
                {report_same: "2026-09-03", report_added: "2026-09-04"},
                {report_same: "2026-09-03"},
                site,
                BASE_URL,
                3,
            )

            self.assertEqual({report_added, *localized.values()}, set(plan.urls))
            self.assertEqual(4, plan.reason_counts["report_added"])

    def test_report_delta_skips_unlisted_or_noncanonical_locale_variants(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            site = Path(directory)
            report_same = f"{BASE_URL}/reports/report-same.html"
            report_added = f"{BASE_URL}/reports/report-added.html"
            write_page(site, report_same)
            write_page(site, report_added)

            ko = f"{BASE_URL}/ko/reports/report-added.html"
            ja = f"{BASE_URL}/ja/reports/report-added.html"
            ar = f"{BASE_URL}/ar/reports/report-added.html"
            ja_home = f"{BASE_URL}/ja/"
            write_page(site, ko)
            write_page(site, ja)
            write_page(site, ja_home)
            write_page(site, ar, canonical=report_added)
            write_sitemap(site / "sitemap-ko.xml", {ko: "2026-09-04"})
            write_sitemap(site / "sitemap-ja.xml", {ja_home: "2026-09-04"})
            write_sitemap(site / "sitemap-ar.xml", {ar: "2026-09-04"})

            plan = indexnow.build_submission_plan(
                {"items": [item("report-same", "same"), item("report-added", "added")]},
                {"items": [item("report-same", "same")]},
                {report_same: "2026-09-03", report_added: "2026-09-04"},
                {report_same: "2026-09-03"},
                site,
                BASE_URL,
                3,
            )

            self.assertEqual({report_added, ko, ja_home}, set(plan.urls))
            self.assertNotIn(ja, plan.urls)
            self.assertNotIn(ar, plan.urls)
            self.assertEqual(2, plan.reason_counts["locale_added"])
            self.assertEqual(1, plan.skipped_reason_counts["locale_not_in_canonical_sitemap"])
            self.assertEqual(1, plan.skipped_reason_counts["locale_not_indexable_self_canonical"])

    def test_removed_locale_urls_are_submitted_from_previous_locale_sitemaps(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "current"
            previous_site = root / "previous"
            site.mkdir()
            previous_site.mkdir()

            home = f"{BASE_URL}/"
            report = f"{BASE_URL}/reports/report-same.html"
            write_page(site, home)
            write_page(site, report)
            localized_reports = {
                locale: f"{BASE_URL}/{locale}/reports/report-same.html"
                for locale in indexnow.LOCALIZED_LOCALES
            }
            for locale, localized_report in localized_reports.items():
                localized_home = f"{BASE_URL}/{locale}/"
                write_page(site, localized_home)
                write_sitemap(site / f"sitemap-{locale}.xml", {localized_home: "2026-09-04"})
                write_sitemap(
                    previous_site / f"sitemap-{locale}.xml",
                    {
                        localized_home: "2026-09-03",
                        localized_report: "2026-09-03",
                    },
                )

            catalog = {"items": [item("report-same", "same")]}
            source_sitemap = {home: "2026-09-04", report: "2026-09-04"}
            plan = indexnow.build_submission_plan(
                catalog,
                catalog,
                source_sitemap,
                source_sitemap,
                site,
                BASE_URL,
                3,
                previous_site,
            )

            self.assertEqual(set(localized_reports.values()), set(plan.urls))
            self.assertNotIn(report, plan.urls, "the unchanged Chinese source URL must stay untouched")
            self.assertEqual(3, plan.reason_counts["report_retired"])
            self.assertEqual({}, dict(plan.skipped_reason_counts))

    def test_initial_locale_inventory_additions_submit_without_a_source_delta(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "current"
            previous_site = root / "previous"
            site.mkdir()
            previous_site.mkdir()

            source_url = f"{BASE_URL}/reports/report-same.html"
            source_sitemap = {source_url: "2026-09-03"}
            localized = {
                locale: f"{BASE_URL}/{locale}/reports/report-same.html"
                for locale in indexnow.LOCALIZED_LOCALES
            }
            noindex_url = f"{BASE_URL}/ko/reports/historical.html"
            for locale, localized_url in localized.items():
                write_page(site, localized_url)
                rows = {localized_url: "2026-09-03"}
                if locale == "ko":
                    write_page(site, noindex_url, robots="noindex,follow")
                    rows[noindex_url] = "2026-09-03"
                write_sitemap(site / f"sitemap-{locale}.xml", rows)

            catalog = {"items": [item("report-same", "same")]}
            plan = indexnow.build_submission_plan(
                catalog,
                catalog,
                source_sitemap,
                source_sitemap,
                site,
                BASE_URL,
                3,
                previous_site,
            )

            self.assertEqual(set(localized.values()), set(plan.urls))
            self.assertNotIn(noindex_url, plan.urls)
            self.assertEqual(3, plan.reason_counts["locale_added"])
            self.assertEqual(1, plan.skipped_reason_counts["current_not_indexable_self_canonical"])

    def test_translation_only_html_change_submits_with_inherited_lastmod_unchanged(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "current"
            previous_site = root / "previous"
            site.mkdir()
            previous_site.mkdir()

            localized_url = f"{BASE_URL}/ja/blog/article-same.html"
            write_page(site, localized_url, body="corrected Japanese translation")
            write_page(previous_site, localized_url, body="previous Japanese translation")
            for release in (site, previous_site):
                write_sitemap(release / "sitemap-ja.xml", {localized_url: "2026-09-03"})

            source_sitemap = {f"{BASE_URL}/blog/article-same.html": "2026-09-03"}
            plan = indexnow.build_submission_plan(
                {"items": []},
                {"items": []},
                source_sitemap,
                source_sitemap,
                site,
                BASE_URL,
                3,
                previous_site,
            )

            self.assertEqual([localized_url], plan.urls)
            self.assertEqual(1, plan.reason_counts["locale_updated"])

    def test_unchanged_locale_html_and_inventory_submit_nothing(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "current"
            previous_site = root / "previous"
            site.mkdir()
            previous_site.mkdir()

            localized_url = f"{BASE_URL}/ar/reports/topics/still-live/"
            for release in (site, previous_site):
                write_page(release, localized_url, body="same Arabic translation")
                write_sitemap(release / "sitemap-ar.xml", {localized_url: "2026-09-03"})

            source_sitemap = {f"{BASE_URL}/reports/topics/still-live/": "2026-09-03"}
            plan = indexnow.build_submission_plan(
                {"items": []},
                {"items": []},
                source_sitemap,
                source_sitemap,
                site,
                BASE_URL,
                3,
                previous_site,
            )

            self.assertEqual([], plan.urls)
            self.assertEqual({}, plan.reason_counts)

    def test_locale_url_still_in_current_locale_sitemap_is_not_retired(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "current"
            previous_site = root / "previous"
            site.mkdir()
            previous_site.mkdir()

            localized_page = f"{BASE_URL}/ja/reports/topics/still-live/"
            write_page(site, localized_page)
            write_sitemap(site / "sitemap-ja.xml", {localized_page: "2026-09-04"})
            write_sitemap(previous_site / "sitemap-ja.xml", {localized_page: "2026-09-03"})

            source_sitemap = {f"{BASE_URL}/": "2026-09-04"}
            plan = indexnow.build_submission_plan(
                {"items": []},
                {"items": []},
                source_sitemap,
                source_sitemap,
                site,
                BASE_URL,
                3,
                previous_site,
            )

            self.assertEqual([], plan.urls)
            self.assertEqual({}, dict(plan.skipped_reason_counts))

    def test_cli_dry_run_emits_reason_counts(self) -> None:
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            site = root / "site"
            site.mkdir()
            report = f"{BASE_URL}/reports/report-added.html"
            for url in (f"{BASE_URL}/", f"{BASE_URL}/reports/", f"{BASE_URL}/reports/topics.html", report):
                write_page(site, url)
            current_catalog_path = root / "current.json"
            previous_catalog_path = root / "previous.json"
            current_catalog_path.write_text(
                json.dumps({"items": [item("report-added", "added")]}), encoding="utf-8"
            )
            previous_catalog_path.write_text(json.dumps({"items": [item("report-old", "old")]}), encoding="utf-8")
            current_sitemap_path = root / "current-sitemap.xml"
            previous_sitemap_path = root / "previous-sitemap.xml"
            write_sitemap(
                current_sitemap_path,
                {
                    f"{BASE_URL}/": "2026-08-30",
                    f"{BASE_URL}/reports/": "2026-08-30",
                    f"{BASE_URL}/reports/topics.html": "2026-08-30",
                    report: "2026-08-30",
                },
            )
            write_sitemap(
                previous_sitemap_path,
                {f"{BASE_URL}/reports/report-old.html": "2026-08-29"},
            )
            stdout = io.StringIO()
            argv = [
                "submit_portal_indexnow.py",
                "--catalog", str(current_catalog_path),
                "--previous-catalog", str(previous_catalog_path),
                "--site-dir", str(site),
                "--sitemap", str(current_sitemap_path),
                "--previous-sitemap", str(previous_sitemap_path),
                "--base-url", BASE_URL,
                "--dry-run",
            ]
            with patch.object(sys, "argv", argv), redirect_stdout(stdout):
                self.assertEqual(0, indexnow.main())
            payload = json.loads(stdout.getvalue())
            self.assertEqual(1, payload["reason_counts"]["report_added"])
            self.assertEqual(1, payload["reason_counts"]["report_retired"])
            self.assertEqual(5, payload["url_count"])


if __name__ == "__main__":
    unittest.main()
