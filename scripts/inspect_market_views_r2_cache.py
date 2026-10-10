#!/usr/bin/env python3
"""Inspect fixed incident caches or one exact OCR checkpoint without mutation.

An archive's stored generation identity is reported, never treated as a match to
current source bytes or code. No provider calls, writes, deletions or PDF creation.
"""
from __future__ import annotations

import argparse
from contextlib import redirect_stderr, redirect_stdout
import hashlib
import json
import os
from pathlib import Path
import re
import tarfile
import tempfile
from typing import Any

import private_workflow_handoff as handoff
from upload_market_view_to_r2 import (parse_issue_date, r2_object_exists,
                                    validate_existing_pdf_object, validate_existing_private_pair)

DATES = ("261001", "261002", "261003")
MAX_OBJECTS = 100
MAX_BYTES = 512 * 1024 * 1024
MAX_MEMBERS = 20000
HASH = re.compile(r"[0-9a-f]{64}")
# Exact original incident producers; no bucket-wide or latest-run discovery.
HANDOFF_RUNS = {"261001": "36932674491", "261002": "37067138754", "261003": "37159099752"}


class InvalidObject(ValueError):
    """A bounded private object failed verification; messages are fixed labels."""


def validate_ocr_request(source_run_id="", date_folder="", expected_reports="", manifest_sha256=""):
    """Empty inputs retain the original incident inventory; partial inputs fail."""
    values = (source_run_id, date_folder, expected_reports, manifest_sha256)
    if values == ("", "", "", ""):
        return None
    if (not all(isinstance(value, str) for value in values)
            or not re.fullmatch(r"[1-9][0-9]{0,19}", source_run_id)
            or not re.fullmatch(r"[1-9][0-9]{0,3}", expected_reports)
            or int(expected_reports) > 1000 or not HASH.fullmatch(manifest_sha256)):
        raise InvalidObject("ocr_request_invalid")
    from recover_durable_mineru_sources import exact_date, RecoveryError
    try:
        exact_date(date_folder)
    except RecoveryError:
        raise InvalidObject("ocr_request_invalid") from None
    return {"source_run_id": source_run_id, "date_folder": date_folder,
            "expected_reports": int(expected_reports), "manifest_sha256": manifest_sha256}


def validate_ocr_producer(producer, request, repository):
    from recover_durable_mineru_sources import check_producer, RecoveryError
    if (not isinstance(repository, str) or not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository)
            or not isinstance(producer, dict) or producer.get("status") != "completed"
            or producer.get("event") not in {"schedule", "workflow_dispatch"}
            or (producer.get("head_repository") or {}).get("full_name") != repository):
        raise InvalidObject("ocr_producer_invalid")
    try:
        return check_producer(producer, request["source_run_id"], repository)
    except RecoveryError:
        raise InvalidObject("ocr_producer_invalid") from None


def inspect_object_presence(client, bucket, key):
    """Read metadata once; only a definite missing response means absence."""
    present, head = r2_object_exists(client, bucket, key)
    row = {"present": present, "object_count": int(present), "archive_bytes_verified": False,
           "size_bytes": 0, "archive_sha256": None}
    if present:
        row["size_bytes"] = bounded_size(head)
        checksum = (head.get("Metadata") or {}).get("sha256")
        if not isinstance(checksum, str) or not HASH.fullmatch(checksum):
            raise InvalidObject("ocr_archive_metadata_invalid")
        row["archive_sha256"] = checksum
    return row


def inspect_ocr_presence(client, bucket, manifest, producer, request, repository):
    """Validate source bytes, then HEAD its exact cache and temporary handoff.

    Presence and stored archive metadata do not prove OCR completeness. Never
    download/extract the checkpoint or admit it for article generation here.
    """
    from private_market_ocr_checkpoint import checkpoint_key
    from recover_durable_mineru_sources import MAX_RECEIPT, RecoveryError
    validate_ocr_producer(producer, request, repository)
    if (not manifest or manifest.is_symlink() or not manifest.is_file()
            or not 0 < manifest.stat().st_size <= MAX_RECEIPT):
        raise InvalidObject("ocr_manifest_invalid")
    raw = manifest.read_bytes()
    if hashlib.sha256(raw).hexdigest() != request["manifest_sha256"]:
        raise InvalidObject("ocr_manifest_sha256_mismatch")
    try:
        key = checkpoint_key(manifest, request["date_folder"], request["expected_reports"])
    except RecoveryError:
        raise InvalidObject("ocr_manifest_binding_invalid") from None
    # Require the derivation to consume exactly the bytes whose hash was pinned.
    if manifest.read_bytes() != raw:
        raise InvalidObject("ocr_manifest_changed")
    row = {**request, "source_binding_verified": True,
           "checkpoint_identity": Path(key).name.removesuffix(".tar.gz"),
           **inspect_object_presence(client, bucket, key)}
    # A completed source handoff is distinct from the durable model/OCR memo.
    # Bind this lookup to the same exact Daily run/date; never list alternatives.
    handoff_key = (f"_private-workflow-handoff/market-ocr-synthesis/{request['source_run_id']}/"
                   f"{request['date_folder']}/shard_0.tar.gz")
    source_handoff = inspect_object_presence(client, bucket, handoff_key)
    return {"schema_version": 1, "mode": "ocr-presence", "success": True, "provider_posts": 0,
            "object_writes": 0, "object_deletions": 0, "ocr_checkpoint": row,
            "ocr_source_handoff": source_handoff}


