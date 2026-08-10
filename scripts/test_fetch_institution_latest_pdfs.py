#!/usr/bin/env python3
"""Regression tests for institution PDF source resolution."""

from __future__ import annotations

import unittest
from unittest.mock import patch

import fetch_institution_latest_pdfs as fetcher


COUNTRY_REPORT_URL = (
    "https://www.imf.org/-/media/files/publications/cr/2026/english/"
    "1zweea2026002.pdf"
)


class FakeResponse:
    def __init__(self, *, text: str = "", json_data: dict | None = None) -> None:
        self.text = text
        self._json_data = json_data or {}

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


if __name__ == "__main__":
    unittest.main(verbosity=2)
