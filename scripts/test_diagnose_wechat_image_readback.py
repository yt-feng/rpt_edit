import copy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import Mock, patch

import requests

import diagnose_wechat_image_readback as diagnostic
from free_editorial_images import attribution_html
from push_portal_translated_to_wechat_drafts import article_prose_text, image_html, WeChatError


def response(value):
    result = requests.Response()
    result.status_code = 200
    result._content = json.dumps(value).encode()
    return result


def article(index=0):
    return {'title': f'PRIVATE TITLE {index}', 'author': 'PRIVATE AUTHOR',
            'content': f'<p>PRIVATE BODY {index} unchanged 123.</p>',
            'content_source_url': f'https://private.invalid/source-{index}',
            'thumb_media_id': f'PRIVATE OLD COVER {index}'}


def fixture():
    drafts = [{'media_id': f'PRIVATE RECEIPT {group}',
               'articles': [article(group * 8 + index) for index in range(count)]}
              for group, count in enumerate([8, 8, 8, 8, 8, 4])]
    targets = copy.deepcopy(diagnostic.TARGETS)
    for group, target in targets.items():
        draft = drafts[group - 1]
        target['receipt_id_sha256'] = diagnostic.digest(draft['media_id'])
        target['repair_expected_prose_sha256'] = diagnostic.digest(article_prose_text(draft['articles'][1]['content']))
    return drafts, targets


class CreditDiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.saved = article()
        self.credit = attribution_html({'source': 'local_editorial'})
        self.image = image_html('https://mmbiz.qpic.cn/PRIVATE-IMAGE/0', '主题配图')
        self.target = {'article_index': 1, 'repair_expected_prose_sha256': diagnostic.digest(article_prose_text(self.saved['content']))}

    def compare(self, credit, *, body=None):
        live = dict(self.saved, content=(self.saved['content'] if body is None else body) + self.image + credit,
                    thumb_media_id='PRIVATE NEW COVER')
        before = copy.deepcopy((live, self.saved))
        result = diagnostic.compare_article(live, self.saved, self.target)
        self.assertEqual(before, (live, self.saved))
        return result

    def test_current_marked_credit_has_strict_identity_but_no_claim_of_new_media_verification(self):
        result = self.compare(self.credit)
        self.assertTrue(result['strict_prose_equal'])
        self.assertTrue(result['saved_prose_matches_recorded_repair_expected_hash'])
        self.assertFalse(result['visible_text_equal'])
        self.assertFalse(result['post_repair_request_available'])
        self.assertFalse(result['repair_acceptance'])
        self.assertEqual('saved_original_receipt', result['comparison_reference'])
        self.assertFalse(result['saved_receipt_media_checks']['matches_cover'])
        self.assertFalse(result['saved_receipt_media_checks']['matches_inline_images'])
        self.assertEqual(1, result['actual_media_inventory']['inline_image_count'])

    def test_marker_class_span_and_block_changes_are_diagnostic_only(self):
        variants = [self.credit.replace(' data-editorial-credit="1"', ''),
                    self.credit.replace(' class="image-credit"', ''),
                    self.credit.replace('>主题', '><span>主题').replace('</p>', '</span></p>'),
                    self.credit.replace('<p ', '<section ').replace('</p>', '</section>')]
        for credit in variants:
            with self.subTest(credit=credit):
                result = self.compare(credit)
                self.assertFalse(result['strict_prose_equal'])
                self.assertTrue(result['diagnostic_known_caption_removal_equal'])
                self.assertEqual(1, result['actual_known_local_credits']['candidate_count'])
                self.assertEqual(0, result['actual_known_local_credits']['current_contract_credit_count'])
                self.assertFalse(result['repair_acceptance'])
                # Production comparison is unchanged even after diagnosis.
                self.assertNotEqual(article_prose_text(self.saved['content'] + credit), article_prose_text(self.saved['content']))

    def test_body_edits_and_extra_text_are_never_removed_by_caption_diagnostic(self):
        bad_credit = self.credit.replace(' data-editorial-credit="1"', '')
        changed = self.compare(bad_credit, body=self.saved['content'].replace('123', '456'))
        self.assertFalse(changed['diagnostic_known_caption_removal_equal'])
        extra = self.compare(bad_credit.replace('</p>', ' PRIVATE NOTE</p>'))
        self.assertEqual(0, extra['actual_known_local_credits']['candidate_count'])
        self.assertFalse(extra['diagnostic_known_caption_removal_equal'])
        linked = self.compare(bad_credit.replace('>主题', '><a href="https://private.invalid">主题').replace('</p>', '</a></p>'))
        self.assertEqual(1, linked['actual_known_local_credits']['candidate_count'])
        self.assertEqual(0, linked['actual_known_local_credits']['diagnostic_removed_count'])

    def test_duplicate_wrapping_containers_are_counted_once_and_comments_not_stripped(self):
        result = self.compare('<section><div>' + self.credit + '</div></section>')
        self.assertEqual(1, result['actual_known_local_credits']['candidate_count'])
        self.assertEqual(1, result['actual_known_local_credits']['diagnostic_removed_count'])
        commented = self.compare(self.credit.replace('</p>', '<!-- PRIVATE NOTE --></p>'))
        self.assertEqual(0, commented['actual_known_local_credits']['diagnostic_removed_count'])

    def test_other_recognized_credit_changes_remain_visible_after_only_local_caption_removal(self):
        commons = attribution_html({'source': 'wikimedia_commons', 'author': 'Synthetic Author A',
            'license': 'CC BY 4.0', 'source_url': 'https://commons.wikimedia.org/wiki/File:Synthetic.jpg',
            'license_url': 'https://creativecommons.org/licenses/by/4.0/'})
        self.saved['content'] += commons
        self.target['repair_expected_prose_sha256'] = diagnostic.digest(article_prose_text(self.saved['content']))
        result = self.compare(self.credit, body=self.saved['content'].replace('Synthetic Author A', 'Synthetic Author B'))
        self.assertTrue(result['strict_prose_equal'])
        self.assertFalse(result['diagnostic_known_caption_removal_equal'])
        self.assertEqual(1, result['actual_known_local_credits']['diagnostic_removed_count'])

    def test_private_values_html_attribute_names_and_urls_never_leave_diagnostics(self):
        credit = self.credit.replace('<p ', '<p PRIVATE_ATTRIBUTE="PRIVATE VALUE" ')
        serialized = json.dumps(self.compare(credit), ensure_ascii=False)
        for private in ('PRIVATE', 'private.invalid', 'mmbiz.qpic.cn', '<p', diagnostic.LOCAL_CAPTION):
            self.assertNotIn(private, serialized)

    def test_large_or_pathological_markup_stops_with_fixed_category(self):
        with self.assertRaisesRegex(diagnostic.DiagnosticError, '^content_bound$'):
            diagnostic.known_credit_shapes('x' * (diagnostic.MAX_CONTENT_BYTES + 1))
        with self.assertRaisesRegex(diagnostic.DiagnosticError, '^html_structure_bound$'):
            diagnostic.known_credit_shapes('<span>' * 70 + '</span>' * 70)


