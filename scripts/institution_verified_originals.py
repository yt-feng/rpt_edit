"""Opt-in recovery of reviewed originals for exactly matching pending IMF items.

The manifest is an explicit, reviewed allowlist, not a discovery source. This
module only reads OriginalCache; it never writes cache, ledger, seen or pending
state. Its caller retains the ordinary downstream handoff/commit boundary.
"""
from __future__ import annotations

import contextlib
from datetime import datetime
import io
import json
import logging
import os
from pathlib import Path
import re
import tempfile
from urllib.parse import urlsplit

from institution_original_cache import MAX_PDF, MAX_TOTAL, OriginalCache, validate_binding, validate_payload
from institution_pending_intake import validate_item
from mineru_task_ledger import digest, encoded

MAX_MANIFEST = 512 * 1024
MAX_RECORDS = 100
HASH = re.compile(r"[a-f0-9]{64}")
RECOVERY_FIELDS = {"acquisition_method", "verified_original_manifest_sha256", "verified_original_binding_id",
                   "verified_original_receipt_sha256", "verified_original_pages", "verified_original_landing_url"}


class VerifiedOriginalError(ValueError):
    """Only caller-controlled diagnostic codes, never remote error material."""


def require(condition, code):
    if not condition:
        raise VerifiedOriginalError(code)


def official_url(value, *, pdf):
    if not isinstance(value, str) or len(value) > 4096 or any(ord(c) < 33 for c in value):
        return False
    try:
        url = urlsplit(value)
        path = url.path
        if (url.scheme != "https" or url.username is not None or url.password is not None
                or url.port not in (None, 443) or url.fragment or "\\" in value
                or "%" in path or any(part in {".", ".."} for part in path.split("/"))):
            return False
        if url.hostname == "www.elibrary.imf.org":
            if url.query and (pdf or not re.fullmatch(r"cid=[A-Za-z0-9-]{1,128}", url.query)):
                return False
            issue = (r"view/journals/(?P<series>[0-9]{3})/(?P<year>[0-9]{4})/(?P<issue>[0-9]{3})/"
                     r"(?:(?P=series)\.(?P=year)\.issue-(?P=issue)|article-A[0-9]{3})-[a-z]{2}")
            return bool(re.fullmatch((r"/downloadpdf/" if pdf else "/") + issue + (r"\.pdf" if pdf else r"\.xml"), path))
        if url.hostname == "www.imf.org":
            if url.query:
                return False
            return bool((path.startswith("/-/media/files/publications/") or path.startswith("/external/pubs/"))
                        and path.endswith((".pdf", ".ashx"))) if pdf else path.startswith("/en/publications/")
        return False
    except ValueError:
        return False


def _object(pairs):
    result = {}
    for key, value in pairs:
        require(key not in result, "verified_original_duplicate_json_key")
        result[key] = value
    return result


def _validate_record(record):
    require(isinstance(record, dict) and set(record) == {
        "item", "official_landing_url", "official_pdf_url", "doi", "sha256", "size", "pages", "binding", "verification"
    }, "verified_original_record_schema")
    try:
        validate_item(record["item"])
        validate_binding(record["binding"])
    except Exception:
        raise VerifiedOriginalError("verified_original_binding") from None
    require(bool(record["item"]["title"].strip()), "verified_original_title")
    require(official_url(record["official_landing_url"], pdf=False)
            and official_url(record["official_pdf_url"], pdf=True), "verified_original_official_url")
    landing, pdf = urlsplit(record["official_landing_url"]), urlsplit(record["official_pdf_url"])
    if pdf.hostname == "www.elibrary.imf.org":
        require(landing.hostname == pdf.hostname
                and pdf.path.removeprefix("/downloadpdf").removesuffix(".pdf") == landing.path.removesuffix(".xml"),
                "verified_original_official_url_pair")
    require(isinstance(record["doi"], str) and re.fullmatch(r"10\.[0-9]{4,9}/[A-Za-z0-9._;()/:-]{1,200}", record["doi"]),
            "verified_original_doi")
    binding = record["binding"]
    require(isinstance(record["sha256"], str) and HASH.fullmatch(record["sha256"])
            and type(record["size"]) is int and 1 <= record["size"] <= MAX_PDF
            and type(record["pages"]) is int and 1 <= record["pages"] <= 5000
            and record["sha256"] == binding["sha256"] and record["size"] == binding["size"],
            "verified_original_payload_metadata")
    review = record["verification"]
    require(isinstance(review, dict) and set(review) == {"method", "review", "receipt_sha256", "reviewed_at"}
            and review["method"] == "official_browser_download" and review["review"] == "approved"
            and isinstance(review["receipt_sha256"], str) and HASH.fullmatch(review["receipt_sha256"]),
            "verified_original_review")
    try:
        reviewed = datetime.fromisoformat(review["reviewed_at"].replace("Z", "+00:00"))
        require(reviewed.tzinfo is not None, "verified_original_review_date")
    except (AttributeError, ValueError, TypeError):
        raise VerifiedOriginalError("verified_original_review_date") from None


