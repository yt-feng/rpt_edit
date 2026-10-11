#!/usr/bin/env python3
"""Offline behavior tests: fake HTTPS connections only, never a live download."""
import contextlib
import http.client
import io
import json
import os
from pathlib import Path
import signal
import ssl
import tempfile
import unittest
from unittest.mock import patch

import portal_download_smoke as smoke


class FakeResponse:
    def __init__(self, body=b"%PDF-1.7\nsynthetic fixture\n%%EOF", *, status=200, headers=None, chunk_size=3):
        self.status = status
        self.body = body
        self.headers = headers if headers is not None else [
            ("Content-Type", "application/pdf"), ("Content-Length", str(len(body))),
        ]
        self.chunk_size = chunk_size
        self.reads = []
        self.eof = False
        self.closed = False

    def getheaders(self):
        return self.headers

    def read(self, amount):
        self.reads.append(amount)
        chunk, self.body = self.body[:min(amount, self.chunk_size)], self.body[min(amount, self.chunk_size):]
        if not chunk:
            self.eof = True
        return chunk

    def close(self):
        self.closed = True


class FakeConnection:
    def __init__(self, response, *, failure=None):
        self.response = response
        self.failure = failure
        self.requests = []
        self.connected = False
        self.closed = False
        self.sock = self
        self.timeouts = []

    def connect(self):
        self.connected = True

    def settimeout(self, value):
        self.timeouts.append(value)

    def request(self, method, path, *, body, headers):
        self.requests.append((method, path, body, headers))
        if self.failure:
            raise self.failure

    def getresponse(self):
        return self.response

    def close(self):
        self.closed = True


