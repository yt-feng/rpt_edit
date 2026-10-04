"""Offline smoke regressions; fake HTTP and local ledger only."""
from __future__ import annotations
import io
import json
import re
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
                 **({'full_zip_url': 'https://results.invalid/private?signed=secret'} if self.mode == 'done' else {})}
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
    def run_smoke(self, *, tokens=TOKENS, downloader=lambda _: zipped(), run_id='123456'):
        return smoke.run_smoke(run_id, self.store, durable.Provider(self.http, smoke.ENDPOINT), tokens,
                               downloader=downloader, clock=self.clock.time, sleep=self.clock.sleep)
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


if __name__ == '__main__':
    unittest.main(verbosity=2)
