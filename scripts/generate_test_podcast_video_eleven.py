#!/usr/bin/env python3
"""Generate Chinese and English ElevenLabs podcast audio + vertical videos.

Fixes:
- ZH_A / EN_A use the fixed male voice; ZH_B / EN_B use the fixed female voice.
- Embedded speaker tags such as `ZH_A:` inside a line are split before parsing.
- The saved script is rewritten from parsed rows, so raw LLM tags cannot leak into subtitles.
- Long turns are split by sentence / comma before TTS, so subtitles do not cut off mid-thought.
- Title and subtitle keywords are highlighted with DeepSeek-selected keywords.
"""
from __future__ import annotations

import argparse
import json
import os
import re
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

LANGS: dict[str, dict[str, Any]] = {
    "zh": {
        "prompt": "prompts/podcast_zh_only_prompt.md",
        "prefixes": ("ZH_A", "ZH_B"),
        "language_code": "zh",
        "host_label": "主持人",
        "analyst_label": "研究员",
        "audio": "podcast_zh.wav",
        "script": "podcast_zh_script.txt",
        "timeline": "podcast_zh_timeline.json",
        "visual_timeline": "podcast_zh_visual_timeline.json",
        "srt": "podcast_zh_subtitles.srt",
        "video": "podcast_zh_explainer.mp4",
        "prompt_out": "prompt_for_podcast_zh.md",
        "voice_a": "UFDAUkGzdLAEJlINT3Fx",
        "voice_b": "bhJUNIXWQQ94l8eI2VUf",
        "title_fallback": "研报讲解",
        "line_width": 18,
        "title_width": 15,
        "max_tts_chars": 52,
        "max_subtitle_lines": 4,
        "show_name": "KC桌面",
        "branded_opening": "欢迎来到KC桌面。今天我们用一份最新研报，拆一个值得继续跟踪的问题。",
    },
    "en": {
        "prompt": "prompts/podcast_en_only_prompt.md",
        "prefixes": ("EN_A", "EN_B"),
        "language_code": "en",
        "host_label": "Host",
        "analyst_label": "Analyst",
        "audio": "podcast_en.wav",
        "script": "podcast_en_script.txt",
        "timeline": "podcast_en_timeline.json",
        "visual_timeline": "podcast_en_visual_timeline.json",
        "srt": "podcast_en_subtitles.srt",
        "video": "podcast_en_explainer.mp4",
        "prompt_out": "prompt_for_podcast_en.md",
        "voice_a": "XZEfcFyBnzsNJrdvkWdI",
        "voice_b": "ISCzWD5dlKGqdgkYePJf",
        "title_fallback": "Research Briefing",
        "line_width": 34,
        "title_width": 26,
        "max_tts_chars": 160,
        "max_subtitle_lines": 4,
        "show_name": "KC桌面",
        "branded_opening": "Welcome to KC桌面. Today we are unpacking one fresh research report and the question it raises.",
    },
}

PROTECTED_TERMS = {"投研": "__PROTECT_TOUYAN__", "投行": "__PROTECT_TOUHANG__", "投资银行": "__PROTECT_IBANK__"}
LOCAL_REPLACEMENTS: list[tuple[str, str]] = [
    (r"不构成任何投资建议", "仅为个人阅读分享"), (r"投资建议", "研究交流"), (r"投资机会", "研究线索"),
    (r"投资逻辑", "研究逻辑"), (r"投资价值", "研究价值"), (r"投资者", "读者"),
    (r"买入评级", "报告评级"), (r"卖出评级", "报告评级"), (r"强烈买入", "报告观点较积极"),
    (r"推荐买入", "报告观点偏积极"), (r"买入", "配置观点"), (r"卖出", "谨慎观点"),
    (r"抄底", "底部观察"), (r"上车", "继续跟踪"), (r"必涨", "存在上行假设"),
    (r"稳赚", "确定性仍需验证"), (r"保本", "风险仍需评估"), (r"翻倍", "弹性较高"),
    (r"内幕", "资料"), (r"内部资料", "资料"), (r"地缘政治", "地缘环境"), (r"政治", "政策环境"),
    (r"政府", "政策端"), (r"监管", "规则环境"), (r"关注点赞", "欢迎交流"), (r"点赞", "收藏"),
    (r"评论区留言", "可以一起讨论"), (r"必看", "值得看看"), (r"必读", "值得读"),
    (r"爆款", "有传播力的"), (r"震惊", "值得注意"), (r"最强", "较强"), (r"最全", "较完整"),
]
EN_REPLACEMENTS: list[tuple[str, str]] = [
    (r"\binvestment\s+advice\b", "research discussion"), (r"\bstrong\s+buy\b", "constructive view"),
    (r"\bbuy\b", "research view"), (r"\bsell\b", "cautious view"), (r"\bguaranteed\b", "not assured"),
    (r"\brisk[- ]free\b", "lower-risk"), (r"\binsider\b", "source material"),
    (r"\bgeopolitical\b", "geo-policy"), (r"\bpolitics\b", "policy environment"),
    (r"\bpolitical\b", "policy-related"), (r"\bgovernment\b", "policy side"),
]
BRAND_REPLACEMENTS: list[tuple[str, str]] = [
    (r"Goldman\s+Sachs|高盛", "GS"), (r"J\.?\s*P\.?\s*Morgan|JPMorgan|摩根大通", "JPM"),
    (r"Morgan\s+Stanley|摩根士丹利|大摩", "MS"),
    (r"Bank\s+of\s+America|BofA\s+Securities|Merrill\s+Lynch|美银|美林", "BofA"),
    (r"Citigroup|Citi\s+Research|花旗", "Citi"), (r"UBS|瑞银", "UBS"),
    (r"Deutsche\s+Bank|德银|德意志银行", "DB"),
]


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


