#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import hashlib
import io
import subprocess
import tempfile
import unittest
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from unittest.mock import Mock, patch

from fetch_release_asset import FetchError, fetch_release_asset, main


class FetchReleaseAssetTests(unittest.TestCase):
    def setUp(self) -> None:
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.directory = Path(self.temp.name)
        self.output = self.directory / "catalog.json"
        self.output.write_bytes(b"previous accepted catalog")
        self.headers = self.directory / "catalog.headers"
        self.headers.write_bytes(b"previous accepted headers")
        self.logger = Mock()
        self.run = self.enterContext(patch("fetch_release_asset.subprocess.run"))
        self.sleep = self.enterContext(patch("fetch_release_asset.time.sleep"))

    def fetch(self, **options):
        defaults = {"label": "public catalog", "logger": self.logger}
        defaults.update(options)
        return fetch_release_asset(
            "https://example.test/catalog.json?credential=secret", self.output, **defaults,
        )

    def response(self, *, status=200, body=b'{"reports":[]}', code=0, headers=""):
        def complete(command, **kwargs):
            # A retry must never expose its partial body/header as accepted data.
            self.assertEqual(self.output.read_bytes(), b"previous accepted catalog")
            self.assertEqual(self.headers.read_bytes(), b"previous accepted headers")
            Path(command[command.index("--output") + 1]).write_bytes(body)
            Path(command[command.index("--dump-header") + 1]).write_text(
                f"HTTP/2 {status}\r\n{headers}\r\n", encoding="iso-8859-1",
            )
            return subprocess.CompletedProcess(command, code, str(status), "error with credential=secret")
        return complete

    def responses(self, *responses):
        remaining = iter(responses)
        self.run.side_effect = lambda *args, **kwargs: next(remaining)(*args, **kwargs)

    def assert_previous_preserved(self):
        self.assertEqual(self.output.read_bytes(), b"previous accepted catalog")
        self.assertEqual(self.headers.read_bytes(), b"previous accepted headers")
        self.assertFalse(list(self.directory.glob(".fetch-*")))

    def test_complete_compressed_request_atomically_installs_body_and_headers(self):
        self.run.side_effect = self.response(headers="Content-Language: zh-CN\r\n")
        result = self.fetch(validate_json=True, dump_header=self.headers)
        self.assertEqual(self.output.read_bytes(), b'{"reports":[]}')
        self.assertIn("Content-Language: zh-CN", self.headers.read_text())
        self.assertEqual(result.http_status, 200)
        self.assertEqual(result.attempts, 1)
        command = self.run.call_args.args[0]
        self.assertIn("--compressed", command)
        self.assertIn("--globoff", command)
        self.assertEqual(command[:2], ["curl", "--disable"])
        self.assertNotIn("--location", command)
        self.assertEqual(command[command.index("--max-redirs") + 1], "0")
        self.assertEqual(command[command.index("--max-time") + 1], "120")
        self.assertIn("Cache-Control: no-cache", command)
        self.sleep.assert_not_called()
        self.assertFalse(list(self.directory.glob(".fetch-*")))

    def test_timeout_with_partial_200_then_complete_success(self):
        self.responses(self.response(code=28, body=b'{"reports":['), self.response())
        result = self.fetch(validate_json=True)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(self.output.read_bytes(), b'{"reports":[]}')
        self.sleep.assert_called_once_with(3)

    def test_incomplete_body_curl_18_retries_and_does_not_accept_valid_json_prefix(self):
        self.responses(self.response(code=18, body=b'{}'), self.response())
        result = self.fetch(validate_json=True)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(self.output.read_bytes(), b'{"reports":[]}')

    def test_exhausted_partial_transfers_preserve_existing_files(self):
        self.run.side_effect = self.response(code=28, body=b'partial')
        with self.assertRaisesRegex(FetchError, "curl exit 28.*3/3"):
            self.fetch(dump_header=self.headers)
        self.assertEqual(self.run.call_count, 3)
        self.assertEqual([call.args[0] for call in self.sleep.call_args_list], [3, 6])
        self.assert_previous_preserved()

    def test_invalid_json_and_empty_200_are_never_accepted(self):
        for payload in (b"", b'{"reports":[', b"<html>maintenance</html>", b'{"value":NaN}'):
            with self.subTest(payload=payload):
                self.run.reset_mock()
                self.run.side_effect = self.response(body=payload)
                with self.assertRaises(FetchError):
                    self.fetch(validate_json=True, attempts=2)
                self.assertEqual(self.run.call_count, 2)
                self.assert_previous_preserved()

    def test_stale_valid_json_200_retries_until_exact_expected_release(self):
        expected = self.directory / "expected.json"
        expected.write_bytes(b'{"build":"new"}')
        self.responses(
            self.response(body=b'{"build":"old"}'),
            self.response(body=expected.read_bytes()),
        )
        result = self.fetch(expected_file=expected, validate_json=True)
        self.assertEqual(result.attempts, 2)
        self.assertEqual(self.output.read_bytes(), expected.read_bytes())
        self.assertIn("SHA256 mismatch", str(self.logger.call_args_list))

    def test_stale_expected_bytes_fail_closed_after_retry_limit(self):
        self.run.side_effect = self.response(body=b'{"old":true}')
        with self.assertRaisesRegex(FetchError, "byte count mismatch"):
            self.fetch(expected_bytes=100, attempts=2)
        self.assert_previous_preserved()

    def test_explicit_digest_and_byte_count_accept_only_matching_body(self):
        payload = b'{"reports":[]}'
        self.run.side_effect = self.response(body=payload)
        result = self.fetch(
            expected_bytes=len(payload), expect_sha256=hashlib.sha256(payload).hexdigest().upper(),
        )
        self.assertEqual(result.bytes_written, len(payload))

    def test_transient_http_errors_retry_and_retry_after_is_capped(self):
        for status in (408, 425, 429, 500, 502, 503, 504, 599):
            with self.subTest(status=status):
                self.output.write_bytes(b"previous accepted catalog")
                self.sleep.reset_mock()
                self.responses(self.response(status=status, headers="Retry-After: 600\r\n"), self.response())
                result = self.fetch(max_retry_delay=17)
                self.assertEqual(result.attempts, 2)
                self.sleep.assert_called_once_with(17)

    def test_retry_after_http_date_is_honored_and_bounded(self):
        retry_at = format_datetime(datetime.now(timezone.utc) + timedelta(minutes=5), usegmt=True)
        self.responses(self.response(status=503, headers=f"Retry-After: {retry_at}\r\n"), self.response())
        self.fetch(max_retry_delay=19)
        self.sleep.assert_called_once_with(19)

    def test_intermediate_header_retry_after_does_not_override_final_headers(self):
        self.responses(
            self.response(status=200, headers="Retry-After: 600\r\n\r\nHTTP/2 503\r\nRetry-After: 7\r\n", code=28),
            self.response(),
        )
        self.fetch()
        self.sleep.assert_called_once_with(7)

    def test_permanent_statuses_fail_immediately_and_do_not_follow_redirect(self):
        for status in (301, 302, 307, 308, 400, 401, 403, 404, 410, 422):
            with self.subTest(status=status):
                self.run.reset_mock()
                self.sleep.reset_mock()
                self.run.side_effect = self.response(status=status, headers="Location: https://other.test/\r\n")
                with self.assertRaisesRegex(FetchError, f"HTTP {status}.*1/3"):
                    self.fetch()
                self.run.assert_called_once()
                self.sleep.assert_not_called()
                self.assert_previous_preserved()

    def test_authorization_errors_fail_even_if_error_body_transfer_times_out(self):
        for status in (401, 403):
            with self.subTest(status=status):
                self.run.reset_mock()
                self.run.side_effect = self.response(status=status, code=28)
                with self.assertRaisesRegex(FetchError, f"HTTP {status}"):
                    self.fetch()
                self.run.assert_called_once()
                self.assert_previous_preserved()

    def test_propagation_404_is_retried_only_when_opted_in(self):
        self.responses(self.response(status=404), self.response())
        result = self.fetch(retry_404=True)
        self.assertEqual(result.attempts, 2)

    def test_allowed_missing_asset_leaves_existing_output_and_headers_untouched(self):
        self.run.side_effect = self.response(status=404)
        result = self.fetch(allow_missing=True, dump_header=self.headers)
        self.assertEqual(result.http_status, 404)
        self.assertEqual(result.bytes_written, 0)
        self.run.assert_called_once()
        self.assert_previous_preserved()

    def test_allowed_missing_can_wait_for_propagation_before_returning_404(self):
        self.run.side_effect = self.response(status=404)
        result = self.fetch(allow_missing=True, retry_404=True)
        self.assertEqual(result.http_status, 404)
        self.assertEqual(result.attempts, 3)
        self.assert_previous_preserved()

    def test_missing_option_does_not_accept_other_errors(self):
        self.run.side_effect = self.response(status=403)
        with self.assertRaisesRegex(FetchError, "HTTP 403"):
            self.fetch(allow_missing=True)
        self.run.assert_called_once()
        self.assert_previous_preserved()

    def test_maximum_size_applies_to_curl_and_decoded_bytes(self):
        self.run.side_effect = self.response(body=b'{"large":123456789}')
        with self.assertRaisesRegex(FetchError, "body exceeds maximum size"):
            self.fetch(max_bytes=10, validate_json=True)
        self.run.assert_called_once()
        command = self.run.call_args.args[0]
        self.assertEqual(command[command.index("--max-filesize") + 1], "10")
        self.assert_previous_preserved()

    def test_partial_content_status_is_never_accepted(self):
        self.run.side_effect = self.response(status=206, body=b'{}')
        with self.assertRaisesRegex(FetchError, "HTTP 206"):
            self.fetch(validate_json=True)
        self.assert_previous_preserved()

    def test_local_io_and_certificate_curl_errors_fail_immediately(self):
        for code in (23, 27, 60, 77):
            with self.subTest(code=code):
                self.run.reset_mock()
                self.run.side_effect = self.response(status=0, code=code)
                with self.assertRaisesRegex(FetchError, f"curl exit {code}"):
                    self.fetch()
                self.run.assert_called_once()
                self.assert_previous_preserved()

    def test_hung_subprocess_is_bounded_and_diagnostics_omit_url_or_stderr(self):
        self.run.side_effect = subprocess.TimeoutExpired("curl https://example.test/?secret", 125)
        with self.assertRaises(FetchError) as captured:
            self.fetch(attempts=2)
        self.assertEqual(self.run.call_count, 2)
        self.assertEqual(self.run.call_args.kwargs["timeout"], 125)
        diagnostics = str(captured.exception) + str(self.logger.call_args_list)
        self.assertNotIn("https://", diagnostics)
        self.assertNotIn("credential", diagnostics)
        self.assertNotIn("secret", diagnostics)
        self.assert_previous_preserved()

    def test_total_deadline_limits_curl_timeout_and_stops_further_attempts(self):
        with patch("fetch_release_asset.time.monotonic", side_effect=[0, 0, 6]):
            self.run.side_effect = self.response(code=28)
            with self.assertRaisesRegex(FetchError, "total time budget exhausted"):
                self.fetch(max_time=180, max_total_time=5)
        self.run.assert_called_once()
        command = self.run.call_args.args[0]
        self.assertEqual(command[command.index("--max-time") + 1], "5")
        self.assertEqual(self.run.call_args.kwargs["timeout"], 5)
        self.sleep.assert_not_called()
        self.assert_previous_preserved()

    def test_bad_options_fail_without_starting_transfer(self):
        for options in (
            {"label": "https://example.test/?secret"}, {"attempts": 0},
            {"max_time": float("inf")}, {"retry_delay": -1},
            {"max_total_time": 0}, {"expect_sha256": "bad"},
            {"expected_file": self.directory / "absent"},
            {"dump_header": self.output},
        ):
            with self.subTest(options=options), self.assertRaises(FetchError):
                self.fetch(**options)
        self.run.assert_not_called()
        self.assert_previous_preserved()

    def test_cli_status_stdout_is_machine_readable_and_errors_stay_on_stderr(self):
        self.run.side_effect = self.response(status=403)
        stdout, stderr = io.StringIO(), io.StringIO()
        with contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
            code = main([
                "--url", "https://example.test/?credential=secret", "--output", str(self.output),
                "--label", "public catalog", "--write-out-http-code",
            ])
        self.assertEqual(code, 1)
        self.assertEqual(stdout.getvalue(), "403\n")
        self.assertIn("HTTP 403", stderr.getvalue())
        self.assertNotIn("secret", stderr.getvalue())
        self.assert_previous_preserved()


if __name__ == "__main__":
    unittest.main()
