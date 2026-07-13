#!/usr/bin/env python3
from __future__ import annotations

import unittest

from fetch_institution_latest_pdfs import INSTITUTIONS, collect_worldbank_items
from select_macro_trend_pdfs import sanitize_filename


class _FakeResponse:
    def raise_for_status(self) -> None:
        return None

    def json(self) -> dict:
        return {
            "documents": {
                "facets": [],
                "D123": {
                    "display_title": "A current working paper",
                    "url": "https://documents.worldbank.org/example",
                    "guid": "D123",
                    "docdt": "2026-07-01",
                    "pdfurl": "https://documents.worldbank.org/example.pdf",
                },
            }
        }


class _FakeSession:
    def __init__(self) -> None:
        self.url = ""
        self.params: dict = {}

    def get(self, url: str, *, params: dict, timeout: int) -> _FakeResponse:
        self.url = url
        self.params = params
        return _FakeResponse()


class SourceMonitoringTests(unittest.TestCase):
    def test_long_selected_filename_keeps_pdf_extension(self) -> None:
        result = sanitize_filename("Goldman Sachs-" + ("very-long-title-" * 30), "report.pdf")
        self.assertTrue(result.endswith(".pdf"))
        self.assertLessEqual(len(result.encode("utf-8")), 180)

    def test_long_unicode_filename_does_not_split_a_character(self) -> None:
        result = sanitize_filename("世界银行" * 100, "report.pdf")
        self.assertTrue(result.endswith(".pdf"))
        self.assertLessEqual(len(result.encode("utf-8")), 180)

    def test_worldbank_uses_current_v3_api_and_sort_parameter(self) -> None:
        cfg = INSTITUTIONS["worldbank"]
        self.assertEqual("https://search.worldbank.org/api/v3/wds", cfg["api_base"])
        self.assertEqual("docdt", cfg["params"]["sort"])
        self.assertNotIn("srt", cfg["params"])
        self.assertTrue(cfg["recency_filter"])

        session = _FakeSession()
        items = collect_worldbank_items(cfg, session, timeout=10, rows=30)
        self.assertEqual(1, len(items))
        self.assertEqual("2026-07-01", items[0]["date"])
        self.assertEqual(30, session.params["rows"])


if __name__ == "__main__":
    unittest.main()
