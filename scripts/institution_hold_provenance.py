"""Read small, authenticated producer manifests for exact held-source versions.

This metadata can suppress unchanged feed discovery, never prove PDF bytes or
permit a provider submission. Missing or ambiguous publications yield no row.
"""
from __future__ import annotations

from collections import defaultdict
from datetime import datetime
from email.utils import parsedate_to_datetime
import hashlib
import io
import json
import os
from pathlib import PurePosixPath
import re
import selectors
import subprocess
import time
from urllib.parse import urlsplit
import zipfile

from institution_original_cache import validate_binding

REPOSITORY = 'yt-feng/rpt_edit'
REPOSITORY_ID = 1225092405
PRODUCER = '.github/workflows/institution-latest-pdf-to-wechat.yml'
MANIFEST = '_institution_latest_pdfs/institution_run_manifest.json'
DOMAINS = {'imf.org', 'worldbank.org', 'bis.org', 'oecd.org', 'adb.org',
           'weforum.org', 'unctad.org', 'wto.org', 'bruegel.org'}
MAX_METADATA = 1024 * 1024
MAX_ARCHIVE = 8 * 1024 * 1024
MAX_MANIFEST = 1024 * 1024
MAX_TOTAL_ARCHIVES = 32 * 1024 * 1024
MAX_SECONDS = 30
HASH = re.compile(r'[a-f0-9]{64}')


def require(condition, code):
    if not condition:
        raise ValueError('Institution provenance '+code)


def positive(value):
    return type(value) is int and value > 0


def bounded_command(command, maximum, deadline):
    """Stream capped bytes and reap a timed out or oversized CLI process."""
    require(deadline > time.monotonic(), 'deadline')
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
    chunks, size = [], 0
    try:
        with selectors.DefaultSelector() as selector:
            selector.register(process.stdout, selectors.EVENT_READ)
            while True:
                remaining = deadline - time.monotonic()
                require(remaining > 0 and selector.select(remaining), 'deadline')
                part = os.read(process.stdout.fileno(), min(65536, maximum-size+1))
                if not part:
                    break
                size += len(part)
                require(size <= maximum, 'response size')
                chunks.append(part)
        require(process.wait(timeout=max(0.001, deadline-time.monotonic())) == 0, 'API read failed')
        return b''.join(chunks)
    finally:
        if process.poll() is None:
            process.kill()
        process.wait()
        process.stdout.close()


class GitHubAPI:
    def __init__(self):
        self.deadline = time.monotonic()+MAX_SECONDS

    def get(self, suffix, binary=False):
        raw = bounded_command(['gh', 'api', '--hostname', 'github.com',
                               f'repos/{REPOSITORY}/{suffix}'],
                              MAX_ARCHIVE if binary else MAX_METADATA, self.deadline)
        return raw if binary else json.loads(raw)


def validate_run(run, run_id):
    require(isinstance(run, dict) and positive(run.get('id')) and run['id'] == run_id
            and positive(run.get('run_attempt')) and run.get('path') == PRODUCER
            and run.get('head_branch') == 'main' and run.get('event') in {'schedule', 'workflow_dispatch'}
            and run.get('status') == 'completed'
            and run.get('conclusion') in {'success', 'failure', 'cancelled', 'timed_out'}
            and isinstance(run.get('head_sha'), str) and re.fullmatch(r'[a-f0-9]{40}', run['head_sha']),
            'producer run')
    for key in ('repository', 'head_repository'):
        repository = run.get(key)
        require(isinstance(repository, dict) and repository.get('full_name') == REPOSITORY
                and type(repository.get('id')) is int and repository['id'] == REPOSITORY_ID,
                'repository identity')


