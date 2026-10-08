"""Private immutable original PDFs, verified before institution submission.

Only an exact content-addressed original is reusable. A storage failure stops
submission; no request is replayed after a lost acknowledgement.
"""
from __future__ import annotations

from pathlib import Path
import re

from mineru_task_ledger import R2Store, digest, encoded, exact_json, validate_source
from mineru_result_cache import ResultCache, missing

PREFIX = '_workflow-cache/institution-originals/v1/'
MAX_PDF = 64 * 1024 * 1024
MAX_TOTAL = 512 * 1024 * 1024
OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}
HASH = re.compile(r'[a-f0-9]{64}')


class OriginalCacheError(ValueError):
    """Fixed diagnostic categories; no source names, URLs or credentials."""


def require(condition, code):
    if not condition:
        raise OriginalCacheError(code)


def validate_binding(binding):
    require(isinstance(binding, dict) and set(binding) ==
            {'source', 'sha256', 'size', 'scope', 'endpoint', 'options', 'id'}, 'original_binding')
    require(binding['scope'] == 'institution' and binding['endpoint'] == 'https://mineru.net'
            and exact_json(binding['options'], OPTIONS), 'original_options')
    require(type(binding['size']) is int and 1 <= binding['size'] <= MAX_PDF
            and isinstance(binding['sha256'], str) and HASH.fullmatch(binding['sha256'])
            and isinstance(binding['id'], str) and HASH.fullmatch(binding['id']), 'original_identity')
    try:
        validate_source(binding['source'])
    except Exception:
        raise OriginalCacheError('original_source') from None
    require(digest(encoded({k: v for k, v in binding.items() if k != 'id'})) == binding['id'],
            'original_binding_hash')


def validate_payload(binding, payload):
    validate_binding(binding)
    require(isinstance(payload, bytes) and len(payload) == binding['size']
            and payload.startswith(b'%PDF-') and digest(payload) == binding['sha256'], 'original_bytes')


class OriginalCache:
    def __init__(self, client, bucket):
        require(isinstance(bucket, str) and bool(bucket.strip()), 'original_bucket')
        self.client, self.bucket = client, bucket

    @classmethod
    def single_attempt(cls, client, bucket):
        configured = ResultCache.single_attempt(client, bucket)
        return cls(configured.client, configured.bucket)

    @staticmethod
    def key(binding):
        validate_binding(binding)
        return PREFIX + binding['sha256'] + '.pdf'

    def get(self, binding):
        key = self.key(binding)
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
        except Exception as error:
            if missing(error):
                return None
            raise OriginalCacheError('original_read_failed') from None
        body = response.get('Body')
        try:
            require(type(response.get('ContentLength')) is int
                    and response['ContentLength'] == binding['size']
                    and response.get('ContentType') == 'application/pdf'
                    and response.get('Metadata') == {'sha256': binding['sha256'], 'kind': 'institution-original-proof'}
                    and callable(getattr(body, 'read', None)), 'original_metadata')
            try:
                payload = body.read(binding['size'] + 1)
            except Exception:
                raise OriginalCacheError('original_read_failed') from None
            validate_payload(binding, payload)
            return payload
        finally:
            close = getattr(body, 'close', None)
            if callable(close):
                close()

    def put(self, binding, payload):
        """Return True for a verified existing object; False for a new write."""
        validate_payload(binding, payload)
        previous = self.get(binding)
        if previous is not None:
            require(previous == payload, 'original_conflict')
            return True
        reused = False
        try:
            self.client.put_object(Bucket=self.bucket, Key=self.key(binding), Body=payload,
                ContentType='application/pdf', Metadata={'sha256': binding['sha256'], 'kind': 'institution-original-proof'},
                CacheControl='private, no-store', IfNoneMatch='*')
        except Exception as error:
            status = getattr(error, 'response', {}).get('ResponseMetadata', {}).get('HTTPStatusCode')
            if type(status) is not int or status not in {409, 412}:
                # An unknown write result is not permission for another remote
                # operation. A later run can verify the immutable object.
                raise OriginalCacheError('original_write_unresolved') from None
            reused = True
        require(self.get(binding) == payload, 'original_readback')
        return reused


def _local_payload(path):
    path = Path(path)
    require(path.is_file() and not path.is_symlink() and 1 <= path.stat().st_size <= MAX_PDF,
            'original_local_size')
    with path.open('rb') as handle:
        payload = handle.read(MAX_PDF + 1)
    require(len(payload) <= MAX_PDF, 'original_local_size')
    return payload


def preserve_sources(ledger, sources):
    """Validate the whole selection before storage, then verify every archive.

    This function never touches provider or ledger state. The caller must only
    enter ledger.run after it returns successfully.
    """
    if ledger.scope != 'institution':
        return {'status': 'not_applicable', 'originals': 0, 'bytes': 0, 'reused': 0}
    require(isinstance(ledger.store, R2Store), 'original_private_store_required')
    sources = list(sources)
    require(bool(sources), 'original_sources_empty')
    prepared, identities, total = [], set(), 0
    for path, source in sources:
        payload = _local_payload(path)
        binding = ledger.bind(path, source)
        validate_payload(binding, payload)
        require(binding['id'] not in identities, 'original_duplicate')
        identities.add(binding['id'])
        total += len(payload)
        require(total <= MAX_TOTAL, 'original_total_size')
        prepared.append((Path(path), binding))
    cache = OriginalCache.single_attempt(ledger.store.client, ledger.store.bucket)
    reused = 0
    for path, binding in prepared:
        payload = _local_payload(path)
        validate_payload(binding, payload)
        reused += int(cache.put(binding, payload))
    return {'status': 'verified', 'originals': len(prepared), 'bytes': total, 'reused': reused}
