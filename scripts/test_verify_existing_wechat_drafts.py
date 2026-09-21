#!/usr/bin/env python3
"""Regression checks for verifying archived drafts without uploading again."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import verify_existing_wechat_drafts as verifier


class ExistingDraftTests(unittest.TestCase):
    def make_archive(self, root: Path) -> Path:
        folder = root / "wechat_drafts" / "xhs_notes" / "260913"
        folder.mkdir(parents=True)
        (folder / "draft_payload_01.json").write_text(json.dumps({"articles": [
            {"title": "银行研究", "author": "KC桌面", "content": "<p>中文正文。</p>"},
        ]}, ensure_ascii=False), encoding="utf-8")
        summary = folder / "wechat_draft_summary.json"
        summary.write_text(json.dumps({"dry_run": False, "drafts": [{
            "media_id": "existing-draft", "article_count": 1,
            "payload": "wechat_drafts/xhs_notes/260913/draft_payload_01.json",
        }]}), encoding="utf-8")
        return summary

    def test_archived_payloads_are_read_and_only_existing_ids_verified(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.make_archive(root)
            drafts = verifier.load_drafts(root)
            session = object()
            with patch.object(verifier, "verify_draft_get", return_value={"ok": True, "article_count": 1}) as readback:
                report = verifier.verify_existing(drafts, session, "token", 30)
            self.assertTrue(report["ok"])
            self.assertEqual(1, report["verified_article_count"])
            self.assertTrue(report["read_only"])
            self.assertEqual((session, "token", "existing-draft", 30, 1), readback.call_args.args[:5])
            self.assertEqual("银行研究", readback.call_args.args[5][0]["title"])
            self.assertNotIn("media_id", report["drafts"][0])

    def test_any_failed_draft_makes_whole_result_fail(self):
        drafts = [{"media_id": "one", "articles": [{"title": "一"}]}, {"media_id": "two", "articles": [{"title": "二"}]}]
        with patch.object(verifier, "verify_draft_get", side_effect=[
            {"ok": False, "article_count": 1}, {"ok": True, "article_count": 1},
        ]) as readback:
            report = verifier.verify_existing(drafts, object(), "token", 30)
        self.assertFalse(report["ok"])
        self.assertEqual(2, readback.call_count)
        self.assertEqual(1, report["verified_article_count"])
        self.assertEqual(2, report["expected_article_count"])

    def test_missing_summary_and_empty_drafts_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            with self.assertRaises(ValueError):
                verifier.load_drafts(root)
            (root / "wechat_draft_summary.json").write_text('{"drafts": []}')
            with self.assertRaises(ValueError):
                verifier.load_drafts(root)

    def test_dry_run_and_mismatched_payload_count_fail(self):
        for changes in ({"dry_run": True}, {"article_count": 2}, {"media_id": ""}):
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                path = self.make_archive(root)
                summary = json.loads(path.read_text())
                if "dry_run" in changes:
                    summary.update(changes)
                else:
                    summary["drafts"][0].update(changes)
                path.write_text(json.dumps(summary))
                with self.assertRaises(ValueError):
                    verifier.load_drafts(root)

    def test_duplicate_media_ids_fail(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = self.make_archive(root)
            summary = json.loads(path.read_text())
            summary["drafts"].append(dict(summary["drafts"][0]))
            path.write_text(json.dumps(summary))
            with self.assertRaises(ValueError):
                verifier.load_drafts(root)

    def test_symlink_payload_outside_artifact_fails(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp) / "artifact"
            path = self.make_archive(root)
            payload = path.parent / "draft_payload_01.json"
            outside = Path(tmp) / "outside.json"
            payload.rename(outside)
            payload.symlink_to(outside)
            with self.assertRaises(ValueError):
                verifier.load_drafts(root)

    def test_all_upload_diagnostics_survive_failed_readback(self):
        root = Path(__file__).resolve().parents[1] / ".github" / "workflows"
        checked = 0
        for path in root.glob("*.yml"):
            for step in path.read_text().split("      - name: "):
                if step.startswith(("Archive WeChat draft diagnostics\n", "Archive WeChat draft maintenance diagnostics\n")):
                    self.assertIn("if: ${{ always() }}", step, str(path))
                    checked += 1
        self.assertEqual(9, checked)

    def test_portal_diagnostic_directory_is_set_before_upload_can_fail(self):
        root = Path(__file__).resolve().parents[1] / ".github" / "workflows"
        workflow = (root / "dropbox-latest-pdf-to-xhs-sharded.yml").read_text()
        step = workflow.split("      - name: Upload Portal translated reports to WeChat drafts\n", 1)[1].split("      - name: ", 1)[0]
        self.assertLess(step.index('echo "WECHAT_DRAFT_DIR='), step.index("python scripts/push_portal_translated_to_wechat_drafts.py"))

    def test_readback_checkout_includes_workflow_contract_tests(self):
        root = Path(__file__).resolve().parents[1] / ".github" / "workflows"
        workflow = (root / "wechat-draft-readback.yml").read_text()
        checkout = workflow.split("      - name: Checkout verification code\n", 1)[1].split("      - uses: actions/setup-python", 1)[0]
        self.assertIn(".github/workflows", checkout)

    def test_intentional_maintenance_deletion_follows_receipt_restore(self):
        root = Path(__file__).resolve().parents[1] / ".github" / "workflows"
        workflow = (root / "portal-wechat-draft-maintenance.yml").read_text()
        self.assertLess(workflow.index("      - name: Restore accepted WeChat draft receipts"), workflow.index("      - name: Delete existing WeChat drafts from summary"))


if __name__ == "__main__":
    unittest.main()
