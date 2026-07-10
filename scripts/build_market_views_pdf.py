#!/usr/bin/env python3
"""Build a market-view roundup from generated daily report outputs.

The script collects already-generated report folders under
xhs_notes/dropbox/<date>/shard_*/<report>/, extracts clean exhibit-style figure
candidates, asks DeepSeek to synthesize a categorized market-view roundup, and
writes structured JSON plus a LaTeX source. PDF rendering is handled by the
ReportLab renderer workflow step, so this script no longer needs a heavy TeX
install for the normal path.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
from pathlib import Path
from typing import Any

import requests

try:
    from finalize_outputs import sanitize_text
except Exception:
    def sanitize_text(text: str) -> str:
        return text

try:
    from institution_names import infer_institution_name
except Exception:
    def infer_institution_name(*_values: Any) -> str:
        return ""

EXHIBIT_RE = re.compile(r"\b(?:Exhibit|EXHIBIT|Exh\.?|Figure|FIGURE)\s*[-#:：]?\s*\d+\b|图表\s*[-#:：]?\s*\d+", re.I)
EXHIBIT_TITLE_RE = re.compile(r"((?:Exhibit|EXHIBIT|Exh\.?|Figure|FIGURE)\s*[-#:：]?\s*\d+\s*[:：-]\s*[^\n。]{8,220}|图表\s*[-#:：]?\s*\d+\s*[:：-]\s*[^\n。]{8,220})", re.I)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^\)]+)\)")
DATE_DIR_RE = re.compile(r"^\d{6,8}$")
REPORT_MARKER_FILES = ("source_mineru.md", "wechat_article.md", "note.md")
EMAIL_RE = re.compile(r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,}", re.I)
PHONE_RE = re.compile(r"(?:\+?\d[\d\s().-]{7,}\d)")
HTML_TAG_RE = re.compile(r"<[^>]+>")
NOISY_WORD_RE = re.compile(r"(?:details|summary|table|tbody|thead|</|<td|<tr|source:|global investment research|equity research|analyst)", re.I)
ROUNDUP_SOURCE_ORDER = ["bank_research", "consulting", "institution"]
EXTERNAL_SOURCE_GROUPS = {"institution", "consulting"}
SOURCE_GROUP_LABELS = {
    "bank_research": "投行/券商",
    "consulting": "战略咨询",
    "institution": "智库/国际机构",
}
DISCLAIMER_TEXT = """This community is a paid learning and information-sharing community created for general educational purposes only. The membership fee is charged solely for access to community discussions, educational content, organization, and operational costs. It is not an advisory fee, management fee, performance fee, brokerage fee, or compensation for personalized financial, investment, legal, tax, or professional advice.

I participate and share information solely as an individual and for educational discussion among community members. I am not acting as a financial adviser, investment adviser, broker, dealer, portfolio manager, legal adviser, tax adviser, accountant, fiduciary, or any other licensed professional adviser. Nothing shared in this community constitutes, and should not be interpreted as, financial advice, investment advice, legal advice, tax advice, a recommendation, solicitation, offer, endorsement, instruction, or guarantee to buy, sell, hold, short, trade, or invest in any security, cryptocurrency, fund, derivative, strategy, or other financial product.

All content shared in this community, including messages, discussions, links, files, charts, examples, market commentary, watchlists, AI-generated or AI-polished summaries, and third-party materials, is general, impersonal, and educational in nature. It does not take into account any individual's financial situation, investment objectives, risk tolerance, investment horizon, liquidity needs, tax status, legal restrictions, or suitability requirements. No content should be relied upon as suitable for any specific person, account, portfolio, or financial decision.

Information shared in this community may be incomplete, inaccurate, outdated, speculative, AI-generated, AI-edited, or based on third-party internet sources that have not been independently verified. I make no representation or warranty as to the accuracy, completeness, timeliness, reliability, or suitability of any information shared.

Financial markets involve substantial risk, including the possible loss of principal. Past performance, historical data, hypothetical examples, simulated results, backtests, personal opinions, or educational examples do not guarantee future results. Each member is solely responsible for conducting their own research, exercising independent judgment, and making their own decisions. Before making any financial, investment, legal, or tax decision, members should consult qualified and licensed professionals.

