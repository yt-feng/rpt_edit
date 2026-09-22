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
    def test_selects_requested_date_folder_instead_of_latest(self) -> None:
        entries = [
            {".tag": "folder", "name": "20260825", "path_lower": "/zip_backup/20260825"},
            {".tag": "folder", "name": "20260826", "path_lower": "/zip_backup/20260826"},
        ]

        selected = downloader.select_date_folder(entries, "20260825")

        self.assertEqual(selected["name"], "20260825")

    def test_empty_requested_date_folder_keeps_latest_behavior(self) -> None:
        entries = [
            {".tag": "folder", "name": "20260825"},
            {".tag": "folder", "name": "20260826"},
        ]

        selected = downloader.select_date_folder(entries)

        self.assertEqual(selected["name"], "20260826")

    def test_expected_date_folder_rejects_stale_latest_selection(self) -> None:
        selected = {".tag": "folder", "name": "20260826"}

        with self.assertRaisesRegex(RuntimeError, "expected 20260827, selected latest folder 20260826"):
            downloader.validate_expected_date_folder(selected, "20260827")

    def test_expected_date_folder_accepts_matching_selection(self) -> None:
        selected = {".tag": "folder", "name": "20260827"}

        self.assertIs(
            downloader.validate_expected_date_folder(selected, "20260827"),
            selected,
        )

    def test_missing_requested_date_folder_fails_closed(self) -> None:
        entries = [{".tag": "folder", "name": "20260826"}]

        with self.assertRaisesRegex(RuntimeError, "was not found: 20260825"):
            downloader.select_date_folder(entries, "20260825")

    def test_invalid_requested_date_folder_fails_closed(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "must contain 6 to 8 digits"):
            downloader.select_date_folder([], "latest")

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


