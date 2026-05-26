#!/usr/bin/env python3
"""Build the static KC Desk Notes Pages artifact."""

from __future__ import annotations

import argparse
import json
import shutil
from pathlib import Path
from typing import Any


PUBLIC_ITEM_KEYS = [
    "id",
    "title",
    "filename",
    "date_folder",
    "date_folders",
    "bank_code",
    "bank_name",
    "password_group",
    "size_bytes",
    "client_modified",
    "server_modified",
    "first_seen_at_bjt",
    "last_seen_at_bjt",
    "available",
    "present_in_latest_scan",
]


def load_json(path: Path) -> dict[str, Any]:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, data: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def public_catalog(catalog: dict[str, Any]) -> dict[str, Any]:
    items: list[dict[str, Any]] = []
    for item in catalog.get("items", []):
        public_item = {key: item.get(key) for key in PUBLIC_ITEM_KEYS if key in item}
        items.append(public_item)
    return {
        "schema_version": catalog.get("schema_version", 1),
        "updated_at_bjt": catalog.get("updated_at_bjt", ""),
        "dropbox_root": catalog.get("dropbox_root", ""),
        "item_count": len(items),
        "items": items,
    }


def public_password_rules(rules: dict[str, Any]) -> dict[str, Any]:
    groups = []
    for group in rules.get("groups", []):
        groups.append({
            "id": group.get("id"),
            "label": group.get("label"),
            "password_sha256": group.get("password_sha256"),
            "active": bool(group.get("active", True)),
        })
    return {
        "schema_version": rules.get("schema_version", 1),
        "hash_rule": rules.get("hash_rule", "sha256(PASSWORD_SECRET + ':' + plain_password)"),
        "default_group": rules.get("default_group", "default"),
        "groups": groups,
    }


def copy_site(src: Path, output: Path) -> None:
    if output.exists():
        shutil.rmtree(output)
    shutil.copytree(src, output)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--site-src", default="kc_desk_notes/site_src")
    parser.add_argument("--output-dir", default="_kc_desk_notes_pages")
    parser.add_argument("--catalog-path", default="kc_desk_notes/data/catalog.json")
    parser.add_argument("--password-rules", default="kc_desk_notes/password_rules.json")
    parser.add_argument("--worker-base-url", default="")
    args = parser.parse_args()

    site_src = Path(args.site_src)
    output_dir = Path(args.output_dir)
    copy_site(site_src, output_dir)

    catalog = public_catalog(load_json(Path(args.catalog_path)))
    rules = public_password_rules(load_json(Path(args.password_rules)))
    write_json(output_dir / "data" / "catalog.json", catalog)
    write_json(output_dir / "data" / "password_rules.json", rules)
    write_json(output_dir / "data" / "config.json", {"worker_base_url": args.worker_base_url.rstrip("/")})
    print(f"Built {output_dir} with {catalog['item_count']} catalog items")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
