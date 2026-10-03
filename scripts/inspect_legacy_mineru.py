"""Single-read legacy MinerU audit. This module cannot submit or adopt tasks."""
from __future__ import annotations

import argparse
import base64
from collections import Counter
import hashlib
import http.client
import json
import os
from pathlib import Path
import re
import urllib.error
import urllib.request
import uuid

MAX_BODY = 1024 * 1024
MAX_ROWS = 200
SLOTS = {'MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4'}
STATES = {'pending', 'running', 'converting', 'waiting-file', 'done', 'failed'}
TERMINAL = {'done', 'failed'}
ENDPOINT = 'https://mineru.net/api/v4/extract-results/batch/'
ID_RE = re.compile(r'[A-Za-z0-9._-]{1,128}', re.ASCII)
DECIMAL_ID_RE = re.compile(r'[1-9][0-9]{0,19}', re.ASCII)
ROW_KEYS = {'batch_id', 'credential_slot', 'expected_data_ids', 'job_id', 'run_id'}


class InputError(ValueError):
    pass


class NetworkStop(RuntimeError):
    """Deliberately excludes transport exception text and request credentials."""


class ResponseBounds(ValueError):
    pass


def canonical(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def sha256(raw):
    return hashlib.sha256(raw).hexdigest()


def valid_uuid(value):
    if not isinstance(value, str):
        return False
    try:
        parsed = uuid.UUID(value)
    except (ValueError, AttributeError):
        return False
    return str(parsed) == value and parsed.version == 4


def validate_request(value):
    if not isinstance(value, dict) or set(value) != {'schema_version', 'batches'}:
        raise InputError('request_keys')
    if type(value['schema_version']) is not int or value['schema_version'] != 1:
        raise InputError('schema')
    batches = value['batches']
    if not isinstance(batches, list) or not 1 <= len(batches) <= 100:
        raise InputError('batch_count')
    seen = set()
    for row in batches:
        if not isinstance(row, dict) or set(row) != ROW_KEYS:
            raise InputError('batch_keys')
        if not valid_uuid(row['batch_id']) or row['batch_id'] in seen:
            raise InputError('batch_identity')
        seen.add(row['batch_id'])
        if not isinstance(row['credential_slot'], str) or row['credential_slot'] not in SLOTS:
            raise InputError('credential_slot')
        for key in ('run_id', 'job_id'):
            if not isinstance(row[key], str) or not DECIMAL_ID_RE.fullmatch(row[key]):
                raise InputError('run_job_identity')
        ids = row['expected_data_ids']
        if (not isinstance(ids, list) or len(ids) > MAX_ROWS
                or any(not isinstance(item, str) or not ID_RE.fullmatch(item) for item in ids)
                or len(ids) != len(set(ids))):
            raise InputError('original_membership')
    return value


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        return None


def get_once(endpoint, token, timeout):
    """Fixed GET endpoint, bounded response, no retries or redirects."""
    batch_id = endpoint.removeprefix(ENDPOINT)
    if not endpoint.startswith(ENDPOINT) or not valid_uuid(batch_id):
        raise InputError('endpoint')
    if type(timeout) is not int or not 10 <= timeout <= 30:
        raise InputError('timeout')
    opener = urllib.request.build_opener(NoRedirect())
    request = urllib.request.Request(endpoint, headers={'Authorization': 'Bearer ' + token}, method='GET')
    try:
        try:
            response = opener.open(request, timeout=timeout)
        except urllib.error.HTTPError as error:
            response = error
        with response:
            status = response.status
            header = response.headers.get('Content-Length')
            if header is not None:
                if not re.fullmatch(r'[0-9]{1,10}', header) or int(header) > MAX_BODY:
                    raise ResponseBounds('response_size')
            raw = response.read(MAX_BODY + 1)
            if len(raw) > MAX_BODY:
                raise ResponseBounds('response_size')
            if header is not None and len(raw) != int(header):
                raise NetworkStop('network_stop')
            return status, raw
    except (urllib.error.URLError, OSError, TimeoutError, http.client.HTTPException) as error:
        raise NetworkStop('network_stop') from error


def classify_response(status, raw, batch):
    """No provider text, file IDs or result URLs enter the public receipt."""
    public = {key: batch[key] for key in ('run_id', 'job_id', 'batch_id')}
    public.update(requested_member_count=len(batch['expected_data_ids']), observed_count=0,
                  membership_proven=False, identified_complete=False, all_succeeded=False,
                  original_source_bytes_proven=False, historical_token_fingerprint_proven=False,
                  response_sha256=sha256(raw))
    private = {'input': batch, 'input_canonical_sha256': sha256(canonical(batch)),
               'http_status': status, 'response_sha256': sha256(raw)}
    if len(raw) > MAX_BODY:
        public['category'] = 'response_size'
        return public, private
    private['raw_response_base64'] = base64.b64encode(raw).decode()
    if type(status) is not int:
        public['category'] = 'invalid_http_status'
        return public, private
    if status != 200:
        public['category'] = {403: 'http_forbidden', 404: 'http_not_found', 401: 'http_unauthorized'}.get(
            status, 'http_redirect_blocked' if 300 <= status <= 399 else 'http_application_error')
        return public, private
    try:
        payload = json.loads(raw)
    except (ValueError, UnicodeError):
        public['category'] = 'invalid_json'
        return public, private
    private['provider_response'] = payload
    code = payload.get('code') if isinstance(payload, dict) else object()
    data = payload.get('data') if isinstance(payload, dict) else None
    if (not (type(code) is int and code == 0 or type(code) is str and code == '0')
            or not isinstance(data, dict) or data.get('batch_id', batch['batch_id']) != batch['batch_id']):
        public['category'] = 'provider_contract'
        return public, private
    rows = data.get('extract_result')
    if not isinstance(rows, list) or len(rows) > MAX_ROWS:
        public['category'] = 'response_row_count'
        return public, private
    public['observed_count'] = len(rows)
    seen = []
    states = Counter()
    invalid = 0
    done_url_missing = 0
    for row in rows:
        if not isinstance(row, dict):
            invalid += 1
            continue
        identity, state = row.get('data_id'), row.get('state')
        if not isinstance(identity, str) or not ID_RE.fullmatch(identity) or not isinstance(state, str) or state not in STATES:
            invalid += 1
            continue
        seen.append(identity)
        states[state] += 1
        if state == 'done' and (not isinstance(row.get('full_zip_url'), str)
                               or not row['full_zip_url'].startswith('https://')):
            done_url_missing += 1
    expected = set(batch['expected_data_ids'])
    observed = set(seen)
    public.update(state_counts=dict(sorted(states.items())), invalid_row_count=invalid,
                  duplicate_member_count=len(seen) - len(observed),
                  missing_member_count=len(expected - observed),
                  unknown_member_count=len(observed - expected) if expected else 0,
                  completed_result_url_missing_count=done_url_missing)
    membership = bool(expected) and not invalid and len(seen) == len(rows) and len(seen) == len(observed) and observed == expected
    complete = membership and sum(states[state] for state in TERMINAL) == len(expected)
    public.update(membership_proven=membership, identified_complete=complete,
                  all_succeeded=complete and states['done'] == len(expected) and not done_url_missing,
                  category='identified' if membership else 'membership_unknown' if not expected else 'membership_mismatch')
    return public, private


def inspect_batches(value, credentials, *, timeout=20, getter=get_once):
    validate_request(value)
    if type(timeout) is not int or not 10 <= timeout <= 30:
        raise InputError('timeout')
    input_hash = sha256(canonical(value))
    public = {'schema_version': 1, 'input_canonical_sha256': input_hash, 'batches': [],
              'network_stop': False, 'provider_gets': 0, 'provider_posts': 0,
              'paid_requests': 0, 'new_submissions': 0}
    private = {'schema_version': 1, 'input': value, 'input_canonical_sha256': input_hash, 'batches': []}
    for batch in value['batches']:
        minimal = {key: batch[key] for key in ('run_id', 'job_id', 'batch_id')}
        minimal.update(identified_complete=False, all_succeeded=False, membership_proven=False,
                       original_source_bytes_proven=False, historical_token_fingerprint_proven=False)
        token = credentials.get(batch['credential_slot'])
        if (not isinstance(token, str) or not token.strip() or len(token) > 8192
                or any(ord(char) < 33 or ord(char) > 126 for char in token.strip())):
            public['batches'].append(minimal | {'category': 'credential_unavailable'})
            continue
        public['provider_gets'] += 1
        try:
            status, raw = getter(ENDPOINT + batch['batch_id'], token.strip(), timeout)
        except NetworkStop:
            public['network_stop'] = True
            public['batches'].append(minimal | {'category': 'network_stop'})
            break
        except ResponseBounds:
            public['batches'].append(minimal | {'category': 'response_size'})
            continue
        row, original = classify_response(status, raw, batch)
        public['batches'].append(row)
        private['batches'].append(original)
    public['uninspected_count'] = len(value['batches']) - len(public['batches'])
    return public, private


def write_private(path, value):
    descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC | os.O_NOFOLLOW, 0o600)
    os.fchmod(descriptor, 0o600)
    with os.fdopen(descriptor, 'w') as stream:
        json.dump(value, stream, ensure_ascii=False, sort_keys=True)
        stream.write('\n')


