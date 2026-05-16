#!/usr/bin/env python3
"""Package publish-ready outputs from a completed Final PDF to XHS run.

The input is usually xhs_notes/dropbox/<date>/shard_*/. A shard is included only
when it contains at least one generated report folder. MinerU raw folders are
excluded from the ZIP.

GitHub blocks single files over 100 MB, so this script creates multiple ZIP
parts by default, each targeting less than --max-zip-mb. The workflow can then
commit the parts safely while the full folder is also uploaded as an artifact.

For mobile publishing convenience, Markdown files are stored inside the ZIP with
.txt suffixes, without changing the original repository files.
"""
from __future__ import annotations

import argparse
import json
import re
import zipfile
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

REPORT_MARKERS = {
    "note.md",
    "wechat_article.md",
    "wechat_article_en.md",
    "xianyu_note.md",
    "podcast_script_zh.md",
    "podcast_script_en.md",
}
RAW_DIR_PATTERNS = [
    re.compile(r"(^|[-_\s])mineru([-_\s]|$)", re.I),
    re.compile(r"(^|[-_\s])raw([-_\s]|$)", re.I),
    re.compile(r"mineru.*raw|raw.*mineru", re.I),
]
RAW_FILE_PATTERNS = [
    re.compile(r"mineru.*raw|raw.*mineru", re.I),
]


@dataclass
class PackageFile:
    source: Path
    arcname: str
    shard: str
    report: str | None
    size: int
    renamed_markdown: bool = False


def log(message: str) -> None:
    print(message, flush=True)


def is_raw_dir(path: Path) -> bool:
    name = path.name.strip()
    return any(pattern.search(name) for pattern in RAW_DIR_PATTERNS)


def is_raw_file(path: Path, exclude_source_mineru: bool) -> bool:
    name = path.name.strip()
    if exclude_source_mineru and name == "source_mineru.md":
        return True
    return any(pattern.search(name) for pattern in RAW_FILE_PATTERNS)


def is_report_dir(path: Path) -> bool:
    if not path.is_dir():
        return False
    for marker in REPORT_MARKERS:
        if (path / marker).exists():
            return True
    if (path / "status.json").exists() and any(p.suffix.lower() in {".png", ".jpg", ".jpeg"} for p in path.rglob("*")):
        return True
    return False


def shard_report_dirs(shard_dir: Path) -> list[Path]:
    return sorted(p for p in shard_dir.iterdir() if is_report_dir(p))


def should_include_top_level_file(path: Path) -> bool:
    allowed = {
        "shard_run_summary.md",
        "finalize_summary.json",
        "sensitive_content_guard_summary.json",
        "batch_run_summary.json",
        "postprocess_summary.json",
        "selected_to_process_manifest.json",
        "selected_macro_candidates.json",
        "macro_classification_all.json",
    }
    return path.name in allowed or path.name.endswith("_progress.log")


def package_arcname(date_name: str, rel: Path) -> tuple[str, bool]:
    """Return ZIP path. Rename .md files to .txt for mobile compatibility."""
    renamed = rel.suffix.lower() == ".md"
    if renamed:
        rel = rel.with_suffix(".txt")
    return (Path(date_name) / rel).as_posix(), renamed


def iter_files_for_shard(shard_dir: Path, report_dirs: list[Path], exclude_source_mineru: bool) -> list[Path]:
    files: list[Path] = []
    for path in sorted(shard_dir.iterdir()):
        if path.is_file() and should_include_top_level_file(path) and not is_raw_file(path, exclude_source_mineru):
            files.append(path)
    report_set = {p.resolve() for p in report_dirs}
    for report_dir in report_dirs:
        for path in sorted(report_dir.rglob("*")):
            if path.is_dir():
                continue
            if any(is_raw_dir(parent) for parent in path.parents if parent.resolve() not in report_set and parent != shard_dir):
                continue
            if is_raw_file(path, exclude_source_mineru):
                continue
            files.append(path)
    return files


def collect_package_files(date_dir: Path, exclude_source_mineru: bool) -> tuple[list[PackageFile], list[dict[str, Any]], list[str]]:
    date_name = date_dir.name
    package_files: list[PackageFile] = []
    included_shards: list[dict[str, Any]] = []
    skipped_shards: list[str] = []

    for shard_dir in sorted(date_dir.glob("shard_*")):
        if not shard_dir.is_dir():
            continue
        report_dirs = shard_report_dirs(shard_dir)
        if not report_dirs:
            skipped_shards.append(shard_dir.name)
            log(f"Skip {shard_dir.name}: no generated report folder.")
            continue
        files = iter_files_for_shard(shard_dir, report_dirs, exclude_source_mineru)
        if not files:
            skipped_shards.append(shard_dir.name)
            log(f"Skip {shard_dir.name}: no publish-ready files after filtering.")
            continue
        report_names = {p.name for p in report_dirs}
        renamed_markdown_count = 0
        for file_path in files:
            rel = file_path.relative_to(date_dir)
            report_name = None
            parts = rel.parts
            if len(parts) >= 2 and parts[1] in report_names:
                report_name = parts[1]
            arcname, renamed_markdown = package_arcname(date_name, rel)
            if renamed_markdown:
                renamed_markdown_count += 1
            package_files.append(PackageFile(
                source=file_path,
                arcname=arcname,
                shard=shard_dir.name,
                report=report_name,
                size=file_path.stat().st_size,
                renamed_markdown=renamed_markdown,
            ))
        included_shards.append({
            "shard": shard_dir.name,
            "report_count": len(report_dirs),
            "file_count": len(files),
            "renamed_markdown_count": renamed_markdown_count,
            "raw_file_bytes": sum(p.stat().st_size for p in files),
            "reports": [p.name for p in report_dirs],
        })
        log(f"Collected {shard_dir.name}: reports={len(report_dirs)}, files={len(files)}, md_to_txt={renamed_markdown_count}")
    return package_files, included_shards, skipped_shards


