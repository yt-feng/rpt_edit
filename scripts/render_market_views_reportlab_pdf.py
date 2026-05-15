#!/usr/bin/env python3
"""Fast PDF renderer for market view summaries.

This renderer guarantees a PDF without installing TeX Live. It uses ReportLab's
built-in CJK CID font first, so Chinese text works even when Noto TTC font files
cannot be registered as TrueType fonts.
"""
from __future__ import annotations

import argparse
import json
import re
from pathlib import Path
from typing import Any

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import Image, KeepTogether, Paragraph, SimpleDocTemplate, Spacer
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"Missing reportlab dependency: {exc}. Please pip install reportlab.")


def log(message: str) -> None:
    print(message, flush=True)


def latest_date_dir(root: Path) -> Path:
    candidates = [p for p in root.iterdir() if p.is_dir() and re.match(r"^\d{6,8}$", p.name)]
    if not candidates:
        raise RuntimeError(f"No date-named market summary folders found under {root}")
    return max(candidates, key=lambda p: int(p.name))


def register_cjk_font() -> str:
    # ReportLab ships CID font support. This is much more reliable than trying
    # to register Linux .ttc collections via TTFont.
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception as exc:
        log(f"Could not register STSong-Light CID font: {exc}")

    # Last-resort TrueType fallback. Skip any font file ReportLab cannot parse.
    candidates = [
        "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf",
    ]
    for path in candidates:
        if Path(path).exists():
            try:
                pdfmetrics.registerFont(TTFont("KC_CJK", path))
                return "KC_CJK"
            except Exception as exc:
                log(f"Skip font {path}: {exc}")
    return "Helvetica"


def clean_text(value: Any) -> str:
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    # Escape a few XML-sensitive chars for ReportLab Paragraph.
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def load_json(path: Path) -> Any:
    return json.loads(path.read_text(encoding="utf-8"))


def image_flowable(path: Path, max_width: float, max_height: float) -> Image | None:
    if not path.exists():
        return None
    try:
        img = Image(str(path))
        ratio = min(max_width / img.imageWidth, max_height / img.imageHeight, 1.0)
        img.drawWidth = img.imageWidth * ratio
        img.drawHeight = img.imageHeight * ratio
        return img
    except Exception as exc:
        log(f"Skip image {path}: {exc}")
        return None


def build_pdf(summary_dir: Path, output_pdf: Path) -> None:
    font = register_cjk_font()
    summary = load_json(summary_dir / "market_views_structured.json")
    reports = {item["id"]: item for item in load_json(summary_dir / "report_inputs.json")}
    figures = {item["figure_id"]: item for item in load_json(summary_dir / "figure_candidates.json")}

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="KCTitle", fontName=font, fontSize=22, leading=28, alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name="KCSubtitle", fontName=font, fontSize=11, leading=15, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="KCH1", fontName=font, fontSize=15, leading=20, spaceBefore=14, spaceAfter=8))
    styles.add(ParagraphStyle(name="KCBody", fontName=font, fontSize=10.5, leading=16, spaceAfter=7))
    styles.add(ParagraphStyle(name="KCRef", fontName=font, fontSize=8, leading=11, textColor=colors.HexColor("#777777"), spaceBefore=4, spaceAfter=10))
    styles.add(ParagraphStyle(name="KCCaption", fontName=font, fontSize=8.2, leading=11, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=8))

    doc = SimpleDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=1.7 * cm,
        leftMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=clean_text(summary.get("title") or "市场最新观点汇总"),
    )
    story: list[Any] = []
    story.append(Paragraph(clean_text(summary.get("title") or "市场最新观点汇总"), styles["KCTitle"]))
    story.append(Paragraph(clean_text(summary.get("subtitle") or "Daily market views roundup"), styles["KCSubtitle"]))

    story.append(Paragraph("一页摘要", styles["KCH1"]))
    for item in summary.get("executive_summary", [])[:6]:
        story.append(Paragraph("• " + clean_text(item), styles["KCBody"]))

    for section in summary.get("sections", [])[:10]:
        block: list[Any] = []
        block.append(Paragraph(clean_text(section.get("heading") or "未命名板块"), styles["KCH1"]))
        if section.get("thesis"):
            block.append(Paragraph("<b>" + clean_text(section.get("thesis")) + "</b>", styles["KCBody"]))
        for bullet in (section.get("bullets") or [])[:8]:
            block.append(Paragraph("• " + clean_text(bullet), styles["KCBody"]))
        if block:
            story.append(KeepTogether(block[:2]))
            for item in block[2:]:
                story.append(item)

        for fig_id in (section.get("figure_ids") or [])[:2]:
            fig = figures.get(fig_id)
            if not fig:
                continue
            img_path = summary_dir / fig.get("latex_path", "")
            img = image_flowable(img_path, max_width=16 * cm, max_height=9.5 * cm)
            if img:
                story.append(Spacer(1, 0.15 * cm))
                story.append(img)
                caption = f"{fig.get('label', 'Exhibit')} - {str(fig.get('context', ''))[:220]}"
                story.append(Paragraph(clean_text(caption), styles["KCCaption"]))

        refs = []
        for ref_id in (section.get("references") or [])[:12]:
            report = reports.get(ref_id)
            if report:
                refs.append(f"[{ref_id}] {report.get('title', '')}")
        if refs:
            story.append(Paragraph("References: " + clean_text("; ".join(refs)), styles["KCRef"]))

    if summary.get("closing"):
        story.append(Paragraph("结语", styles["KCH1"]))
        story.append(Paragraph(clean_text(summary.get("closing")), styles["KCBody"]))

    story.append(Spacer(1, 0.4 * cm))
    story.append(Paragraph("Personal reading notes and learning share only. Not investment advice.", styles["KCRef"]))
    doc.build(story)
    if not output_pdf.exists() or output_pdf.stat().st_size < 1024:
        raise RuntimeError(f"PDF was not created or is too small: {output_pdf}")
    log(f"Fast PDF generated: {output_pdf} ({output_pdf.stat().st_size} bytes)")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--summary-root", default="market_view_summaries")
    parser.add_argument("--date-folder", default="latest")
    args = parser.parse_args()

    root = Path(args.summary_root)
    summary_dir = latest_date_dir(root) if args.date_folder == "latest" else root / args.date_folder
    if not summary_dir.exists():
        raise RuntimeError(f"Summary folder not found: {summary_dir}")
    output_pdf = summary_dir / f"market_views_{summary_dir.name}.pdf"
    build_pdf(summary_dir, output_pdf)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