class ReadOnlyTransportTests(unittest.TestCase):
    def setUp(self):
        self.transport = Mock()
        self.transport.post.return_value = response({'errcode': 0})
        self.session = diagnostic.ReadOnlyWeChat(self.transport, {'id-one', 'id-two'})

    def post(self, path, payload, **kwargs):
        return self.session.post('https://api.weixin.qq.com' + path, data=json.dumps(payload).encode(), timeout=30, **kwargs)

    def test_one_token_and_exactly_two_known_draft_reads_are_allowed_without_redirects(self):
        self.post('/cgi-bin/stable_token', {'grant_type': 'client_credential', 'appid': 'APP', 'secret': 'SECRET', 'force_refresh': False})
        for value in ('id-one', 'id-two'):
            self.post('/cgi-bin/draft/get?access_token=TOKEN', {'media_id': value})
        self.assertEqual(3, self.transport.post.call_count)
        self.assertTrue(all(call.kwargs['allow_redirects'] is False for call in self.transport.post.call_args_list))
        with self.assertRaises(diagnostic.DiagnosticError):
            self.post('/cgi-bin/draft/get?access_token=TOKEN', {'media_id': 'id-one'})
        with self.assertRaises(diagnostic.DiagnosticError):
            self.post('/cgi-bin/stable_token', {'grant_type': 'client_credential', 'appid': 'APP', 'secret': 'SECRET', 'force_refresh': False})
        self.assertEqual(3, self.transport.post.call_count)

    def test_all_writes_uploads_catalog_reads_and_unknown_ids_are_rejected_before_transport(self):
        for path in ('/cgi-bin/draft/update', '/cgi-bin/draft/add', '/cgi-bin/draft/delete',
                     '/cgi-bin/media/uploadimg', '/cgi-bin/material/add_material', '/cgi-bin/freepublish/submit', '/cgi-bin/draft/batchget'):
            with self.subTest(path=path), self.assertRaises(diagnostic.DiagnosticError):
                self.post(path + '?access_token=TOKEN', {'media_id': 'id-one'})
        with self.assertRaises(diagnostic.DiagnosticError):
            self.post('/cgi-bin/draft/get?access_token=TOKEN', {'media_id': 'other-id'})
        with self.assertRaises(diagnostic.DiagnosticError):
            self.post('/cgi-bin/draft/get?access_token=TOKEN', {'media_id': 'id-one'}, files={'media': 'anything'})
        with self.assertRaises(diagnostic.DiagnosticError):
            self.session.post('http://api.weixin.qq.com/cgi-bin/draft/get?access_token=TOKEN', data=b'{}')
        self.transport.post.assert_not_called()


