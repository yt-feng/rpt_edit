#!/usr/bin/env python3
"""One reviewed IMF cache import. No production activation or provider calls."""
from __future__ import annotations

import argparse
import base64
from datetime import datetime, timezone
import hashlib
import io
import json
import os
from pathlib import Path
import re
import stat
import subprocess
import sys
import time
from urllib.parse import parse_qsl, urlsplit

# Change these together only after reviewing a replacement manifest.
MANIFEST_SHA256 = '250557000edbc46f0629393a7a43a139b37926cb54c58535ea498866ccd77e67'
EXPECTED_COUNT = 17
EXPECTED_BYTES = 25038788
PRODUCTION_SHA = 'a1b68ba1ffe4d79281ed2f015aad74182bb24d01'
REPOSITORY = 'yt-feng/rpt_edit'
WORKFLOW = '.github/workflows/institution-fetch-test.yml'
BRANCH = 'codex/imf-reviewed-cache-import-20261012'
SCOPE = 'imf-reviewed-originals-20261012'
ALGORITHM = 'RSA-OAEP-SHA256+A256GCM'
TTL = 900
MAX_ENVELOPE = 256 * 1024
SESSION_ROOT = Path(__file__).resolve().parent / 'sessions'
SHA = re.compile(r'[a-f0-9]{64}')
HOST = re.compile(r'[a-f0-9]{32}\.r2\.cloudflarestorage\.com')
BUCKET = re.compile(r'[a-z0-9][a-z0-9-]{1,61}[a-z0-9]')
QUERY_FIELDS = {'X-Amz-Algorithm', 'X-Amz-Credential', 'X-Amz-Date', 'X-Amz-Expires',
                'X-Amz-SignedHeaders', 'X-Amz-Signature'}
ORIGINAL_ERROR_CODES = frozenset({
    'original_binding', 'original_options', 'original_identity', 'original_source', 'original_binding_hash',
    'original_bytes', 'original_bucket', 'original_read_failed', 'original_metadata',
    'original_write_unresolved', 'original_readback', 'original_conflict', 'original_local_size',
    'original_private_store_required', 'original_sources_empty', 'original_duplicate', 'original_total_size',
})


class BridgeError(ValueError):
    pass


def require(condition, code):
    if not condition:
        raise BridgeError(code)


def sha(raw):
    return hashlib.sha256(raw).hexdigest()


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def strict_json(raw):
    def pairs(items):
        result = {}
        for key, value in items:
            require(key not in result, 'duplicate_json_key')
            result[key] = value
        return result
    try:
        return json.loads(raw, object_pairs_hook=pairs)
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('invalid_json') from None


def read_file(path, maximum, *, mode=None):
    path = Path(path)
    require(not path.is_symlink(), 'local_file_symlink')
    try:
        with os.fdopen(os.open(path, os.O_RDONLY | os.O_NOFOLLOW), 'rb') as stream:
            info = os.fstat(stream.fileno())
            require(stat.S_ISREG(info.st_mode) and 0 < info.st_size <= maximum, 'local_file_size')
            if mode is not None:
                require(stat.S_IMODE(info.st_mode) == mode and info.st_uid == os.getuid(), 'private_file_mode')
            raw = stream.read(maximum + 1)
        require(len(raw) == info.st_size and len(raw) <= maximum, 'local_file_changed')
        return raw
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('local_file_read') from None


def write_new(path, raw, mode=0o600):
    try:
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL | os.O_NOFOLLOW, mode)
        with os.fdopen(descriptor, 'wb') as stream:
            os.fchmod(stream.fileno(), mode)
            stream.write(raw)
    except Exception:
        raise BridgeError('output_file_write') from None


def load_production(repo):
    repo = Path(repo).resolve()
    try:
        head = subprocess.run(['git', '-C', str(repo), 'rev-parse', 'HEAD'],
                              capture_output=True, check=True, text=True).stdout.strip()
        clean = subprocess.run(['git', '-C', str(repo), 'status', '--porcelain', '--untracked-files=no', '--', 'scripts'],
                               capture_output=True, check=True, text=True).stdout
        require(head == PRODUCTION_SHA and not clean, 'production_revision')
        sys.path.insert(0, str(repo / 'scripts'))
        import institution_original_cache as cache
        import institution_verified_originals as verified
        import institution_pending_intake as pending
        return cache, verified, pending
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('production_import') from None


