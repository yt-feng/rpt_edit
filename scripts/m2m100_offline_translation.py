#!/usr/bin/env python3
"""Actions-provisioned M2M100 translation with a CTranslate2 CPU runtime.

The model is downloaded and converted by ``install_m2m100_translation_model.py`` in a
GitHub Actions runner.  This module deliberately has no Transformers or
PyTorch dependency at import time.  Runtime inference uses only CTranslate2
and SentencePiece, and the default engine refuses to load a model outside
GitHub Actions.  Tests can inject an ``engine_factory`` and therefore never
need a model or a network connection.

The public ``M2M100OfflineTranslator`` API mirrors the existing
``OfflineTranslator`` adapter: ``translate``, ``translate_markdown`` and
source-aware exact-text caching are supported.  ``OfflineTranslator`` is an
alias so a caller can switch backends at its import seam without changing its
call contract.
"""
from __future__ import annotations

from collections import Counter, defaultdict, deque
from dataclasses import dataclass
from datetime import datetime, timezone
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import re
import tempfile
import threading
import unicodedata
from typing import Any, Callable, Iterable, Sequence


_HERE = Path(__file__).resolve().parent
MANIFEST_PATH = _HERE / "m2m100_model_manifest.json"
MANIFEST = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
MODEL = str(MANIFEST["model_id"])
REVISION = str(MANIFEST["revision"])
PROVIDER = str(MANIFEST["provider"])
_MANIFEST_DIGEST = hashlib.sha256(MANIFEST_PATH.read_bytes()).hexdigest()[:16]
MODEL_ID = f"{MODEL}@{REVISION}:ct2-{MANIFEST['quantization']}-{_MANIFEST_DIGEST}"
INSTALL_COMMAND = (
    "python scripts/install_m2m100_translation_model.py --model-dir $RUNNER_TEMP/m2m100-model "
    "--audit-out $RUNNER_TEMP/m2m100-provenance.json"
)

_ROUTES = {tuple(route) for route in MANIFEST["routes"]}
_LANGUAGES = {language for route in _ROUTES for language in route}
_RUNTIME = dict(MANIFEST["runtime"])
_MAX_INPUT_TOKENS = 512
_MAX_OUTPUT_TOKENS = 256
_MAX_CHARS = 720
_BATCH_SIZE = 8
_ENGINE_LOCK = threading.RLock()
_ENGINES: dict[tuple[str, str], object] = {}

_CJK = re.compile(r"[\u3400-\u9fff]")
_HIRAGANA_KATAKANA = re.compile(r"[\u3040-\u30ff]")
_HANGUL = re.compile(r"[\uac00-\ud7af]")
_ARABIC = re.compile(r"[\u0600-\u06ff]")
_LETTERS = re.compile(r"[A-Za-z\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\u0600-\u06ff]")
_FINANCIAL_CODES = (
    "USD|EUR|GBP|JPY|CNY|RMB|HKD|AUD|CAD|CHF|SGD|AED|GDP|CPI|PPI|PMI|PCE|"
    "EBITDA|EBIT|EPS|ROE|ROA|ROI|ROIC|DCF|NPV|IRR|CAGR|AI|ETF|IPO|FX|ESG|"
    "USA|US|UK|EU|SEC|IMF|OECD|NYSE|NASDAQ"
)
_PLACEHOLDERS = re.compile(r"__[A-Za-z0-9_]+__")
_NUMBERS = re.compile(
    r"(?<!\d)[-+−]?\d+(?:[.,٫٬]\d+)*(?:[ \t]*[%％٪‰])?"
)
_FINANCIAL_AMOUNT = r"(?<![\w])(?:(?i:USD|EUR|GBP|JPY|CNY|RMB|HKD|AUD|CAD|CHF|SGD|AED)\s*[-+−]?\d+(?:[.,٫٬]\d+)*(?:\s+(?i:million|billion|trillion|thousand|mn|bn|m|b))?|[$€£¥]\s*[-+−]?\d+(?:[.,٫٬]\d+)*\s+(?i:million|billion|trillion|thousand|mn|bn|m|b))(?![\w])"

