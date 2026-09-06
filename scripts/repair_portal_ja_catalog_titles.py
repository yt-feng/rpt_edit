"""Apply reviewed Japanese title corrections to the build cache, without APIs.

This is an exact-source data repair, not a language detector. Existing Japanese
translations other than the reviewed erroneous values are deliberately retained.
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path
from typing import Any, Iterable, Mapping


DEFAULT_REPAIR_DATA = Path(__file__).with_name("portal_ja_catalog_title_repairs.json")
_PLACEHOLDER = re.compile(r"__KC_PH_\d{3}__")


def load_repairs(path: Path = DEFAULT_REPAIR_DATA) -> list[dict[str, Any]]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if payload.get("schema_version") != 1 or payload.get("locale") != "ja":
        raise ValueError("Unsupported Japanese title repair data")
    repairs = payload.get("repairs")
    if not isinstance(repairs, list):
        raise ValueError("Japanese title repairs must be a list")
    seen: set[str] = set()
    for row in repairs:
        if not isinstance(row, dict):
            raise ValueError("Invalid Japanese title repair row")
        key = row.get("unit_key")
        if not isinstance(key, str) or not re.fullmatch(r"[0-9a-f]{64}", key) or key in seen:
            raise ValueError("Invalid or duplicate Japanese title repair key")
        seen.add(key)
        if any(not isinstance(row.get(field), str) or not row[field].strip()
               for field in ("source", "translation", "report_id", "source_title", "translation_title")):
            raise ValueError("Incomplete Japanese title repair row")
        observed = row.get("observed_translations")
        if not isinstance(observed, list) or not observed or any(not isinstance(value, str) or not value.strip() for value in observed):
            raise ValueError("Missing reviewed erroneous Japanese title")
        if row["translation"] in observed:
            raise ValueError("Japanese title correction equals an erroneous value")
        if Counter(_PLACEHOLDER.findall(row["source"])) != Counter(_PLACEHOLDER.findall(row["translation"])):
            raise ValueError("Japanese title correction changed protected placeholders")
    return repairs


def apply_ja_catalog_title_repairs(
    cache: dict[str, Any],
    units: Mapping[str, Any],
    *,
    repairs: Iterable[Mapping[str, Any]] | None = None,
) -> dict[str, int]:
    """Repair matching current-inventory JA rows; preserve other paid cache data.

    Call after loading the cache and collecting units, before missing-unit
    translation. Keys and canonical sources must both match the current builder
    inventory. Thus a changed source or prompt namespace never gets an old fix.
    """
    entries = cache.get("locales", {}).get("ja")
    if not isinstance(entries, dict):
        raise ValueError("Translation cache is missing its Japanese namespace")
    counts = {"replaced": 0, "seeded": 0, "preserved": 0, "unmatched": 0}
    for repair in load_repairs() if repairs is None else repairs:
        key = repair["unit_key"]
        unit = units.get(key)
        if unit is None or unit.key != key or unit.source != repair["source"]:
            counts["unmatched"] += 1
            continue
        previous = entries.get(key)
        if previous is None:
            entries[key] = {"source": repair["source"], "translation": repair["translation"]}
            counts["seeded"] += 1
        elif (isinstance(previous, dict) and previous.get("source") == repair["source"]
              and str(previous.get("translation") or "").strip() in repair["observed_translations"]):
            # Preserve unrelated provenance fields on this exact cache row.
            entries[key] = {**previous, "translation": repair["translation"]}
            counts["replaced"] += 1
        else:
            counts["preserved"] += 1
    return counts
