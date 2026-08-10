#!/usr/bin/env python3
"""Regression tests for resilient Dropbox PDF downloads."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

import download_dropbox_latest_pdfs as downloader


class FakeResponse:
    def __init__(
        self,
        status_code: int,
        *,
        content: bytes = b"",
        text: str = "",
        headers: dict[str, str] | None = None,
    ) -> None:
        self.status_code = status_code
        self.content = content
        self.text = text
        self.headers = headers or {}
        self.closed = False

    def close(self) -> None:
        self.closed = True


class DropboxDownloadRetryTests(unittest.TestCase):
    @patch("download_dropbox_latest_pdfs.time.sleep")
    @patch("download_dropbox_latest_pdfs.requests.post")
    def test_retries_http_500_then_writes_pdf(self, post: Mock, sleep: Mock) -> None:
        failed = FakeResponse(500, text="Dropbox temporary error")
        success = FakeResponse(200, content=b"%PDF-test")
        post.side_effect = [failed, success]

        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "report.pdf"
            downloader.download_file("token", "/reports/report.pdf", target)

            self.assertEqual(target.read_bytes(), b"%PDF-test")

        self.assertEqual(post.call_count, 2)
        self.assertTrue(failed.closed)
        self.assertTrue(success.closed)
        sleep.assert_called_once_with(2.0)

    @patch("download_dropbox_latest_pdfs.time.sleep")
    @patch("download_dropbox_latest_pdfs.requests.post")
    def test_honors_retry_after_for_rate_limit(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = [
            FakeResponse(429, text="busy", headers={"Retry-After": "45"}),
            FakeResponse(200, content=b"%PDF-test"),
        ]

        with tempfile.TemporaryDirectory() as temporary:
            downloader.download_file(
                "token",
                "/reports/report.pdf",
                Path(temporary) / "report.pdf",
            )

        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(45.0)

    def test_caps_unreasonable_retry_after(self) -> None:
        response = FakeResponse(429, headers={"Retry-After": "3600"})

        delay = downloader.download_retry_delay(1, response)

        self.assertEqual(delay, downloader.DOWNLOAD_RETRY_AFTER_MAX_SECONDS)

    @patch("download_dropbox_latest_pdfs.time.sleep")
    @patch("download_dropbox_latest_pdfs.requests.post")
    def test_retries_timeout_then_writes_pdf(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = [
            requests.exceptions.Timeout("timed out"),
            FakeResponse(200, content=b"%PDF-test"),
        ]

        with tempfile.TemporaryDirectory() as temporary:
            target = Path(temporary) / "report.pdf"
            downloader.download_file("token", "/reports/report.pdf", target)

            self.assertEqual(target.read_bytes(), b"%PDF-test")

        self.assertEqual(post.call_count, 2)
        sleep.assert_called_once_with(2.0)

    @patch("download_dropbox_latest_pdfs.time.sleep")
    @patch("download_dropbox_latest_pdfs.requests.post")
    def test_does_not_retry_permanent_dropbox_error(self, post: Mock, sleep: Mock) -> None:
        post.return_value = FakeResponse(409, text="path/not_found")

        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(RuntimeError, "HTTP 409"):
                downloader.download_file(
                    "token",
                    "/reports/missing.pdf",
                    Path(temporary) / "missing.pdf",
                )

        post.assert_called_once()
        sleep.assert_not_called()

    @patch("download_dropbox_latest_pdfs.time.sleep")
    @patch("download_dropbox_latest_pdfs.requests.post")
    def test_stops_at_retry_attempt_limit(self, post: Mock, sleep: Mock) -> None:
        post.side_effect = [
            FakeResponse(503, text="temporary")
            for _ in range(downloader.DOWNLOAD_MAX_ATTEMPTS)
        ]

        with tempfile.TemporaryDirectory() as temporary:
            with self.assertRaisesRegex(RuntimeError, "HTTP 503"):
                downloader.download_file(
                    "token",
                    "/reports/report.pdf",
                    Path(temporary) / "report.pdf",
                )

        self.assertEqual(post.call_count, downloader.DOWNLOAD_MAX_ATTEMPTS)
        self.assertEqual(
            [call.args[0] for call in sleep.call_args_list],
            [2.0, 4.0],
        )


if __name__ == "__main__":
    unittest.main(verbosity=2)
