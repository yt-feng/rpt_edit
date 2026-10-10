"""Exact French quantity-fallback recovery with a durable one-revision unit ledger."""
from __future__ import annotations
import argparse
import copy
import json
from pathlib import Path
import shutil
import time

from assemble_portal_extended_locales import verified_candidate
from build_portal_extended_locales import (CHECKPOINT_VERSION, SOURCE_FALLBACK_VERSION,
    MAX_PUBLIC_TRANSLATION_DIAGNOSTICS, build, reject_symlinks, safe_failure_code,
    translate_document, validate_budget, validate_text)
from offline_translation import MODEL_ID, OfflineTranslationValidationError, TranslationBudgetExceeded
from portal_extended_continuation import producer_identity
from portal_extended_locales import ExpansionError, digest, file_for_url, render_document, stable_bytes, validate_corpus
from portal_extended_r2 import (HEX64, MAX_CHECKPOINT_BYTES, R2NotFound, R2TransportError, checkpoint_is_valid)

POLICY = 'fr-quantity-fallback-v1'
REVISION = 'fr-space-grouping-quarter-v1'
LOCALE = 'fr'
MAX_UNITS = 20
MAX_LEDGER_BYTES = 1024 * 1024
TERMINAL_CODES = {'offline-quantity-validation', 'offline-placeholder-validation',
    'offline-markdown-validation', 'offline-target-script-validation', 'offline-empty-validation',
    'offline-token-limit', 'offline-unicode-validation', 'offline-validation', 'expansion-validation',
    'financial-quantity-validation', 'table-structure-validation', 'untranslated-source-validation',
    'chinese-residue-validation', 'target-script-validation', 'placeholder-validation',
    'empty-translation-validation', 'translation-size-validation'}


def require(condition, category):
    if not condition:
        raise ExpansionError(category)


def request(value, *, require_units=True):
    keys = {'policy', 'validator_revision', 'source_sha256', 'origin_sha256', 'producer',
            'checkpoint_sha256', 'candidate_id', 'manifest_sha256', 'units'}
    require(isinstance(value, dict) and set(value) == keys, 'fr_repair_request_invalid')
    require(value['policy'] == POLICY and value['validator_revision'] == REVISION, 'fr_repair_policy_invalid')
    for name in ('source_sha256', 'origin_sha256', 'checkpoint_sha256', 'candidate_id', 'manifest_sha256'):
        require(isinstance(value[name], str) and bool(HEX64.fullmatch(value[name])), 'fr_repair_identity_invalid')
    producer_identity(value['producer'])
    units = value['units']
    require(isinstance(units, list) and (1 if require_units else 0) <= len(units) <= MAX_UNITS
            and all(isinstance(unit, str) and HEX64.fullmatch(unit) for unit in units)
            and units == sorted(set(units)), 'fr_repair_units_invalid')
    return value


def unit_key(text, language, markdown=False):
    return digest(stable_bytes([CHECKPOINT_VERSION, MODEL_ID, LOCALE, language, text] +
                              (['markdown'] if markdown else [])))


def required_units(corpus):
    units = {}
    class Collect:
        def get(self, text, language='zh', *, markdown=False):
            if text.strip():
                units[unit_key(text, language, markdown)] = {'source': text, 'language': language, 'markdown': markdown}
            return text
    for doc in validate_corpus(corpus):
        translate_document(doc, Collect())
    return units


