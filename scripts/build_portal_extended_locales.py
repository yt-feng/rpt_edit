#!/usr/bin/env python3
"""Build independently resumable locale candidates using the pinned CPU model.

A candidate is never indexed here. Only a complete, approved, byte-verified
candidate can be merged into an inactive site by the companion assembly tool.
"""
from __future__ import annotations
import argparse
import json
import os
from pathlib import Path
import re
import time
from typing import Protocol
from compare_hymt_translation import SCRIPT_PATTERNS, require_actions
from offline_translation import (
    OfflineTranslationError, OfflineTranslationValidationError, TranslationBudgetExceeded,
    OfflineTranslator, MODEL_ID, PROVIDER, _detect_source,
)
from financial_quantity_integrity import quantity_issues
from portal_extended_locales import (
    ADDITIONAL, COPY, ORIGIN, ExpansionError, digest, file_for_url, render_document,
    select_locales, stable_bytes, validate_corpus, daily_corpus_day,
)

MAX_CHECKPOINT_BYTES = 8 * 1024 * 1024
CHECKPOINT_VERSION = 'extended-static-v2'
SOURCE_FALLBACK_VERSION = 'exact-source-v1'
MAX_TRANSLATION_SECONDS = 4 * 60 * 60
MAX_PUBLIC_TRANSLATION_DIAGNOSTICS = 20
SEO_QUANTITY_POLICY = 'seo-advisory-v1'
NUMERIC_FALLBACK_CODES = frozenset({'offline-quantity-validation', 'financial-quantity-validation'})
QUANTITY_DIAGNOSTIC_KINDS = frozenset({
    'number', 'currency', 'percent', 'percentage_points', 'date', 'invalid_date',
    'month', 'month_day', 'quarter', 'half', 'five_year_plan', 'shopping_event',
})
PUBLIC_VALIDATION_CODES = frozenset({
    'offline-quantity-validation', 'offline-placeholder-validation', 'offline-markdown-validation',
    'offline-target-script-validation', 'offline-empty-validation', 'offline-token-limit',
    'offline-unicode-validation', 'offline-validation',
})


def public_quantity_signature(value):
    """Expose fact types and counts, never numeric values or currency labels."""
    if not isinstance(value, dict) or not isinstance(value.get('rows'), list):
        return None
    rows = value['rows']
    total = value.get('total_rows')
    if (len(rows) > 20 or type(total) is not int or total < len(rows)
            or type(value.get('truncated')) is not bool):
        return None
    canonical, counts = [], {}
    for row in rows:
        if (not isinstance(row, dict) or not isinstance(row.get('kind'), str)
                or row['kind'] not in QUANTITY_DIAGNOSTIC_KINDS
                or type(row.get('count')) is not int or row['count'] < 1
                or not isinstance(row.get('values'), list) or len(row['values']) > 3
                or any(item is not None and (not isinstance(item, str) or len(item) > 128)
                       for item in row['values'])):
            return None
        kind = row['kind']
        counts[kind] = counts.get(kind, 0) + row['count']
        canonical.append({'kind': kind, 'values': row['values'], 'count': row['count']})
    canonical.sort(key=stable_bytes)
    return {'signature_sha256': digest(stable_bytes(canonical)), 'type_counts': counts,
            'total_rows': total, 'truncated': value['truncated'] or total != len(rows)}


def public_translation_diagnostics(translator, locale):
    """Summarize existing terminal failures without rerunning any translation."""
    records = getattr(translator, 'failure_diagnostics', [])
    records = records if isinstance(records, list) else []
    result = []
    for row in records[:MAX_PUBLIC_TRANSLATION_DIAGNOSTICS]:
        if (not isinstance(row, dict) or row.get('target_language') != locale
                or not isinstance(row.get('source_sha256'), str)
                or re.fullmatch(r'[a-f0-9]{64}', row['source_sha256']) is None):
            continue
        response = row.get('response_sha256')
        if response is not None and (not isinstance(response, str)
                                    or re.fullmatch(r'[a-f0-9]{64}', response) is None):
            continue
        quantities = row.get('quantities')
        quantities = quantities if isinstance(quantities, dict) else {}
        code = row.get('failure_code')
        result.append({'source_sha256': row['source_sha256'], 'response_sha256': response,
            'target_language': locale, 'failure_type': code if isinstance(code, str) and code in PUBLIC_VALIDATION_CODES else 'offline-validation',
            'quantities': {side: public_quantity_signature(quantities.get(side))
                           for side in ('source', 'response', 'missing', 'extra')}})
    total = getattr(translator, 'validation_failure_count', len(records))
    total = total if type(total) is int and total >= len(records) else len(records)
    return {'terminal_translation_diagnostics': result, 'terminal_validation_failure_count': total,
            'maximum_reported_translation_diagnostics': MAX_PUBLIC_TRANSLATION_DIAGNOSTICS,
            'translation_diagnostics_truncated': total > len(result)}


