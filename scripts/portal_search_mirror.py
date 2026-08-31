#!/usr/bin/env python3
"""Mirror external search metadata into R2 for same-origin Portal Suite search."""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
import unicodedata
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
PUBLIC_SOURCE_MARKERS = re.compile(
    r"(?:report[\s._-]*ify(?:\.cn)?|nash[\s._-]*ai(?:\.cn)?|nash-ai\.cn|"
    r"macro[\s._-]*gate|support[\s._-]+contact|portal[\s._-]*(?:suite|alternate|娱乐)|kc[\s._-]+desk[\s._-]+notes|"
    r"two[\s._-]*tigers|hibor\.com\.cn|慧博)",
    re.IGNORECASE,
)
EXTERNAL_MIRROR_SEED_QUERIES = [
    "Nomura",
    "Goldman Sachs",
    "Morgan Stanley",
    "J.P. Morgan",
    "JPMorgan",
    "UBS",
    "BofA",
    "Citi",
    "HSBC",
    "Barclays",
    "Deutsche Bank",
    "Macquarie",
    "Bernstein",
    "Asia AI Semi",
    "semiconductor",
    "AI server",
    "China macro",
    "Global Views",
    "equity strategy",
    "FX rates",
]


class TimeBudgetExceeded(RuntimeError):
    """The current mirror stage exhausted its bounded wall-clock budget."""


def request_json_with_retries(
    method: Any,
    description: str,
    *,
    retries: int,
    retry_backoff: float,
    deadline: float | None = None,
    **kwargs: Any,
) -> Any:
    last_error: Exception | None = None
    for attempt in range(1, retries + 1):
        call_kwargs = dict(kwargs)
        if deadline is not None:
            remaining = deadline - time.monotonic()
            if remaining <= 0:
                raise TimeBudgetExceeded(f"{description} exceeded its stage time budget")
            request_timeout = call_kwargs.get("timeout")
            if isinstance(request_timeout, (int, float)):
                call_kwargs["timeout"] = max(0.1, min(float(request_timeout), remaining))
        try:
            response = method(**call_kwargs)
            response.raise_for_status()
            return response.json()
        except (requests.RequestException, ValueError) as error:
            last_error = error
            if attempt >= retries:
                break
            sleep_seconds = min(retry_backoff * (2 ** (attempt - 1)), 8.0)
            if deadline is not None:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise TimeBudgetExceeded(f"{description} exceeded its stage time budget")
                sleep_seconds = min(sleep_seconds, remaining)
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


def public_brand_text(value: Any, limit: int = 500) -> str:
    """Remove aggregator and retired deployment brands from public metadata."""
    text = unicodedata.normalize("NFKC", clean_text(value, max(limit * 2, limit)))
    text = "".join(character for character in text if unicodedata.category(character) != "Cf")
    text = PUBLIC_SOURCE_MARKERS.sub("", text)
    text = re.sub(r"\b(?:by|from)\b(?=\s*(?:$|[|·:/,_-]))", "", text, flags=re.IGNORECASE)
    text = re.sub(r"^[\s|·:：/,_-]+|[\s|·:：/,_-]+$", "", text)
    text = re.sub(r"\s{2,}", " ", text)
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
    title = public_brand_text(item.get("title") or item.get("title_cn") or item.get("report_title"), 300)
    if not title:
        return None
    return {
        "id": report_id,
        "source": "external",
        "title": title,
        "title_cn": public_brand_text(item.get("title_cn"), 300),
        "institution": public_brand_text(item.get("institution_name"), 120),
        "date": iso_date_from_ms(item.get("publish_at") or item.get("created_at")),
        "file_type": public_brand_text(item.get("file_type"), 40),
        "summary": public_brand_text(item.get("summary"), 700),
    }


def add_external_records(
    raw_items: Any,
    items: list[dict[str, Any]],
    seen: set[str],
) -> int:
    if not isinstance(raw_items, list) or not raw_items:
        return 0
    added = 0
    for raw in raw_items:
        if not isinstance(raw, dict):
            continue
        slim = slim_external(raw)
        if not slim or slim["id"] in seen:
            continue
        seen.add(slim["id"])
        items.append(slim)
        added += 1
    return added


