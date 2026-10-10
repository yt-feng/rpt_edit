#!/usr/bin/env python3
"""Real uploader + private handoff regression coverage; all services are local fakes."""
import copy
from contextlib import redirect_stdout
import io
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import Mock, patch

import recovered_article_delivery as delivery


class StorageError(RuntimeError):
    def __init__(self, code):
        self.response = {'Error': {'Code': code}}


class Store:
    def __init__(self):
        self.objects = {}
        self.metadata = {}

    def put_object(self, *, Bucket, Key, Body, IfNoneMatch=None, **kwargs):
        if IfNoneMatch == '*' and Key in self.objects:
            raise StorageError('PreconditionFailed')
        self.objects[Key] = bytes(Body)

    def get_object(self, *, Bucket, Key):
        if Key not in self.objects:
            raise StorageError('NoSuchKey')
        return {'Body': io.BytesIO(self.objects[Key])}

    def delete_object(self, *, Bucket, Key):
        self.objects.pop(Key, None)

    def upload_file(self, path, bucket, key, ExtraArgs):
        self.objects[key] = Path(path).read_bytes()
        self.metadata[key] = ExtraArgs['Metadata']

    def download_file(self, bucket, key, path):
        Path(path).write_bytes(self.objects[key])

    def head_object(self, *, Bucket, Key):
        if Key not in self.objects:
            raise StorageError('NoSuchKey')
        return {'ContentLength': len(self.objects[Key]), 'Metadata': self.metadata.get(Key, {})}


def config():
    return delivery.inputs({'SOURCE_RUN_ID': '37854139119', 'SOURCE_HANDOFF_RUN_ID': '37946512807',
        'SOURCE_KIND': 'mineru-recovery', 'DATE_FOLDER': '261008', 'EXPECTED_ARTICLES': '2'})


def original_fixture(attempts=1):
    run = {'id': 37854139119, 'path': delivery.DAILY, 'event': 'schedule', 'head_branch': 'main',
           'repository': {'full_name': 'owner/repo'}, 'head_repository': {'full_name': 'owner/repo'},
           'head_sha': 'a' * 40, 'status': 'completed', 'conclusion': 'failure', 'run_attempt': attempts}
    page = {'total_count': 3, 'jobs': [dict(id=index, name=name, run_id=run['id'], head_sha=run['head_sha'],
        status='completed', conclusion='success' if name == 'select-macro-reports' else 'skipped')
        for index, name in enumerate(('select-macro-reports', 'push-xhs-notes-wechat-drafts',
                                     'push-portal-translated-wechat-drafts'), 1)]}
    return run, [copy.deepcopy(page) for _ in range(attempts)]


def context():
    return {'schema_version': 1, 'source_run_id': '37854139119', 'source_handoff_run_id': '37946512807',
            'source_kind': 'mineru-recovery', 'date_folder': '261008', 'expected_articles': 2,
            'source_execution_sha': 'a' * 40, 'handoff_execution_sha': 'b' * 40,
            'source_receipt_sha256': 'c' * 64, 'manifest_sha256': 'd' * 64}


class SourceAuthenticationTests(unittest.TestCase):
    def test_historical_original_and_distinct_handoff_identity(self):
        run, pages = original_fixture()
        self.assertEqual(delivery.validate_original(run, pages, config(), 'owner/repo', '999'), 'a' * 40)
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            (root / 'selected_to_process_manifest.json').write_bytes(b'[]')
            import recover_durable_mineru_sources as recovery
            (root / recovery.RECEIPT).write_bytes(b'{}')
            receipt = {'source_run_id': config()['SOURCE_RUN_ID'], 'source_execution_sha': 'a' * 40}
            with patch.object(recovery, 'validate_sources', return_value=receipt) as validate:
                actual = delivery.validate_source(root, config(), 'a' * 40, 'b' * 40)
            self.assertEqual(actual['source_run_id'], '37854139119')
            self.assertEqual(actual['source_handoff_run_id'], '37946512807')
            self.assertEqual(validate.call_args.kwargs,
                {'expected_recovery_run_id': '37946512807', 'expected_execution_sha': 'b' * 40})

    def test_current_daily_does_not_wait_for_future_translated_upload(self):
        run, pages = original_fixture()
        run['status'] = 'in_progress'
        pages[0]['jobs'][-1].update(status='queued', conclusion=None)
        delivery.validate_original(run, pages, config(), 'owner/repo', str(run['id']))
        with self.assertRaises(delivery.DeliveryError):
            delivery.validate_original(run, pages, config(), 'owner/repo', '999')
        pages[0]['jobs'][-1].update(status='in_progress')
        with self.assertRaisesRegex(delivery.DeliveryError, 'already_started'):
            delivery.validate_original(run, pages, config(), 'owner/repo', str(run['id']))

    def test_no_prior_attempt_upload_can_be_hidden_by_latest_skip(self):
        run, pages = original_fixture(2)
        for index in (1, 2):
            for outcome in ('success', 'failure', 'cancelled', None):
                changed = copy.deepcopy(pages)
                changed[0]['jobs'][index]['conclusion'] = outcome
                with self.subTest(index=index, outcome=outcome), self.assertRaises(delivery.DeliveryError):
                    delivery.validate_original(run, changed, config(), 'owner/repo', '999')
        with self.assertRaises(delivery.DeliveryError):
            delivery.validate_original(run, pages[1:], config(), 'owner/repo', '999')

    def test_invalid_repository_or_source_does_not_call_services(self):
        run, pages = original_fixture()
        for field, value in (('head_branch', 'other'), ('path', delivery.MANUAL), ('head_sha', 'x'),
                             ('repository', {'full_name': 'other/repo'})):
            with self.subTest(field=field), self.assertRaises(delivery.DeliveryError):
                delivery.validate_original(dict(run, **{field: value}), pages, config(), 'owner/repo', '999')
        with patch('requests.get') as command:
            with self.assertRaises(delivery.DeliveryError):
                delivery.api('owner/repo/escape', '1')
            command.assert_not_called()

    def test_same_manifest_cannot_be_delivered_by_two_original_runs(self):
        store, value = Store(), context()
        delivery.claim_original(value, store, 'private')
        delivery.claim_original(value, store, 'private')
        with self.assertRaisesRegex(delivery.DeliveryError, 'other_original_run'):
            delivery.claim_original(dict(value, source_run_id='37232504334'), store, 'private')

    def test_only_absence_can_skip_checkpoint_restore(self):
        store = Store()
        self.assertFalse(delivery.optional_download('x', Path('/unused'), store, 'private'))
        with patch.object(store, 'head_object', side_effect=StorageError('AccessDenied')):
            with self.assertRaisesRegex(delivery.DeliveryError, 'checkpoint_unavailable'):
                delivery.optional_download('x', Path('/unused'), store, 'private')


