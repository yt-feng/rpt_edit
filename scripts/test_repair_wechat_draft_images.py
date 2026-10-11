"""Existing-draft image recovery must preserve prose, contact art, and identity."""
from __future__ import annotations
import copy
from contextlib import ExitStack, redirect_stdout
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


def stripped_commons_credit(license_name='CC BY 3.0'):
    return ('<p class="image-credit" data-editorial-credit="1">'
            f'主题配图：Synthetic Photographer / Wikimedia Commons / {license_name}'
            '；已裁剪与缩放，非报告原图。 图片来源 · 许可</p>')


def with_legacy_commons(saved, count=3):
    live = copy.deepcopy(saved)
    for index, (url, alt) in enumerate(repair.article_body_images(live['content'])):
        credit = (stripped_commons_credit(('CC BY 3.0','CC BY 3.0','CC BY 2.0')[index])
                  if index < count else attribution_html({'source':'local_editorial'}))
        image = portal.image_html(url, alt)
        live['content'] = live['content'].replace(image, image + credit)
    return live


class IncrementalMediaReadbackTests(unittest.TestCase):
    def baseline(self):
        return [dict(article(broken=False), title=f'Synthetic report {index}')
                if index == 0 else with_legacy_commons(dict(article(broken=False), title=f'Synthetic report {index}'), 1)
                for index in range(2)]

    def verify(self, actual, expected, processed_count=1):
        with patch.object(repair, 'get_draft', return_value={'news_item':copy.deepcopy(actual)}):
            checks, _returned = repair.verify_repair_readback(object(), 'TOKEN', 'existing-exact-id', 30,
                                                            expected, processed_count=processed_count)
        return checks

    def test_unchanged_future_legacy_is_deferred_without_claiming_full_group_media_acceptance(self):
        expected = self.baseline()
        checks = self.verify(expected, expected)
        self.assertTrue(checks['ok']);self.assertTrue(checks['matches_processed_media_contract'])
        self.assertFalse(checks['matches_media_contract']);self.assertEqual([1],checks['pending_legacy_media_indices'])
        final = self.verify(expected, expected, processed_count=2)
        self.assertFalse(final['ok']);self.assertFalse(final['matches_processed_media_contract'])
        self.assertEqual([],final['pending_legacy_media_indices'])

    def test_pending_member_identity_or_any_writable_change_is_rejected(self):
        expected = self.baseline()
        changes = {
            'title':lambda row:row.update(title='Edited title'),
            'author':lambda row:row.update(author='Edited author'),
            'prose':lambda row:row.update(content=row['content']+'<p>New user paragraph.</p>'),
            'source':lambda row:row.update(content_source_url='https://source.example/changed'),
            'digest':lambda row:row.update(digest='Edited summary'),
            'comments':lambda row:row.update(need_open_comment=1),
            'cover':lambda row:row.update(thumb_media_id='different-cover'),
            'inline':lambda row:row.update(content=row['content'].replace('/good-1/0','/different/0')),
            'legacy-author':lambda row:row.update(content=row['content'].replace('Synthetic Photographer','Other Photographer')),
            'legacy-license':lambda row:row.update(content=row['content'].replace('CC BY 3.0','CC BY 4.0')),
        }
        for name, change in changes.items():
            with self.subTest(field=name):
                actual = copy.deepcopy(expected);change(actual[1])
                checks = self.verify(actual, expected)
                self.assertFalse(checks['ok']);self.assertFalse(checks['matches_processed_media_contract'])

    def test_future_complete_credit_and_nonlegacy_media_changes_are_not_excused(self):
        expected = self.baseline()
        complete = attribution_html({'source':'wikimedia_commons','author':'Original Author','license':'CC BY 4.0',
                                     'source_url':'https://commons.wikimedia.org/wiki/File:Original.jpg',
                                     'license_url':'https://creativecommons.org/licenses/by/4.0/'})
        expected[1]['content'] += complete
        for before, after in (('Original Author','Changed Author'),('File:Original.jpg','File:Changed.jpg'),
                              ('CC BY 4.0','CC BY 3.0')):
            with self.subTest(change=before):
                actual=copy.deepcopy(expected);actual[1]['content']=actual[1]['content'].replace(before,after)
                checks=self.verify(actual,expected)
                self.assertFalse(checks['ok']);self.assertFalse(checks['matches_processed_media_contract'])
        expected[1]=article(broken=False)
        actual=copy.deepcopy(expected);actual[1]['content']=actual[1]['content'].replace('/good-1/0','/different/0')
        self.assertFalse(self.verify(actual,expected)['ok'])

    def test_current_and_already_processed_legacy_are_never_deferred(self):
        for legacy_index in (0,1):
            with self.subTest(legacy_index=legacy_index):
                expected=[article(broken=False) for _index in range(3)]
                expected[legacy_index]=with_legacy_commons(expected[legacy_index],1)
                checks=self.verify(expected,expected,processed_count=2)
                self.assertFalse(checks['ok']);self.assertFalse(checks['matches_processed_media_contract'])
        expected=self.baseline();expected[0]['content']+=attribution_html({'source':'local_editorial'})
        actual=copy.deepcopy(expected);actual[0]['content']=actual[0]['content'].replace(attribution_html({'source':'local_editorial'}),'')
        self.assertFalse(self.verify(actual,expected)['ok'])

    def test_invalid_processed_count_fails_closed_before_readback(self):
        expected=self.baseline()
        for count in (True,False,0,-1,3,1.0,'1'):
            with self.subTest(count=count), patch.object(repair,'get_draft') as get:
                with self.assertRaises(ValueError):
                    repair.verify_repair_readback(object(),'TOKEN','existing-exact-id',30,expected,processed_count=count)
                get.assert_not_called()


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
    def test_duplicate_image_renditions_replace_every_adjacent_legacy_credit_atomically(self):
        old='https://mmbiz.qpic.cn/old-commons/0';other='https://mmbiz.qpic.cn/old-commons/640'
        credit=stripped_commons_credit();new='https://mmbiz.qpic.cn/new-licensed/0'
        footer=portal.image_html('https://mmbiz.qpic.cn/contact/0','KC桌面')
        content='<p>Unchanged source prose.</p>'+portal.image_html(old)+credit+credit+'<p>Retained paragraph.</p>'+portal.image_html(other)+credit+footer
        replacement=attribution_html({'source':'local_editorial'})
        updated=repair.replace_image(content,old,new,replacement)
        self.assertEqual(2,updated.count('data-editorial-credit="1"'))
        self.assertNotIn('Synthetic Photographer',updated);self.assertNotIn('old-commons',updated)
        self.assertEqual(2,updated.count(new));self.assertTrue(updated.endswith(footer))
        self.assertEqual(repair.prose_identity({'content':content}),repair.prose_identity({'content':updated}))

    def test_unmarked_unknown_license_extra_text_and_nonadjacent_paragraphs_are_not_stripped(self):
        old='https://mmbiz.qpic.cn/old-commons/0';image=portal.image_html(old);credit=stripped_commons_credit()
        variants=[credit.replace(' data-editorial-credit="1"',''),credit.replace(' class="image-credit"',''),
                  credit.replace('CC BY 3.0','CC BY-NC 3.0'),credit.replace('</p>',' Additional body text.</p>')]
        for note in variants:
            with self.subTest(note_length=len(note)):
                content=image+note
                self.assertFalse(repair.has_incomplete_editorial_credit(content,old))
                updated=repair.replace_image(content,old,'https://mmbiz.qpic.cn/new/0',attribution_html({'source':'local_editorial'}))
                self.assertIn(note,updated)
        separated=image+'<p>Intervening user text.</p>'+credit
        self.assertFalse(repair.has_incomplete_editorial_credit(separated,old))
        self.assertIn(credit,repair.replace_image(separated,old,'https://mmbiz.qpic.cn/new/0',''))

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
            verification=stack.enter_context(patch.object(repair,'verify_repair_readback',side_effect=lambda _s,_t,_id,_timeout,expected,**_kwargs: ({'ok':True},copy.deepcopy(expected))))
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
                patch.object(repair,'verify_repair_readback',side_effect=lambda _s,_t,_id,_timeout,expected,**_kwargs: ({'ok':True},copy.deepcopy(expected))) as verify:
            result=repair.repair_drafts([{'media_id':'expired-id','articles':rows}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(['expired-id','recovered-id','recovered-id'],[call.args[2] for call in gets.call_args_list])
        writes.assert_called_once();self.assertEqual('recovered-id',verify.call_args.args[2])
        self.assertTrue(result['fully_repaired']);self.assertEqual(1,result['recovered_receipt_groups'])

    def test_each_identity_field_is_diagnosed_without_private_values_and_later_group_runs(self):
        base=dict(article(broken=False),content_source_url='https://private.example.invalid/exact-source')
        changes=[('title','private edited title'),
                 ('content','<p>private edited body</p>'),('content_source_url','https://private.example.invalid/edited-source')]
        drafts=[{'media_id':f'private-id-{i}','articles':[copy.deepcopy(base)]} for i in range(4)]
        returned={draft['media_id']:[copy.deepcopy(base)] for draft in drafts}
        for i,(field,value) in enumerate(changes):returned[drafts[i]['media_id']][0][field]=value
        log=io.StringIO()
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(log), \
                patch.object(repair,'get_draft',side_effect=lambda _s,_t,media_id,_timeout:{'news_item':returned[media_id]}), \
                patch.object(repair,'build_media_repair',side_effect=lambda _s,_t,a,*_args:(copy.deepcopy(a),{'cover_replaced':False,'body_replacements':[],'body_added':0,'sources':[]})) as build, \
                patch.object(repair,'verify_repair_readback',side_effect=lambda _s,_t,_id,_timeout,expected,**_kwargs: ({'ok':True},copy.deepcopy(expected))), patch.object(repair,'post_wechat_json') as write:
            result=repair.repair_drafts(drafts,object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(3,result['unresolved_draft_count']);self.assertEqual(1,result['article_count'])
        self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired']);self.assertEqual(0,result['updated_articles'])
        expected_fields=['title','prose','source_url']
        for row,field in zip(result['drafts'][:3],expected_fields):
            fields=row['identity_diagnostics']['articles'][0]
            self.assertFalse(fields['matches'][field]);self.assertEqual([field],list(fields['differences']))
            self.assertTrue(all(value for key,value in fields['matches'].items() if key!=field))
        serialized=json.dumps(result)+log.getvalue()
        for private_value in ['private-id-',base['title'],base['author'],base['content_source_url'],*[value for _,value in changes]]:
            self.assertNotIn(private_value,serialized)
        build.assert_called_once();write.assert_not_called()

    def test_response_only_urls_are_not_concurrency_lock_and_are_diagnosed_separately(self):
        first=article();second=dict(article(broken=False),title='Later unchanged group')
        calls={'first':0}
        def get(_s,_t,media_id,_timeout):
            if media_id=='second-id':return {'news_item':[copy.deepcopy(second)]}
            calls['first']+=1;row=copy.deepcopy(first)
            if calls['first']>1:
                row['thumb_url']='https://mmbiz.qpic.cn/private-server-rendition/0?wxfrom=5'
                row['url']='https://private.example.invalid/temporary-link'
                row['private-return-only-key']='private-return-only-value'
            return {'news_item':[row]}
        def build(_s,_t,a,*_args):
            return copy.deepcopy(a),{'cover_replaced':a['title']==first['title'],'body_replacements':[],'body_added':0,'sources':[]}
        log=io.StringIO()
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(log), patch.object(repair,'get_draft',side_effect=get), \
                patch.object(repair,'build_media_repair',side_effect=build), patch.object(repair,'verify_repair_readback',side_effect=lambda _s,_t,_id,_timeout,expected,**_kwargs: ({'ok':True},copy.deepcopy(expected))), \
                patch.object(repair,'post_wechat_json',return_value=response({'errcode':0})) as write:
            result=repair.repair_drafts([{'media_id':'first-id','articles':[first]},{'media_id':'second-id','articles':[second]}],object(),'TOKEN',Path(temporary),30,True)
        diagnostics=result['drafts'][0]['changed'][0]['response_only_field_changes']
        self.assertEqual(['thumb_url','url'],list(diagnostics['changed_fields']))
        self.assertTrue(all(not field['writable'] for field in diagnostics['changed_fields'].values()))
        self.assertEqual(1,diagnostics['unrecognized_changed_field_count'])
        self.assertEqual(0,result['unresolved_draft_count']);self.assertEqual(2,result['article_count'])
        self.assertEqual(1,result['updated_articles']);write.assert_called_once()
        self.assertTrue(result['fully_repaired'])
        self.assertNotIn('thumb_url',write.call_args.args[2]['articles'])
        self.assertNotIn('url',write.call_args.args[2]['articles'])
        self.assertNotIn('private-server-rendition',json.dumps(result)+log.getvalue())
        self.assertNotIn('private-return-only',json.dumps(result)+log.getvalue())

    def test_each_writable_field_change_skips_group_and_continues_without_overwrite(self):
        changes={'title':'Edited title','author':'Edited author','digest':'Edited digest','content':'<p>Edited body</p>',
                 'content_source_url':'https://example.invalid/edited','thumb_media_id':'changed-thumb',
                 'need_open_comment':1,'only_fans_can_comment':1}
        for field,value in changes.items():
            with self.subTest(field=field), tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
                first=article();second=dict(article(broken=False),title='Later unchanged group');calls={'first':0}
                def get(_s,_t,media_id,_timeout):
                    if media_id=='second-id':return {'news_item':[copy.deepcopy(second)]}
                    calls['first']+=1;row=copy.deepcopy(first)
                    if calls['first']>1:row[field]=value
                    return {'news_item':[row]}
                def build(_s,_t,a,*_args):
                    return copy.deepcopy(a),{'cover_replaced':a['title']==first['title'],'body_replacements':[],'body_added':0,'sources':[]}
                stack.enter_context(redirect_stdout(io.StringIO()))
                stack.enter_context(patch.object(repair,'get_draft',side_effect=get))
                stack.enter_context(patch.object(repair,'build_media_repair',side_effect=build))
                stack.enter_context(patch.object(repair,'verify_repair_readback',side_effect=lambda _s,_t,_id,_timeout,expected,**_kwargs: ({'ok':True},copy.deepcopy(expected))))
                write=stack.enter_context(patch.object(repair,'post_wechat_json'))
                result=repair.repair_drafts([{'media_id':'first-id','articles':[first]},{'media_id':'second-id','articles':[second]}],object(),'TOKEN',Path(temporary),30,True)
                self.assertEqual(1,result['unresolved_draft_count']);self.assertEqual(1,result['article_count'])
                self.assertEqual(0,result['updated_articles']);write.assert_not_called()
                diagnostics=result['drafts'][0]['identity_diagnostics']
                self.assertFalse(diagnostics['writable_group_unchanged'])
                self.assertTrue(diagnostics['target_returned_fields']['changed_fields'][field]['writable'])


class SavedReceiptAuthorTests(unittest.TestCase):
    def execute(self, mode='preserve'):
        receipt_rows=[dict(article(broken=False),content_source_url='https://example.invalid/source-a'),
                      dict(article(broken=False),title='Second exact source',content_source_url='https://example.invalid/source-b')]
        original=copy.deepcopy(receipt_rows)
        state={'news_item':[dict(row,author='Current user-selected author') for row in receipt_rows]}
        writes=[];built=[];log=io.StringIO()
        def get(_s,_t,media_id,_timeout):
            self.assertEqual('saved-live-id',media_id)
            return copy.deepcopy(state)
        def build(_s,_t,current,*_args):
            built.append(copy.deepcopy(current))
            if mode=='concurrent-author':state['news_item'][0]['author']='New intervening author'
            return dict(current,thumb_media_id=f'repaired-cover-{len(built)}'), {'cover_replaced':True,'body_replacements':[],'body_added':0,'sources':[]}
        def post(_s,url,payload,_timeout,**_kwargs):
            self.assertIn('/draft/update?',url)
            self.assertEqual('saved-live-id',payload['media_id'])
            writes.append(copy.deepcopy(payload))
            state['news_item'][payload['index']].update(payload['articles'])
            if mode=='readback-author':state['news_item'][payload['index']]['author']='Changed during readback'
            return response({'errcode':0})
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(log), \
                patch.object(repair,'get_draft',side_effect=get), patch.object(repair,'build_media_repair',side_effect=build), \
                patch.object(repair,'post_wechat_json',side_effect=post), patch.object(repair,'read_complete_draft_catalog') as catalog:
            result=repair.repair_drafts([{'media_id':'saved-live-id','articles':receipt_rows}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(original,receipt_rows)
        catalog.assert_not_called()
        self.assertNotIn('Current user-selected author',json.dumps(result)+log.getvalue())
        return result,state,writes,built

    def test_original_live_id_preserves_author_in_every_update_and_strict_readback(self):
        result,state,writes,built=self.execute()
        self.assertEqual(2,result['article_count']);self.assertEqual(2,result['updated_articles'])
        self.assertTrue(result['fully_repaired'])
        self.assertEqual('author_change_preserved',result['drafts'][0]['resolution'])
        self.assertEqual([0,1],[row['index'] for row in writes])
        self.assertTrue(all(row['articles']['author']=='Current user-selected author' for row in writes))
        self.assertTrue(all(row['author']=='Current user-selected author' for row in state['news_item']))

    def test_other_identity_fields_count_order_and_unchanged_authors_are_not_admitted(self):
        expected=[article(),dict(article(),title='Second unique source')]
        live=[dict(row,author='Current author') for row in expected]
        self.assertTrue(repair.saved_receipt_author_change_only(live,expected))
        self.assertFalse(repair.strict_draft_group_match(live,expected))
        self.assertFalse(repair.saved_receipt_author_change_only(expected,expected))
        variants=[live[:1],list(reversed(live)),[]]
        for key,value in [('title','Different title'),('content','<p>Edited prose</p>'),('content_source_url','https://example.invalid/other')]:
            changed=copy.deepcopy(live);changed[0][key]=value;variants.append(changed)
        for actual in variants:
            with self.subTest(count=len(actual)):
                self.assertFalse(repair.saved_receipt_author_change_only(actual,expected))

    def test_author_changes_never_expand_invalid_receipt_catalog_matching(self):
        expected=[article(broken=False)];live=[dict(expected[0],author='Current author')]
        catalog=[{'media_id':'different-current-id','content':{'news_item':live}}]
        self.assertEqual((None,'invalid_receipt_no_current_match'),repair.resolve_unique_receipt_candidate(catalog,expected,set()))
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
                patch.object(repair,'get_draft',side_effect=portal.WeChatError('Fixture invalid ID',errcode=40007)), \
                patch.object(repair,'read_complete_draft_catalog',return_value=catalog), \
                patch.object(repair,'build_media_repair') as build, patch.object(repair,'post_wechat_json') as write:
            result=repair.repair_drafts([{'media_id':'expired-saved-id','articles':expected}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual('invalid_receipt_no_current_match',result['drafts'][0]['resolution'])
        self.assertEqual(0,result['article_count']);build.assert_not_called();write.assert_not_called()

    def test_intervening_author_change_still_prevents_any_update(self):
        result,state,writes,built=self.execute('concurrent-author')
        self.assertEqual([],writes);self.assertEqual(0,result['updated_articles'])
        self.assertEqual(2,result['unresolved_article_count'])
        self.assertEqual('draft_changed_during_image_preparation',result['drafts'][0]['resolution'])
        self.assertEqual('New intervening author',state['news_item'][0]['author'])

    def test_readback_author_change_is_not_accepted_as_new_baseline(self):
        result,state,writes,built=self.execute('readback-author')
        self.assertEqual(1,len(writes));self.assertEqual(1,result['updated_articles'])
        self.assertEqual(0,result['article_count']);self.assertEqual(1,result['uncertain_article_count'])
        self.assertEqual(2,result['unresolved_article_count'])
        self.assertEqual('draft_image_readback_failed',result['drafts'][0]['resolution'])
        self.assertFalse(result['drafts'][0]['identity_diagnostics']['readback_checks']['matches_prose_and_source'])


class SavedReceiptRemovalTests(unittest.TestCase):
    def execute(self, mode='preserve'):
        expected=[dict(article(broken=False),title=f'Exact source {i}',content_source_url=f'https://example.invalid/source-{i}') for i in range(3)]
        original=copy.deepcopy(expected)
        state={'news_item':[dict(expected[i],author='Preserved live author') for i in (0,2)]}
        writes=[];build_count=0
        def get(_s,_t,media_id,_timeout):
            self.assertEqual('original-saved-id',media_id)
            return copy.deepcopy(state)
        def build(_s,_t,current,*_args):
            nonlocal build_count
            build_count+=1
            if mode=='concurrent' and build_count==2:state['news_item'][1]['author']='Intervening author'
            return dict(current,thumb_media_id=f'updated-cover-{build_count}'), {'cover_replaced':True,'body_replacements':[],'body_added':0,'sources':[]}
        def post(_s,url,payload,_timeout,**_kwargs):
            self.assertIn('/draft/update?',url)
            self.assertEqual('original-saved-id',payload['media_id'])
            writes.append(copy.deepcopy(payload))
            state['news_item'][payload['index']].update(payload['articles'])
            return response({'errcode':0})
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
                patch.object(repair,'get_draft',side_effect=get), patch.object(repair,'build_media_repair',side_effect=build), \
                patch.object(repair,'post_wechat_json',side_effect=post), patch.object(repair,'read_complete_draft_catalog') as catalog:
            result=repair.repair_drafts([{'media_id':'original-saved-id','articles':expected}],object(),'TOKEN',Path(temporary),30,True)
            self.assertEqual(result,json.loads((Path(temporary)/'progress.json').read_text()))
        self.assertEqual(original,expected);catalog.assert_not_called()
        return result,state,writes

    def test_single_removed_article_stays_removed_and_live_indices_authors_are_preserved(self):
        result,state,writes=self.execute()
        self.assertTrue(result['fully_repaired']);self.assertEqual(2,result['article_count'])
        self.assertEqual(3,result['expected_article_count']);self.assertEqual(1,result['preserved_removed_article_count'])
        self.assertEqual(0,result['unresolved_article_count']);self.assertEqual(2,result['updated_articles'])
        self.assertEqual([0,1],[row['index'] for row in writes])
        self.assertEqual(['Exact source 0','Exact source 2'],[row['articles']['title'] for row in writes])
        self.assertTrue(all(row['articles']['author']=='Preserved live author' for row in writes))
        self.assertEqual(2,len(state['news_item']))
        group=result['drafts'][0]
        self.assertEqual('single_removed_article_preserved',group['resolution'])
        self.assertEqual((3,2,1),(group['original_articles'],group['current_articles'],group['preserved_removed_original_index']))

    def test_no_reorder_addition_second_removal_identity_change_or_ambiguous_deletion(self):
        expected=[dict(article(),title=f'Source {i}',content_source_url=f'https://example.invalid/{i}') for i in range(3)]
        actual=[dict(expected[i],author='Live author') for i in (0,2)]
        self.assertEqual(1,repair.saved_receipt_single_removed_index(actual,expected))
        variants=[list(reversed(actual)),actual[:1],actual+[dict(article(),title='Added article')],[]]
        for key,value in [('title','Edited title'),('content','<p>Edited prose</p>'),('content_source_url','https://example.invalid/edited')]:
            changed=copy.deepcopy(actual);changed[0][key]=value;variants.append(changed)
        for changed in variants:
            with self.subTest(count=len(changed)):
                self.assertIsNone(repair.saved_receipt_single_removed_index(changed,expected))
        duplicate=article()
        self.assertIsNone(repair.saved_receipt_single_removed_index([duplicate],[duplicate,copy.deepcopy(duplicate)]))
        self.assertIsNone(repair.saved_receipt_single_removed_index([], [duplicate]))

    def test_invalid_receipt_never_rebinds_to_shorter_current_group(self):
        expected=[article(broken=False),dict(article(broken=False),title='Removed source')]
        current=[dict(expected[0],author='Live author')]
        catalog=[{'media_id':'other-live-id','content':{'news_item':current}}]
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
                patch.object(repair,'get_draft',side_effect=portal.WeChatError('Fixture invalid ID',errcode=40007)), \
                patch.object(repair,'read_complete_draft_catalog',return_value=catalog), \
                patch.object(repair,'build_media_repair') as build, patch.object(repair,'post_wechat_json') as write:
            result=repair.repair_drafts([{'media_id':'expired-saved-id','articles':expected}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual('invalid_receipt_no_current_match',result['drafts'][0]['resolution'])
        self.assertEqual(0,result['preserved_removed_article_count']);self.assertEqual(2,result['unresolved_article_count'])
        build.assert_not_called();write.assert_not_called()

    def test_midgroup_stop_counts_only_live_remaining_members_and_keeps_removal_fact(self):
        result,state,writes=self.execute('concurrent')
        self.assertEqual(1,len(writes));self.assertEqual(1,result['article_count'])
        self.assertEqual(1,result['unresolved_article_count']);self.assertEqual(1,result['preserved_removed_article_count'])
        self.assertEqual(result['expected_article_count'],sum(result[k] for k in ('article_count','unresolved_article_count','preserved_removed_article_count')))
        group=result['drafts'][0]
        self.assertEqual((2,1,1),(group['articles'],group['processed_articles'],group['remaining_articles']))
        self.assertEqual((3,2,1),(group['original_articles'],group['current_articles'],group['preserved_removed_original_index']))
        self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])


class ScheduledPublishLockTests(unittest.TestCase):
    def execute(self, *, lock_at=0, removed=False, error_code=53407, errmsg='定时发布中，无法删除或修改', transport_error=None):
        original=[dict(article(broken=False),title=f'Locked source {i}') for i in range(3)]
        later=[dict(article(broken=False),title='Independent source')]
        drafts=[{'media_id':'locked-id','articles':copy.deepcopy(original)}, {'media_id':'independent-id','articles':copy.deepcopy(later)}]
        state={'locked-id':copy.deepcopy(original[1:] if removed else original), 'independent-id':copy.deepcopy(later)}
        before=copy.deepcopy(state);attempts=[]
        def get(_s,_t,media_id,_timeout):
            return {'news_item':copy.deepcopy(state[media_id])}
        def build(_s,_t,current,*_args):
            return dict(current,thumb_media_id='repaired-cover'), {'cover_replaced':True,'body_replacements':[],'body_added':0,'sources':[]}
        def post(_s,url,payload,_timeout,**kwargs):
            self.assertIn('/draft/update?',url);self.assertEqual(1,kwargs['max_attempts'])
            attempts.append((payload['media_id'],payload['index']))
            if payload['media_id']=='locked-id' and payload['index']==lock_at:
                if transport_error is not None:raise transport_error
                return response({'errcode':error_code,'errmsg':errmsg})
            state[payload['media_id']][payload['index']].update(payload['articles'])
            return response({'errcode':0})
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
                patch.object(repair,'get_draft',side_effect=get), patch.object(repair,'build_media_repair',side_effect=build), \
                patch.object(repair,'post_wechat_json',side_effect=post):
            try:
                result=repair.repair_drafts(drafts,object(),'TOKEN',Path(temporary),30,True)
            except Exception:
                self.assertEqual([('locked-id',0)],attempts)
                self.assertEqual(before,state)
                raise
            self.assertEqual(result,json.loads((Path(temporary)/'progress.json').read_text()))
        for media_id,rows in state.items():
            self.assertEqual([repair.prose_identity(row) for row in before[media_id]], [repair.prose_identity(row) for row in rows])
        self.assertEqual(drafts[0]['articles'],original)
        return result,state,attempts

    def test_locked_first_article_is_unresolved_without_retry_and_later_group_updates(self):
        result,state,attempts=self.execute()
        self.assertEqual([('locked-id',0),('independent-id',0)],attempts)
        self.assertEqual(1,result['updated_articles']);self.assertEqual(1,result['article_count'])
        self.assertEqual(3,result['unresolved_article_count']);self.assertEqual(0,result['uncertain_article_count'])
        self.assertEqual('scheduled_publish_locked',result['drafts'][0]['resolution'])
        self.assertEqual(53407,result['drafts'][0]['wechat_errcode'])
        self.assertEqual(0,result['drafts'][0]['processed_articles'])
        self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])

    def test_lock_after_confirmed_member_preserves_update_and_counts_only_remaining(self):
        result,state,attempts=self.execute(lock_at=1)
        self.assertEqual([('locked-id',0),('locked-id',1),('independent-id',0)],attempts)
        self.assertEqual(2,result['updated_articles']);self.assertEqual(2,result['article_count'])
        self.assertEqual(2,result['unresolved_article_count']);self.assertEqual(0,result['uncertain_article_count'])
        self.assertEqual((1,2),(result['drafts'][0]['processed_articles'],result['drafts'][0]['remaining_articles']))
        self.assertEqual(1,len(result['drafts'][0]['changed']))

    def test_lock_after_preserved_removal_keeps_original_coverage_counts(self):
        result,state,attempts=self.execute(lock_at=1,removed=True)
        self.assertEqual(1,result['preserved_removed_article_count'])
        self.assertEqual(2,result['article_count']);self.assertEqual(1,result['unresolved_article_count'])
        self.assertEqual(result['expected_article_count'],sum(result[k] for k in ('article_count','unresolved_article_count','preserved_removed_article_count')))
        group=result['drafts'][0]
        self.assertEqual((3,2,0),(group['original_articles'],group['current_articles'],group['preserved_removed_original_index']))
        self.assertEqual((1,1),(group['processed_articles'],group['remaining_articles']))

    def test_unknown_code_or_different_53407_message_is_not_swallowed(self):
        for code,message in [(40014,'定时发布中，无法删除或修改'),(53407,'Unknown server refusal')]:
            with self.subTest(code=code), self.assertRaises(portal.WeChatError):
                self.execute(error_code=code,errmsg=message)

    def test_network_uncertainty_stops_without_retry_or_other_group_updates(self):
        with self.assertRaises(requests.ConnectionError):
            self.execute(transport_error=requests.ConnectionError('Synthetic update transport failure'))


class CanonicalReadbackTests(unittest.TestCase):
    def execute(self, mode='normalize'):
        original=[article(broken=False),dict(article(broken=False),title='Second unchanged source')]
        state={'news_item':copy.deepcopy(original)};built=[];written=[];log=io.StringIO()
        def get(_session,_token,media_id,_timeout):
            self.assertEqual('private-test-draft-id',media_id)
            return copy.deepcopy(state)
        def build(_session,_token,current,*_args):
            built.append(current['title'])
            if mode=='edit-second' and len(built)==2:
                state['news_item'][1]['digest']='User edited digest during preparation'
            fixed=dict(current,thumb_media_id=f'replacement-{len(built)}')
            return fixed,{'cover_replaced':True,'body_replacements':[],'body_added':0,'sources':[]}
        def post(_session,url,payload,_timeout,**_kwargs):
            self.assertIn('/draft/update?',url)
            self.assertEqual('private-test-draft-id',payload['media_id'])
            written.append(copy.deepcopy(payload));row=state['news_item'][payload['index']]
            row.update(payload['articles'])
            # Equivalent server HTML differs from the submitted writable field.
            row['content']=row['content'].replace(' />','>')
            row['thumb_url']='https://mmbiz.qpic.cn/server-rendition/0?wxfrom=5'
            if mode=='alter-prose':row['content'] += '<p>User-added independent sentence.</p>'
            return response({'errcode':0})
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(log), patch.object(repair,'get_draft',side_effect=get), \
                patch.object(repair,'build_media_repair',side_effect=build), patch.object(repair,'post_wechat_json',side_effect=post):
            result=repair.repair_drafts([{'media_id':'private-test-draft-id','articles':original}],object(),'TOKEN',Path(temporary),30,True)
            progress=json.loads((Path(temporary)/'progress.json').read_text())
        self.assertNotIn('private-test-draft-id',log.getvalue())
        return result,state,written,progress

    def test_two_consecutive_updates_use_verified_server_html_as_new_baseline(self):
        result,state,written,progress=self.execute()
        self.assertEqual([0,1],[row['index'] for row in written])
        self.assertNotEqual(written[0]['articles']['content'],state['news_item'][0]['content'])
        self.assertEqual(2,result['article_count']);self.assertEqual(2,result['updated_articles'])
        self.assertEqual(0,result['unresolved_article_count']);self.assertEqual(0,result['uncertain_article_count'])
        self.assertTrue(result['fully_repaired']);self.assertFalse(result['partial'])
        self.assertEqual(result,progress);self.assertEqual('complete',progress['status'])

    def test_midgroup_edit_counts_only_remaining_member_and_keeps_completed_update(self):
        result,state,written,progress=self.execute('edit-second')
        self.assertEqual([0],[row['index'] for row in written])
        self.assertEqual(1,result['article_count']);self.assertEqual(1,result['updated_articles'])
        self.assertEqual(1,result['unresolved_article_count']);self.assertEqual(0,result['uncertain_article_count'])
        self.assertEqual(result['expected_article_count'],result['article_count']+result['unresolved_article_count'])
        self.assertEqual(2,result['drafts'][0]['articles']);self.assertEqual(1,result['drafts'][0]['remaining_articles'])
        self.assertEqual('User edited digest during preparation',state['news_item'][1]['digest'])
        self.assertEqual(result,progress);self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])

    def test_prose_change_during_readback_never_becomes_a_new_trusted_baseline(self):
        result,state,written,progress=self.execute('alter-prose')
        self.assertEqual([0],[row['index'] for row in written])
        self.assertEqual(0,result['article_count']);self.assertEqual(1,result['updated_articles'])
        self.assertEqual(2,result['unresolved_article_count']);self.assertEqual(1,result['uncertain_article_count'])
        self.assertFalse(result['drafts'][0]['identity_diagnostics']['readback_checks']['matches_prose_and_source'])
        self.assertEqual(result,progress);self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])


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

        real_verify = repair.verify_repair_readback
        def verify(_session, _token, media_id, _timeout, expected, **kwargs):
            self.assertEqual('existing-exact-id', media_id)
            result, returned = real_verify(_session, _token, media_id, _timeout, expected, **kwargs)
            if not verification: result['ok'] = False
            return result, returned

        stack.enter_context(patch.object(repair, 'verify_repair_readback', side_effect=verify))
        return state, download, provider, upload, cover, post

    def test_real_multimember_groups_reach_later_legacy_images_and_end_with_full_media_acceptance(self):
        # The affected production groups had eight/four members, with the
        # incomplete credits on the second member. Also exercise two pending
        # members separated by a healthy one, not only a single-item draft.
        for size, pending in ((8,{1:3}),(4,{1:2}),(4,{1:3,3:2})):
            with self.subTest(size=size,pending=pending), tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
                saved=[dict(article(broken=False),title=f'Synthetic report {index}') for index in range(size)]
                live=[with_legacy_commons(row,pending[index]) if index in pending else copy.deepcopy(row)
                      for index,row in enumerate(saved)]
                state,_download,provider,upload,cover,post=self.environment(stack,live)
                upload.side_effect=[f'https://mmbiz.qpic.cn/licensed-replacement-{index}/0' for index in range(sum(pending.values()))]
                provider.side_effect=lambda _session,_title,target,*_args,**_kwargs:(photo(target),{
                    'source':'wikimedia_commons','author':'Replacement Author','license':'CC BY 4.0',
                    'source_url':'https://commons.wikimedia.org/wiki/File:Replacement.jpg',
                    'license_url':'https://creativecommons.org/licenses/by/4.0/'})
                original_verify=repair.verify_repair_readback.side_effect
                readbacks=[]
                def record_verify(*args,**kwargs):
                    checks,returned=original_verify(*args,**kwargs)
                    readbacks.append(copy.deepcopy(checks))
                    return checks,returned
                repair.verify_repair_readback.side_effect=record_verify
                receipt=[{'media_id':'existing-exact-id','articles':saved}]
                result=repair.repair_drafts(receipt,object(),'TOKEN',Path(temporary),30,True)
                self.assertTrue(result['fully_repaired']);self.assertFalse(result['partial'])
                self.assertEqual(size,result['article_count']);self.assertEqual(len(pending),result['updated_articles'])
                self.assertEqual(0,result['unresolved_article_count']);self.assertEqual(0,result['uncertain_article_count'])
                self.assertEqual(sorted(pending),[call.args[2]['index'] for call in post.call_args_list])
                self.assertEqual(sum(pending.values()),result['body_replacements'])
                self.assertEqual(len(pending),result['cover_replacements']);self.assertTrue(result['drafts'][0]['verified'])
                self.assertEqual(size,len(readbacks));self.assertTrue(all(checks['ok'] for checks in readbacks))
                self.assertFalse(readbacks[0]['matches_media_contract'])
                self.assertEqual(sorted(pending),readbacks[0]['pending_legacy_media_indices'])
                self.assertTrue(readbacks[-1]['matches_media_contract']);self.assertEqual([],readbacks[-1]['pending_legacy_media_indices'])
                for before,after in zip(saved,state['news_item']):
                    self.assertEqual(repair.prose_identity(before),repair.prose_identity(after))
                    self.assertTrue(portal.wechat_media_contract_check(after,after)['matches'])
                post.reset_mock();provider.reset_mock();upload.reset_mock();cover.reset_mock()
                again=repair.repair_drafts(receipt,object(),'TOKEN',Path(temporary),30,True)
                self.assertTrue(again['fully_repaired']);self.assertEqual(0,again['changed_articles'])
                for operation in (post,provider,upload,cover):operation.assert_not_called()

    def test_later_unrepaired_legacy_is_unresolved_without_recounting_verified_prefix(self):
        saved=[dict(article(broken=False),title=f'Synthetic report {index}') for index in range(2)]
        live=[saved[0],with_legacy_commons(saved[1],3)]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state,_download,_provider,_upload,_cover,post=self.environment(stack,live)
            stack.enter_context(patch.object(repair,'build_media_repair',side_effect=lambda _s,_t,row,*_args:(
                copy.deepcopy(row),{'cover_replaced':False,'body_replacements':[],'body_added':0,'sources':[]})))
            result=repair.repair_drafts([{'media_id':'existing-exact-id','articles':saved}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(1,result['article_count']);self.assertEqual(1,result['unresolved_article_count'])
        self.assertEqual(2,result['expected_article_count']);self.assertEqual(0,result['updated_articles'])
        self.assertEqual(0,result['uncertain_article_count']);self.assertFalse(result['fully_repaired'])
        self.assertFalse(result['drafts'][0]['verified']);self.assertEqual(1,result['drafts'][0]['processed_articles'])
        self.assertEqual('draft_image_readback_failed',result['drafts'][0]['resolution'])
        self.assertFalse(result['drafts'][0]['identity_diagnostics']['readback_checks']['matches_processed_media_contract'])
        self.assertEqual([],result['drafts'][0]['identity_diagnostics']['pending_legacy_media_indices'])
        post.assert_not_called()

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

    def test_real_three_commons_and_two_commons_plus_local_shapes_replace_only_unattributable_media(self):
        for count in (3,2):
            with self.subTest(commons_count=count), tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
                saved=article(broken=False);live=copy.deepcopy(saved)
                refs=repair.article_body_images(live['content'])
                for index,(url,alt) in enumerate(refs):
                    credit=stripped_commons_credit(('CC BY 3.0','CC BY 3.0','CC BY 2.0')[index]) if index<count else attribution_html({'source':'local_editorial'})
                    old=portal.image_html(url,alt);live['content']=live['content'].replace(old,old+credit)
                self.assertEqual(repair.prose_identity(saved),repair.prose_identity(live))
                self.assertFalse(portal.wechat_media_contract_check(live,live)['matches'])
                state,_download,provider,upload,cover,post=self.environment(stack,[live])
                provider.side_effect=lambda _s,_title,target,*_a,**_kw:(photo(target),{
                    'source':'wikimedia_commons','author':'New Synthetic Photographer','license':'CC BY 4.0',
                    'source_url':'https://commons.wikimedia.org/wiki/File:New_Synthetic.jpg',
                    'license_url':'https://creativecommons.org/licenses/by/4.0/'})
                upload.side_effect=[f'https://mmbiz.qpic.cn/new-licensed-{i}/0' for i in range(count)]
                result=repair.repair_drafts([{'media_id':'existing-exact-id','articles':[saved]}],object(),'TOKEN',Path(temporary),30,True)
                self.assertTrue(result['fully_repaired']);self.assertEqual(1,result['updated_articles'])
                self.assertEqual(count,result['body_replacements']);self.assertEqual(0,result['body_added'])
                self.assertEqual(1,result['cover_replacements']);self.assertEqual(count,provider.call_count)
                facts=result['drafts'][0]['changed'][0]
                self.assertEqual('license_source_lost',facts['cover_reason'])
                self.assertTrue(all(row['reason']=='legacy_commons_credit_missing_source' for row in facts['body_replacements']))
                self.assertEqual('editorial_fallback' if count==3 else 'retained_body_image',facts['cover_source'])
                for url,_alt in refs[:count]:self.assertNotIn(url,state['news_item'][0]['content'])
                if count==2:self.assertIn(refs[2][0],state['news_item'][0]['content'])
                self.assertEqual(repair.prose_identity(saved),repair.prose_identity(state['news_item'][0]))
                self.assertTrue(portal.wechat_media_contract_check(state['news_item'][0],state['news_item'][0])['matches'])
                self.assertEqual(count,state['news_item'][0]['content'].count('https://commons.wikimedia.org/wiki/File:New_Synthetic.jpg'))
                post.assert_called_once();cover.assert_called_once()
                post.reset_mock();provider.reset_mock();upload.reset_mock();cover.reset_mock()
                again=repair.repair_drafts([{'media_id':'existing-exact-id','articles':[saved]}],object(),'TOKEN',Path(temporary),30,True)
                self.assertTrue(again['fully_repaired']);self.assertEqual(0,again['changed_articles'])
                for call in (post,provider,upload,cover):call.assert_not_called()

    def test_incomplete_credit_audit_reports_license_problem_without_uploads_or_writes(self):
        original=article(broken=False);url,alt=repair.article_body_images(original['content'])[0]
        image=portal.image_html(url,alt);original['content']=original['content'].replace(image,image+stripped_commons_credit())
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state,_download,provider,upload,cover,post=self.environment(stack,[original])
            result=repair.repair_drafts([{'media_id':'existing-exact-id','articles':[original]}],object(),'TOKEN',Path(temporary),30,False)
        facts=result['drafts'][0]['changed'][0]
        self.assertEqual('license_source_lost',facts['cover_reason'])
        self.assertEqual('legacy_commons_credit_missing_source',facts['body_replacements'][0]['reason'])
        self.assertFalse(result['applied']);self.assertEqual(0,result['updated_articles'])
        for call in (provider,upload,cover,post):call.assert_not_called()

    def test_known_source_chart_replaces_unattributable_cover_and_avoids_unneeded_fallback(self):
        original=article(broken=False);refs=repair.article_body_images(original['content'])
        first=portal.image_html(*refs[0]);original['content']=original['content'].replace(first,first+stripped_commons_credit())
        second=portal.image_html(*refs[1]);original['content']=original['content'].replace(second,portal.image_html(refs[1][0],'assets/source_image_02.png'))
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state,_download,provider,upload,cover,_post=self.environment(stack,[original])
            result,facts=repair.build_media_repair(object(),'TOKEN',original,Path(temporary),30)
        self.assertEqual('license_source_lost',facts['cover_reason'])
        self.assertEqual('retained_source_reference',facts['cover_source'])
        self.assertEqual('remove_invalid_image',facts['body_replacements'][0]['action'])
        self.assertNotIn(refs[0][0],result['content']);self.assertNotIn(stripped_commons_credit(),result['content'])
        self.assertEqual(repair.prose_identity(original),repair.prose_identity(result))
        provider.assert_not_called();upload.assert_not_called();cover.assert_called_once()

    def test_remaining_incomplete_credit_never_passes_media_readback_without_a_repair(self):
        saved=article(broken=False);live=copy.deepcopy(saved);url,alt=repair.article_body_images(live['content'])[0]
        image=portal.image_html(url,alt);live['content']=live['content'].replace(image,image+stripped_commons_credit())
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state,_download,_provider,_upload,_cover,post=self.environment(stack,[live])
            stack.enter_context(patch.object(repair,'build_media_repair',return_value=(copy.deepcopy(live),{'cover_replaced':False,'body_replacements':[],'body_added':0,'sources':[]})))
            result=repair.repair_drafts([{'media_id':'existing-exact-id','articles':[saved]}],object(),'TOKEN',Path(temporary),30,True)
        self.assertEqual(0,result['updated_articles']);self.assertEqual(0,result['article_count'])
        self.assertFalse(result['fully_repaired']);self.assertEqual('draft_image_readback_failed',result['drafts'][0]['resolution'])
        self.assertFalse(result['drafts'][0]['identity_diagnostics']['readback_checks']['matches_media_contract'])
        post.assert_not_called()

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
            result = repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])
            self.assertEqual('draft_changed_during_image_preparation',result['drafts'][0]['resolution'])
            self.assertFalse(result['drafts'][0]['identity_diagnostics']['articles'][0]['matches']['prose'])
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
            result = repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertTrue(result['partial']);self.assertFalse(result['fully_repaired'])
            self.assertEqual('saved_receipt_identity_mismatch',result['drafts'][0]['resolution'])
            for operation in (download, provider, upload, cover, post): operation.assert_not_called()

    def test_failed_readback_cannot_report_success(self):
        original = [article()]
        with tempfile.TemporaryDirectory() as temporary, ExitStack() as stack:
            _state, _download, _provider, _upload, _cover, post = self.environment(stack, original, verification=False)
            result=repair.repair_drafts([{'media_id':'existing-exact-id','articles':original}], object(), 'TOKEN', Path(temporary), 30, True)
            self.assertEqual(1, post.call_count)
            self.assertEqual(1,result['updated_articles'])
            self.assertEqual(1,result['uncertain_article_count'])
            self.assertEqual(1,result['unresolved_article_count'])
            self.assertEqual(0,result['article_count'])
            self.assertFalse(result['fully_repaired']);self.assertTrue(result['partial'])
            self.assertEqual(result,json.loads((Path(temporary)/'progress.json').read_text()))


if __name__ == '__main__': unittest.main()
