"""Pure metadata resolution for IMF's official eLibrary publications.

Callers own HTTP/browser access. No URL is synthesized from a title, journal ID
or language. A returned URL is metadata evidence, never proof of downloaded PDF
bytes. Source/preview hashes are suitable keys for a caller's batch-local cache.
"""
from __future__ import annotations

from dataclasses import dataclass
from functools import wraps
import hashlib
import html
from html.parser import HTMLParser
import json
import re
import unicodedata
from urllib.parse import parse_qsl, urljoin, urlsplit

MAX_HTML = 2_000_000
DOI_RE = re.compile(r"(?<![A-Za-z0-9])10\.5089/([0-9]{13})\.([0-9]{3})(?![A-Za-z0-9.])", re.I)
LIBRARY_HOSTS = {"www.elibrary.imf.org", "elibrary.imf.org"}
JOURNAL_RE = re.compile(r"/(?P<pdf>downloadpdf/)?view/journals/(?P<series>[0-9]{3})/(?P<year>20[0-9]{2})/(?P<issue>[0-9]{3})/(?P<document>(?P=series)\.(?P=year)\.issue-(?P=issue)|article-A[0-9]{3})-(?P<language>[a-z]{2})\.(?P<extension>xml|pdf)")
BOOK_RE = re.compile(r"/(?P<pdf>downloadpdf/)?display/book/(?P<isbn>[0-9]{13})/(?P=isbn)\.(?P<extension>xml|pdf)")
SPANISH_ORIGINAL_PREFIXES = (
    "[This report is only available in Spanish]",
    "[Please note this report is only available in Spanish]",
)


class ResolutionError(ValueError):
    """Fixed, content-free failure category, safe for run summaries."""

    def __init__(self, category):
        self.category = category if isinstance(category, str) and re.fullmatch(r"[a-z_]{1,80}", category) else "invalid_metadata"
        super().__init__(self.category)


