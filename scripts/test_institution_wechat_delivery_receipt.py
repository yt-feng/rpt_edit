import json
from pathlib import Path
import shlex
import shutil
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch

import institution_wechat_delivery_receipt as receipts


class OperationsAlertSparseCheckoutTests(unittest.TestCase):
    def test_notification_checkout_runs_its_actual_tests_with_only_stdlib(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / ".github/workflows/portal-ops-alert.yml").read_text(encoding="utf-8")

        def literal_lines(text, marker):
            lines = text.splitlines()
            index = next(index for index, line in enumerate(lines) if line.strip() == marker)
            indentation = len(lines[index]) - len(lines[index].lstrip())
            block = []
            for line in lines[index + 1:]:
                if not line.strip():
                    break
                if len(line) - len(line.lstrip()) <= indentation:
                    break
                block.append(line.strip())
            return block

        files = literal_lines(workflow, "sparse-checkout: |")
        self.assertEqual(set(files), {
            "scripts/render_private_config.py", "scripts/check_portal_ops_alert_window.py",
            "scripts/send_portal_ops_alert.py", "scripts/test_check_portal_ops_alert_window.py",
            "scripts/test_send_portal_ops_alert.py",
        })
        test_step = workflow.split("- name: Test public operations alert client", 1)[1]
        commands = [shlex.split(line) for line in literal_lines(test_step, "run: |")]
        # This test is deliberately outside the notification checkout. Only its
        # two actual leaf test scripts run there, so this cannot recurse.
        self.assertEqual(commands, [
            ["python", "-B", "scripts/test_check_portal_ops_alert_window.py"],
            ["python", "-B", "scripts/test_send_portal_ops_alert.py"],
        ])
        with tempfile.TemporaryDirectory() as temporary:
            checkout = Path(temporary)
            for name in files:
                destination = checkout / name
                destination.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(root / name, destination)
            self.assertEqual(sorted(str(path.relative_to(checkout)) for path in checkout.rglob("*") if path.is_file()),
                             sorted(files))
            for command in commands:
                with self.subTest(script=command[-1]):
                    result = subprocess.run(
                        [sys.executable, "-E", "-s", "-S", *command[1:]],
                        cwd=checkout, text=True, capture_output=True, timeout=30, check=False,
                    )
                    self.assertEqual(result.returncode, 0, result.stdout + result.stderr)


