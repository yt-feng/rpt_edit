#!/usr/bin/env python3
"""Per-report ready handoffs preserve the real producer's success semantics."""
import contextlib
import io
import json
import os
from pathlib import Path
import sys
import subprocess
import tarfile
import tempfile
from types import SimpleNamespace
import unittest
from unittest.mock import Mock, patch

import finalize_outputs as finalize
import pdf_to_xhs_batch as producer
import postprocess_podcast as postprocess
import private_workflow_handoff as handoff
import progressive_wechat_ready as ready
import run_pdf_to_xhs_in_batches as wrapper
import sensitive_content_guard as guard
import wechat_editorial_binding as binding
from test_progressive_wechat_workflow import workflow


class ReadyTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.pdf = self.root / '0001-01-BIS-source.pdf'; self.pdf.write_bytes(b'exact original PDF')
        self.out = self.root / 'shard_0'; self.out.mkdir()
        self.item = self.out / producer.slug(self.pdf.name); self.item.mkdir()
        self.manifest = self.root / 'selected_to_process_manifest.json'
        self.manifest.write_text(json.dumps([{'name': 'BIS-source.pdf', 'process_local_path': str(self.root / '01-BIS-source.pdf'),
            'content_sha256': ready.sha256(self.pdf.read_bytes())}]))
        self.source_map = self.root / 'mineru-source-map.json'
        self.source_map.write_text(json.dumps({'schema': 1, 'files': {self.pdf.name: {
            'source': '01-BIS-source.pdf', 'sha256': ready.sha256(self.pdf.read_bytes()), 'size': self.pdf.stat().st_size}}}))
        self.env = {'DAILY_PROGRESSIVE_WECHAT_READY': 'true', 'GITHUB_ACTIONS': 'true',
            'GITHUB_REPOSITORY': ready.REPOSITORY, 'GITHUB_REF': 'refs/heads/main',
            'GITHUB_WORKFLOW_REF': f'{ready.REPOSITORY}/{ready.WORKFLOW}@refs/heads/main',
            'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_RUN_ID': '123', 'GITHUB_SHA': 'a' * 40,
            'DATE_FOLDER': '261116', 'PROGRESSIVE_WECHAT_MANIFEST': str(self.manifest),
            'PROGRESSIVE_WECHAT_FINALIZE_API_KEY': 'test-finalize-key', 'GH_TOKEN': 'test-token', 'R2_BUCKET': 'private'}
        self.args = SimpleNamespace(model='deepseek-flash', deepseek_base_url='https://api.deepseek.com', mineru_source_map=str(self.source_map))
        title = '国际清算银行：企业交付数量出现变化'
        (self.item / 'source_mineru.md').write_text('Original extraction remains immutable.\n')
        (self.item / 'wechat_article.md').write_text(f'# {title}\n\n企业交付保持稳定。\n')
        self.status = {'source_pdf': str(self.pdf), 'original_pdf_sha256': ready.sha256(self.pdf.read_bytes()),
            'wechat_article': 'wechat_article.md', 'wechat_title': title,
            'wechat_title_source': 'source_filename_weighted_finetune', 'wechat_editorial_model': self.args.model,
            'wechat_title_decision': {'needs_model_repair': False, 'selected_quality_issues': [],
                                     'final_title_after_wording_guard': title}}
        self.assertTrue(binding.bind_generated_article(self.item, self.status))
        (self.item / 'status.json').write_text(json.dumps(self.status, ensure_ascii=False))

    def snapshot(self):
        return {p.relative_to(self.out).as_posix(): p.read_bytes() for p in self.out.rglob('*') if p.is_file()}

    def publish(self, upload=None):
        with patch.object(ready, 'bounded_r2_client', return_value=object()), \
                patch.object(handoff, 'upload_directory', side_effect=upload) as uploaded, \
                patch.object(ready.requests, 'post', return_value=SimpleNamespace(status_code=204)) as post, \
                patch.object(guard, 'free_api_check', return_value={'hit': False, 'hits': [], 'errors': []}), \
                patch.object(postprocess, 'find_original_images', return_value=['assets/chart.png']), \
                patch.object(postprocess, 'call_deepseek', side_effect=AssertionError('No additional copy')), \
                patch.object(finalize, 'generate_zhihu_for_item', side_effect=AssertionError('No early Zhihu')):
            ready.publish_ready(self.pdf, self.item, self.args, env=self.env)
        return uploaded, post

    def test_ready_archive_binds_original_manifest_and_body_before_single_notification(self):
        originals = (self.item / 'source_mineru.md').read_bytes()
        captured = {}
        def upload(source, key, **kwargs):
            archive = self.root / 'ready.tar.gz'; handoff.create_archive(source, archive)
            with tarfile.open(archive) as opened:
                captured['names'] = opened.getnames()
                captured['identity'] = json.load(opened.extractfile('progressive_source.json'))
                captured['article'] = opened.extractfile('wechat_article.md').read().decode()
            captured['key'] = key
            self.assertIsNotNone(binding.read_bound_article(source))
        uploaded, post = self.publish(upload)
        uploaded.assert_called_once(); post.assert_called_once()
        identity = captured['identity']
        self.assertEqual(identity, {'schema_version': 1, 'source_run_id': '123', 'source_execution_sha': 'a' * 40,
            'date_folder': '261116', 'source_pdf': '01-BIS-source.pdf', 'content_sha256': ready.sha256(self.pdf.read_bytes()),
            'manifest_sha256': ready.sha256(self.manifest.read_bytes())})
        source_id = ready.sha256(('01-BIS-source.pdf\0' + identity['content_sha256']).encode())
        self.assertEqual(captured['key'], f'_private-workflow-handoff/xhs-ready/123/261116/source_{source_id}.tar.gz')
        self.assertIn('assets/chart.png', captured['article'])
        self.assertIn('For informational purposes only.', captured['article'])
        self.assertIn('status.json', captured['names'])
        self.assertFalse(any(name.startswith(self.item.name + '/') for name in captured['names']))
        self.assertEqual((self.item / 'source_mineru.md').read_bytes(), originals)
        self.assertIsNotNone(binding.read_bound_article(self.item))
        self.assertEqual(post.call_args.kwargs['json'], {'ref': 'main', 'inputs': {'source_run_id': '123', 'date_folder': '261116'}})
        self.assertFalse(post.call_args.kwargs['allow_redirects'])
        self.assertEqual(post.call_args.kwargs['timeout'], (5, 15))

    def test_full_shard_repeat_preserves_binding_and_reuses_the_paid_guard_cache(self):
        self.publish()
        with patch.object(postprocess, 'find_original_images', return_value=['assets/chart.png']), \
                patch.object(guard, 'free_api_check', side_effect=AssertionError('already checked')) as api:
            ready.prepare_article(self.out, self.item, self.args)
        api.assert_not_called()
        self.assertIsNotNone(binding.read_bound_article(self.item))

    def test_original_hash_status_and_manifest_must_all_agree_before_any_work(self):
        original_status = (self.item / 'status.json').read_bytes()
        for change in ('pdf', 'status', 'manifest', 'producer', 'article'):
            with self.subTest(change=change), patch.object(ready, 'prepare_article') as prepare, \
                    patch.object(handoff, 'upload_directory') as upload, patch.object(ready.requests, 'post') as post:
                before_pdf, before_manifest = self.pdf.read_bytes(), self.manifest.read_bytes()
                before_article = (self.item / 'wechat_article.md').read_bytes()
                env = dict(self.env)
                if change == 'pdf': self.pdf.write_bytes(b'different original')
                if change == 'status':
                    (self.item / 'status.json').write_text(json.dumps({**self.status, 'original_pdf_sha256': 'b' * 64}))
                if change == 'manifest': self.manifest.write_text('[]')
                if change == 'producer': env['GITHUB_REF'] = 'refs/heads/untrusted'
                if change == 'article': (self.item / 'wechat_article.md').write_text('Changed outside producer')
                with self.assertRaises(ValueError): ready.publish_ready(self.pdf, self.item, self.args, env=env)
                prepare.assert_not_called(); upload.assert_not_called(); post.assert_not_called()
                self.pdf.write_bytes(before_pdf); self.manifest.write_bytes(before_manifest)
                (self.item / 'status.json').write_bytes(original_status)
                (self.item / 'wechat_article.md').write_bytes(before_article)

    def test_daily_and_manual_dates_accept_real_six_or_eight_digit_dates_only(self):
        for day in ('261116', '20261116'):
            self.assertEqual(ready.source_identity(self.pdf, self.item, self.args,
                {**self.env, 'DATE_FOLDER': day})['date_folder'], day)
        for day in ('261399', '20261399', '../261116'):
            with self.assertRaises(ValueError):
                ready.source_identity(self.pdf, self.item, self.args, {**self.env, 'DATE_FOLDER': day})

    def test_guard_import_error_api_error_and_broken_binding_leave_originals_unchanged(self):
        for failure in ('import', 'api', 'binding'):
            with self.subTest(failure=failure), contextlib.ExitStack() as stack:
                before = self.snapshot()
                stack.enter_context(patch.object(ready, 'bounded_r2_client', return_value=object()))
                upload = stack.enter_context(patch.object(handoff, 'upload_directory'))
                stack.enter_context(patch.object(guard, 'free_api_check', return_value={
                    'hit': False, 'hits': [], 'errors': ['unavailable'] if failure == 'api' else []}))
                if failure == 'import': stack.enter_context(patch.object(finalize, 'run_sensitive_guard', None))
                if failure == 'binding': stack.enter_context(patch.object(binding, 'advance_binding', return_value=False))
                with self.assertRaises(ValueError): ready.publish_ready(self.pdf, self.item, self.args, env=self.env)
                upload.assert_not_called()
                self.assertEqual(self.snapshot(), before)

    def test_unknown_notification_never_reposts_or_prints_exception_payload(self):
        for error in (RuntimeError('private-body-token'), SystemExit('private-body-token')):
            output = io.StringIO()
            with patch.dict(os.environ, self.env, clear=True), \
                    patch.object(ready, 'publish_ready', side_effect=error) as publish, \
                    contextlib.redirect_stdout(output):
                ready.try_publish_ready(self.pdf, self.item, self.args)
            publish.assert_called_once()
            self.assertNotIn('private-body-token', output.getvalue())
            self.assertIn(f'deferred ({type(error).__name__})', output.getvalue())
        with patch.object(ready.requests, 'post', side_effect=TimeoutError('private response')) as post:
            with self.assertRaises(TimeoutError):
                ready.notify_publisher({'source_run_id': '123', 'date_folder': '261116'}, self.env)
        post.assert_called_once()

    def test_failed_r2_upload_does_not_notify_and_keeps_valid_source_for_shard_fallback(self):
        with self.assertRaisesRegex(RuntimeError, 'upload unavailable'):
            self.publish(lambda *args, **kwargs: (_ for _ in ()).throw(RuntimeError('upload unavailable')))
        self.assertIsNotNone(binding.read_bound_article(self.item))
        self.assertFalse(json.loads((self.item / 'status.json').read_bytes()).get('error'))

    def test_actual_wrapper_source_map_and_primary_cli_emit_the_pre_staging_source_identity(self):
        original_dir = self.root / 'selected'; original_dir.mkdir()
        original = original_dir / '01-BIS-source.pdf'; original.write_bytes(self.pdf.read_bytes())
        self.manifest.write_text(json.dumps([{'name': 'BIS-source.pdf', 'process_local_path': str(original),
            'content_sha256': ready.sha256(original.read_bytes())}]))
        args = producer.build_arg_parser().parse_args(['--input-dir', str(original_dir), '--output-dir', str(self.out)])
        identities = []
        def generation(pdf, row, output, args):
            self.assertNotEqual(pdf.name, original.name)
            item = output / producer.slug(pdf.name)
            item.mkdir(exist_ok=True)
            (item / 'source_mineru.md').write_text('Source text')
            (item / 'wechat_article.md').write_text('# ' + self.status['wechat_title'] + '\n\n企业交付稳定。\n')
            status = {**self.status, 'source_pdf': str(pdf)}
            self.assertTrue(binding.bind_generated_article(item, status))
            (item / 'status.json').write_text(json.dumps(status, ensure_ascii=False))
            return status
        def child(cmd, outcome_path, **kwargs):
            with patch.object(sys, 'argv', cmd[1:]):
                return subprocess.CompletedProcess(cmd, producer.main()), 1
        def upload(path, key, **kwargs):
            identities.append(json.loads((path / 'progressive_source.json').read_bytes()))
        with patch.dict(os.environ, {**self.env, 'MINER_U': 'test'}, clear=True), \
                patch.object(wrapper, 'run_pending_task_attempts', side_effect=child), \
                patch.object(producer, 'from_environment', return_value=SimpleNamespace(scope='dropbox')), \
                patch('institution_original_cache.preserve_sources'), \
                patch.object(producer, 'run_source_batch', side_effect=lambda ledger, sources, **kw: (
                    {path: {'state': 'done'} for path, name in sources}, {'ready_for_generation': True, 'pending': 0, 'failed': 0})), \
                patch.object(producer, 'result_cache_contexts', return_value=(None, {})), \
                patch.object(producer, 'process_pdf', side_effect=generation), \
                patch.object(ready, 'bounded_r2_client', return_value=object()), \
                patch.object(handoff, 'upload_directory', side_effect=upload), \
                patch.object(ready.requests, 'post', return_value=SimpleNamespace(status_code=204)) as post, \
                patch.object(guard, 'free_api_check', return_value={'hit': False, 'hits': [], 'errors': []}), \
                contextlib.redirect_stdout(io.StringIO()):
            result = wrapper.run_batch(1, [(1, original)], args)
        self.assertEqual(result['returncode'], 0)
        self.assertEqual(len(identities), 1)
        self.assertEqual(identities[0]['source_pdf'], original.name)
        self.assertEqual(identities[0]['manifest_sha256'], ready.sha256(self.manifest.read_bytes()))
        post.assert_called_once()

    def test_finalize_credentials_restore_after_error_without_touching_generation_context(self):
        with patch.dict(os.environ, {'DEEPSEEK_API_KEY': 'notes-key', 'DEEPSEEK_USAGE_STAGE': 'report-notes'}):
            with self.assertRaises(RuntimeError):
                with ready.finalize_environment(self.env):
                    self.assertEqual(os.environ['DEEPSEEK_API_KEY'], 'test-finalize-key')
                    raise RuntimeError('stop')
            self.assertEqual(os.environ['DEEPSEEK_API_KEY'], 'notes-key')
            self.assertEqual(os.environ['DEEPSEEK_USAGE_STAGE'], 'report-notes')

    def test_real_primary_cli_calls_hook_after_success_and_keeps_success_after_hook_error(self):
        argv = ['producer', '--input-dir', str(self.root), '--output-dir', str(self.out), '--mineru-source-map', str(self.source_map)]
        for enabled, status, calls, result in ((True, self.status, 1, 0), (False, self.status, 0, 0),
                                             (True, {'error': 'generation failed'}, 0, 2)):
            with self.subTest(enabled=enabled, result=result), patch.object(sys, 'argv', argv), \
                    patch.dict(os.environ, {'MINER_U': 'test', 'DAILY_PROGRESSIVE_WECHAT_READY': str(enabled).lower()}, clear=True), \
                    patch.object(producer, 'find_pdfs', return_value=[self.pdf]), \
                    patch.object(producer, 'from_environment', return_value=SimpleNamespace(scope='dropbox')), \
                    patch('institution_original_cache.preserve_sources'), \
                    patch.object(producer, 'run_source_batch', return_value=({self.pdf: {'state': 'done'}},
                        {'ready_for_generation': True, 'pending': 0, 'failed': 0})), \
                    patch.object(producer, 'result_cache_contexts', return_value=(None, {})), \
                    patch.object(producer, 'process_pdf', return_value=status), \
                    patch.object(ready, 'try_publish_ready', side_effect=RuntimeError('private details')) as hook, \
                    contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                self.assertEqual(producer.main(), result)
                self.assertEqual(hook.call_count, calls)
                self.assertEqual(json.loads((self.out / 'summary.json').read_bytes()), [status])

    def test_daily_only_opt_in_keeps_full_shard_and_all_other_features(self):
        daily = workflow('dropbox-latest-pdf-to-xhs-sharded.yml')
        steps = daily['jobs']['process-shard']['steps']
        generate = next(step for step in steps if step.get('name') == 'Generate shard outputs')
        env = generate['env']
        self.assertEqual(env['GH_TOKEN'], '${{ github.token }}')
        self.assertIn("wechat_draft_source == 'xhs_notes'", env['DAILY_PROGRESSIVE_WECHAT_READY'])
        self.assertIn("wechat_freepublish != 'true'", env['DAILY_PROGRESSIVE_WECHAT_READY'])
        self.assertEqual(env['PROGRESSIVE_WECHAT_MANIFEST'], '_selected_macro_manifest/selected_to_process_manifest.json')
        self.assertIn('DEEPSEEK_FINALIZE_API_KEY', env['PROGRESSIVE_WECHAT_FINALIZE_API_KEY'])
        names = [step.get('name') for step in steps]
        for name in ('Attach original images without additional copy generation', 'Finalize shard outputs',
                     'Wake short progressive WeChat publisher'):
            self.assertGreater(names.index(name), names.index('Generate shard outputs'))


if __name__ == '__main__':
    unittest.main()
