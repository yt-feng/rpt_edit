"""Read exact accepted legacy Daily tasks and cache results without task admission.

Legacy provider data IDs remain copied-filename IDs in a separate namespace.
No ledger, task-submission, local OCR, model or publication operation is exposed.
"""
from __future__ import annotations

import argparse
import ast
import base64
from copy import deepcopy
import io
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import stat
import tempfile
import zipfile

import consume_legacy_mineru as consumer
import inspect_legacy_mineru as inspect
from mineru_result_cache import ResultCache, MAX_RECEIPT, validate_zip
from mineru_pinned_result_transport import (PinnedResultTransport, prepare_authentication,
    require_before_cutoff, require_cloud_manual, verified_authentication, verified_stored_authentication,
    fixed_result_uri, PinnedTransportError)
from recover_durable_mineru_sources import MANIFEST, PRODUCER, frozen_inputs, exact_date, digest, decode
from recover_legacy_mineru_cloud import Github
from seed_mineru_result_cache import CutoffCacheClient, SAFE_ERRORS as PIN_SAFE_ERRORS

PREFIX = '_workflow-cache/mineru-legacy-market-results/v1/dropbox'
PROOF_PREFIX = '_workflow-cache/mineru-legacy-market-proofs/v1/dropbox'
POLICY = 'complete-original-legacy-market-result-v1'
MAX_ARTIFACT = 512 * 1024 * 1024
MAX_LOG = 4 * 1024 * 1024
MAX_PROOF = 16 * 1024 * 1024
RUN = re.compile(r'[1-9][0-9]{0,19}')
SHA = re.compile(r'[a-f0-9]{40}')
HASH = re.compile(r'[a-f0-9]{64}')
# Exact reviewed historical implementation, independently checked at its
# original commit. Different source code requires a separate review.
ORIGINAL_CODE = {
    'scripts/run_pdf_to_xhs_in_batches.py': 'f0c32f8939e7f2cc9ed62ee15933b94204c1e23f66c2902162975f4ad6ecf5a5',
    'scripts/pdf_to_xhs_batch.py': '0b4335b767ea78e21cf8093b728b38d75637ccda2f906753dc34690c6f744c38',
    PRODUCER: '8321201191f6d42cab263cf4fb2657a7b9759d983297927de45b46501de7a343',
}
SAFE = {'original_producer', 'original_code', 'original_jobs', 'original_artifact',
        'original_artifact_hash', 'original_archive', 'original_archive_bounds',
        'original_group', 'original_map', 'original_membership', 'original_inputs_changed',
        'inspection_failed', 'inspection_membership_or_terminal', 'legacy_cache_receipt',
        'legacy_cache_readback', 'legacy_cache_identity', 'legacy_auth_receipt',
        'source_run_invalid', 'seed_failed'}


class LegacyError(ValueError):
    """Only literal category codes leave this module."""


def fail(category):
    raise LegacyError(category)


def canonical(value):
    return inspect.canonical(value)


def verify_producer(value, run_id, repository):
    if (not isinstance(value, dict) or type(value.get('id')) is not int
            or str(value['id']) != run_id or value.get('path') != PRODUCER
            or value.get('head_branch') != 'main' or value.get('status') != 'completed'
            or value.get('conclusion') not in {'success', 'failure'}
            or value.get('event') not in {'schedule', 'workflow_dispatch'}
            or value.get('repository', {}).get('full_name') != repository
            or value.get('head_repository', {}).get('full_name') != repository
            or not isinstance(value.get('head_sha'), str) or not SHA.fullmatch(value['head_sha'])):
        fail('original_producer')
    return value['head_sha']


