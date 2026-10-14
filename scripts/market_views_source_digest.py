#!/usr/bin/env python3
"""Bounded, model-free source excerpts for the daily delivery deadline.

Each original runs in its own process. A slow PDF/OCR process cannot hold the
daily edition open; its exact manifest identity remains an explicit omission.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import os
from pathlib import Path
import re
import signal
import subprocess
import sys
import time


LEGAL = re.compile(r"disclaimer|disclosure|all rights reserved|not (?:an? )?(?:offer|investment advice)|"
                   r"copyright|analyst certification|distribution of ratings|免责声明|版权|分析师声明|评级分布|"
                   r"(?:investors?|recipients?)\s+should\s+consider.{0,160}(?:single|one)\s+factor.{0,100}investment\s+decision|"
                   r"intended\s+solely\s+for\s+(?:the\s+)?recipient|may\s+not\s+be\s+(?:further\s+)?distributed|"
                   r"does\s+and\s+seeks\s+to\s+do\s+business\s+with|"
                   r"https?://|[\w.+-]+@[\w.-]+\.[A-Za-z]{2,}", re.I)
RESEARCH = re.compile(r"growth|inflation|econom|market|forecast|expect|demand|supply|revenue|earnings|"
                      r"investment|interest rate|valuation|policy|yield|equity|capital|consumer|"
                      r"增长|通胀|经济|市场|预计|预测|需求|供给|收入|盈利|投资|利率|估值|政策|资本|消费", re.I)
FIGURE = re.compile(r"\b(?:exhibit|figure|chart)\s*\d|图表\s*\d|图\s*\d", re.I)
FILENAME_LINE = re.compile(r"^\d{2,6}[-_](?:[A-Za-z]|[\u3400-\u9fff])|\.pdf(?:\s|$)|[-_]\d{6,8}$", re.I)
EN_ASSERTION = re.compile(r"\b(?:is|are|was|were|has|have|had|will|would|can|could|may|might|must|should|"
    r"expects?|expected|believes?|believed|anticipates?|anticipated|forecasts?|forecasted|projects?|projected|"
    r"remains?|remained|increases?|increased|decreases?|decreased|declines?|declined|grows?|grew|rises?|rose|falls?|fell|"
    r"improves?|improved|supports?|supported|suggests?|suggested|reflects?|reflected|continues?|continued|"
    r"indicates?|indicated|benefits?|benefited|depends?|depended|generates?|generated|accounts?|accounted|"
    r"represents?|represented|reaches?|reached|leads?|led|reduces?|reduced|expands?|expanded|contracts?|contracted|"
    r"shows?|showed|observes?|observed|sees?|saw|finds?|found|notes?|noted|argues?|argued|estimates?|estimated)\b", re.I)
ZH_ASSERTION = re.compile(r"预计|预期|认为|显示|表明|达到|增长|下降|上升|提高|降低|增加|减少|放缓|加快|扩大|收缩|"
                          r"推动|支撑|抑制|导致|受到|保持|维持|取决于|意味着|有望|将会|仍然|已经|正在|是|为")


def _assertion(value: str) -> bool:
    han = len(re.findall(r"[\u3400-\u9fff]", value))
    if han >= 18:
        return bool(ZH_ASSERTION.search(value) and re.search(r"[。！？]$", value))
    words = re.findall(r"[A-Za-z]+(?:'[a-z]+)?", value)
    predicate = EN_ASSERTION.search(value)
    if not predicate or not re.search(r"[A-Za-z]{2,}", value[:predicate.start()]):
        return False
    # English headlines usually consist of title-cased noun phrases. A verb
    # keyword alone (e.g. 'Forecast') must not make that a research assertion.
    title_case = sum(word[:1].isupper() for word in words) / max(len(words), 1)
    return title_case < .60 or bool(re.search(r"[.!?][\"”')]*$", value))


def substantive_sentences(text: str, *, limit: int = 12, max_chars: int = 600) -> list[str]:
    """Retain literal source sentences; never invent connective conclusions."""
    text = "\n".join(line for line in str(text or "").splitlines()
                     if not re.match(r"^\s*#{1,6}(?:\s|$)", line)
                     and not FILENAME_LINE.search(line.strip()))
    text = re.sub(r"!\[[^\]]*\]\([^)]*\)", " ", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]*\)", r"\1", text)
    text = re.sub(r"<[^>]+>", " ", text)
    blocks = re.split(r"\n\s*\n|(?<=[。！？])|(?<=[.!?])\s+(?=[A-Z])", text)
    results = []
    for block in blocks:
        value = re.sub(r"\s+", " ", block).strip(" #*>-\t")
        if not 40 <= len(value) <= max_chars or LEGAL.search(value):
            continue
        if any(token in value for token in ("数值待核对", "middle omitted", "新增市场信号", "来源摘录（")):
            continue
        if len(re.findall(r"[A-Za-z]{3,}", value)) < 7 and len(re.findall(r"[\u3400-\u9fff]", value)) < 18:
            continue
        if FILENAME_LINE.search(value) or not RESEARCH.search(value) or not _assertion(value) or value in results:
            continue
        results.append(value)
        if len(results) >= limit:
            break
    return results


def daily_category_for(report: dict) -> str:
    """Classify the report subject, never incidental words in its body.

    In particular EV must not match 'preview', AI must not match 'retail', and
    a company earnings preview belongs to its sector rather than a broad equity
    strategy merely because it mentions earnings or valuation.
    """
    from build_market_views_pdf import BANK_CATEGORY_RULES
    title = str(report.get("title") or "").casefold().replace("_", " ")

    def matches(keyword):
        if keyword.isascii():
            pattern = re.escape(keyword).replace(r"\ ", r"\s+")
            return bool(re.search(r"(?<![a-z0-9])" + pattern + r"(?![a-z0-9])", title))
        return keyword in title

    if any(matches(word) for word in ("telecom", "telecommunications", "broadband", "电信", "宽带", "有线电视")):
        return "电信、宽带与有线网络"
    if any(matches(word) for word in ("equity strategy", "quant strategy", "tech strategy", "equity weekly",
                                     "portfolio strategy", "股票策略", "量化策略")):
        return "股票策略、估值与资金流"
    additions = {
        "AI、半导体与硬件": ("iphone", "smartphone", "apple", "tsmc", "nvidia", "semis", "handset", "智能手机", "台积电", "苹果"),
        "软件、互联网与数字平台": ("payment technology", "payment processing", "payments", "fintech", "amazon", "amzn", "aws",
            "alphabet", "google", "meta", "microsoft", "tencent", "alibaba", "jd.com", "pdd", "baidu", "支付", "金融科技"),
        "汽车、新能源与工业": ("autos", "automotive", "electric vehicles", "nevs", "bevs", "phevs", "toyota", "tesla"),
    }
    generic = {"宏观、央行与利率", "外汇与跨境资金", "股票策略、估值与资金流",
               "日本、韩国与亚洲市场", "欧洲、美洲与新兴市场"}
    scored = []
    for index, (category, keywords) in enumerate(BANK_CATEGORY_RULES):
        hits = [word for word in (*keywords, *additions.get(category, ())) if matches(word)]
        if not hits:
            continue
        score = sum(3 if " " in word or word in additions.get(category, ()) else 1 for word in hits)
        # Specific sector evidence in the title outweighs generic 'earnings'
        # and geographical labels; an explicit strategy title returned above.
        scored.append((category not in generic, score, -index, category))
    return max(scored)[-1] if scored else "其他公司与行业信号"


def _write_json(path: Path, value) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def _chart_regions(page):
    """Original embedded images/vector plots only; never return a full page."""
    import fitz
    page_area = page.rect.get_area()
    regions = []
    for info in page.get_image_info():
        rect = fitz.Rect(info["bbox"]) & page.rect
        if (info.get("width", 0) >= 250 and info.get("height", 0) >= 150
                and 0.035 <= rect.get_area() / page_area <= 0.65
                and 0.55 <= rect.width / max(rect.height, 1) <= 4):
            regions.append(rect)
    if regions:
        return regions[:2]
    # Group touching vector components into plots, while excluding page rules
    # and full-page borders. The pixels remain an exact crop of the original.
    pieces = []
    for drawing in page.get_drawings():
        rect = fitz.Rect(drawing["rect"]) & page.rect
        if rect.width < 2 or rect.height < 2 or rect.get_area() > 0.60 * page_area:
            continue
        expanded = rect + (-8, -8, 8, 8)
        overlaps = [index for index, region in enumerate(pieces) if region.intersects(expanded)]
        if overlaps:
            for index in reversed(overlaps):
                rect |= pieces.pop(index)
        pieces.append(rect)
    return [rect + (-4, -4, 4, 4) for rect in pieces if rect.width >= 140 and rect.height >= 80
            and 0.04 <= rect.get_area() / page_area <= 0.65][:2]


def _extract_one(pdf: Path, destination: Path, digest: str, *, max_pages: int, ocr: bool,
                 deadline_seconds: float) -> dict:
    import fitz
    if hashlib.sha256(pdf.read_bytes()).hexdigest() != digest:
        raise ValueError("original_hash_mismatch")
    destination.mkdir(parents=True, exist_ok=True)
    end = time.monotonic() + deadline_seconds
    evidence, figures, examined = [], [], []
    with fitz.open(pdf) as document:
        if document.needs_pass or not document.page_count:
            raise ValueError("unreadable_original")
        page_count = len(document)
        native_pages = []
        for page in document:
            blocks = page.get_text("blocks", sort=True)
            native_pages.append("\n\n".join(str(block[4]) for block in blocks if len(block) > 6 and block[6] == 0))
        if ocr and sum(len(re.sub(r"\s", "", text)) < 80 for text in native_pages) > max_pages:
            raise ValueError("ocr_page_limit")
        for index, text in enumerate(native_pages):
            if time.monotonic() >= end:
                raise TimeoutError("source_deadline_exceeded")
            page = document[index]
            sentences = substantive_sentences(text, limit=4)
            method = "native-text"
            if not sentences and ocr and len(re.sub(r"\s", "", text)) < 80:
                remaining = end - time.monotonic()
                if remaining < 3:
                    raise TimeoutError("source_deadline_exceeded")
                image = destination / "ocr-input.png"
                page.get_pixmap(dpi=150, alpha=False).save(image)
                try:
                    result = subprocess.run(["tesseract", str(image), "stdout", "-l", "eng+chi_sim", "--psm", "3"],
                        capture_output=True, text=True, timeout=min(12, remaining), check=True)
                    text = result.stdout
                    sentences = substantive_sentences(text, limit=4)
                    method = "tesseract-ocr"
                except (FileNotFoundError, subprocess.SubprocessError):
                    sentences = []
                finally:
                    image.unlink(missing_ok=True)
            examined.append({"page": index + 1, "method": method})
            for sentence in sentences:
                if sentence not in {row["text"] for row in evidence}:
                    evidence.append({"page": index + 1, "method": method, "text": sentence})
            # Preserve original chart pixels without full-page screenshots.
            if len(figures) < 2 and FIGURE.search(text) and not LEGAL.search(text[:300]):
                for region in _chart_regions(page):
                    if len(figures) >= 2:
                        break
                    name = f"assets/source_image_{index + 1:04d}_{len(figures) + 1}.png"
                    target = destination / name
                    target.parent.mkdir(exist_ok=True)
                    page.get_pixmap(dpi=150, clip=region, alpha=False).save(target)
                    figures.append({"path": name, "page": index + 1, "crop_bbox": list(region),
                                    "page_size": [page.rect.width, page.rect.height]})
    if not evidence:
        raise ValueError("no_substantive_source_text")
    selected = evidence if len(evidence) <= 16 else evidence[:12] + evidence[-4:]
    title = pdf.stem
    # Source paragraphs precede extraction notes so the existing extractive
    # builder cannot mistake operational descriptions for research content.
    markdown = f"# {title}\n\n" + "\n\n".join(row["text"] for row in selected)
    markdown += "\n\n## 来源摘录页码\n\n" + "、".join(map(str, sorted({row["page"] for row in selected})))
    for index, figure in enumerate(figures, 1):
        markdown += (f"\n\nFigure {index}: 原报告第 {figure['page']} 页图表（原图裁取）\n\n"
                     f"![Figure {index}: Original research chart from page {figure['page']}]({figure['path']})\n")
    (destination / "source_mineru.md").write_text(markdown, encoding="utf-8")
    _write_json(destination / "source_excerpt_evidence.json", {"source_pdf": pdf.name,
        "content_sha256": digest, "page_count": page_count, "examined_pages": examined,
        "excerpts": selected, "figures": figures, "whole_report_coverage": len(examined) == page_count})
    _write_json(destination / "status.json", {"original_pdf_sha256": digest, "source_pdf": pdf.name,
        "source_method": "source-digest", "title": title, "page_count": page_count,
        "total_pages": page_count, "extracted_pages": [row["page"] for row in examined],
        "excerpt_pages": sorted({row["page"] for row in selected}), "model_requests": 0})
    files = ["source_mineru.md", "status.json", "source_excerpt_evidence.json"] + [row["path"] for row in figures]
    return {"directory": str(destination), "content_sha256": digest, "source_method": "source-digest", "files": files}


def _run_worker(pdf, destination, digest, *, timeout, max_pages, ocr):
    command = [sys.executable, str(Path(__file__).resolve()), "--worker", "--pdf", str(pdf),
        "--destination", str(destination), "--sha256", digest, "--max-pages", str(max_pages),
        "--deadline-seconds", str(max(1, timeout - 1))]
    if not ocr:
        command.append("--no-ocr")
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               text=True, start_new_session=True)
    try:
        stdout, _ = process.communicate(timeout=timeout)
    except subprocess.TimeoutExpired:
        # Terminate only the process group created above, including its own OCR
        # child. There is no executor shutdown that waits past the deadline.
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        process.communicate()
        raise TimeoutError("source_deadline_exceeded")
    value = json.loads(stdout.strip().splitlines()[-1]) if stdout.strip() else {}
    if process.returncode:
        raise ValueError(value.get("error", "source_extraction_failed"))
    return value


def extract_candidates(manifest: Path, originals_dir: Path, destination: Path, *,
                       existing_candidates: dict | None = None, deadline_seconds: float = 600,
                       per_report_seconds: float = 45, max_pages: int = 24, ocr: bool = True,
                       worker=None) -> tuple[dict, dict]:
    from extract_native_market_sources import read_manifest
    manifest, originals_dir, destination = map(Path, (manifest, originals_dir, destination))
    raw = json.loads(manifest.read_text(encoding="utf-8"))
    _, bindings = read_manifest(manifest, len(raw))
    candidates, reasons = dict(existing_candidates or {}), {}
    originals = {}
    for path in originals_dir.rglob("*"):
        if path.is_file() and not path.is_symlink() and path.suffix.lower() == ".pdf":
            originals.setdefault(path.name, []).append(path)
    end = time.monotonic() + max(0, deadline_seconds)
    run = worker or _run_worker
    for index, binding in enumerate(bindings, 1):
        name, digest = binding["source_pdf"], binding["content_sha256"]
        if name in candidates:
            continue
        remaining = end - time.monotonic()
        if remaining <= 1:
            reasons[name] = "delivery_deadline_reached"
            continue
        matching = originals.get(name, [])
        if len(matching) != 1:
            reasons[name] = "original_missing_or_ambiguous"
            continue
        target = destination / f"report_{index:04d}_{digest[:12]}"
        try:
            candidate = run(matching[0], target, digest, timeout=min(per_report_seconds, remaining),
                            max_pages=max_pages, ocr=ocr)
            candidate["directory"] = Path(candidate["directory"])
            candidates[name] = candidate
        except TimeoutError:
            reasons[name] = "source_deadline_exceeded"
        except Exception as exc:
            reasons[name] = str(exc) if str(exc) in {"ocr_page_limit", "original_hash_mismatch", "no_substantive_source_text", "source_deadline_exceeded"} else "source_extraction_failed"
    return candidates, reasons


def make_summary(reports: list[dict], figures: list[dict], receipt: dict) -> dict:
    """A thematic, attributed excerpt edition; no model or inferred consensus."""
    from build_market_views_pdf import bank_alias, cap_bank_plan, select_section_figures
    included = {row["report_id"] for row in receipt["reports"] if row["status"] == "included"}
    if len(reports) != receipt["included_reports"] or {Path(row.get("path", "")).name for row in reports} != included:
        raise ValueError("daily_digest_report_inventory_mismatch")
    by_id = {row["id"]: row for row in reports}
    grouped = {}
    for report in reports:
        heading = daily_category_for(report)
        grouped.setdefault(heading, []).append(report["id"])
    plan_rows = cap_bank_plan([{"heading": heading, "report_ids": ids}
                              for heading, ids in grouped.items()])
    sections, executive = [], []
    for plan in plan_rows:
        views = []
        for rid in plan["report_ids"]:
            report = by_id[rid]
            evidence_path = Path(report.get("path", "")) / "source_excerpt_evidence.json"
            evidence_rows, pages = [], []
            if evidence_path.is_file():
                evidence = json.loads(evidence_path.read_text(encoding="utf-8"))
                for row in evidence.get("excerpts", []):
                    for sentence in substantive_sentences(row.get("text", ""), limit=3):
                        if sentence not in {entry["text"] for entry in evidence_rows}:
                            evidence_rows.append({"text": sentence, "page": row["page"]})
                # The publication renderer retains one main view and one
                # supporting excerpt; cite only the text it will display.
                selected = evidence_rows[:2]
                sentences = [row["text"] for row in selected]
                pages = sorted({row["page"] for row in selected})
            else:
                # Standard report extracts prioritize generated articles. This
                # edition labels the text as source excerpts, so only the bound
                # original transcript may supply quotations without page evidence.
                raw_source = Path(report.get("path", "")) / "source_mineru.md"
                sentences = substantive_sentences(raw_source.read_text(encoding="utf-8"), limit=2)
            if not sentences:
                raise ValueError("daily_digest_report_has_no_substantive_excerpt")
            views.append({"bank": bank_alias(report), "view": sentences[0], "data_points": sentences[1:3],
                          "marginal_change": "", "report_ids": [rid]})
            if pages:
                views[-1]["sources"] = [{"report_id": rid, "pages": pages}]
            if len(executive) < 8:
                executive.append(bank_alias(report) + "：" + sentences[0])
        sections.append({"heading": plan["heading"], "thesis": "本节按主题列出已取得来源的研究摘录，保留机构归属与原始图表。",
            "consensus": [], "divergences": [], "data_points": [], "bank_views": views,
            "references": plan["report_ids"], "figure_ids": select_section_figures([], plan["report_ids"], figures, 4)})
    skipped = [row for row in receipt["reports"] if row["status"] == "skipped"]
    total_sources = receipt.get("expected_source_reports", receipt["expected_reports"])
    return {"schema_version": 2, "source_kind": "daily-digest", "synthesis_status": "source-excerpts",
        "title": "Market Views｜每日来源摘要", "subtitle": f"{receipt['date_folder']}｜来源摘要｜已整理 {len(reports)}/{total_sources} 份研究",
        "executive_summary": executive, "bank_roundup": {"title": "市场与产业主题｜来源摘要",
            "summary": "以下内容摘自本期已取得研究；未推断额外共识或分歧。", "sections": sections},
        "supporting_roundups": [], "coverage": {"bank_reports": len(reports), "bank_content_covered": len(reports)},
        "source_inventory": {"selected_originals": receipt["expected_reports"], "covered_originals": len(reports),
            "skipped_originals": len(skipped)}, "skipped_reports": skipped,
        "delivery_coverage": {key: receipt[key] for key in ("expected_reports", "included_reports", "skipped_reports")},
        "expected_source_reports": total_sources, "unavailable_originals": receipt.get("unavailable_originals", []),
        "delivery_receipt": {key: receipt[key] for key in ("date_folder", "source_run_id", "source_execution_sha", "source_inventory_sha256")},
        "closing": "本期按交付时限整理已取得的研究材料；未完成来源列于覆盖说明，后续完整版本可补充。"}


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--worker", action="store_true")
    parser.add_argument("--pdf", type=Path)
    parser.add_argument("--destination", type=Path, required=True)
    parser.add_argument("--sha256")
    parser.add_argument("--max-pages", type=int, default=24)
    parser.add_argument("--deadline-seconds", type=float, default=45)
    parser.add_argument("--no-ocr", action="store_true")
    args = parser.parse_args()
    if not args.worker:
        parser.error("Use extract_candidates() to bind a complete selected manifest")
    try:
        value = _extract_one(args.pdf, args.destination, args.sha256, max_pages=args.max_pages,
                             ocr=not args.no_ocr, deadline_seconds=args.deadline_seconds)
        print(json.dumps(value))
    except Exception as exc:
        print(json.dumps({"error": str(exc) if str(exc) in {"ocr_page_limit", "original_hash_mismatch", "no_substantive_source_text", "source_deadline_exceeded"} else "source_extraction_failed"}))
        raise SystemExit(1)


if __name__ == "__main__":
    main()
