"""Pure real-source Fiscal chapter matching and strict rejection regressions."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

import imf_fiscal_chapter as f

FIXTURE = json.loads((Path(__file__).parent / 'fixtures/imf_elibrary/fiscal_chapter_observed.json').read_text())


class FiscalChapterTests(unittest.TestCase):
    def setUp(self):
        self.case = deepcopy(FIXTURE)
        self.item = self.case['source_item']
        self.html = self.case['source_preview_html']
        self.source = f.prepare_fiscal_chapter(self.item, self.html, self.item['source_url'])

    def resolve(self, search=None, exact=None):
        return f.resolve_fiscal_chapter(self.source, search or self.case['search_payload'],
                                       exact or self.case['exact_payload'])

    def test_real_source_complete_search_and_exact_doi_bind_one_chapter(self):
        self.assertEqual(f.select_fiscal_chapter(self.source, self.case['search_payload']), '10.5089/9798229056298.089')
        self.assertEqual(self.source['chapter'], 1)
        self.assertEqual((self.source['year'], self.source['month']), ('2026', '10'))
        self.assertEqual(self.source['query_params']['rows'], 100)
        self.assertIn('until-pub-date:2026-10-31', self.source['query_params']['filter'])
        pub = self.resolve()
        self.assertEqual(pub['source_title'], self.item['title'])
        self.assertEqual(pub['subtitle'], 'Chapter 1: ' + self.item['title'])
        self.assertEqual(pub['full_title'], pub['title'] + ': ' + pub['subtitle'])
        self.assertIsNone(pub['crossref_sha256'])
        self.assertEqual(pub['metadata']['exact_crossref_sha256'], f.digest(self.case['exact_payload']))
        self.assertEqual(set(pub['metadata']), f.METADATA_FIELDS)
        self.assertFalse(pub['pdf_verified'])
        self.assertEqual(pub['pdf_url_candidates'], [])

    def test_explicit_any_doi_or_ambiguous_doi_cannot_use_fiscal_discovery(self):
        for tail in ('10.5089/9798229056298.089', '10.1234/example',
                     '10&#46;5089/9798229056298.089', r'10.5089\/9798229056298.089',
                     '10.5089/9798229056298.089 10.5089/9798229057226.087'):
            with self.subTest(tail=tail), self.assertRaises(f.FiscalChapterError):
                f.prepare_fiscal_chapter(self.item, self.html + tail, self.item['source_url'])

    def test_preview_source_title_canonical_date_language_chapter_and_series_bound(self):
        changes = [('Taxing Better', 'Taxing Elsewhere'), ('name="language" content="ENG"', 'name="language" content="SPA"'),
                   ('Chapter 1 Fiscal Monitor', 'See Chapter 1 Fiscal Monitor'),
                   ('Chapter 1 Fiscal Monitor', 'Chapter 0 Fiscal Monitor'), ('2026-10-05', '2026-09-05'),
                   ('<h1>Fiscal Monitor</h1>', '<h1>World Economic Outlook</h1>'),
                   ('/fm/issues/', '/weo/issues/'), ('International Monetary Fund', 'Another Publisher')]
        for old, new in changes:
            with self.subTest(old=old), self.assertRaises(f.FiscalChapterError):
                f.prepare_fiscal_chapter(self.item, self.html.replace(old, new), self.item['source_url'])
        with self.assertRaises(f.FiscalChapterError):
            f.prepare_fiscal_chapter(self.item, self.html, self.item['source_url'] + '/other')

    def test_conflicting_description_and_changed_bound_source_rejected(self):
        with self.assertRaises(f.FiscalChapterError):
            f.prepare_fiscal_chapter(self.item, self.html + '<meta name="Description" content="Chapter 2 Fiscal Monitor">', self.item['source_url'])
        for field, value in [('chapter', True), ('chapter', 2), ('year', '2025'), ('query_params', {}),
                             ('identity_sha256', 'a'*64), ('source_guid', 'bad\nsource'), ('source_guid', 'bad\ud800source')]:
            bad = dict(self.source, **{field:value})
            with self.subTest(field=field), self.assertRaises(f.FiscalChapterError):
                f.select_fiscal_chapter(bad, self.case['search_payload'])

    def test_incomplete_paginated_oversized_or_empty_search_rejected(self):
        for change in ({'total-results': 6}, {'total-results': 101}, {'total-results': True},
                       {'items-per-page': 5}, {'query': {'start-index': 1}}, {'items': []}):
            payload = deepcopy(self.case['search_payload']); payload['message'].update(change)
            with self.subTest(change=change), self.assertRaises(f.FiscalChapterError):
                f.select_fiscal_chapter(self.source, payload)

    def test_nonunique_and_wrong_chapter_month_or_book_rejected(self):
        payload = deepcopy(self.case['search_payload']); payload['message']['items'].append(deepcopy(payload['message']['items'][0]))
        payload['message']['total-results'] += 1
        with self.assertRaises(f.FiscalChapterError): f.select_fiscal_chapter(self.source, payload)
        for change in ({'subtitle':['Chapter 2: '+self.item['title']]}, {'subtitle':['Chapter 1: Online Annexes']},
                       {'title':['Fiscal Monitor, September 2026: Special Edition']}, {'publisher':'Other'},
                       {'type':'journal-article'}, {'language':'es'}, {'published':{'date-parts':[[2026,9]]}},
                       {'ISBN':['9798229057226']}, {'DOI':'10.5089/9798229056298.087'}):
            payload = deepcopy(self.case['search_payload']); payload['message']['items'][0].update(change)
            with self.subTest(change=change), self.assertRaises(f.FiscalChapterError):
                f.select_fiscal_chapter(self.source, payload)

    def test_exact_response_must_agree_with_search_and_every_publication_date(self):
        for change in ({'DOI':'10.5089/9798229057226.089'}, {'subtitle':['Chapter 1: Another Topic']},
                       {'published-print':{'date-parts':[[2026,9]]}}, {'published-online':{'date-parts':[[2026,10,32]]}},
                       {'published':{'date-parts':[[2026]]}}, {'ISBN':[]}, {'language':None}):
            exact = deepcopy(self.case['exact_payload']); exact['message'].update(change)
            with self.subTest(change=change), self.assertRaises(f.FiscalChapterError): self.resolve(exact=exact)

    def test_foreign_mismatched_encoded_and_userinfo_book_urls_rejected(self):
        for replace in (lambda x:x.replace('elibrary.imf.org','example.invalid'), lambda x:x.replace('https:', 'http:'),
                        lambda x:x.replace('https://', 'https://@'), lambda x:x.replace('9798229056298','9798229057226'),
                        lambda x:x.replace('/display/', '/%64isplay/'), lambda x:x+'&extra=yes'):
            exact = deepcopy(self.case['exact_payload']); exact['message']['resource']['primary']['URL']=replace(exact['message']['resource']['primary']['URL'])
            with self.subTest(replace=replace), self.assertRaises(f.FiscalChapterError): self.resolve(exact=exact)

    def test_proof_needs_actual_publisher_page_and_exact_pdf_book(self):
        pub = self.resolve(); meta=pub['metadata']; pdf=pub['landing_url'].split('?')[0].replace('/display/', '/downloadpdf/display/').replace('.xml', '.pdf')
        with self.assertRaises(f.FiscalChapterError):
            f.validate_fiscal_chapter_metadata(meta,pub['source_title'],pub['doi'],pub['landing_url'],pdf)
        complete={**meta,'publisher_page':{'pages':31,'page_sha256':'a'*64}}
        self.assertEqual(f.validate_fiscal_chapter_metadata(complete,pub['source_title'],pub['doi'],pub['landing_url'],pdf),complete)
        for page in ({'pages':True,'page_sha256':'a'*64},{'pages':0,'page_sha256':'a'*64},
                     {'pages':31,'page_sha256':''},{'pages':31,'page_sha256':'a'*64,'unknown':True}):
            with self.subTest(page=page),self.assertRaises(f.FiscalChapterError):
                f.validate_fiscal_chapter_metadata({**meta,'publisher_page':page},pub['source_title'],pub['doi'],pub['landing_url'],pdf)
        with self.assertRaises(f.FiscalChapterError):
            f.validate_fiscal_chapter_metadata(complete,pub['source_title'],pub['doi'],pub['landing_url'],pdf.replace('9798229056298','9798229057226'))

    def test_metadata_unknown_keys_types_title_and_hashes_rejected(self):
        pub=self.resolve()
        for change in ({'extra':True},{'chapter':True},{'search_total_results':101},{'year':2026},
                       {'month':'Oct'},{'exact_crossref_sha256':None},{'book_subtitle':'Chapter 1: Online Annexes'},
                       {'book_title':'Fiscal Monitor, October 2026: Special Edition\n'}):
            with self.subTest(change=change),self.assertRaises(f.FiscalChapterError):
                f.validate_fiscal_chapter_metadata({**pub['metadata'],**change},pub['source_title'],pub['doi'],pub['landing_url'])

    def test_real_book_landing_keeps_main_h1_and_requires_complete_chapter_evidence(self):
        pub = self.resolve(); page = self.case['page']
        original = deepcopy(pub)
        url, metadata = f.resolve_fiscal_landing(pub, page)
        self.assertEqual(url, page['download_hrefs'][0])
        self.assertEqual(metadata['publisher_page']['pages'], 31)
        self.assertEqual(set(metadata), f.METADATA_FIELDS | {'publisher_page'})
        self.assertEqual(pub, original)
        self.assertNotEqual(f.title_key(page['h1s'][0]), f.title_key(pub['full_title']))
        self.assertEqual(f.title_key(page['metadata']['citation_title'][0]), f.title_key(pub['full_title']))
        f.validate_fiscal_chapter_metadata(metadata, pub['source_title'], pub['doi'], page['final_url'], url)

    def test_book_landing_http_readiness_body_bounds_and_source_provenance_required(self):
        pub = self.resolve()
        for change in ({'landing_status':202}, {'landing_status':True}, {'ready':False},
                       {'body_truncated':True}, {'visible_body':'x'*(80*1024+1)},
                       {'h1s':[]}, {'h1s':[pub['full_title']]}, {'h1s':[pub['title'],pub['title']]}):
            with self.subTest(change=list(change)), self.assertRaises(f.FiscalChapterError):
                f.resolve_fiscal_landing(pub,{**self.case['page'],**change})
        for change in ({'crossref_sha256':'a'*64},{'preview_sha256':'a'*64},{'year':'2025'},
                       {'source_title':'Other topic of public finance'},{'title':'Other book'}, {'isbn':'9798229057226'}):
            with self.subTest(change=change), self.assertRaises(f.FiscalChapterError):
                f.resolve_fiscal_landing({**pub,**change},self.case['page'])

    def test_each_book_label_must_be_unique_and_correct(self):
        pub=self.resolve(); original=self.case['page']['visible_body']
        for label in ('Series','Publisher','ISBN','Language','Pages','DOI','Publication Date'):
            line=next(x for x in original.splitlines() if x.startswith(label+':'))
            for body in (original.replace(line,''),original+'\n'+line,original+'\n'+label+': wrong'):
                with self.subTest(label=label),self.assertRaises(f.FiscalChapterError):
                    f.resolve_fiscal_landing(pub,{**self.case['page'],'visible_body':body})
        for old,new in (('Language: English','Language: Spanish'),('Pages: 31','Pages: 0'),
                        ('06 Oct 2026','06 Sep 2026'),('06 Oct 2026','32 Oct 2026'),
                        ('Flagships, Fiscal Monitor','Flagships, World Economic Outlook'),
                        ('ISBN: 9798229056298','ISBN: 9798229057226')):
            with self.subTest(old=old),self.assertRaises(f.FiscalChapterError):
                f.resolve_fiscal_landing(pub,{**self.case['page'],'visible_body':original.replace(old,new)})

    def test_book_chapter_topic_must_appear_independently_in_body_and_citation(self):
        pub=self.resolve()
        for field in ('book_title','book_subtitle'):
            page=deepcopy(self.case['page']);page['visible_body']=page['visible_body'].replace(pub['metadata'][field],'')
            with self.subTest(field=field),self.assertRaises(f.FiscalChapterError):f.resolve_fiscal_landing(pub,page)
        for tag in ('citation_title','citation_isbn'):
            for value in (None,[],[''],[pub['title']],['Unrelated chapter title']):
                page=deepcopy(self.case['page'])
                if value is None:page['metadata'].pop(tag)
                else:page['metadata'][tag]=value
                with self.subTest(tag=tag,value=value),self.assertRaises(f.FiscalChapterError):f.resolve_fiscal_landing(pub,page)

    def test_book_doi_and_pdf_anchors_duplicate_only_when_identical(self):
        pub=self.resolve();page=deepcopy(self.case['page'])
        page['doi_links']*=2;page['download_hrefs']*=2
        self.assertEqual(f.resolve_fiscal_landing(pub,page)[0],page['download_hrefs'][0])
        for field in ('doi_links','download_hrefs'):
            for value in ([],[None],page[field][:1]*17,page[field]+['https://example.invalid/other.pdf']):
                with self.subTest(field=field),self.assertRaises(f.FiscalChapterError):
                    f.resolve_fiscal_landing(pub,{**page,field:value})

    def test_book_same_document_and_present_metadata_conflicts_stay_strict(self):
        pub=self.resolve()
        for tags in ({'citation_doi':['10.5089/9798229057226.087']},{'dc.title':['Other book']},
                     {'citation_doi':[]},{'canonical_url':[pub['landing_url'].replace('9798229056298','9798229057226')]},
                     {'citation_pdf_url':[self.case['page']['download_hrefs'][0].replace('https:','http:')]}):
            page=deepcopy(self.case['page']);page['metadata'].update(tags)
            with self.subTest(tags=tags),self.assertRaises(f.FiscalChapterError):f.resolve_fiscal_landing(pub,page)
        for change in (lambda x:x.replace('9798229056298','9798229057226'),lambda x:x.replace('https:','http:'),
                       lambda x:x.replace('www.elibrary.imf.org','example.invalid'),lambda x:x.replace('https://','https://@')):
            page=deepcopy(self.case['page']);page['final_url']=change(page['final_url'])
            with self.assertRaises(f.FiscalChapterError):f.resolve_fiscal_landing(pub,page)


if __name__ == '__main__':
    unittest.main()
