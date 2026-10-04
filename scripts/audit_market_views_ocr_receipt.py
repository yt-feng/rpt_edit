#!/usr/bin/env python3
"""Read a private complete source receipt and emit a sanitized OCR acceptance audit.

The audit reuses the production source validator before summarizing coverage.
It publishes hashes, page numbers, counters and optional explicitly supplied
numeric fixture matches. It never publishes report names, source prose, image
bytes, download URLs, bucket names or credentials, and makes no network calls.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import sys
import tempfile
from typing import Any

from extract_native_market_sources import MANIFEST_NAME, RECEIPT_NAME, validate_sources
from ocr_numeric_evidence import normalize_number, NUMERIC, _overlap


SCHEMA = 1
SHA = re.compile(r"[a-f0-9]{64}")
COUNT_KEYS = ("source_num_count", "verified_count", "corrected_count", "unresolved_count",
              "secondary_only_count", "observed_num_count")


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
    raw, _ = _read_json(source_dir / RECEIPT_NAME, 256_000_000)
    receipt = validate_sources(source_dir, manifest or source_dir / MANIFEST_NAME, expected_reports,
                               expected_source_context=expected_source_context)
    if (source_dir / RECEIPT_NAME).read_bytes() != raw:
        raise AuditError("receipt_changed_during_audit")
    return summarize_verified_receipt(receipt, hashlib.sha256(raw).hexdigest(), checks)


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
