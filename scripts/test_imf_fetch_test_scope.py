"""Offline scope tests; fake producer, generated one-page PDFs, no network."""
import copy
from datetime import datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import sys
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import patch

from pypdf import PdfWriter
import fetch_institution_latest_pdfs as producer
import imf_fetch_test_scope as scope

ROOT = Path(__file__).resolve().parents[1]


class ScopeTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        for name in (scope.SEED, scope.REVIEWED, *scope.PROTECTED):
            dest = self.root / name
            dest.parent.mkdir(parents=True, exist_ok=True)
            shutil.copyfile(ROOT / name, dest)
        self.items = scope.targets(self.root)
        self.output = self.root / scope.OUT

    def fake_fetch(self, discovered=None, failure=None):
        fresh = dict(next(iter(self.items.values())), guid='fresh-outside-scope')
        discovered = [fresh] if discovered is None else discovered
        fake = SimpleNamespace(PendingIntake=producer.PendingIntake)
        raw = {'actual': 'fresh-discovery-metadata'}
        def main():
            args = sys.argv
            self.assertNotIn('--verified-originals-manifest', args)
            self.assertEqual(args[args.index('--imf-pending-retries') + 1], '17')
            self.assertEqual(args[args.index('--seen-state-path') + 1], str(self.output / 'test_seen.json'))
            fake.raw = raw  # Real collect_coveo_items retains raw before merge.
            intake = fake.PendingIntake(self.output / 'imf-pending-intake.json', {},
                                       now=datetime.now(timezone.utc), retry_limit=17)
            fake.selected = intake.merge(discovered)
            if failure:
                raise failure
            return 0
        fake.main = main
        return fake

    def complete_fixture(self):
        scope.fetch(self.root, '261013', self.fake_fetch())
        rows = []
        for item in self.items.values():
            name = f"IMF_{producer.slug(item['title'])}_{producer.short_hash('imf:' + item['guid'])}.pdf"
            writer = PdfWriter()
            writer.add_blank_page(width=100, height=100)
            writer.add_metadata({'/Title': item['title']})
            writer.write(self.output / name)
            size = (self.output / name).stat().st_size
            digest = hashlib.sha256((self.output / name).read_bytes()).hexdigest()
            pdf_url = 'https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf'
            proof = dict(schema=1, source_guid=item['guid'], source_url=item['source_url'],
                         landing_url=pdf_url.replace('/downloadpdf', '').replace('.pdf', '.xml'),
                         pdf_url=pdf_url, doi='10.5089/9798229063937.019', title=item['title'],
                         identity_sha256='1' * 64, crossref_sha256='2' * 64, sha256=digest,
                         bytes=size, pages=1, landing_status=200, pdf_status=200,
                         source_identity_verified=True, transport='existing_subscription_vless_browser')
            rows.append(dict(institution='imf', title=item['title'], published=item['date'],
                             source_page_url=item['source_url'], local_filename=name,
                             pdf_url=pdf_url, sha256=digest, bytes=size, imf_live_download=proof))
        self.manifest = dict(date='261013', generated_at='2026-10-13T00:00:00+00:00', since_days=7,
                             institutions=['imf'], downloaded_count=17, dependency_held_count=0,
                             skipped_count=0, force_reprocess=False, downloaded=rows, skipped=[],
                             source_checks=[dict(institution='imf', institution_en=producer.INSTITUTIONS['imf']['name_en'],
                                                 status='ok', item_count=18, new_pdf_count=17, eligible_item_count=17,
                                                 resolution_failure_count=0, deferred_retry_count=0, discovery_error=False,
                                                 required_for_clean_zero=True, error='')])
        self.save_manifest()

    def save_manifest(self):
        (self.output / 'institution_run_manifest.json').write_text(json.dumps(self.manifest))
        (self.output / 'test_archive.jsonl').write_text(''.join(json.dumps(row) + '\n' for row in self.manifest['downloaded']))

    def verify(self):
        return scope.verify(self.root, '261013', 0)

    def test_scope_filters_after_real_discovery_and_restores_producer(self):
        fake = self.fake_fetch()
        original = fake.PendingIntake
        original_argv = sys.argv
        self.assertEqual(scope.fetch(self.root, '261013', fake), 0)
        self.assertEqual({i['guid'] for i in fake.selected}, set(self.items))
        self.assertEqual(fake.raw, {'actual': 'fresh-discovery-metadata'})
        self.assertIs(fake.PendingIntake, original)
        self.assertIs(sys.argv, original_argv)
        evidence = json.loads((self.output / 'scope-discovery.json').read_text())
        self.assertEqual((evidence['discovered_count'], evidence['excluded_fresh_count']), (1, 1))

    def test_empty_discovery_is_not_replaced_by_frozen_success(self):
        scope.fetch(self.root, '261013', self.fake_fetch(discovered=[]))
        evidence = json.loads((self.output / 'scope-discovery.json').read_text())
        self.assertEqual(evidence['discovered_count'], 0)

    def test_producer_exception_restores_process_state(self):
        fake = self.fake_fetch(failure=RuntimeError('offline fixture'))
        original, argv = fake.PendingIntake, sys.argv
        with self.assertRaises(RuntimeError):
            scope.fetch(self.root, '261013', fake)
        self.assertIs(fake.PendingIntake, original)
        self.assertIs(sys.argv, argv)

    def test_exact_17_new_pdf_hashes_pass_without_cache_or_golden_bytes(self):
        self.complete_fixture()
        result = self.verify()
        self.assertTrue(result['accepted'], result)
        self.assertEqual(result['verified_count'], 17)
        self.assertEqual(result['pages'], 17)
        known = {row['sha256'] for row in json.loads((self.root / scope.REVIEWED).read_text())['records']}
        self.assertTrue(all(row['sha256'] not in known for row in result['reports']))

    def test_missing_zero_duplicate_and_extra_sources_fail(self):
        self.complete_fixture()
        original = copy.deepcopy(self.manifest)
        for rows in ([], original['downloaded'][:-1], original['downloaded'][:-1] + [original['downloaded'][0]],
                     original['downloaded'] + [original['downloaded'][0]]):
            self.manifest = copy.deepcopy(original)
            self.manifest['downloaded'] = rows
            self.manifest['downloaded_count'] = len(rows)
            self.save_manifest()
            self.assertFalse(self.verify()['accepted'])

    def test_wrong_guid_title_date_or_unproven_download_fails(self):
        self.complete_fixture()
        original = copy.deepcopy(self.manifest)
        for change in ('guid', 'title', 'date', 'proof'):
            self.manifest = copy.deepcopy(original)
            row = self.manifest['downloaded'][0]
            if change == 'guid': row['imf_live_download']['source_guid'] = 'other'
            elif change == 'title': row['title'] += ' wrong'
            elif change == 'date': row['published'] = '2026-10-10T00:00:00+00:00'
            else: del row['imf_live_download']
            self.save_manifest()
            self.assertFalse(self.verify()['accepted'])

    def test_real_page_count_and_bytes_checked(self):
        self.complete_fixture()
        self.manifest['downloaded'][0]['imf_live_download']['pages'] = 2
        self.save_manifest()
        self.assertEqual(self.verify()['error'], 'pdf_page_count_mismatch')
        self.manifest['downloaded'][0]['imf_live_download']['pages'] = 1
        self.save_manifest()
        (self.output / self.manifest['downloaded'][0]['local_filename']).write_bytes(b'%PDF-truncated')
        self.assertEqual(self.verify()['error'], 'pdf_bytes_mismatch')

    def test_extra_pdf_and_production_or_pending_mutation_fail(self):
        self.complete_fixture()
        (self.output / 'extra.pdf').write_bytes(b'extra')
        self.assertEqual(self.verify()['error'], 'extra_pdf_files')
        (self.output / 'extra.pdf').unlink()
        path = self.root / scope.PROTECTED[0]
        old = path.read_bytes()
        path.write_bytes(old + b'\n')
        self.assertEqual(self.verify()['error'], 'production_state_changed')
        path.write_bytes(old)
        pending = json.loads((self.output / 'imf-pending-intake.json').read_text())
        next(iter(pending['items'].values()))['since_days'] += 1
        (self.output / 'imf-pending-intake.json').write_text(json.dumps(pending))
        self.assertEqual(self.verify()['error'], 'pending_admission_changed')

    def test_discovery_error_deferred_or_missing_discovery_never_pass(self):
        self.complete_fixture()
        original = copy.deepcopy(self.manifest)
        for change in (dict(status='degraded', discovery_error=True),
                       dict(status='degraded', deferred_retry_count=1)):
            self.manifest = copy.deepcopy(original)
            self.manifest['source_checks'][0].update(change)
            self.save_manifest()
            self.assertFalse(self.verify()['accepted'])
        self.manifest = original
        self.save_manifest()
        discovery = json.loads((self.output / 'scope-discovery.json').read_text())
        discovery['discovered_count'] = 0
        (self.output / 'scope-discovery.json').write_text(json.dumps(discovery))
        self.assertEqual(self.verify()['error'], 'live_discovery_not_proven')

    def test_tampered_metadata_and_reused_output_rejected(self):
        scope.fetch(self.root, '261013', self.fake_fetch())
        with self.assertRaisesRegex(scope.ScopeError, 'test_output_must_be_fresh'):
            scope.fetch(self.root, '261013', self.fake_fetch())
        (self.root / scope.REVIEWED).write_text('{}')
        with self.assertRaisesRegex(scope.ScopeError, 'frozen_metadata_changed'):
            scope.targets(self.root)

    def test_local_main_rejected_before_imported_producer_runs(self):
        with patch.dict(scope.os.environ, {}, clear=True), patch.object(sys, 'argv', ['scope', '--date', '261013']), \
                patch.object(producer, 'main', side_effect=AssertionError('must not run')):
            with self.assertRaisesRegex(scope.ScopeError, 'cloud_execution_required'):
                scope.main()


if __name__ == '__main__':
    unittest.main()
