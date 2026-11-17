#!/usr/bin/env python3
"""Carry verified published translations into a fresh Chinese catalog release.

The receipt binds the old locale bytes to the captured active static manifest.
Only the Chinese lazy-JavaScript descriptor is rebound to the newly built asset;
translation coverage and source-generation metadata remain those of the old build.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
from pathlib import Path
import re
import tempfile
from typing import Any
from urllib.parse import urlsplit

import publish_static_slot as publisher
from portal_locale_manifest import MAX_LOCALE_MANIFEST_BYTES, load_locale_manifest
from resume_portal_locale_candidate import bounded_results, download_candidate_object, local_target
from verify_prepared_static_slot import (
    MAX_COMMITTED_MANIFEST_BYTES, read_json_object, require_complete_slot, static_tree_sha256,
)

LOCALES = ("ko", "ja", "ar")
MANIFEST = "data/i18n/manifest.json"
SHARED_ASSETS = frozenset((
    "assets/locale.css", "assets/locale-runtime.js", "assets/locale-recovery.js", "assets/locale-detail.js",
))
MAX_RECEIPT_BYTES = 64 * 1024 * 1024


class RetentionError(RuntimeError):
    pass


def require(condition: bool, message: str) -> None:
    if not condition:
        raise RetentionError(message)


def selected_paths(files: dict[str, Any]) -> set[str]:
    return {path for path in files if path.startswith(tuple(code + "/" for code in LOCALES))
            or path.startswith("data/i18n/") or path in SHARED_ASSETS
            or path in {f"sitemap-{code}.xml" for code in LOCALES}}


def checked_manifest(value: dict[str, Any], state: dict[str, Any]) -> dict[str, Any]:
    require(isinstance(state, dict) and state.get("schema_version") == 1
            and state.get("slot") in {"a", "b"}, "Active release identity is invalid")
    manifest = publisher.valid_manifest(value, state["slot"])
    require(manifest is not None and all(manifest.get(key) == state.get(key)
            for key in ("slot", "release_id", "tree_sha256")), "Retained manifest differs from active release")
    require(static_tree_sha256(manifest["files"]) == state["tree_sha256"], "Retained manifest tree is invalid")
    return manifest


def descriptor(path: Path) -> dict[str, Any]:
    require(path.is_file() and not path.is_symlink(), "Retained file must be a regular file")
    digest = hashlib.sha256()
    count = 0
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            count += len(chunk)
            digest.update(chunk)
    return {"size": count, "sha256": digest.hexdigest()}


def current_locale_manifest(source: dict[str, Any], root: Path) -> dict[str, Any]:
    # Work on plain JSON, retaining sharded provenance without expanding it.
    result = json.loads(json.dumps(source))
    lazy = result.get("lazy_javascript_assets")
    if isinstance(lazy, dict) and "zh-Hans" in lazy:
        old = lazy["zh-Hans"]
        require(isinstance(old, dict) and old.get("path") == "assets/newsfeed-app.js",
                "Retained Chinese lazy asset descriptor is invalid")
        row = descriptor(local_target(root, old["path"]))
        lazy["zh-Hans"] = {"path": old["path"], "byte_size": row["size"], "sha256": row["sha256"]}
    return result


def html_discovery_digest(raw: bytes) -> str:
    from assemble_portal_extended_locales import head_alternates
    try:
        return hashlib.sha256(head_alternates(raw.decode("utf-8"), {}).encode("utf-8")).hexdigest()
    except ValueError as error:
        raise RetentionError("Retained published file changed or has invalid HTML") from error


def retained_html_proofs(receipt: dict[str, Any], manifest: dict[str, Any]) -> dict[str, Any]:
    proof = receipt.get("html_discovery_proofs")
    if proof is None:
        return {}  # Older receipts retain their exact-byte-only contract.
    require(isinstance(proof, dict) and proof.get("schema_version") == 1,
            "Retained HTML discovery proof is invalid")
    origin = proof.get("site_origin")
    require(isinstance(origin, str), "Retained HTML discovery origin is invalid")
    parsed = urlsplit(origin)
    require(parsed.scheme == "https" and parsed.netloc and not parsed.username and not parsed.password
            and not parsed.path and not parsed.query and not parsed.fragment,
            "Retained HTML discovery origin is invalid")
    rows = proof.get("files")
    expected = {path for path in selected_paths(manifest["files"])
                if path.split("/", 1)[0] in LOCALES and path.endswith(".html")}
    require(isinstance(rows, dict) and set(rows) == expected,
            "Retained HTML discovery inventory differs from active release")
    for path, row in rows.items():
        require(isinstance(row, dict) and set(row) == {"source_sha256", "normalized_sha256"}
                and row["source_sha256"] == manifest["files"][path]["sha256"]
                and isinstance(row["normalized_sha256"], str)
                and re.fullmatch(r"[0-9a-f]{64}", row["normalized_sha256"]) is not None,
                "Retained HTML discovery proof differs from active release")
    return rows


def validate_html_discovery(root: Path, relative: str, raw: bytes, proof: dict[str, Any], origin: str,
                            context: dict[str, Any]) -> None:
    """Permit only the exact extended publisher's verified hreflang cluster."""
    from assemble_portal_extended_locales import head_alternates
    from portal_extended_locales import ADDITIONAL, HREFLANG, PublicParser, locale_url
    require(html_discovery_digest(raw) == proof["normalized_sha256"],
            f"Retained published file changed outside language links: {relative}")
    if "ledger" not in context:
        ledger_path = local_target(root, "data/extended-locales/assembly.json")
        require(ledger_path.is_file() and not ledger_path.is_symlink() and ledger_path.stat().st_size <= 1024 * 1024,
                "Changed retained language links require an assembled extended ledger")
        ledger = json.loads(ledger_path.read_bytes())
        locales, sources = ledger.get("locales"), ledger.get("source_urls_by_locale")
        require(ledger.get("schema_version") == 2 and ledger.get("status") == "assembled"
                and isinstance(locales, list) and locales and len(set(locales)) == len(locales)
                and all(code in ADDITIONAL for code in locales)
                and isinstance(sources, dict) and set(sources) == set(locales)
                and all(isinstance(urls, list) and all(isinstance(url, str) for url in urls)
                        for urls in sources.values()), "Extended language-link ledger is invalid")
        context["ledger"] = (locales, {code: set(urls) for code, urls in sources.items()})
    locales, sources = context["ledger"]
    source_path = relative.split("/", 1)[1]
    source_url = origin + "/" + (source_path[:-10] if source_path.endswith("index.html") else source_path)
    require(any(source_url in urls for urls in sources.values()),
            "Retained language-link change is outside the assembled source set")
    cluster = {"zh-Hans": source_url, "x-default": source_url}
    def published(code: str, expected: str) -> bool:
        page = local_target(root, code + "/" + source_path)
        if not page.is_file() or page.is_symlink():
            return False
        parser = PublicParser(); parser.feed(page.read_text(encoding="utf-8")); parser.close()
        return (parser.canonical == expected and parser.content_lang == code
                and "noindex" not in parser.metadata.get("robots", "").lower())
    for code in LOCALES:
        expected = origin + "/" + code + source_url[len(origin):]
        if published(code, expected):
            cluster[code] = expected
    for code in locales:
        if source_url in sources[code] and code in HREFLANG:
            expected = locale_url(source_url, code, origin=origin)
            require(published(code, expected), "Extended language-link counterpart is not published")
            cluster[HREFLANG[code]] = expected
    text = raw.decode("utf-8")
    require(text == head_alternates(text, cluster),
            f"Retained language links differ from the assembled cluster: {relative}")


