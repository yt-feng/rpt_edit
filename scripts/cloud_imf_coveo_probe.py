"""Bounded, cloud-only public IMF Coveo original-document diagnostic.

Only the existing browser-exposed search key and returned public result IDs are
used. No index/admin endpoints or content-permission overrides are requested.
"""
import hashlib
import html
import io
import json
import os
from pathlib import Path
import re
from urllib.parse import urljoin, urlsplit

import requests
from pypdf import PdfReader

import fetch_institution_latest_pdfs as f

assert os.environ.get("GITHUB_ACTIONS") == "true", "Run only in GitHub Actions"

OUT = Path("_imf_coveo_probe")
OUT.mkdir(exist_ok=True)
cfg = f.INSTITUTIONS["imf"]
base = cfg["coveo_url"].split("?", 1)[0].rstrip("/")
session = requests.Session()
session.headers.update({
    "Authorization": "Bearer " + (os.getenv("IMF_COVEO_TOKEN") or cfg["coveo_token"]),
    "Origin": "https://www.imf.org",
    "Referer": "https://www.imf.org/",
    "User-Agent": f.DEFAULT_USER_AGENT,
})
seed = json.loads(Path("institution_feeds/pending_intake/imf.json").read_text())
item = next(row["item"] for row in seed["items"].values()
            if "580315" in row["item"]["source_url"])
summary = {"source": item, "queries": [], "previews": [], "streams": [], "crossref": {}}
MAX_BYTES = 32 * 1024 * 1024
PUBLIC_HOSTS = {"www.imf.org", "imf.org", "origin-www.imf.org", "www.elibrary.imf.org"}


def public_url(value):
    p = urlsplit(str(value or ""))
    return p.scheme in {"https", "http"} and p.hostname in PUBLIC_HOSTS


def bounded_get(endpoint, params):
    with session.get(base + endpoint, params=params, timeout=20,
                     allow_redirects=False, stream=True) as response:
        info = {"status": response.status_code,
                "content_type": response.headers.get("Content-Type", "")}
        # Never automatically carry search credentials to a redirected host.
        if 300 <= response.status_code < 400:
            location = response.headers.get("Location", "")
            info["redirect_host"] = urlsplit(location).hostname
            return info, b""
        data = bytearray()
        for chunk in response.iter_content(65536):
            data.extend(chunk)
            if len(data) > MAX_BYTES:
                info["too_large"] = True
                return info, b""
        info["bytes"] = len(data)
        return info, bytes(data)


def markup_metadata(content, source):
    text = content.decode("utf-8", errors="replace")
    hrefs = []
    for href in re.findall(r"(?:href|src|content)=[\"']([^\"']+)[\"']", text, re.I):
        target = urljoin(source, html.unescape(href))
        if public_url(target) and target not in hrefs:
            hrefs.append(target)
    plain = html.unescape(re.sub(r"<[^>]+>", " ", text))
    return {"public_links": hrefs[:100],
            "doi": sorted(set(re.findall(r"10\.5089/[A-Za-z0-9.]+", plain))),
            "isbn": sorted(set(re.findall(r"\b97[89]\d{10}\b", plain))),
            "stock_number": re.findall(r"Stock\s+No\.?\s*:?\s*([A-Z0-9][A-Z0-9._-]{5,31})", plain, re.I),
            "text_sample": re.sub(r"\s+", " ", plain)[:500]}


# Search the public index for the specific original, not arbitrary index content.
queries = ['tarea2026082 OR ("Republic of Estonia" "Consumer Price Index")']
results = {}
for query in queries:
    row = {"query": query}
    try:
        response = session.post(cfg["coveo_url"], timeout=20, json={
            "q": query, "searchHub": "Search", "numberOfResults": 8,
            "enableQuerySyntax": True,
            "fieldsToInclude": ["title", "clickableuri", "permanentid", "filetype",
                                "imfdate", "imfseries", "seriesvolumeno", "isbn", "doi"],
        })
        row["status"] = response.status_code
        if response.ok:
            data = response.json()
            row["total_count"] = data.get("totalCount")
            row["results"] = []
            for result in data.get("results", []):
                raw = result.get("raw", {})
                url = raw.get("clickableuri") or result.get("clickUri") or result.get("uri") or ""
                if not public_url(url):
                    continue
                record = {"title": result.get("title"), "url": url,
                          "unique_id": result.get("uniqueId"),
                          "filetype": raw.get("filetype"),
                          "has_html_version": result.get("hasHtmlVersion"),
                          "raw": raw}
                row["results"].append(record)
                identity = (str(record["title"]) + " " + url).lower()
                if ("tarea2026082" in identity or "580315" in identity or
                        str(record["title"]).casefold() == item["title"].casefold()):
                    results[record["unique_id"]] = record
    except Exception as exc:
        row["error_type"] = type(exc).__name__
    summary["queries"].append(row)

