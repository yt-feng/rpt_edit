#!/usr/bin/env python3
"""Publish existing, report-bound processing outputs for the authenticated content API.

No parsing, translation, model call or customer email is performed here. The private
delivery namespace contains selected content, never entire workflow directories.
"""
from __future__ import annotations

import argparse
import gzip
import hashlib
import json
import math
import re
import shutil
import tarfile
import tempfile
import unicodedata
from datetime import datetime, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import unquote

PREFIX = "_customer-content-data/v1"
MAX_FILE = 64 * 1024 * 1024
MAX_JSON = 16 * 1024 * 1024
MAX_COMPRESSED = 1024 * 1024 * 1024
MAX_EXTRACTED = 4 * 1024 * 1024 * 1024
MAX_MEMBER = 256 * 1024 * 1024
MAX_MEMBERS = 50000
MAX_REPORT_BYTES = 512 * 1024 * 1024
ID_RE = re.compile(r"[a-f0-9]{24}")
HASH_RE = re.compile(r"[a-f0-9]{64}")
IMAGE_RE = re.compile(r"(?:source_image_\d+|fig[_-]?\d+|figure[_-]?\d+|[a-f0-9]{32,64})\.(?:png|jpe?g|webp)", re.I)
TEXT_FILES = {
    "source_mineru.md": ("text", "und"), "source_clean.md": ("text", "und"),
    "translated.md": ("translation", "zh"), "translated_en.md": ("translation", "en"),
    "wechat_article.md": ("article", "zh"), "wechat_article_en.md": ("article", "en"),
    "note.md": ("article", "zh"), "note_en.md": ("article", "en"),
    "zhihu_article.md": ("article", "zh"), "zhihu_article_en.md": ("article", "en"),
    "podcast_script.txt": ("text", "und"), "podcast_zh_script.txt": ("text", "zh"),
    "podcast_en_script.txt": ("text", "en"),
}
MIME = {".md": "text/markdown", ".txt": "text/plain", ".json": "application/json",
        ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".png": "image/png",
        ".webp": "image/webp", ".pdf": "application/pdf"}


