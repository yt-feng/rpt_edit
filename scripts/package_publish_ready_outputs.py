#!/usr/bin/env python3
"""Package publish-ready outputs from a completed Final PDF to XHS run.

The input is usually xhs_notes/dropbox/<date>/shard_*/. A shard is included only
when it contains at least one generated report folder. MinerU raw folders are
excluded from the ZIP.
"""
from __future__ import annotations

import argparse
import json
import re
import zipfile
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
    # Some partially generated folders may only have final status and images.
    if (path / "status.json").exists() and any(p.suffix.lower() in {".png", ".jpg", ".jpeg"} for p in path.rglob("*")):
        return True
    return False


def shard_report_dirs(shard_dir: Path) -> list[Path]:
    return sorted(p for p in shard_dir.iterdir() if is_report_dir(p))


def should_include_top_level_file(path: Path) -> bool:
    # Keep progress and manifest files so the ZIP is auditable, but do not let
    # an empty shard with only logs count as publish-ready.
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


def iter_files_for_shard(shard_dir: Path, report_dirs: list[Path], exclude_source_mineru: bool) -> list[Path]:
    files: list[Path] = []
    for path in sorted(shard_dir.iterdir()):
        if path.is_file() and should_include_top_level_file(path) and not is_raw_file(path, exclude_source_mineru):
            files.append(path)
    for report_dir in report_dirs:
        for path in sorted(report_dir.rglob("*")):
            if path.is_dir():
                continue
            if any(is_raw_dir(parent) for parent in path.parents if parent != shard_dir.parent):
                continue
            if is_raw_file(path, exclude_source_mineru):
                continue
            files.append(path)
    return files


def build_package(date_dir: Path, output_root: Path, exclude_source_mineru: bool) -> dict[str, Any]:
    if not date_dir.exists():
        raise RuntimeError(f"Date output folder not found: {date_dir}")
    date_name = date_dir.name
    output_dir = output_root / date_name
    output_dir.mkdir(parents=True, exist_ok=True)
    zip_path = output_dir / f"publish_ready_{date_name}.zip"

    included_shards: list[dict[str, Any]] = []
    skipped_shards: list[str] = []
    total_files = 0

    with zipfile.ZipFile(zip_path, "w", compression=zipfile.ZIP_DEFLATED, compresslevel=6) as zf:
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
            for file_path in files:
                arcname = Path(date_name) / file_path.relative_to(date_dir)
                zf.write(file_path, arcname.as_posix())
            included_shards.append({
                "shard": shard_dir.name,
                "report_count": len(report_dirs),
                "file_count": len(files),
                "reports": [p.name for p in report_dirs],
            })
            total_files += len(files)
            log(f"Included {shard_dir.name}: reports={len(report_dirs)}, files={len(files)}")

    if not included_shards:
        # Remove empty package to avoid publishing a misleading ZIP.
        if zip_path.exists():
            zip_path.unlink()
        raise RuntimeError(f"No publish-ready shard outputs found under {date_dir}")

    summary = {
        "created_at_utc": datetime.now(timezone.utc).isoformat(),
        "source_date_dir": str(date_dir),
        "zip_path": str(zip_path),
        "zip_size_bytes": zip_path.stat().st_size,
        "exclude_source_mineru": exclude_source_mineru,
        "included_shard_count": len(included_shards),
        "skipped_shards": skipped_shards,
        "total_files": total_files,
        "included_shards": included_shards,
    }
    summary_path = output_dir / f"publish_ready_{date_name}_summary.json"
    summary_path.write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"Wrote package: {zip_path} ({zip_path.stat().st_size} bytes)")
    log(f"Wrote summary: {summary_path}")
    return summary


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--date-dir", required=True, help="e.g. xhs_notes/dropbox/260514")
    parser.add_argument("--output-root", default="publish_ready_zips")
    parser.add_argument("--include-source-mineru", action="store_true", help="include source_mineru.md in the ZIP")
    args = parser.parse_args()
    build_package(Path(args.date_dir), Path(args.output_root), exclude_source_mineru=not args.include_source_mineru)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
