"""Offline complete ZIP, immutable write and source/task binding regressions."""
from __future__ import annotations

import copy
import io
import json
from pathlib import Path
import tempfile
import threading
import types
import unittest
from unittest.mock import patch
import zipfile

from consume_legacy_mineru import ConsumerError
import mineru_result_cache as c
import mineru_task_ledger as m


class S3Error(Exception):
    def __init__(self, code, status):
        super().__init__(code)
        self.response = {'Error': {'Code': code}, 'ResponseMetadata': {'HTTPStatusCode': status}}


class MemoryR2:
    """Exercise the same conditional PutObject/readback boundary as R2."""
    def __init__(self):
        self.objects, self.puts, self.gets = {}, [], []
        self.before_put = self.after_put = self.before_get = None
        self.lock = threading.Lock()

    def get_object(self, **kwargs):
        key = kwargs['Key']
        with self.lock:
            self.gets.append(key)
        if self.before_get:
            self.before_get(key)
        with self.lock:
            if key not in self.objects:
                raise S3Error('NoSuchKey', 404)
            value = copy.deepcopy(self.objects[key])
        body = value.pop('Body')
        return dict(value, Body=io.BytesIO(body), ContentLength=len(body), ETag=m.digest(body))

    def put_object(self, **kwargs):
        key = kwargs['Key']
        with self.lock:
            self.puts.append(copy.deepcopy(kwargs))
        if self.before_put:
            self.before_put(key, kwargs)
        with self.lock:
            if kwargs.get('IfNoneMatch') == '*':
                if key in self.objects:
                    raise S3Error('PreconditionFailed', 412)
            elif kwargs.get('IfMatch'):
                if key not in self.objects or kwargs['IfMatch'] != m.digest(self.objects[key]['Body']):
                    raise S3Error('PreconditionFailed', 412)
            else:
                raise AssertionError('Every write must be conditional')
            self.objects[key] = {field: copy.deepcopy(kwargs[field]) for field in ('Body', 'ContentType', 'Metadata')}
        if self.after_put:
            self.after_put(key, kwargs)
        return {}


def result_zip(text='Original revenue 125.50.'):
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        archive.writestr('payload/full.md', '# Original report\n' + text + '\n')
        archive.writestr('payload/images/chart.bin', b'original asset bytes')
    return buffer.getvalue()


