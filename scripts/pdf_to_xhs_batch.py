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
from typing import Any, NamedTuple

import fitz
import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps, ImageStat

SCRIPT_DIR = Path(__file__).resolve().parent
if str(SCRIPT_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPT_DIR))

try:
    from institution_names import ensure_title_has_institution, infer_institution_name
except Exception:  # pragma: no cover
    def infer_institution_name(*_values: Any) -> str:
        return ""

    def ensure_title_has_institution(title: str, _institution: str) -> str:
        return title

MINERU_BASE_URL = "https://mineru.net"
IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".webp", ".bmp"}
DONE_STATES = {"done", "success", "completed"}
FAILED_STATES = {"failed", "fail", "error"}
XHS_CANVAS_SIZE = (1080, 1440)
XHS_BG_COLOR = (9, 31, 64)
XHS_CARD_COLOR = (255, 255, 255)
XHS_WATERMARK = "KC桌面"
CHART_FILENAME_RE = re.compile(r"(?:chart|figure|fig|exhibit|table|graph|plot|source_image)", re.I)
NON_CHART_FILENAME_RE = re.compile(r"(?:avatar|author|headshot|portrait|profile|logo|cover|hero|banner|photo)", re.I)


class MinerUAttemptResult(NamedTuple):
    rows: list[dict[str, Any]]
    data_id_to_pdf: dict[str, Path]
    timed_out: bool
    error: str
    token_label: str


def log(message: str) -> None:
    print(message, flush=True)


def slug(value: str) -> str:
    value = Path(value).name
    value = re.sub(r"\.pdf$", "", value, flags=re.IGNORECASE)
    value = re.sub(r"[^A-Za-z0-9._-]+", "-", value).strip("-._")
    return value[:80] or "report"


def mineru_headers(token: str) -> dict[str, str]:
    return {"Content-Type": "application/json", "Authorization": f"Bearer {token}"}


def split_secret_tokens(value: str | None) -> list[str]:
    if not value:
        return []
    return [part.strip() for part in re.split(r"[\n,;]+", value) if part.strip()]


def mineru_tokens_from_env() -> list[tuple[str, str]]:
    tokens: list[tuple[str, str]] = []
    seen: set[str] = set()
    for env_name in ["MINER_U_KEYS", "MINER_U_2", "MINER_U", "MINERU_API_KEY"]:
        parts = split_secret_tokens(os.getenv(env_name))
        for index, token in enumerate(parts, 1):
            if token in seen:
                continue
            seen.add(token)
            label = env_name if len(parts) == 1 else f"{env_name}_{index}"
            tokens.append((label, token))
    return tokens


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


def mineru_row_has_progress(row: dict[str, Any]) -> bool:
    state = str(row.get("state", "")).lower()
    return state in DONE_STATES or state in FAILED_STATES or state == "running" or bool(row.get("full_zip_url") or row.get("extract_progress"))


def poll_mineru(batch_id: str, token: str, timeout_seconds: int, interval_seconds: int, no_progress_timeout_seconds: int) -> tuple[list[dict[str, Any]], bool]:
    started_at = time.time()
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
            return rows, False
        if (
            no_progress_timeout_seconds > 0
            and rows
            and not any(mineru_row_has_progress(row) for row in rows)
            and time.time() - started_at >= no_progress_timeout_seconds
        ):
            log(
                f"MinerU batch {batch_id} had no parsing progress after "
                f"{no_progress_timeout_seconds}s; switching token/retry path."
            )
            return rows, True
        time.sleep(interval_seconds)

    rows = (last_response or {}).get("data", {}).get("extract_result") or []
    done_count = sum(1 for row in rows if str(row.get("state", "")).lower() in DONE_STATES and row.get("full_zip_url"))
    if done_count:
        log(
            f"MinerU batch {batch_id} timed out after {timeout_seconds}s; "
            f"continuing with {done_count}/{len(rows)} completed PDF(s)."
        )
        return rows, True
    log(
        f"MinerU batch {batch_id} timed out after {timeout_seconds}s with no completed PDFs. "
        f"Last response: {json.dumps(last_response, ensure_ascii=False)[:1000]}"
    )
    return rows, True


def is_successful_mineru_row(row: dict[str, Any]) -> bool:
    return str(row.get("state", "")).lower() in DONE_STATES and bool(row.get("full_zip_url"))


