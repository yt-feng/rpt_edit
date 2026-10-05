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
from ocr_numeric_evidence import MAX_IMAGE_PIXELS, SECOND_DPI, NumericEvidenceError, audit_numeric_evidence, validate_numeric_evidence, safe_geometry_diagnostics
from ocr_rotated_axis_evidence import RotatedAxisError, safe_rotated_axis_diagnostics


DAILY_WORKFLOW = ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
FIXTURE_BYTE_LIMIT = 65_536
MANIFEST_BYTE_LIMIT = 16_000_000
MAX_REPORT_PAGES = 10_000
MAX_DIAGNOSTIC_PAGES = 8
MAX_OPAQUE_RUNS = 512
MAX_POSITION_WORDS = 20_000
MAX_POSITION_TEXT_BYTES = 1_000_000
MAX_PRIVATE_EVIDENCE_JSON_BYTES = 8_000_000
MAX_PRIVATE_EVIDENCE_PNG_BYTES = 64_000_000
OPAQUE_POSITION_STATUSES = {"mapped", "text_order_mismatch", "word_geometry_unavailable",
                            "word_geometry_invalid", "word_bound_exceeded", "word_boundary_mismatch",
                            "duplicate_position_ambiguous", "page_geometry_unavailable", "input_bound_exceeded"}
OPAQUE_CANDIDATES = {"geometric-sorted", "source-flow", "full-page-psm11"}
READABILITY_COUNTS = ("characters", "minimum_characters", "invalid_unicode_characters", "han_characters",
                      "latin_characters", "plausible_words", "distinct_plausible_words", "plausible_word_characters",
                      "long_ascii_characters", "numeric_tokens")
READABILITY_REASONS = {"insufficient_characters", "invalid_unicode", "opaque_ascii_runs",
                       "missing_language_or_table_structure", "readable", "readable_sparse_structural_ocr"}
OCR_FAILURE_CATEGORIES = native.NUMERIC_FAILURE_CATEGORIES | native.ROTATED_AXIS_FAILURE_CATEGORIES | {
    "ocr_language_data_unavailable", "ocr_engine_failed", "page_ocr_or_numeric_validation_failed",
}


class _PrivateRecognitionDiagnostic(dict):
    """Carry producer provenance internally, outside serializable diagnostics."""

    __slots__ = ("ocr_provenance",)

    def __init__(self, counts, provenance):
        super().__init__(counts)
        self.ocr_provenance = provenance


def _axis_failure_category(error):
    return str(error) if str(error) in native.ROTATED_AXIS_FAILURE_CATEGORIES else "rotated_axis_proof_invalid"


def _rotated_axis_arguments(provenance, *, selected_route=False):
    proof_present = isinstance(provenance, dict) and "rotated_axis" in provenance
    engine = provenance.get("engine") if isinstance(provenance, dict) else None
    if not selected_route and not proof_present and engine != native.OCR_ROTATED_AXIS_ENGINE:
        return {}
    proof = provenance.get("rotated_axis") if isinstance(provenance, dict) else None
    runtime = proof.get("runtime") if isinstance(proof, dict) else None
    if (engine != native.OCR_ROTATED_AXIS_ENGINE or not isinstance(proof, dict)
            or not isinstance(runtime, dict) or runtime.get("languages") != native.OCR_LANGUAGES
            or provenance.get("languages") != native.OCR_LANGUAGES
            or native.canonical_bytes(runtime.get("traineddata")) != native.canonical_bytes(provenance.get("traineddata"))):
        raise ProbeError("rotated_axis_proof_invalid")
    return {"rotated_axis_proof": proof}


class ProbeError(ValueError):
    """Only fixed, public-safe category codes cross the CLI boundary."""

    def __init__(self, category, *, geometry_diagnostics=None, rotated_axis_diagnostics=None):
        super().__init__(category)
        self.geometry_diagnostics = safe_geometry_diagnostics(geometry_diagnostics)
        self.rotated_axis_diagnostics = safe_rotated_axis_diagnostics(rotated_axis_diagnostics)


def failure_summary(category: str, geometry_diagnostics=None, rotated_axis_diagnostics=None) -> dict[str, Any]:
    result = {"schema": 1, "page_probe_only": True, "complete_source_handoff": False,
            "production_acceptance": False, "success": False, "category": category,
            "provider_post_count": 0, "model_call_count": 0, "pdf_count": 0,
            "r2_source_admission_count": 0}
    if category == "numeric_crop_geometry_mismatch":
        safe = safe_geometry_diagnostics(geometry_diagnostics)
        if safe:
            result["geometry_diagnostics"] = safe
    rotated = safe_rotated_axis_diagnostics(rotated_axis_diagnostics)
    if rotated:
        result["rotated_axis_diagnostics"] = rotated
    return result


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


