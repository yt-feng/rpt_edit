#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from build_portal_translated_reports import title_is_sensitive
from sensitive_content_guard import (
    blocked_wechat_title_reason,
    neutralize_wechat_title,
    wechat_title_neutrality_issues,
)
from push_portal_translated_to_wechat_drafts import (
    legacy_all_reports_skipped_by_translation_title_guard,
    neutralize_markdown_headings,
    replace_first_markdown_heading,
    translated_article_title_metadata,
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

    def test_trade_conflict_title_is_reframed_and_article_is_kept(self) -> None:
        title = "高盛：贸易战与出口管制如何影响供应链"
        self.assertEqual("politically_sensitive", blocked_wechat_title_reason(title))
        rewritten, _changes = neutralize_wechat_title(title)
        self.assertEqual("高盛：跨境贸易与行业变化观察", rewritten)
        self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_translation_gate_blocks_without_calling_deepseek(self) -> None:
        self.assertTrue(
            title_is_sensitive(
                "Defense Aviation Has a Readiness Problem. AI Can Help Fix It",
                Namespace(),
            )
        )

    def test_reported_titles_are_rewritten_to_neutral_factual_titles(self) -> None:
        cases = {
            "摩根大通：中国权益策略-AI主题-去杠杆是健康重置":
                "摩根大通：AI主题与市场结构变化观察",
            "德意志银行：关于人民币汇率估值的研究观察":
                "德意志银行：货币定价框架与相关指标观察",
            "花旗：中国宏观，信贷数据与市场预期存在差异":
                "花旗：近期数据与市场预期比较观察",
        }
        for original, expected in cases.items():
            with self.subTest(original=original):
                rewritten, changes = neutralize_wechat_title(original)
                self.assertEqual(expected, rewritten)
                self.assertTrue(changes)
                self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_sensitive_topic_is_reframed_without_dropping_article(self) -> None:
        original = "波士顿咨询：军用飞机战备问题-AI可协助修复"
        rewritten, changes = neutralize_wechat_title(original)
        self.assertEqual("波士顿咨询：航空运维与AI技术应用观察", rewritten)
        self.assertTrue(changes)
        self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_company_title_keeps_source_backed_subject_and_direction(self) -> None:
        original = "瑞银：大族激光盈利下降，订单放缓"
        rewritten, changes = neutralize_wechat_title(original)
        self.assertEqual(original, rewritten)
        self.assertEqual([], changes)
        self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_specific_factual_titles_are_not_replaced_by_generic_observations(self) -> None:
        titles = (
            "摩根大通：中国基础材料，韧性需求支撑高金属价格与矿企盈利",
            "摩根士丹利：海光信息二季度净利润11亿元超预期8%",
            "德意志银行：达芬奇手术机器人三重护城河正被侵蚀",
            "瑞银：韩国单股杠杆ETF新规-AUM已缩水29%",
            "摩根士丹利：月度追踪，6月数据出现变化，三季度更弱",
            "摩根士丹利：台积电激进资本支出应对更强AI需求",
            "波士顿咨询：BCG，AI代理让CMO角色更关键",
        )
        for original in titles:
            with self.subTest(original=original):
                rewritten, changes = neutralize_wechat_title(original)
                self.assertEqual(original, rewritten)
                self.assertEqual([], changes)
                self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_sensitive_titles_are_reframed_without_erasing_the_specific_subject(self) -> None:
        cases = {
            "高盛：美国关税影响追踪-洛杉矶港进口未来两周先升后降":
                "高盛：洛杉矶港进口未来两周变化",
            "野村：中国拟对锂电池征收消费税":
                "野村：锂电池行业规则与成本变化",
            "摩根士丹利：稀土，资金流向何处-中国管制推动90%涨幅":
                "摩根士丹利：基础材料行业数据与主题变化观察",
            "IMF：IMF反洗钱与反恐融资操作指引":
                "IMF：合规治理与组织流程观察",
        }
        for original, expected in cases.items():
            with self.subTest(original=original):
                rewritten, changes = neutralize_wechat_title(original)
                self.assertEqual(expected, rewritten)
                self.assertTrue(changes)
                self.assertEqual([], wechat_title_neutrality_issues(rewritten))

    def test_visible_article_heading_uses_the_same_neutral_title(self) -> None:
        markdown = "# 花旗：中国宏观，信贷数据与市场预期存在差异\n\n正文内容。\n"
        neutral, _changes = neutralize_wechat_title(
            "花旗：中国宏观，信贷数据与市场预期存在差异"
        )
        rewritten = replace_first_markdown_heading(markdown, neutral)
        self.assertTrue(rewritten.startswith(f"# {neutral}\n"))
        self.assertNotIn("中国宏观", rewritten.splitlines()[0])

    def test_section_headings_are_neutralized_without_removing_sections(self) -> None:
        markdown = (
            "# 原标题\n\n"
            "## 信贷数据与市场预期存在差异\n\n第一节。\n\n"
            "## AI应用范围与企业流程观察\n\n第二节。\n"
        )
        rewritten, changes = neutralize_markdown_headings(markdown, "花旗：近期数据观察")
        self.assertIn("## 信贷数据与市场预期存在差异", rewritten)
        self.assertIn("## AI应用范围与企业流程观察", rewritten)
        self.assertIn("第一节。", rewritten)
        self.assertIn("第二节。", rewritten)
        self.assertEqual([], changes)

    def test_malformed_model_title_uses_upload_fallback_instead_of_dropping_article(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            report_dir = Path(tmp) / "01-0001-BCG_CEOs-and-Boards-Are-Aligned-on-AI"
            report_dir.mkdir()
            (report_dir / "translated.md").write_text(
                "# 波士顿咨询：BCG与AI0002CEOs和BoardsAre\n\n正文内容。\n",
                encoding="utf-8",
            )
            (report_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "波士顿咨询：BCG与AI0002CEOs和BoardsAre",
                    "source_pdf": "BCG_CEOs-and-Boards-Are-Aligned-on-AI.pdf",
                    "institution_name": "波士顿咨询",
                }, ensure_ascii=False),
                encoding="utf-8",
            )
            metadata = translated_article_title_metadata(report_dir)

        self.assertEqual("波士顿咨询：AI技术与相关数据观察", metadata["wechat_title"])
        self.assertEqual([], wechat_title_neutrality_issues(metadata["wechat_title"]))
        self.assertTrue(
            any(
                change.startswith("quality_fallback:")
                for change in metadata["title_decision"]["neutralization_changes"]
            )
        )

    def test_all_sensitive_translation_summary_is_a_clean_skip(self) -> None:
        self.assertTrue(
            legacy_all_reports_skipped_by_translation_title_guard({
                "selected_count": 2,
                "successful_count": 0,
                "sensitive_skipped_count": 2,
                "failures": [],
            })
        )

    def test_empty_outputs_from_real_failures_are_not_a_clean_skip(self) -> None:
        self.assertFalse(
            legacy_all_reports_skipped_by_translation_title_guard({
                "selected_count": 2,
                "successful_count": 0,
                "sensitive_skipped_count": 0,
                "failures": [{"error": "DeepSeek unavailable"}],
            })
        )


if __name__ == "__main__":
    unittest.main()