def validate_budget(seconds: int) -> int:
    if not 1 <= seconds <= MAX_TRANSLATION_SECONDS:
        raise ExpansionError(f'Time budget must be 1..{MAX_TRANSLATION_SECONDS} seconds')
    return seconds


def reject_symlinks(path: Path) -> None:
    # The temporary directory on macOS is exposed through /var -> /private/var.
    # Reject the candidate/checkpoint itself and anything below it, while not
    # treating that normal system alias in an otherwise valid parent path as a
    # candidate symlink.
    if path.is_symlink():
        raise ExpansionError('Symlink paths are forbidden for locale candidates/checkpoints')
    if path.is_dir() and any(item.is_symlink() for item in path.rglob('*')):
        raise ExpansionError('Symlink paths are forbidden for locale candidates/checkpoints')

class Translator(Protocol):
    def translate(self, text: str, target: str, source: str | None = None, *, markdown: bool = True) -> str: ...


class TranslationUnitError(Exception):
    """A validation failure annotated with a bounded document field name."""

    def __init__(self, field: str, error: Exception):
        super().__init__(str(error))
        self.field = field
        self.error = error


def safe_failure_code(error: Exception) -> str:
    """Return a bounded diagnostic code without exposing model/source text."""
    if isinstance(error, TranslationUnitError):
        error = error.error
    name, message = type(error).__name__, str(error).casefold()
    if isinstance(error, TranslationBudgetExceeded): return 'time-budget'
    if isinstance(error, TimeoutError): return 'offline-request-timeout'
    if isinstance(error, OfflineTranslationError) and not isinstance(error, OfflineTranslationValidationError):
        return error.code if re.fullmatch(r'offline-[a-z-]+|offline-http-[0-9]{3}(?:-[a-z0-9-]+)?', error.code) else 'offline-runtime'
    if name == 'OfflineTranslationValidationError':
        for needle, code in (
            ('quantity', 'offline-quantity-validation'),
            ('placeholder', 'offline-placeholder-validation'),
            ('markdown', 'offline-markdown-validation'),
            ('target script', 'offline-target-script-validation'),
            ('empty', 'offline-empty-validation'),
            ('token limit', 'offline-token-limit'),
            ('unicode', 'offline-unicode-validation'),
        ):
            if needle in message:
                return code
        return 'offline-validation'
    if name == 'ExpansionError':
        for needle, code in (
            ('financial quantity', 'financial-quantity-validation'),
            ('table column', 'table-structure-validation'),
            ('untranslated source', 'untranslated-source-validation'),
            ('chinese residue', 'chinese-residue-validation'),
            ('target script', 'target-script-validation'),
            ('unrestored', 'placeholder-validation'),
            ('empty translated', 'empty-translation-validation'),
            ('unbounded', 'translation-size-validation'),
        ):
            if needle in message:
                return code
        return 'expansion-validation'
    return {
        'TimeoutError': 'time-budget',
        'OfflineTranslationError': 'offline-runtime',
    }.get(name, 'translation-error')


def extended_source_language(text: str) -> str:
    """Treat mixed Chinese/English public metadata as Chinese source content."""
    if re.search(r'[\u3400-\u9fff]', text):
        return 'zh'
    return _detect_source(text)


def quantity_is_advisory(locale, quantity_validator=None, quantity_policy=None):
    if quantity_policy not in (None, 'strict', 'advisory'):
        raise ExpansionError('Unsupported quantity policy')
    # Historical replay validators always retain their explicit exact contract.
    return quantity_validator is None and (quantity_policy == 'advisory'
        or (quantity_policy is None and locale in ADDITIONAL))


