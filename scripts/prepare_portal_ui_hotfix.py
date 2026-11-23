#!/usr/bin/env python3
"""Prepare a UI-only inactive slot from an exact active release, without cutover.

The caller must hold portal-production-release throughout preparation and
cutover. Catalogs, translations, sitemaps and private English content retain
exactly their currently published bytes. Only approved assets, root HTML asset
versions, two exact analytics fixes, their bound locale asset descriptors, and
approved English ledger projections change.
"""
from __future__ import annotations

import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import sys
import time
from typing import Any, Callable

import publish_static_slot as publish
import portal_english_publication as english
from check_portal_app_budget import check_budget
from portal_extended_r2 import R2Store
from portal_english_ui import PUBLIC_ASSET_NAMES, bind_account_session, detail, homepage
from portal_locale_manifest import (
    FALLBACK_SHARD_DIRECTORY, MAX_LOCALE_MANIFEST_BYTES, locale_manifest_shard_descriptors,
    parse_locale_manifest, validate_translation_resolution,
)
from resume_portal_locale_candidate import live_state, read_pinned_manifest
from verify_prepared_static_slot import read_json_object, read_verified_candidate_body, static_tree_sha256
import verify_portal_locale_routes as locale_routes

ADDED_ASSETS = frozenset(('admin-report-refresh.js', 'admin-users.js'))
ASSETS = ADDED_ASSETS | frozenset(('app.js', 'account-services.js', 'newsfeed-app.js', 'styles.css', 'analytics.js', 'course-full.js', 'site-feedback.js', 'report-discussion.js', 'english-commentary.js'))
MAX_ASSET_BYTES = 2 * 1024 * 1024
MAX_HTML_BYTES = 8 * 1024 * 1024
WORKERS = 8
ANALYTICS_ROOT_PAGES = frozenset(('developer-api.html', 'activity.html'))
ACTIVITY_OPTIONS_BEFORE = '''
            <option value="">全部事件</option>
            <option value="page_view">页面访问</option>
            <option value="search">搜索</option>
            <option value="report_chat">研究问答（服务端）</option>
            <option value="report_chat_interaction">研究问答（交互）</option>
            <option value="course_material_request">KC桌面学堂索取</option>
            <option value="report_open">打开报告</option>
            <option value="download_attempt">尝试下载</option>
            <option value="download_success">下载成功</option>
            <option value="download_error">下载失败</option>
            <option value="download_pending">等待报告</option>
            <option value="delivery_link_generate">生成发货链接</option>
            <option value="account_auth">账号操作</option>
            <option value="admin_user_update">用户权限操作</option>
            <option value="daily_file_download">每日文件下载</option>
          '''
ACTIVITY_OPTIONS_AFTER = ACTIVITY_OPTIONS_BEFORE.replace(
    '<option value="report_open">打开报告</option>',
    '<option value="report_open">打开报告</option>\n'
    '            <option value="report_text_view">查看报告文本</option>',
).replace(
    '<option value="account_auth">账号操作</option>',
    '<option value="account_auth">账号操作</option>\n'
    '            <option value="membership_request">会员与权限申请</option>\n'
    '            <option value="report_request">报告申请</option>\n'
    '            <option value="newsfeed_interaction">Newsfeed 交互</option>\n'
    '            <option value="newsfeed_topic_request">Newsfeed 话题申请</option>\n'
    '            <option value="journey_interaction">阅读与表单交互</option>\n'
    '            <option value="form_confirmation">表单邮件确认</option>\n'
    '            <option value="reward_checkin">签到奖励</option>\n'
    '            <option value="reward_claim">领取奖励</option>',
)


def require(condition: Any, message: str) -> None:
    if not condition:
        raise RuntimeError(message)


def identity(value: dict[str, Any]) -> dict[str, str]:
    result = {key: value.get(key, '') for key in ('slot', 'release_id', 'tree_sha256')}
    publish.validate_slot(result['slot']); publish.validate_release(result['release_id'])
    require(publish.SHA256_PATTERN.fullmatch(result['tree_sha256']), 'Active tree identity is invalid')
    return result


