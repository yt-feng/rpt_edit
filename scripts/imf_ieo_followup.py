"""Exact IEO implementation-plan originals from the official evaluation directory.

Ordinary bounded HTTPS only. The caller first binds the IMF source and its DOI
with imf_elibrary_resolver.bind_source; no Crossref or browser success is implied.
"""
from __future__ import annotations

import contextlib
from datetime import datetime
import hashlib
from html.parser import HTMLParser
import io
import os
from pathlib import Path
import re
import tempfile
import time
from urllib.parse import urljoin, urlsplit

from imf_elibrary_resolver import SourceIdentity, isbn_valid, source_url, title_key

DIRECTORY_URL = "https://ieo.imf.org/en/evaluations"
MAX_HTML = 2_000_000
MAX_PDF = 64 * 1024 * 1024
PROOF_FIELDS = {"schema", "source_guid", "source_url", "published", "title", "doi",
                "source_identity_sha256", "preview_sha256", "directory_url", "directory_sha256",
                "directory_status", "landing_url", "landing_sha256", "landing_status", "pdf_url",
                "sha256", "bytes", "pages", "pdf_status", "source_identity_verified", "transport"}
ERROR_CODES = {"ieo_followup_" + suffix for suffix in (
    "source_invalid", "not_applicable", "url_invalid", "html_invalid", "evaluation_ambiguous",
    "heading_mismatch", "section_ambiguous", "pdf_ambiguous", "http_rejected", "redirect_rejected",
    "response_bound", "request_failed", "request_timeout", "pdf_invalid", "pdf_title_mismatch",
    "destination_exists", "write_failed", "receipt_invalid")}


class FollowupError(ValueError):
    def __init__(self, category, *, http_status=None):
        self.category = category if category in ERROR_CODES else "ieo_followup_request_failed"
        # Callers may permit one bounded alternate route for an actual HTTP 403.
        # Never infer a status from exception text, malformed response values or
        # other failures; the public exception message remains a fixed category.
        self.http_status = (http_status if self.category == "ieo_followup_http_rejected"
                            and type(http_status) is int and 100 <= http_status <= 599 else None)
        super().__init__(self.category)


def require(value, category):
    if not value:
        raise FollowupError(category)


def evaluation_title(title):
    require(isinstance(title, str) and 0 < len(title) <= 4096
            and not re.search(r"[\x00-\x1f\x7f\ud800-\udfff]", title), "ieo_followup_not_applicable")
    match = re.fullmatch(
        r"Implementation Plan in Response to the Board[-\u2010\u2011\u2013\u2014]Endorsed Recommendations "
        r"from the IEO Evaluation on (.+)", title)
    require(match and len(title_key(match[1])) >= 10, "ieo_followup_not_applicable")
    return match[1]


def official_url(value, *, pdf=False, directory=False):
    try:
        parsed = urlsplit(value)
        require(isinstance(value, str) and len(value) <= 4096 and parsed.scheme == "https"
                and parsed.hostname == "ieo.imf.org" and parsed.username is None and parsed.password is None
                and parsed.port in (None, 443) and not parsed.query and not parsed.fragment
                and not re.search(r"[\s\\%]", value), "ieo_followup_url_invalid")
        pattern = (r"/-/media/ieo/files/evaluations/follow-up/[a-z0-9][a-z0-9_-]*\.pdf" if pdf else
                   r"/en/evaluations/completed/[a-z0-9][a-z0-9-]*")
        require(value == DIRECTORY_URL if directory else re.fullmatch(pattern, parsed.path), "ieo_followup_url_invalid")
        return value
    except (TypeError, ValueError, AttributeError):
        raise FollowupError("ieo_followup_url_invalid") from None


class _Node:
    def __init__(self, tag="", attrs=()):
        self.tag, self.attrs, self.children = tag, dict(attrs), []

    def text(self):
        return " ".join(child if isinstance(child, str) else child.text() for child in self.children)

    def walk(self, tag):
        for child in self.children:
            if isinstance(child, _Node):
                if child.tag == tag:
                    yield child
                yield from child.walk(tag)