class InstitutionDeliveryReceiptTests(unittest.TestCase):
    def setUp(self):
        from push_portal_translated_to_wechat_drafts import draft_group_key

        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.output = Path(self.temporary.name) / "20261017"
        self.output.mkdir()
        self.payload = {"articles": [{"title": "研究摘要", "author": "研究编辑", "content": "<p>经济增长保持稳定。</p>"}]}
        self.summary = {
            "date_folder": self.output.name, "dry_run": False, "status": "verified",
            "selected_count": 1, "draft_count": 1, "articles": [{"title": "研究摘要"}],
            "drafts": [{
                "media_id": "sample-media-id", "payload": "draft_payload_001.json", "article_count": 1,
                "group_key": draft_group_key(self.payload["articles"]), "status": "verified",
                "draft_get": {"ok": True, "article_count": 1, "expected_article_count": 1,
                              "matches_editorial_contract": True, "matches_expected_article_count": True,
                              "matches_expected_titles": True, "matches_media_contract": True},
            }],
        }
        self.save()

    def save(self):
        (self.output / "wechat_draft_summary.json").write_text(json.dumps(self.summary), encoding="utf-8")
        (self.output / "draft_payload_001.json").write_text(json.dumps(self.payload), encoding="utf-8")

    def assert_unconfirmed(self):
        self.assertEqual(receipts.institution_wechat_delivery_outputs(self.output),
                         {"wechat_verified": "false", "verified_article_count": "0", "verified_draft_count": "0"})

    def test_saved_complete_readback_produces_only_verified_counts(self):
        self.assertEqual(receipts.institution_wechat_delivery_outputs(self.output),
                         {"wechat_verified": "true", "verified_article_count": "1", "verified_draft_count": "1"})

    def test_unfinished_dry_run_and_wrong_date_receipts_are_not_delivery(self):
        for key, value in (("status", "in_progress"), ("dry_run", True), ("date_folder", "20261016"),
                           ("selected_count", 2), ("draft_count", 2)):
            with self.subTest(key=key):
                previous = self.summary[key]
                self.summary[key] = value
                self.save()
                self.assert_unconfirmed()
                self.summary[key] = previous

    def test_incomplete_readback_is_not_delivery(self):
        readback = self.summary["drafts"][0]["draft_get"]
        for key, value in list(readback.items()):
            with self.subTest(key=key):
                readback[key] = False if isinstance(value, bool) else 2
                self.save()
                self.assert_unconfirmed()
                readback[key] = value

    def test_receipt_cannot_be_reused_for_changed_payload(self):
        self.payload["articles"][0]["content"] = "<p>这是另一份报告。</p>"
        self.save()
        self.assert_unconfirmed()

    def test_missing_or_invalid_summary_and_payload_are_unconfirmed(self):
        for name in ("wechat_draft_summary.json", "draft_payload_001.json"):
            with self.subTest(name=name):
                path = self.output / name
                path.unlink()
                self.assert_unconfirmed()
                path.write_text("[]", encoding="utf-8")
                self.assert_unconfirmed()
                self.save()

    def test_duplicate_receipt_does_not_inflate_counts(self):
        self.summary["drafts"] *= 2
        self.summary.update(draft_count=2, selected_count=2, articles=self.summary["articles"] * 2)
        self.save()
        self.assert_unconfirmed()

    def test_payload_path_cannot_escape_receipt_directory(self):
        path = self.output / "draft_payload_001.json"
        outside = self.output.parent / "draft_payload_external.json"
        path.rename(outside)
        path.symlink_to(outside)
        self.assert_unconfirmed()