def approved_manifest(path, production):
    raw = read_file(path, 512 * 1024)
    require(sha(raw) == MANIFEST_SHA256, 'manifest_digest')
    _, verified, _ = production
    try:
        selection = verified.VerifiedOriginals(path, cache_factory=lambda: None)
        rows = list(selection.records.values())
        require(len(rows) == EXPECTED_COUNT and sum(row['size'] for row in rows) == EXPECTED_BYTES,
                'manifest_inventory')
        return rows
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('manifest_contract') from None


def check_pending(rows, path, production):
    _, _, module = production
    # No mutation and no seen-state invention: presence is necessary here;
    # the production fetcher will independently apply its durable seen state.
    try:
        queue = module.PendingIntake(Path(path), {}, now=datetime.now(timezone.utc))
        require(all('imf:' + row['item']['guid'] in queue.initial_keys and
                    encoded(queue.items['imf:' + row['item']['guid']]['item']) == encoded(row['item'])
                    for row in rows), 'pending_identity')
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('pending_contract') from None


def prepare_files(rows, directory, production):
    cache, verified, _ = production
    directory = Path(directory)
    require(directory.is_dir() and not directory.is_symlink(), 'original_directory')
    expected = {row['sha256'] + '.pdf' for row in rows}
    require({path.name for path in directory.iterdir()} == expected, 'original_inventory')
    prepared = {}
    for row in rows:
        raw = read_file(directory / (row['sha256'] + '.pdf'), cache.MAX_PDF)
        try:
            cache.validate_payload(row['binding'], raw)
            require(verified.pdf_pages(raw) == row['pages'], 'original_page_count')
        except BridgeError:
            raise
        except Exception:
            raise BridgeError('original_validation') from None
        prepared[row['binding']['id']] = raw
    return prepared


def crypto_api():
    try:
        from cryptography.hazmat.primitives import hashes, serialization
        from cryptography.hazmat.primitives.asymmetric import padding, rsa
        from cryptography.hazmat.primitives.ciphers.aead import AESGCM
        return hashes, serialization, padding, rsa, AESGCM
    except Exception:
        raise BridgeError('cryptography_required') from None


def public_key(pem):
    hashes, serialization, padding, rsa, AESGCM = crypto_api()
    try:
        key = serialization.load_pem_public_key(pem)
        require(isinstance(key, rsa.RSAPublicKey) and key.key_size == 3072
                and key.public_numbers().e == 65537, 'recipient_key')
        der = key.public_bytes(serialization.Encoding.DER, serialization.PublicFormat.SubjectPublicKeyInfo)
        return key, sha(der)
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('recipient_key') from None


def public_request(path):
    value = strict_json(read_file(path, 8192))
    require(isinstance(value, dict) and set(value) == {'schema', 'public_key_pem', 'public_key_sha256', 'nonce'}
            and type(value['schema']) is int and value['schema'] == 1
            and isinstance(value['public_key_pem'], str)
            and isinstance(value['nonce'], str) and SHA.fullmatch(value['nonce']), 'recipient_request')
    key, fingerprint = public_key(value['public_key_pem'].encode())
    require(value['public_key_sha256'] == fingerprint, 'recipient_fingerprint')
    return value, key


def session_directory(name):
    require(isinstance(name, str) and re.fullmatch(r'[a-z0-9-]{1,48}', name), 'session_name')
    require(not SESSION_ROOT.is_symlink(), 'session_parent')
    return SESSION_ROOT / name


