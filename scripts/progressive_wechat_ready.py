#!/usr/bin/env python3
"""Checkpoint one verified Daily article without waiting for its shard siblings.

This opt-in producer never sends WeChat requests. The short publisher still owns
the immutable full-manifest plan and every draft's durable delivery receipt.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import shutil
import tempfile

import requests

WORKFLOW = '.github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml'
CACHE = 'sensitive_content_guard_cache.json'


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def sha256(data):
    return hashlib.sha256(data).hexdigest()


def source_identity(pdf_path, item_dir, args, env):
    require(env.get('DAILY_PROGRESSIVE_WECHAT_READY') == 'true', 'ready_not_enabled')
    repository = env.get('GITHUB_REPOSITORY', '')
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'invalid_repository')
    require(env.get('GITHUB_ACTIONS') == 'true'
            and env.get('GITHUB_REF') == 'refs/heads/main'
            and env.get('GITHUB_WORKFLOW_REF') == f'{repository}/{WORKFLOW}@refs/heads/main'
            and env.get('GITHUB_EVENT_NAME') in {'schedule', 'workflow_dispatch'}, 'untrusted_producer')
    run, execution, day = env.get('GITHUB_RUN_ID', ''), env.get('GITHUB_SHA', ''), env.get('DATE_FOLDER', '')
    require(re.fullmatch(r'[1-9][0-9]*', run) and re.fullmatch(r'[a-f0-9]{40}', execution)
            and re.fullmatch(r'[0-9]{6}|[0-9]{8}', day), 'invalid_producer_identity')
    from wechat_account_routing import parse_source_date
    parse_source_date(day)
    manifest = Path(env['PROGRESSIVE_WECHAT_MANIFEST'])
    require(manifest.is_file() and not manifest.is_symlink() and pdf_path.is_file()
            and not pdf_path.is_symlink() and item_dir.is_dir() and not item_dir.is_symlink(), 'invalid_source_path')
    raw = manifest.read_bytes()
    rows = json.loads(raw)
    require(isinstance(rows, list) and rows, 'invalid_manifest')
    # The batch wrapper prefixes a temporary filename (0001-...). Its durable
    # source map is the authority for the selected, pre-staging basename.
    source_map = Path(args.mineru_source_map)
    require(source_map.is_file() and not source_map.is_symlink(), 'source_map_required')
    source_map_data = json.loads(source_map.read_bytes())
    require(source_map_data.get('schema') == 1 and isinstance(source_map_data.get('files'), dict), 'invalid_source_map')
    source = source_map_data['files'].get(pdf_path.name)
    pdf_bytes = pdf_path.read_bytes()
    require(isinstance(source, dict) and source.get('sha256') == sha256(pdf_bytes)
            and source.get('size') == len(pdf_bytes) and isinstance(source.get('source'), str)
            and source['source'] and Path(source['source']).name == source['source'], 'source_map_mismatch')
    matches = [row for row in rows if isinstance(row, dict)
               and Path(str(row.get('process_local_path', ''))).name == source['source']]
    require(len(matches) == 1, 'source_not_in_manifest')
    row = matches[0]
    source_pdf = source['source']
    content = row.get('content_sha256')
    require(isinstance(source_pdf, str) and source_pdf and Path(source_pdf).name == source_pdf
            and isinstance(content, str) and re.fullmatch(r'[a-f0-9]{64}', content)
            and source['sha256'] == content, 'original_pdf_mismatch')
    status = json.loads((item_dir / 'status.json').read_bytes())
    require(isinstance(status, dict) and not status.get('error')
            and status.get('wechat_article') == 'wechat_article.md'
            and Path(str(status.get('source_pdf', ''))).name == pdf_path.name
            and status.get('original_pdf_sha256') == content, 'source_status_mismatch')
    from wechat_editorial_binding import read_bound_article
    require(read_bound_article(item_dir) is not None, 'unbound_article')
    return {'schema_version': 1, 'source_run_id': run, 'source_execution_sha': execution,
            'date_folder': day, 'source_pdf': source_pdf, 'content_sha256': content,
            'manifest_sha256': sha256(raw)}


@contextlib.contextmanager
def finalize_environment(env):
    # Use the existing finalize billing stage, restoring generation's credentials
    # before processing the next report. Never log environment values.
    values = {'DEEPSEEK_API_KEY': env.get('PROGRESSIVE_WECHAT_FINALIZE_API_KEY', ''),
              'DEEPSEEK_API_KEY_BACKUP': '', 'DEEPSEEK_USAGE_STAGE': 'finalize'}
    before = {key: os.environ.get(key) for key in values}
    try:
        os.environ.update(values)
        yield
    finally:
        for key, value in before.items():
            if value is None:
                os.environ.pop(key, None)
            else:
                os.environ[key] = value


def prepare_article(stage, item, args):
    import finalize_outputs as finalize
    import postprocess_podcast as postprocess
    from wechat_editorial_binding import read_bound_article

    require(callable(finalize.run_sensitive_guard) and callable(finalize.build_sensitive_arg_parser),
            'guard_unavailable')
    post_args = postprocess.build_arg_parser().parse_args([
        '--output-dir', str(stage), '--generate-english-article', 'false',
        '--generate-podcast', 'false', '--generate-audio', 'false'])
    postprocess.process_item(item, post_args)
    require(read_bound_article(item) is not None, 'image_binding_failed')
    final_args = finalize.build_arg_parser().parse_args([
        '--output-dir', str(stage), '--model', args.model,
        '--deepseek-base-url', args.deepseek_base_url,
        '--generate-xianyu', 'false', '--generate-zhihu', 'false'])
    finalize.sanitize_output_dir(stage)
    require(finalize.normalize_wechat_articles(stage) >= 1, 'normalize_failed')
    require(read_bound_article(item) is not None, 'normalize_binding_failed')
    finalize.run_guard_if_enabled(stage, final_args)
    results = json.loads((stage / 'sensitive_content_guard_summary.json').read_bytes())
    article_results = [row for row in results if row.get('path') == str(item / 'wechat_article.md')]
    require(len(article_results) == 1 and not any(article_results[0].get(key)
            for key in ('error', 'api_errors', 'rewrite_error', 'skipped')), 'guard_failed')
    finalize.sanitize_output_dir(stage)
    require(read_bound_article(item) is not None, 'final_binding_failed')


def adopt_prepared_article(stage, prepared, original):
    """Only adopt fully verified edits; keep the shard guard's existing cache."""
    for name in ('wechat_article.md', 'status.json'):
        temporary = original / ('.progressive-' + name)
        temporary.write_bytes((prepared / name).read_bytes())
        temporary.replace(original / name)
    try:
        cache = json.loads((original.parent / CACHE).read_bytes())
    except (OSError, ValueError):
        cache = {}
    if not isinstance(cache, dict):
        cache = {}
    prepared_cache = json.loads((stage / CACHE).read_bytes())
    article_key = sha256(f'{original.name}/wechat_article.md'.encode())
    if article_key in prepared_cache:
        cache[article_key] = prepared_cache[article_key]
    temporary = original.parent / ('.progressive-' + CACHE)
    temporary.write_text(json.dumps(cache, sort_keys=True))
    temporary.replace(original.parent / CACHE)


