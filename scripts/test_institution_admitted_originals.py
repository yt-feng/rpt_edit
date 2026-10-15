"""Real private registry bytes, source identity, retry and health boundaries."""
from __future__ import annotations

import copy
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import fetch_institution_latest_pdfs as f
import institution_admitted_originals as a
from institution_dependency_backlog import Backlog
from institution_original_cache import OriginalCache, OPTIONS
from institution_pending_intake import PendingIntake
import institution_source_health as health
from mineru_task_ledger import digest, encoded
from test_fetch_institution_latest_pdfs import live_hold_fixture
from test_institution_verified_originals import pdf
from test_mineru_result_cache import MemoryR2

NOW = datetime(2026, 10, 15, tzinfo=timezone.utc)


class ReadOnlyRegistry(MemoryR2):
    def __init__(self):
        super().__init__(); self.lists = []
    def list_objects_v2(self, **kwargs):
        self.lists.append(kwargs)
        return dict(IsTruncated=False, Contents=[dict(Key=key, Size=len(row['Body']), ETag=digest(row['Body']))
                    for key, row in sorted(self.objects.items()) if key.startswith(kwargs['Prefix'])])
    def put_object(self, **kwargs):
        raise AssertionError('Recovery cannot write storage')


def save(store, key, payload, kind='application/json', metadata=None):
    store.objects[key] = dict(Body=payload, ContentType=kind, Metadata=metadata or {'sha256': digest(payload)})


def fixture(store, number=1):
    row, item, _ = live_hold_fixture(); payload = pdf(number)
    binding = dict(source=row['local_filename'], sha256=digest(payload), size=len(payload), scope='institution',
                   endpoint='https://mineru.net', options=copy.deepcopy(OPTIONS))
    binding['id'] = digest(encoded(binding))
    row.update(binding_id=binding['id'], bytes=len(payload), sha256=digest(payload))
    row['imf_live_download'].update(bytes=len(payload), sha256=digest(payload), pages=2)
    version = dict(schema=1, binding=binding, versions=[row],
                   receipts=[dict(run_id='38658714099', manifest_sha256='1'*64)])
    key = a.PREFIX+binding['id']+'.json'
    save(store, key, encoded(version))
    save(store, OriginalCache.key(binding), payload, 'application/pdf',
         {'sha256': binding['sha256'], 'kind': 'institution-original-proof'})
    return item, version, payload, key


class AdmittedTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.store = ReadOnlyRegistry()
        self.item, self.value, self.payload, self.key = fixture(self.store)
        self.cache = OriginalCache(self.store, 'private-test')
        PendingIntake(self.root/'pending.json', {}, now=NOW).admit(self.item, 7)
        self.pending = PendingIntake(self.root/'pending.json', {}, now=NOW)
        self.dest = self.root/self.value['binding']['source']

    def adapter(self):
        return a.AdmittedOriginals(cache_factory=lambda: self.cache)

    def restore(self, adapter=None, **kwargs):
        return (adapter or self.adapter()).restore(self.item, self.dest.name, self.pending, self.dest, 64*1024*1024, **kwargs)

    def mutate(self, change):
        value = copy.deepcopy(self.value); change(value)
        save(self.store, self.key, encoded(value))

    def test_exact_prior_original_reads_only_and_carries_validated_receipt(self):
        before = self.pending.path.read_bytes(); adapter = self.adapter()
        result = self.restore(adapter)
        self.assertEqual(self.dest.read_bytes(), self.payload)
        self.assertEqual(result['acquisition_method'], 'admitted_original_cache')
        row = dict(self.value['versions'][0], **result)
        row.pop('imf_live_download'); row.pop('binding_id')
        health.validate_resume(row)
        self.restore(adapter)
        self.assertEqual(len(self.store.lists), 1)
        self.assertEqual(self.store.puts, [])
        self.assertEqual(self.pending.path.read_bytes(), before)
        self.assertEqual(list(self.root.glob('.admitted-original-*')), [])

    def test_new_force_and_seen_sources_do_not_even_list_private_storage(self):
        for mode in ('new', 'force', 'downloaded', 'duplicate_pdf'):
            with self.subTest(mode=mode):
                self.pending.initial_keys = set() if mode == 'new' else {'imf:'+self.item['guid']}
                kwargs = dict(force=mode == 'force', seen={'imf:'+self.item['guid']: {'status': mode}})
                self.assertIsNone(self.restore(**kwargs))
        self.assertEqual(self.store.lists, [])
        self.assertEqual(self.store.gets, [])

    def test_changed_pending_identity_is_rejected_before_listing(self):
        for field in self.item:
            pending = copy.deepcopy(self.pending)
            pending.items['imf:'+self.item['guid']]['item'][field] = ['https://www.imf.org/-/media/files/publications/test.pdf'] if field == 'pdf_candidates' else 'changed'
            with self.subTest(field=field), self.assertRaisesRegex(a.AdmittedOriginalError, 'pending_identity'):
                self.adapter().restore(self.item, self.dest.name, pending, self.dest, 64*1024*1024)
        self.assertEqual(self.store.lists, [])

    def test_legacy_without_official_receipt_is_a_cache_miss(self):
        self.mutate(lambda value: value['versions'][0].pop('imf_live_download'))
        self.assertIsNone(self.restore())
        self.assertFalse(self.dest.exists())
        self.assertFalse(any(key.endswith('.pdf') for key in self.store.gets))

    def test_multiple_bindings_and_conflicting_publication_versions_are_never_selected(self):
        fixture(self.store, 2)
        with self.assertRaisesRegex(a.AdmittedOriginalError, 'ambiguous_binding'):
            self.restore()
        self.assertFalse(any(key.endswith('.pdf') for key in self.store.gets))
        self.store.objects = {key: value for key, value in self.store.objects.items()
                              if key in {self.key, OriginalCache.key(self.value['binding'])}}
        self.mutate(lambda value: value['versions'].append(dict(value['versions'][0], published='2026-10-14T00:00:00Z')))
        with self.assertRaisesRegex(a.AdmittedOriginalError, 'version_conflict'):
            self.restore()

    def test_corrupt_registry_receipt_and_source_bytes_fail_closed(self):
        cases = [lambda value: value['binding'].update(id='0'*64),
                 lambda value: value['versions'][0]['imf_live_download'].update(pdf_status=403),
                 lambda value: value['versions'][0]['imf_live_download'].update(source_guid='other'),
                 lambda value: value['versions'][0].update(title='Changed report'),
                 lambda value: value.update(receipts=[]),
                 lambda value: value['receipts'][0].update(run_id='local')]
        for change in cases:
            self.mutate(change)
            with self.subTest(change=change), self.assertRaises(a.AdmittedOriginalError): self.restore()
        save(self.store, self.key, encoded(self.value))
        original = self.store.objects[OriginalCache.key(self.value['binding'])]
        original['Body'] += b'changed'
        with self.assertRaisesRegex(a.AdmittedOriginalError, 'cache_invalid'): self.restore()
        self.assertFalse(self.dest.exists())

    def test_missing_cache_and_wrong_page_count_never_trigger_live_fetch(self):
        original_key = OriginalCache.key(self.value['binding'])
        original = self.store.objects.pop(original_key)
        with self.assertRaisesRegex(a.AdmittedOriginalError, 'cache_missing'): self.restore()
        self.store.objects[original_key] = original
        self.mutate(lambda value: value['versions'][0]['imf_live_download'].update(pages=3))
        with self.assertRaisesRegex(a.AdmittedOriginalError, 'page_count'): self.restore()

    def test_failed_registry_scan_is_not_repeated_for_each_source(self):
        adapter = self.adapter()
        with patch.object(self.store, 'list_objects_v2', side_effect=RuntimeError('synthetic unavailable')) as listing:
            for _ in range(2):
                with self.assertRaisesRegex(a.AdmittedOriginalError, 'registry_list'):
                    self.restore(adapter)
        self.assertEqual(listing.call_count, 1)
        self.assertEqual(adapter.audit['list_requests'], 1)

    def test_listing_requires_complete_unique_bounded_inventory(self):
        entry = dict(Key=self.key, Size=len(encoded(self.value)), ETag=digest(encoded(self.value)))
        cases = [dict(IsTruncated=True, Contents=[entry]),
                 dict(IsTruncated=False, Contents=[entry, entry]),
                 dict(IsTruncated=False, Contents=[dict(entry, Key=a.PREFIX+'unexpected.json')]),
                 dict(IsTruncated=False, Contents=[dict(entry, Size=True)]),
                 dict(IsTruncated=True, Contents=[], NextContinuationToken='repeated')]
        for response in cases:
            with self.subTest(response=response), patch.object(self.store, 'list_objects_v2', return_value=response):
                with self.assertRaises(a.AdmittedOriginalError): self.restore()
        with patch.object(a, 'MAX_REGISTRY_BYTES', 1), self.assertRaisesRegex(a.AdmittedOriginalError, 'registry_bound'):
            self.restore()

    def test_raw_metadata_bytes_are_bounded_before_get_and_listing_change_is_rejected(self):
        raw = encoded(self.value) + b' ' * 5000
        save(self.store, self.key, raw)
        with patch.object(a, 'MAX_REGISTRY_BYTES', len(encoded(self.value)) + 1000):
            with self.assertRaisesRegex(a.AdmittedOriginalError, 'registry_bound'):
                self.restore()
        self.assertEqual(self.store.gets, [])
        snapshot = self.store.list_objects_v2(Prefix=a.PREFIX)
        save(self.store, self.key, encoded(self.value))
        with patch.object(self.store, 'list_objects_v2', return_value=snapshot):
            with self.assertRaisesRegex(a.AdmittedOriginalError, 'registry_changed'):
                self.restore()

    def test_conflict_on_later_listing_page_cannot_be_missed(self):
        _, second, _, second_key = fixture(self.store, 2)
        first = dict(IsTruncated=True, NextContinuationToken='page2',
                     Contents=[dict(Key=self.key, Size=len(encoded(self.value)), ETag=digest(encoded(self.value)))])
        last = dict(IsTruncated=False, Contents=[dict(Key=second_key, Size=len(encoded(second)), ETag=digest(encoded(second)))])
        with patch.object(self.store, 'list_objects_v2', side_effect=[first, last]) as listing:
            with self.assertRaisesRegex(a.AdmittedOriginalError, 'ambiguous_binding'): self.restore()
            self.assertEqual(listing.call_count, 2)

    def invoke(self, *, sources=None, force=False, discovery_failure=False, live_success=False):
        class Clock(datetime):
            @classmethod
            def now(cls, tz=None): return NOW
        args = ['fetch', '--output-dir', str(self.root/'pdfs'), '--date', '261015', '--institutions', 'imf',
                '--seen-state-path', str(self.root/'seen.json'), '--archive-path', str(self.root/'archive.jsonl'),
                '--pending-intake-path', str(self.root/'pending.json'), '--since-days', '7',
                '--force-reprocess', str(force).lower()]
        def download_pdf(session, candidates, destination, *args, **kwargs):
            if live_success:
                destination.write_bytes(self.payload)
                return candidates[0], 'ok'
            return None, 'http_403'
        with (patch.object(f.sys, 'argv', args), patch.object(f, 'datetime', Clock),
              patch.dict(f.os.environ, {'INSTITUTION_ADMITTED_ORIGINALS': 'true', 'PROXY_SUBSCRIPTION_URL': '',
                                       'GITHUB_OUTPUT': '', 'GITHUB_STEP_SUMMARY': ''}),
              patch.object(f, 'collect_coveo_items', side_effect=ValueError('synthetic discovery failure') if discovery_failure else None,
                           return_value=copy.deepcopy(sources if sources is not None else [self.item])),
              patch.object(f, 'download_pdf', side_effect=download_pdf) as download,
              patch.object(f, 'http_get', side_effect=AssertionError('No live network')),
              patch.object(f, 'collect_coveo_preview_candidates', return_value=[]),
              patch.object(f, 'resolve_imf_ieo_followup', return_value=None),
              patch.object(a, '_cache', return_value=self.cache), redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO())):
            code = f.main()
        manifest = json.loads((self.root/'pdfs/institution_run_manifest.json').read_text())
        result = health.classify(manifest, producer_exit_code=code, log_exit_code=0, date_folder='261015', institutions='imf')
        return code, manifest, result, download.call_count

    def test_normal_retry_resumes_without_live_request_and_seen_commit_prevents_repost(self):
        code, manifest, result, calls = self.invoke()
        self.assertEqual((code, calls, result['source_health']), (0, 0, 'healthy'))
        self.assertEqual((manifest['source_checks'][0]['status'], result['source_health_admitted_resume_count'],
                          result['source_health_live_download_attempted']), ('resumed', '1', '0'))
        self.assertNotIn('imf_live_download', manifest['downloaded'][0])
        # Simulate downstream failure: provisional seen is not committed.
        (self.root/'seen.json').unlink()
        self.assertEqual(self.invoke()[1]['downloaded_count'], 1)
        gets = len(self.store.gets)
        # Simulate successful ordinary handoff retaining provisional seen.
        self.assertEqual(self.invoke()[1]['downloaded_count'], 0)
        self.assertEqual(len(self.store.gets), gets)
        self.assertEqual(json.loads((self.root/'pending.json').read_text())['items'], {})

    def test_corrupt_registry_refuses_reuse_and_live_failure_remains_visible(self):
        self.store.objects[self.key]['Metadata']['sha256'] = '0'*64
        code, manifest, result, calls = self.invoke()
        self.assertEqual((code, calls, result['source_health']), (2, 0, 'degraded'))
        self.assertEqual(manifest['downloaded_count'], 0)
        self.assertIn('admitted_original_registry_invalid', manifest['source_checks'][0]['error'])
        self.assertEqual(manifest['source_checks'][0]['admitted_resume_rejected_count'], 1)
        self.assertEqual(manifest['source_checks'][0]['live_download_attempted'], 1)
        self.assertIn('imf:'+self.item['guid'], json.loads((self.root/'pending.json').read_text())['items'])

    def test_unavailable_or_oversized_registry_does_not_block_successful_live_acquisition(self):
        self.item['pdf_candidates'] = ['https://www.imf.org/-/media/files/publications/wp/2026/english/synthetic.pdf']
        self.pending.items['imf:'+self.item['guid']]['item'] = copy.deepcopy(self.item)
        self.pending.save()
        for bound in (0, 2000):
            (self.root/'seen.json').unlink(missing_ok=True)
            with self.subTest(bound=bound), patch.object(a, 'MAX_RECORDS', bound):
                if bound:
                    self.store.objects[self.key]['Metadata']['sha256'] = '0'*64
                code, manifest, result, calls = self.invoke(live_success=True)
            self.assertEqual((code, manifest['downloaded_count'], result['source_health']), (0, 1, 'healthy'))
            self.assertGreater(calls, 0)
            self.assertEqual(manifest['source_checks'][0]['admitted_resume_count'], 0)
            self.assertEqual(manifest['source_checks'][0]['admitted_resume_rejected_count'], 1)
            self.assertNotIn('admitted_original_resume', manifest['downloaded'][0])

    def test_new_failure_beside_resumed_original_stays_degraded(self):
        fresh = copy.deepcopy(self.item); fresh.update(guid='new-report', title='New report',
            pdf_candidates=['https://www.imf.org/-/media/files/publications/wp/2026/english/synthetic.pdf'])
        code, manifest, result, calls = self.invoke(sources=[self.item, fresh])
        self.assertEqual((code, manifest['downloaded_count'], result['source_health']), (0, 1, 'degraded'))
        self.assertGreater(calls, 0)
        self.assertEqual((manifest['source_checks'][0]['admitted_resume_count'],
                          manifest['source_checks'][0]['live_download_attempted']), (1, 1))

    def test_discovery_failure_is_not_hidden_by_successful_resume(self):
        code, manifest, result, calls = self.invoke(discovery_failure=True)
        self.assertEqual((code, manifest['downloaded_count'], calls, result['source_health']), (0, 1, 0, 'degraded'))
        self.assertEqual(manifest['source_checks'][0]['status'], 'error')

    def test_resume_receipt_or_accounting_cannot_claim_unproved_success(self):
        _, manifest, _, _ = self.invoke()
        changes = [lambda value: value['downloaded'][0]['admitted_original_resume']['publication']['imf_live_download'].update(pdf_status=403),
                   lambda value: value['downloaded'][0].update(imf_live_download={}),
                   lambda value: value['downloaded'][0].update(admitted_original_unknown=True),
                   lambda value: value['source_checks'][0].update(admitted_resume_count=0),
                   lambda value: value['source_checks'][0].update(live_download_attempted=1),
                   lambda value: value['source_checks'][0].update(status='ok'),
                   lambda value: value.update(force_reprocess=True)]
        for change in changes:
            value = copy.deepcopy(manifest); change(value)
            with self.subTest(change=change), self.assertRaises(health.InvalidSourceHealth):
                health.classify(value, producer_exit_code=0, log_exit_code=0, date_folder='261015', institutions='imf')

    def test_read_only_canary_exercises_production_adapter_and_exact_source_bytes(self):
        from probe_institution_admitted_originals import run_probe, ReadOnlyR2
        selected = dict(item=self.item, binding=self.value['binding'], sha256=digest(self.payload),
                        size=len(self.payload), pages=2)
        wrapped = ReadOnlyR2(self.store)
        adapter = a.AdmittedOriginals(cache_factory=lambda: OriginalCache.single_attempt(wrapped, 'private-test'))
        result = run_probe([selected], self.pending, {}, adapter)
        self.assertEqual((result['status'], result['verified_count'], result['remote_writes']), ('success', 1, 0))
        self.assertEqual(result['sources'][0]['sha256'], digest(self.payload))
        self.assertEqual(result['registry']['registry_records'], 1)
        self.assertGreater(result['registry']['registry_bytes'], 0)
        self.assertFalse(hasattr(wrapped, 'put_object'))
        changed = dict(selected, sha256='0'*64)
        self.assertEqual(run_probe([changed], self.pending, {}, adapter)['status'], 'failure')

    def test_daily_workflow_enables_resume_after_seen_reset(self):
        workflow = (Path(__file__).resolve().parents[1]/'.github/workflows/institution-latest-pdf-to-wechat.yml').read_text()
        fetch = workflow.split('      - name: Fetch latest institution PDFs\n')[1].split('      - name:', 1)[0]
        self.assertIn('INSTITUTION_ADMITTED_ORIGINALS: "true"', fetch)
        self.assertNotIn('continue-on-error', fetch)


if __name__ == '__main__': unittest.main()
