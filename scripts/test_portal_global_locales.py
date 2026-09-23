#!/usr/bin/env python3
"""Deterministic wiring tests, not claims about linguistic quality."""
import itertools
import json
from pathlib import Path
import unittest
from unittest import mock
import portal_language_registry as r
import build_portal_locales as b
import hymt_offline_translation as o
import test_build_portal_locales as fixtures
from test_build_portal_locales import alternate_links, SITE_URL

SCRIPTS = {'latin':'Synthetic research explanation','han':'測試譯文與研究說明','hangul':'번역 연구 문서','japanese':'研究の翻訳文','arabic':'وثيقة بحث مترجمة','cyrillic':'Перевод исследования','thai':'เอกสารการวิจัย','devanagari':'अनुवाद अनुसंधान','khmer':'ឯកសារស្រាវជ្រាវ','myanmar':'သုတေသနစာတမ်း','gujarati':'સંશોધન અનુવાદ','telugu':'పరిశోధన అనువాదం','hebrew':'תרגום מחקר','bengali':'গবেষণা অনুবাদ','tamil':'ஆராய்ச்சி மொழிபெயர்ப்பு','tibetan':'ཞིབ་འཇུག་ཡིག་ཆ'}
class FixtureTranslator:
    def translate(self, source, target, *args, **kwargs):
        return SCRIPTS[r.LANGUAGES[target].script]+' '+' '.join(b.PLACEHOLDER_RE.findall(source))

