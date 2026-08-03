#!/usr/bin/env python3
"""Generate one Chinese two-male-voice podcast and animated explainer video.

The test workflow supports two local TTS engines:
- chattts: preferred local conversational TTS, more natural and role-distinct.
- piper: lightweight fallback, but Chinese voice choice may sound less male.

Video rendering supports:
- remotion: preferred real Remotion React animation renderer.
- pillow: deterministic Python/FFmpeg fallback.
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

VIDEO_SIZE = (1080, 1920)
VIDEO_BG = (9, 31, 64)
VIDEO_ACCENT = (255, 214, 102)
WATERMARK = "Portal Suite"
FPS = 30


def log(message: str) -> None:
    print(message, flush=True)


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={response.text[:1000]}")
    return data


def trim_source_text(source_text: str, max_chars: int) -> str:
    source_text = re.sub(r"\n{3,}", "\n\n", source_text or "").strip()
    if len(source_text) <= max_chars:
        return source_text
    head_len = int(max_chars * 0.72)
    tail_len = int(max_chars * 0.22)
    return source_text[:head_len] + "\n\n[中间内容因长度限制已省略]\n\n" + source_text[-tail_len:]


def call_deepseek(prompt: str, args: argparse.Namespace, label: str, temperature: float = 0.72) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    response = requests.post(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": args.model,
            "thinking": {"type": "disabled"},
            "temperature": temperature,
            "messages": [
                {"role": "system", "content": "你是中文财经播客制作人，输出可直接朗读的男声双人对话脚本。"},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=240,
    )
    data = parse_json_response(response, f"DeepSeek generate {label}")
    return data["choices"][0]["message"]["content"].strip() + "\n"


def build_prompt(template_path: Path, source_text: str, args: argparse.Namespace) -> str:
    return template_path.read_text(encoding="utf-8").format(
        podcast_minutes=args.podcast_minutes,
        source_text=trim_source_text(source_text, args.prompt_chars),
    )


def parse_zh_script(script: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    pattern = re.compile(r"^(ZH_A|ZH_B)\s*[:：]\s*(.+)$", re.I)
    for raw in script.splitlines():
        line = raw.strip().lstrip("-• ").strip()
        match = pattern.match(line)
        if match:
            text = match.group(2).strip()
            if text:
                rows.append((match.group(1).upper(), text))
    return rows


def wav_duration(path: Path) -> float:
    with wave.open(str(path), "rb") as src:
        return src.getnframes() / float(src.getframerate())


def wav_rate(path: Path) -> int:
    with wave.open(str(path), "rb") as src:
        return int(src.getframerate())


def run_cmd(cmd: list[str], timeout: int = 600, cwd: Path | None = None) -> None:
    log("$ " + " ".join(cmd))
    result = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, timeout=timeout, cwd=str(cwd) if cwd else None)
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="ignore")[-3000:])


def render_piper_tts_segment(text: str, model_path: Path, output: Path, args: argparse.Namespace) -> None:
    piper_bin = shutil.which(args.piper_binary)
    if not piper_bin:
        raise RuntimeError("piper CLI not found. Install piper-tts first.")
    if not model_path.exists():
        raise RuntimeError(f"Piper model missing: {model_path}")
    result = subprocess.run(
        [piper_bin, "--model", str(model_path), "--output_file", str(output)],
        input=text.encode("utf-8"),
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        timeout=180,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.decode("utf-8", errors="ignore")[-1600:])


def stylize_voice(input_wav: Path, output_wav: Path, speaker: str, stronger_male: bool = False) -> None:
    rate = wav_rate(input_wav)
    if stronger_male:
        ratio = 0.84 if speaker == "ZH_A" else 0.89
        tempo = 1.09 if speaker == "ZH_A" else 1.06
    else:
        ratio = 0.88 if speaker == "ZH_A" else 0.94
        tempo = 1.07 if speaker == "ZH_A" else 1.04
    bass = 4.5 if speaker == "ZH_A" else 2.5
    af = f"asetrate={int(rate * ratio)},aresample={rate},atempo={tempo},equalizer=f=140:t=q:w=1:g={bass},volume=0.97"
    run_cmd(["ffmpeg", "-y", "-i", str(input_wav), "-af", af, str(output_wav)], timeout=160)


def combine_wavs(segments: list[Path], output_path: Path, silence_ms: int = 360) -> None:
    if not segments:
        raise RuntimeError("No audio segments")
    with wave.open(str(segments[0]), "rb") as first:
        params = first.getparams()
    silence_frames = int(params.framerate * silence_ms / 1000)
    silence = b"\x00" * silence_frames * params.nchannels * params.sampwidth
    with wave.open(str(output_path), "wb") as out:
        out.setparams(params)
        for segment in segments:
            with wave.open(str(segment), "rb") as src:
                out.writeframes(src.readframes(src.getnframes()))
            out.writeframes(silence)


def render_audio_piper(rows: list[tuple[str, str]], item_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    model_a = Path(args.piper_zh_a_model)
    model_b = Path(args.piper_zh_b_model)
    timeline: list[dict[str, Any]] = []
    final_segments: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="zh_podcast_piper_") as tmp:
        tmp_dir = Path(tmp)
        cursor = 0.0
        for idx, (speaker, text) in enumerate(rows[:140], 1):
            raw = tmp_dir / f"raw_{idx:03d}.wav"
            styled = tmp_dir / f"styled_{idx:03d}.wav"
            render_piper_tts_segment(text, model_a if speaker == "ZH_A" else model_b, raw, args)
            stylize_voice(raw, styled, speaker, stronger_male=True)
            dur = wav_duration(styled)
            timeline.append({"speaker": speaker, "text": text, "start": round(cursor, 3), "end": round(cursor + dur, 3), "tts_engine": "piper"})
            cursor += dur + 0.36
            final_segments.append(styled)
        combine_wavs(final_segments, item_dir / "podcast_zh.wav")
    return timeline


def render_audio_chattts(rows: list[tuple[str, str]], item_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    """Render local ChatTTS audio.

    ChatTTS provides more conversational local speech than Piper. It does not
    expose a hard gender lock, so we use two deterministic speaker embeddings
    and post-process both voices toward lower male timbre.
    """
    try:
        import ChatTTS  # type: ignore
        import soundfile as sf  # type: ignore
    except Exception as exc:
        raise RuntimeError(f"ChatTTS dependencies are missing: {exc}") from exc

    chat = ChatTTS.Chat()
    log("Loading ChatTTS local model from Hugging Face cache/source...")
    try:
        chat.load(compile=False, source="huggingface")
    except TypeError:
        chat.load(compile=False)

    # Deterministic-ish different speakers when the library supports sampling.
    try:
        spk_a = chat.sample_random_speaker()
        spk_b = chat.sample_random_speaker()
    except Exception:
        spk_a = None
        spk_b = None

    timeline: list[dict[str, Any]] = []
    final_segments: list[Path] = []
    with tempfile.TemporaryDirectory(prefix="zh_podcast_chattts_") as tmp:
        tmp_dir = Path(tmp)
        cursor = 0.0
        for idx, (speaker, text) in enumerate(rows[:120], 1):
            clean_text = re.sub(r"\s+", " ", text).strip()
            infer_kwargs: dict[str, Any] = {}
            try:
                spk = spk_a if speaker == "ZH_A" else spk_b
                if spk is not None:
                    infer_kwargs["params_infer_code"] = ChatTTS.Chat.InferCodeParams(spk_emb=spk, temperature=0.28, top_P=0.7, top_K=20)
                infer_kwargs["params_refine_text"] = ChatTTS.Chat.RefineTextParams(prompt="[oral_2][laugh_0][break_5]")
            except Exception:
                infer_kwargs = {}
            wavs = chat.infer([clean_text], **infer_kwargs)
            raw = tmp_dir / f"chattts_raw_{idx:03d}.wav"
            styled = tmp_dir / f"chattts_styled_{idx:03d}.wav"
            sf.write(raw, wavs[0], 24000)
            stylize_voice(raw, styled, speaker, stronger_male=True)
            dur = wav_duration(styled)
            timeline.append({"speaker": speaker, "text": clean_text, "start": round(cursor, 3), "end": round(cursor + dur, 3), "tts_engine": "chattts"})
            cursor += dur + 0.36
            final_segments.append(styled)
        combine_wavs(final_segments, item_dir / "podcast_zh.wav")
    return timeline


def render_audio(rows: list[tuple[str, str]], item_dir: Path, args: argparse.Namespace) -> tuple[list[dict[str, Any]], str]:
    engine = args.tts_engine.lower().strip()
    if engine == "chattts":
        try:
            return render_audio_chattts(rows, item_dir, args), "chattts"
        except Exception as exc:
            if not args.allow_tts_fallback:
                raise
            log(f"ChatTTS failed, falling back to Piper: {exc}")
    return render_audio_piper(rows, item_dir, args), "piper"


def generate_highlights(timeline: list[dict[str, Any]], args: argparse.Namespace) -> list[dict[str, Any]]:
    sample = [{"i": i, "text": seg.get("text", "")} for i, seg in enumerate(timeline[:90])]
    prompt = f"""
