"""Real PDF/cache/archive contracts; no provider or remote storage is used."""
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import fitz

import build_market_views_ocr_fallback as fallback
import recover_ocr_cache_sources as recovery
from private_market_ocr_checkpoint import checkpoint_key
from private_workflow_handoff import create_archive
from test_build_market_views_ocr_fallback import model_fixture, page_record


class MissingObject(Exception):
    response = {'Error': {'Code': 'NoSuchKey'}}


class MemoryR2:
    def __init__(self):
        self.objects = {}
        self.uploads = []

    def head_object(self, Bucket, Key):
        if Key not in self.objects:
            raise MissingObject()
        data, metadata = self.objects[Key]
        return {'ContentLength': len(data), 'Metadata': dict(metadata)}

    def get_object(self, Bucket, Key):
        return {'Body': io.BytesIO(self.objects[Key][0])}

    def upload_file(self, filename, bucket, key, ExtraArgs):
        self.objects[key] = (Path(filename).read_bytes(), dict(ExtraArgs['Metadata']))
        self.uploads.append(key)


class CachedSourceRecoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input = self.root / 'originals'
        self.input.mkdir()
        self.workspace = self.root / 'recovery'
        self.workspace.mkdir()
        self.cache = self.root / 'cache'
        self.client = MemoryR2()
        self.env = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
            'GITHUB_REF': 'refs/heads/main', 'GITHUB_REPOSITORY': 'owner/repo',
            'GITHUB_WORKFLOW_REF': f'owner/repo/{recovery.WORKFLOW}@refs/heads/main',
            'GITHUB_RUN_ID': '999', 'GITHUB_SHA': 'b' * 40}
        self.producer = {'id': 123, 'path': '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml',
            'head_branch': 'main', 'head_sha': 'a' * 40, 'status': 'completed', 'event': 'schedule',
            'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'}}

    def seed(self, count=2):
        rows = []
        for number in range(count):
            path = self.input / f'report-{number:03}.pdf'
            with fitz.open() as document:
                for page in range(2):
                    document.new_page().insert_text((40, 60), f'Report {number}, page {page + 1}.')
                document.save(path)
            rows.append({'process_local_path': '/original/' + path.name, 'name': path.name,
                'content_sha256': recovery.digest(path.read_bytes()), 'dropbox_path': '/zip_backup/261007/' + path.name})
        self.manifest = self.input / 'selected_to_process_manifest.json'
        self.manifest.write_text(json.dumps(rows))
        with redirect_stdout(io.StringIO()):
            fallback.build(self.input, self.manifest, count, '261007', self.root / 'seed', self.cache,
                source_run_id='123', execution_sha='a' * 40, ocr_all_pages=True,
                extractor=lambda path, **kw: [page_record(p, f'{path.name} 研究需求增长与盈利改善3.4%。' * 12) for p in [1, 2]],
                invoke=model_fixture)
        self.request = {'source_run_id': '123', 'date_folder': '261007', 'expected_reports': count,
            'manifest_sha256': recovery.digest(self.manifest.read_bytes())}
        self.cache_key = checkpoint_key(self.manifest, '261007', count)
        self.publish_cache()

    def publish_cache(self):
        archive = self.root / 'checkpoint.tar.gz'
        create_archive(self.cache, archive)
        payload = archive.read_bytes()
        self.request.update(archive_sha256=recovery.digest(payload), archive_size_bytes=len(payload))
        self.client.objects[self.cache_key] = (payload, {'sha256': self.request['archive_sha256']})

    def recover(self):
        with redirect_stdout(io.StringIO()), \
             patch.object(fallback, 'request_with_retry', side_effect=AssertionError('provider must never run')) as provider, \
             patch.object(fallback.subprocess, 'run', side_effect=AssertionError('OCR must never run')) as ocr:
            try:
                return recovery.recover(self.input, self.producer, self.request, self.workspace,
                    self.env, self.client, 'private')
            finally:
                provider.assert_not_called()
                ocr.assert_not_called()

    def archive(self):
        with redirect_stdout(io.StringIO()):
            return recovery.archive(self.input, self.producer, self.request, self.workspace,
                self.env, self.client, 'private')

    def test_44_real_pdfs_complete_without_provider_or_ocr_and_new_lineage(self):
        self.seed(44)
        result = self.recover()
        self.assertEqual(result, {'reused': False, 'reports': 44})
        receipt = json.loads((self.workspace / 'source' / recovery.RECEIPT).read_bytes())
        self.assertEqual((receipt['summarized_reports'], receipt['skipped_reports'], receipt['total_pages']), (44, 0, 88))
        self.assertEqual(receipt['source_run_id'], '123')
        self.assertEqual(receipt['cache_recovery']['recovery_run_id'], '999')
        self.assertEqual(receipt['cache_recovery']['archive_sha256'], self.request['archive_sha256'])
        self.assertEqual(receipt['final_synthesis_metrics']['model_submissions'], 0)
        self.assertEqual(receipt['final_synthesis_metrics']['fallback_stages'], [])
        self.archive()
        self.assertEqual(self.client.uploads, [f'{recovery.PREFIX}/999/261007/shard_0.tar.gz'])

    def test_completed_handoff_reused_without_rebuild_or_receipt_change(self):
        self.seed(); self.recover(); self.archive()
        before = (self.workspace / 'source' / recovery.RECEIPT).read_bytes()
        self.workspace = self.root / 'retry'; self.workspace.mkdir()
        # Existing complete handoff remains usable even if the old memo is gone.
        del self.client.objects[self.cache_key]
        with patch.object(fallback, 'build', side_effect=AssertionError('do not rebuild existing handoff')):
            self.assertTrue(self.recover()['reused'])
        self.archive()
        self.assertEqual((self.workspace / 'source' / recovery.RECEIPT).read_bytes(), before)
        self.assertEqual(len(self.client.uploads), 1)

    def test_original_run_cannot_be_used_as_recovery_identity(self):
        self.seed(); self.env['GITHUB_RUN_ID'] = '123'
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'recovery_main_identity_invalid'):
            self.recover()

    def test_non_main_or_other_workflow_is_rejected(self):
        self.seed(); self.env['GITHUB_WORKFLOW_REF'] = 'owner/repo/.github/workflows/other.yml@refs/heads/main'
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'recovery_main_identity_invalid'):
            self.recover()

    def test_foreign_original_producer_is_rejected(self):
        self.seed(); self.producer['head_repository']['full_name'] = 'other/repo'
        with self.assertRaises(ValueError): self.recover()

    def test_manifest_bytes_changed_is_rejected_even_with_same_bindings(self):
        self.seed(); self.manifest.write_bytes(self.manifest.read_bytes() + b'\n')
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'frozen_manifest_changed'):
            self.recover()

    def test_missing_or_modified_pdf_is_rejected(self):
        self.seed(); next(self.input.glob('*.pdf')).write_bytes(b'%PDF-changed')
        with self.assertRaises(ValueError): self.recover()

    def test_missing_archive_does_not_create_an_empty_cache(self):
        self.seed(); del self.client.objects[self.cache_key]
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'private_object_unavailable'):
            self.recover()
        self.assertFalse((self.workspace / 'cache').exists())

    def test_metadata_must_match_pinned_incident_hash_and_size(self):
        self.seed(); self.request['archive_sha256'] = 'f' * 64
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'pinned_checkpoint_changed'):
            self.recover()
        self.assertFalse((self.workspace / 'source').exists())

    def test_same_size_corrupt_get_bytes_fail_archive_sha(self):
        self.seed()
        old = self.client.get_object
        def corrupt(**kwargs):
            value = old(**kwargs)['Body'].read()
            return {'Body': io.BytesIO(value[:-1] + bytes([value[-1] ^ 1]))}
        with patch.object(self.client, 'get_object', side_effect=corrupt):
            with self.assertRaisesRegex(ValueError, 'archive_hash_mismatch'): self.recover()

    def test_truncated_get_fails_length(self):
        self.seed(); payload = self.client.objects[self.cache_key][0]
        with patch.object(self.client, 'get_object', return_value={'Body': io.BytesIO(payload[:-1])}):
            with self.assertRaisesRegex(ValueError, 'object_size_mismatch'): self.recover()

    def test_unsafe_archive_is_rejected_before_extraction(self):
        self.seed()
        for name, kind in [('../outside.json', tarfile.REGTYPE), ('symlink', tarfile.SYMTYPE)]:
            with self.subTest(name=name):
                buffer = io.BytesIO()
                with tarfile.open(fileobj=buffer, mode='w:gz') as archive:
                    member = tarfile.TarInfo(name); member.type = kind
                    if kind == tarfile.SYMTYPE: member.linkname = '../outside'
                    archive.addfile(member)
                data = buffer.getvalue(); checksum = recovery.digest(data)
                self.client.objects[self.cache_key] = (data, {'sha256': checksum})
                self.request.update(archive_sha256=checksum, archive_size_bytes=len(data))
                with self.assertRaises(ValueError): self.recover()
                self.assertFalse((self.root / 'outside.json').exists())

    def test_missing_one_page_cache_never_extracts_or_accepts_partial(self):
        self.seed(); next((self.cache / 'pages').glob('*.json')).unlink(); self.publish_cache()
        with self.assertRaisesRegex(ValueError, 'cache_only_pages_missing'): self.recover()
        self.assertFalse((self.workspace / 'source').exists())

    def test_missing_last_page_is_rejected_against_real_pdf_count(self):
        self.seed(); path = next((self.cache / 'pages').glob('*.json'))
        value = json.loads(path.read_bytes()); value['pages'].pop(); path.write_text(json.dumps(value)); self.publish_cache()
        with self.assertRaisesRegex(ValueError, 'incomplete or corrupt page coverage'): self.recover()

    def test_missing_summary_does_not_submit_model(self):
        self.seed(); next((self.cache / 'model').glob('*.json')).unlink(); self.publish_cache()
        with self.assertRaisesRegex(ValueError, 'cache_only_summary_missing'): self.recover()

    def test_summary_identity_mismatch_does_not_submit_model(self):
        self.seed(); path = next((self.cache / 'model').glob('*.json'))
        value = json.loads(path.read_bytes()); value['request_sha256'] = '0' * 64
        path.write_text(json.dumps(value)); self.publish_cache()
        with self.assertRaisesRegex(ValueError, 'Model cache identity mismatch'): self.recover()

    def test_pending_only_summary_stays_blocked(self):
        self.seed(); path = next((self.cache / 'model').glob('*.json'))
        path.rename(path.with_suffix('.pending.json')); self.publish_cache()
        with self.assertRaisesRegex(RuntimeError, 'unknown/incomplete'): self.recover()

    def test_completed_response_takes_precedence_over_residual_pending(self):
        self.seed()
        for directory in [self.cache / 'model', self.cache / 'final_synthesis']:
            path = next(directory.rglob('*.json')); path.with_suffix('.pending.json').write_text('{}')
        self.publish_cache(); self.assertEqual(self.recover()['reports'], 2)

    def test_missing_final_synthesis_cannot_be_deterministic_fallback(self):
        self.seed(); next((self.cache / 'final_synthesis').rglob('*.json')).unlink(); self.publish_cache()
        with self.assertRaisesRegex(ValueError, 'cache_only_final_synthesis_missing'): self.recover()
        self.assertFalse((self.workspace / 'source').exists())

    def test_existing_receipt_cannot_be_replaced_by_rebuild(self):
        self.seed(); self.recover(); self.archive()
        path = self.workspace / 'source' / recovery.RECEIPT
        value = json.loads(path.read_bytes()); value['completed_at'] = 'changed'
        path.write_text(json.dumps(value))
        with self.assertRaisesRegex(recovery.CacheRecoveryError, 'existing_handoff_receipt_changed'):
            self.archive()
        self.assertEqual(len(self.client.uploads), 1)

    def test_workflow_has_no_ocr_provider_credentials_or_fresh_source_branch(self):
        import yaml
        root = Path(__file__).resolve().parent.parent
        workflow = (root / recovery.WORKFLOW).read_text()
        value = yaml.safe_load(workflow)
        recover = value['jobs']['recover']
        # GitHub rejects runner context at job.env before registering any job;
        # ordinary YAML parsing and sibling PR checks cannot detect this error.
        self.assertNotIn('${{ runner.', str(recover.get('env', {})))
        names = [step.get('name') for step in recover['steps']]
        self.assertLess(names.index('Restore and verify complete OCR sources from cache only'),
                        names.index('Archive and verify recovered OCR sources in private R2'))
        self.assertNotIn('DEEPSEEK', str(recover))
        self.assertNotIn('MINER_U', str(recover))
        self.assertNotIn('tesseract', str(recover))
        self.assertNotIn('dropbox', str(recover).lower())
        self.assertEqual(value['jobs']['deliver']['uses'], './.github/workflows/recover-report-article-delivery.yml')
        self.assertIn("needs.recover.result == 'success'", value['jobs']['deliver']['if'])
        self.assertTrue(value['jobs']['deliver']['with']['upload_wechat'])

    def test_cli_reports_fixed_missing_stage_without_private_error_text(self):
        producer = self.root / 'producer.json'; producer.write_text(json.dumps(self.producer))
        cases = [
            (ValueError('cache_only_pages_missing'), 'cache_only_pages_missing'),
            (ValueError('cache_only_summary_missing'), 'cache_only_summary_missing'),
            (ValueError('cache_only_final_synthesis_missing'), 'cache_only_final_synthesis_missing'),
            (RuntimeError('Prior model submission has unknown/incomplete outcome; inspect checkpoint PRIVATE_NAME'),
             'summary_submission_pending'),
            (RuntimeError('Final synthesis submission already pending'), 'final_synthesis_submission_pending'),
            (ValueError('PRIVATE_MODEL_OR_SOURCE_BODY'), 'ValueError')]
        for error, category in cases:
            with self.subTest(category=category), patch.object(recovery, 'request_from_env', return_value={}), \
                 patch.object(recovery, 'build_client', return_value=self.client), \
                 patch.object(recovery, 'require_env', return_value='private'), \
                 patch.object(recovery, 'recover', side_effect=error), redirect_stdout(io.StringIO()) as output:
                code = recovery.main(['recover', '--input-dir', str(self.input), '--producer-json', str(producer),
                                      '--workspace', str(self.workspace)])
                self.assertEqual(code, 1)
                self.assertEqual(json.loads(output.getvalue())['category'], category)
                self.assertNotIn('PRIVATE_', output.getvalue())


if __name__ == '__main__':
    unittest.main()