def verify_producer(path: Path, source_run_id: str, *, source_kind: str = "daily",
                    repository: str | None = None) -> str:
    _, metadata = _json_file(Path(path), 1_000_000)
    if (not isinstance(metadata, dict) or type(metadata.get("id")) is not int
            or str(metadata["id"]) != source_run_id
            or metadata.get("head_branch") != "main" or metadata.get("status") != "completed"
            or metadata.get("conclusion") not in {"success", "failure"}
            or not isinstance(metadata.get("head_sha"), str)
            or not re.fullmatch(r"[a-f0-9]{40}", metadata["head_sha"])):
        raise ProbeError("original_daily_producer_not_verified" if source_kind == "daily" else "original_archive_producer_not_verified")
    if source_kind == "daily":
        if metadata.get("path") != DAILY_WORKFLOW:
            raise ProbeError("original_daily_producer_not_verified")
    elif source_kind == "original-archive":
        if not isinstance(repository, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository):
            raise ProbeError("original_archive_producer_not_verified")
        try:
            import archive_market_views_originals as originals_archive
            originals_archive.check_restore_producer(metadata, source_run_id, repository, metadata["head_sha"])
        except (ValueError, TypeError, AttributeError):
            raise ProbeError("original_archive_producer_not_verified") from None
    else:
        raise ProbeError("invalid_source_kind")
    return metadata["head_sha"]


def read_page_checks(path: Path) -> list[dict[str, int]]:
    _, value = _json_file(Path(path), FIXTURE_BYTE_LIMIT)
    if (not isinstance(value, dict) or set(value) != {"schema", "pages"}
            or type(value.get("schema")) is not int or value["schema"] != 1
            or not isinstance(value.get("pages"), list) or not 1 <= len(value["pages"]) <= MAX_DIAGNOSTIC_PAGES):
        raise ProbeError("invalid_page_diagnostics")
    checks = value["pages"]
    for check in checks:
        if (not isinstance(check, dict) or set(check) != {"source_ordinal", "page"}
                or type(check["source_ordinal"]) is not int or not 1 <= check["source_ordinal"] <= 1000
                or type(check["page"]) is not int or not 1 <= check["page"] <= MAX_REPORT_PAGES):
            raise ProbeError("invalid_page_diagnostics")
    if len({(row["source_ordinal"], row["page"]) for row in checks}) != len(checks):
        raise ProbeError("invalid_page_diagnostics")
    return checks


def _archive_receipt(input_dir: Path, manifest: Path, *, source_run_id: str, date_folder: str,
                     execution_sha: str, expected_articles: int, original_source_run_id: str) -> bytes:
    import archive_market_views_originals as originals_archive
    path = input_dir / originals_archive.RECEIPT
    raw, value = _json_file(path, originals_archive.MAX_RECEIPT)
    try:
        expected = originals_archive.context(source_run_id, date_folder, execution_sha, original_source_run_id)
        originals_archive.checked_receipt(value, expected, expected_articles)
        manifest_raw, bindings, _ = originals_archive.checked_inputs(input_dir, expected_articles, date_folder)
        if (manifest.resolve() != (input_dir / originals_archive.MANIFEST).resolve()
                or value["manifest_sha256"] != native.sha256_bytes(manifest_raw)
                or value["original_inventory"] != bindings):
            raise ValueError("binding")
    except (ValueError, TypeError, KeyError, OSError):
        raise ProbeError("original_archive_receipt_not_verified") from None
    if path.read_bytes() != raw:
        raise ProbeError("probe_inputs_changed")
    return raw


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
               date_folder: str, checks: list[dict[str, Any]], *,
               page_checks: list[dict[str, int]] | None = None) -> tuple[bytes, dict[str, Any]]:
    raw, rows = _json_file(manifest, MANIFEST_BYTE_LIMIT)
    try:
        _, bindings = native.read_manifest(manifest, expected_articles)
    except ValueError as exc:
        raise ProbeError("manifest_count_or_binding_invalid") from exc
    if manifest.read_bytes() != raw:
        raise ProbeError("manifest_changed")
    requested_pages = []
    for check in page_checks or []:
        if check["source_ordinal"] > len(bindings):
            raise ProbeError("diagnostic_source_ordinal_out_of_bounds")
        requested_pages.append({"source_pdf_sha256": bindings[check["source_ordinal"] - 1]["content_sha256"],
                                "page": check["page"]})
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
                          for number in {check["page"] for check in checks + requested_pages if check["source_pdf_sha256"] == sha}
                          if number <= document.page_count}
                sources.setdefault(sha, {"path": path, "page_count": document.page_count, "bounds": bounds})
        except ProbeError:
            raise
        except Exception as exc:
            raise ProbeError("damaged_original_pdf") from exc
    # Check every requested source/position before the first page reaches OCR.
    for check in checks + requested_pages:
        source = sources.get(check["source_pdf_sha256"])
        if source is None:
            raise ProbeError("fixture_source_missing")
        if check["page"] > source["page_count"]:
            raise ProbeError("fixture_page_out_of_bounds")
        rect = source["bounds"][check["page"]]
        if "expected_bbox" in check:
            box = check["expected_bbox"]
            if not rect[0] <= box[0] < box[2] <= rect[2] or not rect[1] <= box[1] < box[3] <= rect[3]:
                raise ProbeError("fixture_bbox_out_of_bounds")
        pixels = math.ceil((rect[2] - rect[0]) * SECOND_DPI / 72) * math.ceil((rect[3] - rect[1]) * SECOND_DPI / 72)
        if pixels > MAX_IMAGE_PIXELS:
            raise ProbeError("fixture_page_render_bound_exceeded")
    return raw, sources


