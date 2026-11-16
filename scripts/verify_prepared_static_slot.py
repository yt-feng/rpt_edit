#!/usr/bin/env python3
"""Recheck an already uploaded static candidate immediately before cutover.

This performs no writes. Recovery preparation verifies the entire candidate;
this final guard rechecks its committed identity and key served objects after
the approval wait, while holding the shared production-release concurrency lock.
"""

from __future__ import annotations

import argparse
from concurrent.futures import FIRST_COMPLETED, ThreadPoolExecutor, wait
import hashlib
import json
from pathlib import PurePosixPath
import sys
import time
from typing import Any, Callable, Iterable
import xml.etree.ElementTree as ET

from portal_extended_locales import select_locales, file_for_url
from audit_portal_extended_live import check_page
from portal_extended_ui import UI_VERSION
from r2_transport import R2BodyError, read_r2_bytes, read_r2_into
from portal_locale_manifest import (
    MAX_LOCALE_MANIFEST_BYTES, parse_locale_manifest, validate_translation_resolution,
)
import verify_portal_locale_routes as locale_routes
from publish_static_slot import (
    DEFAULT_RUNTIME_PATHS,
    RUNTIME_SCHEMA_VERSION,
    SHA256_PATTERN,
    build_r2_client,
    incomplete_key,
    manifest_key,
    remote_object_matches_descriptor,
    require_env,
    runtime_manifest_key,
    runtime_object_matches,
    runtime_release_prefix,
    slot_prefix,
    upload_error_code,
    valid_manifest,
    valid_runtime_manifest,
    validate_release,
    validate_slot,
)

MAX_COMMITTED_MANIFEST_BYTES = 64 * 1024 * 1024
VERIFY_WORKERS = 8
PROGRESS_SECONDS = 30


class VerificationProgress:
    """Emit only fixed phase labels and counts; keep stdout machine-readable."""

    def __init__(self) -> None:
        self.started = time.monotonic()

    def report(self, phase: str, completed: int | None = None, total: int | None = None) -> None:
        counts = ""
        if completed is not None:
            counts = f" completed={completed}" + (f"/{total}" if total is not None else "")
        print(f"Prepared verification phase={phase}{counts} elapsed_seconds={time.monotonic() - self.started:.1f}",
              file=sys.stderr, flush=True)


def verify_in_parallel(
    phase: str, items: Iterable[Any], verify: Callable[[Any], Any],
    progress: VerificationProgress,
) -> list[Any]:
    """Bound submitted work, connections and buffered bodies, with heartbeats."""
    items = list(items)
    total = len(items)
    progress.report(phase, 0, total)
    pending_items = iter(items)
    results = []
    last_report = time.monotonic()
    with ThreadPoolExecutor(max_workers=VERIFY_WORKERS) as pool:
        pending = set()
        for item in pending_items:
            pending.add(pool.submit(verify, item))
            if len(pending) == VERIFY_WORKERS:
                break
        while pending:
            done, pending = wait(pending, timeout=PROGRESS_SECONDS, return_when=FIRST_COMPLETED)
            try:
                for future in done:
                    results.append(future.result())
                    item = next(pending_items, None)
                    if item is not None:
                        pending.add(pool.submit(verify, item))
            except Exception:
                for future in pending:
                    future.cancel()
                progress.report(phase + "-failed", len(results), total)
                raise
            now = time.monotonic()
            if not pending or len(results) % 32 == 0 or now - last_report >= PROGRESS_SECONDS:
                progress.report(phase, len(results), total)
                last_report = now
    return results


def read_bounded_body(body: Any, maximum: int) -> bytes:
    """Close every R2 stream, including malformed and oversized responses."""
    try:
        if not hasattr(body, "read"):
            payload = body.encode("utf-8") if isinstance(body, str) else bytes(body)
            if len(payload) > maximum:
                raise RuntimeError("Prepared object exceeds its byte size bound")
            return payload
        chunks = []
        size = 0
        while True:
            chunk = body.read(min(1024 * 1024, maximum - size + 1))
            if not chunk:
                return b"".join(chunks)
            size += len(chunk)
            if size > maximum:
                raise RuntimeError("Prepared object exceeds its byte size bound")
            chunks.append(chunk)
    finally:
        if hasattr(body, "close"):
            body.close()


