#!/usr/bin/env python3
"""Build a market-view roundup PDF from generated daily report outputs.

Input is usually xhs_notes/dropbox/<latest_date>/shard_*/<report>/.
The script:
1. Collects generated report outputs.
2. Extracts exhibit-style figure candidates from MinerU markdown.
3. Calls DeepSeek to synthesize a categorized market-view roundup.
4. Writes a LaTeX source and optionally compiles it to PDF.

Figures are only considered when an image reference is near labels such as
"Exhibit 1", "Exh. 2", "Figure 3", or "图表 4".
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

EXHIBIT_RE = re.compile(r"\b(?:Exhibit|EXHIBIT|Exh\.?|Figure|FIGURE)\s*[-#:：]?\s*\d+\b|图表\s*[-#:：]?\s*\d+", re.I)
IMAGE_RE = re.compile(r"!\[[^\]]*\]\(([^\)]+)\)")
DATE_DIR_RE = re.compile(r"^\d{6,8}$")


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
    if len(text) <= max_chars:
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


def find_report_dirs(date_dir: Path) -> list[Path]:
    report_dirs: list[Path] = []
    for shard in sorted(date_dir.glob("shard_*")):
        if not shard.is_dir():
            continue
        for item in sorted(shard.iterdir()):
            if item.is_dir() and (item / "source_mineru.md").exists():
                report_dirs.append(item)
    for item in sorted(date_dir.iterdir()):
        if item.is_dir() and (item / "source_mineru.md").exists():
            report_dirs.append(item)
    seen = set()
    unique = []
    for p in report_dirs:
        key = str(p.resolve())
        if key not in seen:
            seen.add(key)
            unique.append(p)
    return unique


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


def extract_exhibit_figures(report_dir: Path, report_id: str, title: str, max_per_report: int) -> list[dict[str, Any]]:
    md_path = report_dir / "source_mineru.md"
    if not md_path.exists():
        return []
    lines = md_path.read_text(encoding="utf-8", errors="ignore").splitlines()
    figures: list[dict[str, Any]] = []
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
        label_match = EXHIBIT_RE.search(context)
        label = label_match.group(0) if label_match else "Exhibit"
        context_clean = normalize_space(re.sub(IMAGE_RE, "", context))[:520]
        figures.append({"report_id": report_id, "report_title": title, "source_path": str(image_path), "label": sanitize_text(label), "context": sanitize_text(context_clean)})
        if len(figures) >= max_per_report:
            break
    return figures


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
    figures_dir.mkdir(parents=True, exist_ok=True)
    copied: list[dict[str, Any]] = []
    for idx, fig in enumerate(figures[:max_figures], 1):
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
    report_payload = [{"id": r["id"], "title": r["title"], "digest": trim_text(r["digest"], args.per_report_prompt_chars)} for r in reports]
    figure_payload = [{"figure_id": f["figure_id"], "report_id": f["report_id"], "label": f["label"], "context": f["context"]} for f in figures]
    return f"""
请基于下面每天新报告的摘要，写一份“市场最新观点汇总”的结构化 JSON，用于生成 PDF。

要求：
1. 观点要分门别类，例如：宏观与利率、AI/算力、能源与大宗、地产与消费、区域市场、风险偏好等。类别由内容决定，不要机械套模板。
2. 每个板块要综合多篇报告，不要逐篇复述。
3. 每个板块必须有 3-6 个要点，每个要点是可读的完整句子。
4. 每个板块末尾必须给 references，引用报告 ID，不要在正文每句后塞引用。
5. 可以使用 figure_ids，但只能从提供的 Exhibit/Figure 候选中选择。每个板块最多 2 张图；总图表不要超过 {args.max_selected_figures} 张。
6. 投行名字已经脱敏，但如果看到全称，也必须改成 GS、JPM、MS、BofA、Citi、UBS、DB 等缩写或写“投行”。
7. 不要给投资建议，不要写买卖评级。
8. 输出必须是 JSON 对象，不要 Markdown 代码块。

JSON 格式：
{{"title":"市场最新观点汇总","subtitle":"一句话说明今天的市场主线","executive_summary":["要点1"],"sections":[{{"heading":"板块标题","thesis":"核心判断","bullets":["要点1"],"figure_ids":["F001"],"references":["R001"]}}],"closing":"简短收束"}}

报告摘要：
{json.dumps(report_payload, ensure_ascii=False, indent=2)}

