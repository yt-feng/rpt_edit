"""Validate complete locale coverage, including explicitly retained source units."""

from __future__ import annotations

import base64
import binascii
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable
import zlib


MAX_LOCALE_MANIFEST_BYTES = 16 * 1024 * 1024
MAX_EXPANDED_FALLBACK_BYTES = 64 * 1024 * 1024
MAX_FALLBACK_REFERENCES = 300_000


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
    return _expand_fallback_records(manifest)


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


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _expand_fallback_records(manifest: dict[str, Any]) -> dict[str, Any]:
    """Decode a lossless intern table without weakening the 16 MiB wire limit."""
    fallback = manifest.get("source_fallbacks")
    if isinstance(fallback, dict) and fallback.get("schema_version") == 3:
        fallback = _decompress_fallback_records(fallback)
        manifest = dict(manifest, source_fallbacks=fallback)
    if not isinstance(fallback, dict) or fallback.get("schema_version") != 2:
        return manifest
    records, units = fallback.get("records"), fallback.get("units")
    if (set(fallback) != {"schema_version", "records", "units", "counts"}
            or not isinstance(records, list) or len(records) > MAX_FALLBACK_REFERENCES
            or not isinstance(units, dict) or not units or len(units) > 64):
        raise LocaleManifestError("Invalid interned source fallback table")
    if any(not isinstance(row, dict) for row in records):
        raise LocaleManifestError("Invalid interned source fallback record")
    sizes = [len(_json_bytes(row)) for row in records]
    expanded, used, total, references = {}, set(), 0, 0
    for locale, rows in units.items():
        if not isinstance(rows, dict):
            raise LocaleManifestError("Invalid interned source fallback locale")
        expanded[locale] = {}
        for key, index in rows.items():
            if type(index) is not int or not 0 <= index < len(records):
                raise LocaleManifestError("Invalid interned source fallback reference")
            total += sizes[index] + len(key.encode("utf-8")) + 8
            references += 1
            if total > MAX_EXPANDED_FALLBACK_BYTES or references > MAX_FALLBACK_REFERENCES:
                raise LocaleManifestError(
                    "Expanded source fallback table exceeds safety budget: "
                    f"bytes={total}/{MAX_EXPANDED_FALLBACK_BYTES}, "
                    f"references={references}/{MAX_FALLBACK_REFERENCES}"
                )
            used.add(index)
            expanded[locale][key] = dict(records[index])
    if used != set(range(len(records))):
        raise LocaleManifestError("Unused interned source fallback record")
    manifest = dict(manifest)
    manifest["source_fallbacks"] = {"schema_version": 1, "counts": fallback["counts"], "units": expanded}
    # Verify the original source hashes, identities, counts and coverage after
    # resolving references. Compaction never upgrades source text to translation.
    validate_translation_resolution(manifest, units.keys())
    return manifest


def _decompress_fallback_records(fallback: dict[str, Any]) -> dict[str, Any]:
    """Read one bounded stream; recover the shared keys before validating records."""
    if (set(fallback) != {"schema_version", "encoding", "byte_size", "sha256", "data"}
            or type(fallback["schema_version"]) is not int
            or fallback["encoding"] != "zlib-base64"
            or type(fallback["byte_size"]) is not int
            or not 0 < fallback["byte_size"] <= MAX_EXPANDED_FALLBACK_BYTES
            or not isinstance(fallback["sha256"], str)
            or not isinstance(fallback["data"], str)):
        raise LocaleManifestError("Invalid compressed source fallback table")
    try:
        compressed = base64.b64decode(fallback["data"], validate=True)
        stream = zlib.decompressobj()
        # Never call unbounded decompress/flush, even for a false declared size.
        body = stream.decompress(compressed, fallback["byte_size"] + 1)
    except (ValueError, binascii.Error, zlib.error) as error:
        raise LocaleManifestError("Invalid compressed source fallback data") from error
    if (len(body) != fallback["byte_size"] or not stream.eof
            or stream.unconsumed_tail or stream.unused_data):
        raise LocaleManifestError("Compressed source fallback size or stream differs")
    if hashlib.sha256(body).hexdigest() != fallback["sha256"]:
        raise LocaleManifestError("Compressed source fallback hash differs")
    try:
        table = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeError, RecursionError) as error:
        raise LocaleManifestError("Compressed source fallback must contain UTF-8 JSON") from error
    if (not isinstance(table, dict) or set(table) != {"keys", "records", "units", "counts"}
            or not isinstance(table["keys"], list) or len(table["keys"]) > MAX_FALLBACK_REFERENCES
            or any(not isinstance(key, str) for key in table["keys"])
            or len(set(table["keys"])) != len(table["keys"])
            or not isinstance(table["units"], dict) or not 0 < len(table["units"]) <= 64):
        raise LocaleManifestError("Compressed source fallback must contain an intern table")
    keys, units, used, references = table["keys"], {}, set(), 0
    for locale, rows in table["units"].items():
        if not isinstance(rows, list):
            raise LocaleManifestError("Invalid compressed source fallback locale")
        references += len(rows)
        if references > MAX_FALLBACK_REFERENCES:
            raise LocaleManifestError("Expanded source fallback table exceeds safety budget")
        units[locale] = {}
        for row in rows:
            if (not isinstance(row, list) or len(row) != 2 or type(row[0]) is not int
                    or not 0 <= row[0] < len(keys) or keys[row[0]] in units[locale]):
                raise LocaleManifestError("Invalid compressed source fallback key reference")
            used.add(row[0])
            units[locale][keys[row[0]]] = row[1]
    if used != set(range(len(keys))):
        raise LocaleManifestError("Unused compressed source fallback key")
    return {"schema_version": 2, "records": table["records"],
            "counts": table["counts"], "units": units}


