"""Read one owner's selected account and recent event outcomes; never write R2."""
import hashlib
import json
import os
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.parse import quote, unquote, urlencode, urlsplit
from urllib.request import Request, urlopen


def selected_fields(row, fields):
    return {key: row[key] for key in fields if key in (row or {})}


def database_rows(table, params):
    base = os.environ["SUPABASE_URL"].rstrip("/")
    if urlsplit(base).scheme != "https" or urlsplit(base).username:
        raise ValueError("invalid database origin")
    key = os.environ["SUPABASE_SERVICE_ROLE_KEY"]
    request = Request(base + "/rest/v1/" + table + "?" + urlencode(params),
                      headers={"apikey": key, "Authorization": "Bearer " + key})
    with urlopen(request, timeout=20) as response:
        raw = response.read(2 * 1024 * 1024 + 1)
    if len(raw) > 2 * 1024 * 1024:
        raise ValueError("bounded database response exceeded")
    result = json.loads(raw)
    if not isinstance(result, list):
        raise ValueError("invalid database response")
    return result


def selected_database_users(wanted):
    selected = []
    for offset in range(0, 10000, 1000):
        rows = database_rows("site_users", {"select": "id,username,email", "order": "id.asc", "limit": "1000", "offset": str(offset)})
        selected.extend(row for row in rows if hashlib.sha256(str(row.get("username", "")).strip().lower().encode()).hexdigest() == wanted)
        if len(rows) < 1000:
            return selected
    raise ValueError("bounded account selection exceeded")


def main():
    import boto3
    from botocore.config import Config
    wanted = os.environ["MEMBER_USERNAME_SHA256"]
    if len(wanted) != 64 or any(c not in "0123456789abcdef" for c in wanted):
        raise ValueError("invalid selection")
    client = boto3.client("s3", endpoint_url=f'https://{os.environ["R2_ACCOUNT_ID"]}.r2.cloudflarestorage.com',
                          aws_access_key_id=os.environ["R2_ACCESS_KEY_ID"],
                          aws_secret_access_key=os.environ["R2_SECRET_ACCESS_KEY"], region_name="auto",
                          config=Config(signature_version="s3v4", retries={"max_attempts": 3, "mode": "adaptive"},
                                        connect_timeout=10, read_timeout=20))
    bucket = os.environ["R2_BUCKET"]

    def keys(prefix, maximum=10000):
        found = []
        for page in client.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix):
            found.extend(item["Key"] for item in page.get("Contents", []))
            if len(found) > maximum:
                raise ValueError("bounded listing exceeded")
        return found

    def read(key):
        try:
            response = client.get_object(Bucket=bucket, Key=key)
        except client.exceptions.ClientError as error:
            if error.response.get("Error", {}).get("Code") in {"NoSuchKey", "404"}:
                return None
            raise
        body = response["Body"]
        try:
            data = body.read(512 * 1024 + 1)
            if len(data) > 512 * 1024:
                raise ValueError("bounded object exceeded")
            return json.loads(data)
        finally:
            body.close()

    database = bool(os.environ.get("SUPABASE_URL") and os.environ.get("SUPABASE_SERVICE_ROLE_KEY"))
    prefix = "_account/users/username/"
    matched = selected_database_users(wanted) if database else [read(key) for key in keys(prefix)
        if hashlib.sha256(unquote(key[len(prefix):]).lower().encode()).hexdigest() == wanted]
    report = {"read_only": True, "matched_account_count": len(matched)}
    if len(matched) == 1:
        user = matched[0] or {}
        email, uid = str(user.get("email", "")), str(user.get("id", ""))
        if not email or not uid:
            raise ValueError("selected account identity incomplete")
        def account_key(*parts):
            return "_account/" + "/".join(quote(part, safe="~()*!.'-") for part in parts)
        access = read(account_key("access", email)) or {}
        entitlement = ((database_rows("user_entitlements", {"email": "eq." + email, "order": "updated_at.desc", "limit": "1"}) or [{}])[0]
                       if database else read(account_key("entitlements", email)) or {})
        states = [read(account_key("user-state", kind, value)) or {} for kind, value in [("email", email), ("id", uid)]]
        access_fields = ("status", "access_mode", "duration_value", "duration_unit", "starts_at", "current_period_end",
                         "expires_at", "lifetime", "download_limit", "download_count", "created_at", "updated_at", "revoked_at")
        report.update(account_disabled=bool(user.get("disabled")),
                      state_disabled=[bool(row.get("disabled")) for row in states],
                      access=selected_fields(access, access_fields), entitlement=selected_fields(entitlement, access_fields))
        now = datetime.now(timezone.utc)
        since = now - timedelta(hours=4)
        dates = {(now + timedelta(hours=8)).date().isoformat(), (since + timedelta(hours=8)).date().isoformat()}
        event_keys = []
        for day in sorted(dates):
            for key in keys(f"_analytics/events/{day}/", 30000):
                # Event keys begin with an ISO UTC timestamp with colon/dot replaced.
                if key.split("/")[-1][:19] >= since.strftime("%Y-%m-%dT%H-%M-%S"):
                    event_keys.append(key)
        event_keys = sorted(event_keys)[-2000:]
        outcomes = []
        with ThreadPoolExecutor(max_workers=4) as pool:
            for event in pool.map(read, event_keys):
                if not isinstance(event, dict):
                    continue
                identity = event.get("user") or {}
                if identity.get("id") != uid and identity.get("email") != email:
                    continue
                outcomes.append(selected_fields(event, ("ts", "type", "action", "status", "source", "report_id", "duration_ms")))
        report.update(scanned_recent_events=len(event_keys), event_scan_capped=len(event_keys) == 2000,
                      observed_events=outcomes, checked_at=now.isoformat())
    Path("member-diagnostic.json").write_text(json.dumps(report, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(report, ensure_ascii=False))


if __name__ == "__main__":
    try:
        main()
    except Exception:
        raise SystemExit("Read-only member diagnostic failed; private details omitted.") from None
