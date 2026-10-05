#!/usr/bin/env python3
"""Authenticate a frozen Daily source and bind every original byte before replay."""
import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import subprocess

from daily_market_source_status import verify_frozen_daily
from extract_native_market_sources import read_manifest, _original_inventory


def verify_origin(run_id, date, repository, *, get=None):
    if (not re.fullmatch(r'[1-9][0-9]*', run_id) or not re.fullmatch(r'(?:[0-9]{6}|[0-9]{8})', date)
            or not re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository)):
        raise ValueError('Invalid frozen Daily replay identity')
    if get is None:
        def get(path):
            return json.loads(subprocess.check_output(['gh', 'api', f'repos/{repository}/{path}'], text=True))
    run = get(f'actions/runs/{run_id}')
    jobs = get(f'actions/runs/{run_id}/jobs?filter=latest&per_page=100')
    return verify_frozen_daily(run, jobs, run_id, repository)


def validate_selection(directory, date, source_root, source_run, source_sha, current_run, current_sha):
    if (not re.fullmatch(r'(?:[0-9]{6}|[0-9]{8})', date)
            or any(not re.fullmatch(r'[1-9][0-9]*', value) for value in (source_run, current_run))
            or any(not re.fullmatch(r'[a-f0-9]{40}', value) for value in (source_sha, current_sha))):
        raise ValueError('Invalid frozen Daily replay context')
    directory = Path(directory)
    manifest_path = directory / 'selected_to_process_manifest.json'
    if manifest_path.is_symlink() or not manifest_path.is_file():
        raise ValueError('Frozen replay manifest must be a regular file')
    rows = json.loads(manifest_path.read_text())
    if not isinstance(rows, list) or not rows:
        raise ValueError('Frozen replay requires a nonempty exact source inventory')
    raw, bindings = read_manifest(manifest_path, len(rows))
    originals = _original_inventory(directory)
    if set(originals) != {binding['source_pdf'] for binding in bindings}:
        raise ValueError('Frozen replay original inventory differs')
    prefix = source_root.rstrip('/').lower() + '/' + date + '/'
    for row, binding in zip(rows, bindings):
        if not str(row.get('dropbox_path', '')).lower().startswith(prefix):
            raise ValueError('Frozen replay date/root differs from original Dropbox source')
        if hashlib.sha256(originals[binding['source_pdf']].read_bytes()).hexdigest() != binding['content_sha256']:
            raise ValueError('Frozen replay original SHA-256 differs')
    receipt = {'schema': 1, 'source_run_id': source_run, 'source_execution_sha': source_sha,
               'replay_run_id': current_run, 'replay_execution_sha': current_sha,
               'date': date, 'report_count': len(rows),
               'original_manifest_sha256': hashlib.sha256(raw).hexdigest(),
               'provider_submission_policy': 'existing-accepted-only'}
    (directory / 'daily_replay_receipt.json').write_text(json.dumps(receipt, sort_keys=True) + '\n')
    return receipt


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('mode', choices=('origin', 'selection'))
    parser.add_argument('--directory', default='_selected_macro_pdfs')
    args = parser.parse_args()
    run_id, date = os.environ['REPLAY_SOURCE_RUN_ID'], os.environ['REPLAY_DATE']
    if args.mode == 'origin':
        sha = verify_origin(run_id, date, os.environ['GITHUB_REPOSITORY'])
        with open(os.environ['GITHUB_ENV'], 'a') as target:
            target.write(f'REPLAY_SOURCE_SHA={sha}\n')
        print('Verified completed main Daily and frozen original upload gate.')
    else:
        value = validate_selection(args.directory, date, os.environ['REPLAY_ROOT'], run_id,
            os.environ['REPLAY_SOURCE_SHA'], os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_SHA'])
        with open(os.environ['GITHUB_OUTPUT'], 'a') as target:
            for name, result in {'latest_folder': date, 'pdf_count': value['report_count'],
                                 'candidate_count': value['report_count'], 'process_count': value['report_count']}.items():
                target.write(f'{name}={result}\n')
        print(json.dumps(value, sort_keys=True))