def _compress_fallback_records(fallback: dict[str, Any]) -> dict[str, Any]:
    # The same source identity appears in every locale. Store it once before
    # compression, rather than relying on zlib's limited sliding dictionary.
    keys = sorted({key for rows in fallback["units"].values() for key in rows})
    indexes = {key: index for index, key in enumerate(keys)}
    table = _json_bytes({
        "keys": keys, "records": fallback["records"], "counts": fallback["counts"],
        "units": {locale: [[indexes[key], index] for key, index in sorted(rows.items())]
                  for locale, rows in sorted(fallback["units"].items())},
    })
    if len(table) > MAX_EXPANDED_FALLBACK_BYTES:
        raise LocaleManifestError("Expanded source fallback table exceeds safety budget")
    return {"schema_version": 3, "encoding": "zlib-base64", "byte_size": len(table),
            "sha256": hashlib.sha256(table).hexdigest(),
            "data": base64.b64encode(zlib.compress(table, level=9)).decode("ascii")}


def encode_locale_manifest(manifest: dict[str, Any]) -> bytes:
    """Keep legacy output when it fits; losslessly pack fallback provenance otherwise.

    Every source, reason, context and per-language count round-trips unchanged.
    No truncation, paid retranslation or larger unbounded fetch is introduced.
    """
    body = _json_bytes(manifest)
    if len(body) <= MAX_LOCALE_MANIFEST_BYTES:
        parse_locale_manifest(body)
        return body
    fallback = manifest.get("source_fallbacks")
    if not isinstance(fallback, dict) or fallback.get("schema_version") != 1:
        parse_locale_manifest(body)  # Retain the original explicit size error.
    units = fallback.get("units")
    if not isinstance(units, dict):
        raise LocaleManifestError("Invalid source fallback units")
    validate_translation_resolution(manifest, units.keys())
    records, indexes, refs = [], {}, {}
    for locale in sorted(units):
        refs[locale] = {}
        for key, row in sorted(units[locale].items()):
            identity = _json_bytes(row)
            if identity not in indexes:
                indexes[identity] = len(records)
                records.append(row)
            refs[locale][key] = indexes[identity]
    packed = dict(manifest)
    packed["source_fallbacks"] = {"schema_version": 2, "records": records,
                                 "units": refs, "counts": fallback["counts"]}
    body = _json_bytes(packed)
    if len(body) > MAX_LOCALE_MANIFEST_BYTES:
        # Whole-row interning alone stops helping as new sources and distinct
        # language provenance accumulate. Compress only the intern table; all
        # route descriptors and coverage remain ordinary readable JSON.
        _expand_fallback_records(packed)
        packed["source_fallbacks"] = _compress_fallback_records(packed["source_fallbacks"])
        body = _json_bytes(packed)
    decoded = parse_locale_manifest(body)
    if decoded != manifest:
        raise LocaleManifestError("Source fallback compaction changed manifest semantics")
    return body
