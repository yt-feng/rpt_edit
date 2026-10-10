"""Separate rendered-page progress from translated readiness without inference.

Quality receipts are immutable and bind exact private source/manifest bytes.
The bounded debt ledger is independent of publication ACKs and render cursors;
it never schedules inference or erases an accepted translation checkpoint.
The separate bounded quality-recovery planner consumes exact debt proofs.
"""
from __future__ import annotations

import json

from portal_extended_locales import ExpansionError, digest, select_locales, stable_bytes, validate_corpus
from portal_extended_r2 import (HEX64, MAX_CANDIDATE_MANIFEST_BYTES, MAX_SOURCE_BYTES,
                                R2NotFound, partial_manifest_is_valid, safe_part)

MAX_DEBT_GENERATIONS = 500
MAX_FALLBACK_UNITS = 10000
MAX_PROOF_BYTES = 1024 * 1024


def quality_fields(manifest):
    """Missing legacy evidence is unknown, never inferred from render success."""
    count = manifest.get('source_fallback_unit_count')
    occurrences = manifest.get('source_fallback_occurrences')
    explicit = manifest.get('translation_complete')
    codes = manifest.get('source_fallback_codes')
    known = (type(explicit) is bool and type(count) is int and 0 <= count <= MAX_FALLBACK_UNITS
             and type(occurrences) is int and count <= occurrences <= 1000000
             and isinstance(codes, list) and len(codes) <= 100
             and all(isinstance(code, str) and 1 <= len(code) <= 100 for code in codes)
             and codes == sorted(set(codes)))
    if all(key in manifest for key in ('translation_complete', 'source_fallback_unit_count',
                                      'source_fallback_occurrences', 'source_fallback_codes')) and not known:
        raise ExpansionError('Candidate translated readiness evidence is malformed')
    hashes = manifest.get('source_fallback_unit_sha256')
    if hashes is not None and (not isinstance(hashes, list) or not known or len(hashes) != count
            or any(not isinstance(key, str) or not HEX64.fullmatch(key) for key in hashes)
            or hashes != sorted(set(hashes))):
        raise ExpansionError('Candidate fallback unit inventory is invalid')
    complete = (manifest.get('status') == 'complete-candidate'
                and manifest.get('completed_page_count') == manifest.get('source_document_count')
                and manifest.get('failures') == [] and manifest.get('budget_exhausted') is False)
    if known and (explicit != (complete and count == 0) or (count == 0 and (occurrences != 0 or codes))
                  or (count > 0 and not codes)):
        raise ExpansionError('Candidate translated readiness conflicts with fallback evidence')
    ready = known and complete and explicit and count == 0
    return {'translation_ready': bool(ready),
            'quality_status': 'translated' if ready else 'source-fallback' if known and count else 'unproven',
            'source_fallback_unit_count': count if known else None,
            'source_fallback_occurrences': occurrences if known else None,
            'source_fallback_codes': codes if known else [],
            'fallback_unit_hashes_complete': hashes is not None,
            'source_fallback_unit_sha256': hashes or []}


def proof_key(store, checksum):
    safe_part(checksum, label='quality proof', pattern=HEX64)
    return store.key('incremental', 'quality-proofs', checksum, 'receipt.json')


def candidate_quality(store, locale, generation, candidate, *, manifest_sha256=None):
    """Read and validate exact source/manifest identity; no model or state writes."""
    if select_locales(locale) != (locale,):
        raise ExpansionError('Quality proof requires one non-English locale')
    safe_part(generation, label='quality generation', pattern=HEX64)
    safe_part(candidate, label='quality candidate', pattern=HEX64)
    source_raw = store._get(store.source_key(generation), maximum=MAX_SOURCE_BYTES)
    source = json.loads(source_raw)
    docs = validate_corpus(source)
    if source['documents_sha256'] != generation:
        raise ExpansionError('Quality source generation mismatch')
    raw = store._get(store.candidate_manifest_key(locale, generation, candidate),
                     maximum=MAX_CANDIDATE_MANIFEST_BYTES)
    if manifest_sha256 is not None and digest(raw) != manifest_sha256:
        raise ExpansionError('Quality manifest differs from exact registered outcome')
    manifest = partial_manifest_is_valid(json.loads(raw), locale, generation)
    by_url = {doc['url']: doc for doc in docs}
    pages = manifest['pages']
    if (manifest['files_sha256'] != candidate or manifest.get('source_document_count') != len(docs)
            or len({row['source_url'] for row in pages}) != len(pages)
            or any(row['source_url'] not in by_url
                   or any(row.get(field) != by_url[row['source_url']][source_field]
                          for field, source_field in (('source_content_sha256', 'content_sha256'),
                                                       ('source_html_sha256', 'source_html_sha256')))
                   for row in pages)):
        raise ExpansionError('Quality candidate differs from source inventory')
    fields = quality_fields(manifest)
    return {'schema_version': 1, 'locale': locale, 'generation': generation, 'candidate_id': candidate,
            'source_sha256': digest(source_raw), 'manifest_sha256': digest(raw),
            'render_complete': manifest['status'] == 'complete-candidate',
            'source_page_count': len(docs), 'completed_page_count': manifest['completed_page_count'],
            'paid_provider_requests': 0, **fields}


