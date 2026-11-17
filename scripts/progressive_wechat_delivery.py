#!/usr/bin/env python3
"""Publish ready fixed groups from a source-bound Daily batch and resume by receipt."""
from __future__ import annotations

import argparse
from contextlib import contextmanager
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import time
import unicodedata

from market_views_partial_sources import read_selection
from private_workflow_handoff import build_r2_client, r2_bucket, download_directory, upload_directory
from run_pdf_to_xhs_in_batches import unique_batch_name, slug
from wechat_account_routing import read_routes, ROUTING_KEY, parse_source_date, route_start_date
from wechat_accounts import ACCOUNT_NAMES


class ProgressiveError(ValueError):
    pass


def require(condition, reason):
    if not condition:
        raise ProgressiveError(reason)


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(',', ':')).encode()


def digest(value):
    return hashlib.sha256(value).hexdigest()


def write_json(path, value):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + '.pending')
    temporary.write_bytes(encoded(value))
    temporary.replace(path)


def read_json(path):
    return json.loads(Path(path).read_bytes())


def progressive_prefix(source_run_id, date_folder):
    require(re.fullmatch(r'[1-9][0-9]{0,19}', str(source_run_id)) and re.fullmatch(r'(?:[0-9]{6}|[0-9]{8})', date_folder), 'progressive_identity_invalid')
    parse_source_date(date_folder)
    return f'_private-workflow-handoff/daily-wechat-progressive/{source_run_id}/{date_folder}'


plan_prefix = progressive_prefix


def read_object(client, bucket, key):
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as error:
        if str(getattr(error, 'response', {}).get('Error', {}).get('Code', '')) in {'NoSuchKey', '404', 'NotFound'}:
            return None, None
        raise
    with response['Body'] as stream:
        body = stream.read(8 * 1024 * 1024 + 1)
    require(len(body) <= 8 * 1024 * 1024 and response.get('ETag'), 'progressive_object_invalid')
    return json.loads(body), response['ETag']


def validate_plan(plan):
    require(isinstance(plan, dict) and plan.get('schema_version') == 1, 'progressive_plan_invalid')
    progressive_prefix(plan.get('source_run_id'), plan.get('date_folder', ''))
    require(re.fullmatch(r'[a-f0-9]{40}', plan.get('source_execution_sha', '')), 'progressive_sha_invalid')
    require(plan.get('plan_sha256') == digest(encoded({key: value for key, value in plan.items() if key != 'plan_sha256'})), 'progressive_plan_digest_invalid')
    sources, groups = plan.get('sources'), plan.get('groups')
    require(isinstance(sources, list) and sources and isinstance(groups, list), 'progressive_plan_inventory_invalid')
    identities = [row.get('source_id') for row in sources]
    require(len(set(identities)) == len(identities), 'progressive_source_duplicate')
    for row in sources:
        require(row.get('source_id') == digest((row['source_pdf'] + '\0' + row['content_sha256']).encode())
                and re.fullmatch(r'[a-f0-9]{64}', row['content_sha256'])
                and row.get('account') in {*ACCOUNT_NAMES, None}, 'progressive_source_invalid')
    selected = [row['source_id'] for row in sources if row['selected']]
    grouped = [source for group in groups for source in group['source_ids']]
    require(len(grouped) == len(set(grouped)) and set(grouped) == set(selected), 'progressive_group_partition_invalid')
    by_id = {row['source_id']: row for row in sources}
    for group in groups:
        require(1 <= len(group['source_ids']) <= plan['articles_per_draft']
                and all(by_id[source]['account'] == group['account'] for source in group['source_ids'])
                and group['group_id'] == digest(encoded({'account': group['account'], 'source_ids': group['source_ids']})), 'progressive_group_invalid')
    return plan


def load_plan(client, bucket, source_run_id, date_folder, source_execution_sha, manifest_sha256=None):
    plan, _version = read_object(client, bucket, progressive_prefix(source_run_id, date_folder) + '/plan.json')
    if plan is None:
        return None
    validate_plan(plan)
    require(plan['source_run_id'] == str(source_run_id) and plan['date_folder'] == date_folder
            and plan['source_execution_sha'] == source_execution_sha, 'progressive_plan_owner_changed')
    if manifest_sha256 is not None:
        require(plan['manifest_sha256'] == manifest_sha256, 'progressive_manifest_changed')
    return plan