def descriptor_with_body(descriptor: dict[str, Any], body: bytes) -> dict[str, Any]:
    return {**descriptor, 'size': len(body), 'sha256': hashlib.sha256(body).hexdigest()}


def metadata_matches(metadata: dict[str, Any], descriptor: dict[str, Any], release: str = '') -> bool:
    return (metadata.get('ContentLength') == descriptor['size']
            and (metadata.get('Metadata') or {}).get('sha256') == descriptor['sha256']
            and metadata.get('ContentType', '').lower() == descriptor['content_type'].lower()
            and metadata.get('CacheControl', '').lower() == descriptor['cache_control'].lower()
            and metadata.get('ContentEncoding', '') == descriptor.get('content_encoding', '')
            and (not release or (metadata.get('Metadata') or {}).get('release-id') == release))


def optional_head(client: Any, bucket: str, key: str) -> dict[str, Any] | None:
    try:
        return publish.head_object_with_retry(client, bucket, key)
    except Exception as error:
        if isinstance(error, KeyError) or publish.upload_error_code(error) in {'404', 'nosuchkey', 'notfound'}:
            return None
        raise


def source_head(client: Any, bucket: str, key: str, descriptor: dict[str, Any], release: str = '') -> dict[str, Any]:
    metadata = publish.head_object_with_retry(client, bucket, key)
    require(metadata_matches(metadata, descriptor, release), 'Pinned source object metadata differs')
    etag = metadata.get('ETag')
    require(isinstance(etag, str) and 0 < len(etag) <= 200 and not any(ord(c) < 32 for c in etag), 'Pinned source ETag is missing or invalid')
    require(0 <= descriptor['size'] <= 5 * 1024**3, 'Pinned object exceeds single-copy size bound')
    return metadata


def copy_verified(client: Any, bucket: str, source: str, target: str, descriptor: dict[str, Any], *, source_release: str = '', target_release: str = '', retry_sleep: Callable[[float], None] = time.sleep) -> str:
    current = optional_head(client, bucket, target)
    if current and metadata_matches(current, descriptor, target_release):
        # The destination already matches the pinned candidate descriptor.
        # Source validation is needed only when an object must be copied.
        return 'reused'
    if target_release:
        require(current is None, 'Immutable runtime object already exists with different metadata')
    source_metadata = source_head(client, bucket, source, descriptor, source_release)
    args = dict(Bucket=bucket, Key=target, CopySource={'Bucket': bucket, 'Key': source}, CopySourceIfMatch=source_metadata['ETag'], MetadataDirective='COPY')
    if target_release:
        args.update(publish.upload_extra_args(descriptor), MetadataDirective='REPLACE')
        args['Metadata']['release-id'] = target_release
    for attempt in range(len(publish.UPLOAD_RETRY_DELAYS_SECONDS) + 1):
        try:
            client.copy_object(**args)
            break
        except Exception as error:
            # Deterministic destination: verify an ambiguous response before
            # retrying the same conditional copy; never copy a changed source.
            current = optional_head(client, bucket, target)
            if current and metadata_matches(current, descriptor, target_release):
                return 'copied'
            if publish.upload_error_code(error) not in publish.RETRYABLE_HEAD_ERROR_CODES or attempt == len(publish.UPLOAD_RETRY_DELAYS_SECONDS):
                raise
            retry_sleep(publish.UPLOAD_RETRY_DELAYS_SECONDS[attempt])
    require(metadata_matches(publish.head_object_with_retry(client, bucket, target), descriptor, target_release), 'Copied object failed metadata readback')
    return 'copied'


