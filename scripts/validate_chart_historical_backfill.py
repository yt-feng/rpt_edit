#!/usr/bin/env python3
"""Fail-closed validation for chart-only historical PDF backfills."""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import re
import sys
import unicodedata
from collections import Counter
from pathlib import Path, PurePosixPath
from typing import Any


DATE_FOLDER_RE = re.compile(r"^[0-9]{6,8}$")
SOURCE_MANIFEST = "selected_to_process_manifest.json"
SOURCE_ALLOWED_SUFFIXES = {".json", ".log", ".md", ".pdf", ".txt"}
SOURCE_IMAGE_RE = re.compile(r"^source_image_([0-9]+)\.(?:png|jpe?g|webp)$", re.IGNORECASE)
FORBIDDEN_CHART_OUTPUT_NAMES = {
    "note.md",
    "wechat_article.md",
    "prompt_for_xhs.md",
    "prompt_for_wechat.md",
    "cover.png",
}


class ValidationError(RuntimeError):
    pass


def load_json(path: Path) -> Any:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as exc:
        raise ValidationError(f"Invalid JSON file: {path.name}") from exc


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def normalized_name(value: str) -> str:
    return unicodedata.normalize("NFC", value).casefold()


def validate_date_folder(value: str) -> str:
    value = str(value or "").strip()
    if not DATE_FOLDER_RE.fullmatch(value):
        raise ValidationError("date_folder must contain exactly 6-8 digits")
    return value


def validate_positive(value: int, label: str, *, maximum: int = 200) -> int:
    value = int(value)
    if value < 1 or value > maximum:
        raise ValidationError(f"{label} must be between 1 and {maximum}")
    return value


def validate_tree(root: Path) -> Path:
    if root.is_symlink():
        raise ValidationError(f"Symlinked root is not allowed: {root.name}")
    root = root.resolve()
    if not root.is_dir():
        raise ValidationError(f"Directory does not exist: {root}")
    for path in root.rglob("*"):
        if path.is_symlink():
            raise ValidationError(f"Symlinks are not allowed: {path.relative_to(root)}")
    return root


def validate_pdf(path: Path) -> tuple[int, str, int]:
    try:
        with path.open("rb") as handle:
            header = handle.read(1024)
    except OSError as exc:
        raise ValidationError(f"Cannot read PDF: {path.name}") from exc
    if b"%PDF-" not in header:
        raise ValidationError(f"File does not contain a PDF header: {path.name}")

    try:
        import fitz  # type: ignore

        with fitz.open(path) as document:
            if document.needs_pass:
                raise ValidationError(f"Password-protected PDF is not supported: {path.name}")
            page_count = int(document.page_count)
    except ValidationError:
        raise
    except Exception as exc:  # pragma: no cover - library-specific errors vary
        raise ValidationError(f"Unreadable PDF: {path.name}") from exc
    if page_count < 1:
        raise ValidationError(f"PDF has no pages: {path.name}")
    return path.stat().st_size, sha256_file(path), page_count


def date_in_dropbox_path(value: Any, date_folder: str) -> bool:
    raw = str(value or "").strip().replace("\\", "/")
    if not raw:
        return False
    return date_folder in PurePosixPath(raw).parts