def validate_text(source: str, translated: str, locale: str, source_language: str, *, quantity_validator=None,
                  quantity_policy=None) -> bool:
    """Validate display contracts; return an advisory numeric mismatch flag.

    Additional locales default to numeric prose advisories. English SEO callers
    opt in explicitly; other callers and historical replay validators retain
    their blocking contract. Warning counts never contain source values.
    """
    if not isinstance(translated, str) or not translated.strip(): raise ExpansionError('Empty translated text')
    if re.search(r'[\ufffd\ud800-\udfff]', translated): raise ExpansionError('Invalid Unicode translation')
    if len(translated) > max(2000, len(source) * 12): raise ExpansionError('Unbounded translation expansion')
    if re.search(r'__(?:KC_PH_|HYMTPH_)\d+__', translated): raise ExpansionError('Unrestored protected identifier')
    validator = quantity_issues if quantity_validator is None else quantity_validator
    advisory = quantity_is_advisory(locale, quantity_validator, quantity_policy)
    try:
        quantity_warning = bool(validator(source, translated, source_language, locale))
    except Exception:
        if not advisory:
            raise
        # A prose diagnostic must not block a structurally valid SEO page.
        quantity_warning = True
    if quantity_warning and not advisory: raise ExpansionError('Financial quantity validation failed')
    if source.count('|') != translated.count('|'): raise ExpansionError('Table column boundaries changed')
    clean = re.sub(r'https?://\S+|\b[A-Z][A-Z0-9.-]{0,7}\b', '', source).strip()
    if not any(c.isalpha() for c in clean): return quantity_warning
    # Source English text can legitimately stay unchanged on /en/. This does
    # not excuse unchanged Chinese on any additional target-language page.
    source_is_english = not re.search(r'[\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06ff]', source.replace('KC桌面', ''))
    same_language = locale == 'en' and source_is_english
    source_key = re.sub(r'\W', '', source).casefold()
    translated_key = re.sub(r'\W', '', translated).casefold()
    if not same_language and source_key and source_key in translated_key and len(clean) > 12:
        raise ExpansionError('Untranslated source text')
    if not re.search(SCRIPT_PATTERNS[locale], translated): raise ExpansionError('Target script is missing')
    if re.search(r'[\u3400-\u9fff]', translated) and locale not in {'zh-Hant', 'yue'}:
        # Names may retain a small parenthetic Han label. Paragraph-sized Han
        # residue is not accepted as successful localization.
        if len(re.findall(r'[\u3400-\u9fff]', translated)) > 12: raise ExpansionError('Untranslated Chinese residue')
    return quantity_warning


