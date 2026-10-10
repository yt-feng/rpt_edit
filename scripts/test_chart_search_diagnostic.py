#!/usr/bin/env python3
from __future__ import annotations

import contextlib
import io
import json
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import diagnose_chart_search_state as diagnostic


RUN_ID = "36494813159"
VERSION = diagnostic.chart.ANALYSIS_VERSION


def record(status="error", run=RUN_ID + ":1:recovery-1", **fields):
    return {"status": status, "last_attempt_run_id": run,
            "analysis_version": VERSION, "attempts": 2,
            "stable_attempt_runs": 0, "failure_class": "transient",
            "failure_reason": "model_json", **fields}


def checkpoint(items):
    return {"schema_version": 1, "analysis_version": VERSION, "items": items}


class DiagnosticTests(unittest.TestCase):
    def test_exact_latest_attempt_selection_does_not_claim_candidate_coverage(self):
        state = checkpoint({
            "a" * 64: record(),
            "b" * 64: record("ok", RUN_ID + ":1", analysis={"title": "PRIVATE_CONTENT"}),
            "c" * 64: record("ok", "36400000000:1", analysis={}),  # a cache hit retains its older run
            "d" * 64: record("ok", RUN_ID, analysis_version="chart-search-v1", analysis={}),
            "e" * 64: record(run=RUN_ID + "0:1"),
            "f" * 64: record(run=RUN_ID + ":PRIVATE_SUFFIX"),
            "0" * 64: record(run=None),
            "PRIVATE_PATH": record(),
        })
        report = diagnostic.report_checkpoint(state, RUN_ID)
        self.assertEqual(report["selection"]["matched_status_counts"],
                         {"ok": 2, "error": 1, "quarantined": 0, "unknown": 0})
        self.assertEqual(report["selection"]["matched_reusable_count"], 1)
        self.assertEqual(report["checkpoint_reusable_count"], 2)
        self.assertEqual(report["unrecognized_last_attempt_count"], 2)
        self.assertEqual(report["invalid_record_count"], 1)
        self.assertEqual([item["image_sha256"] for item in report["related_errors"]], ["a" * 64])
        self.assertEqual(report["related_errors"][0]["run_attempt"], 1)
        self.assertEqual(report["related_errors"][0]["recovery_round"], 1)
        self.assertFalse(report["related_errors"][0]["diagnostic_available"])
        self.assertEqual(report["candidate_coverage"]["status"], "unavailable")
        self.assertIsNone(report["candidate_coverage"]["reusable_count"])
        self.assertNotIn("PRIVATE", json.dumps(report))

    def test_private_fields_are_redacted_and_error_details_are_bounded(self):
        items = {f"{n:064x}": record(
            attempts=True, stable_attempt_runs=-1, failure_class="PRIVATE_CLASS",
            failure_reason="PRIVATE_REASON", error_type="PRIVATE_ERROR",
            analysis={"description": "PRIVATE_CONTENT"}, source_path="PRIVATE_PATH",
            failure_diagnostic={"finish_reason": "length", "content_type": "text_blocks",
                                "content_chars": 21033, "content_sha256": "a" * 64,
                                "json_error_pos": 20000, "content": "PRIVATE_CONTENT",
                                "provider_url": "PRIVATE_URL"},
        ) for n in range(diagnostic.MAX_ERROR_RECORDS + 2)}
        report = diagnostic.report_checkpoint(checkpoint(items), RUN_ID)
        self.assertEqual(report["selection"]["matched_error_count"], 102)
        self.assertEqual(len(report["related_errors"]), 100)
        self.assertTrue(report["selection"]["error_details_truncated"])
        item = report["related_errors"][0]
        self.assertIsNone(item["attempts"])
        self.assertIsNone(item["stable_attempt_runs"])
        self.assertEqual(item["failure_reason"], "unknown")
        self.assertEqual(item["failure_class"], "unknown")
        self.assertEqual(item["failure_diagnostic"]["json_error_pos"], 20000)
        self.assertNotIn("PRIVATE", json.dumps(report))

    def test_normal_download_helper_reads_once_and_cli_writes_only_report(self):
        state = checkpoint({"a" * 64: record(analysis={"title": "PRIVATE_CONTENT"})})
        calls = []

        class ReadOnlyClient:
            # Deliberately provides no write/delete/list interface.
            def get_object(self, **kwargs):
                calls.append(kwargs)
                return {"Body": io.BytesIO(json.dumps(state).encode())}

        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "report.json"
            with patch.object(diagnostic.r2, "client_and_bucket", return_value=(ReadOnlyClient(), "PRIVATE_BUCKET")), \
                    patch.object(diagnostic.chart, "VisionClient", side_effect=AssertionError("No model calls")), \
                    patch("sys.argv", ["diagnostic", "--run-id", RUN_ID, "--output", str(output)]), \
                    contextlib.redirect_stdout(io.StringIO()) as log:
                self.assertEqual(diagnostic.main(), 0)
            self.assertEqual([path.name for path in Path(directory).iterdir()], ["report.json"])
            self.assertNotIn("PRIVATE", output.read_text() + log.getvalue())
        self.assertEqual(calls, [{"Bucket": "PRIVATE_BUCKET", "Key": "_chart-search/v1/state.json"}])

    def test_read_errors_missing_state_and_invalid_schema_never_become_empty_success(self):
        with patch.object(diagnostic.r2, "client_and_bucket", side_effect=RuntimeError("PRIVATE_URL_TOKEN")):
            report, status = diagnostic.read_report(RUN_ID)
        self.assertEqual((report["read_status"], status), ("read_failed", 1))
        self.assertNotIn("PRIVATE", json.dumps(report))
        for state, found, expected in ((checkpoint({}), False, "missing"),
                                       ({"schema_version": 1, "items": []}, True, "invalid_schema")):
            with self.subTest(expected=expected), \
                    patch.object(diagnostic.r2, "client_and_bucket", return_value=(object(), "PRIVATE_BUCKET")), \
                    patch.object(diagnostic.r2, "read_json_object", return_value=(state, found)):
                report, status = diagnostic.read_report(RUN_ID)
            self.assertEqual((report["read_status"], status), (expected, 1))

    def test_invalid_filter_never_reads_storage_and_missing_match_is_explicit(self):
        for invalid in ("", "0", "PRIVATE_INPUT", RUN_ID + ":1", RUN_ID + "\n", "1" * 21):
            with self.subTest(value=invalid), patch.object(diagnostic.r2, "client_and_bucket") as client:
                report, status = diagnostic.read_report(invalid)
                self.assertEqual((report["read_status"], status), ("invalid_run_id", 1))
                client.assert_not_called()
                self.assertNotIn("requested_run_id", report)
        report = diagnostic.report_checkpoint(checkpoint({"a" * 64: record(run="1:1")}), RUN_ID)
        self.assertTrue(report["selection"]["no_latest_attempt_match"])
        self.assertEqual(report["related_errors"], [])
        self.assertEqual(report["candidate_coverage"]["status"], "unavailable")

    def test_workflow_has_only_filtered_artifact_and_scoped_probe_credentials(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/portal-chart-search-diagnostic.yml").read_text()
        self.assertIn("default: checkpoint", workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertIn("contents: read", workflow)
        self.assertIn("pull_request:", workflow)
        self.assertEqual(workflow.count("if: github.event_name == 'workflow_dispatch'"), 3)
        self.assertIn("if: always() && github.event_name == 'workflow_dispatch'", workflow)
        self.assertEqual(workflow.count("uses: actions/upload-artifact@"), 1)
        self.assertIn("path: _chart_diagnostic/report.json", workflow)
        checkpoint_step = workflow.split("- name: Read checkpoint", 1)[1].split("- name: Probe", 1)[0]
        self.assertNotIn("VISION_INDEX_API_KEY", checkpoint_step)
        self.assertIn("inputs.operation != 'vision-config'", checkpoint_step)
        probe_step = workflow.split("- name: Probe", 1)[1].split("- name: Upload", 1)[0]
        self.assertIn("inputs.operation == 'vision-config'", probe_step)
        self.assertIn("VISION_INDEX_API_KEY", probe_step)
        self.assertNotIn("R2_ACCESS_KEY_ID", probe_step)
        self.assertNotIn("publish-state", workflow)
        self.assertNotIn("chart_search_r2.py publish", workflow)
        self.assertNotIn("python scripts/build_chart_search_index.py", workflow)


if __name__ == "__main__":
    unittest.main()
