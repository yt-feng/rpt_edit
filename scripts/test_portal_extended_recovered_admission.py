"""Exact published cohort admission, durable dedup and bounded cursor tests."""
import copy
import io
import json
from pathlib import Path
import unittest
from unittest import mock
import zipfile

import portal_extended_recovered_admission as recovery
from portal_extended_daily_queue import (admit, all_queued, followup_needed, inventory,
    prepare_queued, read_admission, read_queue)
from portal_extended_incremental import content_key, write_state
from portal_extended_locales import ADDITIONAL, ExpansionError, ORIGIN, digest, stable_bytes
from portal_extended_r2 import R2IntegrityError, R2Store
import test_portal_extended_daily_queue as queue_tests
from test_portal_extended_incremental import daily_doc
from test_portal_extended_r2 import FakeR2
from watch_recovered_article_publication import body_identity, title_hash

DAY = '2026-10-08'
CAPTURE = '2026-10-10'
RELEASE = {'slot': 'a', 'release_id': 'a'*32, 'tree_sha256': 'b'*64}
PRODUCER = queue_tests.PRODUCER


def fixture(count=2, *, start=0, day=DAY, commit='c'*40):
    pages, records = {}, []
    for index in range(start, start+count):
        fingerprint = digest(f'synthetic-{index}-{day}'.encode())
        slug = day.replace('-', '')+'-'+fingerprint[:16]
        url = ORIGIN+'/blog/'+slug+'.html'
        title = f'公开中文来源 {index}'
        schema = json.dumps({'@type': 'BlogPosting', 'url': url, 'datePublished': day, 'dateModified': day})
        html = (f'<html lang="zh-Hans"><head><link rel="canonical" href="{url}">'
                f'<script type="application/ld+json">{schema}</script></head><body><main><h1>{title}</h1>'
                f'<div class="blog-article-content"><p>{"来源支持的中文分析内容。"*30}</p></div></main></body></html>')
        pages[url] = html.encode()
        records.append({'fingerprint': fingerprint, 'slug': slug,
                        'body_sha256': body_identity(html)[0], 'title_sha256': [title_hash(title)]})
    request = {'schema_version': 1, 'origin': ORIGIN, 'archive_commit': commit, 'records': records}
    state = {'schema_version': 1, 'request_sha256': recovery.request_hash(request),
             'status': 'complete', 'run_ids': [400], 'release_run_id': 400, 'article_count': count}
    value = {'repository': 'example/repo', 'run_id': '300', 'attempt': '1', 'sha': 'a'*40,
             'release_run_id': '400', 'release_attempt': '1', 'release_sha': 'd'*40,
             'request': request, 'state': state}
    return value, pages


def capture(value, pages):
    with mock.patch.object(recovery, 'read_release', return_value=RELEASE), \
         mock.patch.object(recovery, 'read_public', side_effect=lambda session, url: pages[url]):
        return recovery.collect(object(), value, CAPTURE)


class FakeGitHub:
    repository = 'example/repo'

    def __init__(self, publication):
        self.calls = []
        self.ancestor = True
        base = {'status': 'completed', 'conclusion': 'success', 'head_branch': 'main',
                'event': 'workflow_dispatch', 'run_attempt': 1,
                'repository': {'full_name': self.repository, 'private': False},
                'head_repository': {'full_name': self.repository}}
        self.run = {**base, 'id': 300, 'path': recovery.WORKFLOW, 'head_sha': 'a'*40}
        self.release = {**base, 'id': 400, 'path': '.github/workflows/neutral-edge-cutover.yml', 'head_sha': 'd'*40}
        self.jobs = {'total_count': 3, 'jobs': [{'name': name, 'status': 'completed', 'conclusion': 'success',
                     'run_id': 300, 'head_sha': 'a'*40} for name in ('generate', 'deliver', 'publish')]}
        self.artifacts = {'total_count': 2, 'artifacts': [
            {'name': f'recovered-publication-{kind}-300', 'id': index, 'expired': False, 'size_in_bytes': 2048}
            for index, kind in enumerate(('request', 'state'), 1)]}
        self.values = {1: publication['request'], 2: publication['state']}

    def api(self, suffix):
        self.calls.append(suffix)
        return copy.deepcopy({'actions/runs/300': self.run, 'actions/runs/400': self.release,
            'actions/runs/300/attempts/1/jobs?per_page=100': self.jobs,
            'actions/runs/300/artifacts?per_page=100': self.artifacts}[suffix])

    def artifact(self, identity, member):
        self.calls.append((identity, member))
        return copy.deepcopy(self.values[identity])

    def contains(self, base, head):
        self.calls.append((base, head))
        return self.ancestor