Participation in this community, payment of any membership fee, or communication with me or other members does not create any adviser-client, fiduciary, professional, contractual, agency, partnership, employment, or other advisory relationship. By joining or participating in this community, you acknowledge and agree that you are solely responsible for your own decisions, actions, transactions, profits, losses, risks, and consequences, and that I shall not be liable for any direct, indirect, incidental, consequential, financial, legal, tax, or other loss or damage arising from or related to any content, discussion, information, or material shared in this community."""


def log(message: str) -> None:
    print(message, flush=True)


def latex_escape(text: str) -> str:
    text = sanitize_text(str(text or ""))
    replacements = {
        "\\": r"\textbackslash{}", "&": r"\&", "%": r"\%", "$": r"\$", "#": r"\#",
        "_": r"\_", "{": r"\{", "}": r"\}", "~": r"\textasciitilde{}", "^": r"\textasciicircum{}",
    }
    return "".join(replacements.get(ch, ch) for ch in text)


def normalize_space(text: str) -> str:
    return re.sub(r"\s+", " ", sanitize_text(text or "")).strip()


def trim_text(text: str, max_chars: int) -> str:
    text = re.sub(r"\n{3,}", "\n\n", text or "").strip()
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    head = int(max_chars * 0.72)
    tail = int(max_chars * 0.2)
    return text[:head] + "\n\n[... middle omitted ...]\n\n" + text[-tail:]


def latest_date_dir(root: Path) -> Path:
    if not root.exists():
        raise RuntimeError(f"Dropbox output root not found: {root}")
    candidates = [p for p in root.iterdir() if p.is_dir() and DATE_DIR_RE.match(p.name)]
    if not candidates:
        raise RuntimeError(f"No date-named folders found under {root}")
    return max(candidates, key=lambda p: int(p.name))


def date_dir_names(root: Path) -> set[str]:
    if not root.exists():
        return set()
    return {p.name for p in root.iterdir() if p.is_dir() and DATE_DIR_RE.match(p.name)}


def latest_date_name(roots: list[Path]) -> str:
    names: set[str] = set()
    for root in roots:
        names.update(date_dir_names(root))
    if not names:
        roots_text = ", ".join(str(root) for root in roots)
        raise RuntimeError(f"No date-named folders found under source roots: {roots_text}")
    return max(names, key=lambda name: int(name))


def find_report_dirs(date_dir: Path) -> list[Path]:
    if not date_dir.exists():
        return []
    report_dirs: list[Path] = []
    for marker in REPORT_MARKER_FILES:
        for path in sorted(date_dir.rglob(marker)):
            if path.is_file():
                report_dirs.append(path.parent)
    seen = set()
    unique = []
    for p in report_dirs:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


def latest_existing_date_dir(root: Path) -> Path | None:
    if not root.exists():
        return None
    candidates = [p for p in root.iterdir() if p.is_dir() and DATE_DIR_RE.match(p.name)]
    if not candidates:
        return None
    return max(candidates, key=lambda p: int(p.name))


def shard_dirs(date_dir: Path) -> list[Path]:
    if not date_dir.exists():
        return []
    return [p for p in sorted(date_dir.glob("shard_*")) if p.is_dir()]


def report_date_from_path(report_dir: Path) -> str:
    for part in reversed(report_dir.parts):
        if DATE_DIR_RE.match(part):
            return part
    return ""


def source_date_dirs(root: Path, extra_roots: list[Path], date_folder: str) -> tuple[str, list[Path]]:
    roots = [root, *extra_roots]
    if date_folder != "latest":
        report_date = date_folder
        return report_date, [source_root / report_date for source_root in roots]

    report_date = latest_date_name(roots)
    date_dirs: list[Path] = []
    for source_root in roots:
        latest_dir = latest_existing_date_dir(source_root)
        if latest_dir is None:
            log(f"Source root has no date folders, skipping: {source_root}")
            continue
        date_dirs.append(latest_dir)
    return report_date, date_dirs


def report_title(report_dir: Path) -> str:
    for filename in ["wechat_article.md", "note.md"]:
        path = report_dir / filename
        if not path.exists():
            continue
        for raw in path.read_text(encoding="utf-8", errors="ignore").splitlines():
            line = raw.strip()
            if line.startswith("# "):
                title = re.sub(r"^#+\s*", "", line).strip()
                if title:
                    return sanitize_text(title[:100])
    status_path = report_dir / "status.json"
    if status_path.exists():
        try:
            status = json.loads(status_path.read_text(encoding="utf-8", errors="ignore"))
            source_pdf = status.get("source_pdf") or ""
            if source_pdf:
                return sanitize_text(Path(source_pdf).stem[:120])
        except Exception:
            pass
    return sanitize_text(report_dir.name.replace("-", " ")[:100])


def load_status(report_dir: Path) -> dict[str, Any]:
    path = report_dir / "status.json"
    if not path.exists():
        return {}
    try:
        data = json.loads(path.read_text(encoding="utf-8", errors="ignore"))
        return data if isinstance(data, dict) else {}
    except Exception:
        return {}


def infer_source_group(report_dir: Path) -> str:
    parts = {part.lower() for part in report_dir.parts}
    if "institutions" in parts:
        return "institution"
    if "consulting" in parts:
        return "consulting"
    return "bank_research"


def source_group_label(source_group: str) -> str:
    return SOURCE_GROUP_LABELS.get(source_group, source_group or "未知来源")


def infer_source_name(report_dir: Path, title: str, status: dict[str, Any]) -> str:
    for key in ("institution_name", "source_name", "institution_cn", "institution_en"):
        value = normalize_space(str(status.get(key) or ""))
        if value:
            return value
    return infer_institution_name(report_dir.name, title, status)


def report_digest(report_dir: Path, max_chars: int) -> dict[str, Any]:
    title = report_title(report_dir)
    pieces = []
    for filename in ["wechat_article.md", "note.md", "source_mineru.md"]:
        path = report_dir / filename
        if path.exists():
            text = path.read_text(encoding="utf-8", errors="ignore")
            pieces.append(f"[{filename}]\n{trim_text(text, max_chars // 2)}")
    digest = trim_text("\n\n".join(pieces), max_chars)
    return {"title": title, "digest": sanitize_text(digest)}


def clean_markdown_for_extract(text: str) -> str:
    text = IMAGE_RE.sub(" ", text or "")
    text = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = EMAIL_RE.sub(" ", text)
    text = PHONE_RE.sub(" ", text)
    cleaned_lines: list[str] = []
    for raw in text.splitlines():
        line = raw.strip()
        if not line:
            cleaned_lines.append("")
            continue
        if line.startswith("|") or NOISY_WORD_RE.search(line):
            continue
        line = re.sub(r"^#{1,6}\s*", "", line)
        line = re.sub(r"^[>*\-+]\s*", "", line)
        line = re.sub(r"`{1,3}", "", line)
        line = re.sub(r"\*\*([^*]+)\*\*", r"\1", line)
        cleaned_lines.append(line)
    text = "\n".join(cleaned_lines)
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = re.sub(r"[ \t]{2,}", " ", text)
    return sanitize_text(text).strip()


def report_extract(report_dir: Path, max_chars: int) -> str:
    """Keep a readable per-report appendix excerpt outside the LLM summary."""
    blocks: list[str] = []
    for filename in ["wechat_article.md", "note.md", "source_mineru.md"]:
        path = report_dir / filename
        if not path.exists():
            continue
        text = clean_markdown_for_extract(path.read_text(encoding="utf-8", errors="ignore"))
        if not text:
            continue
        for para in text.split("\n\n"):
            para = normalize_space(para)
            if len(para) < 30:
                continue
            if any(para == existing for existing in blocks):
                continue
            blocks.append(para)
            if len("\n\n".join(blocks)) >= max_chars:
                return trim_text("\n\n".join(blocks), max_chars)
    return trim_text("\n\n".join(blocks), max_chars)


def resolve_image_path(markdown_path: Path, image_ref: str) -> Path | None:
    ref = image_ref.strip().strip("<>")
    if ref.startswith("http://") or ref.startswith("https://"):
        return None
    ref = ref.split("#", 1)[0].split("?", 1)[0]
    for candidate in [markdown_path.parent / ref, markdown_path.parent.parent / ref]:
        if candidate.exists() and candidate.is_file():
            return candidate
    basename = Path(ref).name
    for candidate in markdown_path.parent.rglob(basename):
        if candidate.is_file():
            return candidate
    return None


def remove_noise(text: str) -> str:
    text = IMAGE_RE.sub(" ", text or "")
    text = EMAIL_RE.sub(" ", text)
    text = PHONE_RE.sub(" ", text)
    text = HTML_TAG_RE.sub(" ", text)
    text = re.sub(r"\|[^\n]*\|", " ", text)
    text = re.sub(r"Source\s*:[^\n]+", " ", text, flags=re.I)
    text = re.sub(r"(?:GS|JPM|MS|BofA|Citi|UBS|DB)\s+Global\s+Investment\s+Research", " ", text, flags=re.I)
    text = re.sub(r"\s+", " ", text)
    return sanitize_text(text).strip()


def clean_exhibit_context(raw_context: str, fallback_label: str) -> str | None:
    """Return a clean caption or None if the surrounding text is too noisy.

    The uploaded sample showed captions polluted by analyst emails, phone
    numbers, HTML details/summary blocks and markdown tables. Those are removed
    or skipped here before the figure candidate is exposed to DeepSeek/PDF.
    """
    raw_context = raw_context or ""
    lines = []
    for raw in raw_context.splitlines():
        line = raw.strip()
        if not line:
            continue
        if IMAGE_RE.search(line):
            line = IMAGE_RE.sub(" ", line)
        if EMAIL_RE.search(line) or PHONE_RE.search(line):
            # Lines with analyst emails/phone numbers create the ugly captions in the PDF.
            continue
        if NOISY_WORD_RE.search(line) or "|" in line or "<" in line or ">" in line:
            continue
        lines.append(line)
    candidate = " ".join(lines) if lines else raw_context
    title_matches = EXHIBIT_TITLE_RE.findall(candidate)
    if title_matches:
        candidate = title_matches[-1]
    candidate = remove_noise(candidate)
    if not candidate:
        return None
    # Cut at obvious noise tails.
    candidate = re.split(r"\b(?:References|Source|来源|联系人|Analyst)\b", candidate, maxsplit=1, flags=re.I)[0].strip()
    candidate = re.sub(r"\s+", " ", candidate)
    # If it is still noisy after cleaning, skip the figure entirely.
    if EMAIL_RE.search(candidate) or PHONE_RE.search(candidate) or NOISY_WORD_RE.search(candidate) or "|" in candidate or "<" in candidate or ">" in candidate:
        return None
    if len(candidate) < 12:
        candidate = fallback_label
    return candidate[:260]


def extract_exhibit_figures(report_dir: Path, report_id: str, title: str, max_per_report: int) -> list[dict[str, Any]]:
    md_path = report_dir / "source_mineru.md"
    if not md_path.exists():
        return []
    lines = md_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    figures: list[dict[str, Any]] = []
    seen_paths: set[str] = set()
    for i, line in enumerate(lines):
        match = IMAGE_RE.search(line)
        if not match:
            continue
        context = "\n".join(lines[max(0, i - 8): min(len(lines), i + 9)])
        if not EXHIBIT_RE.search(context):
            continue
        image_path = resolve_image_path(md_path, match.group(1))
        if not image_path:
            continue
        resolved = str(image_path.resolve())
        if resolved in seen_paths:
            continue
        label_match = EXHIBIT_RE.search(context)
        label = sanitize_text(label_match.group(0) if label_match else "Exhibit")
        context_clean = clean_exhibit_context(context, label)
        if context_clean is None:
            log(f"Skip noisy exhibit candidate in {report_dir.name}: {label}")
            continue
        seen_paths.add(resolved)
        figures.append({
            "report_id": report_id,
            "report_title": title,
            "source_path": str(image_path),
            "label": label,
            "context": context_clean,
            "figure_type": "source_exhibit",
        })
        if max_per_report > 0 and len(figures) >= max_per_report:
            break
    return figures


def status_visual_candidates(report_dir: Path, status: dict[str, Any]) -> list[Path]:
    candidates: list[Path] = []
    for rel in status.get("images") or []:
        if isinstance(rel, str) and rel:
            candidates.append(report_dir / rel)
    if not candidates:
        candidates.extend(sorted((report_dir / "assets").glob("xhs_card_*.png")))
    cover = status.get("cover")
    if isinstance(cover, str) and cover:
        candidates.append(report_dir / cover)
    seen: set[str] = set()
    unique: list[Path] = []
    for path in candidates:
        if not path.exists() or not path.is_file():
            continue
        resolved = str(path.resolve())
        if resolved in seen:
            continue
        seen.add(resolved)
        unique.append(path)
    return unique


def extract_external_visual_cards(
    report_dir: Path,
    report_id: str,
    title: str,
    source_name: str,
    status: dict[str, Any],
    max_per_report: int,
) -> list[dict[str, Any]]:
    if max_per_report <= 0:
        return []
    cards: list[dict[str, Any]] = []
    for idx, image_path in enumerate(status_visual_candidates(report_dir, status), 1):
        label = f"{source_name or '外部信源'}视觉摘要 {idx}"
        context = f"{source_name or '外部信源'}｜{title}｜用于快速识别该外部报告的核心问题和市场含义。"
        cards.append({
            "report_id": report_id,
            "report_title": title,
            "source_path": str(image_path),
            "label": label,
            "context": context[:260],
            "figure_type": "external_card",
        })
        if len(cards) >= max_per_report:
            break
    return cards


def convert_webp_if_needed(src: Path, target: Path) -> Path:
    if src.suffix.lower() != ".webp":
        shutil.copy2(src, target)
        return target
    try:
        from PIL import Image
        target_png = target.with_suffix(".png")
        Image.open(src).convert("RGB").save(target_png)
        return target_png
    except Exception:
        shutil.copy2(src, target)
        return target


def copy_figures(figures: list[dict[str, Any]], figures_dir: Path, max_figures: int) -> list[dict[str, Any]]:
    if figures_dir.exists():
        shutil.rmtree(figures_dir)
    figures_dir.mkdir(parents=True, exist_ok=True)
    source_figures = [fig for fig in figures if fig.get("figure_type") != "external_card"]
    selected = source_figures if max_figures <= 0 else source_figures[:max_figures]
    copied: list[dict[str, Any]] = []
    for idx, fig in enumerate(selected, 1):
        src = Path(fig["source_path"])
        suffix = src.suffix.lower() or ".png"
        if suffix not in {".png", ".jpg", ".jpeg", ".webp"}:
            continue
        target = figures_dir / f"fig_{idx:03d}{suffix}"
        try:
            actual = convert_webp_if_needed(src, target)
        except Exception as exc:
            log(f"Skip figure copy failed {src}: {exc}")
            continue
        copied.append({**fig, "figure_id": f"F{idx:03d}", "latex_path": f"figures/{actual.name}"})
    return copied


def parse_json_response(response: requests.Response, label: str) -> dict[str, Any]:
    try:
        data = response.json()
    except Exception as exc:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, non-json response: {response.text[:500]}") from exc
    if response.status_code >= 400:
        raise RuntimeError(f"{label}: HTTP {response.status_code}, response={json.dumps(data, ensure_ascii=False)[:1000]}")
    return data


def call_deepseek(prompt: str, args: argparse.Namespace, label: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    response = requests.post(
        args.deepseek_base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": args.model,
            "temperature": 0.25,
            "max_tokens": getattr(args, "deepseek_max_tokens", 8192),
            "messages": [
                {
                    "role": "system",
                    "content": (
                        "你是面向全球机构投资者的资深研究编辑。严格执行报告 ID 覆盖要求，"
                        "保留关键数据、方向、分歧与边际变化。只输出合法 JSON，不要输出 Markdown 代码块。"
                    ),
                },
                {"role": "user", "content": prompt},
            ],
        },
        timeout=240,
    )
    data = parse_json_response(response, label)
    return data["choices"][0]["message"]["content"].strip()


def extract_json(text: str) -> Any:
    try:
        return json.loads(text.strip())
    except Exception:
        pass
    match = re.search(r"(\{.*\}|\[.*\])", text.strip(), flags=re.S)
    if not match:
        raise ValueError("No JSON object found")
    return json.loads(match.group(1))


def build_prompt(reports: list[dict[str, Any]], figures: list[dict[str, Any]], args: argparse.Namespace) -> str:
    source_counts = {
        source_group_label(group): sum(1 for report in reports if report.get("source_group") == group)
        for group in ROUNDUP_SOURCE_ORDER
    }
    return f"""
