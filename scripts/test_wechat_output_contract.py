#!/usr/bin/env python3
"""Contract tests for public-safe WeChat rendering and covers."""

from __future__ import annotations

import tempfile
import unittest
from pathlib import Path

from PIL import Image

from push_portal_translated_to_wechat_drafts import (
    FINAL_CTA_TEXT,
    PUBLIC_SITE_HOST,
    PUBLIC_SITE_HOST_PLACEHOLDER,
    blockquote_html,
    is_explicit_portal_comment,
    materialize_private_article_payload,
    portal_comment_html,
    prepare_cover_upload_image,
    truncate_complete_sentences,
)
from push_xhs_notes_to_wechat_drafts import choose_cover_image


class WeChatOutputContractTests(unittest.TestCase):
    def test_comment_renderer_always_uses_public_label_once(self) -> None:
        legacy = portal_comment_html("**编辑评论：** 结合样本范围理解。")
        current = portal_comment_html("KC评论：结合样本范围理解。")

        for rendered in (legacy, current):
            self.assertEqual(1, rendered.count("KC评论："))
            self.assertNotIn("编辑评论", rendered)
            self.assertIn("结合样本范围理解", rendered)

    def test_ordinary_quotes_are_not_relabelled_as_editorial_comments(self) -> None:
        self.assertFalse(is_explicit_portal_comment("高盛在报告中写道：需求仍在增长。"))
        self.assertTrue(is_explicit_portal_comment("编辑评论：结合样本范围理解。"))
        rendered = blockquote_html("高盛在报告中写道：需求仍在增长。")
        self.assertIn("<blockquote", rendered)
        self.assertNotIn("KC评论", rendered)

    def test_private_values_are_materialized_only_in_request_clone(self) -> None:
        public_articles = [{
            "title": "测试",
            "content": f"<p>{FINAL_CTA_TEXT}</p><p>legacy:{PUBLIC_SITE_HOST_PLACEHOLDER}</p>",
            "content_source_url": f"https://{PUBLIC_SITE_HOST_PLACEHOLDER}/report/1",
        }]
        submitted = materialize_private_article_payload(
            public_articles,
            "https://private.example.invalid",
        )

        self.assertEqual(f"更新信息参见{PUBLIC_SITE_HOST_PLACEHOLDER}", FINAL_CTA_TEXT)
        self.assertIn(PUBLIC_SITE_HOST_PLACEHOLDER, public_articles[0]["content"])
        self.assertNotIn(PUBLIC_SITE_HOST, public_articles[0]["content"])
        self.assertNotIn(PUBLIC_SITE_HOST_PLACEHOLDER, submitted[0]["content"])
        self.assertIn(PUBLIC_SITE_HOST, submitted[0]["content"])
        self.assertNotIn("private.example.invalid", submitted[0]["content"])
        self.assertIn(PUBLIC_SITE_HOST_PLACEHOLDER, public_articles[0]["content_source_url"])
        self.assertIn("private.example.invalid", submitted[0]["content_source_url"])

    def test_body_budget_keeps_only_complete_sentences(self) -> None:
        source = "第一句完整。第二句会在预算边界之后继续展开。"
        self.assertEqual("第一句完整。", truncate_complete_sentences(source, 8))
        self.assertEqual("", truncate_complete_sentences("这个短语没有完整句号", 8))

    def test_private_site_rejects_non_origin_urls(self) -> None:
        for value in (
            "http://private.example.invalid",
            "https://private.example.invalid/path",
            "https://user@private.example.invalid",
            "https://private.example.invalid:8443",
        ):
            with self.subTest(value=value), self.assertRaises(ValueError):
                materialize_private_article_payload([], value)

    def test_cover_is_always_a_valid_wechat_landscape_jpeg(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = root / "report"
            assets = report / "assets"
            output = root / "output"
            assets.mkdir(parents=True)
            portrait = assets / "cover.png"
            Image.new("RGB", (480, 960), (18, 42, 66)).save(portrait)

            source = choose_cover_image(report, [], output / "_assets")
            normalized = prepare_cover_upload_image(source, output, "article_01")

            with Image.open(normalized) as image:
                self.assertEqual("JPEG", image.format)
                self.assertEqual((1200, 675), image.size)

    def test_missing_or_corrupt_cover_falls_back_to_valid_jpeg(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report = root / "report"
            output = root / "output"
            report.mkdir()
            fallback = choose_cover_image(report, [], output / "_assets")
            fallback.write_bytes(b"not-an-image")

            normalized = prepare_cover_upload_image(fallback, output, "article_02")

            with Image.open(normalized) as image:
                self.assertEqual("JPEG", image.format)
                self.assertEqual((1200, 675), image.size)


if __name__ == "__main__":
    unittest.main()
