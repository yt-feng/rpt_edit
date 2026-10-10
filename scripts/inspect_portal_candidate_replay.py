"""Read-only, no-inference comparison of approved candidate and current replay.

Only hashes, counts and fixed error categories leave this diagnostic. Candidate
HTML, source and checkpoint text remain in the temporary runner directory.
"""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import contextmanager
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
import unicodedata

import requests

from assemble_portal_extended_locales import verified_candidate
from build_portal_extended_locales import (build, validate_text, safe_failure_code,
    Memo, extended_source_language, SOURCE_FALLBACK_VERSION)
from portal_extended_locales import COPY, HTML_BLOCKS, ORIGIN, daily_corpus_day, digest, validate_corpus
import portal_extended_publication as publication
from portal_extended_publication import (CacheOnly, checked_batches, read_active_ledger,
    prove_approved_baseline, restore_active_checkpoint, active_checkpoint_sha)
from portal_extended_r2 import R2Store, R2StoreError, R2NotFound
from financial_quantity_integrity import quantities
from portal_approved_quantity_contract import CONTRACT_ID, PARSER_SHA256, bindings, quantity_issues as approved_quantity_issues

MAX_BATCHES = 36
MAX_DOCUMENTS = 24
MAX_STATE_BYTES = 65536
CALENDAR_MONTH_ALIASES = json.loads((Path(__file__).parent/'portal_extended_calendar_months.json').read_text(encoding='utf-8'))['languages']
BN_MONTH_ALIASES = CALENDAR_MONTH_ALIASES['bn']
MAX_CACHE_AUDITS = 128
MAX_UNIT_VARIANTS = 8
SOURCE_LANGUAGES = {'en', 'zh', 'ar', 'ja', 'ko'}


class InspectionError(ValueError):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


class ReadOnlyClient:
    """Reject accidental mutation even if an inspected helper later changes."""
    def __init__(self, client):
        self.client = client

    def __getattr__(self, name):
        if name not in {'head_object', 'get_object'}:
            raise InspectionError('storage-operation-forbidden')
        return getattr(self.client, name)


class PhaseError(ValueError):
    def __init__(self, stage, error):
        super().__init__('inspection-failed')
        self.stage = stage
        self.error_type = type(error).__name__


def phase(stage, function, *args, **kwargs):
    try:
        return function(*args, **kwargs)
    except Exception as error:
        raise PhaseError(stage, error) from error


class VisibleText(HTMLParser):
    def __init__(self):
        super().__init__()
        self.body = False
        self.hidden = 0
        self.parts = []
        self.tags = Counter()

    def handle_starttag(self, tag, attrs):
        if tag == 'body': self.body = True
        if self.body and tag in ('script', 'style'): self.hidden += 1
        if self.body and tag in ('p', 'h1', 'h2', 'h3', 'li', 'table', 'a'):
            self.tags[tag] += 1

    def handle_endtag(self, tag):
        if self.body and tag in ('script', 'style'): self.hidden = max(0, self.hidden - 1)
        if tag == 'body': self.body = False

    def handle_data(self, value):
        if self.body and not self.hidden: self.parts.append(value)


def html_shape(path):
    parser = VisibleText()
    parser.feed(path.read_text(encoding='utf-8'))
    parser.close()
    visible = ' '.join(' '.join(parser.parts).split()).encode('utf-8')
    return {'visible_text_sha256': digest(visible), 'visible_text_bytes': len(visible),
            'element_counts': dict(parser.tags)}


def validated_corpus(path):
    corpus = json.loads(path.read_bytes())
    docs = validate_corpus(corpus)
    if not daily_corpus_day(corpus) or len(docs) > MAX_DOCUMENTS:
        raise InspectionError('unbounded-source')
    return corpus


