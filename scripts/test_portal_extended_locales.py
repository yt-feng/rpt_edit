#!/usr/bin/env python3
"""Synthetic contract tests only; these are not real-model language evaluations."""
from __future__ import annotations
import copy
import json
from pathlib import Path
import re
import tempfile
import time
import unittest
from unittest import mock
import xml.etree.ElementTree as ET

from compare_hymt_translation import LANGUAGES, SCRIPT_PATTERNS
from hymt_offline_translation import normalize_language, OfflineTranslationError, OfflineTranslationValidationError
from portal_extended_locales import *
from build_portal_extended_locales import (
    build, Memo, MODEL_ID, protect_numeric_claims, restore_numeric_claims, validate_text,
)
from assemble_portal_extended_locales import assemble, verified_candidate, head_alternates
from collect_portal_extended_sources import select_urls, read_public

ROOT = Path(__file__).resolve().parent.parent
HOME = ORIGIN + '/'
BLOG = ORIGIN + '/blog/20260922-test.html'


def html(url=HOME, *, body='<h1>Research library</h1><p>Independent market research and source references.</p>', extra=''):
    return f'''<!doctype html><html lang="en"><head><title>Library</title><meta name="description" content="Public financial research summaries."><link rel="canonical" href="{url}">{extra}</head><body><nav>not corpus</nav><main>{body}</main><footer>not corpus</footer></body></html>'''.encode()


def corpus():
    return make_corpus([
        document_from_html(HOME, html(body='<h1>Research library</h1><p>Independent market research.</p><p><a href="/blog/20260922-test.html">Research note</a></p>')),
        document_from_html(BLOG, html(BLOG, body='<h1>Research note</h1><p>Source based analysis for readers.</p>', extra='<script type="application/ld+json">'+json.dumps({'@type':'Article','url':BLOG,'datePublished':'2026-09-22','dateModified':'2026-09-22'})+'</script>')),
    ])

class FakeTranslator:
    """Used only to exercise plumbing; no linguistic quality assertion."""
    def __init__(self, fail=None): self.calls = 0; self.fail = fail
    def translate(self, text, target, source=None, *, markdown=True):
        self.calls += 1
        if self.fail and self.fail in text: raise RuntimeError('synthetic rejected response')
        if target == 'en': return text
        return 'Texte traduit de référence.'


class RetryQuantityTranslator(FakeTranslator):
    def __init__(self):
        super().__init__()
        self.discard_calls = 0

    def translate(self, text, target, source=None, *, markdown=True):
        self.calls += 1
        if self.calls == 1:
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed')
        return text if target == 'en' else 'Texte traduit de référence.'

    def discard_translation(self, text, target, source=None, *, markdown=True):
        self.discard_calls += 1


class LanguageRegistryTests(unittest.TestCase):
    def test_38_entries_and_34_additions(self):
        self.assertEqual(len(LANGUAGES), 38); self.assertEqual(len(ADDITIONAL), 34)
        self.assertEqual(set(SCRIPT_PATTERNS), set(LANGUAGES))
        self.assertEqual(set(NATIVE), set(LANGUAGES))

    def test_all_supported_matrix(self): self.assertEqual(select_locales('all-supported'), ADDITIONAL)
    def test_subset_preserves_order(self): self.assertEqual(select_locales('fr,en,zh-Hant'), ('fr','en','zh-Hant'))
    def test_unknown_codes_fail(self):
        for value in ['xx', '../fr', 'en,fr,en', '', 'en,', 'ko', 'ar', 'zh', 'ALL']:
            with self.subTest(value=value), self.assertRaises(ExpansionError): select_locales(value)
    def test_script_variant_is_not_collapsed(self):
        for value in ['zh-Hant','zh_Hant','zh-TW','zh-HK','zh-Hant-TW']:
            self.assertEqual(normalize_language(value), 'zh-Hant')
        self.assertEqual(normalize_language('zh-Hans'), 'zh')
    def test_all_targets_reach_the_engine(self):
        for code in ADDITIONAL: self.assertEqual(normalize_language(code), code)
    def test_legacy_aliases(self):
        self.assertEqual(normalize_language('jp'), 'ja'); self.assertEqual(normalize_language('kr'), 'ko')
        self.assertEqual(normalize_language('en-US'), 'en'); self.assertEqual(normalize_language('fil'), 'tl')
    def test_no_unlisted_language_fallback(self):
        with self.assertRaises(OfflineTranslationError): normalize_language('xx')
    def test_rtl_scripts(self):
        for code in ['ar','fa','he','ur','ug']: self.assertEqual(direction(code),'rtl')
        for code in ['en','zh-Hant','hi','ru']: self.assertEqual(direction(code),'ltr')
    def test_yue_is_not_mislabeled_as_google_hreflang(self):
        self.assertNotIn('yue', HREFLANG); self.assertEqual(HREFLANG['zh-Hant'],'zh-Hant')
    def test_inventory_file_matches_engine(self):
        self.assertEqual(json.loads((ROOT/'scripts/portal_extended_language_inventory.json').read_text()), LANGUAGES)


