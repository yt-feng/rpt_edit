#!/usr/bin/env python3
"""Offline CPU translation with local Argos packages, structural protection and cache.

Only the separate install_offline_translation_models.py downloads model archives.
Inference uses Argos' local tokenizer and CTranslate2 directly: the higher-level
Argos translator can fetch sentence-splitter models and silently truncate input.
"""
from __future__ import annotations

import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import tempfile
import threading
from datetime import datetime, timezone

PROVIDER = "argos-offline"
INSTALL_COMMAND = "python -m pip install -r requirements-translation.txt && python -m pip install --no-deps argostranslate==1.11.0"
MANIFEST_PATH = Path(__file__).with_name("offline_translation_models.json")
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
MODEL_ID = "argos-cpu-v1-" + hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()[:16]
MODELS = {(m["source"], m["target"]): m for m in MANIFEST["models"]}
_ENGINE_LOCK = threading.RLock()
_ENGINES: dict[tuple[str, str, str], object] = {}
_CJK = re.compile(r"[\u3400-\u9fff]")
_LETTERS = re.compile(r"[A-Za-z\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06ff]")
_FINANCIAL_CODES = "USD|EUR|GBP|JPY|CNY|RMB|HKD|AUD|CAD|CHF|SGD|AED|GDP|CPI|PPI|PMI|PCE|EBITDA|EBIT|EPS|ROE|ROA|ROI|ROIC|DCF|NPV|IRR|CAGR|AI|ETF|IPO|FX|ESG|USA|US|UK|EU|SEC|IMF|OECD|NYSE|NASDAQ"
# Protected spans never enter a model, so URLs, amounts, tickers and placeholders
# survive even when a neural model repeats, moves or drops unfamiliar tokens.
_PROTECTED = re.compile(
    r"(?P<code>(?<!`)(?P<ticks>`+)(?!`).*?(?<!`)(?P=ticks)(?!`))"
    r"|(?P<math>\$\$.*?\$\$|(?<![\\\w])\$(?=[A-Za-z\\])(?=[^$\n]*[=^_{}+*/\\])[^$\n]+\$)"
    r"|(?P<htmlraw><(?:script|style|pre|code)\b[^>]*>.*?</(?:script|style|pre|code)\s*>)"
    r"|(?P<image>!\[(?:\\.|[^\]\\])*\]\((?:[^()\n]|\([^()\n]*\))*\))"
    r"|(?P<token>__[A-Za-z0-9_]+__|\[\[[A-Za-z0-9_:-]+\]\])"
    r"|(?P<destination>\]\((?:[^()\n]|\([^()\n]*\))*\)|\]\[[^\]\n]*\])"
    r"|(?P<html><!--.*?-->|<(?:\"[^\"]*\"|'[^']*'|[^'\">])*>)"
    r"|(?P<url>(?:https?://|mailto:)[^\s<>]+)"
    r"|(?P<entity>&(?:\#\d+|\#x[\da-fA-F]+|[A-Za-z]+);)"
    r"|(?P<ticker>(?<![A-Za-z])(?:\$[A-Z]{1,8}|[A-Z]{1,10}[.:-][A-Z0-9]{1,10}|" + _FINANCIAL_CODES + r")(?![A-Za-z]))"
    r"|(?P<number>[-+−]?(?:[$€£¥￥]\s*)?\d+(?:[.,:/\-]\d+)*(?:\s?[%％‰])?)"
    r"|(?P<syntax>\\.|[|\[\]*_~]+)", re.DOTALL,
)


class OfflineTranslationError(RuntimeError):
    """The required pinned offline engine is absent or cannot translate safely."""


def model_directory() -> Path:
    data = Path(os.environ.get("XDG_DATA_HOME", str(Path.home() / ".local/share")))
    return Path(os.environ.get("ARGOS_PACKAGES_DIR", str(data / "argos-translate/packages")))


def atomic_json(path: Path, value: object) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def normalize_language(language: str) -> str:
    code = language.lower().replace("_", "-").split("-")[0]
    code = {"jp": "ja", "kr": "ko", "cn": "zh"}.get(code, code)
    if code not in {"zh", "en", "ja", "ko", "ar"}:
        raise OfflineTranslationError(f"Unsupported offline language: {language}")
    return code


