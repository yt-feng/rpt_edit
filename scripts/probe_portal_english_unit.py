"""Probe one admitted English failure with at most three equivalent CPU inputs."""
from __future__ import annotations
import argparse
from decimal import Decimal
import json
import os
from pathlib import Path
import re
import tempfile
import time

from build_portal_extended_locales import extended_source_language, safe_failure_code, validate_text
from financial_quantity_integrity import quantities
from hymt_offline_translation import (MODEL_ID, OfflineTranslationError, OfflineTranslationValidationError, _HyMTEngine, _mask,
    _quantity_retry_input, _restore_terms, placeholder_diagnostics, split_sentences, validate_result)
from inspect_portal_extended_continuation import inspect_english, quantity_signature
from portal_english_commentary import PREFIX, require, text as editorial_text
from portal_english_pipeline import batch_admission
from portal_extended_locales import ExpansionError, digest, stable_bytes
from portal_extended_r2 import DEFAULT_PREFIX, HEX64, R2Store, safe_part


def select_unit(store, source_store, generation, checkpoint_sha, candidate_id, unit_sha, temporary):
    safe_part(unit_sha, label='unit sha', pattern=HEX64)
    proof = inspect_english(store, source_store, generation, checkpoint_sha, candidate_id, temporary/'inspection')
    _, _, source = batch_admission(store, source_store, generation)
    matches = []
    for failed in proof['failed_documents']:
        index = failed['first_unvalidated_unit_index']
        if index is None:
            continue
        check = failed['units'][index]
        if check['cached'] or check['source_sha256'] != unit_sha:
            continue
        for doc in source['documents']:
            if digest(doc['id'].encode()) == failed['document_sha256']:
                units = [doc['title']] + [row['text'] for row in doc['blocks']]
                original = units[index]
                require(digest(original.encode()) == unit_sha, 'Probe unit identity mismatch')
                matches.append((original, check['field']))
    require(len(matches) == 1, 'Probe requires exactly one uncached first failed unit')
    original, field = matches[0]
    require(original == original.strip() and 0 < len(original) <= 1800
            and split_sentences(original) == [original], 'Probe requires one bounded translation fragment')
    return original, field, proof


def input_forms(original):
    """Change only one source-derived currency spelling, never its proposition."""
    masked, opaque, terms = _mask(original, 'en')
    current, protected, visible = _quantity_retry_input(masked, len(opaque)+len(terms), target='en')
    require(len(visible) == 1, 'Probe requires one visible financial fact')
    value = next(iter(visible.values()))
    facts = quantities(value)
    require(len(facts) == 1 and sum(facts.values()) == 1, 'Probe requires one currency amount')
    (fact,) = facts
    require(fact[0] == 'currency' and quantities(original) == facts and current.count(value) == 1,
            'Probe requires an unambiguous source currency span')
    currency, amount = fact[1], fact[2]
    require(isinstance(amount, Decimal), 'Probe currency must use exact decimal arithmetic')
    grouped = f'{currency} {amount:,.0f}' if amount == amount.to_integral_value() else f'{currency} {amount:,f}'
    scale, label = next(((scale, label) for scale, label in ((Decimal('1e9'), 'billion'),
        (Decimal('1e6'), 'million'), (Decimal('1e3'), 'thousand')) if abs(amount) >= scale), (Decimal(1), ''))
    number = format(amount/scale, 'f')
    if '.' in number: number = number.rstrip('0').rstrip('.')
    scaled = f'{currency} {number}' + (f' {label}' if label else '')
    absolute = format(amount, 'f')
    if '.' in absolute: absolute = absolute.rstrip('0').rstrip('.')
    alternate = ('absolute', f'{currency} {absolute}') if value == grouped else ('grouped', grouped)
    forms = []; seen = set()
    for name, spelling in (('production', value), alternate, ('scaled', scaled)):
        model_input = current.replace(value, spelling, 1)
        if model_input in seen: continue
        seen.add(model_input)
        materialized = _restore_terms(_restore_terms(_restore_terms(model_input, protected), terms), opaque)
        require(quantities(materialized) == quantities(original), 'Probe input changed source quantities')
        forms.append((name, model_input, protected, terms, opaque))
    require(1 <= len(forms) <= 3, 'Invalid probe bound')
    return forms


def numeric_signals(value):
    # Fixed spellings/counts explain common currency morphology without prose.
    return {name: len(re.findall(pattern, value, re.I)) for name, pattern in {
        'billion_singular': r'\bbillion\b', 'billions_plural': r'\bbillions\b',
        'million_singular': r'\bmillion\b', 'millions_plural': r'\bmillions\b',
        'hyphenated_currency': r'\d[\d.,]*[-–—](?:billion|million|thousand)[-–—](?:euro|dollar|pound)s?\b',
        'euro_alias': r'\b(?:EUR|euros?)\b|€', 'dollar_alias': r'\b(?:USD|dollars?)\b|\$',
    }.items()}


