#!/usr/bin/env python3
"""Translate Portal Suite report titles to Simplified Chinese with the pinned offline Hy-MT2 model."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import sys
import tempfile
from collections import Counter
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any

from offline_translation import MODEL_ID, PROVIDER, OfflineTranslator, _detect_source


CJK_RE = re.compile(r"[\u3400-\u9fff]")
TITLE_CACHE_SCHEMA_VERSION = 1
TITLE_PROMPT_VERSION = "portal-title-zh-v1"
TITLE_IDENTIFIER_RE = re.compile(
    r"[（(](?:\d{6}|[A-Z0-9]{1,12}\.[A-Z]{1,4}|[A-Z]{1,10})[）)]"
    r"|-(?:\d{8}|\d{6})$"
)


def log(message: str) -> None:
    print(message, flush=True)


def bjt_now() -> str:
    tz = timezone(timedelta(hours=8))
    return datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")


def load_json(path: Path, fallback: dict[str, Any]) -> dict[str, Any]:
    if not path.exists():
        return fallback
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(mode="w", encoding="utf-8", dir=path.parent,
                                         prefix=f".{path.name}.", suffix=".tmp", delete=False) as handle:
            temporary = Path(handle.name)
            handle.write(json.dumps(data, ensure_ascii=False, indent=2) + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        temporary.replace(path)
    finally:
        if temporary is not None:
            temporary.unlink(missing_ok=True)


def title_cache_key(source: str, model: str, prompt_version: str | None = None) -> str:
    # Preserve the exact original title, including punctuation and whitespace.
    material = json.dumps([source, model, prompt_version or TITLE_PROMPT_VERSION],
                          ensure_ascii=False, separators=(",", ":"))
    return hashlib.sha256(material.encode("utf-8")).hexdigest()


def load_title_cache(path: Path | None) -> dict[str, Any]:
    empty = {"schema_version": TITLE_CACHE_SCHEMA_VERSION, "provider": PROVIDER, "entries": {}}
    if path is None or not path.is_file():
        return empty
    try:
        cache = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise RuntimeError(f"Invalid title translation cache: {path}") from error
    if (not isinstance(cache, dict)
            or cache.get("schema_version") != TITLE_CACHE_SCHEMA_VERSION
            or cache.get("provider") not in {"deepseek", PROVIDER}
            or not isinstance(cache.get("entries"), dict)):
        raise RuntimeError(f"Unsupported title translation cache: {path}")
    for key, row in cache["entries"].items():
        if (not isinstance(row, dict)
                or any(not isinstance(row.get(field), str) or not row[field].strip()
                       for field in ("source", "model", "prompt_version", "title_zh"))
                or key != title_cache_key(row["source"], row["model"], row["prompt_version"])):
            raise RuntimeError(f"Invalid title translation cache entry: {path}")
    legacy_rows = list(cache["entries"].values()) if cache.get("provider") == "deepseek" else []
    for row in legacy_rows:
        if row["prompt_version"] == TITLE_PROMPT_VERSION:
            key = title_cache_key(row["source"], MODEL_ID)
            cache["entries"].setdefault(key, {**row, "model": MODEL_ID,
                "provenance": "legacy-paid-cache", "source_cache_model": row["model"]})
    cache["provider"] = PROVIDER
    return cache


def seed_title_cache(cache: dict[str, Any], catalog: dict[str, Any], candidates: list[dict[str, Any]],
                     seed_catalog: dict[str, Any], model: str) -> int:
    # Use the same public-title normalization as the actual site builder.
    # Its imports are standard-library-only; defer this import until seeding.
    from build_portal_suite_site import public_source_text

    current_ids = Counter(str(row.get("id") or "") for row in catalog.get("items", [])
                          if isinstance(row, dict))
    seed_rows: dict[str, list[dict[str, Any]]] = {}
    source_translations: dict[str, set[str]] = {}
    for row in seed_catalog["items"]:
        if not isinstance(row, dict):
            continue
        seed_rows.setdefault(str(row.get("id") or ""), []).append(row)
        source = public_source_text(row.get("title"))
        translation = str(row.get("title_zh") or "").strip()
        if source and translation:
            source_translations.setdefault(source, set()).add(translation)

    seeded = 0
    for item in candidates:
        if str(item.get("title_zh") or "").strip():
            continue
        source = str(item.get("title") or "")
        key = title_cache_key(source, model)
        if key in cache["entries"]:
            continue
        report_id = str(item.get("id") or "")
        matches = seed_rows.get(report_id, [])
        if not report_id or current_ids[report_id] != 1 or len(matches) != 1:
            continue
        public_source = public_source_text(source)
        seed = matches[0]
        translation = str(seed.get("title_zh") or "").strip()
        if (not public_source or public_source != public_source_text(seed.get("title"))
                or not translation or len(source_translations.get(public_source, set())) != 1):
            continue
        cache["entries"][key] = {
            "source": source, "model": model, "prompt_version": TITLE_PROMPT_VERSION,
            "title_zh": translation, "provenance": "active-public-catalog",
        }
        seeded += 1
    return seeded


def has_cjk(value: str) -> bool:
    return bool(CJK_RE.search(value or ""))


def normalize_translation(value: str) -> str:
    text = str(value or "").strip()
    text = re.sub(r"^```(?:json|text|markdown)?\s*", "", text, flags=re.IGNORECASE)
    text = re.sub(r"\s*```$", "", text)
    text = re.sub(r"^\s*(?:中文标题|译名|翻译|title_zh|zh)\s*[:：]\s*", "", text, flags=re.IGNORECASE)
    text = text.strip().strip("\"'“”‘’`")
    text = re.sub(r"\s+", " ", text).strip()
    return text


def protect_title_identifiers(title: str) -> tuple[str, dict[str, str]]:
    """Keep ticker symbols and valid filename date suffixes byte-for-byte.

    These identify the document or security, rather than asserting financial
    quantities. Amounts, comparisons and reporting periods stay in the complete
    model input and remain subject to the normal quantity validator.
    """
    identifiers: dict[str, str] = {}
    def reserve(match: re.Match) -> str:
        value = match.group()
        if value.startswith('-'):
            digits = value[1:]
            try:
                datetime.strptime(digits, '%Y%m%d' if len(digits) == 8 else '%y%m%d')
            except ValueError:
                return value
        index = len(identifiers)
        token = f'__KC_PH_{index:04d}__'
        while token in title or token in identifiers:
            index += 1
            token = f'__KC_PH_{index:04d}__'
        identifiers[token] = value
        return token
    return TITLE_IDENTIFIER_RE.sub(reserve, title), identifiers


def translate_title(title: str, args: argparse.Namespace) -> str:
    if not hasattr(args, "_offline_translator"):
        args._offline_title_calls = []
        kwargs = ({"diagnostic_callback": args._offline_title_calls.append}
                  if getattr(args, "diagnostics_out", None) else {})
        args._offline_translator = OfflineTranslator(**kwargs)
    if hasattr(args, "_offline_title_calls"):
        args._offline_title_calls.clear()
    protected, identifiers = protect_title_identifiers(title)
    try:
        translated = normalize_translation(args._offline_translator.translate(
            protected, target="zh", source=_detect_source(title), markdown=False))
        for token, value in identifiers.items():
            if translated.count(token) != 1:
                raise RuntimeError("Offline model changed a protected title identifier")
            translated = translated.replace(token, value)
    except Exception as error:
        if getattr(args, "diagnostics_out", None):
            error.translation_diagnostics = list(getattr(args, "_offline_title_calls", []))
        raise
    if not translated:
        raise RuntimeError("Offline model returned an empty title translation")
    return translated


def candidate_items(catalog: dict[str, Any], force: bool, limit: int) -> list[dict[str, Any]]:
    rows: list[dict[str, Any]] = []
    for item in catalog.get("items", []):
        if not isinstance(item, dict):
            continue
        title = str(item.get("title") or "").strip()
        if not title:
            continue
        current = str(item.get("title_zh") or "").strip()
        if current and not force:
            continue
        rows.append(item)
        if limit > 0 and len(rows) >= limit:
            break
    return rows


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--catalog-path", default="portal_suite/data/catalog.json")
    parser.add_argument("--cache-path", help="Read and atomically checkpoint translated titles in this JSON file.")
    parser.add_argument("--seed-catalog-path", help="Reuse published Chinese titles only for matching unique report IDs and source titles.")
    parser.add_argument("--diagnostics-out", type=Path,
                        help="Write rejected source titles and model outputs for an explicit Actions diagnostic artifact.")
    parser.add_argument("--model", default=MODEL_ID, help="Compatibility only; the pinned offline model is always used")
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--workers", type=int, default=1)
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0, help="Translate at most this many missing titles. 0 means all.")
    parser.add_argument("--force", action="store_true", help="Retranslate titles that already have title_zh.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()
    args.model = MODEL_ID
    diagnostics = {"model": MODEL_ID, "provider": PROVIDER, "failed_titles": []}

    catalog_path = Path(args.catalog_path)
    cache_path = Path(args.cache_path) if args.cache_path else None
    if cache_path is not None and cache_path.resolve() == catalog_path.resolve():
        parser.error("--cache-path must differ from --catalog-path")
    if args.diagnostics_out is not None:
        protected_paths = [catalog_path, cache_path]
        if args.seed_catalog_path:
            protected_paths.append(Path(args.seed_catalog_path))
        if any(path is not None and args.diagnostics_out.resolve() == path.resolve() for path in protected_paths):
            parser.error("--diagnostics-out must differ from the catalog, cache and seed paths")
        if not args.dry_run:
            write_json(args.diagnostics_out, diagnostics)
    catalog = load_json(catalog_path, {"schema_version": 1, "items": []})
    cache = load_title_cache(cache_path)
    items = candidate_items(catalog, args.force, args.limit)
    seeded = 0
    if args.seed_catalog_path and items and not args.force:
        seed_path = Path(args.seed_catalog_path)
        seed_catalog = json.loads(seed_path.read_text(encoding="utf-8"))
        if not isinstance(seed_catalog, dict) or not isinstance(seed_catalog.get("items"), list):
            raise RuntimeError(f"Invalid seed title catalog: {seed_path}")
        seeded = seed_title_cache(cache, catalog, items, seed_catalog, args.model)
        if seeded:
            log(f"Seeded {seeded} title translations from matching published report sources.")
    if cache_path is not None and not args.dry_run:
        write_json(cache_path, cache)
    if not items:
        log("No Portal Suite titles need translation.")
        return 0

    cached = 0
    pending: dict[str, list[dict[str, Any]]] = {}
    for item in items:
        source = str(item.get("title") or "")
        row = cache["entries"].get(title_cache_key(source, args.model)) if not args.force else None
        if row is not None:
            item["title_zh"] = row["title_zh"]
            cached += 1
        else:
            pending.setdefault(source, []).append(item)
    if cached:
        log(f"Reused {cached} Portal Suite title translations from checkpoint.")

    if pending:
        log(f"Translating {sum(len(rows) for rows in pending.values())} Portal Suite titles "
            f"with offline model={args.model}, workers=1")
    translated = 0
    failed = 0

    def work(source: str) -> str:
        title = source.strip()
        if _detect_source(title) == "zh" and not args.force:
            return title
        return translate_title(title, args)

    max_workers = 1
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(work, source): source for source in pending}
        for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            source = futures[future]
            target_items = pending[source]
            try:
                title_zh = future.result()
            except Exception as exc:  # noqa: BLE001 - retry next scheduled run.
                failed += len(target_items)
                diagnostics["failed_titles"].append({
                    "ids": [str(item.get("id") or "") for item in target_items],
                    "source": source, "error": str(exc),
                    "model_calls": getattr(exc, "translation_diagnostics", []),
                })
                if args.diagnostics_out is not None and not args.dry_run:
                    write_json(args.diagnostics_out, diagnostics)
                for item in target_items:
                    log(f"  [failed] {str(item.get('id') or '')}: {exc}")
            else:
                cache["entries"][title_cache_key(source, args.model)] = {
                    "source": source, "model": args.model, "prompt_version": TITLE_PROMPT_VERSION,
                    "title_zh": title_zh,
                }
                # Persist each accepted success before later requests or catalog writes can fail.
                if cache_path is not None and not args.dry_run:
                    write_json(cache_path, cache)
                for item in target_items:
                    item["title_zh"] = title_zh
                translated += len(target_items)
            if index == len(futures) or index % 50 == 0:
                log(f"  progress {index}/{len(futures)} sources translated={translated} failed={failed}")

    catalog["title_translation"] = {
        "provider": PROVIDER,
        "provider_requests": 0,
        "api_cost_cny": 0,
        "model": args.model,
        "updated_at_bjt": bjt_now(),
        "translated_title_count": sum(1 for item in catalog.get("items", []) if str(item.get("title_zh") or "").strip()),
        "last_run_translated": translated,
        "last_run_cached": cached,
        "last_run_seeded": seeded,
        "last_run_failed": failed,
    }

    if args.dry_run:
        log("Dry run; catalog not written.")
    else:
        write_json(catalog_path, catalog)
        log(f"Wrote {catalog_path}: translated={translated}, failed={failed}")

    if failed and args.fail_on_error:
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
