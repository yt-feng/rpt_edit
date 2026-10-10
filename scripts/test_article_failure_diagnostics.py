"""Private exception evidence survives independent-report recovery and archive restore."""
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import shutil
import sys
import traceback
import unittest
from unittest.mock import patch

import article_generation_progress as progress
import pdf_to_xhs_batch as producer
import recover_report_articles as articles
import recovered_article_delivery as delivery
import test_article_title_resume as fixtures


class PrivateFailureTests(unittest.TestCase):
    def fixture(self, count=2):
        self.case = fixtures.ResumeTests()
        self.addCleanup(self.case.doCleanups)
        with redirect_stdout(io.StringIO()):
            self.case.fixture(count)
        self.output = self.case.output
        self.failures = self.output.parent / 'private-diagnostics/article-failures'

    def records(self):
        return [json.loads(path.read_bytes()) for path in sorted(self.failures.glob('ordinal_*.json'))]

    def test_timeout_cause_survives_loop_and_other_report_finishes_without_replaying_pending(self):
        self.fixture()
        calls = []
        def request(prompt, args, label, **kwargs):
            calls.append(label)
            if len(calls) == 1:
                raise TimeoutError('PRIVATE synthetic provider detail')
            return self.case.model(prompt, args, label, **kwargs)
        with patch.object(producer, 'call_deepseek', side_effect=request), \
                patch.object(producer, 'wechat_title_from_filename', return_value=(fixtures.article_fixture.TITLE, fixtures.valid_decision())), self.case.private():
            with self.assertRaises(articles.ArticleRecoveryError) as caught:
                self.case.recover()
        self.assertEqual(caught.exception.category, 'article_progress_request_pending')
        self.assertIsInstance(caught.exception.__cause__, progress.ProgressError)
        self.assertIsInstance(caught.exception.__cause__.__cause__, TimeoutError)
        record, = self.records()
        self.assertEqual(record['source_ordinal'], 1)
        self.assertEqual(record['typed_exception_chain'], ['ProgressError', 'TimeoutError'])
        self.assertIn('PRIVATE synthetic provider detail', record['private_traceback'])
        metadata = articles.read_json(self.output / articles.PROVENANCE)
        self.assertIsNotNone(articles.usable_article(self.output / metadata['sources'][1]['directory']))
        self.assertEqual(len(calls), 2)
        self.assertFalse((self.output / articles.RECEIPT).exists())
        with patch.object(producer, 'call_deepseek', side_effect=AssertionError('no retry')), self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_progress_pending$'):
                self.case.recover()
        self.assertEqual(len(calls), 2)

    def test_partial_status_is_saved_and_failure_snapshot_matches_current_source_and_state(self):
        self.fixture()
        def generate(directory, source_filename, source_text, args, status, **kwargs):
            status['wechat_title_decision'] = {'needs_model_repair': True, 'repair_attempted': True}
            status['private_failure_marker'] = directory.name
            raise RuntimeError('PRIVATE generator stopped after status update')
        with patch.object(producer, 'generate_wechat_article', side_effect=generate), self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_generation_failed$'):
                self.case.recover()
        metadata = articles.read_json(self.output / articles.PROVENANCE)
        self.assertEqual(len(self.records()), 2)
        for source, record in zip(metadata['sources'], self.records()):
            status_path = self.output / source['directory'] / 'status.json'
            status = articles.read_json(status_path)
            self.assertEqual(status['private_failure_marker'], source['directory'])
            self.assertTrue(status['wechat_title_decision']['needs_model_repair'])
            self.assertEqual(record['article_status_sha256'], articles.digest(status_path.read_bytes()))
            self.assertEqual(record['source_provenance_sha256'], articles.digest(articles.encoded(source['provenance'])))
            self.assertEqual(record['source_markdown_sha256'], source['source_markdown_sha256'])
            self.assertEqual(record['generation_contract_sha256'], articles.generation_contract(self.case.h.args))
            self.assertNotIn(articles.FIELD, status)

    def test_failure_before_current_source_staging_never_writes_previous_report_status(self):
        self.fixture()
        original = articles._stage_source
        calls = []
        def stage(plan, directory):
            calls.append(plan['directory'])
            if len(calls) == 2:
                raise OSError('PRIVATE source staging failure')
            return original(plan, directory)
        with patch.object(articles, '_stage_source', side_effect=stage), \
                patch.object(producer, 'call_deepseek', side_effect=self.case.model), \
                patch.object(producer, 'wechat_title_from_filename', return_value=(fixtures.article_fixture.TITLE, fixtures.valid_decision())), self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_generation_failed$'):
                self.case.recover()
        self.assertFalse((self.output / calls[1] / 'status.json').exists())
        record, = self.records()
        self.assertEqual(record['source_ordinal'], 2)
        self.assertIsNone(record['article_status_sha256'])
        self.assertIsNotNone(articles.usable_article(self.output / calls[0]))

    def test_private_records_are_archived_but_never_in_article_receipt_or_article_handoff(self):
        self.fixture(1)
        workspace = self.output.parent.parent
        (workspace / 'context.json').write_bytes(delivery.encode(self.case.context))
        with patch.object(producer, 'call_deepseek', side_effect=TimeoutError('PRIVATE request')), self.case.private():
            with self.assertRaises(articles.ArticleRecoveryError):
                self.case.recover()
            delivery.save_generation(workspace, self.case.f.client, 'private')
        import tarfile
        payload, _ = self.case.f.client.objects[delivery.context_prefix(self.case.context) + '/generation.tar.gz']
        with tarfile.open(fileobj=io.BytesIO(payload), mode='r:gz') as archive:
            self.assertIn('private-diagnostics/article-failures/ordinal_0001.json', archive.getnames())
        self.assertFalse(list(self.output.rglob('ordinal_*.json')))
        # A completed output is packed independently from the private checkpoint.
        from private_workflow_handoff import create_archive
        archive_path = self.output.parent.parent / 'articles-only.tar.gz'
        create_archive(self.output, archive_path)
        with tarfile.open(archive_path) as archive:
            self.assertFalse(any('article-failures' in name or 'private-diagnostics' in name for name in archive.getnames()))

    def test_normal_cli_only_emits_fixed_category_and_ordinal(self):
        self.fixture(1)
        workspace = self.output.parent.parent
        (workspace / 'context.json').write_bytes(delivery.encode(self.case.context))
        shutil.copytree(self.case.f.workspace / 'source', workspace / 'source')
        argv = ['recover_report_articles.py', '--source-dir', str(workspace / 'source'), '--source-kind', 'ocr-pages',
            '--output-dir', str(self.output), '--expected-reports', '1', '--date-folder', '261007',
            '--source-run-id', fixtures.inspector.SOURCE_RUN_ID, '--source-execution-sha', 'a' * 40,
            '--source-handoff-run-id', fixtures.inspector.HANDOFF_RUN_ID, '--source-handoff-execution-sha', 'b' * 40,
            '--checkpoint-workspace', str(workspace)]
        public = io.StringIO()
        with patch.object(sys, 'argv', argv), patch('private_workflow_handoff.build_r2_client', return_value=self.case.f.client), \
                patch('private_workflow_handoff.r2_bucket', return_value='private'), \
                patch.object(producer, 'call_deepseek', side_effect=TimeoutError('PRIVATE provider content')), \
                redirect_stderr(public), redirect_stdout(io.StringIO()):
            self.assertEqual(articles.main(), 2)
        self.assertEqual(public.getvalue(), 'Report article recovery stopped: article_progress_request_pending source_ordinal=1\n')
        self.assertIn('PRIVATE provider content', self.records()[0]['private_traceback'])

    def test_bounded_private_trace_and_unknown_exception_type_not_reflected_in_typed_field(self):
        self.fixture(1)
        class PrivateProviderClass(Exception):
            pass
        with patch.object(producer, 'generate_wechat_article', side_effect=PrivateProviderClass('x' * (articles.MAX_PRIVATE_FAILURE_BYTES * 2))), self.case.private():
            with self.assertRaises(articles.ArticleRecoveryError):
                self.case.recover()
        record, = self.records()
        self.assertEqual(record['typed_exception_chain'], ['UnknownException'])
        self.assertTrue(record['traceback_truncated'])
        self.assertLessEqual(len(record['private_traceback'].encode()), articles.MAX_PRIVATE_FAILURE_BYTES)

    def test_multibyte_private_trace_tail_stays_within_byte_limit(self):
        self.fixture(1)
        with patch.object(producer, 'generate_wechat_article', side_effect=RuntimeError('私密' * articles.MAX_PRIVATE_FAILURE_BYTES)), self.case.private():
            with self.assertRaises(articles.ArticleRecoveryError):
                self.case.recover()
        record, = self.records()
        self.assertTrue(record['traceback_truncated'])
        self.assertLessEqual(len(record['private_traceback'].encode()), articles.MAX_PRIVATE_FAILURE_BYTES)

    def test_diagnostic_write_failure_stops_later_requests_and_keeps_original_cause(self):
        self.fixture()
        with patch.object(producer, 'call_deepseek', side_effect=TimeoutError('PRIVATE provider')) as call, \
                patch.object(articles, 'private_failure_record', side_effect=OSError('PRIVATE disk')), self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_failure_diagnostics_unavailable$') as caught:
                self.case.recover()
        self.assertEqual(call.call_count, 1)
        self.assertIsInstance(caught.exception.__cause__.__cause__.__cause__, TimeoutError)

    def test_failed_durable_error_save_stops_later_reports_and_preserves_original_cause(self):
        self.fixture()
        original = self.case.persisted
        def persist():
            if self.failures.exists():
                raise OSError('PRIVATE checkpoint store')
            original.append(True)
        with patch.object(producer, 'call_deepseek', side_effect=TimeoutError('PRIVATE provider')) as call, self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_failure_checkpoint_unavailable$') as caught:
                articles.recover_articles(self.case.f.workspace / 'source', 'ocr-pages', self.output, 2, '261007', self.case.h.args,
                    source_run_id=fixtures.inspector.SOURCE_RUN_ID, source_execution_sha='a' * 40,
                    source_handoff_run_id=fixtures.inspector.HANDOFF_RUN_ID, source_handoff_execution_sha='b' * 40,
                    checkpoint_progress=True, persist_progress=persist, delivery_context=self.case.context)
        self.assertEqual(call.call_count, 1)
        self.assertIsInstance(caught.exception.__cause__.__cause__.__cause__, TimeoutError)
        self.assertEqual(len(self.records()), 1)

    def test_false_durable_callback_does_not_allow_further_reports(self):
        self.fixture()
        def persist():
            return not self.failures.exists()
        with patch.object(producer, 'call_deepseek', side_effect=TimeoutError('PRIVATE provider')) as call, self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^article_failure_checkpoint_unavailable$'):
                articles.recover_articles(self.case.f.workspace / 'source', 'ocr-pages', self.output, 2, '261007', self.case.h.args,
                    source_run_id=fixtures.inspector.SOURCE_RUN_ID, source_execution_sha='a' * 40,
                    source_handoff_run_id=fixtures.inspector.HANDOFF_RUN_ID, source_handoff_execution_sha='b' * 40,
                    checkpoint_progress=True, persist_progress=persist, delivery_context=self.case.context)
        self.assertEqual(call.call_count, 1)


if __name__ == '__main__':
    unittest.main()