def balanced_route_reservation(client, bucket, route_ids, capacity):
    """Reserve the smallest globally balanced group inventory without moving old sources."""
    accounts = tuple(ACCOUNT_NAMES)
    for attempt in range(6):
        assigned, version = read_routes(client, bucket)
        before = dict(assigned)
        existing = {account: sum(assigned.get(source) == account for source in route_ids) for account in accounts}
        total = len(route_ids)
        count = max(min(len(accounts) * 3, total), (total + capacity - 1) // capacity)
        group_counts = {account: (existing[account] + capacity - 1) // capacity for account in accounts}
        count = max(count, sum(group_counts.values()))
        for _ in range(count - sum(group_counts.values())):
            account = min(accounts, key=lambda item: (group_counts[item], accounts.index(item)))
            group_counts[account] += 1
        quotas = dict(existing)
        for _ in range(total - sum(quotas.values())):
            eligible = [account for account in accounts if quotas[account] < group_counts[account] * capacity]
            account = min(eligible, key=lambda item: (quotas[item], accounts.index(item)))
            quotas[account] += 1
        group_counts = {account: min(group_counts[account], quotas[account]) for account in accounts}
        for _ in range(count - sum(group_counts.values())):
            eligible = [account for account in accounts if group_counts[account] < quotas[account]]
            account = min(eligible, key=lambda item: (group_counts[item], accounts.index(item)))
            group_counts[account] += 1
        # Keep fresh fixed groups contiguous in source order, so the first group
        # need not wait for three accounts' interleaved reports to finish.
        unassigned = [source for source in route_ids if source not in assigned]
        remaining = {account: quotas[account] - existing[account] for account in accounts}
        batches = {account: [] for account in accounts}
        for account in accounts:
            count = min(group_counts[account], quotas[account])
            if count:
                size, extra = divmod(quotas[account], count)
                batches[account] = [size + int(index < extra) for index in range(count)]
        offset = 0
        for index in range(max(map(len, batches.values()), default=0)):
            for account in accounts:
                if index >= len(batches[account]):
                    continue
                size = min(batches[account][index], remaining[account])
                for source in unassigned[offset:offset + size]:
                    assigned[source] = account
                offset += size
                remaining[account] -= size
        require(offset == len(unassigned), 'progressive_route_partition_invalid')
        if assigned == before:
            return {source: assigned[source] for source in route_ids}, group_counts
        try:
            client.put_object(Bucket=bucket, Key=ROUTING_KEY,
                Body=encoded({'version': 1, 'assigned': assigned}), ContentType='application/json',
                CacheControl='private, no-store', **({'IfMatch': version} if version else {'IfNoneMatch': '*'}))
        except Exception as error:
            if getattr(error, 'response', {}).get('ResponseMetadata', {}).get('HTTPStatusCode') not in {409, 412}:
                # Read back an unknown conditional write before making another allocation.
                observed, _ = read_routes(client, bucket)
                require(all(observed.get(source) == assigned[source] for source in route_ids), 'progressive_route_write_unresolved')
                return {source: assigned[source] for source in route_ids}, group_counts
            time.sleep(min(.25 * 2 ** attempt, 2))
        else:
            return {source: assigned[source] for source in route_ids}, group_counts
    raise ProgressiveError('progressive_routes_busy')


def create_plan(manifest, source_run_id, date_folder, source_execution_sha, reports_per_shard, articles_per_draft, max_articles, client, bucket):
    raw, rows = read_selection(Path(manifest))
    existing = load_plan(client, bucket, source_run_id, date_folder, source_execution_sha, digest(raw))
    limit = len(rows) if str(max_articles).lower() == 'all' else min(len(rows), int(max_articles))
    require(0 <= limit <= len(rows) and reports_per_shard > 0 and 1 <= articles_per_draft <= 8, 'progressive_options_invalid')
    if existing is not None:
        require(existing['reports_per_shard'] == reports_per_shard and existing['articles_per_draft'] == articles_per_draft
                and existing['selection_limit'] == limit, 'progressive_options_changed')
        return existing
    sources = []
    start = route_start_date()
    from datetime import timedelta
    routed = start and parse_source_date(date_folder) + timedelta(days=1) >= start
    require(not routed or os.environ.get('WECHAT_ROUTING_SCOPE') == 'dropbox', 'progressive_routing_scope_invalid')
    route_ids = []
    for index, row in enumerate(rows):
        ordinal = index % reports_per_shard + 1
        staged = unique_batch_name(Path(row['process_local_path']), ordinal)
        # This is exactly the source_pdf basename used by the normal producer.
        source_name = unicodedata.normalize('NFC', staged)
        route_id = digest(f'dropbox\0{parse_source_date(date_folder)}\0{source_name}'.encode())
        route_ids.append(route_id)
        sources.append({'source_id': digest((row['source_pdf'] + '\0' + row['content_sha256']).encode()),
                        'source_pdf': row['source_pdf'], 'content_sha256': row['content_sha256'],
                        'report_relative': f'shard_{index // reports_per_shard}/{slug(staged)}',
                        'staged_name': staged, 'selected': index < limit, 'account': None})
    if routed:
        assignments, group_counts = balanced_route_reservation(client, bucket, route_ids[:limit], articles_per_draft)
        for row, route_id in zip(sources[:limit], route_ids[:limit]):
            row['account'] = assignments[route_id]
    groups = []
    for account in dict.fromkeys(row['account'] for row in sources[:limit]):
        source_ids = [row['source_id'] for row in sources[:limit] if row['account'] == account]
        if account is not None:
            count = min(len(source_ids), group_counts[account])
            size, extra = divmod(len(source_ids), count)
            sizes = [size + int(index < extra) for index in range(count)]
        else:
            sizes = [min(articles_per_draft, len(source_ids) - index) for index in range(0, len(source_ids), articles_per_draft)]
        offset = 0
        for size in sizes:
            group = {'account': account, 'source_ids': source_ids[offset:offset + size]}
            groups.append({**group, 'group_id': digest(encoded(group))})
            offset += size
    # Round-robin accounts also lets their persisted cooldowns overlap.
    by_account = {account: [group for group in groups if group['account'] == account] for account in dict.fromkeys(group['account'] for group in groups)}
    groups = [items[index] for index in range(max(map(len, by_account.values()), default=0)) for items in by_account.values() if index < len(items)]
    plan = {'schema_version': 1, 'source_run_id': str(source_run_id), 'source_execution_sha': source_execution_sha,
            'date_folder': date_folder, 'manifest_sha256': digest(raw), 'reports_per_shard': reports_per_shard,
            'articles_per_draft': articles_per_draft, 'selection_limit': limit, 'sources': sources, 'groups': groups}
    plan['plan_sha256'] = digest(encoded(plan))
    validate_plan(plan)
    key = progressive_prefix(source_run_id, date_folder) + '/plan.json'
    try:
        client.put_object(Bucket=bucket, Key=key, Body=encoded(plan), ContentType='application/json', IfNoneMatch='*')
    except Exception:
        accepted = load_plan(client, bucket, source_run_id, date_folder, source_execution_sha, digest(raw))
        require(accepted == plan, 'progressive_plan_write_unresolved')
    require(load_plan(client, bucket, source_run_id, date_folder, source_execution_sha, digest(raw)) == plan, 'progressive_plan_readback_mismatch')
    return plan


def source_directories(plan, source_root):
    result = {}
    for row in plan['sources']:
        report = Path(source_root) / row['report_relative']
        if not (report / 'wechat_article.md').is_file():
            continue
        require(not report.is_symlink(), 'progressive_source_symlink')
        status = read_json(report / 'status.json')
        require(status.get('original_pdf_sha256') == row['content_sha256']
                and Path(str(status.get('source_pdf', ''))).name == row['staged_name'], 'progressive_source_binding_mismatch')
        if status.get('error') or status.get('wechat_article') != 'wechat_article.md':
            continue
        result[row['source_id']] = report
    return result


def restore_ready_sources(plan, source_root, client, bucket):
    """Admit independently completed reports only with the exact frozen source receipt."""
    existing = source_directories(plan, source_root)
    for source in plan['sources']:
        if source['source_id'] in existing:
            continue
        key = f"_private-workflow-handoff/xhs-ready/{plan['source_run_id']}/{plan['date_folder']}/source_{source['source_id']}.tar.gz"
        with tempfile.TemporaryDirectory(prefix='progressive-ready-') as temporary:
            directory = Path(temporary) / 'report'
            try:
                download_directory(key, directory, client=client, bucket=bucket)
            except Exception as error:
                if str(getattr(error, 'response', {}).get('Error', {}).get('Code', '')) in {'NoSuchKey', '404', 'NotFound'}:
                    continue
                raise
            receipt = read_json(directory / 'progressive_source.json')
            expected = {'schema_version': 1, 'source_run_id': plan['source_run_id'],
                'source_execution_sha': plan['source_execution_sha'], 'date_folder': plan['date_folder'],
                'source_pdf': source['source_pdf'], 'content_sha256': source['content_sha256'],
                'manifest_sha256': plan['manifest_sha256']}
            require(all(receipt.get(key) == value for key, value in expected.items()), 'progressive_ready_owner_changed')
            status = read_json(directory / 'status.json')
            require(status.get('original_pdf_sha256') == source['content_sha256']
                    and Path(str(status.get('source_pdf', ''))).name == source['staged_name']
                    and status.get('wechat_article') == 'wechat_article.md' and not status.get('error')
                    and (directory / 'wechat_article.md').is_file(), 'progressive_ready_source_invalid')
            target = Path(source_root) / source['report_relative']
            target.parent.mkdir(parents=True, exist_ok=True)
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(directory, target)
    return source_directories(plan, source_root)


def recovery_source_dirs(plan, article_root):
    result = {}
    for status_path in Path(article_root).glob('*/status.json'):
        status = read_json(status_path)
        names = {Path(str(status.get(key, ''))).name for key in ('source_pdf', 'original_filename', 'source_report_original_name', 'original_report_name')}
        matches = [row for row in plan['sources'] if row['content_sha256'] == status.get('original_pdf_sha256')
                   and names.intersection({row['source_pdf'], row['staged_name']})]
        require(len(matches) == 1 and matches[0]['source_id'] not in result, 'progressive_recovery_source_ambiguous')
        require((status_path.parent / 'wechat_article.md').is_file() and not status.get('error'), 'progressive_recovery_article_missing')
        result[matches[0]['source_id']] = status_path.parent
    require(set(result) == {row['source_id'] for row in plan['sources']}, 'progressive_recovery_source_incomplete')
    return result


def group_directory(workspace, plan, group):
    return Path(workspace) / '.progressive-wechat' / plan['source_run_id'] / plan['date_folder'] / group['group_id'] / plan['date_folder']


def restore_group(plan, group, directory, client, bucket):
    key = progressive_prefix(plan['source_run_id'], plan['date_folder']) + '/groups/' + group['group_id'] + '.tar.gz'
    try:
        download_directory(key, directory, client=client, bucket=bucket)
    except Exception as error:
        if str(getattr(error, 'response', {}).get('Error', {}).get('Code', '')) not in {'NoSuchKey', '404', 'NotFound'}:
            raise
    marker = directory / 'progressive_group.json'
    if marker.exists():
        saved = read_json(marker)
        require(saved['plan_sha256'] == plan['plan_sha256'] and saved['group_id'] == group['group_id'], 'progressive_group_owner_changed')
        return saved
    require(not (directory / 'wechat_draft_summary.json').exists(), 'progressive_unbound_receipt')
    return {'plan_sha256': plan['plan_sha256'], 'group_id': group['group_id'], 'complete': False}


def save_group(plan, group, directory, client, bucket, complete=False):
    write_json(directory / 'progressive_group.json', {'plan_sha256': plan['plan_sha256'], 'group_id': group['group_id'], 'complete': complete})
    key = progressive_prefix(plan['source_run_id'], plan['date_folder']) + '/groups/' + group['group_id'] + '.tar.gz'
    with tempfile.TemporaryDirectory(prefix='progressive-receipt-') as temporary:
        target = Path(temporary)
        for path in directory.glob('*.json'):
            shutil.copyfile(path, target / path.name)
        upload_directory(target, key, client=client, bucket=bucket)


def api_draft_delay(arguments):
    from push_portal_translated_to_wechat_drafts import DEFAULT_WECHAT_DRAFT_DELAY_SECONDS
    parser = argparse.ArgumentParser(add_help=False)
    parser.add_argument('--draft-delay-seconds', type=float, default=DEFAULT_WECHAT_DRAFT_DELAY_SECONDS)
    options, _ = parser.parse_known_args(arguments)
    require(options.draft_delay_seconds >= 0, 'progressive_pacing_invalid')
    return options.draft_delay_seconds


def paced_submission(client, bucket, prefix, account, delay, submit, *, now=time.time, sleep=time.sleep):
    key = prefix + '/pacing/' + (account or 'kc') + '.json'
    previous, version = read_object(client, bucket, key)
    if previous is None and delay:
        # Other WeChat jobs do not yet write this batch ledger. Preserve the
        # configured first-submission interval once, then use elapsed time.
        sleep(delay)
    if previous is not None:
        require(isinstance(previous, dict) and isinstance(previous.get('last_attempt_at'), (int, float)), 'progressive_pacing_receipt_invalid')
        remaining = max(0, previous.get('accepted_at', previous['last_attempt_at']) + delay - now())
        if remaining:
            sleep(remaining)
    attempted = {'last_attempt_at': now()}
    condition = {'IfMatch': version} if version else {'IfNoneMatch': '*'}
    try:
        client.put_object(Bucket=bucket, Key=key, Body=encoded(attempted), ContentType='application/json', **condition)
    except Exception:
        observed, _ = read_object(client, bucket, key)
        require(observed == attempted, 'progressive_pacing_write_unresolved')
    observed, version = read_object(client, bucket, key)
    require(observed == attempted, 'progressive_pacing_write_unresolved')
    result = submit()
    client.put_object(Bucket=bucket, Key=key, Body=encoded({**attempted, 'accepted_at': now()}), ContentType='application/json', IfMatch=version)
    return result


def upload_group(plan, group, directories, directory, client, bucket, uploader_args):
    import push_xhs_notes_to_wechat_drafts as uploader
    from recovered_article_delivery import guarded_add_draft
    directory.mkdir(parents=True, exist_ok=True)
    selected = [directories[source] for source in group['source_ids']]
    routes = {path: group['account'] for path in selected}
    original_checkpoint = uploader.checkpoint_wechat_drafts
    original_build = uploader.build_article
    original_metadata = uploader.xhs_article_title_metadata
    prepared_path = directory / 'progressive_prepared.json'
    prepared = read_json(prepared_path) if prepared_path.exists() else {'articles': {}, 'metadata': {}, 'audits': {}}
    by_path = {str(directories[source]): source for source in group['source_ids']}
    records = {row['source_id']: row for row in plan['sources']}
    def persist_prepared():
        write_json(prepared_path, prepared)
        write_json(directory / 'progressive_figures.json', prepared['audits'])
        save_group(plan, group, directory, client, bucket)
    def metadata(report):
        source = by_path[str(report)]
        if source not in prepared['metadata']:
            value = original_metadata(report)
            proof = {'source_id': source, 'content_sha256': records[source]['content_sha256'], 'metadata': value}
            prepared['metadata'][source] = {**proof, 'audit_sha256': digest(encoded(proof))}
            persist_prepared()
        return prepared['metadata'][source]['metadata']
    def build(report, *args, **kwargs):
        source = by_path[str(report)]
        if source not in prepared['articles']:
            article = original_build(report, *args, **kwargs)
            from wechat_image_quality import source_chart_images
            hashes = article.get('source_image_sha256')
            available = [digest(path.read_bytes()) for path in source_chart_images(report, require_verified=True)]
            require(isinstance(hashes, list) and article.get('source_image_count') == len(hashes)
                    and hashes == available[:len(hashes)], 'progressive_initial_figure_invalid')
            audit = {'source_id': source, 'content_sha256': records[source]['content_sha256'], 'source_image_sha256': hashes}
            prepared['audits'][source] = {**audit, 'audit_sha256': digest(encoded(audit))}
            prepared['articles'][source] = article
            # This precedes draft/add, even when the subsequent ACK checkpoint crashes.
            persist_prepared()
        return dict(prepared['articles'][source])
    def checkpoint(*args, **kwargs):
        original_checkpoint(*args, **kwargs)
        save_group(plan, group, directory, client, bucket)
    delay = api_draft_delay(uploader_args)
    def submit(session, token, articles, timeout, *, account):
        prefix = progressive_prefix(plan['source_run_id'], plan['date_folder'])
        return paced_submission(client, bucket, prefix, account, delay,
            lambda: guarded_add_draft(client, bucket, prefix, session, token, articles, timeout, account=account))
    argv = sys.argv
    uploader.checkpoint_wechat_drafts = checkpoint
    uploader.build_article = build
    uploader.xhs_article_title_metadata = metadata
    sys.argv = ['push_xhs_notes_to_wechat_drafts.py', *uploader_args,
                '--date-folder', plan['date_folder'], '--output-root', str(directory.parent),
                '--max-articles', 'all', '--expected-source-count', str(len(selected)), '--articles-per-draft', str(plan['articles_per_draft']), '--draft-delay-seconds', '0']
    try:
        require(uploader.main(submit_draft=submit, selected_reports=selected, planned_routes=routes, fixed_group=True, preserve_verified=True) == 0, 'progressive_group_upload_failed')
        save_group(plan, group, directory, client, bucket, complete=True)
    finally:
        sys.argv = argv
        uploader.checkpoint_wechat_drafts = original_checkpoint
        uploader.build_article = original_build
        uploader.xhs_article_title_metadata = original_metadata


def aggregate(plan, directories, output_dir, workspace):
    output_dir = Path(output_dir)
    output_dir.mkdir(parents=True, exist_ok=True)
    write_json(output_dir / 'progressive_plan.json', plan)
    drafts, articles, policies, completed = [], {}, {}, set()
    for group in plan['groups']:
        directory = group_directory(workspace, plan, group)
        marker = directory / 'progressive_group.json'
        summary_path = directory / 'wechat_draft_summary.json'
        if not marker.is_file() or not summary_path.is_file():
            continue
        state = read_json(marker)
        summary = read_json(summary_path)
        require(state['plan_sha256'] == plan['plan_sha256'], 'progressive_receipt_owner_changed')
        # Original runner paths can differ on a resumed/recovered worker.
        ordered = summary.get('articles', [])
        exclusions = summary.get('skipped_title_policy', [])
        old_names = {Path(str(row['report_dir'])).name for row in [*ordered, *exclusions]}
        source_by_name = {}
        for source in group['source_ids']:
            record = next(row for row in plan['sources'] if row['source_id'] == source)
            source_by_name[Path(record['report_relative']).name] = source
            if source in directories:
                source_by_name[directories[source].name] = source
        # Save each group's original identities before a recovery can rename dirs.
        binding_path = directory / 'progressive_sources.json'
        if binding_path.exists():
            source_by_name.update(read_json(binding_path))
        require(old_names.issubset(source_by_name), 'progressive_receipt_source_unbound')
        audits = read_json(directory / 'progressive_figures.json') if (directory / 'progressive_figures.json').exists() else {}
        frozen_metadata = read_json(directory / 'progressive_prepared.json').get('metadata', {}) if (directory / 'progressive_prepared.json').exists() else {}
        for row in ordered:
            source = source_by_name[Path(row['report_dir']).name]
            articles[source] = {**row, 'report_dir': str(directories[source]) if source in directories else row['report_dir'], 'progressive_source_id': source, 'progressive_initial_figure_audit': audits.get(source)}
        for row in exclusions:
            source = source_by_name[Path(row['report_dir']).name]
            report = directories.get(source, Path(row['report_dir']))
            policies[source] = {**row, 'report_dir': str(report), 'wechat_markdown': str(report / 'wechat_article.md'), 'progressive_source_id': source, 'progressive_policy_audit': frozen_metadata.get(source)}
        article_offset = 0
        for row in summary.get('drafts', []):
            report_dirs = row.get('report_dirs') or [item['report_dir'] for item in ordered[article_offset:article_offset + row['article_count']]]
            article_offset += row['article_count']
            sources = [source_by_name[Path(path).name] for path in report_dirs]
            payload_name = f"draft_payload_{group['group_id']}_{row['draft_index']:02d}.json"
            shutil.copyfile(directory / Path(row['payload']).name, output_dir / payload_name)
            drafts.append({**row, 'payload': str(output_dir / payload_name), 'progressive_source_ids': sources,
                           'progressive_group_id': group['group_id'], 'progressive_plan_sha256': plan['plan_sha256'],
                           'report_dirs': [str(directories[source]) if source in directories else path for source, path in zip(sources, report_dirs)]})
        if state.get('complete'):
            completed.update(group['source_ids'])
    selected = [row['source_id'] for row in plan['sources'] if row['selected']]
    summary = {'date_folder': plan['date_folder'], 'source': 'xhs_notes/dropbox', 'dry_run': False, 'publish': False,
               'status': 'verified' if set(selected) == completed else 'in_progress',
               'progressive_plan_sha256': plan['plan_sha256'], 'input_selected_count': len(selected),
               'expected_source_count': len(plan['sources']), 'source_report_count': len(directories),
               'selected_count': len(articles), 'draft_count': len(drafts), 'drafts': drafts,
               'articles': [articles[source] for source in selected if source in articles],
               'skipped_title_policy_count': len(policies), 'skipped_title_policy': [policies[source] for source in selected if source in policies],
               'skipped_generation_failure_count': 0, 'skipped_generation_failures': []}
    write_json(output_dir / 'wechat_draft_summary.json', summary)
    return summary


def upload_ready_groups(plan, source_dirs, output_dir, workspace, client, bucket, uploader_args):
    validate_plan(plan)
    output_dir = Path(output_dir)
    old_summary = output_dir / 'wechat_draft_summary.json'
    if old_summary.exists() and not (output_dir / 'progressive_plan.json').exists():
        require(not any(row.get('media_id') for row in read_json(old_summary).get('drafts', [])), 'progressive_legacy_receipt_requires_legacy_resume')
    for group in plan['groups']:
        directory = group_directory(workspace, plan, group)
        saved = restore_group(plan, group, directory, client, bucket)
        if not set(group['source_ids']).issubset(source_dirs):
            continue
        if saved.get('complete'):
            continue
        directory.mkdir(parents=True, exist_ok=True)
        binding_path = directory / 'progressive_sources.json'
        bindings = read_json(binding_path) if binding_path.exists() else {}
        for source in group['source_ids']:
            name = source_dirs[source].name
            require(name not in bindings or bindings[name] == source, 'progressive_source_basename_collision')
            bindings[name] = source
        write_json(binding_path, bindings)
        try:
            upload_group(plan, group, source_dirs, directory, client, bucket, uploader_args)
        finally:
            aggregate(plan, source_dirs, output_dir, workspace)
    return aggregate(plan, source_dirs, output_dir, workspace)


def validate_progressive_delivery(output_dir, plan, source_dirs=None, *, live=False):
    """Validate source-bound first acceptance, then read existing IDs without edits."""
    validate_plan(plan)
    output_dir = Path(output_dir)
    summary = read_json(output_dir / 'wechat_draft_summary.json')
    require(read_json(output_dir / 'progressive_plan.json') == plan, 'progressive_saved_plan_changed')
    require(summary.get('status') == 'verified' and summary.get('dry_run') is False and summary.get('publish') is False
            and summary.get('progressive_plan_sha256') == plan['plan_sha256'], 'progressive_delivery_incomplete')
    require(summary.get('source_report_count') == len(plan['sources']), 'progressive_source_inventory_incomplete')
    if source_dirs is not None:
        require(set(source_dirs) == {row['source_id'] for row in plan['sources']}, 'progressive_source_inventory_incomplete')
    selected = {row['source_id']: row for row in plan['sources'] if row['selected']}
    articles = summary.get('articles', [])
    policies = summary.get('skipped_title_policy', [])
    article_ids = [row.get('progressive_source_id') for row in articles]
    policy_ids = [row.get('progressive_source_id') for row in policies]
    require(len(article_ids + policy_ids) == len(set(article_ids + policy_ids))
            and set(article_ids + policy_ids) == set(selected), 'progressive_coverage_incomplete')
    require(summary.get('input_selected_count') == len(selected) and summary.get('selected_count') == len(articles)
            and summary.get('skipped_title_policy_count') == len(policies), 'progressive_count_mismatch')
    from verify_existing_wechat_drafts import load_drafts
    from push_portal_translated_to_wechat_drafts import draft_group_key
    drafts = load_drafts(output_dir) if articles else []
    rows = summary.get('drafts', [])
    require(len(drafts) == summary.get('draft_count') == len(rows), 'progressive_draft_count_mismatch')
    delivered, media_ids, presence = [], set(), []
    groups = {row['group_id']: row for row in plan['groups']}
    for row, payload in zip(rows, drafts):
        sources = row.get('progressive_source_ids', [])
        group = groups.get(row.get('progressive_group_id'))
        require(group and row.get('progressive_plan_sha256') == plan['plan_sha256']
                and 0 < len(sources) <= plan['articles_per_draft'] and set(sources).issubset(group['source_ids'])
                and all(selected[source]['account'] == row.get('account') for source in sources)
                and len(sources) == row.get('article_count') == len(payload['articles']), 'progressive_draft_source_mismatch')
        require(row.get('group_key') == draft_group_key(payload['articles'], account=row.get('account')),
                'progressive_payload_changed')
        identity = (row.get('account'), row.get('media_id'))
        require(identity not in media_ids and identity[1], 'progressive_media_duplicate')
        media_ids.add(identity)
        acceptance = row.get('draft_get', {})
        require(row.get('status') == 'verified' and all(acceptance.get(key) is True for key in
                ('ok', 'matches_editorial_contract', 'matches_expected_article_count', 'matches_expected_titles', 'matches_media_contract')),
                'progressive_initial_acceptance_missing')
        require(acceptance.get('article_count') == len(sources) and acceptance.get('expected_article_count') == len(sources), 'progressive_initial_count_changed')
        delivered.extend(sources)
    require(len(delivered) == len(set(delivered)) and set(delivered) == set(article_ids), 'progressive_payload_partition_mismatch')
    # The first strict acceptance remains immutable. Later edits are observed,
    # never replaced by the original generated payload or reported as unchanged.
    if live and not drafts:
        write_json(output_dir / 'progressive_presence.json', {'plan_sha256': plan['plan_sha256'], 'checked_at': datetime.now(timezone.utc).isoformat(), 'drafts': []})
    if live and drafts:
        import requests
        from wechat_accounts import draft_tokens, draft_account
        from push_portal_translated_to_wechat_drafts import get_stable_access_token, get_draft, draft_news_items, article_prose_text
        with requests.Session() as session:
            tokens = draft_tokens(session, drafts, 120, get_stable_access_token)
            for row, payload in zip(rows, drafts):
                current = draft_news_items(get_draft(session, tokens[draft_account(payload)], payload['media_id'], 120))
                require(len(current) == len(payload['articles']) and all(isinstance(item, dict)
                        and isinstance(item.get('title'), str) and item['title'].strip()
                        and isinstance(item.get('content'), str) and item['content'].strip() for item in current), 'progressive_existing_draft_missing_or_resized')
                edited = any(str(actual.get('title')) != str(original.get('title'))
                             or str(actual.get('author', '')) != str(original.get('author', ''))
                             or article_prose_text(actual.get('content')) != article_prose_text(original.get('content'))
                             for actual, original in zip(current, payload['articles']))
                presence.append({'account': row.get('account'), 'media_id': row['media_id'], 'article_count': len(current),
                                 'id_exists': True, 'editorial_changes_preserved': edited})
        write_json(output_dir / 'progressive_presence.json', {'plan_sha256': plan['plan_sha256'], 'checked_at': datetime.now(timezone.utc).isoformat(), 'drafts': presence})
    else:
        observed = read_json(output_dir / 'progressive_presence.json')
        require(observed.get('plan_sha256') == plan['plan_sha256'], 'progressive_presence_owner_changed')
        presence = observed.get('drafts', [])
    require(len(presence) == len(rows) and all(proof.get('id_exists') is True and proof.get('media_id') == row['media_id']
            and proof.get('account') == row.get('account') and proof.get('article_count') == row['article_count']
            for proof, row in zip(presence, rows)), 'progressive_presence_incomplete')
    image_verified = True
    for row in articles:
        source = selected[row['progressive_source_id']]
        report = Path(source_dirs[row['progressive_source_id']]) if source_dirs is not None else Path(row['report_dir'])
        status = read_json(report / 'status.json')
        require(status.get('original_pdf_sha256') == source['content_sha256'], 'progressive_final_source_changed')
        hashes = row.get('source_image_sha256')
        audit = row.get('progressive_initial_figure_audit') or {}
        valid_images = (isinstance(hashes, list) and row.get('source_image_count') == len(hashes)
                        and audit.get('source_id') == row['progressive_source_id']
                        and audit.get('content_sha256') == source['content_sha256']
                        and audit.get('source_image_sha256') == hashes
                        and audit.get('audit_sha256') == digest(encoded({key: value for key, value in audit.items() if key != 'audit_sha256'})))
        require(valid_images, 'progressive_initial_figure_audit_missing')
        image_verified = image_verified and valid_images
    from push_xhs_notes_to_wechat_drafts import xhs_article_title_metadata, hard_blocked_xhs_title_record
    for policy in policies:
        source_id = policy['progressive_source_id']
        report = Path(source_dirs[source_id]) if source_dirs is not None else Path(policy['report_dir'])
        require(read_json(report / 'status.json').get('original_pdf_sha256') == selected[source_id]['content_sha256'], 'progressive_policy_source_changed')
        audit = policy.get('progressive_policy_audit') or {}
        require(audit.get('source_id') == source_id and audit.get('content_sha256') == selected[source_id]['content_sha256']
                and audit.get('audit_sha256') == digest(encoded({key: value for key, value in audit.items() if key != 'audit_sha256'})), 'progressive_policy_evidence_missing')
        actual = hard_blocked_xhs_title_record(audit.get('metadata', {}))
        require(actual and all(policy.get(key) == actual.get(key) for key in ('skip_reason', 'hard_block_reason', 'matched_title', 'matched_title_field')), 'progressive_policy_unproven')
    result = {'ok': True, 'complete': True, 'delivery_complete': True, 'wechat_verified': True,
              'status': 'verified', 'verification_scope': 'progressive_accepted_source_and_live_identity',
              'article_count': len(articles), 'draft_count': len(rows), 'source_report_count': len(plan['sources']),
              'expected_count': len(plan['sources']), 'expected_article_count': len(articles),
              'verified_article_count': len(articles), 'verified_draft_count': len(rows),
              'policy_excluded_count': len(policies), 'institution_excluded_count': 0,
              'accounted_report_count': len(articles) + len(policies), 'figure_verification_complete': image_verified,
              'editorial_changes_preserved': any(row.get('editorial_changes_preserved') for row in presence),
              'progressive_plan_sha256': plan['plan_sha256']}
    if any(source['account'] is not None for source in selected.values()):
        result['verified_articles_by_account'] = {name: sum(selected[source]['account'] == account for source in article_ids) for account, name in ACCOUNT_NAMES.items()}
    write_json(output_dir / 'delivery_verification.json', result)
    return result


def validate_recovery_delivery(plan, article_root, output_dir):
    return validate_progressive_delivery(output_dir, plan, recovery_source_dirs(plan, article_root))


def resume_from_recovery(plan, article_root, output_dir, workspace, client, bucket, uploader_args=None):
    directories = recovery_source_dirs(plan, article_root)
    args = uploader_args or ['--dropbox-output-root', str(Path(article_root).parent), '--max-body-chars', '1200', '--min-inline-images', '3', '--max-inline-images', '3']
    # main() still expects its date-root to exist; the selected_reports override
    # supplies the authenticated recovery directories directly.
    date_root = Path(workspace) / '.progressive-input' / plan['date_folder']
    date_root.mkdir(parents=True, exist_ok=True)
    args = [*args, '--dropbox-output-root', str(date_root.parent)]
    with publisher_lease(plan, client, bucket):
        upload_ready_groups(plan, directories, output_dir, workspace, client, bucket, args)
        result = validate_progressive_delivery(output_dir, plan, directories, live=True)
        save_complete(plan, output_dir, client, bucket, directories)
        return result


def github_json(path):
    import requests
    repository = os.environ.get('GITHUB_REPOSITORY', '')
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository) and os.environ.get('GH_TOKEN'), 'progressive_lease_owner_unavailable')
    response = requests.get(f'https://api.github.com/repos/{repository}/{path}',
                            headers={'Authorization': 'Bearer ' + os.environ['GH_TOKEN'], 'Accept': 'application/vnd.github+json'},
                            timeout=30, allow_redirects=False)
    require(response.status_code == 200, 'progressive_lease_owner_unavailable')
    return response.json()