def source_inventory(
    artifact_root: Path,
    *,
    date_folder: str,
    expected_pdf_count: int,
    reports_per_shard: int,
) -> dict[str, Any]:
    date_folder = validate_date_folder(date_folder)
    expected_pdf_count = validate_positive(expected_pdf_count, "expected_pdf_count")
    reports_per_shard = validate_positive(reports_per_shard, "reports_per_shard", maximum=50)
    artifact_root = validate_tree(artifact_root)

    unexpected = [
        path.relative_to(artifact_root).as_posix()
        for path in artifact_root.rglob("*")
        if path.is_file() and path.suffix.casefold() not in SOURCE_ALLOWED_SUFFIXES
    ]
    if unexpected:
        raise ValidationError(f"Unexpected source artifact file type: {unexpected[0]}")

    pdfs = sorted(
        path for path in artifact_root.rglob("*") if path.is_file() and path.suffix.casefold() == ".pdf"
    )
    if len(pdfs) != expected_pdf_count:
        raise ValidationError(
            f"Expected exactly {expected_pdf_count} PDFs, found {len(pdfs)}"
        )

    manifest_path = artifact_root / SOURCE_MANIFEST
    if not manifest_path.is_file():
        raise ValidationError(f"Missing source manifest: {SOURCE_MANIFEST}")
    manifest = load_json(manifest_path)
    if not isinstance(manifest, list) or len(manifest) != expected_pdf_count:
        raise ValidationError(
            f"Source manifest must contain exactly {expected_pdf_count} rows"
        )

    manifest_names: list[str] = []
    ranks: list[int] = []
    for index, row in enumerate(manifest, 1):
        if not isinstance(row, dict):
            raise ValidationError(f"Source manifest row {index} is not an object")
        process_path = str(row.get("process_local_path") or "").strip()
        process_name = Path(process_path).name
        if not process_name or Path(process_name).suffix.casefold() != ".pdf":
            raise ValidationError(f"Source manifest row {index} has no processed PDF name")
        if any(character in process_name for character in "\r\n\0"):
            raise ValidationError(f"Source manifest row {index} has an unsafe PDF name")
        manifest_names.append(normalized_name(process_name))
        try:
            ranks.append(int(row.get("process_rank")))
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"Source manifest row {index} has no integer process_rank") from exc
        if not date_in_dropbox_path(row.get("dropbox_path"), date_folder):
            raise ValidationError(
                f"Source manifest row {index} is not anchored to date folder {date_folder}"
            )

    pdf_names = [normalized_name(path.name) for path in pdfs]
    if Counter(pdf_names) != Counter(manifest_names):
        raise ValidationError("Source manifest PDF names do not exactly match the artifact PDFs")
    if sorted(ranks) != list(range(1, expected_pdf_count + 1)):
        raise ValidationError("Source manifest process_rank values are not a complete 1-based sequence")

    rows: list[dict[str, Any]] = []
    for path in pdfs:
        size, digest, page_count = validate_pdf(path)
        rows.append(
            {
                "path": path.relative_to(artifact_root).as_posix(),
                "bytes": size,
                "sha256": digest,
                "page_count": page_count,
            }
        )

    shard_count = math.ceil(expected_pdf_count / reports_per_shard)
    return {
        "schema_version": 1,
        "date_folder": date_folder,
        "pdf_count": len(rows),
        "reports_per_shard": reports_per_shard,
        "effective_shard_count": shard_count,
        "shard_indices": list(range(shard_count)),
        "pdfs": rows,
    }


def validate_image(path: Path) -> tuple[int, int, str]:
    try:
        from PIL import Image

        with Image.open(path) as image:
            width, height = image.size
            image.verify()
    except Exception as exc:  # pragma: no cover - Pillow error types vary
        raise ValidationError(f"Unreadable chart image: {path.name}") from exc
    if width < 1 or height < 1:
        raise ValidationError(f"Chart image has invalid dimensions: {path.name}")
    return width, height, sha256_file(path)


