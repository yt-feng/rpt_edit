#!/usr/bin/env python3
"""Regression checks for verifying archived drafts without uploading again."""

import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

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


class RestoredIdentityTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.receipt = {"schema_version": 1, "publish": False, "dry_run": False,
                        "draft_count": 1, "expected_article_count": 2,
                        "verified_draft_count": 1, "verified_article_count": 2,
                        "drafts": [{"media_id": "restored-new-id", "article_count": 2,
                                    "titles": ["原题一", "原题二"], "status": "verified"}]}
        self.save()

    def save(self):
        (self.root / "restore_receipt.json").write_text(json.dumps(self.receipt), encoding="utf-8")

    def readback(self, data):
        with patch.object(verifier, "get_draft", return_value=data) as get, \
             patch.object(verifier, "verify_draft_get", side_effect=AssertionError("No editorial verification or repair")):
            result = verifier.verify_existing(verifier.load_drafts(self.root), object(), "token", 20)
        self.assertEqual(get.call_args.args[2], "restored-new-id")
        return result

    def test_title_only_receipt_does_not_invent_an_upload_payload(self):
        drafts = verifier.load_drafts(self.root)
        self.assertNotIn("articles", drafts[0])
        self.assertEqual(drafts[0]["verification_scope"], "restored_receipt_identity")
        report = self.readback({"news_item": [{"title": "原题一", "author": "用户改过署名"}, {"title": "原题二"}],
                                "create_time": 100, "update_time": 200})
        self.assertTrue(report["ok"])
        self.assertTrue(report["read_only"])
        self.assertEqual(report["verified_article_count"], 2)
        self.assertEqual(report["verification_scope"], "restored_receipt_identity")
        self.assertEqual(report["drafts"][0]["update_time"], 200)

    def test_renamed_and_removed_articles_are_existing_ids_with_edits(self):
        for rows, expected in (([{"title": "新题一"}, {"title": "原题二"}], "titles_changed"),
                               ([{"title": "原题一"}], "article_count_changed")):
            with self.subTest(expected=expected):
                report = self.readback({"news_item": rows})
                self.assertFalse(report["ok"])
                self.assertEqual(report["existing_draft_count"], 1)
                self.assertIs(report["drafts"][0]["id_exists"], True)
                self.assertEqual(report["drafts"][0]["identity_status"], expected)
                self.assertEqual(report["drafts"][0]["titles"], [row["title"] for row in rows])

    def test_missing_and_permission_denied_are_distinct_without_raw_error_messages(self):
        for code, status, exists in ((40007, "invalid_media_id", False), (48001, "unknown", None), (None, "unknown", None)):
            with self.subTest(code=code), patch.object(verifier, "get_draft", side_effect=verifier.WeChatError(
                "access_token=TOPSECRET", errcode=code, errmsg="TOPSECRET")):
                report = verifier.verify_existing(verifier.load_drafts(self.root), object(), "token", 20)
            row = report["drafts"][0]
            self.assertEqual(row["identity_status"], status)
            self.assertIs(row["id_exists"], exists)
            self.assertEqual(row["errcode"], code)
            self.assertNotIn("TOPSECRET", json.dumps(report))

    def test_malformed_response_is_unknown_not_absent(self):
        for data in ({}, {"news_item": "broken"}, {"news_item": [{}]}, []):
            with self.subTest(data=data):
                report = self.readback(data)
                self.assertIsNone(report["drafts"][0]["id_exists"])
                self.assertEqual(report["drafts"][0]["identity_status"], "unknown")

    def test_invalid_schema_flags_ids_and_counts_are_rejected(self):
        import copy
        original = copy.deepcopy(self.receipt)
        cases = [("schema_version", True), ("schema_version", 2), ("publish", True), ("dry_run", True),
                 ("expected_article_count", 3), ("draft_count", 2), ("verified_article_count", 1),
                 ("verified_draft_count", 0), ("drafts", []), ("drafts", [None])]
        for key, value in cases:
            with self.subTest(key=key, value=value):
                self.receipt = copy.deepcopy(original)
                self.receipt[key] = value
                self.save()
                with self.assertRaises(ValueError): verifier.load_drafts(self.root)
        for key, value in (("media_id", " "), ("media_id", 123), ("article_count", True),
                           ("article_count", 3), ("titles", ["原题一", ""]), ("titles", ["原题一", 123])):
            with self.subTest(key=key, value=value):
                self.receipt = copy.deepcopy(original)
                self.receipt["drafts"][0][key] = value
                self.save()
                with self.assertRaises(ValueError): verifier.load_drafts(self.root)
        self.receipt = copy.deepcopy(original)
        self.receipt["drafts"] *= 2
        self.receipt.update(draft_count=2, expected_article_count=4, verified_draft_count=2, verified_article_count=4)
        self.save()
        with self.assertRaises(ValueError): verifier.load_drafts(self.root)

    def test_ambiguous_or_escaping_restoration_receipt_is_rejected(self):
        nested = self.root / "nested"
        nested.mkdir()
        duplicate = nested / "restore_receipt.json"
        duplicate.write_text(json.dumps(self.receipt))
        with self.assertRaises(ValueError): verifier.load_drafts(self.root)
        duplicate.unlink()
        with tempfile.TemporaryDirectory() as other:
            outside = Path(other) / "receipt.json"
            path = self.root / "restore_receipt.json"
            path.rename(outside)
            path.symlink_to(outside)
            with self.assertRaises(ValueError): verifier.load_drafts(self.root)

    def test_original_payload_summary_takes_precedence_and_does_not_fallback_when_broken(self):
        summary = ExistingDraftTests().make_archive(self.root)
        drafts = verifier.load_drafts(self.root)
        self.assertEqual(drafts[0]["media_id"], "existing-draft")
        self.assertIn("articles", drafts[0])
        summary.write_text('{"drafts": []}')
        with self.assertRaises(ValueError): verifier.load_drafts(self.root)

    def test_real_http_adapter_only_posts_draft_get(self):
        import requests
        from urllib.parse import urlsplit
        response = requests.Response()
        response.status_code = 200
        response._content = json.dumps({"news_item": [{"title": "原题一"}, {"title": "原题二"}]}).encode()
        session = Mock()
        session.post.return_value = response
        report = verifier.verify_existing(verifier.load_drafts(self.root), session, "token", 20)
        self.assertTrue(report["ok"])
        session.post.assert_called_once()
        self.assertEqual(urlsplit(session.post.call_args.args[0]).path, "/cgi-bin/draft/get")
        self.assertEqual(json.loads(session.post.call_args.kwargs["data"]), {"media_id": "restored-new-id"})
        self.assertEqual([call[0] for call in session.method_calls], ["post"])

    def test_identity_only_input_is_rejected_by_restore_and_inventory_before_authentication(self):
        import audit_wechat_article_presence as audit
        import restore_missing_wechat_drafts as restore
        import contextlib
        import io
        for module in (restore, audit):
            with self.subTest(module=module.__name__), tempfile.TemporaryDirectory() as destination, \
                 patch.object(module.requests, "Session") as session, \
                 patch.object(module, "get_stable_access_token") as auth, \
                 patch.object(module, "post_wechat_json") as post, \
                 patch.dict(module.os.environ, {"WECHAT_MP_APPID": "APP", "WECHAT_MP_APPSECRET": "SECRET"}), \
                 contextlib.redirect_stdout(io.StringIO()):
                code = module.main(["--artifact-root", str(self.root), "--output", str(Path(destination) / "result.json")])
            self.assertEqual(code, 1)
            for mocked in (session, auth, post):
                mocked.assert_not_called()


if __name__ == "__main__":
    unittest.main()