class SourceTests(unittest.TestCase):
    def test_public_paths(self):
        for path in ['/', '/about.html','/reports/','/blog/20260922-abc.html','/reports/topics/ai/']:
            self.assertEqual(public_url(path), ORIGIN+path)
    def test_private_and_external_paths_rejected(self):
        for path in ['/api/report?id=a','/data/catalog.json','https://evil.example/reports/a.html','http://kcdesk.com/reports/a.html',ORIGIN.replace('://', '://u:p@') + '/','/report.html?id=a','/reports/%2e%2e/api/x','/reports/a.html#password=x','/ko/reports/a.html','/blog/bbg-20260922-deadbeef.html']:
            with self.subTest(path=path), self.assertRaises(ExpansionError): public_url(path)
    def test_output_paths(self):
        self.assertEqual(file_for_url(HOME),Path('index.html'))
        self.assertEqual(file_for_url(ORIGIN+'/reports/'),Path('reports/index.html'))
    def test_canonical_mismatch_rejected(self):
        with self.assertRaises(ExpansionError): document_from_html(HOME,html(BLOG))
    def test_challenge_and_noindex_rejected(self):
        for extra in ['<script src="/challenge-platform/x"></script>', '<meta name="robots" content="noindex,follow">']:
            with self.assertRaises(ExpansionError): document_from_html(HOME,html(extra=extra))
    def test_forms_scripts_hidden_and_nav_not_extracted(self):
        document=document_from_html(HOME,html(body='<h1>Library</h1><p>Public prose.</p><form><p>account-secret</p></form><script>private state</script><p hidden>hidden-secret</p>'))
        self.assertEqual([b['text'] for b in document['blocks']],['Library','Public prose.'])
        self.assertNotIn('not corpus',json.dumps(document['blocks']))
    def test_complete_table_rows_and_nested_emphasis(self):
        document=document_from_html(HOME,html(body='<h1>Library</h1><p>Revenue <strong>rose</strong> safely.</p><table><tr><th>Year</th><th>Revenue</th></tr><tr><td>2026</td><td>USD10m</td></tr></table>'))
        self.assertIn({'tag':'p','text':'Revenue rose safely.'},document['blocks'])
        self.assertIn({'tag':'tr','text':'2026 | USD10m'},document['blocks'])
    def test_own_dates_only(self):
        document=corpus()['documents'][1]
        self.assertEqual(document['datePublished'],'2026-09-22')
        unrelated='<script type="application/ld+json">'+json.dumps({'@type':'Article','url':BLOG,'datePublished':'2026-09-22'})+'</script>'
        self.assertEqual(document_from_html(HOME,html(extra=unrelated))['datePublished'],'')
    def test_source_digest_tampering_rejected(self):
        c=corpus();c['documents'][0]['title']='changed'
        with self.assertRaises(ExpansionError): validate_corpus(c)
    def test_corpus_digest_tampering_rejected(self):
        c=corpus();c['documents_sha256']='0'*64
        with self.assertRaises(ExpansionError): validate_corpus(c)
    def test_duplicate_documents_rejected(self):
        doc=corpus()['documents'][0]
        with self.assertRaises(ExpansionError): make_corpus([doc,doc])
    def test_sitemap_page_selection_is_bounded(self):
        urls=[HOME,ORIGIN+'/reports/',BLOG,ORIGIN+'/reports/a.html',ORIGIN+'/reports/topics/macro/']
        self.assertEqual(len(select_urls(urls,3)),3);self.assertIn(HOME,select_urls(urls,3))
        with self.assertRaises(ExpansionError): select_urls(urls,501)
    def test_source_fetch_disables_redirects_and_requires_html(self):
        response=mock.MagicMock();response.__enter__.return_value=response
        response.status_code=200;response.headers={'Content-Type':'text/html'};response.iter_content.return_value=[html()]
        session=mock.Mock();session.get.return_value=response
        self.assertEqual(read_public(session,HOME),html())
        self.assertIs(session.get.call_args.kwargs['allow_redirects'],False)
    def test_source_fetch_fails_on_redirect(self):
        response=mock.MagicMock();response.__enter__.return_value=response
        response.status_code=302;session=mock.Mock();session.get.return_value=response
        with self.assertRaises(ExpansionError): read_public(session,HOME)


