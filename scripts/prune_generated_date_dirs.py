#!/usr/bin/env python3
"""Keep only the newest date-named folders under generated output roots."""

from __future__ import annotations

import argparse
import shutil
from datetime import datetime
from pathlib import Path


DEFAULT_ROOTS = [
    "xhs_notes/dropbox",
    "publish_ready_zips",
    "bank_report_catalogs",
    "market_view_summaries",
    "bilingual_podcast_videos",
    "kc_translated_reports",
]


def parse_date_dir(name: str) -> datetime | None:
    try:
        if name.isdigit() and len(name) == 6:
            return datetime.strptime(name, "%y%m%d")
        if name.isdigit() and len(name) == 8:
            return datetime.strptime(name, "%Y%m%d")
    except ValueError:
        return None
    return None


def prune_root(root: Path, keep: int, dry_run: bool) -> tuple[list[Path], list[Path]]:
    if not root.exists():
        print(f"skip missing root: {root}")
        return [], []
    if not root.is_dir():
        raise NotADirectoryError(root)

    dated_dirs: list[tuple[datetime, Path]] = []
    for child in root.iterdir():
        if not child.is_dir():
            continue
        parsed = parse_date_dir(child.name)
        if parsed is not None:
            dated_dirs.append((parsed, child))

    dated_dirs.sort(key=lambda item: (item[0], item[1].name), reverse=True)
    keep_dirs = [path for _, path in dated_dirs[:keep]]
    remove_dirs = [path for _, path in dated_dirs[keep:]]

    print(f"{root}: keeping {len(keep_dirs)} of {len(dated_dirs)} date folders")
    for path in keep_dirs:
        print(f"  keep   {path}")
    for path in remove_dirs:
        print(f"  remove {path}")
        if not dry_run:
            shutil.rmtree(path)

    return keep_dirs, remove_dirs


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Prune generated output directories, keeping the newest date folders."
    )
    parser.add_argument(
        "--root",
        action="append",
        dest="roots",
        help="Generated output root to prune. Defaults to the repo's heavy output roots.",
    )
    parser.add_argument("--keep", type=int, default=3, help="Number of latest date folders to keep.")
    parser.add_argument("--dry-run", action="store_true", help="Print removals without deleting.")
    args = parser.parse_args()

    if args.keep < 1:
        raise ValueError("--keep must be at least 1")

    roots = [Path(root) for root in (args.roots or DEFAULT_ROOTS)]
    total_removed = 0
    for root in roots:
        _, removed = prune_root(root, args.keep, args.dry_run)
        total_removed += len(removed)

    action = "would remove" if args.dry_run else "removed"
    print(f"{action} {total_removed} old date folders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
