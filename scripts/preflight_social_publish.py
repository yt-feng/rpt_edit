#!/usr/bin/env python3
"""Verify the selected provider identity, then export only its publish secrets.

This command is intended for separate conditional GitHub Actions steps.  A
platform's credentials are appended to ``GITHUB_ENV`` only after a fresh,
read-only identity/scope probe returns healthy.  Output contains only the
platform and normalized status/reason.
"""

from __future__ import annotations

import argparse
import os
from pathlib import Path
import re
import sys
from typing import Any, Callable, Mapping

import check_social_credentials as credentials


PLATFORM_EXPORTS = {
    "youtube": (
        "YOUTUBE_CLIENT_ID",
        "YOUTUBE_CLIENT_SECRET",
        "YOUTUBE_REFRESH_TOKEN",
    ),
    "linkedin": (
        "LINKEDIN_ACCESS_TOKEN",
        "LINKEDIN_AUTHOR_URN",
    ),
    "x": (
        "X_API_KEY",
        "X_API_SECRET",
        "X_ACCESS_TOKEN",
        "X_ACCESS_TOKEN_SECRET",
    ),
}


class PreflightError(RuntimeError):
    pass


def _required(value: str | None, name: str) -> str:
    normalized = (value or "").strip()
    if not normalized or "\n" in normalized or "\r" in normalized:
        raise PreflightError(f"{name} is missing or invalid")
    return normalized


def preflight(
    platform: str,
    env: Mapping[str, str],
    *,
    youtube_probe: Callable[..., Any] = credentials.probe_direct_youtube,
    linkedin_probe: Callable[..., Any] = credentials.probe_direct_linkedin,
    x_probe: Callable[..., Any] = credentials.probe_direct_x,
) -> dict[str, str]:
    if platform not in PLATFORM_EXPORTS:
        raise PreflightError("unsupported platform")
    if platform == "youtube":
        _required(env.get("YOUTUBE_CHANNEL_ID"), "YOUTUBE_CHANNEL_ID")
        result = youtube_probe(env)
    elif platform == "linkedin":
        author = _required(env.get("LINKEDIN_AUTHOR_URN"), "LINKEDIN_AUTHOR_URN")
        if not re.fullmatch(r"urn:li:(person|organization):[A-Za-z0-9_-]+", author):
            raise PreflightError("LINKEDIN_AUTHOR_URN is invalid")
        result = linkedin_probe(env)
    else:
        _required(env.get("X_USER_ID"), "X_USER_ID")
        _required(env.get("X_OAUTH1_SCOPES"), "X_OAUTH1_SCOPES")
        result = x_probe(env)
    status = str(getattr(result, "status", "transient"))
    reason = str(getattr(result, "reason", "provider_response_invalid"))
    if status != "healthy":
        raise PreflightError(f"{platform} preflight failed: {status}/{reason}")
    return {
        name: _required(env.get(name), name)
        for name in PLATFORM_EXPORTS[platform]
    }


def append_github_env(path: Path, values: Mapping[str, str]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("a", encoding="utf-8") as stream:
        for name, value in values.items():
            if not re.fullmatch(r"[A-Z][A-Z0-9_]+", name):
                raise PreflightError("invalid export name")
            if "\n" in value or "\r" in value:
                raise PreflightError("credential value must be one line")
            stream.write(f"{name}={value}\n")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser()
    parser.add_argument("--platform", choices=tuple(PLATFORM_EXPORTS), required=True)
    parser.add_argument(
        "--github-env",
        type=Path,
        default=Path(os.environ["GITHUB_ENV"]) if os.environ.get("GITHUB_ENV") else None,
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    if args.github_env is None:
        print("GITHUB_ENV is required", file=sys.stderr)
        return 2
    try:
        values = preflight(args.platform, os.environ)
        append_github_env(args.github_env, values)
    except PreflightError as exc:
        print(str(exc), file=sys.stderr)
        return 2
    print(f"{args.platform} preflight: healthy")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
