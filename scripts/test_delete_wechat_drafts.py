"""Deleting a draft must invalidate only that draft's recovery receipt."""

import json
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import Mock, patch

import delete_wechat_drafts as delete
from push_portal_translated_to_wechat_drafts import WeChatError, saved_draft_receipt


class DeleteReceiptTests(unittest.TestCase):
    def fixture(self, root):
        summary_path = root / "wechat_draft_summary.json"
        payload = {"articles": [{"title": "中文文章", "author": "KC桌面", "content": "<p>正文</p>"}]}
        delete.write_json(root / "draft_payload_01.json", payload)
        delete.write_json(summary_path, {
            "dry_run": False, "draft_count": 2, "status": "verified",
            "drafts": [
                {"media_id": "FIRST", "payload": "draft_payload_01.json"},
                {"media_id": "SECOND", "payload": "draft_payload_02.json"},
            ],
        })
        return summary_path, payload

    def run_delete(self, summary_path, operation, *extra_args):
        argv = ["delete", "--summary", str(summary_path), "--output", str(summary_path.parent / "deleted.json"),
                "--wechat-appid", "TEST", "--wechat-secret", "TEST", *extra_args]
        with patch.object(sys, "argv", argv), patch.object(delete, "get_stable_access_token", return_value="TOKEN"), patch.object(delete, "delete_draft", operation):
            return delete.main()

    def test_successful_deletion_invalidates_reuse_and_preserves_audit_receipts(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            path, payload = self.fixture(root)
            self.assertEqual("FIRST", saved_draft_receipt(root, payload["articles"])["media_id"])
            operation = Mock(return_value={"errcode": 0})
            self.assertEqual(0, self.run_delete(path, operation))
            result = json.loads(path.read_text())
            self.assertEqual([], result["drafts"])
            self.assertEqual(0, result["draft_count"])
            self.assertEqual("deleted", result["status"])
            self.assertEqual(["FIRST", "SECOND"], [item["media_id"] for item in result["deleted_drafts"]])
            self.assertEqual({}, saved_draft_receipt(root, payload["articles"]))

    def test_partial_failure_checkpoints_first_deletion_before_next_request(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = self.fixture(Path(temporary))

            def operation(_session, _token, media_id, _timeout):
                if media_id == "SECOND":
                    current = json.loads(path.read_text())
                    self.assertEqual(["SECOND"], [item["media_id"] for item in current["drafts"]])
                    raise WeChatError("temporary API failure", errcode=-1)
                return {"errcode": 0}

            with self.assertRaises(WeChatError):
                self.run_delete(path, Mock(side_effect=operation))
            current = json.loads(path.read_text())
            self.assertEqual("partially_deleted", current["status"])
            self.assertEqual(1, current["draft_count"])
            diagnostic = json.loads((path.parent / "deleted.json").read_text())
            self.assertEqual([True, False], [item["deleted"] for item in diagnostic["results"]])

    def test_ignored_error_keeps_failed_id_available_for_a_later_attempt(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = self.fixture(Path(temporary))
            operation = Mock(side_effect=[WeChatError("invalid media_id", errcode=40007), {"errcode": 0}])
            self.assertEqual(0, self.run_delete(path, operation, "--ignore-delete-errors"))
            current = json.loads(path.read_text())
            self.assertEqual(["FIRST"], [item["media_id"] for item in current["drafts"]])
            self.assertEqual(["SECOND"], [item["media_id"] for item in current["deleted_drafts"]])

    def test_dry_run_never_changes_receipts_or_calls_delete_api(self):
        with tempfile.TemporaryDirectory() as temporary:
            path, _ = self.fixture(Path(temporary))
            original = path.read_bytes()
            operation = Mock()
            self.assertEqual(0, self.run_delete(path, operation, "--dry-run"))
            self.assertEqual(original, path.read_bytes())
            operation.assert_not_called()


if __name__ == "__main__":
    unittest.main()
