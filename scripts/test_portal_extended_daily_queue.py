"""Private admitted-source queue contracts; no models, credentials or live writes."""
import copy
from datetime import date, timedelta
import json
from pathlib import Path
import tempfile
import unittest

from portal_extended_daily_queue import (WORKFLOW, admit, batch_admission, followup_needed,
    inventory, prepare_queued, queue_key, read_admission, read_queue, staging_probe)
from portal_extended_incremental import content_key, write_state
from portal_extended_locales import ADDITIONAL, ExpansionError, make_corpus, stable_bytes
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store
from test_portal_extended_incremental import DAY, ORIGIN, daily_doc
from test_portal_extended_r2 import FakeR2
from review_portal_extended_handoff import admission_is_valid, producer_is_valid

PRODUCER = {'run_id': '321', 'attempt': '1', 'sha': 'a'*40, 'repository': 'example/repo', 'workflow': WORKFLOW}


class SourceQueueTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeR2()
        self.store = R2Store(self.client, 'private', '_extended-locales/staging/queue')
        self.docs = [daily_doc(ORIGIN+f'/blog/20260925-{index:03}.html') for index in range(26)]

    def complete(self, locale, docs, day=DAY):
        pages = {doc['url']: {'content_key': content_key(doc), 'generation': 'b'*64, 'candidate_id': 'c'*64} for doc in docs}
        write_state(self.store, 'completed', locale, {'pages': pages}, day)

    def test_empty_day_does_not_fill_with_history_or_create_work(self):
        self.assertFalse(admit(self.store, [], DAY, PRODUCER)['admitted'])
        self.assertFalse(prepare_queued(self.store, ('fr',))['has_work'])
        self.assertFalse(self.client.objects)

    def test_admitted_source_is_immutable_readback_verified_and_private(self):
        result = admit(self.store, self.docs, DAY, PRODUCER)
        entry = read_queue(self.store)[0]
        admission, corpus = inventory(self.store, entry)
        self.assertEqual(result['generation'], corpus['documents_sha256'])
        self.assertEqual(admission['pages'], 26)
        self.assertEqual(read_admission(self.store, result['admission'])['producer'], PRODUCER)
        again = admit(self.store, self.docs, DAY, PRODUCER)
        self.assertEqual(result, again)
        self.assertTrue(all(row['CacheControl'] == 'private, no-store' for row in self.client.objects.values()))

    def test_independent_cursors_do_not_let_one_unfinished_locale_starve_others(self):
        admit(self.store, self.docs, DAY, PRODUCER)
        first = prepare_queued(self.store, ('fr', 'pt'))
        self.assertEqual(first['per_locale_counts']['fr'], {'selected': 24, 'remaining': 2})
        self.complete('fr', self.docs[:24])
        next_batch = prepare_queued(self.store, ('fr', 'pt'))
        jobs = {job['locale']: job for job in json.loads(next_batch['locale_jobs_json'])}
        self.assertNotEqual(jobs['fr']['generation'], jobs['pt']['generation'])
        self.assertEqual(next_batch['per_locale_counts']['fr'], {'selected': 2, 'remaining': 0})
        self.assertEqual(next_batch['per_locale_counts']['pt'], {'selected': 24, 'remaining': 2})
        self.assertEqual(next_batch['generation'], '')
        for job in jobs.values(): self.assertEqual(batch_admission(self.store, job['generation'])['day'], DAY)

    def test_all_33_jobs_keep_the_24_page_ceiling_and_no_english(self):
        admit(self.store, self.docs, DAY, PRODUCER)
        result = prepare_queued(self.store, ADDITIONAL)
        jobs = json.loads(result['locale_jobs_json'])
        self.assertEqual(len(jobs), 33)
        self.assertNotIn('en', {job['locale'] for job in jobs})
        self.assertTrue(all(row['selected'] == 24 for row in result['per_locale_counts'].values()))
        self.assertEqual(len({job['generation'] for job in jobs}), 1)
        with self.assertRaises(ExpansionError): prepare_queued(self.store, ('en',))
        for limit in (0, 25, True):
            with self.assertRaises(ExpansionError): prepare_queued(self.store, ('fr',), limit=limit)

    def test_completed_locale_is_omitted_without_retranslation(self):
        admit(self.store, self.docs, DAY, PRODUCER); self.complete('fr', self.docs)
        result = prepare_queued(self.store, ('fr', 'pt'))
        self.assertEqual(json.loads(result['locales_json']), ['pt'])
        self.complete('pt', self.docs)
        self.assertFalse(prepare_queued(self.store, ('fr', 'pt'))['has_work'])

    def test_new_hot_day_has_priority_but_previously_admitted_work_is_preserved(self):
        admit(self.store, self.docs, DAY, PRODUCER)
        newer = [daily_doc(ORIGIN+'/blog/20260926-new.html', day='2026-09-26')]
        admit(self.store, newer, '2026-09-26', {**PRODUCER, 'run_id': '322'})
        result = prepare_queued(self.store, ('fr',))
        self.assertEqual(result['day'], '2026-09-26')
        self.complete('fr', newer, '2026-09-26')
        self.assertEqual(prepare_queued(self.store, ('fr',))['day'], DAY)
        self.assertEqual(len(read_queue(self.store)), 2)

    def test_changed_body_reactivates_only_changed_content(self):
        admit(self.store, self.docs, DAY, PRODUCER); self.complete('fr', self.docs)
        changed = copy.deepcopy(self.docs)
        changed[0] = daily_doc(changed[0]['url'], body='<h1>Research note</h1><p>Changed findings.</p>')
        admit(self.store, changed, DAY, {**PRODUCER, 'run_id': '323'})
        result = prepare_queued(self.store, ('fr',))
        self.assertEqual(result['per_locale_counts']['fr']['selected'], 1)
        self.assertEqual(len(read_queue(self.store)), 1)

    def test_only_durable_progress_can_self_continue_partial_failures(self):
        saved = admit(self.store, self.docs, DAY, PRODUCER)
        before = {'fr': 26, 'pt': 26}
        self.assertFalse(followup_needed(self.store, saved['admission'], ('fr','pt'), before)['continue'])
        self.complete('fr', self.docs[:24])
        self.assertTrue(followup_needed(self.store, saved['admission'], ('fr','pt'), before)['continue'])
        current = {'fr': 2, 'pt': 26}
        self.assertFalse(followup_needed(self.store, saved['admission'], ('fr','pt'), current)['continue'])
        self.complete('fr', self.docs); self.complete('pt', self.docs)
        self.assertFalse(followup_needed(self.store, saved['admission'], ('fr','pt'), current)['continue'])
        for bad in ({'fr':26}, {'fr':True,'pt':26}, {'fr':27,'pt':26}):
            with self.assertRaises(ExpansionError): followup_needed(self.store, saved['admission'], ('fr','pt'), bad)

    def test_permission_or_checksum_failure_never_becomes_an_empty_queue(self):
        self.client.deny = True
        with self.assertRaises(R2PermissionError): admit(self.store, self.docs, DAY, PRODUCER)
        self.client.deny = False; admit(self.store, self.docs, DAY, PRODUCER)
        self.client.objects[queue_key(self.store)]['Metadata']['sha256'] = '0'*64
        with self.assertRaises(R2IntegrityError): prepare_queued(self.store, ('fr',))

    def test_bad_receipt_or_out_of_admission_batch_is_not_trusted(self):
        saved = admit(self.store, self.docs, DAY, PRODUCER)
        self.complete('fr', self.docs[:1])
        key = self.store.key('incremental', 'completed', 'fr', DAY, 'state.json')
        value = json.loads(self.client.objects[key]['body']); value['pages'][self.docs[0]['url']] = False
        self.store._put(key, stable_bytes(value), metadata={'kind':'test'})
        with self.assertRaises(R2IntegrityError): prepare_queued(self.store, ('fr',))
        unrelated = make_corpus([daily_doc(ORIGIN+'/blog/20260925-outside.html')])
        self.store.put_source(unrelated)
        generation = unrelated['documents_sha256']
        self.store._put(self.store.key('batch-admissions', generation, 'receipt.json'),
            stable_bytes({'schema_version':1, 'policy':'daily-source-admission-v1', 'generation':generation, 'admission':saved['admission']}),
            metadata={'kind':'test'})
        with self.assertRaises(R2IntegrityError): batch_admission(self.store, generation)

    def test_invalid_dates_producer_and_more_than_500_pages_fail_before_writes(self):
        for day in ('n/a', '2026-09-24'):
            with self.assertRaises(ExpansionError): admit(self.store, [], day, PRODUCER)
        for bad in ({**PRODUCER, 'sha':'invalid'}, {**PRODUCER, 'workflow':'other.yml'}):
            with self.assertRaises(ExpansionError): admit(self.store, self.docs, DAY, bad)
        too_many = [daily_doc(ORIGIN+f'/blog/20260925-{index:04}.html') for index in range(501)]
        with self.assertRaises(ExpansionError): admit(self.store, too_many, DAY, PRODUCER)
        self.assertFalse(self.client.objects)

    def test_full_queue_never_discards_unfinished_admitted_days(self):
        for index in range(32):
            day = (date(2026, 10, 1) + timedelta(days=index)).isoformat()
            doc = daily_doc(ORIGIN+'/blog/'+day.replace('-','')+'-new.html', day=day)
            admit(self.store, [doc], day, {**PRODUCER,'run_id':str(1000+index)})
        before = copy.deepcopy(read_queue(self.store))
        day = '2026-11-02'
        with self.assertRaises(ExpansionError):
            admit(self.store, [daily_doc(ORIGIN+'/blog/20261102-new.html',day=day)],day,PRODUCER)
        self.assertEqual(read_queue(self.store), before)

    def test_staging_probe_restores_real_objects_without_inference_or_ready_candidates(self):
        result = staging_probe(self.store)
        self.assertTrue(result['staging_only']); self.assertEqual(result['translation_calls'], 0)
        self.assertEqual(result['ready_candidates'], 0); self.assertFalse(result['deployed'])
        self.assertEqual(result['checkpoint_restore'], 'passed')
        self.assertFalse(any('/candidate-ready.json' in key for key in self.client.objects))
        with self.assertRaises(Exception): staging_probe(R2Store(self.client, 'private', '_extended-locales/v1'))


