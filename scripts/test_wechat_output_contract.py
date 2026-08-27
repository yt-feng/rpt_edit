#!/usr/bin/env python3
"""Contract tests for public-safe WeChat rendering and covers."""

from __future__ import annotations

import json
import sys
import tempfile
import unittest
from pathlib import Path
from types import SimpleNamespace
from unittest.mock import patch

from PIL import Image

from push_portal_translated_to_wechat_drafts import (
    AUTHOR,
    BOTTOM_DISCLAIMER,
    BRAND,
    FINAL_CTA_TEXT,
    PUBLIC_SITE_HOST,
    PUBLIC_SITE_HOST_PLACEHOLDER,
    TRANSLATION_VOLUNTEER_NAMES,
    blockquote_html,
    build_article as build_portal_article,
    find_recent_draft_by_titles,
    footer_html,
    hard_blocked_portal_title_record,
    is_explicit_portal_comment,
    materialize_private_article_payload,
    main as portal_uploader_main,
    portal_comment_html,
    prepare_cover_upload_image,
    render_fitted_wechat_html,
    summarize_draft_get_response,
    translation_volunteer_for_article,
    truncate_complete_sentences,
)
from push_xhs_notes_to_wechat_drafts import (
    AUTHOR as XHS_AUTHOR,
    BRAND as XHS_BRAND,
    choose_cover_image,
)