class QualityTests(unittest.TestCase):
    def test_unchanged_english_is_allowed_only_for_english(self):
        validate_text('Public financial research library.','Public financial research library.','en','en')
        with self.assertRaises(ExpansionError): validate_text('Public financial research library.','Public financial research library.','fr','en')
    def test_english_echo_behind_localized_prefix_rejected(self):
        with self.assertRaises(ExpansionError): validate_text('Public financial research library.','Bonjour Public financial research library.','fr','en')
    def test_changed_quantities_rejected(self):
        for text in ['Revenue USD20m.', 'Revenue CNY10m.', 'Revenue 10.', 'Revenue USD10bn.']:
            with self.subTest(text=text),self.assertRaises(ExpansionError):validate_text('Revenue USD10m.',text,'en','en')
    def test_table_column_loss_rejected(self):
        with self.assertRaises(ExpansionError):validate_text('2026 | USD10m','2026 USD10m','en','en')
    def test_target_script_is_required(self):
        with self.assertRaises(ExpansionError):validate_text('Research findings for investors.','Translated finance document.','hi','en')
    def test_chinese_residue_rejected(self):
        with self.assertRaises(ExpansionError):validate_text('Financial analysis for investors.','Bonjour 这是一段完全没有翻译的中文研究分析材料。','fr','en')
    def test_unrestored_identifiers_rejected(self):
        with self.assertRaises(ExpansionError):validate_text('Title','Title __KC_PH_000__','en','en')
    def test_metadata_literal_does_not_invent_a_quantity(self):
        validate_text('AI','AI','en','en')
    def test_empty_translation_rejected(self):
        with self.assertRaises(ExpansionError): validate_text('Public text','','fr','en')


class BuildFixture:
    def setUp(self):
        self.tmp=tempfile.TemporaryDirectory();self.base=Path(self.tmp.name);self.c=corpus()
    def tearDown(self):self.tmp.cleanup()
    def runbuild(self,locale='en',fake=None,budget=60,output='candidate'):
        return build(self.c,locale,self.base/output,self.base/f'{locale}.json',fake or FakeTranslator(),budget_seconds=budget)


