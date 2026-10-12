"""Cloud-only, bounded IMF probe through the existing subscription protocols.

Uses an official workflow-pinned sing-box binary, never a system installation.
Only this process's ephemeral runner-loopback SOCKS listener is used. No TUN,
system proxy, DNS configuration, routes, daemon installation or raw client logs.

Configuration references:
https://sing-box.sagernet.org/configuration/outbound/{vless,hysteria2,tuic}/
https://sing-box.sagernet.org/configuration/shared/tls/
https://v2.hysteria.network/docs/developers/URI-Scheme/
https://github.com/XTLS/Xray-core/discussions/716
"""
from __future__ import annotations

import argparse
import base64
from collections import Counter
import contextlib
import hashlib
import importlib
import io
import json
import logging
import os
from pathlib import Path
import re
import signal
import socket
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote, urlsplit
import uuid

MAX_NODES = 9
OUTPUT = Path("_imf_protocol_client_probe")
PROTOCOLS = {"vless", "hysteria2", "hy2", "tuic"}
TLS_KEYS = {"sni", "alpn", "insecure", "allowInsecure", "allow_insecure"}
QUERY_KEYS = {
    "vless": TLS_KEYS | {"type", "security", "encryption", "fp", "pbk", "sid", "flow"},
    "hysteria2": TLS_KEYS | {"obfs", "obfs-password"},
    "tuic": TLS_KEYS | {"congestion_control", "udp_relay_mode"},
}
ERROR_CODES = {"invalid_uri", "unsupported_protocol", "unknown_query_parameter", "duplicate_query_parameter",
               "tls_verification_required", "missing_required_parameter", "unsupported_parameter_value",
               "runtime_check_failed", "runtime_check_timeout", "runtime_start_failed", "runtime_start_timeout"}


class UnsupportedNode(ValueError):
    def __init__(self, code):
        self.code = code if code in ERROR_CODES else "invalid_uri"
        super().__init__(self.code)


def require_cloud():
    if os.environ.get("GITHUB_ACTIONS") != "true" or sys.platform != "linux":
        raise RuntimeError("cloud_only")


def decoded(value):
    if re.search(r"%(?![0-9A-Fa-f]{2})", value):
        raise UnsupportedNode("invalid_uri")
    result = unquote(value, encoding="utf-8", errors="strict")
    if any(ord(char) < 32 or ord(char) == 127 for char in result):
        raise UnsupportedNode("invalid_uri")
    return result


def parsed_node(line):
    """Decode values exactly once; preserve literal '+' and case-sensitive keys."""
    try:
        text = line.strip()
        if len(text) > 8192 or any(ord(char) <= 32 or ord(char) == 127 for char in text):
            raise UnsupportedNode("invalid_uri")
        uri = urlsplit(text)
        scheme = "hysteria2" if uri.scheme == "hy2" else uri.scheme
        if scheme not in QUERY_KEYS:
            raise UnsupportedNode("unsupported_protocol")
        if not uri.hostname or uri.path not in ("", "/") or not uri.username:
            raise UnsupportedNode("invalid_uri")
        port = uri.port if uri.port is not None else 443 if scheme == "hysteria2" else None
        if port is None or not 1 <= port <= 65535:
            raise UnsupportedNode("invalid_uri")
        pairs = []
        for item in uri.query.split("&") if uri.query else []:
            key, separator, value = item.partition("=")
            if not separator or not key or len(pairs) >= 32:
                raise UnsupportedNode("invalid_uri")
            pairs.append((decoded(key), decoded(value)))
        if len({key for key, _ in pairs}) != len(pairs):
            raise UnsupportedNode("duplicate_query_parameter")
        return uri, scheme, port, dict(pairs)
    except UnsupportedNode:
        raise
    except Exception:
        raise UnsupportedNode("invalid_uri") from None


def safe_metadata(line):
    try:
        _, scheme, port, query = parsed_node(line)
        return {"protocol": scheme, "port": port,
                "query_keys": sorted(set(query) & QUERY_KEYS[scheme]),
                "unknown_query_key_count": len(set(query) - QUERY_KEYS[scheme])}
    except UnsupportedNode as error:
        return {"parse_category": error.code}


def required(query, key):
    if not query.get(key):
        raise UnsupportedNode("missing_required_parameter")
    return query[key]


def tls_config(query, hostname):
    for key in ("insecure", "allowInsecure", "allow_insecure"):
        if key in query and query[key].lower() not in ("0", "false"):
            raise UnsupportedNode("tls_verification_required")
    server_name = query.get("sni", hostname)
    if not server_name or any(char.isspace() or char in "/?#@" for char in server_name):
        raise UnsupportedNode("invalid_uri")
    tls = {"enabled": True, "server_name": server_name}
    if "alpn" in query:
        alpn = query["alpn"].split(",")
        if not alpn or any(value not in {"h2", "http/1.1", "h3", "h3-29"} for value in alpn):
            raise UnsupportedNode("unsupported_parameter_value")
        tls["alpn"] = alpn
    return tls


