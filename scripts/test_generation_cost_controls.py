#!/usr/bin/env python3
"""Cost-control regressions for disabled outputs and repeat-safe finalization."""
from __future__ import annotations

import tempfile
import sys
import unittest
from pathlib import Path
from unittest.mock import patch

import finalize_outputs as finalize
import package_publish_ready_outputs as package
import pdf_to_xhs_batch as pdf_batch
import postprocess_podcast as postprocess
import build_portal_translated_reports as translated_reports
import run_pdf_to_xhs_in_batches as batches
import sensitive_content_guard as guard
from push_xhs_notes_to_wechat_drafts import find_report_dirs
from PIL import Image, ImageDraw

ROOT = Path(__file__).resolve().parents[1]


class DisabledOutputTests(unittest.TestCase):
    def test_source_only_keeps_original_images_for_single_downstream_article(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source_pdf = root / "WorldBank report.pdf"
            source_pdf.write_bytes(b"placeholder")

            def download(_url, raw_dir):
                (raw_dir / "images").mkdir(parents=True)
                chart = Image.new("RGB", (800, 500), "white")
                draw = ImageDraw.Draw(chart)
                for x in range(0, 800, 20):
                    draw.line((x, 0, 800 - x, 500), fill="blue", width=3)
                chart.save(raw_dir / "images/chart.png")
                (raw_dir / "full.md").write_text(
                    "# World Bank report\n\n" + "This report describes new delivery evidence for participating businesses. " * 2
                    + "\n\nFigure 1: delivery data\n![](images/chart.png)\n\nSource: survey.\n"
                )

            args = pdf_batch.build_arg_parser().parse_args(["--chart-source-only", "--keep-mineru-raw"])
            with patch.object(pdf_batch, "download_and_unzip", side_effect=download), patch.object(
                pdf_batch, "safe_generate_text", side_effect=AssertionError("source stage must not call DeepSeek")
            ):
                pdf_batch.process_pdf(source_pdf, {"state": "done", "full_zip_url": "https://example.invalid/source.zip"}, root / "out", args)
            item = root / "out/WorldBank-report"
            markdown, figures = translated_reports.prepare_clean_markdown(item, root / "translated", 28, strict_chart_images=True)
            self.assertTrue((item / "mineru_raw/images/chart.png").is_file())
            self.assertFalse((item / "wechat_article.md").exists())
            self.assertEqual(len(figures), 1)
            self.assertIn("[[PORTAL_IMAGE_001]]", markdown)
            self.assertTrue(Path(figures[0]["path"]).is_file())

    def test_new_report_only_generates_wechat_copy_and_keeps_old_xhs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            pdf = root / "Alpha report.pdf"
            pdf.write_bytes(b"placeholder")
            item = root / "out" / "Alpha-report"
            item.mkdir(parents=True)
            (item / "note.md").write_text("previous XHS copy", encoding="utf-8")

            def download(_url, raw_dir):
                raw_dir.mkdir(parents=True)
                (raw_dir / "source.md").write_text("# Alpha report\nEvidence from the report.", encoding="utf-8")

            args = pdf_batch.build_arg_parser().parse_args(["--no-wechat-title-refine"])
            with patch.object(pdf_batch, "download_and_unzip", side_effect=download), patch.object(
                pdf_batch, "create_visual_assets", return_value=[]
            ), patch.object(pdf_batch, "make_cover"), patch.object(
                pdf_batch, "safe_generate_text", return_value="# Alpha：季度数据变化\n\n企业交付数量有所变化。\n"
            ) as generate:
                result = pdf_batch.process_pdf(pdf, {"state": "done", "full_zip_url": "https://example.invalid/source.zip"}, root / "out", args)
            self.assertEqual(generate.call_count, 1)
            self.assertEqual(generate.call_args.args[2], "WeChat article")
            self.assertFalse(result["xhs_generation_enabled"])
            self.assertTrue((item / "wechat_article.md").is_file())
            self.assertFalse((item / "prompt_for_xhs.md").exists())
            self.assertEqual((item / "note.md").read_text(), "previous XHS copy")

    def test_retry_package_and_wechat_accept_report_without_xhs(self):
        with tempfile.TemporaryDirectory() as tmp:
            date = Path(tmp) / "260920"
            shard = date / "shard_0"
            item = shard / "0001-Alpha"
            item.mkdir(parents=True)
            (item / "source_mineru.md").write_text("# Source\nFacts.")
            (item / "wechat_article.md").write_text("# Article\nFacts.")
            self.assertTrue(batches.is_already_converted(item))
            self.assertFalse(batches.is_already_converted(item, generate_xhs=True))
            self.assertEqual(batches.count_generated_report_dirs(shard), 1)
            files, included, skipped = package.collect_package_files(date, True)
            self.assertEqual([f.source.name for f in files], ["wechat_article.md"])
            self.assertEqual(skipped, [])
            self.assertEqual(len(included), 1)
            self.assertEqual(find_report_dirs(date), [item])

    def test_postprocess_default_is_free_and_preserves_existing_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            item = Path(tmp)
            (item / "wechat_article.md").write_text("# Article\nFacts.")
            (item / "podcast_script.txt").write_text("previous podcast")
            args = postprocess.build_arg_parser().parse_args([])
            with patch.object(postprocess, "call_deepseek", side_effect=AssertionError("paid generation disabled")), patch.object(
                postprocess, "render_language_audio", side_effect=AssertionError("audio disabled")
            ):
                result = postprocess.process_item(item, args)
            self.assertFalse(result["podcast_generation_enabled"])
            self.assertFalse(result["english_article_generation_enabled"])
            self.assertFalse((item / "wechat_article_en.md").exists())
            self.assertEqual((item / "podcast_script.txt").read_text(), "previous podcast")

    def test_scheduled_and_manual_defaults_disable_retired_outputs(self):
        workflow = (ROOT / ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml").read_text()
        self.assertIn("--generate-xianyu false", workflow)
        self.assertIn("--generate-podcast false", workflow)
        self.assertIn("--generate-english-article false", workflow)
        self.assertNotIn("DEEPSEEK_PODCAST_API_KEY", workflow)
        video = (ROOT / ".github/workflows/daily-bilingual-podcast-videos.yml").read_text()
        self.assertNotIn("  schedule:", video)
        self.assertIn("inputs.enable_generation == true", video)
        self.assertFalse(pdf_batch.build_arg_parser().parse_args([]).generate_xhs)
        self.assertEqual(finalize.build_arg_parser().parse_args([]).generate_xianyu, "false")
        for name in ("institution", "consulting"):
            workflow = (ROOT / f".github/workflows/{name}-latest-pdf-to-wechat.yml").read_text()
            extraction = workflow.split("      - name: Extract MinerU source", 1)[1].split("      - name:", 1)[0]
            self.assertIn("--chart-source-only", extraction)
            self.assertIn("--keep-mineru-raw", extraction)
            self.assertNotIn("DEEPSEEK_API_KEY", extraction)
            self.assertIn("DEEPSEEK_USAGE_STAGE: report-article", workflow)


class RepeatSafeFinalizationTests(unittest.TestCase):
    def test_full_finalize_rerun_does_not_repeat_paid_work(self):
        with tempfile.TemporaryDirectory() as tmp:
            output = Path(tmp)
            item = output / "Goldman-Sachs-report"
            item.mkdir()
            (item / "source_mineru.md").write_text("Goldman Sachs evidence")
            (item / "wechat_article.md").write_text("# GS：企业数据\n\n企业数据发生变化。")
            argv = ["finalize_outputs", "--output-dir", str(output)]
            with patch.object(sys, "argv", argv), patch.object(
                finalize, "call_deepseek", return_value="# GS：企业数据\n\n企业交付数据发生变化。"
            ) as generate, patch.object(
                guard, "free_api_check", return_value={"hit": False, "hits": [], "errors": []}
            ) as check:
                self.assertEqual(finalize.main(), 0)
                calls_after_first = check.call_count
                self.assertGreater(calls_after_first, 0)
                self.assertEqual(finalize.main(), 0)
                self.assertEqual(generate.call_count, 1)
                self.assertEqual(check.call_count, calls_after_first)
            self.assertFalse((item / "xianyu_note.md").exists())

    def generate(self, item, args, template):
        return finalize.generate_from_template(item, args, item / "source_mineru.md", template, "zhihu_article.md", "prompt_for_zhihu.md", "Zhihu article", 26000)

    def test_unchanged_output_reuses_cache_but_source_change_regenerates(self):
        with tempfile.TemporaryDirectory() as tmp:
            item = Path(tmp)
            source = item / "source_mineru.md"
            source.write_text("Evidence A")
            template = item / "template.txt"
            template.write_text("Write from {source_text}")
            args = finalize.build_arg_parser().parse_args([])
            with patch.object(finalize, "call_deepseek", return_value="# Facts\nA supported article.") as call:
                self.generate(item, args, template)
                cached = self.generate(item, args, template)
                self.assertEqual(call.call_count, 1)
                self.assertEqual(cached["zhihu_article.md_reused"], "true")
                source.write_text("Evidence B")
                self.generate(item, args, template)
                self.assertEqual(call.call_count, 2)

    def test_failed_generation_is_not_cached(self):
        with tempfile.TemporaryDirectory() as tmp:
            item = Path(tmp)
            (item / "source_mineru.md").write_text("Evidence")
            template = item / "template.txt"
            template.write_text("Write from {source_text}")
            args = finalize.build_arg_parser().parse_args([])
            with patch.object(finalize, "call_deepseek", side_effect=[RuntimeError("temporary error"), "# Facts\nA supported article."]) as call:
                self.generate(item, args, template)
                self.generate(item, args, template)
                self.assertEqual(call.call_count, 2)

    def test_guard_only_rewrites_changed_content_and_skips_retired_outputs(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            article = root / "wechat_article.md"
            article.write_text("# A report\nEvidence.")
            (root / "note.md").write_text("Previous XHS copy")
            args = guard.build_arg_parser().parse_args(["--output-dir", str(root), "--exclude-filenames", "note.md"])
            with patch.object(guard, "free_api_check", return_value={"hit": True, "hits": [{"ci": "term"}], "errors": []}) as check, patch.object(
                guard, "deepseek_rewrite", return_value="# A report\nRevised evidence.\n"
            ) as rewrite:
                guard.run_sensitive_guard(root, args)
                result = guard.run_sensitive_guard(root, args)
                self.assertEqual(check.call_count, 1)
                self.assertEqual(rewrite.call_count, 1)
                self.assertTrue(result[0]["reused"])
                article.write_text("# A report\nUpdated evidence.")
                guard.run_sensitive_guard(root, args)
                self.assertEqual(rewrite.call_count, 2)
            self.assertEqual((root / "note.md").read_text(), "Previous XHS copy")

    def test_guard_errors_are_retried(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "wechat_article.md").write_text("# Report\nEvidence.")
            args = guard.build_arg_parser().parse_args(["--output-dir", str(root)])
            with patch.object(guard, "free_api_check", return_value={"hit": False, "hits": [], "errors": ["temporary"]}) as check:
                guard.run_sensitive_guard(root, args)
                guard.run_sensitive_guard(root, args)
                self.assertEqual(check.call_count, 2)


if __name__ == "__main__":
    unittest.main()
