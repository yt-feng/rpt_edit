#!/usr/bin/env python3
"""Inspect public JavaScript using an existing cache, without provider calls."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import build_portal_locales as builder


def audit(assets: Path, cache_path: Path, output: Path) -> dict:
    cache = builder.load_cache(cache_path)
    output.mkdir(parents=True, exist_ok=True)
    report = {"schema_version": 1, "provider_requests": 0, "status": "passed", "assets": []}
    public_units = {}
    for name in builder.LOCALIZED_JS_ASSETS:
        source = (assets / name).read_text(encoding="utf-8")
        builder.collect_javascript_units(source, name, public_units)
        for locale in builder.LOCALES:
            row = {"asset": name, "locale": locale, "status": "passed"}
            report["assets"].append(row)
            try:
                localized = builder.render_localized_javascript(source, name, locale, cache)
                target = output / locale / name
                target.parent.mkdir(parents=True, exist_ok=True)
                target.write_text(localized, encoding="utf-8")
                builder.validate_localized_javascript_residuals(source, localized, name, locale, cache)
            except builder.TranslationError as error:
                row.update(status="failed", error=str(error))
                report["status"] = "failed"
                if "localized" not in locals():
                    continue
                suspects = []
                for original, translated in zip(
                    builder.iter_javascript_literal_parts(source),
                    builder.iter_javascript_literal_parts(localized),
                ):
                    nested, start, end, value = original
                    translated_value = translated[3]
                    if (not builder.CJK_RE.search(translated_value)
                            or builder.javascript_literal_is_transport_data(nested, start, end)):
                        continue
                    if (builder.CJK_RE.search(value)
                            and builder.javascript_cjk_literal_is_allowlisted(value, nested, start, end)):
                        continue
                    _, unit = builder.unit_for_text(value, f"javascript:{name}")
                    cached = cache["locales"][locale].get(unit.key, {}) if unit else {}
                    suspects.append({
                        "source": value, "localized": translated_value,
                        "canonical_source": unit.source if unit else None,
                        "cache_translation": cached.get("translation"),
                        "entity_name": cached.get("entity_name"),
                        "ja_keyword_name": cached.get("ja_keyword_name"),
                        "cache_valid": builder._valid_cache_row(locale, unit, cached) if unit else None,
                    })
                row["cjk_candidates"] = suspects
            finally:
                if "localized" in locals():
                    del localized
    # Export only rows belonging to these public scripts for reproducible,
    # offline debugging. Never rewrite the restored, paid translation cache.
    subset = builder.empty_cache()
    for locale in builder.LOCALES:
        subset["locales"][locale] = {
            key: cache["locales"][locale][key]
            for key in public_units if key in cache["locales"][locale]
        }
    builder.write_cache(output / "public-script-cache.json.gz", subset)
    (output / "audit.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--assets", type=Path, required=True)
    parser.add_argument("--cache", type=Path, required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    report = audit(args.assets, args.cache, args.output)
    # This command collects diagnostics; it is not a publication approval gate.
    print(json.dumps({key: report[key] for key in ("status", "provider_requests")}))


if __name__ == "__main__":
    main()
