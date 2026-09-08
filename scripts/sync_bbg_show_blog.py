#!/usr/bin/env python3
"""Archive published bilingual BBG highlight scripts without importing media.

Reads Git objects (never the source working tree) or the public GitHub API.
Deleted rendered snapshots are recovered from bounded history. Only the public
article contract is retained; prompts, local paths and editorial metadata are
discarded. Network or Git failures stop the sync without changing transport.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import math
import os
import re
import subprocess
import sys
import tempfile
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from datetime import date, datetime, timedelta, timezone
from pathlib import Path, PurePosixPath
from typing import Any
from urllib.parse import parse_qsl, quote, urlencode, urlsplit, urlunsplit
from urllib.request import Request, urlopen


ARCHIVE_SCHEMA = 1
DEFAULT_GITHUB_REPO = "yt-feng/bbg-show"
SOURCE_HOSTS = {"bloomberg.com", "youtube.com", "youtu.be", "ark-invest.com", "arkinvest.com"}
PLAN_PATH = re.compile(r"^rendered-clips/(?:(top-videos|ark-invest)/)?(\d{4}-\d{2}-\d{2})/(?:[^/]+/)*highlight_plan\.json$")


class ImportErrorDetail(ValueError):
    pass


class SourceReadError(ImportErrorDetail):
    """A Git/network read failure must stop, even when invalid clips are skipped."""


def clean_text(value: Any, limit: int = 12000) -> str:
    if not isinstance(value, str):
        return ""
    return re.sub(r"[\x00-\x08\x0b\x0c\x0e-\x1f\x7f]", "", value).strip()[:limit]


def source_url(value: Any) -> str:
    try:
        parsed = urlsplit(clean_text(value, 2000))
        host = (parsed.hostname or "").lower()
        if (parsed.scheme != "https" or parsed.username or parsed.password
                or parsed.port not in (None, 443)
                or not any(host == allowed or host.endswith("." + allowed) for allowed in SOURCE_HOSTS)):
            raise ValueError
        # Retain video identifiers, never arbitrary tracking or access tokens.
        query = urlencode([(key, val) for key, val in parse_qsl(parsed.query)
                           if key in {"v", "t", "start"}]) if host.endswith("youtube.com") or host == "youtu.be" else ""
        return urlunsplit(("https", host, parsed.path or "/", query, ""))
    except ValueError as error:
        raise ImportErrorDetail("source_url must identify an allowed public video source") from error


def timestamp(value: Any) -> float:
    if isinstance(value, bool) or not isinstance(value, (int, float)) or not math.isfinite(value):
        raise ImportErrorDetail("clip and segment times must be finite numbers")
    if not 0 <= value <= 7 * 24 * 60 * 60:
        raise ImportErrorDetail("clip and segment times are outside the supported range")
    return round(float(value), 3)


def plan_metadata(path: str) -> tuple[str, date] | None:
    matched = PLAN_PATH.fullmatch(path)
    if not matched:
        return None
    try:
        return matched.group(1) or "shows", date.fromisoformat(matched.group(2))
    except ValueError:
        return None


def clip_article(clip: dict[str, Any], plan: dict[str, Any], show: dict[str, Any], path: str) -> dict[str, Any]:
    metadata = plan_metadata(path)
    if not metadata:
        raise ImportErrorDetail("unexpected published highlight path")
    category, published = metadata
    title = clean_text(clip.get("title"), 300)
    speaker = clean_text(clip.get("speaker") or plan.get("speaker"), 200)
    if not title:
        raise ImportErrorDetail("clip title is missing")
    origin = source_url(clip.get("source_url") or plan.get("source_url") or show.get("SHOW_URL"))
    start, end = timestamp(clip.get("start")), timestamp(clip.get("end"))
    if end <= start:
        raise ImportErrorDetail("clip end must follow start")
    subtitles = clip.get("subtitles")
    if not isinstance(subtitles, list) or not subtitles:
        raise ImportErrorDetail("clip has no bilingual subtitles")
    segments = []
    for subtitle in subtitles:
        if not isinstance(subtitle, dict):
            raise ImportErrorDetail("subtitle must be an object")
        en = clean_text(subtitle.get("en"))
        zh = clean_text(subtitle.get("zh_filtered")) or clean_text(subtitle.get("zh"))
        if not en or not zh:
            raise ImportErrorDetail("subtitle is missing one of its two languages")
        segment_start, segment_end = timestamp(subtitle.get("start")), timestamp(subtitle.get("end"))
        if segment_end <= segment_start:
            raise ImportErrorDetail("subtitle end must follow start")
        # Source plans use absolute video timestamps. Small rounding drift is
        # accepted; a relative-time plan cannot silently become a false quote.
        if segment_start < start - 0.1 or segment_end > end + 0.1:
            raise ImportErrorDetail("subtitle timestamps are outside the clip")
        if segments and segment_start < segments[-1]["start"]:
            raise ImportErrorDetail("subtitles are not chronologically ordered")
        segments.append({"start": segment_start, "end": segment_end, "en": en, "zh": zh})
    identity = json.dumps([category, origin, start, end], ensure_ascii=False, separators=(",", ":"))
    article_id = hashlib.sha256(identity.encode()).hexdigest()
    return {
        "schema_version": ARCHIVE_SCHEMA,
        "id": article_id,
        "slug": f"bbg-{published.strftime('%Y%m%d')}-{article_id[:16]}",
        "date": published.isoformat(), "title": title, "speaker": speaker,
        "category": category, "source_url": origin, "start": start, "end": end,
        "segments": segments,
    }


class GitReader:
    def __init__(self, repo: Path):
        self.repo = repo

    def git(self, *args: str) -> bytes:
        try:
            completed = subprocess.run(["git", "-C", str(self.repo), *args], capture_output=True, timeout=60)
        except subprocess.TimeoutExpired as error:
            raise SourceReadError("Git source read timed out; sync stopped") from error
        if completed.returncode:
            # Do not repeat a private remote address or credential-bearing Git
            # error into an artifact/log, and never attempt a transport bypass.
            raise SourceReadError("Git source read failed; sync stopped")
        return completed.stdout

    def revisions(self, ref: str, since: date) -> list[str]:
        head = self.git("rev-parse", "--verify", ref + "^{commit}").decode().strip()
        history = self.git("log", head, f"--since={since.isoformat()}T00:00:00+08:00", "--format=%H", "--", "rendered-clips").decode().splitlines()
        if len(history) > 250:
            raise ImportErrorDetail("history exceeds 250 revisions; select a shorter date window")
        return list(dict.fromkeys([head, *history]))

    def plans(self, ref: str) -> dict[str, str]:
        rows = self.git("ls-tree", "-rz", ref, "--", "rendered-clips").split(b"\0")
        found = {}
        for raw in rows:
            if not raw:
                continue
            meta, path = raw.split(b"\t", 1)
            decoded = path.decode("utf-8")
            if plan_metadata(decoded):
                found[decoded] = meta.decode().split()[2]
        return found

    def all_plan_sources(self, ref: str) -> tuple[list[tuple[str, str]], int]:
        """Resolve each published path's latest committed version, without media."""
        head = self.git("rev-parse", "--verify", ref + "^{commit}").decode().strip()
        history = self.git(
            "log", head, "--format=COMMIT:%H", "--name-only", "--no-renames", "--diff-filter=AM",
            "--", "rendered-clips/**/highlight_plan.json",
        ).decode().splitlines()
        sources: dict[str, str] = {}
        revisions: set[str] = set()
        revision = ""
        for line in history:
            if line.startswith("COMMIT:"):
                revision = line[7:]
                revisions.add(revision)
            elif revision and plan_metadata(line):
                sources.setdefault(line, revision)
        return [(path, revision) for path, revision in sources.items()], len(revisions)

    def read_json(self, ref: str, path: str, optional: bool = False) -> dict[str, Any]:
        if optional:
            # An absent optional show.json is normal for top-videos. Listing
            # avoids conflating a missing object with a network/Git failure.
            existing = self.git("ls-tree", "--name-only", ref, "--", path).decode().strip()
            if not existing:
                return {}
        payload = json.loads(self.git("show", f"{ref}:{path}"))
        if not isinstance(payload, dict):
            raise ImportErrorDetail("published plan JSON must be an object")
        return payload