def deepseek(prompt: str, args: argparse.Namespace, temperature: float = 0.55) -> str:
    key = os.getenv("DEEPSEEK_API_KEY")
    if not key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    data = post_json(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        {"Content-Type": "application/json", "Authorization": f"Bearer {key}"},
        {"model": args.model, "thinking": {"type": "disabled"}, "temperature": temperature, "messages": [
            {"role": "system", "content": "You are a careful podcast and short-video producer. Return exactly the requested format."},
            {"role": "user", "content": prompt},
        ]},
    )
    return data["choices"][0]["message"]["content"].strip() + "\n"


def sanitize_public_text(text: str, lang: str = "zh") -> str:
    out = str(text or "")
    for pattern, repl in BRAND_REPLACEMENTS:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
    for key, token in PROTECTED_TERMS.items():
        out = out.replace(key, token)
    for pattern, repl in LOCAL_REPLACEMENTS:
        out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
    out = re.sub(r"投资", "研究", out)
    for key, token in PROTECTED_TERMS.items():
        out = out.replace(token, key)
    if lang == "en":
        for pattern, repl in EN_REPLACEMENTS:
            out = re.sub(pattern, repl, out, flags=re.IGNORECASE)
    return re.sub(r"\s+", " ", out).strip()


def strip_script_artifacts(text: str, lang: str) -> str:
    prefixes = LANGS[lang]["prefixes"]
    out = str(text or "")
    out = re.sub(r"```[a-zA-Z]*", "", out).replace("```", "")
    out = re.sub(r"^\s*[-*•]\s*", "", out)
    out = re.sub(r"^\s*\d+[\.)]\s*", "", out)
    out = re.sub(rf"\b(?:{'|'.join(prefixes)})\s*[:：]\s*", "", out, flags=re.IGNORECASE)
    out = re.sub(r"\b(?:主持人|研究员|Host|Analyst)\s*[:：]\s*", "", out, flags=re.IGNORECASE)
    return out.strip()


def find_item(output_dir: Path) -> Path:
    items = [p for p in output_dir.iterdir() if p.is_dir() and (p / "source_mineru.md").exists()]
    if not items:
        raise RuntimeError(f"No generated report folder with source_mineru.md under {output_dir}")
    return sorted(items)[0]


def trim(text: str, limit: int) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text or "").strip()
    if len(text) <= limit:
        return text
    return text[: int(limit * 0.72)] + "\n\n[Middle content omitted]\n\n" + text[-int(limit * 0.22):]


def normalize_text(text: str, lang: str) -> str:
    text = strip_script_artifacts(text, lang)
    text = re.sub(r"\s+", " ", text or "").strip()
    text = re.sub(r"[\[\]（）(){}]", "", text).replace("：", "，")
    return sanitize_public_text(text, lang)


def fragment_text(text: str, lang: str) -> list[str]:
    if lang == "zh":
        pattern = r"[^。！？；，、,.!?;]+[。！？；，、,.!?;]*"
    else:
        pattern = r"[^.!?;,]+[.!?;,]*"
    return [m.group(0).strip() for m in re.finditer(pattern, text) if m.group(0).strip()]