def read_json_object(client: Any, bucket: str, key: str) -> dict[str, Any] | None:
    try:
        body = read_r2_bytes(client, bucket, key, maximum=MAX_COMMITTED_MANIFEST_BYTES)
    except Exception as error:
        if upload_error_code(error) in {"404", "nosuchkey", "notfound"} or isinstance(error, KeyError):
            return None
        raise
    value = json.loads(body.decode("utf-8"))
    return value if isinstance(value, dict) else None


def read_verified_candidate_body(
    client: Any, bucket: str, key: str, descriptor: dict[str, Any], *, maximum: int,
    metadata: dict[str, Any] | None = None,
) -> bytes:
    if not 0 < int(descriptor["size"]) <= maximum:
        raise RuntimeError(f"Prepared object byte size exceeds its bound: {key}")
    matches = (remote_object_matches_descriptor(client, bucket, key, descriptor) if metadata is None else
               int(metadata.get("ContentLength", -1)) == int(descriptor["size"])
               and str((metadata.get("Metadata") or {}).get("sha256") or "") == descriptor["sha256"])
    if not matches:
        raise RuntimeError(f"Prepared object metadata differs from its manifest: {key}")
    try:
        body = read_r2_bytes(client, bucket, key, maximum=int(descriptor["size"]))
    except R2BodyError as error:
        if error.category == "size_invalid":
            raise RuntimeError("Prepared object exceeds its byte size bound") from error
        raise RuntimeError(f"Prepared object content differs from its manifest: {key}") from error
    if len(body) != descriptor["size"] or hashlib.sha256(body).hexdigest() != descriptor["sha256"]:
        raise RuntimeError(f"Prepared object content differs from its manifest: {key}")
    return body


def verify_candidate_locale_routes(
    client: Any, bucket: str, prefix: str, files: dict[str, dict[str, Any]],
    manifest: dict[str, Any], origin: str,
) -> dict[str, Any]:
    validate_translation_resolution(manifest, locale_routes.LOCALES)
    declared = locale_routes.declared_checks(manifest)
    allowed = {}
    for row in declared or []:
        relative = row["path"]
        descriptor = files.get(relative)
        if descriptor is None or descriptor["size"] != row["byte_size"] or descriptor["sha256"] != row["sha256"]:
            raise RuntimeError(f"Locale route descriptor differs from the committed static manifest: {relative}")
        suffix = "?v=" + row["sha256"][:12] if row.get("lazy_module") else ""
        allowed[origin + "/" + relative + suffix] = (relative, descriptor, row.get("locale"))

    def fetch_candidate(url: str, _timeout: int) -> tuple[int, dict[str, str], bytes]:
        # Resolve only exact declared URLs. Never perform HTTP or interpret an
        # arbitrary URL as an R2 key, including a different origin or query.
        if url not in allowed:
            raise locale_routes.RouteVerificationError("Locale request is outside the declared static candidate")
        relative, descriptor, locale = allowed[url]
        try:
            metadata = client.head_object(Bucket=bucket, Key=prefix + relative)
            body = read_verified_candidate_body(
                client, bucket, prefix + relative, descriptor, maximum=locale_routes.MAX_RESPONSE_BYTES,
                metadata=metadata,
            )
        except Exception as error:
            raise locale_routes.RouteVerificationError(f"Prepared locale object failed verification: {relative}: {error}") from error
        headers = {"content-type": str(metadata.get("ContentType") or "")}
        if locale:
            # The static host derives Content-Language from this fixed route.
            headers["content-language"] = locale
        return 200, headers, body

    report = locale_routes.verify_locale_routes(manifest, origin, fetcher=fetch_candidate)
    if report["status"] not in {"passed", "skipped"}:
        failures = [f"{row['path']}: {row.get('error', 'failed')}" for row in report["checks"] if row["status"] != "passed"]
        raise RuntimeError("Prepared locale routes failed verification: " + "; ".join(failures))
    return report


