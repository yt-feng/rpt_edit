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


def write_page(root: Path, url: str, *, canonical: str | None = None, robots: str = "index,follow") -> None:
    path = indexnow.site_path_for_url(root, url, BASE_URL)
    assert path is not None
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(
        "<!doctype html><html><head>"
        f'<meta name="robots" content="{robots}">'
        f'<link rel="canonical" href="{canonical or url}">'
        "</head><body>page</body></html>",
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
    def test_release_workflow_fails_closed_when_indexnow_submission_fails(self) -> None:
        workflow = (
            Path(__file__).resolve().parents[1] / ".github/workflows/neutral-edge-cutover.yml"
        ).read_text(encoding="utf-8")
        start = workflow.index("      - name: Submit changed public URLs to IndexNow\n")
        end = workflow.index("      - name: Remove private values from persistent source\n", start)
        step = workflow[start:end]
        self.assertNotIn("continue-on-error", step)
        self.assertIn("scripts/submit_portal_indexnow.py", step)

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
