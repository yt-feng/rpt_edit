"""Lossless bounded manifest encoding for the production size regression."""
import base64
import copy
import hashlib
import json
import os
from pathlib import Path
import unittest
import zlib
from unittest.mock import patch
import portal_locale_manifest as codec
from test_portal_locale_manifest import with_source_fallback, LOCALES


def retained_accounting(fallback):
    if fallback['schema_version'] in {3, 4}:
        fallback = codec._decompress_fallback_records(fallback)
    if fallback['schema_version'] == 1:
        unique_rows = {codec._json_bytes(row) for rows in fallback['units'].values() for row in rows.values()}
        row_bytes = sum(map(len, unique_rows))
    else:
        row_bytes = sum(len(codec._json_bytes(row)) for row in fallback['records'])
    ref_bytes = sum(len(key.encode()) + 8 for rows in fallback['units'].values() for key in rows)
    return row_bytes, ref_bytes


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

    def test_decoding_keeps_records_shared_instead_of_reexpanding_each_locale(self):
        original, raw = self.packed()
        packed = json.loads(raw)['source_fallbacks']
        # A table that is small when retained once must not be rejected using
        # its hypothetical JSON size if repeated for each language.
        retained = sum(len(codec._json_bytes(row)) for row in packed['records'])
        retained += sum(len(key.encode()) + 8 for rows in packed['units'].values() for key in rows)
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', retained):
            decoded = codec.parse_locale_manifest(raw)
        self.assertEqual(decoded, original)
        rows = decoded['source_fallbacks']['units']
        key = next(iter(rows['ko']))
        self.assertIs(rows['ko'][key], rows['ja'][key])
        self.assertIs(rows['ja'][key], rows['ar'][key])
        shared = rows['ko'][key]
        for mutate in (lambda: shared.__setitem__('source', 'Altered source'),
                       lambda: shared.update(source='Altered source'),
                       lambda: shared.pop('source'), lambda: shared.clear()):
            with self.assertRaises(TypeError):
                mutate()
        self.assertEqual(copy.deepcopy(decoded), original)
        editable = dict(shared)
        editable['source'] = 'Independent edit'
        self.assertEqual(decoded, original)
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', retained - 1):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.parse_locale_manifest(raw)

    def test_shared_records_do_not_bypass_reference_limit_or_identity(self):
        _, raw = self.packed()
        with patch.object(codec, 'MAX_FALLBACK_REFERENCES', 2):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.parse_locale_manifest(raw)
        value = json.loads(raw)
        rows = value['source_fallbacks']['units']['ja']
        rows['0' * 64] = rows.pop(next(iter(rows)))
        with self.assertRaisesRegex(codec.LocaleManifestError, 'identity differs'):
            codec.parse_locale_manifest(codec._json_bytes(value))

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

    def compressed(self, schema_version=3):
        original, raw = self.packed()
        value = json.loads(raw)
        value['source_fallbacks'] = codec._compress_fallback_records(value['source_fallbacks'], schema_version=schema_version)
        return original, value

    def replace_compressed_table(self, value, table):
        body = codec._json_bytes(table)
        value['source_fallbacks'].update(byte_size=len(body), sha256=hashlib.sha256(body).hexdigest(),
                                       data=base64.b64encode(zlib.compress(body)).decode('ascii'))

    def test_compressed_roundtrip_still_validates_source_provenance(self):
        original, value = self.compressed()
        self.assertEqual(codec.parse_locale_manifest(codec._json_bytes(value)), original)
        table = json.loads(zlib.decompress(base64.b64decode(value['source_fallbacks']['data'])))
        table['records'][0]['source'] = 'Altered source 45%'
        self.replace_compressed_table(value, table)
        with self.assertRaisesRegex(codec.LocaleManifestError, 'hash differs'):
            codec.parse_locale_manifest(codec._json_bytes(value))

    def test_compressed_encoding_size_digest_and_stream_are_strict(self):
        _, original = self.compressed()
        for field, bad in [('byte_size', True), ('byte_size', 0), ('byte_size', codec.MAX_EXPANDED_FALLBACK_BYTES + 1),
                           ('encoding', 'gzip'), ('data', '!not base64!'), ('sha256', '0' * 64)]:
            value = copy.deepcopy(original); value['source_fallbacks'][field] = bad
            with self.subTest(field=field, bad=bad), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))
        zipped = base64.b64decode(original['source_fallbacks']['data'])
        for bad in (zipped[:-1], zipped + b'junk', zipped + zipped, zlib.compress(b'x' * 10000)):
            value = copy.deepcopy(original)
            value['source_fallbacks']['data'] = base64.b64encode(bad).decode('ascii')
            with self.subTest(size=len(bad)), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', 1):
            with self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(original))

    def test_compressed_shared_keys_cannot_hide_duplicate_or_missing_units(self):
        _, original = self.compressed()
        table = json.loads(zlib.decompress(base64.b64decode(original['source_fallbacks']['data'])))
        mutations = [lambda t: t['keys'].append(t['keys'][0]),
                     lambda t: t['keys'].append('0' * 64),
                     lambda t: t['units']['ko'].append(t['units']['ko'][0]),
                     lambda t: t['units']['ko'][0].__setitem__(0, True),
                     lambda t: t['units']['ko'][0].__setitem__(0, 99),
                     lambda t: t['units']['ko'][0].__setitem__(1, True),
                     lambda t: t.update(schema_version=3)]
        for mutate in mutations:
            value, bad = copy.deepcopy(original), copy.deepcopy(table)
            mutate(bad); self.replace_compressed_table(value, bad)
            with self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))
        value = copy.deepcopy(original); value['coverage']['ko'] = 1.0
        with self.assertRaises(codec.LocaleManifestError):
            codec.parse_locale_manifest(codec._json_bytes(value))

    def test_schema4_omits_only_derived_digest_and_preserves_shared_semantics(self):
        original, value = self.compressed(4)
        table = json.loads(zlib.decompress(base64.b64decode(value['source_fallbacks']['data'])))
        self.assertTrue(all(set(row) == {'source', 'context', 'reason', 'translation_class'} for row in table['records']))
        restored = codec.parse_locale_manifest(codec._json_bytes(value))
        self.assertEqual(restored, original)
        units = restored['source_fallbacks']['units']
        key = next(iter(units['ko']))
        self.assertIs(units['ko'][key], units['ja'][key])
        self.assertIs(units['ja'][key], units['ar'][key])
        with self.assertRaises(TypeError):
            units['ko'][key]['source_sha256'] = '0' * 64
        self.assertEqual(original, self.fixture())

    def test_all_four_schemas_keep_identical_retained_accounting(self):
        original, packed = self.packed()
        expected = retained_accounting(original['source_fallbacks'])
        self.assertEqual(retained_accounting(json.loads(packed)['source_fallbacks']), expected)
        for version in (3, 4):
            _, compressed = self.compressed(version)
            self.assertEqual(retained_accounting(compressed['source_fallbacks']), expected)

    def test_schema4_rejects_original_bad_hash_before_omitting_it(self):
        value, raw = self.packed()
        packed = json.loads(raw)['source_fallbacks']
        packed['records'][0]['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(codec.LocaleManifestError, 'hash before compaction'):
            codec._compress_fallback_records(packed, schema_version=4)
        key = next(iter(value['source_fallbacks']['units']['ko']))
        value['source_fallbacks']['units']['ko'][key]['source_sha256'] = '0' * 64
        with patch.object(codec, 'MAX_LOCALE_MANIFEST_BYTES', len(codec._json_bytes(value)) - 1):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'hash differs'):
                codec.encode_locale_manifest(value)

    def test_schema4_keeps_original_key_prompt_class_and_source_binding(self):
        _, original = self.compressed(4)
        table = json.loads(zlib.decompress(base64.b64decode(original['source_fallbacks']['data'])))
        for mutate in (lambda t: t['records'][0].update(source='Altered source 45%'),
                       lambda t: t['records'][0].update(translation_class='official-name'),
                       lambda t: t['keys'].__setitem__(0, '0' * 64)):
            value, bad = copy.deepcopy(original), copy.deepcopy(table)
            mutate(bad); self.replace_compressed_table(value, bad)
            with self.assertRaisesRegex(codec.LocaleManifestError, 'identity differs'):
                codec.parse_locale_manifest(codec._json_bytes(value))
        value = copy.deepcopy(original); value['prompt_version'] += '-changed'
        with self.assertRaisesRegex(codec.LocaleManifestError, 'identity differs'):
            codec.parse_locale_manifest(codec._json_bytes(value))

    def test_schema4_rejects_missing_extra_or_conflicting_record_fields(self):
        _, original = self.compressed(4)
        table = json.loads(zlib.decompress(base64.b64decode(original['source_fallbacks']['data'])))
        mutations = [lambda t: t['records'][0].pop('source'),
                     lambda t: t['records'][0].pop('context'),
                     lambda t: t['records'][0].update(source_sha256='0' * 64),
                     lambda t: t['records'][0].update(extra='unexpected'),
                     lambda t: t['records'][0].update(source=42),
                     lambda t: t.update(extra='unexpected')]
        for mutate in mutations:
            value, bad = copy.deepcopy(original), copy.deepcopy(table)
            mutate(bad); self.replace_compressed_table(value, bad)
            with self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))

    def test_schema4_full_restored_records_still_count_toward_retained_budget(self):
        original, raw = self.packed()
        packed = json.loads(raw)['source_fallbacks']
        retained = sum(len(codec._json_bytes(row)) for row in packed['records'])
        retained += sum(len(key.encode()) + 8 for rows in packed['units'].values() for key in rows)
        value = dict(original, source_fallbacks=codec._compress_fallback_records(packed, schema_version=4))
        self.assertLess(value['source_fallbacks']['byte_size'], retained)
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', retained):
            self.assertEqual(codec.parse_locale_manifest(codec._json_bytes(value)), original)
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', retained - 1):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.parse_locale_manifest(codec._json_bytes(value))
        with patch.object(codec, 'MAX_FALLBACK_REFERENCES', 2):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.parse_locale_manifest(codec._json_bytes(value))

    def test_schema4_keeps_strict_encoding_size_digest_stream_and_schema_guards(self):
        _, original = self.compressed(4)
        for field, bad in [('schema_version', 5), ('schema_version', 4.0), ('encoding', 'gzip'),
                           ('byte_size', True), ('byte_size', 1), ('byte_size', codec.MAX_EXPANDED_FALLBACK_BYTES + 1),
                           ('sha256', '0' * 64), ('data', '!not-base64!'), ('extra', 'unexpected')]:
            value = copy.deepcopy(original); value['source_fallbacks'][field] = bad
            with self.subTest(field=field, bad=bad), self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))
        zipped = base64.b64decode(original['source_fallbacks']['data'])
        for bad in (zipped[:-1], zipped + b'junk', zipped + zipped, zlib.compress(b'x' * 10000)):
            value = copy.deepcopy(original)
            value['source_fallbacks']['data'] = base64.b64encode(bad).decode('ascii')
            with self.assertRaises(codec.LocaleManifestError):
                codec.parse_locale_manifest(codec._json_bytes(value))

    def test_regression_growing_distinct_provenance_exceeds_intern_only_capacity(self):
        value = self.fixture()
        # Production on 2026-10-15 failed after 164,393 references: every
        # language recreated a full copy despite the compressed wire format.
        # Exercise an even larger source-preserving release with the same caps.
        count = 56000
        value['source_unit_count'] = count
        for locale in LOCALES:
            rows = {}
            for index in range(count):
                source = f'{index} ' + '原始研究指标与时间范围必须保留。' * 6
                key = hashlib.sha256(f"{value['prompt_version']}\0copy\0{source}".encode()).hexdigest()
                rows[key] = {'source': source, 'source_sha256': hashlib.sha256(source.encode()).hexdigest(),
                             'context': 'html:text:p', 'translation_class': 'copy',
                             'reason': 'translation_time_budget'}
            value['source_fallbacks']['units'][locale] = rows
            value['source_fallbacks']['counts'][locale] = count
            value['translation_entry_count'][locale] = 0
            value['resolved_entry_count'][locale] = count
            value['coverage'][locale] = 0.0
        raw = codec.encode_locale_manifest(value)
        packed = json.loads(raw)
        self.assertEqual(packed['source_fallbacks']['schema_version'], 4)
        self.assertLess(len(raw), codec.MAX_LOCALE_MANIFEST_BYTES)
        self.assertEqual(codec.parse_locale_manifest(raw), value)
        self.assertGreater(len(codec._json_bytes(value)), codec.MAX_EXPANDED_FALLBACK_BYTES)
        with patch.object(codec, 'MAX_EXPANDED_FALLBACK_BYTES', 8 * 1024 * 1024):
            with self.assertRaisesRegex(codec.LocaleManifestError, 'safety budget'):
                codec.encode_locale_manifest(value)

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

    @unittest.skipUnless(os.environ.get('LOCALE_MANIFEST_DIAGNOSTICS'), 'Exact production diagnostics were not requested')
    def test_exact_production_diagnostics_roundtrip_without_losing_source_units(self):
        path = Path(os.environ['LOCALE_MANIFEST_DIAGNOSTICS'])
        self.assertFalse(path.is_symlink())
        self.assertTrue(0 < path.stat().st_size <= 256 * 1024 * 1024)
        report = json.loads(path.read_text())
        self.assertIs(report.get('preflight_only'), False)
        count, units = report['source_unit_count'], report['source_fallbacks']
        self.assertIs(type(count), int)
        self.assertGreater(count, 0)
        self.assertEqual(set(units), set(LOCALES))
        counts = {locale: len(rows) for locale, rows in units.items()}
        self.assertEqual(counts, report['source_fallback_counts'])
        self.assertEqual(counts, report['remaining_units'])
        # This reconstructs only the exact accounting block rejected before
        # rendering. It does not claim that a release was built or published.
        value = self.fixture()
        value.update(source_unit_count=count,
                     translation_entry_count={locale: count - n for locale, n in counts.items()},
                     resolved_entry_count=dict.fromkeys(LOCALES, count),
                     coverage={locale: (count - n) / count for locale, n in counts.items()},
                     source_fallbacks={'schema_version': 1, 'units': units, 'counts': counts})
        codec.validate_translation_resolution(value, LOCALES)
        raw = codec.encode_locale_manifest(value)
        self.assertEqual(codec.parse_locale_manifest(raw), value)
        row_bytes, ref_bytes = retained_accounting(json.loads(raw)['source_fallbacks'])
        print(json.dumps({'production_accounting_roundtrip': 'passed', 'source_unit_count': count,
                          'source_fallback_counts': counts, 'encoded_bytes': len(raw),
                          'wire_limit': codec.MAX_LOCALE_MANIFEST_BYTES,
                          'retained_row_bytes': row_bytes, 'retained_reference_bytes': ref_bytes,
                          'retained_total_bytes': row_bytes + ref_bytes,
                          'references': sum(counts.values()), 'reference_limit': codec.MAX_FALLBACK_REFERENCES,
                          'retained_limit': codec.MAX_EXPANDED_FALLBACK_BYTES}, sort_keys=True))

    @unittest.skipUnless(os.environ.get('LOCALE_MANIFEST_FULL'), 'Exact complete manifest was not requested')
    def test_exact_complete_manifest_roundtrip_retains_all_metadata_and_bounds(self):
        path = Path(os.environ['LOCALE_MANIFEST_FULL'])
        original = codec.load_locale_manifest(path)
        old_body = path.read_bytes()
        old_wire = json.loads(old_body)
        if old_wire['source_fallbacks']['schema_version'] == 5:
            codec.validate_translation_resolution(original, LOCALES)
            self.assertLessEqual(len(old_body), codec.MAX_LOCALE_MANIFEST_BYTES)
            print(json.dumps({'complete_sharded_manifest': 'verified',
                              'source_unit_count': original['source_unit_count'],
                              'shards': len(codec.locale_manifest_shard_descriptors(original)),
                              'root_wire_bytes': len(old_body)}, sort_keys=True))
            return
        self.assertIn(old_wire['source_fallbacks']['schema_version'], (3, 4))
        new_body = codec.encode_locale_manifest(original)
        new_wire = json.loads(new_body)
        self.assertEqual(new_wire['source_fallbacks']['schema_version'], 4)
        self.assertEqual(codec.parse_locale_manifest(new_body), original)
        self.assertEqual({key: value for key, value in old_wire.items() if key != 'source_fallbacks'},
                         {key: value for key, value in new_wire.items() if key != 'source_fallbacks'})
        packed = codec._decompress_fallback_records(new_wire['source_fallbacks'])
        row_bytes = sum(len(codec._json_bytes(row)) for row in packed['records'])
        ref_bytes = sum(len(key.encode()) + 8 for rows in packed['units'].values() for key in rows)
        references = sum(len(rows) for rows in packed['units'].values())
        self.assertLessEqual(row_bytes + ref_bytes, codec.MAX_EXPANDED_FALLBACK_BYTES)
        self.assertLessEqual(references, codec.MAX_FALLBACK_REFERENCES)
        print(json.dumps({'complete_manifest_roundtrip': 'passed', 'source_unit_count': original['source_unit_count'],
                          'input_sha256': hashlib.sha256(old_body).hexdigest(),
                          'before_wire_bytes': len(old_body), 'after_wire_bytes': len(new_body),
                          'wire_limit': codec.MAX_LOCALE_MANIFEST_BYTES,
                          'before_decoded_table_bytes': old_wire['source_fallbacks']['byte_size'],
                          'after_decoded_table_bytes': new_wire['source_fallbacks']['byte_size'],
                          'retained_row_bytes': row_bytes, 'retained_reference_bytes': ref_bytes,
                          'retained_total_bytes': row_bytes + ref_bytes, 'retained_limit': codec.MAX_EXPANDED_FALLBACK_BYTES,
                          'references': references, 'reference_limit': codec.MAX_FALLBACK_REFERENCES}, sort_keys=True))


if __name__ == '__main__':
    unittest.main()
