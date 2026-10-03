"""Offline continuation/approval contracts with fake R2 and a fake translator."""
import copy
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, Mock, patch

from build_portal_extended_locales import build
from offline_translation import TranslationBudgetExceeded
from portal_extended_locales import ExpansionError, digest, make_corpus, stable_bytes
from portal_extended_r2 import R2Store, R2IntegrityError
import portal_extended_incremental as incremental
from portal_extended_continuation import (MAX_CONTINUATIONS, MAX_PENDING_GENERATIONS, adopt_existing,
    acknowledge_published, action_owner, pending, queue, read_origin, register, restore_claimed_checkpoint,
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
        # Model the original producer explicitly. A real CI runner's identity
        # must not leak into these synthetic checkpoints, and ownership checks
        # must stay enabled in both local and Actions test executions.
        environment = patch.dict(os.environ, {**ENV,
            'GITHUB_RUN_ID': PRODUCER['run_id'],
            'GITHUB_RUN_ATTEMPT': PRODUCER['attempt'], 'GITHUB_SHA': PRODUCER['sha']})
        environment.start(); self.addCleanup(environment.stop)
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

    def test_fixture_keeps_original_actions_ownership_checks_enabled(self):
        self.assertEqual(os.environ['GITHUB_ACTIONS'], 'true')
        self.assertEqual(action_owner(), PRODUCER)

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

    def test_handoff_drains_original_continuation_before_refreshed_admitted_source(self):
        import portal_extended_handoff as handoff
        from portal_extended_daily_queue import admit, prepare_queued, WORKFLOW
        from test_portal_extended_source_refresh import proof
        self.partial(); original_result = self.finish()
        origin_before = copy.deepcopy(read_origin(self.store, self.gen))
        original_batch = {'generation': self.gen,
                          'candidates': {'fr': original_result['candidate_id']}}
        newer_day = '2026-09-26'
        newer = [daily_doc(ORIGIN+'/blog/20260926-refresh.html', day=newer_day)]
        corpus = make_corpus(newer)
        admission = admit(self.store, newer, newer_day,
            {**PRODUCER, 'repository': 'example/repo', 'workflow': WORKFLOW},
            refresh=proof(newer, capture='2026-10-02'))
        prepared = prepare_queued(self.store, ('fr',))
        self.assertEqual(prepared['generation'], corpus['documents_sha256'])
        build(corpus, 'fr', self.root/'refreshed', self.root/'refreshed.json', FakeTranslator())
        refreshed = incremental.remember_candidate(self.store, 'fr', corpus, self.root/'refreshed')
        refreshed_batch = {'generation': corpus['documents_sha256'],
                           'candidates': {'fr': refreshed['candidate_id']}}
        self.assertIsNone(read_origin(self.store, corpus['documents_sha256']))
        pending_before = handoff.read_publication_batches(self.store)
        args = ['handoff', '--day', '2026-10-02', '--locales', 'fr', '--enabled-locales', 'fr']
        response = Mock(content=b'{}')
        response.json.return_value = {}
        session = MagicMock()
        session.__enter__.return_value = session
        session.get.return_value = response
        with patch.dict(os.environ, ENV), patch('sys.argv', args), \
             patch.object(handoff.R2Store, 'from_env', return_value=self.store), \
             patch.object(handoff.requests, 'Session', return_value=session), \
             patch.object(handoff, 'read_active_batches', return_value=self.active) as active, \
             patch.object(handoff.subprocess, 'run') as dispatch, \
             patch.object(handoff, 'next_ready_refresh', wraps=handoff.next_ready_refresh) as refresh:
            # Unknown original evidence must block, never select a newer corpus.
            origin_key = self.store.key('incremental', 'generation-origins', self.gen, 'receipt.json')
            original_object = copy.deepcopy(self.store.client.objects[origin_key])
            self.store.client.objects[origin_key]['body'] = b'corrupt'
            with self.assertRaises((R2IntegrityError, ValueError)):
                handoff.main()
            dispatch.assert_not_called(); refresh.assert_not_called()
            self.store.client.objects[origin_key] = original_object
            handoff.main()
            refresh.assert_not_called()
            command = dispatch.call_args.args[0]
            receipt = read_handoff(self.store, next(value.split('=', 1)[1] for value in command
                                                  if value.startswith('extended_handoff=')))
            self.assertEqual(receipt['batch'], original_batch)
            self.assertEqual(receipt['source_origin_sha256'], digest(stable_bytes(origin_before)))
            self.assertEqual(handoff.read_publication_batches(self.store), pending_before)
            active.return_value = self.active + [original_batch]
            handoff.main()
            self.assertEqual((dispatch.call_count, refresh.call_count), (2, 1))
            command = dispatch.call_args.args[0]
            receipt = read_handoff(self.store, next(value.split('=', 1)[1] for value in command
                                                  if value.startswith('extended_handoff=')))
            self.assertEqual(receipt['batch'], refreshed_batch)
            self.assertEqual(receipt['source_admission'], admission['admission'])
            self.assertEqual(receipt['source_day'], newer_day)
        self.assertEqual(queue(self.store, 'fr'), {})
        self.assertEqual(read_origin(self.store, self.gen), origin_before)
        self.assertEqual(handoff.read_publication_batches(self.store), pending_before)

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

    def test_quantity_inspection_emits_bounded_signatures_without_text(self):
        from inspect_portal_extended_continuation import quantity_diagnostics
        rows = {digest(str(number).encode()): {'source': 'Private source rose 50 basis points.',
                              'text': 'Private translated wording rose 50 percentage points.'}
                for number in range(25)}
        before = copy.deepcopy(rows)
        result = quantity_diagnostics({'rows': rows})
        self.assertEqual(rows, before)
        self.assertEqual(result['failed_unit_count'], 25)
        self.assertEqual(len(result['reported_units']), 20)
        first = result['reported_units'][0]
        self.assertEqual(first['source_quantities'], {'rows': [{'kind': 'percentage_points', 'values': ['0.5'], 'count': 1,
                                                             'value_truncated': False}], 'total_rows': 1, 'truncated': False})
        self.assertEqual(first['translated_quantities']['rows'][0]['values'], ['50'])
        self.assertNotIn('Private', json.dumps(result))
        self.assertEqual(quantity_diagnostics({'rows': {digest(b'valid'): {'source': '9月', 'text': 'en septembre'}}})['failed_unit_count'], 0)
        with self.assertRaisesRegex(ExpansionError, 'unit identity'):
            quantity_diagnostics({'rows': {'private-key': {'source': '9月', 'text': 'May'}}})
        huge = '9' * 500
        crowded = ' '.join([huge] + [str(n) for n in range(1, 80)])
        bounded = quantity_diagnostics({'rows': {digest(b'bounded'): {'source': crowded, 'text': '0'}}})['reported_units'][0]
        side = bounded['source_quantities']
        self.assertEqual(side['total_rows'], 80)
        self.assertEqual(len(side['rows']), 64)
        self.assertTrue(side['truncated'])
        self.assertEqual(len(side['rows'][0]['values'][0]), 128)
        self.assertTrue(side['rows'][0]['value_truncated'])

    def test_unit_alias_signals_normalize_invisible_separators_digits_and_word_order(self):
        from inspect_portal_extended_continuation import unit_alias_signals
        result = unit_alias_signals('Private ៥០ ចំណុច\u200bមូលដ្ឋាន; ពិន្ទុគោល ៧; 60 bps; 3 BPSPrivate')
        normalized = result['nfkc_no_invisible']
        self.assertTrue(normalized['khmer_point_base']['present'])
        self.assertEqual(normalized['khmer_point_base']['number_before_count'], 1)
        self.assertEqual(normalized['khmer_score_core']['number_after_count'], 1)
        self.assertEqual(normalized['english_bps']['number_before_count'], 1)
        self.assertFalse(normalized['english_bp']['present'])
        compact = unit_alias_signals('50 ចំ ណុច មូល ដ្ឋាន')['nfc_compact']
        self.assertEqual(compact['khmer_point_base']['number_before_count'], 1)
        self.assertNotIn('Private', json.dumps(result))
        self.assertNotIn('មូលដ្ឋាន', json.dumps(result))

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

    def prepare_main(self, locales='fr,pt', *, include_english=False):
        from contextlib import redirect_stdout
        import io
        output = self.root/'merge-outputs.txt'
        args = ['test', 'prepare', '--locales', locales, '--corpus', str(self.root/'merge-source.json'),
                '--github-output', str(output)]
        if include_english:
            args.append('--include-english')
        with patch.dict(os.environ, {**ENV, 'KC_PUBLIC_REPOSITORY': 'true'}), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value='2026-10-02'), \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No collection')), \
             redirect_stdout(io.StringIO()) as stdout:
            self.assertEqual(incremental.main(), 0)
        return json.loads(stdout.getvalue())

    def admitted_docs(self, count=26):
        from portal_extended_daily_queue import admit, WORKFLOW
        docs = [daily_doc(ORIGIN+f'/blog/20260925-{index:03}.html') for index in range(count)]
        admission = admit(self.store, docs, DAY, {**PRODUCER, 'repository':'example/repo', 'workflow':WORKFLOW})
        return docs, admission

    def mark_pages_complete(self, locale, docs):
        incremental.write_state(self.store, 'completed', locale, {'pages': {doc['url']: {
            'content_key': incremental.content_key(doc), 'generation': 'b'*64, 'candidate_id': 'c'*64}
            for doc in docs}}, DAY)

    def test_admitted_cold_start_keeps_each_independent_cursor_generation(self):
        from portal_extended_daily_queue import read_corpus
        docs, saved = self.admitted_docs()
        self.mark_pages_complete('fr', docs[:24])
        result = self.prepare_main()
        jobs = {job['locale']: job for job in json.loads(result['locale_jobs_json'])}
        self.assertEqual(result['generation'], '')
        self.assertNotEqual(jobs['fr']['generation'], jobs['pt']['generation'])
        for locale, expected in (('fr', 2), ('pt', 24)):
            generation = jobs[locale]['generation']
            self.assertEqual(len(read_corpus(self.store, generation)['documents']), expected)
            self.assertEqual(set(queue(self.store, locale)), {generation})
            self.assertEqual(queue(self.store, locale)[generation]['status'], 'started')
            self.assertEqual(read_origin(self.store, generation)['source_admission'], saved['admission'])
        self.assertEqual(json.loads(result['pending_counts_json']), {'fr': 2, 'pt': 26})

    def test_later_locale_can_first_consume_same_admitted_generation_without_claiming_ready(self):
        from portal_extended_daily_queue import prepare_queued, read_corpus
        self.admitted_docs(2)
        selected = prepare_queued(self.store, ('fr',))
        generation = selected['generation']; corpus = read_corpus(self.store, generation)
        first = register(self.store, corpus, ('fr',), PRODUCER)
        next_producer = {**PRODUCER, 'run_id':'124'}
        self.assertEqual(register(self.store, corpus, ('pt',), next_producer), first)
        self.assertEqual(queue(self.store, 'pt')[generation], {'status':'started','continuations':0,'owner':next_producer})
        self.assertEqual(read_origin(self.store, generation)['locales'], ['fr'])
        self.assertFalse(any('/ready.json' in key for key in self.store.client.objects))

    def test_admitted_cross_day_origin_requires_exact_admission_and_capture_proof(self):
        from portal_extended_daily_queue import prepare_queued, read_corpus, batch_admission, WORKFLOW
        from review_portal_extended_handoff import admission_is_valid
        self.admitted_docs(2)
        selected = prepare_queued(self.store, ('fr',)); generation = selected['generation']
        register(self.store, read_corpus(self.store, generation), ('fr',), PRODUCER)
        origin = read_origin(self.store, generation); admitted = batch_admission(self.store, generation)
        late_jobs = [{**self.jobs[0], 'started_at':'2026-10-02T01:00:00Z', 'completed_at':'2026-10-02T01:01:00Z'}]
        capture_run = {**self.run, 'path':WORKFLOW, 'conclusion':'success'}
        capture_jobs = [{**self.jobs[0], 'name':'source_snapshot'}]
        admission_is_valid(admitted, capture_run, capture_jobs, 'example/repo')
        verify_origin_run(origin, self.run, late_jobs, 'example/repo', admitted=admitted)
        for bad in (None, {**admitted,'admission':'e'*64}, {**admitted,'day':'2026-09-24'}):
            with self.assertRaises(ExpansionError):
                verify_origin_run(origin, self.run, late_jobs, 'example/repo', admitted=bad)
        for bad_run in ({**capture_run,'head_sha':'f'*40}, {**capture_run,'run_attempt':2}):
            with self.assertRaises(ExpansionError): admission_is_valid(admitted,bad_run,capture_jobs,'example/repo')
        with self.assertRaises(ExpansionError):
            admission_is_valid(admitted,capture_run,[{**capture_jobs[0], 'started_at':'2026-10-02T01:00:00Z',
                'completed_at':'2026-10-02T01:01:00Z'}],'example/repo')

    def test_real_pending_original_source_precedes_newer_admission_without_changing_it(self):
        from portal_extended_daily_queue import admit, read_queue, WORKFLOW
        self.partial(); original = stable_bytes(self.corpus)
        newer = [daily_doc(ORIGIN+'/blog/20260926-new.html', day='2026-09-26')]
        admit(self.store, newer, '2026-09-26', {**PRODUCER,'repository':'example/repo','workflow':WORKFLOW})
        before = copy.deepcopy(read_queue(self.store))
        result = self.prepare_main('fr')
        self.assertEqual(json.loads(result['locale_jobs_json']), [{'locale':'fr','generation':self.gen,'day':DAY}])
        self.assertEqual((self.root/'merge-source.json').read_bytes(), original)
        self.assertEqual(read_queue(self.store), before)
        self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], 1)

    def test_blocked_or_exhausted_neighbor_keeps_healthy_admitted_cursor_and_diagnostic(self):
        from portal_extended_continuation import partition_stopped_locales
        self.partial(locale='pt')
        docs, saved = self.admitted_docs(); self.mark_pages_complete('fr', docs[:24])
        base = queue(self.store, 'pt')
        for status, count in (('blocked', 1), ('incomplete', MAX_CONTINUATIONS), ('claimed', 1)):
            with self.subTest(status=status):
                # Reset only synthetic healthy locale state between independent scenarios.
                save_queue(self.store, 'fr', {})
                rows = copy.deepcopy(base)
                rows[self.gen].update(status=status, continuations=count, reason='Synthetic stopped outcome')
                if status == 'claimed': rows[self.gen]['owner'] = PRODUCER
                save_queue(self.store, 'pt', rows)
                before = copy.deepcopy(queue(self.store, 'pt'))
                result = self.prepare_main()
                jobs = json.loads(result['locale_jobs_json'])
                self.assertEqual([row['locale'] for row in jobs], ['fr'])
                self.assertEqual(read_origin(self.store, jobs[0]['generation'])['pages'], 2)
                diagnostic = json.loads(result['stopped_locales_json'])
                self.assertEqual(len(diagnostic), 1)
                self.assertEqual((diagnostic[0]['locale'], diagnostic[0]['model_calls']), ('pt',0))
                self.assertEqual(queue(self.store, 'pt'), before)
                self.assertEqual(json.loads(result['pending_counts_json']), {'fr':2,'pt':26})

    def test_stopped_but_corrupt_checkpoint_is_fatal_not_an_isolated_diagnostic(self):
        proof = self.partial(locale='pt')
        rows = queue(self.store, 'pt'); rows[self.gen]['status'] = 'blocked'; save_queue(self.store, 'pt', rows)
        self.admitted_docs()
        key = self.store.checkpoint_object_key('pt', self.gen, proof['checkpoint_sha256'])
        self.store.client.objects[key]['body'] = b'broken'
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaises((ExpansionError, R2IntegrityError)): self.prepare_main()
        self.assertEqual(self.store.client.objects, before)
        self.assertFalse((self.root/'merge-outputs.txt').exists())

    def test_all_stopped_cursors_report_without_collection_or_model_jobs(self):
        register(self.store, self.corpus, ('fr',), PRODUCER)
        before = copy.deepcopy(self.store.client.objects)
        result = self.prepare_main('fr')
        self.assertFalse(result['has_work'])
        self.assertEqual(json.loads(result['locale_jobs_json']), [])
        self.assertEqual(json.loads(result['stopped_locales_json'])[0]['status'], 'started')
        self.assertEqual(self.store.client.objects, before)

    def test_interrupted_claim_or_started_job_cannot_replay_another_actions_attempt(self):
        original_root = self.root
        for claimed in (False, True):
            with self.subTest(claimed=claimed):
                self.root = original_root/str(claimed); self.root.mkdir()
                save_queue(self.store, 'fr', {})
                self.partial()
                if claimed:
                    with patch.dict(os.environ, ENV): pending(self.store, ('fr',), self.root/'owner-source.json')
                    current = ENV
                else:
                    rows = queue(self.store, 'fr'); rows[self.gen] = {'status':'started','continuations':0,'owner':PRODUCER}
                    save_queue(self.store, 'fr', rows)
                    current = {**ENV,'GITHUB_RUN_ID':PRODUCER['run_id'],'GITHUB_SHA':PRODUCER['sha']}
                with patch.dict(os.environ, current):
                    restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'valid-owner.json')
                before = copy.deepcopy(self.store.client.objects)
                for changed in ({'GITHUB_RUN_ATTEMPT':'2'}, {'GITHUB_RUN_ID':'999'}, {'GITHUB_SHA':'f'*40}):
                    with patch.dict(os.environ, {**current,**changed}):
                        with self.assertRaisesRegex(ExpansionError, 'exact Actions attempt'):
                            restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'invalid-owner.json')
                        with self.assertRaisesRegex(ExpansionError, 'exact Actions attempt'):
                            incremental.remember_checkpoint(self.store, 'fr', self.gen, self.root/'fr-checkpoint.json')
                        with self.assertRaisesRegex(ExpansionError, 'exact Actions attempt'):
                            incremental.remember_candidate(self.store, 'fr', self.corpus, self.root/'fr-partial')
                    self.assertEqual(self.store.client.objects, before)
                self.assertFalse((self.root/'invalid-owner.json').exists())
                self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], int(claimed))

    def test_diagnostic_failure_has_no_dependency_edge_into_healthy_publication(self):
        workflow = (Path(__file__).resolve().parents[1]/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        diagnostic = workflow.split('\n  continuation_diagnostics:',1)[1].split('\n  locale:',1)[0]
        self.assertIn('raise SystemExit(', diagnostic)
        self.assertIn('permissions: {}', diagnostic)
        import re
        for job in ('locale','publication_handoff','continue_admitted_batches'):
            section = re.split(r'\n  [a-z_]+:', workflow.split('\n  '+job+':',1)[1], maxsplit=1)[0]
            self.assertNotIn('continuation_diagnostics', section)
        self.assertIn('needs: [source, locale]', workflow)
        self.assertIn('needs: [source, locale, publication_handoff]', workflow)


    def test_pending_continuation_keeps_english_admission_and_original_approval_scope(self):
        self.partial()
        original = stable_bytes(self.corpus)
        english = {'job': {'locale': 'en', 'generation': 'e'*64, 'day': '2026-10-01'},
                   'admission': 'f'*64, 'pending_count': 25, 'selected_pages': 24}
        with patch('portal_english_pipeline.prepare_queued', return_value=english):
            result = self.prepare_main('fr', include_english=True)
        self.assertEqual(json.loads(result['locale_jobs_json']), [english['job'],
            {'locale': 'fr', 'generation': self.gen, 'day': DAY}])
        self.assertEqual(json.loads(result['locales_json']), ['fr'])
        self.assertEqual((self.root/'merge-source.json').read_bytes(), original)
        self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], 1)
        self.assertFalse(any('/continuations/en/' in key for key in self.store.client.objects))
        outputs = dict(line.split('=', 1) for line in (self.root/'merge-outputs.txt').read_text().splitlines())
        self.assertEqual(outputs['requested_locales'], 'fr')
        self.assertEqual(outputs['english_admission'], english['admission'])
        self.assertEqual(outputs['english_pending_count'], '25')
        self.assertEqual(json.loads(outputs['stopped_locales_json']), [])

    def test_english_can_advance_when_all_additional_locales_require_diagnosis(self):
        register(self.store, self.corpus, ('fr',), PRODUCER)
        before = copy.deepcopy(self.store.client.objects)
        english = {'job': {'locale': 'en', 'generation': 'e'*64, 'day': '2026-10-01'},
                   'admission': 'f'*64, 'pending_count': 2, 'selected_pages': 2}
        with patch('portal_english_pipeline.prepare_queued', return_value=english):
            result = self.prepare_main('fr', include_english=True)
        self.assertTrue(result['has_work'])
        self.assertEqual(json.loads(result['locale_jobs_json']), [english['job']])
        self.assertEqual(result['generation'], '')
        self.assertEqual(json.loads(result['locales_json']), [])
        self.assertEqual(json.loads(result['stopped_locales_json'])[0]['status'], 'started')
        self.assertEqual(self.store.client.objects, before)
        outputs = dict(line.split('=', 1) for line in (self.root/'merge-outputs.txt').read_text().splitlines())
        self.assertEqual(outputs['requested_locales'], 'fr')
        self.assertEqual(outputs['english_admission'], english['admission'])

    def test_workflow_executes_correct_checkpoint_route_for_english_continuation_and_diagnostics(self):
        import subprocess
        import textwrap
        workflow = (Path(__file__).resolve().parents[1]/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        section = workflow.split('      - name: Restore locale checkpoint from private R2\n', 1)[1]
        section = section.split('      - name:', 1)[0]
        script = textwrap.dedent(section.split('        run: |\n', 1)[1])
        # Run the actual workflow branch with shell builtins and a fake Python
        # command. An empty PATH rules out R2, models, or any external executable.
        commands = r'''python3() {
  printf '%s\n' "$@" > "$TRACE_FILE"
  printf '%s\n' '{"present": true}'
}
tee() { while IFS= read -r line; do printf '%s\n' "$line"; done; }
'''
        cases = [('en', 'candidate', 'portal_extended_r2.py', '--output'),
                 ('en', '', 'portal_extended_r2.py', '--output'),
                 ('fr', 'candidate', 'portal_extended_incremental.py', '--checkpoint'),
                 ('km', 'publication-resume', 'portal_extended_incremental.py', '--checkpoint'),
                 ('en', 'recovery-test', 'portal_extended_r2.py', '--output'),
                 ('fr', 'recovery-test', 'portal_extended_r2.py', '--output')]
        for index, (locale, operation, expected, output_flag) in enumerate(cases):
            with self.subTest(locale=locale, operation=operation):
                trace = self.root/f'route-{index}.txt'
                output = self.root/f'route-{index}-outputs.txt'
                environment = {'PATH': '', 'LOCALE': locale, 'REQUESTED_OPERATION': operation,
                    'SOURCE_GENERATION': 'd'*64,
                    'EXTENDED_R2_PREFIX': '_english-commentary/v1' if locale == 'en' else '_extended-locales/v1',
                    'RUNNER_TEMP': str(self.root), 'TRACE_FILE': str(trace),
                    'GITHUB_OUTPUT': str(output), 'GITHUB_STEP_SUMMARY': str(self.root/'summary')}
                run = subprocess.run(['/bin/bash', '--noprofile', '--norc'], input=commands+script,
                                     env=environment, text=True, capture_output=True, check=False)
                self.assertEqual(run.returncode, 0, run.stderr)
                arguments = trace.read_text().splitlines()
                self.assertEqual(arguments[:3], ['-B', 'scripts/'+expected, 'restore-checkpoint'])
                self.assertEqual(arguments[arguments.index('--locale')+1], locale)
                self.assertEqual(arguments[arguments.index('--prefix')+1], environment['EXTENDED_R2_PREFIX'])
                self.assertIn(output_flag, arguments)
                self.assertEqual(output.read_text(), 'present=true\n')


if __name__ == '__main__':
    unittest.main()
