#!/usr/bin/env python3
"""One-shot cloud-only read of the exact production handoff; export metadata only."""
from __future__ import annotations
import argparse
import gzip
import hashlib
import json
import os
from pathlib import Path, PurePosixPath
import re
import subprocess
import sys
import tarfile
import tempfile
import time

RUN_ID = '38224136456'
DATE = '261012'
KEY = f'_private-workflow-handoff/institutions/{RUN_ID}/{DATE}/translated.tar.gz'
REPOSITORY = 'yt-feng/rpt_edit'
BRANCH = 'codex/imf-reviewed-cache-import-20261012'
WORKFLOW = '.github/workflows/institution-fetch-test.yml'
HELPER_TREE = 'fa269a40dfe9c433b9473c6d6800c1bafe70ee4c'
PRODUCTION_SHA = 'f0d61e25c99366be925771e28287dc0c2e4b9ef6'
HASH = re.compile(r'[a-f0-9]{64}')
MAX_COMPRESSED = 256 * 1024 * 1024
MAX_EXPANDED = 1024 * 1024 * 1024
MAX_MEMBERS = 20000
MAX_METADATA = 2 * 1024 * 1024
REPORT_FIELDS = ('source_report_dir', 'source_method', 'source_markdown', 'source_sha256', 'output_dir', 'pdf_path', 'pdf')
STATUS_FIELDS = ('source_report_dir', 'source_method', 'source_markdown', 'source_sha256', 'pdf')

class ExportError(ValueError):
    pass

def require(condition, code):
    if not condition:
        raise ExportError(code)

def cloud_guard():
    require(os.environ.get('GITHUB_ACTIONS') == 'true'
            and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
            and os.environ.get('GITHUB_REPOSITORY') == REPOSITORY
            and os.environ.get('GITHUB_REF') == 'refs/heads/' + BRANCH
            and os.environ.get('GITHUB_WORKFLOW_REF') == REPOSITORY + '/' + WORKFLOW + '@refs/heads/' + BRANCH,
            'cloud_readonly_workflow_required')

def load_helper(repo):
    repo = Path(repo).resolve()
    tree = subprocess.check_output(['git', '-C', str(repo), 'rev-parse', 'HEAD^{tree}'], text=True).strip()
    clean = subprocess.check_output(['git', '-C', str(repo), 'status', '--porcelain', '--untracked-files=no', '--', 'scripts'], text=True)
    require(tree == HELPER_TREE and not clean, 'helper_revision')
    sys.path.insert(0, str(repo / 'scripts'))
    import private_workflow_handoff as handoff
    require(handoff.validate_key(KEY) == KEY, 'handoff_key')
    return handoff

def canonical_path(value, marker, *, child=False):
    require(isinstance(value, str) and 0 < len(value) < 4096 and '\\' not in value
            and not any(ord(char) < 32 for char in value), 'metadata_path')
    parts = PurePosixPath(value).parts
    require('..' not in parts and parts.count(marker) == 1, 'metadata_path')
    parts = parts[parts.index(marker):]
    require(len(parts) == (5 if child else 4) and parts[1:3] == ('institutions', DATE)
            and all(part not in ('', '.', '..') for part in parts), 'metadata_path')
    return '/'.join(parts)

def sanitize_report(row):
    require(isinstance(row, dict) and all(key in row for key in REPORT_FIELDS), 'report_shape')
    result = {key: row[key] for key in REPORT_FIELDS}
    result['source_report_dir'] = canonical_path(row['source_report_dir'], 'xhs_notes')
    result['output_dir'] = canonical_path(row['output_dir'], 'portal_translated_reports')
    result['pdf_path'] = canonical_path(row['pdf_path'], 'portal_translated_reports', child=True)
    require(result['source_method'] == 'mineru' and result['source_markdown'] == 'source_mineru.md'
            and isinstance(result['source_sha256'], str) and HASH.fullmatch(result['source_sha256']), 'source_identity')
    require(isinstance(result['pdf'], str) and re.fullmatch(r'portal_translated_report_[0-9]{2,4}\.pdf', result['pdf'])
            and result['pdf_path'] == result['output_dir'] + '/' + result['pdf'], 'pdf_identity')
    return result

def bounded_copy(source, destination, limit, deadline):
    total = 0
    digest = hashlib.sha256()
    while True:
        require(time.monotonic() < deadline, 'read_time_bound')
        chunk = source.read(min(1024 * 1024, limit - total + 1))
        if not chunk:
            break
        total += len(chunk)
        require(total <= limit, 'read_size_bound')
        destination.write(chunk)
        digest.update(chunk)
    return total, digest.hexdigest()

def json_member(archive, member):
    require(member.isfile() and 0 < member.size <= MAX_METADATA, 'metadata_size')
    stream = archive.extractfile(member)
    require(stream is not None, 'metadata_missing')
    with stream:
        raw = stream.read(MAX_METADATA + 1)
    require(len(raw) == member.size, 'metadata_size')
    value = json.loads(raw)
    require(isinstance(value, dict), 'metadata_shape')
    return value, hashlib.sha256(raw).hexdigest()