class _Document(HTMLParser):
    VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}

    def __init__(self, raw):
        super().__init__(convert_charrefs=True)
        require(isinstance(raw, bytes) and 0 < len(raw) <= MAX_HTML, "ieo_followup_html_invalid")
        self.root, self.count = _Node(), 0
        self.stack = [self.root]
        try:
            self.feed(raw.decode("utf-8")); self.close()
        except (UnicodeError, RecursionError):
            raise FollowupError("ieo_followup_html_invalid") from None

    def handle_starttag(self, tag, attrs):
        self.count += 1
        require(self.count <= 30000 and len(self.stack) <= 100, "ieo_followup_html_invalid")
        node = _Node(tag, attrs); self.stack[-1].children.append(node)
        if tag not in self.VOID:
            self.stack.append(node)

    def handle_endtag(self, tag):
        for index in range(len(self.stack)-1, 0, -1):
            if self.stack[index].tag == tag:
                del self.stack[index:]; break

    def handle_data(self, data):
        if not any(node.tag in {"script", "style"} for node in self.stack):
            self.stack[-1].children.append(data)


def select_evaluation(raw, title):
    expected = title_key(evaluation_title(title))
    matches = {official_url(urljoin(DIRECTORY_URL, node.attrs.get("href", "")))
               for node in _Document(raw).root.walk("a") if title_key(node.text()) == expected}
    require(len(matches) == 1, "ieo_followup_evaluation_ambiguous")
    return next(iter(matches))


def select_followup(raw, landing_url, title):
    official_url(landing_url)
    doc = _Document(raw).root
    headings = list(doc.walk("h1"))
    require(len(headings) == 1 and title_key(headings[0].text()) == title_key(evaluation_title(title)),
            "ieo_followup_heading_mismatch")
    # The current official page uses an accordion <li> with its own h2. Restrict
    # discovery to that full section, excluding the main report and references.
    sections = [node for node in doc.walk("li") if "doc-view-section" in node.attrs.get("class", "").split()
                and [title_key(h.text()) for h in node.walk("h2")] == [title_key("Follow-up by the IMF")]]
    require(len(sections) == 1, "ieo_followup_section_ambiguous")
    matches = {official_url(urljoin(landing_url, node.attrs.get("href", "")), pdf=True)
               for node in sections[0].walk("a") if title_key(node.text()) == title_key(title)}
    require(len(matches) == 1, "ieo_followup_pdf_ambiguous")
    return next(iter(matches))


def _validate_source(proof):
    try:
        evaluation_title(proof["title"])
        require(source_url(proof["source_url"]) == proof["source_url"]
                and urlsplit(proof["source_url"]).path.lower().startswith("/en/publications/policy-papers/"),
                "ieo_followup_receipt_invalid")
        require(isinstance(proof["source_guid"], str) and 0 < len(proof["source_guid"]) <= 4096
                and not re.search(r"[\x00-\x1f\x7f\ud800-\udfff]", proof["source_guid"]), "ieo_followup_receipt_invalid")
        require(isinstance(proof["published"], str)
                and datetime.fromisoformat(proof["published"].replace("Z", "+00:00")).tzinfo is not None,
                "ieo_followup_receipt_invalid")
        doi = re.fullmatch(r"10\.5089/(97[89][0-9]{10})\.007", proof["doi"])
        require(doi and isbn_valid(doi[1]), "ieo_followup_receipt_invalid")
        for field in ("source_identity_sha256", "preview_sha256"):
            require(isinstance(proof[field], str) and re.fullmatch(r"[a-f0-9]{64}", proof[field]), "ieo_followup_source_invalid")
    except (TypeError, ValueError, KeyError, AttributeError):
        raise FollowupError("ieo_followup_source_invalid") from None


def validate_receipt(proof):
    """Strict standalone proof contract; caller also binds it to its manifest row.

    The DOI comes from the validated IMF source preview. It is not a claim that
    the PDF contains that DOI or that a Crossref request succeeded.
    """
    try:
        require(isinstance(proof, dict) and set(proof) == PROOF_FIELDS, "ieo_followup_receipt_invalid")
        require(type(proof["schema"]) is int and proof["schema"] == 1
                and proof["source_identity_verified"] is True
                and proof["transport"] == "official_https_ieo_followup", "ieo_followup_receipt_invalid")
        _validate_source(proof)
        for field in ("source_identity_sha256", "preview_sha256", "directory_sha256", "landing_sha256", "sha256"):
            require(isinstance(proof[field], str) and re.fullmatch(r"[a-f0-9]{64}", proof[field]), "ieo_followup_receipt_invalid")
        for field in ("directory_status", "landing_status", "pdf_status"):
            require(type(proof[field]) is int and proof[field] == 200, "ieo_followup_receipt_invalid")
        require(type(proof["bytes"]) is int and 0 < proof["bytes"] <= MAX_PDF
                and type(proof["pages"]) is int and 0 < proof["pages"] <= 5000, "ieo_followup_receipt_invalid")
        official_url(proof["directory_url"], directory=True)
        official_url(proof["landing_url"])
        official_url(proof["pdf_url"], pdf=True)
    except (TypeError, ValueError, KeyError, AttributeError):
        raise FollowupError("ieo_followup_receipt_invalid") from None