class CandidateTests(BuildFixture, unittest.TestCase):
    def test_numeric_claims_are_protected_and_restored_without_changing_source(self):
        source = '2026-09-23 revenue grew 12.5% and Q2 2026 sales reached USD 120 million.'
        masked, claims = protect_numeric_claims(source)
        self.assertNotIn('2026-09-23', masked)
        self.assertNotIn('12.5', masked)
        self.assertNotIn('120', masked)
        self.assertEqual(restore_numeric_claims(masked, claims), source)

    def test_complete_candidate_is_noindex_and_never_deployed(self):
        result=self.runbuild()
        self.assertEqual(result['status'],'complete-candidate');self.assertFalse(result['indexable'])
        self.assertEqual(result['paid_provider_requests'],0)
        self.assertEqual(result['semantic_review'],'not-performed')
        self.assertIn('content="noindex,follow"',(self.base/'candidate/en/index.html').read_text())
    def test_failure_has_no_partial_page(self):
        result=self.runbuild(fake=FakeTranslator(fail='Source based'))
        self.assertEqual(result['status'],'incomplete-candidate');self.assertEqual(result['completed_page_count'],1)
        self.assertFalse((self.base/'candidate/en/blog/20260922-test.html').exists())
        with self.assertRaises(ExpansionError):verified_candidate(self.base/'candidate',self.c)
    def test_budget_checkpoint_is_not_success(self):
        result=self.runbuild(budget=-1)
        self.assertEqual(result['status'],'incomplete-candidate');self.assertTrue(result['budget_exhausted'])
        self.assertEqual(result['completed_page_count'],0)
    def test_quantity_validation_gets_one_bounded_offline_retry(self):
        fake = RetryQuantityTranslator(); result = self.runbuild(fake=fake)
        self.assertEqual(result['status'], 'complete-candidate')
        self.assertEqual(fake.discard_calls, 1)
    def test_resume_reuses_validated_cache_without_calls(self):
        self.runbuild();fake=FakeTranslator();result=self.runbuild(fake=fake,output='second')
        self.assertEqual(result['status'],'complete-candidate');self.assertEqual(fake.calls,0)
    def test_checkpoint_model_identity_must_match(self):
        self.runbuild();path=self.base/'en.json';payload=json.loads(path.read_text());payload['model']='wrong';path.write_text(json.dumps(payload))
        fake=FakeTranslator();self.runbuild(fake=fake,output='second');self.assertGreater(fake.calls,0)
    def test_candidate_root_is_not_overwritten(self):
        self.runbuild()
        with self.assertRaises(ExpansionError):self.runbuild()
    def test_source_links_and_article_schema(self):
        self.runbuild();text=(self.base/'candidate/en/blog/20260922-test.html').read_text()
        self.assertIn('"inLanguage": "en"',text);self.assertIn('"datePublished": "2026-09-22"',text)
        self.assertIn('"isBasedOn"',text);self.assertIn(BLOG,text)
    def test_html_in_translated_text_is_escaped(self):
        doc=self.c['documents'][0]
        from build_portal_extended_locales import translate_document
        translated=translate_document(doc,Memo(self.base/'memo.json','en',FakeTranslator(),time.monotonic()+60))
        translated['blocks'][0]['text']='<img src=x onerror=alert(1)>'
        text=render_document(doc,translated,'en',{HOME})
        self.assertIn('&lt;img',text);self.assertNotIn('<img src=x',text)
    def test_unknown_link_does_not_become_a_broken_locale_link(self):
        doc=copy.deepcopy(self.c['documents'][0]);doc['links']=[{'url':ORIGIN+'/reports/missing.html','label':'Source'}]
        from build_portal_extended_locales import translate_document
        trans=translate_document(doc,Memo(self.base/'m.json','en',FakeTranslator(),time.monotonic()+60))
        text=render_document(doc,trans,'en',{HOME})
        self.assertIn(ORIGIN+'/reports/missing.html',text);self.assertNotIn(ORIGIN+'/en/reports/missing.html',text)
    def test_digest_mismatch_blocks_assembly(self):
        self.runbuild();p=self.base/'candidate/en/index.html';p.write_text(p.read_text()+'changed')
        with self.assertRaises(ExpansionError):verified_candidate(self.base/'candidate',self.c)
    def test_path_traversal_in_manifest_rejected(self):
        self.runbuild();p=self.base/'candidate/candidate-manifest.json';m=json.loads(p.read_text());m['pages'][0]['path']='../evil';m['files_sha256']=digest(stable_bytes(m['pages']));p.write_bytes(stable_bytes(m))
        with self.assertRaises(ExpansionError):verified_candidate(self.base/'candidate',self.c)


