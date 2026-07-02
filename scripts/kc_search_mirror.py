#!/usr/bin/env python3
"""Mirror external search metadata into R2 for same-origin KC Desk search."""

from __future__ import annotations

import argparse
import json
import os
import sys
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

import requests


EXTERNAL_API = "https://api.reportify.cn/reports"
EXTERNAL_PAGE_SIZE = 50
EXTERNAL_UA = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 "
    "(KHTML, like Gecko) Chrome/124.0 Safari/537.36"
)

AUTHORITY_ORIGIN = "https://www.nash-ai.cn"
AUTHORITY_ENDPOINTS = {
    "foreign": "/reports/foreign/search",
    "foreign-rt": "/reports/foreign-rt/search",
}
AUTHORITY_LABELS = {
    "foreign": "普通外文",
    "foreign-rt": "实时外文",
}

R2_PREFIX = "_search-mirror"


def request_json_with_retries(
    method: Any,
    description: str,
    *,
    retries: int,
    retry_backoff: float,
    **kwargs: Any,
) -> Any:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        try:
            response = method(**kwargs)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as error:
            last_error = error
            if attempt >= retries:
                break
            sleep_seconds = min(retry_backoff * (2 ** (attempt - 1)), 8.0)
            print(
                f"warning: {description} failed on attempt {attempt}/{retries}: {error}; "
                f"retrying in {sleep_seconds:.1f}s",
                file=sys.stderr,
            )
            time.sleep(sleep_seconds)
    raise RuntimeError(f"{description} failed after {retries} attempts: {last_error}")


def iso_date_from_ms(value: Any) -> str:
    try:
        ms = int(value or 0)
    except (TypeError, ValueError):
        return ""
    if not ms:
        return ""
    try:
        return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).date().isoformat()
    except (OSError, OverflowError, ValueError):
        return ""


def clean_text(value: Any, limit: int = 500) -> str:
    text = " ".join(str(value or "").split())
    return text[:limit]


def safe_int(value: Any) -> int:
    try:
        return int(value or 0)
    except (TypeError, ValueError):
        return 0


def slim_external(item: dict[str, Any]) -> dict[str, Any] | None:
    report_id = str(item.get("report_id") or "").strip()
    if not report_id:
        return None
    title = clean_text(item.get("title") or item.get("title_cn") or item.get("report_title"), 300)
    if not title:
        return None
    return {
        "id": report_id,
        "source": "external",
        "title": title,
        "title_cn": clean_text(item.get("title_cn"), 300),
        "institution": clean_text(item.get("institution_name") or item.get("channel_name"), 120),
        "date": iso_date_from_ms(item.get("publish_at") or item.get("created_at")),
        "file_type": clean_text(item.get("file_type"), 40),
        "summary": clean_text(item.get("summary"), 700),
    }


def fetch_external_pages(
    pages: int,
    page_size: int,
    timeout: float,
    retries: int,
    retry_backoff: float,
) -> tuple[list[dict[str, Any]], bool]:
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Referer": "https://reportify.cn/",
        "User-Agent": EXTERNAL_UA,
    })
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    for page in range(1, pages + 1):
        try:
            data = request_json_with_retries(
                session.get,
                f"external page {page}",
                retries=retries,
                retry_backoff=retry_backoff,
                url=EXTERNAL_API,
                params={"query": "", "page_num": page, "page_size": page_size},
                timeout=timeout,
            )
        except RuntimeError as error:
            print(f"warning: stop external mirror at page {page}: {error}", file=sys.stderr)
            return items, False
        raw_items = data.get("items") if isinstance(data, dict) else []
        if not isinstance(raw_items, list) or not raw_items:
            break
        for raw in raw_items:
            if not isinstance(raw, dict):
                continue
            slim = slim_external(raw)
            if not slim or slim["id"] in seen:
                continue
            seen.add(slim["id"])
            items.append(slim)
        time.sleep(0.15)
    return items, True


def authority_payload(page: int, page_size: int) -> dict[str, Any]:
    return {
        "releaseDate": 0,
        "startDate": "",
        "endDate": "",
        "minPages": 0,
        "keyword": "",
        "reportTypes": [],
        "industries": [],
        "pageNum": page,
        "pageSize": page_size,
    }


def slim_authority(kind: str, record: dict[str, Any]) -> dict[str, Any] | None:
    report_id = str(record.get("id") or "").strip()
    if not report_id:
        return None
    title = clean_text(record.get("title"), 300)
    if not title:
        return None
    return {
        "id": f"{kind}:{report_id}",
        "source": "authority",
        "kind": kind,
        "kind_label": AUTHORITY_LABELS.get(kind, ""),
        "title": title,
        "institution": clean_text(record.get("securities") or record.get("companyName"), 120),
        "date": clean_text(record.get("reDate"), 40),
        "report_type": clean_text(record.get("reportType"), 80),
        "page_count": safe_int(record.get("page") or record.get("pages")),
        "language": clean_text(record.get("lang"), 40),
        "stock_code": clean_text(record.get("stockCode") or record.get("companycode"), 60),
        "stock_name": clean_text(record.get("stockName") or record.get("companyName"), 120),
        "author": clean_text(record.get("author") or record.get("authors"), 250),
        "file_type": "pdf",
    }


