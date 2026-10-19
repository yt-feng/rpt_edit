#!/usr/bin/env python3
"""Restore only missing archived WeChat drafts, without publishing or editing."""

from __future__ import annotations

import argparse
from collections import Counter
import contextlib
import hashlib
import io
import json
import os
from pathlib import Path
from typing import Any

import requests

from audit_wechat_article_presence import safe_error, scan_inventory, title_key
from push_portal_translated_to_wechat_drafts import (
    WeChatError, get_draft, get_stable_access_token, materialize_private_article_payload,
    parse_wechat_json, post_wechat_json, verify_draft_get,
)
from verify_existing_wechat_drafts import load_drafts


class RestoreBlocked(RuntimeError):
    def __init__(self, reason: str):
        self.reason = reason
        super().__init__(reason)


def failure(exc: Exception) -> dict[str, Any]:
    return {**safe_error(exc), **({"reason": exc.reason} if isinstance(exc, RestoreBlocked) else {})}


def validate_source_receipts(root: Path, drafts: list[dict[str, Any]]) -> None:
    by_id = {draft["media_id"]: draft for draft in drafts}
    for path in root.rglob("wechat_draft_summary.json"):
        source = json.loads(path.read_text(encoding="utf-8"))
        if source.get("status") != "verified" or source.get("publish") is not False or source.get("dry_run") is not False:
            raise RestoreBlocked("source_receipt_is_not_verified_draft_only")
        for group in source.get("drafts", []):
            receipt = group.get("draft_get", {})
            articles = by_id[group["media_id"]]["articles"]
            if (group.get("status") != "verified" or group.get("published") is not False
                    or group.get("publish_id") or not isinstance(receipt, dict)
                    or any(receipt.get(flag) is not True for flag in (
                        "ok", "matches_expected_article_count", "matches_expected_titles",
                        "matches_editorial_contract", "matches_media_contract"))
                    or receipt.get("article_count") != len(articles)
                    or receipt.get("expected_article_count") != len(articles)
                    or receipt.get("titles") != [article["title"] for article in articles]):
                raise RestoreBlocked("source_draft_receipt_contract_is_incomplete")


def checkpoint(path: Path, report: dict[str, Any]) -> None:
    report["verified_draft_count"] = sum(group.get("status") == "verified" for group in report["drafts"])
    report["verified_article_count"] = sum(group["article_count"] for group in report["drafts"] if group.get("status") == "verified")
    report["ok"] = report.get("status") == "verified" and report["verified_draft_count"] == len(report["drafts"])
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_suffix(path.suffix + ".tmp")
    temporary.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    temporary.replace(path)


def complete_inventory(session: requests.Session, token: str, timeout: int, max_pages: int) -> dict[str, Any]:
    inventory = scan_inventory(session, token, "draft", timeout, max_pages=max_pages)
    if not inventory["complete"]:
        raise RestoreBlocked("draft_inventory_incomplete_" + inventory["stop_reason"])
    return inventory


def matching_group(articles: list[dict[str, Any]], inventory: dict[str, Any]) -> tuple[str, list[str]]:
    expected = Counter(title_key(article["title"]) for article in articles)
    by_id: dict[str, list[str]] = {}
    for article in inventory["articles"]:
        by_id.setdefault(article["group_id"], []).append(title_key(article["title"]))
    overlaps = [(identifier, titles) for identifier, titles in by_id.items() if set(titles).intersection(expected)]
    if not overlaps:
        return "", []
    if len(overlaps) != 1 or Counter(overlaps[0][1]) != expected:
        raise RestoreBlocked("existing_title_subset_or_duplicate_groups")
    return overlaps[0]


def aligned_articles(articles: list[dict[str, Any]], titles: list[str]) -> list[dict[str, Any]]:
    by_title = {title_key(article["title"]): article for article in articles}
    return [by_title[title] for title in titles] if titles else articles


