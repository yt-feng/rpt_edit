"""Opt-in IMF official browser transport; no discovery, ledger or publication writes.

The caller supplies an imf_elibrary_resolver publication. A single cloud client
is initialized lazily per batch; each document uses its own ordinary browser.
"""
from __future__ import annotations

import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import selectors
import signal
import subprocess
import sys
import tempfile
import time
import unicodedata
from urllib.parse import urlsplit

import imf_cloud_client as client

VERSION = "1.14.3"
MAX_MESSAGE = 256 * 1024
RETRY_LANDING_STATUSES = frozenset({403, 429, 502, 503, 504})
SAFE_ENV = {"PATH", "HOME", "RUNNER_TEMP", "PLAYWRIGHT_PACKAGE_ROOT",
            "PLAYWRIGHT_BROWSERS_PATH", "LANG", "LC_ALL", "DISPLAY", "XAUTHORITY"}
PROOF_FIELDS = {"schema", "source_guid", "source_url", "landing_url", "pdf_url", "doi", "title",
                "identity_sha256", "crossref_sha256", "sha256", "bytes", "pages",
                "landing_status", "pdf_status", "source_identity_verified", "transport"}
PROOF_FIELDS_V2 = (PROOF_FIELDS - {"crossref_sha256"}) | {"metadata"}
ERROR_CODES = {"imf_browser_" + code for code in client.ERROR_CODES} | {
    "imf_browser_cloud_approval_required", "imf_browser_subscription_unavailable", "imf_browser_subscription_limit",
    "imf_browser_valid_vless_required", "imf_browser_invalid_listener", "imf_browser_phase_timeout",
    "imf_browser_process_stopped", "imf_browser_message_limit", "imf_browser_protocol_invalid",
    "imf_browser_pdf_bytes_changed", "imf_browser_size_bound_invalid", "imf_browser_pdf_size_invalid",
    "imf_browser_pdf_bytes_invalid", "imf_browser_pdf_pages_invalid", "imf_browser_pdf_parse_failed",
    "imf_browser_pdf_title_mismatch", "imf_browser_start_failed", "imf_browser_runtime_missing",
    "imf_browser_runtime_version", "imf_browser_subscription_missing", "imf_browser_connectivity_rejected",
    "imf_browser_not_enabled", "imf_browser_publication_invalid", "imf_browser_destination_exists",
    "imf_browser_page_not_ready", "imf_browser_page_identity_mismatch", "imf_browser_download_not_verified",
    "imf_browser_process_failed", "imf_browser_download_failed", "imf_browser_landing_http_rejected",
    "imf_browser_evidence_write_failed",
}


class BrowserDownloadError(ValueError):
    """Only fixed application codes; never wrap raw runtime/network errors."""
    def __init__(self, category):
        self.category = category if category in ERROR_CODES else "imf_browser_download_failed"
        super().__init__(self.category)


class _OriginalEdition404(Exception):
    """Internal single alternate-page transition after a real source HTTP404."""


class _LandingHttpRejected(BrowserDownloadError):
    """A typed HTTP rejection observed before the parent authorizes a PDF."""
    def __init__(self, status):
        super().__init__("imf_browser_landing_http_rejected")
        self.status = status


def publication_provenance(publication):
    """Keep exact-Crossref and independently bound official-preview proof distinct."""
    if "metadata" not in publication:
        digest = publication["crossref_sha256"]
        if not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest):
            raise ValueError
        return {"schema": 1, "crossref_sha256": digest}
    metadata = publication["metadata"]
    if type(metadata) is dict and metadata.get("method") == "official_fiscal_chapter":
        from imf_fiscal_chapter import validate_fiscal_chapter_metadata
        if (publication.get("crossref_sha256", "missing") is not None
                or metadata.get("preview_sha256") != publication.get("preview_sha256")
                or publication.get("full_title") != metadata.get("book_title", "") + ": " + metadata.get("book_subtitle", "")):
            raise ValueError
        result = validate_fiscal_chapter_metadata(metadata, publication["source_title"],
                                                 publication["doi"], publication["landing_url"])
        return {"schema": 2, "metadata": result}
    if (type(metadata) is not dict or set(metadata) != {"method", "preview_sha256"}
            or metadata["method"] != "official_source_preview"
            or "crossref_sha256" not in publication or publication["crossref_sha256"] is not None):
        raise ValueError
    digest = metadata["preview_sha256"]
    if (not isinstance(digest, str) or not re.fullmatch(r"[a-f0-9]{64}", digest)
            or digest != publication.get("preview_sha256")):
        raise ValueError
    return {"schema": 2, "metadata": {"method": "official_source_preview", "preview_sha256": digest}}


