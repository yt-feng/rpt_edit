#!/usr/bin/env python3
"""Restore one accepted historical draft batch from R2 without regeneration."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout, redirect_stderr
import io
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

from inspect_recovered_article_generation import (
    SOURCE_RUN_ID, HANDOFF_RUN_ID, DATE_FOLDER, EXPECTED_REPORTS, MANIFEST_SHA256,
)
from inspect_market_views_r2_cache import ReadOnlyClient, build_client
from private_workflow_handoff import download_directory, r2_bucket
from recover_ocr_cache_sources import exact_head
import recovered_article_delivery as delivery
from verify_existing_wechat_drafts import load_drafts

WORKFLOW = '.github/workflows/wechat-draft-image-repair.yml'
ACCEPTED_RUN_ID = '38062937361'
ACCEPTED_DELIVERY_JOB_ID = 114244980478
EXPECTED_DRAFTS = 6


class RestoreError(ValueError):
    pass


def require(condition, category):
    if not condition:
        raise RestoreError(category)


def validate_run(run, records, repository):
    require(str(run.get('id')) == ACCEPTED_RUN_ID
            and run.get('path') == delivery.WORKFLOW
            and run.get('status') == 'completed' and run.get('conclusion') == 'success'
            and run.get('event') == 'workflow_dispatch' and run.get('head_branch') == 'main'
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository
            and run.get('run_attempt') == 1
            and re.fullmatch(r'[a-f0-9]{40}', str(run.get('head_sha', ''))), 'accepted_run_mismatch')
    rows = records.get('jobs', [])
    require(isinstance(rows, list), 'accepted_jobs_invalid')
    for name in ('generate', 'deliver'):
        found = [row for row in rows if row.get('name') == name]
        require(len(found) == 1, 'accepted_job_missing')
        job = found[0]
        require(str(job.get('run_id')) == ACCEPTED_RUN_ID and job.get('head_sha') == run['head_sha']
                and job.get('status') == 'completed' and job.get('conclusion') == 'success', 'accepted_job_mismatch')
        if name == 'deliver':
            require(job.get('id') == ACCEPTED_DELIVERY_JOB_ID, 'accepted_delivery_attempt_changed')
            steps = {step.get('name'): step.get('conclusion') for step in job.get('steps', [])}
            require(all(steps.get(name) == 'success' for name in (
                'Upload drafts and require exact article readback',
                'Save accepted draft receipts even after interruption',
                'Verify full delivery before archiving Blog articles')), 'accepted_receipt_steps_incomplete')


def validate_restored(checkpoint: Path, receipts: Path):
    context = delivery.read_json(checkpoint / 'context.json')
    expected = {'schema_version': 1, 'source_run_id': SOURCE_RUN_ID, 'source_handoff_run_id': HANDOFF_RUN_ID,
                'source_kind': 'ocr-pages', 'date_folder': DATE_FOLDER,
                'expected_articles': EXPECTED_REPORTS, 'manifest_sha256': MANIFEST_SHA256}
    require(all(context.get(k) == v for k, v in expected.items()), 'source_context_mismatch')
    require(re.fullmatch(r'[a-f0-9]{40}', str(context.get('source_execution_sha', '')))
            and re.fullmatch(r'[a-f0-9]{40}', str(context.get('handoff_execution_sha', '')))
            and re.fullmatch(r'[a-f0-9]{64}', str(context.get('source_receipt_sha256', ''))),
            'source_context_hash_invalid')
    require(delivery.read_json(receipts / 'delivery_identity.json') == delivery.delivery_identity(context, checkpoint / 'articles'),
            'delivery_identity_mismatch')
    # Pure validation of all saved source/article bindings and file hashes.
    receipt = delivery.article_receipt(checkpoint.parent, context)
    summary = delivery.read_json(receipts / 'wechat_draft_summary.json')
    require(summary.get('dry_run') is False and summary.get('publish') is False
            and summary.get('status') == 'verified' and summary.get('date_folder') == DATE_FOLDER
            and summary.get('draft_count') == EXPECTED_DRAFTS
            and summary.get('selected_count') == EXPECTED_REPORTS
            and summary.get('input_selected_count') == EXPECTED_REPORTS
            and summary.get('skipped_title_policy_count') == 0
            and summary.get('skipped_generation_failure_count') == 0, 'accepted_summary_mismatch')
    article_rows = summary.get('articles', [])
    require(len(article_rows) == EXPECTED_REPORTS and
            {Path(str(row.get('report_dir', ''))).name for row in article_rows} ==
            {row['directory'] for row in receipt['reports']}, 'accepted_article_inventory_mismatch')
    drafts = load_drafts(receipts)
    require(len(drafts) == EXPECTED_DRAFTS and sum(len(row['articles']) for row in drafts) == EXPECTED_REPORTS,
            'accepted_draft_count_mismatch')
    from push_portal_translated_to_wechat_drafts import draft_group_key
    groups = set()
    for row in summary.get('drafts', []):
        readback = row.get('draft_get', {})
        require(row.get('status') == 'verified' and all(readback.get(key) is True for key in (
            'ok', 'matches_editorial_contract', 'matches_expected_article_count', 'matches_expected_titles')),
            'accepted_readback_incomplete')
        name = Path(str(row.get('payload', ''))).name
        require(re.fullmatch(r'draft_payload_[A-Za-z0-9_-]+\.json', name), 'accepted_payload_name_invalid')
        articles = delivery.read_json(receipts / name).get('articles', [])
        group = draft_group_key(articles)
        require(group == row.get('group_key') and group not in groups
                and len(articles) == readback.get('article_count'), 'accepted_payload_identity_mismatch')
        groups.add(group)
    for path in receipts.glob('draft_payload_*.json'):
        require(draft_group_key(delivery.read_json(path).get('articles', [])) in groups,
                'unaccounted_payload')
    return {'article_count': EXPECTED_REPORTS, 'draft_count': EXPECTED_DRAFTS,
            'context_sha256': delivery.digest(delivery.encode(context)),
            'article_receipt_sha256': delivery.digest((checkpoint / 'articles' / delivery.ARTICLE_RECEIPT).read_bytes())}


def restore(destination: Path, source_run_id: str, repository: str, client, bucket: str):
    require(source_run_id == ACCEPTED_RUN_ID, 'unsupported_recovery_run')
    require(not destination.exists(), 'destination_already_exists')
    run = delivery.api(repository, source_run_id)
    records = delivery.jobs(repository, source_run_id, 1)
    validate_run(run, records, repository)
    prefix = f'_private-workflow-handoff/xhs-recovery/{SOURCE_RUN_ID}/{DATE_FOLDER}/{MANIFEST_SHA256}'
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='accepted-image-receipts-', dir=destination.parent) as temporary:
        workspace = Path(temporary)
        observed = {}
        for filename, root in (('generation.tar.gz', workspace / 'checkpoint'),
                               ('wechat-receipts.tar.gz', workspace / 'receipts')):
            key = prefix + '/' + filename
            head = exact_head(client, bucket, key)
            # Existing verifier pins HEAD, bounds GET and verifies archive hash.
            with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
                download_directory(key, root, client=ReadOnlyClient(client, head), bucket=bucket)
            observed[filename] = head['Metadata']['sha256']
        verified = validate_restored(workspace / 'checkpoint', workspace / 'receipts')
        # Only private receipt/payload files enter the repair source directory;
        # model caches, source text and generation diagnostics remain private.
        output = workspace / 'verified-receipts'
        output.mkdir()
        for path in (workspace / 'receipts').iterdir():
            if path.name in ('wechat_draft_summary.json', 'delivery_identity.json') or re.fullmatch(r'draft_payload_[A-Za-z0-9_-]+\.json', path.name):
                require(path.is_file() and not path.is_symlink(), 'receipt_path_invalid')
                shutil.copyfile(path, output / path.name)
        output.replace(destination)
    return {'schema_version': 1, 'read_only': True, 'source_run_id': ACCEPTED_RUN_ID,
            'source_delivery_job_id': ACCEPTED_DELIVERY_JOB_ID, 'date_folder': DATE_FOLDER,
            'object_writes': 0, 'object_deletions': 0, 'model_calls': 0, 'wechat_writes': 0,
            'archive_sha256': observed, **verified}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--destination', type=Path, required=True)
    parser.add_argument('--report', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        repository = os.environ.get('GITHUB_REPOSITORY', '')
        require(os.environ.get('GITHUB_ACTIONS') == 'true'
                and os.environ.get('GITHUB_EVENT_NAME') == 'workflow_dispatch'
                and os.environ.get('GITHUB_REF') == 'refs/heads/main'
                and os.environ.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main',
                'repair_main_workflow_required')
        result = restore(args.destination, args.source_run_id, repository, build_client(), r2_bucket())
    except Exception as exc:
        result = {'read_only': True, 'success': False,
                  'category': str(exc) if isinstance(exc, RestoreError) else 'receipt_restore_verification_failed',
                  'object_writes': 0, 'model_calls': 0, 'wechat_writes': 0}
        args.report.parent.mkdir(parents=True, exist_ok=True)
        args.report.write_text(json.dumps(result, indent=2))
        print(json.dumps(result))
        return 1
    result['success'] = True
    args.report.parent.mkdir(parents=True, exist_ok=True)
    args.report.write_text(json.dumps(result, indent=2))
    print(json.dumps(result))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
