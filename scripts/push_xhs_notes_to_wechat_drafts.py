#!/usr/bin/env python3
"""Push generated xhs_notes WeChat articles into Official Account drafts."""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

import requests

SCRIPT_DIR = Path(__file__).resolve().parent
sys.path.insert(0, str(SCRIPT_DIR))

from push_kc_translated_to_wechat_drafts import (  # noqa: E402
    AUTHOR,
    BOTTOM_DISCLAIMER,
    BRAND,
    DEFAULT_ARTICLES_PER_DRAFT,
    DEFAULT_BODY_HOOK,
    DEFAULT_BODY_VISIBLE_CHARS,
    DEFAULT_MAX_CONTENT_BYTES,
    DEFAULT_MAX_CONTENT_CHARS,
    DEFAULT_MIN_INLINE_IMAGES,
    DEFAULT_TRAILING_IMAGE,
    DISPLAY_TITLE_MAX_CHARS,
    MD_IMAGE_RE,
    WECHAT_AUTHOR_MAX_BYTES,
    WECHAT_TITLE_MAX_CHARS,
    WeChatError,
    add_draft,
    article_payload,
    chunked,
    content_within_limits,
    digest_from_markdown,
    fake_static_image_url,
    get_stable_access_token,
    is_article_size_error,
    log,
    parse_selection_limit,
    prepare_article_upload_image,
    render_fitted_wechat_html,
    resolve_asset_path,
    resolve_repo_asset_path,
    source_report_name_from_xhs_dir,
    submit_publish,
    truncate_chars,
    truncate_utf8_bytes,
    upload_article_image,
    upload_cover_material,
    utf8_byte_count,
    verify_draft_get,
    wechat_title_policy_skip_reason,
    write_json,
)

from institution_names import ensure_title_has_institution, infer_institution_name  # noqa: E402

DATE_DIR_RE = re.compile(r"^\d{6,8}$")
IMAGE_SUFFIXES = {".jpg", ".jpeg", ".png", ".webp"}
TRAILING_IMAGE_MARKERS = {
    "prompts/zsxq_img.jpg",
    "github.com/yt-feng/rpt_edit/blob/main/prompts/zsxq_img.jpg",
}


def latest_date_dir(root: Path) -> Path:
    if not root.exists():
        raise RuntimeError(f"Dropbox output root not found: {root}")
    candidates = [p for p in root.iterdir() if p.is_dir() and DATE_DIR_RE.match(p.name)]
    if not candidates:
        raise RuntimeError(f"No date-named folders found under {root}")
    return max(candidates, key=lambda p: int(p.name))


def shard_sort_key(path: Path) -> tuple[int, str]:
    match = re.search(r"(\d+)$", path.name)
    return (int(match.group(1)) if match else 10**9, path.name)


def find_report_dirs(date_dir: Path) -> list[Path]:
    report_dirs: list[Path] = []
    for shard in sorted(date_dir.glob("shard_*"), key=shard_sort_key):
        if not shard.is_dir():
            continue
        for item in sorted(shard.iterdir(), key=lambda p: p.name):
            if item.is_dir() and (item / "wechat_article.md").exists():
                report_dirs.append(item)
    for item in sorted(date_dir.iterdir(), key=lambda p: p.name):
        if item.is_dir() and (item / "wechat_article.md").exists():
            report_dirs.append(item)

    seen: set[str] = set()
    unique: list[Path] = []
    for path in report_dirs:
        key = str(path.resolve())
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def clean_xhs_markdown(markdown: str) -> str:
    cleaned: list[str] = []
    for raw in markdown.splitlines():
        line = raw.strip()
        lowered = line.lower()
        if any(marker in line for marker in TRAILING_IMAGE_MARKERS):
            continue
        if line.startswith("<p") and ("not investment advice" in lowered or "personal reading notes" in lowered):
            continue
        cleaned.append(raw)
    return "\n".join(cleaned).strip()


def read_json(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}
    return data if isinstance(data, dict) else {}


def xhs_article_title(markdown: str, fallback: str, institution_name: str) -> str:
    for raw in markdown.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            title = re.sub(r"^#{1,6}\s*", "", line).strip()
            if title:
                return truncate_chars(ensure_title_has_institution(title, institution_name), WECHAT_TITLE_MAX_CHARS)
    return truncate_chars(ensure_title_has_institution(fallback, institution_name), WECHAT_TITLE_MAX_CHARS)


