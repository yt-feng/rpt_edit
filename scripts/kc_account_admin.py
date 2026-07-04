#!/usr/bin/env python3
"""Small KC Desk account maintenance helpers for GitHub Actions."""

from __future__ import annotations

import argparse
import hashlib
import hmac
import json
import os
import secrets
import sys
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone


def env(name: str, default: str = "") -> str:
    return os.environ.get(name, default).strip()


def normalize_username(value: str) -> str:
    return value.strip().lower().lstrip("@")


def normalize_email(value: str) -> str:
    return value.strip().lower()


def require_env(name: str) -> str:
    value = env(name)
    if not value or value == "unconfigured":
        raise SystemExit(f"{name} is required")
    return value


def account_secret() -> str:
    return env("AUTH_SECRET") or env("PASSWORD_SECRET") or env("MASTER_KEY")


def site_password_fields(password: str) -> dict[str, str]:
    secret = account_secret()
    if not secret or secret == "unconfigured":
        raise SystemExit("AUTH_SECRET or PASSWORD_SECRET is required")
    salt = secrets.token_hex(16)
    digest = hmac.new(
        secret.encode("utf-8"),
        f"user-password:{salt}:{password}".encode("utf-8"),
        hashlib.sha256,
    ).hexdigest()
    return {"password_salt": salt, "password_hash": f"hmac_sha256${digest}"}


def supabase_request(method: str, path: str, body: dict | None = None) -> tuple[int, object]:
    base_url = require_env("SUPABASE_URL").rstrip("/")
    service_key = require_env("SUPABASE_SERVICE_ROLE_KEY")
    data = None if body is None else json.dumps(body).encode("utf-8")
    request = urllib.request.Request(
        f"{base_url}{path}",
        data=data,
        method=method,
        headers={
            "apikey": service_key,
            "Authorization": f"Bearer {service_key}",
            "Content-Type": "application/json",
            "Accept": "application/json",
            "Prefer": "return=representation",
        },
    )
    try:
        with urllib.request.urlopen(request, timeout=30) as response:
            text = response.read().decode("utf-8")
            return response.status, json.loads(text) if text else None
    except urllib.error.HTTPError as error:
        text = error.read().decode("utf-8", errors="replace")
        raise SystemExit(f"Supabase {method} {path} failed: {error.code} {text}") from error


def query_string(**params: str) -> str:
    return urllib.parse.urlencode(params, doseq=False, safe="().,*")


def find_site_user(username: str, email: str) -> dict:
    if email:
        _, rows = supabase_request("GET", f"/rest/v1/site_users?{query_string(email=f'eq.{email}', limit='1')}")
        if isinstance(rows, list) and rows:
            return rows[0]
    if username:
        _, rows = supabase_request("GET", f"/rest/v1/site_users?{query_string(username=f'eq.{username}', limit='1')}")
        if isinstance(rows, list) and rows:
            return rows[0]
    raise SystemExit("No matching site_users row found")


def reset_password(args: argparse.Namespace) -> None:
    username = normalize_username(args.username or "")
    email = normalize_email(args.email or "")
    password = args.password or ""
    if not username and not email:
        raise SystemExit("--username or --email is required")
    if len(password) < 4 or len(password) > 128:
        raise SystemExit("--password must be 4-128 characters")
    user = find_site_user(username, email)
    user_id = user.get("id")
    if not user_id:
        raise SystemExit("Matched site_users row is missing id")
    fields = {
        **site_password_fields(password),
        "updated_at": datetime.now(timezone.utc).isoformat().replace("+00:00", "Z"),
    }
    patch_path = f"/rest/v1/site_users?{query_string(id=f'eq.{user_id}', select='id,username,email,updated_at')}"
    _, rows = supabase_request("PATCH", patch_path, fields)
    updated = rows[0] if isinstance(rows, list) and rows else {"id": user_id}
    print(json.dumps({
        "ok": True,
        "id": updated.get("id", user_id),
        "username": updated.get("username", user.get("username", "")),
        "email": updated.get("email", user.get("email", "")),
        "updated_at": updated.get("updated_at", fields["updated_at"]),
    }, ensure_ascii=False))


def main() -> None:
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)
    reset = subparsers.add_parser("reset-password")
    reset.add_argument("--username", default="")
    reset.add_argument("--email", default="")
    reset.add_argument("--password", required=True)
    reset.set_defaults(func=reset_password)
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
