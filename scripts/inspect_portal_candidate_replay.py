"""Read-only, no-inference comparison of approved candidate and current replay.

Only hashes, counts and fixed error categories leave this diagnostic. Candidate
HTML, source and checkpoint text remain in the temporary runner directory.
"""
from __future__ import annotations

import argparse
from collections import Counter
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import tempfile
import unicodedata

import requests

from assemble_portal_extended_locales import verified_candidate
from build_portal_extended_locales import build, validate_text, safe_failure_code
from portal_extended_locales import ORIGIN, daily_corpus_day, digest, validate_corpus
from portal_extended_publication import CacheOnly, checked_batches, read_active_batches, prove_approved_baseline
from portal_extended_r2 import R2Store, R2StoreError
from financial_quantity_integrity import quantities
from portal_approved_quantity_contract import CONTRACT_ID, PARSER_SHA256, bindings, quantity_issues as approved_quantity_issues

MAX_BATCHES = 36
MAX_DOCUMENTS = 24
MAX_STATE_BYTES = 65536
CALENDAR_MONTH_ALIASES = json.loads((Path(__file__).parent/'portal_extended_calendar_months.json').read_text(encoding='utf-8'))['languages']
BN_MONTH_ALIASES = CALENDAR_MONTH_ALIASES['bn']
MAX_CACHE_AUDITS = 128


class InspectionError(ValueError):
    def __init__(self, code):
        super().__init__(code)
        self.code = code


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
    proof = phase('candidate-replay', prove_approved_baseline, corpus, locale, work,
                  work/'seed.json', approved, allow_frozen=frozen_approval, require_match=False)
    replay = proof['manifest']
    replay_dir = proof['checkpoint'].with_suffix('')
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
            'quantity_parser_sha256': proof['quantity_parser_sha256'], 'baseline_attempts': proof['attempts'],
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
    active = checked_batches(phase('active-ledger-read', read_active_batches, store, identity))
    active_approvals = bindings(active)
    batches = checked_batches(active + [target])
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
        results = []
        for index, (batch, corpus) in enumerate(zip(batches, corpora, strict=True)):
            for locale in batch['candidates']:
                if not any(owners[locale, d['url']] == index for d in corpus['documents']): continue
                result = compare(store, batch, locale, root/f'{index}-{locale}',
                                 frozen_approval=(batch['generation'], locale, batch['candidates'][locale]) in active_approvals)
                result['batch_index'] = index
                result['target_candidate'] = batch == target and locale in target['candidates']
                results.append(result)
                if not result['matches']:
                    return {'status': 'mismatch', 'production_writes': 0, 'inference_calls': 0, 'results': results,
                            'carry_forward_cache_audit': audit_cached_rows(store, batches, corpora, owners, root)}
        return {'status': 'all-matched', 'production_writes': 0, 'inference_calls': 0, 'results': results,
                'carry_forward_cache_audit': audit_cached_rows(store, batches, corpora, owners, root)}


def main():
    parser = argparse.ArgumentParser()
    for name in ('generation', 'locale', 'candidate', 'active-release'): parser.add_argument('--'+name, required=True)
    args = parser.parse_args()
    try:
        target = checked_batches([{'generation': args.generation, 'candidates': {args.locale: args.candidate}}])[0]
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
