"""Validate receipt identity and structure without claiming delivery success."""

import json
import os
from pathlib import Path
import re


def nonempty_string(value):
    return isinstance(value, str) and bool(value.strip())


def valid_summary(value, date_folder):
    if (not isinstance(value, dict) or value.get("date_folder") != date_folder
            or type(value.get("dry_run")) is not bool
            or not isinstance(value.get("drafts"), list)
            or type(value.get("draft_count")) is not int
            or value["draft_count"] != len(value["drafts"])):
        return False
    if value["drafts"]:
        return all(isinstance(row, dict) and nonempty_string(row.get("media_id"))
                   and (value["dry_run"] or not row["media_id"].startswith("DRY_RUN_"))
                   for row in value["drafts"])
    if type(value.get("selected_count")) is not int or value["selected_count"] != 0 or value.get("articles") != []:
        return False
    status = value.get("status")
    if status in {"skipped_legacy_translation_title_guard", "failed_source_count_mismatch",
                  "failed_no_xhs_wechat_articles", "failed_generation_failure",
                  "failed_title_policy_and_generation_failure"}:
        return True
    skipped = value.get("skipped_title_policy_count")
    policy_complete = (type(skipped) is int and skipped > 0
                       and value.get("input_selected_count") == skipped
                       and isinstance(value.get("skipped_title_policy"), list)
                       and len(value["skipped_title_policy"]) == skipped)
    if status in {"skipped_title_policy", "verified"}:
        return policy_complete
    return status == "dry_run" and value["dry_run"] and (value.get("input_selected_count") == 0 or policy_complete)


def valid_submission(value, filename):
    if not isinstance(value, dict) or type(value.get("schema_version")) is not int or value["schema_version"] != 1:
        return False
    key, account = value.get("group_key"), value.get("account_fingerprint")
    if (not isinstance(key, str) or not re.fullmatch(r"[0-9a-f]{64}", key)
            or not isinstance(account, str) or not re.fullmatch(r"[0-9a-f]{64}", account)
            or filename != f"draft_submission_{key}.json"
            or type(value.get("article_count")) is not int or not 1 <= value["article_count"] <= 9
            or not isinstance(value.get("titles"), list) or len(value["titles"]) != value["article_count"]
            or not all(nonempty_string(title) for title in value["titles"])):
        return False
    status = value.get("status")
    if status == "accepted":
        return nonempty_string(value.get("media_id"))
    return status in {"add_in_flight", "add_outcome_unknown", "rejected"} and "media_id" not in value


def validate_checkpoint(raw_path):
    if not raw_path or not Path(raw_path).is_dir():
        raise SystemExit("Required WeChat checkpoint directory is missing; stop before uploading.")
    root = Path(raw_path).resolve()
    valid = 0
    for path in sorted({*root.rglob("wechat_draft_summary.json"), *root.rglob("draft_submission_*.json")}):
        if not path.is_file() or not path.resolve().is_relative_to(root):
            continue
        try:
            value = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, UnicodeError, ValueError):
            continue
        if (valid_summary(value, root.name) if path.name == "wechat_draft_summary.json"
                else valid_submission(value, path.name)):
            valid += 1
    if not valid:
        raise SystemExit("No structurally valid WeChat summary or submission checkpoint exists; stop before uploading.")
    return valid


if __name__ == "__main__":
    print("Validated WeChat checkpoint records:", validate_checkpoint(os.environ.get("CHECKPOINT_PATH", "").strip()))
