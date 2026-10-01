"""Offline continuation/approval contracts with fake R2 and a fake translator."""
import copy
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

from build_portal_extended_locales import build
from offline_translation import TranslationBudgetExceeded
from portal_extended_locales import ExpansionError, digest, make_corpus, stable_bytes
from portal_extended_r2 import R2Store, R2IntegrityError
import portal_extended_incremental as incremental
from portal_extended_continuation import (MAX_CONTINUATIONS, MAX_PENDING_GENERATIONS, adopt_existing,
    acknowledge_published, pending, queue, read_origin, register, restore_claimed_checkpoint,
    save_queue, verify_origin_run)
from portal_extended_handoff import next_registered_batch, read_handoff, save_handoff
from review_portal_extended_handoff import producer_is_valid
from inspect_portal_extended_continuation import inspect
from test_portal_extended_incremental import DAY, daily_doc
from test_portal_extended_locales import FakeTranslator, ORIGIN
from test_portal_extended_r2 import FakeR2

PRODUCER = {'run_id': '123', 'attempt': '1', 'sha': 'a'*40}
ENV = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'GITHUB_RUN_ID': '456',
       'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': 'b'*40, 'GITHUB_REPOSITORY': 'example/repo'}


class StopAtLastUnit(FakeTranslator):
    def translate(self, text, **kwargs):
        if text == 'Second unique unfinished unit.':
            raise TranslationBudgetExceeded('synthetic deadline')
        return super().translate(text, **kwargs)