# Market Views 生成协议

目标读者是关注国际主流叙事、数据、图表和边际变化的机构从业者。

1. 投行/券商是正文主体；战略咨询与智库/国际机构只作两个彼此独立的辅助板块。
2. 先依据当天投行报告标题规划动态目录，再逐目录板块调用 DeepSeek。禁止把全部报告与全部图表塞入一次请求。
3. 每篇投行报告必须进入至少一条可见的 bank_view；只有 references 而没有观点文本不算覆盖。
4. 每个投行板块必须给出共识、分歧、逐机构整合观点、关键数据、边际变化及 2-4 张原始报告图表。
5. 正文不展示报告 ID、文件名或逐篇标题目录；PDF 只展示整合后的观点与简短覆盖统计。
6. 投行常用 GS、JPM、MS、BofA、Citi、UBS、DB、NOM 等缩写。
7. 不给投资建议，不写买卖评级，不输出纯文字的逐篇摘录。
8. 当投行输入很多时允许形成 40-70 页，不设 20 页上限。

本次输入：{len(reports)} 篇报告、{len(figures)} 张清洁图表候选。
来源数量：{json.dumps(source_counts, ensure_ascii=False)}
每篇报告送入单个主题请求的最大正文长度：{args.per_report_prompt_chars} 字符。
""".strip()


def fallback_summary(reports: list[dict[str, Any]], figures: list[dict[str, Any]]) -> dict[str, Any]:
    bank_reports = source_group_reports(reports, "bank_research")
    supporting = [
        build_source_roundup_for_group(source_group_reports(reports, group), figures, group, max_themes=3)
        for group in ("consulting", "institution")
    ]
    bank_roundup = build_fallback_bank_roundup(bank_reports, figures)
    return compose_market_summary(bank_roundup, supporting, reports)


EXTERNAL_CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("宏观政策与金融稳定", ("imf", "bis", "central bank", "monetary", "inflation", "fiscal", "debt", "bond", "sovereign", "banking", "货币", "财政", "通胀", "债", "主权", "金融", "央行", "数据透明")),
    ("AI、技术与生产率", ("ai", "artificial intelligence", "digital", "cyber", "agent", "data center", "technology", "算力", "人工智能", "数字", "网络", "生产率", "机器人")),
        ("地缘政治与安全", ("rand", "brookings", "defense", "security", "conflict", "war", "iran", "turkey", "hormuz", "geopolitical", "military", "地缘", "安全", "冲突", "战争", "伊朗", "土耳其", "墨西哥", "兰德", "布鲁金斯", "防务", "军工")),
    ("气候、发展与社会结构", ("world bank", "climate", "poverty", "gender", "tax", "employment", "trade", "energy", "biodiversity", "development", "气候", "贫困", "性别", "就业", "税", "贸易", "生物多样性", "发展")),
    ("咨询与企业战略", ("mckinsey", "bcg", "bain", "consulting", "麦肯锡", "波士顿咨询", "贝恩", "战略", "企业")),
)


def figure_ids_for_report(figures: list[dict[str, Any]], report_id: str, limit: int = 1) -> list[str]:
    ids: list[str] = []
    for fig in figures:
        if str(fig.get("report_id")) != report_id or fig.get("figure_type") == "external_card":
            continue
        fid = str(fig.get("figure_id") or "")
        if fid and fid not in ids:
            ids.append(fid)
        if len(ids) >= limit:
            break
    return ids


def external_category_for(report: dict[str, Any]) -> str:
    title_haystack = " ".join([
        str(report.get("title") or ""),
        str(report.get("institution_name") or ""),
        str(report.get("source_group") or ""),
    ]).lower()
    if report.get("source_group") == "consulting":
        return "咨询与企业战略"

    title_priority = (
        ("AI、技术与生产率", ("ai", "artificial intelligence", "digital", "cyber", "agent", "data center", "technology", "算力", "人工智能", "数字", "网络", "生产率", "机器人")),
        ("地缘政治与安全", ("rand", "brookings", "defense", "security", "conflict", "war", "iran", "turkey", "hormuz", "geopolitical", "military", "地缘", "安全", "冲突", "战争", "伊朗", "土耳其", "墨西哥", "兰德", "布鲁金斯", "防务", "军工", "生物武器", "霍尔木兹")),
        ("宏观政策与金融稳定", ("imf", "bis", "central bank", "monetary", "inflation", "fiscal", "debt", "bond", "sovereign", "banking", "货币", "财政", "通胀", "债", "主权", "金融", "央行", "数据透明")),
        ("气候、发展与社会结构", ("world bank", "climate", "poverty", "gender", "tax", "employment", "trade", "energy", "biodiversity", "development", "气候", "贫困", "性别", "就业", "税", "贸易", "生物多样性", "发展")),
    )
    for category, keywords in title_priority:
        if any(keyword.lower() in title_haystack for keyword in keywords):
            return category

    body_haystack = " ".join([
        title_haystack,
        str(report.get("digest") or "")[:1500],
    ]).lower()
    for category, keywords in EXTERNAL_CATEGORY_RULES:
        if any(keyword.lower() in body_haystack for keyword in keywords):
            return category
    return "外部研究补充"


def first_signal(text: str, max_chars: int = 110) -> str:
    cleaned = clean_markdown_for_extract(text or "")
    for para in re.split(r"\n{2,}", cleaned):
        para = normalize_space(para)
        if len(para) < 28:
            continue
        para = re.sub(r"^\[[^\]]+\]\s*", "", para)
        sentence = re.split(r"(?<=[。.!?！？])\s+", para)[0]
        if len(sentence) > max_chars:
            sentence = sentence[:max_chars].rstrip() + "..."
        return sentence
    return "该报告提供了一条需要纳入今日市场判断的新增信号。"


def relevance_for_category(category: str) -> str:
    if "宏观" in category:
        return "用于校准利率、通胀、财政约束和金融稳定叙事。"
    if "AI" in category:
        return "用于判断 AI 投资周期、生产率扩散和产业约束是否正在改变资产定价。"
    if "地缘" in category:
        return "用于补充能源、航运、防务和供应链风险的尾部情景。"
    if "气候" in category:
        return "用于观察长期增长、资源约束、社会结构和政策执行质量。"
    if "咨询" in category:
        return "用于补充企业战略、管理层议题和产业落地视角。"
    return "用于补充投行报告之外的政策、产业或长期结构变量。"


BANK_CATEGORY_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("宏观、央行与利率", ("macro", "fed", "ecb", "boj", "inflation", "fiscal", "rates", "yield", "bond", "宏观", "美联储", "欧央行", "央行", "通胀", "财政", "利率", "收益率", "债券")),
    ("外汇与跨境资金", ("fx", "currency", "dollar", "yen", "renminbi", "rmb", "forex", "外汇", "美元", "日元", "人民币", "汇率", "中间价", "跨境资金")),
    ("股票策略、估值与资金流", ("equity strategy", "valuation", "earnings", "positioning", "fund flow", "liquidity", "retail investor", "股票策略", "估值", "盈利", "仓位", "资金流", "流动性", "散户", "风险偏好")),
    ("AI、半导体与硬件", ("ai", "semiconductor", "chip", "gpu", "cpu", "memory", "hbm", "server", "pcb", "ccl", "mlcc", "abf", "算力", "半导体", "芯片", "存储", "服务器", "硬件", "载板")),
    ("软件、互联网与数字平台", ("software", "cloud", "internet", "e-commerce", "platform", "saas", "token", "软件", "云", "互联网", "电商", "平台", "即时零售", "大模型")),
    ("中国经济、地产与金融", ("china", "property", "real estate", "bank", "insurance", "credit", "inventory cycle", "中国", "地产", "房地产", "银行", "保险", "信贷", "库存周期", "人民币流动性")),
    ("消费、零售与奢侈品", ("consumer", "retail", "luxury", "beauty", "travel", "leisure", "apparel", "消费", "零售", "奢侈品", "美妆", "旅游", "免税")),
    ("医疗健康与生命科学", ("healthcare", "pharma", "biotech", "drug", "medical", "hospital", "医药", "医疗", "生物制药", "新药", "管线", "医院")),
    ("能源、大宗与公用事业", ("oil", "gas", "commodity", "copper", "gold", "power", "utility", "energy", "solar", "原油", "天然气", "能源", "大宗", "铜", "铝", "黄金", "电力", "公用事业", "光伏")),
    ("汽车、新能源与工业", ("auto", "ev", "battery", "industrial", "machinery", "robot", "automation", "汽车", "电动车", "新能源", "电池", "工业", "机械", "机器人", "自动化")),
    ("航天、国防与先进制造", ("space", "defense", "aerospace", "satellite", "rocket", "advanced manufacturing", "航天", "太空", "国防", "防务", "卫星", "火箭", "先进制造")),
    ("日本、韩国与亚洲市场", ("japan", "korea", "india", "asean", "singapore", "日本", "韩国", "印度", "东南亚", "新加坡", "亚洲")),
    ("欧洲、美洲与新兴市场", ("europe", "eurozone", "latin america", "emerging market", "canada", "mexico", "欧洲", "欧元区", "拉美", "新兴市场", "加拿大", "墨西哥")),
)

BANK_ALIAS_RULES: tuple[tuple[str, tuple[str, ...]], ...] = (
    ("GS", ("goldman sachs", "goldman", "高盛", "gs")),
    ("JPM", ("jpmorgan", "jp morgan", "摩根大通", "jpm")),
    ("MS", ("morgan stanley", "摩根士丹利", "ms")),
    ("BofA", ("bank of america", "bofa", "美银")),
    ("Citi", ("citigroup", "citi", "花旗")),
    ("UBS", ("ubs", "瑞银")),
    ("DB", ("deutsche bank", "deutsche", "德银", "db")),
    ("NOM", ("nomura", "野村", "nom")),
    ("Bernstein", ("bernstein", "伯恩斯坦")),
    ("Barclays", ("barclays", "巴克莱")),
    ("Jefferies", ("jefferies", "杰富瑞")),
    ("HSBC", ("hsbc", "汇丰")),
    ("Macquarie", ("macquarie", "麦格理")),
)


def bank_category_for(report: dict[str, Any]) -> str:
    title = str(report.get("title") or "").lower()
    for category, keywords in BANK_CATEGORY_RULES:
        if any(keyword in title for keyword in keywords):
            return category
    digest = str(report.get("digest") or "")[:1800].lower()
    scored = []
    for index, (category, keywords) in enumerate(BANK_CATEGORY_RULES):
        score = sum(1 for keyword in keywords if keyword in digest)
        if score:
            scored.append((score, -index, category))
    if scored:
        return max(scored)[2]
    return "其他公司与行业信号"


def bank_alias(report: dict[str, Any]) -> str:
    raw_name = normalize_space(str(report.get("institution_name") or ""))
    title = normalize_space(str(report.get("title") or ""))
    haystack = f"{raw_name} {title[:40]}".lower()
    for alias, keywords in BANK_ALIAS_RULES:
        for keyword in keywords:
            lowered = keyword.lower()
            if lowered == raw_name.lower():
                return alias
            if len(lowered) <= 3:
                if re.search(rf"(?<![a-z0-9]){re.escape(lowered)}(?![a-z0-9])", haystack):
                    return alias
            elif lowered in haystack:
                return alias
    if raw_name:
        return raw_name[:20]
    prefix = re.split(r"[：:]", title, maxsplit=1)[0].strip()
    return prefix[:20] if prefix else "投行"


def report_category_for(report: dict[str, Any]) -> str:
    source_group = report.get("source_group")
    if source_group == "bank_research":
        return bank_category_for(report)
    return external_category_for(report)


def source_group_reports(reports: list[dict[str, Any]], source_group: str) -> list[dict[str, Any]]:
    return [r for r in reports if r.get("source_group") == source_group]


def signal_sentences(text: str, limit: int = 3, max_chars: int = 180) -> list[str]:
    cleaned = clean_markdown_for_extract(text or "").replace("[... middle omitted ...]", " ")
    candidates = re.split(r"(?<=[。.!?！？])\s+|\n{2,}", cleaned)
    signals: list[str] = []
    for candidate in candidates:
        sentence = normalize_space(re.sub(r"^#+\s*", "", candidate))
        if len(sentence) < 24 or sentence.startswith("!") or sentence.startswith("["):
            continue
        if sentence in signals:
            continue
        if len(sentence) > max_chars:
            sentence = sentence[:max_chars].rstrip() + "..."
        signals.append(sentence)
        if len(signals) >= limit:
            break
    return signals


def report_signal_fallback(report: dict[str, Any], max_chars: int = 180) -> list[str]:
    signals = signal_sentences(
        report.get("extract") or report.get("digest") or "",
        limit=4,
        max_chars=max_chars,
    )
    title = normalize_space(str(report.get("title") or ""))
    return [signal for signal in signals if signal != title and not title.startswith(signal)]


def report_view_fallback(report: dict[str, Any]) -> dict[str, Any]:
    signals = report_signal_fallback(report)
    return {
        "bank": bank_alias(report),
        "view": signals[0] if signals else "该报告提供了一条需要纳入本节判断的新增市场信号。",
        "data_points": signals[1:3],
        "marginal_change": "",
        "report_ids": [report["id"]],
    }


def heuristic_bank_plan(reports: list[dict[str, Any]], max_reports_per_section: int = 12) -> list[dict[str, Any]]:
    grouped: dict[str, list[str]] = {}
    for report in reports:
        grouped.setdefault(bank_category_for(report), []).append(report["id"])
    plan: list[dict[str, Any]] = []
    for heading, report_ids in grouped.items():
        chunks = [report_ids[index:index + max_reports_per_section] for index in range(0, len(report_ids), max_reports_per_section)]
        for index, chunk in enumerate(chunks, 1):
            chunk_heading = heading if len(chunks) == 1 else f"{heading}（{index}）"
            plan.append({"heading": chunk_heading, "report_ids": chunk})
    return plan


def normalize_bank_plan(
    raw_plan: dict[str, Any],
    reports: list[dict[str, Any]],
    max_reports_per_section: int = 12,
) -> list[dict[str, Any]]:
    valid_ids = {report["id"] for report in reports}
    assigned: set[str] = set()
    normalized: list[dict[str, Any]] = []
    raw_categories = raw_plan.get("categories") if isinstance(raw_plan, dict) else []
    for raw_category in raw_categories or []:
        if not isinstance(raw_category, dict):
            continue
        heading = normalize_space(raw_category.get("heading") or "未命名主题")
        report_ids: list[str] = []
        for report_id in raw_category.get("report_ids") or []:
            rid = str(report_id)
            if rid in valid_ids and rid not in assigned:
                report_ids.append(rid)
                assigned.add(rid)
        if not report_ids:
            continue
        chunks = [report_ids[index:index + max_reports_per_section] for index in range(0, len(report_ids), max_reports_per_section)]
        for index, chunk in enumerate(chunks, 1):
            chunk_heading = heading if len(chunks) == 1 else f"{heading}（{index}）"
            normalized.append({"heading": chunk_heading, "report_ids": chunk})

    missing_reports = [report for report in reports if report["id"] not in assigned]
    normalized.extend(heuristic_bank_plan(missing_reports, max_reports_per_section=max_reports_per_section))
    return normalized or heuristic_bank_plan(reports, max_reports_per_section=max_reports_per_section)


def bank_plan_prompt(reports: list[dict[str, Any]]) -> str:
    target_sections = max(4, min(14, (len(reports) + 7) // 8))
    inventory = [
        {"id": report["id"], "bank": bank_alias(report), "title": report.get("title") or ""}
        for report in reports
    ]
    return f"""
