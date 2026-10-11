"""Exact original job, immutable admitted bytes, and zero-write probe tests."""
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import tempfile
import subprocess
import unittest
import zipfile
from unittest.mock import Mock, patch

import probe_consulting_mineru_figure_binding as p
from mineru_task_ledger import FileStore, Ledger, digest, encoded
from mineru_result_cache import ResultCache
from test_mineru_result_cache import MemoryR2, result_zip


class GitHubReadTests(unittest.TestCase):
    def test_safe_failure_classification_preserves_stage_and_never_retries(self):
        cases = (
            (1, b'gh: Resource not accessible (HTTP 403) private-secret', 'http_403'),
            (1, b'gh: gone (HTTP 404) https://signed.invalid/private', 'http_404'),
            (1, b'error connecting to api.github.com private-secret', 'network_stop'),
            (1, b'x509: certificate has expired private-secret', 'network_stop'),
            (4, b'gh auth login private-secret', 'authentication_required'),
            (1, b'the response contains terminal escape sequences; pass --allow-escape-sequences to output it anyway', 'cli_escape_sequence_rejected'),
            (1, b'unknown private-secret', 'cli_error'),
        )
        for operation in ('run_metadata', 'job_metadata', 'job_logs'):
            for code, stderr, expected in cases:
                with self.subTest(operation=operation, expected=expected), patch.object(p, 'job_log_flags', return_value=[]), patch.object(p.subprocess, 'run',
                        return_value=Mock(returncode=code, stderr=stderr, stdout=b'private body')) as call:
                    with self.assertRaises(p.ProbeError) as error:
                        p.gh_bytes('repos/example/report-repository/actions/runs/123', operation)
                    self.assertEqual(str(error.exception), 'github_' + operation + '_' + expected)
                    self.assertEqual(call.call_count, 1)

    def test_timeout_and_missing_cli_stop_without_returning_exception_details(self):
        for error, expected in ((subprocess.TimeoutExpired(['gh', 'private'], 60, stderr=b'private'), 'network_stop'),
                                (FileNotFoundError('private executable path'), 'cli_unavailable')):
            with self.subTest(expected=expected), patch.object(p, 'job_log_flags', return_value=[]), patch.object(p.subprocess, 'run', side_effect=error) as call:
                with self.assertRaisesRegex(p.ProbeError, '^github_job_logs_' + expected + '$'):
                    p.gh_bytes('repos/example/report-repository/actions/jobs/456/logs', 'job_logs')
                self.assertEqual(call.call_count, 1)

    def test_success_keeps_exact_raw_log_bytes(self):
        with patch.object(p, 'job_log_flags', return_value=[]), patch.object(p.subprocess, 'run', return_value=Mock(returncode=0, stdout=b'exact log\r\n')):
            self.assertEqual(p.gh_bytes('endpoint', 'job_logs'), b'exact log\r\n')

    def test_new_cli_raw_escape_log_is_captured_once_and_preserved_for_identity(self):
        original = b'2026-10-11T00:00:00.0Z \x1b[36;1moriginal log\x1b[0m\n'
        with patch.object(p.subprocess, 'run', side_effect=[
                Mock(returncode=0, stdout=b'OPTIONS\n --allow-escape-sequences Allow printing terminal escape sequences\n'),
                Mock(returncode=0, stdout=original)]) as call:
            result = p.gh_bytes('repos/example/report-repository/actions/jobs/456/logs', 'job_logs')
        self.assertEqual(result, original)
        self.assertEqual(digest(result), digest(original))
        self.assertEqual(call.call_count, 2)  # local help, then one remote read
        self.assertEqual(call.call_args_list[0].args[0], ['gh', 'api', '--help'])
        self.assertEqual(call.call_args_list[1].args[0][-1], '--allow-escape-sequences')
        self.assertTrue(call.call_args_list[1].kwargs['capture_output'])

    def test_old_cli_log_request_has_no_unsupported_flag(self):
        with patch.object(p.subprocess, 'run', side_effect=[
                Mock(returncode=0, stdout=b'OPTIONS --silent --include'),
                Mock(returncode=0, stdout=b'original log')]) as call:
            self.assertEqual(p.gh_bytes('endpoint', 'job_logs'), b'original log')
        self.assertEqual(call.call_args_list[1].args[0], ['gh', 'api', 'endpoint'])

    def test_metadata_never_allows_raw_escape_sequences_or_runs_help(self):
        with patch.object(p.subprocess, 'run', return_value=Mock(returncode=0, stdout=b'{}')) as call:
            self.assertEqual(p.gh_json('endpoint', 'run_metadata'), {})
        self.assertEqual(call.call_count, 1)
        self.assertEqual(call.call_args.args[0], ['gh', 'api', 'endpoint'])

    def test_help_failure_stops_before_any_remote_request(self):
        with patch.object(p.subprocess, 'run', return_value=Mock(returncode=1, stdout=b'private')) as call:
            with self.assertRaisesRegex(p.ProbeError, '^github_job_logs_cli_help_invalid$'):
                p.gh_bytes('endpoint', 'job_logs')
        self.assertEqual(call.call_count, 1)
        self.assertEqual(call.call_args.args[0], ['gh', 'api', '--help'])


