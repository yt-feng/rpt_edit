"""Pure binding of an explicitly declared Spanish IMF original edition.

A generated candidate is never evidence. Acceptance requires the observed
publisher page's independent labelled identity and its exact official PDF link.
This module performs no I/O and imports no browser or transport code.
"""
from __future__ import annotations

from functools import wraps
import re
from urllib.parse import urlsplit, urlunsplit

from imf_elibrary_resolver import digest, isbn_valid, title_key, validate_official_pair, validate_publication_url

SERIES = {"019": "Technical Assistance Reports", "029": "High-Level Summary Technical Assistance Reports"}
METADATA_FIELDS = {"method", "source_crossref_sha256", "preview_sha256", "source_landing_url",
                   "source_landing_status", "original_edition"}
EDITION_FIELDS = {"doi", "isbn", "title", "language", "series", "year", "issue", "pages", "page_sha256"}


class EditionError(ValueError):
    category = "imf_original_edition_invalid"
    def __init__(self):
        super().__init__(self.category)


def checked(function):
    @wraps(function)
    def call(*args, **kwargs):
        try:
            return function(*args, **kwargs)
        except (ValueError, TypeError, KeyError, AttributeError, IndexError):
            raise EditionError() from None
    return call


def require(condition):
    if not condition:
        raise EditionError()


def sha(value):
    return isinstance(value, str) and bool(re.fullmatch(r"[a-f0-9]{64}", value))


def doi_parts(value):
    match = re.fullmatch(r"10\.5089/(97[89]\d{10})\.(019|029)", value) if isinstance(value, str) else None
    require(match is not None and isbn_valid(match[1]))
    return match[1], match[2]


@checked
def original_edition_candidate(publication):
    """One same-issue candidate, only for a source explicitly declaring Spanish."""
    require(publication.get("original_language") == "es" and publication.get("language") == "en"
            and "metadata" not in publication and sha(publication["crossref_sha256"])
            and sha(publication["preview_sha256"]) and sha(publication["identity_sha256"]))
    isbn, series = doi_parts(publication["doi"])
    source = validate_publication_url(publication["landing_url"])
    require(source["kind"] == "journal" and source["language"] == "en" and source["series"] == series
            and source["year"] == publication["year"] and source["issue"] == publication["issue"]
            and publication["isbn"] == isbn and SERIES[series] in publication["series"]
            and title_key(publication["source_title"]) == title_key(publication["full_title"]))
    parsed = urlsplit(publication["landing_url"])
    candidate = urlunsplit(("https", parsed.netloc, source["document_path"].removesuffix("-en") + "-es.xml", "", ""))
    validate_publication_url(candidate)
    return candidate


@checked
def validate_original_edition_metadata(metadata, source_doi, landing_url, pdf_url):
    """Validate the full schema2 receipt group; return its actual edition dict."""
    require(type(metadata) is dict and set(metadata) == METADATA_FIELDS
            and metadata["method"] == "publisher_original_edition"
            and type(metadata["source_landing_status"]) is int and metadata["source_landing_status"] == 404
            and sha(metadata["source_crossref_sha256"]) and sha(metadata["preview_sha256"]))
    _, source_series = doi_parts(source_doi)
    source = validate_publication_url(metadata["source_landing_url"])
    edition = metadata["original_edition"]
    require(type(edition) is dict and set(edition) == EDITION_FIELDS)
    isbn, series = doi_parts(edition["doi"])
    actual = validate_official_pair(landing_url, pdf_url, edition["doi"])
    require(source["kind"] == actual["kind"] == "journal" and source["language"] == "en"
            and actual["language"] == edition["language"] == "es" and source_series == series == source["series"]
            and source["document_path"].removesuffix("-en") == actual["document_path"].removesuffix("-es")
            and edition["year"] == actual["year"] and edition["issue"] == actual["issue"]
            and edition["isbn"] == isbn and edition["series"] == SERIES[series]
            and type(edition["pages"]) is int and 1 <= edition["pages"] <= 5000
            and sha(edition["page_sha256"]) and isinstance(edition["title"], str)
            and 10 <= len(edition["title"]) <= 4096 and len(title_key(edition["title"]).split()) >= 9
            and re.search(r"[\x00-\x1f\x7f\ud800-\udfff]", edition["title"]) is None
            and re.fullmatch(r"[^\d:;\n]{2,80}:.+", edition["title"]) is not None)
    return dict(edition)


