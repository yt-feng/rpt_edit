#!/usr/bin/env python3
"""Safe-area + font patch for Test bilingual podcast video.

Builds on v4 and fixes:
- top/bottom safe areas for iPhone notch and WeChat Channels controls;
- Chinese font preference closer to Microsoft YaHei with Simplified Chinese CJK fonts;
- mixed-video title glyph cleanup and Latin word wrapping from v4.
"""
from __future__ import annotations

from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

import generate_test_podcast_video_eleven as gen
import generate_test_podcast_video_eleven_batch as base_batch
import generate_test_podcast_video_eleven_batch_v2 as v2
import generate_test_podcast_video_eleven_batch_v4 as v4

SIZE = (1080, 1920)
ACCENT = (255, 214, 102)
WHITE = (255, 255, 255)
SOFT_WHITE = (220, 232, 248)
ZH_BRAND = "Portal Suite"
EN_BRAND = "Portal Suite"

TOP_SAFE = 172
BOTTOM_SAFE_START = 1600
TITLE_Y = 178
STAGE_TOP_MIN = 382
STANDARD_STAGE_H = 500
MIXED_STAGE_H = 440
BOX_TOP = 998
BOX_BOTTOM = 1458
PROGRESS_Y = 1510
WATERMARK_Y = 1552


def load_font_cjk_sans(size: int, bold: bool = False) -> ImageFont.ImageFont:
    """Prefer Simplified Chinese CJK sans fonts available on Ubuntu runners."""
    candidates = [
        ("/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc", 2),
        ("/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc", 2),
        ("/usr/share/fonts/truetype/wqy/wqy-microhei.ttc", 0),
        ("/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc", 0),
        ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", 0),
    ]
    for candidate, index in candidates:
        if Path(candidate).exists():
            try:
                return ImageFont.truetype(candidate, size, index=index)
            except TypeError:
                try:
                    return ImageFont.truetype(candidate, size)
                except OSError:
                    continue
            except OSError:
                continue
    return ImageFont.load_default()


