#!/usr/bin/env python3
"""Translate Portal Suite report titles locally with reusable translation memory."""

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

CJK_RE = re.compile(r"[\u3400-\u9fff]")
TITLE_CACHE_SCHEMA_VERSION = 1
TITLE_PROMPT_VERSION = "portal-title-zh-v1"
OFFLINE_TITLE_MODEL = "argos-offline"
LEGACY_TITLE_MODELS = frozenset({"deepseek-v4-flash", "deepseek-chat", "deepseek-reasoner"})


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


def active_title_model() -> str:
    # Import only the adapter's pinned manifest identity, without loading models.
    from offline_translation import MODEL_ID
    return MODEL_ID


def load_title_cache(path: Path | None) -> dict[str, Any]:
    empty = {"schema_version": TITLE_CACHE_SCHEMA_VERSION, "provider": "translation-memory", "entries": {}}
    if path is None or not path.is_file():
        return empty
    try:
        cache = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, ValueError) as error:
        raise RuntimeError(f"Invalid title translation cache: {path}") from error
    if (not isinstance(cache, dict)
            or cache.get("schema_version") != TITLE_CACHE_SCHEMA_VERSION
            or cache.get("provider") not in {"deepseek", "argos-offline", "translation-memory"}
            or not isinstance(cache.get("entries"), dict)):
        raise RuntimeError(f"Unsupported title translation cache: {path}")
    for key, row in cache["entries"].items():
        if (not isinstance(row, dict)
                or any(not isinstance(row.get(field), str) or not row[field].strip()
                       for field in ("source", "model", "prompt_version", "title_zh"))
                or key != title_cache_key(row["source"], row["model"], row["prompt_version"])):
            raise RuntimeError(f"Invalid title translation cache entry: {path}")
    return cache


def cached_title(cache: dict[str, Any], source: str) -> dict[str, Any] | None:
    """Reuse an exact current result or one unambiguous legacy translation."""
    current = cache["entries"].get(title_cache_key(source, active_title_model()))
    if current is not None:
        return current
    legacy = [row for row in cache["entries"].values()
              if row["source"] == source and row["prompt_version"] == TITLE_PROMPT_VERSION
              and row["model"] in LEGACY_TITLE_MODELS
              and row.get("provider", "deepseek") == "deepseek"]
    if legacy and len({row["title_zh"] for row in legacy}) == 1:
        return legacy[0]
    return None


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
        if cached_title(cache, source) is not None:
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
            "title_zh": translation, "provider": "published", "provenance": "active-public-catalog",
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


def translate_title(title: str, args: argparse.Namespace) -> str:
    from offline_translation import OfflineTranslator

    if not hasattr(args, "_offline_translator"):
        args._offline_translator = OfflineTranslator()
    args._offline_model_id = args._offline_translator.model_id
    translated = normalize_translation(args._offline_translator.translate(title, target="zh"))
    if not translated:
        raise RuntimeError("Local title translation returned an empty result")
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
    parser.add_argument("--model", default=OFFLINE_TITLE_MODEL, help="Compatibility option; titles always use local Argos models.")
    parser.add_argument("--deepseek-base-url", default="", help="Compatibility option; no API requests are made.")
    parser.add_argument("--workers", type=int, default=1, help="Compatibility option; local inference uses one worker.")
    parser.add_argument("--timeout", type=int, default=45)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int, default=0, help="Translate at most this many missing titles. 0 means all.")
    parser.add_argument("--force", action="store_true", help="Retranslate titles that already have title_zh.")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--fail-on-error", action="store_true")
    args = parser.parse_args()
    args.model = active_title_model()
    args.workers = 1

    catalog_path = Path(args.catalog_path)
    cache_path = Path(args.cache_path) if args.cache_path else None
    if cache_path is not None and cache_path.resolve() == catalog_path.resolve():
        parser.error("--cache-path must differ from --catalog-path")
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
        row = cached_title(cache, source) if not args.force else None
        if row is not None:
            item["title_zh"] = row["title_zh"]
            cached += 1
        else:
            pending.setdefault(source, []).append(item)
    if cached:
        log(f"Reused {cached} Portal Suite title translations from checkpoint.")
    if pending:
        log(f"Translating {sum(len(rows) for rows in pending.values())} Portal Suite titles "
            f"locally with Argos, workers={args.workers}")
    translated = 0
    failed = 0

    def work(source: str) -> str:
        title = source.strip()
        if has_cjk(title) and not args.force:
            return title
        return translate_title(title, args)

    max_workers = max(1, args.workers)
    with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = {executor.submit(work, source): source for source in pending}
        for index, future in enumerate(concurrent.futures.as_completed(futures), start=1):
            source = futures[future]
            target_items = pending[source]
            try:
                title_zh = future.result()
            except Exception as exc:  # noqa: BLE001 - retry next scheduled run.
                failed += len(target_items)
                for item in target_items:
                    log(f"  [failed] {str(item.get('id') or '')}: {exc}")
            else:
                cache["entries"][title_cache_key(source, args.model)] = {
                    "source": source, "model": args.model, "prompt_version": TITLE_PROMPT_VERSION,
                    "title_zh": title_zh, "provider": "argos-offline" if not has_cjk(source) or args.force else "source",
                    "engine_model_id": getattr(args, "_offline_model_id", args.model),
                }
                cache["provider"] = "translation-memory"
                # Persist each result before later translations or catalog writes can fail.
                if cache_path is not None and not args.dry_run:
                    write_json(cache_path, cache)
                for item in target_items:
                    item["title_zh"] = title_zh
                translated += len(target_items)
            if index == len(futures) or index % 50 == 0:
                log(f"  progress {index}/{len(futures)} sources translated={translated} failed={failed}")

    catalog["title_translation"] = {
        "provider": "translation-memory",
        "new_translation_provider": "argos-offline",
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