def quantity_signature(source, translated, locale):
    before, after = quantities(source), quantities(translated)
    if any(key[0] == 'month' and key[1] is None for key in before.keys() | after.keys()):
        before, after = quantities(source, bare_months=True), quantities(translated, bare_months=True)
    missing, added = before - after, after - before
    result = {'approved_parser_v1_matches': not approved_quantity_issues(source, translated, '', locale),
              'missing_kinds': dict(Counter({kind: sum(n for key, n in missing.items() if key[0] == kind)
                                          for kind in {k[0] for k in missing}})),
              'added_kinds': dict(Counter({kind: sum(n for key, n in added.items() if key[0] == kind)
                                          for kind in {k[0] for k in added}}))}
    if locale in CALENDAR_MONTH_ALIASES:
        normalized = unicodedata.normalize('NFKC', translated).casefold()
        matched = Counter()
        for index, aliases in enumerate(CALENDAR_MONTH_ALIASES[locale], 1):
            pattern = '(?:' + '|'.join(re.escape(unicodedata.normalize('NFKC', name).casefold()) for name in aliases) + ')'
            # Combining marks are part of Bengali words; ASCII boundaries
            # alone would also match a calendar name inside another token.
            for match in re.finditer(pattern, normalized):
                left = normalized[match.start()-1] if match.start() else ''
                right = normalized[match.end()] if match.end() < len(normalized) else ''
                word = lambda c: bool(c) and (c.isalnum() or unicodedata.category(c).startswith('M') or c == '_')
                if not word(left) and not word(right): matched[('month', None, index)] += 1
        result['calendar_alias_occurrences'] = sum(matched.values())
        result['language_scoped_month_repair_matches'] = bool(matched) and before == after + matched
    return result


def failed_source_unit(doc, field):
    """Resolve only the bounded field grammar emitted by translate_document.

    No replay or inference is performed here. A pipe part retains its original
    parent's markdown flag, exactly as the builder does.
    """
    if not isinstance(field, str) or len(field) > 80:
        raise ValueError('unresolved-field')
    base, *parts = field.split('.part')
    if len(parts) > 1 or (parts and not re.fullmatch(r'0|[1-9][0-9]{0,4}', parts[0])):
        raise ValueError('unresolved-field')
    markdown = False
    if base in {'title', 'description'}:
        text = doc[base]
    elif base.startswith('copy.') and base[5:] in COPY:
        text = COPY[base[5:]]
    elif match := re.fullmatch(r'block\.(0|[1-9][0-9]{0,4})\.([a-z][a-z0-9]*)', base):
        block = doc['blocks'][int(match[1])]
        if match[2] not in HTML_BLOCKS or block['tag'] != match[2]: raise ValueError('unresolved-field')
        text = block['text']; markdown = block['tag'] == 'tr' or '|' in text
    elif match := re.fullmatch(r'link\.(0|[1-9][0-9]{0,4})', base):
        text = doc['links'][int(match[1])]['label']
    else:
        raise ValueError('unresolved-field')
    parent = text if parts else None
    if parts:
        if '|' not in text: raise ValueError('unresolved-field')
        text = text.split('|')[int(parts[0])]
    elif '|' in text:
        raise ValueError('unresolved-field')
    return text, markdown, parent


def unit_key(locale, source, language, markdown):
    memo = object.__new__(Memo)
    memo.locale = locale
    return memo.key(source, language, markdown=markdown)


def unit_validation(source, row, locale, validator):
    try:
        validate_text(source, row.get('text'), locale, row['language'], quantity_validator=validator)
    except Exception as error:
        code = safe_failure_code(error)
        return code if code in {'financial-quantity-validation', 'table-structure-validation',
            'untranslated-source-validation', 'chinese-residue-validation', 'target-script-validation',
            'placeholder-validation', 'empty-translation-validation', 'translation-size-validation',
            'expansion-validation'} else 'validation-unavailable'
    return 'accepted'