def validate_artifact(artifact, run):
    require(isinstance(artifact, dict) and positive(artifact.get('id'))
            and artifact.get('expired') is False and positive(artifact.get('size_in_bytes'))
            and artifact['size_in_bytes'] <= MAX_ARCHIVE
            and isinstance(artifact.get('digest'), str)
            and re.fullmatch(r'sha256:[a-f0-9]{64}', artifact['digest'])
            and isinstance(artifact.get('name'), str)
            and re.fullmatch(r'institution-pdf-run-[0-9]{6}-'+str(run['id']), artifact['name']),
            'artifact metadata')
    identity = artifact.get('workflow_run')
    require(isinstance(identity, dict) and type(identity.get('id')) is int and identity['id'] == run['id']
            and type(identity.get('repository_id')) is int and identity['repository_id'] == REPOSITORY_ID
            and type(identity.get('head_repository_id')) is int and identity['head_repository_id'] == REPOSITORY_ID
            and identity.get('head_branch') == 'main' and identity.get('head_sha') == run['head_sha'],
            'artifact producer')


def read_manifest(artifact, run, archive):
    validate_artifact(artifact, run)
    require(isinstance(archive, bytes) and len(archive) == artifact['size_in_bytes']
            and 'sha256:'+hashlib.sha256(archive).hexdigest() == artifact['digest'], 'artifact checksum')
    with zipfile.ZipFile(io.BytesIO(archive)) as zipped:
        entries = zipped.infolist()
        require(1 <= len(entries) <= 100, 'ZIP entries')
        names, total = set(), 0
        for entry in entries:
            path = PurePosixPath(entry.filename)
            require(entry.filename and not path.is_absolute() and '..' not in path.parts
                    and '\\' not in entry.filename and '\x00' not in entry.filename
                    and entry.filename not in names and not entry.flag_bits & 1
                    and entry.compress_type in {zipfile.ZIP_STORED, zipfile.ZIP_DEFLATED}
                    and entry.external_attr >> 16 & 0o170000 in {0, 0o100000, 0o040000}, 'ZIP path')
            total += entry.file_size
            require(total <= MAX_ARCHIVE, 'ZIP expanded size')
            names.add(entry.filename)
        require(MANIFEST in names, 'manifest missing')
        entry = zipped.getinfo(MANIFEST)
        require(not entry.is_dir() and 0 < entry.file_size <= MAX_MANIFEST, 'manifest size')
        with zipped.open(entry) as stream:
            raw = stream.read(MAX_MANIFEST+1)
        require(len(raw) == entry.file_size, 'manifest length')
    manifest = json.loads(raw)
    require(isinstance(manifest, dict) and isinstance(manifest.get('date'), str)
            and artifact['name'] == f"institution-pdf-run-{manifest['date']}-{run['id']}"
            and isinstance(manifest.get('downloaded'), list) and len(manifest['downloaded']) <= 1000
            and type(manifest.get('downloaded_count')) is int
            and manifest['downloaded_count'] == len(manifest['downloaded'])
            and all(isinstance(row, dict) for row in manifest['downloaded']), 'manifest contract')
    receipt = {'run_id': run['id'], 'artifact_id': artifact['id'],
               'artifact_sha256': artifact['digest'][7:], 'manifest_sha256': hashlib.sha256(raw).hexdigest()}
    return manifest['downloaded'], receipt


def official_url(value, *, page=False):
    if not isinstance(value, str) or not 1 <= len(value) <= 4096 or any(ord(c) < 32 for c in value):
        return False
    try:
        parts = urlsplit(value)
        host = parts.hostname or ''
        return (parts.scheme in ({'http', 'https'} if page else {'https'})
                and not parts.username and not parts.password
                and parts.port in ({None, 80, 443} if page else {None, 443}) and not parts.fragment
                and any(host == domain or host.endswith('.'+domain) for domain in DOMAINS))
    except ValueError:
        return False