def run_mineru_attempt(pdfs: list[Path], input_dir: Path, token: str, token_label: str, args: argparse.Namespace, attempt: int) -> MinerUAttemptResult:
    try:
        batch_id, data_id_to_pdf = submit_to_mineru(pdfs, input_dir, token, args)
        log(f"MinerU attempt {attempt} using {token_label} batch_id={batch_id}")
        rows, timed_out = poll_mineru(batch_id, token, args.poll_timeout, args.poll_interval, args.mineru_no_progress_timeout)
        return MinerUAttemptResult(rows=rows, data_id_to_pdf=data_id_to_pdf, timed_out=timed_out, error="", token_label=token_label)
    except Exception as exc:
        log(f"MinerU attempt {attempt} using {token_label} failed before usable results: {exc}")
        return MinerUAttemptResult(rows=[], data_id_to_pdf={}, timed_out=False, error=str(exc), token_label=token_label)


def map_mineru_row_to_pdf(row: dict[str, Any], data_id_to_pdf: dict[str, Path], pdfs: list[Path]) -> Path | None:
    pdf_path = data_id_to_pdf.get(row.get("data_id"))
    if pdf_path:
        return pdf_path
    file_name = row.get("file_name") or row.get("name") or ""
    return next((pdf for pdf in pdfs if slug(pdf.name) == slug(file_name)), None)


def collect_successful_rows(
    attempt_result: MinerUAttemptResult,
    pdfs: list[Path],
    successful_rows: dict[Path, dict[str, Any]],
    latest_rows: dict[Path, dict[str, Any]],
) -> None:
    for row in attempt_result.rows:
        pdf_path = map_mineru_row_to_pdf(row, attempt_result.data_id_to_pdf, pdfs)
        if not pdf_path:
            continue
        latest_rows[pdf_path] = row
        if is_successful_mineru_row(row):
            successful_rows[pdf_path] = row


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


def image_edge_density(image: Image.Image) -> float:
    gray = image.convert("L").resize((96, 96))
    pixels = list(gray.getdata())
    edges = 0
    total = 0
    width = 96
    for y in range(95):
        row = y * width
        next_row = (y + 1) * width
        for x in range(95):
            current = pixels[row + x]
            if abs(current - pixels[row + x + 1]) > 26 or abs(current - pixels[next_row + x]) > 26:
                edges += 1
            total += 1
    return edges / max(1, total)


def chart_image_score(path: Path) -> tuple[int, str]:
    image = safe_open_image(path)
    if image is None:
        return -100, "unreadable"
    width, height = image.size
    area = width * height
    ratio = width / max(1, height)
    if width < 320 or height < 180 or area < 100_000:
        return -100, f"too_small:{width}x{height}"

    score = 0
    reasons: list[str] = []
    if CHART_FILENAME_RE.search(path.name):
        score += 2
        reasons.append("chart_filename")
    if NON_CHART_FILENAME_RE.search(path.name):
        score -= 4
        reasons.append("non_chart_filename")
    if 1.05 <= ratio <= 3.8:
        score += 1
        reasons.append("chart_ratio")
    if 0.72 <= ratio <= 1.35 and not CHART_FILENAME_RE.search(path.name):
        score -= 3
        reasons.append("square_without_chart_hint")
    if ratio < 0.38 or ratio > 4.8:
        score -= 3
        reasons.append(f"odd_ratio:{ratio:.2f}")
    density = image_edge_density(image)
    if density >= 0.10:
        score += 2
        reasons.append(f"edge:{density:.2f}")
    elif density < 0.045:
        score -= 2
        reasons.append(f"low_edge:{density:.2f}")
    stat = ImageStat.Stat(image.convert("L").resize((80, 80)))
    if stat.stddev and stat.stddev[0] > 34:
        score += 1
        reasons.append("contrast")
    if area >= 350_000:
        score += 1
        reasons.append("large")
    return score, ",".join(reasons)


def select_chart_images(images: list[Path], max_images: int) -> list[Path]:
    scored: list[tuple[int, int, Path, str]] = []
    for path in images:
        score, reason = chart_image_score(path)
        if score >= 3:
            scored.append((score, path.stat().st_size, path, reason))
        else:
            log(f"Skip non-chart visual asset {path.name}: score={score};{reason}")
    scored.sort(key=lambda item: (item[0], item[1]), reverse=True)
    return [path for _score, _size, path, _reason in scored[:max_images]]


