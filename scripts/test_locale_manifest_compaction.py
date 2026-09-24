"""Lossless bounded manifest encoding for the production size regression."""
import copy
import hashlib
import json
import unittest
from unittest.mock import patch
import portal_locale_manifest as codec
from test_portal_locale_manifest import with_source_fallback, LOCALES


class CompactionTests(unittest.TestCase):
    def fixture(self):
        value = with_source_fallback({'schema_version': 1})
        row = copy.deepcopy(next(iter(value['source_fallbacks']['units']['ko'].items())))
        for locale in LOCALES:
            value['source_fallbacks']['units'][locale] = {row[0]: dict(row[1])}
            value['source_fallbacks']['counts'][locale] = 1
            value['translation_entry_count'][locale] = 9
            value['coverage'][locale] = .9
        return value

    def packed(self):
        value = self.fixture()
        limit = len(codec._json_bytes(value)) - 1
        with patch.object(codec, 'MAX_LOCALE_MANIFEST_BYTES', limit):
            raw = codec.encode_locale_manifest(value)
        return value, raw

    def test_small_legacy_body_is_unchanged(self):
        value = self.fixture()
        self.assertEqual(codec.encode_locale_manifest(value), codec._json_bytes(value))

    def test_lossless_roundtrip_preserves_provenance_coverage_and_input(self):
        original, raw = self.packed()
        self.assertEqual(json.loads(raw)['source_fallbacks']['schema_version'], 2)
        self.assertEqual(codec.parse_locale_manifest(raw), original)
        self.assertEqual(original, self.fixture())
        codec.validate_translation_resolution(codec.parse_locale_manifest(raw), LOCALES)

    def test_bad_reference_and_hash_remain_fatal(self):
        _, raw = self.packed()
        for bad in (True, -1, 9, '0'):
            value = json.loads(raw)
            rows = value['source_fallbacks']['units']['ko']
            rows[next(iter(rows))] = bad
            with self.subTest(bad=bad), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))
        value = json.loads(raw)
        value['source_fallbacks']['records'][0]['source'] = 'Altered claim 45%'
        with self.assertRaisesRegex(codec.LocaleManifestError, 'hash differs'):
            codec.parse_locale_manifest(codec._json_bytes(value))

    def test_counts_cannot_be_upgraded_to_fully_translated(self):
        _, raw = self.packed()
        value = json.loads(raw); value['coverage']['ko'] = 1.0
        with self.assertRaises(codec.LocaleManifestError):
            codec.parse_locale_manifest(codec._json_bytes(value))

    def test_unused_records_and_expansion_bombs_rejected(self):
        _, raw = self.packed()
        value = json.loads(raw)
        value['source_fallbacks']['records'].append(value['source_fallbacks']['records'][0])
        with self.assertRaisesRegex(codec.LocaleManifestError, 'Unused'):
            codec.parse_locale_manifest(codec._json_bytes(value))
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', 1):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.parse_locale_manifest(raw)

    def test_large_nonfallback_manifest_still_rejected(self):
        with patch.object(codec, 'MAX_LOCALE_MANIFEST_BYTES', 128):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'byte size'):
                codec.encode_locale_manifest({'schema_version': 1, 'padding': 'a' * 200})

    def test_regression_40042_fallback_rows_fit_without_truncation(self):
        value = self.fixture()
        rows = {}
        for index in range(14000):
            source = f'{index} ' + '原始研究指标与时间范围必须保留。' * 5
            key = hashlib.sha256(f"{value['prompt_version']}\0copy\0{source}".encode()).hexdigest()
            rows[key] = {'source': source, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                         'context': 'html:text:p', 'translation_class': 'copy', 'reason': 'translation_time_budget'}
        sizes = {'ko': 13008, 'ja': 13284, 'ar': 13750}
        value['source_unit_count'] = 80191
        for locale, n in sizes.items():
            value['source_fallbacks']['units'][locale] = dict(list(rows.items())[:n])
            value['source_fallbacks']['counts'][locale] = n
            value['translation_entry_count'][locale] = 80191 - n
            value['resolved_entry_count'][locale] = 80191
            value['coverage'][locale] = (80191-n)/80191
        self.assertGreater(len(codec._json_bytes(value)), codec.MAX_LOCALE_MANIFEST_BYTES)
        raw = codec.encode_locale_manifest(value)
        self.assertLess(len(raw), codec.MAX_LOCALE_MANIFEST_BYTES)
        restored = codec.parse_locale_manifest(raw)
        self.assertEqual(restored, value)
        self.assertEqual(sum(restored['source_fallbacks']['counts'].values()), 40042)


if __name__ == '__main__':
    unittest.main()
