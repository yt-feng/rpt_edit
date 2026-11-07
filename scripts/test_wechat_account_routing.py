"""Exercise shared routing, account-bound submission, and verified retries."""
from collections import Counter
from contextlib import redirect_stdout
import hashlib
import io
import json
import os
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import institution_wechat_delivery_receipt as delivery
import push_portal_translated_to_wechat_drafts as portal
import push_xhs_notes_to_wechat_drafts as xhs
import wechat_account_routing as routing
from wechat_accounts import ACCOUNT_NAMES


class R2Error(Exception):
    def __init__(self, code, status):
        self.response = {"Error": {"Code": code}, "ResponseMetadata": {"HTTPStatusCode": status}}


class RoutingStore:
    def __init__(self):
        self.data = None
        self.version = 0

    def get_object(self, **kwargs):
        if self.data is None:
            raise R2Error("NoSuchKey", 404)
        return {"Body": io.BytesIO(self.data), "ETag": f'"{self.version}"'}

    def put_object(self, *, Body, IfMatch=None, IfNoneMatch=None, **kwargs):
        if self.data is None:
            assert IfNoneMatch == "*" and IfMatch is None
        elif IfMatch != f'"{self.version}"':
            raise R2Error("PreconditionFailed", 412)
        self.data = Body
        self.version += 1


