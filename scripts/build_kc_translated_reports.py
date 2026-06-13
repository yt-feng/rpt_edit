#!/usr/bin/env python3
"""Build branded Chinese translation PDFs from existing MinerU outputs.

Input is the post-MinerU report folders created by the XHS shard workflow:

  xhs_notes/dropbox/<date>/shard_*/<report>/source_mineru.md

The script strips front-matter author/contact blocks and trailing disclosure
appendices, keeps body text plus chart/image references, translates the cleaned
Markdown to Chinese with DeepSeek, and renders one branded PDF per report.
"""
from __future__ import annotations

import argparse
import html
import json
import os
import re
import shutil
import sys
import time
from pathlib import Path
from typing import Any

import requests

try:
    from finalize_outputs import sanitize_text
except Exception:  # pragma: no cover
    def sanitize_text(text: str) -> str:
        return text

try:  # Loaded lazily so --help and cleaning logic work without reportlab installed.
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Image as RLImage
    from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer
except Exception:  # pragma: no cover
    colors = None
    TA_CENTER = None
    A4 = None
    ParagraphStyle = None
    getSampleStyleSheet = None
    cm = None
    pdfmetrics = None
    UnicodeCIDFont = None
    TTFont = None
    RLImage = None
    Paragraph = None
    SimpleDocTemplate = None
    Spacer = None


BRAND = "KC桌面——外资精译"
PDF_WATERMARK = "公众号：KC桌面"
PDF_WATERMARK_COLOR = "#0B3B75"
PDF_FOOTER_DISCLAIMER = "For informational purposes only. Not investment advice."
DATE_DIR_RE = re.compile(r"^\d{6,8}$")
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^\)]+)\)")
IMAGE_TOKEN_RE = re.compile(r"\[\[KC_IMAGE_(\d{3})\]\]")
EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PHONE_RE = re.compile(r"(?:\+?\d[\d\s().-]{7,}\d)")
TABLE_LINE_RE = re.compile(r"^\s*\|.*\|\s*$")
TABLE_SEP_RE = re.compile(r"^\s*\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?\s*$")
AUTHOR_NAME_RE = re.compile(r"^[A-Z][A-Za-z.'-]+(?:\s+[A-Z][A-Za-z.'-]+){1,3}$")
COPYRIGHT_RE = re.compile(r"(?:©|copyright|all rights reserved|no redistribution|without .*written permission)", re.I)
DISCLOSURE_RE = re.compile(
    r"^\s*(?:#+\s*)?(?:"
    r"important disclosures?|disclosure appendix|disclosures?|disclaimer|"
    r"analyst certification|regulatory disclosures?|required disclosures?|"
    r"disclosure section|important disclosure information|"
    r"conflicts? of interest|ratings definitions?|legal entity disclosures?|"
    r"global research disclosures?|distribution of ratings"
    r")\b",
    re.I,
)
DISCLOSURE_BODY_RE = re.compile(
    r"(?:analysts? are compensated|to our readers in|this publication is being distributed|"
    r"registered with the|authorised and regulated|registration granted by sebi|"
    r"investments in securities market are subject to market risks|"
    r"does and seeks to do business with companies covered|"
    r"conflict of interest that could affect the objectivity|"
    r"analyst certification and other important disclosures|"
    r"MS Disclosure Website|investment representative)",
    re.I,
)
NOISE_LINE_RE = re.compile(
    r"(?:global investment research|equity research|research analyst|"
    r"please see important disclosures|continued on (?:the )?next page|"
    r"MS ASIA LIMITED|Industry View|^Attractive$|"
    r"related report:)",
    re.I,
)


def log(message: str) -> None:
    print(message, flush=True)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", sanitize_text(text or "")).strip()


def slug(value: str, max_len: int = 96) -> str:
    base = Path(value).stem if "." in value else value
    base = re.sub(r"[^A-Za-z0-9._-]+", "-", base).strip("-._")
    return (base or "report")[:max_len]


def latest_date_dir(root: Path) -> Path:
    if not root.exists():
        raise RuntimeError(f"Dropbox output root not found: {root}")
    candidates = [p for p in root.iterdir() if p.is_dir() and DATE_DIR_RE.match(p.name)]
    if not candidates:
        raise RuntimeError(f"No date-named folders found under {root}")
    return max(candidates, key=lambda p: int(p.name))


