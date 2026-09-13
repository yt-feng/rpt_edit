#!/usr/bin/env python3
"""Persist public Blog archive records from generated WeChat draft payloads."""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path
from typing import Any

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_portal_suite_site import (  # noqa: E402
    BLOG_START_DATE,
    blog_archive_record,
    blog_html_text,
    load_blog_archive,
    load_blog_draft_articles,
    merge_blog_articles,
    parse_blog_start_date,
    persist_blog_archive,
)
from check_public_identity import confusable_skeleton, private_markers  # noqa: E402
from sensitive_content_guard import nomura_sensitive_wechat_report_reasons  # noqa: E402


ORIGINAL_REPORT_RE = re.compile(r"Original report:\s*([^<\n]+)", re.IGNORECASE)
NOMURA_TITLE_MARKER_RE = re.compile(
    r"(?:野村(?:证券)?|(?<![A-Za-z])NOM(?:$|[\s_\\/\-]))",
    re.IGNORECASE,
)


def nomura_sensitive_blog_article_reason(article: dict[str, Any]) -> str | None:
    """Return the publication hard-block code for a sensitive archived article."""
    title = str(article.get("title") or "")
    content = str(article.get("content") or "")
    plain_content = blog_html_text(content)
    report_match = ORIGINAL_REPORT_RE.search(plain_content)
    source_report_name = report_match.group(1).strip() if report_match else ""
    metadata = {
        "raw_title": title,
        "original_title": source_report_name,
        "source_report_name": source_report_name,
        "wechat_title": title,
    }
    if NOMURA_TITLE_MARKER_RE.search(f"{title} {source_report_name}"):
        metadata["institution_name"] = "野村"
    reasons = nomura_sensitive_wechat_report_reasons(metadata, plain_content)
    if any(reason.endswith(":rmb_fixing_or_pricing") for reason in reasons):
        return "nomura_rmb_fixing_or_pricing"
    return None


def split_hard_blocked_blog_articles(
    articles: list[dict[str, Any]],
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    allowed: list[dict[str, Any]] = []
    blocked: list[dict[str, Any]] = []
    for article in articles:
        if nomura_sensitive_blog_article_reason(article):
            blocked.append(article)
        else:
            allowed.append(article)
    return allowed, blocked


def delete_blocked_archive_shards(archive_root: Path, articles: list[dict[str, Any]]) -> int:
    """Remove only validated archive shards for hard-blocked articles."""
    deleted = 0
    for article in articles:
        fingerprint = str(article.get("fingerprint") or "")
        date_value = str(article.get("date") or "")
        if not re.fullmatch(r"[0-9a-f]{64}", fingerprint) or not re.fullmatch(
            r"\d{4}-\d{2}-\d{2}", date_value
        ):
            raise ValueError("Cannot delete hard-blocked archive article with invalid identity")
        path = archive_root / date_value.replace("-", "") / f"{fingerprint}.json"
        if path.is_symlink():
            raise ValueError(f"Hard-blocked archive shard must not be a symlink: {path}")
        if path.is_file():
            path.unlink()
            deleted += 1
    return deleted


def assert_public_archive_identity(articles: list[dict[str, Any]]) -> None:
    """Reject private deployment markers before public archive records are written."""
    markers = tuple(marker.casefold() for marker in private_markers())
    failed: list[str] = []
    for article in articles:
        record = blog_archive_record(article)
        serialized = json.dumps(record, ensure_ascii=False, sort_keys=True)
        skeleton = confusable_skeleton(serialized)
        if any(marker in skeleton for marker in markers):
            failed.append(str(record.get("fingerprint") or "unknown"))
    if failed:
        raise ValueError(
            "Private identity marker found in public Blog archive record(s): "
            + ", ".join(sorted(failed))
        )


def main() -> int:
    parser = argparse.ArgumentParser(description="Update Portal Suite Blog archive from WeChat draft payloads.")
    parser.add_argument("--wechat-drafts-root", default="wechat_drafts")
    parser.add_argument("--blog-archive-root", default="portal_suite/data/blog_archive")
    parser.add_argument("--blog-start-date", default=BLOG_START_DATE)
    args = parser.parse_args()

    start_date = parse_blog_start_date(args.blog_start_date)
    drafts_root = Path(args.wechat_drafts_root)
    archive_root = Path(args.blog_archive_root)

    draft_articles, blocked_draft_articles = split_hard_blocked_blog_articles(
        load_blog_draft_articles(drafts_root, start_date)
    )
    archived_articles, blocked_archived_articles = split_hard_blocked_blog_articles(
        load_blog_archive(archive_root, start_date)
    )
    merged_articles = merge_blog_articles(archived_articles, draft_articles)
    assert_public_archive_identity(merged_articles)
    persist_blog_archive(archive_root, merged_articles, start_date)
    deleted_archived_count = delete_blocked_archive_shards(
        archive_root,
        blocked_archived_articles,
    )

    before = {str(article.get("fingerprint") or "") for article in archived_articles}
    after = {str(article.get("fingerprint") or "") for article in merged_articles}
    print(
        "blog_archive "
        f"draft_articles={len(draft_articles)} "
        f"archived_before={len(archived_articles)} "
        f"archived_after={len(merged_articles)} "
        f"new_articles={len(after - before)} "
        f"hard_blocked_drafts_skipped={len(blocked_draft_articles)} "
        f"hard_blocked_archive_shards_deleted={deleted_archived_count} "
        f"archive_root={archive_root.as_posix()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
