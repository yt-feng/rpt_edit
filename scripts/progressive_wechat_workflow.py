#!/usr/bin/env python3
"""Carry immutable Daily publishing options into short ready-group uploads."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import subprocess
import sys

OPTIONS = {
    'translated_report_count': '--max-articles',
    'wechat_draft_articles_per_draft': '--articles-per-draft',
    'wechat_draft_max_body_chars': '--max-body-chars',
    'wechat_draft_min_inline_images': '--min-inline-images',
    'wechat_draft_max_inline_images': '--max-inline-images',
}


def require(condition, reason):
    if not condition:
        raise ValueError(reason)


def validate(config, env):
    require(isinstance(config, dict) and config.get('schema_version') == 1, 'invalid_config')
    for key, name in (('source_run_id', 'SOURCE_RUN_ID'), ('source_sha', 'SOURCE_SHA'),
                      ('date_folder', 'DATE_FOLDER'), ('repository', 'GITHUB_REPOSITORY')):
        require(config.get(key) == env.get(name), 'producer_config_identity_mismatch')
    require(re.fullmatch(r'[1-9][0-9]*', config['source_run_id'])
            and re.fullmatch(r'[a-f0-9]{40}', config['source_sha'])
            and re.fullmatch(r'[0-9]{6}|[0-9]{8}', config['date_folder']), 'invalid_producer_identity')
    for key in ('shard_count', 'reports_per_shard', 'selected_count'):
        require(type(config.get(key)) is int and 0 < config[key] <= 10000, 'invalid_source_counts')
    options = config.get('options')
    require(isinstance(options, dict), 'invalid_publishing_options')
    count = str(options.get('translated_report_count', ''))
    require(count == 'all' or re.fullmatch(r'[0-9]+', count), 'invalid_article_count')
    require(all(re.fullmatch(r'[0-9]+', str(options.get(key, '')))
                for key in OPTIONS if key != 'translated_report_count'), 'invalid_publishing_options')
    require(1 <= int(options['wechat_draft_articles_per_draft']) <= 9, 'invalid_group_size')
    require(int(options['wechat_draft_max_body_chars']) >= 200, 'invalid_body_limit')
    require(int(options['wechat_draft_min_inline_images']) >= 0 and int(options['wechat_draft_max_inline_images']) >= 0,
            'invalid_image_limits')
    require(options.get('wechat_freepublish') in {'true', 'false'}, 'invalid_publish_option')
    require(type(config.get('enabled')) is bool, 'invalid_enabled_option')
    require(not config['enabled'] or options['wechat_freepublish'] == 'false', 'progressive_requires_drafts')
    return config


def freeze(env):
    options = json.loads(env['PUBLISHING_OPTIONS_JSON'])
    config = {
        'schema_version': 1, 'source_run_id': env['GITHUB_RUN_ID'], 'source_sha': env['GITHUB_SHA'],
        'repository': env['GITHUB_REPOSITORY'], 'date_folder': env['DATE_FOLDER'],
        'shard_count': int(env['SHARD_COUNT']), 'reports_per_shard': int(options['reports_per_shard']),
        'selected_count': int(env['SELECTED_COUNT']),
        'enabled': (options['wechat_draft_upload'] == 'true' and options['wechat_draft_source'] == 'xhs_notes'
                    and options['wechat_freepublish'] == 'false'),
        'options': {key: options[key] for key in (*OPTIONS, 'wechat_freepublish')},
    }
    # Empty selections are an ordinary no-work result and cannot dispatch.
    if config['selected_count']:
        validate(config, {**env, 'SOURCE_RUN_ID': env['GITHUB_RUN_ID'], 'SOURCE_SHA': env['GITHUB_SHA']})
    Path('_progressive_wechat_config.json').write_text(json.dumps(config, sort_keys=True) + '\n')


def once_command(config, env, manifest, *, plan_only=False):
    config = validate(config, env)
    if not config['enabled']:
        return None
    day = config['date_folder']
    command = [sys.executable, 'scripts/progressive_wechat_delivery.py', '--plan-only' if plan_only else '--once',
        '--manifest', str(manifest), '--date-folder', day, '--source-run-id', config['source_run_id'],
        '--source-sha', config['source_sha'], '--shard-count', str(config['shard_count']),
        '--reports-per-shard', str(config['reports_per_shard']),
        '--handoff-prefix', f'_private-workflow-handoff/xhs/{config["source_run_id"]}/{day}',
        '--workspace', '.', '--dropbox-output-root', 'xhs_notes/dropbox',
        '--output-root', 'wechat_drafts/xhs_notes', '--expected-source-count', str(config['selected_count'])]
    for key, flag in OPTIONS.items():
        value = str(config['options'][key])
        command.extend((flag, 'all' if key == 'translated_report_count' and value == '0' else value))
    if config['options']['wechat_freepublish'] == 'true':
        command.append('--publish')
    return command


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('operation', choices=('freeze', 'once', 'plan'))
    parser.add_argument('--config', default='_progressive_wechat_config.json')
    parser.add_argument('--manifest', default='_selected_macro_manifest/selected_to_process_manifest.json')
    args = parser.parse_args()
    if args.operation == 'freeze':
        freeze(os.environ)
        return 0
    command = once_command(json.loads(Path(args.config).read_text()), os.environ, args.manifest,
                           plan_only=args.operation == 'plan')
    if command is None:
        print('Progressive WeChat upload is disabled by the source Daily run.')
        return 0
    return subprocess.run(command, check=False).returncode


if __name__ == '__main__':
    raise SystemExit(main())
