#!/usr/bin/env python3
"""Deliver a source-bound daily issue without an all-reports or model dependency."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import time

from market_views_partial_sources import (
    RECEIPT_NAME, collect_candidates, read_selection, write_delivery_receipt,
)
from market_views_source_digest import extract_candidates, substantive_sentences


def usable_excerpts(candidates, reasons):
    result = {}
    for name, candidate in candidates.items():
        try:
            if not (Path(candidate['directory']) / 'source_mineru.md').is_file():
                reasons[name] = 'daily_source_adapter_unavailable'
                continue
            evidence = Path(candidate['directory']) / 'source_excerpt_evidence.json'
            if evidence.is_file():
                text = '\n\n'.join(row['text'] for row in json.loads(evidence.read_text())['excerpts'])
            else:
                text = (Path(candidate['directory']) / 'source_mineru.md').read_text(encoding='utf-8')
            if not substantive_sentences(text, limit=3):
                raise ValueError('no_substantive_source_text')
            result[name] = candidate
        except (OSError, ValueError, KeyError, TypeError):
            reasons[name] = 'no_substantive_source_text'
    return result


def assemble(context, workspace, *, force_fallback=False):
    workspace = Path(workspace)
    manifest = Path(context['manifest_path'])
    raw, rows = read_selection(manifest)
    if hashlib.sha256(raw).hexdigest() != context['selected_manifest_sha256']:
        raise ValueError('guard_selected_manifest_changed')
    identity = {key: context[key] for key in ('date_folder', 'source_run_id', 'source_execution_sha')}
    candidates, reasons = {}, {}
    originals = Path(context['originals_dir'])
    if force_fallback:
        # Deliberately retain the full selection but make only three originals
        # available, including one deliberately missing source. No production
        # entry point may select this fixture.
        fixture = workspace / 'acceptance-originals'
        fixture.mkdir(parents=True, exist_ok=True)
        for row in rows[1:4]:
            matches = list(originals.rglob(row['source_pdf']))
            if len(matches) == 1 and matches[0].is_file() and not matches[0].is_symlink():
                shutil.copyfile(matches[0], fixture / row['source_pdf'])
        originals = fixture
    else:
        for key, legacy in (('available_dir', False), ('handoff_dir', True)):
            directory = Path(context[key])
            if not directory.is_dir():
                continue
            found, omitted = collect_candidates(manifest, directory, **identity,
                reports_per_shard=(context.get('reports_per_shard') or None) if legacy else None,
                allow_legacy=legacy, candidate_staging=workspace / (key + '-verified'))
            reasons.update(omitted)
            for name, candidate in found.items():
                candidates.setdefault(name, candidate)
        candidates = usable_excerpts(candidates, reasons)
    candidates, fallback_reasons = extract_candidates(manifest, originals, workspace / 'extracted',
        existing_candidates=candidates, deadline_seconds=600, per_report_seconds=45, max_pages=24)
    reasons.update(fallback_reasons)
    candidates = usable_excerpts(candidates, reasons)
    if force_fallback:
        reasons[rows[0]['source_pdf']] = 'acceptance_injected_missing'
        if rows[0]['source_pdf'] in candidates or not 0 < len(candidates) < len(rows):
            raise ValueError('acceptance_partial_source_case_not_exercised')
    source_dir = workspace / 'sources' / context['date_folder']
    receipt = write_delivery_receipt(manifest, source_dir, candidates, **identity,
        omission_reasons=reasons, unavailable_originals=context.get('unavailable_originals', []))
    return source_dir, receipt


def run_command(arguments, timeout):
    subprocess.run([sys.executable, '-B', *map(str, arguments)], check=True, timeout=timeout)


def verify_publication(date, *, attempts=5, sleep=time.sleep):
    from inspect_market_views_live import inspect
    from private_workflow_handoff import build_r2_client, r2_bucket
    for attempt in range(attempts):
        try:
            return inspect(build_r2_client(), r2_bucket(), [date])
        except Exception:
            if attempt == attempts - 1:
                raise
            sleep(10)


def deliver(context, workspace, *, acceptance_only=False, force_fallback=False, runner=run_command):
    if force_fallback and not acceptance_only:
        raise ValueError('forced_fallback_is_acceptance_only')
    workspace = Path(workspace).resolve()
    workspace.mkdir(parents=True, exist_ok=True)
    source_dir, receipt = assemble(context, workspace, force_fallback=force_fallback)
    date = context['date_folder']
    output_root = workspace / 'rendered'
    runner(['scripts/build_market_views_pdf.py', '--dropbox-output-root', source_dir.parent,
        '--date-folder', date, '--output-root', output_root,
        '--daily-delivery-receipt', source_dir / RECEIPT_NAME,
        '--max-figures-per-report', '2', '--max-figures', '40'], 900)
    runner(['scripts/render_market_views_reportlab_pdf.py', '--summary-root', output_root,
        '--date-folder', date], 180)
    output = output_root / date
    pdf = output / f'market_views_{date}.pdf'
    from prepare_public_market_view_pdf import prepare_public_copy
    public_pdf = workspace / 'public' / pdf.name
    prepare_public_copy(pdf, public_pdf)
    result = {'schema_version': 1, 'date_folder': date, 'edition': 'daily-digest',
        'acceptance_only': acceptance_only, 'force_fallback': force_fallback,
        'included_reports': receipt['included_reports'], 'expected_reports': receipt['expected_reports'],
        'skipped_reports': receipt['skipped_reports'],
        'expected_source_reports': receipt.get('expected_source_reports', receipt['expected_reports']),
        'pdf_sha256': hashlib.sha256(pdf.read_bytes()).hexdigest(),
        'public_pdf_sha256': hashlib.sha256(public_pdf.read_bytes()).hexdigest(),
        'public_pdf': str(public_pdf), 'provider_posts': 0, 'model_calls': 0, 'production_writes': 0}
    if not acceptance_only:
        from upload_market_view_to_r2 import upload_market_view, private_publication_complete
        item = upload_market_view(pdf, date, edition='daily-digest', source_receipt=source_dir / RECEIPT_NAME)
        if not private_publication_complete(date, expected_sha256=item['sha256']):
            raise RuntimeError('daily_publication_readback_incomplete')
        result.update(production_writes=0 if item.get('skipped_existing') else 1,
                      published_pdf_sha256=item['sha256'],
                      preserved_existing=bool(item.get('skipped_existing')),
                      live_readback=verify_publication(date))
    (workspace / 'delivery-result.json').write_text(json.dumps(result, indent=2) + '\n')
    (workspace / 'public' / 'delivery-coverage.json').write_text(json.dumps({
        key: receipt[key] for key in ('date_folder', 'source_run_id', 'source_execution_sha',
            'expected_reports', 'included_reports', 'skipped_reports', 'expected_source_reports',
            'manifest_sha256', 'source_inventory_sha256', 'complete_source_inventory')}, indent=2) + '\n')
    output_file = os.environ.get('GITHUB_OUTPUT')
    if output_file:
        with open(output_file, 'a') as stream:
            stream.write(f'public_pdf={public_pdf}\n')
            stream.write(f'published={str(not acceptance_only and not result.get("preserved_existing")).lower()}\n')
    print(json.dumps({key: result[key] for key in ('date_folder', 'included_reports', 'expected_source_reports',
        'skipped_reports', 'acceptance_only', 'production_writes')}, sort_keys=True))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--context', required=True, type=Path)
    parser.add_argument('--workspace', required=True, type=Path)
    parser.add_argument('--acceptance-only', action='store_true')
    parser.add_argument('--force-fallback', action='store_true')
    args = parser.parse_args()
    deliver(json.loads(args.context.read_text()), args.workspace,
            acceptance_only=args.acceptance_only, force_fallback=args.force_fallback)


if __name__ == '__main__':
    main()