REQUIRED_STATIC_PATHS = (
    "index.html",
    "developer-api.html",
    "content-api.openapi.json",
    "downloads/content-agent.zip",
    "downloads/content-agent.zip.sha256",
    "robots.txt",
    "feed.xml",
    "data/catalog.json",
    "data/catalog_preview.json",
    "data/release-semantics.json",
    "assets/styles.css",
    "assets/app.js",
    "sitemap.xml",
    "sitemap-pages.xml",
    "sitemap-baidu.xml",
    "sitemap-sogou.xml",
)
REQUIRED_LOCALE_PATHS = (
    "data/i18n/manifest.json",
    "assets/locale.css",
    "assets/locale-runtime.js",
    *(f"sitemap-{locale}.xml" for locale in ("ko", "ja", "ar")),
    *(f"{locale}/index.html" for locale in ("ko", "ja", "ar")),
)
REQUIRED_EXTENDED_BASE_PATHS = (
    "data/extended-locales/assembly.json",
    "sitemap-extended.xml",
)


def static_tree_sha256(files: dict[str, dict[str, Any]]) -> str:
    """Match build_inventory's Path ordering, including directory/file siblings."""
    digest = hashlib.sha256()
    for relative in sorted(files, key=PurePosixPath):
        digest.update(relative.encode("utf-8"))
        digest.update(b"\0")
        digest.update(json.dumps(files[relative], sort_keys=True, separators=(",", ":")).encode("utf-8"))
        digest.update(b"\n")
    return digest.hexdigest()


