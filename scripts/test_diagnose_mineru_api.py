#!/usr/bin/env python3
"""Mock-only regressions for exact cached bindings and all public exits."""
from __future__ import annotations

import base64
import copy
from contextlib import redirect_stderr, redirect_stdout
import io
import json
from pathlib import Path
import ssl
import tempfile
import unittest
from unittest.mock import patch
import urllib.error

import diagnose_mineru_api as d
from inspect_legacy_mineru import canonical, classify_response

BATCH = '11111111-1111-4111-8111-111111111111'
SECRET = 'PRIVATE-token-AbCd0123456789-actual-credential'
SIGNED = 'https://cdn-mineru.openxlab.org.cn/private/report.zip?signature=PRIVATE-SIGNED-VALUE'


class Store:
    def __init__(self, bodies):
        self.bodies, self.reads = bodies, []

    def key(self, *parts):
        return '/'.join((d.PREFIX, *parts))

    def _get(self, key, *, maximum):
        self.reads.append(key)
        body = self.bodies[key]
        if len(body) > maximum:
            raise ValueError('private object too large')
        return body

    def _put(self, *args, **kwargs):
        raise AssertionError('No private or canonical writes permitted')


class Response:
    def __init__(self, body=b'', status=200, headers=None):
        self.body, self.status, self.headers = body, status, headers or {}
        self.read_sizes, self.closed = [], False

    def getcode(self):
        return self.status

    def read(self, count):
        self.read_sizes.append(count)
        return self.body[:count]

    def close(self):
        self.closed = True

    def __enter__(self):
        return self

    def __exit__(self, *args):
        self.close()


def fixture(rows=None):
    rows = rows or [{'data_id': 'first', 'state': 'failed', 'err_msg': 'Daily priority page quota exceeded', 'err_code': 'R0010'},
                    {'data_id': 'second', 'state': 'done', 'full_zip_url': SIGNED}]
    batch = {'run_id': '37159099752', 'job_id': '111308763553', 'batch_id': BATCH,
             'credential_slot': 'MINER_U', 'expected_data_ids': [row['data_id'] for row in rows]}
    request = {'schema_version': 1, 'batches': [batch]}
    response = canonical({'code': 0, 'data': {'batch_id': BATCH, 'extract_result': rows}})
    _, private = classify_response(200, response, batch)
    packet = canonical(private)
    input_hash, packet_hash = d.checksum(canonical(request)), d.checksum(packet)
    relative = f'37160198464-1/{input_hash}/{BATCH}-{packet_hash}.json'
    receipt = {'schema_version': 1, 'policy': 'legacy-provider-inspection-only-v1',
               'producer': {'run_id': '37160198464', 'attempt': '1', 'sha': 'a' * 40},
               'input': request, 'input_canonical_sha256': input_hash,
               'objects': [{'batch_id': BATCH, 'object': relative, 'sha256': packet_hash, 'bytes': len(packet)}],
               'original_source_bytes_proven': False, 'historical_token_fingerprint_proven': False,
               'canonical_task_admission': False}
    raw = canonical(receipt)
    identity = {'inspection_run_id': '37160198464', 'inspection_attempt': '1',
                'input_sha256': input_hash, 'receipt_sha256': d.checksum(raw)}
    store = Store({f'{d.PREFIX}/{relative}': packet,
                   f'{d.PREFIX}/37160198464-1/{input_hash}/receipt-{identity["receipt_sha256"]}.json': raw})
    return identity, store, receipt


