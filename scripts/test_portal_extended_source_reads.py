"""Offline R2 source-read sharing; mutable state remains fresh on every read."""
from collections import Counter
from concurrent.futures import Future, ThreadPoolExecutor
import copy
import io
import json
import threading
import unittest
from unittest.mock import patch
import weakref
import gc

from portal_extended_continuation import origin_key, read_origin
from portal_extended_daily_queue import (_SourceCorpusCache, POLICY, queue_key,
    read_corpus, read_corpus_bytes, read_queue)
from portal_extended_locales import ExpansionError, digest, make_corpus, stable_bytes
from portal_extended_r2 import R2IntegrityError, R2PermissionError, R2Store, R2TransportError
from test_portal_extended_incremental import DAY, ORIGIN, daily_doc
from test_portal_extended_r2 import FakeR2


class CountedR2(FakeR2):
    def __init__(self):
        super().__init__()
        self.reads = Counter()
        self.lock = threading.Lock()

    def head_object(self, **kwargs):
        with self.lock:
            self.reads['head', kwargs['Key']] += 1
        return super().head_object(**kwargs)

    def get_object(self, **kwargs):
        with self.lock:
            self.reads['get', kwargs['Key']] += 1
        response = super().get_object(**kwargs)
        return {'Body': io.BytesIO(response['Body'].read())}


