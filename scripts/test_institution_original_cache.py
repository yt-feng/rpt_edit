"""Exact-byte original preservation, immutable conflicts and stop boundaries."""
import copy
import io
from pathlib import Path
import tempfile
import types
import unittest
from unittest.mock import Mock, patch

import institution_original_cache as c
import mineru_task_ledger as m
from test_mineru_result_cache import MemoryR2, S3Error


class OriginalCacheTests(unittest.TestCase):
    def setUp(self):
        self.client = MemoryR2()
        self.cache = c.OriginalCache(self.client, 'private-test')
        self.payload = b'%PDF-1.7 exact-original\n'
        self.binding = self.binding_for(self.payload)

    @staticmethod
    def binding_for(payload, source='original.pdf', **changes):
        base = dict(source=source, sha256=m.digest(payload), size=len(payload),
                    scope='institution', endpoint='https://mineru.net', options=copy.deepcopy(c.OPTIONS))
        base.update(changes)
        return dict(base, id=m.digest(m.encoded(base)))

    def test_archive_is_immutable_private_and_reused_without_second_put(self):
        self.assertFalse(self.cache.put(self.binding, self.payload))
        self.assertEqual(self.cache.get(self.binding), self.payload)
        self.assertTrue(self.cache.put(self.binding, self.payload))
        self.assertEqual(len(self.client.puts), 1)
        put = self.client.puts[0]
        self.assertEqual(put['Key'], c.PREFIX + self.binding['sha256'] + '.pdf')
        self.assertEqual(put['IfNoneMatch'], '*')
        self.assertEqual(put['CacheControl'], 'private, no-store')
        self.assertEqual(put['ContentType'], 'application/pdf')
        # Another exact source binding may reuse the identical original bytes.
        self.assertTrue(self.cache.put(self.binding_for(self.payload, 'second.pdf'), self.payload))

    def test_bad_bindings_and_bytes_do_not_access_storage(self):
        variants = [dict(self.binding, id='0' * 64), dict(self.binding, size=True),
                    self.binding_for(self.payload, scope='dropbox'),
                    self.binding_for(self.payload, endpoint='https://example.test'),
                    self.binding_for(self.payload, options=dict(c.OPTIONS, ocr=False)),
                    self.binding_for(self.payload, source='../secret.pdf')]
        for binding in variants:
            with self.subTest(binding=binding), self.assertRaises(c.OriginalCacheError):
                self.cache.put(binding, self.payload)
        for payload in (b'not-pdf', self.payload+b'extra', b'%PDF-different-original'):
            with self.subTest(payload=payload), self.assertRaises(c.OriginalCacheError):
                self.cache.put(self.binding, payload)
        self.assertEqual(self.client.gets, [])
        self.assertEqual(self.client.puts, [])

    def test_only_404_is_a_miss_and_transport_never_writes(self):
        self.assertIsNone(self.cache.get(self.binding))
        for error in (S3Error('NoSuchKey', 403), S3Error('NotFound', 500), TimeoutError('private-url')):
            self.client.before_get = Mock(side_effect=error)
            with self.assertRaisesRegex(c.OriginalCacheError, '^original_read_failed$'):
                self.cache.put(self.binding, self.payload)
        self.assertEqual(self.client.puts, [])

    def test_lost_write_ack_stops_without_readback_or_second_write(self):
        self.client.after_put = Mock(side_effect=TimeoutError('private-url'))
        with self.assertRaisesRegex(c.OriginalCacheError, '^original_write_unresolved$'):
            self.cache.put(self.binding, self.payload)
        self.assertEqual(len(self.client.gets), 1)
        self.assertEqual(len(self.client.puts), 1)
        self.client.after_put = None
        self.assertTrue(self.cache.put(self.binding, self.payload))
        self.assertEqual(len(self.client.puts), 1)

    def test_only_definite_conflict_allows_readback(self):
        for status in (409, 412):
            client = MemoryR2()
            def concurrent_writer(key, request):
                client.objects[key] = {field: request[field] for field in ('Body', 'ContentType', 'Metadata')}
                raise S3Error(str(status), status)
            client.before_put = concurrent_writer
            self.assertTrue(c.OriginalCache(client, 'private-test').put(self.binding, self.payload))
            self.assertEqual(len(client.puts), 1)
            self.assertEqual(len(client.gets), 2)

    def test_conflict_without_matching_object_stops(self):
        self.client.before_put = Mock(side_effect=S3Error('PreconditionFailed', 412))
        with self.assertRaisesRegex(c.OriginalCacheError, '^original_readback$'):
            self.cache.put(self.binding, self.payload)
        self.assertEqual(len(self.client.puts), 1)

    def test_conflict_shaped_code_without_definite_status_never_reads_back(self):
        for status in (500, None, 403):
            client = MemoryR2()
            client.after_put = Mock(side_effect=S3Error('PreconditionFailed', status))
            with self.subTest(status=status), self.assertRaisesRegex(c.OriginalCacheError, 'original_write_unresolved'):
                c.OriginalCache(client, 'private-test').put(self.binding, self.payload)
            self.assertEqual(len(client.gets), 1)
            self.assertEqual(len(client.puts), 1)

    def test_corrupt_or_wrong_metadata_object_is_never_replaced(self):
        key = c.OriginalCache.key(self.binding)
        for field, wrong in (('Body', b'%PDF-wrong'), ('ContentType', 'text/plain'),
                             ('Metadata', {'sha256': self.binding['sha256'], 'kind': 'wrong'})):
            client = MemoryR2()
            value = dict(Body=self.payload, ContentType='application/pdf',
                         Metadata={'sha256': self.binding['sha256'], 'kind': 'institution-original-proof'})
            value[field] = wrong; client.objects[key] = value
            with self.subTest(field=field), self.assertRaises(c.OriginalCacheError):
                c.OriginalCache(client, 'private-test').put(self.binding, self.payload)
            self.assertEqual(client.puts, [])

    def test_stream_is_bounded_and_closed_even_on_bad_payload(self):
        for value in (self.payload, self.payload + b'x'):
            body = Mock(wraps=io.BytesIO(value))
            response = dict(Body=body, ContentLength=len(self.payload), ContentType='application/pdf',
                            Metadata={'sha256': self.binding['sha256'], 'kind': 'institution-original-proof'})
            client = Mock(); client.get_object.return_value = response
            if value == self.payload:
                self.assertEqual(c.OriginalCache(client, 'private-test').get(self.binding), self.payload)
            else:
                with self.assertRaises(c.OriginalCacheError):
                    c.OriginalCache(client, 'private-test').get(self.binding)
            body.read.assert_called_once_with(len(self.payload)+1)
            body.close.assert_called_once()

    def ledger(self):
        store = object.__new__(m.R2Store)
        store.client, store.bucket = self.client, 'private-test'
        return m.Ledger(store, Mock(), 'institution', 'https://mineru.net', c.OPTIONS, [('test', 'test-token')])

    def test_all_local_sources_validate_before_first_storage_operation(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/'a.pdf', Path(directory)/'b.pdf'
            a.write_bytes(self.payload); b.write_bytes(b'invalid')
            ledger = self.ledger()
            with self.assertRaises(c.OriginalCacheError):
                c.preserve_sources(ledger, [(a, 'a.pdf'), (b, 'b.pdf')])
            self.assertEqual(self.client.gets, [])
            self.assertEqual(self.client.puts, [])
            ledger.provider.assert_not_called()

    def test_total_bound_and_duplicate_reject_before_storage(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/'a.pdf', Path(directory)/'b.pdf'
            a.write_bytes(self.payload); b.write_bytes(self.payload)
            ledger = self.ledger()
            with patch.object(c, 'MAX_TOTAL', len(self.payload)):
                with self.assertRaisesRegex(c.OriginalCacheError, 'original_total_size'):
                    c.preserve_sources(ledger, [(a, 'a.pdf'), (b, 'b.pdf')])
            with self.assertRaisesRegex(c.OriginalCacheError, 'original_duplicate'):
                c.preserve_sources(ledger, [(a, 'a.pdf'), (a, 'a.pdf')])
            self.assertEqual(self.client.gets, [])

    def test_preserve_reads_back_all_originals_and_never_touches_provider(self):
        with tempfile.TemporaryDirectory() as directory:
            a, b = Path(directory)/'a.pdf', Path(directory)/'b.pdf'
            a.write_bytes(self.payload); b.write_bytes(self.payload+b'2')
            ledger = self.ledger(); sources = [(a, 'a.pdf'), (b, 'b.pdf')]
            result = c.preserve_sources(ledger, sources)
            self.assertEqual(result, dict(status='verified', originals=2, bytes=len(self.payload)*2+1, reused=0))
            self.assertEqual(c.preserve_sources(ledger, sources)['reused'], 2)
            self.assertEqual(ledger.provider.mock_calls, [])
            self.assertEqual(ledger.submission_posts, 0)

    def test_other_scopes_unchanged_and_institution_requires_private_store(self):
        self.assertEqual(c.preserve_sources(types.SimpleNamespace(scope='dropbox'), [])['status'], 'not_applicable')
        with self.assertRaisesRegex(c.OriginalCacheError, 'original_private_store_required'):
            c.preserve_sources(types.SimpleNamespace(scope='institution', store=object()), [])

    def test_injected_single_attempt_client_is_not_reconfigured(self):
        cache = c.OriginalCache.single_attempt(self.client, 'private-test')
        self.assertIs(cache.client, self.client)


if __name__ == '__main__':
    unittest.main()