def one_label(lines, label):
    values = [line[len(label) + 1:].strip() for line in lines if line.startswith(label + ":")]
    require(len(values) == 1 and values[0])
    return values[0]


@checked
def resolve_original_edition(publication, page, *, source_landing_status):
    """Bind one HTTP200 observed Spanish page to the original English DOI chain."""
    candidate = original_edition_candidate(publication)
    require(type(source_landing_status) is int and source_landing_status == 404
            and type(page) is dict and type(page["landing_status"]) is int and page["landing_status"] == 200
            and page["ready"] is True and page.get("body_truncated") is False)
    candidate_locator = validate_publication_url(candidate)
    actual_locator = validate_publication_url(page["final_url"])
    require(candidate_locator["document_path"] == actual_locator["document_path"])
    body = page["visible_body"]
    require(isinstance(body, str) and 0 < len(body.encode()) <= 80 * 1024)
    lines = [line.strip() for line in body.splitlines() if line.strip()]
    # Each labelled identity occurs exactly once. A second identical label is
    # also ambiguous; the separate plain Volume line must corroborate it.
    series_text = one_label(lines, "Series")
    edition_number = one_label(lines, "Volume/Issue")
    require(one_label(lines, "Publisher") == "International Monetary Fund"
            and one_label(lines, "Language") == "Spanish")
    isbn = one_label(lines, "ISBN")
    pages_text = one_label(lines, "Pages")
    require(re.fullmatch(r"[1-9]\d{0,3}", pages_text) is not None)
    doi_url = one_label(lines, "DOI")
    require(re.fullmatch(r"https://doi\.org/10\.5089/97[89]\d{10}\.(019|029)", doi_url) is not None)
    doi = doi_url.removeprefix("https://doi.org/")
    doi_isbn, series = doi_parts(doi)
    require(isbn == doi_isbn and series_text == "Books and Analytical Papers, " + SERIES[series])
    expected_number = f"Volume {publication['year']}: Issue {publication['issue']}"
    require(edition_number == expected_number and lines.count(expected_number) == 1)
    h1s, doi_links, hrefs = page["h1s"], page["doi_links"], page["download_hrefs"]
    require(isinstance(h1s, list) and len(h1s) == 1 and isinstance(h1s[0], str) and len(h1s[0]) <= 4096
            and isinstance(doi_links, list) and 1 <= len(doi_links) <= 16
            and all(isinstance(value, str) for value in doi_links) and set(doi_links) == {doi_url}
            and isinstance(hrefs, list) and len(hrefs) == 1 and isinstance(hrefs[0], str))
    title = " ".join(h1s[0].split())
    source_country, sep, _ = publication["source_title"].partition(":")
    country, actual_sep, _ = title.partition(":")
    require(sep and actual_sep and title_key(source_country) == title_key(country)
            and sum(title_key(line) == title_key(title) for line in lines) == 1)
    metadata = {"method": "publisher_original_edition", "source_crossref_sha256": publication["crossref_sha256"],
                "preview_sha256": publication["preview_sha256"], "source_landing_url": publication["landing_url"],
                "source_landing_status": source_landing_status, "original_edition": {
                    "doi": doi, "isbn": isbn, "title": title, "language": "es", "series": SERIES[series],
                    "year": publication["year"], "issue": publication["issue"], "pages": int(pages_text),
                    "page_sha256": digest({key: page[key] for key in ("final_url", "landing_status", "h1s",
                        "metadata", "doi_links", "download_hrefs", "visible_body", "body_truncated")})}}
    validate_original_edition_metadata(metadata, publication["doi"], page["final_url"], hrefs[0])
    # Reuse ordinary publisher checks for every optional metadata value. Missing
    # citation tags are allowed by that validator; present conflicts are not.
    from imf_elibrary_resolver import validate_landing_metadata
    edition_publication = {**publication, "doi": doi, "isbn": isbn, "landing_url": page["final_url"],
                           "title": title, "full_title": title, "title_variants": [title]}
    require(validate_landing_metadata(edition_publication, final_url=page["final_url"], metadata=page["metadata"],
        h1s=h1s, download_hrefs=hrefs) == hrefs[0])
    return metadata