def main():
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
        or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
        or os.environ.get('GITHUB_WORKFLOW_REF') != os.environ.get('GITHUB_REPOSITORY', '')+
           '/.github/workflows/mineru-legacy-inspect.yml@refs/heads/main'):
        print('Legacy MinerU inspection is restricted to GitHub Actions.')
        return 1
    parser = argparse.ArgumentParser()
    parser.add_argument('--input', type=Path, required=True)
    parser.add_argument('--public-summary', type=Path, required=True)
    parser.add_argument('--private-result', type=Path, required=True)
    parser.add_argument('--timeout', type=int, default=20)
    args = parser.parse_args()
    try:
        with args.input.open('rb') as stream:
            raw = stream.read(65536 + 1)
        if len(raw) > 65536:
            raise InputError('input_size')
        credentials = {slot: os.environ.get(slot) for slot in SLOTS}
        public, private = inspect_batches(json.loads(raw), credentials, timeout=args.timeout)
        write_private(args.private_result, private)
        args.public_summary.write_text(json.dumps(public, sort_keys=True) + '\n')
    except Exception:
        print('Legacy MinerU inspection failed before a complete receipt was saved.')
        return 1
    print(json.dumps(public, sort_keys=True))
    return 2 if public['network_stop'] else 0


if __name__ == '__main__':
    raise SystemExit(main())
