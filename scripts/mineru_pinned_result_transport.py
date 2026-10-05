"""Short-lived exact-leaf authentication for one manual cloud cache-seeding job.

This is deliberately separate from normal PKI clients. It never changes their
SSL context, CA stores, settings or retry policy. Certificate bytes remain
private runtime inputs; only fixed hashes and authentication facts are emitted.
"""
from __future__ import annotations

from datetime import datetime, timezone
import hashlib
import os
from pathlib import Path
import re
import ssl
import subprocess
import tempfile
import time
from urllib.parse import urlsplit

import certifi
import urllib3
from urllib3.connection import HTTPSConnection

from consume_legacy_mineru import MAX_ZIP, valid_url
from probe_mineru_result_tls import (PEM_RE, bounded_process_output,
                                    openssl_verification_metadata, public_certificate_metadata)

HOST = 'cdn-mineru.openxlab.org.cn'
LEAF_SHA256 = '12137420c572ee3fde42af27309c8f36efdfc4d07e76dcba801ddf6bc308aeb3'
LEAF_EXPIRY = datetime(2026, 10, 2, 23, 59, 59, tzinfo=timezone.utc)
CUTOFF = datetime(2026, 10, 5, 23, 59, 59, tzinfo=timezone.utc)
HISTORICAL_CACHE_CUTOFF = '2026-10-04T23:59:59+00:00'
WORKFLOW = '.github/workflows/mineru-result-cache-seed.yml'
AUTH_MODE = 'exact_leaf_pin'
AUTH_KEYS = {'auth_mode', 'pki_verified_now', 'historical_chain_verified', 'historical_ca_checks',
             'leaf_sha256', 'leaf_not_after_utc', 'cutoff_utc', 'peer_chain_sha256',
             'preflight_tls_connections', 'preflight_http_requests'}


class PinnedTransportError(ValueError):
    """Only fixed public categories, never request URLs or process output."""


def utc_now():
    return datetime.now(timezone.utc)


def require_before_cutoff(now=utc_now):
    value = now()
    if not isinstance(value, datetime) or value.tzinfo is None or not LEAF_EXPIRY <= value < CUTOFF:
        raise PinnedTransportError('pinned_auth_window_closed')
    return value


def require_cloud_manual(env=None):
    env = os.environ if env is None else env
    repository = env.get('GITHUB_REPOSITORY', '')
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or env.get('GITHUB_REF') != 'refs/heads/main'
            or re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is None
            or env.get('GITHUB_WORKFLOW_REF') != repository + '/' + WORKFLOW + '@refs/heads/main'):
        raise PinnedTransportError('reviewed_manual_cloud_required')


def fixed_result_uri(url):
    valid_url(url)
    parsed = urlsplit(url)
    if parsed.netloc not in {HOST, HOST + ':443'} or parsed.hostname != HOST:
        raise PinnedTransportError('fixed_result_origin_required')
    return (parsed.path or '/') + ('?' + parsed.query if parsed.query else '')


def _verified_authentication(value, accepted_cutoffs):
    if (not isinstance(value, dict) or set(value) != AUTH_KEYS or value.get('auth_mode') != AUTH_MODE
            or value.get('pki_verified_now') is not False or value.get('historical_chain_verified') is not True
            or type(value.get('historical_ca_checks')) is not int or value['historical_ca_checks'] != 2
            or value.get('leaf_sha256') != LEAF_SHA256 or value.get('leaf_not_after_utc') != LEAF_EXPIRY.isoformat()
            or value.get('cutoff_utc') not in accepted_cutoffs
            or type(value.get('preflight_tls_connections')) is not int or value['preflight_tls_connections'] != 1
            or type(value.get('preflight_http_requests')) is not int or value['preflight_http_requests'] != 0
            or not isinstance(value.get('peer_chain_sha256'), list) or not 2 <= len(value['peer_chain_sha256']) <= 8
            or value['peer_chain_sha256'][0] != LEAF_SHA256
            or any(not isinstance(item, str) or not re.fullmatch(r'[a-f0-9]{64}', item) for item in value['peer_chain_sha256'])):
        raise PinnedTransportError('prepared_authentication_required')
    return {key: list(item) if isinstance(item, list) else item for key, item in value.items()}


def verified_authentication(value):
    """Require the current fixed window for new connections and writes."""
    return _verified_authentication(value, (CUTOFF.isoformat(),))


def verified_stored_authentication(value):
    """Read an immutable cache authenticated in the fixed prior/current window.

    This does not authorize a connection or write and does not change the
    current transport deadline. All other authentication fields remain exact.
    """
    return _verified_authentication(value, (HISTORICAL_CACHE_CUTOFF, CUTOFF.isoformat()))


