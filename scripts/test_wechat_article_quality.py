#!/usr/bin/env python3
from __future__ import annotations

import unittest

from wechat_article_quality import (
    WECHAT_EDITORIAL_GUARD_ZH,
    WECHAT_EDITOR_SYSTEM_PROMPT,
    WECHAT_REFERENCE_TONE_ZH,
    audit_wechat_article_markdown,
    compose_wechat_editor_prompt,
    sanitize_wechat_article_markdown,
)


class WeChatArticleQualityTests(unittest.TestCase):
    def sanitize(self, markdown: str) -> str:
        cleaned, _changes = sanitize_wechat_article_markdown(markdown)
        return cleaned

    def test_removes_complete_unresolved_question_section(self) -> None:
        source = """# IMF：一个具体判断

导语保留。

## 数据已经给出方向

第一段保留。

## 该报告未解决的问题

这段不应出现。

> 编辑评论：完整报告里还有更多问题值得继续看。

## 执行节奏决定结果

最后一段保留。
"""
        cleaned = self.sanitize(source)
        self.assertNotIn("未解决的问题", cleaned)
        self.assertNotIn("这段不应出现", cleaned)
        self.assertNotIn("完整报告", cleaned)
        self.assertIn("## 执行节奏决定结果", cleaned)
        self.assertIn("最后一段保留", cleaned)

    def test_removes_bold_trailing_meta_section(self) -> None:
        source = """# 世界银行：主判断

## 证据支持判断

正文保留。

**报告尚未回答**

这是一段结尾悬念。
"""
        cleaned = self.sanitize(source)
        self.assertIn("正文保留", cleaned)
        self.assertNotIn("报告尚未回答", cleaned)
        self.assertNotIn("结尾悬念", cleaned)

    def test_removes_cta_sentence_without_deleting_analysis(self) -> None:
        source = """# 麦肯锡：主判断

## 变化来自执行而非口号

样本覆盖了三类公司。更多完整报告可扫码加入社群查看。真正的差异来自交付周期。
"""
        cleaned = self.sanitize(source)
        self.assertIn("样本覆盖了三类公司。", cleaned)
        self.assertIn("真正的差异来自交付周期。", cleaned)
        self.assertNotIn("扫码", cleaned)
        self.assertNotIn("社群", cleaned)

    def test_removes_generated_fixed_link_so_renderer_owns_the_ending(self) -> None:
        source = """# 国际清算银行：主判断

## 样本差异更值得看

正文。

更新信息参见portal.example.invalid
"""
        cleaned = self.sanitize(source)
        self.assertNotIn("更新信息参见", cleaned)
        self.assertNotIn("ⅾеѕk", cleaned)

    def test_keeps_source_limitation_inside_an_analysis_paragraph(self) -> None:
        source = """# 波士顿咨询：主判断

## 样本变化来自流程重构

报告明确说明，样本只覆盖大型企业，向中小企业外推仍需验证。这个限定条件应被保留。
"""
        cleaned = self.sanitize(source)
        self.assertIn("向中小企业外推仍需验证", cleaned)
        self.assertIn("限定条件应被保留", cleaned)

    def test_keeps_non_promotional_source_language(self) -> None:
        source = """# 麦肯锡：主判断

## 企业更关注现金流而不是规模

报告显示，用户社群贡献了30%的复购，这里描述的是公司运营事实。
"""
        cleaned = self.sanitize(source)
        self.assertIn("企业更关注现金流", cleaned)
        self.assertIn("用户社群贡献了30%的复购", cleaned)

    def test_separate_facts_cannot_form_a_cta_across_sentence_boundaries(self) -> None:
        # Previously the sanitizer retained both sentences while its audit
        # combined them into `完整报告.{0,24}查看` and rejected the article.
        for delimiter in ("。", "；", ";", "！", "?", "\n"):
            with self.subTest(delimiter=delimiter):
                fact = f"完整报告覆盖了三类公司{delimiter}查看样本数据可见交付周期缩短。"
                source = f"# 研究机构：交付周期变化\n\n## 样本数据解释变化\n\n{fact}\n"
                cleaned, changes = sanitize_wechat_article_markdown(source)
                self.assertIn(fact, cleaned)
                self.assertNotIn("removed_model_cta", changes)
                self.assertEqual([], audit_wechat_article_markdown(cleaned))
                self.assertEqual(cleaned, self.sanitize(cleaned))

    def test_portal_report_vocabulary_and_assets_are_preserved(self) -> None:
        fact = "企业通过 Customer Portal 提供数据，Transportal 平台覆盖三类客户。"
        image = "![数据平台](assets/portal_chart.png)"
        source = f"# 研究机构：客户平台覆盖范围\n\n## 样本说明平台使用情况\n\n{fact}\n\n{image}\n"
        cleaned = self.sanitize(source)
        self.assertIn(fact, cleaned)
        self.assertIn(image, cleaned)
        self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_actual_ctas_and_private_brand_tokens_remain_blocked(self) -> None:
        for cta in (
            "完整报告可在下方查看。",
            "更多内容欢迎访问 Portal。",
            "portal.example.invalid",
            "Portal Suite",
            "".join(("kc", "desk", ".com")),
            "ΚСⅾеѕk",
        ):
            with self.subTest(cta=cta):
                source = f"# 研究机构：交付周期变化\n\n## 样本说明变化\n\n正文事实保留。{cta}\n"
                self.assertIn("model_cta", audit_wechat_article_markdown(source))
                cleaned = self.sanitize(source)
                self.assertIn("正文事实保留。", cleaned)
                self.assertNotIn(cta, cleaned)
                self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_keeps_complete_portal_image_placeholder(self) -> None:
        source = """# 波士顿咨询：主判断

## 图表说明变化来自执行

正文保留。

[[PORTAL_IMAGE_001]]
"""
        cleaned = self.sanitize(source)
        self.assertIn("[[PORTAL_IMAGE_001]]", cleaned)
        self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_portal_placeholder_does_not_hide_real_cta(self) -> None:
        source = """# 波士顿咨询：主判断

## 图表说明变化来自执行

[[PORTAL_IMAGE_001]]

更新信息参见portal.example.invalid
"""
        cleaned = self.sanitize(source)
        self.assertIn("[[PORTAL_IMAGE_001]]", cleaned)
        self.assertNotIn("portal.example.invalid", cleaned)
        self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_cleanup_is_idempotent_and_passes_blocking_audit(self) -> None:
        source = """# OECD：主判断

## 证据支持判断

正文。

## 为什么值得读完整报告

加入社群继续阅读。
"""
        first = self.sanitize(source)
        second = self.sanitize(first)
        self.assertEqual(first, second)
        self.assertEqual([], audit_wechat_article_markdown(first))

    def test_legacy_comment_label_is_normalized_idempotently(self) -> None:
        source = """# 研究机构：主判断

## 数据支持判断

> **编辑评论：** 这个变化需要结合样本范围理解。
"""
        first = self.sanitize(source)
        second = self.sanitize(first)
        self.assertIn("> **KC评论：** 这个变化", first)
        self.assertNotIn("编辑评论", first)
        self.assertEqual(first, second)

    def test_standalone_legacy_comment_becomes_the_exact_kc_blockquote(self) -> None:
        source = """# 研究机构：主判断

## 数据支持判断

编辑评论：47.7%的增速要结合低基数理解。
"""
        cleaned = self.sanitize(source)
        self.assertIn("> **KC评论：** 47.7%的增速", cleaned)
        self.assertNotIn("编辑评论", cleaned)
        self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_removes_model_written_public_site_link_and_repairs_punctuation(self) -> None:
        public_host = "".join(("kc", "desk", ".com"))
        source = f"""# 研究机构：主判断

## 数据支持判断

第一句。，第二句，。

更新信息参见{public_host}
"""
        cleaned = self.sanitize(source)
        self.assertIn("第一句。第二句。", cleaned)
        self.assertNotIn(public_host, cleaned)
        self.assertEqual([], audit_wechat_article_markdown(cleaned))

    def test_reference_tone_contract_encodes_evidence_causality_and_editorial_choice(self) -> None:
        self.assertIn("原文证据 -> 白话解释", WECHAT_REFERENCE_TONE_ZH)
        self.assertIn("锚定紧邻正文中的一个事实或数字", WECHAT_REFERENCE_TONE_ZH)
        self.assertIn("用大白话解释一层因果机制", WECHAT_REFERENCE_TONE_ZH)
        self.assertIn("我更关注的是", WECHAT_REFERENCE_TONE_ZH)
        self.assertIn("之前评论区有人问", WECHAT_REFERENCE_TONE_ZH)
        self.assertIn("白话因果", WECHAT_EDITORIAL_GUARD_ZH)
        self.assertIn("“人民币定价”是微信公开标题硬禁词", WECHAT_EDITORIAL_GUARD_ZH)
        self.assertIn("解释事实之间的因果", WECHAT_EDITOR_SYSTEM_PROMPT)

    def test_prompt_composer_attaches_tone_before_hard_guard_once(self) -> None:
        prompt = compose_wechat_editor_prompt("基础任务")
        self.assertEqual(1, prompt.count("【参考稿语气卡】"))
        self.assertEqual(1, prompt.count("【DeepSeek 交稿硬约束】"))
        self.assertLess(prompt.index("【参考稿语气卡】"), prompt.index("【DeepSeek 交稿硬约束】"))


if __name__ == "__main__":
    unittest.main()