class DropboxDatePolicyTests(unittest.TestCase):
    @staticmethod
    def folder(name: str) -> dict:
        return {".tag": "folder", "name": name, "path_lower": f"/zip_backup/{name}"}

    def test_same_day_and_overnight_batches_are_accepted(self) -> None:
        for source in ("260921", "20260921", "260922", "20260922"):
            with self.subTest(source=source):
                selected = self.folder(source)
                self.assertIs(downloader.validate_expected_date_folder(selected, "260922", 1), selected)

    def test_older_batches_are_rejected(self) -> None:
        for source in ("260920", "20260919"):
            with self.subTest(source=source), self.assertRaisesRegex(RuntimeError, "allowed age is 0..1"):
                downloader.validate_expected_date_folder(self.folder(source), "260922", 1)

    def test_future_batches_are_rejected(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "Source age is -1"):
            downloader.validate_expected_date_folder(self.folder("260923"), "260922", 1)

    def test_calendar_rollovers(self) -> None:
        for source, expected in (("261231", "270101"), ("260831", "260901"),
                                 ("240229", "240301"), ("230228", "230301")):
            with self.subTest(source=source, expected=expected):
                selected = self.folder(source)
                self.assertIs(downloader.validate_expected_date_folder(selected, expected, 1), selected)

    def test_mixed_width_dates_sort_chronologically(self) -> None:
        entries = [self.folder("20260831"), self.folder("260901")]
        self.assertEqual(downloader.latest_date_folder(entries)["name"], "260901")

    def test_equivalent_formats_pass_strict_validation(self) -> None:
        for source, expected in (("260922", "20260922"), ("20260922", "260922")):
            with self.subTest(source=source):
                selected = self.folder(source)
                self.assertIs(downloader.validate_expected_date_folder(selected, expected), selected)

    def test_invalid_dates_do_not_win_latest_selection(self) -> None:
        entries = [self.folder(name) for name in ("99999999", "2026092", "260231", "260922")]
        entries += [{".tag": "file", "name": "20260923"}]
        self.assertEqual(downloader.latest_date_folder(entries)["name"], "260922")

    def test_no_valid_date_folders_fail(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "No valid date-named"):
            downloader.latest_date_folder([self.folder("archive"), self.folder("20260230")])

    def test_ambiguous_latest_date_requires_explicit_folder(self) -> None:
        entries = [self.folder("260922"), self.folder("20260922")]
        with self.assertRaisesRegex(RuntimeError, "Multiple Dropbox folders"):
            downloader.latest_date_folder(entries)
        self.assertIs(downloader.select_date_folder(entries, "260922"), entries[0])
        self.assertIs(downloader.select_date_folder(entries, "20260922"), entries[1])

    def test_explicit_date_allows_equivalent_format_only(self) -> None:
        for requested, actual in (("260922", "20260922"), ("20260922", "260922")):
            with self.subTest(requested=requested):
                entries = [self.folder(actual), self.folder("260923")]
                self.assertIs(downloader.select_date_folder(entries, requested), entries[0])

    def test_missing_requested_date_explains_available_batches(self) -> None:
        entries = [self.folder("260920"), self.folder("260921")]
        with self.assertRaisesRegex(RuntimeError, "260921, 260920.*No fallback"):
            downloader.select_date_folder(entries, "260922")

    def test_invalid_requested_dates_fail_closed(self) -> None:
        for name in ("260231", "20260229", "2026092", "２６０９２２", "../260922", "latest"):
            with self.subTest(name=name), self.assertRaises(RuntimeError):
                downloader.select_date_folder([self.folder(name)], name)

    def test_short_years_do_not_use_strptime_century_pivot(self) -> None:
        self.assertEqual(downloader.parse_date_folder("690101").isoformat(), "2069-01-01")

    def test_negative_lag_fails_even_without_expected_date(self) -> None:
        with self.assertRaisesRegex(RuntimeError, "non-negative"):
            downloader.validate_expected_date_folder(self.folder("260921"), "", -1)

    def test_diagnostics_are_bounded_and_omit_other_names(self) -> None:
        entries = [self.folder(f"2609{day:02d}") for day in range(1, 31)]
        entries += [self.folder("private-customer-folder"), {".tag": "file", "name": "private.pdf"}]
        names = downloader.recent_date_folder_names(entries)
        self.assertEqual(len(names), 20)
        self.assertEqual(names[0], "260930")
        self.assertEqual(names[-1], "260911")
        self.assertNotIn("private", ",".join(names))

    def test_list_folder_consumes_all_pages(self) -> None:
        first, second = self.folder("260920"), self.folder("260921")
        with patch.object(downloader, "api_post", side_effect=[
            {"entries": [first], "has_more": True, "cursor": "page2"},
            {"entries": [second], "has_more": False},
        ]) as api:
            self.assertEqual(downloader.list_folder("token", "/zip_backup"), [first, second])
        self.assertEqual(api.call_args_list[1].args[1:], ("/files/list_folder/continue", {"cursor": "page2"}))

    def test_summary_failure_does_not_change_primary_result(self) -> None:
        with patch.dict(downloader.os.environ, {"GITHUB_STEP_SUMMARY": "/unwritable/summary"}), \
                patch("builtins.open", side_effect=OSError("read only")), \
                patch.object(downloader, "log") as log:
            downloader.write_input_summary({"status": "downloaded"})
        self.assertIn("primary result is unchanged", log.call_args.args[0])