def checkpoint_units(value, generation):
    checkpoint_is_valid(value, LOCALE, generation)
    require(set(value) <= {'version', 'model', 'locale', 'source_generation', 'rows', 'source_fallbacks'}
            and value.get('source_generation') == generation and isinstance(value.get('source_fallbacks', {}), dict),
            'fr_repair_checkpoint_binding_invalid')
    rows, fallbacks = value['rows'], value.get('source_fallbacks', {})
    require(not set(rows) & set(fallbacks), 'fr_repair_conflicting_cache_units')
    for kind, data in (('row', rows), ('fallback', fallbacks)):
        for identity, row in data.items():
            fields = {'source', 'language', 'text'} if kind == 'row' else {'source', 'language', 'policy', 'code'}
            require(isinstance(row, dict) and set(row) == fields and isinstance(row.get('source'), str)
                    and row['source'].strip() and row.get('language') in {'zh', 'en'}
                    and identity in {unit_key(row['source'], row['language']), unit_key(row['source'], row['language'], True)},
                    'fr_repair_unit_binding_invalid')
            if kind == 'fallback':
                require(row['policy'] == SOURCE_FALLBACK_VERSION and isinstance(row['code'], str),
                        'fr_repair_fallback_policy_invalid')
            else:
                validate_text(row['source'], row.get('text'), LOCALE, row['language'])
    return rows, fallbacks


class FrozenMemo:
    """Read exact persisted units only; there is no translator or seed lookup."""
    def __init__(self, checkpoint):
        self.rows = checkpoint['rows']
        self.fallbacks = checkpoint.get('source_fallbacks', {})
        self.fallback_keys = set()
        self.fallback_uses = 0

    def get(self, text, language='zh', *, markdown=False):
        if not text.strip(): return text
        key = unit_key(text, language, markdown)
        row = self.rows.get(key)
        fallback = self.fallbacks.get(key)
        require(not (row is not None and fallback is not None), 'fr_repair_conflicting_cache_units')
        if row is not None:
            require(row['source'] == text and row['language'] == language, 'fr_repair_unit_binding_invalid')
            validate_text(text, row.get('text'), LOCALE, language)
            return row['text']
        require(isinstance(fallback, dict) and fallback['source'] == text and fallback['language'] == language
                and fallback['policy'] == SOURCE_FALLBACK_VERSION, 'fr_repair_unselected_cache_miss')
        self.fallback_keys.add(key)
        self.fallback_uses += 1
        return text


def verify_cached_pages(corpus, checkpoint, candidate, manifest):
    memo = FrozenMemo(checkpoint)
    urls = {doc['url'] for doc in corpus['documents']}
    for doc in corpus['documents']:
        relative = Path(LOCALE) / file_for_url(doc['url'])
        rendered = render_document(doc, translate_document(doc, memo), LOCALE, urls).encode()
        require((Path(candidate) / relative).read_bytes() == rendered, 'fr_repair_candidate_cache_binding_invalid')
    require(manifest.get('source_fallback_unit_count') == len(memo.fallback_keys)
            and manifest.get('source_fallback_occurrences') == memo.fallback_uses
            and manifest.get('source_fallback_codes') == sorted({memo.fallbacks[key]['code'] for key in memo.fallback_keys})
            and manifest.get('translation_complete') is (not memo.fallback_keys),
            'fr_repair_fallback_counts_invalid')


def frozen(corpus, checkpoint_raw, candidate, repair):
    request(repair, require_units=False)
    docs = validate_corpus(corpus)
    require(1 <= len(docs) <= 24 and digest(stable_bytes(corpus)) == repair['source_sha256'],
            'fr_repair_source_binding_invalid')
    require(isinstance(checkpoint_raw, bytes) and len(checkpoint_raw) <= MAX_CHECKPOINT_BYTES
            and digest(checkpoint_raw) == repair['checkpoint_sha256'], 'fr_repair_checkpoint_bytes_invalid')
    value = json.loads(checkpoint_raw)
    rows, fallbacks = checkpoint_units(value, corpus['documents_sha256'])
    manifest_raw = (Path(candidate) / 'candidate-manifest.json').read_bytes()
    require(digest(manifest_raw) == repair['manifest_sha256'], 'fr_repair_manifest_bytes_invalid')
    manifest, _ = verified_candidate(Path(candidate), corpus)
    require(manifest['locale'] == LOCALE and manifest['files_sha256'] == repair['candidate_id']
            and manifest['status'] == 'complete-candidate' and manifest['completed_page_count'] == len(docs)
            and not manifest.get('failures') and not manifest.get('budget_exhausted'), 'fr_repair_complete_candidate_required')
    required = required_units(corpus)
    # All required units, including unselected rows under the revised validator,
    # are admitted before claiming a single additional model inference.
    verify_cached_pages(corpus, value, candidate, manifest)
    eligible = sorted(key for key in required if key in fallbacks
                      and fallbacks[key]['code'] == 'offline-quantity-validation')
    require(set(repair['units']) <= set(eligible), 'fr_repair_selected_unit_ineligible')
    return value, manifest, required, eligible