class PublicationTests(unittest.TestCase):
    def setUp(self):
        self.publication, self.pages = fixture()

    def test_authenticates_current_attempt_jobs_artifacts_release_and_ancestry(self):
        gh = FakeGitHub(self.publication)
        self.assertEqual(recovery.authenticate(gh, '300'), self.publication)
        self.assertIn(('c'*40, 'd'*40), gh.calls)

    def test_failed_wrong_repo_branch_path_or_unexecuted_job_cannot_admit(self):
        changes = [{'conclusion': 'failure'}, {'head_branch': 'feature'}, {'path': 'other.yml'},
                   {'head_repository': {'full_name': 'other/repo'}}, {'repository': {'full_name': 'example/repo', 'private': True}}]
        for change in changes:
            gh = FakeGitHub(self.publication); gh.run.update(change)
            with self.subTest(change=change), self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        for name in ('generate', 'deliver', 'publish'):
            gh = FakeGitHub(self.publication)
            next(row for row in gh.jobs['jobs'] if row['name'] == name)['conclusion'] = 'skipped'
            with self.subTest(name=name), self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')

    def test_publish_only_rerun_uses_latest_verified_stage_without_requiring_new_upload(self):
        gh = FakeGitHub(self.publication); gh.run['run_attempt'] = 2
        gh.jobs['jobs'][-1]['conclusion'] = 'failure'
        api = gh.api
        latest = {'total_count': 1, 'jobs': [{**gh.jobs['jobs'][-1], 'conclusion': 'success'}]}
        gh.api = lambda path: copy.deepcopy(latest) if path == 'actions/runs/300/attempts/2/jobs?per_page=100' else api(path)
        result = recovery.authenticate(gh, '300')
        self.assertEqual(result['attempt'], '2')
        latest['jobs'][0]['conclusion'] = 'failure'
        with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')

    def test_receipt_count_hash_pending_and_release_identity_fail_closed(self):
        for update in ({'status': 'awaiting_live_content'}, {'request_sha256': '0'*64}, {'article_count': 1}):
            gh = FakeGitHub(self.publication); gh.values[2] = {**gh.values[2], **update}
            with self.subTest(update=update), self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        for change in ({'conclusion': 'failure'}, {'head_branch': 'other'}):
            gh = FakeGitHub(self.publication); gh.release.update(change)
            with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        gh = FakeGitHub(self.publication); gh.ancestor = False
        with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        one, _ = fixture(1); one['state']['article_count'] = True
        with self.assertRaises(ExpansionError): recovery.authenticate(FakeGitHub(one), '300')

    def test_expired_duplicate_oversized_incomplete_artifacts_rejected(self):
        for change in ({'expired': True}, {'size_in_bytes': recovery.MAX_ARTIFACT_BYTES+1}):
            gh = FakeGitHub(self.publication); gh.artifacts['artifacts'][0].update(change)
            with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        gh = FakeGitHub(self.publication); gh.artifacts['total_count'] += 1
        with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')
        gh = FakeGitHub(self.publication); gh.artifacts['artifacts'].append(gh.artifacts['artifacts'][0]); gh.artifacts['total_count'] += 1
        with self.assertRaises(ExpansionError): recovery.authenticate(gh, '300')

    def test_zip_single_member_and_expanded_limit_without_extraction(self):
        def archive(name, value, extra=False):
            output = io.BytesIO()
            with zipfile.ZipFile(output, 'w', compression=zipfile.ZIP_DEFLATED) as item:
                item.writestr(name, value)
                if extra: item.writestr('other.json', '{}')
            return output.getvalue()
        self.assertEqual(recovery.artifact_json(archive('receipt.json', '{"ok":true}'), 'receipt.json'), {'ok': True})
        for raw in (archive('../receipt.json', '{}'), archive('receipt.json', '{}', True),
                    archive('receipt.json', ' '* (recovery.MAX_ARTIFACT_BYTES+1)), b'invalid'):
            with self.assertRaises(ExpansionError): recovery.artifact_json(raw, 'receipt.json')

    def test_only_requested_urls_fetched_with_original_day_and_bound_bytes(self):
        with mock.patch.object(recovery, 'read_release', return_value=RELEASE) as edge, \
             mock.patch.object(recovery, 'read_public', side_effect=lambda session, url: self.pages[url]) as fetch:
            corpus, proof = recovery.collect(object(), self.publication, CAPTURE)
        self.assertEqual({call.args[1] for call in fetch.call_args_list}, set(self.pages))
        self.assertEqual(edge.call_count, 2)
        self.assertEqual(proof['day'], DAY); self.assertEqual(proof['capture_day'], CAPTURE)
        self.assertEqual(len(corpus['documents']), 2)
        changed = copy.deepcopy(corpus); changed['documents'][0]['source_html_sha256'] = '0'*64
        with self.assertRaises(ExpansionError): recovery.validate_proof(proof, changed)

    def test_live_body_canonical_date_and_edge_changes_reject_whole_capture(self):
        url = next(iter(self.pages))
        for content in (self.pages[url].replace('来源支持'.encode(), '不相同'.encode()),
                        self.pages[url].replace(f'canonical" href="{url}'.encode(), b'canonical" href="https://other.invalid'),
                        self.pages[url].replace(DAY.encode(), b'2026-10-07')):
            pages = {**self.pages, url: content}
            with self.assertRaises(ExpansionError): capture(self.publication, pages)
        with mock.patch.object(recovery, 'read_release', side_effect=[RELEASE, {**RELEASE, 'slot': 'b'}]), \
             mock.patch.object(recovery, 'read_public', side_effect=lambda session, url: self.pages[url]):
            with self.assertRaises(ExpansionError): recovery.collect(object(), self.publication, CAPTURE)

    def test_mixed_dates_and_noncanonical_origin_rejected_before_fetch(self):
        other, _ = fixture(1, day='2026-10-07')
        value = copy.deepcopy(self.publication)
        value['request']['records'][0] = other['request']['records'][0]
        value['state']['request_sha256'] = recovery.request_hash(value['request'])
        with mock.patch.object(recovery, 'read_public') as fetch:
            with self.assertRaises(ExpansionError): recovery.collect(object(), value, CAPTURE)
            fetch.assert_not_called()
        value = copy.deepcopy(self.publication); value['request']['origin'] = 'https://other.invalid'
        with self.assertRaises(ExpansionError): recovery.checked_publication(value)

    def test_empty_publication_is_honest_no_work_and_corpus_is_bounded(self):
        value, _ = fixture(0)
        value['state'].pop('release_run_id'); value['state']['run_ids'] = []
        self.assertIsNone(recovery.authenticate(FakeGitHub(value), '300'))
        with mock.patch.object(recovery, 'MAX_SOURCE_BYTES', 100):
            with self.assertRaises(ExpansionError): capture(self.publication, self.pages)