class DropboxInputIntegrationTests(unittest.TestCase):
    def run_main(self, names, extra_args, children=None, fail_download=False):
        """Exercise the real CLI with Dropbox calls mocked and no live credentials."""
        import contextlib
        import io
        import json

        entries = [DropboxDatePolicyTests.folder(name) for name in names]
        if children is None:
            children = [{".tag": "file", "name": "report.PDF", "path_lower": f"/zip_backup/{names[-1]}/report.pdf"}]
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            output = root / "pdfs"
            stdout, stderr = io.StringIO(), io.StringIO()

            def download(token, path, destination):
                if fail_download:
                    raise RuntimeError("simulated download failure")
                destination.parent.mkdir(parents=True, exist_ok=True)
                destination.write_bytes(b"%PDF-mocked-download")

            with patch.object(downloader.sys, "argv", ["download", "--output-dir", str(output), *extra_args]), \
                    patch.dict(downloader.os.environ, {"GITHUB_OUTPUT": str(root / "outputs"),
                                                       "GITHUB_STEP_SUMMARY": str(root / "summary")}), \
                    patch.object(downloader, "dropbox_access_token", return_value="mock-token") as token, \
                    patch.object(downloader, "list_folder", side_effect=[entries, children]) as listing, \
                    patch.object(downloader, "download_file", side_effect=download) as downloading, \
                    contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                result = downloader.main()
            manifest = output / "dropbox_manifest.json"
            return {
                "result": result,
                "manifest": json.loads(manifest.read_text()) if manifest.exists() else None,
                "outputs": (root / "outputs").read_text() if (root / "outputs").exists() else "",
                "summary": (root / "summary").read_text(),
                "stdout": stdout.getvalue(), "stderr": stderr.getvalue(),
                "downloads": downloading.call_count, "list_calls": listing.call_count,
                "token_calls": token.call_count,
            }

    def test_previous_day_batch_downloads_with_explicit_one_day_policy(self) -> None:
        result = self.run_main(["260921"], ["--expected-date-folder", "260922", "--max-folder-age-days", "1"])
        self.assertEqual(result["result"], 0, result["stderr"])
        self.assertEqual(result["downloads"], 1)
        self.assertEqual(result["manifest"]["latest_folder"], "260921")
        self.assertEqual(result["manifest"]["source_date"], "2026-09-21")
        self.assertEqual(result["manifest"]["folder_age_days"], 1)
        self.assertIn("latest_folder=260921", result["outputs"])
        self.assertIn('"status": "downloaded"', result["summary"])
        self.assertIn('"downloaded_pdf_count": 1', result["summary"])

    def test_default_cli_policy_remains_strict(self) -> None:
        result = self.run_main(["260921"], ["--expected-date-folder", "260922"])
        self.assertEqual(result["result"], 2)
        self.assertEqual(result["downloads"], 0)
        self.assertEqual(result["list_calls"], 1)

    def test_stale_and_future_batches_stop_before_recursive_listing(self) -> None:
        for source in ("260920", "260923"):
            with self.subTest(source=source):
                result = self.run_main([source], ["--expected-date-folder", "260922", "--max-folder-age-days", "1"])
                self.assertEqual(result["result"], 2)
                self.assertEqual(result["downloads"], 0)
                self.assertEqual(result["list_calls"], 1)
                self.assertEqual(result["outputs"], "")
                self.assertIsNone(result["manifest"])
                self.assertIn('"status": "failed"', result["summary"])

    def test_missing_exact_date_never_downloads_another_batch(self) -> None:
        result = self.run_main(["260921"], ["--date-folder", "260922", "--max-folder-age-days", "1"])
        self.assertEqual(result["result"], 2)
        self.assertEqual(result["downloads"], 0)
        self.assertEqual(result["list_calls"], 1)
        self.assertIn("was not found: 260922", result["stderr"])
        self.assertIn("Available date folders (newest first): 260921", result["stderr"])
        self.assertIn("Listing Dropbox root: /zip_backup", result["stdout"])
        self.assertEqual(result["outputs"], "")

    def test_explicit_historical_backfill_remains_supported(self) -> None:
        result = self.run_main(["260901", "260921"], ["--date-folder", "260901"], children=[
            {".tag": "file", "name": "old.pdf", "path_lower": "/zip_backup/260901/old.pdf"},
        ])
        self.assertEqual(result["result"], 0, result["stderr"])
        self.assertEqual(result["manifest"]["latest_folder"], "260901")
        self.assertIsNone(result["manifest"]["folder_age_days"])

    def test_same_date_format_alias_preserves_actual_folder_identity(self) -> None:
        result = self.run_main(["20260922"], ["--date-folder", "260922"])
        self.assertEqual(result["result"], 0, result["stderr"])
        self.assertEqual(result["manifest"]["latest_folder"], "20260922")
        self.assertIn("latest_folder=20260922", result["outputs"])

    def test_empty_latest_batch_does_not_fall_back(self) -> None:
        result = self.run_main(["260921", "260922"], ["--expected-date-folder", "260922", "--max-folder-age-days", "1"], children=[])
        self.assertEqual(result["result"], 2)
        self.assertEqual(result["downloads"], 0)
        self.assertEqual(result["list_calls"], 2)
        self.assertIn("No PDFs found", result["stderr"])
        self.assertIn('"selected_date_folder": "260922"', result["summary"])

    def test_invalid_policy_fails_before_auth(self) -> None:
        for args in (["--max-folder-age-days", "-1"], ["--date-folder", "260231"],
                     ["--expected-date-folder", "2026092"]):
            with self.subTest(args=args):
                result = self.run_main(["260921"], args)
                self.assertEqual(result["result"], 2)
                self.assertEqual(result["token_calls"], 0)
                self.assertEqual(result["list_calls"], 0)
                self.assertEqual(result["downloads"], 0)

    def test_download_failure_does_not_export_success_outputs(self) -> None:
        result = self.run_main(["260922"], ["--expected-date-folder", "260922"], fail_download=True)
        self.assertEqual(result["result"], 2)
        self.assertEqual(result["outputs"], "")
        self.assertIsNone(result["manifest"])
        self.assertIn('"status": "failed"', result["summary"])
        self.assertIn('"pdf_count": 1', result["summary"])
        self.assertIn('"downloaded_pdf_count": 0', result["summary"])

    def test_non_pdf_files_do_not_count_as_downloads(self) -> None:
        result = self.run_main(["260922"], [], children=[
            {".tag": "file", "name": "report.PDF", "path_lower": "/zip_backup/260922/report.pdf"},
            {".tag": "file", "name": "ready.json", "path_lower": "/zip_backup/260922/ready.json"},
            {".tag": "folder", "name": "folder.pdf"},
        ])
        self.assertEqual(result["result"], 0, result["stderr"])
        self.assertEqual(result["downloads"], 1)
        self.assertEqual(result["manifest"]["pdf_count"], 1)


