"""Real primary CLI cache integration, without provider POSTs or model calls."""
from __future__ import annotations

import copy
import io
import json
import os
from pathlib import Path
import shutil
import sys
import tempfile
import unittest
from unittest.mock import patch

from consume_legacy_mineru import NetworkStop
import mineru_daily_result_cache as authentication_cache
import mineru_result_cache as c
import mineru_task_ledger as m
import pdf_to_xhs_batch as p
from test_mineru_completed_child_reuse import recovered_fixture, no_mutations
from test_mineru_result_cache import MemoryR2, result_zip


class Provider:
    def __init__(self, items):
        self.items = items; self.polls = []; self.states = ['done'] * len(items); self.signature = 'old'
    def submit(self, *args): raise AssertionError('An accepted task must not be resubmitted')
    def upload(self, *args): raise AssertionError('An accepted task must not be uploaded again')
    def poll(self, batch_id, token, timeout):
        self.polls.append(batch_id)
        return [{'data_id': item['id'], 'state': state,
                 **({'full_zip_url': 'https://results.invalid/' + item['id'] + '?Signature=' + self.signature}
                    if state == 'done' else {'err_code': 'TEST_FAILURE'} if state == 'failed' else {})}
                for item, state in zip(self.items, self.states)]


class DailyResultCacheTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name); self.input = self.root / 'pdfs'; self.input.mkdir()
        self.output = self.root / 'out'; self.r2 = MemoryR2()
        self.store = m.R2Store('dropbox', client=self.r2, bucket='private-test')
        self.ledger = m.Ledger(self.store, None, 'dropbox', 'https://mineru.net', c.OPTIONS,
                               [('MINER_U', 'test-private-token')])
        self.sources = []
        for index in range(3):
            import fitz
            path = self.input / f'original-{index}.pdf'
            with fitz.open() as document:
                document.new_page().insert_text((72, 72), 'Original ' + str(index))
                path.write_bytes(document.tobytes(no_new_id=True))
            self.sources.append((path.resolve(), path.name))
        self.items = [self.ledger.bind(*source) for source in self.sources]
        self.provider = Provider(self.items); self.ledger.provider = self.provider
        self.batch = {'schema': 1, 'key': 'batches/' + 'a' * 32, 'scope': 'dropbox',
                      'endpoint': 'https://mineru.net', 'options': c.OPTIONS,
                      'token_identity': next(iter(self.ledger.tokens)), 'files': self.items,
                      'state': 'terminal', 'batch_id': 'original-task-1'}
        self.store.put(self.batch['key'], self.batch)
        for item in self.items:
            self.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': self.batch['key']})
        self.originals = copy.deepcopy(self.r2.objects)
        self.downloads = []

    def downloader(self, url):
        self.downloads.append(url); return result_zip()

    def cache_objects(self):
        return {key: value for key, value in self.r2.objects.items() if key.startswith(c.PREFIX + '/')}

    def cli(self, downloader=None, pdfs=None):
        argv = ['primary', '--input-dir', str(self.input), '--output-dir', str(self.output), '--chart-source-only']
        with patch.object(sys, 'argv', argv), patch.dict(os.environ, {'MINER_U': 'test-private-token'}), \
             patch.object(p, 'from_environment', return_value=self.ledger), \
             patch.object(p, 'find_pdfs', return_value=[path for path, _ in self.sources] if pdfs is None else pdfs), \
             patch.object(p, 'download_once', side_effect=downloader or self.downloader), \
             patch.object(p, 'download_and_unzip', side_effect=AssertionError('R2/dropbox must use bound ZIP delivery')), \
             patch.object(p, 'create_chart_source_assets', return_value=[]), \
             patch.object(p, 'safe_generate_text', side_effect=AssertionError('Source mode must not call a model')), \
             patch.object(p, 'log'), patch('sys.stderr', new_callable=io.StringIO):
            return p.main()

    def context(self):
        rows = {path: {'data_id': item['id'], 'state': 'done', 'full_zip_url': 'https://results.invalid/source'}
                for (path, _), item in zip(self.sources, self.items)}
        cache, contexts = p.result_cache_contexts(self.ledger, self.sources, rows)
        return cache, contexts, rows

    def test_primary_cli_persists_every_complete_zip_before_releasing_sources(self):
        self.assertEqual(self.cli(), 0)
        self.assertEqual(len(self.cache_objects()), 6)
        self.assertEqual(len(self.downloads), 3)
        self.assertEqual({key: self.r2.objects[key] for key in self.originals}, self.originals)
        self.assertEqual(len(self.provider.polls), 1)
        self.assertFalse(list(self.output.rglob('*.zip')))
        self.assertEqual(len(list(self.output.rglob('source_mineru.md'))), 3)

    def test_primary_rerun_polls_original_task_but_uses_cached_bytes_after_signature_change(self):
        self.assertEqual(self.cli(), 0); shutil.rmtree(self.output)
        self.provider.signature = 'new'
        def expired(url): raise NetworkStop('tls_certificate_expired')
        self.assertEqual(self.cli(downloader=expired), 0)
        self.assertEqual(len(self.downloads), 3)
        self.assertEqual(len(self.provider.polls), 2)
        self.assertEqual({key: self.r2.objects[key] for key in self.originals}, self.originals)

    def test_primary_cache_never_bypasses_failed_unselected_original_member(self):
        self.assertEqual(self.cli(), 0); shutil.rmtree(self.output)
        self.provider.states = ['done', 'done', 'failed']
        def no_download(url): self.fail('Original member failure blocks source release even with cache')
        self.assertEqual(self.cli(downloader=no_download, pdfs=[self.sources[0][0]]), 2)
        self.assertFalse(list(self.output.rglob('source_mineru.md')))
        self.assertEqual(len(self.downloads), 3)

    def test_primary_reuses_completed_children_and_their_exact_cached_zips_without_paid_requests(self):
        fixture = recovered_fixture(self.root, third=True)
        self.ledger, self.store, self.r2, self.provider = fixture.ledger, fixture.store, fixture.r2, fixture.provider
        self.sources, self.items = fixture.sources, fixture.items
        rows, _ = p.reuse_completed_children(self.ledger, self.sources, fixture.results, fixture.summary)
        cache, contexts = p.result_cache_contexts(self.ledger, self.sources, dict(rows))
        payload = result_zip()
        for path, _ in rows:
            cache.put(*contexts[path], payload)
        before = copy.deepcopy(self.r2.objects)
        def no_download(_url): self.fail('Recovered child must reuse its own cached ZIP')
        with no_mutations(fixture), patch.object(self.r2, 'put_object', side_effect=AssertionError('No R2 write')):
            self.assertEqual(self.cli(downloader=no_download), 0)
        self.assertEqual(self.r2.objects, before)
        summary = json.loads((self.output / 'mineru_attempts_summary.json').read_text())
        self.assertEqual((summary['original_batches'][0]['failed'], summary['failed']), (2, 0))
        self.assertEqual(summary['completed_child_reuse']['reused_sources'], 2)
        self.assertTrue(summary['ready_for_generation'])
        self.assertEqual(len(list(self.output.rglob('source_mineru.md'))), 3)

    def test_primary_pending_child_does_not_release_sources_or_create_new_task(self):
        fixture = recovered_fixture(self.root)
        self.ledger, self.store, self.r2, self.provider = fixture.ledger, fixture.store, fixture.r2, fixture.provider
        self.sources = fixture.sources
        key = fixture.control['children'][0]['key']
        child, version = self.store.get(key); child['state'] = 'uploaded'
        self.store.put(key, child, version)
        self.provider.plans[1] = ['running', 'running']
        with no_mutations(fixture):
            self.assertEqual(self.cli(), 2)
        self.assertFalse(list(self.output.rglob('source_mineru.md')))
        self.assertEqual(self.downloads, [])

    def test_primary_first_source_cache_survives_next_tls_failure_and_stops_later_downloads(self):
        attempts = []
        def partial(url):
            attempts.append(url)
            if len(attempts) == 2: raise NetworkStop('tls_certificate_expired')
            return result_zip()
        self.assertEqual(self.cli(downloader=partial), 2)
        self.assertEqual(len(attempts), 2); self.assertEqual(len(self.cache_objects()), 2)
        first = attempts[0]; rerun = []
        def resumed(url):
            self.assertNotEqual(url, first); rerun.append(url); return result_zip()
        self.assertEqual(self.cli(downloader=resumed), 0)
        self.assertEqual(len(rerun), 2); self.assertEqual(len(self.cache_objects()), 6)

    def test_corrupt_primary_cache_stops_without_cdn_fallback_or_later_sources(self):
        self.assertEqual(self.cli(), 0); shutil.rmtree(self.output)
        cache, contexts, _ = self.context()
        binding, lineage = contexts[self.sources[0][0]]
        key = cache.receipt_key(c.identity(binding, lineage))
        self.r2.objects[key]['Body'] += b'tampered'
        def no_download(url): self.fail('Cache corruption cannot fall back to provider download')
        self.assertEqual(self.cli(downloader=no_download), 2)
        self.assertFalse(list(self.output.rglob('source_mineru.md')))

    def test_claim_and_provider_row_data_id_must_match_original_pdf(self):
        _, _, rows = self.context()
        rows[self.sources[0][0]]['data_id'] = self.items[1]['id']
        with self.assertRaisesRegex(c.ResultCacheError, 'cache_original_task'):
            p.result_cache_contexts(self.ledger, self.sources, rows)

    def test_source_change_after_context_rejects_cache_or_download_before_model(self):
        cache, contexts, rows = self.context()
        path = self.sources[0][0]; path.write_bytes(b'%PDF-changed')
        args = p.build_arg_parser().parse_args(['--chart-source-only'])
        args._mineru_result_cache, args._mineru_result_contexts = cache, contexts
        with patch.object(p, 'download_once') as download, self.assertRaisesRegex(c.ResultCacheError, 'cache_source_changed'):
            p.process_pdf(path, rows[path], self.output, args)
        download.assert_not_called(); self.assertEqual(self.cache_objects(), {})

    def test_cache_is_persisted_before_any_paid_generation_attempt(self):
        cache, contexts, rows = self.context()
        args = p.build_arg_parser().parse_args(['--no-wechat-title-refine'])
        args._mineru_result_cache, args._mineru_result_contexts = cache, contexts
        def model(*values, **kwargs):
            self.assertEqual(len(self.cache_objects()), 2)
            raise RuntimeError('model failure after source is saved')
        path = self.sources[0][0]
        with patch.object(p, 'download_once', side_effect=self.downloader), \
             patch.object(p, 'create_visual_assets', return_value=[]), patch.object(p, 'safe_generate_text', side_effect=model), \
             self.assertRaisesRegex(RuntimeError, 'model failure after source is saved'):
            p.process_pdf(path, rows[path], self.output, args)

    def test_local_and_other_cloud_scopes_keep_existing_delivery_behavior(self):
        local = m.Ledger(m.FileStore(self.root / 'local'), None, 'local', 'https://mineru.net', c.OPTIONS,
                         [('MINER_U', 'test')])
        consulting = m.Ledger(m.R2Store('consulting', client=self.r2, bucket='private-test'), None,
                              'consulting', 'https://mineru.net', c.OPTIONS, [('MINER_U', 'test')])
        institution = m.Ledger(m.R2Store('institution', client=self.r2, bucket='private-test'), None,
                               'institution', 'https://mineru.net', dict(c.OPTIONS, language='ch'), [('MINER_U', 'test')])
        for ledger in (local, consulting, institution):
            with self.subTest(scope=ledger.scope):
                self.assertEqual(p.result_cache_contexts(ledger, self.sources, {}), (None, {}))

    def test_recovered_zip_has_private_authentication_readback_before_result_release(self):
        # Transport policy/lease is tested by the transport suite. Here exercise
        # the real CLI, original task ledger, immutable R2 writes and source release.
        auth = {'test_verified_authentication': 'first-lease'}
        payload = result_zip()
        with patch.object(p, 'download_result', return_value=(payload, auth)) as download, \
             patch.object(authentication_cache, 'validate_daily_authentication', return_value=auth):
            self.assertEqual(self.cli(), 0)
        self.assertEqual(download.call_count, 3)
        receipts = [row for row in self.r2.puts if row['Key'].startswith(authentication_cache.AUTH_PREFIX + '/')]
        self.assertEqual(len(receipts), 3)
        for row in receipts:
            proof = json.loads(row['Body'])
            identity_sha = proof['identity_sha256']
            self.assertEqual(proof['policy'], 'daily-exact-leaf-result-cache-v1')
            self.assertEqual(proof['zip_sha256'], m.digest(payload))
            self.assertEqual(proof['authentication'], auth)
            self.assertIn(row['Key'], self.r2.gets)
            writes = [item['Key'] for item in self.r2.puts]
            self.assertLess(writes.index(row['Key']), writes.index(c.ResultCache.receipt_key(identity_sha)))
        shutil.rmtree(self.output)
        with patch.object(p, 'download_result', side_effect=AssertionError('Complete cache must not reconnect')):
            self.assertEqual(self.cli(), 0)
        self.assertEqual(len(self.provider.polls), 2)

    def test_authentication_write_failure_never_releases_zip_or_model_input(self):
        auth = {'test_verified_authentication': 'first-lease'}
        def fail_auth(key, _):
            if key.startswith(authentication_cache.AUTH_PREFIX + '/'):
                raise OSError('private storage write failed')
        self.r2.before_put = fail_auth
        with patch.object(p, 'download_result', return_value=(result_zip(), auth)), \
             patch.object(authentication_cache, 'validate_daily_authentication', return_value=auth):
            self.assertEqual(self.cli(), 2)
        self.assertEqual(self.cache_objects(), {})
        self.assertFalse(list(self.output.rglob('source_mineru.md')))

    def test_invalid_recovered_zip_is_rejected_before_authentication_write(self):
        with patch.object(p, 'download_result', return_value=(b'incomplete archive', {'test': True})), \
             patch.object(authentication_cache, 'validate_daily_authentication') as validation:
            self.assertEqual(self.cli(), 2)
        validation.assert_not_called()
        self.assertFalse(any(key.startswith(authentication_cache.AUTH_PREFIX + '/') for key in self.r2.objects))
        self.assertFalse(list(self.output.rglob('source_mineru.md')))

    def test_interrupted_attempt_authentication_does_not_conflict_with_a_fresh_lease(self):
        cache, contexts, _ = self.context()
        binding, lineage = contexts[self.sources[0][0]]
        for lease in ('earlier', 'fresh'):
            auth = {'test_verified_authentication': lease}
            with patch.object(authentication_cache, 'validate_daily_authentication', return_value=auth):
                authentication_cache.persist_authentication(cache, binding, lineage, result_zip(), auth)
        proofs = [key for key in self.r2.objects if key.startswith(authentication_cache.AUTH_PREFIX + '/')]
        self.assertEqual(len(proofs), 2)
        self.assertIsNone(cache.get(binding, lineage))


if __name__ == '__main__':
    unittest.main()
