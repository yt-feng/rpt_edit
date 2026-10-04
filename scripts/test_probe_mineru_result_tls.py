#!/usr/bin/env python3
"""Offline strict-client and independent-result regressions."""
import io
import base64
import hashlib
import json
from pathlib import Path
import re
import ssl
import subprocess
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock, patch
import urllib.error

import probe_mineru_result_tls as p

CLOUD_ENV = {
    'GITHUB_ACTIONS': 'true', 'GITHUB_EVENT_NAME': 'workflow_dispatch',
    'GITHUB_REF': 'refs/heads/main', 'GITHUB_REPOSITORY': 'example/research',
    'GITHUB_WORKFLOW_REF': 'example/research/.github/workflows/mineru-result-tls-probe.yml@refs/heads/main',
}


def public_pem(label):
    # The parser subprocess is mocked: these deterministic bytes test binding
    # and ordering without requiring a real certificate, binary, or network.
    der = ('public mock DER ' + label).encode('ascii')
    pem = b'-----BEGIN CERTIFICATE-----\n' + base64.b64encode(der) + b'\n-----END CERTIFICATE-----'
    return pem, hashlib.sha256(der).hexdigest()


def metadata_output(pem, *, not_after='Dec 16 23:59:59 2026 GMT', fingerprint=None):
    digest = hashlib.sha256(ssl.PEM_cert_to_DER_cert(pem.decode('ascii'))).hexdigest()
    fingerprint = fingerprint or ':'.join(digest[pos:pos + 2].upper() for pos in range(0, 64, 2))
    return ('subject=CN=*.openxlab.org.cn\nissuer=CN=Public test issuer\n'
            'notBefore=Sep 17 00:00:00 2026 GMT\nnotAfter=' + not_after
            + '\nsha256 Fingerprint=' + fingerprint + '\n').encode('ascii')


def mock_runner(handshakes, *, metadata=None):
    pending = iter(handshakes)

    def invoke(command, **kwargs):
        if command[:2] == ['openssl', 's_client']:
            item = next(pending)
            if isinstance(item, BaseException):
                raise item
            return item
        if command[:2] == ['openssl', 'x509']:
            output = metadata(kwargs['input']) if metadata else metadata_output(kwargs['input'])
            return subprocess.CompletedProcess(command, 0, output, b'')
        if command == ['openssl', 'version']:
            return subprocess.CompletedProcess(command, 0, b'OpenSSL 3.0.13 30 Jan 2024\n', b'')
        raise AssertionError('unexpected subprocess')

    return Mock(side_effect=invoke)


def handshake(certificates, *, code=0, exit_code=0, depth=0):
    stdout = b'\n'.join(certificates) + ('\nVerify return code: %s (PUBLIC status)\n' % code).encode('ascii')
    stderr = (('depth=%s CN=PUBLIC\nverify error:num=%s:PRIVATE failure text\n' % (depth, code)).encode('ascii')
              if code else b'PRIVATE diagnostic lines\n')
    return subprocess.CompletedProcess([], exit_code, stdout, stderr)


class Response:
    def __init__(self, status):
        self.status_code = status
        self.closed = False

    def getcode(self):
        return self.status_code

    def read(self, *args):
        raise AssertionError('HEAD response body must never be read')

    def close(self):
        self.closed = True


def expired():
    error = ssl.SSLCertVerificationError('PRIVATE certificate response')
    error.verify_code = 10
    return error