class AuthTests(unittest.TestCase):
    def setUp(self):
        self.run = {'id': 123, 'status': 'completed', 'head_branch': 'main', 'path': p.PRODUCER,
            'head_sha': 'a' * 40, 'event': 'schedule',
            'repository': {'full_name': p.REPOSITORY}, 'head_repository': {'full_name': p.REPOSITORY}}
        self.job = {'id': 456, 'run_id': 123, 'status': 'completed', 'name': 'fetch-and-build', 'head_sha': 'a' * 40}
        self.summary = {'requested': 2, 'completed': 2, 'pending': 0, 'failed': 0,
            'ready_for_generation': True, 'batch_keys': ['batches/' + 'b' * 32]}
        self.log = ('2026-10-11T00:00:00.0Z HEAD is now at aaaaaaa Original checkout\n'
            '2026-10-11T00:00:01.0Z   saved BCG_b_87654321.pdf (2 KB) <- https://web-assets.bcg.com/b.pdf\n'
            '2026-10-11T00:00:02.0Z   saved BCG_a_12345678.pdf (1 KB) <- https://web-assets.bcg.com/a.pdf\n'
            '2026-10-11T00:00:03.0Z MinerU durable task summary: ' + json.dumps(self.summary) + '\n').encode()

    def authenticate(self, **kwargs):
        return p.authenticate(kwargs.get('run', self.run), kwargs.get('job', self.job),
            kwargs.get('log', self.log), '123', '456', 2, 1)

    def test_exact_completed_job_selects_sorted_original_inventory(self):
        value = self.authenticate()
        self.assertEqual(value['selected'], ('BCG_a_12345678.pdf', 'https://web-assets.bcg.com/a.pdf'))
        self.assertEqual(value['log_sha256'], digest(self.log))

    def test_foreign_changed_incomplete_producers_rejected(self):
        for key, value in (('head_branch', 'feature'), ('status', 'in_progress'),
                           ('path', 'other.yml'), ('event', 'pull_request')):
            with self.subTest(key=key), self.assertRaises(p.ProbeError):
                self.authenticate(run=dict(self.run, **{key: value}))
        with self.assertRaisesRegex(p.ProbeError, 'producer_checkout_changed'):
            self.authenticate(log=self.log.replace(b'aaaaaaa Original', b'bbbbbbb Original'))
        with self.assertRaisesRegex(p.ProbeError, 'producer_job_identity'):
            self.authenticate(job=dict(self.job, run_id=999))

    def test_unauthorized_url_and_partial_inventory_never_reach_download(self):
        for log in (self.log.replace(b'web-assets.bcg.com/a.pdf', b'evil.invalid/a.pdf'),
                    self.log.replace(b'BCG_a_12345678.pdf', b'../outside.pdf'),
                    self.log.replace(b'"completed": 2', b'"completed": 1')):
            with self.subTest(log=digest(log)), self.assertRaises(p.ProbeError):
                self.authenticate(log=log)


class Provider:
    def __init__(self, item):
        self.item, self.gets = item, 0
    def poll(self, *_):
        self.gets += 1
        return [{'data_id': self.item['id'], 'state': 'done', 'full_zip_url': 'https://results.invalid/secret-signed-url'}]
    def submit(self, *_):
        raise AssertionError('No submission')
    def upload(self, *_):
        raise AssertionError('No upload')


class ProbeTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        path = self.root / 'source.pdf'; self.original = b'%PDF-1.7 original'; path.write_bytes(self.original)
        self.ledger = Ledger(FileStore(self.root / 'ledger'), None, 'consulting', 'https://mineru.net',
            p.OPTIONS, [('MINER_U', 'fixture-private-token')])
        self.binding = self.ledger.bind(path, 'BCG_a_12345678.pdf')
        self.ledger.provider = Provider(self.binding)
        self.key = 'batches/' + 'b' * 32
        self.batch = {'schema': 1, 'key': self.key, 'scope': 'consulting', 'endpoint': 'https://mineru.net',
            'options': p.OPTIONS, 'token_identity': next(iter(self.ledger.tokens)), 'files': [self.binding],
            'state': 'terminal', 'batch_id': 'test-original-task'}
        self.ledger.store.put(self.key, self.batch)
        self.ledger.store.put('sources/' + self.binding['id'], {'schema': 1, 'binding': self.binding, 'batch_key': self.key})
        self.plan = {'selected': ('BCG_a_12345678.pdf', 'https://web-assets.bcg.com/a.pdf'), 'batch_keys': [self.key]}
        self.r2 = MemoryR2(); self.cache = ResultCache(self.r2, 'test-private'); self.downloads = []
        self.payload = result_zip()

    def download(self, url):
        self.downloads.append(url)
        return self.original if url == self.plan['selected'][1] else self.payload

    def probe(self):
        with patch.object(p, 'compare_cached_pdf', return_value={'status': 'mismatch', 'stage': 'rgb_pixels'}), \
             patch.object(p, 'verify_production_figures', return_value={'status': 'verified', 'production_consumer_verified': True}), \
             patch.object(self.ledger.store, 'put', side_effect=AssertionError('No ledger write')):
            return p.probe(self.ledger, self.cache, self.plan, self.download, expected_articles=1, ordinal=1)

    def test_uncached_existing_result_is_downloaded_once_without_any_writes_or_artifacts(self):
        value = self.probe()
        self.assertEqual(len(self.downloads), 2)
        self.assertEqual(value['provider_zip_downloads'], 1)
        self.assertEqual(value['comparison']['stage'], 'rgb_pixels')
        self.assertTrue(value['production_figure_consumer']['production_consumer_verified'])
        self.assertEqual(self.r2.puts, [])
        self.assertNotIn('secret-signed-url', json.dumps(value))
        self.assertNotIn('BCG_a', json.dumps(value))
        for key in ('provider_posts', 'provider_uploads', 'model_calls', 'canonical_ledger_writes', 'cache_writes', 'artifact_downloads'):
            self.assertEqual(value[key], 0)

    def test_exact_cache_avoids_result_download_and_still_checks_original_bytes(self):
        lineage = {'batch_id': 'test-original-task', 'batch_key': self.key, 'parent_batch_key': self.key,
            'data_id': self.binding['id'], 'child_ordinal': 0}
        self.cache.put(self.binding, lineage, self.payload); self.r2.puts.clear()
        value = self.probe()
        self.assertEqual(self.downloads, [self.plan['selected'][1]])
        self.assertTrue(value['cache_hit']); self.assertEqual(value['provider_zip_downloads'], 0)
        self.assertEqual(self.r2.puts, [])

    def test_changed_source_bytes_stop_before_result_or_cache_read(self):
        self.original += b'changed'
        with self.assertRaisesRegex(p.ProbeError, 'original_source_bytes_changed'):
            self.probe()
        self.assertEqual(len(self.downloads), 1); self.assertEqual(self.r2.gets, [])

    def test_changed_claim_stops_before_source_download(self):
        claim, version = self.ledger.store.get('sources/' + self.binding['id'])
        claim['batch_key'] = 'batches/' + 'c' * 32
        self.ledger.store.put('sources/' + self.binding['id'], claim, version)
        with self.assertRaisesRegex(p.ProbeError, 'selected_source_claim'):
            self.probe()
        self.assertEqual(self.downloads, [])