def owner_jobs(owner):
    result = []
    for page in range(1, 21):
        payload = github_json(f"actions/runs/{owner['run_id']}/attempts/{owner['run_attempt']}/jobs?per_page=100&page={page}")
        rows = payload.get('jobs')
        require(isinstance(rows, list) and all(str(row.get('run_id')) == owner['run_id'] for row in rows), 'progressive_owner_job_inventory_invalid')
        result.extend(rows)
        if len(result) == payload.get('total_count') and result:
            require(len({row['id'] for row in result}) == len(result), 'progressive_owner_job_inventory_invalid')
            return result
        require(len(rows) == 100 and len(result) < payload.get('total_count', 0), 'progressive_owner_job_inventory_invalid')
    raise ProgressiveError('progressive_owner_job_inventory_invalid')


def publisher_owner():
    owner = {'run_id': os.environ.get('GITHUB_RUN_ID', ''), 'run_attempt': int(os.environ.get('GITHUB_RUN_ATTEMPT', '1'))}
    require(re.fullmatch(r'[1-9][0-9]*', owner['run_id']), 'progressive_publisher_identity_missing')
    job = os.environ.get('GITHUB_JOB', '')
    require(job, 'progressive_publisher_job_missing')
    matches = [row for row in owner_jobs(owner) if row.get('name') == job or str(row.get('name', '')).endswith(' / ' + job)]
    require(len(matches) == 1 and matches[0].get('status') == 'in_progress', 'progressive_publisher_job_ambiguous')
    return {**owner, 'job_id': matches[0]['id'], 'job_name': matches[0]['name']}