def split_long_text(text: str, lang: str, max_chars: int) -> list[str]:
    text = normalize_text(text, lang)
    if not text:
        return []
    if len(text) <= max_chars:
        return [text]
    fragments = fragment_text(text, lang) or [text]
    chunks: list[str] = []
    buf = ""
    joiner = "" if lang == "zh" else " "
    for frag in fragments:
        candidate = (buf + joiner + frag).strip() if buf else frag
        if len(candidate) <= max_chars:
            buf = candidate
            continue
        if buf:
            chunks.append(buf)
        if len(frag) <= max_chars:
            buf = frag
        else:
            for i in range(0, len(frag), max_chars):
                part = frag[i:i + max_chars].strip()
                if part:
                    chunks.append(part)
            buf = ""
    if buf:
        chunks.append(buf)
    return chunks or [text]


def normalize_script_lines(script: str, prefixes: tuple[str, str]) -> list[str]:
    out = str(script or "")
    out = re.sub(rf"\s*((?:{'|'.join(prefixes)})\s*[:：])", r"\n\1", out, flags=re.IGNORECASE)
    return [line.strip() for line in out.splitlines() if line.strip()]


def balance_speakers(rows: list[tuple[str, str]], prefixes: tuple[str, str]) -> list[tuple[str, str]]:
    if not rows:
        return rows
    a, b = prefixes
    speakers = [spk for spk, _ in rows]
    if a not in speakers or b not in speakers:
        return [(a if i % 2 == 0 else b, text) for i, (_spk, text) in enumerate(rows)]
    balanced: list[tuple[str, str]] = []
    run_spk = ""
    run_len = 0
    for spk, text in rows:
        if spk == run_spk:
            run_len += 1
        else:
            run_spk = spk
            run_len = 1
        if run_len > 2:
            spk = b if spk == a else a
            run_spk = spk
            run_len = 1
        balanced.append((spk, text))
    return balanced


def ensure_branded_opening(rows: list[tuple[str, str]], lang: str) -> list[tuple[str, str]]:
    cfg = LANGS[lang]
    if not rows:
        return rows
    first = " ".join(text for _spk, text in rows[:2])
    if str(cfg["show_name"]).lower() in first.lower():
        return rows
    return [(str(cfg["prefixes"][0]), str(cfg["branded_opening"]))] + rows


def parse_script(script: str, prefixes: tuple[str, str], lang: str) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    pattern = re.compile(rf"^({'|'.join(prefixes)})\s*[:：]\s*(.+)$", re.I)
    for raw in normalize_script_lines(script, prefixes):
        match = pattern.match(raw.strip().lstrip("-• ").strip())
        if not match:
            continue
        speaker = match.group(1).upper()
        for chunk in split_long_text(match.group(2), lang, int(LANGS[lang]["max_tts_chars"])):
            rows.append((speaker, chunk))
    return ensure_branded_opening(balance_speakers(rows, prefixes), lang)


def eleven_key() -> str:
    key = os.getenv("ELEVEN_KEY") or os.getenv("ELEVENLABS_API_KEY")
    if not key:
        raise RuntimeError("Missing ELEVEN_KEY. Please add it to repo secrets.")
    return key


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


def eleven_tts(text: str, voice_id: str, language_code: str, mp3_path: Path, wav_path: Path, args: argparse.Namespace) -> None:
    response = requests.post(
        args.eleven_base_url.rstrip("/") + f"/v1/text-to-speech/{voice_id}",
        params={"output_format": args.output_format},
        headers={"xi-api-key": eleven_key(), "Content-Type": "application/json"},
        json={"text": text, "model_id": args.eleven_model, "language_code": language_code, "voice_settings": {
            "stability": args.stability, "similarity_boost": args.similarity_boost, "style": args.style, "use_speaker_boost": True,
        }},
        timeout=180,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"ElevenLabs TTS failed: HTTP {response.status_code}: {response.text[:1000]}")
    mp3_path.write_bytes(response.content)
    run(["ffmpeg", "-y", "-i", str(mp3_path), "-ar", "44100", "-ac", "1", "-c:a", "pcm_s16le", str(wav_path)], timeout=180)


