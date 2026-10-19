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


class DeliveryValidationError(ValueError):
    """A fixed diagnostic code, never a remote message or credential URL."""


def require(condition: bool, code: str) -> None:
    if not condition:
        raise DeliveryValidationError(code)


def count_matches(value, expected: int) -> bool:
    return type(value) is int and value == expected


def read_object(path: Path) -> dict:
    value = json.loads(path.read_text(encoding="utf-8"))
    require(isinstance(value, dict), "invalid_json_object")
    return value


def source_selection(source_dir: Path, source_kind: str, expected_count: int,
                     max_articles: str, include_institutions: str, exclude_institutions: str) -> tuple[list[dict], list[dict], int]:
    """Recompute the uploader's selection from this run's source artifacts."""
    from push_portal_translated_to_wechat_drafts import (
        find_report_dirs, translated_article_title_metadata, hard_blocked_portal_title_record,
        parse_institution_filter, parse_selection_limit,
    )
    limit = parse_selection_limit(max_articles, "--max-articles")
    included = parse_institution_filter(include_institutions)
    excluded = parse_institution_filter(exclude_institutions)
    if not source_dir.exists():
        require(expected_count == 0, "missing_source_directory")
        return [], [], 0
    require(source_dir.is_dir(), "invalid_source_directory")
    if source_kind == "xhs":
        from push_xhs_notes_to_wechat_drafts import (
            find_report_dirs, xhs_article_title_metadata, hard_blocked_xhs_title_record,
        )
        require(not included and not excluded, "unsupported_xhs_institution_filter")
        directories = find_report_dirs(source_dir)
        require(all(path.resolve().is_relative_to(source_dir.resolve()) for path in directories), "source_path_escape")
        require(len(directories) == expected_count, "source_count_mismatch")
        selected = directories if limit is None else directories[:limit]
        metadata = [xhs_article_title_metadata(path) for path in selected]
        policy = hard_blocked_xhs_title_record
        institution_excluded_count = 0
    else:
        directories = find_report_dirs(source_dir)
        require(all(path.resolve().is_relative_to(source_dir.resolve()) for path in directories), "source_path_escape")
        if not directories and expected_count == 0:
            return [], [], 0
        translation_path = source_dir / "translation_summary.json"
        require(translation_path.resolve().is_relative_to(source_dir.resolve()), "translation_path_escape")
        translation = read_object(translation_path)
        require(translation.get("date_folder") == source_dir.name, "translation_date_mismatch")
        require(translation.get("failures") == [], "translation_generation_failure")
        # Current translation code applies institution filters and the limit
        # before selected_count; title policy only rewrites at this stage.
        require(translation.get("sensitive_skipped_count", 0) == 0
                and not translation.get("sensitive_skipped", []), "legacy_translation_policy_skip")
        reports = translation.get("reports")
        require(isinstance(reports, list) and all(isinstance(row, dict) for row in reports), "invalid_translation_reports")
        require(count_matches(translation.get("successful_count"), len(directories))
                and count_matches(translation.get("selected_count"), len(directories))
                and len(reports) == len(directories), "incomplete_translation")
        require({Path(str(row.get("output_dir", ""))).resolve() for row in reports}
                == {path.resolve() for path in directories}, "translation_source_identity_mismatch")
        exclusions = translation.get("institution_exclusions", [])
        require(isinstance(exclusions, list) and all(isinstance(row, dict) for row in exclusions), "invalid_institution_exclusions")
        require(count_matches(translation.get("institution_excluded_count", 0), len(exclusions)), "institution_exclusion_count_mismatch")
        if "input_report_count" in translation:
            require(count_matches(translation["input_report_count"], expected_count), "upstream_source_count_mismatch")
            require(set(translation.get("include_institutions", [])) == included
                    and set(translation.get("exclude_institutions", [])) == excluded, "institution_filter_mismatch")
        else:
            # Historical receipts cannot establish any filtering allowance.
            require(not exclusions, "missing_institution_selection_proof")
        from institution_names import infer_institution_name
        excluded_paths = set()
        delivered_sources = {Path(str(row.get("source_report_dir", ""))).resolve() for row in reports}
        for row in exclusions:
            raw_path = str(row.get("source_report_dir", ""))
            path = Path(raw_path)
            institution = infer_institution_name(path.name)
            require(bool(raw_path) and path.resolve() not in excluded_paths
                    and path.resolve() not in delivered_sources, "duplicate_institution_exclusion")
            require(row.get("institution_name") == institution and (
                (row.get("reason") == "outside_include_filter" and bool(included) and institution not in included)
                or (row.get("reason") == "excluded_institution" and institution in excluded)
            ), "unproven_institution_exclusion")
            excluded_paths.add(path.resolve())
        institution_excluded_count = len(exclusions)
        eligible_count = expected_count - institution_excluded_count
        require(eligible_count >= 0, "institution_exclusion_count_mismatch")
        required = eligible_count if limit is None else min(eligible_count, limit)
        require(len(directories) == required, "source_count_mismatch")
        metadata = [translated_article_title_metadata(path) for path in directories]
        require(all((not included or row["institution_name"] in included)
                    and row["institution_name"] not in excluded for row in metadata), "unexpected_source_institution")
        policy = hard_blocked_portal_title_record
    for row in metadata:
        require(Path(row["report_dir"]).resolve().is_relative_to(source_dir.resolve()), "source_path_escape")
    allowed, blocked = [], []
    for row in metadata:
        record = policy(row)
        if record:
            blocked.append(record)
        else:
            require(not row.get("generation_failure_reason"), "article_generation_failure")
            if source_kind == "portal-translated":
                # Policy selection uses original metadata; build_article then
                # sanitizes stock wording before selecting the final title.
                from sensitive_content_guard import sanitize_wechat_stock_language
                directory = Path(row["report_dir"])
                markdown, _ = sanitize_wechat_stock_language(
                    (directory / "translated.md").read_text(encoding="utf-8", errors="ignore"),
                    strict_h1_wording=False,
                )
                row = translated_article_title_metadata(directory, markdown)
            allowed.append(row)
    return allowed, blocked, institution_excluded_count