def verify_group(group: dict[str, Any], articles: list[dict[str, Any]], report: dict[str, Any], output: Path,
                 session: requests.Session, token: str, timeout: int) -> None:
    group["status"] = "pending_verification"
    checkpoint(output, report)  # Accepted ID is durable before any readback.
    with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
        result = verify_draft_get(session, token, group["media_id"], timeout, len(articles), articles, repair_media=False)
    group["draft_get"] = {key: value for key, value in result.items() if key not in {"error", "errmsg"}}
    group["status"] = "verified" if result.get("ok") is True else "verification_failed"
    checkpoint(output, report)
    if group["status"] != "verified":
        raise RestoreBlocked("existing_or_created_draft_does_not_match_archived_contract")


def restore_missing(drafts: list[dict[str, Any]], output: Path, session: requests.Session, token: str,
                    timeout: int = 60, max_pages: int = 50, expected_articles: int = 15) -> dict[str, Any]:
    count = sum(len(draft["articles"]) for draft in drafts)
    titles = [title_key(article.get("title")) for draft in drafts for article in draft["articles"]]
    if count != expected_articles or not all(titles) or len(set(titles)) != count:
        raise RestoreBlocked("unexpected_article_count_or_duplicate_archived_titles")
    fingerprint = hashlib.sha256(json.dumps(drafts, ensure_ascii=False, sort_keys=True).encode()).hexdigest()
    groups = [{"original_media_id": draft["media_id"], "article_count": len(draft["articles"]),
               "titles": [article["title"] for article in draft["articles"]], "status": "not_started"} for draft in drafts]
    if output.exists():
        report = json.loads(output.read_text(encoding="utf-8"))
        if (report.get("schema_version") != 1 or report.get("source_sha256") != fingerprint
                or not isinstance(report.get("drafts"), list) or len(report["drafts"]) != len(groups)):
            raise RestoreBlocked("checkpoint_does_not_match_archived_source")
        allowed = {"not_started", "add_in_flight", "add_outcome_unknown", "pending_verification", "verification_failed", "verified"}
        for old, expected in zip(report["drafts"], groups):
            if (any(old.get(key) != expected[key] for key in ("original_media_id", "article_count", "titles"))
                    or old.get("status") not in allowed
                    or (old["status"] in {"pending_verification", "verification_failed", "verified"} and not old.get("media_id"))):
                raise RestoreBlocked("checkpoint_group_is_invalid")
    else:
        report = {"schema_version": 1, "source_sha256": fingerprint, "publish": False, "dry_run": False,
                  "expected_article_count": count, "draft_count": len(groups), "drafts": groups}
    report.update(status="in_progress", error=None)
    for group in report["drafts"]:
        if group["status"] == "verified":
            group["status"] = "pending_verification"
    materialized = [materialize_private_article_payload(draft["articles"], os.environ.get("PORTAL_SITE_URL", "")) for draft in drafts]
    try:
        inventory = complete_inventory(session, token, timeout, max_pages)
        plans = []
        # Preflight every group before adding any: a partial/manual edit blocks
        # the entire restoration instead of creating duplicate source articles.
        for group, articles in zip(report["drafts"], materialized):
            try:
                get_draft(session, token, group["original_media_id"], timeout)
                group["original_draft_get"] = {"status": "exists"}
                original_exists = True
            except WeChatError as exc:
                if exc.errcode != 40007:
                    raise
                original_exists = False
                group["original_draft_get"] = {"status": "missing", "errcode": 40007}
            candidate, actual_titles = matching_group(articles, inventory)
            accepted = str(group.get("media_id") or "")
            if original_exists:
                if candidate and candidate != group["original_media_id"]:
                    raise RestoreBlocked("original_exists_with_another_title_match")
                candidate = group["original_media_id"]
            if accepted:
                if candidate and candidate != accepted:
                    raise RestoreBlocked("checkpoint_media_id_conflicts_with_inventory")
                candidate = accepted  # Never recreate an already accepted ID.
            if not candidate and group["status"] != "not_started":
                raise RestoreBlocked("prior_add_outcome_unknown_no_resubmission")
            plans.append((group, aligned_articles(articles, actual_titles), candidate))
        checkpoint(output, report)
        # Verify all existing/recovered groups first. Verification never edits.
        for group, articles, candidate in plans:
            if candidate:
                group.update(media_id=candidate, reused_existing=True)
                verify_group(group, articles, report, output, session, token, timeout)
        for group, articles, candidate in plans:
            if candidate:
                continue
            # Refresh immediately before mutation in case another run or editor
            # added one of these titles since preflight.
            current = complete_inventory(session, token, timeout, max_pages)
            candidate, actual_titles = matching_group(articles, current)
            if candidate:
                group.update(media_id=candidate, reused_existing=True)
                verify_group(group, aligned_articles(articles, actual_titles), report, output, session, token, timeout)
                continue
            group.update(status="add_in_flight", reused_existing=False)
            checkpoint(output, report)  # Crash after POST cannot authorize retry.
            try:
                response = post_wechat_json(session,
                    f"https://api.weixin.qq.com/cgi-bin/draft/add?access_token={token}",
                    {"articles": articles}, timeout, max_attempts=1)
                data = parse_wechat_json(response, "draft/add")
                media_id = data.get("media_id")
                if not isinstance(media_id, str) or not media_id.strip():
                    raise RestoreBlocked("draft_add_missing_media_id")
            except Exception as exc:
                group.update(status="add_outcome_unknown", add_error=failure(exc))
                checkpoint(output, report)
                # Independent inventory lookup recovers accepted-but-unanswered
                # creation. It does not cause another draft/add attempt.
                current = complete_inventory(session, token, timeout, max_pages)
                media_id, actual_titles = matching_group(articles, current)
                if not media_id:
                    raise RestoreBlocked("draft_add_outcome_unknown_no_resubmission") from None
                articles = aligned_articles(articles, actual_titles)
                group["recovered_after_ambiguous_add"] = True
            group.update(media_id=media_id, status="pending_verification")
            checkpoint(output, report)
            verify_group(group, articles, report, output, session, token, timeout)
        report["status"] = "verified"
    except Exception as exc:
        report.update(status="blocked", error=failure(exc))
    checkpoint(output, report)
    return report


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", required=True, type=Path)
    destination = parser.add_mutually_exclusive_group(required=True)
    destination.add_argument("--output", type=Path, help="Restoration checkpoint; never the archived source summary")
    destination.add_argument("--output-dir", type=Path, help="Directory containing restoration_summary.json")
    parser.add_argument("--expected-articles", type=int, default=15)
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--max-pages", type=int, default=50)
    args = parser.parse_args(argv)
    if args.output_dir:
        args.output = args.output_dir / "restoration_summary.json"
    if min(args.expected_articles, args.timeout, args.max_pages) < 1:
        parser.error("bounds must be positive")
    if args.output.resolve().is_relative_to(args.artifact_root.resolve()):
        parser.error("restoration checkpoint must be outside the archived source directory")
    try:
        drafts = load_drafts(args.artifact_root)
        validate_source_receipts(args.artifact_root, drafts)
        appid = os.environ.get("WECHAT_MP_APPID", "").strip()
        secret = os.environ.get("WECHAT_MP_APPSECRET", "").strip()
        if not appid or not secret:
            raise RestoreBlocked("application_credentials_missing")
        with requests.Session() as session:
            with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
                token = get_stable_access_token(session, appid, secret, args.timeout)
            report = restore_missing(drafts, args.output, session, token, args.timeout, args.max_pages, args.expected_articles)
    except Exception as exc:
        report = {"ok": False, "status": "blocked", "error": failure(exc)}
        # Preserve an existing checkpoint if loading/authentication failed.
        error_path = args.output.with_suffix(".error.json")
        error_path.parent.mkdir(parents=True, exist_ok=True)
        error_path.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({key: value for key, value in report.items() if key != "drafts"}, ensure_ascii=False))
    return 0 if report.get("ok") and report.get("status") == "verified" else 1


if __name__ == "__main__":
    raise SystemExit(main())
