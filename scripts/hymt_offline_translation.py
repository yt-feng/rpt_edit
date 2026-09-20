#!/usr/bin/env python3
"""Pinned Hy-MT2 CPU translation, exclusively on Linux GitHub Actions.

Quantities remain inside complete sentences. Only opaque Markdown resources and
code are masked; accepted translations are memoized by exact source and model.
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

from compare_hymt_translation import LANGUAGES, request_json, require_actions, verify_model, file_sha256
from financial_quantity_integrity import quantity_issues

MANIFEST_PATH = Path(__file__).with_name('hymt_translation_model_manifest.json')
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding='utf-8'))
PROVIDER = 'hymt'
MODEL = MANIFEST['model']['repository']
REVISION = MANIFEST['model']['revision']
MODEL_ID = f"{MODEL}@{REVISION}:Q8_0:natural-sentence-v1:{hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()[:16]}"
INSTALL_COMMAND = 'Use .github/actions/setup-offline-translation on a Linux GitHub Actions runner'
_PLACEHOLDERS = re.compile(r'__[A-Za-z0-9_]+__')
_LETTERS = re.compile(r'[A-Za-z\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06ff]')
# Financial amounts, dates, percentages, names, and predicates are intentionally
# absent: splitting those away from the sentence changed financial meaning.
_OPAQUE = re.compile(
    r'(?<!`)(?P<ticks>`+)(?!`).*?(?<!`)(?P=ticks)(?!`)'
    r'|!\[(?:\\.|[^\]\\])*\]\((?:[^()\n]|\([^()\n]*\))*\)'
    r'|\$\$.*?\$\$'
    r'|(?<![\\\w])\$(?=[A-Za-z\\])(?=[^$\n]*[=^_{}+*/\\])[^$\n]+\$'
    r'|<!--.*?-->|<(?:"[^"]*"|\x27[^\x27]*\x27|[^\x27">])*>'
    r'|(?:https?://|mailto:)[^\s<>\])]+(?:\([^\s<>]*\))?'
    r'|&(?:\#\d+|\#x[\da-fA-F]+|[A-Za-z]+);', re.DOTALL)
_ENGINES: dict[str, object] = {}
_LOCK = threading.RLock()

class OfflineTranslationError(RuntimeError):
    """Missing pinned runtime or an incomplete/structurally invalid translation."""


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
    code = str(language).lower().replace('_', '-').split('-')[0]
    code = {'jp': 'ja', 'kr': 'ko', 'cn': 'zh'}.get(code, code)
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


def _mask(text: str) -> tuple[str, dict[str, str]]:
    replacements = {}
    def replace(match: re.Match) -> str:
        index = len(replacements)
        token = f'__HYMTPH_{index:04d}__'
        while token in text or token in replacements:
            index += 1
            token = f'__HYMTPH_{index:04d}__'
        replacements[token] = match.group()
        return token
    return _OPAQUE.sub(replace, text), replacements


def validate_result(source: str, result: str, source_language: str, target: str) -> None:
    if not result.strip():
        raise OfflineTranslationError('Empty Hy-MT2 translation')
    if Counter(_PLACEHOLDERS.findall(source)) != Counter(_PLACEHOLDERS.findall(result)):
        raise OfflineTranslationError('Hy-MT2 changed, omitted, or duplicated a protected placeholder')
    problems = quantity_issues(source, result, source_language, target)
    if problems:
        raise OfflineTranslationError('Hy-MT2 quantity validation failed: ' + '; '.join(problems))
    # Structural punctuation, unlike linguistic punctuation, must stay exact.
    for marker in ('|', '[', ']', '**', '~~'):
        if source.count(marker) != result.count(marker):
            raise OfflineTranslationError(f'Hy-MT2 changed Markdown structure: {marker}')
    clean = _PLACEHOLDERS.sub('', result)
    if _LETTERS.search(_PLACEHOLDERS.sub('', source)):
        scripts = {'zh': r'[\u3400-\u9fff]', 'en': r'[A-Za-z]', 'ko': r'[\uac00-\ud7af]',
                   'ja': r'[\u3040-\u30ff\u3400-\u9fff]', 'ar': r'[\u0600-\u06ff]'}
        if not re.search(scripts[target], clean):
            raise OfflineTranslationError('Hy-MT2 target script missing')


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
                  'Preserve Markdown formatting. Do not change financial facts, units, or comparisons.\n' + text)
        response = request_json(self.port, '/v1/chat/completions', {
            'model': 'hymt-offline', 'messages': [{'role': 'user', 'content': prompt}],
            'stream': False, 'cache_prompt': False, **MANIFEST['sampling'],
        }, timeout=240)
        choice = response['choices'][0]
        if choice.get('finish_reason') != 'stop':
            raise OfflineTranslationError('Hy-MT2 output reached token limit or did not finish')
        return choice['message'].get('content') or ''


class HyMTOfflineTranslator:
    def __init__(self, cache_dir: str | Path | None = None, *, model_dir: str | Path | None = None,
                 engine_factory: Callable[[str, str], object] | None = None, batch_size: int = 1):
        self.cache_dir = Path(cache_dir or os.environ.get('HYMT_TRANSLATION_CACHE') or os.environ.get('PORTAL_OFFLINE_TRANSLATION_CACHE', '.cache/hymt-translation'))
        self.model_dir = Path(model_dir or os.environ.get('HYMT_MODEL_DIR', '.cache/hymt-model'))
        self._engine_factory = engine_factory
        self.model_id = MODEL_ID
        self.stats = {'cache_hits': 0, 'translated_fragments': 0, 'batch_requests': 0}

    def _engine(self, source: str, target: str):
        if self._engine_factory:
            return self._engine_factory(source, target)
        key = str(self.model_dir.resolve())
        if key not in _ENGINES:
            _ENGINES[key] = _HyMTEngine(self.model_dir)
        return _ENGINES[key]

    def _translate_part(self, text: str, target: str, source: str | None) -> str:
        leading, trailing = text[:len(text) - len(text.lstrip())], text[len(text.rstrip()):]
        core = text.strip()
        detected = source or _detect_source(core)
        if not core or detected == target or not _LETTERS.search(_PLACEHOLDERS.sub('', _OPAQUE.sub('', core))):
            return text
        identity = {'provider': PROVIDER, 'model': MODEL_ID, 'source_language': detected,
                    'target_language': target, 'source_sha256': hashlib.sha256(core.encode()).hexdigest()}
        key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
        path = self.cache_dir / key[:2] / f'{key}.json'
        masked, replacements = _mask(core)
        try:
            cached = json.loads(path.read_text(encoding='utf-8'))
            if all(cached.get(name) == value for name, value in identity.items()):
                value = cached['translation']
                # Cache stores the validated masked form, independent of source URLs.
                validate_result(masked, value, detected, target)
                self.stats['cache_hits'] += 1
            else:
                raise ValueError('Cache identity changed')
        except (OSError, ValueError, KeyError, TypeError, OfflineTranslationError):
            try:
                with _LOCK:
                    value = self._engine(detected, target).translate(masked, detected, target)
                validate_result(masked, value, detected, target)
            except OfflineTranslationError:
                raise
            except Exception as error:
                raise OfflineTranslationError(f'Hy-MT2 translation failed: {error}') from error
            atomic_json(path, {**identity, 'translation': value, 'created_at': datetime.now(timezone.utc).isoformat()})
            self.stats['translated_fragments'] += 1
            self.stats['batch_requests'] += 1
        for token, original in replacements.items():
            value = value.replace(token, original)
        return leading + value.strip() + trailing

    def translate(self, text: str, target: str, source: str | None = None) -> str:
        target = normalize_language(target)
        source = normalize_language(source) if source else None
        if not text or source == target:
            return text
        return ''.join(self._translate_part(piece, target, source) for piece in split_sentences(text))

    def translate_many(self, texts: Sequence[str], target: str, source: str | None = None) -> list[str]:
        return [self.translate(text, target, source) for text in texts]

    def translate_markdown(self, markdown: str, target: str = 'zh', source: str | None = None) -> str:
        result, fence, raw_end = [], None, None
        for line in markdown.splitlines(keepends=True):
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
            result.append(prefix + self.translate(line[len(prefix):], target, source))
        return ''.join(result)

OfflineTranslator = HyMTOfflineTranslator
