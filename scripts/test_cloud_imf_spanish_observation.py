"""No browser, subprocess, HTTP or socket is started by these tests."""
from copy import deepcopy
import json
import os
from pathlib import Path
import unittest
from unittest.mock import Mock, patch

import cloud_imf_spanish_observation as p


class ObservationTests(unittest.TestCase):
    def fixture(self, name='chile_hls_observed_metadata.json'):
        return json.loads((Path(__file__).parent / 'fixtures/imf_elibrary' / name).read_text())

    def test_two_source_doi_chains_generate_only_same_issue_spanish_candidates(self):
        rows = p.load_sources()
        self.assertEqual(len(rows), 2)
        self.assertEqual({r[0]['doi'] for r in rows}, {'10.5089/9798229062657.029', '10.5089/9798229064521.019'})
        for source, candidate in rows:
            self.assertEqual(source['original_language'], 'es')
            self.assertIn('-en.xml', source['landing_url'])
            original, observed = p.r.validate_publication_url(source['landing_url']), p.r.validate_publication_url(candidate)
            self.assertEqual(observed['language'], 'es')
            for key in ('series', 'year', 'issue', 'document'):
                self.assertEqual(original[key], observed[key])
            self.assertFalse(source['pdf_verified'])

    def test_missing_explicit_language_or_changed_crossref_identity_never_generates_candidate(self):
        sample = self.fixture()
        identity = p.r.bind_source(sample['item'], {}, sample['preview_excerpt'], sample['item']['source_url'])
        publication = p.r.resolve_crossref(identity, sample['crossref'])
        for change in ({'original_language': None}, {'original_language': 'fr'}, {'issue': '072'},
                       {'year': '2025'}, {'landing_url': 'https://evil.invalid/019.2026.issue-071-es.xml'}):
            with patch.object(p.r, 'resolve_crossref', return_value={**publication, **change}), self.assertRaises(ValueError):
                p.source_and_candidate(sample)
        changed = deepcopy(sample); changed['crossref']['message']['DOI'] = '10.5089/9798229063074.029'
        with self.assertRaises(ValueError): p.source_and_candidate(changed)

    def test_workflow_cloud_and_approval_guards_before_any_process(self):
        env = dict(GITHUB_ACTIONS='true', EXPLICIT_CLOUD_BROWSER_APPROVAL='true',
                   GITHUB_REPOSITORY='yt-feng/rpt_edit', GITHUB_EVENT_NAME='workflow_dispatch',
                   GITHUB_WORKFLOW_REF=f'yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{p.BRANCH}')
        with patch.object(p.sys, 'platform', 'linux'), patch.dict(os.environ, env, clear=True):
            p.require_approval()
            for key in env:
                with patch.dict(os.environ, {key: 'wrong'}), patch.object(p.subprocess, 'Popen') as spawn:
                    with self.assertRaises(p.b.BrowserDownloadError): p.observe('unused', 'unused')
                    spawn.assert_not_called()
        with patch.object(p.sys, 'platform', 'darwin'), patch.dict(os.environ, env, clear=True):
            with self.assertRaises(p.b.BrowserDownloadError): p.require_approval()

    def test_default_workflow_is_false_and_no_production_entrypoint_is_called(self):
        workflow = (Path(__file__).parents[1] / '.github/workflows/institution-fetch-test.yml').read_text()
        self.assertIn('default: false', workflow)
        self.assertIn('timeout-minutes: 10', workflow)
        self.assertIn('persist-credentials: false', workflow)
        self.assertIn('path: _imf_spanish_observation/*.json', workflow)
        self.assertNotIn('python scripts/fetch_institution_latest_pdfs.py', workflow)
        code = Path(p.__file__).read_text()
        self.assertNotIn('.download(', code)
        self.assertNotIn('seen_state', code)


if __name__ == '__main__': unittest.main()