def github_run_completed(owner):
    run = github_json(f"actions/runs/{owner['run_id']}")
    require(str(run.get('id')) == owner['run_id'] and run.get('head_repository', {}).get('full_name') == os.environ['GITHUB_REPOSITORY'], 'progressive_lease_owner_invalid')
    if run.get('status') == 'completed' or int(run.get('run_attempt', 0)) > owner['run_attempt']:
        return True
    if not owner.get('job_id'):
        return False
    matches = [row for row in owner_jobs(owner) if row.get('id') == owner['job_id'] and row.get('name') == owner['job_name']]
    require(len(matches) == 1, 'progressive_owner_job_missing')
    return matches[0].get('status') == 'completed'


@contextmanager
def publisher_lease(plan, client, bucket):
    key = progressive_prefix(plan['source_run_id'], plan['date_folder']) + '/publisher.json'
    previous, version = read_object(client, bucket, key)
    owner = publisher_owner()
    if previous and previous.get('state') == 'held':
        require(github_run_completed(previous['owner']), 'progressive_publisher_busy')
    lease = {'state': 'held', 'owner': owner, 'plan_sha256': plan['plan_sha256']}
    condition = {'IfMatch': version} if version else {'IfNoneMatch': '*'}
    client.put_object(Bucket=bucket, Key=key, Body=encoded(lease), ContentType='application/json', **condition)
    saved, lease_version = read_object(client, bucket, key)
    require(saved == lease, 'progressive_publisher_claim_unresolved')
    try:
        yield
    finally:
        client.put_object(Bucket=bucket, Key=key, Body=encoded({**lease, 'state': 'released'}),
                          ContentType='application/json', IfMatch=lease_version)


