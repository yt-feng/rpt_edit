#!/usr/bin/env python3
"""Restore the exact active Chinese source for an independent locale refresh.

Every source object is checked against the captured active manifest. Only the
three core languages' approved discovery additions are removed before the
normal Chinese parity snapshot; content and all other assets stay unchanged.
"""
from __future__ import annotations

import argparse
import base64
from datetime import datetime
import hashlib
import json
from pathlib import Path
import tempfile
from typing import Any
import xml.etree.ElementTree as ET
from zoneinfo import ZoneInfo

from build_portal_locales import remove_existing_locale_discovery
from portal_locale_history import plan_history_release
from portal_locale_manifest import MAX_LOCALE_MANIFEST_BYTES, load_locale_manifest, parse_locale_manifest, validate_translation_resolution
import publish_static_slot as publisher
from resume_portal_locale_candidate import bounded_results, download_candidate_object, write_local
from retain_published_core_locales import checked_manifest, descriptor, selected_paths as core_locale_paths
import verify_portal_chinese_parity as parity
from verify_prepared_static_slot import read_json_object, read_verified_candidate_body, require_complete_slot

CORE_MANIFEST = 'data/i18n/manifest.json'
HISTORY_LEDGER = 'data/i18n/history-release.json'
MAX_SOURCE_RECEIPT_BYTES = 64 * 1024 * 1024


class SourceRestoreError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise SourceRestoreError(message)


def selected_paths(files: dict[str, Any]) -> set[str]:
    excluded = core_locale_paths(files)
    for path in files:
        if (path.split('/', 1)[0] in parity.LOCALE_DIRS | {'en'}
            or path.startswith(('data/extended-locales/', 'data/english-commentary/'))
            or path in {'assets/extended-locales.js', 'assets/extended-locales.css',
                        'assets/english-commentary.js', 'assets/english-commentary.css',
                        'sitemap-extended.xml', 'sitemap-en.xml'}
            or path.startswith('sitemap-extended-') and path.endswith('.xml')):
            excluded.add(path)
    return set(files) - excluded


def indexed_canonicals(raw: bytes, locale: str, origin: str) -> list[str]:
    values = [str(node.text or '').strip() for node in ET.fromstring(raw).findall('.//{*}loc')]
    prefix = origin + '/' + locale + '/'
    require(len(set(values)) == len(values) and all(value.startswith(prefix) for value in values),
            'Published locale sitemap has an invalid URL inventory')
    return sorted(origin + '/' + value[len(prefix):] for value in values)


