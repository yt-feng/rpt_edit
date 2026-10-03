"""Read exact private continuation evidence; never list, write R2, or translate."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from portal_extended_locales import ExpansionError, daily_corpus_day, digest, stable_bytes, validate_corpus
from portal_extended_r2 import (DEFAULT_PREFIX, HEX64, MAX_CHECKPOINT_BYTES,
    MAX_CANDIDATE_MANIFEST_BYTES, R2Store, checkpoint_is_valid, partial_manifest_is_valid, safe_part)


def quantity_diagnostics(checkpoint):
    """Bounded numeric signatures only; never emit either checkpoint text."""
    from financial_quantity_integrity import quantities, quantity_issues
    failed = []
    total = 0
    for key, row in checkpoint['rows'].items():
        source, translated = row['source'], row['text']
        if not quantity_issues(source, translated):
            continue
        total += 1
        if len(failed) >= 20:
            continue
        before, after = quantities(source), quantities(translated)
        bare_months = any(k[0] == 'month' and k[1] is None for k in before.keys() | after.keys())
        if bare_months:
            before, after = quantities(source, bare_months=True), quantities(translated, bare_months=True)
        def signature(counter):
            return sorted([{'kind': k[0], 'values': [str(v) if v is not None else None for v in k[1:]],
                            'count': n} for k, n in counter.items()], key=lambda item: json.dumps(item, sort_keys=True))
        failed.append({'unit_sha256': key, 'source_sha256': digest(source.encode()),
                       'translated_sha256': digest(translated.encode()),
                       'source_quantities': signature(before), 'translated_quantities': signature(after)})
    return {'failed_unit_count': total, 'reported_units': failed, 'maximum_reported_units': 20}


def inspect(store, generation, locale, checkpoint_sha, candidate_id, output):
    for value, label in ((generation, 'generation'), (checkpoint_sha, 'checkpoint sha'), (candidate_id, 'candidate')):
        safe_part(value, label=label, pattern=HEX64)
    if output.exists():
        raise ExpansionError('Inspection output must be a new directory')
    output.mkdir(parents=True)
    source = store.restore_source(generation, output/'corpus.json')
    corpus = json.loads((output/'corpus.json').read_bytes())
    docs = validate_corpus(corpus)
    if not daily_corpus_day(corpus) or not 1 <= len(docs) <= 24:
        raise ExpansionError('Continuation requires a bounded original daily corpus')
    checkpoint_raw = store._get(store.checkpoint_object_key(locale, generation, checkpoint_sha), maximum=MAX_CHECKPOINT_BYTES)
    if digest(checkpoint_raw) != checkpoint_sha:
        raise ExpansionError('Immutable checkpoint checksum mismatch')
    checkpoint = json.loads(checkpoint_raw)
    checkpoint_is_valid(checkpoint, locale, generation)
    if checkpoint.get('source_generation') != generation:
        raise ExpansionError('Continuation requires an explicit checkpoint source generation')
    manifest_raw = store._get(store.candidate_manifest_key(locale, generation, candidate_id), maximum=MAX_CANDIDATE_MANIFEST_BYTES)
    manifest = partial_manifest_is_valid(json.loads(manifest_raw), locale, generation)
    if manifest['files_sha256'] != candidate_id or manifest.get('source_document_count') != len(docs):
        raise ExpansionError('Candidate identity or source count mismatch')
    source_urls = {doc['url'] for doc in docs}
    completed = [row['source_url'] for row in manifest['pages']]
    if len(set(completed)) != len(completed) or not set(completed) <= source_urls:
        raise ExpansionError('Candidate page inventory differs from original corpus')
    (output/'checkpoint.json').write_bytes(checkpoint_raw)
    (output/'candidate-manifest.json').write_bytes(manifest_raw)
    from probe_portal_extended_runtime import first_pending
    pending = first_pending(corpus, locale, output/'checkpoint.json')
    pending_summary = None
    if pending is not None:
        text, language, markdown = pending
        pending_summary = {'sha256': digest(text.encode()), 'characters': len(text),
                           'whitespace_words': len(text.split()), 'source_language': language, 'markdown': markdown}
    result = {'schema_version': 1, 'read_only': True, 'generation': generation,
        'source_day': daily_corpus_day(corpus), 'source_sha256': source['sha256'],
        'source_document_count': len(docs), 'locale': locale,
        'checkpoint_sha256': checkpoint_sha, 'checkpoint_rows': len(checkpoint['rows']),
        'checkpoint_source_fallbacks': len(checkpoint.get('source_fallbacks', {})),
        'candidate_id': candidate_id, 'manifest_sha256': digest(manifest_raw),
        'status': manifest['status'], 'budget_exhausted': manifest.get('budget_exhausted'),
        'failure_count': len(manifest.get('failures', [])), 'completed_page_count': len(completed),
        'remaining_source_urls': sorted(source_urls - set(completed)),
        'next_pending_unit': pending_summary, 'checkpoint_policy': 'validated-units-with-source-fallback',
        'quantity_diagnostics': quantity_diagnostics(checkpoint),
        'paid_provider_requests': 0,
        'production_writes': 0, 'model_calls': 0}
    (output/'inspection.json').write_bytes(stable_bytes(result))
    return result


def inspect_english(store, source_store, generation, checkpoint_sha, candidate_id, output):
    """Inspect one immutable private English failure without translating or writing R2."""
    from build_portal_extended_locales import Memo, extended_source_language, reject_symlinks, safe_failure_code, validate_text
    from portal_english_commentary import failure_code_counts, preview_text, require, text
    from portal_english_pipeline import MAX_MANIFEST, batch_admission, verify_manifest
    for value, label in ((generation, 'generation'), (checkpoint_sha, 'checkpoint sha'), (candidate_id, 'candidate')):
        safe_part(value, label=label, pattern=HEX64)
    reject_symlinks(output)
    require(not output.exists(), 'Inspection output must be a new directory')
    proof, admission, source = batch_admission(store, source_store, generation)
    checkpoint_raw = store._get(store.checkpoint_object_key('en', generation, checkpoint_sha), maximum=MAX_CHECKPOINT_BYTES)
    require(digest(checkpoint_raw) == checkpoint_sha, 'Immutable English checkpoint checksum mismatch')
    checkpoint = json.loads(checkpoint_raw)
    checkpoint_is_valid(checkpoint, 'en', generation)
    fields = {'model', 'locale', 'version', 'rows', 'source_generation'}
    require(set(checkpoint) in (fields, fields | {'source_fallbacks'})
            and checkpoint.get('source_generation') == generation and checkpoint.get('source_fallbacks', {}) == {},
            'English checkpoint requires exact source and no source fallback')
    memo = object.__new__(Memo); memo.locale = 'en'
    for key, row in checkpoint['rows'].items():
        require(isinstance(row, dict) and set(row) == {'source', 'language', 'text'}
                and all(isinstance(row[field], str) for field in row)
                and key == memo.key(row['source'], row['language']), 'Invalid English checkpoint unit identity')
    manifest_raw = store._get(store.key('candidates', generation, candidate_id, 'candidate-manifest.json'), maximum=MAX_MANIFEST)
    require(digest(manifest_raw) == candidate_id, 'Immutable English candidate checksum mismatch')
    manifest = verify_manifest(json.loads(manifest_raw), source)
    counts = failure_code_counts(manifest['failures'])
    failed = {row['id']: row['code'] for row in manifest['failures']}
    diagnostics = []
    for doc in source['documents']:
        if doc['id'] not in failed:
            continue
        units = [('title', doc['title'])] + [('block', row['text']) for row in doc['blocks']]
        cached_blocks = []; checks = []
        for field, original in units:
            language = extended_source_language(original)
            row = checkpoint['rows'].get(memo.key(original, language))
            check = {'field': field, 'source_sha256': digest(original.encode()),
                     'source_characters': len(original), 'cached': row is not None}
            if row is not None:
                translated = row['text']; check['cached_characters'] = len(translated)
                try:
                    validate_text(original, translated, 'en', language)
                    text(translated, 500 if field == 'title' else 12000, english=True)
                    check['validation'] = 'passed'
                except ExpansionError as error:
                    # Fixed categories only; source/translation/error messages remain private.
                    check['validation'] = {
                        'Empty/oversized English editorial text': 'english-text-size',
                        'Non-English source fallback is forbidden': 'english-source-residue',
                        'Embedded/original asset reference is forbidden': 'english-asset-reference',
                        'Original report field is forbidden': 'english-original-field',
                    }.get(str(error), safe_failure_code(error))
                if field == 'block': cached_blocks.append({'text': translated})
            checks.append(check)
        preview_check = 'missing-cached-blocks'
        if len(cached_blocks) == len(doc['blocks']):
            try:
                preview_text(cached_blocks); preview_check = 'passed'
            except ExpansionError:
                preview_check = 'english-preview-validation'
        diagnostics.append({'document_sha256': digest(doc['id'].encode()), 'code': failed[doc['id']],
                            'units': checks, 'preview_validation': preview_check})
    result = {'schema_version': 1, 'read_only': True, 'locale': 'en', 'generation': generation,
        'source_day': source['day'], 'source_sha256': digest(stable_bytes(source)),
        'source_admission': admission['source_admission'], 'english_admission': proof['admission'],
        'source_document_count': len(source['documents']), 'checkpoint_sha256': checkpoint_sha,
        'checkpoint_rows': len(checkpoint['rows']), 'candidate_id': candidate_id,
        'manifest_sha256': digest(manifest_raw), 'status': manifest['status'],
        'budget_exhausted': manifest['budget_exhausted'], 'completed_page_count': manifest['completed_page_count'],
        'failure_code_counts': counts, 'failed_documents': diagnostics,
        'production_writes': 0, 'model_calls': 0, 'paid_provider_requests': 0}
    output.mkdir(parents=True)
    (output/'inspection.json').write_bytes(stable_bytes(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix')
    parser.add_argument('--source-prefix', default=DEFAULT_PREFIX)
    for option in ('generation', 'locale', 'checkpoint-sha', 'candidate-id'):
        parser.add_argument('--'+option, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    if args.locale == 'en':
        from portal_english_commentary import PREFIX
        store = R2Store.from_env(args.prefix or PREFIX)
        result = inspect_english(store, R2Store(store.client, store.bucket, args.source_prefix),
            args.generation, args.checkpoint_sha, args.candidate_id, args.output)
        print(json.dumps(result, sort_keys=True))
        return
    print(json.dumps(inspect(R2Store.from_env(args.prefix or DEFAULT_PREFIX), args.generation, args.locale,
        args.checkpoint_sha, args.candidate_id, args.output), sort_keys=True))


if __name__ == '__main__':
    main()