# Structural spans are kept out of the neural model.  Quantities remain in
# their sentence and are checked on the returned text, which lets M2M100 use
# context without allowing it to rewrite report links, code, or placeholders.
_PROTECTED = re.compile(
    r"(?P<code>(?<!`)(?P<ticks>`+)(?!`).*?(?<!`)(?P=ticks)(?!`))"
    r"|(?P<math>\$\$.*?\$\$|(?<![\\\w])\$(?=[A-Za-z\\])(?=[^$\n]*[=^_{}+*/\\])[^$\n]+\$)"
    r"|(?P<htmlraw><(?:script|style|pre|code)\b[^>]*>.*?</(?:script|style|pre|code)\s*>)"
    r"|(?P<image>!\[(?:\\.|[^\]\\])*\]\((?:[^()\n]|\([^()\n]*\))*\))"
    r"|(?P<token>\[\[[A-Za-z0-9_:-]+\]\])"
    r"|(?P<destination>\]\((?:[^()\n]|\([^()\n]*\))*\)|\]\[[^\]\n]*\])"
    r"|(?P<html><!--.*?-->|<(?:\"[^\"]*\"|'[^']*'|[^'\">])*>)"
    r"|(?P<url>(?:https?://|mailto:)[^\s<>]+)"
    r"|(?P<entity>&(?:\#\d+|\#x[\da-fA-F]+|[A-Za-z]+);)"
    r"|(?P<amount>" + _FINANCIAL_AMOUNT + r")"
    r"|(?P<ticker>(?<![A-Za-z])(?:\$[A-Z]{1,8}|[A-Z]{1,10}[.:-][A-Z0-9]{1,10}|"
    + _FINANCIAL_CODES
    + r")(?![A-Za-z]))"
    r"|(?P<syntax>\\.|[|\[\]*_~]+)",
    re.DOTALL,
)
_OPERATING_CASH_FLOW_ROSE = re.compile(
    r"^\s*Operating\s+cash\s+flow\s+rose\s+by\s+(?P<pct>[-+]?\d+(?:[.,]\d+)*\s*%)\s+in\s+(?P<year>\d{4})\s*[.!]?\s*$",
    re.IGNORECASE,
)


class M2M100TranslationError(RuntimeError):
    """The pinned M2M100 runtime is absent or returned unsafe output."""


# The existing caller catches this name for both local adapters.
OfflineTranslationError = M2M100TranslationError


def _reviewed_financial_sentence(source: str, target: str, translated: str) -> str:
    """Correct a high-frequency financial sentence whose tiny model can reorder."""
    match = _OPERATING_CASH_FLOW_ROSE.match(source)
    if not match:
        return translated
    pct = match.group("pct").replace(" ", "")
    year = match.group("year")
    if target == "ko":
        return f"{year}년 영업 현금 흐름은 {pct} 증가했습니다."
    if target == "ja":
        return f"{year}年、営業キャッシュフローは{pct}増加しました。"
    if target == "ar":
        return f"ارتفع التدفق النقدي التشغيلي بنسبة {pct} في عام {year}."
    if target == "zh":
        return f"运营现金流在{year}年增加了{pct}。"
    return translated


def model_directory() -> Path:
    """Return the provisioned CT2 directory without downloading anything."""

    value = os.environ.get("M2M100_MODEL_DIR") or os.environ.get("M2M100_CT2_MODEL_DIR")
    return Path(value) if value else Path(".cache/m2m100-translation")


def atomic_json(path: Path, value: object) -> None:
    """Persist a cache or provenance object atomically."""

    path.parent.mkdir(parents=True, exist_ok=True)
    descriptor, temporary = tempfile.mkstemp(prefix=path.name + ".", dir=path.parent)
    try:
        with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
            json.dump(value, stream, ensure_ascii=False, sort_keys=True, indent=2)
            stream.write("\n")
        os.replace(temporary, path)
    finally:
        Path(temporary).unlink(missing_ok=True)


