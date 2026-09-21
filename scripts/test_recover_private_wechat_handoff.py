#!/usr/bin/env python3
"""Recovery must reuse only a complete handoff from a producer that never uploaded."""
import copy
import json
import shutil
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import recover_private_wechat_handoff as recovery
from private_workflow_handoff import create_archive


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.run = {
            "id": 35545560867, "path": recovery.SOURCES["institution"][1],
            "head_branch": "main", "head_repository": {"full_name": "yt-feng/rpt_edit"},
            "status": "completed", "conclusion": "failure", "run_attempt": 1,
        }
        self.jobs = {"jobs": [
            {"name": "fetch-and-build", "steps": [
                {"name": "Build Portal translated report PDFs", "conclusion": "success"},
                {"name": "Upload translated reports to private R2 handoff", "conclusion": "success"},
            ]},
            {"name": "upload-wechat-drafts", "conclusion": "skipped"},
        ]}

    def validate_run(self, run=None, jobs=None):
        recovery.validate_run(run or self.run, jobs or self.jobs, source="institution",
                              run_id="35545560867", repository="yt-feng/rpt_edit")

    def test_exact_blocked_producer_is_allowed(self):
        self.validate_run()

    def test_prior_or_unknown_attempts_cannot_hide_earlier_uploads(self):
        for attempt in (None, 2, 3):
            with self.subTest(attempt=attempt):
                run = {**self.run, "run_attempt": attempt}
                if attempt is None:
                    del run["run_attempt"]
                with self.assertRaisesRegex(ValueError, "prior or unknown attempts require review"):
                    self.validate_run(run=run)

    def test_other_workflow_branch_repository_run_or_success_is_rejected(self):
        for key, value in (("path", recovery.SOURCES["consulting"][1]), ("head_branch", "test"),
                           ("head_repository", {"full_name": "other/repository"}),
                           ("id", 12), ("conclusion", "success"), ("status", "in_progress")):
            with self.subTest(key=key):
                changed = {**self.run, key: value}
                with self.assertRaises(ValueError):
                    self.validate_run(run=changed)

    def test_any_upload_attempt_or_missing_handoff_blocks_recovery(self):
        for conclusion in ("success", "failure", "cancelled", None):
            with self.subTest(conclusion=conclusion):
                jobs = copy.deepcopy(self.jobs)
                jobs["jobs"][1]["conclusion"] = conclusion
                with self.assertRaises(ValueError):
                    self.validate_run(jobs=jobs)
        jobs = copy.deepcopy(self.jobs)
        jobs["jobs"][0]["steps"][1]["conclusion"] = "failure"
        with self.assertRaises(ValueError):
            self.validate_run(jobs=jobs)

    def write_handoff(self, root, *, date="260921", scope="institutions", count=2):
        reports = []
        for index in range(count):
            report = root / f"report-{index}"
            report.mkdir()
            (report / "translated.md").write_text("# Completed article\nBody", encoding="utf-8")
            (report / "translation_status.json").write_text(json.dumps({
                "source_report_dir": f"xhs_notes/{scope}/{date}/source-{index}",
                "translated_markdown": "translated.md",
            }))
            reports.append({"output_dir": f"portal_translated_reports/{scope}/{date}/{report.name}"})
        (root / "translation_summary.json").write_text(json.dumps({
            "date_folder": date, "successful_count": count, "reports": reports, "failures": [],
        }))

    def test_complete_manifest_count_is_required(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.write_handoff(root)
            recovery.validate_translations(root, "institutions", "260921", 2)
            for expected in (0, 1, 3):
                with self.assertRaises(ValueError):
                    recovery.validate_translations(root, "institutions", "260921", expected)
            (root / "report-1" / "translated.md").unlink()
            with self.assertRaises(ValueError):
                recovery.validate_translations(root, "institutions", "260921", 2)

    def test_other_scope_date_and_empty_article_are_rejected(self):
        for changed in ("scope", "date", "empty"):
            with self.subTest(changed=changed), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.write_handoff(root, scope="consulting" if changed == "scope" else "institutions",
                                   date="260920" if changed == "date" else "260921")
                if changed == "empty":
                    (root / "report-0" / "translated.md").write_text("")
                with self.assertRaises(ValueError):
                    recovery.validate_translations(root, "institutions", "260921", 2)

    def test_only_absent_receipt_is_optional(self):
        client = Mock()
        for code in ("404", "NoSuchKey", "AccessDenied", "503"):
            error = RuntimeError(code)
            error.response = {"Error": {"Code": code}}
            client.head_object.side_effect = error
            with self.subTest(code=code):
                if code in ("404", "NoSuchKey"):
                    self.assertFalse(recovery.restore_receipts("prefix", Path("unused"), client=client, bucket="test"))
                else:
                    with self.assertRaises(RuntimeError):
                        recovery.restore_receipts("prefix", Path("unused"), client=client, bucket="test")

    def test_existing_receipts_restore_the_same_source_checkpoint(self):
        client = Mock()
        with patch.object(recovery, "download_directory") as download, patch.object(recovery, "merge_receipts") as merge:
            self.assertTrue(recovery.restore_receipts("exact/source", Path("receipts"), client=client, bucket="test"))
            self.assertEqual(download.call_args.args[0], "exact/source/recovery-receipts.tar.gz")
            self.assertNotEqual(download.call_args.args[1], Path("receipts"))
            merge.assert_called_once_with(Path("receipts"), download.call_args.args[1])

    def write_receipts(self, directory, entries):
        directory.mkdir(parents=True, exist_ok=True)
        drafts = []
        for index, (media_id, group_key, title) in enumerate(entries, 1):
            filename = f"draft_payload_{index:02d}.json"
            (directory / filename).write_text(json.dumps({"articles": [{"title": title}]}))
            drafts.append({"media_id": media_id, "group_key": group_key, "payload": filename, "article_count": 1})
        summary = {"date_folder": "260921", "dry_run": False, "drafts": drafts}
        (directory / "wechat_draft_summary.json").write_text(json.dumps(summary))
        return summary

    def test_private_receipts_roundtrip_preserves_expected_nested_output_path(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            original = root / "original-receipts"
            self.write_receipts(original, [("accepted-123", "stable-key", "Accepted title")])
            archive = root / "receipts.tar.gz"
            _, size, digest = create_archive(original, archive)
            client = Mock()
            client.head_object.return_value = {"ContentLength": size, "Metadata": {"sha256": digest}}
            client.download_file.side_effect = lambda bucket, key, destination: shutil.copyfile(archive, destination)
            destination = root / "wechat_drafts" / "institutions" / "260921"
            recovery.restore_receipts("exact/source", destination, client=client, bucket="test")
            summary = json.loads((destination / "wechat_draft_summary.json").read_text())
            self.assertEqual(summary["drafts"][0]["media_id"], "accepted-123")
            self.assertTrue((destination / summary["drafts"][0]["payload"]).is_file())
            self.assertEqual(len(list(destination.rglob("wechat_draft_summary.json"))), 1)

    def test_stale_r2_or_stale_diagnostics_preserve_every_accepted_draft(self):
        first = ("accepted-1", "group-1", "First title")
        second = ("accepted-2", "group-2", "Second title")
        for local_entries, r2_entries in (([first, second], [first]), ([first], [first, second]), ([first], [second])):
            with self.subTest(local=local_entries, r2=r2_entries), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                local, restored = root / "local", root / "restored"
                self.write_receipts(local, local_entries)
                self.write_receipts(restored, r2_entries)
                recovery.merge_receipts(local, restored)
                merged = json.loads((local / "wechat_draft_summary.json").read_text())["drafts"]
                self.assertEqual({draft["media_id"] for draft in merged}, {"accepted-1", "accepted-2"})
                self.assertEqual(len({draft["payload"] for draft in merged}), 2)
                self.assertEqual({json.loads((local / draft["payload"]).read_text())["articles"][0]["title"] for draft in merged}, {"First title", "Second title"})

    def test_conflicting_media_or_payload_does_not_modify_local_receipts(self):
        for conflicting in (("different-media", "group-1", "Title"), ("accepted-1", "group-1", "Different title")):
            with self.subTest(conflicting=conflicting), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                local, restored = root / "local", root / "restored"
                before = self.write_receipts(local, [("accepted-1", "group-1", "Title")])
                self.write_receipts(restored, [conflicting])
                with self.assertRaisesRegex(ValueError, "Conflicting"):
                    recovery.merge_receipts(local, restored)
                self.assertEqual(json.loads((local / "wechat_draft_summary.json").read_text()), before)

    def test_empty_early_failure_never_overwrites_accepted_private_receipts(self):
        with tempfile.TemporaryDirectory() as tmp, patch.object(recovery, "upload_directory") as upload:
            receipts = Path(tmp)
            self.assertFalse(recovery.save_receipts("source", receipts))
            self.write_receipts(receipts, [])
            self.assertFalse(recovery.save_receipts("source", receipts))
            upload.assert_not_called()
            self.write_receipts(receipts, [("accepted-1", "group-1", "Title")])
            self.assertTrue(recovery.save_receipts("source", receipts))
            upload.assert_called_once_with(receipts, "source/recovery-receipts.tar.gz")

    def test_workflow_preserves_receipts_before_blog_and_never_regenerates_or_publishes(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/recover-private-wechat-handoff.yml").read_text()
        self.assertIn("'institution-latest-pdf-to-wechat' || 'consulting-latest-pdf-to-wechat'", workflow)
        self.assertIn("always() && steps.restore.outcome == 'success'", workflow)
        self.assertLess(workflow.index("save-receipts"), workflow.index("Update public Blog archive"))
        self.assertLess(workflow.index("restore-wechat-diagnostics"), workflow.index("id: restore"))
        for forbidden in ("--publish", "build_portal_translated_reports.py", "fetch_institution_latest_pdfs.py", "delete-prefix"):
            self.assertNotIn(forbidden, workflow)

    def test_coordinates_reject_traversal_and_invalid_dates(self):
        for run_id, date in (("../7", "260921"), ("1", "260932"), ("1", "26/921")):
            with self.assertRaises(ValueError):
                recovery.coordinates("institution", run_id, date)


if __name__ == "__main__":
    unittest.main()