class ProbeTests(unittest.TestCase):
    def test_http_errors_still_verify_tls_and_neither_reads_body(self):
        response = Response(403)
        opener, head = Mock(return_value=response), Mock(return_value=response)
        report = p.compare(opener=opener, head=head)
        request = opener.call_args.args[0]
        self.assertEqual(request.full_url, p.TARGET)
        self.assertEqual(request.get_method(), 'HEAD')
        self.assertIsNone(request.get_header('Authorization'))
        self.assertEqual(opener.call_args.kwargs, {'timeout': 20})
        head.assert_called_once_with(p.TARGET, timeout=20, allow_redirects=False, verify=p.certifi.where())
        self.assertEqual(report['comparison'], 'both_verified')
        self.assertEqual([item['http_status'] for item in report['probes']], [403, 403])
        self.assertTrue(response.closed)
        self.assertEqual(report['provider_posts'], 0)
        self.assertFalse(report['result_zip_verified'])

    def test_urllib_raised_http_error_and_redirect_are_tls_success(self):
        for status in (301, 404, 500):
            response = io.BytesIO(b'PRIVATE response body')
            error = urllib.error.HTTPError(p.TARGET, status, 'PRIVATE', {}, response)
            report = p.probe_system_ca(Mock(side_effect=error))
            self.assertTrue(report['tls_verified'])
            self.assertEqual(report['http_status'], status)
            self.assertTrue(response.closed)
        self.assertIsNone(p.NoRedirect().redirect_request(None, None, 301, '', {}, 'https://different.invalid/'))

    def test_expired_system_chain_does_not_suppress_certifi_probe(self):
        opener = Mock(side_effect=urllib.error.URLError(expired()))
        head = Mock(return_value=Response(404))
        report = p.compare(opener=opener, head=head)
        self.assertEqual(report['comparison'], 'certifi_only_verified')
        self.assertEqual(report['probes'][0]['category'], 'tls_certificate_expired')
        self.assertEqual(report['probes'][1]['http_status'], 404)
        opener.assert_called_once()
        head.assert_called_once()
        self.assertNotIn('PRIVATE', json.dumps(report))

    def test_nested_requests_certificate_error_is_sanitized(self):
        error = p.requests.exceptions.SSLError(ssl.SSLError(expired()))
        report = p.compare(opener=Mock(return_value=Response(200)), head=Mock(side_effect=error))
        self.assertEqual(report['comparison'], 'system_ca_only_verified')
        self.assertEqual(report['probes'][1]['category'], 'tls_certificate_expired')
        self.assertNotIn('PRIVATE', json.dumps(report))

    def test_network_errors_are_independent_without_retries(self):
        opener = Mock(side_effect=TimeoutError('PRIVATE timeout'))
        head = Mock(side_effect=p.requests.exceptions.ConnectionError('PRIVATE network'))
        report = p.compare(opener=opener, head=head)
        self.assertEqual(report['comparison'], 'neither_verified')
        self.assertEqual([item['category'] for item in report['probes']], ['timeout', 'network_error'])
        self.assertTrue(all(item['requests_attempted'] == 1 and item['retries'] == 0 for item in report['probes']))
        opener.assert_called_once()
        head.assert_called_once()
        self.assertNotIn('PRIVATE', json.dumps(report))

    def test_default_urllib_uses_strict_context_and_no_redirect(self):
        opener = Mock()
        opener.open.return_value = Response(200)
        with patch.object(p.urllib.request, 'build_opener', return_value=opener) as build:
            report = p.probe_system_ca()
        handlers = build.call_args.args
        context = next(item._context for item in handlers if isinstance(item, p.urllib.request.HTTPSHandler))
        self.assertEqual(context.verify_mode, ssl.CERT_REQUIRED)
        self.assertTrue(context.check_hostname)
        self.assertTrue(any(isinstance(item, p.NoRedirect) for item in handlers))
        opener.open.assert_called_once()
        self.assertTrue(report['tls_verified'])

    def test_default_requests_uses_certifi_zero_retries_and_closes_session(self):
        session = Mock()
        session.head.return_value = Response(404)
        with patch.object(p.requests, 'Session', return_value=session):
            report = p.probe_certifi()
        protocol, adapter = session.mount.call_args.args
        self.assertEqual(protocol, 'https://')
        self.assertEqual(adapter.max_retries.total, 0)
        session.head.assert_called_once_with(p.TARGET, timeout=20, allow_redirects=False, verify=p.certifi.where())
        session.close.assert_called_once()
        self.assertTrue(report['tls_verified'])

    def test_cli_refuses_local_live_probe_but_preserves_safe_report(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'report.json'
            with patch.dict(p.os.environ, {'GITHUB_ACTIONS': ''}), patch.object(p, 'compare') as compare, redirect_stdout(io.StringIO()):
                self.assertEqual(p.main(['--output', str(path)]), 2)
            compare.assert_not_called()
            self.assertEqual(json.loads(path.read_text())['requests_attempted'], 0)

    def test_cloud_cli_always_preserves_failed_comparison(self):
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'report.json'
            report = {'comparison': 'neither_verified', 'probes': []}
            evidence = {'scope': 'public_hostname_tls_only', 'probes': [{'tls_verified': True}], 'result_zip_verified': False}
            with patch.dict(p.os.environ, CLOUD_ENV), patch.object(p, 'compare', return_value=report), \
                    patch.object(p, 'capture_handshake_evidence', return_value=evidence) as capture, redirect_stdout(io.StringIO()):
                self.assertEqual(p.main(['--output', str(path)]), 1)
            capture.assert_called_once_with()
            self.assertEqual(json.loads(path.read_text()), report)
            self.assertEqual(report['handshake_evidence'], evidence)
            self.assertEqual(report['exit_status_basis'], 'head_trust_comparison')

    def test_live_openssl_guard_requires_exact_manual_main_workflow(self):
        changes = {'GITHUB_ACTIONS': '', 'GITHUB_EVENT_NAME': 'pull_request',
                   'GITHUB_REF': 'refs/heads/feature', 'GITHUB_REPOSITORY': '',
                   'GITHUB_WORKFLOW_REF': 'example/research/.github/workflows/other.yml@refs/heads/main'}
        for key, invalid in changes.items():
            with self.subTest(key=key):
                env = dict(CLOUD_ENV, **{key: invalid})
                runner = Mock()
                report = p.capture_handshake_evidence(runner=runner, env=env)
                runner.assert_not_called()
                self.assertEqual(report['tls_connections_attempted'], 0)
                self.assertFalse(report['result_zip_verified'])
                self.assertTrue(all(item['category'] == 'cloud_execution_required' for item in report['probes']))

    def test_actual_runner_metadata_is_sanitized_and_never_derived_from_choice(self):
        for runner_os, runner_arch in (('Linux', 'X64'), ('macOS', 'ARM64')):
            with self.subTest(runner_os=runner_os):
                env = {'RUNNER_OS': runner_os, 'RUNNER_ARCH': runner_arch,
                       'MINERU_PROBE_RUNNER_IMAGE': 'macos-latest'}
                self.assertEqual(p.cloud_runner_metadata(env),
                                 {'runner_os': runner_os, 'runner_arch': runner_arch, 'requested_image': 'macos-latest'})
        # A requested image alone proves no executed OS or architecture.
        self.assertEqual(p.cloud_runner_metadata({'MINERU_PROBE_RUNNER_IMAGE': 'macos-latest'}),
                         {'runner_os': None, 'runner_arch': None, 'requested_image': 'macos-latest'})
        invalid = {'RUNNER_OS': 'PRIVATE hostname', 'RUNNER_ARCH': 'PRIVATE hardware',
                   'MINERU_PROBE_RUNNER_IMAGE': 'PRIVATE self-hosted label'}
        self.assertEqual(p.cloud_runner_metadata(invalid),
                         {'runner_os': None, 'runner_arch': None, 'requested_image': None})

    def test_mac_cloud_cli_keeps_strict_head_exit_policy_and_records_actual_runner(self):
        env = dict(CLOUD_ENV, RUNNER_OS='macOS', RUNNER_ARCH='ARM64', MINERU_PROBE_RUNNER_IMAGE='macos-latest')
        with tempfile.TemporaryDirectory() as folder:
            path = Path(folder) / 'report.json'
            report = {'comparison': 'neither_verified', 'probes': [], 'result_zip_verified': False}
            evidence = {'probes': [{'category': 'openssl_unavailable', 'tls_verified': False}], 'result_zip_verified': False}
            with patch.dict(p.os.environ, env), patch.object(p, 'compare', return_value=report), \
                    patch.object(p, 'capture_handshake_evidence', return_value=evidence), redirect_stdout(io.StringIO()):
                self.assertEqual(p.main(['--output', str(path)]), 1)
            saved = json.loads(path.read_text())
            self.assertEqual(saved['cloud_runner'], {'runner_os': 'macOS', 'runner_arch': 'ARM64', 'requested_image': 'macos-latest'})
            self.assertFalse(saved['result_zip_verified'])
            self.assertEqual(saved['comparison'], 'neither_verified')
            self.assertEqual(saved['handshake_evidence'], evidence)

    def test_two_fixed_strict_handshakes_keep_complete_ordered_peer_chain(self):
        leaf, leaf_hash = public_pem('leaf')
        intermediate, intermediate_hash = public_pem('intermediate')
        runner = mock_runner([handshake([leaf, intermediate]), handshake([leaf, intermediate])])
        report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
        connections = [call for call in runner.call_args_list if call.args[0][1] == 's_client']
        self.assertEqual(len(connections), 2)
        for call in connections:
            command = call.args[0]
            self.assertEqual(command[command.index('-connect') + 1], p.HOSTNAME + ':443')
            self.assertEqual(command[command.index('-servername') + 1], p.HOSTNAME)
            self.assertEqual(command[command.index('-verify_hostname') + 1], p.HOSTNAME)
            self.assertIn('-verify_return_error', command)
            self.assertIn('-showcerts', command)
            self.assertEqual(call.kwargs, {'input': b'', 'capture_output': True, 'timeout': 20, 'check': False})
            for forbidden in ('-proxy', '-no_check_time', '-ignore_critical', '-reconnect', '-ign_eof', '-4', '-6'):
                self.assertNotIn(forbidden, command)
        self.assertNotIn('-tls1_2', connections[0].args[0])
        self.assertEqual(connections[1].args[0][-3:], ['-tls1_2', '-cipher', p.TLS12_RSA_CIPHER])
        for item in report['probes']:
            self.assertTrue(item['tls_verified'])
            self.assertEqual(item['process_exit_code'], 0)
            self.assertEqual(item['verify_return_code'], 0)
            self.assertEqual(item['certificate_chain_kind'], 'peer_provided')
            self.assertEqual([cert['chain_position'] for cert in item['certificate_chain']], [0, 1])
            self.assertEqual([cert['sha256'] for cert in item['certificate_chain']], [leaf_hash, intermediate_hash])
            self.assertEqual(item['certificate_chain'][0]['not_before_utc'], '2026-09-17T00:00:00+00:00')
            self.assertEqual(item['certificate_chain'][0]['not_after_utc'], '2026-12-16T23:59:59+00:00')
        self.assertEqual(report['leaf_fingerprint_comparison'], 'same')
        self.assertEqual(report['peer_chain_fingerprint_comparison'], 'same')
        self.assertEqual(report['tls_connections_attempted'], 2)
        self.assertEqual(report['openssl_cli_version'], 'OpenSSL 3.0.13')
        self.assertEqual(report['http_requests'], 0)
        self.assertFalse(report['result_zip_verified'])
        self.assertNotIn('PRIVATE', json.dumps(report))
        self.assertNotIn('BEGIN CERTIFICATE', json.dumps(report))

    def test_expired_intermediate_is_visible_without_mislabeling_valid_leaf(self):
        leaf, _ = public_pem('valid leaf')
        intermediate, _ = public_pem('expired intermediate')
        runner = mock_runner([handshake([leaf, intermediate], code=10, exit_code=1, depth=1), handshake([leaf])],
                             metadata=lambda pem: metadata_output(pem, not_after='Oct  1 23:59:59 2026 GMT')
                             if pem == intermediate else metadata_output(pem))
        report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
        failed, passed = report['probes']
        self.assertEqual(failed['category'], 'tls_certificate_expired')
        self.assertEqual(failed['verification_error_depth'], 1)
        self.assertEqual(failed['process_exit_code'], 1)
        self.assertEqual(failed['verify_return_code'], 10)
        self.assertFalse(failed['tls_verified'])
        self.assertEqual(failed['certificate_chain'][0]['not_after_utc'], '2026-12-16T23:59:59+00:00')
        self.assertEqual(failed['certificate_chain'][1]['not_after_utc'], '2026-10-01T23:59:59+00:00')
        self.assertTrue(passed['tls_verified'])
        self.assertEqual(report['leaf_fingerprint_comparison'], 'same')
        self.assertEqual(report['peer_chain_fingerprint_comparison'], 'different')
        self.assertNotIn('PRIVATE', json.dumps(report))

    def test_distinct_peer_leaf_fingerprints_are_reported_without_recovery_claim(self):
        first, _ = public_pem('ECDSA leaf')
        second, _ = public_pem('RSA leaf')
        runner = mock_runner([handshake([first]), handshake([second])])
        report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
        self.assertEqual(report['leaf_fingerprint_comparison'], 'different')
        self.assertEqual(report['peer_chain_fingerprint_comparison'], 'different')
        self.assertFalse(report['result_zip_verified'])

    def test_verification_requires_zero_exit_and_explicit_zero_verify_code(self):
        leaf, _ = public_pem('leaf')
        cases = [(handshake([leaf], exit_code=1), 'tls_handshake_process_failed'),
                 (subprocess.CompletedProcess([], 0, leaf, b'PRIVATE'), 'tls_verification_unconfirmed'),
                 (handshake([leaf], code=62, exit_code=1, depth=0), 'tls_hostname_mismatch'),
                 (handshake([leaf], code=9, exit_code=1), 'tls_certificate_not_yet_valid'),
                 (handshake([leaf], code=20, exit_code=1), 'tls_certificate_verification_failed')]
        for completed, category in cases:
            with self.subTest(category=category):
                report = p.probe_openssl('default', runner=mock_runner([completed]), env=CLOUD_ENV)
                self.assertFalse(report['tls_verified'])
                self.assertEqual(report['category'], category)
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_timeout_missing_binary_and_oversized_output_still_allow_second_handshake(self):
        leaf, _ = public_pem('leaf')
        cases = [(subprocess.TimeoutExpired('openssl', 20, b'PRIVATE PEM'), 'timeout'),
                 (FileNotFoundError('PRIVATE missing path'), 'openssl_unavailable'),
                 (OSError('PRIVATE execution path'), 'openssl_execution_error'),
                 (subprocess.CompletedProcess([], 0, b'X' * (p.MAX_OPENSSL_OUTPUT_BYTES + 1), b''), 'invalid_openssl_output')]
        for first, category in cases:
            with self.subTest(category=category):
                runner = mock_runner([first, handshake([leaf])])
                report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
                self.assertEqual(report['probes'][0]['category'], category)
                self.assertTrue(report['probes'][1]['tls_verified'])
                self.assertEqual(report['tls_connections_attempted'], 2)
                self.assertNotIn('PRIVATE', json.dumps(report))

    def test_peer_chain_is_bounded_at_eight_and_truncation_is_explicit(self):
        chain = [public_pem(str(index))[0] for index in range(9)]
        runner = mock_runner([handshake(chain), handshake(chain)])
        report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
        self.assertTrue(all(item['certificate_chain_truncated'] for item in report['probes']))
        self.assertTrue(all(len(item['certificate_chain']) == 8 for item in report['probes']))
        self.assertEqual(report['peer_chain_fingerprint_comparison'], 'incomplete')
        self.assertEqual(len([call for call in runner.call_args_list if call.args[0][1] == 'x509']), 16)

    def test_metadata_fingerprint_or_field_failure_does_not_leak_raw_output(self):
        leaf, _ = public_pem('leaf')
        intermediate, _ = public_pem('intermediate')
        cases = [metadata_output(leaf, fingerprint='00:' * 31 + '00'),
                 b'PRIVATE raw parser output\n',
                 metadata_output(leaf).replace(b'CN=*.openxlab.org.cn', b'CN=PRIVATE\x1b[0m')]
        for invalid in cases:
            with self.subTest(invalid=invalid[:20]):
                runner = mock_runner([handshake([leaf, intermediate])],
                                     metadata=lambda pem: invalid if pem == leaf else metadata_output(pem))
                probe = p.probe_openssl('default', runner=runner, env=CLOUD_ENV)
                self.assertEqual(probe['certificate_metadata_category'], 'certificate_metadata_failed')
                self.assertEqual([cert['chain_position'] for cert in probe['certificate_chain']], [1])
                self.assertNotIn('PRIVATE', json.dumps(probe))

    def test_missing_leaf_metadata_cannot_be_compared_as_an_intermediate_leaf(self):
        leaf, _ = public_pem('leaf')
        intermediate, _ = public_pem('intermediate')
        runner = mock_runner([handshake([leaf, intermediate]), handshake([leaf, intermediate])],
                             metadata=lambda pem: b'PRIVATE failure' if pem == leaf else metadata_output(pem))
        report = p.capture_handshake_evidence(runner=runner, env=CLOUD_ENV)
        self.assertEqual(report['leaf_fingerprint_comparison'], 'not_observed')
        self.assertEqual(report['peer_chain_fingerprint_comparison'], 'incomplete')

    def test_workflow_has_main_only_probe_and_always_sanitized_artifact(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/mineru-result-tls-probe.yml').read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", workflow)
        self.assertIn("github.event_name == 'pull_request'", workflow)
        self.assertIn('if: always()', workflow)
        self.assertIn('${{ runner.temp }}/mineru-result-tls-probe.json', workflow)
        self.assertNotIn('secrets.', workflow)
        self.assertNotIn('workflow_call:', workflow)
        self.assertIn('two independent strict TLS handshakes', workflow)

    def test_runner_choice_contract_is_closed_default_ubuntu_and_manual_main_only(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/mineru-result-tls-probe.yml').read_text()
        dispatch = re.search(r'^  workflow_dispatch:\n(?P<body>(?:^    .*\n|^      .*\n|^        .*\n|^          .*\n)+)',
                             workflow, re.MULTILINE).group('body')
        self.assertIn('runner_image:', dispatch)
        self.assertIn('type: choice', dispatch)
        self.assertIn('default: ubuntu-latest', dispatch)
        self.assertEqual(re.findall(r'^          - (\S+)\s*$', dispatch, re.MULTILINE),
                         ['ubuntu-latest', 'macos-latest'])
        contract, probe = workflow.split('  contract:\n', 1)[1].split('  probe:\n', 1)
        self.assertIn("if: github.event_name == 'pull_request'", contract)
        self.assertIn('    runs-on: ubuntu-latest\n', contract)
        self.assertNotIn('runner_image', contract)
        self.assertIn("if: github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", probe)
        expression = re.search(r'^    runs-on: (.+)$', probe, re.MULTILINE).group(1)
        mapped = re.fullmatch(r"\$\{\{ inputs\.runner_image == '([^']+)' && '([^']+)' \|\| '([^']+)' \}\}", expression)
        self.assertIsNotNone(mapped, 'Runner mapping must be closed; never interpolate an arbitrary runner label')
        chosen, matched, fallback = mapped.groups()
        self.assertEqual((chosen, matched, fallback), ('macos-latest', 'macos-latest', 'ubuntu-latest'))
        for input_value, expected in (('', 'ubuntu-latest'), ('ubuntu-latest', 'ubuntu-latest'),
                                      ('macos-latest', 'macos-latest'), ('self-hosted', 'ubuntu-latest')):
            self.assertEqual(matched if input_value == chosen else fallback, expected)
        self.assertIn("MINERU_PROBE_RUNNER_IMAGE: ${{ inputs.runner_image || 'ubuntu-latest' }}", probe)


if __name__ == '__main__':
    unittest.main()