class MetadataResponse:
    def __init__(self, body=b'{"id":123}', *, status=200, headers=None, chunks=None):
        self.status_code = status
        self.headers = headers or {}
        self.chunks = [body] if chunks is None else chunks
        self.closed = False
        self.read = False

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.closed = True

    def iter_content(self, *, chunk_size):
        assert chunk_size == 64 * 1024
        self.read = True
        for chunk in self.chunks:
            if isinstance(chunk, Exception):
                raise chunk
            yield chunk


class MetadataApiTests(unittest.TestCase):
    def test_authenticated_fixed_host_requests_work_without_any_cli(self):
        for suffix in ('123', '123/jobs?per_page=100&page=10&filter=latest',
                       '123/attempts/10/jobs?per_page=100&page=1'):
            response = MetadataResponse()
            with self.subTest(suffix=suffix), patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), \
                 patch('requests.get', return_value=response) as get, \
                 patch('subprocess.run', side_effect=FileNotFoundError('gh')) as command:
                self.assertEqual(delivery.api('owner/repo', suffix), {'id': 123})
                command.assert_not_called()
                get.assert_called_once_with('https://api.github.com/repos/owner/repo/actions/runs/' + suffix,
                    headers={'Authorization': 'Bearer PRIVATE_TOKEN', 'Accept': 'application/vnd.github+json',
                             'X-GitHub-Api-Version': '2022-11-28'},
                    timeout=45, allow_redirects=False, stream=True)
                self.assertTrue(response.closed)

    def test_invalid_coordinates_and_absent_auth_never_send_a_request(self):
        with patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), patch('requests.get') as get:
            for repository in ('../repo', 'owner/..', 'owner/repo/escape', 'owner/repo?token=secret',
                               'owner@host/repo', 'https://example.com/owner/repo'):
                with self.subTest(repository=repository), self.assertRaisesRegex(delivery.DeliveryError, '^invalid_delivery_repository$'):
                    delivery.api(repository, '123')
            for suffix in ('../secrets', '123/../../secrets', '123?token=secret', '123#fragment',
                           '123/jobs?per_page=100&page=11&filter=latest',
                           '123/attempts/0/jobs?per_page=100&page=1', 'https://example.com/'):
                with self.subTest(suffix=suffix), self.assertRaisesRegex(delivery.DeliveryError, '^invalid_delivery_metadata_path$'):
                    delivery.api('owner/repo', suffix)
            for token in ('', ' PRIVATE_TOKEN', 'PRIVATE_TOKEN\n', 'PRIVATE\rTOKEN'):
                with patch.dict(delivery.os.environ, {'GH_TOKEN': token}), \
                     self.assertRaisesRegex(delivery.DeliveryError, '^delivery_github_token_missing_or_invalid$'):
                    delivery.api('owner/repo', '123')
            get.assert_not_called()

    def test_non_success_and_redirects_are_closed_without_reading_private_bodies(self):
        for status in (301, 302, 307, 401, 403, 404, 500):
            response = MetadataResponse(b'PRIVATE_BODY PRIVATE_TOKEN', status=status,
                                        headers={'Location': 'https://untrusted.example/'})
            with self.subTest(status=status), patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), \
                 patch('requests.get', return_value=response), \
                 self.assertRaisesRegex(delivery.DeliveryError, '^delivery_github_metadata_failed$'):
                delivery.api('owner/repo', '123')
            self.assertTrue(response.closed)
            self.assertFalse(response.read)

    def test_metadata_has_both_declared_and_streamed_size_limits(self):
        limit = 16 * 1024 * 1024
        for response in (MetadataResponse(headers={'Content-Length': str(limit + 1)}),
                         MetadataResponse(headers={'Content-Length': '10'},
                                          chunks=[b' ' * (64 * 1024)] * 256 + [b'x'])):
            with patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), \
                 patch('requests.get', return_value=response), \
                 self.assertRaisesRegex(delivery.DeliveryError, '^delivery_github_metadata_oversized$'):
                delivery.api('owner/repo', '123')
            self.assertTrue(response.closed)
        self.assertTrue(response.read)

    def test_invalid_json_or_headers_never_expose_server_text(self):
        for response in (MetadataResponse(b'PRIVATE_BODY PRIVATE_TOKEN'), MetadataResponse(b'[]'),
                         MetadataResponse(b'\xff'), MetadataResponse(headers={'Content-Length': 'PRIVATE_BODY'})):
            with patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), \
                 patch('requests.get', return_value=response), \
                 self.assertRaisesRegex(delivery.DeliveryError, '^delivery_github_metadata_invalid$'):
                delivery.api('owner/repo', '123')
            self.assertTrue(response.closed)

    def test_transport_and_stream_errors_have_only_fixed_public_categories(self):
        import requests
        import traceback
        for at_request in (True, False):
            error = requests.Timeout('PRIVATE_TOKEN PRIVATE_BODY')
            response = MetadataResponse(chunks=[b'{', error])
            kwargs = {'side_effect': error} if at_request else {'return_value': response}
            with patch.dict(delivery.os.environ, {'GH_TOKEN': 'PRIVATE_TOKEN'}), patch('requests.get', **kwargs):
                try:
                    delivery.api('owner/repo', '123')
                except delivery.DeliveryError as caught:
                    self.assertEqual(str(caught), 'delivery_github_metadata_failed')
                    rendered = ''.join(traceback.format_exception(caught))
                    self.assertNotIn('PRIVATE_TOKEN', rendered)
                    self.assertNotIn('PRIVATE_BODY', rendered)
                else:
                    self.fail('Transport failure was accepted')
            if not at_request:
                self.assertTrue(response.closed)


