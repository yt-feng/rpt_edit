#!/usr/bin/env python3
"""Regression tests for institution PDF source resolution."""

from __future__ import annotations

import unittest
import json
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import fetch_institution_latest_pdfs as fetcher


COUNTRY_REPORT_URL = (
    "https://www.imf.org/-/media/files/publications/cr/2026/english/"
    "1zweea2026002.pdf"
)
MONGOLIA_COUNTRY_REPORT_URL = (
    "https://www.imf.org/-/media/files/publications/cr/2026/english/"
    "1mngea2026001.pdf"
)


class FakeResponse:
    def __init__(
        self,
        *,
        text: str = "",
        json_data: dict | None = None,
        status_code: int = 200,
    ) -> None:
        self.text = text
        self.content = text.encode("utf-8")
        self._json_data = json_data or {}
        self.status_code = status_code

    def json(self) -> dict:
        return self._json_data

    def raise_for_status(self) -> None:
        return None


class BISRedesignTests(unittest.TestCase):
    FIXTURES = Path(__file__).parent / "fixtures" / "institution_sources"
    REPORT_URL = "https://www.bis.org/publications/working-paper-1376-what-determines-banks-excess-demand-reserves"

    def test_modern_feed_keeps_publications_dates_and_legacy_dedup(self) -> None:
        response = FakeResponse(text=(self.FIXTURES / "bis_research_redesign.rss").read_text())
        with patch.object(fetcher, "http_get", return_value=response) as get:
            items = fetcher.collect_rss_items(fetcher.INSTITUTIONS["bis"], object(), 10)
        self.assertEqual(get.call_count, 1)
        self.assertEqual(len(items), 7)
        self.assertEqual(items[0]["source_url"], self.REPORT_URL)
        self.assertEqual(items[0]["guid"], "https://www.bis.org/publ/work1376.htm")
        self.assertEqual(items[0]["date"], "2026-09-07T00:00:00Z")
        self.assertEqual(items[0]["pdf_candidates"], [])
        self.assertEqual(items[0]["scrape_url"], self.REPORT_URL)
        self.assertEqual(items[2]["pdf_candidates"], ["https://www.bis.org/bcbs/publ/d600.pdf"])
        self.assertEqual(items[3]["pdf_candidates"], ["https://www.bis.org/fsi/publ/insights77.pdf"])
        self.assertEqual([item["pdf_candidates"][0] for item in items[4:]], [
            "https://www.bis.org/publ/arpdf/ar2026e.pdf",
            "https://www.bis.org/publ/qtrpdf/r_qt2606.pdf",
            "https://www.bis.org/publ/bppdf/bispap172.pdf",
        ])

    def test_scoped_download_ignores_related_reports_and_attachments(self) -> None:
        page = (self.FIXTURES / "bis_work1376_download.html").read_text()
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), [self.REPORT_URL + ".pdf"])

    def test_primary_download_can_point_to_official_file_storage(self) -> None:
        page = '<div class="hero-publication__buttons"><a class="btn btn--primary" href="/content/dam/bis/papers/work1376.pdf">PDF (38 Pages)</a></div>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), ["https://www.bis.org/content/dam/bis/papers/work1376.pdf"])

    def test_quarterly_review_download_uses_issue_hero_not_related_pdfs(self) -> None:
        page_url = "https://www.bis.org/publications/qr-202609"
        page = '''<div class="hero-quaterly container-xxl">
          <div class="col-12 hero-quaterly__buttons"><div class="button">
          <a class="btn btn--primary btn--size-large btn--inverted"
             href="https://www.bis.org/publications/qr-202609_0.pdf"
             aria-label="PDF (90 Pages)">PDF (90 Pages)</a></div></div></div>
          <div class="related"><a class="btn btn--primary"
             href="/publications/qr-202606.pdf">Previous issue</a></div>'''
        self.assertEqual(fetcher.scrape_pdf_candidates(page, page_url), [
            "https://www.bis.org/publications/qr-202609_0.pdf",
        ])

    def test_quarterly_review_without_issue_pdf_stays_unresolved(self) -> None:
        page = '''<div class="hero-quaterly__buttons"><a class="btn btn--outline"
          href="#">Share</a></div><a class="btn btn--primary"
          href="/publications/unrelated.pdf">Related report</a>'''
        self.assertEqual(fetcher.scrape_pdf_candidates(
            page, "https://www.bis.org/publications/qr-202609"), [])

    def test_missing_main_pdf_does_not_use_related_file_or_non_bis_host(self) -> None:
        page = '<a href="/publications/unrelated.pdf">Related paper</a><div class="hero-publication__buttons"><a class="btn btn--primary" href="https://example.org/report.pdf">PDF</a></div>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, self.REPORT_URL), [])

    def test_legacy_page_pdf_and_query_compatibility(self) -> None:
        cfg = fetcher.INSTITUTIONS["bis"]
        page_url = "https://www.bis.org/publ/work1376.htm"
        self.assertEqual(fetcher._derive_pdf_candidates(cfg, page_url + "?download=1"), ["https://www.bis.org/publ/work1376.pdf?download=1"])
        page = '<a href="work1376.pdf">Full paper</a><a href="work1375.pdf">Previous paper</a>'
        self.assertEqual(fetcher.scrape_pdf_candidates(page, page_url), ["https://www.bis.org/publ/work1376.pdf"])

    def test_known_series_keep_existing_seen_state_keys(self) -> None:
        for modern, old in (
            ("working-paper-1373-settlement-liquidity", "publ/work1373.htm"),
            ("bulletin-134-supervisory-screening", "publ/bisbull134.htm"),
            ("fsi-insight-77-high-expectation", "fsi/publ/insights77.htm"),
        ):
            with self.subTest(modern=modern):
                self.assertEqual(fetcher.bis_publication_guid("https://www.bis.org/publications/" + modern), "https://www.bis.org/" + old)

    def run_bis_main(self, directory: str, items: list[dict], seen: dict | None = None) -> tuple[int, dict, dict]:
        path = Path(directory)
        state_path = path / "seen.json"
        state_path.write_text(json.dumps({"version": 1, "items": seen or {}}))
        argv = ["fetcher", "--institutions", "bis", "--output-dir", str(path / "pdfs"), "--seen-state-path", str(state_path), "--archive-path", str(path / "archive.jsonl"), "--since-days", "7"]
        with (
            patch.object(fetcher.sys, "argv", argv),
            patch.object(fetcher, "collect_rss_items", return_value=items),
            patch.object(fetcher, "http_get", return_value=FakeResponse(text='<a href="/unrelated.pdf">Related paper</a>')),
            patch.object(fetcher, "write_github_output"),
            patch.object(fetcher, "write_source_health_summary"),
        ):
            code = fetcher.main()
        return code, json.loads(state_path.read_text()), json.loads((path / "pdfs" / "institution_run_manifest.json").read_text())

    def test_main_pdf_missing_is_reported_and_remains_retryable(self) -> None:
        item = {"title": "Fixture report", "source_url": self.REPORT_URL, "guid": self.REPORT_URL, "date": fetcher.datetime.now(fetcher.timezone.utc).isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL}
        with tempfile.TemporaryDirectory() as directory:
            code, state, manifest = self.run_bis_main(directory, [item])
        self.assertEqual(code, 2)
        self.assertNotIn("bis:" + self.REPORT_URL, state["items"])
        self.assertEqual(manifest["source_checks"][0]["resolution_failure_count"], 1)
        self.assertEqual(manifest["skipped"][0]["reason"], "main_pdf_missing")

    def test_existing_seen_identity_and_recency_still_skip_downloads(self) -> None:
        now = fetcher.datetime.now(fetcher.timezone.utc)
        guid = fetcher.bis_publication_guid(self.REPORT_URL)
        items = [
            {"title": "Seen report", "source_url": self.REPORT_URL, "guid": guid, "date": now.isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
            {"title": "Older report", "source_url": self.REPORT_URL + "-older", "guid": "older", "date": (now - fetcher.timedelta(days=8)).isoformat(), "pdf_candidates": [], "scrape_url": self.REPORT_URL},
        ]
        seen = {"bis:" + guid: {"status": "downloaded", "first_seen": now.date().isoformat()}}
        with tempfile.TemporaryDirectory() as directory:
            code, state, manifest = self.run_bis_main(directory, items, seen)
        self.assertEqual(code, 0)
        self.assertEqual(manifest["source_checks"][0]["eligible_item_count"], 0)
        self.assertEqual(state["items"]["bis:" + guid]["status"], "downloaded")
        self.assertEqual(state["items"]["bis:older"]["status"], "too_old")


class CoveoPreviewTests(unittest.TestCase):
    def test_cached_html_exposes_country_report_pdf(self) -> None:
        cached_html = (
            '<html><a href="/-/media/files/publications/cr/2026/english/'
            '1zweea2026002.pdf">Download PDF</a></html>'
        )

        candidates = fetcher.scrape_pdf_candidates(
            cached_html,
            "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/zimbabwe",
        )

        self.assertEqual(candidates[0], COUNTRY_REPORT_URL)

    def test_cached_stock_number_resolves_fresh_country_report(self) -> None:
        cached_html = (
            '<li><p>Stock No<!-- -->:</p>'
            '<p role="presentation">1MNGEA2026001</p></li>'
        )

        candidates = fetcher.scrape_imf_preview_candidates(
            cached_html,
            (
                "https://www.imf.org/en/publications/cr/issues/2026/08/05/"
                "mongolia-2026-article-iv-consultation-discussions"
            ),
        )

        self.assertEqual(candidates[0], MONGOLIA_COUNTRY_REPORT_URL)
        self.assertEqual(
            candidates[1],
            MONGOLIA_COUNTRY_REPORT_URL.removesuffix(".pdf") + "-source-pdf.pdf",
        )

    def test_coveo_items_keep_preview_id_and_filter_rollups(self) -> None:
        payload = {
            "totalCount": 2,
            "results": [
                {
                    "title": "Zimbabwe: Staff Report",
                    "uniqueId": "country-report-cache-id",
                    "raw": {
                        "clickableuri": (
                            "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/"
                            "zimbabwe-staff-report"
                        ),
                        "permanentid": "country-report",
                        "imfseries": "IMF Staff Country Reports",
                        "seriesvolumeno": "2026/212",
                    },
                },
                {
                    "title": "Commodity Special Feature",
                    "uniqueId": "rollup-cache-id",
                    "raw": {
                        "clickableuri": (
                            "https://www.imf.org/en/Publications/SPROLLs/"
                            "commodity-special-feature"
                        ),
                        "permanentid": "rollup",
                    },
                },
            ],
        }
        cfg = dict(fetcher.INSTITUTIONS["imf"])

        with patch.object(fetcher, "http_post", return_value=FakeResponse(json_data=payload)):
            items = fetcher.collect_coveo_items(cfg, object(), timeout=10, rows=25)

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["guid"], "country-report")
        self.assertEqual(items[0]["coveo_unique_id"], "country-report-cache-id")

    def test_preview_helper_calls_coveo_html_endpoint(self) -> None:
        captured: dict = {}
        cached_html = f'<a href="{COUNTRY_REPORT_URL}">PDF</a>'

        def fake_http_get(session, url, timeout, **kwargs):
            captured.update({"url": url, "timeout": timeout, **kwargs})
            return FakeResponse(text=cached_html)

        cfg = dict(fetcher.INSTITUTIONS["imf"])
        with patch.object(fetcher, "http_get", side_effect=fake_http_get):
            candidates = fetcher.collect_coveo_preview_candidates(
                cfg,
                object(),
                "country-report-cache-id",
                "https://www.imf.org/en/Publications/CR/Issues/2026/08/07/zimbabwe",
                12,
            )

        self.assertEqual(candidates[0], COUNTRY_REPORT_URL)
        self.assertTrue(captured["url"].endswith("/rest/search/v2/html"))
        self.assertEqual(
            captured["params"],
            {
                "organizationId": "imfproduction561s308u",
                "uniqueId": "country-report-cache-id",
            },
        )
        self.assertTrue(captured["headers"]["Authorization"].startswith("Bearer "))


