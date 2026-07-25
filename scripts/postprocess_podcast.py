#!/usr/bin/env python3
"""Post-process generated report folders.

Adds:
1. WeChat markdown image refs using original MinerU/source images.
2. English long-form article.
3. Conversational Chinese and English podcast scripts.
4. Separate Chinese/English WAV files.
5. Separate vertical Chinese/English MP4 videos with original MinerU charts, video title, and DeepSeek-selected subtitle highlights.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import textwrap
import wave
from pathlib import Path
from typing import Any

import requests

from deepseek_http import deepseek_api_keys_from_env, request_with_key_fallback
from PIL import Image, ImageDraw, ImageFont, ImageOps

VIDEO_SIZE = (1080, 1440)
VIDEO_BG = (9, 31, 64)
VIDEO_FPS = 24


def log(message: str) -> None:
    print(message, flush=True)


def as_bool(value: str | bool) -> bool:
    if isinstance(value, bool):
        return value
    return str(value).strip().lower() in {"1", "true", "yes", "y", "on"}


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    code = data.get("code")
    if response.status_code >= 400 or code not in (None, 0, "0"):
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:1000]}")
    return data


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_keys = deepseek_api_keys_from_env()
    if not api_keys:
        return f"未检测到 DEEPSEEK_API_KEY。请复制 prompt 手动生成：{label}\n"
    url = args.deepseek_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": args.model,
        "temperature": 0.72,
        "messages": [
            {"role": "system", "content": "你是专业财经内容制作人，输出必须可直接发布、朗读和制作视频。"},
            {"role": "user", "content": prompt},
        ],
    }
    response = request_with_key_fallback(
        url,
        headers={"Content-Type": "application/json"},
        payload=payload,
        label=label,
        api_keys=api_keys,
        timeout=180,
    )
    data = parse_json_response(response, f"DeepSeek generate {label}")
    return data["choices"][0]["message"]["content"].strip() + "\n"


def trim_source_text(source_text: str, prompt_chars: int) -> str:
    source_text = re.sub(r"\n{3,}", "\n\n", source_text).strip()
    if len(source_text) > prompt_chars:
        head_len = int(prompt_chars * 0.72)
        tail_len = int(prompt_chars * 0.22)
        source_text = source_text[:head_len] + "\n\n[中间内容因长度限制已省略]\n\n" + source_text[-tail_len:]
    return source_text


def build_podcast_prompt(template_path: Path, source_text: str, args: argparse.Namespace) -> str:
    return template_path.read_text(encoding="utf-8").format(
        podcast_minutes=args.podcast_minutes,
        source_text=trim_source_text(source_text, args.podcast_prompt_chars),
    )


def build_english_article_prompt(template_path: Path, source_text: str, args: argparse.Namespace) -> str:
    return template_path.read_text(encoding="utf-8").format(
        target_length=args.english_article_length,
        community_cta=args.english_community_cta,
        source_text=trim_source_text(source_text, args.english_article_prompt_chars),
    )


def find_original_images(item_dir: Path) -> list[str]:
    assets_dir = item_dir / "assets"
    if not assets_dir.exists():
        return []
    image_suffixes = {".png", ".jpg", ".jpeg", ".webp"}
    preferred = sorted(p for p in assets_dir.glob("source_image_*") if p.suffix.lower() in image_suffixes)
    if preferred:
        return [p.relative_to(item_dir).as_posix() for p in preferred]
    fallback = sorted(p for p in assets_dir.glob("mineru_original_*") if p.suffix.lower() in image_suffixes)
    if fallback:
        return [p.relative_to(item_dir).as_posix() for p in fallback]
    xhs_fallback = sorted(p for p in assets_dir.glob("xhs_card_*.png"))
    return [p.relative_to(item_dir).as_posix() for p in xhs_fallback]


def embed_original_images(article: str, image_paths: list[str], max_images: int = 3, alt: str = "研报原图") -> str:
    clean = [p for p in image_paths if p.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
    if not clean:
        return article
    article = re.sub(r"\n?!\[研报图表 \d+\]\(assets/xhs_card_\d+\.png\)\n?", "\n", article)
    article = re.sub(r"\n?!\[(?:研报原图|Report chart) \d+\]\(assets/[^\)]+\)\n?", "\n", article)
    images = [f"\n![{alt} {i}]({path})\n" for i, path in enumerate(clean[:max_images], 1)]
    lines = article.strip().splitlines()
    h2_indices = [idx for idx, line in enumerate(lines) if line.startswith("## ")]
    if h2_indices:
        offset = 0
        for img, original_idx in zip(images, h2_indices[:max_images]):
            lines.insert(original_idx + offset, img)
            offset += 1
    else:
        insert_at = min(len(lines), 6)
        for img in reversed(images):
            lines.insert(insert_at, img)
    return "\n".join(lines).strip() + "\n"


def extract_markdown_title(path: Path, fallback: str) -> str:
    if not path.exists():
        return fallback
    for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
        line = raw.strip()
        if line.startswith("# "):
            return re.sub(r"^#+\s*", "", line).strip()[:42] or fallback
    return fallback


def parse_script(script: str, prefixes: tuple[str, ...]) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    prefix_pattern = "|".join(re.escape(p) for p in prefixes)
    pattern = re.compile(rf"^({prefix_pattern})\s*[:：]\s*(.+)$", flags=re.IGNORECASE)
    for raw in script.splitlines():
        line = raw.strip().lstrip("-• ").strip()
        match = pattern.match(line)
        if match:
            speaker = match.group(1).upper()
            text = match.group(2).strip()
            if text:
                rows.append((speaker, text))
    return rows


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as src:
        return src.getnframes() / float(src.getframerate())


def wav_rate(path: Path) -> int:
    with wave.open(str(path), "rb") as src:
        return int(src.getframerate())


def run_ffmpeg(cmd: list[str], timeout: int = 600) -> None:
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="ignore")[-1200:])


def apply_voice_variation(segment: Path, speaker: str) -> Path:
    """Create a light A/B voice difference for Piper without downloading extra voice models."""
    if not speaker.endswith("_B") or not shutil.which("ffmpeg"):
        return segment
    rate = wav_rate(segment)
    shifted = segment.with_name(segment.stem + "_voice_b.wav")
    run_ffmpeg([
        "ffmpeg", "-y", "-i", str(segment),
        "-af", f"asetrate={int(rate * 0.94)},aresample={rate},atempo=1.06,volume=0.96",
        str(shifted),
    ], timeout=120)
    return shifted


def combine_wavs(segment_paths: list[Path], output_path: Path, silence_ms: int = 280) -> None:
    if not segment_paths:
        raise RuntimeError("No podcast audio segments were generated.")
    with wave.open(str(segment_paths[0]), "rb") as first:
        params = first.getparams()
    silence_frames = int(params.framerate * silence_ms / 1000)
    silence = b"\x00" * silence_frames * params.nchannels * params.sampwidth
    with wave.open(str(output_path), "wb") as out:
        out.setparams(params)
        for path in segment_paths:
            with wave.open(str(path), "rb") as src:
                out.writeframes(src.readframes(src.getnframes()))
                out.writeframes(silence)


def render_language_audio_piper(rows: list[tuple[str, str]], output_path: Path, model_path: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    piper_bin = shutil.which(args.piper_binary)
    if not piper_bin:
        raise RuntimeError("piper CLI not found. Make sure workflow installed piper-tts.")
    if not model_path.exists():
        raise RuntimeError(f"Piper model not found: {model_path}")
    timeline: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="podcast_segments_") as tmp:
        tmp_dir = Path(tmp)
        segment_paths: list[Path] = []
        cursor = 0.0
        for idx, (speaker, text) in enumerate(rows[:160], 1):
            segment = tmp_dir / f"segment_{idx:03d}.wav"
            result = subprocess.run([piper_bin, "--model", str(model_path), "--output_file", str(segment)], input=text.encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=120)
            if result.returncode != 0:
                raise RuntimeError(f"Piper failed on segment {idx}: {result.stderr.decode('utf-8', errors='ignore')[:500]}")
            final_segment = apply_voice_variation(segment, speaker)
            dur = wav_duration(final_segment)
            timeline.append({"speaker": speaker, "text": text, "start": round(cursor, 3), "end": round(cursor + dur, 3)})
            cursor += dur + 0.28
            segment_paths.append(final_segment)
        combine_wavs(segment_paths, output_path)
    return timeline


def edge_voice_for_speaker(speaker: str, args: argparse.Namespace) -> str:
    if speaker == "ZH_A":
        return args.edge_zh_a_voice
    if speaker == "ZH_B":
        return args.edge_zh_b_voice
    if speaker == "EN_A":
        return args.edge_en_a_voice
    if speaker == "EN_B":
        return args.edge_en_b_voice
    return args.edge_zh_a_voice if speaker.startswith("ZH") else args.edge_en_a_voice


def run_edge_tts(text: str, voice: str, out_mp3: Path) -> None:
    edge_bin = shutil.which("edge-tts")
    if edge_bin:
        cmd = [edge_bin, "--voice", voice, "--text", text, "--write-media", str(out_mp3)]
    else:
        cmd = [sys.executable, "-m", "edge_tts", "--voice", voice, "--text", text, "--write-media", str(out_mp3)]
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=180)
    if result.returncode != 0:
        raise RuntimeError(f"edge-tts failed: {result.stderr.decode('utf-8', errors='ignore')[:700]}")


def render_language_audio_edge(rows: list[tuple[str, str]], output_path: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg is required to convert edge-tts mp3 output to wav.")
    timeline: list[dict[str, Any]] = []
    with tempfile.TemporaryDirectory(prefix="edge_segments_") as tmp:
        tmp_dir = Path(tmp)
        segment_paths: list[Path] = []
        cursor = 0.0
        for idx, (speaker, text) in enumerate(rows[:160], 1):
            mp3 = tmp_dir / f"segment_{idx:03d}.mp3"
            wav = tmp_dir / f"segment_{idx:03d}.wav"
            run_edge_tts(text, edge_voice_for_speaker(speaker, args), mp3)
            run_ffmpeg(["ffmpeg", "-y", "-i", str(mp3), "-ar", "24000", "-ac", "1", str(wav)], timeout=120)
            dur = wav_duration(wav)
            timeline.append({"speaker": speaker, "text": text, "start": round(cursor, 3), "end": round(cursor + dur, 3)})
            cursor += dur + 0.28
            segment_paths.append(wav)
        combine_wavs(segment_paths, output_path)
    return timeline


def render_language_audio(rows: list[tuple[str, str]], output_path: Path, model_path: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    engine = args.tts_engine.lower().strip()
    if engine == "edge":
        return render_language_audio_edge(rows, output_path, args)
    if engine == "piper":
        return render_language_audio_piper(rows, output_path, model_path, args)
    raise RuntimeError(f"Unknown tts engine: {args.tts_engine}")


def load_font(size: int):
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def wrap_subtitle(text: str) -> list[str]:
    if re.search(r"[\u4e00-\u9fff]", text):
        return [text[i : i + 18] for i in range(0, len(text), 18)][:4]
    return textwrap.wrap(text, width=36)[:4]


def wrap_title(text: str) -> list[str]:
    if re.search(r"[\u4e00-\u9fff]", text):
        return [text[i : i + 15] for i in range(0, len(text), 15)][:2]
    return textwrap.wrap(text, width=31)[:2]


def parse_json_array(text: str) -> Any:
    text = text.strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    match = re.search(r"(\[.*\]|\{.*\})", text, flags=re.S)
    if not match:
        raise ValueError("No JSON object or array found")
    return json.loads(match.group(1))


def generate_highlights(rows: list[tuple[str, str]], args: argparse.Namespace, lang: str) -> dict[int, list[str]]:
    if not rows:
        return {}
    payload = [{"i": i, "text": text} for i, (_speaker, text) in enumerate(rows)]
    prompt = f"""
