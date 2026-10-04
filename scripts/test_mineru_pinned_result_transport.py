"""Offline exact-leaf, historical-chain, cutoff and bounded-download contracts."""
from datetime import timedelta
import copy
import io
import json
from pathlib import Path
import ssl
import subprocess
import unittest
from unittest.mock import Mock, patch

import mineru_pinned_result_transport as p
from test_probe_mineru_result_tls import public_pem, metadata_output, handshake

ENV = {'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
       'GITHUB_REF': 'refs/heads/main', 'GITHUB_REPOSITORY': 'example/research',
       'GITHUB_WORKFLOW_REF': 'example/research/' + p.WORKFLOW + '@refs/heads/main'}
NOW = p.CUTOFF - timedelta(hours=1)


def authentication():
    return {'auth_mode': p.AUTH_MODE, 'pki_verified_now': False, 'historical_chain_verified': True,
            'historical_ca_checks': 2, 'leaf_sha256': p.LEAF_SHA256,
            'leaf_not_after_utc': p.LEAF_EXPIRY.isoformat(), 'cutoff_utc': p.CUTOFF.isoformat(),
            'peer_chain_sha256': [p.LEAF_SHA256, 'a' * 64], 'preflight_tls_connections': 1,
            'preflight_http_requests': 0}


class Response:
    def __init__(self, payload=b'complete bytes', status=200, headers=None):
        self.body, self.status, self.headers = io.BytesIO(payload), status, headers or {}
        self.closed = False

    def read(self, amount, **kwargs):
        assert kwargs == {'decode_content': False}
        return self.body.read(amount)

    def close(self):
        self.closed = True


class Pool:
    def __init__(self, response):
        self.response, self.calls, self.closed = response, [], False

    def request(self, *args, **kwargs):
        self.calls.append((args, kwargs))
        return self.response

    def close(self):
        self.closed = True


