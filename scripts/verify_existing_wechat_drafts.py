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
    WeChatError,
    get_draft,
    get_stable_access_token,
    materialize_private_article_payload,
    normalize_space,
    verify_draft_get,
)


def load_drafts(artifact_root: Path) -> list[dict[str, Any]]:
    root = artifact_root.resolve()
    summaries = sorted(root.rglob("wechat_draft_summary.json"))
    if not summaries:
        return load_restored_drafts(root)
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


def load_restored_drafts(root: Path) -> list[dict[str, Any]]:
    """Load identity-only receipts without inventing a reusable article payload."""
    paths = sorted(root.rglob("restore_receipt.json"))
    if len(paths) != 1 or not paths[0].resolve().is_relative_to(root):
        raise ValueError("Artifact must contain exactly one contained restoration receipt")
    receipt = json.loads(paths[0].read_text(encoding="utf-8"))
    if (not isinstance(receipt, dict) or type(receipt.get("schema_version")) is not int
            or receipt["schema_version"] != 1 or receipt.get("publish") is not False
            or receipt.get("dry_run") is not False):
        raise ValueError("Restoration receipt must be version 1 and real draft-only")
    rows = receipt.get("drafts")
    if (not isinstance(rows, list) or not rows or type(receipt.get("draft_count")) is not int
            or receipt["draft_count"] != len(rows)):
        raise ValueError("Restoration draft count is inconsistent")
    drafts, seen, total = [], set(), 0
    for row in rows:
        if not isinstance(row, dict):
            raise ValueError("Invalid restoration draft record")
        media_id, titles, count = row.get("media_id"), row.get("titles"), row.get("article_count")
        if (not isinstance(media_id, str) or not media_id.strip() or media_id.strip() in seen
                or not isinstance(titles, list) or not titles
                or not all(isinstance(title, str) and title.strip() for title in titles)
                or type(count) is not int or count != len(titles)):
            raise ValueError("Restoration draft identity or article count is invalid")
        media_id = media_id.strip()
        seen.add(media_id)
        total += count
        # Deliberately no `articles`: consumers requiring complete upload
        # payloads must not use a title-only receipt to construct new content.
        drafts.append({"verification_scope": "restored_receipt_identity", "media_id": media_id,
                       "expected_titles": titles, "expected_article_count": count})
    if type(receipt.get("expected_article_count")) is not int or receipt["expected_article_count"] != total:
        raise ValueError("Restoration article total is inconsistent")
    for key, expected in (
        ("verified_draft_count", sum(row.get("status") == "verified" for row in rows)),
        ("verified_article_count", sum(row["article_count"] for row in rows if row.get("status") == "verified")),
    ):
        if key in receipt and (type(receipt[key]) is not int or receipt[key] != expected):
            raise ValueError("Restoration verified counts are inconsistent")
    return drafts


def verify_restored_identity(draft: dict[str, Any], session: requests.Session, token: str, timeout: int) -> dict[str, Any]:
    """Read a saved new ID, retaining edits and distinguishing absence from uncertainty."""
    import contextlib
    import io
    from datetime import datetime, timezone
    result = {"verification_scope": "restored_receipt_identity", "ok": False,
              "media_id": draft["media_id"], "id_exists": None, "identity_status": "unknown",
              "expected_article_count": draft["expected_article_count"],
              "expected_titles": draft["expected_titles"], "article_count": None, "titles": [],
              "matches_expected_article_count": False, "matches_expected_titles": False,
              "create_time": None, "update_time": None, "errcode": None}
    try:
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            data = get_draft(session, token, draft["media_id"], timeout)
        rows = data.get("news_item", data.get("articles")) if isinstance(data, dict) else None
        if (not isinstance(rows, list) or not rows or not all(isinstance(row, dict)
                and isinstance(row.get("title"), str) and row["title"].strip() for row in rows)):
            raise ValueError("Malformed draft identity response")
        titles = [normalize_space(row["title"]) for row in rows]
        count_matches = len(rows) == draft["expected_article_count"]
        titles_match = titles == [normalize_space(title) for title in draft["expected_titles"]]
        result.update(id_exists=True, article_count=len(rows), titles=titles,
                      matches_expected_article_count=count_matches, matches_expected_titles=titles_match,
                      ok=count_matches and titles_match,
                      identity_status="matched" if count_matches and titles_match else
                                      "article_count_changed" if not count_matches else "titles_changed")
        for key in ("create_time", "update_time"):
            if type(data.get(key)) is int:
                result[key] = data[key]
    except WeChatError as exc:
        result["errcode"] = exc.errcode if type(exc.errcode) is int else None
        if exc.errcode == 40007:
            result.update(id_exists=False, identity_status="invalid_media_id")
        result["error_type"] = "WeChatError"
    except Exception as exc:
        result["error_type"] = type(exc).__name__
    result["checked_at"] = datetime.now(timezone.utc).isoformat()
    return result


def verify_existing(drafts: list[dict[str, Any]], session: requests.Session, token: str, timeout: int) -> dict[str, Any]:
    results = []
    for index, draft in enumerate(drafts, 1):
        if draft.get("verification_scope") == "restored_receipt_identity":
            result = verify_restored_identity(draft, session, token, timeout)
        else:
            articles = materialize_private_article_payload(draft["articles"], os.environ.get("PORTAL_SITE_URL", ""))
            result = verify_draft_get(session, token, draft["media_id"], timeout, len(articles), articles)
        results.append({"draft_index": index, **result})
    report = {
        "ok": bool(results) and all(item.get("ok") is True for item in results),
        "read_only": True,
        "draft_count": len(results),
        "expected_article_count": sum(draft["expected_article_count"] if draft.get("verification_scope") == "restored_receipt_identity"
                                      else len(draft["articles"]) for draft in drafts),
        "verified_article_count": sum(item.get("article_count", 0) for item in results if item.get("ok") is True),
        "drafts": results,
    }
    if results and all(row.get("verification_scope") == "restored_receipt_identity" for row in results):
        report.update(verification_scope="restored_receipt_identity",
                      existing_draft_count=sum(row["id_exists"] is True for row in results),
                      interpretation="Checks draft ID existence and ordered titles/count only; does not verify body, editorial/media contract or publication status.")
    return report


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
