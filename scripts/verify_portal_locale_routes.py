#!/usr/bin/env python3
"""Verify only declared locale application shells against a trusted artifact."""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import subprocess
import time
from typing import Any, Callable
from urllib.parse import urlsplit


LOCALES = {"ko": "ltr", "ja": "ltr", "ar": "rtl"}
APPLICATION_PAGES = {
    "report.html": "report",
    "doc.html": "external",
    "delivery.html": "delivery",
    "newsfeed.html": "newsfeed",
    "courses.html": "course",
}
RECOVERY_PATH = "assets/locale-recovery.js"
MAX_RESPONSE_BYTES = 16 * 1024 * 1024
MAX_MANIFEST_BYTES = 2 * 1024 * 1024
TIMEOUT_SECONDS = 20
MAX_WORKERS = 4
VOID_TAGS = frozenset("area base br col embed hr img input link meta param source track wbr".split())


class RouteVerificationError(RuntimeError):
    """A declared public application route is unavailable or mismatched."""


def validate_origin(value: str) -> str:
    try:
        parsed = urlsplit(value)
        port = parsed.port
    except (TypeError, ValueError) as error:
        raise RouteVerificationError("Origin must be a bare HTTPS origin") from error
    if (
        parsed.scheme != "https" or not parsed.hostname
        or parsed.username is not None or parsed.password is not None
        or port is not None or parsed.path not in {"", "/"}
        or parsed.query or parsed.fragment or "\\" in value
        or any(character.isspace() or ord(character) < 32 for character in value)
    ):
        raise RouteVerificationError("Origin must be a bare HTTPS origin")
    return f"https://{parsed.netloc.lower()}"


def descriptor(row: Any, expected_path: str) -> dict[str, Any]:
    if (
        not isinstance(row, dict) or row.get("path") != expected_path
        or type(row.get("byte_size")) is not int
        or not 0 < row["byte_size"] <= MAX_RESPONSE_BYTES
        or not isinstance(row.get("sha256"), str)
        or re.fullmatch(r"[0-9a-f]{64}", row["sha256"]) is None
    ):
        raise RouteVerificationError(f"Invalid declared route descriptor: {expected_path}")
    return {key: row[key] for key in ("path", "byte_size", "sha256")}


def declared_checks(manifest: dict[str, Any]) -> list[dict[str, Any]] | None:
    if not isinstance(manifest, dict) or manifest.get("schema_version") != 1:
        raise RouteVerificationError("Locale manifest schema is invalid")
    if "application_routes" not in manifest:
        return None
    groups = manifest["application_routes"]
    if not isinstance(groups, dict) or set(groups) != set(LOCALES):
        raise RouteVerificationError("Application routes must contain all three locales")
    checks = []
    for locale in LOCALES:
        rows = groups[locale]
        if not isinstance(rows, dict) or set(rows) != set(APPLICATION_PAGES):
            raise RouteVerificationError(f"Application routes must contain all five exact shells: {locale}")
        for filename in APPLICATION_PAGES:
            checks.append({**descriptor(rows[filename], f"{locale}/{filename}"),
                           "locale": locale, "filename": filename})
    checks.append(descriptor(manifest.get("recovery_asset"), RECOVERY_PATH))
    return checks


