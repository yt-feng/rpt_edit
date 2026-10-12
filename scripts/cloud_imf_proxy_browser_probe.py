"""One approved GHA-only browser download over one existing subscription route.

No local execution, system networking changes, direct fallback or session export.
Node receives only an ephemeral SOCKS port, never subscription/node credentials.
"""
from __future__ import annotations

import argparse
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
from urllib.parse import urlsplit

import cloud_imf_protocol_client_probe as client

OUT = Path("_imf_browser_probe")
BRANCH = "codex/imf-proxy-browser-20261013"
SHA = "c31da5c22e845f767b39a0a16679c0f1249ce46b5f60bd0170bdb67964e663b3"
SIZE = 365715
VERSION = "1.14.3"
SAFE_ENV = {"PATH", "HOME", "RUNNER_TEMP", "PLAYWRIGHT_PACKAGE_ROOT",
            "PLAYWRIGHT_BROWSERS_PATH", "LANG", "LC_ALL", "DISPLAY", "XAUTHORITY"}


class ProbeFailure(ValueError):
    pass


def require_approval():
    client.require_cloud()
    expected = f"yt-feng/rpt_edit/.github/workflows/institution-fetch-test.yml@refs/heads/{BRANCH}"
    if (os.environ.get("EXPLICIT_CLOUD_BROWSER_APPROVAL") != "true"
            or os.environ.get("GITHUB_REPOSITORY") != "yt-feng/rpt_edit"
            or os.environ.get("GITHUB_EVENT_NAME") != "workflow_dispatch"
            or os.environ.get("GITHUB_WORKFLOW_REF") != expected):
        raise ProbeFailure("cloud_browser_not_authorized")


def select_outbound(body, decode):
    """Select only a unique valid VLESS TCP/Reality entry; never try other nodes."""
    if not isinstance(body, str) or not body.strip() or len(body) > 2_000_000:
        raise ProbeFailure("subscription_unavailable_or_expired")
    if "://" not in body.splitlines()[0]:
        body = decode(body) or ""
    accepted = []
    candidates = 0
    for line in body.splitlines():
        if not line.strip().lower().startswith("vless://"):
            continue
        candidates += 1
        if candidates > 64:
            raise ProbeFailure("subscription_node_limit")
        try:
            outbound = client.build_outbound(line)
        except client.UnsupportedNode:
            continue
        if outbound["type"] == "vless":
            accepted.append(outbound)
    if len(accepted) != 1:
        raise ProbeFailure("unique_valid_vless_required")
    return accepted[0]


def browser_environment(proxy):
    parsed = urlsplit(proxy)
    if (parsed.scheme != "socks5h" or parsed.hostname != "127.0.0.1"
            or parsed.username is not None or parsed.password is not None
            or parsed.path or parsed.query or parsed.fragment
            or parsed.port is None or not 1 <= parsed.port <= 65535):
        raise ProbeFailure("invalid_cloud_listener")
    env = {key: value for key, value in os.environ.items() if key in SAFE_ENV}
    env.update(GITHUB_ACTIONS="true", EXPLICIT_CLOUD_BROWSER_APPROVAL="true",
               IMF_CLOUD_SOCKS_PORT=str(parsed.port))
    return env


def connectivity(proxy, cffi, nop_proxy_option):
    """Exactly one small request, explicit route, no redirect/retry or body read."""
    response = None
    try:
        response = cffi.get("https://www.gstatic.com/generate_204", timeout=8,
                            proxies={"http": proxy, "https": proxy},
                            curl_options={nop_proxy_option: ""},
                            allow_redirects=False, stream=True)
        status = int(response.status_code)
        return {"status": status, "accepted": status == 204,
                "category": "connectivity_verified" if status == 204 else "connectivity_http_rejected"}
    except Exception:
        return {"status": None, "accepted": False, "category": "connectivity_request_failed"}
    finally:
        if response is not None:
            response.close()