请只根据下面的投行报告清单，为今日 Market Views 规划动态目录。

硬性要求：
1. 目标约 {target_sections} 个类别，通常每类 5-12 篇；类别数量随当天内容调整。
2. 每个报告 ID 必须且只能出现一次，不能遗漏，不能重复。
3. 类别按资产、市场或产业主题命名，例如宏观、利率、FX、Equity、科技、能源、消费、医疗、区域市场；不要按投行名称分类。
4. 避免一个笼统的“其他”吞掉大量报告；相关性弱时拆成更清楚的行业或市场类别。
5. 只做目录规划，不写摘要，不引用文件名。

输出 JSON：
{{"categories":[{{"heading":"主题名称","report_ids":["R001","R002"]}}]}}

投行报告清单：
{json.dumps(inventory, ensure_ascii=False, indent=2)}
""".strip()


def section_figure_candidates(
    figures: list[dict[str, Any]],
    report_ids: list[str],
    max_candidates: int,
) -> list[dict[str, Any]]:
    report_id_set = set(report_ids)
    by_report: dict[str, list[dict[str, Any]]] = {report_id: [] for report_id in report_ids}
    for figure in figures:
        report_id = str(figure.get("report_id") or "")
        if report_id not in report_id_set or figure.get("figure_type") == "external_card":
            continue
        if len(by_report[report_id]) >= 4:
            continue
        by_report[report_id].append({
            "figure_id": figure.get("figure_id"),
            "report_id": report_id,
            "label": figure.get("label"),
            "context": trim_text(str(figure.get("context") or ""), 260),
        })
    payload: list[dict[str, Any]] = []
    for depth in range(4):
        for report_id in report_ids:
            candidates = by_report.get(report_id) or []
            if depth >= len(candidates):
                continue
            payload.append(candidates[depth])
            if max_candidates > 0 and len(payload) >= max_candidates:
                return payload
    return payload


def bank_section_prompt(
    heading: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
) -> str:
    report_payload = [
        {
            "id": report["id"],
            "bank": bank_alias(report),
            "title": report.get("title") or "",
            "digest": trim_text(report.get("digest") or "", args.per_report_prompt_chars),
        }
        for report in reports
    ]
    report_ids = [report["id"] for report in reports]
    figure_payload = section_figure_candidates(
        figures,
        report_ids,
        getattr(args, "max_section_figure_candidates", 40),
    )
    return f"""
你正在撰写 Market Views 的投行主体栏目“{heading}”。输入只有本栏目相关报告，必须做系统汇编。

硬性要求：
1. 先给 3-5 条主流共识、2-4 条分歧或条件差异，再给“机构观点”。
2. bank_views 是正文内容，不是报告目录。可以把同一投行、同一子主题的多篇报告合并成一条，但每条要写成 100-220 字的完整判断，保留方向、机制、数字和边际变化。
3. 输入中的每个报告 ID 必须出现在某条 bank_view.report_ids 中；只放进 references 不算覆盖。不得漏掉任何 ID。
4. 同一条 bank_view 不要混合不同投行。投行名称使用 GS、JPM、MS、BofA、Citi、UBS、DB、NOM 等缩写。
5. data_points 提炼 4-10 条最有辨识度的数字或事实，不能写空泛结论；marginal_change 说明相对旧叙事的新变化。
6. 从候选中选择最多 {getattr(args, 'figures_per_bank_section', 4)} 张真正支撑观点的原始报告图；优先来自不同报告。没有合适图可以少选，禁止编造 figure_id。
7. 不写买卖评级，不写逐篇报告标题，不输出文件名，不做纯翻译堆叠。
8. references 必须列出本栏目全部输入 ID，供程序校验，但这些 ID 不会在 PDF 正文显示。

