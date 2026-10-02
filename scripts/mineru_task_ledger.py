"""Durable, source-bound MinerU tasks. Accepted work is polled, never resubmitted.

Private R2 is used by production workflows. The local backend supports offline
CLI use. Unknown submission outcomes and interrupted claims need investigation;
no lease expiry authorizes another provider POST.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import time
import uuid

PREFIX = '_workflow-cache/mineru-inflight/v1'
DONE = {'done', 'success', 'completed'}
FAILED = {'failed', 'fail', 'error'}
ACTIVE = {'pending', 'waiting-file', 'running', 'converting'}
MAX_CHECKPOINT_BYTES = 64 * 1024


class LedgerError(RuntimeError):
    pass


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def token_fingerprint(token):
    return digest(b'mineru-token-identity-v1\0' + token.encode())


def validate_scope(scope):
    if not isinstance(scope, str) or not re.fullmatch(r'[a-z][a-z0-9-]{0,63}', scope):
        raise LedgerError('Explicit stable pipeline scope is required')


def validate_source(source):
    if not isinstance(source, str):
        raise LedgerError('Invalid stable source identity')
    name = PurePosixPath(source)
    if (name.is_absolute() or '..' in name.parts or name.as_posix() != source
            or name.suffix.lower() != '.pdf' or '\\' in source
            or any(ord(c) < 32 for c in source)):
        raise LedgerError('Invalid stable source identity')


def validate_key(key):
    if not isinstance(key, str) or not re.fullmatch(r'(sources/[a-f0-9]{64}|batches/[a-f0-9]{32})', key):
        raise LedgerError('Invalid ledger key')


def decode(raw):
    if len(raw) > MAX_CHECKPOINT_BYTES:
        raise LedgerError('Task checkpoint exceeds size bound')
    try:
        value = json.loads(raw)
    except (ValueError, UnicodeError) as error:
        raise LedgerError('Malformed task checkpoint') from error
    if not isinstance(value, dict):
        raise LedgerError('Malformed task checkpoint object')
    return value


class FileStore:
    def __init__(self, root):
        self.root = Path(root)
        self.root.mkdir(parents=True, exist_ok=True)

    def _path(self, key):
        validate_key(key)
        return self.root / (key + '.json')

    def get(self, key):
        path = self._path(key)
        if not path.exists():
            return None, None
        with path.open('rb') as stream:
            raw = stream.read(MAX_CHECKPOINT_BYTES + 1)
        return decode(raw), digest(raw)

    def put(self, key, value, previous=None):
        import fcntl
        path = self._path(key)
        path.parent.mkdir(parents=True, exist_ok=True)
        with (self.root / '.lock').open('a') as lock:
            fcntl.flock(lock, fcntl.LOCK_EX)
            _, actual = self.get(key)
            if actual != previous:
                raise LedgerError('Ledger compare-and-swap conflict; no new submission')
            raw = encoded(value)
            temporary = path.with_suffix('.' + uuid.uuid4().hex + '.tmp')
            temporary.write_bytes(raw)
            temporary.replace(path)
            return digest(raw)


class R2Store:
    def __init__(self, scope, client=None, bucket=None):
        validate_scope(scope)
        from private_workflow_handoff import build_r2_client, r2_bucket
        self.client = client or build_r2_client()
        if client is None:
            validate_s3_model(self.client.meta.service_model)
        self.bucket = bucket or r2_bucket()
        self.prefix = f'{PREFIX}/{scope}/'

    def get(self, key):
        validate_key(key)
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=self.prefix + key + '.json')
        except Exception as error:
            code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
            if code in {'NoSuchKey', '404', 'NotFound'}:
                return None, None
            raise
        if not isinstance(response.get('ContentLength'), int) or not 0 < response['ContentLength'] <= MAX_CHECKPOINT_BYTES:
            raise LedgerError('Task checkpoint size is invalid')
        raw = response['Body'].read(MAX_CHECKPOINT_BYTES + 1)
        if (len(raw) != response.get('ContentLength')
                or digest(raw) != response.get('Metadata', {}).get('sha256')
                or not response.get('ETag')):
            raise LedgerError('Private task checkpoint size, digest or version mismatch')
        return decode(raw), response['ETag']

    def put(self, key, value, previous=None):
        validate_key(key)
        raw = encoded(value)
        if len(raw) > MAX_CHECKPOINT_BYTES:
            raise LedgerError('Task checkpoint exceeds size bound')
        condition = {'IfMatch': previous} if previous is not None else {'IfNoneMatch': '*'}
        try:
            self.client.put_object(Bucket=self.bucket, Key=self.prefix + key + '.json',
                Body=raw, ContentType='application/json', Metadata={'sha256': digest(raw)}, **condition)
        except Exception:
            # A lost ACK can mean the conditional write succeeded. Read only;
            # never replay a write or infer that an absent read authorizes POST.
            stored, version = self.get(key)
            if stored == value and version:
                return version
            raise LedgerError('Private checkpoint write outcome unresolved; no new submission') from None
        stored, version = self.get(key)
        if stored != value or not version:
            raise LedgerError('Private checkpoint durable readback mismatch; no new submission')
        return version


def validate_s3_model(model):
    members = model.operation_model('PutObject').input_shape.members
    for parameter, header in [('IfMatch', 'If-Match'), ('IfNoneMatch', 'If-None-Match')]:
        shape = members.get(parameter)
        if shape is None or shape.serialization.get('location') != 'header' or shape.serialization.get('name') != header:
            raise LedgerError('MinerU checkpoints require boto3>=1.37.32 with conditional PutObject headers')



class Provider:
    def __init__(self, http, endpoint):
        self.http, self.endpoint = http, endpoint

    @staticmethod
    def parse(response):
        data = response.json()
        if (response.status_code >= 400 or not isinstance(data, dict)
                or data.get('code') not in (None, 0, '0') or not isinstance(data.get('data'), dict)):
            # Do not retain arbitrary provider error bodies, URLs or tokens.
            raise LedgerError(f'MinerU request rejected or malformed: HTTP {response.status_code}')
        return data['data']

    @staticmethod
    def headers(token):
        return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

    def request(self, method, *args, **kwargs):
        try:
            return getattr(self.http, method)(*args, **kwargs)
        except Exception as error:
            raise LedgerError(f'MinerU {method} transport outcome unknown; saved task retained') from error

    def submit(self, items, options, token, timeout):
        files = [{'name': item['source'].rsplit('/', 1)[-1], 'data_id': item['id'],
                  'is_ocr': options['ocr']} for item in items]
        body = self.parse(self.request('post', self.endpoint + '/api/v4/file-urls/batch',
            headers=self.headers(token), json={'files': files, 'model_version': options['model'],
                'language': options['language'], 'enable_table': True, 'enable_formula': True}, timeout=min(60, timeout)))
        batch_id, urls = body.get('batch_id'), body.get('file_urls')
        if (not isinstance(batch_id, str) or not batch_id or not isinstance(urls, list)
                or len(urls) != len(items) or not all(isinstance(u, str) and u.startswith('https://') for u in urls)):
            raise LedgerError('MinerU submission acknowledgement is incomplete')
        return batch_id, urls

    def upload(self, url, raw, timeout):
        response = self.request('put', url, data=raw, timeout=min(300, timeout))
        if response.status_code not in (200, 201, 204):
            raise LedgerError(f'MinerU upload did not complete: HTTP {response.status_code}')

    def poll(self, batch_id, token, timeout):
        from urllib.parse import quote
        return self.parse(self.request('get', self.endpoint + '/api/v4/extract-results/batch/' + quote(batch_id, safe=''),
            headers=self.headers(token), timeout=min(60, timeout))).get('extract_result')


class Ledger:
    def __init__(self, store, provider, scope, endpoint, options, tokens, *, clock=time.monotonic, sleep=time.sleep):
        validate_scope(scope)
        if endpoint != 'https://mineru.net':
            raise LedgerError('Unexpected extraction provider endpoint')
        self.store, self.provider, self.scope, self.endpoint, self.options = store, provider, scope, endpoint, options
        self.tokens = {token_fingerprint(token): token for _, token in tokens}
        if not self.tokens:
            raise LedgerError('No MinerU token identities available')
        self.clock, self.sleep = clock, sleep

    def bind(self, path, source):
        validate_source(source)
        raw = Path(path).read_bytes()
        if not raw:
            raise LedgerError('Empty source PDF cannot be admitted')
        value = {'source': source, 'sha256': digest(raw), 'size': len(raw), 'scope': self.scope,
                 'endpoint': self.endpoint, 'options': self.options}
        return dict(value, id=digest(encoded(value)))

    def _read_batch(self, key):
        validate_key(key)
        if not key.startswith('batches/'):
            raise LedgerError('Invalid batch reference')
        row, version = self.store.get(key)
        if (not isinstance(row, dict) or row.get('schema') != 1 or row.get('scope') != self.scope
                or row.get('endpoint') != self.endpoint or row.get('options') != self.options
                or row.get('key') != key or row.get('token_identity') not in self.tokens
                or not isinstance(row.get('files'), list) or not 1 <= len(row['files']) <= 5):
            raise LedgerError('Stored task scope, source, options or token identity mismatch')
        for item in row['files']:
            if not isinstance(item, dict):
                raise LedgerError('Stored source binding is malformed')
            if (set(item) != {'id', 'source', 'sha256', 'size', 'scope', 'endpoint', 'options'}
                    or not isinstance(item['sha256'], str) or not re.fullmatch('[a-f0-9]{64}', item['sha256'])
                    or type(item['size']) is not int or item['size'] <= 0):
                raise LedgerError('Stored source binding is malformed')
            validate_source(item['source'])
            body = {k: v for k, v in item.items() if k != 'id'}
            if (item.get('id') != digest(encoded(body)) or item.get('scope') != self.scope
                    or item.get('endpoint') != self.endpoint or item.get('options') != self.options):
                raise LedgerError('Stored source binding is malformed')
        if len({item['id'] for item in row['files']}) != len(row['files']):
            raise LedgerError('Stored task has duplicate source identities')
        return row, version

    def _remaining(self, deadline):
        remaining = deadline - self.clock()
        if remaining <= 0:
            raise LedgerError('Task attempt time budget exhausted; saved task retained')
        return remaining

    def _create(self, items, paths, deadline):
        key = 'batches/' + uuid.uuid4().hex
        row = {'schema': 1, 'key': key, 'scope': self.scope, 'endpoint': self.endpoint,
               'options': self.options, 'token_identity': next(iter(self.tokens)), 'files': items,
               'state': 'claiming', 'batch_id': None}
        version = self.store.put(key, row)
        for item in items:
            # A competing claim or interruption cannot authorize another POST.
            self.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': key})
        row['state'] = 'submitting'
        version = self.store.put(key, row, version)
        token = self.tokens[row['token_identity']]
        batch_id, urls = self.provider.submit(items, self.options, token, self._remaining(deadline))
        row.update(state='accepted', batch_id=batch_id)
        version = self.store.put(key, row, version)  # Before any upload or poll.
        for item, url in zip(items, urls):
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Source bytes changed after task admission')
            self.provider.upload(url, raw, self._remaining(deadline))
        row['state'] = 'uploaded'
        self.store.put(key, row, version)
        return key

    def _poll(self, key, requested, deadline, interval, queue_budget):
        batch, version = self._read_batch(key)
        if batch['state'] in {'claiming', 'submitting'}:
            raise LedgerError('Interrupted or ambiguous submission; inspect saved task, never resubmit')
        if batch['state'] not in {'accepted', 'uploaded', 'terminal'} or not isinstance(batch.get('batch_id'), str):
            raise LedgerError('Unrecognized saved task state')
        bound = {item['id']: item for item in batch['files']}
        if any(bound.get(item['id']) != item for item in requested):
            raise LedgerError('Requested PDF does not match accepted task bytes and scope')
        token = self.tokens[batch['token_identity']]
        begun = self.clock()
        no_progress_since = begun
        last_states = None
        last = {}
        while self.clock() < deadline:
            rows = self.provider.poll(batch['batch_id'], token, self._remaining(deadline))
            if not isinstance(rows, list):
                raise LedgerError('Malformed MinerU result rows')
            seen = {}
            for row in rows:
                if not isinstance(row, dict) or row.get('data_id') not in bound or row['data_id'] in seen:
                    raise LedgerError('Unknown or duplicate result source identity')
                state = str(row.get('state', '')).lower()
                if state not in DONE | FAILED | ACTIVE:
                    raise LedgerError('Unknown MinerU result state')
                if state in DONE and not (isinstance(row.get('full_zip_url'), str) and row['full_zip_url'].startswith('https://')):
                    raise LedgerError('Completed MinerU row lacks source result URL')
                seen[row['data_id']] = row
            last = seen
            states = {key: str(row['state']).lower() for key, row in seen.items()}
            if states != last_states:
                no_progress_since = self.clock()
                last_states = states
            # Every admitted file must have a terminal row before batch completion.
            if len(seen) == len(bound) and all(str(r['state']).lower() in DONE | FAILED for r in seen.values()):
                if batch['state'] != 'terminal':
                    batch['state'] = 'terminal'
                    self.store.put(key, batch, version)
                break
            if batch['state'] == 'terminal':
                raise LedgerError('Previously terminal batch returned truncated or nonterminal results')
            if queue_budget > 0 and self.clock() - no_progress_since >= queue_budget:
                break
            remaining = deadline - self.clock()
            if remaining > 0:
                self.sleep(min(interval, remaining))
        wanted = {item['id'] for item in requested}
        return {i: r for i, r in last.items() if i in wanted}

    def run(self, paths_and_sources, *, timeout, interval=15, queue_budget=600):
        if not 1 <= len(paths_and_sources) <= 5 or timeout <= 0 or interval <= 0:
            raise LedgerError('Use a bounded batch of one to five PDFs and positive timeout')
        items = [self.bind(path, source) for path, source in paths_and_sources]
        if len({item['id'] for item in items}) != len(items):
            raise LedgerError('Duplicate input source identity')
        paths = {item['id']: path for item, (path, _) in zip(items, paths_and_sources)}
        groups, fresh = {}, []
        for item in items:
            reference, _ = self.store.get('sources/' + item['id'])
            if reference is None:
                fresh.append(item)
                continue
            if not isinstance(reference, dict) or reference.get('schema') != 1 or reference.get('binding') != item or not isinstance(reference.get('batch_key'), str):
                raise LedgerError('Source claim binding mismatch')
            groups.setdefault(reference['batch_key'], []).append(item)
        # Validate every existing task before any new provider mutation.
        for key, requested in groups.items():
            batch, _ = self._read_batch(key)
            bound = {item['id']: item for item in batch['files']}
            if any(bound.get(item['id']) != item for item in requested):
                raise LedgerError('Requested PDF does not match accepted task bytes and scope')
            if batch.get('state') not in {'accepted', 'uploaded', 'terminal'} or not batch.get('batch_id'):
                raise LedgerError('Ambiguous existing task blocks new submissions')
        deadline = self.clock() + timeout
        if fresh:
            groups[self._create(fresh, paths, deadline)] = fresh
        observed = {}
        for key, requested in groups.items():
            observed.update(self._poll(key, requested, deadline, interval, queue_budget))
        for item in items:
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Source bytes changed during polling; results cannot be reused')
        successes = [(Path(paths[i]), row) for i, row in observed.items() if str(row['state']).lower() in DONE]
        failed = sum(str(row['state']).lower() in FAILED for row in observed.values())
        pending = len(items) - len(successes) - failed
        return successes, {'requested': len(items), 'completed': len(successes), 'failed': failed,
                           'pending': pending, 'batch_keys': list(groups), 'provider_posts': int(bool(fresh))}


def from_environment(output_dir, http, endpoint, options, tokens):
    scope = os.environ.get('MINERU_CHECKPOINT_SCOPE', 'local')
    validate_scope(scope)
    backend = os.environ.get('MINERU_LEDGER_BACKEND', 'local')
    if os.environ.get('GITHUB_ACTIONS') == 'true' and (backend != 'r2' or scope == 'local'):
        raise LedgerError('GitHub Actions requires a durable private MinerU scope')
    if backend == 'r2':
        store = R2Store(scope)
    elif backend == 'local':
        store = FileStore(Path(output_dir) / '.mineru-task-ledger' / scope)
    else:
        raise LedgerError('Unknown MinerU ledger backend')
    return Ledger(store, Provider(http, endpoint), scope, endpoint, options, tokens)


def input_sources(pdfs, input_dir, source_map=None):
    """Bind wrapper temp names to original relative names and frozen exact bytes."""
    root = Path(input_dir).resolve()
    if any(Path(pdf).is_symlink() for pdf in pdfs):
        raise LedgerError('PDF symlinks are not frozen inputs')
    pdfs = [Path(pdf).resolve() for pdf in pdfs]
    entries = None
    if source_map:
        value = decode(Path(source_map).read_bytes())
        entries = value.get('files')
        if value.get('schema') != 1 or not isinstance(entries, dict):
            raise LedgerError('Malformed stable source map')
        if set(entries) != {Path(pdf).relative_to(root).as_posix() for pdf in pdfs}:
            raise LedgerError('Stable source map does not exactly cover selected PDFs')
    result = []
    for pdf in pdfs:
        pdf = Path(pdf)
        if pdf.is_symlink() or root not in pdf.resolve().parents:
            raise LedgerError('PDF escapes frozen input directory')
        relative = pdf.relative_to(root).as_posix()
        source = relative
        if entries is not None:
            entry = entries[relative]
            raw = pdf.read_bytes()
            if (not isinstance(entry, dict) or entry.get('sha256') != digest(raw)
                    or entry.get('size') != len(raw) or not isinstance(entry.get('source'), str)):
                raise LedgerError('Stable source map bytes mismatch')
            source = entry['source']
        validate_source(source)
        result.append((pdf, source))
    if len({source for _, source in result}) != len(result):
        raise LedgerError('Duplicate stable source name')
    return result