def unpack_original_artifact(payload, destination):
    """Bound the complete authenticated archive, including unused members."""
    destination = Path(destination)
    if destination.exists() or destination.is_symlink() or not isinstance(payload, bytes) or not 1 <= len(payload) <= MAX_ARTIFACT:
        fail('original_archive')
    try:
        with zipfile.ZipFile(io.BytesIO(payload)) as archive:
            entries = archive.infolist()
            if not 1 <= len(entries) <= 1000 or sum(row.file_size for row in entries) > MAX_ARTIFACT:
                fail('original_archive_bounds')
            seen = set()
            for row in entries:
                name = row.orig_filename
                path = PurePosixPath(name)
                if (not name or len(name) > 1024 or path.is_absolute() or '\\' in name or ':' in name
                        or any(ord(c) < 32 for c in name) or row.flag_bits & 1
                        or any(p in {'', '.', '..'} for p in name.rstrip('/').split('/'))
                        or name.casefold() in seen or stat.S_IFMT(row.external_attr >> 16) not in {0, stat.S_IFREG, stat.S_IFDIR}
                        or row.file_size > consumer.MAX_MEMBER or row.file_size > max(1, row.compress_size) * 1000):
                    fail('original_archive')
                seen.add(name.casefold())
            destination.mkdir(mode=0o700, parents=True)
            for row in entries:
                path = destination / PurePosixPath(row.orig_filename)
                if row.is_dir():
                    path.mkdir(mode=0o700, parents=True, exist_ok=True)
                    continue
                path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
                with archive.open(row) as source, path.open('xb') as out:
                    total = 0
                    while block := source.read(65536):
                        total += len(block)
                        if total > row.file_size:
                            fail('original_archive_bounds')
                        out.write(block)
                path.chmod(0o600)
                if total != row.file_size:
                    fail('original_archive')
            manifests = list(destination.rglob(MANIFEST))
            if len(manifests) != 1:
                fail('original_archive')
            return manifests[0]
    except (zipfile.BadZipFile, RuntimeError, EOFError, OSError):
        fail('original_archive')


def original_group(log, names, *, shard, total, job_id, run_id):
    """One entire wrapper group, every recorded accepted retry, no membership union."""
    if not isinstance(log, bytes) or len(log) > MAX_LOG:
        fail('original_group')
    try:
        lines = log.decode('utf-8-sig').splitlines()
    except UnicodeError:
        fail('original_group')
    lines = [re.sub(r'^\d{4}-\d{2}-\d{2}T[0-9:.]+Z\s+', '', line) for line in lines]
    found = [re.fullmatch(r'Found ([0-9]+) total PDFs; shard ([0-9]+)/([0-9]+) has ([0-9]+) PDFs, skips 0 already converted, will process ([0-9]+) PDFs with batch_size=5\.', line) for line in lines]
    found = [match for match in found if match]
    if (len(found) != 1 or [int(found[0][index]) for index in (1, 2, 4, 5)] != [total, shard, len(names), len(names)]
            or int(found[0][3]) < math.ceil(total / 5)):
        fail('original_group')
    running = [line for line in lines if re.fullmatch(r'Running batch [0-9]+: [0-9]+ PDFs', line)]
    if running != [f'Running batch 1: {len(names)} PDFs']:
        fail('original_group')
    accepted = []
    submissions = []
    uploads = []
    current_uploads = []
    maps = []
    for line in lines:
        match = re.fullmatch(r'MinerU attempt ([1-9][0-9]*) using (MINER_U(?:_[234])?) batch_id=([a-f0-9-]{36})', line)
        if match:
            if not inspect.valid_uuid(match[3]):
                fail('original_group')
            accepted.append({'attempt': int(match[1]), 'credential_slot': match[2], 'batch_id': match[3]})
            uploads.append(current_uploads)
            current_uploads = []
        elif (match := re.fullmatch(r'MinerU attempt ([1-9][0-9]*)/([1-9][0-9]*) using (MINER_U(?:_[234])?): submitting ([1-9][0-9]*) PDF\(s\)\.', line)):
            submissions.append((int(match[1]), match[3], int(match[4])))
        elif line.startswith('Uploading PDF to MinerU: '):
            current_uploads.append(PurePosixPath(line.removeprefix('Uploading PDF to MinerU: ')).name)
        elif line.startswith('Batch 1 failed: '):
            if len(line) > 128 * 1024:
                fail('original_group')
            try:
                maps.append(ast.literal_eval(line.removeprefix('Batch 1 failed: ')))
            except (ValueError, SyntaxError, RecursionError):
                fail('original_group')
    if (not 1 <= len(accepted) <= 4 or len({row['batch_id'] for row in accepted}) != len(accepted)
            or [row['attempt'] for row in accepted] != list(range(1, len(accepted) + 1))
            or len(maps) != 1 or not isinstance(maps[0], dict)):
        fail('original_group')
    summary = maps[0]
    files = summary.get('files')
    if (type(summary.get('batch_index')) is not int or summary['batch_index'] != 1
            or type(summary.get('pdf_count')) is not int or summary['pdf_count'] != len(names)
            or type(summary.get('returncode')) is not int or summary['returncode'] == 0
            or summary.get('status') != 'failed' or not isinstance(files, list) or len(files) != len(names)):
        fail('original_group')
    members = []
    for index, (row, name) in enumerate(zip(files, names), 1):
        if (not isinstance(row, dict) or set(row) != {'source', 'batch_file', 'stable_index'}
                or not all(isinstance(row[key], str) for key in row)
                or any('\\' in row[key] for key in ('source', 'batch_file'))
                or PurePosixPath(row['source']).name != name
                or PurePosixPath(row['source']).parent.name != '_selected_macro_pdfs'
                or PurePosixPath(row['batch_file']).parent.name != 'pdfs'
                or PurePosixPath(row['batch_file']).name != consumer.copied_name(name, index)
                or row['stable_index'] != str(index)):
            fail('original_map')
        alias = consumer.copied_name(name, index)
        members.append({'source_pdf': name, 'source_filename': alias, 'data_id': consumer.data_id(alias)})
    ids = [row['data_id'] for row in members]
    if (len(set(ids)) != len(ids) or current_uploads
            or submissions != [(row['attempt'], row['credential_slot'], len(names)) for row in accepted]
            or uploads != [[row['source_filename'] for row in members] for _ in accepted]):
        fail('original_membership')
    batches = [{'run_id': run_id, 'job_id': job_id, 'batch_id': row['batch_id'],
                'credential_slot': row['credential_slot'], 'expected_data_ids': ids} for row in accepted]
    inspect.validate_request({'schema_version': 1, 'batches': batches})
    return {'shard': shard, 'job_id': job_id, 'job_log_sha256': digest(log),
            'accepted': accepted, 'members': members, 'batches': batches}