class BoundedBody:
    def __init__(self, body, limit):
        self.body, self.limit, self.count = body, limit, 0

    def read(self, size=-1):
        remaining = self.limit + 1 - self.count
        chunk = self.body.read(remaining if size < 0 else min(size, remaining))
        self.count += len(chunk)
        if self.count > self.limit:
            raise InvalidObject("object_size_limit")
        return chunk

    def close(self):
        close = getattr(self.body, "close", None)
        if callable(close):
            close()


def build_client():
    import boto3
    from botocore.config import Config
    return boto3.client("s3", endpoint_url=f"https://{handoff.require_env('R2_ACCOUNT_ID')}.r2.cloudflarestorage.com",
                        aws_access_key_id=handoff.require_env("R2_ACCESS_KEY_ID"),
                        aws_secret_access_key=handoff.require_env("R2_SECRET_ACCESS_KEY"), region_name="auto",
                        config=Config(retries={"total_max_attempts": 1}, connect_timeout=15, read_timeout=60))


def bounded_size(head: dict, limit: int = MAX_BYTES) -> int:
    size = head.get("ContentLength")
    if type(size) is not int or not 0 < size <= limit:
        raise InvalidObject("object_size_limit")
    return size


class ReadOnlyClient:
    """Supply the existing handoff verifier with a bounded single GET downloader."""
    def __init__(self, client, pinned_head=None):
        self.client = client
        self.pinned_head = pinned_head

    def head_object(self, **kwargs):
        head = self.client.head_object(**kwargs)
        if self.pinned_head is not None and (head.get("ContentLength") != self.pinned_head.get("ContentLength")
                or (head.get("Metadata") or {}).get("sha256") != (self.pinned_head.get("Metadata") or {}).get("sha256")):
            raise InvalidObject("archive_changed")
        return head

    def get_object(self, **kwargs):
        response = self.client.get_object(**kwargs)
        body = response.get("Body")
        if body is None or not hasattr(body, "read"):
            raise InvalidObject("object_body")
        limit = 1024 * 1024 if kwargs["Key"].endswith(".json") else MAX_BYTES
        return {**response, "Body": BoundedBody(body, limit)}

    def download_file(self, bucket, key, filename):
        expected = bounded_size(self.head_object(Bucket=bucket, Key=key))
        response = self.get_object(Bucket=bucket, Key=key)
        body = response.get("Body")
        if body is None or not hasattr(body, "read"):
            raise InvalidObject("object_body")
        size = 0
        try:
            with open(filename, "wb") as output:
                while chunk := body.read(min(1024 * 1024, expected + 1 - size)):
                    size += len(chunk)
                    if size > expected:
                        raise InvalidObject("object_size_mismatch")
                    output.write(chunk)
        finally:
            close = getattr(body, "close", None)
            if callable(close):
                close()
        if size != expected:
            raise InvalidObject("object_size_mismatch")
        if hashlib.sha256(Path(filename).read_bytes()).hexdigest() != self.pinned_head["Metadata"]["sha256"]:
            raise InvalidObject("archive_hash_mismatch")
        # Safe extraction is also checked by download_directory. Bound expansion
        # before it extracts, including zero-sized-member bombs and special files.
        try:
            with tarfile.open(filename, "r:gz") as archive:
                expanded, seen = 0, set()
                for index, member in enumerate(archive, 1):
                    if index > MAX_MEMBERS or not (member.isfile() or member.isdir()):
                        raise InvalidObject("archive_member_limit")
                    expanded += member.size
                    if expanded > MAX_BYTES:
                        raise InvalidObject("archive_expansion_limit")
                    path = Path(member.name)
                    if path.is_absolute() or ".." in path.parts:
                        raise InvalidObject("archive_path")
                    if path in seen:
                        raise InvalidObject("archive_duplicate_member")
                    seen.add(path)
        except (tarfile.TarError, EOFError, OSError) as exc:
            raise InvalidObject("archive_format") from exc


