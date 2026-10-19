#!/usr/bin/env python3
"""Find title-only candidates in bounded, read-only WeChat endpoint inventories.

This is diagnostic evidence, never permission to recreate a missing draft. The
freepublish inventory may not include manually mass-sent/group-send articles.
"""

from __future__ import annotations

import argparse
import contextlib
from datetime import datetime, timezone
import io
import json
import os
from pathlib import Path
import unicodedata
from typing import Any
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit

import requests

from push_portal_translated_to_wechat_drafts import (
    get_stable_access_token,
    parse_wechat_json,
    post_wechat_json,
)
from verify_existing_wechat_drafts import load_drafts


ENDPOINTS = {"draft": "draft/batchget", "published": "freepublish/batchget"}
TIME_FIELDS = ("create_time", "update_time", "publish_time", "publish_date")


def safe_error(exc: Exception) -> dict[str, Any]:
    """Exception text can contain credentials, API URLs, or response bodies."""
    error: dict[str, Any] = {"type": type(exc).__name__}
    code = getattr(exc, "errcode", None)
    if isinstance(code, int) and not isinstance(code, bool):
        error["errcode"] = code
    return error


def title_key(value: Any) -> str:
    return " ".join(unicodedata.normalize("NFC", value).split()) if isinstance(value, str) else ""


def public_url(value: Any) -> str:
    if not isinstance(value, str):
        return ""
    try:
        parts = urlsplit(value)
        if (parts.scheme not in {"http", "https"} or parts.hostname != "mp.weixin.qq.com"
                or parts.username or parts.password or parts.port not in {None, 80, 443}
                or not (parts.path == "/s" or parts.path.startswith("/s/"))):
            return ""
        public_fields = {"__biz", "mid", "idx", "sn", "chksm", "scene"}
        query = urlencode([(k, v) for k, v in parse_qsl(parts.query, keep_blank_values=True) if k in public_fields])
        return urlunsplit(("https", "mp.weixin.qq.com", parts.path, query, ""))
    except ValueError:
        return ""


def explicit_times(container: dict[str, Any]) -> dict[str, Any]:
    # Preserve the API's field names; update_time is not publication time.
    return {key: container[key] for key in TIME_FIELDS
            if isinstance(container.get(key), (int, str)) and not isinstance(container.get(key), bool)}


def empty_inventory(kind: str) -> dict[str, Any]:
    return {"endpoint": ENDPOINTS[kind], "complete": False, "pages_requested": 0,
            "pages_received": 0, "groups_scanned": 0, "articles_scanned": 0,
            "reported_total_counts": [], "stop_reason": "not_started", "errors": [], "articles": []}


def scan_inventory(session: requests.Session, token: str, kind: str, timeout: int,
                   max_pages: int = 10, page_size: int = 20) -> dict[str, Any]:
    if kind not in ENDPOINTS or max_pages < 1 or not 1 <= page_size <= 20:
        raise ValueError("Invalid inventory scan bounds")
    result = empty_inventory(kind)
    offset = 0
    seen: set[str] = set()
    unstable = False
    for _ in range(max_pages):
        result["pages_requested"] += 1
        try:
            # A single attempt prevents the shared retry logger from emitting
            # raw provider error messages. A failed page remains unknown.
            response = post_wechat_json(
                session, f"https://api.weixin.qq.com/cgi-bin/{ENDPOINTS[kind]}?access_token={token}",
                {"offset": offset, "count": page_size, "no_content": 0}, timeout, max_attempts=1,
            )
            data = parse_wechat_json(response, ENDPOINTS[kind])
        except Exception as exc:
            result["errors"].append(safe_error(exc))
            result["stop_reason"] = "api_error"
            break
        result["pages_received"] += 1
        total = data.get("total_count")
        items = data.get("item", [] if total == 0 else None)
        count = data.get("item_count")
        if (not isinstance(total, int) or isinstance(total, bool) or total < 0
                or not isinstance(items, list) or len(items) > page_size
                or any(not isinstance(item, dict) for item in items)
                or (count is not None and (not isinstance(count, int) or isinstance(count, bool) or count != len(items)))):
            result["stop_reason"] = "malformed_page"
            break
        if result["reported_total_counts"] and total != result["reported_total_counts"][-1]:
            unstable = True
        result["reported_total_counts"].append(total)
        page_articles = []
        page_ids = []
        malformed = False
        for item in items:
            identifier = item.get("media_id" if kind == "draft" else "article_id")
            content = item.get("content")
            news = content.get("news_item") if isinstance(content, dict) else None
            if (not isinstance(identifier, str) or not identifier.strip()
                    or not isinstance(news, list) or not news
                    or any(not isinstance(article, dict) or not title_key(article.get("title")) for article in news)):
                malformed = True
                break
            page_ids.append(identifier)
            for index, article in enumerate(news):
                page_articles.append({
                    "title": article["title"], "author": article.get("author") if isinstance(article.get("author"), str) else "",
                    "url": public_url(article.get("url")),
                    "group_id": identifier, "article_index": index,
                    "group_times": explicit_times(item), "content_times": explicit_times(content),
                    "article_times": explicit_times(article),
                })
        if malformed:
            result["stop_reason"] = "malformed_article_metadata"
            break
        if len(set(page_ids)) != len(page_ids) or seen.intersection(page_ids):
            result["stop_reason"] = "repeated_group_id"
            break
        seen.update(page_ids)
        result["articles"].extend(page_articles)
        result["groups_scanned"] += len(items)
        result["articles_scanned"] += len(page_articles)
        offset += len(items)
        if offset > total:
            result["stop_reason"] = "inconsistent_total"
            break
        if offset == total:
            result["complete"] = not unstable
            result["stop_reason"] = "total_changed_during_scan" if unstable else "end_of_inventory"
            break
        if not items:
            result["stop_reason"] = "empty_page_before_total"
            break
    else:
        result["stop_reason"] = "page_limit"
    return result


