#!/usr/bin/env python3
from __future__ import annotations

import unittest
from argparse import Namespace

from build_kc_translated_reports import title_is_sensitive
from sensitive_content_guard import blocked_wechat_title_reason
from push_kc_translated_to_wechat_drafts import (
    all_reports_skipped_by_translation_title_guard,
    wechat_title_policy_skip_reason,
)


class SensitiveTitleGuardTests(unittest.TestCase):
    def test_blocks_reported_chinese_military_title(self) -> None:
        title = "波士顿咨询：军用飞机战备问题-AI可协助修复"
        self.assertEqual("military_or_defense", blocked_wechat_title_reason(title))

    def test_blocks_english_source_filename_before_translation(self) -> None:
        title = "Defense Aviation Has a Readiness Problem. AI Can Help Fix It"
        self.assertEqual("military_or_defense", blocked_wechat_title_reason(title))

    def test_blocks_politically_sensitive_title(self) -> None:
        title = "全球选举与地缘政治变化观察"
        self.assertEqual("politically_sensitive", blocked_wechat_title_reason(title))

    def test_keeps_normal_consulting_title(self) -> None:
        title = "波士顿咨询：生成式AI信任缺口如何影响企业采用"
        self.assertIsNone(blocked_wechat_title_reason(title))

    def test_keeps_trade_policy_title_without_sensitive_topic(self) -> None:
        title = "高盛：关税政策变化如何影响供应链"
        self.assertIsNone(blocked_wechat_title_reason(title))

    def test_final_wechat_upload_gate_blocks_military_title(self) -> None:
        reason = wechat_title_policy_skip_reason("波士顿咨询：军用飞机战备问题-AI可协助修复")
        self.assertEqual("public_account_sensitive_title=military_or_defense", reason)

    def test_translation_gate_blocks_without_calling_deepseek(self) -> None:
        self.assertTrue(
            title_is_sensitive(
                "Defense Aviation Has a Readiness Problem. AI Can Help Fix It",
                Namespace(),
            )
        )

    def test_all_sensitive_translation_summary_is_a_clean_skip(self) -> None:
        self.assertTrue(
            all_reports_skipped_by_translation_title_guard({
                "selected_count": 2,
                "successful_count": 0,
                "sensitive_skipped_count": 2,
                "failures": [],
            })
        )

    def test_empty_outputs_from_real_failures_are_not_a_clean_skip(self) -> None:
        self.assertFalse(
            all_reports_skipped_by_translation_title_guard({
                "selected_count": 2,
                "successful_count": 0,
                "sensitive_skipped_count": 0,
                "failures": [{"error": "DeepSeek unavailable"}],
            })
        )


if __name__ == "__main__":
    unittest.main()
