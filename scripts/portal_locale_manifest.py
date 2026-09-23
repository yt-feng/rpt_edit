"""Validate complete locale coverage, including explicitly retained source units."""

from __future__ import annotations

import hashlib
import json
from pathlib import Path
from typing import Any, Iterable

from portal_language_registry import DEFAULT_LOCALES, LANGUAGES


MAX_LOCALE_MANIFEST_BYTES = 16 * 1024 * 1024


class LocaleManifestError(ValueError):
    """A locale manifest does not account for its source units faithfully."""


def parse_locale_manifest(body: bytes) -> dict[str, Any]:
    """Use one bounded input contract for generated, staged, and live manifests."""
    if not isinstance(body, bytes) or not 0 < len(body) <= MAX_LOCALE_MANIFEST_BYTES:
        actual = len(body) if isinstance(body, bytes) else "invalid"
        raise LocaleManifestError(
            f"Locale manifest byte size {actual} is outside 1..{MAX_LOCALE_MANIFEST_BYTES}"
        )
    try:
        manifest = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeError, RecursionError) as error:
        raise LocaleManifestError("Locale manifest must be valid UTF-8 JSON") from error
    if not isinstance(manifest, dict) or type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
        raise LocaleManifestError("Locale manifest schema is invalid")
    return manifest


def load_locale_manifest(path: Path) -> dict[str, Any]:
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise LocaleManifestError("Locale manifest must be a regular non-symlink file")
    size = path.stat().st_size
    if not 0 < size <= MAX_LOCALE_MANIFEST_BYTES:
        raise LocaleManifestError(
            f"Locale manifest byte size {size} is outside 1..{MAX_LOCALE_MANIFEST_BYTES}"
        )
    with path.open("rb") as handle:
        return parse_locale_manifest(handle.read(MAX_LOCALE_MANIFEST_BYTES + 1))


def validate_translation_resolution(manifest: dict[str, Any], locales: Iterable[str]) -> None:
    expected = set(locales)
    if not expected or not expected.issubset(LANGUAGES):
        raise LocaleManifestError("Unknown locale coverage")

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
        if locale not in DEFAULT_LOCALES:
            require(rows == {} and counts[locale] == 0, f"source fallback forbidden for expanded locale {locale}")
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
