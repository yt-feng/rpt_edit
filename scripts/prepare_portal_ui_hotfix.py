#!/usr/bin/env python3
"""Prepare a UI-only inactive slot from an exact active release, without cutover.

The caller must hold portal-production-release throughout preparation and
cutover. Catalogs, translations, sitemaps and private English content retain
exactly their currently published bytes. Only six assets, existing root HTML
script versions, and projections of the already approved English ledger change.
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
from portal_english_ui import PUBLIC_ASSET_NAMES, detail, homepage
from resume_portal_locale_candidate import live_state, read_pinned_manifest
from verify_prepared_static_slot import read_json_object, read_verified_candidate_body, static_tree_sha256

ASSETS = frozenset(('app.js', 'analytics.js', 'course-full.js', 'site-feedback.js', 'report-discussion.js', 'english-commentary.js'))
MAX_ASSET_BYTES = 2 * 1024 * 1024
MAX_HTML_BYTES = 8 * 1024 * 1024
WORKERS = 4


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
    source_metadata = source_head(client, bucket, source, descriptor, source_release)
    current = optional_head(client, bucket, target)
    if current and metadata_matches(current, descriptor, target_release):
        return 'reused'
    if target_release:
        require(current is None, 'Immutable runtime object already exists with different metadata')
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
    """Change actual script src values only, preserving all other HTML bytes."""
    source = body.decode('utf-8'); offsets = [0]
    for line in source.splitlines(keepends=True): offsets.append(offsets[-1] + len(line))
    replacements = []
    attribute = re.compile(r"\s+([A-Za-z_:][-\w:.]*)(?:\s*=\s*(?:\"([^\"]*)\"|'([^']*)'|([^\s>]+)))?")
    class Scripts(HTMLParser):
        def handle_starttag(self, tag, attrs):
            if tag != 'script': return
            raw = self.get_starttag_text(); line, column = self.getpos(); start = offsets[line - 1] + column
            require(sum(name == 'src' for name, _ in attrs) <= 1, 'Ambiguous script src attributes')
            for match in attribute.finditer(raw):
                if match[1].lower() != 'src': continue
                group = next((number for number in (2, 3, 4) if match[number] is not None), None)
                if group is None: continue
                value = match[group]
                path = re.fullmatch(r'(?:/|\./)?assets/([a-z0-9_.-]+\.js)(?:\?v=[a-zA-Z0-9_.-]+)?', value)
                if path and path[1] in ASSETS:
                    replacement = value.split('?', 1)[0] + '?v=' + files['assets/' + path[1]]['sha256'][:12]
                    replacements.append((start + match.start(group), start + match.end(group), replacement))
        handle_startendtag = handle_starttag
    parser = Scripts(convert_charrefs=False); parser.feed(source); parser.close()
    for start, end, replacement in reversed(replacements): source = source[:start] + replacement + source[end:]
    return source.encode('utf-8')


def build_patch(client: Any, bucket: str, active: dict[str, str], manifest: dict[str, Any], source_root: Path, locale_assets: Path, store: R2Store) -> tuple[dict[str, bytes], dict[str, dict[str, Any]], dict[str, Any] | None]:
    old = manifest['files']; files = {path: dict(row) for path, row in old.items()}; bodies = {}
    for name in sorted(ASSETS):
        relative = 'assets/' + name
        require(relative in old, 'UI hotfix cannot introduce a new asset')
        root = locale_assets if name == 'english-commentary.js' else source_root / 'assets'
        path = root / name
        require(not root.is_symlink() and path.is_file() and not path.is_symlink() and 0 < path.stat().st_size <= MAX_ASSET_BYTES, 'Materialized UI asset is missing, linked or oversized')
        bodies[relative] = path.read_bytes()
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
        updated = root_html_versions(raw, files)
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
    bodies = {key: body for key, body in bodies.items() if files[key] != old[key]}
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
        source_head(client, bucket, source, original['files'][relative])
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
