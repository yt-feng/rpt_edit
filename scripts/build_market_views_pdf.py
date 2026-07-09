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
        json={"model": args.model, "temperature": 0.35, "messages": [{"role": "system", "content": "你是专业宏观策略研究编辑。只输出合法 JSON，不要输出 Markdown 代码块。"}, {"role": "user", "content": prompt}]},
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
    report_payload = [
        {
            "id": r["id"],
            "title": r["title"],
            "source_group": r.get("source_group", ""),
            "source_label": r.get("source_label") or source_group_label(r.get("source_group", "")),
            "institution": r.get("institution_name") or "",
            "digest": trim_text(r["digest"], args.per_report_prompt_chars),
        }
        for r in reports
    ]
    figure_payload = [
        {
            "figure_id": f["figure_id"],
            "report_id": f["report_id"],
            "label": f["label"],
            "figure_type": f.get("figure_type", "source_exhibit"),
            "context": f["context"],
        }
        for f in figures
    ]
    source_counts = {source_group_label(group): sum(1 for r in reports if r.get("source_group") == group) for group in ROUNDUP_SOURCE_ORDER}
    figure_rule = "可以使用所有 figure_ids，没有总数限制，但只选择真正支撑该板块观点且图表说明干净的图。"
    if args.max_selected_figures > 0:
        figure_rule = f"可以使用 figure_ids，但总图表数不要超过 {args.max_selected_figures} 张。"
    return f"""
请基于下面每天新报告的摘要，写一份“Market Views / 国际信源汇编&评论”的结构化 JSON，用于生成 PDF。

目标读者：
关注每日更新的国际信源汇编&评论，希望快速看到国际主流叙事、数据、图表和边际变化。读者来自头部券商、PE/VC、投行、并购、hedge fund、资管机构、战略咨询、智库等。

要求：
1. 严格按来源拆成三个并列板块，不要混在一起：投行/券商（source_group=bank_research）、战略咨询（source_group=consulting）、智库/国际机构（source_group=institution）。
2. 三个板块篇幅要尽量接近。即使某一类报告更多，也要压缩成和另外两类相近的阅读体量；不要让世界银行/智库报告把 PDF 撑成长篇翻译。
3. 每个来源板块内部再按主题归纳 2-4 个 themes，例如宏观与利率、AI/算力、能源与大宗、地缘政治、企业战略、发展经济等。主题由内容决定，不要机械套模板。
4. 每个 theme 综合多篇报告，写 3-5 个 bullets；每条必须是可读完整句，保留关键数据、方向、分歧和边际变化，不要逐篇复述。
5. 每个 theme 必须给 references，引用报告 ID；三个来源板块合计 references 应覆盖全部或绝大多数报告。覆盖清单会展示这些 references，所以不要漏。
6. {figure_rule}
7. 投行名字必须脱敏：常见投行写 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写，不确定就写“投行”。
8. 不要给投资建议，不要写买卖评级。
9. 不要输出“逐篇报告摘录”；正文只需要整合后的信号、评论、数据和图表。
10. source_roundups 必须按 source_group 输出三个对象，顺序为 bank_research、consulting、institution；如果某类当天没有报告，仍输出空 themes，并在 summary 写“今日暂无新增”。
11. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{{"title":"市场最新观点汇总","subtitle":"一句话说明今天国际信源的共同主线","executive_summary":["全局要点1"],"source_roundups":[{{"source_group":"bank_research","title":"投行/券商","summary":"本来源板块一句话摘要","themes":[{{"heading":"主题标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001","R002"]}}]}},{{"source_group":"consulting","title":"战略咨询","summary":"本来源板块一句话摘要","themes":[]}},{{"source_group":"institution","title":"智库/国际机构","summary":"本来源板块一句话摘要","themes":[]}}],"closing":"简短收束"}}

来源数量：
{json.dumps(source_counts, ensure_ascii=False, indent=2)}

报告摘要：
{json.dumps(report_payload, ensure_ascii=False, indent=2)}

可选图表候选（已经过滤掉邮箱、电话、HTML/table 噪音）：
{json.dumps(figure_payload, ensure_ascii=False, indent=2)}
""".strip()