class SourceProvenanceTests(unittest.TestCase):
    def setUp(self):
        self.admitted = {'day': DAY, 'producer': PRODUCER, 'admission':'c'*64}
        self.run = {'id':321, 'run_attempt':1, 'head_sha':'a'*40, 'status':'completed', 'conclusion':'success',
            'head_branch':'main', 'path':WORKFLOW, 'event':'workflow_run',
            'repository':{'full_name':'example/repo', 'private':False}, 'head_repository':{'full_name':'example/repo'}}
        self.jobs = [{'name':'source_snapshot','status':'completed','conclusion':'success',
            'started_at':'2026-09-25T01:00:00Z','completed_at':'2026-09-25T01:05:00Z'}]

    def test_capture_must_be_complete_main_public_same_day_and_exact_attempt(self):
        self.assertEqual(admission_is_valid(self.admitted,self.run,self.jobs,'example/repo'), self.admitted)
        for changes in ({'conclusion':'failure'}, {'status':'in_progress'}, {'head_branch':'feature'}, {'run_attempt':2},
            {'path':'other.yml'}, {'head_repository':{'full_name':'other/repo'}}):
            with self.assertRaises(ExpansionError): admission_is_valid(self.admitted,{**self.run,**changes},self.jobs,'example/repo')
        with self.assertRaises(ExpansionError): admission_is_valid({**self.admitted,'day':'2026-09-24'},self.run,self.jobs,'example/repo')

    def test_later_consumer_can_resume_only_its_verified_frozen_admission(self):
        from test_review_portal_extended_handoff import DailyReviewTests
        original = DailyReviewTests(); original.setUp()
        receipt = {**original.receipt,'source_admission':self.admitted['admission']}
        jobs = copy.deepcopy(original.jobs)
        jobs[0].update(started_at='2026-09-26T01:00:00Z',completed_at='2026-09-26T01:05:00Z')
        with self.assertRaises(ExpansionError): producer_is_valid(receipt,original.run,jobs,'example/repo')
        producer_is_valid(receipt,original.run,jobs,'example/repo',self.admitted)
        for bad in ({**self.admitted,'day':'2026-09-24'}, {**self.admitted,'admission':'d'*64}):
            with self.assertRaises(ExpansionError): producer_is_valid(receipt,original.run,jobs,'example/repo',bad)

    def test_workflow_keeps_cpu_bound_no_artifacts_and_has_source_day_admission(self):
        root = Path(__file__).resolve().parents[1]
        source = (root/'.github/workflows/portal-extended-locales-source.yml').read_text()
        consumer = (root/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        for text in ('source_snapshot:', 'Neutral edge catalog refresh', 'ubuntu-22.04', 'cancel-in-progress: false'):
            self.assertIn(text, source)
        for text in ('max-parallel: 2', 'timeout-minutes: 270', 'matrix.generation', 'locale_jobs_json',
                     'continue_admitted_batches:', "steps.frontier.outputs.continue == 'true'"):
            self.assertIn(text, consumer)
        self.assertNotIn('actions/upload-artifact', source+consumer)
        self.assertNotIn('actions/cache', source)


if __name__ == '__main__': unittest.main()
