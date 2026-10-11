import copy
from contextlib import redirect_stdout
import hashlib
import io
import json
from pathlib import Path
import tarfile
import tempfile
import unittest
from unittest.mock import patch

import restore_wechat_image_repair_receipts as restore
from push_portal_translated_to_wechat_drafts import draft_group_key


class ReadOnlyStore:
    def __init__(self, objects):
        self.objects = objects
        self.reads = []

    def head_object(self, *, Bucket, Key):
        self.reads.append(('head', Key))
        raw = self.objects[Key]
        return {'ContentLength': len(raw), 'Metadata': {'sha256': hashlib.sha256(raw).hexdigest()}}

    def get_object(self, *, Bucket, Key):
        self.reads.append(('get', Key))
        return {'Body': io.BytesIO(self.objects[Key])}

    def __getattr__(self, name):
        raise AssertionError('No write operation allowed: ' + name)


def archive(root):
    data = io.BytesIO()
    with tarfile.open(fileobj=data, mode='w:gz') as target:
        for path in root.rglob('*'):
            if path.is_file():
                target.add(path, arcname=path.relative_to(root).as_posix())
    return data.getvalue()


class RestoreTest(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.checkpoint = self.root / 'checkpoint'
        self.receipts = self.root / 'receipts'
        (self.checkpoint / 'articles').mkdir(parents=True)
        self.receipts.mkdir()
        self.context = {'schema_version': 1, 'source_run_id': restore.SOURCE_RUN_ID,
                        'source_handoff_run_id': restore.HANDOFF_RUN_ID, 'source_kind': 'ocr-pages',
                        'date_folder': restore.DATE_FOLDER, 'expected_articles': restore.EXPECTED_REPORTS,
                        'manifest_sha256': restore.MANIFEST_SHA256,
                        'source_execution_sha': 'a' * 40, 'handoff_execution_sha': 'b' * 40,
                        'source_receipt_sha256': 'c' * 64}
        self.article_receipt = {'reports': [{'directory': f'report_{i:04d}_' + 'd' * 12} for i in range(44)]}
        self.write(self.checkpoint / 'context.json', self.context)
        self.write(self.checkpoint / 'articles' / restore.delivery.ARTICLE_RECEIPT, self.article_receipt)
        self.write(self.receipts / 'delivery_identity.json', restore.delivery.delivery_identity(self.context, self.checkpoint / 'articles'))
        self.summary = {'dry_run': False, 'publish': False, 'status': 'verified', 'date_folder': restore.DATE_FOLDER,
                        'draft_count': 6, 'selected_count': 44, 'input_selected_count': 44,
                        'skipped_title_policy_count': 0, 'skipped_generation_failure_count': 0,
                        'articles': [{'report_dir': row['directory']} for row in self.article_receipt['reports']],
                        'drafts': []}
        for group, start in enumerate(range(0, 44, 8)):
            articles = [{'title': 'Private article ' + str(i), 'content': '<p>Private text ' + str(i) + '</p>'}
                        for i in range(start, min(start + 8, 44))]
            name = f'draft_payload_{group:02d}.json'
            self.write(self.receipts / name, {'articles': articles})
            self.summary['drafts'].append({'media_id': f'existing-{group}', 'group_key': draft_group_key(articles),
                'payload': name, 'article_count': len(articles), 'status': 'verified',
                'draft_get': dict(ok=True, matches_editorial_contract=True, matches_expected_article_count=True,
                                  matches_expected_titles=True, article_count=len(articles))})
        self.write(self.receipts / 'wechat_draft_summary.json', self.summary)
        self.run = {'id': int(restore.ACCEPTED_RUN_ID), 'path': restore.delivery.WORKFLOW,
                    'status': 'completed', 'conclusion': 'success', 'event': 'workflow_dispatch',
                    'head_branch': 'main', 'repository': {'full_name': 'owner/repo'},
                    'head_repository': {'full_name': 'owner/repo'}, 'run_attempt': 1, 'head_sha': 'e' * 40}
        steps = ['Upload drafts and require exact article readback', 'Save accepted draft receipts even after interruption',
                 'Verify full delivery before archiving Blog articles']
        self.jobs = {'jobs': [dict(id=1 if name == 'generate' else restore.ACCEPTED_DELIVERY_JOB_ID,
                                  name=name, run_id=int(restore.ACCEPTED_RUN_ID), head_sha=self.run['head_sha'],
                                  status='completed', conclusion='success',
                                  steps=[{'name': step, 'conclusion': 'success'} for step in steps])
                              for name in ('generate', 'deliver')]}

    def write(self, path, value):
        path.write_text(json.dumps(value))

    def store(self):
        prefix = f'_private-workflow-handoff/xhs-recovery/{restore.SOURCE_RUN_ID}/{restore.DATE_FOLDER}/{restore.MANIFEST_SHA256}'
        return ReadOnlyStore({prefix + '/generation.tar.gz': archive(self.checkpoint),
                              prefix + '/wechat-receipts.tar.gz': archive(self.receipts)})

    def execute(self, store=None, source=None):
        store = store or self.store()
        with patch.object(restore.delivery, 'api', return_value=self.run), \
             patch.object(restore.delivery, 'jobs', return_value=self.jobs), \
             patch.object(restore.delivery, 'article_receipt', return_value=self.article_receipt) as validator:
            result = restore.restore(self.root / 'output', source or restore.ACCEPTED_RUN_ID, 'owner/repo', store, 'private')
        validator.assert_called_once()
        return result, store

    def test_restores_exact_receipts_without_models_or_store_writes(self):
        result, store = self.execute()
        self.assertEqual((result['article_count'], result['draft_count']), (44, 6))
        self.assertEqual((result['object_writes'], result['model_calls'], result['wechat_writes']), (0, 0, 0))
        self.assertEqual(sum(kind == 'get' for kind, key in store.reads), 2)
        drafts = restore.load_drafts(self.root / 'output')
        self.assertEqual(len(drafts), 6)
        self.assertNotIn('Private text', json.dumps(result))
        self.assertNotIn('existing-0', json.dumps(result))
        self.assertFalse((self.root / 'output' / 'articles').exists())

    def test_rejects_unknown_run_without_any_storage_reads(self):
        store = self.store()
        with self.assertRaisesRegex(restore.RestoreError, 'unsupported_recovery_run'):
            self.execute(store, '123456')
        self.assertEqual(store.reads, [])

    def test_rejects_failed_or_wrong_workflow_and_changed_attempt_before_restore(self):
        baseline = copy.deepcopy(self.run)
        for key, value in [('conclusion', 'failure'), ('path', 'wrong.yml'), ('run_attempt', 2),
                           ('head_branch', 'feature'), ('head_repository', {'full_name': 'other/repo'})]:
            self.run = {**baseline, key: value}
            store = self.store()
            with self.subTest(key=key), self.assertRaises(restore.RestoreError):
                self.execute(store)
            self.assertEqual(store.reads, [])

    def test_requires_exact_successful_delivery_and_saved_readback(self):
        self.jobs['jobs'][1]['steps'][1]['conclusion'] = 'failure'
        with self.assertRaisesRegex(restore.RestoreError, 'accepted_receipt_steps_incomplete'):
            self.execute()

    def test_rejects_context_or_receipt_identity_changes(self):
        self.context['manifest_sha256'] = 'f' * 64
        self.write(self.checkpoint / 'context.json', self.context)
        with self.assertRaisesRegex(restore.RestoreError, 'source_context_mismatch'):
            self.execute()
        self.assertFalse((self.root / 'output').exists())

    def test_rejects_wrong_delivery_hash(self):
        identity = restore.delivery.delivery_identity(self.context, self.checkpoint / 'articles')
        identity['article_receipt_sha256'] = '0' * 64
        self.write(self.receipts / 'delivery_identity.json', identity)
        with self.assertRaisesRegex(restore.RestoreError, 'delivery_identity_mismatch'):
            self.execute()

    def test_rejects_missing_article_and_missing_original_readback(self):
        self.summary['drafts'][0]['draft_get']['matches_editorial_contract'] = False
        self.write(self.receipts / 'wechat_draft_summary.json', self.summary)
        with self.assertRaisesRegex(restore.RestoreError, 'accepted_readback_incomplete'):
            self.execute()

    def test_rejects_payload_body_changed_after_receipt(self):
        path = self.receipts / self.summary['drafts'][0]['payload']
        value = json.loads(path.read_text())
        value['articles'][0]['content'] = 'unrelated content'
        self.write(path, value)
        with self.assertRaisesRegex(restore.RestoreError, 'accepted_payload_identity_mismatch'):
            self.execute()

    def test_rejects_unaccounted_payload(self):
        self.write(self.receipts / 'draft_payload_unknown.json', {'articles': [{'title': 'Unrelated'}]})
        with self.assertRaisesRegex(restore.RestoreError, 'unaccounted_payload'):
            self.execute()

    def test_workflow_separates_artifact_and_private_receipt_reads(self):
        text = (Path(__file__).resolve().parents[1] / restore.WORKFLOW).read_text()
        self.assertIn('options: [successful-artifact, recovered-261007]', text)
        self.assertIn("if: inputs.receipt_source == 'successful-artifact'", text)
        self.assertIn("if: inputs.receipt_source == 'recovered-261007'", text)
        self.assertIn('scripts/restore_wechat_image_repair_receipts.py', text)
        self.assertNotIn('restore-delivery --workspace', text)
        self.assertNotIn('save-receipts --workspace', text)

    def test_cli_rejects_unapproved_workflow_before_storage_or_models(self):
        report = self.root / 'report.json'
        with patch.dict('os.environ', {'GITHUB_REF': 'refs/heads/feature'}, clear=True), \
             patch.object(restore, 'build_client') as client, redirect_stdout(io.StringIO()):
            code = restore.main(['--source-run-id', restore.ACCEPTED_RUN_ID, '--destination', str(self.root / 'out'), '--report', str(report)])
        self.assertEqual(code, 1)
        client.assert_not_called()
        self.assertEqual(json.loads(report.read_text())['category'], 'repair_main_workflow_required')


if __name__ == '__main__':
    unittest.main()
