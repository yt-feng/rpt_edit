#!/usr/bin/env python3
"""Validate saved institution draft readback for operations status outputs."""

from __future__ import annotations

import json
from pathlib import Path


def institution_wechat_delivery_outputs(output_dir: Path) -> dict[str, str]:
    """Summarize a completed upload's saved readback without calling WeChat.

    Call only after this invocation's uploader succeeds. Restored or partial
    checkpoints must never establish a fresh delivery on their own.
    """
    unconfirmed = {"wechat_verified": "false", "verified_article_count": "0", "verified_draft_count": "0"}
    try:
        summary = json.loads((output_dir / "wechat_draft_summary.json").read_text(encoding="utf-8"))
        if (summary.get("dry_run") is not False or summary.get("status") != "verified"
                or summary.get("date_folder") != output_dir.name):
            return unconfirmed
        from verify_existing_wechat_drafts import load_drafts
        from push_portal_translated_to_wechat_drafts import draft_group_key

        drafts = load_drafts(output_dir)
        rows = summary.get("drafts", [])
        article_count = sum(len(draft["articles"]) for draft in drafts)
        if (type(summary.get("draft_count")) is not int or summary["draft_count"] != len(drafts)
                or type(summary.get("selected_count")) is not int or summary["selected_count"] != article_count
                or len(rows) != len(drafts) or len(summary.get("articles", [])) != article_count):
            return unconfirmed
        groups = set()
        for row, draft in zip(rows, drafts):
            readback = row.get("draft_get", {})
            group = draft_group_key(draft["articles"])
            if (row.get("media_id") != draft["media_id"] or row.get("status") != "verified"
                    or row.get("group_key") != group or group in groups
                    or readback.get("article_count") != len(draft["articles"])
                    or readback.get("expected_article_count") != len(draft["articles"])
                    or not all(readback.get(key) is True for key in (
                        "ok", "matches_editorial_contract", "matches_expected_article_count",
                        "matches_expected_titles", "matches_media_contract"))):
                return unconfirmed
            groups.add(group)
        return {"wechat_verified": "true", "verified_article_count": str(article_count),
                "verified_draft_count": str(len(drafts))}
    except (OSError, ValueError, TypeError, AttributeError, KeyError):
        return unconfirmed