def fetch_public(url: str, timeout: int) -> tuple[int, dict[str, str], bytes]:
    """A normal HTTPS GET, no redirects/retries, with a wall-clock deadline."""
    try:
        result = subprocess.run(
            ["curl", "--silent", "--show-error", "--include", "--suppress-connect-headers",
             "--connect-timeout", "5", "--max-time", str(timeout), "--max-redirs", "0",
             "--max-filesize", str(MAX_RESPONSE_BYTES), "--header", "Cache-Control: no-cache",
             "--write-out", "\nKC_ROUTE_STATUS:%{http_code}", "--", url],
            capture_output=True, timeout=timeout, check=False,
        )
    except (OSError, subprocess.TimeoutExpired) as error:
        raise RouteVerificationError(f"Public GET did not complete within its deadline: {type(error).__name__}") from error
    if result.returncode:
        raise RouteVerificationError(f"Public GET failed: curl exit {result.returncode}")
    try:
        raw, status = result.stdout.rsplit(b"\nKC_ROUTE_STATUS:", 1)
        code = int(status)
        headers: dict[str, str] = {}
        while raw.startswith(b"HTTP/"):
            block, raw = raw.split(b"\r\n\r\n", 1)
            headers = {}
            for line in block.decode("iso-8859-1").split("\r\n")[1:]:
                if ":" in line:
                    name, value = line.split(":", 1)
                    headers[name.strip().lower()] = value.strip()
    except (ValueError, UnicodeError) as error:
        raise RouteVerificationError("Public GET returned an invalid response envelope") from error
    if len(raw) > MAX_RESPONSE_BYTES:
        raise RouteVerificationError("Public GET exceeded the response size bound")
    return code, headers, raw


class ShellParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.stack: list[str] = []
        self.html: list[dict[str, str]] = []
        self.bodies: list[dict[str, str]] = []
        self.robots: list[set[str]] = []
        self.help_count = 0
        self.contact_count = 0
        self.public_contact_count = 0
        self.help_depth: int | None = None
        self.contact_depth: int | None = None
        self.anchor_depth: int | None = None
        self.anchors: list[dict[str, Any]] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): value or "" for key, value in attrs}
        if tag not in VOID_TAGS:
            self.stack.append(tag)
        depth = len(self.stack)
        if tag == "html":
            self.html.append(values)
        if tag == "body":
            self.bodies.append(values)
        if tag == "meta" and "head" in self.stack and values.get("name", "").lower() in {"robots", "googlebot", "bingbot"}:
            self.robots.append(set(re.split(r"[\s,]+", values.get("content", "").lower())))
        if "data-kc-locale-help" in values:
            self.help_count += 1
            self.help_depth = depth
        if "data-kc-public-account-contact" in values:
            self.public_contact_count += 1
        if self.help_depth is not None:
            if "data-kc-public-account-contact" in values:
                self.contact_count += 1
                self.contact_depth = depth
            if tag == "a":
                self.anchors.append({"attrs": values, "text": "", "contact": self.contact_depth is not None})
                self.anchor_depth = depth

    def handle_endtag(self, tag: str) -> None:
        if tag not in self.stack:
            return
        position = len(self.stack) - 1 - self.stack[::-1].index(tag)
        for name in ("anchor_depth", "contact_depth", "help_depth"):
            depth = getattr(self, name)
            if depth is not None and depth > position:
                setattr(self, name, None)
        del self.stack[position:]

    def handle_data(self, data: str) -> None:
        if self.anchor_depth is not None:
            self.anchors[-1]["text"] += data