def bounded_listing(client, bucket, prefixes):
    objects, truncated = [], False
    for prefix in prefixes:
        token, seen = None, set()
        while len(objects) < MAX_OBJECTS:
            options = {"Bucket": bucket, "Prefix": prefix, "MaxKeys": MAX_OBJECTS - len(objects)}
            if token:
                options["ContinuationToken"] = token
            response = client.list_objects_v2(**options)
            rows = response.get("Contents", [])
            if not isinstance(rows, list) or len(rows) > options["MaxKeys"]:
                raise InvalidObject("listing_contract")
            for row in rows:
                key = row.get("Key") if isinstance(row, dict) else None
                if not isinstance(key, str) or not key.startswith(prefix):
                    raise InvalidObject("listing_scope")
                objects.append(key)
            if not response.get("IsTruncated"):
                break
            token = response.get("NextContinuationToken")
            if not isinstance(token, str) or not token or token in seen:
                raise InvalidObject("listing_continuation")
            seen.add(token)
        else:
            truncated = True
            break
        if len(objects) == MAX_OBJECTS:
            # More exact prefixes remain uninspected even if this page is final.
            truncated = truncated or prefix != prefixes[-1]
            break
    return sorted(set(objects)), not truncated


def read_json(path: Path):
    if path.stat().st_size > 1024 * 1024:
        raise InvalidObject("json_size_limit")
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except (ValueError, UnicodeError) as exc:
        raise InvalidObject("json_format") from exc


def summarize_tree(root: Path):
    sources = list(root.rglob("source_mineru.md"))
    result = {"source_count": len(sources), "nonempty_source_count": 0, "status_count": 0,
              "report_binding_count": 0, "pdf_hash_binding_count": 0, "error_status_count": 0,
              "asset_file_count": 0, "frozen_source_manifest_present": False,
              "stored_checkpoint_identity": None, "checkpoint_complete": None,
              "current_source_binding_verified": False}
    checkpoint = root / "_generation_checkpoint.json"
    if checkpoint.is_file():
        metadata = read_json(checkpoint)
        if (not isinstance(metadata, dict) or metadata.get("version") != 1
                or not HASH.fullmatch(str(metadata.get("identity", "")))
                or type(metadata.get("complete")) is not bool):
            raise InvalidObject("checkpoint_metadata")
        result.update(stored_checkpoint_identity=metadata["identity"], checkpoint_complete=metadata["complete"])
    for source in sources:
        result["nonempty_source_count"] += int(source.stat().st_size > 0)
        status_path = source.parent / "status.json"
        if status_path.is_file():
            status = read_json(status_path)
            if not isinstance(status, dict):
                raise InvalidObject("report_status")
            result["status_count"] += 1
            result["report_binding_count"] += int(isinstance(status.get("source_pdf"), str) and bool(status["source_pdf"]))
            result["pdf_hash_binding_count"] += int(bool(HASH.fullmatch(str(status.get("original_pdf_sha256", "")))))
            result["error_status_count"] += int(bool(status.get("error")))
        assets = source.parent / "assets"
        if assets.is_dir():
            result["asset_file_count"] += sum(1 for path in assets.rglob("*") if path.is_file())
    # Presence is an inventory observation, not an authorization to reuse it.
    result["frozen_source_manifest_present"] = any(
        path.is_file() for name in ("selected_to_process_manifest.json", "selected_macro_pdfs.json", "selected-manifest.json", "source-manifest.json")
        for path in root.rglob(name))
    return result


def inspect_archive(client, bucket, key, date_key, ordinal):
    prefix = f"_workflow-cache/report-generation/v1/{date_key}/"
    generation = re.fullmatch(re.escape(prefix) + r"shard_(\d+)/([0-9a-f]{64})\.tar\.gz", key)
    row = {"ordinal": ordinal, "kind": "generation" if generation else "handoff", "verified": False}
    if generation:
        row.update(shard_index=int(generation[1]), object_identity=generation[2])
    try:
        head = client.head_object(Bucket=bucket, Key=key)
        size = bounded_size(head)
        digest = str((head.get("Metadata") or {}).get("sha256", ""))
        if not HASH.fullmatch(digest):
            raise InvalidObject("archive_hash_missing")
        row.update(size_bytes=size, archive_sha256=digest)
        with tempfile.TemporaryDirectory(prefix="r2-cache-inspect-") as temporary:
            root = Path(temporary) / "tree"
            try:
                handoff.download_directory(key, root, client=ReadOnlyClient(client, head), bucket=bucket)
            except RuntimeError as exc:
                raise InvalidObject("archive_verification") from exc
            row.update(summarize_tree(root))
            if generation and row["stored_checkpoint_identity"] != row["object_identity"]:
                raise InvalidObject("checkpoint_identity_mismatch")
        row["verified"] = True
    except InvalidObject as exc:
        row["category"] = str(exc)
    return row


