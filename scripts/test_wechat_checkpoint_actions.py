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
            self.assertIn("name: ${{ inputs.name }}" if name == "Upload diagnostic artifact" else "name: ${{ inputs.name }}-retry", block)

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
                              env={**os.environ, "CHECKPOINT_PATH": str(path), "CHECKPOINT_VALIDATOR": str(VALIDATOR), "PRIMARY_DOWNLOAD": "success"},
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
        self.assertIn("if: ${{ steps.locate.outputs.found == 'true' }}", RESTORE.read_text())

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


class CheckpointRestoreTests(unittest.TestCase):
    def choose(self, names, current=4, histories=None):
        import wechat_attempt_history as history
        artifacts = [{"name": item, "expired": False} if isinstance(item, str) else item for item in names]
        def jobs(attempt):
            if histories is None or attempt not in histories:
                raise history.HistoryError("Missing complete attempt history")
            return histories[attempt]
        return history.choose_checkpoint(artifacts, current, "wechat-drafts-123", jobs,
                                         "upload-wechat-drafts", ["Upload drafts"])

    def skipped(self):
        return [{"name": "upload-wechat-drafts", "status": "completed", "conclusion": "skipped"}]

    def not_started(self):
        return [{"name": "upload-wechat-drafts", "status": "completed", "conclusion": "failure", "steps": [
            {"name": "Restore accepted WeChat draft receipts", "status": "completed", "conclusion": "failure"},
            {"name": "Upload drafts", "status": "completed", "conclusion": "skipped"}]}]

    def test_latest_strictly_prior_attempt_wins_over_legacy_current_future_and_near_names(self):
        result = self.choose(["wechat-drafts-123", "wechat-drafts-123-attempt-1", "wechat-drafts-123-attempt-3",
                              "wechat-drafts-123-attempt-2", "wechat-drafts-123-attempt-4", "wechat-drafts-123-attempt-5",
                              "other-wechat-drafts-123-attempt-3", "wechat-drafts-123-attempt-3-extra"])
        self.assertEqual("wechat-drafts-123-attempt-3", result["artifact_name"])
        self.assertIn("name: ${{ steps.locate.outputs.artifact_name }}", RESTORE.read_text())

    def test_legacy_exact_name_and_immutable_retry_copy_are_supported(self):
        self.assertEqual("wechat-drafts-123", self.choose(["wechat-drafts-123"], current=2)["artifact_name"])
        self.assertEqual("wechat-drafts-123-attempt-3-retry",
            self.choose(["wechat-drafts-123-attempt-3-retry"])["artifact_name"])
        self.assertEqual("wechat-drafts-123-attempt-3",
            self.choose(["wechat-drafts-123-attempt-3-retry", "wechat-drafts-123-attempt-3"])["artifact_name"])

    def test_first_uploader_after_skipped_producer_or_restore_failures_needs_no_fictional_checkpoint(self):
        result = self.choose([], current=3, histories={1:self.skipped(),2:self.not_started()})
        self.assertEqual((result["found"],result["no_prior_submission"]),("false","true"))
        self.assertEqual(json.loads(result["checked_attempts"]),[2,1])
        self.assertEqual(self.choose([],current=2,histories={1:[]})["no_prior_submission"],"true")

    def test_older_receipts_are_usable_only_across_proven_non_submitting_gaps(self):
        result = self.choose(["wechat-drafts-123-attempt-1"], current=4,
                             histories={3:self.not_started(),2:self.skipped()})
        self.assertEqual(result["artifact_name"],"wechat-drafts-123-attempt-1")
        with self.assertRaises(ValueError):
            self.choose(["wechat-drafts-123-attempt-1"],current=4,histories={3:self.not_started()})

    def test_any_begun_uncertain_missing_or_duplicate_submission_step_blocks_without_receipts(self):
        for state in ("success","failure","cancelled",None):
            records=self.not_started()
            records[0]["steps"][1]["conclusion"]=state
            with self.subTest(state=state),self.assertRaises(ValueError):
                self.choose([],current=2,histories={1:records})
        for records in ([{"name":"upload-wechat-drafts","status":"completed","conclusion":"failure"}],
                        self.not_started()+self.not_started()):
            with self.subTest(records=records),self.assertRaises(ValueError):
                self.choose([],current=2,histories={1:records})

    def test_expired_or_duplicate_checkpoint_never_falls_back_to_older(self):
        for rows in (["wechat-drafts-123-attempt-2", {"name": "wechat-drafts-123-attempt-3", "expired": True}],
                     ["wechat-drafts-123-attempt-3", "wechat-drafts-123-attempt-3"]):
            with self.subTest(rows=rows),self.assertRaises(ValueError):
                self.choose(rows)

    def test_download_outage_requires_a_successful_read_before_validating_receipts(self):
        for primary,retry,expected in (("failure","failure",1),("failure","success",0),("success","skipped",0)):
            with self.subTest(primary=primary,retry=retry),tempfile.TemporaryDirectory() as tmp:
                root=Path(tmp)
                (root/"wechat_draft_summary.json").write_text(json.dumps(summary(root)))
                result=subprocess.run([sys.executable,"-c",step_script(RESTORE,"Validate restored delivery checkpoint")],
                    env={**os.environ,"CHECKPOINT_PATH":str(root),"CHECKPOINT_VALIDATOR":str(VALIDATOR),
                         "PRIMARY_DOWNLOAD":primary,"RETRY_DOWNLOAD":retry},capture_output=True,text=True)
                self.assertEqual(result.returncode,expected)
        self.assertIn("name: ${{ inputs.name }}-retry",ARCHIVE.read_text())
        self.assertNotIn("overwrite: true",ARCHIVE.read_text())


