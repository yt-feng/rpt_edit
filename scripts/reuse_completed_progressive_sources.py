#!/usr/bin/env python3
"""Reuse complete current-run source proofs without generating or uploading drafts."""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout, redirect_stderr
import io
import os
from pathlib import Path
import re
import shutil
import tempfile
import time

import progressive_wechat_delivery as progressive
from market_views_partial_sources import read_selection
from private_workflow_handoff import build_r2_client, r2_bucket, download_directory, upload_directory
from recovered_article_delivery import api, jobs, DAILY, DeliveryError
from report_extraction_source import resolve_extraction_source
from wechat_editorial_binding import read_bound_article

RECEIPT = 'completed_primary_source_receipt.json'
PROOF = '_completed_primary_proof'
PUBLISHER = 'push-xhs-notes-wechat-drafts'
STEPS = ('Initialize progressive WeChat delivery plan', 'Verify complete current WeChat delivery')


class ReuseError(ValueError):
    pass


def require(condition, category):
    if not condition:
        raise ReuseError(category)


def primary_identity(source_run_id, env):
    """Retry only classified transient reads, restarting the complete identity check."""
    transient = {'delivery_jobs_changed', 'delivery_jobs_incomplete', 'delivery_github_metadata_failed'}
    for attempt in range(3):
        try:
            return _primary_identity_once(source_run_id, env)
        except DeliveryError as error:
            if str(error) not in transient or attempt == 2:
                raise
            time.sleep((1, 3)[attempt])


def _primary_identity_once(source_run_id, env):
    repository = env.get('GITHUB_REPOSITORY', '')
    sha = env.get('GITHUB_SHA', '')
    attempt = env.get('GITHUB_RUN_ATTEMPT', '')
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
            and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{DAILY}@refs/heads/main'
            and str(source_run_id) == env.get('GITHUB_RUN_ID')
            and re.fullmatch(r'[1-9][0-9]{0,19}', str(source_run_id))
            and re.fullmatch(r'[a-f0-9]{40}', sha)
            and re.fullmatch(r'[1-9]|10', attempt), 'reuse_current_daily_identity_invalid')
    run = api(repository, str(source_run_id))
    require(str(run.get('id')) == str(source_run_id) and run.get('head_sha') == sha
            and run.get('run_attempt') == int(attempt) and run.get('path') == DAILY
            and run.get('head_branch') == 'main' and run.get('event') in {'schedule', 'workflow_dispatch'}
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository
            and run.get('status') == 'in_progress' and run.get('conclusion') is None, 'reuse_original_daily_changed')
    inventory = jobs(repository, str(source_run_id), int(attempt))
    records = inventory.get('jobs', [])
    require(records and inventory.get('total_count') == len(records)
            and len({row.get('id') for row in records}) == len(records)
            and all(str(row.get('run_id')) == str(source_run_id) and row.get('head_sha') == sha for row in records),
            'reuse_job_inventory_invalid')
    selected = [row for row in records if row.get('name') == 'select-macro-reports']
    require(len(selected) == 1 and selected[0].get('status') == 'completed'
            and selected[0].get('conclusion') == 'success', 'reuse_selection_not_complete')
    publishers = [row for row in records if row.get('name') == PUBLISHER]
    require(len(publishers) == 1 and publishers[0].get('status') == 'completed', 'reuse_primary_not_terminal')
    publisher = publishers[0]
    if publisher.get('conclusion') in {'failure', 'cancelled', 'skipped', 'timed_out'}:
        return None
    require(publisher.get('conclusion') == 'success', 'reuse_primary_conclusion_invalid')
    for name in STEPS:
        matches = [row for row in publisher.get('steps', []) if row.get('name') == name]
        require(len(matches) == 1 and matches[0].get('status') == 'completed'
                and matches[0].get('conclusion') == 'success', 'reuse_progressive_completion_unproven')
    require(type(publisher.get('id')) is int and publisher['id'] > 0, 'reuse_publisher_identity_invalid')
    return {'source_run_id': str(source_run_id), 'source_execution_sha': sha,
            'source_run_attempt': int(attempt), 'publisher_job_id': publisher['id']}