def fetch_external_query_pages(
    session: requests.Session,
    query: str,
    pages: int,
    page_size: int,
    timeout: float,
    retries: int,
    retry_backoff: float,
    items: list[dict[str, Any]],
    seen: set[str],
    deadline: float | None = None,
) -> bool:
    for page in range(1, pages + 1):
        description = f"external {query or 'latest'} page {page}"
        try:
            data = request_json_with_retries(
                session.get,
                description,
                retries=retries,
                retry_backoff=retry_backoff,
                deadline=deadline,
                url=EXTERNAL_API,
                params={"query": query, "page_num": page, "page_size": page_size},
                timeout=timeout,
            )
        except TimeBudgetExceeded:
            raise
        except RuntimeError as error:
            print(f"warning: stop {description}: {error}", file=sys.stderr)
            return False
        raw_items = data.get("items") if isinstance(data, dict) else []
        if not isinstance(raw_items, list) or not raw_items:
            break
        add_external_records(raw_items, items, seen)
        time.sleep(0.15)
    return True


def fetch_external_pages(
    pages: int,
    page_size: int,
    timeout: float,
    retries: int,
    retry_backoff: float,
    seed_queries: list[str],
    seed_pages: int,
    budget_seconds: float = 0,
) -> tuple[list[dict[str, Any]], bool]:
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Referer": "https://reportify.cn/",
        "User-Agent": EXTERNAL_UA,
    })
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    deadline = time.monotonic() + budget_seconds if budget_seconds > 0 else None
    try:
        complete = fetch_external_query_pages(
            session,
            "",
            pages,
            page_size,
            timeout,
            retries,
            retry_backoff,
            items,
            seen,
            deadline,
        )
    except TimeBudgetExceeded as error:
        print(f"warning: stop external mirror: {error}", file=sys.stderr)
        return items, False
    if not complete:
        return items, False
    if seed_pages > 0:
        for query in seed_queries:
            seed = clean_text(query, 120)
            if not seed:
                continue
            try:
                seed_complete = fetch_external_query_pages(
                    session,
                    seed,
                    seed_pages,
                    page_size,
                    timeout,
                    retries,
                    retry_backoff,
                    items,
                    seen,
                    deadline,
                )
            except TimeBudgetExceeded as error:
                print(f"warning: stop external seed mirror: {error}", file=sys.stderr)
                return items, False
            complete = seed_complete and complete
    return items, complete


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
    title = public_brand_text(record.get("title"), 300)
    if not title:
        return None
    return {
        "id": f"{kind}:{report_id}",
        "source": "authority",
        "kind": kind,
        "kind_label": AUTHORITY_LABELS.get(kind, ""),
        "title": title,
        "institution": public_brand_text(record.get("securities") or record.get("companyName"), 120),
        "date": clean_text(record.get("reDate"), 40),
        "report_type": public_brand_text(record.get("reportType"), 80),
        "page_count": safe_int(record.get("page") or record.get("pages")),
        "language": clean_text(record.get("lang"), 40),
        "stock_code": clean_text(record.get("stockCode") or record.get("companycode"), 60),
        "stock_name": public_brand_text(record.get("stockName") or record.get("companyName"), 120),
        "author": public_brand_text(record.get("author") or record.get("authors"), 250),
        "file_type": "pdf",
    }


def fetch_authority_pages(
    pages: int,
    page_size: int,
    timeout: float,
    retries: int,
    retry_backoff: float,
    budget_seconds: float = 0,
) -> tuple[list[dict[str, Any]], bool]:
    session = requests.Session()
    session.headers.update({
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Origin": AUTHORITY_ORIGIN,
        "User-Agent": "PortalSuiteAuthorityMirror/1.0",
    })
    items: list[dict[str, Any]] = []
    seen: set[str] = set()
    complete = True
    deadline = time.monotonic() + budget_seconds if budget_seconds > 0 else None
    for kind, endpoint in AUTHORITY_ENDPOINTS.items():
        referer = f"{AUTHORITY_ORIGIN}/foreign.html" if kind == "foreign" else f"{AUTHORITY_ORIGIN}/foreign-rt.html"
        for page in range(1, pages + 1):
            try:
                data = request_json_with_retries(
                    session.post,
                    f"authority {kind} page {page}",
                    retries=retries,
                    retry_backoff=retry_backoff,
                    deadline=deadline,
                    url=f"{AUTHORITY_ORIGIN}{endpoint}",
                    headers={"Referer": referer},
                    json=authority_payload(page, page_size),
                    timeout=timeout,
                )
            except TimeBudgetExceeded as error:
                print(f"warning: stop authority mirror: {error}", file=sys.stderr)
                return items, False
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


