#!/usr/bin/env python3
"""Pinned Hy-MT2 CPU translation, exclusively on Linux GitHub Actions.

Amounts and rates remain inside complete sentences. Opaque Markdown resources,
code and bounded controlled terminology (including a source-derived five-year
planning period) are masked; accepted translations are memoized by exact source and model.
The private runner-local llama server never uses a paid translation provider.
"""
from __future__ import annotations
import atexit
from collections import Counter
from datetime import datetime, timezone
import hashlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import tempfile
import threading
import time
from typing import Callable, Sequence

from compare_hymt_translation import LANGUAGES, SCRIPT_PATTERNS, request_json, require_actions, verify_model, file_sha256
from financial_quantity_integrity import FIVE_YEAR_PERIOD_RE, quantity_issues

MANIFEST_PATH = Path(__file__).with_name('hymt_translation_model_manifest.json')
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
PROVIDER = 'hymt'
MODEL = MANIFEST['model']['repository']
REVISION = MANIFEST['model']['revision']
MODEL_ID = f"{MODEL}@{REVISION}:Q8_0:natural-sentence-v4-table-structure:{hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()[:16]}"
INSTALL_COMMAND = 'Use .github/actions/setup-offline-translation on a Linux GitHub Actions runner'
# Recognize the complete reserved token even when a filename underscore or
# Markdown emphasis touches it; those surrounding underscores are punctuation.
_PLACEHOLDERS = re.compile(r'__(?:KC_PH_\d+|HYMTPH_\d+)__|__[A-Za-z0-9][A-Za-z0-9_]*?__')
_LETTERS = re.compile(r'[^\W\d_]', re.UNICODE)
# Financial amounts, dates, percentages, names, and predicates are intentionally
# absent from opaque-resource masking: splitting those away from the sentence
# changed financial meaning. Exact five-year period terminology is handled
# separately below, with its ordinal derived directly from the source.
_OPAQUE = re.compile(
    r'(?<!`)(?P<ticks>`+)(?!`).*?(?<!`)(?P=ticks)(?!`)'
    r'|!\[(?:\\.|[^\]\\])*\]\((?:[^()\n]|\([^()\n]*\))*\)'
    r'|\[\[[A-Za-z0-9_:-]+\]\]'
    r'|(?<=\]\()(?:(?:[^()\n]|\([^()\n]*\))+)(?=\))'
    r'|(?<=\]\[)[^\]\n]+(?=\])'
    r'|(?i:<(?:script|style|pre|code)\b[^>]*>.*?</(?:script|style|pre|code)\s*>)'
    r'|\$\$.*?\$\$'
    r'|(?<![\\\w])\$(?=[A-Za-z\\])(?=[^$\n]*[=^_{}+*/\\])[^$\n]+\$'
    r'|<!--.*?-->|<(?:"[^"]*"|\x27[^\x27]*\x27|[^\x27">])*>'
    r'|(?:https?://|mailto:)(?:[^\s<>\[\]()]|\([^\s<>\[\]()]*\))+'
    r'|&(?:\#\d+|\#x[\da-fA-F]+|[A-Za-z]+);'
    r'|\\.', re.DOTALL)
# Keep the source numeric atoms inside the model's sentence context, but make
# the exact digits opaque to a small CPU model.  The caller restores the
# source spelling and validates the restored result again.  This covers the
# ordinary decimal/date atoms plus compact quarter/half-year and ordinal
# forms; units remain visible so the model can translate them naturally.
_NUMERIC_ATOM = re.compile(
    # Use ASCII word boundaries deliberately. Chinese, Japanese, Arabic and
    # other scripts commonly attach a date or unit directly to the digits
    # (for example 2024年9月 or 第15个五年); those digits still need to be
    # opaque while their surrounding unit remains in model context.
    r'(?<![A-Za-z0-9_])(?:[QH]\d+(?![A-Za-z0-9_])|\d+(?:Q|H)\d+(?![A-Za-z0-9_])|\d+(?:st|nd|rd|th)(?![A-Za-z0-9_])'
    r'|[+\-−]?\d+(?:[.,]\d+)*)(?![A-Za-z0-9_])', re.IGNORECASE)
