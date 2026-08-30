#!/usr/bin/env python3

from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest import mock

sys.path.insert(0, str(Path(__file__).resolve().parent))

import archive_portal_growth_review as archive


class FakeClient:
    def __init__(self, error: Exception | None = None) -> None:
        self.error = error
        self.calls: list[dict[str, object]] = []
        self.objects: dict[str, bytes] = {}

    def put_object(self, **kwargs: object) -> None:
        if self.error:
            raise self.error
        self.calls.append(kwargs)
        self.objects[str(kwargs["Key"])] = bytes(kwargs["Body"])


def write_review(folder: Path, report: dict[str, object] | None = None) -> tuple[Path, Path]:
    payload = report or {
        "start_date": "2026-08-12",
        "end_date": "2026-08-28",
        "privacy": {
            "visitor_ids_included": False,
            "session_ids_included": False,
            "search_queries_included": False,
        },
    }
    json_path = folder / "growth-review.json"
    markdown_path = folder / "growth-review.md"
    json_path.write_text(json.dumps(payload, ensure_ascii=False), encoding="utf-8")
    markdown_path.write_text("# aggregate review\n", encoding="utf-8")
    return json_path, markdown_path


class ArchiveGrowthReviewTest(unittest.TestCase):
    def test_actual_and_nested_review_window_fields_are_supported(self) -> None:
        self.assertEqual(
            archive.review_window({"start_date": "2026-08-12", "end_date": "2026-08-28"}),
            ("2026-08-12", "2026-08-28"),
        )
        self.assertEqual(
            archive.review_window({"review_window": {"start": "2026-08-01", "end": "2026-08-07"}}),
            ("2026-08-01", "2026-08-07"),
        )

    def test_review_window_cannot_inject_an_object_path(self) -> None:
        for value in ("../../private", "2026-08-01/secret", "2026-8-1", "2026-02-30"):
            with self.assertRaises(archive.ArchiveError):
                archive.archive_keys(value, "2026-08-28")
        with self.assertRaises(archive.ArchiveError):
            archive.review_window({"start_date": "2026-08-29", "end_date": "2026-08-28"})

    def test_both_formats_upload_to_stable_private_keys_and_rerun_overwrites(self) -> None:
        with tempfile.TemporaryDirectory() as folder_name:
            json_path, markdown_path = write_review(Path(folder_name))
            client = FakeClient()
            result = archive.archive_growth_review(client, "private-bucket", json_path, markdown_path)
            archive.archive_growth_review(client, "private-bucket", json_path, markdown_path)
        self.assertEqual(result, ("2026-08-12", "2026-08-28", 2))
        expected_root = "_analytics/reviews/weekly/2026-08-12_2026-08-28"
        self.assertEqual(
            set(client.objects),
            {f"{expected_root}/growth-review.json", f"{expected_root}/growth-review.md"},
            "a same-window rerun must target and overwrite the same two keys",
        )
        self.assertEqual(len(client.calls), 4)
        self.assertEqual(
            [call["ContentType"] for call in client.calls[:2]],
            ["application/json; charset=utf-8", "text/markdown; charset=utf-8"],
        )
        self.assertTrue(all(call["CacheControl"] == "private, no-store" for call in client.calls))

    def test_missing_aggregate_only_assertion_blocks_upload(self) -> None:
        with tempfile.TemporaryDirectory() as folder_name:
            folder = Path(folder_name)
            json_path, markdown_path = write_review(folder, {
                "start_date": "2026-08-12",
                "end_date": "2026-08-28",
                "privacy": {"search_queries_included": True},
            })
            client = FakeClient()
            with self.assertRaises(archive.ArchiveError):
                archive.archive_growth_review(client, "private-bucket", json_path, markdown_path)
        self.assertEqual(client.calls, [])

    def test_cli_logs_only_fixed_status_dates_and_object_count(self) -> None:
        with tempfile.TemporaryDirectory() as folder_name:
            json_path, markdown_path = write_review(Path(folder_name))
            client = FakeClient()
            stdout = io.StringIO()
            stderr = io.StringIO()
            argv = ["archive", "--json", str(json_path), "--markdown", str(markdown_path)]
            with mock.patch.object(sys, "argv", argv), mock.patch.object(
                archive, "build_r2_client", return_value=(client, "private-secret-bucket")
            ), contextlib.redirect_stdout(stdout), contextlib.redirect_stderr(stderr):
                self.assertEqual(archive.main(), 0)
        self.assertEqual(stdout.getvalue(), "growth-review-archive: 2026-08-12_2026-08-28 objects=2\n")
        self.assertEqual(stderr.getvalue(), "")
        self.assertNotIn("private-secret-bucket", stdout.getvalue())

        with tempfile.TemporaryDirectory() as folder_name:
            json_path, markdown_path = write_review(Path(folder_name))
            leaked_error = RuntimeError("endpoint.example private-secret-bucket private-secret-key")
            stderr = io.StringIO()
            argv = ["archive", "--json", str(json_path), "--markdown", str(markdown_path)]
            with mock.patch.object(sys, "argv", argv), mock.patch.object(
                archive, "build_r2_client", return_value=(FakeClient(leaked_error), "private-secret-bucket")
            ), contextlib.redirect_stderr(stderr):
                self.assertEqual(archive.main(), 1)
        self.assertEqual(stderr.getvalue(), "growth-review-archive: failed\n")

    def test_workflow_archives_after_validation_before_short_lived_artifact(self) -> None:
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/portal-growth-review.yml").read_text(encoding="utf-8")
        verify = workflow.index("name: Verify aggregate-only output")
        persistent = workflow.index("name: Archive aggregate review to private R2")
        artifact = workflow.index("name: Upload short-lived aggregate review")
        self.assertLess(verify, persistent)
        self.assertLess(persistent, artifact)
        archive_step = workflow[persistent:artifact]
        self.assertIn("scripts/archive_portal_growth_review.py", workflow)
        self.assertIn("R2_ACCOUNT_ID:", archive_step)
        self.assertIn("R2_ACCESS_KEY_ID:", archive_step)
        self.assertIn("R2_SECRET_ACCESS_KEY:", archive_step)
        self.assertIn("R2_BUCKET:", archive_step)
        self.assertNotIn("continue-on-error", archive_step)


if __name__ == "__main__":
    unittest.main()
