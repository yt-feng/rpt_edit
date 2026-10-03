"""Consume an authenticated, complete legacy consulting result as source-only data.

The reviewed cloud caller authenticates the original job, manifest artifact and
inspection receipt before supplying their frozen bytes and context. This module
does not fetch PDFs, submit/poll MinerU, rotate credentials or admit canonical tasks.
"""
from __future__ import annotations

import argparse
import ast
import base64
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import http.client
import io
import ipaddress
import json
import os
from pathlib import Path, PurePosixPath
import re
import shutil
import ssl
import stat
import tempfile
import time
import unicodedata
import urllib.error
import urllib.parse
import urllib.request
import zipfile

from inspect_legacy_mineru import MAX_BODY, canonical, classify_response, validate_request

MAX_METADATA = 3 * 1024 * 1024
MAX_LOG = 16 * 1024 * 1024
MAX_ZIP = 128 * 1024 * 1024
MAX_EXPANDED = 512 * 1024 * 1024
MAX_MEMBER = 128 * 1024 * 1024
MAX_FILES = 2000
MAX_MARKDOWN = 8 * 1024 * 1024
MAX_JOB_MEMBERS = 5
WORKFLOW = '.github/workflows/consulting-latest-pdf-to-wechat.yml'
SHA = re.compile(r'[a-f0-9]{64}')
UUID = re.compile(r'[a-f0-9]{8}-[a-f0-9]{4}-4[a-f0-9]{3}-[89ab][a-f0-9]{3}-[a-f0-9]{12}')
DECIMAL_ID = re.compile(r'[1-9][0-9]{0,19}')


class ConsumerError(ValueError):
    """Only fixed categories are exposed by the CLI."""


class ResultHTTPError(ConsumerError):
    def __init__(self, status):
        super().__init__('result_http')
        self.category = 'result_http'
        self.http_status = status if type(status) is int and 100 <= status <= 599 else 0


class NetworkStop(ConsumerError):
    pass


def fail(category):
    raise ConsumerError(category)


def digest(raw):
    return hashlib.sha256(raw).hexdigest()


def decode(raw, maximum=MAX_METADATA):
    if not isinstance(raw, bytes) or len(raw) > maximum:
        fail('input_size')
    def pairs(values):
        result = {}
        for key, value in values:
            if key in result:
                fail('duplicate_json_key')
            result[key] = value
        return result
    try:
        value = json.loads(raw, object_pairs_hook=pairs)
    except (UnicodeError, ValueError, RecursionError) as exc:
        if isinstance(exc, ConsumerError):
            raise
        fail('input_json')
    if not isinstance(value, dict):
        fail('input_contract')
    return value


def basename(value):
    if (not isinstance(value, str) or not 1 <= len(value) <= 512 or value in {'.', '..'}
            or any(ord(c) < 32 for c in value) or '/' in value or '\\' in value
            or ':' in value or not value.lower().endswith('.pdf')):
        fail('filename_contract')
    return value


def copied_name(filename, index):
    safe = ''.join(c if c.isalnum() or c in '._-()[] ' else '-' for c in filename).strip()
    return f'{index:04d}-{safe or "report.pdf"}'


def data_id(filename):
    return re.sub(r'[^A-Za-z0-9._-]+', '_', filename)[:128]


def output_name(filename):
    stem = re.sub(r'\.pdf$', '', filename, flags=re.I)
    return re.sub(r'[^A-Za-z0-9._-]+', '-', stem).strip('-._')[:80] or 'report'


