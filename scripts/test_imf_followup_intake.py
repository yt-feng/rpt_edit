"""Official IEO originals retain exact intake and durable hold provenance."""
import copy
from datetime import datetime, timezone
import json
from pathlib import Path
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import fetch_institution_latest_pdfs as fetcher
import imf_elibrary_resolver as resolver
import imf_ieo_followup as followup
import institution_source_health as health
import test_imf_ieo_followup as fixture


NOW = datetime(2026, 10, 13, tzinfo=timezone.utc)


def followup_hold_fixture():
    with tempfile.TemporaryDirectory() as directory:
        proof, _, _ = fixture.FollowupTests().run_download(Path(directory))
    row = dict(institution='imf', title=proof['title'], published=proof['published'],
               source_page_url=proof['source_url'], pdf_url=proof['pdf_url'], bytes=proof['bytes'],
               sha256=proof['sha256'], feed_pdf_candidates=[], imf_official_followup=proof,
               local_filename=f"IMF_{fetcher.slug(proof['title'])}_{fetcher.short_hash('imf:' + proof['source_guid'])}.pdf")
    item = dict(title=row['title'], guid=proof['source_guid'], date=row['published'],
                source_url=row['source_page_url'], scrape_url=row['source_page_url'],
                coveo_unique_id='synthetic-ieo-source', pdf_candidates=[])
    source = dict(source=row['local_filename'], sha256=row['sha256'], size=row['bytes'])
    return row, item, source


