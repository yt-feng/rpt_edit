"""Existing-draft image recovery must preserve prose, contact art, and identity."""
from __future__ import annotations
import copy
from contextlib import ExitStack
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

from PIL import Image, ImageDraw
import requests

import repair_wechat_draft_images as repair
import push_portal_translated_to_wechat_drafts as portal
from free_editorial_images import attribution_html


def photo(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    image = Image.new('RGB', (600, 400), (71, 112, 167))
    ImageDraw.Draw(image).ellipse((80, 80, 350, 350), fill=(80, 180, 112))
    image.save(path)
    return path


def article(*, broken=True):
    body = ''.join(portal.image_html(f'https://mmbiz.qpic.cn/{"bad" if broken and i == 0 else "good"}-{i}/0', '报告图表') for i in range(3))
    return {
        'title': '行业数据与企业运营更新', 'author': portal.AUTHOR, 'digest': '原始摘要',
        'content': f'<p>{portal.BRAND}</p><p>保持原始正文和全部来源。</p>{body}<p>{portal.BOTTOM_DISCLAIMER}</p><p>撰稿：Olivia</p><p>责编：KC</p><p>排版：胡桃</p>' + portal.image_html('https://mmbiz.qpic.cn/contact/0', 'KC桌面'),
        'thumb_media_id': 'old-cover' if broken else 'good-cover',
        'thumb_url': 'https://mmbiz.qpic.cn/bad-cover/0' if broken else 'https://mmbiz.qpic.cn/good-cover/0',
    }


def response(data):
    result = requests.Response()
    result.status_code = 200
    result._content = json.dumps(data).encode()
    return result


class ImageDownloadTests(unittest.TestCase):
    def test_untrusted_and_malformed_urls_make_no_request(self):
        session = Mock()
        with tempfile.TemporaryDirectory() as temporary:
            for url in ('https://evil.example/image', 'https://mmbiz.qpic.cn.evil.test/image', 'https://user:pass@mmbiz.qpic.cn/image', 'https://mmbiz.qpic.cn:invalid/image', 'file:///private/image', 'https://mmbiz.qpic.cn/image#fragment'):
                with self.subTest(url=url):
                    self.assertEqual('untrusted_image_url', repair.fetch_wechat_image(session, url, Path(temporary)/'image.jpg', 30))
        session.get.assert_not_called()

    def test_redirect_is_not_followed(self):
        downloaded = Mock(status_code=302, headers={'Location': 'https://evil.example/image'})
        downloaded.__enter__ = Mock(return_value=downloaded)
        downloaded.__exit__ = Mock(return_value=False)
        session = Mock()
        session.get.return_value = downloaded
        with tempfile.TemporaryDirectory() as temporary:
            result = repair.fetch_wechat_image(session, 'https://mmbiz.qpic.cn/image/0', Path(temporary)/'image.jpg', 30)
        self.assertEqual('image_http_302', result)
        self.assertFalse(session.get.call_args.kwargs['allow_redirects'])
        self.assertEqual(1, session.get.call_count)

    def test_stream_limit_enforced_without_content_length(self):
        downloaded = Mock(status_code=200, headers={})
        downloaded.__enter__ = Mock(return_value=downloaded)
        downloaded.__exit__ = Mock(return_value=False)
        downloaded.iter_content.return_value = [b'a' * 6, b'b' * 6]
        session = Mock()
        session.get.return_value = downloaded
        with tempfile.TemporaryDirectory() as temporary, patch.object(repair, 'MAX_IMAGE_BYTES', 10):
            result = repair.fetch_wechat_image(session, 'https://mmbiz.qpic.cn/image/0', Path(temporary)/'image.jpg', 30)
        self.assertEqual('oversized_image', result)


class ReplacementTests(unittest.TestCase):
    def test_credit_replacement_is_adjacent_atomic_and_never_nested_in_image_paragraph(self):
        first = attribution_html({'source': 'local_editorial'})
        second = attribution_html({'source': 'commons', 'author': 'New Author', 'license': 'CC BY 4.0',
                                   'source_url': 'https://commons.wikimedia.org/wiki/File:Test.jpg',
                                   'license_url': 'https://creativecommons.org/licenses/by/4.0/'})
        content = '<p>正文保持不变。</p>' + portal.image_html('https://mmbiz.qpic.cn/old/0') + first + first + '<p>尾部正文。</p>'
        updated = repair.replace_image(content, 'https://mmbiz.qpic.cn/old/0', 'https://mmbiz.qpic.cn/new/0', second)
        self.assertEqual(1, updated.count('data-editorial-credit="1"'))
        self.assertNotIn('Portal Suite 原创插画', updated)
        self.assertIn(' /></p><p class="image-credit"', updated)
        self.assertEqual(repair.prose_identity({'content': content}), repair.prose_identity({'content': updated}))

    def test_no_arbitrary_text_paragraph_is_rearranged(self):
        content = '<p>人工排列的正文 <img src="https://mmbiz.qpic.cn/old/0"> 后续内容</p>'
        with self.assertRaisesRegex(ValueError, 'unsupported text paragraph'):
            repair.replace_image(content, 'https://mmbiz.qpic.cn/old/0', 'https://mmbiz.qpic.cn/new/0', attribution_html({'source':'local_editorial'}))

    def test_normal_prose_cannot_be_removed_as_unmanaged_credit(self):
        before = {'title': '标题', 'content': '<p>原始正文。</p><p class="image-credit">人工写的备注。</p>'}
        changed = dict(before, content='<p>原始正文。</p>')
        self.assertNotEqual(repair.prose_identity(before), repair.prose_identity(changed))

    def test_body_misuse_of_contact_picture_does_not_replace_actual_trailing_contact(self):
        url = 'https://mmbiz.qpic.cn/contact/0'
        footer = portal.image_html(url, 'KC桌面')
        content = portal.image_html(url, '报告图表') + footer
        repaired = repair.replace_image(content, url, 'https://mmbiz.qpic.cn/new/0', attribution_html({'source':'local_editorial'}))
        self.assertTrue(repaired.endswith(footer))
        self.assertEqual(1, repaired.count('data-editorial-credit="1"'))


class ReceiptRecoveryTests(unittest.TestCase):
    def record(self, media_id, articles):
        return {'media_id':media_id, 'content':{'news_item':copy.deepcopy(articles)}}

    def test_complete_catalog_paginates_and_never_calls_mutating_endpoints(self):
        records = [self.record(f'current-{i}', [dict(article(broken=False), title=f'Public test title {i}')]) for i in range(23)]
        with patch.object(repair, 'post_wechat_json', side_effect=[response({'total_count':23,'item':records[:20]}), response({'total_count':23,'item':records[20:]})]) as post:
            actual = repair.read_complete_draft_catalog(object(), 'TOKEN', 30)
        self.assertEqual(records, actual)
        self.assertEqual([0,20], [call.args[2]['offset'] for call in post.call_args_list])
        self.assertTrue(all('/draft/batchget?' in call.args[1] and call.args[2]['no_content']==0 for call in post.call_args_list))

    def test_incomplete_or_mutating_catalog_cannot_establish_uniqueness(self):
        record = self.record('public-id', [article(broken=False)])
        cases = [
            [response({'total_count':1001,'item':[record]})],
            [response({'total_count':2,'item':[record]}), response({'total_count':2,'item':[]})],
            [response({'total_count':2,'item':[record]}), response({'total_count':1,'item':[record]})],
            [response({'total_count':2,'item':[record]}), response({'total_count':2,'item':[record]})],
            [response({'total_count':1,'item':[{'media_id':'public-id','content':{'news_item':[article(), 'bad-row']}}]})],
        ]
        for pages in cases:
            with self.subTest(page_count=len(pages)), patch.object(repair,'post_wechat_json',side_effect=pages), self.assertRaises(repair.DraftCatalogError):
                repair.read_complete_draft_catalog(object(), 'TOKEN', 30)

    def test_exact_group_requires_body_author_order_and_source_url_and_unique_id(self):
        expected = [dict(article(broken=False), content_source_url='https://example.invalid/report-a'),
                    dict(article(broken=False), title='Second report', content_source_url='https://example.invalid/report-b')]
        variants = []
        for key, value in [('title','Different'),('author','Other author'),('content','<p>Different body</p>'),('content_source_url','https://example.invalid/other')]:
            changed = copy.deepcopy(expected); changed[0][key]=value; variants.append(changed)
        variants.append(list(reversed(expected)))
        for actual in variants:
            with self.subTest(first_title=actual[0]['title']):
                self.assertFalse(repair.strict_draft_group_match(actual,expected))
        candidate = self.record('new-exact-id',expected)
        self.assertEqual('unique_exact_group_match',repair.resolve_unique_receipt_candidate([candidate],expected,set())[1])
        self.assertEqual('invalid_receipt_ambiguous_match',repair.resolve_unique_receipt_candidate([candidate,self.record('another-id',expected)],expected,set())[1])
        self.assertEqual('invalid_receipt_target_already_bound',repair.resolve_unique_receipt_candidate([candidate],expected,{'new-exact-id'})[1])

    def execute(self, root, drafts, *, candidate=None, error_code=40007, candidate_changes=False, apply=False):
        def get(_session, _token, media_id, _timeout):
            if media_id == 'expired-id':
                raise portal.WeChatError('public fixture error',errcode=error_code)
            if media_id == 'recovered-id':
                rows = copy.deepcopy(candidate)
                if candidate_changes:rows[0]['content'] += '<p>Edited during lookup</p>'
                return {'news_item':rows}
            return {'news_item':copy.deepcopy(drafts[-1]['articles'])}
        with ExitStack() as stack:
            get_mock=stack.enter_context(patch.object(repair,'get_draft',side_effect=get))
            catalog=stack.enter_context(patch.object(repair,'read_complete_draft_catalog',return_value=[] if candidate is None else [self.record('recovered-id',candidate)]))
            fetch=stack.enter_context(patch.object(repair,'fetch_wechat_image',return_value=''))
            provider=stack.enter_context(patch.object(repair,'download_editorial_image'))
            uploads=stack.enter_context(patch.object(repair,'upload_article_image'))
            mutations=stack.enter_context(patch.object(repair,'post_wechat_json'))
            verification=stack.enter_context(patch.object(repair,'verify_draft_get',return_value={'ok':True}))
            build=stack.enter_context(patch.object(repair,'build_media_repair',side_effect=lambda _s,_t,a,*args: (copy.deepcopy(a),{'cover_replaced':False,'body_replacements':[],'body_added':0,'sources':[]})))
            result=repair.repair_drafts(drafts,object(),'TOKEN',root,30,apply)
            for operation in (provider,uploads,mutations):operation.assert_not_called()
        return result,get_mock,catalog,fetch,build,verification

    def test_invalid_first_id_does_not_block_later_valid_group_and_reports_partial(self):
        rows=[article(broken=False)]
        drafts=[{'media_id':'expired-id','articles':rows},{'media_id':'valid-id','articles':[dict(rows[0],title='Later source')]}]
        for apply in (False,True):
            with self.subTest(apply=apply), tempfile.TemporaryDirectory() as temporary:
                result,*_=self.execute(Path(temporary),drafts,apply=apply)
            self.assertEqual(1,result['article_count'])
            self.assertEqual(1,result['unresolved_draft_count'])
            self.assertEqual(1,result['unresolved_article_count'])
            self.assertEqual(2,result['expected_article_count'])
            self.assertTrue(result['partial']);self.assertFalse(result['ok']);self.assertFalse(result['fully_repaired'])
            self.assertEqual([1,2],[d['index'] for d in result['drafts']])
            self.assertNotIn('expired-id',json.dumps(result));self.assertNotIn('valid-id',json.dumps(result))

    def test_unique_exact_candidate_is_freshly_confirmed_and_reused_without_add(self):
        rows=[article(broken=False)]
        with tempfile.TemporaryDirectory() as temporary:
            result,get,catalog,fetch,build,verification=self.execute(Path(temporary),[{'media_id':'expired-id','articles':rows}],candidate=rows,apply=True)
        self.assertEqual(['expired-id','recovered-id'],[c.args[2] for c in get.call_args_list])
        self.assertEqual('recovered-id',verification.call_args.args[2])
        self.assertEqual(1,result['recovered_receipt_groups'])
        self.assertTrue(result['ok']);self.assertTrue(result['fully_repaired']);self.assertFalse(result['partial'])
        catalog.assert_called_once();build.assert_called_once()

    def test_candidate_changed_on_fresh_get_remains_unresolved_without_media_calls(self):
        rows=[article(broken=False)]
        with tempfile.TemporaryDirectory() as temporary:
            result,get,catalog,fetch,build,verification=self.execute(Path(temporary),[{'media_id':'expired-id','articles':rows}],candidate=rows,candidate_changes=True,apply=True)
        self.assertEqual('matched_candidate_changed_before_use',result['drafts'][0]['resolution'])
        self.assertEqual(0,result['article_count']);self.assertTrue(result['partial'])
        fetch.assert_not_called();build.assert_not_called();verification.assert_not_called()

    def test_other_wechat_errors_do_not_trigger_catalog_rebinding(self):
        rows=[article(broken=False)]
        with tempfile.TemporaryDirectory() as temporary, patch.object(repair,'read_complete_draft_catalog') as catalog, patch.object(repair,'get_draft',side_effect=portal.WeChatError('auth fixture',errcode=40014)):
            with self.assertRaises(portal.WeChatError):
                repair.repair_drafts([{'media_id':'expired-id','articles':rows}],object(),'TOKEN',Path(temporary),30,False)
            catalog.assert_not_called()

    def test_recovered_group_update_targets_only_freshly_confirmed_id_and_index(self):
        rows=[article(broken=False)]
        state={'news_item':copy.deepcopy(rows)}
        def get(_session,_token,media_id,_timeout):
            if media_id=='expired-id':raise portal.WeChatError('invalid fixture',errcode=40007)
            self.assertEqual('recovered-id',media_id)
            return copy.deepcopy(state)
        def build(_session,_token,current,*_args):
            fixed=dict(current,thumb_media_id='new-thumb')
            return fixed,{'cover_replaced':True,'body_replacements':[],'body_added':0,'sources':[]}
        def update(_session,url,payload,_timeout,**_kwargs):
            self.assertIn('/draft/update?',url)
            self.assertEqual('recovered-id',payload['media_id']);self.assertEqual(0,payload['index'])
            self.assertEqual('new-thumb',payload['articles']['thumb_media_id'])
            state['news_item'][0].update(payload['articles'])
            return response({'errcode':0})
        with tempfile.TemporaryDirectory() as temporary, patch.object(repair,'get_draft',side_effect=get) as gets, \
                patch.object(repair,'read_complete_draft_catalog',return_value=[self.record('recovered-id',rows)]), \
                patch.object(repair,'build_media_repair',side_effect=build), \
                patch.object(repair,'post_wechat_json',side_effect=update) as writes, \
                patch.object(repair,'verify_draft_get',return_value={'ok':True}) as verify:
            result=repair.repair_drafts([{'media_id':'expired-id','articles':rows}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(['expired-id','recovered-id','recovered-id'],[call.args[2] for call in gets.call_args_list])
        writes.assert_called_once();self.assertEqual('recovered-id',verify.call_args.args[2])
        self.assertTrue(result['fully_repaired']);self.assertEqual(1,result['recovered_receipt_groups'])


class DraftRepairTests(unittest.TestCase):
    def environment(self, stack, articles, *, verification=True):
        state = {'news_item': copy.deepcopy(articles)}
        stack.enter_context(patch.dict('os.environ', {'PORTAL_SITE_URL':'https://private.example.invalid'}))
        stack.enter_context(patch.object(repair, 'get_draft', side_effect=lambda *_args: copy.deepcopy(state)))

        def fetch(_session, url, path, _timeout):
            photo(path)
            return 'legacy_placeholder' if '/bad' in url else ''

        download = stack.enter_context(patch.object(repair, 'fetch_wechat_image', side_effect=fetch))
        provider = stack.enter_context(patch.object(repair, 'download_editorial_image', side_effect=lambda _session, _title, target, *_args, **_kwargs: (photo(target), {'source':'local_editorial'})))
        upload = stack.enter_context(patch.object(repair, 'upload_article_image', return_value='https://mmbiz.qpic.cn/replacement/0'))
        cover = stack.enter_context(patch.object(repair, 'upload_cover_material', return_value='replacement-cover'))

        def update(_session, url, payload, _timeout, **_kwargs):
            self.assertIn('/draft/update?', url)
            self.assertNotIn('/draft/add', url)
            self.assertNotIn('/draft/delete', url)
            self.assertNotIn('/freepublish/', url)
            self.assertEqual('existing-exact-id', payload['media_id'])
            state['news_item'][payload['index']].update(payload['articles'])
            state['news_item'][payload['index']]['thumb_url'] = 'https://mmbiz.qpic.cn/good-replacement-cover/0'
            return response({'errcode':0})

        post = stack.enter_context(patch.object(repair, 'post_wechat_json', side_effect=update))

        def verify(_session, _token, media_id, _timeout, count, expected, *args):
            self.assertEqual('existing-exact-id', media_id)
            self.assertEqual([], list(args))  # Explicit read-only verification.
            result = portal.summarize_draft_get_response(copy.deepcopy(state), count, expected)
            if not verification: result['ok'] = False
            return result

        stack.enter_context(patch.object(repair, 'verify_draft_get', side_effect=verify))
        return state, download, provider, upload, cover, post

    def test_same_receipt_repairs_existing_index_preserves_contact_and_second_run_is_noop(self):
        original = [article(broken=False), article()]
        receipt = [{'media_id':'existing-exact-id', 'articles':copy.deepcopy(original)}]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            state, _download, provider, upload, cover, post = self.environment(stack, original)
            result = repair.repair_drafts(receipt, object(), 'TOKEN', Path(temporary), 30, True)
            self.assertTrue(result['ok'])
            self.assertEqual(1, result['changed_articles'])
            self.assertEqual(1, post.call_count)
            self.assertEqual(1, post.call_args.args[2]['index'])
            self.assertEqual(1, provider.call_count)
            self.assertEqual(3, len(repair.article_body_images(state['news_item'][1]['content'])))
            self.assertEqual(portal.image_html('https://mmbiz.qpic.cn/contact/0', 'KC桌面'), state['news_item'][1]['content'][-len(portal.image_html('https://mmbiz.qpic.cn/contact/0', 'KC桌面')):])
            self.assertEqual(repair.prose_identity(original[1]), repair.prose_identity(state['news_item'][1]))
            post.reset_mock(); provider.reset_mock(); upload.reset_mock(); cover.reset_mock()
            again = repair.repair_drafts(receipt, object(), 'TOKEN', Path(temporary), 30, True)
            self.assertEqual(0, again['changed_articles'])
            for operation in (post, provider, upload, cover): operation.assert_not_called()

    def test_audit_has_no_provider_upload_or_update_calls(self):
        original = [article()]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, _download, provider, upload, cover, post = self.environment(stack, original)
            result = repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, False)
            self.assertTrue(result['ok'])
            self.assertFalse(result['applied'])
            self.assertEqual(1, result['changed_articles'])
            for operation in (post, provider, upload, cover): operation.assert_not_called()

    def test_contact_only_article_gains_three_body_images_with_contact_unchanged(self):
        original = [article()]
        for url, alt in portal.wechat_content_images(original[0]['content']):
            if alt != 'KC桌面':
                original[0]['content'] = original[0]['content'].replace(portal.image_html(url, alt), '')
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            state, _download, provider, _upload, _cover, post = self.environment(stack, original)
            result = repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertEqual(3, result['body_added'])
            self.assertEqual(3, provider.call_count)
            self.assertEqual(1, post.call_count)
            images = portal.wechat_content_images(state['news_item'][0]['content'])
            self.assertEqual(4, len(images))
            self.assertEqual(('https://mmbiz.qpic.cn/contact/0', 'KC桌面'), images[-1])
            self.assertEqual(repair.prose_identity(original[0]), repair.prose_identity(state['news_item'][0]))

    def test_repeated_legacy_image_is_replaced_once_and_does_not_satisfy_three_image_floor(self):
        original = [article()]
        original[0]['content'] = original[0]['content'].replace('/good-1/0', '/bad-0/640?wx_fmt=jpeg').replace('/good-2/0', '/bad-0/1080')
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            state, _download, _provider, upload, _cover, post = self.environment(stack, original)
            upload.side_effect = [f'https://mmbiz.qpic.cn/replacement-{i}/0' for i in range(3)]
            result = repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertEqual(1, result['body_replacements'])
            self.assertEqual(2, result['body_added'])
            self.assertEqual(3, len(repair.article_body_images(state['news_item'][0]['content'])))
            self.assertEqual(1, post.call_count)

    def test_edit_during_preparation_is_rechecked_before_update(self):
        original = [article()]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            state, _download, provider, _upload, cover, post = self.environment(stack, original)
            def cover_with_user_edit(*_args, **_kwargs):
                state['news_item'][0]['content'] += '<p>准备图片期间用户的修改。</p>'
                return 'replacement-cover'
            cover.side_effect = cover_with_user_edit
            with self.assertRaisesRegex(ValueError, 'changed during image preparation'):
                repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            post.assert_not_called()

    def test_title_card_cover_uses_retained_body_chart_before_credited_stock(self):
        original = article(broken=False)
        first_url = repair.article_body_images(original['content'])[0][0]
        original['content'] = repair.replace_image(original['content'], first_url, first_url, attribution_html({'source':'local_editorial'}))
        second_url = repair.article_body_images(original['content'])[1][0]
        original['content'] = original['content'].replace(portal.image_html(second_url, '报告图表'), portal.image_html(second_url, 'assets/source_image_02.png'))
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, download, provider, upload, cover, _post = self.environment(stack, [original])
            def inspect(_session, url, path, _timeout):
                photo(path)
                return 'generated_pdf_title_card' if 'cover' in url else ''
            download.side_effect = inspect
            prepare = stack.enter_context(patch.object(repair, 'prepare_cover_upload_image', side_effect=lambda path, *_args: path))
            result, facts = repair.build_media_repair(object(), 'TOKEN', original, Path(temporary), 30)
            self.assertTrue(facts['cover_replaced'])
            self.assertEqual('generated_pdf_title_card', facts['cover_reason'])
            self.assertEqual('retained_source_reference', facts['cover_source'])
            self.assertEqual('body_02.jpg', prepare.call_args.args[0].name)
            self.assertEqual(original['content'], result['content'])
            provider.assert_not_called(); upload.assert_not_called()

    def test_uncredited_legacy_photo_is_preserved_without_claiming_original_chart(self):
        original = article(broken=False)
        first_url = repair.article_body_images(original['content'])[0][0]
        original['content'] = original['content'].replace(portal.image_html(first_url, '报告图表'), portal.image_html(first_url, '研报原图 1'))
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, download, provider, upload, _cover, _post = self.environment(stack, [original])
            def inspect(_session, url, path, _timeout):
                photo(path)
                return 'generated_pdf_title_card' if 'cover' in url else ''
            download.side_effect = inspect
            result, facts = repair.build_media_repair(object(), 'TOKEN', original, Path(temporary), 30)
            self.assertEqual('retained_body_image', facts['cover_source'])
            self.assertEqual(original['content'], result['content'])
            self.assertFalse(repair.has_source_image_reference('研报原图 1'))
            self.assertFalse(repair.has_source_image_reference('主题配图'))
            self.assertFalse(repair.has_source_image_reference('assets/xhs_card_02.png'))
            provider.assert_not_called(); upload.assert_not_called()

    def test_known_source_reference_avoids_stock_replacement_for_rejected_extra(self):
        original = article()
        second_url = repair.article_body_images(original['content'])[1][0]
        original['content'] = original['content'].replace(portal.image_html(second_url, '报告图表'), portal.image_html(second_url, 'assets/source_image_02.png'))
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, _download, provider, upload, _cover, _post = self.environment(stack, [original])
            result, facts = repair.build_media_repair(object(), 'TOKEN', original, Path(temporary), 30)
            self.assertEqual(1, len(facts['body_replacements']))
            self.assertEqual('remove_invalid_image', facts['body_replacements'][0]['action'])
            self.assertEqual(2, len(repair.article_body_images(result['content'])))
            self.assertEqual('retained_source_reference', facts['cover_source'])
            provider.assert_not_called(); upload.assert_not_called()

    def test_receipt_body_mismatch_prevents_all_media_processing(self):
        original = [article()]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            state, download, provider, upload, cover, post = self.environment(stack, original)
            state['news_item'][0]['content'] += '<p>用户额外写的正文。</p>'
            with self.assertRaisesRegex(ValueError, 'prose differs'):
                repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            for operation in (download, provider, upload, cover, post): operation.assert_not_called()

    def test_failed_readback_cannot_report_success(self):
        original = [article()]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, _download, _provider, _upload, _cover, post = self.environment(stack, original, verification=False)
            with self.assertRaisesRegex(ValueError, 'readback failed'):
                repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertEqual(1, post.call_count)


if __name__ == '__main__': unittest.main()
