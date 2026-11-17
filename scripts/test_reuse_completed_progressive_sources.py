"""Current-run success can feed translations without becoming a second publisher."""
import copy
import contextlib
import io
import json
import os
from pathlib import Path
import shutil
import unittest
from unittest.mock import patch

import progressive_wechat_delivery as progressive
import reuse_completed_progressive_sources as reuse
import wechat_editorial_binding as binding
import test_progressive_wechat_delivery as fixtures
import portal_translation_shards as translation


class ReuseTests(unittest.TestCase):
    def setUp(self):
        self.fixture = fixtures.ProgressiveTests()
        self.fixture.setUp()
        self.addCleanup(self.fixture.doCleanups)
        self.root, self.plan = self.fixture.root, self.fixture.plan
        self.store = self.fixture.store
        self.env = {'GITHUB_REPOSITORY': 'owner/reports', 'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main',
                    'GITHUB_WORKFLOW_REF': f'owner/reports/{reuse.DAILY}@refs/heads/main',
                    'GITHUB_RUN_ID': '1234', 'GITHUB_RUN_ATTEMPT': '1', 'GITHUB_SHA': 'a' * 40}
        self.run = {'id': 1234, 'path': reuse.DAILY, 'head_sha': 'a' * 40, 'head_branch': 'main',
                    'event': 'workflow_dispatch', 'run_attempt': 1, 'status': 'in_progress',
                    'repository': {'full_name': 'owner/reports'}, 'head_repository': {'full_name': 'owner/reports'}}
        common = {'run_id': 1234, 'head_sha': 'a' * 40, 'status': 'completed', 'conclusion': 'success'}
        self.jobs = {'total_count': 2, 'jobs': [{'id': 11, 'name': 'select-macro-reports', **common},
                     {'id': 12, 'name': reuse.PUBLISHER, **common, 'steps': [
                         {'name': name, 'status': 'completed', 'conclusion': 'success'} for name in reuse.STEPS]}]}
        self.api = patch.object(reuse, 'api', side_effect=lambda *_: copy.deepcopy(self.run)); self.api.start(); self.addCleanup(self.api.stop)
        self.job_mock = patch.object(reuse, 'jobs', side_effect=lambda *_: copy.deepcopy(self.jobs)); self.job_mock.start(); self.addCleanup(self.job_mock.stop)

    def snapshot(self, recovery=False):
        directories = self.fixture.materialize()
        originals = {}
        for source in self.plan['sources']:
            directory = directories[source['source_id']]
            (directory / 'source_mineru.md').write_text('The exact original extracted source text.\n')
            status = progressive.read_json(directory / 'status.json')
            name = source['source_pdf'] if recovery else '/runner/tmp/staged/' + source['staged_name']
            status.update(source_pdf=name, wechat_title='A report', wechat_title_source='source_filename_weighted_finetune',
                          wechat_editorial_model='fixture', wechat_title_decision={'needs_model_repair': False,
                          'selected_quality_issues': [], 'final_title_after_wording_guard': 'A report'})
            if recovery:
                status.update(source_method='mineru', source_markdown='source_mineru.md', wechat_source_provenance={
                    'source_kind': 'mineru-recovery', 'source_pdf': name, 'content_sha256': source['content_sha256'],
                    'source_receipt_sha256': 'b' * 64, 'source_report_id': 'R0001'})
            self.assertTrue(binding.bind_generated_article(directory, status))
            progressive.write_json(directory / 'status.json', status)
            originals[source['source_id']] = (directory / 'status.json').read_bytes()
            assets = directory / 'assets'; assets.mkdir(); (assets / 'chart.png').write_bytes(b'image-fixture')
        self.fixture.send(directories)
        self.fixture.presence()
        progressive.save_complete(self.plan, self.fixture.output, self.store, 'private', directories)
        return originals

    def execute(self):
        return reuse.reuse_sources('1234', '261116', 12, self.fixture.manifest, self.root / 'workspace',
                                   env=self.env, client=self.store, bucket='private')

    def test_absolute_primary_binding_survives_completion_and_export_roundtrip(self):
        originals = self.snapshot()
        before = dict(self.store.rows)
        with patch.object(progressive, 'upload_ready_groups', side_effect=AssertionError('no uploader')):
            result = self.execute()
        self.assertEqual(result['reuse'], 'true')
        self.assertEqual(result['article_count'], '12')
        self.assertEqual({key for key in self.store.rows if key not in before}, {result['article_handoff_prefix'] + '/shard_0.tar.gz'})
        self.assertTrue(all(self.store.rows[key] == value for key, value in before.items()))
        root = self.root / 'readback'
        progressive.download_directory(result['article_handoff_prefix'] + '/shard_0.tar.gz', root, client=self.store, bucket='private')
        receipt = reuse.validate_complete_handoff(root, '1234', '261116', result['manifest_sha256'], 12, 'a' * 40)
        for row in receipt['sources']:
            directory = root / row['directory']
            self.assertEqual((directory / 'status.json').read_bytes(), originals[row['source_id']])
            self.assertIsNotNone(binding.read_bound_article(directory))
            self.assertEqual((directory / 'assets/chart.png').read_bytes(), b'image-fixture')
        date = self.root / 'translation' / '261116'; date.mkdir(parents=True)
        shutil.copytree(root, date / 'shard_0')
        plan = translation.create_plan(date, reports_per_shard=5, source_prefix=result['article_handoff_prefix'])
        self.assertEqual(plan['source_count'], 12)
        self.assertTrue(all(row['relative_dir'].startswith('shard_0/report_') for row in plan['reports']))
        (root / receipt['sources'][0]['directory'] / 'assets/chart.png').write_bytes(b'changed')
        with self.assertRaisesRegex(ValueError, 'source_changed'):
            reuse.validate_complete_handoff(root, '1234', '261116', result['manifest_sha256'], 12)

    def test_recovery_original_name_binding_and_provenance_survive_complete_retry(self):
        originals = self.snapshot(recovery=True)
        target = self.root / 'completed'
        prefix = progressive.progressive_prefix('1234', '261116')
        progressive.download_directory(prefix + '/sources.tar.gz', target, client=self.store, bucket='private')
        marker, _ = progressive.read_object(self.store, 'private', prefix + '/complete.json')
        directories = progressive.completed_source_directories(self.plan, target, marker)
        for source_id, directory in directories.items():
            self.assertEqual((directory / 'status.json').read_bytes(), originals[source_id])
            self.assertIsNotNone(binding.read_bound_article(directory))
        with self.assertRaisesRegex(ValueError, 'binding_mismatch'):
            progressive.source_directories(self.plan, target)
        self.assertEqual(self.execute()['reuse'], 'true')

    def test_non_success_leaves_all_source_and_receipt_storage_untouched(self):
        for conclusion in ('failure', 'skipped', 'cancelled', 'timed_out'):
            self.jobs['jobs'][1]['conclusion'] = conclusion
            before = dict(self.store.rows)
            self.assertEqual(self.execute(), {'reuse': 'false'})
            self.assertEqual(before, self.store.rows)

    def test_wrong_attempt_sha_repo_and_duplicate_or_missing_marker_never_reuse(self):
        for key, bad in (('run_attempt', 2), ('head_sha', 'b' * 40), ('head_branch', 'dev'), ('path', 'other'), ('status', 'completed')):
            original = self.run[key]; self.run[key] = bad
            with self.assertRaisesRegex(ValueError, 'original_daily_changed'):
                self.execute()
            self.run[key] = original
        marker = self.jobs['jobs'][1]['steps'].pop()
        with self.assertRaisesRegex(ValueError, 'completion_unproven'):
            self.execute()
        self.jobs['jobs'][1]['steps'].extend([marker, marker])
        with self.assertRaisesRegex(ValueError, 'completion_unproven'):
            self.execute()

    def test_success_with_missing_marker_manifest_source_or_payload_fails_closed(self):
        self.snapshot()
        key = progressive.progressive_prefix('1234', '261116') + '/complete.json'
        saved = self.store.rows.pop(key)
        with self.assertRaisesRegex(ValueError, 'completion_missing'):
            self.execute()
        self.store.rows[key] = saved
        raw = self.fixture.manifest.read_bytes()
        self.fixture.manifest.write_bytes(raw + b'\n')
        with self.assertRaisesRegex(ValueError, 'manifest_changed'):
            self.execute()
        self.fixture.manifest.write_bytes(raw)
        source = self.plan['sources'][0]
        report = self.fixture.source_root / source['report_relative']
        (report / 'wechat_article.md').write_text('# A report\nUnbound replacement')
        progressive.save_complete(self.plan, self.fixture.output, self.store, 'private',
                                  {row['source_id']: self.fixture.source_root / row['report_relative'] for row in self.plan['sources']})
        with self.assertRaisesRegex(ValueError, 'editorial_binding_invalid'):
            self.execute()

    def test_completed_prefix_is_bound_to_run_date_manifest_and_exact_suffix(self):
        prefix = '_private-workflow-handoff/xhs-complete/1234/261116/' + 'a' * 64 + '/articles'
        self.assertEqual(translation.source_prefix_identity(prefix, '261116'), ('1234', 'a' * 64))
        for bad in (prefix + '/extra', prefix.replace('261116', '261115'), prefix.replace('1234/', '0/'), prefix.replace('a' * 64, 'invalid')):
            with self.assertRaises(ValueError):
                translation.source_prefix_identity(bad, '261116')

    def test_complete_payload_corruption_never_exports_or_falls_back(self):
        self.snapshot()
        payload = next(self.fixture.output.glob('draft_payload_*.json'))
        value = progressive.read_json(payload)
        value['articles'][0]['title'] = 'Unattested new title'
        progressive.write_json(payload, value)
        prefix = progressive.progressive_prefix('1234', '261116')
        progressive.upload_directory(self.fixture.output, prefix + '/complete.tar.gz', client=self.store, bucket='private')
        with self.assertRaisesRegex(ValueError, 'payload_changed'):
            self.execute()
        self.assertFalse(any('/xhs-complete/' in key for key in self.store.rows))

    def test_rerun_during_validation_cannot_export_old_attempt(self):
        self.snapshot()
        changed = {**self.run, 'run_attempt': 2}
        with patch.object(reuse, 'api', side_effect=[self.run, changed]):
            with self.assertRaisesRegex(ValueError, 'original_daily_changed'):
                self.execute()
        self.assertFalse(any('/xhs-complete/' in key for key in self.store.rows))

    def test_final_retry_requires_matching_complete_marker_before_original_alias(self):
        self.snapshot(recovery=True)
        prefix = progressive.progressive_prefix('1234', '261116')
        root = self.root / 'complete-retry'
        progressive.download_directory(prefix + '/sources.tar.gz', root, client=self.store, bucket='private')
        with self.assertRaisesRegex(ValueError, 'complete_owner_changed'):
            progressive.completed_source_directories(self.plan, root, {'plan_sha256': 'b' * 64, 'complete': True})

    def test_cli_explicit_false_output_and_failure_never_dump_provider_text(self):
        output = self.root / 'github-output'
        args = ['--source-run-id', '1234', '--date-folder', '261116', '--expected-articles', '12',
                '--workspace', str(self.root / 'workspace'), '--output-github', str(output)]
        with patch.object(reuse, 'reuse_sources', return_value={'reuse': 'false'}):
            self.assertEqual(reuse.main(args), 0)
        self.assertEqual(output.read_text(), 'reuse=false\n')
        printed = io.StringIO()
        with (patch.object(reuse, 'reuse_sources', side_effect=RuntimeError('private-provider-body')),
                contextlib.redirect_stdout(printed)):
            self.assertEqual(reuse.main(args), 1)
        self.assertEqual(printed.getvalue(), 'completed_primary_source_reuse_failed\n')
        self.assertEqual(output.read_text(), 'reuse=false\n')

    def test_transient_job_inventory_drift_restarts_full_identity_then_exports_once(self):
        self.snapshot()
        before = dict(self.store.rows)
        with (patch.object(reuse, 'jobs', side_effect=[reuse.DeliveryError('delivery_jobs_changed'), self.jobs, self.jobs]) as jobs,
              patch.object(reuse, 'api', return_value=self.run) as api,
              patch.object(reuse.time, 'sleep') as sleep):
            result = self.execute()
        self.assertEqual(result['reuse'], 'true')
        self.assertEqual(api.call_count, 3)
        self.assertEqual(jobs.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1])
        self.assertEqual(set(self.store.rows) - set(before), {result['article_handoff_prefix'] + '/shard_0.tar.gz'})
        self.assertTrue(all(self.store.rows[key] == value for key, value in before.items()))

    def test_three_transient_inventory_failures_leave_r2_untouched(self):
        before = dict(self.store.rows)
        with (patch.object(reuse, 'jobs', side_effect=reuse.DeliveryError('delivery_jobs_incomplete')) as jobs,
              patch.object(reuse, 'api', return_value=self.run) as api,
              patch.object(reuse.time, 'sleep') as sleep):
            with self.assertRaisesRegex(reuse.DeliveryError, 'delivery_jobs_incomplete'):
                self.execute()
        self.assertEqual(api.call_count, 3)
        self.assertEqual(jobs.call_count, 3)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1, 3])
        self.assertEqual(before, self.store.rows)

    def test_transport_retry_still_rejects_changed_identity_without_another_retry(self):
        before = dict(self.store.rows)
        with (patch.object(reuse, 'api', side_effect=[reuse.DeliveryError('delivery_github_metadata_failed'),
                                                   {**self.run, 'run_attempt': 2}]) as api,
              patch.object(reuse, 'jobs') as jobs,
              patch.object(reuse.time, 'sleep') as sleep):
            with self.assertRaisesRegex(reuse.ReuseError, 'original_daily_changed'):
                self.execute()
        self.assertEqual(api.call_count, 2)
        jobs.assert_not_called()
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1])
        self.assertEqual(before, self.store.rows)

    def test_export_recheck_exhaustion_keeps_all_r2_objects_unchanged(self):
        self.snapshot()
        before = dict(self.store.rows)
        failure = reuse.DeliveryError('delivery_jobs_changed')
        with (patch.object(reuse, 'jobs', side_effect=[self.jobs, failure, failure, failure]) as jobs,
              patch.object(reuse, 'api', return_value=self.run) as api,
              patch.object(reuse.time, 'sleep') as sleep):
            with self.assertRaisesRegex(reuse.DeliveryError, 'delivery_jobs_changed'):
                self.execute()
        self.assertEqual(api.call_count, 4)
        self.assertEqual(jobs.call_count, 4)
        self.assertEqual([call.args[0] for call in sleep.call_args_list], [1, 3])
        self.assertEqual(before, self.store.rows)

    def test_nontransient_metadata_and_invalid_marker_fail_immediately(self):
        with (patch.object(reuse, 'api', side_effect=reuse.DeliveryError('delivery_github_metadata_invalid')) as api,
              patch.object(reuse.time, 'sleep') as sleep):
            with self.assertRaisesRegex(reuse.DeliveryError, 'metadata_invalid'):
                self.execute()
        api.assert_called_once()
        sleep.assert_not_called()
        self.jobs['jobs'][1]['steps'].pop()
        with patch.object(reuse.time, 'sleep') as sleep:
            with self.assertRaisesRegex(reuse.ReuseError, 'completion_unproven'):
                self.execute()
        sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