def keygen(name):
    """Explicit later operation; tests do not invoke real key generation."""
    hashes, serialization, padding, rsa, AESGCM = crypto_api()
    directory = session_directory(name)
    SESSION_ROOT.mkdir(mode=0o700, exist_ok=True)
    require(stat.S_IMODE(SESSION_ROOT.stat().st_mode) == 0o700, 'session_parent_mode')
    directory.mkdir(mode=0o700)
    key = rsa.generate_private_key(public_exponent=65537, key_size=3072)
    private = key.private_bytes(serialization.Encoding.PEM, serialization.PrivateFormat.PKCS8,
                                serialization.NoEncryption())
    pem = key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
    _, fingerprint = public_key(pem)
    request = {'schema': 1, 'public_key_pem': pem.decode(), 'public_key_sha256': fingerprint,
               'nonce': os.urandom(32).hex()}
    write_new(directory / 'private.pem', private)
    write_new(directory / 'public-request.json', encoded(request))
    return {'status': 'key_created', 'session': name, 'public_key_sha256': fingerprint}


def context(request, run_id, head_sha, issued):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id or '')
            and re.fullmatch(r'[a-f0-9]{40}', head_sha or '') and type(issued) is int
            and isinstance(request.get('public_key_sha256'), str) and SHA.fullmatch(request['public_key_sha256'])
            and isinstance(request.get('nonce'), str) and SHA.fullmatch(request['nonce']), 'producer_identity')
    return {'schema': 1, 'scope': SCOPE, 'repository': REPOSITORY, 'workflow': WORKFLOW,
            'ref': 'refs/heads/' + BRANCH, 'run_id': run_id, 'head_sha': head_sha,
            'manifest_sha256': MANIFEST_SHA256, 'record_count': EXPECTED_COUNT, 'total_bytes': EXPECTED_BYTES,
            'public_key_sha256': request['public_key_sha256'], 'nonce': request['nonce'],
            'issued_at': issued, 'expires_at': issued + TTL}


def cloud_context(request):
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
            and os.environ.get('GITHUB_REF') == 'refs/heads/' + BRANCH
            and os.environ.get('GITHUB_WORKFLOW_REF') == REPOSITORY + '/' + WORKFLOW + '@refs/heads/' + BRANCH,
            'reviewed_cloud_workflow_required')
    return context(request, os.environ.get('GITHUB_RUN_ID'), os.environ.get('GITHUB_SHA'), int(time.time()))


def put_headers(row):
    return {'Content-Type': 'application/pdf', 'Content-Length': str(row['size']),
            'Cache-Control': 'private, no-store', 'If-None-Match': '*',
            'x-amz-meta-sha256': row['sha256'], 'x-amz-meta-kind': 'institution-original-proof'}


def validate_url(url, *, bucket, host, key, method, headers, ctx, now):
    require(isinstance(url, str) and len(url) <= 8192 and not any(ord(c) < 33 for c in url), 'signed_url')
    try:
        parsed = urlsplit(url)
        require(parsed.scheme == 'https' and parsed.hostname == host and parsed.netloc == host
                and not parsed.username and not parsed.password and parsed.port is None
                and not parsed.fragment and '\\' not in url
                and parsed.path == '/' + bucket + '/' + key, 'signed_target')
        pairs = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        query = dict(pairs)
        require(len(query) == len(pairs) and set(query) == QUERY_FIELDS, 'signed_query')
        require(query['X-Amz-Algorithm'] == 'AWS4-HMAC-SHA256'
                and re.fullmatch(r'[a-fA-F0-9]{64}', query['X-Amz-Signature'])
                and query['X-Amz-Expires'] == str(TTL), 'signed_scope')
        stamp = datetime.strptime(query['X-Amz-Date'], '%Y%m%dT%H%M%SZ').replace(tzinfo=timezone.utc)
        signed_at = int(stamp.timestamp())
        credential = query['X-Amz-Credential'].split('/')
        require(len(credential) == 5 and bool(re.fullmatch(r'[A-Za-z0-9]{16,128}', credential[0]))
                and credential[1:] == [stamp.strftime('%Y%m%d'), 'auto', 's3', 'aws4_request'], 'signed_credential_scope')
        expected = {'host'} | {name.lower() for name in headers}
        signed_headers = query['X-Amz-SignedHeaders'].split(';')
        require(set(signed_headers) == expected and len(signed_headers) == len(expected), 'signed_headers')
        require(method in {'GET', 'PUT'} and ctx['issued_at'] - 5 <= signed_at <= ctx['issued_at'] + 30
                and signed_at <= now + 5 and now < min(ctx['expires_at'], signed_at + TTL), 'signed_expiry')
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('signed_url') from None