def root_html_versions(body: bytes, files: dict[str, dict[str, Any]]) -> bytes:
    """Version approved scripts and stylesheets, preserving other HTML bytes."""
    source = body.decode('utf-8'); offsets = [0]
    for line in source.splitlines(keepends=True): offsets.append(offsets[-1] + len(line))
    replacements = []
    attribute = re.compile(r"\s+([A-Za-z_:][-\w:.]*)(?:\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+)))?")
    class Scripts(HTMLParser):
        def handle_starttag(self, tag, attrs):
            attr_name = 'src' if tag == 'script' else 'href' if tag == 'link' and 'stylesheet' in (dict(attrs).get('rel') or '').lower().split() else ''
            if not attr_name: return
            raw = self.get_starttag_text(); line, column = self.getpos(); start = offsets[line - 1] + column
            require(sum(name == attr_name for name, _ in attrs) <= 1, 'Ambiguous UI asset attributes')
            for match in attribute.finditer(raw):
                if match[1].lower() != attr_name: continue
                group = next((number for number in (2, 3, 4) if match[number] is not None), None)
                if group is None: continue
                value = match[group]
                path = re.fullmatch(r'(?:/|\./)?assets/([a-z0-9_.-]+\.(?:js|css))(?:\?v=[a-zA-Z0-9_.-]+)?', value)
                if path and path[1] in ASSETS:
                    replacement = value.split('?', 1)[0] + '?v=' + files['assets/' + path[1]]['sha256'][:12]
                    replacements.append((start + match.start(group), start + match.end(group), replacement))
        handle_startendtag = handle_starttag
    parser = Scripts(convert_charrefs=False); parser.feed(source); parser.close()
    for start, end, replacement in reversed(replacements): source = source[:start] + replacement + source[end:]
    return source.encode('utf-8')


def root_html_analytics_patch(relative: str, body: bytes) -> bytes:
    """Apply only the two approved analytics edits to verified live HTML bytes."""
    if relative not in ANALYTICS_ROOT_PAGES:
        return body
    source = body.decode('utf-8'); offsets = [0]
    for line in source.splitlines(keepends=True): offsets.append(offsets[-1] + len(line))
    bodies = []; selects = []; active_select = None
    attribute = re.compile(r"\s+([A-Za-z_:][-\w:.]*)(?:\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+)))?")

    class Targets(HTMLParser):
        def position(self):
            line, column = self.getpos()
            return offsets[line - 1] + column

        def handle_starttag(self, tag, attrs):
            nonlocal active_select
            raw = self.get_starttag_text(); start = self.position()
            if tag == 'body': bodies.append((start, raw, attrs))
            if tag == 'select' and active_select is not None:
                raise RuntimeError('Unexpected nested analytics event select')
            if any(name == 'id' and value == 'analyticsHistoryType' for name, value in attrs):
                require(tag == 'select' and sum(name == 'id' for name, _ in attrs) == 1,
                        'Ambiguous analytics event select')
                active_select = start + len(raw)

        def handle_endtag(self, tag):
            nonlocal active_select
            if tag == 'select' and active_select is not None:
                selects.append((active_select, self.position()))
                active_select = None

        def handle_startendtag(self, tag, attrs):
            require(tag not in {'body', 'select'}, 'Unexpected self-closing analytics HTML target')

    parser = Targets(convert_charrefs=False); parser.feed(source); parser.close()
    expected_page = 'developer-api' if relative == 'developer-api.html' else 'activity'
    require(len(bodies) == 1, 'Expected one analytics page body')
    start, raw, attrs = bodies[0]
    require(sum(name == 'data-page' for name, _ in attrs) == 1 and dict(attrs).get('data-page') == expected_page,
            'Unexpected analytics page identity')
    if relative == 'developer-api.html':
        flags = [value for name, value in attrs if name == 'data-analytics-auto']
        require(len(flags) <= 1 and (not flags or flags == ['manual']), 'Unexpected analytics automatic pageview flag')
        if not flags: return body
        matches = [match for match in attribute.finditer(raw) if match[1].lower() == 'data-analytics-auto']
        require(len(matches) == 1, 'Ambiguous analytics automatic pageview flag')
        match = matches[0]
        require(next((match[index] for index in (2, 3, 4) if match[index] is not None), '') == 'manual',
                'Unexpected analytics automatic pageview encoding')
        return (source[:start + match.start()] + source[start + match.end():]).encode('utf-8')
    require(active_select is None and len(selects) == 1, 'Expected one complete analytics event select')
    start, end = selects[0]
    options = source[start:end]
    require(options in {ACTIVITY_OPTIONS_BEFORE, ACTIVITY_OPTIONS_AFTER}, 'Unexpected analytics event options; live HTML retained')
    if options == ACTIVITY_OPTIONS_AFTER: return body
    return (source[:start] + ACTIVITY_OPTIONS_AFTER + source[end:]).encode('utf-8')


