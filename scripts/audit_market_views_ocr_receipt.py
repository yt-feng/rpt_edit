#!/usr/bin/env python3
"""Read a private complete source receipt and emit a sanitized OCR acceptance audit.

The audit reuses the production source validator before summarizing coverage.
It publishes hashes, page numbers, counters and optional explicitly supplied
numeric fixture matches. It never publishes report names, source prose, image
bytes, download URLs, bucket names or credentials, and makes no network calls.
Failed fixtures include only bounded, allowlisted numeric recognition evidence.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
from pathlib import Path
import re
import sys
import tempfile
import stat
from typing import Any

from extract_native_market_sources import MANIFEST_NAME, RECEIPT_NAME, validate_sources
from ocr_numeric_evidence import normalize_number, NUMERIC, _overlap, OCR_CROP_POLICY, MAX_IMAGE_PIXELS


SCHEMA = 1
SHA = re.compile(r"[a-f0-9]{64}")
COUNT_KEYS = ("source_num_count", "verified_count", "corrected_count", "unresolved_count",
              "secondary_only_count", "observed_num_count")
DIAGNOSTIC_RECORD_LIMIT = 8
DIAGNOSTIC_READ_LIMIT = 3
DIAGNOSTIC_SCAN_LIMIT = 10_000
DIAGNOSTIC_MARK_LIMIT = 4096
DIAGNOSTIC_BYTE_LIMIT = 32_768
DIAGNOSTIC_STATUSES = {"verified", "corrected", "unresolved"}
DIAGNOSTIC_REASONS = {
    "source_position_unresolved", "positioned_reads_disagree", "decimal_not_visible",
    "visible_decimal_omitted", "visible_minus_omitted", "visible_negative_parentheses_omitted",
    "minus_not_visible", "negative_parentheses_not_visible", "percent_not_visible",
    "visible_percent_omitted", "three_positioned_reads_and_source_marks", "not_present_in_primary_transcript",
}
DIAGNOSTIC_METHODS = {"second-page-psm-3", "source-crop-psm-6", "source-crop-psm-11"}
DIAGNOSTIC_MARKS = ("decimal_marks", "minus_marks", "percent_marks", "parentheses_marks")


class AuditError(ValueError):
    pass


def _read_json(path: Path, limit: int) -> tuple[bytes, Any]:
    if path.is_symlink() or not path.is_file() or path.stat().st_size > limit:
        raise AuditError("invalid_input_file")
    raw = path.read_bytes()
    try:
        return raw, json.loads(raw)
    except (UnicodeError, json.JSONDecodeError) as exc:
        raise AuditError("invalid_input_json") from exc


def read_fixtures(path: Path | None) -> list[dict[str, Any]]:
    if path is None:
        return []
    _, fixtures = _read_json(Path(path), 1_000_000)
    if not isinstance(fixtures, dict) or set(fixtures) != {"schema", "checks"} or type(fixtures.get("schema")) is not int or fixtures.get("schema") != 1:
        raise AuditError("invalid_fixture_schema")
    checks = fixtures["checks"]
    if not isinstance(checks, list) or not 1 <= len(checks) <= 100:
        raise AuditError("invalid_fixture_count")
    seen = set()
    for check in checks:
        required = {"id", "source_pdf_sha256", "page", "expected_literal", "expected_bbox"}
        if not isinstance(check, dict) or set(check) - (required | {"min_overlap"}) or required - set(check):
            raise AuditError("invalid_fixture_fields")
        identifier = check["id"]
        if not isinstance(identifier, str) or not re.fullmatch(r"[a-z][a-z0-9_]{0,47}", identifier) or identifier in seen:
            raise AuditError("invalid_fixture_id")
        seen.add(identifier)
        if not isinstance(check["source_pdf_sha256"], str) or not SHA.fullmatch(check["source_pdf_sha256"]):
            raise AuditError("invalid_fixture_source_hash")
        if type(check["page"]) is not int or check["page"] <= 0:
            raise AuditError("invalid_fixture_page")
        literal = check["expected_literal"]
        if not isinstance(literal, str) or len(literal) > 64 or not NUMERIC.fullmatch(literal):
            raise AuditError("invalid_fixture_numeric_literal")
        box = check["expected_bbox"]
        if not isinstance(box, list) or len(box) != 4 or any(type(v) not in (int, float) or not 0 <= v <= 100_000 for v in box) or box[2] <= box[0] or box[3] <= box[1]:
            raise AuditError("invalid_fixture_bbox")
        overlap = check.get("min_overlap", 0.55)
        if type(overlap) not in (int, float) or not 0.1 <= overlap <= 1:
            raise AuditError("invalid_fixture_overlap")
    return checks


def _counts(page: dict[str, Any]) -> dict[str, int]:
    if page["extraction_method"] != "ocr":
        return {key: 0 for key in COUNT_KEYS}
    evidence = page["ocr"]["numeric_evidence"]
    counts = {key: evidence.get(key) for key in COUNT_KEYS}
    if any(type(value) is not int or value < 0 for value in counts.values()):
        raise AuditError("invalid_numeric_counts")
    if counts["source_num_count"] != counts["verified_count"] + counts["corrected_count"] + counts["unresolved_count"] or counts["observed_num_count"] != counts["source_num_count"] + counts["secondary_only_count"]:
        raise AuditError("inconsistent_numeric_counts")
    return counts


def _diagnostic_number(value: Any) -> str | None:
    # Numeric OCR candidates remain untrusted data, even after receipt hashing.
    # Do not copy arbitrary strings or pending markers to this public summary.
    if (isinstance(value, str) and 0 < len(value) <= 64
            and re.fullmatch(r"[0-9.,+\-−–()$€£¥% bBpPsSxX]+", value)
            and NUMERIC.fullmatch(value)):
        return value
    return None


def _diagnostic_bbox(value: Any) -> list[int | float] | None:
    if (isinstance(value, list) and len(value) == 4
            and all(type(item) in (int, float) and 0 <= item <= 100_000 and math.isfinite(item) for item in value)
            and value[2] > value[0] and value[3] > value[1]):
        return list(value)
    return None


def _diagnostic_witness(value: Any) -> dict[str, Any]:
    if not isinstance(value, dict):
        return {}
    output = {}
    for key in ("width", "height"):
        if type(value.get(key)) is int and 1 <= value[key] <= 100_000:
            output[key] = value[key]
    if type(value.get("threshold")) is int and 0 <= value["threshold"] <= 255:
        output["threshold"] = value["threshold"]
    if isinstance(value.get("pixel_sha256"), str) and SHA.fullmatch(value["pixel_sha256"]):
        output["pixel_sha256"] = value["pixel_sha256"]
    components = value.get("components")
    if isinstance(components, list) and len(components) <= DIAGNOSTIC_MARK_LIMIT:
        output["component_count"] = len(components)
    for key in DIAGNOSTIC_MARKS:
        marks = value.get(key)
        if (isinstance(marks, list) and len(marks) <= DIAGNOSTIC_MARK_LIMIT
                and all(_diagnostic_bbox(box) is not None for box in marks)):
            output[key] = {"present": bool(marks), "count": len(marks)}
    return output


def _diagnostic_read(value: Any) -> dict[str, Any] | None:
    if (not isinstance(value, dict) or not isinstance(value.get("method"), str)
            or value["method"] not in DIAGNOSTIC_METHODS):
        return None
    output = {"method": value["method"], "literal": _diagnostic_number(value.get("literal"))}
    if type(value.get("dpi")) is int and value["dpi"] in {300, 450, 600}:
        output["dpi"] = value["dpi"]
    box = _diagnostic_bbox(value.get("bbox"))
    if box is not None:
        output["bbox"] = box
    if type(value.get("field_count")) is int and 0 <= value["field_count"] <= 2500:
        output["field_count"] = value["field_count"]
    if isinstance(value.get("input_pixel_sha256"), str) and SHA.fullmatch(value["input_pixel_sha256"]):
        output["input_pixel_sha256"] = value["input_pixel_sha256"]
    clip, size = _diagnostic_bbox(value.get("source_clip_bbox")), value.get("crop_pixel_size")
    if (value["method"] in {"source-crop-psm-6", "source-crop-psm-11"}
            and value.get("crop_policy") == OCR_CROP_POLICY and clip is not None
            and isinstance(size, list) and len(size) == 2
            and all(type(item) is int and 1 <= item <= 100_000 for item in size)
            and size[0] * size[1] <= MAX_IMAGE_PIXELS):
        output.update(crop_policy=OCR_CROP_POLICY, source_clip_bbox=clip, crop_pixel_size=list(size))
    return output


def _diagnostic_candidates(evidence: dict[str, Any], box: list[int | float], overlap: float) -> dict[str, Any]:
    fields = evidence.get("second_page_fields")
    if not isinstance(fields, list):
        return {"candidate_count": 0, "candidates": [], "scan_truncated": False, "candidates_truncated": False}
    hits = []
    for field in fields[:DIAGNOSTIC_SCAN_LIMIT]:
        if not isinstance(field, dict):
            continue
        position = _diagnostic_bbox(field.get("bbox"))
        if position is not None and _overlap(box, position) >= overlap:
            hits.append({"bbox": position, "literal": _diagnostic_number(field.get("literal"))})
    return {"candidate_count": len(hits), "candidates": hits[:DIAGNOSTIC_RECORD_LIMIT],
            "scan_truncated": len(fields) > DIAGNOSTIC_SCAN_LIMIT,
            "candidates_truncated": len(hits) > DIAGNOSTIC_RECORD_LIMIT}


def _fixture_diagnostics(evidence: dict[str, Any], hits: list[dict[str, Any]],
                         check: dict[str, Any]) -> dict[str, Any]:
    """Project only bounded numeric evidence; never participate in acceptance."""
    output = {"positional_record_count": len(hits), "records_truncated": len(hits) > DIAGNOSTIC_RECORD_LIMIT,
              "records": [], "second_page_at_fixture": _diagnostic_candidates(
                  evidence, check["expected_bbox"], check.get("min_overlap", 0.55))}
    if type(evidence.get("source_dpi")) is int and evidence["source_dpi"] in {300, 450, 600}:
        output["source_dpi"] = evidence["source_dpi"]
    for record in hits[:DIAGNOSTIC_RECORD_LIMIT]:
        row = {"primary_literal": _diagnostic_number(record.get("literal"))}
        if isinstance(record.get("id"), str) and re.fullmatch(r"[ns][0-9]{4}", record["id"]):
            row["id"] = record["id"]
        if isinstance(record.get("status"), str) and record["status"] in DIAGNOSTIC_STATUSES:
            row["status"] = record["status"]
            if record["status"] in {"verified", "corrected"}:
                row["admitted_literal"] = _diagnostic_number(record.get("safe_literal"))
        if isinstance(record.get("reason"), str) and record["reason"] in DIAGNOSTIC_REASONS:
            row["reason"] = record["reason"]
        for key in ("bbox", "source_pixel_bbox"):
            position = _diagnostic_bbox(record.get(key))
            if position is not None:
                row[key] = position
        if "bbox" in row:
            # Mirror the numeric auditor's exact 0.55 source-position lookup.
            # The fixture's wider box may contain a different candidate set.
            row["second_page_at_record"] = _diagnostic_candidates(evidence, row["bbox"], 0.55)
        reads = record.get("reads")
        if isinstance(reads, list):
            row["reads"] = [safe for value in reads[:DIAGNOSTIC_READ_LIMIT]
                            if (safe := _diagnostic_read(value)) is not None]
            row["reads_truncated"] = len(reads) > DIAGNOSTIC_READ_LIMIT
        row["pixel_punctuation"] = _diagnostic_witness(record.get("pixel_punctuation"))
        output["records"].append(row)
    if len(json.dumps(output, ensure_ascii=False, allow_nan=False).encode("utf-8")) > DIAGNOSTIC_BYTE_LIMIT:
        raise AuditError("numeric_diagnostic_size_exceeded")
    return output


def _fixture_matches(receipt: dict[str, Any], checks: list[dict[str, Any]]) -> list[dict[str, Any]]:
    output = []
    # Duplicate file aliases preserve source coverage but cannot make one
    # content-bound fixture look ambiguous or multiply its evidence.
    sources = {}
    for report in receipt["reports"]:
        sources.setdefault(report["content_sha256"], report)
    for check in checks:
        report = sources.get(check["source_pdf_sha256"])
        result = {"id": check["id"], "source_pdf_sha256": check["source_pdf_sha256"],
                  "page": check["page"], "expected_literal": check["expected_literal"],
                  "expected_bbox": check["expected_bbox"], "matched": False,
                  "category": "source_missing", "matched_bbox": None, "extraction_decision": None}
        if report is None:
            output.append(result)
            continue
        if check["page"] > report["page_count"]:
            result["category"] = "page_missing"
            output.append(result)
            continue
        page = report["pages"][check["page"] - 1]
        if page["extraction_method"] != "ocr":
            result["category"] = "not_an_ocr_page"
            output.append(result)
            continue
        evidence = page["ocr"]["numeric_evidence"]
        result["numeric_evidence_sha256"] = evidence["evidence_sha256"]
        result["input_pixel_sha256"] = evidence["input_pixel_sha256"]
        hits = [record for record in evidence["records"] if record.get("bbox") is not None
                and _overlap(check["expected_bbox"], record["bbox"]) >= check.get("min_overlap", 0.55)]
        matching = [record for record in hits if record["status"] in {"verified", "corrected"}
                    and normalize_number(record["safe_literal"]) == normalize_number(check["expected_literal"])]
        if len(matching) == 1:
            result.update({"matched": True, "category": "passed", "matched_bbox": matching[0]["bbox"],
                           "extraction_decision": matching[0]["status"]})
        elif len(matching) > 1:
            result["category"] = "ambiguous_match"
        elif any(record["status"] == "unresolved" for record in hits):
            result["category"] = "field_unresolved"
        elif hits:
            result["category"] = "value_mismatch"
        else:
            result["category"] = "position_missing"
        if not result["matched"]:
            result["numeric_diagnostics"] = _fixture_diagnostics(evidence, hits, check)
        output.append(result)
    return output


def summarize_verified_receipt(receipt: dict[str, Any], receipt_sha256: str,
                               checks: list[dict[str, Any]]) -> dict[str, Any]:
    if receipt.get("schema") != 2 or receipt.get("complete") is not True:
        raise AuditError("complete_schema_two_required")
    totals = {key: 0 for key in COUNT_KEYS}
    unique_totals = {key: 0 for key in COUNT_KEYS}
    pages, seen = [], set()
    methods = {"native": 0, "ocr": 0, "blank": 0}
    for ordinal, report in enumerate(receipt["reports"], 1):
        sha = report["content_sha256"]
        duplicate = sha in seen
        seen.add(sha)
        for page in report["pages"]:
            counts = _counts(page)
            method = page["extraction_method"]
            methods[method] += 1
            for key, value in counts.items():
                totals[key] += value
                if not duplicate:
                    unique_totals[key] += value
            row = {"source_ordinal": ordinal, "source_pdf_sha256": sha, "duplicate_content": duplicate,
                   "page": page["page"], "extraction_method": method, **counts,
                   "unconfirmed_num_count": counts["unresolved_count"] + counts["secondary_only_count"]}
            if method == "ocr":
                evidence = page["ocr"]["numeric_evidence"]
                row.update({"numeric_evidence_sha256": evidence["evidence_sha256"],
                            "input_pixel_sha256": evidence["input_pixel_sha256"]})
            pages.append(row)
    fixtures = _fixture_matches(receipt, checks)
    return {"schema": SCHEMA, "success": all(row["matched"] for row in fixtures),
            "source_contract_verified": True, "receipt_sha256": receipt_sha256,
            "manifest_sha256": receipt["manifest_sha256"], "report_count": receipt["report_count"],
            "unique_content_count": len(seen), "page_count": len(pages), "page_methods": methods,
            "numeric_totals": {**totals, "unconfirmed_num_count": totals["unresolved_count"] + totals["secondary_only_count"]},
            "unique_content_numeric_totals": {**unique_totals, "unconfirmed_num_count": unique_totals["unresolved_count"] + unique_totals["secondary_only_count"]},
            "pages": pages, "fixture_count": len(fixtures),
            "fixture_passed_count": sum(row["matched"] for row in fixtures), "fixtures": fixtures,
            "fixture_acceptance": ("passed" if all(row["matched"] for row in fixtures) else "failed") if fixtures else "not_requested",
            "provider_post_count": 0, "model_call_count": 0}


def audit_sources(source_dir: Path, expected_reports: int, *, manifest: Path | None = None,
                  fixtures: Path | None = None, expected_source_context: dict[str, str] | None = None) -> dict[str, Any]:
    source_dir = Path(source_dir)
    if type(expected_reports) is not int or expected_reports <= 0:
        raise AuditError("invalid_expected_reports")
    checks = read_fixtures(fixtures)
    # A complete OCR receipt can legitimately exceed the old audit-only 256 MB
    # limit. The source validator owns the full evidence contract. Hash it in
    # bounded chunks instead of retaining another bytes/JSON copy beside it.
    before = receipt_identity(source_dir / RECEIPT_NAME)
    receipt = validate_sources(source_dir, manifest or source_dir / MANIFEST_NAME, expected_reports,
                               expected_source_context=expected_source_context)
    if receipt_identity(source_dir / RECEIPT_NAME) != before:
        raise AuditError("receipt_changed_during_audit")
    return summarize_verified_receipt(receipt, before["sha256"], checks)


def receipt_identity(path: Path) -> dict[str, Any]:
    """Hash a stable regular receipt without materializing its source contents."""
    path = Path(path)
    if path.is_symlink():
        raise AuditError("invalid_receipt_file")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    try:
        fd = os.open(path, flags)
        with os.fdopen(fd, "rb") as stream:
            before = os.fstat(stream.fileno())
            if not stat.S_ISREG(before.st_mode):
                raise AuditError("invalid_receipt_file")
            digest, size = hashlib.sha256(), 0
            while block := stream.read(1024 * 1024):
                size += len(block)
                digest.update(block)
            after = os.fstat(stream.fileno())
        current = path.lstat()
    except OSError:
        raise AuditError("invalid_receipt_file") from None
    signature = lambda value: (value.st_dev, value.st_ino, value.st_size, value.st_mtime_ns, value.st_ctime_ns)
    if (not stat.S_ISREG(current.st_mode) or signature(before) != signature(after)
            or signature(after) != signature(current) or size != after.st_size):
        raise AuditError("receipt_changed_during_audit")
    return {"sha256": digest.hexdigest(), "bytes": size}


def write_summary(path: Path, summary: dict[str, Any], *, source_dir: Path) -> None:
    path = Path(path)
    if path.is_symlink() or source_dir.resolve() == path.resolve() or source_dir.resolve() in path.resolve().parents:
        raise AuditError("summary_must_be_outside_private_sources")
    path.parent.mkdir(parents=True, exist_ok=True)
    raw = (json.dumps(summary, ensure_ascii=False, indent=2) + "\n").encode("utf-8")
    temporary = None
    try:
        with tempfile.NamedTemporaryFile(prefix=".ocr-audit-", dir=path.parent, delete=False) as output:
            temporary = Path(output.name)
            output.write(raw)
        os.replace(temporary, path)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--expected-reports", type=int, required=True)
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--fixtures", type=Path)
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--date-folder")
    parser.add_argument("--producer-run-id")
    parser.add_argument("--execution-sha")
    parser.add_argument("--original-source-run-id")
    args = parser.parse_args()
    context = {name: getattr(args, name) for name in ("date_folder", "producer_run_id", "execution_sha", "original_source_run_id")}
    try:
        if any(value is not None for value in context.values()) and any(value is None for value in context.values()):
            raise AuditError("incomplete_expected_source_context")
        summary = audit_sources(args.source_dir, args.expected_reports, manifest=args.manifest,
                                fixtures=args.fixtures, expected_source_context=context if context["date_folder"] else None)
        write_summary(args.summary, summary, source_dir=args.source_dir)
    except (OSError, ValueError, TypeError, KeyError):
        # Source validators may mention a private filename in their exceptions.
        # Never print or attach the raw exception to this public audit output.
        print("OCR source audit stopped: source_contract_or_input_invalid", file=sys.stderr)
        return 2
    print(json.dumps({"source_contract_verified": True, "page_count": summary["page_count"],
                      "ocr_page_count": summary["page_methods"]["ocr"], "numeric_totals": summary["numeric_totals"],
                      "fixture_count": summary["fixture_count"], "fixture_passed_count": summary["fixture_passed_count"]}, sort_keys=True))
    return 0 if summary["success"] else 3


if __name__ == "__main__":
    raise SystemExit(main())
