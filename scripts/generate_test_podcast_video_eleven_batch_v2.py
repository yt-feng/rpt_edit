#!/usr/bin/env python3
"""Visual patch wrapper for Test bilingual podcast video.

Adds professional illustrated male avatars and safer mixed bilingual subtitle
wrapping, then delegates the rest of the batch flow to the existing wrapper.
"""
from __future__ import annotations

import re
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFilter

import generate_test_podcast_video_eleven as gen
import generate_test_podcast_video_eleven_batch as batch

SIZE = (1080, 1920)
ACCENT = (255, 214, 102)
EN_BRAND = "KC Desk Notes"
ZH_BRAND = "KC桌面"


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

    y = 50
    for line in batch.title_lines(title_zh, "zh", 2):
        batch.draw_text_center(draw, line, title_font_zh, y, (255, 255, 255))
        y += 64
    for line in batch.wrap_words_balanced(title_en, 36, 2)[:2]:
        batch.draw_text_center(draw, line, title_font_en, y, (220, 232, 248))
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
    draw.text((136, box_top + 38), label, font=small_font, fill=(255, 255, 255))

    yy = box_top + 112
    for line in str(seg.get("text_en", "")).split("\n")[:2]:
        for safe_line in wrap_by_pixel(draw, line, subtitle_font_en, 820, "en", 1):
            draw.text((120, yy), safe_line, font=subtitle_font_en, fill=(255, 255, 255))
            yy += 54
    yy += 10
    zh_source = str(seg.get("text_zh_raw") or seg.get("text_zh") or "").replace("\n", "")
    for line in wrap_by_pixel(draw, zh_source, subtitle_font_zh, 820, "zh", 3):
        draw.text((120, yy), line, font=subtitle_font_zh, fill=ACCENT)
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


def apply_visual_patches() -> None:
    batch.draw_avatar_pair = draw_avatar_pair
    batch.draw_mixed_frame = draw_mixed_frame


def main() -> int:
    apply_visual_patches()
    return batch.main()


if __name__ == "__main__":
    raise SystemExit(main())
