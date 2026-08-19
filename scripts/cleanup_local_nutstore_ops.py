#!/usr/bin/env python3
"""Safely move expired local Nutstore Ops folders to the macOS Trash."""

from __future__ import annotations

import argparse
import os
import re
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo


TIMEZONE = ZoneInfo("Asia/Hong_Kong")
RETENTION_DAYS = 3
KCDESK_OPS = Path("/Users/ytfeng/Nutstore Files/Nutstore/KCdesk/Ops")
WRONG_PORTAL_OPS = Path("/Users/ytfeng/Nutstore Files/Nutstore/Portal Suite/Ops")
TRASH_ROOT = Path("/Users/ytfeng/.Trash")
DATE_FOLDER_RE = re.compile(r"^20\d{2}-\d{2}-\d{2}$")


@dataclass(frozen=True)
class CleanupPlan:
    expired_dates: tuple[Path, ...]
    wrong_portal_ops: Path | None
    skipped: tuple[str, ...]


def is_real_directory(path: Path) -> bool:
    try:
        return (
            path.is_dir()
            and not path.is_symlink()
            and not path.is_mount()
            and path.resolve(strict=True) == path
        )
    except (FileNotFoundError, OSError):
        return False


def contains_link_or_mount(root: Path) -> bool:
    stack = [root]
    while stack:
        current = stack.pop()
        with os.scandir(current) as entries:
            for entry in entries:
                if entry.is_symlink():
                    return True
                if entry.is_dir(follow_symlinks=False):
                    path = Path(entry.path)
                    if path.is_mount():
                        return True
                    stack.append(path)
    return False


def build_plan(
    kcdesk_ops: Path,
    wrong_portal_ops: Path,
    today: date,
    retention_days: int = RETENTION_DAYS,
) -> CleanupPlan:
    if retention_days < 1:
        raise ValueError("retention_days must be at least 1")

    cutoff = today - timedelta(days=retention_days - 1)
    expired: list[Path] = []
    skipped: list[str] = []

    if is_real_directory(kcdesk_ops):
        with os.scandir(kcdesk_ops) as entries:
            for entry in sorted(entries, key=lambda item: item.name):
                if not DATE_FOLDER_RE.fullmatch(entry.name):
                    continue
                try:
                    folder_date = date.fromisoformat(entry.name)
                except ValueError:
                    skipped.append(f"invalid date folder: {entry.path}")
                    continue
                path = Path(entry.path)
                if folder_date >= cutoff:
                    continue
                if not entry.is_dir(follow_symlinks=False) or entry.is_symlink():
                    skipped.append(f"not a real directory: {path}")
                    continue
                if path.resolve(strict=True) != path:
                    skipped.append(f"resolved path differs: {path}")
                    continue
                if path.is_mount() or contains_link_or_mount(path):
                    skipped.append(f"contains a link or mount: {path}")
                    continue
                expired.append(path)
    elif kcdesk_ops.exists() or kcdesk_ops.is_symlink():
        skipped.append(f"KCdesk Ops is not a real directory: {kcdesk_ops}")
    else:
        skipped.append(f"KCdesk Ops is missing: {kcdesk_ops}")

    portal_target: Path | None = None
    if is_real_directory(wrong_portal_ops):
        if contains_link_or_mount(wrong_portal_ops):
            skipped.append(f"wrong Portal Ops contains a link or mount: {wrong_portal_ops}")
        else:
            portal_target = wrong_portal_ops
    elif wrong_portal_ops.exists() or wrong_portal_ops.is_symlink():
        skipped.append(f"wrong Portal Ops is not a real directory: {wrong_portal_ops}")

    return CleanupPlan(tuple(expired), portal_target, tuple(skipped))


def unique_run_directory(trash_root: Path, now: datetime) -> Path:
    if not is_real_directory(trash_root):
        raise RuntimeError(f"Trash root is not a real directory: {trash_root}")
    base = f"Nutstore Ops cleanup {now.strftime('%Y-%m-%d %H%M%S-%f')}"
    destination = trash_root / base
    destination.mkdir(mode=0o700)
    return destination


def move_atomically(source: Path, destination: Path) -> None:
    if source.lstat().st_dev != destination.parent.lstat().st_dev:
        raise RuntimeError(f"Source and Trash are on different devices: {source}")
    os.replace(source, destination)


def apply_plan(plan: CleanupPlan, trash_root: Path, now: datetime) -> tuple[Path, ...]:
    sources = [*plan.expired_dates]
    if plan.wrong_portal_ops is not None:
        sources.append(plan.wrong_portal_ops)
    if not sources:
        return ()

    if not is_real_directory(trash_root):
        raise RuntimeError(f"Trash root is not a real directory: {trash_root}")
    trash_device = trash_root.lstat().st_dev
    for source in sources:
        if not is_real_directory(source) or contains_link_or_mount(source):
            raise RuntimeError(f"Cleanup target changed or is no longer a real directory: {source}")
        if source.lstat().st_dev != trash_device:
            raise RuntimeError(f"Source and Trash are on different devices: {source}")

    run_dir = unique_run_directory(trash_root, now)
    moved: list[Path] = []
    for source in sources:
        label = (
            f"KCdesk-Ops-{source.name}"
            if source.parent == KCDESK_OPS
            else "Portal Suite-Ops"
        )
        destination = run_dir / label
        move_atomically(source, destination)
        moved.append(destination)
    return tuple(moved)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Move approved targets to the macOS Trash. Without this flag, only preview.",
    )
    args = parser.parse_args()
    now = datetime.now(TIMEZONE)
    plan = build_plan(KCDESK_OPS, WRONG_PORTAL_OPS, now.date())
    cutoff = now.date() - timedelta(days=RETENTION_DAYS - 1)

    print(f"TODAY={now.date().isoformat()} CUTOFF={cutoff.isoformat()} RETENTION_DAYS={RETENTION_DAYS}")
    print(
        "EXPIRED_DATE_FOLDERS="
        + (",".join(path.name for path in plan.expired_dates) or "-")
    )
    print(f"WRONG_PORTAL_OPS={'yes' if plan.wrong_portal_ops else 'no'}")
    for message in plan.skipped:
        print(f"SKIPPED {message}")

    if not args.apply:
        print("DRY_RUN_COMPLETE")
        return 0

    moved = apply_plan(plan, TRASH_ROOT, now)
    for destination in moved:
        print(f"MOVED_TO_TRASH {destination}")
    print(f"CLEANUP_COMPLETE moved={len(moved)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
