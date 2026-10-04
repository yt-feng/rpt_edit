#!/usr/bin/env python3
"""Cloud-only strict HEAD comparison and bounded public TLS-chain diagnostics."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import ssl
import subprocess
import urllib.error
import urllib.request

import certifi
import requests

TARGET = 'https://cdn-mineru.openxlab.org.cn/'
HOSTNAME = 'cdn-mineru.openxlab.org.cn'
TIMEOUT = 20
MAX_OPENSSL_OUTPUT_BYTES = 262144
MAX_CHAIN_CERTIFICATES = 8
TLS12_RSA_CIPHER = 'ECDHE-RSA-AES128-GCM-SHA256'
PEM_RE = re.compile(rb'-----BEGIN CERTIFICATE-----\r?\n[A-Za-z0-9+/=\r\n]+-----END CERTIFICATE-----')


def cloud_manual_execution_allowed(env=None):
    """Live diagnostics belong only to this exact main manual cloud workflow."""
    env = os.environ if env is None else env
    repository = env.get('GITHUB_REPOSITORY', '')
    expected = repository + '/.github/workflows/mineru-result-tls-probe.yml@refs/heads/main'
    return (env.get('GITHUB_ACTIONS') == 'true'
            and env.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and env.get('GITHUB_REF') == 'refs/heads/main'
            and re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is not None
            and env.get('GITHUB_WORKFLOW_REF') == expected)


def bounded_process_output(completed):
    """Raw process output stays in memory and is never included in the report."""
    parts = [completed.stdout or b'', completed.stderr or b'']
    if any(not isinstance(part, bytes) for part in parts) or sum(map(len, parts)) > MAX_OPENSSL_OUTPUT_BYTES:
        raise ValueError('invalid_process_output')
    return parts


def public_certificate_metadata(pem, runner):
    # x509 is a local parser, not another TLS connection. Only one PEM is passed
    # per call, preserving the peer-provided leaf/intermediate order.
    parsed = runner(['openssl', 'x509', '-noout', '-subject', '-issuer', '-startdate', '-enddate',
                     '-fingerprint', '-sha256', '-nameopt', 'RFC2253'],
                    input=pem, capture_output=True, timeout=5, check=False)
    stdout, _ = bounded_process_output(parsed)
    if parsed.returncode != 0:
        raise ValueError('certificate_metadata_failed')
    fields = {}
    for line in stdout.decode('ascii', errors='strict').splitlines():
        if '=' not in line:
            raise ValueError('invalid_certificate_metadata')
        key, value = line.split('=', 1)
        key = key.strip()
        if key.lower() == 'sha256 fingerprint':
            key = 'sha256 Fingerprint'
        if key in fields or not value or len(value) > 2048 or any(ord(char) < 32 or ord(char) > 126 for char in value):
            raise ValueError('invalid_certificate_metadata')
        fields[key] = value
    if set(fields) != {'subject', 'issuer', 'notBefore', 'notAfter', 'sha256 Fingerprint'}:
        raise ValueError('invalid_certificate_metadata')
    fingerprint = fields['sha256 Fingerprint']
    if re.fullmatch(r'(?:[0-9A-Fa-f]{2}:){31}[0-9A-Fa-f]{2}', fingerprint) is None:
        raise ValueError('invalid_certificate_fingerprint')
    digest = hashlib.sha256(ssl.PEM_cert_to_DER_cert(pem.decode('ascii'))).hexdigest()
    if fingerprint.replace(':', '').lower() != digest:
        raise ValueError('certificate_fingerprint_mismatch')
    dates = {}
    for name in ('notBefore', 'notAfter'):
        dates[name] = datetime.strptime(fields[name], '%b %d %H:%M:%S %Y GMT').replace(tzinfo=timezone.utc).isoformat()
    return {'subject': fields['subject'], 'issuer': fields['issuer'],
            'not_before_utc': dates['notBefore'], 'not_after_utc': dates['notAfter'], 'sha256': digest}


def openssl_verification_metadata(stdout, stderr):
    # OpenSSL may print a final return code on stdout and a certificate error
    # with its depth on stderr. Report only integers; never print those lines.
    combined = (stdout + b'\n' + stderr).decode('ascii', errors='replace')
    returns = re.findall(r'Verify return code:\s*(\d{1,5})\b', combined)
    errors = re.findall(r'verify error:num=(\d{1,5})\b', combined)
    failing = next((int(item) for item in errors + returns if int(item) != 0), None)
    code = failing if failing is not None else int(returns[-1]) if returns else None
    depth = None
    if failing is not None:
        last_depth = None
        for line in combined.splitlines():
            match = re.match(r'depth=(\d{1,3})\b', line)
            if match:
                last_depth = int(match.group(1))
            match = re.search(r'verify error:num=(\d{1,5})\b', line)
            if match and int(match.group(1)) == failing:
                depth = last_depth
                break
    return code, depth


def probe_openssl(variant, *, runner=None, env=None):
    if variant not in ('default', 'tls12_rsa'):
        raise ValueError('unsupported_tls_diagnostic_variant')
    probe = {'engine': 'openssl_s_client_' + variant, 'category': 'cloud_execution_required',
             'tls_verified': False, 'process_exit_code': None, 'verify_return_code': None,
             'verification_error_depth': None, 'certificate_chain': [],
             'certificate_chain_kind': 'peer_provided', 'certificate_chain_truncated': False,
             'certificate_metadata_category': 'not_observed', 'tls_connections_attempted': 0,
             'http_requests': 0, 'provider_posts': 0, 'retries': 0, 'result_zip_verified': False}
    if not cloud_manual_execution_allowed(env):
        return probe
    runner = subprocess.run if runner is None else runner
    command = ['openssl', 's_client', '-connect', HOSTNAME + ':443', '-servername', HOSTNAME,
               '-verify_hostname', HOSTNAME, '-verify_return_error', '-showcerts', '-no_ign_eof']
    if variant == 'tls12_rsa':
        # These invocation-only parameters are diagnostic evidence, never a
        # production Requests/Worker TLS configuration or an automatic retry.
        command.extend(['-tls1_2', '-cipher', TLS12_RSA_CIPHER])
    probe['tls_connections_attempted'] = 1
    try:
        completed = runner(command, input=b'', capture_output=True, timeout=TIMEOUT, check=False)
        probe['process_exit_code'] = completed.returncode if type(completed.returncode) is int else None
        stdout, stderr = bounded_process_output(completed)
        code, depth = openssl_verification_metadata(stdout, stderr)
        probe['verify_return_code'], probe['verification_error_depth'] = code, depth
        if code not in (None, 0):
            probe['category'] = {9: 'tls_certificate_not_yet_valid', 10: 'tls_certificate_expired',
                                 62: 'tls_hostname_mismatch'}.get(code, 'tls_certificate_verification_failed')
        elif probe['process_exit_code'] != 0:
            probe['category'] = 'tls_handshake_process_failed'
        elif code != 0:
            probe['category'] = 'tls_verification_unconfirmed'
        else:
            probe['category'], probe['tls_verified'] = 'tls_verified', True
        certificates = PEM_RE.findall(stdout)
        probe['certificate_chain_truncated'] = len(certificates) > MAX_CHAIN_CERTIFICATES
        if certificates:
            probe['certificate_metadata_category'] = 'parsed'
            for position, pem in enumerate(certificates[:MAX_CHAIN_CERTIFICATES]):
                try:
                    metadata = public_certificate_metadata(pem, runner)
                    metadata['chain_position'] = position
                    probe['certificate_chain'].append(metadata)
                except Exception:
                    probe['certificate_metadata_category'] = 'certificate_metadata_failed'
        return probe
    except subprocess.TimeoutExpired:
        probe['category'] = 'timeout'
    except FileNotFoundError:
        probe['category'] = 'openssl_unavailable'
    except OSError:
        probe['category'] = 'openssl_execution_error'
    except Exception:
        probe['category'] = 'invalid_openssl_output'
    return probe


def capture_handshake_evidence(*, runner=None, env=None):
    # Two connections, no HTTP and no provider submission. Either handshake
    # can fail without suppressing the other or changing the HEAD exit policy.
    probes = [probe_openssl(variant, runner=runner, env=env) for variant in ('default', 'tls12_rsa')]
    leaf_hashes = [item['certificate_chain'][0]['sha256']
                   if item['certificate_chain'] and item['certificate_chain'][0]['chain_position'] == 0 else None
                   for item in probes]
    chains = [[cert['sha256'] for cert in item['certificate_chain']] for item in probes]
    observed = all(leaf_hashes)
    complete = all(item['certificate_metadata_category'] == 'parsed' and not item['certificate_chain_truncated']
                   for item in probes) and observed
    cli_version = None
    if cloud_manual_execution_allowed(env):
        try:
            # The CLI binary and Python ssl module can use different versions.
            # This local-only parser call adds no TLS or HTTP connection.
            invoke = subprocess.run if runner is None else runner
            version = invoke(['openssl', 'version'], input=b'', capture_output=True, timeout=5, check=False)
            stdout, _ = bounded_process_output(version)
            match = re.match(rb'OpenSSL ([0-9]+\.[0-9]+\.[0-9]+[a-z]?)(?:\s|$)', stdout)
            if version.returncode == 0 and match:
                cli_version = 'OpenSSL ' + match.group(1).decode('ascii')
        except Exception:
            pass
    return {'scope': 'public_hostname_tls_only', 'probes': probes,
            'openssl_cli_version': cli_version,
            'leaf_fingerprint_comparison': ('same' if leaf_hashes[0] == leaf_hashes[1] else 'different') if observed else 'not_observed',
            'peer_chain_fingerprint_comparison': ('same' if chains[0] == chains[1] else 'different') if complete else 'incomplete',
            'tls_connections_attempted': sum(item['tls_connections_attempted'] for item in probes),
            'http_requests': 0, 'provider_posts': 0, 'result_zip_verified': False}


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
    if not cloud_manual_execution_allowed():
        report = {'schema_version': 1, 'category': 'cloud_execution_required', 'requests_attempted': 0}
        code = 2
    else:
        report = compare()
        report['handshake_evidence'] = capture_handshake_evidence()
        report['exit_status_basis'] = 'head_trust_comparison'
        code = 0 if report['comparison'] == 'both_verified' else 1
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=True, indent=2) + '\n', encoding='utf-8')
    print(json.dumps(report, ensure_ascii=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
