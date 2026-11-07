"""Reserve a stable WeChat destination for each eligible source article."""
from __future__ import annotations

import hashlib
import json
import os
import re
import time
import unicodedata
from datetime import date, timedelta
from pathlib import Path

from portal_discovery_quality import report_source_metadata
from private_workflow_handoff import build_r2_client, r2_bucket
from wechat_accounts import ACCOUNT_NAMES, all_account_credentials

ROUTING_KEY = "_workflow-state/wechat/account-routing-v1.json"
ACCOUNTS = tuple(ACCOUNT_NAMES)
SOURCES = {"dropbox", "institutions", "consulting", "ark"}


def parse_source_date(folder: str) -> date:
    if not re.fullmatch(r"(?:20)?[0-9]{6}", folder):
        raise ValueError("WeChat routing requires a six- or eight-digit source date")
    return date.fromisoformat("20" + folder if len(folder) == 6 else folder)


def route_start_date() -> date | None:
    value = os.environ.get("WECHAT_ROUTING_START_DATE", "").strip()
    return date.fromisoformat(value) if value else None


def allocate(assigned: dict[str, str], source_ids: list[str]) -> dict[str, str]:
    for source_id in source_ids:
        if source_id not in assigned:
            assigned[source_id] = ACCOUNTS[len(assigned) % len(ACCOUNTS)]
    return {source_id: assigned[source_id] for source_id in source_ids}


def reserve_routes(client, bucket: str, source_ids: list[str]) -> dict[str, str]:
    """Use a single conditional update for all producers, keeping retry assignments."""
    for attempt in range(6):
        assigned, version = read_routes(client, bucket)
        count_before = len(assigned)
        allocation = allocate(assigned, source_ids)
        if len(assigned) == count_before:
            return allocation
        condition = {"IfMatch": version} if version else {"IfNoneMatch": "*"}
        try:
            client.put_object(
                Bucket=bucket, Key=ROUTING_KEY,
                Body=json.dumps({"version": 1, "assigned": assigned}, separators=(",", ":")).encode(),
                ContentType="application/json", CacheControl="private, no-store", **condition,
            )
        except Exception as error:
            status = getattr(error, "response", {}).get("ResponseMetadata", {}).get("HTTPStatusCode")
            if status not in {409, 412}:
                raise
            time.sleep(min(0.25 * 2**attempt, 2))
        else:
            return allocation
    raise RuntimeError("WeChat account routing remained busy")


def read_routes(client, bucket: str) -> tuple[dict[str, str], str]:
    try:
        response = client.get_object(Bucket=bucket, Key=ROUTING_KEY)
    except Exception as error:
        code = str(getattr(error, "response", {}).get("Error", {}).get("Code", ""))
        if code in {"NoSuchKey", "404", "NotFound"}:
            return {}, ""
        raise

    with response["Body"] as body:
        ledger = json.load(body)
    version = response.get("ETag")
    assigned = ledger.get("assigned") if isinstance(ledger, dict) else None
    if (not version or not isinstance(assigned, dict) or ledger.get("version") != 1
            or any(not re.fullmatch(r"[0-9a-f]{64}", key) or value not in ACCOUNTS
                   for key, value in assigned.items())):
        raise ValueError("Invalid WeChat account routing state")
    return assigned, version


def routing_source_name(report: Path) -> str:
    for filename in ("translation_status.json", "status.json"):
        path = report / filename
        if not path.is_file():
            continue
        status = json.loads(path.read_text(encoding="utf-8"))
        if not isinstance(status, dict):
            raise ValueError("Invalid report status for WeChat routing")
        original = (status.get("wechat_routing_source_name") or status.get("source_report_original_name")
                    or status.get("original_report_name") or status.get("original_filename"))
        name = report_source_metadata({**status, "source_report_original_name": original}).get("source_report_name")
        if name:
            return name
        source_dir = status.get("source_report_dir")
        if isinstance(source_dir, str) and source_dir:
            return Path(source_dir).name
    return report.name


def plan_destinations(args, date_dir: Path, reports: list[Path]) -> tuple[
    dict[Path, str | None], dict[str | None, tuple[str, str]]
]:
    """Keep the original destination for batches published before the cutover."""
    primary = (args.wechat_appid, args.wechat_secret)
    start = route_start_date()
    if not reports or not start:
        return dict.fromkeys(reports), {None: primary}
    scope = os.environ.get("WECHAT_ROUTING_SCOPE")
    if scope not in SOURCES:
        raise ValueError("A stable WeChat routing scope is required")
    source_date = parse_source_date(date_dir.name)
    # The nightly Dropbox workflow publishes the previous report day's batch.
    publication_date = source_date + timedelta(days=1 if scope == "dropbox" else 0)
    if publication_date < start:
        return dict.fromkeys(reports), {None: primary}

    names = [unicodedata.normalize("NFC", routing_source_name(report)) for report in reports]
    source_ids = [hashlib.sha256(f"{scope}\0{source_date}\0{name}".encode()).hexdigest() for name in names]
    if len(set(source_ids)) != len(source_ids):
        raise ValueError("Source reports have duplicate identities for WeChat routing")
    credentials = dict.fromkeys(ACCOUNTS, ("", "")) if args.dry_run else all_account_credentials(primary)
    if args.dry_run:
        allocation = allocate({}, source_ids)
    else:
        allocation = reserve_routes(build_r2_client(), r2_bucket(), source_ids)
    return dict(zip(reports, (allocation[source_id] for source_id in source_ids))), credentials