def build_outbound(line):
    """Build only documented, reviewed parameters; reject every unknown key."""
    uri, scheme, port, query = parsed_node(line)
    if set(query) - QUERY_KEYS[scheme]:
        raise UnsupportedNode("unknown_query_parameter")
    tls = tls_config(query, uri.hostname)
    outbound = {"type": scheme, "tag": "subscription-route", "server": uri.hostname,
                "server_port": port, "network": "tcp", "tls": tls}
    if scheme == "vless":
        if uri.password is not None or query.get("type") != "tcp" or query.get("security") != "reality":
            raise UnsupportedNode("unsupported_parameter_value")
        if query.get("encryption", "none") != "none":
            raise UnsupportedNode("unsupported_parameter_value")
        try:
            outbound["uuid"] = str(uuid.UUID(decoded(uri.username)))
        except Exception:
            raise UnsupportedNode("invalid_uri") from None
        public_key = required(query, "pbk")
        if not re.fullmatch(r"[A-Za-z0-9_-]{43}", public_key) or len(base64.urlsafe_b64decode(public_key + "=")) != 32:
            raise UnsupportedNode("invalid_uri")
        short_id = query.get("sid", "")
        if not re.fullmatch(r"(?:[0-9a-fA-F]{2}){0,8}", short_id):
            raise UnsupportedNode("invalid_uri")
        fingerprint = required(query, "fp")
        if fingerprint not in {"chrome", "firefox", "edge", "safari", "360", "qq", "ios", "android", "random", "randomized"}:
            raise UnsupportedNode("unsupported_parameter_value")
        tls["server_name"] = required(query, "sni")
        tls["utls"] = {"enabled": True, "fingerprint": fingerprint}
        tls["reality"] = {"enabled": True, "public_key": public_key, "short_id": short_id}
        if query.get("flow"):
            if query["flow"] != "xtls-rprx-vision":
                raise UnsupportedNode("unsupported_parameter_value")
            outbound["flow"] = query["flow"]
    elif scheme == "hysteria2":
        # The official URI uses all userinfo as auth, including user:password.
        outbound["password"] = decoded(uri.netloc.rsplit("@", 1)[0])
        if not outbound["password"]:
            raise UnsupportedNode("missing_required_parameter")
        if "obfs" in query or "obfs-password" in query:
            if required(query, "obfs") != "salamander":
                raise UnsupportedNode("unsupported_parameter_value")
            outbound["obfs"] = {"type": "salamander", "password": required(query, "obfs-password")}
    else:
        try:
            outbound["uuid"] = str(uuid.UUID(decoded(uri.username)))
        except Exception:
            raise UnsupportedNode("invalid_uri") from None
        if not uri.password:
            raise UnsupportedNode("missing_required_parameter")
        outbound["password"] = decoded(uri.password)
        for key, choices in (("congestion_control", {"cubic", "new_reno", "bbr"}),
                             ("udp_relay_mode", {"native", "quic"})):
            if key in query:
                if query[key] not in choices:
                    raise UnsupportedNode("unsupported_parameter_value")
                outbound[key] = query[key]
    return outbound


def client_config(outbound, port):
    if not 1 <= port <= 65535:
        raise UnsupportedNode("invalid_uri")
    return {"log": {"disabled": True},
            "inbounds": [{"type": "socks", "tag": "probe-input", "listen": "127.0.0.1", "listen_port": port}],
            "outbounds": [outbound]}


@contextlib.contextmanager
def running_client(binary, outbound):
    require_cloud()
    process = None
    # Only reserve this test's new loopback listener on an ephemeral cloud runner.
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as reserved:
        reserved.bind(("127.0.0.1", 0))
        port = reserved.getsockname()[1]
    with tempfile.TemporaryDirectory(prefix="imf-protocol-", dir=os.environ.get("RUNNER_TEMP")) as directory:
        os.chmod(directory, 0o700)
        path = Path(directory) / "client.json"
        descriptor = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(descriptor, "w") as stream:
            json.dump(client_config(outbound, port), stream)
        try:
            try:
                checked = subprocess.run([str(binary), "check", "-c", str(path)],
                                         stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                         stderr=subprocess.DEVNULL, cwd=directory, timeout=8, check=False)
            except subprocess.TimeoutExpired:
                raise UnsupportedNode("runtime_check_timeout") from None
            if checked.returncode:
                raise UnsupportedNode("runtime_check_failed")
            process = subprocess.Popen([str(binary), "run", "-c", str(path)],
                                       stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL,
                                       stderr=subprocess.DEVNULL, cwd=directory)
            deadline = time.monotonic() + 5
            while True:
                if process.poll() is not None:
                    raise UnsupportedNode("runtime_start_failed")
                try:
                    with socket.create_connection(("127.0.0.1", port), timeout=0.2):
                        break
                except OSError:
                    if time.monotonic() >= deadline:
                        raise UnsupportedNode("runtime_start_timeout") from None
                    time.sleep(0.1)
            yield f"socks5h://127.0.0.1:{port}"
        finally:
            if process is not None and process.poll() is None:
                process.terminate()
                try:
                    process.wait(timeout=3)
                except subprocess.TimeoutExpired:
                    process.kill()
                    process.wait(timeout=3)


