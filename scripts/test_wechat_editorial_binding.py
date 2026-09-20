#!/usr/bin/env python3
"""Prove source-bound upstream editorial reuse never makes another paid call."""
from __future__ import annotations

import json
from pathlib import Path
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

import build_portal_translated_reports as reports
import finalize_outputs as finalize
import pdf_to_xhs_batch as producer
import postprocess_podcast as postprocess
import sensitive_content_guard as guard
import wechat_editorial_binding as binding

TITLE = "国际清算银行：企业交付数量出现变化"
BODY = f"# {TITLE}\n\n本次样本记录了企业交付数量变化。\n\n## 企业样本提供交付证据\n\n企业产出保持稳定。\n"


class EditorialBindingTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.report = self.root / "BIS-public-report"
        self.report.mkdir()
        (self.report / "source_mineru.md").write_text("# BIS report\nCompanies report stable output.\n")
        (self.report / "wechat_article.md").write_text(BODY)
        self.status = {
            "source_pdf": "BIS-public-report.pdf", "wechat_article": "wechat_article.md",
            "wechat_title": TITLE, "wechat_title_source": "source_filename_weighted_finetune",
            "wechat_editorial_model": "deepseek-flash",
            "wechat_title_decision": {"needs_model_repair": False, "selected_quality_issues": [],
                                      "final_title_after_wording_guard": TITLE},
        }
        self.write_status(self.status)
        self.bind()

    def write_status(self, value):
        (self.report / "status.json").write_text(json.dumps(value, ensure_ascii=False))

    def bind(self):
        self.assertTrue(binding.bind_generated_article(self.report, self.status))
        self.write_status(self.status)

    def process(self):
        args = SimpleNamespace(max_images_per_report=2, model="unused-consumer-model", title_refine=True)
        figures = [{"token": "[[PORTAL_IMAGE_001]]", "path": "approved-chart.png"}]
        with patch.object(reports, "prepare_clean_markdown", return_value=("Clean public source", figures)) as prepare, \
                patch.object(reports, "render_pdf") as render:
            result = reports.process_report(self.report, self.root / "out", 1, args)
        self.assertTrue(prepare.call_args.kwargs["strict_chart_images"])
        return result, render.call_args.args[0]

    def test_valid_source_body_and_title_reuse_has_zero_paid_calls_and_only_strict_figures(self):
        article = BODY + '\n![old](assets/old.png)\n<img src="old-photo.png">\n[[PORTAL_IMAGE_999]]\n'
        (self.report / "wechat_article.md").write_text(article)
        self.bind()
        with patch.object(reports, "call_deepseek", side_effect=AssertionError("paid editorial forbidden")) as paid, \
                patch.object(reports, "wechat_title_from_filename", wraps=reports.wechat_title_from_filename) as title:
            result, output = self.process()
        paid.assert_not_called()
        title.assert_not_called()
        self.assertEqual(result["body_provider"], "upstream-editorial-cache")
        self.assertEqual(result["title_provider"], "upstream-editorial-cache")
        self.assertEqual(result["translation_model"], "deepseek-flash")
        self.assertEqual(result["title"], TITLE)
        self.assertIn("[[PORTAL_IMAGE_001]]", output)
        for unwanted in ("old.png", "old-photo", "PORTAL_IMAGE_999", "!["):
            self.assertNotIn(unwanted, output)

    def test_changed_source_body_or_title_and_legacy_unbound_articles_use_existing_editorial_path(self):
        for mismatch in ("source", "body", "title", "missing", "unrepaired-title"):
            with self.subTest(mismatch=mismatch):
                (self.report / "source_mineru.md").write_text("Stable source")
                (self.report / "wechat_article.md").write_text(BODY)
                self.bind()
                status = json.loads((self.report / "status.json").read_text())
                if mismatch == "source":
                    (self.report / "source_mineru.md").write_text("Changed source")
                elif mismatch == "body":
                    (self.report / "wechat_article.md").write_text(BODY + "Untracked change")
                elif mismatch == "title":
                    status["wechat_title_decision"]["new_untracked_decision"] = True
                elif mismatch == "missing":
                    status.pop(binding.FIELD)
                else:
                    status["wechat_title_decision"]["needs_model_repair"] = True
                self.write_status(status)
                with patch.object(reports, "generate_article_style_markdown", return_value=BODY) as body, \
                        patch.object(reports, "wechat_title_from_filename", return_value=(TITLE, {})) as title:
                    result, _text = self.process()
                body.assert_called_once()
                title.assert_called_once()
                self.assertEqual(result["body_provider"], "deepseek-editorial")

    def test_bound_error_placeholder_and_quality_guard_failure_are_not_reused(self):
        for invalid in ("DeepSeek 生成正文失败，请复制 prompt 文件。", "更多完整报告可扫码加入社群查看。"):
            with self.subTest(invalid=invalid):
                (self.report / "wechat_article.md").write_text(BODY + invalid)
                self.bind()
                self.assertIsNone(reports.reusable_upstream_editorial(self.report, []))

    def test_known_image_footer_and_guard_changes_preserve_verified_binding(self):
        with patch.object(postprocess, "find_original_images", return_value=["assets/chart.png"]), \
                patch.object(postprocess, "call_deepseek", side_effect=AssertionError("paid disabled")):
            postprocess.process_item(self.report, postprocess.build_arg_parser().parse_args([]))
        self.assertIsNotNone(binding.read_bound_article(self.report))
        self.assertEqual(finalize.normalize_wechat_articles(self.root), 1)
        self.assertIsNotNone(binding.read_bound_article(self.report))
        args = guard.build_arg_parser().parse_args(["--output-dir", str(self.root), "--use-free-api", "false"])
        with patch.object(guard, "apply_local_guard", side_effect=lambda text: (text.replace("保持稳定", "有所变化"), ["synthetic_edit"])):
            guard.guard_file(self.report / "wechat_article.md", args)
        after = binding.read_bound_article(self.report)
        self.assertIsNotNone(after)
        self.assertIn("有所变化", after.article)
        with patch.object(reports, "call_deepseek", side_effect=AssertionError("paid editorial forbidden")) as paid:
            result, rendered = self.process()
        paid.assert_not_called()
        self.assertEqual(result["body_provider"], "upstream-editorial-cache")
        self.assertNotIn(finalize.GRAY_DISCLAIMER, rendered)

    def test_sanitize_file_advances_only_a_verified_body_binding(self):
        before = binding.read_bound_article(self.report)
        with patch.object(finalize, "sanitize_text", side_effect=lambda text: text.replace("保持稳定", "有所变化")):
            self.assertTrue(finalize.sanitize_file(self.report / "wechat_article.md"))
        after = binding.read_bound_article(self.report)
        self.assertIsNotNone(after)
        self.assertNotEqual(before.binding["article_sha256"], after.binding["article_sha256"])
        self.assertEqual(before.binding["source_sha256"], after.binding["source_sha256"])

    def test_transformation_never_legitimizes_legacy_or_already_changed_content(self):
        for mode in ("legacy", "source", "body", "title"):
            with self.subTest(mode=mode):
                (self.report / "source_mineru.md").write_text("Stable source")
                (self.report / "wechat_article.md").write_text(BODY)
                self.bind()
                status = json.loads((self.report / "status.json").read_text())
                if mode == "legacy":
                    status.pop(binding.FIELD)
                    self.write_status(status)
                elif mode == "source":
                    (self.report / "source_mineru.md").write_text("Changed source")
                elif mode == "body":
                    (self.report / "wechat_article.md").write_text(BODY + "Unexpected change")
                else:
                    status["wechat_title"] = "Changed title"
                    self.write_status(status)
                finalize.normalize_wechat_articles(self.root)
                self.assertIsNone(binding.read_bound_article(self.report))

    def test_guard_provider_failure_does_not_extend_changed_body_binding(self):
        args = guard.build_arg_parser().parse_args(["--output-dir", str(self.root), "--use-free-api", "true"])
        with patch.object(guard, "apply_local_guard", side_effect=lambda text: (text + "Local change", [])), \
                patch.object(guard, "free_api_check", return_value={"hit": True, "hits": [], "errors": []}), \
                patch.object(guard, "deepseek_rewrite", side_effect=RuntimeError("synthetic failure")):
            guard.guard_file(self.report / "wechat_article.md", args)
        self.assertIsNone(binding.read_bound_article(self.report))

    def test_existing_guard_rewrite_can_advance_verified_body_without_changing_source(self):
        before = binding.read_bound_article(self.report)
        args = guard.build_arg_parser().parse_args(["--output-dir", str(self.root), "--use-free-api", "true"])
        with patch.object(guard, "free_api_check", return_value={"hit": True, "hits": [], "errors": []}), \
                patch.object(guard, "deepseek_rewrite", return_value=BODY.replace("保持稳定", "有所变化")) as rewrite:
            guard.guard_file(self.report / "wechat_article.md", args)
        rewrite.assert_called_once()
        after = binding.read_bound_article(self.report)
        self.assertIsNotNone(after)
        self.assertEqual(after.binding["source_sha256"], before.binding["source_sha256"])
        self.assertNotEqual(after.binding["article_sha256"], before.binding["article_sha256"])

    def test_complete_finalization_sequence_keeps_binding_for_downstream_zero_paid_reuse(self):
        with patch.object(sys, "argv", ["finalize_outputs.py", "--output-dir", str(self.root),
                                       "--generate-zhihu", "false", "--use-free-api", "false"]), \
                patch.object(finalize, "call_deepseek", side_effect=AssertionError("unexpected finalizer call")) as final_paid:
            self.assertEqual(finalize.main(), 0)
        final_paid.assert_not_called()
        self.assertIsNotNone(binding.read_bound_article(self.report))
        with patch.object(reports, "call_deepseek", side_effect=AssertionError("paid editorial forbidden")) as paid:
            result, _text = self.process()
        paid.assert_not_called()
        self.assertEqual(result["body_provider"], "upstream-editorial-cache")

    def test_producer_binds_only_after_successful_new_article_and_title(self):
        source_pdf = self.root / "BIS-new-report.pdf"
        source_pdf.write_bytes(b"synthetic")
        def extract(_url, directory):
            directory.mkdir(parents=True)
            (directory / "source.md").write_text("Public synthetic extraction")
        args = producer.build_arg_parser().parse_args([])
        with patch.object(producer, "download_and_unzip", side_effect=extract), \
                patch.object(producer, "create_visual_assets", return_value=[]), \
                patch.object(producer, "make_cover"), \
                patch.object(producer, "safe_generate_text", return_value=BODY), \
                patch.object(producer, "wechat_title_from_filename", return_value=(TITLE, {"needs_model_repair": False})):
            status = producer.process_pdf(source_pdf, {"state": "done", "full_zip_url": "https://example.invalid/synthetic"}, self.root / "produced", args)
        directory = self.root / "produced/BIS-new-report"
        self.assertIn(binding.FIELD, status)
        self.assertIsNotNone(binding.read_bound_article(directory))


if __name__ == "__main__":
    unittest.main()
