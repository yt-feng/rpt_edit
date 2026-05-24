#!/usr/bin/env python3
"""Batch wrapper for bilingual ElevenLabs podcast/video test.

This wrapper reuses generate_test_podcast_video_eleven.py but:
- forces the second speaker to the requested male voice ID;
- processes up to N generated report folders instead of only the first one.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
from types import SimpleNamespace
from typing import Any

import generate_test_podcast_video_eleven as gen

SECOND_MALE_VOICE_ID = "bdt3B5N3GXM2nOc0SUW7"


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


def process_one(item_dir: Path, args: argparse.Namespace) -> dict[str, Any]:
    raw_source = (item_dir / "source_mineru.md").read_text(encoding="utf-8", errors="ignore")
    source_text = gen.trim(gen.sanitize_public_text(raw_source, "zh"), args.prompt_chars)
    status_update: dict[str, Any] = {
        "podcast_video_watermark": gen.WATERMARK,
        "podcast_tts_engine_actual": "elevenlabs",
        "subtitle_source": "same text as TTS; role tags normalized; rows split by punctuation before TTS; long visual subtitles are paged",
        "highlight_source": "DeepSeek title and subtitle keyword analysis",
        "sensitive_filter": "local xhs_notes-style replacements before TTS and rendering",
        "batch_wrapper": "generate_test_podcast_video_eleven_batch.py",
    }
    for lang in ["zh", "en"]:
        log(f"Generating {lang.upper()} podcast audio/video for {item_dir.name}")
        status_update.update(gen.generate_language(item_dir, lang, source_text, args))
    status_path = item_dir / "status.json"
    status = load_status(status_path)
    status.update(status_update)
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    return status_update


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--max-items", type=int, default=5)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--podcast-minutes", type=int, default=5)
    parser.add_argument("--prompt-chars", type=int, default=26000)
    parser.add_argument("--eleven-base-url", default=os.getenv("ELEVEN_BASE_URL", "https://api.elevenlabs.io"))
    parser.add_argument("--eleven-model", default="eleven_multilingual_v2")
    parser.add_argument("--output-format", default="mp3_44100_128")
    parser.add_argument("--stability", type=float, default=0.45)
    parser.add_argument("--similarity-boost", type=float, default=0.78)
    parser.add_argument("--style", type=float, default=0.18)
    args = parser.parse_args()

    # Force the B-speaker voice in both Chinese and English to the requested male voice.
    gen.LANGS["zh"]["voice_b"] = SECOND_MALE_VOICE_ID
    gen.LANGS["en"]["voice_b"] = SECOND_MALE_VOICE_ID
    gen.LANGS["zh"]["analyst_label"] = "嘉宾"
    gen.LANGS["en"]["analyst_label"] = "Guest"

    output_dir = Path(args.output_dir)
    item_dirs = find_item_dirs(output_dir, args.max_items)
    summary: dict[str, Any] = {
        "max_items": args.max_items,
        "processed_count": 0,
        "second_speaker_voice_id": SECOND_MALE_VOICE_ID,
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
