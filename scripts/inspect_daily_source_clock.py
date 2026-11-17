#!/usr/bin/env python3
"""Read the independent clock's cron and the shared wake-up receipt; never write."""
from __future__ import annotations

from contextlib import suppress
from datetime import datetime
import json
import os
import re

from private_workflow_handoff import build_r2_client, r2_bucket
from sync_portal_worker_schedules import HALF_HOURLY, ScheduleApi

RECEIPT_KEY = '_account/ops/daily-source-wakeup.json'
MAX_RECEIPT_BYTES = 8192
RECEIPT_STATES = {'dispatching', 'accepted', 'observed', 'unknown', 'rejected'}


def safe_receipt(raw):
    """Whitelist evidence fields, including when an object has unrelated data."""
    try:
        row = json.loads(raw)
        if not isinstance(row, dict) or row.get('state') not in RECEIPT_STATES:
            raise ValueError
        requested = row.get('requested_at')
        if not isinstance(requested, str) or not re.fullmatch(
                r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,6})?Z', requested):
            raise ValueError
        datetime.fromisoformat(requested.replace('Z', '+00:00'))
        result = {'receipt_state': row['state'], 'requested_at': requested}
        for field in ('run_id', 'previous_dispatch_run_id'):
            value = row.get(field)
            if value is not None:
                lower = 1 if field == 'run_id' else 0
                if type(value) is not int or not lower <= value <= 2**53 - 1:
                    raise ValueError
                result[field] = value
        if row['state'] == 'observed' and not result.get('run_id'):
            raise ValueError
        return result
    except (ValueError, TypeError, OverflowError):
        return {'receipt_state': 'invalid'}


def read_receipt(client, bucket):
    body = None
    try:
        response = client.get_object(Bucket=bucket, Key=RECEIPT_KEY)
        body = response['Body']
        raw = body.read(MAX_RECEIPT_BYTES + 1)
        if not isinstance(raw, bytes) or len(raw) > MAX_RECEIPT_BYTES:
            return {'receipt_state': 'invalid'}
        return safe_receipt(raw)
    except Exception as error:
        response = getattr(error, 'response', {})
        details = response.get('Error', {}) if isinstance(response, dict) else {}
        code = details.get('Code') if isinstance(details, dict) else None
        if code in {'NoSuchKey', 'NotFound', '404'}:
            return {'receipt_state': 'not_observed'}
        return {'receipt_state': 'unavailable'}
    finally:
        if body is not None:
            with suppress(Exception):
                body.close()


def inspect_clock(api_factory, client_factory, bucket_getter):
    result = {'inspection_state': 'read_only'}
    try:
        schedules = api_factory().get()
        result['schedule_state'] = 'half_hourly_verified' if schedules == [HALF_HOURLY] else 'mismatch'
    except Exception:
        result['schedule_state'] = 'unavailable'
    try:
        result.update(read_receipt(client_factory(), bucket_getter()))
    except Exception:
        result['receipt_state'] = 'unavailable'
    return result


def main():
    result = inspect_clock(
        lambda: ScheduleApi(os.environ.get('CLOUDFLARE_ACCOUNT_ID', ''),
                            'portal-daily-source-clock', os.environ.get('CLOUDFLARE_API_TOKEN', '')),
        build_r2_client, r2_bucket)
    print(json.dumps(result, sort_keys=True), flush=True)
    # A new clock may legitimately have no receipt before its first eligible
    # tick. A successful read does not claim a wake or a Daily delivery occurred.
    return int(result['schedule_state'] != 'half_hourly_verified'
               or result['receipt_state'] in {'invalid', 'unavailable'})


if __name__ == '__main__':
    raise SystemExit(main())