def require_cloud():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or sys.platform != "linux"
            or os.environ.get("EXPLICIT_CLOUD_BROWSER_APPROVAL") != "true"):
        raise BrowserDownloadError("imf_browser_cloud_approval_required")


def select_outbounds(body, decode):
    if not isinstance(body, str) or not body.strip() or len(body) > 2_000_000:
        raise BrowserDownloadError("imf_browser_subscription_unavailable")
    if "://" not in body.splitlines()[0]:
        body = decode(body) or ""
    selected, count = [], 0
    for line in body.splitlines():
        if not line.strip().lower().startswith("vless://"):
            continue
        count += 1
        if count > 64:
            raise BrowserDownloadError("imf_browser_subscription_limit")
        try:
            selected.append(client.build_outbound(line))
            if len(selected) == 3:
                break
        except client.UnsupportedNode:
            continue
    if not selected:
        raise BrowserDownloadError("imf_browser_valid_vless_required")
    return selected


def child_environment(proxy):
    u = urlsplit(proxy)
    if (u.scheme != "socks5h" or u.hostname != "127.0.0.1" or u.username is not None or u.password is not None
            or u.path or u.query or u.fragment or u.port is None or not 1 <= u.port <= 65535):
        raise BrowserDownloadError("imf_browser_invalid_listener")
    env = {k: v for k, v in os.environ.items() if k in SAFE_ENV}
    env.update(GITHUB_ACTIONS="true", EXPLICIT_CLOUD_BROWSER_APPROVAL="true", IMF_CLOUD_SOCKS_PORT=str(u.port))
    return env


def read_message(proc, timeout):
    """Bound one JSON line and wall-clock wait without trusting child output."""
    deadline, data = time.monotonic() + timeout, bytearray()
    os.set_blocking(proc.stdout.fileno(), False)
    with selectors.DefaultSelector() as selector:
        selector.register(proc.stdout, selectors.EVENT_READ)
        while True:
            remaining = deadline - time.monotonic()
            if remaining <= 0 or not selector.select(remaining):
                raise BrowserDownloadError("imf_browser_phase_timeout")
            chunk = os.read(proc.stdout.fileno(), min(65536, MAX_MESSAGE + 1 - len(data)))
            if not chunk:
                raise BrowserDownloadError("imf_browser_process_stopped")
            data.extend(chunk)
            if len(data) > MAX_MESSAGE:
                raise BrowserDownloadError("imf_browser_message_limit")
            if b"\n" in data:
                line, rest = data.split(b"\n", 1)
                if rest.strip():
                    raise BrowserDownloadError("imf_browser_protocol_invalid")
                try:
                    value = json.loads(line)
                except Exception:
                    raise BrowserDownloadError("imf_browser_protocol_invalid") from None
                if not isinstance(value, dict):
                    raise BrowserDownloadError("imf_browser_protocol_invalid")
                return value


def stop_browser(proc):
    try:
        if proc.poll() is None:
            try:
                os.killpg(proc.pid, signal.SIGTERM)
            except ProcessLookupError:
                pass  # The child may finish between poll and termination.
            try:
                proc.wait(timeout=8)
            except subprocess.TimeoutExpired:
                try:
                    os.killpg(proc.pid, signal.SIGKILL)
                except ProcessLookupError:
                    pass
                proc.wait(timeout=3)
    finally:
        for stream in (proc.stdin, proc.stdout):
            if stream:
                stream.close()