def previous_mirror_is_fresh(
    source: str,
    max_age_hours: float,
    *,
    now: datetime | None = None,
    client: Any | None = None,
) -> bool:
    """Check the last successfully uploaded snapshot without exposing its contents."""
    bucket = os.environ.get("R2_BUCKET", "").strip()
    if not bucket or max_age_hours <= 0:
        return False
    try:
        response = (client or r2_client()).get_object(
            Bucket=bucket,
            Key=f"{R2_PREFIX}/{source}/latest.json",
        )
        body = response.get("Body")
        raw = body.read() if hasattr(body, "read") else body
        if not isinstance(raw, (bytes, bytearray)):
            return False
        payload = json.loads(bytes(raw).decode("utf-8"))
        generated_at = str(payload.get("generated_at") or "") if isinstance(payload, dict) else ""
        timestamp = datetime.fromisoformat(generated_at.replace("Z", "+00:00"))
        if timestamp.tzinfo is None:
            timestamp = timestamp.replace(tzinfo=timezone.utc)
        current = now or datetime.now(timezone.utc)
        age_seconds = (current.astimezone(timezone.utc) - timestamp.astimezone(timezone.utc)).total_seconds()
        return 0 <= age_seconds <= max_age_hours * 3600
    except Exception as error:
        print(
            f"warning: unable to validate previous {source} mirror freshness "
            f"({type(error).__name__})",
            file=sys.stderr,
        )
        return False


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--external-pages", type=int, default=40)
    parser.add_argument("--authority-pages", type=int, default=30)
    parser.add_argument("--page-size", type=int, default=EXTERNAL_PAGE_SIZE)
    parser.add_argument("--timeout", type=float, default=30.0)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--retry-backoff", type=float, default=1.5)
    parser.add_argument("--external-budget-seconds", type=float, default=540.0)
    parser.add_argument("--authority-budget-seconds", type=float, default=240.0)
    parser.add_argument("--failure-grace-hours", type=float, default=24.0)
    parser.add_argument("--external-seed-pages", type=int, default=3)
    parser.add_argument("--external-seed-query", action="append", default=[])
    parser.add_argument("--output-dir", type=Path, default=Path("outputs/portal-search-mirror"))
    parser.add_argument("--upload-r2", action="store_true")
    args = parser.parse_args()
    seed_queries = list(dict.fromkeys([*EXTERNAL_MIRROR_SEED_QUERIES, *args.external_seed_query]))

    external_items, external_complete = fetch_external_pages(
        args.external_pages,
        args.page_size,
        args.timeout,
        args.retries,
        args.retry_backoff,
        seed_queries,
        args.external_seed_pages,
        max(0.0, args.external_budget_seconds),
    )
    authority_items, authority_complete = fetch_authority_pages(
        args.authority_pages,
        args.page_size,
        args.timeout,
        args.retries,
        args.retry_backoff,
        max(0.0, args.authority_budget_seconds),
    )
    external = mirror_payload("external", external_items, external_complete)
    authority = mirror_payload("authority", authority_items, authority_complete)

    write_json(args.output_dir / "external.json", external)
    write_json(args.output_dir / "authority.json", authority)

    stale_sources: list[str] = []
    if args.upload_r2:
        if external_complete:
            upload_r2("external", external)
        else:
            print("warning: external mirror incomplete; keep previous R2 latest.json", file=sys.stderr)
            if not previous_mirror_is_fresh("external", max(0.0, args.failure_grace_hours)):
                stale_sources.append("external")
        if authority_complete:
            upload_r2("authority", authority)
        else:
            print("warning: authority mirror incomplete; keep previous R2 latest.json", file=sys.stderr)
            if not previous_mirror_is_fresh("authority", max(0.0, args.failure_grace_hours)):
                stale_sources.append("authority")

    print(
        f"external={external['count']} complete={external_complete} "
        f"authority={authority['count']} complete={authority_complete}"
    )
    if stale_sources:
        print(
            "error: no complete mirror refresh within the grace window for "
            + ", ".join(stale_sources),
            file=sys.stderr,
        )
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
