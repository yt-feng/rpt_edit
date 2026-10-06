#!/usr/bin/env python3
"""Offline smoke transport tests: never connect to a real service."""
import contextlib
from email.utils import formatdate
import io
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import portal_smoke_get as smoke


class SmokeGetTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory(); self.addCleanup(self.temp.cleanup)
        self.output = Path(self.temp.name) / 'response.json'
        self.calls, self.waits, self.logs = [], [], []
        self.responses = []
        self.origin = 'https://private-origin.example.test'

    def transport(self, args, **kwargs):
        self.calls.append((args, kwargs))
        value = self.responses.pop(0)
        if isinstance(value, Exception):
            raise value
        code, status, headers, body = value
        Path(args[args.index('--dump-header')+1]).write_bytes(headers)
        Path(args[args.index('--output')+1]).write_bytes(body)
        return subprocess.CompletedProcess(args, code, str(status).zfill(3).encode(), b'private transport body/token')

    def invoke(self):
        return smoke.smoke_get('market-views', self.origin, self.output, run=self.transport,
                               sleep=self.waits.append, now=lambda: 1000, emit=self.logs.append)

    @staticmethod
    def response(status=200, *, code=0, retry=None, body=b'{"items": [1]}'):
        headers = f'HTTP/2 {status}\r\n'.encode()
        if retry is not None: headers += f'Retry-After: {retry}\r\n'.encode()
        return code, status, headers + b'\r\n', body

    def test_three_temporary_failures_then_success_keep_identical_get_and_body(self):
        self.responses = [self.response(502), self.response(429), self.response(503), self.response()]
        self.invoke()
        self.assertEqual(len(self.calls), 4); self.assertEqual(self.waits, [5,15,30])
        self.assertTrue(all(call == self.calls[0] for call in self.calls))
        args, kwargs = self.calls[0]
        self.assertEqual(args[args.index('--request')+1], 'GET')
        self.assertEqual(args[args.index('--max-time')+1], '30')
        self.assertEqual(args[args.index('--max-redirs')+1], '0')
        self.assertEqual(kwargs['timeout'], 35)
        for forbidden in ('--insecure', '-k', '--location', '-L', '--retry'):
            self.assertNotIn(forbidden,args)
        self.assertEqual(self.output.read_bytes(), b'{"items": [1]}')
        self.assertNotIn(self.origin, '\n'.join(self.logs))
        self.assertNotIn('private transport', '\n'.join(self.logs))

    def test_fourth_temporary_failure_stops_without_stale_body(self):
        self.output.write_bytes(b'old success')
        self.responses = [self.response(408)]*4
        with self.assertRaisesRegex(smoke.SmokeFailure, 'status=408 attempts=4'): self.invoke()
        self.assertEqual(len(self.calls),4); self.assertEqual(self.waits,[5,15,30])
        self.assertFalse(self.output.exists())

    def test_timeout_and_connection_failures_retry_only_bounded_get(self):
        for failure in (self.response(0, code=28), self.response(0,code=7),
                        self.response(0,code=56), subprocess.TimeoutExpired('private command',35)):
            with self.subTest(failure=type(failure).__name__):
                self.calls.clear(); self.waits.clear()
                self.responses=[failure,self.response()]; self.invoke()
                self.assertEqual(len(self.calls),2); self.assertEqual(self.waits,[5])

    def test_temporary_dns_failure_retries_same_endpoint_without_network_changes(self):
        self.responses = [self.response(0, code=6), self.response()]
        self.invoke()
        self.assertEqual(len(self.calls), 2)
        self.assertEqual(self.calls[0], self.calls[1])
        self.assertEqual(self.waits, [5])
        self.assertIn('dns_resolution_failed', self.logs[0])
        self.assertNotIn(self.origin, '\n'.join(self.logs))
        self.assertEqual(self.output.read_bytes(), b'{"items": [1]}')

    def test_auth_redirect_certificate_and_other_errors_do_not_retry(self):
        for status,code in ((401,0),(403,0),(301,0),(302,0),(307,0),(308,0),(404,0),(0,60),(0,35),(0,23),(401,28),(302,28)):
            with self.subTest(status=status,code=code):
                self.calls.clear();self.waits.clear();self.responses=[self.response(status,code=code)]
                with self.assertRaises(smoke.SmokeFailure): self.invoke()
                self.assertEqual(len(self.calls),1);self.assertEqual(self.waits,[])
                self.assertFalse(self.output.exists())

    def test_retry_after_seconds_and_http_date_are_respected(self):
        for header in ('20',formatdate(1025,usegmt=True)):
            self.waits.clear(); self.responses=[self.response(429,retry=header),self.response()]
            self.invoke(); self.assertEqual(self.waits,[20 if header=='20' else 25])

    def test_retry_after_over_budget_or_invalid_fails_without_early_retry(self):
        for header in ('61','not-a-date','NaN','-1'):
            self.calls.clear();self.waits.clear();self.responses=[self.response(503,retry=header)]
            with self.assertRaisesRegex(smoke.SmokeFailure,'retry_after'): self.invoke()
            self.assertEqual(len(self.calls),1);self.assertEqual(self.waits,[])

    def test_validation_remains_callers_responsibility_without_transport_replay(self):
        self.responses=[self.response(body=b'not valid JSON')]
        self.invoke(); self.assertEqual(len(self.calls),1)
        self.assertEqual(self.output.read_bytes(),b'not valid JSON')

    def test_cli_only_prints_fixed_label_and_sanitized_failure(self):
        with patch.dict(os.environ,{'PORTAL_SITE_URL':self.origin}), \
             patch.object(smoke,'smoke_get',side_effect=OSError('secret origin/token/body')), \
             contextlib.redirect_stdout(io.StringIO()) as output:
            result=smoke.main(['--endpoint','runtime-data','--output',str(self.output)])
        self.assertEqual(result,1)
        self.assertEqual(output.getvalue(),'::error::smoke endpoint=runtime-data local_failure\n')

    def test_only_https_origin_and_fixed_endpoint_are_admitted(self):
        for origin in ('http://bad.test','https://user:password@bad.test','https://bad.test/path','https://bad.test?token=private'):
            with self.assertRaisesRegex(smoke.SmokeFailure,'invalid_origin'):
                smoke.smoke_get('market-views',origin,self.output,run=self.transport)
        self.assertFalse(self.calls)

    def test_real_cli_with_offline_curl_preserves_response_and_hides_origin(self):
        binary = Path(self.temp.name) / 'curl'
        binary.write_text('#!' + sys.executable + '\n'
            'import sys\nfrom pathlib import Path\n'
            'args=sys.argv[1:]\n'
            'assert args[args.index("--request")+1]=="GET"\n'
            'assert "--location" not in args and "--insecure" not in args\n'
            'Path(args[args.index("--dump-header")+1]).write_bytes(b"HTTP/2 200\\r\\n\\r\\n")\n'
            'Path(args[args.index("--output")+1]).write_bytes(b"{\\"items\\":[1]}")\n'
            'print("200",end="")\n')
        binary.chmod(0o755)
        result = subprocess.run([sys.executable, '-B', str(Path(smoke.__file__)),
            '--endpoint', 'runtime-data', '--output', str(self.output)], capture_output=True, text=True,
            env={**os.environ, 'PATH':self.temp.name, 'PORTAL_SITE_URL':self.origin})
        self.assertEqual(result.returncode, 0, result.stderr)
        self.assertEqual(self.output.read_bytes(), b'{"items":[1]}')
        self.assertIn('endpoint=runtime-data attempt=1/4 status=200', result.stdout)
        self.assertNotIn(self.origin, result.stdout + result.stderr)


if __name__=='__main__': unittest.main()
