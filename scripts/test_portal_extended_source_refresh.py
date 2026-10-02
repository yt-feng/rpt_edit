"""Late source refresh, immutable admission and publication across midnight."""
import copy
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

from build_portal_extended_locales import build
from portal_extended_daily_queue import (admit, batch_admission, main, prepare_queued,
                                        read_admission, read_queue)
from portal_extended_handoff import next_ready_refresh, read_publication_batches
from portal_extended_incremental import remember_candidate, write_state
from portal_extended_locales import ADDITIONAL, ExpansionError, make_corpus, stable_bytes
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store
from portal_extended_source_refresh import (POLICY, collect_refresh, latest_day, read_proof,
                                           save_proof, validate_proof)
from review_portal_extended_handoff import admission_is_valid
from test_portal_extended_daily_queue import PRODUCER
from test_portal_extended_incremental import DAY, ORIGIN, daily_doc, raw_page
from test_portal_extended_locales import FakeTranslator
from test_portal_extended_r2 import FakeR2

CAPTURE = '2026-09-27'
RELEASE = {'slot': 'a', 'release_id': 'a'*32, 'tree_sha256': 'b'*64}


def proof(docs, *, capture=CAPTURE):
    return {'schema_version': 1, 'policy': POLICY, 'capture_day': capture,
            'day': docs[0]['selection_day'], 'release': RELEASE,
            'inventory': {doc['url']: doc['datePublished'] for doc in docs}}


class RefreshCollectionTests(unittest.TestCase):
    def test_source_day_is_newest_available_not_runner_date_or_archive_start(self):
        entries = {ORIGIN+'/blog/20260925-new.html': DAY,
                   ORIGIN+'/blog/20260924-old.html': CAPTURE,
                   ORIGIN+'/about.html': CAPTURE, ORIGIN+'/reports/': CAPTURE}
        self.assertEqual(latest_day(entries, CAPTURE), DAY)
        self.assertEqual(latest_day({ORIGIN+'/blog/20260924-old.html': DAY}, CAPTURE), '')
        self.assertEqual(latest_day({ORIGIN+'/blog/20260928-future.html': CAPTURE}, CAPTURE), '')

    def test_latest_day_is_pinned_and_shared_with_english_without_fetching_history(self):
        url = ORIGIN+'/blog/20260925-new.html'
        entries = {url: DAY, ORIGIN+'/blog/20260924-old.html': DAY}
        sink = mock.Mock()
        with mock.patch('portal_extended_source_refresh.read_release', return_value=RELEASE), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value=entries), \
             mock.patch('portal_extended_incremental.read_public', return_value=raw_page()) as fetch:
            day, docs, evidence = collect_refresh(mock.Mock(), CAPTURE, on_source=sink)
        self.assertEqual(day, DAY); self.assertEqual(len(docs), 1)
        self.assertEqual(fetch.call_args.args[1], url); self.assertEqual(fetch.call_count, 1)
        self.assertEqual(sink.call_args.args[1], raw_page())
        self.assertEqual(evidence['capture_day'], CAPTURE)
        self.assertEqual(docs[0]['datePublished'], DAY)

    def test_lastmod_never_turns_an_old_report_into_a_new_page(self):
        url = ORIGIN+'/reports/old.html'
        with mock.patch('portal_extended_source_refresh.read_release', return_value=RELEASE), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value={url: DAY}), \
             mock.patch('portal_extended_incremental.read_public', return_value=raw_page(url, '2026-09-24', 'Report')):
            day, docs, _ = collect_refresh(mock.Mock(), CAPTURE)
        self.assertEqual(day, DAY); self.assertEqual(docs, [])

    def test_release_change_rejects_capture_and_keeps_page_limit(self):
        url = ORIGIN+'/blog/20260925-new.html'
        with mock.patch('portal_extended_source_refresh.read_release', side_effect=[RELEASE, {**RELEASE, 'slot':'b'}]), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value={url: DAY}), \
             mock.patch('portal_extended_incremental.read_public', return_value=raw_page()):
            with self.assertRaisesRegex(ExpansionError, 'changed during capture'):
                collect_refresh(mock.Mock(), CAPTURE)
        entries = {ORIGIN+f'/blog/20260925-{i}.html': DAY for i in range(501)}
        with mock.patch('portal_extended_source_refresh.read_release', return_value=RELEASE), \
             mock.patch('portal_extended_source_refresh.inventory_entries', return_value=entries), \
             mock.patch('portal_extended_incremental.read_public') as fetch:
            with self.assertRaisesRegex(ExpansionError, '500'):
                collect_refresh(mock.Mock(), CAPTURE)
            fetch.assert_not_called()

    def test_private_routes_unknown_dates_and_bbg_scope_stay_excluded(self):
        for url in (ORIGIN+'/api/private', ORIGIN+'/blog/bbg-20260925-example.html',
                    'https://other.invalid/blog/20260925-new.html'):
            with self.assertRaises(ExpansionError): latest_day({url: DAY}, CAPTURE)
        self.assertEqual(latest_day({ORIGIN+'/reports/new.html': 'unknown'}, CAPTURE), '')


class RefreshAdmissionTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeR2(); self.store = R2Store(self.client, 'private', '_extended-locales/staging/refresh')
        self.docs = [daily_doc()]; self.corpus = make_corpus(self.docs)

    def test_new_admission_restores_capture_proof_and_original_dates(self):
        saved = admit(self.store, self.docs, DAY, PRODUCER, refresh=proof(self.docs))
        receipt = read_admission(self.store, saved['admission'])
        self.assertEqual(receipt['schema_version'], 2); self.assertEqual(receipt['day'], DAY)
        self.assertEqual(receipt['capture_day'], CAPTURE)
        self.assertEqual(read_proof(self.store, receipt['refresh'], self.corpus)['release'], RELEASE)
        self.assertTrue(all(row['CacheControl'] == 'private, no-store' for row in self.client.objects.values()))
        result = prepare_queued(self.store, ADDITIONAL)
        self.assertEqual(result['pending_locale_count'], 33)
        self.assertEqual(batch_admission(self.store, result['generation'])['capture_day'], CAPTURE)
        self.assertEqual(len(read_publication_batches(self.store)), 1)

    def test_cannot_admit_an_older_day_when_a_newer_source_exists(self):
        evidence = proof(self.docs)
        evidence['inventory'][ORIGIN+'/blog/20260926-new.html'] = '2026-09-26'
        with self.assertRaisesRegex(ExpansionError, 'identity'):
            save_proof(self.store, evidence, self.corpus)
        self.assertFalse(self.client.objects)
        later = [daily_doc(ORIGIN+'/blog/20260926-new.html', day='2026-09-26')]
        admit(self.store, later, '2026-09-26', PRODUCER, refresh=proof(later))
        with self.assertRaisesRegex(ExpansionError, 'backwards'):
            admit(self.store, self.docs, DAY, PRODUCER, refresh=proof(self.docs))

    def test_corrupt_inventory_and_permission_errors_do_not_become_empty_days(self):
        saved = admit(self.store, self.docs, DAY, PRODUCER, refresh=proof(self.docs))
        receipt = read_admission(self.store, saved['admission'])
        key = self.store.key('source-refreshes', receipt['refresh'], 'inventory.json')
        self.client.deny = True
        with self.assertRaises(R2PermissionError): read_admission(self.store, saved['admission'])
        self.client.deny = False
        self.client.objects[key]['Metadata']['sha256'] = '0'*64
        with self.assertRaises(R2IntegrityError): read_admission(self.store, saved['admission'])

    def test_same_run_proof_keeps_required_capture_job_checks(self):
        from test_portal_extended_daily_queue import SourceProvenanceTests
        saved = admit(self.store, self.docs, DAY, PRODUCER, refresh=proof(self.docs))
        receipt = read_admission(self.store, saved['admission'])
        original = SourceProvenanceTests(); original.setUp()
        jobs = copy.deepcopy(original.jobs)
        jobs[0].update(started_at=CAPTURE+'T01:00:00Z', completed_at=CAPTURE+'T01:05:00Z')
        admission_is_valid(receipt, original.run, jobs, 'example/repo')
        with self.assertRaises(ExpansionError):
            admission_is_valid(receipt, original.run, original.jobs, 'example/repo')
        with self.assertRaises(ExpansionError):
            admission_is_valid(receipt, {**original.run, 'head_branch':'feature'}, jobs, 'example/repo')
        legacy = {**original.admitted}
        with self.assertRaises(ExpansionError): admission_is_valid(legacy, original.run, jobs, 'example/repo')

    def test_source_cli_uses_actual_capture_day_and_separate_editorial_projection(self):
        from test_portal_english_commentary import page
        from portal_english_commentary import extract_editorial
        from portal_english_pipeline import read_admission as read_english_admission
        from portal_extended_locales import document_from_html, DAILY_SCOPE, digest
        url = ORIGIN+'/blog/20260925-0000000000000001.html'
        raw = page(url=url, day=DAY)
        doc = document_from_html(url, raw, exclude_related=True)
        doc.update(selection_day=DAY, selection_scope=DAILY_SCOPE)
        doc['content_sha256'] = digest(stable_bytes({k:v for k,v in doc.items() if k != 'content_sha256'}))
        def collect(session, capture, *, on_source):
            self.assertEqual(capture, CAPTURE); on_source(doc, raw)
            return DAY, [doc], proof([doc])
        env = {'GITHUB_ACTIONS':'true', 'GITHUB_REF':'refs/heads/main', 'KC_PUBLIC_REPOSITORY':'true',
               'GITHUB_RUN_ID':'321', 'GITHUB_RUN_ATTEMPT':'1', 'GITHUB_SHA':'a'*40, 'GITHUB_REPOSITORY':'example/repo'}
        output = io.StringIO()
        with mock.patch.dict('os.environ', env), mock.patch('sys.argv', ['source', '--prefix', self.store.prefix]), \
             mock.patch('portal_extended_daily_queue.today', return_value=CAPTURE), \
             mock.patch('portal_extended_daily_queue.R2Store.from_env', return_value=self.store), \
             mock.patch('portal_extended_source_refresh.collect_refresh', side_effect=collect), \
             mock.patch('sys.stdout', output):
            main()
        result = json.loads(output.getvalue())
        self.assertTrue(result['admitted']); self.assertEqual(result['source_day'], DAY)
        self.assertEqual(result['capture_day'], CAPTURE)
        english = R2Store(self.client, 'private', self.store.prefix+'/english-commentary')
        receipt, source = read_english_admission(english, result['english_editorial']['receipt'], self.store)
        self.assertEqual(source['documents'], [extract_editorial(url, raw, DAY)])
        self.assertEqual(receipt['day'], DAY)

    def test_cross_day_publication_survives_completed_cursor_pruning(self):
        saved = admit(self.store, self.docs, DAY, PRODUCER, refresh=proof(self.docs))
        prepare_queued(self.store, ('fr',))
        active = [{'generation':'a'*64, 'candidates':{'fr':'b'*64}}]
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            build(self.corpus, 'fr', root/'candidate', root/'memo.json', FakeTranslator())
            remember_candidate(self.store, 'fr', self.corpus, root/'candidate')
            from portal_extended_incremental import read_state
            completed = read_state(self.store, 'completed', 'fr', DAY)
            for locale in ADDITIONAL:
                write_state(self.store, 'completed', locale, {'pages': completed['pages']}, DAY)
            # Simulate the next source admission pruning a fully translated day.
            later = [daily_doc(ORIGIN+'/blog/20260926-new.html', day='2026-09-26')]
            admit(self.store, later, '2026-09-26', PRODUCER, refresh=proof(later))
            self.assertEqual([row['day'] for row in read_queue(self.store)], ['2026-09-26'])
            batch, corpus = next_ready_refresh(self.store, CAPTURE, 'fr', 'fr', active, root/'restored')
            self.assertEqual(corpus, self.corpus)
            self.assertEqual(batch['generation'], saved['generation'])
            self.assertIsNone(next_ready_refresh(self.store, CAPTURE, 'fr', 'fr', active+[batch], root/'again'))


if __name__ == '__main__': unittest.main()