def read_core_policy(client: Any, bucket: str, manifest: dict[str, Any], origin: str) -> dict[str, Any]:
    files = manifest['files']; prefix = publisher.slot_prefix(manifest['slot'])
    def read(relative: str) -> bytes:
        require(relative in files, 'Active core locale policy object is missing')
        return read_verified_candidate_body(client, bucket, prefix + relative, files[relative], maximum=MAX_LOCALE_MANIFEST_BYTES)
    def shard(row: dict[str, Any]) -> bytes:
        descriptor = files.get(row['path']) or {}
        require(descriptor.get('sha256') == row['sha256'] and descriptor.get('size') == row['byte_size'],
                'Active locale source shard differs from the committed manifest')
        return read(row['path'])
    raw = read(CORE_MANIFEST)
    locale = parse_locale_manifest(raw, shard_resolver=shard)
    validate_translation_resolution(locale, parity.LOCALES)
    scope = locale.get('translation_scope'); policy = locale.get('index_policy')
    require(scope in {'incremental', 'release', 'month'} and isinstance(policy, dict)
            and type(policy.get('allowlist_count')) is int and policy['allowlist_count'] >= 0,
            'Published locale scope or index policy is invalid')
    incremental = scope == 'incremental'
    require(policy.get('mode') == ('incremental-publication-cutoff' if incremental else 'fixed-publication-cutoff')
            and policy.get('default') == ('new-content-and-core-hubs' if incremental else 'hubs-only'),
            'Published locale index policy does not match its scope')
    html = {code: sorted(path for path in files if path.startswith(code + '/') and path.endswith('.html'))
            for code in parity.LOCALES}
    require(type(locale.get('html_page_count')) is int and locale['html_page_count'] > 0
            and all(len(paths) == locale['html_page_count'] for paths in html.values()),
            'Published locale HTML inventory does not match its manifest')
    indexed = {code: indexed_canonicals(read(f'sitemap-{code}.xml'), code, origin) for code in parity.LOCALES}
    result = {'translation_scope': scope, 'index_policy': policy, 'html_paths': html,
              'indexed_canonicals': indexed, 'manifest_descriptor': files[CORE_MANIFEST]}
    history_policy = policy.get('history_release')
    if history_policy is None:
        require(HISTORY_LEDGER not in files, 'Published history ledger has no matching index policy')
        if incremental:
            require(policy.get('history_release_count') == 0 and policy['allowlist_count'] == 0,
                    'Incremental source contains historical publication policy')
        return result
    require(not incremental and isinstance(history_policy, dict) and policy['allowlist_count'] == 0,
            'Published history policy is inconsistent')
    history_raw = read(HISTORY_LEDGER); ledger = json.loads(history_raw)
    require(isinstance(ledger, dict) and ledger.get('launch_date') == policy.get('index_start_date')
            and ledger.get('history_start_date') == history_policy.get('history_start_date')
            and ledger.get('daily_limit') == history_policy.get('daily_limit'),
            'Published history ledger configuration differs from its index policy')
    paused = plan_history_release(
        dict.fromkeys(ledger.get('released', []), ledger['history_start_date']),
        history_start_date=ledger['history_start_date'], launch_date=ledger['launch_date'],
        today=datetime.now(ZoneInfo('Asia/Shanghai')).date().isoformat(), previous=ledger,
        daily_limit=ledger['daily_limit'], paused=True,
    )
    require(len(ledger['released']) == history_policy.get('released_count')
            and len(ledger['selected_today']) == history_policy.get('selected_today_count')
            and set(paused['released']) == set(ledger['released'])
            and all(set(ledger['released']) <= set(values) for values in indexed.values()),
            'Published history pages differ from their approved locale discovery')
    result['history'] = {'descriptor': files[HISTORY_LEDGER], 'body_b64': base64.b64encode(history_raw).decode('ascii')}
    return result


def source_receipt(path: Path) -> dict[str, Any]:
    require(path.is_file() and not path.is_symlink() and 0 < path.stat().st_size <= MAX_SOURCE_RECEIPT_BYTES,
            'Chinese source receipt is missing or oversized')
    result = json.loads(path.read_bytes())
    require(result.get('schema_version') == 1 and result.get('kind') == 'published-chinese-source'
            and isinstance(result.get('core_locales'), dict), 'Chinese source receipt is invalid')
    return result


def history_bytes(core: dict[str, Any]) -> bytes | None:
    if 'history' not in core:
        return None
    value = core['history']; raw = base64.b64decode(value['body_b64'], validate=True)
    require(0 < len(raw) <= MAX_LOCALE_MANIFEST_BYTES and len(raw) == value['descriptor']['size']
            and hashlib.sha256(raw).hexdigest() == value['descriptor']['sha256'], 'Pinned history ledger proof differs')
    return raw