def debt_rows(store, locale):
    from portal_extended_incremental import read_state
    rows = read_state(store, 'quality-debt', locale).get('generations', {})
    if not isinstance(rows, dict) or len(rows) > MAX_DEBT_GENERATIONS:
        raise ExpansionError('Locale quality debt exceeds its bounded ledger')
    for generation, row in rows.items():
        if (not HEX64.fullmatch(str(generation)) or not isinstance(row, dict)
                or set(row) != {'proof_sha256', 'candidate_id', 'source_fallback_unit_count', 'quality_status'}
                or any(not HEX64.fullmatch(str(row.get(key))) for key in ('proof_sha256', 'candidate_id'))
                or row['quality_status'] not in {'source-fallback', 'unproven'}
                or (row['source_fallback_unit_count'] is not None and
                    (type(row['source_fallback_unit_count']) is not int
                     or not 0 <= row['source_fallback_unit_count'] <= MAX_FALLBACK_UNITS))):
            raise ExpansionError('Invalid locale quality debt entry')
    return rows


def record_quality(store, locale, generation, candidate, *, manifest_sha256=None):
    """Persist immutable evidence before updating/removing a mutable debt row."""
    proof = candidate_quality(store, locale, generation, candidate, manifest_sha256=manifest_sha256)
    raw = stable_bytes(proof)
    if len(raw) > MAX_PROOF_BYTES:
        raise ExpansionError('Locale quality proof exceeds byte bound')
    checksum = digest(raw)
    key = proof_key(store, checksum)
    try:
        previous = store._get(key, maximum=MAX_PROOF_BYTES)
    except R2NotFound:
        store._put(key, raw, metadata={'kind': 'locale-quality-proof'})
        previous = store._get(key, maximum=MAX_PROOF_BYTES)
    if previous != raw:
        raise ExpansionError('Immutable locale quality proof did not persist')
    rows = debt_rows(store, locale)
    updated = dict(rows)
    if proof['translation_ready']:
        updated.pop(generation, None)
    elif proof['render_complete']:
        updated[generation] = {key: proof[key] for key in ('candidate_id', 'source_fallback_unit_count', 'quality_status')}
        updated[generation]['proof_sha256'] = checksum
    if updated != rows:
        if len(updated) > MAX_DEBT_GENERATIONS:
            raise ExpansionError('Locale quality debt is full; no existing evidence was evicted')
        from portal_extended_incremental import write_state
        write_state(store, 'quality-debt', locale, {'generations': updated})
    return {**proof, 'proof_sha256': checksum}


def verify_quality(store, checksum, locale, generation, candidate):
    raw = store._get(proof_key(store, checksum), maximum=MAX_PROOF_BYTES)
    if digest(raw) != checksum:
        raise ExpansionError('Locale quality proof checksum mismatch')
    proof = json.loads(raw)
    if (not isinstance(proof, dict) or proof.get('locale') != locale
            or proof.get('generation') != generation or proof.get('candidate_id') != candidate):
        raise ExpansionError('Locale quality proof identity mismatch')
    expected = candidate_quality(store, locale, generation, candidate)
    if proof != expected or not proof['translation_ready']:
        raise ExpansionError('Automatic publication requires exact translated-ready quality evidence')
    return proof


def handoff_quality(store, receipt):
    proofs = receipt.get('translation_quality_proofs')
    batch = receipt['batch']
    if not isinstance(proofs, dict) or set(proofs) != set(batch['candidates']):
        raise ExpansionError('Automatic handoff lacks exact translated-ready quality proofs')
    return {locale: verify_quality(store, proofs[locale], locale, batch['generation'], candidate)
            for locale, candidate in batch['candidates'].items()}


def quality_summary(store, locales):
    details = {}
    for locale in locales:
        rows = debt_rows(store, locale)
        if rows:
            details[locale] = {'generations': len(rows),
                'source_fallback_units': sum(row['source_fallback_unit_count'] or 0 for row in rows.values()),
                'unproven_generations': sum(row['quality_status'] == 'unproven' for row in rows.values())}
    return {'quality_debt_locale_count': len(details),
            'quality_debt_generation_count': sum(row['generations'] for row in details.values()),
            'quality_debt_source_fallback_units': sum(row['source_fallback_units'] for row in details.values()),
            'quality_debt_by_locale': details, 'quality_debt_automatic_retries': 0}
