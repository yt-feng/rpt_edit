#!/usr/bin/env python3
"""Offline crash, concurrency and exact-source recovery regressions."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import tempfile
import threading
import unittest
from unittest.mock import patch

import mineru_task_ledger as m
from mineru_terminal_recovery import TerminalRecovery, failure_hash

OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
TOKENS = [('MINER_U', 'secret-first'), ('MINER_U_2', 'secret-second')]
AUTH = {'run_id': '1234', 'manifest_sha256': 'a' * 64}
ERROR = {'err_code': 'PARSE_TRANSIENT', 'err_msg': 'temporary parsing failure', 'error': None}


class Provider:
    def __init__(self):
        self.posts, self.uploads, self.polls, self.tasks = [], [], [], {}
        self.plans = [['done', 'failed', 'failed'], ['done', 'failed'], ['done']]
        self.on_submit = None
        self.on_upload = None
        self.on_poll = None
        self.lock = threading.Lock()

    def submit(self, items, options, token, timeout):
        with self.lock:
            batch_id = str(len(self.posts) + 1)
            self.posts.append((copy.deepcopy(items), copy.deepcopy(options), token))
            self.tasks[batch_id] = copy.deepcopy(items)
        if self.on_submit:
            self.on_submit(batch_id)
        return batch_id, ['https://upload.invalid/' + row['id'] for row in items]

    def upload(self, url, raw, timeout):
        self.uploads.append((url, raw))
        if self.on_upload:
            self.on_upload()

    def poll(self, batch_id, token, timeout):
        self.polls.append((batch_id, token))
        items = self.tasks[batch_id]
        if self.on_poll:
            replacement = self.on_poll(batch_id, items)
            if replacement is not None:
                return replacement
        plan = self.plans[min(int(batch_id) - 1, len(self.plans) - 1)]
        return [{'data_id': item['id'], 'state': state,
                 **({'full_zip_url': 'https://results.invalid/' + batch_id + '/' + item['id']}
                    if state == 'done' else ERROR if state == 'failed' else {})}
                for item, state in zip(items, plan)]


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.folder = Path(self.temp.name)
        self.store = m.FileStore(self.folder / 'ledger')
        self.provider = Provider()
        self.now = 0
        self.inputs = []
        for index in range(3):
            path = self.folder / f'{index}.pdf'
            path.write_bytes(b'%PDF-original-' + str(index).encode())
            self.inputs.append((path, f'dropbox/261003/report-{index}.pdf'))
        ledger = self.ledger()
        items = [ledger.bind(*entry) for entry in self.inputs]
        self.root_key = ledger._create(items, {row['id']: path for row, (path, _) in zip(items, self.inputs)}, 20)
        self.original = {path.relative_to(self.folder / 'ledger').as_posix(): path.read_bytes()
                         for path in (self.folder / 'ledger').rglob('*.json')}

    def ledger(self, *, tokens=TOKENS, store=None):
        return m.Ledger(store or self.store, self.provider, 'daily', 'https://mineru.net', OPTIONS,
                        tokens, clock=lambda: self.now, sleep=self.sleep)

    def sleep(self, seconds):
        self.now += seconds

    def run_recovery(self, *, allow=True, inputs=None, codes=(), authorization=AUTH,
                     done_verifier=None, ledger=None):
        return TerminalRecovery(ledger or self.ledger(), allowed_error_codes=codes,
                                allowed_error_hashes=[failure_hash(ERROR)] if allow else []).run(
            self.inputs if inputs is None else inputs, authorization=authorization, timeout=20,
            interval=2, queue_budget=4, done_verifier=done_verifier)

    def control(self):
        paths = list((self.folder / 'ledger/recoveries').glob('*.json'))
        self.assertEqual(len(paths), 1)
        return json.loads(paths[0].read_bytes())

    def assert_original_unchanged(self):
        for name, raw in self.original.items():
            self.assertEqual((self.folder / 'ledger' / name).read_bytes(), raw)

    def test_complete_original_inventory_with_root_and_two_children_has_exact_lineage(self):
        verified = []
        rows, summary = self.run_recovery(done_verifier=lambda path, row: verified.append((path, row)))
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual((len(rows), summary['completed'], summary['provider_posts']), (3, 3, 2))
        self.assertEqual([len(row[0]) for row in self.provider.posts], [3, 2, 1])
        self.assertEqual([path for path, _ in rows], [path for path, _ in self.inputs])
        children = self.control()['children']
        for index, (_, row) in enumerate(rows):
            lineage = row['_recovery_lineage']
            self.assertEqual(set(lineage), {'batch_id', 'batch_key', 'parent_batch_key', 'data_id', 'child_ordinal'})
            self.assertEqual(lineage['batch_id'], str(index + 1))
            self.assertEqual(lineage['batch_key'], self.root_key if index == 0 else children[index - 1]['key'])
            self.assertEqual(lineage['parent_batch_key'], self.root_key)
            self.assertEqual(lineage['data_id'], row['data_id'])
            self.assertEqual(lineage['child_ordinal'], index)
        self.assertEqual([row['_recovery_lineage']['child_ordinal'] for _, row in verified], [0, 1, 2])
        self.assert_original_unchanged()

    def test_completed_controller_resume_reuses_all_tasks_and_original_credentials(self):
        self.run_recovery()
        rows, summary = self.run_recovery(ledger=self.ledger(tokens=list(reversed(TOKENS))))
        self.assertEqual((len(rows), summary['provider_posts'], len(self.provider.posts)), (3, 0, 3))
        self.assertTrue(all(token == TOKENS[0][1] for _, token in self.provider.polls))
        self.assert_original_unchanged()

    def test_all_done_original_needs_no_controller_or_posts(self):
        self.provider.plans[0] = ['done'] * 3
        rows, summary = self.run_recovery(allow=False)
        self.assertEqual((len(rows), summary['provider_posts'], len(self.provider.posts)), (3, 0, 1))
        self.assertFalse((self.folder / 'ledger/recoveries').exists())
        self.assert_original_unchanged()

    def test_two_children_is_lifetime_bound_even_across_days(self):
        self.provider.plans = [['failed'] * 3] * 3
        for _ in range(3):
            rows, summary = self.run_recovery()
            self.assertEqual(rows, [])
            self.assertFalse(summary['ready_for_generation'])
            self.assertEqual(summary['failed'], 3)
            self.now += 86400
        self.assertEqual(len(self.control()['children']), 2)
        self.assertEqual(len(self.provider.posts), 3)
        self.assert_original_unchanged()

    def test_default_ledger_still_never_retries_terminal_failures(self):
        for _ in range(2):
            rows, summary = self.ledger().run(self.inputs, timeout=20)
            self.assertEqual(rows, [])
            self.assertEqual(summary['failed'], 2)
        self.assertEqual(len(self.provider.posts), 1)

    def test_empty_or_nonmatching_allowlists_stop_before_reservation(self):
        for code in ((), ('DIFFERENT_ERROR',)):
            with self.assertRaisesRegex(m.LedgerError, 'not explicitly authorized'):
                self.run_recovery(allow=False, codes=code)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertFalse((self.folder / 'ledger/recoveries').exists())

    def test_explicit_error_code_allowlist_can_authorize_exact_failed_members(self):
        rows, summary = self.run_recovery(allow=False, codes=('PARSE_TRANSIENT',))
        self.assertEqual(len(rows), 3)
        self.assertTrue(summary['ready_for_generation'])

    def test_policy_and_manifest_cannot_change_on_resume(self):
        self.run_recovery()
        before = len(self.provider.polls)
        with self.assertRaisesRegex(m.LedgerError, 'fixed policy'):
            self.run_recovery(allow=False, codes=('PARSE_TRANSIENT',))
        with self.assertRaisesRegex(m.LedgerError, 'frozen original manifest'):
            self.run_recovery(authorization=dict(AUTH, manifest_sha256='b' * 64))
        self.assertEqual(len(self.provider.polls), before)
        self.assertEqual(len(self.provider.posts), 3)

    def test_exact_original_member_inventory_required_before_get(self):
        for inputs in (self.inputs[:2], self.inputs + self.inputs[:1], [self.inputs[0]] * 3):
            with self.assertRaises(m.LedgerError):
                self.run_recovery(inputs=inputs)
        self.assertEqual(len(self.provider.polls), 0)
        self.assertEqual(len(self.provider.posts), 1)

    def test_changed_bytes_and_options_cannot_recover_existing_claim(self):
        self.inputs[0][0].write_bytes(b'changed')
        with self.assertRaises(m.LedgerError):
            self.run_recovery()
        self.assertEqual(len(self.provider.polls), 0)
        self.assertEqual(len(self.provider.posts), 1)

    def test_done_zip_failure_prevents_first_child_reservation(self):
        def fail(path, row):
            raise OSError('secret-first https://signed.invalid/?signature=secret')
        with self.assertRaisesRegex(m.LedgerError, 'OSError') as caught:
            self.run_recovery(done_verifier=fail)
        self.assertNotIn('secret', str(caught.exception))
        self.assertEqual(len(self.provider.posts), 1)
        self.assertFalse((self.folder / 'ledger/recoveries').exists())

    def test_done_child_zip_failure_prevents_second_child(self):
        def fail_child(path, row):
            if row['_recovery_lineage']['child_ordinal'] == 1:
                raise OSError('download TLS failure')
        with self.assertRaises(m.LedgerError):
            self.run_recovery(done_verifier=fail_child)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(self.control()['children']), 1)

    def test_bytes_mutation_in_done_verifier_stops_before_child(self):
        def mutate(path, row):
            self.inputs[2][0].write_bytes(b'changed in verifier')
        with self.assertRaisesRegex(m.LedgerError, 'bytes changed'):
            self.run_recovery(done_verifier=mutate)
        self.assertEqual(len(self.provider.posts), 1)

    def test_pending_original_or_truncated_rows_never_authorize_child(self):
        for states in (['done', 'pending', 'failed'], ['done']):
            self.provider.plans[0] = states
            rows, summary = self.run_recovery()
            self.assertEqual(rows, [])
            self.assertFalse(summary['ready_for_generation'])
            self.assertEqual(summary['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 1)

    def test_unknown_or_duplicate_results_stop_without_child(self):
        cases = [lambda items: [{'data_id': 'unknown', 'state': 'failed', **ERROR}],
                 lambda items: [{'data_id': items[0]['id'], 'state': 'failed', **ERROR}] * 2]
        for value in cases:
            self.provider.on_poll = lambda batch_id, items: value(items)
            with self.assertRaises(m.LedgerError):
                self.run_recovery()
        self.assertEqual(len(self.provider.posts), 1)

    def test_crash_after_controller_reservation_reuses_same_child(self):
        actual = self.store.put
        def write(key, value, previous=None):
            if value.get('recovery_parent') and value['state'] == 'claiming':
                raise OSError('runner died before child create')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=write), self.assertRaises(m.LedgerError):
            self.run_recovery()
        reserved = self.control()['children'][0]['key']
        rows, _ = self.run_recovery()
        self.assertEqual(len(rows), 3)
        self.assertEqual(self.control()['children'][0]['key'], reserved)
        self.assertEqual(len(self.provider.posts), 3)

    def test_crash_after_child_creation_before_submit_can_claim_same_child(self):
        actual = self.store.put
        def write(key, value, previous=None):
            if value.get('recovery_parent') and value['state'] == 'submitting':
                raise OSError('runner died before submission intent')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=write), self.assertRaises(m.LedgerError):
            self.run_recovery()
        reserved = self.control()['children'][0]['key']
        self.assertEqual(self.store.get(reserved)[0]['state'], 'claiming')
        rows, _ = self.run_recovery()
        self.assertEqual(len(rows), 3)
        self.assertEqual(self.control()['children'][0]['key'], reserved)

    def test_unknown_post_outcome_never_retries_or_reserves_second_child(self):
        self.provider.on_submit = lambda batch_id: (_ for _ in ()).throw(TimeoutError('secret-first'))
        with self.assertRaises(m.LedgerError):
            self.run_recovery()
        self.provider.on_submit = None
        for _ in range(2):
            with self.assertRaisesRegex(m.LedgerError, 'Ambiguous'):
                self.run_recovery()
        self.assertEqual(len(self.control()['children']), 1)
        self.assertEqual(len(self.provider.posts), 2)

    def test_crash_after_acceptance_before_upload_never_posts_existing_child_again(self):
        self.provider.on_upload = lambda: (_ for _ in ()).throw(OSError('lost upload'))
        with self.assertRaises(m.LedgerError):
            self.run_recovery()
        self.provider.on_upload = None
        child = self.store.get(self.control()['children'][0]['key'])[0]
        self.assertEqual((child['state'], child['batch_id']), ('accepted', '2'))
        rows, _ = self.run_recovery()
        self.assertEqual(len(rows), 3)
        self.assertEqual(len(self.provider.posts), 3)

    def test_crash_after_provider_acceptance_before_checkpoint_stays_ambiguous(self):
        actual = self.store.put
        def write(key, value, previous=None):
            if value.get('recovery_parent') and value['state'] == 'accepted':
                raise OSError('lost acceptance checkpoint')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=write), self.assertRaises(m.LedgerError):
            self.run_recovery()
        with self.assertRaisesRegex(m.LedgerError, 'Ambiguous'):
            self.run_recovery()
        self.assertEqual(len(self.provider.posts), 2)

    def test_concurrent_controller_creation_has_one_winner(self):
        self._concurrent_at('controller')

    def test_concurrent_claiming_to_submitting_has_one_winner(self):
        actual = self.store.put
        def write(key, value, previous=None):
            if value.get('recovery_parent') and value['state'] == 'submitting':
                raise OSError('pause before intent')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=write), self.assertRaises(m.LedgerError):
            self.run_recovery()
        self._concurrent_at('submitting')

    def _concurrent_at(self, stage):
        barrier = threading.Barrier(2)
        actual = self.store.put
        def write(key, value, previous=None):
            selected = ((stage == 'controller' and key.startswith('recoveries/') and previous is None)
                        or (stage == 'submitting' and value.get('recovery_parent')
                            and value.get('state') == 'submitting' and len(self.provider.posts) == 1))
            if selected:
                barrier.wait(timeout=5)
            return actual(key, value, previous)
        results = []
        def worker():
            try:
                results.append(self.run_recovery())
            except Exception as error:
                results.append(error)
        with patch.object(self.store, 'put', side_effect=write):
            threads = [threading.Thread(target=worker) for _ in range(2)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join(timeout=10)
                self.assertFalse(thread.is_alive())
        self.assertEqual(sum(isinstance(value, tuple) for value in results), 1)
        self.assertEqual(sum(isinstance(value, m.LedgerError) for value in results), 1)
        self.assertEqual(len(self.provider.posts), 3)
        self.assertEqual(len(self.control()['children']), 2)
        self.assert_original_unchanged()

    def test_checkpoint_does_not_store_tokens_signed_urls_or_source_bytes(self):
        self.run_recovery()
        raw = b'\n'.join(path.read_bytes() for path in (self.folder / 'ledger').rglob('*.json'))
        for secret in [token.encode() for _, token in TOKENS] + [b'https://results.invalid', b'%PDF-original']:
            self.assertNotIn(secret, raw)

    def test_pending_accepted_child_never_creates_a_second_child(self):
        self.provider.plans[1] = ['done', 'running']
        for _ in range(2):
            rows, summary = self.run_recovery()
            self.assertEqual(rows, [])
            self.assertFalse(summary['ready_for_generation'])
            self.assertEqual(summary['pending'], 1)
        self.assertEqual(len(self.control()['children']), 1)
        self.assertEqual(len(self.provider.posts), 2)
        self.assert_original_unchanged()

    def test_child_auth_rejection_switches_key_on_same_reserved_child(self):
        actual = self.provider.submit
        attempts = []
        def submit(items, options, token, timeout):
            attempts.append((tuple(item['id'] for item in items), token))
            if token == TOKENS[0][1]:
                raise m.DefinitiveAuthRejection('A0211', 200)
            return actual(items, options, token, timeout)
        with patch.object(self.provider, 'submit', side_effect=submit):
            rows, summary = self.run_recovery()
        self.assertEqual((len(rows), summary['provider_posts']), (3, 4))
        self.assertEqual(attempts[0][0], attempts[1][0])
        self.assertEqual(attempts[2][0], attempts[3][0])
        for entry in self.control()['children']:
            child = self.store.get(entry['key'])[0]
            self.assertEqual(child['auth_rejections'][0]['token_identity'], entry['initial_token_identity'])
            self.assertEqual(child['token_identity'], m.token_fingerprint(TOKENS[1][1]))
        self.assertEqual(len(self.provider.posts), 3)
        self.assert_original_unchanged()

    def test_tampered_child_credential_without_rejection_stops_before_post(self):
        self.run_recovery()
        key = self.control()['children'][0]['key']
        child, version = self.store.get(key)
        child['token_identity'] = m.token_fingerprint(TOKENS[1][1])
        self.store.put(key, child, version)
        with self.assertRaisesRegex(m.LedgerError, 'credential changed'):
            self.run_recovery()
        self.assertEqual(len(self.provider.posts), 3)

    def test_tampered_reservation_members_and_proof_stop_before_child_post(self):
        actual = self.store.put
        def pause(key, value, previous=None):
            if value.get('recovery_parent'):
                raise OSError('pause before child')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=pause), self.assertRaises(m.LedgerError):
            self.run_recovery()
        control_key = 'recoveries/' + self.root_key.split('/')[1]
        original, version = self.store.get(control_key)
        mutations = [lambda c: c['children'][0].update(file_ids=[]),
                     lambda c: c['children'][0].update(ordinal=True),
                     lambda c: c['children'][0]['proof'].update(sha256='f' * 64),
                     lambda c: c.update(root_identity_sha256='f' * 64)]
        for mutate in mutations:
            bad = copy.deepcopy(original)
            mutate(bad)
            current = self.store.put(control_key, bad, version)
            with self.assertRaises(m.LedgerError):
                self.run_recovery()
            version = self.store.put(control_key, original, current)
        self.assertEqual(len(self.provider.posts), 1)

    def test_invalid_authorization_and_unbounded_timing_rejected_before_get(self):
        for auth in [None, {}, dict(AUTH, run_id='0'), dict(AUTH, run_id=1234),
                     dict(AUTH, manifest_sha256='A' * 64), dict(AUTH, extra=True)]:
            with self.assertRaises(m.LedgerError):
                self.run_recovery(authorization=auth)
        recovery = TerminalRecovery(self.ledger(), allowed_error_hashes=[failure_hash(ERROR)])
        for values in [(float('inf'), 1, 1), (1, float('nan'), 1), (1, 1, -1), (True, 1, 1)]:
            with self.assertRaises(m.LedgerError):
                recovery.run(self.inputs, authorization=AUTH, timeout=values[0],
                             interval=values[1], queue_budget=values[2])
        self.assertEqual(len(self.provider.polls), 0)
        self.assertEqual(len(self.provider.posts), 1)

    def test_r2_identical_competing_write_never_counts_as_lost_ack(self):
        from test_mineru_task_ledger import FakeR2
        store = m.R2Store('daily', client=FakeR2(), bucket='private')
        key = 'batches/' + 'a' * 32
        value = {'state': 'claiming'}
        version = store.put(key, value)
        with self.assertRaisesRegex(m.LedgerError, 'compare-and-swap'):
            store.put(key, value)
        changed = dict(value, state='submitting')
        store.put(key, changed, version)
        with self.assertRaisesRegex(m.LedgerError, 'compare-and-swap'):
            store.put(key, changed, version)

    def test_r2_concurrent_submission_intents_have_one_post_owner(self):
        from test_mineru_task_ledger import FakeR2
        client = FakeR2()
        store = m.R2Store('daily', client=client, bucket='private')
        for name, raw in self.original.items():
            store.put(name.removesuffix('.json'), json.loads(raw))
        recovery = TerminalRecovery(self.ledger(store=store), allowed_error_hashes=[failure_hash(ERROR)])
        root, paths = recovery._original(self.inputs)
        rows, _ = recovery._poll(root, root, paths, 20, 2, 4, 0, None)
        key, _, _ = recovery._read_control(root)
        control = recovery._reserve(root, key, None, None, root, rows, AUTH)
        recovery._child(root, key, control['children'][0], create=True)
        actual = client.put_object
        barrier, lock = threading.Barrier(2), threading.Lock()
        intents, results = [], []
        def write(**kwargs):
            value = json.loads(kwargs['Body'])
            if value.get('recovery_parent') and value.get('state') == 'submitting' and len(self.provider.posts) == 1:
                intents.append(value['submission_attempt'])
                barrier.wait(timeout=5)
            with lock:
                return actual(**kwargs)
        def worker():
            try:
                results.append(self.run_recovery(ledger=self.ledger(store=store)))
            except Exception as error:
                results.append(error)
        with patch.object(client, 'put_object', side_effect=write):
            threads = [threading.Thread(target=worker) for _ in range(2)]
            for thread in threads:
                thread.start()
            for thread in threads:
                thread.join(timeout=10)
                self.assertFalse(thread.is_alive())
        self.assertEqual(len(set(intents)), 2)
        self.assertEqual(sum(isinstance(value, tuple) for value in results), 1)
        self.assertEqual(sum(isinstance(value, m.LedgerError) for value in results), 1)
        self.assertEqual(len(self.provider.posts), 3)
        self.assert_original_unchanged()

    def test_r2_unknown_write_cannot_read_back_a_foreign_submission_nonce(self):
        from test_mineru_task_ledger import FakeR2
        client = FakeR2()
        store = m.R2Store('daily', client=client, bucket='private')
        key = 'batches/' + 'a' * 32
        version = store.put(key, {'state': 'claiming'})
        actual = client.put_object
        def foreign_writer(**kwargs):
            value = json.loads(kwargs['Body'])
            value['submission_attempt'] = 'f' * 32
            raw = m.encoded(value)
            actual(**dict(kwargs, Body=raw, Metadata={'sha256': m.digest(raw)}))
            raise TimeoutError('unknown acknowledgement')
        with patch.object(client, 'put_object', side_effect=foreign_writer), self.assertRaises(m.LedgerError):
            store.put(key, {'state': 'submitting', 'submission_attempt': 'a' * 32}, version)

    def test_reserved_claiming_child_uses_original_key_after_configuration_reorder(self):
        actual = self.store.put
        def pause(key, value, previous=None):
            if value.get('recovery_parent') and value['state'] == 'submitting':
                raise OSError('pause before intent')
            return actual(key, value, previous)
        with patch.object(self.store, 'put', side_effect=pause), self.assertRaises(m.LedgerError):
            self.run_recovery()
        rows, _ = self.run_recovery(ledger=self.ledger(tokens=list(reversed(TOKENS))))
        self.assertEqual(len(rows), 3)
        self.assertEqual(self.provider.posts[1][2], TOKENS[0][1])

    def test_private_failure_hash_matches_durable_inspection_three_fields(self):
        from inspect_legacy_mineru import canonical, sha256
        value = dict(ERROR, full_zip_url='https://ignored.invalid', private='ignored')
        self.assertEqual(failure_hash(value), sha256(canonical({key: value.get(key)
                                                              for key in ('err_msg', 'error', 'err_code')})))


class DailyRetryTests(unittest.TestCase):
    setUp = RecoveryTests.setUp
    ledger = RecoveryTests.ledger
    sleep = RecoveryTests.sleep
    control = RecoveryTests.control
    assert_original_unchanged = RecoveryTests.assert_original_unchanged
    run_recovery = RecoveryTests.run_recovery

    def daily(self, authorization=AUTH, **kwargs):
        terminal = TerminalRecovery(self.ledger(), allowed_error_hashes=[failure_hash(ERROR)], daily_retry_limit=3)
        return terminal.run(self.inputs, authorization=authorization, timeout=20, interval=2,
                            queue_budget=4, partial=True, **kwargs)

    def test_three_retries_submit_only_still_failed_members(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['done', 'failed'], ['failed'], ['done']]
        rows, summary = self.daily()
        self.assertEqual([len(post[0]) for post in self.provider.posts], [3, 2, 1, 1])
        self.assertEqual([row['_recovery_lineage']['child_ordinal'] for _, row in rows], [0, 1, 3])
        self.assertEqual([row['retry_count'] for row in summary['source_outcomes']], [0, 1, 3])
        self.assertEqual({row['status'] for row in summary['source_outcomes']}, {'done'})
        self.assertTrue(summary['ready_for_generation'])
        self.assertFalse(summary['partial'])
        self.assert_original_unchanged()

    def test_old_two_children_new_manifest_adds_only_third_and_keeps_old_policy_and_proofs(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['failed', 'failed'], ['failed', 'failed'], ['done', 'done']]
        self.run_recovery()
        previous = self.control()
        auth = {'run_id': '9999', 'manifest_sha256': 'b' * 64}
        rows, summary = self.daily(auth)
        current = self.control()
        self.assertEqual((len(rows), summary['provider_posts'], len(self.provider.posts)), (3, 1, 4))
        self.assertEqual(current['policy'], previous['policy'])
        self.assertEqual(current['children'][:2], previous['children'])
        extension = current['daily_retry_extension']
        self.assertEqual(extension['previous_children_count'], 2)
        self.assertEqual(extension['previous_controller_sha256'], m.digest(m.encoded(previous)))
        self.assertEqual(extension['authorizations'], [auth])
        for child in current['children']:
            stored, _ = self.store.get(child['key'])
            self.assertEqual(stored['recovery_parent']['policy'], previous['policy']['name'])
        # Strict manual callers may read/resume already authorized third work.
        rows, summary = self.run_recovery(authorization=auth)
        self.assertEqual((len(rows), summary['provider_posts']), (3, 0))
        self.assert_original_unchanged()

    def test_exhausted_three_reservations_survive_later_daily_and_manual_runs(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['failed', 'failed'], ['failed', 'failed'], ['failed', 'failed']]
        for index in range(3):
            rows, summary = self.daily({'run_id': str(9000 + index), 'manifest_sha256': str(index) * 64})
            self.assertEqual(len(rows), 1)
            self.assertEqual([row['status'] for row in summary['source_outcomes']], ['done', 'retry_exhausted', 'retry_exhausted'])
            self.assertEqual([row['retry_count'] for row in summary['source_outcomes']], [0, 3, 3])
        rows, summary = self.run_recovery(authorization={'run_id': '9001', 'manifest_sha256': '1' * 64})
        self.assertEqual(rows, [])
        self.assertEqual(len(self.control()['children']), 3)
        self.assertEqual(len(self.provider.posts), 4)
        self.assert_original_unchanged()

    def test_pending_original_returns_verified_partial_without_reservation(self):
        self.provider.plans = [['done', 'running', 'failed']]
        for _ in range(2):
            rows, summary = self.daily()
            self.assertEqual(len(rows), 1)
            self.assertEqual([row['status'] for row in summary['source_outcomes']], ['done', 'pending', 'failed'])
            self.assertEqual(summary['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 1)
        self.assertFalse((self.folder / 'ledger/recoveries').exists())

    def test_pending_child_is_only_polled_and_preserves_prior_successes(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['done', 'running']]
        for _ in range(2):
            rows, summary = self.daily()
            self.assertEqual(len(rows), 2)
            self.assertEqual([row['status'] for row in summary['source_outcomes']], ['done', 'done', 'pending'])
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(self.control()['children']), 1)

    def test_unknown_post_current_and_later_attempts_keep_success_without_reposting(self):
        self.provider.on_submit = lambda batch_id: (_ for _ in ()).throw(TimeoutError('private-provider-text'))
        rows, summary = self.daily()
        self.assertEqual(len(rows), 1)
        self.assertEqual([row['status'] for row in summary['source_outcomes']], ['done', 'submission_unknown', 'submission_unknown'])
        self.assertEqual((summary['failed'], summary['pending']), (0, 2))
        self.provider.on_submit = None
        for _ in range(2):
            rows, summary = self.daily()
            self.assertEqual(len(rows), 1)
            self.assertEqual(summary['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(self.control()['children']), 1)
        self.assertNotIn('private-provider-text', json.dumps(summary))

    def test_accepted_child_upload_interruption_never_reposts(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['done', 'done']]
        self.provider.on_upload = lambda: (_ for _ in ()).throw(OSError('upload interrupted'))
        rows, summary = self.daily()
        self.assertEqual(len(rows), 1)
        self.assertEqual([row['status'] for row in summary['source_outcomes']], ['done', 'pending', 'pending'])
        self.provider.on_upload = None
        rows, summary = self.daily()
        self.assertEqual((len(rows), summary['provider_posts'], len(self.provider.posts)), (3, 0, 2))

    def test_daily_extension_authorizes_new_failure_without_rewriting_old_allowlist(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['done', 'failed'], ['failed'], ['done']]
        def changed(batch_id, items):
            if batch_id == '3':
                return [{'data_id': item['id'], 'state': 'failed', 'err_code': 'NEW_FAILURE',
                         'err_msg': 'new terminal failure'} for item in items]
        self.provider.on_poll = changed
        self.run_recovery()
        previous = self.control()
        self.daily({'run_id': '9001', 'manifest_sha256': 'b' * 64})
        self.assertEqual(self.control()['policy'], previous['policy'])
        self.assertEqual(self.control()['children'][:2], previous['children'])
        rows, summary = self.run_recovery(authorization={'run_id': '9001', 'manifest_sha256': 'b' * 64})
        self.assertEqual((len(rows), summary['provider_posts']), (3, 0))

    def test_tampered_extension_or_history_stops_before_provider_requests(self):
        self.daily()
        key = 'recoveries/' + self.root_key.split('/')[1]
        original, _ = self.store.get(key)
        for mutate in (lambda x: x['daily_retry_extension'].__setitem__('max_children', 4),
                       lambda x: x['daily_retry_extension'].__setitem__('previous_controller_sha256', 'a' * 64),
                       lambda x: x['daily_retry_extension'].__setitem__('authorizations', [])):
            changed = copy.deepcopy(original); mutate(changed)
            _, version = self.store.get(key); self.store.put(key, changed, version)
            before = len(self.provider.polls), len(self.provider.posts)
            with self.assertRaises(m.LedgerError): self.daily()
            self.assertEqual((len(self.provider.polls), len(self.provider.posts)), before)
        self.assert_original_unchanged()

    def test_new_manifest_does_not_authorize_changed_original_bytes(self):
        self.run_recovery()
        previous = self.control()
        self.inputs[0][0].write_bytes(b'%PDF-different')
        with self.assertRaises(m.LedgerError):
            self.daily({'run_id': '9001', 'manifest_sha256': 'b' * 64})
        self.assertEqual(self.control(), previous)
        self.assertEqual(len(self.provider.posts), 3)

    def test_extension_cas_conflict_cannot_submit_an_extra_child(self):
        self.provider.plans = [['done', 'failed', 'failed'], ['failed', 'failed'], ['failed', 'failed'], ['done', 'done']]
        self.run_recovery()
        previous = self.control()
        barrier = threading.Barrier(2)
        actual = self.store.put
        def write(key, value, prior=None):
            if (key.startswith('recoveries/') and value.get('daily_retry_extension')
                    and len(value['children']) == 2):
                barrier.wait(timeout=5)
            return actual(key, value, prior)
        results = []
        def worker():
            try: results.append(self.daily({'run_id': '9001', 'manifest_sha256': 'b' * 64}))
            except Exception as error: results.append(error)
        with patch.object(self.store, 'put', side_effect=write):
            threads = [threading.Thread(target=worker) for _ in range(2)]
            for thread in threads: thread.start()
            for thread in threads:
                thread.join(timeout=10)
                self.assertFalse(thread.is_alive())
        self.assertEqual(sum(isinstance(result, tuple) for result in results), 1)
        self.assertEqual(len(self.provider.posts), 4)
        self.assertEqual(self.control()['children'][:2], previous['children'])
        self.assertEqual(len(self.control()['children']), 3)

    def test_daily_retry_limit_is_explicit_and_bounded(self):
        for limit in (True, 2, 4, 3.0, '3'):
            with self.assertRaises(m.LedgerError):
                TerminalRecovery(self.ledger(), daily_retry_limit=limit)


if __name__ == '__main__':
    unittest.main()