class ProductionConsumerTests(unittest.TestCase):
    def setUp(self):
        from test_mineru_figure_sources import Fixture, visual
        from test_mineru_pdf_output_intents import output_intent_fixture, pdfium_copy
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        self.fixture = Fixture(self.root / 'fixture', pages=2, visuals=[
            visual(0, [35,100,185,260], kind='chart', page_idx=0),
            visual(1, [35,100,185,260], kind='chart', page_idx=1)])
        self.original = output_intent_fixture(plain_first=True)
        self.embedded = pdfium_copy(self.original)
        self.fixture.original.write_bytes(self.original)
        (self.fixture.raw / 'source.pdf').write_bytes(self.embedded)

    def archive(self):
        output = io.BytesIO()
        with zipfile.ZipFile(output, 'w', zipfile.ZIP_DEFLATED) as archive:
            archive.writestr('full.md', (self.fixture.report / 'source_mineru.md').read_bytes())
            for path in self.fixture.raw.rglob('*'):
                if path.is_file(): archive.writestr(path.relative_to(self.fixture.raw).as_posix(), path.read_bytes())
        return output.getvalue()

    def verify(self, payload=None):
        import requests
        import urllib.request
        with (patch.object(requests.sessions.Session, 'request', side_effect=AssertionError('No network')),
                patch.object(urllib.request, 'urlopen', side_effect=AssertionError('No network'))):
            return p.verify_production_figures(self.fixture.original, payload or self.archive(), digest(self.original))

    def test_real_producer_and_consumer_accept_exact_icc_repair_and_raw_free_handoff(self):
        import mineru_figure_sources as figures
        import pdf_to_xhs_batch as producer
        raw = self.archive()
        with (patch.object(producer, 'create_chart_source_assets', wraps=producer.create_chart_source_assets) as create,
                patch.object(figures, 'validate_figure_sources', wraps=figures.validate_figure_sources) as validate):
            result = self.verify(raw)
        self.assertEqual(result['status'], 'verified', result)
        self.assertTrue(result['production_consumer_verified']); self.assertTrue(result['private_handoff_replay_verified'])
        self.assertEqual(create.call_count, 1); self.assertEqual(validate.call_count, 2)
        self.assertEqual(create.call_args.args[2], 8)
        self.assertEqual(result['image_count'], 2); self.assertEqual(result['selected_page_count'], 2)
        self.assertEqual(result['validated_reference_count'], 2)
        self.assertEqual(result['restoration_policy'], 'authenticated-outputintents-restoration-v1')
        self.assertEqual(result['original_pdf_sha256'], digest(self.original))
        self.assertEqual(result['result_zip_sha256'], digest(raw))
        self.assertEqual(self.fixture.original.read_bytes(), self.original)
        self.assertEqual((self.fixture.raw / 'source.pdf').read_bytes(), self.embedded)
        self.assertFalse(result['production_acceptance']); self.assertFalse(result['complete_source_handoff'])
        for private in ('Synthetic', 'PRIVATE_PROFILE', 'images/image-', 'full.md', str(self.root)):
            self.assertNotIn(private, json.dumps(result))

    def test_changed_provider_body_is_rejected_by_real_producer(self):
        from test_mineru_pdf_output_intents import changed
        altered = changed(self.embedded, lambda doc: doc[0].insert_text((30,80), 'PRIVATE ALTERED', fontsize=9))
        (self.fixture.raw / 'source.pdf').write_bytes(altered)
        result = self.verify()
        self.assertEqual(result['status'], 'rejected')
        self.assertEqual(result['category'], 'figure_source_pixels_mismatch')
        self.assertFalse(result['production_consumer_verified'])
        self.assertNotIn('PRIVATE ALTERED', json.dumps(result))

    def test_sidecar_removal_during_raw_free_handoff_is_rejected(self):
        import mineru_figure_sources as figures
        real_validate = figures.validate_figure_sources
        calls = 0
        def tamper(report, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 2: (Path(report) / figures.SIDECAR).unlink()
            return real_validate(report, **kwargs)
        with patch.object(figures, 'validate_figure_sources', side_effect=tamper):
            result = self.verify()
        self.assertEqual(result['status'], 'rejected'); self.assertEqual(calls, 2)
        self.assertFalse(result['private_handoff_replay_verified'])

    def test_image_map_mismatch_and_producer_private_output_never_escape(self):
        import pdf_to_xhs_batch as producer
        real_create = producer.create_chart_source_assets
        def bad_map(raw, assets, *args, **kwargs):
            print('PRIVATE PRODUCER OUTPUT')
            images = real_create(raw, assets, *args, **kwargs)
            path = assets.parent / 'source_image_map.json'
            value = json.loads(path.read_bytes()); value['images'] = {}; path.write_text(json.dumps(value))
            return images
        output = io.StringIO()
        with patch.object(producer, 'create_chart_source_assets', side_effect=bad_map), redirect_stdout(output), redirect_stderr(output):
            result = self.verify()
        self.assertEqual(result['status'], 'rejected'); self.assertEqual(result['category'], 'production_image_map_mismatch')
        self.assertEqual(output.getvalue(), '')
        self.assertNotIn('PRIVATE PRODUCER OUTPUT', json.dumps(result))

    def test_changed_admitted_original_stops_before_unpack_or_consumer(self):
        self.fixture.original.write_bytes(self.original + b'changed')
        with patch('consume_legacy_mineru.safe_unzip', side_effect=AssertionError('No unpack')):
            result = self.verify()
        self.assertEqual(result['status'], 'rejected'); self.assertEqual(result['category'], 'production_original_bytes_changed')


if __name__ == '__main__':
    unittest.main()
