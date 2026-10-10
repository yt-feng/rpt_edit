"""Real filesystem checkpoints with a local durable store and fake provider."""
import copy
from concurrent.futures import ThreadPoolExecutor
import json
from pathlib import Path
import shutil
import tempfile
import threading
import unittest
from unittest.mock import Mock, patch

import article_generation_progress as progress


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / 'article'
        self.store = self.root / 'durable'
        self.identity = {'source_sha256': 'a' * 64, 'source_receipt_sha256': 'b' * 64,
                         'generation_contract_sha256': 'c' * 64, 'source_kind': 'ocr-pages'}
        self.saved_states = []
        self.calls = []

    def persist(self):
        state = json.loads((self.directory / progress.RECEIPT).read_bytes())
        self.saved_states.append(copy.deepcopy(state))
        shutil.copytree(self.directory, self.store, dirs_exist_ok=True)

    def make(self, *, persist=None, identity=None):
        return progress.Progress(self.directory, identity=identity or self.identity,
                                 persist=self.persist if persist is None else persist)

    def call(self, response):
        def invoke():
            state = json.loads((self.store / progress.RECEIPT).read_bytes())
            self.assertEqual(state['requests'][-1]['state'], 'pending')
            self.calls.append(state['requests'][-1]['kind'])
            return response
        return invoke

    def body(self, checkpoint=None):
        return (checkpoint or self.make()).request('body', 'PRIVATE source body prompt', {'model': 'test', 'temperature': 0.38},
                                                   self.call('# 原标题\n\n已生成的正文。\n'))

    def load(self):
        return json.loads((self.directory / progress.RECEIPT).read_bytes())

    def write(self, state):
        (self.directory / progress.RECEIPT).write_bytes(progress.encoded(state))

    def test_body_and_title_each_persist_intent_before_call_and_result_after_call(self):
        checkpoint = self.make()
        self.assertIsNone(checkpoint.saved_body())
        body = self.body(checkpoint)
        title = checkpoint.request('title', 'PRIVATE title prompt', {'model': 'test'}, self.call('{"title":"资料标题"}'))
        self.assertEqual([state['requests'][-1]['state'] for state in self.saved_states],
                         ['pending', 'complete', 'pending', 'complete'])
        self.assertEqual(self.calls, ['body', 'title'])
        self.assertEqual(checkpoint.saved_body(), body)
        self.assertEqual(title, '{"title":"资料标题"}')
        self.assertNotIn('PRIVATE', (self.directory / progress.RECEIPT).read_text())

    def test_fresh_process_and_restored_checkpoint_reuse_identical_responses_without_provider(self):
        body = self.body()
        checkpoint = self.make()
        title = checkpoint.request('title', 'title prompt', {'model': 'test'}, self.call('accepted title'))
        shutil.rmtree(self.directory)
        shutil.copytree(self.store, self.directory)
        no_call = Mock(side_effect=AssertionError('provider forbidden'))
        checkpoint = self.make()
        self.assertEqual(checkpoint.request('body', 'PRIVATE source body prompt', {'temperature': 0.38, 'model': 'test'}, no_call), body)
        self.assertEqual(checkpoint.request('title', 'title prompt', {'model': 'test'}, no_call), title)
        self.assertEqual(checkpoint.saved_body(), body)
        no_call.assert_not_called()
        self.assertEqual(len(self.saved_states), 4)

    def test_unknown_body_submission_survives_restore_and_blocks_every_changed_request(self):
        def timeout():
            self.assertEqual(json.loads((self.store / progress.RECEIPT).read_bytes())['requests'][0]['state'], 'pending')
            raise TimeoutError('PRIVATE provider outcome unknown')
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_request_pending$'):
            self.make().request('body', 'body', {}, timeout)
        shutil.rmtree(self.directory)
        shutil.copytree(self.store, self.directory)
        checkpoint = self.make()
        for kind, prompt in [('body', 'body'), ('body', 'changed'), ('title', 'changed')]:
            call = Mock()
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_pending$'):
                checkpoint.request(kind, prompt, {}, call)
            call.assert_not_called()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_pending$'):
            checkpoint.saved_body()
        self.assertEqual(self.load()['requests'][0]['state'], 'pending')

    def test_unknown_title_blocks_new_title_but_saved_body_is_reusable(self):
        body = self.body()
        checkpoint = self.make()
        with self.assertRaises(progress.ProgressError):
            checkpoint.request('title', 'title A', {}, Mock(side_effect=TimeoutError()))
        self.assertEqual(self.make().saved_body(), body)
        for prompt in ('title A', 'title B'):
            no_call = Mock()
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_pending$'):
                self.make().request('title', prompt, {}, no_call)
            no_call.assert_not_called()

    def test_intent_persistence_failure_submits_nothing_and_retains_pending(self):
        persist, call = Mock(side_effect=OSError('PRIVATE storage')), Mock()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_intent_persistence_failed$'):
            self.make(persist=persist).request('body', 'body', {}, call)
        call.assert_not_called()
        self.assertEqual(self.load()['requests'][0]['state'], 'pending')
        with self.assertRaises(progress.ProgressError):
            self.make().request('body', 'body', {}, call)
        call.assert_not_called()

    def test_result_persistence_failure_returns_to_pending_without_repeating_call(self):
        def persist():
            if len(self.saved_states) == 1:
                raise OSError('PRIVATE result save failed')
            self.persist()
        call = Mock(return_value='known response')
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_result_persistence_failed$'):
            self.make(persist=persist).request('body', 'body', {}, call)
        self.assertEqual(call.call_count, 1)
        self.assertEqual(self.load()['requests'][0]['state'], 'pending')
        self.assertEqual(len(list(self.directory.glob(progress.RESPONSE_PREFIX + '*.txt'))), 1)
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_pending$'):
            self.make().request('body', 'body', {}, call)
        self.assertEqual(call.call_count, 1)

    def test_best_effort_false_persistence_cannot_grant_a_provider_call(self):
        call = Mock()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_intent_persistence_failed$'):
            self.make(persist=lambda: False).request('body', 'body', {}, call)
        call.assert_not_called()
        self.assertEqual(self.load()['requests'][0]['state'], 'pending')

    def test_nonfinite_options_and_invalid_request_kinds_stop_before_state_or_call(self):
        checkpoint = self.make()
        call = Mock()
        for kind, options in [('body', {'temperature': float('nan')}), ([], {}), ('other', {})]:
            with self.assertRaises(progress.ProgressError):
                checkpoint.request(kind, 'body', options, call)
        call.assert_not_called()
        self.assertFalse((self.directory / progress.RECEIPT).exists())

    def test_changed_body_prompt_options_or_identity_cannot_open_a_second_body(self):
        self.body()
        no_call = Mock()
        for prompt, options in [('changed', {'model': 'test', 'temperature': 0.38}),
                                ('PRIVATE source body prompt', {'model': 'different', 'temperature': 0.38})]:
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_body_mismatch$'):
                self.make().request('body', prompt, options, no_call)
        for field in self.identity:
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_identity_mismatch$'):
                self.make(identity={**self.identity, field: 'changed'})
        no_call.assert_not_called()

    def test_title_limit_is_four_distinct_requests_across_resumes_and_replays_are_free(self):
        self.body()
        for index in range(4):
            self.make().request('title', 'title ' + str(index), {'model': 'test'}, self.call('title response ' + str(index)))
        no_call = Mock()
        self.assertEqual(self.make().request('title', 'title 0', {'model': 'test'}, no_call), 'title response 0')
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_title_budget$'):
            self.make().request('title', 'title 4', {'model': 'test'}, no_call)
        no_call.assert_not_called()
        self.assertEqual(self.calls, ['body', 'title', 'title', 'title', 'title'])

    def test_title_cannot_precede_body(self):
        call = Mock()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_body_missing$'):
            self.make().request('title', 'title', {}, call)
        call.assert_not_called()

    def test_corrupt_missing_symlink_or_unbound_response_blocks_reuse(self):
        self.body()
        response = self.directory / self.load()['requests'][0]['response_path']
        original = response.read_bytes()
        for defect in ('changed', 'missing', 'symlink'):
            response.unlink(missing_ok=True)
            if defect == 'changed': response.write_bytes(b'forged content')
            if defect == 'symlink': response.symlink_to(self.root / 'outside')
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_response_changed$'):
                self.make()
        response.unlink(missing_ok=True); response.write_bytes(original)
        (self.directory / (progress.RESPONSE_PREFIX + 'unbound.txt')).write_text('unbound')
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_response_unbound$'):
            self.make()

    def test_state_deletion_cannot_hide_previous_requests(self):
        self.body()
        (self.directory / progress.RECEIPT).unlink()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_state_missing$'):
            self.make()

    def test_malformed_state_requests_and_duplicate_keys_fail_closed(self):
        self.body()
        original = self.load()
        mutations = [lambda s: s.update(schema_version=True), lambda s: s.update(extra=True),
                     lambda s: s['requests'].append(copy.deepcopy(s['requests'][0])),
                     lambda s: s['requests'][0].update(id='0' * 64),
                     lambda s: s['requests'][0].update(response_bytes=True),
                     lambda s: s['requests'][0].update(response_path='../outside'),
                     lambda s: s['requests'][0].update(kind=[]),
                     lambda s: s['requests'][0].update(proof={}),
                     lambda s: s['requests'][0].update(state='pending')]
        for mutate in mutations:
            state = copy.deepcopy(original); mutate(state); self.write(state)
            with self.assertRaises(progress.ProgressError): self.make()
        (self.directory / progress.RECEIPT).write_text('{"schema_version":1,"schema_version":1}')
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_json_invalid$'): self.make()

    def test_empty_or_oversized_provider_response_leaves_request_pending(self):
        for response in ('', ' ', None, '\ud800', 'x' * (progress.MAX_RESPONSE_BYTES + 1)):
            with self.subTest(kind=type(response).__name__):
                if self.directory.exists(): shutil.rmtree(self.directory)
                with self.assertRaisesRegex(progress.ProgressError, '^article_progress_request_pending$'):
                    self.make().request('body', 'body', {}, lambda: response)
                self.assertEqual(self.load()['requests'][0]['state'], 'pending')

    def test_seeded_legacy_body_is_proof_bound_reused_and_does_not_submit_body(self):
        proof = {'archive_sha256': 'd' * 64, 'source_ordinal': 28, 'body_sha256': progress.digest(b'known body')}
        checkpoint = self.make()
        checkpoint.seed_body('known body', proof=proof)
        self.assertEqual(checkpoint.saved_body(), 'known body')
        self.make().seed_body('known body', proof=proof)
        self.assertEqual(len(self.saved_states), 1)
        for body, value in [('changed', proof), ('known body', {**proof, 'source_ordinal': 29})]:
            with self.assertRaisesRegex(progress.ProgressError, '^article_progress_legacy_mismatch$'):
                self.make().seed_body(body, proof=value)
        no_call = Mock()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_body_mismatch$'):
            self.make().request('body', 'body', {}, no_call)
        no_call.assert_not_called()
        self.assertEqual(self.make().request('title', 'title', {}, self.call('new title')), 'new title')

    def test_seed_cannot_replace_normal_body_and_pending_body_cannot_be_seeded(self):
        self.body()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_legacy_mismatch$'):
            self.make().seed_body('known body', proof={'archive_sha256': 'd' * 64})
        shutil.rmtree(self.directory)
        with self.assertRaises(progress.ProgressError):
            self.make().request('body', 'body', {}, Mock(side_effect=TimeoutError()))
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_legacy_mismatch$'):
            self.make().seed_body('known body', proof={'archive_sha256': 'd' * 64})

    def test_failed_legacy_persistence_must_be_saved_before_subsequent_title_call(self):
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_legacy_persistence_failed$'):
            self.make(persist=Mock(side_effect=OSError())).seed_body('known body', proof={'archive_sha256': 'd' * 64})
        self.assertEqual(self.make().saved_body(), 'known body')
        self.make().request('title', 'title', {}, self.call('new title'))
        self.assertEqual(self.saved_states[0]['requests'][0]['origin'], 'legacy')
        self.assertEqual(self.saved_states[0]['requests'][0]['state'], 'complete')

    def test_two_local_workers_share_one_submission(self):
        entered, release = threading.Event(), threading.Event()
        def call():
            entered.set()
            self.assertTrue(release.wait(5))
            self.calls.append('body')
            return 'single result'
        with ThreadPoolExecutor(max_workers=2) as pool:
            first = pool.submit(lambda: self.make().request('body', 'body', {}, call))
            self.assertTrue(entered.wait(5))
            second = pool.submit(lambda: self.make().request('body', 'body', {}, call))
            release.set()
            self.assertEqual(first.result(5), 'single result')
            self.assertEqual(second.result(5), 'single result')
        self.assertEqual(self.calls, ['body'])


if __name__ == '__main__':
    unittest.main()