def verify_extended_static_tree(
    client: Any, bucket: str, prefix: str, files: dict[str, dict[str, Any]],
    *, origin: str | None, verified_paths: set[str] | None = None,
    progress: VerificationProgress | None = None,
    on_verified_body: Callable[[str, bytes], None] | None = None,
) -> dict[str, Any] | None:
    progress = progress or VerificationProgress()
    verified_paths = verified_paths or set()
    assembly_descriptor = files.get("data/extended-locales/assembly.json")
    if assembly_descriptor is None:
        return None
    def read_body(relative: str, maximum: int) -> bytes:
        body = read_verified_candidate_body(client, bucket, prefix + relative, files[relative], maximum=maximum)
        if on_verified_body is not None:
            on_verified_body(relative, body)
        return body
    progress.report("extended-manifest")
    assembly = json.loads(read_body("data/extended-locales/assembly.json", 1024 * 1024).decode("utf-8"))
    locales = assembly.get("locales")
    if (
        assembly.get("status") != "assembled"
        or not isinstance(locales, list)
        or not locales
        or assembly.get("paid_provider_requests") != 0
        or assembly.get("deployment_performed") is not False
        or assembly.get("locale_homepages") is not True
        or assembly.get("pages_per_locale", 0) <= 0
    ):
        raise RuntimeError("Prepared extended assembly receipt is incomplete")
    approved = select_locales(",".join(locales))
    standard_ui = assembly.get('ui_version') == UI_VERSION
    if assembly.get('ui_version') and not standard_ui:
        raise RuntimeError('Unknown extended UI version')
    if standard_ui:
        assets = []
        for name in ('styles.css', 'blog.css', 'locale.css', 'extended-locales.css', 'extended-locales.js', 'app.js', 'contact.js'):
            path = 'assets/' + name
            if path not in files:
                raise RuntimeError(f'Prepared extended UI asset is missing: {path}')
            if not 0 < files[path]['size'] <= 4 * 1024 * 1024:
                raise RuntimeError(f'Prepared extended UI asset exceeds its byte size bound: {path}')
            if path not in verified_paths:
                assets.append(path)
        def verify_asset(path: str) -> None:
            read_body(path, 4 * 1024 * 1024)
        verify_in_parallel("extended-assets", assets, verify_asset, progress)
    index_descriptor = files.get("sitemap-extended.xml")
    if index_descriptor is None:
        raise RuntimeError("Prepared extended sitemap index is missing")
    index_body = read_body("sitemap-extended.xml", 2 * 1024 * 1024)
    index_locations = [str(node.text or "").strip() for node in ET.fromstring(index_body).findall(".//{*}loc")]
    expected_index = {f"{origin.rstrip('/')}/sitemap-extended-{locale}.xml" for locale in approved} if origin else set()
    if origin and set(index_locations) != expected_index:
        raise RuntimeError("Prepared extended sitemap index does not match its assembly receipt")
    def verify_locale(locale: str) -> list[tuple[str, str, str]]:
        sitemap_body = None
        required = [f"{locale}/llms.txt", f"sitemap-extended-{locale}.xml", f"{locale}/index.html"]
        for relative in required:
            descriptor = files.get(relative)
            if descriptor is None:
                raise RuntimeError(f"Prepared extended object is missing: {relative}")
            body = read_body(relative, 4 * 1024 * 1024 if relative.endswith(".html") else 2 * 1024 * 1024)
            if relative.endswith(".html") and b"noindex" in body.lower():
                raise RuntimeError(f"Prepared extended homepage remains noindex: {relative}")
            if relative == f"{locale}/index.html" and origin:
                check_page(body, f"{origin.rstrip('/')}/{locale}/", locale, require_standard_ui=standard_ui)
            if relative == f"sitemap-extended-{locale}.xml":
                sitemap_body = body
        locations = [str(node.text or "").strip() for node in ET.fromstring(sitemap_body).findall(".//{*}loc")]
        expected_prefix = f"{origin.rstrip('/')}/{locale}/" if origin else ""
        count = assembly.get("page_counts", {}).get(locale, assembly["pages_per_locale"])
        if len(locations) != count or len(set(locations)) != count or (origin and any(not value.startswith(expected_prefix) for value in locations)):
            raise RuntimeError(f"Prepared extended sitemap is incomplete: {locale}")
        if origin:
            def localized_path(url):
                # Validate the source route after stripping the already checked
                # locale prefix; file_for_url intentionally rejects locale URLs.
                source = origin.rstrip('/') + '/' + url[len(expected_prefix):]
                return locale + '/' + file_for_url(source, origin=origin.rstrip('/')).as_posix()
            expected_paths = {localized_path(url) for url in locations}
            actual_paths = {path for path in files if path.startswith(locale+'/') and path.endswith('.html')
                            and path != f"{locale}/index.html"}
            if expected_paths != actual_paths:
                raise RuntimeError(f"Prepared extended page set differs from its sitemap: {locale}")
            return [(localized_path(url), url, locale) for url in locations]
        return []

    locale_pages = verify_in_parallel("extended-locale-inventories", approved, verify_locale, progress)

    def verify_page(row: tuple[str, str, str]) -> None:
        path, url, locale = row
        body = read_body(path, 4 * 1024 * 1024)
        check_page(body, url, locale, require_standard_ui=standard_ui)

    # Every page is verified. One bounded queue avoids a slow locale holding up
    # all following locales; at most eight 4 MiB page bodies are in flight.
    verify_in_parallel("extended-pages", (row for rows in locale_pages for row in rows), verify_page, progress)
    return {"locales": list(approved), "pages_per_locale": assembly["pages_per_locale"]}


def require_complete_slot(client: Any, bucket: str, slot: str) -> None:
    # An existing malformed/empty marker also means incomplete; parsing it as a
    # JSON object would incorrectly treat [] or null as an absent marker.
    try:
        client.head_object(Bucket=bucket, Key=incomplete_key(slot))
    except Exception as error:
        if upload_error_code(error) in {"404", "nosuchkey", "notfound"}:
            return
        raise
    raise RuntimeError("Prepared static slot has an incomplete publication marker")


def read_prepared_manifest(
    client: Any, bucket: str, slot: str, release: str, tree: str,
) -> dict[str, Any]:
    try:
        manifest = valid_manifest(read_json_object(client, bucket, manifest_key(slot)), slot)
    except (TypeError, ValueError) as error:
        raise RuntimeError("Prepared static manifest is invalid") from error
    if manifest is None or manifest["release_id"] != release or manifest["tree_sha256"] != tree:
        raise RuntimeError("Prepared static manifest does not match the requested candidate")
    files = manifest["files"]
    if not files or static_tree_sha256(files) != tree:
        raise RuntimeError("Prepared static manifest file tree does not match its committed digest")
    if manifest.get("total_bytes") != sum(int(row["size"]) for row in files.values()):
        raise RuntimeError("Prepared static manifest total bytes do not match its file inventory")
    return manifest


