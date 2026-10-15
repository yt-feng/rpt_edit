"""Resume already admitted IMF originals from their private producer receipts.

This adapter only lists/reads the publication registry and immutable originals.
It does not discover sources, select a newest version, contact MinerU, or mark a
source seen. The ordinary successful handoff remains the commit boundary.
"""
from __future__ import annotations

import copy
import os
from pathlib import Path
import re
import tempfile
import time

from institution_original_cache import OriginalCache, MAX_PDF, validate_binding, validate_payload
from institution_pending_intake import validate_item
from institution_verified_originals import pdf_pages
from mineru_task_ledger import digest, encoded, exact_json

PREFIX = '_workflow-cache/institution-dependencies/v1/versions/'
MAX_RECORDS = 2000
MAX_REGISTRY_BYTES = 16 * 1024 * 1024
MAX_SECONDS = 120
RESUME_FIELDS = {'acquisition_method', 'admitted_original_resume'}


class AdmittedOriginalError(ValueError):
    """Fixed categories only; never expose remote credentials or exception text."""


def require(condition, code):
    if not condition:
        raise AdmittedOriginalError(code)


def _cache():
    from private_workflow_handoff import build_r2_client, r2_bucket
    return OriginalCache.single_attempt(build_r2_client(), r2_bucket())


def _publication(binding, row, item, filename):
    """Validate one complete previous official receipt and exact publication."""
    from institution_source_health import validate_live_download, validate_followup_download
    from fetch_institution_latest_pdfs import short_hash, slug
    validate_item(item)
    validate_binding(binding)
    require(filename == binding['source'] == f"IMF_{slug(item['title'])}_{short_hash('imf:' + item['guid'])}.pdf",
            'admitted_original_filename')
    require(isinstance(row, dict) and row.get('binding_id') == binding['id']
            and row.get('local_filename') == filename and row.get('sha256') == binding['sha256']
            and type(row.get('bytes')) is int and row['bytes'] == binding['size']
            and row.get('source_page_url') == item['source_url'] and row.get('published') == item['date']
            and row.get('feed_pdf_candidates') == item['pdf_candidates'] and row.get('title') == item['title'],
            'admitted_original_publication_identity')
    keys = {key for key in row if key == 'acquisition_method' or key.startswith(('imf_live_download', 'imf_official_followup',
                                                                              'verified_original_', 'admitted_original_'))}
    require(keys in ({'imf_live_download'}, {'imf_official_followup'}), 'admitted_original_official_proof')
    proof_key = next(iter(keys))
    try:
        (validate_live_download if proof_key == 'imf_live_download' else validate_followup_download)(row)
    except Exception:
        raise AdmittedOriginalError('admitted_original_official_proof') from None
    proof = row[proof_key]
    require(proof['source_guid'] == item['guid'], 'admitted_original_guid')
    return proof


def validate_resume(row):
    """Validate the carried prior receipt without calling it a fresh download."""
    require(row.get('acquisition_method') == 'admitted_original_cache' and row.get('institution') == 'imf',
            'admitted_original_resume_method')
    receipt = row.get('admitted_original_resume')
    require(isinstance(receipt, dict) and set(receipt) == {'schema', 'registry_sha256', 'binding', 'item', 'publication'}
            and type(receipt['schema']) is int and receipt['schema'] == 1
            and isinstance(receipt['registry_sha256'], str) and re.fullmatch('[a-f0-9]{64}', receipt['registry_sha256']),
            'admitted_original_resume_schema')
    proof = _publication(receipt['binding'], receipt['publication'], receipt['item'], row.get('local_filename'))
    require(all(row.get(key) == receipt['publication'].get(key)
                for key in ('title', 'source_page_url', 'published', 'pdf_url', 'sha256', 'bytes', 'feed_pdf_candidates')),
            'admitted_original_resume_identity')
    return proof


