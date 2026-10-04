"""Offline raw-PDF preservation, identity, expiry and read-only restore tests."""
import copy
from datetime import datetime, timedelta, timezone
import io
import json
from pathlib import Path
import tempfile
import tarfile
import unittest
from unittest.mock import patch

import archive_market_views_originals as a
from mineru_task_ledger import digest, encoded
from test_mineru_result_cache import MemoryR2


class ArchiveTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.source = self.root / 'originals'
        self.source.mkdir()
        self.rows = []
        for number in range(2):
            name = f'PRIVATE-{number}.pdf'
            raw = b'%PDF-1.7 exact original ' + str(number).encode()
            (self.source / name).write_bytes(raw)
            self.rows.append({'process_local_path': '/selected/' + name, 'content_sha256': digest(raw),
                              'dropbox_path': '/zip_backup/261002/' + name})
        (self.source / a.MANIFEST).write_bytes(encoded(self.rows))
        self.ctx = a.context('12345', '261002', 'a' * 40)
        self.client = MemoryR2()
        self.time = datetime(2026, 10, 4, 12, tzinfo=timezone.utc)
        self.now = lambda: self.time

    def upload(self):
        return a.upload_originals(self.source, 2, self.ctx, self.client, 'private', now=self.now)

    def restore(self):
        return a.restore_originals(self.root / 'restored', 2, self.ctx, self.client, 'private', now=self.now)

    def test_all_raw_pdf_bytes_survive_immutable_archive_and_read_only_restore(self):
        receipt = self.upload()
        puts = len(self.client.puts)
        self.restore()
        self.assertEqual(len(self.client.puts), puts)
        self.assertEqual(len(self.client.objects), 2)
        self.assertFalse(receipt['source_ready'])
        self.assertFalse(receipt['physical_deletion_guaranteed'])
        for path in self.source.iterdir():
            self.assertEqual(path.read_bytes(), (self.root / 'restored' / path.name).read_bytes())
        self.assertFalse((self.root / 'restored' / 'source_receipt.json').exists())
        self.assertTrue(all(key.startswith(a.PREFIX + '/12345/261002/') for key in self.client.objects))
        self.assertTrue(all(call['IfNoneMatch'] == '*' for call in self.client.puts))

    def test_repeat_preserves_same_immutable_bytes_and_first_expiry(self):
        first = self.upload()
        before = copy.deepcopy(self.client.objects)
        self.time += timedelta(hours=1)
        self.assertEqual(first, self.upload())
        self.assertEqual(before, self.client.objects)

    def test_wrong_count_hash_date_or_extra_pdf_never_writes_r2(self):
        self.rows[0]['content_sha256'] = 'b' * 64
        (self.source / a.MANIFEST).write_bytes(encoded(self.rows))
        with self.assertRaises(ValueError): self.upload()
        self.assertEqual(self.client.puts, [])
        self.rows[0]['content_sha256'] = digest((self.source / 'PRIVATE-0.pdf').read_bytes())
        self.rows[0]['dropbox_path'] = '/zip_backup/261001/261002/PRIVATE.pdf'
        (self.source / a.MANIFEST).write_bytes(encoded(self.rows))
        with self.assertRaises(ValueError): self.upload()
        self.assertEqual(self.client.puts, [])

    def test_expiry_disables_restore_without_deleting_or_changing_stored_objects(self):
        self.upload()
        before = copy.deepcopy(self.client.objects)
        self.time += timedelta(days=7)
        with self.assertRaises(a.OriginalsError): self.restore()
        self.assertFalse((self.root / 'restored').exists())
        self.assertEqual(before, self.client.objects)

    def test_corrupt_archive_is_rejected_and_no_partial_destination_survives(self):
        self.upload()
        key = next(key for key in self.client.objects if key.endswith('.tar.gz'))
        self.client.objects[key]['Body'] = b'PRIVATE corrupt archive'
        with self.assertRaises(a.OriginalsError): self.restore()
        self.assertFalse((self.root / 'restored').exists())

    def test_self_hashed_traversal_link_or_oversize_archive_still_cannot_extract(self):
        self.upload()
        archive_key = next(key for key in self.client.objects if key.endswith('.tar.gz'))
        receipt_key = next(key for key in self.client.objects if key.endswith(a.RECEIPT))
        original_receipt = json.loads(self.client.objects[receipt_key]['Body'])
        for mode in ('traversal', 'symlink', 'oversize'):
            output = io.BytesIO()
            with tarfile.open(fileobj=output, mode='w:gz') as archive:
                info = tarfile.TarInfo('../PRIVATE.pdf' if mode == 'traversal' else 'PRIVATE-0.pdf')
                info.size = 1
                if mode == 'symlink':
                    info.type, info.linkname = tarfile.SYMTYPE, '../PRIVATE'
                    archive.addfile(info)
                elif mode == 'oversize':
                    info.size = a.MAX_ARCHIVE + 1
                    # A large header must be rejected before its body is read.
                    archive.fileobj.write(info.tobuf())
                else:
                    archive.addfile(info, io.BytesIO(b'x'))
            payload = output.getvalue()
            receipt = copy.deepcopy(original_receipt)
            receipt.update(archive_sha256=digest(payload), archive_bytes=len(payload))
            for key, raw in ((archive_key, payload), (receipt_key, encoded(receipt))):
                self.client.objects[key]['Body'] = raw
                self.client.objects[key]['Metadata']['sha256'] = digest(raw)
            with self.subTest(mode=mode), self.assertRaises(a.OriginalsError): self.restore()
            self.assertFalse((self.root / 'restored').exists())
            self.assertFalse(list(self.root.glob('.originals-restore-*')))

    def test_wrong_run_or_execution_sha_cannot_restore_another_archive(self):
        self.upload()
        self.ctx['execution_sha'] = 'b' * 40
        with self.assertRaises(a.OriginalsError): self.restore()
        self.assertFalse((self.root / 'restored').exists())

    def test_pax_header_counts_toward_the_total_decoded_archive_limit(self):
        self.upload()
        archive_key = next(key for key in self.client.objects if key.endswith('.tar.gz'))
        receipt_key = next(key for key in self.client.objects if key.endswith(a.RECEIPT))
        receipt = json.loads(self.client.objects[receipt_key]['Body'])
        output = io.BytesIO()
        with tarfile.open(fileobj=output, mode='w:gz', format=tarfile.PAX_FORMAT) as archive:
            for path in self.source.iterdir():
                raw = path.read_bytes()
                info = tarfile.TarInfo(path.name)
                info.size = len(raw)
                info.pax_headers = {'comment': 'x' * (2 * 1024 * 1024)}
                archive.addfile(info, io.BytesIO(raw))
        payload = output.getvalue()
        receipt.update(archive_sha256=digest(payload), archive_bytes=len(payload))
        for key, raw in ((archive_key, payload), (receipt_key, encoded(receipt))):
            self.client.objects[key]['Body'] = raw
            self.client.objects[key]['Metadata']['sha256'] = digest(raw)
        with patch.object(a, 'MAX_ARCHIVE', 1024 * 1024), self.assertRaisesRegex(a.OriginalsError, 'decoded_archive_exceeds_bound'):
            self.restore()
        self.assertFalse((self.root / 'restored').exists())

    def test_sealed_payload_is_hash_verified_even_if_source_changes_then_is_restored_while_packing(self):
        original_pack = a.packed_originals
        path = self.source / 'PRIVATE-0.pdf'
        raw = path.read_bytes()
        def transient_change(manifest, pairs):
            try:
                path.write_bytes(b'%PDF-1.7 PRIVATE changed during pack')
                return original_pack(manifest, pairs)
            finally:
                path.write_bytes(raw)
        with patch.object(a, 'packed_originals', side_effect=transient_change), self.assertRaises(ValueError):
            self.upload()
        self.assertEqual(path.read_bytes(), raw)
        self.assertEqual(self.client.puts, [])

    def test_restore_refuses_existing_destination_without_modifying_it(self):
        self.upload()
        destination = self.root / 'restored'
        destination.mkdir()
        (destination / 'marker').write_bytes(b'preserve')
        with self.assertRaises(a.OriginalsError): self.restore()
        self.assertEqual((destination / 'marker').read_bytes(), b'preserve')

    def test_symlink_original_is_not_archived(self):
        (self.source / 'PRIVATE-1.pdf').unlink()
        (self.source / 'PRIVATE-1.pdf').symlink_to(self.source / 'PRIVATE-0.pdf')
        with self.assertRaises(ValueError): self.upload()
        self.assertEqual(self.client.puts, [])

    def test_restore_producer_allows_failed_ocr_but_requires_exact_manual_main_identity(self):
        value = {'id': 12345, 'path': a.WORKFLOW, 'event': 'workflow_dispatch', 'head_branch': 'main',
                 'head_sha': 'a' * 40, 'repository': {'full_name': 'owner/repo'}, 'status': 'completed', 'conclusion': 'failure'}
        a.check_restore_producer(value, '12345', 'owner/repo', 'a' * 40)
        for change in ({'id': 12346}, {'path': 'PRIVATE.yml'}, {'event': 'push'}, {'head_branch': 'branch'}, {'head_sha': 'b' * 40}):
            with self.assertRaises(a.OriginalsError):
                a.check_restore_producer({**value, **change}, '12345', 'owner/repo', 'a' * 40)

    def test_in_progress_cancelled_timed_out_or_queued_producer_is_rejected_before_r2_get(self):
        producer = {'id': 12345, 'path': a.WORKFLOW, 'event': 'workflow_dispatch', 'head_branch': 'main',
                    'head_sha': 'a' * 40, 'repository': {'full_name': 'owner/repo'}, 'status': 'completed', 'conclusion': 'success'}
        path = self.root / 'private-producer.json'
        args = ['restore', '--run-id', '12345', '--date-folder', '261002', '--execution-sha', 'a' * 40,
                '--expected-reports', '2', '--producer-json', str(path), '--repository', 'owner/repo',
                '--destination', str(self.root / 'restored')]
        for change in ({'status': 'in_progress', 'conclusion': None}, {'status': 'queued', 'conclusion': None},
                       {'conclusion': 'cancelled'}, {'conclusion': 'timed_out'}, {'conclusion': 'skipped'}):
            path.write_bytes(encoded({**producer, **change}))
            with self.subTest(change=change), patch.object(a, 'read_object') as get, \
                    patch('socket.create_connection', side_effect=AssertionError('No offline network')), \
                    patch('sys.stderr', new_callable=io.StringIO) as stderr:
                self.assertEqual(a.main(args), 2)
            get.assert_not_called()
            self.assertEqual(stderr.getvalue(), 'Original PDF archive stopped: restore_producer_invalid\n')

    def test_workflow_archives_after_manifest_check_and_before_extraction(self):
        root = Path(__file__).resolve().parents[1]
        workflow = (root / '.github/workflows/market-views-native-recovery.yml').read_text()
        archive = workflow.index('- name: Preserve complete original PDFs in private R2 before extraction')
        self.assertLess(workflow.index('- name: Verify that every selected original'), archive)
        self.assertLess(archive, workflow.index('- name: Extract and verify'))
        self.assertIn('archive_market_views_originals.py upload', workflow)
        self.assertNotIn('delete', workflow[archive:workflow.index('- name: Extract and verify')])
        regression = (root / '.github/workflows/wechat-pipeline-regression.yml').read_text()
        self.assertIn('python scripts/test_archive_market_views_originals.py', regression)

    def test_originals_only_success_is_rejected_by_real_source_readiness_guard(self):
        from market_views_source_readiness import require_source_readiness, SourceReadinessError, SOURCE_GATES
        producer = {'id': 12345, 'head_sha': 'a' * 40, 'head_branch': 'main', 'path': a.WORKFLOW,
                    'status': 'completed', 'conclusion': 'success'}
        gates = SOURCE_GATES[a.WORKFLOW][1]
        steps = [{'number': 1, 'name': 'Preserve complete original PDFs in private R2 before extraction',
                  'status': 'completed', 'conclusion': 'success'}]
        steps += [{'number': number + 2, 'name': name, 'status': 'completed', 'conclusion': 'skipped'}
                  for number, name in enumerate(gates)]
        jobs = {'total_count': 1, 'jobs': [{'id': 99, 'run_id': 12345, 'name': 'recover', 'head_sha': 'a' * 40,
                                          'status': 'completed', 'conclusion': 'success', 'steps': steps}]}
        with self.assertRaisesRegex(SourceReadinessError, 'source_gate_not_successful'):
            require_source_readiness(producer, jobs)
        root = Path(__file__).resolve().parents[1]
        text = (root / '.github/workflows/market-views-native-recovery.yml').read_text()
        self.assertIn('archive_originals_only:', text)
        self.assertIn('if [ "$ARCHIVE_ORIGINALS_ONLY" = true ] && [ "$GENERATE_PDF" != false ]', text)
        for name in ('Extract and verify the complete original source batch', 'Record source-only validation counts',
                     'Archive verified native sources in private R2', 'Audit complete cloud OCR numeric evidence'):
            block = text.split('- name: ' + name, 1)[1].split('- name:', 1)[0]
            self.assertIn('if: ${{ !inputs.archive_originals_only }}', block)
        self.assertIn('if: ${{ inputs.enable_ocr && !inputs.archive_originals_only }}', text)
        self.assertEqual(text.count('if: ${{ inputs.generate_pdf && !inputs.archive_originals_only }}'), 2)


if __name__ == '__main__':
    unittest.main()
