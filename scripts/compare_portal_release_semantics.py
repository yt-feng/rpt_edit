#!/usr/bin/env python3
"""Compare public catalog and sitemap semantics before an Edge cutover."""

from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit
import xml.etree.ElementTree as ET


VOLATILE_KEYS = frozenset({
    "generated_at",
    "generated_at_bjt",
    "last_seen_at",
    "last_seen_at_bjt",
    "refreshed_at",
    "refreshed_at_bjt",
    "scanned_at",
    "scanned_at_bjt",
    "updated_at",
    "updated_at_bjt",
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


def catalog_projection(path: Path) -> dict[str, Any]:
    payload = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(payload, dict):
        raise ValueError(f"Catalog is not an object: {path}")
    items = payload.get("items")
    if not isinstance(items, list) or not items:
        raise ValueError(f"Catalog has no items: {path}")
    projected_items: list[dict[str, Any]] = []
    ids: set[str] = set()
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


def sitemap_projection(path: Path) -> list[tuple[str, str]]:
    root = ET.parse(path).getroot()
    if root.tag.rsplit("}", 1)[-1] != "urlset":
        raise ValueError(f"Sitemap must be a flat urlset: {path}")
    rows: list[tuple[str, str]] = []
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
        rows.append((location, lastmod))
    if not rows:
        raise ValueError(f"Sitemap has no URLs: {path}")
    return sorted(rows)


def digest(value: Any) -> str:
    body = json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return hashlib.sha256(body).hexdigest()


def compare(
    previous_catalog: Path,
    current_catalog: Path,
    previous_sitemap: Path,
    current_sitemap: Path,
) -> dict[str, Any]:
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
    parser.add_argument("--previous-catalog", type=Path, required=True)
    parser.add_argument("--current-catalog", type=Path, required=True)
    parser.add_argument("--previous-sitemap", type=Path, required=True)
    parser.add_argument("--current-sitemap", type=Path, required=True)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--github-output", type=Path)
    args = parser.parse_args()
    result = compare(
        args.previous_catalog,
        args.current_catalog,
        args.previous_sitemap,
        args.current_sitemap,
    )
    if args.force:
        result["changed"] = True
        result["forced"] = True
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    if args.github_output:
        with args.github_output.open("a", encoding="utf-8") as handle:
            handle.write(f"changed={'true' if result['changed'] else 'false'}\n")
            handle.write(f"catalog_changed={'true' if result['catalog_changed'] else 'false'}\n")
            handle.write(f"sitemap_changed={'true' if result['sitemap_changed'] else 'false'}\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
