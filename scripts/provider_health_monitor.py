#!/usr/bin/env python3
"""Read provider account health without generation calls or credential logging."""
from __future__ import annotations

import argparse
from datetime import datetime, timezone
from decimal import Decimal, InvalidOperation
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request

ENDPOINTS = {
    'deepseek': 'https://api.deepseek.com/user/balance',
    'tikhub': 'https://api.tikhub.io/api/v1/tikhub/user/get_user_info',
}
STATUSES = (
    'invalid_key', 'expired_key', 'account_disabled', 'permission_denied',
    'exhausted', 'payment_required', 'missing_key', 'malformed_response',
    'transport_error', 'service_unavailable', 'rate_limited', 'low_balance',
    'expiring_key', 'healthy',
)
MAX_BYTES = 32768


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def utc_now():
    return datetime.now(timezone.utc)


def timestamp(value):
    parsed = datetime.fromisoformat(value.replace('Z', '+00:00'))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)


def number(value):
    if isinstance(value, bool) or not isinstance(value, (str, int, float, Decimal)):
        raise ValueError('Invalid numeric field')
    try:
        result = Decimal(str(value))
    except InvalidOperation:
        raise ValueError('Invalid numeric field') from None
    if not result.is_finite():
        raise ValueError('Non-finite numeric field')
    return result


def thresholds(env):
    result = {
        'tikhub': number(env.get('PROVIDER_TIKHUB_LOW_BALANCE') or '5'),
        'CNY': number(env.get('PROVIDER_DEEPSEEK_LOW_CNY') or '20'),
        'USD': number(env.get('PROVIDER_DEEPSEEK_LOW_USD') or '5'),
    }
    if any(value < 0 for value in result.values()):
        raise ValueError('Low-balance thresholds must be non-negative')
    return result


def http_status(code):
    return {401: 'invalid_key', 402: 'payment_required', 403: 'permission_denied',
            429: 'rate_limited'}.get(code, 'service_unavailable' if code >= 500 else 'malformed_response')


def fetch(provider, key):
    request = urllib.request.Request(ENDPOINTS[provider], headers={
        'Authorization': f'Bearer {key}', 'Accept': 'application/json',
        'User-Agent': 'provider-health-monitor/1',
    })
    try:
        with urllib.request.build_opener(NoRedirect()).open(request, timeout=20) as response:
            raw = response.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                return 200, None
            try:
                return response.status, json.loads(raw)
            except (ValueError, UnicodeError):
                return response.status, None
    except urllib.error.HTTPError as error:
        # Provider error bodies can echo credentials. Never retain or print them.
        error.close()
        return error.code, None
    except (urllib.error.URLError, TimeoutError, OSError):
        return 0, None


def classify(provider, code, data, limits, now):
    if not code:
        return ['transport_error']
    if code != 200:
        return [http_status(code)]
    if not isinstance(data, dict):
        return ['malformed_response']
    try:
        if provider == 'deepseek':
            available = data.get('is_available')
            balances = data.get('balance_infos')
            if type(available) is not bool or not isinstance(balances, list) or not balances:
                raise ValueError('Balance schema')
            rows = []
            seen = set()
            for row in balances:
                currency = row['currency']
                if currency not in ('CNY', 'USD') or currency in seen:
                    raise ValueError('Unknown or duplicate currency')
                seen.add(currency)
                rows.append((number(row['total_balance']), limits[currency]))
            if not available or all(balance <= 0 for balance, _ in rows):
                return ['exhausted']
            return ['low_balance' if all(balance <= limit for balance, limit in rows) else 'healthy']

        result_code = data.get('code', 200)
        if type(result_code) is not int:
            raise ValueError('Provider code')
        if result_code != 200:
            return [http_status(result_code)]
        user, api_key = data.get('user_data'), data.get('api_key_data')
        if not isinstance(user, dict) or not isinstance(api_key, dict):
            raise ValueError('User schema')
        if type(user.get('account_disabled')) is not bool or type(user.get('is_active')) is not bool:
            raise ValueError('Account state schema')
        if user['account_disabled'] or not user['is_active']:
            return ['account_disabled']
        if type(api_key.get('api_key_status')) is not int:
            raise ValueError('Key state schema')
        signals = []
        if api_key['api_key_status'] != 1:
            signals.append('invalid_key')
        expiry = api_key.get('expires_at')
        if expiry is not None:
            remaining = (timestamp(expiry) - now).total_seconds()
            if remaining <= 0:
                signals.append('expired_key')
            elif remaining <= 14 * 86400:
                signals.append('expiring_key')
        paid = number(user.get('balance_exact', user.get('balance')))
        # Free credits are not accepted by every endpoint. They must not mask
        # an empty paid wallet used by the daily low-fan workflow.
        if paid <= 0:
            signals.append('exhausted')
        elif paid <= limits['tikhub']:
            signals.append('low_balance')
        return sorted(set(signals), key=STATUSES.index) or ['healthy']
    except (KeyError, TypeError, ValueError, OverflowError, AttributeError):
        return ['malformed_response']


