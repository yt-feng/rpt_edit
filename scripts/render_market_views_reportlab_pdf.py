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

ROUNDUP_SOURCE_ORDER = ["bank_research", "consulting", "institution"]
EXTERNAL_SOURCE_GROUPS = {"institution", "consulting"}
SOURCE_GROUP_LABELS = {
    "bank_research": "投行/券商",
    "consulting": "战略咨询",
    "institution": "智库/国际机构",
}
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
                pdfmetrics.registerFont(TTFont("PORTAL_CJK", path))
                return "PORTAL_CJK"
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
        img.hAlign = "CENTER"
        return img
    except Exception as exc:
        log(f"Skip image {path}: {exc}")
        return None


def repo_asset_path(summary_dir: Path, relative_path: str) -> Path:
    candidates = [
        Path(relative_path),
        summary_dir / relative_path,
        summary_dir.parent / relative_path,
        summary_dir.parent.parent / relative_path,
    ]
    for candidate in candidates:
        if candidate.exists():
            return candidate
    return candidates[0]


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


def report_source_group(report: dict[str, Any]) -> str:
    value = str(report.get("source_group") or "").strip()
    if value:
        return value
    path = str(report.get("path") or "").lower()
    if "/institutions/" in path:
        return "institution"
    if "/consulting/" in path:
        return "consulting"
    return "bank_research"


def report_source_label(report: dict[str, Any]) -> str:
    group = report_source_group(report)
    return clean_plain(report.get("source_label") or SOURCE_GROUP_LABELS.get(group, group or "未知来源"))


def report_source_name(report: dict[str, Any]) -> str:
    value = clean_plain(report.get("institution_name") or report.get("source_name") or "")
    if value:
        return value
    if report_source_group(report) in EXTERNAL_SOURCE_GROUPS:
        title = clean_plain(report.get("title") or "")
        if "：" in title:
            prefix = title.split("：", 1)[0].strip()
            if 1 <= len(prefix) <= 12:
                return prefix
    return report_source_label(report)


def report_bank_name(report: dict[str, Any]) -> str:
    raw_name = clean_plain(report.get("institution_name") or report.get("source_name") or "")
    title = clean_plain(report.get("title") or "")
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


