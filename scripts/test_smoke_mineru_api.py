"""Offline smoke regressions; fake HTTP and local ledger only."""
from __future__ import annotations
import io
import json
import re
import copy
from datetime import timedelta
from pathlib import Path
import ssl
import tempfile
import unittest
from unittest.mock import patch
import urllib.error
import zipfile

import consume_legacy_mineru as result_helpers
import mineru_task_ledger as durable
import smoke_mineru_api as smoke
from test_mineru_result_cache import MemoryR2

TOKENS = [('MINER_U', 'private-key-a'), ('MINER_U_2', 'private-key-b')]


class Clock:
    now = 0
    def time(self): return self.now
    def sleep(self, seconds): self.now += seconds


class Response:
    def __init__(self, status, body):
        self.status_code, self.body, self.closed = status, body, False
    def json(self): return self.body
    def close(self): self.closed = True


class FakeHTTP:
    def __init__(self):
        self.posts, self.uploads, self.polls, self.files = [], [], [], []
        self.mode = 'done'
        self.reject_first = False
        self.reject_all = False
        self.result_url = 'https://results.invalid/private?signed=secret'
    def post(self, url, **kw):
        self.posts.append(kw)
        if self.mode == 'unknown':
            raise TimeoutError('remote details and private-key-a must never be printed')
        if self.reject_all or (self.reject_first and kw['headers']['Authorization'] == 'Bearer private-key-a'):
            return Response(200, {'code': 'A0211', 'data': {}})
        self.files = kw['json']['files']
        return Response(200, {'code': 0, 'data': {'batch_id': 'single-accepted-task',
                                                'file_urls': ['https://uploads.invalid/private']}})
    def put(self, url, **kw):
        self.uploads.append(kw)
        return Response(200, {})
    def get(self, url, **kw):
        self.polls.append(kw)
        rows = [{'data_id': item['data_id'], 'state': self.mode,
                 **({'full_zip_url': self.result_url} if self.mode == 'done' else {})}
                for item in self.files]
        return Response(200, {'code': 0, 'data': {'extract_result': rows}})


def zipped(text=None, name='full.md'):
    out = io.BytesIO()
    with zipfile.ZipFile(out, 'w') as archive:
        archive.writestr(name, text if text is not None else smoke.MARKER + '\nCost 42.75 Revenue 125.50 Combined 168.25\n')
    return out.getvalue()


