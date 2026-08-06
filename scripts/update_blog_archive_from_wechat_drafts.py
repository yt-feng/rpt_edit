#!/usr/bin/env python3
"""Persist public Blog archive records from generated WeChat draft payloads."""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from build_portal_suite_site import (  # noqa: E402
    BLOG_START_DATE,
    load_blog_archive,
    load_blog_draft_articles,
    merge_blog_articles,
    parse_blog_start_date,
    persist_blog_archive,
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

    draft_articles = load_blog_draft_articles(drafts_root, start_date)
    archived_articles = load_blog_archive(archive_root, start_date)
    merged_articles = merge_blog_articles(archived_articles, draft_articles)
    persist_blog_archive(archive_root, merged_articles, start_date)

    before = {str(article.get("fingerprint") or "") for article in archived_articles}
    after = {str(article.get("fingerprint") or "") for article in merged_articles}
    print(
        "blog_archive "
        f"draft_articles={len(draft_articles)} "
        f"archived_before={len(archived_articles)} "
        f"archived_after={len(merged_articles)} "
        f"new_articles={len(after - before)} "
        f"archive_root={archive_root.as_posix()}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