class DiagnosticTests(unittest.TestCase):
    def setUp(self):
        self.identity, self.store, self.receipt = fixture()
        self.env = {slot: SECRET + str(index) for index, slot in enumerate(d.key_monitor.SLOT_NAMES)}
        self.calls, self.responses = [], []

    def opener(self, request, timeout):
        method, url = request.get_method(), request.full_url
        self.calls.append((method, url))
        self.assertIn(method, {'GET', 'HEAD'}, 'No provider mutation is authorized')
        if d.key_monitor.PROBE_BATCH_ID in url:
            self.assertEqual(url, 'https://mineru.net/api/v4/extract-results/batch/' + d.key_monitor.PROBE_BATCH_ID)
            response = Response(canonical({'code': 'A0204', 'msg': 'No such synthetic task'}))
        elif method == 'HEAD':
            self.assertEqual(url, SIGNED)
            response = Response(b'must never read HEAD body', headers={'Content-Length': '12345'})
        else:
            self.assertEqual(url, SIGNED)
            self.assertEqual(request.get_header('Range'), 'bytes=0-3')
            self.assertIsNone(request.get_header('Authorization'))
            response = Response(b'PK\x03\x04PRIVATE-MORE-BYTES', status=206, headers={'Content-Length': '4'})
        self.responses.append(response)
        return response

    def test_exact_snapshot_then_four_auth_gets_and_four_zip_bytes_without_task_or_email(self):
        report = d.diagnose(self.identity, self.store, self.env, opener=self.opener)
        self.assertEqual(len(self.store.reads), 2)
        self.assertEqual([method for method, _ in self.calls], ['GET'] * 4 + ['HEAD', 'GET'])
        self.assertEqual(report['historical_tasks']['failures'], [{'reason': 'priority_quota', 'code': 'R0010', 'reason_known': True, 'count': 1}])
        self.assertEqual(report['authentication']['configured_count'], 4)
        self.assertTrue(all(slot['probe_state'] == 'valid' for slot in report['authentication']['slots']))
        self.assertFalse(report['authentication']['quota_or_parse_capacity_verified'])
        result = report['result_download']
        self.assertEqual(result['status'], 'zip_prefix_readable')
        self.assertEqual(result['bytes_read'], 4)
        self.assertFalse(result['full_zip_verified'])
        self.assertEqual(self.responses[-2].read_sizes, [])
        self.assertEqual(self.responses[-1].read_sizes, [4])
        self.assertTrue(all(response.closed for response in self.responses))
        self.assertEqual((report['provider_posts'], report['new_submissions'], report['canonical_ledger_writes'], report['emails_sent']), (0, 0, 0, 0))
        self.assertFalse(report['historical_tasks']['original_source_bytes_proven'])

    def test_invalid_identity_and_snapshot_corruption_stop_before_live_probes(self):
        for mutation in ('path', 'hash', 'attempt', 'receipt_bytes', 'object_bytes'):
            identity, store, _ = fixture()
            if mutation == 'path': identity['inspection_run_id'] = '../secret'
            elif mutation == 'hash': identity['input_sha256'] = 'not-a-hash'
            elif mutation == 'attempt': identity['inspection_attempt'] = True
            elif mutation == 'receipt_bytes':
                key = next(key for key in store.bodies if '/receipt-' in key)
                store.bodies[key] += b'changed'
            else:
                key = next(key for key in store.bodies if '/receipt-' not in key)
                store.bodies[key] += b'changed'
            with self.subTest(mutation=mutation), self.assertRaises(d.DiagnosticError):
                d.diagnose(identity, store, self.env, opener=self.opener)
            self.assertEqual(self.calls, [])

    def test_forged_object_path_or_membership_is_rejected_even_with_new_receipt_hash(self):
        for mutation in ('path', 'missing', 'duplicate', 'producer'):
            identity, store, receipt = fixture()
            if mutation == 'path': receipt['objects'][0]['object'] = '../arbitrary-private-object'
            elif mutation == 'missing': receipt['objects'] = []
            elif mutation == 'duplicate': receipt['objects'].append(copy.deepcopy(receipt['objects'][0]))
            else: receipt['producer']['attempt'] = '2'
            raw = canonical(receipt)
            identity['receipt_sha256'] = d.checksum(raw)
            store.bodies[store.key('37160198464-1', identity['input_sha256'], 'receipt-' + identity['receipt_sha256'] + '.json')] = raw
            with self.subTest(mutation=mutation), self.assertRaises(d.DiagnosticError):
                d.diagnose(identity, store, self.env, opener=self.opener)
            self.assertEqual(self.calls, [])

    def test_duplicate_json_keys_are_rejected_at_receipt_object_and_raw_provider_boundary(self):
        for layer in ('receipt', 'object', 'provider'):
            identity, store, receipt = fixture()
            if layer != 'receipt':
                item = receipt['objects'][0]
                packet = json.loads(store.bodies[store.key(*item['object'].split('/'))])
                if layer == 'provider':
                    original = base64.b64decode(packet['raw_response_base64'])
                    raw_response = b'{"code":401,' + original[1:]
                    packet['raw_response_base64'] = base64.b64encode(raw_response).decode()
                    packet['response_sha256'] = d.checksum(raw_response)
                    raw_packet = canonical(packet)
                else:
                    raw_packet = b'{"http_status":401,' + canonical(packet)[1:]
                digest = d.checksum(raw_packet)
                item.update(sha256=digest, bytes=len(raw_packet),
                            object=f'37160198464-1/{identity["input_sha256"]}/{BATCH}-{digest}.json')
                store.bodies[store.key(*item['object'].split('/'))] = raw_packet
            raw = canonical(receipt)
            if layer == 'receipt':
                raw = b'{"schema_version":99,' + raw[1:]
            identity['receipt_sha256'] = d.checksum(raw)
            store.bodies[store.key('37160198464-1', identity['input_sha256'], 'receipt-' + identity['receipt_sha256'] + '.json')] = raw
            with self.subTest(layer=layer), self.assertRaisesRegex(d.DiagnosticError, 'object_duplicate_keys'):
                d.diagnose(identity, store, self.env, opener=self.opener)
            self.assertEqual(self.calls, [])

    def test_official_negative_codes_are_public_without_guessing_message_reason(self):
        for value in (-60007, '-60007'):
            self.assertEqual(d.public_code(value), {'code': -60007, 'documented_code_reason': 'model_service_unavailable'})
        for value in (-123456, '-60007 PRIVATE', ' -60007'):
            self.assertIsNone(d.public_code(value)['code'])
            self.assertIn('code_sha256', d.public_code(value))
        rows = [{'data_id': 'first', 'state': 'failed', 'err_msg': 'Unclassified provider response', 'err_code': '-60007'},
                {'data_id': 'second', 'state': 'done', 'full_zip_url': SIGNED}]
        identity, store, _ = fixture(rows)
        failure = d.diagnose(identity, store, self.env, opener=self.opener)['historical_tasks']['failures'][0]
        self.assertEqual(failure['reason'], 'other_provider_failure')
        self.assertFalse(failure['reason_known'])
        self.assertEqual(failure['documented_code_reason'], 'model_service_unavailable')

    def test_unknown_provider_strings_and_encoded_secrets_cannot_cross_public_exits(self):
        variants = [SECRET, 'Bearer ' + SECRET, 'api_key=' + SECRET, 'person@private.example',
                    SIGNED, 'https://user:password@private.example/file?signature=VALUE', '/Users/private/account/config',
                    base64.b64encode(SECRET.encode()).decode(), SECRET.encode().hex(),
                    d.urllib.parse.quote(d.urllib.parse.quote(SECRET, safe=''), safe=''),
                    'eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhY2NvdW50In0.signatureSECRET']
        for secret in variants:
            rows = [{'data_id': 'first', 'state': 'failed', 'err_msg': secret, 'error': secret,
                     'err_code': secret, 'file_name': secret},
                    {'data_id': 'second', 'state': 'done', 'full_zip_url': SIGNED}]
            identity, store, _ = fixture(rows)
            report = d.diagnose(identity, store, {'MINER_U': SECRET}, opener=self.opener, stream_probe=False)
            encoded = json.dumps(report)
            with self.subTest(secret=secret[:20]):
                self.assertNotIn(secret, encoded)
                self.assertNotIn(SECRET, encoded)
                self.assertNotIn('raw_response', encoded)
                self.assertNotIn('full_zip_url', encoded)
                self.assertNotIn('file_name', encoded)
                failure = report['historical_tasks']['failures'][0]
                self.assertEqual(set(failure), {'reason', 'code', 'code_sha256', 'reason_known', 'count'})
                self.assertIsNone(failure['code'])

    def test_reason_classification_uses_provider_words_not_current_counter(self):
        for message, category in [('priority page quota exceeded', 'priority_quota'),
                                  ('daily file limit exhausted', 'daily_quota'),
                                  ('Insufficient account balance', 'overall_quota'),
                                  ('Too many requests', 'rate_limit'), ('PDF parsing failed', 'provider_internal'),
                                  ('模型服务暂时不可用', 'provider_unavailable'), ('任务提交队列已满', 'queue_full'),
                                  ('重试次数达到上限', 'provider_retry_limit'),
                                  ('PDF password protected', 'encrypted_pdf'), ('Unknown text', 'other_provider_failure')]:
            self.assertEqual(d.normalize_reason(message), category)

    def test_auth_network_failure_stops_other_keys_and_result_reads(self):
        calls = []
        def failure(request, timeout):
            calls.append(request.get_method())
            raise urllib.error.URLError(SECRET)
        report = d.diagnose(self.identity, self.store, self.env, opener=failure)
        self.assertEqual(calls, ['GET'])
        self.assertTrue(report['network_stop'])
        self.assertEqual(report['result_download']['status'], 'uninspected_after_network_stop')
        self.assertNotIn(SECRET, json.dumps(report))

    def test_auth_http_error_body_is_closed_and_http_protocol_failure_stops(self):
        body = Response(canonical({'code': 'A0204'}))
        def notfound(request, timeout):
            raise urllib.error.HTTPError(request.full_url, 404, SECRET, {}, body)
        report = d.authentication_summary({'MINER_U': SECRET}, notfound)
        self.assertEqual(report['slots'][0]['probe_state'], 'valid')
        self.assertTrue(body.closed)
        self.assertNotIn(SECRET, json.dumps(report))
        def broken(request, timeout):
            raise d.http.client.BadStatusLine(SECRET)
        report = d.diagnose(self.identity, self.store, self.env, opener=broken)
        self.assertTrue(report['network_stop'])
        self.assertNotIn(SECRET, json.dumps(report))

    def test_expired_key_is_reported_without_fallback_post_and_other_keys_checked(self):
        count = 0
        def expiry(request, timeout):
            nonlocal count
            if d.key_monitor.PROBE_BATCH_ID in request.full_url:
                count += 1
                return Response(canonical({'code': 'A0211' if count == 1 else 'A0204'}))
            return self.opener(request, timeout)
        report = d.diagnose(self.identity, self.store, self.env, opener=expiry, stream_probe=False)
        self.assertEqual(count, 4)
        self.assertEqual(report['authentication']['slots'][0]['probe_state'], 'expired')
        self.assertEqual(report['provider_posts'], 0)

    def test_unknown_auth_codes_do_not_prove_authentication(self):
        for code, status, expected in [('A9999', 200, 'unknown'), ('A0200', 200, 'unknown'),
                                       ('-60013', 200, 'unknown'), ('-60012', 200, 'valid'),
                                       ('-60012', 400, 'valid'), ('A0204', 400, 'valid'),
                                       ('A9999', 400, 'unknown'), ('-60013', 400, 'unknown'),
                                       ('A0204', 404, 'valid'), ('A0301', 200, 'valid'),
                                       ('A0204', 302, 'unknown'), ('A0204', 401, 'unknown'),
                                       (0, 200, 'valid'), (None, 204, 'valid'), (0, 404, 'unknown')]:
            def probe(request, timeout):
                self.assertEqual(request.get_method(), 'GET')
                return Response(canonical({'code': code}), status=status)
            report = d.authentication_summary(self.env, probe)
            with self.subTest(code=code, status=status):
                self.assertEqual([slot['probe_state'] for slot in report['slots']], [expected] * 4)
                self.assertFalse(report['quota_or_parse_capacity_verified'])

    def test_head_405_only_proves_tls_and_optional_get_reads_four_bytes(self):
        rows = [{'state': 'done', 'full_zip_url': SIGNED}]
        responses = []
        def head405(request, timeout):
            response = Response(b'PK\x03\x04large-body', status=405 if request.get_method() == 'HEAD' else 200,
                                headers={'Content-Length': '999'})
            responses.append(response)
            return response
        result = d.result_summary(rows, head405, False)
        self.assertEqual(result['status'], 'tls_only')
        self.assertEqual(result['tls'], 'verified')
        self.assertEqual(result['stream_get_requests'], 0)
        self.assertEqual(responses[0].read_sizes, [])
        result = d.result_summary(rows, head405, True)
        self.assertEqual(result['status'], 'zip_prefix_readable')
        self.assertEqual(responses[-1].read_sizes, [4])
        self.assertFalse(result['full_zip_verified'])

    def test_expired_certificate_stops_after_one_head_with_no_verify_bypass(self):
        calls = []
        error = ssl.SSLCertVerificationError(1, SECRET)
        error.verify_code = 10
        def expired(request, timeout):
            calls.append(request.get_method())
            raise urllib.error.URLError(error)
        result = d.result_summary([{'state': 'done', 'full_zip_url': SIGNED}], expired, True)
        self.assertEqual(calls, ['HEAD'])
        self.assertEqual(result['status'], 'certificate_expired')
        self.assertTrue(result['network_stop'])
        self.assertNotIn(SECRET, json.dumps(result))

    def test_stream_protocol_error_closes_response_and_does_not_retry(self):
        responses = []
        class BrokenBody(Response):
            def read(self, count):
                self.read_sizes.append(count)
                raise d.http.client.BadStatusLine(SECRET)
        def broken(request, timeout):
            response = (Response(headers={'Content-Length': '500'}) if request.get_method() == 'HEAD'
                        else BrokenBody(headers={'Content-Length': '500'}))
            responses.append(response)
            return response
        result = d.result_summary([{'state': 'done', 'full_zip_url': SIGNED}], broken, True)
        self.assertEqual(len(responses), 2)
        self.assertTrue(all(response.closed for response in responses))
        self.assertEqual(responses[-1].read_sizes, [4])
        self.assertTrue(result['network_stop'])
        self.assertNotIn(SECRET, json.dumps(result))

    def test_redirect_5xx_oversize_and_nonzip_do_not_trigger_transport_fallback(self):
        for status, length, prefix, expected_calls in ((302, '10', b'PK\x03\x04', 1), (503, '10', b'PK\x03\x04', 1),
                                                       (200, str(d.MAX_ZIP + 1), b'PK\x03\x04', 1), (200, '10', b'HTML', 2)):
            calls = []
            def response(request, timeout):
                calls.append(request.get_method())
                return Response(prefix, status=status, headers={'Content-Length': length})
            result = d.result_summary([{'state': 'done', 'full_zip_url': SIGNED}], response, True)
            self.assertEqual(len(calls), expected_calls)
            self.assertFalse(result['full_zip_verified'])
        self.assertIsNone(d.NoRedirect().redirect_request(None, None, 302, 'redirect', {}, 'https://other.example'))

    def test_unsafe_result_url_does_not_touch_local_or_other_endpoints(self):
        for url in ('http://cdn.example/file', 'https://127.0.0.1/file', 'https://localhost/file', 'https://user:password@cdn.example/file'):
            result = d.result_summary([{'state': 'done', 'full_zip_url': url}], self.opener, True)
            self.assertEqual(result['status'], 'unsafe_result_url')
        self.assertEqual(self.calls, [])

    def test_cloud_only_main_public_stdout_artifact_summary_and_exceptions_are_sanitized(self):
        with tempfile.TemporaryDirectory() as directory:
            env = self.env | {key.upper(): value for key, value in self.identity.items()} | {
                'GITHUB_ACTIONS': 'true', 'GITHUB_REF': 'refs/heads/main', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
                'GITHUB_REPOSITORY': 'owner/repo', 'GITHUB_WORKFLOW_REF': 'owner/repo/' + d.WORKFLOW + '@refs/heads/main',
                'RUNNER_TEMP': directory, 'GITHUB_STEP_SUMMARY': directory + '/summary.md', 'STREAM_PROBE': 'true'}
            out, err = io.StringIO(), io.StringIO()
            with redirect_stdout(out), redirect_stderr(err):
                self.assertEqual(d.main(env, store_factory=lambda: self.store, opener=self.opener), 0)
            artifact = Path(directory, 'mineru-api-diagnostics.json').read_text()
            combined = artifact + Path(env['GITHUB_STEP_SUMMARY']).read_text() + out.getvalue() + err.getvalue()
            for secret in (SECRET, SIGNED, 'PRIVATE-SIGNED-VALUE'):
                self.assertNotIn(secret, combined)
            with redirect_stdout(out), redirect_stderr(err):
                self.assertEqual(d.main(env, store_factory=lambda: (_ for _ in ()).throw(RuntimeError(SECRET))), 1)
            self.assertNotIn(SECRET, out.getvalue() + err.getvalue())
            with patch('socket.create_connection', side_effect=AssertionError('No local network permitted')):
                self.assertEqual(d.main({}), 1)

    def test_workflow_has_no_email_provider_creation_or_write_permissions(self):
        workflow = Path(__file__).resolve().parents[1] / d.WORKFLOW
        text = workflow.read_text()
        self.assertIn('contents: read', text)
        self.assertNotIn('contents: write', text)
        self.assertNotIn('send_portal_ops_alert', text)
        self.assertNotIn('MINERU_LEDGER_BACKEND', text)
        self.assertNotIn('workflow run', text)
        self.assertIn('scripts/diagnose_mineru_api.py', text)
        self.assertIn('--retries 0', text)


if __name__ == '__main__':
    unittest.main(verbosity=2)
