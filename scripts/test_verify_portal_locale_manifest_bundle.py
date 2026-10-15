"""No-network integration checks for public, immutable locale provenance."""
import copy
import hashlib
import json
from pathlib import Path
import tempfile
import unittest

import portal_locale_manifest as codec
from test_portal_locale_manifest import with_source_fallback
from verify_portal_locale_manifest_bundle import verify_bundle

RELEASE = 'a' * 32
TREE = 'b' * 64
IMMUTABLE = '.well-known/edge-release/' + RELEASE + '/'

def sharded_fixture(manifest):
    value = with_source_fallback(copy.deepcopy(manifest))
    units = value['source_fallbacks']['units']
    prefix = next(iter(units['ko']))[0]
    descriptor, body = codec._encode_fallback_shard(units, prefix, value['prompt_version'])
    value['source_fallbacks'] = {'schema_version': 5, 'counts': value['source_fallbacks']['counts'],
                                'shards': [descriptor]}
    return value, {descriptor['path']: body}


class PublicBundleTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name).resolve()
        self.manifest, self.files = sharded_fixture({'schema_version': 1})
        self.files['data/i18n/manifest.json'] = codec._json_bytes(self.manifest)
        for relative, body in self.files.items():
            path = self.root / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_bytes(body)
        self.calls = []
        self.now = 0

    def fetch(self, url, path, **options):
        self.assertTrue(url.startswith('https://portal.example.invalid/'))
        relative = url.removeprefix('https://portal.example.invalid/')
        self.calls.append(relative)
        if relative == '.well-known/edge-state':
            body = json.dumps({'schema_version': 1, 'slot': 'b', 'release_id': RELEASE, 'tree_sha256': TREE}).encode()
        else:
            body = self.files[relative.removeprefix(IMMUTABLE)]
            self.assertEqual(options['max_bytes'], codec.MAX_LOCALE_MANIFEST_BYTES)
            self.assertEqual(options['expected_bytes'], len(body))
            self.assertEqual(options['expect_sha256'], hashlib.sha256(body).hexdigest())
        self.assertLessEqual(options['max_total_time'], 600 - self.now)
        path.write_bytes(body)

    def verify(self, fetcher=None):
        return verify_bundle(self.root / 'data/i18n/manifest.json', 'https://portal.example.invalid',
                             self.root / 'evidence', release=RELEASE, tree=TREE,
                             fetcher=fetcher or self.fetch, clock=lambda: self.now)

    def test_every_shard_is_checked_between_matching_roots(self):
        result = self.verify()
        self.assertEqual(result['source_shards_verified_per_namespace'], 1)
        self.assertEqual(result['source_unit_count'], 10)
        self.assertEqual(result['source_fallback_counts'], {'ko': 1, 'ja': 0, 'ar': 0})
        self.assertEqual(result['source_fallback_references'], 1)
        size = self.manifest['source_fallbacks']['shards'][0]['byte_size']
        self.assertEqual(result['source_shard_wire_bytes'], size)
        self.assertEqual(result['max_source_shard_wire_bytes'], size)
        three = ['data/i18n/manifest.json', self.manifest['source_fallbacks']['shards'][0]['path'], 'data/i18n/manifest.json']
        self.assertEqual(self.calls, ['.well-known/edge-state'] + [IMMUTABLE + p for p in three] + three + ['.well-known/edge-state'])

    def test_missing_corrupt_and_replaced_release_never_pass(self):
        for failure in ('missing', 'corrupt', 'root-changed', 'release-changed'):
            self.calls.clear()
            def fetch(url, path, **options):
                self.fetch(url, path, **options)
                if ('source-fallbacks/' in url and failure == 'missing'):
                    path.unlink()
                if ('source-fallbacks/' in url and failure == 'corrupt') or (len(self.calls) == 4 and failure == 'root-changed'):
                    path.write_bytes(b'x' * path.stat().st_size)
                if failure == 'release-changed' and len(self.calls) == 8:
                    value = json.loads(path.read_bytes()); value['release_id'] = 'c' * 32
                    path.write_text(json.dumps(value))
            with self.subTest(failure=failure), self.assertRaises((ValueError, OSError)):
                self.verify(fetch)

    def test_invalid_namespace_rejected_before_any_http(self):
        value = copy.deepcopy(self.manifest)
        value['source_fallbacks']['shards'][0]['path'] = 'https://another.example/foreign.json'
        (self.root / 'data/i18n/manifest.json').write_bytes(codec._json_bytes(value))
        with self.assertRaises(codec.LocaleManifestError):
            self.verify()
        self.assertEqual(self.calls, [])

    def test_old_unsharded_root_remains_supported(self):
        self.files['data/i18n/manifest.json'] = codec._json_bytes({'schema_version': 1, 'coverage': {'ko': 1.0}})
        (self.root / 'data/i18n/manifest.json').write_bytes(self.files['data/i18n/manifest.json'])
        self.assertEqual(self.verify()['source_shards_verified_per_namespace'], 0)

    def test_shared_deadline_stops_before_another_request(self):
        def fetch(url, path, **options):
            self.fetch(url, path, **options)
            self.now += 301
        with self.assertRaisesRegex(ValueError, 'time budget exhausted'):
            self.verify(fetch)
        self.assertEqual(len(self.calls), 2)


if __name__ == '__main__':
    unittest.main()
