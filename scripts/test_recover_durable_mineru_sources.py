"""Offline exact-source, complete-batch and private-handoff regressions."""
from __future__ import annotations
import copy
import io
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import zipfile

import mineru_task_ledger as m
import recover_durable_mineru_sources as r
from consume_legacy_mineru import NetworkStop
from mineru_result_cache import ResultCache, ResultCacheError
from test_mineru_result_cache import MemoryR2


def result_zip():
    buffer = io.BytesIO()
    with zipfile.ZipFile(buffer, 'w') as archive:
        archive.writestr('full.md', '# Original report\nVerified source revenue 125.50.\n')
    return buffer.getvalue()


def assets(raw_dir, asset_dir, maximum):
    (asset_dir.parent / 'source_image_map.json').write_bytes(m.encoded({
        'version': 1, 'source_sha256': m.digest((raw_dir / 'full.md').read_bytes()), 'images': {}}))
    return []


class Provider:
    def __init__(self):
        self.tasks, self.plans, self.posts, self.polls, self.events = {}, {}, [], [], []
    def submit(self, items, options, token, timeout):
        batch_id = 'child-' + str(len(self.posts) + 1)
        self.posts.append(copy.deepcopy(items)); self.events.append('post')
        self.tasks[batch_id] = copy.deepcopy(items)
        return batch_id, ['https://upload.invalid/' + item['id'] for item in items]
    def upload(self, url, raw, timeout):
        pass
    def poll(self, batch_id, token, timeout):
        self.polls.append(batch_id); self.events.append('get:' + batch_id)
        states = self.plans.get(batch_id, ['done'] * len(self.tasks[batch_id]))
        return [{'data_id': item['id'], 'state': state,
                 **({'full_zip_url': 'https://results.invalid/' + batch_id + '/' + item['id']} if state == 'done'
                    else {'err_code': 'TEST_TRANSIENT', 'err_msg': 'test temporary failure'} if state == 'failed' else {})}
                for item, state in zip(self.tasks[batch_id], states)]


class RecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input = self.root / 'input'; self.input.mkdir()
        self.output = self.root / 'output'
        self.store = m.FileStore(self.root / 'ledger'); self.provider = Provider()
        self.ledger = m.Ledger(self.store, self.provider, 'dropbox', 'https://mineru.net', r.OPTIONS,
                               [('MINER_U', 'private-token')], sleep=lambda seconds: None)
        self.rows = []
        for index in range(7):
            name = f'{index + 1:02d}-report-{index}.pdf'
            raw = b'%PDF-1.4 test source ' + str(index).encode()
            (self.input / name).write_bytes(raw)
            self.rows.append({'process_local_path': '_selected/' + name, 'content_sha256': m.digest(raw),
                              'dropbox_path': '/zip_backup/261003/report-' + str(index) + '.pdf',
                              'name': 'Original report ' + str(index) + '.pdf'})
        self.manifest = self.input / r.MANIFEST; self.save_manifest()
        self.pairs = [(self.input / Path(row['process_local_path']).name,
                       Path(row['process_local_path']).name) for row in self.rows]
        self.originals = []
        # Deliberately interleaved original groups. New sequential five-file
        # slicing would be incorrect and must never create extra submissions.
        for number, indices in enumerate(([0, 2, 4], [1, 3, 5, 6]), 1):
            items = [self.ledger.bind(*self.pairs[index]) for index in indices]
            key, batch_id = 'batches/' + str(number) * 32, 'root-' + str(number)
            batch = {'schema': 1, 'key': key, 'scope': 'dropbox', 'endpoint': 'https://mineru.net',
                     'options': r.OPTIONS, 'token_identity': next(iter(self.ledger.tokens)),
                     'files': items, 'state': 'accepted', 'batch_id': batch_id}
            self.store.put(key, batch)
            for item in items:
                self.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': key})
            self.provider.tasks[batch_id] = items; self.originals.append(batch)
        self.downloads = []
    def save_manifest(self):
        self.manifest.write_bytes(m.encoded(self.rows))
    def downloader(self, url):
        self.downloads.append(url); self.provider.events.append('zip')
        return result_zip()
    def recover(self, **kwargs):
        values = dict(source_run_id='123', recovery_run_id='456', source_execution_sha='a' * 40,
                      allowed_error_codes=['TEST_TRANSIENT'], downloader=self.downloader, asset_writer=assets,
                      timeout=2, interval=1, queue_budget=0)
        values.update(kwargs)
        return r.recover_sources(self.ledger, self.input, self.manifest, self.output, len(self.rows), '261003', **values)
    def validate(self):
        return r.validate_sources(self.output, len(self.rows), '261003')
    def rewrite_receipt(self, change, refresh_files=False):
        path = self.output / r.RECEIPT; receipt = json.loads(path.read_bytes()); change(receipt)
        if refresh_files:
            receipt['files'] = r.regular_inventory(self.output)
        path.write_bytes(m.encoded(receipt))
    def test_complete_done_originals_use_no_post_and_keep_every_original_claim_byte(self):
        before = {str(path.relative_to(self.store.root)): path.read_bytes() for path in self.store.root.rglob('*.json')}
        receipt = self.recover()
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 0))
        self.assertEqual(self.provider.posts, [])
        self.assertEqual(before, {str(path.relative_to(self.store.root)): path.read_bytes() for path in self.store.root.rglob('*.json')})
        self.assertEqual(len(self.downloads), 7)
        self.assertEqual(len(self.validate()['reports']), 7)
        self.assertFalse(list(self.output.rglob('*.zip')))
        self.assertFalse(list(self.output.rglob('mineru_raw')))
    def test_persistent_cache_hit_survives_changed_signed_urls_and_broken_cdn(self):
        cache = ResultCache(MemoryR2(), 'private-test')
        before = {str(path.relative_to(self.store.root)): path.read_bytes() for path in self.store.root.rglob('*.json')}
        self.recover(result_cache=cache)
        __import__('shutil').rmtree(self.output)
        original = self.provider.poll
        def different_signature(batch_id, token, timeout):
            values = original(batch_id, token, timeout)
            for value in values:
                if 'full_zip_url' in value: value['full_zip_url'] += '?Expires=999&Signature=changed'
            return values
        self.provider.poll = different_signature
        def broken(url): raise NetworkStop('tls_certificate_expired')
        polls = len(self.provider.polls)
        receipt = self.recover(result_cache=cache, downloader=broken)
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 0))
        self.assertGreater(len(self.provider.polls), polls)
        self.assertEqual(len(self.downloads), 7)
        self.assertEqual(before, {str(path.relative_to(self.store.root)): path.read_bytes() for path in self.store.root.rglob('*.json')})
        self.validate()
    def test_first_verified_zip_is_retained_when_next_cdn_download_fails(self):
        r2 = MemoryR2(); cache = ResultCache(r2, 'private-test')
        attempts = []
        def partial(url):
            attempts.append(url)
            if len(attempts) == 2: raise NetworkStop('tls_certificate_expired')
            return result_zip()
        with self.assertRaises(NetworkStop): self.recover(result_cache=cache, downloader=partial)
        self.assertFalse(self.output.exists()); self.assertEqual(self.provider.posts, [])
        self.assertEqual(len(r2.objects), 2)
        first = attempts[0]
        rerun_downloads = []
        def restored(url):
            if url == first: self.fail('Already verified source must not use CDN again')
            rerun_downloads.append(url); return result_zip()
        receipt = self.recover(result_cache=cache, downloader=restored)
        self.assertEqual(len(rerun_downloads), 6)
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 0))
        self.validate()
    def test_cached_bytes_never_admit_truncated_original_provider_membership(self):
        cache = ResultCache(MemoryR2(), 'private-test'); self.recover(result_cache=cache)
        __import__('shutil').rmtree(self.output)
        self.provider.plans['root-2'] = ['done']
        with self.assertRaises((r.RecoveryError, m.LedgerError)):
            self.recover(result_cache=cache, timeout=0.01)
        self.assertEqual(self.provider.posts, []); self.assertFalse(self.output.exists())
    def test_corrupt_cache_never_falls_back_to_cdn_or_recovery_post(self):
        r2 = MemoryR2(); cache = ResultCache(r2, 'private-test'); self.recover(result_cache=cache)
        __import__('shutil').rmtree(self.output)
        first_binding = self.originals[0]['files'][0]
        lineage = r.TerminalRecovery._lineage({'data_id': first_binding['id']}, self.originals[0], self.originals[0], 0)['_recovery_lineage']
        from mineru_result_cache import identity
        key = cache.receipt_key(identity(first_binding, lineage))
        r2.objects[key]['Body'] += b'tampered'
        def no_download(url): self.fail('Corrupt cache must stop, not download again')
        with self.assertRaises(ResultCacheError): self.recover(result_cache=cache, downloader=no_download)
        self.assertEqual(self.provider.posts, []); self.assertFalse(self.output.exists())
    def test_failed_members_only_children_can_populate_distinct_cache_entries(self):
        cache = ResultCache(MemoryR2(), 'private-test')
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        receipt = self.recover(result_cache=cache)
        self.assertEqual(receipt['provider_posts'], 1)
        self.assertEqual(len(cache.client.objects), 14)
        __import__('shutil').rmtree(self.output)
        def broken(url): raise NetworkStop('tls_certificate_expired')
        receipt = self.recover(result_cache=cache, downloader=broken)
        self.assertEqual(receipt['provider_posts'], 0)
        self.assertEqual(len(self.provider.posts), 1); self.validate()
    def test_fresh_result_lineage_is_bound_before_persistent_cache_write(self):
        __import__('shutil').rmtree(self.store.root / 'sources')
        cache = ResultCache(MemoryR2(), 'private-test')
        receipt = self.recover(result_cache=cache, source_run_id='', allow_fresh=True)
        self.assertEqual((receipt['report_count'], receipt['provider_posts']), (7, 2))
        self.assertEqual(len(cache.client.objects), 14); self.validate()
    def test_failed_members_only_are_recovered_after_all_original_gets_and_zip_downloads(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        self.provider.plans['root-2'] = ['done', 'done', 'failed', 'done']
        receipt = self.recover()
        self.assertEqual(receipt['provider_posts'], 2)
        self.assertEqual([len(items) for items in self.provider.posts], [1, 1])
        first_post = self.provider.events.index('post')
        preceding = self.provider.events[:first_post]
        self.assertIn('get:root-1', preceding); self.assertIn('get:root-2', preceding)
        self.assertEqual(preceding.count('zip'), 5)
        self.assertEqual(sum(report['task']['child_ordinal'] == 1 for report in receipt['reports']), 2)
        self.validate()
    def test_tls_failure_stops_before_any_recovery_post_or_output(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        def fail(url):
            raise NetworkStop('tls_certificate_expired')
        with self.assertRaises(NetworkStop): self.recover(downloader=fail)
        self.assertEqual(self.provider.posts, []); self.assertFalse(self.output.exists())
    def test_bad_zip_stops_before_any_recovery_post(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        with self.assertRaises(Exception): self.recover(downloader=lambda url: b'not a ZIP')
        self.assertEqual(self.provider.posts, []); self.assertFalse(self.output.exists())
    def test_missing_claim_from_original_run_never_becomes_fresh(self):
        claim = self.store._path('sources/' + self.originals[0]['files'][0]['id']); claim.unlink()
        with self.assertRaisesRegex(r.RecoveryError, 'missing_original_claim'): self.recover(allow_fresh=True)
        self.assertEqual(self.provider.posts, [])
    def test_entirely_missing_claims_require_empty_source_run_and_explicit_fresh(self):
        shutil = __import__('shutil'); shutil.rmtree(self.store.root / 'sources')
        with self.assertRaises(r.RecoveryError): self.recover(source_run_id='')
        with self.assertRaises(r.RecoveryError): self.recover(allow_fresh=True)
        receipt = self.recover(source_run_id='', allow_fresh=True)
        self.assertEqual([len(items) for items in self.provider.posts], [5, 2])
        self.assertEqual(receipt['provider_posts'], 2); self.validate()
    def test_mixed_existing_and_fresh_never_posts(self):
        self.store._path('sources/' + self.originals[1]['files'][0]['id']).unlink()
        with self.assertRaises(r.RecoveryError): self.recover(source_run_id='', allow_fresh=True)
        self.assertEqual(self.provider.posts, [])
    def test_original_subset_cannot_escape_failed_neighbor(self):
        self.rows = self.rows[:1]; self.save_manifest()
        for path in list(self.input.glob('*.pdf')):
            if path != self.pairs[0][0]: path.unlink()
        with self.assertRaisesRegex(r.RecoveryError, 'original_task_inventory'): self.recover()
        self.assertEqual(self.provider.posts, [])
    def test_unapproved_terminal_failure_never_posts(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        with self.assertRaises(m.LedgerError): self.recover(allowed_error_codes=[])
        self.assertEqual(self.provider.posts, [])
    def test_unapproved_failure_in_later_original_group_blocks_all_children(self):
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        self.provider.plans['root-2'] = ['done', 'failed', 'done', 'done']
        original = self.provider.poll
        def different_error(batch_id, token, timeout):
            values = original(batch_id, token, timeout)
            if batch_id == 'root-2':
                for value in values:
                    if value['state'] == 'failed': value['err_code'] = 'NOT_ALLOWED'
            return values
        self.provider.poll = different_error
        with self.assertRaises(m.LedgerError): self.recover()
        self.assertEqual(self.provider.posts, [])
    def test_truncated_original_get_never_posts(self):
        self.provider.plans['root-2'] = ['done']
        with self.assertRaises((r.RecoveryError, m.LedgerError)): self.recover(timeout=0.01)
        self.assertEqual(self.provider.posts, [])
    def test_exact_manifest_hash_and_pdf_inventory_enforced(self):
        self.pairs[0][0].write_bytes(b'%PDF-tampered')
        with self.assertRaisesRegex(r.RecoveryError, 'input_pdf_hash'): self.recover()
        self.assertEqual(self.provider.polls, [])
    def test_extra_original_pdf_rejected(self):
        (self.input / 'extra.pdf').write_bytes(b'%PDF-extra')
        with self.assertRaisesRegex(r.RecoveryError, 'input_inventory'): self.recover()
    def test_manifest_date_mismatch_rejected(self):
        self.rows[0]['dropbox_path'] = '/zip_backup/261002/report.pdf'; self.save_manifest()
        with self.assertRaisesRegex(r.RecoveryError, 'manifest_date'): self.recover()
    def test_distinct_original_names_with_duplicate_pdf_content_are_preserved(self):
        # Rebuild isolated fresh claims, preserving both manifest bindings.
        __import__('shutil').rmtree(self.store.root / 'sources')
        self.pairs[1][0].write_bytes(self.pairs[0][0].read_bytes())
        self.rows[1]['content_sha256'] = self.rows[0]['content_sha256']; self.save_manifest()
        receipt = self.recover(source_run_id='', allow_fresh=True)
        self.assertEqual(len(receipt['reports']), 7); self.validate()
    def test_symlink_input_rejected(self):
        source = self.pairs[0][0]; target = self.root / 'actual.pdf'; source.rename(target); source.symlink_to(target)
        with self.assertRaisesRegex(r.RecoveryError, 'input_symlink'): self.recover()
    def test_ambiguous_original_task_blocks_all_posts(self):
        batch = self.originals[0]; _, version = self.store.get(batch['key'])
        batch['state'] = 'submitting'; self.store.put(batch['key'], batch, version)
        with self.assertRaisesRegex(r.RecoveryError, 'original_task_not_accepted'): self.recover()
        self.assertEqual(self.provider.posts, [])
    def test_receipt_rejects_source_markdown_tampering(self):
        self.recover(); next(self.output.rglob('source_mineru.md')).write_bytes(b'changed source')
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_rejects_status_tampering_even_with_refreshed_inventory(self):
        self.recover(); path = next(self.output.rglob('status.json'))
        status = json.loads(path.read_bytes()); status['original_pdf_sha256'] = 'f' * 64
        path.write_bytes(m.encoded(status)); self.rewrite_receipt(lambda receipt: None, refresh_files=True)
        with self.assertRaisesRegex(r.RecoveryError, 'report_status'): self.validate()
    def test_receipt_rejects_extra_file(self):
        self.recover(); (self.output / 'extra.txt').write_text('extra')
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_rejects_nested_receipt_named_extra_file(self):
        self.recover(); folder = self.output / 'extra'; folder.mkdir()
        (folder / r.RECEIPT).write_text('{}')
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_rejects_source_identity_rebinding(self):
        self.recover(); self.rewrite_receipt(lambda receipt: receipt['reports'][0]['source_binding'].__setitem__('size', 999))
        with self.assertRaisesRegex(r.RecoveryError, 'receipt_source_binding'): self.validate()

    def test_default_writer_receives_each_frozen_original_path_and_hash(self):
        calls = []
        def create(raw_dir, assets_dir, maximum, **kwargs):
            calls.append(kwargs)
            return assets(raw_dir, assets_dir, maximum)
        with patch('pdf_to_xhs_batch.create_chart_source_assets', side_effect=create):
            self.recover(asset_writer=r.chart_assets)
        self.assertEqual(len(calls), 7)
        for (path, _), row, call in zip(self.pairs, self.rows, calls):
            self.assertEqual(call['auth_original_pdf'], path)
            self.assertEqual(call['original_pdf_sha256'], row['content_sha256'])
            self.assertEqual(m.digest(path.read_bytes()), call['original_pdf_sha256'])
            self.assertEqual(call['markdown_sha256'], m.digest(b'# Original report\nVerified source revenue 125.50.\n'))
        self.validate()

    def test_rehashed_invalid_optional_figure_sidecar_is_rejected(self):
        self.recover()
        directory = next(self.output.glob('report_*'))
        (directory / 'source_figure_map.json').write_bytes(b'[]')
        self.rewrite_receipt(lambda _: None, refresh_files=True)
        with self.assertRaisesRegex(r.RecoveryError, 'report_figure_source'): self.validate()

    def test_declared_figure_sidecar_cannot_disappear_or_be_null(self):
        self.recover()
        directory = next(self.output.glob('report_*')); path = directory / 'status.json'
        status = json.loads(path.read_bytes())
        for name, sha in [('source_figure_map.json', 'a' * 64), (None, None)]:
            status.update(source_figure_map=name, source_figure_map_sha256=sha)
            path.write_bytes(m.encoded(status)); self.rewrite_receipt(lambda _: None, refresh_files=True)
            with self.subTest(name=name), self.assertRaisesRegex(r.RecoveryError, 'report_figure_source'): self.validate()
    def test_receipt_rejects_missing_file(self):
        self.recover(); next(self.output.rglob('source_image_map.json')).unlink()
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_rejects_wrong_date_or_count(self):
        self.recover()
        for count, date in ((6, '261003'), (7, '261002')):
            with self.assertRaises(r.RecoveryError): r.validate_sources(self.output, count, date)
    def test_receipt_rejects_duplicate_source_coverage(self):
        self.recover(); self.rewrite_receipt(lambda receipt: receipt['reports'].__setitem__(1, copy.deepcopy(receipt['reports'][0])))
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_rejects_wrong_task_data_id(self):
        self.recover(); self.rewrite_receipt(lambda receipt: receipt['reports'][0]['task'].__setitem__('data_id', 'f' * 64))
        with self.assertRaises(r.RecoveryError): self.validate()
    def test_receipt_binds_the_consumer_requested_recovery_run(self):
        self.recover()
        self.assertEqual(r.validate_sources(self.output, 7, '261003', expected_recovery_run_id='456')['recovery_run_id'], '456')
        with self.assertRaisesRegex(r.RecoveryError, 'receipt_recovery_run'):
            r.validate_sources(self.output, 7, '261003', expected_recovery_run_id='999')
    def test_receipt_separates_original_and_recovery_execution_hashes(self):
        receipt = self.recover(recovery_execution_sha='b' * 40)
        self.assertEqual(receipt['source_execution_sha'], 'a' * 40)
        self.assertEqual(receipt['recovery_execution_sha'], 'b' * 40)
        r.validate_sources(self.output, 7, '261003', expected_execution_sha='b' * 40)
        with self.assertRaisesRegex(r.RecoveryError, 'receipt_execution_sha'):
            r.validate_sources(self.output, 7, '261003', expected_execution_sha='a' * 40)
    def test_receipt_rejects_wrong_image_count_with_refreshed_inventory(self):
        self.recover(); path = next(self.output.rglob('status.json'))
        status = json.loads(path.read_bytes()); status['chart_source_image_count'] = 1
        path.write_bytes(m.encoded(status)); self.rewrite_receipt(lambda receipt: None, refresh_files=True)
        with self.assertRaisesRegex(r.RecoveryError, 'report_status'): self.validate()
    def test_receipt_rejects_nonobject_image_map_with_refreshed_inventory(self):
        self.recover(); next(self.output.rglob('source_image_map.json')).write_bytes(b'[]')
        self.rewrite_receipt(lambda receipt: None, refresh_files=True)
        with self.assertRaisesRegex(r.RecoveryError, 'report_image_map'): self.validate()
    @unittest.skipUnless(all(importlib.util.find_spec(name) for name in ('PIL', 'fitz', 'requests')),
                         'Cloud image dependencies are unavailable in this offline test environment')
    def test_real_png_zip_retains_source_bytes_and_aliases_through_private_archive(self):
        from PIL import Image, ImageDraw
        from private_workflow_handoff import create_archive, extract_archive
        chart = Image.new('RGB', (800, 500), 'white'); draw = ImageDraw.Draw(chart)
        for x in range(0, 800, 20):
            draw.line((x, 0, 800 - x, 500), fill='blue', width=3)
        image_buffer = io.BytesIO(); chart.save(image_buffer, format='PNG'); png = image_buffer.getvalue()
        markdown = '# Original report\n\nFigure 1: revenue\n![](images/原始 chart.png)\n'.encode('utf-8')
        buffer = io.BytesIO()
        with zipfile.ZipFile(buffer, 'w') as archive:
            archive.writestr('payload/full.md', markdown)
            archive.writestr('payload/images/原始 chart.png', png)
        self.recover(downloader=lambda url: buffer.getvalue(), asset_writer=r.chart_assets)
        report = next(self.output.glob('report_*'))
        self.assertEqual((report / 'source_mineru.md').read_bytes(), markdown)
        self.assertEqual((report / 'assets/source_image_01.png').read_bytes(), png)
        mapping = json.loads((report / 'source_image_map.json').read_bytes())
        self.assertEqual(mapping['images']['images/原始 chart.png'], 'assets/source_image_01.png')
        packed = self.root / 'handoff.tar.gz'; restored = self.root / 'restored'
        create_archive(self.output, packed); extract_archive(packed, restored)
        r.validate_sources(restored, 7, '261003', expected_recovery_run_id='456')
        self.assertEqual((restored / report.name / 'assets/source_image_01.png').read_bytes(), png)
    def test_producer_is_exact_daily_main_run_and_repository(self):
        producer = {'id': 123, 'path': r.PRODUCER, 'head_branch': 'main', 'head_sha': 'a' * 40,
                    'repository': {'full_name': 'owner/repo'}}
        self.assertEqual(r.check_producer(producer, '123', 'owner/repo'), 'a' * 40)
        for field, value in (('path', '.github/workflows/other.yml'), ('head_branch', 'feature'), ('id', 999)):
            bad = dict(producer, **{field: value})
            with self.assertRaises(r.RecoveryError): r.check_producer(bad, '123', 'owner/repo')
    def test_cli_rejects_non_main_before_network_or_credentials(self):
        with patch.dict('os.environ', {'GITHUB_EVENT_NAME': 'pull_request'}, clear=True), \
             patch('sys.argv', ['recover', 'recover', '--output-dir', str(self.output), '--expected-reports', '7',
                                '--date-folder', '261003', '--input-dir', str(self.input)]), \
             patch('sys.stderr', new_callable=io.StringIO) as stderr:
            self.assertEqual(r.main(), 2)
            self.assertIn('reviewed_main_workflow_required', stderr.getvalue())

    def test_cached_originals_then_child_network_failure_is_classified_and_accepted_child_retained(self):
        cache = ResultCache(MemoryR2(), 'private-test')
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        for root in self.originals:
            for offset, binding in enumerate(root['files']):
                if root['batch_id'] == 'root-1' and offset == 1:
                    continue
                lineage = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                           'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
                cache.put(binding, lineage, result_zip())
        downloads = []
        def unavailable_child(url):
            downloads.append(url)
            raise NetworkStop('network_stop')
        with self.assertRaises(m.LedgerError) as stopped:
            self.recover(result_cache=cache, downloader=unavailable_child)
        self.assertEqual(r.safe_ledger_error_category(stopped.exception), 'ledger_child_result_network_stop')
        self.assertEqual(len(self.provider.posts), 1)
        self.assertEqual(len(downloads), 1)
        self.assertIn('child-1', downloads[0])
        controller = self.store.get('recoveries/' + '1' * 32)[0]
        child = self.store.get(controller['children'][0]['key'])[0]
        self.assertEqual(child['state'], 'terminal')
        self.assertEqual(child['batch_id'], 'child-1')
        self.assertFalse((self.output / r.RECEIPT).exists())

    def cached_failed_parents(self):
        cache = ResultCache(MemoryR2(), 'private-test')
        self.provider.plans['root-1'] = ['done', 'failed', 'done']
        self.provider.plans['root-2'] = ['failed', 'done', 'done', 'done']
        for root in self.originals:
            states = self.provider.plans[root['batch_id']]
            for binding, state in zip(root['files'], states):
                if state == 'failed':
                    continue
                lineage = {'batch_id': root['batch_id'], 'batch_key': root['key'],
                           'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 0}
                cache.put(binding, lineage, result_zip())
        return cache

    def test_exact_expired_done_child_zip_is_deferred_across_groups_but_no_handoff_is_admitted(self):
        cache = self.cached_failed_parents()
        downloads = []
        def expired(url):
            downloads.append(url)
            raise NetworkStop('tls_certificate_expired')
        with self.assertRaisesRegex(r.RecoveryError, '^ledger_child_result_tls_certificate_expired$'):
            self.recover(result_cache=cache, downloader=expired)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(downloads), 2)
        for root in self.originals:
            controller = self.store.get('recoveries/' + root['key'].split('/')[1])[0]
            self.assertEqual(len(controller['children']), 1)
            child = self.store.get(controller['children'][0]['key'])[0]
            self.assertEqual(child['state'], 'terminal')
        self.assertFalse(self.output.exists())
        self.assertFalse(list(self.root.glob('.mineru-market-source-*')))
        # An unchanged rerun polls the same accepted children, with no new POST.
        with self.assertRaisesRegex(r.RecoveryError, 'ledger_child_result_tls_certificate_expired'):
            self.recover(result_cache=cache, downloader=expired)
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(len(downloads), 4)

    def test_non_expiry_child_failure_stops_before_another_original_group_can_post(self):
        for error in (NetworkStop('network_stop'), NetworkStop('tls_certificate_expired PRIVATE'),
                      ValueError('PRIVATE unknown download failure')):
            cache = self.cached_failed_parents()
            with self.subTest(kind=type(error).__name__), self.assertRaises(m.LedgerError):
                self.recover(result_cache=cache, downloader=lambda url: (_ for _ in ()).throw(error))
            self.assertEqual(len(self.provider.posts), 1)
            self.assertIsNone(self.store.get('recoveries/' + '2' * 32)[0])
            self.assertFalse(self.output.exists())

    def test_original_expiry_is_immediate_and_cannot_authorize_child_submission(self):
        cache = self.cached_failed_parents()
        # Only cached originals can pass. Removing one original's cache must
        # stop in the original verification phase, before any recovery POST.
        cache.client.objects.clear()
        with self.assertRaises(NetworkStop):
            self.recover(result_cache=cache, downloader=lambda url: (_ for _ in ()).throw(
                NetworkStop('tls_certificate_expired')))
        self.assertEqual(self.provider.posts, [])
        self.assertFalse(self.output.exists())

    def test_source_handoff_requires_all_deferred_child_bytes_on_later_cache_reuse(self):
        cache = self.cached_failed_parents()
        with self.assertRaises(r.RecoveryError):
            self.recover(result_cache=cache, downloader=lambda url: (_ for _ in ()).throw(
                NetworkStop('tls_certificate_expired')))
        for root in self.originals:
            controller = self.store.get('recoveries/' + root['key'].split('/')[1])[0]
            child = self.store.get(controller['children'][0]['key'])[0]
            for binding in child['files']:
                lineage = {'batch_id': child['batch_id'], 'batch_key': child['key'],
                           'parent_batch_key': root['key'], 'data_id': binding['id'], 'child_ordinal': 1}
                cache.put(binding, lineage, result_zip())
        def forbidden(url):
            raise AssertionError('All originals and accepted children must use the exact cache')
        receipt = self.recover(result_cache=cache, downloader=forbidden)
        self.assertEqual(receipt['report_count'], 7)
        self.assertEqual(len(self.provider.posts), 2)
        self.validate()
    def test_workflow_dispatch_fixes_private_handoff_and_waits_before_cleanup(self):
        workflow = Path(__file__).resolve().parents[1] / '.github/workflows/market-views-mineru-recovery.yml'
        text = workflow.read_text()
        self.assertIn("github.ref == 'refs/heads/main'", text)
        self.assertIn('source_handoff_kind=mineru-recovery', text)
        self.assertIn('_private-workflow-handoff/mineru-market-sources/$GITHUB_RUN_ID/$DATE_FOLDER/shard_0.tar.gz', text)
        self.assertIn('compile_latex=false', text)
        self.assertLess(text.index('gh run watch'), text.index('delete-prefix'))
        self.assertNotIn('continue-on-error', text)
        self.assertNotIn('upload-artifact', text)


class SafeDiagnosticTests(unittest.TestCase):
    def test_exact_fixed_messages_and_wrapped_error_classes_have_only_safe_categories(self):
        for message, category in r.LEDGER_ERROR_CATEGORIES.items():
            with self.subTest(category=category):
                self.assertEqual(r.safe_ledger_error_category(m.LedgerError(message)), 'ledger_' + category)
        for name, category in r.WRAPPED_RECOVERY_CATEGORIES.items():
            message = 'Terminal recovery stopped; saved tasks retained (' + name + ')'
            with self.subTest(name=name):
                self.assertEqual(r.safe_ledger_error_category(m.LedgerError(message)), 'ledger_' + category)

    def test_unknown_private_or_malformed_error_arguments_never_escape(self):
        messages = ['PRIVATE report.pdf https://PRIVATE.invalid?token=PRIVATE',
                    'Stored task scope, source, options or token identity mismatch\nPRIVATE',
                    'Terminal recovery stopped; saved tasks retained (PRIVATE_SECRET)',
                    'MinerU request rejected or malformed: HTTP 403 PRIVATE', 'PRIVATE' * 1000,
                    {'PRIVATE': 'secret'}, ['PRIVATE'], None]
        for message in messages:
            with self.subTest(kind=type(message).__name__):
                self.assertEqual(r.safe_ledger_error_category(m.LedgerError(message)), 'ledger_error')
        self.assertEqual(r.safe_ledger_error_category(m.LedgerError('PRIVATE', 'secret')), 'ledger_error')
        self.assertEqual(r.safe_ledger_error_category(ValueError('PRIVATE')), 'ledger_error')

    def test_wrapped_network_context_admits_only_exact_fixed_tls_category(self):
        message = 'Terminal recovery stopped; saved tasks retained (NetworkStop)'
        class PrivateArgument:
            def __eq__(self, other):
                raise AssertionError('Untrusted argument comparison must not execute')
            def __str__(self):
                raise AssertionError('Untrusted argument rendering must not execute')
        for context, expected in ((NetworkStop('tls_certificate_expired'), 'ledger_child_result_tls_certificate_expired'),
                                  (NetworkStop('network_stop'), 'ledger_child_result_network_stop'),
                                  (NetworkStop('tls_certificate_expired PRIVATE'), 'ledger_child_result_network_stop'),
                                  (NetworkStop(PrivateArgument()), 'ledger_child_result_network_stop'),
                                  (NetworkStop(['tls_certificate_expired']), 'ledger_child_result_network_stop'),
                                  (NetworkStop({'PRIVATE': 'secret'}), 'ledger_child_result_network_stop'),
                                  (ValueError('tls_certificate_expired'), 'ledger_child_result_network_stop')):
            error = m.LedgerError(message)
            error.__context__ = context
            self.assertEqual(r.safe_ledger_error_category(error), expected)

    def test_status_templates_are_strict_and_do_not_publish_provider_text(self):
        self.assertEqual(r.safe_ledger_error_category(m.LedgerError('MinerU response is not valid JSON: HTTP 403')),
                         'ledger_provider_response_json_invalid')
        self.assertEqual(r.safe_ledger_error_category(m.LedgerError('MinerU request rejected or malformed: HTTP 429')),
                         'ledger_provider_request_rejected')
        self.assertEqual(r.safe_ledger_error_category(m.LedgerError('MinerU upload did not complete: HTTP 503')),
                         'ledger_provider_upload_rejected')
        for invalid in ('-1', '2000', '999', 'PRIVATE'):
            self.assertEqual(r.safe_ledger_error_category(m.LedgerError(
                'MinerU request rejected or malformed: HTTP ' + invalid)), 'ledger_error')

    def test_real_cli_catches_known_and_unknown_ledger_error_without_private_text(self):
        for message, expected in (('Terminal recovery stopped; saved tasks retained (NetworkStop)',
                                   'ledger_child_result_network_stop'),
                                  ('PRIVATE source.pdf https://PRIVATE.invalid?token=PRIVATE', 'ledger_error')):
            with patch('sys.argv', ['recover', 'validate', '--output-dir', 'PRIVATE', '--expected-reports', '1',
                                    '--date-folder', '261003']), \
                    patch.object(r, 'validate_sources', side_effect=m.LedgerError(message)), \
                    patch('socket.create_connection', side_effect=AssertionError('Offline tests')), \
                    patch('sys.stderr', new_callable=io.StringIO) as stderr:
                self.assertEqual(r.main(), 2)
            self.assertEqual(stderr.getvalue(), 'MinerU source recovery stopped: ' + expected + '\n')
            self.assertNotIn('PRIVATE', stderr.getvalue())


if __name__ == '__main__':
    unittest.main()