def fetch_authority_pages(
    pages: int,
    page_size: int,
    timeout: float,
    retries: int,
    retry_backoff: float,
) -> tuple[list[dict[str, Any]], bool]:
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": AUTHORITY_ORIGIN,
        "User-Agent": "KCDeskAuthorityMirror/1.0",
    })
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    complete = True
    for kind, endpoint in AUTHORITY_ENDPOINTS.items():
        referer = f"{AUTHORITY_ORIGIN}/foreign.html" if kind == "foreign" else f"{AUTHORITY_ORIGIN}/foreign-rt.html"
        for page in range(1, pages + 1):
            try:
                data = request_json_with_retries(
                    session.post,
                    f"authority {kind} page {page}",
                    retries=retries,
                    retry_backoff=retry_backoff,
                    url=f"{AUTHORITY_ORIGIN}{endpoint}",
                    headers={"Referer": referer},
                    json=authority_payload(page, page_size),
                    timeout=timeout,
                )
            except RuntimeError as error:
                print(f"warning: stop authority {kind} mirror at page {page}: {error}", file=sys.stderr)
                complete = False
                break
            records = ((data.get("data") or {}).get("records") if isinstance(data, dict) else []) or []
            if not isinstance(records, list) or not records:
                break
            for record in records:
                if not isinstance(record, dict):
                    continue
                slim = slim_authority(kind, record)
                if not slim or slim["id"] in seen:
                    continue
                seen.add(slim["id"])
                items.append(slim)
            time.sleep(0.15)
    return items, complete


def mirror_payload(source: str, items: list[dict[str, Any]], complete: bool = True) -> dict[str, Any]:
    return {
        "source": source,
        "generated_at": datetime.now(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z"),
        "count": len(items),
        "complete": complete,
        "items": items,
    }


def write_json(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")


def r2_client() -> Any:
    import boto3

    account_id = os.environ.get("R2_ACCOUNT_ID", "").strip()
    access_key = os.environ.get("R2_ACCESS_KEY_ID", "").strip()
    secret_key = os.environ.get("R2_SECRET_ACCESS_KEY", "").strip()
    if not account_id or not access_key or not secret_key:
        raise RuntimeError("R2_ACCOUNT_ID, R2_ACCESS_KEY_ID, and R2_SECRET_ACCESS_KEY are required")
    return boto3.client(
        "s3",
        endpoint_url=f"https://{account_id}.r2.cloudflarestorage.com",
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name="auto",
    )


def upload_r2(source: str, payload: dict[str, Any]) -> None:
    bucket = os.environ.get("R2_BUCKET", "").strip()
    if not bucket:
        raise RuntimeError("R2_BUCKET is required")
    body = json.dumps(payload, ensure_ascii=False, separators=(",", ":")).encode("utf-8")
    r2_client().put_object(
        Bucket=bucket,
        Key=f"{R2_PREFIX}/{source}/latest.json",
        Body=body,
        ContentType="application/json; charset=utf-8",
        CacheControl="no-store",
        Metadata={
            "source": source,
            "generated_at": payload.get("generated_at", ""),
        },
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-pages", type=int, default=40)
    parser.add_argument("--authority-pages", type=int, default=30)
    parser.add_argument("--page-size", type=int, default=EXTERNAL_PAGE_SIZE)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-backoff", type=float, default=1.5)
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/kc-search-mirror"))
    parser.add_argument("--upload-r2", action="store_true")
    args = parser.parse_args()

    external_items, external_complete = fetch_external_pages(
        args.external_pages,
        args.page_size,
        args.timeout,
        args.retries,
        args.retry_backoff,
    )
    authority_items, authority_complete = fetch_authority_pages(
        args.authority_pages,
        args.page_size,
        args.timeout,
        args.retries,
        args.retry_backoff,
    )
    external = mirror_payload("external", external_items, external_complete)
    authority = mirror_payload("authority", authority_items, authority_complete)

    write_json(args.output_dir / "external.json", external)
    write_json(args.output_dir / "authority.json", authority)

    if args.upload_r2:
        if external_complete:
            upload_r2("external", external)
        else:
            print("warning: external mirror incomplete; keep previous R2 latest.json", file=sys.stderr)
        if authority_complete:
            upload_r2("authority", authority)
        else:
            print("warning: authority mirror incomplete; keep previous R2 latest.json", file=sys.stderr)

    print(
        f"external={external['count']} complete={external_complete} "
        f"authority={authority['count']} complete={authority_complete}"
    )
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