class ContinuationTests(unittest.TestCase):
    def setUp(self):
        tmp = tempfile.TemporaryDirectory(); self.addCleanup(tmp.cleanup)
        self.root = Path(tmp.name)
        self.store = R2Store(FakeR2(), 'private', '_extended-locales/staging/continuation')
        self.corpus = make_corpus([daily_doc(), daily_doc(ORIGIN+'/blog/20260925-second.html',
            body='<h1>Second page</h1><p>Second unique unfinished unit.</p>')])
        self.gen = self.corpus['documents_sha256']
        self.store.put_source(self.corpus)
        self.active = [{'generation': 'a'*64, 'candidates': {'fr': 'b'*64}}]
        self.run = {'id': 123, 'run_attempt': 1, 'head_sha': 'a'*40, 'status': 'completed',
            'conclusion': 'failure', 'head_branch': 'main', 'event': 'workflow_run',
            'path': '.github/workflows/portal-extended-locales-r2.yml',
            'repository': {'full_name': 'example/repo', 'private': False},
            'head_repository': {'full_name': 'example/repo'}}
        self.jobs = [{'name': 'source', 'status': 'completed', 'conclusion': 'success',
            'started_at': DAY+'T01:00:00Z', 'completed_at': DAY+'T01:10:00Z'},
            {'name': 'locale (fr)', 'status': 'completed', 'conclusion': 'failure'}]

    def partial(self, *, registered=True, locale='fr'):
        if registered:
            register(self.store, self.corpus, (locale,), PRODUCER)
        checkpoint = self.root/(locale+'-checkpoint.json')
        output = self.root/(locale+'-partial')
        manifest = build(self.corpus, locale, output, checkpoint, StopAtLastUnit(), allow_source_fallback=True)
        self.assertEqual(manifest['status'], 'incomplete-candidate')
        self.assertTrue(manifest['budget_exhausted'])
        self.assertEqual(manifest['completed_page_count'], 1)
        saved = incremental.remember_checkpoint(self.store, locale, self.gen, checkpoint)
        result = incremental.remember_candidate(self.store, locale, self.corpus, output)
        return {'checkpoint_sha256': saved['sha256'], 'candidate_id': result['candidate_id'],
                'manifest_sha256': result['manifest_sha256']}

    def finish(self):
        pending(self.store, ('fr',), self.root/'restored-source.json')
        checkpoint = self.root/'resumed-checkpoint.json'
        restore_claimed_checkpoint(self.store, 'fr', self.gen, checkpoint)
        translator = FakeTranslator()
        manifest = build(self.corpus, 'fr', self.root/'finished', checkpoint, translator)
        self.assertEqual(manifest['status'], 'complete-candidate')
        self.assertEqual(translator.calls, 1)
        incremental.remember_checkpoint(self.store, 'fr', self.gen, checkpoint)
        result = incremental.remember_candidate(self.store, 'fr', self.corpus, self.root/'finished')
        return result

    def test_cross_day_main_restores_original_source_before_any_collection(self):
        self.partial()
        original = stable_bytes(self.corpus)
        args = ['test', 'prepare', '--locales', 'fr', '--corpus', str(self.root/'next.json')]
        with patch.dict(os.environ, ENV), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value='2026-10-02'), \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No new-day collection')):
            self.assertEqual(incremental.main(), 0)
        self.assertEqual((self.root/'next.json').read_bytes(), original)
        row = queue(self.store, 'fr')[self.gen]
        self.assertEqual((row['status'], row['continuations']), ('claimed', 1))
        self.assertEqual(read_origin(self.store, self.gen)['source_day'], DAY)

    def test_same_generation_resume_uses_only_one_missing_unit_and_preserves_quality_gates(self):
        self.partial()
        result = self.finish()
        self.assertTrue(result['ready'])
        self.assertEqual(queue(self.store, 'fr')[self.gen]['status'], 'complete')
        self.assertEqual(queue(self.store, 'fr')[self.gen]['snapshot']['completed_pages'], 2)
        self.assertFalse(pending(self.store, ('fr',), self.root/'unused.json'))

    def test_claimed_immutable_checkpoint_ignores_changed_latest_pointer(self):
        proof = self.partial()
        pending(self.store, ('fr',), self.root/'source.json')
        other = json.loads((self.root/'fr-checkpoint.json').read_bytes())
        other['rows'] = {}
        changed = self.root/'changed.json'; changed.write_bytes(stable_bytes(other))
        self.store.put_checkpoint('fr', self.gen, changed)
        restored = restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'exact.json')
        self.assertEqual(restored['sha256'], proof['checkpoint_sha256'])
        self.assertEqual(digest((self.root/'exact.json').read_bytes()), proof['checkpoint_sha256'])

    def test_partial_manifest_history_is_retained_when_inventory_id_is_reused(self):
        proof = self.partial()
        key = self.store.candidate_manifest_key('fr', self.gen, proof['candidate_id'])
        changed = json.loads(self.store.client.objects[key]['body'])
        changed['translation_calls_this_run'] = 999
        self.store._put(key, stable_bytes(changed), metadata={'kind': 'synthetic-later-attempt'})
        # Checkpointed continuation uses the preserved exact outcome, not this mutable metadata path.
        self.assertTrue(pending(self.store, ('fr',), self.root/'source.json')['has_work'])
        archive = self.store.key('incremental', 'continuation-manifests', self.gen, 'fr', proof['manifest_sha256']+'.json')
        self.assertEqual(digest(self.store._get(archive, maximum=2*1024*1024)), proof['manifest_sha256'])

    def test_rerunning_only_a_locale_without_new_source_claim_stops_before_model_setup(self):
        self.partial()
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'new source-job claim'):
            restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'not-restored.json')
        self.assertFalse((self.root/'not-restored.json').exists())
        self.assertEqual(self.store.client.objects, before)

    def test_no_progress_stops_and_incomplete_never_marks_complete_or_ready(self):
        self.partial()
        pending(self.store, ('fr',), self.root/'source.json')
        cp = self.root/'resume.json'; restore_claimed_checkpoint(self.store, 'fr', self.gen, cp)
        build(self.corpus, 'fr', self.root/'same-partial', cp, StopAtLastUnit())
        incremental.remember_checkpoint(self.store, 'fr', self.gen, cp)
        with self.assertRaisesRegex(ExpansionError, 'No continuation progress'):
            incremental.remember_candidate(self.store, 'fr', self.corpus, self.root/'same-partial')
        self.assertEqual(queue(self.store, 'fr')[self.gen]['status'], 'blocked')
        self.assertEqual(incremental.read_state(self.store, 'completed', 'fr', DAY), {})
        with self.assertRaisesRegex(ExpansionError, 'No continuation progress'):
            pending(self.store, ('fr',), self.root/'never.json')
        self.assertFalse(any('/ready.json' in key for key in self.store.client.objects))

    def test_no_checkpoint_unknown_outcome_and_exhausted_budget_stop_before_claim(self):
        register(self.store, self.corpus, ('fr',), PRODUCER)
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'missing completed checkpoint outcome'):
            pending(self.store, ('fr',), self.root/'never.json')
        self.assertEqual(self.store.client.objects, before)
        self.partial()
        rows = queue(self.store, 'fr'); rows[self.gen]['continuations'] = MAX_CONTINUATIONS
        save_queue(self.store, 'fr', rows)
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'bound reached'):
            pending(self.store, ('fr',), self.root/'never.json')
        self.assertEqual(self.store.client.objects, before)

    def test_corrupt_checkpoint_or_manifest_stops_before_any_claim(self):
        proof = self.partial()
        for key in (self.store.checkpoint_object_key('fr', self.gen, proof['checkpoint_sha256']),
                    self.store.key('incremental', 'continuation-manifests', self.gen, 'fr', proof['manifest_sha256']+'.json')):
            old = self.store.client.objects[key]['body']
            self.store.client.objects[key]['body'] = b'broken'
            before = copy.deepcopy(self.store.client.objects)
            with self.assertRaises((ExpansionError, R2IntegrityError)):
                pending(self.store, ('fr',), self.root/'never.json')
            self.assertEqual(self.store.client.objects, before)
            self.store.client.objects[key]['body'] = old

    def test_locale_queues_do_not_overwrite_each_other(self):
        register(self.store, self.corpus, ('fr', 'pt'), PRODUCER)
        self.partial()
        self.assertEqual(queue(self.store, 'pt')[self.gen]['status'], 'started')
        self.assertEqual(queue(self.store, 'fr')[self.gen]['status'], 'incomplete')

    def test_unpublished_cross_day_result_survives_new_completed_receipts_and_only_exact_live_ack_removes_it(self):
        self.partial(); result = self.finish()
        # A later source revision may replace per-page daily completed receipts.
        incremental.write_state(self.store, 'completed', 'fr', {'pages': {}}, DAY)
        batch, corpus = next_registered_batch(self.store, 'fr', 'fr', self.active, self.root/'handoff')
        self.assertEqual(batch, {'generation': self.gen, 'candidates': {'fr': result['candidate_id']}})
        self.assertEqual(corpus, self.corpus)
        acknowledge_published(self.store, ('fr',), self.active)
        self.assertIn(self.gen, queue(self.store, 'fr'))
        before_origins = {k: v for k, v in self.store.client.objects.items() if 'generation-origins' in k or 'continuation-results' in k}
        acknowledge_published(self.store, ('fr',), self.active+[batch])
        self.assertEqual(queue(self.store, 'fr'), {})
        self.assertEqual({k: v for k, v in self.store.client.objects.items() if k in before_origins}, before_origins)

    def test_handoff_keeps_active_locale_approval_and_complete_candidate_checks(self):
        self.partial(); result = self.finish()
        self.assertIsNone(next_registered_batch(self.store, 'fr', '', self.active, self.root/'disabled'))
        self.assertIsNone(next_registered_batch(self.store, 'fr', 'fr', [], self.root/'not-live'))
        key = next(k for k in self.store.client.objects if k.endswith('.html') and '/'+result['candidate_id']+'/' in k)
        self.store.client.objects[key]['body'] = b'changed'
        with self.assertRaises(R2IntegrityError):
            next_registered_batch(self.store, 'fr', 'fr', self.active, self.root/'corrupt')

    def test_public_inspection_is_read_only_and_summary_excludes_private_units(self):
        proof = self.partial(registered=False)
        before = copy.deepcopy(self.store.client.objects)
        result = inspect(self.store, self.gen, 'fr', proof['checkpoint_sha256'], proof['candidate_id'], self.root/'inspection')
        self.assertEqual(self.store.client.objects, before)
        self.assertEqual((result['completed_page_count'], result['source_document_count']), (1, 2))
        self.assertEqual(result['remaining_source_urls'], [ORIGIN+'/blog/20260925-second.html'])
        self.assertNotIn('Second unique unfinished unit', json.dumps(result))
        self.assertEqual((result['production_writes'], result['model_calls'], result['paid_provider_requests']), (0, 0, 0))
        with self.assertRaisesRegex(ExpansionError, 'new directory'):
            inspect(self.store, self.gen, 'fr', proof['checkpoint_sha256'], proof['candidate_id'], self.root/'inspection')

    def test_exact_preledger_adoption_is_bounded_and_cannot_reset_counters(self):
        proof = self.partial(registered=False)
        evidence = {'producer': PRODUCER, 'locales': {'fr': proof}}
        def api(path):
            return {'total_count': len(self.jobs), 'jobs': self.jobs} if '/jobs?' in path else self.run
        adopt_existing(self.store, self.corpus, ('fr',), evidence, 'example/repo', api)
        self.assertEqual(queue(self.store, 'fr')[self.gen]['status'], 'incomplete')
        self.finish()
        with self.assertRaisesRegex(ExpansionError, 'cannot reset'):
            adopt_existing(self.store, self.corpus, ('fr',), evidence, 'example/repo', api)

    def test_adoption_rejects_unfinished_origin_wrong_date_or_proof_before_writes(self):
        proof = self.partial(registered=False)
        evidence = {'producer': PRODUCER, 'locales': {'fr': proof}}
        before = copy.deepcopy(self.store.client.objects)
        for run, jobs, item in (({**self.run, 'status': 'in_progress'}, self.jobs, evidence),
            (self.run, [{**self.jobs[0], 'started_at': '2026-09-26T01:00:00Z', 'completed_at': '2026-09-26T01:10:00Z'}, self.jobs[1]], evidence),
            (self.run, self.jobs, {**evidence, 'locales': {'fr': {**proof, 'manifest_sha256': '0'*64}}})):
            def api(path):
                return {'total_count': len(jobs), 'jobs': jobs} if '/jobs?' in path else run
            with self.assertRaises(ExpansionError):
                adopt_existing(self.store, self.corpus, ('fr',), item, 'example/repo', api)
            self.assertEqual(self.store.client.objects, before)

    def test_cross_day_reviewer_requires_original_source_job_and_exact_origin_hash(self):
        self.partial(); result = self.finish()
        batch = {'generation': self.gen, 'candidates': {'fr': result['candidate_id']}}
        receipt_id = save_handoff(self.store, batch, day=DAY, pages=2,
            producer={'run_id': '456', 'attempt': '1', 'sha': 'b'*40})
        receipt = read_handoff(self.store, receipt_id)
        current = {**self.run, 'id': 456, 'head_sha': 'b'*40, 'event': 'workflow_dispatch'}
        jobs = [{**self.jobs[0], 'started_at': '2026-10-02T01:00:00Z', 'completed_at': '2026-10-02T01:10:00Z'},
            {'name': 'publication_handoff', 'status': 'completed', 'conclusion': 'success'}]
        origin = read_origin(self.store, self.gen)
        producer_is_valid(receipt, current, jobs, 'example/repo', origin=origin, original_run=self.run, original_jobs=self.jobs)
        for changes in ({'origin': None}, {'origin': {**origin, 'source_sha256': '0'*64}},
                        {'original_run': {**self.run, 'head_sha': '0'*40}}, {'original_jobs': []}):
            kwargs = {'origin': origin, 'original_run': self.run, 'original_jobs': self.jobs}; kwargs.update(changes)
            with self.assertRaises(ExpansionError): producer_is_valid(receipt, current, jobs, 'example/repo', **kwargs)
        legacy = {k: v for k, v in receipt.items() if k != 'source_origin_sha256'}
        with self.assertRaisesRegex(ExpansionError, 'Historical source'):
            producer_is_valid(legacy, current, jobs, 'example/repo')

    def test_queue_capacity_fails_without_eviction_or_partial_new_origin(self):
        rows = {f'{index:064x}': {'status': 'complete', 'continuations': 0} for index in range(MAX_PENDING_GENERATIONS)}
        save_queue(self.store, 'fr', rows)
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'queue is full'):
            register(self.store, self.corpus, ('fr',), PRODUCER)
        self.assertEqual(self.store.client.objects, before)

    def test_different_locale_generations_never_mix_or_discard_later_work(self):
        self.partial()
        earlier = self.gen
        first_root = self.root
        self.root = first_root/'later'; self.root.mkdir()
        self.corpus = make_corpus([daily_doc(ORIGIN+'/blog/20260926-first.html', day='2026-09-26'),
            daily_doc(ORIGIN+'/blog/20260926-second.html', day='2026-09-26',
                      body='<h1>Second page</h1><p>Second unique unfinished unit.</p>')])
        self.gen = self.corpus['documents_sha256']; self.store.put_source(self.corpus)
        self.partial(locale='pt')
        later_before = copy.deepcopy(queue(self.store, 'pt'))
        result = pending(self.store, ('fr', 'pt'), self.root/'selected-source.json')
        self.assertEqual(result['generation'], earlier)
        self.assertEqual(json.loads(result['locales_json']), ['fr'])
        self.assertEqual(json.loads((self.root/'selected-source.json').read_bytes())['documents_sha256'], earlier)
        self.assertEqual(queue(self.store, 'pt'), later_before)

    def test_ready_locale_is_not_retranslated_when_same_generation_other_locale_resumes(self):
        register(self.store, self.corpus, ('fr', 'pt'), PRODUCER)
        self.partial(); self.finish()
        self.partial(locale='pt')
        before = copy.deepcopy(queue(self.store, 'fr'))
        result = pending(self.store, ('fr', 'pt'), self.root/'selected-source.json')
        self.assertEqual(result['generation'], self.gen)
        self.assertEqual(json.loads(result['locales_json']), ['pt'])
        self.assertEqual(queue(self.store, 'fr'), before)

    def test_nonmain_branch_cannot_claim_or_restore_registered_production_work(self):
        self.partial()
        before = copy.deepcopy(self.store.client.objects)
        args = ['test', 'prepare', '--locales', 'fr', '--corpus', str(self.root/'branch.json')]
        with patch.dict(os.environ, {**ENV, 'GITHUB_REF': 'refs/heads/codex/example'}), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'collect_today', return_value=[]), \
             patch.object(incremental.requests, 'Session'):
            with patch('sys.argv', args):
                self.assertEqual(incremental.main(), 0)
            args = ['test', 'restore-checkpoint', '--locale', 'fr', '--generation', self.gen,
                    '--checkpoint', str(self.root/'forbidden.json')]
            with patch('sys.argv', args), self.assertRaisesRegex(ExpansionError, 'reviewed main'):
                incremental.main()
        self.assertEqual(self.store.client.objects, before)
        self.assertFalse((self.root/'forbidden.json').exists())

    def test_explicit_same_day_generation_keeps_full_corpus_when_one_page_was_completed(self):
        doc = self.corpus['documents'][0]
        incremental.write_state(self.store, 'completed', 'fr', {'pages': {
            doc['url']: {'content_key': incremental.content_key(doc), 'generation': 'c'*64, 'candidate_id': 'd'*64}
        }}, DAY)
        args = ['test', 'prepare', '--generation', self.gen, '--locales', 'fr',
                '--corpus', str(self.root/'explicit.json'), '--github-output', str(self.root/'outputs')]
        with patch.dict(os.environ, ENV), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value=DAY), \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No collection')):
            self.assertEqual(incremental.main(), 0)
        self.assertEqual((self.root/'explicit.json').read_bytes(), stable_bytes(self.corpus))
        self.assertEqual(set(queue(self.store, 'fr')), {self.gen})
        self.assertEqual(read_origin(self.store, self.gen)['pages'], 2)
        self.assertIn('generation='+self.gen, (self.root/'outputs').read_text())
        self.assertIn('has_work=true', (self.root/'outputs').read_text())

    def test_workflow_preserves_global_serialization_budgets_and_exit75(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        for required in ("'extended-locales-r2-pipeline'", 'cancel-in-progress: false', 'max-parallel: 2',
                         "'14400'", 'timeout-minutes: 270', 'exit 75'):
            self.assertIn(required, workflow)
        inspection = (root/'.github/workflows/portal-extended-continuation-inspect.yml').read_text()
        self.assertNotIn('extended-locales-r2-pipeline', inspection)
        self.assertIn('/inspection.json', inspection)
        self.assertNotIn('setup_hymt', inspection)
        self.assertNotIn('actions: write', inspection)


if __name__ == '__main__':
    unittest.main()