def publish_original(downloaded, destination, validated):
    """Expose a complete verified file atomically, without replacing any file."""
    data = downloaded.read_bytes()
    if len(data) != validated["bytes"] or hashlib.sha256(data).hexdigest() != validated["sha256"]:
        raise BrowserDownloadError("imf_browser_pdf_bytes_changed")
    destination.parent.mkdir(parents=True, exist_ok=True)
    fd, temporary = tempfile.mkstemp(prefix=".imf-original-", dir=destination.parent)
    try:
        with os.fdopen(fd, "wb") as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        # Both paths are on the same filesystem. link is atomic and exclusive.
        os.link(temporary, destination)
    finally:
        Path(temporary).unlink(missing_ok=True)


def _tokens(value):
    return set(re.findall(r"[^\W_]+", unicodedata.normalize("NFKC", value).casefold()))


def title_words_present(title, text):
    """Allow exact printed joining of an explicit alphabetic title compound.

    The observed Stablecoins title prints Macrofinancial while source metadata
    says Macro-Financial. Keep every other word, and never join number ranges.
    """
    observed = _tokens(text)
    normalized = unicodedata.normalize("NFKC", title).casefold()
    def join_observed(match):
        parts = re.split(r"[-\u2010\u2011]", match[0])
        joined = "".join(parts)
        return joined if joined in observed else match[0]
    # Replace only that exact occurrence. A component appearing separately
    # elsewhere in the title must remain independently required.
    normalized = re.sub(r"[^\W\d_]+(?:[-\u2010\u2011][^\W\d_]+)+", join_observed, normalized)
    expected = _tokens(normalized)
    return bool(observed and expected and expected <= observed)


def spanish_series_identity(publication, pdf_title, text):
    """Recognize only the two observed Spanish IMF report edition formats.

    The caller has already bound DOI, official issue URL and landing metadata.
    Here the PDF must independently name that series/edition and its substantive
    Spanish report title must occur in its body; a country/year alone never pass.
    """
    from imf_elibrary_resolver import title_key, validate_publication_url
    try:
        # This flag is extracted from this exact IMF preview's explicit original
        # language statement and included in its identity hash by the resolver.
        # Crossref/landing language and DOI remain the English source edition.
        if publication.get("original_language") != "es" or not isinstance(pdf_title, str) or not 0 < len(pdf_title) <= 4096:
            return False
        locator = validate_publication_url(publication["landing_url"])
        series = publication["doi"].rsplit(".", 1)[1]
        names = {"019": "Technical Assistance Reports", "029": "High-Level Summary Technical Assistance Reports"}
        if (series not in names or locator["kind"] != "journal" or locator["series"] != series
                or locator["language"] != publication.get("language") or locator["year"] != publication.get("year")
                or locator["issue"] != publication.get("issue")
                or title_key(names[series]) not in {title_key(x) for x in publication.get("series", [])}):
            return False
        source_head, separator, _ = publication["source_title"].partition(":")
        if not separator or not re.fullmatch(r"[^\d:;\n]{2,80}", source_head):
            return False
        parts = [part.strip() for part in unicodedata.normalize("NFKC", pdf_title).split(";")]
        if not 2 <= len(parts) <= 3:
            return False
        heading = re.fullmatch(r"([^:;\u2013\u2014]{2,80})\s*(?::|[\u2013\u2014])\s*(.+)", parts[0])
        if heading is None or title_key(heading[1]) != title_key(source_head):
            return False
        patterns = {
            "019": r"Informe de asistencia técnica del FMI n\.\s*[o°]\s*(20\d{2}|\d{2})/(\d{1,3})",
            "029": r"Informe del FMI sobre asistencia técnica:\s*Resumen de alto nivel n\.\s*[o°]\s*(20\d{2})/(\d{1,3})",
        }
        edition = re.fullmatch(patterns[series], parts[1], re.I)
        if edition is None:
            return False
        year = int(edition[1]) + (2000 if len(edition[1]) == 2 else 0)
        if str(year) != publication["year"] or int(edition[2]) != int(publication["issue"]):
            return False
        # Remove only the observed generic type prefix. Keep the actual mission
        # topic, date and every other title word, including accents and numbers.
        substantive = re.sub(r"^Informe de asistencia técnica\s*[\u2013\u2014]\s*", "", heading[2], flags=re.I)
        if len(_tokens(substantive)) < 8 or not title_words_present(substantive, text):
            return False
        if "fondo monetario internacional" not in title_key(text):
            return False
        if " " + title_key(source_head) + " " not in " " + title_key(text) + " ":
            return False
        if series == "029":
            body_editions = {(int(y) + (2000 if len(y) == 2 else 0), int(i))
                             for y, i in re.findall(r"\bHLS\s*/\s*(20\d{2}|\d{2})\s*/\s*(\d{1,3})\b", text, re.I)}
            if body_editions != {(year, int(publication["issue"]))}:
                return False
        return True
    except (KeyError, TypeError, ValueError):
        return False


