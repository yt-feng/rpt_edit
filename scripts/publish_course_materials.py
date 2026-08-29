#!/usr/bin/env python3
"""Publish the curated KCDesk course PDF set from private storage to R2.

The public manifest owns display metadata and exact content digests. Source
paths and WebDAV credentials remain deployment secrets. Every PDF is verified
before the first R2 write; the stable private manifest is committed last.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import tempfile
import time
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Iterable
from urllib.parse import quote, urlsplit


COURSE_ID = "str-01"
OBJECT_PREFIX = "_course-materials/v1"
MANIFEST_OBJECT_KEY = f"{OBJECT_PREFIX}/manifest.json"
EXPECTED_ITEM_COUNT = 20
EXPECTED_TOTAL_PAGES = 746
EXPECTED_TOTAL_BYTES = 21_902_439
MAX_ITEM_BYTES = 12 * 1024 * 1024
MAX_TOTAL_BYTES = 64 * 1024 * 1024
RETRYABLE_STATUS = {408, 425, 429, 500, 502, 503, 504}
ITEM_ID_RE = re.compile(r"maifu-(?:0[1-9]|1[0-9]|20)\Z")
SHA256_RE = re.compile(r"[0-9a-f]{64}\Z")
ALLOWED_TOP_LEVEL = frozenset({"schema_version", "course", "items"})
ALLOWED_COURSE_FIELDS = frozenset({"id", "category", "title"})
ALLOWED_ITEM_FIELDS = frozenset({
    "id", "source_filename", "title", "topic", "summary", "pages", "bytes",
    "sha256", "cover", "featured", "entities",
})


class PublishError(RuntimeError):
    """Raised when a release cannot be proven complete and immutable."""


@dataclass(frozen=True)
class Material:
    id: str
    source_filename: str
    title: str
    topic: str
    summary: str
    pages: int
    size: int
    sha256: str
    cover: str
    featured: bool
    entities: tuple[str, ...]

    @property
    def object_key(self) -> str:
        return f"{OBJECT_PREFIX}/{self.id}.pdf"


def _text(value: Any, field: str, limit: int) -> str:
    if not isinstance(value, str):
        raise PublishError(f"{field} must be a string")
    result = re.sub(r"\s+", " ", value).strip()
    if not result or len(result) > limit or any(ord(char) < 32 for char in result):
        raise PublishError(f"{field} is invalid")
    return result


def load_manifest(path: Path) -> tuple[dict[str, str], tuple[Material, ...]]:
    try:
        raw = json.loads(path.read_text(encoding="utf-8"))
    except (OSError, json.JSONDecodeError) as error:
        raise PublishError("course material manifest is unavailable or invalid") from error
    if not isinstance(raw, dict) or set(raw) != ALLOWED_TOP_LEVEL or raw.get("schema_version") != 1:
        raise PublishError("course material manifest schema is invalid")
    course = raw.get("course")
    if not isinstance(course, dict) or set(course) != ALLOWED_COURSE_FIELDS:
        raise PublishError("course metadata schema is invalid")
    clean_course = {
        "id": _text(course.get("id"), "course.id", 32),
        "category": _text(course.get("category"), "course.category", 80),
        "title": _text(course.get("title"), "course.title", 160),
    }
    if clean_course["id"] != COURSE_ID:
        raise PublishError("course id is invalid")
    rows = raw.get("items")
    if not isinstance(rows, list) or len(rows) != EXPECTED_ITEM_COUNT:
        raise PublishError("course material item count is invalid")
    materials: list[Material] = []
    seen_ids: set[str] = set()
    seen_sources: set[str] = set()
    seen_hashes: set[str] = set()
    for position, row in enumerate(rows, start=1):
        if not isinstance(row, dict) or set(row) != ALLOWED_ITEM_FIELDS:
            raise PublishError(f"course material row {position} schema is invalid")
        item_id = _text(row.get("id"), f"items[{position}].id", 32)
        if not ITEM_ID_RE.fullmatch(item_id) or item_id in seen_ids:
            raise PublishError(f"course material row {position} id is invalid")
        expected_id = f"maifu-{position:02d}"
        if item_id != expected_id:
            raise PublishError("course material ids must be complete and ordered")
        source_filename = _text(row.get("source_filename"), f"items[{position}].source_filename", 240)
        if source_filename != Path(source_filename).name or not source_filename.lower().endswith(".pdf"):
            raise PublishError(f"course material row {position} source filename is invalid")
        if source_filename in seen_sources:
            raise PublishError("course material source filenames must be unique")
        digest = _text(row.get("sha256"), f"items[{position}].sha256", 64).lower()
        if not SHA256_RE.fullmatch(digest) or digest in seen_hashes:
            raise PublishError(f"course material row {position} digest is invalid")
        pages = row.get("pages")
        size = row.get("bytes")
        if not isinstance(pages, int) or not 1 <= pages <= 500:
            raise PublishError(f"course material row {position} page count is invalid")
        if not isinstance(size, int) or not 5 <= size <= MAX_ITEM_BYTES:
            raise PublishError(f"course material row {position} byte size is invalid")
        cover = _text(row.get("cover"), f"items[{position}].cover", 180)
        if cover != f"assets/course-covers/{item_id}.webp":
            raise PublishError(f"course material row {position} cover path is invalid")
        if not isinstance(row.get("featured"), bool):
            raise PublishError(f"course material row {position} featured flag is invalid")
        entities = row.get("entities")
        if not isinstance(entities, list) or len(entities) > 6:
            raise PublishError(f"course material row {position} entities are invalid")
        clean_entities = tuple(_text(value, f"items[{position}].entities", 80) for value in entities)
        if len(set(clean_entities)) != len(clean_entities):
            raise PublishError(f"course material row {position} entities are duplicated")
        materials.append(Material(
            id=item_id,
            source_filename=source_filename,
            title=_text(row.get("title"), f"items[{position}].title", 180),
            topic=_text(row.get("topic"), f"items[{position}].topic", 80),
            summary=_text(row.get("summary"), f"items[{position}].summary", 360),
            pages=pages,
            size=size,
            sha256=digest,
            cover=cover,
            featured=bool(row["featured"]),
            entities=clean_entities,
        ))
        seen_ids.add(item_id)
        seen_sources.add(source_filename)
        seen_hashes.add(digest)
    if sum(item.pages for item in materials) != EXPECTED_TOTAL_PAGES:
        raise PublishError("course material total page count is invalid")
    total_bytes = sum(item.size for item in materials)
    if total_bytes != EXPECTED_TOTAL_BYTES or total_bytes > MAX_TOTAL_BYTES:
        raise PublishError("course material total byte size is invalid")
    if sum(item.featured for item in materials) != 6:
        raise PublishError("course material featured cover count is invalid")
    return clean_course, tuple(materials)


def _safe_remote_parts(source_root: str, filename: str) -> list[str]:
    parts = [part for part in source_root.strip("/").split("/") if part]
    if not parts or any(part in {".", ".."} or "\x00" in part for part in parts):
        raise PublishError("private source root is invalid")
    return [*parts, filename]


def _webdav_url(base_url: str, source_root: str, filename: str) -> str:
    parsed = urlsplit(base_url.strip())
    if parsed.scheme != "https" or not parsed.netloc or parsed.query or parsed.fragment:
        raise PublishError("WebDAV origin is invalid")
    root = base_url.rstrip("/") + "/"
    return root + "/".join(quote(part, safe="") for part in _safe_remote_parts(source_root, filename))


def download_webdav(session: Any, base_url: str, source_root: str, material: Material, destination: Path) -> None:
    url = _webdav_url(base_url, source_root, material.source_filename)
    last_error: Exception | None = None
    for attempt in range(1, 5):
        try:
            with session.get(url, stream=True, timeout=(20, 180)) as response:
                if response.status_code not in RETRYABLE_STATUS:
                    response.raise_for_status()
                    written = 0
                    hasher = hashlib.sha256()
                    with destination.open("wb") as handle:
                        for chunk in response.iter_content(chunk_size=1024 * 1024):
                            if not chunk:
                                continue
                            written += len(chunk)
                            if written > material.size or written > MAX_ITEM_BYTES:
                                raise PublishError(f"{material.id} download size is invalid")
                            hasher.update(chunk)
                            handle.write(chunk)
                    if written != material.size or hasher.hexdigest() != material.sha256:
                        raise PublishError(f"{material.id} content verification failed")
                    return
                last_error = PublishError(f"{material.id} source returned HTTP {response.status_code}")
        except PublishError:
            raise
        except Exception as error:  # requests errors are retried without echoing a private URL.
            last_error = error
        if attempt < 4:
            time.sleep(min(2 ** (attempt - 1), 8))
    raise PublishError(f"{material.id} source download failed") from last_error


def verify_pdf(path: Path, material: Material) -> None:
    try:
        from pypdf import PdfReader
        header = path.read_bytes()[:5]
        pages = len(PdfReader(str(path), strict=True).pages)
    except Exception as error:
        raise PublishError(f"{material.id} PDF validation failed") from error
    if header != b"%PDF-" or pages != material.pages:
        raise PublishError(f"{material.id} PDF page contract failed")


def build_r2_client() -> Any:
    try:
        import boto3
    except ImportError as error:
        raise PublishError("boto3 is required for R2 publishing") from error
    account_id = os.environ.get("R2_ACCOUNT_ID", "").strip()
    access_key = os.environ.get("R2_ACCESS_KEY_ID", "").strip()
    secret_key = os.environ.get("R2_SECRET_ACCESS_KEY", "").strip()
    if not account_id or not access_key or not secret_key:
        raise PublishError("R2 credentials are incomplete")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
    )


def _missing_object(error: Exception) -> bool:
    response = getattr(error, "response", {})
    code = str(response.get("Error", {}).get("Code", "")) if isinstance(response, dict) else ""
    status = response.get("ResponseMetadata", {}).get("HTTPStatusCode") if isinstance(response, dict) else None
    return code in {"404", "NoSuchKey", "NotFound"} or status == 404


def matching_head(client: Any, bucket: str, material: Material) -> bool:
    try:
        head = client.head_object(Bucket=bucket, Key=material.object_key)
    except Exception as error:
        if _missing_object(error):
            return False
        raise
    metadata = {str(key).lower(): str(value) for key, value in (head.get("Metadata") or {}).items()}
    return (
        int(head.get("ContentLength") or 0) == material.size
        and str(head.get("ContentType") or "").split(";", 1)[0].lower() == "application/pdf"
        and metadata.get("sha256") == material.sha256
        and metadata.get("material-id") == material.id
        and metadata.get("pages") == str(material.pages)
    )


def publish_material(client: Any, bucket: str, path: Path, material: Material, release: str) -> bool:
    if matching_head(client, bucket, material):
        return False
    with path.open("rb") as body:
        client.put_object(
            Bucket=bucket,
            Key=material.object_key,
            Body=body,
            ContentType="application/pdf",
            CacheControl="private, no-store",
            Metadata={
                "sha256": material.sha256,
                "material-id": material.id,
                "pages": str(material.pages),
                "release": release,
            },
        )
    if not matching_head(client, bucket, material):
        raise PublishError(f"{material.id} R2 verification failed")
    return True


def matching_private_manifest_head(client: Any, bucket: str, body: bytes, release: str) -> bool:
    try:
        head = client.head_object(Bucket=bucket, Key=MANIFEST_OBJECT_KEY)
    except Exception as error:
        if _missing_object(error):
            return False
        raise
    metadata = {str(key).lower(): str(value) for key, value in (head.get("Metadata") or {}).items()}
    return (
        int(head.get("ContentLength") or 0) == len(body)
        and str(head.get("ContentType") or "").split(";", 1)[0].lower() == "application/json"
        and metadata.get("release") == release
        and metadata.get("sha256") == hashlib.sha256(body).hexdigest()
    )


def private_manifest(course: dict[str, str], materials: Iterable[Material]) -> bytes:
    rows = [{
        "id": item.id,
        "title": item.title,
        "topic": item.topic,
        "pages": item.pages,
        "bytes": item.size,
        "sha256": item.sha256,
    } for item in materials]
    release = hashlib.sha256(json.dumps(rows, ensure_ascii=False, separators=(",", ":")).encode("utf-8")).hexdigest()
    return (json.dumps({
        "schema_version": 1,
        "course": course,
        "release": release,
        "item_count": len(rows),
        "total_pages": sum(row["pages"] for row in rows),
        "total_bytes": sum(row["bytes"] for row in rows),
        "items": rows,
    }, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n").encode("utf-8")


def run(args: argparse.Namespace) -> int:
    course, materials = load_manifest(Path(args.manifest))
    manifest_body = private_manifest(course, materials)
    release = json.loads(manifest_body)["release"]
    source_dir = Path(args.source_dir).resolve() if args.source_dir else None
    session = None
    if source_dir is None:
        import requests
        session = requests.Session()
        session.auth = (
            os.environ.get("JIANGUOYUN_WEBDAV_USERNAME", "").strip(),
            os.environ.get("JIANGUOYUN_WEBDAV_PASSWORD", "").strip(),
        )
        if not all(session.auth):
            raise PublishError("WebDAV credentials are incomplete")
    client = None if args.dry_run else build_r2_client()
    bucket = os.environ.get("R2_BUCKET", "").strip()
    if not args.dry_run and not bucket:
        raise PublishError("R2 bucket is unavailable")
    uploaded = 0
    reused = 0
    with tempfile.TemporaryDirectory(prefix="kcdesk-course-materials-") as temp:
        temp_root = Path(temp)
        verified_paths: dict[str, Path] = {}
        for material in materials:
            path = source_dir / material.source_filename if source_dir else temp_root / f"{material.id}.pdf"
            if source_dir:
                if not path.is_file() or path.stat().st_size != material.size:
                    raise PublishError(f"{material.id} local source is unavailable")
                if hashlib.sha256(path.read_bytes()).hexdigest() != material.sha256:
                    raise PublishError(f"{material.id} local content verification failed")
            else:
                download_webdav(
                    session,
                    os.environ.get("JIANGUOYUN_WEBDAV_URL", ""),
                    os.environ.get("COURSE_MAIFU_WEBDAV_PATH", ""),
                    material,
                    path,
                )
            verify_pdf(path, material)
            verified_paths[material.id] = path
        if not args.dry_run:
            for material in materials:
                if publish_material(client, bucket, verified_paths[material.id], material, release):
                    uploaded += 1
                else:
                    reused += 1
    if not args.dry_run:
        client.put_object(
            Bucket=bucket,
            Key=MANIFEST_OBJECT_KEY,
            Body=manifest_body,
            ContentType="application/json; charset=utf-8",
            CacheControl="private, no-store",
            Metadata={"release": release, "sha256": hashlib.sha256(manifest_body).hexdigest()},
        )
        if not matching_private_manifest_head(client, bucket, manifest_body, release):
            raise PublishError("private course material manifest verification failed")
    print(
        f"course_materials_validated={len(materials)} total_pages={EXPECTED_TOTAL_PAGES} "
        f"total_bytes={EXPECTED_TOTAL_BYTES} uploaded={uploaded} reused={reused} "
        f"published={'false' if args.dry_run else 'true'} release={release}",
        flush=True,
    )
    return 0


def parser() -> argparse.ArgumentParser:
    value = argparse.ArgumentParser(description=__doc__)
    value.add_argument("--manifest", default="portal_suite/site_src/data/course-materials.json")
    value.add_argument("--source-dir", default="")
    value.add_argument("--dry-run", action="store_true")
    return value


def main() -> int:
    try:
        return run(parser().parse_args())
    except PublishError as error:
        print(f"course material publish failed: {error}", file=os.sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
