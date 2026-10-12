"""Bounded GitHub Actions probe of the current subscription and one frozen IMF PDF.

No credentials, subscription URLs, proxy identities, raw errors or HTML are
printed or saved. The production checkout supplies the parser and frozen seed.
"""
from __future__ import annotations

import argparse
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
import contextlib
import hashlib
import html
import importlib
import io
import json
import os
from pathlib import Path
import re
import sys
import threading
import time
from urllib.parse import parse_qsl, urlsplit

MAX_NODES = 28
MAX_BYTES = 32 * 1024 * 1024
TIMEOUT = 8
OUTPUT = Path("_imf_current_proxy_probe")
EXPECTED_PDF = "https://www.imf.org/-/media/files/publications/tar/2026/english/tarea2026082.pdf"
SCHEMES = {"http", "https", "socks5", "socks5h", "ss", "ssr", "vmess", "vless", "trojan"}
INVENTORY_SCHEMES = SCHEMES | {"anytls", "hysteria", "hysteria2", "hy2", "tuic", "snell", "naive", "naive+https", "wireguard", "socks", "socks4", "socks4a"}
VLESS_QUERY_KEYS = {"type", "encryption", "flow", "security", "path", "host", "serviceName", "mode", "authority", "extra", "fp", "sni", "alpn", "ech", "pcs", "vcn", "pbk", "sid", "spx", "pqv", "fm", "headerType", "seed", "mtu", "tti", "allowInsecure", "insecure", "packetEncoding", "ed", "eh"}
VLESS_TRANSPORTS = {"tcp", "raw", "kcp", "ws", "http", "grpc", "httpupgrade", "xhttp"}
OFFICIAL_HOSTS = {"www.imf.org", "imf.org", "origin-www.imf.org", "www.elibrary.imf.org"}
SAVE_LOCK = threading.Lock()


def line_scheme(line: str) -> str:
    """Recognize URI schemes without emitting arbitrary subscription text."""
    match = re.match(r"^([A-Za-z][A-Za-z0-9+.-]{0,31})://", line.strip())
    if not match:
        return "no_uri_scheme"
    scheme = match.group(1).lower()
    return scheme if scheme in INVENTORY_SCHEMES else "other_uri_scheme"


def vless_metadata(line: str) -> dict:
    """Only enumerated protocol settings, integer port and known key names."""
    result = {"parse_valid": False}
    try:
        uri = urlsplit(line.strip())
        pairs = parse_qsl(uri.query, keep_blank_values=True, errors="strict", max_num_fields=64)
        keys = [key for key, _ in pairs]
        values = dict(pairs)
        result.update(
            parse_valid=(uri.scheme == "vless" and bool(uri.hostname) and bool(uri.username)
                         and uri.password is None and uri.port is not None and not uri.path),
            port=uri.port,
            transport=(values["type"] if values.get("type") in VLESS_TRANSPORTS
                       else "absent" if "type" not in values else "other"),
            security=(values["security"] if values.get("security") in {"none", "tls", "reality"}
                      else "absent" if "security" not in values else "other"),
            query_keys=sorted(set(keys) & VLESS_QUERY_KEYS),
            unknown_query_key_count=len(set(keys) - VLESS_QUERY_KEYS),
            duplicate_query_keys=len(keys) != len(set(keys)),
        )
    except Exception:
        pass
    return result


def category(error: Exception) -> str:
    """Only fixed classifications escape this function, never exception text."""
    code = getattr(error, "code", None)
    detail = str(error).lower()
    if code == 67 or any(x in detail for x in (
        "user was rejected", "authentication failed", "no authentication method was acceptable",
        "proxy authentication required", "response 407", "http 407",
    )):
        return "authentication_rejected"
    if code == 97:
        return "proxy_handshake_failed"
    if code == 28 or isinstance(error, TimeoutError):
        return "connection_timeout"
    if code in {5, 6, 7, 35, 52, 55, 56, 60}:
        return "connection_failed"
    return "request_failed"