def fiscal_pdf_identity(publication, metadata, pdf_title, pdf_subject, text, page_count):
    """The downloaded chapter independently names its DOI, whole topic and period."""
    from calendar import month_name
    from imf_elibrary_resolver import title_key
    try:
        chapter = metadata["chapter"]
        period = f"{month_name[int(metadata['month'])]} {metadata['year']}"
        expected_title = f"Chapter {chapter}. {publication['source_title']}. IMF Fiscal Monitor; {period}."
        return (metadata["method"] == "official_fiscal_chapter"
                and type(metadata["publisher_page"]["pages"]) is int
                and page_count == metadata["publisher_page"]["pages"]
                and isinstance(pdf_subject, str) and pdf_subject.strip() == "https://doi.org/" + publication["doi"]
                and isinstance(pdf_title, str) and title_key(pdf_title) == title_key(expected_title)
                and title_words_present(publication["source_title"], text)
                and re.search(r"\bfiscal\s+monitor\b", text, re.I) is not None
                and re.search(r"\bchapter\s+" + str(chapter) + r"\b", text, re.I) is not None
                and title_key(period) in title_key(text))
    except (KeyError, TypeError, ValueError, IndexError):
        return False


def write_public_evidence(publication, page):
    """Optional canary artifact: bounded public identity only, never runtime state.

    This is observation, not acceptance. Sanitized evidence must never feed the
    validators: they always receive the original metadata from the child pipe.
    """
    directory = os.environ.get("IMF_PUBLIC_EVIDENCE_DIR")
    if not directory:
        return
    require_cloud()
    from imf_elibrary_resolver import source_url, validate_publication_url
    def text(value):
        return value if isinstance(value, str) and len(value) <= 4096 else "[invalid_value]"
    def values(value):
        return [text(x) for x in value[:32]] if isinstance(value, list) else ["[invalid_list]"]
    def official_url(value, *, pdf=False, source=False):
        try:
            if source:
                source_url(value)
            else:
                validate_publication_url(value, pdf=pdf)
            return value
        except Exception:
            return "[invalid_official_url]"
    public = {key: text(publication.get(key)) for key in (
        "source_guid", "source_title", "title", "subtitle", "full_title", "doi", "isbn", "language", "original_language",
        "year", "issue", "identity_sha256", "crossref_sha256")}
    public["source_url"] = official_url(publication.get("source_url"), source=True)
    public["landing_url"] = official_url(publication.get("landing_url"))
    public["series"] = values(publication.get("series", []))
    public["title_variants"] = values(publication.get("title_variants", []))
    allowed = {"citation_doi", "dc.identifier.doi", "prism.doi", "citation_title", "dc.title",
               "citation_isbn", "citation_pdf_url", "canonical_url"}
    metadata = page.get("metadata") if isinstance(page.get("metadata"), dict) else {}
    observed = {key: values(value) for key, value in metadata.items() if key in allowed}
    for key in ("canonical_url", "citation_pdf_url"):
        if key in observed:
            observed[key] = [official_url(value, pdf=key == "citation_pdf_url") for value in observed[key]]
    status = page.get("landing_status")
    keys = page.get("metadata_keys", [])
    if (not isinstance(keys, list) or len(keys) > 128
            or any(not isinstance(key, str) or len(key) > 128 for key in keys)):
        keys = ["[invalid_names]"]
    record = {"schema": 1, "accepted": False, "kind": "public_landing_observation",
              "publication": public, "page": {
                  "final_url": official_url(page.get("final_url")),
                  "landing_status": status if type(status) is int and 100 <= status <= 599 else None,
                  "ready": page.get("ready") if type(page.get("ready")) is bool else None,
                  "metadata_keys": list(dict.fromkeys(keys)),
                  "metadata": observed, "h1s": values(page.get("h1s", [])),
                  "download_hrefs": [official_url(value, pdf=True) for value in values(page.get("download_hrefs", []))]}}
    if "visible_body" in page:
        body = page.get("visible_body")
        links = page.get("doi_links")
        record["page"].update({
            "visible_body": body if isinstance(body, str) and len(body.encode("utf-8", errors="replace")) <= 80 * 1024 else "[invalid_body]",
            "body_truncated": page.get("body_truncated") is not False,
            "doi_links": [value if isinstance(value, str) and re.fullmatch(r"https://doi\.org/10\.5089/97[89]\d{10}\.(019|029|089)", value)
                          else "[invalid_doi_url]" for value in links[:16]] if isinstance(links, list) else []})
    temporary = None
    try:
        root = Path(directory)
        root.mkdir(parents=True, exist_ok=True)
        filename = hashlib.sha256(publication["source_guid"].encode()).hexdigest() + ".json"
        descriptor, temporary = tempfile.mkstemp(prefix=".imf-public-", dir=root)
        with os.fdopen(descriptor, "w") as stream:
            json.dump(record, stream, ensure_ascii=False, sort_keys=True)
            stream.write("\n")
        os.replace(temporary, root / filename)
    except Exception:
        raise BrowserDownloadError("imf_browser_evidence_write_failed") from None
    finally:
        if temporary is not None:
            Path(temporary).unlink(missing_ok=True)


