#!/usr/bin/env python3
from __future__ import annotations

import json
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from build_kc_translated_reports import report_title
from pdf_to_xhs_batch import wechat_title_from_filename
from push_kc_translated_to_wechat_drafts import sharpen_wechat_title, write_wechat_title_log
from sensitive_content_guard import sanitize_wechat_stock_language
from wechat_title_optimizer import (
    build_filename_title_repair_prompt,
    build_filename_title_translation_prompt,
    clean_filename_wechat_title,
    choose_filename_anchored_title,
    decide_filename_anchored_title,
    filename_title_fallback,
    required_filename_terms,
    strip_source_filename_noise,
    title_quality_issues,
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
        self.assertIn("可用钩子证据", prompt)

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
            evidence_text="公司态度反而更加谨慎，通胀压力继续加大。",
        )
        self.assertEqual(sharpened, selected)

    def test_unsupported_contrarian_hook_is_rejected(self) -> None:
        invented = "巴克莱：日本市场策略-公司谨慎和通胀压力反而加大"
        selected = choose_filename_anchored_title(
            [EXPECTED_TITLE, invented, EXPECTED_TITLE],
            SOURCE_FILENAME,
            "巴克莱",
            evidence_text="报告讨论公司谨慎和通胀压力。",
        )
        self.assertEqual(EXPECTED_TITLE, selected)

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

    def test_upload_cleanup_preserves_semantic_hyphens(self) -> None:
        cases = [
            "伯恩斯坦：PayPal-Stripe第二轮交易或重塑全球支付",
            "花旗：埃斯顿2Q26盈利增9.8-14.8倍，六成来自一次性收益",
            "高盛：口服IL-23通过NewCo与合并结构出海",
        ]
        for title in cases:
            with self.subTest(title=title):
                institution = title.split("：", 1)[0]
                self.assertEqual(title, sharpen_wechat_title(title, institution))

    def test_vacuous_research_note_prefix_is_removed(self) -> None:
        raw = "摩根大通：研究笔记，中国家电六月零售数据观察"
        self.assertEqual(
            "摩根大通：中国家电六月零售数据观察",
            clean_filename_wechat_title(raw, "摩根大通"),
        )
        self.assertEqual(
            "摩根大通：中国家电六月零售数据观察",
            sharpen_wechat_title(raw, "摩根大通"),
        )

    def test_vacuous_industry_observation_prefix_is_removed(self) -> None:
        raw = "野村：行业观察，半导体封装基板出货同比增长36%"
        self.assertEqual(
            "野村：半导体封装基板出货同比增长36%",
            clean_filename_wechat_title(raw, "野村"),
        )

    def test_all_source_technical_acronyms_are_mandatory(self) -> None:
        source = "Jefferies-PCB CCL update-260714.pdf"
        self.assertEqual(["PCB", "CCL"], required_filename_terms(source, "杰富瑞"))
        selected, decision = decide_filename_anchored_title(
            [
                "杰富瑞：CCL更新",
                "杰富瑞：PCB与CCL更新，出货增长36%",
                "杰富瑞：PCB与CCL供需出现反转",
            ],
            source,
            "杰富瑞",
            evidence_text="PCB与CCL出货同比增长36%。",
        )
        self.assertIn("PCB", selected)
        self.assertIn("CCL", selected)
        self.assertIn("36%", selected)
        self.assertEqual("supported_hook", decision["selection_reason"])
        rejected = {item["title"]: item["reasons"] for item in decision["rejected_candidates"]}
        self.assertTrue(any("missing_required_terms=PCB" in reason for reason in rejected["杰富瑞：CCL更新"]))

    def test_exchange_and_finance_shorthand_are_not_literal_requirements(self) -> None:
        source = (
            "MS-Where Are We Trading Now- Heading into EPS- Focused on AI ROIC-"
            "MSFT.US-260714.pdf"
        )
        self.assertEqual(["AI"], required_filename_terms(source, "MS"))

    def test_tourism_title_prefers_complete_chinese_candidate(self) -> None:
        source = (
            "MS-China Tourism Group Duty Free-1880.HK-2Q26 preliminary results-"
            "sequentially weaker as expected-260714.pdf"
        )
        selected, decision = decide_filename_anchored_title(
            [
                "中国中免2Q26初步业绩：环比走弱符合预期",
                "中国中免2Q26：收入降2%利润降20%",
                "中国中免2Q26：毛利率改善1.44个百分点",
            ],
            source,
            "MS",
            evidence_text="中国中免2Q26初步业绩环比走弱符合预期。",
        )
        self.assertEqual("摩根士丹利：中国中免2Q26初步业绩，环比走弱符合预期", selected)
        self.assertEqual([], decision["selected_quality_issues"])
        self.assertNotIn("HK", decision["required_terms"])

    def test_key_stock_ideas_becomes_complete_neutral_chinese(self) -> None:
        source = "MS-Memory Cycle Debates - Key Stock Ideas-260714.pdf"
        selected, _decision = decide_filename_anchored_title(
            [
                "存储周期辩论-关键股票观点",
                "存储周期辩论-关键股票观点：DRAM价格增速回落但市场理性",
                "存储周期辩论-关键股票观点：周期拉长而非崩塌",
            ],
            source,
            "MS",
            evidence_text="DRAM价格增速回落，但市场表现更为理性。",
        )
        self.assertEqual("摩根士丹利：存储周期讨论-核心公司线索", selected)
        self.assertNotIn("股票", selected)
        self.assertEqual([], title_quality_issues(selected, "MS", source))

    def test_ai_only_fallback_cannot_beat_complete_cio_title(self) -> None:
        source = (
            "MS-2Q26 CIO Survey- IT Services Lags Broader Budget Acceleration as AI "
            "Continues to Crowd Out Discretionary Spend-260716.pdf"
        )
        selected, decision = decide_filename_anchored_title(
            [
                "MS：2Q26 CIO调查-IT服务落后于预算加速，AI持续挤出可自由支配支出",
                "MS：2Q26 CIO调查-IT预算加速至3.8%，但IT服务增速降至1.8%",
                "MS：2Q26 CIO调查-AI从推动力变挤出者，IT服务成唯一下滑支出",
            ],
            source,
            "MS",
            evidence_text="AI持续挤出可自由支配支出，IT服务增速降至1.8%。",
        )
        self.assertEqual("摩根士丹利：2Q26CIO调查-AI从推动力变挤出者", selected)
        self.assertEqual([], decision["selected_quality_issues"])
        self.assertNotEqual("摩根士丹利：AI", selected)

    def test_generic_series_title_must_use_body_thesis(self) -> None:
        source = "NOM-FX Insights-Thoughts on USD-260715.pdf"
        selected, decision = decide_filename_anchored_title(
            [
                "NOMFX洞察-对美元的思考",
                "NOMFX洞察-美元拐点未到，三个变量决定方向",
                "NOMFX洞察-美元拐点未到，6月核心CPI环比0%低于预期",
            ],
            source,
            "NOM",
            evidence_text="美元拐点尚未到来。6月核心CPI环比0%低于预期。",
        )
        self.assertTrue(decision["generic_series_source"])
        self.assertEqual("series_body_thesis", decision["selection_reason"])
        self.assertIn("美元拐点未到", selected)
        self.assertNotIn("宏观观察笔记", selected)

    def test_hard_gate_detects_all_reported_bad_shapes(self) -> None:
        bad_titles = [
            "摩根士丹利：中国TourismGroupDutyFree1880.HK",
            "摩根士丹利：存储周期讨论-关键",
            "摩根士丹利：AI",
            "野村：宏观观察笔记",
        ]
        for title in bad_titles:
            with self.subTest(title=title):
                self.assertTrue(title_quality_issues(title))

    def test_hard_gate_detects_truncated_number_and_forbidden_call(self) -> None:
        self.assertIn(
            "bare_trailing_number",
            title_quality_issues("花旗：埃斯顿2Q26盈利增9.8-14.8倍至5200"),
        )
        self.assertIn(
            "forbidden_public_wording",
            title_quality_issues("美银：大立光上调至买入，CPO驱动业务变化"),
        )

    def test_overview_filename_requires_a_body_thesis(self) -> None:
        source = "MS-China Autos - Shared Mobility- Autos Overview-260714.pdf"
        selected, decision = decide_filename_anchored_title(
            [
                "中国汽车-共享出行-汽车行业概览",
                "中国汽车周度订单放缓，八月产品周期或成转折点",
                "中国汽车共享出行：订单放缓但新品周期临近",
            ],
            source,
            "MS",
            evidence_text="周度订单放缓，但八月产品周期临近。",
        )
        self.assertTrue(decision["generic_series_source"])
        self.assertNotIn("行业概览", selected)
        self.assertIn("订单", selected)

    def test_repair_prompt_names_completeness_failures(self) -> None:
        prompt = build_filename_title_repair_prompt(
            "MS-Where Are We Trading Now- Heading into EPS- Focused on AI ROIC-260714.pdf",
            "MS",
            "财报季前，市场聚焦AI投入回报率。",
            ["摩根士丹利：AI"],
            ["body_too_short"],
        )
        self.assertIn("摩根士丹利", prompt)
        self.assertIn("不能只写 AI", prompt)
        self.assertIn("body_too_short", prompt)

    def test_generation_retries_once_when_all_first_pass_titles_are_broken(self) -> None:
        source = "MS-Where Are We Trading Now- Heading into EPS- Focused on AI ROIC-260714.pdf"
        args = SimpleNamespace(wechat_title_refine=True)
        responses = [
            '{"titles":["AI","AI","AI"]}',
            '{"titles":["财报季前聚焦AI投入回报率","AI投入回报率成为定价分水岭","AI投入回报率分化加大"]}',
        ]
        with patch("pdf_to_xhs_batch.call_deepseek", side_effect=responses) as mocked:
            selected, decision = wechat_title_from_filename(
                source,
                "# 原标题\n\n财报季前，市场聚焦AI投入回报率，相关表现分化。",
                "MS",
                args,
            )
        self.assertEqual(2, mocked.call_count)
        self.assertTrue(decision["repair_attempted"])
        self.assertIn("AI投入回报率", selected)
        self.assertEqual([], decision["selected_quality_issues"])

    def test_deterministic_fallback_repairs_all_bad_deepseek_candidates(self) -> None:
        source = "Jefferies-PCB CCL update-260714.pdf"
        selected, decision = decide_filename_anchored_title(
            ["杰富瑞：CCL更新", "杰富瑞：CCL近期变化", "杰富瑞：CCL供需观察"],
            source,
            "杰富瑞",
        )
        self.assertIn("PCB", selected)
        self.assertIn("CCL", selected)
        self.assertEqual("fallback_missing_required_terms", decision["selection_reason"])

    def test_daily_title_log_keeps_source_candidates_and_final_title(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            output_dir = Path(tmp)
            path = write_wechat_title_log(
                output_dir,
                "260716",
                "xhs_notes/dropbox",
                [{
                    "source_report_name": "Jefferies-PCB CCL update-260714",
                    "institution_name": "杰富瑞",
                    "raw_title": "杰富瑞：研究笔记，PCB与CCL更新",
                    "wechat_title": "杰富瑞：PCB与CCL出货增长36%",
                    "report_dir": "report-1",
                    "title_decision": {
                        "raw_candidates": ["杰富瑞：CCL更新", "杰富瑞：PCB与CCL出货增长36%"],
                        "selected_title": "杰富瑞：PCB与CCL出货增长36%",
                    },
                }],
            )
            payload = json.loads(path.read_text(encoding="utf-8"))
            self.assertEqual(1, payload["article_count"])
            self.assertEqual("杰富瑞：PCB与CCL出货增长36%", payload["articles"][0]["final_wechat_title"])
            self.assertEqual(2, len(payload["articles"][0]["generation_decision"]["raw_candidates"]))

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
