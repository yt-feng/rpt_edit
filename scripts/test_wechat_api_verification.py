"""Regression coverage for UTF-8 readback and recoverable draft delivery."""

from __future__ import annotations

import copy
import json
import sys
import tempfile
import traceback
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import Mock, patch

import requests

import push_portal_translated_to_wechat_drafts as portal
import push_xhs_notes_to_wechat_drafts as xhs


def article() -> dict:
    return {
        "title": "巴克莱：AI音乐生成服务更像Roblox而非Spotify",
        "author": "KC桌面",
        "content": (
            f"<p>{portal.BRAND}</p><p>报告指出，服务用户规模持续增长。</p>"
            f"<p>{portal.BOTTOM_DISCLAIMER}</p><p>撰稿：Olivia</p>"
            "<p>责编：KC</p><p>排版：胡桃</p>"
        ),
        "thumb_media_id": "thumb-one",
    }


def response(data, *, status=200, encoding="ISO-8859-1") -> requests.Response:
    result = requests.Response()
    result.status_code = status
    result.encoding = encoding
    result.headers["Content-Type"] = "text/plain"
    result._content = json.dumps(data, ensure_ascii=False).encode("utf-8")
    return result


class WeChatJsonTests(unittest.TestCase):
    def test_actual_chinese_title_and_footer_survive_latin1_http_default(self):
        expected = article()
        raw = response({"news_item": [expected]})
        # Reproduce the September 14 diagnostics before exercising the fix.
        self.assertEqual("KCæ¡\x8cé\x9d¢", raw.json()["news_item"][0]["author"])
        parsed = portal.parse_wechat_json(raw, "draft/get")
        self.assertEqual(expected, parsed["news_item"][0])
        summary = portal.summarize_draft_get_response(parsed, 1, [expected])
        self.assertTrue(summary["ok"])
        self.assertTrue(summary["matches_expected_titles"])
        self.assertTrue(summary["matches_editorial_contract"])

    def test_bom_is_allowed_but_malformed_utf8_json_shapes_are_rejected(self):
        bom = response({"errcode": 0})
        bom._content = b"\xef\xbb\xbf" + bom.content
        self.assertEqual({"errcode": 0}, portal.parse_wechat_json(bom, "test"))
        bad_responses = [response([]), response(None), response("wrong"), response({}, status=503)]
        for raw_bytes in (b"<html>unavailable</html>", b'{"title":"\xff"}'):
            bad = response({})
            bad._content = raw_bytes
            bad_responses.append(bad)
        for bad in bad_responses:
            with self.subTest(body=bad.content, status=bad.status_code):
                with self.assertRaises(portal.WeChatError):
                    portal.parse_wechat_json(bad, "draft/get")

    def test_api_error_message_is_decoded_and_transient_error_remains_retryable(self):
        raw = response({"errcode": -1, "errmsg": "系统繁忙"})
        self.assertIn("系统繁忙", portal.retryable_wechat_json_error(raw))
        with self.assertRaisesRegex(portal.WeChatError, "系统繁忙"):
            portal.parse_wechat_json(raw, "draft/get")
        self.assertEqual("", portal.retryable_wechat_json_error(response([])))

    def test_batchget_failure_cannot_be_mistaken_for_no_existing_draft(self):
        with patch.object(portal, "batchget_recent_drafts", side_effect=portal.WeChatError("read failed")):
            with self.assertRaisesRegex(portal.WeChatError, "read failed"):
                portal.find_recent_draft_by_titles(object(), "TOKEN", [article()["title"]], 30)
        for data in ({"total_count": 5}, {"item": [None]}, {"item": [], "total_count": 1}):
            with self.subTest(data=data), patch.object(portal, "post_wechat_json", return_value=response(data)):
                with self.assertRaises(portal.WeChatError):
                    portal.batchget_recent_drafts(object(), "TOKEN", 30)

    def test_utf8_remote_duplicate_lookup_reuses_the_existing_id(self):
        expected = article()
        raw = response({"total_count": 1, "item": [{"media_id": "EXISTING", "content": {"news_item": [expected]}}]})
        with patch.object(portal, "post_wechat_json", return_value=raw):
            found = portal.find_recent_draft_by_titles(object(), "TOKEN", [expected["title"]], 30, expected_articles=[expected])
        self.assertEqual("EXISTING", found)

    def test_incomplete_batchget_item_is_not_treated_as_a_missing_match(self):
        items = [
            {"media_id": "EXISTING"},
            {"media_id": "EXISTING", "content": {"news_item": [None]}},
            {"media_id": "EXISTING", "content": {"news_item": []}},
            {"media_id": "", "content": {"news_item": [article()]}},
            {"media_id": "EXISTING", "content": {"news_item": [{"title": "", "content": "body"}]}},
            {"media_id": "EXISTING", "content": {"news_item": [{"title": article()["title"]}]}},
        ]
        for item in items:
            with self.subTest(item=item), patch.object(portal, "post_wechat_json", return_value=response({"total_count": 1, "item": [item]})):
                with self.assertRaisesRegex(portal.WeChatError, "incomplete draft content"):
                    portal.find_recent_draft_by_titles(object(), "TOKEN", [article()["title"]], 30, expected_articles=[article()])

    def test_ambiguous_add_timeout_recovers_without_a_second_create(self):
        with (
            patch.object(portal, "post_wechat_json", side_effect=portal.WeChatError("wechat/json request failed")) as post,
            patch.object(portal, "recover_draft_after_ambiguous_add", return_value="ACCEPTED") as recover,
        ):
            self.assertEqual("ACCEPTED", portal.add_draft(object(), "TOKEN", [article()], 30))
        self.assertEqual(1, post.call_count)
        recover.assert_called_once()


