#!/usr/bin/env python3
"""Display-cleanup patch for Test bilingual podcast video.

Builds on v3 and fixes two mixed-video rendering issues:
- remove unsupported emoji/symbol glyphs from titles before drawing;
- keep embedded Latin names such as Waller as atomic tokens in Chinese subtitles,
  so highlights/wrapping do not split them into Wall + er.
"""
from __future__ import annotations

import re
import unicodedata
from typing import Any

import generate_test_podcast_video_eleven_batch_v2 as v2
import generate_test_podcast_video_eleven_batch_v3 as v3

SAFE_SYMBOLS = set("%$€£¥+−-/–—_=#&@.,;:!?()[]{}<>‘’'\"“”·…，。！？；：、（）《》【】")
BAD_TITLE_CHARS = set("□■☐☑☒�")


def clean_display_text(text: str, lang: str = "zh") -> str:
    """Remove glyphs that Noto CJK often renders as tofu boxes."""
    raw = v2.sanitize_sensitive_text(str(text or ""), lang)
    out: list[str] = []
    for ch in raw:
        if ch in BAD_TITLE_CHARS:
            continue
        cat = unicodedata.category(ch)
        if cat in {"Cc", "Cf", "Cs", "Co", "Cn"}:
            continue
        if cat.startswith("S") and ch not in SAFE_SYMBOLS:
            continue
        if cat.startswith("M"):
            continue
        out.append(ch)
    cleaned = "".join(out)
    cleaned = re.sub(r"\s+", " ", cleaned).strip()
    cleaned = re.sub(r"[\s,，:：;；\-–—]+$", "", cleaned).strip()
    return cleaned


def sanitize_title(title: str, lang: str) -> str:
    cleaned = clean_display_text(title, lang)
    cleaned = re.sub(r"^[#>*\-\s]+", "", cleaned).strip()
    return cleaned


def zh_units(text: str) -> list[str]:
    """Tokenize Chinese subtitles while keeping Latin words/numbers intact."""
    compact = re.sub(r"\s+", "", text or "")
    pattern = re.compile(
        r"[A-Za-z][A-Za-z0-9._%+-]*"
        r"|\d+(?:\.\d+)?%?"
        r"|[，。！？；：、,.!?;:]"
        r"|[\u4e00-\u9fff]"
        r"|."
    )
    return [m.group(0) for m in pattern.finditer(compact) if m.group(0)]


def wrap_by_pixel(draw: Any, text: str, font: Any, max_width: int, lang: str, max_lines: int) -> list[str]:
    text = clean_display_text(text, lang)
    if not text:
        return []
    units = text.split() if lang == "en" else zh_units(text)
    lines: list[str] = []
    current = ""
    for unit in units:
        sep = " " if lang == "en" and current else ""
        candidate = f"{current}{sep}{unit}" if current else unit
        if v2.text_size(draw, candidate, font)[0] <= max_width:
            current = candidate
            continue
        if current:
            # Avoid leaving a Latin word fragment at the end: because Latin words are atomic,
            # the entire word will move to the next line when it does not fit.
            lines.append(current)
        # If a single token is too wide, only then fall back to character slicing.
        if v2.text_size(draw, unit, font)[0] > max_width and re.match(r"^[A-Za-z0-9._%+-]+$", unit):
            buf = ""
            for ch in unit:
                cand = buf + ch
                if v2.text_size(draw, cand, font)[0] <= max_width:
                    buf = cand
                else:
                    if buf:
                        lines.append(buf)
                    buf = ch
                    if len(lines) >= max_lines:
                        break
            current = buf
        else:
            current = unit
        if len(lines) >= max_lines:
            break
    if current and len(lines) < max_lines:
        lines.append(current)
    return lines[:max_lines]


def draw_highlighted_line_local(
    draw: Any,
    line: str,
    terms: list[str],
    font: Any,
    x: int,
    y: int,
    normal_fill: tuple[int, int, int],
    highlight_fill: tuple[int, int, int] = v2.ACCENT,
) -> None:
    # Clean line and terms first, then reuse v3's boundary-aware highlighter.
    lang = "zh" if v3.has_cjk(line) else "en"
    safe_line = clean_display_text(line, lang)
    safe_terms = [clean_display_text(str(t), "zh" if v3.has_cjk(str(t)) else "en") for t in terms]
    # Do not highlight Latin partials inside Chinese text unless the whole token is present.
    filtered: list[str] = []
    for term in safe_terms:
        if not term or term not in safe_line:
            continue
        if re.match(r"^[A-Za-z][A-Za-z0-9._%+-]*$", term):
            if not re.search(rf"(?<![A-Za-z0-9._%+-]){re.escape(term)}(?![A-Za-z0-9._%+-])", safe_line):
                continue
        filtered.append(term)
    return v3.draw_highlighted_line_local(draw, safe_line, filtered, font, x, y, normal_fill, highlight_fill)


def apply_display_patch() -> None:
    v3.apply_boundary_patch()
    v2.sanitize_title = sanitize_title
    v2.wrap_by_pixel = wrap_by_pixel
    v2.draw_highlighted_line_local = draw_highlighted_line_local


def main() -> int:
    apply_display_patch()
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
