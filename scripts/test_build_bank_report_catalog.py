#!/usr/bin/env python3
"""Regression tests for resilient Dropbox metadata and content requests."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

import build_bank_report_catalog as catalog
import portal_suite_catalog as portal_catalog


class FakeResponse:
    def __init__(
        self,
        status_code: int,
        *,
        json_data: object | None = None,
        text: str = "",
        headers: dict[str, str] | None = None,
        chunks: list[bytes] | Exception | None = None,
    ) -> None:
        self.status_code = status_code
        self.json_data = json_data
        self.text = text
        self.headers = headers or {}
        self.chunks = chunks if chunks is not None else []
        self.closed = False

    def json(self) -> object:
        if isinstance(self.json_data, Exception):
            raise self.json_data
        return self.json_data

    def iter_content(self, chunk_size: int) -> list[bytes]:
        self.chunk_size = chunk_size
        if isinstance(self.chunks, Exception):
            raise self.chunks
        return self.chunks

    def close(self) -> None:
        self.closed = True


class DropboxRequestRetryTests(unittest.TestCase):
    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_retries_typed_other_403_then_returns_metadata(self, post: Mock, sleep: Mock) -> None:
        failed = FakeResponse(
            403,
            json_data={
                "error": {".tag": "other"},
                "user_message": {
                    "text": "Access denied for spiffe://prod.dbxnw.net/service/envoy-edge"
                },
            },
            text='{"error":{".tag":"other"},"user_message":{"text":"spiffe://prod.dbxnw.net/service/envoy-edge"}}',
            headers={"X-Dropbox-Request-Id": "request-403"},
        )
        success = FakeResponse(200, json_data={"entries": [], "has_more": False})
        post.side_effect = [failed, success]

        with patch.object(catalog, "log") as logger:
            result = catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        self.assertEqual(result, {"entries": [], "has_more": False})
        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(5.0)
        self.assertTrue(
            any("request_id=request-403" in str(call) for call in logger.call_args_list)
        )
        self.assertTrue(failed.closed)
        self.assertTrue(success.closed)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_does_not_retry_explicit_permanent_403(self, post: Mock, sleep: Mock) -> None:
        response = FakeResponse(
            403,
            json_data={"error": {".tag": "missing_scope"}},
            text='{"error":{".tag":"missing_scope"}}',
            headers={"X-Dropbox-Request-Id": "request-scope"},
        )
        post.return_value = response

        with self.assertRaisesRegex(RuntimeError, "HTTP 403.*request-scope"):
            catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        post.assert_called_once()
        sleep.assert_not_called()
        self.assertTrue(response.closed)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_does_not_retry_unclassified_other_403(self, post: Mock, sleep: Mock) -> None:
        response = FakeResponse(
            403,
            json_data={"error": {".tag": "other"}},
            text='{"error":{".tag":"other"}}',
        )
        post.return_value = response

        with self.assertRaisesRegex(RuntimeError, "HTTP 403"):
            catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        post.assert_called_once()
        sleep.assert_not_called()
        self.assertTrue(response.closed)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_honors_retry_after_for_rate_limit(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = [
            FakeResponse(429, json_data={}, text="busy", headers={"Retry-After": "45"}),
            FakeResponse(200, json_data={"entries": []}),
        ]

        catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        sleep.assert_called_once_with(45.0)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_retries_timeout_then_returns_metadata(self, post: Mock, sleep: Mock) -> None:
        success = FakeResponse(200, json_data={"entries": []})
        post.side_effect = [requests.exceptions.Timeout("timed out"), success]

        result = catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        self.assertEqual(result, {"entries": []})
        sleep.assert_called_once_with(5.0)
        self.assertTrue(success.closed)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_list_folder_continue_retries_internal_403(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = [
            FakeResponse(
                200,
                json_data={
                    "entries": [{"id": "first"}],
                    "has_more": True,
                    "cursor": "cursor-1",
                },
            ),
            FakeResponse(
                403,
                json_data={
                    "error": {".tag": "other"},
                    "user_message": {
                        "text": "spiffe://prod.dbxnw.net/service/envoy-edge"
                    },
                },
                text="spiffe://prod.dbxnw.net/service/envoy-edge",
            ),
            FakeResponse(
                200,
                json_data={"entries": [{"id": "second"}], "has_more": False},
            ),
        ]

        result = catalog.list_folder("token", "/zip_backup")

        self.assertEqual(result, [{"id": "first"}, {"id": "second"}])
        self.assertEqual(post.call_count, 3)
        self.assertTrue(post.call_args_list[1].args[0].endswith("/files/list_folder/continue"))
        sleep.assert_called_once_with(5.0)

    @patch("build_bank_report_catalog.time.sleep")
    @patch("build_bank_report_catalog.requests.post")
    def test_stops_after_bounded_transient_attempts(self, post: Mock, sleep: Mock) -> None:
        responses = [
            FakeResponse(503, json_data={}, text="temporary")
            for _ in range(catalog.DROPBOX_REQUEST_MAX_ATTEMPTS)
        ]
        post.side_effect = responses

        with self.assertRaisesRegex(RuntimeError, "after 5 attempts.*HTTP 503"):
            catalog.api_post("token", "/files/list_folder", {"path": "/zip_backup"})

        self.assertEqual(post.call_count, catalog.DROPBOX_REQUEST_MAX_ATTEMPTS)
        self.assertEqual(
            [call.args[0] for call in sleep.call_args_list],
            [5.0, 10.0, 20.0, 40.0],
        )
        self.assertTrue(all(response.closed for response in responses))

    @patch("portal_suite_catalog.dropbox_post_with_retry")
    def test_portal_content_download_uses_shared_resilient_request(self, request: Mock) -> None:
        response = FakeResponse(200, chunks=[b"%PDF-", b"test"])
        request.return_value = response

        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "report.pdf"
            portal_catalog.download_dropbox_file("token", "/reports/report.pdf", target)
            self.assertEqual(target.read_bytes(), b"%PDF-test")

        request.assert_called_once()
        self.assertTrue(response.closed)

    @patch("portal_suite_catalog.time.sleep")
    @patch("portal_suite_catalog.dropbox_post_with_retry")
    def test_portal_content_download_restarts_after_stream_interruption(
        self, request: Mock, sleep: Mock
    ) -> None:
        interrupted = FakeResponse(
            200,
            chunks=requests.exceptions.ChunkedEncodingError("stream interrupted"),
        )
        success = FakeResponse(200, chunks=[b"%PDF-restarted"])
        request.side_effect = [interrupted, success]

        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "report.pdf"
            portal_catalog.download_dropbox_file("token", "/reports/report.pdf", target)
            self.assertEqual(target.read_bytes(), b"%PDF-restarted")
            self.assertFalse((target.parent / ".report.pdf.part").exists())

        self.assertEqual(request.call_count, 2)
        sleep.assert_called_once_with(5.0)
        self.assertTrue(interrupted.closed)
        self.assertTrue(success.closed)


if __name__ == "__main__":
    unittest.main(verbosity=2)