def _cache():
    from private_workflow_handoff import build_r2_client, r2_bucket
    return OriginalCache.single_attempt(build_r2_client(), r2_bucket())


def pdf_pages(payload):
    from pypdf import PdfReader
    # Malformed parser diagnostics can quote arbitrary input bytes.
    logger = logging.getLogger("pypdf")
    disabled = logger.disabled
    logger.disabled = True
    try:
        with contextlib.redirect_stderr(io.StringIO()):
            reader = PdfReader(io.BytesIO(payload), strict=True)
            require(not reader.is_encrypted, "verified_original_pdf_encrypted")
            return len(reader.pages)
    except VerifiedOriginalError:
        raise
    except Exception:
        raise VerifiedOriginalError("verified_original_pdf_invalid") from None
    finally:
        logger.disabled = disabled


class VerifiedOriginals:
    def __init__(self, path, *, cache_factory=None):
        path = Path(path)
        require(path.is_file() and not path.is_symlink() and path.stat().st_size <= MAX_MANIFEST,
                "verified_original_manifest_file")
        raw = path.read_bytes()
        try:
            data = json.loads(raw, object_pairs_hook=_object)
        except VerifiedOriginalError:
            raise
        except Exception:
            raise VerifiedOriginalError("verified_original_manifest_json") from None
        require(isinstance(data, dict) and set(data) == {"schema", "institution", "frozen_pending_sha256", "records"}
                and type(data["schema"]) is int and data["schema"] == 1 and data["institution"] == "imf"
                and isinstance(data["frozen_pending_sha256"], str) and HASH.fullmatch(data["frozen_pending_sha256"])
                and isinstance(data["records"], list) and 1 <= len(data["records"]) <= MAX_RECORDS,
                "verified_original_manifest_schema")
        # Review provenance only: the historical queue snapshot is not loaded
        # here, and retry counters change the current queue's file hash. Restore
        # enforces all seven immutable item fields against the admitted queue.
        self.frozen_pending_provenance_sha256 = data["frozen_pending_sha256"]
        self.records = {}
        hashes, sources, urls = set(), set(), set()
        total = 0
        for row in data["records"]:
            _validate_record(row)
            key = "imf:" + row["item"]["guid"]
            require(key not in self.records and row["sha256"] not in hashes
                    and row["binding"]["source"] not in sources and row["official_pdf_url"] not in urls,
                    "verified_original_duplicate_record")
            total += row["size"]
            require(total <= MAX_TOTAL, "verified_original_total_size")
            self.records[key] = row
            hashes.add(row["sha256"]); sources.add(row["binding"]["source"]); urls.add(row["official_pdf_url"])
        self.manifest_sha256 = digest(raw)
        self.cache_factory = cache_factory or _cache
        self.cache = None

    def contains(self, item):
        return "imf:" + item["guid"] in self.records

    def restore(self, item, filename, pending, destination, max_bytes):
        key = "imf:" + item["guid"]
        row = self.records[key]
        require(pending is not None and key in pending.initial_keys and key in pending.items
                and encoded(item) == encoded(row["item"]) == encoded(pending.items[key]["item"]),
                "verified_original_pending_identity")
        require(row["binding"]["source"] == filename and row["size"] <= max_bytes,
                "verified_original_selected_identity")
        try:
            if self.cache is None:
                self.cache = self.cache_factory()
            payload = self.cache.get(row["binding"])
            require(payload is not None, "verified_original_cache_missing")
            validate_payload(row["binding"], payload)
        except VerifiedOriginalError:
            raise
        except Exception:
            raise VerifiedOriginalError("verified_original_cache_invalid") from None
        require(pdf_pages(payload) == row["pages"], "verified_original_page_count")
        destination = Path(destination)
        require(destination.name == filename and not destination.is_symlink()
                and (not destination.exists() or destination.is_file()), "verified_original_destination")
        temporary = None
        try:
            with tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".verified-original-", delete=False) as stream:
                temporary = Path(stream.name)
                stream.write(payload)
                stream.flush()
                os.fsync(stream.fileno())
            temporary.replace(destination)
        finally:
            if temporary is not None:
                temporary.unlink(missing_ok=True)
        return {"pdf_url": row["official_pdf_url"], "acquisition_method": "verified_original_cache",
                "verified_original_manifest_sha256": self.manifest_sha256,
                "verified_original_binding_id": row["binding"]["id"],
                "verified_original_receipt_sha256": row["verification"]["receipt_sha256"],
                "verified_original_pages": row["pages"], "verified_original_landing_url": row["official_landing_url"]}
