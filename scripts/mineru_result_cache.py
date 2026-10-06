"""Immutable private R2 cache of complete, source-bound MinerU result ZIPs.

The current provider GET and complete original membership gate remain mandatory.
Only result delivery is cached; URLs, credentials and provider responses are not.
"""
from __future__ import annotations

import json
from pathlib import Path
import re
import tempfile

from consume_legacy_mineru import MAX_ZIP, safe_unzip
from mineru_task_ledger import digest, encoded, exact_json, validate_source

PREFIX = '_workflow-cache/mineru-results/v1/dropbox'
POLICY = 'complete-source-bound-mineru-result-v1'
MAX_RECEIPT = 64 * 1024
HASH = re.compile(r'[a-f0-9]{64}')
BATCH = re.compile(r'batches/[a-f0-9]{32}')
OPTIONS = {'model': 'vlm', 'language': 'en', 'ocr': True}


class ResultCacheError(ValueError):
    """Fixed categories only, without private object or provider URL details."""


def reject(category):
    raise ResultCacheError(category)


def identity(source_binding, lineage):
    if (not isinstance(source_binding, dict) or set(source_binding) !=
            {'source', 'sha256', 'size', 'scope', 'endpoint', 'options', 'id'}
            or source_binding['scope'] != 'dropbox' or source_binding['endpoint'] != 'https://mineru.net'
            or not isinstance(source_binding['options'], dict)
            or set(source_binding['options']) != {'model', 'language', 'ocr'}
            or not all(isinstance(source_binding['options'][key], str) and source_binding['options'][key]
                       for key in ('model', 'language')) or type(source_binding['options']['ocr']) is not bool
            or type(source_binding['size']) is not int or source_binding['size'] < 1
            or not isinstance(source_binding['sha256'], str) or not HASH.fullmatch(source_binding['sha256'])
            or not isinstance(source_binding['id'], str) or not HASH.fullmatch(source_binding['id'])):
        reject('cache_source_binding')
    validate_source(source_binding['source'])
    base = {key: value for key, value in source_binding.items() if key != 'id'}
    if digest(encoded(base)) != source_binding['id']:
        reject('cache_source_identity')
    if (not isinstance(lineage, dict) or set(lineage) !=
            {'batch_id', 'batch_key', 'parent_batch_key', 'data_id', 'child_ordinal'}
            or not isinstance(lineage['batch_id'], str)
            or not re.fullmatch(r'[A-Za-z0-9_-]{1,128}', lineage['batch_id'])
            or any(not isinstance(lineage[key], str) or not BATCH.fullmatch(lineage[key])
                   for key in ('batch_key', 'parent_batch_key'))
            or lineage['data_id'] != source_binding['id']
            or type(lineage['child_ordinal']) is not int or not 0 <= lineage['child_ordinal'] <= 3
            or (lineage['batch_key'] == lineage['parent_batch_key']) != (lineage['child_ordinal'] == 0)):
        reject('cache_task_binding')
    value = {'source_binding': source_binding, 'lineage': lineage}
    return digest(encoded(value))


def validate_zip(payload):
    # Inspect every ZIP entry and verify its complete CRC-backed bytes before
    # either publishing a receipt or trusting a retrieved cache object.
    with tempfile.TemporaryDirectory(prefix='mineru-result-cache-') as temporary:
        safe_unzip(payload, Path(temporary) / 'raw')


def missing(error):
    response = getattr(error, 'response', {})
    return response.get('ResponseMetadata', {}).get('HTTPStatusCode') == 404


def conflict(error):
    response = getattr(error, 'response', {})
    return (str(response.get('Error', {}).get('Code', '')) in
            {'PreconditionFailed', 'ConditionalRequestConflict', '409', '412'}
            or response.get('ResponseMetadata', {}).get('HTTPStatusCode') in {409, 412})