def authenticate(api, run_id, repository, destination, expected_reports, date_folder, *, artifact_id=''):
    """All original bytes, jobs and implementation precede provider/result reads."""
    exact_date(date_folder)
    root = f'repos/{repository}/'
    run = api.get(root + f'actions/runs/{run_id}')
    execution_sha = verify_producer(run, run_id, repository)
    if not ORIGINAL_CODE or set(ORIGINAL_CODE) != {'scripts/run_pdf_to_xhs_in_batches.py', 'scripts/pdf_to_xhs_batch.py', PRODUCER}:
        fail('original_code')
    for path, expected in ORIGINAL_CODE.items():
        source = api.get(root + f'contents/{path}?ref={execution_sha}')
        try:
            raw = base64.b64decode(source['content'], validate=False)
        except (KeyError, ValueError, TypeError):
            fail('original_code')
        if source.get('path') != path or source.get('encoding') != 'base64' or digest(raw) != expected:
            fail('original_code')
    if artifact_id:
        artifact = api.get(root + f'actions/artifacts/{artifact_id}')
    else:
        listing = api.get(root + f'actions/runs/{run_id}/artifacts?per_page=100')
        if type(listing.get('total_count')) is not int or listing['total_count'] > 100 or not isinstance(listing.get('artifacts'), list):
            fail('original_artifact')
        candidates = [row for row in listing['artifacts'] if row.get('name') == f'selected-macro-pdfs-{run_id}']
        if len(candidates) != 1:
            fail('original_artifact')
        artifact = candidates[0]
    if (not isinstance(artifact, dict) or type(artifact.get('id')) is not int or artifact['id'] < 1
            or artifact.get('name') != f'selected-macro-pdfs-{run_id}' or artifact.get('expired') is not False
            or artifact.get('workflow_run', {}).get('id') != int(run_id)
            or type(artifact.get('size_in_bytes')) is not int or not 1 <= artifact['size_in_bytes'] <= MAX_ARTIFACT
            or not isinstance(artifact.get('digest'), str) or not re.fullmatch(r'sha256:[a-f0-9]{64}', artifact['digest'])):
        fail('original_artifact')
    archive = api.raw(root + f'actions/artifacts/{artifact["id"]}/zip', MAX_ARTIFACT, redirect=True)
    if len(archive) != artifact['size_in_bytes'] or digest(archive) != artifact['digest'].split(':')[1]:
        fail('original_artifact_hash')
    manifest = unpack_original_artifact(archive, destination)
    raw, bindings, pairs = frozen_inputs(destination, manifest, expected_reports, date_folder)
    if any(PurePosixPath(row['dropbox_path']).parts[:3] != ('/', 'zip_backup', date_folder) for row in bindings):
        fail('original_membership')
    jobs = api.get(root + f'actions/runs/{run_id}/jobs?filter=latest&per_page=100')
    if (type(jobs.get('total_count')) is not int or not 1 <= jobs['total_count'] <= 100
            or not isinstance(jobs.get('jobs'), list) or len(jobs['jobs']) != jobs['total_count']):
        fail('original_jobs')
    names = sorted(row['source_pdf'] for row in bindings)
    groups = []
    for shard in range(math.ceil(len(names) / 5)):
        candidates = [row for row in jobs['jobs'] if row.get('name') == f'process-shard ({shard})']
        if len(candidates) != 1:
            fail('original_jobs')
        job = candidates[0]
        if (type(job.get('id')) is not int or job['id'] < 1 or job.get('run_id') != int(run_id)
                or job.get('head_sha') != execution_sha or job.get('status') != 'completed'
                or job.get('conclusion') not in {'success', 'failure'}):
            fail('original_jobs')
        log = api.raw(root + f'actions/jobs/{job["id"]}/logs', MAX_LOG, redirect=True)
        # The checkout's actual HEAD, not only the run metadata, must identify
        # the implementation whose exact file bytes were reviewed above.
        log_lines = [re.sub(r'^\d{4}-\d{2}-\d{2}T[0-9:.]+Z\s+', '', line)
                     for line in log.decode('utf-8-sig').splitlines()]
        heads = [log_lines[index + 1] for index, line in enumerate(log_lines[:-1])
                 if re.fullmatch(r'\[command\].*/git log -1 --format=%H', line)]
        if heads != [execution_sha]:
            fail('original_code')
        groups.append(original_group(log, names[shard * 5:(shard + 1) * 5], shard=shard,
                                     total=len(names), job_id=str(job['id']), run_id=run_id))
    batches = [row for group in groups for row in group['batches']]
    inspect.validate_request({'schema_version': 1, 'batches': batches})
    authority = {'schema_version': 1, 'repository': repository, 'workflow_path': PRODUCER,
                 'run_id': run_id, 'execution_sha': execution_sha, 'date_folder': date_folder,
                 'manifest_sha256': digest(raw), 'artifact_id': str(artifact['id']),
                 'artifact_zip_sha256': digest(archive), 'code_sha256': ORIGINAL_CODE,
                 'expected_reports': expected_reports, 'groups': groups, 'original_inventory': bindings,
                 'original_sizes': {source: path.stat().st_size for path, source in pairs}}
    authority['authority_sha256'] = digest(canonical(authority))
    return authority, Path(manifest), pairs


