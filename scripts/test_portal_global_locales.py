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

class GlobalSafetyFollowupTests(unittest.TestCase):
    def test_traditional_conversion_is_exact_and_never_loads_model(self):
        import tempfile
        from portal_chinese_script import to_traditional
        source = '阅读报告：收入增长12.5%，风险降低。'
        with tempfile.TemporaryDirectory() as directory:
            translator = o.OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: self.fail('Conversion needs no model'))
            result = translator.translate(source, 'zh-Hant', 'zh')
        self.assertEqual(result, to_traditional(source))
        self.assertIn('閱讀報告', result)
        self.assertIn('12.5%', result)
        _, unit = b.unit_for_text('研究方法', 'html:text:p')
        b.validate_translation_quality('zh-Hant', unit, '研究方法')
        _, unit = b.unit_for_text('报告分析半导体需求', 'html:text:p')
        with self.assertRaises(b.TranslationQualityError):
            b.validate_translation_quality('zh-Hant', unit, '报告解释了半导体需求')

    def test_generic_url_mask_does_not_swallow_markdown_delimiters(self):
        source = '阅读研究结论与来源：[报告](https://example.org/report.pdf)。'
        protected, unit = b.unit_for_text(source, 'html:text:p')
        self.assertIn('](__KC_PH_', unit.source)
        self.assertTrue(unit.source.endswith('__)。'))
        self.assertEqual(protected.restore(unit.source), source)

    def test_unknown_script_cannot_be_an_english_identity_copy(self):
        import tempfile
        calls = []
        class Engine:
            def translate(self, text, source, target):
                calls.append(text)
                return 'Research report'
        with tempfile.TemporaryDirectory() as directory:
            translator = o.OfflineTranslator(cache_dir=directory, engine_factory=lambda *_: Engine())
            self.assertEqual(translator.translate('Отчет исследования', 'en'), 'Research report')
            self.assertEqual(len(calls), 1)
            self.assertEqual(translator.translate('Research report', 'en'), 'Research report')
            self.assertEqual(len(calls), 1)

    def test_expanded_source_fallback_is_rejected(self):
        from portal_locale_manifest import validate_translation_resolution, LocaleManifestError
        manifest = {'coverage': {'fr': 0.0}, 'source_unit_count': 1, 'prompt_version': 'test',
                    'translation_entry_count': {'fr': 0}, 'resolved_entry_count': {'fr': 1},
                    'resolved_coverage': {'fr': 1.0},
                    'source_fallbacks': {'schema_version': 1, 'counts': {'fr': 1}, 'units': {'fr': {'bad': {}}}}}
        with self.assertRaisesRegex(LocaleManifestError, 'source fallback forbidden'):
            validate_translation_resolution(manifest, ['fr'])

    def test_shadow_and_resume_reject_unknown_or_alias_locale_configuration(self):
        import audit_portal_shadow_preview as audit
        self.assertEqual(audit.locale_directions({'locales': ['fr','zh-Hant','he']}),
                         {'fr':'ltr','zh-Hant':'ltr','he':'rtl'})
        for codes in (['xx'], ['zh-hant'], ['fr','fr']):
            with self.assertRaises(audit.AuditError): audit.locale_directions({'locales':codes})

class GlobalPreparationTests(unittest.TestCase):
    def test_complete_candidate_keeps_chinese_bytes_and_does_not_claim_live(self):
        import prepare_portal_global_locales as prep
        case = fixtures.PortalLocaleBuildTests(); case.setUp(); self.addCleanup(case.tearDown)
        for name in ('sitemap-baidu.xml','sitemap-sogou.xml'):
            (case.site/name).write_bytes((case.site/'sitemap-pages.xml').read_bytes())
        (case.site/'data/hot_reports.json').write_bytes(case.hot_report_index.read_bytes())
        before = {p.relative_to(case.site).as_posix():p.read_bytes() for p in case.site.rglob('*') if p.is_file()}
        with mock.patch('offline_translation.OfflineTranslator',FixtureTranslator), mock.patch('requests.sessions.Session.request',side_effect=AssertionError('Paid request')):
            result = prep.prepare(case.site,case.site.parent/'candidate',case.cache,'fr',SITE_URL,'2026-09-23',60)
        self.assertTrue(result['candidate_complete'])
        self.assertFalse(result['production_ready'])
        self.assertEqual(result['paid_provider_requests'],0)
        for name, body in before.items(): self.assertEqual((case.site/name).read_bytes(),body)
        self.assertEqual(tuple(b.LOCALES),r.DEFAULT_LOCALES)

    def test_candidate_budget_and_source_boundaries_fail_before_translation(self):
        import tempfile
        import prepare_portal_global_locales as prep
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory); source = root/'source'; source.mkdir()
            (source/'index.html').write_text('<html lang="zh-Hans"><body>公开研究</body></html>')
            with mock.patch('offline_translation.OfflineTranslator',side_effect=AssertionError('Must validate first')):
                with self.assertRaises(ValueError):
                    prep.prepare(source,source/'nested',root/'cache','fr',SITE_URL,'2026-09-23',30)
                with self.assertRaises(ValueError):
                    prep.prepare(source,root/'output',root/'cache','fr',SITE_URL,'2026-09-23',10000)
            self.assertTrue((source/'index.html').is_file())

    def test_scheduled_warming_uses_only_standard_public_cpu_and_bounded_cache(self):
        text = Path(__file__).resolve().parents[1].joinpath('.github/workflows/portal-global-locale-prepare.yml').read_text()
        self.assertIn('github.event.repository.private == false',text)
        self.assertIn('max-parallel: 2',text)
        self.assertIn('8 * 1024 * 1024',text)
        self.assertNotIn('secrets.',text)
        self.assertNotIn('self-hosted',text)
        self.assertNotIn('--allow-source-fallback',text)
        self.assertNotIn('wrangler',text)
        self.assertNotIn('createWorkflowDispatch',text)

    def test_hebrew_grammatical_hyphen_is_not_a_negative_rate(self):
        from financial_quantity_integrity import quantity_issues
        self.assertEqual(quantity_issues('Growth was 12.5%.', 'הצמיחה הייתה ב-12.5%.'), [])
        self.assertTrue(quantity_issues('Growth was -12.5%.', 'הצמיחה הייתה ב-12.5%.'))
        self.assertEqual(quantity_issues('Growth was -12.5%.', 'הצמיחה הייתה -12.5%.'), [])

    def test_low_resource_prompt_and_memo_identity_keep_explicit_scripts(self):
        engine = object.__new__(o._HyMTEngine); engine.port=1
        response={'choices':[{'finish_reason':'stop','message':{'content':'研究嘅方法'}}]}
        with mock.patch.object(o,'request_json',return_value=response) as request:
            engine.translate('研究的方法','zh','yue')
        self.assertIn('香港粵語',request.call_args.args[2]['messages'][0]['content'])
        with self.assertRaises(o.OfflineTranslationValidationError):
            o.validate_result('研究方法','この報告書方法','zh','yue')

    def test_traditional_financial_quantities_preserve_magnitude_and_currency(self):
        from financial_quantity_integrity import quantity_issues
        self.assertEqual(quantity_issues('收入为1.2亿美元和3亿元人民币。', '收入為1.2億美元和3億元人民幣。'),[])
        self.assertTrue(quantity_issues('收入为1.2亿美元。','收入為1.2萬美元。'))

if __name__=='__main__': unittest.main()
