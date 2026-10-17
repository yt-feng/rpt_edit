"""Offline fake-upstream tests. No account key or live API is used."""
import contextlib
from email.message import Message
import io
import hashlib
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
import urllib.error
import urllib.parse
import urllib.request

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
sys.path.insert(0, str(SCRIPTS))
from content_client import Client, ClientError, FILE_LIMIT, JSON_LIMIT, NoRedirect, TEXT_LIMIT, invoke, main, validate_origin

RID = "a" * 24
AID = "b" * 64
KEY = "kcd_live_" + "1" * 24 + "." + "2" * 64


class Response(io.BytesIO):
    def __init__(self, raw, mime="application/json", length="auto", **headers):
        super().__init__(raw)
        self.status = 200
        self.headers = Message()
        self.headers["Content-Type"] = mime
        if length is not None:
            self.headers["Content-Length"] = str(len(raw) if length == "auto" else length)
        for key, value in headers.items():
            self.headers[key] = value
        self.url = ""

    def geturl(self):
        return self.url


class FakeOpener:
    def __init__(self, *responses):
        self.responses = list(responses)
        self.requests = []

    def open(self, request, timeout):
        self.requests.append((request, timeout))
        response = self.responses.pop(0)
        if isinstance(response, Exception):
            raise response
        response.url = response.url or request.full_url
        return response