def parse_selection_limit(value: str, label: str) -> int | None:
    normalized = str(value or "").strip().lower()
    if normalized in {"all", "*"}:
        return None
    try:
        limit = int(normalized)
    except ValueError as exc:
        raise ValueError(f"{label} must be a positive integer or 'all'") from exc
    if limit < 1:
        raise ValueError(f"{label} must be at least 1, or use 'all'")
    return limit


def find_report_dirs(date_dir: Path) -> list[Path]:
    report_dirs: list[Path] = []
    for shard in sorted(date_dir.glob("shard_*"), key=lambda p: p.name):
        if not shard.is_dir():
            continue
        for item in sorted(shard.iterdir(), key=lambda p: p.name):
            if item.is_dir() and (item / "source_mineru.md").exists():
                report_dirs.append(item)
    for item in sorted(date_dir.iterdir(), key=lambda p: p.name):
        if item.is_dir() and (item / "source_mineru.md").exists():
            report_dirs.append(item)

    seen: set[str] = set()
    unique: list[Path] = []
    for path in report_dirs:
        key = str(path.resolve())
        if key not in seen:
            seen.add(key)
            unique.append(path)
    return unique


def report_title(report_dir: Path) -> str:
    for filename in ["wechat_article.md", "note.md", "source_mineru.md"]:
        path = report_dir / filename
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if line.startswith("# "):
                title = re.sub(r"^#+\s*", "", line).strip()
                if title:
                    return sanitize_text(title[:140])
    status_path = report_dir / "status.json"
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
            source_pdf = status.get("source_pdf") or ""
            if source_pdf:
                return sanitize_text(Path(source_pdf).stem[:140])
        except Exception:
            pass
    return sanitize_text(report_dir.name.replace("-", " ")[:140])


def resolve_image_path(markdown_path: Path, image_ref: str) -> Path | None:
    ref = image_ref.strip().strip("<>")
    if ref.startswith("http://") or ref.startswith("https://"):
        return None
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    for candidate in [
        markdown_path.parent / ref,
        markdown_path.parent / "mineru_raw" / ref,
        markdown_path.parent.parent / ref,
    ]:
        if candidate.exists() and candidate.is_file():
            return candidate
    basename = Path(ref).name
    for candidate in markdown_path.parent.rglob(basename):
        if candidate.is_file():
            return candidate
    return None