输出 JSON：
{{"heading":"可优化的栏目标题","thesis":"本栏目的核心判断","consensus":["共识1"],"divergences":["分歧1"],"bank_views":[{{"bank":"JPM","view":"整合后的机构判断","data_points":["关键数字"],"marginal_change":"边际变化","report_ids":["R001"]}}],"data_points":["跨报告关键数字"],"figure_ids":["F001"],"references":{json.dumps(report_ids, ensure_ascii=False)}}}

报告摘要：
{json.dumps(report_payload, ensure_ascii=False, indent=2)}

本栏目可选图表：
{json.dumps(figure_payload, ensure_ascii=False, indent=2)}
""".strip()


def select_section_figures(
    requested_ids: list[Any],
    report_ids: list[str],
    figures: list[dict[str, Any]],
    limit: int,
) -> list[str]:
    if limit <= 0:
        return []
    report_id_set = set(report_ids)
    figures_by_id = {str(figure.get("figure_id") or ""): figure for figure in figures}
    selected: list[str] = []
    selected_reports: set[str] = set()
    for requested_id in requested_ids:
        figure_id = str(requested_id)
        figure = figures_by_id.get(figure_id)
        if not figure or str(figure.get("report_id") or "") not in report_id_set:
            continue
        if figure_id not in selected:
            selected.append(figure_id)
            selected_reports.add(str(figure.get("report_id") or ""))
        if len(selected) >= limit:
            return selected

    for distinct_only in (True, False):
        for figure in figures:
            report_id = str(figure.get("report_id") or "")
            figure_id = str(figure.get("figure_id") or "")
            if report_id not in report_id_set or not figure_id or figure_id in selected:
                continue
            if distinct_only and report_id in selected_reports:
                continue
            selected.append(figure_id)
            selected_reports.add(report_id)
            if len(selected) >= limit:
                return selected
    return selected


def clean_string_list(value: Any, limit: int) -> list[str]:
    if not isinstance(value, list):
        return []
    cleaned = [normalize_space(str(item)) for item in value if normalize_space(str(item))]
    return cleaned[:limit]


def normalize_bank_section(
    raw_section: dict[str, Any],
    planned_heading: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    figure_limit: int,
) -> dict[str, Any]:
    reports_by_id = {report["id"]: report for report in reports}
    valid_ids = set(reports_by_id)
    bank_views: list[dict[str, Any]] = []
    covered: set[str] = set()
    raw_views = (raw_section.get("bank_views") or raw_section.get("views") or []) if isinstance(raw_section, dict) else []
    for raw_view in raw_views:
        if not isinstance(raw_view, dict):
            continue
        raw_ids = raw_view.get("report_ids") or ([raw_view.get("report_id")] if raw_view.get("report_id") else [])
        report_ids = [
            str(report_id)
            for report_id in raw_ids
            if str(report_id) in valid_ids and str(report_id) not in covered
        ]
        if not report_ids:
            continue
        by_bank: dict[str, list[str]] = {}
        for report_id in report_ids:
            by_bank.setdefault(bank_alias(reports_by_id[report_id]), []).append(report_id)
        for bank, bank_report_ids in by_bank.items():
            view = normalize_space(str(raw_view.get("view") or raw_view.get("summary") or ""))
            if not view:
                view = report_view_fallback(reports_by_id[bank_report_ids[0]])["view"]
            bank_views.append({
                "bank": bank,
                "view": view,
                "data_points": clean_string_list(raw_view.get("data_points") or [], 4),
                "marginal_change": normalize_space(str(raw_view.get("marginal_change") or "")),
                "report_ids": bank_report_ids,
            })
            covered.update(bank_report_ids)

    for report in reports:
        if report["id"] not in covered:
            bank_views.append(report_view_fallback(report))
            covered.add(report["id"])

    report_ids = [report["id"] for report in reports]
    requested_figures = (raw_section.get("figure_ids") or []) if isinstance(raw_section, dict) else []
    figure_ids = select_section_figures(requested_figures, report_ids, figures, figure_limit)
    consensus = clean_string_list(
        raw_section.get("consensus") or raw_section.get("bullets") or [],
        6,
    ) if isinstance(raw_section, dict) else []
    if not consensus:
        consensus = [view["view"] for view in bank_views[:3]]
    thesis = normalize_space(str(raw_section.get("thesis") or "")) if isinstance(raw_section, dict) else ""
    return {
        "heading": normalize_space(str(raw_section.get("heading") or planned_heading)) if isinstance(raw_section, dict) else planned_heading,
        "thesis": thesis or "本节按机构观点、关键数据和边际变化汇总今日新增投行研究。",
        "consensus": consensus,
        "divergences": clean_string_list(raw_section.get("divergences") or [], 5) if isinstance(raw_section, dict) else [],
        "bank_views": bank_views,
        "data_points": clean_string_list(raw_section.get("data_points") or [], 10) if isinstance(raw_section, dict) else [],
        "figure_ids": figure_ids,
        "references": report_ids,
    }


def build_fallback_bank_roundup(reports: list[dict[str, Any]], figures: list[dict[str, Any]]) -> dict[str, Any]:
    reports_by_id = {report["id"]: report for report in reports}
    sections = []
    for planned in heuristic_bank_plan(reports):
        section_reports = [reports_by_id[report_id] for report_id in planned["report_ids"]]
        sections.append(normalize_bank_section({}, planned["heading"], section_reports, figures, figure_limit=4))
    return {
        "title": "全球投行叙事汇编",
        "summary": f"今日纳入 {len(reports)} 篇投行/券商研究，按 {len(sections)} 个市场与产业主题系统整理。",
        "sections": sections,
    }


def fallback_theme_for_reports(
    heading: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    max_bullets: int = 8,
) -> dict[str, Any]:
    refs = [r["id"] for r in reports]
    bullet_limit = len(reports) if max_bullets <= 0 else max_bullets
    bullets = [
        (report_signal_fallback(report, max_chars=140) or ["该报告提供了一条需要纳入本主题判断的新增信号。"])[0]
        for report in reports[:bullet_limit]
    ]
    figure_ids: list[str] = []
    for report in reports:
        for fig_id in figure_ids_for_report(figures, report["id"], limit=1):
            if fig_id not in figure_ids:
                figure_ids.append(fig_id)
            if len(figure_ids) >= 2:
                break
        if len(figure_ids) >= 2:
            break
    return {
        "heading": heading,
        "thesis": relevance_for_category(heading) if reports and reports[0].get("source_group") != "bank_research" else "用于观察该来源今日最集中的市场叙事与数据边际变化。",
        "bullets": bullets or ["今日该主题没有足够文本形成独立要点。"],
        "figure_ids": figure_ids,
        "references": refs,
    }


def build_source_roundup_for_group(
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    source_group: str,
    max_themes: int = 4,
) -> dict[str, Any]:
    label = source_group_label(source_group)
    if not reports:
        return {
            "source_group": source_group,
            "title": label,
            "summary": "今日暂无新增报告。",
            "themes": [],
        }

    grouped: dict[str, list[dict[str, Any]]] = {}
    for report in reports:
        grouped.setdefault(report_category_for(report), []).append(report)

    ordered_groups = sorted(grouped.items(), key=lambda item: (-len(item[1]), item[0]))
    primary = ordered_groups[:max_themes]
    overflow = ordered_groups[max_themes:]
    if overflow:
        overflow_reports = [report for _, items in overflow for report in items]
        primary.append(("其他边际信号", overflow_reports))

    themes = [fallback_theme_for_reports(heading, items, figures, max_bullets=len(items)) for heading, items in primary if items]
    total_refs = sum(len(theme.get("references") or []) for theme in themes)
    summary = f"今日纳入 {len(reports)} 篇，压缩为 {len(themes)} 个主题、{total_refs} 个引用点，重点看叙事和数据边际变化。"
    return {
        "source_group": source_group,
        "title": label,
        "summary": summary,
        "themes": themes,
    }


def build_source_roundups(reports: list[dict[str, Any]], figures: list[dict[str, Any]]) -> list[dict[str, Any]]:
    return [
        build_source_roundup_for_group(
            source_group_reports(reports, source_group),
            figures,
            source_group,
            max_themes=12 if source_group == "bank_research" else 3,
        )
        for source_group in ROUNDUP_SOURCE_ORDER
    ]


def collect_roundup_references(source_roundup: dict[str, Any]) -> set[str]:
    refs: set[str] = set()
    for theme in source_roundup.get("themes") or []:
        if not isinstance(theme, dict):
            continue
        for ref in theme.get("references") or []:
            refs.add(str(ref))
    return refs


def normalize_source_roundup(
    raw_roundup: dict[str, Any],
    reports_by_id: dict[str, dict[str, Any]],
    figures_by_id: dict[str, dict[str, Any]],
    source_group: str,
) -> dict[str, Any]:
    label = source_group_label(source_group)
    source_report_ids = [rid for rid, report in reports_by_id.items() if report.get("source_group") == source_group]
    source_id_set = set(source_report_ids)
    themes: list[dict[str, Any]] = []
    if isinstance(raw_roundup, dict):
        for raw_theme in raw_roundup.get("themes") or raw_roundup.get("sections") or []:
            if not isinstance(raw_theme, dict):
                continue
            refs = [str(ref) for ref in (raw_theme.get("references") or []) if str(ref) in source_id_set]
            if not refs:
                continue
            fig_ids = [str(fig_id) for fig_id in (raw_theme.get("figure_ids") or []) if str(fig_id) in figures_by_id]
            bullets = [normalize_space(b) for b in (raw_theme.get("bullets") or []) if normalize_space(b)]
            themes.append({
                "heading": normalize_space(raw_theme.get("heading") or "未命名主题"),
                "thesis": normalize_space(raw_theme.get("thesis") or ""),
                "bullets": bullets[:6],
                "figure_ids": fig_ids[:3],
                "references": refs,
            })

    if not themes and source_report_ids:
        return build_source_roundup_for_group([reports_by_id[rid] for rid in source_report_ids], list(figures_by_id.values()), source_group)

    roundup = {
        "source_group": source_group,
        "title": normalize_space((raw_roundup or {}).get("title") or label) if isinstance(raw_roundup, dict) else label,
        "summary": normalize_space((raw_roundup or {}).get("summary") or "") if isinstance(raw_roundup, dict) else "",
        "themes": themes,
    }
    if not source_report_ids:
        roundup["summary"] = "今日暂无新增报告。"
        return roundup

    referenced = collect_roundup_references(roundup)
    missing = [rid for rid in source_report_ids if rid not in referenced]
    if missing:
        missing_reports = [reports_by_id[rid] for rid in missing]
        fallback = build_source_roundup_for_group(
            missing_reports,
            list(figures_by_id.values()),
            source_group,
            max_themes=12 if source_group == "bank_research" else 3,
        )
        roundup["themes"].extend(fallback["themes"])

    if not roundup["summary"]:
        total_refs = len(collect_roundup_references(roundup))
        roundup["summary"] = f"今日纳入 {len(source_report_ids)} 篇，整合为 {len(roundup['themes'])} 个主题、{total_refs} 个引用点。"
    return roundup


def enrich_source_roundups(
    summary: dict[str, Any],
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
) -> dict[str, Any]:
    reports_by_id = {r["id"]: r for r in reports}
    figures_by_id = {f["figure_id"]: f for f in figures}
    raw_roundups = summary.get("source_roundups")
    raw_by_group: dict[str, dict[str, Any]] = {}
    if isinstance(raw_roundups, list):
        for raw in raw_roundups:
            if not isinstance(raw, dict):
                continue
            group = str(raw.get("source_group") or "")
            if group in ROUNDUP_SOURCE_ORDER and group not in raw_by_group:
                raw_by_group[group] = raw

    source_roundups = [
        normalize_source_roundup(raw_by_group.get(group, {}), reports_by_id, figures_by_id, group)
        for group in ROUNDUP_SOURCE_ORDER
    ]
    summary["source_roundups"] = source_roundups
    summary.pop("sections", None)
    summary.pop("external_roundup", None)
    return summary


def request_model_json(
    prompt: str,
    args: argparse.Namespace,
    label: str,
    raw_path: Path,
) -> dict[str, Any]:
    raw = call_deepseek(prompt, args, label)
    raw_path.write_text(raw, encoding="utf-8")
    parsed = extract_json(raw)
    if not isinstance(parsed, dict):
        raise ValueError(f"{label}: expected a JSON object")
    return parsed


def generate_bank_roundup(
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
    out_dir: Path,
    use_model: bool,
) -> dict[str, Any]:
    if not reports:
        return {"title": "全球投行叙事汇编", "summary": "今日暂无新增投行研究。", "sections": []}

    raw_plan: dict[str, Any] = {}
    if use_model:
        try:
            raw_plan = request_model_json(
                bank_plan_prompt(reports),
                args,
                "bank category plan",
                out_dir / "deepseek_bank_category_plan_raw.json",
            )
        except Exception as exc:
            log(f"DeepSeek bank category plan failed; using heuristic plan: {exc}")
            (out_dir / "deepseek_bank_category_plan_error.txt").write_text(str(exc), encoding="utf-8")

    plan = normalize_bank_plan(
        raw_plan,
        reports,
        max_reports_per_section=getattr(args, "max_reports_per_bank_section", 12),
    )
    (out_dir / "bank_category_plan.json").write_text(json.dumps(plan, ensure_ascii=False, indent=2), encoding="utf-8")
    reports_by_id = {report["id"]: report for report in reports}
    sections: list[dict[str, Any]] = []
    for index, planned in enumerate(plan, 1):
        section_reports = [reports_by_id[report_id] for report_id in planned["report_ids"]]
        raw_section: dict[str, Any] = {}
        if use_model:
            try:
                raw_section = request_model_json(
                    bank_section_prompt(planned["heading"], section_reports, figures, args),
                    args,
                    f"bank section {index}/{len(plan)}",
                    out_dir / f"deepseek_bank_section_{index:02d}_raw.json",
                )
            except Exception as exc:
                log(f"DeepSeek bank section {index} failed; using content fallback: {exc}")
                (out_dir / f"deepseek_bank_section_{index:02d}_error.txt").write_text(str(exc), encoding="utf-8")
        section = normalize_bank_section(
            raw_section,
            planned["heading"],
            section_reports,
            figures,
            figure_limit=getattr(args, "figures_per_bank_section", 4),
        )
        sections.append(section)
        content_ids = {
            report_id
            for view in section.get("bank_views") or []
            for report_id in view.get("report_ids") or []
        }
        log(
            f"Bank section {index}/{len(plan)}: {section['heading']} | "
            f"reports={len(section_reports)} content_covered={len(content_ids)} figures={len(section['figure_ids'])}"
        )

    return {
        "title": "全球投行叙事汇编",
        "summary": f"今日纳入 {len(reports)} 篇投行/券商研究，按 {len(sections)} 个市场、资产与产业主题系统整理。",
        "sections": sections,
    }


def supporting_roundup_prompt(
    source_group: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
) -> str:
    label = source_group_label(source_group)
    report_payload = [
        {
            "id": report["id"],
            "institution": report.get("institution_name") or label,
            "title": report.get("title") or "",
            "digest": trim_text(report.get("digest") or "", min(args.per_report_prompt_chars, 1800)),
        }
        for report in reports
    ]
    figure_payload = section_figure_candidates(
        figures,
        [report["id"] for report in reports],
        max_candidates=16,
    )
    return f"""