class ClientTests(unittest.TestCase):
    def client(self, *responses, **kwargs):
        self.opener = FakeOpener(*responses)
        return Client(api_key=KEY, opener=self.opener, base_url="https://api.example.invalid", **kwargs)

    def test_search_encodes_query_cursor_and_preserves_pagination(self):
        client = self.client(Response(b'{"items":[],"next_cursor":"next=="}'))
        result = client.search_reports(q="AI & 电力", date="2026-10-17", cursor="abc+/=", limit=100)
        request, timeout = self.opener.requests[0]
        self.assertEqual(request.get_method(), "GET")
        self.assertEqual(request.get_header("Authorization"), "Bearer " + KEY)
        self.assertEqual(urllib.parse.parse_qs(urllib.parse.urlsplit(request.full_url).query)["q"], ["AI & 电力"])
        self.assertEqual(result["next_cursor"], "next==")
        self.assertEqual(timeout, 30)

    def test_invalid_ids_filters_types_and_dates_never_reach_upstream(self):
        client = self.client()
        calls = [("content_get_report", {"report_id": "../private"}),
                 ("content_search_reports", {"limit": True}),
                 ("content_search_reports", {"limit": 101}),
                 ("content_search_reports", {"date": "2026-02-31"}),
                 ("content_search_reports", {"url": "https://other.invalid"}),
                 ("content_download", {"report_id": RID, "artifact_id": False}),
                 ("content_read_artifact", {"report_id": RID, "artifact_id": "x/y"}),
                 ("content_list_artifacts", {"report_id": RID, "language": "zh-CN\n"})]
        for name, args in calls:
            with self.subTest(name=name, args=args), self.assertRaises(ClientError):
                invoke(client, name, args)
        self.assertEqual(self.opener.requests, [])

    def test_origin_rejects_credentials_paths_and_non_https(self):
        for origin in ["http://api.example.invalid", "https://u:p@api.example.invalid", "https://api.example.invalid/api", "https://api.example.invalid?x=1", "https://api.example.invalid#x", "https://api.example.invalid:444", "https://api.example.invalid\\@evil.test", "https://api.example.invalid\n"]:
            with self.subTest(origin=origin), self.assertRaises(ClientError):
                validate_origin(origin)
        self.assertEqual(validate_origin("https://api.example.invalid/"), "https://api.example.invalid")

    def test_redirect_handler_never_forwards_bearer(self):
        handler = NoRedirect()
        request = urllib.request.Request("https://api.example.invalid/api/content/v1/reports", headers={"Authorization": "Bearer " + KEY})
        for target in ["https://evil.test/steal", "https://api.example.invalid/another", "http://api.example.invalid/"]:
            with self.assertRaisesRegex(ClientError, "redirect_refused"):
                handler.redirect_request(request, None, 302, "Found", {}, target)
        response = Response(b"{}")
        response.url = "https://evil.test/"
        with self.assertRaisesRegex(ClientError, "redirect_refused"):
            self.client(response).get_report(RID)
        self.assertTrue(response.closed)

    def test_missing_key_and_capabilities_have_no_network_dependency(self):
        opener = FakeOpener()
        with self.assertRaisesRegex(ClientError, "missing_api_key"):
            Client(api_key="", opener=opener).get_report(RID)
        with contextlib.redirect_stdout(io.StringIO()) as output:
            self.assertEqual(main(["capabilities"]), 0)
        self.assertEqual(len(json.loads(output.getvalue())["tools"]), 6)
        self.assertEqual(opener.requests, [])

    def test_errors_and_reflected_content_do_not_expose_key(self):
        headers = Message()
        headers["Retry-After"] = "60"
        error = urllib.error.HTTPError("https://api.example.invalid", 429, KEY, headers,
            io.BytesIO(json.dumps({"error": "rate_limited", "detail": KEY}).encode()))
        with self.assertRaises(ClientError) as raised:
            self.client(error).get_report(RID)
        self.assertEqual(raised.exception.result()["error"], "rate_limited")
        self.assertEqual(raised.exception.result()["retry_after_seconds"], 60)
        result = self.client(Response(json.dumps({"value": KEY}).encode())).get_report(RID)
        self.assertNotIn(KEY, json.dumps(result))
        reflected = self.client(Response(KEY.encode(), "text/plain")).read_artifact(RID, AID, max_chars=20)
        self.assertEqual(reflected["text"], "[REDACTED]")
        with contextlib.redirect_stderr(io.StringIO()) as output, self.assertRaises(SystemExit):
            main(["--api-key", KEY])
        self.assertNotIn(KEY, output.getvalue())

    def test_json_size_content_encoding_and_truncated_body_limits(self):
        responses = [Response(b"{}", length=JSON_LIMIT + 1), Response(b"x" * (JSON_LIMIT + 1), length=None),
                     Response(b"{}", length=100), Response(b"{}", **{"Content-Encoding": "gzip"})]
        for response in responses:
            with self.subTest(response=response), self.assertRaises(ClientError):
                self.client(response).get_report(RID)
            self.assertTrue(response.closed)

    def test_revoked_grant_preserves_api_permission_denied(self):
        headers = Message()
        error = urllib.error.HTTPError("https://api.example.invalid", 403, "Forbidden", headers,
            io.BytesIO(b'{"ok":false,"error":"api_permission_denied"}'))
        with self.assertRaises(ClientError) as raised:
            invoke(self.client(error), "content_get_report", {"report_id": RID})
        self.assertEqual(raised.exception.result(), {"ok": False, "error": "api_permission_denied",
            "status": 403, "api_requests": {"attempted": 1, "http_200": 0}})

    def test_utf8_prefix_truncation_and_excerpt_are_explicit(self):
        raw = ("中国" * TEXT_LIMIT).encode()
        result = self.client(Response(raw, "text/plain")).read_artifact(RID, "extracted-text", max_chars=7)
        self.assertTrue(result["truncated"])
        self.assertEqual(result["text"], "中国中国中国中")
        self.assertEqual(result["returned_chars"], 7)
        self.assertEqual(result["source_bytes"], len(raw))
        self.assertEqual(result["text_scope"], "partial_excerpt")
        self.assertEqual(result["api_source_url"], f"https://api.example.invalid/api/content/v1/reports/{RID}/artifacts/extracted-text")

    def test_text_reader_rejects_binary(self):
        with self.assertRaisesRegex(ClientError, "binary_artifact_use_download"):
            self.client(Response(b"%PDF", "application/pdf")).read_artifact(RID, AID)

    def test_download_ignores_remote_filename_and_returns_real_hash(self):
        with tempfile.TemporaryDirectory() as root:
            response = Response(b"%PDF-test", "application/pdf", **{"Content-Disposition": 'attachment; filename="../../escape"'})
            result = self.client(response, download_dir=root).download(RID)
            output = Path(result["path"])
            self.assertEqual(output.parent, Path(root).resolve())
            self.assertEqual(output.suffix, ".pdf")
            self.assertEqual(output.read_bytes(), b"%PDF-test")
            self.assertEqual(result["bytes"], 9)
            self.assertEqual(result["computed_sha256"], hashlib.sha256(b"%PDF-test").hexdigest())
            self.assertFalse(result["manifest_hash_verified"])
            self.assertEqual(output.stat().st_mode & 0o777, 0o600)

    def test_partial_oversize_or_mismatched_download_leaves_no_file(self):
        with tempfile.TemporaryDirectory() as root:
            for response in [Response(b"%PDF", "application/pdf", length=20),
                             Response(b"%PDF", "application/pdf", length=2),
                             Response(b"", "application/pdf", length=FILE_LIMIT + 1)]:
                with self.assertRaises(ClientError):
                    self.client(response, download_dir=root).download(RID)
                self.assertEqual(list(Path(root).iterdir()), [])

    def test_five_routes_are_exact_and_no_mutation_methods_exist(self):
        client = self.client(*[Response(b"{}") for _ in range(3)])
        client.get_report(RID)
        client.list_artifacts(RID, kind="translation", language="zh")
        client.get_metadata(RID)
        urls = [urllib.parse.urlsplit(req.full_url).path for req, _ in self.opener.requests]
        self.assertEqual(urls, [f"/api/content/v1/reports/{RID}", f"/api/content/v1/reports/{RID}/artifacts", f"/api/content/v1/reports/{RID}/artifacts/report-metadata"])
        self.assertEqual(urllib.parse.parse_qs(urllib.parse.urlsplit(self.opener.requests[1][0].full_url).query)["language"], ["zh"])

    def test_request_counts_distinguish_local_validation_http_success_and_failure(self):
        client = self.client(Response(b"{}"), urllib.error.URLError("private transport detail"), Response(b"invalid JSON"))
        self.assertEqual(invoke(client, "content_get_report", {"report_id": RID})["api_requests"], {"attempted": 1, "http_200": 1})
        for expected in [{"attempted": 1, "http_200": 0}, {"attempted": 1, "http_200": 1}]:
            with self.assertRaises(ClientError) as raised:
                invoke(client, "content_get_report", {"report_id": RID})
            self.assertEqual(raised.exception.result()["api_requests"], expected)
        with self.assertRaises(ClientError) as raised:
            invoke(client, "content_get_report", {"report_id": "invalid"})
        self.assertEqual(raised.exception.result()["api_requests"], {"attempted": 0, "http_200": 0})


if __name__ == "__main__":
    unittest.main()