def bounded_r2_client(env):
    import boto3
    from botocore.config import Config
    return boto3.client('s3', endpoint_url=f'https://{env["R2_ACCOUNT_ID"]}.r2.cloudflarestorage.com',
        aws_access_key_id=env['R2_ACCESS_KEY_ID'], aws_secret_access_key=env['R2_SECRET_ACCESS_KEY'],
        region_name='auto', config=Config(connect_timeout=5, read_timeout=20, retries={'max_attempts': 1}))


def notify_publisher(identity, env):
    # Exactly one POST. An unknown response is left for later article/shard
    # signals; the shared publisher plan makes such signals idempotent.
    repository = env.get('GITHUB_REPOSITORY', '')
    require(re.fullmatch(r'[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+', repository), 'invalid_repository')
    response = requests.post(
        f'https://api.github.com/repos/{repository}/actions/workflows/progressive-wechat-delivery.yml/dispatches',
        headers={'Authorization': 'Bearer ' + env['GH_TOKEN'], 'Accept': 'application/vnd.github+json',
                 'X-GitHub-Api-Version': '2022-11-28'},
        json={'ref': 'main', 'inputs': {'source_run_id': identity['source_run_id'],
                                      'date_folder': identity['date_folder']}},
        timeout=(5, 15), allow_redirects=False)
    require(response.status_code == 204, 'publisher_notification_unconfirmed')


def publish_ready(pdf_path, item_dir, args, *, env=None):
    env = os.environ if env is None else env
    identity = source_identity(pdf_path, item_dir, args, env)
    from private_workflow_handoff import upload_directory
    source_id = sha256((identity['source_pdf'] + '\0' + identity['content_sha256']).encode())
    key = (f'_private-workflow-handoff/xhs-ready/{identity["source_run_id"]}/'
           f'{identity["date_folder"]}/source_{source_id}.tar.gz')
    # Stage outside output_root: failed preparation must not become another
    # report discovered by the ordinary full-shard finalizer.
    with tempfile.TemporaryDirectory(prefix='progressive-wechat-ready-') as temporary:
        stage = Path(temporary)
        prepared = stage / item_dir.name
        require(not any(path.is_symlink() for path in item_dir.rglob('*')), 'source_symlink')
        shutil.copytree(item_dir, prepared)
        if (item_dir.parent / CACHE).is_file():
            shutil.copy2(item_dir.parent / CACHE, stage / CACHE)
        # Existing helpers sometimes print external error bodies. The optional
        # hook only emits its fixed completion/fallback status at the caller.
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()), finalize_environment(env):
            prepare_article(stage, prepared, args)
        require(source_identity(pdf_path, prepared, args, env) == identity, 'prepared_source_changed')
        (prepared / 'progressive_source.json').write_text(json.dumps(identity, sort_keys=True))
        adopt_prepared_article(stage, prepared, item_dir)
        upload_directory(prepared, key, client=bounded_r2_client(env), bucket=env['R2_BUCKET'])
    notify_publisher(identity, env)


def try_publish_ready(pdf_path, item_dir, args):
    """A checkpoint/notification failure never relabels successful generation."""
    if os.environ.get('DAILY_PROGRESSIVE_WECHAT_READY') != 'true':
        return
    try:
        publish_ready(pdf_path, item_dir, args)
        print('Progressive WeChat source ready: checkpoint verified; publisher notified.')
    except (Exception, SystemExit) as error:
        # Fixed class only; API response bodies, filenames and credentials do
        # not become workflow diagnostics from this optional notification.
        print(f'Progressive WeChat source ready: deferred ({type(error).__name__}); full-shard handoff retained.')
