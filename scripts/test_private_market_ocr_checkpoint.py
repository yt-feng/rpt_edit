"""Private cache binding, atomic restore and ambiguous-paid-request persistence."""
import contextlib
import io
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import private_market_ocr_checkpoint as cache
from private_workflow_handoff import create_archive, extract_archive


class StorageError(RuntimeError):
    def __init__(self, code):
        self.response = {'Error': {'Code': code}}


class CheckpointTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.directory = self.root / 'cache'
        self.manifest = self.root / 'manifest.json'
        self.rows = [{'process_local_path': f'/old/path/{n}.pdf', 'name': f'Report{n}.pdf',
                      'content_sha256': str(n) * 64, 'dropbox_path': f'/261005/{n}.pdf'} for n in (1, 2)]
        self.write()

    def write(self):
        self.manifest.write_text(json.dumps(self.rows))

    def key(self):
        return cache.checkpoint_key(self.manifest, '261005', 2)

    def test_manifest_identity_ignores_local_paths_and_order_but_pins_all_source_bindings(self):
        original = self.key()
        self.rows.reverse()
        self.rows[0]['process_local_path'] = '/new/run/2.pdf'
        self.write()
        self.assertEqual(self.key(), original)
        self.assertRegex(original, r'^_workflow-cache/market-ocr-synthesis/v1/261005/[a-f0-9]{64}\.tar\.gz$')
        for field in ('name', 'content_sha256', 'dropbox_path'):
            value = self.rows[0][field]
            self.rows[0][field] = 'a' * 64 if field == 'content_sha256' else '/261005/changed.pdf'
            self.write()
            self.assertNotEqual(self.key(), original)
            self.rows[0][field] = value

    def test_invalid_manifest_and_date_cannot_select_a_cache(self):
        with self.assertRaises(ValueError):
            cache.checkpoint_key(self.manifest, '261006', 2)
        with self.assertRaises(ValueError):
            cache.checkpoint_key(self.manifest, '261005', 3)
        self.rows[0]['content_sha256'] = 'invalid'
        self.write()
        with self.assertRaises(ValueError):
            self.key()

    def test_restore_missing_and_unavailable_are_advisory_and_never_expose_error_text(self):
        for error in (StorageError('NoSuchKey'), StorageError('AccessDenied'), TimeoutError('private-token')):
            with patch.object(cache, 'download_directory', side_effect=error), contextlib.redirect_stdout(io.StringIO()) as output:
                self.assertFalse(cache.restore(self.directory, self.key()))
                self.assertTrue(self.directory.is_dir())
                self.assertNotIn('private-token', output.getvalue())

    def test_interrupted_restore_never_uses_partial_rows_or_erases_local_work(self):
        self.directory.mkdir()
        (self.directory / 'existing.json').write_text('prior')
        def interrupted(key, destination, **kwargs):
            destination.mkdir()
            (destination / 'unverified.json').write_text('partial')
            raise TimeoutError('private-details')
        with patch.object(cache, 'download_directory', side_effect=interrupted):
            self.assertFalse(cache.restore(self.directory, self.key()))
        self.assertEqual(list(p.name for p in self.directory.iterdir()), ['existing.json'])

    def test_real_archive_roundtrip_preserves_completed_and_pending_model_rows(self):
        source = self.root / 'source'
        (source / 'model').mkdir(parents=True)
        (source / 'pages').mkdir()
        rows = {'model/prompt.json': '{"summary":"private"}',
                'model/unknown.pending.json': '{"status":"ambiguous"}',
                'pages/original.json': '{"pages":["private OCR"]}'}
        for name, value in rows.items():
            (source / name).write_text(value)
        archive = self.root / 'saved.tar.gz'
        def upload(directory, key, **kwargs):
            self.assertEqual(key, self.key())
            create_archive(directory, archive)
        def download(key, destination, **kwargs):
            self.assertEqual(key, self.key())
            return extract_archive(archive, destination)
        with patch.object(cache, 'upload_directory', side_effect=upload), patch.object(cache, 'download_directory', side_effect=download):
            self.assertTrue(cache.save(source, self.key()))
            self.assertTrue(cache.restore(self.directory, self.key()))
        self.assertEqual({name: (self.directory / name).read_text() for name in rows}, rows)

    def test_empty_cache_is_not_saved_and_storage_failure_does_not_claim_success(self):
        with patch.object(cache, 'upload_directory') as upload:
            self.assertFalse(cache.save(self.directory, self.key()))
            upload.assert_not_called()
        self.directory.mkdir()
        (self.directory / 'unknown.pending.json').write_text('{}')
        with patch.object(cache, 'upload_directory', side_effect=TimeoutError('private')):
            self.assertFalse(cache.save(self.directory, self.key()))
        self.assertTrue((self.directory / 'unknown.pending.json').is_file())


if __name__ == '__main__':
    unittest.main()