def complete_results(authority, credentials, *, getter=inspect.get_once):
    request = {'schema_version': 1, 'batches': [row for group in authority['groups'] for row in group['batches']]}
    public, private = inspect.inspect_batches(request, credentials, getter=getter)
    if public['network_stop'] or public['uninspected_count'] or len(public['batches']) != len(request['batches']):
        fail('inspection_failed')
    if any(row.get('membership_proven') is not True or row.get('identified_complete') is not True for row in public['batches']):
        fail('inspection_membership_or_terminal')
    observed = {row['input']['batch_id']: row for row in private['batches']}
    by_name = {row['source_pdf']: row for row in authority['original_inventory']}
    selected = []
    unresolved_groups = 0
    for group in authority['groups']:
        chosen = next((row for row in group['accepted'] if next(p for p in public['batches'] if p['batch_id'] == row['batch_id']).get('all_succeeded') is True), None)
        if chosen is None:
            unresolved_groups += 1
            continue
        original = observed[chosen['batch_id']]
        rows = {row['data_id']: row for row in original['provider_response']['data']['extract_result']}
        for member in group['members']:
            binding = {**deepcopy(by_name[member['source_pdf']]), 'run_id': authority['run_id'],
                'execution_sha': authority['execution_sha'], 'manifest_sha256': authority['manifest_sha256'],
                'artifact_zip_sha256': authority['artifact_zip_sha256'], 'job_id': group['job_id'],
                'job_log_sha256': group['job_log_sha256'], 'batch_id': chosen['batch_id'],
                'data_id': member['data_id'], 'credential_slot': chosen['credential_slot'],
                'source_filename': member['source_filename'], 'options': {'model': 'vlm', 'language': 'en', 'ocr': True,
                    'enable_table': True, 'enable_formula': True},
                'original_pdf_bytes': authority['original_sizes'][member['source_pdf']]}
            fixed_result_uri(rows[member['data_id']]['full_zip_url'])
            selected.append((binding, rows[member['data_id']]['full_zip_url']))
    states = {}
    for batch in public['batches']:
        for state, count in batch.get('state_counts', {}).items():
            states[state] = states.get(state, 0) + count
    return selected, {'provider_gets': public['provider_gets'], 'original_batch_count': len(request['batches']),
                      'terminal_original_groups': len(authority['groups']), 'unresolved_original_groups': unresolved_groups,
                      'recoverable_original_members': len(selected), 'accepted_retry_member_state_counts': states}, private