class WeChatOutputContractTests(unittest.TestCase):
    def test_real_portal_builder_uses_shared_identity_and_credits(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            report_dir = root / "01-worldbank-supply-chain"
            report_dir.mkdir()
            (report_dir / "translated.md").write_text(
                "# 世界银行：供应链数据与交付周期更新\n\n"
                "## 企业交付周期呈现新的变化\n\n"
                "报告记录了一个可核验的数据变化。\n",
                encoding="utf-8",
            )
            (report_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "世界银行：供应链数据与交付周期更新",
                    "source_report_original_name": "World Bank supply chain report.pdf",
                }),
                encoding="utf-8",
            )
            args = SimpleNamespace(
                author=AUTHOR,
                body_hook="",
                brand=BRAND,
                content_source_url="",
                disclaimer=BOTTOM_DISCLAIMER,
                dry_run=True,
                image_upload_delay_seconds=0,
                max_body_chars=1200,
                max_content_bytes=18000,
                max_content_chars=19500,
                max_inline_images=0,
                min_inline_images=0,
                timeout=30,
            )

            built = build_portal_article(
                report_dir,
                1,
                args,
                None,
                None,
                root / "output",
                "",
            )

            article = built["article"]
            volunteer = built["translator_name"]
            self.assertEqual("KC桌面", article["author"])
            self.assertIn(volunteer, TRANSLATION_VOLUNTEER_NAMES)
            self.assertIn("外资精译", article["content"])
            self.assertIn(BOTTOM_DISCLAIMER, article["content"])
            self.assertIn(f"撰稿：{volunteer}", article["content"])
            self.assertIn("责编：KC", article["content"])
            self.assertIn("排版：胡桃", article["content"])

    def test_shared_wechat_identity_and_editorial_footer_are_exact(self) -> None:
        self.assertEqual("外资精译", BRAND)
        self.assertEqual("KC桌面", AUTHOR)
        self.assertEqual(BRAND, XHS_BRAND)
        self.assertEqual(AUTHOR, XHS_AUTHOR)

        volunteer = translation_volunteer_for_article("高盛", "AI基础设施报告")
        self.assertIn(volunteer, TRANSLATION_VOLUNTEER_NAMES)
        self.assertRegex(volunteer, r"^[A-Za-z][A-Za-z'-]*$")
        self.assertEqual(
            volunteer,
            translation_volunteer_for_article("高盛", "AI基础设施报告"),
        )
        self.assertGreater(
            len({translation_volunteer_for_article("机构", f"报告-{index}") for index in range(20)}),
            1,
        )

        footer = footer_html(BOTTOM_DISCLAIMER, volunteer)
        self.assertEqual(1, footer.count("——人工智能免责声明（部分内容由人工智能工具辅助生成）"))
        self.assertEqual(1, footer.count(f"撰稿：{volunteer}"))
        self.assertEqual(1, footer.count("责编：KC"))
        self.assertEqual(1, footer.count("排版：胡桃"))

    def test_shared_renderer_owns_opening_disclaimer_and_credits(self) -> None:
        volunteer = translation_volunteer_for_article("世界银行", "供应链报告")
        markdown = (
            "# 世界银行：供应链数据更新\n\n"
            "## 企业交付周期出现变化\n\n"
            "报告记录了一个可核验的变化。\n\n"
            "<p>For informational purposes only. This is an old generated footer.</p>\n"
        )
        content, *_ = render_fitted_wechat_html(
            markdown,
            "供应链数据更新",
            BRAND,
            {},
            [],
            "",
            BOTTOM_DISCLAIMER,
            "",
            "世界银行-供应链报告",
            1200,
            19500,
            18000,
            translator_name=volunteer,
        )

        self.assertIn("外资精译", content)
        self.assertLess(content.index("外资精译"), content.index("供应链数据更新"))
        self.assertNotIn("Portal Suite", content)
        self.assertNotIn("For informational purposes only", content)
        self.assertEqual(1, content.count(BOTTOM_DISCLAIMER))
        self.assertEqual(1, content.count(f"撰稿：{volunteer}"))
        self.assertEqual(1, content.count("责编：KC"))
        self.assertEqual(1, content.count("排版：胡桃"))

    def test_recent_draft_reuse_requires_current_editorial_contract(self) -> None:
        title = "世界银行：供应链数据更新"
        volunteer = translation_volunteer_for_article("世界银行", "供应链报告")
        content, *_ = render_fitted_wechat_html(
            "# 世界银行：供应链数据更新\n\n## 数据发生变化\n\n正文事实。\n",
            "供应链数据更新",
            BRAND,
            {},
            [],
            "",
            BOTTOM_DISCLAIMER,
            "",
            "世界银行-供应链报告",
            1200,
            19500,
            18000,
            translator_name=volunteer,
        )
        expected = {"title": title, "author": AUTHOR, "content": content}
        stale = {
            "media_id": "STALE_MEDIA",
            "content": {"news_item": [{"title": title, "author": "Portal Suite", "content": "<p>Portal Suite</p>"}]},
        }
        current = {"media_id": "CURRENT_MEDIA", "content": {"news_item": [dict(expected)]}}

        with patch(
            "push_portal_translated_to_wechat_drafts.batchget_recent_drafts",
            return_value=[stale],
        ):
            self.assertEqual(
                "",
                find_recent_draft_by_titles(
                    object(),
                    "TOKEN",
                    [title],
                    30,
                    expected_articles=[expected],
                ),
            )
        with patch(
            "push_portal_translated_to_wechat_drafts.batchget_recent_drafts",
            return_value=[current],
        ):
            self.assertEqual(
                "CURRENT_MEDIA",
                find_recent_draft_by_titles(
                    object(),
                    "TOKEN",
                    [title],
                    30,
                    expected_articles=[expected],
                ),
            )

        current_summary = summarize_draft_get_response(
            {"news_item": [dict(expected)]},
            1,
            [expected],
        )
        stale_summary = summarize_draft_get_response(
            {"news_item": stale["content"]["news_item"]},
            1,
            [expected],
        )
        self.assertTrue(current_summary["ok"])
        self.assertTrue(current_summary["matches_editorial_contract"])
        self.assertFalse(stale_summary["ok"])
        self.assertFalse(stale_summary["matches_editorial_contract"])

    def test_portal_hard_block_checks_raw_title_before_neutralized_title(self) -> None:
        record = hard_blocked_portal_title_record({
            "raw_title": "德意志银行：人民币定价框架与相关指标观察",
            "original_title": "德意志银行：货币研究",
            "wechat_title": "德意志银行：货币定价框架与相关指标观察",
        })
        self.assertIsNotNone(record)
        self.assertEqual("forbidden_title_term_rmb_pricing", record["skip_reason"])
        self.assertEqual("raw_title", record["matched_title_field"])
        self.assertIn("人民币定价", record["matched_title"])

    def test_portal_hard_block_checks_final_title_as_a_fail_closed_guard(self) -> None:
        record = hard_blocked_portal_title_record({
            "raw_title": "德意志银行：货币市场与相关指标观察",
            "original_title": "德意志银行：货币研究",
            "source_report_name": "德意志银行-货币市场观察",
            "wechat_title": "德意志银行：人民币定价框架与相关指标观察",
        })
        self.assertIsNotNone(record)
        self.assertEqual("forbidden_title_term_rmb_pricing", record["skip_reason"])
        self.assertEqual("wechat_title", record["matched_title_field"])

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

    def test_portal_uploader_skips_hard_blocked_original_title_before_upload(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            translated_root = root / "translated"
            date_dir = translated_root / "260822"
            output_root = root / "drafts"
            blocked_dir = date_dir / "01-blocked"
            allowed_dir = date_dir / "02-allowed"
            blocked_dir.mkdir(parents=True)
            allowed_dir.mkdir(parents=True)

            (blocked_dir / "translated.md").write_text(
                "# 德意志银行：货币框架与相关指标观察\n\n正文。\n",
                encoding="utf-8",
            )
            (blocked_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "德意志银行：货币框架与相关指标观察",
                    "source_report_original_name": "德意志银行-人民币定价框架.pdf",
                }, ensure_ascii=False),
                encoding="utf-8",
            )
            (allowed_dir / "translated.md").write_text(
                "# 世界银行：供应链数据与企业运营观察\n\n正文。\n",
                encoding="utf-8",
            )
            (allowed_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "世界银行：供应链数据与企业运营观察",
                    "source_report_original_name": "世界银行-供应链数据与企业运营观察.pdf",
                }, ensure_ascii=False),
                encoding="utf-8",
            )

            def fake_build_article(report_dir, *_args, **_kwargs):
                self.assertEqual(allowed_dir, report_dir)
                title = "世界银行：供应链数据与企业运营观察"
                return {
                    "report_dir": str(report_dir),
                    "translated_markdown": str(report_dir / "translated.md"),
                    "raw_title": title,
                    "title": title,
                    "wechat_title": title,
                    "header_title": "供应链数据与企业运营观察",
                    "digest": "供应链数据呈现新的运营变化。",
                    "institution_name": "世界银行",
                    "source_report_name": "世界银行-供应链数据与企业运营观察",
                    "title_decision": {},
                    "article": {
                        "article_type": "news",
                        "title": title,
                        "author": "KC桌面",
                        "digest": "供应链数据呈现新的运营变化。",
                        "content": "<p>正文。</p>",
                        "thumb_media_id": "THUMB_OK",
                    },
                    "cover_image": "allowed-cover.jpg",
                    "inline_images": [],
                    "content_chars": 10,
                    "content_bytes": 13,
                    "visible_text_chars": 3,
                    "body_image_count": 0,
                    "ai_image_count": 0,
                }

            argv = [
                "push_portal_translated_to_wechat_drafts.py",
                "--translated-root", str(translated_root),
                "--date-folder", "260822",
                "--output-root", str(output_root),
                "--max-articles", "all",
                "--trailing-image", "",
                "--site-url", "https://private.example.invalid",
                "--wechat-appid", "test-appid",
                "--wechat-secret", "test-secret",
                "--publish",
                "--image-upload-delay-seconds", "0",
                "--article-delay-seconds", "0",
                "--draft-delay-seconds", "0",
                "--draft-verify-delay-seconds", "0",
            ]
            draft_get = {
                "ok": True,
                "article_count": 1,
                "expected_article_count": 1,
                "matches_expected_article_count": True,
                "titles": ["世界银行：供应链数据与企业运营观察"],
            }
            with (
                patch.object(sys, "argv", argv),
                patch("push_portal_translated_to_wechat_drafts.requests.Session", return_value=object()),
                patch("push_portal_translated_to_wechat_drafts.get_stable_access_token", return_value="TOKEN"),
                patch("push_portal_translated_to_wechat_drafts.build_article", side_effect=fake_build_article) as build_mock,
                patch("push_portal_translated_to_wechat_drafts.find_recent_draft_by_titles", return_value=""),
                patch("push_portal_translated_to_wechat_drafts.add_draft", return_value="MEDIA_OK") as add_mock,
                patch("push_portal_translated_to_wechat_drafts.verify_draft_get", return_value=draft_get),
                patch("push_portal_translated_to_wechat_drafts.submit_publish", return_value="PUBLISH_OK") as publish_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_article_image") as article_image_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_cover_material") as cover_image_mock,
            ):
                self.assertEqual(0, portal_uploader_main())

            self.assertEqual(1, build_mock.call_count)
            self.assertEqual(1, add_mock.call_count)
            self.assertEqual(1, publish_mock.call_count)
            article_image_mock.assert_not_called()
            cover_image_mock.assert_not_called()
            submitted_articles = add_mock.call_args.args[2]
            self.assertEqual(["世界银行：供应链数据与企业运营观察"], [item["title"] for item in submitted_articles])

            summary = json.loads((output_root / "260822" / "wechat_draft_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(2, summary["input_selected_count"])
            self.assertEqual(1, summary["selected_count"])
            self.assertEqual(1, summary["skipped_title_policy_count"])
            skipped = summary["skipped_title_policy"][0]
            self.assertEqual("forbidden_title_term_rmb_pricing", skipped["skip_reason"])
            self.assertEqual("original_title", skipped["matched_title_field"])
            self.assertIn("人民币定价", skipped["matched_title"])
            self.assertEqual(1, summary["draft_count"])

            title_log = json.loads((output_root / "260822" / "wechat_title_log.json").read_text(encoding="utf-8"))
            self.assertEqual(1, title_log["uploaded_count"])
            self.assertEqual(1, title_log["skipped_count"])
            skipped_log = next(item for item in title_log["articles"] if not item["uploaded"])
            self.assertEqual("forbidden_title_term_rmb_pricing", skipped_log["skip_reason"])
            self.assertEqual("original_title", skipped_log["matched_title_field"])
            self.assertIn("人民币定价", skipped_log["matched_title"])

    def test_portal_all_hard_blocked_titles_create_no_remote_work(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            translated_root = root / "translated"
            report_dir = translated_root / "260822" / "01-blocked"
            report_dir.mkdir(parents=True)
            (report_dir / "translated.md").write_text(
                "# 德意志银行：货币框架与相关指标观察\n\n正文。\n",
                encoding="utf-8",
            )
            (report_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "德意志银行：货币框架与相关指标观察",
                    "source_report_original_name": "德意志银行-人民币定价框架.pdf",
                }, ensure_ascii=False),
                encoding="utf-8",
            )

            output_root = root / "drafts"
            argv = [
                "push_portal_translated_to_wechat_drafts.py",
                "--translated-root", str(translated_root),
                "--date-folder", "260822",
                "--output-root", str(output_root),
                "--max-articles", "all",
                "--trailing-image", "",
                "--site-url", "https://private.example.invalid",
                "--wechat-appid", "test-appid",
                "--wechat-secret", "test-secret",
                "--publish",
            ]
            with (
                patch.object(sys, "argv", argv),
                patch("push_portal_translated_to_wechat_drafts.requests.Session") as session_mock,
                patch("push_portal_translated_to_wechat_drafts.get_stable_access_token") as token_mock,
                patch("push_portal_translated_to_wechat_drafts.resolve_repo_asset_path") as asset_mock,
                patch("push_portal_translated_to_wechat_drafts.build_article") as build_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_article_image") as article_image_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_cover_material") as cover_image_mock,
                patch("push_portal_translated_to_wechat_drafts.add_draft") as add_mock,
                patch("push_portal_translated_to_wechat_drafts.submit_publish") as publish_mock,
            ):
                self.assertEqual(0, portal_uploader_main())

            for mocked_call in (
                session_mock,
                token_mock,
                asset_mock,
                build_mock,
                article_image_mock,
                cover_image_mock,
                add_mock,
                publish_mock,
            ):
                mocked_call.assert_not_called()

            output_dir = output_root / "260822"
            self.assertEqual([], list(output_dir.glob("draft_payload_*.json")))
            summary = json.loads((output_dir / "wechat_draft_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(1, summary["input_selected_count"])
            self.assertEqual(0, summary["selected_count"])
            self.assertEqual(1, summary["skipped_title_policy_count"])
            self.assertEqual(0, summary["draft_count"])

    def test_portal_sensitive_nomura_report_creates_no_remote_work(self) -> None:
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            translated_root = root / "translated"
            report_dir = translated_root / "260822" / "61-NOM-strategy-trade"
            report_dir.mkdir(parents=True)
            (report_dir / "translated.md").write_text(
                "# 野村：行业技术与相关数据观察\n\n"
                "报告维持人民币相对美元中期看多观点，并认为人民币仍被低估8.5%。\n",
                encoding="utf-8",
            )
            (report_dir / "translation_status.json").write_text(
                json.dumps({
                    "title": "野村：行业技术与相关数据观察",
                    "source_report_original_name": (
                        "NOM-Strategy Trade-Short USD CNH-4 5 conviction remains intact-"
                        "but raising our guard-260817.pdf"
                    ),
                    "wechat_title_decision": {},
                }, ensure_ascii=False),
                encoding="utf-8",
            )

            output_root = root / "drafts"
            argv = [
                "push_portal_translated_to_wechat_drafts.py",
                "--translated-root", str(translated_root),
                "--date-folder", "260822",
                "--output-root", str(output_root),
                "--max-articles", "all",
                "--trailing-image", "",
                "--site-url", "https://private.example.invalid",
                "--wechat-appid", "test-appid",
                "--wechat-secret", "test-secret",
                "--publish",
            ]
            with (
                patch.object(sys, "argv", argv),
                patch("push_portal_translated_to_wechat_drafts.requests.Session") as session_mock,
                patch("push_portal_translated_to_wechat_drafts.get_stable_access_token") as token_mock,
                patch("push_portal_translated_to_wechat_drafts.resolve_repo_asset_path") as asset_mock,
                patch("push_portal_translated_to_wechat_drafts.build_article") as build_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_article_image") as article_image_mock,
                patch("push_portal_translated_to_wechat_drafts.upload_cover_material") as cover_image_mock,
                patch("push_portal_translated_to_wechat_drafts.add_draft") as add_mock,
                patch("push_portal_translated_to_wechat_drafts.submit_publish") as publish_mock,
            ):
                self.assertEqual(0, portal_uploader_main())

            for mocked_call in (
                session_mock,
                token_mock,
                asset_mock,
                build_mock,
                article_image_mock,
                cover_image_mock,
                add_mock,
                publish_mock,
            ):
                mocked_call.assert_not_called()

            output_dir = output_root / "260822"
            self.assertEqual([], list(output_dir.glob("draft_payload_*.json")))
            summary = json.loads((output_dir / "wechat_draft_summary.json").read_text(encoding="utf-8"))
            self.assertEqual(1, summary["input_selected_count"])
            self.assertEqual(0, summary["selected_count"])
            self.assertEqual(1, summary["skipped_title_policy_count"])
            skipped = summary["skipped_title_policy"][0]
            self.assertEqual("nomura_sensitive_report", skipped["skip_reason"])
            self.assertEqual("野村", skipped["institution_name"])
            self.assertIn(
                "source_report_name:directional_currency_trade",
                skipped["sensitive_title_reasons"],
            )
            self.assertEqual(0, summary["draft_count"])

            title_log = json.loads((output_dir / "wechat_title_log.json").read_text(encoding="utf-8"))
            self.assertEqual(0, title_log["uploaded_count"])
            self.assertEqual(1, title_log["skipped_count"])
            self.assertEqual(
                skipped["sensitive_title_reasons"],
                title_log["articles"][0]["sensitive_title_reasons"],
            )


if __name__ == "__main__":
    unittest.main()