class AdmittedOriginals:
    def __init__(self, *, cache_factory=None, clock=time.monotonic):
        self.cache_factory = cache_factory or _cache
        self.clock, self.cache, self.records = clock, None, None
        self.load_error = None
        self.audit = {'list_requests': 0, 'metadata_reads': 0, 'registry_records': 0,
                      'registry_bytes': 0, 'registry_elapsed_seconds': 0}

    def _load(self):
        if self.load_error:
            raise AdmittedOriginalError(self.load_error)
        if self.records is not None:
            return
        started = self.clock()
        try:
            self._scan()
        except AdmittedOriginalError as exc:
            self.load_error = str(exc)
            raise
        finally:
            self.audit['registry_elapsed_seconds'] = round(self.clock() - started, 3)

    def _scan(self):
        from institution_dependency_backlog import Backlog, MAX_OBJECT
        if self.records is not None:
            return
        deadline = self.clock() + MAX_SECONDS
        try:
            self.cache = self.cache_factory()
        except Exception:
            raise AdmittedOriginalError('admitted_original_registry_unavailable') from None
        client, bucket = self.cache.client, self.cache.bucket
        keys, tokens, token = [], set(), None
        for _ in range(2):
            require(self.clock() < deadline, 'admitted_original_registry_deadline')
            kwargs = dict(Bucket=bucket, Prefix=PREFIX, MaxKeys=1000)
            if token:
                kwargs['ContinuationToken'] = token
            try:
                self.audit['list_requests'] += 1
                response = client.list_objects_v2(**kwargs)
            except Exception:
                raise AdmittedOriginalError('admitted_original_registry_list') from None
            require(isinstance(response, dict) and type(response.get('IsTruncated')) is bool
                    and isinstance(response.get('Contents', []), list) and len(response.get('Contents', [])) <= 1000,
                    'admitted_original_registry_listing')
            for entry in response.get('Contents', []):
                key = entry.get('Key') if isinstance(entry, dict) else None
                require(isinstance(key, str) and re.fullmatch(re.escape(PREFIX) + '[a-f0-9]{64}\\.json', key)
                        and type(entry.get('Size')) is int and 0 < entry['Size'] <= MAX_OBJECT
                        and key not in keys, 'admitted_original_registry_key')
                keys.append(key)
                self.audit['registry_records'] = len(keys)
            require(len(keys) <= MAX_RECORDS, 'admitted_original_registry_bound')
            if not response['IsTruncated']:
                break
            token = response.get('NextContinuationToken')
            require(isinstance(token, str) and 0 < len(token) <= 4096 and token not in tokens,
                    'admitted_original_registry_pagination')
            tokens.add(token)
        else:
            raise AdmittedOriginalError('admitted_original_registry_bound')
        backlog, records, total = Backlog(client, bucket), {}, 0
        for key in sorted(keys):
            require(self.clock() < deadline, 'admitted_original_registry_deadline')
            try:
                self.audit['metadata_reads'] += 1
                value, _ = backlog._read(key.removeprefix('_workflow-cache/institution-dependencies/v1/'))
                require(isinstance(value, dict), 'admitted_original_registry_disappeared')
                binding = value.get('binding')
                validate_binding(binding)
                require(key == PREFIX + binding['id'] + '.json', 'admitted_original_registry_binding')
                backlog.validate_versions(value, binding)
                total += len(encoded(value))
                self.audit['registry_bytes'] = total
                require(total <= MAX_REGISTRY_BYTES, 'admitted_original_registry_bound')
            except AdmittedOriginalError:
                raise
            except Exception:
                raise AdmittedOriginalError('admitted_original_registry_invalid') from None
            records.setdefault(binding['source'], []).append(value)
        require(self.clock() < deadline, 'admitted_original_registry_deadline')
        self.records = records

    def restore(self, item, filename, pending, destination, max_bytes, *, force=False, seen=None):
        key = 'imf:' + item['guid']
        # Ineligible paths do not even list private storage.
        if force or pending is None or key not in pending.initial_keys or key not in pending.items:
            return None
        if (seen or {}).get(key, {}).get('status') in {'downloaded', 'duplicate_pdf'}:
            return None
        require(exact_json(item, pending.items[key]['item']), 'admitted_original_pending_identity')
        self._load()
        candidates = self.records.get(filename, [])
        if not candidates:
            return None
        require(len(candidates) == 1, 'admitted_original_ambiguous_binding')
        value = candidates[0]; binding = value['binding']
        proofs = {}
        for row in value['versions']:
            # Every saved version must agree; never choose a convenient newer row.
            require(row.get('source_page_url') == item['source_url'] and row.get('published') == item['date']
                    and row.get('feed_pdf_candidates') == item['pdf_candidates'], 'admitted_original_version_conflict')
            if any(key.startswith(('imf_live_download', 'imf_official_followup')) for key in row):
                proof = _publication(binding, row, item, filename)
                proofs[digest(encoded(row))] = (row, proof)
        if not proofs:
            return None  # Legacy metadata alone cannot prove an official original.
        require(len(proofs) == 1, 'admitted_original_ambiguous_publication')
        row, proof = next(iter(proofs.values()))
        require(all(version.get('pdf_url') == row['pdf_url'] for version in value['versions']),
                'admitted_original_version_conflict')
        require(isinstance(value['receipts'], list) and bool(value['receipts'])
                and all(isinstance(entry, dict) and set(entry) == {'run_id', 'manifest_sha256'}
                        and isinstance(entry['run_id'], str) and re.fullmatch('[0-9]{1,24}', entry['run_id'])
                        and isinstance(entry['manifest_sha256'], str) and re.fullmatch('[a-f0-9]{64}', entry['manifest_sha256'])
                        for entry in value['receipts']), 'admitted_original_producer_receipt')
        require(binding['size'] <= min(max_bytes, MAX_PDF), 'admitted_original_size')
        try:
            payload = self.cache.get(binding)
            require(payload is not None, 'admitted_original_cache_missing')
            validate_payload(binding, payload)
            require(pdf_pages(payload) == proof['pages'], 'admitted_original_page_count')
        except AdmittedOriginalError:
            raise
        except Exception:
            raise AdmittedOriginalError('admitted_original_cache_invalid') from None
        destination = Path(destination)
        require(destination.name == filename and not destination.is_symlink()
                and (not destination.exists() or destination.is_file()), 'admitted_original_destination')
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=destination.parent, prefix='.admitted-original-', delete=False) as stream:
                temporary = Path(stream.name); stream.write(payload); stream.flush(); os.fsync(stream.fileno())
            temporary.replace(destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return {'pdf_url': row['pdf_url'], 'acquisition_method': 'admitted_original_cache',
                'admitted_original_resume': {'schema': 1, 'registry_sha256': digest(encoded(value)),
                    'binding': copy.deepcopy(binding), 'item': copy.deepcopy(item), 'publication': copy.deepcopy(row)}}
