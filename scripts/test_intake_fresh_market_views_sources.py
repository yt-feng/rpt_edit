"""Offline full-intake reservation, resumption and no-duplicate-POST contracts."""
import copy
from datetime import timedelta
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch
import uuid

import intake_fresh_market_views_sources as intake
import archive_market_views_originals as archive
import mineru_task_ledger as ledger_module
from mineru_task_ledger import digest, encoded
from test_mineru_result_cache import MemoryR2


class Provider:
    def __init__(self, owner):
        self.owner, self.posts, self.uploads = owner, [], []
        self.submit_error = self.upload_error = None

    def submit(self, items, options, token, timeout):
        # The first accepted request must already have complete immutable
        # authority, all canonical roots and every original source claim.
        owner = self.owner
        self.assert_complete(owner)
        self.posts.append(copy.deepcopy(items))
        if self.submit_error:
            raise self.submit_error
        return str(uuid.UUID(int=len(self.posts))), ['https://upload.invalid/fixed'] * len(items)

    @staticmethod
    def assert_complete(owner):
        owner.assertEqual(len(list((owner.store.root / 'sources').glob('*.json'))), len(owner.rows))
        owner.assertEqual(len(list((owner.store.root / 'batches').glob('*.json'))), (len(owner.rows) + 4) // 5)
        owner.assertEqual(len(owner.r2.objects), 1)

    def upload(self, url, raw, timeout):
        self.uploads.append(raw)
        if self.upload_error:
            raise self.upload_error

    def poll(self, *args):
        raise AssertionError('Fresh intake must never poll or download results')


class IntakeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.input = self.root / 'originals'; self.input.mkdir()
        self.rows = []
        for number in range(7):
            name = f'PRIVATE-{number}.pdf'; raw = b'%PDF-1.7 raw original ' + str(number).encode()
            (self.input / name).write_bytes(raw)
            self.rows.append({'process_local_path': '/selected/' + name, 'content_sha256': digest(raw),
                              'dropbox_path': '/zip_backup/261002/' + name})
        (self.input / archive.MANIFEST).write_bytes(encoded(self.rows))
        self.producer = {'id': 12345, 'path': archive.WORKFLOW, 'event': 'workflow_dispatch', 'head_branch': 'main',
                         'head_sha': 'a' * 40, 'status': 'completed', 'conclusion': 'success',
                         'repository': {'full_name': 'owner/repo'}}
        self.receipt()
        self.store = ledger_module.FileStore(self.root / 'ledger')
        self.provider = Provider(self)
        self.sleeps = []
        self.ledger = ledger_module.Ledger(self.store, self.provider, 'dropbox', 'https://mineru.net', intake.OPTIONS,
            [('MINER_U', 'PRIVATE-key')], sleep=lambda seconds: self.sleeps.append(seconds))
        self.r2 = MemoryR2()
        self.authority = intake.AuthorityStore(self.r2, 'private')

    def receipt(self):
        raw, bindings, _ = archive.checked_inputs(self.input, len(self.rows), '261002')
        now = archive.now_utc()
        value = {'schema_version': 1, 'kind': archive.KIND, 'source_ready': False,
                 'source_context': archive.context('12345', '261002', 'a' * 40), 'report_count': len(self.rows),
                 'manifest_sha256': digest(raw), 'original_inventory': bindings, 'archive_sha256': 'b' * 64,
                 'archive_bytes': 100, 'created_at_utc': now.isoformat(),
                 'expires_at_utc': (now + timedelta(days=7)).isoformat(),
                 'expiry_policy': 'restore-disabled-after-7-days', 'physical_deletion_guaranteed': False}
        (self.input / archive.RECEIPT).write_bytes(encoded(value))

    def call(self):
        with patch('socket.create_connection', side_effect=AssertionError('No network')):
            return intake.intake_sources(self.ledger, self.authority, self.input, self.producer,
                archive_run_id='12345', repository='owner/repo', expected_reports=len(self.rows), date_folder='261002',
                intake_run_id='54321', execution_sha='c' * 40)

    def test_complete_reservation_precedes_first_post_and_no_poll_or_zip_occurs(self):
        result = self.call()
        self.assertEqual([len(items) for items in self.provider.posts], [5, 2])
        self.assertEqual(self.sleeps, [10])
        self.assertEqual(result['provider_posts'], 2)
        self.assertEqual(result['accepted_root_count'], 2)
        self.assertEqual(result['uploaded_root_count'], 2)
        self.assertTrue(result['success'])
        self.assertFalse(result['source_ready'])
        self.assertFalse(result['complete_source_handoff'])
        self.assertFalse(result['production_acceptance'])
        self.assertEqual(result['provider_gets'], 0)
        self.assertEqual(result['result_gets'], 0)
        self.assertNotIn('PRIVATE', json.dumps(result))
        self.assertFalse((self.input / 'source-recovery-receipt.json').exists())

    def test_exact_fifty_sources_are_all_reserved_then_ten_original_posts(self):
        for number in range(7, 50):
            name = f'PRIVATE-{number}.pdf'; raw = b'%PDF-1.7 raw original ' + str(number).encode()
            (self.input / name).write_bytes(raw)
            self.rows.append({'process_local_path': '/selected/' + name, 'content_sha256': digest(raw),
                              'dropbox_path': '/zip_backup/261002/' + name})
        (self.input / archive.MANIFEST).write_bytes(encoded(self.rows)); self.receipt()
        result = self.call()
        self.assertEqual(len(self.provider.posts), 10)
        self.assertEqual(result['original_file_count'], 50)
        self.assertEqual(result['accepted_root_count'], 10)
        self.assertEqual(len(self.provider.uploads), 50)
        self.assertEqual(self.sleeps, [10] * 9)
        self.assertTrue(result['success'])

    def test_repeated_intake_reuses_every_accepted_root_with_zero_new_post(self):
        first = self.call()
        before = copy.deepcopy(self.r2.objects)
        result = self.call()
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(result['provider_posts'], 0)
        self.assertEqual(result['authority_sha256'], first['authority_sha256'])
        self.assertEqual(before, self.r2.objects)

    def test_canonical_reservation_interruption_resumes_only_its_prepared_full_authority(self):
        original_put = self.store.put
        stopped = False
        def interrupted(key, value, previous=None):
            nonlocal stopped
            if key.startswith('sources/') and not stopped and len(list((self.store.root / 'sources').glob('*.json'))) == 3:
                stopped = True
                raise OSError('fixture interruption')
            return original_put(key, value, previous)
        with patch.object(self.store, 'put', side_effect=interrupted), self.assertRaises(OSError):
            self.call()
        self.assertEqual(self.provider.posts, [])
        self.assertEqual(len(self.r2.objects), 1)
        result = self.call()
        self.assertTrue(result['success'])
        self.assertEqual(len(self.provider.posts), 2)

    def test_ambiguous_post_never_repeats_or_starts_another_root(self):
        self.provider.submit_error = TimeoutError('PRIVATE transport')
        with self.assertRaises(TimeoutError): self.call()
        self.assertEqual(len(self.provider.posts), 1)
        self.provider.submit_error = None
        with self.assertRaisesRegex(intake.IntakeError, 'ambiguous_intake_submission_retained'): self.call()
        self.assertEqual(len(self.provider.posts), 1)

    def test_accepted_task_after_upload_error_is_never_submitted_again(self):
        self.provider.upload_error = OSError('PRIVATE upload')
        with self.assertRaises(OSError): self.call()
        self.assertEqual(len(self.provider.posts), 1)
        self.provider.upload_error = None
        result = self.call()
        self.assertEqual(len(self.provider.posts), 2)
        self.assertEqual(result['accepted_root_count'], 2)
        self.assertEqual(result['uploaded_root_count'], 1)
        self.assertFalse(result['success'])
        self.assertEqual(result['category'], 'accepted_upload_incomplete')
        self.assertFalse(result['complete_source_handoff'])

    def test_preexisting_claim_without_this_complete_authority_cannot_become_fresh(self):
        item = self.ledger.bind(self.input / 'PRIVATE-0.pdf', 'PRIVATE-0.pdf')
        self.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': 'batches/' + 'd' * 32})
        with self.assertRaisesRegex(intake.IntakeError, 'existing_claims_without_intake_authority'): self.call()
        self.assertEqual(self.provider.posts, [])
        self.assertEqual(self.r2.puts, [])

    def test_missing_accepted_root_or_claim_never_grants_another_post(self):
        self.call()
        authority = json.loads(next(iter(self.r2.objects.values()))['Body'])
        self.store._path(authority['batches'][0]['key']).unlink()
        with self.assertRaisesRegex(intake.IntakeError, 'intake_claim_root_missing'): self.call()
        self.assertEqual(len(self.provider.posts), 2)

    def test_archive_producer_receipt_date_hash_or_expiry_fails_before_any_mutation(self):
        original = (self.input / archive.RECEIPT).read_bytes()
        for change in ({'source_ready': True}, {'manifest_sha256': 'f' * 64}, {'report_count': 6},
                       {'expires_at_utc': json.loads(original)['created_at_utc']}):
            (self.input / archive.RECEIPT).write_bytes(encoded({**json.loads(original), **change}))
            with self.subTest(change=change), self.assertRaises(intake.IntakeError): self.call()
            self.assertEqual(self.provider.posts, [])
            self.assertEqual(self.r2.puts, [])
        (self.input / archive.RECEIPT).write_bytes(original)
        self.producer['status'] = 'in_progress'
        with self.assertRaises(intake.IntakeError): self.call()
        self.assertEqual(self.r2.puts, [])

    def test_one_changed_unsubmitted_original_blocks_next_root_and_preserves_all_claims(self):
        base_upload = self.provider.upload
        def changed(url, raw, timeout):
            base_upload(url, raw, timeout)
            if len(self.provider.uploads) == 5:
                path = self.input / 'PRIVATE-6.pdf'; path.write_bytes(path.read_bytes() + b' changed')
        with patch.object(self.provider, 'upload', side_effect=changed), self.assertRaises(intake.IntakeError): self.call()
        self.assertEqual(len(self.provider.posts), 1)
        self.assertEqual(len(list((self.store.root / 'sources').glob('*.json'))), 7)

    def test_unaccepted_root_mutation_cannot_clear_ambiguous_post(self):
        self.provider.submit_error = TimeoutError()
        with self.assertRaises(TimeoutError): self.call()
        authority = json.loads(next(iter(self.r2.objects.values()))['Body'])
        key = authority['batches'][0]['key']; row, version = self.store.get(key)
        row['state'] = 'claiming'; self.store.put(key, row, version)
        self.provider.submit_error = None
        with self.assertRaisesRegex(intake.IntakeError, 'intake_unsubmitted_root_mismatch'): self.call()
        self.assertEqual(len(self.provider.posts), 1)

    def test_frozen_authority_tampering_is_rejected_even_with_rehashed_storage(self):
        self.call()
        value = next(iter(self.r2.objects.values()))
        authority = json.loads(value['Body']); authority['batches'][0]['file_ids'] = []
        value['Body'] = encoded(authority); value['Metadata']['sha256'] = digest(value['Body'])
        with self.assertRaisesRegex(intake.IntakeError, 'intake_authority_mismatch'): self.call()
        self.assertEqual(len(self.provider.posts), 2)

    def test_manual_main_origin_is_required(self):
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
               'GITHUB_REPOSITORY': 'owner/repo', 'GITHUB_WORKFLOW_REF': 'owner/repo/' + intake.WORKFLOW + '@refs/heads/main',
               'GITHUB_RUN_ID': '54321', 'GITHUB_SHA': 'c' * 40}
        intake.require_cloud_main(env)
        for key, value in (('GITHUB_EVENT_NAME', 'push'), ('GITHUB_REF', 'branch'), ('GITHUB_RUN_ID', 'PRIVATE'),
                           ('GITHUB_WORKFLOW_REF', 'owner/repo/other.yml@refs/heads/main')):
            with self.subTest(key=key), self.assertRaises(intake.IntakeError):
                intake.require_cloud_main({**env, key: value})

    def test_cli_emits_only_known_categories_and_never_private_unknown_error_text(self):
        output = self.root / 'summary.json'
        args = ['--input-dir', str(self.input), '--producer-json', str(self.root / 'PRIVATE.json'),
                '--archive-run-id', '12345', '--date-folder', '261002', '--expected-reports', '7',
                '--summary', str(output)]
        for error, category in ((intake.IntakeError('PRIVATE https://PRIVATE.invalid?secret=PRIVATE'), 'fresh_intake_failed'),
                                (intake.IntakeError('reviewed_fresh_intake_workflow_required'),
                                 'reviewed_fresh_intake_workflow_required')):
            with patch.object(intake, 'require_cloud_main', side_effect=error), patch('builtins.print') as printed:
                self.assertEqual(intake.main(args), 2)
            self.assertEqual(json.loads(output.read_bytes())['category'], category)
            self.assertNotIn('PRIVATE', output.read_text())
            self.assertNotIn('PRIVATE', str(printed.call_args_list))
        args[-1] = str(self.input / 'PRIVATE-summary.json')
        with patch.object(intake, 'require_cloud_main', side_effect=intake.IntakeError('PRIVATE')), \
                patch('builtins.print') as printed:
            self.assertEqual(intake.main(args), 2)
        self.assertNotIn('PRIVATE', str(printed.call_args_list))
        self.assertFalse((self.input / 'PRIVATE-summary.json').exists())

    def test_workflow_restores_full_originals_before_intake_without_source_or_pdf_generation(self):
        text = (Path(__file__).resolve().parents[1] / intake.WORKFLOW).read_text()
        self.assertLess(text.index('scripts/archive_market_views_originals.py restore'), text.index('scripts/intake_fresh_market_views_sources.py \\'))
        for forbidden in ('tesseract', 'build_market_views', 'upload-dir', 'seed_mineru_result_cache.py', 'workflow run'):
            self.assertNotIn(forbidden, text)
        self.assertIn('test_intake_fresh_market_views_sources.py', text)
        self.assertEqual(text.count('actions/upload-artifact@v4'), 1)


if __name__ == '__main__':
    unittest.main()
