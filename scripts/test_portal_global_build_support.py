"""Regressions for exact normalization caching and protected link spacing."""
import tempfile
import unittest
from types import SimpleNamespace
from unittest import mock
import hymt_offline_translation as h
from portal_global_build_support import cache_metadata_normalization

class GlobalBuildSupportTests(unittest.TestCase):
    def test_bounded_cache_preserves_normalization_and_does_not_cache_body(self):
        fn=mock.Mock(side_effect=lambda s: s.casefold())
        builder=SimpleNamespace(normalize_search_text=fn)
        cached=cache_metadata_normalization(builder)
        self.assertEqual(builder.normalize_search_text('ABC'),'abc')
        self.assertEqual(builder.normalize_search_text('ABC'),'abc')
        self.assertEqual(fn.call_count,1)
        builder.normalize_search_text('X'*1001);builder.normalize_search_text('X'*1001)
        self.assertEqual(fn.call_count,3)
        self.assertEqual(cached.cache_info().maxsize,32768)

    def test_spaces_in_prose_not_in_destinations(self):
        text='研究__KC_PH_000__：[报告](__HYMTPH_0000__)。'
        value=h._space_protected_tokens(text,markdown=True)
        self.assertIn('研究 __KC_PH_000__ ',value)
        self.assertIn('](__HYMTPH_0000__)',value)

    def test_exact_link_whitespace_repair_keeps_valid_url_and_cached_form(self):
        source='阅读[报告](https://example.org/r.pdf)。'
        engine=SimpleNamespace(translate=mock.Mock(return_value='Read [Report]( __HYMTPH_0000__ ).'))
        with tempfile.TemporaryDirectory() as directory:
            translator=h.OfflineTranslator(cache_dir=directory,engine_factory=lambda *_:engine)
            self.assertEqual(translator.translate(source,'en','zh'),'Read [Report](https://example.org/r.pdf).')
            self.assertEqual(translator.translate(source,'en','zh'),'Read [Report](https://example.org/r.pdf).')
            self.assertEqual(engine.translate.call_count,1)
            self.assertIn('](__HYMTPH_0000__)',engine.translate.call_args.args[0])

    def test_repairs_cannot_invent_missing_destination_or_accept_extra_content(self):
        source='报告：[Report](__HYMTPH_0000__)。'
        for bad in ('Read [Report](other __HYMTPH_0000__ ).',
                    'Read [Report] __HYMTPH_0000__.',
                    'Read [Report]( __HYMTPH_0001__ ).',
                    'Read [Report]( __HYMTPH_0000__ ). [Again]( __HYMTPH_0000__ ).'):
            with self.subTest(bad=bad), self.assertRaises(h.OfflineTranslationValidationError):
                h.validate_result(source,h._restore_protected_link_spacing(source,bad),'zh','en')

    def test_source_without_link_keeps_token_spacing_and_rejects_added_link(self):
        source='阅读__HYMTPH_0000__。'
        value='Read [Report]( __HYMTPH_0000__ ).'
        self.assertEqual(h._restore_protected_link_spacing(source,value),value)
        with self.assertRaises(h.OfflineTranslationValidationError):h.validate_result(source,value,'zh','en')

if __name__=='__main__':unittest.main()