class SmokeTests(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        self.store = durable.FileStore(self.root / 'ledger')
        self.http = FakeHTTP()
        self.clock = Clock()
    def run_smoke(self, *, tokens=TOKENS, downloader=lambda _: zipped(), run_id='123456', result_downloader=None):
        return smoke.run_smoke(run_id, self.store, durable.Provider(self.http, smoke.ENDPOINT), tokens,
                               downloader=downloader, result_downloader=result_downloader,
                               clock=self.clock.time, sleep=self.clock.sleep)
    def batches(self):
        return [json.loads(path.read_text()) for path in (self.root / 'ledger' / 'batches').glob('*.json')]
    def test_deterministic_fixture_is_exactly_one_page_without_private_report(self):
        first, second = smoke.synthetic_pdf(), smoke.synthetic_pdf()
        self.assertEqual(first, second)
        self.assertEqual(len(re.findall(rb'/Type\s*/Page\b', first)), 1)
        self.assertIn(smoke.MARKER.encode(), first)
        for number in smoke.NUMBERS: self.assertIn(number.encode(), first)
    def test_full_parse_zip_marker_and_numbers_are_required_and_summary_is_sanitized(self):
        result = self.run_smoke()
        self.assertEqual(result['status'], 'passed')
        self.assertTrue(result['authentication']['accepted'])
        self.assertTrue(result['download']['complete_zip_verified'])
        self.assertTrue(result['marker_verified'])
        self.assertEqual((result['provider_posts'], result['parse']['requested']), (1, 1))
        self.assertEqual(len(self.http.uploads), 1)
        public = json.dumps(result)
        for private in ('private-key', 'signed=', 'results.invalid', smoke.MARKER, 'single-accepted-task'):
            self.assertNotIn(private, public)
    def test_rerun_uses_original_task_key_and_exact_bytes_without_another_post(self):
        first = self.run_smoke()
        second = self.run_smoke(tokens=list(reversed(TOKENS)))
        self.assertEqual(second['status'], 'passed')
        self.assertEqual(second['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
        self.assertEqual(first['hashes']['pdf_sha256'], second['hashes']['pdf_sha256'])
        self.assertEqual(self.http.polls[-1]['headers']['Authorization'], 'Bearer private-key-a')
        self.assertEqual(len(self.batches()), 1)
    def test_unknown_submission_crash_blocks_rerun_post(self):
        self.http.mode = 'unknown'
        first = self.run_smoke()
        self.assertEqual(first['category'], 'durable_task_stopped')
        self.assertEqual(first['provider_posts'], 1)
        self.assertTrue(first['network_stop'])
        self.assertIsNone(first['authentication']['accepted'])
        self.assertEqual(self.batches()[0]['state'], 'submitting')
        self.http.mode = 'done'
        second = self.run_smoke()
        self.assertEqual(second['category'], 'durable_task_stopped')
        self.assertEqual(second['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
        self.assertEqual(self.http.polls, [])
    def test_exact_auth_rejection_falls_through_once_but_only_one_task_is_accepted(self):
        self.http.reject_first = True
        result = self.run_smoke()
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['provider_posts'], 2)
        self.assertEqual(len(self.http.uploads), 1)
        batch = self.batches()[0]
        self.assertEqual(batch['auth_rejections'][0]['code'], 'A0211')
        self.assertEqual(batch['token_identity'], durable.token_fingerprint('private-key-b'))
        self.assertEqual(len(self.batches()), 1)
    def test_four_configured_keys_fall_through_definitive_rejection_only(self):
        tokens = [('MINER_U' + (('_' + str(i)) if i > 1 else ''), 'private-key-' + str(i)) for i in range(1, 5)]
        original = self.http.post
        def reject_three(url, **kwargs):
            if kwargs['headers']['Authorization'] != 'Bearer private-key-4':
                self.http.posts.append(kwargs)
                return Response(200, {'code': 'A0202', 'data': {}})
            return original(url, **kwargs)
        with patch.object(self.http, 'post', side_effect=reject_three):
            result = self.run_smoke(tokens=tokens)
        self.assertEqual(result['status'], 'passed')
        self.assertEqual(result['authentication']['configured_slots'], 4)
        self.assertEqual(result['provider_posts'], 4)
        self.assertEqual(len(self.http.uploads), 1)
        self.assertEqual(len(self.batches()), 1)
        self.assertEqual(len(self.batches()[0]['auth_rejections']), 3)
        again = self.run_smoke(tokens=tokens)
        self.assertEqual(again['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 4)
    def test_all_rejected_keys_do_not_report_acceptance_or_create_another_batch(self):
        self.http.reject_all = True
        result = self.run_smoke()
        self.assertEqual(result['category'], 'authentication_rejected')
        self.assertIs(result['authentication']['accepted'], False)
        self.assertEqual(result['provider_posts'], 2)
        self.assertEqual(self.http.uploads, [])
        again = self.run_smoke()
        self.assertEqual(again['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 2)
        self.assertEqual(len(self.batches()), 1)
    def test_accepted_original_key_cannot_be_replaced_on_rerun(self):
        self.run_smoke()
        result = self.run_smoke(tokens=[TOKENS[1]])
        self.assertEqual(result['category'], 'durable_task_stopped')
        self.assertEqual(result['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
    def test_changed_fixture_cannot_create_another_source_claim_on_same_run(self):
        self.run_smoke()
        with patch.object(smoke, 'synthetic_pdf', return_value=smoke.synthetic_pdf() + b'changed'):
            result = self.run_smoke()
        self.assertEqual(result['category'], 'run_source_binding_changed')
        self.assertEqual(len(self.http.posts), 1)
        self.assertEqual(len(self.batches()), 1)
    def test_changed_options_cannot_repost_the_same_run(self):
        self.run_smoke()
        with patch.object(smoke, 'OPTIONS', dict(smoke.OPTIONS, language='ch')):
            result = self.run_smoke()
        self.assertEqual(result['category'], 'run_source_binding_changed')
        self.assertEqual(len(self.http.posts), 1)
        self.assertEqual(len(self.batches()), 1)
    def test_new_run_has_its_own_one_source_identity(self):
        self.run_smoke()
        self.run_smoke(run_id='123457')
        self.assertEqual(len(self.http.posts), 2)
        self.assertEqual(len(self.batches()), 2)
        self.assertEqual({batch['files'][0]['source'] for batch in self.batches()},
                         {'mineru-api-smoke-123456.pdf', 'mineru-api-smoke-123457.pdf'})
    def test_tls_download_failure_preserves_terminal_task_and_rerun_gets_original(self):
        class TLSFailure:
            def open(self, *args, **kwargs):
                raise urllib.error.URLError(ssl.SSLCertVerificationError('certificate invalid'))
        with patch.object(result_helpers.urllib.request, 'build_opener', return_value=TLSFailure()) as opening:
            result = self.run_smoke(downloader=result_helpers.download_once)
        self.assertTrue(result['network_stop'])
        self.assertEqual(result['stage'], 'download')
        self.assertFalse(result['marker_verified'])
        self.assertEqual(opening.call_count, 1)
        self.assertEqual(self.batches()[0]['state'], 'terminal')
        recovered = self.run_smoke()
        self.assertEqual(recovered['status'], 'passed')
        self.assertEqual(recovered['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
    def test_expired_certificate_is_distinct_without_insecure_retry(self):
        expired = ssl.SSLCertVerificationError('certificate expired')
        expired.verify_code = 10
        class TLSFailure:
            def open(self, *args, **kwargs):
                raise urllib.error.URLError(expired)
        with patch.object(result_helpers.urllib.request, 'build_opener', return_value=TLSFailure()) as opening:
            result = self.run_smoke(downloader=result_helpers.download_once)
        self.assertEqual(result['category'], 'tls_certificate_expired')
        self.assertTrue(result['network_stop'])
        self.assertEqual(opening.call_count, 1)
        self.assertEqual(opening.call_args.args, (result_helpers.NoRedirect,))
        self.assertEqual(result['provider_posts'], 1)
    def test_result_redirect_is_rejected_and_terminal_task_is_retained(self):
        class Redirect:
            def open(self, *args, **kwargs):
                raise urllib.error.HTTPError('https://private.invalid?secret=yes', 302, 'redirect', {}, None)
        with patch.object(result_helpers.urllib.request, 'build_opener', return_value=Redirect()):
            result = self.run_smoke(downloader=result_helpers.download_once)
        self.assertEqual(result['category'], 'result_http')
        self.assertNotIn('private.invalid', json.dumps(result))
        self.assertEqual(self.batches()[0]['state'], 'terminal')
        again = self.run_smoke()
        self.assertEqual(again['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
    def test_large_result_is_rejected_before_unzip_and_no_repost(self):
        result = self.run_smoke(downloader=lambda _: b'x' * (smoke.MAX_RESULT + 1))
        self.assertEqual(result['category'], 'result_size')
        self.assertFalse(result['download']['complete_zip_verified'])
        again = self.run_smoke()
        self.assertEqual(again['provider_posts'], 0)
        self.assertEqual(len(self.http.posts), 1)
    def test_malformed_zip_path_and_missing_marker_fail_without_repost(self):
        for bad, category in ((b'not a zip', 'zip_integrity'), (zipped(name='../full.md'), 'zip_path'),
                              (zipped(text='42.75 125.50 168.25'), 'marker_missing'),
                              (zipped(text=smoke.MARKER + ' 42.75 125.50'), 'numeric_evidence_missing')):
            with self.subTest(category=category):
                result = self.run_smoke(downloader=lambda _, raw=bad: raw)
                self.assertEqual(result['category'], category)
                self.assertFalse(result['marker_verified'])
        self.assertEqual(len(self.http.posts), 1)
    def test_pending_and_failed_parses_never_download_results(self):
        for mode in ('pending', 'failed'):
            with self.subTest(mode=mode), patch.object(self.http, 'mode', mode):
                with patch.object(smoke, 'download_once') as download:
                    result = self.run_smoke(downloader=download)
                self.assertEqual(result['status'], mode)
                download.assert_not_called()
                self.assertFalse(result['marker_verified'])
        self.assertEqual(len(self.http.posts), 1)
    def test_api_redirects_are_refused_before_credentials_can_be_forwarded(self):
        response = Response(302, {})
        calls = []
        def request(method, url, **kwargs):
            calls.append(kwargs)
            return response
        http = smoke.NoRedirectHTTP(request)
        with self.assertRaises(durable.LedgerError):
            http.post('https://mineru.net/api', headers={'Authorization': 'Bearer private'})
        self.assertEqual(len(calls), 1)
        self.assertFalse(calls[0]['allow_redirects'])
        self.assertTrue(response.closed)
    def test_main_guard_blocks_local_network_and_nonmain_dispatch(self):
        with patch.dict(smoke.os.environ, {}, clear=True), patch.object(smoke, 'cloud_store') as store:
            with self.assertRaises(SystemExit): smoke.main()
            store.assert_not_called()
    def test_run_identity_and_credentials_are_bounded(self):
        with self.assertRaises(smoke.SmokeError): self.run_smoke(run_id='123; echo private')
        self.assertEqual(smoke.credentials({'MINER_U':'same', 'MINER_U_2':'same', 'MINER_U_3':'new'}),
                         [('MINER_U','same'), ('MINER_U_3','new')])
        with self.assertRaises(smoke.SmokeError): smoke.credentials({})

    def cloud_storage(self):
        client = MemoryR2()
        self.store = durable.R2Store(smoke.SCOPE, client=client, bucket='private-smoke')
        return client

    def test_r2_result_is_immutable_smoke_scoped_and_replay_never_downloads_or_posts(self):
        client = self.cloud_storage()
        downloads = []
        def download(url): downloads.append(url); return zipped()
        first = self.run_smoke(downloader=download)
        self.assertEqual(first['status'], 'passed')
        self.assertEqual(first['result_cache'], {'enabled': True, 'durable_readback': True, 'initial_hit': False,
            'replay_hit': True, 'replay_provider_posts': 0, 'replay_result_downloads': 0})
        self.assertEqual((len(downloads), len(self.http.posts), len(self.http.polls)), (1, 1, 2))
        objects = {k: v for k, v in client.objects.items() if k.startswith(smoke.CACHE_PREFIX + '/')}
        self.assertEqual(len(objects), 2)
        receipt = json.loads(next(v['Body'] for k, v in objects.items() if k.endswith('receipt.json')))
        self.assertEqual(receipt['source_binding']['scope'], smoke.SCOPE)
        self.assertEqual(receipt['policy'], smoke.CACHE_POLICY)
        self.assertNotIn('dropbox', json.dumps(receipt))
        self.assertNotIn('full_zip_url', receipt)
        for operation in client.puts:
            if operation['Key'].startswith(smoke.CACHE_PREFIX + '/'):
                self.assertEqual(operation['IfNoneMatch'], '*')
        def no_cdn(url): self.fail('Cached smoke must not GET CDN')
        second = self.run_smoke(downloader=no_cdn)
        self.assertEqual(second['status'], 'passed')
        self.assertEqual(second['provider_posts'], 0)
        self.assertTrue(second['result_cache']['initial_hit'])
        self.assertEqual((len(self.http.posts), len(self.http.polls)), (1, 4))
        self.assertEqual(first['hashes'], second['hashes'])
        self.assertEqual(objects, {k: v for k, v in client.objects.items() if k.startswith(smoke.CACHE_PREFIX + '/')})

    def test_shared_transport_strict_then_pin_persists_authentication_and_replays_from_r2(self):
        import mineru_daily_result_transport as transport
        from test_mineru_pinned_result_transport import authentication
        client = self.cloud_storage()
        self.http.result_url = 'https://cdn-mineru.openxlab.org.cn/pdf/synthetic.zip'
        now = transport.utc_now()
        auth = authentication(); auth.pop('cutoff_utc')
        auth.update(schema_version=1, policy=transport.POLICY, issued_at_utc=now.isoformat(),
                    expires_at_utc=(now + timedelta(minutes=15)).isoformat(), repository='example/research',
                    workflow_path=smoke.WORKFLOW, event='workflow_dispatch')
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
               'GITHUB_REPOSITORY': 'example/research',
               'GITHUB_WORKFLOW_REF': 'example/research/' + smoke.WORKFLOW + '@refs/heads/main'}
        calls = []
        def strict(url): calls.append('strict'); raise result_helpers.NetworkStop('tls_certificate_expired')
        def pinned(url): calls.append('pin'); return zipped()
        with patch.dict(smoke.os.environ, env, clear=True), \
             patch.object(transport, '_prepare_daily_authentication', return_value=auth) as prepare, \
             patch.object(transport, 'DailyPinnedResultTransport', return_value=pinned):
            first = self.run_smoke(downloader=strict, result_downloader=transport.download_result)
        self.assertEqual(first['status'], 'passed')
        self.assertEqual(calls, ['strict', 'pin'])
        prepare.assert_called_once()
        self.assertEqual(first['result_authentication']['auth_mode'], 'exact_leaf_pin')
        self.assertIs(first['result_authentication']['pki_verified_now'], False)
        self.assertEqual(first['provider_posts'], 1)
        self.assertTrue(first['result_cache']['replay_hit'])
        records = [json.loads(v['Body']) for k, v in client.objects.items()
                   if k.startswith(smoke.CACHE_PREFIX + '/') and k.endswith('receipt.json')]
        self.assertEqual(records[0]['authentication'], auth)
        # Stored authentication is historical evidence, not a new lease.
        with patch.object(transport, 'validate_daily_authentication', side_effect=AssertionError('No new live auth')):
            again = self.run_smoke(downloader=lambda _: self.fail('No new CDN GET'), result_downloader=transport.download_result)
        self.assertEqual(again['status'], 'passed')
        self.assertEqual(again['provider_posts'], 0)
        public = json.dumps(first)
        for private in ('private-key', 'results.invalid', 'signed=', smoke.MARKER, 'single-accepted-task'):
            self.assertNotIn(private, public)

    def test_bad_marker_or_numeric_result_never_enters_result_cache(self):
        client = self.cloud_storage()
        for raw in (b'not ZIP', zipped(text='42.75 125.50 168.25'), zipped(text=smoke.MARKER + ' 42.75')):
            with self.subTest(raw_length=len(raw)):
                result = self.run_smoke(downloader=lambda _: raw)
                self.assertEqual(result['status'], 'failed')
                self.assertFalse(result['result_cache']['durable_readback'])
                self.assertFalse(any(k.startswith(smoke.CACHE_PREFIX + '/') for k in client.objects))
        self.assertEqual(len(self.http.posts), 1)

    def test_corrupted_cache_receipt_or_blob_stops_without_a_new_download(self):
        client = self.cloud_storage()
        self.assertEqual(self.run_smoke()['status'], 'passed')
        original = copy.deepcopy(client.objects)
        receipt_key = next(k for k in client.objects if k.startswith(smoke.CACHE_PREFIX + '/') and k.endswith('receipt.json'))
        blob_key = next(k for k in client.objects if k.startswith(smoke.CACHE_PREFIX + '/') and k.endswith('.zip'))
        for kind in ('source-scope', 'task', 'markdown', 'blob', 'receipt-hash'):
            client.objects = copy.deepcopy(original)
            if kind == 'blob': client.objects[blob_key]['Body'] += b'changed'
            elif kind == 'receipt-hash': client.objects[receipt_key]['Metadata']['sha256'] = 'a' * 64
            else:
                receipt = json.loads(client.objects[receipt_key]['Body'])
                if kind == 'source-scope': receipt['source_binding']['scope'] = 'dropbox'
                elif kind == 'task': receipt['lineage']['batch_id'] = 'another-task'
                else: receipt['markdown_sha256'] = 'a' * 64
                raw = durable.encoded(receipt)
                client.objects[receipt_key]['Body'] = raw
                client.objects[receipt_key]['Metadata']['sha256'] = durable.digest(raw)
            with self.subTest(kind=kind):
                result = self.run_smoke(downloader=lambda _: self.fail('Bad cache must not redownload'))
                self.assertEqual(result['status'], 'failed')
                self.assertFalse(result['result_cache']['replay_hit'])
                self.assertEqual(result['provider_posts'], 0)

    def test_r2_write_readback_failure_never_claims_durable_or_cache_replay_success(self):
        client = self.cloud_storage()
        def corrupt(key, operation):
            if key.startswith(smoke.CACHE_PREFIX + '/') and key.endswith('.zip'):
                client.objects[key]['Body'] += b'changed'
        client.after_put = corrupt
        result = self.run_smoke()
        self.assertEqual(result['status'], 'failed')
        self.assertEqual(result['category'], 'result_cache_contract')
        self.assertFalse(result['marker_verified'])
        self.assertFalse(result['result_cache']['durable_readback'])
        self.assertFalse(result['result_cache']['replay_hit'])
        self.assertEqual(len([k for k in client.objects if k.startswith(smoke.CACHE_PREFIX + '/')]), 1)
        self.assertEqual(len(self.http.posts), 1)

    def test_replay_rechecks_current_original_task_before_using_a_valid_cache(self):
        self.cloud_storage()
        original = self.http.get
        def fail_second_poll(url, **kwargs):
            if self.http.polls: self.http.mode = 'failed'
            return original(url, **kwargs)
        with patch.object(self.http, 'get', side_effect=fail_second_poll):
            result = self.run_smoke()
        self.assertEqual(result['category'], 'result_cache_replay_task')
        self.assertTrue(result['result_cache']['durable_readback'])
        self.assertFalse(result['result_cache']['replay_hit'])
        self.assertEqual(len(self.http.posts), 1)

    def test_main_passes_shared_cloud_result_transport_and_keeps_public_summary_only(self):
        import mineru_daily_result_transport as transport
        env = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch', 'GITHUB_REF': 'refs/heads/main',
               'GITHUB_REPOSITORY': 'example/research', 'GITHUB_RUN_ID': '123456', 'MINER_U': 'private-key',
               'GITHUB_WORKFLOW_REF': 'example/research/' + smoke.WORKFLOW + '@refs/heads/main',
               'RUNNER_TEMP': str(self.root)}
        passed = {'schema_version': 1, 'status': 'passed', 'marker_verified': True}
        with patch.dict(smoke.os.environ, env, clear=True), patch.object(smoke, 'cloud_store'), \
             patch.object(smoke, 'run_smoke', return_value=passed) as run, patch('builtins.print'):
            self.assertEqual(smoke.main(), 0)
        self.assertIs(run.call_args.kwargs['result_downloader'], transport.download_result)
        self.assertEqual(json.loads((self.root / 'mineru-api-smoke-summary.json').read_text()), passed)


if __name__ == '__main__':
    unittest.main(verbosity=2)