def original_group(log_bytes, manifest_bytes, context):
    keys = {'schema_version', 'repository', 'workflow_path', 'run_id', 'job_id',
            'execution_source_sha', 'job_log_sha256', 'manifest_sha256', 'inspection_receipt_sha256'}
    if (not isinstance(context, dict) or set(context) != keys
            or type(context['schema_version']) is not int or context['schema_version'] != 1
            or context['repository'] != 'yt-feng/rpt_edit' or context['workflow_path'] != WORKFLOW
            or any(not isinstance(context[k], str) or not DECIMAL_ID.fullmatch(context[k]) for k in ('run_id', 'job_id'))
            or not isinstance(context['execution_source_sha'], str)
            or not re.fullmatch(r'[a-f0-9]{40}', context['execution_source_sha'])
            or any(not isinstance(context[k], str) or not SHA.fullmatch(context[k])
                   for k in ('job_log_sha256', 'manifest_sha256', 'inspection_receipt_sha256'))
            or len(log_bytes) > MAX_LOG or digest(log_bytes) != context['job_log_sha256']
            or digest(manifest_bytes) != context['manifest_sha256']):
        fail('original_context')
    manifest = decode(manifest_bytes)
    rows = manifest.get('downloaded')
    if (not isinstance(rows, list) or not 1 <= len(rows) <= 200
            or type(manifest.get('downloaded_count')) is not int or manifest['downloaded_count'] != len(rows)
            or not isinstance(manifest.get('date'), str) or not re.fullmatch(r'[0-9]{6}', manifest['date'])):
        fail('original_manifest')
    names = [basename(row.get('local_filename')) if isinstance(row, dict) else fail('original_manifest') for row in rows]
    if len(set(names)) != len(names):
        fail('original_manifest')
    try:
        lines = log_bytes.decode('utf-8').splitlines()
    except UnicodeError:
        fail('original_log')
    groups = []; group = None
    for raw in lines:
        line = re.sub(r'^\d{4}-\d{2}-\d{2}T[0-9:.]+Z\s+', '', raw)
        match = re.fullmatch(r'Running batch ([1-9][0-9]*): ([1-9][0-9]*) PDFs', line)
        if match:
            group = {'index': int(match[1]), 'count': int(match[2]), 'accepted': [], 'files': None}
            groups.append(group)
            continue
        match = re.fullmatch(r'MinerU attempt ([1-9][0-9]*) using (MINER_U(?:_[234])?) batch_id=(' + UUID.pattern + ')', line)
        if match:
            if group is None:
                fail('original_log')
            group['accepted'].append({'attempt': int(match[1]), 'credential_slot': match[2], 'batch_id': match[3]})
            continue
        match = re.fullmatch(r'Batch ([1-9][0-9]*) failed: (.+)', line)
        if match:
            if group is None or int(match[1]) != group['index'] or len(match[2]) > 128 * 1024:
                fail('original_log')
            try:
                result = ast.literal_eval(match[2])
            except (ValueError, SyntaxError, RecursionError):
                fail('original_log')
            if (not isinstance(result, dict) or result.get('batch_index') != group['index']
                    or result.get('pdf_count') != group['count'] or not isinstance(result.get('files'), list)
                    or type(result.get('returncode')) is not int or result['returncode'] == 0
                    or result.get('status') != 'failed'
                    or group['files'] is not None):
                fail('original_log')
            group['files'] = result['files']
    # Version 1 consumes one whole original wrapper job/group, never a partial
    # selection or unions of different retry memberships.
    if len(groups) != 1 or groups[0]['files'] is None:
        fail('original_group_incomplete')
    group = groups[0]
    if (not 1 <= group['count'] <= MAX_JOB_MEMBERS or len(group['files']) != group['count']
            or len(names) != group['count'] or not 1 <= len(group['accepted']) <= 100):
        fail('original_group_incomplete')
    members = []
    for row in group['files']:
        if not isinstance(row, dict) or set(row) != {'source', 'batch_file', 'stable_index'}:
            fail('original_file_map')
        if (not isinstance(row['source'], str) or not isinstance(row['batch_file'], str)
                or '\\' in row['source'] or '\\' in row['batch_file']
                or not isinstance(row['stable_index'], str) or not re.fullmatch(r'[1-9][0-9]{0,5}', row['stable_index'])):
            fail('original_file_map')
        original = basename(PurePosixPath(row['source']).name)
        alias = basename(PurePosixPath(row['batch_file']).name)
        if (original not in names or PurePosixPath(row['source']).parent.name != '_consulting_latest_pdfs'
                or PurePosixPath(row['batch_file']).parent.name != 'pdfs'
                or int(row['stable_index']) != sorted(names).index(original) + 1
                or alias != copied_name(original, int(row['stable_index']))):
            fail('original_file_map')
        members.append({'data_id': data_id(alias), 'source_filename': alias, 'original_filename': original})
    if (len({m['data_id'] for m in members}) != len(members)
            or {m['original_filename'] for m in members} != set(names)
            or len({output_name(m['source_filename']).casefold() for m in members}) != len(members)
            or len({a['batch_id'] for a in group['accepted']}) != len(group['accepted'])
            or [a['attempt'] for a in group['accepted']] != list(range(1, len(group['accepted']) + 1))):
        fail('original_identity_collision')
    return {'date_folder': manifest['date'], 'members': members, 'accepted': group['accepted']}


