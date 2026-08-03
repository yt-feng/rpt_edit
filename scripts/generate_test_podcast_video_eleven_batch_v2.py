#!/usr/bin/env python3
"""Visual patch wrapper for Test bilingual podcast video.

Adds professional illustrated male avatars, safer mixed bilingual subtitle
wrapping, mixed-video keyword highlights, and an extra sensitive-word filter for
mixed bilingual subtitles/titles, then delegates the batch flow to the existing
wrapper.
"""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFilter

import generate_test_podcast_video_eleven as gen
import generate_test_podcast_video_eleven_batch as batch

SIZE = (1080, 1920)
ACCENT = (255, 214, 102)
EN_BRAND = "Portal Suite"
ZH_BRAND = "Portal Suite"
WHITE = (255, 255, 255)
SOFT_WHITE = (220, 232, 248)

SENSITIVE_REPLACEMENTS: list[tuple[str, str]] = [
    (r"习近平|习主席|习总书记|Xi\s+Jinping", "政策人物"),
    (r"中国共产党|共产党|中共|CCP|Communist\s+Party", "政策组织"),
    (r"政治局|Politburo", "政策会议"),
    (r"政治|politics|political", "政策环境"),
    (r"地缘政治|geopolitical", "地缘环境"),
    (r"两会|人大|政协", "政策会议"),
    (r"政府", "政策端"),
    (r"监管", "规则环境"),
    (r"制裁", "限制措施"),
    (r"战争", "冲突"),
    (r"台海|台湾", "区域议题"),
    (r"俄乌", "区域冲突"),
    (r"特朗普|川普|Trump", "海外政策人物"),
    (r"拜登|Biden", "海外政策人物"),
    (r"投资建议", "研究交流"),
    (r"投资", "投研"),
    (r"买入", "配置观点"),
    (r"卖出", "谨慎观点"),
]


def log(message: str) -> None:
    print(message, flush=True)


def sanitize_sensitive_text(text: str, lang: str = "zh") -> str:
    """Extra public-facing sensitive-word cleanup for mixed video text."""
    out = gen.sanitize_public_text(str(text or ""), lang)
    for pattern, repl in SENSITIVE_REPLACEMENTS:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
    # Clean artifacts after replacement.
    out = re.sub(r"\s+", " ", out).strip()
    return out


def sanitize_title(title: str, lang: str) -> str:
    cleaned = sanitize_sensitive_text(title, lang)
    cleaned = re.sub(r"^[#>*\-\s]+", "", cleaned).strip()
    return cleaned


def find_item_dirs(output_dir: Path, limit: int) -> list[Path]:
    items = sorted(
        p for p in output_dir.iterdir()
        if p.is_dir() and (p / "source_mineru.md").exists()
    )
    if not items:
        raise RuntimeError(f"No generated report folders with source_mineru.md under {output_dir}")
    return items[:limit]


def load_status(path: Path) -> dict[str, Any]:
    if not path.exists():
        return {}
    try:
        return json.loads(path.read_text(encoding="utf-8", errors="ignore"))
    except Exception:
        return {}


def text_size(draw: ImageDraw.ImageDraw, text: str, font: Any) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_by_pixel(draw: ImageDraw.ImageDraw, text: str, font: Any, max_width: int, lang: str, max_lines: int) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if not text:
        return []
    units = text.split() if lang == "en" else list(re.sub(r"\s+", "", text))
    lines: list[str] = []
    current = ""
    for unit in units:
        sep = " " if lang == "en" and current else ""
        candidate = f"{current}{sep}{unit}" if current else unit
        if text_size(draw, candidate, font)[0] <= max_width:
            current = candidate
            continue
        if current:
            lines.append(current)
        current = unit
        if len(lines) >= max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]


def draw_highlighted_line_local(
    draw: ImageDraw.ImageDraw,
    line: str,
    terms: list[str],
    font: Any,
    x: int,
    y: int,
    normal_fill: tuple[int, int, int],
    highlight_fill: tuple[int, int, int] = ACCENT,
) -> None:
    """Draw one line with phrase highlights, preserving exact substrings."""
    safe_terms = [t for t in terms if t and t in line]
    chunks: list[tuple[str, bool]] = [(line, False)]
    for term in sorted(set(safe_terms), key=len, reverse=True):
        next_chunks: list[tuple[str, bool]] = []
        for chunk, marked in chunks:
            if marked or term not in chunk:
                next_chunks.append((chunk, marked))
                continue
            parts = chunk.split(term)
            for idx, part in enumerate(parts):
                if part:
                    next_chunks.append((part, False))
                if idx < len(parts) - 1:
                    next_chunks.append((term, True))
        chunks = next_chunks
    cursor = x
    for chunk, marked in chunks:
        draw.text((cursor, y), chunk, font=font, fill=highlight_fill if marked else normal_fill)
        cursor += text_size(draw, chunk, font)[0]