def shard_inventory(
    output_root: Path,
    *,
    date_folder: str,
    expected_pdf_count: int,
    reports_per_shard: int,
    shard_index: int,
) -> dict[str, Any]:
    date_folder = validate_date_folder(date_folder)
    expected_pdf_count = validate_positive(expected_pdf_count, "expected_pdf_count")
    reports_per_shard = validate_positive(reports_per_shard, "reports_per_shard", maximum=50)
    output_root = validate_tree(output_root)
    effective_shards = math.ceil(expected_pdf_count / reports_per_shard)
    if shard_index < 0 or shard_index >= effective_shards:
        raise ValidationError(f"shard_index must be between 0 and {effective_shards - 1}")
    expected_shard_reports = min(
        reports_per_shard,
        expected_pdf_count - shard_index * reports_per_shard,
    )

    forbidden: list[str] = []
    for path in output_root.rglob("*"):
        if path.is_dir() and path.name == "mineru_raw":
            forbidden.append(path.relative_to(output_root).as_posix())
        elif path.is_file() and (
            path.name in FORBIDDEN_CHART_OUTPUT_NAMES
            or path.name.startswith("xhs_card_")
            or path.suffix.casefold() in {".pdf", ".zip"}
        ):
            forbidden.append(path.relative_to(output_root).as_posix())
    if forbidden:
        raise ValidationError(f"Chart-only output contains forbidden file: {forbidden[0]}")

    batch_summary_path = output_root / "batch_run_summary.json"
    if not batch_summary_path.is_file():
        raise ValidationError("Missing batch_run_summary.json")
    batch_summary = load_json(batch_summary_path)
    expected_summary = {
        "total_pdf_count_before_shard": expected_pdf_count,
        "pdf_count_before_skip": expected_shard_reports,
        "pdf_count": expected_shard_reports,
        "generated_report_count": expected_shard_reports,
        "failures": 0,
        "shard_index": shard_index,
        "shard_count": effective_shards,
    }
    for key, expected in expected_summary.items():
        if int(batch_summary.get(key, -1)) != expected:
            raise ValidationError(
                f"Batch summary {key} mismatch: expected {expected}, got {batch_summary.get(key)!r}"
            )
    if batch_summary.get("chart_source_only") is not True:
        raise ValidationError("Batch summary is not marked chart_source_only")

    reports: list[dict[str, Any]] = []
    source_names: set[str] = set()
    for report_dir in sorted(path for path in output_root.iterdir() if path.is_dir()):
        status_path = report_dir / "status.json"
        source_markdown = report_dir / "source_mineru.md"
        if not status_path.is_file() or not source_markdown.is_file():
            raise ValidationError(f"Incomplete chart report directory: {report_dir.name}")
        if source_markdown.stat().st_size < 1:
            raise ValidationError(f"Empty MinerU markdown: {report_dir.name}")
        status = load_json(status_path)
        if not isinstance(status, dict) or status.get("chart_source_only") is not True:
            raise ValidationError(f"Report is not marked chart_source_only: {report_dir.name}")
        if status.get("error"):
            raise ValidationError(f"Report contains an extraction error: {report_dir.name}")
        source_name = str(status.get("source_pdf") or "").strip()
        if not source_name or Path(source_name).name != source_name or "\\" in source_name:
            raise ValidationError(f"Report exposes a non-basename source path: {report_dir.name}")
        normalized_source = normalized_name(source_name)
        if normalized_source in source_names:
            raise ValidationError(f"Duplicate source PDF in shard output: {source_name}")
        source_names.add(normalized_source)

        images: list[dict[str, Any]] = []
        assets_dir = report_dir / "assets"
        if assets_dir.is_dir():
            numbered: list[tuple[int, Path]] = []
            for image_path in sorted(assets_dir.iterdir()):
                if not image_path.is_file():
                    continue
                match = SOURCE_IMAGE_RE.fullmatch(image_path.name)
                if not match:
                    raise ValidationError(f"Unexpected chart asset: {image_path.name}")
                numbered.append((int(match.group(1)), image_path))
            if [number for number, _path in numbered] != list(range(1, len(numbered) + 1)):
                raise ValidationError(f"Chart image ordinals are not contiguous: {report_dir.name}")
            for ordinal, image_path in numbered:
                width, height, digest = validate_image(image_path)
                images.append(
                    {
                        "ordinal": ordinal,
                        "path": image_path.relative_to(output_root).as_posix(),
                        "width": width,
                        "height": height,
                        "sha256": digest,
                    }
                )
        if int(status.get("chart_source_image_count", -1)) != len(images):
            raise ValidationError(f"Chart image count mismatch: {report_dir.name}")
        reports.append(
            {
                "report_dir": report_dir.name,
                "source_pdf": source_name,
                "source_markdown_bytes": source_markdown.stat().st_size,
                "chart_count": len(images),
                "charts": images,
            }
        )

    if len(reports) != expected_shard_reports:
        raise ValidationError(
            f"Expected {expected_shard_reports} complete report directories, found {len(reports)}"
        )
    return {
        "schema_version": 1,
        "date_folder": date_folder,
        "shard_index": shard_index,
        "expected_report_count": expected_shard_reports,
        "report_count": len(reports),
        "chart_count": sum(int(report["chart_count"]) for report in reports),
        "reports": reports,
    }


