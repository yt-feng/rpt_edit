#!/usr/bin/env python3
"""Check the Chinese app's existing loading budgets before expensive build work."""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
from pathlib import Path


MAX_RAW_BYTES = 700_000
MAX_GZIP_BYTES = 150_000
MAX_RAW_DELTA = 24_000
MAX_GZIP_DELTA = 6_000


def check_budget(candidate: bytes, active: bytes | None = None) -> dict:
    compressed = gzip.compress(candidate, compresslevel=9, mtime=0)
    report = {
        "schema_version": 1,
        "candidate_bytes": len(candidate),
        "candidate_gzip_bytes": len(compressed),
        "candidate_sha256": hashlib.sha256(candidate).hexdigest(),
        "active_compared": active is not None,
        "limits": {"raw_bytes": MAX_RAW_BYTES, "gzip_bytes": MAX_GZIP_BYTES,
                   "raw_delta_bytes": MAX_RAW_DELTA, "gzip_delta_bytes": MAX_GZIP_DELTA},
        "violations": [],
    }
    if not candidate:
        report["violations"].append("empty app bundle")
    if len(candidate) > MAX_RAW_BYTES or len(compressed) > MAX_GZIP_BYTES:
        report["violations"].append("absolute loading budget")
    if active is not None:
        active_gzip = gzip.compress(active, compresslevel=9, mtime=0)
        report.update(active_bytes=len(active), active_gzip_bytes=len(active_gzip),
                      active_sha256=hashlib.sha256(active).hexdigest(),
                      raw_delta_bytes=len(candidate) - len(active),
                      gzip_delta_bytes=len(compressed) - len(active_gzip))
        if report["raw_delta_bytes"] > MAX_RAW_DELTA or report["gzip_delta_bytes"] > MAX_GZIP_DELTA:
            report["violations"].append("active-release delta budget")
    report["status"] = "failed" if report["violations"] else "passed"
    return report


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--candidate", type=Path, required=True)
    parser.add_argument("--active", type=Path)
    parser.add_argument("--output", type=Path)
    args = parser.parse_args()
    report = check_budget(args.candidate.read_bytes(), args.active.read_bytes() if args.active else None)
    payload = json.dumps(report, sort_keys=True, separators=(",", ":")) + "\n"
    if args.output:
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(payload, encoding="utf-8")
    print(payload, end="")
    if report["status"] != "passed":
        print("Chinese app bundle exceeds its " + ", ".join(report["violations"]))
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