class Memo:
    def __init__(self, path: Path, locale: str, translator: Translator, deadline: float, *, source_generation: str | None = None,
                 allow_source_fallback: bool = False, seed_checkpoint: Path | None = None, quantity_validator=None,
                 quantity_policy=None):
        reject_symlinks(path)
        self.path, self.locale, self.translator, self.deadline = path, locale, translator, deadline
        self.quantity_validator = quantity_validator
        self.quantity_policy = quantity_policy
        self.quantity_advisory = quantity_is_advisory(locale, quantity_validator, quantity_policy)
        self.source_generation = source_generation
        self.allow_source_fallback = allow_source_fallback
        self.source_fallbacks = {}
        self.fallback_keys = set()
        self.fallback_uses = 0
        self.rejected = {}
        self.rows = {}
        self.seed_rows, self.seed_fallbacks = {}, {}
        self.calls = self.hits = 0
        self.quantity_warning_keys = set()
        self.quantity_warning_occurrences = 0
        if path.is_file():
            if path.stat().st_size > MAX_CHECKPOINT_BYTES: raise ExpansionError('Checkpoint is too large')
            payload = json.loads(path.read_text())
            if (payload.get('model') == MODEL_ID and payload.get('locale') == locale
                and payload.get('version') == CHECKPOINT_VERSION
                and (source_generation is None or payload.get('source_generation') in {None, source_generation})):
                self.rows = payload.get('rows', {})
                if not isinstance(self.rows, dict): raise ExpansionError('Invalid checkpoint rows')
                self.source_fallbacks = payload.get('source_fallbacks', {})
                if not isinstance(self.source_fallbacks, dict): raise ExpansionError('Invalid source fallback rows')
        if seed_checkpoint is not None:
            reject_symlinks(seed_checkpoint)
            if seed_checkpoint.stat().st_size > MAX_CHECKPOINT_BYTES: raise ExpansionError('Seed checkpoint too large')
            seed = json.loads(seed_checkpoint.read_text())
            if seed.get('model') != MODEL_ID or seed.get('locale') != locale or seed.get('version') != CHECKPOINT_VERSION:
                raise ExpansionError('Seed checkpoint identity mismatch')
            self.seed_rows, self.seed_fallbacks = seed.get('rows', {}), seed.get('source_fallbacks', {})
            if not isinstance(self.seed_rows, dict) or not isinstance(self.seed_fallbacks, dict):
                raise ExpansionError('Invalid seed checkpoint rows')

    def key(self, source: str, language: str, *, markdown: bool = False) -> str:
        parts = [CHECKPOINT_VERSION, MODEL_ID, self.locale, language, source]
        if markdown:
            parts.append('markdown')
        return digest(stable_bytes(parts))

    def get(self, source: str, language: str = 'zh', *, markdown: bool = False, validate_result=None) -> str:
        if not source.strip(): return source
        key = self.key(source, language, markdown=markdown)
        row = self.rows.get(key, self.seed_rows.get(key))
        if isinstance(row, dict) and row.get('source') == source and row.get('language') == language:
            try:
                warning = validate_text(source, row.get('text'), self.locale, language,
                                        quantity_validator=self.quantity_validator, quantity_policy=self.quantity_policy)
                if validate_result is not None: validate_result(row['text'])
                self.record_quantity_warning(key, warning)
                self.hits += 1
                self.rows[key] = row
                return row['text']
            except ExpansionError:
                self.rows.pop(key, None)
                # A stricter caller contract can reject a row accepted by the
                # shared model adapter. Evict that exact adapter unit as well,
                # so resuming cannot immediately return the same bad text.
                discard = getattr(self.translator, 'discard_translation', None)
                if callable(discard): discard(source, self.locale, language, markdown=markdown)
        fallback = self.source_fallbacks.get(key, self.seed_fallbacks.get(key))
        if (self.allow_source_fallback and isinstance(fallback, dict)
            and fallback.get('source') == source and fallback.get('language') == language
            and fallback.get('policy') == SOURCE_FALLBACK_VERSION):
            self.fallback_keys.add(key)
            self.source_fallbacks[key] = fallback
            self.fallback_uses += 1
            return source
        if key in self.rejected:
            raise self.rejected[key]
        if time.monotonic() >= self.deadline: raise TranslationBudgetExceeded('Local translation time budget reached')
        diagnostics = getattr(self.translator, 'failure_diagnostics', [])
        diagnostic_start = len(diagnostics) if isinstance(diagnostics, list) else 0
        try:
            self.calls += 1
            translated = self.translator.translate(source, target=self.locale, source=language, markdown=markdown)
            warning = validate_text(source, translated, self.locale, language,
                                    quantity_validator=self.quantity_validator, quantity_policy=self.quantity_policy)
            if validate_result is not None: validate_result(translated)
        except (OfflineTranslationValidationError, ExpansionError) as error:
            # Attach only the existing fixed category to diagnostics already
            # captured by the adapter. Never retain a rejected response here.
            diagnostics = getattr(self.translator, 'failure_diagnostics', [])
            if isinstance(diagnostics, list):
                for row in diagnostics[diagnostic_start:MAX_PUBLIC_TRANSLATION_DIAGNOSTICS]:
                    if isinstance(row, dict): row['failure_code'] = safe_failure_code(error)
            discard = getattr(self.translator, 'discard_translation', None)
            if callable(discard): discard(source, self.locale, language, markdown=markdown)
            if not self.allow_source_fallback:
                self.rejected[key] = error
                raise
            # Match the established ko/ja/ar source-fallback policy. Rejected
            # model text is never a translation row, nor rendered or persisted.
            self.source_fallbacks[key] = {'source': source, 'language': language,
                'policy': SOURCE_FALLBACK_VERSION, 'code': safe_failure_code(error)}
            self.fallback_keys.add(key)
            self.fallback_uses += 1
            self.save()
            return source
        self.source_fallbacks.pop(key, None)
        self.record_quantity_warning(key, warning)
        self.rows[key] = {'source': source, 'language': language, 'text': translated}
        self.save()
        return translated

    def record_quantity_warning(self, key, warning):
        if warning and self.quantity_advisory:
            self.quantity_warning_keys.add(key)
            self.quantity_warning_occurrences += 1

    def save(self):
        reject_symlinks(self.path)
        reject_symlinks(self.path.with_suffix('.tmp'))
        payload = {'model': MODEL_ID, 'locale': self.locale, 'version': CHECKPOINT_VERSION, 'rows': self.rows}
        if self.source_fallbacks:
            payload['source_fallbacks'] = self.source_fallbacks
        if self.source_generation is not None:
            payload['source_generation'] = self.source_generation
        raw = stable_bytes(payload)
        if len(raw) > MAX_CHECKPOINT_BYTES: raise ExpansionError('Checkpoint exceeds storage budget')
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix('.tmp')
        temporary.write_bytes(raw); temporary.replace(self.path)