def inspect_response_markers(headers, content: bytes) -> dict:
    server = str(headers.get("server", "")).lower()
    sample = content[:65536].lower()
    title_match = re.search(rb"<title[^>]*>(.*?)</title\s*>", sample, re.S)
    title = " ".join(html.unescape(title_match.group(1).decode("utf-8", "replace")).split()) if title_match else ""
    title_class = title if title in {"access denied", "403 forbidden", "forbidden", "request rejected", "error", "just a moment..."} else "other" if title_match else "absent"
    return {
        "body_sha256": hashlib.sha256(content).hexdigest(),
        "html_title_class": title_class,
        "server_present": bool(server),
        "server_akamai": "akamai" in server,
        "server_cloudflare": "cloudflare" in server,
        "server_squid": "squid" in server,
        "proxy_authenticate_header_present": "proxy-authenticate" in headers,
        "body_akamai_marker": any(x in sample for x in (b"akamai", b"errors.edgesuite.net", b"errors.edgekey.net")),
        "body_access_denied_marker": b"access denied" in sample,
        "body_reference_marker": b"reference #" in sample,
        "body_html_marker": b"<html" in sample or b"<!doctype html" in sample,
    }


def probe(index: int, proxy: str, target: str, url: str, f, cffi, PdfReader) -> dict:
    started = time.monotonic()
    scheme = urlsplit(proxy).scheme.lower()
    row = {"route_index": index, "route_scheme": scheme if scheme in SCHEMES else "other",
           "target": target, "status": None, "bytes": 0, "is_pdf": False,
           "accepted_source_pdf": False}
    response = None
    try:
        from curl_cffi import CurlOpt

        response = cffi.get(
            url, timeout=TIMEOUT, impersonate=f.CFFI_IMPERSONATE,
            proxies={"http": proxy, "https": proxy}, headers=f.source_request_headers(),
            # Bind this diagnostic request to its chosen route even if the
            # isolated runner has an inherited NO_PROXY environment value.
            curl_options={CurlOpt.NOPROXY: ""},
            allow_redirects=True, stream=True,
        )
        row["status"] = int(response.status_code)
        body = bytearray()
        for chunk in response.iter_content(65536):
            if not chunk:
                continue
            if len(body) + len(chunk) > MAX_BYTES:
                row["too_large"] = True
                break
            body.extend(chunk)
        data = bytes(body)
        row["bytes"] = len(data)
        row.update(inspect_response_markers(response.headers, data))
        row["official_final_host"] = urlsplit(str(response.url)).hostname in OFFICIAL_HOSTS
        row["pdf_signature"] = f.is_pdf_bytes(data)
        if row["pdf_signature"] and not row.get("too_large") and row["status"] == 200:
            try:
                # Parser warnings sometimes quote source bytes; keep them private.
                with contextlib.redirect_stderr(io.StringIO()):
                    reader = PdfReader(io.BytesIO(data))
                    pages = len(reader.pages)
                    first_page = reader.pages[0].extract_text() or "" if pages else ""
                    first_pages = "\n".join((page.extract_text() or "") for page in reader.pages[:3])
                row["is_pdf"] = pages > 0
                if row["is_pdf"]:
                    digest = hashlib.sha256(data).hexdigest()
                    text = first_pages.casefold()
                    identity = "estonia" in text and "consumer price index" in text and "2026" in text
                    row.update(sha256=digest, pages=pages, source_identity_match=identity,
                               accepted_source_pdf=(target == "pdf" and row["official_final_host"] and identity))
                    if identity:
                        row["first_page_text"] = first_page[:400]
                    with SAVE_LOCK:
                        path = OUTPUT / (digest + ".pdf")
                        if not path.exists():
                            path.write_bytes(data)
                    row["artifact_file"] = path.name
            except Exception:
                row["pdf_parse_failed"] = True
        if row["status"] == 407:
            row["category"] = "authentication_rejected"
        elif row["status"] >= 400:
            row["category"] = "http_rejected"
        else:
            row["category"] = "http_response"
    except Exception as error:
        row["category"] = category(error)
        code = getattr(error, "code", None)
        if isinstance(code, int) and 0 <= code <= 999:
            row["curl_code"] = code
    finally:
        if response is not None:
            try:
                response.close()
            except Exception:
                pass
        row["elapsed_seconds"] = round(time.monotonic() - started, 3)
    return row