def validate_shell(body: bytes, headers: dict[str, str], locale: str, filename: str, origin: str) -> None:
    try:
        text = body.decode("utf-8")
        parser = ShellParser()
        parser.feed(text)
        parser.close()
    except (UnicodeError, ValueError) as error:
        raise RouteVerificationError("Application shell is not valid UTF-8 HTML") from error
    if len(parser.html) != 1 or parser.html[0].get("lang") != locale or parser.html[0].get("dir") != LOCALES[locale]:
        raise RouteVerificationError("Application shell has the wrong HTML language or direction")
    if len(parser.bodies) != 1 or parser.bodies[0].get("data-page") != APPLICATION_PAGES[filename]:
        raise RouteVerificationError("Application shell has the wrong page identity (possibly a 200 Not Found page)")
    normalized_headers = {key.lower(): str(value).strip().lower() for key, value in headers.items()}
    if normalized_headers.get("content-language") != locale:
        raise RouteVerificationError("Application shell has the wrong Content-Language")
    if not any(tokens & {"noindex", "none"} for tokens in parser.robots) or any("index" in tokens for tokens in parser.robots):
        raise RouteVerificationError("Application shell must remain noindex")
    if parser.help_count != 1:
        raise RouteVerificationError("Application shell must contain one static locale help strip")

    def chinese_entry(anchor: dict[str, Any], path: str, equivalent: bool) -> bool:
        attrs = anchor["attrs"]
        return (
            attrs.get("href") == origin + path
            and attrs.get("hreflang", "").lower() == "zh-hans"
            and "data-kc-chinese-entry" in attrs
            and (not equivalent or "data-kc-chinese-equivalent" in attrs)
            and bool(anchor["text"].strip())
        )

    if not any(chinese_entry(anchor, "/" + filename, True) for anchor in parser.anchors):
        raise RouteVerificationError("Static Chinese equivalent must target the real non-locale root route")
    if not any(chinese_entry(anchor, "/", False) for anchor in parser.anchors):
        raise RouteVerificationError("Static Chinese homepage entry is missing")
    if parser.contact_count != 1 or parser.public_contact_count != 1 or not any(
        anchor["contact"] and anchor["attrs"].get("href") == "mailto:info@kcdesk.com"
        and anchor["text"].strip() == "info@kcdesk.com" for anchor in parser.anchors
    ):
        raise RouteVerificationError("Static public account email must appear once in the help strip")


def verify_locale_routes(
    manifest: dict[str, Any], origin: str,
    *, fetcher: Callable[[str, int], tuple[int, dict[str, str], bytes]] = fetch_public,
) -> dict[str, Any]:
    origin = validate_origin(origin)
    checks = declared_checks(manifest)
    if checks is None:
        return {"schema_version": 1, "status": "skipped", "origin": origin,
                "reason": "legacy-manifest-without-application-routes", "request_count": 0,
                "route_count": 0, "asset_count": 0, "checks": []}
    started = time.monotonic()

    def verify(row: dict[str, Any]) -> dict[str, Any]:
        output = {"path": "/" + row["path"], "status": "failed"}
        try:
            status, headers, body = fetcher(origin + output["path"], TIMEOUT_SECONDS)
            output["http_status"] = status
            if status != 200:
                raise RouteVerificationError(f"Expected HTTP 200 without redirects, got {status}")
            if not isinstance(body, bytes) or len(body) != row["byte_size"] or hashlib.sha256(body).hexdigest() != row["sha256"]:
                raise RouteVerificationError("Public response size/SHA-256 differs from the trusted manifest")
            if "locale" in row:
                validate_shell(body, headers, row["locale"], row["filename"], origin)
                output["locale"] = row["locale"]
            output.update(status="passed", byte_size=len(body), sha256=row["sha256"])
        except Exception as error:
            output["error"] = str(error) if isinstance(error, RouteVerificationError) else type(error).__name__
        return output

    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        results = list(pool.map(verify, checks))
    return {"schema_version": 1, "status": "passed" if all(row["status"] == "passed" for row in results) else "failed",
            "origin": origin, "request_count": len(results), "route_count": 15, "asset_count": 1,
            "elapsed_seconds": round(time.monotonic() - started, 3), "checks": results}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--manifest", type=Path, required=True)
    parser.add_argument("--origin", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        if args.manifest.is_symlink() or not args.manifest.is_file() or not 0 < args.manifest.stat().st_size <= MAX_MANIFEST_BYTES:
            raise RouteVerificationError("Trusted locale manifest is missing or exceeds its size bound")
        manifest = json.loads(args.manifest.read_text(encoding="utf-8"))
        report = verify_locale_routes(manifest, args.origin)
    except (OSError, ValueError, RouteVerificationError) as error:
        report = {"schema_version": 1, "status": "failed", "error": str(error)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "checks"}, ensure_ascii=False))
    return 1 if report["status"] == "failed" else 0


if __name__ == "__main__":
    raise SystemExit(main())
