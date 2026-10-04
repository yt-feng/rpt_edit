#!/usr/bin/env python3
"""Cloud-only comparison of two strict TLS clients against one public CDN root."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import socket
import ssl
import urllib.error
import urllib.request

import certifi
import requests

TARGET = 'https://cdn-mineru.openxlab.org.cn/'
TIMEOUT = 20


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, newurl):
        return None


def error_category(error):
    """Expose a fixed category, never exception text or server response data."""
    pending, seen, nested = [error], set(), []
    while pending and len(seen) < 30:
        item = pending.pop()
        if not isinstance(item, BaseException) or id(item) in seen:
            continue
        seen.add(id(item))
        nested.append(item)
        pending.extend([getattr(item, 'reason', None), item.__cause__, item.__context__])
        pending.extend(item.args)
    for item in nested:
        if isinstance(item, ssl.SSLCertVerificationError):
            if getattr(item, 'verify_code', None) == 10:
                return 'tls_certificate_expired'
            if getattr(item, 'verify_code', None) == 9:
                return 'tls_certificate_not_yet_valid'
            return 'tls_certificate_verification_failed'
    if any(isinstance(item, (ssl.SSLError, requests.exceptions.SSLError)) for item in nested):
        return 'tls_error'
    if any(isinstance(item, (TimeoutError, socket.timeout, requests.exceptions.Timeout)) for item in nested):
        return 'timeout'
    if any(isinstance(item, (OSError, urllib.error.URLError, requests.exceptions.RequestException)) for item in nested):
        return 'network_error'
    return 'unexpected_error'


def result(engine, *, status=None, error=None):
    valid_status = type(status) is int and 100 <= status <= 599
    return {
        'engine': engine,
        'category': error_category(error) if error is not None else 'tls_verified' if valid_status else 'invalid_http_status',
        'tls_verified': error is None and valid_status,
        'http_status': status if error is None and valid_status else None,
        'requests_attempted': 1,
        'redirects_followed': 0,
        'retries': 0,
        'body_bytes_read': 0,
    }


def probe_system_ca(opener=None):
    response = None
    try:
        if opener is None:
            context = ssl.create_default_context()
            # These assertions protect strict validation if this client is edited later.
            if not context.check_hostname or context.verify_mode != ssl.CERT_REQUIRED:
                raise ValueError('strict_tls_required')
            opener = urllib.request.build_opener(urllib.request.HTTPSHandler(context=context), NoRedirect()).open
        response = opener(urllib.request.Request(TARGET, method='HEAD'), timeout=TIMEOUT)
        return result('urllib_system_ca', status=response.getcode())
    except urllib.error.HTTPError as error:
        # An HTTP error proves that TLS completed, including a refused redirect.
        response = error
        return result('urllib_system_ca', status=error.code)
    except Exception as error:
        return result('urllib_system_ca', error=error)
    finally:
        if response is not None:
            response.close()


def probe_certifi(head=None):
    session, response = None, None
    try:
        if head is None:
            session = requests.Session()
            session.mount('https://', requests.adapters.HTTPAdapter(max_retries=0))
            head = session.head
        response = head(TARGET, timeout=TIMEOUT, allow_redirects=False, verify=certifi.where())
        return result('requests_certifi', status=response.status_code)
    except Exception as error:
        return result('requests_certifi', error=error)
    finally:
        if response is not None:
            response.close()
        if session is not None:
            session.close()


def compare(*, opener=None, head=None):
    # Both are deliberately independent, single-attempt probes. A failure in one
    # must not suppress the other or trigger an automatic network retry.
    probes = [probe_system_ca(opener), probe_certifi(head)]
    outcomes = tuple(item['tls_verified'] for item in probes)
    comparison = {
        (True, True): 'both_verified',
        (True, False): 'system_ca_only_verified',
        (False, True): 'certifi_only_verified',
        (False, False): 'neither_verified',
    }[outcomes]
    return {'schema_version': 1, 'observed_at_utc': datetime.now(timezone.utc).isoformat(),
            'openssl_version': ssl.OPENSSL_VERSION, 'certifi_version': certifi.__version__,
            'target': TARGET, 'method': 'HEAD', 'comparison': comparison, 'probes': probes,
            'provider_posts': 0, 'source_files_read': 0, 'result_zip_verified': False}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--output', type=Path,
                        default=Path(os.environ.get('RUNNER_TEMP', '.')) / 'mineru-result-tls-probe.json')
    args = parser.parse_args(argv)
    if os.environ.get('GITHUB_ACTIONS') != 'true':
        report = {'schema_version': 1, 'category': 'cloud_execution_required', 'requests_attempted': 0}
        code = 2
    else:
        report = compare()
        code = 0 if report['comparison'] == 'both_verified' else 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
