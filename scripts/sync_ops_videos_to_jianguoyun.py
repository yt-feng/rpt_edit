#!/usr/bin/env python3
"""Mirror Portal Suite operations videos from GitHub to Jianguoyun WebDAV."""

from __future__ import annotations

import argparse
import hashlib
import os
import re
import tempfile
import time
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, unquote, urlparse
from zoneinfo import ZoneInfo

import requests
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry


GITHUB_API = "https://api.github.com"
TIMEZONE = ZoneInfo("Asia/Shanghai")
DEFAULT_REMOTE_ROOT = "/我的坚果云/Portal Suite/Ops"
DATE_RE = re.compile(r"^20\d{2}-\d{2}-\d{2}$")
DAV = "{DAV:}"
UPLOAD_MAX_ATTEMPTS = 3
UPLOAD_RETRYABLE_STATUSES = frozenset({408, 429, 500, 502, 503, 504})
WEBDAV_ERROR_DETAIL_LIMIT = 300


@dataclass(frozen=True)
class VideoFile:
    repo: str
    path: str
    name: str
    size: int
    sha: str
    generated_date: str
    category: str
    download_url: str


def build_session(token: str = "") -> requests.Session:
    session = requests.Session()
    retry = Retry(
        total=4,
        connect=4,
        read=4,
        backoff_factor=1.0,
        status_forcelist=(429, 500, 502, 503, 504),
        allowed_methods=frozenset({"GET", "HEAD", "PROPFIND", "MKCOL", "DELETE"}),
    )
    session.mount("https://", HTTPAdapter(max_retries=retry))
    session.headers.update({"User-Agent": "portal-ops-video-mirror/1.0"})
    if token:
        session.headers.update(
            {
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json",
                "X-GitHub-Api-Version": "2022-11-28",
            }
        )
    return session


class GithubSource:
    def __init__(self, token: str):
        self.session = build_session(token)

    def contents(self, repo: str, path: str) -> list[dict]:
        encoded = quote(path.strip("/"), safe="/")
        response = self.session.get(
            f"{GITHUB_API}/repos/{repo}/contents/{encoded}", timeout=(15, 45)
        )
        if response.status_code == 404:
            return []
        response.raise_for_status()
        payload = response.json()
        return payload if isinstance(payload, list) else [payload]

    def walk_mp4(self, repo: str, root: str, max_depth: int = 4) -> list[dict]:
        files: list[dict] = []
        queue: list[tuple[str, int]] = [(root, 0)]
        while queue:
            current, depth = queue.pop(0)
            for item in self.contents(repo, current):
                item_type = str(item.get("type") or "")
                item_path = str(item.get("path") or "")
                if item_type == "file" and item_path.lower().endswith(".mp4"):
                    files.append(item)
                elif item_type == "dir" and depth < max_depth:
                    queue.append((item_path, depth + 1))
        return files

    def download(self, video: VideoFile, destination: Path) -> int:
        url = video.download_url
        headers: dict[str, str] = {}
        if not url:
            encoded = quote(video.path.strip("/"), safe="/")
            url = f"{GITHUB_API}/repos/{video.repo}/contents/{encoded}"
            headers["Accept"] = "application/vnd.github.raw+json"
        with self.session.get(url, headers=headers, stream=True, timeout=(20, 180)) as response:
            response.raise_for_status()
            written = 0
            with destination.open("wb") as handle:
                for chunk in response.iter_content(chunk_size=1024 * 1024):
                    if not chunk:
                        continue
                    handle.write(chunk)
                    written += len(chunk)
        return written


def video_from_item(item: dict, repo: str, generated_date: str, category: str) -> VideoFile:
    path = str(item.get("path") or "")
    return VideoFile(
        repo=repo,
        path=path,
        name=str(item.get("name") or path.rsplit("/", 1)[-1]),
        size=int(item.get("size") or 0),
        sha=str(item.get("sha") or ""),
        generated_date=generated_date,
        category=category,
        download_url=str(item.get("download_url") or ""),
    )


def parse_iso_date(value: str) -> date:
    return datetime.strptime(value, "%Y-%m-%d").date()


def target_dates(end_date: date, days: int) -> list[date]:
    count = max(1, days)
    return [end_date - timedelta(days=offset) for offset in reversed(range(count))]


