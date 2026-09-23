#!/usr/bin/env python3
"""Prepare resumable, offline-only global locale candidates from public sources.

This is an isolated preparation lane, not a production publisher. Existing
Chinese/ko/ja/ar releases, private profiles, R2 objects and search submissions
are never changed. A candidate can be complete without being production-ready.
"""
from __future__ import annotations
import argparse
from datetime import date, datetime, timezone
import hashlib
import json
from pathlib import Path
import shutil
import subprocess
import sys
from urllib.parse import urlsplit

from portal_language_registry import selected_locales, manifest_locales, MIRROR_CODES
from offline_translation import MODEL_ID, atomic_json
import build_portal_locales as builder
import verify_portal_chinese_parity as parity
from portal_locale_manifest import load_locale_manifest, validate_translation_resolution

ROOT = Path(__file__).resolve().parents[1]
MAX_CACHE_BYTES = 8 * 1024 * 1024
MAX_CANDIDATE_BYTES = 2 * 1024 * 1024 * 1024


def public_origin(value: str) -> str:
    parts = urlsplit(value)
    if (parts.scheme != 'https' or not parts.hostname or parts.username or parts.password
            or parts.port or parts.path not in ('','/') or parts.query or parts.fragment):
        raise ValueError('A canonical HTTPS origin without credentials, port or path is required')
    return value.rstrip('/')


def source_identity(root: Path) -> str:
    digest = hashlib.sha256()
    total = 0
    for path in sorted(root.rglob('*')):
        if path.is_symlink():
            raise ValueError('Candidate input must not contain symlinks')
        if not path.is_file(): continue
        total += path.stat().st_size
        if total > MAX_CANDIDATE_BYTES: raise ValueError('Candidate input exceeds the preparation size bound')
        digest.update(path.relative_to(root).as_posix().encode() + b'\0')
        digest.update(hashlib.sha256(path.read_bytes()).digest())
    if not (root/'index.html').is_file(): raise ValueError('Candidate Chinese homepage is missing')
    return digest.hexdigest()