def aggregate_inventory(
    inventory_root: Path,
    *,
    date_folder: str,
    expected_pdf_count: int,
    expected_shards: int,
) -> dict[str, Any]:
    """Require a complete, non-duplicated set of useful shard inventories."""
    date_folder = validate_date_folder(date_folder)
    expected_pdf_count = validate_positive(expected_pdf_count, "expected_pdf_count")
    expected_shards = validate_positive(expected_shards, "expected_shards", maximum=200)
    inventory_root = validate_tree(inventory_root)
    inventory_paths = sorted(inventory_root.rglob("validated_chart_shard_inventory.json"))
    if len(inventory_paths) != expected_shards:
        raise ValidationError(
            f"Expected exactly {expected_shards} shard inventories, found {len(inventory_paths)}"
        )

    by_shard: dict[int, dict[str, Any]] = {}
    source_names: set[str] = set()
    total_reports = 0
    total_charts = 0
    for path in inventory_paths:
        inventory = load_json(path)
        if not isinstance(inventory, dict) or int(inventory.get("schema_version") or 0) != 1:
            raise ValidationError(f"Unsupported shard inventory: {path.parent.name}")
        if str(inventory.get("date_folder") or "") != date_folder:
            raise ValidationError(f"Shard inventory date mismatch: {path.parent.name}")
        try:
            shard_index = int(inventory.get("shard_index"))
            report_count = int(inventory.get("report_count"))
            expected_report_count = int(inventory.get("expected_report_count"))
            declared_chart_count = int(inventory.get("chart_count"))
        except (TypeError, ValueError) as exc:
            raise ValidationError(f"Shard inventory has invalid counts: {path.parent.name}") from exc
        if shard_index in by_shard:
            raise ValidationError(f"Duplicate shard inventory index: {shard_index}")
        if shard_index < 0 or shard_index >= expected_shards:
            raise ValidationError(f"Shard inventory index is out of range: {shard_index}")
        reports = inventory.get("reports")
        if not isinstance(reports, list) or len(reports) != report_count:
            raise ValidationError(f"Shard inventory report_count mismatch: {shard_index}")
        if report_count != expected_report_count or report_count < 1:
            raise ValidationError(f"Shard inventory is incomplete: {shard_index}")

        computed_chart_count = 0
        for report in reports:
            if not isinstance(report, dict):
                raise ValidationError(f"Shard inventory contains an invalid report: {shard_index}")
            source_name = str(report.get("source_pdf") or "").strip()
            if not source_name or Path(source_name).name != source_name or "\\" in source_name:
                raise ValidationError(f"Shard inventory exposes an invalid source name: {shard_index}")
            normalized_source = normalized_name(source_name)
            if normalized_source in source_names:
                raise ValidationError(f"Duplicate source PDF across shard inventories: {source_name}")
            source_names.add(normalized_source)
            charts = report.get("charts")
            try:
                report_chart_count = int(report.get("chart_count"))
            except (TypeError, ValueError) as exc:
                raise ValidationError(f"Invalid report chart count: {source_name}") from exc
            if report_chart_count < 0 or not isinstance(charts, list) or len(charts) != report_chart_count:
                raise ValidationError(f"Report chart inventory mismatch: {source_name}")
            computed_chart_count += report_chart_count
        if computed_chart_count != declared_chart_count:
            raise ValidationError(f"Shard chart_count mismatch: {shard_index}")

        by_shard[shard_index] = {
            "report_count": report_count,
            "chart_count": computed_chart_count,
        }
        total_reports += report_count
        total_charts += computed_chart_count

    expected_indices = set(range(expected_shards))
    if set(by_shard) != expected_indices:
        missing = sorted(expected_indices - set(by_shard))
        raise ValidationError(f"Missing shard inventory indices: {missing}")
    if total_reports != expected_pdf_count or len(source_names) != expected_pdf_count:
        raise ValidationError(
            f"Expected exactly {expected_pdf_count} unique reports, found {total_reports}"
        )
    minimum_chart_count = expected_pdf_count
    if total_charts < minimum_chart_count:
        raise ValidationError(
            f"Chart source candidates below minimum: expected at least {minimum_chart_count}, found {total_charts}"
        )

    return {
        "schema_version": 1,
        "date_folder": date_folder,
        "shard_count": len(by_shard),
        "report_count": total_reports,
        "chart_count": total_charts,
        "minimum_chart_count": minimum_chart_count,
        "shards": [
            {"shard_index": shard_index, **by_shard[shard_index]}
            for shard_index in sorted(by_shard)
        ],
    }