def validate_retention(root: Path, receipt_path: Path, active_manifest_path: Path) -> dict[str, Any]:
    """Recheck retained bytes before using older coverage instead of fresh coverage."""
    require(receipt_path.is_file() and not receipt_path.is_symlink()
            and 0 < receipt_path.stat().st_size <= MAX_RECEIPT_BYTES, "Retention receipt is missing or oversized")
    receipt = json.loads(receipt_path.read_bytes())
    require(receipt.get("schema_version") == 1 and receipt.get("kind") == "published-core-locales",
            "Retention receipt is invalid")
    require(active_manifest_path.is_file() and not active_manifest_path.is_symlink()
            and 0 < active_manifest_path.stat().st_size <= MAX_COMMITTED_MANIFEST_BYTES,
            "Retention active manifest is missing or oversized")
    manifest = checked_manifest(json.loads(active_manifest_path.read_bytes()), receipt.get("source_state"))
    html_proofs = retained_html_proofs(receipt, manifest)
    paths = selected_paths(manifest["files"])
    require(receipt.get("retained_files") == len(paths), "Retained file count changed")
    try:
        raw = base64.b64decode(receipt["source_manifest_b64"], validate=True)
    except (ValueError, KeyError, TypeError) as error:
        raise RetentionError("Retained source manifest proof is invalid") from error
    require(0 < len(raw) <= MAX_LOCALE_MANIFEST_BYTES, "Retained source manifest is oversized")
    old = manifest["files"].get(MANIFEST, {})
    require(len(raw) == old.get("size") and hashlib.sha256(raw).hexdigest() == old.get("sha256"),
            "Retained source manifest proof differs from active release")
    expected = current_locale_manifest(json.loads(raw), root)
    require((root / MANIFEST).is_file() and not (root / MANIFEST).is_symlink()
            and 0 < (root / MANIFEST).stat().st_size <= MAX_LOCALE_MANIFEST_BYTES,
            "Retained locale manifest is missing or oversized")
    require(json.loads((root / MANIFEST).read_bytes()) == expected,
            "Retained translation metadata changed beyond the Chinese asset binding")
    actual_paths = selected_paths({path.relative_to(root).as_posix(): None for path in root.rglob("*")
                                   if path.is_file() or path.is_symlink()})
    require(paths == actual_paths, "Retained locale inventory changed")
    discovery_context: dict[str, Any] = {}
    for relative in sorted(paths - {MANIFEST}):
        row = descriptor(local_target(root, relative))
        if all(row[key] == manifest["files"][relative][key] for key in row):
            continue
        require(relative in html_proofs, f"Retained published file changed: {relative}")
        validate_html_discovery(root, relative, local_target(root, relative).read_bytes(), html_proofs[relative],
                                receipt["html_discovery_proofs"]["site_origin"], discovery_context)
    loaded = load_locale_manifest(root / MANIFEST)
    from audit_portal_shadow_preview import manifest_files
    from verify_portal_locale_routes import declared_checks
    manifest_files(loaded)
    declared_checks(loaded)
    return {"retained_files": len(paths), "translation_scope": loaded["translation_scope"],
            "index_policy": loaded["index_policy"],
            "detail_prefixes": {code: sorted(loaded["catalog_detail_overlays"][code]) for code in LOCALES}}


