#!/usr/bin/env python3
"""Regroup receipt-bound drafts using their current content and durable private checkpoints."""
from __future__ import annotations

import argparse
from collections import Counter
from contextlib import redirect_stderr, redirect_stdout
from datetime import date, timedelta
from difflib import SequenceMatcher
import hashlib
import html
import io
import json
from pathlib import Path

import requests

from delete_wechat_drafts import delete_draft
from private_workflow_handoff import build_r2_client, r2_bucket
from push_portal_translated_to_wechat_drafts import (
    WeChatError, add_draft, draft_news_items, get_draft, get_stable_access_token,
)
from repair_wechat_draft_images import WECHAT_DRAFT_WRITABLE_FIELDS, read_complete_draft_catalog
from verify_existing_wechat_drafts import load_drafts
from wechat_account_routing import parse_source_date
from wechat_accounts import ACCOUNT_NAMES, account_credentials, draft_account, draft_tokens
from wechat_draft_grouping import balanced_draft_groups

FIELDS = (*WECHAT_DRAFT_WRITABLE_FIELDS, "article_type", "show_cover_pic", "pic_crop_235_1", "pic_crop_1_1")
MAX_STATE_BYTES = 16 * 1024 * 1024


def markup_difference(actual, expected):
    safe = {"amp;", "&amp;", "<p><br></p>", "<p><br/></p>", "<div>", "</div>", "\n", " ", "<br/>", "<br>"}
    changes = []
    for operation, a, b, c, d in SequenceMatcher(None, expected, actual, autojunk=False).get_opcodes():
        if operation == "equal":
            continue
        before, after = expected[a:b], actual[c:d]
        changes.append({"operation": operation, "before_length": len(before), "after_length": len(after),
                        **({"before": before} if before in safe or len(before) <= 3 else {}),
                        **({"after": after} if after in safe or len(after) <= 3 else {})})
    return {"equal_after_html_unescape": html.unescape(actual) == html.unescape(expected), "markup_changes": changes[:20]}


class ContentMismatch(ValueError):
    def __init__(self, actual, expected):
        super().__init__("replacement_content_changed")
        self.differences = [
            {"article": index, "field": field,
             "actual_type": type(row.get(field)).__name__, "expected_type": type(reference.get(field)).__name__,
             "actual_length": len(str(row.get(field, ""))), "expected_length": len(str(reference.get(field, ""))),
             "actual_sha256": fingerprint(row.get(field)), "expected_sha256": fingerprint(reference.get(field)),
             **(markup_difference(row[field], reference[field]) if field == "content" else {}),
             **({"actual": row.get(field), "expected": reference.get(field)}
                if field in {"need_open_comment", "only_fans_can_comment", "show_cover_pic"} else {})}
            for index, (row, reference) in enumerate(zip(actual, expected))
            for field in FIELDS if row.get(field) != reference.get(field)
        ]


def require(condition, category):
    if not condition:
        raise ValueError(category)


def encoded(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":")).encode()


def fingerprint(value):
    return hashlib.sha256(encoded(value)).hexdigest()


def writable_articles(data):
    articles = draft_news_items(data)
    require(bool(articles) and len(articles) <= 9, "invalid_live_article_count")
    result = []
    for article in articles:
        require(article.get("article_type", "news") == "news", "unsupported_article_type")
        require(all(isinstance(article.get(key), str) and article[key].strip()
                    for key in ("title", "content", "thumb_media_id")), "incomplete_live_article")
        result.append({key: article[key] for key in FIELDS if key in article})
    return result


def group_matches(actual, expected):
    if len(actual) != len(expected):
        return False
    for row, reference in zip(actual, expected):
        for field in FIELDS:
            # WeChat may supply defaults for flags that were absent in a request.
            default = 0 if field in {"need_open_comment", "only_fans_can_comment", "show_cover_pic"} else ""
            if field == "article_type":
                default = "news"
            if row.get(field, default) != reference.get(field, default):
                return False
    return True


