#!/usr/bin/env python3
"""Read the active site's catalog and current search text for private indexing."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from urllib.parse import urlsplit
from urllib.request import Request, build_opener, HTTPRedirectHandler


class NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        raise ValueError("Research input URL must not redirect")


def clean_origin(value: str) -> str:
    parsed = urlsplit(value.strip())
    if (parsed.scheme != "https" or not parsed.hostname or parsed.username or parsed.password
            or parsed.port is not None or parsed.path not in {"", "/"} or parsed.query or parsed.fragment):
        raise ValueError("PORTAL_SITE_URL must be a clean HTTPS origin")
    return f"https://{parsed.hostname}"


def download_inputs(origin: str, output: Path, *, opener=None) -> dict[str, int]:
    origin = clean_origin(origin)
    opener = opener or build_opener(NoRedirect())
    payloads: dict[str, bytes] = {}
    counts = {}
    for filename, limit in (("catalog.json", 32 * 1024 * 1024), ("search_index.json", 160 * 1024 * 1024)):
        request = Request(f"{origin}/data/{filename}", headers={"User-Agent": "portal-research-refresh/1.0", "Cache-Control": "no-cache"})
        with opener.open(request, timeout=90) as response:
            data = response.read(limit + 1)
        if len(data) > limit:
            raise ValueError("Research input exceeds bounded read size")
        payload = json.loads(data)
        if not isinstance(payload, dict) or not isinstance(payload.get("items"), list) or not payload["items"]:
            raise ValueError("Research input must contain a nonempty items array")
        payloads[filename] = data
        counts[filename] = len(payload["items"])
    # Write only after both bounded inputs have passed validation.
    output.mkdir(parents=True, exist_ok=True)
    for filename, data in payloads.items():
        target = output / filename
        target.write_bytes(data)
        target.chmod(0o600)
    return counts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output-dir", type=Path, required=True)
    args = parser.parse_args()
    origin = clean_origin(os.environ.get("PORTAL_SITE_URL", ""))
    if os.environ.get("GITHUB_ACTIONS") == "true":
        print(f"::add-mask::{origin}")
        print(f"::add-mask::{urlsplit(origin).hostname}")
    print(json.dumps(download_inputs(origin, args.output_dir)))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
