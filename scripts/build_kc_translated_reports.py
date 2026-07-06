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

try:
    from institution_names import ensure_title_has_institution, infer_institution_name
except Exception:  # pragma: no cover
    def ensure_title_has_institution(title: str, institution: str) -> str:
        title = title.strip()
        institution = institution.strip()
        if institution and not title.startswith(f"{institution}："):
            return f"{institution}：{title}"
        return title

    def infer_institution_name(*_values: Any) -> str:
        return ""

from wechat_title_optimizer import (
    build_wechat_title_refinement_prompt,
    choose_best_wechat_title,
    extract_title_candidates,
    extract_wechat_keywords,
)
from sensitive_content_guard import sanitize_wechat_stock_language

# Maps the institution keys used by fetch_institution_latest_pdfs.py to the Chinese
# names institution_names.infer_institution_name returns, so --exclude-institutions
# can drop whole sources (e.g. rand,brookings) before translating.
INSTITUTION_KEY_TO_CN = {
    "imf": "IMF",
    "bis": "国际清算银行",
    "worldbank": "世界银行",
    "world bank": "世界银行",
    "oecd": "经合组织",
    "adb": "亚洲开发银行",
    "wef": "世界经济论坛",
    "unctad": "联合国贸发会议",
    "wto": "世界贸易组织",
    "bruegel": "布鲁盖尔研究所",
    "rand": "兰德公司",
    "brookings": "布鲁金斯学会",
}

INSTITUTION_TITLE_ALIASES: list[tuple[str, list[str]]] = [
    ("高盛", ["GS", "Goldman Sachs"]),
    ("摩根大通", ["JPM", "J.P. Morgan", "JP Morgan", "JPMorgan"]),
    ("摩根士丹利", ["MS", "Morgan Stanley", "摩根斯坦利", "大摩"]),
    ("美银", ["BofA", "Bank of America", "美国银行", "美银证券"]),
    ("花旗", ["Citi", "Citigroup"]),
    ("瑞银", ["UBS"]),
    ("汇丰", ["HSBC"]),
    ("巴克莱", ["BARC", "Barclays"]),
    ("伯恩斯坦", ["Bernstein", "Sanford C. Bernstein", "Sanford Bernstein"]),
    ("杰富瑞", ["JEF", "Jefferies"]),
    ("德意志银行", ["DB", "Deutsche Bank", "德银"]),
    ("野村", ["NOM", "Nomura"]),
    ("美联储", ["Fed", "Federal Reserve"]),
]
TITLE_ALIAS_SEPARATOR_RE = r"(?:[：:，,、;；\-—]\s*)?"

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
PDF_FOOTER_DISCLAIMER = (
    "For informational purposes only. Portions may be generated, translated, summarized, or edited with "
    "AI assistance based on source materials and may contain omissions or errors. Please verify independently. "
    "This is not investment, legal, tax, accounting, or other professional advice."
)
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
PUBLIC_AND_CONSULTING_INSTITUTIONS = {
    "IMF",
    "世界银行",
    "国际清算银行",
    "麦肯锡",
    "波士顿咨询",
    "兰德公司",
    "布鲁金斯学会",
    "木头姐ARK",
}
CHART_CONTEXT_RE = re.compile(
    r"(?:\b(?:exhibit|figure|fig\.|chart|table|source|survey|respondents?|percentage|percent|"
    r"growth|inflation|gdp|forecast|index|rate|share|basis points?|bps?)\b|"
    r"图表|图\s*\d+|表\s*\d+|来源[:：]|受访者|占比|同比|环比|预测|指数|增速|利率|通胀|增长)",
    re.I,
)
NON_CHART_CONTEXT_RE = re.compile(
    r"(?:\b(?:headshot|portrait|profile|author|authors?|partner|senior partner|associate partner|"
    r"managing director|biography|bio|commentary|interview|photo|photograph|image credit|"
    r"getty|shutterstock|unsplash|istock|cover)\b|"
    r"合伙人|作者|头像|照片|访谈|人物|履历|麦肯锡评论)",
    re.I,
)
NON_CHART_FILENAME_RE = re.compile(r"(?:avatar|author|headshot|portrait|profile|logo|cover|hero|banner|photo)", re.I)
ARTICLE_STYLE_MAX_IMAGE_TOKENS = 3


