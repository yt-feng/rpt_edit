"""Validate complete locale coverage, including explicitly retained source units."""

from __future__ import annotations

import base64
import binascii
import hashlib
import json
from pathlib import Path
import re
from typing import Any, Callable, Iterable, Iterator
import zlib


MAX_LOCALE_MANIFEST_BYTES = 16 * 1024 * 1024
# Bound the decoded table and retained records plus reference keys. Locale maps
# share their interned records; never recreate one full record per language.
MAX_EXPANDED_FALLBACK_BYTES = 64 * 1024 * 1024
MAX_FALLBACK_REFERENCES = 300_000
MAX_FALLBACK_SHARDS = 4096
FALLBACK_SHARD_DIRECTORY = "data/i18n/source-fallbacks"
_DERIVED_HASH_RECORD_FIELDS = frozenset({"source", "context", "reason", "translation_class"})


class LocaleManifestError(ValueError):
    """A locale manifest does not account for its source units faithfully."""


class _ShardBudgetExceeded(LocaleManifestError):
    """Only a valid shard exceeding a size budget may be split further."""


class _VerifiedLocaleManifest(dict):
    """In-process proof that every bound shard was read and validated.

    JSON can never supply this capability. Its fingerprint binds all root
    metadata, so a caller cannot change counts or coverage after verification.
    No decoded source rows survive the individual shard validation.
    """

    def __init__(self, manifest: dict[str, Any], counts: dict[str, int]):
        super().__init__(manifest)
        self._verified_fingerprint = hashlib.sha256(_json_bytes(manifest)).digest()
        self._verified_counts = tuple(sorted(counts.items()))


class _SharedFallbackRecord(dict):
    """A shared provenance row cannot be changed through one locale's view."""

    def _readonly(self, *args: Any, **kwargs: Any) -> None:
        raise TypeError("Source fallback provenance is read-only; copy the record before editing")

    __setitem__ = __delitem__ = clear = pop = popitem = setdefault = update = __ior__ = _readonly

    def __copy__(self) -> dict[str, Any]:
        return dict(self)

    def __deepcopy__(self, memo: dict[int, Any]) -> dict[str, Any]:
        import copy
        return _SharedFallbackRecord(copy.deepcopy(dict(self), memo))


def parse_locale_manifest(body: bytes, *,
                          shard_resolver: Callable[[dict[str, Any]], bytes] | None = None) -> dict[str, Any]:
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
    if isinstance(manifest.get("source_fallbacks"), dict) and manifest["source_fallbacks"].get("schema_version") == 5:
        return _verify_sharded_manifest(manifest, shard_resolver)
    return _expand_fallback_records(manifest)


def load_locale_manifest(path: Path) -> dict[str, Any]:
    return read_locale_manifest_bundle(path)[1]


def read_locale_manifest_bundle(path: Path) -> tuple[bytes, dict[str, Any]]:
    """Return the exact bounded root bytes whose complete bundle was validated."""
    body = _read_local_manifest_body(path)
    manifest = parse_locale_manifest(body, shard_resolver=lambda descriptor: _read_local_shard(path, descriptor))
    return body, manifest


def _read_local_manifest_body(path: Path) -> bytes:
    path = Path(path)
    if path.is_symlink() or not path.is_file():
        raise LocaleManifestError("Locale manifest must be a regular non-symlink file")
    size = path.stat().st_size
    if not 0 < size <= MAX_LOCALE_MANIFEST_BYTES:
        raise LocaleManifestError(
            f"Locale manifest byte size {size} is outside 1..{MAX_LOCALE_MANIFEST_BYTES}"
        )
    with path.open("rb") as handle:
        return handle.read(MAX_LOCALE_MANIFEST_BYTES + 1)


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
            and fallback["schema_version"] in {1, 5},
            "invalid source fallback schema")
    sharded = fallback["schema_version"] == 5
    if sharded:
        require(isinstance(manifest, _VerifiedLocaleManifest)
                and manifest._verified_fingerprint == hashlib.sha256(_json_bytes(manifest)).digest(),
                "source fallback shards have not been verified or root metadata changed")
        verified_counts = dict(manifest._verified_counts)
        require(verified_counts == fallback.get("counts"), "verified shard counts differ")
    else:
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
        rows = {} if sharded else units[locale]
        require(isinstance(rows, dict), f"invalid source fallback units.{locale}")
        fallback_count = verified_counts[locale] if sharded else len(rows)
        require(count(counts[locale], f"source fallback count.{locale}") == fallback_count,
                f"source fallback count differs for {locale}")
        for key, row in rows.items():
            _validate_fallback_row(key, row, prompt_version, locale)
        translated_count = count(translated[locale], f"translation entry count.{locale}")
        resolved_count = count(resolved[locale], f"resolved entry count.{locale}")
        require(translated_count + fallback_count == resolved_count == source_count,
                f"unaccounted source units for {locale}")
        ratio(coverage[locale], translated_count / source_count if source_count else 1.0,
              f"coverage.{locale}")
        ratio(resolved_coverage[locale], 1.0, f"resolved coverage.{locale}")