def split_text(text: str, limit: int = 240) -> list[str]:
    """Lossless deterministic splitting; never drop an oversized sentence's tail."""
    result = []
    while len(text) > limit:
        candidates = list(re.finditer(r"[。！？.!?;；]\s*|\s+", text[:limit]))
        end = candidates[-1].end() if candidates and candidates[-1].end() > limit // 3 else limit
        result.append(text[:end])
        text = text[end:]
    if text:
        result.append(text)
    return result


class _ArgosEngine:
    def __init__(self, source: str, target: str, packages_dir: Path):
        expected = MODELS[(source, target)]
        try:
            for distribution, version in MANIFEST["runtime"].items():
                if importlib.metadata.version(distribution) != version:
                    raise OfflineTranslationError(f"Install pinned runtime: {INSTALL_COMMAND} ({distribution}=={version})")
            # Do not import argostranslate.translate: its sentence splitters may
            # download external resources. Package + tokenizer are local only.
            from argostranslate.package import Package
            import ctranslate2
        except ImportError as exc:
            raise OfflineTranslationError(f"Install the offline runtime: {INSTALL_COMMAND}") from exc
        package_path = None
        for metadata_path in sorted(packages_dir.glob("*/metadata.json")):
            metadata = json.loads(metadata_path.read_text(encoding="utf-8"))
            if (metadata.get("from_code"), metadata.get("to_code"), str(metadata.get("package_version"))) == (source, target, expected["version"]):
                package_path = metadata_path.parent
                break
        if package_path is None:
            raise OfflineTranslationError(f"Missing pinned offline model {source}->{target} v{expected['version']}; run python scripts/install_offline_translation_models.py --targets {target}")
        self.package = Package(package_path)
        threads = max(1, min(2, int(os.environ.get("PORTAL_OFFLINE_TRANSLATION_THREADS", "1"))))
        self.model = ctranslate2.Translator(str(package_path / "model"), device="cpu", compute_type="int8", inter_threads=1, intra_threads=threads)

    def translate(self, text: str) -> str:
        tokens = self.package.tokenizer.encode(text)
        # SentencePiece can expand characters into several byte tokens. Enforce
        # the token bound as well as the character bound before calling CT2.
        if len(tokens) > 192:
            if len(text) < 2:
                raise OfflineTranslationError("A single character exceeds the offline tokenizer bound")
            return "".join(self.translate(piece) for piece in split_text(text, max(1, len(text) // 2)))
        prefix = self.package.target_prefix
        translated = self.model.translate_batch(
            [tokens], target_prefix=[[prefix]] if prefix else None,
            beam_size=4, num_hypotheses=1, replace_unknowns=True,
            max_input_length=0, max_decoding_length=1024, length_penalty=0.2,
        )[0].hypotheses[0]
        if len(translated) >= 1024:
            raise OfflineTranslationError("Offline decoder reached its output limit; refusing a potentially truncated translation")
        value = self.package.tokenizer.decode(translated)
        if prefix and value.startswith(prefix):
            value = value[len(prefix):]
        return value.strip()


class OfflineTranslator:
    def __init__(self, cache_dir: str | Path | None = None, *, engine_factory=None):
        self.cache_dir = Path(cache_dir or os.environ.get("PORTAL_OFFLINE_TRANSLATION_CACHE", ".cache/offline-translation"))
        self.packages_dir = model_directory()
        self._engine_factory = engine_factory
        receipt = self.packages_dir / "offline-model-provenance.json"
        receipt_hash = hashlib.sha256(receipt.read_bytes()).hexdigest() if receipt.exists() else "unreceipted"
        self.model_id = MODEL_ID + ":" + receipt_hash
        self.stats = {"cache_hits": 0, "translated_fragments": 0}

    def _engine(self, source: str, target: str):
        if self._engine_factory is not None:
            return self._engine_factory(source, target)
        key = (str(self.packages_dir.resolve()), source, target)
        if key not in _ENGINES:
            _ENGINES[key] = _ArgosEngine(source, target, self.packages_dir)
        return _ENGINES[key]

    def _run(self, text: str, source: str, target: str) -> str:
        if source == target or not _LETTERS.search(text):
            return text
        if (source, target) not in MODELS:
            if source == "zh" and target in {"ja", "ko", "ar"}:
                return self._run(self._run(text, "zh", "en"), "en", target)
            raise OfflineTranslationError(f"No pinned offline route {source}->{target}")
        source_hash = hashlib.sha256(text.encode()).hexdigest()
        identity = {"provider": PROVIDER, "model": self.model_id, "source_language": source, "target_language": target, "source_sha256": source_hash}
        key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode()).hexdigest()
        path = self.cache_dir / key[:2] / (key + ".json")
        with _ENGINE_LOCK:
            if path.exists():
                try:
                    cached = json.loads(path.read_text(encoding="utf-8"))
                    if all(cached.get(k) == v for k, v in identity.items()) and isinstance(cached.get("translation"), str) and cached["translation"].strip():
                        self.stats["cache_hits"] += 1
                        return cached["translation"]
                except (ValueError, OSError):
                    pass  # A partial/stale cache entry is recalculated, never treated as output.
            try:
                result = self._engine(source, target).translate(text)
            except OfflineTranslationError:
                raise
            except Exception as exc:
                raise OfflineTranslationError(f"Offline translation failed for {source}->{target}: {exc}") from exc
            if not isinstance(result, str) or not result.strip():
                raise OfflineTranslationError(f"Empty offline translation for {source}->{target}")
            atomic_json(path, {**identity, "translation": result, "created_at": datetime.now(timezone.utc).isoformat()})
            self.stats["translated_fragments"] += 1
            return result

    def _fragment(self, text: str, target: str, source: str | None) -> str:
        if not text or not _LETTERS.search(text):
            return text
        # Mixed Chinese/English inputs occur in navigation labels and titles.
        # Translate Latin phrases independently when both scripts are present;
        # an English model must never be asked to interpret a Chinese paragraph.
        if source is None and _CJK.search(text) and re.search(r"[A-Za-z]", text):
            runs = re.findall(r"[A-Za-z]+(?:[ \t’'\-]+[A-Za-z]+)*|[^A-Za-z]+", text)
            return "".join(self._fragment(run, target, "zh" if _CJK.search(run) else "en") for run in runs)
        source = source or ("zh" if _CJK.search(text) else "en")
        outputs = []
        for piece in split_text(text):
            core = piece.strip()
            if not core:
                outputs.append(piece)
                continue
            leading = piece[:len(piece) - len(piece.lstrip())]
            trailing = piece[len(piece.rstrip()):]
            outputs.append(leading + self._run(core, source, target) + trailing)
        return "".join(outputs)

    def translate(self, text: str, target: str, source: str | None = None) -> str:
        target = normalize_language(target)
        source = normalize_language(source) if source else None
        pieces, cursor = [], 0
        # Newlines are structural for subtitles, prose and HTML alike.
        for match in re.finditer(r"\r?\n|" + _PROTECTED.pattern, text, re.DOTALL):
            pieces.append(self._fragment(text[cursor:match.start()], target, source))
            pieces.append(match.group())
            cursor = match.end()
        pieces.append(self._fragment(text[cursor:], target, source))
        return "".join(pieces)

    def translate_markdown(self, markdown: str, target: str = "zh", source: str | None = "en") -> str:
        output, fence, raw_html = [], None, None
        for line in markdown.splitlines(keepends=True):
            if raw_html:
                output.append(line)
                if raw_html in line.lower():
                    raw_html = None
                continue
            marker = re.match(r"^\s*(`{3,}|~{3,})", line)
            if fence:
                output.append(line)
                if marker and marker[1][0] == fence[0] and len(marker[1]) >= len(fence):
                    fence = None
                continue
            if marker:
                fence = marker[1]
                output.append(line)
                continue
            raw_start = re.match(r"^\s*(<!--|<(script|style|pre|code)\b)", line, re.I)
            if raw_start:
                end = "-->" if raw_start[1] == "<!--" else "</" + raw_start[2].lower() + ">"
                output.append(line)
                raw_html = None if end in line.lower() else end
                continue
            if re.match(r"^(?: {4}|\t)|^\s*\[[^]]+\]:|^\s*\|?[\s:|\-]+\|?\s*$", line):
                output.append(line)
                continue
            prefix = re.match(r"^(?:\s*>\s*)*(?:\s{0,3}#{1,6}\s+|\s*[-+*]\s+(?:\[[ xX]\]\s+)?|\s*\d+[.)]\s+)?", line).group()
            output.append(prefix + self.translate(line[len(prefix):], target, source))
        return "".join(output)