class ResultCacheTests(unittest.TestCase):
    def setUp(self):
        self.r2 = MemoryR2(); self.cache = c.ResultCache(self.r2, 'private-test')
        base = {'source': '261003/original.pdf', 'sha256': m.digest(b'%PDF-original'), 'size': 13,
                'scope': 'dropbox', 'endpoint': 'https://mineru.net', 'options': c.OPTIONS}
        self.binding = dict(base, id=m.digest(m.encoded(base)))
        self.lineage = {'batch_id': 'original-task-1', 'batch_key': 'batches/' + 'a' * 32,
                        'parent_batch_key': 'batches/' + 'a' * 32, 'data_id': self.binding['id'], 'child_ordinal': 0}
        self.payload = result_zip()

    def keys(self):
        identity = c.identity(self.binding, self.lineage)
        return self.cache.receipt_key(identity), self.cache.blob_key(identity, m.digest(self.payload))

    def tamper_receipt(self, change):
        receipt_key, _ = self.keys()
        item = self.r2.objects[receipt_key]
        value = json.loads(item['Body']); change(value)
        item['Body'] = m.encoded(value); item['Metadata']['sha256'] = m.digest(item['Body'])

    def test_missing_receipt_is_only_download_admission(self):
        self.assertIsNone(self.cache.get(self.binding, self.lineage))
        self.assertEqual(self.r2.puts, [])

    def test_dedicated_sdk_cache_client_disables_retries_without_mutating_shared_client(self):
        original_config = types.SimpleNamespace(retries={'max_attempts': 4})
        client = types.SimpleNamespace(meta=types.SimpleNamespace(config=original_config))
        calls = []
        def create(*args, **kwargs):
            calls.append((args, kwargs)); return self.r2
        sdk = types.ModuleType('boto3'); sdk.client = create
        botocore = types.ModuleType('botocore'); config = types.ModuleType('botocore.config')
        config.Config = lambda **kwargs: kwargs
        with patch.dict('sys.modules', {'boto3': sdk, 'botocore': botocore, 'botocore.config': config}), \
             patch.dict('os.environ', {'R2_ACCOUNT_ID': 'test-account', 'R2_ACCESS_KEY_ID': 'test-access',
                                      'R2_SECRET_ACCESS_KEY': 'test-private'}, clear=True):
            cached = c.ResultCache.single_attempt(client, 'private-test')
        self.assertIs(cached.client, self.r2)
        self.assertEqual(calls[0][1]['config']['retries'], {'total_max_attempts': 1, 'mode': 'standard'})
        self.assertEqual(original_config.retries, {'max_attempts': 4})
        self.assertEqual(calls[0][1]['endpoint_url'], 'https://test-account.r2.cloudflarestorage.com')

    def test_already_single_attempt_sdk_client_is_reused(self):
        client = types.SimpleNamespace(meta=types.SimpleNamespace(config=types.SimpleNamespace(
            retries={'total_max_attempts': 1, 'mode': 'standard'})))
        self.assertIs(c.ResultCache.single_attempt(client, 'private-test').client, client)

    def test_full_zip_roundtrip_has_no_provider_url_or_credentials_and_is_immutable(self):
        self.assertEqual(self.cache.put(self.binding, self.lineage, self.payload), self.payload)
        self.assertEqual(self.cache.get(self.binding, self.lineage), self.payload)
        self.assertEqual(len(self.r2.objects), 2)
        self.assertTrue(all(value['IfNoneMatch'] == '*' for value in self.r2.puts))
        receipt_key, _ = self.keys()
        receipt = json.loads(self.r2.objects[receipt_key]['Body'])
        self.assertEqual(receipt['source_binding'], self.binding)
        self.assertEqual(receipt['lineage'], self.lineage)
        self.assertNotIn('url', receipt)
        before = copy.deepcopy(self.r2.objects); writes = len(self.r2.puts)
        self.cache.put(self.binding, self.lineage, self.payload)
        self.assertEqual(self.r2.objects, before); self.assertEqual(len(self.r2.puts), writes)

    def test_different_valid_zip_does_not_replace_existing_result(self):
        self.cache.put(self.binding, self.lineage, self.payload); before = copy.deepcopy(self.r2.objects)
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_result_differs'):
            self.cache.put(self.binding, self.lineage, result_zip('Changed numbers 999.00.'))
        self.assertEqual(before, self.r2.objects)

    def test_corrupt_zip_is_rejected_before_any_write(self):
        with self.assertRaises(ConsumerError): self.cache.put(self.binding, self.lineage, b'not a ZIP')
        self.assertEqual(self.r2.puts, [])

    def test_unsafe_zip_path_is_rejected_before_any_write(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as archive:
            archive.writestr('../full.md', 'private')
        with self.assertRaises(ConsumerError): self.cache.put(self.binding, self.lineage, stream.getvalue())
        self.assertEqual(self.r2.puts, [])

    def test_zip_without_complete_markdown_is_rejected_before_any_write(self):
        stream = io.BytesIO()
        with zipfile.ZipFile(stream, 'w') as archive:
            archive.writestr('images/chart.bin', b'asset')
        with self.assertRaises(ConsumerError): self.cache.put(self.binding, self.lineage, stream.getvalue())
        self.assertEqual(self.r2.puts, [])

    def test_source_hash_must_match_its_full_identity(self):
        binding = dict(self.binding, sha256='b' * 64)
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_source_identity'):
            self.cache.get(binding, self.lineage)
        self.assertEqual(self.r2.gets, [])

    def test_task_data_id_and_ordinal_are_exact_source_bindings(self):
        for lineage in (dict(self.lineage, data_id='b' * 64), dict(self.lineage, child_ordinal=True),
                        dict(self.lineage, child_ordinal=1), dict(self.lineage, full_zip_url='https://private.invalid/file')):
            with self.subTest(lineage=lineage), self.assertRaises(c.ResultCacheError):
                self.cache.get(self.binding, lineage)
        self.assertEqual(self.r2.gets, [])

    def test_child_and_original_results_have_distinct_cache_identities(self):
        child = dict(self.lineage, batch_id='child-task-1', batch_key='batches/' + 'b' * 32, child_ordinal=1)
        self.assertNotEqual(c.identity(self.binding, self.lineage), c.identity(self.binding, child))
        self.cache.put(self.binding, self.lineage, self.payload)
        self.assertIsNone(self.cache.get(self.binding, child))

    def test_receipt_source_task_and_blob_rebinding_are_rejected(self):
        self.cache.put(self.binding, self.lineage, self.payload)
        receipt_key, _ = self.keys(); original = copy.deepcopy(self.r2.objects[receipt_key])
        for change in (lambda value: value['source_binding'].__setitem__('size', 999),
                       lambda value: value['lineage'].__setitem__('batch_id', 'other-task'),
                       lambda value: value.__setitem__('blob_key', '_other/unknown.zip'),
                       lambda value: value.__setitem__('zip_bytes', len(self.payload) + 1)):
            self.r2.objects[receipt_key] = copy.deepcopy(original); self.tamper_receipt(change)
            with self.assertRaises(c.ResultCacheError): self.cache.get(self.binding, self.lineage)

    def test_receipt_duplicate_json_keys_are_rejected(self):
        self.cache.put(self.binding, self.lineage, self.payload)
        receipt_key, _ = self.keys(); item = self.r2.objects[receipt_key]
        item['Body'] = item['Body'][:-1] + b',"schema_version":1}'
        item['Metadata']['sha256'] = m.digest(item['Body'])
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_receipt_json'):
            self.cache.get(self.binding, self.lineage)

    def test_blob_tampering_is_rejected_even_with_refreshed_object_hash(self):
        self.cache.put(self.binding, self.lineage, self.payload)
        _, blob_key = self.keys(); item = self.r2.objects[blob_key]
        item['Body'] = result_zip('Changed source numbers.')
        item['Metadata']['sha256'] = m.digest(item['Body'])
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_zip_receipt'):
            self.cache.get(self.binding, self.lineage)

    def test_object_content_type_identity_and_metadata_hash_are_required(self):
        self.cache.put(self.binding, self.lineage, self.payload)
        receipt_key, blob_key = self.keys()
        for key in (receipt_key, blob_key):
            original = copy.deepcopy(self.r2.objects[key])
            for change in (lambda value: value.__setitem__('ContentType', 'text/html'),
                           lambda value: value['Metadata'].__setitem__('identity-sha256', 'f' * 64),
                           lambda value: value['Metadata'].__setitem__('sha256', '0' * 64)):
                self.r2.objects[key] = copy.deepcopy(original); change(self.r2.objects[key])
                with self.assertRaises(c.ResultCacheError): self.cache.get(self.binding, self.lineage)
            self.r2.objects[key] = original

    def test_missing_blob_after_receipt_is_corruption_never_cache_miss(self):
        self.cache.put(self.binding, self.lineage, self.payload)
        _, blob_key = self.keys(); del self.r2.objects[blob_key]
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_object_missing'):
            self.cache.get(self.binding, self.lineage)

    def test_non404_read_failure_never_becomes_cache_miss(self):
        for error in (S3Error('AccessDenied', 403), S3Error('InternalError', 500),
                      S3Error('NoSuchKey', 500), ConnectionResetError()):
            def fail(key, error=error): raise error
            self.r2.before_get = fail
            with self.assertRaisesRegex(c.ResultCacheError, 'cache_read_failed'):
                self.cache.get(self.binding, self.lineage)
        self.assertEqual(self.r2.puts, [])

    def test_lost_blob_or_receipt_ack_uses_readback_without_rewrite(self):
        def lost(key, values): raise ConnectionResetError('lost private ACK')
        self.r2.after_put = lost
        self.assertEqual(self.cache.put(self.binding, self.lineage, self.payload), self.payload)
        self.assertEqual(len(self.r2.puts), 2)

    def test_unknown_uncommitted_write_aborts_after_one_attempt(self):
        def lost(key, values): raise ConnectionResetError('lost private ACK')
        self.r2.before_put = lost
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_write_unresolved'):
            self.cache.put(self.binding, self.lineage, self.payload)
        self.assertEqual(len(self.r2.puts), 1); self.assertEqual(self.r2.objects, {})

    def test_definite_conflict_without_readable_object_does_not_replay_write(self):
        def lost(key, values): raise S3Error('ConditionalRequestConflict', 409)
        self.r2.before_put = lost
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_write_conflict'):
            self.cache.put(self.binding, self.lineage, self.payload)
        self.assertEqual(len(self.r2.puts), 1)

    def concurrent_put(self, payloads):
        barrier = threading.Barrier(2)
        def wait_receipt(key, values):
            if key.endswith('/receipt.json'): barrier.wait(timeout=5)
        self.r2.before_put = wait_receipt
        outcomes = []; lock = threading.Lock()
        def worker(payload):
            try: result = self.cache.put(self.binding, self.lineage, payload)
            except Exception as error: result = error
            with lock: outcomes.append(result)
        threads = [threading.Thread(target=worker, args=(payload,)) for payload in payloads]
        for thread in threads: thread.start()
        for thread in threads: thread.join(timeout=10)
        self.assertFalse(any(thread.is_alive() for thread in threads))
        return outcomes

    def test_identical_concurrent_writers_verify_same_canonical_bytes(self):
        outcomes = self.concurrent_put([self.payload, self.payload])
        self.assertEqual(outcomes, [self.payload, self.payload])
        self.assertEqual(len(self.r2.objects), 2)
        self.assertEqual(len([call for call in self.r2.puts if call['Key'].endswith('/receipt.json')]), 2)

    def test_different_concurrent_results_preserve_first_valid_receipt(self):
        other = result_zip('Another complete source.')
        outcomes = self.concurrent_put([self.payload, other])
        successes = [outcome for outcome in outcomes if isinstance(outcome, bytes)]
        failures = [outcome for outcome in outcomes if isinstance(outcome, c.ResultCacheError)]
        self.assertEqual((len(successes), len(failures)), (1, 1))
        self.assertEqual(self.cache.get(self.binding, self.lineage), successes[0])


if __name__ == '__main__':
    unittest.main()