def validate_plan(plan, rows, ctx, now):
    require(isinstance(ctx, dict), 'plan_context')
    try:
        request = {field: ctx[field] for field in ('public_key_sha256', 'nonce')}
        require(ctx == context(request, ctx['run_id'], ctx['head_sha'], ctx['issued_at'])
                and ctx['issued_at'] <= now + 5 and now < ctx['expires_at'], 'plan_context')
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('plan_context') from None
    require(isinstance(plan, dict) and set(plan) == {'context', 'bucket', 'host', 'objects'}
            and plan['context'] == ctx and isinstance(plan['bucket'], str) and BUCKET.fullmatch(plan['bucket'])
            and isinstance(plan['host'], str) and HOST.fullmatch(plan['host'])
            and isinstance(plan['objects'], list) and len(plan['objects']) == len(rows), 'plan_contract')
    by_id = {row['binding']['id']: row for row in rows}
    selected = set()
    for entry in plan['objects']:
        require(isinstance(entry, dict) and set(entry) == {'binding', 'pages', 'key', 'get', 'put'}, 'plan_entry')
        binding = entry['binding']
        require(isinstance(binding, dict) and binding.get('id') in by_id, 'plan_binding')
        row = by_id[binding['id']]
        require(binding == row['binding'] and binding['id'] not in selected and entry['pages'] == row['pages']
                and type(entry['pages']) is int and entry['key'] == '_workflow-cache/institution-originals/v1/' + row['sha256'] + '.pdf',
                'plan_identity')
        selected.add(binding['id'])
        for operation, headers in (('get', {}), ('put', put_headers(row))):
            request = entry[operation]
            require(isinstance(request, dict) and set(request) == {'method', 'headers', 'url'}
                    and request['method'] == operation.upper() and request['headers'] == headers, 'plan_operation')
            validate_url(request['url'], bucket=plan['bucket'], host=plan['host'], key=entry['key'],
                         method=request['method'], headers=headers, ctx=ctx, now=now)
    return plan


def mint_plan(rows, request, client, bucket, host, ctx):
    objects = []
    for row in rows:
        key = '_workflow-cache/institution-originals/v1/' + row['sha256'] + '.pdf'
        params = {'Bucket': bucket, 'Key': key}
        get = client.generate_presigned_url('get_object', Params=params, ExpiresIn=TTL, HttpMethod='GET')
        params = dict(params, ContentType='application/pdf', ContentLength=row['size'], CacheControl='private, no-store',
                      IfNoneMatch='*', Metadata={'sha256': row['sha256'], 'kind': 'institution-original-proof'})
        put = client.generate_presigned_url('put_object', Params=params, ExpiresIn=TTL, HttpMethod='PUT')
        objects.append({'binding': row['binding'], 'pages': row['pages'], 'key': key,
                        'get': {'method': 'GET', 'headers': {}, 'url': get},
                        'put': {'method': 'PUT', 'headers': put_headers(row), 'url': put}})
    return validate_plan({'context': ctx, 'bucket': bucket, 'host': host, 'objects': objects}, rows, ctx, int(time.time()))


def seal(plan, key):
    hashes, serialization, padding, rsa, AESGCM = crypto_api()
    aes_key, nonce = os.urandom(32), os.urandom(12)
    ctx = plan['context']
    ciphertext = AESGCM(aes_key).encrypt(nonce, encoded(plan), encoded(ctx))
    wrapped = key.encrypt(aes_key, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                               algorithm=hashes.SHA256(), label=None))
    return {'algorithm': ALGORITHM, 'context': ctx, 'wrapped_key': base64.b64encode(wrapped).decode(),
            'nonce': base64.b64encode(nonce).decode(), 'ciphertext': base64.b64encode(ciphertext).decode()}


