#!/usr/bin/env python3
"""Replay frozen originals without provider calls; verify an isolated private object."""
import argparse
import json
import os
from pathlib import Path
import re

from market_views_source_preview import prepare, render, verify_pdf, digest
from prepare_public_market_view_pdf import prepare_public_copy
from upload_market_view_to_r2 import (
    build_r2_client, private_publication_complete, validate_existing_pdf_object,
)


from daily_market_source_status import verify_frozen_daily


def accept(originals, output, date, source_run, source_sha, run_id, attempt, *, client, bucket):
    if not re.fullmatch('[1-9][0-9]*', str(run_id)) or not re.fullmatch('[1-9][0-9]*', str(attempt)):
        raise ValueError('Acceptance run identity is invalid')
    output, originals = Path(output), Path(originals)
    output.mkdir(parents=True, exist_ok=True)
    manifest = originals / 'selected_to_process_manifest.json'
    count = len(json.loads(manifest.read_text()))
    item_key = f'_market-views/items/{date}.json'
    if not private_publication_complete(date, client=client, bucket=bucket):
        raise ValueError('Existing production PDF must be verified before isolated acceptance')
    before = client.get_object(Bucket=bucket, Key=item_key)['Body'].read()
    preview = output / 'sources'
    receipt = prepare(originals, manifest, preview, count, date=date, run_id=source_run, sha=source_sha)
    private = output / 'private.pdf'
    render(preview, private, count, date=date, run_id=source_run, sha=source_sha)
    key = f'_private-workflow-handoff/market-preview-acceptance/{run_id}/{attempt}/preview.pdf'
    raw, sha = private.read_bytes(), digest(private)
    client.put_object(Bucket=bucket, Key=key, Body=raw, ContentType='application/pdf',
                      Metadata={'date-key': date, 'sha256': sha})
    verified = validate_existing_pdf_object(client, bucket, key=key,
        head=client.head_object(Bucket=bucket, Key=key), date_key=date, expected_sha256=sha)
    readback = output / 'private-readback.pdf'
    readback.write_bytes(client.get_object(Bucket=bucket, Key=key)['Body'].read())
    if digest(readback) != sha:
        raise ValueError('Acceptance readback bytes changed')
    verify_pdf(readback, receipt['selected_page_count'])
    public = output / f'market_views_{date}.public.pdf'
    prepare_public_copy(readback, public)
    verify_pdf(public, receipt['selected_page_count'])
    if (not private_publication_complete(date, client=client, bucket=bucket)
            or client.get_object(Bucket=bucket, Key=item_key)['Body'].read() != before):
        raise ValueError('Production publication changed during isolated acceptance')
    # Only this exact acceptance object is removed after full successful readback.
    client.delete_object(Bucket=bucket, Key=key)
    result = {'status': 'accepted', 'production_unchanged': True, 'provider_posts': 0,
              'source_run_id': source_run, 'source_sha': source_sha,
              'report_count': count, 'source_pages': receipt['selected_page_count'],
              'private_sha256': sha, 'private_bytes': verified['size_bytes'],
              'public_sha256': digest(public), 'public_bytes': public.stat().st_size,
              'temporary_object_deleted': True}
    (output / 'acceptance.json').write_text(json.dumps(result, indent=2) + '\n')
    return result


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    for name in ('input-dir', 'output-dir', 'date', 'source-run-id', 'source-sha'):
        parser.add_argument('--' + name, required=True)
    args = parser.parse_args()
    result = accept(args.input_dir, args.output_dir, args.date, args.source_run_id, args.source_sha,
                    os.environ['GITHUB_RUN_ID'], os.environ['GITHUB_RUN_ATTEMPT'],
                    client=build_r2_client(), bucket=os.environ['R2_BUCKET'])
    print(json.dumps(result))