def translate_document(doc: dict, memo: Memo) -> dict:
    # English UI literals and English report titles get explicit English source
    # context; Chinese prose is not translated via a pivot or paid fallback.
    def translate(text, *, markdown=False, field='unit'):
        if '|' in text:
            # Public source headings/lists use a literal pipe as a title
            # separator (for example, ``title | KC桌面``), not an HTML table.
            # Keep that structural byte outside model inference while each
            # side remains an independently validated translation unit.
            return '|'.join(translate(part, markdown=markdown, field=f'{field}.part{index}')
                            for index, part in enumerate(text.split('|')))
        try:
            language = extended_source_language(text)
            return memo.get(text, language, markdown=markdown)
        except TranslationBudgetExceeded:
            raise
        except Exception as error:
            raise TranslationUnitError(field, error) from error
    return {'title': translate(doc['title'], field='title'),
            'description': translate(doc['description'], field='description'),
            'copy': {key: translate(value, field=f'copy.{key}') for key, value in COPY.items()},
            'blocks': [{'tag': b['tag'], 'text': translate(
                b['text'], markdown=b['tag'] == 'tr' or '|' in b['text'], field=f'block.{index}.{b["tag"]}')}
                       for index, b in enumerate(doc['blocks'])],
            'links': [{'url': row['url'], 'label': translate(row['label'], field=f'link.{index}')}
                      for index, row in enumerate(doc['links'])]}