def verify_pdf(path, publication, max_bytes, expected_sha256=None, *, original_edition=None, fiscal_metadata=None):
    if type(max_bytes) is not int or not 0 < max_bytes <= 128 * 1024 * 1024:
        raise BrowserDownloadError("imf_browser_size_bound_invalid")
    if not path.is_file() or not 0 < path.stat().st_size <= max_bytes:
        raise BrowserDownloadError("imf_browser_pdf_size_invalid")
    data = path.read_bytes()
    digest = hashlib.sha256(data).hexdigest()
    if not data.startswith(b"%PDF-") or (expected_sha256 is not None and digest != expected_sha256):
        raise BrowserDownloadError("imf_browser_pdf_bytes_invalid")
    from pypdf import PdfReader
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            reader = PdfReader(io.BytesIO(data))
            if reader.is_encrypted or not 0 < len(reader.pages) <= 5000:
                raise BrowserDownloadError("imf_browser_pdf_pages_invalid")
            text = " ".join((page.extract_text() or "") for page in reader.pages[:3])
            page_count = len(reader.pages)
            pdf_title = (getattr(reader, "metadata", None) or {}).get("/Title", "")
            pdf_subject = (getattr(reader, "metadata", None) or {}).get("/Subject", "")
    except BrowserDownloadError:
        raise
    except Exception:
        raise BrowserDownloadError("imf_browser_pdf_parse_failed") from None
    # URL/DOI/title were already bound by the shared resolver. Still reject a
    # different or unreadable PDF: require the full official title's words here.
    # A short Crossref main title can be only a country. Require the combined
    # title/subtitle, not that weaker variant, for PDF body identity.
    if fiscal_metadata is not None:
        identity_verified = fiscal_pdf_identity(publication, fiscal_metadata, pdf_title, pdf_subject, text, page_count)
    elif publication.get("original_language") == "es":
        identity_verified = spanish_series_identity(publication, pdf_title, text)
    else:
        identity_verified = title_words_present(publication.get("full_title") or publication["source_title"], text)
    if original_edition is not None:
        from imf_elibrary_resolver import title_key
        identity_verified = (identity_verified and publication.get("original_language") == "es"
                             and type(original_edition.get("pages")) is int and page_count == original_edition["pages"]
                             and title_key(pdf_title.split(";", 1)[0]) == title_key(original_edition["title"])
                             and title_words_present(original_edition["title"], text))
    if not identity_verified:
        raise BrowserDownloadError("imf_browser_pdf_title_mismatch")
    return {"sha256": digest, "bytes": len(data), "pages": page_count}