class GitHubReader:
    def __init__(self, repo: str, token: str = ""):
        if not re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repo):
            raise ImportErrorDetail("GitHub repository must be owner/name")
        self.repo, self.token = repo, token
        self.trees: dict[str, dict[str, Any]] = {}

    def request_json(self, path: str) -> Any:
        headers = {"Accept": "application/vnd.github+json", "User-Agent": "portal-bbg-script-archive/1.0"}
        if self.token:
            headers["Authorization"] = f"Bearer {self.token}"
        request = Request(f"https://api.github.com/repos/{self.repo}/{path}", headers=headers)
        try:
            with urlopen(request, timeout=45) as response:
                return json.load(response)
        except Exception as error:
            raise SourceReadError("GitHub source read failed; sync stopped without changing network or transport") from error

    def revisions(self, ref: str, since: date) -> list[str]:
        head = self.request_json(f"commits/{quote(ref, safe='')}")["sha"]
        history = []
        for page in range(1, 4):
            params = urlencode({"sha": head, "path": "rendered-clips", "since": since.isoformat() + "T00:00:00+08:00", "per_page": 100, "page": page})
            rows = self.request_json("commits?" + params)
            if not isinstance(rows, list):
                raise ImportErrorDetail("GitHub returned an invalid revision list")
            history.extend(row["sha"] for row in rows)
            if len(rows) < 100:
                return list(dict.fromkeys([head, *history]))
        raise ImportErrorDetail("history exceeds 300 revisions; select a shorter date window")

    def plans(self, ref: str) -> dict[str, str]:
        tree = self.request_json(f"git/trees/{ref}?recursive=1")
        if tree.get("truncated"):
            raise ImportErrorDetail("GitHub tree was truncated; use local Git mode")
        self.trees[ref] = tree
        return {row["path"]: row["sha"] for row in tree.get("tree", []) if row.get("type") == "blob" and plan_metadata(row["path"])}

    def read_json(self, ref: str, path: str, optional: bool = False) -> dict[str, Any]:
        import base64
        if optional:
            tree = self.trees.get(ref) or self.request_json(f"git/trees/{ref}?recursive=1")
            if tree.get("truncated"):
                raise ImportErrorDetail("GitHub tree was truncated")
            if not any(row.get("path") == path for row in tree.get("tree", [])):
                return {}
        item = self.request_json(f"contents/{quote(path, safe='/')}?ref={quote(ref, safe='')}")
        if item.get("encoding") != "base64" or not item.get("content"):
            raise ImportErrorDetail("GitHub returned an unsupported plan encoding")
        payload = json.loads(base64.b64decode(item["content"]))
        if not isinstance(payload, dict):
            raise ImportErrorDetail("published plan JSON must be an object")
        return payload


