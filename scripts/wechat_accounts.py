#!/usr/bin/env python3
"""Resolve WeChat account aliases and check draft API access."""
from __future__ import annotations

import argparse
import os

ACCOUNT_NAMES = {"kc": "KC桌面", "tt": "TT与老葛", "pankou": "盘口观市"}
ACCOUNT_SUFFIXES = {"kc": "", "tt": "_TT", "pankou": "_PANKOU"}
DEFAULT_ACCOUNT = "kc"


def account_credentials(account: str) -> tuple[str, str]:
    if account not in ACCOUNT_SUFFIXES:
        raise ValueError("Unknown WeChat account alias")
    suffix = ACCOUNT_SUFFIXES[account]
    credentials = (
        os.environ.get(f"WECHAT_MP_APPID{suffix}", "").strip(),
        os.environ.get(f"WECHAT_MP_APPSECRET{suffix}", "").strip(),
    )
    if not all(credentials):
        raise ValueError(f"Missing WeChat credentials for {ACCOUNT_NAMES[account]}")
    return credentials


def draft_account(draft: dict) -> str:
    account = draft.get("account", DEFAULT_ACCOUNT)
    if not isinstance(account, str) or account not in ACCOUNT_NAMES:
        raise ValueError("Invalid WeChat account alias in draft receipt")
    return account


def draft_tokens(session, drafts: list[dict], timeout: int, fetch_token) -> dict[str, str]:
    return {
        account: fetch_token(session, *account_credentials(account), timeout)
        for account in dict.fromkeys(draft_account(draft) for draft in drafts)
    }


def all_account_credentials(primary: tuple[str, str] | None = None) -> dict[str, tuple[str, str]]:
    credentials = {
        account: primary if account == DEFAULT_ACCOUNT and primary is not None else account_credentials(account)
        for account in ACCOUNT_NAMES
    }
    if len({appid for appid, _ in credentials.values()}) != len(credentials):
        raise ValueError("WeChat account aliases must have distinct AppIDs")
    return credentials


def check_access() -> int:
    import requests

    from push_portal_translated_to_wechat_drafts import (
        WeChatError,
        get_stable_access_token,
        parse_wechat_json,
        post_wechat_json,
    )

    failed = False
    with requests.Session() as session:
        for account, (appid, secret) in all_account_credentials().items():
            name = ACCOUNT_NAMES[account]
            operation = "stable_token"
            try:
                token = get_stable_access_token(session, appid, secret, 20)
                operation = "draft/batchget"
                response = post_wechat_json(
                    session, f"https://api.weixin.qq.com/cgi-bin/draft/batchget?access_token={token}",
                    {"offset": 0, "count": 1, "no_content": 1}, 20,
                )
                data = parse_wechat_json(response, operation)
                if type(data.get("total_count")) is not int:
                    raise WeChatError("Missing draft count")
            except WeChatError as error:
                print(f"{name}: {operation} failed (errcode={error.errcode})", flush=True)
                failed = True
            else:
                print(f"{name}: stable_token and draft/batchget verified", flush=True)
    return int(failed)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check-access", action="store_true", required=True)
    parser.parse_args()
    raise SystemExit(check_access())