def normalized_row(row):
    name, size, published = row.get('local_filename'), row.get('bytes'), row.get('published')
    if (not isinstance(name, str) or not 1 <= len(name) <= 512 or '/' in name or '\\' in name
            or not name.endswith('.pdf') or not positive(size)
            or not official_url(row.get('source_page_url'), page=True) or not official_url(row.get('pdf_url'))
            or not isinstance(published, str) or not 1 <= len(published) <= 64):
        return None
    try:
        try:
            stamp = datetime.fromisoformat(published.replace('Z', '+00:00'))
        except ValueError:
            stamp = parsedate_to_datetime(published)
        if stamp.tzinfo is None:
            return None
    except (ValueError, TypeError):
        return None
    result = {key: row[key] for key in ('local_filename', 'bytes', 'source_page_url', 'published', 'pdf_url')}
    if 'sha256' in row:
        if not isinstance(row['sha256'], str) or not HASH.fullmatch(row['sha256']):
            return None
        result['sha256'] = row['sha256']
    if 'feed_pdf_candidates' in row:
        candidates = row['feed_pdf_candidates']
        if not isinstance(candidates, list) or len(candidates) > 20 or not all(official_url(url) for url in candidates):
            return None
        result['feed_pdf_candidates'] = candidates
    return result


def match_versions(downloaded, bindings):
    """Do not infer content hashes or collapse competing legacy identities."""
    by_pair, sources = defaultdict(list), defaultdict(dict)
    for row in downloaded:
        name, size = row.get('local_filename'), row.get('bytes')
        if isinstance(name, str) and type(size) is int:
            by_pair[(name, size)].append(row)
    for binding in bindings:
        validate_binding(binding)
        sources[(binding['source'], binding['size'])][binding['id']] = binding
    result = []
    for pair, identities in sources.items():
        rows = by_pair.get(pair, [])
        if len(identities) != 1 or not rows:
            continue
        binding = next(iter(identities.values()))
        normalized = [normalized_row(row) for row in rows]
        if any(row is None or row.get('sha256', binding['sha256']) != binding['sha256'] for row in normalized):
            continue
        # Optional fields are evidence, too: disagreement permits fetching.
        unique = {json.dumps(row, sort_keys=True, separators=(',', ':')) for row in normalized}
        if len(unique) != 1:
            continue
        result.append(dict(normalized[0], binding_id=binding['id']))
    return sorted(result, key=lambda row: row['binding_id'])


def get_original_versions(run_ids, bindings, *, api=None):
    """Return (archive-like rows, receipts) after authenticating every source run."""
    require(isinstance(run_ids, list) and 1 <= len(run_ids) <= 6
            and all(isinstance(value, (str, int)) and not isinstance(value, bool)
                    and re.fullmatch(r'[1-9][0-9]{0,19}', str(value)) for value in run_ids)
            and len({str(value) for value in run_ids}) == len(run_ids), 'run IDs')
    require(isinstance(bindings, list) and len(bindings) <= 200, 'bindings limit')
    for binding in bindings:
        validate_binding(binding)
    api = api or GitHubAPI()
    downloaded, receipts, total = [], [], 0
    for value in run_ids:
        run_id = int(value)
        run = api.get(f'actions/runs/{run_id}')
        validate_run(run, run_id)
        listing = api.get(f'actions/runs/{run_id}/artifacts?per_page=100')
        require(isinstance(listing, dict) and type(listing.get('total_count')) is int
                and isinstance(listing.get('artifacts'), list)
                and 0 <= listing['total_count'] == len(listing['artifacts']) <= 100, 'artifact listing')
        candidates = [row for row in listing['artifacts'] if isinstance(row, dict)
                      and isinstance(row.get('name'), str) and row['name'].startswith('institution-pdf-run-')]
        require(len(candidates) <= 1, 'ambiguous artifact')
        if not candidates or candidates[0].get('expired') is True:
            continue
        artifact = candidates[0]
        validate_artifact(artifact, run)
        total += artifact['size_in_bytes']
        require(total <= MAX_TOTAL_ARCHIVES, 'total archive size')
        archive = api.get(f"actions/artifacts/{artifact['id']}/zip", binary=True)
        rows, receipt = read_manifest(artifact, run, archive)
        downloaded.extend(rows)
        receipts.append(receipt)
    return match_versions(downloaded, bindings), receipts
