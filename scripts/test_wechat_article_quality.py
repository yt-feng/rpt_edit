#!/usr/bin/env python3
from __future__ import annotations

import unittest

from wechat_article_quality import audit_wechat_article_markdown, sanitize_wechat_article_markdown


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


if __name__ == "__main__":
    unittest.main()
