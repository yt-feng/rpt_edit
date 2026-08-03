#!/usr/bin/env python3
"""Generate Portal Suite password hashes."""

from __future__ import annotations

import argparse
import getpass
import hashlib


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--secret", default="", help="Cloudflare Worker PASSWORD_SECRET.")
    parser.add_argument("--password", default="", help="Plain password to hash.")
    args = parser.parse_args()

    secret = args.secret or getpass.getpass("PASSWORD_SECRET: ")
    password = args.password or getpass.getpass("Plain password: ")
    digest = hashlib.sha256(f"{secret}:{password}".encode("utf-8")).hexdigest()
    print(digest)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
