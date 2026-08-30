#!/usr/bin/env python3
"""Manually purge a fixed allowlist of canonical URLs from Cloudflare."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from dataclasses import dataclass
from typing import Any, Iterable


API_ROOT = "https://api.cloudflare.com/client/v4"
CANONICAL_PATHS = (
    "/",
    "/reports/",
    "/blog/",
    "/reports/institutions/bernstein/",
    "/sitemap.xml",
    "/robots.txt",
    "/llms.txt",
)


@dataclass(frozen=True)
class CloudflareFailure(Exception):
    stage: str
    http_status: int | None
    errors: tuple[tuple[int | None, str], ...] = ()


def _safe_message(value: Any) -> str:
    message = re.sub(r"\s+", " ", str(value or "")).strip()
    return message[:200] or "unspecified error"


def _cloudflare_errors(payload: Any) -> tuple[tuple[int | None, str], ...]:
    if not isinstance(payload, dict):
        return ()
    rows = payload.get("errors")
    if not isinstance(rows, list):
        return ()
    errors: list[tuple[int | None, str]] = []
    for row in rows[:10]:
        if not isinstance(row, dict):
            continue
        raw_code = row.get("code")
        try:
            code = int(raw_code)
        except (TypeError, ValueError):
            code = None
        errors.append((code, _safe_message(row.get("message"))))
    return tuple(errors)


def _decode_payload(raw: bytes) -> Any:
    try:
        return json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError):
        return None


def api_request(
    path: str,
    *,
    token: str,
    stage: str,
    method: str = "GET",
    body: dict[str, Any] | None = None,
) -> Any:
    data = None if body is None else json.dumps(body, separators=(",", ":")).encode("utf-8")
    request = urllib.request.Request(
        API_ROOT + path,
        data=data,
        method=method,
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            status = int(response.status)
            payload = _decode_payload(response.read(65537))
    except urllib.error.HTTPError as exc:
        payload = _decode_payload(exc.read(65537))
        raise CloudflareFailure(stage, int(exc.code), _cloudflare_errors(payload)) from None
    except (OSError, TimeoutError):
        raise CloudflareFailure(stage, None) from None

    if not isinstance(payload, dict) or payload.get("success") is not True:
        raise CloudflareFailure(stage, status, _cloudflare_errors(payload))
    return payload.get("result")


def deployment_origin(value: str) -> tuple[str, str]:
    parsed = urllib.parse.urlsplit(value.strip())
    if (
        parsed.scheme != "https"
        or not parsed.hostname
        or parsed.username is not None
        or parsed.password is not None
        or parsed.port is not None
        or parsed.path not in {"", "/"}
        or parsed.query
        or parsed.fragment
    ):
        raise ValueError("PORTAL_SITE_URL must be a bare HTTPS origin")
    hostname = parsed.hostname.lower()
    return f"https://{hostname}", hostname


def canonical_urls(origin: str) -> tuple[str, ...]:
    return tuple(origin.rstrip("/") + path for path in CANONICAL_PATHS)


def find_zone_id(token: str, zone_name: str) -> str:
    query = urllib.parse.urlencode({"name": zone_name, "status": "active", "per_page": 2})
    result = api_request(f"/zones?{query}", token=token, stage="zone_lookup")
    matches = [
        row
        for row in result if isinstance(row, dict) and str(row.get("name") or "").lower() == zone_name
    ] if isinstance(result, list) else []
    if len(matches) != 1 or not str(matches[0].get("id") or ""):
        raise CloudflareFailure("zone_lookup", 200, ((None, "expected one active zone"),))
    return str(matches[0]["id"])


def purge_urls(token: str, zone_name: str, urls: Iterable[str]) -> int:
    files = list(urls)
    if not files or any(not url.startswith(f"https://{zone_name}/") for url in files):
        raise ValueError("purge URL allowlist invariant failed")
    zone_id = find_zone_id(token, zone_name)
    api_request(
        f"/zones/{zone_id}/purge_cache",
        token=token,
        stage="url_cache_purge",
        method="POST",
        body={"files": files},
    )
    return len(files)


def format_failure(failure: CloudflareFailure) -> str:
    status = str(failure.http_status) if failure.http_status is not None else "transport_error"
    if failure.errors:
        details = "; ".join(
            f"{code if code is not None else 'unknown'}:{message}" for code, message in failure.errors
        )
    else:
        details = "none"
    return f"cloudflare_error stage={failure.stage} http_status={status} errors={details}"


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--mode", choices=("dry-run", "apply"), default="dry-run")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        origin, zone_name = deployment_origin(os.environ.get("PORTAL_SITE_URL", ""))
    except ValueError:
        print("configuration_error invalid=PORTAL_SITE_URL", file=sys.stderr)
        return 2
    urls = canonical_urls(origin)
    print(f"mode={args.mode} url_count={len(urls)}")
    for index, path in enumerate(CANONICAL_PATHS, start=1):
        print(f"path[{index}]={path}")
    if args.mode == "dry-run":
        print("No Cloudflare API request was sent.")
        return 0

    token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    if not token:
        print("configuration_error missing=CLOUDFLARE_API_TOKEN", file=sys.stderr)
        return 2
    try:
        count = purge_urls(token, zone_name, urls)
    except CloudflareFailure as failure:
        print(format_failure(failure), file=sys.stderr)
        return 1
    print(f"Cloudflare URL cache purge accepted for {count} canonical URLs.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
