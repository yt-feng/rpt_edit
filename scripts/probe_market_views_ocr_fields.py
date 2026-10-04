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


DAILY_WORKFLOW = ".github/workflows/dropbox-latest-pdf-to-xhs-sharded.yml"
FIXTURE_BYTE_LIMIT = 65_536
MANIFEST_BYTE_LIMIT = 16_000_000
MAX_REPORT_PAGES = 10_000
MAX_DIAGNOSTIC_PAGES = 8
READABILITY_COUNTS = ("characters", "minimum_characters", "invalid_unicode_characters", "han_characters",
                      "latin_characters", "plausible_words", "distinct_plausible_words", "plausible_word_characters",
                      "long_ascii_characters", "numeric_tokens")
READABILITY_REASONS = {"insufficient_characters", "invalid_unicode", "opaque_ascii_runs",
                       "missing_language_or_table_structure", "readable", "readable_sparse_structural_ocr"}


class ProbeError(ValueError):
    """Only fixed, public-safe category codes cross the CLI boundary."""

    def __init__(self, category, *, geometry_diagnostics=None):
        super().__init__(category)
        self.geometry_diagnostics = safe_geometry_diagnostics(geometry_diagnostics)


def failure_summary(category: str, geometry_diagnostics=None) -> dict[str, Any]:
    result = {"schema": 1, "page_probe_only": True, "complete_source_handoff": False,
            "production_acceptance": False, "success": False, "category": category,
            "provider_post_count": 0, "model_call_count": 0, "pdf_count": 0,
            "r2_source_admission_count": 0}
    if category == "numeric_crop_geometry_mismatch":
        safe = safe_geometry_diagnostics(geometry_diagnostics)
        if safe:
            result["geometry_diagnostics"] = safe
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
                    validate_numeric_evidence(safe_text, ocr.get("numeric_evidence"), pixel_sha,
                                              image_path=image_path)
                except native.SourceValidationError as exc:
                    category = getattr(exc, "category", None)
                    allowed = native.NUMERIC_FAILURE_CATEGORIES | {"ocr_language_data_unavailable", "ocr_engine_failed"}
                    if isinstance(category, str) and category in allowed:
                        raise ProbeError(category, geometry_diagnostics=safe_geometry_diagnostics(exc)) from None
                    raise ProbeError("page_ocr_or_numeric_validation_failed") from None
                except NumericEvidenceError as exc:
                    raise ProbeError(native._numeric_failure_category(exc),
                                     geometry_diagnostics=safe_geometry_diagnostics(exc)) from None
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


def _raw_page_ocr(page: fitz.Page) -> tuple[str, list[Any], str, dict[str, Any]]:
    """Use the production full-page engine parameters without admitting sources."""
    try:
        tessdata = Path(fitz.get_tessdata())
        if not all((tessdata / f"{language}.traineddata").is_file() for language in native.OCR_LANGUAGES.split("+")):
            raise ValueError("models")
    except Exception:
        raise ProbeError("ocr_language_data_unavailable") from None
    try:
        textpage = page.get_textpage_ocr(language=native.OCR_LANGUAGES, dpi=native.PAGE_DPI,
                                       full=True, tessdata=str(tessdata))
        sorted_text = page.get_text("text", textpage=textpage, sort=True).strip()
    except Exception:
        raise ProbeError("ocr_engine_failed") from None
    selection = "geometric-sorted"
    try:
        primary, selected_sort, _ = native._select_ocr_text_layout(page, textpage, sorted_text, "page-probe", 1)
        if not selected_sort:
            selection = "source-flow"
    except native.SourceValidationError as exc:
        if getattr(exc, "category", None) == "ocr_engine_failed":
            raise ProbeError("ocr_engine_failed") from None
        # Preserve the real rejected default's counts. This instrument does
        # not turn a rejected layout into an admitted source transcript.
        primary, selected_sort, selection = sorted_text, True, "rejected"
    try:
        words = page.get_text("words", textpage=textpage, sort=selected_sort)
    except Exception:
        raise ProbeError("ocr_engine_failed") from None
    layout = {"selection": selection, "sorted_readability": _readability_projection(sorted_text, allow_sparse_ocr=True)}
    return primary, words, str(tessdata), layout