class AuthenticationTests(unittest.TestCase):
    def setup_runner(self, *, code=10, depth=0, exit_code=1, historical_exit=0, count=2):
        leaf, leaf_hash = public_pem('fixed leaf')
        intermediate, _ = public_pem('fixed intermediate')
        certs = [leaf, intermediate][:count] + [intermediate] * max(0, count - 2)
        calls = []

        def runner(command, **kwargs):
            calls.append((command, kwargs))
            if command[:2] == ['openssl', 's_client']:
                return handshake(certs, code=code, depth=depth, exit_code=exit_code)
            if command[:2] == ['openssl', 'x509']:
                output = metadata_output(kwargs['input'], not_after='Oct  2 23:59:59 2026 GMT'
                                         if kwargs['input'] == leaf else 'Nov  2 23:59:59 2027 GMT')
                return subprocess.CompletedProcess(command, 0, output, b'PRIVATE parser stderr')
            if command[:2] == ['openssl', 'verify']:
                self.assertTrue(Path(command[-1]).read_bytes().startswith(b'-----BEGIN CERTIFICATE'))
                return subprocess.CompletedProcess(command, historical_exit, b'PRIVATE parser stdout', b'PRIVATE stderr')
            raise AssertionError(command)

        return leaf_hash, runner, calls

    def test_public_fixed_identity_and_deadline_cannot_be_runtime_options(self):
        self.assertEqual(p.LEAF_SHA256, '12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3')
        self.assertEqual(p.HOST, 'cdn-mineru.openxlab.org.cn')
        self.assertEqual(p.CUTOFF.isoformat(), '2026-10-04T23:59:59+00:00')
        self.assertEqual(p.CUTOFF - p.LEAF_EXPIRY, timedelta(hours=48))

    def test_one_strict_no_http_handshake_then_two_offline_chain_and_san_checks(self):
        leaf_hash, runner, calls = self.setup_runner()
        with patch.object(p, 'LEAF_SHA256', leaf_hash):
            result = p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)
        commands = [row[0] for row in calls]
        self.assertEqual(sum(command[1] == 's_client' for command in commands), 1)
        capture = commands[0]
        self.assertIn('-verify_return_error', capture)
        self.assertIn('-verify_hostname', capture)
        self.assertIn('-servername', capture)
        self.assertEqual(calls[0][1]['input'], b'')
        verifies = [command for command in commands if command[1] == 'verify']
        self.assertEqual(len(verifies), 2)
        for command in verifies:
            self.assertEqual(command[command.index('-attime') + 1], str(int(p.LEAF_EXPIRY.timestamp()) - 1))
            self.assertEqual(command[command.index('-purpose') + 1], 'sslserver')
            self.assertEqual(command[command.index('-verify_hostname') + 1], p.HOST)
            self.assertNotIn('-no_check_time', command)
        self.assertNotIn('-CAfile', verifies[0])
        self.assertIn('-CAfile', verifies[1])
        self.assertIn('-no-CApath', verifies[1])
        self.assertIn('-no-CAstore', verifies[1])
        self.assertFalse(result['pki_verified_now'])
        self.assertTrue(result['historical_chain_verified'])
        self.assertNotIn('PRIVATE', json.dumps(result))
        self.assertNotIn('CERTIFICATE', json.dumps(result))

    def test_wrong_cloud_event_branch_workflow_or_cutoff_never_attempts_a_connection(self):
        for change in ({'GITHUB_EVENT_NAME': 'schedule'}, {'GITHUB_REF': 'refs/heads/feature'},
                       {'GITHUB_ACTIONS': 'false'}, {'GITHUB_WORKFLOW_REF': 'other'}, {'GITHUB_REPOSITORY': ''}):
            runner = Mock()
            with self.subTest(change=change), self.assertRaises(p.PinnedTransportError):
                p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV | change)
            runner.assert_not_called()
        runner = Mock()
        with self.assertRaises(p.PinnedTransportError):
            p.prepare_authentication(runner=runner, now=lambda: p.CUTOFF, env=ENV)
        runner.assert_not_called()

    def test_other_verification_failures_and_valid_pki_never_enter_pin_mode(self):
        for values in ({'code': 62}, {'depth': 1}, {'code': 0, 'exit_code': 0}):
            _, runner, calls = self.setup_runner(**values)
            with self.subTest(values=values), self.assertRaisesRegex(p.PinnedTransportError, 'expected_leaf_expiry'):
                p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)
            self.assertEqual(len(calls), 1)

    def test_exact_der_pin_and_bounded_complete_chain_are_mandatory(self):
        _, runner, _ = self.setup_runner()
        with self.assertRaisesRegex(p.PinnedTransportError, 'fingerprint_mismatch'):
            p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)
        for count in (1, 9):
            _, runner, _ = self.setup_runner(count=count)
            with self.assertRaisesRegex(p.PinnedTransportError, 'complete_peer_chain'):
                p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)

    def test_failed_historical_signature_or_san_check_is_closed(self):
        leaf_hash, runner, calls = self.setup_runner(historical_exit=1)
        with patch.object(p, 'LEAF_SHA256', leaf_hash), self.assertRaisesRegex(p.PinnedTransportError, 'historical_chain_or_hostname'):
            p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)
        self.assertEqual(sum(command[0][1] == 'verify' for command in calls), 1)

    def test_process_output_bounds_and_raw_failures_are_not_published(self):
        runner = Mock(return_value=subprocess.CompletedProcess([], 1, b'x' * 262145, b'PRIVATE'))
        with self.assertRaisesRegex(p.PinnedTransportError, '^authentication_preflight_failed$'):
            p.prepare_authentication(runner=runner, now=lambda: NOW, env=ENV)

    def test_authentication_has_a_strict_numeric_and_hash_whitelist(self):
        for change in ({'url': 'https://PRIVATE'}, {'pki_verified_now': True}, {'historical_ca_checks': True},
                       {'peer_chain_sha256': [p.LEAF_SHA256, 'PRIVATE']}, {'leaf_sha256': 'a' * 64},
                       {'cutoff_utc': '2026-10-05T23:59:59+00:00'}):
            with self.subTest(change=change), self.assertRaises(p.PinnedTransportError):
                p.verified_authentication(authentication() | change)


