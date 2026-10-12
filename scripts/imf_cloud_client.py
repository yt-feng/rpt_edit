"""Cloud-only strict VLESS TCP/Reality client, extracted from the validated probe.

No TUN, global DNS/routing/system proxy settings or raw client output.
Temporary 0700/0600 configuration and process cleanup are scoped to the batch.
Reference: https://sing-box.sagernet.org/configuration/outbound/vless/
"""
from __future__ import annotations
import base64
import contextlib
import json
import os
from pathlib import Path
import re
import socket
import subprocess
import sys
import tempfile
import time
from urllib.parse import unquote, urlsplit
import uuid

TLS_KEYS = {"sni", "alpn", "insecure", "allowInsecure", "allow_insecure"}
QUERY_KEYS = {"vless": TLS_KEYS | {"type", "security", "encryption", "fp", "pbk", "sid", "flow"}}
ERROR_CODES = {"invalid_uri", "unsupported_protocol", "unknown_query_parameter", "duplicate_query_parameter",
               "tls_verification_required", "missing_required_parameter", "unsupported_parameter_value",
               "runtime_check_failed", "runtime_check_timeout", "runtime_start_failed", "runtime_start_timeout"}

class UnsupportedNode(ValueError):
    def __init__(self, code):
        self.code = code if code in ERROR_CODES else "invalid_uri"
        super().__init__(self.code)


def require_cloud():
    if (os.environ.get("GITHUB_ACTIONS") != "true" or sys.platform != "linux"
            or os.environ.get("EXPLICIT_CLOUD_BROWSER_APPROVAL") != "true"):
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
        scheme = uri.scheme
        if scheme not in QUERY_KEYS:
            raise UnsupportedNode("unsupported_protocol")
        if not uri.hostname or uri.path not in ("", "/") or not uri.username:
            raise UnsupportedNode("invalid_uri")
        port = uri.port
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