def probe_fields(input_dir: Path, manifest: Path, fixtures: Path, producer_metadata: Path, *,
                 date_folder: str, source_run_id: str, expected_articles: int,
                 source_kind: str = "daily", repository: str | None = None,
                 original_source_run_id: str = "") -> dict[str, Any]:
    validate_inputs(date_folder, source_run_id, expected_articles)
    producer_raw, _ = _json_file(Path(producer_metadata), 1_000_000)
    execution_sha = verify_producer(producer_metadata, source_run_id, source_kind=source_kind, repository=repository)
    fixture_raw, _ = _json_file(Path(fixtures), FIXTURE_BYTE_LIMIT)
    checks = read_checks(fixtures)
    if Path(producer_metadata).read_bytes() != producer_raw or Path(fixtures).read_bytes() != fixture_raw:
        raise ProbeError("probe_inputs_changed")
    input_dir, manifest = Path(input_dir), Path(manifest)
    raw_manifest, sources = _preflight(input_dir, manifest, expected_articles, date_folder, checks)
    archive_raw = None
    if source_kind == "original-archive":
        archive_raw = _archive_receipt(input_dir, manifest, source_run_id=source_run_id, date_folder=date_folder,
                                       execution_sha=execution_sha, expected_articles=expected_articles,
                                       original_source_run_id=original_source_run_id)
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
                    axis_arguments = _rotated_axis_arguments(ocr)
                    validate_numeric_evidence(safe_text, ocr.get("numeric_evidence"), pixel_sha,
                                              image_path=image_path, **axis_arguments)
                except native.SourceValidationError as exc:
                    category = getattr(exc, "category", None)
                    if isinstance(category, str) and category in OCR_FAILURE_CATEGORIES:
                        raise ProbeError(category, geometry_diagnostics=safe_geometry_diagnostics(exc),
                                         rotated_axis_diagnostics=exc.rotated_axis_diagnostics) from None
                    raise ProbeError("page_ocr_or_numeric_validation_failed",
                                     rotated_axis_diagnostics=exc.rotated_axis_diagnostics) from None
                except NumericEvidenceError as exc:
                    raise ProbeError(native._numeric_failure_category(exc),
                                     geometry_diagnostics=safe_geometry_diagnostics(exc)) from None
                except RotatedAxisError as exc:
                    raise ProbeError(_axis_failure_category(exc)) from None
                except ProbeError:
                    raise
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
    if archive_raw is not None and _archive_receipt(input_dir, manifest, source_run_id=source_run_id,
            date_folder=date_folder, execution_sha=execution_sha, expected_articles=expected_articles,
            original_source_run_id=original_source_run_id) != archive_raw:
        raise ProbeError("probe_inputs_changed")
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
    if source_kind == "original-archive":
        summary["source_kind"] = source_kind
    if re.fullmatch(r"[a-f0-9]{40}", os.getenv("GITHUB_SHA", "")):
        summary["probe_execution_sha"] = os.environ["GITHUB_SHA"]
    if re.fullmatch(r"[1-9][0-9]{0,19}", os.getenv("GITHUB_RUN_ID", "")):
        summary["probe_run_id"] = os.environ["GITHUB_RUN_ID"]
    return summary


def _safe_readability(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}
    output = {key: value[key] for key in READABILITY_COUNTS
              if type(value.get(key)) is int and 0 <= value[key] <= 10_000_000}
    if type(value.get("accepted")) is bool:
        output["accepted"] = value["accepted"]
    if isinstance(value.get("reason"), str) and value["reason"] in READABILITY_REASONS:
        output["reason"] = value["reason"]
    return output


def _readability_projection(text: str, *, allow_sparse_ocr: bool = False) -> dict[str, Any]:
    return _safe_readability(native.page_readability(text, allow_sparse_ocr=allow_sparse_ocr))


def _finite_coordinate(value: Any) -> bool:
    if type(value) not in (int, float):
        return False
    try:
        return math.isfinite(value)
    except OverflowError:
        return False


def _page_bounds(rect: Any) -> list[float] | None:
    try:
        values = list(rect)
        if (len(values) != 4 or any(not _finite_coordinate(value) for value in values)
                or values[2] <= values[0] or values[3] <= values[1]):
            return None
        return values
    except (TypeError, ValueError):
        return None