def run_browser(proxy):
    """Close the browser process group before the caller closes its client."""
    proc = subprocess.Popen(["node", "scripts/cloud_imf_browser_probe.cjs"],
                            env=browser_environment(proxy), start_new_session=True,
                            stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                            stderr=subprocess.DEVNULL)
    try:
        try:
            return proc.wait(timeout=150)
        except subprocess.TimeoutExpired:
            raise ProbeFailure("browser_process_timeout") from None
    finally:
        if proc.poll() is None:
            os.killpg(proc.pid, signal.SIGTERM)
            try:
                proc.wait(timeout=8)
            except subprocess.TimeoutExpired:
                os.killpg(proc.pid, signal.SIGKILL)
                proc.wait(timeout=3)


def verify_pdf(folder, reader_class):
    target = folder / f"{SHA}.pdf"
    if not target.is_file() or target.stat().st_size != SIZE:
        raise ProbeFailure("pdf_size_mismatch")
    data = target.read_bytes()
    if not data.startswith(b"%PDF-") or hashlib.sha256(data).hexdigest() != SHA:
        raise ProbeFailure("pdf_bytes_mismatch")
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        reader = reader_class(io.BytesIO(data))
        if reader.is_encrypted or len(reader.pages) != 14:
            raise ProbeFailure("pdf_pages_mismatch")
        text = " ".join((page.extract_text() or "") for page in reader.pages[:3]).casefold()
    if not all(term in text for term in ("estonia", "consumer price index", "2026")):
        raise ProbeFailure("pdf_source_identity_mismatch")
    return {"sha256": SHA, "bytes": SIZE, "pages": 14, "source_identity_match": True}


def main():
    require_approval()  # Before secret access, imports with network clients or subprocesses.
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--sing-box", type=Path, required=True)
    args = parser.parse_args()
    report = {"accepted": False, "source": "normal_official_browser_via_existing_cloud_subscription",
              "route": "unique_vless_tcp_reality", "max_routes": 1,
              "connectivity_requests": 1, "browser_reports": 1}
    OUT.mkdir(exist_ok=False)
    save = lambda: (OUT / "summary.json").write_text(json.dumps(report, indent=2) + "\n")
    save()
    try:
        binary = args.sing_box.resolve(strict=True)
        result = subprocess.run([str(binary), "version"], capture_output=True, text=True,
                                timeout=5, check=False)
        if result.returncode or not re.search(r"^sing-box version " + re.escape(VERSION) + r"\s*$", result.stdout, re.M):
            raise ProbeFailure("runtime_version_mismatch")
        import fetch_institution_latest_pdfs as fetcher
        from curl_cffi import requests as cffi, CurlOpt
        from pypdf import PdfReader
        subscription = os.environ.get("PROXY_SUBSCRIPTION_URL", "")
        if not subscription:
            raise ProbeFailure("missing_subscription")
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            body = fetcher._fetch_subscription(subscription, 8)
        outbound = select_outbound(body, fetcher._b64_text)
        with client.running_client(binary, outbound) as proxy:
            report["connectivity"] = connectivity(proxy, cffi, CurlOpt.NOPROXY)
            save()
            if not report["connectivity"]["accepted"]:
                raise ProbeFailure(report["connectivity"]["category"])
            exit_code = run_browser(proxy)
            browser_report = json.loads((OUT / "browser-summary.json").read_text())
            report["browser"] = browser_report
            if exit_code or not browser_report.get("bytes_verified"):
                raise ProbeFailure("browser_download_not_verified")
            report["pdf"] = verify_pdf(OUT, PdfReader)
            report.update(category="verified_official_pdf", accepted=True)
    except ProbeFailure as error:
        report["category"] = str(error)
    except client.UnsupportedNode as error:
        report["category"] = error.code
    except (KeyboardInterrupt, SystemExit):
        report["category"] = "probe_interrupted"
    except Exception:
        report["category"] = "proxy_browser_probe_failed"
    finally:
        save()
    print(json.dumps(report), flush=True)
    return 0 if report["accepted"] else 1


if __name__ == "__main__":
    def terminate(_signal, _frame):
        raise KeyboardInterrupt
    signal.signal(signal.SIGTERM, terminate)
    try:
        raise SystemExit(main())
    except Exception:
        print(json.dumps({"accepted": False, "category": "proxy_browser_setup_failed"}), flush=True)
        raise SystemExit(1) from None
