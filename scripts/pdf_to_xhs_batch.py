#!/usr/bin/env python3
"""Repo PDFs -> MinerU -> Xiaohongshu cards/notes + WeChat teaser articles."""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import sys
import time
import zipfile
from io import BytesIO
from pathlib import Path
from typing import Any

import fitz
import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

MINERU_BASE_URL = "https://mineru.net"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
DONE_STATES = {"done", "success", "completed"}
FAILED_STATES = {"failed", "fail", "error"}
XHS_CANVAS_SIZE = (1080, 1440)
XHS_BG_COLOR = (9, 31, 64)
XHS_CARD_COLOR = (255, 255, 255)


def log(message: str) -> None:
    print(message, flush=True)


def slug(value: str) -> str:
    value = Path(value).name
    value = re.sub(r"\.pdf$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:80] or "report"


def mineru_headers(token: str) -> dict[str, str]:
    return {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    code = data.get("code")
    if response.status_code >= 400 or code not in (None, 0, "0"):
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:1000]}")
    return data


def find_pdfs(input_dir: Path, output_dir: Path) -> list[Path]:
    if not input_dir.exists():
        raise RuntimeError(f"Input folder does not exist: {input_dir}")
    output_dir = output_dir.resolve()
    return sorted(p for p in input_dir.rglob("*.pdf") if p.is_file() and output_dir not in p.resolve().parents)


def submit_to_mineru(pdfs: list[Path], input_dir: Path, token: str, args: argparse.Namespace) -> tuple[str, dict[str, Path]]:
    files = []
    data_id_to_pdf: dict[str, Path] = {}
    for pdf in pdfs:
        rel = pdf.relative_to(input_dir).as_posix()
        data_id = re.sub(r"[^A-Za-z0-9._-]+", "_", rel)[:128]
        data_id_to_pdf[data_id] = pdf
        files.append({"name": f"{slug(rel)}.pdf", "data_id": data_id, "is_ocr": args.ocr.lower() == "true"})

    payload = {
        "files": files,
        "model_version": args.mineru_model,
        "language": args.language,
        "enable_table": True,
        "enable_formula": True,
    }
    response = requests.post(f"{MINERU_BASE_URL}/api/v4/file-urls/batch", headers=mineru_headers(token), json=payload, timeout=60)
    data = parse_json_response(response, "MinerU get upload URLs")
    body = data.get("data", {})
    batch_id = body.get("batch_id")
    upload_urls = body.get("file_urls") or []
    if not batch_id or len(upload_urls) != len(pdfs):
        raise RuntimeError(f"Unexpected MinerU upload-url response: {json.dumps(data, ensure_ascii=False)[:1000]}")

    for pdf, upload_url in zip(pdfs, upload_urls):
        log(f"Uploading PDF to MinerU: {pdf}")
        upload = requests.put(upload_url, data=pdf.read_bytes(), timeout=300)
        if upload.status_code not in (200, 201, 204):
            raise RuntimeError(f"MinerU upload failed for {pdf}: HTTP {upload.status_code}, {upload.text[:500]}")
    return str(batch_id), data_id_to_pdf


def poll_mineru(batch_id: str, token: str, timeout_seconds: int, interval_seconds: int) -> list[dict[str, Any]]:
    deadline = time.time() + timeout_seconds
    url = f"{MINERU_BASE_URL}/api/v4/extract-results/batch/{batch_id}"
    last_response: dict[str, Any] | None = None
    while time.time() < deadline:
        response = requests.get(url, headers=mineru_headers(token), timeout=60)
        data = parse_json_response(response, "MinerU poll results")
        last_response = data
        rows = data.get("data", {}).get("extract_result") or []
        states = [str(row.get("state", "")).lower() for row in rows]
        if states:
            log("MinerU states: " + ", ".join(states))
        if rows and all(state in DONE_STATES or state in FAILED_STATES for state in states):
            return rows
        time.sleep(interval_seconds)
    raise RuntimeError(f"Timed out waiting for MinerU batch {batch_id}. Last response: {json.dumps(last_response, ensure_ascii=False)[:1000]}")