def _opaque_run_positions(text: Any, words: Any, rect: Any) -> dict[str, Any]:
    """Map exact non-whitespace character offsets, never search duplicate words."""
    result = {"status": "input_bound_exceeded", "counts_available": False, "run_count": 0,
              "long_ascii_characters": 0, "returned_run_count": 0, "mapped_run_count": 0,
              "truncated": True, "runs": []}
    if not isinstance(text, str) or len(text.encode("utf-8")) > MAX_POSITION_TEXT_BYTES:
        return result
    # Each run is already contiguous ASCII. Offsets count all other source
    # glyphs too, so punctuation/order changes cannot borrow a nearby word.
    positions, previous, offset, total, characters = [], 0, 0, 0, 0
    seen_runs, duplicate_runs = set(), False
    for match in native.LONG_ASCII_RUN.finditer(text):
        offset += sum(not character.isspace() for character in text[previous:match.start()])
        length = match.end() - match.start()
        if len(positions) < MAX_OPAQUE_RUNS:
            positions.append((offset, offset + length, length))
        offset += length
        previous = match.end()
        total += 1
        characters += length
        value = match.group()
        duplicate_runs = duplicate_runs or value in seen_runs
        seen_runs.add(value)
    result.update(counts_available=True, run_count=total, long_ascii_characters=characters,
                  returned_run_count=len(positions), truncated=total > len(positions))
    bounds = _page_bounds(rect)
    status = "page_geometry_unavailable" if bounds is None else "word_geometry_unavailable"
    if isinstance(words, (list, tuple)) and len(words) > MAX_POSITION_WORDS:
        status = "word_bound_exceeded"
    spans, parts, size, stream_bytes = [], [], 0, 0
    if bounds is not None and isinstance(words, (list, tuple)) and len(words) <= MAX_POSITION_WORDS:
        status = "word_geometry_invalid"
        for word in words:
            box, value = (word.get("bbox"), word.get("text")) if isinstance(word, dict) else (
                (list(word[:4]), word[4]) if isinstance(word, (list, tuple)) and len(word) >= 5 else (None, None))
            if (not isinstance(box, list) or len(box) != 4
                    or any(not _finite_coordinate(number) for number in box)
                    or not bounds[0] <= box[0] < box[2] <= bounds[2]
                    or not bounds[1] <= box[1] < box[3] <= bounds[3]
                    or not isinstance(value, str) or not value):
                break
            stream_bytes += len(value.encode("utf-8"))
            if stream_bytes > MAX_POSITION_TEXT_BYTES:
                break
            glyphs = "".join(character for character in value if not character.isspace())
            spans.append((size, size + len(glyphs), box))
            parts.append(glyphs)
            size += len(glyphs)
        else:
            target = "".join(character for character in text if not character.isspace())
            status = "mapped" if "".join(parts) == target else "text_order_mismatch"
            # Repeated identical glyphs can conceal a moved word boundary.
            # A run may cover many whole OCR words, or part of one word next
            # to punctuation, but cannot invent a break inside its ASCII run.
            if status == "mapped" and any(
                    start < begin < finish and target[begin - 1].isascii() and target[begin - 1].isalnum()
                    or start < end < finish and target[end].isascii() and target[end].isalnum()
                    for begin, end, _ in positions for start, finish, _ in spans):
                status = "word_boundary_mismatch"
            # Exact duplicate runs can swap whole word groups without changing
            # the flattened glyphs or boundaries. This diagnostic has no proof
            # of their individual occurrence, so retain counts without boxes.
            if status == "mapped" and duplicate_runs:
                status = "duplicate_position_ambiguous"
    result["status"] = status
    for index, (begin, end, length) in enumerate(positions, 1):
        covering = [box for start, finish, box in spans if start < end and finish > begin] if status == "mapped" else []
        box = ([min(box[0] for box in covering), min(box[1] for box in covering),
                max(box[2] for box in covering), max(box[3] for box in covering)] if covering else None)
        result["runs"].append({"run": index, "characters": length,
                               "bbox": [min(bounds[axis % 2 + 2], max(bounds[axis % 2], round(number, 4)))
                                        for axis, number in enumerate(box)] if box is not None else None,
                               "source_word_count": len(covering)})
    result["mapped_run_count"] = sum(run["bbox"] is not None for run in result["runs"])
    return result