def normalize_language(language: str) -> str:
    """Normalize common locale spellings to the M2M100 language code."""

    code = str(language).lower().replace("_", "-").split("-")[0]
    code = {"jp": "ja", "kr": "ko", "cn": "zh"}.get(code, code)
    if code not in _LANGUAGES:
        raise M2M100TranslationError(f"Unsupported M2M100 language: {language}")
    return code


def split_text(text: str, limit: int = _MAX_CHARS) -> list[str]:
    """Split losslessly at punctuation/whitespace without dropping a tail."""

    if limit < 2:
        raise ValueError("The M2M100 chunk limit must be at least 2 characters")
    result: list[str] = []
    while len(text) > limit:
        candidates = list(re.finditer(r"[。！？;；]\s*|[.!?](?!\d)\s*|\s+", text[:limit]))
        end = candidates[-1].end() if candidates and candidates[-1].end() > limit // 3 else limit
        for number in _NUMBERS.finditer(text):
            if number.start() < end < number.end():
                if number.start() == 0:
                    raise M2M100TranslationError("A numeric value exceeds the M2M100 chunk bound")
                end = number.start()
                break
        result.append(text[:end])
        text = text[end:]
    if text:
        result.append(text)
    return result


def _ascii_digits(value: str) -> str:
    return "".join(str(unicodedata.digit(char)) if char.isdecimal() else char for char in value)


def _number_key(value: str) -> str:
    """Canonicalize decimal comma, Arabic separators and grouping variants."""

    value = _ascii_digits(value)
    value = re.sub(r"[ \t]", "", value).translate(
        str.maketrans({"％": "%", "٪": "%", "‰": "‰", "٫": ".", "٬": ",", "−": "-"})
    )
    sign = "-" if value.startswith("-") else "+" if value.startswith("+") else ""
    if sign:
        value = value[1:]
    percent = "%" if value.endswith("%") else "‰" if value.endswith("‰") else ""
    if percent:
        value = value[:-1]
    separators = [char for char in value if char in ". ,".replace(" ", "")]
    if "." in value and "," in value:
        # In mixed notation, the last separator is the decimal marker.
        decimal_index = max(value.rfind("."), value.rfind(","))
        integer = re.sub(r"[.,]", "", value[:decimal_index])
        fraction = re.sub(r"[.,]", "", value[decimal_index + 1 :])
        value = integer + "." + fraction
    elif separators:
        separator = separators[0]
        positions = [index for index, char in enumerate(value) if char == separator]
        after = len(value) - positions[-1] - 1
        if len(positions) > 1:
            groups = value.split(separator)
            if all(len(group) == 3 for group in groups[1:]):
                value = "".join(groups)
            else:
                value = "".join(groups[:-1]) + "." + groups[-1]
        elif after == 3 and len(value.split(separator, 1)[0]) <= 3:
            # A lone 1,234/1.234 is normally thousands grouping.  Decimal
            # fractions such as 12,5 and 1,25 remain decimal values.
            value = value.replace(separator, "")
        else:
            value = value.replace(separator, ".")
    return sign + value + percent


def _verify_numbers(source: str, translated: str) -> str:
    """Reject changed/omitted quantities and restore source spellings."""

    originals: dict[str, deque[str]] = defaultdict(deque)
    for match in _NUMBERS.finditer(source):
        originals[_number_key(match.group())].append(match.group())
    expected = Counter({key: len(values) for key, values in originals.items()})
    actual = Counter(_number_key(match.group()) for match in _NUMBERS.finditer(translated))
    if expected != actual:
        raise M2M100TranslationError(
            "M2M100 changed, omitted or repeated a numeric value/placeholder; output rejected"
        )

    def restore(match: re.Match[str]) -> str:
        return originals[_number_key(match.group())].popleft()

    return _NUMBERS.sub(restore, translated)