def live_draft_readback(drafts: list[dict], timeout: int) -> list[dict]:
    """Only token acquisition and draft/get; never repair, create or publish."""
    import os
    import requests
    from push_portal_translated_to_wechat_drafts import (
        get_stable_access_token, materialize_private_article_payload, verify_draft_get,
    )
    appid, secret = os.environ.get("WECHAT_MP_APPID", ""), os.environ.get("WECHAT_MP_APPSECRET", "")
    require(bool(appid.strip() and secret.strip()), "missing_wechat_credentials")
    results = []
    with requests.Session() as session:
        token = get_stable_access_token(session, appid, secret, timeout)
        for draft in drafts:
            articles = materialize_private_article_payload(draft["articles"], os.environ.get("PORTAL_SITE_URL", ""))
            results.append(verify_draft_get(session, token, draft["media_id"], timeout,
                                            len(articles), articles, repair_media=False))
    return results


def validate_delivery(output_dir: Path, source_dir: Path, source_kind: str, expected_count: int,
                      max_articles: str = "all", include_institutions: str = "", exclude_institutions: str = "",
                      dry_run: bool = False, timeout: int = 60, readback=None) -> dict:
    """Fail closed on incomplete receipts; API text is never retained in output."""
    import contextlib
    import io
    from datetime import datetime, timezone

    report = {"ok": False, "delivery_complete": False, "wechat_verified": False,
              "verified_article_count": 0, "verified_draft_count": 0, "policy_excluded_count": 0,
              "institution_excluded_count": 0, "expected_count": expected_count,
              "expected_article_count": 0, "read_only": True, "dry_run": dry_run, "status": "failed"}
    try:
        # Existing API helpers may log remote error messages. Do not let those
        # messages, URLs or credentials reach Actions logs or the final receipt.
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            require(type(expected_count) is int and expected_count >= 0, "invalid_expected_count")
            require(source_kind in {"xhs", "portal-translated"}, "invalid_source_kind")
            require(source_dir.name == output_dir.name, "source_date_mismatch")
            allowed, blocked, institution_excluded = source_selection(
                source_dir, source_kind, expected_count, max_articles, include_institutions, exclude_institutions)
            report.update(expected_article_count=len(allowed), policy_excluded_count=len(blocked),
                          institution_excluded_count=institution_excluded)
            summary_path = output_dir / "wechat_draft_summary.json"
            if expected_count == 0 and not summary_path.exists():
                report.update(ok=True, delivery_complete=not dry_run, status="dry_run" if dry_run else "no_new_articles")
                return report
            require(summary_path.resolve().is_relative_to(output_dir.resolve()), "receipt_path_escape")
            summary = read_object(summary_path)
            require(summary.get("date_folder") == output_dir.name, "receipt_date_mismatch")
            require(summary.get("dry_run") is dry_run, "dry_run_mismatch")
            require(summary.get("publish") is not True, "published_receipt_requires_publication_verification")
            require(count_matches(summary.get("input_selected_count"), len(allowed) + len(blocked)), "input_count_mismatch")
            require(count_matches(summary.get("selected_count"), len(allowed)), "selected_count_mismatch")
            require(count_matches(summary.get("skipped_generation_failure_count", 0), 0)
                    and summary.get("skipped_generation_failures", []) == [], "article_generation_failure")
            policies = summary.get("skipped_title_policy")
            require(isinstance(policies, list) and count_matches(summary.get("skipped_title_policy_count"), len(blocked))
                    and len(policies) == len(blocked), "policy_count_mismatch")
            for saved, actual in zip(policies, blocked):
                require(isinstance(saved, dict) and all(saved.get(key) == actual.get(key) for key in (
                    "report_dir", "skip_reason", "hard_block_reason", "matched_title", "matched_title_field")), "unproven_policy_exclusion")
            articles = summary.get("articles")
            require(isinstance(articles, list) and len(articles) == len(allowed), "article_count_mismatch")
            for saved, actual in zip(articles, allowed):
                require(isinstance(saved, dict) and all(saved.get(key) == actual.get(key) for key in (
                    "report_dir", "wechat_title", "source_report_name", "institution_name")), "receipt_source_mismatch")
            if not allowed:
                require(summary.get("drafts") == [] and count_matches(summary.get("draft_count"), 0), "unexpected_empty_delivery_drafts")
                require(summary.get("status") in {"verified", "dry_run", "skipped_title_policy", "skipped_no_xhs_wechat_articles"}, "unfinished_receipt")
                report.update(ok=True, delivery_complete=not dry_run,
                              status="dry_run" if dry_run else "policy_excluded" if blocked or institution_excluded else "no_new_articles")
            elif dry_run:
                require(summary.get("status") == "dry_run", "unfinished_dry_run")
                report.update(ok=True, status="dry_run")
            else:
                saved = institution_wechat_delivery_outputs(output_dir)
                require(saved["wechat_verified"] == "true" and int(saved["verified_article_count"]) == len(allowed), "invalid_saved_readback")
                from verify_existing_wechat_drafts import load_drafts
                drafts = load_drafts(output_dir)
                require([item.get("title") for draft in drafts for item in draft["articles"]]
                        == [item["wechat_title"] for item in allowed], "payload_source_title_mismatch")
                current = (readback or live_draft_readback)(drafts, timeout)
                require(isinstance(current, list) and len(current) == len(drafts), "incomplete_live_readback")
                for draft, row in zip(drafts, current):
                    require(isinstance(row, dict) and all(row.get(key) is True for key in (
                        "ok", "matches_editorial_contract", "matches_expected_article_count",
                        "matches_expected_titles", "matches_media_contract"))
                        and count_matches(row.get("article_count"), len(draft["articles"]))
                        and count_matches(row.get("expected_article_count"), len(draft["articles"]))
                        and row.get("media_repair_attempted", False) is False, "current_draft_verification_failed")
                report.update(ok=True, delivery_complete=True, wechat_verified=True, status="verified",
                              verified_article_count=len(allowed), verified_draft_count=len(drafts))
    except DeliveryValidationError as exc:
        report["error_code"] = str(exc)
    except Exception as exc:
        # Only an exception type is safe: requests/API errors can embed tokens.
        report["error_code"] = "delivery_validation_error"
        report["error_type"] = type(exc).__name__
    finally:
        report["checked_at"] = datetime.now(timezone.utc).isoformat()
    return report


