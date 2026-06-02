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
    from reportlab.lib.enums import TA_CENTER, TA_LEFT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import cm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.cidfonts import UnicodeCIDFont
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        Image,
        KeepTogether,
        PageBreak,
        PageTemplate,
        Paragraph,
        Spacer,
        Table,
        TableStyle,
    )
    from reportlab.platypus.tableofcontents import TableOfContents
except Exception as exc:  # pragma: no cover
    raise SystemExit(f"Missing reportlab dependency: {exc}. Please pip install reportlab.")


DISCLAIMER_TEXT = """This community is a paid learning and information-sharing community created for general educational purposes only. The membership fee is charged solely for access to community discussions, educational content, organization, and operational costs. It is not an advisory fee, management fee, performance fee, brokerage fee, or compensation for personalized financial, investment, legal, tax, or professional advice.

I participate and share information solely as an individual and for educational discussion among community members. I am not acting as a financial adviser, investment adviser, broker, dealer, portfolio manager, legal adviser, tax adviser, accountant, fiduciary, or any other licensed professional adviser. Nothing shared in this community constitutes, and should not be interpreted as, financial advice, investment advice, legal advice, tax advice, a recommendation, solicitation, offer, endorsement, instruction, or guarantee to buy, sell, hold, short, trade, or invest in any security, cryptocurrency, fund, derivative, strategy, or other financial product.

All content shared in this community, including messages, discussions, links, files, charts, examples, market commentary, watchlists, AI-generated or AI-polished summaries, and third-party materials, is general, impersonal, and educational in nature. It does not take into account any individual's financial situation, investment objectives, risk tolerance, investment horizon, liquidity needs, tax status, legal restrictions, or suitability requirements. No content should be relied upon as suitable for any specific person, account, portfolio, or financial decision.

Information shared in this community may be incomplete, inaccurate, outdated, speculative, AI-generated, AI-edited, or based on third-party internet sources that have not been independently verified. I make no representation or warranty as to the accuracy, completeness, timeliness, reliability, or suitability of any information shared.

Financial markets involve substantial risk, including the possible loss of principal. Past performance, historical data, hypothetical examples, simulated results, backtests, personal opinions, or educational examples do not guarantee future results. Each member is solely responsible for conducting their own research, exercising independent judgment, and making their own decisions. Before making any financial, investment, legal, or tax decision, members should consult qualified and licensed professionals.

Participation in this community, payment of any membership fee, or communication with me or other members does not create any adviser-client, fiduciary, professional, contractual, agency, partnership, employment, or other advisory relationship. By joining or participating in this community, you acknowledge and agree that you are solely responsible for your own decisions, actions, transactions, profits, losses, risks, and consequences, and that I shall not be liable for any direct, indirect, incidental, consequential, financial, legal, tax, or other loss or damage arising from or related to any content, discussion, information, or material shared in this community."""


def log(message: str) -> None:
    print(message, flush=True)


def latest_date_dir(root: Path) -> Path:
    candidates = [p for p in root.iterdir() if p.is_dir() and re.match(r"^\d{6,8}$", p.name)]
    if not candidates:
        raise RuntimeError(f"No date-named market summary folders found under {root}")
    return max(candidates, key=lambda p: int(p.name))


def register_cjk_font() -> str:
    try:
        pdfmetrics.registerFont(UnicodeCIDFont("STSong-Light"))
        return "STSong-Light"
    except Exception as exc:
        log(f"Could not register STSong-Light CID font: {exc}")
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
    return text.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")


def clean_plain(value: Any) -> str:
    return re.sub(r"\s+", " ", str(value or "")).strip()


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


def iter_figure_ids(section: dict[str, Any]) -> list[str]:
    ids = section.get("figure_ids") or []
    if not isinstance(ids, list):
        return []
    return [str(x) for x in ids if x]


