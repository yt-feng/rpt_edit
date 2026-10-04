#!/usr/bin/env python3
"""Offline strict-client and independent-result regressions."""
import io
import json
from pathlib import Path
import ssl
import tempfile
import unittest
from contextlib import redirect_stdout
from unittest.mock import Mock, patch
import urllib.error

import probe_mineru_result_tls as p


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
            with patch.dict(p.os.environ, {'GITHUB_ACTIONS': 'true'}), patch.object(p, 'compare', return_value=report), redirect_stdout(io.StringIO()):
                self.assertEqual(p.main(['--output', str(path)]), 1)
            self.assertEqual(json.loads(path.read_text()), report)

    def test_workflow_has_main_only_probe_and_always_sanitized_artifact(self):
        workflow = (Path(__file__).resolve().parents[1] / '.github/workflows/mineru-result-tls-probe.yml').read_text()
        self.assertIn("github.event_name == 'workflow_dispatch' && github.ref == 'refs/heads/main'", workflow)
        self.assertIn("github.event_name == 'pull_request'", workflow)
        self.assertIn('if: always()', workflow)
        self.assertIn('${{ runner.temp }}/mineru-result-tls-probe.json', workflow)
        self.assertNotIn('secrets.', workflow)
        self.assertNotIn('workflow_call:', workflow)


if __name__ == '__main__':
    unittest.main()