def binding_identity(binding):
    keys = {'source_pdf', 'original_filename', 'content_sha256', 'dropbox_path', 'run_id', 'execution_sha',
            'manifest_sha256', 'artifact_zip_sha256', 'job_id', 'job_log_sha256', 'batch_id', 'data_id',
            'credential_slot', 'source_filename', 'options', 'original_pdf_bytes'}
    if not isinstance(binding, dict) or set(binding) != keys:
        fail('legacy_cache_identity')
    for field in {'content_sha256', 'manifest_sha256', 'artifact_zip_sha256', 'job_log_sha256'}:
        if not isinstance(binding[field], str) or not HASH.fullmatch(binding[field]):
            fail('legacy_cache_identity')
    if (not isinstance(binding['execution_sha'], str) or not SHA.fullmatch(binding['execution_sha'])
            or any(not isinstance(binding[field], str) or not RUN.fullmatch(binding[field]) for field in ('run_id', 'job_id'))
            or not inspect.valid_uuid(binding['batch_id']) or binding['credential_slot'] not in inspect.SLOTS
            or not isinstance(binding['data_id'], str) or not inspect.ID_RE.fullmatch(binding['data_id'])
            or not isinstance(binding['source_filename'], str) or consumer.data_id(binding['source_filename']) != binding['data_id']
            or binding['options'] != {'model': 'vlm', 'language': 'en', 'ocr': True, 'enable_table': True, 'enable_formula': True}
            or type(binding['original_pdf_bytes']) is not int or not 1 <= binding['original_pdf_bytes'] <= consumer.MAX_MEMBER):
        fail('legacy_cache_identity')
    for field in ('source_pdf', 'source_filename'):
        consumer.basename(binding[field])
    if (not isinstance(binding['original_filename'], str) or not 1 <= len(binding['original_filename']) <= 1024
            or any(ord(c) < 32 for c in binding['original_filename']) or not isinstance(binding['dropbox_path'], str)
            or len(binding['dropbox_path']) > 4096 or '\\' in binding['dropbox_path']
            or any(ord(c) < 32 for c in binding['dropbox_path'])):
        fail('legacy_cache_identity')
    return digest(canonical(binding))


