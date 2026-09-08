#!/usr/bin/env python3
"""Capture bounded GDELT GAL descriptions into a private seven-day snapshot.

Source schema: https://blog.gdeltproject.org/announcing-the-gdelt-article-list-rss-feed/
GAL date can be discovery time; it is never represented as published_at.
No article pages or images are fetched, and no news text is printed to logs.
"""
from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor, as_completed
from datetime import datetime, timedelta, timezone
import hashlib
import html
import http.client
import ipaddress
import json
import os
import re
import time
from typing import Any, Iterable
from urllib.parse import parse_qsl, urlencode, urlsplit, urlunsplit
import zlib

HOST = "data.gdeltproject.org"
KEY = "_research-news/v1/snapshot.json"
MAX_COMPRESSED = 3 * 1024 * 1024
MAX_DECOMPRESSED = 16 * 1024 * 1024
MAX_SNAPSHOT_BYTES = 2 * 1024 * 1024
MAX_ITEMS = 1800
MAX_WORKERS = 6
REQUEST_SECONDS = 12
WINDOW_DAYS = 7
TOPICS = re.compile(
    r"\b(?:econom(?:y|ic|ics)|inflation|interest rates?|federal reserve|central bank|tariffs?|trade|"
    r"financ\w*|banks?|bonds?|treasur\w*|stocks?|equities|earnings|investment|markets?|"
    r"ai|artificial intelligence|semiconductors?|chips?|data cent(?:er|re)s?|technology|software|"
    r"energy|electricity|power grid|oil|natural gas|lng|solar|batter(?:y|ies)|gold|copper)\b"
    r"|经济|經濟|金融|通胀|通脹|利率|央行|美联储|美聯儲|关税|關稅|贸易|貿易|债券|債券|"
    r"股票|股市|财报|財報|投资|投資|人工智能|人工智慧|半导体|半導體|芯片|晶片|数据中心|數據中心|"
    r"科技|能源|电力|電力|石油|天然气|天然氣|光伏|电池|電池|黄金|黃金", re.I,
)
PROMO = re.compile(r"\b(?:advertorial|sponsored content|promo code|coupon|register now|buy tickets|free shipping|webinar registration)\b|优惠券|優惠券|立即购买|立即購買|限时抢购|限時搶購|付费推广|付費推廣", re.I)


class SnapshotError(RuntimeError):
    """Messages are fixed codes suitable for public workflow logs."""


def utc(value: Any = None) -> datetime:
    if value is None:
        return datetime.now(timezone.utc)
    if isinstance(value, datetime):
        parsed = value
    else:
        parsed = datetime.fromisoformat(str(value).replace("Z", "+00:00"))
    return parsed.replace(tzinfo=timezone.utc) if parsed.tzinfo is None else parsed.astimezone(timezone.utc)


def iso(value: datetime) -> str:
    return value.astimezone(timezone.utc).isoformat(timespec="seconds").replace("+00:00", "Z")


def clean_text(value: Any, limit: int) -> str:
    text = str(value or "")[:16000]
    for _ in range(2):
        text = html.unescape(text)
    text = re.sub(r"(?is)<(script|style|iframe|object)\b[^>]*>.*?</\1\s*>", " ", text)
    text = re.sub(r"(?s)<!--.*?-->|<[^>]*>", " ", text)
    text = re.sub(r"[<>\x00-\x1f\x7f\u200b-\u200f\u202a-\u202e\u2060-\u206f\ufeff]", " ", text)
    return " ".join(text.split())[:limit]


