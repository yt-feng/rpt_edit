"""Distribute each account's articles evenly across small draft groups."""
from __future__ import annotations

import json
from pathlib import Path

DEFAULT_ARTICLES_PER_DRAFT = 3
MIN_DRAFTS_PER_ACCOUNT = 3


def draft_group_sizes(article_count: int, max_articles: int = DEFAULT_ARTICLES_PER_DRAFT) -> list[int]:
    if article_count < 0 or not 1 <= max_articles <= 9:
        raise ValueError("Invalid WeChat draft article count or group limit")
    if article_count == 0:
        return []
    groups = max(min(MIN_DRAFTS_PER_ACCOUNT, article_count), (article_count + max_articles - 1) // max_articles)
    size, extra = divmod(article_count, groups)
    return [size + int(index < extra) for index in range(groups)]


def balanced_draft_groups(articles: list, max_articles: int = DEFAULT_ARTICLES_PER_DRAFT) -> list[list]:
    groups = []
    offset = 0
    for size in draft_group_sizes(len(articles), max_articles):
        groups.append(articles[offset:offset + size])
        offset += size
    return groups


def account_group_sizes(selected: list[Path], routes: dict, output_dir: Path, limit: int) -> dict:
    """Keep accepted group boundaries when resuming an existing source upload."""
    path = output_dir / "wechat_draft_summary.json"
    summary = json.loads(path.read_text()) if path.is_file() else {}
    saved = summary.get("drafts", []) if not summary.get("dry_run") else []
    result = {}
    for account in dict.fromkeys(routes.values()):
        names = [report.name for report in selected if routes[report] == account]
        if account is None:
            result[account] = [len(names[index:index + limit]) for index in range(0, len(names), limit)]
            continue
        sizes, saved_names = [], []
        for row in saved:
            if row.get("account") != account or not row.get("media_id"):
                continue
            directories = row.get("report_dirs", [])
            if not directories or len(directories) != row.get("article_count"):
                raise ValueError("Existing routed draft has incomplete source identities")
            saved_names.extend(Path(directory).name for directory in directories)
            sizes.append(len(directories))
        if saved_names != names[:len(saved_names)]:
            raise ValueError("Existing draft groups differ from the selected source order")
        result[account] = sizes + draft_group_sizes(len(names) - len(saved_names), limit)
    return result
