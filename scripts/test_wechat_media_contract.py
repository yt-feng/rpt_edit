"""Image-specific regressions: publication furniture, crops, and draft readback."""
from __future__ import annotations

import copy
import hashlib
import json
from pathlib import Path
import re
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

from PIL import Image, ImageDraw, ImageOps
import requests

import push_portal_translated_to_wechat_drafts as portal
import push_xhs_notes_to_wechat_drafts as xhs
from wechat_image_quality import article_image_rejection, is_article_image_candidate, source_chart_images, REPO_ROOT
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
    def test_actual_title_card_renderer_rejected_after_rename_crop_and_cdn_resize(self):
        import fitz
        from pdf_to_xhs_batch import make_cover
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            pdf = fitz.open(); page = pdf.new_page()
            page.insert_text((60, 60), 'Original report title page', fontsize=22)
            page.draw_rect((40, 180, 350, 450), color=(.1, .3, .6), fill=(.8, .9, .95))
            pdf.save(root / 'fixture.pdf'); pdf.close()
            cover = root / 'renamed.png'
            make_cover(root / 'fixture.pdf', cover, '0001-01-Fixture', 'Research notes', 'Fixture')
            self.assertEqual('generated_pdf_title_card', article_image_rejection(cover))
            for size in ((1200, 675), (940, 400), (640, 360), (320, 180)):
                with self.subTest(size=size), Image.open(cover) as original:
                    path = root / f'cdn-{size[0]}.jpg'
                    ImageOps.fit(original, size, method=Image.Resampling.LANCZOS).save(path, quality=82)
                    self.assertEqual('generated_pdf_title_card', article_image_rejection(path))
            chart = image(root / 'sparse-chart.jpg')
            self.assertEqual('', article_image_rejection(chart))
            # White chart panels are common; a generic framed chart must stay.
            framed = Image.new('RGB', (1200, 675), (210, 220, 230))
            draw = ImageDraw.Draw(framed)
            draw.rectangle((60, 70, 1140, 620), fill='white', outline='black', width=2)
            draw.line((100, 540, 400, 300, 1000, 150), fill='blue', width=5)
            framed.save(root / 'framed-chart.jpg')
            self.assertEqual('', article_image_rejection(root / 'framed-chart.jpg'))

    def test_source_map_excludes_stale_art_and_cover_prefers_retained_original(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            chart = image(root / 'assets/source_image_02.png')
            image(root / 'assets/source_image_01.jpg', (210, 40, 90))
            image(root / 'assets/cover.png')
            source = root / 'source_mineru.md'; source.write_text('Bound source fixture.')
            mapping = {'version':1, 'source_sha256':hashlib.sha256(source.read_bytes()).hexdigest(),
                       'images':{'images/original.png':'assets/source_image_02.png'}}
            (root / 'source_image_map.json').write_text(json.dumps(mapping))
            self.assertEqual([chart], source_chart_images(root))
            stock = image(root / 'stock.jpg')
            self.assertEqual(chart, xhs.choose_cover_image(root, [stock], root / 'fallback'))
            self.assertEqual(chart, portal.choose_cover_image(root, {}, root / 'fallback', [stock]))
            source.write_text('Changed source.')
            self.assertEqual([], source_chart_images(root))

    def test_both_real_builders_use_one_original_without_padding_with_stock(self):
        for uploader, markdown_name, status_name in ((xhs, 'wechat_article.md', 'status.json'),
                                                    (portal, 'translated.md', 'translation_status.json')):
            with self.subTest(uploader=uploader.__name__), tempfile.TemporaryDirectory() as temporary:
                root = Path(temporary); report = root / 'report'; report.mkdir()
                chart = image(report / 'assets/source_image_01.png')
                image(report / 'assets/cover.png', (190, 20, 30))
                (report / markdown_name).write_text('# 高盛：企业订单与交付周期更新\n\n完整的报告正文记录了企业订单与交付周期的变化。')
                (report / status_name).write_text(json.dumps({'source_pdf':'GS-orders.pdf', 'title':'高盛：企业订单与交付周期更新'}))
                if uploader is portal:
                    (report / 'figure_manifest.json').write_text(json.dumps([{'token':'[[PORTAL_IMAGE_001]]', 'relative_path':'assets/source_image_01.png'}]))
                args = SimpleNamespace(author=portal.AUTHOR, brand=portal.BRAND, body_hook='', content_source_url='', disclaimer=portal.BOTTOM_DISCLAIMER,
                                       dry_run=True, image_upload_delay_seconds=0, max_body_chars=1200, max_content_bytes=18000,
                                       max_content_chars=19500, max_inline_images=6, min_inline_images=3, timeout=30)
                with patch.object(uploader, 'download_pollinations_image') as provider:
                    built = uploader.build_article(report, 1, args, None, None, root / 'out', '')
                provider.assert_not_called()
                self.assertEqual(1, len(built['inline_images']))
                self.assertEqual(str(chart), built['inline_images'][0]['path'])
                self.assertEqual(1, built['body_image_count'])
                self.assertNotIn('主题配图', built['article']['content'])

    def test_source_provenance_excludes_toc_and_generated_page_even_when_renamed(self):
        with tempfile.TemporaryDirectory() as temporary:
            root = Path(temporary)
            chart = image(root / 'assets/source_image_01.png')
            toc = image(root / 'assets/source_image_02.png', (180, 50, 40))
            sidecar = {'metadata':{'records':[{'index':1, 'kind':'chart'}, {'index':2, 'body_text':'Table of Contents'}]},
                       'assets':[{'index':i, 'path':p.relative_to(root).as_posix(), 'sha256':hashlib.sha256(p.read_bytes()).hexdigest()} for i,p in enumerate((chart,toc),1)]}
            (root / 'source_figure_map.json').write_text(json.dumps(sidecar))
            self.assertEqual([chart], source_chart_images(root))
            (root / 'figure_manifest.json').write_text(json.dumps([
                {'token':'good', 'relative_path':'assets/source_image_01.png'},
                {'token':'toc', 'relative_path':'assets/source_image_02.png', 'role':'table_of_contents'},
                {'token':'renamed-title', 'relative_path':'assets/source_image_02.png', 'source_path':'/old/report/assets/cover.png'},
            ]))
            self.assertEqual({'good':chart}, portal.load_figure_paths(root))

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

    def legacy_credit(self, author="Photographer", filename="Original", version="4.0"):
        # Pin the original deployed format; the provider now renders visible
        # URLs because WeChat stripped these external anchors in real readback.
        return ('<p class="image-credit" data-editorial-credit="1">'
                f'主题配图：{author} / Wikimedia Commons / CC BY {version}；已裁剪与缩放，非报告原图。 '
                f'<a href="https://commons.wikimedia.org/wiki/File:{filename}.jpg">图片来源</a> · '
                f'<a href="https://creativecommons.org/licenses/by/{version}/">许可</a></p>')

    def test_visible_attribution_urls_survive_anchor_removal_and_whitespace(self):
        credit = self.commons_credit("Photographer", "Original")
        self.assertNotIn('<a ', credit)
        self.assertIn('图片来源：https://commons.wikimedia.org/wiki/File:Original.jpg', credit)
        self.assertIn('许可：https://creativecommons.org/licenses/by/4.0/', credit)
        original_signature = portal.generated_image_credit_signature(self.legacy_credit())
        self.assertEqual(original_signature, portal.generated_image_credit_signature(credit))
        linked = re.sub(r'https://[^\s<]+', lambda match: f'<a href="{match.group()}">{match.group()}</a>', credit)
        stripped = re.sub(r'</?a\b[^>]*>', '', linked).replace(' · ', '\n  ·\t')
        for returned in (credit, linked, stripped):
            with self.subTest(returned=returned):
                self.assertEqual(original_signature, portal.generated_image_credit_signature(returned))
                expected = dict(article(), content=article()['content'] + credit)
                actual = dict(expected, content=article()['content'] + returned)
                self.assertEqual(portal.article_prose_text(expected['content']), portal.article_prose_text(actual['content']))
                self.assertTrue(portal.wechat_media_contract_check(actual, expected)['matches'])

    def test_real_link_stripped_legacy_shapes_are_prose_only_never_media_accepted(self):
        credits = [re.sub(r'</?a\b[^>]*>', '', self.legacy_credit(f'Author {index}', f'Photo{index}', version))
                   for index, version in enumerate(('3.0', '3.0', '2.0'), 1)]
        local = attribution_html({'source': 'local_editorial'})
        for rows in (credits, credits[:2] + [local]):
            with self.subTest(count=len(rows)):
                actual = dict(article(), content=article()['content'] + ''.join(rows))
                self.assertEqual(portal.article_prose_text(article()['content']), portal.article_prose_text(actual['content']))
                self.assertTrue(all(portal.legacy_stripped_commons_credit(row) for row in rows if row != local))
                for expected in (None, actual, article()):
                    checks = portal.wechat_media_contract_check(actual, expected)
                    self.assertFalse(checks['matches'])
                    self.assertFalse(checks['matches_image_credits'])
                    self.assertEqual(3 if rows == credits else 2, checks['incomplete_image_credit_count'])

    def test_legacy_prose_exception_rejects_missing_markers_unknown_license_and_extra_text(self):
        legacy = re.sub(r'</?a\b[^>]*>', '', self.legacy_credit())
        for malformed in (
            legacy.replace('data-editorial-credit="1"', ''),
            legacy.replace('class="image-credit"', ''),
            legacy.replace('CC BY 4.0', 'CC BY-NC 4.0'),
            legacy.replace('</p>', ' Important manual note.</p>'),
            legacy.replace('图片来源 · 许可', '图片来源'),
            legacy.replace('图片来源', '<span>图片来源</span>'),
            legacy.replace('</p>', '<!-- extra --></p>'),
            self.legacy_credit().replace(' href=', ' data-href='),
        ):
            with self.subTest(malformed=malformed):
                self.assertFalse(portal.legacy_stripped_commons_credit(malformed))
                self.assertIn('主题配图', portal.article_prose_text(malformed))
                self.assertIsNone(portal.generated_image_credit_signature(malformed))
        changed_body = article()['content'].replace('不应被图片修复改变', 'changed') + legacy
        self.assertNotEqual(portal.article_prose_text(article()['content']), portal.article_prose_text(changed_body))

    def test_visible_source_and_license_uri_binding_remains_strict(self):
        credit = self.commons_credit('Photographer', 'Original')
        for bad in (
            credit.replace('https://commons.', 'http://commons.'),
            credit.replace('commons.wikimedia.org', 'untrusted.invalid'),
            credit.replace('/wiki/File:', '/wiki/Category:'),
            credit.replace('File:Original.jpg', 'File:'),
            credit.replace('Original.jpg', 'Original.jpg?tracking=1'),
            credit.replace('Original.jpg', 'Original.jpg#fragment'),
            credit.replace('creativecommons.org', 'untrusted.invalid'),
            credit.replace('/licenses/by/4.0/', '/licenses/by/3.0/'),
            credit.replace('CC BY 4.0', 'CC BY-SA 4.0'),
            credit.replace('图片来源：https', '图片来源：<a href="https://wrong.invalid">https').replace('jpg ·', 'jpg</a> ·'),
        ):
            with self.subTest(bad=bad):
                self.assertIsNone(portal.generated_image_credit_signature(bad))
                self.assertFalse(portal.legacy_stripped_commons_credit(bad))
                self.assertIn('主题配图', portal.article_prose_text(bad))

    def test_auto_link_anchor_text_must_equal_its_own_destination(self):
        credit = self.commons_credit('Photographer', 'Original')
        source = 'https://commons.wikimedia.org/wiki/File:Original.jpg'
        license_url = 'https://creativecommons.org/licenses/by/4.0/'
        # The complete visible text and ordered href list are still correct,
        # but clicking the source URL would go to the license. Reject it.
        misleading = credit.replace('图片来源：' + source,
            f'<a href="{source}">图片来源：</a><a href="{license_url}">{source}</a>')
        self.assertEqual(portal._generated_image_credit_parts(credit)[0], portal._generated_image_credit_parts(misleading)[0])
        self.assertIsNone(portal.generated_image_credit_signature(misleading))
        self.assertFalse(portal.legacy_stripped_commons_credit(misleading))
        old = self.legacy_credit()
        misleading_old = old.replace(f'<a href="{source}">图片来源</a>',
            f'<a href="{source}"></a>图片来源').replace(f'<a href="{license_url}">许可</a>',
            f'<a href="{license_url}"></a>许可')
        self.assertIsNone(portal.generated_image_credit_signature(misleading_old))

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
