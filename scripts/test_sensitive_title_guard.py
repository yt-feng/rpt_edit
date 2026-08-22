#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from argparse import Namespace
from pathlib import Path

from build_portal_translated_reports import title_is_sensitive
from institution_names import infer_institution_name
from sensitive_content_guard import (
    blocked_wechat_title_reason,
    hard_blocked_wechat_title_reason,
    neutralize_wechat_title,
    nomura_sensitive_wechat_report_reason,
    nomura_sensitive_wechat_report_reasons,
    wechat_title_neutrality_issues,
)
from push_portal_translated_to_wechat_drafts import (
    legacy_all_reports_skipped_by_translation_title_guard,
    neutralize_markdown_headings,
    replace_first_markdown_heading,
    translated_article_title_metadata,
)


class SensitiveTitleGuardTests(unittest.TestCase):
    def test_nomura_institution_aliases_are_normalized(self) -> None:
        for value in (
            "NOM-Strategy Trade-Short USD CNH.pdf",
            "Nomura FX Insights.pdf",
            "野村证券：亚洲汇率观察",
        ):
            with self.subTest(value=value):
                self.assertEqual("野村", infer_institution_name(value))

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

    def test_hard_blocks_rmb_pricing_title_term(self) -> None:
        for title in (
            "德意志银行：人民币定价框架与相关指标观察",
            "高盛：人民币 定价机制出现变化",
        ):
            with self.subTest(title=title):
                self.assertEqual(
                    "forbidden_title_term_rmb_pricing",
                    hard_blocked_wechat_title_reason(title),
                )

    def test_hard_title_term_does_not_expand_to_adjacent_currency_topics(self) -> None:
        self.assertIsNone(
            hard_blocked_wechat_title_reason("德意志银行：人民币汇率估值的研究观察")
        )

    def test_nomura_sensitive_report_is_blocked_from_wechat(self) -> None:
        metadata = {
            "raw_title": "野村：行业技术与相关数据观察",
            "wechat_title": "野村：行业技术与相关数据观察",
            "source_report_name": (
                "61-NOM-Strategy Trade-Short USD CNH-4 5 conviction remains intact-"
                "but raising our guard-260817"
            ),
            "title_decision": {},
        }
        reasons = nomura_sensitive_wechat_report_reasons(
            metadata,
            "报告维持人民币相对美元中期看多观点，并认为人民币仍被低估8.5%。",
        )

        self.assertIn("raw_title:generic_sensitive_fallback", reasons)
        self.assertIn("source_report_name:directional_currency_trade", reasons)
        self.assertIn("article_content:china_systemic_topic", reasons)
        metadata["sensitive_title_reasons"] = reasons
        self.assertEqual(
            "nomura_sensitive_report",
            nomura_sensitive_wechat_report_reason(metadata),
        )

    def test_nomura_sensitive_title_decision_is_blocked(self) -> None:
        metadata = {
            "institution_name": "野村",
            "raw_title": "野村：相关行业变化观察",
            "wechat_title": "野村：相关行业变化观察",
            "title_decision": {
                "neutralization_changes": ["neutralized:politically_sensitive"],
            },
        }
        reasons = nomura_sensitive_wechat_report_reasons(metadata)

        self.assertEqual(["title_decision:politically_sensitive"], reasons)
        self.assertEqual(
            "nomura_sensitive_report",
            nomura_sensitive_wechat_report_reason(
                {**metadata, "sensitive_title_reasons": reasons}
            ),
        )

    def test_nomura_quality_cleanup_without_sensitive_signal_is_kept(self) -> None:
        metadata = {
            "institution_name": "野村",
            "raw_title": "野村：行业技术与相关数据观察",
            "wechat_title": "野村：行业技术与相关数据观察",
            "source_report_name": "Nomura-AI server supply-chain update",
            "title_decision": {
                "neutralization_changes": ["quality_fallback:long_untranslated_english"],
            },
        }
        self.assertEqual(
            [],
            nomura_sensitive_wechat_report_reasons(
                metadata,
                "AI服务器供应链交付数据与产品迭代进展。",
            ),
        )
        self.assertIsNone(nomura_sensitive_wechat_report_reason(metadata))

    def test_nomura_generic_sensitive_fallback_is_institution_specific(self) -> None:
        nomura = {
            "institution_name": "野村",
            "raw_title": "野村：行业技术与相关数据观察",
            "wechat_title": "野村：行业技术与相关数据观察",
        }
        goldman = {
            "institution_name": "高盛",
            "raw_title": "高盛：行业技术与相关数据观察",
            "wechat_title": "高盛：行业技术与相关数据观察",
        }

        self.assertEqual([], nomura_sensitive_wechat_report_reasons(nomura))
        self.assertEqual([], nomura_sensitive_wechat_report_reasons(goldman))
        self.assertIsNone(
            nomura_sensitive_wechat_report_reason({
                **goldman,
                "sensitive_title_reasons": ["raw_title:generic_sensitive_fallback"],
            })
        )

    def test_non_nomura_institution_is_not_inferred_from_display_title(self) -> None:
        metadata = {
            "institution_name": "高盛",
            "raw_title": "高盛：野村季度业绩与人民币估值观察",
            "wechat_title": "高盛：野村季度业绩与人民币估值观察",
            "source_report_name": "Goldman-quarterly-broker-results",
            "title_decision": {
                "neutralization_changes": ["neutralized:china_systemic_topic"],
            },
        }
        self.assertEqual([], nomura_sensitive_wechat_report_reasons(metadata))
        self.assertIsNone(nomura_sensitive_wechat_report_reason(metadata))

    def test_nomura_evaluative_wording_alone_is_not_a_sensitive_report(self) -> None:
        metadata = {
            "institution_name": "野村",
            "raw_title": "野村：AI服务器估值低估",
            "wechat_title": "野村：AI服务器估值观察",
            "source_report_name": "Nomura-AI-server-valuation",
            "title_decision": {
                "neutralization_changes": [
                    "neutralized:evaluative_or_adversarial_wording",
                ],
            },
        }
        self.assertEqual([], nomura_sensitive_wechat_report_reasons(metadata))
        self.assertIsNone(nomura_sensitive_wechat_report_reason(metadata))

    def test_concrete_nomura_report_is_not_blocked_by_incidental_body_term(self) -> None:
        metadata = {
            "institution_name": "野村",
            "raw_title": "野村：半导体设备订单与交付数据更新",
            "wechat_title": "野村：半导体设备订单与交付数据更新",
            "source_report_name": "Nomura-semiconductor-equipment-orders",
        }
        self.assertEqual(
            [],
            nomura_sensitive_wechat_report_reasons(
                metadata,
                "正文比较了台湾半导体设备进口数据与季度交付节奏。",
            ),
        )

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