def patch_locale_asset_descriptors(client: Any, bucket: str, active: dict[str, str],
                                   old: dict[str, dict[str, Any]], files: dict[str, dict[str, Any]]) -> bytes | None:
    """Rebind only changed asset references; retain the original provenance encoding."""
    relative = 'data/i18n/manifest.json'
    if relative not in old:
        return None
    prefix = publish.slot_prefix(active['slot'])
    raw = read_verified_candidate_body(client, bucket, prefix + relative, old[relative], maximum=MAX_LOCALE_MANIFEST_BYTES)

    def matches(row: dict[str, Any], inventory: dict[str, dict[str, Any]]) -> bool:
        descriptor = inventory.get(row['path'])
        return bool(descriptor and type(row.get('byte_size')) is int
                    and row['byte_size'] == descriptor['size'] and row.get('sha256') == descriptor['sha256'])

    def checked(body: bytes, inventory: dict[str, dict[str, Any]]) -> dict[str, Any]:
        def shard(row: dict[str, Any]) -> bytes:
            require(matches(row, inventory), 'Locale source shard differs from pinned static manifest: ' + row['path'])
            return read_verified_candidate_body(client, bucket, prefix + row['path'], old[row['path']], maximum=MAX_LOCALE_MANIFEST_BYTES)
        manifest = parse_locale_manifest(body, shard_resolver=shard)
        validate_translation_resolution(manifest, locale_routes.LOCALES)
        declared_shards = {row['path'] for row in locale_manifest_shard_descriptors(manifest)}
        require(declared_shards == {path for path in inventory if path.startswith(FALLBACK_SHARD_DIRECTORY + '/')},
                'Locale source shard inventory differs from pinned manifest')
        for row in locale_routes.declared_checks(manifest) or []:
            require(matches(row, inventory), 'Locale route descriptor differs from pinned static manifest: ' + row['path'])
        return manifest

    # Validate the original graph before repairing any references. Never turn a
    # mismatched old descriptor into apparently verified candidate metadata.
    checked(raw, old)
    manifest = json.loads(raw.decode('utf-8'))
    changed_assets = {path for path, row in files.items() if path.startswith('assets/')
                      and any(row[field] != old.get(path, {}).get(field) for field in ('size', 'sha256'))}
    changed = False

    def rebind(value: Any) -> None:
        nonlocal changed
        if isinstance(value, list):
            for item in value: rebind(item)
        elif isinstance(value, dict):
            path = value.get('path')
            if isinstance(path, str) and path in changed_assets:
                require(matches(value, old), 'Changed locale asset descriptor differs from pinned static manifest: ' + path)
                value.update(byte_size=files[path]['size'], sha256=files[path]['sha256'])
                changed = True
            for item in value.values(): rebind(item)

    rebind(manifest)
    if not changed:
        return None
    # Serialize the original representation, not the parser's expanded fallback
    # records. Shard paths, coverage, translations and locale routes stay exact.
    body = (json.dumps(manifest, ensure_ascii=False, sort_keys=True, separators=(',', ':')) + '\n').encode('utf-8')
    checked(body, files)
    return body


