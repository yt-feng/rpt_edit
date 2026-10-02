"""Read exact private continuation evidence; never list, write R2, or translate."""
from __future__ import annotations
import argparse
import json
from pathlib import Path
from portal_extended_locales import ExpansionError, daily_corpus_day, digest, stable_bytes, validate_corpus
from portal_extended_r2 import (DEFAULT_PREFIX, HEX64, MAX_CHECKPOINT_BYTES,
    MAX_CANDIDATE_MANIFEST_BYTES, R2Store, checkpoint_is_valid, partial_manifest_is_valid, safe_part)


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
        'paid_provider_requests': 0,
        'production_writes': 0, 'model_calls': 0}
    (output/'inspection.json').write_bytes(stable_bytes(result))
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--prefix', default=DEFAULT_PREFIX)
    for option in ('generation', 'locale', 'checkpoint-sha', 'candidate-id'):
        parser.add_argument('--'+option, required=True)
    parser.add_argument('--output', type=Path, required=True)
    args = parser.parse_args()
    print(json.dumps(inspect(R2Store.from_env(args.prefix), args.generation, args.locale,
        args.checkpoint_sha, args.candidate_id, args.output), sort_keys=True))


if __name__ == '__main__':
    main()
