#!/usr/bin/env python3
"""Rebuild ``shard_N`` directories from downloaded GitHub Actions artifacts."""
from __future__ import annotations

import argparse
import re
import shutil
from pathlib import Path


ARTIFACT_INDEX_RE = re.compile(r"-(\d+)$")
REPORT_MARKERS = ("wechat_article.md", "note.md", "source_mineru.md")


def artifact_index(path: Path) -> int:
    match = ARTIFACT_INDEX_RE.search(path.name)
    if not match:
        raise RuntimeError(f"Cannot resolve shard index from artifact directory: {path.name}")
    return int(match.group(1))


def report_dirs(shard_dir: Path) -> list[Path]:
    return sorted(
        child
        for child in shard_dir.iterdir()
        if child.is_dir() and any((child / marker).exists() for marker in REPORT_MARKERS)
    )


def materialize(
    artifact_root: Path,
    destination: Path,
    expected_shards: int = 0,
    expected_reports: int = 0,
) -> tuple[int, int]:
    if not artifact_root.is_dir():
        raise RuntimeError(f"Artifact root does not exist: {artifact_root}")
    artifact_dirs = sorted(
        (
            path
            for path in artifact_root.iterdir()
            if path.is_dir() and ARTIFACT_INDEX_RE.search(path.name)
        ),
        key=artifact_index,
    )
    if not artifact_dirs:
        raise RuntimeError(f"No shard artifact directories found under {artifact_root}")

    indexed = [(artifact_index(path), path) for path in artifact_dirs]
    indices = [index for index, _path in indexed]
    if len(set(indices)) != len(indices):
        raise RuntimeError(f"Duplicate shard artifact indices: {indices}")
    if expected_shards and len(indexed) != expected_shards:
        raise RuntimeError(f"Expected {expected_shards} shard artifacts, found {len(indexed)}: {indices}")

    destination.mkdir(parents=True, exist_ok=True)
    total_reports = 0
    for index, artifact_dir in indexed:
        shard_destination = destination / f"shard_{index}"
        if shard_destination.is_symlink():
            shard_destination.unlink()
        elif shard_destination.exists():
            shutil.rmtree(shard_destination)
        shutil.copytree(artifact_dir, shard_destination)
        reports = report_dirs(shard_destination)
        if not reports:
            raise RuntimeError(f"Shard artifact {artifact_dir.name} contains no report markers")
        total_reports += len(reports)
        print(f"Materialized {artifact_dir.name} -> {shard_destination} ({len(reports)} reports)")

    if expected_reports and total_reports != expected_reports:
        raise RuntimeError(f"Expected {expected_reports} reports, found {total_reports}")
    print(f"Materialized shard artifacts: shards={len(indexed)}, reports={total_reports}")
    return len(indexed), total_reports


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True)
    parser.add_argument("--destination", required=True)
    parser.add_argument("--expected-shards", type=int, default=0)
    parser.add_argument("--expected-reports", type=int, default=0)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    materialize(
        Path(args.artifact_root),
        Path(args.destination),
        max(0, args.expected_shards),
        max(0, args.expected_reports),
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
