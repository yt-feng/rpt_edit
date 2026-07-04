#!/usr/bin/env python3
"""Delete WeChat Official Account drafts listed in a saved draft summary."""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import requests

from push_kc_translated_to_wechat_drafts import (
    WeChatError,
    get_stable_access_token,
    normalize_space,
    parse_wechat_json,
    post_wechat_json,
)


def log(message: str) -> None:
    print(message, flush=True)


def read_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def write_json(path: Path, payload: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")


def collect_media_ids(summary: dict[str, Any], extra_media_ids: list[str]) -> list[str]:
    media_ids: list[str] = []
    for item in summary.get("drafts") or []:
        if not isinstance(item, dict):
            continue
        media_id = normalize_space(str(item.get("media_id") or ""))
        if media_id:
            media_ids.append(media_id)
    media_ids.extend(normalize_space(value) for value in extra_media_ids if normalize_space(value))

    unique: list[str] = []
    seen: set[str] = set()
    for media_id in media_ids:
        if media_id not in seen:
            unique.append(media_id)
            seen.add(media_id)
    return unique


def delete_draft(session: requests.Session, access_token: str, media_id: str, timeout: int) -> dict[str, Any]:
    response = post_wechat_json(
        session,
        f"https://api.weixin.qq.com/cgi-bin/draft/delete?access_token={access_token}",
        {"media_id": media_id},
        timeout,
    )
    return parse_wechat_json(response, "draft/delete")


def main() -> int:
    parser = argparse.ArgumentParser(description="Delete WeChat drafts by media_id from a summary file.")
    parser.add_argument("--summary", type=Path, required=True)
    parser.add_argument("--media-id", action="append", default=[])
    parser.add_argument("--output", type=Path, default=Path("deleted_wechat_drafts_summary.json"))
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--wechat-appid", default=os.getenv("WECHAT_MP_APPID", ""))
    parser.add_argument("--wechat-secret", default=os.getenv("WECHAT_MP_APPSECRET", ""))
    parser.add_argument("--ignore-delete-errors", action="store_true")
    parser.add_argument("--dry-run", action="store_true")
    args = parser.parse_args()

    if not args.summary.exists():
        raise RuntimeError(f"Draft summary not found: {args.summary}")
    if not args.dry_run and (not args.wechat_appid or not args.wechat_secret):
        raise RuntimeError("WECHAT_MP_APPID and WECHAT_MP_APPSECRET are required unless --dry-run is set")

    summary = read_json(args.summary)
    if not isinstance(summary, dict):
        raise RuntimeError(f"Draft summary must be a JSON object: {args.summary}")

    media_ids = collect_media_ids(summary, args.media_id)
    if not media_ids:
        raise RuntimeError(f"No draft media_id values found in {args.summary}")

    log(f"Deleting {len(media_ids)} WeChat draft(s) from {args.summary}")
    results: list[dict[str, Any]] = []

    session: requests.Session | None = None
    access_token = ""
    if not args.dry_run:
        session = requests.Session()
        access_token = get_stable_access_token(session, args.wechat_appid, args.wechat_secret, args.timeout)

    for media_id in media_ids:
        record: dict[str, Any] = {"media_id": media_id}
        if args.dry_run:
            record["deleted"] = False
            record["dry_run"] = True
            log(f"Dry run: would delete draft media_id={media_id}")
            results.append(record)
            continue
        try:
            if session is None:
                raise RuntimeError("session is required outside dry-run")
            delete_draft(session, access_token, media_id, args.timeout)
            record["deleted"] = True
            log(f"Deleted WeChat draft media_id={media_id}")
        except WeChatError as exc:
            record["deleted"] = False
            record["errcode"] = exc.errcode
            record["errmsg"] = exc.errmsg
            record["error"] = str(exc)
            log(f"Failed to delete WeChat draft media_id={media_id}: {exc}")
            if not args.ignore_delete_errors:
                results.append(record)
                write_json(args.output, {"summary": str(args.summary), "results": results})
                raise
        results.append(record)

    payload = {
        "summary": str(args.summary),
        "dry_run": args.dry_run,
        "requested_count": len(media_ids),
        "deleted_count": sum(1 for item in results if item.get("deleted")),
        "results": results,
    }
    write_json(args.output, payload)
    log(f"Wrote delete summary: {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
