#!/usr/bin/env python3
"""Capture the single active Worker version used as an exact rollback target."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path
from typing import Any


API_ROOT = "https://api.cloudflare.com/client/v4"
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$", re.I)


class CaptureError(Exception):
    pass


def request_deployments(account_id: str, script_name: str, token: str) -> list[dict[str, Any]]:
    path = (
        f"/accounts/{urllib.parse.quote(account_id, safe='')}"
        f"/workers/scripts/{urllib.parse.quote(script_name, safe='')}/deployments"
    )
    request = urllib.request.Request(
        API_ROOT + path,
        headers={"Authorization": f"Bearer {token}", "Accept": "application/json"},
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            payload = json.load(response)
    except (OSError, ValueError, urllib.error.HTTPError):
        raise CaptureError("deployment_lookup") from None
    result = payload.get("result") if isinstance(payload, dict) and payload.get("success") is True else None
    deployments = result.get("deployments") if isinstance(result, dict) else None
    if (
        not isinstance(deployments, list)
        or not deployments
        or any(not isinstance(row, dict) for row in deployments)
    ):
        raise CaptureError("deployment_shape")
    return deployments


def active_rollback_target(deployments: list[dict[str, Any]]) -> tuple[str, str]:
    # Cloudflare documents the first list entry as the latest deployment that
    # is actively serving traffic.  Do not infer active state from timestamps.
    current = deployments[0]
    deployment_id = str(current.get("id") or "").lower()
    versions = current.get("versions")
    if not UUID.fullmatch(deployment_id) or not isinstance(versions, list) or len(versions) != 1:
        raise CaptureError("deployment_not_single_version")
    version = versions[0]
    if not isinstance(version, dict):
        raise CaptureError("deployment_not_single_version")
    version_id = str(version.get("version_id") or "").lower()
    try:
        percentage = float(version.get("percentage"))
    except (TypeError, ValueError):
        raise CaptureError("deployment_not_single_version") from None
    if not UUID.fullmatch(version_id) or percentage != 100.0:
        raise CaptureError("deployment_not_single_version")
    return deployment_id, version_id


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--script-name", required=True)
    parser.add_argument("--output-env", type=Path)
    parser.add_argument("--expect-version")
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    account_id = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "").strip()
    token = os.environ.get("CLOUDFLARE_API_TOKEN", "").strip()
    script_name = args.script_name.strip()
    expected_version = str(args.expect_version or "").strip().lower()
    if (
        not account_id
        or not token
        or not script_name
        or (args.output_env is None and not expected_version)
        or (expected_version and not UUID.fullmatch(expected_version))
    ):
        print("edge rollback target configuration is incomplete", file=sys.stderr)
        return 2
    try:
        deployments = request_deployments(account_id, script_name, token)
        deployment_id, version_id = active_rollback_target(deployments)
        if expected_version and version_id != expected_version:
            raise CaptureError("deployment_version_mismatch")
        if args.output_env is not None:
            with args.output_env.open("a", encoding="utf-8") as handle:
                handle.write(f"EDGE_PREVIOUS_DEPLOYMENT_ID={deployment_id}\n")
                handle.write(f"EDGE_PREVIOUS_VERSION_ID={version_id}\n")
    except (CaptureError, OSError) as error:
        print(f"edge rollback target capture failed: {error}", file=sys.stderr)
        return 1
    print("edge rollback target verified" if expected_version else "edge rollback target captured")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
