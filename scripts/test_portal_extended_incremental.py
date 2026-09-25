"""Synthetic daily-source and private-R2 contracts; no real model or live writes."""
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from build_portal_extended_locales import build, validate_budget, MAX_TRANSLATION_SECONDS
from portal_extended_locales import (DAILY_SCOPE, ExpansionError, daily_corpus_day, digest,
                                    document_from_html, make_corpus, publication_day, stable_bytes)
from portal_extended_incremental import (collect_today, eligible_url, prepare, read_state, remember_candidate,
                                        remember_checkpoint, restore_seed, state_key, write_state)
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store
from test_portal_extended_r2 import FakeR2
from test_portal_extended_locales import FakeTranslator, ORIGIN, html

DAY = '2026-09-25'
URL = ORIGIN + '/blog/20260925-new.html'
ROOT = Path(__file__).resolve().parent.parent


def raw_page(url=URL, day=DAY, kind='Article', body='<h1>Research note</h1><p>New market findings.</p>'):
    schema = {'@type': kind, 'url': url, 'datePublished': day, 'dateModified': day}
    return html(url, body=body, extra='<script type="application/ld+json">'+json.dumps(schema)+'</script>')


def daily_doc(url=URL, day=DAY, body='<h1>Research note</h1><p>New market findings.</p>'):
    doc = document_from_html(url, raw_page(url, day, body=body), exclude_related=True)
    doc.update(selection_day=day, selection_scope=DAILY_SCOPE)
    doc['content_sha256'] = digest(stable_bytes({k:v for k,v in doc.items() if k != 'content_sha256'}))
    return doc


class DailySourcesTests(unittest.TestCase):
    def test_four_hour_budget_is_valid_and_larger_or_empty_budget_is_not(self):
        self.assertEqual(MAX_TRANSLATION_SECONDS, 14400)
        for value in (1, 2400, 14400): self.assertEqual(validate_budget(value), value)
        for value in (0, -1, 14401):
            with self.assertRaises(ExpansionError): validate_budget(value)

    def test_urls_exclude_hubs_and_history_without_filling_to_24(self):
        self.assertTrue(eligible_url(URL, '', DAY))
        self.assertTrue(eligible_url(ORIGIN+'/reports/abc123.html', DAY, DAY))
        for path in ('/', '/about.html', '/blog/', '/blog/20260924-old.html', '/reports/',
                     '/reports/index.html', '/reports/topics.html', '/reports/topics/macro/', '/reports/institutions/ubs/'):
            self.assertFalse(eligible_url(ORIGIN+path, DAY, DAY), path)

    def test_dates_follow_shanghai_and_reject_invalid_or_ambiguous_dates(self):
        self.assertEqual(publication_day('2026-09-24T17:00:00Z'), DAY)
        for value in ('', '2026-02-30', '2026-09-25T10:00:00', 'n/a'):
            self.assertEqual(publication_day(value), '')

    def test_report_uses_own_publication_date_not_sitemap_refresh_date(self):
        report = ORIGIN+'/reports/old.html'
        with mock.patch('portal_extended_incremental.inventory_entries', return_value={URL: DAY, report: DAY}), \
             mock.patch('portal_extended_incremental.read_public', side_effect=lambda session, url:
                        raw_page(url, '2026-09-24', 'Report') if url == report else
                        raw_page(body='<h1>Today</h1><p><a href="/reports/old.html">Old report</a></p>')):
            docs = collect_today(mock.Mock(), DAY)
        self.assertEqual([doc['url'] for doc in docs], [URL])
        self.assertEqual(daily_corpus_day(make_corpus(docs)), DAY)
        self.assertFalse(docs[0]['links'])

    def test_related_history_does_not_become_translation_units(self):
        body = '<h1>New research</h1><p>Today text.</p><ul class="seo-related-reports"><li><a href="/reports/old.html">Old history title</a></li></ul>'
        doc = document_from_html(URL, raw_page(body=body), exclude_related=True)
        self.assertNotIn('Old history title', json.dumps(doc['blocks']))
        self.assertNotIn('Old history title', json.dumps(doc['links']))