def cached_unit_variants(seed, locale, source, approved_keys):
    result, total = [], 0
    for kind, rows in (('translation', seed.get('rows', {})), ('source-fallback', seed.get('source_fallbacks', {}))):
        for identity, row in rows.items():
            if not isinstance(row, dict) or row.get('source') != source: continue
            total += 1
            if len(result) >= MAX_UNIT_VARIANTS: continue
            language = row.get('language')
            known_language = isinstance(language, str) and language in SOURCE_LANGUAGES
            valid_hash = isinstance(identity, str) and re.fullmatch(r'[a-f0-9]{64}', identity) is not None
            matches = [markdown for markdown in (False, True) if known_language
                       and identity == unit_key(locale, source, language, markdown)]
            item = {'kind': kind, 'unit_sha256': identity if valid_hash else None,
                    'language': language if known_language else 'other', 'key_matches_markdown': matches,
                    'approved_fallback_member': valid_hash and identity in approved_keys if approved_keys is not None else None}
            if kind == 'translation':
                item.update(current_validation=unit_validation(source, row, locale, None),
                    approved_quantity_validation=unit_validation(source, row, locale, approved_quantity_issues))
            else:
                item['policy_matches'] = row.get('policy') == SOURCE_FALLBACK_VERSION
            result.append(item)
    return {'count': total, 'truncated': total > len(result), 'rows': result}


@contextmanager
def record_cache_misses():
    """Observe exact failed call arguments while retaining the original error.

    This single-threaded diagnostic always restores the original factory. The
    original no-inference translator still rejects every call; raw arguments
    remain local and are never included in the report.
    """
    original, attempts = publication.CacheOnly, []
    class RecordingCacheOnly(original):
        def __init__(self):
            self.calls = []
            attempts.append(self.calls)

        def translate(self, text, target, source=None, *, markdown=True):
            self.calls.append((text, target, source, markdown))
            return super().translate(text, target, source, markdown=markdown)
    publication.CacheOnly = RecordingCacheOnly
    try:
        yield attempts
    finally:
        publication.CacheOnly = original


def failed_unit_diagnostics(corpus, locale, seed, approved, replay, traced_calls):
    """Hash-only evidence for missing/rejected units; never authorization to reuse."""
    inventory = approved.get('source_fallback_unit_sha256')
    inventory_present = (isinstance(inventory, list) and all(isinstance(key, str)
        and re.fullmatch(r'[a-f0-9]{64}', key) for key in inventory))
    approved_keys = set(inventory) if inventory_present else None
    fallback_keys = set(seed.get('source_fallbacks', {}))
    result = {'seed_fallback_rows': len(fallback_keys),
        'approved_fallback_inventory_present': inventory_present,
        'approved_fallback_units': len(approved_keys) if inventory_present else None,
        'approved_fallback_keys_present': len(approved_keys & fallback_keys) if inventory_present else None,
        'approved_fallback_keys_absent': len(approved_keys - fallback_keys) if inventory_present else None,
        'seed_fallback_keys_extra': len(fallback_keys - approved_keys) if inventory_present else None,
        'traced_cache_miss_calls': len(traced_calls), 'failures': []}
    docs = {doc['url']: doc for doc in corpus['documents']}
    trace_index = 0
    for failure in replay['failures'][:MAX_DOCUMENTS]:
        field = failure.get('field')
        try:
            doc = docs[failure['url']]
            source, markdown, parent = failed_source_unit(doc, field)
        except (KeyError, IndexError, TypeError, ValueError):
            result['failures'].append({'code': 'unresolved-field'})
            continue
        language = extended_source_language(source)
        trace_matches = None
        if failure.get('code') == 'offline-approval-cache-miss':
            trace_matches = (trace_index < len(traced_calls)
                and traced_calls[trace_index] == (source, locale, language, markdown))
            trace_index += 1
        identity = unit_key(locale, source, language, markdown)
        row = seed.get('rows', {}).get(identity)
        fallback = seed.get('source_fallbacks', {}).get(identity)
        exact_row = isinstance(row, dict) and row.get('source') == source and row.get('language') == language
        exact_fallback = (isinstance(fallback, dict) and fallback.get('source') == source
            and fallback.get('language') == language and fallback.get('policy') == SOURCE_FALLBACK_VERSION)
        item = {'field': field, 'document_sha256': digest(doc['url'].encode()),
            'source_sha256': digest(source.encode()), 'source_bytes': len(source.encode()),
            'unit_sha256': identity, 'language': language if language in SOURCE_LANGUAGES else 'other',
            'markdown': markdown, 'actual_call_matches_resolved_field': trace_matches,
            'approved_fallback_member': identity in approved_keys if inventory_present else None,
            'exact_translation_key_present': identity in seed.get('rows', {}),
            'exact_translation_identity_matches': exact_row,
            'exact_fallback_key_present': identity in seed.get('source_fallbacks', {}),
            'exact_fallback_identity_matches': exact_fallback,
            'same_source_variants': cached_unit_variants(seed, locale, source, approved_keys)}
        if exact_row:
            item.update(current_validation=unit_validation(source, row, locale, None),
                approved_quantity_validation=unit_validation(source, row, locale, approved_quantity_issues))
        if parent is not None:
            item['whole_pipe_parent'] = {'source_sha256': digest(parent.encode()), 'source_bytes': len(parent.encode()),
                'variants': cached_unit_variants(seed, locale, parent, approved_keys)}
        result['failures'].append(item)
    return result