_ENGINES: dict[str, object] = {}
_LOCK = threading.RLock()
# Finance vocabulary constrains individual concepts, never whole sentences.
# Rates must remain distinct from the corresponding absolute profit amounts.
_KOREAN_FINANCIAL_TERMS = (
    (r'毛(?:利润|利)率|\bgross(?:\s+profit)?\s+margin\b', '매출총이익률', True),
    (r'(?:营业|经营)利润率|\boperating(?:\s+profit)?\s+margin\b', '영업이익률', True),
    (r'净利润率|净利率|\bnet(?:\s+profit)?\s+margin\b', '순이익률', True),
    (r'毛利润(?!率)|毛利(?!润?率)|\bgross\s+profit\b(?!\s+margin)', '매출총이익', False),
    (r'(?:营业|经营)利润(?!率)|\boperating\s+profit\b(?!\s+margin)', '영업이익', False),
    (r'净利润(?!率)|\bnet\s+profit\b(?!\s+margin)', '순이익', False),
    (r'销售收入|营业收入|\bsales\s+revenue\b', '매출액', False),
)


def financial_glossary(text: str, target: str) -> str:
    if target != 'ko':
        return ''
    constraints = []
    for pattern, term, _is_rate in _KOREAN_FINANCIAL_TERMS:
        match = re.search(pattern, text, re.I)
        if match:
            constraints.append(f'{match.group()} = {term}')
    if not constraints:
        return ''
    return ('Use these Korean financial terms for the corresponding source concepts: '
            + '; '.join(constraints)
            + '. Keep gross, operating and net profit margins distinct from one another and from profit amounts. ')


def validate_financial_terms(source: str, translated: str, target: str) -> None:
    """Optional review diagnostic; never called by the production release gate."""
    if target != 'ko':
        return
    compact = re.sub(r'\s+', '', translated)
    expected = {term for pattern, term, is_rate in _KOREAN_FINANCIAL_TERMS
                if is_rate and re.search(pattern, source, re.I)}
    if any(term not in compact for term in expected):
        raise OfflineTranslationError('Hy-MT2 changed or omitted a Korean financial margin concept')
    # An isolated gross-margin assertion must not acquire an operating margin.
    if '매출총이익률' in expected and '영업이익률' not in expected and '영업이익률' in compact:
        raise OfflineTranslationError('Hy-MT2 confused gross margin with operating margin')

class OfflineTranslationError(RuntimeError):
    """Missing pinned runtime or an incomplete/structurally invalid translation."""


class OfflineTranslationValidationError(OfflineTranslationError):
    """A completed model response failed content validation, not runtime setup."""


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + '.', dir=path.parent)
    try:
        with os.fdopen(fd, 'w', encoding='utf-8') as stream:
            json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2)
            stream.write('\n')
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def normalize_language(language: str) -> str:
    value = str(language).strip().lower().replace('_', '-')
    # Traditional Chinese must retain a distinct target/cache namespace.
    if value in {'zh-hant', 'zh-tw', 'zh-hk', 'zh-mo'} or value.startswith('zh-hant-'):
        return 'zh-Hant'
    code = value.split('-')[0]
    code = {'jp': 'ja', 'kr': 'ko', 'cn': 'zh', 'fil': 'tl'}.get(code, code)
    if code not in LANGUAGES:
        raise OfflineTranslationError(f'Unsupported offline language: {language}')
    return code


def _detect_source(text: str) -> str:
    clean = _PLACEHOLDERS.sub('', _OPAQUE.sub('', text))
    for language, pattern in (('ar', r'[\u0600-\u06ff]'), ('ko', r'[\uac00-\ud7af]'), ('ja', r'[\u3040-\u30ff]')):
        if re.search(pattern, clean):
            return language
    han = len(re.findall(r'[\u3400-\u9fff]', clean))
    words = re.findall(r'[A-Za-z]{2,}', clean)
    return 'zh' if han and not (len(words) >= 4 and sum(map(len, words)) > han * 2) else 'en'


