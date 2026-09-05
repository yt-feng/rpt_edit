#!/usr/bin/env python3
"""Check all planned root-head additions before any paid translation call."""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import build_portal_locales as builder
import verify_portal_chinese_parity as parity


def audit(root: Path, site_url: str) -> dict:
    checked = clusters = 0
    for path in sorted(root.rglob("*.html")):
        relative = path.relative_to(root).as_posix()
        if path.relative_to(root).parts[0] in builder.LOCALES or parity.is_site_verification_html(relative):
            continue
        before = path.read_bytes()
        source = before.decode("utf-8")
        canonical = builder.extract_canonical(source)
        # Test the maximum potential additions. History policy can only remove
        # links from this set; it never authorizes changing existing metadata.
        planned = builder.inject_root_discovery(source, canonical, site_url, "0123456789ab").encode("utf-8")
        baseline = parity._validate_snapshot_head(before, relative=relative)
        clusters += parity._validate_final_head(planned, relative=relative, baseline=baseline, origin=site_url)
        if parity._body(before, relative=relative) != parity._body(planned, relative=relative):
            raise parity.ParityError(f"Planned discovery changes protected body: {relative}")
        if parity._neutral_head(before, relative=relative) != parity._neutral_head(planned, relative=relative):
            raise parity.ParityError(f"Planned discovery changes protected head: {relative}")
        checked += 1
    if not checked:
        raise parity.ParityError("No root HTML pages were checked")
    return {"status": "passed", "html_checked": checked, "eligible_clusters": clusters, "provider_requests": 0}


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, required=True)
    parser.add_argument("--site-url", required=True)
    args = parser.parse_args()
    print(json.dumps(audit(args.root, args.site_url), sort_keys=True))


if __name__ == "__main__":
    main()
