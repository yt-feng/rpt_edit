#!/usr/bin/env python3
"""Batch wrapper for bilingual ElevenLabs podcast/video test.

This wrapper reuses generate_test_podcast_video_eleven.py and adds the latest
visual requirements:
- both speakers are male; the second speaker uses the requested ElevenLabs ID;
- up to N generated report folders are processed;
- output mode can produce all variants or only the mixed bilingual video/audio;
- speaker avatars are drawn above the subtitle panel;
- English/Chinese title wrapping avoids overlap and awkward one-character lines;
- All language variants use the KC桌面 watermark.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import tempfile
from pathlib import Path
from typing import Any

from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

import generate_test_podcast_video_eleven as gen

SECOND_MALE_VOICE_ID = "bdt3B5N3GXM2nOc0SUW7"
EN_BRAND = "KC桌面"
ZH_BRAND = "KC桌面"
SIZE = (1080, 1920)
ACCENT = (255, 214, 102)


def log(message: str) -> None:
    print(message, flush=True)


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


def text_size(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont) -> tuple[int, int]:
    box = draw.textbbox((0, 0), text, font=font)
    return box[2] - box[0], box[3] - box[1]


def wrap_words_balanced(text: str, max_chars: int, max_lines: int = 2) -> list[str]:
    words = re.sub(r"\s+", " ", text or "").strip().split()
    if not words:
        return [""]
    if len(" ".join(words)) <= max_chars:
        return [" ".join(words)]
    if max_lines <= 1:
        return [" ".join(words)[:max_chars]]
    total = " ".join(words)
    best: tuple[int, list[str]] | None = None
    for i in range(1, len(words)):
        left = " ".join(words[:i])
        right = " ".join(words[i:])
        if len(left) > max_chars or len(right) > max_chars:
            continue
        score = abs(len(left) - len(right))
        if best is None or score < best[0]:
            best = (score, [left, right])
    if best:
        return best[1]
    lines: list[str] = []
    current = ""
    for word in words:
        candidate = (current + " " + word).strip()
        if len(candidate) <= max_chars:
            current = candidate
        else:
            if current:
                lines.append(current)
            current = word
        if len(lines) >= max_lines - 1:
            break
    if current:
        rest_words = words[sum(len(x.split()) for x in lines):]
        rest = " ".join(rest_words)
        lines.append(rest[:max_chars])
    return lines[:max_lines]


def split_chinese_balanced(text: str, max_chars: int = 15) -> list[str]:
    text = re.sub(r"\s+", "", text or "").strip()
    if not text:
        return [""]
    if len(text) <= max_chars:
        return [text]
    comma_positions = [m.end() for m in re.finditer(r"[，,；;：:]", text)]
    if comma_positions:
        midpoint = len(text) / 2
        pos = min(comma_positions, key=lambda p: abs(p - midpoint))
        left, right = text[:pos], text[pos:]
        if len(left) >= 4 and len(right) >= 4:
            return [left, right]
    best = len(text) // 2
    for delta in range(0, len(text)):
        for pos in (best - delta, best + delta):
            if 4 <= pos <= len(text) - 4:
                return [text[:pos], text[pos:]]
    return [text[:max_chars], text[max_chars:max_chars * 2]]


def title_lines(title: str, lang: str, max_lines: int = 2) -> list[str]:
    title = re.sub(r"\s+", " ", title or "").strip()
    if lang == "zh" or re.search(r"[\u4e00-\u9fff]", title):
        lines = split_chinese_balanced(title, 15)
    else:
        lines = wrap_words_balanced(title, 28, max_lines=max_lines)
    return [line for line in lines if line][:max_lines]


def draw_text_center(draw: ImageDraw.ImageDraw, text: str, font: ImageFont.ImageFont, y: int, fill: tuple[int, int, int]) -> None:
    w, _ = text_size(draw, text, font)
    draw.text(((SIZE[0] - w) // 2, y), text, font=font, fill=fill)


def draw_avatar_pair(draw: ImageDraw.ImageDraw, speaker: str, prefixes: tuple[str, str], y: int, lang: str) -> None:
    labels = ("A", "B")
    names = ("Host", "Guest") if lang in {"en", "mixed"} else ("主持", "嘉宾")
    colors = ((37, 99, 235), (32, 146, 128))
    centers = ((140, y), (245, y))
    active_index = 0 if speaker == prefixes[0] else 1
    font = gen.load_font(30, True)
    small = gen.load_font(20, True)
    for i, (cx, cy) in enumerate(centers):
        active = i == active_index
        r = 42 if active else 34
        draw.ellipse((cx - r, cy - r, cx + r, cy + r), fill=colors[i], outline=ACCENT if active else (210, 220, 235), width=5 if active else 2)
        w, h = text_size(draw, labels[i], font)
        draw.text((cx - w / 2, cy - h / 2 - 2), labels[i], font=font, fill=(255, 255, 255))
        nw, _ = text_size(draw, names[i], small)
        draw.text((cx - nw / 2, cy + r + 4), names[i], font=small, fill=(230, 238, 250))


def draw_frame_v2(image_path: Path | None, title: str, title_terms: list[str], seg: dict[str, Any], output: Path, index: int, total: int, lang: str) -> None:
    cfg = gen.LANGS[lang]
    canvas = gen.background()
    draw = ImageDraw.Draw(canvas)
    title_font = gen.load_font(52, True)
    subtitle_font = gen.load_font(48, True)
    small_font = gen.load_font(30)
    watermark_font = gen.load_font(54, True)

    y = 54
    lines = title_lines(title, lang, 2)
    for line in lines:
        gen.draw_highlighted_line(draw, line, title_terms, title_font, y, center=True)
        y += 68
    separator_y = y + 18
    draw.rounded_rectangle((78, separator_y, 1002, separator_y + 8), radius=4, fill=ACCENT)

    stage_top = max(260, separator_y + 62)
    stage = (70, stage_top, 1010, stage_top + 820)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((88, stage_top + 22, 1028, stage_top + 842), radius=42, fill=(0, 0, 0, 100))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(22)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=42, fill=(255, 255, 255, 238))
    if image_path:
        image = gen.fit_image(image_path)
        if image:
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    box_top = 1210
    avatar_y = box_top - 66
    draw_avatar_pair(draw, str(seg.get("speaker", cfg["prefixes"][0])), cfg["prefixes"], avatar_y, lang)
    draw.rounded_rectangle((70, box_top, 1010, 1668), radius=38, fill=(0, 0, 0, 185))
    label = cfg["host_label"] if seg["speaker"] == cfg["prefixes"][0] else cfg["analyst_label"]
    label_color = (37, 99, 235) if seg["speaker"] == cfg["prefixes"][0] else (32, 146, 128)
    label_right = 290 if lang == "en" else 248
    draw.rounded_rectangle((116, box_top + 34, label_right, box_top + 82), radius=24, fill=label_color)
    draw.text((136, box_top + 38), str(label), font=small_font, fill=(255, 255, 255))

    yy = box_top + 118
    for line in str(seg["text"]).split("\n")[: int(cfg["max_subtitle_lines"])] :
        gen.draw_highlighted_line(draw, line, list(seg.get("highlight_terms", [])), subtitle_font, yy, center=False)
        yy += 66
    if int(seg.get("page_count", 1)) > 1:
        draw.text((900, box_top + 40), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw.text((70, 1728), f"{index + 1}/{total}", font=small_font, fill=(200, 215, 235))
    progress = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress, 1752), radius=6, fill=ACCENT)
    watermark = ZH_BRAND if lang == "zh" else EN_BRAND
    w, _ = text_size(draw, watermark, watermark_font)
    draw.text(((SIZE[0] - w) // 2, 1802), watermark, font=watermark_font, fill=(205, 220, 238))
    canvas.convert("RGB").save(output, quality=93)


def translate_english_lines_to_zh(timeline: list[dict[str, Any]], args: argparse.Namespace) -> dict[int, str]:
    payload = [{"i": i, "text": seg.get("text", "")} for i, seg in enumerate(timeline)]
    prompt = f"""