def fallback_zh_highlights(text: str, limit: int = 2) -> list[str]:
    text = sanitize_sensitive_text(text, "zh")
    candidates = re.findall(r"\d+(?:\.\d+)?%?|[\u4e00-\u9fff]{2,6}|[A-Za-z]{2,}", text)
    banned = {"这个", "一个", "我们", "报告", "市场", "如果", "但是", "所以", "还是", "政策环境"}
    out: list[str] = []
    for item in candidates:
        if item in banned or len(item) < 2:
            continue
        if item not in out:
            out.append(item)
        if len(out) >= limit:
            break
    return out


def draw_professional_male_avatar(draw: ImageDraw.ImageDraw, cx: int, cy: int, active: bool, variant: int) -> None:
    bg_colors = ((37, 99, 235), (32, 146, 128))
    suit_colors = ((21, 45, 92), (22, 78, 72))
    hair_colors = ((32, 38, 52), (44, 53, 66))
    skin = (238, 197, 153) if variant == 0 else (225, 176, 132)
    radius = 46 if active else 40
    draw.ellipse((cx - radius, cy - radius, cx + radius, cy + radius), fill=bg_colors[variant], outline=ACCENT if active else (220, 230, 245), width=5 if active else 2)
    draw.rounded_rectangle((cx - 14, cy + 18, cx + 14, cy + 42), radius=7, fill=skin)
    draw.pieslice((cx - 42, cy + 22, cx + 42, cy + 94), 180, 360, fill=suit_colors[variant])
    draw.polygon([(cx - 18, cy + 30), (cx, cy + 54), (cx + 18, cy + 30), (cx + 8, cy + 72), (cx - 8, cy + 72)], fill=(244, 248, 252))
    tie_color = (255, 214, 102) if variant == 0 else (105, 208, 190)
    draw.polygon([(cx - 5, cy + 42), (cx + 5, cy + 42), (cx + 8, cy + 70), (cx, cy + 78), (cx - 8, cy + 70)], fill=tie_color)
    draw.ellipse((cx - 25, cy - 25, cx + 25, cy + 30), fill=skin)
    if variant == 0:
        draw.pieslice((cx - 28, cy - 32, cx + 28, cy + 8), 180, 360, fill=hair_colors[variant])
        draw.polygon([(cx - 25, cy - 10), (cx - 5, cy - 27), (cx + 25, cy - 11), (cx + 20, cy - 22), (cx - 18, cy - 25)], fill=hair_colors[variant])
        draw.ellipse((cx - 12, cy, cx - 7, cy + 5), fill=(35, 40, 46))
        draw.ellipse((cx + 7, cy, cx + 12, cy + 5), fill=(35, 40, 46))
    else:
        draw.pieslice((cx - 29, cy - 34, cx + 29, cy + 10), 170, 360, fill=hair_colors[variant])
        draw.rectangle((cx - 25, cy - 12, cx + 25, cy - 2), fill=hair_colors[variant])
        draw.ellipse((cx - 17, cy - 3, cx - 4, cy + 10), outline=(38, 48, 58), width=2)
        draw.ellipse((cx + 4, cy - 3, cx + 17, cy + 10), outline=(38, 48, 58), width=2)
        draw.line((cx - 4, cy + 3, cx + 4, cy + 3), fill=(38, 48, 58), width=2)
    draw.arc((cx - 12, cy + 9, cx + 12, cy + 22), 15, 165, fill=(120, 72, 64), width=2)


def draw_avatar_pair(draw: ImageDraw.ImageDraw, speaker: str, prefixes: tuple[str, str], y: int, lang: str) -> None:
    names = ("Host", "Guest") if lang in {"en", "mixed"} else ("主持", "嘉宾")
    centers = ((142, y), (258, y))
    active_index = 0 if speaker == prefixes[0] else 1
    small = gen.load_font(20, True)
    for idx, (cx, cy) in enumerate(centers):
        draw_professional_male_avatar(draw, cx, cy, active=(idx == active_index), variant=idx)
        nw, _ = text_size(draw, names[idx], small)
        draw.text((cx - nw / 2, cy + 58), names[idx], font=small, fill=(230, 238, 250))