def append_github_outputs(path: Path, inventory: dict[str, Any]) -> None:
    lines = [
        f"pdf_count={inventory['pdf_count']}",
        f"effective_shard_count={inventory['effective_shard_count']}",
        "shard_indices=" + json.dumps(inventory["shard_indices"], separators=(",", ":")),
    ]
    with path.open("a", encoding="utf-8") as handle:
        handle.write("\n".join(lines) + "\n")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)

    source = subparsers.add_parser("source")
    source.add_argument("--artifact-root", required=True)
    source.add_argument("--date-folder", required=True)
    source.add_argument("--expected-pdf-count", required=True, type=int)
    source.add_argument("--reports-per-shard", required=True, type=int)
    source.add_argument("--inventory", required=True)
    source.add_argument("--github-output")

    shard = subparsers.add_parser("shard")
    shard.add_argument("--output-root", required=True)
    shard.add_argument("--date-folder", required=True)
    shard.add_argument("--expected-pdf-count", required=True, type=int)
    shard.add_argument("--reports-per-shard", required=True, type=int)
    shard.add_argument("--shard-index", required=True, type=int)
    shard.add_argument("--inventory", required=True)

    aggregate = subparsers.add_parser("aggregate")
    aggregate.add_argument("--inventory-root", required=True)
    aggregate.add_argument("--date-folder", required=True)
    aggregate.add_argument("--expected-pdf-count", required=True, type=int)
    aggregate.add_argument("--expected-shards", required=True, type=int)
    aggregate.add_argument("--inventory", required=True)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        if args.command == "source":
            inventory = source_inventory(
                Path(args.artifact_root),
                date_folder=args.date_folder,
                expected_pdf_count=args.expected_pdf_count,
                reports_per_shard=args.reports_per_shard,
            )
            write_json(Path(args.inventory), inventory)
            if args.github_output:
                append_github_outputs(Path(args.github_output), inventory)
            print(
                "Validated chart backfill source: "
                f"date={inventory['date_folder']}, PDFs={inventory['pdf_count']}, "
                f"shards={inventory['effective_shard_count']}"
            )
        elif args.command == "shard":
            inventory = shard_inventory(
                Path(args.output_root),
                date_folder=args.date_folder,
                expected_pdf_count=args.expected_pdf_count,
                reports_per_shard=args.reports_per_shard,
                shard_index=args.shard_index,
            )
            write_json(Path(args.inventory), inventory)
            print(
                "Validated chart backfill shard: "
                f"date={inventory['date_folder']}, shard={inventory['shard_index']}, "
                f"reports={inventory['report_count']}, charts={inventory['chart_count']}"
            )
        elif args.command == "aggregate":
            inventory = aggregate_inventory(
                Path(args.inventory_root),
                date_folder=args.date_folder,
                expected_pdf_count=args.expected_pdf_count,
                expected_shards=args.expected_shards,
            )
            write_json(Path(args.inventory), inventory)
            print(
                "Validated chart backfill aggregate: "
                f"date={inventory['date_folder']}, shards={inventory['shard_count']}, "
                f"reports={inventory['report_count']}, charts={inventory['chart_count']}, "
                f"minimum={inventory['minimum_chart_count']}"
            )
        else:  # pragma: no cover
            raise ValidationError(f"Unsupported command: {args.command}")
        return 0
    except ValidationError as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