def checked(function):
    @wraps(function)
    def call(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except ResolutionError:
            raise
        except (TypeError, ValueError, KeyError, AttributeError, IndexError):
            raise ResolutionError("invalid_metadata") from None
    return call


def require(condition, category):
    if not condition:
        raise ResolutionError(category)


def digest(value):
    return hashlib.sha256(json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def title_key(value):
    return re.sub(r"[\W_]+", " ", unicodedata.normalize("NFKC", html.unescape(value)).casefold()).strip()


def strings(value):
    if isinstance(value, str):
        return [value]
    if isinstance(value, (list, tuple)) and all(isinstance(item, str) for item in value):
        return list(value)
    return []


def isbn_valid(value):
    return bool(re.fullmatch(r"97[89][0-9]{10}", value)) and sum(int(c) * (1 if i % 2 == 0 else 3) for i, c in enumerate(value)) % 10 == 0


@checked
def source_url(value):
    require(isinstance(value, str) and len(value) <= 4096, "invalid_source_url")
    parsed = urlsplit(value)
    require(parsed.scheme == "https" and parsed.hostname in {"www.imf.org", "imf.org", "origin-www.imf.org"}
            and parsed.username is None and parsed.password is None and parsed.port in (None, 443)
            and not parsed.query and not parsed.fragment and "\\" not in value
            and parsed.path.lower().startswith("/en/publications/") and "%" not in parsed.path
            and not any(part in {".", ".."} for part in parsed.path.split("/")),
            "invalid_source_url")
    return "https://www.imf.org" + parsed.path


@checked
def validate_publication_url(value, *, pdf=False):
    """Validate an observed eLibrary URL and return its exact document locator."""
    require(isinstance(value, str) and 0 < len(value) <= 4096 and not re.search(r"[\s\\]", value), "invalid_official_url")
    try:
        parsed = urlsplit(value)
        require(parsed.scheme == "https" and parsed.hostname in LIBRARY_HOSTS and parsed.username is None
                and parsed.password is None and parsed.port in (None, 443) and not parsed.fragment
                and "%" not in parsed.path, "invalid_official_url")
        query = parse_qsl(parsed.query, keep_blank_values=True, strict_parsing=True)
        require(not query if pdf else (not query or (len(query) == 1 and query[0][0] == "cid"
                and re.fullmatch(r"[A-Za-z0-9-]{1,128}", query[0][1]))), "invalid_official_url")
        match = JOURNAL_RE.fullmatch(parsed.path) or BOOK_RE.fullmatch(parsed.path)
        require(match is not None, "invalid_official_url")
        result = match.groupdict()
        require(bool(result.pop("pdf")) == pdf and result.pop("extension") == ("pdf" if pdf else "xml"), "invalid_official_url")
        result["kind"] = "book" if "isbn" in result else "journal"
        result["document_path"] = parsed.path.removeprefix("/downloadpdf").rsplit(".", 1)[0]
        return result
    except (TypeError, ValueError) as error:
        if isinstance(error, ResolutionError):
            raise
        raise ResolutionError("invalid_official_url") from None


class _Document(HTMLParser):
    def __init__(self, markup):
        super().__init__(convert_charrefs=True)
        require(isinstance(markup, str) and 0 < len(markup) <= MAX_HTML, "invalid_html")
        self.metadata, self.h1s, self.hrefs, self.titles, self.visible = {}, [], [], [], []
        self.capture, self.parts = None, []
        self.hidden = 0
        self.feed(markup)
        self.close()

    def handle_starttag(self, tag, attrs):
        if tag in {"script", "style"}:
            self.hidden += 1
        values = dict(attrs)
        if tag == "meta":
            key = (values.get("name") or values.get("property") or "").lower()
            if key:
                self.metadata.setdefault(key, []).append(values.get("content", ""))
        if tag == "a" and values.get("href") and urlsplit(values["href"]).path.lower().endswith(".pdf"):
            self.hrefs.append(values["href"])
        if tag == "link" and values.get("rel", "").lower() == "canonical":
            self.metadata.setdefault("canonical_url", []).append(values.get("href", ""))
        if tag in {"h1", "title"}:
            self.capture, self.parts = tag, []

    def handle_data(self, text):
        if self.hidden:
            return
        self.visible.append(text)
        if self.capture:
            self.parts.append(text)

    def handle_endtag(self, tag):
        if tag in {"script", "style"}:
            self.hidden = max(0, self.hidden - 1)
        if tag == self.capture:
            (self.h1s if tag == "h1" else self.titles).append(" ".join(self.parts))
            self.capture = None


@dataclass(frozen=True)
class SourceIdentity:
    guid: str
    source_url: str
    title: str
    published: str
    doi: str
    isbn: str
    series: tuple[str, ...]
    year: str | None
    issue: str | None
    original_language: str | None
    source_binding_sha256: str
    preview_sha256: str


@checked
def bind_source(item, raw, preview_html, preview_url):
    """Bind one observed source to an explicit DOI; raw may be empty for pending."""
    require(isinstance(item, dict) and isinstance(raw, dict), "invalid_source_metadata")
    guid, title, published = item.get("guid"), item.get("title"), item.get("date", "")
    require(isinstance(guid, str) and 0 < len(guid) <= 4096 and isinstance(title, str)
            and bool(title_key(title)) and len(title) <= 4096 and isinstance(published, str), "invalid_source_metadata")
    canonical = source_url(item.get("source_url"))
    require(source_url(preview_url) == canonical, "preview_source_mismatch")
    for key in ("permanentid", "urihash"):
        if raw.get(key) and (key == "permanentid" or not raw.get("permanentid")):
            require(raw[key] == guid, "raw_identity_mismatch")
    for key in ("clickableuri", "sysclickableuri"):
        if raw.get(key):
            require(source_url(raw[key]) == canonical, "raw_identity_mismatch")
    for key in ("title", "systitle"):
        if raw.get(key):
            require(isinstance(raw[key], str) and title_key(raw[key]) == title_key(title), "raw_identity_mismatch")
    doc = _Document(preview_html)
    primary_titles = doc.h1s + doc.titles
    for key in ("citation_title", "dc.title", "og:title"):
        primary_titles.extend(doc.metadata.get(key, []))
    require(any(title_key(value) == title_key(title) for value in primary_titles), "preview_title_mismatch")
    for canonical_link in doc.metadata.get("canonical_url", []):
        require(source_url(urljoin(preview_url, canonical_link)) == canonical, "preview_source_mismatch")
    # Reject ambiguity, including references to other IMF reports. Never choose
    # the first DOI or infer one from an ISBN/journal/filename.
    doi_values = {match.group(0).lower() for match in DOI_RE.finditer(html.unescape(preview_html).replace("\\/", "/"))}
    for key in ("doi", "imfdoi", "citation_doi"):
        for value in strings(raw.get(key)):
            doi_values.update(match.group(0).lower() for match in DOI_RE.finditer(value))
    require(len(doi_values) == 1, "explicit_doi_missing_or_ambiguous")
    doi = next(iter(doi_values))
    isbn = doi.split("/", 1)[1].split(".", 1)[0]
    require(isbn_valid(isbn), "invalid_source_isbn")
    explicit_isbns = []
    for key in ("isbn", "imfisbn"):
        explicit_isbns.extend(strings(raw.get(key)))
    for key in ("citation_isbn", "dc.identifier.isbn", "isbn"):
        explicit_isbns.extend(doc.metadata.get(key, []))
    visible = " ".join(doc.visible)
    explicit_isbns.extend(re.findall(r"\bISBN(?:-13)?\s*:?\s*(97[89](?:[\s-]?[0-9]){10})(?![0-9])", visible, re.I))
    for value in explicit_isbns:
        require(re.sub(r"[\s-]", "", value) == isbn, "source_isbn_mismatch")
    series = tuple(strings(raw.get("imfseries")))
    preview_series = tuple(doc.metadata.get("series", []))
    if series and preview_series:
        require({title_key(value) for value in series} == {title_key(value) for value in preview_series}, "preview_series_mismatch")
    series = series or preview_series
    volume = str(raw.get("seriesvolumeno") or "")
    numbers = set(re.findall(r"\b(20[0-9]{2})\s*/\s*([0-9]{1,4})\b", volume))
    require(len(numbers) <= 1, "source_series_ambiguous")
    year, issue = next(iter(numbers)) if numbers else (None, None)
    issue = str(int(issue)).zfill(3) if issue is not None else None
    preview_years = set(re.findall(r"\bVolume\s*:?\s*(20[0-9]{2})(?![0-9])", visible, re.I))
    preview_issues = {str(int(value)).zfill(3) for value in re.findall(r"\bIssue\s*:?\s*([0-9]{1,4})(?![0-9])", visible, re.I)}
    require(len(preview_years) <= 1 and len(preview_issues) <= 1, "preview_series_ambiguous")
    if preview_years:
        observed_year = next(iter(preview_years))
        require(year is None or year == observed_year, "preview_year_mismatch")
        year = observed_year
    if preview_issues:
        observed_issue = next(iter(preview_issues))
        require(issue is None or issue == observed_issue, "preview_issue_mismatch")
        issue = observed_issue
    # These two declarations are observed on the English source's own official
    # Description metadata. They describe original PDF language, not the DOI
    # metadata/landing language; never substitute another edition's DOI/ISBN.
    descriptions = doc.metadata.get("description", [])
    original_language = "es" if descriptions and all(
        value.strip().startswith(SPANISH_ORIGINAL_PREFIXES) for value in descriptions
    ) else None
    binding = {"guid": guid, "source_url": canonical, "title": title, "published": published,
               "doi": doi, "isbn": isbn, "series": series, "year": year, "issue": issue,
               "original_language": original_language}
    return SourceIdentity(guid, canonical, title, published, doi, isbn, series, year, issue, original_language,
                          digest(binding), hashlib.sha256(preview_html.encode()).hexdigest())


def _crossref_year(message):
    if message.get("volume"):
        require(re.fullmatch(r"20[0-9]{2}", str(message["volume"])), "crossref_year_mismatch")
        return str(message["volume"])
    for key in ("published", "issued", "published-print", "published-online"):
        dates = message.get(key, {}).get("date-parts", [])
        if dates and dates[0]:
            require(isinstance(dates[0][0], int) and 2000 <= dates[0][0] <= 2099, "crossref_year_mismatch")
            return str(dates[0][0])
    return None


def _check_locator(identity, locator, *, year, issue, language):
    if locator["kind"] == "book":
        require(locator["isbn"] == identity.isbn, "official_url_identity_mismatch")
    else:
        require(locator["series"] == identity.doi.rsplit(".", 1)[1], "official_url_identity_mismatch")
        require(year is not None and locator["year"] == year and issue is not None and locator["issue"] == issue,
                "official_url_identity_mismatch")
        if language:
            require(locator["language"] == language, "official_url_language_mismatch")


@checked
def resolve_crossref(identity, payload):
    """Validate an exact-DOI response; retain only observed official URLs."""
    require(isinstance(identity, SourceIdentity) and isinstance(payload, dict), "invalid_crossref_metadata")
    message = payload.get("message", payload)
    require(isinstance(message, dict), "invalid_crossref_metadata")
    require(str(message.get("DOI", "")).lower() == identity.doi, "crossref_doi_mismatch")
    require(message.get("publisher") in {"International Monetary Fund (IMF)", "International Monetary Fund"}, "crossref_publisher_mismatch")
    titles, subtitles = strings(message.get("title")), strings(message.get("subtitle"))
    require(len(titles) == 1 and len(subtitles) <= 1, "crossref_title_ambiguous")
    full_title = titles[0] + (": " + subtitles[0] if subtitles else "")
    require(title_key(full_title) == title_key(identity.title), "crossref_title_mismatch")
    crossref_series = strings(message.get("container-title"))
    if identity.series:
        require({title_key(value) for value in identity.series} & {title_key(value) for value in crossref_series},
                "crossref_series_mismatch")
    year = _crossref_year(message)
    issue = str(message.get("issue") or message.get("journal-issue", {}).get("issue") or "")
    require(not issue or re.fullmatch(r"[0-9]{1,4}", issue), "crossref_issue_mismatch")
    issue = str(int(issue)).zfill(3) if issue else None
    require(identity.year is None or identity.year == year, "crossref_year_mismatch")
    require(identity.issue is None or identity.issue == issue, "crossref_issue_mismatch")
    if identity.year is None and re.match(r"^20[0-9]{2}-", identity.published):
        require(year == identity.published[:4], "crossref_year_mismatch")
    for value in strings(message.get("ISBN")):
        require(re.sub(r"[\s-]", "", value) == identity.isbn, "crossref_isbn_mismatch")
    language = message.get("language") or None
    require(language is None or (isinstance(language, str) and re.fullmatch(r"[a-z]{2}", language)), "crossref_language_mismatch")
    landing = message.get("resource", {}).get("primary", {}).get("URL")
    require(isinstance(landing, str), "official_landing_missing")
    locator = validate_publication_url(landing)
    _check_locator(identity, locator, year=year, issue=issue, language=language)
    candidates = []
    for link in message.get("link", []):
        require(isinstance(link, dict), "invalid_crossref_metadata")
        if link.get("content-type") != "application/pdf":
            continue
        candidate = link.get("URL")
        pdf_locator = validate_publication_url(candidate, pdf=True)
        _check_locator(identity, pdf_locator, year=year, issue=issue, language=language)
        require(pdf_locator["document_path"] == locator["document_path"], "official_pdf_identity_mismatch")
        if candidate not in candidates:
            candidates.append(candidate)
    return {"source_guid": identity.guid, "source_url": identity.source_url, "source_title": identity.title,
            "doi": identity.doi, "isbn": identity.isbn, "title": titles[0], "subtitle": subtitles[0] if subtitles else "",
            "full_title": full_title, "title_variants": list(dict.fromkeys([titles[0], full_title])),
            "series": crossref_series, "year": year, "issue": issue, "language": language or locator.get("language"),
            "original_language": identity.original_language,
            "landing_url": landing, "pdf_url_candidates": candidates, "identity_sha256": identity.source_binding_sha256,
            "preview_sha256": identity.preview_sha256, "crossref_sha256": digest(payload), "pdf_verified": False}


@checked
def validate_official_pair(landing_url, pdf_url, doi):
    """Structural binding only; callers still verify source identity/PDF bytes."""
    match = DOI_RE.fullmatch(doi) if isinstance(doi, str) else None
    require(match is not None and isbn_valid(match.group(1)), "invalid_source_doi")
    landing = validate_publication_url(landing_url)
    pdf = validate_publication_url(pdf_url, pdf=True)
    require(landing["document_path"] == pdf["document_path"], "official_pdf_identity_mismatch")
    if landing["kind"] == "book":
        require(landing["isbn"] == match.group(1), "official_url_identity_mismatch")
    else:
        require(landing["series"] == match.group(2), "official_url_identity_mismatch")
    return landing


@checked
def validate_landing_metadata(publication, *, final_url, metadata, h1s, download_hrefs):
    """Validate bounded browser-observed metadata and select its one exact PDF."""
    require(isinstance(publication, dict) and isinstance(metadata, dict), "invalid_landing_metadata")
    require(isinstance(h1s, list) and isinstance(download_hrefs, list) and len(h1s) <= 32
            and len(download_hrefs) <= 32 and all(isinstance(x, str) for x in h1s + download_hrefs), "invalid_landing_metadata")
    require(len(metadata) <= 64 and all(isinstance(k, str) and isinstance(v, list) and len(v) <= 32
            and all(isinstance(x, str) and len(x) <= 4096 for x in v) for k, v in metadata.items()), "invalid_landing_metadata")
    expected = validate_publication_url(publication["landing_url"])
    current = validate_publication_url(final_url)
    require(expected["document_path"] == current["document_path"], "landing_url_identity_mismatch")
    normalized = {}
    for key, values in metadata.items():
        normalized.setdefault(key.lower(), []).extend(values)
    metadata = normalized
    dois = {value.strip().lower().removeprefix("https://doi.org/") for key in ("citation_doi", "dc.identifier.doi", "prism.doi")
            for value in metadata.get(key, [])}
    require(dois == {publication["doi"]}, "landing_doi_mismatch")
    known_titles = {title_key(value) for value in publication["title_variants"]}
    observed_titles = metadata.get("citation_title", []) or metadata.get("dc.title", [])
    require(observed_titles and all(title_key(value) in known_titles for value in observed_titles), "landing_title_mismatch")
    require(len(h1s) == 1 and title_key(h1s[0]) == title_key(publication["full_title"]), "landing_heading_mismatch")
    for value in metadata.get("citation_isbn", []):
        require(re.sub(r"[\s-]", "", value) == publication["isbn"], "landing_isbn_mismatch")
    for canonical in metadata.get("canonical_url", []):
        require(validate_publication_url(urljoin(final_url, canonical))["document_path"] == current["document_path"], "landing_url_identity_mismatch")
    for href in metadata.get("citation_pdf_url", []):
        validate_official_pair(final_url, urljoin(final_url, href), publication["doi"])
    candidates = []
    for href in download_hrefs + metadata.get("citation_pdf_url", []):
        value = urljoin(final_url, href)
        # Ignore unrelated navigation anchors; explicit PDF links must remain
        # official. A different issue's PDF is never selected as this report.
        if not urlsplit(value).path.lower().endswith(".pdf"):
            continue
        candidate = validate_publication_url(value, pdf=True)
        if candidate["document_path"] == current["document_path"]:
            candidates.append(value)
    paths = {validate_official_pair(final_url, value, publication["doi"])["document_path"] for value in candidates}
    require(len(paths) == 1, "official_pdf_missing_or_ambiguous")
    require(candidates, "official_pdf_missing_or_ambiguous")
    return candidates[0]


@checked
def resolve_landing(publication, html_text, final_url):
    doc = _Document(html_text)
    return validate_landing_metadata(publication, final_url=final_url, metadata=doc.metadata,
                                     h1s=doc.h1s, download_hrefs=doc.hrefs)