def validate_manifest_plan(manifest, plan, expected_articles):
    raw, rows = read_selection(Path(manifest))
    progressive.validate_plan(plan)
    require(type(expected_articles) is int and 1 <= expected_articles <= 1000
            and len(rows) == len(plan['sources']) == expected_articles
            and progressive.digest(raw) == plan.get('manifest_sha256'), 'reuse_manifest_inventory_mismatch')
    width = plan.get('reports_per_shard')
    require(type(width) is int and width > 0, 'reuse_plan_shard_width_invalid')
    for index, (row, source) in enumerate(zip(rows, plan['sources'])):
        staged = progressive.unique_batch_name(Path(row['process_local_path']), index % width + 1)
        require(source.get('source_pdf') == row['source_pdf'] and source.get('content_sha256') == row['content_sha256']
                and source.get('staged_name') == staged
                and source.get('report_relative') == f'shard_{index // width}/{progressive.slug(staged)}',
                'reuse_manifest_source_mismatch')
    return raw


def inventory(directory):
    require(directory.is_dir() and not directory.is_symlink(), 'reuse_source_directory_invalid')
    result = {}
    for path in sorted(directory.rglob('*')):
        require(not path.is_symlink(), 'reuse_source_symlink')
        if path.is_file():
            result[path.relative_to(directory).as_posix()] = progressive.digest(path.read_bytes())
    return result


def validate_complete_handoff(root, source_run_id, date_folder, manifest_sha256, expected_articles, source_sha=None):
    """Verify a downloaded single-shard export, including original complete proofs."""
    root = Path(root)
    receipt = progressive.read_json(root / RECEIPT)
    require(isinstance(receipt, dict) and receipt.get('schema_version') == 1
            and receipt.get('source_run_id') == str(source_run_id) and receipt.get('date_folder') == date_folder
            and receipt.get('manifest_sha256') == manifest_sha256
            and receipt.get('article_count') == expected_articles
            and re.fullmatch(r'[a-f0-9]{40}', str(receipt.get('source_execution_sha', '')))
            and (source_sha is None or receipt['source_execution_sha'] == source_sha)
            and type(receipt.get('source_run_attempt')) is int and 1 <= receipt['source_run_attempt'] <= 10
            and type(receipt.get('publisher_job_id')) is int and receipt['publisher_job_id'] > 0,
            'reuse_handoff_identity_invalid')
    require(receipt.get('receipt_sha256') == progressive.digest(progressive.encoded(
        {key: value for key, value in receipt.items() if key != 'receipt_sha256'})), 'reuse_handoff_digest_invalid')
    proof = root / PROOF
    require(inventory(proof) == receipt.get('proof_files'), 'reuse_handoff_proof_changed')
    plan = progressive.read_json(proof / 'progressive_plan.json')
    validate_manifest_plan(proof / 'selected_to_process_manifest.json', plan, expected_articles)
    require(all(plan.get(key) == receipt.get(key) for key in ('source_run_id', 'source_execution_sha', 'date_folder', 'manifest_sha256', 'plan_sha256')),
            'reuse_handoff_plan_changed')
    complete = progressive.read_json(proof / 'complete.json')
    require(complete == {'plan_sha256': plan['plan_sha256'], 'complete': True}, 'reuse_handoff_completion_missing')
    records = receipt.get('sources')
    require(isinstance(records, list) and len(records) == expected_articles, 'reuse_handoff_sources_missing')
    directories = {}
    for index, (source, record) in enumerate(zip(plan['sources'], records)):
        name = f"report_{index:04d}_{source['source_id'][:16]}"
        require(record.get('directory') == name and record.get('source_id') == source['source_id'], 'reuse_handoff_source_order_changed')
        directory = root / name
        require(inventory(directory) == record.get('files'), 'reuse_handoff_source_changed')
        status = progressive.read_json(directory / 'status.json')
        require(not status.get('error') and status.get('original_pdf_sha256') == source['content_sha256']
                and Path(str(status.get('source_pdf', ''))).name in {source['source_pdf'], source['staged_name']}
                and read_bound_article(directory) is not None, 'reuse_handoff_source_binding_invalid')
        extraction = resolve_extraction_source(directory)
        require(extraction.identity() == record.get('extraction'), 'reuse_handoff_extraction_changed')
        provenance = status.get('wechat_source_provenance')
        require(provenance is None or provenance.get('content_sha256') == source['content_sha256'], 'reuse_handoff_provenance_changed')
        directories[source['source_id']] = directory
    require({path.name for path in root.iterdir()} == {PROOF, RECEIPT, *(row['directory'] for row in records)}, 'reuse_handoff_extra_files')
    # Static validation uses the archived first acceptance and exact payloads;
    # it never obtains WeChat credentials or calls any write/readback API.
    with tempfile.TemporaryDirectory(prefix='reuse-static-proof-') as temporary:
        copied = Path(temporary) / 'proof'
        shutil.copytree(proof, copied)
        progressive.validate_progressive_delivery(copied, plan, directories, live=False)
    return receipt


