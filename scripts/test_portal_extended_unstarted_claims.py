"""Exact GitHub inventory and real fake-R2 claim transfers; no live APIs/models."""
import copy
import json
import os
from unittest.mock import patch
import unittest

import portal_extended_unstarted_claims as recovery
import portal_extended_incremental as incremental
from portal_extended_continuation import (partition_stopped_locales, pending, queue, register,
    require_active_owner, restore_claimed_checkpoint, save_queue)
from portal_extended_locales import ExpansionError, stable_bytes
from portal_extended_r2 import R2TransportError
import test_portal_extended_continuation as fixtures

OLD = {'run_id':'456', 'attempt':'1', 'sha':'c'*40}
NEW = {'run_id':'789', 'attempt':'1', 'sha':'d'*40}
REPOSITORY = 'example/repo'


def environment(owner=NEW):
    return {**fixtures.ENV, 'GITHUB_RUN_ID':owner['run_id'], 'GITHUB_RUN_ATTEMPT':owner['attempt'],
        'GITHUB_SHA':owner['sha'], 'GITHUB_EVENT_NAME':'workflow_dispatch', 'KC_PUBLIC_REPOSITORY':'true',
        'GITHUB_WORKFLOW_REF':REPOSITORY+'/'+recovery.WORKFLOW+'@refs/heads/main'}


def failed_run(owner):
    return {'id':int(owner['run_id']), 'run_attempt':int(owner['attempt']), 'head_sha':owner['sha'],
        'status':'completed', 'conclusion':'cancelled', 'path':recovery.WORKFLOW,
        'head_branch':'main', 'event':'workflow_run',
        'repository':{'full_name':REPOSITORY, 'private':False}, 'head_repository':{'full_name':REPOSITORY}}


def skipped_jobs(owner):
    common = {'run_id':int(owner['run_id']), 'head_sha':owner['sha'], 'status':'completed',
        'started_at':'2026-10-23T00:20:00Z', 'completed_at':'2026-10-23T00:20:00Z'}
    return [{**common, 'id':int(owner['run_id'])*10+1, 'name':'source', 'conclusion':'cancelled',
             'runner_id':1, 'steps':[{'name':'prepare','conclusion':'cancelled'}]},
            {**common, 'id':int(owner['run_id'])*10+2, 'name':'locale (${{ matrix.locale }})',
             'conclusion':'skipped', 'runner_id':None, 'steps':[]}]


class UnstartedClaimTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ContinuationTests('test_fixture_keeps_original_actions_ownership_checks_enabled')
        self.f.setUp()
        self.addCleanup(self.f.doCleanups)
        self.store, self.gen, self.root = self.f.store, self.f.gen, self.f.root
        self.origin_run = copy.deepcopy(self.f.run)
        self.origin_jobs = [{**job, 'id':i+1, 'run_id':123, 'head_sha':fixtures.PRODUCER['sha']}
                            for i, job in enumerate(self.f.jobs)]
        self.runs = {'456':failed_run(OLD)}
        self.jobs = {'456':skipped_jobs(OLD)}
        self.checks = {}
        self.calls = []

    def api(self, path):
        self.calls.append(path)
        if '/check-suites/' in path:
            return copy.deepcopy(self.checks[path.split('/check-suites/')[1].split('/')[0]])
        run_id = path.split('/runs/')[1].split('/')[0]
        if run_id == '123':
            run, jobs = self.origin_run, self.origin_jobs
        else:
            run, jobs = self.runs[run_id], self.jobs[run_id]
        return copy.deepcopy({'total_count':len(jobs), 'jobs':jobs} if '/jobs?' in path else run)

    def claimed(self, count=1):
        self.f.partial()
        pending(self.store, ('fr',), self.root/'initial.json', producer=OLD)
        if count != 1:
            rows = queue(self.store, 'fr')
            rows[self.gen]['continuations'] = count
            save_queue(self.store, 'fr', rows)
        return copy.deepcopy(queue(self.store, 'fr')[self.gen])

    def scan(self, owner=NEW):
        return recovery.UnstartedClaims(self.store, REPOSITORY, owner, self.api)

    def stage(self, scan, locales=('fr',)):
        eligible, stopped = partition_stopped_locales(self.store, locales, unstarted=scan)
        self.assertEqual((eligible, stopped), (locales, []))
        return pending(self.store, eligible, self.root/'recovered.json', producer=scan.owner, unstarted=scan)

    def receipts(self):
        return {key:value for key,value in self.store.client.objects.items() if '/unstarted-claim-transfers/' in key}

    def terminal_worker(self, owner=OLD, locale='fr', conclusion='failure'):
        jobs = skipped_jobs(owner)
        jobs[0]['conclusion'] = 'success'
        jobs[1].update(name=f'locale ({locale})', conclusion=conclusion, runner_id=42,
            steps=[{'name':'Run bounded locale translation and retain timeout state', 'conclusion':'success'},
                   {'name':'Persist complete or incomplete candidate pages privately', 'conclusion':conclusion}])
        return jobs

    def missing_worker(self):
        register(self.store, self.f.corpus, ('fr',), fixtures.PRODUCER)
        rows = queue(self.store, 'fr'); rows[self.gen]['owner'] = OLD
        save_queue(self.store, 'fr', rows)
        self.runs['456'].update(conclusion='failure', check_suite_id=222)
        self.jobs['456'] = self.terminal_worker(locale='pt', conclusion='success')
        self.checks['222'] = {'total_count':len(self.jobs['456']), 'check_runs':[
            {'id':job['id'], 'name':job['name'], 'status':'completed', 'conclusion':job['conclusion'],
             'head_sha':OLD['sha'], 'check_suite':{'id':222}, 'app':{'slug':'github-actions'}}
            for job in self.jobs['456']]}
        return copy.deepcopy(rows[self.gen])

    def test_missing_initial_worker_requires_two_matching_complete_inventories_and_spends_one_retry(self):
        before = self.missing_worker(); original = copy.deepcopy(self.store.client.objects)
        scan = self.scan(); self.stage(scan)
        self.assertEqual(self.store.client.objects, original)
        with patch.dict(os.environ, environment()):
            self.assertEqual(scan.commit(), 1)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW, 'continuations':1})
        receipt = json.loads(next(iter(self.receipts().values()))['body'])
        self.assertEqual(receipt['policy'], recovery.INITIAL_REPLAY_POLICY)
        self.assertEqual(receipt['evidence']['missing_locale_job'], 'fr')
        self.assertEqual(receipt['evidence']['check_run_ids'], [4561, 4562])
        self.assertEqual(receipt['paid_provider_requests'], 0)
        with self.assertRaisesRegex(ExpansionError, 'missing_worker_replay_bound_reached'):
            recovery.transferred_row(queue(self.store, 'fr')[self.gen], OLD, receipt['evidence'], 'fr')

    def test_missing_worker_never_replays_if_checks_are_partial_changed_foreign_or_present(self):
        self.missing_worker(); original_checks = copy.deepcopy(self.checks['222'])
        variants = [lambda d:d.update(total_count=3),
                    lambda d:d['check_runs'][1].update(name='locale (fr)'),
                    lambda d:d['check_runs'][1].update(head_sha='e'*40),
                    lambda d:d['check_runs'][1].update(status='in_progress'),
                    lambda d:d['check_runs'][1].update(app={'slug':'other'}),
                    lambda d:d['check_runs'][1].update(check_suite={'id':333})]
        before = copy.deepcopy(self.store.client.objects)
        for mutate in variants:
            self.checks['222'] = copy.deepcopy(original_checks); mutate(self.checks['222'])
            self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())
            self.assertEqual(self.store.client.objects, before)

    def test_a_new_check_record_before_commit_prevents_missing_worker_transfer(self):
        self.missing_worker(); scan = self.scan(); self.stage(scan)
        self.checks['222']['total_count'] += 1
        before = copy.deepcopy(self.store.client.objects)
        with patch.dict(os.environ, environment()), self.assertRaises(ExpansionError):
            scan.commit()
        self.assertEqual(self.store.client.objects, before)

    def test_candidate_tail_failure_recovers_exact_snapshot_with_a_new_bounded_attempt(self):
        from build_portal_extended_locales import build
        from test_portal_extended_locales import FakeTranslator
        before = self.claimed()
        checkpoint = self.root/'failed-worker-checkpoint.json'
        with patch.dict(os.environ, environment(OLD)):
            restore_claimed_checkpoint(self.store, 'fr', self.gen, checkpoint)
            output = self.root/'failed-worker-candidate'
            self.assertEqual(build(self.f.corpus, 'fr', output, checkpoint, FakeTranslator())['status'],
                             'complete-candidate')
            incremental.remember_checkpoint(self.store, 'fr', self.gen, checkpoint)
            with patch('portal_extended_continuation.record_result', side_effect=R2TransportError('serviceunavailable')):
                with self.assertRaises(R2TransportError):
                    incremental.remember_candidate(self.store, 'fr', self.f.corpus, output)
        self.assertEqual(queue(self.store, 'fr')[self.gen], before)
        self.jobs['456'] = self.terminal_worker()
        scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()):
            self.assertEqual(scan.commit(), 1)
            self.assertEqual(scan.commit(), 1)
            restored = restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'recovered-checkpoint.json')
        self.assertEqual(restored['sha256'], before['snapshot']['checkpoint_sha256'])
        after = queue(self.store, 'fr')[self.gen]
        self.assertEqual(after, {**before, 'owner':NEW, 'continuations':2})
        receipt = json.loads(next(iter(self.receipts().values()))['body'])
        self.assertEqual(receipt['policy'], recovery.TERMINAL_POLICY)
        self.assertEqual(receipt['evidence']['terminal_locale_job_id'], 4562)

    def test_terminal_worker_requires_exact_failed_locale_and_completed_owner(self):
        before = self.claimed()
        for changed in ({'name':'locale (pt)'}, {'conclusion':'success'}, {'conclusion':'skipped'},
                        {'status':'in_progress'}, {'runner_id':None}, {'steps':[]}):
            with self.subTest(changed=changed):
                self.jobs['456'] = self.terminal_worker()
                self.jobs['456'][1].update(changed)
                self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())
                self.assertEqual(queue(self.store, 'fr')[self.gen], before)
        self.jobs['456'] = self.terminal_worker()
        self.runs['456']['status'] = 'in_progress'
        self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())
        self.assertEqual(self.receipts(), {})

    def test_terminal_worker_recovery_never_resets_or_exceeds_continuation_bound(self):
        self.claimed(count=3)
        self.jobs['456'] = self.terminal_worker()
        before = copy.deepcopy(self.store.client.objects)
        stopped = partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[1]
        self.assertEqual(stopped[0]['recovery_code'], 'terminal_worker_continuation_bound_reached')
        self.assertEqual(self.store.client.objects, before)

    def test_exact_publication_resume_recovers_only_registered_generation_without_collection(self):
        before = self.claimed()
        self.jobs['456'] = self.terminal_worker()
        output = self.root/'explicit-source.json'
        args = ['test', 'prepare-publication', '--generation', self.gen, '--locales', 'fr',
                '--corpus', str(output)]
        with patch.dict(os.environ, environment()), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value='2026-11-05'), \
             patch('review_portal_extended_handoff.api', side_effect=self.api), \
             patch.object(incremental, 'include_english_matrix', side_effect=AssertionError('No English planning')), \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No new collection')):
            self.assertEqual(incremental.main(), 0)
        self.assertEqual(output.read_bytes(), stable_bytes(self.f.corpus))
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW, 'continuations':2})

    def test_cancelled_and_timed_out_workers_charge_one_attempt_and_recheck_evidence(self):
        self.claimed()
        for conclusion in ('cancelled', 'timed_out'):
            with self.subTest(conclusion=conclusion):
                self.jobs['456'] = self.terminal_worker(conclusion=conclusion)
                scan = self.scan(); self.stage(scan)
                self.jobs['456'][1]['conclusion'] = 'success'
                state = copy.deepcopy(self.store.client.objects)
                with patch.dict(os.environ, environment()), self.assertRaises(ExpansionError):
                    scan.commit()
                self.assertEqual(self.store.client.objects, state)

    def test_claimed_transfer_keeps_snapshot_counter_origin_and_exact_checkpoint(self):
        before = self.claimed()
        origin = copy.deepcopy(self.store.client.objects)
        scan = self.scan()
        self.assertTrue(self.stage(scan)['has_work'])
        self.assertEqual(queue(self.store, 'fr')[self.gen], before)
        self.assertEqual(self.receipts(), {})
        with patch.dict(os.environ, environment()):
            with self.assertRaises(ExpansionError):
                require_active_owner(self.store, 'fr', self.gen)
            self.assertEqual(scan.commit(), 1)
            require_active_owner(self.store, 'fr', self.gen)
            restored = restore_claimed_checkpoint(self.store, 'fr', self.gen, self.root/'exact.json')
            self.assertEqual(restored['sha256'], before['snapshot']['checkpoint_sha256'])
            self.assertEqual(scan.commit(), 1)  # Same prepared transfer is idempotent.
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW})
        self.assertEqual(len(self.receipts()), 1)
        for key,value in origin.items():
            if '/continuations/' not in key:
                self.assertEqual(self.store.client.objects[key], value)
        receipt = json.loads(next(iter(self.receipts().values()))['body'])
        self.assertEqual(receipt['before'], before)
        self.assertEqual(receipt['after'], {**before, 'owner':NEW})
        self.assertEqual(receipt['paid_provider_requests'], 0)

    def test_last_allocated_continuation_does_not_spend_another_attempt(self):
        before = self.claimed(count=3)
        scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()): scan.commit()
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW})

    def test_started_allocation_with_valid_original_source_stays_started_zero(self):
        register(self.store, self.f.corpus, ('fr',), fixtures.PRODUCER)
        rows = queue(self.store, 'fr'); rows[self.gen]['owner'] = OLD; save_queue(self.store, 'fr', rows)
        before = copy.deepcopy(rows[self.gen])
        scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()): scan.commit()
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW})
        self.assertNotIn('snapshot', queue(self.store, 'fr')[self.gen])

    def test_cancelled_matrix_recovers_unused_jobs_and_one_interrupted_first_attempt(self):
        locales = ('fr', 'pt', 'es', 'de')
        register(self.store, self.f.corpus, locales, fixtures.PRODUCER)
        for locale in locales:
            rows = queue(self.store, locale)
            rows[self.gen]['owner'] = OLD
            save_queue(self.store, locale, rows)
        jobs = self.terminal_worker(locale='fr', conclusion='cancelled')
        common = {'run_id':456, 'head_sha':OLD['sha'], 'status':'completed'}
        jobs[1]['steps'] = [
            {'name':recovery.TRANSLATE_STEP, 'started_at':'2026-10-23T00:25:00Z', 'conclusion':None},
            *({'name':name, 'started_at':None, 'completed_at':None, 'conclusion':None}
              for name in recovery.PERSIST_STEPS),
        ]
        jobs += [
            {**common, 'id':4563, 'name':'locale (pt)', 'conclusion':'cancelled',
             'runner_id':None, 'runner_name':None, 'steps':[]},
            {**common, 'id':4564, 'name':'locale (es)', 'conclusion':'success',
             'runner_id':42, 'steps':[{'name':recovery.TRANSLATE_STEP, 'conclusion':'success'}]},
            {**common, 'id':4565, 'name':'locale (de)', 'conclusion':'cancelled',
             'runner_id':42, 'steps':[jobs[1]['steps'][0], jobs[1]['steps'][1],
                                     {**jobs[1]['steps'][2], 'started_at':'2026-10-23T00:26:00Z'}]},
        ]
        self.jobs['456'] = jobs
        scan = self.scan()
        eligible, stopped = partition_stopped_locales(self.store, locales, unstarted=scan)
        self.assertEqual(eligible, ('fr', 'pt'))
        self.assertEqual([row['locale'] for row in stopped], ['es', 'de'])
        self.assertEqual(self.calls.count(f'repos/{REPOSITORY}/actions/runs/456/attempts/1/jobs?per_page=100'), 1)
        pending(self.store, eligible, self.root/'recovered.json', producer=NEW, unstarted=scan)
        with patch.dict(os.environ, environment()):
            self.assertEqual(scan.commit(), 2)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {'status':'started','continuations':1,'owner':NEW})
        self.assertEqual(queue(self.store, 'pt')[self.gen], {'status':'started','continuations':0,'owner':NEW})
        self.assertEqual(queue(self.store, 'es')[self.gen]['owner'], OLD)
        policies = {json.loads(record['body'])['locale']:json.loads(record['body'])['policy']
                    for record in self.receipts().values()}
        self.assertEqual(policies, {'fr':recovery.INITIAL_REPLAY_POLICY, 'pt':recovery.POLICY})

        self.runs['789'] = failed_run(NEW)
        self.jobs['789'] = [{**job, 'run_id':789, 'head_sha':NEW['sha']} for job in jobs]
        following = self.scan({'run_id':'999', 'attempt':'1', 'sha':'e'*40})
        eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=following)
        self.assertEqual(eligible, ())
        self.assertEqual(stopped[0]['recovery_code'], 'initial_worker_replay_bound_reached')

    def test_failed_original_source_stays_blocked_before_any_model_or_write(self):
        self.claimed()
        self.origin_run['conclusion'] = 'cancelled'
        self.origin_jobs[0]['conclusion'] = 'cancelled'
        before = copy.deepcopy(self.store.client.objects)
        eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())
        self.assertEqual(eligible, ())
        self.assertEqual(stopped[0]['recovery_code'], 'original_source_unproved')
        self.assertEqual(self.store.client.objects, before)
        self.assertFalse(any('/runs/456' in path for path in self.calls))

    def test_latest_attempt_repo_sha_branch_workflow_and_terminal_state_are_required(self):
        before = self.claimed()
        cases = [('run_attempt',2), ('head_sha','e'*40), ('head_branch','other'), ('status','in_progress'),
                 ('path','.github/workflows/other.yml'), ('conclusion','success'), ('event','pull_request'),
                 ('repository',{'full_name':'foreign/repo','private':False}),
                 ('repository',{'full_name':REPOSITORY,'private':True}),
                 ('head_repository',{'full_name':'foreign/repo'})]
        for field,value in cases:
            with self.subTest(field=field, value=value):
                self.runs['456'] = {**failed_run(OLD), field:value}
                eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())
                self.assertEqual(eligible, ())
                self.assertIn('recovery_code', stopped[0])
                self.assertEqual(queue(self.store, 'fr')[self.gen], before)
        self.assertEqual(self.receipts(), {})

    def test_incomplete_duplicate_and_started_job_inventories_never_transfer(self):
        before = self.claimed()
        cases = []
        for change in ({'runner_id':42}, {'runner_name':'assigned-runner'}, {'steps':[{'name':'checkout'}]}, {'conclusion':'cancelled'},
                       {'conclusion':'success'}, {'status':'in_progress'}):
            jobs = skipped_jobs(OLD); jobs[1].update(change); cases.append(jobs)
        jobs = skipped_jobs(OLD); jobs[0]['conclusion']='success'; cases.append(jobs)
        jobs = skipped_jobs(OLD); jobs[1]['id']=jobs[0]['id']; cases.append(jobs)
        jobs = skipped_jobs(OLD); jobs[1]['head_sha']='f'*40; cases.append(jobs)
        cases.extend([skipped_jobs(OLD)[:1], skipped_jobs(OLD)*51])
        for jobs in cases:
            with self.subTest(jobs=jobs[:2]):
                self.jobs['456'] = jobs
                self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())
                self.assertEqual(queue(self.store, 'fr')[self.gen], before)
        self.jobs['456'] = skipped_jobs(OLD)
        original = self.api
        def truncated(path):
            value = original(path)
            if '/runs/456/' in path and '/jobs?' in path: value['total_count'] += 1
            return value
        with patch.object(self, 'api', side_effect=truncated):
            self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())

    def test_latest_rerun_during_job_read_and_api_failure_are_not_evidence(self):
        self.claimed()
        original = self.api
        def newer_attempt(path):
            value = original(path)
            if path.endswith('/runs/456') and self.calls.count(path) == 2: value['run_attempt'] = 2
            return value
        with patch.object(self, 'api', side_effect=newer_attempt):
            self.assertEqual(partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[0], ())
        def unavailable(path):
            if '/runs/456' in path: raise RuntimeError('private transport details')
            return original(path)
        with patch.object(self, 'api', side_effect=unavailable):
            stopped = partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())[1]
        self.assertEqual(stopped[0]['recovery_code'], 'owner_api_unavailable')
        self.assertNotIn('private', json.dumps(stopped))
        self.assertEqual(self.receipts(), {})

    def test_corrupt_snapshot_remains_fatal_before_owner_proof(self):
        self.claimed()
        rows = queue(self.store, 'fr'); rows[self.gen]['snapshot']['resolved_units'] += 1
        save_queue(self.store, 'fr', rows)
        with self.assertRaises(ExpansionError):
            partition_stopped_locales(self.store, ('fr',), unstarted=self.scan())
        self.assertEqual(self.calls, [])

    def test_row_or_owner_attempt_change_after_staging_prevents_all_writes(self):
        self.claimed(); scan = self.scan(); self.stage(scan)
        self.runs['456']['run_attempt'] = 2
        before = copy.deepcopy(self.store.client.objects)
        with patch.dict(os.environ, environment()), self.assertRaises(ExpansionError): scan.commit()
        self.assertEqual(self.store.client.objects, before)
        self.runs['456']['run_attempt'] = 1
        rows = queue(self.store, 'fr'); rows[self.gen]['continuations'] = 2; save_queue(self.store, 'fr', rows)
        before = copy.deepcopy(self.store.client.objects)
        with patch.dict(os.environ, environment()), self.assertRaises(ExpansionError): scan.commit()
        self.assertEqual(self.store.client.objects, before)

    def test_receipt_before_queue_interruption_is_idempotently_resumed(self):
        before = self.claimed(); scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()):
            with patch.object(recovery, 'save_queue', side_effect=RuntimeError('interrupted')):
                with self.assertRaises(RuntimeError): scan.commit()
            self.assertEqual(len(self.receipts()), 1)
            self.assertEqual(queue(self.store, 'fr')[self.gen], before)
            scan.commit()
        self.assertEqual(len(self.receipts()), 1)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW})

    def test_repeated_source_interruption_requires_new_exact_owner_proof(self):
        before = self.claimed(); scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()): scan.commit()
        self.runs['789'], self.jobs['789'] = failed_run(NEW), skipped_jobs(NEW)
        following = {'run_id':'999', 'attempt':'1', 'sha':'e'*40}
        scan = self.scan(following); self.stage(scan)
        with patch.dict(os.environ, environment(following)): scan.commit()
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':following})
        self.assertEqual(len(self.receipts()), 2)

    def test_source_tail_failure_leaves_old_owner_and_success_commits_after_audits(self):
        before = self.claimed()
        args = ['test','prepare','--locales','fr','--corpus',str(self.root/'main.json')]
        def audit(_store, _locales):
            self.assertEqual(queue(self.store, 'fr')[self.gen], before)
            return {}
        with patch.dict(os.environ, environment()), patch('sys.argv',args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value='2026-10-23'), \
             patch('review_portal_extended_handoff.api', side_effect=self.api), \
             patch('portal_extended_quality_recovery.resume_prepared', return_value=[]), \
             patch('portal_extended_quality_recovery.pending_tail_locales', return_value=()), \
             patch('portal_extended_quality_recovery.prepare', return_value=([],[])), \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No new collection')):
            with patch('portal_extended_quality.quality_summary', side_effect=RuntimeError('tail interrupted')):
                with self.assertRaisesRegex(RuntimeError, 'tail interrupted'): incremental.main()
            self.assertEqual(queue(self.store, 'fr')[self.gen], before)
            self.assertEqual(self.receipts(), {})
            with patch('portal_extended_quality.quality_summary', side_effect=audit):
                self.assertEqual(incremental.main(), 0)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner':NEW})

    def test_for_source_rejects_nonserialized_context_before_api_or_storage(self):
        for changes in ({'GITHUB_REF':'refs/heads/other'}, {'GITHUB_EVENT_NAME':'push'},
                        {'KC_PUBLIC_REPOSITORY':'false'}, {'GITHUB_WORKFLOW_REF':'other'}):
            with patch.dict(os.environ, {**environment(), **changes}):
                self.assertIsNone(recovery.for_source(self.store, REPOSITORY, NEW, self.api))
        self.assertEqual(self.calls, [])

    def test_unrelated_six_hundred_second_gap_does_not_spend_api_budget(self):
        self.claimed(); scan = self.scan()
        with patch.object(scan, 'clock', return_value=0) as clock:
            self.stage(scan)
            clock.return_value = 600
            with patch.dict(os.environ, environment()): scan.commit()
        self.assertEqual(scan.api_seconds, 0)
        self.assertEqual(queue(self.store, 'fr')[self.gen]['owner'], NEW)

    def test_api_time_read_count_and_origin_count_are_bounded_before_writes(self):
        self.claimed()
        scan = self.scan()
        with patch.object(scan, 'clock', side_effect=[0, recovery.MAX_API_SECONDS]):
            stopped = partition_stopped_locales(self.store, ('fr',), unstarted=scan)[1]
        self.assertEqual(stopped[0]['recovery_code'], 'recovery_api_scan_bound_reached')
        self.assertEqual(scan.api_reads, 1)
        for limit, expected in [('api_reads', 'recovery_api_scan_bound_reached'),
                                ('origins', 'original_source_scan_bound_reached'),
                                ('owners', 'owner_scan_bound_reached')]:
            scan = self.scan()
            setattr(scan, limit, recovery.MAX_API_READS if limit == 'api_reads' else
                    {str(i):False for i in range(recovery.MAX_ORIGIN_LOOKUPS if limit == 'origins' else recovery.MAX_OWNER_RUNS)})
            stopped = partition_stopped_locales(self.store, ('fr',), unstarted=scan)[1]
            self.assertEqual(stopped[0]['recovery_code'], expected)
        self.assertEqual(self.receipts(), {})

    def started_pair(self):
        register(self.store, self.f.corpus, ('fr', 'pt'), fixtures.PRODUCER)
        for locale in ('fr', 'pt'):
            rows = queue(self.store, locale); rows[self.gen]['owner'] = OLD
            save_queue(self.store, locale, rows)
        scan = self.scan(); self.stage(scan, ('fr', 'pt'))
        return scan

    def test_all_rows_are_checked_before_first_transfer_write(self):
        scan = self.started_pair()
        rows = queue(self.store, 'pt'); rows[self.gen]['owner'] = fixtures.PRODUCER
        save_queue(self.store, 'pt', rows)
        before = copy.deepcopy(self.store.client.objects)
        with patch.dict(os.environ, environment()), self.assertRaises(ExpansionError): scan.commit()
        self.assertEqual(self.store.client.objects, before)

    def test_interruption_between_locales_resumes_without_extra_allocations(self):
        scan = self.started_pair()
        original = recovery.save_queue
        def interrupted(store, locale, rows):
            if locale == 'pt': raise RuntimeError('interrupted second locale')
            return original(store, locale, rows)
        with patch.dict(os.environ, environment()):
            with patch.object(recovery, 'save_queue', side_effect=interrupted):
                with self.assertRaises(RuntimeError): scan.commit()
            self.assertEqual(queue(self.store, 'fr')[self.gen]['owner'], NEW)
            self.assertEqual(queue(self.store, 'pt')[self.gen]['owner'], OLD)
            self.assertEqual(scan.commit(), 2)
        self.assertEqual(len(self.receipts()), 2)
        for locale in ('fr', 'pt'):
            self.assertEqual(queue(self.store, locale)[self.gen], {'status':'started','continuations':0,'owner':NEW})

    def test_already_transferred_owner_requires_its_immutable_receipt(self):
        self.claimed(); scan = self.scan(); self.stage(scan)
        with patch.dict(os.environ, environment()):
            scan.commit()
            self.store.client.objects.pop(next(iter(self.receipts())))
            with self.assertRaisesRegex(ExpansionError, 'transfer_receipt_missing'): scan.commit()


if __name__ == '__main__':
    unittest.main(verbosity=2)