def external_section_map(summary: dict[str, Any]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    roundup = summary.get("external_roundup") or {}
    if not isinstance(roundup, dict):
        return mapping
    for category in roundup.get("categories") or []:
        if not isinstance(category, dict):
            continue
        heading = clean_plain(category.get("heading") or "外部研究补充")
        for item in category.get("items") or []:
            if not isinstance(item, dict):
                continue
            rid = str(item.get("report_id") or item.get("id") or "")
            if not rid:
                continue
            mapping.setdefault(rid, [])
            label = "外部：" + heading
            if label not in mapping[rid]:
                mapping[rid].append(label)
    return mapping


def combined_categories(report_id: str, main_map: dict[str, list[str]], ext_map: dict[str, list[str]]) -> str:
    values = []
    for category in main_map.get(report_id, []) + ext_map.get(report_id, []):
        if category not in values:
            values.append(category)
    return " / ".join(values or ["未被主题摘要引用"])


def figure_ids_for_report(figures: dict[str, dict[str, Any]], report_id: str, limit: int = 1) -> list[str]:
    matching = [
        fig for fig in figures.values()
        if str(fig.get("report_id") or "") == report_id and fig.get("figure_type") != "external_card"
    ]
    ids: list[str] = []
    for fig in matching:
        fid = str(fig.get("figure_id") or "")
        if fid and fid not in ids:
            ids.append(fid)
        if len(ids) >= limit:
            break
    return ids


def first_signal(text: str, max_chars: int = 96) -> str:
    paragraphs = extract_paragraphs(text, max_paragraphs=3)
    if not paragraphs:
        return "该报告提供了一条需要纳入今日市场判断的新增信号。"
    sentence = re.split(r"(?<=[。.!?！？])\s+", paragraphs[0])[0]
    if len(sentence) > max_chars:
        sentence = sentence[:max_chars].rstrip() + "..."
    return sentence


def fallback_external_roundup(reports: dict[str, dict[str, Any]], figures: dict[str, dict[str, Any]]) -> dict[str, Any]:
    items = []
    for report_id, report in reports.items():
        if report_source_group(report) not in EXTERNAL_SOURCE_GROUPS:
            continue
        items.append({
            "report_id": report_id,
            "institution": report_source_name(report),
            "title": clean_plain(report.get("title") or ""),
            "signal": first_signal(report.get("extract") or report.get("digest") or ""),
            "market_relevance": "用于补充投行观点之外的政策、产业、地缘或长期结构变量。",
            "figure_ids": figure_ids_for_report(figures, report_id, limit=1),
        })
        if len(items) >= 24:
            break
    return {
        "title": "外部机构与咨询信号",
        "summary": "这些来源用于补充投行观点之外的政策、产业、地缘和长期结构变量。",
        "categories": [{"heading": "外部研究补充", "items": items}] if items else [],
    }


def external_roundup(summary: dict[str, Any], reports: dict[str, dict[str, Any]], figures: dict[str, dict[str, Any]]) -> dict[str, Any]:
    roundup = summary.get("external_roundup")
    if not isinstance(roundup, dict) or not isinstance(roundup.get("categories"), list) or not roundup.get("categories"):
        return fallback_external_roundup(reports, figures)
    clean_categories: list[dict[str, Any]] = []
    item_total = 0
    for category in roundup.get("categories") or []:
        if not isinstance(category, dict):
            continue
        items = []
        for item in category.get("items") or []:
            if not isinstance(item, dict) or item_total >= 24:
                continue
            report_id = str(item.get("report_id") or item.get("id") or "")
            report = reports.get(report_id)
            if not report or report_source_group(report) not in EXTERNAL_SOURCE_GROUPS:
                continue
            fig_ids = [str(fid) for fid in (item.get("figure_ids") or []) if str(fid)]
            if not fig_ids:
                fig_ids = figure_ids_for_report(figures, report_id, limit=1)
            items.append({
                "report_id": report_id,
                "institution": clean_plain(item.get("institution") or report_source_name(report)),
                "title": clean_plain(item.get("title") or report.get("title") or ""),
                "signal": clean_plain(item.get("signal") or first_signal(report.get("extract") or report.get("digest") or "")),
                "market_relevance": clean_plain(item.get("market_relevance") or "用于补充投行观点之外的政策、产业、地缘或长期结构变量。"),
                "figure_ids": fig_ids[:2],
            })
            item_total += 1
        if items:
            clean_categories.append({"heading": clean_plain(category.get("heading") or "外部研究补充"), "items": items})
    if not clean_categories:
        return fallback_external_roundup(reports, figures)
    return {
        "title": clean_plain(roundup.get("title") or "外部机构与咨询信号"),
        "summary": clean_plain(roundup.get("summary") or "这些来源用于补充投行观点之外的政策、产业、地缘和长期结构变量。"),
        "categories": clean_categories,
    }


def source_roundup_map(source_roundups: list[dict[str, Any]]) -> dict[str, list[str]]:
    mapping: dict[str, list[str]] = {}
    for roundup in source_roundups:
        if not isinstance(roundup, dict):
            continue
        source_title = clean_plain(roundup.get("title") or SOURCE_GROUP_LABELS.get(str(roundup.get("source_group") or ""), "来源"))
        for theme in roundup.get("themes") or []:
            if not isinstance(theme, dict):
                continue
            heading = clean_plain(theme.get("heading") or "未归类")
            label = f"{source_title} / {heading}"
            for ref_id in theme.get("references") or []:
                rid = str(ref_id)
                mapping.setdefault(rid, [])
                if label not in mapping[rid]:
                    mapping[rid].append(label)
    return mapping


def fallback_source_roundup(source_group: str, reports: dict[str, dict[str, Any]], figures: dict[str, dict[str, Any]]) -> dict[str, Any]:
    source_reports = [(rid, report) for rid, report in reports.items() if report_source_group(report) == source_group]
    label = SOURCE_GROUP_LABELS.get(source_group, source_group)
    if not source_reports:
        return {"source_group": source_group, "title": label, "summary": "今日暂无新增报告。", "themes": []}

    refs = [rid for rid, _ in source_reports]
    bullet_limit = len(source_reports) if source_group in EXTERNAL_SOURCE_GROUPS else min(10, len(source_reports))
    bullets = [first_signal(report.get("extract") or report.get("digest") or "") for _, report in source_reports[:bullet_limit]]
    figure_ids: list[str] = []
    for rid, _ in source_reports:
        for fig_id in figure_ids_for_report(figures, rid, limit=1):
            if fig_id not in figure_ids:
                figure_ids.append(fig_id)
            if len(figure_ids) >= 3:
                break
        if len(figure_ids) >= 3:
            break
    return {
        "source_group": source_group,
        "title": label,
        "summary": f"今日纳入 {len(source_reports)} 篇，折叠为一个来源板块。",
        "themes": [{
            "heading": "今日主线",
            "thesis": "用于观察该来源今日最集中的叙事、数据和边际变化。",
            "bullets": bullets,
            "figure_ids": figure_ids,
            "references": refs,
        }],
    }


def source_roundups(summary: dict[str, Any], reports: dict[str, dict[str, Any]], figures: dict[str, dict[str, Any]]) -> list[dict[str, Any]]:
    raw_roundups = summary.get("source_roundups")
    raw_by_group: dict[str, dict[str, Any]] = {}
    if isinstance(raw_roundups, list):
        for raw in raw_roundups:
            if not isinstance(raw, dict):
                continue
            group = str(raw.get("source_group") or "")
            if group in ROUNDUP_SOURCE_ORDER and group not in raw_by_group:
                raw_by_group[group] = raw

    normalized: list[dict[str, Any]] = []
    for group in ROUNDUP_SOURCE_ORDER:
        raw = raw_by_group.get(group)
        if not raw:
            normalized.append(fallback_source_roundup(group, reports, figures))
            continue
        themes = []
        source_ids = {rid for rid, report in reports.items() if report_source_group(report) == group}
        for theme in raw.get("themes") or []:
            if not isinstance(theme, dict):
                continue
            refs = [str(ref) for ref in (theme.get("references") or []) if str(ref) in source_ids]
            fig_ids = [str(fig_id) for fig_id in (theme.get("figure_ids") or []) if str(fig_id) in figures]
            bullets = [clean_plain(bullet) for bullet in (theme.get("bullets") or []) if clean_plain(bullet)]
            if refs or bullets:
                themes.append({
                    "heading": clean_plain(theme.get("heading") or "未命名主题"),
                    "thesis": clean_plain(theme.get("thesis") or ""),
                    "bullets": bullets[:6],
                    "figure_ids": fig_ids[:3],
                    "references": refs,
                })
        if not themes and source_ids:
            normalized.append(fallback_source_roundup(group, reports, figures))
            continue
        roundup = {
            "source_group": group,
            "title": clean_plain(raw.get("title") or SOURCE_GROUP_LABELS.get(group, group)),
            "summary": clean_plain(raw.get("summary") or ""),
            "themes": themes,
        }
        if not source_ids:
            roundup["summary"] = "今日暂无新增报告。"
        elif not roundup["summary"]:
            roundup["summary"] = f"今日纳入 {len(source_ids)} 篇，整合为 {len(themes)} 个主题。"
        missing = [rid for rid in source_ids if rid not in source_roundup_map([roundup])]
        if missing:
            themes.append({
                "heading": "补充信号",
                "thesis": "以下观点补齐本来源中尚未进入前述主题的新增研究。",
                "bullets": [first_signal(reports[rid].get("extract") or reports[rid].get("digest") or "", max_chars=130) for rid in missing],
                "figure_ids": [],
                "references": missing,
            })
        normalized.append(roundup)
    return normalized


def clean_list(value: Any, limit: int = 0) -> list[str]:
    if not isinstance(value, list):
        return []
    items = [clean_plain(item) for item in value if clean_plain(item)]
    return items[:limit] if limit > 0 else items


def fallback_bank_view(report_id: str, report: dict[str, Any]) -> dict[str, Any]:
    view = first_signal(report.get("extract") or report.get("digest") or "", max_chars=180)
    title = clean_plain(report.get("title") or "")
    if view == title or title.startswith(view):
        paragraphs = extract_paragraphs(report.get("extract") or report.get("digest") or "", max_paragraphs=4)
        view = next((paragraph for paragraph in paragraphs if paragraph != title and not title.startswith(paragraph)), view)
        if len(view) > 180:
            view = view[:180].rstrip() + "..."
    return {
        "bank": report_bank_name(report),
        "view": view,
        "data_points": [],
        "marginal_change": "",
        "report_ids": [report_id],
    }


def normalized_bank_roundup(
    summary: dict[str, Any],
    reports: dict[str, dict[str, Any]],
    figures: dict[str, dict[str, Any]],
) -> dict[str, Any]:
    bank_ids = {report_id for report_id, report in reports.items() if report_source_group(report) == "bank_research"}
    raw_roundup = summary.get("bank_roundup")
    if not isinstance(raw_roundup, dict) or not isinstance(raw_roundup.get("sections"), list):
        grouped = source_roundups(summary, reports, figures)
        bank_source = next((item for item in grouped if item.get("source_group") == "bank_research"), None)
        bank_source = bank_source or fallback_source_roundup("bank_research", reports, figures)
        sections = []
        for theme in bank_source.get("themes") or []:
            refs = [str(ref) for ref in theme.get("references") or [] if str(ref) in bank_ids]
            sections.append({
                "heading": clean_plain(theme.get("heading") or "投行市场主线"),
                "thesis": clean_plain(theme.get("thesis") or ""),
                "consensus": clean_list(theme.get("bullets") or []),
                "divergences": [],
                "bank_views": [fallback_bank_view(report_id, reports[report_id]) for report_id in refs],
                "data_points": [],
                "figure_ids": [str(fig_id) for fig_id in theme.get("figure_ids") or [] if str(fig_id) in figures][:4],
                "references": refs,
            })
        return {
            "title": "全球投行叙事汇编",
            "summary": clean_plain(bank_source.get("summary") or f"今日纳入 {len(bank_ids)} 篇投行研究。"),
            "sections": sections,
        }

    sections = []
    for raw_section in raw_roundup.get("sections") or []:
        if not isinstance(raw_section, dict):
            continue
        refs = [str(ref) for ref in raw_section.get("references") or [] if str(ref) in bank_ids]
        views = []
        covered: set[str] = set()
        for raw_view in raw_section.get("bank_views") or []:
            if not isinstance(raw_view, dict):
                continue
            view_ids = [
                str(report_id)
                for report_id in raw_view.get("report_ids") or []
                if str(report_id) in bank_ids and str(report_id) not in covered
            ]
            if not view_ids:
                continue
            views.append({
                "bank": clean_plain(raw_view.get("bank") or report_bank_name(reports[view_ids[0]])),
                "view": clean_plain(raw_view.get("view") or first_signal(reports[view_ids[0]].get("extract") or "", max_chars=180)),
                "data_points": clean_list(raw_view.get("data_points") or [], 4),
                "marginal_change": clean_plain(raw_view.get("marginal_change") or ""),
                "report_ids": view_ids,
            })
            covered.update(view_ids)
        for report_id in refs:
            if report_id not in covered:
                views.append(fallback_bank_view(report_id, reports[report_id]))
                covered.add(report_id)
        sections.append({
            "heading": clean_plain(raw_section.get("heading") or "投行市场主线"),
            "thesis": clean_plain(raw_section.get("thesis") or ""),
            "consensus": clean_list(raw_section.get("consensus") or raw_section.get("bullets") or [], 6),
            "divergences": clean_list(raw_section.get("divergences") or [], 5),
            "bank_views": views,
            "data_points": clean_list(raw_section.get("data_points") or [], 10),
            "figure_ids": [str(fig_id) for fig_id in raw_section.get("figure_ids") or [] if str(fig_id) in figures][:4],
            "references": refs,
        })
    return {
        "title": clean_plain(raw_roundup.get("title") or "全球投行叙事汇编"),
        "summary": clean_plain(raw_roundup.get("summary") or f"今日纳入 {len(bank_ids)} 篇投行研究。"),
        "sections": sections,
    }


def normalized_supporting_roundups(
    summary: dict[str, Any],
    reports: dict[str, dict[str, Any]],
    figures: dict[str, dict[str, Any]],
) -> list[dict[str, Any]]:
    raw_supporting = summary.get("supporting_roundups")
    if isinstance(raw_supporting, list):
        grouped = source_roundups({"source_roundups": raw_supporting}, reports, figures)
    else:
        grouped = source_roundups(summary, reports, figures)
    return [roundup for roundup in grouped if roundup.get("source_group") in ("consulting", "institution")]


def coverage_sentence(report_ids: list[Any], reports: dict[str, dict[str, Any]], bank_only: bool = False) -> str:
    valid_reports = []
    for report_id in report_ids:
        report = reports.get(str(report_id))
        if not report or (bank_only and report_source_group(report) != "bank_research"):
            continue
        valid_reports.append(report)
    names: list[str] = []
    for report in valid_reports:
        name = report_bank_name(report) if report_source_group(report) == "bank_research" else report_source_name(report)
        if name and name not in names:
            names.append(name)
    institution_text = "、".join(names[:10])
    if len(names) > 10:
        institution_text += "等"
    suffix = f"；涉及 {institution_text}" if institution_text else ""
    return f"本节综合 {len(valid_reports)} 篇研究{suffix}。"


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
        if style_name == "PortalH1":
            self.notify("TOCEntry", (0, flowable.getPlainText(), self.page))
        elif style_name == "PortalH2":
            self.notify("TOCEntry", (1, flowable.getPlainText(), self.page))


def build_pdf(summary_dir: Path, output_pdf: Path) -> None:
    font = register_cjk_font()
    summary = load_json(summary_dir / "market_views_structured.json")
    reports = {item["id"]: item for item in load_json(summary_dir / "report_inputs.json")}
    figures = {
        item["figure_id"]: item
        for item in load_json(summary_dir / "figure_candidates.json")
        if item.get("figure_type") != "external_card"
    }
    bank_roundup = normalized_bank_roundup(summary, reports, figures)
    supporting_roundups = normalized_supporting_roundups(summary, reports, figures)
    cta_path = repo_asset_path(summary_dir, "prompts/zsxq_img.jpg")
    if not cta_path.exists():
        raise RuntimeError(f"Required Market Views ending image is missing: {cta_path}")

    styles = getSampleStyleSheet()
    styles.add(ParagraphStyle(name="PortalTitle", fontName=font, fontSize=22, leading=28, alignment=TA_CENTER, spaceAfter=10))
    styles.add(ParagraphStyle(name="PortalSubtitle", fontName=font, fontSize=11, leading=15, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=18))
    styles.add(ParagraphStyle(name="PortalTocTitle", fontName=font, fontSize=15, leading=20, spaceBefore=10, spaceAfter=8))
    styles.add(ParagraphStyle(name="PortalH1", fontName=font, fontSize=15, leading=20, spaceBefore=14, spaceAfter=8))
    styles.add(ParagraphStyle(name="PortalH2", fontName=font, fontSize=11.5, leading=15, spaceBefore=10, spaceAfter=5))
    styles.add(ParagraphStyle(name="PortalH3", fontName=font, fontSize=10.2, leading=14, spaceBefore=8, spaceAfter=4, textColor=colors.HexColor("#344054")))
    styles.add(ParagraphStyle(name="PortalBody", fontName=font, fontSize=10.5, leading=16, spaceAfter=7))
    styles.add(ParagraphStyle(name="PortalBankView", fontName=font, fontSize=9.8, leading=15, leftIndent=8, firstLineIndent=-8, spaceAfter=7, textColor=colors.HexColor("#1F2937")))
    styles.add(ParagraphStyle(name="PortalLabel", fontName=font, fontSize=9, leading=12, textColor=colors.HexColor("#475467"), spaceBefore=7, spaceAfter=4))
    styles.add(ParagraphStyle(name="PortalRef", fontName=font, fontSize=8, leading=11, textColor=colors.HexColor("#777777"), spaceBefore=4, spaceAfter=10))
    styles.add(ParagraphStyle(name="PortalSmall", fontName=font, fontSize=8.5, leading=12, textColor=colors.HexColor("#666666"), spaceAfter=5))
    styles.add(ParagraphStyle(name="PortalCardTitle", fontName=font, fontSize=10, leading=13, textColor=colors.HexColor("#1F2937"), spaceBefore=5, spaceAfter=3))
    styles.add(ParagraphStyle(name="PortalCardBody", fontName=font, fontSize=8.8, leading=12.2, textColor=colors.HexColor("#374151"), spaceAfter=3))
    styles.add(ParagraphStyle(name="PortalTag", fontName=font, fontSize=7.8, leading=10.5, textColor=colors.HexColor("#667085"), spaceAfter=2))
    styles.add(ParagraphStyle(name="PortalCaption", fontName=font, fontSize=8.2, leading=11, textColor=colors.HexColor("#555555"), alignment=TA_CENTER, spaceAfter=8))
    styles.add(ParagraphStyle(name="PortalDisclaimer", fontName=font, fontSize=6.8, leading=9.2, textColor=colors.HexColor("#777777"), alignment=TA_LEFT, spaceAfter=5))
    styles.add(ParagraphStyle(name="PortalCTA", fontName=font, fontSize=16, leading=22, alignment=TA_CENTER, textColor=colors.HexColor("#111827"), spaceAfter=12))
    styles.add(ParagraphStyle(name="PortalTocLevel0", fontName=font, fontSize=10, leading=14, leftIndent=0, firstLineIndent=0, spaceBefore=4))
    styles.add(ParagraphStyle(name="PortalTocLevel1", fontName=font, fontSize=8.5, leading=11.5, leftIndent=16, firstLineIndent=0, textColor=colors.HexColor("#666666")))

    def draw_page(canvas: Any, doc: Any) -> None:
        canvas.saveState()
        canvas.setFont(font, 7.5)
        canvas.setFillColor(colors.HexColor("#888888"))
        canvas.drawString(doc.leftMargin, 0.75 * cm, "Portal Suite - Market Views")
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

    def append_figures(figure_ids: list[Any], max_count: int) -> None:
        rendered = 0
        for raw_figure_id in figure_ids:
            if rendered >= max_count:
                break
            figure = figures.get(str(raw_figure_id))
            if not figure:
                continue
            image_path = summary_dir / figure.get("latex_path", "")
            image = image_flowable(image_path, max_width=15.2 * cm, max_height=8.2 * cm)
            if not image:
                continue
            story.append(Spacer(1, 0.12 * cm))
            story.append(image)
            caption = f"{figure.get('label', 'Figure')} - {str(figure.get('context', ''))}"
            story.append(Paragraph(clean_text(caption), styles["PortalCaption"]))
            rendered += 1

    source_counts = {
        group: sum(1 for report in reports.values() if report_source_group(report) == group)
        for group in ROUNDUP_SOURCE_ORDER
    }
    selected_figure_ids = {
        str(figure_id)
        for section in bank_roundup.get("sections") or []
        for figure_id in section.get("figure_ids") or []
    }
    selected_figure_ids.update(
        str(figure_id)
        for roundup in supporting_roundups
        for theme in roundup.get("themes") or []
        for figure_id in theme.get("figure_ids") or []
    )
    story.append(Paragraph(clean_text(summary.get("title") or "Market Views｜全球投行叙事汇编"), styles["PortalTitle"]))
    story.append(Paragraph(clean_text(summary.get("subtitle") or "Daily market views roundup"), styles["PortalSubtitle"]))
    story.append(Paragraph(
        clean_text(
            f"投行/券商 {source_counts['bank_research']} 篇 | 战略咨询 {source_counts['consulting']} 篇 | "
            f"智库/国际机构 {source_counts['institution']} 篇 | 正文原始图表 {len(selected_figure_ids)} 张 | 日期 {summary_dir.name}"
        ),
        styles["PortalRef"],
    ))
    story.append(Spacer(1, 0.2 * cm))
    story.append(Paragraph("目录", styles["PortalTocTitle"]))
    toc = TableOfContents()
    toc.levelStyles = [styles["PortalTocLevel0"], styles["PortalTocLevel1"]]
    story.append(toc)
    story.append(PageBreak())

    story.append(Paragraph("一页摘要", styles["PortalH1"]))
    for item in summary.get("executive_summary", []):
        story.append(Paragraph("- " + clean_text(item), styles["PortalBody"]))

    story.append(PageBreak())
    story.append(Paragraph(clean_text(bank_roundup.get("title") or "全球投行叙事汇编"), styles["PortalH1"]))
    if bank_roundup.get("summary"):
        story.append(Paragraph(clean_text(bank_roundup.get("summary")), styles["PortalSmall"]))

    for section_index, section in enumerate(bank_roundup.get("sections") or []):
        if section_index > 0:
            story.append(PageBreak())
        heading_block = [Paragraph(clean_text(section.get("heading") or "投行市场主线"), styles["PortalH2"])]
        if section.get("thesis"):
            heading_block.append(Paragraph("<b>" + clean_text(section.get("thesis")) + "</b>", styles["PortalBody"]))
        story.append(KeepTogether(heading_block))

        if section.get("consensus"):
            story.append(Paragraph("<b>主流共识</b>", styles["PortalLabel"]))
            for point in section.get("consensus") or []:
                story.append(Paragraph("- " + clean_text(point), styles["PortalBody"]))
        if section.get("divergences"):
            story.append(Paragraph("<b>分歧与条件差异</b>", styles["PortalLabel"]))
            for point in section.get("divergences") or []:
                story.append(Paragraph("- " + clean_text(point), styles["PortalBody"]))

        story.append(Paragraph("<b>机构观点</b>", styles["PortalLabel"]))
        for view in section.get("bank_views") or []:
            bank = clean_text(view.get("bank") or "投行")
            body = clean_text(view.get("view") or "")
            story.append(Paragraph(f"<b>{bank}</b>｜{body}", styles["PortalBankView"]))
            for data_point in view.get("data_points") or []:
                story.append(Paragraph("数据：" + clean_text(data_point), styles["PortalSmall"]))
            if view.get("marginal_change"):
                story.append(Paragraph("边际变化：" + clean_text(view.get("marginal_change")), styles["PortalSmall"]))

        if section.get("data_points"):
            story.append(Paragraph("<b>关键数据</b>", styles["PortalLabel"]))
            for data_point in section.get("data_points") or []:
                story.append(Paragraph("- " + clean_text(data_point), styles["PortalBody"]))

        append_figures(section.get("figure_ids") or [], 4)
        story.append(Paragraph(
            clean_text(coverage_sentence(section.get("references") or [], reports, bank_only=True)),
            styles["PortalRef"],
        ))

    for roundup in supporting_roundups:
        story.append(PageBreak())
        title = roundup.get("title") or SOURCE_GROUP_LABELS.get(str(roundup.get("source_group") or ""), "辅助信号")
        story.append(Paragraph(clean_text("辅助信号｜" + str(title)), styles["PortalH1"]))
        if roundup.get("summary"):
            story.append(Paragraph(clean_text(roundup.get("summary")), styles["PortalSmall"]))
        if not roundup.get("themes"):
            story.append(Paragraph("- " + clean_text(roundup.get("summary") or "今日暂无新增报告。"), styles["PortalBody"]))
        for theme in roundup.get("themes") or []:
            block = [Paragraph(clean_text(theme.get("heading") or "辅助研究主题"), styles["PortalH2"])]
            if theme.get("thesis"):
                block.append(Paragraph("<b>" + clean_text(theme.get("thesis")) + "</b>", styles["PortalBody"]))
            story.append(KeepTogether(block))
            for bullet in theme.get("bullets") or []:
                story.append(Paragraph("- " + clean_text(bullet), styles["PortalBody"]))
            append_figures(theme.get("figure_ids") or [], 2)
            story.append(Paragraph(
                clean_text(coverage_sentence(theme.get("references") or [], reports)),
                styles["PortalRef"],
            ))

    if summary.get("closing"):
        story.append(Paragraph("结语", styles["PortalH1"]))
        story.append(Paragraph(clean_text(summary.get("closing")), styles["PortalBody"]))

    story.append(PageBreak())
    story.append(Paragraph("覆盖概览", styles["PortalH1"]))
    story.append(Paragraph(
        clean_text(
            f"今日共纳入 {len(reports)} 篇研究，其中投行/券商 {source_counts['bank_research']} 篇，"
            f"战略咨询 {source_counts['consulting']} 篇，智库/国际机构 {source_counts['institution']} 篇。"
        ),
        styles["PortalBody"],
    ))
    bank_counts: dict[str, int] = {}
    for report in reports.values():
        if report_source_group(report) != "bank_research":
            continue
        name = report_bank_name(report)
        bank_counts[name] = bank_counts.get(name, 0) + 1
    if bank_counts:
        bank_mix = " / ".join(f"{name} {count}篇" for name, count in sorted(bank_counts.items(), key=lambda item: (-item[1], item[0])))
        story.append(Paragraph(clean_text("投行覆盖：" + bank_mix), styles["PortalBody"]))
    story.append(Paragraph("<b>主题分布</b>", styles["PortalLabel"]))
    for section in bank_roundup.get("sections") or []:
        story.append(Paragraph(
            "- " + clean_text(f"{section.get('heading') or '投行主题'}：{len(section.get('references') or [])} 篇"),
            styles["PortalBody"],
        ))

    story.append(PageBreak())
    story.append(Paragraph("Disclaimer", styles["PortalH1"]))
    for paragraph in DISCLAIMER_TEXT.split("\n\n"):
        story.append(Paragraph(clean_text(paragraph), styles["PortalDisclaimer"]))

    story.append(PageBreak())
    story.append(Spacer(1, 0.8 * cm))
    story.append(Paragraph("更多详情报告portal.example.invalid", styles["PortalCTA"]))
    cta_image = image_flowable(cta_path, max_width=10.5 * cm, max_height=12.5 * cm)
    if not cta_image:
        raise RuntimeError(f"Could not render required Market Views ending image: {cta_path}")
    story.append(cta_image)

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
