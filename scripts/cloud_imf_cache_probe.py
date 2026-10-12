"""Cloud-only, bounded GET inspection of exact pending IMF source bindings.

No object listing, writes, PDF downloads, provider calls, or credential output.
The active institution dependency index is the sole private discovery root.
"""
from __future__ import annotations

import hashlib
import json
import os
from pathlib import Path
import re
from urllib.parse import urlsplit

from institution_dependency_backlog import Backlog, PREFIX
from mineru_result_cache import ResultCache
from mineru_task_ledger import digest, encoded, exact_json
from private_workflow_handoff import build_r2_client, r2_bucket

MAX_RECORDS = 100
MAX_VERSIONS = 200
REQUIRED_ENV = ("R2_ACCOUNT_ID", "R2_ACCESS_KEY_ID", "R2_SECRET_ACCESS_KEY", "R2_BUCKET")
SEED = Path("institution_feeds/pending_intake/imf.json")
OUT = Path("_imf_cache_probe/summary.json")


class ProbeContractError(ValueError):
    pass


def require(condition):
    if not condition:
        raise ProbeContractError()


def targets_from_seed(path=SEED):
    require(path.is_file() and not path.is_symlink() and path.stat().st_size <= 128 * 1024)
    seed = json.loads(path.read_text())
    require(seed.get("institution") == "imf" and isinstance(seed.get("items"), dict)
            and len(seed["items"]) == 17)
    targets = {}
    for record in seed["items"].values():
        item = record["item"]
        url, guid = item["source_url"], item["guid"]
        parsed = urlsplit(url)
        require(parsed.scheme == "https" and parsed.netloc == "www.imf.org"
                and parsed.path.startswith("/en/publications/")
                and not parsed.query and not parsed.fragment
                and isinstance(guid, str) and re.fullmatch(r"[a-f0-9]{56,64}", guid)
                and url not in targets)
        targets[url] = guid
    return targets


def probe(client, bucket, targets):
    """Accept an injected client so offline tests cannot contact storage."""
    result = {
        "schema": 1,
        "status": "starting",
        "scope": "active institution dependency index only",
        "target_count": len(targets),
        "limits": {"active_records": MAX_RECORDS, "versions": MAX_VERSIONS,
                   "object_bytes": 256 * 1024, "get_requests": 1 + MAX_RECORDS + MAX_VERSIONS},
        "counts": {"get_requests": 0, "active_roots": 0, "records_read": 0,
                   "unique_bindings": 0, "versions_read": 0, "versions_absent": 0,
                   "publication_rows": 0, "matched_sources": 0},
        "truncated": {"active_records": False, "versions": False},
        "matches": [],
        "pdf_bytes_verified": False,
        "evidence": {"index_key": PREFIX + "active.json"},
    }
    backlog = Backlog(client, bucket)
    stage = "active_index"

    def read(key):
        result["counts"]["get_requests"] += 1
        require(result["counts"]["get_requests"] <= 1 + MAX_RECORDS + MAX_VERSIONS)
        return backlog._read(key)[0]

    try:
        index = read("active.json")
        if index is None:
            result["status"] = "active_index_absent"
            return result
        Backlog.validate_index(index)
        result["evidence"]["index_sha256"] = digest(encoded(index))
        roots = sorted(index["roots"].items())
        result["counts"]["active_roots"] = len(roots)
        result["truncated"]["active_records"] = len(roots) > MAX_RECORDS
        bindings, records = {}, {}
        stage = "active_record"
        for root, checksum in roots[:MAX_RECORDS]:
            record = read("records/" + checksum + ".json")
            require(record is not None and digest(encoded(record)) == checksum
                    and record.get("root_key") == root)
            Backlog.validate(record)
            result["counts"]["records_read"] += 1
            for binding in record["files"]:
                bid = binding["id"]
                require(bid not in bindings or exact_json(bindings[bid], binding))
                bindings[bid] = binding
                records.setdefault(bid, []).append(checksum)
        result["counts"]["unique_bindings"] = len(bindings)
        result["truncated"]["versions"] = len(bindings) > MAX_VERSIONS
        stage = "publication_versions"
        seen_matches = set()
        for bid in sorted(bindings)[:MAX_VERSIONS]:
            binding = bindings[bid]
            versions = read("versions/" + bid + ".json")
            if versions is None:
                result["counts"]["versions_absent"] += 1
                continue
            Backlog.validate_versions(versions, binding)
            result["counts"]["versions_read"] += 1
            versions_sha = digest(encoded(versions))
            for row in versions["versions"]:
                result["counts"]["publication_rows"] += 1
                source = row["source_page_url"]
                if source not in targets or (source, bid) in seen_matches:
                    continue
                seen_matches.add((source, bid))
                # Emit only exact allowlisted public source identity and hashes.
                # PDF URLs, source filenames, receipts, and raw records may carry
                # private data; they are never serialized into this diagnostic.
                result["matches"].append({
                    "guid": targets[source], "source_url": source,
                    "binding_id": bid, "pdf_sha256": binding["sha256"],
                    "pdf_bytes": binding["size"],
                    "record_sha256": sorted(set(records[bid])),
                    "versions_sha256": versions_sha,
                    "publication_row_sha256": digest(encoded(row)),
                    "pdf_url_sha256": hashlib.sha256(row["pdf_url"].encode()).hexdigest(),
                })
        result["status"] = "bounded_partial" if any(result["truncated"].values()) else "complete"
    except Exception as error:
        # Never serialize exception text: SDK errors can include request URLs.
        result["status"] = "stopped"
        result["error"] = {"stage": stage, "type": type(error).__name__}
    result["counts"]["matched_sources"] = len({x["guid"] for x in result["matches"]})
    return result


def main():
    if os.getenv("GITHUB_ACTIONS") != "true":
        print(json.dumps({"status": "cloud_only", "required_field": "GITHUB_ACTIONS"}))
        return 2
    summary = {"schema": 1, "status": "starting"}
    try:
        missing = [name for name in REQUIRED_ENV if not os.getenv(name, "").strip()]
        if missing:
            summary = {"schema": 1, "status": "configuration_missing", "fields": missing}
        else:
            targets = targets_from_seed()
            configured = ResultCache.single_attempt(build_r2_client(), r2_bucket())
            summary = probe(configured.client, configured.bucket, targets)
    except Exception as error:
        summary = {"schema": 1, "status": "stopped",
                   "error": {"stage": "configuration_or_seed", "type": type(error).__name__}}
    OUT.parent.mkdir(exist_ok=True)
    OUT.write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"status": summary["status"], "counts": summary.get("counts", {}),
                      "summary": str(OUT)}))
    return 1 if summary["status"] in {"stopped", "configuration_missing"} else 0


if __name__ == "__main__":
    raise SystemExit(main())
