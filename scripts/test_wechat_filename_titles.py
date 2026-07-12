#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path

from build_kc_translated_reports import report_title
from push_kc_translated_to_wechat_drafts import sharpen_wechat_title
from sensitive_content_guard import sanitize_wechat_stock_language
from wechat_title_optimizer import (
    build_filename_title_translation_prompt,
    choose_filename_anchored_title,
    filename_title_fallback,
    strip_source_filename_noise,
)


SOURCE_FILENAME = "Barclays-Market Strategy Japan：Corporate caution and inflationary pressure-260403.pdf"
EXPECTED_TITLE = "巴克莱：日本市场策略-公司谨慎和通胀压力"


class WeChatFilenameTitleTests(unittest.TestCase):
    def test_user_example_has_exact_deterministic_fallback(self) -> None:
        self.assertEqual(EXPECTED_TITLE, filename_title_fallback(SOURCE_FILENAME, "巴克莱"))

    def test_archive_numbers_and_date_are_removed(self) -> None:
        source = "0001-27-Barclays-Market Strategy Japan：Corporate caution and inflationary pressure-260403.pdf"
        self.assertEqual(
            "Barclays-Market Strategy Japan：Corporate caution and inflationary pressure",
            strip_source_filename_noise(source),
        )

    def test_prompt_uses_body_only_as_secondary_hook_evidence(self) -> None:
        prompt = build_filename_title_translation_prompt(
            SOURCE_FILENAME,
            "巴克莱",
            "样本显示通胀读数达到4%，但公司态度反而更加谨慎。",
        )
        self.assertIn("原始 PDF 文件名标题是最高权重", prompt)
        self.assertIn("忠实底稿", prompt)
        self.assertIn("数据增强版", prompt)
        self.assertIn("反常识增强版", prompt)
        self.assertIn("通胀读数达到4%", prompt)

    def test_off_topic_clickbait_cannot_replace_filename_topic(self) -> None:
        selected = choose_filename_anchored_title(
            [
                EXPECTED_TITLE,
                "巴克莱：日本市场迎来意外反转",
                "巴克莱：4%数据震动全球市场",
            ],
            SOURCE_FILENAME,
            "巴克莱",
        )
        self.assertEqual(EXPECTED_TITLE, selected)

    def test_hook_can_win_when_it_keeps_the_full_filename_anchor(self) -> None:
        sharpened = "巴克莱：日本市场策略-公司谨慎和通胀压力反而加大"
        selected = choose_filename_anchored_title(
            [EXPECTED_TITLE, sharpened, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
        )
        self.assertEqual(sharpened, selected)

    def test_data_can_win_when_it_is_added_to_the_full_filename_anchor(self) -> None:
        with_data = "巴克莱：日本市场策略-公司谨慎和通胀压力升至4%"
        selected = choose_filename_anchored_title(
            [EXPECTED_TITLE, with_data, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
            evidence_text="样本显示通胀读数升至4%。",
        )
        self.assertEqual(with_data, selected)

    def test_unsupported_data_is_rejected(self) -> None:
        invented = "巴克莱：日本市场策略-公司谨慎和通胀压力升至9%"
        selected = choose_filename_anchored_title(
            [EXPECTED_TITLE, invented, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
            evidence_text="样本显示通胀读数升至4%。",
        )
        self.assertEqual(EXPECTED_TITLE, selected)

    def test_big_name_hook_requires_source_support(self) -> None:
        with_name = "巴克莱：日本市场策略-公司谨慎和通胀压力，鲍威尔表态"
        rejected = choose_filename_anchored_title(
            [EXPECTED_TITLE, with_name, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
            evidence_text="正文没有出现相关人物。",
        )
        accepted = choose_filename_anchored_title(
            [EXPECTED_TITLE, with_name, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
            evidence_text="鲍威尔在正文第一段被明确提及。",
        )
        self.assertEqual(EXPECTED_TITLE, rejected)
        self.assertEqual(with_name, accepted)

    def test_title_keeps_filename_wording_while_body_remains_strict(self) -> None:
        markdown = "# 巴克莱：日本市场策略-公司谨慎和通胀压力\n\n正文仍有压力。"
        cleaned, _changes = sanitize_wechat_stock_language(markdown, strict_h1_wording=False)
        heading, body = cleaned.split("\n\n", 1)
        self.assertIn("通胀压力", heading)
        self.assertIn("不确定性", body)

    def test_upload_title_cleanup_does_not_rewrite_filename_semantics(self) -> None:
        self.assertEqual(EXPECTED_TITLE, sharpen_wechat_title(EXPECTED_TITLE, "巴克莱"))

    def test_report_title_prefers_original_source_pdf_over_generated_heading(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report_dir = Path(tmp)
            (report_dir / "wechat_article.md").write_text("# 正文重新概括的标题\n", encoding="utf-8")
            (report_dir / "status.json").write_text(
                json.dumps({"source_pdf": f"/reports/{SOURCE_FILENAME}"}, ensure_ascii=False),
                encoding="utf-8",
            )
            self.assertEqual(Path(SOURCE_FILENAME).stem, report_title(report_dir))


if __name__ == "__main__":
    unittest.main()
