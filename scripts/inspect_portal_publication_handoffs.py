#!/usr/bin/env python3
"""Read exact known publication receipts; emit only replay inputs and hashes."""
from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import sys


# Bound to receipts observed in successful producer dispatch logs for the
# pending maintenance queue. No listing, guessing, writes or source-text reads.
KNOWN_RECEIPTS = {
    "15c77cbe1a70e01cb08c73bfb1db6ba026da3c61c92c032b0433ad835005b91d": "extended",
    "96d82177ff5aa7620306aa7f1a9ae7091e6001aa98396db2d2b18c210b9fa343": "extended",
    "4cf76de0b8807a2ba4c0dcf133abf8b758caad22dfa7c2afe64229f846e68886": "extended",
    "b35eacbcbe619b5b18a515d593fb28b36595ae76a9ee0c4f47c91ab4affce389": "extended",
    "53b1b6f05090013b7c8202b95c7ddca571ca2eaa81122202188d8271878a3ff3": "extended",
    "b21cd49b56267d8e49b7f84474e714668ff22a90d0936cf0b9cd642621f5b542": "extended",
    "e25caa544eb5fe5f101caa239c21ba0c3cca8a4a503a76f1aeff72a59fccd323": "english",
    "70c8c92d5050635588b527e1e6820ad24c3b6b6c5e4a33ad6d4d08c86f50099a": "english",
}
PREFIXES = {"extended": "_extended-locales/v1", "english": "_english-commentary/v1"}
HEX64 = re.compile(r"[0-9a-f]{64}\Z")
LOCALES = frozenset("fr pt es tr ru th it de vi ms id tl hi zh-Hant pl cs nl km my fa gu ur te mr he bn ta uk bo kk mn ug yue".split())
MAX_BYTES = 65536


def require(condition):
    if not condition:
        raise ValueError("Invalid publication receipt inspection input")


def checked_projection(raw: bytes, receipt: str, kind: str) -> dict:
    require(kind in PREFIXES and bool(HEX64.fullmatch(receipt)))
    require(0 < len(raw) <= MAX_BYTES and hashlib.sha256(raw).hexdigest() == receipt)
    value = json.loads(raw)
    require(isinstance(value, dict) and value.get("schema_version") == 1)
    batch = value.get("batch")
    require(isinstance(batch, dict) and isinstance(batch.get("generation"), str)
            and bool(HEX64.fullmatch(batch["generation"])))
    inputs = {"operation": "migrate", "translation_scope": "incremental"}
    if kind == "extended":
        candidates = batch.get("candidates")
        require(isinstance(candidates, dict) and 0 < len(candidates) <= len(LOCALES))
        require(all(locale in LOCALES and isinstance(candidate, str) and HEX64.fullmatch(candidate)
                    for locale, candidate in candidates.items()))
        inputs.update(extended_locales=",".join(sorted(candidates)),
                      extended_source_generation=batch["generation"],
                      extended_candidate_ids=",".join(f"{key}={candidates[key]}" for key in sorted(candidates)),
                      extended_handoff=receipt)
        candidate_map = {key: candidates[key] for key in sorted(candidates)}
    else:
        candidate = batch.get("candidate_id")
        require(isinstance(candidate, str) and bool(HEX64.fullmatch(candidate)))
        inputs["english_handoff"] = receipt
        candidate_map = {"en": candidate}
    return {"kind": kind, "receipt_sha256": receipt, "source_generation": batch["generation"],
            "candidate_map": candidate_map, "workflow": "neutral-edge-cutover.yml", "ref": "main", "inputs": inputs}


def inspect(client, bucket: str, receipts: list[str]) -> dict:
    require(0 < len(receipts) <= len(KNOWN_RECEIPTS) and len(set(receipts)) == len(receipts))
    require(all(receipt in KNOWN_RECEIPTS for receipt in receipts))
    rows = []
    for receipt in receipts:
        kind = KNOWN_RECEIPTS[receipt]
        response = client.get_object(Bucket=bucket, Key=f"{PREFIXES[kind]}/publication-handoffs/{receipt}/receipt.json")
        body = response["Body"]
        try:
            raw = body.read(MAX_BYTES + 1)
        finally:
            body.close()
        rows.append(checked_projection(raw, receipt, kind))
    return {"schema_version": 1, "read_only": True, "receipts": rows}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--receipts", required=True)
    args = parser.parse_args()
    try:
        from portal_extended_r2 import build_r2_client, require_env
        result = inspect(build_r2_client(), require_env("R2_BUCKET"), args.receipts.split(","))
    except Exception:
        print("Publication receipt inspection failed; no private receipt content emitted.", file=sys.stderr)
        return 1
    print(json.dumps(result, ensure_ascii=False, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
