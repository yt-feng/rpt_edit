#!/usr/bin/env python3
"""Cloud-only, read-only diagnostics for cached MinerU responses and result URLs."""
from __future__ import annotations

import base64
from collections import Counter
from datetime import datetime, timezone
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import ssl
import urllib.error
import urllib.parse
import urllib.request

import check_mineru_key_expiry as key_monitor
from consume_legacy_mineru import MAX_ZIP, valid_url
from inspect_durable_mineru import error_category
from inspect_legacy_mineru import MAX_BODY, NoRedirect, canonical, classify_response, valid_uuid, validate_request
from persist_legacy_mineru_inspection import MAX_OBJECT, single_attempt_store

WORKFLOW = '.github/workflows/mineru-api-diagnostics.yml'
PREFIX = '_workflow-cache/mineru-legacy-inspections/v1'
HEX64 = re.compile(r'[a-f0-9]{64}')
DECIMAL = re.compile(r'[1-9][0-9]{0,19}')
# Fixed codes from https://mineru.net/apiManage/docs (common error codes).
# The code meaning and actual response words remain separate diagnostics.
DOCUMENTED_CODES = {
    -500: 'invalid_parameters', -10001: 'provider_unavailable', -10002: 'invalid_parameters',
    -60001: 'upload_url_failure', -60002: 'unsupported_file', -60003: 'file_read_failure',
    -60004: 'empty_file', -60005: 'file_size_limit', -60006: 'page_limit',
    -60007: 'model_service_unavailable', -60008: 'file_read_timeout', -60009: 'queue_full',
    -60010: 'parse_failure', -60011: 'valid_file_missing', -60012: 'task_not_found',
    -60013: 'task_permission_denied', -60014: 'running_task_delete_rejected',
    -60015: 'conversion_failure', -60016: 'conversion_failure', -60017: 'provider_retry_limit',
    -60018: 'daily_quota', -60019: 'html_quota', -60020: 'file_split_failure',
    -60021: 'page_count_failure', -60022: 'web_page_read_failure',
}


class DiagnosticError(ValueError):
    """Only a fixed diagnostic category may cross the public boundary."""


def checksum(raw):
    return hashlib.sha256(raw).hexdigest()


def decode(raw, maximum):
    if not isinstance(raw, bytes) or not 0 < len(raw) <= maximum:
        raise DiagnosticError('object_bounds')
    def pairs(items):
        value = {}
        for key, item in items:
            if key in value:
                raise DiagnosticError('object_duplicate_keys')
            value[key] = item
        return value
    try:
        return json.loads(raw, object_pairs_hook=pairs)
    except DiagnosticError:
        raise
    except (UnicodeError, ValueError):
        raise DiagnosticError('object_json') from None


def validate_identity(value):
    if not isinstance(value, dict) or set(value) != {'inspection_run_id', 'inspection_attempt', 'input_sha256', 'receipt_sha256'}:
        raise DiagnosticError('snapshot_identity')
    if any(not isinstance(value[name], str) or not DECIMAL.fullmatch(value[name])
           for name in ('inspection_run_id', 'inspection_attempt')):
        raise DiagnosticError('snapshot_producer')
    if any(not isinstance(value[name], str) or not HEX64.fullmatch(value[name])
           for name in ('input_sha256', 'receipt_sha256')):
        raise DiagnosticError('snapshot_hash')
    return value


