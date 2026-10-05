"""Strict-first cloud MinerU result delivery with a fresh exact-leaf lease.

Only the known expired official result certificate can use this path. API
credentials never enter the downloader. The separate historical manual seed
deadline and its stored authentication receipts are unchanged.
"""
from __future__ import annotations

from datetime import datetime, timedelta, timezone
import os
import re
import subprocess
import time

import urllib3

from consume_legacy_mineru import NetworkStop, download_once
import mineru_pinned_result_transport as pinned

POLICY = 'daily-expired-leaf-auth-v1'
LEASE_SECONDS = 900
WORKFLOWS = {
    '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml': {'schedule', 'workflow_dispatch'},
    '.github/workflows/mineru-api-smoke.yml': {'workflow_dispatch'},
    '.github/workflows/market-views-mineru-recovery.yml': {'workflow_dispatch'},
}
AUTH_KEYS = (pinned.AUTH_KEYS - {'cutoff_utc'}) | {
    'schema_version', 'policy', 'issued_at_utc', 'expires_at_utc',
    'repository', 'workflow_path', 'event',
}
PIN_FAILURES = {
    'fixed_result_origin_required', 'expected_leaf_expiry_not_observed',
    'complete_peer_chain_required', 'fixed_leaf_fingerprint_mismatch',
    'fixed_leaf_metadata_mismatch', 'peer_intermediate_not_current',
    'historical_chain_or_hostname_failed', 'authentication_preflight_failed',
    'result_http_rejected', 'result_content_encoding_rejected', 'result_size_rejected',
    'result_read_budget_exhausted', 'result_body_invalid', 'result_body_incomplete',
    'pinned_result_transport_failed',
}


def utc_now():
    return datetime.now(timezone.utc)


def _fail(category):
    raise NetworkStop(category)


def _current(now):
    value = now()
    if not isinstance(value, datetime) or value.tzinfo is None:
        _fail('daily_auth_clock_invalid')
    return value.astimezone(timezone.utc)


def _cloud_context(env=None):
    env = os.environ if env is None else env
    repository = env.get('GITHUB_REPOSITORY', '')
    workflow_ref = env.get('GITHUB_WORKFLOW_REF', '')
    event = env.get('GITHUB_EVENT_NAME', '')
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_REF') != 'refs/heads/main'
            or not isinstance(repository, str)
            or not isinstance(workflow_ref, str) or not isinstance(event, str)
            or re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) is None):
        _fail('daily_cloud_context_required')
    for workflow_path, events in WORKFLOWS.items():
        if workflow_ref == repository + '/' + workflow_path + '@refs/heads/main' and event in events:
            return {'repository': repository, 'workflow_path': workflow_path, 'event': event}
    _fail('daily_cloud_context_required')


def _timestamp(value):
    if not isinstance(value, str):
        _fail('daily_authentication_invalid')
    try:
        stamp = datetime.fromisoformat(value)
    except ValueError:
        _fail('daily_authentication_invalid')
    if stamp.tzinfo is None or stamp.utcoffset() != timedelta(0) or stamp.isoformat() != value:
        _fail('daily_authentication_invalid')
    return stamp


def validate_stored_daily_authentication(value):
    """Check immutable historical facts without authorizing another connection."""
    if (not isinstance(value, dict) or set(value) != AUTH_KEYS
            or type(value.get('schema_version')) is not int or value['schema_version'] != 1
            or value.get('policy') != POLICY or value.get('auth_mode') != pinned.AUTH_MODE
            or value.get('pki_verified_now') is not False
            or value.get('historical_chain_verified') is not True
            or type(value.get('historical_ca_checks')) is not int or value['historical_ca_checks'] != 2
            or value.get('leaf_sha256') != pinned.LEAF_SHA256
            or value.get('leaf_not_after_utc') != pinned.LEAF_EXPIRY.isoformat()
            or type(value.get('preflight_tls_connections')) is not int or value['preflight_tls_connections'] != 1
            or type(value.get('preflight_http_requests')) is not int or value['preflight_http_requests'] != 0
            or not isinstance(value.get('peer_chain_sha256'), list)
            or not 2 <= len(value['peer_chain_sha256']) <= 8
            or value['peer_chain_sha256'][0] != pinned.LEAF_SHA256
            or any(not isinstance(item, str) or re.fullmatch(r'[a-f0-9]{64}', item) is None
                   for item in value['peer_chain_sha256'])
            or not isinstance(value.get('repository'), str)
            or re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', value['repository']) is None
            or not isinstance(value.get('workflow_path'), str) or value['workflow_path'] not in WORKFLOWS
            or not isinstance(value.get('event'), str)
            or value.get('event') not in WORKFLOWS[value['workflow_path']]):
        _fail('daily_authentication_invalid')
    issued, expires = _timestamp(value['issued_at_utc']), _timestamp(value['expires_at_utc'])
    if issued < pinned.LEAF_EXPIRY or not timedelta(0) < expires - issued <= timedelta(seconds=LEASE_SECONDS):
        _fail('daily_authentication_invalid')
    return {key: list(item) if isinstance(item, list) else item for key, item in value.items()}