def find_disclosure_start(lines: list[str]) -> int:
    if not lines:
        return 0
    minimum_index = max(12, len(lines) // 3)
    for idx, raw in enumerate(lines):
        line = raw.strip()
        if idx < minimum_index:
            continue
        normalized = re.sub(r"^#+\s*", "", line)
        normalized = re.sub(r"^(?:[IVXLCDM]+|\d+)[.)]?\s+", "", normalized, flags=re.I)
        if DISCLOSURE_RE.search(normalized) or DISCLOSURE_BODY_RE.search(line):
            return idx
    return len(lines)


def strip_details_blocks(lines: list[str]) -> list[str]:
    cleaned: list[str] = []
    in_details = False
    for raw in lines:
        line = raw.strip().lower()
        if line.startswith("<details"):
            in_details = True
            continue
        if in_details:
            if "</details>" in line:
                in_details = False
            continue
        cleaned.append(raw)
    return cleaned


def is_noise_line(line: str) -> bool:
    text = line.strip()
    if not text:
        return False
    if EMAIL_RE.search(text) or PHONE_RE.search(text):
        return True
    if COPYRIGHT_RE.search(text):
        return True
    if NOISE_LINE_RE.search(text):
        return True
    if TABLE_LINE_RE.match(text) or TABLE_SEP_RE.match(text):
        return True
    if "<lcel>" in text or "<nl>" in text:
        return True
    # Drop obvious name/title-only author lines in the front matter.
    if len(text) < 45 and re.search(r"\b(?:Ph\.?D\.?|CFA|CPA|Analyst|Strategist)\b", text, re.I):
        return True
    if len(text) < 45 and AUTHOR_NAME_RE.match(text) and not re.search(r"\b(?:PMI|Source|Figure|Exhibit|Industry|Index)\b", text):
        return True
    return False


def first_body_line(lines: list[str]) -> int:
    for idx, raw in enumerate(lines):
        line = raw.strip()
        if not line or line.startswith("#") or IMAGE_RE.search(line) or is_noise_line(line):
            continue
        if len(normalize_space(line)) >= 80:
            return idx
    return 0


def collect_initial_headings(lines: list[str], body_start: int) -> list[str]:
    headings: list[str] = []
    for raw in lines[:body_start]:
        line = raw.strip()
        if not line.startswith("#"):
            continue
        if DISCLOSURE_RE.search(line):
            continue
        if len(headings) >= 3:
            break
        headings.append(line)
    return headings


def copy_image_for_report(
    source_markdown: Path,
    image_ref: str,
    assets_dir: Path,
    image_index: int,
) -> tuple[str, dict[str, Any]] | None:
    src = resolve_image_path(source_markdown, image_ref)
    if not src:
        return None
    suffix = src.suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
        return None
    assets_dir.mkdir(parents=True, exist_ok=True)
    if suffix == ".webp":
        target = assets_dir / f"fig_{image_index:03d}.png"
        try:
            from PIL import Image

            Image.open(src).convert("RGB").save(target)
        except Exception:
            target = assets_dir / f"fig_{image_index:03d}.webp"
            shutil.copy2(src, target)
    else:
        target = assets_dir / f"fig_{image_index:03d}{suffix}"
        shutil.copy2(src, target)
    token = f"[[KC_IMAGE_{image_index:03d}]]"
    meta = {"token": token, "source_path": str(src), "path": str(target), "relative_path": str(target.name)}
    return token, meta


def prepare_clean_markdown(report_dir: Path, out_dir: Path, max_images: int) -> tuple[str, list[dict[str, Any]]]:
    source_markdown = report_dir / "source_mineru.md"
    lines = source_markdown.read_text(encoding="utf-8", errors="ignore").splitlines()
    lines = lines[: find_disclosure_start(lines)]
    lines = strip_details_blocks(lines)
    body_start = first_body_line(lines)
    headings = collect_initial_headings(lines, body_start)

    output_lines: list[str] = []
    if headings:
        output_lines.extend(headings)
        output_lines.append("")
    else:
        output_lines.extend([f"# {report_title(report_dir)}", ""])

    assets_dir = out_dir / "assets"
    figures: list[dict[str, Any]] = []
    image_index = 1
    previous_blank = False

    for raw in lines[body_start:]:
        line = raw.rstrip()
        stripped = line.strip()
        if not stripped:
            if not previous_blank:
                output_lines.append("")
                previous_blank = True
            continue
        previous_blank = False

        image_match = IMAGE_RE.search(stripped)
        if image_match:
            if max_images <= 0 or image_index <= max_images:
                copied = copy_image_for_report(source_markdown, image_match.group(1), assets_dir, image_index)
                if copied:
                    token, meta = copied
                    figures.append(meta)
                    output_lines.extend(["", token, ""])
                    image_index += 1
            continue

        if is_noise_line(stripped):
            continue
        if stripped.startswith("<") and stripped.endswith(">"):
            continue
        output_lines.append(stripped)

    clean_md = "\n".join(output_lines)
    clean_md = re.sub(r"\n{4,}", "\n\n\n", clean_md).strip() + "\n"
    return sanitize_text(clean_md), figures


def split_markdown_chunks(markdown: str, max_chars: int) -> list[str]:
    paragraphs = re.split(r"(\n\s*\n)", markdown)
    chunks: list[str] = []
    current = ""
    for part in paragraphs:
        if not part and not current:
            continue
        if current and len(current) + len(part) > max_chars:
            chunks.append(current.strip())
            current = part
        else:
            current += part
    if current.strip():
        chunks.append(current.strip())
    final_chunks: list[str] = []
    for chunk in chunks:
        if len(chunk) <= max_chars * 1.3:
            final_chunks.append(chunk)
            continue
        for start in range(0, len(chunk), max_chars):
            final_chunks.append(chunk[start : start + max_chars])
    return final_chunks


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:1000]}")
    return data