class LegacyResultCache(ResultCache):
    """Reuse bounded immutable storage, with genuine legacy task identities."""

    def preserve_proof(self, authority, private):
        raw = canonical({'schema_version': 1, 'authority': authority, 'inspection': private,
                         'canonical_task_admission': False, 'provider_posts': 0})
        checksum = digest(raw)
        if len(raw) > MAX_PROOF:
            fail('inspection_failed')
        self._immutable(f'{PROOF_PREFIX}/{checksum}.json', raw, content_type='application/json',
                        identity_sha=checksum, maximum=MAX_PROOF)
        return checksum

    def get(self, binding):
        checksum = binding_identity(binding)
        receipt_key = f'{PREFIX}/{checksum}/receipt.json'
        raw = self._read(receipt_key, maximum=MAX_RECEIPT, content_type='application/json', identity_sha=checksum, allow_missing=True)
        if raw is None:
            return None
        receipt = decode(raw)
        if (not isinstance(receipt, dict) or set(receipt) != {'schema_version', 'policy', 'identity_sha256',
                'binding', 'zip_sha256', 'zip_bytes', 'blob_key', 'authentication_receipt_sha256', 'canonical_task_admission'}
                or type(receipt.get('schema_version')) is not int or receipt['schema_version'] != 1
                or receipt.get('policy') != POLICY or receipt.get('identity_sha256') != checksum
                or canonical(receipt.get('binding')) != canonical(binding) or receipt.get('canonical_task_admission') is not False
                or not isinstance(receipt.get('zip_sha256'), str) or not HASH.fullmatch(receipt['zip_sha256'])
                or not isinstance(receipt.get('authentication_receipt_sha256'), str) or not HASH.fullmatch(receipt['authentication_receipt_sha256'])
                or type(receipt.get('zip_bytes')) is not int or not 1 <= receipt['zip_bytes'] <= consumer.MAX_ZIP
                or receipt.get('blob_key') != f'{PREFIX}/{checksum}/{receipt["zip_sha256"]}.zip'):
            fail('legacy_cache_receipt')
        payload = self._read(receipt['blob_key'], maximum=consumer.MAX_ZIP, content_type='application/zip', identity_sha=checksum)
        auth = self._read(f'{PREFIX}/{checksum}/auth-{receipt["zip_sha256"]}.json', maximum=MAX_RECEIPT,
                          content_type='application/json', identity_sha=checksum)
        value = decode(auth)
        if (digest(auth) != receipt['authentication_receipt_sha256'] or not isinstance(value, dict)
                or set(value) != {'schema_version', 'binding', 'identity_sha256', 'zip_sha256', 'zip_bytes', 'authentication',
                    'terminal_proof_sha256', 'canonical_task_admission'}
                or type(value.get('schema_version')) is not int or value['schema_version'] != 1
                or canonical(value.get('binding')) != canonical(binding) or value.get('identity_sha256') != checksum
                or value.get('zip_sha256') != digest(payload) or value.get('zip_bytes') != len(payload)
                or value.get('canonical_task_admission') is not False
                or not isinstance(value.get('terminal_proof_sha256'), str) or not HASH.fullmatch(value['terminal_proof_sha256'])):
            fail('legacy_auth_receipt')
        verified_stored_authentication(value['authentication'])
        proof = self._read(f'{PROOF_PREFIX}/{value["terminal_proof_sha256"]}.json',
                           maximum=MAX_PROOF, content_type='application/json',
                           identity_sha=value['terminal_proof_sha256'])
        if digest(proof) != value['terminal_proof_sha256']:
            fail('legacy_auth_receipt')
        snapshot = decode(proof)
        authority = snapshot.get('authority') if isinstance(snapshot, dict) else None
        if (not isinstance(authority, dict) or set(snapshot) != {'schema_version', 'authority', 'inspection', 'canonical_task_admission', 'provider_posts'}
                or snapshot.get('canonical_task_admission') is not False or type(snapshot.get('provider_posts')) is not int
                or snapshot['provider_posts'] != 0 or type(snapshot.get('schema_version')) is not int or snapshot['schema_version'] != 1
                or digest(canonical({key: item for key, item in authority.items() if key != 'authority_sha256'})) != authority.get('authority_sha256')
                or authority.get('run_id') != binding['run_id'] or authority.get('execution_sha') != binding['execution_sha']
                or authority.get('manifest_sha256') != binding['manifest_sha256']
                or authority.get('artifact_zip_sha256') != binding['artifact_zip_sha256']
                or authority.get('code_sha256') != ORIGINAL_CODE):
            fail('legacy_auth_receipt')
        if len(payload) != receipt['zip_bytes'] or digest(payload) != receipt['zip_sha256']:
            fail('legacy_cache_receipt')
        validate_zip(payload)
        return payload

    def put(self, binding, payload, authentication, terminal_proof_sha256):
        verified_authentication(authentication)
        validate_zip(payload)
        if not isinstance(terminal_proof_sha256, str) or not HASH.fullmatch(terminal_proof_sha256):
            fail('legacy_auth_receipt')
        checksum, zip_sha = binding_identity(binding), digest(payload)
        if self.get(binding) is not None:
            if self.get(binding) != payload:
                fail('legacy_cache_readback')
            return
        auth = canonical({'schema_version': 1, 'binding': binding, 'identity_sha256': checksum,
                          'zip_sha256': zip_sha, 'zip_bytes': len(payload), 'authentication': authentication,
                          'canonical_task_admission': False, 'terminal_proof_sha256': terminal_proof_sha256})
        # Authentication binds the exact bytes first, before the result receipt.
        self._immutable(f'{PREFIX}/{checksum}/auth-{zip_sha}.json', auth, content_type='application/json',
                        identity_sha=checksum, maximum=MAX_RECEIPT)
        blob = f'{PREFIX}/{checksum}/{zip_sha}.zip'
        self._immutable(blob, payload, content_type='application/zip', identity_sha=checksum, maximum=consumer.MAX_ZIP)
        receipt = canonical({'schema_version': 1, 'policy': POLICY, 'identity_sha256': checksum, 'binding': binding,
            'zip_sha256': zip_sha, 'zip_bytes': len(payload), 'blob_key': blob,
            'authentication_receipt_sha256': digest(auth), 'canonical_task_admission': False})
        self._immutable(f'{PREFIX}/{checksum}/receipt.json', receipt, content_type='application/json',
                        identity_sha=checksum, maximum=MAX_RECEIPT)
        if self.get(binding) != payload:
            fail('legacy_cache_readback')


