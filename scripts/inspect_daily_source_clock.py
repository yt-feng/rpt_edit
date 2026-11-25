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
CHECK_KEY = '_account/ops/daily-source-clock-check.json'
UPSTREAM_CHECK_KEY = '_account/ops/drive-source-clock-check.json'
MAX_RECEIPT_BYTES = 8192
RECEIPT_STATES = {'dispatching', 'accepted', 'observed', 'unknown', 'rejected'}
CHECK_STATES = RECEIPT_STATES | {'before_daily_start', 'unconfigured', 'inspection_unavailable',
    'wake_active', 'wake_recent', 'dispatch_cooldown', 'dispatch_claimed', 'receipt_unavailable'}


def utc_stamp(value):
    if not isinstance(value, str) or not re.fullmatch(
            r'[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(?:\.[0-9]{1,6})?Z', value):
        raise ValueError
    datetime.fromisoformat(value.replace('Z', '+00:00'))
    return value


def safe_receipt(raw):
    """Whitelist evidence fields, including when an object has unrelated data."""
    try:
        row = json.loads(raw)
        if not isinstance(row, dict) or row.get('state') not in RECEIPT_STATES:
            raise ValueError
        requested = utc_stamp(row.get('requested_at'))
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


def safe_check(raw):
    try:
        row = json.loads(raw)
        if not isinstance(row, dict) or row.get('state') not in CHECK_STATES:
            raise ValueError
        result = {'clock_check_state': row['state'], 'clock_checked_at': utc_stamp(row.get('checked_at'))}
        run = row.get('run_id')
        if run is not None:
            if type(run) is not int or not 1 <= run <= 2**53 - 1:
                raise ValueError
            result['clock_run_id'] = run
        if row['state'] in {'wake_active', 'wake_recent', 'observed'} and run is None:
            raise ValueError
        return result
    except (ValueError, TypeError, OverflowError):
        return {'clock_check_state': 'invalid'}


UPSTREAM_CHECK_STATES = {'unconfigured', 'inspection_unavailable', 'sync_active', 'sync_completed',
    'awaiting_dispatch_readback', 'receipt_unavailable', 'sync_retry_wait', 'retry_limit',
    'dispatch_claimed', 'accepted', 'rejected', 'unknown'}


def safe_upstream_check(raw):
    try:
        row = json.loads(raw)
        if not isinstance(row, dict) or row.get('state') not in UPSTREAM_CHECK_STATES:
            raise ValueError
        day = row.get('date_folder')
        if not isinstance(day, str) or not re.fullmatch(r'[0-9]{6}', day):
            raise ValueError
        datetime.strptime('20' + day, '%Y%m%d')
        result = {'upstream_sync_state': row['state'],
                  'upstream_checked_at': utc_stamp(row.get('checked_at')), 'upstream_batch_date': day}
        run = row.get('run_id')
        if run is not None:
            if type(run) is not int or not 1 <= run <= 2**53 - 1:
                raise ValueError
            result['upstream_run_id'] = run
        if row['state'] in {'sync_active', 'sync_completed'} and run is None:
            raise ValueError
        return result
    except (ValueError, TypeError, OverflowError):
        return {'upstream_sync_state': 'invalid'}


def read_receipt(client, bucket, *, heartbeat=False, upstream=False):
    if upstream:
        key, field, normalize = UPSTREAM_CHECK_KEY, 'upstream_sync_state', safe_upstream_check
    elif heartbeat:
        key, field, normalize = CHECK_KEY, 'clock_check_state', safe_check
    else:
        key, field, normalize = RECEIPT_KEY, 'receipt_state', safe_receipt
    body = None
    try:
        response = client.get_object(Bucket=bucket, Key=key)
        body = response['Body']
        raw = body.read(MAX_RECEIPT_BYTES + 1)
        if not isinstance(raw, bytes) or len(raw) > MAX_RECEIPT_BYTES:
            return {field: 'invalid'}
        return normalize(raw)
    except Exception as error:
        response = getattr(error, 'response', {})
        details = response.get('Error', {}) if isinstance(response, dict) else {}
        code = details.get('Code') if isinstance(details, dict) else None
        if code in {'NoSuchKey', 'NotFound', '404'}:
            return {field: 'not_observed'}
        return {field: 'unavailable'}
    finally:
        if body is not None:
            with suppress(Exception):
                body.close()


def inspect_clock(api_factory, client_factory, bucket_getter, *, upstream=False):
    result = {'inspection_state': 'read_only'}
    try:
        schedules = api_factory().get()
        result['schedule_state'] = 'half_hourly_verified' if schedules == [HALF_HOURLY] else 'mismatch'
    except Exception:
        result['schedule_state'] = 'unavailable'
    try:
        client, bucket = client_factory(), bucket_getter()
        result.update(read_receipt(client, bucket))
        result.update(read_receipt(client, bucket, heartbeat=True))
        if upstream:
            result.update(read_receipt(client, bucket, upstream=True))
    except Exception:
        result.setdefault('receipt_state', 'unavailable')
        result.setdefault('clock_check_state', 'unavailable')
        if upstream:
            result.setdefault('upstream_sync_state', 'unavailable')
    return result


def main():
    result = inspect_clock(
        lambda: ScheduleApi(os.environ.get('CLOUDFLARE_ACCOUNT_ID', ''),
                            'portal-daily-source-clock', os.environ.get('CLOUDFLARE_API_TOKEN', '')),
        build_r2_client, r2_bucket, upstream=bool(os.environ.get('REPORT_UPSTREAM_SYNC_REPO')))
    print(json.dumps(result, sort_keys=True), flush=True)
    # A new clock may legitimately have no receipt before its first eligible
    # tick. A successful read does not claim a wake or a Daily delivery occurred.
    return int(result['schedule_state'] != 'half_hourly_verified'
               or result['receipt_state'] in {'invalid', 'unavailable'}
               or result['clock_check_state'] in {'invalid', 'unavailable'}
               or result.get('upstream_sync_state') in {'invalid', 'unavailable'})


if __name__ == '__main__':
    raise SystemExit(main())