def main() -> int:
    if os.environ.get("GITHUB_ACTIONS") != "true":
        raise RuntimeError("Run only in GitHub Actions")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--production-root", type=Path, default=Path("."))
    parser.add_argument("--metadata-only", action="store_true", help="Inspect subscription protocol metadata without making node requests")
    args = parser.parse_args()
    root = args.production_root.resolve()
    sys.path.insert(0, str(root / "scripts"))
    f = importlib.import_module("fetch_institution_latest_pdfs")
    if not hasattr(f, "_subscription_expired"):
        raise RuntimeError("Current production subscription monitoring is required")
    from curl_cffi import requests as cffi
    from pypdf import PdfReader

    seed_bytes = (root / "institution_feeds/pending_intake/imf.json").read_bytes()
    seed = json.loads(seed_bytes)
    candidates = [record["item"] for record in seed["items"].values()
                  if "580315" in record.get("item", {}).get("source_url", "")]
    if len(candidates) != 1:
        raise RuntimeError("Expected exactly one frozen Estonia source")
    source = candidates[0]
    title = source["title"].casefold()
    if ("estonia" not in title or "consumer price index" not in title or
            source.get("pdf_candidates", [None])[0] != EXPECTED_PDF or
            urlsplit(source["source_url"]).hostname != "www.imf.org"):
        raise RuntimeError("Frozen source identity mismatch")
    OUTPUT.mkdir(exist_ok=True)
    report = {"source": {key: source[key] for key in ("title", "source_url", "date")},
              "pdf_url": EXPECTED_PDF, "source_seed_sha256": hashlib.sha256(seed_bytes).hexdigest(),
              "limits": {"max_nodes": MAX_NODES, "concurrency": 4, "request_timeout_seconds": TIMEOUT,
                         "targets_per_node": 3, "max_response_bytes": MAX_BYTES},
              "subscription": {}, "probes": []}
    subscription_url = os.environ.get("PROXY_SUBSCRIPTION_URL", "")
    if not subscription_url:
        report["subscription"]["category"] = "missing_subscription"
        (OUTPUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
        return 1
    # Production performs expiry checks/redaction. Suppress its console output
    # defensively; this probe emits only its own fixed-schema diagnostic rows.
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        body = f._fetch_subscription(subscription_url, TIMEOUT)
    if not body:
        report["subscription"]["category"] = "subscription_unavailable_or_expired"
        (OUTPUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
        return 1
    if "://" not in body.splitlines()[0]:
        body = f._b64_text(body) or body
    counts = Counter()
    detailed_counts = Counter()
    vless_nodes = []
    nodes = []
    for line in body.splitlines():
        if not line.strip():
            continue
        scheme = line.strip().split("://", 1)[0].lower()
        counts[scheme if scheme in SCHEMES else "other"] += 1
        detailed_counts[line_scheme(line)] += 1
        if line_scheme(line) == "vless":
            vless_nodes.append(vless_metadata(line))
        normalized = f._normalize_proxy_node(line)
        if normalized:
            nodes.append(normalized)
    report["subscription"].update(category="retrieved", line_scheme_counts=dict(sorted(counts.items())),
                                   uri_scheme_counts=dict(sorted(detailed_counts.items())), vless_metadata=vless_nodes,
                                   total_normalized_compatible=len(nodes), probed_nodes=0 if args.metadata_only else min(MAX_NODES, len(nodes)))
    print(json.dumps({"subscription": report["subscription"]}), flush=True)
    if args.metadata_only:
        report["mode"] = "metadata_only"
        (OUTPUT / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
        return 0
    targets = (("connectivity", "https://www.gstatic.com/generate_204"),
               ("landing", source["source_url"]), ("pdf", EXPECTED_PDF))
    jobs = [(index, node, name, url) for index, node in enumerate(nodes[:MAX_NODES], 1)
            for name, url in targets]
    with ThreadPoolExecutor(max_workers=4) as pool:
        for row in pool.map(lambda args: probe(*args, f, cffi, PdfReader), jobs):
            report["probes"].append(row)
            print(json.dumps(row, ensure_ascii=False), flush=True)
            (OUTPUT / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    report["accepted_pdf_routes"] = [row["route_index"] for row in report["probes"] if row["accepted_source_pdf"]]
    (OUTPUT / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps({"completed_probes": len(report["probes"]), "accepted_pdf_routes": report["accepted_pdf_routes"]}), flush=True)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({"category": "probe_setup_failed"}), flush=True)
        raise SystemExit(1) from None