class TargetReadbackTests(unittest.TestCase):
    def test_real_get_path_reads_only_two_pinned_receipts_and_reports_sanitized_differences(self):
        drafts, targets = fixture()
        live = {draft['media_id']: copy.deepcopy(draft['articles']) for draft in drafts}
        credit = attribution_html({'source': 'local_editorial'}).replace(' data-editorial-credit="1"', '')
        for group in targets:
            live[drafts[group-1]['media_id']][1]['content'] += image_html('https://mmbiz.qpic.cn/PRIVATE/0') + credit
        transport = Mock()
        def serve(_url, **kwargs):
            payload = json.loads(kwargs['data'])
            return response({'news_item': live[payload['media_id']]})
        transport.post.side_effect = serve
        session = diagnostic.ReadOnlyWeChat(transport, {drafts[index-1]['media_id'] for index in targets})
        result = diagnostic.diagnose(drafts, session, 'TOKEN', targets=targets)
        self.assertEqual(2, transport.post.call_count)
        self.assertEqual(0, result['wechat_writes']); self.assertEqual(0, result['catalog_reads'])
        self.assertFalse(result['production_acceptance']); self.assertFalse(result['full_repair_verified'])
        for row in result['drafts']:
            self.assertTrue(row['article']['diagnostic_known_caption_removal_equal'])
            self.assertTrue(row['article']['saved_prose_matches_recorded_repair_expected_hash'])
            self.assertFalse(row['article']['strict_prose_equal'])
        for private in ('PRIVATE', 'TOKEN', 'mmbiz.qpic.cn', 'private.invalid'):
            self.assertNotIn(private, json.dumps(result))

    def test_wrong_inventory_or_id_stops_before_any_draft_read(self):
        drafts, targets = fixture()
        for changed in (drafts[:-1], [dict(drafts[0], media_id='wrong'), *drafts[1:]]):
            with patch.object(diagnostic, 'get_draft') as get, self.assertRaises(diagnostic.DiagnosticError):
                diagnostic.diagnose(changed, object(), 'TOKEN', targets=targets)
            get.assert_not_called()

    def test_changed_count_never_guesses_new_article_position_or_rebinds(self):
        drafts, targets = fixture()
        with patch.object(diagnostic, 'get_draft', side_effect=[{'news_item': drafts[0]['articles'][1:]}, {'news_item': drafts[5]['articles']}]) as get:
            result = diagnostic.diagnose(drafts, object(), 'TOKEN', targets=targets)
        self.assertEqual(2, get.call_count)
        self.assertEqual('count_changed_no_article_comparison', result['drafts'][0]['status'])
        self.assertNotIn('article', result['drafts'][0])

    def test_invalid_id_is_not_deleted_and_network_error_stops_without_retry(self):
        drafts, targets = fixture()
        with patch.object(diagnostic, 'get_draft', side_effect=[WeChatError('PRIVATE URL', errcode=40007), {'news_item': drafts[5]['articles']}]) as get:
            result = diagnostic.diagnose(drafts, object(), 'TOKEN', targets=targets)
        self.assertEqual('original_receipt_unavailable', result['drafts'][0]['status'])
        self.assertNotIn('deleted', json.dumps(result)); self.assertNotIn('PRIVATE', json.dumps(result))
        with patch.object(diagnostic, 'get_draft', side_effect=requests.ConnectionError('PRIVATE TOKEN URL')) as get:
            with self.assertRaises(requests.ConnectionError):
                diagnostic.diagnose(drafts, object(), 'TOKEN', targets=targets)
        self.assertEqual(1, get.call_count)

    def test_main_restores_only_the_existing_pinned_receipts_and_hides_exception_text(self):
        env = {'GITHUB_REPOSITORY': 'example/repo', 'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
               'GITHUB_REF': 'refs/heads/main', 'GITHUB_WORKFLOW_REF': f'example/repo/{diagnostic.WORKFLOW}@refs/heads/main'}
        with tempfile.TemporaryDirectory() as directory, patch.dict('os.environ', env), redirect_stdout(io.StringIO()) as output:
            root = Path(directory)
            with patch.object(diagnostic.receipts, 'build_client', return_value=object()), patch.object(diagnostic.receipts, 'r2_bucket', return_value='PRIVATE BUCKET'), \
                    patch.object(diagnostic.receipts, 'restore', return_value={'read_only': True}) as restore:
                self.assertEqual(0, diagnostic.main(['--mode', 'restore', '--artifact-root', str(root/'receipts'), '--output', str(root/'report.json')]))
                self.assertEqual(diagnostic.receipts.ACCEPTED_RUN_ID, restore.call_args.args[1])
            with patch.object(diagnostic.receipts, 'build_client', side_effect=RuntimeError('PRIVATE TOKEN URL')):
                self.assertEqual(1, diagnostic.main(['--mode', 'restore', '--artifact-root', str(root/'receipts'), '--output', str(root/'report.json')]))
            self.assertEqual('diagnostic_operation_failed', json.loads((root/'report.json').read_text())['category'])
            self.assertNotIn('PRIVATE', output.getvalue())


if __name__ == '__main__':
    unittest.main()