def reuse_sources(source_run_id, date_folder, expected_articles, manifest, workspace, *, env=None, client=None, bucket=None):
    env = os.environ if env is None else env
    owner = primary_identity(source_run_id, env)
    if owner is None:
        return {'reuse': 'false'}
    progressive.progressive_prefix(source_run_id, date_folder)
    client = build_r2_client() if client is None else client
    bucket = r2_bucket() if bucket is None else bucket
    raw, _rows = read_selection(Path(manifest))
    manifest_sha = progressive.digest(raw)
    plan = progressive.load_plan(client, bucket, source_run_id, date_folder, owner['source_execution_sha'], manifest_sha)
    require(plan is not None, 'reuse_progressive_plan_missing')
    validate_manifest_plan(manifest, plan, expected_articles)
    prefix = progressive.progressive_prefix(source_run_id, date_folder)
    complete, _etag = progressive.read_object(client, bucket, prefix + '/complete.json')
    require(complete == {'plan_sha256': plan['plan_sha256'], 'complete': True}, 'reuse_progressive_completion_missing')
    workspace = Path(workspace)
    workspace.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix='completed-primary-', dir=workspace) as temporary:
        root = Path(temporary)
        sources, proof, export = root / 'sources', root / 'proof', root / 'export'
        download_directory(prefix + '/sources.tar.gz', sources, client=client, bucket=bucket)
        download_directory(prefix + '/complete.tar.gz', proof, client=client, bucket=bucket)
        directories = progressive.completed_source_directories(plan, sources, complete)
        progressive.validate_progressive_delivery(proof, plan, directories, live=False)
        export.mkdir()
        shutil.copytree(proof, export / PROOF)
        (export / PROOF / 'selected_to_process_manifest.json').write_bytes(raw)
        progressive.write_json(export / PROOF / 'complete.json', complete)
        records = []
        for index, source in enumerate(plan['sources']):
            name = f"report_{index:04d}_{source['source_id'][:16]}"
            directory = export / name
            shutil.copytree(directories[source['source_id']], directory)
            records.append({'source_id': source['source_id'], 'directory': name, 'files': inventory(directory),
                            'extraction': resolve_extraction_source(directory).identity()})
        receipt = {'schema_version': 1, **owner, 'date_folder': date_folder, 'manifest_sha256': manifest_sha,
                   'plan_sha256': plan['plan_sha256'], 'article_count': expected_articles,
                   'sources': records, 'proof_files': inventory(export / PROOF)}
        receipt['receipt_sha256'] = progressive.digest(progressive.encoded(receipt))
        progressive.write_json(export / RECEIPT, receipt)
        validate_complete_handoff(export, source_run_id, date_folder, manifest_sha, expected_articles, owner['source_execution_sha'])
        require(primary_identity(source_run_id, env) == owner, 'reuse_primary_changed_during_export')
        target = f'_private-workflow-handoff/xhs-complete/{source_run_id}/{date_folder}/{manifest_sha}/articles'
        upload_directory(export, target + '/shard_0.tar.gz', client=client, bucket=bucket)
        verified = root / 'verified'
        download_directory(target + '/shard_0.tar.gz', verified, client=client, bucket=bucket)
        validate_complete_handoff(verified, source_run_id, date_folder, manifest_sha, expected_articles, owner['source_execution_sha'])
    return {'reuse': 'true', 'article_handoff_prefix': target, 'article_count': str(expected_articles), 'manifest_sha256': manifest_sha}


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--expected-articles', type=int, required=True)
    parser.add_argument('--workspace', type=Path, required=True)
    parser.add_argument('--manifest', type=Path, default=Path('_selected_macro_manifest/selected_to_process_manifest.json'))
    parser.add_argument('--output-github', default=os.environ.get('GITHUB_OUTPUT'))
    args = parser.parse_args(argv)
    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            result = reuse_sources(args.source_run_id, args.date_folder, args.expected_articles, args.manifest, args.workspace)
        require(args.output_github, 'reuse_output_path_missing')
        with open(args.output_github, 'a') as output:
            for key, value in result.items():
                output.write(f'{key}={value}\n')
        print('completed_primary_source_reused' if result['reuse'] == 'true' else 'completed_primary_source_not_applicable')
        return 0
    except Exception:
        print('completed_primary_source_reuse_failed')
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