def ordinary_bbg_generated_date(folder_name: str) -> date | None:
    exact = re.fullmatch(r"(20\d{2}-\d{2}-\d{2})", folder_name)
    if exact:
        return parse_iso_date(exact.group(1)) + timedelta(days=1)
    prefixed = re.match(r"^(20\d{2}-\d{2}-\d{2})(?:[-_].+)$", folder_name)
    return parse_iso_date(prefixed.group(1)) if prefixed else None


def dated_children(github: GithubSource, repo: str, root: str, wanted: set[str]) -> list[tuple[str, str]]:
    selected: list[tuple[str, str]] = []
    for item in github.contents(repo, root):
        if item.get("type") != "dir":
            continue
        name = str(item.get("name") or "")
        matched = re.match(r"^(20\d{2}-\d{2}-\d{2})", name)
        if matched and matched.group(1) in wanted:
            selected.append((str(item.get("path") or ""), matched.group(1)))
    return selected


def discover_bbg(github: GithubSource, wanted_dates: set[str]) -> list[VideoFile]:
    repo = "source/media-a"
    root = "rendered-clips"
    results: list[VideoFile] = []
    roots = github.contents(repo, root)

    for item in roots:
        if item.get("type") != "dir":
            continue
        name = str(item.get("name") or "")
        path = str(item.get("path") or "")
        if name == "top-videos":
            for selected_path, generated in dated_children(github, repo, path, wanted_dates):
                results.extend(
                    video_from_item(video, repo, generated, "BBG Top Videos")
                    for video in github.walk_mp4(repo, selected_path)
                )
            continue
        if name == "ark-invest":
            for selected_path, generated in dated_children(github, repo, path, wanted_dates):
                results.extend(
                    video_from_item(video, repo, generated, "ARK Invest")
                    for video in github.walk_mp4(repo, selected_path)
                )
            continue

        generated_date = ordinary_bbg_generated_date(name)
        if generated_date and generated_date.isoformat() in wanted_dates:
            generated = generated_date.isoformat()
            results.extend(
                video_from_item(video, repo, generated, "BBG Show")
                for video in github.walk_mp4(repo, path)
            )
            continue

        # Named buckets such as "weekend" can contain their own dated folders.
        for selected_path, generated in dated_children(github, repo, path, wanted_dates):
            results.extend(
                video_from_item(video, repo, generated, "BBG Show")
                for video in github.walk_mp4(repo, selected_path)
            )
    return results


def discover_portal_entertainment(github: GithubSource, dates: Iterable[date]) -> list[VideoFile]:
    repo = "source/media-b"
    results: list[VideoFile] = []
    for target in dates:
        generated = target.isoformat()
        root = f"outputs/portal_entertain/{generated}"
        results.extend(
            video_from_item(video, repo, generated, "Portal 娱乐")
            for video in github.walk_mp4(repo, root)
        )
    return results


def discover_report_videos(github: GithubSource, dates: Iterable[date]) -> list[VideoFile]:
    repo = "source/media-c"
    results: list[VideoFile] = []
    seen_paths: set[str] = set()
    for target in dates:
        generated = target.isoformat()
        folder_names = (target.strftime("%y%m%d"), target.strftime("%Y%m%d"))
        for folder in folder_names:
            root = f"videos/pdf_portal/{folder}"
            for video in github.walk_mp4(repo, root):
                path = str(video.get("path") or "")
                if path in seen_paths:
                    continue
                seen_paths.add(path)
                results.append(video_from_item(video, repo, generated, "报告视频"))
    return results


def discover_videos(github: GithubSource, dates: list[date]) -> list[VideoFile]:
    wanted = {value.isoformat() for value in dates}
    discovered = [
        *discover_bbg(github, wanted),
        *discover_portal_entertainment(github, dates),
        *discover_report_videos(github, dates),
    ]
    unique: dict[tuple[str, str], VideoFile] = {}
    for video in discovered:
        unique[(video.repo, video.path)] = video
    return sorted(
        unique.values(),
        key=lambda video: (video.generated_date, video.category, video.name),
    )