def open_envelope(raw, private, request, run_id, head_sha, now):
    require(len(raw) <= MAX_ENVELOPE, 'envelope_size')
    envelope = strict_json(raw)
    require(isinstance(envelope, dict) and set(envelope) == {'algorithm', 'context', 'wrapped_key', 'nonce', 'ciphertext'}
            and envelope['algorithm'] == ALGORITHM and isinstance(envelope['context'], dict), 'envelope_contract')
    ctx = envelope['context']; issued = ctx.get('issued_at')
    require(type(issued) is int and ctx == context(request, run_id, head_sha, issued)
            and issued <= now + 5 and now < issued + TTL, 'envelope_context')
    hashes, serialization, padding, rsa, AESGCM = crypto_api()
    try:
        key = serialization.load_pem_private_key(private, password=None)
        require(isinstance(key, rsa.RSAPrivateKey) and key.key_size == 3072, 'private_key')
        pub = key.public_key().public_bytes(serialization.Encoding.PEM, serialization.PublicFormat.SubjectPublicKeyInfo)
        require(public_key(pub)[1] == request['public_key_sha256'], 'private_key_identity')
        wrapped, nonce, ciphertext = (base64.b64decode(envelope[field], validate=True)
                                      for field in ('wrapped_key', 'nonce', 'ciphertext'))
        require(len(wrapped) == 384 and len(nonce) == 12 and 16 < len(ciphertext) <= MAX_ENVELOPE, 'envelope_encoding')
        aes_key = key.decrypt(wrapped, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
                                                   algorithm=hashes.SHA256(), label=None))
        require(len(aes_key) == 32, 'envelope_key')
        decoded = AESGCM(aes_key).decrypt(nonce, ciphertext, encoded(ctx))
        return strict_json(decoded), ctx
    except BridgeError:
        raise
    except Exception:
        raise BridgeError('envelope_authentication') from None


class StorageStatus(Exception):
    def __init__(self, status):
        super().__init__('storage_status')
        self.response = {'ResponseMetadata': {'HTTPStatusCode': status}}


class SignedStorage:
    """Only the exact S3-shaped GET and conditional PUT used by OriginalCache."""
    def __init__(self, plan, session, *, clock=time.time):
        self.plan, self.session, self.clock = plan, session, clock
        self.entries = {entry['key']: entry for entry in plan['objects']}
        self.calls = {}

    def _entry(self, bucket, key, operation):
        require(bucket == self.plan['bucket'] and key in self.entries, 'storage_target')
        entry = self.entries[key]; request = entry[operation]
        validate_url(request['url'], bucket=bucket, host=self.plan['host'], key=key, method=request['method'],
                     headers=request['headers'], ctx=self.plan['context'], now=int(self.clock()))
        counter = (key, operation); self.calls[counter] = self.calls.get(counter, 0) + 1
        require(self.calls[counter] <= (2 if operation == 'get' else 1), 'storage_call_bound')
        return entry

    def _request(self, entry, operation, payload=None):
        request = entry[operation]
        try:
            response = self.session.request(request['method'], request['url'], headers=request['headers'],
                data=payload, timeout=(20, 30), allow_redirects=False, stream=True, verify=True)
        except Exception:
            raise BridgeError('storage_transport') from None
        if response.url != request['url']:
            response.close(); raise BridgeError('storage_response_target')
        if response.status_code != 200:
            status = response.status_code; response.close(); raise StorageStatus(status)
        return response

    def get_object(self, **kwargs):
        require(set(kwargs) == {'Bucket', 'Key'}, 'storage_get_contract')
        entry = self._entry(kwargs['Bucket'], kwargs['Key'], 'get')
        response = self._request(entry, 'get')
        try:
            headers = {key.lower(): value for key, value in response.headers.items()}
            raw_length = headers.get('content-length', '')
            require(isinstance(raw_length, str) and raw_length.isdigit(), 'storage_length')
            require(not headers.get('content-encoding') or headers['content-encoding'] == 'identity', 'storage_encoding')
            length = int(raw_length)
            require(length == entry['binding']['size'], 'storage_length')
            payload = response.raw.read(length + 1, decode_content=False)
            return {'ContentLength': length, 'ContentType': headers.get('content-type'),
                    'Metadata': {key.removeprefix('x-amz-meta-'): value for key, value in headers.items()
                                 if key.startswith('x-amz-meta-')}, 'Body': io.BytesIO(payload)}
        except BridgeError:
            raise
        except Exception:
            raise BridgeError('storage_body_read') from None
        finally:
            response.close()

    def put_object(self, **kwargs):
        require(set(kwargs) == {'Bucket', 'Key', 'Body', 'ContentType', 'Metadata', 'CacheControl', 'IfNoneMatch'},
                'storage_put_contract')
        entry = self._entry(kwargs['Bucket'], kwargs['Key'], 'put')
        binding = entry['binding']
        require(kwargs['ContentType'] == 'application/pdf' and kwargs['CacheControl'] == 'private, no-store'
                and kwargs['IfNoneMatch'] == '*' and kwargs['Metadata'] ==
                {'sha256': binding['sha256'], 'kind': 'institution-original-proof'}
                and isinstance(kwargs['Body'], bytes) and len(kwargs['Body']) == binding['size']
                and sha(kwargs['Body']) == binding['sha256'], 'storage_put_identity')
        response = self._request(entry, 'put', kwargs['Body'])
        response.close()
        return {}