def fallback_summary(reports: list[dict[str, Any]], figures: list[dict[str, Any]]) -> dict[str, Any]:
    return {
        "title": "市场最新观点汇总",
        "subtitle": "以下汇总基于今日新增报告的自动整理。",
        "executive_summary": [
            "今日信源按投行/券商、战略咨询、智库/国际机构三类拆开整理，避免不同类型叙事互相混杂。",
            "正文只保留整合后的主线、边际变化、数据和图表；逐篇原文摘录不进入 PDF。",
            "报告覆盖清单用于核对所有纳入的报告及其整合位置。",
        ],
        "source_roundups": build_source_roundups(reports, figures),
        "closing": "后续更重要的是跟踪哪些叙事被数据确认，哪些只停留在观点层面。",
    }


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
    return "该外部来源提供了一个需要纳入今日市场判断的补充信号。"


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


def bank_category_for(report: dict[str, Any]) -> str:
    haystack = " ".join([
        str(report.get("title") or ""),
        str(report.get("digest") or "")[:1600],
    ]).lower()
    rules = (
        ("宏观、利率与外汇", ("macro", "rates", "fed", "ecb", "boj", "inflation", "fx", "currency", "bond", "yield", "宏观", "利率", "美联储", "欧央行", "央行", "通胀", "外汇", "人民币", "债券", "收益率")),
        ("AI、科技与产业链", ("ai", "semiconductor", "data center", "cloud", "software", "chip", "tech", "算力", "半导体", "数据中心", "芯片", "科技", "互联网", "软件")),
        ("能源、大宗与资源", ("oil", "gas", "commodity", "copper", "gold", "power", "utility", "energy", "solar", "battery", "原油", "天然气", "能源", "大宗", "铜", "黄金", "电力", "公用事业", "光伏", "电池")),
        ("中国、消费与地产", ("china", "consumer", "property", "real estate", "retail", "bank", "中国", "消费", "地产", "房地产", "银行", "零售", "美妆")),
        ("区域市场与风险偏好", ("japan", "india", "europe", "em", "equity", "liquidity", "retail", "flow", "日本", "印度", "欧洲", "新兴市场", "股票", "资金流", "散户", "风险偏好")),
    )
    for category, keywords in rules:
        if any(keyword in haystack for keyword in keywords):
            return category
    return "其他市场边际信号"


def report_category_for(report: dict[str, Any]) -> str:
    source_group = report.get("source_group")
    if source_group == "bank_research":
        return bank_category_for(report)
    return external_category_for(report)


def source_group_reports(reports: list[dict[str, Any]], source_group: str) -> list[dict[str, Any]]:
    return [r for r in reports if r.get("source_group") == source_group]