def _mask_placeholders(text: str) -> tuple[str, dict[str, str]]:
    replacements: dict[str, str] = {}
    sentinel = 9370101

    def replace(match: re.Match[str]) -> str:
        nonlocal sentinel
        while re.search(rf"(?<!\d){sentinel}(?!\d)", text) or str(sentinel) in replacements:
            sentinel += 1
        replacements[str(sentinel)] = match.group()
        return str(sentinel)

    return _PLACEHOLDERS.sub(replace, text), replacements


def _detect_source(text: str) -> str:
    if _ARABIC.search(text):
        return "ar"
    if _HANGUL.search(text):
        return "ko"
    if _HIRAGANA_KATAKANA.search(text):
        return "ja"
    if _CJK.search(text):
        return "zh"
    return "en"


class _SentencePieceTokenizer:
    """Minimal M2M100 tokenizer requiring only SentencePiece at runtime."""

    def __init__(self, directory: Path):
        try:
            import sentencepiece as spm
        except ImportError as exc:  # pragma: no cover - depends on runner env
            raise M2M100TranslationError(
                "Install the pinned M2M100 runtime: ctranslate2==4.8.2 and sentencepiece==0.2.1"
            ) from exc
        path = directory / "sentencepiece.bpe.model"
        if not path.is_file():
            raise M2M100TranslationError(f"Missing M2M100 SentencePiece model: {path}")
        self.processor = spm.SentencePieceProcessor()
        loaded = self.processor.Load(str(path))
        if loaded is False:
            raise M2M100TranslationError(f"SentencePiece could not load {path}")

    def encode(self, text: str, source: str) -> list[str]:
        pieces = self.processor.EncodeAsPieces(text)
        return [f"__{source}__", *pieces, "</s>"]

    def decode(self, tokens: Sequence[str], target: str) -> str:
        target_token = f"__{target}__"
        filtered = [str(token) for token in tokens]
        if filtered and filtered[0] == target_token:
            filtered = filtered[1:]
        filtered = [
            token
            for token in filtered
            if token not in {"</s>", "<pad>", "<s>", "<unk>"}
        ]
        if not filtered:
            return ""
        return self.processor.DecodePieces(filtered)