def canonical_url(value: Any) -> str:
    raw = str(value or "").strip()
    if not raw or len(raw) > 2048 or re.search(r"[\s\\]", raw):
        return ""
    try:
        parsed = urlsplit(raw)
        host = (parsed.hostname or "").lower().encode("idna").decode("ascii")
        if parsed.scheme != "https" or parsed.username or parsed.password or parsed.port not in (None, 443):
            return ""
        if not re.fullmatch(r"(?:[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?\.)+[a-z][a-z0-9-]{1,62}", host):
            return ""
        if host.rsplit(".", 1)[-1] in {"localhost", "local", "internal", "lan", "home", "test", "invalid", "example", "onion"}:
            return ""
        try:
            ipaddress.ip_address(host)
            return ""
        except ValueError:
            pass
        if parsed.path in ("", "/"):
            return ""
        query = [(key, val) for key, val in parse_qsl(parsed.query, keep_blank_values=True)
                 if not key.lower().startswith("utm_") and key.lower() not in {"fbclid", "gclid", "msclkid"}]
        return urlunsplit(("https", host, parsed.path, urlencode(query), ""))
    except (ValueError, UnicodeError):
        return ""


def normalize_record(raw: Any, now: datetime) -> dict[str, Any] | None:
    if not isinstance(raw, dict):
        return None
    language = str(raw.get("lang", "")).lower()
    if language not in {"en", "zh", "zh-hans", "zh-hant"}:
        return None
    title = clean_text(raw.get("title"), 420)
    summary = clean_text(raw.get("desc"), 700)
    url = canonical_url(raw.get("url"))
    if not title or not url or len(summary) < 80 or sum(char.isalnum() for char in summary) < 60:
        return None
    normalized = lambda text: re.sub(r"\W+", "", text.casefold())
    title_text, summary_text = normalized(title), normalized(summary)
    title_only = bool(title_text) and not summary_text.replace(title_text, "")
    if title_only or PROMO.search(title + " " + summary) or not TOPICS.search(title + " " + summary):
        return None
    try:
        observed = utc(raw.get("date"))
    except (ValueError, TypeError):
        return None
    if not raw.get("date") or observed < now - timedelta(days=WINDOW_DAYS) or observed > now + timedelta(minutes=5):
        return None
    outlet = clean_text(raw.get("outletName"), 160) or urlsplit(url).hostname
    return {
        "id": "news:" + hashlib.sha256(url.encode("utf-8")).hexdigest(),
        "title": title, "source_url": url, "institution": outlet, "outlet": outlet,
        "observed_at": iso(observed), "published_at": "", "language": "en" if language == "en" else "zh",
        "summary": summary, "evidence_kind": "news_description", "provider": "gdelt-gal",
    }


def decode_gal(chunks: Iterable[bytes], now: datetime) -> list[dict[str, Any]]:
    """Bound compressed/decompressed bytes and JSONL line size while streaming."""
    inflater = zlib.decompressobj(16 + zlib.MAX_WBITS)
    compressed = decompressed = 0
    pending = b""
    dropping = False
    rows: list[dict[str, Any]] = []

    def consume(data: bytes) -> None:
        nonlocal pending, dropping, decompressed
        decompressed += len(data)
        if decompressed > MAX_DECOMPRESSED:
            raise SnapshotError("decompressed_limit")
        for index, part in enumerate(data.split(b"\n")):
            if index:
                if pending and not dropping:
                    try:
                        item = normalize_record(json.loads(pending.decode("utf-8")), now)
                        if item:
                            rows.append(item)
                    except (ValueError, UnicodeError):
                        pass
                pending = b""
                dropping = False
            if not dropping:
                pending += part
                if len(pending) > 65536:
                    pending = b""
                    dropping = True

    try:
        for chunk in chunks:
            compressed += len(chunk)
            if compressed > MAX_COMPRESSED:
                raise SnapshotError("compressed_limit")
            remaining = chunk
            while remaining:
                consume(inflater.decompress(remaining, 65536))
                remaining = inflater.unconsumed_tail
        consume(b"\n")
        if not inflater.eof or inflater.unused_data:
            raise SnapshotError("invalid_gzip")
    except zlib.error as error:
        raise SnapshotError("invalid_gzip") from error
    return retain_items(rows)