def restore_discovery(root: Path, site_url: str, paths: set[str]) -> int:
    from build_portal_locales import (extract_canonical, commit_chinese_discovery, inject_root_discovery,
                                     is_indexable_html)
    # Only advertise a counterpart that really exists and is already indexable
    # in every retained core language; new Chinese pages wait for their translation.
    counterparts = {path[len("ko/"):] for path in paths if path.startswith("ko/") and path.endswith(".html")}
    asset_version = hashlib.sha256((root / "assets/locale-runtime.js").read_bytes()).hexdigest()[:12]
    from portal_locale_text_store import StagedTextMapping
    from datetime import datetime, timezone
    with tempfile.TemporaryDirectory(prefix="retained-discovery-") as temporary:
        updates = StagedTextMapping(Path(temporary) / "updates")
        for relative in sorted(counterparts):
            page = root / relative
            if not page.is_file() or page.is_symlink():
                continue
            if not all(f"{code}/{relative}" in paths and is_indexable_html((root / code / relative).read_text())
                       for code in LOCALES):
                continue
            source = page.read_text(encoding="utf-8")
            canonical = extract_canonical(source)
            if canonical:
                updates[page] = inject_root_discovery(source, canonical, site_url, asset_version)
        # The index changed today; retained language sitemaps keep their own dates.
        commit_chinese_discovery(root, updates, site_url, datetime.now(timezone.utc).date().isoformat())
        return len(updates)