class FollowupIntakeTests(unittest.TestCase):
    def invoke(self, root, *, held=False, failed=False):
        row, item, source = followup_hold_fixture()
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return NOW
        session = Mock()
        session.get.side_effect = [fixture.Response(followup.DIRECTORY_URL, fixture.directory(), 404 if failed else 200),
                                   fixture.Response(fixture.LANDING, fixture.landing()),
                                   fixture.Response(fixture.PDF_URL, fixture.pdf_bytes())]
        browser = SimpleNamespace(enabled=True, download=Mock(side_effect=AssertionError('No browser download')))
        argv = ['fetcher', '--institutions', 'imf', '--since-days', '7', '--output-dir', str(root/'pdfs'),
                '--archive-path', str(root/'archive.jsonl'), '--seen-state-path', str(root/'seen.json'),
                '--pending-intake-path', str(root/'pending.json')]
        if held:
            (root/'holds.json').write_text(json.dumps(dict(schema=1, sources=[source], versions=[row])))
            argv += ['--dependency-holds', str(root/'holds.json')]
            pending = fetcher.PendingIntake(root/'pending.json', {}, now=NOW)
            pending.admit(item, 7); pending.save()
        with (patch.object(fetcher.sys, 'argv', argv), patch.object(fetcher, 'datetime', Clock),
              patch.object(fetcher.requests, 'Session', return_value=session),
              patch.object(fetcher, 'collect_coveo_items', return_value=[item]),
              patch.object(fetcher, 'collect_coveo_preview_html', return_value='bound source preview') as preview,
              patch.object(resolver, 'bind_source', return_value=fixture.IDENTITY),
              patch.object(fetcher, 'resolve_imf_browser_publication', side_effect=ValueError('unavailable')) as resolve,
              patch.object(fetcher, 'collect_coveo_preview_candidates', return_value=[]),
              patch.object(fetcher, 'http_get', return_value=Mock(text='', url=item['source_url'])),
              patch.object(fetcher, 'download_pdf', side_effect=AssertionError('No ordinary PDF candidate')),
              patch.object(fetcher, 'resolve_working_proxy', side_effect=AssertionError('No proxy probe')),
              patch.object(fetcher, 'log'), patch.object(fetcher, 'warn'),
              patch.object(fetcher, 'write_github_output'), patch.object(fetcher, 'write_source_health_summary')):
            code = fetcher._main(browser)
        manifest = json.loads((root/'pdfs/institution_run_manifest.json').read_text())
        browser.download.assert_not_called()
        return code, manifest, session, resolve, preview

    def test_actual_followup_route_is_healthy_and_deduplicates_only_after_seen(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            code, manifest, session, resolve, _ = self.invoke(root)
            self.assertEqual((code, manifest['downloaded_count']), (0, 1))
            self.assertEqual(session.get.call_count, 3)
            resolve.assert_not_called()
            row = manifest['downloaded'][0]
            self.assertIn('imf_official_followup', row)
            self.assertNotIn('imf_live_download', row)
            self.assertEqual(health.classify(manifest, producer_exit_code=code, log_exit_code=0,
                             date_folder=manifest['date'], institutions='imf')['source_health'], 'healthy')
            key = 'imf:'+fixture.IDENTITY.guid
            self.assertIn(key, json.loads((root/'pending.json').read_text())['items'])
            self.assertEqual(json.loads((root/'seen.json').read_text())['items'][key]['status'], 'downloaded')
            code, manifest, session, resolve, preview = self.invoke(root)
            self.assertEqual((code, manifest['downloaded_count']), (0, 0))
            session.get.assert_not_called(); resolve.assert_not_called(); preview.assert_not_called()
            self.assertEqual(json.loads((root/'pending.json').read_text())['items'], {})
            self.assertEqual(len((root/'archive.jsonl').read_text().splitlines()), 1)

    def test_real_followup_hold_skips_network_without_seen_or_pending_retirement(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            code, manifest, session, resolve, preview = self.invoke(root, held=True)
            self.assertEqual((code, manifest['downloaded_count'], manifest['dependency_held_count']), (0, 0, 1))
            session.get.assert_not_called(); resolve.assert_not_called(); preview.assert_not_called()
            self.assertEqual(json.loads((root/'seen.json').read_text())['items'], {})
            self.assertIn('imf:'+fixture.IDENTITY.guid, json.loads((root/'pending.json').read_text())['items'])
            self.assertFalse((root/'archive.jsonl').exists())

    def test_failed_followup_stays_queued_and_truthfully_unhealthy(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            code, manifest, session, resolve, _ = self.invoke(root, failed=True)
            self.assertEqual((code, manifest['downloaded_count']), (2, 0))
            self.assertEqual(session.get.call_count, 1)
            resolve.assert_called_once()
            self.assertEqual(json.loads((root/'seen.json').read_text())['items'], {})
            self.assertIn('imf:'+fixture.IDENTITY.guid, json.loads((root/'pending.json').read_text())['items'])
            self.assertNotEqual(health.classify(manifest, producer_exit_code=code, log_exit_code=0,
                                date_folder=manifest['date'], institutions='imf')['source_health'], 'healthy')

    def test_hold_requires_exact_complete_proof_and_current_identity(self):
        row, item, source = followup_hold_fixture()
        with tempfile.TemporaryDirectory() as directory:
            archive = Path(directory)/'absent.jsonl'
            versions = fetcher.dependency_hold_versions(archive, [source], [row])
            self.assertTrue(fetcher.matches_dependency_hold(versions, source['source'], item))
            for changed in ({'guid': 'different'}, {'title': item['title']+' Annex'},
                            {'date': '2026-10-10T04:00:00+00:00'}, {'source_url': item['source_url']+'-other'},
                            {'pdf_candidates': [row['pdf_url']]}, {'pdf_candidates': ()}):
                with self.subTest(changed=changed):
                    self.assertFalse(fetcher.matches_dependency_hold(versions, source['source'], dict(item, **changed)))
            self.assertFalse(fetcher.matches_dependency_hold(versions, source['source'], item, []))
            variants = []
            for missing in row['imf_official_followup']:
                value = copy.deepcopy(row); del value['imf_official_followup'][missing]; variants.append(value)
            for changed in ({'imf_official_followup_extra': True}, {'imf_live_download': {}},
                            {'verified_original_pages': 25}, {'acquisition_method': 'verified_original_cache'},
                            {'institution': 'bis'}, {'sha256': None}, {'title': 'Different title'},
                            {'published': '2026-10-09'}):
                variants.append(dict(row, **changed))
            for changed in ({'source_guid': 'wrong'}, {'sha256': 'f'*64}, {'bytes': True}, {'pdf_status': 404}):
                variants.append(dict(row, imf_official_followup=dict(row['imf_official_followup'], **changed)))
            variants += [{key: value for key, value in row.items() if key != missing}
                         for missing in ('sha256', 'feed_pdf_candidates', 'imf_official_followup')]
            for value in variants:
                with self.subTest(value=value):
                    held = fetcher.dependency_hold_versions(archive, [source], [value])
                    self.assertFalse(fetcher.matches_dependency_hold(held, source['source'], item))
            for changed in ({'sha256': 'f'*64}, {'size': source['size']+1}):
                held = fetcher.dependency_hold_versions(archive, [dict(source, **changed)], [row])
                self.assertFalse(fetcher.matches_dependency_hold(held, source['source'], item))
            conflict = copy.deepcopy(row); conflict['imf_official_followup']['preview_sha256'] = 'e'*64
            held = fetcher.dependency_hold_versions(archive, [source], [row, conflict])
            self.assertFalse(fetcher.matches_dependency_hold(held, source['source'], item))
            legacy = {key: value for key, value in row.items() if key not in {'imf_official_followup', 'sha256'}}
            held = fetcher.dependency_hold_versions(archive, [source], [row, legacy])
            self.assertFalse(fetcher.matches_dependency_hold(held, source['source'], item))


if __name__ == '__main__':
    unittest.main()
