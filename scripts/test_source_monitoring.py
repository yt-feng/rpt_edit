#!/usr/bin/env python3
from __future__ import annotations

import unittest
import contextlib
import io
import os
import tempfile
from pathlib import Path
from unittest.mock import Mock, patch

import requests
import fetch_institution_latest_pdfs as fetcher

from fetch_institution_latest_pdfs import (
    IMF_PROXY_TEST_URL,
    INSTITUTIONS,
    collect_worldbank_items,
    derive_imf_pdf_candidates,
    http_get,
    http_post,
    resolve_working_proxy,
)
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
    def test_imf_uses_source_validated_proxy(self) -> None:
        cfg = INSTITUTIONS["imf"]
        self.assertTrue(cfg["use_proxy"])
        self.assertEqual(IMF_PROXY_TEST_URL, cfg["proxy_test_url"])

    def test_proxy_validation_rotates_past_imf_blocked_node(self) -> None:
        client = Mock()
        client.get.side_effect = [
            Mock(status_code=403),
            Mock(status_code=200),
        ]
        subscription = "http://proxy-one.example:8080\nhttp://proxy-two.example:8080"
        with (
            patch("fetch_institution_latest_pdfs._HAS_CFFI", True),
            patch("fetch_institution_latest_pdfs._fetch_subscription", return_value=subscription),
            patch("fetch_institution_latest_pdfs.cffi_requests", client),
        ):
            selected = resolve_working_proxy(
                "https://subscription.example/nodes",
                timeout=12,
                test_url=IMF_PROXY_TEST_URL,
            )

        self.assertEqual("http://proxy-two.example:8080", selected)
        self.assertEqual(2, client.get.call_count)
        for call in client.get.call_args_list:
            self.assertEqual(IMF_PROXY_TEST_URL, call.args[0])
            self.assertEqual(10, call.kwargs["timeout"])

    def test_impersonated_imf_request_receives_selected_proxy(self) -> None:
        client = Mock()
        response = Mock(status_code=200, headers={})
        client.get.return_value = response
        proxy = "http://proxy.example:8080"
        with (
            patch("fetch_institution_latest_pdfs._HAS_CFFI", True),
            patch("fetch_institution_latest_pdfs.cffi_requests", client),
        ):
            result = http_get(
                Mock(),
                "https://www.imf.org/en/Publications/example",
                timeout=20,
                impersonate=True,
                proxy=proxy,
            )

        self.assertIs(response, result)
        self.assertEqual(
            {"http": proxy, "https": proxy},
            client.get.call_args.kwargs["proxies"],
        )

    def test_imf_working_paper_candidates_bypass_landing_page(self) -> None:
        candidates = derive_imf_pdf_candidates({
            "imfseries": ["IMF Working Papers"],
            "seriesvolumeno": "Working Paper No. 2026/153",
        })

        self.assertEqual(
            "https://www.imf.org/-/media/files/publications/wp/2026/english/"
            "wpiea2026153-source-pdf.pdf",
            candidates[0],
        )
        self.assertEqual(
            "https://www.imf.org/-/media/files/publications/wp/2026/english/"
            "wpiea2026153.pdf",
            candidates[1],
        )

    def test_imf_series_candidates_cover_other_publication_families(self) -> None:
        cases = [
            ("Technical Assistance Reports", "Technical Assistance Report No. 2026/058", "tar/2026/english/tarea2026058.pdf"),
            ("Selected Issues Papers", "Selected Issues Paper No. 2026/065", "selected-issues-papers/2026/english/sipea2026065.pdf"),
            ("High Level Summary Technical Assistance Reports", "High Level Summary Technical Assistance Report No. 2026/039", "hls/2026/english/hlsea2026039.pdf"),
            ("Policy Papers", "Policy Paper No. 2026/022", "pp/2026/english/ppea2026022.pdf"),
        ]
        for series, volume, suffix in cases:
            with self.subTest(series=series):
                candidates = derive_imf_pdf_candidates({"imfseries": [series], "seriesvolumeno": volume})
                self.assertTrue(candidates[0].endswith(suffix))

    def test_imf_country_report_is_not_guessed(self) -> None:
        candidates = derive_imf_pdf_candidates({
            "imfseries": ["IMF Staff Country Reports"],
            "seriesvolumeno": "Country Report No. 2026/184",
        })

        self.assertEqual([], candidates)

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