可选图表候选：
{json.dumps(figure_payload, ensure_ascii=False, indent=2)}
""".strip()


def fallback_summary(reports: list[dict[str, Any]], figures: list[dict[str, Any]]) -> dict[str, Any]:
    refs = [r["id"] for r in reports[:8]]
    return {"title": "市场最新观点汇总", "subtitle": "以下汇总基于今日新增报告的自动整理。", "executive_summary": ["今日报告主要围绕宏观、行业供需、估值重定价和风险偏好展开。", "不同报告之间的共同线索，是市场正在重新评估增长确定性、资金成本和产业链议价能力。", "部分结论仍需要结合后续数据验证，尤其是需求恢复的持续性和盈利弹性。"], "sections": [{"heading": "跨资产主线仍围绕增长、利率和盈利再定价展开", "thesis": "报告共同指向一个问题：市场不是只在交易单点事件，而是在重新评估未来几个季度的增长质量。", "bullets": ["多篇报告都把需求弹性、供给约束和资金成本作为判断资产价格的核心变量。", "行业内部的分化仍然显著，能够把规模或资源优势转化为现金流的主体更容易获得估值支撑。", "当前观点并非单边乐观，报告普遍保留了对政策、价格和盈利兑现节奏的验证要求。"], "figure_ids": [f["figure_id"] for f in figures[:1]], "references": refs}], "closing": "后续更重要的是跟踪哪些假设被数据确认，哪些只停留在叙事层面。"}


def render_latex(summary: dict[str, Any], reports_by_id: dict[str, dict[str, Any]], figures_by_id: dict[str, dict[str, Any]], report_date: str) -> str:
    title = summary.get("title") or "市场最新观点汇总"
    subtitle = summary.get("subtitle") or "Daily market views roundup"
    lines: list[str] = []
    lines += [r"\documentclass[11pt]{ctexart}", r"\usepackage[a4paper,margin=1in]{geometry}", r"\usepackage{graphicx}", r"\usepackage{xcolor}", r"\usepackage{hyperref}", r"\definecolor{refgray}{gray}{0.45}", r"\title{\textbf{" + latex_escape(title) + r"}\\[0.4em]{\large " + latex_escape(subtitle) + r"}}", r"\author{KC桌面 自动生成}", r"\date{" + latex_escape(report_date) + r"}", r"\begin{document}", r"\maketitle", r"\section*{一页摘要}", r"\begin{itemize}"]
    for item in summary.get("executive_summary", [])[:6]:
        lines.append(r"  \item " + latex_escape(item))
    lines.append(r"\end{itemize}")
    for section in summary.get("sections", [])[:10]:
        lines.append(r"\section{" + latex_escape(section.get("heading") or "未命名板块") + r"}")
        if section.get("thesis"):
            lines.append(r"\textbf{" + latex_escape(section.get("thesis")) + r"}")
            lines.append("")
        if section.get("bullets"):
            lines.append(r"\begin{itemize}")
            for bullet in section.get("bullets", [])[:8]:
                lines.append(r"  \item " + latex_escape(bullet))
            lines.append(r"\end{itemize}")
        for fig_id in (section.get("figure_ids") or [])[:2]:
            fig = figures_by_id.get(fig_id)
            if not fig:
                continue
            lines += [r"\begin{figure}[htbp]", r"\centering", r"\includegraphics[width=0.88\linewidth]{" + fig["latex_path"] + r"}", r"\caption{" + latex_escape(f"{fig.get('label', 'Exhibit')} - {fig.get('context', '')[:180]}") + r"}", r"\end{figure}"]
        refs = []
        for ref_id in section.get("references", [])[:12]:
            report = reports_by_id.get(ref_id)
            if report:
                refs.append(f"[{ref_id}] {report['title']}")
        if refs:
            lines.append(r"{\small\color{refgray}\textbf{References:} " + latex_escape("; ".join(refs)) + r"}")
        lines.append("")
    if summary.get("closing"):
        lines += [r"\section*{结语}", latex_escape(summary.get("closing"))]
    lines += [r"\vfill", r"{\small\color{refgray}Personal reading notes and learning share only. Not investment advice.}", r"\end{document}"]
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
    parser.add_argument("--date-folder", default="latest")
    parser.add_argument("--output-root", default="market_view_summaries")
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--max-reports", type=int, default=80)
    parser.add_argument("--per-report-prompt-chars", type=int, default=2200)
    parser.add_argument("--max-figures", type=int, default=40)
    parser.add_argument("--max-selected-figures", type=int, default=12)
    parser.add_argument("--max-figures-per-report", type=int, default=2)
    parser.add_argument("--compile", default="true")
    args = parser.parse_args()

    root = Path(args.dropbox_output_root)
    date_dir = latest_date_dir(root) if args.date_folder == "latest" else root / args.date_folder
    if not date_dir.exists():
        raise RuntimeError(f"Date folder not found: {date_dir}")
    report_date = date_dir.name
    out_dir = Path(args.output_root) / report_date
    figures_dir = out_dir / "figures"
    out_dir.mkdir(parents=True, exist_ok=True)

    report_dirs = find_report_dirs(date_dir)[: args.max_reports]
    if not report_dirs:
        raise RuntimeError(f"No report outputs found under {date_dir}")
    log(f"Found {len(report_dirs)} report directories under {date_dir}")

    reports: list[dict[str, Any]] = []
    raw_figures: list[dict[str, Any]] = []
    for idx, report_dir in enumerate(report_dirs, 1):
        rid = f"R{idx:03d}"
        digest = report_digest(report_dir, args.per_report_prompt_chars)
        reports.append({"id": rid, "title": digest["title"], "path": str(report_dir), "digest": digest["digest"]})
        figs = extract_exhibit_figures(report_dir, rid, digest["title"], args.max_figures_per_report)
        raw_figures.extend(figs)
        log(f"Collected {rid}: {digest['title']} | exhibit_figures={len(figs)}")

    figures = copy_figures(raw_figures, figures_dir, args.max_figures)
    log(f"Copied {len(figures)} exhibit-style figures to {figures_dir}")
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
