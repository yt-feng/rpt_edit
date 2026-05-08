#!/usr/bin/env python3
"""Post-process generated report folders.

Adds:
1. WeChat markdown image refs using original MinerU/source images.
2. Bilingual Chinese+English podcast script.
3. Optional local open-source Piper TTS audio.
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
import time
import wave
from pathlib import Path
from typing import Any

import requests


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
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        return f"未检测到 DEEPSEEK_API_KEY。请复制 prompt 手动生成：{label}\n"
    url = args.deepseek_base_url.rstrip("/") + "/chat/completions"
    payload = {
        "model": args.model,
        "temperature": 0.72,
        "messages": [
            {"role": "system", "content": "你是专业财经内容制作人，输出必须可直接发布或朗读。"},
            {"role": "user", "content": prompt},
        ],
    }
    response = requests.post(
        url,
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json=payload,
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
    return []


def embed_original_images(article: str, image_paths: list[str], max_images: int = 3) -> str:
    clean = [p for p in image_paths if p.lower().endswith((".png", ".jpg", ".jpeg", ".webp"))]
    if not clean:
        return article
    # Remove previously inserted generated-card refs, if any.
    article = re.sub(r"\n?!\[研报图表 \d+\]\(assets/xhs_card_\d+\.png\)\n?", "\n", article)
    article = re.sub(r"\n?!\[研报原图 \d+\]\(assets/[^\)]+\)\n?", "\n", article)
    images = [f"\n![研报原图 {i}]({path})\n" for i, path in enumerate(clean[:max_images], 1)]
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


def parse_podcast_lines(script: str) -> list[tuple[str, str]]:
    lines: list[tuple[str, str]] = []
    for raw in script.splitlines():
        line = raw.strip().lstrip("-• ").strip()
        match = re.match(r"^(ZH|EN)\s*[:：]\s*(.+)$", line, flags=re.IGNORECASE)
        if match:
            lang = match.group(1).upper()
            text = match.group(2).strip()
            if text:
                lines.append((lang, text))
    return lines


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
                if src.getparams()[:3] != params[:3]:
                    raise RuntimeError(f"Segment wav parameters differ: {path}")
                out.writeframes(src.readframes(src.getnframes()))
                out.writeframes(silence)


def render_podcast_audio(script: str, output_path: Path, args: argparse.Namespace) -> None:
    piper_bin = shutil.which(args.piper_binary)
    if not piper_bin:
        raise RuntimeError("piper CLI not found. Make sure workflow installed piper-tts.")
    zh_model = Path(args.piper_zh_model)
    en_model = Path(args.piper_en_model)
    if not zh_model.exists():
        raise RuntimeError(f"Chinese Piper model not found: {zh_model}")
    if not en_model.exists():
        raise RuntimeError(f"English Piper model not found: {en_model}")
    lines = parse_podcast_lines(script)
    if not lines:
        raise RuntimeError("Podcast script has no ZH:/EN: lines, cannot synthesize audio.")
    with tempfile.TemporaryDirectory(prefix="podcast_segments_") as tmp:
        tmp_dir = Path(tmp)
        segment_paths: list[Path] = []
        for idx, (lang, text) in enumerate(lines[:120], 1):
            model = zh_model if lang == "ZH" else en_model
            segment = tmp_dir / f"segment_{idx:03d}.wav"
            result = subprocess.run(
                [piper_bin, "--model", str(model), "--output_file", str(segment)],
                input=text.encode("utf-8"),
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE,
                timeout=120,
            )
            if result.returncode != 0:
                raise RuntimeError(f"Piper failed on segment {idx}: {result.stderr.decode('utf-8', errors='ignore')[:500]}")
            segment_paths.append(segment)
        combine_wavs(segment_paths, output_path)


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
        article_path.write_text(embed_original_images(article, image_paths, max_images=args.max_wechat_images), encoding="utf-8")
        status["wechat_images"] = image_paths[: args.max_wechat_images]

    source_path = item_dir / "source_mineru.md"
    if not source_path.exists():
        status["podcast_error"] = "source_mineru.md not found"
        status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
        return status

    source_text = source_path.read_text(encoding="utf-8", errors="ignore")
    prompt = build_podcast_prompt(Path(args.podcast_prompt_template), source_text, args)
    (item_dir / "prompt_for_podcast.md").write_text(prompt, encoding="utf-8")
    try:
        script = call_deepseek(prompt, args, "bilingual podcast script")
    except Exception as exc:
        script = f"DeepSeek 生成 podcast 脚本失败：{exc}\n"
        status["podcast_error"] = str(exc)
    (item_dir / "podcast_zh_en_script.txt").write_text(script, encoding="utf-8")
    status["podcast_script"] = "podcast_zh_en_script.txt"

    if as_bool(args.generate_audio):
        try:
            render_podcast_audio(script, item_dir / "podcast_zh_en.wav", args)
            status["podcast_audio"] = "podcast_zh_en.wav"
        except Exception as exc:
            log(f"Audio generation failed for {item_dir.name}: {exc}")
            status["podcast_audio_error"] = str(exc)

    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return status


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", default="xhs_notes")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--podcast-prompt-template", default="prompts/podcast_zh_en_prompt.md")
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--podcast-prompt-chars", type=int, default=26000)
    parser.add_argument("--generate-audio", default="true")
    parser.add_argument("--max-wechat-images", type=int, default=3)
    parser.add_argument("--piper-binary", default="piper")
    parser.add_argument("--piper-zh-model", default=".piper-voices/zh_CN-huayan-medium.onnx")
    parser.add_argument("--piper-en-model", default=".piper-voices/en_US-lessac-medium.onnx")
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