def inspect_frozen(corpus, checkpoint_raw, old_candidate_path, repair):
    old, manifest, required, eligible = frozen(corpus, checkpoint_raw, old_candidate_path, repair)
    return {'schema_version': 1, 'policy': POLICY, 'validator_revision': REVISION, 'locale': LOCALE,
            'generation': corpus['documents_sha256'], 'source_sha256': repair['source_sha256'],
            'checkpoint_sha256': repair['checkpoint_sha256'], 'candidate_id': repair['candidate_id'],
            'manifest_sha256': repair['manifest_sha256'], 'page_count': len(manifest['pages']),
            'required_unit_count': len(required), 'eligible_unit_count': len(eligible),
            'eligible_units': eligible, 'maximum_selected_units': MAX_UNITS,
            'fallback_count': sum(key in old.get('source_fallbacks', {}) for key in required),
            'model_calls': 0, 'storage_writes': 0}


def ledger_key(store, unit, name):
    require(isinstance(unit, str) and bool(HEX64.fullmatch(unit)), 'fr_repair_ledger_unit_invalid')
    identity = digest(stable_bytes([CHECKPOINT_VERSION, MODEL_ID, LOCALE, unit, REVISION]))
    require(name in {'started.json', 'outcome.json'}, 'fr_repair_ledger_name_invalid')
    return store.key('source-fallback-repair-units', identity, name)


def read_optional(store, key):
    try:
        raw = store._get(key, maximum=MAX_LEDGER_BYTES)
    except R2NotFound:
        return None
    value = json.loads(raw)
    require(raw == stable_bytes(value), 'fr_repair_ledger_not_canonical')
    return value


def create_record(store, key, value):
    """Atomic create plus exact readback; an uncertain write never authorizes a call."""
    raw = stable_bytes(value)
    require(len(raw) <= MAX_LEDGER_BYTES, 'fr_repair_ledger_too_large')
    try:
        store.client.put_object(Bucket=store.bucket, Key=key, Body=raw, ContentType='application/json',
            CacheControl='private, no-store', Metadata={'sha256': digest(raw), 'kind': POLICY}, IfNoneMatch='*')
    except Exception as error:
        code = str(getattr(error, 'response', {}).get('Error', {}).get('Code', ''))
        if code in {'PreconditionFailed', '412', 'ConditionalRequestConflict', '409'}:
            return False
        raise R2TransportError('fr_repair_ledger_write_unresolved') from None
    require(store._get(key, maximum=MAX_LEDGER_BYTES) == raw, 'fr_repair_ledger_readback_invalid')
    return True


def claim_contract(unit, source):
    return {'schema_version': 1, 'policy': POLICY, 'validator_revision': REVISION, 'locale': LOCALE,
            'model': MODEL_ID, 'checkpoint_version': CHECKPOINT_VERSION, 'unit_sha256': unit,
            'source_sha256': digest(source['source'].encode()), 'source_language': source['language'],
            'markdown': source['markdown']}