def compare(store, batch, locale, work, *, frozen_approval=False):
    work.mkdir()
    phase('candidate-source-read', store.restore_source, batch['generation'], work/'corpus.json')
    corpus = phase('candidate-source-validation', validated_corpus, work/'corpus.json')
    phase('candidate-read', store.restore_candidate, locale, batch['generation'], batch['candidates'][locale], work/'approved')
    approved, _ = phase('candidate-validation', verified_candidate, work/'approved', corpus)
    restored = phase('checkpoint-read', store.restore_checkpoint, locale, batch['generation'], work/'seed.json')
    if not restored.get('present'):
        return {'locale': locale, 'generation': batch['generation'], 'candidate': batch['candidates'][locale],
                'checkpoint_present': False, 'matches': False, 'failure_codes': {'checkpoint-absent': 1}}
    seed = json.loads((work/'seed.json').read_bytes())
    with record_cache_misses() as traced_attempts:
        proof = phase('candidate-replay', prove_approved_baseline, corpus, locale, work,
                      work/'seed.json', approved, allow_frozen=frozen_approval, require_match=False)
    replay = proof['manifest']
    replay_dir = proof['checkpoint'].with_suffix('')
    attempts = []
    for index, attempt in enumerate(proof['attempts']):
        manifest = json.loads((work/f'baseline-{index}'/'candidate-manifest.json').read_bytes())
        attempts.append({**attempt, 'approved_pages': len(approved['pages']),
            'replayed_pages': len(manifest['pages']), 'cache_hits': manifest['cache_hits'],
            'source_fallback_units': manifest.get('source_fallback_unit_count'),
            'failure_codes': dict(Counter(row['code'] for row in manifest['failures'])),
            'failed_unit_diagnostics': failed_unit_diagnostics(corpus, locale, seed, approved, manifest,
                traced_attempts[index] if index < len(traced_attempts) else [])})
    rejected, total = [], 0
    for key, row in seed['rows'].items():
        try:
            validate_text(row['source'], row['text'], locale, row['language'])
        except Exception as error:
            total += 1
            if len(rejected) < 30:
                diagnostic = {'unit_sha256': digest(str(key).encode()), 'code': safe_failure_code(error)}
                if diagnostic['code'] == 'financial-quantity-validation':
                    diagnostic['quantity_signature'] = quantity_signature(row['source'], row['text'], locale)
                rejected.append(diagnostic)
    before = {r['path']: r for r in approved['pages']}
    after = {r['path']: r for r in replay['pages']}
    differences = []
    for path in sorted(set(before) | set(after)):
        a, b = before.get(path), after.get(path)
        if a != b:
            difference = {'path_sha256': digest(path.encode()), 'approved_bytes': a.get('bytes') if a else None,
                          'replay_bytes': b.get('bytes') if b else None,
                          'approved_sha256': a.get('sha256') if a else None,
                          'replay_sha256': b.get('sha256') if b else None,
                          'descriptor_only': bool(a and b and a['sha256'] == b['sha256'])}
            if a: difference['approved_shape'] = html_shape(work/'approved'/path)
            if b: difference['replay_shape'] = html_shape(replay_dir/path)
            differences.append(difference)
    return {'locale': locale, 'generation': batch['generation'], 'candidate': batch['candidates'][locale],
            'quantity_contract': proof['quantity_contract'],
            'quantity_parser_sha256': proof['quantity_parser_sha256'], 'baseline_attempts': attempts,
            'checkpoint_sha256': restored['sha256'], 'matches': replay['status'] == 'complete-candidate'
                and replay['translation_calls_this_run'] == 0 and replay['files_sha256'] == approved['files_sha256'],
            'status': replay['status'], 'approved_pages': len(before), 'replayed_pages': len(after),
            'translation_calls': replay['translation_calls_this_run'],
            'failure_codes': dict(Counter(r['code'] for r in replay['failures'])),
            'approved_fallbacks': approved.get('source_fallback_unit_count'),
            'replayed_fallbacks': replay.get('source_fallback_unit_count'),
            'checkpoint_rows': len(seed['rows']), 'replayed_cache_hits': replay['cache_hits'],
            'rejected_rows': rejected, 'rejected_rows_total': total, 'changed_pages': differences[:MAX_DOCUMENTS]}


