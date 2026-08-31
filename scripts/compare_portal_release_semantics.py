#!/usr/bin/env python3
"""Build and compare stable semantics for a Portal static release."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET


SCHEMA_VERSION = 1
NORMALIZER_VERSION = 1
VOLATILE_KEYS = frozenset({
    "generated_at",
    "generated_at_bjt",
    "last_seen_at",
    "last_seen_at_bjt",
    "refreshed_at",
    "refreshed_at_bjt",
    "scanned_at",
    "scanned_at_bjt",
    "text_storage_size_bytes",
    "updated_at",
    "updated_at_bjt",
})
COMPONENT_KEYS = frozenset({
    "blog_archive",
    "build_contract",
    "canonical_urls",
    "catalog",
    "chart_search_index",
    "materialized_site_source",
    "password_rules",
    "public_paths",
    "runtime_config",
    "search_index",
})


def stable_value(value: Any) -> Any:
    if isinstance(value, dict):
        return {
            str(key): stable_value(child)
            for key, child in sorted(value.items(), key=lambda row: str(row[0]))
            if str(key) not in VOLATILE_KEYS
        }
    if isinstance(value, list):
        return [stable_value(child) for child in value]
    return value


def digest(value: Any) -> str:
    body = json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(body).hexdigest()


def json_projection(path: Path, *, require_items: bool = False) -> Any:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if require_items:
        if not isinstance(payload, dict):
            raise ValueError(f"Catalog is not an object: {path}")
        items = payload.get("items")
        if not isinstance(items, list) or not items:
            raise ValueError(f"Catalog has no items: {path}")
        ids: set[str] = set()
        projected_items: list[dict[str, Any]] = []
        for raw in items:
            if not isinstance(raw, dict):
                raise ValueError(f"Catalog item is not an object: {path}")
            item_id = str(raw.get("id") or "").strip()
            if not item_id or item_id in ids:
                raise ValueError(f"Catalog has a missing or duplicate id: {path}")
            ids.add(item_id)
            projected = stable_value(raw)
            if not isinstance(projected, dict):
                raise ValueError(f"Catalog projection is invalid: {path}")
            projected_items.append(projected)
        projected_items.sort(key=lambda item: str(item.get("id") or ""))
        root = stable_value({key: value for key, value in payload.items() if key != "items"})
        if not isinstance(root, dict):
            raise ValueError(f"Catalog root projection is invalid: {path}")
        root["items"] = projected_items
        return root
    return stable_value(payload)


def catalog_projection(path: Path) -> dict[str, Any]:
    projected = json_projection(path, require_items=True)
    if not isinstance(projected, dict):
        raise ValueError(f"Catalog projection is invalid: {path}")
    return projected


def sitemap_projection(path: Path, *, include_lastmod: bool = True) -> list[Any]:
    root = ET.parse(path).getroot()
    if root.tag.rsplit("}", 1)[-1] != "urlset":
        raise ValueError(f"Sitemap must be a flat urlset: {path}")
    rows: list[Any] = []
    seen: set[str] = set()
    host = ""
    for node in root.findall("./{*}url"):
        location = str(node.findtext("./{*}loc") or "").strip()
        lastmod = str(node.findtext("./{*}lastmod") or "").strip()
        parsed = urlsplit(location)
        if parsed.scheme != "https" or not parsed.hostname or parsed.query or parsed.fragment:
            raise ValueError(f"Sitemap URL is not canonical HTTPS: {location}")
        if host and parsed.hostname != host:
            raise ValueError(f"Sitemap contains multiple hosts: {path}")
        host = parsed.hostname
        if location in seen:
            raise ValueError(f"Sitemap contains a duplicate URL: {location}")
        seen.add(location)
        rows.append((location, lastmod) if include_lastmod else location)
    if not rows:
        raise ValueError(f"Sitemap has no URLs: {path}")
    return sorted(rows)


def file_tree_projection(
    roots: Iterable[Path],
    *,
    json_only: bool = False,
    excluded_relative_paths: frozenset[str] = frozenset(),
) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    seen: set[str] = set()
    for root in roots:
        if not root.exists():
            raise ValueError(f"Semantic input does not exist: {root}")
        base = root if root.is_dir() else root.parent
        paths = sorted(root.rglob("*") if root.is_dir() else [root])
        for path in paths:
            if path.is_symlink():
                raise ValueError(f"Semantic input must not be a symlink: {path}")
            if not path.is_file():
                continue
            relative = path.relative_to(base).as_posix()
            label = f"{root.name}/{relative}" if root.is_dir() else root.as_posix()
            if relative in excluded_relative_paths or label in excluded_relative_paths:
                continue
            if json_only and path.suffix.lower() != ".json":
                raise ValueError(f"Blog archive contains a non-JSON file: {path}")
            if label in seen:
                raise ValueError(f"Duplicate semantic input label: {label}")
            seen.add(label)
            if json_only:
                value_digest = digest(json_projection(path))
            else:
                value_digest = hashlib.sha256(path.read_bytes()).hexdigest()
            rows.append((label, value_digest))
    if not rows:
        raise ValueError("Semantic file tree is empty")
    return sorted(rows)


def public_path_projection(root: Path, manifest_relative_path: str) -> list[str]:
    if not root.is_dir():
        raise ValueError(f"Public release root is not a directory: {root}")
    paths: list[str] = []
    for path in sorted(root.rglob("*")):
        if path.is_symlink():
            raise ValueError(f"Public release must not contain symlinks: {path}")
        if not path.is_file():
            continue
        relative = path.relative_to(root).as_posix()
        if relative != manifest_relative_path:
            paths.append(relative)
    if not paths:
        raise ValueError(f"Public release has no files: {root}")
    return paths


def build_manifest(
    *,
    catalog: Path,
    sitemap: Path,
    search_index: Path,
    chart_search_index: Path,
    password_rules: Path,
    runtime_config: Path,
    blog_archive_root: Path,
    site_source_root: Path,
    build_contract_paths: list[Path],
    public_root: Path,
    manifest_relative_path: str = "data/release-semantics.json",
) -> dict[str, Any]:
    canonical_urls = sitemap_projection(sitemap, include_lastmod=False)
    public_paths = public_path_projection(public_root, manifest_relative_path)
    components = {
        "catalog": digest(catalog_projection(catalog)),
        "search_index": digest(json_projection(search_index)),
        "chart_search_index": digest(json_projection(chart_search_index)),
        "password_rules": digest(json_projection(password_rules)),
        "runtime_config": digest(json_projection(runtime_config)),
        "blog_archive": digest(file_tree_projection([blog_archive_root], json_only=True)),
        "materialized_site_source": digest(file_tree_projection([site_source_root])),
        "build_contract": digest(file_tree_projection(build_contract_paths)),
        "public_paths": digest(public_paths),
        "canonical_urls": digest(canonical_urls),
    }
    if frozenset(components) != COMPONENT_KEYS:
        raise ValueError("Release semantic component set is incomplete")
    return {
        "schema_version": SCHEMA_VERSION,
        "normalizer_version": NORMALIZER_VERSION,
        "components": components,
        "semantic_sha256": digest(components),
        "metrics": {
            "canonical_url_count": len(canonical_urls),
            "public_file_count": len(public_paths),
        },
    }


def validate_manifest(payload: Any, *, source: str) -> dict[str, Any]:
    if not isinstance(payload, dict):
        raise ValueError(f"Release semantics manifest is not an object: {source}")
    if payload.get("schema_version") != SCHEMA_VERSION:
        raise ValueError(f"Unsupported release semantics schema: {source}")
    if payload.get("normalizer_version") != NORMALIZER_VERSION:
        raise ValueError(f"Unsupported release semantics normalizer: {source}")
    components = payload.get("components")
    if not isinstance(components, dict) or frozenset(components) != COMPONENT_KEYS:
        raise ValueError(f"Release semantics components are incomplete: {source}")
    if any(
        not isinstance(value, str)
        or len(value) != 64
        or any(character not in "0123456789abcdef" for character in value)
        for value in components.values()
    ):
        raise ValueError(f"Release semantics component digest is invalid: {source}")
    expected = digest(components)
    if payload.get("semantic_sha256") != expected:
        raise ValueError(f"Release semantics digest does not match components: {source}")
    return payload


def load_manifest(path: Path) -> dict[str, Any]:
    return validate_manifest(json.loads(path.read_text(encoding="utf-8")), source=str(path))


def compare_manifests(previous: dict[str, Any], current: dict[str, Any]) -> dict[str, Any]:
    previous = validate_manifest(previous, source="previous")
    current = validate_manifest(current, source="current")
    changed_components = sorted(
        key for key in COMPONENT_KEYS
        if previous["components"][key] != current["components"][key]
    )
    return {
        "changed": bool(changed_components),
        "changed_components": changed_components,
        "previous_semantic_sha256": previous["semantic_sha256"],
        "current_semantic_sha256": current["semantic_sha256"],
    }


def compare(
    previous_catalog: Path,
    current_catalog: Path,
    previous_sitemap: Path,
    current_sitemap: Path,
) -> dict[str, Any]:
    """Compatibility helper retained for focused legacy callers and tests."""
    previous_catalog_value = catalog_projection(previous_catalog)
    current_catalog_value = catalog_projection(current_catalog)
    previous_sitemap_value = sitemap_projection(previous_sitemap)
    current_sitemap_value = sitemap_projection(current_sitemap)
    catalog_changed = previous_catalog_value != current_catalog_value
    sitemap_changed = previous_sitemap_value != current_sitemap_value
    return {
        "changed": catalog_changed or sitemap_changed,
        "catalog_changed": catalog_changed,
        "sitemap_changed": sitemap_changed,
        "previous_catalog_sha256": digest(previous_catalog_value),
        "current_catalog_sha256": digest(current_catalog_value),
        "previous_sitemap_sha256": digest(previous_sitemap_value),
        "current_sitemap_sha256": digest(current_sitemap_value),
        "previous_url_count": len(previous_sitemap_value),
        "current_url_count": len(current_sitemap_value),
    }


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--previous-manifest", type=Path)
    parser.add_argument("--current-catalog", type=Path, required=True)
    parser.add_argument("--current-sitemap", type=Path, required=True)
    parser.add_argument("--current-search-index", type=Path, required=True)
    parser.add_argument("--current-chart-search-index", type=Path, required=True)
    parser.add_argument("--current-password-rules", type=Path, required=True)
    parser.add_argument("--current-runtime-config", type=Path, required=True)
    parser.add_argument("--blog-archive-root", type=Path, required=True)
    parser.add_argument("--site-source-root", type=Path, required=True)
    parser.add_argument("--build-contract", type=Path, action="append", required=True)
    parser.add_argument("--public-root", type=Path, required=True)
    parser.add_argument("--write-current-manifest", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()

    current = build_manifest(
        catalog=args.current_catalog,
        sitemap=args.current_sitemap,
        search_index=args.current_search_index,
        chart_search_index=args.current_chart_search_index,
        password_rules=args.current_password_rules,
        runtime_config=args.current_runtime_config,
        blog_archive_root=args.blog_archive_root,
        site_source_root=args.site_source_root,
        build_contract_paths=args.build_contract,
        public_root=args.public_root,
    )
    args.write_current_manifest.parent.mkdir(parents=True, exist_ok=True)
    args.write_current_manifest.write_text(
        json.dumps(current, ensure_ascii=False, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
    )

    if args.previous_manifest and args.previous_manifest.is_file():
        result = compare_manifests(load_manifest(args.previous_manifest), current)
    elif args.force:
        result = {
            "changed": True,
            "changed_components": sorted(COMPONENT_KEYS),
            "previous_semantic_sha256": None,
            "current_semantic_sha256": current["semantic_sha256"],
            "seeded": True,
        }
    else:
        raise ValueError("Active release semantics are missing; seed with a reviewed manual operation")
    if args.force:
        result["changed"] = True
        result["forced"] = True
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as handle:
            handle.write(f"changed={'true' if result['changed'] else 'false'}\n")
            handle.write(f"semantic_sha256={current['semantic_sha256']}\n")
            handle.write("changed_components=" + ",".join(result["changed_components"]) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