def main():
    require_cloud()
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--production-root", type=Path, default=Path("."))
    parser.add_argument("--sing-box", type=Path, required=True)
    parser.add_argument("--expected-version", required=True)
    args = parser.parse_args()
    binary = args.sing_box.resolve(strict=True)
    if not re.fullmatch(r"[0-9]+\.[0-9]+\.[0-9]+", args.expected_version):
        raise RuntimeError("invalid_runtime_version")
    version = subprocess.run([str(binary), "version"], capture_output=True, text=True, timeout=5, check=True)
    if not re.search(r"^sing-box version " + re.escape(args.expected_version) + r"\s*$", version.stdout, re.M):
        raise RuntimeError("runtime_version_mismatch")
    root = args.production_root.resolve()
    sys.path.insert(0, str(root / "scripts"))
    f = importlib.import_module("fetch_institution_latest_pdfs")
    if not hasattr(f, "_subscription_expired"):
        raise RuntimeError("current_production_required")
    import cloud_imf_current_proxy_probe as p
    from curl_cffi import requests as cffi
    from pypdf import PdfReader
    logging.getLogger("pypdf").disabled = True
    OUTPUT.mkdir(exist_ok=True)
    p.OUTPUT = OUTPUT
    seed_bytes = (root / "institution_feeds/pending_intake/imf.json").read_bytes()
    seed = json.loads(seed_bytes)
    sources = [record["item"] for record in seed["items"].values()
               if "580315" in record.get("item", {}).get("source_url", "")]
    if len(sources) != 1:
        raise RuntimeError("source_identity_mismatch")
    source = sources[0]
    if ("estonia" not in source["title"].casefold() or "consumer price index" not in source["title"].casefold()
            or source.get("pdf_candidates", [None])[0] != p.EXPECTED_PDF
            or urlsplit(source["source_url"]).hostname != "www.imf.org"):
        raise RuntimeError("source_identity_mismatch")
    report = {"runtime": {"version": args.expected_version, "sha256": hashlib.sha256(binary.read_bytes()).hexdigest()},
              "source": {key: source[key] for key in ("title", "source_url", "date")},
              "pdf_url": p.EXPECTED_PDF, "source_seed_sha256": hashlib.sha256(seed_bytes).hexdigest(),
              "limits": {"max_nodes": MAX_NODES, "targets_per_node": 2, "concurrency": 1, "request_timeout_seconds": p.TIMEOUT},
              "routes": [], "probes": []}

    def save():
        (OUTPUT / "summary.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")

    subscription = os.environ.get("PROXY_SUBSCRIPTION_URL", "")
    if not subscription:
        report["category"] = "missing_subscription"
        save()
        return 1
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        body = f._fetch_subscription(subscription, p.TIMEOUT)
    if not body:
        report["category"] = "subscription_unavailable_or_expired"
        save()
        return 1
    if "://" not in body.splitlines()[0]:
        body = f._b64_text(body) or body
    lines = [line.strip() for line in body.splitlines() if p.line_scheme(line) in PROTOCOLS]
    report["subscription"] = {"protocol_counts": dict(Counter(p.line_scheme(line) for line in lines)),
                              "available_protocol_nodes": len(lines), "selected_nodes": min(MAX_NODES, len(lines))}
    print(json.dumps({"subscription": report["subscription"]}), flush=True)
    save()
    for index, line in enumerate(lines[:MAX_NODES], 1):
        route = {"route_index": index, **safe_metadata(line)}
        report["routes"].append(route)
        try:
            outbound = build_outbound(line)
            with running_client(binary, outbound) as proxy:
                route["category"] = "client_started"
                for target, url in (("connectivity", "https://www.gstatic.com/generate_204"), ("pdf", p.EXPECTED_PDF)):
                    row = p.probe(index, proxy, target, url, f, cffi, PdfReader)
                    row["route_scheme"] = outbound["type"]
                    report["probes"].append(row)
                    print(json.dumps(row, ensure_ascii=False), flush=True)
                    save()
        except UnsupportedNode as error:
            route["category"] = error.code
        except Exception:
            route["category"] = "client_probe_failed"
        print(json.dumps({"route": route}), flush=True)
        save()
    report["accepted_pdf_routes"] = [row["route_index"] for row in report["probes"] if row["accepted_source_pdf"]]
    save()
    print(json.dumps({"completed_probes": len(report["probes"]), "accepted_pdf_routes": report["accepted_pdf_routes"]}), flush=True)
    return 0


if __name__ == "__main__":
    def terminate(_signal, _frame):
        raise SystemExit(143)
    signal.signal(signal.SIGTERM, terminate)
    try:
        raise SystemExit(main())
    except (Exception, KeyboardInterrupt):
        print(json.dumps({"category": "protocol_probe_setup_failed"}), flush=True)
        raise SystemExit(1) from None