class _SocketResponse(http.client.HTTPResponse):
    def __init__(self, sock: Any, *args: Any, **kwargs: Any):
        self.transport_socket = sock
        super().__init__(sock, *args, **kwargs)


def fetch_minute(stamp: datetime, now: datetime) -> list[dict[str, Any]]:
    path = f"/gdeltv3/gal/{stamp.strftime('%Y%m%d%H%M')}00.gal.json.gz"
    deadline = time.monotonic() + REQUEST_SECONDS
    connection = http.client.HTTPSConnection(HOST, timeout=REQUEST_SECONDS)
    connection.response_class = _SocketResponse
    try:
        connection.connect()
        connection.sock.settimeout(max(0.001, deadline - time.monotonic()))
        connection.request("GET", path, headers={"Accept": "application/gzip,application/octet-stream", "User-Agent": "PortalResearchSnapshot/1.0"})
        connection.sock.settimeout(max(0.001, deadline - time.monotonic()))
        response = connection.getresponse()
        if response.status == 404:
            return []
        if response.status != 200:
            raise SnapshotError("upstream_status")  # Redirects are not followed.
        if int(response.getheader("Content-Length", "0")) > MAX_COMPRESSED:
            raise SnapshotError("compressed_limit")

        def chunks() -> Iterable[bytes]:
            while True:
                remaining = deadline - time.monotonic()
                if remaining <= 0:
                    raise SnapshotError("upstream_timeout")
                response.transport_socket.settimeout(remaining)
                block = response.read1(65536)
                if not block:
                    break
                yield block

        return decode_gal(chunks(), now)
    except SnapshotError:
        raise
    except (OSError, ValueError, http.client.HTTPException) as error:
        raise SnapshotError("upstream_unavailable") from error
    finally:
        connection.close()


def retain_items(rows: Iterable[dict[str, Any]]) -> list[dict[str, Any]]:
    by_url: dict[str, dict[str, Any]] = {}
    for row in rows:
        previous = by_url.get(row["source_url"])
        if previous is None or (row["observed_at"], len(row["summary"])) > (previous["observed_at"], len(previous["summary"])):
            by_url[row["source_url"]] = row
    ranked = sorted(by_url.values(), key=lambda row: (row["observed_at"], len(set(TOPICS.findall(row["title"] + " " + row["summary"]))), row["id"]), reverse=True)
    return ranked[:MAX_ITEMS]


def collect_recent(now: datetime, lookback_minutes: int = 75, fetcher: Any = fetch_minute) -> tuple[list[dict[str, Any]], dict[str, int]]:
    if not 1 <= lookback_minutes <= 75:
        raise SnapshotError("invalid_lookback")
    end = now.replace(second=0, microsecond=0)
    minutes = [end - timedelta(minutes=offset) for offset in range(1, lookback_minutes + 1)]
    rows: list[dict[str, Any]] = []
    failed = completed = 0
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = [pool.submit(fetcher, minute, now) for minute in minutes]
        for future in as_completed(futures):
            try:
                rows = retain_items([*rows, *future.result()])
                completed += 1
            except Exception:
                failed += 1
    return rows, {"requested_files": len(minutes), "completed_files": completed, "failed_files": failed}


def read_r2_snapshot(client: Any, bucket: str) -> dict[str, Any]:
    try:
        obj = client.get_object(Bucket=bucket, Key=KEY)
    except Exception as error:
        if str(getattr(error, "response", {}).get("Error", {}).get("Code", "")) in {"NoSuchKey", "404", "NotFound"}:
            return {"schema_version": 1, "items": []}
        raise SnapshotError("snapshot_read_failed") from error
    body = obj["Body"]
    try:
        content = body.read(MAX_SNAPSHOT_BYTES + 1)
    finally:
        body.close()
    if len(content) > MAX_SNAPSHOT_BYTES:
        raise SnapshotError("snapshot_size_invalid")
    try:
        payload = json.loads(content)
        if not isinstance(payload, dict) or payload.get("schema_version") != 1 or not isinstance(payload.get("items"), list) or len(payload["items"]) > MAX_ITEMS:
            raise ValueError("schema")
        return payload
    except (ValueError, TypeError) as error:
        raise SnapshotError("snapshot_schema_invalid") from error