请为中文短视频字幕挑选高亮信息词。

要求：
1. 对每条字幕返回 0-3 个关键词。
2. 关键词必须是字幕原文中连续出现的短词，不要改写。
3. 优先高亮：行业、变量、数字、转折点、结论词。
4. 不要高亮“这个、我们、报告、所以”等泛词。
5. 只输出 JSON 数组，格式：[{{"i":0,"keywords":["关键词"]}}]

字幕：
{json.dumps(sample, ensure_ascii=False)}
""".strip()
    try:
        raw = call_deepseek(prompt, args, "subtitle highlight keywords", temperature=0.15)
        match = re.search(r"\[[\s\S]*\]", raw)
        data = json.loads(match.group(0) if match else raw)
        mapping = {int(x.get("i")): [str(k) for k in x.get("keywords", [])[:3]] for x in data if isinstance(x, dict)}
    except Exception as exc:
        log(f"DeepSeek highlight failed, using fallback keywords: {exc}")
        mapping = {}
    for i, seg in enumerate(timeline):
        text = str(seg.get("text", ""))
        keywords = mapping.get(i, [])
        if not keywords:
            keywords = re.findall(r"[A-Za-z0-9]{2,}|[\u4e00-\u9fff]{2,6}", text)[:2]
        seg["highlight_terms"] = [k for k in keywords if k and k in text][:3]
    return timeline


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


def wrap_cn(text: str, width: int) -> list[str]:
    text = re.sub(r"\s+", " ", text).strip()
    return [text[i:i + width] for i in range(0, len(text), width)] or [""]


def find_original_images(item_dir: Path) -> list[Path]:
    assets = item_dir / "assets"
    if not assets.exists():
        return []
    suffixes = {".png", ".jpg", ".jpeg", ".webp"}
    preferred = sorted([p for p in assets.glob("source_image_*") if p.suffix.lower() in suffixes])
    fallback = sorted([p for p in assets.glob("xhs_card_*.png") if p.suffix.lower() in suffixes])
    return preferred or fallback


def extract_title(item_dir: Path) -> str:
    for name in ["note.md", "wechat_article.md"]:
        path = item_dir / name
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = re.sub(r"^[#>*\-\s]+", "", raw).strip()
            if line and not line.startswith("封面"):
                return line[:34]
    return "研报讲解"


def draw_gradient_bg() -> Image.Image:
    canvas = Image.new("RGB", VIDEO_SIZE, VIDEO_BG)
    overlay = Image.new("RGBA", VIDEO_SIZE, (0, 0, 0, 0))
    draw = ImageDraw.Draw(overlay)
    draw.ellipse((-260, -180, 760, 620), fill=(22, 76, 135, 160))
    draw.ellipse((520, 1180, 1420, 2140), fill=(11, 88, 116, 130))
    overlay = overlay.filter(ImageFilter.GaussianBlur(80))
    return Image.alpha_composite(canvas.convert("RGBA"), overlay).convert("RGB")


def fit_image_for_stage(path: Path) -> Image.Image | None:
    try:
        img = Image.open(path).convert("RGB")
        return ImageOps.contain(img, (920, 820), method=Image.Resampling.LANCZOS)
    except Exception as exc:
        log(f"Skip video image {path}: {exc}")
        return None


def draw_highlighted_lines(draw: ImageDraw.ImageDraw, text: str, terms: list[str], font: ImageFont.ImageFont, y: int) -> int:
    x0 = 120
    for line in wrap_cn(text, 18)[:4]:
        x = x0
        chunks: list[tuple[str, bool]] = [(line, False)]
        for term in sorted(terms, key=len, reverse=True):
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
        for chunk, marked in chunks:
            fill = VIDEO_ACCENT if marked else (255, 255, 255)
            draw.text((x, y), chunk, font=font, fill=fill)
            bbox = draw.textbbox((0, 0), chunk, font=font)
            x += bbox[2] - bbox[0]
        y += 66
    return y


def draw_speaker_badge(draw: ImageDraw.ImageDraw, speaker: str, x: int, y: int) -> None:
    font = load_font(30, bold=True)
    label = "主持人" if speaker == "ZH_A" else "研究员"
    color = (37, 99, 235) if speaker == "ZH_A" else (20, 130, 100)
    draw.rounded_rectangle((x, y, x + 132, y + 48), radius=24, fill=color)
    bbox = draw.textbbox((0, 0), label, font=font)
    draw.text((x + (132 - (bbox[2] - bbox[0])) // 2, y + 5), label, font=font, fill=(255, 255, 255))


def draw_frame(image_path: Path | None, title: str, speaker: str, subtitle: str, highlights: list[str], out_path: Path, index: int, total: int) -> None:
    canvas = draw_gradient_bg().convert("RGBA")
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(54, bold=True)
    subtitle_font = load_font(48, bold=True)
    small_font = load_font(28)
    watermark_font = load_font(30)

    y = 66
    for line in wrap_cn(title, 15)[:2]:
        bbox = draw.textbbox((0, 0), line, font=title_font)
        draw.text(((VIDEO_SIZE[0] - (bbox[2] - bbox[0])) // 2, y), line, font=title_font, fill=(255, 255, 255))
        y += 68
    draw.rounded_rectangle((70, 190, 1010, 198), radius=4, fill=VIDEO_ACCENT)

    stage = (70, 260, 1010, 1110)
    shadow = Image.new("RGBA", VIDEO_SIZE, (0, 0, 0, 0))
    sd = ImageDraw.Draw(shadow)
    sd.rounded_rectangle((stage[0] + 18, stage[1] + 22, stage[2] + 18, stage[3] + 22), radius=42, fill=(0, 0, 0, 100))
    shadow = shadow.filter(ImageFilter.GaussianBlur(22))
    canvas = Image.alpha_composite(canvas, shadow)
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=42, fill=(255, 255, 255, 238))
    if image_path:
        img = fit_image_for_stage(image_path)
        if img:
            canvas.paste(img.convert("RGBA"), ((VIDEO_SIZE[0] - img.width) // 2, stage[1] + (stage[3] - stage[1] - img.height) // 2), img.convert("RGBA"))
    else:
        draw.text((140, 630), "报告图表讲解", font=title_font, fill=(35, 48, 68))

    box = (70, 1190, 1010, 1660)
    draw.rounded_rectangle(box, radius=38, fill=(0, 0, 0, 185))
    draw_speaker_badge(draw, speaker, 116, 1234)
    draw_highlighted_lines(draw, subtitle, highlights, subtitle_font, 1318)

    draw.text((70, 1728), f"{index + 1}/{max(total, 1)}", font=small_font, fill=(200, 215, 235))
    progress_w = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress_w, 1752), radius=6, fill=VIDEO_ACCENT)
    bbox = draw.textbbox((0, 0), WATERMARK, font=watermark_font)
    draw.text(((VIDEO_SIZE[0] - (bbox[2] - bbox[0])) // 2, 1828), WATERMARK, font=watermark_font, fill=(205, 220, 238))

    out_path.parent.mkdir(parents=True, exist_ok=True)
    canvas.convert("RGB").save(out_path, quality=93)


def render_video_pillow(audio_path: Path, timeline: list[dict[str, Any]], images: list[Path], output_path: Path, title: str) -> None:
    if not timeline:
        raise RuntimeError("No timeline for video")
    with tempfile.TemporaryDirectory(prefix="portal_video_frames_") as tmp:
        tmp_dir = Path(tmp)
        concat = tmp_dir / "concat.txt"
        lines: list[str] = []
        for idx, seg in enumerate(timeline):
            frame = tmp_dir / f"frame_{idx:04d}.png"
            image = images[idx % len(images)] if images else None
            draw_frame(image, title, str(seg["speaker"]), str(seg["text"]), list(seg.get("highlight_terms", [])), frame, idx, len(timeline))
            duration = max(0.8, min(3.0, float(seg["end"]) - float(seg["start"]) + 0.36))
            lines.append(f"file '{frame.as_posix()}'\n")
            lines.append(f"duration {duration:.3f}\n")
        lines.append(lines[-2])
        concat.write_text("".join(lines), encoding="utf-8")
        silent = tmp_dir / "silent.mp4"
        run_cmd(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-vsync", "vfr", "-pix_fmt", "yuv420p", str(silent)], timeout=900)
        run_cmd(["ffmpeg", "-y", "-i", str(silent), "-i", str(audio_path), "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-shortest", str(output_path)], timeout=900)


def prepare_remotion_assets(item_dir: Path, timeline: list[dict[str, Any]], images: list[Path], title: str) -> Path:
    public_root = Path("remotion/public/generated") / re.sub(r"[^A-Za-z0-9_-]+", "-", item_dir.name)[:80]
    public_root.mkdir(parents=True, exist_ok=True)
    shutil.copy2(item_dir / "podcast_zh.wav", public_root / "podcast_zh.wav")
    image_entries: list[str] = []
    img_dir = public_root / "images"
    img_dir.mkdir(parents=True, exist_ok=True)
    for idx, img in enumerate(images[:16], 1):
        target = img_dir / f"image_{idx:02d}{img.suffix.lower()}"
        shutil.copy2(img, target)
        image_entries.append(target.relative_to(Path("remotion/public")).as_posix())
    duration_seconds = max(float(timeline[-1].get("end", 0)) + 1.0, 6.0)
    props = {
        "title": title,
        "watermark": WATERMARK,
        "audioSrc": (public_root / "podcast_zh.wav").relative_to(Path("remotion/public")).as_posix(),
        "images": image_entries,
        "timeline": timeline,
        "fps": FPS,
        "durationFrames": int(duration_seconds * FPS) + 30,
    }
    props_path = item_dir / "remotion_input_props.json"
    props_path.write_text(json.dumps(props, ensure_ascii=False, indent=2), encoding="utf-8")
    return props_path


def render_video_remotion(item_dir: Path, timeline: list[dict[str, Any]], images: list[Path], output_path: Path, title: str) -> None:
    props_path = prepare_remotion_assets(item_dir, timeline, images, title)
    run_cmd([
        "npx", "remotion", "render", "remotion/src/index.tsx", "PodcastExplainer", str(output_path),
        "--props", str(props_path),
        "--codec", "h264", "--pixel-format", "yuv420p", "--overwrite",
    ], timeout=1800)


def render_video(item_dir: Path, timeline: list[dict[str, Any]], images: list[Path], output_path: Path, title: str, args: argparse.Namespace) -> str:
    if args.video_engine.lower() == "remotion":
        try:
            render_video_remotion(item_dir, timeline, images, output_path, title)
            return "remotion"
        except Exception as exc:
            if not args.allow_video_fallback:
                raise
            log(f"Remotion render failed, falling back to Pillow/FFmpeg: {exc}")
    render_video_pillow(item_dir / "podcast_zh.wav", timeline, images, output_path, title)
    return "pillow_ffmpeg"


def find_single_item_dir(output_dir: Path) -> Path:
    candidates = [p for p in output_dir.iterdir() if p.is_dir() and (p / "source_mineru.md").exists()]
    if not candidates:
        raise RuntimeError(f"No generated report folder with source_mineru.md under {output_dir}")
    return sorted(candidates)[0]


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--prompt-template", default="prompts/podcast_zh_only_prompt.md")
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--prompt-chars", type=int, default=26000)
    parser.add_argument("--tts-engine", default="chattts", choices=["chattts", "piper"])
    parser.add_argument("--allow-tts-fallback", default="true")
    parser.add_argument("--piper-binary", default="piper")
    parser.add_argument("--piper-zh-a-model", default=".piper-voices/zh_CN-huayan-medium.onnx")
    parser.add_argument("--piper-zh-b-model", default=".piper-voices/zh_CN-huayan-medium.onnx")
    parser.add_argument("--video-engine", default="remotion", choices=["remotion", "pillow"])
    parser.add_argument("--allow-video-fallback", default="true")
    args = parser.parse_args()
    args.allow_tts_fallback = str(args.allow_tts_fallback).lower() in {"1", "true", "yes", "y", "on"}
    args.allow_video_fallback = str(args.allow_video_fallback).lower() in {"1", "true", "yes", "y", "on"}

    output_dir = Path(args.output_dir)
    item_dir = find_single_item_dir(output_dir)
    source_text = (item_dir / "source_mineru.md").read_text(encoding="utf-8", errors="ignore")
    prompt = build_prompt(Path(args.prompt_template), source_text, args)
    (item_dir / "prompt_for_podcast_zh.md").write_text(prompt, encoding="utf-8")
    script = call_deepseek(prompt, args, "Chinese two-male podcast")
    (item_dir / "podcast_zh_script.txt").write_text(script, encoding="utf-8")
    rows = parse_zh_script(script)
    if not rows:
        raise RuntimeError("DeepSeek returned no ZH_A/ZH_B podcast rows")
    timeline, actual_tts = render_audio(rows, item_dir, args)
    timeline = generate_highlights(timeline, args)
    (item_dir / "podcast_zh_timeline.json").write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")
    images = find_original_images(item_dir)
    title = extract_title(item_dir)
    actual_video = render_video(item_dir, timeline, images, item_dir / "podcast_zh_explainer.mp4", title, args)
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
        "podcast_zh_video": "podcast_zh_explainer.mp4",
        "podcast_video_watermark": WATERMARK,
        "podcast_tts_engine_requested": args.tts_engine,
        "podcast_tts_engine_actual": actual_tts,
        "podcast_video_engine_requested": args.video_engine,
        "podcast_video_engine_actual": actual_video,
        "subtitle_highlight": "DeepSeek keyword highlights with yellow rendering",
    })
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"Generated Chinese podcast audio/video in {item_dir}; tts={actual_tts}, video={actual_video}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