def make_audio(rows: list[tuple[str, str]], item_dir: Path, lang: str, args: argparse.Namespace) -> list[dict[str, Any]]:
    cfg = LANGS[lang]
    timeline: list[dict[str, Any]] = []
    wav_parts: list[Path] = []
    with tempfile.TemporaryDirectory(prefix=f"eleven_{lang}_segments_") as temp_dir:
        tmp = Path(temp_dir)
        cursor = 0.0
        for index, (speaker, text) in enumerate(rows[:140], 1):
            mp3 = tmp / f"seg_{index:03d}.mp3"
            wav = tmp / f"seg_{index:03d}.wav"
            voice_id = cfg["voice_a"] if speaker == cfg["prefixes"][0] else cfg["voice_b"]
            eleven_tts(text, voice_id, cfg["language_code"], mp3, wav, args)
            duration = wav_duration(wav)
            timeline.append({"speaker": speaker, "text": text, "start": round(cursor, 3), "end": round(cursor + duration, 3), "voice_id": voice_id, "tts_engine": "elevenlabs"})
            cursor += duration + 0.36
            wav_parts.append(wav)
        combine_wavs(wav_parts, item_dir / cfg["audio"])
    log(f"{lang.upper()} ElevenLabs voices: A={cfg['voice_a']}, B={cfg['voice_b']}")
    return timeline


def srt_time(seconds: float) -> str:
    total_ms = int(round(seconds * 1000))
    hh, rem = divmod(total_ms, 3600000)
    mm, rem = divmod(rem, 60000)
    ss, ms = divmod(rem, 1000)
    return f"{hh:02d}:{mm:02d}:{ss:02d},{ms:03d}"


def write_srt(timeline: list[dict[str, Any]], path: Path, lang: str) -> None:
    cfg = LANGS[lang]
    blocks = []
    for index, seg in enumerate(timeline, 1):
        label = cfg["host_label"] if seg["speaker"] == cfg["prefixes"][0] else cfg["analyst_label"]
        blocks.append(f"{index}\n{srt_time(float(seg['start']))} --> {srt_time(float(seg['end']))}\n{label}: {seg['text']}\n")
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


def wrap_text(text: str, width: int, lang: str) -> list[str]:
    text = re.sub(r"\s+", " ", text or "").strip()
    if lang == "en":
        words = text.split()
        lines: list[str] = []
        current = ""
        for word in words:
            if len(current) + len(word) + 1 <= width:
                current = (current + " " + word).strip()
            else:
                if current:
                    lines.append(current)
                current = word
        if current:
            lines.append(current)
        return lines or [""]
    return [text[i:i + width] for i in range(0, len(text), width)] or [""]


def report_images(item_dir: Path) -> list[Path]:
    assets = item_dir / "assets"
    if not assets.exists():
        return []
    suffixes = {".png", ".jpg", ".jpeg", ".webp"}
    source_images = sorted(p for p in assets.glob("source_image_*") if p.suffix.lower() in suffixes)
    return source_images or sorted(p for p in assets.glob("xhs_card_*.png") if p.suffix.lower() in suffixes)


