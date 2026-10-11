"""Synthetic editorial-only source, strict translation and private R2 tests."""
import copy
import json
from pathlib import Path
import tempfile
import time
import unittest
from unittest import mock

from build_portal_extended_locales import Memo
from offline_translation import TranslationBudgetExceeded
from portal_english_commentary import (POLICY, build, extract_editorial, failure_code_counts, freeze_editorial, make_source, put_source,
                                      read_source, staging_probe, validate_source, main as english_main)
from portal_extended_locales import ExpansionError, ORIGIN, digest, stable_bytes
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store
from test_portal_extended_r2 import FakeR2
from portal_extended_daily_queue import WORKFLOW, main as admit_main

DAY = '2026-10-01'
IDENTIFIER = '20261001-' + 'a'*16
URL = f'{ORIGIN}/blog/{IDENTIFIER}.html'
COMMENT = '我的理解是，订单变化需要和交付情况一起观察。下一步应关注实际交付。'
TITLE = '订单与交付的观察'


def page(content=None, *, url=URL, day=DAY, author='KC桌面', language='zh-Hans'):
    if content is None:
        content = ('<p>原始报告正文不能进入英文。</p><h3>原文标题</h3><table><tr><td>原始图表数据</td></tr></table>'
                   '<p><img src="https://example.invalid/chart.jpg" alt="SECRET CHART"></p>'
                   f'<section><strong>KC评论：</strong>{COMMENT}</section>'
                   '<p>Original report: SECRET ORIGINAL</p>')
    ld = {'@type': 'BlogPosting', 'url': url, 'datePublished': day, 'inLanguage': language,
          'author': {'@type': 'Organization', 'name': author}}
    return ('<!doctype html><html lang="zh-Hans"><head>'
            f'<link rel="canonical" href="{url}"><meta name="description" content="原始报告摘要 SECRET DIGEST">'
            f'<script type="application/ld+json">{json.dumps(ld)}</script></head><body><main>'
            '<article class="blog-article"><header class="blog-article-header">'
            f'<h1>{TITLE} | KC桌面</h1><p class="blog-digest">SECRET DIGEST</p></header>'
            '<aside class="blog-source-card">SECRET SOURCE CARD</aside>'
            f'<div class="blog-article-content">{content}</div></article>'
            '<aside class="related"><section><strong>KC评论：</strong>SECRET RELATED</section></aside>'
            '</main></body></html>').encode()


class SyntheticTranslator:
    def __init__(self): self.calls = []
    def translate(self, value, target, source, **kwargs):
        self.calls.append(value)
        assert target == 'en'
        return {TITLE: 'Watching orders and deliveries',
                COMMENT: 'In our view, order changes need to be considered alongside deliveries. Next, watch actual deliveries.',
                '我的理解是增长5.3%。': 'In our view, growth is 5.3%.'}[value]


class EnglishEditorialTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory(); self.root = Path(self.temporary.name)
        self.client = FakeR2(); self.store = R2Store(self.client, 'private', '_extended-locales/staging/english')
        self.doc = extract_editorial(URL, page(), DAY); self.source = make_source([self.doc], DAY)

    def tearDown(self): self.temporary.cleanup()

    def test_source_contains_only_explicit_comment_not_original_digest_charts_or_source_cards(self):
        self.assertEqual(self.doc['blocks'], [{'tag': 'p', 'text': COMMENT}])
        self.assertEqual(self.doc['title'], TITLE)
        for prohibited in ['SECRET', '原始报告正文', '原始图表数据', '原文标题', 'KC评论', 'img', 'table']:
            self.assertNotIn(prohibited, json.dumps(self.source, ensure_ascii=False))
        self.assertEqual(self.doc['source_html_sha256'], digest(page()))

    def test_no_marked_comment_does_not_fall_back_to_report_or_translated_article(self):
        for content in ['<p>KC评论：只是正文中的一个标签，不是评论段。</p>',
                        '<section><p><strong>KC评论：</strong>不能授权周围原文。</p></section>',
                        '<p>Original report body.</p><p>原文摘要。</p>']:
            self.assertIsNone(extract_editorial(URL, page(content), DAY))

    def test_styled_inline_and_paragraph_commentary_preserve_full_quantities(self):
        raw = page('<section><strong>编辑评论：</strong><p>我的理解是增长<span>5.3%</span>。</p></section>')
        doc = extract_editorial(URL, raw, DAY)
        self.assertEqual(doc['blocks'][0], {'tag': 'p', 'text': '我的理解是增长5.3%。'})

    def test_original_quotes_assets_hidden_or_embeds_inside_a_comment_are_rejected(self):
        for fragment in ['<blockquote>Original quotation.</blockquote>', '<q>Original words.</q>',
                         '<img src="https://example.invalid/chart.png">', '<table><tr><td>5</td></tr></table>',
                         '<iframe src="https://example.invalid/original.pdf"></iframe>',
                         '<span hidden>SECRET</span>', '<span style="display:none">SECRET</span>',
                         '<p>https://example.invalid/original</p>', '<p>[[PORTAL_IMAGE_001]]</p>']:
            with self.subTest(fragment=fragment), self.assertRaises(ExpansionError):
                extract_editorial(URL, page(f'<section><strong>KC评论：</strong>{COMMENT}{fragment}</section>'), DAY)
        with self.assertRaises(ExpansionError):
            extract_editorial(URL, page(f'<div hidden><section><strong>KC评论：</strong>{COMMENT}</section></div>'), DAY)

    def test_current_day_canonical_owned_chinese_blog_required_not_report_or_bbg(self):
        for url, kwargs in [(ORIGIN+'/reports/abc.html', {}), (ORIGIN+'/blog/bbg-20261001.html', {}),
                            (URL, {'day': '2026-09-30'}), (URL, {'author': 'BBG Show'}),
                            (URL, {'language': ['zh-Hans', 'en']}),
                            (URL, {'url': ORIGIN+'/blog/20261001-'+ 'b'*16+'.html'})]:
            with self.subTest(url=url, kwargs=kwargs), self.assertRaises(ExpansionError):
                extract_editorial(url, page(**kwargs), DAY)

    def test_noindex_malformed_html_and_duplicate_metadata_fail_closed(self):
        for raw in [page().replace(b'<head>', b'<head><meta name="robots" content="noindex">'),
                    page().replace(b'</section>', b'</div>'),
                    page().replace(b'<link rel="canonical"', b'<link rel="canonical" rel="alternate"'),
                    page().replace(b'</head>', f'<link rel="canonical" href="{URL}"></head>'.encode())]:
            with self.assertRaises(ExpansionError): extract_editorial(URL, raw, DAY)

    def test_source_checksum_extra_fields_and_generation_tampering_rejected(self):
        for key, value in [('original_text', 'SECRET'), ('generation', '0'*64), ('day', '2026-09-30')]:
            broken = copy.deepcopy(self.source); broken[key] = value
            with self.assertRaises(ExpansionError): validate_source(broken)
        broken = copy.deepcopy(self.source); broken['documents'][0]['blocks'][0]['text'] = '篡改'
        with self.assertRaises(ExpansionError): validate_source(broken)

    def test_private_r2_source_readback_and_permissions(self):
        saved = put_source(self.store, self.source)
        self.assertEqual(saved['pages'], 1)
        self.assertEqual(read_source(self.store, saved['generation']), self.source)
        self.assertEqual(put_source(self.store, self.source), saved)
        self.assertTrue(all(row['CacheControl'] == 'private, no-store' for row in self.client.objects.values()))
        self.client.deny = True
        with self.assertRaises(R2PermissionError): put_source(self.store, self.source)
        with self.assertRaises(R2PermissionError): read_source(self.store, saved['generation'])

    def test_corrupt_r2_source_and_generation_cannot_resume(self):
        saved = put_source(self.store, self.source)
        row = next(iter(self.client.objects.values())); row['body'] = b'x' + row['body'][1:]
        with self.assertRaises(R2IntegrityError): read_source(self.store, saved['generation'])

    def test_synthetic_builder_reuses_memo_and_never_translates_original_units(self):
        translator = SyntheticTranslator(); memo = self.root/'memo.json'
        first = build(self.source, self.root/'first', memo, translator)
        self.assertEqual(first['status'], 'complete-candidate'); self.assertFalse(first['indexable'])
        self.assertEqual(translator.calls, [TITLE, COMMENT]); self.assertEqual(first['paid_provider_requests'], 0)
        body = json.loads(next((self.root/'first'/'private'/'bodies').glob('*.json')).read_text())
        self.assertEqual(body['policy'], POLICY); self.assertEqual(len(body['blocks']), 1)
        self.assertEqual(body['preview'], 'In our view, order changes need to be considered alongside deliveries.')
        self.assertNotIn('SECRET', json.dumps(first)); self.assertFalse((self.root/'first'/'en').exists())
        translator.calls = []
        second = build(self.source, self.root/'second', memo, translator)
        self.assertEqual(second['cache_hits'], 2); self.assertEqual(translator.calls, [])

    def test_english_source_fallback_and_display_corruption_never_produce_a_body(self):
        for translated in [COMMENT, 'Read https://example.invalid/chart.png', '<p>Growth is 6.3%.</p>',
                           'Growth is 6.3% __KC_PH_000__.', 'Growth is 6.3%\ufffd.',
                           'Growth | increased to 6.3%.', '增长6.3%。']:
            doc = extract_editorial(URL, page('<section><strong>KC评论：</strong>我的理解是增长5.3%。</section>'), DAY)
            fake = SyntheticTranslator()
            original = fake.translate
            fake.translate = lambda value, **kwargs: original(value, **kwargs) if value == TITLE else translated
            directory = self.root/digest(translated.encode())
            result = build(make_source([doc], DAY), directory, directory.with_suffix('.json'), fake)
            self.assertEqual(result['completed_page_count'], 0); self.assertEqual(result['status'], 'incomplete-candidate')
            self.assertFalse((directory/'private').exists())
            self.assertNotIn(translated, json.dumps(result))

    def test_numeric_advisory_passes_real_adapter_and_memo_and_reuses_cache(self):
        from hymt_offline_translation import OfflineTranslator
        doc = extract_editorial(URL, page('<section><strong>KC评论：</strong>我的理解是增长5.3%。</section>'), DAY)
        source = make_source([doc], DAY)
        engine = mock.Mock()
        engine.translate.side_effect = lambda value, *_: ('Watching orders and deliveries' if value == TITLE else 'In our view, growth is 6.3%.')
        translator = OfflineTranslator(cache_dir=self.root/'adapter-cache',
            engine_factory=lambda *_: engine, quantity_policy='advisory')
        checkpoint = self.root/'numeric-memo.json'; diagnostics = {}
        first = build(source, self.root/'numeric-first', checkpoint, translator, quantity_diagnostics=diagnostics)
        self.assertEqual(first['status'], 'complete-candidate')
        self.assertEqual(first['schema_version'], 2)
        self.assertNotIn('quantity_warning_unit_count', first)
        self.assertEqual(diagnostics, {'quantity_validation_policy':'seo-advisory-v1',
            'quantity_warning_unit_count':1, 'quantity_warning_occurrences':1})
        self.assertEqual(translator.validation_failure_count, 0)
        self.assertEqual(translator.quantity_warning_count, 1)
        calls = engine.translate.call_count
        repeat = {}; second = build(source, self.root/'numeric-second', checkpoint, translator, quantity_diagnostics=repeat)
        self.assertEqual(second['translation_calls'], 0)
        self.assertEqual(second['cache_hits'], 2)
        self.assertEqual(engine.translate.call_count, calls)
        self.assertEqual(repeat, diagnostics)
        # Adapter-level cache also passes the advisory policy without inference.
        self.assertEqual(translator.translate('我的理解是增长5.3%。', 'en', 'zh', markdown=False), 'In our view, growth is 6.3%.')
        self.assertEqual(engine.translate.call_count, calls)
        for private in ('5.3', '6.3', doc['title'], doc['blocks'][0]['text']):
            self.assertNotIn(private, json.dumps(diagnostics, ensure_ascii=False))

    def test_numeric_advisory_revalidates_seed_without_retranslation(self):
        doc = extract_editorial(URL, page('<section><strong>KC评论：</strong>我的理解是增长5.3%。</section>'), DAY)
        source = make_source([doc], DAY); translator = SyntheticTranslator()
        original = translator.translate
        translator.translate = lambda value, **kwargs: original(value, **kwargs) if value == TITLE else 'In our view, growth is 6.3%.'
        seed = self.root/'numeric-seed.json'
        build(source, self.root/'seed-out', seed, translator)
        no_model = mock.Mock(); no_model.translate.side_effect = AssertionError('Seed must avoid inference')
        diagnostics = {}
        result = build(source, self.root/'seed-resume', self.root/'seed-resume.json', no_model,
                       seed_checkpoint=seed, quantity_diagnostics=diagnostics)
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertEqual(result['cache_hits'], 2)
        self.assertEqual(diagnostics['quantity_warning_unit_count'], 1)
        no_model.translate.assert_not_called()

    def test_editorial_rejection_never_poison_checkpoint_or_block_valid_resume(self):
        for bad_text in ['In our view, watch orders 订单 and deliveries.',
                         'Read https://example.invalid/original', 'Original report: private source']:
            with self.subTest(bad_text=bad_text):
                directory = self.root/digest(bad_text.encode()); checkpoint = directory.with_suffix('.json')
                bad = SyntheticTranslator(); original = bad.translate
                bad.translate = lambda value, **kwargs: original(value, **kwargs) if value == TITLE else bad_text
                bad.discard_translation = mock.Mock()
                first = build(self.source, directory/'first', checkpoint, bad)
                self.assertEqual(first['completed_page_count'], 0)
                self.assertEqual(failure_code_counts(first['failures']),
                                 {'english-language-validation' if '订单' in bad_text else 'english-asset-validation': 1})
                self.assertFalse((directory/'first'/'private').exists())
                self.assertNotIn(bad_text, [row['text'] for row in json.loads(checkpoint.read_text())['rows'].values()])
                bad.discard_translation.assert_called_once_with(COMMENT, 'en', 'zh', markdown=False)
                good = SyntheticTranslator()
                second = build(self.source, directory/'second', checkpoint, good)
                self.assertEqual(second['status'], 'complete-candidate')
                self.assertEqual(good.calls, [COMMENT]); self.assertEqual(second['cache_hits'], 1)

    def test_legacy_editorial_bad_checkpoint_and_seed_discard_only_invalid_unit(self):
        bad_text = 'In our view, watch orders 订单 and deliveries.'
        for seeded in (False, True):
            with self.subTest(seeded=seeded):
                directory = self.root/str(seeded); directory.mkdir()
                legacy = directory/'legacy.json'
                old = SyntheticTranslator(); original = old.translate
                old.translate = lambda value, **kwargs: original(value, **kwargs) if value == TITLE else bad_text
                # Materialize an authentic pre-fix memo row that passes the
                # generic language contract, but violates English policy.
                memo = Memo(legacy, 'en', old, time.monotonic()+30, source_generation=self.source['generation'])
                memo.get(TITLE); memo.get(COMMENT)
                translator = SyntheticTranslator(); valid_translate = translator.translate
                adapter_cache = {COMMENT: bad_text}; discarded = []
                def translate(value, **kwargs):
                    return adapter_cache[value] if value in adapter_cache else valid_translate(value, **kwargs)
                def discard(value, target, source, **kwargs):
                    discarded.append(value); adapter_cache.pop(value, None)
                translator.translate = translate; translator.discard_translation = discard
                checkpoint = directory/'fresh.json' if seeded else legacy
                result = build(self.source, directory/'out', checkpoint, translator,
                               seed_checkpoint=legacy if seeded else None)
                self.assertEqual(result['status'], 'complete-candidate')
                self.assertEqual(discarded, [COMMENT]); self.assertEqual(translator.calls, [COMMENT])
                self.assertEqual(result['cache_hits'], 1)
                self.assertNotIn(bad_text, [row['text'] for row in json.loads(checkpoint.read_text())['rows'].values()])

    def test_oversized_english_title_is_rejected_before_cache_write(self):
        translator = SyntheticTranslator(); original = translator.translate
        translator.translate = lambda value, **kwargs: 'Editorial observation ' * 30 if value == TITLE else original(value, **kwargs)
        result = build(self.source, self.root/'out', self.root/'memo.json', translator)
        self.assertEqual(result['status'], 'incomplete-candidate')
        self.assertEqual(failure_code_counts(result['failures']), {'english-size-validation': 1})
        self.assertEqual(json.loads((self.root/'memo.json').read_text())['rows'], {})
        self.assertFalse((self.root/'out'/'private').exists())

    def test_timeout_materializes_checkpoint_and_cannot_be_complete(self):
        fake = SyntheticTranslator(); fake.translate = mock.Mock(side_effect=TranslationBudgetExceeded('budget'))
        result = build(self.source, self.root/'out', self.root/'memo.json', fake)
        self.assertTrue(result['budget_exhausted']); self.assertEqual(result['status'], 'incomplete-candidate')
        checkpoint = json.loads((self.root/'memo.json').read_text())
        self.assertEqual(checkpoint['rows'], {}); self.assertEqual(checkpoint['source_generation'], self.source['generation'])

    def test_only_24_pages_per_batch_and_no_overwrite_or_symlink(self):
        docs = []
        for number in range(25):
            doc = copy.deepcopy(self.doc); doc['id'] = '20261001-'+f'{number:016x}'
            doc['source_url'] = f'{ORIGIN}/blog/{doc["id"]}.html'
            doc['editorial_sha256'] = digest(stable_bytes({k:v for k,v in doc.items() if k != 'editorial_sha256'}))
            docs.append(doc)
        with self.assertRaises(ExpansionError): build(make_source(docs, DAY), self.root/'out', self.root/'memo', SyntheticTranslator())
        self.assertFalse((self.root/'out').exists())
        (self.root/'out').mkdir(); (self.root/'out'/'keep').write_text('user file')
        with self.assertRaises(ExpansionError): build(self.source, self.root/'out', self.root/'memo', SyntheticTranslator())
        self.assertEqual((self.root/'out'/'keep').read_text(), 'user file')
        (self.root/'linked').symlink_to(self.root/'out', target_is_directory=True)
        with self.assertRaises(ExpansionError): build(self.source, self.root/'linked', self.root/'memo', SyntheticTranslator())

    def test_staging_probe_never_infers_or_creates_ready_ledger(self):
        result = staging_probe(self.store)
        self.assertEqual(result['english_editorial_restore'], 'passed'); self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['english_checkpoint_restore'], 'passed')
        self.assertEqual(result['ready_candidates'], 0); self.assertFalse(result['deployed'])
        self.assertTrue(all('/sources/' in key or '/checkpoints/' in key for key in self.client.objects))
        with self.assertRaises(Exception): staging_probe(R2Store(self.client, 'private', '_english-commentary/v1'))

    def test_feature_branch_cannot_start_production_english_model(self):
        # Test the CLI boundary, never instantiate or execute a real translator.
        environment = {'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_REF': 'refs/heads/feature'}
        with mock.patch.dict('os.environ', environment, clear=True), \
             mock.patch('sys.argv', ['english']), mock.patch('portal_english_commentary.require_actions'), \
             mock.patch('portal_english_commentary.OfflineTranslator') as translator:
            with self.assertRaises(ExpansionError): english_main()
            translator.assert_not_called()

    def test_main_emits_safe_terminal_diagnostics_without_publishing_failed_body(self):
        from hymt_offline_translation import OfflineTranslationValidationError
        corpus = self.root/'source.json'; corpus.write_text(json.dumps(self.source))
        fake = SyntheticTranslator()
        fake.failure_diagnostics = [{'source_sha256': digest(COMMENT.encode()),
                                     'placeholders': {'expected': 1, 'canonical': {'missing': 1}}}]
        fake.validation_failure_count = 1
        original = fake.translate
        def translate(value, **kwargs):
            if value == TITLE: return original(value, **kwargs)
            raise OfflineTranslationValidationError('offline-placeholder-validation')
        fake.translate = translate
        environment = {'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_REF': 'refs/heads/main'}
        with mock.patch.dict('os.environ', environment, clear=True), \
             mock.patch('sys.argv', ['english', '--corpus', str(corpus), '--output', str(self.root/'out'),
                                     '--checkpoint', str(self.root/'memo.json')]), \
             mock.patch('portal_english_commentary.require_actions'), \
             mock.patch('portal_english_commentary.OfflineTranslator', return_value=fake) as factory, \
             mock.patch('builtins.print') as printed:
            self.assertEqual(english_main(), 1)
        factory.assert_called_once_with(validation_attempts=3, quantity_policy='advisory')
        summary = json.loads(printed.call_args.args[0])
        self.assertEqual(summary['terminal_translation_diagnostics'], fake.failure_diagnostics)
        self.assertEqual(summary['terminal_validation_failure_count'], 1)
        self.assertEqual(summary['failure_code_counts'], {'offline-placeholder-validation': 1})
        self.assertEqual(summary['completed_page_count'], 0)
        self.assertEqual(summary['quantity_validation_policy'], 'seo-advisory-v1')
        self.assertEqual(summary['quantity_warning_unit_count'], 0)
        self.assertNotIn(COMMENT, json.dumps(summary, ensure_ascii=False))
        self.assertFalse((self.root/'out'/'private').exists())

    def test_frozen_source_receipt_is_bound_to_original_admission_and_has_no_ready_or_active_pointer(self):
        producer = {'run_id': '123', 'attempt': '1', 'sha': 'b'*40, 'repository': 'example/repo', 'workflow': WORKFLOW}
        result = freeze_editorial(self.store, [self.doc], DAY, producer, 'c'*64)
        self.assertTrue(result['admitted'])
        receipt_key = self.store.key('source-admissions', result['receipt'], 'receipt.json')
        receipt = json.loads(self.store._get(receipt_key, maximum=65536))
        self.assertEqual(receipt['producer'], producer); self.assertEqual(receipt['source_admission'], 'c'*64)
        self.assertEqual(digest(stable_bytes(receipt)), result['receipt'])
        self.assertEqual(freeze_editorial(self.store, [self.doc], DAY, producer, 'c'*64), result)
        self.assertFalse(any('active.json' in key or 'ready' in key for key in self.client.objects))
        self.assertEqual(freeze_editorial(self.store, [], DAY, producer, 'c'*64)['pages'], 0)

    def test_source_workflow_projects_same_fetch_once_into_private_english_snapshot(self):
        environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true',
                       'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': 'b'*40,
                       'GITHUB_REPOSITORY': 'example/repo'}
        with mock.patch.dict('os.environ', environment), \
             mock.patch('sys.argv', ['queue', '--prefix', self.store.prefix]), \
             mock.patch('portal_extended_daily_queue.today', return_value=DAY), \
             mock.patch('portal_extended_daily_queue.R2Store.from_env', return_value=self.store), \
             mock.patch('portal_extended_source_refresh.read_release', return_value={
                 'slot':'a', 'release_id':'a'*32, 'tree_sha256':'b'*64}), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value={URL: DAY}), \
             mock.patch('portal_extended_incremental.read_public', return_value=page()) as fetch, \
             mock.patch('builtins.print') as printed:
            admit_main()
        self.assertEqual(fetch.call_count, 1)
        result = json.loads(printed.call_args.args[0]); self.assertTrue(result['admitted'])
        self.assertEqual(result['english_editorial']['pages'], 1)
        self.assertEqual(result['english_editorial']['excluded_page_count'], 0)
        self.assertTrue(all(key.startswith(self.store.prefix + '/') for key in self.client.objects))

    def test_english_persistence_failure_does_not_claim_english_completion_or_stall_other_locales(self):
        environment = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true',
                       'GITHUB_RUN_ID': '123', 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': 'b'*40,
                       'GITHUB_REPOSITORY': 'example/repo'}
        with mock.patch.dict('os.environ', environment), \
             mock.patch('sys.argv', ['queue', '--prefix', self.store.prefix]), \
             mock.patch('portal_extended_daily_queue.today', return_value=DAY), \
             mock.patch('portal_extended_daily_queue.R2Store.from_env', return_value=self.store), \
             mock.patch('portal_extended_source_refresh.read_release', return_value={
                 'slot':'a', 'release_id':'a'*32, 'tree_sha256':'b'*64}), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value={URL: DAY}), \
             mock.patch('portal_extended_incremental.read_public', return_value=page()), \
             mock.patch('portal_english_commentary.freeze_editorial', side_effect=R2PermissionError('denied')), \
             mock.patch('builtins.print') as printed:
            admit_main()
        result = json.loads(printed.call_args.args[0]); self.assertTrue(result['admitted'])
        self.assertFalse(result['english_editorial']['admitted'])
        self.assertTrue(result['english_editorial']['capture_incomplete'])


if __name__ == '__main__': unittest.main()