class DuckDuckGoFallbackTests(unittest.TestCase):
    RESULT_HTML = (
        '<html><a href="https://www.mckinsey.com/~/media/mckinsey/'
        'featured-insights/2026/example-report.pdf">Example report</a></html>'
    )
    STORE_HTML = (
        '<article><h5><span>Independent official report</span></h5>'
        '<time datetime="2026-08-22T12:00:00Z">August 22, 2026</time>'
        '<a href="#/download/%2F~%2Fmedia%2Fmckinsey%2Fofficial-report.pdf">'
        'Report (20 pages)</a></article>'
    )

    @staticmethod
    def config() -> dict:
        return {
            "query": "site:mckinsey.com filetype:pdf",
            "recent_years": 0,
            "fallback_pdf_listing_urls": [
                "https://www.mckinsey.com/featured-insights/insights-store",
            ],
        }

    def test_browser_timeout_falls_back_to_plain_requests(self) -> None:
        browser = Mock()
        browser.get.side_effect = fetcher.requests.Timeout("fixture timeout")
        session = Mock()
        session.get.return_value = FakeResponse(text=self.RESULT_HTML)

        with (
            patch.object(fetcher, "_HAS_CFFI", True),
            patch.object(fetcher, "cffi_requests", browser),
        ):
            items = fetcher.collect_ddg_items(self.config(), session, timeout=60, df="")

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Example report")
        self.assertEqual(browser.get.call_count, 1)
        self.assertEqual(session.get.call_count, 1)
        self.assertEqual(session.get.call_args.kwargs["timeout"], 25)

    def test_ddg_challenge_falls_back_to_official_listing(self) -> None:
        session = Mock()
        session.get.side_effect = [
            FakeResponse(
                text='<form class="challenge-form">bots use DuckDuckGo too.</form>',
                status_code=202,
            ),
            FakeResponse(text=self.STORE_HTML),
        ]

        with patch.object(fetcher, "_HAS_CFFI", False):
            items = fetcher.collect_ddg_items(self.config(), session, timeout=10, df="")

        self.assertEqual(len(items), 1)
        self.assertEqual(items[0]["title"], "Independent official report")
        self.assertEqual(items[0]["date"], "2026-08-22T12:00:00Z")
        self.assertEqual(
            items[0]["source_url"],
            "https://www.mckinsey.com/~/media/mckinsey/official-report.pdf",
        )
        called_urls = [call.args[0] for call in session.get.call_args_list]
        self.assertEqual(
            called_urls,
            [
                "https://html.duckduckgo.com/html/",
                "https://www.mckinsey.com/featured-insights/insights-store",
            ],
        )

    def test_official_listing_parser_uses_publication_date_for_recent_filter(self) -> None:
        year = str(fetcher.datetime.now(fetcher.timezone.utc).year)
        store_html = self.STORE_HTML.replace("2026", year)
        session = Mock()
        session.get.side_effect = [
            fetcher.requests.Timeout("fixture timeout"),
            FakeResponse(text=store_html),
        ]
        cfg = self.config()
        cfg["recent_years"] = 1

        with patch.object(fetcher, "_HAS_CFFI", False):
            items = fetcher.collect_ddg_items(cfg, session, timeout=10, df="")

        self.assertEqual(len(items), 1)
        self.assertTrue(items[0]["date"].startswith(year))

    def test_all_transport_failures_raise_source_health_error(self) -> None:
        session = Mock()
        session.get.side_effect = fetcher.requests.Timeout("fixture timeout")

        with (
            patch.object(fetcher, "_HAS_CFFI", False),
            self.assertRaisesRegex(RuntimeError, "unavailable across all routes"),
        ):
            fetcher.collect_ddg_items(self.config(), session, timeout=10, df="")

        self.assertEqual(session.get.call_count, 2)


if __name__ == "__main__":
    unittest.main(verbosity=2)
