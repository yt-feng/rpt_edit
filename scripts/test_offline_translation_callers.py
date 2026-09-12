"""Pure translation dispatch must never reach the paid generation provider."""

from __future__ import annotations

import tempfile
import unittest
from argparse import Namespace
from pathlib import Path
from types import ModuleType
from unittest.mock import Mock, patch

import build_portal_translated_reports as reports
import generate_test_podcast_video_eleven_batch as subtitles
import generate_test_podcast_video_eleven_batch_v2 as subtitles_v2
import translate_portal_titles as titles


class OfflineTranslationCallerTests(unittest.TestCase):
    def setUp(self):
        self.engine = Mock()
        self.engine.model_id = "test-pinned-model:receipt"
        self.engine.translate.return_value = "半导体产量增长"
        self.engine.translate_markdown.return_value = "# 半导体产量增长\n\n正文内容。\n\n[[PORTAL_IMAGE_001]]\n"
        module = ModuleType("offline_translation")
        module.OfflineTranslator = Mock(return_value=self.engine)
        module.MODEL_ID = "test-pinned-model"
        module.PROVIDER = "argos-offline"
        self.factory = module.OfflineTranslator
        self.addCleanup(patch.stopall)
        patch.dict("sys.modules", {"offline_translation": module}).start()
        self.paid = patch.object(reports, "call_deepseek", side_effect=AssertionError("paid translation forbidden")).start()
        self.paid_subtitles = patch.object(subtitles.gen, "deepseek", side_effect=AssertionError("paid subtitles forbidden")).start()

    def test_title_translation_runs_without_key_and_reuses_model(self):
        args = Namespace(model="deepseek-v4-flash", deepseek_base_url="https://unused.invalid")
        with patch.dict("os.environ", {}, clear=True):
            self.assertEqual(titles.translate_title("Semiconductor output grows", args), "半导体产量增长")
            titles.translate_title("Another title", args)
        self.assertEqual(self.factory.call_count, 1)
        self.engine.translate.assert_called_with("Another title", target="zh")

    def test_report_markdown_and_compatibility_chunk_use_local_structure_aware_adapter(self):
        args = Namespace(deepseek_retries=3, chunk_chars=7200)
        source = "# Output\n\n- More output\n\n[[PORTAL_IMAGE_001]]\n"
        self.assertIn("[[PORTAL_IMAGE_001]]", reports.translate_markdown(source, args))
        reports.translate_chunk(source, args, 1, 1)
        self.engine.translate_markdown.assert_called_with(source, target="zh", source=None)
        self.assertEqual(self.factory.call_count, 1)
        self.paid.assert_not_called()

    def test_local_failure_never_invokes_api_retry(self):
        self.engine.translate_markdown.side_effect = RuntimeError("Required model is missing")
        with self.assertRaisesRegex(RuntimeError, "model is missing"):
            reports.translate_markdown("Report body", Namespace(deepseek_retries=3, chunk_chars=7200))
        self.assertEqual(self.engine.translate_markdown.call_count, 1)
        self.paid.assert_not_called()

    def test_full_translation_filename_uses_existing_deterministic_selection(self):
        with patch.object(reports, "decide_filename_anchored_title", return_value=("最终标题", {})) as selector:
            title, decision = reports.wechat_title_from_filename(
                "Semiconductor output grows", "正文", "", Namespace(title_refine=True), editorial=False)
        self.assertEqual(title, "最终标题")
        self.assertEqual(decision["translation_provider"], "argos-offline")
        selector.assert_called_once_with(["半导体产量增长"], "Semiconductor output grows", "", evidence_text="正文")
        self.paid.assert_not_called()

    def test_process_report_marks_full_body_and_title_as_offline(self):
        with tempfile.TemporaryDirectory() as tmp:
            source = Path(tmp) / "report"
            source.mkdir()
            (source / "source_mineru.md").write_text("# Output\n\nMore output")
            args = Namespace(max_images_per_report=1, title_refine=True)
            with patch.object(reports, "report_title", return_value="Semiconductor output grows"), \
                    patch.object(reports, "is_public_or_consulting_report", return_value=False), \
                    patch.object(reports, "prepare_clean_markdown", return_value=("# Output\n\nMore output", [])), \
                    patch.object(reports, "render_pdf"):
                result = reports.process_report(source, Path(tmp) / "out", 1, args)
        self.assertEqual(result["body_provider"], "argos-offline")
        self.assertEqual(result["title_provider"], "argos-offline")
        self.assertFalse(result["article_style"])
        self.paid.assert_not_called()

    def test_article_style_generation_remains_editorial(self):
        self.paid.side_effect = None
        self.paid.return_value = "# 半导体产量增长\n\n该报告分析生产数据。"
        reports.generate_article_style_markdown("Source", "Title", "", [], Namespace())
        self.paid.assert_called_once()
        self.engine.translate_markdown.assert_not_called()

    def test_subtitle_indices_and_v2_wrapper_keep_offline_translation(self):
        timeline = [{"text": "Output rises."}, {"text": "Output rises."}]
        args = Namespace()
        result = subtitles.translate_english_lines_to_zh(timeline, args)
        self.assertEqual(set(result), {0, 1})
        self.assertTrue(all(result.values()))
        with patch.object(subtitles, "translate_english_lines_to_zh_original", subtitles.translate_english_lines_to_zh, create=True):
            wrapped = subtitles_v2.translate_english_lines_to_zh(timeline, args)
        self.assertEqual(set(wrapped), {0, 1})
        self.paid_subtitles.assert_not_called()

    def test_subtitle_failure_stops_instead_of_emitting_empty_captions(self):
        self.engine.translate.side_effect = RuntimeError("Required model is missing")
        with self.assertRaisesRegex(RuntimeError, "model is missing"):
            subtitles.translate_english_lines_to_zh([{"text": "Output rises."}], Namespace())
        self.paid_subtitles.assert_not_called()

    def test_english_video_title_uses_local_translation(self):
        self.engine.translate.return_value = "Semiconductor output grows"
        result = subtitles.gen.translate_title_to_english("半导体产量增长", "Context", Namespace())
        self.assertIn("Semiconductor", result)
        self.engine.translate.assert_called_once_with("半导体产量增长", target="en")
        self.paid_subtitles.assert_not_called()

    def test_english_title_failure_never_uses_generic_or_paid_fallback(self):
        self.engine.translate.side_effect = RuntimeError("Required model is missing")
        with self.assertRaisesRegex(RuntimeError, "model is missing"):
            subtitles.gen.translate_title_to_english("半导体产量增长", "Context", Namespace())
        self.paid_subtitles.assert_not_called()


if __name__ == "__main__":
    unittest.main()