def build_report(drafts: list[dict[str, Any]], inventories: dict[str, dict[str, Any]]) -> dict[str, Any]:
    articles = []
    for draft in drafts:
        for index, expected in enumerate(draft["articles"]):
            title = title_key(expected.get("title"))
            if not title:
                raise ValueError("Archived article has no title")
            article: dict[str, Any] = {"archived_media_id": draft["media_id"], "archived_article_index": index,
                                       "expected_title": expected["title"], "content_identity_verified": False}
            for kind, inventory in inventories.items():
                matches = [{**item, "match_basis": "normalized_title_only",
                            "same_archived_media_id": kind == "draft" and item["group_id"] == draft["media_id"]}
                           for item in inventory["articles"] if title_key(item["title"]) == title]
                article[kind] = {"status": "title_candidates_found" if matches else (
                    "not_found_in_complete_endpoint_inventory" if inventory["complete"] else "unknown"),
                    "candidates": matches}
            articles.append(article)
    return {
        "read_only": True, "ok": all(item["complete"] for item in inventories.values()),
        "checked_at": datetime.now(timezone.utc).isoformat(),
        "scope": "Only draft/batchget and freepublish/batchget inventories were read after authentication.",
        "interpretation": "Title matches are candidates, not proof of identical content. Endpoint nonmatches do not prove deletion or authorize restoration.",
        "url_scope": "URLs retain only public mp.weixin.qq.com article paths and known public query fields, using HTTPS.",
        "published_scope": "freepublish/batchget may not cover manually mass-sent or group-send content.",
        "expected_draft_count": len(drafts), "expected_article_count": len(articles),
        "inventories": {kind: {key: value for key, value in inventory.items() if key != "articles"}
                        for kind, inventory in inventories.items()},
        "articles": articles,
    }


def audit_presence(drafts: list[dict[str, Any]], session: requests.Session, token: str,
                   timeout: int = 60, max_pages: int = 10, page_size: int = 20) -> dict[str, Any]:
    # Scan both independently even if one endpoint denies access or fails.
    inventories = {kind: scan_inventory(session, token, kind, timeout, max_pages, page_size) for kind in ENDPOINTS}
    return build_report(drafts, inventories)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True, type=Path)
    parser.add_argument("--output", required=True, type=Path)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--max-pages", type=int, default=10)
    parser.add_argument("--page-size", type=int, default=20, choices=range(1, 21))
    args = parser.parse_args(argv)
    if args.timeout < 1 or args.max_pages < 1:
        parser.error("timeout and max-pages must be positive")
    try:
        drafts = load_drafts(args.artifact_root)
        appid = os.environ.get("WECHAT_MP_APPID", "").strip()
        secret = os.environ.get("WECHAT_MP_APPSECRET", "").strip()
        if not appid or not secret:
            raise ValueError("WeChat application credentials are required")
        with requests.Session() as session:
            try:
                # Shared authentication retries can log provider messages; do
                # not emit those, or raw exception text, from this diagnostic.
                with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                    token = get_stable_access_token(session, appid, secret, args.timeout)
            except Exception as exc:
                inventories = {kind: empty_inventory(kind) for kind in ENDPOINTS}
                for inventory in inventories.values():
                    inventory.update(stop_reason="authentication_error", errors=[safe_error(exc)])
                report = build_report(drafts, inventories)
            else:
                report = audit_presence(drafts, session, token, args.timeout, args.max_pages, args.page_size)
    except Exception as exc:
        report = {"read_only": True, "ok": False, "status": "unknown", "error": safe_error(exc)}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key not in {"articles"}}, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
