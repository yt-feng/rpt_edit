#!/usr/bin/env python3
"""Restoration must preserve accepted IDs and never duplicate uncertain adds."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import requests

import restore_missing_wechat_drafts as restore
from push_portal_translated_to_wechat_drafts import WeChatError


def inventory(groups=(), complete=True):
    return {"complete": complete, "stop_reason": "end_of_inventory" if complete else "api_error",
            "articles": [{"group_id": identifier, "title": title} for identifier, titles in groups for title in titles]}


def response(data):
    result = requests.Response()
    result.status_code = 200
    result._content = json.dumps(data).encode()
    return result


class RestorationTests(unittest.TestCase):
    def drafts(self):
        return [{"media_id": "original", "articles": [
            {"title": "文章一", "author": "Author", "content": "private-body-one", "thumb_media_id": "cover"},
            {"title": "文章二", "author": "Author", "content": "private-body-two", "thumb_media_id": "cover"},
        ]}]

    def run_restore(self, output):
        return restore.restore_missing(self.drafts(), output, object(), "TOKEN", expected_articles=2)

    def test_single_add_persists_inflight_and_accepted_id_before_verification(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "restoration_summary.json"
            def add(*args, **kwargs):
                saved = json.loads(output.read_text())
                self.assertEqual("add_in_flight", saved["drafts"][0]["status"])
                self.assertTrue(args[1].startswith("https://api.weixin.qq.com/cgi-bin/draft/add?"))
                self.assertEqual(1, kwargs["max_attempts"])
                self.assertEqual("private-body-one", args[2]["articles"][0]["content"])
                return response({"media_id": "accepted"})
            def verify(*args, **kwargs):
                saved = json.loads(output.read_text())
                self.assertEqual("pending_verification", saved["drafts"][0]["status"])
                self.assertEqual("accepted", saved["drafts"][0]["media_id"])
                self.assertFalse(kwargs["repair_media"])
                return {"ok": True, "article_count": 2}
            with patch.object(restore, "scan_inventory", return_value=inventory()), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json", side_effect=add) as post, \
                    patch.object(restore, "verify_draft_get", side_effect=verify):
                result = self.run_restore(output)
            self.assertEqual(1, post.call_count)
            self.assertTrue(result["ok"])
            self.assertEqual(2, result["verified_article_count"])
            self.assertEqual("original", result["drafts"][0]["original_media_id"])
            self.assertFalse(result["publish"])
            self.assertNotIn("private-body", output.read_text())

    def test_ambiguous_add_recovers_from_independent_inventory_without_second_post(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(restore, "scan_inventory", side_effect=[inventory(), inventory(), inventory([("accepted", ["文章一", "文章二"])])]), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json", side_effect=requests.Timeout("TOKEN PRIVATE")) as post, \
                    patch.object(restore, "verify_draft_get", return_value={"ok": True, "article_count": 2}):
                report = self.run_restore(Path(tmp) / "receipt.json")
        self.assertTrue(report["ok"])
        self.assertTrue(report["drafts"][0]["recovered_after_ambiguous_add"])
        self.assertEqual(1, post.call_count)
        self.assertNotIn("TOKEN", json.dumps(report))
        self.assertNotIn("PRIVATE", json.dumps(report))

    def test_unknown_add_remains_blocked_on_resume_without_resubmission(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "receipt.json"
            with patch.object(restore, "scan_inventory", return_value=inventory()), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json", side_effect=requests.Timeout("TOKEN")) as post:
                first = self.run_restore(output)
                second = self.run_restore(output)
            self.assertFalse(first["ok"])
            self.assertFalse(second["ok"])
            self.assertEqual("add_outcome_unknown", second["drafts"][0]["status"])
            self.assertEqual(1, post.call_count)
            self.assertEqual("prior_add_outcome_unknown_no_resubmission", second["error"]["reason"])

    def test_pending_receipt_is_reverified_even_if_inventory_does_not_yet_show_it(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "receipt.json"
            with patch.object(restore, "scan_inventory", return_value=inventory()), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json", return_value=response({"media_id": "accepted"})) as post, \
                    patch.object(restore, "verify_draft_get", side_effect=[{"ok": False, "errcode": 40007}, {"ok": True, "article_count": 2}]) as verify:
                first = self.run_restore(output)
                second = self.run_restore(output)
            self.assertFalse(first["ok"])
            self.assertTrue(second["ok"])
            self.assertEqual(1, post.call_count)
            self.assertEqual(["accepted", "accepted"], [call.args[2] for call in verify.call_args_list])

    def test_complete_existing_group_reordered_is_reused_without_mutation(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(restore, "scan_inventory", return_value=inventory([("edited", ["文章二", "文章一"])])), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json") as post, \
                    patch.object(restore, "verify_draft_get", return_value={"ok": True, "article_count": 2}) as verify:
                report = self.run_restore(Path(tmp) / "receipt.json")
        self.assertTrue(report["ok"])
        self.assertTrue(report["drafts"][0]["reused_existing"])
        self.assertEqual(["文章二", "文章一"], [a["title"] for a in verify.call_args.args[5]])
        post.assert_not_called()

    def test_manual_edit_or_split_existing_titles_blocks_all_adds(self):
        cases = [[("edited", ["文章一"])], [("one", ["文章一"]), ("two", ["文章二"])],
                 [("one", ["文章一", "文章二"]), ("duplicate", ["文章一", "文章二"])]]
        for groups in cases:
            with self.subTest(groups=groups), tempfile.TemporaryDirectory() as tmp:
                with patch.object(restore, "scan_inventory", return_value=inventory(groups)), \
                        patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                        patch.object(restore, "post_wechat_json") as post:
                    report = self.run_restore(Path(tmp) / "receipt.json")
                self.assertFalse(report["ok"])
                self.assertEqual("existing_title_subset_or_duplicate_groups", report["error"]["reason"])
                post.assert_not_called()

    def test_original_get_provider_error_is_not_missing(self):
        for error in (WeChatError("invalid credential SECRET", errcode=40001), requests.Timeout("TOKEN")):
            with self.subTest(error=type(error).__name__), tempfile.TemporaryDirectory() as tmp:
                with patch.object(restore, "scan_inventory", return_value=inventory()), \
                        patch.object(restore, "get_draft", side_effect=error), patch.object(restore, "post_wechat_json") as post:
                    report = self.run_restore(Path(tmp) / "receipt.json")
                self.assertFalse(report["ok"])
                post.assert_not_called()
                self.assertNotIn("SECRET", json.dumps(report))
                self.assertNotIn("TOKEN", json.dumps(report))

    def test_incomplete_inventory_and_changed_source_fail_closed(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "receipt.json"
            with patch.object(restore, "scan_inventory", return_value=inventory(complete=False)), \
                    patch.object(restore, "post_wechat_json") as post:
                report = self.run_restore(output)
            self.assertFalse(report["ok"])
            post.assert_not_called()
            previous = output.read_text()
            changed = self.drafts()
            changed[0]["articles"][0]["content"] = "different source"
            with self.assertRaises(restore.RestoreBlocked):
                restore.restore_missing(changed, output, object(), "TOKEN", expected_articles=2)
            self.assertEqual(previous, output.read_text())

    def test_existing_original_with_manual_author_change_is_never_replaced(self):
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(restore, "scan_inventory", return_value=inventory([("original", ["文章一", "文章二"])])), \
                    patch.object(restore, "get_draft", return_value={"news_item": []}), \
                    patch.object(restore, "post_wechat_json") as post, \
                    patch.object(restore, "verify_draft_get", return_value={"ok": False, "matches_editorial_contract": False}):
                report = self.run_restore(Path(tmp) / "receipt.json")
        self.assertFalse(report["ok"])
        self.assertEqual("original", report["drafts"][0]["media_id"])
        post.assert_not_called()

    def test_all_groups_are_checked_for_partial_edits_before_any_creation(self):
        drafts = self.drafts() + [{"media_id": "original-two", "articles": [{"title": "文章三"}, {"title": "文章四"}]}]
        with tempfile.TemporaryDirectory() as tmp:
            with patch.object(restore, "scan_inventory", return_value=inventory([("edited-subset", ["文章三"])])), \
                    patch.object(restore, "get_draft", side_effect=WeChatError("missing", errcode=40007)), \
                    patch.object(restore, "post_wechat_json") as post:
                report = restore.restore_missing(drafts, Path(tmp) / "receipt.json", object(), "TOKEN", expected_articles=4)
        self.assertFalse(report["ok"])
        post.assert_not_called()

    def test_restore_requires_complete_verified_source_receipt(self):
        original = self.drafts()[0]
        receipt = {"status": "verified", "publish": False, "dry_run": False, "drafts": [{
            "media_id": "original", "status": "verified", "published": False, "publish_id": "",
            "draft_get": {"ok": True, "matches_expected_article_count": True, "matches_expected_titles": True,
                          "matches_editorial_contract": True, "matches_media_contract": True,
                          "article_count": 2, "expected_article_count": 2, "titles": ["文章一", "文章二"]},
        }]}
        changes = [("status", "pending"), ("publish", True), ("dry_run", True),
                   ("matches_media_contract", False), ("article_count", 1), ("titles", ["unrelated"]), ("ok", False)]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            path = root / "wechat_draft_summary.json"
            path.write_text(json.dumps(receipt))
            restore.validate_source_receipts(root, [original])
            for key, value in changes:
                changed = json.loads(json.dumps(receipt))
                target = changed if key in {"status", "publish", "dry_run"} else changed["drafts"][0]["draft_get"]
                target[key] = value
                path.write_text(json.dumps(changed))
                with self.subTest(key=key), self.assertRaises(restore.RestoreBlocked):
                    restore.validate_source_receipts(root, [original])


if __name__ == "__main__":
    unittest.main()
