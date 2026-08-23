#!/usr/bin/env python3
"""Regression tests for institution PDF source resolution."""

from __future__ import annotations

import unittest
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
        self._json_data = json_data or {}
        self.status_code = status_code

    def json(self) -> dict:
        return self._json_data

    def raise_for_status(self) -> None:
        return None


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