def followup_configuration(receipt_path: Path, *, index_start_date: str, history_start_date: str,
                           allowlist_path: str = '') -> dict[str, Any]:
    from build_portal_locales import normalize_index_canonical, read_index_allowlist
    receipt = source_receipt(receipt_path); core = receipt['core_locales']; policy = core['index_policy']
    require((index_start_date or None) == policy.get('index_start_date'), 'Configured index start differs from published source')
    if allowlist_path:
        publisher.safe_relative_path(allowlist_path)
        candidate = Path(allowlist_path)
        require(candidate.is_file() and not candidate.is_symlink()
                and candidate.resolve().is_relative_to(Path.cwd().resolve()), 'Configured index allowlist is not a safe repository file')
    allowlist = {normalize_index_canonical(value, receipt['site_origin'])
                 for value in read_index_allowlist(Path(allowlist_path) if allowlist_path else None)}
    require(len(allowlist) == policy['allowlist_count']
            and all(allowlist <= set(values) for values in core['indexed_canonicals'].values()),
            'Configured index allowlist changes the published locale policy')
    result = {'translation_scope': 'incremental' if core['translation_scope'] == 'incremental' else 'release',
              'index_start_date': policy.get('index_start_date') or '', 'history_start_date': '',
              'history_daily_limit': 100, 'history_paused': False, 'history_state_in': ''}
    raw = history_bytes(core)
    if raw is not None:
        ledger = json.loads(raw)
        require(history_start_date == ledger['history_start_date'], 'Configured history start differs from published source')
        target = receipt_path.with_name(receipt_path.stem + '.history.json')
        write_local(target.parent, target.name, raw); target.chmod(0o600)
        result.update(history_start_date=ledger['history_start_date'], history_daily_limit=ledger['daily_limit'],
                      history_paused=True, history_state_in=str(target))
    return result


def validate_followup(root: Path, receipt_path: Path) -> None:
    receipt = source_receipt(receipt_path); core = receipt['core_locales']; before = core['index_policy']
    locale = load_locale_manifest(root / CORE_MANIFEST); validate_translation_resolution(locale, parity.LOCALES)
    after = locale['index_policy']
    scope = 'incremental' if core['translation_scope'] == 'incremental' else 'release'
    require(locale.get('translation_scope') == scope
            and all(after.get(key) == before.get(key) for key in ('mode', 'default', 'index_start_date', 'allowlist_count')),
            'Locale follow-up changed the published index policy')
    for code in parity.LOCALES:
        actual = {path.relative_to(root).as_posix() for path in (root/code).rglob('*.html') if path.is_file() and not path.is_symlink()}
        require(set(core['html_paths'][code]) <= actual, 'Locale follow-up dropped a published page')
        indexed = indexed_canonicals((root/f'sitemap-{code}.xml').read_bytes(), code, receipt['site_origin'])
        require(set(core['indexed_canonicals'][code]) <= set(indexed), 'Locale follow-up removed published discovery')
    raw = history_bytes(core)
    if raw is None:
        require('history_release' not in after and not (root/HISTORY_LEDGER).exists(),
                'Locale follow-up opened an unapproved historical release')
        return
    previous = json.loads(raw); current = json.loads((root/HISTORY_LEDGER).read_bytes())
    require(all(current.get(key) == previous.get(key) for key in
                ('history_start_date', 'launch_date', 'daily_limit', 'released', 'last_release_date'))
            and current.get('paused') is True and after.get('history_release', {}).get('paused') is True,
            'Locale follow-up changed the admitted history set or consumed a release day')


