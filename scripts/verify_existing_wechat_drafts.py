#!/usr/bin/env python3
"""Read back existing draft IDs from an archived upload; never create or publish."""

from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from typing import Any

import requests

from push_portal_translated_to_wechat_drafts import (
    get_stable_access_token,
    materialize_private_article_payload,
    verify_draft_get,
)


def load_drafts(artifact_root: Path) -> list[dict[str, Any]]:
    root = artifact_root.resolve()
    summaries = sorted(root.rglob("wechat_draft_summary.json"))
    if not summaries:
        raise ValueError("Artifact has no WeChat draft summary")
    drafts: list[dict[str, Any]] = []
    seen: set[str] = set()
    for path in summaries:
        if not path.resolve().is_relative_to(root):
            raise ValueError("Summary escapes artifact directory")
        summary = json.loads(path.read_text(encoding="utf-8"))
        if summary.get("dry_run"):
            raise ValueError("Cannot verify a dry-run summary")
        for draft in summary.get("drafts", []):
            media_id = str(draft.get("media_id") or "").strip()
            if not media_id or media_id in seen:
                raise ValueError("Summary contains a missing or duplicate draft ID")
            # Upload artifacts preserve payload files beside their summary even
            # when GitHub strips the common parent directory from the archive.
            payload_name = Path(str(draft.get("payload") or "")).name
            if not payload_name.startswith("draft_payload_") or not payload_name.endswith(".json"):
                raise ValueError("Draft payload filename is invalid")
            payload_path = path.parent / payload_name
            if not payload_path.resolve().is_relative_to(root):
                raise ValueError("Payload escapes artifact directory")
            payload = json.loads(payload_path.read_text(encoding="utf-8"))
            articles = payload.get("articles")
            if not isinstance(articles, list) or not articles or not all(isinstance(a, dict) for a in articles):
                raise ValueError("Draft payload must contain articles")
            if len(articles) != draft.get("article_count"):
                raise ValueError("Payload article count differs from summary")
            seen.add(media_id)
            drafts.append({"media_id": media_id, "articles": articles})
    if not drafts:
        raise ValueError("Artifact contains no existing drafts")
    return drafts


def verify_existing(drafts: list[dict[str, Any]], session: requests.Session, token: str, timeout: int) -> dict[str, Any]:
    results = []
    for index, draft in enumerate(drafts, 1):
        articles = materialize_private_article_payload(draft["articles"], os.environ.get("PORTAL_SITE_URL", ""))
        result = verify_draft_get(session, token, draft["media_id"], timeout, len(articles), articles)
        results.append({"draft_index": index, **result})
    return {
        "ok": bool(results) and all(item.get("ok") is True for item in results),
        "read_only": True,
        "draft_count": len(results),
        "expected_article_count": sum(len(draft["articles"]) for draft in drafts),
        "verified_article_count": sum(item.get("article_count", 0) for item in results if item.get("ok") is True),
        "drafts": results,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args()
    drafts = load_drafts(args.artifact_root)
    appid = os.environ.get("WECHAT_MP_APPID", "").strip()
    secret = os.environ.get("WECHAT_MP_APPSECRET", "").strip()
    if not appid or not secret:
        raise ValueError("WeChat application credentials are required")
    with requests.Session() as session:
        token = get_stable_access_token(session, appid, secret, args.timeout)
        report = verify_existing(drafts, session, token, args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "drafts"}, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