def probe(store, source_store, generation, checkpoint_sha, candidate_id, unit_sha, output, *, engine_factory=None, mode="equivalent-forms"):
    require(not output.exists(), 'Probe output already exists')
    with tempfile.TemporaryDirectory(prefix='english-unit-proof-') as directory:
        original, field, proof = select_unit(store, source_store, generation, checkpoint_sha,
            candidate_id, unit_sha, Path(directory))
    require(mode in {'equivalent-forms', 'production-sequence'}, 'Invalid probe mode')
    if mode == 'equivalent-forms':
        forms = [(name, value, protected, terms, opaque, 2)
                 for name, value, protected, terms, opaque in input_forms(original)]
    else:
        masked, opaque, terms = _mask(original, 'en')
        final, protected, _ = _quantity_retry_input(masked, len(opaque)+len(terms), target='en')
        forms = [('attempt-0', masked, {}, terms, opaque, 0),
                 ('attempt-1', masked, {}, terms, opaque, 1),
                 ('attempt-2', final, protected, terms, opaque, 2)]
    for _, value, protected, terms, opaque, _ in forms:
        materialized = _restore_terms(_restore_terms(_restore_terms(value, protected), terms), opaque)
        require(quantities(materialized) == quantities(original), 'Probe input changed original quantities')
    language = extended_source_language(original)
    require(language == 'zh', 'Probe requires the admitted Chinese source')
    before = quantities(original)
    result = {'schema_version': 1, 'read_only': True, 'generation': generation,
        'checkpoint_sha256': checkpoint_sha, 'candidate_id': candidate_id, 'unit_sha256': unit_sha,
        'source_sha256': proof['source_sha256'], 'source_admission': proof['source_admission'],
        'english_admission': proof['english_admission'], 'checkpoint_rows': proof['checkpoint_rows'],
        'completed_page_count': proof['completed_page_count'], 'source_characters': len(original),
        'source_quantities': quantity_signature(before), 'model': MODEL_ID, 'mode': mode,
        'maximum_model_calls': 3, 'model_calls': 0, 'production_writes': 0, 'paid_provider_requests': 0,
        'results': []}
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_bytes(stable_bytes(result))
    deadline = time.monotonic()+900
    factory = engine_factory or (lambda: _HyMTEngine(Path(os.environ['HYMT_MODEL_DIR'])))
    engine = factory()
    try:
        for name, model_input, protected, terms, opaque, retry in forms:
            require(time.monotonic() < deadline, 'Probe deadline exceeded')
            row = {'form': name, 'model_input_sha256': digest(model_input.encode()),
                   'model_input_characters': len(model_input), 'input_quantities_verified': True,
                   'accepted': False, 'quality_retry': retry, 'adapter_accepted': False}
            continue_sequence = True
            result['model_calls'] += 1
            try:
                response = engine.translate(model_input, language, 'en', quality_retry=retry, deadline=deadline)
                row.update(request_sha256=getattr(engine, 'last_request_sha256', None),
                    server_sha256=getattr(engine, 'server_sha256', None),
                    response_sha256=digest(response.encode(errors='surrogatepass')),
                    response_characters=len(response), placeholders=placeholder_diagnostics(model_input, response),
                    raw_response_quantities=quantity_signature(quantities(response)),
                    numeric_signals=numeric_signals(response))
                materialized = _restore_terms(_restore_terms(_restore_terms(response, protected), terms), opaque)
                after = quantities(materialized)
                row.update(materialized_sha256=digest(materialized.encode(errors='surrogatepass')),
                    materialized_quantities=quantity_signature(after),
                    missing_quantities=quantity_signature(before-after), extra_quantities=quantity_signature(after-before))
                validate_result(model_input, response, language, 'en', markdown=False, check_quantities=False)
                validate_result(original, materialized, language, 'en', markdown=False)
                row['adapter_accepted'] = True
                validate_text(original, materialized, 'en', language)
                editorial_text(materialized, 500 if field == 'title' else 12000, english=True)
                row['accepted'] = True
            except (OfflineTranslationError, ExpansionError, TimeoutError) as error:
                row['failure_code'] = safe_failure_code(error)
                continue_sequence = isinstance(error, OfflineTranslationValidationError)
            result['results'].append(row)
            output.write_bytes(stable_bytes(result))
            if mode == 'production-sequence' and (row['adapter_accepted'] or not continue_sequence):
                break
    finally:
        engine.close()
    return result


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    for option in ('generation', 'checkpoint-sha', 'candidate-id', 'unit-sha'):
        parser.add_argument('--'+option, required=True)
    parser.add_argument('--output', type=Path, required=True)
    parser.add_argument('--mode', choices=['production-sequence', 'equivalent-forms'], default='production-sequence')
    args = parser.parse_args()
    try:
        store = R2Store.from_env(PREFIX)
        result = probe(store, R2Store(store.client, store.bucket, DEFAULT_PREFIX), args.generation,
            args.checkpoint_sha, args.candidate_id, args.unit_sha, args.output, mode=args.mode)
        print(json.dumps(result, sort_keys=True))
    except Exception as error:
        # No traceback or exception prose: engine/storage errors may contain private text.
        print(json.dumps({'probe_failed': True, 'failure_code': safe_failure_code(error)}))
        raise SystemExit(1) from None


if __name__ == '__main__': main()
