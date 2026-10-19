#!/usr/bin/env python3
"""Read-only presence diagnosis across edits, regrouping, and incomplete APIs."""

import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import requests

import audit_wechat_article_presence as audit
from push_portal_translated_to_wechat_drafts import WeChatError


def response(data, status=200):
    result = requests.Response()
    result.status_code = status
    result._content = json.dumps(data, ensure_ascii=False).encode("utf-8")
    return result


def group(identifier, titles, published=False, author="KCDeskNotes"):
    return {"article_id" if published else "media_id": identifier, "update_time": 1792381404,
            "content": {"create_time": 1792367749, "news_item": [
                {"title": title, "author": author, "content": "BODY_MUST_NOT_ESCAPE",
                 "url": "https://mp.weixin.qq.com/s?__biz=public&mid=1&access_token=HIDDEN",
                 "publish_time": 1792381400} for title in titles]}}


def page(items, total=None):
    return response({"total_count": len(items) if total is None else total, "item_count": len(items), "item": items})


class PresenceAuditTests(unittest.TestCase):
    def expected(self):
        return [{"media_id": "old-id", "articles": [{"title": "文章一"}, {"title": "文章二"}]}]

    def test_split_reordered_and_edited_articles_are_only_title_candidates(self):
        with patch.object(audit, "post_wechat_json", side_effect=[
            page([group("new-b", ["文章二"]), group("old-id", ["文章一"])]),
            page([group("published-a", ["文章二", "文章一"], published=True)]),
        ]) as post:
            report = audit.audit_presence(self.expected(), object(), "TOKEN")
        self.assertTrue(report["ok"])
        for article in report["articles"]:
            self.assertFalse(article["content_identity_verified"])
            for kind in ("draft", "published"):
                self.assertEqual("title_candidates_found", article[kind]["status"])
                match = article[kind]["candidates"][0]
                self.assertEqual("normalized_title_only", match["match_basis"])
                self.assertEqual("KCDeskNotes", match["author"])
                self.assertEqual(1792381404, match["group_times"]["update_time"])
                self.assertEqual(1792381400, match["article_times"]["publish_time"])
                self.assertIn("__biz=public", match["url"])
        self.assertTrue(report["articles"][0]["draft"]["candidates"][0]["same_archived_media_id"])
        self.assertFalse(report["articles"][1]["draft"]["candidates"][0]["same_archived_media_id"])
        serialized = json.dumps(report)
        for hidden in ("BODY_MUST_NOT_ESCAPE", "HIDDEN", "TOKEN"):
            self.assertNotIn(hidden, serialized)
        self.assertEqual(2, post.call_count)
        for call in post.call_args_list:
            self.assertIn(call.args[1].split("/cgi-bin/")[1].split("?")[0], audit.ENDPOINTS.values())
            self.assertEqual(0, call.args[2]["no_content"])
            self.assertEqual(1, call.kwargs["max_attempts"])

    def test_endpoint_api_error_is_unknown_and_other_endpoint_still_scans(self):
        with patch.object(audit, "post_wechat_json", side_effect=[
            response({"errcode": 48001, "errmsg": "secret=SECRET body=PRIVATE"}),
            page([group("published", ["文章一"], published=True)]),
        ]) as post:
            report = audit.audit_presence(self.expected(), object(), "TOKEN")
        self.assertEqual(2, post.call_count)
        self.assertFalse(report["ok"])
        self.assertEqual("unknown", report["articles"][0]["draft"]["status"])
        self.assertEqual("title_candidates_found", report["articles"][0]["published"]["status"])
        self.assertEqual(48001, report["inventories"]["draft"]["errors"][0]["errcode"])
        self.assertNotIn("SECRET", json.dumps(report))
        self.assertNotIn("PRIVATE", json.dumps(report))

    def test_complete_zero_is_endpoint_nonmatch_not_proof_of_deletion(self):
        with patch.object(audit, "post_wechat_json", side_effect=[page([]), page([])]):
            report = audit.audit_presence(self.expected(), object(), "TOKEN")
        self.assertTrue(report["ok"])
        self.assertEqual("not_found_in_complete_endpoint_inventory", report["articles"][0]["draft"]["status"])
        self.assertIn("do not prove deletion", report["interpretation"])
        self.assertIn("manually mass-sent", report["published_scope"])

    def test_pagination_uses_observed_count_and_stops_at_bound(self):
        with patch.object(audit, "post_wechat_json", side_effect=[
            page([group("one", ["unrelated"])], total=3),
            page([group("two", ["also unrelated"])], total=3),
        ]) as post:
            inventory = audit.scan_inventory(object(), "TOKEN", "draft", 30, max_pages=2, page_size=1)
        self.assertFalse(inventory["complete"])
        self.assertEqual("page_limit", inventory["stop_reason"])
        self.assertEqual([0, 1], [call.args[2]["offset"] for call in post.call_args_list])
        report = audit.build_report(self.expected(), {"draft": inventory})
        self.assertEqual("unknown", report["articles"][0]["draft"]["status"])

    def test_partial_error_preserves_found_candidates_without_claiming_completeness(self):
        with patch.object(audit, "post_wechat_json", side_effect=[
            page([group("one", ["文章一"])], total=2),
            requests.Timeout("https://api.weixin.qq.com/?access_token=SECRET"),
        ]):
            inventory = audit.scan_inventory(object(), "TOKEN", "draft", 30, max_pages=2, page_size=1)
        report = audit.build_report(self.expected(), {"draft": inventory})
        self.assertFalse(report["ok"])
        self.assertEqual("title_candidates_found", report["articles"][0]["draft"]["status"])
        self.assertEqual("unknown", report["articles"][1]["draft"]["status"])
        self.assertNotIn("SECRET", json.dumps(report))

    def test_malformed_page_or_incomplete_article_never_means_absent(self):
        cases = [response({"total_count": "0", "item": []}),
                 response({"total_count": 1, "item_count": 1, "item": []}),
                 page([{"media_id": "one", "content": {}}]), page([], total=2)]
        for data in cases:
            with self.subTest(data=data.content), patch.object(audit, "post_wechat_json", return_value=data):
                inventory = audit.scan_inventory(object(), "TOKEN", "draft", 30)
            self.assertFalse(inventory["complete"])

    def test_repeated_ids_and_changed_totals_cannot_claim_complete(self):
        cases = [([page([group("one", ["文章一"])], 2), page([group("one", ["文章一"])], 2)], "repeated_group_id"),
                 ([page([group("one", ["文章一"])], 3), page([group("two", ["文章二"])], 2)], "total_changed_during_scan")]
        for pages, reason in cases:
            with self.subTest(reason=reason), patch.object(audit, "post_wechat_json", side_effect=pages):
                inventory = audit.scan_inventory(object(), "TOKEN", "draft", 30, max_pages=2, page_size=1)
            self.assertFalse(inventory["complete"])
            self.assertEqual(reason, inventory["stop_reason"])

    def test_same_title_multiple_candidates_remain_ambiguous(self):
        with patch.object(audit, "post_wechat_json", side_effect=[
            page([group("a", ["文章一"]), group("b", ["文章一"])]), page([]),
        ]):
            report = audit.audit_presence(self.expected(), object(), "TOKEN")
        self.assertEqual(2, len(report["articles"][0]["draft"]["candidates"]))
        self.assertFalse(report["articles"][0]["content_identity_verified"])

    def test_only_public_article_url_fields_survive(self):
        url = audit.public_url("http://mp.weixin.qq.com/s?__biz=public&mid=2&tempkey=SECRET&ticket=SECRET&auth_token=SECRET&future_secret=SECRET#SECRET")
        self.assertEqual("https://mp.weixin.qq.com/s?__biz=public&mid=2", url)
        for url in ("https://example.com/s?mid=2", "https://user:SECRET@mp.weixin.qq.com/s?mid=2",
                    "https://mp.weixin.qq.com/cgi-bin/preview?ticket=SECRET", "https://mp.weixin.qq.com:bad/s"):
            self.assertEqual("", audit.public_url(url))

    def test_authentication_failure_always_writes_safe_unknown_report(self):
        def fail_auth(*args):
            print("credential=SECRET raw_body=PRIVATE")
            raise WeChatError("access_token=SECRET raw_body=PRIVATE", errcode=40013)
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp) / "result.json"
            stdout = io.StringIO()
            with patch.object(audit, "load_drafts", return_value=self.expected()), \
                    patch.dict(audit.os.environ, {"WECHAT_MP_APPID": "APPID", "WECHAT_MP_APPSECRET": "SECRET"}), \
                    patch.object(audit, "get_stable_access_token", side_effect=fail_auth), \
                    patch.object(audit, "post_wechat_json") as post, contextlib.redirect_stdout(stdout):
                code = audit.main(["--artifact-root", tmp, "--output", str(output)])
            report = json.loads(output.read_text())
        self.assertEqual(1, code)
        self.assertFalse(report["ok"])
        self.assertEqual("unknown", report["articles"][0]["draft"]["status"])
        self.assertEqual("authentication_error", report["inventories"]["published"]["stop_reason"])
        post.assert_not_called()
        for hidden in ("SECRET", "PRIVATE", "APPID"):
            self.assertNotIn(hidden, stdout.getvalue() + json.dumps(report))


if __name__ == "__main__":
    unittest.main()