def draw_centered_text(draw: ImageDraw.ImageDraw, text: str, y: int, font: ImageFont.ImageFont, fill: tuple[int, int, int, int] | tuple[int, int, int], max_chars: int = 12, line_gap: int = 18) -> int:
    text = re.sub(r"\s+", " ", text).strip()
    if not text:
        return y
    lines = [text[i : i + max_chars] for i in range(0, len(text), max_chars)]
    for line in lines[:4]:
        bbox = draw.textbbox((0, 0), line, font=font)
        x = (XHS_CANVAS_SIZE[0] - (bbox[2] - bbox[0])) // 2
        draw.text((x, y), line, font=font, fill=fill)
        y += bbox[3] - bbox[1] + line_gap
    return y


def draw_kc_watermark(draw: ImageDraw.ImageDraw) -> None:
    watermark_font = load_kai_font(38)
    bbox = draw.textbbox((0, 0), XHS_WATERMARK, font=watermark_font)
    text_w = bbox[2] - bbox[0]
    text_h = bbox[3] - bbox[1]
    draw.text(((XHS_CANVAS_SIZE[0] - text_w) // 2, XHS_CANVAS_SIZE[1] - text_h - 46), XHS_WATERMARK, font=watermark_font, fill=(226, 234, 246, 150))


def draw_title_card(title: str, target_path: Path) -> None:
    """Create the first Xiaohongshu card with the report title."""
    canvas = Image.new("RGB", XHS_CANVAS_SIZE, XHS_BG_COLOR).convert("RGBA")
    draw = ImageDraw.Draw(canvas)

    title = re.sub(r"[《》#>*\-]+", "", title).strip() or "研报速览"
    title_font = load_font(78, bold=True)
    subtitle_font = load_font(34, bold=False)
    small_font = load_kai_font(32)

    # Soft title card block.
    block = (92, 430, 988, 860)
    shadow = Image.new("RGBA", XHS_CANVAS_SIZE, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((block[0] + 12, block[1] + 18, block[2] + 12, block[3] + 18), radius=44, fill=(0, 0, 0, 90))
    shadow = shadow.filter(ImageFilter.GaussianBlur(18))
    canvas = Image.alpha_composite(canvas, shadow)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(block, radius=44, fill=(255, 255, 255, 232))

    draw_centered_text(draw, title, 545, title_font, fill=(15, 29, 48, 255), max_chars=9, line_gap=20)
    subtitle = "研报图表速览"
    bbox = draw.textbbox((0, 0), subtitle, font=subtitle_font)
    draw.text(((XHS_CANVAS_SIZE[0] - (bbox[2] - bbox[0])) // 2, 770), subtitle, font=subtitle_font, fill=(78, 93, 112, 255))

    hint = "向右滑动查看图表 →"
    bbox = draw.textbbox((0, 0), hint, font=small_font)
    draw.text(((XHS_CANVAS_SIZE[0] - (bbox[2] - bbox[0])) // 2, 1068), hint, font=small_font, fill=(218, 230, 246, 190))
    draw_kc_watermark(draw)

    target_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(target_path, quality=94)


def draw_chart_badge(draw: ImageDraw.ImageDraw, number: int) -> None:
    badge_font = load_font(40, bold=True)
    cx, cy, r = 102, 100, 44
    draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 230))
    text = str(number)
    bbox = draw.textbbox((0, 0), text, font=badge_font)
    draw.text((cx - (bbox[2] - bbox[0]) / 2, cy - (bbox[3] - bbox[1]) / 2 - 4), text, font=badge_font, fill=(9, 31, 64, 255))


def draw_next_arrow(draw: ImageDraw.ImageDraw) -> None:
    arrow_font = load_font(70, bold=True)
    arrow = "→"
    bbox = draw.textbbox((0, 0), arrow, font=arrow_font)
    x = XHS_CANVAS_SIZE[0] - 112
    y = XHS_CANVAS_SIZE[1] // 2 - (bbox[3] - bbox[1]) // 2
    draw.rounded_rectangle((x - 18, y - 12, x + 74, y + 82), radius=32, fill=(255, 255, 255, 42))
    draw.text((x, y), arrow, font=arrow_font, fill=(226, 234, 246, 210))


def draw_xhs_chart_card(image: Image.Image, target_path: Path, chart_number: int, show_next_arrow: bool) -> None:
    """Pad source chart on a clean deep-blue 1080x1440 canvas with chart number and optional right arrow."""
    canvas = Image.new("RGB", XHS_CANVAS_SIZE, XHS_BG_COLOR)
    image = ImageOps.contain(image.convert("RGB"), (930, 1120), method=Image.Resampling.LANCZOS)
    image_x = (XHS_CANVAS_SIZE[0] - image.width) // 2
    image_y = (XHS_CANVAS_SIZE[1] - image.height) // 2 - 28
    image_y = max(118, image_y)

    margin = 28
    card_box = (
        max(36, image_x - margin),
        max(110, image_y - margin),
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
    draw_chart_badge(draw, chart_number)
    if show_next_arrow:
        draw_next_arrow(draw)
    draw_kc_watermark(draw)

    target_path.parent.mkdir(parents=True, exist_ok=True)
    canvas_rgba.convert("RGB").save(target_path, quality=94)


def pad_image_for_xhs(source_path: Path, target_path: Path, chart_number: int, show_next_arrow: bool) -> bool:
    image = safe_open_image(source_path)
    if image is None:
        return False
    draw_xhs_chart_card(image, target_path, chart_number=chart_number, show_next_arrow=show_next_arrow)
    return True


def render_pdf_page_cards(pdf_path: Path, assets_dir: Path, max_pages: int, title: str) -> list[str]:
    cards: list[str] = []
    draw_title_card(title, assets_dir / "xhs_card_01.png")
    cards.append("assets/xhs_card_01.png")
    try:
        doc = fitz.open(pdf_path)
    except Exception as exc:
        log(f"Cannot open PDF for fallback image cards: {pdf_path}: {exc}")
        return cards
    try:
        page_count = min(max_pages, len(doc))
        for index in range(page_count):
            pix = doc[index].get_pixmap(matrix=fitz.Matrix(1.8, 1.8), alpha=False)
            image = Image.open(BytesIO(pix.tobytes("png"))).convert("RGB")
            target = assets_dir / f"xhs_card_{index + 2:02d}.png"
            draw_xhs_chart_card(image, target, chart_number=index + 1, show_next_arrow=index < page_count - 1)
            cards.append(str(target.relative_to(assets_dir.parent)))
    finally:
        doc.close()
    return cards


def create_visual_assets(result_dir: Path, pdf_path: Path, assets_dir: Path, max_images: int, title: str) -> list[str]:
    """Create stable Xiaohongshu image cards.

    xhs_card_01.png is always a title card.
    xhs_card_02.png and later are chart cards with 1/2/3... badges and right arrows until the last chart.
    """
    assets_dir.mkdir(parents=True, exist_ok=True)
    images = [p for p in result_dir.rglob("*") if p.is_file() and p.suffix.lower() in IMAGE_SUFFIXES]
    cards: list[str] = []

    if images:
        draw_title_card(title, assets_dir / "xhs_card_01.png")
        cards.append("assets/xhs_card_01.png")
        chart_images = select_chart_images(images, max_images)
        if not chart_images:
            log("MinerU images did not look like charts; keeping only the title card and letting downstream AI fill body images.")
            return cards
        total = len(chart_images)
        for index, image in enumerate(chart_images, 1):
            original_target = assets_dir / f"source_image_{index:02d}{image.suffix.lower()}"
            shutil.copy2(image, original_target)
            card_target = assets_dir / f"xhs_card_{index + 1:02d}.png"
            if pad_image_for_xhs(image, card_target, chart_number=index, show_next_arrow=index < total):
                cards.append(str(card_target.relative_to(assets_dir.parent)))
            else:
                cards.append(str(original_target.relative_to(assets_dir.parent)))
    else:
        log("MinerU result contained no standalone chart images; creating title card only.")
        draw_title_card(title, assets_dir / "xhs_card_01.png")
        cards.append("assets/xhs_card_01.png")
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
    disclaimer = "不要写免责声明，不要出现‘投资’或‘非投资建议’。"
    tags = "末尾只允许保留一个话题标签：#学习笔记。不要输出任何其他标签。"
    return template_path.read_text(encoding="utf-8").format(
        style_preset=args.style,
        target_length=args.length,
        emoji_density=args.emoji,
        disclaimer_rule=disclaimer,
        hashtag_rule=tags,
        source_text=source_text,
    )


def build_wechat_prompt(template_path: Path, source_text: str, args: argparse.Namespace, institution_name: str = "") -> str:
    source_text = trim_source_text(source_text, args.wechat_prompt_chars)
    return template_path.read_text(encoding="utf-8").format(
        target_length=args.wechat_length,
        community_cta=args.community_cta,
        institution_name=institution_name or "可从报告标题识别的机构中文名",
        source_text=source_text,
    )


def ensure_markdown_h1_institution(markdown: str, institution_name: str) -> str:
    if not institution_name:
        return markdown
    lines = markdown.splitlines()
    for index, raw in enumerate(lines):
        stripped = raw.strip()
        if stripped.startswith("# "):
            title = re.sub(r"^#\s*", "", stripped).strip()
            updated = ensure_title_has_institution(title, institution_name)
            if updated != title:
                lines[index] = f"# {updated}"
            return "\n".join(lines)
    return markdown


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return f"未检测到 DEEPSEEK_API_KEY。请复制对应 prompt 文件到 DeepSeek 中生成：{label}。\n"
    url = args.deepseek_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": args.model,
        "temperature": 0.7,
        "messages": [
            {"role": "system", "content": "你是严谨但有传播力的中文内容编辑，输出必须可直接发布。"},
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


def visible_char_count(text: str) -> int:
    return len(re.sub(r"\s+", "", text or ""))


def truncate_visible_text(text: str, max_chars: int, suffix: str = "…") -> str:
    if max_chars <= 0 or visible_char_count(text) <= max_chars:
        return text
    budget = max(1, max_chars - visible_char_count(suffix))
    kept: list[str] = []
    used = 0
    for char in text:
        if char.isspace():
            kept.append(char)
            continue
        if used >= budget:
            break
        kept.append(char)
        used += 1
    return "".join(kept).rstrip("，,。；;：:\n ") + suffix


def limit_xhs_note_length(note: str, max_chars: int) -> str:
    if max_chars <= 0 or visible_char_count(note) <= max_chars:
        return note
    text = note.strip()
    tag = "#学习笔记"
    body = re.sub(r"(?:^|\n)\s*#学习笔记\s*$", "", text).strip()
    tag_budget = visible_char_count(tag)
    body_budget = max(120, max_chars - tag_budget)
    limited = truncate_visible_text(body, body_budget)
    return limited.strip() + "\n\n#学习笔记\n"


def clean_xhs_note(note: str) -> str:
    """Post-process note.md so it is directly publishable on XHS."""
    text = note.strip()
    # Remove explicit framework labels / thinking-process headings.
    banned_heading_patterns = [
        r"^\s*#+\s*(一句话结论|我最想提醒的一点|配图建议|免责声明)\s*[:：]?.*$",
        r"^\s*(一句话结论|我最想提醒的一点|配图建议|免责声明)\s*[:：].*$",
    ]
    lines = []
    skip_after_image_suggestion = False
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            if not skip_after_image_suggestion:
                lines.append(line)
            continue
        if re.match(r"^#+\s*配图建议\s*[:：]?$", stripped) or re.match(r"^配图建议\s*[:：]", stripped):
            skip_after_image_suggestion = True
            continue
        if skip_after_image_suggestion:
            # Once 配图建议 starts, drop everything after it. We will append #学习笔记 later.
            continue
        if any(re.match(pattern, stripped, flags=re.IGNORECASE) for pattern in banned_heading_patterns):
            # Preserve the content after colon when a line is like “一句话结论：xxx”.
            if "：" in stripped or ":" in stripped:
                content = re.split(r"[:：]", stripped, 1)[-1].strip()
                if content and content not in {"一句话结论", "我最想提醒的一点", "配图建议", "免责声明"}:
                    lines.append(content)
            continue
        if re.search(r"非\s*投资\s*建议|仅\s*(?:做|作|供)?\s*学习交流|不构成.*投资", stripped):
            continue
        lines.append(line)
    text = "\n".join(lines).strip()

    # Remove hashtags line(s), then append only #学习笔记.
    text = re.sub(r"(?:^|\n)\s*(?:#[^\n#\s]+\s*)+\s*$", "", text, flags=re.MULTILINE).strip()
    text = re.sub(r"#(?:投资学习|财经|金融|股票|基金|理财|研报解读|小红书笔记|笔记分享|干货分享)\b", "", text)
    # Remove remaining disallowed disclaimer phrases wherever they appear.
    text = re.sub(r"非\s*投资\s*建议[，,。；;\s]*", "", text)
    text = re.sub(r"仅\s*(?:做|作|供)?\s*学习交流[，,。；;\s]*", "", text)
    text = re.sub(r"不构成[^\n。；;]*投资[^\n。；;]*[。；;]?", "", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    return text + "\n\n#学习笔记\n"


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
    state = str(result_row.get("state", "")).lower()
    fallback_title = slug(pdf_path.name)[:18]
    status: dict[str, Any] = {
        "source_pdf": str(pdf_path),
        "mineru_state": result_row.get("state"),
        "mineru_error": result_row.get("err_msg") or result_row.get("error") or "",
    }
    if state not in DONE_STATES or not result_row.get("full_zip_url"):
        status["error"] = "MinerU did not return a successful full_zip_url for this PDF."
        log(f"Skipping incomplete MinerU result for {pdf_path.name}: state={result_row.get('state')}")
        return status

    item_dir = output_root / slug(pdf_path.name)
    raw_dir = item_dir / "mineru_raw"
    assets_dir = item_dir / "assets"
    item_dir.mkdir(parents=True, exist_ok=True)
    download_and_unzip(result_row["full_zip_url"], raw_dir)
    markdown_path = find_markdown(raw_dir)
    if not markdown_path:
        status["images"] = create_visual_assets(raw_dir, pdf_path, assets_dir, args.max_images, title=fallback_title)
        status["error"] = "MinerU result zip did not contain markdown. Visual cards may still have been generated."
        (item_dir / "status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return status
    source_text = markdown_path.read_text(encoding="utf-8", errors="ignore")
    (item_dir / "source_mineru.md").write_text(source_text, encoding="utf-8")
    institution_name = infer_institution_name(pdf_path.name, status.get("source_pdf"), source_text[:2000])
    if institution_name:
        status["institution_name"] = institution_name
    xhs_prompt = build_xhs_prompt(Path(args.prompt_template), source_text, args)
    (item_dir / "prompt_for_xhs.md").write_text(xhs_prompt, encoding="utf-8")
    note = safe_generate_text(xhs_prompt, args, "Xiaohongshu note")
    note = clean_xhs_note(note)
    note = limit_xhs_note_length(note, args.length)
    (item_dir / "note.md").write_text(note, encoding="utf-8")
    title, subtitle = extract_cover_titles(note, fallback_title)
    status["cover_short_title"] = title
    status["cover_subtitle"] = subtitle
    status["images"] = create_visual_assets(raw_dir, pdf_path, assets_dir, args.max_images, title=title)
    wechat_prompt = build_wechat_prompt(Path(args.wechat_prompt_template), source_text, args, institution_name)
    (item_dir / "prompt_for_wechat.md").write_text(wechat_prompt, encoding="utf-8")
    wechat_article = safe_generate_text(wechat_prompt, args, "WeChat article")
    wechat_article = ensure_markdown_h1_institution(wechat_article, institution_name)
    wechat_article = embed_images_in_wechat_article(wechat_article, status.get("images", []), max_images=3)
    (item_dir / "wechat_article.md").write_text(wechat_article, encoding="utf-8")
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
    parser.add_argument("--length", type=int, default=1000)
    parser.add_argument("--wechat-length", type=int, default=1200)
    parser.add_argument("--community-cta", default="加入社群，领取完整研报解读与原始图表。")
    parser.add_argument("--emoji", default="中")
    parser.add_argument("--hashtags", default="#学习笔记")
    parser.add_argument("--disclaimer", action="store_true", default=False)
    parser.add_argument("--max-images", type=int, default=8)
    parser.add_argument("--prompt-chars", type=int, default=24000)
    parser.add_argument("--wechat-prompt-chars", type=int, default=26000)
    parser.add_argument("--poll-timeout", type=int, default=3600)
    parser.add_argument("--poll-interval", type=int, default=15)
    parser.add_argument("--mineru-retries", type=int, default=1, help="Retry incomplete/failed MinerU PDFs this many times.")
    parser.add_argument("--mineru-no-progress-timeout", type=int, default=600, help="Switch token/retry path if MinerU rows stay pending with no progress this long.")
    parser.add_argument("--watermark", default=XHS_WATERMARK)
    return parser


def main() -> int:
    args = build_arg_parser().parse_args()
    try:
        mineru_tokens = mineru_tokens_from_env()
        if not mineru_tokens:
            raise RuntimeError("Missing MinerU token. Please add repo secret MINER_U.")
        input_dir = Path(args.input_dir).resolve()
        output_dir = Path(args.output_dir).resolve()
        output_dir.mkdir(parents=True, exist_ok=True)
        pdfs = find_pdfs(input_dir, output_dir)
        if not pdfs:
            raise RuntimeError(f"No PDF files found under {input_dir}")
        log(f"Found {len(pdfs)} PDFs. MinerU token slots available={len(mineru_tokens)}.")
        max_rounds = max(1, int(args.mineru_retries) + 1)
        remaining_pdfs = list(pdfs)
        successful_rows: dict[Path, dict[str, Any]] = {}
        latest_rows: dict[Path, dict[str, Any]] = {}
        attempt_summaries: list[dict[str, Any]] = []
        mineru_timed_out = False
        attempt = 0
        for round_index in range(1, max_rounds + 1):
            for token_label, token in mineru_tokens:
                if not remaining_pdfs:
                    break
                attempt += 1
                max_attempts = max_rounds * len(mineru_tokens)
                log(
                    f"MinerU attempt {attempt}/{max_attempts} using {token_label}: "
                    f"submitting {len(remaining_pdfs)} PDF(s)."
                )
                attempt_result = run_mineru_attempt(remaining_pdfs, input_dir, token, token_label, args, attempt)
                mineru_timed_out = mineru_timed_out or attempt_result.timed_out
                collect_successful_rows(attempt_result, remaining_pdfs, successful_rows, latest_rows)
                success_count = sum(1 for pdf in remaining_pdfs if pdf in successful_rows)
                retry_pdfs = [pdf for pdf in remaining_pdfs if pdf not in successful_rows]
                attempt_summaries.append({
                    "attempt": attempt,
                    "round": round_index,
                    "token_label": attempt_result.token_label,
                    "submitted_pdf_count": len(remaining_pdfs),
                    "successful_pdf_count": success_count,
                    "retry_pdf_count": len(retry_pdfs),
                    "timed_out": attempt_result.timed_out,
                    "error": attempt_result.error,
                    "states": [
                        {
                            "pdf": str(map_mineru_row_to_pdf(row, attempt_result.data_id_to_pdf, remaining_pdfs) or ""),
                            "state": row.get("state"),
                            "error": row.get("err_msg") or row.get("error") or "",
                        }
                        for row in attempt_result.rows
                    ],
                })
                if retry_pdfs:
                    log(f"{len(retry_pdfs)} PDF(s) remain incomplete after attempt {attempt}.")
                remaining_pdfs = retry_pdfs
            if not remaining_pdfs:
                break

        summary: list[dict[str, Any]] = []
        successful_reports = 0
        for pdf_path in pdfs:
            row = successful_rows.get(pdf_path)
            if not row:
                last_row = latest_rows.get(pdf_path, {})
                status = {
                    "source_pdf": str(pdf_path),
                    "mineru_state": last_row.get("state") or "not_returned",
                    "mineru_error": last_row.get("err_msg") or last_row.get("error") or "",
                    "error": f"MinerU did not finish successfully after {attempt} attempt(s).",
                }
                log(f"Skipping PDF after MinerU retry exhaustion: {pdf_path.name}")
                summary.append(status)
                continue
            status = process_pdf(pdf_path, row, output_dir, args)
            summary.append(status)
            if not status.get("error") and status.get("wechat_article") == "wechat_article.md":
                successful_reports += 1
        (output_dir / "summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
        (output_dir / "mineru_attempts_summary.json").write_text(
            json.dumps(attempt_summaries, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )
        log(
            f"Done. Results written to {output_dir}; "
            f"successful_reports={successful_reports}; mineru_timed_out={mineru_timed_out}; "
            f"mineru_attempts={len(attempt_summaries)}"
        )
        return 0 if successful_reports else 2
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
