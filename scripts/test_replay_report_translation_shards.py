#!/usr/bin/env python3
"""A PDF-only replay preserves plan identity and never repeats successful members."""
import argparse
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import build_portal_translated_reports as builder
import replay_report_translation_shards as replay


def plan_fixture(count=21):
    reports = [{"global_index": index, "relative_dir": f"shard_{(index - 1) // 5}/report-{index}",
                "source_sha256": hashlib.sha256(str(index).encode()).hexdigest()} for index in range(1, count + 1)]
    plan = {"schema_version": 1, "date_folder": "260920", "source_count": count, "selected_count": count,
            "max_reports": "all", "reports_per_shard": 5, "shard_count": (count + 4) // 5, "reports": reports}
    plan["plan_sha256"] = hashlib.sha256(json.dumps(plan, sort_keys=True).encode()).hexdigest()
    return plan


def completed_result(root, plan, index):
    date_root = root / "portal_translated_reports" / plan["date_folder"]
    reports = []
    for record in replay.shards.shard_records(plan, index):
        number = record["global_index"]
        directory = date_root / f"{number:02d}-report"
        directory.mkdir(parents=True)
        pdf = f"portal_translated_report_{number:02d}.pdf"
        (directory / pdf).write_bytes(b"%PDF-" + b"0" * 1100)
        (directory / "translated.md").write_text("完整测试译文", encoding="utf-8")
        status = {"global_index": number, "source_report_dir": "xhs_notes/dropbox/260920/" + record["relative_dir"], "pdf": pdf}
        (directory / "translation_status.json").write_text(json.dumps(status))
        reports.append({**status, "output_dir": str(directory), "pdf_path": str(directory / pdf)})
    summary = {"plan_sha256": plan["plan_sha256"], "successful_count": len(reports), "reports": reports, "failures": []}
    (date_root / f"translation_shard_{index}.json").write_text(json.dumps(summary))


class ReplayTests(unittest.TestCase):
    def setUp(self):
        self.plan = plan_fixture()
        self.run = {"id": 123, "path": replay.SOURCE_WORKFLOW, "head_branch": "main", "run_attempt": 1,
                    "head_repository": {"full_name": "example/repo"}, "status": "in_progress"}
        self.jobs = {"jobs": [{"name": "plan-portal-translated-reports", "status": "completed", "conclusion": "success"}] + [
            {"name": f"translate-report-shard ({index})", "status": "completed", "conclusion": "failure" if index in (0, 4) else "success"}
            for index in range(5)]}

    def validate(self, run=None, jobs=None, indices=None):
        return replay.validate_source(run or self.run, jobs or self.jobs, "example/repo", "123", [0, 4] if indices is None else indices)

    def test_completed_failed_matrix_can_replay_while_article_branch_is_running(self):
        matrix = self.validate()
        replay.validate_plan(self.plan, "260920", matrix, self.plan["plan_sha256"])
        self.assertEqual(set(matrix), set(range(5)))

    def test_success_active_cancelled_missing_and_unrequested_failed_shards_are_rejected(self):
        for mutate in ("active", "success", "cancelled", "missing", "partial-jobs"):
            with self.subTest(mutate=mutate):
                jobs = copy.deepcopy(self.jobs)
                if mutate == "active":
                    jobs["jobs"][1]["status"] = "in_progress"
                elif mutate in ("success", "cancelled"):
                    jobs["jobs"][1]["conclusion"] = mutate
                elif mutate == "missing":
                    jobs["jobs"].pop()
                else:
                    jobs["total_count"] = 999
                with self.assertRaises(ValueError):
                    self.validate(jobs=jobs)
        with self.assertRaises(ValueError):
            self.validate(indices=[4])
        with self.assertRaises(ValueError):
            self.validate(indices=[0, 1, 4])

    def test_other_sources_or_prior_attempts_cannot_target_original_slots(self):
        for key, value in (("path", "other.yml"), ("head_branch", "other"), ("id", 124), ("run_attempt", 2),
                           ("head_repository", {"full_name": "other/repository"})):
            with self.subTest(key=key), self.assertRaises(ValueError):
                self.validate(run={**self.run, key: value})

    def test_changed_plan_hash_date_or_dimensions_fail(self):
        for date, matrix, digest in (("260921", self.validate(), ""), ("260920", {0: {}}, ""),
                                     ("260920", self.validate(), "different")):
            with self.assertRaises(ValueError):
                replay.validate_plan(self.plan, date, matrix, digest)

    def test_requested_coordinates_are_exact(self):
        self.assertEqual(replay.coordinates("123", "260920", "4,0"), ("_private-workflow-handoff/xhs/123/260920", [0, 4]))
        for run, date, indices in (("../123", "260920", "4"), ("123", "260932", "4"),
                                   ("123", "260920", "0,0"), ("123", "260920", "[0,4]")):
            with self.assertRaises(ValueError):
                replay.coordinates(run, date, indices)

    def test_completed_slot_reused_without_upload_and_global_index_21_preserved(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed_result(root, self.plan, 4)
            client = Mock()
            with patch.object(replay, "download_directory") as download, patch.object(replay, "upload_directory") as upload:
                self.assertTrue(replay.restore_completed_slot(self.plan, 4, "source/run/date", root, client=client, bucket="test"))
                download.assert_called_once_with("source/run/date/translated_4.tar.gz", root, client=client, bucket="test")
                upload.assert_not_called()
            self.assertTrue((root / "portal_translated_reports/260920/21-report/portal_translated_report_21.pdf").is_file())

    def test_only_missing_slots_are_optional_and_partial_slots_fail(self):
        client = Mock()
        for code in ("404", "NoSuchKey", "AccessDenied", "503"):
            error = RuntimeError(code)
            error.response = {"Error": {"Code": code}}
            client.head_object.side_effect = error
            if code in ("404", "NoSuchKey"):
                self.assertFalse(replay.restore_completed_slot(self.plan, 4, "prefix", Path("unused"), client=client, bucket="test"))
            else:
                with self.assertRaises(RuntimeError):
                    replay.restore_completed_slot(self.plan, 4, "prefix", Path("unused"), client=client, bucket="test")
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            completed_result(root, self.plan, 4)
            (root / "portal_translated_reports/260920/21-report/portal_translated_report_21.pdf").write_bytes(b"partial")
            with self.assertRaises(ValueError):
                replay.validate_result(self.plan, 4, root)

    def test_exact_union_merges_21_reports_and_refuses_missing_member(self):
        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            for index in range(5):
                completed_result(root / "shards" / f"shard_{index}", self.plan, index)
            summary = replay.shards.merge_shards(self.plan, root / "shards", root / "merged")
            self.assertEqual(summary["successful_count"], 21)
            self.assertEqual([report["global_index"] for report in summary["reports"]], list(range(1, 22)))
            (root / "shards/shard_4/portal_translated_reports/260920/21-report/portal_translated_report_21.pdf").unlink()
            with self.assertRaises(ValueError):
                replay.shards.merge_shards(self.plan, root / "shards", root / "incomplete")
            self.assertFalse((root / "incomplete").exists())

    def test_offline_only_rejects_paid_editorial_before_key_or_network_lookup(self):
        with patch.object(builder, "deepseek_api_keys_from_env") as keys, patch.object(builder, "request_with_key_fallback") as request:
            with self.assertRaisesRegex(RuntimeError, "Paid editorial calls are disabled"):
                builder.call_deepseek("prompt", argparse.Namespace(offline_only=True), "replay")
            keys.assert_not_called()
            request.assert_not_called()

    def test_workflow_has_no_wechat_or_source_regeneration_and_preserves_checkpoints(self):
        workflow = (Path(__file__).resolve().parents[1] / ".github/workflows/replay-report-translation-shards.yml").read_text()
        self.assertIn("--offline-only", workflow)
        self.assertIn("--report-plan", workflow)
        self.assertIn("--translation-shard-index", workflow)
        self.assertIn("always() && steps.translation_checkpoint.outcome == 'success'", workflow)
        self.assertIn("needs: [validate-plan, replay-shard]", workflow)
        self.assertIn("steps.sources.outputs.complete != 'true'", workflow)
        for forbidden in ("secrets.DEEPSEEK", "push_portal_translated_to_wechat", "push_xhs_notes_to_wechat", "run_pdf_to_xhs", "delete-prefix", "--publish"):
            self.assertNotIn(forbidden, workflow)


if __name__ == "__main__":
    unittest.main()