def load_snapshot(identity, store):
    """Validate every cached response and exact membership before live probes."""
    validate_identity(identity)
    context = identity['inspection_run_id'] + '-' + identity['inspection_attempt']
    receipt_key = store.key(context, identity['input_sha256'], 'receipt-' + identity['receipt_sha256'] + '.json')
    raw = store._get(receipt_key, maximum=256 * 1024)
    if checksum(raw) != identity['receipt_sha256']:
        raise DiagnosticError('receipt_checksum')
    receipt = decode(raw, 256 * 1024)
    if (not isinstance(receipt, dict) or type(receipt.get('schema_version')) is not int
            or receipt['schema_version'] != 1 or receipt.get('policy') != 'legacy-provider-inspection-only-v1'
            or any(receipt.get(field) is not False for field in ('canonical_task_admission', 'original_source_bytes_proven', 'historical_token_fingerprint_proven'))):
        raise DiagnosticError('receipt_contract')
    producer = receipt.get('producer')
    if (not isinstance(producer, dict) or set(producer) != {'run_id', 'attempt', 'sha'}
            or producer['run_id'] != identity['inspection_run_id'] or producer['attempt'] != identity['inspection_attempt']
            or not isinstance(producer['sha'], str) or not re.fullmatch(r'[a-f0-9]{40}', producer['sha'])):
        raise DiagnosticError('receipt_producer')
    try:
        request = validate_request(receipt['input'])
    except (KeyError, ValueError):
        raise DiagnosticError('receipt_membership') from None
    if checksum(canonical(request)) != identity['input_sha256'] or receipt.get('input_canonical_sha256') != identity['input_sha256']:
        raise DiagnosticError('receipt_input_hash')
    requested = {row['batch_id']: row for row in request['batches']}
    objects = receipt.get('objects')
    if not isinstance(objects, list) or len(objects) != len(requested):
        raise DiagnosticError('snapshot_incomplete')
    seen, responses = set(), []
    for item in objects:
        if not isinstance(item, dict) or set(item) != {'batch_id', 'object', 'sha256', 'bytes'}:
            raise DiagnosticError('response_identity')
        batch_id, digest = item['batch_id'], item['sha256']
        if (not valid_uuid(batch_id) or batch_id not in requested or batch_id in seen
                or not isinstance(digest, str) or not HEX64.fullmatch(digest)
                or type(item['bytes']) is not int or not 0 < item['bytes'] <= MAX_OBJECT):
            raise DiagnosticError('response_identity')
        expected = f'{context}/{identity["input_sha256"]}/{batch_id}-{digest}.json'
        if item['object'] != expected:
            raise DiagnosticError('response_path')
        body = store._get(store.key(*expected.split('/')), maximum=MAX_OBJECT)
        if len(body) != item['bytes'] or checksum(body) != digest:
            raise DiagnosticError('response_checksum')
        value = decode(body, MAX_OBJECT)
        if (not isinstance(value, dict) or canonical(value.get('input')) != canonical(requested[batch_id])
                or value.get('input_canonical_sha256') != checksum(canonical(requested[batch_id]))
                or type(value.get('http_status')) is not int):
            raise DiagnosticError('response_binding')
        encoded = value.get('raw_response_base64')
        if not isinstance(encoded, str) or len(encoded) > 4 * ((MAX_BODY + 2) // 3):
            raise DiagnosticError('response_bounds')
        try:
            response_raw = base64.b64decode(encoded, validate=True)
        except ValueError:
            raise DiagnosticError('response_encoding') from None
        if len(response_raw) > MAX_BODY or checksum(response_raw) != value.get('response_sha256'):
            raise DiagnosticError('provider_response_checksum')
        decode(response_raw, MAX_BODY)
        public, private = classify_response(value['http_status'], response_raw, requested[batch_id])
        if (not public.get('membership_proven') or not public.get('identified_complete')
                or canonical(private.get('provider_response')) != canonical(value.get('provider_response'))):
            raise DiagnosticError('provider_response_membership')
        seen.add(batch_id)
        responses.append(private['provider_response']['data']['extract_result'])
    if seen != set(requested):
        raise DiagnosticError('snapshot_incomplete')
    return [row for rows in responses for row in rows]


def public_code(value):
    """Arbitrary provider strings cannot masquerade as safe error codes."""
    if value is None:
        return {'code': None}
    if value == '0':
        return {'code': 0}
    if (type(value) is int and value in DOCUMENTED_CODES
            or isinstance(value, str) and value in {str(code) for code in DOCUMENTED_CODES}):
        code = int(value)
        return {'code': code, 'documented_code_reason': DOCUMENTED_CODES[code]}
    if isinstance(value, str) and re.fullmatch(r'[AR][0-9]{4}', value.strip().upper()):
        return {'code': value.strip().upper()}
    if type(value) is int and (value == 0 or 100 <= value <= 599):
        return {'code': value}
    return {'code': None, 'code_sha256': checksum(canonical(value))}


def normalize_reason(message):
    """Classify actual provider words, without inferring from current quotas."""
    if not isinstance(message, str):
        return 'other_provider_failure'
    text = message.lower()
    if re.search(r'rate.{0,20}limit|too many requests|频率|限流', text):
        return 'rate_limit'
    if re.search(r'(priority|优先).{0,60}(quota|limit|page|exceed|exhaust|配额|额度|页|上限)|(quota|limit|配额|额度).{0,40}(priority|优先)', text):
        return 'priority_quota'
    if re.search(r'(daily|per.day|每日|当天).{0,40}(quota|limit|page|file|额度|配额|页|文件)|(quota|limit|额度|配额).{0,40}(daily|per.day|每日|当天)', text):
        return 'daily_quota'
    if re.search(r'quota|balance|credit|额度|余额|配额', text):
        return 'overall_quota'
    if re.search(r'queue.{0,20}(full|limit)|队列.{0,20}(满|上限)', text):
        return 'queue_full'
    if re.search(r'retr(?:y|ies).{0,25}(limit|exceed|exhaust)|重试.{0,20}(上限|次数)', text):
        return 'provider_retry_limit'
    if re.search(r'(model|service).{0,25}unavailable|模型服务暂时不可用|服务暂时不可用', text):
        return 'provider_unavailable'
    if re.search(r'pars(?:e|ing).{0,25}fail|convert.{0,25}fail|process.{0,25}(fail|error)|internal|unexpected|解析失败|服务异常|任务失败', text):
        return 'provider_internal'
    return error_category({'err_msg': message})


def historical_summary(rows):
    states, failures = Counter(row['state'] for row in rows), Counter()
    for row in rows:
        if row['state'] != 'failed':
            continue
        message = row.get('err_msg') or row.get('error') or row.get('message')
        code = row.get('err_code', row.get('error_code', row.get('code')))
        reason = normalize_reason(message)
        detail = {'reason': reason, **public_code(code)}
        if reason == 'other_provider_failure':
            detail['reason_known'] = False
        else:
            detail['reason_known'] = True
        failures[canonical(detail)] += 1
    return {'source': 'verified_cached_provider_responses', 'observed_files': len(rows),
            'state_counts': dict(states), 'failures': [json.loads(key) | {'count': count} for key, count in failures.items()],
            'original_source_bytes_proven': False, 'historical_token_fingerprint_proven': False,
            'all_cached_tasks_succeeded': states.get('failed', 0) == 0 and states.get('done', 0) == len(rows)}


def authentication_summary(env, opener):
    results, stopped = [], False
    now = datetime.now(timezone.utc)
    for slot in key_monitor.collect_configured_slots(env):
        if stopped:
            results.append({'slot': slot.env_name, 'probe_state': 'uninspected_after_network_stop'})
            continue
        errors = []
        def open_probe(request, **kwargs):
            try:
                return opener(request, **kwargs)
            except urllib.error.HTTPError as error:
                errors.append(error)
                raise
            except http.client.HTTPException:
                raise urllib.error.URLError('network_stop') from None
        try:
            probe = key_monitor.probe_token(slot.token, opener=open_probe,
                                            api_base_url=key_monitor.DEFAULT_MINERU_BASE_URL, timeout=20)
        finally:
            # The existing monitor reads HTTP errors but does not close them.
            # Closing here keeps this one-shot diagnostic bounded on all exits.
            for error in errors:
                error.close()
        # Reuse the fixed GET probe without accepting an arbitrary application
        # error as proof of authentication. No parsing capacity is established.
        state = probe.state
        if state == 'valid':
            accepted = (probe.code in {'A0204', 'A0301', '-60012'} and (200 <= probe.http_status < 300 or probe.http_status in {400, 404})
                        or (probe.code in {'', '0'} and 200 <= probe.http_status < 300))
            if not accepted:
                state = 'unknown'
        expiry, source, malformed = key_monitor.resolve_expiry(slot)
        expiry_state, _, days = key_monitor.expiry_evaluation(expiry, now=now, malformed=malformed)
        results.append({'slot': slot.env_name, 'probe_state': state, 'http_status': probe.http_status,
                        **public_code(probe.code or None), 'expiry_state': expiry_state, 'days_remaining': days})
        stopped = probe.http_status is None
    return {'configured_count': len(results), 'slots': results, 'network_stop': stopped,
            'probe': 'synthetic_nonexistent_batch_get', 'quota_or_parse_capacity_verified': False}


def _content_length(headers):
    value = headers.get('Content-Length')
    if value is None:
        return None
    if not isinstance(value, str) or not re.fullmatch(r'[0-9]{1,12}', value) or not 0 < int(value) <= MAX_ZIP:
        raise DiagnosticError('content_length_bounds')
    return int(value)


def _transport_category(error):
    reason = error.reason if isinstance(error, urllib.error.URLError) else error
    if isinstance(reason, ssl.SSLCertVerificationError):
        return 'certificate_expired' if getattr(reason, 'verify_code', None) == 10 else 'certificate_verification_failed'
    return 'network_stop'


def result_summary(rows, opener, stream_probe):
    url = next((row.get('full_zip_url') for row in rows if row['state'] == 'done'), None)
    result = {'selection': 'first_done_in_verified_snapshot', 'head_requests': 0, 'stream_get_requests': 0,
              'full_zip_verified': False, 'full_zip_downloaded': False, 'network_stop': False}
    if url is None:
        return result | {'status': 'no_done_result'}
    try:
        valid_url(url)
    except ValueError:
        return result | {'status': 'unsafe_result_url'}
    result['host'] = urllib.parse.urlsplit(url).hostname
    headers = {'User-Agent': 'mineru-api-diagnostics/1.0'}
    result['head_requests'] = 1
    try:
        try:
            response = opener(urllib.request.Request(url, headers=headers, method='HEAD'), timeout=20)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            status = response.getcode()
            result.update(head_http_status=status, tls='verified', status='tls_only')
            length = _content_length(response.headers)
            result['head_content_length'] = length
        if not stream_probe or status not in (200, 405):
            return result
        result['stream_get_requests'] = 1
        try:
            response = opener(urllib.request.Request(url, headers=headers | {'Range': 'bytes=0-3'}, method='GET'), timeout=20)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            get_status = response.getcode()
            result['stream_http_status'] = get_status
            length = _content_length(response.headers)
            result['stream_content_length'] = length
            if get_status not in (200, 206):
                return result | {'status': 'result_http_unavailable'}
            prefix = response.read(4)
            if len(prefix) != 4 or (length is not None and length < 4):
                return result | {'status': 'incomplete_zip_prefix', 'bytes_read': len(prefix)}
            result.update(zip_magic_observed=prefix == b'PK\x03\x04', bytes_read=4,
                          status='zip_prefix_readable' if prefix == b'PK\x03\x04' else 'invalid_zip_prefix')
    except DiagnosticError as error:
        result['status'] = str(error)
    except (urllib.error.URLError, OSError, TimeoutError, http.client.HTTPException) as error:
        category = _transport_category(error)
        result.update(status=category, tls=category, network_stop=True)
    return result


def diagnose(identity, store, env, *, opener=None, stream_probe=True):
    rows = load_snapshot(identity, store)
    # The default HTTPS handler validates certificates; NoRedirect forbids auth
    # or signed URLs following an unverified redirect. No caller retries here.
    open_once = opener or urllib.request.build_opener(NoRedirect()).open
    historical = historical_summary(rows)
    authentication = authentication_summary(env, open_once)
    download = ({'status': 'uninspected_after_network_stop', 'head_requests': 0, 'stream_get_requests': 0,
                 'full_zip_verified': False, 'full_zip_downloaded': False, 'network_stop': True}
                if authentication['network_stop'] else result_summary(rows, open_once, stream_probe))
    return {'schema_version': 1, 'status': 'diagnostic_complete', 'historical_tasks': historical,
            'authentication': authentication, 'result_download': download,
            'provider_posts': 0, 'new_submissions': 0, 'canonical_ledger_writes': 0, 'emails_sent': 0,
            'network_stop': authentication['network_stop'] or download['network_stop']}


def main(env=None, *, store_factory=single_attempt_store, opener=None):
    env = os.environ if env is None else env
    expected = env.get('GITHUB_REPOSITORY', '') + '/' + WORKFLOW + '@refs/heads/main'
    if (env.get('GITHUB_ACTIONS') != 'true' or env.get('GITHUB_REF') != 'refs/heads/main'
            or env.get('GITHUB_EVENT_NAME') != 'workflow_dispatch' or env.get('GITHUB_WORKFLOW_REF') != expected):
        print(json.dumps({'status': 'diagnostic_rejected', 'category': 'reviewed_main_cloud_workflow_required'}))
        return 1
    stage = 'input'
    try:
        identity = validate_identity({name: env.get(name.upper(), '') for name in
                                      ('inspection_run_id', 'inspection_attempt', 'input_sha256', 'receipt_sha256')})
        if env.get('STREAM_PROBE', 'true') not in {'true', 'false'}:
            raise DiagnosticError('stream_probe_input')
        stage = 'snapshot_and_probes'
        report = diagnose(identity, store_factory(), env, opener=opener, stream_probe=env.get('STREAM_PROBE', 'true') == 'true')
        encoded = json.dumps(report, sort_keys=True) + '\n'
        Path(env['RUNNER_TEMP'], 'mineru-api-diagnostics.json').write_text(encoded)
        if env.get('GITHUB_STEP_SUMMARY'):
            auth, old, download = report['authentication'], report['historical_tasks'], report['result_download']
            summary = (f"MinerU authentication: {auth['configured_count']} configured slots; "
                       f"network_stop={auth['network_stop']}\n\n"
                       f"Historical cached tasks: {old['state_counts']}; reasons are provider diagnostics.\n\n"
                       f"Result download probe: {download['status']}; full ZIP verified=false.\n\n"
                       "Provider POST=0; canonical ledger writes=0; emails=0.\n")
            with Path(env['GITHUB_STEP_SUMMARY']).open('a') as output:
                output.write(summary)
        print(encoded, end='')
        return 2 if report['network_stop'] else 0
    except Exception as error:
        category = str(error) if isinstance(error, DiagnosticError) else 'diagnostic_unavailable'
        print(json.dumps({'status': 'diagnostic_rejected', 'stage': stage, 'category': category,
                          'exception_class': type(error).__name__, 'provider_posts': 0, 'canonical_ledger_writes': 0}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