class AccountRoutingTests(unittest.TestCase):
    def setUp(self):
        self.store = RoutingStore()
        self.enterContext(patch.dict(os.environ, {
            "WECHAT_ROUTING_START_DATE": "2026-11-08",
            "WECHAT_ROUTING_SCOPE": "dropbox",
            "WECHAT_MP_APPID": "kc",
            "WECHAT_MP_APPSECRET": "kc-secret",
            "WECHAT_MP_APPID_TT": "tt",
            "WECHAT_MP_APPSECRET_TT": "tt-secret",
            "WECHAT_MP_APPID_PANKOU": "pankou",
            "WECHAT_MP_APPSECRET_PANKOU": "pankou-secret",
        }))
        self.enterContext(patch.object(routing, "build_r2_client", return_value=self.store))
        self.enterContext(patch.object(routing, "r2_bucket", return_value="private"))

    def test_concurrent_reservation_advances_the_shared_position(self):
        first, second = [hashlib.sha256(value).hexdigest() for value in (b"one", b"two")]
        put = self.store.put_object

        def concurrent_put(**kwargs):
            if self.store.data is None:
                put(Body=json.dumps({"version": 1, "assigned": {first: "kc"}}).encode(), IfNoneMatch="*")
            return put(**kwargs)

        with patch.object(self.store, "put_object", side_effect=concurrent_put), patch.object(routing.time, "sleep"):
            self.assertEqual({second: "tt"}, routing.reserve_routes(self.store, "private", [second]))
        self.assertEqual({second: "tt", first: "kc"}, routing.reserve_routes(self.store, "private", [second, first]))
        self.assertEqual(2, self.store.version)

    def test_historical_replay_and_dry_run_do_not_touch_routing_state(self):
        args = SimpleNamespace(wechat_appid="kc", wechat_secret="kc-secret", dry_run=False)
        source = Path("261106")
        report = source / "report"
        self.assertEqual({report: None}, routing.plan_destinations(args, source, [report])[0])
        args.dry_run = True
        source = Path("20261107")
        report = source / "report"
        self.assertEqual({report: "kc"}, routing.plan_destinations(args, source, [report])[0])
        self.assertIsNone(self.store.data)

    def test_recovered_and_translated_source_share_the_original_assignment(self):
        args = SimpleNamespace(wechat_appid="kc", wechat_secret="kc-secret", dry_run=False)
        with tempfile.TemporaryDirectory() as temp:
            roots = [Path(temp) / name / "261108" for name in ("regular", "recovery", "translation")]
            reports = [
                (roots[0] / "source-report", "status.json", {"source_pdf": "/sources/My report.pdf"}),
                (roots[1] / "report_0001_hash", "status.json", {"original_filename": "My report.pdf"}),
                (roots[2] / "08-source-report", "translation_status.json", {"wechat_routing_source_name": "My report.pdf"}),
            ]
            for (report, status_path, status), root in zip(reports, roots):
                report.mkdir(parents=True)
                (report / status_path).write_text(json.dumps(status), encoding="utf-8")
                self.assertEqual({report: "kc"}, routing.plan_destinations(args, root, [report])[0])
        self.assertEqual(1, self.store.version)

    def test_two_uploaders_share_article_count_and_read_back_each_account(self):
        accepted = {}

        def add_draft(_session, token, articles, _timeout):
            # Media and trailing-image URLs must be prepared with the destination token.
            for article in articles:
                self.assertTrue(article["thumb_media_id"].startswith(token + "-"))
                self.assertIn(token + "-trailing.jpg", article["content"])
            media_id = str(len(accepted) + 1)
            accepted[media_id] = (token, [article["title"] for article in articles])
            return media_id

        def verify(_session, token, media_id, _timeout, count, articles, repair_media=True):
            self.assertEqual((token, [article["title"] for article in articles]), accepted[media_id])
            return {
                "ok": True, "article_count": count, "expected_article_count": count,
                "matches_expected_article_count": True, "matches_expected_titles": True,
                "matches_editorial_contract": True, "matches_media_contract": True,
            }

        def fetch_token(_session, appid, _secret, _timeout):
            return appid

        def exercise(module, root, count):
            is_xhs = module is xhs
            source_root, output_root = root / "source", root / "drafts"
            source, output = source_root / "261108", output_root / "261108"
            metadata = xhs.xhs_article_title_metadata if is_xhs else portal.translated_article_title_metadata
            for index in range(count):
                report = source / f"{index:02}-report"
                report.mkdir(parents=True)
                filename = "wechat_article.md" if is_xhs else "translated.md"
                (report / filename).write_text("# 世界银行：全球供应链与企业订单观察\n\n订单增长反映了企业对未来需求的判断。\n", encoding="utf-8")
            if is_xhs:
                blocked = source / "00-blocked"
                blocked.mkdir()
                (blocked / "wechat_article.md").write_text("# 高盛：人民币定价机制出现变化\n\n正文是一段说明。", encoding="utf-8")
            else:
                portal.write_json(source / "translation_summary.json", {
                    "date_folder": source.name, "failures": [], "successful_count": count, "selected_count": count,
                    "reports": [{"output_dir": str(report)} for report in source.iterdir()],
                })

            def build(report, index, _args, _session, token, _output, trailing):
                row = metadata(report)
                row["article"] = {"title": row["wechat_title"], "content": f'<p>稿件 {index}</p><img src="{trailing}">',
                                  "thumb_media_id": f"{token}-{index}"}
                return {**row, "content_chars": 20, "content_bytes": 30, "visible_text_chars": 10,
                        "inline_images": [], "body_image_count": 1, "ai_image_count": 0, "cover_image": "cover.jpg"}

            argv = [
                module.__name__, "--dropbox-output-root" if is_xhs else "--translated-root", str(source_root),
                "--date-folder", source.name, "--output-root", str(output_root),
                "--max-articles", "all", "--articles-per-draft", "2", "--site-url", "https://portal.example.invalid",
                "--image-upload-delay-seconds", "0", "--article-delay-seconds", "0",
                "--draft-delay-seconds", "0", "--draft-verify-delay-seconds", "0",
            ]
            with (
                patch.object(sys, "argv", argv),
                patch.object(module, "get_stable_access_token", side_effect=fetch_token),
                patch.object(module, "resolve_repo_asset_path", return_value=Path("trailing.jpg")),
                patch.object(module, "upload_article_image", side_effect=lambda _s, token, path, _t: f"https://example.invalid/{token}-{path}"),
                patch.object(module, "build_article", side_effect=build),
                patch.object(module, "find_recent_draft_by_titles", return_value=""),
                patch.object(module, "add_draft", side_effect=add_draft) as submit,
                patch.object(module, "verify_draft_get", side_effect=verify),
                patch.object(module, "submit_publish") as publish,
                redirect_stdout(io.StringIO()),
            ):
                self.assertEqual(0, module.main())
                draft_count = submit.call_count
                self.assertEqual(0, module.main())
                self.assertEqual(draft_count, submit.call_count)
                publish.assert_not_called()
            with (
                patch.object(portal, "get_stable_access_token", side_effect=fetch_token),
                patch.object(portal, "verify_draft_get", side_effect=verify),
                patch.dict(os.environ, {"PORTAL_SITE_URL": "https://portal.example.invalid"}),
            ):
                report = delivery.validate_delivery(output, source, "xhs" if is_xhs else "portal-translated",
                                                    count + int(is_xhs))
            self.assertTrue(report["delivery_complete"], report)
            self.assertEqual(int(is_xhs), report["policy_excluded_count"])
            return Counter({account: report["verified_articles_by_account"][name]
                            for account, name in ACCOUNT_NAMES.items()})

        with tempfile.TemporaryDirectory() as temp:
            root = Path(temp)
            xhs_counts = exercise(xhs, root / "dropbox", 7)
            with patch.dict(os.environ, {"WECHAT_ROUTING_SCOPE": "consulting"}):
                portal_counts = exercise(portal, root / "consulting", 8)
        self.assertEqual({account: 5 for account in ACCOUNT_NAMES}, xhs_counts + portal_counts)


if __name__ == "__main__":
    unittest.main()