def normalize_discovery(relative: str, raw: bytes, origin: str) -> tuple[bytes, dict[str, Any] | None]:
    """Use the existing parity contract to prove the only permitted removals."""
    proof: dict[str, Any]
    if relative.endswith('.html') and not parity.is_site_verification_html(relative):
        old_head = parity._head(raw, relative=relative)
        new_head = remove_existing_locale_discovery(
            old_head.decode('utf-8'), hreflangs_to_remove=frozenset(parity.LOCALES),
        ).encode('utf-8')
        match = parity.HEAD_RE.search(raw)
        require(match is not None, 'Published Chinese HTML has no head')
        normalized = raw[:match.start()] + new_head + raw[match.end():]
        baseline = parity._validate_snapshot_head(normalized, relative=relative)
        parity._validate_final_head(raw, relative=relative, baseline=baseline, origin=origin)
        require(parity._body(raw, relative=relative) == parity._body(normalized, relative=relative)
                and parity._neutral_head(raw, relative=relative) == parity._neutral_head(normalized, relative=relative),
                'Chinese HTML changed beyond approved core locale discovery')
        proof = {'kind': 'core-locale-head-discovery',
                 'body_sha256': hashlib.sha256(parity._body(raw, relative=relative)).hexdigest(),
                 'neutral_head_sha256': hashlib.sha256(parity._neutral_head(raw, relative=relative)).hexdigest()}
    elif relative == 'robots.txt':
        if parity._robot_locale_lines(raw, relative=relative):
            parity._validate_final_robots(raw, origin=origin)
        normalized = parity._neutral_robots(raw, relative=relative)
        require(not parity._robot_locale_lines(normalized, relative=relative), 'Core locale robots entries remain')
        proof = {'kind': 'core-locale-robots-discovery', 'neutral_sha256': hashlib.sha256(normalized).hexdigest()}
    elif relative == 'sitemap.xml':
        if parity._sitemap_locale_blocks(raw, relative=relative):
            parity._validate_final_sitemap(raw, origin=origin)
        # Preserve every byte outside the exact controlled sitemap elements.
        allowed = {f'{origin}/sitemap-{code}.xml'.encode() for code in parity.LOCALES}
        def remove(match):
            locations = parity.SITEMAP_LOC_RE.findall(match.group(0))
            return b'' if len(locations) == 1 and locations[0].strip() in allowed else match.group(0)
        normalized = parity.SITEMAP_BLOCK_RE.sub(remove, raw)
        require(not parity._sitemap_locale_blocks(normalized, relative=relative)
                and parity._neutral_sitemap(raw, relative=relative) == parity._neutral_sitemap(normalized, relative=relative),
                'Chinese sitemap changed beyond approved core locale discovery')
        proof = {'kind': 'core-locale-sitemap-discovery',
                 'neutral_sha256': hashlib.sha256(parity._neutral_sitemap(raw, relative=relative)).hexdigest()}
    else:
        return raw, None
    if normalized == raw:
        return raw, None
    return normalized, {**proof, 'source_size': len(raw), 'source_sha256': hashlib.sha256(raw).hexdigest(),
                        'size': len(normalized), 'sha256': hashlib.sha256(normalized).hexdigest()}


def target_root(root: Path) -> Path:
    # Replacement is restricted to this task's generated site, never an
    # arbitrary directory supplied to a reusable download primitive.
    expected = Path.cwd().resolve() / '_neutral_site'
    absolute = root.parent.resolve() / root.name
    require(absolute == expected and not root.is_symlink(),
            'Chinese source restore may replace only the task _neutral_site directory')
    require(not root.exists() or root.is_dir(), 'Chinese source target is not a directory')
    if root.exists():
        require(not any(path.is_symlink() for path in root.rglob('*')), 'Chinese source target contains a symlink')
    return absolute


