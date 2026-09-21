#!/usr/bin/env python3
"""Exact-source publication fallback without memoizing rejected translations."""
import gzip
import hashlib
import json
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_portal_locales as b
from offline_translation import OfflineTranslationError, OfflineTranslationValidationError


COPY = {'ko': '검증된 보고서를 읽으세요', 'ja': '検証済みレポートを読む', 'ar': 'اقرأ التقرير الموثوق'}


def valid_translation(source, locale):
    return COPY[locale] + ' ' + ' '.join(b.PLACEHOLDER_RE.findall(source))


class SourceFallbackTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.cache_path = Path(self.temporary.name) / 'cache.json.gz'
        self.source = '  收入增长12.5%，查看 https://example.invalid/report?q=1。\n'
        self.unit = b.unit_for_text(self.source, 'html:text:p')[1]
        self.neighbor = b.unit_for_text('阅读完整行业研究报告', 'html:text:p')[1]
        self.units = {unit.key: unit for unit in (self.unit, self.neighbor)}
        self.cache = b.empty_cache('hymt-offline-v1', provider='hymt')

    def run_translation(self, translate, **options):
        with mock.patch('offline_translation.OfflineTranslator') as factory, \
             mock.patch.object(b, 'deepseek_translate_batch', side_effect=AssertionError('Paid fallback')):
            factory.return_value.translate.side_effect = translate
            b.translate_missing_units(self.units, self.cache, cache_path=self.cache_path,
                model='hymt-offline-v1', base_url='https://example.invalid', workers=1,
                timeout=1, attempts=1, provider='hymt', **options)
            return factory.return_value.translate.call_args_list

    def saved(self):
        return json.loads(gzip.decompress(self.cache_path.read_bytes()))

    def test_changed_quantity_and_placeholder_retain_exact_source_and_retry(self):
        reasons = {'ko': 'Hy-MT2 quantity validation failed: financial_quantity_changed_missing_or_added',
                   'ja': 'Hy-MT2 placeholder validation failed'}
        def translate(source, locale):
            if source == self.unit.source and locale in reasons:
                raise OfflineTranslationValidationError(reasons[locale])
            return valid_translation(source, locale)
        self.run_translation(translate, allow_source_fallback=True)
        for locale, reason in reasons.items():
            self.assertEqual(b.translated_text(self.source, 'html:text:p', locale, self.cache), self.source)
            self.assertIn(COPY[locale], b.translated_text('阅读完整行业研究报告', 'html:text:p', locale, self.cache))
            row = self.cache['_source_fallbacks'][locale][self.unit.key]
            self.assertEqual(row['source_sha256'], hashlib.sha256(self.unit.source.encode()).hexdigest())
            self.assertEqual(row['reason'], reason)
            self.assertNotIn(self.unit.key, self.saved()['locales'][locale])
        self.assertNotIn('_source_fallbacks', self.saved())
        calls = self.run_translation(valid_translation, allow_source_fallback=True)
        self.assertEqual({(call.args[0], call.args[1]) for call in calls},
                         {(self.unit.source, 'ko'), (self.unit.source, 'ja')})
        self.assertFalse(any(self.cache['_source_fallbacks'].values()))

    def test_locale_quality_failure_is_retained_but_default_remains_strict(self):
        def translate(source, locale):
            return source if source == self.unit.source else valid_translation(source, locale)
        with self.assertRaisesRegex(b.TranslationError, 'unresolved'):
            self.run_translation(translate)
        self.run_translation(translate, allow_source_fallback=True)
        self.assertEqual(b.translated_text(self.source, 'html:text:p', 'ko', self.cache), self.source)

    def test_unknown_runtime_and_programming_errors_remain_failures(self):
        for error in (OfflineTranslationError('runtime stopped'), OSError('transport failed'), TypeError('bad argument')):
            with self.subTest(error=error), self.assertRaises(type(error) if not isinstance(error, OfflineTranslationError) else b.TranslationError):
                self.run_translation(mock.Mock(side_effect=error), allow_source_fallback=True)
            self.assertFalse(any(self.cache.get('_source_fallbacks', {}).values()))

    def test_budget_keeps_completed_rows_then_retains_unattempted_units(self):
        clock = [0]
        def translate(source, locale):
            clock[0] = 2
            return valid_translation(source, locale)
        with mock.patch.object(b.time, 'monotonic', side_effect=lambda: clock[0]):
            calls = self.run_translation(translate, allow_source_fallback=True, offline_time_budget_seconds=1)
        self.assertEqual(len(calls), 1)
        translated_count = sum(len(rows) for rows in self.saved()['locales'].values())
        self.assertEqual(translated_count, 1)
        fallbacks = [row for rows in self.cache['_source_fallbacks'].values() for row in rows.values()]
        self.assertEqual(len(fallbacks), len(self.units) * len(b.LOCALES) - 1)
        self.assertEqual({row['reason'] for row in fallbacks}, {'translation_time_budget'})
        self.assertNotIn('_source_fallbacks', self.saved())
        calls = self.run_translation(valid_translation, allow_source_fallback=True)
        self.assertEqual(len(calls), len(fallbacks))

    def test_strict_budget_still_stops_without_source_overlay(self):
        with mock.patch.object(b.time, 'monotonic', side_effect=[0, 2]):
            with self.assertRaises(b.TranslationStopped):
                self.run_translation(valid_translation, offline_time_budget_seconds=1)
        self.assertNotIn('_source_fallbacks', self.cache)

    def test_caller_rejection_discards_only_its_real_hymt_memo(self):
        from hymt_offline_translation import HyMTOfflineTranslator
        bad_source = '这是用于测试的中文说明并且包含完整的长句子'
        bad_unit = b.unit_for_text(bad_source, 'html:text:p')[1]
        self.units = {bad_unit.key: bad_unit, self.neighbor.key: self.neighbor}
        calls = []
        class Engine:
            def translate(self, source, source_language, locale):
                calls.append((source, locale))
                if source == bad_source and locale == 'ja':
                    return source
                return valid_translation(source, locale)
        translator = HyMTOfflineTranslator(cache_dir=Path(self.temporary.name) / 'memo',
                                           engine_factory=lambda _source, _target: Engine())
        with mock.patch('offline_translation.OfflineTranslator', return_value=translator):
            for _ in range(2):
                b.translate_missing_units(self.units, self.cache, cache_path=self.cache_path,
                    model=translator.model_id, base_url='https://example.invalid', workers=1,
                    timeout=1, attempts=1, provider='hymt', allow_source_fallback=True)
        self.assertEqual(calls.count((bad_source, 'ja')), 2)
        self.assertEqual(calls.count((self.neighbor.source, 'ja')), 1)
        self.assertNotIn(bad_unit.key, self.saved()['locales']['ja'])
        before = len(calls)
        translator.translate(self.neighbor.source, 'ja')
        self.assertEqual(len(calls), before)
        _identity, path = translator._memo_identity(bad_source, 'ja', 'zh', markdown=True)
        self.assertFalse(path.exists())

    def test_budget_requires_a_finite_positive_number(self):
        for budget in (0, -1, float('nan'), float('inf')):
            with self.subTest(budget=budget), self.assertRaises(b.TranslationError):
                self.run_translation(valid_translation, offline_time_budget_seconds=budget)

    def test_best_effort_does_not_start_an_unbounded_batch(self):
        class Translator:
            def translate_many(self, *_args):
                raise AssertionError('Best effort must check the deadline before each unit')
            def translate(self, source, locale):
                return valid_translation(source, locale)
        with mock.patch('offline_translation.OfflineTranslator', return_value=Translator()):
            b.translate_missing_units(self.units, self.cache, cache_path=self.cache_path,
                model='hymt-offline-v1', base_url='https://example.invalid', workers=1,
                timeout=1, attempts=1, provider='hymt', allow_source_fallback=True)

    def test_source_hash_mismatch_cannot_authorize_fallback(self):
        self.run_translation(mock.Mock(side_effect=OfflineTranslationValidationError('bad content')),
                             allow_source_fallback=True)
        self.cache['_source_fallbacks']['ko'][self.unit.key]['source_sha256'] = '0' * 64
        with self.assertRaisesRegex(b.TranslationError, 'Missing ko'):
            b.translated_text(self.source, 'html:text:p', 'ko', self.cache)

    def test_js_fallback_requires_exact_render_before_any_language_bypass(self):
        source = 'const label = "中文报告增长 12%";'
        units = {}
        b.collect_javascript_units(source, 'app.js', units)
        self.units = units
        self.run_translation(mock.Mock(side_effect=OfflineTranslationValidationError('bad content')),
                             allow_source_fallback=True)
        for locale in b.LOCALES:
            expected = b.render_localized_javascript(source, 'app.js', locale, self.cache)
            b.validate_localized_javascript_residuals(source, expected, 'app.js', locale, self.cache)
            for mutation in ('한국어 中文报告变更 25%', '한국어 25%', '日本語 25%'):
                with self.subTest(locale=locale, mutation=mutation), self.assertRaises(b.TranslationError):
                    b.validate_localized_javascript_residuals(source, 'const label = "' + mutation + '";',
                                                             'app.js', locale, self.cache)


