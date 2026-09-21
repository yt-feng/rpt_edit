"""Validate complete locale coverage, including explicitly retained source units."""

from __future__ import annotations

import hashlib
from typing import Any, Iterable


class LocaleManifestError(ValueError):
    """A locale manifest does not account for its source units faithfully."""


def validate_translation_resolution(manifest: dict[str, Any], locales: Iterable[str]) -> None:
    expected = set(locales)

    def require(condition: bool, detail: str) -> None:
        if not condition:
            raise LocaleManifestError(f"Multilingual manifest is incomplete: {detail}")

    def locale_map(value: Any, label: str) -> dict[str, Any]:
        require(isinstance(value, dict) and set(value) == expected, f"invalid {label} locales")
        return value

    def count(value: Any, label: str) -> int:
        require(isinstance(value, int) and not isinstance(value, bool) and value >= 0,
                f"invalid {label}")
        return value

    def ratio(value: Any, expected_value: float, label: str) -> None:
        require(isinstance(value, (int, float)) and not isinstance(value, bool)
                and value == expected_value,
                f"invalid {label}")

    coverage = locale_map(manifest.get("coverage"), "coverage")
    if "source_fallbacks" not in manifest:
        # Existing fully translated releases retain their original contract.
        for locale in expected:
            ratio(coverage[locale], 1.0, f"coverage.{locale}")
        return

    fallback = manifest["source_fallbacks"]
    require(isinstance(fallback, dict) and type(fallback.get("schema_version")) is int
            and fallback["schema_version"] == 1,
            "invalid source fallback schema")
    units = locale_map(fallback.get("units"), "source fallback units")
    counts = locale_map(fallback.get("counts"), "source fallback counts")
    translated = locale_map(manifest.get("translation_entry_count"), "translation entry counts")
    resolved = locale_map(manifest.get("resolved_entry_count"), "resolved entry counts")
    resolved_coverage = locale_map(manifest.get("resolved_coverage"), "resolved coverage")
    source_count = count(manifest.get("source_unit_count"), "source unit count")
    prompt_version = manifest.get("prompt_version")
    require(isinstance(prompt_version, str) and bool(prompt_version.strip()) and "\0" not in prompt_version,
            "invalid prompt version")
    for locale in expected:
        rows = units[locale]
        require(isinstance(rows, dict), f"invalid source fallback units.{locale}")
        require(count(counts[locale], f"source fallback count.{locale}") == len(rows),
                f"source fallback count differs for {locale}")
        for key, row in rows.items():
            require(isinstance(row, dict), f"invalid source fallback row for {locale}")
            source = row.get("source")
            context = row.get("context")
            reason = row.get("reason")
            translation_class = row.get("translation_class")
            require(isinstance(source, str) and bool(source.strip())
                    and isinstance(context, str) and bool(context.strip())
                    and isinstance(reason, str) and bool(reason.strip())
                    and isinstance(translation_class, str) and translation_class in {"copy", "official-name"},
                    f"invalid source fallback provenance for {locale}")
            require(row.get("source_sha256") == hashlib.sha256(source.encode("utf-8")).hexdigest(),
                    f"source fallback hash differs for {locale}")
            identity = f"{prompt_version}\0{translation_class}\0{source}".encode("utf-8")
            require(key == hashlib.sha256(identity).hexdigest(),
                    f"source fallback identity differs for {locale}")
        translated_count = count(translated[locale], f"translation entry count.{locale}")
        resolved_count = count(resolved[locale], f"resolved entry count.{locale}")
        require(translated_count + len(rows) == resolved_count == source_count,
                f"unaccounted source units for {locale}")
        ratio(coverage[locale], translated_count / source_count if source_count else 1.0,
              f"coverage.{locale}")
        ratio(resolved_coverage[locale], 1.0, f"resolved coverage.{locale}")
