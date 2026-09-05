#!/usr/bin/env python3
"""Bounded grouped DeepL checks, without website or production cache writes."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import build_portal_locales as builder
from deepl_locale_repair import DeepLRepair

SOURCES = (
    "，比去年同期提升__KC_PH_000__个百分点。",
    "MS-Walt Disney Co（DIS.UN）The Force Awakens – Reiterate OW-__KC_PH_000__",
    "区间，远低于",
)


def run_preflight(path: Path, *, repair=None) -> dict:
    report = {"mode": "deepl", "status": "running", "samples": [], "provider_requests": 0,
              "max_provider_requests": 6, "max_source_characters": 3000, "billed_characters": 0}
    try:
        if sum(len(text.encode("utf-8")) for text in SOURCES) * len(builder.LOCALES) > 3000:
            raise ValueError("DeepL preflight exceeds its source bound")
        repair = repair or DeepLRepair(max_requests=6)
        for locale in builder.LOCALES:
            translations = repair.translate_many(locale, list(SOURCES))
            for index, (source, text) in enumerate(zip(SOURCES, translations, strict=True)):
                unit = builder.TranslationUnit(f"{index:064x}", "html:text:p", source)
                builder.validate_translation_quality(locale, unit, text)
                report["samples"].append({"locale": locale, "source": source, "translation": text})
        report["status"] = "passed"
    except Exception as error:
        report.update(status="failed", error_type=type(error).__name__)
    finally:
        if repair is not None:
            snapshot = repair.snapshot()
            report.update({key: snapshot[key] for key in (
                "provider_requests", "balance_requests", "billed_characters", "reserved_characters", "remaining_character_budget"
            ) if key in snapshot})
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--diagnostics-out", type=Path, required=True)
    args = parser.parse_args()
    report = run_preflight(args.diagnostics_out)
    print(json.dumps({key: report.get(key) for key in ("status", "provider_requests", "billed_characters", "remaining_character_budget")}))
    return 0 if report["status"] == "passed" else 1


if __name__ == "__main__":
    raise SystemExit(main())