def requests_session():
    import requests
    from requests.adapters import HTTPAdapter
    session = requests.Session()
    session.mount('https://', HTTPAdapter(max_retries=0))
    return session


def import_prepared(rows, prepared, plan, production, session, *, clock=time.time):
    cache, _, _ = production
    validate_plan(plan, rows, plan['context'], int(clock()))
    require(set(prepared) == {row['binding']['id'] for row in rows}, 'prepared_inventory')
    for row in rows:
        cache.validate_payload(row['binding'], prepared[row['binding']['id']])
    adapter = SignedStorage(plan, session, clock=clock)
    original_cache = cache.OriginalCache.single_attempt(adapter, plan['bucket'])
    reused = 0
    for row in rows:
        # put performs GET, conditional PUT if absent, then an exact GET readback.
        reused += int(original_cache.put(row['binding'], prepared[row['binding']['id']]))
    return {'status': 'verified', 'manifest_sha256': MANIFEST_SHA256, 'originals': len(rows),
            'bytes': sum(row['size'] for row in rows), 'reused': reused, 'written': len(rows) - reused}


def safe_error_code(error):
    if isinstance(error, BridgeError) and re.fullmatch(r'[a-z_]{1,64}', str(error)):
        return str(error)
    module = sys.modules.get('institution_original_cache')
    if module is not None and type(error) is module.OriginalCacheError and str(error) in ORIGINAL_ERROR_CODES:
        return str(error)
    return 'operation_stopped'


def cloud_readback(rows, original_cache, production):
    """One bounded GET per exact source; no writes or repeat after an error."""
    cache, verified, _ = production
    require(len(rows) == EXPECTED_COUNT, 'readback_inventory')
    results = []
    counts = dict(verified=0, missing=0, invalid=0, read_error=0)
    for row in rows:
        status, code = 'verified', 'original_verified'
        try:
            payload = original_cache.get(row['binding'])
        except cache.OriginalCacheError as error:
            code = safe_error_code(error)
            status = 'read_error' if code in {'original_read_failed', 'operation_stopped'} else 'invalid'
        except Exception:
            status, code = 'read_error', 'original_read_error'
        else:
            if payload is None:
                status, code = 'missing', 'original_missing'
            else:
                try:
                    cache.validate_payload(row['binding'], payload)
                    if verified.pdf_pages(payload) != row['pages']:
                        status, code = 'invalid', 'original_page_count'
                except Exception:
                    status, code = 'invalid', 'original_pdf_invalid'
        counts[status] += 1
        results.append({'guid': row['item']['guid'], 'sha256': row['sha256'], 'status': status, 'code': code})
    accepted = counts['verified'] == EXPECTED_COUNT
    return {'status': 'cloud_readback_verified' if accepted else 'cloud_readback_incomplete',
            'accepted': accepted, 'manifest_sha256': MANIFEST_SHA256, 'originals': len(rows),
            'expected_bytes': sum(row['size'] for row in rows), 'counts': counts, 'results': results}