def retain(*, client: Any, bucket: str, active_state: dict[str, Any], active_manifest: dict[str, Any],
           root: Path, site_url: str, workers: int = 16) -> dict[str, Any]:
    manifest = checked_manifest(active_manifest, active_state)
    files = manifest["files"]
    paths = selected_paths(files)
    require({MANIFEST, *SHARED_ASSETS, *(f"sitemap-{code}.xml" for code in LOCALES)} <= paths,
            "Active release has no complete published core locales")
    require_complete_slot(client, bucket, manifest["slot"])
    prefix = publisher.slot_prefix(manifest["slot"])
    root = root.resolve()
    require(root.is_dir(), "Fresh Chinese site is missing")
    require(not (selected_paths({p.relative_to(root).as_posix(): None for p in root.rglob("*")
                                 if p.is_file() or p.is_symlink()}) - SHARED_ASSETS),
            "Core retention requires a fresh Chinese tree without staged translations")
    with tempfile.TemporaryDirectory(prefix="retained-locales-", dir=root.parent) as temporary:
        staging = Path(temporary)
        def fetch(relative: str) -> str:
            download_candidate_object(client, bucket, prefix + relative, files[relative], staging, relative)
            return relative
        progress = publisher._PublishProgress("retain_core_locales", objects=len(paths), workers=workers)
        for count, _relative in enumerate(bounded_results(sorted(paths), fetch, workers=workers), 1):
            progress.update(count)
        progress.finish(retained=len(paths))
        source_body = (staging / MANIFEST).read_bytes()
        require(len(source_body) <= MAX_LOCALE_MANIFEST_BYTES, "Retained locale manifest is oversized")
        loaded = load_locale_manifest(staging / MANIFEST)
        from audit_portal_shadow_preview import manifest_files
        manifest_files(loaded)
        for code in LOCALES:
            require(sum(path.startswith(code + "/") and path.endswith(".html") for path in paths)
                    == loaded.get("html_page_count"), f"Retained HTML inventory is incomplete: {code}")
        html_proofs = {relative: {"source_sha256": files[relative]["sha256"],
                                  "normalized_sha256": html_discovery_digest((staging / relative).read_bytes())}
                       for relative in paths if relative.split("/", 1)[0] in LOCALES and relative.endswith(".html")}
        require_complete_slot(client, bucket, manifest["slot"])
        latest = read_json_object(client, bucket, f"edge-static/slot-manifests/{manifest['slot']}.json")
        require(checked_manifest(latest, active_state) == manifest, "Active static manifest changed during retention")
        for relative in sorted(paths):
            target = local_target(root, relative)
            (staging / relative).replace(target)
    value = current_locale_manifest(json.loads(source_body), root)
    (root / MANIFEST).write_text(json.dumps(value, sort_keys=True, separators=(",", ":")) + "\n")
    discovery_count = restore_discovery(root, site_url, paths)
    return {"schema_version": 1, "kind": "published-core-locales", "source_state": active_state,
            "retained_files": len(paths), "translated_pages_per_locale": loaded["html_page_count"],
            "chinese_discovery_pages": discovery_count, "provider_requests": 0,
            "html_discovery_proofs": {"schema_version": 1, "site_origin": site_url.rstrip("/"), "files": html_proofs},
            "source_manifest_b64": base64.b64encode(source_body).decode("ascii")}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--active-state", type=Path, required=True)
    parser.add_argument("--active-manifest", type=Path, required=True)
    parser.add_argument("--site-url", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    require(not args.output.resolve().is_relative_to(args.root.resolve()),
            "Retention receipt must remain outside the public tree")
    from chart_search_r2 import client_and_bucket
    client, bucket = client_and_bucket()
    receipt = retain(client=client, bucket=bucket, active_state=json.loads(args.active_state.read_bytes()),
                     active_manifest=json.loads(args.active_manifest.read_bytes()), root=args.root,
                     site_url=args.site_url)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(receipt, sort_keys=True, separators=(",", ":")) + "\n")
    args.output.chmod(0o600)
    result = validate_retention(args.root, args.output, args.active_manifest)
    print(json.dumps({"retained_files": result["retained_files"], "provider_requests": 0}))
    print("retained_core_locales=true")
    print("retention_receipt_sha256=" + hashlib.sha256(args.output.read_bytes()).hexdigest())
    print("retention_active_manifest_sha256=" + hashlib.sha256(args.active_manifest.read_bytes()).hexdigest())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
