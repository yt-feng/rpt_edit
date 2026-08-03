#!/usr/bin/env python3
"""Regression tests for the Jianguoyun WebDAV sync client."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import requests

import sync_ops_videos_to_jianguoyun as sync


def response(
    status: int,
    body: str = "",
    *,
    headers: dict[str, str] | None = None,
    reason: str = "",
) -> requests.Response:
    result = requests.Response()
    result.status_code = status
    result._content = body.encode("utf-8")
    result.encoding = "utf-8"
    result.headers.update(headers or {})
    result.reason = reason
    result.url = "https://dav.example.test/dav/resource"
    return result


def propfind_xml(length: str | None, status: str = "HTTP/1.1 200 OK") -> str:
    property_xml = (
        f"<d:getcontentlength>{length}</d:getcontentlength>"
        if length is not None
        else "<d:displayname>video.mp4</d:displayname>"
    )
    return f"""<?xml version="1.0" encoding="utf-8" ?>
<d:multistatus xmlns:d="DAV:">
  <d:response>
    <d:href>/dav/Ops/video.mp4</d:href>
    <d:propstat>
      <d:prop>{property_xml}</d:prop>
      <d:status>{status}</d:status>
    </d:propstat>
  </d:response>
</d:multistatus>"""


def target() -> sync.WebDavTarget:
    result = sync.WebDavTarget("https://dav.example.test/dav", "user", "password", "/Ops")
    result.session = Mock()
    return result


class CollectionTests(unittest.TestCase):
    def test_ensure_collection_caches_shared_prefixes(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(405)

        webdav.ensure_collection(["2026-07-29", "BBG Show"])
        webdav.ensure_collection(["2026-07-29", "BBG Show"])
        webdav.ensure_collection(["2026-07-29", "Portal 娱乐"])

        urls = [item.args[1] for item in webdav.session.request.call_args_list]
        self.assertEqual(
            urls,
            [
                "https://dav.example.test/dav/Ops",
                "https://dav.example.test/dav/Ops/2026-07-29",
                "https://dav.example.test/dav/Ops/2026-07-29/BBG%20Show",
                "https://dav.example.test/dav/Ops/2026-07-29/Portal%20%E5%A8%B1%E4%B9%90",
            ],
        )

    def test_failed_collection_is_not_cached(self) -> None:
        webdav = target()
        webdav.session.request.side_effect = [response(201), response(403, "denied")]

        with self.assertRaisesRegex(RuntimeError, r"MKCOL failed \(403\)"):
            webdav.ensure_collection(["2026-07-29", "BBG Show"])

        webdav.session.request.side_effect = [response(201), response(201)]
        webdav.ensure_collection(["2026-07-29", "BBG Show"])
        urls = [item.args[1] for item in webdav.session.request.call_args_list]
        self.assertEqual(urls.count("https://dav.example.test/dav/Ops"), 1)
        self.assertEqual(urls.count("https://dav.example.test/dav/Ops/2026-07-29"), 2)


class RemoteSizeTests(unittest.TestCase):
    def test_same_and_different_sizes_use_propfind(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(207, propfind_xml("123"))

        self.assertTrue(webdav.has_same_size(["2026-07-29", "video.mp4"], 123))
        self.assertFalse(webdav.has_same_size(["2026-07-29", "video.mp4"], 124))

        request_call = webdav.session.request.call_args_list[0]
        self.assertEqual(request_call.args[0], "PROPFIND")
        self.assertEqual(request_call.kwargs["headers"]["Depth"], "0")
        self.assertIn(b"getcontentlength", request_call.kwargs["data"])

    def test_404_means_remote_file_is_missing(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(404)

        self.assertFalse(webdav.has_same_size(["video.mp4"], 123))

    def test_missing_size_property_stops_instead_of_uploading(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(207, propfind_xml(None))

        with self.assertRaisesRegex(RuntimeError, "getcontentlength.*video.mp4"):
            webdav.has_same_size(["video.mp4"], 123)

    def test_invalid_size_values_stop(self) -> None:
        for raw_size, message in (("not-a-number", "invalid"), ("-1", "negative")):
            with self.subTest(raw_size=raw_size):
                webdav = target()
                webdav.session.request.return_value = response(207, propfind_xml(raw_size))
                with self.assertRaisesRegex(RuntimeError, message):
                    webdav.has_same_size(["video.mp4"], 123)

    def test_failed_size_propstat_stops(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(
            207,
            propfind_xml("123", "HTTP/1.1 404 Not Found"),
        )

        with self.assertRaisesRegex(RuntimeError, "404 Not Found"):
            webdav.has_same_size(["video.mp4"], 123)

    def test_valid_size_wins_when_unrelated_property_fails(self) -> None:
        webdav = target()
        body = """<d:multistatus xmlns:d="DAV:"><d:response>
