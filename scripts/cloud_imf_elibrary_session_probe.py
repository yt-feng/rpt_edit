"""Cloud-only exact-source probe using a coherent browser HTTP profile.

Tests the official download link observed on the exact eLibrary report page.
No browser process, system network changes, or exported browser cookies.
"""
from __future__ import annotations

import contextlib
import io
import json
import logging
import os
from pathlib import Path
import sys

LANDING = "https://www.elibrary.imf.org/view/journals/019/2026/082/019.2026.issue-082-en.xml?cid=580315-com-dsp-crossref"
PDF = "https://www.elibrary.imf.org/downloadpdf/view/journals/019/2026/082/019.2026.issue-082-en.pdf"
EXPECTED_SHA256 = "c31da5c22e845f767b39a0a16679c0f1249ce46b5f60bd0170bdb67964e663b3"
OUTPUT = Path("_imf_elibrary_session_probe")


class CoherentSession:
    def __init__(self, session, direct, curl_opt, coherent=True):
        self.session, self.direct, self.curl_opt = session, direct, curl_opt
        self.coherent = coherent

    def get(self, url, **kwargs):
        # curl_cffi supplies a User-Agent matching its selected TLS/HTTP profile.
        headers = dict(kwargs.get("headers", {}))
        if self.coherent:
            headers.pop("User-Agent", None)
        if url == PDF:
            headers["Referer"] = LANDING
        kwargs["headers"] = headers
        if self.direct:
            kwargs["curl_options"][self.curl_opt.PROXY] = ""
        return self.session.get(url, **kwargs)


def main():
    if os.environ.get("GITHUB_ACTIONS") != "true" or sys.platform != "linux":
        raise RuntimeError("cloud_only")
    from curl_cffi import CurlOpt, requests as cffi
    from pypdf import PdfReader
    import fetch_institution_latest_pdfs as f
    import cloud_imf_current_proxy_probe as p
    logging.getLogger("pypdf").disabled = True
    OUTPUT.mkdir(exist_ok=True)
    p.OUTPUT = OUTPUT
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        body = f._fetch_subscription(os.environ.get("PROXY_SUBSCRIPTION_URL", ""), 8)
    if not body:
        raise RuntimeError("subscription_unavailable")
    if "://" not in body.splitlines()[0]:
        body = f._b64_text(body) or body
    nodes = [node for line in body.splitlines() if (node := f._normalize_proxy_node(line))]
    # These indices were verified to return generic 204 in the same subscription.
    chosen = [(0, "")] + [(index, nodes[index - 1]) for index in (2, 4, 5)
                            if len(nodes) >= index and nodes[index - 1].startswith("https://")]
    report = {"landing": LANDING, "pdf_url": PDF, "expected_pdf_sha256": EXPECTED_SHA256,
              "expected_pages": 14, "max_routes": 4, "probes": []}
    def save():
        (OUTPUT / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    save()
    for index, node in chosen:
        for coherent in (True, False):
            with cffi.Session() as session:
                client = CoherentSession(session, not node, CurlOpt, coherent)
                targets = [("landing", LANDING), ("pdf", PDF)]
                if coherent:
                    targets.append(("main_pdf", p.EXPECTED_PDF))
                for target, url in targets:
                    row = p.probe(index, node, "pdf" if target == "main_pdf" else target, url, f, client, PdfReader)
                    row["target"] = target
                    row["profile"] = "coherent" if coherent else "existing_fixed_ua"
                    row["route_kind"] = "direct" if not node else "existing_subscription_https"
                    row["matches_browser_verified_bytes"] = row.get("sha256") == EXPECTED_SHA256
                    row["accepted_source_pdf"] = bool(row["accepted_source_pdf"] and row.get("pages") == 14
                                                       and row["matches_browser_verified_bytes"])
                    report["probes"].append(row)
                    print(json.dumps(row, ensure_ascii=False), flush=True)
                    save()
    report["accepted_pdf_routes"] = [{"route_index": r["route_index"], "target": r["target"], "profile":r["profile"]}
                                      for r in report["probes"] if r["accepted_source_pdf"]]
    save()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({"category": "elibrary_probe_setup_failed"}), flush=True)
        raise SystemExit(1) from None