class PrivateCheckpoint:
    def __init__(self, client, bucket, key):
        self.client, self.bucket, self.key = client, bucket, key
        self.version = None

    def load(self):
        try:
            response = self.client.get_object(Bucket=self.bucket, Key=self.key)
        except Exception as error:
            code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
            if code in {"404", "NoSuchKey", "NotFound"}:
                return None
            raise
        with response["Body"] as body:
            raw = body.read(MAX_STATE_BYTES + 1)
        require(0 < len(raw) <= MAX_STATE_BYTES and response.get("ETag"), "invalid_private_checkpoint")
        require(hashlib.sha256(raw).hexdigest() == response.get("Metadata", {}).get("sha256"),
                "private_checkpoint_digest_mismatch")
        self.version = response["ETag"]
        return json.loads(raw)

    def save(self, state):
        raw = encoded(state)
        require(len(raw) <= MAX_STATE_BYTES, "private_checkpoint_too_large")
        condition = {"IfMatch": self.version} if self.version else {"IfNoneMatch": "*"}
        try:
            self.client.put_object(
                Bucket=self.bucket, Key=self.key, Body=raw, ContentType="application/json",
                CacheControl="private, no-store", Metadata={"sha256": hashlib.sha256(raw).hexdigest()}, **condition,
            )
        except Exception as error:
            status = getattr(error, "response", {}).get("ResponseMetadata", {}).get("HTTPStatusCode")
            require(status not in {409, 412}, "regroup_checkpoint_changed")
            # A lost write acknowledgement is resolved by durable readback.
            require(self.load() == state, "regroup_checkpoint_write_unresolved")
            return
        require(self.load() == state, "regroup_checkpoint_readback_mismatch")


def source_drafts(root, publication_date):
    summaries = list(root.rglob("wechat_draft_summary.json"))
    require(bool(summaries), "source_summary_missing")
    for path in summaries:
        summary = json.loads(path.read_text())
        published_on = parse_source_date(summary.get("date_folder", ""))
        if summary.get("source") == "xhs_notes/dropbox":
            published_on += timedelta(days=1)
        require(published_on == publication_date, "source_publication_date_mismatch")
        require(summary.get("status") == "verified" and summary.get("dry_run") is False
                and summary.get("publish") is False, "source_is_not_a_verified_draft_upload")
        require(all(row.get("status") == "verified" and not row.get("publish_id")
                    for row in summary.get("drafts", [])), "source_draft_is_not_verified")
    return load_drafts(root)


def snapshot(drafts, tokens, session, timeout):
    accounts = {}
    for account in dict.fromkeys(draft_account(row) for row in drafts):
        token = tokens[account]
        catalog = read_complete_draft_catalog(session, token, timeout)
        live_ids = {row["media_id"] for row in catalog}
        originals, missing = [], []
        for draft in drafts:
            if draft_account(draft) != account:
                continue
            if draft["media_id"] not in live_ids:
                missing.append({"media_id": draft["media_id"], "article_count": len(draft["articles"])})
                continue
            articles = writable_articles(get_draft(session, token, draft["media_id"], timeout))
            originals.append({"media_id": draft["media_id"], "articles": articles, "status": "present"})
        all_articles = [article for original in originals for article in original["articles"]]
        require(len({fingerprint(article) for article in all_articles}) == len(all_articles), "duplicate_source_articles")
        groups = []
        for articles in balanced_draft_groups(all_articles):
            existing = [row["media_id"] for row in originals if group_matches(row["articles"], articles)]
            require(len(existing) <= 1, "ambiguous_original_group")
            groups.append({"articles": articles, "status": "accepted" if existing else "not_started",
                           "media_id": existing[0] if existing else ""})
        accounts[account] = {
            "account_fingerprint": hashlib.sha256(account_credentials(account)[0].encode()).hexdigest(),
            "originals": originals, "unavailable": missing, "groups": groups,
            "baseline_ids": sorted(live_ids), "status": "planned",
        }
    return accounts


def check_group(session, token, group, timeout):
    actual = writable_articles(get_draft(session, token, group["media_id"], timeout))
    if not group_matches(actual, group["articles"]):
        raise ContentMismatch(actual, group["articles"])


def recover_pending_group(session, token, account, group, timeout):
    matches = [row["media_id"] for row in read_complete_draft_catalog(session, token, timeout)
               if row["media_id"] not in account["baseline_ids"]
               and group_matches(writable_articles(row), group["articles"])]
    require(len(matches) == 1, "previous_draft_add_outcome_unresolved")
    group.update(media_id=matches[0], status="accepted")


