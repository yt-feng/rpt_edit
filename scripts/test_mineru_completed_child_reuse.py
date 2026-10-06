"""Read-only reuse of accepted recovery children, with real durable bindings."""
import copy
from contextlib import ExitStack
from pathlib import Path
from types import SimpleNamespace
import tempfile
import unittest
from unittest.mock import patch

import mineru_task_ledger as m
import mineru_result_cache as c
import mineru_completed_child_reuse as reuse
from mineru_terminal_recovery import TerminalRecovery, failure_hash
from test_mineru_result_cache import MemoryR2
from test_mineru_terminal_recovery import Provider, ERROR, AUTH


def recovered_fixture(folder, *, third=False):
    folder = Path(folder)
    inputs = folder / 'pdfs'; inputs.mkdir(exist_ok=True)
    sources = []
    for index in range(3):
        path = inputs / f'original-{index}.pdf'; path.write_bytes(b'%PDF-original-' + str(index).encode())
        sources.append((path.resolve(), path.name))
    r2 = MemoryR2(); store = m.R2Store('dropbox', client=r2, bucket='private-test')
    provider = Provider()
    ledger = m.Ledger(store, provider, 'dropbox', 'https://mineru.net', c.OPTIONS,
                      [('MINER_U', 'test-private-token')])
    items = [ledger.bind(*source) for source in sources]
    root_key = ledger._create(items, {item['id']: path for item, (path, _) in zip(items, sources)}, ledger.clock() + 60)
    if third:
        provider.plans = [['done', 'failed', 'failed'], ['done', 'failed'], ['failed'], ['done']]
    terminal = TerminalRecovery(ledger, allowed_error_hashes=[failure_hash(ERROR)])
    terminal.run(sources, authorization=AUTH, timeout=60)
    if third:
        terminal = TerminalRecovery(ledger, allowed_error_hashes=[failure_hash(ERROR)], daily_retry_limit=3)
        terminal.run(sources, authorization={'run_id': '9999', 'manifest_sha256': 'b' * 64}, timeout=60)
    # Simulate the ordinary producer observing the original task. Finish this
    # fixture setup before installing the read-only boundary assertions.
    results, summary = ledger.run(sources, timeout=60)
    root, _ = ledger._read_batch(root_key)
    key, control, _ = terminal._read_control(root)
    return SimpleNamespace(ledger=ledger, store=store, r2=r2, provider=provider, input=inputs,
                           sources=sources, items=items, root=root, key=key, control=control,
                           results=results, summary=summary)


def no_mutations(fixture):
    stack = ExitStack()
    for owner, names in ((fixture.store, ('put',)), (fixture.provider, ('submit', 'upload')),
                         (TerminalRecovery, ('run', '_reserve', '_extend_daily'))):
        for name in names:
            stack.enter_context(patch.object(owner, name, side_effect=AssertionError('read-only path mutated ' + name)))
    return stack


class CompletedChildReuseTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.f = recovered_fixture(self.temp.name)

    def invoke(self, sources=None):
        f = self.f
        results, summary = f.results, f.summary
        if sources is not None:
            results, summary = f.ledger.run(sources, timeout=60)
        before = copy.deepcopy(f.r2.objects)
        polls = len(f.provider.polls)
        with no_mutations(f):
            result = reuse.reuse_completed_children(f.ledger, sources or f.sources, results, summary)
        self.assertEqual(f.r2.objects, before)
        self.assertLessEqual(len(f.provider.polls) - polls, 4)
        return result

    def update_child(self, ordinal, **changes):
        key = self.f.control['children'][ordinal - 1]['key']
        child, version = self.f.store.get(key); child.update(changes)
        self.f.store.put(key, child, version)
        return child

    def test_original_failure_and_two_completed_children_become_effective_success_without_mutation(self):
        rows, summary = self.invoke()
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual((summary['completed'], summary['failed'], summary['pending']), (3, 0, 0))
        self.assertEqual(summary['original_batches'], self.f.summary['original_batches'])
        self.assertEqual(summary['original_outcomes'], {'completed': 1, 'failed': 2, 'pending': 0})
        self.assertEqual(summary['completed_child_reuse'], {'schema': 1, 'provider_posts': 0,
                                                          'provider_gets': 3, 'reused_sources': 2})
        self.assertEqual([row['_recovery_lineage']['child_ordinal'] for _, row in rows], [0, 1, 2])
        for path, row in rows:
            binding = self.f.ledger.bind(path, path.name)
            self.assertEqual(reuse.result_lineage(self.f.ledger, binding, self.f.root, row), row['_recovery_lineage'])

    def test_third_child_extension_preserves_old_policy_and_new_manifest_authorization(self):
        with tempfile.TemporaryDirectory() as other:
            self.f = recovered_fixture(other, third=True)
            rows, summary = self.invoke()
            self.assertTrue(summary['ready_for_generation'])
            self.assertEqual([row['_recovery_lineage']['child_ordinal'] for _, row in rows], [0, 1, 3])
            self.assertEqual(self.f.control['policy']['max_children'], 2)
            self.assertEqual(summary['completed_child_reuse']['provider_gets'], 4)

    def test_pending_child_is_get_once_and_not_resubmitted(self):
        self.update_child(1, state='uploaded')
        self.f.provider.plans[1] = ['done', 'running']
        rows, summary = self.invoke()
        self.assertEqual(rows, [])
        self.assertFalse(summary['ready_for_generation'])
        self.assertEqual(summary['pending'], 1)
        self.assertEqual(summary['completed_child_reuse']['provider_gets'], 2)

    def test_unknown_submission_is_not_polled_or_resubmitted(self):
        self.update_child(1, state='submitting', batch_id=None)
        rows, summary = self.invoke()
        self.assertEqual(rows, [])
        self.assertFalse(summary['ready_for_generation'])
        self.assertEqual(summary['completed_child_reuse']['provider_gets'], 1)

    def test_missing_reserved_child_is_not_created(self):
        entry = self.f.control['children'][0]
        del self.f.r2.objects[self.f.store.prefix + entry['key'] + '.json']
        rows, summary = self.invoke()
        self.assertEqual(rows, []); self.assertFalse(summary['ready_for_generation'])

    def test_wrong_parent_lineage_is_rejected(self):
        child = self.update_child(1)
        parent = dict(child['recovery_parent'], root_key='batches/' + 'f' * 32)
        self.update_child(1, recovery_parent=parent)
        with self.assertRaisesRegex(m.LedgerError, 'parent reservation'):
            self.invoke()

    def test_changed_failure_proof_is_rejected_before_reading_child(self):
        original = self.f.provider.poll
        def poll(*args):
            rows = original(*args)
            if args[0] == self.f.root['batch_id']:
                rows[1]['err_msg'] = 'different failure'
            return rows
        with patch.object(self.f.provider, 'poll', side_effect=poll), self.assertRaisesRegex(m.LedgerError, 'proof mismatch|not explicitly authorized'):
            self.invoke()

    def test_changed_child_options_or_credential_are_rejected(self):
        for changes in ({'options': dict(c.OPTIONS, language='ch')}, {'token_identity': 'f' * 64}):
            with self.subTest(changes=changes), tempfile.TemporaryDirectory() as folder:
                self.f = recovered_fixture(folder)
                self.update_child(1, **changes)
                with self.assertRaisesRegex(m.LedgerError, 'options or token'):
                    self.invoke()

    def test_source_changed_after_original_poll_cannot_reuse_old_child(self):
        self.f.sources[1][0].write_bytes(b'%PDF-changed')
        with self.assertRaisesRegex(m.LedgerError, 'source claim'):
            self.invoke()

    def test_selected_original_success_cannot_bypass_pending_unselected_member(self):
        self.update_child(1, state='uploaded'); self.f.provider.plans[1] = ['done', 'running']
        rows, summary = self.invoke([self.f.sources[0]])
        self.assertEqual(rows, [])
        self.assertEqual(summary['completed'], 1)
        self.assertFalse(summary['ready_for_generation'])
        self.assertEqual(summary['effective_batches'][0]['pending'], 1)

    def test_no_controller_keeps_original_failure_without_extra_provider_get(self):
        del self.f.r2.objects[self.f.store.prefix + self.f.key + '.json']
        count = len(self.f.provider.polls)
        rows, summary = self.invoke()
        self.assertEqual(rows, self.f.results); self.assertEqual(summary, self.f.summary)
        self.assertEqual(len(self.f.provider.polls), count)

    def test_cache_lineage_cannot_relabel_child_as_another_accepted_task(self):
        rows, _ = self.invoke()
        row = rows[-1][1]; row['_recovery_lineage']['batch_id'] = 'wrong-task'
        with self.assertRaisesRegex(m.LedgerError, 'lineage mismatch'):
            reuse.result_lineage(self.f.ledger, self.f.items[-1], self.f.root, row)

    def test_provider_json_cannot_select_its_own_recovery_cache_context(self):
        path = self.f.sources[0][0]
        row = {'data_id': self.f.items[0]['id'], 'state': 'done', '_recovery_lineage': {'forged': True}}
        results, _ = reuse.reuse_completed_children(self.f.ledger, self.f.sources, [(path, row)],
                                                   {'ready_for_generation': True})
        self.assertNotIn('_recovery_lineage', results[0][1])
        self.assertIn('_recovery_lineage', row)

    def test_snapshot_change_during_get_rejects_previously_valid_child(self):
        original = self.f.provider.poll
        key = self.f.key
        real_get = self.f.store.get
        changed = False
        def poll(*args):
            nonlocal changed
            rows = original(*args)
            if args[0] == '3':
                changed = True
            return rows
        def get(requested):
            value, version = real_get(requested)
            if changed and requested == key:
                value = dict(value, unexpected='concurrent change')
            return value, version
        with patch.object(self.f.provider, 'poll', side_effect=poll), \
             patch.object(self.f.store, 'get', side_effect=get), \
             self.assertRaisesRegex(m.LedgerError, 'snapshot changed'):
            self.invoke()

    def test_unknown_get_does_not_become_permission_to_submit_or_release(self):
        with no_mutations(self.f), patch.object(self.f.provider, 'poll', side_effect=m.LedgerError('GET outcome unknown')), \
             self.assertRaisesRegex(m.LedgerError, 'GET outcome unknown'):
            reuse.read_completed_batch(self.f.ledger, self.f.root)


if __name__ == '__main__':
    unittest.main()