def audit_cached_rows(store, batches, corpora, owners, root):
    results = []
    for index, (batch, corpus) in enumerate(zip(batches, corpora, strict=True)):
        for locale in batch['candidates']:
            if not any(owners[locale, doc['url']] == index for doc in corpus['documents']): continue
            if len(results) >= MAX_CACHE_AUDITS: raise InspectionError('too-many-cache-audits')
            path = root/f'audit-{index}-{locale}.json'
            restored = phase('cache-audit-read', store.restore_checkpoint, locale, batch['generation'], path)
            if not restored.get('present'):
                results.append({'batch_index': index, 'locale': locale, 'checkpoint_present': False}); continue
            payload = json.loads(path.read_bytes()); signatures = []
            rejected = Counter()
            for row in payload['rows'].values():
                try: validate_text(row['source'], row['text'], locale, row['language'])
                except Exception as error:
                    code = safe_failure_code(error); rejected[code] += 1
                    if code == 'financial-quantity-validation' and len(signatures) < 30:
                        signatures.append(quantity_signature(row['source'], row['text'], locale))
            results.append({'batch_index': index, 'locale': locale, 'generation': batch['generation'],
                            'checkpoint_sha256': restored['sha256'], 'cached_rows': len(payload['rows']),
                            'rejected_codes': dict(rejected), 'quantity_signatures': signatures})
    return results