class WeChatReadbackTests(unittest.TestCase):
    def test_temporary_non_json_response_is_retried_using_get_only(self):
        session = Mock()
        malformed = response({})
        malformed._content = b"temporary gateway response"
        session.post.side_effect = [malformed, response({"news_item": [article()]})]
        with patch.object(portal, "sleep_before_wechat_retry") as pause:
            result = portal.verify_draft_get(session, "TOKEN", "EXISTING", 30, 1, [article()])
        self.assertTrue(result["ok"])
        self.assertEqual(2, result["attempts"])
        self.assertEqual(1, pause.call_count)
        for call in session.post.call_args_list:
            self.assertIn("/draft/get?", call.args[0])

    def test_transport_retries_are_bounded_and_never_log_success(self):
        session = Mock()
        session.post.side_effect = requests.Timeout("timed out")
        with patch.object(portal, "sleep_before_wechat_retry"), patch.object(portal, "log") as log:
            result = portal.verify_draft_get(session, "TOKEN", "EXISTING", 30, 1, [article()])
        self.assertFalse(result["ok"])
        self.assertEqual(3, result["attempts"])
        self.assertEqual(3, session.post.call_count)
        self.assertFalse(any("Verified draft/get" in call.args[0] for call in log.call_args_list))

    def test_token_bearing_transport_errors_never_reach_logs_summaries_or_tracebacks(self):
        token = "DYNAMIC_TOKEN_MUST_STAY_PRIVATE"
        session = Mock()
        session.post.side_effect = requests.ConnectionError(f"Max retries exceeded with url: /cgi-bin/draft/get?access_token={token}")
        with patch.object(portal, "sleep_before_wechat_retry"), patch.object(portal, "log") as log:
            result = portal.verify_draft_get(session, token, "EXISTING", 30, 1, [article()])
        self.assertNotIn(token, json.dumps(result) + repr(log.call_args_list))
        with tempfile.TemporaryDirectory() as temporary:
            image = Path(temporary) / "image.jpg"
            image.write_bytes(b"image")
            with patch.object(portal, "sleep_before_wechat_retry"), patch.object(portal, "WECHAT_REQUEST_MAX_ATTEMPTS", 1):
                try:
                    portal.upload_wechat_file(session, f"https://api.weixin.qq.com/upload?access_token={token}", image, "uploadimg", 30)
                except portal.WeChatError:
                    rendered = traceback.format_exc()
                else:
                    self.fail("Expected upload failure")
            self.assertNotIn(token, rendered)
            self.assertIn("ConnectionError", rendered)

    def test_content_and_title_mismatches_fail_even_when_article_count_matches(self):
        variants = []
        bad_footer = article()
        bad_footer["content"] = "<p>正文缺少完整署名</p>"
        variants.append(bad_footer)
        wrong_title = article()
        wrong_title["title"] = "完全不同的文章"
        variants.append(wrong_title)
        for returned in variants:
            with self.subTest(returned=returned), patch.object(portal, "get_draft", return_value={"news_item": [returned]}), patch.object(portal, "sleep_before_wechat_retry"):
                result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [article()])
                self.assertFalse(result["ok"])
                self.assertTrue(result["matches_expected_article_count"])


