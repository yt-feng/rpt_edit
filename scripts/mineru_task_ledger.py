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
# MinerU's official error-code table: https://mineru.net/apiManage/docs
# A0211 is expired authentication; A0202 is an invalid token.
AUTH_REJECTION_CODES = {'A0211', 'A0202'}


class LedgerError(RuntimeError):
    pass


class DefinitiveAuthRejection(LedgerError):
    """The provider explicitly refused authentication before accepting a task."""
    def __init__(self, code, http_status):
        if (not isinstance(code, str) or type(http_status) is not int
                or not 200 <= http_status < 500 or http_status == 429
                or (code not in AUTH_REJECTION_CODES and not (code == 'HTTP401' and http_status == 401))):
            raise LedgerError('Invalid definitive authentication rejection')
        self.code, self.http_status = code, http_status
        super().__init__(f'MinerU authentication definitively rejected: {code}, HTTP {http_status}')


def encoded(value):
    return json.dumps(value, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()


def exact_json(left, right):
    # Python considers True == 1 and 1 == 1.0; source and state bindings must not.
    return encoded(left) == encoded(right)


def schema_v1(value):
    return isinstance(value, dict) and type(value.get('schema')) is int and value['schema'] == 1


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
    if not isinstance(key, str) or not re.fullmatch(r'(sources/[a-f0-9]{64}|(?:batches|recoveries)/[a-f0-9]{32})', key):
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
    if 'schema' in value and type(value['schema']) is not int:
        raise LedgerError('Task checkpoint schema must be an integer')
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
        except Exception as error:
            code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
            status = getattr(error, 'response', {}).get('ResponseMetadata', {}).get('HTTPStatusCode')
            if code in {'PreconditionFailed', 'ConditionalRequestConflict', '412', '409'} or status in {409, 412}:
                # A definite failed condition belongs to another writer, even
                # if its resulting bytes happen to match this write exactly.
                raise LedgerError('Ledger compare-and-swap conflict; no new submission') from None
            # A lost ACK can mean the conditional write succeeded. Read only;
            # never replay a write or infer that an absent read authorizes POST.
            stored, version = self.get(key)
            if exact_json(stored, value) and version:
                return version
            raise LedgerError('Private checkpoint write outcome unresolved; no new submission') from None
        stored, version = self.get(key)
        if not exact_json(stored, value) or not version:
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
        status = response.status_code
        try:
            data = response.json()
        except Exception:
            if status == 401:
                raise DefinitiveAuthRejection('HTTP401', 401) from None
            raise LedgerError(f'MinerU response is not valid JSON: HTTP {status}') from None
        code = None
        if isinstance(data, dict):
            code = data.get('code')
            if code is None:
                code = data.get('msgCode')
            if code is None:
                code = data.get('msg_code')
        normalized = code.strip().upper() if isinstance(code, str) else ''
        # Even an auth-shaped reply cannot authorize another POST if it also
        # contains an acceptance acknowledgement. Leave the saved intent
        # ambiguous rather than infer that the first task was rejected.
        body = data.get('data') if isinstance(data, dict) else None
        acknowledgement = any(
            isinstance(candidate, dict) and any(key in candidate for key in ('batch_id', 'file_urls'))
            for candidate in (data, body)
        )
        auth_rejection = (type(status) is int and 200 <= status < 500 and status != 429
                          and (normalized in AUTH_REJECTION_CODES or status == 401))
        if auth_rejection:
            if acknowledgement:
                raise LedgerError('MinerU authentication rejection conflicts with a submission acknowledgement')
            raise DefinitiveAuthRejection(normalized if normalized in AUTH_REJECTION_CODES else 'HTTP401', status)
        if (response.status_code >= 400 or not isinstance(data, dict)
                or code not in (None, 0, '0') or not isinstance(data.get('data'), dict)):
            # Do not retain arbitrary provider error bodies, URLs or tokens.
            raise LedgerError(f'MinerU request rejected or malformed: HTTP {response.status_code}')
        return data['data']

    @staticmethod
    def headers(token):
        return {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + token}

    def request(self, method, *args, **kwargs):
        try:
            return getattr(self.http, method)(*args, **kwargs)
        except Exception:
            raise LedgerError(f'MinerU {method} transport outcome unknown; saved task retained') from None

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
    def __init__(self, store, provider, scope, endpoint, options, tokens, *, clock=time.monotonic, sleep=time.sleep, forbid_new_submissions=False):
        validate_scope(scope)
        if endpoint != 'https://mineru.net':
            raise LedgerError('Unexpected extraction provider endpoint')
        if (not isinstance(options, dict) or set(options) != {'model', 'language', 'ocr'}
                or not all(isinstance(options.get(key), str) and options[key] for key in ('model', 'language'))
                or type(options.get('ocr')) is not bool):
            raise LedgerError('Invalid exact extraction options')
        self.store, self.provider, self.scope, self.endpoint, self.options = store, provider, scope, endpoint, options
        self.tokens = {token_fingerprint(token): token for _, token in tokens}
        if not self.tokens:
            raise LedgerError('No MinerU token identities available')
        self.clock, self.sleep = clock, sleep
        if type(forbid_new_submissions) is not bool:
            raise LedgerError('Invalid no-new-submission policy')
        self.forbid_new_submissions = forbid_new_submissions
        self.submission_posts = 0

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
        if (not schema_v1(row) or row.get('scope') != self.scope
                or row.get('endpoint') != self.endpoint or not exact_json(row.get('options'), self.options)
                or row.get('key') != key
                or not re.fullmatch(r'[a-f0-9]{64}', str(row.get('token_identity') or ''))
                or (row.get('state') != 'auth_rejected' and row.get('token_identity') not in self.tokens)
                or not isinstance(row.get('files'), list) or not 1 <= len(row['files']) <= 5):
            raise LedgerError('Stored task scope, source, options or token identity mismatch')
        rejections = row.get('auth_rejections', [])
        if not isinstance(rejections, list):
            raise LedgerError('Stored authentication rejection history is malformed')
        rejected_tokens = set()
        for rejection in rejections:
            if (not isinstance(rejection, dict) or set(rejection) != {'token_identity', 'code', 'http_status'}
                    or not re.fullmatch(r'[a-f0-9]{64}', str(rejection.get('token_identity') or ''))
                    or rejection['token_identity'] in rejected_tokens):
                raise LedgerError('Stored authentication rejection history is malformed')
            DefinitiveAuthRejection(rejection['code'], rejection['http_status'])
            rejected_tokens.add(rejection['token_identity'])
        if row.get('state') == 'auth_rejected':
            if (not rejections or row.get('batch_id') is not None
                    or row['token_identity'] != rejections[-1]['token_identity']):
                raise LedgerError('Stored authentication rejection state is inconsistent')
        elif row.get('state') in {'accepted', 'uploaded', 'terminal'} and row['token_identity'] in rejected_tokens:
            raise LedgerError('Accepted task refers to a definitively rejected credential')
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
                    or item.get('endpoint') != self.endpoint or not exact_json(item.get('options'), self.options)):
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
        if self.forbid_new_submissions:
            raise LedgerError('Replay requires existing accepted source bindings; new submissions forbidden')
        key = 'batches/' + uuid.uuid4().hex
        row = {'schema': 1, 'key': key, 'scope': self.scope, 'endpoint': self.endpoint,
               'options': self.options, 'token_identity': next(iter(self.tokens)), 'files': items,
               'state': 'claiming', 'batch_id': None}
        version = self.store.put(key, row)
        for item in items:
            # A competing claim or interruption cannot authorize another POST.
            self.store.put('sources/' + item['id'], {'schema': 1, 'binding': item, 'batch_key': key})
        self._submit_claimed(row, version, paths, deadline)
        return key

    def _submit_claimed(self, row, version, paths, deadline):
        """Try another key only after durable, definitive pre-acceptance rejection."""
        if self.forbid_new_submissions:
            raise LedgerError('Replay cannot submit an unaccepted task; new submissions forbidden')
        items, key = row['files'], row['key']
        if row.get('state') not in {'claiming', 'auth_rejected'} or row.get('batch_id') is not None:
            raise LedgerError('Only unaccepted or definitively auth-rejected claims may be submitted')
        if set(paths).intersection(item['id'] for item in items) != {item['id'] for item in items}:
            raise LedgerError('Authentication-rejected batch requires its complete original source inventory')
        for item in items:
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Original source bytes changed before task submission')
        rejections = row.setdefault('auth_rejections', [])
        rejected = {entry['token_identity'] for entry in rejections}
        identities = list(self.tokens)
        if row['token_identity'] in identities:
            identities.remove(row['token_identity'])
            identities.insert(0, row['token_identity'])
        for identity in identities:
            token = self.tokens[identity]
            if identity in rejected:
                continue
            remaining = self._remaining(deadline)
            for item in items:
                raw = Path(paths[item['id']]).read_bytes()
                if len(raw) != item['size'] or digest(raw) != item['sha256']:
                    raise LedgerError('Original source bytes changed before task submission')
            # A crash or unrecognized response after this durable write stays
            # submitting. It never becomes permission to try the next key.
            row.update(state='submitting', token_identity=identity, batch_id=None,
                       submission_attempt=uuid.uuid4().hex)
            version = self.store.put(key, row, version)
            self.submission_posts += 1
            try:
                batch_id, urls = self.provider.submit(items, self.options, token, remaining)
            except DefinitiveAuthRejection as error:
                rejections.append({'token_identity': identity, 'code': error.code, 'http_status': error.http_status})
                rejected.add(identity)
                row['state'] = 'auth_rejected'
                version = self.store.put(key, row, version)
                continue
            row.update(state='accepted', batch_id=batch_id)
            version = self.store.put(key, row, version)  # Before any upload or poll.
            break
        else:
            raise LedgerError('All configured MinerU credentials were definitively rejected; saved batch is auth_rejected')
        for item, url in zip(items, urls):
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Source bytes changed after task admission')
            self.provider.upload(url, raw, self._remaining(deadline))
        row['state'] = 'uploaded'
        self.store.put(key, row, version)

    def _poll(self, key, requested, deadline, interval, queue_budget, *, persist_terminal=True):
        batch, version = self._read_batch(key)
        if batch['state'] in {'claiming', 'submitting'}:
            raise LedgerError('Interrupted or ambiguous submission; inspect saved task, never resubmit')
        if batch['state'] not in {'accepted', 'uploaded', 'terminal'} or not isinstance(batch.get('batch_id'), str):
            raise LedgerError('Unrecognized saved task state')
        bound = {item['id']: item for item in batch['files']}
        if any(not exact_json(bound.get(item['id']), item) for item in requested):
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
                if persist_terminal and batch['state'] != 'terminal':
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
        completed = sum(str(row['state']).lower() in DONE for row in last.values())
        failed = sum(str(row['state']).lower() in FAILED for row in last.values())
        original_batch = {'key': key, 'admitted': len(bound), 'observed': len(last),
                          'completed': completed, 'failed': failed,
                          'pending': len(bound) - completed - failed,
                          'missing': len(bound) - len(last)}
        original_batch['all_succeeded'] = completed == len(bound)
        return {i: r for i, r in last.items() if i in wanted}, original_batch

    def run(self, paths_and_sources, *, timeout, interval=15, queue_budget=600):
        if not 1 <= len(paths_and_sources) <= 5 or timeout <= 0 or interval <= 0:
            raise LedgerError('Use a bounded batch of one to five PDFs and positive timeout')
        items = [self.bind(path, source) for path, source in paths_and_sources]
        if len({item['id'] for item in items}) != len(items):
            raise LedgerError('Duplicate input source identity')
        self.submission_posts = 0
        paths = {item['id']: path for item, (path, _) in zip(items, paths_and_sources)}
        groups, fresh = {}, []
        for item in items:
            reference, _ = self.store.get('sources/' + item['id'])
            if reference is None:
                fresh.append(item)
                continue
            if not schema_v1(reference) or not exact_json(reference.get('binding'), item) or not isinstance(reference.get('batch_key'), str):
                raise LedgerError('Source claim binding mismatch')
            groups.setdefault(reference['batch_key'], []).append(item)
        # Validate every existing task before any new provider mutation.
        rejected_batches = []
        for key, requested in groups.items():
            batch, version = self._read_batch(key)
            bound = {item['id']: item for item in batch['files']}
            if any(not exact_json(bound.get(item['id']), item) for item in requested):
                raise LedgerError('Requested PDF does not match accepted task bytes and scope')
            if batch.get('state') == 'auth_rejected':
                if ({item['id'] for item in requested} != set(bound)
                        or {item['id'] for item in items} != set(bound)):
                    raise LedgerError('Authentication-rejected batch requires only its complete original source inventory')
                rejected_batches.append((batch, version))
            elif batch.get('state') not in {'accepted', 'uploaded', 'terminal'} or not batch.get('batch_id'):
                raise LedgerError('Ambiguous existing task blocks new submissions')
        if self.forbid_new_submissions and (fresh or rejected_batches):
            raise LedgerError('Replay requires existing accepted source bindings; new submissions forbidden')
        deadline = self.clock() + timeout
        for batch, version in rejected_batches:
            self._submit_claimed(batch, version, paths, deadline)
        if fresh:
            groups[self._create(fresh, paths, deadline)] = fresh
        observed = {}
        original_batches = []
        for key, requested in groups.items():
            selected_rows, original_batch = self._poll(key, requested, deadline, interval, queue_budget)
            observed.update(selected_rows)
            original_batches.append(original_batch)
        for item in items:
            raw = Path(paths[item['id']]).read_bytes()
            if len(raw) != item['size'] or digest(raw) != item['sha256']:
                raise LedgerError('Source bytes changed during polling; results cannot be reused')
        successes = [(Path(paths[i]), row) for i, row in observed.items() if str(row['state']).lower() in DONE]
        failed = sum(str(row['state']).lower() in FAILED for row in observed.values())
        pending = len(items) - len(successes) - failed
        ready = not pending and not failed and all(batch['all_succeeded'] for batch in original_batches)
        # Completed selected counts remain diagnostic, but partial original batches
        # never release result rows to downstream generation, even after regrouping.
        return (successes if ready else []), {
            'requested': len(items), 'completed': len(successes), 'failed': failed,
            'pending': pending, 'batch_keys': list(groups), 'provider_posts': self.submission_posts,
            'original_batches': original_batches, 'ready_for_generation': ready,
        }


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
    policy = os.environ.get('MINERU_FORBID_NEW_SUBMISSIONS', '0')
    if policy not in {'0', '1'}:
        raise LedgerError('Invalid no-new-submission policy')
    return Ledger(store, Provider(http, endpoint), scope, endpoint, options, tokens,
                  forbid_new_submissions=policy == '1')


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
        if not schema_v1(value) or not isinstance(entries, dict):
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