def xhs_article_title_metadata(report_dir: Path) -> dict[str, str]:
    markdown_path = report_dir / "wechat_article.md"
    markdown = clean_xhs_markdown(markdown_path.read_text(encoding="utf-8", errors="ignore"))
    status = read_json(report_dir / "status.json")
    institution_name = infer_institution_name(
        report_dir.name,
        status.get("source_pdf"),
        markdown[:1200],
    )
    source_report_name = source_report_name_from_xhs_dir(report_dir)
    title = xhs_article_title(markdown, report_dir.name, institution_name)
    return {
        "report_dir": str(report_dir),
        "wechat_markdown": str(markdown_path),
        "title": title,
        "wechat_title": title,
        "institution_name": institution_name,
        "source_report_name": source_report_name,
    }


def markdown_local_image_refs(markdown: str) -> list[str]:
    refs: list[str] = []
    for _alt, raw_ref in MD_IMAGE_RE.findall(markdown):
        ref = raw_ref.strip().strip("<>").split("#", 1)[0].split("?", 1)[0]
        if not ref or ref.startswith(("http://", "https://")):
            continue
        if ref not in refs:
            refs.append(ref)
    return refs


def extra_asset_images(report_dir: Path, already: set[Path]) -> list[tuple[str, Path]]:
    assets_dir = report_dir / "assets"
    if not assets_dir.exists():
        return []
    candidates = [
        *sorted(assets_dir.glob("source_image_*")),
        *sorted(assets_dir.glob("cover.*")),
        *sorted(assets_dir.glob("xhs_card_*")),
    ]
    extras: list[tuple[str, Path]] = []
    for path in candidates:
        if path.suffix.lower() not in IMAGE_SUFFIXES or not path.is_file():
            continue
        resolved = path.resolve()
        if resolved in already:
            continue
        already.add(resolved)
        ref = path.relative_to(report_dir).as_posix()
        extras.append((ref, path))
    return extras


def choose_cover_image(report_dir: Path, uploaded_paths: list[Path]) -> Path:
    for candidate in [
        report_dir / "assets" / "cover.png",
        report_dir / "assets" / "cover.jpg",
        report_dir / "assets" / "source_image_01.jpg",
        report_dir / "assets" / "source_image_01.png",
    ]:
        if candidate.exists() and candidate.is_file():
            return candidate
    for path in uploaded_paths:
        if path.exists() and path.is_file():
            return path
    fallback = report_dir / "assets" / "cover.png"
    if fallback.exists():
        return fallback
    raise RuntimeError(f"No cover image found for {report_dir}")


def upload_or_fake_article_image(
    report_dir: Path,
    ref: str,
    path: Path,
    index: int,
    args: argparse.Namespace,
    session: requests.Session | None,
    access_token: str | None,
    output_dir: Path,
) -> tuple[str, str]:
    if args.dry_run:
        return str(path), fake_static_image_url(f"{report_dir.name}/{ref}")
    if session is None or access_token is None:
        raise RuntimeError("session and access_token are required outside dry-run")
    upload_path = prepare_article_upload_image(path, output_dir, f"article_{index:02d}_{path.stem}")
    return str(upload_path), upload_article_image(session, access_token, upload_path, args.timeout)


