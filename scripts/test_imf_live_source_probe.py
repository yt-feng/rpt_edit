"""Offline tests: no HTTP, cloud client or browser process is started."""
import contextlib
from copy import deepcopy
import hashlib
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import imf_live_source_probe as p
from imf_cloud_browser import BrowserDownloadError
from fetch_institution_latest_pdfs import short_hash, slug

ROOT = Path(__file__).resolve().parents[1]


class ProbeTests(unittest.TestCase):
    @contextlib.contextmanager
    def root(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            for name in (p.FIXTURE, *p.PROTECTED):
                path = root / name
                path.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(ROOT / name, path)
            yield root

    def test_frozen_three_are_the_exact_original_sources_and_filenames(self):
        with self.root() as root:
            rows = p.targets(root)
            original = json.loads((ROOT / 'scripts/fixtures/institution_sources/figure_metadata_20261015.json').read_text())
            self.assertEqual([{key: row[key] for key in ('local_filename', 'sha256', 'bytes')} for row in rows],
                             original['sources'][:3])
            for row in rows:
                self.assertEqual(row['local_filename'],
                    f"IMF_{slug(row['item']['title'])}_{short_hash('imf:' + row['item']['guid'])}.pdf")
            (root / p.FIXTURE).write_text('{}')
            with self.assertRaisesRegex(p.ProbeError, 'frozen_sources_changed'):
                p.targets(root)

    @contextlib.contextmanager
    def mocks(self, root, *, change=None, resolve_change=None):
        rows = deepcopy(p.targets(root))
        bodies = {row['item']['guid']: b'%PDF-mock-' + str(i).encode() for i, row in enumerate(rows)}
        for row in rows:
            data = bodies[row['item']['guid']]
            row['sha256'], row['bytes'] = hashlib.sha256(data).hexdigest(), len(data)
        browser = SimpleNamespace(last_source_attempts=[])
        def resolve(cfg, session, item, timeout):
            publication = dict(source_guid=item['guid'], source_url=item['source_url'], source_title=item['title'])
            if resolve_change:
                resolve_change(publication)
            return publication
        def download(publication, path, max_bytes, expected_sha256):
            data = bodies[publication['source_guid']]
            self.assertEqual(expected_sha256, hashlib.sha256(data).hexdigest())
            self.assertEqual(max_bytes, 128 * 1024 * 1024)
            path.write_bytes(data)
            browser.last_source_attempts = [{'route': 1, 'landing_status': 403}, {'route': 2, 'landing_status': 200}]
            proof = dict(schema=1, source_guid=publication['source_guid'], source_url=publication['source_url'],
                title=publication['source_title'], doi='10.5089/9798229063937.019',
                landing_url='https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml',
                pdf_url='https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf',
                identity_sha256='a' * 64, crossref_sha256='b' * 64, sha256=expected_sha256, bytes=len(data),
                pages=2, landing_status=200, pdf_status=200, source_identity_verified=True,
                transport='existing_subscription_vless_browser')
            if change:
                change(proof, path)
            return proof
        browser.download = Mock(side_effect=download)
        @contextlib.contextmanager
        def factory(**kwargs):
            try:
                yield browser
            finally:
                browser.closed = True
        session = Mock()
        @contextlib.contextmanager
        def session_factory():
            try:
                yield session
            finally:
                session.close()
        producer = SimpleNamespace(INSTITUTIONS={'imf': {}}, requests=SimpleNamespace(Session=session_factory),
            _fetch_subscription=Mock(), _b64_text=Mock(), source_request_headers=Mock(return_value={}),
            resolve_imf_browser_publication=Mock(side_effect=resolve))
        with patch.object(p, 'targets', return_value=rows), patch.object(p, 'require_cloud'), \
             patch.dict(os.environ, {'IMF_CLOUD_BROWSER_ENABLED': 'true'}, clear=True):
            yield producer, factory, browser, session

    def test_all_three_live_receipts_and_bytes_pass_without_production_writes(self):
        with self.root() as root, self.mocks(root) as (producer, factory, browser, session):
            before = {name: (root / name).read_bytes() for name in p.PROTECTED}
            result = p.probe(root, producer, browser_factory=factory)
            self.assertTrue(result['accepted'])
            self.assertTrue(result['production_state_unchanged'])
            self.assertEqual(result['verified_count'], 3)
            self.assertEqual(producer.resolve_imf_browser_publication.call_count, 3)
            self.assertEqual(browser.download.call_count, 3)
            self.assertTrue(browser.closed); session.close.assert_called_once()
            producer._fetch_subscription.assert_not_called()
            self.assertIs(session.trust_env, False)
            self.assertEqual(before, {name: (root / name).read_bytes() for name in p.PROTECTED})
            self.assertEqual({file.suffix for file in (root / p.OUT).iterdir()}, {'.json', '.pdf'})
            self.assertEqual(json.loads((root / p.OUT / 'exact-scope-acceptance.json').read_text()), result)

    def test_each_corruption_is_rejected_and_remaining_sources_still_checked(self):
        for change in (lambda proof, path: proof.update(source_guid='different-source'),
                       lambda proof, path: proof.update(pdf_status=403),
                       lambda proof, path: proof.update(title='Different report'),
                       lambda proof, path: path.write_bytes(b'%PDF-changed'),
                       lambda proof, path: proof.update(bytes=proof['bytes'] + 1)):
            with self.subTest(change=change), self.root() as root, self.mocks(root, change=change) as (producer, factory, browser, session):
                result = p.probe(root, producer, browser_factory=factory)
                self.assertFalse(result['accepted'])
                self.assertEqual(result['verified_count'], 0)
                self.assertEqual(browser.download.call_count, 3)

    def test_changed_resolved_source_never_starts_download(self):
        with self.root() as root, self.mocks(root, resolve_change=lambda publication: publication.update(
                source_url='https://www.imf.org/en/publications/wrong')) as (producer, factory, browser, session):
            result = p.probe(root, producer, browser_factory=factory)
            self.assertFalse(result['accepted'])
            browser.download.assert_not_called()
            self.assertEqual([row['source_attempts'] for row in result['reports']], [[], [], []])

    def test_state_change_or_existing_output_cannot_pass(self):
        with self.root() as root, self.mocks(root, change=lambda proof, path:
                (root / p.PROTECTED[0]).write_text('changed')) as (producer, factory, browser, session):
            result = p.probe(root, producer, browser_factory=factory)
            self.assertFalse(result['accepted']); self.assertFalse(result['production_state_unchanged'])
            with self.assertRaisesRegex(p.ProbeError, 'probe_output_must_be_fresh'):
                p.probe(root, producer, browser_factory=factory)

    def test_disabled_or_local_execution_is_zero_metadata_sessions_and_browser(self):
        for env, platform in (({}, 'linux'), ({'GITHUB_ACTIONS': 'true',
                'EXPLICIT_CLOUD_BROWSER_APPROVAL': 'true'}, 'linux'),
                ({'GITHUB_ACTIONS': 'true', 'EXPLICIT_CLOUD_BROWSER_APPROVAL': 'true',
                  'IMF_CLOUD_BROWSER_ENABLED': 'true'}, 'darwin')):
            producer, factory = Mock(), Mock()
            with self.subTest(platform=platform, env=env), patch.dict(os.environ, env, clear=True), \
                 patch.object(sys, 'platform', platform):
                with self.assertRaises((p.ProbeError, BrowserDownloadError)):
                    p.probe(Path('/unused-mocked-root'), producer, browser_factory=factory)
            self.assertEqual(producer.mock_calls, []); factory.assert_not_called()

    def test_workflow_scope_is_read_only_and_exposes_no_downstream_credentials(self):
        workflow = (ROOT / '.github/workflows/institution-fetch-test.yml').read_text()
        self.assertIn('- imf-live-exact-20261015', workflow)
        self.assertIn('scripts/imf_live_source_probe.py', workflow)
        self.assertIn('contents: read', workflow)
        for secret in ('R2_ACCESS_KEY_ID', 'R2_SECRET_ACCESS_KEY', 'WECHAT_APPSECRET', 'DEEPSEEK_API_KEY', 'MINERU_API_TOKEN'):
            self.assertNotIn(secret, workflow)


if __name__ == '__main__':
    unittest.main()