class DownloadSmokeTests(unittest.TestCase):
    def setUp(self):
        self.response = FakeResponse()
        self.connection = FakeConnection(self.response)
        self.factories = []
        self.password = "  synthetic PRIVATE password \n"

    def factory(self, host, **kwargs):
        self.factories.append((host, kwargs))
        return self.connection

    def invoke(self, **kwargs):
        return smoke.download_smoke(self.password, connection_factory=self.factory, **kwargs)

    def fail(self, category, status=200):
        with self.assertRaises(smoke.SmokeFailure) as raised:
            self.invoke()
        self.assertEqual(raised.exception.category, category)
        self.assertEqual(raised.exception.status, status)
        self.assertTrue(self.connection.closed)
        return raised.exception

    def test_success_reads_declared_http_body_with_one_verified_canonical_post(self):
        expected = len(self.response.body)
        self.assertEqual(self.invoke(), {"http_status": 200, "pdf_magic_ok": True, "bytes_read": expected})
        self.assertTrue(self.response.eof)
        self.assertTrue(self.response.closed)
        self.assertTrue(self.connection.closed)
        self.assertEqual(len(self.factories), 1)
        host, options = self.factories[0]
        self.assertEqual(host, "kcdesk.com")
        self.assertEqual(options["timeout"], 20)
        self.assertTrue(options["context"].check_hostname)
        self.assertEqual(options["context"].verify_mode, ssl.CERT_REQUIRED)
        self.assertEqual(len(self.connection.requests), 1)
        method, path, body, headers = self.connection.requests[0]
        self.assertEqual((method, path), ("POST", "/api/download"))
        self.assertEqual(json.loads(body), {"id": "aabc619d832a0cf0fbb1b510", "password": self.password})
        self.assertEqual(headers, {"Content-Type": "application/json", "Accept": "application/pdf", "Accept-Encoding": "identity"})
        self.assertGreater(self.connection.timeouts[0], 0)
        self.assertLessEqual(self.connection.timeouts[0], 90)

    def test_redirect_auth_and_temporary_errors_never_read_body_follow_or_retry(self):
        for status in (301, 302, 303, 307, 308, 401, 403, 429, 500, 503):
            with self.subTest(status=status):
                self.setUp()
                self.response.status = status
                self.response.headers.append(("Location", "https://secret.invalid/private-token"))
                self.fail("http_status", status)
                self.assertEqual(len(self.connection.requests), 1)
                self.assertEqual(len(self.factories), 1)
                self.assertEqual(self.response.reads, [])

    def test_private_transport_exceptions_do_not_retry_or_expose_the_exception(self):
        for error, category in ((OSError("private address body token"), "transport"),
                                (ssl.SSLError("private certificate"), "tls"),
                                (TimeoutError("private request"), "timeout"),
                                (http.client.IncompleteRead(b"private PDF bytes"), "transport")):
            with self.subTest(category=category):
                self.setUp()
                self.connection.failure = error
                failure = self.fail(category, None)
                self.assertEqual(str(failure), category)
                self.assertEqual(len(self.connection.requests), 1)

    def test_oversized_declared_body_is_rejected_before_reading(self):
        self.response.headers[1] = ("Content-Length", str(smoke.MAX_BYTES + 1))
        self.fail("body_too_large")
        self.assertEqual(self.response.reads, [])

    def test_unframed_fake_stream_cannot_cross_size_cap(self):
        self.response = FakeResponse(b"%PDF-" + b"x" * smoke.MAX_BYTES,
                                     headers=[("Content-Type", "application/pdf"), ("Content-Length", str(smoke.MAX_BYTES))],
                                     chunk_size=smoke.CHUNK_BYTES)
        self.connection.response = self.response
        self.fail("body_too_large")
        self.assertEqual(self.response.reads[-1], 1)

    def test_truncated_or_unframed_fake_excess_body_is_rejected(self):
        for difference in (-1, 1):
            with self.subTest(difference=difference):
                self.setUp()
                self.response.headers[1] = ("Content-Length", str(len(self.response.body) + difference))
                self.fail("body_length")

    def test_invalid_mime_encoding_length_or_magic_fails_without_echoing_data(self):
        variants = [
            ([("Content-Type", "text/html private"), ("Content-Length", "5")], "content_type"),
            ([("Content-Type", "application/pdf"), ("Content-Encoding", "gzip"), ("Content-Length", "5")], "content_encoding"),
            ([("Content-Type", "application/pdf")], "content_length"),
            ([("Content-Type", "application/pdf"), ("Content-Length", "0")], "content_length"),
            ([("Content-Type", "application/pdf"), ("Content-Length", "secret")], "content_length"),
            ([("Content-Type", "application/pdf"), ("Content-Length", "5"), ("Content-Length", "5")], "content_length"),
            ([("Content-Type", "application/pdf"), ("Content-Length", "5"), ("Transfer-Encoding", "chunked")], "content_length"),
        ]
        for headers, category in variants:
            with self.subTest(category=category, headers=headers):
                self.setUp()
                self.response.headers = headers
                self.fail(category)
        self.setUp()
        self.response.body = b"PRIVATE document"
        self.response.headers[1] = ("Content-Length", str(len(self.response.body)))
        self.fail("pdf_magic")

    def test_missing_secret_fails_without_creating_a_connection(self):
        with self.assertRaisesRegex(smoke.SmokeFailure, "missing_password"):
            smoke.download_smoke("", connection_factory=self.factory)
        self.assertEqual(self.factories, [])

    def test_deadline_applies_across_many_body_reads(self):
        current = [0.0]
        original = self.response.read

        def slow_read(amount):
            current[0] += 31
            return original(amount)

        self.response.read = slow_read
        with self.assertRaises(smoke.SmokeFailure) as raised:
            self.invoke(clock=lambda: current[0])
        self.assertEqual(raised.exception.category, "deadline")
        self.assertEqual(raised.exception.status, 200)
        self.assertEqual(len(self.connection.requests), 1)
        self.assertEqual(len(self.response.reads), 3)

    def test_total_deadline_interrupts_a_blocked_system_call_and_restores_handler(self):
        previous = signal.getsignal(signal.SIGALRM)
        with self.assertRaises(smoke._DeadlineExpired):
            with smoke.total_deadline(0.01):
                signal.pause()
        self.assertEqual(signal.getsignal(signal.SIGALRM), previous)
        self.assertEqual(signal.getitimer(signal.ITIMER_REAL), (0.0, 0.0))

    def test_cli_and_job_summary_contain_only_fixed_fields_and_never_private_failure_text(self):
        for failure in (OSError("PRIVATE password headers body filename URL hash"),
                        smoke.SmokeFailure("http_status", 307),
                        smoke.SmokeFailure("PRIVATE unexpected category", "PRIVATE status")):
            with self.subTest(kind=type(failure).__name__), tempfile.TemporaryDirectory() as directory:
                summary = Path(directory) / "summary"
                with patch.dict(os.environ, {"PORTAL_DOWNLOAD_PASSWORD": self.password, "GITHUB_STEP_SUMMARY": str(summary)}), \
                        patch.object(smoke, "download_smoke", side_effect=failure), \
                        contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()) as errors:
                    self.assertEqual(smoke.main(), 1)
                result = json.loads(output.getvalue())
                self.assertEqual(set(result), {"http_status", "error"})
                self.assertIn(result["error"], smoke.ERRORS)
                payload = json.loads(summary.read_text().splitlines()[1])
                self.assertEqual(payload, {"result": result, "scope": smoke.SCOPE, "normal_side_effects": smoke.SIDE_EFFECTS})
                self.assertNotIn("PRIVATE", output.getvalue() + summary.read_text() + errors.getvalue())
                self.assertEqual(errors.getvalue(), "")

    def test_real_main_success_only_writes_summary_not_pdf(self):
        with tempfile.TemporaryDirectory() as directory:
            summary = Path(directory) / "summary"
            with patch.dict(os.environ, {"PORTAL_DOWNLOAD_PASSWORD": self.password, "GITHUB_STEP_SUMMARY": str(summary)}), \
                    patch.object(smoke.http.client, "HTTPSConnection", self.factory), \
                    contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertEqual(smoke.main(), 0)
            self.assertEqual(set(json.loads(output.getvalue())), {"http_status", "pdf_magic_ok", "bytes_read"})
            self.assertEqual(list(Path(directory).iterdir()), [summary])
            self.assertNotIn("synthetic", summary.read_text())
            self.assertNotIn("%PDF", summary.read_text())

    def test_real_main_rejects_private_error_response_without_reading_or_exposing_it(self):
        self.response.status = 503
        self.response.body = b"PRIVATE password and error body"
        self.response.headers = [("Location", "https://PRIVATE.invalid/token"),
                                 ("Content-Disposition", "attachment; filename=PRIVATE.pdf")]
        with tempfile.TemporaryDirectory() as directory:
            summary = Path(directory) / "summary"
            with patch.dict(os.environ, {"PORTAL_DOWNLOAD_PASSWORD": self.password, "GITHUB_STEP_SUMMARY": str(summary)}), \
                    patch.object(smoke.http.client, "HTTPSConnection", self.factory), \
                    contextlib.redirect_stdout(io.StringIO()) as output, contextlib.redirect_stderr(io.StringIO()) as errors:
                self.assertEqual(smoke.main(), 1)
            self.assertEqual(json.loads(output.getvalue()), {"http_status": 503, "error": "http_status"})
            self.assertEqual(self.response.reads, [])
            self.assertEqual(len(self.connection.requests), 1)
            self.assertEqual(list(Path(directory).iterdir()), [summary])
            self.assertNotIn("PRIVATE", output.getvalue() + summary.read_text() + errors.getvalue())
            self.assertEqual(errors.getvalue(), "")

    def test_workflow_is_manual_main_owner_only_with_one_secret_and_no_publish_or_notify(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/portal-download-smoke.yml").read_text()
        self.assertIn("workflow_dispatch:", workflow)
        self.assertIn("github.ref == 'refs/heads/main' && github.actor == github.repository_owner", workflow)
        self.assertIn("github.triggering_actor == github.repository_owner && github.run_attempt == '1'", workflow)
        self.assertIn("persist-credentials: false", workflow)
        self.assertIn("contents: read", workflow)
        self.assertEqual(workflow.count("secrets[vars.PORTAL_DOWNLOAD_SECRET_REF]"), 1)
        self.assertEqual(workflow.count("secrets"), 1)
        self.assertEqual(workflow.count("run: python3 -B scripts/portal_download_smoke.py"), 1)
        for forbidden in ("schedule:", "workflow_run:", "upload-artifact", "portal-ops-alert", "PASSWORD_SECRET", "wrangler", "deploy", "curl"):
            self.assertNotIn(forbidden, workflow)


if __name__ == "__main__":
    unittest.main()
