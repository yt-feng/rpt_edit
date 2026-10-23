"""Interrupted original provenance, using real fake-R2 objects and no model/API."""
import copy
import json
import os
import unittest
from unittest.mock import patch

import portal_extended_interrupted_origin as interrupted
import portal_extended_unstarted_claims as claims
from build_portal_extended_locales import build
from portal_extended_continuation import (acknowledge_published, partition_stopped_locales, pending,
    queue, read_origin, register, verify_origin_run)
from portal_extended_daily_queue import admit, prepare_queued, WORKFLOW as CAPTURE_WORKFLOW
from portal_extended_french_repair import RepairPipeline
from portal_extended_handoff import read_handoff, save_handoff
from portal_extended_incremental import remember_candidate, remember_checkpoint
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2StoreError
from review_portal_extended_handoff import producer_is_valid
import test_portal_extended_continuation as fixtures
from test_portal_extended_unstarted_claims import NEW, REPOSITORY, environment, failed_run, skipped_jobs

CAPTURE = {'run_id': '321', 'attempt': '1', 'sha': 'e'*40,
           'repository': REPOSITORY, 'workflow': CAPTURE_WORKFLOW}
PRODUCER, FakeTranslator, DAY = fixtures.PRODUCER, fixtures.FakeTranslator, fixtures.DAY