def seed_results(authority, manifest, input_dir, credentials, cache, *, max_results=1,
                 getter=inspect.get_once, transport_factory=None, cutoff_check=require_before_cutoff):
    if type(max_results) is not int or max_results not in {0, 1}:
        fail('original_membership')
    if digest(canonical({key: value for key, value in authority.items() if key != 'authority_sha256'})) != authority.get('authority_sha256'):
        fail('original_membership')
    raw, bindings, _ = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
    if digest(raw) != authority['manifest_sha256'] or bindings != authority['original_inventory']:
        fail('original_inputs_changed')
    cutoff_check()
    results, counts, private = complete_results(authority, credentials, getter=getter)
    fresh, fresh_bindings, _ = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
    if fresh != raw or fresh_bindings != bindings:
        fail('original_inputs_changed')
    selected = results if max_results == 0 else results[:1]
    proof_sha = None
    if selected:
        cutoff_check()
        proof_sha = cache.preserve_proof(authority, private)
    summary = {'schema_version': 1, 'success': False, 'category': 'legacy_cache_seed_only',
               'canonical_task_admission': False, 'complete_source_handoff': False, 'production_acceptance': False,
               'pipeline_restored': False, 'provider_posts': 0, 'ledger_writes': 0, 'model_calls': 0, 'pdf_count': 0,
               'date_folder': authority['date_folder'], 'source_run_id': authority['run_id'],
               'manifest_sha256': authority['manifest_sha256'], 'original_file_count': authority['expected_reports'],
               'unique_original_content_count': len({row['content_sha256'] for row in bindings}),
               'authority_sha256': authority['authority_sha256'], **counts, 'selected_results': len(selected),
               'terminal_proof_sha256': proof_sha,
               'cached_results': 0, 'new_result_downloads': 0, 'existing_cache_hits': 0, 'results': []}
    transport = None
    for binding, url in selected:
        cutoff_check()
        payload = cache.get(binding)
        if payload is None:
            if transport is None:
                transport = transport_factory() if transport_factory else PinnedResultTransport(prepare_authentication())
            payload = transport(url)
            validate_zip(payload)
            final, current, _ = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
            if final != raw or current != bindings:
                fail('original_inputs_changed')
            cutoff_check()
            cache.put(binding, payload, transport.authentication, proof_sha)
            summary['new_result_downloads'] += 1
        else:
            summary['existing_cache_hits'] += 1
        if cache.get(binding) != payload:
            fail('legacy_cache_readback')
        summary['cached_results'] += 1
        summary['results'].append({'identity_sha256': digest(canonical(binding)), 'zip_sha256': digest(payload),
                                   'zip_bytes': len(payload), 'auth_mode': 'exact_leaf_pin'})
    final, current, _ = frozen_inputs(input_dir, manifest, authority['expected_reports'], authority['date_folder'])
    if final != raw or current != bindings:
        fail('original_inputs_changed')
    summary['result_gets'] = transport.result_gets if transport else 0
    summary['authentication'] = deepcopy(transport.authentication) if transport else None
    summary['success'] = bool(selected) and summary['cached_results'] == len(selected)
    if not selected:
        summary['category'] = 'legacy_no_complete_result_batch'
    summary['all_original_results_cached'] = len(selected) == len(results) == authority['expected_reports'] == summary['cached_results']
    return summary, private


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--artifact-id', default='')
    parser.add_argument('--max-results', choices=('1', 'all'), default='1')
    parser.add_argument('--summary', type=Path, required=True)
    args = parser.parse_args(argv)
    summary = {'schema_version': 1, 'success': False, 'category': 'seed_failed', 'provider_posts': 0,
               'ledger_writes': 0, 'model_calls': 0, 'pdf_count': 0, 'canonical_task_admission': False,
               'complete_source_handoff': False, 'production_acceptance': False, 'pipeline_restored': False}
    try:
        require_cloud_manual()
        require_before_cutoff()
        if not RUN.fullmatch(args.source_run_id) or args.artifact_id and not RUN.fullmatch(args.artifact_id):
            fail('source_run_invalid')
        from private_workflow_handoff import require_env
        import boto3
        from botocore.config import Config
        client = boto3.client('s3', endpoint_url=f'https://{require_env("R2_ACCOUNT_ID")}.r2.cloudflarestorage.com',
            aws_access_key_id=require_env('R2_ACCESS_KEY_ID'), aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'),
            region_name='auto', config=Config(connect_timeout=20, read_timeout=30,
            retries={'total_max_attempts': 1, 'mode': 'standard'}))
        cache = LegacyResultCache(CutoffCacheClient(client, require_before_cutoff), require_env('R2_BUCKET'))
        with tempfile.TemporaryDirectory(prefix='legacy-market-originals-') as temporary:
            input_dir = Path(temporary) / 'originals'
            authority, manifest, _ = authenticate(Github(require_env('GH_TOKEN')), args.source_run_id,
                require_env('GITHUB_REPOSITORY'), input_dir, args.expected_reports, args.date_folder, artifact_id=args.artifact_id)
            credentials = {slot: os.environ.get(slot, '') for slot in inspect.SLOTS}
            summary, _ = seed_results(authority, manifest, input_dir, credentials, cache,
                                     max_results=0 if args.max_results == 'all' else 1)
        code = 0 if summary['success'] else 3
    except Exception as error:
        if (isinstance(error, (LegacyError, PinnedTransportError)) and len(error.args) == 1
                and type(error.args[0]) is str and error.args[0] in SAFE | PIN_SAFE_ERRORS):
            summary['category'] = error.args[0]
        code = 2
    from audit_market_views_ocr_receipt import write_summary
    write_summary(args.summary, summary, source_dir=Path('_selected_macro_pdfs'))
    print(json.dumps(summary, sort_keys=True))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
