"""Distribute each account's articles evenly across small draft groups."""
from __future__ import annotations

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