class CloudImfBrowser:
    def __init__(self, *, fetch_subscription, decode_subscription):
        self.enabled = os.environ.get("IMF_CLOUD_BROWSER_ENABLED") == "true"
        self._fetch, self._decode = fetch_subscription, decode_subscription
        self._stack = contextlib.ExitStack()
        self._proxy = None
        self._active_index = None
        self._outbounds = ()
        self._binary = None
        self.last_source_attempts = []
        self._attempted = False
        self._startup_error = None
        self._signal_previous = None
        self._entered = False

    def __enter__(self):
        self._entered = True
        return self  # Disabled mode does not inspect runtime, credentials or OS.

    def __exit__(self, *_):
        try:
            self._stack.close()
        finally:
            if self._signal_previous is not None:
                signal.signal(signal.SIGTERM, self._signal_previous)
            self._entered = False

    def _start(self):
        require_cloud()
        if self._proxy:
            return set()
        if self._attempted:
            if self._startup_error is None and self._outbounds:
                tried = set()
                if self._next_source_route(tried):
                    return tried
                raise BrowserDownloadError("imf_browser_connectivity_rejected")
            raise BrowserDownloadError(self._startup_error or "imf_browser_start_failed")
        self._attempted = True
        try:
            binary = Path(os.environ.get("IMF_SING_BOX_BINARY", ""))
            if not binary.is_absolute() or not binary.is_file():
                raise BrowserDownloadError("imf_browser_runtime_missing")
            result = subprocess.run([str(binary), "version"], capture_output=True, text=True, timeout=5, check=False)
            if result.returncode or not re.search(r"^sing-box version " + re.escape(VERSION) + r"\s*$", result.stdout, re.M):
                raise BrowserDownloadError("imf_browser_runtime_version")
            subscription = os.environ.get("PROXY_SUBSCRIPTION_URL", "")
            if not subscription:
                raise BrowserDownloadError("imf_browser_subscription_missing")
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                body = self._fetch(subscription, 8)
            self._outbounds = tuple(select_outbounds(body, self._decode))
            self._binary = binary
            self._signal_previous = signal.getsignal(signal.SIGTERM)
            signal.signal(signal.SIGTERM, lambda *_: (_ for _ in ()).throw(KeyboardInterrupt()))
            tried = set()
            if self._activate(range(len(self._outbounds)), tried):
                return tried
            raise BrowserDownloadError("imf_browser_connectivity_rejected")
        except BrowserDownloadError as error:
            self._startup_error = str(error)
            self._stack.close()
            raise
        except client.UnsupportedNode as error:
            self._startup_error = "imf_browser_" + error.code
            self._stack.close()
            raise BrowserDownloadError(self._startup_error) from None
        except Exception:
            self._startup_error = "imf_browser_start_failed"
            self._stack.close()
            raise BrowserDownloadError(self._startup_error) from None

    def _activate(self, indices, tried):
        """Replace only this batch's ephemeral cloud client; never system state."""
        require_cloud()
        self._stack.close()
        self._proxy = self._active_index = None
        from curl_cffi import requests as cffi, CurlOpt
        for index in indices:
            tried.add(index)
            with contextlib.ExitStack() as candidate:
                proxy = candidate.enter_context(client.running_client(self._binary, self._outbounds[index]))
                response = None
                connected = False
                try:
                    response = cffi.get("https://www.gstatic.com/generate_204", timeout=8,
                                        proxies={"http": proxy, "https": proxy},
                                        curl_options={CurlOpt.NOPROXY: ""}, allow_redirects=False, stream=True)
                    connected = type(response.status_code) is int and response.status_code == 204
                except Exception:
                    pass
                finally:
                    if response is not None:
                        response.close()
                if connected:
                    self._stack.callback(candidate.pop_all().close)
                    self._proxy, self._active_index = proxy, index
                    return True
        return False

    def _next_source_route(self, tried):
        # _download_page has already stopped its child in finally. The same
        # route is never retried for this publication, even on connectivity
        # failure. A later publication gets its own independent budget.
        indices = [index for index in range(len(self._outbounds)) if index not in tried]
        if not indices:
            return False
        try:
            return self._activate(indices, tried)
        except client.UnsupportedNode as error:
            raise BrowserDownloadError("imf_browser_" + error.code) from None
        except BrowserDownloadError:
            raise
        except Exception:
            raise BrowserDownloadError("imf_browser_start_failed") from None

    @contextlib.contextmanager
    def http_session(self):
        """One scoped requests session over the already selected cloud client."""
        if not self.enabled or not self._entered:
            raise BrowserDownloadError("imf_browser_not_enabled")
        require_cloud()
        self._start()
        child_environment(self._proxy)  # Reuse strict 127.0.0.1 SOCKS listener validation.
        import requests
        with requests.Session() as session:
            session.trust_env = False
            session.proxies = {"http": self._proxy, "https": self._proxy}
            yield session

    def download(self, publication, dest, max_bytes, expected_sha256=None):
        self.last_source_attempts = []
        if not self.enabled or not self._entered:
            raise BrowserDownloadError("imf_browser_not_enabled")
        require_cloud()
        try:
            from imf_elibrary_resolver import source_url, title_key, validate_publication_url, validate_landing_metadata
            validate_publication_url(publication["landing_url"])
            if source_url(publication["source_url"]) != publication["source_url"]:
                raise ValueError
            if not re.fullmatch(r"10\.5089/97[89]\d{10}\.\d{3}(?:\.A\d{3})?", publication["doi"]):
                raise ValueError
            if not re.fullmatch(r"[a-f0-9]{64}", publication["identity_sha256"]):
                raise ValueError
            provenance = publication_provenance(publication)
            for field in ("source_guid", "title", "source_title", "full_title"):
                if not isinstance(publication[field], str) or not 0 < len(publication[field]) <= 8192:
                    raise ValueError
            if (publication.get("metadata", {}).get("method") != "official_fiscal_chapter"
                    and title_key(publication["source_title"]) != title_key(publication["full_title"])):
                raise ValueError
            if (type(max_bytes) is not int or not 0 < max_bytes <= 128 * 1024 * 1024
                    or (expected_sha256 is not None and not re.fullmatch(r"[a-f0-9]{64}", expected_sha256))):
                raise ValueError
        except Exception:
            raise BrowserDownloadError("imf_browser_publication_invalid") from None
        tried = self._start()
        tried.add(self._active_index)
        source_landing_status = None
        while True:
            try:
                return self._download_page(publication, dest, max_bytes, expected_sha256, provenance,
                                           source_landing_status=source_landing_status)
            except _OriginalEdition404:
                # One original-edition transition, retained across any route
                # change. It never returns to the missing English edition.
                if source_landing_status is not None:
                    raise BrowserDownloadError("imf_browser_landing_http_rejected") from None
                source_landing_status = 404
            except _LandingHttpRejected as error:
                if error.status not in RETRY_LANDING_STATUSES or not self._next_source_route(tried):
                    raise BrowserDownloadError("imf_browser_landing_http_rejected") from None

    def _download_page(self, publication, dest, max_bytes, expected_sha256, provenance, *, source_landing_status=None):
        from imf_elibrary_resolver import validate_landing_metadata, validate_publication_url
        from imf_original_edition import original_edition_candidate, resolve_original_edition
        requested_landing = (original_edition_candidate(publication) if source_landing_status == 404 else publication["landing_url"])
        fiscal = publication.get("metadata", {}).get("method") == "official_fiscal_chapter"
        destination = Path(dest)
        if destination.exists():
            raise BrowserDownloadError("imf_browser_destination_exists")
        with tempfile.TemporaryDirectory(prefix="imf-browser-", dir=os.environ.get("RUNNER_TEMP")) as folder:
            os.chmod(folder, 0o700)
            folder = Path(folder)
            request = folder / "request.json"
            with os.fdopen(os.open(request, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600), "w") as stream:
                json.dump({"landing_url": requested_landing, "max_bytes": max_bytes,
                           "observe_original_edition": source_landing_status == 404,
                           "observe_fiscal_chapter": fiscal}, stream)
            proc = None
            try:
                proc = subprocess.Popen(["node", str(Path(__file__).with_suffix(".cjs")), str(request)],
                                        env=child_environment(self._proxy), start_new_session=True,
                                        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL)
                page = read_message(proc, 100)
                write_public_evidence(publication, page)
                if page.get("stage") != "metadata":
                    raise BrowserDownloadError("imf_browser_page_not_ready")
                self.last_source_attempts.append({
                    "route": self._active_index + 1 if type(self._active_index) is int else None,
                    "landing_status": page.get("landing_status") if type(page.get("landing_status")) is int else None,
                })
                if type(page.get("landing_status")) is not int or page["landing_status"] != 200:
                    if type(page.get("landing_status")) is int and page["landing_status"] == 404 and source_landing_status is None:
                        try:
                            original_edition_candidate(publication)
                            if (validate_publication_url(page["final_url"])["document_path"] !=
                                    validate_publication_url(publication["landing_url"])["document_path"]):
                                raise ValueError
                        except ValueError:
                            pass
                        else:
                            raise _OriginalEdition404()
                    if type(page.get("landing_status")) is int:
                        raise _LandingHttpRejected(page["landing_status"])
                    raise BrowserDownloadError("imf_browser_landing_http_rejected")
                if page.get("ready") is not True:
                    raise BrowserDownloadError("imf_browser_page_not_ready")
                try:
                    edition = None
                    fiscal_metadata = None
                    if fiscal:
                        from imf_fiscal_chapter import resolve_fiscal_landing
                        pdf_url, fiscal_metadata = resolve_fiscal_landing(publication, page)
                        provenance = {"schema": 2, "metadata": fiscal_metadata}
                    elif source_landing_status == 404:
                        metadata = resolve_original_edition(publication, page, source_landing_status=source_landing_status)
                        provenance = {"schema": 2, "metadata": metadata}
                        edition = metadata["original_edition"]
                        pdf_url = page["download_hrefs"][0]
                    else:
                        pdf_url = validate_landing_metadata(publication, final_url=page["final_url"],
                                                            metadata=page["metadata"], h1s=page["h1s"],
                                                            download_hrefs=page["download_hrefs"])
                except Exception:
                    raise BrowserDownloadError("imf_browser_page_identity_mismatch") from None
                proc.stdin.write((json.dumps({"pdf_url": pdf_url}) + "\n").encode())
                proc.stdin.flush()
                result = read_message(proc, 70)
                if (result.get("stage") != "download" or result.get("pdf_url") != pdf_url
                        or type(result.get("landing_status")) is not int or type(result.get("pdf_status")) is not int
                        or result.get("landing_status") != 200 or result.get("pdf_status") != 200):
                    raise BrowserDownloadError("imf_browser_download_not_verified")
                if proc.wait(timeout=10) != 0:
                    raise BrowserDownloadError("imf_browser_process_failed")
                downloaded = folder / "download.pdf"
                if fiscal_metadata is not None:
                    validated = verify_pdf(downloaded, publication, max_bytes, expected_sha256, fiscal_metadata=fiscal_metadata)
                elif edition is not None:
                    validated = verify_pdf(downloaded, publication, max_bytes, expected_sha256, original_edition=edition)
                else:
                    validated = verify_pdf(downloaded, publication, max_bytes, expected_sha256)
                proof = {**provenance, "source_guid": publication["source_guid"], "source_url": publication["source_url"],
                         "landing_url": page["final_url"], "pdf_url": pdf_url, "doi": publication["doi"],
                         "title": publication["source_title"],
                         "identity_sha256": publication["identity_sha256"],
                         **validated, "landing_status": 200, "pdf_status": 200,
                         "source_identity_verified": True, "transport": "existing_subscription_vless_browser"}
                publish_original(downloaded, destination, validated)
                return proof
            except (_OriginalEdition404, BrowserDownloadError):
                raise
            except Exception:
                raise BrowserDownloadError("imf_browser_download_failed") from None
            finally:
                if proc is not None:
                    stop_browser(proc)