def build_patch(client: Any, bucket: str, active: dict[str, str], manifest: dict[str, Any], source_root: Path, locale_assets: Path, store: R2Store) -> tuple[dict[str, bytes], dict[str, dict[str, Any]], dict[str, Any] | None]:
    old = manifest['files']; files = {path: dict(row) for path, row in old.items()}; bodies = {}
    require(ANALYTICS_ROOT_PAGES <= set(old), 'Required analytics root HTML is missing from the active release')
    for name in sorted(ASSETS):
        relative = 'assets/' + name
        require(relative in old or name in ADDED_ASSETS, 'UI hotfix cannot introduce an unapproved asset')
        root = locale_assets if name == 'english-commentary.js' else source_root / 'assets'
        path = root / name
        require(not root.is_symlink() and path.is_file() and not path.is_symlink() and 0 < path.stat().st_size <= MAX_ASSET_BYTES, 'Materialized UI asset is missing, linked or oversized')
        bodies[relative] = path.read_bytes()
        files[relative] = descriptor_with_body(old.get(relative) or publish.describe_file(path), bodies[relative])
    # The shared app has already been materialized for this deployment. Locale
    # assets arrive later and must use that exact account storage namespace.
    relative = 'assets/english-commentary.js'
    bodies[relative] = bind_account_session(bodies[relative], bodies['assets/app.js'])
    files[relative] = descriptor_with_body(old[relative], bodies[relative])
    # Bind lazy module URLs to the actual candidate, including retained assets.
    def lazy(match: re.Match[str]) -> str:
        relative = match[1].lstrip('/')
        require(relative in files, 'App references a missing lazy asset')
        return match[1] + '?v=' + files[relative]['sha256'][:12]
    app = re.sub(r'(/?assets/[a-z0-9_.-]+\.(?:js|css))\?v=[^\"\x27\s]+', lazy, bodies['assets/app.js'].decode('utf-8')).encode('utf-8')
    bodies['assets/app.js'] = app; files['assets/app.js'] = descriptor_with_body(old['assets/app.js'], app)
    active_app = read_verified_candidate_body(client, bucket, publish.slot_prefix(active['slot']) + 'assets/app.js', old['assets/app.js'], maximum=MAX_ASSET_BYTES)
    budget = check_budget(app, active_app)
    print(json.dumps({'phase': 'ui_app_budget', **budget}, sort_keys=True), flush=True)
    require(budget['status'] == 'passed', 'Materialized app exceeds loading budget')
    for relative in sorted(old):
        if '/' in relative or not relative.endswith('.html'):
            continue
        raw = read_verified_candidate_body(client, bucket, publish.slot_prefix(active['slot']) + relative, old[relative], maximum=MAX_HTML_BYTES)
        updated = root_html_versions(root_html_analytics_patch(relative, raw), files)
        if updated != raw:
            bodies[relative] = updated; files[relative] = descriptor_with_body(old[relative], updated)
    approved = english.read_active(store, active)
    if approved:
        ledger = english.read_ledger(store, approved['ledger_sha256'])
        hashes = {name: files['assets/' + name]['sha256'] for name in PUBLIC_ASSET_NAMES}
        previews = {'en/index.html': homepage(ledger['items'], approved=True, asset_hashes=hashes)}
        previews.update({f'en/blog/{row["id"]}.html': detail(row, approved=True, asset_hashes=hashes) for row in ledger['items']})
        assembly = {**approved, 'public_files': {key: dict(row) for key, row in approved['public_files'].items()}}
        for relative, raw in previews.items():
            require(relative in old, 'UI hotfix cannot introduce English pages')
            bodies[relative] = raw; files[relative] = descriptor_with_body(old[relative], raw)
            assembly['public_files'][relative] = {'sha256': files[relative]['sha256'], 'bytes': len(raw)}
        raw = english.stable_bytes(english.checked_assembly(assembly))
        bodies[english.ASSEMBLY] = raw; files[english.ASSEMBLY] = descriptor_with_body(old[english.ASSEMBLY], raw)
    locale_body = patch_locale_asset_descriptors(client, bucket, active, old, files)
    if locale_body is not None:
        relative = 'data/i18n/manifest.json'
        bodies[relative] = locale_body; files[relative] = descriptor_with_body(old[relative], locale_body)
    bodies = {key: body for key, body in bodies.items() if files[key] != old.get(key)}
    require(bool(bodies), 'UI hotfix has no changes')
    return bodies, files, approved