def probe(keys, env, *, getter=fetch, now=None, workflow='.github/workflows/provider-api-health.yml'):
    now = now or utc_now()
    limits = thresholds(env)
    checks = []
    seen = set()
    for spec in keys:
        provider, slot = spec.split(':', 1)
        if provider not in ENDPOINTS or not re.fullmatch(r'[A-Z][A-Z0-9_]{0,63}', slot) or spec in seen:
            raise ValueError('Invalid or repeated provider key slot')
        seen.add(spec)
        key = env.get(slot, '').strip()
        signals = classify(provider, *getter(provider, key), limits, now) if key else ['missing_key']
        checks.append({'provider': provider, 'slot': slot, 'status': signals[0], 'signals': signals})
    if not checks or len(checks) > 32:
        raise ValueError('Expected 1-32 provider slots')
    report = {
        'schema_version': 1, 'repository': env.get('GITHUB_REPOSITORY', ''),
        'run_id': env.get('GITHUB_RUN_ID', ''), 'run_attempt': int(env.get('GITHUB_RUN_ATTEMPT', '1')),
        'commit': env.get('GITHUB_SHA', ''), 'workflow': workflow,
        'checked_at': now.isoformat().replace('+00:00', 'Z'), 'checks': checks,
    }
    return report


def validate_report(report, *, now, repository, run_id, run_attempt, commit, workflow, max_age_hours=3):
    expected_fields = {'schema_version', 'repository', 'run_id', 'run_attempt', 'commit', 'workflow', 'checked_at', 'checks'}
    if not isinstance(report, dict) or set(report) != expected_fields or report['schema_version'] != 1:
        raise ValueError('Unrecognized health report')
    for name, expected in dict(repository=repository, run_id=str(run_id), run_attempt=run_attempt, commit=commit, workflow=workflow).items():
        if report[name] != expected:
            raise ValueError('Health report provenance mismatch')
    age = (now - timestamp(report['checked_at'])).total_seconds()
    if not -300 <= age <= max_age_hours * 3600:
        raise ValueError('Health report is stale or future-dated')
    checks = report['checks']
    if not isinstance(checks, list) or not 1 <= len(checks) <= 32:
        raise ValueError('Invalid health checks')
    seen = set()
    for row in checks:
        if not isinstance(row, dict) or set(row) != {'provider', 'slot', 'status', 'signals'}:
            raise ValueError('Unsafe health check fields')
        if row['provider'] not in ENDPOINTS or not re.fullmatch(r'[A-Z][A-Z0-9_]{0,63}', row['slot']):
            raise ValueError('Invalid health slot')
        identity = (row['provider'], row['slot'])
        signals = row['signals']
        if identity in seen or not isinstance(signals, list) or not signals or any(s not in STATUSES for s in signals):
            raise ValueError('Invalid health status')
        if signals != sorted(set(signals), key=STATUSES.index) or row['status'] != signals[0] or ('healthy' in signals and len(signals) != 1):
            raise ValueError('Inconsistent health status')
        seen.add(identity)
    return report


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--key', action='append', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--workflow', default='.github/workflows/provider-api-health.yml')
    args = parser.parse_args()
    report = probe(args.key, os.environ, workflow=args.workflow)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, sort_keys=True, indent=2) + '\n', encoding='utf-8')
    for check in report['checks']:
        print(f"{check['provider']} {check['slot']}: {','.join(check['signals'])}")
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception:
        # Tracebacks from a HTTP library may expose a credential-shaped value.
        print('Provider health monitor could not create a valid report.')
        raise SystemExit(1)
