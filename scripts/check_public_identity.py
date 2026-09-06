#!/usr/bin/env python3
"""Fail when a public working tree contains a private deployment identity."""

from __future__ import annotations

import base64
import re
import subprocess
import sys
import unicodedata
from pathlib import Path


def private_markers() -> tuple[str, ...]:
    product = "".join(("kc", "desk"))
    owner = "".join(("yt", "-", "feng"))
    repository = "".join(("rpt", "_", "edit"))
    account = "".join(("8182", "ec40", "eab8", "c484", "e11e", "bf5d", "6a51", "6fbd"))
    compact = product.encode("ascii")
    return (
        product,
        f"{product}.com",
        " ".join(("kc", "desk")),
        "_".join(("kc", "desk")),
        "-".join(("kc", "desk")),
        "/".join((owner, repository)),
        account,
        # The Chinese public-facing editorial term is intentionally allowed.
        # Keep the private deployment domain and historical English identity
        # blocked; the public term itself must remain indexable for SEO.
        "".join(("kc", "娱乐")),
        "".join(("x-", "kc")),
        base64.b64encode(compact + b".com").decode("ascii").rstrip("="),
        (compact + b".com").hex(),
    )


def confusable_skeleton(value: str) -> str:
    substitutions = {
        0x039A: "k",
        0x03BA: "k",
        0x041A: "k",
        0x043A: "k",
        0x0421: "c",
        0x0441: "c",
        0x03F9: "c",
        0x0501: "d",
        0x0435: "e",
        0x0415: "e",
        0x0455: "s",
        0x0405: "s",
        0x03BF: "o",
        0x039F: "o",
        0x043E: "o",
        0x041E: "o",
        0x2024: ".",
        0x3002: ".",
        0xFF0E: ".",
    }
    normalized = unicodedata.normalize("NFKC", value).casefold()
    return normalized.translate(substitutions).replace("\u200b", "").replace("\u200c", "").replace("\u200d", "")


def repository_paths() -> tuple[Path, ...]:
    result = subprocess.run(
        ["git", "ls-files", "-co", "--exclude-standard", "-z"],
        check=True,
        stdout=subprocess.PIPE,
    )
    paths = []
    for raw_path in result.stdout.split(b"\0"):
        if not raw_path:
            continue
        path = Path(raw_path.decode("utf-8", errors="surrogateescape"))
        if path.is_file() and path.suffix != ".enc":
            paths.append(path)
    return tuple(paths)


def redact_approved_public_contact(skeleton: str) -> str:
    # This exact account-opening address is deliberately public. Keep the
    # deployment domain, alternate addresses and all other identities blocked.
    return re.sub(
        r"(?<![a-z0-9.!#$%&'*+/=?^_`{|}~-])" + re.escape("info@kcdesk.com") + r"(?![a-z0-9.-])",
        "[approved-public-account-email]", skeleton,
    )


def main() -> int:
    markers = tuple(marker.casefold() for marker in private_markers())
    failed_paths: set[str] = set()
    for path in repository_paths():
        normalized_path = confusable_skeleton(path.as_posix())
        if any(marker in normalized_path for marker in markers):
            failed_paths.add(path.as_posix())
            continue
        try:
            data = path.read_bytes()
        except OSError:
            failed_paths.add(path.as_posix())
            continue
        try:
            skeleton = redact_approved_public_contact(confusable_skeleton(data.decode("utf-8")))
        except UnicodeDecodeError:
            lowered = data.lower()
            if any(
                marker.encode("utf-8") in lowered
                for marker in markers
                if len(marker.encode("utf-8")) >= 6
            ):
                failed_paths.add(path.as_posix())
            continue
        if any(marker in skeleton for marker in markers):
            failed_paths.add(path.as_posix())

    if failed_paths:
        for path in sorted(failed_paths):
            print(f"private identity marker found in public path: {path}", file=sys.stderr)
        return 1
    print(f"public identity check passed ({len(repository_paths())} files)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
