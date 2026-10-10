"""Exact 44-report retained-response revalidation; all provider/storage calls synthetic."""
from contextlib import ExitStack, redirect_stdout
import copy
import io
import json
from pathlib import Path
import re
import tarfile
import unittest
from unittest.mock import patch

import article_generation_progress as progress
import pdf_to_xhs_batch as producer
import recover_report_articles as articles
import recovered_article_delivery as delivery
import revalidate_saved_article_titles as revalidation
import test_article_title_resume as fixtures
import test_inspect_recovered_article_generation as inspection_fixtures
import wechat_title_optimizer as titles


class WhitespaceTests(unittest.TestCase):
    def test_both_cleaners_keep_ascii_boundaries_and_compact_chinese_punctuation(self):
        for clean in (titles.clean_wechat_title, titles.clean_filename_wechat_title):
            for name in ('Apple Watch', 'AMD Instinct', 'GPT 5', '3 D'):
                with self.subTest(clean=clean.__name__, name=name):
                    candidate = clean('国际清算银行 ： ' + name + ' 产品 交付 数量 与 需求 结构 变化', '国际清算银行')
                    self.assertIn(name, candidate)
                    self.assertIn('产品交付数量', candidate)
                    self.assertNotIn('long_untranslated_english', titles.title_quality_issues(candidate))
        self.assertEqual(titles.compact_title_whitespace('甲 \t A\t  B\n2\u00a03  ， 乙'), '甲A B 2 3，乙')

    def test_existing_long_word_ratio_acronym_and_quality_gates_remain(self):
        source = 'BIS-GPU Supply Changes-261007.pdf'
        for clean in (titles.clean_wechat_title, titles.clean_filename_wechat_title):
            self.assertIn('long_untranslated_english', titles.title_quality_issues(
                clean('国际清算银行：Salesforce产品交付数量变化', '国际清算银行')))
        self.assertEqual(titles.missing_required_filename_terms('国际清算银行：产品交付数量变化', titles.required_filename_terms(source)), ['GPU'])
        self.assertEqual(progress.MAX_TITLES, 4)

    def test_valid_filename_fallback_cannot_substitute_for_missing_or_invalid_saved_candidates(self):
        status = {'original_filename': 'BIS-苹果产品交付数量与需求变化-261007.pdf', 'institution_name': '国际清算银行'}
        body = '苹果产品交付数量与需求变化，企业产出和交付保持稳定。'
        for batch in ([], [''], ['AI'], ['国际清算银行：Salesforce产品交付数量变化']):
            with self.subTest(candidate_count=len(batch)):
                selected, _ = revalidation.select_title(status, body, [batch])
                self.assertIsNone(selected)