class FinalDeliveryGateTests(unittest.TestCase):
    def setUp(self):
        from push_portal_translated_to_wechat_drafts import translated_article_title_metadata, draft_group_key
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.source = self.root / "source" / "20261017"
        self.source_report = self.source / "0001-BofA-economic-growth"
        self.source_report.mkdir(parents=True)
        (self.source_report / "translated.md").write_text("# 美银：经济增长与资本开支观察\n\n经济增长保持稳定，企业资本开支继续增长。", encoding="utf-8")
        (self.source_report / "translation_status.json").write_text(json.dumps({"title": "美银：经济增长与资本开支观察", "source_title": "BofA economic growth"}), encoding="utf-8")
        self.metadata = translated_article_title_metadata(self.source_report)
        self.output = self.root / "drafts" / "20261017"
        self.output.mkdir(parents=True)
        self.payload = {"articles": [{"title": self.metadata["wechat_title"], "author": "研究编辑", "content": "<p>经济增长保持稳定。</p>"}]}
        self.live = {"ok": True, "article_count": 1, "expected_article_count": 1,
                     "matches_editorial_contract": True, "matches_expected_article_count": True,
                     "matches_expected_titles": True, "matches_media_contract": True,
                     "media_repair_attempted": False}
        self.translation = {"date_folder": self.source.name, "input_report_count": 1,
                            "include_institutions": [], "exclude_institutions": [],
                            "institution_excluded_count": 0, "institution_exclusions": [],
                            "selected_count": 1, "successful_count": 1, "failures": [],
                            "reports": [{"output_dir": str(self.source_report), "source_report_dir": "extracted/BofA-economic-growth"}]}
        self.summary = {"date_folder": self.output.name, "dry_run": False, "publish": False, "status": "verified",
                        "input_selected_count": 1, "selected_count": 1, "skipped_title_policy_count": 0,
                        "skipped_title_policy": [], "articles": [dict(self.metadata)], "draft_count": 1,
                        "drafts": [{"media_id": "sample-media-id", "payload": "draft_payload_001.json", "article_count": 1,
                                    "group_key": draft_group_key(self.payload["articles"]), "status": "verified", "draft_get": dict(self.live)}]}
        self.readback = Mock(return_value=[dict(self.live)])
        self.save()

    def save(self):
        for path, value in ((self.source / "translation_summary.json", self.translation),
                            (self.output / "wechat_draft_summary.json", self.summary),
                            (self.output / "draft_payload_001.json", self.payload)):
            path.write_text(json.dumps(value), encoding="utf-8")

    def run_gate(self, **kwargs):
        arguments = dict(output_dir=self.output, source_dir=self.source, source_kind="portal-translated",
                         expected_count=1, readback=self.readback)
        arguments.update(kwargs)
        return receipts.validate_delivery(**arguments)

    def test_saved_success_requires_fresh_complete_readback(self):
        report = self.run_gate()
        self.assertTrue(report["ok"])
        self.assertTrue(report["delivery_complete"])
        self.assertTrue(report["wechat_verified"])
        self.assertEqual(report["verified_article_count"], 1)
        self.readback.assert_called_once()
        self.readback.return_value = [{**self.live, "ok": False, "error": "access_token=TOPSECRET"}]
        report = self.run_gate()
        self.assertFalse(report["ok"])
        self.assertFalse(report["wechat_verified"])
        self.assertNotIn("TOPSECRET", json.dumps(report))

    def test_partial_generation_and_smaller_source_cannot_lower_expected_count(self):
        self.assertFalse(self.run_gate(expected_count=2)["ok"])
        self.translation["failures"] = [{"error": "failed"}]
        self.save()
        self.assertEqual(self.run_gate()["error_code"], "translation_generation_failure")
        self.translation["failures"] = []
        self.summary["skipped_generation_failure_count"] = 1
        self.summary["skipped_generation_failures"] = [{"reason": "failed"}]
        self.save()
        self.assertEqual(self.run_gate()["error_code"], "article_generation_failure")
        self.readback.assert_not_called()

    def test_same_count_old_receipt_different_source_is_rejected(self):
        self.summary["articles"][0]["report_dir"] = "another-source/report"
        self.save()
        self.assertEqual(self.run_gate()["error_code"], "receipt_source_mismatch")
        self.readback.assert_not_called()

    def test_payload_titles_are_bound_to_current_source(self):
        from push_portal_translated_to_wechat_drafts import draft_group_key
        self.payload["articles"][0]["title"] = "另一篇研究报告"
        self.summary["drafts"][0]["group_key"] = draft_group_key(self.payload["articles"])
        self.save()
        self.assertEqual(self.run_gate()["error_code"], "payload_source_title_mismatch")

    def test_portal_source_binding_uses_uploader_sanitized_final_title(self):
        from push_portal_translated_to_wechat_drafts import translated_article_title_metadata, draft_group_key
        from sensitive_content_guard import sanitize_wechat_stock_language
        markdown = "# 美银：推荐AI股票与半导体资本开支\n\n全球企业正在扩大资本开支。"
        (self.source_report / "translated.md").write_text(markdown, encoding="utf-8")
        cleaned, changes = sanitize_wechat_stock_language(markdown, strict_h1_wording=False)
        self.assertTrue(changes)
        metadata = translated_article_title_metadata(self.source_report, cleaned)
        self.summary["articles"] = [metadata]
        self.payload["articles"][0]["title"] = metadata["wechat_title"]
        self.summary["drafts"][0]["group_key"] = draft_group_key(self.payload["articles"])
        self.save()
        self.assertTrue(self.run_gate()["ok"])

    def test_configured_translation_limit_applies_once(self):
        self.translation["input_report_count"] = 4
        self.save()
        self.assertTrue(self.run_gate(expected_count=4, max_articles="1")["ok"])
        self.assertFalse(self.run_gate(expected_count=4, max_articles="all")["ok"])

    def test_merged_translation_summary_without_filter_metadata_respects_independent_limit(self):
        for key in ("input_report_count", "include_institutions", "exclude_institutions",
                    "institution_excluded_count", "institution_exclusions"):
            self.translation.pop(key)
        self.translation.update(plan_sha256="test-merged-plan", max_reports=1, shard_count=1)
        self.save()
        self.assertTrue(self.run_gate(expected_count=4, max_articles="1")["ok"])
        self.assertFalse(self.run_gate(expected_count=4, max_articles="all")["ok"])

    def test_explicit_institution_exclusion_has_evidence_and_is_not_generation_loss(self):
        self.translation.update(input_report_count=2, exclude_institutions=["兰德公司"],
                                institution_excluded_count=1,
                                institution_exclusions=[{"source_report_dir": "extracted/RAND-economic-report",
                                                         "institution_name": "兰德公司", "reason": "excluded_institution"}])
        self.save()
        report = self.run_gate(expected_count=2, exclude_institutions="rand")
        self.assertTrue(report["ok"], report)
        self.assertEqual(report["institution_excluded_count"], 1)
        self.translation["institution_exclusions"][0]["source_report_dir"] = "extracted/BofA-economic-report"
        self.save()
        self.assertFalse(self.run_gate(expected_count=2, exclude_institutions="rand")["ok"])

    def test_duplicate_exclusions_cannot_hide_missing_sources(self):
        record = {"source_report_dir": "extracted/RAND-report", "institution_name": "兰德公司", "reason": "excluded_institution"}
        self.translation.update(input_report_count=3, exclude_institutions=["兰德公司"],
                                institution_excluded_count=2, institution_exclusions=[record, dict(record)])
        self.save()
        self.assertFalse(self.run_gate(expected_count=3, exclude_institutions="rand")["ok"])

    def test_policy_exclusion_must_match_policy_recomputed_from_actual_source(self):
        from push_portal_translated_to_wechat_drafts import translated_article_title_metadata, hard_blocked_portal_title_record
        (self.source_report / "translation_status.json").write_text(json.dumps({"source_title": "北京经济观察"}), encoding="utf-8")
        (self.source_report / "translated.md").write_text("# 美银：北京经济观察\n\n经济分析。", encoding="utf-8")
        metadata = translated_article_title_metadata(self.source_report)
        blocked = hard_blocked_portal_title_record(metadata)
        self.assertIsNotNone(blocked)
        self.summary.update(selected_count=0, articles=[], drafts=[], draft_count=0,
                            skipped_title_policy_count=1, skipped_title_policy=[blocked])
        self.save()
        report = self.run_gate()
        self.assertTrue(report["ok"], report)
        self.assertEqual(report["status"], "policy_excluded")
        self.assertFalse(report["wechat_verified"])
        self.readback.assert_not_called()
        self.summary["skipped_title_policy"][0]["skip_reason"] = "generation_failure"
        self.save()
        self.assertFalse(self.run_gate()["ok"])

    def test_zero_new_articles_is_complete_without_any_api_call(self):
        absent = self.root / "empty" / "20261017"
        report = self.run_gate(source_dir=absent, output_dir=absent, expected_count=0)
        self.assertTrue(report["ok"])
        self.assertTrue(report["delivery_complete"])
        self.assertFalse(report["wechat_verified"])
        self.assertEqual(report["status"], "no_new_articles")
        self.readback.assert_not_called()
        self.assertFalse(self.run_gate(source_dir=absent, output_dir=absent, expected_count=1)["ok"])

    def test_dry_run_and_publish_do_not_claim_draft_delivery(self):
        self.summary.update(dry_run=True, status="dry_run")
        self.save()
        report = self.run_gate(dry_run=True)
        self.assertTrue(report["ok"])
        self.assertFalse(report["delivery_complete"])
        self.assertFalse(report["wechat_verified"])
        self.summary.update(dry_run=False, status="verified", publish=True)
        self.save()
        self.assertFalse(self.run_gate()["ok"])
        self.readback.assert_not_called()

    def test_error_messages_and_helper_logs_never_escape(self):
        import contextlib
        import io
        def fail_with_remote_data(*_args):
            print("https://api.weixin.qq.com/?access_token=TOPSECRET")
            raise RuntimeError("secret=TOPSECRET")
        output = io.StringIO()
        with contextlib.redirect_stdout(output), contextlib.redirect_stderr(output):
            report = self.run_gate(readback=fail_with_remote_data)
        self.assertFalse(report["ok"])
        self.assertNotIn("TOPSECRET", json.dumps(report) + output.getvalue())

    def test_live_reader_explicitly_disables_repairs(self):
        import os
        with patch.dict(os.environ, {"WECHAT_MP_APPID": "test-app", "WECHAT_MP_APPSECRET": "test-secret"}), \
             patch("requests.Session"), \
             patch("push_portal_translated_to_wechat_drafts.get_stable_access_token", return_value="token"), \
             patch("push_portal_translated_to_wechat_drafts.verify_draft_get", return_value=self.live) as verify:
            receipts.live_draft_readback([{"media_id": "media", "articles": self.payload["articles"]}], 10)
        self.assertIs(verify.call_args.kwargs["repair_media"], False)

    def test_xhs_source_count_and_generation_failure_are_independent_of_receipt(self):
        from push_xhs_notes_to_wechat_drafts import xhs_article_title_metadata
        (self.source_report / "wechat_article.md").write_text("# 美银：经济增长与资本开支观察\n\n经济增长保持稳定。", encoding="utf-8")
        (self.source_report / "status.json").write_text("{}", encoding="utf-8")
        metadata = xhs_article_title_metadata(self.source_report)
        self.summary["articles"] = [metadata]
        self.payload["articles"][0]["title"] = metadata["wechat_title"]
        from push_portal_translated_to_wechat_drafts import draft_group_key
        self.summary["drafts"][0]["group_key"] = draft_group_key(self.payload["articles"])
        self.save()
        self.assertTrue(self.run_gate(source_kind="xhs")["ok"])
        self.assertFalse(self.run_gate(source_kind="xhs", expected_count=2)["ok"])
        with patch("push_xhs_notes_to_wechat_drafts.xhs_article_title_metadata", return_value={**metadata, "generation_failure_reason": "missing_article_body"}):
            self.assertEqual(self.run_gate(source_kind="xhs")["error_code"], "article_generation_failure")

    def test_cli_emits_auditable_output_and_nonzero_on_missing_expected_source(self):
        import contextlib
        import io
        import os
        missing = self.root / "missing" / "20261017"
        destination = self.root / "final_delivery.json"
        github_output = self.root / "github-output"
        arguments = ["--output-dir", str(missing), "--source-dir", str(missing), "--source-kind", "xhs",
                     "--expected-count", "0", "--output", str(destination)]
        with patch.dict(os.environ, {"GITHUB_OUTPUT": str(github_output)}), contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(receipts.main(arguments), 0)
            self.assertEqual(json.loads(destination.read_text())["status"], "no_new_articles")
            outputs = github_output.read_text()
            self.assertIn("delivery_complete=true\n", outputs)
            self.assertIn("wechat_verified=false\n", outputs)
            arguments[arguments.index("--expected-count") + 1] = "1"
            self.assertEqual(receipts.main(arguments), 1)
        self.assertFalse(json.loads(destination.read_text())["ok"])

    def test_translation_selection_records_actual_configured_exclusions_before_limit(self):
        import build_portal_translated_reports as builder
        import contextlib
        import io
        date = self.root / "extracted" / "20261017"
        directories = [date / "BofA-economic-growth", date / "RAND-report"]
        for path in directories:
            path.mkdir(parents=True)
        destination = self.root / "translated"
        argv = ["build_portal_translated_reports.py", "--dropbox-output-root", str(date.parent),
                "--date-folder", date.name, "--output-root", str(destination),
                "--exclude-institutions", "rand", "--max-reports", "1"]
        with patch.object(sys, "argv", argv), patch.object(builder, "find_report_dirs", return_value=directories), \
             patch.object(builder, "process_report", return_value={"source_report_dir": str(directories[0])}) as process, \
             contextlib.redirect_stdout(io.StringIO()):
            self.assertEqual(builder.main(), 0)
        summary = json.loads((destination / date.name / "translation_summary.json").read_text())
        self.assertEqual(summary["input_report_count"], 2)
        self.assertEqual(summary["institution_excluded_count"], 1)
        self.assertEqual(summary["institution_exclusions"], [{"source_report_dir": str(directories[1]),
                                                           "institution_name": "兰德公司", "reason": "excluded_institution"}])
        self.assertEqual(summary["selected_count"], 1)
        process.assert_called_once()


if __name__ == "__main__":
    unittest.main()