class SourceFallbackBuildTests(unittest.TestCase):
    def test_budget_exhaustion_still_renders_a_complete_release(self):
        import test_build_portal_locales as fixtures
        from portal_locale_manifest import validate_translation_resolution
        fixture = fixtures.PortalLocaleBuildTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        before = fixtures.body_bytes(fixture.site / 'index.html')
        clock = [0]
        def translate(source, locale):
            clock[0] = 2
            return valid_translation(source, locale)
        with mock.patch('offline_translation.OfflineTranslator') as factory, \
             mock.patch.object(b.time, 'monotonic', side_effect=lambda: clock[0]):
            factory.return_value.translate.side_effect = translate
            manifest = fixture._build(None, provider='hymt', allow_source_fallback=True,
                                      offline_time_budget_seconds=1)
            self.assertEqual(factory.return_value.translate.call_count, 1)
        validate_translation_resolution(manifest, b.LOCALES)
        self.assertEqual(fixtures.body_bytes(fixture.site / 'index.html'), before)
        for locale in b.LOCALES:
            self.assertTrue((fixture.site / locale / 'index.html').is_file())
            self.assertGreater(manifest['source_fallbacks']['counts'][locale], 0)
            self.assertEqual(manifest['resolved_coverage'][locale], 1)
        self.assertEqual({row['reason'] for rows in manifest['source_fallbacks']['units'].values()
                          for row in rows.values()}, {'translation_time_budget'})
        cache = json.loads(gzip.decompress(fixture.cache.read_bytes()))
        self.assertNotIn('_source_fallbacks', cache)

    def test_real_render_keeps_js_source_and_manifest_counts_are_honest(self):
        import test_build_portal_locales as fixtures
        from portal_locale_manifest import validate_translation_resolution
        fixture = fixtures.PortalLocaleBuildTests()
        fixture.setUp()
        self.addCleanup(fixture.tearDown)
        label = '搜索报告'
        def translate(source, locale):
            if source == label:
                raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed: financial_quantity_changed_missing_or_added')
            return valid_translation(source, locale)
        with mock.patch('offline_translation.OfflineTranslator') as factory:
            factory.return_value.translate.side_effect = translate
            manifest = fixture._build(None, provider='hymt', allow_source_fallback=True)
        validate_translation_resolution(manifest, b.LOCALES)
        for locale in b.LOCALES:
            self.assertIn('const label = "搜索报告"', (fixture.site / locale / 'assets/app.js').read_text())
            self.assertEqual(manifest['source_fallbacks']['counts'][locale], 1)
            self.assertLess(manifest['coverage'][locale], 1)
            self.assertEqual(manifest['resolved_coverage'][locale], 1)
        cache = json.loads(gzip.decompress(fixture.cache.read_bytes()))
        self.assertNotIn('_source_fallbacks', cache)
        source_js = (fixture.site / 'assets/app.js').read_text()
        localized_js = (fixture.site / 'ko/assets/app.js').read_text()
        cache['_source_fallbacks'] = manifest['source_fallbacks']['units']
        with self.assertRaises(b.TranslationError):
            b.validate_localized_javascript_residuals(source_js, localized_js.replace(label, '搜索99报告'),
                                                     'app.js', 'ko', cache)


if __name__ == '__main__':
    unittest.main()