def _safe_opaque_positions(value: Any, rect: Any) -> dict[str, Any] | None:
    """Project only bounded typed coordinates/counts; never copy engine text."""
    bounds = _page_bounds(rect)
    if (not isinstance(value, dict) or not isinstance(value.get("status"), str)
            or value["status"] not in OPAQUE_POSITION_STATUSES
            or any(type(value.get(key)) is not bool for key in ("counts_available", "truncated"))
            or any(type(value.get(key)) is not int or not 0 <= value[key] <= MAX_POSITION_TEXT_BYTES
                   for key in ("run_count", "long_ascii_characters", "returned_run_count", "mapped_run_count"))
            or not isinstance(value.get("runs"), list) or len(value["runs"]) > MAX_OPAQUE_RUNS
            or value["returned_run_count"] != len(value["runs"])
            or value["run_count"] < len(value["runs"])):
        return None
    runs = []
    for index, run in enumerate(value["runs"], 1):
        if (not isinstance(run, dict) or type(run.get("run")) is not int or run["run"] != index
                or type(run.get("characters")) is not int or not 25 <= run["characters"] <= MAX_POSITION_TEXT_BYTES
                or type(run.get("source_word_count")) is not int or not 0 <= run["source_word_count"] <= MAX_POSITION_WORDS):
            return None
        box = run.get("bbox")
        if box is not None:
            if (bounds is None or not isinstance(box, list) or len(box) != 4
                    or any(not _finite_coordinate(number) for number in box)
                    or not bounds[0] <= box[0] < box[2] <= bounds[2]
                    or not bounds[1] <= box[1] < box[3] <= bounds[3] or run["source_word_count"] < 1):
                return None
        elif run["source_word_count"] != 0:
            return None
        runs.append({"run": index, "characters": run["characters"], "bbox": box,
                     "source_word_count": run["source_word_count"]})
    if (value["mapped_run_count"] != sum(run["bbox"] is not None for run in runs)
            or sum(run["characters"] for run in runs) > value["long_ascii_characters"]
            or value["counts_available"] and value["truncated"] != (value["run_count"] > len(runs))):
        return None
    if (value["status"] == "mapped" and value["mapped_run_count"] != len(runs)
            or value["status"] != "mapped" and value["mapped_run_count"] != 0
            or not value["counts_available"] and (value["status"] != "input_bound_exceeded"
                or value["run_count"] or value["long_ascii_characters"] or runs or not value["truncated"])):
        return None
    return {**{key: value[key] for key in ("status", "counts_available", "run_count", "long_ascii_characters",
                                         "returned_run_count", "mapped_run_count", "truncated")}, "runs": runs}


class _ObservedOCRPage:
    """Expose the same page; retain the one existing OCR TextPage privately."""
    def __init__(self, page):
        self.page, self.textpage, self.texts = page, None, {}

    def __getattr__(self, name):
        return getattr(self.page, name)

    def get_textpage_ocr(self, **options):
        self.textpage = self.page.get_textpage_ocr(**options)
        return self.textpage

    def get_text(self, kind, *args, **options):
        value = self.page.get_text(kind, *args, **options)
        if (kind == "text" and options.get("textpage") is self.textpage
                and type(options.get("sort")) is bool and isinstance(value, str)):
            self.texts[options["sort"]] = value.strip()
        return value


def _raw_page_ocr(page: fitz.Page, *, private_evidence=None) -> tuple[str, list[Any], str, dict[str, Any]]:
    """Use the production full-page engine parameters without admitting sources."""
    observed = _ObservedOCRPage(page)
    try:
        trace_arguments = ({"private_region_trace": private_evidence}
                           if private_evidence is not None else {})
        primary, words, tessdata, provenance, diagnostic = native._recognize_ocr_page(observed, "page-probe", 1,
                                                                           allow_rejected=True, **trace_arguments)
    except native.SourceValidationError as exc:
        category = getattr(exc, "category", None)
        raise ProbeError(category if isinstance(category, str) and category in OCR_FAILURE_CATEGORIES
                         else "page_ocr_or_numeric_validation_failed") from None
    except Exception:
        raise ProbeError("ocr_engine_failed") from None
    if private_evidence is not None:
        # Reuse the existing TextPage and returned alternate/proof candidates.
        # Collecting this private diagnostic never starts another recognition.
        try:
            rotated = provenance.get("rotated_axis") if isinstance(provenance, dict) else None
            retained = rotated.get("candidates") if isinstance(rotated, dict) else None
            candidates = retained if isinstance(retained, dict) else {
                label: {"text": observed.texts[sort], "words": page.get_text("words", textpage=observed.textpage, sort=sort)}
                for sort, label in ((True, "geometric-sorted"), (False, "source-flow")) if sort in observed.texts}
            if not isinstance(retained, dict) and isinstance(provenance.get("recognition"), dict):
                candidates["full-page-psm11"] = {"text": primary, "words": words}
            private_evidence.update(candidates=candidates, provenance=provenance, diagnostic=dict(diagnostic))
        except Exception:
            # Keep any native snapshot and completed regional reads already
            # retained before a later failure; the private writer still bounds
            # and validates the complete payload before writing either file.
            pass
    _rotated_axis_arguments(provenance, selected_route=diagnostic.get("selection") == "rotated-axis")
    opaque = {}
    rect = getattr(page, "rect", None)
    rotated = provenance.get("rotated_axis") if isinstance(provenance, dict) else None
    retained = rotated.get("candidates") if isinstance(rotated, dict) else None
    for sort, label, assessment in ((True, "geometric-sorted", "sorted_readability"),
                                    (False, "source-flow", "source_flow_readability")):
        candidate = retained.get(label) if isinstance(retained, dict) else None
        if isinstance(candidate, dict) and diagnostic.get(assessment, {}).get("accepted") is False:
            opaque[label] = _opaque_run_positions(candidate.get("text"), candidate.get("words"), rect)
        elif sort in observed.texts and diagnostic.get(assessment, {}).get("accepted") is False:
            try:
                positioned = page.get_text("words", textpage=observed.textpage, sort=sort) if _page_bounds(rect) else None
            except Exception:
                positioned = None
            opaque[label] = _opaque_run_positions(observed.texts[sort], positioned, rect)
    if diagnostic.get("alternate_readability", {}).get("accepted") is False:
        candidate = retained.get("full-page-psm11") if isinstance(retained, dict) else None
        opaque["full-page-psm11"] = _opaque_run_positions(
            candidate.get("text") if isinstance(candidate, dict) else primary,
            candidate.get("words") if isinstance(candidate, dict) else words, rect)
    if opaque:
        diagnostic = {**diagnostic, "opaque_runs": opaque}
    return primary, words, tessdata, _PrivateRecognitionDiagnostic(diagnostic, provenance)