请把下面的“{label}”新增研究整理成 Market Views 的独立辅助板块。它不能与投行主体混写，也不需要和投行板块等长。

要求：
1. 按当天内容归纳 1-3 个 themes，每个 theme 写 3-5 条完整要点，保留数据、政策含义和边际变化。
2. 每篇输入报告都必须在某个 theme 中得到实质整合，并列入该 theme.references；不能只把 ID 堆到最后。
3. 这是辅助信号，只写对宏观、产业、企业战略或资产叙事有帮助的部分，不做逐篇翻译。
4. 每个 theme 最多选 2 张原始报告图表，不要输出文件名。

输出 JSON：
{{"source_group":"{source_group}","title":"{label}","summary":"本板块摘要","themes":[{{"heading":"主题","thesis":"核心含义","bullets":["要点"],"figure_ids":["F001"],"references":["R001"]}}]}}

报告摘要：
{json.dumps(report_payload, ensure_ascii=False, indent=2)}

可选图表：
{json.dumps(figure_payload, ensure_ascii=False, indent=2)}
""".strip()


def generate_supporting_roundup(
    source_group: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
    out_dir: Path,
    use_model: bool,
) -> dict[str, Any]:
    raw_roundup: dict[str, Any] = {}
    if reports and use_model:
        try:
            raw_roundup = request_model_json(
                supporting_roundup_prompt(source_group, reports, figures, args),
                args,
                f"supporting roundup {source_group}",
                out_dir / f"deepseek_support_{source_group}_raw.json",
            )
        except Exception as exc:
            log(f"DeepSeek supporting roundup {source_group} failed; using fallback: {exc}")
            (out_dir / f"deepseek_support_{source_group}_error.txt").write_text(str(exc), encoding="utf-8")

    reports_by_id = {report["id"]: report for report in reports}
    figures_by_id = {figure["figure_id"]: figure for figure in figures}
    return normalize_source_roundup(raw_roundup, reports_by_id, figures_by_id, source_group)


def overview_prompt(bank_roundup: dict[str, Any], supporting_roundups: list[dict[str, Any]], reports: list[dict[str, Any]]) -> str:
    section_payload = [
        {
            "heading": section.get("heading"),
            "thesis": section.get("thesis"),
            "consensus": (section.get("consensus") or [])[:4],
            "divergences": (section.get("divergences") or [])[:3],
            "report_count": len(section.get("references") or []),
        }
        for section in bank_roundup.get("sections") or []
    ]
    supporting_payload = [
        {
            "title": roundup.get("title"),
            "summary": roundup.get("summary"),
            "themes": [theme.get("heading") for theme in roundup.get("themes") or []],
        }
        for roundup in supporting_roundups
    ]
    bank_count = sum(1 for report in reports if report.get("source_group") == "bank_research")
    return f"""
请为今日 Market Views 写封面信息和一页摘要。投行叙事是绝对主体，咨询与国际机构只作为辅助校准。

要求：
1. executive_summary 写 6-8 条，每条必须指出主流叙事、关键数据或分歧，不写编辑流程和覆盖说明。
2. subtitle 一句话概括今天最重要的跨主题变化。
3. closing 说明后续需要验证的数据或叙事节点，不给投资建议。
4. 不引用报告 ID、文件名或标题清单。

输出 JSON：
{{"title":"Market Views｜全球投行叙事汇编","subtitle":"今日主线","executive_summary":["要点"],"closing":"收束"}}

投行报告数：{bank_count}
投行板块：
{json.dumps(section_payload, ensure_ascii=False, indent=2)}

