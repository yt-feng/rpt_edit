#!/usr/bin/env python3
from __future__ import annotations

import unittest
from unittest.mock import Mock, patch

import requests

from fetch_institution_latest_pdfs import INSTITUTIONS, collect_worldbank_items, http_get, http_post
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

    def get(self, url: str, *, params: dict | None = None, timeout: int, **_kwargs) -> _FakeResponse:
        self.url = url
        self.params = params or {}
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

    @patch("fetch_institution_latest_pdfs.time.sleep")
    def test_http_get_retries_connection_error(self, sleep: Mock) -> None:
        session = Mock()
        success = Mock(status_code=200, headers={})
        session.get.side_effect = [requests.exceptions.ConnectionError("reset"), success]

        response = http_get(session, "https://example.com/feed", timeout=10)

        self.assertIs(response, success)
        self.assertEqual(session.get.call_count, 2)
        sleep.assert_called_once_with(2.0)

    @patch("fetch_institution_latest_pdfs.time.sleep")
    def test_http_get_retries_503_and_honors_retry_after(self, sleep: Mock) -> None:
        session = Mock()
        busy = Mock(status_code=503, headers={"Retry-After": "6"})
        success = Mock(status_code=200, headers={})
        session.get.side_effect = [busy, success]

        response = http_get(session, "https://example.com/feed", timeout=10)

        self.assertIs(response, success)
        self.assertEqual(session.get.call_count, 2)
        busy.close.assert_called_once()
        sleep.assert_called_once_with(6.0)

    @patch("fetch_institution_latest_pdfs.time.sleep")
    def test_http_get_does_not_retry_permanent_status(self, sleep: Mock) -> None:
        session = Mock()
        forbidden = Mock(status_code=403, headers={})
        session.get.return_value = forbidden

        response = http_get(session, "https://example.com/feed", timeout=10)

        self.assertIs(response, forbidden)
        session.get.assert_called_once()
        sleep.assert_not_called()

    @patch("fetch_institution_latest_pdfs.time.sleep")
    def test_http_get_does_not_retry_programming_error(self, sleep: Mock) -> None:
        session = Mock()
        session.get.side_effect = ValueError("bad test input")

        with self.assertRaises(ValueError):
            http_get(session, "https://example.com/feed", timeout=10)

        session.get.assert_called_once()
        sleep.assert_not_called()

    @patch("fetch_institution_latest_pdfs.time.sleep")
    def test_http_post_retries_timeout(self, sleep: Mock) -> None:
        session = Mock()
        success = Mock(status_code=200, headers={})
        session.post.side_effect = [requests.exceptions.Timeout("slow"), success]

        response = http_post(
            session,
            "https://example.com/search",
            timeout=10,
            json_payload={"q": ""},
        )

        self.assertIs(response, success)
        self.assertEqual(session.post.call_count, 2)
        sleep.assert_called_once_with(2.0)


if __name__ == "__main__":
    unittest.main()