def log(message: str) -> None:
    print(message, flush=True)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", sanitize_text(text or "")).strip()


def canonicalize_institution_title_name(title: str) -> str:
    normalized = normalize_space(title)
    normalized = normalized.replace("摩根斯坦利", "摩根士丹利")
    normalized = normalized.replace("美国银行", "美银")
    return normalized


def alias_pattern(alias: str) -> str:
    if alias.lower() == "bofa":
        return r"(?<![A-Za-z])BofA(?=(?:Q[1-4]|\d|[^A-Za-z]|$))"
    if re.fullmatch(r"[A-Z]{2,5}", alias):
        return rf"(?<![A-Za-z]){re.escape(alias)}(?![A-Za-z])"
    if re.fullmatch(r"[A-Za-z. ]+", alias):
        return r"\b" + re.escape(alias).replace(r"\ ", r"[\s._-]+") + r"\b"
    return re.escape(alias)


def limit_title_colons(title: str) -> str:
    cleaned = normalize_space(title).replace(":", "：")
    if "：" not in cleaned:
        return cleaned
    head, tail = cleaned.split("：", 1)
    tail = re.sub(r"\s*：\s*", "，", tail).strip(" ，")
    if not tail:
        return head.strip()
    return f"{head.strip()}：{tail}"


def clean_leading_report_slug(title: str) -> str:
    cleaned = normalize_space(title)
    cleaned = re.sub(
        r"^([^：:]{1,18}[：:]\s*)(?:\d{4}[-_])?\d{1,4}[-_]\d{1,4}[-_]+",
        r"\1",
        cleaned,
    )
    cleaned = re.sub(r"^(?:\d{4}[-_])?\d{1,4}[-_]\d{1,4}[-_]+", "", cleaned)

    def readable_slug_tail(value: str) -> str:
        if value.count("-") + value.count("_") < 3:
            return value
        value = value.replace("_", " ")
        value = re.sub(r"\s*-{2,}\s*", "，", value)
        value = re.sub(r"\s*-\s*", " ", value)
        return normalize_space(value)

    for sep in ("：", ":"):
        if sep in cleaned:
            head, tail = cleaned.split(sep, 1)
            return f"{head.strip()}：{readable_slug_tail(tail.strip())}".strip("： ")
    return readable_slug_tail(cleaned).strip(" -_")