def report_section_map(summary: dict[str, Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for section in summary.get("sections", []) or []:
        heading = clean_plain(section.get("heading") or "未归类")
        for ref_id in section.get("references", []) or []:
            rid = str(ref_id)
            mapping.setdefault(rid, [])
            if heading not in mapping[rid]:
                mapping[rid].append(heading)
    return mapping


def extract_paragraphs(text: str, max_paragraphs: int = 5) -> list[str]:
    text = str(text or "").replace("[... middle omitted ...]", " ")
    parts = [clean_plain(part) for part in re.split(r"\n{2,}", text) if clean_plain(part)]
    if len(parts) <= 1:
        parts = [clean_plain(part) for part in re.split(r"(?<=[。.!?！？])\s+", text) if clean_plain(part)]
    return [part for part in parts if len(part) >= 24][:max_paragraphs]


class MarketDocTemplate(BaseDocTemplate):
    def afterFlowable(self, flowable: Any) -> None:
        if not isinstance(flowable, Paragraph):
            return
        style_name = getattr(flowable.style, "name", "")
        if style_name == "KCH1":
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page))
        elif style_name == "KCH2":
            self.notify("TOCEntry", (1, flowable.getPlainText(), self.page))


def build_pdf(summary_dir: Path, output_pdf: Path) -> None:
    font = register_cjk_font()
    summary = load_json(summary_dir / "market_views_structured.json")
    reports = {item["id"]: item for item in load_json(summary_dir / "report_inputs.json")}
    figures = {item["figure_id"]: item for item in load_json(summary_dir / "figure_candidates.json")}
    section_map = report_section_map(summary)

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="KCTitle", fontName=font, fontSize=22, leading=28, alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name="KCSubtitle", fontName=font, fontSize=11, leading=15, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="KCTocTitle", fontName=font, fontSize=15, leading=20, spaceBefore=10, spaceAfter=8))
    styles.add(ParagraphStyle(name="KCH1", fontName=font, fontSize=15, leading=20, spaceBefore=14, spaceAfter=8))
    styles.add(ParagraphStyle(name="KCH2", fontName=font, fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle(name="KCBody", fontName=font, fontSize=10.5, leading=16, spaceAfter=7))
    styles.add(ParagraphStyle(name="KCRef", fontName=font, fontSize=8, leading=11, textColor=colors.HexColor("#777777"), spaceBefore=4, spaceAfter=10))
    styles.add(ParagraphStyle(name="KCSmall", fontName=font, fontSize=8.5, leading=12, textColor=colors.HexColor("#666666"), spaceAfter=5))
    styles.add(ParagraphStyle(name="KCCaption", fontName=font, fontSize=8.2, leading=11, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle(name="KCDisclaimer", fontName=font, fontSize=6.8, leading=9.2, textColor=colors.HexColor("#777777"), alignment=TA_LEFT, spaceAfter=5))
    styles.add(ParagraphStyle(name="KCTocLevel0", fontName=font, fontSize=10, leading=14, leftIndent=0, firstLineIndent=0, spaceBefore=4))
    styles.add(ParagraphStyle(name="KCTocLevel1", fontName=font, fontSize=8.5, leading=11.5, leftIndent=16, firstLineIndent=0, textColor=colors.HexColor("#666666")))

    def draw_page(canvas: Any, doc: Any) -> None:
        canvas.saveState()
        canvas.setFont(font, 7.5)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawString(doc.leftMargin, 0.75 * cm, "KC桌面 - Market Views")
        canvas.drawRightString(A4[0] - doc.rightMargin, 0.75 * cm, str(doc.page))
        canvas.restoreState()

    doc = MarketDocTemplate(
        str(output_pdf),
        pagesize=A4,
        rightMargin=1.7 * cm,
        leftMargin=1.7 * cm,
        topMargin=1.5 * cm,
        bottomMargin=1.5 * cm,
        title=clean_text(summary.get("title") or "市场最新观点汇总"),
    )
    frame = Frame(doc.leftMargin, doc.bottomMargin, doc.width, doc.height, id="normal")
    doc.addPageTemplates([PageTemplate(id="main", frames=[frame], onPage=draw_page)])

    story: list[Any] = []
    story.append(Paragraph(clean_text(summary.get("title") or "市场最新观点汇总"), styles["KCTitle"]))
    story.append(Paragraph(clean_text(summary.get("subtitle") or "Daily market views roundup"), styles["KCSubtitle"]))
    story.append(Paragraph(clean_text(f"覆盖报告：{len(reports)} 篇 | 图表候选：{len(figures)} 张 | 日期文件夹：{summary_dir.name}"), styles["KCRef"]))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("目录", styles["KCTocTitle"]))
    toc = TableOfContents()
    toc.levelStyles = [styles["KCTocLevel0"], styles["KCTocLevel1"]]
    story.append(toc)
    story.append(PageBreak())

    story.append(Paragraph("一页摘要", styles["KCH1"]))
    for item in summary.get("executive_summary", []):
        # Avoid the unicode bullet glyph; it rendered as a CJK character in some CID fonts.
        story.append(Paragraph("- " + clean_text(item), styles["KCBody"]))

    for section in summary.get("sections", []):
        block: list[Any] = []
        block.append(Paragraph(clean_text(section.get("heading") or "未命名板块"), styles["KCH1"]))
        if section.get("thesis"):
            block.append(Paragraph("<b>" + clean_text(section.get("thesis")) + "</b>", styles["KCBody"]))
        for bullet in (section.get("bullets") or []):
            block.append(Paragraph("- " + clean_text(bullet), styles["KCBody"]))
        if block:
            story.append(KeepTogether(block[:2]))
            for item in block[2:]:
                story.append(item)

        for fig_id in iter_figure_ids(section):
            fig = figures.get(fig_id)
            if not fig:
                continue
            img_path = summary_dir / fig.get("latex_path", "")
            img = image_flowable(img_path, max_width=16 * cm, max_height=9.5 * cm)
            if img:
                story.append(Spacer(1, 0.15 * cm))
                story.append(img)
                caption = f"{fig.get('label', 'Exhibit')} - {str(fig.get('context', ''))}"
                story.append(Paragraph(clean_text(caption), styles["KCCaption"]))

        refs = []
        for ref_id in (section.get("references") or []):
            report = reports.get(ref_id)
            if report:
                refs.append(f"[{ref_id}] {report.get('title', '')}")
        if refs:
            story.append(Paragraph("References: " + clean_text("; ".join(refs)), styles["KCRef"]))

    if summary.get("closing"):
        story.append(Paragraph("结语", styles["KCH1"]))
        story.append(Paragraph(clean_text(summary.get("closing")), styles["KCBody"]))

    story.append(PageBreak())
    story.append(Paragraph("报告覆盖清单", styles["KCH1"]))
    table_rows = [[Paragraph(clean_text("ID"), styles["KCRef"]), Paragraph(clean_text("归类"), styles["KCRef"]), Paragraph(clean_text("报告标题"), styles["KCRef"])]]
    for report_id, report in reports.items():
        categories = " / ".join(section_map.get(report_id, ["未被主题摘要引用"]))
        table_rows.append([
            Paragraph(clean_text(report_id), styles["KCRef"]),
            Paragraph(clean_text(categories), styles["KCRef"]),
            Paragraph(clean_text(report.get("title", "")), styles["KCRef"]),
        ])
    table = Table(table_rows, colWidths=[1.35 * cm, 4.2 * cm, 10.0 * cm], repeatRows=1, splitByRow=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.HexColor("#F2F4F7")),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.HexColor("#555555")),
        ("GRID", (0, 0), (-1, -1), 0.25, colors.HexColor("#DDDDDD")),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
    ]))
    story.append(table)

    story.append(PageBreak())
    story.append(Paragraph("逐篇报告摘录", styles["KCH1"]))
    story.append(Paragraph("以下摘录来自当天已完成 MinerU 解析和内容生成的报告文件夹，用于确认覆盖范围；主题摘要仍以开头各板块为准。", styles["KCSmall"]))
    for report_id, report in reports.items():
        categories = " / ".join(section_map.get(report_id, ["未被主题摘要引用"]))
        story.append(KeepTogether([
            Paragraph(clean_text(f"[{report_id}] {report.get('title', '')}"), styles["KCH2"]),
            Paragraph(clean_text("归类：" + categories), styles["KCSmall"]),
        ]))
        paragraphs = extract_paragraphs(report.get("extract") or report.get("digest") or "", max_paragraphs=5)
        for paragraph in paragraphs:
            story.append(Paragraph(clean_text(paragraph), styles["KCBody"]))

    story.append(PageBreak())
    story.append(Paragraph("Disclaimer", styles["KCH1"]))
    for paragraph in DISCLAIMER_TEXT.split("\n\n"):
        story.append(Paragraph(clean_text(paragraph), styles["KCDisclaimer"]))

    doc.multiBuild(story)
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