def build(corpus: dict, locale: str, output: Path, checkpoint: Path, translator: Translator,
          *, budget_seconds=MAX_TRANSLATION_SECONDS, origin=ORIGIN, allow_source_fallback=False,
          seed_checkpoint: Path | None = None, quantity_validator=None) -> dict:
    if locale not in ADDITIONAL: raise ExpansionError('Not an additional locale')
    docs = validate_corpus(corpus, origin=origin)
    if origin + '/' not in {doc['url'] for doc in docs} and not daily_corpus_day(corpus):
        raise ExpansionError('A localized homepage source is required')
    reject_symlinks(output)
    reject_symlinks(checkpoint)
    if output.exists() and any(output.iterdir()): raise ExpansionError('Candidate output must be empty; never overwrite an active release')
    output.mkdir(parents=True, exist_ok=True)
    memo = Memo(checkpoint, locale, translator, time.monotonic() + budget_seconds,
                source_generation=corpus['documents_sha256'], allow_source_fallback=allow_source_fallback,
                seed_checkpoint=seed_checkpoint, quantity_validator=quantity_validator)
    set_deadline = getattr(translator, 'set_deadline', None)
    if callable(set_deadline): set_deadline(memo.deadline)
    # Materialize an empty or resumed checkpoint before the first model call.
    # A runner interruption or first-call failure must still leave a durable,
    # honest resume point; this contains no fabricated translation rows.
    memo.save()
    translated, failures, timed_out = {}, [], False
    for doc in docs:
        try: translated[doc['url']] = translate_document(doc, memo)
        except TranslationBudgetExceeded:
            timed_out = True; break
        except Exception as error:
            # Persist accepted units and record a bounded error category. Do not
            # emit partial pages or serialize raw model responses to CI logs.
            root_error = error.error if isinstance(error, TranslationUnitError) else error
            failures.append({'url': doc['url'], 'error': type(root_error).__name__,
                             'code': safe_failure_code(error),
                             'field': error.field if isinstance(error, TranslationUnitError) else 'document'})
    memo.save()
    complete_urls = set(translated)
    records = []
    for doc in docs:
        if doc['url'] not in translated: continue
        relative = Path(locale) / file_for_url(doc['url'], origin=origin)
        target = output / relative
        target.parent.mkdir(parents=True, exist_ok=True)
        page = render_document(doc, translated[doc['url']], locale, complete_urls, origin=origin)
        target.write_text(page, encoding='utf-8')
        records.append({'path': relative.as_posix(), 'source_url': doc['url'],
                        'source_content_sha256': doc['content_sha256'],
                        'source_html_sha256': doc['source_html_sha256'],
                        'sha256': digest(target.read_bytes()), 'bytes': target.stat().st_size})
    complete = len(records) == len(docs) and not failures and not timed_out
    manifest = {'schema_version': 1, 'locale': locale, 'origin': origin,
                'provider': PROVIDER, 'model': MODEL_ID, 'paid_provider_requests': 0,
                'status': 'complete-candidate' if complete else 'incomplete-candidate',
                'indexable': False, 'semantic_review': 'not-performed',
                'source_documents_sha256': corpus['documents_sha256'],
                'source_document_count': len(docs), 'completed_page_count': len(records),
                'translation_calls_this_run': memo.calls, 'cache_hits': memo.hits,
                'translation_policy': 'validated-units-with-source-fallback' if allow_source_fallback else 'strict',
                'translation_complete': complete and not memo.fallback_keys,
                'source_fallback_unit_count': len(memo.fallback_keys),
                'source_fallback_unit_sha256': sorted(memo.fallback_keys),
                'source_fallback_occurrences': memo.fallback_uses,
                'source_fallback_codes': sorted({memo.source_fallbacks[key]['code'] for key in memo.fallback_keys}),
                'budget_exhausted': timed_out, 'failures': failures, 'pages': records,
                'files_sha256': digest(stable_bytes(records))}
    if quantity_validator is None and locale in ADDITIONAL:
        manifest.update(quantity_validation_policy=SEO_QUANTITY_POLICY,
                        quantity_warning_unit_count=len(memo.quantity_warning_keys),
                        quantity_warning_occurrences=memo.quantity_warning_occurrences,
                        numeric_source_fallback_unit_count=sum(
                            memo.source_fallbacks[key]['code'] in NUMERIC_FALLBACK_CODES for key in memo.fallback_keys))
    (output / 'candidate-manifest.json').write_bytes(stable_bytes(manifest))
    return manifest


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument('--list-locales', action='store_true')
    parser.add_argument('--locales', default='all-supported')
    parser.add_argument('--corpus', type=Path)
    parser.add_argument('--locale')
    parser.add_argument('--output', type=Path)
    parser.add_argument('--checkpoint', type=Path)
    parser.add_argument('--seed-checkpoint', type=Path, help='Verified private R2 memo; reuse only exact validated units')
    parser.add_argument('--seconds', type=int, default=MAX_TRANSLATION_SECONDS)
    parser.add_argument('--allow-source-fallback', action='store_true',
                        help='Keep exact source units on content validation failure, like ko/ja/ar; never keep rejected model output')
    args = parser.parse_args()
    if args.list_locales:
        print(json.dumps({'locale': list(select_locales(args.locales))})); return 0
    if not all((args.corpus, args.locale, args.output, args.checkpoint)): parser.error('corpus, locale, output and checkpoint are required')
    require_actions()
    if os.environ.get('KC_PUBLIC_REPOSITORY') != 'true': raise ExpansionError('Translation requires an explicitly verified public repository')
    validate_budget(args.seconds)
    if args.corpus.stat().st_size > 32 * 1024 * 1024: raise ExpansionError('Corpus too large')
    corpus = json.loads(args.corpus.read_text())
    translator = OfflineTranslator(validation_attempts=1 if args.allow_source_fallback else 3,
                                   quantity_policy='advisory')
    result = build(corpus, args.locale, args.output, args.checkpoint, translator,
                   budget_seconds=args.seconds, allow_source_fallback=args.allow_source_fallback,
                   seed_checkpoint=args.seed_checkpoint)
    summary = {key: result[key] for key in ('locale', 'status', 'source_document_count', 'completed_page_count', 'paid_provider_requests', 'budget_exhausted')}
    summary['failure_count'] = len(result.get('failures') or [])
    for key in ('translation_policy', 'translation_complete', 'source_fallback_unit_count',
                'source_fallback_occurrences', 'source_fallback_codes', 'translation_calls_this_run', 'cache_hits'):
        summary[key] = result[key]
    for key in ('quantity_validation_policy', 'quantity_warning_unit_count', 'quantity_warning_occurrences',
                'numeric_source_fallback_unit_count'):
        summary[key] = result[key]
    summary['failure_types'] = sorted({str(row.get('error')) for row in result.get('failures') or []})
    summary['failure_codes'] = sorted({str(row.get('code')) for row in result.get('failures') or []})
    summary['failure_fields'] = sorted({str(row.get('field')) for row in result.get('failures') or []})
    summary['failure_field_codes'] = {
        field: sorted({str(row.get('code')) for row in result.get('failures') or []
                       if str(row.get('field')) == field})
        for field in sorted({str(row.get('field')) for row in result.get('failures') or []})
    }
    summary.update(public_translation_diagnostics(translator, args.locale))
    print(json.dumps(summary))
    return 0 if result['status'] == 'complete-candidate' else 75 if result['budget_exhausted'] and not result['failures'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
