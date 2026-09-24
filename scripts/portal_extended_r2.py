#!/usr/bin/env python3
"""Persist extended-locale source, checkpoints, and candidates in private R2.

The objects in this module are private build inputs and review evidence.  They
are never served by the public Edge Worker.  A candidate is uploaded before a
``ready`` receipt is written; publication code must require that receipt and
the matching source generation before it can assemble an inactive site.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import mimetypes
import os
import re
import sys
from pathlib import Path, PurePosixPath
from typing import Any, Iterable

from portal_extended_locales import ORIGIN, digest, stable_bytes, validate_corpus
from offline_translation import MODEL_ID, PROVIDER


SCHEMA_VERSION = 1
DEFAULT_PREFIX = "_extended-locales/v1"
MAX_SOURCE_BYTES = 32 * 1024 * 1024
MAX_CHECKPOINT_BYTES = 8 * 1024 * 1024
MAX_CANDIDATE_MANIFEST_BYTES = 2 * 1024 * 1024
MAX_CANDIDATE_PAGE_BYTES = 4 * 1024 * 1024
HEX64 = re.compile(r"^[0-9a-f]{64}$")
LOCALE = re.compile(r"^[a-z]{2,3}(?:-[A-Za-z]{4}|-[A-Z]{2})?$")
RETRYABLE_CODES = frozenset(
    {"408", "429", "500", "502", "503", "504", "slowdown", "throttling", "requestlimitexceeded"}
)


class R2StoreError(RuntimeError):
    """Base class for safe, user-facing R2 failures."""


class R2NotFound(R2StoreError):
    pass


class R2PermissionError(R2StoreError):
    pass


class R2TransportError(R2StoreError):
    pass


class R2IntegrityError(R2StoreError):
    pass


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise R2StoreError(f"Missing required R2 configuration: {name}")
    return value


def build_r2_client() -> Any:
    try:
        import boto3  # type: ignore
        from botocore.config import Config  # type: ignore
    except ImportError as error:  # pragma: no cover - Actions installs boto3
        raise R2StoreError("boto3 is required; install it with python -m pip install boto3") from error
    account_id = require_env("R2_ACCOUNT_ID")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=require_env("R2_ACCESS_KEY_ID"),
        aws_secret_access_key=require_env("R2_SECRET_ACCESS_KEY"),
        region_name="auto",
        config=Config(
            retries={"max_attempts": 8, "mode": "adaptive"},
            connect_timeout=10,
            read_timeout=60,
        ),
    )


def error_code(error: BaseException) -> str:
    response = getattr(error, "response", None)
    if isinstance(response, dict):
        details = response.get("Error")
        if isinstance(details, dict):
            return str(details.get("Code") or "").strip().lower()
    return ""


def error_status(error: BaseException) -> str:
    response = getattr(error, "response", None)
    if isinstance(response, dict):
        metadata = response.get("ResponseMetadata")
        if isinstance(metadata, dict):
            return str(metadata.get("HTTPStatusCode") or "").strip()
    return ""


def is_missing(error: BaseException) -> bool:
    return error_code(error) in {"404", "nosuchkey", "notfound", "nosuchbucket"}


def classify(error: BaseException, operation: str) -> R2StoreError:
    code = error_code(error)
    status = error_status(error)
    if is_missing(error):
        return R2NotFound(f"R2 object is missing during {operation}")
    if code in {"accessdenied", "invalidaccesskeyid", "signaturedoesnotmatch", "forbidden"} or status in {"401", "403"}:
        return R2PermissionError(f"R2 permission denied during {operation}")
    if code in RETRYABLE_CODES or status in RETRYABLE_CODES:
        return R2TransportError(f"R2 transient failure during {operation}: {code or status}")
    return R2TransportError(f"R2 request failed during {operation}: {code or status or type(error).__name__}")


def safe_part(value: str, *, label: str, pattern: re.Pattern[str] | None = None) -> str:
    value = str(value or "").strip()
    if not value or value in {".", ".."} or "/" in value or "\\" in value or "\x00" in value:
        raise R2StoreError(f"Unsafe R2 {label}")
    if pattern is not None and pattern.fullmatch(value) is None:
        raise R2StoreError(f"Invalid R2 {label}")
    return value


def safe_prefix(value: str) -> str:
    value = str(value or "").strip().strip("/")
    path = PurePosixPath(value)
    if not value or path.is_absolute() or ".." in path.parts or "\\" in value or "\x00" in value:
        raise R2StoreError("Unsafe R2 prefix")
    if len(value.encode("utf-8")) > 240 or any(part in {"", ".", ".."} for part in path.parts):
        raise R2StoreError("Invalid R2 prefix")
    return value


def safe_relative(value: str) -> str:
    value = str(value or "")
    path = PurePosixPath(value)
    if (
        not value
        or path.is_absolute()
        or path.as_posix() != value
        or "\\" in value
        or "\x00" in value
        or any(part in {"", ".", ".."} for part in path.parts)
    ):
        raise R2StoreError("Unsafe candidate relative path")
    return value


def source_generation(corpus: dict[str, Any]) -> str:
    try:
        validate_corpus(corpus, origin=ORIGIN)
    except Exception as error:
        raise R2StoreError("Source corpus failed its origin or digest validation") from error
    value = str(corpus.get("documents_sha256") or "")
    if HEX64.fullmatch(value) is None:
        raise R2StoreError("Source corpus generation is not a SHA-256")
    return value


def json_bytes(value: Any) -> bytes:
    return stable_bytes(value)


def sha256_bytes(body: bytes) -> str:
    return hashlib.sha256(body).hexdigest()


def content_type(key: str) -> str:
    guessed, _encoding = mimetypes.guess_type(key)
    if key.endswith(".json"):
        return "application/json; charset=utf-8"
    if key.endswith(".html"):
        return "text/html; charset=utf-8"
    return guessed or "application/octet-stream"


def checkpoint_is_valid(value: Any, locale: str, generation: str | None = None) -> None:
    if not isinstance(value, dict):
        raise R2IntegrityError("Checkpoint is not an object")
    if value.get("model") != MODEL_ID or value.get("locale") != locale:
        raise R2IntegrityError("Checkpoint model or locale identity does not match")
    if value.get("version") != "extended-static-v2":
        raise R2IntegrityError("Checkpoint version is unsupported")
    if generation is not None and value.get("source_generation") not in {None, generation}:
        raise R2IntegrityError("Checkpoint source generation does not match the requested corpus")
    if not isinstance(value.get("rows"), dict):
        raise R2IntegrityError("Checkpoint rows are invalid")


def partial_manifest_is_valid(value: Any, locale: str, generation: str) -> dict[str, Any]:
    if not isinstance(value, dict) or value.get("schema_version") != 1:
        raise R2IntegrityError("Candidate manifest schema is unsupported")
    if value.get("locale") != locale or value.get("origin") != ORIGIN:
        raise R2IntegrityError("Candidate locale or origin does not match")
    if value.get("provider") != PROVIDER or value.get("model") != MODEL_ID:
        raise R2IntegrityError("Candidate translation provenance does not match")
    if value.get("paid_provider_requests") != 0:
        raise R2IntegrityError("Candidate reports a paid provider request")
    if value.get("source_documents_sha256") != generation:
        raise R2IntegrityError("Candidate source generation does not match")
    if value.get("indexable") is not False:
        raise R2IntegrityError("Candidate must remain noindex until approved")
    if value.get("status") not in {"complete-candidate", "incomplete-candidate"}:
        raise R2IntegrityError("Candidate status is unsupported")
    pages = value.get("pages")
    if not isinstance(pages, list) or value.get("completed_page_count") != len(pages):
        raise R2IntegrityError("Candidate page count is inconsistent")
    if value.get("files_sha256") != digest(stable_bytes(pages)):
        raise R2IntegrityError("Candidate page manifest digest is invalid")
    if HEX64.fullmatch(str(value.get("files_sha256") or "")) is None:
        raise R2IntegrityError("Candidate id is invalid")
    for row in pages:
        if not isinstance(row, dict) or not isinstance(row.get("source_url"), str):
            raise R2IntegrityError("Candidate page record is invalid")
        safe_relative(str(row.get("path") or ""))
        if HEX64.fullmatch(str(row.get("sha256") or "")) is None:
            raise R2IntegrityError("Candidate page checksum is invalid")
        if not isinstance(row.get("bytes"), int) or not 0 < row["bytes"] <= MAX_CANDIDATE_PAGE_BYTES:
            raise R2IntegrityError("Candidate page byte count is invalid")
    return value


class R2Store:
    def __init__(self, client: Any, bucket: str, prefix: str = DEFAULT_PREFIX):
        self.client = client
        self.bucket = safe_part(bucket, label="bucket")
        self.prefix = safe_prefix(prefix)

    @classmethod
    def from_env(cls, prefix: str = DEFAULT_PREFIX) -> "R2Store":
        return cls(build_r2_client(), require_env("R2_BUCKET"), prefix)

    def key(self, *parts: str) -> str:
        checked = [safe_part(part, label="key component") for part in parts]
        return "/".join((self.prefix, *checked))

    def source_key(self, generation: str) -> str:
        return self.key("sources", safe_part(generation, label="source generation", pattern=HEX64), "corpus.json")

    def checkpoint_object_key(self, locale: str, generation: str, checksum: str) -> str:
        return self.key("checkpoints", safe_part(generation, label="source generation", pattern=HEX64),
                        safe_part(locale, label="locale", pattern=LOCALE), "objects",
                        f"sha256-{safe_part(checksum, label='checkpoint checksum', pattern=HEX64)}.json")

    def checkpoint_pointer_key(self, locale: str, generation: str) -> str:
        return self.key("checkpoints", safe_part(generation, label="source generation", pattern=HEX64),
                        safe_part(locale, label="locale", pattern=LOCALE), "latest.json")

    def candidate_root(self, locale: str, generation: str, candidate_id: str) -> str:
        return self.key("candidates", safe_part(generation, label="source generation", pattern=HEX64),
                        safe_part(locale, label="locale", pattern=LOCALE),
                        safe_part(candidate_id, label="candidate id", pattern=HEX64))

    def candidate_key(self, locale: str, generation: str, candidate_id: str, relative: str) -> str:
        return "/".join((self.candidate_root(locale, generation, candidate_id), safe_relative(relative)))

    def candidate_manifest_key(self, locale: str, generation: str, candidate_id: str) -> str:
        return self.candidate_key(locale, generation, candidate_id, "candidate-manifest.json")

    def candidate_ready_key(self, locale: str, generation: str, candidate_id: str) -> str:
        return self.candidate_key(locale, generation, candidate_id, "candidate-ready.json")

    def _put(self, key: str, body: bytes, *, metadata: dict[str, str], cache_control: str = "private, no-store") -> dict[str, Any]:
        if not body:
            raise R2IntegrityError(f"Refusing to persist empty R2 object: {key}")
        checksum = sha256_bytes(body)
        custom = {"sha256": checksum, **metadata}
        try:
            self.client.put_object(
                Bucket=self.bucket,
                Key=key,
                Body=body,
                ContentType=content_type(key),
                CacheControl=cache_control,
                Metadata=custom,
            )
            head = self.client.head_object(Bucket=self.bucket, Key=key)
        except Exception as error:
            raise classify(error, f"put {key}") from error
        self._verify_head(head, key, len(body), checksum)
        return {"key": key, "bytes": len(body), "sha256": checksum}

    def _get(self, key: str, *, maximum: int) -> bytes:
        try:
            head = self.client.head_object(Bucket=self.bucket, Key=key)
        except Exception as error:
            raise classify(error, f"head {key}") from error
        try:
            length = int(head.get("ContentLength") or 0)
        except (TypeError, ValueError) as error:
            raise R2IntegrityError(f"R2 object length is invalid: {key}") from error
        if length <= 0 or length > maximum:
            raise R2IntegrityError(f"R2 object length is outside the bound: {key}")
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=key)
            body = response["Body"].read(maximum + 1)
        except Exception as error:
            raise classify(error, f"get {key}") from error
        if len(body) != length or len(body) > maximum:
            raise R2IntegrityError(f"R2 object length changed during read: {key}")
        expected = str((head.get("Metadata") or {}).get("sha256") or "").lower()
        actual = sha256_bytes(body)
        if expected and expected != actual:
            raise R2IntegrityError(f"R2 object checksum mismatch: {key}")
        return body

    @staticmethod
    def _verify_head(head: dict[str, Any], key: str, expected_length: int, expected_checksum: str) -> None:
        actual_length = int(head.get("ContentLength") or 0)
        metadata = head.get("Metadata") or {}
        actual_checksum = str(metadata.get("sha256") or "").lower()
        if actual_length != expected_length or actual_checksum != expected_checksum:
            raise R2IntegrityError(f"R2 write verification failed: {key}")

    def put_source(self, corpus: dict[str, Any]) -> dict[str, Any]:
        generation = source_generation(corpus)
        body = json_bytes(corpus)
        if len(body) > MAX_SOURCE_BYTES:
            raise R2IntegrityError("Source corpus exceeds the R2 bound")
        key = self.source_key(generation)
        try:
            existing = self._get(key, maximum=MAX_SOURCE_BYTES)
        except R2NotFound:
            existing = None
        if existing is not None:
            if existing != body:
                raise R2IntegrityError("Existing R2 source generation differs from the requested corpus")
            return {"generation": generation, "key": key, "bytes": len(body), "sha256": sha256_bytes(body), "reused": True}
        result = self._put(key, body, metadata={"kind": "source-corpus", "generation": generation})
        return {"generation": generation, **result, "reused": False}

    def restore_source(self, generation: str, destination: Path) -> dict[str, Any]:
        generation = safe_part(generation, label="source generation", pattern=HEX64)
        body = self._get(self.source_key(generation), maximum=MAX_SOURCE_BYTES)
        try:
            corpus = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("R2 source corpus is not valid UTF-8 JSON") from error
        if source_generation(corpus) != generation:
            raise R2IntegrityError("R2 source corpus generation mismatch")
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_bytes(body)
        temporary.replace(destination)
        return {"generation": generation, "key": self.source_key(generation), "bytes": len(body), "sha256": sha256_bytes(body)}

    def put_checkpoint(self, locale: str, generation: str, checkpoint: Path) -> dict[str, Any]:
        locale = safe_part(locale, label="locale", pattern=LOCALE)
        generation = safe_part(generation, label="source generation", pattern=HEX64)
        body = checkpoint.read_bytes()
        if len(body) > MAX_CHECKPOINT_BYTES:
            raise R2IntegrityError("Checkpoint exceeds the R2 bound")
        try:
            value = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("Checkpoint is not valid UTF-8 JSON") from error
        checkpoint_is_valid(value, locale, generation)
        checksum = sha256_bytes(body)
        object_key = self.checkpoint_object_key(locale, generation, checksum)
        self._put(object_key, body, metadata={"kind": "translation-checkpoint", "locale": locale, "generation": generation})
        pointer = {
            "schema_version": SCHEMA_VERSION,
            "locale": locale,
            "source_generation": generation,
            "model": MODEL_ID,
            "provider": PROVIDER,
            "checkpoint_sha256": checksum,
            "checkpoint_bytes": len(body),
            "object_key": object_key,
        }
        pointer_body = json_bytes(pointer)
        pointer_key = self.checkpoint_pointer_key(locale, generation)
        self._put(pointer_key, pointer_body, metadata={"kind": "checkpoint-pointer", "locale": locale, "generation": generation})
        return {"locale": locale, "generation": generation, "object_key": object_key, "pointer_key": pointer_key,
                "bytes": len(body), "sha256": checksum}

    def restore_checkpoint(self, locale: str, generation: str, destination: Path) -> dict[str, Any]:
        locale = safe_part(locale, label="locale", pattern=LOCALE)
        generation = safe_part(generation, label="source generation", pattern=HEX64)
        pointer_key = self.checkpoint_pointer_key(locale, generation)
        try:
            pointer_body = self._get(pointer_key, maximum=256 * 1024)
        except R2NotFound:
            return {"present": False, "locale": locale, "generation": generation, "pointer_key": pointer_key}
        try:
            pointer = json.loads(pointer_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("R2 checkpoint pointer is invalid") from error
        expected_key = self.checkpoint_object_key(locale, generation, str(pointer.get("checkpoint_sha256") or ""))
        if (
            pointer.get("schema_version") != SCHEMA_VERSION
            or pointer.get("locale") != locale
            or pointer.get("source_generation") != generation
            or pointer.get("model") != MODEL_ID
            or pointer.get("provider") != PROVIDER
            or pointer.get("object_key") != expected_key
            or HEX64.fullmatch(str(pointer.get("checkpoint_sha256") or "")) is None
        ):
            raise R2IntegrityError("R2 checkpoint pointer identity is invalid")
        body = self._get(expected_key, maximum=MAX_CHECKPOINT_BYTES)
        if sha256_bytes(body) != pointer["checkpoint_sha256"]:
            raise R2IntegrityError("R2 checkpoint pointer checksum mismatch")
        try:
            value = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("R2 checkpoint object is invalid JSON") from error
        checkpoint_is_valid(value, locale, generation)
        destination.parent.mkdir(parents=True, exist_ok=True)
        temporary = destination.with_suffix(destination.suffix + ".tmp")
        temporary.write_bytes(body)
        temporary.replace(destination)
        return {"present": True, "locale": locale, "generation": generation, "pointer_key": pointer_key,
                "object_key": expected_key, "bytes": len(body), "sha256": sha256_bytes(body)}

    def upload_candidate(self, directory: Path, locale: str, generation: str) -> dict[str, Any]:
        locale = safe_part(locale, label="locale", pattern=LOCALE)
        generation = safe_part(generation, label="source generation", pattern=HEX64)
        manifest_path = directory / "candidate-manifest.json"
        if manifest_path.is_symlink() or not manifest_path.is_file() or manifest_path.stat().st_size > MAX_CANDIDATE_MANIFEST_BYTES:
            raise R2IntegrityError("Candidate manifest is missing or oversized")
        body = manifest_path.read_bytes()
        try:
            manifest = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("Candidate manifest is invalid JSON") from error
        partial_manifest_is_valid(manifest, locale, generation)
        candidate_id = str(manifest["files_sha256"])
        rows = manifest["pages"]
        uploaded = []
        for row in rows:
            relative = safe_relative(str(row["path"]))
            if not relative.startswith(locale + "/"):
                raise R2IntegrityError("Candidate path is outside its locale namespace")
            local = directory / relative
            if local.is_symlink() or not local.is_file() or local.stat().st_size != row["bytes"]:
                raise R2IntegrityError(f"Candidate page is missing or changed: {relative}")
            page = local.read_bytes()
            if len(page) > MAX_CANDIDATE_PAGE_BYTES or sha256_bytes(page) != row["sha256"]:
                raise R2IntegrityError(f"Candidate page checksum failed: {relative}")
            key = self.candidate_key(locale, generation, candidate_id, relative)
            uploaded.append(self._put(key, page, metadata={"kind": "candidate-page", "locale": locale,
                                                              "generation": generation, "candidate": candidate_id}))
        manifest_key = self.candidate_manifest_key(locale, generation, candidate_id)
        uploaded.append(self._put(manifest_key, body, metadata={"kind": "candidate-manifest", "locale": locale,
                                                                   "generation": generation, "candidate": candidate_id}))
        result: dict[str, Any] = {
            "schema_version": SCHEMA_VERSION,
            "locale": locale,
            "source_generation": generation,
            "candidate_id": candidate_id,
            "status": manifest["status"],
            "completed_page_count": len(rows),
            "uploaded_object_count": len(uploaded),
            "manifest_key": manifest_key,
            "manifest_sha256": sha256_bytes(body),
        }
        if manifest["status"] == "complete-candidate":
            ready = {**result, "ready": True, "indexable": False, "model": MODEL_ID, "provider": PROVIDER}
            ready_body = json_bytes(ready)
            ready_key = self.candidate_ready_key(locale, generation, candidate_id)
            self._put(ready_key, ready_body, metadata={"kind": "candidate-ready", "locale": locale,
                                                        "generation": generation, "candidate": candidate_id})
            result["ready"] = True
            result["ready_key"] = ready_key
        else:
            result["ready"] = False
        return result

    def restore_candidate(self, locale: str, generation: str, candidate_id: str, destination: Path) -> dict[str, Any]:
        locale = safe_part(locale, label="locale", pattern=LOCALE)
        generation = safe_part(generation, label="source generation", pattern=HEX64)
        candidate_id = safe_part(candidate_id, label="candidate id", pattern=HEX64)
        ready_key = self.candidate_ready_key(locale, generation, candidate_id)
        ready_body = self._get(ready_key, maximum=512 * 1024)
        try:
            ready = json.loads(ready_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("Candidate ready receipt is invalid") from error
        if (
            ready.get("schema_version") != SCHEMA_VERSION
            or ready.get("ready") is not True
            or ready.get("locale") != locale
            or ready.get("source_generation") != generation
            or ready.get("candidate_id") != candidate_id
            or ready.get("indexable") is not False
        ):
            raise R2IntegrityError("Candidate ready receipt identity is invalid")
        manifest_body = self._get(self.candidate_manifest_key(locale, generation, candidate_id), maximum=MAX_CANDIDATE_MANIFEST_BYTES)
        try:
            manifest = json.loads(manifest_body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as error:
            raise R2IntegrityError("Candidate manifest is invalid") from error
        partial_manifest_is_valid(manifest, locale, generation)
        if manifest["status"] != "complete-candidate" or manifest["files_sha256"] != candidate_id:
            raise R2IntegrityError("Candidate is not complete or its id changed")
        destination.mkdir(parents=True, exist_ok=True)
        (destination / "candidate-manifest.json").write_bytes(manifest_body)
        restored = 0
        for row in manifest["pages"]:
            relative = safe_relative(str(row["path"]))
            body = self._get(self.candidate_key(locale, generation, candidate_id, relative), maximum=MAX_CANDIDATE_PAGE_BYTES)
            if len(body) != row["bytes"] or sha256_bytes(body) != row["sha256"]:
                raise R2IntegrityError(f"Candidate restore checksum failed: {relative}")
            target = destination / relative
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_bytes(body)
            restored += 1
        return {"ready": True, "locale": locale, "source_generation": generation, "candidate_id": candidate_id,
                "completed_page_count": restored, "ready_key": ready_key}


def require_staging_prefix(value: str) -> str:
    prefix = safe_prefix(value)
    if not prefix.startswith("_extended-locales/staging/"):
        raise R2StoreError("R2 round-trip requires an isolated _extended-locales/staging/ prefix")
    return prefix


def roundtrip(store: R2Store, run_id: str) -> dict[str, Any]:
    run_id = safe_part(run_id, label="round-trip id", pattern=re.compile(r"^[A-Za-z0-9][A-Za-z0-9._-]{0,63}$"))
    key = store.key("roundtrip", run_id, "receipt.json")
    body = json_bytes({"schema_version": 1, "run_id": run_id, "purpose": "private-r2-roundtrip"})
    written = store._put(key, body, metadata={"kind": "roundtrip", "run": run_id})
    restored = store._get(key, maximum=64 * 1024)
    if restored != body:
        raise R2IntegrityError("R2 round-trip bytes did not match")
    return {"status": "passed", "key": key, "bytes": len(body), "sha256": sha256_bytes(body),
            "readback": True, "private_prefix": store.prefix}


def fake_permission_check() -> dict[str, str]:
    """Exercise the permission classification without touching a live bucket."""
    class Denied(Exception):
        response = {"Error": {"Code": "AccessDenied"}, "ResponseMetadata": {"HTTPStatusCode": 403}}

    error = classify(Denied(), "permission regression")
    if not isinstance(error, R2PermissionError):
        raise R2IntegrityError("Permission failures are not classified fail-closed")
    return {"permission_failure": type(error).__name__}


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    rt = sub.add_parser("roundtrip")
    rt.add_argument("--prefix", required=True)
    rt.add_argument("--run-id", default=os.environ.get("GITHUB_RUN_ID", "local"))
    source = sub.add_parser("put-source")
    source.add_argument("--prefix", default=DEFAULT_PREFIX)
    source.add_argument("--corpus", required=True, type=Path)
    restore_source_parser = sub.add_parser("restore-source")
    restore_source_parser.add_argument("--prefix", default=DEFAULT_PREFIX)
    restore_source_parser.add_argument("--generation", required=True)
    restore_source_parser.add_argument("--output", required=True, type=Path)
    checkpoint = sub.add_parser("put-checkpoint")
    checkpoint.add_argument("--prefix", default=DEFAULT_PREFIX)
    checkpoint.add_argument("--locale", required=True)
    checkpoint.add_argument("--generation", required=True)
    checkpoint.add_argument("--input", required=True, type=Path)
    restore_checkpoint_parser = sub.add_parser("restore-checkpoint")
    restore_checkpoint_parser.add_argument("--prefix", default=DEFAULT_PREFIX)
    restore_checkpoint_parser.add_argument("--locale", required=True)
    restore_checkpoint_parser.add_argument("--generation", required=True)
    restore_checkpoint_parser.add_argument("--output", required=True, type=Path)
    candidate = sub.add_parser("upload-candidate")
    candidate.add_argument("--prefix", default=DEFAULT_PREFIX)
    candidate.add_argument("--locale", required=True)
    candidate.add_argument("--generation", required=True)
    candidate.add_argument("--directory", required=True, type=Path)
    restore_candidate_parser = sub.add_parser("restore-candidate")
    restore_candidate_parser.add_argument("--prefix", default=DEFAULT_PREFIX)
    restore_candidate_parser.add_argument("--locale", required=True)
    restore_candidate_parser.add_argument("--generation", required=True)
    restore_candidate_parser.add_argument("--candidate-id", required=True)
    restore_candidate_parser.add_argument("--directory", required=True, type=Path)
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    prefix = require_staging_prefix(args.prefix) if args.command == "roundtrip" else safe_prefix(args.prefix)
    store = R2Store.from_env(prefix)
    if args.command == "roundtrip":
        result = {**roundtrip(store, args.run_id), **fake_permission_check()}
    elif args.command == "put-source":
        result = store.put_source(json.loads(args.corpus.read_text(encoding="utf-8")))
    elif args.command == "restore-source":
        result = store.restore_source(args.generation, args.output)
    elif args.command == "put-checkpoint":
        result = store.put_checkpoint(args.locale, args.generation, args.input)
    elif args.command == "restore-checkpoint":
        result = store.restore_checkpoint(args.locale, args.generation, args.output)
    elif args.command == "upload-candidate":
        result = store.upload_candidate(args.directory, args.locale, args.generation)
    elif args.command == "restore-candidate":
        result = store.restore_candidate(args.locale, args.generation, args.candidate_id, args.directory)
    else:  # pragma: no cover
        raise R2StoreError("Unsupported command")
    print(json.dumps(result, ensure_ascii=True, sort_keys=True))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except R2StoreError as error:
        print(f"ERROR: {error}", file=sys.stderr)
        raise SystemExit(1) from error