def restore(*, client: Any, bucket: str, active_state: dict[str, Any], active_manifest: dict[str, Any],
            root: Path, site_url: str, workers: int = 16) -> dict[str, Any]:
    root = target_root(root)
    origin = parity._normalize_origin(site_url)
    manifest = checked_manifest(active_manifest, active_state)
    files = manifest['files']
    require(all(type(row.get('size')) is int and row['size'] >= 0 for row in files.values())
            and manifest.get('total_bytes') == sum(row['size'] for row in files.values()),
            'Active manifest byte inventory is invalid')
    paths = selected_paths(files)
    require({'index.html', 'robots.txt', 'sitemap.xml', 'data/catalog.json', 'assets/app.js'} <= paths,
            'Active Chinese source is incomplete')
    require_complete_slot(client, bucket, manifest['slot'])
    current = read_json_object(client, bucket, publisher.manifest_key(manifest['slot']))
    require(checked_manifest(current, active_state) == manifest, 'Captured active manifest is no longer current')
    core_policy = read_core_policy(client, bucket, manifest, origin)
    prefix = publisher.slot_prefix(manifest['slot'])
    normalized: dict[str, Any] = {}
    source_files: dict[str, Any] = {}
    with tempfile.TemporaryDirectory(prefix='published-chinese-', dir=root.parent) as temporary:
        transaction = Path(temporary)
        staging = transaction / 'source'; staging.mkdir()
        def fetch(relative: str) -> str:
            download_candidate_object(client, bucket, prefix + relative, files[relative], staging, relative)
            return relative
        progress = publisher._PublishProgress('restore_published_chinese', objects=len(paths), workers=workers)
        for count, _relative in enumerate(bounded_results(sorted(paths), fetch, workers=workers), 1):
            progress.update(count)
        progress.finish(restored=len(paths))
        for relative in sorted(paths):
            path = staging / relative
            if relative.endswith('.html') or relative in {'robots.txt', 'sitemap.xml'}:
                raw = path.read_bytes()
                row = {'size': len(raw), 'sha256': hashlib.sha256(raw).hexdigest()}
                require(all(row[key] == files[relative][key] for key in row), 'Staged Chinese source changed before normalization')
                body, proof = normalize_discovery(relative, raw, origin)
                if proof is not None:
                    write_local(staging, relative, body)
                    normalized[relative] = proof
                    row = {'size': len(body), 'sha256': hashlib.sha256(body).hexdigest()}
            else:
                row = descriptor(path)
                require(all(row[key] == files[relative][key] for key in row), 'Staged Chinese source differs from active manifest')
            source_files[relative] = {**files[relative], **row}
        # A failed download, normalization, or source identity check leaves any
        # previously generated task tree intact. Only a complete staged tree moves.
        require_complete_slot(client, bucket, manifest['slot'])
        latest = read_json_object(client, bucket, publisher.manifest_key(manifest['slot']))
        require(checked_manifest(latest, active_state) == manifest, 'Active manifest changed during Chinese source restore')
        require_complete_slot(client, bucket, manifest['slot'])
        target_root(root)
        backup = transaction / 'previous'
        if root.exists():
            root.rename(backup)
        try:
            staging.rename(root)
        except BaseException:
            if backup.exists():
                backup.rename(root)
            raise
    return {'schema_version': 1, 'kind': 'published-chinese-source', 'source_state': active_state,
            'site_origin': origin, 'core_locales': core_policy,
            'source_tree_sha256': manifest['tree_sha256'], 'source_file_count': len(files),
            'files': source_files, 'file_count': len(source_files),
            'total_bytes': sum(row['size'] for row in source_files.values()),
            'normalized_files': normalized, 'provider_requests': 0, 'remote_mutations': 0}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root', type=Path, required=True)
    parser.add_argument('--active-state', type=Path, required=True)
    parser.add_argument('--active-manifest', type=Path, required=True)
    parser.add_argument('--site-url', required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.resolve().is_relative_to(args.root.resolve()), 'Source receipt must remain outside the public tree')
    from chart_search_r2 import client_and_bucket
    client, bucket = client_and_bucket()
    receipt = restore(client=client, bucket=bucket, active_state=json.loads(args.active_state.read_bytes()),
                      active_manifest=json.loads(args.active_manifest.read_bytes()), root=args.root, site_url=args.site_url)
    raw = publisher.json_bytes(receipt)
    require(len(raw) <= MAX_SOURCE_RECEIPT_BYTES, 'Chinese source receipt is oversized')
    write_local(args.output.parent, args.output.name, raw)
    args.output.chmod(0o600)
    print(json.dumps({'restored_files': receipt['file_count'], 'normalized_files': len(receipt['normalized_files']),
                      'provider_requests': 0, 'remote_mutations': 0}))
    print('chinese_locale_source_sha256=' + hashlib.sha256(raw).hexdigest())
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