def encoded(value: Any) -> bytes:
    return (json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n").encode()


def digest(value: bytes) -> str:
    return hashlib.sha256(value).hexdigest()


def date_iso(value: str) -> str:
    raw = value.replace("-", "")
    if re.fullmatch(r"\d{6}", raw):
        raw = "20" + raw
    parsed = datetime.strptime(raw, "%Y%m%d")
    return parsed.strftime("%Y-%m-%d")


def title_key(value: Any) -> str:
    name = Path(str(value or "")).name
    return re.sub(r"[\W_]+", "", unicodedata.normalize("NFKC", re.sub(r"\.pdf$", "", name, flags=re.I)).lower())


def catalog_dates(row: dict) -> set[str]:
    dates = set()
    extra = row.get("date_folders") if isinstance(row.get("date_folders"), list) else []
    for value in [row.get("date_folder"), *extra]:
        try:
            dates.add(date_iso(str(value)))
        except (ValueError, TypeError):
            pass
    return dates


def read_local(path: Path, maximum: int = MAX_JSON) -> dict:
    if not path.exists():
        return {}
    if path.is_symlink() or not path.is_file() or path.stat().st_size > maximum:
        raise ValueError("invalid_processing_metadata")
    value = json.loads(path.read_bytes())
    return value if isinstance(value, dict) else {}


def load_catalog(path: Path) -> list[dict]:
    value = read_local(path, 64 * 1024 * 1024)
    rows = value.get("items")
    if not isinstance(rows, list) or not rows or len(rows) > 100000 or any(
            not isinstance(row, dict) or not isinstance(row.get("id"), str) or not ID_RE.fullmatch(row["id"]) for row in rows):
        raise ValueError("invalid_current_catalog")
    if len({row["id"] for row in rows}) != len(rows):
        raise ValueError("invalid_current_catalog")
    return rows


def public_string(value: Any, limit: int = 1000) -> str:
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", value)[:limit] if isinstance(value, str) else ""


def translation_statuses(directory: Path) -> list[tuple[str, dict]]:
    result = []
    for filename, default in (("translation_status.json", "zh"), ("translation_status_en.json", "en")):
        status = read_local(directory / filename)
        if not status:
            continue
        raw = status.get("target_language", status.get("language", default))
        language = {"zh": "zh", "zh-Hans": "zh", "zh-CN": "zh", "en": "en", "en-US": "en", "en-GB": "en"}.get(raw) if isinstance(raw, str) else None
        if language is None or default == "en" and language != "en":
            raise ValueError("invalid_translation_language")
        result.append((language, status))
    return result


def report_binding(directory: Path, catalog: list[dict], date: str) -> tuple[dict, dict]:
    status = read_local(directory / "status.json")
    translations = translation_statuses(directory)
    translation = translations[0][1] if translations else {}
    title = Path(public_string(status.get("source_pdf"), 2048)).name
    title = re.sub(r"\.pdf$", "", title, flags=re.I) or public_string(translation.get("source_title"), 500)
    if not title:
        source = directory / "source_mineru.md"
        if source.is_file() and not source.is_symlink() and source.stat().st_size <= MAX_JSON:
            title = next((line.lstrip("# ").strip() for line in source.read_text(errors="replace").splitlines()[:100] if line.startswith("#")), "")
    title = title or directory.name
    matches = {row["id"]: row for row in catalog if ID_RE.fullmatch(str(row.get("id", ""))) and date in catalog_dates(row) and title_key(title)
               in {title_key(row.get(field)) for field in ("title", "filename", "title_zh", "title_en")}}
    # Only a unique exact title AND source date bind to the catalog. Recurring
    # titles on other dates cannot inherit another report's permissions.
    if len(matches) == 1:
        chosen = next(iter(matches.values()))
        row = {key: public_string(chosen[key], 500) for key in ("id", "title", "title_zh", "title_en", "bank_name", "institution", "date_folder") if isinstance(chosen.get(key), str)}
        if type(chosen.get("page_count")) is int and 0 <= chosen["page_count"] <= 100000:
            row["page_count"] = chosen["page_count"]
    else:
        row = {"id": digest(f"customer-processed-v1:{date}:{title_key(title)}".encode())[:24],
               "title": title[:500], "date_folder": date.replace("-", "")[2:], "source": "processed", "available": False}
    untranslated = translation.get("untranslated_unit_count")
    metadata = {"report_id": row["id"], "title": row.get("title", title), "date": date,
                "extraction_method": "mineru" if status.get("mineru_state") == "done" else "stored_text",
                "translation_language": translations[0][0] if translations else "",
                "translation_languages": sorted({language for language, _ in translations}),
                "translation_notice": public_string(translation.get("translation_notice"), 500),
                "untranslated_unit_count": untranslated if type(untranslated) is int and 0 <= untranslated <= 100000 else 0}
    return row, metadata


def image_reference(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    value = unquote(value.strip().strip("<>"))
    if not value or re.search(r"[\x00-\x20\\:#?]", value):
        return ""
    path = PurePosixPath(value)
    if path.is_absolute() or ".." in path.parts:
        return ""
    return path.as_posix()


def rewrite_images(markdown: str, aliases: dict[str, str], tokens: dict[str, str]) -> str:
    definitions = {match[1].casefold(): match[2] for match in re.finditer(r"(?m)^ {0,3}\[([^]\n]+)\]:[ \t]*(\S+).*$", markdown)}
    referenced = set()
    def reference_image(match: re.Match) -> str:
        identifier = (match[2] or match[1]).casefold()
        referenced.add(identifier)
        filename = aliases.get(image_reference(definitions.get(identifier)))
        return f"![{match[1]}]({filename})" if filename else match[1]
    markdown = re.sub(r"!\[([^]\n]*)\]\[([^]\n]*)\]", reference_image, markdown)
    markdown = re.sub(r"(?m)^ {0,3}\[([^]\n]+)\]:[^\n]*(?:\n|$)",
                      lambda match: "" if match[1].casefold() in referenced else match[0], markdown)
    def image(match: re.Match) -> str:
        target = match[2].strip()
        # Markdown image titles are prose, never a way to carry a locator.
        target = re.sub(r'\s+["\'].*["\']\s*$', "", target)
        filename = aliases.get(image_reference(target))
        return f"![{match[1]}]({filename})" if filename else match[1]
    markdown = re.sub(r"!\[([^\]\n]*)\]\(([^)\n]*)\)", image, markdown)
    def html_image(match: re.Match) -> str:
        src = re.search(r'''\bsrc\s*=\s*(["'])(.*?)\1''', match[0], re.I | re.S)
        filename = aliases.get(image_reference(src[2])) if src else None
        return f"![]({filename})" if filename else ""
    markdown = re.sub(r"<img\b[^>]*>", html_image, markdown, flags=re.I | re.S)
    for token, filename in tokens.items():
        markdown = markdown.replace(token, f"![]({filename})")
    return markdown


def number_list(value: Any, length: int, *, positive: bool = False) -> list | None:
    if not isinstance(value, list) or len(value) != length or any(
            type(item) not in (int, float) or not math.isfinite(item) or abs(item) > 10000000
            or positive and item <= 0 for item in value):
        return None
    return value


def figure_record(value: Any, aliases: dict[str, str]) -> dict:
    if not isinstance(value, dict):
        return {}
    result = {}
    for key in ("index", "page_idx", "block_index", "level"):
        if type(value.get(key)) is int and 0 <= value[key] <= 100000:
            result[key] = value[key]
    for key in ("kind", "type"):
        if value.get(key) in ("image", "table", "chart", "text", "title", "equation", "figure"):
            result[key] = value[key]
    for key in ("bbox", "body_bbox", "content_bbox"):
        if number_list(value.get(key), 4) is not None:
            result[key] = value[key]
    for key in ("caption", "text", "body_text"):
        if isinstance(value.get(key), str):
            result[key] = rewrite_images(public_string(value[key], 20000), aliases, {})
    for key in ("captions", "footnotes", "content_captions", "content_footnotes"):
        if not isinstance(value.get(key), list):
            continue
        items = []
        for item in value[key][:1000]:
            if isinstance(item, str):
                items.append(rewrite_images(public_string(item, 2000), aliases, {}))
            elif isinstance(item, dict) and isinstance(item.get("text"), str):
                projected = {"text": rewrite_images(public_string(item["text"], 2000), aliases, {})}
                if number_list(item.get("bbox"), 4) is not None:
                    projected["bbox"] = item["bbox"]
                items.append(projected)
        result[key] = items
    return result


def content_files(directory: Path) -> list[tuple[str, str, str, bytes]]:
    images, aliases, tokens = {}, {}, {}
    image_bytes = 0
    for assets in (directory / "assets", directory / "images"):
        if assets.is_symlink():
            raise ValueError("symlink_content_directory")
        if not assets.is_dir():
            continue
        for path in sorted(assets.iterdir()):
            if not IMAGE_RE.fullmatch(path.name):
                continue
            if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_FILE:
                raise ValueError("invalid_image")
            raw = path.read_bytes()
            if not raw:
                continue
            if path.name in images and images[path.name] != raw:
                raise ValueError("ambiguous_artifact_filename")
            if path.name not in images:
                image_bytes += len(raw)
                if image_bytes > MAX_REPORT_BYTES or len(images) >= 1990:
                    raise ValueError("report_content_too_large")
                images[path.name] = raw
            aliases[path.relative_to(directory).as_posix()] = path.name
            aliases[path.name] = path.name

    figure_map = read_local(directory / "source_figure_map.json")
    clean_assets, bound_aliases = [], {}
    raw_assets = figure_map.get("assets", [])
    if not isinstance(raw_assets, list) or len(raw_assets) > 2000:
        raise ValueError("invalid_figure_metadata")
    for row in raw_assets:
        if not isinstance(row, dict):
            continue
        filename = aliases.get(image_reference(row.get("path")))
        if not filename:
            continue
        sha = digest(images[filename])
        if row.get("sha256") != sha:
            raise ValueError("image_binding_mismatch")
        reference = image_reference(row.get("ref"))
        if reference:
            if reference in bound_aliases and bound_aliases[reference] != filename:
                raise ValueError("ambiguous_image_binding")
            # The authenticated crop can intentionally replace a delivered
            # provider thumbnail with a different filename and different bytes.
            bound_aliases[reference] = filename
            aliases[reference] = filename
        asset = {"filename": filename, "sha256": sha}
        if type(row.get("page_idx")) is int and 0 <= row["page_idx"] <= 100000:
            asset["page_number"] = row["page_idx"] + 1
        if number_list(row.get("pixel_size"), 2, positive=True) is not None:
            asset["pixel_size"] = row["pixel_size"]
        clean_assets.append(asset)

    clean_figures = []
    figure_manifest = directory / "figure_manifest.json"
    if figure_manifest.exists():
        if figure_manifest.is_symlink() or not figure_manifest.is_file() or figure_manifest.stat().st_size > MAX_JSON:
            raise ValueError("invalid_figure_manifest")
        raw_figures = json.loads(figure_manifest.read_bytes())
        if not isinstance(raw_figures, list) or len(raw_figures) > 2000:
            raise ValueError("invalid_figure_manifest")
        for row in raw_figures:
            if not isinstance(row, dict):
                continue
            filename = aliases.get(image_reference(row.get("relative_path"))) or aliases.get(image_reference(row.get("path")))
            token = row.get("token")
            if not filename or not isinstance(token, str) or not re.fullmatch(r"\[\[PORTAL_IMAGE_\d{3,5}\]\]", token):
                continue
            if token in tokens and tokens[token] != filename:
                raise ValueError("ambiguous_image_binding")
            tokens[token] = filename
            clean_figures.append({"token": token, "filename": filename})

    result = []
    for filename, (kind, language) in TEXT_FILES.items():
        path = directory / filename
        if not path.exists():
            continue
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_JSON:
            raise ValueError("invalid_content_file")
        raw = rewrite_images(path.read_text(encoding="utf-8"), aliases, tokens)
        if raw.strip():
            result.append((filename, kind, language, raw.encode()))
    result.extend((filename, "image", "und", raw) for filename, raw in images.items())
    if figure_map:
        metadata = figure_map.get("metadata") if isinstance(figure_map.get("metadata"), dict) else {}
        records, pages = metadata.get("records", []), metadata.get("pages", [])
        if not isinstance(records, list) or not isinstance(pages, list) or len(records) > 20000 or len(pages) > 10000:
            raise ValueError("invalid_figure_metadata")
        clean_pages = []
        for page in pages:
            if not isinstance(page, dict) or type(page.get("page_idx")) is not int or not 0 <= page["page_idx"] <= 100000:
                continue
            item = {"page_idx": page["page_idx"]}
            if number_list(page.get("provider_size"), 2, positive=True) is not None:
                item["page_size"] = page["provider_size"]
            blocks = page.get("text_blocks")
            if isinstance(blocks, list):
                item["text_blocks"] = [projected for block in blocks[:20000] if (projected := figure_record(block, aliases))]
            clean_pages.append(item)
        projected = {"records": [row for record in records if (row := figure_record(record, aliases))], "pages": clean_pages, "images": clean_assets}
        result.append(("figure-metadata.json", "metadata", "und", encoded(projected)))
    if figure_manifest.exists():
        result.append(("translation-figures.json", "metadata", "und", encoded({"images": clean_figures})))

    pdfs = set()
    for language, status in translation_statuses(directory):
        filename = status.get("pdf")
        if not filename:
            continue
        match = re.fullmatch(r"portal_translated_report_(?:(zh|en)_)?\d+\.pdf", filename) if isinstance(filename, str) else None
        if not match or match[1] and match[1] != language:
            raise ValueError("invalid_translation_pdf_binding")
        if filename in pdfs:
            raise ValueError("ambiguous_translation_pdf")
        pdfs.add(filename)
        path = directory / filename
        if not path.exists():
            continue  # Older handoffs intentionally omitted rendered PDFs.
        expected_markdown = "translated_en.md" if language == "en" else "translated.md"
        if status.get("translated_markdown", expected_markdown) != expected_markdown or not (directory / expected_markdown).is_file():
            raise ValueError("invalid_translation_pdf_binding")
        if path.is_symlink() or not path.is_file() or path.stat().st_size > MAX_FILE:
            raise ValueError("invalid_translation_pdf")
        raw = path.read_bytes()
        if not raw.startswith(b"%PDF-") or not re.search(rb"%%EOF[\x00\t\r\n ]*$", raw[-2048:]):
            raise ValueError("invalid_translation_pdf")
        result.append((filename, "pdf", language, raw))
    if len(result) >= 2000 or sum(len(row[3]) for row in result) > MAX_REPORT_BYTES or any(
            len(raw) > (MAX_JSON if MIME[Path(name).suffix.lower()].startswith(("text/", "application/json")) else MAX_FILE)
            for name, _kind, _language, raw in result):
        raise ValueError("report_content_too_large")
    return result


def report_directories(root: Path) -> list[Path]:
    root = root.resolve()
    directories = {path.parent for pattern in (*TEXT_FILES, "translation_status.json", "translation_status_en.json") for path in root.rglob(pattern)}
    result = []
    for directory in sorted(directories):
        if any(part in {"mineru_raw", ".git", ".translation_cache"} for part in directory.relative_to(root).parts):
            continue
        if directory.is_symlink() or root not in directory.resolve().parents and directory.resolve() != root:
            raise ValueError("symlink_content_directory")
        result.append(directory)
    return result


def remote_json(client: Any, bucket: str, key: str) -> tuple[dict | None, str]:
    try:
        response = client.get_object(Bucket=bucket, Key=key)
    except Exception as error:
        if str(getattr(error, "response", {}).get("Error", {}).get("Code", "")) in {"NoSuchKey", "404", "NotFound"}:
            return None, ""
        raise
    try:
        if int(response.get("ContentLength") or 0) > MAX_JSON:
            raise ValueError("published_manifest_too_large")
        raw = response["Body"].read(MAX_JSON + 1)
    finally:
        response["Body"].close()
    if len(raw) > MAX_JSON:
        raise ValueError("published_manifest_too_large")
    value = json.loads(raw)
    if not isinstance(value, dict):
        raise ValueError("invalid_published_manifest")
    return value, response["ETag"]


def collection(value: dict | None, field: str) -> dict[str, dict]:
    rows = (value or {}).get(field, [])
    if not isinstance(rows, list) or len(rows) > (2000 if field == "artifacts" else 100000):
        raise ValueError("invalid_published_manifest")
    result = {}
    pattern = HASH_RE if field == "artifacts" else ID_RE
    for row in rows:
        if not isinstance(row, dict) or not isinstance(row.get("id"), str) or not pattern.fullmatch(row["id"]) or row["id"] in result:
            raise ValueError("invalid_published_manifest")
        result[row["id"]] = row
    return result


def verify_collection(expected: dict, observed: dict | None, field: str) -> None:
    if not observed or observed.get("schema_version") != 1 or expected.get("report_id") != observed.get("report_id"):
        raise ValueError("publish_readback_failed")
    wanted, actual = collection(expected, field), collection(observed, field)
    for identifier, row in wanted.items():
        stored = actual.get(identifier)
        if field == "items" and stored:
            # Concurrent manifest publication can advance the timestamp of the
            # same report without removing this index entry or its identity.
            expected_time = row.get("processed_updated_at", "")
            actual_time = stored.get("processed_updated_at", "")
            row = {key: value for key, value in row.items() if key != "processed_updated_at"}
            stored = {key: value for key, value in stored.items() if key != "processed_updated_at"}
            if actual_time < expected_time:
                raise ValueError("publish_readback_failed")
        if row != stored:
            raise ValueError("publish_readback_failed")


def cas_json(client: Any, bucket: str, key: str, update: Any, field: str) -> dict:
    for _ in range(8):
        previous, etag = remote_json(client, bucket, key)
        value = update(previous)
        raw = encoded(value)
        if len(raw) > MAX_JSON:
            raise ValueError("published_manifest_too_large")
        try:
            client.put_object(Bucket=bucket, Key=key, Body=raw, ContentType="application/json",
                              CacheControl="private, no-store", **({"IfMatch": etag} if etag else {"IfNoneMatch": "*"}))
        except Exception as error:
            if str(getattr(error, "response", {}).get("Error", {}).get("Code", "")) in {"PreconditionFailed", "412", "ConditionalRequestConflict", "409"}:
                continue
            raise
        verified, _ = remote_json(client, bucket, key)
        # Permit unrelated concurrent additions, but require every entry from
        # this write, including hashes, sizes, MIME, and report/blob bindings.
        # A conflicting replacement is a failure, not a reason to overwrite it.
        verify_collection(value, verified, field)
        return value
    raise ValueError("publish_concurrent_conflict")


def publish_directory(client: Any, bucket: str, root: Path, catalog: list[dict], date: str,
                      *, seen_reports: set[str] | None = None) -> dict:
    now = datetime.now(timezone.utc).isoformat()
    reports: dict[str, dict] = {}
    artifacts = 0
    for directory in report_directories(root):
        report, metadata = report_binding(directory, catalog, date)
        selected = content_files(directory)
        if not selected:
            continue
        metadata_name = "translation-metadata.json" if translation_statuses(directory) else "processing-metadata.json"
        selected.append((metadata_name, "metadata", "und", encoded(metadata)))
        descriptors = []
        seen_names = set()
        for filename, kind, language, raw in selected:
            identity = (filename, kind, language)
            if identity in seen_names:
                raise ValueError("ambiguous_artifact_filename")
            seen_names.add(identity)
            sha = digest(raw)
            ext = Path(filename).suffix.lower().replace(".jpeg", ".jpg")
            key = f"{PREFIX}/blobs/{report['id']}/{sha}{ext}"
            client.put_object(Bucket=bucket, Key=key, Body=raw, ContentType=MIME[Path(filename).suffix.lower()],
                              CacheControl="private, max-age=31536000, immutable", Metadata={"sha256": sha})
            check = client.get_object(Bucket=bucket, Key=key)
            try:
                if (check.get("ContentLength") != len(raw) or (check.get("Metadata") or {}).get("sha256") != sha
                        or check.get("ContentType") != MIME[Path(filename).suffix.lower()]
                        or digest(check["Body"].read(MAX_FILE + 1)) != sha):
                    raise ValueError("artifact_readback_failed")
            finally:
                check["Body"].close()
            descriptors.append({"id": digest(f"{kind}:{language}:{filename}".encode()), "kind": kind,
                                "language": language, "filename": filename, "size": len(raw),
                                "sha256": sha, "mime_type": MIME[Path(filename).suffix.lower()], "object_key": key})

        def merge_manifest(previous: dict | None) -> dict:
            if previous and (previous.get("schema_version") != 1 or previous.get("report_id") != report["id"]):
                raise ValueError("manifest_report_mismatch")
            existing = collection(previous, "artifacts")
            existing.update({row["id"]: row for row in descriptors})
            if len(existing) > 2000:
                raise ValueError("too_many_report_artifacts")
            return {"schema_version": 1, "report_id": report["id"], "updated_at": now, "artifacts": sorted(existing.values(), key=lambda row: row["id"])}

        cas_json(client, bucket, f"{PREFIX}/reports/{report['id']}/manifest.json", merge_manifest, "artifacts")
        reports[report["id"]] = {**report, "processed_updated_at": now}
        artifacts += len(descriptors)

    if reports:
        def merge_index(previous: dict | None) -> dict:
            if previous and previous.get("schema_version") != 1:
                raise ValueError("invalid_content_index")
            existing = collection(previous, "items")
            existing.update(reports)
            return {"schema_version": 1, "updated_at": now, "items": sorted(existing.values(), key=lambda row: row["id"])}
        cas_json(client, bucket, f"{PREFIX}/index.json", merge_index, "items")
    if seen_reports is not None:
        seen_reports.update(reports)
    return {"reports": len(reports), "artifacts": artifacts}


class DecompressedReader:
    """Bound every inflated byte, including PAX headers and tar padding."""
    def __init__(self, source: Any):
        self.source, self.count = source, 0

    def read(self, size: int = -1) -> bytes:
        size = min(64 * 1024, MAX_EXTRACTED - self.count + 1) if size < 0 else min(size, MAX_EXTRACTED - self.count + 1)
        chunk = self.source.read(size)
        self.count += len(chunk)
        if self.count > MAX_EXTRACTED:
            raise ValueError("handoff_expansion_too_large")
        return chunk


class BoundedTarInfo(tarfile.TarInfo):
    # tarfile parses extended headers before yielding a member. Bound them at
    # that earlier point, so a forged PAX size cannot allocate gigabytes first.
    def _proc_member(self, archive):
        extended = self.type in (tarfile.XHDTYPE, tarfile.XGLTYPE, tarfile.SOLARIS_XHDTYPE,
                                tarfile.GNUTYPE_LONGNAME, tarfile.GNUTYPE_LONGLINK)
        if self.size < 0 or self.size > (64 * 1024 if extended else MAX_MEMBER):
            raise ValueError("invalid_handoff_member")
        return super()._proc_member(archive)

    def _proc_sparse(self, *_args):
        raise ValueError("invalid_handoff_member")

    _proc_gnusparse_00 = _proc_sparse
    _proc_gnusparse_01 = _proc_sparse
    _proc_gnusparse_10 = _proc_sparse


def extract_bounded(archive_path: Path, destination: Path) -> int:
    if destination.exists() or destination.is_symlink():
        raise ValueError("handoff_destination_exists")
    destination.mkdir(parents=True)
    names, files = set(), 0
    try:
        with archive_path.open("rb") as compressed, gzip.GzipFile(fileobj=compressed) as expanded:
            bounded = DecompressedReader(expanded)
            with tarfile.open(fileobj=bounded, mode="r|", tarinfo=BoundedTarInfo) as archive:
                for member in archive:
                    if len(names) >= MAX_MEMBERS:
                        raise ValueError("handoff_too_many_members")
                    path = PurePosixPath(member.name)
                    if (not member.name or len(member.name) > 1024 or len(path.parts) > 30
                            or path.is_absolute() or ".." in path.parts or not path.parts
                            or re.search(r"[\x00-\x1f\x7f\\]", member.name)
                            or member.name in names or member.sparse is not None
                            or not (member.isfile() or member.isdir())
                            or member.size < 0 or member.size > MAX_MEMBER):
                        raise ValueError("invalid_handoff_member")
                    normalized = path.as_posix()
                    if normalized in names:
                        raise ValueError("invalid_handoff_member")
                    names.add(normalized)
                    target = destination.joinpath(*path.parts)
                    if member.isdir():
                        target.mkdir(parents=True, exist_ok=True)
                        continue
                    target.parent.mkdir(parents=True, exist_ok=True)
                    source = archive.extractfile(member)
                    if source is None:
                        raise ValueError("invalid_handoff_member")
                    remaining = member.size
                    with source, target.open("xb") as output:
                        while remaining:
                            block = source.read(min(64 * 1024, remaining))
                            if not block:
                                raise ValueError("incomplete_handoff_member")
                            output.write(block)
                            remaining -= len(block)
                    files += 1
            # tar ends before gzip does; verify its CRC and bound trailing data.
            while bounded.read(64 * 1024):
                pass
        if not files:
            raise ValueError("empty_source_handoff")
        return files
    except Exception:
        shutil.rmtree(destination, ignore_errors=True)
        raise


def download_bounded(client: Any, bucket: str, key: str, destination: Path) -> int:
    response = client.get_object(Bucket=bucket, Key=key)
    body = response["Body"]
    try:
        length = response.get("ContentLength")
        expected = (response.get("Metadata") or {}).get("sha256", "")
        if type(length) is not int or not 0 < length <= MAX_COMPRESSED or not isinstance(expected, str) or not HASH_RE.fullmatch(expected):
            raise ValueError("invalid_handoff_identity")
        with tempfile.TemporaryDirectory(prefix="customer-api-archive-") as temp:
            archive = Path(temp) / "payload.tar.gz"
            received, checksum = 0, hashlib.sha256()
            with archive.open("xb") as output:
                while True:
                    block = body.read(min(64 * 1024, MAX_COMPRESSED - received + 1))
                    if not block:
                        break
                    received += len(block)
                    if received > MAX_COMPRESSED or received > length:
                        raise ValueError("handoff_too_large")
                    checksum.update(block)
                    output.write(block)
            if received != length or checksum.hexdigest() != expected:
                raise ValueError("handoff_identity_mismatch")
            return extract_bounded(archive, destination)
    finally:
        body.close()


def publish_run(client: Any, bucket: str, run_id: str, catalog: list[dict], date_filter: str = "") -> dict:
    if not re.fullmatch(r"[1-9][0-9]{0,19}", run_id):
        raise ValueError("invalid_source_run")
    keys = []
    for family in ("xhs", "xhs-recovery", "mineru-market-sources"):
        prefix = f"_private-workflow-handoff/{family}/{run_id}/"
        response = client.list_objects_v2(Bucket=bucket, Prefix=prefix, MaxKeys=1000)
        if response.get("IsTruncated"):
            raise ValueError("source_run_inventory_too_large")
        for row in response.get("Contents", []):
            key = row["Key"]
            match = re.fullmatch(re.escape(prefix) + r"(\d{6})(?:/[a-f0-9]{64})?/(?:shard_\d+|translated_\d+)\.tar\.gz", key)
            if match and (not date_filter or date_iso(match[1]) == date_filter):
                if type(row.get("Size")) is not int or not 0 < row["Size"] <= MAX_COMPRESSED:
                    raise ValueError("handoff_too_large")
                keys.append((key, date_iso(match[1])))
    if not keys:
        raise ValueError("no_completed_source_handoffs")
    if len(keys) > 100:
        raise ValueError("source_run_inventory_too_large")
    seen_reports: set[str] = set()
    summary = {"handoffs": len(keys), "unique_reports": 0, "report_publications": 0, "artifact_publications": 0}
    for key, date in sorted(keys):
        # Do not accumulate up to 100 expanded source archives on runner disk.
        with tempfile.TemporaryDirectory(prefix="customer-api-publish-") as temp:
            directory = Path(temp) / "source"
            download_bounded(client, bucket, key, directory)
            result = publish_directory(client, bucket, directory, catalog, date, seen_reports=seen_reports)
            summary["report_publications"] += result["reports"]
            summary["artifact_publications"] += result["artifacts"]
    summary["unique_reports"] = len(seen_reports)
    return summary


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    inputs = parser.add_mutually_exclusive_group(required=True)
    inputs.add_argument("--source-root", type=Path)
    inputs.add_argument("--source-run-id")
    parser.add_argument("--date", default="")
    parser.add_argument("--catalog", type=Path, default=Path("portal_suite/data/catalog.json"))
    args = parser.parse_args()
    from private_workflow_handoff import build_r2_client, r2_bucket
    client, bucket = build_r2_client(), r2_bucket()
    catalog = load_catalog(args.catalog)
    date = date_iso(args.date) if args.date else ""
    if args.source_root:
        if not date:
            parser.error("--date is required with --source-root")
        result = publish_directory(client, bucket, args.source_root, catalog, date)
    else:
        result = publish_run(client, bucket, args.source_run_id, catalog, date)
    print(json.dumps(result, sort_keys=True))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
