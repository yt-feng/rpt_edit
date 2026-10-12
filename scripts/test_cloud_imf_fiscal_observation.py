"""Offline only: observed book metadata, branch guards and no PDF access."""
from copy import deepcopy
import json
import os
from pathlib import Path
import unittest
from unittest.mock import patch

import cloud_imf_fiscal_observation as p


class FiscalObservationTests(unittest.TestCase):
    def fixture(self):
        return json.loads((Path(__file__).parent/'fixtures/imf_elibrary'/p.FIXTURE).read_text())

    def test_single_actual_crossref_book_resource_without_url_construction(self):
        rows = p.load_sources()
        self.assertEqual(len(rows), 1)
        publication, candidate = rows[0]
        self.assertEqual(candidate, self.fixture()['message']['resource']['primary']['URL'])
        self.assertEqual(publication['doi'], '10.5089/9798229056298.089')
        self.assertEqual(publication['full_title'], 'Fiscal Monitor, October 2026: Special Edition: Chapter 1: Taxing Better to Boost Growth')
        self.assertEqual(p.r.validate_publication_url(candidate)['isbn'], publication['isbn'])
        self.assertFalse(publication['pdf_verified'])

    def test_changed_isbn_doi_resource_or_title_is_rejected(self):
        for change in ({'DOI':'10.5089/9798229056298.007'}, {'ISBN':['9798229056299']},
                       {'title':[]}, {'subtitle':[]}, {'type':'journal-article'},
                       {'resource':{'primary':{'URL':'https://evil.invalid/book'}}},
                       {'resource':{'primary':{'URL':'https://elibrary.imf.org/display/book/9798229056298/9798229056299.xml'}}}):
            fixture=deepcopy(self.fixture());fixture['message'].update(change)
            with self.subTest(change=change), self.assertRaises(ValueError):p.source_and_candidate(fixture)
        with patch.object(p.Path,'read_bytes',return_value=b'{}'), self.assertRaisesRegex(ValueError,'book_fixture_changed'):
            p.load_sources()

    def test_cloud_explicit_approval_and_exact_workflow_branch_before_any_process(self):
        env=dict(GITHUB_ACTIONS='true', EXPLICIT_CLOUD_BROWSER_APPROVAL='true',
                 GITHUB_REPOSITORY='yt-feng/rpt_edit',GITHUB_EVENT_NAME='workflow_dispatch',
                 GITHUB_WORKFLOW_REF=f'yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{p.BRANCH}')
        with patch.object(p.sys,'platform','linux'),patch.dict(os.environ,env,clear=True):
            p.require_approval()
            for key in env:
                with patch.dict(os.environ,{key:'wrong'}),patch.object(p.subprocess,'Popen') as launch:
                    with self.assertRaises(p.b.BrowserDownloadError):p.observe('unused','unused')
                    launch.assert_not_called()
        with patch.object(p.sys,'platform','darwin'),patch.dict(os.environ,env,clear=True):
            with self.assertRaises(p.b.BrowserDownloadError):p.require_approval()

    def test_workflow_is_default_off_and_metadata_only(self):
        workflow=(Path(__file__).parents[1]/'.github/workflows/institution-fetch-test.yml').read_text()
        self.assertIn('default: false',workflow);self.assertIn('persist-credentials: false',workflow)
        self.assertIn('refs/heads/'+p.BRANCH,workflow);self.assertIn('_imf_fiscal_observation/*.json',workflow)
        self.assertNotIn('python scripts/fetch_institution_latest_pdfs.py',workflow)
        code=Path(p.__file__).read_text();self.assertNotIn('.download(',code);self.assertNotIn('seen_state',code)


if __name__ == '__main__': unittest.main()
