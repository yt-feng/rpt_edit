#!/usr/bin/env python3
"""Read a claimed Daily delivery checkpoint and expose only aggregate counts."""
from contextlib import redirect_stderr, redirect_stdout
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import re
import tempfile

from private_workflow_handoff import download_directory, r2_bucket
from inspect_market_views_r2_cache import ReadOnlyClient, build_client
from recover_ocr_cache_sources import exact_head
from recovered_article_delivery import DAILY, api

WORKFLOW = '.github/workflows/recovered-wechat-delivery-inspect.yml'
ACCOUNTS = ('kc', 'tt', 'pankou')


def require(condition):
    if not condition:
        raise ValueError('invalid_delivery_inspection')


def summarize(summary, date_folder):
    require(isinstance(summary, dict) and summary.get('date_folder') == date_folder
            and summary.get('dry_run') is False)
    drafts = summary.get('drafts')
    require(isinstance(drafts, list) and len(drafts) <= 1000)
    accepted = dict.fromkeys(ACCOUNTS, 0)
    verified = dict.fromkeys(ACCOUNTS, 0)
    groups = {account: [] for account in ACCOUNTS}
    seen = set()
    pending = 0
    for draft in drafts:
        require(isinstance(draft, dict))
        account, count = draft.get('account'), draft.get('article_count')
        require(account in ACCOUNTS and type(count) is int and 1 <= count <= 9)
        media = draft.get('media_id')
        require(isinstance(media, str) and media and (account, media) not in seen)
        seen.add((account, media))
        accepted[account] += count
        receipt = draft.get('draft_get')
        if (draft.get('status') == 'verified' and isinstance(receipt, dict)
                and receipt.get('ok') is True and receipt.get('article_count') == count):
            verified[account] += count
            groups[account].append(count)
        else:
            pending += 1
    return {'accepted_articles_by_account': accepted,
            'verified_articles_by_account': verified,
            'verified_drafts_by_account': {account: len(values) for account, values in groups.items()},
            'draft_article_counts_by_account': groups,
            'pending_readback_drafts': pending}


def inspect(client, bucket, run, repository, run_id, date_folder, manifest_sha, workspace):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id)
            and re.fullmatch(r'[0-9]{6}', date_folder)
            and re.fullmatch(r'[a-f0-9]{64}', manifest_sha))
    datetime.strptime(date_folder, '%y%m%d')
    require(str(run.get('id')) == run_id and run.get('path') == DAILY
            and run.get('head_branch') == 'main'
            and run.get('event') in {'schedule', 'workflow_dispatch'}
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository)
    identity = {'source_run_id': run_id, 'date_folder': date_folder, 'manifest_sha256': manifest_sha}
    claim_key = f'_private-workflow-handoff/xhs-recovery-claims/{date_folder}/{manifest_sha}.json'
    response = client.get_object(Bucket=bucket, Key=claim_key)
    body = response['Body']
    try:
        raw = body.read(4097)
    finally:
        body.close()
    require(len(raw) <= 4096 and json.loads(raw) == identity)
    key = f'_private-workflow-handoff/xhs-recovery/{run_id}/{date_folder}/{manifest_sha}/wechat-receipts.tar.gz'
    head = exact_head(client, bucket, key)
    restored = workspace / 'receipts'
    download_directory(key, restored, client=ReadOnlyClient(client, head), bucket=bucket)
    summary_path = restored / 'wechat_draft_summary.json'
    require(summary_path.is_file() and summary_path.stat().st_size <= 16 * 1024 * 1024)
    result = summarize(json.loads(summary_path.read_bytes()), date_folder)
    modified = head.get('LastModified')
    return {'status': 'checkpoint_read', 'source_run_id': run_id, 'date_folder': date_folder,
            'checkpoint_bytes': head['ContentLength'],
            'checkpoint_updated_at': modified.astimezone(timezone.utc).isoformat() if isinstance(modified, datetime) else None,
            **result}


def main():
    try:
        repository = os.environ.get('GITHUB_REPOSITORY', '')
        require(os.environ.get('GITHUB_ACTIONS') == 'true'
                and os.environ.get('GITHUB_REF') == 'refs/heads/main'
                and os.environ.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main')
        run_id = os.environ.get('SOURCE_RUN_ID', '')
        require(re.fullmatch(r'[1-9][0-9]{0,19}', run_id))
        with tempfile.TemporaryDirectory() as temporary, redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = inspect(build_client(), r2_bucket(), api(repository, run_id), repository, run_id,
                             os.environ.get('DATE_FOLDER', ''), os.environ.get('MANIFEST_SHA256', ''), Path(temporary))
        print(json.dumps(result, sort_keys=True))
        return 0
    except Exception:
        print(json.dumps({'status': 'inspection_incomplete', 'category': 'delivery_checkpoint_not_verified'}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