def filename_for_remote(video: VideoFile, duplicate: bool) -> str:
    cleaned = re.sub(r"[\\/:*?\"<>|\x00-\x1f]", "_", video.name).strip(" .") or "video.mp4"
    suffix = Path(cleaned).suffix or ".mp4"
    stem = cleaned[: -len(suffix)] if cleaned.endswith(suffix) else cleaned
    digest = (video.sha or hashlib.sha256(f"{video.repo}:{video.path}".encode()).hexdigest())[:8]
    if duplicate:
        stem = f"{stem}__{digest}"
    while len(f"{stem}{suffix}".encode("utf-8")) > 220 and stem:
        stem = stem[:-1]
    return f"{stem}{suffix}"


def assign_remote_names(videos: list[VideoFile]) -> dict[tuple[str, str], str]:
    counts: dict[tuple[str, str, str], int] = {}
    for video in videos:
        key = (video.generated_date, video.category, video.name.casefold())
        counts[key] = counts.get(key, 0) + 1
    return {
        (video.repo, video.path): filename_for_remote(
            video,
            counts[(video.generated_date, video.category, video.name.casefold())] > 1,
        )
        for video in videos
    }


class WebDavTarget:
    def __init__(self, base_url: str, username: str, password: str, root: str):
        self.base_url = base_url.rstrip("/") + "/"
        self.root_parts = [part for part in root.strip("/").split("/") if part]
        self.session = build_session()
        self.session.auth = (username, password)
        self._confirmed_collections: set[tuple[str, ...]] = set()

    def url(self, parts: Iterable[str]) -> str:
        return self.base_url + "/".join(quote(part, safe="") for part in parts)

    @staticmethod
    def _response_detail(response: requests.Response) -> str:
        details: list[str] = []
        retry_after = str(response.headers.get("Retry-After") or "").strip()
        if retry_after:
            details.append(f"retry-after={retry_after}")
        body = re.sub(r"\s+", " ", response.text or "").strip()
        if body:
            if len(body) > WEBDAV_ERROR_DETAIL_LIMIT:
                body = body[: WEBDAV_ERROR_DETAIL_LIMIT - 3] + "..."
            details.append(f"response={body}")
        return "; ".join(details)

    @classmethod
    def _request_error(
        cls,
        operation: str,
        response: requests.Response,
        path: str,
    ) -> RuntimeError:
        reason = str(response.reason or "").strip()
        status = f"{response.status_code}{f' {reason}' if reason else ''}"
        detail = cls._response_detail(response)
        suffix = f"; {detail}" if detail else ""
        return RuntimeError(f"{operation} failed ({status}) for {path}{suffix}")

    def ensure_collection(self, extra_parts: Iterable[str] = ()) -> None:
        current: list[str] = []
        for part in [*self.root_parts, *extra_parts]:
            current.append(part)
            key = tuple(current)
            if key in self._confirmed_collections:
                continue
            response = self.session.request("MKCOL", self.url(current), timeout=(15, 45))
            if response.status_code not in (201, 405):
                raise self._request_error("MKCOL", response, "/".join(current))
            self._confirmed_collections.add(key)

    def remote_file_size(self, parts: list[str]) -> int | None:
        body = b"""<?xml version="1.0" encoding="utf-8" ?>
<d:propfind xmlns:d="DAV:"><d:prop><d:getcontentlength /></d:prop></d:propfind>"""
        path = "/".join(parts)
        response = self.session.request(
            "PROPFIND",
            self.url([*self.root_parts, *parts]),
            headers={"Depth": "0", "Content-Type": "application/xml"},
            data=body,
            timeout=(15, 60),
        )
        if response.status_code == 404:
            return None
        if response.status_code != 207:
            raise self._request_error("PROPFIND", response, path)

        try:
            root = ET.fromstring(response.content)
        except ET.ParseError as error:
            raise RuntimeError(f"PROPFIND returned invalid XML for {path}: {error}") from error

        length_statuses: list[str] = []
        for propstat in root.findall(f".//{DAV}propstat"):
            prop = propstat.find(f"{DAV}prop")
            length = prop.find(f"{DAV}getcontentlength") if prop is not None else None
            if length is None:
                continue
            status_text = (propstat.findtext(f"{DAV}status") or "").strip()
            length_statuses.append(status_text or "missing status")
            matched = re.search(r"\s(\d{3})(?:\s|$)", status_text)
            if not matched or not 200 <= int(matched.group(1)) < 300:
                continue
            raw_size = (length.text or "").strip()
            try:
                remote_size = int(raw_size)
            except ValueError as error:
                raise RuntimeError(
                    f"PROPFIND returned invalid getcontentlength {raw_size!r} for {path}"
                ) from error
            if remote_size < 0:
                raise RuntimeError(
                    f"PROPFIND returned negative getcontentlength {remote_size} for {path}"
                )
            return remote_size

        status_detail = ", ".join(length_statuses) or "property missing"
        raise RuntimeError(
            f"PROPFIND did not return a usable getcontentlength for {path} ({status_detail})"
        )

    def has_same_size(self, parts: list[str], expected_size: int) -> bool:
        remote_size = self.remote_file_size(parts)
        return expected_size > 0 and remote_size == expected_size

    @staticmethod
    def _upload_retry_delay(attempt: int, response: requests.Response | None = None) -> float:
        retry_after = (
            str(response.headers.get("Retry-After") or "").strip() if response is not None else ""
        )
        try:
            parsed = float(retry_after)
        except ValueError:
            parsed = -1
        if parsed >= 0:
            return min(parsed, 60.0)
        return min(float(2 ** (attempt - 1)), 10.0)

    def upload(self, local_path: Path, parts: list[str]) -> None:
        size = local_path.stat().st_size
        headers = {"Content-Type": "video/mp4", "Content-Length": str(size)}
        path = "/".join(parts)
        for attempt in range(1, UPLOAD_MAX_ATTEMPTS + 1):
            try:
                with local_path.open("rb") as handle:
                    response = self.session.put(
                        self.url([*self.root_parts, *parts]),
                        data=handle,
                        headers=headers,
                        timeout=(20, 900),
                    )
            except requests.RequestException as error:
                if attempt == UPLOAD_MAX_ATTEMPTS:
                    raise RuntimeError(
                        f"PUT request failed after {UPLOAD_MAX_ATTEMPTS} attempts for {path}: "
                        f"{type(error).__name__}: {error}"
                    ) from error
                delay = self._upload_retry_delay(attempt)
                print(
                    f"UPLOAD_RETRY error={type(error).__name__} attempt={attempt}/"
                    f"{UPLOAD_MAX_ATTEMPTS} delay={delay:g}s path={path}",
                    flush=True,
                )
                time.sleep(delay)
                continue
            if response.status_code in (200, 201, 204):
                return
            if (
                response.status_code not in UPLOAD_RETRYABLE_STATUSES
                or attempt == UPLOAD_MAX_ATTEMPTS
            ):
                raise self._request_error("PUT", response, path)
            delay = self._upload_retry_delay(attempt, response)
            print(
                f"UPLOAD_RETRY status={response.status_code} attempt={attempt}/"
                f"{UPLOAD_MAX_ATTEMPTS} delay={delay:g}s path={path}",
                flush=True,
            )
            time.sleep(delay)

    def cleanup_old_dates(self, retention_days: int, today: date, dry_run: bool = False) -> list[str]:
        body = """<?xml version="1.0" encoding="utf-8" ?>
<d:propfind xmlns:d="DAV:"><d:prop><d:resourcetype /></d:prop></d:propfind>"""
        response = self.session.request(
            "PROPFIND",
            self.url(self.root_parts),
            headers={"Depth": "1", "Content-Type": "application/xml"},
            data=body.encode("utf-8"),
            timeout=(15, 60),
        )
        if response.status_code != 207:
            raise self._request_error("PROPFIND", response, "the operations root")
        cutoff = today - timedelta(days=max(1, retention_days) - 1)
        removed: list[str] = []
        root = ET.fromstring(response.content)
        for item in root.findall("{DAV:}response"):
            href = item.findtext("{DAV:}href") or ""
            name = unquote(urlparse(href).path.rstrip("/").rsplit("/", 1)[-1])
            if not DATE_RE.fullmatch(name):
                continue
            folder_date = parse_iso_date(name)
            if folder_date >= cutoff:
                continue
            removed.append(name)
            if dry_run:
                continue
            delete_response = self.session.delete(
                self.url([*self.root_parts, name]), timeout=(20, 180)
            )
            if delete_response.status_code not in (200, 204, 404):
                raise self._request_error("DELETE", delete_response, name)
        return sorted(removed)