# Always preserve diagnostic metadata of the exact previously observed landing.
results.setdefault(item["coveo_unique_id"], {
    "title": item["title"], "url": item["source_url"],
    "unique_id": item["coveo_unique_id"], "filetype": "html",
})
preview_done = False
for record in list(results.values())[:3]:
    uid = record["unique_id"]
    if not uid:
        continue
    params = {"organizationId": cfg["coveo_organization_id"], "uniqueId": uid}
    if not preview_done:
        preview_done = True
        try:
            info, content = bounded_get("/html", params)
            info["source"] = record
            if info["status"] == 200:
                info.update(markup_metadata(content, record["url"]))
            summary["previews"].append(info)
        except Exception as exc:
            summary["previews"].append({"source": record, "error_type": type(exc).__name__})
    try:
        stream_params = {**params, "dataStream": "documentdata"}
        if str(record.get("filetype", "")).lower() == "pdf" or urlsplit(record["url"]).path.lower().endswith(".pdf"):
            stream_params["contentType"] = "application/pdf"
        info, content = bounded_get("/datastream", stream_params)
        info["source"] = record
        info["pdf"] = f.is_pdf_bytes(content)
        if info["status"] == 200 and info["pdf"]:
            reader = PdfReader(io.BytesIO(content))
            first_pages = "\n".join((page.extract_text() or "") for page in reader.pages[:3])
            info.update(sha256=hashlib.sha256(content).hexdigest(), pages=len(reader.pages),
                        first_page_text=first_pages[:1000],
                        identity_match=("estonia" in first_pages.lower() and
                                        "consumer price index" in first_pages.lower() and
                                        "2026" in first_pages))
            (OUT / (info["sha256"] + ".pdf")).write_bytes(content)
        elif info["status"] == 200 and ("html" in info["content_type"] or b"<html" in content[:500].lower()):
            info.update(markup_metadata(content, record["url"]))
        elif content:
            # Only structured application error code; never dump arbitrary HTML.
            try:
                error = json.loads(content)
                info["error_code"] = error.get("errorCode")
                info["error_message"] = str(error.get("message", ""))[:200]
            except (ValueError, AttributeError):
                pass
        summary["streams"].append(info)
    except Exception as exc:
        summary["streams"].append({"source": record, "error_type": type(exc).__name__})

# Exact DOI/ISBN comes from the official eLibrary subject/2 listing for this
# Estonia report. Crossref is queried separately: never forward the search key.
doi = "10.5089/9798229063937.019"
summary["crossref"]["doi"] = doi
try:
    response = requests.get("https://api.crossref.org/works/" + doi,
                            timeout=20, headers={"User-Agent": f.DEFAULT_USER_AGENT})
    summary["crossref"]["status"] = response.status_code
    if response.ok:
        message = response.json().get("message", {})
        summary["crossref"].update({key: message.get(key) for key in
                                    ("DOI", "title", "ISBN", "published", "link", "resource", "URL")})
        title = " ".join(message.get("title", []))
        matched = (str(message.get("DOI", "")).lower() == doi.lower() and
                   "estonia" in title.lower() and "consumer price index" in title.lower())
        summary["crossref"]["identity_match"] = matched
        summary["crossref"]["pdf_probes"] = []
        observed_pdf_links = [link.get("URL", "") for link in message.get("link", [])
                              if public_url(link.get("URL")) and
                              (link.get("content-type") == "application/pdf" or
                               urlsplit(link.get("URL", "")).path.lower().endswith(".pdf"))]
        # Leave one of the three permitted binary probes for a publisher-deposited
        # Crossref link only when fewer than three Coveo originals were queried.
        for url in list(dict.fromkeys(observed_pdf_links))[:max(0, 3 - len(summary["streams"]))] if matched else []:
            row = {"url": url}
            try:
                with requests.get(url, timeout=20, stream=True, allow_redirects=False,
                                  headers={"User-Agent": f.DEFAULT_USER_AGENT}) as pdf_response:
                    row.update(status=pdf_response.status_code,
                               content_type=pdf_response.headers.get("Content-Type", ""))
                    content = bytearray()
                    for chunk in pdf_response.iter_content(65536):
                        content.extend(chunk)
                        if len(content) > MAX_BYTES:
                            row["too_large"] = True
                            break
                    row.update(bytes=len(content), pdf=f.is_pdf_bytes(content))
                    if row["status"] == 200 and row["pdf"] and not row.get("too_large"):
                        reader = PdfReader(io.BytesIO(content))
                        first_pages = "\n".join((page.extract_text() or "") for page in reader.pages[:3])
                        row.update(sha256=hashlib.sha256(content).hexdigest(), pages=len(reader.pages),
                                   first_page_text=first_pages[:1000],
                                   identity_match=("estonia" in first_pages.lower() and
                                                   "consumer price index" in first_pages.lower() and
                                                   "2026" in first_pages))
                        (OUT / (row["sha256"] + ".pdf")).write_bytes(content)
            except Exception as exc:
                row["error_type"] = type(exc).__name__
            summary["crossref"]["pdf_probes"].append(row)
except Exception as exc:
    summary["crossref"]["error_type"] = type(exc).__name__

(OUT / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
print(json.dumps({"queries": [{k: v for k, v in r.items() if k != "results"}
                               for r in summary["queries"]],
                  "exact_candidates": len(results),
                  "crossref_status": summary["crossref"].get("status"),
                  "streams": [{k: v for k, v in r.items()
                               if k not in {"source", "public_links", "text_sample", "first_page_text"}}
                              for r in summary["streams"]]}, ensure_ascii=False))