def call_deepseek(prompt: str, args: argparse.Namespace, label: str, temperature: float = 0.15) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    payload: dict[str, Any] = {
        "model": args.model,
        "temperature": temperature,
        "messages": [
            {
                "role": "system",
                "content": (
                    "你是专业金融研报中文精译编辑。忠实翻译，不编造，不输出解释。"
                    "保留 Markdown 结构和图片占位符。"
                ),
            },
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json=payload,
        timeout=args.deepseek_timeout,
    )
    data = parse_json_response(response, label)
    return data["choices"][0]["message"]["content"].strip()


def translate_chunk(chunk: str, args: argparse.Namespace, chunk_index: int, chunk_total: int) -> str:
    prompt = f"""
请把下面这段英文/混合语言研报正文精译成简体中文。

硬性要求：
1. 保留 Markdown 标题、列表、段落结构。
2. 必须原样保留所有形如 [[KC_IMAGE_001]] 的图片占位符，不能改编号、不能删除。
3. 不要摘要，不要扩写，不要增加原文没有的信息。
4. 如果仍出现作者姓名、邮箱、电话、投行免责声明、评级分布、法律披露，请删除。
5. 投行名不要作为标题或署名露出；例如 “CITI'S TAKE” 译为“核心观点”，不要译为“Citi观点”。
6. 公司名、产品名、股票代码可保留英文；分析逻辑、结论、图表标题和注释翻译成自然中文。
7. 只输出译文 Markdown，不要输出代码块，不要解释。

片段：{chunk_index}/{chunk_total}

待翻译内容：
{chunk}
""".strip()
    return call_deepseek(prompt, args, f"translate chunk {chunk_index}/{chunk_total}")


def translate_markdown(markdown: str, args: argparse.Namespace) -> str:
    chunks = split_markdown_chunks(markdown, args.chunk_chars)
    translated: list[str] = []
    for idx, chunk in enumerate(chunks, 1):
        log(f"Translating chunk {idx}/{len(chunks)} ({len(chunk)} chars)")
        last_error: Exception | None = None
        for attempt in range(1, args.deepseek_retries + 1):
            try:
                text = translate_chunk(chunk, args, idx, len(chunks))
                translated.append(text)
                break
            except Exception as exc:
                last_error = exc
                wait = min(60, 5 * attempt)
                log(f"DeepSeek chunk {idx} attempt {attempt} failed: {exc}; retrying in {wait}s")
                time.sleep(wait)
        else:
            raise RuntimeError(f"DeepSeek translation failed for chunk {idx}: {last_error}")
    text = "\n\n".join(translated)
    text = re.sub(r"```(?:markdown)?\s*", "", text)
    text = text.replace("```", "")
    return sanitize_text(text).strip() + "\n"


def register_cjk_font() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception as exc:
        log(f"Could not register STSong-Light CID font: {exc}")
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for path in candidates:
        if not Path(path).exists():
            continue
        try:
            pdfmetrics.registerFont(TTFont("KC_CJK", path))
            return "KC_CJK"
        except Exception as exc:
            log(f"Skip font {path}: {exc}")
    return "Helvetica"


def xml_text(text: str) -> str:
    escaped = html.escape(normalize_space(text), quote=False)
    escaped = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", escaped)
    return escaped


def require_reportlab() -> None:
    if SimpleDocTemplate is None:
        raise RuntimeError("Missing reportlab dependency. Please pip install reportlab.")


def image_flowable(path: Path, max_width: float, max_height: float) -> Any | None:
    if not path.exists():
        return None
    try:
        img = RLImage(str(path))
        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight, 1.0)
        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio
        img.hAlign = "CENTER"
        return img
    except Exception as exc:
        log(f"Skip image {path}: {exc}")
        return None


def normalize_image_token_lines(markdown: str) -> str:
    return IMAGE_TOKEN_RE.sub(lambda m: f"\n[[KC_IMAGE_{m.group(1)}]]\n", markdown)


def first_heading(markdown: str, fallback: str) -> str:
    for raw in markdown.splitlines():
        line = raw.strip()
        if line.startswith("#"):
            title = re.sub(r"^#+\s*", "", line).strip()
            if title:
                return title[:140]
    return fallback[:140]


def build_styles(font: str) -> dict[str, ParagraphStyle]:
    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="KCBrand", fontName=font, fontSize=18, leading=23, alignment=TA_CENTER, textColor=colors.HexColor("#0B3B75"), spaceAfter=10))
    styles.add(ParagraphStyle(name="KCTitle", fontName=font, fontSize=20, leading=27, alignment=TA_CENTER, spaceAfter=14))
    styles.add(ParagraphStyle(name="KCH1", fontName=font, fontSize=15, leading=21, spaceBefore=14, spaceAfter=7, textColor=colors.HexColor("#0B3B75")))
    styles.add(ParagraphStyle(name="KCH2", fontName=font, fontSize=13, leading=19, spaceBefore=11, spaceAfter=6, textColor=colors.HexColor("#1E5A8A")))
    styles.add(ParagraphStyle(name="KCBody", fontName=font, fontSize=10.2, leading=16, spaceAfter=6))
    styles.add(ParagraphStyle(name="KCBullet", fontName=font, fontSize=10.2, leading=16, leftIndent=0.45 * cm, firstLineIndent=-0.25 * cm, spaceAfter=5))
    styles.add(ParagraphStyle(name="KCCaption", fontName=font, fontSize=8.2, leading=11, alignment=TA_CENTER, textColor=colors.HexColor("#666666"), spaceAfter=8))
    styles.add(ParagraphStyle(name="KCFootnote", fontName=font, fontSize=8, leading=11, textColor=colors.HexColor("#777777"), alignment=TA_CENTER))
    return styles


