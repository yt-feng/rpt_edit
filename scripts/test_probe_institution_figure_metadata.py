import copy
import unittest
from unittest.mock import Mock, patch

import probe_institution_figure_metadata as p
from mineru_task_ledger import digest, encoded


class ProbeTests(unittest.TestCase):
    def test_pinned_inventory_is_complete_and_binds_exact_originals(self):
        value = p.selection()
        self.assertEqual(value['source_job_id'], '116174580136')
        bindings = [p.binding_for(row) for row in value['sources']]
        self.assertEqual(len({row['id'] for row in bindings}), 4)
        for row, binding in zip(value['sources'], bindings):
            self.assertEqual(binding['sha256'], row['sha256'])
            self.assertEqual(binding['size'], row['bytes'])

    def test_only_exact_claim_and_completed_cached_result_are_read(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger, cache = Mock(), Mock()
        ledger.store.get.return_value = ({'binding': binding, 'batch_key': 'batches/test'}, None)
        ledger._read_batch.return_value = ({'files': [binding]}, None)
        lineage = {'exact': True}
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: {'_recovery_lineage': lineage}}, {'all_succeeded': True})):
            self.assertEqual(p.cached_payload(ledger, cache, binding), cache.get.return_value)
        cache.get.assert_called_once_with(binding, lineage)
        ledger.store.put.assert_not_called()
        cache.put.assert_not_called()
        ledger.provider.submit.assert_not_called()
        changed = copy.deepcopy(binding); changed['sha256'] = 'f' * 64
        ledger.store.get.return_value = ({'binding': changed, 'batch_key': 'batches/test'}, None)
        cache.reset_mock()
        with self.assertRaisesRegex(p.ProbeError, 'source_claim_missing'):
            p.cached_payload(ledger, cache, binding)
        cache.get.assert_not_called()

    def test_missing_cache_never_downloads_or_submits(self):
        binding = p.binding_for(p.selection()['sources'][0])
        ledger, cache = Mock(), Mock()
        ledger.store.get.return_value = ({'binding': binding, 'batch_key': 'batches/test'}, None)
        ledger._read_batch.return_value = ({'files': [binding]}, None)
        cache.get.return_value = None
        with patch.object(p, 'read_completed_batch', return_value=(
                {binding['id']: {'_recovery_lineage': {}}}, {'all_succeeded': True})):
            with self.assertRaisesRegex(p.ProbeError, 'source_result_cache_missing'):
                p.cached_payload(ledger, cache, binding)
        ledger.provider.submit.assert_not_called()
        cache.put.assert_not_called()

    def test_write_capable_ledger_rejected_before_any_read(self):
        ledger = Mock(scope='institution', forbid_new_submissions=False)
        with self.assertRaisesRegex(p.ProbeError, 'read_only_scope'):
            p.probe(ledger, Mock(), 'private')
        ledger.store.get.assert_not_called()

    def test_invalid_binding_is_rejected(self):
        row = dict(p.selection()['sources'][0], local_filename='../outside.pdf')
        with self.assertRaises(ValueError): p.binding_for(row)


if __name__ == '__main__': unittest.main()