def make_snapshot(previous: dict[str, Any], new_items: list[dict[str, Any]], now: datetime) -> tuple[bytes, int]:
    merged = []
    for item in [*previous.get("items", []), *new_items]:
        normalized = normalize_record({"title": item.get("title"), "url": item.get("source_url"), "desc": item.get("summary"), "date": item.get("observed_at"), "lang": item.get("language"), "outletName": item.get("outlet") or item.get("institution")}, now)
        if normalized:
            merged.append(normalized)
    payload = {"schema_version": 1, "updated_at": iso(now), "window_days": WINDOW_DAYS, "items": []}
    size = len(json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8"))
    for item in retain_items(merged):
        added = len(json.dumps(item, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")) + bool(payload["items"])
        if size + added > MAX_SNAPSHOT_BYTES:
            break
        payload["items"].append(item)
        size += added
    encoded = json.dumps(payload, ensure_ascii=False, separators=(",", ":"), sort_keys=True).encode("utf-8")
    return encoded, len(payload["items"])


def publish_snapshot(client: Any, bucket: str, new_items: list[dict[str, Any]], now: datetime) -> dict[str, Any]:
    if not new_items:
        return {"status": "skipped", "reason": "no_new_data", "item_count": 0, "domain_count": 0, "updated_at": iso(now)}
    previous = read_r2_snapshot(client, bucket)
    encoded, count = make_snapshot(previous, new_items, now)
    if not count:
        raise SnapshotError("empty_snapshot_refused")
    client.put_object(Bucket=bucket, Key=KEY, Body=encoded, ContentType="application/json; charset=utf-8", CacheControl="private, max-age=0", Metadata={"sha256": hashlib.sha256(encoded).hexdigest()})
    body = client.get_object(Bucket=bucket, Key=KEY)["Body"]
    try:
        committed = body.read(MAX_SNAPSHOT_BYTES + 1)
    finally:
        body.close()
    if committed != encoded:
        raise SnapshotError("snapshot_verify_failed")
    items = json.loads(encoded)["items"]
    return {"status": "published", "item_count": count, "domain_count": len({urlsplit(row["source_url"]).hostname for row in items}), "bytes": len(encoded), "updated_at": iso(now)}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--lookback-minutes", type=int, default=75)
    parser.add_argument("--publish", action="store_true")
    args = parser.parse_args(argv)
    now = utc()
    try:
        rows, stats = collect_recent(now, args.lookback_minutes)
        if args.publish and rows:
            from build_report_chat_index import build_r2_client
            summary = publish_snapshot(build_r2_client(), os.environ["R2_BUCKET"], rows, now)
        else:
            summary = {"status": "ready" if rows else "skipped", "reason": "preview" if rows else "no_new_data", "item_count": len(rows), "domain_count": len({urlsplit(row["source_url"]).hostname for row in rows}), "updated_at": iso(now)}
        summary.update(stats)
        print(json.dumps(summary, ensure_ascii=True, sort_keys=True))
        if os.environ.get("GITHUB_STEP_SUMMARY"):
            with open(os.environ["GITHUB_STEP_SUMMARY"], "a", encoding="utf-8") as output:
                output.write("\nResearch news snapshot\n\n" + "\n".join(f"- {key}: {value}" for key, value in summary.items()) + "\n")
        return 1 if stats["failed_files"] == stats["requested_files"] else 0
    except Exception as error:
        print(json.dumps({"status": "failed", "reason": str(error) if isinstance(error, SnapshotError) else "snapshot_failed"}))
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