class GitHubHistoryTests(unittest.TestCase):
    def test_paginated_complete_jobs_do_not_hide_a_later_uploader(self):
        import io
        from unittest.mock import Mock
        from wechat_attempt_history import GitHubHistory
        first=[{"id":i,"name":"other"} for i in range(1,101)]
        last=[{"id":101,"name":"upload-wechat-drafts"}]
        request=Mock(side_effect=[io.BytesIO(json.dumps({"total_count":101,"jobs":rows}).encode()) for rows in (first,last)])
        reader=GitHubHistory("owner/repo",123,"secret",request=request)
        self.assertEqual(len(reader.jobs(1)),101)
        self.assertIn("page=2",request.call_args.args[0].full_url)

    def test_partial_missing_duplicate_or_changed_pagination_is_rejected(self):
        import io
        from unittest.mock import Mock
        from wechat_attempt_history import GitHubHistory
        for values in ([{"total_count":2,"jobs":[{"id":1}]},{"total_count":2,"jobs":[]}],
                       [{"total_count":2,"jobs":[{"id":1},{"id":1}]}],
                       [{"total_count":2,"jobs":[{"id":1}]},{"total_count":3,"jobs":[{"id":2}]}]):
            request=Mock(side_effect=[io.BytesIO(json.dumps(row).encode()) for row in values])
            with self.subTest(values=values),self.assertRaises(ValueError):
                GitHubHistory("owner/repo",123,"secret",request=request).jobs(1)

    def test_transient_gets_have_bounded_retries_and_authentication_never_retries(self):
        import io
        from urllib.error import HTTPError
        from unittest.mock import Mock
        from wechat_attempt_history import GitHubHistory
        request=Mock(side_effect=[HTTPError("https://api.github.com",503,"private",{},None),
                                 TimeoutError(),io.BytesIO(b'{"run_attempt":2}')])
        sleep=Mock()
        self.assertEqual(GitHubHistory("owner/repo",123,"secret",request=request,sleep=sleep).get(),{"run_attempt":2})
        self.assertEqual(request.call_count,3)
        self.assertEqual(sleep.call_count,2)
        request=Mock(side_effect=HTTPError("https://api.github.com",403,"private",{},None))
        with self.assertRaisesRegex(ValueError,"HTTP 403"):
            GitHubHistory("owner/repo",123,"secret",request=request,sleep=sleep).get()
        self.assertEqual(request.call_count,1)

    def test_persistent_service_or_invalid_json_outage_never_becomes_an_empty_history(self):
        import io
        from urllib.error import HTTPError
        from unittest.mock import Mock
        from wechat_attempt_history import GitHubHistory
        for failures in ([HTTPError('https://api.github.com',503,'private-body',{},None)
                          for _ in range(3)], [io.BytesIO(b'not-json') for _ in range(3)]):
            request, sleep = Mock(side_effect=failures), Mock()
            with self.subTest(failure=type(failures[0]).__name__), self.assertRaises(ValueError) as error:
                GitHubHistory('owner/repo',123,'private-token',request=request,sleep=sleep).artifacts()
            self.assertEqual((request.call_count,sleep.call_count),(3,2))
            self.assertNotIn('private-token',str(error.exception))
            self.assertNotIn('private-body',str(error.exception))


if __name__ == "__main__":
    unittest.main()
