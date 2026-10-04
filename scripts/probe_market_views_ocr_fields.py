#!/usr/bin/env python3
"""Probe explicit numeric fields on a few original pages, never a source handoff.

The whole Daily artifact is checked before any OCR. Only fixture pages are
recognized, and only the production auditor's sanitized numeric projection is
published. Private prose, PDF names, page images and incomplete receipt data are
never diagnostic outputs. This module makes no network, provider or model call.
"""
from __future__ import annotations

import argparse
import contextlib
from datetime import datetime
import hashlib
import json
import math
import os
from pathlib import Path, PurePosixPath
import re
import sys
import tempfile
from typing import Any

import fitz

import audit_market_views_ocr_receipt as audit
import extract_native_market_sources as native
from ocr_numeric_evidence import MAX_IMAGE_PIXELS, SECOND_DPI, validate_numeric_evidence


DAILY_WORKFLOW = ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
FIXTURE_BYTE_LIMIT = 65_536
MANIFEST_BYTE_LIMIT = 16_000_000
MAX_REPORT_PAGES = 10_000


class ProbeError(ValueError):
    """Only fixed, public-safe category codes cross the CLI boundary."""


def failure_summary(category: str) -> dict[str, Any]:
    return {"schema": 1, "page_probe_only": True, "complete_source_handoff": False,
            "production_acceptance": False, "success": False, "category": category,
            "provider_post_count": 0, "model_call_count": 0, "pdf_count": 0,
            "r2_source_admission_count": 0}


def positive_count(value: str) -> int:
    if not isinstance(value, str) or not re.fullmatch(r"[1-9][0-9]{0,3}", value):
        raise ProbeError("invalid_expected_articles")
    return int(value)


def validate_inputs(date_folder: str, source_run_id: str, expected_articles: int) -> None:
    if not isinstance(date_folder, str) or not re.fullmatch(r"[0-9]{6}", date_folder):
        raise ProbeError("invalid_date")
    try:
        datetime.strptime(date_folder, "%y%m%d")
    except ValueError as exc:
        raise ProbeError("invalid_date") from exc
    if not isinstance(source_run_id, str) or not re.fullmatch(r"[1-9][0-9]{0,19}", source_run_id):
        raise ProbeError("invalid_source_run")
    if type(expected_articles) is not int or not 1 <= expected_articles <= 9999:
        raise ProbeError("invalid_expected_articles")


def _json_file(path: Path, limit: int) -> tuple[bytes, Any]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > limit:
        raise ProbeError("invalid_input_file")
    raw = path.read_bytes()

    def pairs(items):
        result = {}
        for key, value in items:
            if key in result:
                raise ProbeError("duplicate_json_key")
            result[key] = value
        return result

    def constant(value):
        raise ProbeError("invalid_json_number")

    try:
        return raw, json.loads(raw, object_pairs_hook=pairs, parse_constant=constant)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise ProbeError("invalid_input_json") from exc


def verify_producer(path: Path, source_run_id: str) -> str:
    _, metadata = _json_file(Path(path), 1_000_000)
    if (not isinstance(metadata, dict) or type(metadata.get("id")) is not int
            or str(metadata["id"]) != source_run_id or metadata.get("path") != DAILY_WORKFLOW
            or metadata.get("head_branch") != "main" or metadata.get("status") != "completed"
            or metadata.get("conclusion") not in {"success", "failure"}
            or not isinstance(metadata.get("head_sha"), str)
            or not re.fullmatch(r"[a-f0-9]{40}", metadata["head_sha"])):
        raise ProbeError("original_daily_producer_not_verified")
    return metadata["head_sha"]


def read_checks(path: Path) -> list[dict[str, Any]]:
    raw, _ = _json_file(Path(path), FIXTURE_BYTE_LIMIT)
    try:
        checks = audit.read_fixtures(Path(path))
    except (ValueError, TypeError, OverflowError) as exc:
        raise ProbeError("invalid_numeric_fixtures") from exc
    if Path(path).read_bytes() != raw:
        raise ProbeError("fixtures_changed")
    if any(audit._diagnostic_number(check["expected_literal"]) is None for check in checks):
        raise ProbeError("invalid_numeric_fixtures")
    return checks


def _inventory(input_dir: Path) -> dict[str, Path]:
    if input_dir.is_symlink() or not input_dir.is_dir():
        raise ProbeError("invalid_original_directory")
    if any(path.is_symlink() for path in input_dir.rglob("*")):
        raise ProbeError("original_symlink_rejected")
    try:
        return native._original_inventory(input_dir)
    except (ValueError, OSError) as exc:
        raise ProbeError("invalid_original_inventory") from exc


