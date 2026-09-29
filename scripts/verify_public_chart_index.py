#!/usr/bin/env python3
"""Bind served chart indexes to the prepared release; never fetch or publish."""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re

from compare_portal_release_semantics import digest, load_manifest, stable_value

MAX_INDEX_BYTES = 128 * 1024 * 1024
FIELDS = frozenset({"schema_version", "normalizer_version", "byte_size", "file_sha256",
                    "semantic_sha256", "report_count", "item_count"})


def document(path: Path) -> tuple[dict, bytes]:
    with path.open("rb") as stream:
        body = stream.read(MAX_INDEX_BYTES + 1)
    if not body or len(body) > MAX_INDEX_BYTES:
        raise ValueError("index_size_invalid")
    value = json.loads(body)
    if not isinstance(value, dict):
        raise ValueError("index_shape_invalid")
    return value, body


def index_receipt(path: Path) -> dict:
    value, body = document(path)
    if type(value.get("schema_version")) is not int or value["schema_version"] != 1:
        raise ValueError("index_schema_invalid")
    reports = value.get("reports")
    if not isinstance(reports, list):
        raise ValueError("reports_shape_invalid")
    total = 0
    for report in reports:
        if not isinstance(report, dict) or not isinstance(report.get("charts"), list):
            raise ValueError("report_shape_invalid")
        charts = report["charts"]
        if any(not isinstance(chart, dict) for chart in charts):
            raise ValueError("chart_shape_invalid")
        if type(report.get("chart_count")) is not int or report["chart_count"] != len(charts):
            raise ValueError("report_chart_count_mismatch")
        total += len(charts)
    for key, expected in (("report_count", len(reports)), ("item_count", total)):
        if type(value.get(key)) is not int or value[key] != expected:
            raise ValueError("index_count_mismatch")
    return {"schema_version": 1, "normalizer_version": 1, "byte_size": len(body),
            "file_sha256": hashlib.sha256(body).hexdigest(),
            "semantic_sha256": digest(stable_value(value)),
            "report_count": len(reports), "item_count": total}


def read_receipt(path: Path) -> dict:
    value, _ = document(path)
    if set(value) != FIELDS or value.get("schema_version") != 1 or value.get("normalizer_version") != 1:
        raise ValueError("receipt_schema_invalid")
    for field in ("schema_version", "normalizer_version", "byte_size", "report_count", "item_count"):
        if type(value[field]) is not int or value[field] < 0:
            raise ValueError("receipt_count_invalid")
    if not 0 < value["byte_size"] <= MAX_INDEX_BYTES:
        raise ValueError("receipt_size_invalid")
    for field in ("file_sha256", "semantic_sha256"):
        if not isinstance(value[field], str) or not re.fullmatch(r"[0-9a-f]{64}", value[field]):
            raise ValueError("receipt_digest_invalid")
    return value


def require_semantics(receipt: dict, semantics: Path) -> None:
    manifest = load_manifest(semantics)
    if receipt["semantic_sha256"] != manifest["components"]["chart_search_index"]:
        raise ValueError("release_chart_semantics_mismatch")


def write_report(path: Path, value: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, sort_keys=True, indent=2) + "\n", encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("mode", choices=("prepare", "verify"))
    parser.add_argument("--index", type=Path)
    parser.add_argument("--semantics", type=Path, required=True)
    parser.add_argument("--expected", type=Path)
    parser.add_argument("--public-index", type=Path)
    parser.add_argument("--release-index", type=Path)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    if args.mode == "prepare" and args.index is None:
        parser.error("prepare requires --index")
    if args.mode == "verify" and any(value is None for value in
                                      (args.expected, args.public_index, args.release_index)):
        parser.error("verify requires --expected, --public-index and --release-index")
    report = {"schema_version": 1, "status": "failed"}
    try:
        if args.mode == "prepare":
            receipt = index_receipt(args.index)
            require_semantics(receipt, args.semantics)
            write_report(args.output, receipt)
        else:
            expected = read_receipt(args.expected)
            require_semantics(expected, args.semantics)
            report["expected"] = expected
            for label, path in (("release", args.release_index), ("public", args.public_index)):
                actual = index_receipt(path)
                report[label] = actual
                if actual != expected:
                    raise ValueError("served_chart_index_mismatch")
            report["status"] = "passed"
            write_report(args.output, report)
    except (OSError, ValueError, TypeError, KeyError, UnicodeError):
        # Only bounded counts and digests enter the artifact, never response
        # content, source paths, URLs, or exception text.
        if args.mode == "verify":
            write_report(args.output, report)
        print("Chart index acceptance failed; expected release content was not verified")
        return 1
    print("Chart index acceptance " + ("prepared" if args.mode == "prepare" else "passed"))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