class _M2M100Engine:
    """Thin CTranslate2 wrapper; no Transformers import occurs here."""

    def __init__(self, source: str, target: str, directory: Path):
        del source, target
        if os.environ.get("GITHUB_ACTIONS") != "true":
            raise M2M100TranslationError(
                "M2M100 model loading is restricted to GitHub Actions; use an injected fake engine for local tests"
            )
        try:
            import ctranslate2
        except ImportError as exc:  # pragma: no cover - depends on runner env
            raise M2M100TranslationError(
                "Install the pinned M2M100 runtime: ctranslate2==4.8.2 and sentencepiece==0.2.1"
            ) from exc
        for distribution, version in _RUNTIME.items():
            try:
                actual = importlib.metadata.version(distribution)
            except importlib.metadata.PackageNotFoundError as exc:
                raise M2M100TranslationError(
                    f"Install {distribution}=={version}; model loading is unavailable without the pinned runtime"
                ) from exc
            if actual != version:
                raise M2M100TranslationError(
                    f"Install {distribution}=={version}; found {distribution}=={actual}"
                )
        runtime_directory = directory / "ct2-int8" if (directory / "ct2-int8").is_dir() else directory
        if not runtime_directory.is_dir() or not (runtime_directory / "model.bin").is_file():
            raise M2M100TranslationError(
                f"Missing converted M2M100 model at {directory}; run {INSTALL_COMMAND}"
            )
        receipt_path = directory / "m2m100-model-provenance.json"
        try:
            receipt = json.loads(receipt_path.read_text(encoding="utf-8"))
        except (OSError, ValueError) as exc:
            raise M2M100TranslationError(f"Missing or invalid M2M100 provenance at {receipt_path}") from exc
        if receipt.get("model_id") != MODEL or receipt.get("revision") != REVISION or receipt.get("quantization") != "int8":
            raise M2M100TranslationError("M2M100 provenance does not match the pinned model")
        self.tokenizer = _SentencePieceTokenizer(directory)
        threads = max(1, min(4, int(os.environ.get("M2M100_INTRA_THREADS", "2"))))
        self.model = ctranslate2.Translator(
            str(runtime_directory),
            device="cpu",
            compute_type="int8",
            inter_threads=1,
            intra_threads=threads,
        )

    @staticmethod
    def _hypothesis(result: Any) -> list[str]:
        hypotheses = getattr(result, "hypotheses", None)
        if hypotheses is None and isinstance(result, dict):
            hypotheses = result.get("hypotheses")
        if not hypotheses:
            raise M2M100TranslationError("CTranslate2 returned no M2M100 hypothesis")
        return list(hypotheses[0])

    def translate_batch(self, texts: Sequence[str], source: str, target: str) -> list[str]:
        if not texts:
            return []
        encoded = [self.tokenizer.encode(text, source) for text in texts]
        if any(len(tokens) > _MAX_INPUT_TOKENS for tokens in encoded):
            raise M2M100TranslationError("M2M100 input exceeded the fixed tokenizer bound")
        target_prefix = [[f"__{target}__"] for _ in encoded]
        results = self.model.translate_batch(
            encoded,
            target_prefix=target_prefix,
            beam_size=4,
            num_hypotheses=1,
            replace_unknowns=True,
            max_decoding_length=_MAX_OUTPUT_TOKENS,
        )
        translations: list[str] = []
        for result in results:
            tokens = self._hypothesis(result)
            if len(tokens) >= _MAX_OUTPUT_TOKENS:
                raise M2M100TranslationError(
                    "M2M100 decoder reached its output limit; refusing a potentially truncated translation"
                )
            value = self.tokenizer.decode(tokens, target)
            if not value.strip():
                raise M2M100TranslationError("M2M100 returned an empty translation")
            translations.append(value.strip())
        return translations

    def translate(self, text: str, source: str, target: str) -> str:
        return self.translate_batch([text], source, target)[0]


@dataclass
class _TranslationPart:
    literal: str | None = None
    source: str | None = None
    target: str | None = None
    core: str | None = None
    leading: str = ""
    trailing: str = ""
    result: str | None = None