def _json_bytes(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def _validate_fallback_row(key: Any, row: Any, prompt_version: str, locale: str) -> None:
    if not isinstance(row, dict):
        raise LocaleManifestError(f"Invalid source fallback row for {locale}")
    source, context, reason, translation_class = (row.get(field) for field in
                                                  ("source", "context", "reason", "translation_class"))
    if (not isinstance(source, str) or not source.strip()
            or not isinstance(context, str) or not context.strip()
            or not isinstance(reason, str) or not reason.strip()
            or not isinstance(translation_class, str) or translation_class not in {"copy", "official-name"}):
        raise LocaleManifestError(f"Invalid source fallback provenance for {locale}")
    if row.get("source_sha256") != hashlib.sha256(source.encode("utf-8")).hexdigest():
        raise LocaleManifestError(f"source fallback hash differs for {locale}")
    identity = f"{prompt_version}\0{translation_class}\0{source}".encode("utf-8")
    if key != hashlib.sha256(identity).hexdigest():
        raise LocaleManifestError(f"source fallback identity differs for {locale}")


def locale_manifest_shard_descriptors(manifest: dict[str, Any]) -> list[dict[str, Any]]:
    """Validate the index before any resolver sees an untrusted path.

    Prefix-free partitions exclude duplicates across shards without keeping a
    release-wide set of keys. Paths are content-addressed in one fixed namespace.
    This validates the index only; resolution acceptance still needs the reader.
    """
    fallback = manifest.get("source_fallbacks")
    if not isinstance(fallback, dict) or fallback.get("schema_version") != 5:
        return []
    counts, shards = fallback.get("counts"), fallback.get("shards")
    if (set(fallback) != {"schema_version", "counts", "shards"}
            or type(fallback["schema_version"]) is not int
            or not isinstance(counts, dict) or not 0 < len(counts) <= 64
            or any(not isinstance(locale, str) or not locale
                   or type(value) is not int or value < 0 for locale, value in counts.items())
            or not isinstance(shards, list) or not 0 < len(shards) <= MAX_FALLBACK_SHARDS):
        raise LocaleManifestError("Invalid source fallback shard index")
    previous = ""
    result = []
    for descriptor in shards:
        if not isinstance(descriptor, dict) or set(descriptor) != {"prefix", "path", "byte_size", "sha256"}:
            raise LocaleManifestError("Invalid source fallback shard descriptor")
        prefix, digest, size = descriptor["prefix"], descriptor["sha256"], descriptor["byte_size"]
        if (not isinstance(prefix, str) or not re.fullmatch(r"[0-9a-f]{1,64}", prefix)
                or not isinstance(digest, str) or not re.fullmatch(r"[0-9a-f]{64}", digest)
                or type(size) is not int or not 0 < size <= MAX_LOCALE_MANIFEST_BYTES
                or descriptor["path"] != f"{FALLBACK_SHARD_DIRECTORY}/{prefix}-{digest}.json"
                or (previous and (prefix <= previous or prefix.startswith(previous)))):
            raise LocaleManifestError("Invalid or overlapping source fallback shard partition")
        previous = prefix
        result.append(dict(descriptor))
    return result


def _decode_fallback_shard(body: bytes, descriptor: dict[str, Any], prompt_version: str,
                           locales: set[str]) -> dict[str, Any]:
    if (not isinstance(body, bytes) or len(body) != descriptor["byte_size"]
            or len(body) > MAX_LOCALE_MANIFEST_BYTES
            or hashlib.sha256(body).hexdigest() != descriptor["sha256"]):
        raise LocaleManifestError("Source fallback shard byte size or hash differs")
    try:
        shard = json.loads(body.decode("utf-8"))
    except (ValueError, UnicodeError, RecursionError) as error:
        raise LocaleManifestError("Source fallback shard must be UTF-8 JSON") from error
    if (not isinstance(shard, dict) or set(shard) != {"schema_version", "prefix", "prompt_version", "source_fallbacks"}
            or type(shard["schema_version"]) is not int or shard["schema_version"] != 1
            or shard["prefix"] != descriptor["prefix"] or shard["prompt_version"] != prompt_version
            or not isinstance(shard["source_fallbacks"], dict)
            or shard["source_fallbacks"].get("schema_version") != 4):
        raise LocaleManifestError("Invalid source fallback shard schema or identity")
    fallback = _expand_fallback_records(shard, validate_resolution=False)["source_fallbacks"]
    if (set(fallback["units"]) != locales or not isinstance(fallback.get("counts"), dict)
            or set(fallback["counts"]) != locales):
        raise LocaleManifestError("Source fallback shard locales differ")
    references = 0
    for locale, rows in fallback["units"].items():
        if type(fallback["counts"][locale]) is not int or fallback["counts"][locale] != len(rows):
            raise LocaleManifestError("Source fallback shard counts differ")
        references += len(rows)
        for key, row in rows.items():
            if not key.startswith(descriptor["prefix"]):
                raise LocaleManifestError("Source fallback key lies outside its shard partition")
            _validate_fallback_row(key, row, prompt_version, locale)
    if not references:
        raise LocaleManifestError("Empty source fallback shard")
    return fallback


def _verify_sharded_manifest(manifest: dict[str, Any],
                             resolver: Callable[[dict[str, Any]], bytes] | None) -> dict[str, Any]:
    descriptors = locale_manifest_shard_descriptors(manifest)
    prompt_version = manifest.get("prompt_version")
    if not isinstance(prompt_version, str) or not prompt_version.strip() or "\0" in prompt_version:
        raise LocaleManifestError("Invalid source fallback prompt version")
    if resolver is None:
        raise LocaleManifestError("Source fallback shards require a bounded resolver")
    counts = {locale: 0 for locale in manifest["source_fallbacks"]["counts"]}
    for descriptor in descriptors:
        body = resolver(dict(descriptor))
        fallback = _decode_fallback_shard(body, descriptor, prompt_version, set(counts))
        for locale in counts:
            counts[locale] += fallback["counts"][locale]
        # Only aggregate counts survive. The next resolver runs after all
        # records, reference dictionaries and bytes for this leaf are released.
        del fallback, body
    verified = _VerifiedLocaleManifest(manifest, counts)
    validate_translation_resolution(verified, counts)
    return verified


def _local_shard_path(manifest_path: Path, descriptor: dict[str, Any]) -> Path:
    # A root can be renamed (e.g. downloaded evidence); shards are always its
    # source-fallbacks sibling. Never follow a symlink at the bundle directory
    # or below it; system aliases above this caller-selected anchor are allowed.
    relative = Path(descriptor["path"]).relative_to("data/i18n")
    parent = Path(manifest_path).parent
    if parent.is_symlink():
        raise LocaleManifestError("Locale manifest bundle must not contain symlinks")
    candidate = parent
    for component in relative.parts:
        candidate = candidate / component
        if candidate.is_symlink():
            raise LocaleManifestError("Source fallback shard must not be a symlink")
    return candidate


def _read_local_shard(manifest_path: Path, descriptor: dict[str, Any]) -> bytes:
    path = _local_shard_path(manifest_path, descriptor)
    if not path.is_file() or path.stat().st_size != descriptor["byte_size"]:
        raise LocaleManifestError("Source fallback shard is missing or its byte size differs")
    with path.open("rb") as handle:
        return handle.read(descriptor["byte_size"] + 1)


def copy_locale_manifest_bundle(manifest_path: Path, destination_path: Path) -> None:
    """Copy every verified dependency, then the root, into a validation artifact."""
    manifest_path, destination_path = Path(manifest_path), Path(destination_path)
    root_body, manifest = read_locale_manifest_bundle(manifest_path)
    destination_path.parent.mkdir(parents=True, exist_ok=True)
    for descriptor in locale_manifest_shard_descriptors(manifest):
        destination = _local_shard_path(destination_path, descriptor)
        destination.parent.mkdir(parents=True, exist_ok=True)
        body = _read_local_shard(manifest_path, descriptor)
        if hashlib.sha256(body).hexdigest() != descriptor["sha256"]:
            raise LocaleManifestError("Source fallback shard changed during artifact copy")
        destination.write_bytes(body)
    # Do not reread the source root: it could have changed after verification.
    _write_bundle_root(destination_path, root_body)
    _remove_unused_fallback_shards(destination_path, locale_manifest_shard_descriptors(manifest))


def _expand_fallback_records(manifest: dict[str, Any], *, validate_resolution: bool = True) -> dict[str, Any]:
    """Resolve references while keeping interned records shared and bounded.

    These are read-only release manifests. Returning the same record for each
    reference preserves the intern table's storage bound through all readers;
    copying it per locale undid compaction and hit the cap as the catalog grew.
    """
    fallback = manifest.get("source_fallbacks")
    if isinstance(fallback, dict) and (type(fallback.get("schema_version")) is not int
                                      or fallback["schema_version"] not in {1, 2, 3, 4}):
        raise LocaleManifestError("Unsupported source fallback schema")
    if isinstance(fallback, dict) and fallback.get("schema_version") in {3, 4}:
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
    records = [_SharedFallbackRecord(row) for row in records]
    total = sum(len(_json_bytes(row)) for row in records)
    if total > MAX_EXPANDED_FALLBACK_BYTES:
        raise LocaleManifestError("Retained source fallback table exceeds safety budget")
    expanded, used, references = {}, set(), 0
    for locale, rows in units.items():
        if not isinstance(rows, dict):
            raise LocaleManifestError("Invalid interned source fallback locale")
        expanded[locale] = {}
        for key, index in rows.items():
            if not isinstance(key, str) or type(index) is not int or not 0 <= index < len(records):
                raise LocaleManifestError("Invalid interned source fallback reference")
            # Full source/context/reason strings remain in records once. The
            # locale map retains only its key and reference to that same row.
            total += len(key.encode("utf-8")) + 8
            references += 1
            if total > MAX_EXPANDED_FALLBACK_BYTES or references > MAX_FALLBACK_REFERENCES:
                raise LocaleManifestError(
                    "Retained source fallback table exceeds safety budget: "
                    f"bytes={total}/{MAX_EXPANDED_FALLBACK_BYTES}, "
                    f"references={references}/{MAX_FALLBACK_REFERENCES}"
                )
            used.add(index)
            expanded[locale][key] = records[index]
    if used != set(range(len(records))):
        raise LocaleManifestError("Unused interned source fallback record")
    manifest = dict(manifest)
    manifest["source_fallbacks"] = {"schema_version": 1, "counts": fallback["counts"], "units": expanded}
    # Verify the original source hashes, identities, counts and coverage after
    # resolving references. Compaction never upgrades source text to translation.
    if validate_resolution:
        validate_translation_resolution(manifest, units.keys())
    return manifest


def _decompress_fallback_records(fallback: dict[str, Any]) -> dict[str, Any]:
    """Read one bounded stream; recover the shared keys before validating records."""
    if (set(fallback) != {"schema_version", "encoding", "byte_size", "sha256", "data"}
            or type(fallback["schema_version"]) is not int
            or fallback["schema_version"] not in {3, 4}
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
    if fallback["schema_version"] == 4:
        # Schema 4 omits only a digest derived from source text. Retain the
        # original unit keys: prompt/class/source identity is still validated
        # by _expand_fallback_records after reconstructing the digest.
        records = table["records"]
        if not isinstance(records, list) or len(records) > MAX_FALLBACK_REFERENCES:
            raise LocaleManifestError("Invalid derived-hash source fallback records")
        retained = 0
        restored = []
        for row in records:
            if (not isinstance(row, dict) or set(row) != _DERIVED_HASH_RECORD_FIELDS
                    or not isinstance(row["source"], str)):
                raise LocaleManifestError("Invalid derived-hash source fallback record")
            row = dict(row, source_sha256=hashlib.sha256(row["source"].encode("utf-8")).hexdigest())
            # Reconstructed hashes count toward the same retained-byte budget.
            retained += len(_json_bytes(row))
            if retained > MAX_EXPANDED_FALLBACK_BYTES:
                raise LocaleManifestError("Retained source fallback table exceeds safety budget")
            restored.append(row)
        table["records"] = restored
    return {"schema_version": 2, "records": table["records"],
            "counts": table["counts"], "units": units}


def _compress_fallback_records(fallback: dict[str, Any], *, schema_version: int = 3) -> dict[str, Any]:
    if type(schema_version) is not int or schema_version not in {3, 4}:
        raise LocaleManifestError("Unsupported compressed source fallback schema")
    records = fallback["records"]
    if schema_version == 4:
        compact = []
        for row in records:
            if (not isinstance(row, dict) or set(row) != _DERIVED_HASH_RECORD_FIELDS | {"source_sha256"}
                    or not isinstance(row["source"], str)
                    or row["source_sha256"] != hashlib.sha256(row["source"].encode("utf-8")).hexdigest()):
                raise LocaleManifestError("Invalid source fallback hash before compaction")
            compact.append({key: value for key, value in row.items() if key != "source_sha256"})
        records = compact
    # The same source identity appears in every locale. Store it once before
    # compression, rather than relying on zlib's limited sliding dictionary.
    keys = sorted({key for rows in fallback["units"].values() for key in rows})
    indexes = {key: index for index, key in enumerate(keys)}
    table = _json_bytes({
        "keys": keys, "records": records, "counts": fallback["counts"],
        "units": {locale: [[indexes[key], index] for key, index in sorted(rows.items())]
                  for locale, rows in sorted(fallback["units"].items())},
    })
    if len(table) > MAX_EXPANDED_FALLBACK_BYTES:
        raise _ShardBudgetExceeded("Expanded source fallback table exceeds safety budget")
    return {"schema_version": schema_version, "encoding": "zlib-base64", "byte_size": len(table),
            "sha256": hashlib.sha256(table).hexdigest(),
            "data": base64.b64encode(zlib.compress(table, level=9)).decode("ascii")}


def _encode_fallback_shard(units: dict[str, dict[str, Any]], prefix: str,
                            prompt_version: str) -> tuple[dict[str, Any], bytes]:
    records, indexes, refs = [], {}, {}
    retained, references = 0, 0
    for locale, rows in sorted(units.items()):
        refs[locale] = {}
        for key, row in sorted(rows.items()):
            identity = _json_bytes(row)
            if identity not in indexes:
                indexes[identity] = len(records)
                records.append(row)
                retained += len(identity)
            retained += len(key.encode("utf-8")) + 8
            references += 1
            if retained > MAX_EXPANDED_FALLBACK_BYTES or references > MAX_FALLBACK_REFERENCES:
                raise _ShardBudgetExceeded("Source fallback shard exceeds retained-byte or reference budget")
            refs[locale][key] = indexes[identity]
    packed = {"schema_version": 2, "records": records, "units": refs,
              "counts": {locale: len(rows) for locale, rows in units.items()}}
    shard = {"schema_version": 1, "prefix": prefix, "prompt_version": prompt_version,
             "source_fallbacks": _compress_fallback_records(packed, schema_version=4)}
    body = _json_bytes(shard)
    if len(body) > MAX_LOCALE_MANIFEST_BYTES:
        raise _ShardBudgetExceeded("Source fallback shard exceeds wire-byte budget")
    digest = hashlib.sha256(body).hexdigest()
    descriptor = {"prefix": prefix, "path": f"{FALLBACK_SHARD_DIRECTORY}/{prefix}-{digest}.json",
                  "byte_size": len(body), "sha256": digest}
    decoded = _decode_fallback_shard(body, descriptor, prompt_version, set(units))
    if decoded["units"] != units:
        raise LocaleManifestError("Source fallback sharding changed manifest semantics")
    return descriptor, body


def _iter_encoded_fallback_shards(units: dict[str, dict[str, Any]], prompt_version: str,
                                   prefix: str = "") -> Iterator[tuple[dict[str, Any], bytes]]:
    # Start at sixteen leaves, then split only a valid over-budget leaf. Each
    # recursion scans its own partition; it never serializes the whole release.
    for digit in "0123456789abcdef":
        child = prefix + digit
        selected = {locale: {key: row for key, row in rows.items() if key.startswith(child)}
                    for locale, rows in units.items()}
        if not any(selected.values()):
            continue
        split = False
        try:
            encoded = _encode_fallback_shard(selected, child, prompt_version)
        except _ShardBudgetExceeded:
            split = True
        # Leave the exception handler before recursion so its traceback cannot
        # keep the over-budget encoder's intern table alive in every ancestor.
        if split:
            if len(child) == 64:
                raise LocaleManifestError("A single source fallback identity exceeds the shard budgets")
            yield from _iter_encoded_fallback_shards(selected, prompt_version, child)
        else:
            yield encoded


def _encode_locale_manifest_bundle(manifest: dict[str, Any],
                                    sink: Callable[[dict[str, Any], bytes], None] | None = None) -> bytes:
    if type(manifest.get("schema_version")) is not int or manifest["schema_version"] != 1:
        raise LocaleManifestError("Locale manifest schema is invalid")
    fallback = manifest.get("source_fallbacks")
    if not isinstance(fallback, dict) or fallback.get("schema_version") != 1:
        return encode_locale_manifest(manifest)
    units = fallback.get("units")
    if (set(fallback) != {"schema_version", "units", "counts"}
            or not isinstance(units, dict) or not 0 < len(units) <= 64):
        raise LocaleManifestError("Invalid source fallback locales")
    # Validate original provenance before choosing partitions. Invalid source
    # hashes, identity, coverage or counts must never trigger a size fallback.
    validate_translation_resolution(manifest, units)
    if not any(units.values()):
        return encode_locale_manifest(manifest)
    descriptors = []
    for descriptor, body in _iter_encoded_fallback_shards(units, manifest["prompt_version"]):
        descriptors.append(descriptor)
        if len(descriptors) > MAX_FALLBACK_SHARDS:
            raise LocaleManifestError("Source fallback shard index exceeds its leaf budget")
        if sink:
            sink(descriptor, body)
    root = dict(manifest, source_fallbacks={"schema_version": 5,
                "counts": dict(fallback["counts"]), "shards": descriptors})
    locale_manifest_shard_descriptors(root)
    body = _json_bytes(root)
    if len(body) > MAX_LOCALE_MANIFEST_BYTES:
        raise LocaleManifestError("Locale manifest root exceeds its byte size budget")
    validate_translation_resolution(_VerifiedLocaleManifest(root, fallback["counts"]), units)
    return body


def validate_locale_manifest_capacity(manifest: dict[str, Any]) -> None:
    """Validate strict provenance and bounded leaves before expensive rendering."""
    _encode_locale_manifest_bundle(manifest)


def write_locale_manifest_bundle(path: Path, manifest: dict[str, Any]) -> None:
    """Write content-addressed leaves one at a time, then publish their root.

    Legacy readers remain supported; new generated fallbacks use the bounded
    index so ordinary cumulative content growth does not hit a global row cap.
    """
    path = Path(path)
    if path.is_symlink():
        raise LocaleManifestError("Locale manifest must not be a symlink")
    path.parent.mkdir(parents=True, exist_ok=True)

    def save(descriptor: dict[str, Any], body: bytes) -> None:
        destination = _local_shard_path(path, descriptor)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_bytes(body)

    body = _encode_locale_manifest_bundle(manifest, save)
    # The complete candidate is staged separately; replace its root only after
    # all referenced leaves have been written successfully.
    _write_bundle_root(path, body)
    _remove_unused_fallback_shards(path, locale_manifest_shard_descriptors(json.loads(body)))


def _write_bundle_root(path: Path, body: bytes) -> None:
    if path.is_symlink() or path.parent.is_symlink():
        raise LocaleManifestError("Locale manifest root must not be a symlink")
    temporary = path.with_name(path.name + ".tmp")
    if temporary.is_symlink():
        raise LocaleManifestError("Locale manifest temporary path must not be a symlink")
    temporary.write_bytes(body)
    temporary.replace(path)


def _remove_unused_fallback_shards(path: Path, descriptors: list[dict[str, Any]]) -> None:
    """Remove obsolete generated leaves only after the replacement root exists."""
    directory = path.parent / "source-fallbacks"
    if directory.is_symlink():
        raise LocaleManifestError("Source fallback shard directory must not be a symlink")
    if not directory.exists():
        return
    wanted = {Path(descriptor["path"]).name for descriptor in descriptors}
    for candidate in directory.iterdir():
        if (candidate.name not in wanted
                and re.fullmatch(r"[0-9a-f]{1,64}-[0-9a-f]{64}\.json", candidate.name)
                and (candidate.is_file() or candidate.is_symlink())):
            candidate.unlink()


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
        packed["source_fallbacks"] = _compress_fallback_records(packed["source_fallbacks"], schema_version=4)
        body = _json_bytes(packed)
    decoded = parse_locale_manifest(body)
    if decoded != manifest:
        raise LocaleManifestError("Source fallback compaction changed manifest semantics")
    return body
