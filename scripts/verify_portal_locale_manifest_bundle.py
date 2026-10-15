#!/usr/bin/env python3
"""Read back an exact public locale root and all bound source shards."""
from __future__ import annotations

import argparse
import hashlib
import json
import math
from pathlib import Path
import re
import time
from typing import Callable

from fetch_release_asset import fetch_release_asset
from portal_locale_manifest import (
    MAX_LOCALE_MANIFEST_BYTES, read_locale_manifest_bundle, locale_manifest_shard_descriptors,
    parse_locale_manifest,
)
from verify_portal_locale_routes import validate_origin


def verify_bundle(manifest_path: Path, origin: str, output: Path, *,
                  release: str, tree: str, fetcher: Callable = fetch_release_asset,
                  total_timeout: float = 600, clock: Callable = time.monotonic) -> dict:
    origin = validate_origin(origin)
    if not re.fullmatch('[0-9a-f]{32}', release) or not re.fullmatch('[0-9a-f]{64}', tree):
        raise ValueError('Expected locale release identity is invalid')
    if not math.isfinite(total_timeout) or not 0 < total_timeout <= 600:
        raise ValueError('Locale bundle time budget is invalid')
    deadline = clock() + total_timeout
    expected_root, manifest = read_locale_manifest_bundle(manifest_path)
    descriptors = locale_manifest_shard_descriptors(manifest)
    output.mkdir(parents=True, exist_ok=True)
    if not 0 < len(expected_root) <= MAX_LOCALE_MANIFEST_BYTES:
        raise ValueError('Expected locale root exceeds its byte bound')
    root_sha = hashlib.sha256(expected_root).hexdigest()

    def get(relative: str, destination: Path, size: int | None = None, sha256: str | None = None) -> bytes:
        remaining = deadline - clock()
        if remaining <= 0:
            raise ValueError('Locale bundle time budget exhausted')
        maximum = MAX_LOCALE_MANIFEST_BYTES if size is not None else 64 * 1024
        fetcher(origin + '/' + relative, destination, label='public locale bundle',
                expected_bytes=size, expect_sha256=sha256, max_bytes=maximum,
                retry_404=True, max_time=min(180, remaining), max_total_time=min(420, remaining))
        if clock() > deadline:
            raise ValueError('Locale bundle time budget exhausted')
        # Recheck even custom fetchers: returned evidence must be exact bytes.
        with destination.open('rb') as handle:
            body = handle.read((size if size is not None else maximum) + 1)
        if len(body) > maximum or (size is not None and
                                  (len(body) != size or hashlib.sha256(body).hexdigest() != sha256)):
            raise ValueError('Public locale bundle differs from the prepared release')
        return body

    def read_state(label: str) -> dict:
        state = json.loads(get('.well-known/edge-state', output / (label + '-state.json')))
        if (not isinstance(state, dict) or set(state) != {'schema_version', 'slot', 'release_id', 'tree_sha256'}
                or type(state['schema_version']) is not int or state['schema_version'] != 1
                or state['slot'] not in {'a', 'b'} or state['release_id'] != release or state['tree_sha256'] != tree):
            raise ValueError('Public locale release changed during verification')
        return state

    state = read_state('before')
    for label, prefix in [('immutable', '.well-known/edge-release/' + release + '/'), ('public', '')]:
        root = get(prefix + 'data/i18n/manifest.json', output / (label + '-root-before.json'), len(expected_root), root_sha)
        def resolve(row: dict) -> bytes:
            # The codec checks the exact fixed namespace before invoking this callback.
            return get(prefix + row['path'], output / (label + '-' + Path(row['path']).name), row['byte_size'], row['sha256'])
        parse_locale_manifest(root, shard_resolver=resolve)
        get(prefix + 'data/i18n/manifest.json', output / (label + '-root-after.json'), len(expected_root), root_sha)
    if read_state('after') != state:
        raise ValueError('Public locale release changed during verification')
    counts = dict((manifest.get('source_fallbacks') or {}).get('counts') or {})
    return {'status': 'passed', 'release_id': release, 'tree_sha256': tree,
            'root_sha256': root_sha, 'source_shards_verified_per_namespace': len(descriptors),
            'source_unit_count': manifest.get('source_unit_count'), 'source_fallback_counts': counts,
            'source_fallback_references': sum(counts.values()),
            'source_shard_wire_bytes': sum(row['byte_size'] for row in descriptors),
            'max_source_shard_wire_bytes': max((row['byte_size'] for row in descriptors), default=0)}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--manifest', type=Path, required=True)
    parser.add_argument('--origin', required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--release', required=True)
    parser.add_argument('--tree', required=True)
    args = parser.parse_args()
    result = verify_bundle(args.manifest, args.origin, args.output, release=args.release, tree=args.tree)
    body = json.dumps(result, sort_keys=True) + '\n'
    (args.output / 'verification.json').write_text(body)
    print(body, end='')


if __name__ == '__main__':
    main()