def build_public_source(output: Path, site_url: str) -> dict:
    """Reuse the production generator with public repository inputs only."""
    site_url = public_origin(site_url)
    if output.exists(): raise ValueError('Source output must be a new directory')
    scratch = output.parent / (output.name + '-inputs')
    scratch.mkdir(parents=True, exist_ok=False)
    for name in ('catalog.json','archive_catalog.json','search_index.json'):
        source = ROOT/'portal_suite/data'/name
        if source.is_file(): shutil.copyfile(source, scratch/name)
        else: (scratch/name).write_text('{"items":[]}')
    # Set only the public generator's canonical origin, not any private profile.
    command = [sys.executable, '-B', '-c',
               'import sys; sys.path.insert(0,"scripts"); import build_portal_suite_site as b; '
               'from portal_global_build_support import cache_metadata_normalization; '
               'cache_metadata_normalization(b); '
               'b.SITE_BASE_URL=sys.argv.pop(1); raise SystemExit(b.main())', site_url,
               '--site-src','portal_suite/site_src','--output-dir',str(output),
               '--catalog-path',str(scratch/'catalog.json'),
               '--archive-catalog-path',str(scratch/'archive_catalog.json'),
               '--search-index-path',str(scratch/'search_index.json'),
               '--wechat-drafts-root',str(scratch/'no-private-drafts')]
    subprocess.run(command, cwd=ROOT, check=True, timeout=900)
    # The separate private chart/Hot overlay is intentionally not retrieved.
    # Explicitly mark this as a public-source candidate, not production parity.
    if not (output/'data/chart_search_index.json').exists():
        atomic_json(output/'data/chart_search_index.json', {'schema_version':1, 'items':[]})
    if not (output/'data/hot_reports.json').exists():
        atomic_json(output/'data/hot_reports.json',
                    {'version':builder.HOT_REPORT_PUBLIC_INDEX_VERSION, 'items':[],
                     'generation':hashlib.sha256(b'public-only-empty-hot-projection').hexdigest()[:16],
                     'updated_at':datetime.now(timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')})
    result = {'schema_version':1, 'source_kind':'public-repository-projection',
              'site_url':site_url, 'source_sha256':source_identity(output),
              'private_chart_and_hot_overlays':'not_loaded', 'production_ready':False}
    atomic_json(output.parent/'public-source-manifest.json',result)
    return result


def prepare(source: Path, output: Path, cache: Path, targets: str, site_url: str,
            cutoff: str, budget: int) -> dict:
    codes = selected_locales(targets)
    date.fromisoformat(cutoff)
    if not 30 <= budget <= 1200: raise ValueError('Translation budget must be between 30 and 1200 seconds')
    site_url = public_origin(site_url)
    if source.resolve() == output.resolve() or source.resolve() in output.resolve().parents:
        raise ValueError("Candidate output must be isolated from the source")
    if source.resolve() == cache.resolve() or source.resolve() in cache.resolve().parents:
        raise ValueError("Translation cache must not mutate the source")
    identity = source_identity(source)
    if output.exists(): raise ValueError('Candidate output must be a new directory')
    if any((source/code).exists() for code in MIRROR_CODES):
        raise ValueError('Source must be a pre-localization Chinese tree')
    if cache.exists() and (cache.is_symlink() or cache.stat().st_size > MAX_CACHE_BYTES):
        raise ValueError('Translation checkpoint exceeds its storage bound')
    shutil.copytree(source, output)
    original_codes = parity.LOCALES
    try:
        parity.configure_locale_targets(codes)
        snapshot = output.parent/'chinese-parity-before.json'
        atomic_json(snapshot, parity.create_snapshot(root=output, site_origin=site_url))
        result = builder.build_localized_release(
            root=output, locales=codes, site_url=site_url,
            cache_in=cache if cache.exists() else None,
            cache_out=cache, assets_root=ROOT/'portal_suite/locale_assets',
            provider='hymt', workers=1, model=MODEL_ID,
            deepseek_base_url='https://paid-provider.invalid', timeout=180, attempts=2,
            hot_report_index_path=output/'data/hot_reports.json',
            index_start_date=cutoff, translation_scope='incremental',
            offline_time_budget_seconds=budget, allow_source_fallback=False,
            checkpoint_on_budget=True, diagnostics_out=output.parent/'translation-diagnostics.json')
        complete = result.get('ready', result.get('status') == 'passed')
        if (output/'data/i18n/manifest.json').exists():
            manifest = load_locale_manifest(output/'data/i18n/manifest.json')
            if manifest_locales(manifest) != codes: raise ValueError('Candidate locale set differs')
            validate_translation_resolution(manifest,codes)
            parity.verify_snapshot(root=output, snapshot_path=snapshot, site_origin=site_url, locale_build_complete=True)
            complete = True
        else:
            parity.verify_snapshot(root=output, snapshot_path=snapshot, site_origin=site_url, locale_build_complete=False)
            complete = False
        return {'schema_version':1, 'status':'candidate-complete' if complete else 'checkpointed',
                'source_kind':'public-repository-projection','source_sha256':identity,
                'targets':list(codes),'model':MODEL_ID,'provider':'hymt',
                'candidate_complete':complete,'production_ready':False,
                'paid_provider_requests':0, 'index_start_date':cutoff,
                'stop_reason':result.get('stop_reason'),
                'publication_gate':'existing production profile, full acceptance and semantic review required'}
    finally:
        parity.configure_locale_targets(original_codes)
        if cache.exists() and cache.stat().st_size > MAX_CACHE_BYTES:
            # Do not save unbounded new caches into the hosted cache service.
            cache.unlink()
            raise ValueError('Translation checkpoint exceeded 8 MiB and was not retained')


def main() -> int:
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--build-source', action='store_true')
    parser.add_argument('--source-root',type=Path)
    parser.add_argument('--output-root',type=Path,required=True)
    parser.add_argument('--cache',type=Path)
    parser.add_argument('--targets',default='new')
    parser.add_argument('--site-url',default='https://kcdesk.com')
    parser.add_argument('--index-start-date',default='2026-09-23')
    parser.add_argument('--budget-seconds',type=int,default=300)
    args=parser.parse_args()
    from compare_hymt_translation import require_actions
    require_actions()
    if args.build_source:
        result=build_public_source(args.output_root,args.site_url)
    else:
        if args.source_root is None or args.cache is None: parser.error('source-root and cache are required')
        try:
            result=prepare(args.source_root,args.output_root,args.cache,args.targets,args.site_url,
                           args.index_start_date,args.budget_seconds)
        except Exception as error:
            atomic_json(args.output_root.parent/'readiness.json',
                        {'schema_version':1,'status':'blocked','production_ready':False,
                         'candidate_complete':False,'error':str(error), 'paid_provider_requests':0})
            raise
        atomic_json(args.output_root.parent/'readiness.json',result)
    print(json.dumps(result,ensure_ascii=False))
    return 0

if __name__=='__main__': raise SystemExit(main())