<d:propstat><d:prop><d:displayname /></d:prop><d:status>HTTP/1.1 404 Not Found</d:status></d:propstat>
<d:propstat><d:prop><d:getcontentlength>123</d:getcontentlength></d:prop><d:status>HTTP/1.1 200 OK</d:status></d:propstat>
</d:response></d:multistatus>"""
        webdav.session.request.return_value = response(207, body)

        self.assertTrue(webdav.has_same_size(["video.mp4"], 123))

    def test_malformed_xml_stops(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(207, "<not-closed>")

        with self.assertRaisesRegex(RuntimeError, "invalid XML.*video.mp4"):
            webdav.has_same_size(["video.mp4"], 123)

    def test_non_multistatus_error_includes_server_detail(self) -> None:
        webdav = target()
        webdav.session.request.return_value = response(
            403,
            "<error>\n  temporarily denied  </error>",
            headers={"Retry-After": "30"},
            reason="Forbidden",
        )

        with self.assertRaises(RuntimeError) as raised:
            webdav.has_same_size(["video.mp4"], 123)
        message = str(raised.exception)
        self.assertIn("403 Forbidden", message)
        self.assertIn("retry-after=30", message)
        self.assertIn("response=<error> temporarily denied </error>", message)


class UploadTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp_dir = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp_dir.cleanup)
        self.local_path = Path(self.temp_dir.name) / "video.mp4"
        self.payload = b"complete-video-payload"
        self.local_path.write_bytes(self.payload)

    def test_success_statuses_do_not_retry(self) -> None:
        for status in (200, 201, 204):
            with self.subTest(status=status):
                webdav = target()
                webdav.session.put.return_value = response(status)
                webdav.upload(self.local_path, ["video.mp4"])
                webdav.session.put.assert_called_once()
                self.assertEqual(
                    webdav.session.put.call_args.kwargs["headers"]["Content-Length"],
                    str(len(self.payload)),
                )

    def test_retryable_upload_reopens_the_complete_file(self) -> None:
        webdav = target()
        replies = iter([response(503, "busy"), response(201)])
        payloads: list[bytes] = []

        def put(*_args: object, **kwargs: object) -> requests.Response:
            payloads.append(kwargs["data"].read())  # type: ignore[union-attr]
            return next(replies)

        webdav.session.put.side_effect = put
        with patch.object(sync.time, "sleep") as sleep:
            webdav.upload(self.local_path, ["video.mp4"])

        self.assertEqual(payloads, [self.payload, self.payload])
        sleep.assert_called_once_with(1.0)

    def test_transport_error_reopens_the_complete_file(self) -> None:
        webdav = target()
        attempts = 0
        successful_payloads: list[bytes] = []

        def put(*_args: object, **kwargs: object) -> requests.Response:
            nonlocal attempts
            attempts += 1
            if attempts == 1:
                raise requests.ReadTimeout("simulated upload timeout")
            successful_payloads.append(kwargs["data"].read())  # type: ignore[union-attr]
            return response(201)

        webdav.session.put.side_effect = put
        with patch.object(sync.time, "sleep") as sleep:
            webdav.upload(self.local_path, ["video.mp4"])

        self.assertEqual(attempts, 2)
        self.assertEqual(successful_payloads, [self.payload])
        sleep.assert_called_once_with(1.0)

    def test_retry_after_is_honored_for_429(self) -> None:
        webdav = target()
        webdav.session.put.side_effect = [
            response(429, headers={"Retry-After": "7"}),
            response(204),
        ]

        with patch.object(sync.time, "sleep") as sleep:
            webdav.upload(self.local_path, ["video.mp4"])

        sleep.assert_called_once_with(7.0)

    def test_retry_stops_at_attempt_limit(self) -> None:
        webdav = target()
        webdav.session.put.return_value = response(503, "still busy")

        with patch.object(sync.time, "sleep") as sleep:
            with self.assertRaisesRegex(RuntimeError, r"PUT failed \(503\)"):
                webdav.upload(self.local_path, ["video.mp4"])

        self.assertEqual(webdav.session.put.call_count, sync.UPLOAD_MAX_ATTEMPTS)
        self.assertEqual(sleep.call_count, sync.UPLOAD_MAX_ATTEMPTS - 1)

    def test_403_is_not_retried_and_reports_bounded_body(self) -> None:
        webdav = target()
        server_body = "denied\n" + ("x" * 500)
        webdav.session.put.return_value = response(403, server_body, reason="Forbidden")

        with patch.object(sync.time, "sleep") as sleep:
            with self.assertRaises(RuntimeError) as raised:
                webdav.upload(self.local_path, ["folder", "video.mp4"])

        message = str(raised.exception)
        self.assertEqual(webdav.session.put.call_count, 1)
        sleep.assert_not_called()
        self.assertIn("403 Forbidden", message)
        self.assertIn("folder/video.mp4", message)
        self.assertNotIn("\n", message)
        self.assertTrue(message.endswith("..."))
        self.assertLess(len(message), 450)


if __name__ == "__main__":
    unittest.main()
