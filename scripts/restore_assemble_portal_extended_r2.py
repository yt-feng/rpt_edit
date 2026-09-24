#!/usr/bin/env python3
"""Restore approved R2 candidates and assemble them into one fresh inactive tree.

The candidate map is an explicit approval boundary: every locale named for the
release must have a matching complete candidate id.  Restores use the private
R2 client and a temporary runner directory; only the verified assembled tree
and a small review identity are left for the normal release workflow.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import tempfile

from assemble_portal_extended_locales import assemble
from offline_translation import MODEL_ID, PROVIDER
from portal_extended_locales import ExpansionError, select_locales, stable_bytes
from portal_extended_r2 import HEX64, R2Store, safe_part


def parse_candidate_specs(value: str, approved_locales: str) -> tuple[tuple[str, ...], dict[str, str]]:
    """Parse an explicit ``locale=candidate_sha256`` approval map."""
    approved = select_locales(approved_locales)
    rows = [item.strip() for item in str(value or '').split(',') if item.strip()]
    if not rows:
        raise ExpansionError('At least one approved R2 candidate is required')
    candidates: dict[str, str] = {}
    for row in rows:
        locale, separator, candidate_id = row.partition('=')
        if not separator or locale not in approved or locale in candidates:
            raise ExpansionError('Candidate map must contain one id for each approved locale')
        candidate_id = candidate_id.strip()
        if HEX64.fullmatch(candidate_id) is None:
            raise ExpansionError(f'Invalid candidate id for {locale}')
        candidates[locale] = candidate_id
    if set(candidates) != set(approved):
        raise ExpansionError('Candidate map must exactly match the approved locale set')
    return approved, candidates


def restore_and_assemble(
    *,
    root: Path,
    prefix: str,
    source_generation: str,
    approved_locales: str,
    candidate_specs: str,
    evidence_out: Path,
) -> dict:
    approved, candidates = parse_candidate_specs(candidate_specs, approved_locales)
    generation = safe_part(source_generation, label='source generation', pattern=HEX64)
    store = R2Store.from_env(prefix)
    with tempfile.TemporaryDirectory(prefix='extended-r2-restore-') as temporary:
        workspace = Path(temporary)
        corpus_path = workspace / 'source-corpus.json'
        source_result = store.restore_source(generation, corpus_path)
        corpus = json.loads(corpus_path.read_text(encoding='utf-8'))
        candidate_dirs = []
        restore_results = []
        for locale in approved:
            directory = workspace / 'candidates' / locale
            restore_results.append(store.restore_candidate(locale, generation, candidates[locale], directory))
            candidate_dirs.append(directory)
        result = assemble(
            root, corpus, candidate_dirs, approved, apply=True,
            existing_locales=('ko', 'ja', 'ar'),
        )
        evidence = {
            'schema_version': 1,
            'source_generation': generation,
            'source_restore': source_result,
            'locales': list(approved),
            'candidate_ids': candidates,
            'candidate_restores': restore_results,
            'pages_per_locale': result['pages_per_locale'],
            'assembly': result,
            'model': MODEL_ID,
            'provider': PROVIDER,
            'paid_provider_requests': 0,
            'indexable_after_approval': True,
        }
    evidence_out.parent.mkdir(parents=True, exist_ok=True)
    evidence_out.write_bytes(stable_bytes(evidence))
    return evidence


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--root', required=True, type=Path)
    parser.add_argument('--prefix', default='_extended-locales/v1')
    parser.add_argument('--source-generation', required=True)
    parser.add_argument('--approved-locales', required=True)
    parser.add_argument('--candidates', required=True, help='locale=sha256,locale=sha256')
    parser.add_argument('--evidence-out', required=True, type=Path)
    args = parser.parse_args()
    result = restore_and_assemble(
        root=args.root,
        prefix=args.prefix,
        source_generation=args.source_generation,
        approved_locales=args.approved_locales,
        candidate_specs=args.candidates,
        evidence_out=args.evidence_out,
    )
    print(json.dumps({
        'source_generation': result['source_generation'],
        'locales': result['locales'],
        'candidate_ids': result['candidate_ids'],
        'pages_per_locale': result['pages_per_locale'],
        'model': result['model'],
        'provider': result['provider'],
    }, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