def _read(session, url, limit, timeout):
    response = None
    deadline = time.monotonic() + timeout
    try:
        response = session.get(url, timeout=(min(10, timeout), timeout), allow_redirects=False, stream=True)
        if type(response.status_code) is not int or response.status_code != 200:
            raise FollowupError("ieo_followup_http_rejected", http_status=response.status_code)
        require(response.url == url, "ieo_followup_redirect_rejected")
        data = bytearray()
        for chunk in response.iter_content(65536):
            require(time.monotonic() <= deadline, "ieo_followup_request_timeout")
            data.extend(chunk)
            require(len(data) <= limit, "ieo_followup_response_bound")
        return bytes(data)
    except FollowupError:
        raise
    except Exception:
        raise FollowupError("ieo_followup_request_failed") from None
    finally:
        if response is not None:
            try:
                response.close()
            except Exception:
                raise FollowupError("ieo_followup_request_failed") from None


def verify_pdf(data, title, max_bytes):
    require(isinstance(data, bytes) and 0 < len(data) <= max_bytes and data.startswith(b"%PDF-"), "ieo_followup_pdf_invalid")
    try:
        from pypdf import PdfReader
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            reader = PdfReader(io.BytesIO(data))
            require(not reader.is_encrypted and 0 < len(reader.pages) <= 5000, "ieo_followup_pdf_invalid")
            text = " ".join(page.extract_text() or "" for page in reader.pages[:3])
            pages = len(reader.pages)
    except Exception:
        raise FollowupError("ieo_followup_pdf_invalid") from None
    require(title_key(title) in title_key(text), "ieo_followup_pdf_title_mismatch")
    return {"sha256": hashlib.sha256(data).hexdigest(), "bytes": len(data), "pages": pages}


def download_followup(identity, session, dest, max_bytes, timeout):
    """Three GETs maximum, no retry/redirect; atomically publish one proven PDF."""
    require(isinstance(identity, SourceIdentity), "ieo_followup_source_invalid")
    evaluation_title(identity.title)
    require(type(max_bytes) is int and 0 < max_bytes <= MAX_PDF and type(timeout) in (int, float)
            and 0 < timeout <= 60, "ieo_followup_source_invalid")
    proof = dict(schema=1, source_guid=identity.guid, source_url=identity.source_url,
                 published=identity.published, title=identity.title, doi=identity.doi,
                 source_identity_sha256=identity.source_binding_sha256, preview_sha256=identity.preview_sha256,
                 directory_url=DIRECTORY_URL, directory_status=200, landing_status=200, pdf_status=200,
                 source_identity_verified=True, transport="official_https_ieo_followup")
    _validate_source(proof)
    destination = Path(dest)
    require(not destination.exists() and not destination.is_symlink(), "ieo_followup_destination_exists")
    directory = _read(session, DIRECTORY_URL, MAX_HTML, min(timeout, 30))
    landing_url = select_evaluation(directory, identity.title)
    landing = _read(session, landing_url, MAX_HTML, min(timeout, 30))
    pdf_url = select_followup(landing, landing_url, identity.title)
    data = _read(session, pdf_url, max_bytes, min(timeout, 30))
    proof.update(landing_url=landing_url, pdf_url=pdf_url,
                 directory_sha256=hashlib.sha256(directory).hexdigest(), landing_sha256=hashlib.sha256(landing).hexdigest(),
                 **verify_pdf(data, identity.title, max_bytes))
    validate_receipt(proof)
    temporary = None
    try:
        destination.parent.mkdir(parents=True, exist_ok=True)
        fd, temporary = tempfile.mkstemp(prefix=".imf-ieo-original-", dir=destination.parent)
        with os.fdopen(fd, "wb") as stream:
            stream.write(data); stream.flush(); os.fsync(stream.fileno())
        os.link(temporary, destination)  # Exclusive and atomic; never replace a prior original.
    except Exception:
        raise FollowupError("ieo_followup_write_failed") from None
    finally:
        if temporary is not None:
            try:
                Path(temporary).unlink(missing_ok=True)
            except OSError:
                pass  # A hidden temp cleanup must not orphan the published manifest entry.
    return proof