def prepare(client: Any, bucket: str, *, active_state: dict[str, Any], release: str, source_root: Path, locale_assets: Path, assert_active: Callable[[], None]) -> dict[str, Any]:
    active = identity(active_state); release = publish.validate_release(release)
    require(release != active['release_id'], 'UI hotfix requires a new release ID')
    assert_active()
    print('UI hotfix phase=validate_source', flush=True)
    original = read_pinned_manifest(client, bucket, active)
    store = R2Store(client, bucket, english.PREFIX)
    print('UI hotfix phase=build_ui_patch', flush=True)
    bodies, files, approved = build_patch(client, bucket, active, original, source_root, locale_assets, store)
    slot = publish.target_slot(active['slot']); prefix = publish.slot_prefix(slot)
    runtime = publish.valid_runtime_manifest(read_json_object(client, bucket, publish.runtime_manifest_key(active['release_id'])), active['release_id'])
    require(runtime is not None, 'Active immutable runtime manifest is invalid')
    require(original.get('runtime_data') == {key: runtime[key] for key in ('schema_version', 'release_id', 'prefix', 'tree_sha256')}, 'Active runtime binding differs')
    require(set(runtime['files']) == {Path(path).name for path in publish.DEFAULT_RUNTIME_PATHS}, 'Active runtime inventory differs')
    for relative in publish.DEFAULT_RUNTIME_PATHS:
        row = runtime['files'][Path(relative).name]
        require(all(row[key] == original['files'][relative][key] for key in ('sha256', 'size')), 'Active runtime and static catalog bytes differ')
    new_runtime = {**runtime, 'release_id': release, 'prefix': publish.runtime_release_prefix(release)}
    committed_runtime = read_json_object(client, bucket, publish.runtime_manifest_key(release))
    require(committed_runtime is None or committed_runtime == new_runtime, 'Runtime release is already committed differently')
    runtime_keys = set(publish.list_objects(client, bucket, new_runtime['prefix']))
    expected_runtime_keys = {new_runtime['prefix'] + name for name in runtime['files']} | {publish.runtime_manifest_key(release)}
    require(runtime_keys <= expected_runtime_keys, 'New immutable runtime has unexpected objects')
    assert_active()
    require(read_pinned_manifest(client, bucket, active) == original, 'Source manifest changed during preparation')
    publish.put_json(client, bucket, publish.incomplete_key(slot), {'schema_version': 1, 'slot': slot, 'release_id': release, 'source_release': active['release_id']})
    target_objects = publish.list_objects(client, bucket, prefix)
    def transfer(relative: str) -> str:
        source = publish.slot_prefix(active['slot']) + relative; target = prefix + relative
        if relative not in bodies:
            return copy_verified(client, bucket, source, target, files[relative])
        if relative in original['files']:
            source_head(client, bucket, source, original['files'][relative])
        else:
            require(relative.removeprefix('assets/') in ADDED_ASSETS, 'Unexpected added UI asset')
        current = optional_head(client, bucket, target)
        if current and metadata_matches(current, files[relative]):
            return 'reused'
        client.put_object(Bucket=bucket, Key=target, Body=bodies[relative], **publish.upload_extra_args(files[relative]))
        require(metadata_matches(publish.head_object_with_retry(client, bucket, target), files[relative]), 'Patched asset failed metadata readback')
        read_verified_candidate_body(client, bucket, target, files[relative], maximum=MAX_HTML_BYTES)
        return 'patched'
    progress = publish._PublishProgress('ui_hotfix_copy', files=len(files), workers=WORKERS)
    outcomes = []
    with ThreadPoolExecutor(max_workers=WORKERS) as executor:
        pending = {executor.submit(transfer, relative) for relative in sorted(files)}
        try:
            while pending:
                completed, pending = wait(pending, timeout=30, return_when=FIRST_COMPLETED)
                for future in completed:
                    outcomes.append(future.result())
                progress.update(len(outcomes))
        finally:
            for future in pending:
                future.cancel()
    progress.finish(files=len(outcomes))
    expected = {prefix + relative: row['size'] for relative, row in files.items()}
    publish.delete_keys(client, bucket, set(target_objects) - set(expected))
    require(publish.list_objects(client, bucket, prefix) == expected, 'Inactive slot inventory differs after verification')
    print('UI hotfix phase=clone_runtime', flush=True)
    for filename, row in runtime['files'].items():
        copy_verified(client, bucket, runtime['prefix'] + filename, new_runtime['prefix'] + filename, row, source_release=active['release_id'], target_release=release)
    publish.put_json(client, bucket, publish.runtime_manifest_key(release), new_runtime, Metadata={'tree-sha256': new_runtime['tree_sha256'], 'release-id': release})
    require(read_json_object(client, bucket, publish.runtime_manifest_key(release)) == new_runtime, 'Runtime manifest readback differs')
    assert_active()
    require(read_pinned_manifest(client, bucket, active) == original, 'Source manifest changed before commit')
    print('UI hotfix phase=commit_manifest', flush=True)
    tree = static_tree_sha256(files)
    candidate = {'schema_version': 1, 'slot': slot, 'release_id': release, 'tree_sha256': tree,
                 'file_count': len(files), 'total_bytes': sum(row['size'] for row in files.values()), 'files': files,
                 'runtime_data': {key: new_runtime[key] for key in ('schema_version', 'release_id', 'prefix', 'tree_sha256')}}
    publish.put_json(client, bucket, publish.manifest_key(slot), candidate, Metadata={'tree-sha256': tree, 'release-id': release})
    require(read_json_object(client, bucket, publish.manifest_key(slot)) == candidate, 'Static manifest readback differs')
    publish.delete_keys(client, bucket, [publish.incomplete_key(slot)])
    candidate_identity = {'slot': slot, 'release_id': release, 'tree_sha256': tree}
    require(read_pinned_manifest(client, bucket, candidate_identity) == candidate, 'Committed candidate differs')
    if approved:
        english.bind_release(store, candidate_identity, active)
    assert_active()
    return {'schema_version': 1, **candidate_identity, 'static_slot': slot, 'static_prefix': prefix,
            'previous': {'schema_version': 1, **active}, 'changed_files': {relative: files[relative] for relative in sorted(bodies)},
            'file_count': len(files), 'copied_files': outcomes.count('copied'), 'reused_files': outcomes.count('reused'),
            'patched_files': outcomes.count('patched'), 'deleted_files': len(set(target_objects) - set(expected)),
            'runtime_tree_sha256': runtime['tree_sha256'], 'english_ledger_sha256': approved['ledger_sha256'] if approved else '',
            'content_changed': False, 'deployed': False}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--active-state', required=True, type=Path)
    parser.add_argument('--live-origin', required=True)
    parser.add_argument('--release', required=True)
    parser.add_argument('--source-root', type=Path, default=Path('portal_suite/site_src'))
    parser.add_argument('--locale-assets', type=Path, default=Path('portal_suite/locale_assets'))
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--output-env', type=Path)
    args = parser.parse_args()
    expected = json.loads(args.active_state.read_text())
    active = identity(expected)
    def guard() -> None:
        require(identity(live_state(args.live_origin)) == active, 'Active release changed; hotfix preparation aborted')
    client, _ = publish.build_r2_client()
    receipt = prepare(client, publish.require_env('R2_BUCKET'), active_state=expected, release=args.release, source_root=args.source_root,
                      locale_assets=args.locale_assets, assert_active=guard)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, sort_keys=True, indent=2) + '\n')
    if args.output_env:
        publish.append_github_values(str(args.output_env), {'STATIC_SLOT': receipt['slot'], 'STATIC_RELEASE': receipt['release_id'],
            'STATIC_TREE_SHA256': receipt['tree_sha256'], 'STATIC_PREFIX': receipt['static_prefix']})
    print(json.dumps({key: value for key, value in receipt.items() if key != 'changed_files'}, sort_keys=True))
    return 0


if __name__ == '__main__':
    try:
        raise SystemExit(main())
    except Exception as error:
        # Provider exceptions can contain signed URLs or private R2 keys.
        print(json.dumps({'error': 'ui_hotfix_preparation_failed', 'error_class': type(error).__name__[:80]}), file=sys.stderr)
        raise SystemExit(1) from None
