#!/usr/bin/env python3
"""Deliver authenticated recovered articles with durable, source-bound receipts.

Only GitHub metadata and private handoffs are read here. MinerU is never called.
All public diagnostics are fixed categories and counts; private bodies stay in
the runner workspace and R2. An unresolved draft POST intent blocks resubmission.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stdout, redirect_stderr
from datetime import datetime
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile

DAILY = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
MANUAL = '.github/workflows/market-views-mineru-recovery.yml'
WORKFLOW = '.github/workflows/recover-report-article-delivery.yml'
PREFIXES = {'mineru-recovery': 'mineru-market-sources', 'ocr-synthesis': 'market-ocr-synthesis'}
ARTICLE_RECEIPT = 'article_recovery_receipt.json'
SHA = re.compile(r'[a-f0-9]{64}')


class DeliveryError(ValueError):
    """Only fixed program-owned categories may enter public diagnostics."""


def require(condition, category):
    if not condition:
        raise DeliveryError(category)


def encode(value):
    return json.dumps(value, sort_keys=True, ensure_ascii=True, separators=(',', ':')).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def read_json(path):
    require(path.is_file() and not path.is_symlink() and path.stat().st_size <= 32 * 1024 * 1024,
            'delivery_json_missing_or_oversized')
    return json.loads(path.read_bytes())


def write_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name('.' + path.name + '.pending')
    temporary.write_bytes(encode(value))
    temporary.replace(path)


def inputs(env):
    value = {key: env.get(key, '') for key in
             ('SOURCE_RUN_ID', 'SOURCE_HANDOFF_RUN_ID', 'SOURCE_KIND', 'DATE_FOLDER', 'EXPECTED_ARTICLES')}
    for key in ('SOURCE_RUN_ID', 'SOURCE_HANDOFF_RUN_ID'):
        require(re.fullmatch(r'[1-9][0-9]{0,19}', value[key]), 'invalid_delivery_run_id')
    require(value['SOURCE_KIND'] in PREFIXES, 'invalid_delivery_source_kind')
    require(re.fullmatch(r'\d{6}|\d{8}', value['DATE_FOLDER']), 'invalid_delivery_date')
    datetime.strptime(value['DATE_FOLDER'], '%y%m%d' if len(value['DATE_FOLDER']) == 6 else '%Y%m%d')
    require(re.fullmatch(r'[1-9][0-9]{0,3}', value['EXPECTED_ARTICLES']), 'invalid_delivery_count')
    value['EXPECTED_ARTICLES'] = int(value['EXPECTED_ARTICLES'])
    require(value['EXPECTED_ARTICLES'] <= 1000, 'invalid_delivery_count')
    return value


def api(repository, suffix):
    require(isinstance(repository, str) and re.fullmatch(
        r'[A-Za-z0-9][A-Za-z0-9-]{0,38}/[A-Za-z0-9_][A-Za-z0-9_.-]{0,99}', repository),
        'invalid_delivery_repository')
    require(isinstance(suffix, str) and re.fullmatch(
        r'[1-9][0-9]{0,19}(?:/jobs\?per_page=100&page=(?:[1-9]|10)&filter=latest'
        r'|/attempts/(?:[1-9]|10)/jobs\?per_page=100&page=(?:[1-9]|10))?', suffix),
        'invalid_delivery_metadata_path')
    token = os.environ.get('GH_TOKEN', '')
    require(token and token == token.strip() and '\r' not in token and '\n' not in token,
            'delivery_github_token_missing_or_invalid')
    # The WeChat runner needs only the declared Python dependencies. Never invoke
    # a local CLI, forward authentication to redirects, or expose provider errors.
    import requests
    limit = 16 * 1024 * 1024
    try:
        with requests.get(f'https://api.github.com/repos/{repository}/actions/runs/{suffix}',
                          headers={'Authorization': f'Bearer {token}',
                                   'Accept': 'application/vnd.github+json',
                                   'X-GitHub-Api-Version': '2022-11-28'},
                          timeout=45, allow_redirects=False, stream=True) as response:
            require(response.status_code == 200, 'delivery_github_metadata_failed')
            length = response.headers.get('Content-Length')
            if length is not None:
                require(re.fullmatch(r'[0-9]{1,20}', length), 'delivery_github_metadata_invalid')
                require(int(length) <= limit, 'delivery_github_metadata_oversized')
            body = bytearray()
            for chunk in response.iter_content(chunk_size=64 * 1024):
                require(len(body) + len(chunk) <= limit, 'delivery_github_metadata_oversized')
                body.extend(chunk)
    except requests.RequestException:
        raise DeliveryError('delivery_github_metadata_failed') from None
    try:
        value = json.loads(body)
    except (ValueError, UnicodeDecodeError):
        raise DeliveryError('delivery_github_metadata_invalid') from None
    require(isinstance(value, dict), 'delivery_github_metadata_invalid')
    return value


def jobs(repository, run_id, attempt=None):
    suffix = f'{run_id}/' + (f'attempts/{attempt}/' if attempt is not None else '')
    rows, total = [], None
    for page in range(1, 11):
        value = api(repository, suffix + f'jobs?per_page=100&page={page}' + ('&filter=latest' if attempt is None else ''))
        require(isinstance(value, dict) and type(value.get('total_count')) is int
                and isinstance(value.get('jobs'), list), 'delivery_jobs_invalid')
        total = value['total_count'] if total is None else total
        require(value['total_count'] == total and 0 <= total <= 1000, 'delivery_jobs_changed')
        rows.extend(value['jobs'])
        if len(rows) >= total:
            break
        require(value['jobs'], 'delivery_jobs_incomplete')
    require(len(rows) == total and len({row.get('id') for row in rows}) == total, 'delivery_jobs_incomplete')
    return {'total_count': total, 'jobs': rows}


def validate_original(run, attempts, config, repository, current_run_id):
    require(isinstance(run, dict) and str(run.get('id')) == config['SOURCE_RUN_ID']
            and run.get('path') == DAILY and run.get('head_branch') == 'main'
            and run.get('event') in {'schedule', 'workflow_dispatch'}
            and run.get('repository', {}).get('full_name') == repository
            and run.get('head_repository', {}).get('full_name') == repository
            and re.fullmatch(r'[a-f0-9]{40}', str(run.get('head_sha', ''))), 'original_daily_identity_invalid')
    current = current_run_id == config['SOURCE_RUN_ID']
    require(run.get('status') == 'completed' or (current and run.get('status') == 'in_progress'),
            'original_daily_not_complete')
    count = run.get('run_attempt')
    require(type(count) is int and 1 <= count <= 10 and len(attempts) == count,
            'original_attempt_inventory_invalid')
    for index, page in enumerate(attempts, 1):
        records = page.get('jobs', [])
        require(page.get('total_count') == len(records) and records, 'original_jobs_incomplete')
        for row in records:
            require(row.get('run_id') == run['id'] and row.get('head_sha') == run['head_sha'],
                    'original_job_identity_invalid')
        for name in ('push-xhs-notes-wechat-drafts', 'push-portal-translated-wechat-drafts'):
            found = [row for row in records if row.get('name') == name]
            # The current Daily's translated branch waits for these articles.
            # Its future status cannot be a precondition of producing them.
            if current and index == count and name == 'push-portal-translated-wechat-drafts':
                require(len(found) <= 1 and (not found or found[0].get('conclusion') == 'skipped'
                        or found[0].get('status') in {'queued', 'waiting', 'pending'}),
                        'original_upload_already_started')
            else:
                require(len(found) == 1 and found[0].get('conclusion') == 'skipped',
                        'original_upload_not_proven_skipped')
        selected = [row for row in records if row.get('name') == 'select-macro-reports']
        require(len(selected) == 1 and selected[0].get('conclusion') == 'success', 'original_selection_not_complete')
    return run['head_sha']


def authenticated_context(config, env):
    repository = env.get('GITHUB_REPOSITORY', '')
    workflow_ref = env.get('GITHUB_WORKFLOW_REF', '')
    require(env.get('GITHUB_ACTIONS') == 'true' and env.get('GITHUB_REF') == 'refs/heads/main'
            and workflow_ref in {f'{repository}/{path}@refs/heads/main' for path in (DAILY, MANUAL, WORKFLOW)},
            'delivery_main_workflow_required')
    original = api(repository, config['SOURCE_RUN_ID'])
    attempts = original.get('run_attempt')
    require(type(attempts) is int and 1 <= attempts <= 10, 'original_attempt_inventory_invalid')
    original_sha = validate_original(original,
        [jobs(repository, config['SOURCE_RUN_ID'], attempt) for attempt in range(1, attempts + 1)],
        config, repository, env.get('GITHUB_RUN_ID', ''))
    handoff = original if config['SOURCE_HANDOFF_RUN_ID'] == config['SOURCE_RUN_ID'] else api(repository, config['SOURCE_HANDOFF_RUN_ID'])
    require(str(handoff.get('id')) == config['SOURCE_HANDOFF_RUN_ID']
            and handoff.get('repository', {}).get('full_name') == repository
            and handoff.get('head_repository', {}).get('full_name') == repository,
            'handoff_repository_or_run_invalid')
    from market_views_source_readiness import require_source_readiness
    require_source_readiness(handoff, jobs(repository, config['SOURCE_HANDOFF_RUN_ID']), source_kind=config['SOURCE_KIND'])
    return original_sha, handoff['head_sha']


def optional_download(key, destination, client, bucket):
    try:
        client.head_object(Bucket=bucket, Key=key)
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        if code in {'404', 'NoSuchKey', 'NotFound'}:
            return False
        raise DeliveryError('delivery_checkpoint_unavailable') from None
    from private_workflow_handoff import download_directory
    download_directory(key, destination, client=client, bucket=bucket)
    return True


def state(workspace):
    return read_json(workspace / 'context.json')


def context_prefix(context):
    return ('_private-workflow-handoff/xhs-recovery/' + context['source_run_id'] + '/'
            + context['date_folder'] + '/' + context['manifest_sha256'])


def validate_source(root, config, original_sha, handoff_sha):
    if config['SOURCE_KIND'] == 'mineru-recovery':
        from recover_durable_mineru_sources import validate_sources, RECEIPT
        receipt = validate_sources(root, config['EXPECTED_ARTICLES'], config['DATE_FOLDER'],
            expected_recovery_run_id=config['SOURCE_HANDOFF_RUN_ID'], expected_execution_sha=handoff_sha)
        require(receipt['source_run_id'] == config['SOURCE_RUN_ID'] and receipt['source_execution_sha'] == original_sha,
                'recovered_original_identity_invalid')
    else:
        from market_views_publication import validate_ocr_synthesis_receipt, RECEIPT_NAME
        RECEIPT = RECEIPT_NAME
        require(config['SOURCE_RUN_ID'] == config['SOURCE_HANDOFF_RUN_ID'], 'ocr_original_run_invalid')
        receipt = validate_ocr_synthesis_receipt(root, date_folder=config['DATE_FOLDER'],
            expected_reports=config['EXPECTED_ARTICLES'], source_run_id=config['SOURCE_RUN_ID'], execution_sha=original_sha)
    manifest_sha = digest((root / 'selected_to_process_manifest.json').read_bytes())
    return {'schema_version': 1, 'source_run_id': config['SOURCE_RUN_ID'],
        'source_handoff_run_id': config['SOURCE_HANDOFF_RUN_ID'], 'source_kind': config['SOURCE_KIND'],
        'date_folder': config['DATE_FOLDER'], 'expected_articles': config['EXPECTED_ARTICLES'],
        'source_execution_sha': original_sha, 'handoff_execution_sha': handoff_sha,
        'source_receipt_sha256': digest((root / RECEIPT).read_bytes()), 'manifest_sha256': manifest_sha}


def prepare(workspace, config, env, client, bucket):
    from private_workflow_handoff import download_directory
    original_sha, handoff_sha = authenticated_context(config, env)
    source = workspace / 'source'
    download_directory(f"_private-workflow-handoff/{PREFIXES[config['SOURCE_KIND']]}/{config['SOURCE_HANDOFF_RUN_ID']}/{config['DATE_FOLDER']}/shard_0.tar.gz",
                       source, client=client, bucket=bucket)
    context = validate_source(source, config, original_sha, handoff_sha)
    claim_original(context, client, bucket)
    write_json(workspace / 'context.json', context)
    checkpoint = workspace / 'checkpoint'
    if optional_download(context_prefix(context) + '/generation.tar.gz', checkpoint, client, bucket):
        require(read_json(checkpoint / 'context.json') == context, 'generation_checkpoint_source_changed')
    else:
        write_json(checkpoint / 'context.json', context)
    (checkpoint / 'articles').mkdir(parents=True, exist_ok=True)
    return context


def claim_original(context, client, bucket):
    """One original run owns delivery for the same date and selected inventory."""
    key = ('_private-workflow-handoff/xhs-recovery-claims/' + context['date_folder']
           + '/' + context['manifest_sha256'] + '.json')
    identity = {name: context[name] for name in ('source_run_id', 'date_folder', 'manifest_sha256')}
    try:
        client.put_object(Bucket=bucket, Key=key, Body=encode(identity),
                          ContentType='application/json', IfNoneMatch='*')
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        require(code in {'412', 'PreconditionFailed', 'ConditionalRequestConflict'}, 'delivery_claim_unavailable')
        saved = client.get_object(Bucket=bucket, Key=key)['Body'].read(4097)
        require(len(saved) <= 4096 and json.loads(saved) == identity, 'delivery_claim_other_original_run')


def article_receipt(workspace, context):
    from recover_report_articles import validate_articles
    root = workspace / 'checkpoint' / 'articles'
    receipt = validate_articles(root, context['expected_articles'], context['date_folder'],
        source_kind=context['source_kind'], source_receipt_sha256=context['source_receipt_sha256'])
    require(receipt['source_run_id'] == context['source_run_id']
            and receipt['source_execution_sha'] == context['source_execution_sha']
            and receipt['source_handoff_run_id'] == context['source_handoff_run_id']
            and receipt['source_handoff_execution_sha'] == context['handoff_execution_sha'], 'article_original_identity_invalid')
    return receipt


def save_generation(workspace, client, bucket, complete=False):
    from private_workflow_handoff import upload_directory
    context = state(workspace)
    checkpoint = workspace / 'checkpoint'
    require(read_json(checkpoint / 'context.json') == context, 'generation_checkpoint_source_changed')
    save_private_logs(workspace, checkpoint / 'private-diagnostics')
    prefix = context_prefix(context)
    # Never replace a durable completed checkpoint with an invalid full package.
    receipt = article_receipt(workspace, context) if complete or (checkpoint / 'articles' / ARTICLE_RECEIPT).exists() else None
    upload_directory(checkpoint, prefix + '/generation.tar.gz', client=client, bucket=bucket)
    if complete:
        upload_directory(checkpoint / 'articles', prefix + '/articles/shard_0.tar.gz', client=client, bucket=bucket)
        return {'article_handoff_prefix': prefix + '/articles', 'article_count': receipt['report_count'],
                'context_sha256': digest(encode(context)), 'manifest_sha256': context['manifest_sha256']}
    return {}


def delivery_identity(context, article_root):
    return {'schema_version': 1, 'context_sha256': digest(encode(context)),
            'article_receipt_sha256': digest((article_root / ARTICLE_RECEIPT).read_bytes())}


def restore_delivery(workspace, config, env, client, bucket):
    # Reauthenticate the run, but use the exact package already checked by the
    # generation job; no private source contents are exposed through outputs.
    original_sha, handoff_sha = authenticated_context(config, env)
    manifest_sha = env.get('DELIVERY_MANIFEST_SHA256', '')
    require(SHA.fullmatch(manifest_sha), 'delivery_manifest_hash_invalid')
    prefix = f"_private-workflow-handoff/xhs-recovery/{config['SOURCE_RUN_ID']}/{config['DATE_FOLDER']}/{manifest_sha}"
    from private_workflow_handoff import download_directory
    checkpoint = workspace / 'checkpoint'
    download_directory(prefix + '/generation.tar.gz', checkpoint, client=client, bucket=bucket)
    context = read_json(checkpoint / 'context.json')
    require(digest(encode(context)) == env.get('DELIVERY_CONTEXT_SHA256')
            and context['source_execution_sha'] == original_sha and context['handoff_execution_sha'] == handoff_sha
            and context['source_run_id'] == config['SOURCE_RUN_ID'] and context['source_handoff_run_id'] == config['SOURCE_HANDOFF_RUN_ID']
            and context['source_kind'] == config['SOURCE_KIND'] and context['date_folder'] == config['DATE_FOLDER']
            and context['expected_articles'] == config['EXPECTED_ARTICLES'] and context['manifest_sha256'] == manifest_sha,
            'delivery_context_changed')
    write_json(workspace / 'context.json', context)
    claim_original(context, client, bucket)
    article_receipt(workspace, context)
    destination = workspace / 'xhs' / context['date_folder'] / 'shard_0'
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(checkpoint / 'articles', destination)
    receipts = workspace / 'wechat_drafts' / 'xhs_notes' / context['date_folder']
    identity = delivery_identity(context, checkpoint / 'articles')
    with tempfile.TemporaryDirectory(dir=workspace) as temporary:
        restored = Path(temporary) / 'receipts'
        if optional_download(prefix + '/wechat-receipts.tar.gz', restored, client, bucket):
            require(read_json(restored / 'delivery_identity.json') == identity, 'accepted_article_identity_changed')
            restored_summary = read_json(restored / 'wechat_draft_summary.json')
            if restored_summary.get('status') == 'skipped_title_policy' and restored_summary.get('drafts') == []:
                shutil.copytree(restored, receipts)
            else:
                from recover_private_wechat_handoff import merge_receipts
                merge_receipts(receipts, restored)
    write_json(receipts / 'delivery_identity.json', identity)
    if (receipts / 'wechat_draft_summary.json').is_file() and read_json(receipts / 'wechat_draft_summary.json').get('status') == 'skipped_title_policy':
        validate_delivery(workspace)
    return context


def receipt_root(workspace, context):
    return workspace / 'wechat_drafts' / 'xhs_notes' / context['date_folder']


def save_receipts(workspace, client, bucket):
    from private_workflow_handoff import upload_directory
    context = state(workspace)
    root = receipt_root(workspace, context)
    if not (root / 'wechat_draft_summary.json').is_file():
        return False
    summary = read_json(root / 'wechat_draft_summary.json')
    require(summary.get('dry_run') is False, 'dry_run_receipt_forbidden')
    if not any(row.get('media_id') for row in summary.get('drafts', []) if isinstance(row, dict)):
        if summary.get('status') != 'skipped_title_policy':
            return False
        validate_delivery(workspace)
    require(read_json(root / 'delivery_identity.json') == delivery_identity(context, workspace / 'checkpoint' / 'articles'),
            'accepted_article_identity_changed')
    save_private_logs(workspace, root / 'private-diagnostics')
    final_receipt = workspace / 'wechat_delivery_receipt.json'
    if final_receipt.is_file():
        shutil.copyfile(final_receipt, root / final_receipt.name)
    upload_directory(root, context_prefix(context) + '/wechat-receipts.tar.gz', client=client, bucket=bucket)
    return True


def save_private_logs(workspace, destination):
    for name in ('private-delivery.log', 'private-generation.log'):
        path = workspace / name
        if path.is_file() and not path.is_symlink():
            destination.mkdir(parents=True, exist_ok=True)
            with path.open('rb') as source:
                source.seek(max(0, path.stat().st_size - 2 * 1024 * 1024))
                (destination / name).write_bytes(source.read(2 * 1024 * 1024))


def validate_delivery(workspace):
    context = state(workspace)
    receipt = article_receipt(workspace, context)
    root = receipt_root(workspace, context)
    summary = read_json(root / 'wechat_draft_summary.json')
    expected = context['expected_articles']
    from push_xhs_notes_to_wechat_drafts import xhs_article_title_metadata, hard_blocked_xhs_title_record
    eligible, blocked = set(), {}
    article_root = workspace / 'checkpoint' / 'articles'
    for report in receipt['reports']:
        name = report['directory']
        metadata = xhs_article_title_metadata(article_root / name)
        # A failed body cannot hide behind an otherwise legitimate title policy.
        require(not metadata.get('generation_failure_reason'), 'wechat_generation_failure_present')
        exclusion = hard_blocked_xhs_title_record(metadata)
        if exclusion:
            blocked[name] = canonical_policy_record(exclusion)
        else:
            eligible.add(name)
    require(len(eligible) + len(blocked) == expected, 'wechat_source_partition_invalid')
    recorded_exclusions = summary.get('skipped_title_policy', [])
    require(isinstance(recorded_exclusions, list) and len(recorded_exclusions) == len(blocked),
            'wechat_policy_exclusion_mismatch')
    observed = {}
    for row in recorded_exclusions:
        normalized = canonical_policy_record(row)
        name = normalized['report_dir']
        require(name not in observed and name in blocked and normalized == blocked[name],
                'wechat_policy_exclusion_mismatch')
        observed[name] = normalized
    require(observed == blocked, 'wechat_policy_exclusion_mismatch')
    require(summary.get('dry_run') is False and summary.get('publish') is False
            and summary.get('status') == ('verified' if eligible else 'skipped_title_policy')
            and summary.get('date_folder') == context['date_folder']
            and summary.get('input_selected_count') == expected and summary.get('selected_count') == len(eligible)
            and summary.get('skipped_title_policy_count') == len(blocked)
            and summary.get('skipped_generation_failure_count') == 0
            and summary.get('skipped_generation_failures', []) == [],
            'wechat_article_coverage_incomplete')
    rows = summary.get('articles', [])
    require(isinstance(rows, list) and all(isinstance(row, dict) for row in rows)
            and len(rows) == len(eligible) and {Path(row.get('report_dir', '')).name for row in rows} == eligible,
            'wechat_article_identity_incomplete')
    drafts = summary.get('drafts', [])
    require(isinstance(drafts, list) and bool(drafts) == bool(eligible)
            and summary.get('draft_count') == len(drafts), 'wechat_drafts_missing')
    media, groups, count = set(), set(), 0
    from push_portal_translated_to_wechat_drafts import draft_group_key
    for draft in drafts:
        result = draft.get('draft_get', {})
        media_id, group = draft.get('media_id'), draft.get('group_key')
        require(isinstance(media_id, str) and media_id and media_id not in media
                and isinstance(group, str) and SHA.fullmatch(group) and group not in groups
                and draft.get('status') == 'verified' and result.get('ok') is True
                and result.get('matches_editorial_contract') is True
                and result.get('matches_expected_article_count') is True
                and result.get('matches_expected_titles') is True,
                'wechat_draft_readback_incomplete')
        name = Path(str(draft.get('payload', ''))).name
        require(re.fullmatch(r'draft_payload_[A-Za-z0-9_-]+\.json', name), 'wechat_payload_invalid')
        payload = read_json(root / name)
        articles = payload.get('articles', [])
        require(articles and len(articles) == draft.get('article_count') == result.get('article_count')
                and draft_group_key(articles) == group, 'wechat_payload_identity_changed')
        count += len(articles); media.add(media_id); groups.add(group)
    require(count == len(eligible), 'wechat_article_coverage_incomplete')
    # Blog ingestion scans payload files, including restored aliases. Do not
    # let an old, now-unaccounted payload bypass the verified current partition.
    for path in root.glob('draft_payload_*.json'):
        payload = read_json(path)
        articles = payload.get('articles')
        require(isinstance(articles, list) and articles and draft_group_key(articles) in groups,
                'wechat_unaccounted_archive_payload')
    result = {'schema_version': 1, 'complete': True, 'source_run_id': context['source_run_id'],
              'date_folder': context['date_folder'], 'article_count': count, 'draft_count': len(drafts),
              'source_report_count': expected, 'policy_excluded_count': len(blocked),
              'accounted_report_count': count + len(blocked),
              'article_receipt_sha256': digest((workspace / 'checkpoint' / 'articles' / ARTICLE_RECEIPT).read_bytes())}
    write_json(workspace / 'wechat_delivery_receipt.json', result)
    return result


def canonical_policy_record(record):
    """Compare the complete recomputed policy evidence across runner paths."""
    require(isinstance(record, dict) and isinstance(record.get('report_dir'), str)
            and isinstance(record.get('wechat_markdown'), str), 'wechat_policy_exclusion_mismatch')
    value = dict(record)
    directory = Path(value['report_dir']).name
    markdown = Path(value['wechat_markdown'])
    require(markdown.name == 'wechat_article.md' and markdown.parent.name == directory,
            'wechat_policy_exclusion_mismatch')
    value['report_dir'] = directory
    value['wechat_markdown'] = directory + '/wechat_article.md'
    return value


def guarded_add_draft(client, bucket, prefix, session, token, articles, timeout):
    """Never retry an unknown POST; preserve the existing known-rejection repair."""
    import push_portal_translated_to_wechat_drafts as api_module
    group = api_module.draft_group_key(articles)
    key = prefix + '/wechat-intents/' + group + '.json'
    intent = {'schema_version': 1, 'group_sha256': group, 'state': 'submitting'}
    try:
        client.put_object(Bucket=bucket, Key=key, Body=encode(intent),
                          ContentType='application/json', IfNoneMatch='*')
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        require(code in {'412', 'PreconditionFailed', 'ConditionalRequestConflict'}, 'wechat_intent_unavailable')
        raw = client.get_object(Bucket=bucket, Key=key)['Body'].read(8193)
        require(len(raw) <= 8192, 'wechat_intent_invalid')
        saved = json.loads(raw)
        require(saved.get('schema_version') == 1 and saved.get('group_sha256') == group
                and saved.get('state') in {'submitting', 'accepted'}, 'wechat_intent_invalid')
        if saved['state'] == 'accepted':
            require(isinstance(saved.get('media_id'), str) and saved['media_id'], 'wechat_intent_invalid')
            return saved['media_id']
        # A lost ACK can be resolved only by readback, never by another POST.
        media = api_module.recover_draft_after_ambiguous_add(session, token, articles, timeout)
        require(media, 'wechat_submission_intent_unresolved')
        client.put_object(Bucket=bucket, Key=key, Body=encode(dict(intent, state='accepted', media_id=media)),
                          ContentType='application/json')
        return media
    try:
        response = api_module.post_wechat_json(session,
            f'https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}', {'articles': articles}, timeout,
            max_attempts=1)
        result = api_module.parse_wechat_json(response, 'draft/add')
        media = result.get('media_id')
        if not isinstance(media, str) or not media:
            media = api_module.recover_draft_after_ambiguous_add(session, token, articles, timeout)
            require(media, 'wechat_submission_intent_unresolved')
    except api_module.WeChatError as error:
        if error.errcode is not None and (api_module.is_cover_crop_error(error)
                or api_module.is_article_size_error(error)):
            # These structured API errors establish that no draft was accepted.
            # Let the existing uploader repair the cover or split the group.
            client.delete_object(Bucket=bucket, Key=key)
            raise
        if error.errcode is None:
            media = api_module.recover_draft_after_ambiguous_add(session, token, articles, timeout)
            require(media, 'wechat_submission_intent_unresolved')
        else:
            raise
    client.put_object(Bucket=bucket, Key=key, Body=encode(dict(intent, state='accepted', media_id=media)),
                      ContentType='application/json')
    return media


def upload_wechat(workspace, client, bucket):
    """Use the existing uploader, persisting each ACK before the next request."""
    import push_xhs_notes_to_wechat_drafts as uploader
    context = state(workspace)
    article_receipt(workspace, context)
    original_checkpoint, original_add = uploader.checkpoint_wechat_drafts, uploader.add_draft
    prefix = context_prefix(context)

    def checkpoint(*args, **kwargs):
        original_checkpoint(*args, **kwargs)
        save_receipts(workspace, client, bucket)

    def add(session, token, articles, timeout):
        return guarded_add_draft(client, bucket, prefix, session, token, articles, timeout)

    uploader.checkpoint_wechat_drafts, uploader.add_draft = checkpoint, add
    argv = sys.argv
    sys.argv = ['push_xhs_notes_to_wechat_drafts.py', '--dropbox-output-root', str(workspace / 'xhs'),
        '--date-folder', context['date_folder'], '--output-root', str(workspace / 'wechat_drafts' / 'xhs_notes'),
        '--max-articles', 'all', '--articles-per-draft', '8', '--max-body-chars', '1200',
        '--min-inline-images', '3', '--max-inline-images', '3']
    try:
        require(uploader.main() == 0, 'wechat_upload_failed')
        return validate_delivery(workspace)
    finally:
        sys.argv = argv
        uploader.checkpoint_wechat_drafts, uploader.add_draft = original_checkpoint, original_add


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('prepare', 'save-generation', 'complete-generation',
        'restore-delivery', 'upload-wechat', 'save-receipts', 'validate-delivery'))
    parser.add_argument('--workspace', type=Path, required=True)
    args = parser.parse_args(argv)
    workspace = args.workspace
    require(not workspace.is_symlink(), 'delivery_workspace_invalid')
    workspace.mkdir(parents=True, exist_ok=True)
    try:
        config = inputs(os.environ)
        from private_workflow_handoff import build_r2_client, r2_bucket
        with (workspace / 'private-delivery.log').open('a') as log, redirect_stdout(log), redirect_stderr(log):
            client, bucket = build_r2_client(), r2_bucket()
            if args.command == 'prepare':
                result = prepare(workspace, config, os.environ, client, bucket)
            elif args.command in {'save-generation', 'complete-generation'}:
                result = save_generation(workspace, client, bucket, args.command == 'complete-generation')
            elif args.command == 'restore-delivery':
                result = restore_delivery(workspace, config, os.environ, client, bucket)
            elif args.command == 'upload-wechat':
                result = upload_wechat(workspace, client, bucket)
            elif args.command == 'save-receipts':
                result = {'saved': save_receipts(workspace, client, bucket)}
            else:
                result = validate_delivery(workspace)
        if args.command == 'complete-generation':
            with open(os.environ['GITHUB_OUTPUT'], 'a') as output:
                for key, value in result.items():
                    output.write(f'{key}={value}\n')
        print(json.dumps({'status': 'complete', 'stage': args.command,
                          **({key: result[key] for key in ('article_count', 'draft_count', 'source_report_count',
                              'policy_excluded_count', 'accounted_report_count') if key in result})}))
        return 0
    except Exception as error:
        # Error text from SDKs, HTML generation or providers may contain bodies.
        import traceback
        with (workspace / 'private-delivery.log').open('a') as log:
            traceback.print_exc(file=log)
        category = str(error) if isinstance(error, DeliveryError) else type(error).__name__
        print(json.dumps({'status': 'incomplete', 'stage': args.command, 'category': category}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