def draw_page_brand(font: str):
    def _draw(canvas, doc) -> None:
        width, height = A4
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(PDF_WATERMARK_COLOR))
        canvas.setFont(font, 9)
        canvas.drawString(1.45 * cm, height - 0.43 * cm, BRAND)
        canvas.drawCentredString(width / 2, height - 0.43 * cm, PDF_WATERMARK)
        canvas.drawCentredString(width / 2, 0.86 * cm, PDF_WATERMARK)
        canvas.setFillColor(colors.HexColor("#8A8A8A"))
        canvas.setFont(font, 7)
        canvas.drawCentredString(width / 2, 0.48 * cm, PDF_FOOTER_DISCLAIMER)
        canvas.setFillColor(colors.HexColor(PDF_WATERMARK_COLOR))
        canvas.drawRightString(width - 1.45 * cm, 0.86 * cm, str(doc.page))
        canvas.restoreState()

    return _draw


def flush_paragraph(buffer: list[str], story: list[Any], styles: dict[str, ParagraphStyle]) -> None:
    if not buffer:
        return
    text = " ".join(item.strip() for item in buffer if item.strip())
    if text:
        story.append(Paragraph(xml_text(text), styles["KCBody"]))
    buffer.clear()


def render_pdf(translated_markdown: str, figures: list[dict[str, Any]], output_pdf: Path, title_hint: str) -> None:
    require_reportlab()
    font = register_cjk_font()
    styles = build_styles(font)
    token_to_path = {item["token"]: Path(item["path"]) for item in figures}
    title = first_heading(translated_markdown, title_hint)

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=1.55 * cm,
        leftMargin=1.55 * cm,
        topMargin=1.25 * cm,
        bottomMargin=1.25 * cm,
        title=normalize_space(f"{BRAND} {title}"),
    )

    story: list[Any] = [
        Paragraph(BRAND, styles["KCBrand"]),
        Paragraph(xml_text(title), styles["KCTitle"]),
        Spacer(1, 0.2 * cm),
    ]

    paragraph_buffer: list[str] = []
    image_count = 0
    markdown = normalize_image_token_lines(translated_markdown)
    for raw in markdown.splitlines():
        line = raw.strip()
        if not line:
            flush_paragraph(paragraph_buffer, story, styles)
            continue
        token_match = IMAGE_TOKEN_RE.fullmatch(line)
        if token_match:
            flush_paragraph(paragraph_buffer, story, styles)
            token = f"[[KC_IMAGE_{token_match.group(1)}]]"
            img_path = token_to_path.get(token)
            if img_path:
                flowable = image_flowable(img_path, max_width=16.2 * cm, max_height=12.0 * cm)
                if flowable:
                    image_count += 1
                    story.append(Spacer(1, 0.12 * cm))
                    story.append(flowable)
                    story.append(Paragraph(f"图表 {image_count}", styles["KCCaption"]))
            continue
        if line.startswith("#"):
            flush_paragraph(paragraph_buffer, story, styles)
            heading = re.sub(r"^#+\s*", "", line).strip()
            if not heading:
                continue
            level = len(line) - len(line.lstrip("#"))
            if level <= 1:
                if normalize_space(heading) == normalize_space(title):
                    continue
                story.append(Paragraph(xml_text(heading), styles["KCH1"]))
            else:
                story.append(Paragraph(xml_text(heading), styles["KCH2"]))
            continue
        if re.match(r"^[-*]\s+", line) or re.match(r"^\d+[.)]\s+", line):
            flush_paragraph(paragraph_buffer, story, styles)
            bullet = re.sub(r"^(?:[-*]|\d+[.)])\s+", "", line).strip()
            story.append(Paragraph("- " + xml_text(bullet), styles["KCBullet"]))
            continue
        if TABLE_LINE_RE.match(line) or TABLE_SEP_RE.match(line):
            continue
        paragraph_buffer.append(line)
    flush_paragraph(paragraph_buffer, story, styles)

    output_pdf.parent.mkdir(parents=True, exist_ok=True)
    doc.build(story, onFirstPage=draw_page_brand(font), onLaterPages=draw_page_brand(font))
    if not output_pdf.exists() or output_pdf.stat().st_size < 1024:
        raise RuntimeError(f"PDF was not created or is too small: {output_pdf}")
    log(f"PDF generated: {output_pdf} ({output_pdf.stat().st_size} bytes)")