def _preflight(input_dir: Path, manifest: Path, expected_articles: int,
               date_folder: str, checks: list[dict[str, Any]]) -> tuple[bytes, dict[str, Any]]:
    raw, rows = _json_file(manifest, MANIFEST_BYTE_LIMIT)
    try:
        _, bindings = native.read_manifest(manifest, expected_articles)
    except ValueError as exc:
        raise ProbeError("manifest_count_or_binding_invalid") from exc
    if manifest.read_bytes() != raw:
        raise ProbeError("manifest_changed")
    for row in rows:
        value = row.get("dropbox_path")
        if not isinstance(value, str) or "\\" in value or ".." in PurePosixPath(value).parts:
            raise ProbeError("manifest_date_mismatch")
        parts = PurePosixPath(value).parts
        if len(parts) < 4 or parts[:3] != ("/", "zip_backup", date_folder):
            raise ProbeError("manifest_date_mismatch")
    originals = _inventory(input_dir)
    if set(originals) != {row["source_pdf"] for row in bindings}:
        raise ProbeError("original_inventory_mismatch")
    sources = {}
    for binding in bindings:
        path = originals[binding["source_pdf"]]
        content = path.read_bytes()
        sha = hashlib.sha256(content).hexdigest()
        if sha != binding["content_sha256"]:
            raise ProbeError("original_hash_mismatch")
        if not content.startswith(b"%PDF-"):
            raise ProbeError("invalid_original_pdf")
        try:
            with fitz.open(stream=content, filetype="pdf") as document:
                if (document.is_encrypted or document.needs_pass or document.is_repaired
                        or not 1 <= document.page_count <= MAX_REPORT_PAGES):
                    raise ProbeError("unsupported_original_pdf")
                for page_index in range(document.page_count):
                    document.load_page(page_index)
                bounds = {number: tuple(document[number - 1].rect)
                          for number in {check["page"] for check in checks if check["source_pdf_sha256"] == sha}
                          if number <= document.page_count}
                sources.setdefault(sha, {"path": path, "page_count": document.page_count, "bounds": bounds})
        except ProbeError:
            raise
        except Exception as exc:
            raise ProbeError("damaged_original_pdf") from exc
    # Check every requested source/position before the first page reaches OCR.
    for check in checks:
        source = sources.get(check["source_pdf_sha256"])
        if source is None:
            raise ProbeError("fixture_source_missing")
        if check["page"] > source["page_count"]:
            raise ProbeError("fixture_page_out_of_bounds")
        rect = source["bounds"][check["page"]]
        box = check["expected_bbox"]
        if not rect[0] <= box[0] < box[2] <= rect[2] or not rect[1] <= box[1] < box[3] <= rect[3]:
            raise ProbeError("fixture_bbox_out_of_bounds")
        pixels = math.ceil((rect[2] - rect[0]) * SECOND_DPI / 72) * math.ceil((rect[3] - rect[1]) * SECOND_DPI / 72)
        if pixels > MAX_IMAGE_PIXELS:
            raise ProbeError("fixture_page_render_bound_exceeded")
    return raw, sources