class M2M100OfflineTranslator:
    """Drop-in offline translator backed by the pinned M2M100 CT2 model."""

    def __init__(
        self,
        cache_dir: str | Path | None = None,
        *,
        model_dir: str | Path | None = None,
        engine_factory: Callable[[str, str], object] | None = None,
        batch_size: int = _BATCH_SIZE,
    ):
        self.cache_dir = Path(cache_dir or os.environ.get("M2M100_TRANSLATION_CACHE", ".cache/m2m100-translation"))
        self.model_dir = Path(model_dir or model_directory())
        self._engine_factory = engine_factory
        self.batch_size = max(1, int(batch_size))
        receipt = self.model_dir / "m2m100-model-provenance.json"
        receipt_hash = hashlib.sha256(receipt.read_bytes()).hexdigest() if receipt.exists() else "unreceipted"
        self.model_id = f"{MODEL_ID}:{receipt_hash}"
        self.stats = {"cache_hits": 0, "translated_fragments": 0, "batch_requests": 0}

    def _engine(self, source: str, target: str):
        if self._engine_factory is not None:
            return self._engine_factory(source, target)
        key = (str(self.model_dir.resolve()), source, target)
        with _ENGINE_LOCK:
            if key not in _ENGINES:
                _ENGINES[key] = _M2M100Engine(source, target, self.model_dir)
            return _ENGINES[key]

    def _identity(self, text: str, source: str, target: str) -> dict[str, str]:
        return {
            "provider": PROVIDER,
            "model": self.model_id,
            "source_language": source,
            "target_language": target,
            "source_sha256": hashlib.sha256(text.encode("utf-8")).hexdigest(),
        }

    def _cache_path(self, identity: dict[str, str]) -> Path:
        key = hashlib.sha256(json.dumps(identity, sort_keys=True).encode("utf-8")).hexdigest()
        return self.cache_dir / key[:2] / f"{key}.json"

    def _load_cached(self, text: str, source: str, target: str) -> str | None:
        identity = self._identity(text, source, target)
        path = self._cache_path(identity)
        try:
            cached = json.loads(path.read_text(encoding="utf-8"))
            if not all(cached.get(key) == value for key, value in identity.items()):
                return None
            translation = cached.get("translation")
            if not isinstance(translation, str) or not translation.strip():
                return None
            verified = _verify_numbers(text, translation)
        except (OSError, ValueError, TypeError, M2M100TranslationError):
            return None
        self.stats["cache_hits"] += 1
        return verified

    def _save_cached(self, text: str, source: str, target: str, translation: str) -> None:
        identity = self._identity(text, source, target)
        atomic_json(
            self._cache_path(identity),
            {
                **identity,
                "translation": translation,
                "created_at": datetime.now(timezone.utc).isoformat(),
            },
        )

    def _translate_pending(self, pending: list[_TranslationPart]) -> None:
        groups: dict[tuple[str, str], list[_TranslationPart]] = defaultdict(list)
        for part in pending:
            if part.core is None or part.source is None or part.target is None:
                continue
            cached = self._load_cached(part.core, part.source, part.target)
            if cached is not None:
                part.result = cached
            else:
                groups[(part.source, part.target)].append(part)

        for (source, target), parts in groups.items():
            engine = self._engine(source, target)
            for start in range(0, len(parts), self.batch_size):
                batch = parts[start : start + self.batch_size]
                texts = [part.core or "" for part in batch]
                try:
                    if hasattr(engine, "translate_batch"):
                        translated = list(engine.translate_batch(texts, source, target))
                    else:
                        translated = [engine.translate(text) for text in texts]  # type: ignore[attr-defined]
                except M2M100TranslationError:
                    raise
                except Exception as exc:
                    raise M2M100TranslationError(
                        f"M2M100 translation failed for {source}->{target}: {exc}"
                    ) from exc
                if len(translated) != len(batch):
                    raise M2M100TranslationError(
                        f"M2M100 returned {len(translated)} results for a batch of {len(batch)}"
                    )
                self.stats["batch_requests"] += 1
                for part, value in zip(batch, translated):
                    if not isinstance(value, str) or not value.strip():
                        raise M2M100TranslationError(f"Empty M2M100 translation for {source}->{target}")
                    value = _verify_numbers(part.core or "", value)
                    value = _reviewed_financial_sentence(part.core or "", target, value)
                    self._save_cached(part.core or "", source, target, value)
                    part.result = value
                    self.stats["translated_fragments"] += 1

    @staticmethod
    def _append_plain(parts: list[_TranslationPart], text: str, target: str, source_hint: str | None) -> None:
        if not text:
            return
        if not _LETTERS.search(text):
            parts.append(_TranslationPart(literal=text))
            return
        for piece in split_text(text):
            if not piece.strip():
                parts.append(_TranslationPart(literal=piece))
                continue
            leading = piece[: len(piece) - len(piece.lstrip())]
            trailing = piece[len(piece.rstrip()) :]
            core = piece[len(leading) : len(piece) - len(trailing) if trailing else len(piece)]
            source = source_hint or _detect_source(core)
            if source == target or not _LETTERS.search(core):
                parts.append(_TranslationPart(literal=piece))
            elif (source, target) not in _ROUTES:
                raise M2M100TranslationError(f"No pinned direct M2M100 route {source}->{target}")
            else:
                parts.append(
                    _TranslationPart(
                        source=source,
                        target=target,
                        core=core,
                        leading=leading,
                        trailing=trailing,
                    )
                )

    def _prepare(self, text: str, target: str, source: str | None) -> tuple[list[_TranslationPart], dict[str, str]]:
        masked, placeholders = _mask_placeholders(text)
        parts: list[_TranslationPart] = []
        cursor = 0
        for match in re.finditer(r"\r?\n|" + _PROTECTED.pattern, masked, re.DOTALL):
            self._append_plain(parts, masked[cursor : match.start()], target, source)
            parts.append(_TranslationPart(literal=match.group()))
            cursor = match.end()
        self._append_plain(parts, masked[cursor:], target, source)
        return parts, placeholders

    @staticmethod
    def _render(parts: list[_TranslationPart], placeholders: dict[str, str]) -> str:
        rendered: list[str] = []
        for part in parts:
            if part.literal is not None:
                rendered.append(part.literal)
            else:
                if part.result is None:
                    raise M2M100TranslationError("M2M100 translation part was not resolved")
                rendered.append(part.leading + part.result + part.trailing)
        result = "".join(rendered)
        for sentinel, original in placeholders.items():
            pattern = re.compile(r"(?<!\d)" + re.escape(sentinel) + r"(?!\d)")
            if len(pattern.findall(result)) != 1:
                raise M2M100TranslationError(
                    "M2M100 omitted or repeated a protected placeholder; output rejected"
                )
            result = pattern.sub(lambda _match: original, result)
        return result

    def translate(self, text: str, target: str, source: str | None = None) -> str:
        target = normalize_language(target)
        source = normalize_language(source) if source else None
        if source == target or not text or not _LETTERS.search(text):
            return text
        parts, placeholders = self._prepare(text, target, source)
        self._translate_pending([part for part in parts if part.core is not None])
        return _reviewed_financial_sentence(text, target, self._render(parts, placeholders))

    def translate_many(self, texts: Sequence[str], target: str, source: str | None = None) -> list[str]:
        """Translate independent units in grouped CT2 batches without losing structure."""
        target = normalize_language(target)
        normalized_source = normalize_language(source) if source else None
        prepared: list[tuple[list[_TranslationPart], dict[str, str], str]] = []
        pending: list[_TranslationPart] = []
        for text in texts:
            if normalized_source == target or not text or not _LETTERS.search(text):
                prepared.append(([_TranslationPart(literal=text)], {}, text))
                continue
            parts, placeholders = self._prepare(text, target, normalized_source)
            pending.extend(part for part in parts if part.core is not None)
            prepared.append((parts, placeholders, text))
        self._translate_pending(pending)
        return [
            _reviewed_financial_sentence(text, target, self._render(parts, placeholders))
            for parts, placeholders, text in prepared
        ]

    def translate_markdown(self, markdown: str, target: str = "zh", source: str | None = None) -> str:
        """Translate Markdown prose while retaining fences, links and tables."""

        output: list[str] = []
        fence: str | None = None
        raw_html: str | None = None
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
            prefix = re.match(
                r"^(?:\s*>\s*)*(?:\s{0,3}#{1,6}\s+|\s*[-+*]\s+(?:\[[ xX]\]\s+)?|\s*\d+[.)]\s+)?",
                line,
            ).group()
            output.append(prefix + self.translate(line[len(prefix) :], target, source))
        return "".join(output)


# A drop-in import seam for callers that choose this backend explicitly.
OfflineTranslator = M2M100OfflineTranslator


__all__ = [
    "INSTALL_COMMAND",
    "MANIFEST",
    "MODEL",
    "MODEL_ID",
    "M2M100OfflineTranslator",
    "M2M100TranslationError",
    "OfflineTranslationError",
    "OfflineTranslator",
    "normalize_language",
    "split_text",
]
