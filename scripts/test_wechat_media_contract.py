"""Image-specific regressions: publication furniture, crops, and draft readback."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from PIL import Image, ImageDraw, ImageOps
import requests

import push_portal_translated_to_wechat_drafts as portal
import push_xhs_notes_to_wechat_drafts as xhs
from wechat_image_quality import article_image_rejection, is_article_image_candidate, REPO_ROOT
from free_editorial_images import attribution_html


def image(path: Path, color=(51, 107, 151)) -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    result = Image.new("RGB", (600, 400), "white")
    draw = ImageDraw.Draw(result)
    draw.line((40, 350, 180, 260, 310, 300, 560, 80), fill=color, width=12)
    result.save(path)
    return path


def article() -> dict:
    return {
        "title": "高盛：全球市场行业数据更新", "author": portal.AUTHOR,
        "thumb_media_id": "good-cover",
        "content": f'<p>{portal.BRAND}</p><p>完整且不应被图片修复改变的文章正文。</p>'
                   '<img src="https://mmbiz.qpic.cn/mmbiz_jpg/body-image/0?wx_fmt=jpeg" alt="报告图表">'
                   f'<p>{portal.BOTTOM_DISCLAIMER}</p><p>撰稿：Olivia</p><p>责编：KC</p><p>排版：胡桃</p>'
                   '<img src="https://mmbiz.qpic.cn/mmbiz_jpg/contact-image/0?wx_fmt=jpeg" alt="KC桌面">',
    }


def response(payload: dict) -> requests.Response:
    result = requests.Response()
    result.status_code = 200
    result._content = json.dumps(payload).encode()
    return result


class ImageAdmissionTests(unittest.TestCase):
    def test_contact_card_renamed_or_cropped_is_not_article_art(self):
        source = REPO_ROOT / "prompts/zsxq_img.jpg"
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            renamed = root / "source_image_01.jpg"
            renamed.write_bytes(source.read_bytes())
            with Image.open(source) as original:
                cropped = root / "cover.jpg"
                ImageOps.fit(original, (1200, 675)).save(cropped, quality=84)
            self.assertEqual("contact_card", article_image_rejection(renamed))
            self.assertEqual("contact_card", article_image_rejection(cropped))

    def test_legacy_cream_placeholder_rejected_but_sparse_source_chart_retained(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            legacy = root / "cover.png"
            portal.write_fallback_cover(legacy)
            self.assertEqual("legacy_placeholder", article_image_rejection(legacy))
            legacy_editorial = root / "generated.jpg"
            portal.write_editorial_fallback_image(legacy_editorial)
            self.assertEqual("legacy_placeholder", article_image_rejection(legacy_editorial))
            self.assertTrue(is_article_image_candidate(image(root / "source.jpg")))

    def test_both_cover_selectors_skip_bad_assets_and_choose_uploaded_real_picture(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            assets = root / "report/assets"
            assets.mkdir(parents=True)
            bad = assets / "cover.png"
            portal.write_fallback_cover(bad)
            contact = assets / "source_image_01.jpg"
            contact.write_bytes((REPO_ROOT / "prompts/zsxq_img.jpg").read_bytes())
            stock = image(root / "licensed.jpg")
            self.assertEqual(stock, xhs.choose_cover_image(assets.parent, [stock], root / "fallback"))
            self.assertEqual(stock, portal.choose_cover_image(assets.parent, {"one": bad, "two": contact}, root / "fallback", [stock]))
            self.assertEqual([], xhs.extra_asset_images(assets.parent, set()))

    def test_crop_recovery_preserves_distinct_images_and_persists_final_thumb_fields(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            a = image(root / "one.jpg", (200, 40, 40))
            b = image(root / "two.jpg", (20, 170, 80))
            group = [{"cover_image": str(a)}, {"cover_image": str(b)}]
            articles = [dict(article(), title="one"), dict(article(), title="two")]
            public = copy.deepcopy(articles)
            public[0]["content_source_url"] = "PUBLIC_PLACEHOLDER"
            articles[0]["content_source_url"] = "https://private.example.invalid"
            with patch.object(portal, "upload_cover_material", side_effect=["cover-one", "cover-two"]) as upload:
                portal.normalize_group_cover_media(object(), "TOKEN", group, articles, root, 1, 30)
            self.assertEqual(2, upload.call_count)
            self.assertEqual(["cover-one", "cover-two"], [row["thumb_media_id"] for row in articles])
            self.assertNotEqual(Path(group[0]["cover_image"]).read_bytes(), Path(group[1]["cover_image"]).read_bytes())
            for item in group:
                with Image.open(item["cover_image"]) as normalized:
                    self.assertEqual((940, 400), normalized.size)
            portal.sync_article_media_fields(public, articles)
            self.assertEqual("cover-one", public[0]["thumb_media_id"])
            self.assertEqual("PUBLIC_PLACEHOLDER", public[0]["content_source_url"])


class MediaReadbackTests(unittest.TestCase):
    def commons_credit(self, author, filename):
        return attribution_html({"source":"commons", "author":author, "license":"CC BY 4.0",
                                 "source_url":f"https://commons.wikimedia.org/wiki/File:{filename}.jpg",
                                 "license_url":"https://creativecommons.org/licenses/by/4.0/"})

    def test_changed_commons_credit_preserves_group_identity_and_repairs_same_draft(self):
        old = article()
        old["content"] += self.commons_credit("First Photographer", "First")
        expected = article()
        expected["content"] = expected["content"].replace("body-image", "replacement-image") + self.commons_credit("Second Photographer", "Second")
        expected["thumb_media_id"] = "new-cover"
        self.assertEqual(portal.draft_group_key([old]), portal.draft_group_key([expected]))
        self.assertEqual(portal.article_prose_text(old["content"]), portal.article_prose_text(expected["content"]))
        with patch.object(portal, "batchget_recent_drafts", return_value=[{"media_id":"EXISTING", "content":{"news_item":[old]}}]):
            self.assertEqual("EXISTING", portal.find_recent_draft_by_titles(object(), "TOKEN", [expected["title"]], 30, expected_articles=[expected]))
        with patch.object(portal, "get_draft", side_effect=[{"news_item":[old]}, {"news_item":[expected]}]), patch.object(portal, "post_wechat_json", return_value=response({"errcode":0})) as post:
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [expected], True)
        self.assertTrue(result["ok"])
        self.assertEqual(1, post.call_count)
        self.assertIn("/draft/update?", post.call_args.args[1])
        self.assertEqual("EXISTING", post.call_args.args[2]["media_id"])
        self.assertEqual(0, post.call_args.args[2]["index"])

    def test_missing_changed_or_invalid_license_credit_cannot_pass_media_acceptance(self):
        expected = article()
        expected["content"] += self.commons_credit("Photographer", "Original")
        changed = copy.deepcopy(expected)
        changed["content"] = changed["content"].replace("File:Original", "File:Other")
        invalid = copy.deepcopy(expected)
        invalid["content"] = invalid["content"].replace("creativecommons.org", "untrusted.example")
        for actual in (article(), changed, invalid):
            with self.subTest(content=actual["content"]):
                checks = portal.wechat_media_contract_check(actual, expected)
                self.assertTrue(checks["matches_inline_images"])
                self.assertFalse(checks["matches_image_credits"])
                self.assertFalse(checks["matches"])

    def test_noncredit_prose_and_fake_marked_paragraph_stay_in_identity(self):
        expected = article()
        expected["content"] += self.commons_credit("First", "First")
        old = article()
        old["content"] += self.commons_credit("Second", "Second") + '<p class="image-credit" data-editorial-credit="1">人工补写的重要正文。</p>'
        self.assertNotEqual(portal.draft_group_key([old]), portal.draft_group_key([expected]))
        with patch.object(portal, "get_draft", return_value={"news_item":[old]}), patch.object(portal, "post_wechat_json") as post, patch.object(portal, "sleep_before_wechat_retry"):
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [expected], True)
        self.assertFalse(result["ok"])
        post.assert_not_called()

    def test_legacy_credit_key_recovers_saved_id_and_split_prefix_without_duplicate_creation(self):
        old = article()
        old["content"] += self.commons_credit("First", "First")
        expected = article()
        expected["content"] += self.commons_credit("Second", "Second")
        identity = [{"title":old["title"], "author":old["author"], "text":portal.visible_wechat_content_text(old["content"])}]
        old_key = hashlib.sha256(json.dumps(identity, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
        self.assertNotEqual(old_key, portal.draft_group_key([expected]))
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            portal.write_json(root / "draft_payload_01.json", {"articles":[old]})
            portal.write_json(root / "wechat_draft_summary.json", {"dry_run":False, "drafts":[{
                "media_id":"EXISTING_CHILD", "group_key":old_key, "payload":"/old/runner/draft_payload_01.json",
            }]})
            self.assertEqual("EXISTING_CHILD", portal.saved_draft_receipt(root, [expected])["media_id"])
            self.assertEqual(1, portal.saved_draft_prefix_length(root, [expected, dict(expected, title="另一篇文章")]))

    def test_html_budget_cannot_silently_drop_all_body_images_and_leave_contact_card(self):
        oversized_image = "https://mmbiz.qpic.cn/" + "x" * 18000
        with self.assertRaisesRegex(RuntimeError, "exceeds limits"):
            portal.render_fitted_wechat_html(
                "# 行业数据更新\n\n报告记录了一个完整的数据变化。", "行业数据更新", portal.BRAND,
                {}, [{"url": oversized_image, "token": "source", "source": "mineru"}],
                "", portal.BOTTOM_DISCLAIMER, "https://mmbiz.qpic.cn/contact/0", "source.pdf",
                1200, 19500, 5000,
            )

    def test_missing_body_image_contact_only_and_wrong_cover_cannot_pass(self):
        expected = article()
        variants = []
        wrong_cover = copy.deepcopy(expected)
        wrong_cover["thumb_media_id"] = "contact-or-placeholder"
        variants.append(wrong_cover)
        missing_body = copy.deepcopy(expected)
        missing_body["content"] = missing_body["content"].replace('<img src="https://mmbiz.qpic.cn/mmbiz_jpg/body-image/0?wx_fmt=jpeg" alt="报告图表">', "")
        variants.append(missing_body)
        blank_source = copy.deepcopy(expected)
        blank_source["content"] = blank_source["content"].replace("https://mmbiz.qpic.cn/mmbiz_jpg/body-image/0?wx_fmt=jpeg", "")
        variants.append(blank_source)
        for actual in variants:
            with self.subTest(actual=actual):
                result = portal.summarize_draft_get_response({"news_item": [actual]}, 1, [expected])
                self.assertTrue(result["matches_editorial_contract"])
                self.assertFalse(result["ok"])
                self.assertFalse(result["matches_media_contract"])
        media = portal.wechat_media_contract_check(expected, expected)
        self.assertEqual(1, media["expected_body_image_count"])
        self.assertEqual(1, media["expected_trailing_image_count"])

    def test_wechat_http_resize_and_html_entities_remain_same_media(self):
        expected = article()
        actual = copy.deepcopy(expected)
        actual["content"] = actual["content"].replace("https://", "http://").replace("/0?wx_fmt=jpeg", "/640?wx_fmt=jpeg&amp;wxfrom=5")
        self.assertTrue(portal.wechat_media_contract_check(actual, expected)["matches"])

    def test_read_only_verify_never_updates_media(self):
        old = dict(article(), thumb_media_id="old")
        with patch.object(portal, "get_draft", return_value={"news_item": [old]}), patch.object(portal, "post_wechat_json") as post, patch.object(portal, "sleep_before_wechat_retry"):
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [article()])
        self.assertFalse(result["ok"])
        post.assert_not_called()

    def test_same_text_repair_updates_exact_index_then_requires_readback(self):
        expected = article()
        old = dict(expected, thumb_media_id="old")
        old["content"] = old["content"].replace("body-image", "lost-image")
        with patch.object(portal, "get_draft", side_effect=[{"news_item": [expected, old]}, {"news_item": [expected, expected]}]), patch.object(portal, "post_wechat_json", return_value=response({"errcode": 0})) as post:
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 2, [expected, expected], True)
        self.assertTrue(result["ok"])
        self.assertEqual([1], result["media_repaired_indices"])
        self.assertEqual(1, post.call_count)
        self.assertIn("/draft/update?", post.call_args.args[1])
        payload = post.call_args.args[2]
        self.assertEqual("EXISTING", payload["media_id"])
        self.assertEqual(1, payload["index"])
        self.assertEqual("good-cover", payload["articles"]["thumb_media_id"])

    def test_user_edited_prose_prevents_any_media_update(self):
        expected = article()
        old = dict(expected, thumb_media_id="old")
        old["content"] = old["content"].replace("完整且", "用户修改了正文，")
        with patch.object(portal, "get_draft", return_value={"news_item": [old]}), patch.object(portal, "post_wechat_json") as post, patch.object(portal, "sleep_before_wechat_retry"):
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [expected], True)
        self.assertFalse(result["ok"])
        post.assert_not_called()

    def test_ambiguous_update_is_read_back_without_repeating_write(self):
        expected = article()
        old = dict(expected, thumb_media_id="old")
        with patch.object(portal, "get_draft", side_effect=[{"news_item": [old]}, {"news_item": [expected]}]), patch.object(portal, "post_wechat_json", side_effect=portal.WeChatError("unknown update result")) as post, patch.object(portal, "sleep_before_wechat_retry"):
            result = portal.verify_draft_get(object(), "TOKEN", "EXISTING", 30, 1, [expected], True)
        self.assertTrue(result["ok"])
        self.assertEqual(1, post.call_count)


if __name__ == "__main__":
    unittest.main()
