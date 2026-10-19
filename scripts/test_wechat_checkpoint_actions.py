#!/usr/bin/env python3
"""Execute checkpoint action guards locally without GitHub or WeChat calls."""

import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile
import textwrap
import unittest


ROOT = Path(__file__).resolve().parents[1]
ARCHIVE = ROOT / ".github/actions/resilient-diagnostic-artifact/action.yml"
RESTORE = ROOT / ".github/actions/restore-wechat-diagnostics/action.yml"
VALIDATOR = ARCHIVE.with_name("validate_wechat_checkpoint.py")
GROUP_KEY = "a" * 64
SUBMISSION_NAME = f"draft_submission_{GROUP_KEY}.json"


def summary(root, **changes):
    return {"date_folder": root.name, "dry_run": False, "draft_count": 1,
            "drafts": [{"media_id": "accepted-id"}], "status": "in_progress", **changes}


def submission(**changes):
    return {"schema_version": 1, "group_key": GROUP_KEY, "account_fingerprint": "b" * 64,
            "article_count": 1, "titles": ["Example article"], "status": "add_in_flight", **changes}


def step_script(path, name, field="run"):
    block = path.read_text().split("    - name: " + name + "\n", 1)[1].split("\n    - name:", 1)[0]
    return textwrap.dedent(block.split(field + ": |\n", 1)[1])


