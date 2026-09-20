#!/usr/bin/env python3
"""Offline boundary, paid-cache migration and partial checkpoint regressions."""
import gzip
import json
import os
from pathlib import Path
import tempfile
import unittest
from unittest import mock

import build_portal_locales as b


class OfflineLocaleTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.path = Path(self.temp.name) / 'cache.json.gz'
        self.unit = b.unit_for_text('阅读最新报告', 'html:text:p')[1]

    def test_import_existing_translations_without_retranslating(self):
        cache = b.empty_cache()
        for language in b.LOCALES:
            cache['locales'][language][self.unit.key] = b._translation_cache_row(
                self.unit, {'ko': '최신 보고서 읽기', 'ja': '最新レポートを読む', 'ar': 'اقرأ أحدث تقرير'}[language])
        b.write_cache(self.path, cache)
        imported = b.load_cache(self.path, 'hymt-offline-v1', provider='hymt')
        self.assertEqual(imported['provider'], 'hymt')
        with mock.patch('offline_translation.OfflineTranslator', side_effect=AssertionError('Cache should avoid model load')):
            missing = self.run_translation(imported)
        self.assertEqual(sum(missing.values()), 0)
        restored = b.load_cache(self.path, 'hymt-offline-v1', provider='hymt')
        self.assertEqual(restored['locales']['ko'][self.unit.key]['provider'], 'legacy-cache')

    def test_changed_namespace_is_not_imported(self):
        cache = b.empty_cache('unknown-model')
        cache['locales']['ko'][self.unit.key] = b._translation_cache_row(self.unit, '최신 보고서 읽기')
        b.write_cache(self.path, cache)
        loaded = b.load_cache(self.path, 'hymt-offline-v1', provider='hymt')
        self.assertFalse(loaded['locales']['ko'])
        cache = b.empty_cache()
        cache['prompt_version'] = 'old-prompt'
        b.write_cache(self.path, cache)
        self.assertEqual(b.load_cache(self.path, 'hymt-offline-v1', provider='hymt')['prompt_version'], b.PROMPT_VERSION)

    def test_retired_paid_commands_cannot_call_the_provider(self):
        import preflight_portal_locale_translation
        import probe_portal_locale_protocol
        import preflight_deepl_locale_repair
        import run_portal_locale_backfill
        with mock.patch('requests.sessions.Session.request', side_effect=AssertionError('Paid request')):
            for module in (preflight_portal_locale_translation, probe_portal_locale_protocol,
                           preflight_deepl_locale_repair, run_portal_locale_backfill):
                self.assertEqual(module.main(), 2)

    def test_model_upgrade_keeps_paid_rows_but_invalidates_old_offline_rows(self):
        cache = b.empty_cache('old-offline-model', provider='hymt')
        paid = {**b._translation_cache_row(self.unit, '최신 보고서 읽기'),
                'provider': 'legacy-cache', 'source_cache_provider': 'deepseek',
                'model': b.DEFAULT_DEEPSEEK_MODEL}
        cache['locales']['ko'][self.unit.key] = paid
        cache['locales']['ar'][self.unit.key] = {**b._translation_cache_row(self.unit, 'اقرأ أحدث تقرير'),
                                               'provider': 'hymt', 'model': 'old-offline-model'}
        b.write_cache(self.path, cache)
        loaded = b.load_cache(self.path, 'new-offline-model', provider='hymt')
        self.assertIn(self.unit.key, loaded['locales']['ko'])
        self.assertFalse(loaded['locales']['ar'])

    def run_translation(self, cache):
        return b.translate_missing_units({self.unit.key: self.unit}, cache, cache_path=self.path,
            model='hymt-offline-v1', base_url='https://example.invalid', workers=32,
            timeout=1, attempts=3, provider='hymt')

    def test_offline_failure_keeps_other_languages_and_never_repairs_via_api(self):
        def translate(source, language):
            return {'ko': '최신 보고서 읽기', 'ja': '', 'ar': 'اقرأ أحدث تقرير'}[language]
        with mock.patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'unused', 'DEEPL_API_KEY': 'unused'}), \
             mock.patch('offline_translation.OfflineTranslator') as factory, \
             mock.patch.object(b, 'deepseek_translate_batch', side_effect=AssertionError('Paid fallback')):
            factory.return_value.translate.side_effect = translate
            with self.assertRaisesRegex(b.TranslationError, 'unresolved'):
                self.run_translation(b.empty_cache('hymt-offline-v1', provider='hymt'))
        saved = json.loads(gzip.decompress(self.path.read_bytes()))
        self.assertIn(self.unit.key, saved['locales']['ko'])
        self.assertIn(self.unit.key, saved['locales']['ar'])
        self.assertNotIn(self.unit.key, saved['locales']['ja'])
        self.assertEqual(saved['locales']['ko'][self.unit.key]['provider'], 'hymt')

    def test_missing_model_stops_instead_of_spending_or_reporting_success(self):
        from offline_translation import OfflineTranslationError
        with mock.patch('offline_translation.OfflineTranslator') as factory, \
             mock.patch.object(b, 'deepseek_translate_batch', side_effect=AssertionError('Paid fallback')):
            factory.return_value.translate.side_effect = OfflineTranslationError('Model not installed')
            with self.assertRaisesRegex(b.TranslationError, 'not installed'):
                self.run_translation(b.empty_cache('hymt-offline-v1', provider='hymt'))
            self.assertEqual(factory.return_value.translate.call_count, 1)
        self.assertTrue(self.path.exists())


class PercentPlaceholderRestorationTests(unittest.TestCase):
    def test_added_percent_is_removed_only_for_known_percent_value(self):
        protected = b.protect_text('收入增长12.5%，利润率为8%。')
        translated = '売上は__KC_PH_000__%増加し、利益率は__KC_PH_001__％でした。'
        self.assertEqual(protected.restore(translated), '売上は12.5%増加し、利益率は8%でした。')

    def test_plain_number_with_model_percent_is_not_silently_rewritten(self):
        protected = b.protect_text('数值为8。')
        self.assertEqual(protected.restore('__KC_PH_000__%'), '8%')

    def test_literal_source_double_percent_is_preserved(self):
        protected = b.protect_text('显示12.5%%。')
        self.assertEqual(protected.restore('__KC_PH_000__%'), '12.5%%')
        self.assertEqual(protected.restore('__KC_PH_000__%%'), '12.5%%')

    def test_unrelated_percent_and_nonadjacent_symbols_are_not_rewritten(self):
        protected = b.protect_text('增长12.5%。')
        translated = '__KC_PH_000__相当; 另一个真实符号%%'
        self.assertEqual(protected.restore(translated), '12.5%相当; 另一个真实符号%%')


if __name__ == '__main__':
    unittest.main()
