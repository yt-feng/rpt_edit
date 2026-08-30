#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_ROOT = "https://api.cloudflare.com/client/v4"
LAST_VERIFY_FAILURE = "not_started"
ALIAS_REDIRECT_PATHS = ("/", "/reports/", "/robots.txt", "/sitemap.xml")


class CutoverError(Exception):
    pass


def api_json(
    path: str,
    *,
    method: str = "GET",
    body: dict[str, Any] | None = None,
    stage: str = "cloud_api",
) -> Any:
    token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
    if not token:
        raise CutoverError
    data = None if body is None else json.dumps(body, separators=(",", ":")).encode()
    request = urllib.request.Request(
        API_ROOT + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Content-Type": "application/json",
            "Accept": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except (OSError, ValueError, urllib.error.HTTPError):
        raise CutoverError(stage) from None
    if not isinstance(payload, dict) or payload.get("success") is not True:
        raise CutoverError(stage)
    return payload.get("result")


def find_zone_id(hostname: str) -> str:
    labels = hostname.split(".")
    for offset in range(max(1, len(labels) - 1)):
        candidate = ".".join(labels[offset:])
        query = urllib.parse.urlencode({"name": candidate, "status": "active", "per_page": 50})
        result = api_json(f"/zones?{query}", stage="zone_lookup")
        if isinstance(result, list) and len(result) == 1 and isinstance(result[0], dict):
            zone_id = str(result[0].get("id") or "")
            if zone_id:
                return zone_id
    raise CutoverError("zone_not_found")


def exact_route(zone_id: str, pattern: str) -> dict[str, Any] | None:
    result = api_json(f"/zones/{zone_id}/workers/routes", stage="route_list")
    if not isinstance(result, list):
        raise CutoverError
    matches = [row for row in result if isinstance(row, dict) and row.get("pattern") == pattern]
    if len(matches) > 1:
        raise CutoverError("route_ambiguous")
    return matches[0] if matches else None


def delete_edge_route(zone_id: str, pattern: str, script_name: str) -> None:
    route = exact_route(zone_id, pattern)
    if route is None:
        return
    if str(route.get("script") or "") != script_name:
        raise CutoverError("route_conflict")
    route_id = str(route.get("id") or "")
    if not route_id:
        raise CutoverError("route_missing_id")
    api_json(
        f"/zones/{zone_id}/workers/routes/{route_id}",
        method="DELETE",
        stage="route_delete",
    )


def request_status(
    url: str,
    *,
    method: str = "HEAD",
    headers: dict[str, str] | None = None,
) -> tuple[int, dict[str, str], bytes]:
    request_method = method.upper()
    if request_method not in {"GET", "HEAD"}:
        return 0, {}, b""
    try:
        with tempfile.TemporaryDirectory(prefix="edge-route-verify-") as temporary_directory:
            temporary_root = Path(temporary_directory)
            header_path = temporary_root / "headers.txt"
            body_path = temporary_root / "body.bin"
            command = [
                "curl",
                "--silent",
                "--show-error",
                "--max-time",
                "30",
                "--dump-header",
                str(header_path),
                "--output",
                str(body_path),
                "--write-out",
                "%{http_code}",
            ]
            if request_method == "HEAD":
                command.append("--head")
            else:
                command.extend(("--max-filesize", "65536"))
            for key, value in (headers or {}).items():
                command.extend(("--header", f"{key}: {value}"))
            command.extend(("--", url))
            completed = subprocess.run(
                command,
                check=False,
                capture_output=True,
                text=True,
                timeout=35,
            )
            if completed.returncode != 0:
                return 0, {}, b""
            status_text = completed.stdout.strip()
            if len(status_text) != 3 or not status_text.isdigit():
                return 0, {}, b""
            response_headers = parse_curl_headers(header_path.read_bytes())
            response_body = b""
            if request_method == "GET":
                with body_path.open("rb") as response_file:
                    response_body = response_file.read(65536)
            return int(status_text), response_headers, response_body
    except (OSError, subprocess.SubprocessError):
        return 0, {}, b""


def parse_curl_headers(payload: bytes) -> dict[str, str]:
    blocks = payload.replace(b"\r\n", b"\n").split(b"\n\n")
    for block in reversed(blocks):
        lines = block.splitlines()
        if not lines or not lines[0].startswith(b"HTTP/"):
            continue
        response_headers: dict[str, str] = {}
        for line in lines[1:]:
            if b":" not in line:
                continue
            key, value = line.split(b":", 1)
            response_headers[key.decode("latin-1").strip().lower()] = value.decode("latin-1").strip()
        return response_headers
    return {}


def verify_edge(origin: str) -> bool:
    global LAST_VERIFY_FAILURE
    checks = (
        ("/", "HEAD", 200, "text/html"),
        ("/assets/app.js", "HEAD", 200, "javascript"),
        ("/data/catalog.json", "HEAD", 200, "application/json"),
        ("/data/search_index.json", "HEAD", 200, "application/json"),
        ("/api/health", "GET", 200, ""),
        ("/__edge_missing_check__", "GET", 404, ""),
    )
    for path, method, expected_status, expected_type in checks:
        status, headers, _body = request_status(origin + path, method=method)
        if status != expected_status:
            LAST_VERIFY_FAILURE = f"{method} {path} status={status} expected={expected_status}"
            return False
        if path != "/api/health" and headers.get("x-origin-class", "").lower() != "edge-static":
            LAST_VERIFY_FAILURE = f"{method} {path} missing_edge_origin"
            return False
        if expected_type and expected_type not in headers.get("content-type", "").lower():
            LAST_VERIFY_FAILURE = f"{method} {path} unexpected_content_type"
            return False

    status, headers, body = request_status(
        origin + "/data/search_index.json",
        method="GET",
        headers={"Range": "bytes=0-1023"},
    )
    valid = (
        status == 206
        and len(body) == 1024
        and headers.get("x-origin-class", "").lower() == "edge-static"
        and headers.get("content-range", "").lower().startswith("bytes 0-1023/")
    )
    LAST_VERIFY_FAILURE = "" if valid else (
        f"GET /data/search_index.json range_status={status} bytes={len(body)}"
    )
    return valid


def wait_for_edge(origin: str, *, expected: bool, attempts: int = 120) -> bool:
    for attempt in range(attempts):
        active = verify_edge(origin)
        if active is expected:
            return True
        if (attempt + 1) % 12 == 0:
            print(
                f"edge verification pending attempt={attempt + 1}: {LAST_VERIFY_FAILURE}",
                file=sys.stderr,
            )
        time.sleep(5)
    return False


def verify_alias(alias_origin: str, canonical_origin: str) -> bool:
    global LAST_VERIFY_FAILURE
    alias_base = alias_origin.rstrip("/")
    canonical_base = canonical_origin.rstrip("/")
    for path in ALIAS_REDIRECT_PATHS:
        status, headers, _body = request_status(alias_base + path, method="HEAD")
        expected_location = canonical_base + path
        if status != 301:
            LAST_VERIFY_FAILURE = f"HEAD alias {path} status={status} expected=301"
            return False
        if headers.get("x-origin-class", "").lower() != "edge-static":
            LAST_VERIFY_FAILURE = f"HEAD alias {path} missing_edge_origin"
            return False
        location = headers.get("location", "")
        if location != expected_location:
            LAST_VERIFY_FAILURE = (
                f"HEAD alias {path} location={location!r} expected={expected_location!r}"
            )
            return False
    LAST_VERIFY_FAILURE = ""
    return True


def wait_for_alias(alias_origin: str, canonical_origin: str, attempts: int = 120) -> bool:
    for attempt in range(attempts):
        if verify_alias(alias_origin, canonical_origin):
            return True
        if (attempt + 1) % 12 == 0:
            print(
                f"alias verification pending attempt={attempt + 1}: {LAST_VERIFY_FAILURE}",
                file=sys.stderr,
            )
        time.sleep(5)
    return False


def migrate(zone_id: str, pattern: str, origin: str, script_name: str) -> None:
    route = exact_route(zone_id, pattern)
    if route is not None and str(route.get("script") or "") != script_name:
        raise CutoverError("route_conflict")
    created = route is None
    if created:
        result = api_json(
            f"/zones/{zone_id}/workers/routes",
            method="POST",
            body={"pattern": pattern, "script": script_name},
            stage="route_create",
        )
        if not isinstance(result, dict) or not result.get("id"):
            raise CutoverError("route_create")
    try:
        if not wait_for_edge(origin, expected=True):
            raise CutoverError("edge_verify")
    except Exception:
        if created:
            try:
                delete_edge_route(zone_id, pattern, script_name)
                wait_for_edge(origin, expected=False, attempts=18)
            except Exception:
                pass
        raise


def rollback(zone_id: str, pattern: str, origin: str, script_name: str) -> None:
    delete_edge_route(zone_id, pattern, script_name)
    if not wait_for_edge(origin, expected=False, attempts=18):
        raise CutoverError


def migrate_alias(zone_id: str, pattern: str, origin: str, canonical_origin: str, script_name: str) -> None:
    route = exact_route(zone_id, pattern)
    if route is not None and str(route.get("script") or "") != script_name:
        raise CutoverError("route_conflict")
    created = route is None
    if created:
        result = api_json(
            f"/zones/{zone_id}/workers/routes",
            method="POST",
            body={"pattern": pattern, "script": script_name},
            stage="route_create",
        )
        if not isinstance(result, dict) or not result.get("id"):
            raise CutoverError("route_create")
    try:
        if not wait_for_alias(origin, canonical_origin):
            raise CutoverError("edge_verify")
    except Exception:
        if created:
            try:
                delete_edge_route(zone_id, pattern, script_name)
            except Exception:
                pass
        raise


def configured_alias_hosts(hostname: str) -> list[str]:
    values = []
    for value in os.environ.get("EDGE_ALIAS_HOSTS", "").split(","):
        alias = value.strip().lower()
        if not alias or alias == hostname or "/" in alias or ":" in alias or "." not in alias:
            continue
        if alias not in values:
            values.append(alias)
    return values


def purge_edge_cache(zone_id: str) -> None:
    api_json(
        f"/zones/{zone_id}/purge_cache",
        method="POST",
        body={"purge_everything": True},
        stage="cache_purge",
    )


def run() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"migrate", "rollback", "verify", "purge"}:
        return 2
    hostname = os.environ.get("SITE_HOST", "").strip().lower()
    script_name = os.environ.get("EDGE_SCRIPT_NAME", "").strip()
    if not hostname or "/" in hostname or not script_name:
        return 2
    origin = "https://" + hostname
    pattern = hostname + "/*"
    aliases = configured_alias_hosts(hostname)
    try:
        if sys.argv[1] == "verify":
            if not wait_for_edge(origin, expected=True):
                raise CutoverError("edge_verify")
            for alias in aliases:
                if not wait_for_alias("https://" + alias, origin):
                    raise CutoverError("edge_verify")
            print("edge route verified")
            return 0
        zone_id = find_zone_id(hostname)
        if sys.argv[1] == "purge":
            purge_edge_cache(zone_id)
            print("edge cache purged")
        elif sys.argv[1] == "migrate":
            migrate(zone_id, pattern, origin, script_name)
            for alias in aliases:
                migrate_alias(zone_id, alias + "/*", "https://" + alias, origin, script_name)
            print("edge route verified")
        else:
            for alias in aliases:
                delete_edge_route(zone_id, alias + "/*", script_name)
            rollback(zone_id, pattern, origin, script_name)
            print("edge route restored")
    except Exception:
        stage = str(sys.exc_info()[1] or "unknown")
        if stage not in {
            "zone_lookup",
            "zone_not_found",
            "route_list",
            "route_ambiguous",
            "route_conflict",
            "route_missing_id",
            "route_create",
            "route_delete",
            "edge_verify",
            "cache_purge",
            "cloud_api",
        }:
            stage = "unknown"
        print(f"edge route operation failed: {stage}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