def inspect_final_pdf(client, bucket, date_key):
    client = ReadOnlyClient(client)
    pdf_key, item_key = f"_market-views/pdfs/{date_key}.pdf", f"_market-views/items/{date_key}.json"
    pdf_exists, pdf_head = r2_object_exists(client, bucket, pdf_key)
    item_exists, item_head = r2_object_exists(client, bucket, item_key)
    result = {"pdf_present": pdf_exists, "item_present": item_exists,
              "pdf_bytes_verified": False, "pair_verified": False}
    try:
        if pdf_exists:
            bounded_size(pdf_head)
            if item_exists:
                bounded_size(item_head, 1024 * 1024)
                issue_date, _ = parse_issue_date(date_key)
                item = validate_existing_private_pair(client, bucket, pdf_key=pdf_key, item_key=item_key,
                    pdf_head=pdf_head, item_head=item_head, issue_date=issue_date, date_key=date_key,
                    filename=f"market_views_{date_key}.pdf")
                result.update(pdf_bytes_verified=True, pair_verified=True, size_bytes=item["size_bytes"], sha256=item["sha256"])
            else:
                verified = validate_existing_pdf_object(client, bucket, key=pdf_key, head=pdf_head, date_key=date_key)
                result.update(pdf_bytes_verified=True, **verified)
    except (InvalidObject, RuntimeError) as exc:
        result["category"] = str(exc) if isinstance(exc, InvalidObject) else "final_pdf_verification"
    return result


def inspect_cache(client, bucket):
    result = {"schema_version": 1, "success": False, "provider_posts": 0, "object_writes": 0,
              "object_deletions": 0, "dates": []}
    for date_key in DATES:
        row = {"date_key": date_key, "archives": []}
        result["dates"].append(row)
        row["final_pdf"] = inspect_final_pdf(client, bucket, date_key)
        prefix = f"_workflow-cache/report-generation/v1/{date_key}/"
        run = HANDOFF_RUNS.get(date_key)
        handoff_prefix = f"_private-workflow-handoff/xhs/{run}/{date_key}/" if run else None
        prefixes = [prefix] + ([handoff_prefix] if handoff_prefix else [])
        keys, row["listing_complete"] = bounded_listing(client, bucket, prefixes)
        row["listed_object_count"] = len(keys)
        candidates = [key for key in keys if re.fullmatch(re.escape(prefix) + r"shard_\d+/[0-9a-f]{64}\.tar\.gz", key)
                      or (handoff_prefix and re.fullmatch(re.escape(handoff_prefix) + r"shard_\d+\.tar\.gz", key))]
        row["ignored_object_count"] = len(keys) - len(candidates)
        for ordinal, key in enumerate(candidates):
            row["archives"].append(inspect_archive(client, bucket, key, date_key, ordinal))
    result["success"] = True
    return result


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--source-run-id", default="")
    parser.add_argument("--date-folder", default="")
    parser.add_argument("--expected-reports", default="")
    parser.add_argument("--manifest-sha256", default="")
    parser.add_argument("--manifest", type=Path)
    parser.add_argument("--producer-json", type=Path)
    args = parser.parse_args(argv)
    result = {"schema_version": 1, "success": False, "provider_posts": 0, "object_writes": 0,
              "object_deletions": 0, "dates": [], "category": "storage_read_failed"}
    # Helper logs and SDK errors can contain private keys, endpoints or filenames.
    with open(os.devnull, "w") as sink, redirect_stdout(sink), redirect_stderr(sink):
        try:
            request = validate_ocr_request(args.source_run_id, args.date_folder,
                                           args.expected_reports, args.manifest_sha256)
            if request is None:
                if args.manifest is not None or args.producer_json is not None:
                    raise InvalidObject("ocr_request_invalid")
                result = inspect_cache(build_client(), handoff.require_env("R2_BUCKET"))
            else:
                if not args.producer_json or args.producer_json.is_symlink() or not args.producer_json.is_file():
                    raise InvalidObject("ocr_producer_invalid")
                result = inspect_ocr_presence(build_client(), handoff.require_env("R2_BUCKET"), args.manifest,
                    read_json(args.producer_json), request, os.environ.get("GITHUB_REPOSITORY", ""))
        except InvalidObject as error:
            result["category"] = str(error)
        except Exception:
            pass
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, sort_keys=True, indent=2) + "\n", encoding="utf-8")
    print(f"Private R2 incident inventory: success={str(result['success']).lower()}")
    return 0 if result["success"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