def _diagnose_page(page: fitz.Page, image_path: Path, *, private_evidence=None) -> dict[str, Any]:
    """Publish only counts; a language rejection still retains its actual reason."""
    result = {"native_readability": _readability_projection(page.get_text("text", sort=True).strip()),
              "ocr_attempted": True, "numeric_audit_performed": False}
    try:
        with open(os.devnull, "w") as silent, contextlib.redirect_stdout(silent), contextlib.redirect_stderr(silent):
            primary, words, tessdata, layout = (_raw_page_ocr(page) if private_evidence is None
                else _raw_page_ocr(page, private_evidence=private_evidence))
            result["ocr_readability"] = _readability_projection(primary, allow_sparse_ocr=True)
            if (isinstance(layout, dict) and isinstance(layout.get("selection"), str)
                    and layout["selection"] in {"geometric-sorted", "source-flow", "full-page-psm11", "rotated-axis", "rejected"}):
                result["ocr_layout"] = {"selection": layout["selection"],
                    "sorted_readability": _safe_readability(layout.get("sorted_readability")),
                    "selected_readability": dict(result["ocr_readability"])}
                for key in ("source_flow_readability", "alternate_readability", "rotated_axis_readability"):
                    if key in layout:
                        result["ocr_layout"][key] = _safe_readability(layout[key])
                for key in ("source_flow_same_glyphs", "recognition_attempted", "rotated_axis_attempted"):
                    if type(layout.get(key)) is bool:
                        result["ocr_layout"][key] = layout[key]
                rotated = safe_rotated_axis_diagnostics(layout.get("rotated_axis_diagnostics"))
                if rotated:
                    result["ocr_layout"]["rotated_axis_diagnostics"] = rotated
                if isinstance(layout.get("opaque_runs"), dict):
                    projected = {candidate: _safe_opaque_positions(value, page.rect)
                                 for candidate, value in layout["opaque_runs"].items() if candidate in OPAQUE_CANDIDATES}
                    result["ocr_layout"]["opaque_runs"] = {key: value for key, value in projected.items() if value is not None}
            if not result["ocr_readability"].get("accepted"):
                result["category"] = "ocr_readability_rejected"
                return result
            # Keep the exact production language gate and numeric consensus;
            # ordinal selectors never replace expected-value acceptance fixtures.
            native.require_readable_page(primary, "page-probe", 1, allow_sparse_ocr=True)
            result["numeric_audit_performed"] = True
            provenance = getattr(layout, "ocr_provenance", None)
            axis_arguments = _rotated_axis_arguments(provenance, selected_route=layout.get("selection") == "rotated-axis")
            numeric = audit_numeric_evidence(page, primary, primary_words=words,
                                            language=native.OCR_LANGUAGES, tessdata=tessdata, **axis_arguments)
            image = fitz.Pixmap(str(image_path))
            validate_numeric_evidence(numeric["safe_text"], numeric["evidence"], native.sha256_bytes(image.samples),
                                      image_path=image_path, **axis_arguments)
    except ProbeError as exc:
        result["category"] = str(exc) if str(exc) in OCR_FAILURE_CATEGORIES else "page_ocr_or_numeric_validation_failed"
        return result
    except NumericEvidenceError as exc:
        result["category"] = native._numeric_failure_category(exc)
        if result["category"] == "numeric_crop_geometry_mismatch":
            diagnostic = safe_geometry_diagnostics(exc)
            if diagnostic:
                result["geometry_diagnostics"] = diagnostic
        return result
    except RotatedAxisError as exc:
        result["category"] = _axis_failure_category(exc)
        return result
    except Exception:
        result["category"] = "page_ocr_or_numeric_validation_failed"
        return result
    evidence = numeric["evidence"]
    result["numeric_counts"] = {key: evidence[key] for key in
        ("source_num_count", "verified_count", "corrected_count", "unresolved_count", "secondary_only_count", "observed_num_count")
        if type(evidence.get(key)) is int and 0 <= evidence[key] <= 100_000}
    result["category"] = "page_checks_completed"
    return result