def draw_mixed_frame(image_path: Path | None, title_zh: str, title_en: str, seg: dict[str, Any], output: Path, index: int, total: int) -> None:
    canvas = gen.background()
    draw = ImageDraw.Draw(canvas)
    title_font_zh = gen.load_font(52, True)
    title_font_en = gen.load_font(34, True)
    subtitle_font_en = gen.load_font(42, True)
    subtitle_font_zh = gen.load_font(40, True)
    small_font = gen.load_font(30)
    watermark_font = gen.load_font(54, True)

    title_zh = sanitize_title(title_zh, "zh")
    title_en = sanitize_title(title_en, "en")
    y = 50
    for line in batch.title_lines(title_zh, "zh", 2):
        batch.draw_text_center(draw, line, title_font_zh, y, WHITE)
        y += 64
    for line in batch.wrap_words_balanced(title_en, 36, 2)[:2]:
        batch.draw_text_center(draw, line, title_font_en, y, SOFT_WHITE)
        y += 44
    separator_y = y + 12
    draw.rounded_rectangle((78, separator_y, 1002, separator_y + 8), radius=4, fill=ACCENT)

    stage_top = max(330, separator_y + 54)
    stage = (70, stage_top, 1010, stage_top + 760)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((88, stage_top + 22, 1028, stage_top + 782), radius=42, fill=(0, 0, 0, 100))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(22)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=42, fill=(255, 255, 255, 238))
    if image_path:
        image = gen.fit_image(image_path)
        if image:
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    prefixes = gen.LANGS["en"]["prefixes"]
    box_top = 1210
    draw_avatar_pair(draw, str(seg.get("speaker", prefixes[0])), prefixes, box_top - 66, "mixed")
    draw.rounded_rectangle((70, box_top, 1010, 1668), radius=38, fill=(0, 0, 0, 185))
    label = "Host" if seg.get("speaker") == prefixes[0] else "Guest"
    label_color = (37, 99, 235) if seg.get("speaker") == prefixes[0] else (32, 146, 128)
    draw.rounded_rectangle((116, box_top + 34, 286, box_top + 82), radius=24, fill=label_color)
    draw.text((136, box_top + 38), label, font=small_font, fill=WHITE)

    yy = box_top + 112
    en_terms = [sanitize_sensitive_text(str(t), "en") for t in seg.get("highlight_terms", []) if str(t)]
    for line in str(seg.get("text_en", "")).split("\n")[:2]:
        for safe_line in wrap_by_pixel(draw, sanitize_sensitive_text(line, "en"), subtitle_font_en, 820, "en", 1):
            draw_highlighted_line_local(draw, safe_line, en_terms, subtitle_font_en, 120, yy, WHITE, ACCENT)
            yy += 54
    yy += 10
    zh_source = sanitize_sensitive_text(str(seg.get("text_zh_raw") or seg.get("text_zh") or "").replace("\n", ""), "zh")
    zh_terms = [t for t in seg.get("highlight_terms_zh", []) if t and t in zh_source]
    if not zh_terms:
        zh_terms = fallback_zh_highlights(zh_source, 2)
    for line in wrap_by_pixel(draw, zh_source, subtitle_font_zh, 820, "zh", 3):
        draw_highlighted_line_local(draw, line, zh_terms, subtitle_font_zh, 120, yy, WHITE, ACCENT)
        yy += 54
    if int(seg.get("page_count", 1)) > 1:
        draw.text((900, box_top + 40), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw.text((70, 1728), f"{index + 1}/{total}", font=small_font, fill=(200, 215, 235))
    progress = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress, 1752), radius=6, fill=ACCENT)
    width, _ = text_size(draw, EN_BRAND, watermark_font)
    draw.text(((SIZE[0] - width) // 2, 1802), EN_BRAND, font=watermark_font, fill=(205, 220, 238))
    canvas.convert("RGB").save(output, quality=93)


def translate_english_lines_to_zh(timeline: list[dict[str, Any]], args: Any) -> dict[int, str]:
    # Use the original translator, then add a strict cleanup layer for mixed video.
    raw = batch.translate_english_lines_to_zh_original(timeline, args) if hasattr(batch, "translate_english_lines_to_zh_original") else batch.translate_english_lines_to_zh(timeline, args)
    return {int(k): sanitize_sensitive_text(v, "zh") for k, v in raw.items()}


def wrap_mixed_pages(seg: dict[str, Any], zh_text: str) -> list[dict[str, Any]]:
    clean_en = sanitize_sensitive_text(str(seg.get("text", "")), "en")
    clean_zh = sanitize_sensitive_text(zh_text, "zh")
    en_lines = gen.wrap_text(clean_en, 32, "en")
    zh_clean = re.sub(r"\s+", "", clean_zh)
    en_pages = [en_lines[i:i + 2] for i in range(0, len(en_lines), 2)] or [[]]
    pages: list[dict[str, Any]] = []
    duration = max(0.5, float(seg["end"]) - float(seg["start"]))
    page_dur = duration / len(en_pages)
    for page_idx, en_page in enumerate(en_pages):
        item = dict(seg)
        item["text"] = clean_en
        item["text_en"] = "\n".join(en_page)
        item["text_zh_raw"] = zh_clean
        item["highlight_terms"] = [sanitize_sensitive_text(str(t), "en") for t in seg.get("highlight_terms", []) if str(t)]
        item["highlight_terms_zh"] = fallback_zh_highlights(zh_clean, 2)
        item["page_index"] = page_idx + 1
        item["page_count"] = len(en_pages)
        item["start"] = round(float(seg["start"]) + page_idx * page_dur, 3)
        item["end"] = round(float(seg["start"]) + (page_idx + 1) * page_dur, 3)
        pages.append(item)
    return pages


def make_mixed_video(item_dir: Path, args: Any, status: dict[str, Any]) -> dict[str, Any]:
    # Sanitized replacement for the batch mixed renderer.
    en_timeline_path = item_dir / "podcast_en_timeline.json"
    en_audio_path = item_dir / "podcast_en.wav"
    if not en_timeline_path.exists() or not en_audio_path.exists():
        raise RuntimeError("English timeline/audio missing; generate English podcast first")
    en_timeline = json.loads(en_timeline_path.read_text(encoding="utf-8"))
    for seg in en_timeline:
        seg["text"] = sanitize_sensitive_text(str(seg.get("text", "")), "en")
        seg["highlight_terms"] = [sanitize_sensitive_text(str(t), "en") for t in seg.get("highlight_terms", []) if str(t)]
    zh_map = translate_english_lines_to_zh(en_timeline, args)
    visual: list[dict[str, Any]] = []
    for i, seg in enumerate(en_timeline):
        visual.extend(wrap_mixed_pages(seg, zh_map.get(i, "")))
    title_zh = sanitize_title(str(status.get("podcast_zh_title") or "研报讲解"), "zh")
    title_en = sanitize_title(str(status.get("podcast_en_title") or "Research Briefing"), "en")
    images = gen.report_images(item_dir)
    import tempfile
    with tempfile.TemporaryDirectory(prefix="portal_mixed_frames_") as temp_dir:
        tmp = Path(temp_dir)
        concat = tmp / "concat.txt"
        concat_lines: list[str] = []
        for index, seg in enumerate(visual):
            frame = tmp / f"frame_{index:04d}.png"
            image_path = images[index % len(images)] if images else None
            draw_mixed_frame(image_path, title_zh, title_en, seg, frame, index, len(visual))
            concat_lines.append(f"file '{frame.as_posix()}'\n")
            concat_lines.append(f"duration {gen.frame_duration(visual, index):.3f}\n")
        concat_lines.append(concat_lines[-2])
        concat.write_text("".join(concat_lines), encoding="utf-8")
        silent = tmp / "silent.mp4"
        out_video = item_dir / "podcast_mixed_bilingual_explainer.mp4"
        gen.run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-vsync", "vfr", "-pix_fmt", "yuv420p", str(silent)], timeout=1200)
        gen.run(["ffmpeg", "-y", "-i", str(silent), "-i", str(en_audio_path), "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-shortest", str(out_video)], timeout=1200)
    (item_dir / "podcast_mixed_visual_timeline.json").write_text(json.dumps(visual, ensure_ascii=False, indent=2), encoding="utf-8")
    return {
        "podcast_mixed_video": "podcast_mixed_bilingual_explainer.mp4",
        "podcast_mixed_audio_source": "podcast_en.wav",
        "podcast_mixed_visual_timeline": "podcast_mixed_visual_timeline.json",
        "podcast_mixed_watermark": EN_BRAND,
        "podcast_mixed_sensitive_filter": "extra strict policy/person-name cleanup in mixed renderer",
        "podcast_mixed_highlight": "English and Chinese subtitle phrase highlights enabled",
    }


def apply_visual_patches() -> None:
    batch.draw_avatar_pair = draw_avatar_pair
    batch.draw_mixed_frame = draw_mixed_frame
    if not hasattr(batch, "translate_english_lines_to_zh_original"):
        batch.translate_english_lines_to_zh_original = batch.translate_english_lines_to_zh
    batch.translate_english_lines_to_zh = translate_english_lines_to_zh
    batch.wrap_mixed_pages = wrap_mixed_pages
    batch.make_mixed_video = make_mixed_video


def main() -> int:
    apply_visual_patches()
    return batch.main()


if __name__ == "__main__":
    raise SystemExit(main())