def ledger_outcome(store, unit, source):
    claim = read_optional(store, ledger_key(store, unit, 'started.json'))
    outcome = read_optional(store, ledger_key(store, unit, 'outcome.json'))
    if claim is None:
        require(outcome is None, 'fr_repair_orphan_ledger_outcome')
        return None, None
    contract = claim_contract(unit, source)
    require(isinstance(claim, dict) and set(claim) == set(contract) | {'producer'}
            and {k: claim[k] for k in contract} == contract, 'fr_repair_ledger_claim_invalid')
    producer_identity(claim['producer'])
    if outcome is None:
        return claim, None
    common = {'schema_version', 'policy', 'validator_revision', 'unit_sha256', 'claim_sha256', 'status'}
    require(isinstance(outcome, dict) and outcome.get('status') in {'accepted', 'terminal'}, 'fr_repair_ledger_outcome_invalid')
    extra = {'row'} if outcome['status'] == 'accepted' else {'failure_code'}
    require(set(outcome) == common | extra and outcome['schema_version'] == 1
            and outcome['policy'] == POLICY and outcome['validator_revision'] == REVISION
            and outcome['unit_sha256'] == unit and outcome['claim_sha256'] == digest(stable_bytes(claim)),
            'fr_repair_ledger_outcome_invalid')
    if outcome['status'] == 'accepted':
        row = outcome['row']
        require(isinstance(row, dict) and set(row) == {'source', 'language', 'text'}
                and row['source'] == source['source'] and row['language'] == source['language'], 'fr_repair_ledger_row_invalid')
        validate_text(row['source'], row['text'], LOCALE, row['language'])
    else:
        require(outcome['failure_code'] in TERMINAL_CODES,
                'fr_repair_terminal_code_invalid')
    return claim, outcome


def attempt_unit(store, unit, source, owner, translator):
    claim, outcome = ledger_outcome(store, unit, source)
    if outcome is not None:
        return claim, outcome
    require(claim is None, 'fr_repair_unit_started_unresolved')
    claim = {**claim_contract(unit, source), 'producer': producer_identity(owner)}
    require(create_record(store, ledger_key(store, unit, 'started.json'), claim), 'fr_repair_unit_claim_already_exists')
    outcome = {'schema_version': 1, 'policy': POLICY, 'validator_revision': REVISION, 'unit_sha256': unit,
               'claim_sha256': digest(stable_bytes(claim))}
    diagnostics = getattr(translator, 'failure_diagnostics', [])
    diagnostic_start = len(diagnostics) if isinstance(diagnostics, list) else 0
    try:
        translated = translator.translate(source['source'], target=LOCALE, source=source['language'], markdown=source['markdown'])
        validate_text(source['source'], translated, LOCALE, source['language'])
    except (OfflineTranslationValidationError, ExpansionError) as error:
        code = safe_failure_code(error)
        require(code in TERMINAL_CODES, 'fr_repair_terminal_code_invalid')
        diagnostics = getattr(translator, 'failure_diagnostics', [])
        if isinstance(diagnostics, list):
            for row in diagnostics[diagnostic_start:MAX_PUBLIC_TRANSLATION_DIAGNOSTICS]:
                if isinstance(row, dict): row['failure_code'] = code
        discard = getattr(translator, 'discard_translation', None)
        if callable(discard): discard(source['source'], LOCALE, source['language'], markdown=source['markdown'])
        outcome.update(status='terminal', failure_code=code)
    else:
        outcome.update(status='accepted', row={'source': source['source'], 'language': source['language'], 'text': translated})
    # A crash/transport error above leaves only the started record. Retrying,
    # importing a new seed, or changing a producer ID cannot reopen this unit.
    require(create_record(store, ledger_key(store, unit, 'outcome.json'), outcome), 'fr_repair_outcome_already_exists')
    return ledger_outcome(store, unit, source)


def candidate_snapshot(path, checkpoint_raw):
    raw = (Path(path) / 'candidate-manifest.json').read_bytes()
    return {'checkpoint_sha256': digest(checkpoint_raw), 'candidate_id': json.loads(raw)['files_sha256'],
            'manifest_sha256': digest(raw)}