class IncrementalR2Tests(unittest.TestCase):
    def setUp(self):
        directory = tempfile.TemporaryDirectory(); self.addCleanup(directory.cleanup)
        self.root = Path(directory.name)
        self.client = FakeR2()
        self.store = R2Store(self.client, 'private-bucket', '_extended-locales/staging/daily')
        self.doc = daily_doc()
        self.corpus = make_corpus([self.doc])

    def test_no_new_content_does_not_build_or_fetch_history(self):
        result = prepare(self.store, [], ('fr',), DAY, self.root/'source.json')
        self.assertFalse(result['has_work']); self.assertFalse((self.root/'source.json').exists())
        self.assertFalse(self.client.objects)

    def test_single_new_page_is_valid_without_historic_homepage(self):
        result = prepare(self.store, [self.doc], ('fr',), DAY, self.root/'source.json')
        self.assertEqual(result['selected_page_count'], 1)
        manifest = build(self.corpus, 'fr', self.root/'out', self.root/'memo.json', FakeTranslator())
        self.assertEqual(manifest['status'], 'complete-candidate')
        text = (self.root/'out/fr/blog/20260925-new.html').read_text()
        self.assertIn('noindex,follow', text)
        self.assertNotIn('href="'+ORIGIN+'/fr/"', text)

    def test_complete_receipt_skips_unchanged_content_but_changed_content_returns(self):
        build(self.corpus, 'fr', self.root/'out', self.root/'memo.json', FakeTranslator())
        remember_candidate(self.store, 'fr', self.corpus, self.root/'out')
        result = prepare(self.store, [self.doc], ('fr',), DAY, self.root/'source.json')
        self.assertFalse(result['has_work'])
        changed = daily_doc(body='<h1>Research note</h1><p>Changed findings.</p>')
        result = prepare(self.store, [changed], ('fr',), DAY, self.root/'source.json')
        self.assertTrue(result['has_work'])

    def test_content_unchanged_source_receipt_does_not_overwrite_immutable_corpus(self):
        first = prepare(self.store, [self.doc], ('fr',), DAY, self.root/'one.json')
        second = prepare(self.store, [self.doc], ('fr',), DAY, self.root/'two.json')
        self.assertEqual(first['generation'], second['generation'])

    def test_incomplete_candidate_never_marks_pages_done(self):
        build(self.corpus, 'fr', self.root/'out', self.root/'memo.json', FakeTranslator(), budget_seconds=-1)
        saved = remember_candidate(self.store, 'fr', self.corpus, self.root/'out')
        self.assertFalse(saved['ready'])
        self.assertEqual(read_state(self.store, 'completed', 'fr', DAY), {})
        self.assertTrue(prepare(self.store, [self.doc], ('fr',), DAY, self.root/'source.json')['has_work'])

    def test_new_batches_advance_by_content_receipts_and_stay_bounded(self):
        docs = [daily_doc(ORIGIN+f'/blog/20260925-{index:03}.html') for index in range(26)]
        result = prepare(self.store, docs, ('fr',), DAY, self.root/'source.json')
        self.assertEqual(result['selected_page_count'], 24); self.assertEqual(result['remaining_page_count'], 2)
        first = json.loads((self.root/'source.json').read_text())
        build(first, 'fr', self.root/'out', self.root/'memo.json', FakeTranslator())
        remember_candidate(self.store, 'fr', first, self.root/'out')
        result = prepare(self.store, docs, ('fr',), DAY, self.root/'source2.json')
        self.assertEqual(result['selected_page_count'], 2)

    def test_other_language_does_not_inherit_french_completion(self):
        build(self.corpus, 'fr', self.root/'out', self.root/'memo.json', FakeTranslator())
        remember_candidate(self.store, 'fr', self.corpus, self.root/'out')
        self.assertTrue(prepare(self.store, [self.doc], ('fr','pt'), DAY, self.root/'source.json')['has_work'])

    def test_changed_generation_reuses_exact_units_only(self):
        build(self.corpus, 'fr', self.root/'first', self.root/'memo.json', FakeTranslator())
        saved = remember_checkpoint(self.store, 'fr', self.corpus['documents_sha256'], self.root/'memo.json')
        result = restore_seed(self.store, 'fr', self.root/'seed.json')
        self.assertEqual(saved['sha256'], result['sha256'])
        second = make_corpus([daily_doc(ORIGIN+'/blog/20260925-other.html')])
        fake = FakeTranslator()
        manifest = build(second, 'fr', self.root/'second', self.root/'memo2.json', fake, seed_checkpoint=self.root/'seed.json')
        self.assertEqual(fake.calls, 0); self.assertEqual(manifest['status'], 'complete-candidate')
        self.assertEqual(json.loads((self.root/'memo2.json').read_text())['source_generation'], second['documents_sha256'])
        changed = make_corpus([daily_doc(body='<h1>Research note</h1><p>Changed findings.</p>')])
        fake = FakeTranslator()
        build(changed, 'fr', self.root/'third', self.root/'memo3.json', fake, seed_checkpoint=self.root/'seed.json')
        self.assertEqual(fake.calls, 1)

    def test_memo_snapshot_does_not_follow_a_changed_latest_pointer(self):
        build(self.corpus, 'fr', self.root/'first', self.root/'memo.json', FakeTranslator())
        first = remember_checkpoint(self.store, 'fr', self.corpus['documents_sha256'], self.root/'memo.json')
        value = json.loads((self.root/'memo.json').read_text()); value['rows'] = {}
        (self.root/'memo.json').write_bytes(stable_bytes(value))
        self.store.put_checkpoint('fr', self.corpus['documents_sha256'], self.root/'memo.json')
        restored = restore_seed(self.store, 'fr', self.root/'seed.json')
        self.assertEqual(first['sha256'], restored['sha256'])

    def test_permissions_and_checksum_fail_without_completion(self):
        self.client.deny = True
        with self.assertRaises(R2PermissionError): prepare(self.store, [self.doc], ('fr',), DAY, self.root/'source.json')
        self.client.deny = False
        write_state(self.store, 'completed', 'fr', {'pages': {}}, DAY)
        key = state_key(self.store, 'completed', 'fr', DAY)
        self.client.objects[key]['Metadata']['sha256'] = '0'*64
        with self.assertRaises(R2IntegrityError): read_state(self.store, 'completed', 'fr', DAY)

    def test_old_batch_and_english_are_rejected(self):
        with self.assertRaises(ExpansionError): prepare(self.store, [daily_doc(day='2026-09-24')], ('fr',), DAY, self.root/'source.json')
        with self.assertRaises(ExpansionError): prepare(self.store, [self.doc], ('en',), DAY, self.root/'source.json')


class WorkflowTests(unittest.TestCase):
    def test_daily_hook_four_hour_budget_and_persistence_margin(self):
        source = (ROOT/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        for required in ('workflows: [Neutral edge catalog refresh]', 'timeout-minutes: 270', 'default: "14400"',
                         "inputs.seconds || '14400'", '-gt 14400', 'max-parallel: 2',
                         "needs.source.outputs.has_work == 'true'", 'cancel-in-progress: false',
                         'portal_extended_incremental.py prepare', '--seed-checkpoint'):
            self.assertIn(required, source)
        self.assertNotIn('2400', source)
        self.assertNotIn('actions/upload-artifact', source)


if __name__ == '__main__': unittest.main()