def cloud_client(*, read_only=False):
    import boto3
    from botocore.config import Config
    from private_workflow_handoff import require_env
    host = require_env('R2_ACCOUNT_ID') + '.r2.cloudflarestorage.com'
    bucket = require_env('R2_BUCKET')
    require(HOST.fullmatch(host) and BUCKET.fullmatch(bucket), 'cloud_storage_configuration')
    client = boto3.client('s3', endpoint_url='https://' + host,
        aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
        region_name='auto', config=Config(signature_version='s3v4', s3={'addressing_style': 'path'},
            connect_timeout=5 if read_only else 20, read_timeout=10 if read_only else 30,
            retries={'total_max_attempts': 1, 'mode': 'standard'},
            request_checksum_calculation='when_required', response_checksum_validation='when_required'))
    return client, bucket, host


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest='command', required=True)
    key = sub.add_parser('keygen'); key.add_argument('--session', required=True)
    for operation in ('mint', 'verify', 'import'):
        part = sub.add_parser(operation)
        part.add_argument('--repo', type=Path, required=True)
        part.add_argument('--manifest', type=Path, default=Path(__file__).with_name('reviewed-originals.json'))
        if operation in {'mint', 'verify'}:
            part.add_argument('--pending', type=Path, required=True)
            part.add_argument('--public-request', type=Path, required=True)
        if operation == 'mint':
            part.add_argument('--output', type=Path, required=True)
        if operation == 'import':
            part.add_argument('--session', required=True)
            part.add_argument('--envelope', type=Path, required=True)
            part.add_argument('--originals', type=Path, required=True)
            part.add_argument('--run-id', required=True)
            part.add_argument('--head-sha', required=True)
    args = parser.parse_args(argv)
    if args.command == 'keygen':
        return keygen(args.session)
    production = load_production(args.repo)
    rows = approved_manifest(args.manifest, production)
    if args.command in {'mint', 'verify'}:
        request, key = public_request(args.public_request)
        ctx = cloud_context(request)
        check_pending(rows, args.pending, production)
        if args.command == 'mint':
            client, bucket, host = cloud_client()
            plan = mint_plan(rows, request, client, bucket, host, ctx)
            write_new(args.output, encoded(seal(plan, key)))
            return {'status': 'encrypted_grants_created', 'manifest_sha256': MANIFEST_SHA256, 'originals': len(rows),
                    'expires_at': ctx['expires_at']}
        cache, verified, _ = production
        client, bucket, _ = cloud_client(read_only=True)
        original_cache = cache.OriginalCache.single_attempt(client, bucket)
        return cloud_readback(rows, original_cache, production)
    directory = session_directory(args.session)
    require(not directory.is_symlink() and stat.S_IMODE(directory.stat().st_mode) == 0o700
            and directory.stat().st_uid == os.getuid(), 'session_mode')
    request, _ = public_request(directory / 'public-request.json')
    private = read_file(directory / 'private.pem', 16384, mode=0o600)
    raw = read_file(args.envelope, MAX_ENVELOPE)
    plan, ctx = open_envelope(raw, private, request, args.run_id, args.head_sha, int(time.time()))
    validate_plan(plan, rows, ctx, int(time.time()))
    prepared = prepare_files(rows, args.originals, production)
    with requests_session() as session:
        return import_prepared(rows, prepared, plan, production, session)


if __name__ == '__main__':
    try:
        print(json.dumps(main(), sort_keys=True))
    except Exception as error:
        # Signed URLs and HTTP errors must never reach logs, including traceback.
        code = safe_error_code(error)
        print(json.dumps({'status': 'stopped', 'code': code}), file=sys.stderr)
        raise SystemExit(1) from None