def fallback_theme_for_reports(
    heading: str,
    reports: list[dict[str, Any]],
    figures: list[dict[str, Any]],
    max_bullets: int = 4,
) -> dict[str, Any]:
    refs = [r["id"] for r in reports]
    bullets = [first_signal(r.get("extract") or r.get("digest") or "", max_chars=120) for r in reports[:max_bullets]]
    if len(reports) > max_bullets:
        bullets.append(f"另有 {len(reports) - max_bullets} 篇同主题报告已纳入 references，用于校准该主题的叙事覆盖与边际变化。")
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

    themes = [fallback_theme_for_reports(heading, items, figures) for heading, items in primary if items]
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
        build_source_roundup_for_group(source_group_reports(reports, source_group), figures, source_group)
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
        target = roundup["themes"][-1] if roundup["themes"] else None
        if target is None:
            fallback = build_source_roundup_for_group([reports_by_id[rid] for rid in missing], list(figures_by_id.values()), source_group)
            roundup["themes"] = fallback["themes"]
        else:
            target.setdefault("references", [])
            target["references"].extend(rid for rid in missing if rid not in target["references"])
            target.setdefault("bullets", [])
            target["bullets"].append(f"另有 {len(missing)} 篇同来源报告纳入 references，用于校准该来源板块覆盖面。")

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
    for roundup in summary.get("source_roundups", []) or []:
        lines.append(r"\section{" + latex_escape(roundup.get("title") or source_group_label(roundup.get("source_group", ""))) + r"}")
        if roundup.get("summary"):
            lines.append(latex_escape(roundup.get("summary")))
            lines.append("")
        for theme in roundup.get("themes") or []:
            lines.append(r"\subsection{" + latex_escape(theme.get("heading") or "未命名主题") + r"}")
            if theme.get("thesis"):
                lines.append(r"\textbf{" + latex_escape(theme.get("thesis")) + r"}")
                lines.append("")
            if theme.get("bullets"):
                lines.append(r"\begin{itemize}")
                for bullet in theme.get("bullets", []):
                    lines.append(r"  \item " + latex_escape(bullet))
                lines.append(r"\end{itemize}")
            for fig_id in (theme.get("figure_ids") or []):
                fig = figures_by_id.get(fig_id)
                if not fig:
                    continue
                lines += [r"\begin{figure}[htbp]", r"\centering", r"\includegraphics[width=0.88\linewidth]{" + fig["latex_path"] + r"}", r"\caption{" + latex_escape(f"{fig.get('label', 'Figure')} - {fig.get('context', '')}") + r"}", r"\end{figure}"]
            refs = []
            for ref_id in theme.get("references", []):
                report = reports_by_id.get(str(ref_id))
                if report:
                    refs.append(f"[{ref_id}] {report['title']}")
            if refs:
                lines.append(r"{\small\color{refgray}\textbf{References:} " + latex_escape("; ".join(refs)) + r"}")
            lines.append("")
        if not roundup.get("themes"):
            lines.append(r"\begin{itemize}")
            lines.append(r"  \item " + latex_escape(roundup.get("summary") or "今日暂无新增报告。"))
            lines.append(r"\end{itemize}")
    if summary.get("closing"):
        lines += [r"\section{结语}", latex_escape(summary.get("closing"))]
    lines += [r"\newpage", r"\section{报告覆盖清单}", r"\begin{itemize}"]
    coverage = source_roundup_map(summary)
    for report_id, report in reports_by_id.items():
        categories = " / ".join(coverage.get(report_id, ["未被来源板块引用"]))
        source = source_group_label(report.get("source_group", ""))
        lines.append(r"  \item " + latex_escape(f"[{report_id}] {source} | {categories} - {report.get('title', '')}"))
    lines += [r"\end{itemize}"]
    lines += [r"\section{Disclaimer}", r"{\scriptsize\color{refgray}"]
    for para in DISCLAIMER_TEXT.split("\n\n"):
        lines.append(latex_escape(para) + r"\par")
    lines += [r"}", r"\end{document}"]
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

    prompt = build_prompt(reports, figures, args)
    (out_dir / "prompt_for_market_views.md").write_text(prompt, encoding="utf-8")
    try:
        raw = call_deepseek(prompt, args, "market views roundup")
        (out_dir / "deepseek_market_views_raw.json").write_text(raw, encoding="utf-8")
        summary = extract_json(raw)
    except Exception as exc:
        log(f"DeepSeek market summary failed; using fallback: {exc}")
        summary = fallback_summary(reports, figures)
        (out_dir / "deepseek_market_views_error.txt").write_text(str(exc), encoding="utf-8")
    summary = json.loads(sanitize_text(json.dumps(summary, ensure_ascii=False)))
    summary = enrich_source_roundups(summary, reports, figures)
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