def validate_daily_authentication(value, *, now=utc_now, env=None):
    """Require the same allowed cloud context and an unexpired current lease."""
    authentication = validate_stored_daily_authentication(value)
    context = _cloud_context(env)
    if any(authentication[key] != item for key, item in context.items()):
        _fail('daily_authentication_context_mismatch')
    if not _timestamp(authentication['issued_at_utc']) <= _current(now) < _timestamp(authentication['expires_at_utc']):
        _fail('daily_auth_lease_expired')
    return authentication


def _prepare_daily_authentication(*, runner, now, env):
    context = _cloud_context(env)
    issued = _current(now)
    if issued < pinned.LEAF_EXPIRY:
        _fail('daily_auth_clock_invalid')
    expires = issued + timedelta(seconds=LEASE_SECONDS)

    def check_time():
        if not issued <= _current(now) < expires:
            _fail('daily_auth_lease_expired')

    facts, chain_valid_until = pinned._prepare_expired_leaf_identity(
        runner=runner, observed=issued, check_time=check_time)
    # A short lease must also finish before a currently valid intermediate expires.
    expires = min(expires, chain_valid_until)
    authentication = {**facts, **context, 'schema_version': 1, 'policy': POLICY,
                      'issued_at_utc': issued.isoformat(), 'expires_at_utc': expires.isoformat()}
    return validate_daily_authentication(authentication, now=now, env=env)


class DailyPinnedResultTransport(pinned._ExactLeafResultTransport):
    def __init__(self, authentication, *, now=utc_now, env=None,
                 pool_factory=urllib3.HTTPSConnectionPool, monotonic=time.monotonic):
        self.authentication = validate_daily_authentication(authentication, now=now, env=env)
        self.now, self.env, self.pool_factory, self.monotonic = now, env, pool_factory, monotonic
        self.result_gets = 0

    def check_cutoff(self):
        # The shared downloader calls this before/after connection and each read.
        validate_daily_authentication(self.authentication, now=self.now, env=self.env)


def download_result(url, *, strict_downloader=download_once, env=None, now=utc_now,
                    runner=subprocess.run, pool_factory=urllib3.HTTPSConnectionPool,
                    monotonic=time.monotonic):
    """Return complete bytes and optional fresh cloud authentication facts."""
    try:
        return strict_downloader(url), None
    except NetworkStop as error:
        if error.args != ('tls_certificate_expired',):
            raise
    try:
        pinned.fixed_result_uri(url)
        authentication = _prepare_daily_authentication(runner=runner, now=now, env=env)
        transport = DailyPinnedResultTransport(authentication, now=now, env=env,
                                               pool_factory=pool_factory, monotonic=monotonic)
        payload = transport(url)
        validate_daily_authentication(authentication, now=now, env=env)
        return payload, authentication
    except NetworkStop:
        raise
    except pinned.PinnedTransportError as error:
        category = (error.args[0] if len(error.args) == 1 and isinstance(error.args[0], str)
                    and error.args[0] in PIN_FAILURES else 'daily_result_recovery_failed')
        raise NetworkStop(category) from None
    except Exception:
        raise NetworkStop('daily_result_recovery_failed') from None
