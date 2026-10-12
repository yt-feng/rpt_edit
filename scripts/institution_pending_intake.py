"""Durable, bounded retries for IMF reports observed inside the intake window.

This is source-discovery state, not proof of a download or downstream handoff.
Keep successful fetches here until the ordinary seen-state commit is durable.
"""
from __future__ import annotations

import copy
from datetime import datetime, timedelta, timezone
import json
from pathlib import Path
from urllib.parse import urlsplit


ITEM_FIELDS = {"title", "source_url", "guid", "date", "pdf_candidates", "scrape_url", "coveo_unique_id"}
MAX_ITEMS = 2000


def _date(value):
    if not isinstance(value, str):
        raise ValueError("Invalid IMF intake date")
    result = datetime.fromisoformat(value.replace("Z", "+00:00"))
    if result.tzinfo is None:
        raise ValueError("IMF intake dates must include a timezone")
    return result


def _official_url(value, *, pdf=False):
    if not isinstance(value, str) or len(value) > 4096:
        return False
    try:
        parsed = urlsplit(value)
        path = parsed.path.lower()
        allowed_path = ((path.startswith("/-/media/files/publications/") or path.startswith("/external/pubs/"))
                        and path.endswith((".pdf", ".ashx"))) if pdf else path.startswith("/en/publications/")
        return (parsed.scheme == "https" and parsed.hostname == "www.imf.org"
                and not parsed.username and not parsed.password and parsed.port in (None, 443)
                and not parsed.fragment and "\\" not in value and "%" not in path
                and "/../" not in path and "/./" not in path and allowed_path)
    except ValueError:
        return False


def validate_item(item):
    if (not isinstance(item, dict) or set(item) != ITEM_FIELDS
            or not all(isinstance(item[key], str) and len(item[key]) <= 8192
                       for key in ITEM_FIELDS - {"pdf_candidates"})
            or not item["guid"] or not (_official_url(item["source_url"]) or _official_url(item["source_url"], pdf=True))
            or item["scrape_url"] not in ("", item["source_url"])
            or not isinstance(item["pdf_candidates"], list) or len(item["pdf_candidates"]) > 10
            or not all(_official_url(url, pdf=True) for url in item["pdf_candidates"])):
        raise ValueError("Invalid IMF pending source identity")
    _date(item["date"])


class PendingIntake:
    def __init__(self, path: Path, seen: dict, *, now: datetime, retry_limit: int = 10):
        if not 1 <= retry_limit <= 100:
            raise ValueError("IMF retry limit must be between 1 and 100")
        self.path, self.now, self.retry_limit = path, now, retry_limit
        self.items = {}
        if path.exists():
            if path.is_symlink() or path.stat().st_size > 16 * 1024 * 1024:
                raise ValueError("IMF intake checkpoint exceeds bound")
            data = json.loads(path.read_text())
            if (not isinstance(data, dict) or set(data) != {"schema", "institution", "items"}
                    or type(data["schema"]) is not int or data["schema"] != 1
                    or data["institution"] != "imf" or not isinstance(data["items"], dict)
                    or len(data["items"]) > MAX_ITEMS):
                raise ValueError("Invalid IMF intake checkpoint")
            for key, row in data["items"].items():
                if not isinstance(row, dict) or set(row) != {"item", "admitted_at", "since_days", "last_attempted_at", "attempts"}:
                    raise ValueError("Invalid IMF intake record")
                validate_item(row["item"])
                admitted, attempted = _date(row["admitted_at"]), _date(row["last_attempted_at"])
                published = _date(row["item"]["date"])
                if (key != "imf:" + row["item"]["guid"] or type(row["since_days"]) is not int
                        or not 0 <= row["since_days"] <= 3660 or type(row["attempts"]) is not int
                        or not 0 <= row["attempts"] <= 1_000_000
                        or not admitted <= attempted <= now
                        or not admitted - timedelta(days=row["since_days"]) <= published <= admitted):
                    raise ValueError("Invalid IMF intake admission evidence")
                # Only the durable, successful seen state retires a source.
                if seen.get(key, {}).get("status") not in {"downloaded", "duplicate_pdf"}:
                    self.items[key] = row
        self.initial_keys = set(self.items)
        self.attempted = set()
        self.resolved = set()

    def merge(self, discovered):
        ordered = sorted(self.items, key=lambda key: (self.items[key]["last_attempted_at"], key))
        selected = ordered[:self.retry_limit]
        # Preserve original URL/date/title even if feed metadata changes, and
        # don't accidentally retry a deferred entry again through today's feed.
        fresh = [item for item in discovered if "imf:" + item["guid"] not in self.items]
        self.item_count = len(self.items) + len(fresh)
        return [copy.deepcopy(self.items[key]["item"]) for key in selected] + fresh

    def admit(self, item, since_days):
        validate_item(item)
        key = "imf:" + item["guid"]
        if key not in self.items:
            if len(self.items) >= MAX_ITEMS:
                raise ValueError("IMF pending intake is full; no source was discarded")
            published = _date(item["date"])
            if not self.now - timedelta(days=since_days) <= published <= self.now:
                raise ValueError("Cannot admit an unobserved historical IMF source")
            self.items[key] = dict(item=copy.deepcopy(item), admitted_at=self.now.isoformat(),
                                   since_days=since_days, last_attempted_at=self.now.isoformat(), attempts=0)
        row = self.items[key]
        row["last_attempted_at"] = self.now.isoformat()
        row["attempts"] += 1
        self.attempted.add(key)
        # Persist discovery before any fallible download or downstream work.
        self.save()

    def observe_hold(self, key):
        self.resolved.add(key)
        if key in self.items:
            # The source bytes already have an exact durable dependency hold.
            # Rotate its queue position without claiming a fresh download.
            self.items[key]["last_attempted_at"] = self.now.isoformat()
            self.save()

    @property
    def deferred_count(self):
        return len(self.initial_keys - self.attempted - self.resolved)

    def save(self):
        self.path.parent.mkdir(parents=True, exist_ok=True)
        temporary = self.path.with_suffix(".tmp")
        temporary.write_text(json.dumps(dict(schema=1, institution="imf", items=self.items),
                                        ensure_ascii=False, indent=2) + "\n")
        temporary.replace(self.path)


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="Validate the IMF pending intake checkpoint without mutating it")
    parser.add_argument("path", type=Path)
    args = parser.parse_args()
    if not args.path.is_file():
        raise SystemExit("IMF intake checkpoint is missing")
    PendingIntake(args.path, {}, now=datetime.now(timezone.utc))
