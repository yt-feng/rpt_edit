"""Pure replay of the two real Spanish publisher pages; no transport calls."""
from copy import deepcopy
import json
from pathlib import Path
import unittest

import imf_original_edition as e

CASES = json.loads((Path(__file__).parent / 'fixtures/imf_elibrary/spanish_editions_observed.json').read_text())['observations']


class EditionTests(unittest.TestCase):
    def resolve(self, case, status=404):
        return e.resolve_original_edition(case['publication'], case['page'], source_landing_status=status)

    def test_real_pages_keep_original_doi_and_bind_different_actual_edition(self):
        for case in CASES:
            original = deepcopy(case['publication'])
            metadata = self.resolve(case)
            actual = e.validate_original_edition_metadata(metadata, original['doi'], case['page']['final_url'],
                                                          case['page']['download_hrefs'][0])
            self.assertNotEqual(actual['doi'], original['doi'])
            self.assertEqual(actual['isbn'], actual['doi'].split('/')[1].split('.')[0])
            self.assertIn(actual['pages'], {5, 54})
            self.assertEqual(case['publication'], original)
            self.assertEqual(set(metadata), e.METADATA_FIELDS)
            self.assertEqual(set(actual), e.EDITION_FIELDS)

    def test_exact_original_404_is_required_not_connection_or_challenge_failure(self):
        for status in (None, 200, 202, 403, 405, 500, True, '404'):
            with self.subTest(status=status), self.assertRaises(e.EditionError):
                self.resolve(CASES[0], status)

    def test_source_requires_explicit_spanish_and_exact_original_doi_crossref_chain(self):
        for change in ({'original_language': None}, {'original_language': 'fr'}, {'language': 'es'},
                       {'crossref_sha256': None}, {'preview_sha256': ''}, {'metadata': {}},
                       {'isbn': '9798229063074'}, {'issue': '999'}, {'year': '2025'},
                       {'series': ['Working Papers']}, {'full_title': 'Chile: unrelated report'}):
            case = deepcopy(CASES[0]); case['publication'].update(change)
            with self.subTest(change=change), self.assertRaises(e.EditionError): self.resolve(case)

    def test_missing_duplicate_and_conflicting_public_labels_are_rejected(self):
        for label in ('Series', 'Publisher', 'ISBN', 'Language', 'Pages', 'DOI', 'Volume/Issue'):
            original = CASES[0]['page']['visible_body']
            line = next(x for x in original.splitlines() if x.startswith(label + ':'))
            for body in (original.replace(line, ''), original + '\n' + line, original + '\n' + label + ': wrong'):
                case = deepcopy(CASES[0]); case['page']['visible_body'] = body
                with self.subTest(label=label), self.assertRaises(e.EditionError): self.resolve(case)

    def test_no_country_only_or_truncated_or_unready_acceptance(self):
        for change in ({'h1s': ['Chile']}, {'h1s': []}, {'h1s': ['Chile: unrelated mission statistics']},
                       {'ready': False}, {'landing_status': 405}, {'body_truncated': True},
                       {'visible_body': 'x' * (80 * 1024 + 1)}, {'doi_links': []}):
            case = deepcopy(CASES[0]); case['page'].update(change)
            with self.subTest(change=list(change)), self.assertRaises(e.EditionError): self.resolve(case)
        case = deepcopy(CASES[0]); case['publication']['source_title'] = case['publication']['source_title'].replace('Chile', 'Peru')
        case['publication']['full_title'] = case['publication']['source_title']
        with self.assertRaises(e.EditionError): self.resolve(case)

    def test_same_country_wrong_edition_or_external_and_downgraded_urls_rejected(self):
        for field in ('final_url', 'download_hrefs'):
            for transform in (lambda s:s.replace('/083/', '/082/').replace('issue-083', 'issue-082'),
                              lambda s:s.replace('https:', 'http:'), lambda s:s.replace('www.elibrary.imf.org', 'evil.invalid'),
                              lambda s:s.replace('-es.', '-en.'), lambda s:s.replace('https://', 'https://user@')):
                case = deepcopy(CASES[0]); page = case['page']
                page[field] = [transform(page[field][0])] if field == 'download_hrefs' else transform(page[field])
                with self.subTest(field=field), self.assertRaises(e.EditionError): self.resolve(case)

    def test_optional_metadata_conflicts_still_reject(self):
        for metadata in ({'citation_doi':['10.5089/9798229063074.029']}, {'citation_isbn':['9798229063074']},
                         {'dc.title':['Chile: unrelated report']}, {'canonical_url':[CASES[1]['page']['final_url']]}):
            case = deepcopy(CASES[0]); case['page']['metadata'] = metadata
            with self.subTest(metadata=metadata), self.assertRaises(e.EditionError): self.resolve(case)

    def test_receipt_groups_types_unknowns_and_status_are_strict(self):
        case = CASES[0]; original = self.resolve(case)
        variants = [{**original, 'unknown': True}, {k:v for k,v in original.items() if k!='preview_sha256'},
                    {**original, 'source_landing_status': '404'}, {**original, 'source_landing_status': 405},
                    {**original, 'method': 'official_source_preview'}]
        for change in ({'pages':True},{'pages':0},{'isbn':'9798229063074'},{'language':'en'}, {'issue':'082'},
                       {'year':'2025'},{'series':'Working Papers'},{'page_sha256':None}, {'extra':True},
                       {'title':original['original_edition']['title'] + '\x00'},
                       {'title':original['original_edition']['title'] + '\ud800'}):
            variants.append({**original, 'original_edition': {**original['original_edition'], **change}})
        for metadata in variants:
            with self.subTest(metadata=metadata), self.assertRaises(e.EditionError):
                e.validate_original_edition_metadata(metadata, case['publication']['doi'], case['page']['final_url'], case['page']['download_hrefs'][0])


if __name__ == '__main__':
    unittest.main()