def _write_private_evidence(destination: Path, payload: dict[str, Any], png: bytes) -> dict[str, Any]:
    """Two private diagnostic files; never the source-handoff receipt layout."""
    raw = native.canonical_bytes(payload)
    provenance = payload.get("recognition", {}).get("provenance", {})
    models = provenance.get("traineddata", [])
    if (len(raw) > MAX_PRIVATE_EVIDENCE_JSON_BYTES or not 0 < len(png) <= MAX_PRIVATE_EVIDENCE_PNG_BYTES
            or not isinstance(payload.get("recognition", {}).get("candidates"), dict)
            or not 1 <= len(payload["recognition"]["candidates"]) <= 3
            or provenance.get("engine") not in {"tesseract-via-pymupdf", "tesseract-cli", native.OCR_ROTATED_AXIS_ENGINE}
            or not isinstance(models, list) or not models
            or any(not isinstance(model, dict) or not isinstance(model.get("sha256"), str)
                   or not re.fullmatch(r"[a-f0-9]{64}", model["sha256"]) for model in models)):
        raise ProbeError("private_evidence_unavailable")
    if destination.exists() or destination.is_symlink():
        raise ProbeError("private_evidence_destination_invalid")
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(prefix=".ocr-probe-evidence-", dir=destination.parent) as temporary:
        root = Path(temporary)
        for name, content in (("ocr-evidence.json", raw), ("page.png", png)):
            path = root / name
            path.write_bytes(content)
            path.chmod(0o600)
        os.replace(root, destination)
    return {"status": "ready", "file_count": 2, "candidate_count": len(payload["recognition"]["candidates"]),
            "evidence_json_sha256": native.sha256_bytes(raw), "page_png_sha256": native.sha256_bytes(png)}


