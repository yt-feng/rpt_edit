#!/usr/bin/env python3
"""Read exact Extended handoff receipts and export only replay identities.

This does not inspect source text, change a queue, approve a candidate, or
dispatch publication. The publisher must still perform its normal checks.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
from pathlib import Path
from typing import Callable

from portal_extended_locales import ADDITIONAL
from portal_extended_r2 import DEFAULT_PREFIX, R2Store

MAX_RECEIPTS = 20
MAX_RECEIPT_BYTES = 65536
SHA256 = re.compile(r"[0-9a-f]{64}")
COMMIT = re.compile(r"[0-9a-f]{40}")
POSITIVE_ID = re.compile(r"[1-9][0-9]{0,19}")


class InspectionError(ValueError):
    pass


def receipt_hashes(value: str) -> list[str]:
    if not isinstance(value, str) or len(value) > MAX_RECEIPTS * 68:
        raise InspectionError("Receipt input exceeds its bound.")
    values = [part.strip() for part in re.split(r"[,\r\n]", value) if part.strip()]
    if not 1 <= len(values) <= MAX_RECEIPTS:
        raise InspectionError("Provide between 1 and 20 receipt hashes.")
    if any(not SHA256.fullmatch(part) for part in values):
        raise InspectionError("Receipt hashes must be lowercase SHA-256 values.")
    return list(dict.fromkeys(values))


def unique_object(pairs: list[tuple]) -> dict:
    value = {}
    for key, item in pairs:
        if key in value:
            raise InspectionError("Receipt contains duplicate fields.")
        value[key] = item
    return value


def replay_identity(identity: str, raw: bytes) -> dict:
    if not isinstance(identity, str) or not SHA256.fullmatch(identity):
        raise InspectionError("Receipt identity is invalid.")
    if not isinstance(raw, bytes) or not 0 < len(raw) <= MAX_RECEIPT_BYTES:
        raise InspectionError("Receipt size is invalid.")
    if hashlib.sha256(raw).hexdigest() != identity:
        raise InspectionError("Receipt checksum differs from its requested identity.")
    value = json.loads(raw, object_pairs_hook=unique_object)
    if (not isinstance(value, dict) or type(value.get("schema_version")) is not int
            or value["schema_version"] != 1 or type(value.get("paid_provider_requests")) is not int
            or value["paid_provider_requests"] != 0):
        raise InspectionError("Receipt provenance is invalid.")
    batch = value.get("batch")
    if not isinstance(batch, dict) or set(batch) != {"generation", "candidates"}:
        raise InspectionError("Receipt batch is invalid.")
    generation = batch["generation"]
    candidates = batch["candidates"]
    if not isinstance(generation, str) or not SHA256.fullmatch(generation):
        raise InspectionError("Receipt source generation is invalid.")
    if (not isinstance(candidates, dict) or not 1 <= len(candidates) <= len(ADDITIONAL)
            or any(locale not in ADDITIONAL for locale in candidates)
            or any(not isinstance(candidate, str) or not SHA256.fullmatch(candidate)
                   for candidate in candidates.values())):
        raise InspectionError("Receipt candidate identities are invalid.")
    producer = value.get("producer")
    if (not isinstance(producer, dict) or set(producer) != {"run_id", "attempt", "sha"}
            or any(not POSITIVE_ID.fullmatch(str(producer[key])) for key in ("run_id", "attempt"))
            or not isinstance(producer["sha"], str) or not COMMIT.fullmatch(producer["sha"])):
        raise InspectionError("Receipt producer identity is invalid.")
    # Deliberate projection: no raw receipt, content, emails, URLs, storage
    # identifiers, credentials, or additional provenance fields are exported.
    return {
        "handoff_sha256": identity,
        "generation": generation,
        "candidates": dict(sorted(candidates.items())),
        "producer": {"run_id": str(producer["run_id"]), "attempt": str(producer["attempt"]),
                     "sha": producer["sha"]},
    }


def inspect(read_receipt: Callable[[str], bytes], requested: str) -> dict:
    identities = receipt_hashes(requested)
    rows = [replay_identity(identity, read_receipt(identity)) for identity in identities]
    return {"schema_version": 1, "receipt_count": len(rows), "receipts": rows}


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipt-hashes", default=os.environ.get("HANDOFF_SHA256S", ""))
    parser.add_argument("--output", required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        # Validate before initializing any service client or reading storage.
        identities = receipt_hashes(args.receipt_hashes)
        store = R2Store.from_env(DEFAULT_PREFIX)
        result = inspect(lambda identity: store._get(
            store.key("publication-handoffs", identity, "receipt.json"), maximum=MAX_RECEIPT_BYTES,
        ), "\n".join(identities))
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(result, ensure_ascii=True, sort_keys=True, indent=2) + "\n", encoding="utf-8")
        args.output.chmod(0o600)
    except Exception:
        # Provider exceptions can include service endpoints or request details.
        # Neither raw receipt data nor exception strings belong in public logs.
        print(json.dumps({"ok": False, "error": "handoff_receipt_inspection_failed"}))
        return 1
    print(json.dumps({"ok": True, "receipt_count": result["receipt_count"]}))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
