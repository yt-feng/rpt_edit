#!/usr/bin/env python3
"""Generate a Chinese two-male-voice podcast and vertical explainer video.

This test script uses ElevenLabs for TTS through the ELEVEN_KEY secret.
The subtitle text is the exact text sent to TTS, and each video frame duration
is based on the measured duration of that exact audio segment.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import tempfile
import wave
from pathlib import Path
from typing import Any

import requests
from PIL import Image, ImageDraw, ImageFilter, ImageFont, ImageOps

SIZE = (1080, 1920)
BG = (9, 31, 64)
ACCENT = (255, 214, 102)
WATERMARK = "KC桌面"
VOICE_A_FALLBACK = "pNInz6obpgDQGcFmaJgB"
VOICE_B_FALLBACK = "ErXwobaYiN019PkySvjV"


def log(message: str) -> None:
    print(message, flush=True)


def run(cmd: list[str], timeout: int = 600) -> None:
    log("$ " + " ".join(cmd))
    proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout)
    if proc.returncode:
        raise RuntimeError(proc.stderr.decode("utf-8", errors="ignore")[-2400:])


def post_json(url: str, headers: dict[str, str], payload: dict[str, Any], timeout: int = 240) -> dict[str, Any]:
    response = requests.post(url, headers=headers, json=payload, timeout=timeout)
    if response.status_code >= 400:
        raise RuntimeError(f"HTTP {response.status_code}: {response.text[:1000]}")
    return response.json()


def deepseek(prompt: str, args: argparse.Namespace, temperature: float = 0.72) -> str:
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    data = post_json(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        {
            "model": args.model,
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": "你是中文播客制作人，输出适合男声双人对话朗读的脚本。"},
                {"role": "user", "content": prompt},
            ],
        },
    )
    return data["choices"][0]["message"]["content"].strip() + "\n"


def find_item(output_dir: Path) -> Path:
    items = [p for p in output_dir.iterdir() if p.is_dir() and (p / "source_mineru.md").exists()]
    if not items:
        raise RuntimeError(f"No generated report folder with source_mineru.md under {output_dir}")
    return sorted(items)[0]


def trim(text: str, limit: int) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text or "").strip()
    if len(text) <= limit:
        return text
    head = int(limit * 0.72)
    tail = int(limit * 0.22)
    return text[:head] + "\n\n[中间内容省略]\n\n" + text[-tail:]


def normalize_text(text: str) -> str:
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"[\[\]（）(){}]", "", text)
    text = text.replace("：", "，")
    return text


def parse_script(script: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    pattern = re.compile(r"^(ZH_A|ZH_B)\s*[:：]\s*(.+)$", re.I)
    for raw in script.splitlines():
        match = pattern.match(raw.strip().lstrip("-• ").strip())
        if match:
            speaker = match.group(1).upper()
            text = normalize_text(match.group(2))
            if text:
                rows.append((speaker, text))
    return rows


def eleven_key() -> str:
    key = os.getenv("ELEVEN_KEY") or os.getenv("ELEVENLABS_API_KEY")
    if not key:
        raise RuntimeError("Missing ELEVEN_KEY. Please add it to repo secrets.")
    return key


def score_voice(voice: dict[str, Any]) -> int:
    blob = (json.dumps(voice.get("labels") or {}, ensure_ascii=False) + " " + str(voice.get("name", ""))).lower()
    score = 0
    if "male" in blob or "男" in blob:
        score += 10
    if any(word in blob for word in ["deep", "calm", "professional", "narration", "news", "authoritative"]):
        score += 3
    if any(word in blob for word in ["chinese", "mandarin", "中文", "普通话"]):
        score += 2
    return score


def choose_voices(args: argparse.Namespace, item_dir: Path) -> tuple[str, str]:
    voice_a = args.voice_a_id
    voice_b = args.voice_b_id
    if voice_a != "auto" and voice_b != "auto":
        return voice_a, voice_b
    try:
        response = requests.get(
            args.eleven_base_url.rstrip("/") + "/v1/voices",
            headers={"xi-api-key": eleven_key()},
            timeout=45,
        )
        if response.status_code >= 400:
            raise RuntimeError(response.text[:800])
        voices = response.json().get("voices") or []
        voices = sorted([v for v in voices if v.get("voice_id")], key=score_voice, reverse=True)
        if voices and voice_a == "auto":
            voice_a = str(voices[0]["voice_id"])
        if voices and voice_b == "auto":
            pick = next((v for v in voices if str(v["voice_id"]) != voice_a), voices[0])
            voice_b = str(pick["voice_id"])
        (item_dir / "elevenlabs_selected_voices.json").write_text(json.dumps(voices[:8], ensure_ascii=False, indent=2), encoding="utf-8")
    except Exception as exc:
        log(f"ElevenLabs voice auto-select failed; using fallback male voices: {exc}")
    if voice_a == "auto":
        voice_a = VOICE_A_FALLBACK
    if voice_b == "auto" or voice_b == voice_a:
        voice_b = VOICE_B_FALLBACK
    return voice_a, voice_b


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as wav:
        return wav.getnframes() / float(wav.getframerate())


def combine_wavs(parts: list[Path], output: Path, silence_ms: int = 360) -> None:
    if not parts:
        raise RuntimeError("No audio parts to combine")
    with wave.open(str(parts[0]), "rb") as first:
        params = first.getparams()
    silence = b"\x00" * int(params.framerate * silence_ms / 1000) * params.nchannels * params.sampwidth
    with wave.open(str(output), "wb") as dst:
        dst.setparams(params)
        for part in parts:
            with wave.open(str(part), "rb") as src:
                dst.writeframes(src.readframes(src.getnframes()))
            dst.writeframes(silence)


def eleven_tts(text: str, voice_id: str, mp3_path: Path, wav_path: Path, args: argparse.Namespace) -> None:
    response = requests.post(
        args.eleven_base_url.rstrip("/") + f"/v1/text-to-speech/{voice_id}",
        params={"output_format": args.output_format},
        headers={"xi-api-key": eleven_key(), "Content-Type": "application/json"},
        json={
            "text": text,
            "model_id": args.eleven_model,
            "language_code": "zh",
            "voice_settings": {
                "stability": args.stability,
                "similarity_boost": args.similarity_boost,
                "style": args.style,
                "use_speaker_boost": True,
            },
        },
        timeout=180,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"ElevenLabs TTS failed: HTTP {response.status_code}: {response.text[:1000]}")
    mp3_path.write_bytes(response.content)
    run(["ffmpeg", "-y", "-i", str(mp3_path), "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", str(wav_path)], timeout=180)


def make_audio(rows: list[tuple[str, str]], item_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    voice_a, voice_b = choose_voices(args, item_dir)
    timeline: list[dict[str, Any]] = []
    wav_parts: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="eleven_segments_") as temp_dir:
        tmp = Path(temp_dir)
        cursor = 0.0
        for index, (speaker, text) in enumerate(rows[:120], 1):
            mp3 = tmp / f"seg_{index:03d}.mp3"
            wav = tmp / f"seg_{index:03d}.wav"
            voice_id = voice_a if speaker == "ZH_A" else voice_b
            eleven_tts(text, voice_id, mp3, wav, args)
            duration = wav_duration(wav)
            timeline.append({
                "speaker": speaker,
                "text": text,
                "start": round(cursor, 3),
                "end": round(cursor + duration, 3),
                "voice_id": voice_id,
                "tts_engine": "elevenlabs",
            })
            cursor += duration + 0.36
            wav_parts.append(wav)
        combine_wavs(wav_parts, item_dir / "podcast_zh.wav")
    log(f"ElevenLabs voices used: ZH_A={voice_a}, ZH_B={voice_b}")
    return timeline


def srt_time(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hh, rem = divmod(total_ms, 3600000)
    mm, rem = divmod(rem, 60000)
    ss, ms = divmod(rem, 1000)
    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"


def write_srt(timeline: list[dict[str, Any]], path: Path) -> None:
    blocks: list[str] = []
    for index, seg in enumerate(timeline, 1):
        label = "主持人" if seg["speaker"] == "ZH_A" else "研究员"
        blocks.append(f"{index}\n{srt_time(float(seg['start']))} --> {srt_time(float(seg['end']))}\n{label}：{seg['text']}\n")
    path.write_text("\n".join(blocks), encoding="utf-8")


def load_font(size: int, bold: bool = False) -> ImageFont.ImageFont:
    candidates = [
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/noto/NotoSansCJK-Bold.ttc" if bold else "/usr/share/fonts/truetype/noto/NotoSansCJK-Regular.ttc",
        "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf" if bold else "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
    ]
    for candidate in candidates:
        if Path(candidate).exists():
            return ImageFont.truetype(candidate, size)
    return ImageFont.load_default()


def wrap_text(text: str, width: int) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    return [text[i : i + width] for i in range(0, len(text), width)] or [""]


def report_images(item_dir: Path) -> list[Path]:
    assets = item_dir / "assets"
    if not assets.exists():
        return []
    suffixes = {".png", ".jpg", ".jpeg", ".webp"}
    source_images = sorted(p for p in assets.glob("source_image_*") if p.suffix.lower() in suffixes)
    return source_images or sorted(p for p in assets.glob("xhs_card_*.png") if p.suffix.lower() in suffixes)


def report_title(item_dir: Path) -> str:
    for filename in ["note.md", "wechat_article.md"]:
        path = item_dir / filename
        if path.exists():
            for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
                line = re.sub(r"^[#>*\-\s]+", "", raw).strip()
                if line and not line.startswith("封面"):
                    return line[:34]
    return "研报讲解"


def background() -> Image.Image:
    base = Image.new("RGB", SIZE, BG).convert("RGBA")
    layer = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(layer)
    draw.ellipse((-260, -180, 760, 620), fill=(22, 76, 135, 160))
    draw.ellipse((520, 1180, 1420, 2140), fill=(11, 88, 116, 130))
    return Image.alpha_composite(base, layer.filter(ImageFilter.GaussianBlur(80))).convert("RGBA")


def fit_image(path: Path) -> Image.Image | None:
    try:
        return ImageOps.contain(Image.open(path).convert("RGB"), (920, 820), method=Image.Resampling.LANCZOS)
    except Exception as exc:
        log(f"Skip image {path}: {exc}")
        return None


def draw_frame(image_path: Path | None, title: str, seg: dict[str, Any], output: Path, index: int, total: int) -> None:
    canvas = background()
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(54, True)
    subtitle_font = load_font(48, True)
    small_font = load_font(30)

    y = 66
    for line in wrap_text(title, 15)[:2]:
        box = draw.textbbox((0, 0), line, font=title_font)
        draw.text(((SIZE[0] - (box[2] - box[0])) // 2, y), line, font=title_font, fill=(255, 255, 255))
        y += 68
    draw.rounded_rectangle((70, 190, 1010, 198), radius=4, fill=ACCENT)

    stage = (70, 260, 1010, 1110)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    shadow_draw = ImageDraw.Draw(shadow)
    shadow_draw.rounded_rectangle((88, 282, 1028, 1132), radius=42, fill=(0, 0, 0, 100))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(22)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=42, fill=(255, 255, 255, 238))
    if image_path:
        image = fit_image(image_path)
        if image:
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    draw.rounded_rectangle((70, 1190, 1010, 1660), radius=38, fill=(0, 0, 0, 185))
    label = "主持人" if seg["speaker"] == "ZH_A" else "研究员"
    label_color = (37, 99, 235) if seg["speaker"] == "ZH_A" else (20, 130, 100)
    draw.rounded_rectangle((116, 1234, 248, 1282), radius=24, fill=label_color)
    draw.text((140, 1238), label, font=small_font, fill=(255, 255, 255))

    yy = 1318
    for line in wrap_text(str(seg["text"]), 18)[:4]:
        draw.text((120, yy), line, font=subtitle_font, fill=(255, 255, 255))
        yy += 66

    draw.text((70, 1728), f"{index + 1}/{total}", font=small_font, fill=(200, 215, 235))
    progress = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress, 1752), radius=6, fill=ACCENT)
    box = draw.textbbox((0, 0), WATERMARK, font=small_font)
    draw.text(((SIZE[0] - (box[2] - box[0])) // 2, 1828), WATERMARK, font=small_font, fill=(205, 220, 238))
    canvas.convert("RGB").save(output, quality=93)


def frame_duration(timeline: list[dict[str, Any]], index: int) -> float:
    if index + 1 < len(timeline):
        return max(0.5, float(timeline[index + 1]["start"]) - float(timeline[index]["start"]))
    return max(0.5, float(timeline[index]["end"]) - float(timeline[index]["start"]) + 0.36)


def make_video(item_dir: Path, timeline: list[dict[str, Any]]) -> None:
    images = report_images(item_dir)
    title = report_title(item_dir)
    with tempfile.TemporaryDirectory(prefix="kc_frames_") as temp_dir:
        tmp = Path(temp_dir)
        concat = tmp / "concat.txt"
        concat_lines: list[str] = []
        for index, seg in enumerate(timeline):
            frame = tmp / f"frame_{index:04d}.png"
            image_path = images[index % len(images)] if images else None
            draw_frame(image_path, title, seg, frame, index, len(timeline))
            concat_lines.append(f"file '{frame.as_posix()}'\n")
            concat_lines.append(f"duration {frame_duration(timeline, index):.3f}\n")
        concat_lines.append(concat_lines[-2])
        concat.write_text("".join(concat_lines), encoding="utf-8")
        silent = tmp / "silent.mp4"
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-vsync", "vfr", "-pix_fmt", "yuv420p", str(silent)], timeout=1200)
        run(["ffmpeg", "-y", "-i", str(silent), "-i", str(item_dir / "podcast_zh.wav"), "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-shortest", str(item_dir / "podcast_zh_explainer.mp4")], timeout=1200)


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--prompt-template", default="prompts/podcast_zh_only_prompt.md")
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--prompt-chars", type=int, default=26000)
    parser.add_argument("--eleven-base-url", default=os.getenv("ELEVEN_BASE_URL", "https://api.elevenlabs.io"))
    parser.add_argument("--eleven-model", default="eleven_multilingual_v2")
    parser.add_argument("--output-format", default="mp3_44100_128")
    parser.add_argument("--voice-a-id", default="auto")
    parser.add_argument("--voice-b-id", default="auto")
    parser.add_argument("--stability", type=float, default=0.45)
    parser.add_argument("--similarity-boost", type=float, default=0.78)
    parser.add_argument("--style", type=float, default=0.18)
    args = parser.parse_args()

    output_dir = Path(args.output_dir)
    item_dir = find_item(output_dir)
    source_text = trim((item_dir / "source_mineru.md").read_text(encoding="utf-8", errors="ignore"), args.prompt_chars)
    prompt = Path(args.prompt_template).read_text(encoding="utf-8").format(podcast_minutes=args.podcast_minutes, source_text=source_text)
    (item_dir / "prompt_for_podcast_zh.md").write_text(prompt, encoding="utf-8")
    script = deepseek(prompt, args)
    (item_dir / "podcast_zh_script.txt").write_text(script, encoding="utf-8")
    rows = parse_script(script)
    if not rows:
        raise RuntimeError("DeepSeek returned no ZH_A/ZH_B rows")

    timeline = make_audio(rows, item_dir, args)
    (item_dir / "podcast_zh_timeline.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")
    write_srt(timeline, item_dir / "podcast_zh_subtitles.srt")
    make_video(item_dir, timeline)

    status_path = item_dir / "status.json"
    status: dict[str, Any] = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            status = {}
    status.update({
        "podcast_zh_script": "podcast_zh_script.txt",
        "podcast_zh_audio": "podcast_zh.wav",
        "podcast_zh_subtitles": "podcast_zh_subtitles.srt",
        "podcast_zh_video": "podcast_zh_explainer.mp4",
        "podcast_tts_engine_actual": "elevenlabs",
        "subtitle_source": "same text as TTS, frame durations from measured audio",
        "podcast_video_watermark": WATERMARK,
    })
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"Generated ElevenLabs podcast/video in {item_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