def verify_object_body(
    client: Any, bucket: str, key: str, descriptor: dict[str, Any],
    *, runtime_release: str | None = None,
) -> None:
    if runtime_release is not None:
        if not runtime_object_matches(client.head_object(Bucket=bucket, Key=key), descriptor, runtime_release):
            raise RuntimeError(f"Prepared immutable runtime metadata differs: {PurePosixPath(key).name}")
    elif not remote_object_matches_descriptor(client, bucket, key, descriptor):
        raise RuntimeError(f"Prepared object metadata differs from its manifest: {key}")
    digest = hashlib.sha256()
    def reset_digest() -> None:
        nonlocal digest
        digest = hashlib.sha256()
    try:
        size = read_r2_into(client, bucket, key, maximum=max(1, int(descriptor["size"])),
                            reset=reset_digest, write=lambda chunk: digest.update(chunk))
    except R2BodyError as error:
        if error.category == "size_invalid":
            raise RuntimeError(f"Prepared object is larger than its manifest: {key}") from error
        raise RuntimeError(f"Prepared object content differs from its manifest: {key}") from error
    if size != int(descriptor["size"]) or digest.hexdigest() != descriptor["sha256"]:
        raise RuntimeError(f"Prepared object content differs from its manifest: {key}")


def verify_prepared_static_slot(
    client: Any, bucket: str, *, slot: str, release: str, tree: str,
    locale_origin: str | None = None,
) -> dict[str, Any]:
    slot = validate_slot(slot)
    release = validate_release(release)
    if not SHA256_PATTERN.fullmatch(tree):
        raise ValueError("Static tree must contain exactly 64 lowercase hex characters")
    if locale_origin is not None:
        locale_origin = locale_routes.validate_origin(locale_origin)
    progress = VerificationProgress()
    progress.report("candidate-identity")
    require_complete_slot(client, bucket, slot)
    manifest = read_prepared_manifest(client, bucket, slot, release, tree)
    files = manifest["files"]
    prefix = slot_prefix(slot)
    has_extended = "data/extended-locales/assembly.json" in files
    required_paths = REQUIRED_STATIC_PATHS + (
        REQUIRED_LOCALE_PATHS if "data/i18n/manifest.json" in files else ()
    ) + (REQUIRED_EXTENDED_BASE_PATHS if has_extended else ())
    locale_manifest = None
    locale_shards_verified = 0
    def resolve_locale_shard(row: dict[str, Any]) -> bytes:
        nonlocal locale_shards_verified
        relative = row["path"]
        descriptor = files.get(relative)
        if (descriptor is None or descriptor["size"] != row["byte_size"]
                or descriptor["sha256"] != row["sha256"]):
            raise RuntimeError(f"Locale source shard differs from the committed static manifest: {relative}")
        body = read_verified_candidate_body(
            client, bucket, prefix + relative, descriptor, maximum=MAX_LOCALE_MANIFEST_BYTES,
        )
        locale_shards_verified += 1
        progress.report("locale-source-shards", locale_shards_verified, None)
        return body
    if locale_origin is not None and "data/i18n/manifest.json" not in files:
        raise RuntimeError("Prepared locale manifest is required when locale origin is provided")
    for relative in required_paths:
        if relative not in files or int(files[relative]["size"]) <= 0:
            raise RuntimeError(f"Prepared static manifest lacks a required object: {relative}")
    locale_manifest_path = "data/i18n/manifest.json"
    if locale_origin is not None:
        progress.report("locale-manifest")
        locale_manifest = parse_locale_manifest(read_verified_candidate_body(
            client, bucket, prefix + locale_manifest_path, files[locale_manifest_path], maximum=MAX_LOCALE_MANIFEST_BYTES,
        ), shard_resolver=resolve_locale_shard)
    # Assembly and extended sitemap bytes are checked while parsing below;
    # reading them here as well only duplicates the same committed-body check.
    body_paths = [relative for relative in required_paths
                  if relative not in REQUIRED_EXTENDED_BASE_PATHS
                  and not (locale_origin is not None and relative == locale_manifest_path)]
    verify_in_parallel("required-static", body_paths, lambda relative: verify_object_body(
        client, bucket, prefix + relative, files[relative]), progress)

    locale_report = None
    if locale_origin is not None:
        progress.report("locale-routes")
        locale_report = verify_candidate_locale_routes(client, bucket, prefix, files, locale_manifest, locale_origin)
        progress.report("locale-routes", locale_report["request_count"], locale_report["request_count"])
    extended_report = verify_extended_static_tree(
        client, bucket, prefix, files, origin=locale_origin, verified_paths=set(body_paths), progress=progress,
    )

    progress.report("runtime-identity")
    runtime = valid_runtime_manifest(
        read_json_object(client, bucket, runtime_manifest_key(release)), release,
    )
    if runtime is None:
        raise RuntimeError("Prepared immutable runtime manifest is invalid")
    binding = {
        "schema_version": RUNTIME_SCHEMA_VERSION,
        "release_id": release,
        "prefix": runtime_release_prefix(release),
        "tree_sha256": runtime["tree_sha256"],
    }
    if manifest.get("runtime_data") != binding:
        raise RuntimeError("Prepared static and immutable runtime manifest identities differ")
    expected_runtime = {PurePosixPath(relative).name for relative in DEFAULT_RUNTIME_PATHS}
    if set(runtime["files"]) != expected_runtime:
        raise RuntimeError("Prepared immutable runtime manifest has an unexpected file inventory")
    for relative in DEFAULT_RUNTIME_PATHS:
        filename = PurePosixPath(relative).name
        descriptor = runtime["files"][filename]
        static_descriptor = files.get(relative) or {}
        if any(descriptor[field] != static_descriptor.get(field) for field in ("sha256", "size")):
            raise RuntimeError(f"Prepared runtime content does not match the static candidate: {filename}")
    verify_in_parallel("runtime-objects", runtime["files"].items(), lambda row: verify_object_body(
        client, bucket, runtime["prefix"] + row[0], row[1], runtime_release=release), progress)

    # A publisher may have started or committed while the object checks ran.
    progress.report("final-identity")
    require_complete_slot(client, bucket, slot)
    if read_prepared_manifest(client, bucket, slot, release, tree) != manifest:
        raise RuntimeError("Prepared static manifest changed during verification")
    if read_json_object(client, bucket, runtime_manifest_key(release)) != runtime:
        raise RuntimeError("Prepared immutable runtime manifest changed during verification")
    require_complete_slot(client, bucket, slot)
    result = {
        "verified": True,
        "slot": slot,
        "release_id": release,
        "tree_sha256": tree,
        "static_objects_verified": len(required_paths),
        "runtime_objects_verified": len(expected_runtime),
        "locale_source_shards_verified": locale_shards_verified,
    }
    if locale_report is not None:
        result["locale_routes_status"] = locale_report["status"]
        result["locale_objects_verified"] = locale_report["request_count"]
    if extended_report is not None:
        result["extended_locales"] = extended_report["locales"]
        result["extended_pages_per_locale"] = extended_report["pages_per_locale"]
    progress.report("complete")
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--slot", required=True)
    parser.add_argument("--release", required=True)
    parser.add_argument("--tree", required=True)
    parser.add_argument("--locale-origin", help="Verify declared locale routes against this public origin using only R2")
    args = parser.parse_args()
    try:
        client, _transfer = build_r2_client()
        result = verify_prepared_static_slot(
            client, require_env("R2_BUCKET"), slot=args.slot, release=args.release, tree=args.tree,
            locale_origin=args.locale_origin,
        )
        print(json.dumps(result, sort_keys=True))
        return 0
    except Exception as error:
        print(f"Prepared static slot verification failed: {error}", file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