class CheckpointArchiveTests(unittest.TestCase):
    def validate(self, path, name="wechat-drafts-123-attempt-2", attempt="2"):
        return subprocess.run([sys.executable, "-c", step_script(ARCHIVE, "Validate required delivery checkpoint")],
                              env={**os.environ, "CHECKPOINT_PATH": str(path), "ARTIFACT_NAME": name,
                                   "CURRENT_RUN_ATTEMPT": attempt, "CHECKPOINT_VALIDATOR": str(VALIDATOR)},
                              capture_output=True, text=True)

    def test_log_only_malformed_and_non_object_json_cannot_be_checkpoints(self):
        for content in (None, "{}", "{broken", "[]", "null", '"a string"'):
            with self.subTest(content=content), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "upload.log").write_text("accepted some draft")
                if content is not None:
                    (root / "wechat_draft_summary.json").write_text(content)
                self.assertNotEqual(0, self.validate(root).returncode)

    def test_summary_or_inflight_ledger_is_enough_and_is_explicitly_uploaded(self):
        for name in ("wechat_draft_summary.json", SUBMISSION_NAME):
            with self.subTest(name=name), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                nested = root / "261019"
                nested.mkdir()
                (nested / name).write_text(json.dumps(summary(root) if name == "wechat_draft_summary.json" else submission()))
                self.assertEqual(0, self.validate(root).returncode)
        action = ARCHIVE.read_text()
        for name in ("Upload diagnostic artifact", "Retry diagnostic artifact upload"):
            block = action.split("    - name: " + name + "\n", 1)[1].split("\n    - name:", 1)[0]
            self.assertIn("${{ inputs.checkpoint-path }}", block)
            self.assertIn("name: ${{ inputs.name }}", block)

    def test_critical_retry_cannot_overwrite_a_legacy_or_previous_attempt_name(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "wechat_draft_summary.json").write_text(json.dumps(summary(root)))
            for name, attempt in (("wechat-drafts-123", "2"), ("wechat-drafts-123-attempt-1", "2"),
                                  ("wechat-drafts-123-attempt-3", "2"), ("wechat-drafts-123-attempt-0", "0")):
                with self.subTest(name=name, attempt=attempt):
                    self.assertNotEqual(0, self.validate(root, name, attempt).returncode)
            self.assertEqual(0, self.validate(root).returncode)

    def test_symlink_to_an_outside_json_object_does_not_validate(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "checkpoint"
            root.mkdir()
            outside = Path(tmp) / "outside.json"
            outside.write_text(json.dumps(summary(root)))
            (root / "wechat_draft_summary.json").symlink_to(outside)
            self.assertNotEqual(0, self.validate(root).returncode)

    def test_required_result_needs_artifact_id_but_noncritical_behavior_is_unchanged(self):
        cases = [("true", "success", "", 1), ("true", "success", "123", 0),
                 ("true", "failure", "", 1), ("false", "failure", "", 0), ("false", "success", "", 0)]
        for required, outcome, identifier, expected in cases:
            with self.subTest(required=required, outcome=outcome, identifier=identifier), tempfile.TemporaryDirectory() as tmp:
                result = subprocess.run(["bash", "-e", "-o", "pipefail", "-c", step_script(ARCHIVE, "Report diagnostic artifact result")],
                                        env={**os.environ, "REQUIRED": required, "PRIMARY_OUTCOME": outcome,
                                             "RETRY_OUTCOME": "skipped", "PRIMARY_ARTIFACT_ID": identifier,
                                             "RETRY_ARTIFACT_ID": "", "ARTIFACT_NAME": "checkpoint",
                                             "GITHUB_OUTPUT": str(Path(tmp) / "output")}, capture_output=True, text=True)
                self.assertEqual(expected, result.returncode)
        self.assertIn("if: ${{ inputs.required == 'true' }}", ARCHIVE.read_text())


class RestoredCheckpointContentTests(unittest.TestCase):
    def validate(self, path):
        return subprocess.run([sys.executable, "-c", step_script(RESTORE, "Validate restored delivery checkpoint")],
                              env={**os.environ, "CHECKPOINT_PATH": str(path), "CHECKPOINT_VALIDATOR": str(VALIDATOR)},
                              capture_output=True, text=True)

    def test_legacy_log_only_artifact_and_other_job_checkpoint_do_not_enable_upload(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            target = root / "expected-job"
            other = root / "another-job"
            target.mkdir()
            other.mkdir()
            (target / "upload.log").write_text("draft accepted")
            (other / "wechat_draft_summary.json").write_text(json.dumps(summary(other)))
            self.assertNotEqual(0, self.validate(target).returncode)
            self.assertNotEqual(0, self.validate(root / "missing-job").returncode)
            for value in ("{}", "[]", "{bad", "null"):
                (target / "wechat_draft_summary.json").write_text(value)
                self.assertNotEqual(0, self.validate(target).returncode)

    def test_exact_restored_directory_accepts_summary_or_inflight_objects(self):
        for filename in ("wechat_draft_summary.json", SUBMISSION_NAME):
            with self.subTest(filename=filename), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / filename).write_text(json.dumps(summary(root) if filename == "wechat_draft_summary.json" else submission()))
                self.assertEqual(0, self.validate(root).returncode)
        self.assertIn("if: ${{ github.run_attempt > 1 && inputs.checkpoint-path != '' }}", RESTORE.read_text())

    def test_summary_date_ids_types_and_count_must_be_consistent_for_both_actions(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for changes in ({"date_folder": "other-date"}, {"dry_run": "false"}, {"draft_count": 2},
                            {"draft_count": True}, {"drafts": [{}]}, {"drafts": [{"media_id": " "}]},
                            {"drafts": []}, {"draft_count": 0, "drafts": []}):
                with self.subTest(changes=changes):
                    (root / "wechat_draft_summary.json").write_text(json.dumps(summary(root, **changes)))
                    self.assertNotEqual(0, self.validate(root).returncode)
                    self.assertNotEqual(0, CheckpointArchiveTests().validate(root).returncode)

    def test_complete_zero_policy_or_failure_receipt_is_preserved_but_verified_zero_is_not(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            zero = summary(root, drafts=[], draft_count=0, selected_count=0, articles=[],
                           input_selected_count=1, skipped_title_policy_count=1, skipped_title_policy=[{}])
            for status in ("skipped_title_policy", "verified", "failed_generation_failure"):
                (root / "wechat_draft_summary.json").write_text(json.dumps({**zero, "status": status}))
                self.assertEqual(0, self.validate(root).returncode)
            (root / "wechat_draft_summary.json").write_text(json.dumps({**zero, "status": "verified", "skipped_title_policy_count": 0}))
            self.assertNotEqual(0, self.validate(root).returncode)

    def test_submission_requires_account_group_and_accepted_id(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / SUBMISSION_NAME
            for changes in ({"schema_version": 2}, {"group_key": "c" * 64}, {"account_fingerprint": ""},
                            {"article_count": 2}, {"status": "other"}, {"status": "accepted"},
                            {"status": "accepted", "media_id": " "}, {"media_id": "unexpected-id"}):
                with self.subTest(changes=changes):
                    path.write_text(json.dumps(submission(**changes)))
                    self.assertNotEqual(0, self.validate(root).returncode)
                    self.assertNotEqual(0, CheckpointArchiveTests().validate(root).returncode)
            for changes in ({"status": "accepted", "media_id": "accepted-id"}, {"status": "add_outcome_unknown"},
                            {"status": "rejected", "errcode": 45009}):
                path.write_text(json.dumps(submission(**changes)))
                self.assertEqual(0, self.validate(root).returncode)


@unittest.skipUnless(shutil.which("node"), "Node is needed to execute the GitHub script fixture")
class CheckpointRestoreTests(unittest.TestCase):
    def choose(self, names, current=4):
        artifacts = [{"name": item, "expired": False} if isinstance(item, str) else item for item in names]
        payload = {"script": step_script(RESTORE, "Locate prior draft receipts", "script"), "artifacts": artifacts}
        harness = """
        const fs = require('fs');
        const input = JSON.parse(fs.readFileSync(0, 'utf8'));
        const outputs = {};
        const github = { paginate: async () => input.artifacts,
                         rest: { actions: { listWorkflowRunArtifacts: () => {} } } };
        const context = { repo: { owner: 'example', repo: 'reports' }, runId: 123 };
        const core = { setOutput: (key, value) => outputs[key] = value };
        const AsyncFunction = Object.getPrototypeOf(async function(){}).constructor;
        new AsyncFunction('github', 'context', 'core', input.script)(github, context, core)
          .then(() => process.stdout.write(JSON.stringify({ok: true, outputs})))
          .catch(error => process.stdout.write(JSON.stringify({ok: false, error: error.message, outputs})));
        """
        result = subprocess.run([shutil.which("node"), "-e", harness], input=json.dumps(payload),
                                env={**os.environ, "RECEIPT_ARTIFACT_NAME": "wechat-drafts-123",
                                     "CURRENT_RUN_ATTEMPT": str(current)}, capture_output=True, text=True, check=True)
        return json.loads(result.stdout)

    def test_latest_strictly_prior_attempt_wins_over_legacy_current_future_and_near_names(self):
        result = self.choose(["wechat-drafts-123", "wechat-drafts-123-attempt-1", "wechat-drafts-123-attempt-3",
                              "wechat-drafts-123-attempt-2", "wechat-drafts-123-attempt-4", "wechat-drafts-123-attempt-5",
                              "other-wechat-drafts-123-attempt-3", "wechat-drafts-123-attempt-3-extra"])
        self.assertTrue(result["ok"])
        self.assertEqual("wechat-drafts-123-attempt-3", result["outputs"]["artifact_name"])
        self.assertIn("name: ${{ steps.locate.outputs.artifact_name }}", RESTORE.read_text())

    def test_legacy_exact_name_is_supported_only_without_prior_attempt_artifacts(self):
        result = self.choose(["wechat-drafts-123", "wechat-drafts-123-attempt-2"], current=2)
        self.assertTrue(result["ok"])
        self.assertEqual("wechat-drafts-123", result["outputs"]["artifact_name"])

    def test_missing_immediately_previous_attempt_cannot_fall_back_to_older_or_legacy(self):
        for names in (["wechat-drafts-123-attempt-1"], ["wechat-drafts-123"],
                      ["wechat-drafts-123", "wechat-drafts-123-attempt-1"]):
            with self.subTest(names=names):
                self.assertFalse(self.choose(names, current=3)["ok"])

    def test_latest_expired_or_duplicate_checkpoint_never_falls_back_to_older(self):
        for rows in (["wechat-drafts-123-attempt-2", {"name": "wechat-drafts-123-attempt-3", "expired": True}],
                     ["wechat-drafts-123", "wechat-drafts-123-attempt-3", "wechat-drafts-123-attempt-3"]):
            with self.subTest(rows=rows):
                self.assertFalse(self.choose(rows)["ok"])

    def test_missing_current_only_future_only_or_invalid_attempt_fails_closed(self):
        for rows, attempt in (([], 4), (["wechat-drafts-123-attempt-4"], 4),
                              (["wechat-drafts-123-attempt-5"], 4), (["wechat-drafts-123"], "bad")):
            with self.subTest(rows=rows, attempt=attempt):
                self.assertFalse(self.choose(rows, attempt)["ok"])


if __name__ == "__main__":
    unittest.main()