class DownloadTests(unittest.TestCase):
    def make(self, response=None, now=lambda: NOW):
        response = response or Response()
        pool = Pool(response)
        factory = Mock(return_value=pool)
        transport = p.PinnedResultTransport(authentication(), now=now, pool_factory=factory)
        return transport, factory, pool, response

    def test_dedicated_pool_always_pins_exact_leaf_before_get_and_never_retries_redirects_or_decodes(self):
        transport, factory, pool, response = self.make()
        payload = transport('https://' + p.HOST + '/private-result.zip?signed=PRIVATE')
        self.assertEqual(payload, b'complete bytes')
        self.assertEqual(factory.call_args.args, (p.HOST,))
        options = factory.call_args.kwargs
        self.assertEqual(options['assert_fingerprint'], p.LEAF_SHA256)
        self.assertEqual(options['cert_reqs'], 'CERT_NONE')
        self.assertEqual(options['port'], 443)
        self.assertEqual(options['ssl_minimum_version'], ssl.TLSVersion.TLSv1_2)
        self.assertIs(options['retries'], False)
        self.assertEqual(pool.calls[0][0], ('GET', '/private-result.zip?signed=PRIVATE'))
        self.assertEqual(pool.calls[0][1], {'headers': {'Accept-Encoding': 'identity'}, 'redirect': False,
                                         'retries': False, 'preload_content': False, 'decode_content': False})
        self.assertTrue(pool.closed)
        self.assertTrue(response.closed)
        self.assertEqual(transport.result_gets, 1)

    def test_arbitrary_origin_credentials_port_ip_http_and_redirect_requests_are_rejected_before_pool(self):
        for url in ('http://' + p.HOST + '/x', 'https://other.invalid/x', 'https://' + p.HOST + ':8443/x',
                    'https://' + p.HOST + '.attacker.invalid/x', 'https://user:secret@' + p.HOST + '/x',
                    'https://127.0.0.1/x', 'https://' + p.HOST + '/x#fragment'):
            transport, factory, _, _ = self.make()
            with self.subTest(url=url), self.assertRaises(ValueError):
                transport(url)
            factory.assert_not_called()

    def test_no_connection_or_read_after_fixed_cutoff(self):
        transport, factory, _, _ = self.make(now=lambda: p.CUTOFF)
        with self.assertRaises(p.PinnedTransportError):
            transport('https://' + p.HOST + '/x')
        factory.assert_not_called()
        times = iter([NOW, NOW, NOW, p.CUTOFF])
        transport, _, pool, response = self.make(now=lambda: next(times))
        with self.assertRaises(p.PinnedTransportError):
            transport('https://' + p.HOST + '/x')
        self.assertEqual(response.body.tell(), 0)
        self.assertTrue(pool.closed)

    def test_connect_extension_checks_cutoff_before_and_after_library_handshake(self):
        transport, _, pool, _ = self.make()
        transport('https://' + p.HOST + '/x')
        connection = pool.ConnectionCls(p.HOST)
        with patch.object(p.HTTPSConnection, 'connect') as connect, patch.object(p, 'require_before_cutoff') as check:
            connection.connect()
        connect.assert_called_once()
        self.assertEqual(check.call_count, 2)

    def test_redirect_http_error_encoding_truncation_and_size_are_closed(self):
        for response in (Response(status=302), Response(status=403), Response(headers={'Content-Encoding': 'gzip'}),
                         Response(headers={'Content-Length': '999'}), Response(headers={'Content-Length': str(p.MAX_ZIP + 1)}),
                         Response(headers={'Content-Length': 'not a number'}), Response(payload=b'')):
            transport, _, pool, _ = self.make(response)
            with self.subTest(response=response.headers), self.assertRaises(p.PinnedTransportError):
                transport('https://' + p.HOST + '/x')
            self.assertEqual(len(pool.calls), 1)
            self.assertTrue(response.closed)

    def test_library_fingerprint_failure_is_never_retried_or_exposed(self):
        transport, _, pool, _ = self.make()
        pool.request = Mock(side_effect=ssl.SSLError('PRIVATE URL secret mismatch'))
        with self.assertRaisesRegex(p.PinnedTransportError, '^pinned_result_transport_failed$'):
            transport('https://' + p.HOST + '/x')
        self.assertEqual(pool.request.call_count, 1)


if __name__ == '__main__':
    unittest.main()
