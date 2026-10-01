import copy
import json
from pathlib import Path
import tempfile
import unittest

from build_portal_extended_locales import build
from portal_extended_handoff import next_ready_batch, pending_batch, read_handoff, save_handoff, verify_handoff
from portal_extended_incremental import prepare, read_state, remember_candidate, write_state
from portal_extended_locales import ExpansionError, make_corpus
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store
from test_portal_extended_incremental import DAY, daily_doc
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_r2 import FakeR2


class HandoffTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.store = R2Store(FakeR2(), 'private', '_extended-locales/staging/handoff')
        self.corpus = make_corpus([daily_doc()])
        self.generation = self.corpus['documents_sha256']
        self.active = [{'generation':'a'*64, 'candidates':{'fr':'b'*64}}]
        self.producer = {'run_id':'123', 'attempt':'1', 'sha':'a'*40}

    def complete(self, locale='fr'):
        directory = self.root/('candidate-'+locale)
        build(self.corpus, locale, directory, self.root/(locale+'.json'), FakeTranslator())
        self.store.put_source(self.corpus)
        return remember_candidate(self.store, locale, self.corpus, directory)['candidate_id']

    def pending(self, requested='fr', enabled='fr', active=None):
        return pending_batch(self.store, self.corpus, requested, enabled,
                             self.active if active is None else active, self.root/'restored')

    def test_complete_requires_enabled_and_already_published_locale(self):
        candidate = self.complete()
        self.assertEqual(self.pending(enabled='')['candidates'], {})
        self.assertEqual(self.pending(active=[])['candidates'], {})
        self.assertEqual(self.pending(), {'generation':self.generation, 'candidates':{'fr':candidate}})

    def test_partial_matrix_publishes_only_complete_enabled_locales(self):
        candidate = self.complete()
        self.active[0]['candidates']['pt'] = 'c'*64
        self.assertEqual(self.pending('fr,pt', 'fr,pt')['candidates'], {'fr':candidate})

    def test_already_active_identity_is_noop_without_repeat_dispatch(self):
        candidate = self.complete()
        active = [{'generation':self.generation, 'candidates':{'fr':candidate}}]
        self.assertEqual(self.pending(active=active)['candidates'], {})

    def test_corruption_and_permissions_do_not_become_missing_candidate(self):
        self.complete()
        self.store.client.deny = True
        with self.assertRaises(R2PermissionError): self.pending()
        self.store.client.deny = False
        key = next(k for k in self.store.client.objects if k.endswith('.html'))
        self.store.client.objects[key]['body'] = b'corrupt'
        with self.assertRaises(R2IntegrityError): self.pending()

    def test_english_and_malformed_receipts_are_rejected(self):
        with self.assertRaises(ExpansionError): self.pending('en', 'en')
        write_state(self.store, 'completed', 'fr', {'pages':[]}, DAY)
        with self.assertRaises(ExpansionError): self.pending()

    def test_immutable_handoff_is_bound_to_exact_generation_and_candidates(self):
        candidate = self.complete()
        batch = self.pending()
        receipt = save_handoff(self.store, batch, day=DAY, pages=1, producer=self.producer)
        before = copy.deepcopy(self.store.client.objects)
        self.assertEqual(save_handoff(self.store, batch, day=DAY, pages=1, producer=self.producer), receipt)
        self.assertEqual(self.store.client.objects, before)
        self.assertEqual(verify_handoff(self.store, receipt, self.generation, {'fr':candidate})['batch'], batch)
        with self.assertRaises(ExpansionError): verify_handoff(self.store, receipt, 'b'*64, {'fr':candidate})
        with self.assertRaises(ExpansionError): verify_handoff(self.store, receipt, self.generation, {'pt':candidate})
        key = self.store.key('publication-handoffs', receipt, 'receipt.json')
        value = json.loads(self.store.client.objects[key]['body'])
        value['pages_per_locale'] = 2
        self.store._put(key, json.dumps(value).encode(), metadata={'kind':'test'})
        with self.assertRaisesRegex(ExpansionError, 'checksum'): read_handoff(self.store, receipt)

    def test_publication_handoff_accepts_proved_continuation_but_not_readonly_recovery(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/'.github/workflows/portal-extended-locales-r2.yml').read_text().split('  publication_handoff:', 1)[1]
        self.assertIn("inputs.operation == 'candidate'", workflow)
        self.assertIn("inputs.operation == 'publication-resume'", workflow)
        self.assertNotIn("inputs.operation == 'recovery-test'", workflow)
        self.assertIn('vars.PORTAL_EXTENDED_AUTO_PUBLISH_LOCALES', workflow)
        self.assertIn("github.ref == 'refs/heads/main'", workflow)
        self.assertNotIn('pending_deployments', workflow)
        self.assertNotIn('actions/upload-artifact', workflow)
        self.assertNotIn('needs.source.outputs.has_work', workflow)
        self.assertIn('needs.source.outputs.requested_locales', workflow)

    def test_completed_but_unpublished_pages_drain_when_translation_is_noop(self):
        candidate = self.complete()
        result = prepare(self.store, self.corpus['documents'], ('fr',), DAY, self.root/'unused.json')
        self.assertFalse(result['has_work'])
        batch, corpus = next_ready_batch(self.store, DAY, 'fr', 'fr', self.active, self.root/'drain')
        self.assertEqual(batch['candidates'], {'fr':candidate})
        self.assertEqual(corpus, self.corpus)
        self.assertIsNone(next_ready_batch(self.store, DAY, 'fr', 'fr', self.active+[batch], self.root/'again'))

    def test_partial_runs_keep_complete_receipts_across_exact_generations(self):
        self.complete('fr')
        self.active[0]['candidates']['pt'] = 'c'*64
        self.corpus = make_corpus([daily_doc('https://kcdesk.com/blog/20260925-later.html')])
        self.complete('pt')
        first, _corpus = next_ready_batch(self.store, DAY, 'fr,pt', 'fr,pt', self.active, self.root/'one')
        second, _corpus = next_ready_batch(self.store, DAY, 'fr,pt', 'fr,pt', self.active+[first], self.root/'two')
        self.assertNotEqual(first['generation'], second['generation'])
        self.assertEqual(set(first['candidates']) | set(second['candidates']), {'fr','pt'})
        self.assertIsNone(next_ready_batch(self.store, DAY, 'fr,pt', 'fr,pt', self.active+[first,second], self.root/'three'))

    def test_daily_receipt_drain_never_discovers_or_backfills_other_dates(self):
        self.complete()
        self.assertIsNone(next_ready_batch(self.store, '2026-09-26', 'fr', 'fr', self.active, self.root/'tomorrow'))
        pages = read_state(self.store, 'completed', 'fr', DAY)['pages']
        write_state(self.store, 'completed', 'fr', {'pages':pages}, '2026-09-26')
        with self.assertRaisesRegex(ExpansionError, 'outside the selected source day'):
            next_ready_batch(self.store, '2026-09-26', 'fr', 'fr', self.active, self.root/'wrong')


if __name__ == '__main__':
    unittest.main()