class WeChatUploaderRecoveryTests(unittest.TestCase):
    def run_uploader(self, uploader, root, *, verification, add, lookup, publish, change_image=False, article_count=1):
        source = root / "input"
        report = source / "260914" / "01-Barclays-music"
        report.mkdir(parents=True, exist_ok=True)
        for filename in ("translated.md", "wechat_article.md"):
            (report / filename).write_text(f"# {article()['title']}\n\n报告记录了可核验的数据变化。", encoding="utf-8")
        (report / "translation_status.json").write_text(json.dumps({"title": article()["title"], "source_report_original_name": "Barclays music.pdf"}), encoding="utf-8")
        for index in range(2, article_count + 1):
            additional = source / "260914" / f"{index:02d}-Barclays-music"
            additional.mkdir(exist_ok=True)
            for filename in ("translated.md", "wechat_article.md", "translation_status.json"):
                (additional / filename).write_bytes((report / filename).read_bytes())
        built_article = article()
        built_article["content"] += '<img src="https://example.invalid/old.jpg" />'
        if change_image:
            built_article["content"] = built_article["content"].replace("old.jpg", "new.jpg")
            built_article["thumb_media_id"] = "new-thumb"
        built = {
            "title": built_article["title"], "wechat_title": built_article["title"], "raw_title": built_article["title"],
            "article": built_article, "institution_name": "巴克莱", "source_report_name": "Barclays music",
            "report_dir": str(report), "content_chars": 100, "content_bytes": 200, "visible_text_chars": 100,
            "inline_images": [], "body_image_count": 0, "ai_image_count": 0, "cover_image": "", "title_decision": {},
        }

        def build_one(report_dir, index, *_args):
            result = copy.deepcopy(built)
            if index > 1:
                result["article"]["title"] += f"（第{index}篇）"
                for key in ("title", "wechat_title", "raw_title"):
                    result[key] = result["article"]["title"]
                result["report_dir"] = str(report_dir)
            return result

        source_arg = "--dropbox-output-root" if uploader is xhs else "--translated-root"
        argv = [
            "uploader", source_arg, str(source), "--date-folder", "260914", "--output-root", str(root / "output"),
            "--trailing-image", "", "--site-url", "https://private.example.invalid", "--wechat-appid", "TEST",
            "--wechat-secret", "TEST", "--publish", "--article-delay-seconds", "0", "--draft-delay-seconds", "0",
            "--draft-verify-delay-seconds", "0",
        ]
        with ExitStack() as stack:
            stack.enter_context(patch.object(sys, "argv", argv))
            for name, mocked in {
                "get_stable_access_token": Mock(return_value="TOKEN"), "build_article": Mock(side_effect=build_one),
                "verify_draft_get": verification, "add_draft": add, "find_recent_draft_by_titles": lookup,
                "submit_publish": publish,
            }.items():
                stack.enter_context(patch.object(uploader, name, mocked))
            return uploader.main()

    def test_both_entrypoints_checkpoint_before_verification_and_reuse_on_retry(self):
        for uploader in (portal, xhs):
            with self.subTest(uploader=uploader.__name__), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                summary_path = root / "output/260914/wechat_draft_summary.json"
                add = Mock(return_value="ACCEPTED")
                lookup = Mock(return_value="")
                publish = Mock(return_value="PUBLISHED")

                def reject(*args):
                    checkpoint = json.loads(summary_path.read_text())
                    self.assertEqual("ACCEPTED", checkpoint["drafts"][0]["media_id"])
                    self.assertEqual("pending_verification", checkpoint["drafts"][0]["status"])
                    return {"ok": False, "error": "readback temporarily unavailable"}

                with self.assertRaisesRegex(portal.WeChatError, "receipt saved"):
                    self.run_uploader(uploader, root, verification=Mock(side_effect=reject), add=add, lookup=lookup, publish=publish)
                failed = json.loads(summary_path.read_text())
                self.assertEqual("verification_failed", failed["status"])
                self.assertFalse(failed["drafts"][0]["published"])
                publish.assert_not_called()
                add.assert_called_once()

                lookup.reset_mock()
                good = Mock(return_value={"ok": True})
                self.assertEqual(0, self.run_uploader(uploader, root, verification=good, add=add, lookup=lookup, publish=publish, change_image=True))
                lookup.assert_not_called()
                add.assert_called_once()  # No second draft/add after the failed read.
                publish.assert_called_once()
                verified = json.loads(summary_path.read_text())
                self.assertEqual("verified", verified["status"])
                self.assertEqual("ACCEPTED", verified["drafts"][0]["media_id"])
                self.assertTrue(verified["drafts"][0]["reused_existing"])

                self.assertEqual(0, self.run_uploader(uploader, root, verification=good, add=add, lookup=lookup, publish=publish))
                publish.assert_called_once()  # Preserve accepted publish_id too.

    def test_legacy_artifact_receipt_can_be_restored_at_a_different_path(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            public = [article()]
            portal.write_json(root / "draft_payload_01.json", {"articles": public})
            portal.write_json(root / "wechat_draft_summary.json", {"dry_run": False, "drafts": [{
                "media_id": "HISTORICAL", "payload": "/old/runner/path/draft_payload_01.json", "draft_get": {"ok": False},
            }]})
            found = portal.saved_draft_receipt(root, public)
            self.assertEqual("HISTORICAL", found["media_id"])
            (root / "wechat_draft_summary.json").write_text("truncated{")
            with self.assertRaises(portal.WeChatError):
                portal.saved_draft_receipt(root, public)

    def test_retry_reuses_accepted_split_prefix_before_any_larger_group_add(self):
        for uploader in (portal, xhs):
            with self.subTest(uploader=uploader.__name__), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                first_add = Mock(side_effect=[portal.WeChatError("article size out of limit", errcode=45008), "FIRST_CHILD"])
                lookup = Mock(return_value="")
                publish = Mock(return_value="PUBLISHED")
                with self.assertRaisesRegex(portal.WeChatError, "receipt saved"):
                    self.run_uploader(uploader, root, verification=Mock(return_value={"ok": False}), add=first_add, lookup=lookup, publish=publish, article_count=2)
                self.assertEqual([2, 1], [len(call.args[2]) for call in first_add.call_args_list])

                # The API would now accept the full batch. Replaying it would
                # duplicate FIRST_CHILD, so only the second article may be added.
                retry_add = Mock(return_value="SECOND_CHILD")
                self.assertEqual(0, self.run_uploader(uploader, root, verification=Mock(return_value={"ok": True}), add=retry_add, lookup=lookup, publish=publish, article_count=2))
                retry_add.assert_called_once()
                self.assertEqual(1, len(retry_add.call_args.args[2]))
                self.assertTrue(retry_add.call_args.args[2][0]["title"].endswith("（第2篇）"))
                result = json.loads((root / "output/260914/wechat_draft_summary.json").read_text())
                self.assertEqual(["FIRST_CHILD", "SECOND_CHILD"], [item["media_id"] for item in result["drafts"]])


if __name__ == "__main__":
    unittest.main()
