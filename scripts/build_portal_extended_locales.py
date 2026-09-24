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
    OfflineTranslationValidationError, OfflineTranslator, MODEL_ID, PROVIDER, _detect_source,
)
from financial_quantity_integrity import quantity_issues
from portal_extended_locales import (
    ADDITIONAL, COPY, ORIGIN, ExpansionError, digest, file_for_url, render_document,
    select_locales, stable_bytes, validate_corpus,
)

MAX_CHECKPOINT_BYTES = 8 * 1024 * 1024
CHECKPOINT_VERSION = 'extended-static-v2'
MAX_QUANTITY_RETRIES = 1


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
    if name == 'OfflineTranslationValidationError':
        for needle, code in (
            ('quantity', 'offline-quantity-validation'),
            ('placeholder', 'offline-placeholder-validation'),
            ('markdown', 'offline-markdown-validation'),
            ('target script', 'offline-target-script-validation'),
            ('empty', 'offline-empty-validation'),
            ('token limit', 'offline-token-limit'),
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


def validate_text(source: str, translated: str, locale: str, source_language: str) -> None:
    if not isinstance(translated, str) or not translated.strip(): raise ExpansionError('Empty translated text')
    if len(translated) > max(2000, len(source) * 12): raise ExpansionError('Unbounded translation expansion')
    if re.search(r'__(?:KC_PH_|HYMTPH_)\d+__', translated): raise ExpansionError('Unrestored protected identifier')
    if quantity_issues(source, translated, source_language, locale): raise ExpansionError('Financial quantity validation failed')
    if source.count('|') != translated.count('|'): raise ExpansionError('Table column boundaries changed')
    clean = re.sub(r'https?://\S+|\b[A-Z][A-Z0-9.-]{0,7}\b', '', source).strip()
    if not any(c.isalpha() for c in clean): return
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


class Memo:
    def __init__(self, path: Path, locale: str, translator: Translator, deadline: float, *, source_generation: str | None = None):
        reject_symlinks(path)
        self.path, self.locale, self.translator, self.deadline = path, locale, translator, deadline
        self.source_generation = source_generation
        self.rows = {}
        self.calls = self.hits = 0
        if path.is_file():
            if path.stat().st_size > MAX_CHECKPOINT_BYTES: raise ExpansionError('Checkpoint is too large')
            payload = json.loads(path.read_text())
            if (payload.get('model') == MODEL_ID and payload.get('locale') == locale
                and payload.get('version') == CHECKPOINT_VERSION
                and (source_generation is None or payload.get('source_generation') in {None, source_generation})):
                self.rows = payload.get('rows', {})
                if not isinstance(self.rows, dict): raise ExpansionError('Invalid checkpoint rows')

    def key(self, source: str, language: str, *, markdown: bool = False) -> str:
        parts = [CHECKPOINT_VERSION, MODEL_ID, self.locale, language, source]
        if markdown:
            parts.append('markdown')
        return digest(stable_bytes(parts))

    def get(self, source: str, language: str = 'zh', *, markdown: bool = False) -> str:
        if not source.strip(): return source
        key = self.key(source, language, markdown=markdown)
        row = self.rows.get(key)
        if isinstance(row, dict) and row.get('source') == source and row.get('language') == language:
            try:
                validate_text(source, row.get('text'), self.locale, language)
                self.hits += 1
                return row['text']
            except ExpansionError: self.rows.pop(key, None)
        if time.monotonic() >= self.deadline: raise TimeoutError('Local translation time budget reached')
        translated = None
        for attempt in range(MAX_QUANTITY_RETRIES + 1):
            try:
                translated = self.translator.translate(source, target=self.locale, source=language, markdown=markdown)
                self.calls += 1
                break
            except OfflineTranslationValidationError as error:
                self.calls += 1
                retry = (attempt < MAX_QUANTITY_RETRIES and 'quantity' in str(error).casefold()
                         and callable(getattr(self.translator, 'discard_translation', None)))
                if not retry:
                    raise
                self.translator.discard_translation(source, self.locale, language, markdown=markdown)
        if translated is None:
            raise ExpansionError('Offline translation returned no result')
        validate_text(source, translated, self.locale, language)
        self.rows[key] = {'source': source, 'language': language, 'text': translated}
        self.save()
        return translated

    def save(self):
        reject_symlinks(self.path)
        reject_symlinks(self.path.with_suffix('.tmp'))
        payload = {'model': MODEL_ID, 'locale': self.locale, 'version': CHECKPOINT_VERSION, 'rows': self.rows}
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
        except TimeoutError:
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
          *, budget_seconds=1800, origin=ORIGIN) -> dict:
    if locale not in ADDITIONAL: raise ExpansionError('Not an additional locale')
    docs = validate_corpus(corpus, origin=origin)
    if origin + '/' not in {doc['url'] for doc in docs}:
        raise ExpansionError('A localized homepage source is required')
    reject_symlinks(output)
    reject_symlinks(checkpoint)
    if output.exists() and any(output.iterdir()): raise ExpansionError('Candidate output must be empty; never overwrite an active release')
    output.mkdir(parents=True, exist_ok=True)
    memo = Memo(checkpoint, locale, translator, time.monotonic() + budget_seconds,
                source_generation=corpus['documents_sha256'])
    # Materialize an empty or resumed checkpoint before the first model call.
    # A runner interruption or first-call failure must still leave a durable,
    # honest resume point; this contains no fabricated translation rows.
    memo.save()
    translated, failures, timed_out = {}, [], False
    for doc in docs:
        try: translated[doc['url']] = translate_document(doc, memo)
        except TimeoutError:
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
                'budget_exhausted': timed_out, 'failures': failures, 'pages': records,
                'files_sha256': digest(stable_bytes(records))}
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
    parser.add_argument('--seconds', type=int, default=1800)
    args = parser.parse_args()
    if args.list_locales:
        print(json.dumps({'locale': list(select_locales(args.locales))})); return 0
    if not all((args.corpus, args.locale, args.output, args.checkpoint)): parser.error('corpus, locale, output and checkpoint are required')
    require_actions()
    if os.environ.get('KC_PUBLIC_REPOSITORY') != 'true': raise ExpansionError('Translation requires an explicitly verified public repository')
    if not 1 <= args.seconds <= 2400: raise ExpansionError('Time budget must be 1..2400 seconds')
    if args.corpus.stat().st_size > 32 * 1024 * 1024: raise ExpansionError('Corpus too large')
    corpus = json.loads(args.corpus.read_text())
    result = build(corpus, args.locale, args.output, args.checkpoint, OfflineTranslator(), budget_seconds=args.seconds)
    summary = {key: result[key] for key in ('locale', 'status', 'source_document_count', 'completed_page_count', 'paid_provider_requests', 'budget_exhausted')}
    summary['failure_count'] = len(result.get('failures') or [])
    summary['failure_types'] = sorted({str(row.get('error')) for row in result.get('failures') or []})
    summary['failure_codes'] = sorted({str(row.get('code')) for row in result.get('failures') or []})
    summary['failure_fields'] = sorted({str(row.get('field')) for row in result.get('failures') or []})
    summary['failure_field_codes'] = {
        field: sorted({str(row.get('code')) for row in result.get('failures') or []
                       if str(row.get('field')) == field})
        for field in sorted({str(row.get('field')) for row in result.get('failures') or []})
    }
    print(json.dumps(summary))
    return 0 if result['status'] == 'complete-candidate' else 75 if result['budget_exhausted'] and not result['failures'] else 1

if __name__ == '__main__':
    raise SystemExit(main())