class IntentTests(unittest.TestCase):
    def setUp(self):
        import push_portal_translated_to_wechat_drafts as api_module
        self.api = api_module
        self.store = Store()
        self.articles = [{'title': 'Fixture', 'author': 'KC', 'content': '<p>Fixture body</p>'}]

    def add(self, articles=None):
        return delivery.guarded_add_draft(self.store, 'private', 'scope', None, 'TEST_TOKEN',
                                         articles or self.articles, 10)

    def test_accepted_intent_reuses_id_after_ack_before_checkpoint_interruption(self):
        with patch.object(self.api, 'post_wechat_json', return_value=object()) as post, \
             patch.object(self.api, 'parse_wechat_json', return_value={'media_id': 'ACK'}):
            self.assertEqual(self.add(), 'ACK')
            self.assertEqual(self.add(), 'ACK')
            post.assert_called_once()
            self.assertEqual(post.call_args.kwargs, {'max_attempts': 1})

    def test_lost_ack_never_performs_second_post(self):
        with patch.object(self.api, 'post_wechat_json', side_effect=self.api.WeChatError('request failed')) as post, \
             patch.object(self.api, 'recover_draft_after_ambiguous_add', return_value=''):
            for _ in range(2):
                with self.assertRaisesRegex(delivery.DeliveryError, 'intent_unresolved'):
                    self.add()
            post.assert_called_once()
        with patch.object(self.api, 'post_wechat_json') as post, \
             patch.object(self.api, 'recover_draft_after_ambiguous_add', return_value='FOUND'):
            self.assertEqual(self.add(), 'FOUND')
            post.assert_not_called()

    def test_definitive_crop_and_size_errors_release_only_rejected_intent(self):
        for code in (53401, 53402, 45008):
            self.store = Store()
            with self.subTest(code=code), patch.object(self.api, 'post_wechat_json', return_value=object()), \
                 patch.object(self.api, 'parse_wechat_json', side_effect=[
                     self.api.WeChatError('known rejection', errcode=code), {'media_id': 'REPAIRED'}]):
                with self.assertRaises(self.api.WeChatError):
                    self.add()
                self.assertEqual(self.store.objects, {})
                self.assertEqual(self.add(), 'REPAIRED')

    def test_unclassified_structured_error_is_not_automatically_released(self):
        with patch.object(self.api, 'post_wechat_json', return_value=object()), \
             patch.object(self.api, 'parse_wechat_json', side_effect=self.api.WeChatError('unknown', errcode=99999)):
            with self.assertRaises(self.api.WeChatError):
                self.add()
        self.assertEqual(len(self.store.objects), 1)

    def test_public_and_materialized_payload_group_identity_is_identical(self):
        public = [{'title': 'Fixture', 'author': 'KC', 'content':
                   '<p>Body</p><a href="https://portal.example.invalid/blog/">Archive</a>'}]
        materialized = self.api.materialize_private_article_payload(public, 'https://private.example.invalid')
        self.assertEqual(self.api.draft_group_key(public), self.api.draft_group_key(materialized))

    def test_real_uploader_cover_fallback_uses_guarded_retry(self):
        from test_wechat_api_verification import WeChatUploaderRecoveryTests
        import push_xhs_notes_to_wechat_drafts as uploader
        harness = WeChatUploaderRecoveryTests()
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
             patch.object(self.api, 'post_wechat_json', return_value=object()) as post, \
             patch.object(self.api, 'parse_wechat_json', side_effect=[
                 self.api.WeChatError('crop rejected', errcode=53401), {'media_id': 'SAFE'}]), \
             patch.object(uploader, 'replacement_cover_media_id', return_value='SAFE_THUMB'):
            harness.run_uploader(uploader, Path(temporary), verification=Mock(return_value={'ok': True}),
                add=lambda session, token, articles, timeout: delivery.guarded_add_draft(
                    self.store, 'private', 'scope', session, token, articles, timeout),
                lookup=Mock(return_value=''), publish=Mock(return_value='PUBLISHED'))
            self.assertEqual(post.call_count, 2)

    def test_real_uploader_split_keeps_first_child_and_resumes_second(self):
        from test_wechat_api_verification import WeChatUploaderRecoveryTests
        import push_xhs_notes_to_wechat_drafts as uploader
        harness = WeChatUploaderRecoveryTests()
        wrapped = lambda session, token, articles, timeout: delivery.guarded_add_draft(
            self.store, 'private', 'scope', session, token, articles, timeout)
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), \
             patch.object(self.api, 'post_wechat_json', return_value=object()) as post, \
             patch.object(self.api, 'parse_wechat_json', side_effect=[
                 self.api.WeChatError('article size out of limit', errcode=45008),
                 {'media_id': 'CHILD1'}, {'media_id': 'CHILD2'}]):
            root = Path(temporary)
            with self.assertRaises(self.api.WeChatError):
                harness.run_uploader(uploader, root, verification=Mock(return_value={'ok': False}), add=wrapped,
                    lookup=Mock(return_value=''), publish=Mock(), article_count=2)
            self.assertEqual(post.call_count, 2)
            harness.run_uploader(uploader, root, verification=Mock(return_value={'ok': True}), add=wrapped,
                lookup=Mock(return_value=''), publish=Mock(return_value='PUBLISHED'), article_count=2)
            self.assertEqual(post.call_count, 3)
            self.assertEqual(len(post.call_args.args[2]['articles']), 1)