def build_article(
    report_dir: Path,
    index: int,
    args: argparse.Namespace,
    session: requests.Session | None,
    access_token: str | None,
    output_dir: Path,
    trailing_image_url: str,
) -> dict[str, Any]:
    markdown_path = report_dir / "wechat_article.md"
    markdown = clean_xhs_markdown(markdown_path.read_text(encoding="utf-8", errors="ignore"))
    status = read_json(report_dir / "status.json")
    institution_name = infer_institution_name(
        report_dir.name,
        status.get("source_pdf"),
        markdown[:1200],
    )
    source_report_name = source_report_name_from_xhs_dir(report_dir)
    title = xhs_article_title(markdown, report_dir.name, institution_name)
    wechat_title = title

    image_urls: dict[str, str] = {}
    uploaded_images: list[dict[str, str]] = []
    uploaded_paths: list[Path] = []
    seen_paths: set[Path] = set()

    refs = markdown_local_image_refs(markdown)
    target_image_count = min(max(args.min_inline_images, len(refs)), args.max_inline_images)
    image_items: list[tuple[str, Path]] = []
    for ref in refs:
        path = resolve_asset_path(report_dir, ref)
        if not path or path.suffix.lower() not in IMAGE_SUFFIXES:
            continue
        resolved = path.resolve()
        if resolved in seen_paths:
            continue
        seen_paths.add(resolved)
        image_items.append((ref, path))
        if len(image_items) >= args.max_inline_images:
            break

    if len(image_items) < target_image_count:
        image_items.extend(extra_asset_images(report_dir, seen_paths)[: target_image_count - len(image_items)])

    for ref, path in image_items[: args.max_inline_images]:
        upload_path, image_url = upload_or_fake_article_image(
            report_dir, ref, path, index, args, session, access_token, output_dir
        )
        image_urls[ref] = image_url
        image_urls[path.name] = image_url
        image_urls[path.relative_to(report_dir).as_posix()] = image_url
        uploaded_paths.append(Path(upload_path))
        uploaded_images.append({"token": ref, "path": upload_path, "url": image_url, "source": "xhs_notes"})

    cover_image = choose_cover_image(report_dir, [p for p in uploaded_paths if p.exists()])
    if args.dry_run:
        thumb_media_id = f"DRY_RUN_THUMB_{index:02d}"
    else:
        if session is None or access_token is None:
            raise RuntimeError("session and access_token are required outside dry-run")
        thumb_media_id = upload_cover_material(session, access_token, cover_image, args.timeout)

    content, visible_text_chars, body_image_count, fitted_image_count = render_fitted_wechat_html(
        markdown,
        title,
        args.brand,
        image_urls,
        uploaded_images,
        args.body_hook,
        args.disclaimer,
        trailing_image_url,
        source_report_name,
        args.max_body_chars,
        args.max_content_chars,
        args.max_content_bytes,
    )
    if not content_within_limits(content, args.max_content_chars, args.max_content_bytes):
        raise RuntimeError(
            f"WeChat HTML for {report_dir.name} is {len(content)} chars / {utf8_byte_count(content)} bytes, "
            f"above --max-content-chars={args.max_content_chars} or --max-content-bytes={args.max_content_bytes}"
        )
    if fitted_image_count < len(uploaded_images):
        log(
            f"Compressed article {index}: kept {fitted_image_count}/{len(uploaded_images)} body images "
            f"to fit WeChat content limit."
        )

    article: dict[str, Any] = {
        "article_type": "news",
        "title": wechat_title,
        "author": truncate_utf8_bytes(args.author, WECHAT_AUTHOR_MAX_BYTES),
        "digest": "",
        "content": content,
        "thumb_media_id": thumb_media_id,
        "need_open_comment": 0,
        "only_fans_can_comment": 0,
    }
    if args.content_source_url:
        article["content_source_url"] = args.content_source_url

    return {
        "report_dir": str(report_dir),
        "wechat_markdown": str(markdown_path),
        "title": truncate_chars(title, DISPLAY_TITLE_MAX_CHARS),
        "wechat_title": wechat_title,
        "digest": digest_from_markdown(markdown),
        "institution_name": institution_name,
        "source_report_name": source_report_name,
        "article": article,
        "cover_image": str(cover_image),
        "inline_images": uploaded_images,
        "content_chars": len(content),
        "content_bytes": utf8_byte_count(content),
        "visible_text_chars": visible_text_chars,
        "body_image_count": body_image_count,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Create WeChat drafts from xhs_notes/dropbox report articles.")
    parser.add_argument("--dropbox-output-root", default="xhs_notes/dropbox")
    parser.add_argument("--date-folder", default="latest")
    parser.add_argument("--output-root", default="wechat_drafts/xhs_notes")
    parser.add_argument("--max-articles", default="all")
    parser.add_argument("--article-offset", type=int, default=0)
    parser.add_argument("--articles-per-draft", type=int, default=DEFAULT_ARTICLES_PER_DRAFT)
    parser.add_argument("--max-inline-images", type=int, default=DEFAULT_MIN_INLINE_IMAGES)
    parser.add_argument("--min-inline-images", type=int, default=DEFAULT_MIN_INLINE_IMAGES)
    parser.add_argument("--max-body-chars", type=int, default=DEFAULT_BODY_VISIBLE_CHARS)
    parser.add_argument("--max-content-chars", type=int, default=DEFAULT_MAX_CONTENT_CHARS)
    parser.add_argument("--max-content-bytes", type=int, default=DEFAULT_MAX_CONTENT_BYTES)
    parser.add_argument("--brand", default=BRAND)
    parser.add_argument("--author", default=AUTHOR)
    parser.add_argument("--disclaimer", default=BOTTOM_DISCLAIMER)
    parser.add_argument("--body-hook", default=DEFAULT_BODY_HOOK)
    parser.add_argument("--trailing-image", default=DEFAULT_TRAILING_IMAGE)
    parser.add_argument("--content-source-url", default="")
    parser.add_argument("--wechat-appid", default=os.getenv("WECHAT_MP_APPID", ""))
    parser.add_argument("--wechat-secret", default=os.getenv("WECHAT_MP_APPSECRET", ""))
    parser.add_argument("--timeout", type=int, default=120)
    parser.add_argument("--publish", action="store_true", help="Submit each created draft for publishing.")
    parser.add_argument("--dry-run", action="store_true", help="Build payloads without calling WeChat APIs.")
    args = parser.parse_args()

    max_articles = parse_selection_limit(args.max_articles, "--max-articles")
    if args.article_offset < 0:
        raise ValueError("--article-offset must be non-negative")
    if not 1 <= args.articles_per_draft <= 9:
        raise ValueError("--articles-per-draft must be between 1 and 9")
    if args.max_inline_images < 0:
        raise ValueError("--max-inline-images must be non-negative")
    if args.min_inline_images < 0:
        raise ValueError("--min-inline-images must be non-negative")
    if args.max_body_chars < 200:
        raise ValueError("--max-body-chars must be at least 200")
    if not args.dry_run and (not args.wechat_appid or not args.wechat_secret):
        raise ValueError("WECHAT_MP_APPID and WECHAT_MP_APPSECRET are required unless --dry-run is set")

    root = Path(args.dropbox_output_root)
    date_dir = latest_date_dir(root) if args.date_folder == "latest" else root / args.date_folder
    if not date_dir.exists():
        raise RuntimeError(f"Date folder not found: {date_dir}")

    report_dirs = find_report_dirs(date_dir)
    if max_articles is None:
        selected = report_dirs[args.article_offset :]
    else:
        selected = report_dirs[args.article_offset : args.article_offset + max_articles]

    output_dir = Path(args.output_root) / date_dir.name
    output_dir.mkdir(parents=True, exist_ok=True)
    if not selected:
        summary_path = output_dir / "wechat_draft_summary.json"
        summary = {
            "date_folder": date_dir.name,
            "source": "xhs_notes/dropbox",
            "dry_run": args.dry_run,
            "publish": args.publish,
            "max_articles": "all" if max_articles is None else max_articles,
            "input_selected_count": 0,
            "selected_count": 0,
            "skipped_title_policy_count": 0,
            "skipped_title_policy": [],
            "draft_count": 0,
            "status": "skipped_no_xhs_wechat_articles",
            "message": f"No xhs report articles selected from {date_dir}",
            "drafts": [],
            "articles": [],
        }
        write_json(summary_path, summary)
        log(f"No xhs report articles selected from {date_dir}; wrote skip summary: {summary_path}")
        return 0

    input_selected_count = len(selected)
    skipped_title_policy: list[dict[str, str]] = []
    allowed_selected: list[Path] = []
    for report_dir in selected:
        metadata = xhs_article_title_metadata(report_dir)
        reason = wechat_title_policy_skip_reason(metadata["wechat_title"])
        if reason:
            record = dict(metadata)
            record["skip_reason"] = reason
            skipped_title_policy.append(record)
            log(
                "Skipped WeChat draft article by title policy: "
                f"{metadata['wechat_title']} ({reason})"
            )
        else:
            allowed_selected.append(report_dir)
    selected = allowed_selected

    if not selected:
        summary_path = output_dir / "wechat_draft_summary.json"
        summary = {
            "date_folder": date_dir.name,
            "source": "xhs_notes/dropbox",
            "dry_run": args.dry_run,
            "publish": args.publish,
            "max_articles": "all" if max_articles is None else max_articles,
            "input_selected_count": input_selected_count,
            "selected_count": 0,
            "skipped_title_policy_count": len(skipped_title_policy),
            "skipped_title_policy": skipped_title_policy,
            "draft_count": 0,
            "status": "skipped_title_policy",
            "message": f"All selected xhs report articles were blocked by WeChat title policy from {date_dir}",
            "drafts": [],
            "articles": [],
        }
        write_json(summary_path, summary)
        log(f"All selected xhs report articles blocked by title policy; wrote skip summary: {summary_path}")
        return 0

    log(
        f"Selected {len(selected)} xhs WeChat articles from {date_dir} "
        f"(skipped_title_policy={len(skipped_title_policy)}/{input_selected_count})"
    )

    session: requests.Session | None = None
    access_token: str | None = None
    if not args.dry_run:
        session = requests.Session()
        access_token = get_stable_access_token(session, args.wechat_appid, args.wechat_secret, args.timeout)
        log("Fetched WeChat access token")

    trailing_image_url = ""
    trailing_image_path = resolve_repo_asset_path(args.trailing_image)
    if args.trailing_image and not trailing_image_path:
        raise RuntimeError(f"Trailing image not found: {args.trailing_image}")
    if trailing_image_path:
        if args.dry_run:
            trailing_image_url = fake_static_image_url(str(trailing_image_path))
        else:
            if session is None or access_token is None:
                raise RuntimeError("session and access_token are required outside dry-run")
            trailing_image_url = upload_article_image(session, access_token, trailing_image_path, args.timeout)
            log(f"Uploaded trailing image: {trailing_image_path}")

    built_articles = [
        build_article(report_dir, idx, args, session, access_token, output_dir, trailing_image_url)
        for idx, report_dir in enumerate(selected, 1)
    ]

    drafts: list[dict[str, Any]] = []

    def create_draft(group: list[dict[str, Any]]) -> None:
        articles = article_payload(group)
        payload_bytes = utf8_byte_count(json.dumps({"articles": articles}, ensure_ascii=False, separators=(",", ":")))
        if args.dry_run:
            media_id = f"DRY_RUN_DRAFT_{len(drafts) + 1:02d}"
            publish_id = f"DRY_RUN_PUBLISH_{len(drafts) + 1:02d}" if args.publish else ""
            draft_get = {
                "ok": True,
                "dry_run": True,
                "article_count": len(articles),
                "expected_article_count": len(articles),
                "matches_expected_article_count": True,
                "titles": [item.get("title", "") for item in articles],
            }
        else:
            if session is None or access_token is None:
                raise RuntimeError("session and access_token are required outside dry-run")
            try:
                media_id = add_draft(session, access_token, articles, args.timeout)
            except WeChatError as exc:
                if is_article_size_error(exc) and len(group) > 1:
                    split_at = max(1, len(group) // 2)
                    log(
                        "WeChat rejected draft group as too large; "
                        f"splitting {len(group)} articles into {split_at}+{len(group) - split_at} and retrying."
                    )
                    create_draft(group[:split_at])
                    create_draft(group[split_at:])
                    return
                raise
            draft_get = verify_draft_get(session, access_token, media_id, args.timeout, len(articles))
            publish_id = submit_publish(session, access_token, media_id, args.timeout) if args.publish else ""

        draft_index = len(drafts) + 1
        payload_path = output_dir / f"draft_payload_{draft_index:02d}.json"
        write_json(payload_path, {"articles": articles})
        drafts.append(
            {
                "draft_index": draft_index,
                "media_id": media_id,
                "publish_id": publish_id,
                "published": bool(publish_id),
                "article_count": len(articles),
                "payload_bytes": payload_bytes,
                "payload": str(payload_path),
                "titles": [item["title"] for item in group],
                "wechat_titles": [item["wechat_title"] for item in group],
                "draft_get": draft_get,
            }
        )
        if publish_id:
            log(f"Draft {draft_index}: articles={len(articles)} media_id={media_id} publish_id={publish_id}")
        else:
            log(f"Draft {draft_index}: articles={len(articles)} media_id={media_id}")

    for group in chunked(built_articles, args.articles_per_draft):
        create_draft(group)

    summary = {
        "date_folder": date_dir.name,
        "source": "xhs_notes/dropbox",
        "dry_run": args.dry_run,
        "publish": args.publish,
        "max_articles": "all" if max_articles is None else max_articles,
        "input_selected_count": input_selected_count,
        "selected_count": len(selected),
        "skipped_title_policy_count": len(skipped_title_policy),
        "skipped_title_policy": skipped_title_policy,
        "articles_per_draft": args.articles_per_draft,
        "draft_count": len(drafts),
        "max_body_chars": args.max_body_chars,
        "max_content_chars": args.max_content_chars,
        "max_content_bytes": args.max_content_bytes,
        "min_inline_images": args.min_inline_images,
        "max_inline_images": args.max_inline_images,
        "body_hook": args.body_hook,
        "trailing_image": str(trailing_image_path) if trailing_image_path else "",
        "drafts": drafts,
        "articles": [
            {
                "title": item["title"],
                "wechat_title": item["wechat_title"],
                "institution_name": item["institution_name"],
                "source_report_name": item["source_report_name"],
                "report_dir": item["report_dir"],
                "content_chars": item["content_chars"],
                "content_bytes": item["content_bytes"],
                "visible_text_chars": item["visible_text_chars"],
                "inline_image_count": len(item["inline_images"]),
                "body_image_count": item["body_image_count"],
                "cover_image": item["cover_image"],
            }
            for item in built_articles
        ],
    }
    summary_path = output_dir / "wechat_draft_summary.json"
    write_json(summary_path, summary)
    log(f"Wrote summary: {summary_path}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