def text_size(draw: ImageDraw.ImageDraw, text: str, font: Any) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def center_text(draw: ImageDraw.ImageDraw, text: str, font: Any, y: int, fill: tuple[int, int, int]) -> None:
    w, _ = text_size(draw, text, font)
    draw.text(((SIZE[0] - w) // 2, y), text, font=font, fill=fill)


def draw_safe_bottom(draw: ImageDraw.ImageDraw, index: int, total: int, watermark: str, font_small: Any, font_watermark: Any) -> None:
    draw.text((78, PROGRESS_Y - 12), f"{index + 1}/{total}", font=font_small, fill=(200, 215, 235))
    progress = int(720 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((210, PROGRESS_Y, 930, PROGRESS_Y + 12), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((210, PROGRESS_Y, 210 + progress, PROGRESS_Y + 12), radius=6, fill=ACCENT)
    w, _ = text_size(draw, watermark, font_watermark)
    draw.text(((SIZE[0] - w) // 2, WATERMARK_Y), watermark, font=font_watermark, fill=(205, 220, 238))


def paste_report_image(canvas: Image.Image, image_path: Path | None, stage: tuple[int, int, int, int]) -> None:
    if not image_path:
        return
    image = gen.fit_image(image_path)
    if not image:
        return
    max_w = stage[2] - stage[0] - 70
    max_h = stage[3] - stage[1] - 50
    image = ImageOps.contain(image.convert("RGB"), (max_w, max_h), method=Image.Resampling.LANCZOS) if False else image
    canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))


def draw_standard_frame_safe(image_path: Path | None, title: str, title_terms: list[str], seg: dict[str, Any], output: Path, index: int, total: int, lang: str) -> None:
    cfg = gen.LANGS[lang]
    canvas = gen.background()
    draw = ImageDraw.Draw(canvas)
    title_font = gen.load_font(50, True)
    subtitle_font = gen.load_font(44, True)
    small_font = gen.load_font(28, True)
    watermark_font = gen.load_font(50, True)

    title = v4.clean_display_text(title, lang)
    y = TITLE_Y
    for line in base_batch.title_lines(title, lang, 2):
        gen.draw_highlighted_line(draw, line, title_terms, title_font, y, center=True)
        y += 62
    separator_y = y + 18
    draw.rounded_rectangle((96, separator_y, 984, separator_y + 8), radius=4, fill=ACCENT)

    stage_top = max(STAGE_TOP_MIN, separator_y + 56)
    stage = (86, stage_top, 994, stage_top + STANDARD_STAGE_H)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((104, stage_top + 20, 1012, stage_top + STANDARD_STAGE_H + 20), radius=38, fill=(0, 0, 0, 90))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(20)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=38, fill=(255, 255, 255, 238))
    if image_path:
        image = gen.fit_image(image_path)
        if image:
            image = ImageOps.contain(image.convert("RGB"), (stage[2] - stage[0] - 70, stage[3] - stage[1] - 50), method=Image.Resampling.LANCZOS)
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    v2.draw_avatar_pair(draw, str(seg.get("speaker", cfg["prefixes"][0])), cfg["prefixes"], BOX_TOP - 76, lang)
    draw.rounded_rectangle((86, BOX_TOP, 994, BOX_BOTTOM), radius=38, fill=(0, 0, 0, 190))
    label = cfg["host_label"] if seg["speaker"] == cfg["prefixes"][0] else cfg["analyst_label"]
    label_color = (37, 99, 235) if seg["speaker"] == cfg["prefixes"][0] else (32, 146, 128)
    label_right = 288 if lang == "en" else 238
    draw.rounded_rectangle((120, BOX_TOP + 30, label_right, BOX_TOP + 76), radius=23, fill=label_color)
    draw.text((138, BOX_TOP + 34), str(label), font=small_font, fill=WHITE)

    yy = BOX_TOP + 106
    max_lines = 4
    for line in str(seg.get("text", "")).split("\n")[:max_lines]:
        safe_line = v4.clean_display_text(line, lang)
        gen.draw_highlighted_line(draw, safe_line, list(seg.get("highlight_terms", [])), subtitle_font, yy, center=False)
        yy += 58
    if int(seg.get("page_count", 1)) > 1:
        draw.text((874, BOX_TOP + 38), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw_safe_bottom(draw, index, total, ZH_BRAND if lang == "zh" else EN_BRAND, small_font, watermark_font)
    canvas.convert("RGB").save(output, quality=93)


def draw_mixed_frame_safe(image_path: Path | None, title_zh: str, title_en: str, seg: dict[str, Any], output: Path, index: int, total: int) -> None:
    canvas = gen.background()
    draw = ImageDraw.Draw(canvas)
    title_font_zh = gen.load_font(48, True)
    title_font_en = gen.load_font(31, True)
    subtitle_font_en = gen.load_font(39, True)
    subtitle_font_zh = gen.load_font(37, True)
    small_font = gen.load_font(28, True)
    watermark_font = gen.load_font(50, True)

    title_zh = v4.sanitize_title(title_zh, "zh")
    title_en = v4.sanitize_title(title_en, "en")
    y = TITLE_Y
    for line in base_batch.title_lines(title_zh, "zh", 2):
        center_text(draw, line, title_font_zh, y, WHITE)
        y += 58
    for line in base_batch.wrap_words_balanced(title_en, 40, 2)[:2]:
        center_text(draw, line, title_font_en, y, SOFT_WHITE)
        y += 38
    separator_y = y + 14
    draw.rounded_rectangle((96, separator_y, 984, separator_y + 8), radius=4, fill=ACCENT)

    stage_top = max(STAGE_TOP_MIN + 18, separator_y + 48)
    stage = (86, stage_top, 994, stage_top + MIXED_STAGE_H)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((104, stage_top + 20, 1012, stage_top + MIXED_STAGE_H + 20), radius=38, fill=(0, 0, 0, 90))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(20)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=38, fill=(255, 255, 255, 238))
    if image_path:
        image = gen.fit_image(image_path)
        if image:
            image = ImageOps.contain(image.convert("RGB"), (stage[2] - stage[0] - 70, stage[3] - stage[1] - 50), method=Image.Resampling.LANCZOS)
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    prefixes = gen.LANGS["en"]["prefixes"]
    v2.draw_avatar_pair(draw, str(seg.get("speaker", prefixes[0])), prefixes, BOX_TOP - 76, "mixed")
    draw.rounded_rectangle((86, BOX_TOP, 994, BOX_BOTTOM), radius=38, fill=(0, 0, 0, 190))
    label = "Host" if seg.get("speaker") == prefixes[0] else "Guest"
    label_color = (37, 99, 235) if seg.get("speaker") == prefixes[0] else (32, 146, 128)
    draw.rounded_rectangle((120, BOX_TOP + 30, 278, BOX_TOP + 76), radius=23, fill=label_color)
    draw.text((138, BOX_TOP + 34), label, font=small_font, fill=WHITE)

    yy = BOX_TOP + 102
    en_terms = [v4.clean_display_text(str(t), "en") for t in seg.get("highlight_terms", []) if str(t)]
    for line in str(seg.get("text_en", "")).split("\n")[:2]:
        for safe_line in v4.wrap_by_pixel(draw, line, subtitle_font_en, 810, "en", 1):
            v4.draw_highlighted_line_local(draw, safe_line, en_terms, subtitle_font_en, 120, yy, WHITE, ACCENT)
            yy += 50
    yy += 8
    zh_source = v4.clean_display_text(str(seg.get("text_zh_raw") or seg.get("text_zh") or "").replace("\n", ""), "zh")
    zh_terms = [t for t in seg.get("highlight_terms_zh", []) if t and t in zh_source]
    if not zh_terms:
        zh_terms = v2.fallback_zh_highlights(zh_source, 2)
    for line in v4.wrap_by_pixel(draw, zh_source, subtitle_font_zh, 810, "zh", 3):
        v4.draw_highlighted_line_local(draw, line, zh_terms, subtitle_font_zh, 120, yy, WHITE, ACCENT)
        yy += 50
    if int(seg.get("page_count", 1)) > 1:
        draw.text((874, BOX_TOP + 38), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw_safe_bottom(draw, index, total, EN_BRAND, small_font, watermark_font)
    canvas.convert("RGB").save(output, quality=93)


def apply_safe_area_patch() -> None:
    # v4 first: title glyph cleanup, Latin word wrapping, and sensitive filtering.
    v4.apply_display_patch()
    # Then font and layout patches.
    gen.load_font = load_font_cjk_sans
    v2.gen.load_font = load_font_cjk_sans
    v2.draw_frame_v2 = draw_standard_frame_safe
    v2.draw_mixed_frame = draw_mixed_frame_safe


def main() -> int:
    apply_safe_area_patch()
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
