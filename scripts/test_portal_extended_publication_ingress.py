"""Durable event capture, strict attempt provenance and interrupted writer recovery."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import portal_extended_publication_ingress as ingress
import portal_extended_recovered_admission as recovered
from portal_extended_daily_queue import WORKFLOW, admit, read_admission, read_queue
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import R2Store, R2StoreError
from test_portal_extended_recovered_admission import fixture, RELEASE, CAPTURE, PRODUCER
from test_portal_extended_r2 import FakeR2
from test_portal_extended_incremental import daily_doc


class Storage(FakeR2):
    def __init__(self):
        super().__init__()
        self.fail_put = None
        self.fail_after_put = None
        self.fail_delete = False
        self.writes = []

    def put_object(self, **kwargs):
        path = kwargs['Key']
        if self.fail_put and self.fail_put(path):
            raise OSError('synthetic private failure')
        super().put_object(**kwargs)
        self.writes.append(path)
        if self.fail_after_put and self.fail_after_put(path):
            raise OSError('synthetic unknown outcome')

    def list_objects_v2(self, *, Bucket, Prefix, MaxKeys, ContinuationToken='0'):
        paths = sorted(k for k in self.objects if k.startswith(Prefix))
        start = int(ContinuationToken)
        page = paths[start:start+MaxKeys]
        more = start+len(page) < len(paths)
        return {'Contents': [{'Key': k} for k in page], 'IsTruncated': more,
                **({'NextContinuationToken': str(start+len(page))} if more else {})}

    def delete_object(self, *, Bucket, Key):
        if self.fail_delete:
            raise OSError('synthetic cleanup failure')
        self.objects.pop(Key, None)


class GitHub:
    repository = 'example/repo'

    def __init__(self, publication, *, daily=True):
        self.calls, self.unavailable = [], False
        self.runs, self.jobs, self.artifacts, self.values = {}, {}, {}, {}
        self.attempt_runs = {}
        self.add(publication, daily=daily)

    def base(self, identity, path, sha='a'*40, attempt=1, conclusion='success'):
        return {'id': identity, 'path': path, 'head_sha': sha, 'run_attempt': attempt,
                'status': 'completed', 'conclusion': conclusion, 'head_branch': 'main',
                'event': 'workflow_dispatch', 'repository': {'full_name': self.repository, 'private': False},
                'head_repository': {'full_name': self.repository}}

    def add(self, publication, *, daily=True):
        identity = int(publication['run_id'])
        path = recovered.DAILY_WORKFLOW if daily else recovered.WORKFLOW
        run = self.base(identity, path, publication['sha'])
        if daily:
            run.update(event='schedule', conclusion='failure')
        self.runs[identity] = run
        self.runs[400] = self.base(400, '.github/workflows/neutral-edge-cutover.yml', 'd'*40)
        prefix = recovered.DAILY_JOB_PREFIX if daily else ''
        self.jobs[identity, 1] = [self.job(identity, identity*10+i, prefix+stage, f'0{i}')
                                for i, stage in enumerate(ingress.STAGES, 1)]
        self.artifacts[identity] = []
        for i, kind in enumerate(('request', 'state'), 2):
            artifact_id = identity*100+i
            self.artifacts[identity].append({'id': artifact_id, 'name': f'recovered-publication-{kind}-{identity}',
                'expired': False, 'size_in_bytes': 2048, 'created_at': f'{CAPTURE}T0{i}:02:00Z'})
            self.values[artifact_id] = publication[kind]

    def job(self, identity, job_id, name, hour='01'):
        return {'id': job_id, 'name': name, 'run_id': identity, 'head_sha': 'a'*40,
            'status': 'completed', 'conclusion': 'success',
            'started_at': f'{CAPTURE}T{hour}:00:00Z', 'completed_at': f'{CAPTURE}T{hour}:05:00Z'}

    def producer(self, value=PRODUCER, conclusion='success'):
        identity = int(value['run_id'])
        self.runs[identity] = self.base(identity, WORKFLOW, value['sha'], int(value['attempt']), conclusion)
        self.runs[identity]['event'] = 'workflow_run'
        self.attempt_runs[identity, int(value['attempt'])] = copy.deepcopy(self.runs[identity])
        self.jobs[identity, int(value['attempt'])] = [self.job(identity, identity*10, 'source_snapshot', '06')]
        return value

    def api(self, suffix):
        self.calls.append(suffix)
        import re
        match = re.fullmatch(r'actions/runs/(\d+)', suffix)
        if match:
            identity = int(match[1])
            if self.unavailable and identity in self.artifacts:
                raise ExpansionError('synthetic_origin_unavailable')
            return copy.deepcopy(self.runs[identity])
        match = re.fullmatch(r'actions/runs/(\d+)/attempts/(\d+)', suffix)
        if match:
            identity, attempt = int(match[1]), int(match[2])
            run = self.runs[identity] if self.runs[identity]['run_attempt'] == attempt else self.attempt_runs[identity, attempt]
            return copy.deepcopy(run)
        match = re.fullmatch(r'actions/runs/(\d+)/attempts/(\d+)/jobs\?per_page=100(?:&page=(\d+))?', suffix)
        if match:
            rows = self.jobs[int(match[1]), int(match[2])]
            page = int(match[3] or 1)
            return copy.deepcopy({'total_count': len(rows), 'jobs': rows[(page-1)*100:page*100]})
        match = re.fullmatch(r'actions/runs/(\d+)/artifacts\?per_page=100', suffix)
        if match:
            rows = self.artifacts[int(match[1])]
            return copy.deepcopy({'total_count': len(rows), 'artifacts': rows})
        raise AssertionError(suffix)

    def artifact(self, identity, member):
        return copy.deepcopy(self.values[identity])

    def contains(self, base, head):
        return True


class IngressTests(unittest.TestCase):
    def setUp(self):
        self.client = Storage()
        self.store = R2Store(self.client, 'private', '_extended-locales/staging/ingress')
        self.publication, self.pages = fixture(2)
        self.gh = GitHub(self.publication)
        self.event = ingress.event_from_run(self.gh.runs[300], self.gh.repository)
        self.fetch = mock.patch.object(recovered, 'read_public', side_effect=lambda session, url: self.pages[url])
        self.edge = mock.patch.object(recovered, 'read_release', return_value=RELEASE)
        self.fetch.start(); self.edge.start()
        self.addCleanup(self.fetch.stop); self.addCleanup(self.edge.stop)

    def capture(self):
        return ingress.capture(self.store, self.gh, self.event)

    def reconcile(self, producer=PRODUCER):
        return ingress.reconcile(self.store, self.gh, object(), producer, CAPTURE)

    def finish(self, prior=PRODUCER, conclusion='success', next_id='322'):
        self.gh.producer(prior, conclusion)
        return self.reconcile({**PRODUCER, 'run_id': next_id})

    def test_failed_daily_chart_sibling_does_not_hide_successful_nested_publication(self):
        self.assertTrue(self.capture()['frozen'])
        value = ingress.load_group(self.store, ingress.event_id(self.event), next(iter(ingress.pending_inventory(self.store).values())))
        self.assertEqual(value['event']['path'], recovered.DAILY_WORKFLOW)
        self.assertEqual(value['evidence']['jobs']['deliver']['name'], recovered.DAILY_JOB_PREFIX+'deliver')
        self.assertNotIn('caller', value['publication'])
        first = self.reconcile()
        self.assertEqual(first['awaiting_producer_events'], 1)
        self.assertEqual(len(ingress.pending_inventory(self.store)), 1)
        self.assertFalse(any('/acks/' in key for key in self.client.objects))
        self.assertEqual(self.finish()['admitted_events'], 1)
        self.assertFalse(ingress.pending_inventory(self.store))
        self.assertEqual(len(recovered.read_queue(self.store)), 1)

    def test_frozen_receipts_survive_original_artifacts_and_attempt_replacement(self):
        self.capture()
        self.gh.runs[300]['run_attempt'] = 2
        self.gh.artifacts[300] = []
        self.gh.values.clear()
        self.gh.unavailable = True
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 1)
        self.assertEqual(self.finish()['admitted_events'], 1)

    def test_same_event_immutable_capture_is_idempotent_and_conflicting_head_cannot_split_key(self):
        self.capture(); original = copy.deepcopy(self.client.objects)
        self.capture(); self.assertEqual(original, self.client.objects)
        changed = {**self.event, 'head_sha': 'f'*40}
        self.assertEqual(ingress.event_id(self.event), ingress.event_id(changed))
        ingress.persist_envelope(self.store, changed)
        self.assertEqual(self.reconcile()['blocked_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), [])

    def test_hint_write_then_cancel_is_discovered_without_original_workflow_rerun(self):
        ingress.persist_envelope(self.store, self.event)
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 1)
        self.assertEqual(self.finish()['admitted_events'], 1)

    def test_hint_put_unknown_outcome_is_recovered_by_same_key_readback(self):
        self.client.fail_after_put = lambda key: '/pending/' in key
        with self.assertRaises(R2StoreError): self.capture()
        self.assertEqual(len(ingress.pending_inventory(self.store)), 1)
        self.client.fail_after_put = None
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 1)

    def test_full_envelope_put_unknown_retains_both_discoverable_objects(self):
        self.client.fail_after_put = lambda key: '/pending/' in key and len(self.client.writes) == 2
        with self.assertRaises(R2StoreError): self.capture()
        self.assertEqual(sum(map(len, ingress.pending_inventory(self.store).values())), 2)
        self.client.fail_after_put = None
        self.gh.unavailable = True
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 1)

    def test_job_name_attempt_artifact_window_and_identity_rejections_remain_pending(self):
        mutators = [
            lambda: self.gh.jobs[300, 1][0].update(name='other / generate'),
            lambda: self.gh.jobs[300, 1][1].update(conclusion='failure'),
            lambda: self.gh.jobs[300, 1][2].update(run_id=301),
            lambda: self.gh.artifacts[300][0].update(created_at=f'{CAPTURE}T01:02:00Z'),
            lambda: self.gh.artifacts[300][1].update(expired=True),
        ]
        for mutate in mutators:
            self.gh = GitHub(self.publication)
            mutate()
            with self.subTest(mutation=mutate):
                self.assertFalse(self.capture()['frozen'])
        self.assertEqual(recovered.read_queue(self.store), [])
        self.assertEqual(len(ingress.pending_inventory(self.store)), 1)

    def test_publish_only_new_attempt_binds_request_to_original_deliver_window(self):
        self.gh.runs[300]['run_attempt'] = 2
        newer = self.gh.job(300, 3999, recovered.DAILY_JOB_PREFIX+'publish', '04')
        self.gh.jobs[300, 2] = [newer]
        self.gh.artifacts[300][1]['created_at'] = f'{CAPTURE}T04:02:00Z'
        self.event['run_attempt'] = 2
        self.assertTrue(self.capture()['frozen'])
        value = ingress.load_group(self.store, ingress.event_id(self.event), next(iter(ingress.pending_inventory(self.store).values())))
        self.assertEqual(value['evidence']['jobs']['deliver']['attempt'], 1)
        self.assertEqual(value['evidence']['jobs']['publish']['attempt'], 2)

    def test_old_attempt_hint_never_binds_new_attempt_artifacts(self):
        ingress.persist_envelope(self.store, self.event)
        self.gh.runs[300]['run_attempt'] = 2
        self.assertEqual(self.reconcile()['blocked_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), [])
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_complete_paginated_job_list_and_duplicate_page_rejection(self):
        self.gh.jobs[300, 1] = [self.gh.job(300, 5000+i, 'other '+str(i)) for i in range(105)] + self.gh.jobs[300, 1]
        self.assertTrue(self.capture()['frozen'])
        self.assertIn('actions/runs/300/attempts/1/jobs?per_page=100&page=2', self.gh.calls)
        api = self.gh.api
        def duplicate(path):
            value = api(path)
            if '&page=2' in path:
                value['jobs'][0] = copy.deepcopy(self.gh.jobs[300, 1][0])
            return value
        self.gh.api = duplicate
        with self.assertRaises(ExpansionError): recovered.attempt_jobs(self.gh, '300', 1)

    def test_only_explicit_skipped_parent_without_artifacts_is_terminal(self):
        self.gh.artifacts[300] = []
        self.gh.jobs[300, 1] = []
        self.assertFalse(self.capture()['frozen'])
        parent = self.gh.job(300, 3900, 'deliver-recovered-report-articles')
        parent['conclusion'] = 'skipped'
        self.gh.jobs[300, 1] = [parent]
        self.assertTrue(self.capture()['frozen'])
        result = self.reconcile()
        self.assertEqual(result['no_work_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), [])
        self.assertFalse(ingress.pending_inventory(self.store))

    def test_skipped_parent_with_expired_publication_artifact_stays_pending(self):
        self.gh.jobs[300, 1] = [self.gh.job(300, 3900, 'deliver-recovered-report-articles')]
        self.gh.jobs[300, 1][0]['conclusion'] = 'skipped'
        self.gh.artifacts[300][0]['expired'] = True
        self.assertFalse(self.capture()['frozen'])
        self.assertEqual(self.reconcile()['blocked_events'], 1)

    def test_successful_empty_receipt_is_zero_translation_no_work(self):
        value, _ = fixture(0)
        self.gh = GitHub(value)
        self.assertTrue(self.capture()['frozen'])
        self.assertEqual(self.reconcile()['no_work_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), [])

    def test_skipped_new_attempt_cannot_erase_prior_executed_publication(self):
        self.gh.runs[300]['run_attempt'] = 2
        self.event['run_attempt'] = 2
        self.gh.jobs[300, 2] = copy.deepcopy(self.gh.jobs[300, 1])
        for row in self.gh.jobs[300, 2]:
            row['id'] += 1000
            row['conclusion'] = 'skipped'
        self.gh.artifacts[300] = []
        self.assertFalse(self.capture()['frozen'])
        self.assertEqual(self.reconcile()['blocked_events'], 1)

    def test_pending_writer_replacement_and_same_day_events_preserve_ordinary_queue(self):
        normal = daily_doc('https://kcdesk.com/blog/20261010-latest.html', day=CAPTURE)
        admit(self.store, [normal], CAPTURE, PRODUCER)
        normal_before = copy.deepcopy(read_queue(self.store))
        self.capture()  # Writer A is replaced before starting.
        second, pages = fixture(1, start=99)
        second['run_id'] = '301'; self.pages.update(pages)
        self.gh.add(second)
        ingress.capture(self.store, self.gh, ingress.event_from_run(self.gh.runs[301], self.gh.repository))
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 2)
        self.assertEqual(self.finish()['admitted_events'], 2)
        self.assertEqual(len(recovered.read_queue(self.store)), 2)
        self.assertEqual(read_queue(self.store), normal_before)

    def test_cancelled_producer_rebinds_exact_source_without_changing_old_receipt(self):
        self.capture(); self.reconcile()
        old_id = recovered.read_queue(self.store)[0]['admission']
        old_raw = self.store._get(self.store.key('source-admissions', old_id, 'receipt.json'), maximum=65536)
        newer = {**PRODUCER, 'run_id': '322'}
        self.gh.producer(PRODUCER, 'cancelled')
        self.assertEqual(self.reconcile(newer)['awaiting_producer_events'], 1)
        new_id = recovered.read_queue(self.store)[0]['admission']
        self.assertNotEqual(old_id, new_id)
        self.assertEqual(self.store._get(self.store.key('source-admissions', old_id, 'receipt.json'), maximum=65536), old_raw)
        self.assertEqual(read_admission(self.store, new_id)['generation'], read_admission(self.store, old_id)['generation'])
        self.assertTrue(ingress.pending_inventory(self.store))
        self.assertEqual(self.finish(newer, next_id='323')['admitted_events'], 1)

    def test_rebind_queue_written_claim_not_written_recovers_authoritative_queue(self):
        self.capture(); self.reconcile()
        newer = {**PRODUCER, 'run_id': '322'}
        self.gh.producer(PRODUCER, 'cancelled')
        self.client.fail_put = lambda key: '/recovered-publication-claims/' in key
        self.assertEqual(self.reconcile(newer)['blocked_events'], 1)
        queued_id = recovered.read_queue(self.store)[0]['admission']
        self.client.fail_put = None
        self.gh.producer(newer)
        self.assertEqual(self.finish(newer, next_id='323')['admitted_events'], 1)
        self.assertEqual(recovered.read_queue(self.store)[0]['admission'], queued_id)

    def test_ack_write_unknown_and_cleanup_failure_do_not_refetch_or_rebind(self):
        self.capture(); self.reconcile()
        self.gh.producer(PRODUCER)
        self.client.fail_after_put = lambda key: '/acks/' in key
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
        self.client.fail_after_put = None
        self.client.fail_delete = True
        with mock.patch.object(recovered, 'read_public', side_effect=AssertionError('must not fetch')):
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '323'})['blocked_events'], 1)
            self.client.fail_delete = False
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '324'})['retained_events'], 0)
        self.assertEqual(len(recovered.read_queue(self.store)), 1)

    def test_successful_original_producer_attempt_survives_later_failed_rerun_before_ack(self):
        self.capture(); self.reconcile(); self.gh.producer(PRODUCER)
        old_id = recovered.read_queue(self.store)[0]['admission']
        self.gh.producer({**PRODUCER, 'attempt': '2'}, 'failure')
        result = self.reconcile({**PRODUCER, 'run_id': '322'})
        self.assertEqual(result['admitted_events'], 1)
        self.assertEqual(recovered.read_queue(self.store)[0]['admission'], old_id)
        self.assertIn('actions/runs/321/attempts/1', self.gh.calls)

    def test_final_ack_cleanup_uses_successful_original_attempt_after_later_rerun_failure(self):
        self.capture(); self.reconcile(); self.gh.producer(PRODUCER)
        self.client.fail_delete = True
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
        self.gh.producer({**PRODUCER, 'attempt': '2'}, 'failure')
        self.client.fail_delete = False
        with mock.patch.object(recovered, 'read_public', side_effect=AssertionError('no collection')):
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '323'})['retained_events'], 0)

    def test_pruned_all_completed_cancelled_producer_claim_can_finish_without_requeue(self):
        from portal_extended_incremental import content_key, write_state
        from portal_extended_locales import ADDITIONAL
        from portal_extended_daily_queue import read_corpus
        from test_portal_extended_recovered_admission import capture as collect_fixture
        self.capture(); self.reconcile()
        old_id = recovered.read_queue(self.store)[0]['admission']
        old = read_admission(self.store, old_id)
        corpus = read_corpus(self.store, old['generation'])
        for locale in ADDITIONAL:
            write_state(self.store, 'completed', locale, {'pages': {doc['url']: {
                'content_key': content_key(doc), 'generation': 'b'*64, 'candidate_id': 'c'*64}
                for doc in corpus['documents']}}, old['day'])
        other, pages = fixture(1, start=999)
        other_corpus, other_proof = collect_fixture(other, pages)
        recovered.admit(self.store, other_corpus, other_proof, {**PRODUCER, 'run_id': '399'})
        queue_before = copy.deepcopy(recovered.read_queue(self.store))
        self.assertNotIn(old_id, [row['admission'] for row in queue_before])
        self.gh.producer(PRODUCER, 'cancelled')
        newer = {**PRODUCER, 'run_id': '322'}
        self.assertEqual(self.reconcile(newer)['awaiting_producer_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), queue_before)
        self.assertTrue(ingress.pending_inventory(self.store))
        self.assertEqual(self.finish(newer, next_id='323')['admitted_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), queue_before)

    def test_missing_queue_with_any_pending_locale_does_not_clear_failed_claim(self):
        from portal_extended_daily_queue import read_corpus, write_verified
        self.capture(); self.reconcile()
        write_verified(self.store, self.store.key('incremental', 'recovered-source-cohorts', 'queue.json'),
            {'schema_version': 1, 'policy': recovered.POLICY, 'entries': []}, kind='synthetic-invalid-prune')
        self.gh.producer(PRODUCER, 'cancelled')
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_rebinding_cancelled_producer_requires_fresh_exact_live_source(self):
        self.capture(); self.reconcile(); self.gh.producer(PRODUCER, 'cancelled')
        original = copy.deepcopy(recovered.read_queue(self.store))
        with mock.patch.object(recovered, 'read_public', return_value=b'changed source'):
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
        self.assertEqual(recovered.read_queue(self.store), original)
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_source_job_failure_or_unknown_exact_attempt_never_creates_final_ack(self):
        self.capture(); self.reconcile(); self.gh.producer(PRODUCER)
        self.gh.jobs[321, 1][0]['conclusion'] = 'failure'
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
        with mock.patch.object(self.gh, 'api', side_effect=ExpansionError('private transport detail')):
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '323'})['blocked_events'], 1)
        self.assertFalse(any('/acks/' in path for path in self.client.objects))
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_32_cohort_full_retains_unacknowledged_publication(self):
        self.capture()
        with mock.patch.object(recovered, 'MAX_COHORTS', 0):
            self.assertEqual(self.reconcile()['blocked_events'], 1)
        self.assertTrue(ingress.pending_inventory(self.store))
        self.assertFalse(any('/acks/' in path for path in self.client.objects))
        self.assertEqual(self.reconcile()['awaiting_producer_events'], 1)

    def test_failed_live_binding_and_unknown_producer_never_ack(self):
        self.capture()
        with mock.patch.object(recovered, 'read_public', return_value=b'wrong body'):
            self.assertEqual(self.reconcile()['blocked_events'], 1)
        self.reconcile()
        self.gh.producer(PRODUCER); self.gh.runs[321]['status'] = 'in_progress'
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['awaiting_producer_events'], 1)
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_budget_rotation_reaches_later_event_and_listing_truncation_is_not_empty(self):
        for identity in range(300, 310):
            ingress.persist_envelope(self.store, {**self.event, 'id': identity})
        with mock.patch.object(ingress, 'capture', return_value={'frozen': False}):
            self.assertEqual(self.reconcile()['checked_events'], 8)
            first = {key for key in self.client.objects if '/turns/' in key}
            self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['checked_events'], 8)
            self.assertGreater(len({key for key in self.client.objects if '/turns/' in key}), len(first))
        with mock.patch.object(self.client, 'list_objects_v2', return_value={'Contents': [], 'IsTruncated': True}):
            with self.assertRaises(ExpansionError): ingress.pending_inventory(self.store)
        with mock.patch.object(ingress, 'MAX_PENDING', 1):
            with self.assertRaises(ExpansionError): ingress.pending_inventory(self.store)

    def test_deadline_stops_before_next_event_without_dropping_pending(self):
        self.capture()
        with mock.patch.object(recovered, 'collect') as collect:
            with self.assertRaises((ExpansionError, R2StoreError)):
                ingress.reconcile(self.store, self.gh, object(), PRODUCER, CAPTURE, clock=mock.Mock(side_effect=[0, 1201]))
        collect.assert_not_called()
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_deadline_covers_listing_and_turn_reads_before_any_new_transaction(self):
        self.capture()
        for operation in ('list_objects_v2', 'get_object'):
            now = [0.0]
            original = getattr(self.client, operation)
            def slow(**kwargs):
                value = original(**kwargs)
                if operation == 'list_objects_v2' or '/turns/' in kwargs['Key']:
                    now[0] = 1201.0
                return value
            # Populate an old turn to exercise the actual successful GET path.
            turn = ingress.key(self.store, 'turns', ingress.event_id(self.event)+'.json')
            from portal_extended_daily_queue import write_verified
            write_verified(self.store, turn, {'run_id': 1, 'attempt': 1}, kind='test-turn')
            with self.subTest(operation=operation), mock.patch.object(self.client, operation, side_effect=slow), \
                 mock.patch.object(recovered, 'collect') as collect, self.assertRaises((ExpansionError, R2StoreError)):
                ingress.reconcile(self.store, self.gh, object(), PRODUCER, CAPTURE, clock=lambda: now[0])
            collect.assert_not_called()
            self.assertEqual(recovered.read_queue(self.store), [])
            self.assertTrue(ingress.pending_inventory(self.store))

    def test_deadline_after_queue_write_retains_pending_and_recovers_without_claim(self):
        self.capture()
        now = [0.0]
        original = self.client.put_object
        def slow(**kwargs):
            value = original(**kwargs)
            if '/recovered-source-cohorts/' in kwargs['Key']:
                now[0] = 1201.0
            return value
        with mock.patch.object(self.client, 'put_object', side_effect=slow):
            result = ingress.reconcile(self.store, self.gh, object(), PRODUCER, CAPTURE, clock=lambda: now[0])
        self.assertEqual(result['blocked_events'], 1)
        self.assertFalse(any('/recovered-publication-claims/' in k for k in self.client.objects))
        self.assertTrue(ingress.pending_inventory(self.store))
        self.gh.producer(PRODUCER)
        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['admitted_events'], 1)

    def test_every_initial_admission_write_interruption_retains_discoverable_request(self):
        self.capture()
        captured = copy.deepcopy(self.client.objects)
        self.client.writes.clear(); self.reconcile()
        writes = [k for k in self.client.writes if '/turns/' not in k]
        self.assertGreaterEqual(len(writes), 4)
        for target in writes:
            for after in (False, True):
                with self.subTest(path=target, after=after):
                    self.client.objects = copy.deepcopy(captured)
                    self.client.fail_put = None; self.client.fail_after_put = None
                    setattr(self.client, 'fail_after_put' if after else 'fail_put', lambda key: key == target)
                    self.assertEqual(self.reconcile()['blocked_events'], 1)
                    self.assertTrue(ingress.pending_inventory(self.store))
                    self.client.fail_put = None; self.client.fail_after_put = None
                    self.gh.producer(PRODUCER, 'cancelled')
                    newer = {**PRODUCER, 'run_id': '322'}
                    self.assertEqual(self.reconcile(newer)['awaiting_producer_events'], 1)
                    self.assertEqual(self.finish(newer, next_id='323')['admitted_events'], 1)
                    self.assertEqual(len(recovered.read_queue(self.store)), 1)

    def test_every_rebind_write_interruption_recovers_without_old_failed_claim_lock(self):
        self.capture(); self.reconcile()
        original = copy.deepcopy(self.client.objects)
        self.gh.producer(PRODUCER, 'cancelled')
        newer = {**PRODUCER, 'run_id': '322'}
        self.client.writes.clear(); self.reconcile(newer)
        writes = [key for key in self.client.writes if '/turns/' not in key]
        self.assertEqual(len(writes), 3)
        for target in writes:
            for after in (False, True):
                with self.subTest(path=target, after=after):
                    self.client.objects = copy.deepcopy(original)
                    setattr(self.client, 'fail_after_put' if after else 'fail_put', lambda key: key == target)
                    self.assertEqual(self.reconcile(newer)['blocked_events'], 1)
                    self.client.fail_put = None; self.client.fail_after_put = None
                    self.gh.producer(newer, 'cancelled')
                    third = {**PRODUCER, 'run_id': '323'}
                    self.assertEqual(self.reconcile(third)['awaiting_producer_events'], 1)
                    self.assertEqual(self.finish(third, next_id='324')['admitted_events'], 1)
                    self.assertEqual(len(recovered.read_queue(self.store)), 1)

    def test_every_final_ack_write_interruption_preserves_accepted_producer(self):
        self.capture(); self.reconcile(); self.gh.producer(PRODUCER)
        original = copy.deepcopy(self.client.objects)
        self.client.writes.clear(); self.reconcile({**PRODUCER, 'run_id': '322'})
        writes = [key for key in self.client.writes if '/turns/' not in key]
        self.assertEqual(len(writes), 2)
        for target in writes:
            for after in (False, True):
                with self.subTest(path=target, after=after):
                    self.client.objects = copy.deepcopy(original)
                    setattr(self.client, 'fail_after_put' if after else 'fail_put', lambda key: key == target)
                    self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '322'})['blocked_events'], 1)
                    self.client.fail_put = None; self.client.fail_after_put = None
                    self.gh.producer({**PRODUCER, 'run_id': '322'}, 'cancelled')
                    with mock.patch.object(recovered, 'read_public', side_effect=AssertionError('no duplicate collection')):
                        self.assertEqual(self.reconcile({**PRODUCER, 'run_id': '323'})['retained_events'], 0)
                    receipt = read_admission(self.store, recovered.read_queue(self.store)[0]['admission'])
                    self.assertEqual(receipt['producer'], PRODUCER)

    def test_envelope_byte_tamper_never_collects_or_acknowledges(self):
        self.capture()
        for path in next(iter(ingress.pending_inventory(self.store).values())):
            self.client.objects[path]['body'] += b' '
            self.client.objects[path]['ContentLength'] += 1
        with mock.patch.object(recovered, 'read_public') as fetch:
            self.assertEqual(self.reconcile()['blocked_events'], 1)
        fetch.assert_not_called()
        self.assertEqual(recovered.read_queue(self.store), [])

    def test_frozen_capture_races_new_attempt_before_last_identity_read(self):
        api = self.gh.api
        reads = 0
        def changed(path):
            nonlocal reads
            if path == 'actions/runs/300':
                reads += 1
                if reads > 1:
                    self.gh.runs[300]['run_attempt'] = 2
            return api(path)
        self.gh.api = changed
        self.assertFalse(self.capture()['frozen'])
        self.assertTrue(ingress.pending_inventory(self.store))

    def test_wrong_caller_branch_private_repo_and_nondefault_event_rejected(self):
        for change in ({'path': 'other.yml'}, {'event': 'pull_request'}, {'head_branch': 'other'},
                {'repository': {'full_name': 'example/repo', 'private': True}},
                {'head_repository': {'full_name': 'other/repo'}}):
            run = {**self.gh.runs[300], **change}
            with self.subTest(change=change), self.assertRaises(ExpansionError):
                ingress.event_from_run(run, self.gh.repository)

    def test_safe_summary_has_no_article_url_or_source_text(self):
        self.capture()
        summary = stable_bytes(self.reconcile()).decode()
        self.assertNotIn('https:', summary)
        self.assertNotIn('公开中文来源', summary)
        self.assertNotIn(self.publication['request']['records'][0]['slug'], summary)
        self.assertEqual(json.loads(summary)['paid_provider_requests'], 0)

    def test_real_pre_ingress_readers_accept_daily_and_rebound_admission_unchanged_schema(self):
        import types
        import portal_extended_daily_queue as queue
        frozen = json.loads((Path(__file__).parent/'fixtures/extended_source_readers_335.json').read_text())
        self.assertEqual(frozen['modules']['recovered']['git_blob_sha'], 'ccb3d3b8ac91e8dba521fc9234650a26b0373fa2')
        self.assertEqual(frozen['modules']['queue']['git_blob_sha'], 'd05b0bee750f0c070d9bfafa74fef936b8850cc6')
        legacy_recovered = types.ModuleType('portal_extended_recovered_admission')
        legacy_recovered.__dict__.update(vars(recovered))
        exec(compile(frozen['modules']['recovered']['source'], 'head335-recovered-readers', 'exec'), legacy_recovered.__dict__)
        legacy_queue = dict(vars(queue))
        exec(compile(frozen['modules']['queue']['source'], 'head335-queue-reader', 'exec'), legacy_queue)
        self.capture(); self.reconcile()
        first = recovered.read_queue(self.store)[0]['admission']
        self.gh.producer(PRODUCER, 'cancelled')
        self.reconcile({**PRODUCER, 'run_id': '322'})
        second = recovered.read_queue(self.store)[0]['admission']
        with mock.patch.dict('sys.modules', {'portal_extended_recovered_admission': legacy_recovered}):
            for identity in (first, second):
                self.assertEqual(legacy_queue['read_admission'](self.store, identity), read_admission(self.store, identity))
        self.assertEqual(set(legacy_recovered.checked_publication(self.publication)), set(self.publication))

    def test_workflow_capture_has_no_lock_writer_owns_queue_and_only_safe_events(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        value = yaml.safe_load((root/'.github/workflows/portal-extended-locales-source.yml').read_text())
        self.assertNotIn('concurrency', value)
        capture_job, writer = value['jobs']['capture'], value['jobs']['source_snapshot']
        self.assertNotIn('concurrency', capture_job)
        self.assertEqual(writer['concurrency'], {'group': 'extended-locales-source-admission', 'cancel-in-progress': False})
        self.assertEqual(writer['needs'], 'capture')
        captures = '\n'.join(row.get('run', '') for row in capture_job['steps'])
        writes = '\n'.join(row.get('run', '') for row in writer['steps'])
        self.assertIn('publication_ingress.py capture', captures)
        self.assertNotIn('daily_queue.py', captures)
        self.assertIn('publication_ingress.py reconcile', writes)
        self.assertIn('daily_queue.py', writes)
        self.assertNotIn('recovered-publication-run', writes)
        pipeline = yaml.safe_load((root/'.github/workflows/portal-extended-locales-r2.yml').read_text())
        self.assertEqual(pipeline['jobs']['locale']['strategy']['max-parallel'], 2)

    def test_cli_manual_capture_freezes_exact_event_and_empty_dispatch_keeps_latest_day(self):
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true',
            'GITHUB_REPOSITORY': self.gh.repository, 'GITHUB_EVENT_NAME': 'workflow_dispatch',
            'GITHUB_WORKFLOW_REF': self.gh.repository+'/'+WORKFLOW+'@refs/heads/main'}
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory)/'outputs'
            for arguments, expected in ((['--run-id', '300'], 'false'), ([], 'true'), (['--reconcile-only'], 'false')):
                with self.subTest(arguments=arguments), mock.patch.dict('os.environ', env, clear=True), \
                     mock.patch('sys.argv', ['ingress', 'capture', *arguments, '--github-output', str(output)]), \
                     mock.patch.object(ingress.R2Store, 'from_env', return_value=self.store), \
                     mock.patch.object(recovered, 'GitHub', return_value=self.gh), \
                     mock.patch('sys.stdout', new_callable=io.StringIO) as stdout:
                    ingress.main()
                    self.assertNotIn('https:', stdout.getvalue())
                    self.assertTrue(output.read_text().endswith('latest_day='+expected+'\n'))
        self.assertEqual(recovered.read_queue(self.store), [])
        self.assertEqual(len(ingress.pending_inventory(self.store)), 1)

    def test_cli_neutral_failure_wrong_workflow_and_run_input_are_rejected_without_queue_writes(self):
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true',
            'GITHUB_REPOSITORY': self.gh.repository, 'GITHUB_EVENT_NAME': 'workflow_dispatch',
            'GITHUB_WORKFLOW_REF': self.gh.repository+'/'+WORKFLOW+'@refs/heads/main'}
        self.gh.runs[400]['conclusion'] = 'failure'
        for bad_env, arguments in (({}, ['--run-id', '400']), ({}, ['--run-id', '300; print']),
                ({}, ['--run-id', '300', '--reconcile-only']),
                ({'GITHUB_WORKFLOW_REF': 'example/repo/other.yml@refs/heads/main'}, [])):
            with self.subTest(arguments=arguments, env=bad_env), mock.patch.dict('os.environ', {**env, **bad_env}, clear=True), \
                 mock.patch('sys.argv', ['ingress', 'capture', *arguments]), \
                 mock.patch.object(ingress.R2Store, 'from_env', return_value=self.store), \
                 mock.patch.object(recovered, 'GitHub', return_value=self.gh), self.assertRaises(ExpansionError):
                ingress.main()
        self.assertFalse(self.client.objects)

    def test_empty_hourly_wake_is_one_bounded_read_zero_writes_and_zero_dispatch(self):
        dispatch = mock.Mock()
        with mock.patch.object(self.client, 'list_objects_v2', wraps=self.client.list_objects_v2) as listing:
            result = ingress.wake(self.store, self.gh, '20261011T02', dispatch=dispatch)
        self.assertEqual(result, {'pending': False, 'dispatches': 0, 'category': 'empty', 'paid_provider_requests': 0})
        self.assertEqual(listing.call_count, 1)
        self.assertEqual(listing.call_args.kwargs['MaxKeys'], 1)
        dispatch.assert_not_called(); self.assertFalse(self.client.objects)

    def test_pending_wake_unknown_dispatch_is_reserved_once_per_utc_hour(self):
        ingress.persist_envelope(self.store, self.event)
        dispatch = mock.Mock(return_value=False)
        one = ingress.wake(self.store, self.gh, '20261011T02', dispatch=dispatch)
        self.assertEqual(one['category'], 'dispatch_unknown')
        two = ingress.wake(self.store, self.gh, '20261011T02', dispatch=dispatch)
        self.assertEqual(two['category'], 'hour_already_reserved')
        self.assertEqual(dispatch.call_count, 1)
        three = ingress.wake(self.store, self.gh, '20261011T03', dispatch=dispatch)
        self.assertEqual(three['dispatches'], 1)
        self.assertEqual(dispatch.call_count, 2)

    def test_wake_reservation_unknown_write_never_posts_before_verified_readback(self):
        ingress.persist_envelope(self.store, self.event)
        dispatch = mock.Mock(return_value=True)
        self.client.fail_after_put = lambda path: '/wake-reservations/' in path
        with self.assertRaises(R2StoreError):
            ingress.wake(self.store, self.gh, '20261011T02', dispatch=dispatch)
        dispatch.assert_not_called()
        self.client.fail_after_put = None
        self.assertEqual(ingress.wake(self.store, self.gh, '20261011T02', dispatch=dispatch)['dispatches'], 0)
        self.assertEqual(ingress.wake(self.store, self.gh, '20261011T03', dispatch=dispatch)['dispatches'], 1)
        dispatch.assert_called_once()

    def test_wake_does_not_guess_empty_or_dispatch_from_incomplete_listing(self):
        with mock.patch.object(self.client, 'list_objects_v2', return_value={'Contents': [], 'IsTruncated': True}), \
             self.assertRaises(ExpansionError):
            ingress.wake(self.store, self.gh, '20261011T02', dispatch=mock.Mock(side_effect=AssertionError))
        self.assertFalse(self.client.objects)

    def test_dispatch_is_exact_main_source_reconcile_boolean_and_not_retried(self):
        import subprocess
        with mock.patch.object(ingress.subprocess, 'run', return_value=mock.Mock(returncode=0)) as run:
            self.assertTrue(ingress.dispatch_reconcile(self.gh))
        self.assertEqual(run.call_count, 1)
        self.assertEqual(run.call_args.args[0], ['gh', 'api',
            'repos/example/repo/actions/workflows/portal-extended-locales-source.yml/dispatches',
            '--method', 'POST', '--input', '-'])
        self.assertEqual(json.loads(run.call_args.kwargs['input']), {'ref': 'main', 'inputs': {'reconcile_only': True}})
        with mock.patch.object(ingress.subprocess, 'run', side_effect=subprocess.TimeoutExpired('private command', 60)) as run:
            self.assertFalse(ingress.dispatch_reconcile(self.gh))
        self.assertEqual(run.call_count, 1)

    def test_wake_workflow_is_not_watched_and_shell_reconcile_only_cannot_collect_latest(self):
        import os
        import subprocess
        import yaml
        root = Path(__file__).resolve().parents[1]
        wake = yaml.safe_load((root/'.github/workflows/portal-extended-source-wakeup.yml').read_text())
        source = yaml.safe_load((root/'.github/workflows/portal-extended-locales-source.yml').read_text())
        consumer = yaml.safe_load((root/'.github/workflows/portal-extended-locales-r2.yml').read_text())
        for workflow in (source, consumer):
            self.assertNotIn(wake['name'], workflow[True]['workflow_run']['workflows'])
        self.assertEqual(wake[True]['schedule'], [{'cron': '17 * * * *'}])
        self.assertEqual(wake['concurrency'], {'group': 'extended-locale-publication-wake', 'cancel-in-progress': False})
        self.assertEqual(wake['permissions']['actions'], 'write')
        self.assertEqual(source[True]['workflow_dispatch']['inputs']['reconcile_only']['type'], 'boolean')
        command = next(row['run'] for row in source['jobs']['capture']['steps'] if row.get('id') == 'capture')
        writer = source['jobs']['source_snapshot']['steps'][-1]['run']
        with tempfile.TemporaryDirectory() as directory:
            temp = Path(directory)
            stub = temp/'python3'
            stub.write_text('#!/bin/sh\nprintf "%s\\n" "$@" >> "$CALLS"\n')
            stub.chmod(0o755)
            calls = temp/'calls'
            env = {**os.environ, 'PATH': str(temp)+':/usr/bin:/bin', 'CALLS': str(calls),
                'RECOVERED_PUBLICATION_RUN': '', 'RECONCILE_ONLY': 'true', 'LATEST_DAY': 'false',
                'GITHUB_OUTPUT': str(temp/'output'), 'GITHUB_STEP_SUMMARY': str(temp/'summary')}
            subprocess.run(['bash', '-c', command], env=env, check=True, capture_output=True)
            capture_args = calls.read_text()
            self.assertIn('--reconcile-only', capture_args)
            self.assertNotIn('--run-id', capture_args)
            calls.unlink()
            subprocess.run(['bash', '-c', writer], env=env, check=True, capture_output=True)
            self.assertIn('reconcile', calls.read_text())
            self.assertNotIn('daily_queue.py', calls.read_text())


if __name__ == '__main__':
    unittest.main()