def _diagnose_page(page: fitz.Page, image_path: Path) -> dict[str, Any]:
    """Publish only counts; a language rejection still retains its actual reason."""
    result = {"native_readability": _readability_projection(page.get_text("text", sort=True).strip()),
              "ocr_attempted": True, "numeric_audit_performed": False}
    try:
        with open(os.devnull, "w") as silent, contextlib.redirect_stdout(silent), contextlib.redirect_stderr(silent):
            primary, words, tessdata, layout = _raw_page_ocr(page)
            result["ocr_readability"] = _readability_projection(primary, allow_sparse_ocr=True)
            if (isinstance(layout, dict) and isinstance(layout.get("selection"), str)
                    and layout["selection"] in {"geometric-sorted", "source-flow", "rejected"}):
                result["ocr_layout"] = {"selection": layout["selection"],
                    "sorted_readability": _safe_readability(layout.get("sorted_readability")),
                    "selected_readability": dict(result["ocr_readability"])}
            if not result["ocr_readability"].get("accepted"):
                result["category"] = "ocr_readability_rejected"
                return result
            # Keep the exact production language gate and numeric consensus;
            # ordinal selectors never replace expected-value acceptance fixtures.
            native.require_readable_page(primary, "page-probe", 1, allow_sparse_ocr=True)
            result["numeric_audit_performed"] = True
            numeric = audit_numeric_evidence(page, primary, primary_words=words,
                                            language=native.OCR_LANGUAGES, tessdata=tessdata)
            image = fitz.Pixmap(str(image_path))
            validate_numeric_evidence(numeric["safe_text"], numeric["evidence"], native.sha256_bytes(image.samples),
                                      image_path=image_path)
    except ProbeError as exc:
        result["category"] = str(exc) if str(exc) in {"ocr_language_data_unavailable", "ocr_engine_failed"} else "page_ocr_or_numeric_validation_failed"
        return result
    except NumericEvidenceError as exc:
        result["category"] = native._numeric_failure_category(exc)
        if result["category"] == "numeric_crop_geometry_mismatch":
            diagnostic = safe_geometry_diagnostics(exc)
            if diagnostic:
                result["geometry_diagnostics"] = diagnostic
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


def probe_pages(input_dir: Path, manifest: Path, page_checks: Path, producer_metadata: Path, *,
                date_folder: str, source_run_id: str, expected_articles: int,
                source_kind: str, repository: str, original_source_run_id: str = "") -> dict[str, Any]:
    if source_kind != "original-archive":
        raise ProbeError("page_diagnostics_require_original_archive")
    validate_inputs(date_folder, source_run_id, expected_articles)
    producer_raw, _ = _json_file(Path(producer_metadata), 1_000_000)
    execution_sha = verify_producer(producer_metadata, source_run_id, source_kind=source_kind, repository=repository)
    request_raw, _ = _json_file(Path(page_checks), FIXTURE_BYTE_LIMIT)
    requests = read_page_checks(page_checks)
    input_dir, manifest = Path(input_dir), Path(manifest)
    raw_manifest, sources = _preflight(input_dir, manifest, expected_articles, date_folder, [], page_checks=requests)
    archive_raw = _archive_receipt(input_dir, manifest, source_run_id=source_run_id, date_folder=date_folder,
                                   execution_sha=execution_sha, expected_articles=expected_articles,
                                   original_source_run_id=original_source_run_id)
    if Path(producer_metadata).read_bytes() != producer_raw or Path(page_checks).read_bytes() != request_raw:
        raise ProbeError("probe_inputs_changed")
    rows = json.loads(raw_manifest)
    results = []
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
                results.append({**request, "source_pdf_sha256": sha, **_diagnose_page(page, image_path)})
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
    args = parser.parse_args(argv)
    try:
        if (args.fixtures is None) == (args.page_checks is None):
            raise ProbeError("exactly_one_probe_request_required")
        if args.page_checks is not None:
            summary = probe_pages(args.input_dir, args.manifest, args.page_checks, args.producer_metadata,
                                  date_folder=args.date_folder, source_run_id=args.source_run_id,
                                  expected_articles=positive_count(args.expected_articles), source_kind=args.source_kind,
                                  repository=args.repository, original_source_run_id=args.original_source_run_id)
        else:
            summary = probe_fields(args.input_dir, args.manifest, args.fixtures, args.producer_metadata,
                                   date_folder=args.date_folder, source_run_id=args.source_run_id,
                                   expected_articles=positive_count(args.expected_articles), source_kind=args.source_kind,
                                   repository=args.repository, original_source_run_id=args.original_source_run_id)
        exit_code = 0 if summary["success"] else 3
    except ProbeError as exc:
        summary, exit_code = failure_summary(str(exc), exc.geometry_diagnostics), 2
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