def apply_account(state, account, token, session, timeout, checkpoint):
    target = state["accounts"][account]
    check_originals(target, session, token, timeout)
    for group in target["groups"]:
        if group["status"] == "add_in_flight":
            recover_pending_group(session, token, target, group, timeout)
            checkpoint.save(state)
        if group["status"] == "not_started":
            group["status"] = "add_in_flight"
            checkpoint.save(state)
            try:
                media_id = add_draft(session, token, group["articles"], timeout)
            except WeChatError as error:
                if error.errcode is not None:
                    group["status"] = "not_started"
                    checkpoint.save(state)
                raise
            group.update(media_id=media_id, status="accepted")
            checkpoint.save(state)
        check_group(session, token, group, timeout)
        group["status"] = "verified"
        checkpoint.save(state)

    kept_ids = {group["media_id"] for group in target["groups"]}
    check_originals(target, session, token, timeout)

    for original in target["originals"]:
        if original["media_id"] in kept_ids or original["status"] == "deleted":
            continue
        try:
            actual = writable_articles(get_draft(session, token, original["media_id"], timeout))
        except WeChatError as error:
            require(error.errcode == 40007 and original["status"] == "delete_in_flight", "original_draft_disappeared")
        else:
            require(group_matches(actual, original["articles"]), "original_content_changed_before_delete")
            for group in target["groups"]:
                check_group(session, token, group, timeout)
            original["status"] = "delete_in_flight"
            checkpoint.save(state)
            delete_draft(session, token, original["media_id"], timeout)
        original["status"] = "deleted"
        checkpoint.save(state)

    current = {row["media_id"]: writable_articles(row)
               for row in read_complete_draft_catalog(session, token, timeout)}
    expected_articles = Counter(fingerprint(article) for row in target["originals"] for article in row["articles"])
    actual_articles = []
    for group in target["groups"]:
        require(group["media_id"] in current and group_matches(current[group["media_id"]], group["articles"]),
                "final_replacement_readback_failed")
        actual_articles.extend(group["articles"])
    require(Counter(map(fingerprint, actual_articles)) == expected_articles, "final_article_count_mismatch")
    require(all(row["media_id"] in kept_ids or row["media_id"] not in current for row in target["originals"]),
            "original_draft_still_present")
    target["status"] = "complete"
    checkpoint.save(state)


def check_originals(target, session, token, timeout):
    for original in target["originals"]:
        if original["status"] in {"deleted", "delete_in_flight"}:
            continue
        actual = writable_articles(get_draft(session, token, original["media_id"], timeout))
        require(group_matches(actual, original["articles"]), "original_content_changed_since_snapshot")


def public_report(state, apply):
    return {
        "publication_date": state["publication_date"], "applied": apply,
        "complete": apply and all(row["status"] == "complete" for row in state["accounts"].values()),
        "accounts": [{
            "account": ACCOUNT_NAMES[account], "status": row["status"],
            "remaining_articles": sum(len(group["articles"]) for group in row["groups"]),
            "original_drafts": len(row["originals"]),
            "unavailable_original_drafts": len(row["unavailable"]),
            "group_sizes": [len(group["articles"]) for group in row["groups"]],
            "deleted_original_drafts": sum(original["status"] == "deleted" for original in row["originals"]),
        } for account, row in state["accounts"].items()],
    }


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--artifact-root", type=Path, required=True)
    parser.add_argument("--publication-date", type=date.fromisoformat, required=True)
    parser.add_argument("--source-run-id", type=int, required=True)
    parser.add_argument("--output", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--timeout", type=int, default=60)
    args = parser.parse_args(argv)
    report = {"complete": False, "applied": args.apply}
    state = None
    try:
        with redirect_stdout(io.StringIO()), redirect_stderr(io.StringIO()):
            drafts = source_drafts(args.artifact_root, args.publication_date)
            source_identity = fingerprint(drafts)
            key = f"_workflow-state/wechat/regroup/v1/{args.publication_date}/{args.source_run_id}.json"
            checkpoint = PrivateCheckpoint(build_r2_client(), r2_bucket(), key)
            state = checkpoint.load()
            if state is not None:
                require(state.get("version") == 1 and state.get("source_identity") == source_identity
                        and state.get("publication_date") == args.publication_date.isoformat(), "regroup_source_changed")
            with requests.Session() as session:
                tokens = draft_tokens(session, drafts, args.timeout, get_stable_access_token)
                if state is None:
                    state = {"version": 1, "publication_date": args.publication_date.isoformat(),
                             "source_identity": source_identity,
                             "accounts": snapshot(drafts, tokens, session, args.timeout)}
                    if args.apply:
                        checkpoint.save(state)
                for account, target in state["accounts"].items():
                    require(target["account_fingerprint"] == hashlib.sha256(account_credentials(account)[0].encode()).hexdigest(),
                            "regroup_account_changed")
                    if args.apply:
                        apply_account(state, account, tokens[account], session, args.timeout, checkpoint)
                report = public_report(state, args.apply)
    except Exception as error:
        if state is not None:
            report = public_report(state, args.apply)
        report.update(error_type=type(error).__name__)
        if isinstance(error, ContentMismatch):
            report.update(error_code=str(error), field_differences=error.differences)
        if type(error) is ValueError:
            report["error_code"] = str(error)
        if isinstance(error, WeChatError):
            report["wechat_error_code"] = error.errcode
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps(report, ensure_ascii=False), flush=True)
    return int("error_type" in report or (args.apply and not report["complete"]))


if __name__ == "__main__":
    raise SystemExit(main())
