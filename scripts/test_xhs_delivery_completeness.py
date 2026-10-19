#!/usr/bin/env python3
"""Missing article bodies cannot turn a successful source plan into green delivery."""

import contextlib
import io
import json
from pathlib import Path
import sys
import tempfile
import unittest
from unittest.mock import patch

import push_xhs_notes_to_wechat_drafts as uploader


class DeliveryCompletenessTests(unittest.TestCase):
    def add_report(self, root, index, text):
        directory = root / "source" / "261019" / "shard_0" / f"{index:04d}-GS-report"
        directory.mkdir(parents=True)
        if text is not None:
            (directory / "wechat_article.md").write_text(text, encoding="utf-8")
        return directory

    def arguments(self, root, *extra):
        return ["push_xhs_notes_to_wechat_drafts.py", "--dropbox-output-root", str(root / "source"),
                "--date-folder", "261019", "--output-root", str(root / "output"),
                "--trailing-image", "", "--site-url", "https://private.example.invalid",
                "--wechat-appid", "test-appid", "--wechat-secret", "test-secret",
                "--article-delay-seconds", "0", "--draft-verify-delay-seconds", "0", *extra]

    def summary(self, root):
        return json.loads((root / "output" / "261019" / "wechat_draft_summary.json").read_text())

    def build_article(self, report_dir, *_args, **_kwargs):
        title = f"高盛：人工智能基础设施订单增长{report_dir.name[:4]}"
        return {"title": title, "wechat_title": title, "raw_title": title, "institution_name": "高盛",
                "source_report_name": report_dir.name, "report_dir": str(report_dir), "title_decision": {},
                "article": {"article_type": "news", "title": title, "author": uploader.AUTHOR,
                            "content": "<p>有数据支撑的完整正文。</p>", "thumb_media_id": "cover"},
                "content_chars": 20, "content_bytes": 40, "visible_text_chars": 12,
                "inline_images": [], "body_image_count": 0, "cover_image": ""}

    def test_empty_selection_fails_without_authentication(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "source" / "261019").mkdir(parents=True)
            with patch.object(sys, "argv", self.arguments(root)), patch.object(uploader, "requests") as requests, \
                    patch.object(uploader, "get_stable_access_token") as token, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, uploader.main())
            requests.Session.assert_not_called()
            token.assert_not_called()
            self.assertEqual("failed_no_xhs_wechat_articles", self.summary(root)["status"])

    def test_missing_report_markdown_fails_bound_source_count_before_upload(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.add_report(root, 1, "# 高盛：人工智能订单增长\n完整正文。")
            self.add_report(root, 2, None)
            with patch.object(sys, "argv", self.arguments(root, "--expected-source-count", "2")), \
                    patch.object(uploader, "requests") as requests, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, uploader.main())
            requests.Session.assert_not_called()
            summary = self.summary(root)
            self.assertEqual("failed_source_count_mismatch", summary["status"])
            self.assertEqual((2, 1), (summary["expected_source_count"], summary["source_report_count"]))

    def test_placeholder_empty_and_heading_only_bodies_fail_without_api_calls(self):
        for markdown in ("# 高盛：基础设施投资\nDeepSeek 生成内容失败，请复制对应 prompt", "", "# 高盛：基础设施投资\n\n", "# 高盛：基础设施投资\n![](image.png)"):
            with self.subTest(markdown=markdown), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                self.add_report(root, 1, markdown)
                with patch.object(sys, "argv", self.arguments(root)), patch.object(uploader, "requests") as requests, \
                        patch.object(uploader, "build_article") as build, contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(1, uploader.main())
                requests.Session.assert_not_called()
                build.assert_not_called()
                summary = self.summary(root)
                self.assertEqual("failed_generation_failure", summary["status"])
                self.assertEqual(1, summary["skipped_generation_failure_count"])

    def test_partial_generation_failure_keeps_verified_id_but_returns_failure(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            good = self.add_report(root, 1, "# 高盛：人工智能订单增长\n完整正文。")
            self.add_report(root, 2, "# 高盛：基础设施投资\nDeepSeek 生成内容失败")
            with patch.object(sys, "argv", self.arguments(root, "--expected-source-count", "2")), \
                    patch.object(uploader, "requests") as requests, \
                    patch.object(uploader, "get_stable_access_token", return_value="test-token"), \
                    patch.object(uploader, "build_article", side_effect=self.build_article) as build, \
                    patch.object(uploader, "saved_draft_receipt", return_value={"media_id": "already-accepted"}), \
                    patch.object(uploader, "verify_draft_get", return_value={"ok": True, "article_count": 1}), \
                    contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(1, uploader.main())
            self.assertEqual([good], [call.args[0] for call in build.call_args_list])
            requests.Session.return_value.post.assert_not_called()
            summary = self.summary(root)
            self.assertEqual("partial_generation_failure", summary["status"])
            self.assertEqual((2, 1, 1), (summary["input_selected_count"], summary["selected_count"], summary["skipped_generation_failure_count"]))
            self.assertEqual("already-accepted", summary["drafts"][0]["media_id"])
            self.assertEqual("verified", summary["drafts"][0]["status"])
            self.assertTrue(summary["drafts"][0]["draft_get"]["ok"])

    def test_policy_exclusion_is_independent_and_does_not_claim_draft_delivery(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            self.add_report(root, 1, "# 高盛：人民币定价机制出现变化\n完整正文。")
            with patch.object(sys, "argv", self.arguments(root, "--expected-source-count", "1")), \
                    patch.object(uploader, "requests") as requests, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, uploader.main())
            requests.Session.assert_not_called()
            summary = self.summary(root)
            self.assertEqual("skipped_title_policy", summary["status"])
            self.assertEqual((1, 0, 0), (summary["skipped_title_policy_count"], summary["skipped_generation_failure_count"], summary["draft_count"]))

    def test_expected_source_count_is_checked_before_limit_and_offset(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for index in range(1, 4):
                self.add_report(root, index, f"# 高盛：人工智能订单增长{index}\n完整正文。")
            with patch.object(sys, "argv", self.arguments(root, "--expected-source-count", "3", "--article-offset", "1", "--max-articles", "1", "--dry-run")), \
                    patch.object(uploader, "build_article", side_effect=self.build_article) as build, contextlib.redirect_stdout(io.StringIO()):
                self.assertEqual(0, uploader.main())
            summary = self.summary(root)
            self.assertEqual((3, 3, 1), (summary["expected_source_count"], summary["source_report_count"], summary["input_selected_count"]))
            self.assertEqual("0002-GS-report", build.call_args.args[0].name)

    def test_early_failure_preserves_legacy_accepted_ids_and_payloads(self):
        for scenario in ("empty", "source_count", "generation_failure"):
            with self.subTest(scenario=scenario), tempfile.TemporaryDirectory() as tmp:
                root = Path(tmp)
                (root / "source" / "261019").mkdir(parents=True)
                extra = []
                if scenario == "source_count":
                    extra = ["--expected-source-count", "1"]
                elif scenario == "generation_failure":
                    self.add_report(root, 1, "# 高盛：基础设施投资\nDeepSeek 生成内容失败")
                output = root / "output" / "261019"
                output.mkdir(parents=True)
                payload = output / "draft_payload_01.json"
                payload.write_text('{"articles":[{"title":"Earlier accepted article"}]}')
                original_payload = payload.read_bytes()
                previous = {"date_folder": "261019", "dry_run": False, "status": "verified", "draft_count": 1,
                            "drafts": [{"media_id": "legacy-accepted-id", "status": "verified", "article_count": 1,
                                        "payload": str(payload), "group_key": "legacy-source-key", "draft_get": {"ok": True}}]}
                (output / "wechat_draft_summary.json").write_text(json.dumps(previous))
                with patch.object(sys, "argv", self.arguments(root, *extra)), patch.object(uploader, "requests") as requests, \
                        contextlib.redirect_stdout(io.StringIO()):
                    self.assertEqual(1, uploader.main())
                requests.Session.assert_not_called()
                summary = self.summary(root)
                self.assertTrue(summary["status"].startswith("failed_"))
                self.assertEqual("legacy-accepted-id", summary["drafts"][0]["media_id"])
                self.assertEqual("legacy-source-key", summary["drafts"][0]["group_key"])
                self.assertTrue(summary["drafts"][0]["readback_from_previous_attempt"])
                self.assertEqual((1, 0, 0), (summary["preserved_previous_draft_count"],
                                            summary["current_run_verified_draft_count"], summary["current_run_verified_article_count"]))
                self.assertEqual(original_payload, payload.read_bytes())

    def test_unreadable_or_different_date_receipt_is_never_overwritten(self):
        for original in ("{broken", '{"date_folder":"261018","drafts":[]}'):
            with self.subTest(original=original), tempfile.TemporaryDirectory() as tmp:
                output = Path(tmp) / "261019"
                output.mkdir()
                receipt = output / "wechat_draft_summary.json"
                receipt.write_text(original)
                with self.assertRaises(RuntimeError):
                    uploader.write_early_delivery_summary(output, {"status": "failed_no_xhs_wechat_articles"})
                self.assertEqual(original, receipt.read_text())
                self.assertTrue((output / "wechat_delivery_failure.json").exists())


if __name__ == "__main__":
    unittest.main()