def probe_fields(input_dir: Path, manifest: Path, fixtures: Path, producer_metadata: Path, *,
                 date_folder: str, source_run_id: str, expected_articles: int) -> dict[str, Any]:
    validate_inputs(date_folder, source_run_id, expected_articles)
    producer_raw, _ = _json_file(Path(producer_metadata), 1_000_000)
    execution_sha = verify_producer(producer_metadata, source_run_id)
    fixture_raw, _ = _json_file(Path(fixtures), FIXTURE_BYTE_LIMIT)
    checks = read_checks(fixtures)
    if Path(producer_metadata).read_bytes() != producer_raw or Path(fixtures).read_bytes() != fixture_raw:
        raise ProbeError("probe_inputs_changed")
    input_dir, manifest = Path(input_dir), Path(manifest)
    raw_manifest, sources = _preflight(input_dir, manifest, expected_articles, date_folder, checks)
    selected = sorted({(check["source_pdf_sha256"], check["page"]) for check in checks})
    # This is a private positional lookup for _fixture_matches, NOT a receipt.
    # Unprobed positions deliberately remain None. Never validate or publish it
    # as complete source coverage, and never call summarize_verified_receipt.
    lookup = {"reports": [{"content_sha256": sha, "page_count": row["page_count"],
                            "pages": [None] * row["page_count"]} for sha, row in sources.items()]}
    reports = {row["content_sha256"]: row for row in lookup["reports"]}
    with tempfile.TemporaryDirectory(prefix="market-views-field-probe-") as temporary:
        for ordinal, (sha, number) in enumerate(selected, 1):
            source = sources[sha]
            content = source["path"].read_bytes()
            if hashlib.sha256(content).hexdigest() != sha:
                raise ProbeError("original_changed")
            with fitz.open(stream=content, filetype="pdf") as document:
                page = document[number - 1]
                image = page.get_pixmap(dpi=native.PAGE_DPI, colorspace=fitz.csRGB, alpha=False)
                image_path = Path(temporary) / f"page-{ordinal}.png"
                image.save(str(image_path))
                pixel_sha = native.sha256_bytes(image.samples)
                try:
                    # Suppress engine prose; only the fixed numeric projection
                    # below is allowed into a diagnostic artifact or CLI log.
                    with open(os.devnull, "w") as silent, contextlib.redirect_stdout(silent), contextlib.redirect_stderr(silent):
                        safe_text, ocr = native._ocr_page(page, "field-probe", number)
                    native.require_readable_page(native._ocr_primary_text(ocr), "field-probe", number,
                                                 allow_sparse_ocr=True)
                    validate_numeric_evidence(safe_text, ocr.get("numeric_evidence"), pixel_sha,
                                              image_path=image_path)
                except Exception as exc:
                    raise ProbeError("page_ocr_or_numeric_validation_failed") from exc
                reports[sha]["pages"][number - 1] = {"extraction_method": "ocr", "ocr": ocr}
    # Recheck all original bytes and manifest after OCR, including unprobed PDFs.
    if manifest.read_bytes() != raw_manifest:
        raise ProbeError("manifest_changed")
    if Path(producer_metadata).read_bytes() != producer_raw or Path(fixtures).read_bytes() != fixture_raw:
        raise ProbeError("probe_inputs_changed")
    final_raw, _ = _preflight(input_dir, manifest, expected_articles, date_folder, checks)
    if final_raw != raw_manifest:
        raise ProbeError("manifest_changed")
    matches = audit._fixture_matches(lookup, checks)
    success = all(row["matched"] for row in matches)
    summary = failure_summary("passed" if success else "numeric_fixture_failed")
    summary.update(success=success, original_batch_verified=True, date_folder=date_folder,
                   source_run_id=source_run_id, original_execution_sha=execution_sha,
                   fixture_sha256=native.sha256_bytes(fixture_raw),
                   manifest_sha256=native.sha256_bytes(raw_manifest), original_file_count=expected_articles,
                   unique_original_content_count=len(sources), probed_page_count=len(selected),
                   fixture_count=len(matches), fixture_passed_count=sum(row["matched"] for row in matches),
                   fixture_acceptance="passed" if success else "failed", fixtures=matches)
    if re.fullmatch(r"[a-f0-9]{40}", os.getenv("GITHUB_SHA", "")):
        summary["probe_execution_sha"] = os.environ["GITHUB_SHA"]
    if re.fullmatch(r"[1-9][0-9]{0,19}", os.getenv("GITHUB_RUN_ID", "")):
        summary["probe_run_id"] = os.environ["GITHUB_RUN_ID"]
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--fixtures", type=Path, required=True)
    parser.add_argument("--producer-metadata", type=Path, required=True)
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--expected-articles", required=True)
    parser.add_argument("--summary", type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        summary = probe_fields(args.input_dir, args.manifest, args.fixtures, args.producer_metadata,
                               date_folder=args.date_folder, source_run_id=args.source_run_id,
                               expected_articles=positive_count(args.expected_articles))
        exit_code = 0 if summary["success"] else 3
    except ProbeError as exc:
        summary, exit_code = failure_summary(str(exc)), 2
    except Exception:
        summary, exit_code = failure_summary("probe_failed"), 2
    try:
        audit.write_summary(args.summary, summary, source_dir=args.input_dir)
    except Exception:
        print("OCR field probe rejected: diagnostic_output_invalid", file=sys.stderr)
        return 2
    print(f"OCR field probe: {summary['category']}; page_probe_only=true; production_acceptance=false")
    return exit_code


if __name__ == "__main__":
    raise SystemExit(main())