def split_sentences(text: str, limit: int = 1800) -> list[str]:
    """Bound context only at sentence ends, never in a financial assertion."""
    parts = []
    while len(text) > limit:
        candidates = list(re.finditer(r'[。！？](?:\s*)|[.!?](?=\s|$)(?:\s*)', text[:limit + 1]))
        if not candidates:
            raise OfflineTranslationError('Single sentence exceeds offline context limit; source retained')
        end = candidates[-1].end()
        parts.append(text[:end])
        text = text[end:]
    if text:
        parts.append(text)
    return parts


def _mask(text: str, target: str) -> tuple[str, dict[str, str], dict[str, str]]:
    replacements: dict[str, str] = {}
    terms: dict[str, str] = {}
    def reserve(value: str, dictionary: dict[str, str]) -> str:
        index = len(replacements) + len(terms)
        token = f'__HYMTPH_{index:04d}__'
        while token in text or token in replacements or token in terms:
            index += 1
            token = f'__HYMTPH_{index:04d}__'
        dictionary[token] = value
        return token
    masked = _OPAQUE.sub(lambda match: reserve(match.group(), replacements), text)
    if target == 'zh':
        # The model can replace a current plan with the historically common
        # preceding plan (15th -> 14th). Treat this named planning period as a
        # controlled term, deriving its ordinal from the exact source digits.
        # All surrounding claims and amounts remain in the same model request.
        masked = FIVE_YEAR_PERIOD_RE.sub(
            lambda match: reserve(f'第{int(match[1])}个五年', terms), masked)
        # Keep the source innovation category visible instead of allowing the
        # model to collapse FIC Innovation into generic medical innovation.
        masked = re.sub(r'\bFIC\s+Innovation\b', lambda _match: reserve('FIC创新', terms), masked, flags=re.I)
    if target == 'ko':
        for pattern, term, _is_rate in _KOREAN_FINANCIAL_TERMS:
            masked = re.sub(pattern, lambda _match, term=term: reserve(term, terms), masked, flags=re.I)
    # Do this after opaque resources and controlled terms so digits inside a
    # protected token are never exposed as a second claim.  The model still
    # sees surrounding units and predicates, while exact source numbers are
    # restored only after placeholder and quantity validation.
    masked = _NUMERIC_ATOM.sub(lambda match: reserve(match.group(), replacements), masked)
    return masked, replacements, terms


def _restore_terms(value: str, terms: dict[str, str]) -> str:
    for token, term in terms.items():
        value = value.replace(token, term)
    return value


def _restore_table_edges(source: str, result: str) -> str:
    """Restore optional row-edge pipes only when all data columns still match.

    Markdown permits a table row without its exterior pipes. The translation
    output keeps the source spelling, while dropped interior separators remain
    an error. Values and text are never split into separate model requests.
    """
    source = source.strip()
    if not (source.startswith('|') and source.endswith('|') and source.count('|') >= 2):
        return result
    inner = result.strip()
    if inner.startswith('|'):
        inner = inner[1:]
    if inner.endswith('|'):
        inner = inner[:-1]
    if len(inner.split('|')) != len(source[1:-1].split('|')):
        return result
    return '|' + inner + '|'