def compare_active_checkpoint(store, ledger, batch, locale, work, latest_result=None):
    """Prove the same immutable seed used by production without any R2 write."""
    outcome = {'matches': False, 'checkpoint_sha256': None, 'inference_calls': 0}
    try:
        checksum = active_checkpoint_sha(ledger, locale, batch['generation'], batch['candidates'][locale])
        outcome['checkpoint_sha256'] = checksum
    except Exception:
        return {**outcome, 'code': 'approved-checkpoint-receipt-invalid'}
    replay_work = work/'approved-checkpoint-replay'; replay_work.mkdir()
    try:
        restored = restore_active_checkpoint(store, ledger, locale, batch['generation'],
                                              batch['candidates'][locale], replay_work/'seed.json')
    except R2NotFound:
        return {**outcome, 'code': 'approved-checkpoint-missing'}
    except Exception:
        return {**outcome, 'code': 'approved-checkpoint-unavailable-or-invalid'}
    try:
        corpus = validated_corpus(work/'corpus.json')
        approved, _ = verified_candidate(work/'approved', corpus)
        if (isinstance(latest_result, dict) and latest_result.get('checkpoint_sha256') == checksum
            and (latest_result.get('locale'), latest_result.get('generation'), latest_result.get('candidate'))
                == (locale, batch['generation'], batch['candidates'][locale])
            and latest_result.get('baseline_attempts') and (work/'seed.json').is_file()
            and (work/'seed.json').read_bytes() == (replay_work/'seed.json').read_bytes()):
            # Both complete blobs were read and verified in this inspection.
            # The same seed/corpus/approved candidate has already traversed the
            # exact current/frozen proof; a second identical build adds nothing.
            return {**outcome, 'matches': latest_result['matches'],
                'code': 'matched' if latest_result['matches'] else 'approved-bytes-mismatch',
                'quantity_contract': latest_result['quantity_contract'],
                'baseline_attempts': latest_result['baseline_attempts'],
                'approved_pages': latest_result['approved_pages'], 'replayed_pages': latest_result['replayed_pages'],
                'cache_miss_attempts': latest_result['translation_calls'], 'failure_codes': latest_result['failure_codes'],
                'binding': restored['binding'], 'reused_verified_latest_replay': True}
        with record_cache_misses() as traced_attempts:
            proof = prove_approved_baseline(corpus, locale, replay_work, replay_work/'seed.json',
                                           approved, allow_frozen=True, require_match=False)
    except Exception:
        return {**outcome, 'code': 'approved-baseline-unavailable-or-invalid'}
    manifest = proof['manifest']
    seed = json.loads((replay_work/'seed.json').read_bytes())
    attempts = []
    for index, attempt in enumerate(proof['attempts']):
        replay = json.loads((replay_work/f'baseline-{index}'/'candidate-manifest.json').read_bytes())
        attempts.append({**attempt, 'failed_unit_diagnostics': failed_unit_diagnostics(
            corpus, locale, seed, approved, replay, traced_attempts[index] if index < len(traced_attempts) else [])})
    return {**outcome, 'matches': proof['matches'], 'code': 'matched' if proof['matches'] else 'approved-bytes-mismatch',
        'quantity_contract': proof['quantity_contract'], 'baseline_attempts': attempts,
        'approved_pages': len(approved['pages']), 'replayed_pages': len(manifest['pages']),
        'cache_miss_attempts': manifest['translation_calls_this_run'],
        'failure_codes': dict(Counter(row['code'] for row in manifest['failures'])),
        'binding': restored['binding'], 'reused_verified_latest_replay': False}


def read_identity():
    with requests.get(ORIGIN+'/.well-known/edge-state', timeout=(10, 30), allow_redirects=False, stream=True) as response:
        response.raise_for_status()
        raw = response.raw.read(MAX_STATE_BYTES + 1, decode_content=True)
        if len(raw) > MAX_STATE_BYTES: raise InspectionError('oversized-state')
        value = json.loads(raw)
    if not isinstance(value, dict): raise InspectionError('invalid-state')
    return value