def export_metadata(client, bucket, helper, output):
    output = Path(output)
    require(not output.exists() and not output.is_symlink(), 'output_must_be_new')
    deadline = time.monotonic() + 180
    # Exactly one read of the fixed run key. No listing, retry, upload, delete, or provider call.
    response = client.get_object(Bucket=bucket, Key=KEY)
    body = response['Body']
    try:
        size = response.get('ContentLength')
        metadata = response.get('Metadata', {})
        expected_hash = metadata.get('sha256')
        count = metadata.get('file-count', '')
        require(type(size) is int and 0 < size <= MAX_COMPRESSED and response.get('ContentType') == 'application/gzip', 'object_shape')
        require(isinstance(expected_hash, str) and HASH.fullmatch(expected_hash)
                and isinstance(count, str) and re.fullmatch(r'[1-9][0-9]{0,4}', count)
                and int(count) <= MAX_MEMBERS, 'object_digest_metadata')
        with tempfile.TemporaryDirectory(prefix='imf-readonly-handoff-') as directory:
            temp = Path(directory)
            compressed = temp / 'handoff.tar.gz'
            with compressed.open('wb') as stream:
                actual_size, actual_hash = bounded_copy(body, stream, MAX_COMPRESSED, deadline)
            require(actual_size == size and actual_hash == expected_hash, 'object_digest_mismatch')
            tar_path = temp / 'handoff.tar'
            with gzip.open(compressed, 'rb') as source, tar_path.open('wb') as destination:
                expanded_size, _ = bounded_copy(source, destination, MAX_EXPANDED, deadline)
            with tarfile.open(tar_path, 'r:') as archive:
                members = []
                for member in archive:
                    require(len(members) < MAX_MEMBERS and time.monotonic() < deadline, 'archive_bound')
                    require(member.isfile() and member.size >= 0, 'archive_member_type')
                    members.append(member)
                # Apply the production handoff helper's traversal/link/device checks too.
                safe = helper._safe_members(archive, temp / 'never-extracted')
                require(len(safe) == len(members) == int(count), 'archive_file_count')
                names = [member.name for member in safe]
                require(len(names) == len(set(names)) and all(str(PurePosixPath(name)) == name for name in names), 'archive_duplicate_path')
                inventory = dict(zip(names, safe))
                require('translation_summary.json' in inventory, 'translation_summary_missing')
                summary, summary_hash = json_member(archive, inventory['translation_summary.json'])
                require(summary.get('date_folder') == DATE and summary.get('max_reports') == 'all'
                        and summary.get('failures') == [] and summary.get('sensitive_skipped_count') == 0
                        and isinstance(summary.get('reports'), list) and 0 < len(summary['reports']) <= 100,
                        'translation_summary_incomplete')
                reports = [sanitize_report(row) for row in summary['reports']]
                require(type(summary.get('selected_count')) is int and type(summary.get('successful_count')) is int
                        and summary['selected_count'] == summary['successful_count'] == len(reports), 'translation_counts')
                require(len({row['source_report_dir'] for row in reports}) == len(reports)
                        and len({row['output_dir'] for row in reports}) == len(reports), 'translation_duplicate_identity')
                status_hashes = {}
                for row in reports:
                    slug = PurePosixPath(row['output_dir']).name
                    name = slug + '/translation_status.json'
                    require(name in inventory, 'translation_status_missing')
                    status, status_hash = json_member(archive, inventory[name])
                    status['source_report_dir'] = canonical_path(status.get('source_report_dir'), 'xhs_notes')
                    require(all(status.get(key) == row[key] for key in STATUS_FIELDS), 'translation_status_binding')
                    status_hashes[name] = status_hash
                require(set(status_hashes) == {name for name in names if PurePosixPath(name).name == 'translation_status.json'}, 'translation_status_inventory')
    finally:
        body.close()
    sanitized = {key: summary[key] for key in ('date_folder', 'max_reports', 'selected_count', 'successful_count', 'sensitive_skipped_count')}
    sanitized.update(failures=[], reports=reports, origin_run_id=RUN_ID)
    raw = (json.dumps(sanitized, ensure_ascii=False, indent=2) + '\n').encode()
    receipt = dict(status='metadata_export_verified', production_run_id=RUN_ID, production_sha=PRODUCTION_SHA,
                   date_folder=DATE, handoff_sha256=actual_hash, handoff_bytes=actual_size,
                   handoff_expanded_bytes=expanded_size, handoff_file_count=int(count),
                   source_summary_sha256=summary_hash, exported_summary_sha256=hashlib.sha256(raw).hexdigest(),
                   status_file_sha256=status_hashes, translated_count=len(reports), target_count=17,
                   exact_target_count=len(reports) == 17, storage_gets=1, storage_writes=0,
                   extracted_article_bodies=0, extracted_pdfs=0)
    output.mkdir(mode=0o700)
    (output / 'translation_summary.json').write_bytes(raw)
    (output / 'handoff_metadata_receipt.json').write_text(json.dumps(receipt, indent=2) + '\n')
    return receipt

def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args(argv)
    cloud_guard()
    helper = load_helper(args.repo)
    from persist_legacy_mineru_inspection import single_attempt_store
    store = single_attempt_store()
    return export_metadata(store.client, store.bucket, helper, args.output)

if __name__ == '__main__':
    try:
        receipt = main()
        print(json.dumps({key: receipt[key] for key in ('status', 'production_run_id', 'translated_count', 'exact_target_count', 'storage_gets', 'storage_writes')}))
    except Exception as error:
        code = str(error) if type(error) is ExportError else 'handoff_metadata_read_failed'
        print(json.dumps({'status': 'stopped', 'code': code}), file=sys.stderr)
        raise SystemExit(1) from None