class SubscriptionHealthTests(unittest.TestCase):
    NOW = 1800000000
    SECRET_URL = "https://subscription-private.example/token-secret"
    NODE = "socks5://user-secret:password-secret@proxy-private.example:1080"

    def setUp(self) -> None:
        self.directory = self.enterContext(tempfile.TemporaryDirectory())
        self.summary = Path(self.directory) / "summary.md"
        self.enterContext(patch.dict(os.environ, {
            "GITHUB_ACTIONS": "true", "GITHUB_STEP_SUMMARY": str(self.summary),
        }))
        self.output = io.StringIO()
        self.enterContext(contextlib.redirect_stdout(self.output))
        self.enterContext(patch.object(fetcher.time, "time", return_value=self.NOW))
        self.get = self.enterContext(patch.object(fetcher.requests, "get"))
        self.curl = self.enterContext(patch.object(fetcher.subprocess, "run"))
        self.client = Mock()
        self.client.get.return_value = Mock(status_code=200)
        self.enterContext(patch.object(fetcher, "cffi_requests", self.client))
        self.enterContext(patch.object(fetcher, "_HAS_CFFI", True))
        self.get.return_value = self.response(self.NOW + 30 * 86400)

    def response(self, expires: int | None) -> Mock:
        headers = {} if expires is None else {"Subscription-Userinfo": f"upload=12; download=30; total=100; expire={expires}"}
        return Mock(text=self.NODE, status_code=200, headers=headers)

    def resolve(self) -> str | None:
        return fetcher.resolve_working_proxy(self.SECRET_URL, 12, IMF_PROXY_TEST_URL)

    def test_expired_skips_all_nodes_and_other_subscription_transports(self) -> None:
        self.get.return_value = self.response(self.NOW - 1)
        self.assertIsNone(self.resolve())
        self.client.get.assert_not_called()
        self.curl.assert_not_called()
        self.assertIn("::warning::Proxy subscription expired", self.output.getvalue())
        self.assertIn("Renew or replace", self.summary.read_text())
        self.assertIn("Direct source fetching remains enabled", self.summary.read_text())

    def test_expiry_exactly_now_is_expired(self) -> None:
        self.assertTrue(fetcher._subscription_expired({"subscription-userinfo": f"expire={self.NOW}"}))

    def test_seven_day_boundary_warns_but_still_validates_node(self) -> None:
        self.get.return_value = self.response(self.NOW + 7 * 86400)
        self.assertEqual(self.resolve(), self.NODE.replace("socks5:", "socks5h:"))
        self.assertIn("::warning::Proxy subscription expires within 7 days", self.output.getvalue())
        self.client.get.assert_called_once()

    def test_not_near_expiry_avoids_renewal_warning(self) -> None:
        self.assertIsNotNone(self.resolve())
        self.assertNotIn("::warning::", self.output.getvalue())
        self.assertIn("more than 7 days remaining", self.summary.read_text())

    def test_missing_metadata_is_unknown_and_preserves_compatibility(self) -> None:
        self.get.return_value = self.response(None)
        self.assertIsNotNone(self.resolve())
        self.assertIn("expiry unknown", self.summary.read_text())
        self.client.get.assert_called_once()

    def test_malformed_metadata_never_guesses_expiration(self) -> None:
        for value in ("expire=bad-token-secret", "expire=-1", "expire=nan", "expire=1.5",
                      "expire=123; expire=456", "upload=1", "expire=99999999999999999",
                      "expire=999999999999", "expire=0"):
            with self.subTest(value=value):
                self.assertFalse(fetcher._subscription_expired({"subscription-userinfo": value}))
        self.assertNotIn("bad-token-secret", self.output.getvalue())
        self.assertIn("expiry unknown", self.summary.read_text())

    def test_header_name_is_case_insensitive(self) -> None:
        self.assertTrue(fetcher._subscription_expired({"SUBSCRIPTION-USERINFO": f"expire={self.NOW - 1}"}))

    def test_curl_metadata_checked_and_private_temporary_file_removed(self) -> None:
        self.get.side_effect = requests.ConnectionError(self.SECRET_URL)
        captured_paths = []

        def curl_response(command, **kwargs):
            path = Path(command[command.index("--dump-header") + 1])
            captured_paths.append(path)
            self.assertEqual(path.parent.stat().st_mode & 0o777, 0o700)
            path.write_text(f"HTTP/2 200\r\nSubscription-Userinfo: expire={self.NOW - 1}\r\n\r\n")
            return Mock(returncode=0, stdout=self.NODE, stderr="")

        self.curl.side_effect = curl_response
        self.assertIsNone(self.resolve())
        self.client.get.assert_not_called()
        self.assertTrue(captured_paths)
        self.assertFalse(captured_paths[0].parent.exists())

    def test_redirect_response_metadata_does_not_override_final_header(self) -> None:
        header = (f"HTTP/1.1 302 Found\r\nSubscription-Userinfo: expire={self.NOW - 1}\r\n\r\n"
                  f"HTTP/2 200\r\nSubscription-Userinfo: expire={self.NOW + 86400}\r\n\r\n")
        self.assertFalse(fetcher._subscription_expired(fetcher._curl_final_headers(header)))

    def test_cffi_subscription_metadata_is_checked(self) -> None:
        self.get.side_effect = requests.ConnectionError(self.SECRET_URL)
        self.curl.return_value = Mock(returncode=7, stderr=self.SECRET_URL)
        self.client.get.return_value = self.response(self.NOW - 1)
        self.assertIsNone(self.resolve())
        self.assertEqual(self.client.get.call_count, 1)  # subscription only; no node
        self.assertIn("subscription expired", self.summary.read_text())

    def test_node_auth_connection_and_source_rejection_are_distinct(self) -> None:
        auth = Exception("User was rejected by the SOCKS5 server " + self.NODE)
        auth.code = 97
        connection = Exception("Failed to connect to " + self.NODE)
        connection.code = 7
        self.get.return_value.text = "\n".join([self.NODE] * 4)
        self.client.get.side_effect = [auth, connection, Mock(status_code=403), Mock(status_code=200)]
        self.assertIsNotNone(self.resolve())
        for category in ("authentication_rejected", "connection_failed", "source_rejected (http_403)"):
            self.assertIn(category, self.output.getvalue())
        self.assertEqual(self.client.get.call_count, 4)
        self.assert_no_sensitive_output()

    def test_http_407_is_authentication_not_origin_rejection(self) -> None:
        self.client.get.return_value = Mock(status_code=407)
        self.assertIsNone(self.resolve())
        self.assertIn("authentication_rejected", self.summary.read_text())
        self.assertNotIn("source_rejected", self.summary.read_text())

    def test_handshake_error_without_auth_evidence_is_not_called_expired(self) -> None:
        error = Exception("SOCKS handshake failed " + self.NODE)
        error.code = 97
        self.assertEqual(fetcher._proxy_failure_category(error), "proxy_handshake_failed")

    def test_ten_node_bound_is_preserved(self) -> None:
        self.get.return_value.text = "\n".join([self.NODE] * 15)
        self.client.get.return_value = Mock(status_code=403)
        self.assertIsNone(self.resolve())
        self.assertEqual(self.client.get.call_count, 10)
        self.assertIn("source_rejected=10", self.summary.read_text())

    def test_transport_exceptions_and_selected_route_never_leak(self) -> None:
        detail = self.SECRET_URL + " " + self.NODE
        self.get.side_effect = requests.ConnectionError(detail)
        self.curl.return_value = Mock(returncode=7, stderr=detail)
        self.client.get.side_effect = Exception(detail)
        self.assertIsNone(self.resolve())
        for node in (self.NODE, "http://proxy-private.example:8080", "invalid-host"):
            print(fetcher.mask_proxy(node))
        self.assert_no_sensitive_output()

    def assert_no_sensitive_output(self) -> None:
        visible = self.output.getvalue() + (self.summary.read_text() if self.summary.exists() else "")
        for sensitive in ("subscription-private", "proxy-private", "user-secret", "password-secret", "token-secret"):
            self.assertNotIn(sensitive, visible)


if __name__ == "__main__":
    unittest.main()