def save_complete(plan, output_dir, client, bucket, source_dirs):
    prefix = progressive_prefix(plan['source_run_id'], plan['date_folder'])
    require(set(source_dirs) == {row['source_id'] for row in plan['sources']}, 'progressive_completion_source_incomplete')
    # A later final retry must still support the normal source verifier/blog archive
    # after the producer's transient shard objects have been cleaned up.
    with tempfile.TemporaryDirectory(prefix='progressive-complete-') as temporary:
        source_root = Path(temporary)
        for source in plan['sources']:
            target = source_root / source['report_relative']
            shutil.copytree(source_dirs[source['source_id']], target)
            status = read_json(target / 'status.json')
            status.update(source_pdf=source['staged_name'], original_pdf_sha256=source['content_sha256'], wechat_article='wechat_article.md')
            write_json(target / 'status.json', status)
        upload_directory(source_root, prefix + '/sources.tar.gz', client=client, bucket=bucket)
    upload_directory(Path(output_dir), prefix + '/complete.tar.gz', client=client, bucket=bucket)
    marker = {'plan_sha256': plan['plan_sha256'], 'complete': True}
    client.put_object(Bucket=bucket, Key=prefix + '/complete.json', Body=encoded(marker), ContentType='application/json')


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--date-folder', required=True)
    parser.add_argument('--source-run-id', required=True)
    parser.add_argument('--source-sha', required=True)
    parser.add_argument('--shard-count', type=int, required=True)
    parser.add_argument('--reports-per-shard', type=int, required=True)
    parser.add_argument('--handoff-prefix', required=True)
    parser.add_argument('--workspace', type=Path, default=Path('.'))
    parser.add_argument('--dropbox-output-root', type=Path, default=Path('xhs_notes/dropbox'))
    parser.add_argument('--output-root', type=Path, default=Path('wechat_drafts/xhs_notes'))
    parser.add_argument('--expected-source-count', type=int, required=True)
    parser.add_argument('--articles-per-draft', type=int, default=3)
    parser.add_argument('--max-articles', default='all')
    parser.add_argument('--once', action='store_true')
    parser.add_argument('--plan-only', action='store_true')
    parser.add_argument('--complete-final', action='store_true')
    args, upload_args = parser.parse_known_args(argv)
    require('--publish' not in upload_args, 'progressive_freepublish_requires_legacy_mode')
    client, bucket = build_r2_client(), r2_bucket()
    plan = create_plan(args.manifest, args.source_run_id, args.date_folder, args.source_sha,
                       args.reports_per_shard, args.articles_per_draft, args.max_articles, client, bucket)
    require(len(plan['sources']) == args.expected_source_count, 'progressive_expected_count_changed')
    if args.plan_only:
        print(json.dumps({'state': 'plan_ready', 'plan_sha256': plan['plan_sha256']}))
        return 0
    output_dir = args.output_root / args.date_folder
    source_root = args.dropbox_output_root / args.date_folder
    prefix = progressive_prefix(args.source_run_id, args.date_folder)
    with publisher_lease(plan, client, bucket):
        complete, _version = read_object(client, bucket, prefix + '/complete.json')
        if complete is not None:
            require(complete == {'plan_sha256': plan['plan_sha256'], 'complete': True}, 'progressive_complete_owner_changed')
            download_directory(prefix + '/complete.tar.gz', output_dir, client=client, bucket=bucket)
            if args.complete_final:
                download_directory(prefix + '/sources.tar.gz', source_root, client=client, bucket=bucket)
                directories = source_directories(plan, source_root)
                # Remap runner-absolute paths from durable per-group receipts.
                for group in plan['groups']:
                    restore_group(plan, group, group_directory(args.workspace, plan, group), client, bucket)
                aggregate(plan, directories, output_dir, args.workspace)
                validate_progressive_delivery(output_dir, plan, directories, live=True)
            print(json.dumps({'state': 'already_complete', 'source_run_id': args.source_run_id}))
            return 0
        expected_prefix = f"_private-workflow-handoff/xhs/{args.source_run_id}/{args.date_folder}"
        require(args.handoff_prefix.rstrip('/') == expected_prefix, 'progressive_handoff_owner_invalid')
        for index in range(args.shard_count):
            key = args.handoff_prefix.rstrip('/') + f'/shard_{index}.tar.gz'
            try:
                download_directory(key, source_root / f'shard_{index}', client=client, bucket=bucket)
            except Exception as error:
                if str(getattr(error, 'response', {}).get('Error', {}).get('Code', '')) in {'NoSuchKey', '404', 'NotFound'}:
                    continue
                raise
        directories = restore_ready_sources(plan, source_root, client, bucket)
        uploader_args = ['--dropbox-output-root', str(args.dropbox_output_root), *upload_args]
        summary = upload_ready_groups(plan, directories, output_dir, args.workspace, client, bucket, uploader_args)
        if summary['status'] == 'verified' and len(directories) == len(plan['sources']):
            result = validate_progressive_delivery(output_dir, plan, directories, live=True)
            if args.complete_final:
                save_complete(plan, output_dir, client, bucket, directories)
            print(json.dumps({'state': 'complete', 'article_count': result['article_count'], 'draft_count': result['draft_count']}))
            return 0
        print(json.dumps({'state': 'partial', 'ready_source_count': len(directories), 'article_count': summary['selected_count'], 'draft_count': summary['draft_count']}))
        return 2 if args.complete_final else 0


if __name__ == '__main__':
    raise SystemExit(main())
