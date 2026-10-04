#!/usr/bin/env python3
"""Read-only cloud acceptance of dated private PDFs and KCDesk's public list.

Does not authenticate a customer, publish, generate, or change stored objects.
The anonymous download check confirms the membership gate, not a paid download.
"""
import argparse
import json
import os
from pathlib import Path
import urllib.error
import urllib.request

from upload_market_view_to_r2 import (
    build_r2_client, parse_issue_date, validate_existing_private_pair,
)

ORIGIN = "https://kcdesk.com"


class InspectionError(ValueError):
    pass


class NoRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, *args, **kwargs):
        raise InspectionError("unexpected_redirect")


def get_public(path, *, max_bytes=1_000_000):
    opener = urllib.request.build_opener(NoRedirect())
    try:
        response = opener.open(urllib.request.Request(ORIGIN + path,
            headers={"Accept": "application/json", "User-Agent": "KCDesk-MarketViews-Acceptance/1"}), timeout=30)
    except urllib.error.HTTPError as error:
        response = error
    with response:
        body = response.read(max_bytes + 1)
        if len(body) > max_bytes:
            raise InspectionError("response_size_exceeded")
        return response.status, response.headers.get_content_type(), body


def inspect_date(client, bucket, date_key, listing, fetch=get_public):
    issue_date, normalized = parse_issue_date(date_key)
    if normalized != date_key:
        raise InspectionError("date_must_be_yymmdd")
    pdf_key, item_key = f"_market-views/pdfs/{date_key}.pdf", f"_market-views/items/{date_key}.json"
    item = validate_existing_private_pair(client, bucket, pdf_key=pdf_key, item_key=item_key,
        pdf_head=client.head_object(Bucket=bucket, Key=pdf_key),
        item_head=client.head_object(Bucket=bucket, Key=item_key),
        issue_date=issue_date, date_key=date_key, filename=f"market_views_{date_key}.pdf")
    matches = [row for row in listing if isinstance(row, dict) and row.get("id") == item["id"]]
    if len(matches) != 1:
        raise InspectionError("public_date_missing_or_duplicated")
    if any(matches[0].get(key) != item[key] for key in ("id", "date", "filename", "size_bytes")):
        raise InspectionError("public_private_metadata_mismatch")
    status, _, _ = fetch(f"/api/market-views/pdf?id=market-view%3A{date_key}")
    if status != 401:
        raise InspectionError("anonymous_membership_gate_failed")
    return {"date": item["date"], "id": item["id"], "private_pdf_sha256": item["sha256"],
            "size_bytes": item["size_bytes"], "private_pdf_full_read_verified": True,
            "public_list_matches": True, "anonymous_download_status": status,
            "authenticated_download_verified": False}


def inspect(client, bucket, dates, fetch=get_public):
    if not dates or len(dates) > 4 or len(set(dates)) != len(dates):
        raise InspectionError("bounded_unique_dates_required")
    # Validate before network or R2 access.
    for key in dates:
        _, normalized = parse_issue_date(key)
        if normalized != key:
            raise InspectionError("date_must_be_yymmdd")
    status, content_type, body = fetch("/api/market-views")
    if status != 200 or content_type != "application/json":
        raise InspectionError("public_list_unavailable")
    listing = json.loads(body)
    items = listing.get("items") if isinstance(listing, dict) else None
    if not isinstance(items, list) or len(items) > 500 or listing.get("total") != len(items):
        raise InspectionError("public_list_contract_failed")
    return {"schema_version": 1, "success": True, "read_only": True,
            "production_writes": 0, "provider_posts": 0, "model_calls": 0,
            "authenticated_download_verified": False,
            "dates": [inspect_date(client, bucket, key, items, fetch) for key in dates]}


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dates", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        result = inspect(build_r2_client(), os.environ.get("R2_BUCKET") or "portal-suite-pdfs", args.dates.split(","))
    except Exception as error:
        category = str(error) if isinstance(error, InspectionError) else type(error).__name__
        result = {"schema_version": 1, "success": False, "category": category, "read_only": True,
                  "authenticated_download_verified": False}
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(json.dumps(result, indent=2) + "\n")
    print("Market Views live inspection: " + ("passed" if result["success"] else "failed"))
    return 0 if result["success"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