def process_report(report_dir: Path, out_dir: Path, index: int, args: argparse.Namespace) -> dict[str, Any]:
    title = report_title(report_dir)
    report_out_dir = out_dir / f"{index:02d}-{slug(report_dir.name)}"
    report_out_dir.mkdir(parents=True, exist_ok=True)
    log(f"Processing report {index}: {title}")

    clean_md, figures = prepare_clean_markdown(report_dir, report_out_dir, args.max_images_per_report)
    (report_out_dir / "source_clean.md").write_text(clean_md, encoding="utf-8")
    (report_out_dir / "figure_manifest.json").write_text(json.dumps(figures, ensure_ascii=False, indent=2), encoding="utf-8")

    translated_md = translate_markdown(clean_md, args)
    translated_path = report_out_dir / "translated.md"
    translated_path.write_text(translated_md, encoding="utf-8")

    output_pdf = report_out_dir / f"kc_translated_report_{index:02d}.pdf"
    render_pdf(translated_md, figures, output_pdf, title)

    status = {
        "source_report_dir": str(report_dir),
        "title": title,
        "source_clean": "source_clean.md",
        "translated_markdown": "translated.md",
        "pdf": output_pdf.name,
        "figure_count": len(figures),
    }
    (report_out_dir / "translation_status.json").write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return {**status, "output_dir": str(report_out_dir), "pdf_path": str(output_pdf)}


def main() -> int:
    parser = argparse.ArgumentParser(description="Render KC-branded Chinese translation PDFs from MinerU report outputs.")
    parser.add_argument("--dropbox-output-root", default="xhs_notes/dropbox")
    parser.add_argument("--date-folder", default="latest")
    parser.add_argument("--output-root", default="kc_translated_reports")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--max-reports", default="1")
    parser.add_argument("--report-offset", type=int, default=0)
    parser.add_argument("--chunk-chars", type=int, default=7200)
    parser.add_argument("--max-images-per-report", type=int, default=28)
    parser.add_argument("--deepseek-timeout", type=int, default=300)
    parser.add_argument("--deepseek-retries", type=int, default=3)
    args = parser.parse_args()

    max_reports = parse_selection_limit(args.max_reports, "--max-reports")
    if args.report_offset < 0:
        raise ValueError("--report-offset must be non-negative")
    root = Path(args.dropbox_output_root)
    date_dir = latest_date_dir(root) if args.date_folder == "latest" else root / args.date_folder
    if not date_dir.exists():
        raise RuntimeError(f"Date folder not found: {date_dir}")

    all_reports = find_report_dirs(date_dir)
    if not all_reports:
        raise RuntimeError(f"No report outputs with source_mineru.md found under {date_dir}")
    if max_reports is None:
        selected = all_reports[args.report_offset :]
    else:
        selected = all_reports[args.report_offset : args.report_offset + max_reports]
    if not selected:
        raise RuntimeError(f"Report offset {args.report_offset} selected no reports from {len(all_reports)} available reports")

    out_dir = Path(args.output_root) / date_dir.name
    out_dir.mkdir(parents=True, exist_ok=True)
    log(f"Selected {len(selected)} of {len(all_reports)} reports from {date_dir}")

    summary: list[dict[str, Any]] = []
    failures: list[dict[str, Any]] = []
    for idx, report_dir in enumerate(selected, 1):
        try:
            summary.append(process_report(report_dir, out_dir, idx, args))
        except Exception as exc:
            log(f"ERROR processing {report_dir}: {exc}")
            failures.append({"source_report_dir": str(report_dir), "error": str(exc)})
            if len(selected) == 1:
                raise

    payload = {
        "date_folder": date_dir.name,
        "max_reports": "all" if max_reports is None else max_reports,
        "selected_count": len(selected),
        "successful_count": len(summary),
        "failures": failures,
        "reports": summary,
    }
    (out_dir / "translation_summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if not summary:
        return 2
    log(f"Done. Generated {len(summary)} translated report PDF(s) under {out_dir}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