def probe_pages(input_dir: Path, manifest: Path, page_checks: Path, producer_metadata: Path, *,
                date_folder: str, source_run_id: str, expected_articles: int,
                source_kind: str, repository: str, original_source_run_id: str = "",
                private_evidence_dir: Path | None = None) -> dict[str, Any]:
    if source_kind != "original-archive":
        raise ProbeError("page_diagnostics_require_original_archive")
    validate_inputs(date_folder, source_run_id, expected_articles)
    producer_raw, _ = _json_file(Path(producer_metadata), 1_000_000)
    execution_sha = verify_producer(producer_metadata, source_run_id, source_kind=source_kind, repository=repository)
    request_raw, _ = _json_file(Path(page_checks), FIXTURE_BYTE_LIMIT)
    requests = read_page_checks(page_checks)
    if private_evidence_dir is not None:
        private_evidence_dir = Path(private_evidence_dir)
        if len(requests) != 1:
            raise ProbeError("private_evidence_requires_single_page")
        if (not re.fullmatch(r"[1-9][0-9]*", os.getenv("GITHUB_RUN_ID", ""))
                or not re.fullmatch(r"[a-f0-9]{40}", os.getenv("GITHUB_SHA", ""))):
            raise ProbeError("private_evidence_context_invalid")
        if (private_evidence_dir.exists() or private_evidence_dir.is_symlink()
                or Path(input_dir).resolve() == private_evidence_dir.resolve()
                or Path(input_dir).resolve() in private_evidence_dir.resolve().parents):
            raise ProbeError("private_evidence_destination_invalid")
    input_dir, manifest = Path(input_dir), Path(manifest)
    raw_manifest, sources = _preflight(input_dir, manifest, expected_articles, date_folder, [], page_checks=requests)
    archive_raw = _archive_receipt(input_dir, manifest, source_run_id=source_run_id, date_folder=date_folder,
                                   execution_sha=execution_sha, expected_articles=expected_articles,
                                   original_source_run_id=original_source_run_id)
    if Path(producer_metadata).read_bytes() != producer_raw or Path(page_checks).read_bytes() != request_raw:
        raise ProbeError("probe_inputs_changed")
    rows = json.loads(raw_manifest)
    results, private_payload, private_png = [], None, None
    with tempfile.TemporaryDirectory(prefix="market-views-page-probe-") as temporary:
        for ordinal, request in enumerate(requests, 1):
            sha = rows[request["source_ordinal"] - 1]["content_sha256"]
            content = sources[sha]["path"].read_bytes()
            if native.sha256_bytes(content) != sha:
                raise ProbeError("original_changed")
            with fitz.open(stream=content, filetype="pdf") as document:
                page = document[request["page"] - 1]
                image_path = Path(temporary) / f"page-{ordinal}.png"
                page.get_pixmap(dpi=native.PAGE_DPI, colorspace=fitz.csRGB, alpha=False).save(str(image_path))
                recognition = {} if private_evidence_dir is not None else None
                result = (_diagnose_page(page, image_path) if recognition is None
                          else _diagnose_page(page, image_path, private_evidence=recognition))
                results.append({**request, "source_pdf_sha256": sha, **result})
                if recognition is not None:
                    private_png = image_path.read_bytes()
                    pixels = fitz.Pixmap(str(image_path))
                    private_payload = {"schema": 1, "kind": "market-views-ocr-probe-evidence",
                        "diagnostic_only": True, "complete_source_handoff": False, "source_admission": False,
                        "source_context": {"source_kind": source_kind, "source_run_id": source_run_id,
                            "original_source_run_id": original_source_run_id, "source_execution_sha": execution_sha,
                            "date_folder": date_folder, "manifest_sha256": native.sha256_bytes(raw_manifest),
                            "probe_run_id": os.environ["GITHUB_RUN_ID"], "probe_execution_sha": os.environ["GITHUB_SHA"]},
                        "source_pdf_sha256": sha, **request,
                        "page_size_points": [float(page.rect.width), float(page.rect.height)],
                        "image_size": [pixels.width, pixels.height], "render_dpi": native.PAGE_DPI,
                        "page_png_sha256": native.sha256_bytes(private_png), "pixel_sha256": native.sha256_bytes(pixels.samples),
                        "recognition": recognition, "result": result}
    if Path(producer_metadata).read_bytes() != producer_raw or Path(page_checks).read_bytes() != request_raw:
        raise ProbeError("probe_inputs_changed")
    final_raw, _ = _preflight(input_dir, manifest, expected_articles, date_folder, [], page_checks=requests)
    if final_raw != raw_manifest:
        raise ProbeError("manifest_changed")
    if _archive_receipt(input_dir, manifest, source_run_id=source_run_id, date_folder=date_folder,
            execution_sha=execution_sha, expected_articles=expected_articles,
            original_source_run_id=original_source_run_id) != archive_raw:
        raise ProbeError("probe_inputs_changed")
    success = all(result["category"] == "page_checks_completed" for result in results)
    summary = failure_summary("page_checks_completed" if success else "page_probe_failed")
    summary.update(success=success, diagnostic_complete=True, page_diagnostic_only=True,
                   source_kind=source_kind, original_batch_verified=True, date_folder=date_folder,
                   source_run_id=source_run_id, original_execution_sha=execution_sha,
                   manifest_sha256=native.sha256_bytes(raw_manifest), original_file_count=expected_articles,
                   unique_original_content_count=len(sources), probed_page_count=len(results),
                   request_sha256=native.sha256_bytes(request_raw), fixture_acceptance="not_requested", pages=results)
    if private_evidence_dir is not None:
        try:
            summary["private_evidence"] = _write_private_evidence(private_evidence_dir, private_payload, private_png)
        except Exception:
            # Evidence retention must not promote or replace the page result.
            summary["private_evidence"] = {"status": "unavailable", "file_count": 0, "candidate_count": 0}
    return summary


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--input-dir", type=Path, required=True)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--fixtures", type=Path)
    parser.add_argument("--page-checks", type=Path)
    parser.add_argument("--source-kind", choices=("daily", "original-archive"), default="daily")
    parser.add_argument("--repository")
    parser.add_argument("--original-source-run-id", default="")
    parser.add_argument("--producer-metadata", type=Path, required=True)
    parser.add_argument("--source-run-id", required=True)
    parser.add_argument("--date-folder", required=True)
    parser.add_argument("--expected-articles", required=True)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--private-evidence-dir", type=Path)
    args = parser.parse_args(argv)
    try:
        if (args.fixtures is None) == (args.page_checks is None):
            raise ProbeError("exactly_one_probe_request_required")
        if args.private_evidence_dir is not None and (args.page_checks is None or args.source_kind != "original-archive"):
            raise ProbeError("private_evidence_requires_single_archive_page")
        if args.private_evidence_dir is not None and (args.private_evidence_dir.resolve() == args.summary.resolve()
                or args.private_evidence_dir.resolve() in args.summary.resolve().parents):
            raise ProbeError("private_evidence_destination_invalid")
        if args.page_checks is not None:
            summary = probe_pages(args.input_dir, args.manifest, args.page_checks, args.producer_metadata,
                                  date_folder=args.date_folder, source_run_id=args.source_run_id,
                                  expected_articles=positive_count(args.expected_articles), source_kind=args.source_kind,
                                  repository=args.repository, original_source_run_id=args.original_source_run_id,
                                  private_evidence_dir=args.private_evidence_dir)
        else:
            summary = probe_fields(args.input_dir, args.manifest, args.fixtures, args.producer_metadata,
                                   date_folder=args.date_folder, source_run_id=args.source_run_id,
                                   expected_articles=positive_count(args.expected_articles), source_kind=args.source_kind,
                                   repository=args.repository, original_source_run_id=args.original_source_run_id)
        exit_code = 0 if summary["success"] else 3
    except ProbeError as exc:
        summary, exit_code = failure_summary(str(exc), exc.geometry_diagnostics, exc.rotated_axis_diagnostics), 2
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
