"""Exercise next-key timeout recovery with real durable source/task bindings."""
import copy
import json
from pathlib import Path
import unittest

import mineru_task_ledger as m
import test_mineru_task_ledger as fixture
from mineru_terminal_recovery import TerminalRecovery

TOKENS = [('MINER_U' + ('' if i == 1 else '_' + str(i)), 'test-private-key-' + str(i))
          for i in range(1, 5)]


class Provider(fixture.FakeProvider):
    def __init__(self):
        super().__init__()
        self.plans = {token: 'pending' for _, token in TOKENS}
        self.after_submit = None

    def submit(self, *args):
        result = super().submit(*args)
        if self.after_submit:
            self.after_submit()
        return result

    def poll(self, batch_id, token, timeout):
        self.polls.append((batch_id, token, timeout))
        plan = self.plans[token]
        if callable(plan):
            return plan(self.tasks[batch_id])
        return [{'data_id': item['id'], 'state': plan,
            **({'full_zip_url': 'https://results.invalid/' + batch_id + '/' + item['id']}
               if plan == 'done' else {})} for item in self.tasks[batch_id]]


class FailoverTests(unittest.TestCase):
    setUp = fixture.LedgerTests.setUp

    def ledger(self, *, enabled=True, forbid=False, **kwargs):
        return m.Ledger(self.store, self.provider, 'daily', 'https://mineru.net', fixture.OPTIONS, TOKENS,
            clock=self.clock.time, sleep=self.clock.sleep, wallclock=self.clock.time,
            key_failover=enabled, forbid_new_submissions=forbid, **kwargs)

    def start(self):
        self.provider = Provider()
        ledger = self.ledger()
        items = [ledger.bind(*pair) for pair in self.inputs]
        key = ledger._create(items, {row['id']: path for row, (path, _) in zip(items, self.inputs)}, 100)
        self.root_key = key
        self.claims = {p.name: p.read_bytes() for p in (self.store.root / 'sources').glob('*.json')}
        self.original = (self.store.root / (key + '.json')).read_bytes()

    def run_batch(self, **kwargs):
        return self.ledger(**kwargs).run(self.inputs, timeout=30, interval=1, queue_budget=4)

    def assert_original(self):
        self.assertEqual(self.original, (self.store.root / (self.root_key + '.json')).read_bytes())
        self.assertEqual(self.claims, {p.name: p.read_bytes() for p in (self.store.root / 'sources').glob('*.json')})

    def control(self):
        return json.loads(next((self.store.root / 'keyfailovers').glob('*.json')).read_bytes())

    def test_first_timeout_uses_second_key_and_resume_does_not_submit_again(self):
        self.start()
        self.provider.plans[TOKENS[1][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual([p[2] for p in self.provider.posts], [TOKENS[0][1], TOKENS[1][1]])
        self.assertEqual({row['_recovery_lineage']['child_ordinal'] for _, row in rows}, {1})
        chosen = copy.deepcopy(self.control()['winners'])
        self.provider.plans[TOKENS[0][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertEqual((summary['provider_posts'], len(self.provider.posts)), (0, 2))
        self.assertEqual(self.control()['winners'], chosen)
        self.assertEqual({row['_recovery_lineage']['child_ordinal'] for _, row in rows}, {1})
        self.assert_original()

    def test_fourth_key_can_finish_after_first_three_stall(self):
        self.start()
        self.provider.plans[TOKENS[3][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertEqual(len(rows), 5)
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual([p[2] for p in self.provider.posts], [token for _, token in TOKENS])
        self.assertEqual({row['_recovery_lineage']['child_ordinal'] for _, row in rows}, {3})
        self.assert_original()

    def test_completed_siblings_are_never_in_alternate_submission(self):
        self.start()
        first = self.provider.tasks['1'][0]['id']
        self.provider.plans[TOKENS[0][1]] = lambda items: [
            {'data_id': item['id'], 'state': 'done' if item['id'] == first else 'pending',
             **({'full_zip_url': 'https://results.invalid/original'} if item['id'] == first else {})}
            for item in items]
        self.provider.plans[TOKENS[1][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(len(self.provider.posts[1][0]), 4)
        self.assertNotIn(first, [item['id'] for item in self.provider.posts[1][0]])
        self.assertEqual(sorted(row['_recovery_lineage']['child_ordinal'] for _, row in rows), [0, 1, 1, 1, 1])
        self.assert_original()

    def test_all_keys_stalled_has_a_lifetime_bound_and_no_false_success(self):
        self.start()
        for _ in range(2):
            rows, summary = self.run_batch()
            self.assertEqual(rows, [])
            self.assertFalse(summary['ready_for_generation'])
        self.assertEqual(len(self.provider.posts), 4)
        self.assertEqual(len(self.control()['attempts']), 3)
        self.assert_original()

    def test_unknown_alternate_post_never_tries_a_third_key(self):
        self.start()
        self.provider.after_submit = lambda: (_ for _ in ()).throw(m.ProviderTransportError('post'))
        with self.assertRaises(m.ProviderTransportError):
            self.run_batch()
        self.assertEqual(len(self.provider.posts), 2)
        self.provider.after_submit = None
        for _ in range(2):
            rows, summary = self.run_batch()
            self.assertFalse(summary['ready_for_generation'])
            self.assertEqual(rows, [])
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(self.control()['attempts']), 1)
        self.assert_original()

    def test_changed_bytes_and_corrupt_controller_stop_before_provider_calls(self):
        self.start()
        self.provider.plans[TOKENS[1][1]] = 'done'
        self.run_batch()
        before = len(self.provider.polls), len(self.provider.posts)
        control_path = next((self.store.root / 'keyfailovers').glob('*.json'))
        valid = control_path.read_bytes()
        value = json.loads(valid); value['attempts'][0]['token_identity'] = 'a' * 64
        control_path.write_bytes(m.encoded(value))
        with self.assertRaises(m.LedgerError): self.run_batch()
        self.assertEqual(before, (len(self.provider.polls), len(self.provider.posts)))
        control_path.write_bytes(valid)
        self.inputs[0][0].write_bytes(b'%PDF-changed')
        with self.assertRaises(m.LedgerError):
            TerminalRecovery(self.ledger(), automatic=True).run(self.inputs,
                authorization={'run_id': '123', 'manifest_sha256': 'a' * 64},
                timeout=30, interval=1, queue_budget=4)
        self.assertEqual(before, (len(self.provider.polls), len(self.provider.posts)))

    def test_incomplete_membership_cannot_authorize_another_key(self):
        self.start()
        self.provider.plans[TOKENS[0][1]] = lambda items: [
            {'data_id': item['id'], 'state': 'pending'} for item in items[:-1]]
        with self.assertRaises(m.LedgerError): self.run_batch()
        self.assertEqual(len(self.provider.posts), 1)
        self.assertFalse((self.store.root / 'keyfailovers').exists())

    def test_no_new_submission_replay_reuses_winner_without_any_ledger_write(self):
        self.start()
        self.provider.plans[TOKENS[1][1]] = 'done'
        self.run_batch()
        before = {p.relative_to(self.store.root): p.read_bytes() for p in self.store.root.rglob('*.json')}
        rows, summary = self.run_batch(enabled=False, forbid=True)
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(len(rows), 5)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(before, {p.relative_to(self.store.root): p.read_bytes() for p in self.store.root.rglob('*.json')})

    def test_terminal_recovery_uses_same_alternate_and_exact_result_lineage(self):
        self.start()
        self.provider.plans[TOKENS[1][1]] = 'done'
        ledger = self.ledger()
        rows, summary = TerminalRecovery(ledger, automatic=True).run(self.inputs,
            authorization={'run_id': '123', 'manifest_sha256': 'a' * 64},
            timeout=30, interval=1, queue_budget=4, partial=True)
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(len(rows), 5)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual({row['_recovery_lineage']['parent_batch_key'] for _, row in rows}, {self.root_key})
        self.assert_original()

    def test_lost_reservation_ack_resumes_the_same_child(self):
        self.start()
        self.provider.plans[TOKENS[1][1]] = 'done'
        put = self.store.put
        interrupted = False
        def write(key, value, previous=None):
            nonlocal interrupted
            version = put(key, value, previous)
            if key.startswith('keyfailovers/') and value['attempts'] and not interrupted:
                interrupted = True
                raise m.LedgerError('Private checkpoint write outcome unresolved; no new submission')
            return version
        self.store.put = write
        with self.assertRaises(m.LedgerError): self.run_batch()
        self.assertEqual(len(self.provider.posts), 1)
        reserved = self.control()['attempts'][0]['key']
        rows, summary = self.run_batch()
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(self.control()['attempts'][0]['key'], reserved)
        self.assertEqual(len(self.control()['attempts']), 1)

    def test_expired_second_key_immediately_moves_to_third(self):
        self.start()
        submit = self.provider.submit
        def create(items, options, token, timeout):
            if token == TOKENS[1][1]:
                raise m.DefinitiveAuthRejection('A0211', 401)
            return submit(items, options, token, timeout)
        self.provider.submit = create
        self.provider.plans[TOKENS[2][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual([p[2] for p in self.provider.posts], [TOKENS[0][1], TOKENS[2][1]])
        self.assertEqual(len(self.control()['attempts']), 2)
        self.assertEqual({row['_recovery_lineage']['child_ordinal'] for _, row in rows}, {2})

    def test_page_limit_failure_is_not_reposted_to_another_key(self):
        self.start()
        first = self.provider.tasks['1'][0]['id']
        self.provider.plans[TOKENS[0][1]] = lambda items: [
            {'data_id': item['id'], 'state': 'failed' if item['id'] == first else 'pending',
             **({'err_code': -60006} if item['id'] == first else {})} for item in items]
        self.provider.plans[TOKENS[1][1]] = 'done'
        rows, summary = self.run_batch()
        self.assertFalse(summary['ready_for_generation'])
        self.assertEqual(rows, [])
        self.assertEqual(len(self.provider.posts), 2)
        self.assertNotIn(first, [row['id'] for row in self.provider.posts[1][0]])


if __name__ == '__main__':
    unittest.main()