def main(argv=None) -> int:
    import argparse
    import os
    parser = argparse.ArgumentParser(description="Validate this upload against its source count and current WeChat drafts, read-only.")
    parser.add_argument("--output-dir", type=Path, required=True)
    parser.add_argument("--source-dir", type=Path, required=True)
    parser.add_argument("--source-kind", choices=("xhs", "portal-translated"), required=True)
    parser.add_argument("--expected-count", type=int, required=True)
    parser.add_argument("--max-articles", default="all")
    parser.add_argument("--include-institutions", default="")
    parser.add_argument("--exclude-institutions", default="")
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args(argv)
    report = validate_delivery(args.output_dir, args.source_dir, args.source_kind, args.expected_count,
                               args.max_articles, args.include_institutions, args.exclude_institutions,
                               args.dry_run, args.timeout)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if os.environ.get("GITHUB_OUTPUT"):
        with open(os.environ["GITHUB_OUTPUT"], "a", encoding="utf-8") as handle:
            for key in ("ok", "delivery_complete", "wechat_verified", "verified_article_count", "verified_draft_count",
                        "policy_excluded_count", "institution_excluded_count", "expected_article_count", "status"):
                value = report[key]
                handle.write(f"{key}={str(value).lower() if isinstance(value, bool) else value}\n")
    print(json.dumps(report, ensure_ascii=False))
    return 0 if report["ok"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
