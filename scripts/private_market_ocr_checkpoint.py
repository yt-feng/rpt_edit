#!/usr/bin/env python3
"""Best-effort private persistence for source-bound Market Views OCR/LLM memo."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import tempfile

from private_workflow_handoff import download_directory, upload_directory, require_env
from recover_durable_mineru_sources import manifest_bindings


def checkpoint_key(manifest: Path, date_folder: str, expected_reports: int) -> str:
    bindings = manifest_bindings(manifest.read_bytes(), expected_reports, date_folder)
    # Ignore checkout/run-local paths and row ordering, but pin every original
    # filename, content hash and Dropbox location. Per-row cache keys additionally
    # pin OCR settings and the full model/prompt/base-URL identity.
    bindings.sort(key=lambda row: row['source_pdf'])
    encoded = json.dumps(bindings, sort_keys=True, separators=(',', ':'), ensure_ascii=False).encode()
    identity = hashlib.sha256(encoded).hexdigest()
    return f'_workflow-cache/market-ocr-synthesis/v1/{date_folder}/{identity}.tar.gz'


def runtime_client():
    import boto3
    from botocore.config import Config
    return boto3.client('s3',
        endpoint_url=f"https://{require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env('R2_ACCESS_KEY_ID'),
        aws_secret_access_key=require_env('R2_SECRET_ACCESS_KEY'), region_name='auto',
        config=Config(connect_timeout=10, read_timeout=20,
                      retries={'total_max_attempts': 1, 'mode': 'standard'}))


def notice(operation: str, error: Exception) -> None:
    # Never echo provider contents, bucket/account identifiers or signed URLs.
    print(f'::notice::Private OCR cache {operation} unavailable ({type(error).__name__}); document processing continues.')


def restore(directory: Path, key: str, *, client=None, bucket=None) -> bool:
    directory.parent.mkdir(parents=True, exist_ok=True)
    # Verify/extract off to the side: a missing, interrupted or corrupt download
    # cannot turn a partial cache into trusted prompt results or erase local work.
    try:
        with tempfile.TemporaryDirectory(prefix='market-ocr-cache-', dir=directory.parent) as temp:
            staged = Path(temp) / 'memo'
            download_directory(key, staged, client=client, bucket=bucket)
            if directory.exists() or directory.is_symlink():
                raise ValueError('OCR cache restoration requires a fresh destination')
            staged.rename(directory)
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        if code in {'NoSuchKey', '404', 'NotFound'}:
            print('No previous private OCR checkpoint; starting with an empty cache.')
        else:
            notice('restore', error)
        directory.mkdir(parents=True, exist_ok=True)
        return False
    return True


def save(directory: Path, key: str, *, client=None, bucket=None) -> bool:
    if not directory.is_dir() or not any(directory.rglob('*.json')):
        print('No OCR/model checkpoint rows to save.')
        return False
    try:
        # Includes *.pending.json: an ambiguous paid request must survive reruns
        # and remain blocked by the synthesis consumer until explicitly resolved.
        upload_directory(directory, key, client=client, bucket=bucket)
    except Exception as error:
        notice('save', error)
        return False
    return True


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('restore', 'save'))
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-reports', type=int, required=True)
    parser.add_argument('--directory', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        key = checkpoint_key(args.manifest, args.date_folder, args.expected_reports)
        client, bucket = runtime_client(), require_env('R2_BUCKET')
        (restore if args.command == 'restore' else save)(args.directory, key, client=client, bucket=bucket)
    except Exception as error:
        # The synthesis step independently validates the complete frozen source
        # inventory. This cache never controls document success or source trust.
        notice(args.command, error)
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
