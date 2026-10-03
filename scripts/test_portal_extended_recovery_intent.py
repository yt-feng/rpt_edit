"""Fault injection for intent persistence, serialized adoption and publication gates."""
import copy
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import portal_extended_recovery_intent as intent
import portal_extended_incremental as incremental
from portal_extended_continuation import pending, queue, read_origin, save_queue
from portal_extended_locales import ExpansionError, file_for_url, make_corpus, stable_bytes
from portal_extended_publication import current_document
from portal_extended_r2 import R2IntegrityError, R2NotFound
import test_portal_extended_continuation as fixtures
from test_portal_extended_continuation import ENV, PRODUCER
from test_portal_extended_incremental import DAY, daily_doc, raw_page
from test_portal_extended_locales import ORIGIN


class IntentTests(unittest.TestCase):
    setUp = fixtures.ContinuationTests.setUp
    partial = fixtures.ContinuationTests.partial
    finish = fixtures.ContinuationTests.finish

    def api(self, path):
        if path.endswith('/jobs?per_page=100'):
            return {'total_count': len(self.jobs), 'jobs': copy.deepcopy(self.jobs)}
        self.assertEqual(path, 'repos/example/repo/actions/runs/123/attempts/1')
        return copy.deepcopy(self.run)

    def legacy(self):
        proof = self.partial(registered=False)
        return {'producer': PRODUCER, 'locales': {'fr': proof}}

    def submit(self, evidence):
        return intent.register_intent(self.store, self.gen, evidence, 'example/repo', self.api)

    def consume(self):
        return intent.consume_one(self.store, ('fr',), 'example/repo', self.api)

    def another_legacy(self):
        old_root, old_corpus, old_gen = self.root, self.corpus, self.gen
        self.root = self.root/'other'; self.root.mkdir()
        self.corpus = make_corpus([daily_doc(body='<h1>Changed research</h1><p>Other market evidence.</p>'),
            daily_doc(ORIGIN+'/blog/20260925-second.html', body='<h1>Second page</h1><p>Second unique unfinished unit.</p>')])
        self.gen = self.corpus['documents_sha256']; self.store.put_source(self.corpus)
        evidence = self.legacy()
        value = (self.gen, evidence)
        self.root, self.corpus, self.gen = old_root, old_corpus, old_gen
        return value

    def test_registration_has_no_continuation_checkpoint_candidate_or_publication_writes(self):
        evidence = self.legacy(); before = copy.deepcopy(self.store.client.objects)
        identity = self.submit(evidence)
        self.assertEqual(len(intent.read_index(self.store)), 1)
        self.assertIsNone(read_origin(self.store, self.gen)); self.assertEqual(queue(self.store, 'fr'), {})
        for key, value in before.items(): self.assertEqual(self.store.client.objects[key], value)
        added = set(self.store.client.objects)-set(before)
        self.assertEqual(added, {intent.key(self.store, 'index.json'), intent.key(self.store, identity, 'receipt.json')})
        self.assertFalse(intent.acknowledged(self.store, identity))
        self.assertEqual(self.submit(evidence), identity)

    def test_original_source_and_exact_proofs_revalidated_before_source_adoption(self):
        evidence = self.legacy(); identity = self.submit(evidence)
        with patch.object(intent, 'validate_existing', wraps=intent.validate_existing) as validate:
            self.assertEqual(self.consume(), identity)
        validate.assert_called_once()
        row = queue(self.store, 'fr')[self.gen]
        self.assertEqual((row['status'], row['continuations']), ('incomplete', 0))
        self.assertTrue(intent.acknowledged(self.store, identity))
        self.assertEqual(read_origin(self.store, self.gen)['producer'], PRODUCER)
        with patch.dict(os.environ, ENV): self.finish()
        advanced = copy.deepcopy(self.store.client.objects)
        self.assertEqual(self.submit(evidence), identity)
        self.assertIsNone(self.consume())
        self.assertEqual(advanced, self.store.client.objects)

    def test_registration_can_append_during_consumer_snapshot_without_lost_intent(self):
        evidence = self.legacy(); first = self.submit(evidence)
        generation, other = self.another_legacy()
        read = intent.read_index; appended = []
        def concurrent_read(store):
            snapshot = read(store)
            with patch.object(intent, 'read_index', read):
                appended.append(intent.register_intent(store, generation, other, 'example/repo', self.api))
            return snapshot
        with patch.object(intent, 'read_index', concurrent_read):
            self.assertEqual(self.consume(), first)
        self.assertEqual(len(read(self.store)), 2)
        self.assertFalse(intent.acknowledged(self.store, appended[0]))
        self.assertIsNone(read_origin(self.store, generation))
        self.assertEqual(self.consume(), appended[0])

    def test_receipt_before_index_crash_is_inert_and_retry_reuses_exact_receipt(self):
        evidence = self.legacy()
        with patch.object(intent, 'write_verified', side_effect=RuntimeError('synthetic index crash')):
            with self.assertRaises(RuntimeError): self.submit(evidence)
        self.assertEqual(intent.read_index(self.store), [])
        self.assertIsNone(self.consume()); self.assertEqual(queue(self.store, 'fr'), {})
        receipts = {k: v for k, v in self.store.client.objects.items() if '/legacy-recovery-intents/' in k}
        self.assertEqual(len(receipts), 1)
        self.submit(evidence)
        for k, v in receipts.items(): self.assertEqual(self.store.client.objects[k], v)
        self.assertIsNotNone(self.consume())

    def test_crashes_at_every_adoption_write_resume_without_reset_or_duplicate_claim(self):
        evidence = self.legacy()
        evidence['locales']['pt'] = self.partial(registered=False, locale='pt')
        self.jobs.append({'name': 'locale (pt)', 'status': 'completed', 'conclusion': 'failure'})
        identity = self.submit(evidence)
        consume = lambda: intent.consume_one(self.store, ('fr', 'pt'), 'example/repo', self.api)
        baseline = copy.deepcopy(self.store.client.objects)
        writes = []; original = self.store._put
        def capture(key, *args, **kwargs):
            writes.append(key); return original(key, *args, **kwargs)
        with patch.object(self.store, '_put', capture): consume()
        self.assertGreaterEqual(len(writes), 9)
        self.assertTrue(any(k.endswith('ack.json') for k in writes))
        for stop in range(len(writes)):
            with self.subTest(write=stop):
                self.store.client.objects = copy.deepcopy(baseline); count = [0]
                def crash(key, *args, **kwargs):
                    if count[0] == stop: raise RuntimeError('synthetic process death')
                    count[0] += 1
                    return original(key, *args, **kwargs)
                with patch.object(self.store, '_put', crash):
                    with self.assertRaises(RuntimeError): consume()
                self.assertEqual(consume(), identity)
                self.assertTrue(intent.acknowledged(self.store, identity))
                self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], 0)
                with patch.dict(os.environ, ENV): pending(self.store, ('fr',), self.root/'resumed.json')
                advanced = copy.deepcopy(self.store.client.objects)
                self.assertIsNone(consume()); self.assertEqual(self.store.client.objects, advanced)
                self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], 1)

    def test_adoption_ack_crash_cannot_reset_an_advanced_generation(self):
        evidence = self.legacy(); identity = self.submit(evidence)
        put = self.store._put
        def crash(key, *args, **kwargs):
            if key.endswith('/ack.json'): raise RuntimeError('synthetic ack crash')
            return put(key, *args, **kwargs)
        with patch.object(self.store, '_put', crash):
            with self.assertRaises(RuntimeError): self.consume()
        with patch.dict(os.environ, ENV): pending(self.store, ('fr',), self.root/'claimed.json')
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'cannot reset'): self.consume()
        self.assertEqual(before, self.store.client.objects)
        self.assertFalse(intent.acknowledged(self.store, identity))

    def test_different_identity_for_same_generation_rejected_before_writes(self):
        evidence = self.legacy(); self.submit(evidence)
        changed = copy.deepcopy(evidence); changed['producer']['attempt'] = '2'
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'different immutable'): self.submit(changed)
        self.assertEqual(before, self.store.client.objects)

    def test_missing_or_changed_private_evidence_rejected_at_consumption(self):
        evidence = self.legacy(); self.submit(evidence)
        proof = evidence['locales']['fr']
        keys = [self.store.source_key(self.gen),
            self.store.checkpoint_object_key('fr', self.gen, proof['checkpoint_sha256']),
            self.store.candidate_manifest_key('fr', self.gen, proof['candidate_id'])]
        baseline = copy.deepcopy(self.store.client.objects)
        for key in keys:
            with self.subTest(key=key.rsplit('/', 1)[-1]):
                self.store.client.objects = copy.deepcopy(baseline)
                del self.store.client.objects[key]
                before = copy.deepcopy(self.store.client.objects)
                with self.assertRaises((ExpansionError, R2NotFound, R2IntegrityError)): self.consume()
                self.assertEqual(before, self.store.client.objects)
        self.store.client.objects = copy.deepcopy(baseline)
        changed = copy.deepcopy(self.corpus); changed['captured_at'] = 'modified'
        self.store._put(self.store.source_key(self.gen), stable_bytes(changed), metadata={})
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaisesRegex(ExpansionError, 'source differs'): self.consume()
        self.assertEqual(before, self.store.client.objects)

    def test_missing_or_modified_completed_candidate_bytes_fail_registration_and_consumption(self):
        evidence = self.legacy(); proof = evidence['locales']['fr']
        manifest = json.loads(self.store._get(self.store.candidate_manifest_key('fr', self.gen, proof['candidate_id']), maximum=2*1024*1024))
        key = self.store.candidate_key('fr', self.gen, proof['candidate_id'], manifest['pages'][0]['path'])
        baseline = copy.deepcopy(self.store.client.objects)
        for registered in (False, True):
            self.store.client.objects = copy.deepcopy(baseline)
            if registered: self.submit(evidence)
            registered_baseline = copy.deepcopy(self.store.client.objects)
            for mutation in ('missing', 'changed'):
                with self.subTest(registered=registered, mutation=mutation):
                    self.store.client.objects = copy.deepcopy(registered_baseline)
                    if mutation == 'missing': del self.store.client.objects[key]
                    else: self.store._put(key, b'<html>unproved replacement</html>', metadata={})
                    before = copy.deepcopy(self.store.client.objects)
                    with self.assertRaises((ExpansionError, R2NotFound)):
                        self.consume() if registered else self.submit(evidence)
                    self.assertEqual(before, self.store.client.objects)

    def test_changed_terminal_run_identity_fails_revalidation_without_writes(self):
        evidence = self.legacy(); self.submit(evidence)
        before = copy.deepcopy(self.store.client.objects)
        for field, value in [('status', 'in_progress'), ('run_attempt', 2), ('head_sha', 'f'*40)]:
            with self.subTest(field=field):
                original = self.run[field]; self.run[field] = value
                with self.assertRaises(ExpansionError): self.consume()
                self.run[field] = original
                self.assertEqual(before, self.store.client.objects)

    def test_malformed_unknown_english_and_duplicate_index_are_fail_closed(self):
        evidence = self.legacy()
        for change in ('unknown', 'malformed', 'english'):
            value = copy.deepcopy(evidence)
            if change == 'unknown': value['private-source-text'] = 'not allowed'
            if change == 'malformed': value['locales']['fr']['candidate_id'] = 'bad'
            if change == 'english': value['locales']['en'] = value['locales'].pop('fr')
            before = copy.deepcopy(self.store.client.objects)
            with self.assertRaises(ExpansionError): self.submit(value)
            self.assertEqual(before, self.store.client.objects)
        self.submit(evidence)
        rows = intent.read_index(self.store)
        self.store._put(intent.key(self.store, 'index.json'), stable_bytes({'schema_version': 1,
            'policy': intent.POLICY, 'entries': rows+rows}), metadata={})
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaises(ExpansionError): self.consume()
        self.assertEqual(before, self.store.client.objects)

    def test_bound_and_requested_locale_scope_never_evict_or_silently_expand(self):
        evidence = self.legacy(); first = self.submit(evidence)
        before = copy.deepcopy(self.store.client.objects)
        self.assertIsNone(intent.consume_one(self.store, ('pt',), 'example/repo', self.api))
        self.assertEqual(before, self.store.client.objects)
        generation, other = self.another_legacy(); before = copy.deepcopy(self.store.client.objects)
        with patch.object(intent, 'MAX_INTENTS', 1):
            with self.assertRaisesRegex(ExpansionError, 'index is full'):
                intent.register_intent(self.store, generation, other, 'example/repo', self.api)
        self.assertEqual(before, self.store.client.objects)
        self.assertFalse(intent.acknowledged(self.store, first))

    def test_source_prepare_consumes_before_selecting_new_work_and_keeps_english_separate(self):
        evidence = self.legacy(); identity = self.submit(evidence)
        args = ['test', 'prepare', '--locales', 'fr', '--corpus', str(self.root/'source.json'), '--include-english']
        with patch.dict(os.environ, {**ENV, 'KC_PUBLIC_REPOSITORY': 'true'}), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store), \
             patch.object(incremental, 'today', return_value='2026-10-02'), \
             patch('review_portal_extended_handoff.api', self.api), \
             patch.object(incremental, 'include_english_matrix', side_effect=lambda store, result: result) as english, \
             patch.object(incremental.requests, 'Session', side_effect=AssertionError('No new collection')):
            self.assertEqual(incremental.main(), 0)
        self.assertTrue(intent.acknowledged(self.store, identity)); english.assert_called_once()
        self.assertEqual((self.root/'source.json').read_bytes(), stable_bytes(self.corpus))
        self.assertEqual(queue(self.store, 'fr')[self.gen]['continuations'], 1)

    def test_recovery_test_does_not_consume_intent_or_claim_production_work(self):
        evidence = self.legacy(); identity = self.submit(evidence)
        args = ['test', 'prepare-recovery', '--generation', self.gen, '--locales', 'fr', '--corpus', str(self.root/'recovery.json')]
        before = copy.deepcopy(self.store.client.objects)
        with patch.dict(os.environ, ENV), patch('sys.argv', args), \
             patch.object(incremental.R2Store, 'from_env', return_value=self.store):
            self.assertEqual(incremental.main(), 0)
        self.assertEqual(before, self.store.client.objects)
        self.assertFalse(intent.acknowledged(self.store, identity))

    def test_completed_legacy_candidate_cannot_override_newer_current_source(self):
        evidence = self.legacy(); self.submit(evidence); self.consume()
        with patch.dict(os.environ, ENV): self.finish()
        original = self.corpus['documents'][0]
        path = self.root/file_for_url(original['url']); path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(raw_page(body='<h1>Research note</h1><p>Newer source findings must remain authoritative.</p>'))
        before = path.read_bytes()
        with self.assertRaisesRegex(ExpansionError, 'source content changed'):
            current_document(self.root, original)
        self.assertEqual(path.read_bytes(), before)
        self.assertEqual(queue(self.store, 'fr')[self.gen]['status'], 'complete')

    def test_cli_requires_exact_public_main_registration_workflow_and_public_summary_is_safe(self):
        evidence = self.legacy()
        args = ['test', '--generation', self.gen, '--evidence', json.dumps(evidence),
                '--output', str(self.root/'public-summary.json')]
        environment = {**ENV, 'KC_PUBLIC_REPOSITORY': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
            'GITHUB_WORKFLOW_REF': 'example/repo/'+intent.WORKFLOW+'@refs/heads/main'}
        for field, value in [('GITHUB_ACTIONS', 'false'), ('GITHUB_REF', 'refs/pull/1/merge'),
                             ('KC_PUBLIC_REPOSITORY', 'false'), ('GITHUB_EVENT_NAME', 'workflow_run'),
                             ('GITHUB_WORKFLOW_REF', 'example/repo/other.yml@refs/heads/main')]:
            with self.subTest(field=field), patch.dict(os.environ, {**environment, field: value}), \
                 patch('sys.argv', args), patch.object(intent.R2Store, 'from_env') as storage:
                with self.assertRaisesRegex(ExpansionError, 'requires reviewed main'): intent.main()
                storage.assert_not_called()
        with patch.dict(os.environ, environment), patch('sys.argv', args), \
             patch.object(intent.R2Store, 'from_env', return_value=self.store), \
             patch('review_portal_extended_handoff.api', self.api):
            self.assertEqual(intent.main(), 0)
        summary = json.loads((self.root/'public-summary.json').read_bytes())
        self.assertEqual(set(summary), {'schema_version', 'intent', 'generation', 'status',
                                       'paid_provider_requests', 'translation_calls'})
        self.assertEqual((summary['paid_provider_requests'], summary['translation_calls']), (0, 0))
        self.assertNotIn(ORIGIN, json.dumps(summary))
        self.assertNotIn('New market findings', json.dumps(summary))
        self.assertIsNone(read_origin(self.store, self.gen))

    def test_tampered_receipt_ack_or_unowned_origin_rejected_without_mutation(self):
        evidence = self.legacy(); identity = self.submit(evidence)
        baseline = copy.deepcopy(self.store.client.objects)
        for filename in ('receipt.json', 'ack.json'):
            with self.subTest(filename=filename):
                self.store.client.objects = copy.deepcopy(baseline)
                self.store._put(intent.key(self.store, identity, filename), b'{"private":"malformed"}', metadata={})
                before = copy.deepcopy(self.store.client.objects)
                with self.assertRaises(ExpansionError): self.consume()
                self.assertEqual(before, self.store.client.objects)
        self.store.client.objects = copy.deepcopy(baseline)
        intent.register(self.store, self.corpus, ('fr',), PRODUCER)
        before = copy.deepcopy(self.store.client.objects)
        with self.assertRaises(R2NotFound): self.consume()
        self.assertEqual(before, self.store.client.objects)

    def test_registration_workflow_is_main_only_separate_serialized_and_no_model_or_dispatch(self):
        root = Path(__file__).resolve().parent.parent
        text = (root/'.github/workflows/portal-extended-recovery-intent.yml').read_text()
        self.assertIn('group: extended-legacy-recovery-intent-registration', text)
        self.assertIn('cancel-in-progress: false', text)
        self.assertIn("github.ref == 'refs/heads/main' && github.event.repository.private == false", text)
        self.assertIn('actions: read', text)
        self.assertNotIn('actions: write', text)
        self.assertNotIn('setup-offline-translation', text)
        self.assertNotIn('workflow run', text)
        self.assertNotIn('upload-artifact@v4\n        with:\n          path: scripts', text)
        pipeline = (root/'.github/workflows/portal-extended-locales-r2.yml').read_text()
        self.assertIn("|| 'extended-locales-r2-pipeline'", pipeline)
        self.assertIn('max-parallel: 2', pipeline)


if __name__ == '__main__': unittest.main()
