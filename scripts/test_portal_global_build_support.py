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

class NativePromptTests(unittest.TestCase):
    def test_source_owned_destination_allows_only_spacing_after_label(self):
        source='报告：[Report](__HYMTPH_0000__)。'
        value='Translated [Report] (__HYMTPH_0000__).'
        result=h._restore_protected_link_spacing(source,value)
        self.assertEqual(result,'Translated [Report](__HYMTPH_0000__).')
        h.validate_result(source,result,'zh','en')
        damaged='Translated [Report] garbage (__HYMTPH_0000__).'
        with self.assertRaises(h.OfflineTranslationValidationError):
            h.validate_result(source,h._restore_protected_link_spacing(source,damaged),'zh','en')

    def test_native_prose_prompt_is_not_a_sample_override(self):
        for target,name in [('mr','马拉地语'),('bo','藏语')]:
            with self.subTest(target=target):
                engine=object.__new__(h._HyMTEngine);engine.port=1
                reply={'choices':[{'finish_reason':'stop','message':{'content':'mock'}}]}
                with mock.patch.object(h,'request_json',return_value=reply) as request:
                    engine.translate('全新的文本与__KC_PH_000__。','zh',target)
                text=request.call_args.args[2]['messages'][0]['content']
                self.assertIn(name,text)
                self.assertTrue(text.endswith('\n\n全新的文本与__KC_PH_000__。'))
                self.assertNotIn('Translate the following',text)

class HeldLocaleSafetyTests(unittest.TestCase):
    def test_held_scripts_stay_registered_but_cannot_be_prepared_or_uploaded(self):
        import portal_language_registry as r
        import portal_global_r2 as store
        self.assertEqual(set(r.HELD_LOCALES),{'kk','mn'})
        self.assertEqual(len(r.selected_locales('all')),37)
        self.assertEqual(len(r.preparation_locales('ready')),35)
        self.assertEqual(len(r.preparation_locales()),32)
        for code in r.HELD_LOCALES:
            with self.subTest(code=code):
                self.assertIn(code,r.selected_locales('all'))
                with self.assertRaises(ValueError):r.preparation_locales(code)
                with self.assertRaises(ValueError):store.object_key('candidate',code)
        with self.assertRaises(ValueError):r.preparation_locales('all')

class ExistingEnglishLegalTests(unittest.TestCase):
    def test_root_legal_self_reference_is_not_a_generated_english_mirror(self):
        import verify_portal_chinese_parity as p
        html=b'<html lang="en"><head><link rel="canonical" href="https://portal.example.invalid/privacy.html"><link rel="alternate" hreflang="en" href="https://portal.example.invalid/privacy.html"><link rel="alternate" hreflang="x-default" href="https://portal.example.invalid/privacy.html"></head><body>Privacy policy</body></html>'
        previous=p.LOCALES
        try:
            p.configure_locale_targets(('en',))
            before=p._validate_snapshot_head(html,relative='privacy.html')
            self.assertEqual(before['alternates']['en'],before['canonical'])
            for bad,relative in ((html.replace(b'/privacy.html',b'/en/privacy.html'),'privacy.html'),(html,'other.html')):
                with self.assertRaises(p.ParityError):p._validate_snapshot_head(bad,relative=relative)
        finally:p.configure_locale_targets(previous)

if __name__=='__main__':unittest.main()