Translate these English short-video subtitle lines into concise natural Chinese.
Return JSON only: {{"lines":[{{"i":0,"zh":"..."}}]}}
Keep each Chinese line short, neutral, and suitable for on-screen subtitles.
Do not include markdown.

Lines:
{json.dumps(payload, ensure_ascii=False)}
""".strip()
    try:
        data = gen.extract_json(gen.deepseek(prompt, args, temperature=0.15))
        result: dict[int, str] = {}
        for row in data.get("lines", []):
            idx = int(row.get("i"))
            result[idx] = gen.sanitize_public_text(str(row.get("zh", "")), "zh")
        return result
    except Exception as exc:
        log(f"Chinese subtitle translation failed, using empty Chinese captions: {exc}")
        return {}


def wrap_mixed_pages(seg: dict[str, Any], zh_text: str) -> list[dict[str, Any]]:
    en_lines = gen.wrap_text(str(seg.get("text", "")), 32, "en")
    zh_lines = title_lines(zh_text, "zh", 2) if zh_text else []
    # Keep each visual page compact: 2 English lines + 2 Chinese lines.
    en_pages = [en_lines[i:i + 2] for i in range(0, len(en_lines), 2)] or [[]]
    pages: list[dict[str, Any]] = []
    duration = max(0.5, float(seg["end"]) - float(seg["start"]))
    page_dur = duration / len(en_pages)
    for page_idx, en_page in enumerate(en_pages):
        item = dict(seg)
        item["text_en"] = "\n".join(en_page)
        item["text_zh"] = "\n".join(zh_lines[:2])
        item["page_index"] = page_idx + 1
        item["page_count"] = len(en_pages)
        item["start"] = round(float(seg["start"]) + page_idx * page_dur, 3)
        item["end"] = round(float(seg["start"]) + (page_idx + 1) * page_dur, 3)
        pages.append(item)
    return pages


def draw_mixed_frame(image_path: Path | None, title_zh: str, title_en: str, seg: dict[str, Any], output: Path, index: int, total: int) -> None:
    canvas = gen.background()
    draw = ImageDraw.Draw(canvas)
    title_font_zh = gen.load_font(52, True)
    title_font_en = gen.load_font(34, True)
    subtitle_font_en = gen.load_font(42, True)
    subtitle_font_zh = gen.load_font(44, True)
    small_font = gen.load_font(30)
    watermark_font = gen.load_font(54, True)

    y = 50
    for line in title_lines(title_zh, "zh", 2):
        draw_text_center(draw, line, title_font_zh, y, (255, 255, 255))
        y += 64
    for line in wrap_words_balanced(title_en, 36, 2)[:2]:
        draw_text_center(draw, line, title_font_en, y, (220, 232, 248))
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
    yy = box_top + 118
    for line in str(seg.get("text_en", "")).split("\n")[:2]:
        draw.text((120, yy), line, font=subtitle_font_en, fill=(255, 255, 255))
        yy += 58
    yy += 8
    for line in str(seg.get("text_zh", "")).split("\n")[:2]:
        draw.text((120, yy), line, font=subtitle_font_zh, fill=ACCENT)
        yy += 60
    if int(seg.get("page_count", 1)) > 1:
        draw.text((900, box_top + 40), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw.text((70, 1728), f"{index + 1}/{total}", font=small_font, fill=(200, 215, 235))
    progress = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress, 1752), radius=6, fill=ACCENT)
    w, _ = text_size(draw, EN_BRAND, watermark_font)
    draw.text(((SIZE[0] - w) // 2, 1802), EN_BRAND, font=watermark_font, fill=(205, 220, 238))
    canvas.convert("RGB").save(output, quality=93)


def make_mixed_video(item_dir: Path, args: argparse.Namespace, status: dict[str, Any]) -> dict[str, Any]:
    en_timeline_path = item_dir / "podcast_en_timeline.json"
    en_audio_path = item_dir / "podcast_en.wav"
    if not en_timeline_path.exists() or not en_audio_path.exists():
        raise RuntimeError("English timeline/audio missing; generate English podcast first")
    en_timeline = json.loads(en_timeline_path.read_text(encoding="utf-8"))
    zh_map = translate_english_lines_to_zh(en_timeline, args)
    visual: list[dict[str, Any]] = []
    for i, seg in enumerate(en_timeline):
        visual.extend(wrap_mixed_pages(seg, zh_map.get(i, "")))
    title_zh = str(status.get("podcast_zh_title") or "研报讲解")
    title_en = str(status.get("podcast_en_title") or "Research Briefing")
    images = gen.report_images(item_dir)
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
    }


def normalize_output_mode(value: str) -> str:
    mode = str(value or "all").strip().lower().replace("-", "_")
    if mode in {"bilingual", "bilingual_only", "mixed", "mixed_only"}:
        return "bilingual_only"
    if mode == "all":
        return "all"
    raise RuntimeError(f"Unsupported output mode: {value}")


def outputs_for_mode(mode: str, extract_mixed_audio: bool = False) -> list[str]:
    if mode == "bilingual_only":
        return ["podcast_mixed_bilingual_explainer.mp4", "podcast_mixed_bilingual_audio.m4a"]
    outputs = ["podcast_zh_explainer.mp4", "podcast_en_explainer.mp4", "podcast_mixed_bilingual_explainer.mp4"]
    if extract_mixed_audio:
        outputs.append("podcast_mixed_bilingual_audio.m4a")
    return outputs


def extract_mixed_audio(item_dir: Path) -> dict[str, Any]:
    video = item_dir / "podcast_mixed_bilingual_explainer.mp4"
    audio = item_dir / "podcast_mixed_bilingual_audio.m4a"
    if not video.exists():
        raise RuntimeError(f"Mixed bilingual video missing: {video}")
    gen.run(["ffmpeg", "-y", "-i", str(video), "-map", "0:a:0", "-vn", "-c:a", "copy", str(audio)], timeout=300)
    return {
        "podcast_mixed_audio": audio.name,
        "podcast_mixed_audio_source": video.name,
        "podcast_mixed_render_audio_source": "podcast_en.wav",
        "podcast_mixed_audio_extracted_from": video.name,
        "podcast_mixed_audio_extraction": "ffmpeg -c:a copy from final mixed video",
    }


def remove_intermediate_english_audio(item_dir: Path, status_update: dict[str, Any]) -> None:
    audio = item_dir / "podcast_en.wav"
    if audio.exists():
        audio.unlink()
        status_update["podcast_en_audio_intermediate_removed"] = audio.name
    status_update.pop("podcast_en_audio", None)


def apply_runtime_patches() -> None:
    # Force the B-speaker voice in both Chinese and English to the requested male voice.
    gen.LANGS["zh"]["voice_b"] = SECOND_MALE_VOICE_ID
    gen.LANGS["en"]["voice_b"] = SECOND_MALE_VOICE_ID
    gen.LANGS["zh"]["analyst_label"] = "嘉宾"
    gen.LANGS["en"]["analyst_label"] = "Guest"
    gen.LANGS["en"]["show_name"] = EN_BRAND
    gen.LANGS["en"]["branded_opening"] = "Welcome to KC桌面. Today we are unpacking one fresh research report and the question it raises."
    gen.draw_frame = draw_frame_v2


def process_one(item_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    raw_source = (item_dir / "source_mineru.md").read_text(encoding="utf-8", errors="ignore")
    source_text = gen.trim(gen.sanitize_public_text(raw_source, "zh"), args.prompt_chars)
    output_mode = normalize_output_mode(args.output_mode)
    status_update: dict[str, Any] = {
        "podcast_video_watermark_zh": ZH_BRAND,
        "podcast_video_watermark_en": EN_BRAND,
        "podcast_tts_engine_actual": "elevenlabs",
        "podcast_output_mode": output_mode,
        "subtitle_source": "same text as TTS; role tags normalized; rows split by punctuation before TTS; long visual subtitles are paged",
        "highlight_source": "DeepSeek title and subtitle keyword analysis",
        "sensitive_filter": "local xhs_notes-style replacements before TTS and rendering",
        "batch_wrapper": "generate_test_podcast_video_eleven_batch.py",
        "speaker_avatar_style": "fixed circular A/B avatars above subtitle panel",
        "second_speaker_voice_id": SECOND_MALE_VOICE_ID,
    }

    if output_mode == "bilingual_only":
        log(f"Generating EN podcast audio/timeline only for MIXED bilingual video for {item_dir.name}")
        status_update.update(gen.generate_language(item_dir, "en", source_text, args, render_video=False))
        status_update["podcast_zh_title"] = gen.report_title(item_dir, "zh", source_text, args)
        status_update["podcast_zh_title_source"] = "report metadata only; Chinese standalone TTS/video skipped"
        status_update["podcast_tts_passes"] = 1
        log(f"Generating MIXED bilingual video for {item_dir.name}")
        status_update.update(make_mixed_video(item_dir, args, status_update))
        status_update.update(extract_mixed_audio(item_dir))
        remove_intermediate_english_audio(item_dir, status_update)
    else:
        status_update["podcast_tts_passes"] = 2
        for lang in ["zh", "en"]:
            log(f"Generating {lang.upper()} podcast audio/video for {item_dir.name}")
            status_update.update(gen.generate_language(item_dir, lang, source_text, args))
        log(f"Generating MIXED bilingual video for {item_dir.name}")
        status_update.update(make_mixed_video(item_dir, args, status_update))
        if args.extract_mixed_audio:
            status_update.update(extract_mixed_audio(item_dir))

    status_path = item_dir / "status.json"
    status = load_status(status_path)
    status.update(status_update)
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return status_update


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-items", type=int, default=5)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--prompt-chars", type=int, default=26000)
    parser.add_argument("--output-mode", default=os.getenv("PODCAST_VIDEO_OUTPUT_MODE", "all"), help="all or bilingual_only")
    parser.add_argument("--extract-mixed-audio", action="store_true", help="also write podcast_mixed_bilingual_audio.m4a from the final mixed video")
    parser.add_argument("--eleven-base-url", default=os.getenv("ELEVEN_BASE_URL", "https://api.elevenlabs.io"))
    parser.add_argument("--eleven-model", default="eleven_multilingual_v2")
    parser.add_argument("--output-format", default="mp3_44100_128")
    parser.add_argument("--stability", type=float, default=0.45)
    parser.add_argument("--similarity-boost", type=float, default=0.78)
    parser.add_argument("--style", type=float, default=0.18)
    args = parser.parse_args()

    apply_runtime_patches()
    output_dir = Path(args.output_dir)
    item_dirs = find_item_dirs(output_dir, args.max_items)
    output_mode = normalize_output_mode(args.output_mode)
    summary: dict[str, Any] = {
        "max_items": args.max_items,
        "processed_count": 0,
        "output_mode": output_mode,
        "second_speaker_voice_id": SECOND_MALE_VOICE_ID,
        "outputs_per_item": outputs_for_mode(output_mode, args.extract_mixed_audio),
        "items": [],
    }
    for idx, item_dir in enumerate(item_dirs, 1):
        log(f"[{idx}/{len(item_dirs)}] Processing podcast/video for {item_dir}")
        try:
            status = process_one(item_dir, args)
            summary["processed_count"] += 1
            summary["items"].append({"item_dir": str(item_dir), "status": "ok", "outputs": status})
        except Exception as exc:
            log(f"ERROR processing {item_dir}: {exc}")
            summary["items"].append({"item_dir": str(item_dir), "status": "failed", "error": str(exc)})
            raise
    (output_dir / "bilingual_podcast_video_batch_summary.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"Generated bilingual podcast/video outputs for {summary['processed_count']} report folders")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