def inspect(store, target, expected_release, identity):
    # Refuse a stale deployment identity before reading any private source.
    if identity.get('release_id') != expected_release:
        raise InspectionError('active-release-changed')
    store = R2Store(ReadOnlyClient(store.client), store.bucket, store.prefix)
    active_ledger = phase('active-ledger-read', read_active_ledger, store, identity)
    active = checked_batches(active_ledger['batches'])
    active_approvals = bindings(active)
    batches = checked_batches(active + ([target] if target is not None else []))
    identity_summary = {'mode': 'active-only' if target is None else 'candidate',
                        'active_release': expected_release}
    if not batches:
        return {**identity_summary, 'status': 'no-active-batches', 'production_writes': 0,
                'inference_calls': 0, 'results': [], 'carry_forward_cache_audit': []}
    if len(batches) > MAX_BATCHES: raise InspectionError('too-many-batches')
    owners = {}
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        corpora = []
        for index, batch in enumerate(batches):
            path = root/f'source-{index}.json'
            phase('owner-source-read', store.restore_source, batch['generation'], path)
            corpus = phase('owner-source-validation', validated_corpus, path)
            corpora.append(corpus)
            for locale in batch['candidates']:
                for doc in corpus['documents']: owners[locale, doc['url']] = index
        def report(status, results):
            result = {**identity_summary, 'status': status, 'production_writes': 0,
                      'inference_calls': 0, 'results': results,
                      'checked_candidates': len(results), 'selected_candidates': selected_candidates}
            try:
                result['carry_forward_cache_audit'] = audit_cached_rows(store, batches, corpora, owners, root)
            except Exception as error:
                if target is not None:
                    raise
                # The first exact mismatch remains useful even if a later
                # optional cache audit is unavailable. Never print its text.
                result.update(carry_forward_cache_audit=[], cache_audit_complete=False,
                    cache_audit_code='cache-audit-bound' if isinstance(error, InspectionError)
                    and error.code == 'too-many-cache-audits' else 'cache-audit-unavailable')
            else:
                result['cache_audit_complete'] = True
            return result
        results = []
        selected_candidates = sum(any(owners[locale, doc['url']] == index for doc in corpus['documents'])
            for index, (batch, corpus) in enumerate(zip(batches, corpora, strict=True)) for locale in batch['candidates'])
        for index, (batch, corpus) in enumerate(zip(batches, corpora, strict=True)):
            for locale in batch['candidates']:
                if not any(owners[locale, d['url']] == index for d in corpus['documents']): continue
                frozen = (batch['generation'], locale, batch['candidates'][locale]) in active_approvals
                work = root/f'{index}-{locale}'
                try:
                    result = compare(store, batch, locale, work, frozen_approval=frozen)
                except PhaseError:
                    if not frozen: raise
                    result = {'locale': locale, 'generation': batch['generation'], 'candidate': batch['candidates'][locale],
                              'matches': False, 'code': 'latest-comparison-unavailable'}
                result['publication_matches'] = result['matches']
                if frozen:
                    result['approved_checkpoint_replay'] = compare_active_checkpoint(store, active_ledger, batch, locale, work, result)
                    result['publication_matches'] = result['approved_checkpoint_replay']['matches']
                result['batch_index'] = index
                result['target_candidate'] = batch == target and locale in target['candidates']
                results.append(result)
                if not result['publication_matches']:
                    return report('mismatch', results)
        return report('all-matched', results)


def main():
    parser = argparse.ArgumentParser()
    for name in ('generation', 'locale', 'candidate'): parser.add_argument('--'+name, default='')
    parser.add_argument('--active-release', required=True)
    parser.add_argument('--active-only', action='store_true')
    args = parser.parse_args()
    try:
        supplied = (args.generation, args.locale, args.candidate)
        if (args.active_only and any(supplied)) or (not args.active_only and not all(supplied)):
            raise InspectionError('invalid-inspection-mode')
        target = None if args.active_only else checked_batches([
            {'generation': args.generation, 'candidates': {args.locale: args.candidate}}])[0]
        if re.fullmatch(r'[0-9a-f]{32}', args.active_release) is None: raise InspectionError('invalid-release')
        identity = phase('active-identity-read', read_identity)
        # Identity is checked before initializing the private storage client.
        if identity.get('release_id') != args.active_release: raise InspectionError('active-release-changed')
        store = phase('storage-configuration', R2Store.from_env, '_extended-locales/v1')
        result = inspect(store, target, args.active_release, identity)
    except Exception as error:
        code = error.code if isinstance(error, InspectionError) else 'storage-integrity' if isinstance(error, R2StoreError) else 'inspection-failed'
        error_type = error.error_type if isinstance(error, PhaseError) else type(error).__name__
        if re.fullmatch(r'[A-Za-z][A-Za-z0-9_]{0,79}', error_type) is None: error_type = 'Exception'
        print(json.dumps({'status': 'failed', 'code': code, 'stage': getattr(error, 'stage', 'input-or-summary'),
                          'error_type': error_type, 'production_writes': 0, 'inference_calls': 0}, sort_keys=True))
        return 1
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