def sync_archive(reader: Any, ref: str, since: date, until: date, output: Path, *, skip_invalid: bool = False, all_history: bool = False, read_workers: int = 1) -> dict[str, Any]:
    if since > until:
        raise ImportErrorDetail("since must not be after until")
    sources: list[tuple[str, str]] = []
    if all_history:
        if not isinstance(reader, GitReader):
            raise ImportErrorDetail("all-history requires a local Git repository")
        sources, revisions_scanned = reader.all_plan_sources(ref)
    else:
        revisions = reader.revisions(ref, since)
        revisions_scanned = len(revisions)
        seen_paths: set[str] = set()
        for revision in revisions:
            for path in sorted(reader.plans(revision)):
                if path not in seen_paths:
                    seen_paths.add(path)
                    sources.append((path, revision))
    sources = [(path, revision) for path, revision in sources
               if (metadata := plan_metadata(path)) and since <= metadata[1] <= until]
    articles: dict[str, dict[str, Any]] = {}
    skipped, skipped_plans, plans_read, empty_plans, clip_records, duplicate_clips = 0, 0, 0, 0, 0, 0
    invalid_reasons: Counter[str] = Counter()
    def read_plan(source: tuple[str, str]) -> tuple[str, dict[str, Any], dict[str, Any], str]:
        path, revision = source
        try:
            plan = reader.read_json(revision, path)
            show = reader.read_json(revision, str(PurePosixPath(path).parent / "show.json"), optional=True) if plan_metadata(path)[0] == "shows" else {}
            return path, plan, show, ""
        except SourceReadError:
            raise
        except (ImportErrorDetail, json.JSONDecodeError, UnicodeDecodeError):
            if not skip_invalid:
                raise ImportErrorDetail("published plan is not valid JSON")
            return path, {}, {}, "invalid_plan_json"
    # Latest snapshot wins for an existing path. Older snapshots restore paths
    # deleted by cleanup without resurrecting outdated drafts of the same plan.
    # Read only a small batch at a time. A source read failure stops before any
    # further batch is submitted; --skip-invalid never masks a network failure.
    workers = max(1, min(8, read_workers))
    with ThreadPoolExecutor(max_workers=workers) as pool:
        for offset in range(0, len(sources), workers):
            batch = list(pool.map(read_plan, sources[offset:offset + workers]))
            for path, plan, show, invalid_plan in batch:
                metadata = plan_metadata(path)
                if invalid_plan:
                    skipped_plans += 1
                    invalid_reasons[invalid_plan] += 1
                    continue
                clips = plan.get("clips")
                if not isinstance(clips, list):
                    if skip_invalid:
                        skipped_plans += 1
                        invalid_reasons["missing_clips_array"] += 1
                        continue
                    raise ImportErrorDetail("published plan has no clips array")
                plans_read += 1
                empty_plans += int(not clips)
                for clip_index, clip in enumerate(clips):
                    clip_records += 1
                    try:
                        if not isinstance(clip, dict):
                            raise ImportErrorDetail("clip must be an object")
                        article = clip_article(clip, plan, show, path)
                    except ImportErrorDetail as error:
                        if skip_invalid:
                            skipped += 1
                            invalid_reasons[str(error)] += 1
                            continue
                        raise ImportErrorDetail(f"invalid bilingual clip {metadata[1]} #{clip_index + 1}: {error}") from error
                    duplicate_clips += int(article["id"] in articles)
                    articles.setdefault(article["id"], article)
    if not articles:
        raise ImportErrorDetail(f"no valid bilingual clips in the selected date window (skipped {skipped} clips, {skipped_plans} plans)")
    # Validation and all remote reads finish before existing local archives are
    # touched. Atomic replace prevents an interrupted write from corrupting JSON.
    added, updated, unchanged = 0, 0, 0
    prepared: list[tuple[Path, str, bool]] = []
    for article_id, article in sorted(articles.items()):
        destination = output / f"{article_id}.json"
        previous_body = ""
        if destination.exists():
            previous_body = destination.read_text(encoding="utf-8")
            previous = json.loads(previous_body)
            # Re-publication of the same clip can update its title/translation
            # without breaking its original archive permalink.
            try:
                if not isinstance(previous, dict) or previous.get("id") != article_id:
                    raise ValueError
                original_date = date.fromisoformat(previous["date"])
                article["date"] = original_date.isoformat()
                article["slug"] = f"bbg-{original_date.strftime('%Y%m%d')}-{article_id[:16]}"
            except (KeyError, TypeError, ValueError) as error:
                raise ImportErrorDetail("existing archive has an invalid identity or publication date") from error
        body = json.dumps(article, ensure_ascii=False, indent=2) + "\n"
        if destination.exists() and previous_body == body:
            unchanged += 1
            continue
        prepared.append((destination, body, destination.exists()))
    output.mkdir(parents=True, exist_ok=True)
    for destination, body, existed in prepared:
        descriptor, temp_name = tempfile.mkstemp(prefix=".bbg-", suffix=".tmp", dir=output)
        try:
            with os.fdopen(descriptor, "w", encoding="utf-8") as stream:
                stream.write(body)
            os.replace(temp_name, destination)
        finally:
            Path(temp_name).unlink(missing_ok=True)
        updated += int(existed)
        added += int(not existed)
    return {
        "schema_version": ARCHIVE_SCHEMA, "since": since.isoformat(), "until": until.isoformat(),
        "all_history": all_history, "revisions_scanned": revisions_scanned,
        "plans_considered": len(sources), "plans_read": plans_read,
        "empty_plans": empty_plans, "clip_records": clip_records, "duplicate_clips": duplicate_clips,
        "articles": len(articles), "segments": sum(len(row["segments"]) for row in articles.values()),
        "added": added, "updated": updated, "unchanged": unchanged, "skipped_invalid_clips": skipped,
        "skipped_invalid_plans": skipped_plans, "invalid_reasons": dict(sorted(invalid_reasons.items())),
        "dates": sorted({row["date"] for row in articles.values()}),
        "categories": {category: sum(row["category"] == category for row in articles.values()) for category in ("shows", "top-videos", "ark-invest")},
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", type=Path, help="read committed objects in this local Git repository")
    parser.add_argument("--github-repo", default=DEFAULT_GITHUB_REPO)
    parser.add_argument("--ref", default="main")
    parser.add_argument("--history-days", type=int, default=8)
    parser.add_argument("--all-history", action="store_true", help="recover all locally available committed highlight scripts")
    parser.add_argument("--read-workers", type=int, default=1, help="bounded concurrent JSON reads (1-8)")
    parser.add_argument("--since", type=date.fromisoformat)
    parser.add_argument("--until", type=date.fromisoformat)
    parser.add_argument("--output-dir", type=Path, default=Path("portal_suite/data/bbg_show_archive"))
    parser.add_argument("--skip-invalid", action="store_true", help="explicitly skip malformed clips and report their count")
    args = parser.parse_args()
    today = datetime.now(timezone(timedelta(hours=8))).date()
    until = args.until or today
    if not 1 <= args.history_days <= 63:
        parser.error("history-days must be from 1 through 63")
    if args.all_history and not args.repo:
        parser.error("all-history requires --repo")
    if not 1 <= args.read_workers <= 8:
        parser.error("read-workers must be from 1 through 8")
    since = args.since or (date(2000, 1, 1) if args.all_history else until - timedelta(days=args.history_days - 1))
    reader = GitReader(args.repo) if args.repo else GitHubReader(args.github_repo, os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN") or "")
    try:
        summary = sync_archive(reader, args.ref, since, until, args.output_dir, skip_invalid=args.skip_invalid, all_history=args.all_history, read_workers=args.read_workers)
    except (ImportErrorDetail, json.JSONDecodeError) as error:
        print(f"bbg-script-sync: {error}", file=sys.stderr)
        return 1
    print(json.dumps(summary, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