def proof_for(store, corpus, old, new, old_raw, new_raw, old_candidate, new_candidate, repair, required, *, changed):
    accepted, terminal, ledger = [], [], []
    for unit in repair['units']:
        claim, outcome = ledger_outcome(store, unit, required[unit])
        require(outcome is not None, 'fr_repair_unit_started_unresolved')
        (accepted if outcome['status'] == 'accepted' else terminal).append(unit)
        ledger.append({'unit_sha256': unit, 'claim_sha256': digest(stable_bytes(claim)),
                       'outcome_sha256': digest(stable_bytes(outcome)), 'status': outcome['status']})
    selected = set(repair['units'])
    untouched_rows = {k: v for k, v in old['rows'].items() if k not in selected}
    untouched_fallbacks = {k: v for k, v in old.get('source_fallbacks', {}).items() if k not in selected}
    coverage = [{key: doc[key] for key in ('url', 'content_sha256', 'source_html_sha256')} for doc in corpus['documents']]
    return {'schema_version': 1, 'policy': POLICY, 'validator_revision': REVISION,
            'generation': corpus['documents_sha256'], 'locale': LOCALE, 'source_sha256': repair['source_sha256'],
            'old': candidate_snapshot(old_candidate, old_raw), 'new': candidate_snapshot(new_candidate, new_raw),
            'units': repair['units'], 'accepted_units': accepted, 'terminal_units': terminal, 'ledger': ledger,
            'unchanged_rows_sha256': digest(stable_bytes(untouched_rows)),
            'unchanged_fallbacks_sha256': digest(stable_bytes(untouched_fallbacks)),
            'coverage_sha256': digest(stable_bytes(coverage)),
            'fallbacks_before': sum(k in old.get('source_fallbacks', {}) for k in required),
            'fallbacks_after': sum(k in new.get('source_fallbacks', {}) for k in required), 'changed': changed}


def verify_rebuild(store, corpus, oldraw, newraw, oldcandidate, newcandidate, repair, proof):
    request(repair)
    old, before, required, _ = frozen(corpus, oldraw, oldcandidate, repair)
    require(isinstance(newraw, bytes) and len(newraw) <= MAX_CHECKPOINT_BYTES, 'fr_repair_new_checkpoint_invalid')
    new = json.loads(newraw)
    checkpoint_units(new, corpus['documents_sha256'])
    after, _ = verified_candidate(Path(newcandidate), corpus)
    changed = after['files_sha256'] != before['files_sha256']
    expected = copy.deepcopy(old)
    for unit in repair['units']:
        _, outcome = ledger_outcome(store, unit, required[unit])
        require(outcome is not None, 'fr_repair_unit_started_unresolved')
        if changed and outcome['status'] == 'accepted':
            expected['rows'][unit] = outcome['row']
            del expected['source_fallbacks'][unit]
    if changed and not expected.get('source_fallbacks'):
        expected.pop('source_fallbacks', None)
    require(stable_bytes(new) == stable_bytes(expected), 'fr_repair_preserved_checkpoint_changed')
    if not changed:
        require(newraw == oldraw and candidate_snapshot(oldcandidate, oldraw) == candidate_snapshot(newcandidate, newraw),
                'fr_repair_noop_identity_changed')
    else:
        require(after['locale'] == LOCALE and len(after['pages']) == len(before['pages'])
                and after['status'] == 'complete-candidate', 'fr_repair_candidate_coverage_changed')
        verify_cached_pages(corpus, new, newcandidate, after)
    expected_proof = proof_for(store, corpus, old, new, oldraw, newraw, oldcandidate, newcandidate, repair, required, changed=changed)
    require(proof == expected_proof, 'fr_repair_proof_changed')
    return expected_proof


def rebuild(store, corpus, checkpoint_raw, old_candidate_path, output, checkpoint_path, repair, owner, translator, seconds=14400):
    request(repair); validate_budget(seconds); producer_identity(owner)
    old, before, required, _ = frozen(corpus, checkpoint_raw, old_candidate_path, repair)
    output, checkpoint_path = Path(output), Path(checkpoint_path)
    reject_symlinks(output); reject_symlinks(checkpoint_path)
    old_path = Path(old_candidate_path).resolve()
    out_path, memo_path = output.resolve(), checkpoint_path.resolve()
    require(not out_path.is_relative_to(old_path) and not old_path.is_relative_to(out_path)
            and not memo_path.is_relative_to(old_path) and not memo_path.is_relative_to(out_path)
            and not out_path.is_relative_to(memo_path), 'fr_repair_output_overlap')
    require(not output.exists() and not checkpoint_path.exists(), 'fr_repair_output_not_fresh')
    deadline = time.monotonic() + seconds
    setter = getattr(translator, 'set_deadline', None)
    if callable(setter): setter(deadline)
    # An already unresolved selected unit makes this request unbuildable. Detect
    # that before claiming fresh units; accepted outcomes remain available.
    for unit in repair['units']:
        claim, outcome = ledger_outcome(store, unit, required[unit])
        require(claim is None or outcome is not None, 'fr_repair_unit_started_unresolved')
    cloned = copy.deepcopy(old)
    for unit in repair['units']:
        if time.monotonic() >= deadline:
            raise TranslationBudgetExceeded('fr_repair_budget_exhausted')
        _, outcome = attempt_unit(store, unit, required[unit], owner, translator)
        if outcome['status'] == 'accepted':
            cloned['rows'][unit] = outcome['row']
            del cloned['source_fallbacks'][unit]
    if not cloned.get('source_fallbacks'):
        cloned.pop('source_fallbacks', None)
    checkpoint_path.parent.mkdir(parents=True, exist_ok=True)
    checkpoint_path.write_bytes(stable_bytes(cloned))
    class ForbiddenTranslator:
        def translate(self, *args, **kwargs):
            raise RuntimeError('fr_repair_unselected_cache_miss')
    result = build(corpus, LOCALE, output, checkpoint_path, ForbiddenTranslator(),
                   budget_seconds=max(1, min(seconds, int(deadline - time.monotonic()))), allow_source_fallback=True)
    require(result['status'] == 'complete-candidate' and result['translation_calls_this_run'] == 0,
            'fr_repair_cache_only_rebuild_failed')
    changed = result['files_sha256'] != before['files_sha256']
    if not changed:
        # Candidate IDs bind page bytes, so metadata-only rewrites would collide.
        shutil.rmtree(output); shutil.copytree(old_candidate_path, output)
        checkpoint_path.write_bytes(checkpoint_raw)
    newraw = checkpoint_path.read_bytes()
    proof = proof_for(store, corpus, old, json.loads(newraw), checkpoint_raw, newraw, old_candidate_path,
                      output, repair, required, changed=changed)
    verify_rebuild(store, corpus, checkpoint_raw, newraw, old_candidate_path, output, repair, proof)
    return proof


def main(argv=None):
    parser = argparse.ArgumentParser(description='Read an exact local frozen candidate; no network or model calls')
    parser.add_argument('operation', choices=['inspect'])
    for name in ('corpus', 'checkpoint', 'candidate', 'request', 'output'):
        parser.add_argument('--' + name, type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        summary = inspect_frozen(json.loads(args.corpus.read_bytes()), args.checkpoint.read_bytes(),
                                 args.candidate, json.loads(args.request.read_bytes()))
        args.output.write_bytes(stable_bytes(summary))
        print(json.dumps(summary, sort_keys=True))
        return 0
    except Exception:
        print(json.dumps({'status': 'rejected', 'code': 'fr_fallback_inspection_failed'}))
        return 1


if __name__ == '__main__':
    raise SystemExit(main())