class ResultCache:
    def __init__(self, client, bucket):
        if not isinstance(bucket, str) or not bucket.strip():
            reject('cache_bucket_required')
        self.client, self.bucket = client, bucket

    @classmethod
    def single_attempt(cls, client, bucket):
        """Keep cache PUT/GET calls single-attempt without changing the ledger.

        Injected non-SDK clients already implement one call. For a botocore
        client with retries enabled, create a dedicated cache-only client from
        the same private R2 environment; leave every other consumer unchanged.
        """
        metadata = getattr(client, 'meta', None)
        if metadata is None:
            return cls(client, bucket)
        retries = getattr(getattr(metadata, 'config', None), 'retries', {}) or {}
        if retries.get('total_max_attempts') == 1:
            return cls(client, bucket)
        import boto3
        from botocore.config import Config
        from private_workflow_handoff import require_env
        configured = boto3.client('s3',
            endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto', config=Config(connect_timeout=20, read_timeout=30,
                retries={'total_max_attempts': 1, 'mode': 'standard'}))
        return cls(configured, bucket)

    @staticmethod
    def receipt_key(identity_sha):
        return f'{PREFIX}/{identity_sha}/receipt.json'

    @staticmethod
    def blob_key(identity_sha, zip_sha):
        return f'{PREFIX}/{identity_sha}/{zip_sha}.zip'

    def _read(self, key, *, maximum, content_type, identity_sha, allow_missing=False):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
        except Exception as error:
            if missing(error):
                if allow_missing:
                    return None
                reject('cache_object_missing')
            reject('cache_read_failed')
        body = response.get('Body')
        try:
            length, metadata = response.get('ContentLength'), response.get('Metadata')
            if (type(length) is not int or not 1 <= length <= maximum
                    or response.get('ContentType') != content_type or not isinstance(metadata, dict)
                    or set(metadata) != {'sha256', 'identity-sha256'}
                    or metadata['identity-sha256'] != identity_sha
                    or not isinstance(metadata['sha256'], str) or not HASH.fullmatch(metadata['sha256'])
                    or body is None or not callable(getattr(body, 'read', None))):
                reject('cache_object_metadata')
            try:
                payload = body.read(maximum + 1)
            except Exception:
                reject('cache_read_failed')
            if (not isinstance(payload, bytes) or len(payload) != length
                    or digest(payload) != metadata['sha256']):
                reject('cache_object_hash')
            return payload
        finally:
            close = getattr(body, 'close', None)
            if callable(close):
                close()

    def _immutable(self, key, payload, *, content_type, identity_sha, maximum):
        try:
            self.client.put_object(Bucket=self.bucket, Key=key, Body=payload,
                ContentType=content_type, Metadata={'sha256': digest(payload), 'identity-sha256': identity_sha},
                IfNoneMatch='*')
        except Exception as error:
            # A definite conflict never grants ownership. A lost ACK permits
            # only a read-back, not a second conditional write.
            category = 'cache_write_conflict' if conflict(error) else 'cache_write_unresolved'
            stored = self._read(key, maximum=maximum, content_type=content_type,
                                identity_sha=identity_sha, allow_missing=True)
            if stored != payload:
                reject(category)
            return
        stored = self._read(key, maximum=maximum, content_type=content_type, identity_sha=identity_sha)
        if stored != payload:
            reject('cache_write_readback')

    def get(self, source_binding, lineage):
        identity_sha = identity(source_binding, lineage)
        raw = self._read(self.receipt_key(identity_sha), maximum=MAX_RECEIPT,
                         content_type='application/json', identity_sha=identity_sha, allow_missing=True)
        if raw is None:
            return None
        def pairs(values):
            result = {}
            for key, value in values:
                if key in result:
                    reject('cache_receipt_json')
                result[key] = value
            return result
        try:
            receipt = json.loads(raw, object_pairs_hook=pairs)
        except (ValueError, UnicodeError):
            reject('cache_receipt_json')
        if (not isinstance(receipt, dict) or set(receipt) !=
                {'schema_version', 'policy', 'identity_sha256', 'source_binding', 'lineage', 'zip_sha256', 'zip_bytes', 'blob_key'}
                or type(receipt['schema_version']) is not int or receipt['schema_version'] != 1
                or receipt['policy'] != POLICY or receipt['identity_sha256'] != identity_sha
                or not exact_json(receipt['source_binding'], source_binding)
                or not exact_json(receipt['lineage'], lineage)
                or not isinstance(receipt['zip_sha256'], str) or not HASH.fullmatch(receipt['zip_sha256'])
                or type(receipt['zip_bytes']) is not int or not 1 <= receipt['zip_bytes'] <= MAX_ZIP
                or receipt['blob_key'] != self.blob_key(identity_sha, receipt['zip_sha256'])):
            reject('cache_receipt_binding')
        payload = self._read(receipt['blob_key'], maximum=MAX_ZIP, content_type='application/zip',
                             identity_sha=identity_sha)
        if len(payload) != receipt['zip_bytes'] or digest(payload) != receipt['zip_sha256']:
            reject('cache_zip_receipt')
        validate_zip(payload)
        return payload

    def put(self, source_binding, lineage, payload):
        identity_sha = identity(source_binding, lineage)
        validate_zip(payload)
        existing = self.get(source_binding, lineage)
        if existing is not None:
            if existing != payload:
                reject('cache_result_differs')
            return existing
        zip_sha = digest(payload)
        blob = self.blob_key(identity_sha, zip_sha)
        self._immutable(blob, payload, content_type='application/zip', identity_sha=identity_sha, maximum=MAX_ZIP)
        receipt = encoded({'schema_version': 1, 'policy': POLICY, 'identity_sha256': identity_sha,
                           'source_binding': source_binding, 'lineage': lineage, 'zip_sha256': zip_sha,
                           'zip_bytes': len(payload), 'blob_key': blob})
        self._immutable(self.receipt_key(identity_sha), receipt, content_type='application/json',
                        identity_sha=identity_sha, maximum=MAX_RECEIPT)
        stored = self.get(source_binding, lineage)
        if stored != payload:
            reject('cache_complete_readback')
        return stored