def validate_result(source: str, result: str, source_language: str, target: str,
                    *, markdown: bool = True, check_quantities: bool = True) -> None:
    if not result.strip():
        raise OfflineTranslationValidationError('Empty Hy-MT2 translation')
    if Counter(_PLACEHOLDERS.findall(source)) != Counter(_PLACEHOLDERS.findall(result)):
        raise OfflineTranslationValidationError('Hy-MT2 changed, omitted, or duplicated a protected placeholder')
    # Korean/Japanese GEO copy is gated on structure and quantities, not wording.
    if check_quantities:
        problems = quantity_issues(source, result, source_language, target)
        if problems:
            raise OfflineTranslationValidationError('Hy-MT2 quantity validation failed: ' + '; '.join(problems))
    # Catalog filenames are plain text: their ~ and _ characters are often
    # punctuation substitutions, not Markdown. The caller must opt in to that
    # format; report Markdown retains all existing structural checks.
    if markdown:
        for marker in ('|', '[', ']', '*', '_', '~', '`'):
            if source.count(marker) != result.count(marker):
                raise OfflineTranslationValidationError(f'Hy-MT2 changed Markdown structure: {marker}')
        destination_shape = r'\]\(__HYMTPH_\d+__\)|\]\[__HYMTPH_\d+__\]'
        if Counter(re.findall(destination_shape, source)) != Counter(re.findall(destination_shape, result)):
            raise OfflineTranslationValidationError('Hy-MT2 changed a Markdown link destination boundary')
    clean = _PLACEHOLDERS.sub('', result)
    if _LETTERS.search(_PLACEHOLDERS.sub('', source)):
        if target not in SCRIPT_PATTERNS or not re.search(SCRIPT_PATTERNS[target], clean):
            raise OfflineTranslationValidationError('Hy-MT2 target script missing')


class _HyMTEngine:
    def __init__(self, directory: Path):
        try:
            require_actions()
        except RuntimeError as error:
            raise OfflineTranslationError(str(error)) from error
        self.manifest = MANIFEST
        self.model = directory / MANIFEST['model']['filename']
        binary = Path(os.environ.get('HYMT_SERVER_BIN', ''))
        receipt_path = directory / 'hymt-model-provenance.json'
        try:
            receipt = json.loads(receipt_path.read_text(encoding='utf-8'))
            if receipt.get('runtime_revision') != MANIFEST['runtime']['revision'] or receipt.get('model_sha256') != MANIFEST['model']['sha256']:
                raise ValueError('Manifest identity mismatch')
            verify_model(self.model, MANIFEST)
            if not binary.is_file() or file_sha256(binary) != receipt.get('server_sha256'):
                raise ValueError('Pinned runtime binary checksum mismatch')
        except (OSError, ValueError) as error:
            raise OfflineTranslationError(f'Missing or invalid Hy-MT2 provenance: {error}') from error
        threads = max(1, min(4, int(os.environ.get('PORTAL_OFFLINE_TRANSLATION_THREADS', '4'))))
        with socket.socket() as probe:
            probe.bind(('127.0.0.1', 0))
            self.port = probe.getsockname()[1]
        self.log = (Path(os.environ.get('RUNNER_TEMP', '.')) / f'hymt-server-{os.getpid()}.log').open('w')
        command = [str(binary), '--model', str(self.model), '--alias', 'hymt-offline',
                   '--host', '127.0.0.1', '--port', str(self.port), '--gpu-layers', '0', '--device', 'none',
                   '--threads', str(threads), '--threads-batch', str(threads), '--ctx-size', '8192',
                   '--parallel', '1', '--cache-ram', '0', '--jinja', '--offline']
        self.process = subprocess.Popen(command, stdout=self.log, stderr=subprocess.STDOUT)
        atexit.register(self.close)
        start = time.monotonic()
        while time.monotonic() - start < 180:
            if self.process.poll() is not None:
                raise OfflineTranslationError('Hy-MT2 pinned runtime exited during startup')
            try:
                request_json(self.port, '/health', timeout=2)
                return
            except (OSError, RuntimeError, json.JSONDecodeError):
                time.sleep(1)
        self.close()
        raise OfflineTranslationError('Hy-MT2 pinned runtime startup timeout')

    def close(self) -> None:
        if self.process.poll() is None:
            self.process.terminate()
            try:
                self.process.wait(timeout=10)
            except subprocess.TimeoutExpired:
                self.process.kill()
                self.process.wait(timeout=5)
        self.log.close()

    def translate(self, text: str, source: str, target: str) -> str:
        prompt = (f'Translate the following text into {LANGUAGES[target]}. '
                  'Note that you should only output the translated result without any additional explanation. '
                  'Preserve all __KC_PH_...__ and __HYMTPH_...__ placeholders exactly, including their order. '
                  'Do not append inferred units or percent signs to placeholders. '
                  'Each __HYMTPH_...__ is an already translated noun or protected resource; integrate it without rewriting it. '
                  'Preserve Markdown formatting. Do not add Markdown table pipes, brackets, backticks, emphasis markers, or other formatting that is not present in the input. '
                  'Do not change financial facts, units, or comparisons. '
                  'Copy every source digit sequence, date, percentage, currency amount, and numeric unit exactly; '
                  'translate the surrounding words without normalizing, rounding, dropping, or inventing numeric facts. '
                  + financial_glossary(text, target) + '\n' + text)
        response = request_json(self.port, '/v1/chat/completions', {
            'model': 'hymt-offline', 'messages': [{'role': 'user', 'content': prompt}],
            'stream': False, 'cache_prompt': False, **MANIFEST['sampling'],
        }, timeout=240)
        choice = response['choices'][0]
        if choice.get('finish_reason') == 'length':
            raise OfflineTranslationValidationError('Hy-MT2 output reached token limit')
        if choice.get('finish_reason') != 'stop':
            raise OfflineTranslationError('Hy-MT2 output reached token limit or did not finish')
        return choice['message'].get('content') or ''


