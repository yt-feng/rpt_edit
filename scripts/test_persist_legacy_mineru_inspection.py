import copy
import json
import sys
import types
import unittest
from unittest.mock import patch

import inspect_legacy_mineru as inspector
import persist_legacy_mineru_inspection as target
from test_inspect_legacy_mineru import BATCH2, TOKEN, batch, request, response

PRODUCER = {'run_id': '12345', 'attempt': '1', 'sha': 'a' * 40}


class MemoryStore:
    def __init__(self, corrupt=False, fail=False):
        self.objects = {}; self.calls = []; self.corrupt = corrupt; self.fail = fail

    def key(self, *parts):
        return '/'.join((target.PREFIX, *parts))

    def _put(self, key, body, **kwargs):
        self.calls.append(('put', key))
        if self.fail: raise OSError('private-error-sentinel')
        self.objects[key] = body

    def _get(self, key, maximum):
        self.calls.append(('get', key))
        body = self.objects[key]
        return body + b'!' if self.corrupt else body


def receipts(rows=None, credentials=None):
    return inspector.inspect_batches(request(rows), credentials or {'MINER_U': TOKEN},
                                     getter=lambda *_: (200, response()))


class ReceiptTests(unittest.TestCase):
    def test_exact_raw_membership_is_private_and_separate_from_admission(self):
        public, private = receipts(); store = MemoryStore()
        result = target.persist(store, public, private, PRODUCER)
        self.assertEqual(result['private_metadata_objects'], 1)
        self.assertFalse(result['canonical_task_admission']); self.assertFalse(result['source_bytes_proven'])
        self.assertEqual(len(store.objects), 2)
        for key in store.objects:
            self.assertTrue(key.startswith(target.PREFIX + '/12345-1/'))
            self.assertNotIn('_extended-locales/', key)
        receipt = next(json.loads(raw) for key, raw in store.objects.items() if '/receipt-' in key)
        self.assertEqual(receipt['input'], request()); self.assertEqual(receipt['producer'], PRODUCER)
        self.assertFalse(receipt['historical_token_fingerprint_proven'])
        self.assertNotIn('provider.invalid', json.dumps(result)); self.assertNotIn(TOKEN, json.dumps(result))

    def test_all_local_evidence_is_validated_before_any_write(self):
        public, private = receipts()
        mutations = [
            lambda p, q: p.update(network_stop=True),
            lambda p, q: p.update(provider_posts=1),
            lambda p, q: p.update(paid_requests=False),
            lambda p, q: p.update(provider_gets=2),
            lambda p, q: p.update(uninspected_count=1),
            lambda p, q: q.update(input_canonical_sha256='0' * 64),
            lambda p, q: p['batches'].append(copy.deepcopy(p['batches'][0])),
            lambda p, q: q['batches'].clear(),
            lambda p, q: q['batches'].append(copy.deepcopy(q['batches'][0])),
            lambda p, q: q['batches'][0].update(raw_response_base64='e30='),
            lambda p, q: p['batches'][0].update(all_succeeded=False),
            lambda p, q: q['batches'][0].update(provider_response={}),
            lambda p, q: q['batches'][0]['input'].update(batch_id=BATCH2),
        ]
        for mutate in mutations:
            p, q = copy.deepcopy(public), copy.deepcopy(private); mutate(p, q); store = MemoryStore()
            with self.subTest(mutate=mutate), self.assertRaises(ValueError): target.persist(store, p, q, PRODUCER)
            self.assertEqual(store.calls, [])

    def test_oversize_is_rejected_before_base64_decode(self):
        public, private = receipts()
        private['batches'][0]['raw_response_base64'] = 'A' * (4 * ((inspector.MAX_BODY + 2) // 3) + 1)
        store = MemoryStore()
        with patch.object(target.base64, 'b64decode') as decode, self.assertRaises(ValueError):
            target.persist(store, public, private, PRODUCER)
        decode.assert_not_called(); self.assertEqual(store.calls, [])

    def test_absent_credentials_cannot_forge_a_completed_claim(self):
        public, private = receipts(credentials={'MINER_U': None}); store = MemoryStore()
        target.persist(store, public, private, PRODUCER)
        self.assertEqual(len(store.objects), 1)
        public['batches'][0]['all_succeeded'] = True; store = MemoryStore()
        with self.assertRaises(ValueError): target.persist(store, public, private, PRODUCER)
        self.assertEqual(store.calls, [])

    def test_network_or_readback_failure_stops_before_receipt_or_next_object(self):
        public, private = receipts()
        for store, exception, count in [(MemoryStore(fail=True), OSError, 1), (MemoryStore(corrupt=True), ValueError, 2)]:
            with self.subTest(exception=exception), self.assertRaises(exception):
                target.persist(store, public, private, PRODUCER)
            self.assertEqual(len(store.calls), count)
            self.assertFalse(any('/receipt-' in key for _, key in store.calls))

    def test_single_attempt_private_client_does_not_inherit_publishing_retries(self):
        calls = []
        fake_boto = types.SimpleNamespace(client=lambda *a, **kw: calls.append((a, kw)) or object())
        fake_config = types.SimpleNamespace(Config=lambda **kw: kw)
        fake_r2 = types.SimpleNamespace(R2Store=lambda client, bucket, prefix: (client, bucket, prefix),
                                       require_env=lambda name: {'R2_ACCOUNT_ID': 'fake', 'R2_BUCKET': 'private'}.get(name, 'hidden'))
        with patch.dict(sys.modules, {'boto3': fake_boto, 'botocore.config': fake_config, 'portal_extended_r2': fake_r2}):
            _, bucket, prefix = target.single_attempt_store()
        self.assertEqual((bucket, prefix), ('private', target.PREFIX)); self.assertEqual(len(calls), 1)
        self.assertEqual(calls[0][1]['config']['retries'], {'total_max_attempts': 1, 'mode': 'standard'})


if __name__ == '__main__': unittest.main()
