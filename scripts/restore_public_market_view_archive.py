#!/usr/bin/env python3
"""Restore a sanitized public archive from an exact already published private PDF."""
import argparse
import hashlib
import json
from pathlib import Path
import re
import tempfile

from prepare_public_market_view_pdf import prepare_public_copy
from upload_market_view_to_r2 import build_r2_client, parse_issue_date, validate_existing_private_pair


def restore(client, bucket, day, expected_sha, output):
    issue_date, normalized = parse_issue_date(day)
    if normalized != day or not re.fullmatch(r'[a-f0-9]{64}', expected_sha):
        raise ValueError('exact_archive_date_and_hash_required')
    pdf_key, item_key = f'_market-views/pdfs/{day}.pdf', f'_market-views/items/{day}.json'
    item = validate_existing_private_pair(client, bucket, pdf_key=pdf_key, item_key=item_key,
        pdf_head=client.head_object(Bucket=bucket, Key=pdf_key),
        item_head=client.head_object(Bucket=bucket, Key=item_key),
        issue_date=issue_date, date_key=day, filename=f'market_views_{day}.pdf')
    if item['sha256'] != expected_sha or not 1024 < item['size_bytes'] <= 100 * 1024 * 1024:
        raise ValueError('published_private_pdf_identity_differs')
    body = client.get_object(Bucket=bucket, Key=pdf_key)['Body']
    try:
        raw = body.read(item['size_bytes'] + 1)
    finally:
        body.close()
    if len(raw) != item['size_bytes'] or hashlib.sha256(raw).hexdigest() != expected_sha:
        raise ValueError('published_private_pdf_changed_during_read')
    with tempfile.TemporaryDirectory(prefix='market-archive-source-') as directory:
        source = Path(directory) / 'private.pdf'
        source.write_bytes(raw)
        result = prepare_public_copy(source, output)
    return {'date_folder': day, 'private_pdf_sha256': expected_sha,
            'public_pdf_sha256': hashlib.sha256(Path(output).read_bytes()).hexdigest(),
            'provider_posts': 0, 'model_calls': 0, 'private_object_writes': 0, **result}


def main():
    import os
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--date', required=True)
    parser.add_argument('--expected-private-sha256', required=True)
    args = parser.parse_args()
    if (os.environ.get('GITHUB_ACTIONS') != 'true' or os.environ.get('GITHUB_REF') != 'refs/heads/main'
            or os.environ.get('GITHUB_EVENT_NAME') != 'workflow_dispatch'):
        raise ValueError('archive_recovery_requires_manual_main')
    path = Path('market_view_summaries') / args.date / f'market_views_{args.date}.pdf'
    result = restore(build_r2_client(), os.environ['R2_BUCKET'], args.date, args.expected_private_sha256, path)
    print(json.dumps(result, sort_keys=True))


if __name__ == '__main__':
    main()