class InterruptedOriginTests(unittest.TestCase):
    def setUp(self):
        self.f = fixtures.ContinuationTests('test_fixture_keeps_original_actions_ownership_checks_enabled')
        self.f.setUp(); self.addCleanup(self.f.doCleanups)
        self.store, self.gen, self.root = self.f.store, self.f.gen, self.f.root
        self.admitted = admit(self.store, self.f.corpus['documents'], DAY, CAPTURE)
        self.assertEqual(prepare_queued(self.store, ('fr',))['generation'], self.gen)
        self.origin = register(self.store, self.f.corpus, ('fr',), PRODUCER)
        self.old_run, self.old_jobs = failed_run(PRODUCER), skipped_jobs(PRODUCER)
        self.capture_run = {**failed_run(CAPTURE), 'path': CAPTURE_WORKFLOW, 'conclusion': 'success'}
        self.capture_jobs = [{'id': 3211, 'name': 'source_snapshot', 'run_id': 321,
            'head_sha': CAPTURE['sha'], 'status': 'completed', 'conclusion': 'success',
            'started_at': DAY+'T01:00:00Z', 'completed_at': DAY+'T01:02:00Z'}]
        self.new_run = {**failed_run(NEW), 'conclusion': 'success'}
        self.new_jobs = [{**job, 'id': 7891+i, 'name': name, 'conclusion': 'success', 'runner_id': 1,
            'steps': [{'name': 'complete'}]} for i, (job, name) in enumerate(zip(
                skipped_jobs(NEW)+skipped_jobs(NEW)[:1], ('source', 'locale (fr)', 'publication_handoff')))]

    def api(self, path):
        run_id = path.split('/runs/')[1].split('/')[0]
        run, jobs = {'123': (self.old_run, self.old_jobs), '321': (self.capture_run, self.capture_jobs),
                     '789': (self.new_run, self.new_jobs)}[run_id]
        return copy.deepcopy({'total_count': len(jobs), 'jobs': jobs} if '/jobs?' in path else run)

    def transfer(self):
        scan = claims.UnstartedClaims(self.store, REPOSITORY, NEW, self.api)
        eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=scan)
        self.assertEqual((eligible, stopped), (('fr',), []))
        before = copy.deepcopy(queue(self.store, 'fr')[self.gen])
        pending(self.store, eligible, self.root/'source.json', unstarted=scan)
        self.assertIsNone(interrupted.read_proof(self.store, self.origin))
        with patch.dict(os.environ, environment()):
            self.assertEqual(scan.commit(), 1)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner': NEW})
        return interrupted.read_proof(self.store, self.origin)

    def complete(self):
        proof = self.transfer()
        checkpoint = self.root/'complete-checkpoint.json'
        output = self.root/'complete'
        build(self.f.corpus, 'fr', output, checkpoint, FakeTranslator(), allow_source_fallback=True)
        with patch.dict(os.environ, environment()):
            remember_checkpoint(self.store, 'fr', self.gen, checkpoint)
            remember_candidate(self.store, 'fr', self.f.corpus, output)
        self.assertEqual(interrupted.read_proof(self.store, self.origin), proof)
        row = queue(self.store, 'fr')[self.gen]
        batch = {'generation': self.gen, 'candidates': {'fr': row['snapshot']['candidate_id']}}
        receipt = read_handoff(self.store, save_handoff(self.store, batch, day=DAY, pages=2, producer=NEW))
        return proof, row, receipt

    def test_independent_capture_proof_keeps_owner_only_transfer_and_strict_default(self):
        proof = self.transfer()
        self.assertEqual(proof['admission_producer'], CAPTURE)
        self.assertEqual(read_origin(self.store, self.gen), self.origin)
        self.assertNotIn(NEW['run_id'], json.dumps(proof))
        self.assertEqual(interrupted.authenticate(self.store, self.origin, REPOSITORY, self.api), proof)
        with self.assertRaises(ExpansionError):
            verify_origin_run(self.origin, self.old_run, self.old_jobs, REPOSITORY)

    def test_failed_capture_incomplete_inventory_and_started_worker_never_write(self):
        original_capture, original_jobs = copy.deepcopy(self.capture_run), copy.deepcopy(self.old_jobs)
        cases = ('capture_failed', 'capture_wrong_sha', 'capture_source_failed', 'worker_started', 'inventory_missing')
        for case in cases:
            with self.subTest(case=case):
                self.capture_run, self.old_jobs = copy.deepcopy(original_capture), copy.deepcopy(original_jobs)
                self.capture_jobs[0]['conclusion'] = 'success'
                if case == 'capture_failed': self.capture_run['conclusion'] = 'failure'
                if case == 'capture_wrong_sha': self.capture_run['head_sha'] = 'f'*40
                if case == 'capture_source_failed': self.capture_jobs[0]['conclusion'] = 'failure'
                if case == 'worker_started': self.old_jobs[1]['runner_id'] = 10
                if case == 'inventory_missing': self.old_jobs.pop()
                before = copy.deepcopy(self.store.client.objects)
                eligible, stopped = partition_stopped_locales(self.store, ('fr',),
                    unstarted=claims.UnstartedClaims(self.store, REPOSITORY, NEW, self.api))
                self.assertEqual(eligible, ())
                self.assertEqual(stopped[0]['recovery_code'], 'original_source_unproved')
                self.assertEqual(self.store.client.objects, before)

    def test_changed_admission_missing_proof_and_changed_original_attempt_are_rejected(self):
        proof = self.transfer()
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaises(ExpansionError):
            interrupted.authenticate(self.store, {**self.origin, 'source_admission': 'f'*64}, REPOSITORY, self.api)
        self.old_run['run_attempt'] = 2
        with self.assertRaises(ExpansionError): interrupted.authenticate(self.store, self.origin, REPOSITORY, self.api)
        self.assertEqual(self.store.client.objects, before)
        self.old_run['run_attempt'] = 1
        self.store.client.objects.pop(interrupted.proof_key(self.store, self.origin))
        with self.assertRaisesRegex(ExpansionError, 'proof_missing'):
            interrupted.authenticate(self.store, self.origin, REPOSITORY, self.api, identity=digest(stable_bytes(proof)))

    def test_record_result_and_acknowledgement_keep_durable_exact_handoff_completion(self):
        proof, row, receipt = self.complete()
        self.assertEqual(receipt['interrupted_origin_sha256'], digest(stable_bytes(proof)))
        self.assertEqual(receipt['interrupted_origin_results'], {'fr': digest(stable_bytes(row))})
        before = copy.deepcopy(self.store.client.objects)
        actual = interrupted.authenticate_handoff(self.store, receipt, self.origin, REPOSITORY, self.api)
        producer_is_valid(receipt, self.new_run, self.new_jobs, REPOSITORY, origin=self.origin,
            original_run=self.old_run, original_jobs=self.old_jobs, interrupted_origin=actual)
        RepairPipeline().authenticate_original(self.store, self.origin, REPOSITORY, self.api)
        self.assertEqual(self.store.client.objects, before)
        acknowledge_published(self.store, ('fr',), [receipt['batch']])
        self.assertNotIn(self.gen, queue(self.store, 'fr'))
        self.assertEqual(interrupted.authenticate_handoff(self.store, receipt, self.origin, REPOSITORY, self.api), proof)
        RepairPipeline().authenticate_original(self.store, self.origin, REPOSITORY, self.api,
            snapshot=row['snapshot'], completed_row=row)

    def test_changed_real_batch_admission_cannot_borrow_persisted_origin_proof(self):
        self.transfer()
        other = admit(self.store, self.f.corpus['documents'], DAY, {**CAPTURE, 'run_id': '322'})
        key = self.store.key('batch-admissions', self.gen, 'receipt.json')
        current = json.loads(self.store._get(key, maximum=65536))
        current['admission'] = other['admission']
        self.store._put(key, stable_bytes(current), metadata={'kind': 'batch-admission'})
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'source admission differs'):
            interrupted.authenticate(self.store, self.origin, REPOSITORY, self.api)
        self.assertEqual(self.store.client.objects, before)

    def test_publication_needs_explicit_proof_exact_result_and_actual_completed_worker(self):
        proof, row, receipt = self.complete()
        for changes in ({'interrupted_origin_sha256': 'f'*64}, {'interrupted_origin_results': {}},
                        {'interrupted_origin_results': {'fr': 'e'*64}},
                        {'continuation_checkpoints': {'fr': 'f'*64}}):
            with self.subTest(changes=changes), self.assertRaises((ExpansionError, R2StoreError)):
                interrupted.authenticate_handoff(self.store, {**receipt, **changes}, self.origin, REPOSITORY, self.api)
        without = {key: value for key, value in receipt.items() if not key.startswith('interrupted_origin')}
        with self.assertRaises(ExpansionError):
            producer_is_valid(without, self.new_run, self.new_jobs, REPOSITORY, origin=self.origin,
                              original_run=self.old_run, original_jobs=self.old_jobs)
        with self.assertRaises(ExpansionError):
            producer_is_valid(receipt, self.new_run, self.new_jobs, REPOSITORY, origin=self.origin)
        for index in (0, 1):
            self.new_jobs[index]['conclusion'] = 'failure'
            before = copy.deepcopy(self.store.client.objects)
            with self.assertRaises(ExpansionError):
                interrupted.authenticate_handoff(self.store, receipt, self.origin, REPOSITORY, self.api)
            with self.assertRaises(ExpansionError):
                RepairPipeline().authenticate_original(self.store, self.origin, REPOSITORY, self.api)
            self.assertEqual(self.store.client.objects, before)
            self.new_jobs[index]['conclusion'] = 'success'

    def test_explicit_origin_scan_obeys_shared_api_bound_without_writes(self):
        scan = claims.UnstartedClaims(self.store, REPOSITORY, NEW, self.api)
        before = copy.deepcopy(self.store.client.objects)
        with patch.object(claims, 'MAX_API_READS', 3):
            eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=scan)
        self.assertEqual(eligible, ())
        self.assertEqual(stopped[0]['recovery_code'], 'recovery_api_scan_bound_reached')
        self.assertEqual(scan.api_reads, 3)
        self.assertEqual(self.store.client.objects, before)

    def test_replacement_failure_reuses_proof_without_resetting_started_allocation(self):
        proof = self.transfer()
        self.new_run, self.new_jobs = failed_run(NEW), skipped_jobs(NEW)
        following = {'run_id': '999', 'attempt': '1', 'sha': 'f'*40}
        scan = claims.UnstartedClaims(self.store, REPOSITORY, following, self.api)
        eligible, stopped = partition_stopped_locales(self.store, ('fr',), unstarted=scan)
        self.assertEqual((eligible, stopped), (('fr',), []))
        pending(self.store, eligible, self.root/'following.json', unstarted=scan)
        with patch.dict(os.environ, environment(following)):
            self.assertEqual(scan.commit(), 1)
        self.assertEqual(queue(self.store, 'fr')[self.gen],
            {'status': 'started', 'continuations': 0, 'owner': following})
        self.assertEqual(interrupted.read_proof(self.store, self.origin), proof)

    def test_origin_proof_before_queue_interruption_can_be_reused(self):
        scan = claims.UnstartedClaims(self.store, REPOSITORY, NEW, self.api)
        partition_stopped_locales(self.store, ('fr',), unstarted=scan)
        pending(self.store, ('fr',), self.root/'prepared.json', unstarted=scan)
        before = copy.deepcopy(queue(self.store, 'fr')[self.gen])
        with patch.dict(os.environ, environment()):
            with patch.object(claims, 'save_queue', side_effect=RuntimeError('queue interrupted')):
                with self.assertRaisesRegex(RuntimeError, 'queue interrupted'):
                    scan.commit()
            proof = interrupted.read_proof(self.store, self.origin)
            self.assertIsNotNone(proof)
            self.assertEqual(queue(self.store, 'fr')[self.gen], before)
            scan.commit()
        self.assertEqual(interrupted.read_proof(self.store, self.origin), proof)
        self.assertEqual(queue(self.store, 'fr')[self.gen], {**before, 'owner': NEW})

    def test_unrelated_source_audit_time_does_not_expire_interrupted_origin_api_budget(self):
        now = [0]
        def api(path):
            now[0] += 1
            return self.api(path)
        scan = claims.UnstartedClaims(self.store, REPOSITORY, NEW, api)
        scan.clock = lambda: now[0]
        partition_stopped_locales(self.store, ('fr',), unstarted=scan)
        pending(self.store, ('fr',), self.root/'timed.json', unstarted=scan)
        now[0] += 600
        with patch.dict(os.environ, environment()):
            self.assertEqual(scan.commit(), 1)
        self.assertEqual(scan.api_seconds, scan.api_reads)
        self.assertLess(scan.api_seconds, claims.MAX_API_SECONDS)

    def test_quality_consumer_cache_rechecks_latest_attempt_and_charges_each_read(self):
        from portal_extended_quality_recovery import cached_attempt_api, ScanBudget
        self.complete()
        calls = []
        def rerun(path):
            calls.append(path)
            result = self.api(path)
            if path.endswith('/runs/123') and calls.count(path) == 2:
                result['run_attempt'] = 2
            return result
        budget = ScanBudget()
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'owner_run_unproved'):
            RepairPipeline().authenticate_original(self.store, self.origin, REPOSITORY,
                                                   cached_attempt_api(rerun, budget))
        self.assertEqual(calls.count(f'repos/{REPOSITORY}/actions/runs/123'), 2)
        self.assertEqual(budget.api_reads, len(calls))
        self.assertEqual(self.store.client.objects, before)


if __name__ == '__main__':
    unittest.main(verbosity=2)