class RevalidationTests(unittest.TestCase):
    TITLE = '国际清算银行：Apple Watch GPU产品交付数量变化'

    def setUp(self):
        self.case = fixtures.ResumeTests()
        self.addCleanup(self.case.doCleanups)
        seed = fixtures.pages_fixture.OCRPagesTests.seed
        def named_source(fixture, count):
            seed(fixture, count)
            rows = json.loads(fixture.manifest.read_bytes())
            item = rows[37]
            name = 'BIS-Apple Watch GPU Product Shipments-261007.pdf'
            (fixture.input / item['name']).rename(fixture.input / name)
            item.update(name=name, process_local_path='/original/' + name, dropbox_path='/zip_backup/261007/' + name)
            fixture.manifest.write_text(json.dumps(rows))
            fixture.request['manifest_sha256'] = articles.digest(fixture.manifest.read_bytes())
            fixture.publish_cache()
        with patch.object(fixtures.pages_fixture.OCRPagesTests, 'seed', named_source), redirect_stdout(io.StringIO()):
            self.case.fixture(44)
        self.workspace = self.case.output.parent.parent
        self.checkpoint = self.case.output.parent
        (self.workspace / 'context.json').write_bytes(delivery.encode(self.case.context))
        self.counter = 0
        def model(prompt, args, label, **kwargs):
            if label == 'WeChat article':
                self.counter += 1
                return fixtures.article_fixture.BODY
            return json.dumps({'titles': [self.TITLE] if self.counter == 38 else [fixtures.article_fixture.TITLE]})
        # Recreate the old defect through its single whitespace operation while
        # generating real source, progress, response and editorial-binding files.
        with patch.object(titles, 'compact_title_whitespace', side_effect=lambda value: re.sub(r'\s+', '', value)), \
                patch.object(producer, 'call_deepseek', side_effect=model), self.case.private():
            with self.assertRaisesRegex(articles.ArticleRecoveryError, '^generated_article_unbound$'):
                self.case.recover()
        self.assertEqual(self.counter, 44)
        self.metadata = articles.read_json(self.case.output / articles.PROVENANCE)
        self.directory = self.case.output / self.metadata['sources'][37]['directory']
        self.progress_path = self.checkpoint / 'generation-progress' / self.directory.name / progress.RECEIPT
        self.assertEqual(len(json.loads(self.progress_path.read_bytes())['requests']), 5)
        (self.workspace / 'private-generation.log').write_text(
            'Report article recovery stopped: generated_article_unbound source_ordinal=38\n')
        self.stack = ExitStack()
        self.addCleanup(self.stack.close)
        self.stack.enter_context(patch.object(revalidation.inspection, 'MANIFEST_SHA256', self.case.context['manifest_sha256']))
        self.stack.enter_context(patch.object(revalidation.inspection, 'KEY', delivery.context_prefix(self.case.context) + '/generation.tar.gz'))
        self.stack.enter_context(patch.object(revalidation, 'CONTEXT_SHA', articles.digest(delivery.encode(self.case.context))))
        self.stack.enter_context(patch.object(revalidation, 'OLD_CONTRACT', articles.generation_contract(self.case.h.args)))
        self.stack.enter_context(patch.object(revalidation, 'FILE_PINS', {name: (len((self.directory / name).read_bytes()),
            articles.digest((self.directory / name).read_bytes())) for name in revalidation.FILE_PINS}))
        self.pin_progress()
        self.publish_snapshot()
        self.original, self.handoff, self.source_jobs = inspection_fixtures.evidence()
        self.recovery = {**self.handoff, 'id': int(revalidation.GENERATION_RUN_ID),
            'path': '.github/workflows/recover-report-article-delivery.yml', 'head_sha': 'c' * 40, 'run_attempt': 1}
        job = copy.deepcopy(self.source_jobs['jobs'][1])
        job.update(id=revalidation.GENERATION_JOB_ID, run_id=self.recovery['id'], head_sha='c' * 40, name='generate')
        self.recovery_jobs = {'jobs': [job]}
        self.no_model = self.stack.enter_context(patch.object(producer, 'call_deepseek', side_effect=AssertionError('no provider request')))
        self.stack.enter_context(patch('requests.Session.request', side_effect=AssertionError('no external requests')))

    def pin_progress(self):
        self.stack.enter_context(patch.object(revalidation, 'PROGRESS_SHA', articles.digest(self.progress_path.read_bytes())))

    def publish_snapshot(self):
        with redirect_stdout(io.StringIO()):
            delivery.save_generation(self.workspace, self.case.f.client, 'private')
        head = self.case.f.client.head_object(Bucket='private', Key=revalidation.inspection.KEY)
        self.stack.enter_context(patch.object(revalidation, 'ARCHIVE_SHA', head['Metadata']['sha256']))
        self.stack.enter_context(patch.object(revalidation, 'ARCHIVE_BYTES', head['ContentLength']))
        self.case.f.client.uploads.clear()
        self.objects_before = copy.deepcopy(self.case.f.client.objects)

    def execute(self, mode='inspect'):
        destination = self.case.f.root / ('revalidation-' + mode)
        destination.mkdir(exist_ok=True)
        with redirect_stdout(io.StringIO()):
            return revalidation.execute(self.case.f.client, 'private', self.original, self.handoff,
                self.source_jobs, self.recovery, self.recovery_jobs, 'owner/repo', destination, mode)

    def test_inspect_real44_uses_four_saved_responses_zero_posts_writes_and_keeps_every_other_byte(self):
        before = revalidation.snapshot(self.checkpoint)
        result = self.execute()
        self.assertTrue(result['revalidation_ready'])
        self.assertFalse(result['applied'])
        self.assertEqual(result['completed_article_count_after'], 44)
        self.assertEqual(result['unchanged_article_count'], 43)
        self.assertEqual(result['retained_title_response_count'], 4)
        self.assertEqual((result['provider_posts'], result['object_writes']), (0, 0))
        self.assertEqual(self.case.f.client.objects, self.objects_before)
        self.assertEqual(revalidation.snapshot(self.checkpoint), before)
        candidate = self.case.f.root / 'revalidation-inspect/candidate/checkpoint'
        changed = candidate / 'articles' / self.directory.name
        self.assertIn('Apple Watch', articles.usable_article(changed).title)
        self.assertEqual(revalidation.replace_h1((changed / 'wechat_article.md').read_bytes()),
                         revalidation.replace_h1((self.directory / 'wechat_article.md').read_bytes()))
        after = revalidation.snapshot(candidate)
        mutable = {f'articles/{self.directory.name}/status.json', f'articles/{self.directory.name}/wechat_article.md'}
        for name, value in before.items():
            if name not in mutable:
                self.assertEqual(after[name], value, name)
        self.no_model.assert_not_called()
        serialized = json.dumps(result, ensure_ascii=False)
        for private in ('Apple', 'Watch', '国际清算银行', 'PRIVATE'):
            self.assertNotIn(private, serialized)

    def test_apply_full44_handoff_excludes_private_proof_and_all_progress_bytes_are_identical(self):
        result = self.execute('apply')
        self.assertTrue(result['applied'])
        self.assertEqual((result['object_writes'], result['object_write_attempts']), (2, 2))
        key = revalidation.inspection.KEY
        generation, _ = self.case.f.client.objects[key]
        handoff, _ = self.case.f.client.objects[key.removesuffix('/generation.tar.gz') + '/articles/shard_0.tar.gz']
        with tarfile.open(fileobj=io.BytesIO(generation), mode='r:gz') as archive:
            self.assertIn('private-diagnostics/title-revalidation/ordinal_0038.json', archive.getnames())
            self.assertEqual(archive.extractfile('generation-progress/' + self.directory.name + '/' + progress.RECEIPT).read(),
                             self.progress_path.read_bytes())
            proof = json.load(archive.extractfile('private-diagnostics/title-revalidation/ordinal_0038.json'))
            self.assertEqual(proof['old_generation_contract_sha256'], revalidation.OLD_CONTRACT)
            self.assertEqual(len(proof['requests']), 5)
        with tarfile.open(fileobj=io.BytesIO(handoff), mode='r:gz') as archive:
            names = archive.getnames()
            self.assertFalse(any('private-diagnostics' in name or 'generation-progress' in name or 'title-revalidation' in name for name in names))
            receipt = json.load(archive.extractfile(articles.RECEIPT))
            self.assertEqual(receipt['report_count'], 44)
        self.no_model.assert_not_called()
        with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_archive_changed$'):
            self.execute('apply')
        self.assertEqual(len(self.case.f.client.uploads), 2)

    def test_old_decision_candidates_are_not_used_as_saved_model_responses(self):
        status = articles.read_json(self.directory / 'status.json')
        status['wechat_title_decision']['raw_candidates'] = ['PRIVATE FORGED OLD CANDIDATE']
        status['wechat_title_decision']['selected_title'] = 'PRIVATE emergency fallback'
        articles.write_json(self.directory / 'status.json', status)
        self.publish_snapshot()
        self.assertTrue(self.execute()['revalidation_ready'])
        candidate = self.case.f.root / 'revalidation-inspect/candidate/checkpoint/articles' / self.directory.name
        decision = articles.read_json(candidate / 'status.json')['wechat_title_decision']
        self.assertNotIn('PRIVATE FORGED OLD CANDIDATE', decision['raw_candidates'])
        self.assertTrue(all(candidate == self.TITLE for candidate in decision['raw_candidates']))

    def test_pending_title_is_rejected_before_candidate_extraction_and_without_writes(self):
        state = json.loads(self.progress_path.read_bytes())
        state['requests'][-1].update(state='pending', response_sha256=None, response_bytes=None)
        self.progress_path.write_bytes(progress.encoded(state))
        self.pin_progress()
        self.publish_snapshot()
        with patch.object(titles, 'extract_title_candidates', side_effect=AssertionError('pending response forbidden')) as parse:
            with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_progress_pending$'):
                self.execute('apply')
        parse.assert_not_called()
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_pending_progress_on_another_bound_report_also_blocks_the_whole_cohort(self):
        other = self.checkpoint / 'generation-progress' / self.metadata['sources'][0]['directory'] / progress.RECEIPT
        state = json.loads(other.read_bytes())
        state['requests'][-1].update(state='pending', response_sha256=None, response_bytes=None)
        other.write_bytes(progress.encoded(state))
        self.publish_snapshot()
        with patch.object(titles, 'extract_title_candidates', side_effect=AssertionError('any pending blocks reuse')) as parse:
            with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_progress_pending$'):
                self.execute('apply')
        parse.assert_not_called()
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_changed_response_and_identity_fail_without_any_request_or_write(self):
        state = json.loads(self.progress_path.read_bytes())
        response = self.progress_path.parent / state['requests'][2]['response_path']
        response.write_text('tampered')
        self.publish_snapshot()
        with self.assertRaises(ValueError):
            self.execute('apply')
        self.assertEqual(self.case.f.client.objects, self.objects_before)
        self.no_model.assert_not_called()

    def test_changed_contract_is_not_adopted_or_rewritten(self):
        state = json.loads(self.progress_path.read_bytes())
        state['identity']['generation_contract_sha256'] = '0' * 64
        self.progress_path.write_bytes(progress.encoded(state))
        self.pin_progress()
        self.publish_snapshot()
        before = self.progress_path.read_bytes()
        with self.assertRaisesRegex(progress.ProgressError, '^article_progress_identity_mismatch$'):
            self.execute('apply')
        self.assertEqual(self.progress_path.read_bytes(), before)
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_source_prompt_body_pins_and_other43_binding_are_required(self):
        (self.directory / 'prompt_for_wechat.md').write_text('PRIVATE changed prompt')
        self.publish_snapshot()
        with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_file_mismatch$'):
            self.execute('apply')
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_other_bound_article_changes_stop_revalidation(self):
        other = self.case.output / self.metadata['sources'][0]['directory'] / 'wechat_article.md'
        other.write_text(other.read_text() + '\nPRIVATE tampered content\n')
        self.publish_snapshot()
        with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_incident_invalid$'):
            self.execute('apply')
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_unready_saved_candidates_do_not_enable_new_request_or_object_write(self):
        with patch.object(titles, 'extract_title_candidates', return_value=['国际清算银行：Salesforce产品交付数量变化']):
            result = self.execute()
            self.assertFalse(result['revalidation_ready'])
            with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_title_unready$'):
                self.execute('apply')
        self.assertEqual(self.case.f.client.objects, self.objects_before)
        self.no_model.assert_not_called()

    def test_neutralization_quality_fallback_cannot_authorize_model_evidence(self):
        with patch.object(titles, 'ensure_publishable_neutral_title', return_value=('国际清算银行：公司产品交付数量变化', ['quality_evidence_fallback'])):
            with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_title_guard_failed$'):
                self.execute('apply')
        self.assertEqual(self.case.f.client.objects, self.objects_before)

    def test_metadata_gates_precede_archive_read_and_changed_head_precedes_writes(self):
        self.recovery_jobs['jobs'][0]['steps'][-1]['conclusion'] = 'failure'
        with patch.object(self.case.f.client, 'head_object') as head:
            with self.assertRaises(ValueError):
                self.execute()
        head.assert_not_called()
        self.recovery_jobs['jobs'][0]['steps'][-1]['conclusion'] = 'success'
        with patch.object(revalidation, 'ARCHIVE_SHA', '0' * 64):
            with self.assertRaisesRegex(revalidation.RevalidationError, '^revalidation_archive_changed$'):
                self.execute()
        self.assertFalse(self.case.f.client.uploads)

    def test_write_failure_reports_unknown_write_count_without_replay(self):
        original = self.case.f.client.upload_file
        def failed_after_write(*args, **kwargs):
            original(*args, **kwargs)
            raise OSError('PRIVATE response lost after upload')
        with patch.object(self.case.f.client, 'upload_file', side_effect=failed_after_write):
            result = self.execute('apply')
        self.assertFalse(result['success'])
        self.assertIsNone(result['object_writes'])
        self.assertEqual(result['object_write_attempts'], 1)
        self.assertNotIn('PRIVATE', json.dumps(result))
        self.no_model.assert_not_called()

    def test_second_write_failure_can_resume_existing_complete_receipt_without_provider(self):
        original = self.case.f.client.upload_file
        def fail_handoff(filename, bucket, key, **kwargs):
            if key.endswith('/articles/shard_0.tar.gz'):
                raise OSError('PRIVATE handoff storage failure')
            return original(filename, bucket, key, **kwargs)
        with patch.object(self.case.f.client, 'upload_file', side_effect=fail_handoff):
            result = self.execute('apply')
        self.assertFalse(result['success'])
        self.assertEqual(result['object_write_attempts'], 2)
        self.assertIsNone(result['object_writes'])
        restored = self.case.f.root / 'standalone-resume'
        restored.mkdir()
        from private_workflow_handoff import download_directory
        with redirect_stdout(io.StringIO()):
            head = self.case.f.client.head_object(Bucket='private', Key=revalidation.inspection.KEY)
            download_directory(revalidation.inspection.KEY, restored / 'checkpoint',
                client=revalidation.ReadOnlyClient(self.case.f.client, head), bucket='private')
        (restored / 'context.json').write_bytes((restored / 'checkpoint/context.json').read_bytes())
        with patch.object(articles, 'generation_contract', return_value='d' * 64), \
                patch.object(progress.Progress, '__init__', side_effect=AssertionError('complete receipts never reopen progress')):
            receipt = articles.recover_articles(self.case.f.workspace / 'source', 'ocr-pages', restored / 'checkpoint/articles',
                44, '261007', self.case.h.args, source_run_id=fixtures.inspector.SOURCE_RUN_ID,
                source_execution_sha='a' * 40, source_handoff_run_id=fixtures.inspector.HANDOFF_RUN_ID,
                source_handoff_execution_sha='b' * 40, checkpoint_progress=True,
                persist_progress=lambda: delivery.save_generation(restored, self.case.f.client, 'private'),
                delivery_context=self.case.context)
        self.assertEqual(receipt['report_count'], 44)
        with redirect_stdout(io.StringIO()):
            complete = delivery.save_generation(restored, self.case.f.client, 'private', complete=True)
        self.assertEqual(complete['article_count'], 44)
        key = revalidation.inspection.KEY.removesuffix('/generation.tar.gz') + '/articles/shard_0.tar.gz'
        self.assertIn(key, self.case.f.client.objects)
        self.no_model.assert_not_called()


class RuntimeTests(unittest.TestCase):
    def test_main_identity_and_workflow_have_no_provider_secrets_or_nested_delivery(self):
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
            'GITHUB_REPOSITORY': 'owner/repo', 'GITHUB_WORKFLOW_REF': 'owner/repo/' + revalidation.WORKFLOW + '@refs/heads/main'}
        self.assertEqual(revalidation.runtime_identity(env), 'owner/repo')
        for name, value in (('GITHUB_REF', 'refs/pull/1/merge'), ('GITHUB_EVENT_NAME', 'push'), ('GITHUB_WORKFLOW_REF', 'other')):
            with self.assertRaises(revalidation.RevalidationError):
                revalidation.runtime_identity({**env, name: value})
        workflow = (Path(__file__).resolve().parents[1] / revalidation.WORKFLOW).read_text()
        self.assertIn('recovered-report-articles-37695511597-261007', workflow)
        self.assertNotIn('DEEPSEEK', workflow)
        self.assertNotIn('MINERU', workflow)
        self.assertNotIn('recover-report-article-delivery.yml', workflow)
        self.assertEqual(progress.MAX_TITLES, 4)


if __name__ == '__main__':
    unittest.main()