class HyMTOfflineTranslator:
    def __init__(self, cache_dir: str | Path | None = None, *, model_dir: str | Path | None = None,
                 engine_factory: Callable[[str, str], object] | None = None, batch_size: int = 1,
                 diagnostic_callback: Callable[[dict], None] | None = None):
        self.cache_dir = Path(cache_dir or os.environ.get('HYMT_TRANSLATION_CACHE') or os.environ.get('PORTAL_OFFLINE_TRANSLATION_CACHE', '.cache/hymt-translation'))
        self.model_dir = Path(model_dir or os.environ.get('HYMT_MODEL_DIR', '.cache/hymt-model'))
        self._engine_factory = engine_factory
        # Explicit opt-in for the fixed public smoke corpus only; never printed or persisted here.
        self._diagnostic_callback = diagnostic_callback
        self.model_id = MODEL_ID
        self.stats = {'cache_hits': 0, 'translated_fragments': 0, 'batch_requests': 0}

    def _engine(self, source: str, target: str):
        if self._engine_factory:
            return self._engine_factory(source, target)
        key = str(self.model_dir.resolve())
        if key not in _ENGINES:
            _ENGINES[key] = _HyMTEngine(self.model_dir)
        return _ENGINES[key]

    def _memo_identity(self, core: str, target: str, source: str, *, markdown: bool) -> tuple[dict, Path]:
        identity = {'provider': PROVIDER, 'model': MODEL_ID, 'source_language': source,
                    'target_language': target, 'source_sha256': hashlib.sha256(core.encode()).hexdigest()}
        if not markdown:
            identity['text_format'] = 'plain'
        key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
        path = self.cache_dir / key[:2] / f'{key}.json'
        return identity, path

    def discard_translation(self, text: str, target: str, source: str | None = None, *, markdown: bool = True) -> None:
        """Retry this exact unit after a caller rejects its content quality."""
        target = normalize_language(target)
        source = normalize_language(source) if source else None
        for piece in split_sentences(text):
            core = piece.strip()
            _identity, path = self._memo_identity(core, target, source or _detect_source(core), markdown=markdown)
            path.unlink(missing_ok=True)

    def _translate_part(self, text: str, target: str, source: str | None, *, markdown: bool = True) -> str:
        leading, trailing = text[:len(text) - len(text.lstrip())], text[len(text.rstrip()):]
        core = text.strip()
        detected = source or _detect_source(core)
        if not core or detected == target or not _LETTERS.search(_PLACEHOLDERS.sub('', _OPAQUE.sub('', core))):
            return text
        identity, path = self._memo_identity(core, target, detected, markdown=markdown)
        masked, replacements, terms = _mask(core, target)
        fresh_translation = False
        cache_value = None
        try:
            cached = json.loads(path.read_text(encoding='utf-8'))
            if all(cached.get(name) == value for name, value in identity.items()):
                value = cached['translation']
                # Cache stores the validated masked form, independent of source URLs.
                validate_result(masked, value, detected, target, markdown=markdown, check_quantities=False)
                self.stats['cache_hits'] += 1
            else:
                raise ValueError('Cache identity changed')
        except (OSError, ValueError, KeyError, TypeError, OfflineTranslationError):
            try:
                with _LOCK:
                    value = self._engine(detected, target).translate(masked, detected, target)
                if self._diagnostic_callback is not None:
                    self._diagnostic_callback({'model_input': masked, 'raw_translation': value,
                                               'source_language': detected, 'target_language': target,
                                               'controlled_terms': dict(terms)})
                if markdown:
                    value = _restore_table_edges(masked, value)
                validate_result(masked, value, detected, target, markdown=markdown, check_quantities=False)
                cache_value = value
                fresh_translation = True
            except OfflineTranslationError:
                raise
            except Exception as error:
                raise OfflineTranslationError(f'Hy-MT2 translation failed: {error}') from error
        value = _restore_terms(value, terms)
        for token, original in replacements.items():
            value = value.replace(token, original)
        # Validate the materialized response as well as the masked response.
        # This keeps the standalone translator safe if a caller does not add
        # the extended-locale builder's outer quantity gate.
        validate_result(core, value, detected, target, markdown=markdown)
        if fresh_translation:
            atomic_json(path, {**identity, 'translation': cache_value, 'created_at': datetime.now(timezone.utc).isoformat()})
            self.stats['translated_fragments'] += 1
            self.stats['batch_requests'] += 1
        return leading + value.strip() + trailing

    def translate(self, text: str, target: str, source: str | None = None, *, markdown: bool = True) -> str:
        target = normalize_language(target)
        source = normalize_language(source) if source else None
        if not text or source == target:
            return text
        return ''.join(self._translate_part(piece, target, source, markdown=markdown) for piece in split_sentences(text))

    def translate_many(self, texts: Sequence[str], target: str, source: str | None = None) -> list[str]:
        return [self.translate(text, target, source) for text in texts]

    def translate_markdown(self, markdown: str, target: str = 'zh', source: str | None = None,
                           *, source_fallback: Callable[[dict], None] | None = None) -> str:
        result, fence, raw_end = [], None, None
        for line_number, line in enumerate(markdown.splitlines(keepends=True), start=1):
            marker = re.match(r'^\s*(`{3,}|~{3,})', line)
            if raw_end:
                result.append(line)
                if raw_end in line.lower(): raw_end = None
                continue
            if fence:
                result.append(line)
                if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence): fence = None
                continue
            if marker:
                fence = marker[1]
                result.append(line)
                continue
            raw_start = re.match(r'^\s*(<!--|<(script|style|pre|code)\b)', line, re.I)
            if raw_start:
                end = '-->' if raw_start[1] == '<!--' else '</' + raw_start[2].lower() + '>'
                result.append(line)
                raw_end = None if end in line.lower() else end
                continue
            if re.match(r'^(?: {4}|\t)|^\s*\[[^]]+\]:|^\s*\|?[\s:|\-]+\|?\s*$', line):
                result.append(line)
                continue
            prefix = re.match(r'^(?:\s*>\s*)*(?:\s{0,3}#{1,6}\s+|\s*[-+*]\s+(?:\[[ xX]\]\s+)?|\s*\d+[.)]\s+)?', line).group()
            try:
                translated = prefix + self.translate(line[len(prefix):], target, source)
            except OfflineTranslationValidationError as error:
                if source_fallback is None:
                    raise
                # Preserve the complete source unit, including its exact
                # prefix, links, figures and line ending. Invalid model output
                # was never checkpointed by _translate_part.
                source_fallback({'line': line_number, 'source_sha256': hashlib.sha256(line.encode()).hexdigest(),
                                 'reason': str(error)})
                translated = line
            result.append(translated)
        return ''.join(result)

OfflineTranslator = HyMTOfflineTranslator