def remove_redundant_title_aliases(title: str) -> str:
    cleaned = clean_leading_report_slug(canonicalize_institution_title_name(title))
    for cn_name, aliases in INSTITUTION_TITLE_ALIASES:
        alias_group = "|".join(alias_pattern(alias) for alias in aliases)
        cleaned = re.sub(
            rf"^({re.escape(cn_name)})[：:]\s*(?:{alias_group})\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
        cleaned = re.sub(
            rf"^(?:{alias_group})\s*[：:]\s*({re.escape(cn_name)})\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
        cleaned = re.sub(
            rf"^({re.escape(cn_name)})\s*(?:\(|（)\s*(?:{alias_group})\s*(?:\)|）)\s*{TITLE_ALIAS_SEPARATOR_RE}",
            rf"\1：",
            cleaned,
            flags=re.I,
        )
    cleaned = re.sub(r"\s*[：:]\s*", "：", cleaned)
    cleaned = re.sub(r"：{2,}", "：", cleaned)
    return limit_title_colons(cleaned).strip("：: -—")


def strip_unexpected_leading_institution_prefix(title: str, institution_name: str) -> str:
    expected = canonicalize_institution_title_name(institution_name)
    cleaned = remove_redundant_title_aliases(title)
    for _ in range(3):
        for cn_name, aliases in INSTITUTION_TITLE_ALIASES:
            if canonicalize_institution_title_name(cn_name) == expected:
                continue
            prefix_group = "|".join([re.escape(cn_name), *(alias_pattern(alias) for alias in aliases)])
            replaced = re.sub(
                rf"^(?:{prefix_group})\s*[：:，,、;；\-—]\s*",
                "",
                cleaned,
                flags=re.I,
            ).strip()
            if replaced != cleaned:
                cleaned = replaced
                break
        else:
            break
    return cleaned


def clean_display_title(title: str, institution_name: str = "") -> str:
    cleaned = remove_redundant_title_aliases(title)
    cleaned = re.sub(r"^(?:标题|微信标题)\s*[：:]\s*", "", cleaned)
    if institution_name:
        cleaned = strip_unexpected_leading_institution_prefix(cleaned, institution_name)
        cleaned = ensure_title_has_institution(
            cleaned,
            canonicalize_institution_title_name(institution_name),
        )
    return remove_redundant_title_aliases(cleaned)[:140]


def replace_first_heading(markdown: str, title: str) -> str:
    lines = markdown.splitlines()
    for idx, raw in enumerate(lines):
        if raw.strip().startswith("#"):
            lines[idx] = f"# {title}"
            return "\n".join(lines).strip() + "\n"
    return f"# {title}\n\n{markdown.strip()}\n"


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


def parse_institution_filter(value: str) -> set[str]:
    filters: set[str] = set()
    for raw in (value or "").split(","):
        token = normalize_space(raw)
        if not token or token.lower() in {"all", "*"}:
            continue
        filters.add(INSTITUTION_KEY_TO_CN.get(token.lower(), token))
    return filters


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


def is_public_or_consulting_report(report_dir: Path, title: str = "", source_preview: str = "") -> bool:
    institution = infer_institution_name(report_dir.name, title, source_preview)
    if institution in PUBLIC_AND_CONSULTING_INSTITUTIONS:
        return True
    path_hint = str(report_dir).lower()
    return "/institutions/" in path_hint or "/consulting/" in path_hint or "/ark/" in path_hint


def chart_context(lines: list[str], index: int, radius: int = 5) -> str:
    start = max(0, index - radius)
    end = min(len(lines), index + radius + 1)
    return "\n".join(line.strip() for line in lines[start:end] if line.strip())


def image_edge_density(image: Any) -> float:
    try:
        gray = image.convert("L").resize((96, 96))
        pixels = list(gray.getdata())
    except Exception:
        return 0.0
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


def chart_image_score(path: Path, context: str = "") -> tuple[int, str]:
    score = 0
    reasons: list[str] = []
    if NON_CHART_FILENAME_RE.search(path.name):
        score -= 4
        reasons.append("non_chart_filename")
    if NON_CHART_CONTEXT_RE.search(context):
        score -= 5
        reasons.append("non_chart_context")
    if CHART_CONTEXT_RE.search(context):
        score += 6
        reasons.append("chart_context")

    try:
        from PIL import Image, ImageStat

        with Image.open(path) as image:
            width, height = image.size
            area = width * height
            ratio = width / max(1, height)
            if width < 320 or height < 180 or area < 100_000:
                return -100, f"too_small:{width}x{height}"
            if ratio < 0.38 or ratio > 4.8:
                score -= 3
                reasons.append(f"odd_ratio:{ratio:.2f}")
            if 1.05 <= ratio <= 3.8:
                score += 1
                reasons.append("chart_ratio")
            if 0.72 <= ratio <= 1.35 and not CHART_CONTEXT_RE.search(context):
                score -= 3
                reasons.append("square_without_context")
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
    except Exception as exc:
        reasons.append(f"image_probe_failed:{str(exc)[:80]}")

    return score, ",".join(reasons)


def should_keep_report_image(path: Path, context: str, strict_chart: bool) -> tuple[bool, str]:
    if not strict_chart:
        return True, "legacy"
    if not CHART_CONTEXT_RE.search(context) and not re.search(r"(?:chart|figure|fig|exhibit|table|graph|plot)", path.name, re.I):
        return False, "missing_chart_context"
    score, reason = chart_image_score(path, context)
    return score >= 3, f"score={score};{reason}"


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


def copy_resolved_image_for_report(
    src: Path,
    assets_dir: Path,
    image_index: int,
    score_reason: str = "",
) -> tuple[str, dict[str, Any]] | None:
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
    if score_reason:
        meta["chart_filter"] = score_reason
    return token, meta


def copy_image_for_report(
    source_markdown: Path,
    image_ref: str,
    assets_dir: Path,
    image_index: int,
) -> tuple[str, dict[str, Any]] | None:
    src = resolve_image_path(source_markdown, image_ref)
    if not src:
        return None
    return copy_resolved_image_for_report(src, assets_dir, image_index)


def prepare_clean_markdown(
    report_dir: Path,
    out_dir: Path,
    max_images: int,
    strict_chart_images: bool = False,
) -> tuple[str, list[dict[str, Any]]]:
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

    for source_index, raw in enumerate(lines[body_start:], start=body_start):
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
                src = resolve_image_path(source_markdown, image_match.group(1))
                copied = None
                if src:
                    keep_image, score_reason = should_keep_report_image(
                        src,
                        chart_context(lines, source_index),
                        strict_chart_images,
                    )
                    if keep_image:
                        copied = copy_resolved_image_for_report(src, assets_dir, image_index, score_reason)
                    else:
                        log(f"  Skip non-chart image {src.name}: {score_reason}")
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


def call_deepseek(
    prompt: str,
    args: argparse.Namespace,
    label: str,
    temperature: float = 0.15,
    system_content: str | None = None,
) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")

    payload: dict[str, Any] = {
        "model": args.model,
        "temperature": temperature,
        "messages": [
            {
                "role": "system",
                "content": system_content or (
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


def title_is_sensitive(title: str, args: argparse.Namespace) -> bool:
    """Ask DeepSeek whether a report title is China-sensitive.

    Used to gate the WeChat draft path: a title that disparages China / touches
    sensitive political topics must not reach the 公众号 draft box. API errors are
    fatal so an exhausted DeepSeek balance cannot be mistaken for sensitive titles.
    Unclear verdicts still fail closed and skip only that report.
    """
    title = (title or "").strip()
    if not title:
        return False
    prompt = (
        "你是中国大陆微信公众号合规审核员。下面是一篇外文研究报告的标题。"
        "判断该标题是否包含对中国不友好、负面唱衰、攻击中国制度或政策，"
        "或涉及敏感政治议题（如台独、疆独、藏独、人权指控等）的内容。"
        "只回答一个英文单词：SENSITIVE 或 SAFE。\n\n标题：" + title
    )
    try:
        verdict = call_deepseek(prompt, args, f"title guard: {title[:40]}", temperature=0.0).upper()
    except Exception as exc:  # noqa: BLE001 - make quota/API issues visible
        raise RuntimeError(f"title guard failed for {title[:80]}: {exc}") from exc
    if "SENSITIVE" in verdict:
        return True
    if "SAFE" in verdict:
        return False
    log(f"  [title-guard] unclear verdict {verdict!r}; skipping to stay safe")
    return True


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


def remove_unwanted_image_tokens(markdown: str, allowed_tokens: list[str]) -> str:
    allowed = set(allowed_tokens)

    def replace(match: re.Match[str]) -> str:
        token = f"[[KC_IMAGE_{match.group(1)}]]"
        return token if token in allowed else ""

    text = IMAGE_TOKEN_RE.sub(replace, markdown)
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    return text.strip()


def insert_article_tokens(markdown: str, tokens: list[str]) -> str:
    if not tokens:
        return markdown.strip() + "\n"
    text = remove_unwanted_image_tokens(markdown, tokens)
    present = [token for token in tokens if token in text]
    missing = [token for token in tokens if token not in present]
    if not missing:
        return text.strip() + "\n"

    lines = text.splitlines()
    h2_indices = [idx for idx, line in enumerate(lines) if line.startswith("## ")]
    insert_positions = h2_indices[1:] or h2_indices or [min(len(lines), 4)]
    offset = 0
    for token, pos in zip(missing, insert_positions):
        insert_at = min(len(lines), pos + offset)
        lines.insert(insert_at, "")
        lines.insert(insert_at + 1, token)
        lines.insert(insert_at + 2, "")
        offset += 3
    if len(missing) > len(insert_positions):
        for token in missing[len(insert_positions) :]:
            lines.extend(["", token, ""])
    return re.sub(r"\n{4,}", "\n\n\n", "\n".join(lines)).strip() + "\n"


def build_article_style_prompt(markdown: str, title: str, institution_name: str, image_tokens: list[str]) -> str:
    token_text = ", ".join(image_tokens) if image_tokens else "无可用图表占位符"
    source = markdown[: min(len(markdown), 22_000)]
    return f"""
你是“KC桌面”的微信公众号财经文章主笔。请把下面的公共机构/咨询公司英文报告，改写成和外资投行研报系列一致的中文微信文章。

写作目标：
- 不是逐段翻译，而是基于原报告写一篇完整、顺滑、有主线的中文综述。
- 保留报告里的核心数据、结论、因果链和读者最该追问的问题。
- 删除作者介绍、头像说明、访谈口吻、网页导航、版权页、脚注长串、目录、免责声明、机构自我宣传。
- 不能编造原文没有的信息；如果某个数字不确定，就不要写。
- 语言要像人工编辑润色过：句长有变化，不要整齐排比，不要用模板化转折堆段落。

格式要求：
1. 第一行必须是 `# {{机构中文名}}：{{短标题}}`，标题短、清楚、有传播性；优先 20-35 个中文字符，最多一个冒号。
   - 标题必须包含至少两个钩子：机构/人物 big name、可搜索主题词、反常识判断、市场误判、数据节点、政策/行业变量。
   - 不要写英文机构简称或 ticker，例如 GS、JPM、JEF、NOM、BARC、MS、DB、Citi；不要写“核心观点”“关键要点”“研报速览”。
   - 标题不要把三段以上信息塞满；只保留主判断，其余放在开头自然展开。
2. 正文控制在 1200-1800 个中文字符。
3. 开头 2 段要自然带出 4-7 个长尾关键词，例如国家/行业/政策/数据/公司/技术词，让读者从搜一搜进入也能立刻判断相关性。
4. 使用 3 个 `##` 小节，每个小节标题都要是 action title，读标题就知道结论。
5. 每个小节 1-2 段，段落要像投行报告解读，避免散乱摘抄。
6. 插入 2 条 `> KC评论：...`。KC评论要用大白话解释“这对市场/企业/政策观察意味着什么”，不要空泛，也不要夹带 CTA。
7. 如有可用图表占位符，只能从这些 token 里选 1-3 个并原样插入，单独成行：{token_text}
8. 正文中间禁止插入 CTA、广告、扫码、社群、知识星球、每日汇编、喂给 AI 等表达；中间只允许正文、图表占位和 KC评论。
9. 如果是单一公司/个股报告，只写公司情况、行业变化、业务进展、竞争格局和报告事实；禁止输出目标价、评级、买入、卖出、增持、减持、推荐、荐股、Buy、Sell、Overweight、Underweight、Outperform、Underperform、PT、TP、PO 等卖方操作口径。
10. 不要输出代码块，不要输出英文原文，不要输出“以下是”等解释。

机构中文名：{institution_name or "该机构"}
原报告标题：{title}

已清洗原文：
{source}
""".strip()


def generate_article_style_markdown(
    clean_markdown: str,
    title: str,
    institution_name: str,
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
) -> str:
    image_tokens = [str(item.get("token") or "") for item in figures[:ARTICLE_STYLE_MAX_IMAGE_TOKENS] if item.get("token")]
    prompt = build_article_style_prompt(clean_markdown, title, institution_name, image_tokens)
    system_content = (
        "你是专业中文财经编辑，擅长把英文公共机构、咨询公司、投行报告改写成"
        "微信公众号可读的中文研报解读。只根据原文写作，不编造。"
    )
    article = call_deepseek(
        prompt,
        args,
        f"article-style rewrite: {title[:40]}",
        temperature=0.18,
        system_content=system_content,
    )
    article = article.replace("```markdown", "").replace("```", "")
    article = insert_article_tokens(article, image_tokens)
    article, _stock_changes = sanitize_wechat_stock_language(article)
    return sanitize_text(article).strip() + "\n"


def refine_wechat_title_with_deepseek(
    source_title: str,
    translated_md: str,
    institution_name: str,
    args: argparse.Namespace,
) -> str:
    fallback = clean_display_title(first_heading(translated_md, source_title), institution_name)
    if not getattr(args, "title_refine", True):
        return fallback
    article_excerpt = normalize_space(re.sub(r"[#>*`!\\[\\]()]+", " ", translated_md))[:2400]
    source_keywords = extract_wechat_keywords(source_title, translated_md, max_keywords=10)
    prompt = build_wechat_title_refinement_prompt(
        source_title=source_title,
        institution_name=institution_name,
        article_excerpt=article_excerpt,
        source_keywords=source_keywords,
    )
    try:
        raw = call_deepseek(
            prompt,
            args,
            f"WeChat title refine: {source_title[:40]}",
            temperature=0.25,
            system_content="你是中文微信公众号标题编辑，只输出严格 JSON。",
        )
        candidates = extract_title_candidates(raw)
    except Exception as exc:
        log(f"  Title refinement failed, using generated heading: {exc}")
        candidates = []
    return choose_best_wechat_title(
        candidates,
        fallback=fallback,
        institution_name=institution_name,
        source_keywords=source_keywords,
        max_chars=64,
    )


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
    def wrap_footer_lines(text: str, canvas, max_width: float) -> list[str]:
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            candidate = f"{current} {word}".strip()
            if current and canvas.stringWidth(candidate, font, 6.2) > max_width:
                lines.append(current)
                current = word
            else:
                current = candidate
        if current:
            lines.append(current)
        return lines[:3]

    def _draw(canvas, doc) -> None:
        width, height = A4
        canvas.saveState()
        canvas.setFillColor(colors.HexColor(PDF_WATERMARK_COLOR))
        canvas.setFont(font, 9)
        canvas.drawString(1.45 * cm, height - 0.43 * cm, BRAND)
        canvas.drawCentredString(width / 2, height - 0.43 * cm, PDF_WATERMARK)
        canvas.drawCentredString(width / 2, 0.86 * cm, PDF_WATERMARK)
        canvas.setFillColor(colors.HexColor("#8A8A8A"))
        canvas.setFont(font, 6.2)
        footer_lines = wrap_footer_lines(PDF_FOOTER_DISCLAIMER, canvas, width - 3.0 * cm)
        for idx, line in enumerate(reversed(footer_lines)):
            canvas.drawCentredString(width / 2, (0.34 + idx * 0.20) * cm, line)
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
    source_title = report_title(report_dir)
    report_out_dir = out_dir / f"{index:02d}-{slug(report_dir.name)}"
    report_out_dir.mkdir(parents=True, exist_ok=True)
    log(f"Processing report {index}: {source_title}")

    source_preview = ""
    source_path = report_dir / "source_mineru.md"
    if source_path.exists():
        source_preview = source_path.read_text(encoding="utf-8", errors="ignore")[:1600]
    institution_name = infer_institution_name(report_dir.name, source_title, source_preview)
    article_style = is_public_or_consulting_report(report_dir, source_title, source_preview)
    if article_style:
        log(f"  Using article-style rewrite and strict chart filtering for {institution_name or report_dir.name}")

    clean_md, figures = prepare_clean_markdown(
        report_dir,
        report_out_dir,
        args.max_images_per_report,
        strict_chart_images=article_style,
    )
    (report_out_dir / "source_clean.md").write_text(clean_md, encoding="utf-8")
    (report_out_dir / "figure_manifest.json").write_text(json.dumps(figures, ensure_ascii=False, indent=2), encoding="utf-8")

    if article_style:
        translated_md = generate_article_style_markdown(clean_md, source_title, institution_name, figures, args)
    else:
        translated_md = translate_markdown(clean_md, args)
    translated_md, stock_changes = sanitize_wechat_stock_language(translated_md)
    display_title = refine_wechat_title_with_deepseek(source_title, translated_md, institution_name, args)
    display_title, title_stock_changes = sanitize_wechat_stock_language(display_title)
    translated_md = replace_first_heading(translated_md, display_title)
    translated_md, stock_changes_after_title = sanitize_wechat_stock_language(translated_md)
    translated_path = report_out_dir / "translated.md"
    translated_path.write_text(translated_md, encoding="utf-8")

    output_pdf = report_out_dir / f"kc_translated_report_{index:02d}.pdf"
    render_pdf(translated_md, figures, output_pdf, display_title)

    status = {
        "source_report_dir": str(report_dir),
        "title": display_title,
        "source_title": source_title,
        "source_clean": "source_clean.md",
        "translated_markdown": "translated.md",
        "pdf": output_pdf.name,
        "figure_count": len(figures),
        "institution_name": institution_name,
        "article_style": article_style,
        "stock_language_sanitized": stock_changes[:40] + title_stock_changes[:20] + stock_changes_after_title[:20],
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
    parser.add_argument("--exclude-institutions", default="",
                        help="Comma list of institution keys to skip entirely, e.g. rand,brookings.")
    parser.add_argument("--include-institutions", default="",
                        help="Comma list of institution keys/names to keep, e.g. bis,imf.")
    parser.add_argument("--no-title-refine", dest="title_refine", action="store_false",
                        help="Skip the extra DeepSeek title-candidate pass and use the generated heading.")
    parser.set_defaults(title_refine=True)
    parser.add_argument("--title-guard", action="store_true",
                        help="Use DeepSeek to skip reports whose title is China-sensitive (keeps them out of WeChat).")
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

    included_cn = parse_institution_filter(args.include_institutions)
    if included_cn:
        kept: list[Path] = []
        for report_dir in all_reports:
            institution = infer_institution_name(report_dir.name)
            if institution in included_cn:
                kept.append(report_dir)
            else:
                log(f"Skipping institution report outside include filter ({institution or 'unknown'}): {report_dir.name}")
        all_reports = kept
        if not all_reports:
            raise RuntimeError(f"No reports under {date_dir} matched --include-institutions={args.include_institutions}")

    excluded_cn = {
        INSTITUTION_KEY_TO_CN.get(key.strip().lower(), key.strip())
        for key in (args.exclude_institutions or "").split(",") if key.strip()
    }
    if excluded_cn:
        kept: list[Path] = []
        for report_dir in all_reports:
            institution = infer_institution_name(report_dir.name)
            if institution and institution in excluded_cn:
                log(f"Excluding institution report ({institution}): {report_dir.name}")
            else:
                kept.append(report_dir)
        all_reports = kept
        if not all_reports:
            raise RuntimeError(f"All reports under {date_dir} were excluded by --exclude-institutions={args.exclude_institutions}")

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
    sensitive_skipped: list[dict[str, Any]] = []
    for idx, report_dir in enumerate(selected, 1):
        if args.title_guard:
            title = report_title(report_dir)
            if title_is_sensitive(title, args):
                log(f"Skipping China-sensitive title, not sending to WeChat: {title}")
                sensitive_skipped.append({"source_report_dir": str(report_dir), "title": title})
                continue
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
        "sensitive_skipped_count": len(sensitive_skipped),
        "sensitive_skipped": sensitive_skipped,
        "failures": failures,
        "reports": summary,
    }
    (out_dir / "translation_summary.json").write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    if not summary:
        if sensitive_skipped:
            log(f"No translated reports: all {len(sensitive_skipped)} selected title(s) were China-sensitive and skipped. Not an error.")
            return 0
        return 2
    log(f"Done. Generated {len(summary)} translated report PDF(s) under {out_dir} (skipped {len(sensitive_skipped)} sensitive).")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise
