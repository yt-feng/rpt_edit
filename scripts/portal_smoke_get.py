#!/usr/bin/env python3
"""Bounded read-only live smoke GETs; response validation belongs to the caller."""
from __future__ import annotations

import argparse
from email.utils import parsedate_to_datetime
import math
import os
from pathlib import Path
import subprocess
import tempfile
import time
from urllib.parse import urlsplit

ENDPOINTS = {'runtime-data': '/api/health?runtime-data=1', 'market-views': '/api/market-views'}
DELAYS = (5, 15, 30)
# Do not outwait the deployment's rollback window or ignore a longer server delay.
MAX_RETRY_AFTER = 30
# curl enforces a whole-request 30-second deadline, including response body reads.
TRANSIENT_CURL = {6: 'dns_resolution_failed', 7: 'connection_failed', 28: 'connection_timeout',
                  52: 'empty_reply', 55: 'connection_send', 56: 'connection_receive'}
CERTIFICATE_CURL = {35, 51, 58, 59, 60, 64, 66, 77, 80, 82, 83, 90, 91}


class SmokeFailure(Exception):
    """Only fixed, public diagnostics may be placed in this exception."""


def retry_after(headers, *, now):
    """Read the last response block, including optional proxy/100 headers."""
    values = []
    for line in headers.decode('iso-8859-1').splitlines():
        if line.startswith('HTTP/'):
            values = []
        elif line.lower().startswith('retry-after:'):
            values.append(line.split(':', 1)[1].strip())
    if not values:
        return 0
    if len(values) != 1:
        raise SmokeFailure('invalid_retry_after')
    value = values[0]
    if value.isascii() and value.isdecimal():
        delay = int(value)
    else:
        try:
            when = parsedate_to_datetime(value)
            if when.tzinfo is None:
                raise ValueError('Missing timezone')
            delay = max(0, math.ceil(when.timestamp() - now()))
        except (ValueError, TypeError, OverflowError):
            raise SmokeFailure('invalid_retry_after') from None
    if delay > MAX_RETRY_AFTER:
        raise SmokeFailure('retry_after_exceeds_budget')
    return delay


def smoke_get(label, origin, output, *, run=subprocess.run, sleep=time.sleep,
              now=time.time, emit=print):
    if label not in ENDPOINTS:
        raise SmokeFailure('invalid_endpoint_label')
    try:
        parsed = urlsplit(origin)
        valid = (parsed.scheme == 'https' and parsed.hostname and not parsed.username and not parsed.password
                 and parsed.path in ('', '/') and not parsed.query and not parsed.fragment)
        parsed.port  # Validate a malformed port before constructing a command.
    except (TypeError, ValueError):
        valid = False
    if not valid:
        raise SmokeFailure('invalid_origin')
    output = Path(output)
    # A failed attempt never leaves a stale successful body at the caller's path.
    output.unlink(missing_ok=True)
    output.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='.portal-smoke-', dir=output.parent) as temporary:
        body, headers = Path(temporary) / 'body', Path(temporary) / 'headers'
        command = ['curl', '--silent', '--max-time', '30', '--connect-timeout', '10',
                   '--proto', '=https', '--max-redirs', '0', '--request', 'GET',
                   '--dump-header', str(headers), '--output', str(body), '--write-out', '%{http_code}',
                   '--', origin.rstrip('/') + ENDPOINTS[label]]
        for attempt in range(4):
            body.unlink(missing_ok=True); headers.unlink(missing_ok=True)
            status = None
            try:
                result = run(command, capture_output=True, check=False, timeout=35)
            except subprocess.TimeoutExpired:
                code, category = 28, 'connection_timeout'
            except OSError:
                raise SmokeFailure('client_unavailable') from None
            else:
                code = result.returncode
                if result.stdout.strip().isdigit() and len(result.stdout.strip()) == 3:
                    status = int(result.stdout.strip())
                category = (TRANSIENT_CURL.get(code) or ('tls_validation' if code in CERTIFICATE_CURL
                            else 'client_failure')) if code else 'http_status'
            if code == 0 and status == 200:
                if not body.is_file():
                    raise SmokeFailure('response_body_missing')
                body.replace(output)
                emit(f'::notice::smoke endpoint={label} attempt={attempt + 1}/4 status=200')
                return
            transient = (code in TRANSIENT_CURL or code == 0 and status is not None
                         and (status in (408, 429) or 500 <= status <= 599))
            if status in (401, 403) or status is not None and 300 <= status <= 399:
                transient = False
            diagnostic = f'{category}' + (f' status={status}' if status is not None else '')
            if not transient or attempt == 3:
                raise SmokeFailure(f'{diagnostic} attempts={attempt + 1}')
            delay = max(DELAYS[attempt], retry_after(headers.read_bytes() if headers.exists() else b'', now=now))
            emit(f'::notice::smoke endpoint={label} attempt={attempt + 1}/4 {diagnostic}; retry_in={delay}s')
            sleep(delay)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--endpoint', choices=ENDPOINTS, required=True)
    parser.add_argument('--output', required=True)
    args = parser.parse_args(argv)
    try:
        smoke_get(args.endpoint, os.environ.get('PORTAL_SITE_URL', ''), args.output)
    except SmokeFailure as error:
        print(f'::error::smoke endpoint={args.endpoint} {error}', flush=True)
        return 1
    except Exception:
        # Neither origin, command arguments, transport text nor response body may
        # leak through a traceback. Unexpected local failures remain failures.
        print(f'::error::smoke endpoint={args.endpoint} local_failure', flush=True)
        return 1
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