class GlobalLocaleTests(unittest.TestCase):
    def fixture(self):
        case=fixtures.PortalLocaleBuildTests('test_detail_source_contract_fails_before_translation_and_chinese_mutation')
        case.setUp(); self.addCleanup(case.tearDown)
        return case

    def test_supported_set_default_and_directions(self):
        self.assertEqual(len(r.LANGUAGES),38)
        self.assertEqual(len(r.selected_locales('all')),37)
        self.assertEqual(len(r.selected_locales('new')),34)
        self.assertEqual(r.selected_locales(),('ko','ja','ar'))
        self.assertEqual(tuple(b.LOCALES),r.DEFAULT_LOCALES)
        self.assertEqual({code for code,row in r.LANGUAGES.items() if row.direction=='rtl'},{'ar','fa','ur','he','ug'})

    def test_canonical_aliases_and_fail_closed_selection(self):
        for source,target in [('zh-Hant','zh-Hant'),('zh_TW','zh-Hant'),('zh-Hant-HK','zh-Hant'),('zh-Hans-CN','zh'),('fil','tl'),('fr-CA','fr'),('yue-HK','yue')]:
            self.assertEqual(o.normalize_language(source),target)
        for value in ('fr,fr','zh','en,xx',''):
            with self.assertRaises(ValueError): r.selected_locales(value)
        with self.assertRaises(o.OfflineTranslationError): o.normalize_language('xx')

    def test_manifest_targets_not_aliases(self):
        self.assertEqual(r.manifest_locales({}),r.DEFAULT_LOCALES)
        self.assertEqual(r.manifest_locales({'locales':['en','zh-Hant','he']}),('en','zh-Hant','he'))
        for value in (['zh-hant'],['en','en'],[],['zh'],['xx']):
            with self.assertRaises(ValueError): r.manifest_locales({'locales':value})

    def test_selection_restores_on_error(self):
        with self.assertRaises(RuntimeError):
            with b.locale_selection('en,fr'):
                self.assertEqual(tuple(b.LOCALES),('en','fr'))
                raise RuntimeError('test')
        self.assertEqual(tuple(b.LOCALES),r.DEFAULT_LOCALES)

    def test_all_model_scripts_preserve_placeholders(self):
        for code in r.MIRROR_CODES:
            with self.subTest(locale=code):
                translated=SCRIPTS[r.LANGUAGES[code].script]+' __KC_PH_000__'
                o.validate_result('报告 __KC_PH_000__',translated,'zh',code,markdown=False)
                with self.assertRaises(o.OfflineTranslationValidationError):
                    o.validate_result('报告 __KC_PH_000__',translated.replace('__KC_PH_000__',''),'zh',code,markdown=False)

    def test_runtime_lists_only_selected_languages(self):
        self.assertEqual(len(r.runtime_languages(r.MIRROR_CODES)),38)
        self.assertEqual(set(r.runtime_languages(['fr'])),{'zh-Hans','fr'})
        for code in r.MIRROR_CODES:
            self.assertEqual(r.runtime_languages([code])[code]['direction'],r.LANGUAGES[code].direction)

    def test_actions_only_model_boundary(self):
        with mock.patch.dict('os.environ',{'GITHUB_ACTIONS':'false','RUNNER_OS':'Linux'}):
            with self.assertRaisesRegex(RuntimeError,'Linux GitHub Actions'): o.require_actions()
        self.assertNotIn('api.deepseek.com',Path(o.__file__).read_text())
        self.assertNotIn('api.deepl.com',Path(o.__file__).read_text())

    def test_all_mirrors_have_complete_metadata_discovery_and_protected_root(self):
        case=self.fixture()
        before={name:(case.site/name).read_bytes() for name in ('feed.xml','llms.txt','llms-full.txt','assets/app.js')}
        with mock.patch('offline_translation.OfflineTranslator',FixtureTranslator),mock.patch('requests.sessions.Session.request',side_effect=AssertionError('Paid API')):
            result=case._build(None,locales='all',provider='hymt',workers=1)
        self.assertEqual(result['locales'],list(r.MIRROR_CODES))
        self.assertEqual(result['coverage'],{code:1.0 for code in r.MIRROR_CODES})
        for code in r.MIRROR_CODES:
            with self.subTest(locale=code):
                html=(case.site/code/'index.html').read_text()
                self.assertIn(f'lang="{code}"',html)
                self.assertIn(f'dir="{r.LANGUAGES[code].direction}"',html)
                self.assertIn(f'<link rel="canonical" href="{SITE_URL}/{code}/"',html)
                links=alternate_links(html)
                self.assertEqual(set(links),{'zh-Hans','x-default',*r.MIRROR_CODES})
                self.assertEqual(links[code],f'{SITE_URL}/{code}/')
                self.assertTrue((case.site/f'sitemap-{code}.xml').is_file())
                self.assertNotIn('PRIVATE-OBJECT-KEY-MUST-NOT-LEAVE',html)
        for name,data in before.items(): self.assertEqual((case.site/name).read_bytes(),data)
        self.assertEqual(tuple(b.LOCALES),r.DEFAULT_LOCALES)
        runtime=(case.site/'assets/locale-runtime.js').read_text()
        config=json.loads(runtime.split('window.PortalLocaleConfig = ',1)[1].split(';\n',1)[0])
        self.assertEqual(len(config['languages']),38)
        self.assertEqual(set(config['copy']),set(r.EXPANSION_CODES))

    def test_single_locale_does_not_advertise_unbuilt_siblings(self):
        case=self.fixture()
        with mock.patch('offline_translation.OfflineTranslator',FixtureTranslator):
            result=case._build(None,locales='fr',provider='hymt')
        self.assertEqual(result['locales'],['fr'])
        self.assertEqual(set(alternate_links((case.site/'fr/index.html').read_text())),{'zh-Hans','x-default','fr'})
        self.assertFalse((case.site/'en').exists())
        self.assertFalse((case.site/'sitemap-ko.xml').exists())

    def test_expansion_refuses_paid_and_source_fallback_before_writes(self):
        for opts in ({'provider':'deepseek'},{'provider':'hymt','allow_source_fallback':True}):
            case=self.fixture(); before=(case.site/'index.html').read_bytes()
            with mock.patch('requests.sessions.Session.request',side_effect=AssertionError('Paid API')),mock.patch('offline_translation.OfflineTranslator',side_effect=AssertionError('Model loaded')):
                with self.assertRaises(b.TranslationError): case._build(None,locales='fr',**opts)
            self.assertEqual((case.site/'index.html').read_bytes(),before)
            self.assertFalse((case.site/'fr').exists())

    def test_budget_checkpoint_cannot_publish(self):
        case=self.fixture(); before=(case.site/'index.html').read_bytes()
        with mock.patch('offline_translation.OfflineTranslator',FixtureTranslator), mock.patch.object(b.time,'monotonic',side_effect=itertools.count(0,10)):
            result=case._build(None,locales='fr',provider='hymt',offline_time_budget_seconds=1,checkpoint_on_budget=True)
        self.assertFalse(result['ready']); self.assertTrue(case.cache.is_file())
        self.assertFalse((case.site/'fr').exists()); self.assertFalse((case.site/'sitemap-fr.xml').exists())
        self.assertEqual(before,(case.site/'index.html').read_bytes())

    def test_javascript_paths_expand_once(self):
        source='const codes = ["ko", "ja", "ar"]; const path = /^(ko|ja|ar|en|zh-Hant)\\//;'
        updated=b.specialize_locale_javascript(source,'fr')
        self.assertEqual(updated.count(r.LOCALE_PATTERN),1)
        self.assertIn('zh-hant',updated)
        self.assertEqual(b.specialize_locale_javascript(source,'ja'),source)

if __name__=='__main__': unittest.main()
