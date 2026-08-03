#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from typing import Any


API_ROOT = "https://api.cloudflare.com/client/v4"


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


def request_status(url: str, *, method: str = "HEAD", headers: dict[str, str] | None = None) -> tuple[int, dict[str, str], bytes]:
    request = urllib.request.Request(url, method=method, headers=headers or {})
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            return response.status, {key.lower(): value for key, value in response.headers.items()}, response.read(65536)
    except urllib.error.HTTPError as error:
        return error.code, {key.lower(): value for key, value in error.headers.items()}, error.read(65536)
    except OSError:
        return 0, {}, b""


def verify_edge(origin: str) -> bool:
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
            return False
        if path != "/api/health" and headers.get("x-origin-class", "").lower() != "edge-static":
            return False
        if expected_type and expected_type not in headers.get("content-type", "").lower():
            return False

    status, headers, body = request_status(
        origin + "/data/search_index.json",
        method="GET",
        headers={"Range": "bytes=0-1023"},
    )
    return (
        status == 206
        and len(body) == 1024
        and headers.get("x-origin-class", "").lower() == "edge-static"
        and headers.get("content-range", "").lower().startswith("bytes 0-1023/")
    )


def wait_for_edge(origin: str, *, expected: bool, attempts: int = 36) -> bool:
    for _attempt in range(attempts):
        active = verify_edge(origin)
        if active is expected:
            return True
        time.sleep(5)
    return False


def migrate(zone_id: str, pattern: str, origin: str, script_name: str) -> None:
    route = exact_route(zone_id, pattern)
    if route is not None and str(route.get("script") or "") != script_name:
        raise CutoverError("route_conflict")
    if route is None:
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
        try:
            delete_edge_route(zone_id, pattern, script_name)
            wait_for_edge(origin, expected=False, attempts=18)
        finally:
            raise CutoverError from None


def rollback(zone_id: str, pattern: str, origin: str, script_name: str) -> None:
    delete_edge_route(zone_id, pattern, script_name)
    if not wait_for_edge(origin, expected=False, attempts=18):
        raise CutoverError


def run() -> int:
    if len(sys.argv) != 2 or sys.argv[1] not in {"migrate", "rollback"}:
        return 2
    hostname = os.environ.get("SITE_HOST", "").strip().lower()
    script_name = os.environ.get("EDGE_SCRIPT_NAME", "").strip()
    if not hostname or "/" in hostname or not script_name:
        return 2
    origin = "https://" + hostname
    pattern = hostname + "/*"
    try:
        zone_id = find_zone_id(hostname)
        if sys.argv[1] == "migrate":
            migrate(zone_id, pattern, origin, script_name)
            print("edge route verified")
        else:
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
            "cloud_api",
        }:
            stage = "unknown"
        print(f"edge route operation failed: {stage}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(run())