def prepare_authentication(*, runner=subprocess.run, now=utc_now, env=None):
    """One strict, no-HTTP handshake, then two offline historical CA checks."""
    require_cloud_manual(env)
    observed = require_before_cutoff(now)
    command = ['openssl', 's_client', '-connect', HOST + ':443', '-servername', HOST,
               '-verify_hostname', HOST, '-verify_return_error', '-showcerts', '-no_ign_eof']
    try:
        completed = runner(command, input=b'', capture_output=True, timeout=20, check=False)
        stdout, stderr = bounded_process_output(completed)
        code, depth = openssl_verification_metadata(stdout, stderr)
        if completed.returncode == 0 or code != 10 or depth != 0:
            raise PinnedTransportError('expected_leaf_expiry_not_observed')
        certificates = PEM_RE.findall(stdout)
        if not 2 <= len(certificates) <= 8:
            raise PinnedTransportError('complete_peer_chain_required')
        leaf_der = ssl.PEM_cert_to_DER_cert(certificates[0].decode('ascii'))
        if hashlib.sha256(leaf_der).hexdigest() != LEAF_SHA256:
            raise PinnedTransportError('fixed_leaf_fingerprint_mismatch')
        metadata = [public_certificate_metadata(pem, runner) for pem in certificates]
        if (metadata[0]['sha256'] != LEAF_SHA256
                or datetime.fromisoformat(metadata[0]['not_after_utc']) != LEAF_EXPIRY):
            raise PinnedTransportError('fixed_leaf_metadata_mismatch')
        for row in metadata[1:]:
            if not datetime.fromisoformat(row['not_before_utc']) <= observed < datetime.fromisoformat(row['not_after_utc']):
                raise PinnedTransportError('peer_intermediate_not_current')
        with tempfile.TemporaryDirectory(prefix='mineru-auth-chain-') as directory:
            leaf, intermediates = Path(directory) / 'leaf.pem', Path(directory) / 'intermediates.pem'
            leaf.write_bytes(certificates[0] + b'\n')
            intermediates.write_bytes(b'\n'.join(certificates[1:]) + b'\n')
            # The second verification uses only certifi's roots, rather than
            # silently falling back to the runner's default CA path/store.
            for ca_options in ([], ['-CAfile', certifi.where(), '-no-CApath', '-no-CAstore']):
                require_before_cutoff(now)
                verify = runner(['openssl', 'verify', '-attime', str(int(LEAF_EXPIRY.timestamp()) - 1),
                                 '-purpose', 'sslserver', '-verify_hostname', HOST,
                                 '-untrusted', str(intermediates), *ca_options, str(leaf)],
                                input=b'', capture_output=True, timeout=10, check=False)
                bounded_process_output(verify)
                if verify.returncode != 0:
                    raise PinnedTransportError('historical_chain_or_hostname_failed')
        require_before_cutoff(now)
        return {'auth_mode': AUTH_MODE, 'pki_verified_now': False, 'historical_chain_verified': True,
                'historical_ca_checks': 2, 'leaf_sha256': LEAF_SHA256,
                'leaf_not_after_utc': LEAF_EXPIRY.isoformat(), 'cutoff_utc': CUTOFF.isoformat(),
                'peer_chain_sha256': [row['sha256'] for row in metadata],
                'preflight_tls_connections': 1, 'preflight_http_requests': 0}
    except PinnedTransportError:
        raise
    except Exception:
        raise PinnedTransportError('authentication_preflight_failed') from None


class PinnedResultTransport:
    def __init__(self, authentication, *, now=utc_now, pool_factory=urllib3.HTTPSConnectionPool,
                 monotonic=time.monotonic):
        self.authentication = verified_authentication(authentication)
        self.now, self.pool_factory, self.monotonic = now, pool_factory, monotonic
        self.result_gets = 0

    def check_cutoff(self):
        require_before_cutoff(self.now)

    def __call__(self, url):
        uri = fixed_result_uri(url)
        self.check_cutoff()
        check_cutoff = self.check_cutoff

        class DeadlineConnection(HTTPSConnection):
            # This documented extension point adds only time guards. urllib3
            # performs every TLS/HTTP operation and its exact-leaf assertion.
            def connect(self):
                check_cutoff()
                super().connect()
                check_cutoff()

        pool, response = None, None
        try:
            pool = self.pool_factory(HOST, port=443, cert_reqs='CERT_NONE', assert_fingerprint=LEAF_SHA256,
                                     ssl_minimum_version=ssl.TLSVersion.TLSv1_2, maxsize=1, block=True,
                                     retries=False, timeout=urllib3.Timeout(connect=20, read=20))
            pool.ConnectionCls = DeadlineConnection
            self.check_cutoff()
            self.result_gets += 1
            started = self.monotonic()
            response = pool.request('GET', uri, headers={'Accept-Encoding': 'identity'},
                                    redirect=False, retries=False, preload_content=False, decode_content=False)
            self.check_cutoff()
            if response.status != 200:
                raise PinnedTransportError('result_http_rejected')
            if response.headers.get('Content-Encoding', 'identity').lower() not in {'', 'identity'}:
                raise PinnedTransportError('result_content_encoding_rejected')
            length = response.headers.get('Content-Length')
            if length is not None and (not re.fullmatch(r'[0-9]{1,12}', length) or not 1 <= int(length) <= MAX_ZIP):
                raise PinnedTransportError('result_size_rejected')
            chunks, size = [], 0
            while True:
                self.check_cutoff()
                if self.monotonic() - started > 120:
                    raise PinnedTransportError('result_read_budget_exhausted')
                chunk = response.read(min(65_536, MAX_ZIP + 1 - size), decode_content=False)
                self.check_cutoff()
                if not isinstance(chunk, bytes):
                    raise PinnedTransportError('result_body_invalid')
                if not chunk:
                    break
                chunks.append(chunk)
                size += len(chunk)
                if size > MAX_ZIP:
                    raise PinnedTransportError('result_size_rejected')
            if not size or length is not None and size != int(length):
                raise PinnedTransportError('result_body_incomplete')
            return b''.join(chunks)
        except PinnedTransportError:
            raise
        except Exception:
            raise PinnedTransportError('pinned_result_transport_failed') from None
        finally:
            if response is not None:
                response.close()
            if pool is not None:
                pool.close()