def looks_chinese(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def translate_title_to_english(title: str, source_text: str, args: argparse.Namespace) -> str:
    prompt = f"""Translate or rewrite this video title into concise English, under 60 characters.
Use neutral research wording. Do not include Chinese. Return only the title.

Current title: {title}
Report context: {trim(source_text, 1600)}"""
    try:
        translated = deepseek(prompt, args, temperature=0.15).strip().strip('"')
        translated = re.sub(r"^[#>*\-\s]+", "", translated).strip()
        if translated and not looks_chinese(translated):
            return sanitize_public_text(translated[:80], "en")
    except Exception as exc:
        log(f"English title rewrite failed: {exc}")
    return str(LANGS["en"]["title_fallback"])


def report_title(item_dir: Path, lang: str, source_text: str, args: argparse.Namespace) -> str:
    preferred = ["wechat_article_en.md", "wechat_article.md", "note.md"] if lang == "en" else ["note.md", "wechat_article.md"]
    for filename in preferred:
        path = item_dir / filename
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = re.sub(r"^[#>*\-\s]+", "", raw).strip()
            if line and not line.startswith("封面") and not line.startswith("!"):
                cleaned = sanitize_public_text(line[:80 if lang == "en" else 42], lang)
                if lang == "en" and looks_chinese(cleaned):
                    return translate_title_to_english(cleaned, source_text, args)
                return cleaned
    return str(LANGS[lang]["title_fallback"])


def extract_json(text: str) -> Any:
    match = re.search(r"(\{[\s\S]*\}|\[[\s\S]*\])", text)
    return json.loads(match.group(1) if match else text)


def fallback_terms(text: str, lang: str, limit: int = 3) -> list[str]:
    if lang == "en":
        words = [w.strip(".,:;!?()[]{}\"'") for w in text.split()]
        words = [w for w in words if len(w) >= 5 and w.lower() not in {"about", "there", "which", "their", "report", "market", "today"}]
        return list(dict.fromkeys([w for w in words if w in text]))[:limit]
    return re.findall(r"[\u4e00-\u9fff]{2,6}|[A-Za-z0-9]{2,}", text)[:limit]


def apply_highlights(title: str, timeline: list[dict[str, Any]], lang: str, args: argparse.Namespace) -> tuple[list[str], list[dict[str, Any]]]:
    sample = [{"i": i, "text": seg["text"]} for i, seg in enumerate(timeline[:90])]
    prompt = f"""Analyze this {lang} video title and subtitles. Pick concise highlight keywords.
Return JSON only: {{"title_keywords":["..."],"lines":[{{"i":0,"keywords":["..."]}}]}}
Each keyword must be an exact continuous substring from the original title or subtitle.
Prefer numbers, sectors, companies, variables, turning points, and core concepts.
Avoid generic words like report, market, this, today, 所以, 报告, 我们.

Title: {title}
Subtitles: {json.dumps(sample, ensure_ascii=False)}"""
    title_terms: list[str] = []
    mapping: dict[int, list[str]] = {}
    try:
        data = extract_json(deepseek(prompt, args, temperature=0.1))
        title_terms = [sanitize_public_text(str(x), lang) for x in data.get("title_keywords", []) if str(x) in title][:3]
        for row in data.get("lines", []):
            idx = int(row.get("i"))
            text = timeline[idx]["text"] if idx < len(timeline) else ""
            mapping[idx] = [sanitize_public_text(str(k), lang) for k in row.get("keywords", []) if str(k) in text][:3]
    except Exception as exc:
        log(f"Highlight keyword analysis failed for {lang}, using fallback: {exc}")
    if not title_terms:
        title_terms = fallback_terms(title, lang, 3)
    for i, seg in enumerate(timeline):
        terms = mapping.get(i) or fallback_terms(str(seg.get("text", "")), lang, 2)
        seg["highlight_terms"] = [t for t in terms if t and t in seg.get("text", "")][:3]
    return title_terms, timeline


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


def split_highlight_chunks(text: str, terms: list[str]) -> list[tuple[str, bool]]:
    chunks: list[tuple[str, bool]] = [(text, False)]
    for term in sorted(set(terms), key=len, reverse=True):
        if not term:
            continue
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
    return chunks


def draw_highlighted_line(draw: ImageDraw.ImageDraw, line: str, terms: list[str], font: ImageFont.ImageFont, y: int, center: bool = False) -> None:
    chunks = split_highlight_chunks(line, terms)
    widths = [draw.textbbox((0, 0), chunk, font=font)[2] - draw.textbbox((0, 0), chunk, font=font)[0] for chunk, _ in chunks]
    total_w = sum(widths)
    x = max(44, (SIZE[0] - total_w) // 2) if center else 120
    for (chunk, marked), width in zip(chunks, widths):
        draw.text((x, y), chunk, font=font, fill=ACCENT if marked else (255, 255, 255))
        x += width


def make_visual_segments(timeline: list[dict[str, Any]], lang: str) -> list[dict[str, Any]]:
    cfg = LANGS[lang]
    visual: list[dict[str, Any]] = []
    max_lines = int(cfg["max_subtitle_lines"])
    for seg in timeline:
        lines = wrap_text(str(seg["text"]), int(cfg["line_width"]), lang)
        pages = [lines[i:i + max_lines] for i in range(0, len(lines), max_lines)] or [[]]
        duration = max(0.5, float(seg["end"]) - float(seg["start"]))
        page_dur = duration / len(pages)
        for page_idx, page_lines in enumerate(pages):
            item = dict(seg)
            item["text"] = "\n".join(page_lines)
            item["page_index"] = page_idx + 1
            item["page_count"] = len(pages)
            item["start"] = round(float(seg["start"]) + page_idx * page_dur, 3)
            item["end"] = round(float(seg["start"]) + (page_idx + 1) * page_dur, 3)
            visual.append(item)
    return visual


def draw_frame(image_path: Path | None, title: str, title_terms: list[str], seg: dict[str, Any], output: Path, index: int, total: int, lang: str) -> None:
    cfg = LANGS[lang]
    canvas = background()
    draw = ImageDraw.Draw(canvas)
    title_font = load_font(54, True)
    subtitle_font = load_font(48, True)
    small_font = load_font(30)
    watermark_font = load_font(54, True)

    y = 66
    for line in wrap_text(title, int(cfg["title_width"]), lang)[:2]:
        draw_highlighted_line(draw, line, title_terms, title_font, y, center=True)
        y += 68
    draw.rounded_rectangle((70, 190, 1010, 198), radius=4, fill=ACCENT)

    stage = (70, 260, 1010, 1110)
    shadow = Image.new("RGBA", SIZE, (0, 0, 0, 0))
    ImageDraw.Draw(shadow).rounded_rectangle((88, 282, 1028, 1132), radius=42, fill=(0, 0, 0, 100))
    canvas = Image.alpha_composite(canvas, shadow.filter(ImageFilter.GaussianBlur(22)))
    draw = ImageDraw.Draw(canvas)
    draw.rounded_rectangle(stage, radius=42, fill=(255, 255, 255, 238))
    if image_path:
        image = fit_image(image_path)
        if image:
            canvas.paste(image.convert("RGBA"), ((SIZE[0] - image.width) // 2, stage[1] + (stage[3] - stage[1] - image.height) // 2), image.convert("RGBA"))

    box_top = 1164 if int(seg.get("page_count", 1)) > 1 else 1190
    draw.rounded_rectangle((70, box_top, 1010, 1668), radius=38, fill=(0, 0, 0, 185))
    label = cfg["host_label"] if seg["speaker"] == cfg["prefixes"][0] else cfg["analyst_label"]
    label_color = (37, 99, 235) if seg["speaker"] == cfg["prefixes"][0] else (190, 96, 135)
    label_right = 286 if lang == "en" else 248
    draw.rounded_rectangle((116, box_top + 44, label_right, box_top + 92), radius=24, fill=label_color)
    draw.text((136, box_top + 48), str(label), font=small_font, fill=(255, 255, 255))

    yy = box_top + 128
    for line in str(seg["text"]).split("\n")[: int(cfg["max_subtitle_lines"])] :
        draw_highlighted_line(draw, line, list(seg.get("highlight_terms", [])), subtitle_font, yy, center=False)
        yy += 66
    if int(seg.get("page_count", 1)) > 1:
        draw.text((900, box_top + 50), f"{seg.get('page_index')}/{seg.get('page_count')}", font=small_font, fill=(220, 230, 245))

    draw.text((70, 1728), f"{index + 1}/{total}", font=small_font, fill=(200, 215, 235))
    progress = int(760 * ((index + 1) / max(total, 1)))
    draw.rounded_rectangle((170, 1740, 930, 1752), radius=6, fill=(255, 255, 255, 70))
    draw.rounded_rectangle((170, 1740, 170 + progress, 1752), radius=6, fill=ACCENT)
    box = draw.textbbox((0, 0), WATERMARK, font=watermark_font)
    draw.text(((SIZE[0] - (box[2] - box[0])) // 2, 1802), WATERMARK, font=watermark_font, fill=(205, 220, 238))
    canvas.convert("RGB").save(output, quality=93)


def frame_duration(timeline: list[dict[str, Any]], index: int) -> float:
    if index + 1 < len(timeline):
        return max(0.5, float(timeline[index + 1]["start"]) - float(timeline[index]["start"]))
    return max(0.5, float(timeline[index]["end"]) - float(timeline[index]["start"]) + 0.36)


def make_video(item_dir: Path, timeline: list[dict[str, Any]], lang: str, title: str, title_terms: list[str]) -> list[dict[str, Any]]:
    cfg = LANGS[lang]
    images = report_images(item_dir)
    visual_timeline = make_visual_segments(timeline, lang)
    with tempfile.TemporaryDirectory(prefix=f"portal_{lang}_frames_") as temp_dir:
        tmp = Path(temp_dir)
        concat = tmp / "concat.txt"
        concat_lines: list[str] = []
        for index, seg in enumerate(visual_timeline):
            frame = tmp / f"frame_{index:04d}.png"
            image_path = images[index % len(images)] if images else None
            draw_frame(image_path, title, title_terms, seg, frame, index, len(visual_timeline), lang)
            concat_lines.append(f"file '{frame.as_posix()}'\n")
            concat_lines.append(f"duration {frame_duration(visual_timeline, index):.3f}\n")
        concat_lines.append(concat_lines[-2])
        concat.write_text("".join(concat_lines), encoding="utf-8")
        silent = tmp / "silent.mp4"
        run(["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat), "-vsync", "vfr", "-pix_fmt", "yuv420p", str(silent)], timeout=1200)
        run(["ffmpeg", "-y", "-i", str(silent), "-i", str(item_dir / cfg["audio"]), "-c:v", "libx264", "-preset", "medium", "-crf", "23", "-c:a", "aac", "-b:a", "160k", "-shortest", str(item_dir / cfg["video"])], timeout=1200)
    return visual_timeline


def generate_language(item_dir: Path, lang: str, source_text: str, args: argparse.Namespace, render_video: bool = True) -> dict[str, Any]:
    cfg = LANGS[lang]
    prompt = Path(str(cfg["prompt"])).read_text(encoding="utf-8").format(podcast_minutes=args.podcast_minutes, source_text=source_text)
    (item_dir / str(cfg["prompt_out"])).write_text(prompt, encoding="utf-8")
    raw_script = deepseek(prompt, args, temperature=0.72)
    rows = parse_script(raw_script, cfg["prefixes"], lang)
    if not rows:
        raise RuntimeError(f"DeepSeek returned no {cfg['prefixes'][0]}/{cfg['prefixes'][1]} rows for {lang}")
    clean_script = "\n".join(f"{spk}: {text}" for spk, text in rows) + "\n"
    (item_dir / str(cfg["script"])).write_text(clean_script, encoding="utf-8")
    timeline = make_audio(rows, item_dir, lang, args)
    title = report_title(item_dir, lang, source_text, args)
    title_terms, timeline = apply_highlights(title, timeline, lang, args)
    (item_dir / str(cfg["timeline"])).write_text(json.dumps(timeline, ensure_ascii=False, indent=2), encoding="utf-8")
    write_srt(timeline, item_dir / str(cfg["srt"]), lang)
    result = {
        f"podcast_{lang}_script": cfg["script"], f"podcast_{lang}_audio": cfg["audio"],
        f"podcast_{lang}_subtitles": cfg["srt"], f"podcast_{lang}_timeline": cfg["timeline"],
        f"podcast_{lang}_voice_a": cfg["voice_a"], f"podcast_{lang}_voice_b": cfg["voice_b"],
        f"podcast_{lang}_title_highlights": title_terms, f"podcast_{lang}_title": title,
        f"podcast_{lang}_video_rendered": bool(render_video),
    }
    if render_video:
        visual_timeline = make_video(item_dir, timeline, lang, title, title_terms)
        (item_dir / str(cfg["visual_timeline"])).write_text(json.dumps(visual_timeline, ensure_ascii=False, indent=2), encoding="utf-8")
        result[f"podcast_{lang}_visual_timeline"] = cfg["visual_timeline"]
        result[f"podcast_{lang}_video"] = cfg["video"]
    return result


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-v4-flash"))
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

    item_dir = find_item(Path(args.output_dir))
    raw_source = (item_dir / "source_mineru.md").read_text(encoding="utf-8", errors="ignore")
    source_text = trim(sanitize_public_text(raw_source, "zh"), args.prompt_chars)
    status_update: dict[str, Any] = {
        "podcast_video_watermark": WATERMARK,
        "podcast_tts_engine_actual": "elevenlabs",
        "subtitle_source": "same text as TTS; role tags normalized; rows split by punctuation before TTS; long visual subtitles are paged",
        "highlight_source": "DeepSeek title and subtitle keyword analysis",
        "sensitive_filter": "local xhs_notes-style replacements before TTS and rendering",
    }
    for lang in ["zh", "en"]:
        log(f"Generating {lang.upper()} podcast audio/video")
        status_update.update(generate_language(item_dir, lang, source_text, args))
    status_path = item_dir / "status.json"
    status: dict[str, Any] = {}
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
        except Exception:
            status = {}
    status.update(status_update)
    status_path.write_text(json.dumps(status, ensure_ascii=False, indent=2), encoding="utf-8")
    log(f"Generated bilingual ElevenLabs podcast/video in {item_dir}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