def prepare(receipt_bytes, object_loader, log_bytes, manifest_bytes, context):
    group = original_group(log_bytes, manifest_bytes, context)
    if digest(receipt_bytes) != context['inspection_receipt_sha256']:
        fail('inspection_receipt_hash')
    receipt = decode(receipt_bytes, 256 * 1024)
    if (set(receipt) != {'schema_version', 'policy', 'producer', 'input', 'input_canonical_sha256', 'objects',
                         'original_source_bytes_proven', 'historical_token_fingerprint_proven', 'canonical_task_admission'}
            or receipt.get('schema_version') != 1 or type(receipt['schema_version']) is not int
            or receipt['policy'] != 'legacy-provider-inspection-only-v1'
            or any(receipt[k] is not False for k in ('original_source_bytes_proven',
                'historical_token_fingerprint_proven', 'canonical_task_admission'))):
        fail('inspection_receipt_contract')
    try:
        request = validate_request(receipt['input'])
    except Exception:
        fail('inspection_request')
    request_hash = digest(canonical(request))
    producer = receipt['producer']
    if (receipt['input_canonical_sha256'] != request_hash or not isinstance(producer, dict)
            or set(producer) != {'run_id', 'attempt', 'sha'}
            or any(not isinstance(producer[k], str) or not DECIMAL_ID.fullmatch(producer[k]) for k in ('run_id', 'attempt'))
            or not isinstance(producer['sha'], str) or not re.fullmatch(r'[a-f0-9]{40}', producer['sha'])):
        fail('inspection_producer')
    selected = [b for b in request['batches'] if b['run_id'] == context['run_id'] and b['job_id'] == context['job_id']]
    accepted = {a['batch_id']: a for a in group['accepted']}
    if {b['batch_id'] for b in selected} != set(accepted) or len(selected) != len(accepted):
        fail('original_batch_coverage')
    descriptors = receipt['objects']
    if not isinstance(descriptors, list) or len(descriptors) > 100:
        fail('inspection_objects')
    objects = {}
    request_ids = {b['batch_id'] for b in request['batches']}
    for desc in descriptors:
        if (not isinstance(desc, dict) or set(desc) != {'batch_id', 'object', 'sha256', 'bytes'}
                or desc['batch_id'] not in request_ids or desc['batch_id'] in objects
                or not isinstance(desc['sha256'], str) or not SHA.fullmatch(desc['sha256'])
                or type(desc['bytes']) is not int or not 1 <= desc['bytes'] <= MAX_METADATA):
            fail('inspection_objects')
        expected = f"{producer['run_id']}-{producer['attempt']}/{request_hash}/{desc['batch_id']}-{desc['sha256']}.json"
        if desc['object'] != expected:
            fail('inspection_object_path')
        objects[desc['batch_id']] = desc
    members = {m['data_id']: m for m in group['members']}
    complete = {}
    for batch in selected:
        identity = batch['batch_id']
        if (batch['credential_slot'] != accepted[identity]['credential_slot']
                or set(batch['expected_data_ids']) != set(members) or len(batch['expected_data_ids']) != len(members)
                or identity not in objects):
            fail('original_membership')
        descriptor = objects[identity]
        raw = object_loader(descriptor['object'])
        if not isinstance(raw, bytes) or len(raw) != descriptor['bytes'] or digest(raw) != descriptor['sha256']:
            fail('inspection_object_hash')
        obj = decode(raw)
        if (set(obj) != {'input', 'input_canonical_sha256', 'http_status', 'response_sha256',
                        'raw_response_base64', 'provider_response'} or obj['input'] != batch
                or obj['input_canonical_sha256'] != digest(canonical(batch))
                or not isinstance(obj['raw_response_base64'], str)
                or len(obj['raw_response_base64']) > 4 * ((MAX_BODY + 2) // 3)):
            fail('inspection_object_contract')
        try:
            body = base64.b64decode(obj['raw_response_base64'], validate=True)
        except (ValueError, TypeError):
            fail('inspection_response')
        if len(body) > MAX_BODY or digest(body) != obj['response_sha256'] or decode(body, MAX_BODY) != obj['provider_response']:
            fail('inspection_response_hash')
        public, _ = classify_response(obj['http_status'], body, batch)
        if not public['membership_proven'] or not public['identified_complete']:
            fail('original_membership_or_terminal')
        if public['all_succeeded']:
            complete[identity] = (obj, descriptor)
    chosen = next((a['batch_id'] for a in group['accepted'] if a['batch_id'] in complete), None)
    if chosen is None:
        fail('no_complete_original_batch')
    obj, descriptor = complete[chosen]
    rows = {r['data_id']: r for r in obj['provider_response']['data']['extract_result']}
    ordered = [{**member, 'result': rows[member['data_id']]} for member in group['members']]
    plan = {'context': context, 'date_folder': group['date_folder'], 'inspection_request_sha256': request_hash,
            'selected_batch_id': chosen, 'selected_credential_slot': accepted[chosen]['credential_slot'],
            'selected_object_sha256': descriptor['sha256'], 'selected_response_sha256': obj['response_sha256'],
            'verified_original_batches': len(selected), 'members': ordered}
    plan['prepared_contract_sha256'] = digest(canonical(plan))
    return plan


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *_):
        return None


def valid_url(url):
    if not isinstance(url, str) or len(url) > 8192 or any(ord(c) < 33 for c in url):
        fail('result_url')
    try:
        parsed = urllib.parse.urlsplit(url)
        port = parsed.port
    except ValueError:
        fail('result_url')
    if (parsed.scheme != 'https' or not parsed.hostname or parsed.username or parsed.password
            or port not in (None, 443) or parsed.fragment):
        fail('result_url')
    try:
        ipaddress.ip_address(parsed.hostname)
    except ValueError:
        if parsed.hostname in {'localhost', 'local'} or parsed.hostname.endswith(('.localhost', '.local')):
            fail('result_url')
    else:
        fail('result_url')


def download_once(url, *, timeout=20):
    valid_url(url)
    if type(timeout) is not int or not 10 <= timeout <= 30:
        fail('timeout')
    opener = urllib.request.build_opener(NoRedirect)
    request = urllib.request.Request(url, method='GET')
    start = time.monotonic()
    try:
        with opener.open(request, timeout=timeout) as response:
            if response.status != 200:
                raise ResultHTTPError(response.status)
            length = response.headers.get('Content-Length')
            if length is not None and (not re.fullmatch(r'[0-9]{1,12}', length) or int(length) > MAX_ZIP):
                fail('zip_size')
            chunks = []; size = 0
            while True:
                if time.monotonic() - start > 120:
                    raise NetworkStop('network_stop')
                chunk = response.read(min(65536, MAX_ZIP + 1 - size))
                if not chunk:
                    break
                chunks.append(chunk); size += len(chunk)
                if size > MAX_ZIP:
                    fail('zip_size')
            if length is not None and size != int(length):
                raise NetworkStop('network_stop')
            return b''.join(chunks)
    except urllib.error.HTTPError as error:
        status = error.code
        error.close()
        raise ResultHTTPError(status) from None
    except (urllib.error.URLError, OSError, TimeoutError, http.client.HTTPException) as error:
        reason = error.reason if isinstance(error, urllib.error.URLError) else error
        if isinstance(reason, ssl.SSLCertVerificationError) and getattr(reason, 'verify_code', None) == 10:
            raise NetworkStop('tls_certificate_expired') from None
        raise NetworkStop('network_stop') from None


def safe_unzip(raw, root):
    if not isinstance(raw, bytes) or not 1 <= len(raw) <= MAX_ZIP:
        fail('zip_size')
    try:
        with zipfile.ZipFile(io.BytesIO(raw)) as archive:
            entries = archive.infolist()
            if not entries or len(entries) > MAX_FILES:
                fail('zip_member_count')
            names = set(); total = 0
            for info in entries:
                original = info.orig_filename
                path = PurePosixPath(original.rstrip('/'))
                mode = info.external_attr >> 16
                normalized = unicodedata.normalize('NFKC', str(path)).casefold()
                if (not original or len(original) > 1024 or '\\' in original or ':' in original
                        or any(ord(c) < 32 for c in original) or path.is_absolute()
                        or any(part in {'', '.', '..'} for part in original.rstrip('/').split('/'))
                        or normalized in names or info.flag_bits & 1
                        or stat.S_IFMT(mode) not in (0, stat.S_IFREG, stat.S_IFDIR)):
                    fail('zip_path')
                names.add(normalized)
                total += info.file_size
                if info.file_size > MAX_MEMBER or total > MAX_EXPANDED or info.file_size > max(1, info.compress_size) * 1000:
                    fail('zip_expansion')
            root.mkdir(parents=True)
            for info in entries:
                target = root / PurePosixPath(info.orig_filename.rstrip('/'))
                if info.is_dir():
                    target.mkdir(parents=True, exist_ok=True); continue
                target.parent.mkdir(parents=True, exist_ok=True)
                with archive.open(info) as source, target.open('xb') as out:
                    size = 0
                    while True:
                        chunk = source.read(65536)
                        if not chunk:
                            break
                        size += len(chunk)
                        if size > info.file_size or size > MAX_MEMBER:
                            fail('zip_expansion')
                        out.write(chunk)
                if size != info.file_size:
                    fail('zip_integrity')
    except (zipfile.BadZipFile, RuntimeError, EOFError, OSError):
        fail('zip_integrity')
    markdowns = [p for p in root.rglob('*.md') if p.is_file()]
    full = [p for p in markdowns if p.name == 'full.md']
    eligible = full if full else markdowns
    if len(eligible) != 1:
        fail('markdown_ambiguous')
    markdown = eligible[0].read_bytes()
    if not 1 <= len(markdown) <= MAX_MARKDOWN:
        fail('markdown_size')
    try:
        if not markdown.decode('utf-8').strip():
            fail('markdown_empty')
    except UnicodeError:
        fail('markdown_encoding')
    return markdown


def chart_assets(raw_dir, assets_dir, maximum):
    from pdf_to_xhs_batch import create_chart_source_assets
    # The cloud caller receives only fixed public counts, not producer filenames.
    with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
        return create_chart_source_assets(raw_dir, assets_dir, maximum)


def materialize(plan, destination, *, downloader=download_once, asset_writer=chart_assets, max_images=28):
    if (not isinstance(plan, dict) or not isinstance(plan.get('prepared_contract_sha256'), str)
            or digest(canonical({k: v for k, v in plan.items() if k != 'prepared_contract_sha256'})) != plan['prepared_contract_sha256']):
        fail('prepared_contract')
    if type(max_images) is not int or not 0 <= max_images <= 100:
        fail('image_limit')
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        fail('destination_exists')
    destination.parent.mkdir(parents=True, exist_ok=True)
    stage = Path(tempfile.mkdtemp(prefix='.legacy-result-', dir=destination.parent))
    downloads = 0
    try:
        statuses = []
        for member in plan['members']:
            url = member['result']['full_zip_url']; valid_url(url)
            downloads += 1
            raw = downloader(url)
            directory = stage / output_name(member['source_filename'])
            markdown = safe_unzip(raw, directory / 'mineru_raw')
            (directory / 'source_mineru.md').write_bytes(markdown)
            assets = directory / 'assets'; assets.mkdir()
            images = asset_writer(directory / 'mineru_raw', assets, max_images)
            if (not isinstance(images, list) or len(images) > max_images
                    or not all(isinstance(image, str) for image in images) or len(set(images)) != len(images)):
                fail('image_contract')
            for ordinal, image in enumerate(images, 1):
                if (not isinstance(image, str) or not re.fullmatch(r'assets/source_image_' + f'{ordinal:02d}' + r'\.(?:png|jpe?g|webp|gif|bmp|tiff?)', image)
                        or not (directory / image).is_file() or (directory / image).is_symlink()):
                    fail('image_contract')
            mapping = decode((directory / 'source_image_map.json').read_bytes())
            if (mapping.get('version') != 1 or mapping.get('source_sha256') != digest(markdown)
                    or not isinstance(mapping.get('images'), dict)
                    or any(not isinstance(ref, str) or target not in images for ref, target in mapping['images'].items())):
                fail('image_map_contract')
            status = {
                'source_pdf': member['source_filename'], 'original_filename': member['original_filename'],
                'mineru_state': 'done', 'chart_source_only': True, 'source_markdown': 'source_mineru.md',
                'images': images, 'chart_source_image_count': len(images),
                'original_source_bytes_proven': False, 'original_pdf_sha256': None,
                'canonical_task_admission': False,
                'legacy_result': {'run_id': plan['context']['run_id'], 'job_id': plan['context']['job_id'],
                    'batch_id': plan['selected_batch_id'], 'data_id': member['data_id'],
                    'credential_slot': plan['selected_credential_slot'], 'zip_sha256': digest(raw),
                    'source_markdown_sha256': digest(markdown),
                    'inspection_receipt_sha256': plan['context']['inspection_receipt_sha256'],
                    'provider_response_sha256': plan['selected_response_sha256']},
            }
            (directory / 'status.json').write_bytes(canonical(status))
            statuses.append(status)
        files = []
        for path in sorted(stage.rglob('*')):
            if path.is_symlink():
                fail('output_contract')
            if path.is_file():
                payload = path.read_bytes()
                files.append({'path': path.relative_to(stage).as_posix(), 'sha256': digest(payload), 'bytes': len(payload)})
        receipt = {'schema_version': 1, 'policy': 'legacy-source-only-consumption-v1',
            'context': plan['context'], 'date_folder': plan['date_folder'],
            'selected_batch_id': plan['selected_batch_id'], 'selected_credential_slot': plan['selected_credential_slot'],
            'verified_original_batches': plan['verified_original_batches'], 'source_count': len(statuses),
            'selected_object_sha256': plan['selected_object_sha256'],
            'selected_response_sha256': plan['selected_response_sha256'],
            'original_source_bytes_proven': False, 'original_pdf_sha256': None, 'canonical_task_admission': False,
            'historical_token_fingerprint_proven': False, 'provider_posts': 0, 'provider_gets': 0,
            'paid_requests': 0, 'new_submissions': 0, 'result_downloads': downloads,
            'reports': statuses, 'files': files}
        encoded = canonical(receipt)
        output = stage / '_legacy_output_receipt.json'
        output.write_bytes(encoded); output.chmod(0o600)
        verify_materialized_output(stage, encoded)
        os.replace(stage, destination)
        return {'status': 'legacy-source-only-complete', 'source_count': len(statuses),
                'verified_original_batches': plan['verified_original_batches'],
                'legacy_output_receipt_sha256': digest(encoded),
                'original_source_bytes_proven': False, 'original_pdf_sha256': None,
                'canonical_task_admission': False, 'provider_posts': 0, 'provider_gets': 0,
                'paid_requests': 0, 'new_submissions': 0, 'result_downloads': downloads}
    finally:
        if stage.exists():
            shutil.rmtree(stage)


def verify_materialized_output(root, receipt_bytes):
    """Verify a frozen private source-only receipt before any downstream use.

    The cloud caller must authenticate receipt_bytes against its immutable R2
    descriptor. A locally supplied receipt alone is not historical admission.
    """
    root = Path(root)
    if root.is_symlink() or not root.is_dir(): fail('materialized_root')
    receipt = decode(receipt_bytes)
    keys = {'schema_version', 'policy', 'context', 'date_folder', 'selected_batch_id',
            'selected_credential_slot', 'verified_original_batches', 'source_count',
            'selected_object_sha256', 'selected_response_sha256', 'original_source_bytes_proven',
            'original_pdf_sha256', 'canonical_task_admission', 'historical_token_fingerprint_proven',
            'provider_posts', 'provider_gets', 'paid_requests', 'new_submissions', 'result_downloads', 'reports', 'files'}
    if (set(receipt) != keys or type(receipt['schema_version']) is not int or receipt['schema_version'] != 1
            or receipt['policy'] != 'legacy-source-only-consumption-v1'
            or any(receipt[k] is not False for k in ('original_source_bytes_proven', 'canonical_task_admission', 'historical_token_fingerprint_proven'))
            or receipt['original_pdf_sha256'] is not None
            or any(type(receipt[k]) is not int or receipt[k] != 0 for k in ('provider_posts', 'provider_gets', 'paid_requests', 'new_submissions'))
            or type(receipt['source_count']) is not int or not 1 <= receipt['source_count'] <= MAX_JOB_MEMBERS
            or type(receipt['result_downloads']) is not int or receipt['result_downloads'] != receipt['source_count']
            or type(receipt['verified_original_batches']) is not int or not 1 <= receipt['verified_original_batches'] <= 100
            or not isinstance(receipt['date_folder'], str) or not re.fullmatch(r'[0-9]{6}', receipt['date_folder'])
            or not isinstance(receipt['selected_batch_id'], str) or not UUID.fullmatch(receipt['selected_batch_id'])
            or receipt['selected_credential_slot'] not in ('MINER_U', 'MINER_U_2', 'MINER_U_3', 'MINER_U_4')
            or any(not isinstance(receipt[k], str) or not SHA.fullmatch(receipt[k]) for k in ('selected_object_sha256', 'selected_response_sha256'))):
        fail('materialized_receipt_contract')
    context = receipt['context']
    if (not isinstance(context, dict) or set(context) != {'schema_version', 'repository', 'workflow_path', 'run_id', 'job_id',
            'execution_source_sha', 'job_log_sha256', 'manifest_sha256', 'inspection_receipt_sha256'}
            or type(context['schema_version']) is not int or context['schema_version'] != 1
            or context['repository'] != 'yt-feng/rpt_edit' or context['workflow_path'] != WORKFLOW
            or any(not isinstance(context[k], str) or not DECIMAL_ID.fullmatch(context[k]) for k in ('run_id', 'job_id'))
            or not isinstance(context['execution_source_sha'], str) or not re.fullmatch(r'[a-f0-9]{40}', context['execution_source_sha'])
            or any(not isinstance(context[k], str) or not SHA.fullmatch(context[k])
                   for k in ('job_log_sha256', 'manifest_sha256', 'inspection_receipt_sha256'))):
        fail('materialized_context')
    local_receipt = root / '_legacy_output_receipt.json'
    if local_receipt.is_symlink() or not local_receipt.is_file() or local_receipt.read_bytes() != receipt_bytes:
        fail('materialized_receipt_hash')
    rows = receipt['files']
    if not isinstance(rows, list) or not 1 <= len(rows) <= MAX_JOB_MEMBERS * (MAX_FILES + 103):
        fail('materialized_files')
    declared = {}
    for row in rows:
        if (not isinstance(row, dict) or set(row) != {'path', 'sha256', 'bytes'}
                or not isinstance(row['path'], str) or not 1 <= len(row['path']) <= 1024
                or '\\' in row['path'] or ':' in row['path'] or any(ord(x) < 32 for x in row['path'])
                or row['path'].startswith('/') or any(p in ('', '.', '..') for p in row['path'].split('/'))
                or not isinstance(row['sha256'], str) or not SHA.fullmatch(row['sha256'])
                or type(row['bytes']) is not int or not 0 <= row['bytes'] <= MAX_MEMBER):
            fail('materialized_files')
        folded = unicodedata.normalize('NFKC', row['path']).casefold()
        if folded in declared: fail('materialized_files')
        declared[folded] = row
    actual = {}
    for path in root.rglob('*'):
        if path.is_symlink(): fail('materialized_files')
        if path.is_dir(): continue
        if not stat.S_ISREG(path.stat().st_mode): fail('materialized_files')
        relative = path.relative_to(root).as_posix()
        if relative == '_legacy_output_receipt.json': continue
        folded = unicodedata.normalize('NFKC', relative).casefold()
        row = declared.get(folded)
        if row is None or row['path'] != relative or path.stat().st_size != row['bytes']:
            fail('materialized_files')
        checksum = hashlib.sha256()
        with path.open('rb') as stream:
            for chunk in iter(lambda: stream.read(65536), b''): checksum.update(chunk)
        if checksum.hexdigest() != row['sha256']: fail('materialized_file_hash')
        actual[folded] = relative
    if set(actual) != set(declared): fail('materialized_files')
    reports = receipt['reports']
    if not isinstance(reports, list) or len(reports) != receipt['source_count']: fail('materialized_reports')
    report_dirs = set(); member_ids = set(); original_names = set()
    status_keys = {'source_pdf', 'original_filename', 'mineru_state', 'chart_source_only', 'source_markdown', 'images',
                   'chart_source_image_count', 'original_source_bytes_proven', 'original_pdf_sha256', 'canonical_task_admission', 'legacy_result'}
    provenance_keys = {'run_id', 'job_id', 'batch_id', 'data_id', 'credential_slot', 'zip_sha256', 'source_markdown_sha256',
                       'inspection_receipt_sha256', 'provider_response_sha256'}
    for index, report in enumerate(reports, 1):
        if (not isinstance(report, dict) or set(report) != status_keys or report['mineru_state'] != 'done'
                or report['chart_source_only'] is not True or report['source_markdown'] != 'source_mineru.md'
                or report['original_source_bytes_proven'] is not False or report['canonical_task_admission'] is not False
                or report['original_pdf_sha256'] is not None): fail('materialized_reports')
        name = basename(report['source_pdf']); original = basename(report['original_filename'])
        if name != copied_name(original, index) or original in original_names: fail('materialized_membership')
        original_names.add(original)
        dirname = output_name(name)
        if dirname in report_dirs: fail('materialized_membership')
        report_dirs.add(dirname)
        directory = root / dirname
        if decode((directory / 'status.json').read_bytes()) != report: fail('materialized_status')
        legacy = report['legacy_result']
        if (not isinstance(legacy, dict) or set(legacy) != provenance_keys
                or legacy['run_id'] != context['run_id'] or legacy['job_id'] != context['job_id']
                or legacy['batch_id'] != receipt['selected_batch_id'] or legacy['credential_slot'] != receipt['selected_credential_slot']
                or legacy['data_id'] != data_id(name) or legacy['data_id'] in member_ids
                or legacy['inspection_receipt_sha256'] != context['inspection_receipt_sha256']
                or legacy['provider_response_sha256'] != receipt['selected_response_sha256']
                or any(not isinstance(legacy[k], str) or not SHA.fullmatch(legacy[k]) for k in ('zip_sha256', 'source_markdown_sha256'))):
            fail('materialized_provenance')
        member_ids.add(legacy['data_id'])
        markdown = (directory / 'source_mineru.md').read_bytes()
        if (not 1 <= len(markdown) <= MAX_MARKDOWN or digest(markdown) != legacy['source_markdown_sha256']):
            fail('materialized_markdown')
        try:
            if not markdown.decode('utf-8').strip(): fail('materialized_markdown')
        except UnicodeError: fail('materialized_markdown')
        raw_markdowns = list((directory / 'mineru_raw').rglob('*.md'))
        full = [p for p in raw_markdowns if p.name == 'full.md']
        selected = full if full else raw_markdowns
        if len(selected) != 1 or selected[0].read_bytes() != markdown: fail('materialized_markdown')
        images = report['images']
        if (not isinstance(images, list) or len(images) > 100 or type(report['chart_source_image_count']) is not int
                or report['chart_source_image_count'] != len(images) or len(set(images)) != len(images)):
            fail('materialized_image_map')
        for ordinal, image in enumerate(images, 1):
            if (not isinstance(image, str) or not re.fullmatch(r'assets/source_image_' + f'{ordinal:02d}' + r'\.(?:png|jpe?g|webp|gif|bmp|tiff?)', image)
                    or not (directory / image).is_file()): fail('materialized_image_map')
        mapping = decode((directory / 'source_image_map.json').read_bytes())
        if (set(mapping) != {'version', 'source_sha256', 'images'} or type(mapping['version']) is not int or mapping['version'] != 1
                or mapping['source_sha256'] != digest(markdown) or not isinstance(mapping['images'], dict)
                or any(not isinstance(ref, str) or not ref or value not in images for ref, value in mapping['images'].items())
                or set(mapping['images'].values()) != set(images)):
            fail('materialized_image_map')
    if any(PurePosixPath(row['path']).parts[0] not in report_dirs for row in rows): fail('materialized_membership')
    return {'status': 'legacy-source-only-verified', 'source_count': len(reports),
            'legacy_output_receipt_sha256': digest(receipt_bytes), 'original_source_bytes_proven': False,
            'original_pdf_sha256': None, 'canonical_task_admission': False, 'provider_posts': 0,
            'provider_gets': 0, 'paid_requests': 0, 'new_submissions': 0}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('receipt', 'objects-root', 'original-log', 'original-manifest', 'context', 'output'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
            or os.environ.get('GITHUB_REPOSITORY') != 'yt-feng/rpt_edit'
            or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'
            or os.environ.get('GITHUB_WORKFLOW_REF') != 'yt-feng/rpt_edit/.github/workflows/mineru-legacy-consume.yml@refs/heads/main'):
        print(json.dumps({'status': 'legacy-consumption-rejected', 'provider_posts': 0,
                          'paid_requests': 0, 'new_submissions': 0}))
        return 2
    try:
        def load_object(relative):
            path = args.objects_root / relative
            if path.is_symlink() or not path.resolve().is_relative_to(args.objects_root.resolve()):
                fail('inspection_object_path')
            return path.read_bytes()
        plan = prepare(args.receipt.read_bytes(), load_object, args.original_log.read_bytes(),
                       args.original_manifest.read_bytes(), decode(args.context.read_bytes()))
        public = materialize(plan, args.output)
    except NetworkStop as error:
        print(json.dumps({'status': 'legacy-consumption-stopped', 'network_stop': True,
                          'category': str(error) if str(error) == 'tls_certificate_expired' else 'network_stop',
                          'provider_posts': 0, 'paid_requests': 0, 'new_submissions': 0}))
        return 75
    except ResultHTTPError as error:
        print(json.dumps({'status': 'legacy-consumption-rejected', 'category': 'result_http',
                          'http_status': error.http_status, 'provider_posts': 0, 'paid_requests': 0, 'new_submissions': 0}))
        return 2
    except Exception:
        print(json.dumps({'status': 'legacy-consumption-rejected', 'provider_posts': 0,
                          'paid_requests': 0, 'new_submissions': 0}))
        return 2
    print(json.dumps(public, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