你是短视频财经字幕编辑。请为每一句字幕挑选 0-2 个最值得高亮的短语。
要求：
- 只返回 JSON 数组，不要解释。
- 每项格式：{{"i": 0, "phrases": ["短语1", "短语2"]}}
- phrases 必须是原句中连续出现的原文短语，不能改写。
- 不要高亮泛词；优先选择核心资产、行业变量、关键判断、风险变量、拐点、估值/利润/现金流等。
- 每个短语尽量 2-8 个中文字符或 1-4 个英文单词。
- 如果一句没有值得高亮的内容，phrases 为空数组。
语言：{lang}
字幕数据：
{json.dumps(payload[:120], ensure_ascii=False)}
""".strip()
    try:
        raw = call_deepseek(prompt, args, f"{lang} subtitle highlights")
        data = parse_json_array(raw)
        result: dict[int, list[str]] = {}
        if isinstance(data, dict):
            data = data.get("items", [])
        for item in data:
            if not isinstance(item, dict):
                continue
            idx = int(item.get("i", -1))
            phrases = [str(p).strip() for p in item.get("phrases", []) if str(p).strip()]
            if idx >= 0:
                result[idx] = phrases[:2]
        return result
    except Exception as exc:
        log(f"DeepSeek highlight generation failed for {lang}: {exc}")
        return {}


def split_highlight_chunks(line: str, phrases: list[str]) -> list[tuple[str, bool]]:
    phrases = [p for p in phrases if p and p in line]
    if not phrases:
        return [(line, False)]
    pattern = "|".join(re.escape(t) for t in sorted(phrases, key=len, reverse=True))
    chunks: list[tuple[str, bool]] = []
    pos = 0
    for match in re.finditer(pattern, line, flags=re.IGNORECASE):
        if match.start() > pos:
            chunks.append((line[pos : match.start()], False))
        chunks.append((match.group(0), True))
        pos = match.end()
    if pos < len(line):
        chunks.append((line[pos:], False))
    return chunks or [(line, False)]


def draw_highlighted_center(draw: ImageDraw.ImageDraw, line: str, y: int, font: ImageFont.ImageFont, phrases: list[str]) -> None:
    chunks = split_highlight_chunks(line, phrases)
    widths = [draw.textbbox((0, 0), chunk, font=font)[2] for chunk, _ in chunks]
    x = (VIDEO_SIZE[0] - sum(widths)) // 2
    for (chunk, highlight), width in zip(chunks, widths):
        fill = (255, 214, 102) if highlight else (255, 255, 255)
        draw.text((x, y), chunk, font=font, fill=fill)
        x += width


def make_video_frame(image_path: Path | None, subtitle: str, title: str, out_path: Path, highlight_phrases: list[str]) -> None:
    canvas = Image.new("RGB", VIDEO_SIZE, VIDEO_BG)
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(44)
    subtitle_font = load_font(44)
    speaker_font = load_font(30)

    y_title = 54
    for line in wrap_title(title):
        bbox = draw.textbbox((0, 0), line, font=title_font)
        draw.text(((VIDEO_SIZE[0] - (bbox[2] - bbox[0])) // 2, y_title), line, fill=(255, 255, 255), font=title_font)
        y_title += 56

    if image_path and image_path.exists():
        try:
            img = Image.open(image_path).convert("RGB")
            img = ImageOps.contain(img, (960, 700))
            card_x = (VIDEO_SIZE[0] - img.width) // 2
            card_y = 195
            draw.rounded_rectangle((card_x - 22, card_y - 22, card_x + img.width + 22, card_y + img.height + 22), radius=28, fill=(255, 255, 255))
            canvas.paste(img, (card_x, card_y))
        except Exception as exc:
            log(f"Cannot draw video image {image_path}: {exc}")

    wrapped = wrap_subtitle(subtitle)
    box_y = 1010
    draw.rounded_rectangle((54, box_y, 1026, 1320), radius=30, fill=(0, 0, 0))
    y = box_y + 38
    for line in wrapped:
        draw_highlighted_center(draw, line, y, subtitle_font, highlight_phrases)
        y += 60
    draw.text((76, 1358), "Kris笔记 Podcast", fill=(190, 206, 226), font=speaker_font)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(out_path, quality=92)


def render_video(audio_path: Path, timeline: list[dict[str, Any]], image_paths: list[Path], output_path: Path, title: str, highlights: dict[int, list[str]]) -> None:
    if not shutil.which("ffmpeg"):
        raise RuntimeError("ffmpeg not found. Make sure workflow installed ffmpeg.")
    if not timeline:
        raise RuntimeError("No timeline for video rendering.")
    with tempfile.TemporaryDirectory(prefix="podcast_video_") as tmp:
        tmp_dir = Path(tmp)
        concat_file = tmp_dir / "concat.txt"
        lines: list[str] = []
        for idx, seg in enumerate(timeline):
            img = image_paths[idx % len(image_paths)] if image_paths else None
            frame = tmp_dir / f"frame_{idx:04d}.png"
            make_video_frame(img, seg["text"], title, frame, highlights.get(idx, []))
            duration = max(0.8, float(seg["end"]) - float(seg["start"]) + 0.28)
            lines.append(f"file '{frame.as_posix()}'\n")
            lines.append(f"duration {duration:.3f}\n")
        lines.append(lines[-2])
        concat_file.write_text("".join(lines), encoding="utf-8")
        silent_video = tmp_dir / "silent.mp4"
        run_ffmpeg(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_file), "-vsync", "vfr", "-pix_fmt", "yuv420p", str(silent_video)])
        run_ffmpeg(["ffmpeg", "-y", "-i", str(silent_video), "-i", str(audio_path), "-c:v", "libx264", "-c:a", "aac", "-shortest", str(output_path)])


def process_item(item_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    status_path = item_dir / "status.json"
    status: dict[str, Any] = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8"))
        except Exception:
            status = {}

    image_paths = find_original_images(item_dir)
    article_path = item_dir / "wechat_article.md"
    if article_path.exists() and image_paths:
        article = article_path.read_text(encoding="utf-8", errors="ignore")
        article_path.write_text(embed_original_images(article, image_paths, max_images=args.max_wechat_images, alt="研报原图"), encoding="utf-8")
        status["wechat_images"] = image_paths[: args.max_wechat_images]

    source_path = item_dir / "source_mineru.md"
    if not source_path.exists():
        status["podcast_error"] = "source_mineru.md not found"
        status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return status

    source_text = source_path.read_text(encoding="utf-8", errors="ignore")

    en_article_prompt = build_english_article_prompt(Path(args.english_article_prompt_template), source_text, args)
    (item_dir / "prompt_for_wechat_en.md").write_text(en_article_prompt, encoding="utf-8")
    try:
        en_article = call_deepseek(en_article_prompt, args, "English WeChat-style article")
    except Exception as exc:
        en_article = f"DeepSeek generated English article failed: {exc}\n"
        status["wechat_en_error"] = str(exc)
    if image_paths:
        en_article = embed_original_images(en_article, image_paths, max_images=args.max_wechat_images, alt="Report chart")
    en_article_path = item_dir / "wechat_article_en.md"
    en_article_path.write_text(en_article, encoding="utf-8")
    status["wechat_article_en"] = "wechat_article_en.md"

    prompt = build_podcast_prompt(Path(args.podcast_prompt_template), source_text, args)
    (item_dir / "prompt_for_podcast.md").write_text(prompt, encoding="utf-8")
    try:
        script = call_deepseek(prompt, args, "conversational Chinese and English podcast scripts")
    except Exception as exc:
        script = f"DeepSeek 生成 podcast 脚本失败：{exc}\n"
        status["podcast_error"] = str(exc)
    (item_dir / "podcast_script.txt").write_text(script, encoding="utf-8")
    status["podcast_script"] = "podcast_script.txt"

    zh_rows = parse_script(script, ("ZH_A", "ZH_B"))
    en_rows = parse_script(script, ("EN_A", "EN_B"))
    (item_dir / "podcast_zh_script.txt").write_text("\n".join(f"{s}: {t}" for s, t in zh_rows) + "\n", encoding="utf-8")
    (item_dir / "podcast_en_script.txt").write_text("\n".join(f"{s}: {t}" for s, t in en_rows) + "\n", encoding="utf-8")

    zh_title = extract_markdown_title(article_path, "Kris笔记：研报播客")
    en_title = extract_markdown_title(en_article_path, "Kris Notes: Research Podcast")

    if as_bool(args.generate_audio):
        image_abs = [item_dir / p for p in image_paths]
        try:
            zh_highlights = generate_highlights(zh_rows, args, "Chinese")
            (item_dir / "podcast_zh_highlights.json").write_text(json.dumps(zh_highlights, ensure_ascii=False, indent=2), encoding="utf-8")
            zh_timeline = render_language_audio(zh_rows, item_dir / "podcast_zh.wav", Path(args.piper_zh_model), args)
            (item_dir / "podcast_zh_timeline.json").write_text(json.dumps(zh_timeline, ensure_ascii=False, indent=2), encoding="utf-8")
            status["podcast_zh_audio"] = "podcast_zh.wav"
            render_video(item_dir / "podcast_zh.wav", zh_timeline, image_abs, item_dir / "podcast_zh.mp4", zh_title, zh_highlights)
            status["podcast_zh_video"] = "podcast_zh.mp4"
        except Exception as exc:
            log(f"Chinese audio/video generation failed for {item_dir.name}: {exc}")
            status["podcast_zh_error"] = str(exc)
        try:
            en_highlights = generate_highlights(en_rows, args, "English")
            (item_dir / "podcast_en_highlights.json").write_text(json.dumps(en_highlights, ensure_ascii=False, indent=2), encoding="utf-8")
            en_timeline = render_language_audio(en_rows, item_dir / "podcast_en.wav", Path(args.piper_en_model), args)
            (item_dir / "podcast_en_timeline.json").write_text(json.dumps(en_timeline, ensure_ascii=False, indent=2), encoding="utf-8")
            status["podcast_en_audio"] = "podcast_en.wav"
            render_video(item_dir / "podcast_en.wav", en_timeline, image_abs, item_dir / "podcast_en.mp4", en_title, en_highlights)
            status["podcast_en_video"] = "podcast_en.mp4"
        except Exception as exc:
            log(f"English audio/video generation failed for {item_dir.name}: {exc}")
            status["podcast_en_error"] = str(exc)

    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="xhs_notes")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--podcast-prompt-template", default="prompts/podcast_zh_en_prompt.md")
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--podcast-prompt-chars", type=int, default=26000)
    parser.add_argument("--generate-audio", default="true")
    parser.add_argument("--tts-engine", default="edge", choices=["edge", "piper"])
    parser.add_argument("--max-wechat-images", type=int, default=3)
    parser.add_argument("--english-article-prompt-template", default="prompts/wechat_report_article_en_prompt.md")
    parser.add_argument("--english-article-length", type=int, default=2200)
    parser.add_argument("--english-article-prompt-chars", type=int, default=26000)
    parser.add_argument("--english-community-cta", default="Join the community to read the full report and review the original charts.")
    parser.add_argument("--piper-binary", default="piper")
    parser.add_argument("--piper-zh-model", default=".piper-voices/zh_CN-huayan-medium.onnx")
    parser.add_argument("--piper-en-model", default=".piper-voices/en_US-lessac-medium.onnx")
    parser.add_argument("--edge-zh-a-voice", default="zh-CN-XiaoxiaoNeural")
    parser.add_argument("--edge-zh-b-voice", default="zh-CN-YunxiNeural")
    parser.add_argument("--edge-en-a-voice", default="en-US-JennyNeural")
    parser.add_argument("--edge-en-b-voice", default="en-US-GuyNeural")
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    if not output_dir.exists():
        log(f"No output directory found: {output_dir}; skipping podcast postprocess.")
        return 0
    results = []
    for item_dir in sorted(p for p in output_dir.iterdir() if p.is_dir()):
        log(f"Post-processing {item_dir}")
        results.append({"item": item_dir.name, **process_item(item_dir, args)})
    (output_dir / "postprocess_summary.json").write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
