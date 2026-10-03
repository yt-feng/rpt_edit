import copy
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import uuid

import inspect_durable_mineru as m
from mineru_task_ledger import FileStore, Ledger, LedgerError, encoded, token_fingerprint


class InspectionTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.store = FileStore(self.root / 'ledger')
        self.credentials = {'MINER_U': 'first', 'MINER_U_2': 'second'}
        self.ledger = Ledger(self.store, None, 'dropbox', 'https://mineru.net',
                             {'model': 'vlm', 'language': 'en', 'ocr': True}, list(self.credentials.items()))
        path = self.root / 'source.pdf'; path.write_bytes(b'%PDF-exact')
        self.item = self.ledger.bind(path, 'source.pdf')
        self.key = 'batches/' + 'a' * 32
        self.batch = {'schema': 1, 'key': self.key, 'scope': 'dropbox', 'endpoint': 'https://mineru.net',
                      'options': self.ledger.options, 'token_identity': token_fingerprint('second'),
                      'state': 'terminal', 'batch_id': str(uuid.uuid4()), 'files': [self.item]}
        self.store.put(self.key, self.batch)
        self.request = {'scope': 'dropbox', 'run_id': '123', 'batches': [{'key': self.key, 'job_id': '456'}]}
        self.calls = []

    def getter(self, endpoint, token, timeout):
        self.calls.append((endpoint, token, timeout))
        return 200, encoded({'code': 0, 'data': {'batch_id': self.batch['batch_id'], 'extract_result': [
            {'data_id': self.item['id'], 'state': 'failed', 'err_msg': 'PDF page limit exceeded SECRET-REPORT'}]}})

    def test_exact_original_token_one_get_no_ledger_write_no_error_text(self):
        before = {str(p): p.read_bytes() for p in self.root.rglob('*.json')}
        with patch.object(self.store, 'put', side_effect=AssertionError('must not write')):
            public, private, diag = m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(len(self.calls), 1); self.assertEqual(self.calls[0][1], 'second')
        self.assertEqual(public['provider_posts'], 0); self.assertTrue(public['batches'][0]['membership_proven'])
        self.assertEqual(diag['failure_categories'], {'page_limit': 1})
        self.assertNotIn('SECRET-REPORT', json.dumps(public | diag))
        self.assertIn('SECRET-REPORT', json.dumps(private))
        self.assertEqual(before, {str(p): p.read_bytes() for p in self.root.rglob('*.json')})

    def test_corrupt_source_binding_fails_before_get(self):
        self.batch['files'][0]['sha256'] = '0' * 64
        (self.root / 'ledger' / (self.key + '.json')).write_bytes(encoded(self.batch))
        with self.assertRaises(LedgerError):
            m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_missing_later_task_validated_before_first_get(self):
        self.request['batches'].append({'key': 'batches/' + 'b' * 32, 'job_id': '457'})
        with self.assertRaises(ValueError):
            m.inspect(self.request, self.store, self.credentials, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_input_cannot_select_arbitrary_objects_or_duplicate_tasks(self):
        for bad in ['../secret', 'sources/' + 'a' * 64, self.key + '/x']:
            request = copy.deepcopy(self.request); request['batches'][0]['key'] = bad
            with self.assertRaises(ValueError): m.validate_request(request)
        self.request['batches'] *= 2
        with self.assertRaises(ValueError): m.validate_request(self.request)

    def test_rotated_away_original_token_stops_before_get(self):
        with self.assertRaises(LedgerError):
            m.inspect(self.request, self.store, {'MINER_U': 'new-token'}, getter=self.getter)
        self.assertEqual(self.calls, [])

    def test_error_classification_is_fixed_vocabulary(self):
        for raw, category in [('password protected PDF', 'encrypted_pdf'), ('Insufficient quota', 'quota'),
                               ('download failed', 'file_download'), ('arbitrary-private-url', 'other_provider_failure')]:
            self.assertEqual(m.error_category({'err_msg': raw}), category)


if __name__ == '__main__': unittest.main()