def require_env(name: str) -> str:
    value = os.environ.get(name, "").strip()
    if not value:
        raise RuntimeError(f"Missing required environment variable: {name}")
    return value


def run(args: argparse.Namespace) -> int:
    today = datetime.now(TIMEZONE).date()
    end_date = parse_iso_date(args.target_date) if args.target_date else today
    dates = target_dates(end_date, args.days)
    github = GithubSource(os.environ.get("GITHUB_TOKEN", "").strip())
    videos = discover_videos(github, dates)
    remote_names = assign_remote_names(videos)
    total_bytes = sum(video.size for video in videos)
    date_labels = ",".join(value.isoformat() for value in dates)
    print(f"SYNC_STARTED dates={date_labels} files={len(videos)} bytes={total_bytes}", flush=True)
    for video in videos:
        print(
            f"PLAN {video.generated_date}/{video.category}/{video.name} "
            f"({video.size} bytes from {video.repo})",
            flush=True,
        )
    if args.dry_run:
        print("DRY_RUN_COMPLETE", flush=True)
        return 0

    target = WebDavTarget(
        require_env("JIANGUOYUN_WEBDAV_URL"),
        require_env("JIANGUOYUN_WEBDAV_USERNAME"),
        require_env("JIANGUOYUN_WEBDAV_PASSWORD"),
        args.remote_root,
    )
    target.ensure_collection()
    # Reclaim expired mirror space before attempting any new uploads.  Doing
    # this at the end can deadlock a full account: the upload fails before the
    # cleanup step ever gets a chance to run.
    removed = target.cleanup_old_dates(args.retention_days, today)
    print(
        f"CLEANUP_COMPLETE removed={len(removed)} "
        f"removed_dates={','.join(removed) or '-'}",
        flush=True,
    )
    uploaded = 0
    skipped = 0
    with tempfile.TemporaryDirectory(prefix="portal-jianguoyun-") as temp_dir:
        temp_root = Path(temp_dir)
        for index, video in enumerate(videos, start=1):
            remote_name = remote_names[(video.repo, video.path)]
            remote_parts = [video.generated_date, video.category, remote_name]
            target.ensure_collection(remote_parts[:2])
            if target.has_same_size(remote_parts, video.size):
                skipped += 1
                print(f"SKIP_EXISTS {index}/{len(videos)} {'/'.join(remote_parts)}", flush=True)
                continue

            local_path = temp_root / f"{index:04d}.mp4"
            print(f"DOWNLOAD_START {index}/{len(videos)} {video.repo}:{video.path}", flush=True)
            downloaded = github.download(video, local_path)
            if video.size and downloaded != video.size:
                raise RuntimeError(
                    f"Downloaded size mismatch for {video.path}: expected {video.size}, got {downloaded}"
                )
            print(f"UPLOAD_START {index}/{len(videos)} {'/'.join(remote_parts)}", flush=True)
            target.upload(local_path, remote_parts)
            uploaded += 1
            print(f"UPLOAD_DONE {index}/{len(videos)} {'/'.join(remote_parts)}", flush=True)
            local_path.unlink(missing_ok=True)

    print(
        f"SYNC_COMPLETE uploaded={uploaded} skipped={skipped} removed={len(removed)} "
        f"removed_dates={','.join(removed) or '-'}",
        flush=True,
    )
    return 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--target-date", default="", help="Last Beijing date to sync (YYYY-MM-DD).")
    parser.add_argument("--days", type=int, default=2, help="Number of dates ending at target date.")
    parser.add_argument("--retention-days", type=int, default=2)
    parser.add_argument("--remote-root", default=DEFAULT_REMOTE_ROOT)
    parser.add_argument("--dry-run", action="store_true")
    return parser


if __name__ == "__main__":
    started = time.monotonic()
    try:
        exit_code = run(build_parser().parse_args())
    except Exception as error:
        print(f"SYNC_FAILED {type(error).__name__}: {error}", flush=True)
        raise
    finally:
        print(f"ELAPSED_SECONDS={time.monotonic() - started:.1f}", flush=True)
    raise SystemExit(exit_code)
