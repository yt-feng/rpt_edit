import json
import io
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

import inspect_recovered_wechat_delivery as module
from inspect_recovered_wechat_delivery import summarize


class ReceiptCountsTests(unittest.TestCase):
    def test_counts_require_successful_readback_and_exclude_private_fields(self):
        secret = 'private title and media value'
        drafts = [
            {'account': 'kc', 'article_count': 3, 'media_id': secret, 'titles': [secret],
             'status': 'verified', 'draft_get': {'ok': True, 'article_count': 3}},
            {'account': 'tt', 'article_count': 2, 'media_id': secret, 'status': 'pending_verification'},
            {'account': 'pankou', 'article_count': 1, 'media_id': secret, 'status': 'verified',
             'draft_get': {'ok': True, 'article_count': 2}},
        ]
        result = summarize({'date_folder': '261112', 'dry_run': False, 'drafts': drafts}, '261112')
        self.assertEqual(result['accepted_articles_by_account'], {'kc': 3, 'tt': 2, 'pankou': 1})
        self.assertEqual(result['verified_articles_by_account'], {'kc': 3, 'tt': 0, 'pankou': 0})
        self.assertEqual(result['pending_readback_drafts'], 2)
        self.assertNotIn(secret, json.dumps(result))

    def test_rejects_dry_runs_unknown_accounts_and_duplicate_media(self):
        draft = {'account': 'kc', 'article_count': 3, 'media_id': 'same', 'status': 'verified',
                 'draft_get': {'ok': True, 'article_count': 3}}
        for changes in ({'dry_run': True}, {'drafts': [draft, draft]},
                        {'drafts': [{**draft, 'account': 'private account'}]},
                        {'drafts': [{**draft, 'article_count': True}]},
                        {'date_folder': '261111'}):
            with self.subTest(changes=changes), self.assertRaises(ValueError):
                summarize({'date_folder': '261112', 'dry_run': False, 'drafts': [draft], **changes}, '261112')

    def test_reads_only_a_claimed_main_daily_checkpoint(self):
        identity = {'source_run_id': '123', 'date_folder': '261112', 'manifest_sha256': 'a' * 64}
        run = {'id': 123, 'path': module.DAILY, 'head_branch': 'main', 'event': 'workflow_dispatch',
               'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'}}

        class ReadOnlyStore:
            def get_object(self, **kwargs):
                return {'Body': io.BytesIO(json.dumps(identity).encode())}

        def restore(key, destination, *, client, bucket):
            self.assertIsInstance(client, module.ReadOnlyClient)
            self.assertTrue(key.startswith('_private-workflow-handoff/xhs-recovery/123/261112/'))
            destination.mkdir()
            (destination / 'wechat_draft_summary.json').write_text(json.dumps(
                {'date_folder': '261112', 'dry_run': False, 'drafts': []}))

        with tempfile.TemporaryDirectory() as temporary, \
                patch.object(module, 'exact_head', return_value={'ContentLength': 100}), \
                patch.object(module, 'download_directory', side_effect=restore) as download:
            result = module.inspect(ReadOnlyStore(), 'bucket', run, 'owner/repo', '123',
                                    '261112', 'a' * 64, Path(temporary))
            self.assertEqual(result['status'], 'checkpoint_read')
            self.assertEqual(result['checkpoint_bytes'], 100)
            self.assertEqual(download.call_count, 1)
            for metadata, run_id, manifest in (({**run, 'head_branch': 'feature'}, '123', 'a' * 64),
                                                (run, '124', 'a' * 64),
                                                (run, '123', 'b' * 64)):
                with self.assertRaises(ValueError):
                    module.inspect(ReadOnlyStore(), 'bucket', metadata, 'owner/repo', run_id,
                                   '261112', manifest, Path(temporary))
            self.assertEqual(download.call_count, 1)


if __name__ == '__main__':
    unittest.main()