class QueueTests(unittest.TestCase):
    def setUp(self):
        self.client = FakeR2(); self.store = R2Store(self.client, 'private', '_extended-locales/staging/recovered')
        self.publication, pages = fixture(44)
        self.corpus, self.proof = capture(self.publication, pages)

    def recover(self, corpus=None, proof=None):
        return recovery.admit(self.store, corpus or self.corpus, proof or self.proof, PRODUCER)

    def complete(self, locale, docs, day=DAY):
        write_state(self.store, 'completed', locale, {'pages': {doc['url']: {
            'content_key': content_key(doc), 'generation': 'b'*64, 'candidate_id': 'c'*64} for doc in docs}}, day)

    def test_historical_and_same_day_cohorts_append_without_touching_normal_queue(self):
        normal = daily_doc(ORIGIN+'/blog/20261010-new.html', day=CAPTURE)
        admit(self.store, [normal], CAPTURE, PRODUCER)
        latest = copy.deepcopy(read_queue(self.store))
        one = self.recover()
        other, pages = fixture(1, start=100)
        corpus, proof = capture(other, pages); two = self.recover(corpus, proof)
        self.assertEqual(read_queue(self.store), latest)
        self.assertEqual(len(recovery.read_queue(self.store)), 2)
        self.assertEqual(len(all_queued(self.store)), 3)
        self.assertNotEqual(one['admission'], two['admission'])
        self.assertEqual(read_admission(self.store, one['admission'])['schema_version'], 3)
        self.assertTrue(all(row['CacheControl'] == 'private, no-store' for row in self.client.objects.values()))

    def test_same_publication_replay_no_queue_or_receipt_mutation(self):
        first = self.recover(); before = copy.deepcopy(self.client.objects)
        second = self.recover()
        self.assertTrue(second['reused']); self.assertFalse(second['admitted'])
        self.assertEqual(first['admission'], second['admission'])
        self.assertEqual(self.client.objects, before)

    def test_interrupted_final_claim_is_restored_without_duplicate_admission(self):
        saved = self.recover()
        key = self.store.key('recovered-publication-claims', recovery.request_hash(self.publication['request']), 'receipt.json')
        del self.client.objects[key]
        result = self.recover()
        self.assertTrue(result['reused']); self.assertEqual(result['admission'], saved['admission'])
        self.assertEqual(len(recovery.read_queue(self.store)), 1)
        self.assertIn(key, self.client.objects)

    def test_44_pages_33_locales_are_batched_24_then_20_without_retranslation(self):
        self.recover()
        first = prepare_queued(self.store, ADDITIONAL)
        self.assertEqual(len(json.loads(first['locale_jobs_json'])), 33)
        self.assertTrue(all(row == {'selected': 24, 'remaining': 20} for row in first['per_locale_counts'].values()))
        ordered = sorted(self.corpus['documents'], key=lambda doc: doc['url'])
        self.complete('fr', ordered)
        self.complete('pt', ordered[:24])
        second = prepare_queued(self.store, ('fr', 'pt', 'de'))
        self.assertNotIn('fr', json.loads(second['locales_json']))
        self.assertEqual(second['per_locale_counts']['pt'], {'selected': 20, 'remaining': 0})
        self.assertEqual(second['per_locale_counts']['de'], {'selected': 24, 'remaining': 20})

    def test_content_receipts_deduplicate_overlapping_publications(self):
        self.recover()
        self.complete('fr', self.corpus['documents'])
        value, pages = fixture(2, commit='e'*40)
        corpus, proof = capture(value, pages); self.recover(corpus, proof)
        self.assertFalse(prepare_queued(self.store, ('fr',))['has_work'])

    def test_finish_hot_batch_continues_older_admitted_cohort_only_after_progress(self):
        saved = self.recover()
        normal = daily_doc(ORIGIN+'/blog/20261010-new.html', day=CAPTURE)
        hot = admit(self.store, [normal], CAPTURE, PRODUCER)
        before = {'fr': 1}
        self.assertFalse(followup_needed(self.store, hot['admission'], ('fr',), before)['continue'])
        self.complete('fr', [normal], CAPTURE)
        self.assertTrue(followup_needed(self.store, hot['admission'], ('fr',), before)['continue'])
        self.assertEqual(prepare_queued(self.store, ('fr',))['source_admission'], saved['admission'])
        self.complete('fr', self.corpus['documents'])
        self.assertFalse(followup_needed(self.store, hot['admission'], ('fr',), before)['continue'])

    def test_corrupt_proof_rejected_and_capacity_never_discards_pending_cohorts(self):
        broken = copy.deepcopy(self.proof); broken['sources'] = {}
        with self.assertRaises(ExpansionError): self.recover(proof=broken)
        self.assertFalse(self.client.objects)
        with mock.patch.object(recovery, 'MAX_COHORTS', 1):
            self.recover(); before = copy.deepcopy(self.client.objects)
            other, pages = fixture(1, start=100); corpus, proof = capture(other, pages)
            with self.assertRaises(ExpansionError): self.recover(corpus, proof)
            self.assertEqual(self.client.objects, before)

    def test_review_checks_real_capture_day_and_exact_source_producer(self):
        from review_portal_extended_handoff import admission_is_valid
        saved = self.recover(); receipt = read_admission(self.store, saved['admission'])
        origin = queue_tests.SourceProvenanceTests(); origin.setUp()
        jobs = copy.deepcopy(origin.jobs)
        jobs[0].update(started_at=CAPTURE+'T01:00:00Z', completed_at=CAPTURE+'T01:05:00Z')
        admission_is_valid(receipt, origin.run, jobs, 'example/repo')
        with self.assertRaises(ExpansionError): admission_is_valid(receipt, origin.run, origin.jobs, 'example/repo')
        with self.assertRaises(ExpansionError): admission_is_valid(receipt, {**origin.run, 'run_attempt': 2}, jobs, 'example/repo')

    def test_workflow_reuses_source_lock_and_existing_global_two_worker_pipeline(self):
        import yaml
        root = Path(__file__).resolve().parents[1]
        source = yaml.safe_load((root/'.github/workflows/portal-extended-locales-source.yml').read_text())
        self.assertEqual(source['concurrency']['group'], 'extended-locales-source-admission')
        self.assertFalse(source['concurrency']['cancel-in-progress'])
        self.assertEqual(set(source['jobs']), {'source_snapshot'})
        self.assertIn('Recover report article delivery', (root/'.github/workflows/portal-extended-locales-source.yml').read_text())
        pipeline = yaml.safe_load((root/'.github/workflows/portal-extended-locales-r2.yml').read_text())
        self.assertEqual(pipeline['jobs']['locale']['strategy']['max-parallel'], 2)
        self.assertIn('extended-locales-r2-pipeline', pipeline['concurrency']['group'])

    def test_cli_exact_route_does_not_discover_latest_or_admit_english(self):
        from portal_extended_daily_queue import main
        value, pages = fixture(2)
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'KC_PUBLIC_REPOSITORY': 'true',
               'GITHUB_RUN_ID': '321', 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': 'a'*40, 'GITHUB_REPOSITORY': 'example/repo'}
        output = io.StringIO()
        with mock.patch.dict('os.environ', env), \
             mock.patch('sys.argv', ['source', '--recovered-publication-run', '300']), \
             mock.patch('portal_extended_daily_queue.R2Store.from_env', return_value=self.store), \
             mock.patch('portal_extended_daily_queue.today', return_value=CAPTURE), \
             mock.patch.object(recovery, 'GitHub', return_value=FakeGitHub(value)), \
             mock.patch.object(recovery, 'read_release', return_value=RELEASE), \
             mock.patch.object(recovery, 'read_public', side_effect=lambda session, url: pages[url]), \
             mock.patch('portal_extended_source_refresh.collect_refresh') as latest, \
             mock.patch('portal_english_commentary.freeze_editorial') as english, \
             mock.patch('sys.stdout', output):
            main()
        latest.assert_not_called(); english.assert_not_called()
        result = json.loads(output.getvalue())
        self.assertEqual(result['pages'], 2); self.assertEqual(result['selection_policy'], recovery.POLICY)
        self.assertNotIn('/blog/', output.getvalue()); self.assertNotIn('来源', output.getvalue())

    def test_corrupted_stored_proof_never_becomes_empty_queue_or_new_source(self):
        saved = self.recover()
        receipt = read_admission(self.store, saved['admission'])
        key = self.store.key('recovered-publications', receipt['recovery'], 'proof.json')
        self.client.objects[key]['Metadata']['sha256'] = '0'*64
        before = copy.deepcopy(self.client.objects)
        with self.assertRaises(R2IntegrityError): prepare_queued(self.store, ('fr',))
        self.assertEqual(self.client.objects, before)


if __name__ == '__main__':
    unittest.main()