class DropboxWorkflowContractTests(unittest.TestCase):
    @staticmethod
    def workflow() -> str:
        root = Path(__file__).resolve().parents[1]
        return (root / ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml").read_text(encoding="utf-8")

    def test_daily_downloader_explicitly_allows_only_one_day_lag(self) -> None:
        workflow = self.workflow()
        download_step = workflow.split("      - name: Download PDFs from latest Dropbox date folder\n", 1)[1]
        download_step = download_step.split("      - name: Select reports with DeepSeek\n", 1)[0]
        self.assertIn('--expected-date-folder "$EXPECTED_DATE"', download_step)
        self.assertIn('--date-folder "$REQUESTED_DATE"', download_step)
        self.assertIn('--max-folder-age-days 1 \\', download_step)
        self.assertEqual(download_step.count('--max-folder-age-days'), 1)

    def test_schedule_reference_and_actual_batch_identity_are_preserved(self) -> None:
        workflow = self.workflow()
        self.assertIn('if [ "${{ github.event_name }}" = "schedule" ]; then', workflow)
        self.assertIn('TZ=Asia/Shanghai date +%y%m%d', workflow)
        self.assertIn('echo "expected_dropbox_date_folder=" >> "$GITHUB_OUTPUT"', workflow)
        self.assertIn('latest_folder: ${{ steps.dropbox.outputs.latest_folder }}', workflow)
        self.assertIn('OUTPUT_DIR: xhs_notes/dropbox/${{ needs.select-macro-reports.outputs.latest_folder }}', workflow)


if __name__ == "__main__":
    unittest.main(verbosity=2)