def download_and_unzip(url: str, result_dir: Path) -> None:
    result_dir.mkdir(parents=True, exist_ok=True)
    response = requests.get(url, timeout=300)
    response.raise_for_status()
    zip_path = result_dir.parent / "mineru_result.zip"
    zip_path.write_bytes(response.content)
    with zipfile.ZipFile(BytesIO(response.content)) as zf:
        zf.extractall(result_dir)


def find_markdown(result_dir: Path) -> Path | None:
    candidates = list(result_dir.rglob("full.md")) or list(result_dir.rglob("*.md"))
    return max(candidates, key=lambda path: path.stat().st_size) if candidates else None


def load_font(size: int, bold: bool = False):
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def load_kai_font(size: int):
    candidates = [
        "/usr/share/fonts/truetype/arphic/ukai.ttc",
        "/usr/share/fonts/opentype/arphic/ukai.ttc",
        "/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSerifCJK-Regular.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return load_font(size, bold=False)


def safe_open_image(path: Path) -> Image.Image | None:
    try:
        return Image.open(path).convert("RGB")
    except Exception as exc:
        log(f"Skip unreadable image {path}: {exc}")
        return None


def draw_xhs_card(image: Image.Image, target_path: Path) -> None:
    """Pad source image on a clean deep-blue 1080x1440 canvas."""
    canvas = Image.new("RGB", XHS_CANVAS_SIZE, XHS_BG_COLOR)
    image = ImageOps.contain(image.convert("RGB"), (960, 1120), method=Image.Resampling.LANCZOS)
    image_x = (XHS_CANVAS_SIZE[0] - image.width) // 2
    image_y = (XHS_CANVAS_SIZE[1] - image.height) // 2 - 28
    image_y = max(64, image_y)

    margin = 28
    card_box = (
        max(36, image_x - margin),
        max(50, image_y - margin),
        min(XHS_CANVAS_SIZE[0] - 36, image_x + image.width + margin),
        min(XHS_CANVAS_SIZE[1] - 150, image_y + image.height + margin),
    )

    canvas_rgba = canvas.convert("RGBA")
    shadow = Image.new("RGBA", XHS_CANVAS_SIZE, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((card_box[0] + 10, card_box[1] + 14, card_box[2] + 10, card_box[3] + 14), radius=34, fill=(0, 0, 0, 80))
    shadow = shadow.filter(ImageFilter.GaussianBlur(16))
    canvas_rgba = Image.alpha_composite(canvas_rgba, shadow)

    draw = ImageDraw.Draw(canvas_rgba)
    draw.rounded_rectangle(card_box, radius=32, fill=XHS_CARD_COLOR)
    canvas_rgba.paste(image.convert("RGBA"), (image_x, image_y))

    watermark = "Kris笔记"
    watermark_font = load_kai_font(38)
    bbox = draw.textbbox((0, 0), watermark, font=watermark_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text(((XHS_CANVAS_SIZE[0] - text_w) // 2, XHS_CANVAS_SIZE[1] - text_h - 46), watermark, font=watermark_font, fill=(226, 234, 246, 150))

    target_path.parent.mkdir(parents=True, exist_ok=True)
    canvas_rgba.convert("RGB").save(target_path, quality=94)


def pad_image_for_xhs(source_path: Path, target_path: Path) -> bool:
    image = safe_open_image(source_path)
    if image is None:
        return False
    draw_xhs_card(image, target_path)
    return True


def render_pdf_page_cards(pdf_path: Path, assets_dir: Path, max_pages: int) -> list[str]:
    cards: list[str] = []
    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:
        log(f"Cannot open PDF for fallback image cards: {pdf_path}: {exc}")
        return cards
    try:
        for index in range(min(max_pages, len(doc))):
            pix = doc[index].get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
            image = Image.open(BytesIO(pix.tobytes("png"))).convert("RGB")
            target = assets_dir / f"xhs_card_{index + 1:02d}.png"
            draw_xhs_card(image, target)
            cards.append(str(target.relative_to(assets_dir.parent)))
    finally:
        doc.close()
    return cards


def create_visual_assets(result_dir: Path, pdf_path: Path, assets_dir: Path, max_images: int) -> list[str]:
    """Create stable Xiaohongshu image cards: assets/xhs_card_01.png, assets/xhs_card_02.png, etc."""
    assets_dir.mkdir(parents=True, exist_ok=True)
    images = [p for p in result_dir.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES]
    images.sort(key=lambda path: path.stat().st_size, reverse=True)
    cards: list[str] = []
    for index, image in enumerate(images[:max_images], 1):
        original_target = assets_dir / f"source_image_{index:02d}{image.suffix.lower()}"
        shutil.copy2(image, original_target)
        card_target = assets_dir / f"xhs_card_{index:02d}.png"
        if pad_image_for_xhs(image, card_target):
            cards.append(str(card_target.relative_to(assets_dir.parent)))
        else:
            cards.append(str(original_target.relative_to(assets_dir.parent)))
    if not cards:
        log("MinerU result contained no standalone images; rendering PDF page fallback cards.")
        cards = render_pdf_page_cards(pdf_path, assets_dir, max_pages=min(max_images, 4))
    return cards


def trim_source_text(source_text: str, prompt_chars: int) -> str:
    source_text = re.sub(r"\n{3,}", "\n\n", source_text).strip()
    if len(source_text) > prompt_chars:
        head_len = int(prompt_chars * 0.72)
        tail_len = int(prompt_chars * 0.22)
        source_text = source_text[:head_len] + "\n\n[中间内容因长度限制已省略]\n\n" + source_text[-tail_len:]
    return source_text


def build_xhs_prompt(template_path: Path, source_text: str, args: argparse.Namespace) -> str:
    source_text = trim_source_text(source_text, args.prompt_chars)
    disclaimer = "在最后加一行轻量免责声明：非投资建议，仅作学习交流。" if args.disclaimer else "不要写免责声明。"
    tags = f"末尾追加 3-8 个话题标签，优先包含：{args.hashtags}" if args.hashtags else "末尾追加 3-8 个合适的话题标签。"
    return template_path.read_text(encoding="utf-8").format(
        style_preset=args.style,
        target_length=args.length,
        emoji_density=args.emoji,
        disclaimer_rule=disclaimer,
        hashtag_rule=tags,
        source_text=source_text,
    )


def build_wechat_prompt(template_path: Path, source_text: str, args: argparse.Namespace) -> str:
    source_text = trim_source_text(source_text, args.wechat_prompt_chars)
    return template_path.read_text(encoding="utf-8").format(
        target_length=args.wechat_length,
        community_cta=args.community_cta,
        source_text=source_text,
    )


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return f"未检测到 DEEPSEEK_API_KEY。请复制对应 prompt 文件到 DeepSeek 中生成：{label}。\n"
    url = args.deepseek_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": args.model,
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": "你是严谨但有传播力的中文财经内容编辑，输出必须可直接发布。"},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(url, headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}, json=payload, timeout=180)
    data = parse_json_response(response, f"DeepSeek generate {label}")
    try:
        return data["choices"][0]["message"]["content"].strip() + "\n"
    except Exception as exc:
        raise RuntimeError(f"Unexpected DeepSeek response: {json.dumps(data, ensure_ascii=False)[:1000]}") from exc


def safe_generate_text(prompt: str, args: argparse.Namespace, label: str) -> str:
    try:
        return call_deepseek(prompt, args, label)
    except Exception as exc:
        log(f"DeepSeek generation failed for {label}: {exc}")
        return f"DeepSeek 生成 {label} 失败：{exc}\n\n请复制对应 prompt 文件手动生成。\n"


def embed_images_in_wechat_article(article: str, image_paths: list[str], max_images: int = 3) -> str:
    clean_paths = [p for p in image_paths if p.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
    if not clean_paths:
        return article
    images = [f"\n![研报图表 {i}]({path})\n" for i, path in enumerate(clean_paths[:max_images], 1)]
    lines = article.strip().splitlines()
    if not lines:
        return "\n".join(images).strip() + "\n"
    h2_indices = [idx for idx, line in enumerate(lines) if line.startswith("## ")]
    inserted = 0
    if h2_indices:
        lines.insert(h2_indices[0], images[0])
        inserted = 1
        offset = 1
        for img, original_idx in zip(images[1:], h2_indices[1:max_images]):
            lines.insert(original_idx + offset, img)
            offset += 1
            inserted += 1
    if inserted == 0:
        insert_at = min(len(lines), 5)
        for img in reversed(images):
            lines.insert(insert_at, img)
    return "\n".join(lines).strip() + "\n"


def extract_cover_titles(note: str, fallback: str) -> tuple[str, str]:
    lines = [re.sub(r"^[#>*\-\s]+", "", line).strip() for line in note.splitlines() if line.strip()]
    short_title = ""
    subtitle = ""
    for line in lines[:10]:
        if "封面短标题" in line:
            short_title = re.split(r"[:：]", line, 1)[-1].strip()
        if "封面副标题" in line:
            subtitle = re.split(r"[:：]", line, 1)[-1].strip()
    if not short_title:
        short_title = lines[0] if lines else fallback
    if not subtitle:
        subtitle = "研报重点一图看懂"
    return short_title[:10], subtitle[:18]


def center_crop(image: Image.Image, size: tuple[int, int]) -> Image.Image:
    source_w, source_h = image.size
    target_w, target_h = size
    scale = max(target_w / source_w, target_h / source_h)
    resized = image.resize((int(source_w * scale), int(source_h * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - target_w) // 2
    top = (resized.height - target_h) // 2
    return resized.crop((left, top, left + target_w, top + target_h))


def make_cover(pdf_path: Path, cover_path: Path, title: str, subtitle: str, watermark: str) -> None:
    cover_path.parent.mkdir(parents=True, exist_ok=True)
    doc = fitz.open(pdf_path)
    try:
        pix = doc[0].get_pixmap(matrix=fitz.Matrix(2, 2), alpha=False)
        image = Image.open(BytesIO(pix.tobytes("png"))).convert("RGB")
    finally:
        doc.close()
    image = center_crop(image, XHS_CANVAS_SIZE).filter(ImageFilter.GaussianBlur(0.4)).convert("RGBA")
    overlay = Image.new("RGBA", XHS_CANVAS_SIZE, (*XHS_BG_COLOR, 75))
    image = Image.alpha_composite(image, overlay)
    draw = ImageDraw.Draw(image)
    box = (110, 500, 970, 900)
    blurred = image.crop(box).filter(ImageFilter.GaussianBlur(16))
    image.paste(blurred, box)
    draw.rounded_rectangle(box, radius=42, fill=(255, 255, 255, 222), outline=(40, 40, 40, 55), width=2)
    title_font = load_font(88, bold=True)
    subtitle_font = load_font(38, bold=False)
    watermark_font = load_kai_font(28)
    for text, y, font, fill in [(title, 620, title_font, (18, 18, 18, 255)), (subtitle, 745, subtitle_font, (70, 70, 70, 255))]:
        bbox = draw.textbbox((0, 0), text, font=font)
        x = (1080 - (bbox[2] - bbox[0])) // 2
        draw.text((x, y), text, font=font, fill=fill)
    draw.text((54, 1368), watermark, font=watermark_font, fill=(255, 255, 255, 210), stroke_width=2, stroke_fill=(0, 0, 0, 110))
    image.convert("RGB").save(cover_path, quality=92)


def process_pdf(pdf_path: Path, result_row: dict[str, Any], output_root: Path, args: argparse.Namespace) -> dict[str, Any]:
    item_dir = output_root / slug(pdf_path.name)
    raw_dir = item_dir / "mineru_raw"
    assets_dir = item_dir / "assets"
    item_dir.mkdir(parents=True, exist_ok=True)
    state = str(result_row.get("state", "")).lower()
    fallback_title = slug(pdf_path.name)[:18]
    status: dict[str, Any] = {
        "source_pdf": str(pdf_path),
        "mineru_state": result_row.get("state"),
        "mineru_error": result_row.get("err_msg") or result_row.get("error") or "",
    }
    if state not in DONE_STATES or not result_row.get("full_zip_url"):
        status["error"] = "MinerU did not return a successful full_zip_url for this PDF."
        (item_dir / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return status
    download_and_unzip(result_row["full_zip_url"], raw_dir)
    status["images"] = create_visual_assets(raw_dir, pdf_path, assets_dir, args.max_images)
    markdown_path = find_markdown(raw_dir)
    if not markdown_path:
        status["error"] = "MinerU result zip did not contain markdown. Visual cards may still have been generated."
        (item_dir / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return status
    source_text = markdown_path.read_text(encoding="utf-8", errors="ignore")
    (item_dir / "source_mineru.md").write_text(source_text, encoding="utf-8")
    xhs_prompt = build_xhs_prompt(Path(args.prompt_template), source_text, args)
    (item_dir / "prompt_for_xhs.md").write_text(xhs_prompt, encoding="utf-8")
    note = safe_generate_text(xhs_prompt, args, "Xiaohongshu note")
    (item_dir / "note.md").write_text(note, encoding="utf-8")
    wechat_prompt = build_wechat_prompt(Path(args.wechat_prompt_template), source_text, args)
    (item_dir / "prompt_for_wechat.md").write_text(wechat_prompt, encoding="utf-8")
    wechat_article = safe_generate_text(wechat_prompt, args, "WeChat article")
    wechat_article = embed_images_in_wechat_article(wechat_article, status.get("images", []), max_images=3)
    (item_dir / "wechat_article.md").write_text(wechat_article, encoding="utf-8")
    title, subtitle = extract_cover_titles(note, fallback_title)
    status["cover_short_title"] = title
    status["cover_subtitle"] = subtitle
    try:
        make_cover(pdf_path, assets_dir / "cover.png", title, subtitle, args.watermark)
        status["cover"] = "assets/cover.png"
    except Exception as exc:
        status["cover_error"] = str(exc)
    status["wechat_article"] = "wechat_article.md"
    (item_dir / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return status


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description="Convert repo PDFs to Xiaohongshu notes and WeChat teaser articles.")
    parser.add_argument("--input-dir", default="pdfs")
    parser.add_argument("--output-dir", default="xhs_notes")
    parser.add_argument("--prompt-template", default="prompts/xhs_report_note_prompt.md")
    parser.add_argument("--wechat-prompt-template", default="prompts/wechat_report_article_prompt.md")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--mineru-model", default="vlm")
    parser.add_argument("--language", default="en")
    parser.add_argument("--ocr", default="true")
    parser.add_argument("--style", default="投研博主风：信息密度高，但像给朋友讲逻辑")
    parser.add_argument("--length", type=int, default=850)
    parser.add_argument("--wechat-length", type=int, default=1200)
    parser.add_argument("--community-cta", default="加入社群，领取完整研报解读与原始图表。")
    parser.add_argument("--emoji", default="中")
    parser.add_argument("--hashtags", default="#研报解读 #投资学习 #财经 #小红书笔记")
    parser.add_argument("--disclaimer", action="store_true", default=True)
    parser.add_argument("--max-images", type=int, default=8)
    parser.add_argument("--prompt-chars", type=int, default=24000)
    parser.add_argument("--wechat-prompt-chars", type=int, default=26000)
    parser.add_argument("--poll-timeout", type=int, default=1800)
    parser.add_argument("--poll-interval", type=int, default=15)
    parser.add_argument("--watermark", default="Kris笔记")
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    try:
        token = os.getenv("MINER_U") or os.getenv("MINERU_API_KEY")
        if not token:
            raise RuntimeError("Missing MinerU token. Please add repo secret MINER_U.")
        input_dir = Path(args.input_dir).resolve()
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        pdfs = find_pdfs(input_dir, output_dir)
        if not pdfs:
            raise RuntimeError(f"No PDF files found under {input_dir}")
        log(f"Found {len(pdfs)} PDFs.")
        batch_id, data_id_to_pdf = submit_to_mineru(pdfs, input_dir, token, args)
        log(f"MinerU batch_id={batch_id}")
        rows = poll_mineru(batch_id, token, args.poll_timeout, args.poll_interval)
        summary = []
        for row in rows:
            pdf_path = data_id_to_pdf.get(row.get("data_id"))
            if not pdf_path:
                file_name = row.get("file_name") or row.get("name") or ""
                pdf_path = next((pdf for pdf in pdfs if slug(pdf.name) == slug(file_name)), None)
            if not pdf_path:
                summary.append({"mineru_row": row, "error": "Could not map MinerU result row back to a repo PDF."})
                continue
            summary.append(process_pdf(pdf_path, row, output_dir, args))
        (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        log(f"Done. Results written to {output_dir}")
        return 0
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