class SourceReadTests(unittest.TestCase):
    def setUp(self):
        self.client = CountedR2()
        self.store = self.fresh_store()
        self.corpus = make_corpus([daily_doc()])
        self.generation = self.corpus['documents_sha256']
        self.key = self.store.source_key(self.generation)
        self.store.put_source(self.corpus)
        self.raw = self.client.objects[self.key]['body']
        self.client.reads.clear()

    def fresh_store(self):
        return R2Store(self.client, 'private', '_extended-locales/staging/source-reads')

    def source_reads(self, key=None):
        key = key or self.key
        return self.client.reads['head', key], self.client.reads['get', key]

    def save_origin(self, source_hash):
        value = {'schema_version': 1, 'generation': self.generation,
            'source_sha256': source_hash, 'source_day': DAY, 'pages': 1,
            'locales': ['fr'], 'producer': {'run_id': '123', 'attempt': '1', 'sha': 'a' * 40}}
        self.store._put(origin_key(self.store, self.generation), stable_bytes(value), metadata={'kind': 'test'})
        return value

    def test_repeated_reads_use_one_head_and_get_and_return_independent_copies(self):
        first = read_corpus(self.store, self.generation)
        first['documents'][0]['blocks'][0]['text'] = 'caller edit'
        first['documents'].clear()
        self.assertEqual(read_corpus(self.store, self.generation), self.corpus)
        self.assertEqual(read_corpus_bytes(self.store, self.generation), self.raw)
        self.assertEqual(self.source_reads(), (1, 1))

    def test_raw_bytes_and_origin_checksum_are_preserved_on_cache_hits(self):
        # The receipt hashes original bytes, not reserialized or normalized JSON.
        raw = json.dumps(self.corpus, indent=2).encode() + b'\n'
        self.store._put(self.key, raw, metadata={'kind': 'test'})
        origin = self.save_origin(digest(raw))
        self.client.reads.clear()
        for _ in range(2):
            self.assertEqual(read_origin(self.store, self.generation), origin)
            self.assertEqual(read_corpus_bytes(self.store, self.generation), raw)
        self.assertEqual(self.source_reads(), (1, 1))
        receipt_key = origin_key(self.store, self.generation)
        self.assertEqual(self.source_reads(receipt_key), (2, 2))
        self.save_origin('0' * 64)
        with self.assertRaisesRegex(ExpansionError, 'origin differs'):
            read_origin(self.store, self.generation)
        self.assertEqual(self.source_reads(), (1, 1))

    def test_permission_and_invalid_source_failures_are_never_cached(self):
        self.client.deny = True
        with self.assertRaises(R2PermissionError):
            read_corpus(self.store, self.generation)
        self.client.deny = False
        self.assertEqual(read_corpus(self.store, self.generation), self.corpus)
        self.assertEqual(self.source_reads(), (2, 1))

        other = make_corpus([daily_doc(ORIGIN + '/blog/20260925-other.html')])
        damaged = copy.deepcopy(self.corpus)
        damaged['documents'][0]['title'] = 'invalid content digest'
        for bad, error in ((b'broken JSON', json.JSONDecodeError),
                           (stable_bytes(damaged), ExpansionError),
                           (stable_bytes(other), R2IntegrityError)):
            with self.subTest(error=error):
                store = self.fresh_store()
                store._put(self.key, bad, metadata={'kind': 'test'})
                with self.assertRaises(error):
                    read_corpus(store, self.generation)
                self.assertFalse(store._source_corpus_cache.entries)
                self.assertFalse(store._source_corpus_cache.inflight)
                store._put(self.key, self.raw, metadata={'kind': 'test'})
                self.assertEqual(read_corpus(store, self.generation), self.corpus)

    def test_r2_checksum_failure_is_not_cached(self):
        self.client.objects[self.key]['Metadata']['sha256'] = '0' * 64
        with self.assertRaises(R2IntegrityError):
            read_corpus(self.store, self.generation)
        self.client.objects[self.key]['Metadata']['sha256'] = digest(self.raw)
        self.assertEqual(read_corpus(self.store, self.generation), self.corpus)
        self.assertEqual(self.source_reads(), (2, 2))

    def test_four_readers_share_one_fetch_and_failed_flight_can_be_retried(self):
        for fail in (False, True):
            with self.subTest(fail=fail):
                store = self.fresh_store()
                barrier = threading.Barrier(4)
                followers = threading.Event()
                release = threading.Event()
                arrivals = []
                lock = threading.Lock()

                class ObservedFuture(Future):
                    def result(self, timeout=None):
                        with lock:
                            arrivals.append(1)
                            if len(arrivals) == 3:
                                followers.set()
                        return super().result(timeout)

                original_get = store._get

                def blocked_get(*args, **kwargs):
                    if not release.wait(5):
                        raise AssertionError('Concurrent readers did not join the flight')
                    if fail:
                        raise R2TransportError('synthetic transport failure')
                    return original_get(*args, **kwargs)

                def read():
                    barrier.wait(timeout=5)
                    return read_corpus_bytes(store, self.generation)

                with patch('portal_extended_daily_queue.Future', ObservedFuture), \
                        patch.object(store, '_get', side_effect=blocked_get) as fetch, \
                        ThreadPoolExecutor(max_workers=4) as pool:
                    results = [pool.submit(read) for _ in range(4)]
                    try:
                        self.assertTrue(followers.wait(5), 'All followers must await the same fetch')
                    finally:
                        release.set()
                    for result in results:
                        if fail:
                            with self.assertRaises(R2TransportError):
                                result.result(timeout=5)
                        else:
                            self.assertEqual(result.result(timeout=5), self.raw)
                    self.assertEqual(fetch.call_count, 1)
                self.assertFalse(store._source_corpus_cache.inflight)
                if fail:
                    self.assertFalse(store._source_corpus_cache.entries)
                    self.assertEqual(read_corpus_bytes(store, self.generation), self.raw)

    def test_unrelated_generations_are_not_serialized_behind_one_fetch(self):
        other = make_corpus([daily_doc(ORIGIN + '/blog/20260925-other.html')])
        self.store.put_source(other)
        barrier = threading.Barrier(2)
        original_get = self.store._get

        def fetch(*args, **kwargs):
            barrier.wait(timeout=5)
            return original_get(*args, **kwargs)

        with patch.object(self.store, '_get', side_effect=fetch), ThreadPoolExecutor(max_workers=2) as pool:
            results = [pool.submit(read_corpus, self.store, item['documents_sha256'])
                       for item in (self.corpus, other)]
            self.assertEqual([result.result(timeout=5) for result in results], [self.corpus, other])

    def test_lru_entry_and_byte_limits_and_oversized_bypass(self):
        corpora = [self.corpus] + [make_corpus([daily_doc(ORIGIN + f'/blog/20260925-{i}.html')])
                                  for i in range(2)]
        for corpus in corpora[1:]:
            self.store.put_source(corpus)
        generations = [corpus['documents_sha256'] for corpus in corpora]
        self.store._source_corpus_cache = _SourceCorpusCache(max_entries=2)
        self.client.reads.clear()
        for index in (0, 1, 0, 2, 0, 1):
            self.assertEqual(read_corpus(self.store, generations[index]), corpora[index])
        self.assertEqual(self.source_reads(), (1, 1))
        self.assertEqual(self.source_reads(self.store.source_key(generations[1])), (2, 2))
        self.assertEqual(len(self.store._source_corpus_cache.entries), 2)

        byte_limit = len(self.raw) + len(self.client.objects[self.store.source_key(generations[1])]['body']) - 1
        cache = self.store._source_corpus_cache = _SourceCorpusCache(max_bytes=byte_limit)
        self.client.reads.clear()
        for index in (0, 1, 0):
            read_corpus(self.store, generations[index])
            self.assertLessEqual(cache.byte_count, byte_limit)
        self.assertEqual(self.source_reads(), (2, 2))
        self.assertEqual(len(cache.entries), 1)

        cache = self.store._source_corpus_cache = _SourceCorpusCache(max_bytes=len(self.raw) - 1)
        self.client.reads.clear()
        for _ in range(2):
            self.assertEqual(read_corpus(self.store, self.generation), self.corpus)
        self.assertEqual(self.source_reads(), (2, 2))
        self.assertEqual((len(cache.entries), cache.byte_count), (0, 0))

    def test_cache_is_per_store_and_dies_with_its_owner(self):
        for store in (self.store, self.fresh_store()):
            self.assertEqual(read_corpus(store, self.generation), self.corpus)
        self.assertEqual(self.source_reads(), (2, 2))
        cache_ref = weakref.ref(store._source_corpus_cache)
        del store
        gc.collect()
        self.assertIsNone(cache_ref())

    def test_queue_and_checkpoint_latest_are_read_fresh(self):
        read_corpus(self.store, self.generation)
        pointer = self.store.checkpoint_pointer_key('fr', self.generation)
        entry = {'day': DAY, 'admission': 'b' * 64}
        for entries, revision in (([], 1), ([entry], 2)):
            self.store._put(queue_key(self.store), stable_bytes({'schema_version': 1,
                'policy': POLICY, 'entries': entries}), metadata={'kind': 'test'})
            self.store._put(pointer, stable_bytes({'revision': revision}), metadata={'kind': 'test'})
            self.assertEqual(read_queue(self.store), entries)
            self.assertEqual(json.loads(self.store._get(pointer, maximum=65536)), {'revision': revision})
        self.assertEqual(self.client.reads['get', queue_key(self.store)], 2)
        self.assertEqual(self.client.reads['get', pointer], 2)
        self.assertEqual(self.source_reads(), (1, 1))


if __name__ == '__main__':
    unittest.main()