辅助板块：
{json.dumps(supporting_payload, ensure_ascii=False, indent=2)}
""".strip()


def compose_market_summary(
    bank_roundup: dict[str, Any],
    supporting_roundups: list[dict[str, Any]],
    reports: list[dict[str, Any]],
    overview: dict[str, Any] | None = None,
) -> dict[str, Any]:
    overview = overview or {}
    bank_count = sum(1 for report in reports if report.get("source_group") == "bank_research")
    consulting_count = sum(1 for report in reports if report.get("source_group") == "consulting")
    institution_count = sum(1 for report in reports if report.get("source_group") == "institution")
    executive_summary = clean_string_list(overview.get("executive_summary") or [], 8)
    if not executive_summary:
        for section in bank_roundup.get("sections") or []:
            points = section.get("consensus") or []
            if points:
                executive_summary.append(normalize_space(str(points[0])))
            if len(executive_summary) >= 6:
                break
    if not executive_summary:
        executive_summary = ["今日投行研究按宏观、资产、区域与产业主题分组整理，正文逐篇落实到机构观点。"]

    content_covered = {
        str(report_id)
        for section in bank_roundup.get("sections") or []
        for view in section.get("bank_views") or []
        for report_id in view.get("report_ids") or []
    }
    return {
        "schema_version": 2,
        "title": normalize_space(str(overview.get("title") or "Market Views｜全球投行叙事汇编")),
        "subtitle": normalize_space(str(overview.get("subtitle") or f"今日以 {bank_count} 篇投行研究为主体，观察全球市场叙事与数据的边际变化。")),
        "executive_summary": executive_summary,
        "bank_roundup": bank_roundup,
        "supporting_roundups": supporting_roundups,
        "coverage": {
            "bank_reports": bank_count,
            "bank_content_covered": len(content_covered),
            "consulting_reports": consulting_count,
            "institution_reports": institution_count,
        },
        "closing": normalize_space(str(overview.get("closing") or "后续重点是跟踪关键数据能否继续验证今日形成的共识与分歧。")),
    }


def build_market_summary(
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    args: argparse.Namespace,
    out_dir: Path,
) -> dict[str, Any]:
    use_model = bool(os.getenv("DEEPSEEK_API_KEY"))
    if not use_model:
        log("DEEPSEEK_API_KEY is missing; building deterministic content fallback without model calls.")
    bank_reports = source_group_reports(reports, "bank_research")
    bank_roundup = generate_bank_roundup(bank_reports, figures, args, out_dir, use_model)
    supporting_roundups = [
        generate_supporting_roundup(
            source_group,
            source_group_reports(reports, source_group),
            figures,
            args,
            out_dir,
            use_model,
        )
        for source_group in ("consulting", "institution")
    ]

    overview: dict[str, Any] = {}
    if use_model:
        try:
            overview = request_model_json(
                overview_prompt(bank_roundup, supporting_roundups, reports),
                args,
                "market views overview",
                out_dir / "deepseek_market_overview_raw.json",
            )
        except Exception as exc:
            log(f"DeepSeek market overview failed; using section-derived summary: {exc}")
            (out_dir / "deepseek_market_overview_error.txt").write_text(str(exc), encoding="utf-8")
    return compose_market_summary(bank_roundup, supporting_roundups, reports, overview)


def build_external_roundup(
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    max_items: int = 24,
) -> dict[str, Any]:
    external_reports = [r for r in reports if r.get("source_group") in EXTERNAL_SOURCE_GROUPS]
    categories: dict[str, list[dict[str, Any]]] = {}
    for report in external_reports[:max_items]:
        category = external_category_for(report)
        categories.setdefault(category, []).append({
            "report_id": report["id"],
            "institution": report.get("institution_name") or report.get("source_label") or "",
            "title": report.get("title") or "",
            "signal": first_signal(report.get("extract") or report.get("digest") or ""),
            "market_relevance": relevance_for_category(category),
            "figure_ids": figure_ids_for_report(figures, report["id"], limit=1),
        })
    return {
        "title": "外部机构与咨询信号",
        "summary": "这些来源用于补充投行观点之外的政策、地缘、产业和长期结构变量。",
        "categories": [{"heading": heading, "items": items} for heading, items in categories.items()],
    }


def enrich_external_roundup(
    summary: dict[str, Any],
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    max_items: int,
) -> dict[str, Any]:
    external_reports = {r["id"]: r for r in reports if r.get("source_group") in EXTERNAL_SOURCE_GROUPS}
    if not external_reports:
        summary["external_roundup"] = {"title": "外部机构与咨询信号", "summary": "", "categories": []}
        return summary

    roundup = summary.get("external_roundup")
    if not isinstance(roundup, dict) or not isinstance(roundup.get("categories"), list) or not roundup.get("categories"):
        summary["external_roundup"] = build_external_roundup(reports, figures, max_items=max_items)
        return summary

    normalized_categories: list[dict[str, Any]] = []
    item_count = 0
    for category in roundup.get("categories") or []:
        if not isinstance(category, dict):
            continue
        heading = normalize_space(category.get("heading") or "外部研究补充")
        items: list[dict[str, Any]] = []
        for raw_item in category.get("items") or []:
            if not isinstance(raw_item, dict) or item_count >= max_items:
                continue
            rid = str(raw_item.get("report_id") or raw_item.get("ref_id") or raw_item.get("id") or "")
            report = external_reports.get(rid)
            if not report:
                continue
            fig_ids = [str(fid) for fid in (raw_item.get("figure_ids") or []) if str(fid)]
            if not fig_ids:
                fig_ids = figure_ids_for_report(figures, rid, limit=1)
            items.append({
                "report_id": rid,
                "institution": normalize_space(raw_item.get("institution") or report.get("institution_name") or report.get("source_label") or ""),
                "title": normalize_space(raw_item.get("title") or report.get("title") or ""),
                "signal": normalize_space(raw_item.get("signal") or first_signal(report.get("digest") or "")),
                "market_relevance": normalize_space(raw_item.get("market_relevance") or relevance_for_category(heading)),
                "figure_ids": fig_ids[:2],
            })
            item_count += 1
        if items:
            normalized_categories.append({"heading": heading, "items": items})

    if not normalized_categories:
        summary["external_roundup"] = build_external_roundup(reports, figures, max_items=max_items)
        return summary
    summary["external_roundup"] = {
        "title": normalize_space(roundup.get("title") or "外部机构与咨询信号"),
        "summary": normalize_space(roundup.get("summary") or "这些来源用于补充投行观点之外的政策、地缘、产业和长期结构变量。"),
        "categories": normalized_categories,
    }
    return summary


def report_section_map(summary: dict[str, Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for section in summary.get("sections", []) or []:
        heading = str(section.get("heading") or "未归类")
        for ref_id in section.get("references", []) or []:
            mapping.setdefault(str(ref_id), [])
            if heading not in mapping[str(ref_id)]:
                mapping[str(ref_id)].append(heading)
    return mapping


def source_roundup_map(summary: dict[str, Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for roundup in summary.get("source_roundups", []) or []:
        if not isinstance(roundup, dict):
            continue
        source_title = str(roundup.get("title") or source_group_label(roundup.get("source_group", "")))
        for theme in roundup.get("themes") or []:
            if not isinstance(theme, dict):
                continue
            heading = str(theme.get("heading") or "未归类")
            label = f"{source_title} / {heading}"
            for ref_id in theme.get("references") or []:
                rid = str(ref_id)
                mapping.setdefault(rid, [])
                if label not in mapping[rid]:
                    mapping[rid].append(label)
    return mapping


def render_latex(summary: dict[str, Any], reports_by_id: dict[str, dict[str, Any]], figures_by_id: dict[str, dict[str, Any]], report_date: str) -> str:
    title = summary.get("title") or "市场最新观点汇总"
    subtitle = summary.get("subtitle") or "Daily market views roundup"
    lines: list[str] = []
    lines += [r"\documentclass[11pt]{ctexart}", r"\usepackage[a4paper,margin=1in]{geometry}", r"\usepackage{graphicx}", r"\usepackage{xcolor}", r"\usepackage{hyperref}", r"\definecolor{refgray}{gray}{0.45}", r"\title{\textbf{" + latex_escape(title) + r"}\\[0.4em]{\large " + latex_escape(subtitle) + r"}}", r"\author{KC桌面 自动生成}", r"\date{" + latex_escape(report_date) + r"}", r"\begin{document}", r"\maketitle", r"\tableofcontents", r"\newpage", r"\section{一页摘要}", r"\begin{itemize}"]
    for item in summary.get("executive_summary", []):
        lines.append(r"  \item " + latex_escape(item))
    lines.append(r"\end{itemize}")

    bank_roundup = summary.get("bank_roundup") or build_fallback_bank_roundup(
        [report for report in reports_by_id.values() if report.get("source_group") == "bank_research"],
        list(figures_by_id.values()),
    )
    lines.append(r"\section{" + latex_escape(bank_roundup.get("title") or "全球投行叙事汇编") + r"}")
    if bank_roundup.get("summary"):
        lines.append(latex_escape(bank_roundup.get("summary")))
    for section in bank_roundup.get("sections") or []:
        lines.append(r"\newpage")
        lines.append(r"\subsection{" + latex_escape(section.get("heading") or "投行市场主线") + r"}")
        if section.get("thesis"):
            lines.append(r"\textbf{" + latex_escape(section.get("thesis")) + r"}")
        for label, key in (("主流共识", "consensus"), ("分歧与条件差异", "divergences")):
            values = section.get(key) or []
            if not values:
                continue
            lines += [r"\subsubsection*{" + label + r"}", r"\begin{itemize}"]
            lines.extend(r"  \item " + latex_escape(value) for value in values)
            lines.append(r"\end{itemize}")
        lines.append(r"\subsubsection*{机构观点}")
        for view in section.get("bank_views") or []:
            lines.append(r"\paragraph{" + latex_escape(view.get("bank") or "投行") + r"} " + latex_escape(view.get("view") or ""))
            for data_point in view.get("data_points") or []:
                lines.append(r"{\small\color{refgray}数据：" + latex_escape(data_point) + r"\par}")
            if view.get("marginal_change"):
                lines.append(r"{\small\color{refgray}边际变化：" + latex_escape(view.get("marginal_change")) + r"\par}")
        if section.get("data_points"):
            lines += [r"\subsubsection*{关键数据}", r"\begin{itemize}"]
            lines.extend(r"  \item " + latex_escape(value) for value in section.get("data_points") or [])
            lines.append(r"\end{itemize}")
        for fig_id in (section.get("figure_ids") or [])[:4]:
            fig = figures_by_id.get(str(fig_id))
            if not fig:
                continue
            lines += [r"\begin{figure}[htbp]", r"\centering", r"\includegraphics[width=0.88\linewidth]{" + fig["latex_path"] + r"}", r"\caption{" + latex_escape(f"{fig.get('label', 'Figure')} - {fig.get('context', '')}") + r"}", r"\end{figure}"]
        report_names = []
        for report_id in section.get("references") or []:
            report = reports_by_id.get(str(report_id))
            if not report:
                continue
            name = bank_alias(report)
            if name not in report_names:
                report_names.append(name)
        lines.append(r"{\small\color{refgray}" + latex_escape(f"本节综合 {len(section.get('references') or [])} 篇研究；涉及 {'、'.join(report_names)}。") + r"}")

    for roundup in summary.get("supporting_roundups") or []:
        lines.append(r"\newpage")
        lines.append(r"\section{" + latex_escape("辅助信号｜" + str(roundup.get("title") or source_group_label(roundup.get("source_group", "")))) + r"}")
        if roundup.get("summary"):
            lines.append(latex_escape(roundup.get("summary")))
        for theme in roundup.get("themes") or []:
            lines.append(r"\subsection{" + latex_escape(theme.get("heading") or "辅助研究主题") + r"}")
            if theme.get("thesis"):
                lines.append(r"\textbf{" + latex_escape(theme.get("thesis")) + r"}")
            if theme.get("bullets"):
                lines.append(r"\begin{itemize}")
                lines.extend(r"  \item " + latex_escape(value) for value in theme.get("bullets") or [])
                lines.append(r"\end{itemize}")
            for fig_id in (theme.get("figure_ids") or [])[:2]:
                fig = figures_by_id.get(str(fig_id))
                if not fig:
                    continue
                lines += [r"\begin{figure}[htbp]", r"\centering", r"\includegraphics[width=0.88\linewidth]{" + fig["latex_path"] + r"}", r"\caption{" + latex_escape(f"{fig.get('label', 'Figure')} - {fig.get('context', '')}") + r"}", r"\end{figure}"]
    if summary.get("closing"):
        lines += [r"\section{结语}", latex_escape(summary.get("closing"))]
    source_counts = {group: sum(1 for report in reports_by_id.values() if report.get("source_group") == group) for group in ROUNDUP_SOURCE_ORDER}
    bank_counts: dict[str, int] = {}
    for report in reports_by_id.values():
        if report.get("source_group") != "bank_research":
            continue
        name = bank_alias(report)
        bank_counts[name] = bank_counts.get(name, 0) + 1
    bank_mix = " / ".join(f"{name} {count}篇" for name, count in sorted(bank_counts.items(), key=lambda item: (-item[1], item[0])))
    lines += [
        r"\newpage",
        r"\section{覆盖概览}",
        latex_escape(f"投行/券商 {source_counts['bank_research']} 篇；战略咨询 {source_counts['consulting']} 篇；智库/国际机构 {source_counts['institution']} 篇。") + r"\par",
        latex_escape("投行覆盖：" + bank_mix) + r"\par",
        r"\section{Disclaimer}",
        r"{\scriptsize\color{refgray}",
    ]
    for para in DISCLAIMER_TEXT.split("\n\n"):
        lines.append(latex_escape(para) + r"\par")
    lines += [
        r"}",
        r"\newpage",
        r"\begin{center}",
        r"{\Large 更多详情报告kcdesk.com}\par\vspace{0.8cm}",
        r"\includegraphics[width=0.58\linewidth]{\detokenize{../../prompts/zsxq_img.jpg}}",
        r"\end{center}",
        r"\end{document}",
    ]
    return "\n".join(lines) + "\n"


def compile_pdf(tex_path: Path) -> bool:
    if not shutil.which("xelatex"):
        log("xelatex not found; skipping PDF compilation.")
        return False
    cwd = tex_path.parent
    result = subprocess.run(["xelatex", "-interaction=nonstopmode", "-halt-on-error", tex_path.name], cwd=str(cwd), stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True, timeout=600)
    (cwd / "xelatex.log").write_text(result.stdout, encoding="utf-8")
    if result.returncode != 0:
        log(f"xelatex failed. See {cwd / 'xelatex.log'}")
        return False
    return tex_path.with_suffix(".pdf").exists()


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--dropbox-output-root", default="xhs_notes/dropbox")
    parser.add_argument("--extra-roots", default="",
                        help="Comma list of extra output roots to merge for the same date, e.g. xhs_notes/institutions.")
    parser.add_argument("--date-folder", default="latest")
    parser.add_argument("--output-root", default="market_view_summaries")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--deepseek-max-tokens", type=int, default=8192)
    parser.add_argument("--max-reports", type=int, default=0, help="0 means no limit")
    parser.add_argument("--per-report-prompt-chars", type=int, default=2200)
    parser.add_argument("--per-report-extract-chars", type=int, default=2200)
    parser.add_argument("--max-figures", type=int, default=0, help="0 means no limit")
    parser.add_argument("--max-selected-figures", type=int, default=0, help="0 means no limit")
    parser.add_argument("--max-figures-per-report", type=int, default=0, help="0 means no limit")
    parser.add_argument("--max-external-visuals-per-report", type=int, default=0,
                        help="Deprecated; Market Views uses source exhibits only, not generated visual cards.")
    parser.add_argument("--max-external-roundup-items", type=int, default=24,
                        help="Maximum institution/consulting items to expand in the external roundup.")
    parser.add_argument("--max-reports-per-bank-section", type=int, default=12,
                        help="Split planned bank themes above this size so DeepSeek can cover every report.")
    parser.add_argument("--max-section-figure-candidates", type=int, default=40,
                        help="Maximum relevant exhibit candidates sent to one DeepSeek bank-section request.")
    parser.add_argument("--figures-per-bank-section", type=int, default=4,
                        help="Maximum source exhibits rendered for each bank-led theme.")
    parser.add_argument("--compile", default="false")
    args = parser.parse_args()

    root = Path(args.dropbox_output_root)
    extra_roots = [Path(r.strip()) for r in (args.extra_roots or "").split(",") if r.strip()]
    report_date, date_dirs = source_date_dirs(root, extra_roots, args.date_folder)
    out_dir = Path(args.output_root) / report_date
    figures_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    report_dirs: list[Path] = []
    for source_dir in date_dirs:
        if not source_dir.exists():
            log(f"Source date folder not found, skipping: {source_dir}")
            continue
        source_dirs = find_report_dirs(source_dir)
        if source_dir.parent == root and shard_dirs(source_dir) and not source_dirs:
            raise RuntimeError(
                f"Primary Dropbox folder has shard directories but no report folders: {source_dir}. "
                "Refusing to generate Market Views without bank research inputs."
            )
        log(f"Using {len(source_dirs)} report directories from {source_dir}")
        report_dirs.extend(source_dirs)
    if args.max_reports > 0:
        report_dirs = report_dirs[: args.max_reports]
    if not report_dirs:
        roots_text = ", ".join(str(path) for path in date_dirs)
        raise RuntimeError(f"No report outputs found under source date folders: {roots_text}")
    log(f"MARKET_VIEWS_DATE_FOLDER={report_date}")
    log(f"Found {len(report_dirs)} report directories (incl. all source roots)")

    reports: list[dict[str, Any]] = []
    raw_figures: list[dict[str, Any]] = []
    for idx, report_dir in enumerate(report_dirs, 1):
        rid = f"R{idx:03d}"
        status = load_status(report_dir)
        digest = report_digest(report_dir, args.per_report_prompt_chars)
        source_group = infer_source_group(report_dir)
        institution_name = infer_source_name(report_dir, digest["title"], status)
        reports.append({
            "id": rid,
            "title": digest["title"],
            "path": str(report_dir),
            "source_group": source_group,
            "source_label": source_group_label(source_group),
            "institution_name": institution_name,
            "source_date_folder": report_date_from_path(report_dir),
            "digest": digest["digest"],
            "extract": report_extract(report_dir, args.per_report_extract_chars),
        })
        figs = extract_exhibit_figures(report_dir, rid, digest["title"], args.max_figures_per_report)
        for fig in figs:
            fig["source_group"] = source_group
            fig["source_label"] = source_group_label(source_group)
            fig["institution_name"] = institution_name
        raw_figures.extend(figs)
        log(f"Collected {rid}: {digest['title']} | source={source_group_label(source_group)} {institution_name or ''} | figure_candidates={len(figs)}")

    figures = copy_figures(raw_figures, figures_dir, args.max_figures)
    log(f"Copied {len(figures)} clean exhibit-style figures to {figures_dir}")
    (out_dir / "report_inputs.json").write_text(json.dumps(reports, ensure_ascii=False, indent=2), encoding="utf-8")
    (out_dir / "figure_candidates.json").write_text(json.dumps(figures, ensure_ascii=False, indent=2), encoding="utf-8")

    for stale_path in out_dir.glob("deepseek_bank_section_*_raw.json"):
        stale_path.unlink()
    for stale_path in out_dir.glob("deepseek_bank_section_*_error.txt"):
        stale_path.unlink()
    (out_dir / "prompt_for_market_views.md").write_text(build_prompt(reports, figures, args), encoding="utf-8")
    summary = build_market_summary(reports, figures, args, out_dir)
    summary = json.loads(sanitize_text(json.dumps(summary, ensure_ascii=False)))
    coverage = summary.get("coverage") or {}
    if coverage.get("bank_content_covered") != coverage.get("bank_reports"):
        raise RuntimeError(
            "Bank content coverage validation failed: "
            f"covered={coverage.get('bank_content_covered')} total={coverage.get('bank_reports')}"
        )
    log(
        "Validated substantive bank coverage: "
        f"{coverage.get('bank_content_covered')}/{coverage.get('bank_reports')} reports appear in bank_views"
    )
    (out_dir / "market_views_structured.json").write_text(json.dumps(summary, ensure_ascii=False, indent=2), encoding="utf-8")
    tex_path = out_dir / f"market_views_{report_date}.tex"
    tex_path.write_text(render_latex(summary, {r["id"]: r for r in reports}, {f["figure_id"]: f for f in figures}, report_date), encoding="utf-8")
    log(f"Wrote LaTeX: {tex_path}")
    if str(args.compile).lower() in {"1", "true", "yes", "y", "on"}:
        if compile_pdf(tex_path):
            log(f"PDF generated: {tex_path.with_suffix('.pdf')}")
        else:
            log("PDF compilation did not complete successfully. LaTeX source is still available.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