class DeliveryWorkflowTests(unittest.TestCase):
    def test_website_publish_wait_runs_on_hosted_runner_after_successful_delivery(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/recover-report-article-delivery.yml'
        workflow = path.read_text()
        deliver, publish = workflow.split('\n  deliver:\n', 1)[1].split('\n  publish:\n', 1)
        self.assertIn('runs-on: [self-hosted, wechat-draft]', deliver)
        self.assertNotRegex(deliver, r'\bgh\s+(?:api|workflow|run)\b')
        self.assertIn('validate-delivery --workspace', deliver)
        self.assertIn('bash scripts/commit_output_dir.sh portal_suite/data/blog_archive', deliver)
        self.assertIn('needs: [deliver]', publish)
        self.assertIn("if: ${{ inputs.upload_wechat && needs.deliver.result == 'success' }}", publish)
        self.assertIn('runs-on: ubuntu-latest', publish)
        self.assertNotIn('always()', publish.split('    steps:', 1)[0])
        self.assertIn('GH_TOKEN: ${{ github.token }}', publish)
        self.assertIn('watch_recovered_article_publication.py watch', publish)
        self.assertIn('timeout-minutes: 360', publish)
        self.assertIn('Locate a previous publication attempt without redispatching', publish)
        self.assertIn('artifact-ids: ${{ steps.prior.outputs.id }}', publish)
        self.assertIn('if: ${{ always() }}', publish.split('Preserve publication state', 1)[1])
        self.assertLess(publish.index('artifact-ids:'), publish.index('watch_recovered_article_publication.py watch'))
        self.assertNotIn('gh run list', publish)

    def test_workspace_uses_runner_environment_after_job_starts_not_job_expression_context(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/recover-report-article-delivery.yml'
        workflow = path.read_text()
        for job_name, prefix, consumer in (
                ('generate', 'recovered-report-articles', 'Authenticate original upload'),
                ('deliver', 'recovered-report-article-delivery', 'Restore complete articles')):
            block = workflow.split('\n  ' + job_name + ':\n', 1)[1].split('\n  deliver:\n', 1)[0]
            job_configuration, steps = block.split('    steps:\n', 1)
            self.assertNotRegex(job_configuration, r'\$\{\{\s*runner\.')
            initialization = steps.split('\n      - ', 1)[0]
            self.assertIn('Initialize isolated article', initialization)
            self.assertIn(f'DELIVERY_WORKSPACE=$RUNNER_TEMP/{prefix}-$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT', initialization)
            self.assertIn('>> "$GITHUB_ENV"', initialization)
            self.assertLess(steps.index('Initialize isolated article'), steps.index(consumer))

    def test_generation_timeout_leaves_budget_for_always_saved_checkpoint(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/recover-report-article-delivery.yml'
        workflow = path.read_text()
        job = workflow.split('\n  generate:\n', 1)[1].split('\n  deliver:\n', 1)[0]
        job_timeout = int(re.search(r'^    timeout-minutes: (\d+)$', job, re.M)[1])
        generate = job.split('- name: Generate only missing bound report articles\n', 1)[1].split('\n      - ', 1)[0]
        step_timeout = int(re.search(r'^        timeout-minutes: (\d+)$', generate, re.M)[1])
        self.assertEqual((job_timeout, step_timeout), (180, 120))
        self.assertGreaterEqual(job_timeout - step_timeout, 60)
        checkpoint = job.split('- name: Save generation progress even after interruption\n', 1)[1].split('\n      - ', 1)[0]
        self.assertIn("always() && steps.prepare.outcome == 'success'", checkpoint)
        self.assertIn('recovered_article_delivery.py save-generation', checkpoint)
        self.assertLess(job.index('Generate only missing bound report articles'), job.index('Save generation progress'))

    def test_workflow_exposes_complete_retained_shards_and_is_draft_only(self):
        path = Path(__file__).resolve().parents[1] / '.github/workflows/recover-report-article-delivery.yml'
        text = path.read_text()
        for required in ('workflow_dispatch:', 'workflow_call:', 'article_handoff_prefix:', 'article_count:',
                         'inputs.upload_wechat', 'secrets.DEEPSEEK_REPORT_NOTES_API_KEY',
                         '--source-handoff-run-id "$SOURCE_HANDOFF_RUN_ID"',
                         '$GITHUB_RUN_ID-$GITHUB_RUN_ATTEMPT', 'watch_recovered_article_publication.py watch',
                         "always() && steps.prepare.outcome == 'success'", "always() && steps.restore.outcome == 'success'"):
            self.assertIn(required, text)
        self.assertNotIn('delete-prefix', text)
        self.assertNotIn('--publish', text)
        # Public publication requests contain only identities/digests. Original
        # sources, article bodies and draft receipts remain in private storage.
        for upload in text.split('uses: actions/upload-artifact@v4')[1:]:
            block = upload.split('\n      - ', 1)[0]
            self.assertRegex(block, r'path: .*\b(?:recovered-publication-request|publication-state)\.json')
            self.assertNotIn('DELIVERY_WORKSPACE', block)
        self.assertLess(text.index('validate-delivery --workspace'), text.index('Update and commit'))

    def test_main_exposes_fixed_category_and_never_provider_text(self):
        with tempfile.TemporaryDirectory() as temporary:
            env = {**{key: str(value) for key, value in config().items()}, 'GH_TOKEN': 'PRIVATE_TOKEN'}
            with patch.dict(delivery.os.environ, env, clear=True), \
                 patch('private_workflow_handoff.build_r2_client', return_value=Store()), \
                 patch('private_workflow_handoff.r2_bucket', return_value='private'), \
                 patch.object(delivery, 'prepare', side_effect=delivery.DeliveryError('original_upload_not_proven_skipped')), \
                 redirect_stdout(io.StringIO()) as public:
                self.assertEqual(delivery.main(['prepare', '--workspace', temporary]), 2)
                self.assertIn('original_upload_not_proven_skipped', public.getvalue())
                self.assertNotIn('PRIVATE_TOKEN', public.getvalue())
            with patch.dict(delivery.os.environ, env, clear=True), \
                 patch('private_workflow_handoff.build_r2_client', side_effect=RuntimeError('PRIVATE_BODY')), \
                 redirect_stdout(io.StringIO()) as public:
                self.assertEqual(delivery.main(['prepare', '--workspace', temporary]), 2)
                self.assertNotIn('PRIVATE_BODY', public.getvalue())
                self.assertIn('RuntimeError', public.getvalue())


class PrivateRoundTripTests(unittest.TestCase):
    def setUp(self):
        from test_recover_report_articles import ArticleRecoveryTests
        self.harness = ArticleRecoveryTests()
        self.harness.setUp()
        self.addCleanup(self.harness.doCleanups)
        self.source = self.harness.mineru()
        self.config = {'SOURCE_RUN_ID': '123', 'SOURCE_HANDOFF_RUN_ID': '456',
                       'SOURCE_KIND': 'mineru-recovery', 'DATE_FOLDER': '261003', 'EXPECTED_ARTICLES': 7}
        self.context = delivery.validate_source(self.source.output, self.config, 'a' * 40, 'b' * 40)
        self.workspace = self.harness.root / 'generation'
        delivery.write_json(self.workspace / 'context.json', self.context)
        delivery.write_json(self.workspace / 'checkpoint/context.json', self.context)
        with self.harness.paid():
            self.receipt = self.harness.recover(self.source, output=self.workspace / 'checkpoint/articles',
                source_run_id='123', source_execution_sha='a' * 40,
                source_handoff_run_id='456', source_handoff_execution_sha='b' * 40)
        self.store = Store()

    def add_policy_fixture(self, count, *, root=None, generation_failure=False):
        import recover_report_articles as articles
        from wechat_editorial_binding import bind_generated_article, FIELD
        root = root or self.workspace / 'checkpoint/articles'
        receipt = articles.read_json(root / articles.RECEIPT)
        for row in receipt['reports'][:count]:
            directory = root / row['directory']
            status = articles.read_json(directory / 'status.json')
            title = '野村：行业技术与相关数据观察'
            body = '# ' + title + '\n\n自建样本的企业交付数据保持稳定。\n'
            if generation_failure:
                body += '\nInsufficient Balance\n'
            (directory / 'wechat_article.md').write_text(body)
            status['wechat_title'] = title
            status['wechat_title_decision'].update(final_title_after_wording_guard=title,
                neutralization_changes=['neutralized:china_systemic_topic'])
            self.assertTrue(bind_generated_article(directory, status))
            articles.write_json(directory / 'status.json', status)
            row.update(article_sha256=status[FIELD]['article_sha256'], editorial_binding=status[FIELD])
        receipt['files'] = articles.inventory(root, exclude=(articles.RECEIPT,))
        articles.write_json(root / articles.RECEIPT, receipt)
        self.assertEqual(articles.validate_articles(root, 7, '261003'), receipt)
        return receipt

    def run_policy_fixture(self, count):
        from contextlib import ExitStack
        import push_xhs_notes_to_wechat_drafts as uploader
        import push_portal_translated_to_wechat_drafts as api_module
        self.add_policy_fixture(count)
        with redirect_stdout(io.StringIO()):
            outputs = delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        self.assertEqual(outputs['article_count'], 7)  # Translation/chart handoff remains complete.
        environment = {'DELIVERY_MANIFEST_SHA256': outputs['manifest_sha256'],
                       'DELIVERY_CONTEXT_SHA256': outputs['context_sha256']}
        consumer = self.harness.root / 'policy-dispatch'
        consumer.mkdir()
        with patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'b' * 40)), redirect_stdout(io.StringIO()):
            delivery.restore_delivery(consumer, self.config, environment, self.store, 'private')

        def build(report_dir, index, *args):
            title = f'Fixture {index}'
            return {'title': title, 'wechat_title': title, 'raw_title': title,
                'article': {'title': title, 'author': 'KC', 'content': f'<p>Body {index}</p>', 'thumb_media_id': 'THUMB'},
                'institution_name': 'Fixture', 'source_report_name': f'fixture-{index}.pdf',
                'report_dir': str(report_dir), 'content_chars': 100, 'content_bytes': 200,
                'visible_text_chars': 100, 'inline_images': [], 'body_image_count': 0,
                'cover_image': '', 'title_decision': {}}

        with ExitStack() as stack, redirect_stdout(io.StringIO()):
            stack.enter_context(patch.dict(delivery.os.environ, {
                'PORTAL_SITE_URL': 'https://private.example.invalid', 'WECHAT_MP_APPID': 'TEST', 'WECHAT_MP_APPSECRET': 'TEST'}))
            token = Mock(return_value='TOKEN')
            readback = {'ok': True, 'article_count': 7-count, 'matches_editorial_contract': True,
                        'matches_expected_article_count': True, 'matches_expected_titles': True}
            for name, value in {'get_stable_access_token': token, 'build_article': build,
                                'pacing_sleep': Mock(), 'DEFAULT_TRAILING_IMAGE': '',
                                'find_recent_draft_by_titles': Mock(return_value=''),
                                'verify_draft_get': Mock(return_value=readback)}.items():
                stack.enter_context(patch.object(uploader, name, value))
            post = stack.enter_context(patch.object(api_module, 'post_wechat_json', return_value=object()))
            stack.enter_context(patch.object(api_module, 'parse_wechat_json', return_value={'media_id': 'ELIGIBLE_ACK'}))
            receipt = delivery.upload_wechat(consumer, self.store, 'private')
            self.assertTrue(delivery.save_receipts(consumer, self.store, 'private'))
            if count == 7:
                token.assert_not_called()
                post.assert_not_called()
            else:
                post.assert_called_once()
        self.assertEqual((receipt['source_report_count'], receipt['article_count'], receipt['policy_excluded_count'],
                          receipt['accounted_report_count']), (7, 7-count, count, 7))
        return consumer, environment

    def test_real_policy_exclusion_delivers_remaining_six_and_rejects_forged_partition(self):
        consumer, _ = self.run_policy_fixture(1)
        path = delivery.receipt_root(consumer, self.context) / 'wechat_draft_summary.json'
        summary = delivery.read_json(path)
        self.assertEqual(summary['skipped_title_policy'][0]['skip_reason'], 'nomura_sensitive_report')
        mutations = []
        wrong_reason = copy.deepcopy(summary)
        wrong_reason['skipped_title_policy'][0]['skip_reason'] = 'invented_policy'
        mutations.append(wrong_reason)
        forged_allowed = copy.deepcopy(summary)
        record = forged_allowed['skipped_title_policy'][0]
        allowed = forged_allowed['articles'][0]['report_dir']
        record.update(report_dir=allowed, wechat_markdown=allowed + '/wechat_article.md')
        mutations.append(forged_allowed)
        missing = copy.deepcopy(summary)
        missing.update(skipped_title_policy=[], skipped_title_policy_count=0)
        mutations.append(missing)
        duplicate = copy.deepcopy(summary)
        duplicate['skipped_title_policy'] *= 2
        duplicate['skipped_title_policy_count'] = 2
        mutations.append(duplicate)
        duplicate_delivered = copy.deepcopy(summary)
        duplicate_delivered['articles'][0] = duplicate_delivered['articles'][1]
        mutations.append(duplicate_delivered)
        omitted_delivered = copy.deepcopy(summary)
        omitted_delivered['articles'].pop()
        mutations.append(omitted_delivered)
        generation_skip = copy.deepcopy(summary)
        generation_skip['skipped_generation_failure_count'] = 1
        mutations.append(generation_skip)
        for index, changed in enumerate(mutations):
            delivery.write_json(path, changed)
            with self.subTest(index=index), self.assertRaises(delivery.DeliveryError):
                delivery.validate_delivery(consumer)
        delivery.write_json(path, summary)
        self.add_policy_fixture(1, root=consumer / 'checkpoint/articles', generation_failure=True)
        with self.assertRaisesRegex(delivery.DeliveryError, 'generation_failure_present'):
            delivery.validate_delivery(consumer)

    def test_all_policy_blocked_roundtrip_records_zero_real_delivery_without_api_calls(self):
        consumer, environment = self.run_policy_fixture(7)
        root = delivery.receipt_root(consumer, self.context)
        summary = delivery.read_json(root / 'wechat_draft_summary.json')
        self.assertEqual((summary['status'], summary['drafts'], summary['articles']), ('skipped_title_policy', [], []))
        self.assertTrue((root / 'wechat_delivery_receipt.json').is_file())
        restored = self.harness.root / 'policy-next-dispatch'
        restored.mkdir()
        with patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'b' * 40)), redirect_stdout(io.StringIO()):
            delivery.restore_delivery(restored, self.config, environment, self.store, 'private')
        receipt = delivery.validate_delivery(restored)
        self.assertEqual((receipt['source_report_count'], receipt['article_count'], receipt['policy_excluded_count']), (7, 0, 7))
        # The Blog loader scans payloads independently of summary.json. A stale
        # payload must not become publishable merely because every source skipped.
        delivery.write_json(delivery.receipt_root(restored, self.context) / 'draft_payload_stale.json',
                            {'articles': [{'title': 'Stale', 'content': '<p>Old body</p>'}]})
        with self.assertRaisesRegex(delivery.DeliveryError, 'unaccounted_archive_payload'):
            delivery.validate_delivery(restored)

    def test_full_real_source_generation_archive_restore_and_existing_receipts_across_dispatch(self):
        with redirect_stdout(io.StringIO()):
            outputs = delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        self.assertEqual(outputs['article_count'], 7)
        self.assertTrue(outputs['article_handoff_prefix'].endswith('/articles'))
        self.assertIn(outputs['article_handoff_prefix'] + '/shard_0.tar.gz', self.store.objects)
        environment = {'DELIVERY_MANIFEST_SHA256': outputs['manifest_sha256'],
                       'DELIVERY_CONTEXT_SHA256': outputs['context_sha256']}
        consumer = self.harness.root / 'another-dispatch'
        consumer.mkdir()
        with patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'b' * 40)), \
             redirect_stdout(io.StringIO()):
            delivery.restore_delivery(consumer, self.config, environment, self.store, 'private')
        self.assertEqual(delivery.article_receipt(consumer, self.context), self.receipt)
        self.assertEqual(len(list((consumer / 'xhs/261003/shard_0').glob('*/wechat_article.md'))), 7)
        import push_portal_translated_to_wechat_drafts as api_module
        articles = [{'title': f'Article {index}', 'author': 'KC', 'content': f'<p>Body {index}</p>'}
                    for index in range(7)]
        root = delivery.receipt_root(consumer, self.context)
        delivery.write_json(root / 'draft_payload_01.json', {'articles': articles})
        summary = {'date_folder': '261003', 'dry_run': False, 'publish': False, 'status': 'verified',
                   'input_selected_count': 7, 'selected_count': 7, 'skipped_title_policy_count': 0,
                   'skipped_generation_failure_count': 0, 'draft_count': 1,
                   'articles': [{'report_dir': row['directory']} for row in self.receipt['reports']],
                   'drafts': [{'media_id': 'ACCEPTED', 'group_key': api_module.draft_group_key(articles),
                       'payload': '/old/runner/draft_payload_01.json', 'status': 'verified', 'article_count': 7,
                       'draft_get': {'ok': True, 'article_count': 7, 'matches_editorial_contract': True,
                           'matches_expected_article_count': True, 'matches_expected_titles': True}}]}
        delivery.write_json(root / 'wechat_draft_summary.json', summary)
        self.assertEqual(delivery.validate_delivery(consumer)['article_count'], 7)
        with redirect_stdout(io.StringIO()):
            self.assertTrue(delivery.save_receipts(consumer, self.store, 'private'))
        next_consumer = self.harness.root / 'next-dispatch'
        next_consumer.mkdir()
        with patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'b' * 40)), \
             redirect_stdout(io.StringIO()):
            delivery.restore_delivery(next_consumer, self.config, environment, self.store, 'private')
        restored = delivery.receipt_root(next_consumer, self.context)
        self.assertEqual(api_module.saved_draft_receipt(restored, articles)['media_id'], 'ACCEPTED')
        self.assertEqual(delivery.validate_delivery(next_consumer)['article_count'], 7)
        for key, value in (('selected_count', 6), ('status', 'skipped_no_xhs_wechat_articles'), ('dry_run', True)):
            broken = dict(summary, **{key: value})
            delivery.write_json(root / 'wechat_draft_summary.json', broken)
            with self.subTest(key=key), self.assertRaises(delivery.DeliveryError):
                delivery.validate_delivery(consumer)
        broken = copy.deepcopy(summary)
        broken['drafts'][0]['draft_get']['matches_editorial_contract'] = False
        delivery.write_json(root / 'wechat_draft_summary.json', broken)
        with self.assertRaises(delivery.DeliveryError):
            delivery.validate_delivery(consumer)

    def test_invalid_full_package_never_overwrites_durable_checkpoint(self):
        with redirect_stdout(io.StringIO()):
            delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        before = dict(self.store.objects)
        article = next((self.workspace / 'checkpoint/articles').glob('*/wechat_article.md'))
        article.write_text('corrupt body')
        with self.assertRaises(Exception):
            delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        self.assertEqual(self.store.objects, before)

    def test_actual_delivery_wrapper_persists_ack_before_readback_and_reuses_across_dispatch(self):
        from contextlib import ExitStack
        import push_xhs_notes_to_wechat_drafts as uploader
        import push_portal_translated_to_wechat_drafts as api_module
        with redirect_stdout(io.StringIO()):
            outputs = delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        environment = {'DELIVERY_MANIFEST_SHA256': outputs['manifest_sha256'],
                       'DELIVERY_CONTEXT_SHA256': outputs['context_sha256']}

        def build(report_dir, index, *args):
            title = f'Fixture article {index}'
            return {'title': title, 'wechat_title': title, 'raw_title': title,
                'article': {'title': title, 'author': 'KC', 'content': f'<p>Source body {index}</p>', 'thumb_media_id': 'THUMB'},
                'institution_name': 'Fixture', 'source_report_name': f'source-{index}.pdf',
                'report_dir': str(report_dir), 'content_chars': 100, 'content_bytes': 200,
                'visible_text_chars': 100, 'inline_images': [], 'body_image_count': 0,
                'cover_image': '', 'title_decision': {}}

        def check_ack(*args):
            key = delivery.context_prefix(self.context) + '/wechat-receipts.tar.gz'
            self.assertIn(key, self.store.objects)
            return {'ok': False}

        with ExitStack() as stack, redirect_stdout(io.StringIO()):
            stack.enter_context(patch.dict(delivery.os.environ, {
                'PORTAL_SITE_URL': 'https://private.example.invalid', 'WECHAT_MP_APPID': 'TEST', 'WECHAT_MP_APPSECRET': 'TEST'}))
            for name, value in {'get_stable_access_token': Mock(return_value='TOKEN'), 'build_article': build,
                                'pacing_sleep': Mock(), 'DEFAULT_TRAILING_IMAGE': '',
                                'find_recent_draft_by_titles': Mock(return_value='')}.items():
                stack.enter_context(patch.object(uploader, name, value))
            post = stack.enter_context(patch.object(api_module, 'post_wechat_json', return_value=object()))
            stack.enter_context(patch.object(api_module, 'parse_wechat_json', return_value={'media_id': 'DURABLE_ACK'}))
            publish = stack.enter_context(patch.object(uploader, 'submit_publish'))
            for index in range(2):
                consumer = self.harness.root / f'dispatch-{index}'
                consumer.mkdir()
                with patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'b' * 40)):
                    delivery.restore_delivery(consumer, self.config, environment, self.store, 'private')
                if index == 0:
                    with patch.object(uploader, 'verify_draft_get', side_effect=check_ack), self.assertRaises(api_module.WeChatError):
                        delivery.upload_wechat(consumer, self.store, 'private')
                else:
                    readback = {'ok': True, 'article_count': 7, 'matches_editorial_contract': True,
                                'matches_expected_article_count': True, 'matches_expected_titles': True}
                    with patch.object(uploader, 'verify_draft_get', return_value=readback):
                        self.assertEqual(delivery.upload_wechat(consumer, self.store, 'private')['article_count'], 7)
                    delivery.save_receipts(consumer, self.store, 'private')
            post.assert_called_once()
            publish.assert_not_called()

    def test_changed_handoff_cannot_overwrite_generation_or_create_more_articles(self):
        with redirect_stdout(io.StringIO()):
            delivery.save_generation(self.workspace, self.store, 'private', complete=True)
        from private_workflow_handoff import upload_directory
        with redirect_stdout(io.StringIO()):
            upload_directory(self.source.output,
                '_private-workflow-handoff/mineru-market-sources/999/261003/shard_0.tar.gz',
                client=self.store, bucket='private')
        before = dict(self.store.objects)
        changed = dict(self.context, source_handoff_run_id='999', handoff_execution_sha='e' * 40)
        with tempfile.TemporaryDirectory() as directory, \
             patch.object(delivery, 'authenticated_context', return_value=('a' * 40, 'e' * 40)), \
             patch.object(delivery, 'validate_source', return_value=changed), redirect_stdout(io.StringIO()), \
             self.assertRaisesRegex(delivery.DeliveryError, 'generation_checkpoint_source_changed'):
            delivery.prepare(Path(directory), dict(self.config, SOURCE_HANDOFF_RUN_ID='999'), {}, self.store, 'private')
        # Only the immutable date/manifest ownership claim may have been added.
        for key, value in before.items():
            self.assertEqual(self.store.objects[key], value)


if __name__ == '__main__':
    unittest.main()