class AssemblyTests(BuildFixture, unittest.TestCase):
    def staging(self):
        root=self.base/'site';root.mkdir()
        originals={HOME:html(body='<h1>Research library</h1><p>Independent market research.</p><p><a href="/blog/20260922-test.html">Research note</a></p>'),
                   BLOG:html(BLOG,body='<h1>Research note</h1><p>Source based analysis for readers.</p>',extra='<script type="application/ld+json">'+json.dumps({'@type':'Article','url':BLOG,'datePublished':'2026-09-22','dateModified':'2026-09-22'})+'</script>')}
        for url,raw in originals.items():p=root/file_for_url(url);p.parent.mkdir(parents=True,exist_ok=True);p.write_bytes(raw)
        (root/'robots.txt').write_text('User-agent: GPTBot\nDisallow: /\nUser-agent: *\nAllow: /\n')
        return root,originals
    def test_dry_run_writes_nothing(self):
        self.runbuild();root,originals=self.staging()
        result=assemble(root,self.c,[self.base/'candidate'],('en',))
        self.assertEqual(result['status'],'dry-run');self.assertFalse((root/'en').exists())
        self.assertEqual((root/'index.html').read_bytes(),originals[HOME])
    def test_approval_is_explicit_and_exact(self):
        self.runbuild();root,_=self.staging()
        with self.assertRaises(ExpansionError):assemble(root,self.c,[self.base/'candidate'],('fr',),apply=True)
        self.assertFalse((root/'en').exists())
    def test_activation_preserves_body_dates_and_training_policy(self):
        self.runbuild();root,originals=self.staging()
        result=assemble(root,self.c,[self.base/'candidate'],('en',),apply=True)
        self.assertFalse(result['deployment_performed'])
        self.assertIn('content="index,follow"',(root/'en/index.html').read_text())
        self.assertEqual((root/'index.html').read_text().split('</head>',1)[1],originals[HOME].decode().split('</head>',1)[1])
        self.assertIn('User-agent: GPTBot\nDisallow: /',(root/'robots.txt').read_text())
    def test_reciprocal_alternates_and_sitemap(self):
        self.runbuild();root,_=self.staging();assemble(root,self.c,[self.base/'candidate'],('en',),apply=True)
        parsers=[]
        for p in [root/'index.html',root/'en/index.html']:
            parser=PublicParser();parser.feed(p.read_text());parser.close();parsers.append(parser)
        self.assertEqual(parsers[0].alternates,parsers[1].alternates)
        self.assertEqual(parsers[1].alternates['en'],ORIGIN+'/en/')
        self.assertNotIn('ko',parsers[1].alternates)
        rootxml=ET.fromstring((root/'sitemap-extended-en.xml').read_bytes())
        self.assertEqual(len(rootxml),2)
    def test_stale_generation_is_rejected_before_any_write(self):
        self.runbuild();root,_=self.staging();(root/'index.html').write_text('changed')
        with self.assertRaises(ExpansionError):assemble(root,self.c,[self.base/'candidate'],('en',),apply=True)
        self.assertFalse((root/'en').exists())
    def test_existing_locale_directory_is_not_overwritten(self):
        self.runbuild();root,_=self.staging();(root/'en').mkdir()
        with self.assertRaises(ExpansionError):assemble(root,self.c,[self.base/'candidate'],('en',),apply=True)
    def test_two_locales_publish_independently_as_one_validated_group(self):
        self.runbuild();self.runbuild('fr',output='french');root,_=self.staging()
        result=assemble(root,self.c,[self.base/'candidate',self.base/'french'],('en','fr'),apply=True)
        self.assertEqual(result['locales'],['en','fr'])
        self.assertIn('hreflang="fr"',(root/'en/index.html').read_text())
        self.assertIn('hreflang="en"',(root/'fr/index.html').read_text())


class CostAndWorkflowTests(unittest.TestCase):
    def test_new_workflow_never_receives_provider_credentials(self):
        source=(ROOT/'.github/workflows/portal-extended-locales-check.yml').read_text()
        self.assertNotIn('secrets.',source);self.assertIn('runs-on: ubuntu-24.04',source)
        self.assertIn('max-parallel: 2',source);self.assertNotIn('actions/upload-artifact',source)
        self.assertNotIn('contents: write',source);self.assertNotIn('actions: write',source)
    def test_no_new_paid_client_or_publication_code(self):
        source=(ROOT/'scripts/build_portal_extended_locales.py').read_text()
        for forbidden in ['import openai','api.deepseek.com','api.deepl.com','requests.post','subprocess.run']:
            self.assertNotIn(forbidden,source)
        self.assertIn('require_actions()',source);self.assertIn("KC_PUBLIC_REPOSITORY",source)
    def test_existing_three_locale_builder_is_not_globally_expanded(self):
        from build_portal_locales import LOCALES
        self.assertEqual(set(LOCALES),{'ko','ja','ar'})
    def test_workflow_yaml_parses(self):
        try:import yaml
        except ImportError:self.skipTest('PyYAML unavailable')
        value=yaml.safe_load((ROOT/'.github/workflows/portal-extended-locales-check.yml').read_text())
        self.assertEqual(set(value['jobs']),{'regression','model-canary'})
    def test_setup_action_uses_same_registry_and_model(self):
        source=(ROOT/'.github/actions/setup-offline-translation/action.yml').read_text()
        self.assertIn('from compare_hymt_translation import LANGUAGES',source)
        self.assertIn('install_hymt_translation_model.py',source)
        self.assertNotIn('DEEPSEEK_API_KEY',source)

if __name__=='__main__':unittest.main(verbosity=2)
