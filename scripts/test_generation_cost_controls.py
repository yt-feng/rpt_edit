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
    def make_handoff_report(self, root, producer_kind):
        from private_workflow_handoff import create_archive, extract_archive

        report = root / "source" / "report"
        raw = report / "mineru_raw"
        images = raw / "payload" / "images"
        images.mkdir(parents=True)
        original = images / "Goldman Sachs chart.png"
        chart = Image.new("RGB", (800, 500), "white")
        draw = ImageDraw.Draw(chart)
        for x in range(0, 800, 20):
            draw.line((x, 0, 800 - x, 500), fill="blue", width=3)
        chart.save(original)
        source_text = ("# Quarterly report\n\n" + "The report records enterprise delivery evidence across surveyed businesses. " * 2
                       + "\n\nFigure 1: delivery data\n![](images/Goldman Sachs chart.png)\n\nSource: survey.\n")
        (raw / "payload/full.md").write_text(source_text)
        (report / "source_mineru.md").write_text(source_text)
        if producer_kind == "visual":
            pdf_batch.create_visual_assets(raw, root / "unused.pdf", report / "assets", 8, "Quarterly report")
        else:
            pdf_batch.create_chart_source_assets(raw, report / "assets", 8)
        mapping_bytes = (report / "source_image_map.json").read_bytes()
        finalize.sanitize_output_dir(report)
        self.assertEqual((report / "source_image_map.json").read_bytes(), mapping_bytes)
        self.assertEqual((report / "source_mineru.md").read_text(), source_text)
        self.assertFalse(guard.should_process(report / "source_image_map.json"))
        archive = root / "handoff.tar.gz"
        create_archive(report.parent, archive)
        restored = root / "restored"
        extract_archive(archive, restored)
        self.assertFalse((restored / "report/mineru_raw").exists())
        return restored / "report"

    def test_private_handoff_maps_original_chart_refs_to_retained_assets(self):
        for producer_kind in ("visual", "chart-only"):
            with self.subTest(producer_kind=producer_kind), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary)
                report = self.make_handoff_report(root, producer_kind)
                resolved = translated_reports.resolve_image_path(report / "source_mineru.md", "./images/Goldman Sachs chart.png?size=full")
                self.assertEqual(resolved, (report / "assets/source_image_01.png").resolve())
                markdown, figures = translated_reports.prepare_clean_markdown(report, root / "translated", 28, strict_chart_images=True)
                self.assertEqual(len(figures), 1)
                self.assertIn("[[PORTAL_IMAGE_001]]", markdown)
                self.assertTrue(Path(figures[0]["path"]).is_file())
                self.assertIn("score=", figures[0]["chart_filter"])

    @unittest.skipIf(translated_reports.SimpleDocTemplate is None, "reportlab is required for PDF rendering")
    def test_private_handoff_chart_token_renders_pdf_image(self):
        import fitz

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = self.make_handoff_report(root, "chart-only")
            markdown, figures = translated_reports.prepare_clean_markdown(report, root / "translated", 28, strict_chart_images=True)
            output = root / "translated/report.pdf"
            translated_reports.render_pdf(markdown, figures, output, "Quarterly report")
            with fitz.open(output) as document:
                self.assertGreater(sum(len(page.get_images()) for page in document), 0)

    def test_image_mapping_rejects_stale_source_and_escaping_targets(self):
        import json

        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = self.make_handoff_report(root, "chart-only")
            source = report / "source_mineru.md"
            mapping_path = report / "source_image_map.json"
            original = json.loads(mapping_path.read_text())
            (root / "outside.png").write_bytes(b"outside")
            for target in ("../../outside.png", str(root / "outside.png"), "assets/escape.png"):
                if target == "assets/escape.png":
                    (report / target).symlink_to(root / "outside.png")
                altered = dict(original, images={"images/Goldman Sachs chart.png": target})
                mapping_path.write_text(json.dumps(altered))
                self.assertIsNone(translated_reports.resolve_image_path(source, "images/Goldman Sachs chart.png"))
            mapping_path.write_text(json.dumps(original))
            source.write_text(source.read_text() + "Changed source")
            self.assertIsNone(translated_reports.resolve_image_path(source, "images/Goldman Sachs chart.png"))

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

    def test_explicit_podcast_flags_restore_copy_audio_and_video_chain(self):
        with tempfile.TemporaryDirectory() as temporary:
            item = Path(temporary)
            (item / "source_mineru.md").write_text("Public report fixture.")
            (item / "wechat_article.md").write_text("# 中文标题\n公开样本。")
            args = postprocess.build_arg_parser().parse_args([
                "--generate-english-article", "true", "--generate-podcast", "true", "--generate-audio", "true",
            ])
            script = "ZH_A: 公开中文样本。\nZH_B: 第二句。\nEN_A: Public sample.\nEN_B: Another sentence."
            with patch.object(postprocess, "call_deepseek", side_effect=["# English title\nPublic text.", script]) as generate, \
                 patch.object(postprocess, "generate_highlights", return_value={}), \
                 patch.object(postprocess, "render_language_audio", return_value=[]) as audio, \
                 patch.object(postprocess, "render_video") as video:
                status = postprocess.process_item(item, args)
            self.assertEqual(generate.call_count, 2)
            self.assertEqual(audio.call_count, 2)
            self.assertEqual(video.call_count, 2)
            self.assertTrue(status["podcast_generation_enabled"])
            self.assertEqual(status["podcast_en_video"], "podcast_en.mp4")
            self.assertIn("EN_A", (item / "podcast_en_script.txt").read_text())

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
    def test_original_extraction_is_byte_preserved_and_never_sent_to_guard(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            item = output / "report"
            raw = item / "mineru_raw" / "nested"
            raw.mkdir(parents=True)
            sources = {item / "source_mineru.md": b"Goldman Sachs original evidence.\n"}
            for name in ("full.md", "content_list.json", "ocr.txt", "wechat_article.md", "wechat_article_en.md", "xianyu_note.md"):
                sources[raw / name] = b"Goldman Sachs original source must never change.\n"
            for path, content in sources.items():
                path.write_bytes(content)
            (item / "wechat_article.md").write_text("# Generated article\nPublic generated text.")
            argv = ["finalize", "--output-dir", str(output), "--generate-zhihu", "false"]
            with patch.object(sys, "argv", argv), patch.object(
                guard, "free_api_check", return_value={"hit": True, "hits": [{"ci": "fixture"}], "errors": []}
            ) as check, patch.object(guard, "deepseek_rewrite", return_value="# Generated article\nRevised generated text.\n") as rewrite:
                self.assertEqual(finalize.main(), 0)
            self.assertEqual(check.call_count, 1)
            self.assertEqual(rewrite.call_count, 1)
            self.assertIn("Revised generated", (item / "wechat_article.md").read_text())
            for path, content in sources.items():
                self.assertEqual(path.read_bytes(), content, str(path))
            with patch.object(guard, "free_api_check", side_effect=AssertionError("source reached API")):
                self.assertEqual(guard.guard_file(raw / "full.md", guard.build_arg_parser().parse_args([
                    "--output-dir", str(output)
                ]))["skipped"], "original_source_material")

    def test_explicit_finalizer_flags_restore_guards_for_reenabled_outputs(self):
        with tempfile.TemporaryDirectory() as temporary:
            output = Path(temporary)
            filenames = {"wechat_article.md", "note.md", "wechat_article_en.md", "xianyu_note.md",
                         "podcast_script.txt", "podcast_zh_script.txt", "podcast_en_script.txt", "podcast_zh.md"}
            for name in filenames:
                (output / name).write_text(f"Public generated fixture {name}.")
            visited = []

            def accept(path, _args):
                visited.append(path.name)
                return {"path": str(path), "changed": False}

            with patch.object(guard, "guard_file", side_effect=accept):
                finalize.run_guard_if_enabled(output, finalize.build_arg_parser().parse_args([]))
                self.assertEqual(visited, ["wechat_article.md"])
                args = finalize.build_arg_parser().parse_args([
                    "--guard-xhs", "true", "--guard-english-article", "true", "--guard-podcast", "true",
                    "--generate-xianyu", "true",
                ])
                finalize.run_guard_if_enabled(output, args)
            self.assertEqual(set(visited), filenames)

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