def write_zip(zip_path: Path, files: list[PackageFile]) -> dict[str, Any]:
    seen_arcnames: set[str] = set()
    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6, allowZip64=True) as zf:
        for item in files:
            arcname = item.arcname
            if arcname in seen_arcnames:
                base = Path(arcname)
                arcname = (base.parent / f"{base.stem}_{len(seen_arcnames):04d}{base.suffix}").as_posix()
            seen_arcnames.add(arcname)
            zf.write(item.source, arcname)
    return {
        "path": str(zip_path),
        "size_bytes": zip_path.stat().st_size,
        "file_count": len(files),
        "renamed_markdown_count": sum(1 for item in files if item.renamed_markdown),
        "raw_file_bytes": sum(item.size for item in files),
        "shards": sorted({item.shard for item in files}),
    }


def split_into_parts(files: list[PackageFile], max_zip_bytes: int) -> list[list[PackageFile]]:
    parts: list[list[PackageFile]] = []
    current: list[PackageFile] = []
    current_bytes = 0
    for item in files:
        # Approximate by source size because PNG/JPEG files rarely compress much.
        if current and current_bytes + item.size > max_zip_bytes:
            parts.append(current)
            current = []
            current_bytes = 0
        current.append(item)
        current_bytes += item.size
    if current:
        parts.append(current)
    return parts


def build_package(date_dir: Path, output_root: Path, exclude_source_mineru: bool, max_zip_mb: int, single_zip: bool) -> dict[str, Any]:
    if not date_dir.exists():
        raise RuntimeError(f"Date output folder not found: {date_dir}")
    date_name = date_dir.name
    output_dir = output_root / date_name
    output_dir.mkdir(parents=True, exist_ok=True)

    # Clear stale ZIPs from previous attempts so a failed >100 MB zip does not get committed later.
    for stale in output_dir.glob(f"publish_ready_{date_name}*.zip"):
        stale.unlink()

    package_files, included_shards, skipped_shards = collect_package_files(date_dir, exclude_source_mineru)
    if not included_shards or not package_files:
        raise RuntimeError(f"No publish-ready shard outputs found under {date_dir}")

    max_zip_bytes = max_zip_mb * 1024 * 1024
    if single_zip:
        parts = [package_files]
    else:
        parts = split_into_parts(package_files, max_zip_bytes)

    zip_entries: list[dict[str, Any]] = []
    if len(parts) == 1:
        zip_path = output_dir / f"publish_ready_{date_name}.zip"
        zip_entries.append(write_zip(zip_path, parts[0]))
    else:
        for idx, part_files in enumerate(parts, 1):
            zip_path = output_dir / f"publish_ready_{date_name}_part{idx:03d}.zip"
            zip_entries.append(write_zip(zip_path, part_files))

    oversized = [entry for entry in zip_entries if entry["size_bytes"] > 100 * 1024 * 1024]
    if oversized:
        log("WARNING: Some ZIP parts still exceed GitHub's 100 MB per-file limit:")
        for entry in oversized:
            log(f"  {entry['path']} = {entry['size_bytes']} bytes")

    summary = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_date_dir": str(date_dir),
        "output_dir": str(output_dir),
        "max_zip_mb": max_zip_mb,
        "single_zip": single_zip,
        "exclude_source_mineru": exclude_source_mineru,
        "markdown_files_renamed_to_txt": True,
        "included_shard_count": len(included_shards),
        "skipped_shards": skipped_shards,
        "total_files": len(package_files),
        "total_renamed_markdown_count": sum(1 for item in package_files if item.renamed_markdown),
        "total_raw_file_bytes": sum(item.size for item in package_files),
        "zip_count": len(zip_entries),
        "zips": zip_entries,
        "included_shards": included_shards,
    }
    summary_path = output_dir / f"publish_ready_{date_name}_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    for entry in zip_entries:
        log(f"Wrote package: {entry['path']} ({entry['size_bytes']} bytes, {entry['file_count']} files, md_to_txt={entry['renamed_markdown_count']})")
    log(f"Wrote summary: {summary_path}")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date-dir", required=True, help="e.g. xhs_notes/dropbox/260514")
    parser.add_argument("--output-root", default="publish_ready_zips")
    parser.add_argument("--include-source-mineru", action="store_true", help="include source_mineru.md in the ZIP")
    parser.add_argument("--max-zip-mb", type=int, default=90, help="target max size per zip part for GitHub commit safety")
    parser.add_argument("--single-zip", action="store_true", help="write one ZIP even if it exceeds GitHub's 100 MB file limit")
    args = parser.parse_args()
    build_package(
        Path(args.date_dir),
        Path(args.output_root),
        exclude_source_mineru=not args.include_source_mineru,
        max_zip_mb=args.max_zip_mb,
        single_zip=args.single_zip,
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
