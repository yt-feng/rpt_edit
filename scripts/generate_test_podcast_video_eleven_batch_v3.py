#!/usr/bin/env python3
"""Boundary-aware mixed bilingual highlight patch.

This wrapper keeps the v2 visual logic but changes highlight selection/drawing so
Chinese mixed subtitles highlight complete phrases instead of arbitrary chopped
character runs such as "国内市场是主".
"""
from __future__ import annotations

import re
from typing import Any

import generate_test_podcast_video_eleven_batch_v2 as v2

BAD_PREFIX = set("的了和与及或但而并就却也都很更较最主要求对从在由为把被将其该此这那")
BAD_SUFFIX = set("的是在为由从对和与及或但而并就也都很更较最主非有中上下一这那其该")
BAD_TERMS = {
    "没错", "是的", "好的", "那么", "这个", "一个", "我们", "他们", "报告", "指出", "显示",
    "市场", "如果", "但是", "所以", "还是", "非常", "已经", "可以", "需要", "政策环境",
}
PREFERRED_ZH_TERMS = [
    "国内市场", "主要拖累", "出口增长", "同比增长", "环比增长", "出口量", "中国GDP", "GDP",
    "人民币", "中间价", "汇率", "央行", "反应函数", "政策干预", "政策力度", "基准情景",
    "分析框架", "估值框架", "供应链", "库存周期", "原油供应", "通胀预期", "AI算力", "云厂商",
    "需求回暖", "供给收缩", "盈利修复", "风险偏好", "利润率", "现金流", "订单增速",
]
TAIL_PATTERNS = [
    "增长", "下降", "拖累", "改善", "走强", "走弱", "回落", "反弹", "修复", "压力", "风险",
    "趋势", "框架", "信号", "模型", "需求", "供给", "库存", "出口", "进口", "利率", "汇率",
    "收入", "利润", "成本", "销量", "价格", "产能", "周期", "弹性", "假设",
]


def has_cjk(text: str) -> bool:
    return bool(re.search(r"[\u4e00-\u9fff]", text or ""))


def is_awkward_partial(line: str, term: str) -> bool:
    """Reject substrings that look like they were cut from a longer phrase."""
    if not term or term not in line:
        return True
    if term in BAD_TERMS:
        return True
    if not has_cjk(term):
        return False
    if len(term) < 2 or len(term) > 8:
        return True
    if term[0] in BAD_PREFIX or term[-1] in BAD_SUFFIX:
        return True
    for match in re.finditer(re.escape(term), line):
        before = line[match.start() - 1] if match.start() > 0 else ""
        after = line[match.end()] if match.end() < len(line) else ""
        if before and re.match(r"[\u4e00-\u9fff]", before) and term[0] in BAD_PREFIX:
            return True
        if after and re.match(r"[\u4e00-\u9fff]", after) and term[-1] in BAD_SUFFIX:
            return True
    return False


def add_candidate(out: list[str], text: str, item: str, limit: int) -> None:
    item = re.sub(r"^[，。！？；、,.;:：\s]+|[，。！？；、,.;:：\s]+$", "", item or "")
    item = item.strip()
    if not item or item in out or item in BAD_TERMS:
        return
    if item not in text:
        return
    if has_cjk(item) and is_awkward_partial(text, item):
        return
    out.append(item)


def fallback_zh_highlights(text: str, limit: int = 2) -> list[str]:
    text = v2.sanitize_sensitive_text(text, "zh")
    compact = re.sub(r"\s+", "", text)
    out: list[str] = []

    # 1) Prefer known complete finance / macro phrases when present.
    for term in PREFERRED_ZH_TERMS:
        if term in compact:
            add_candidate(out, compact, term, limit)
            if len(out) >= limit:
                return out[:limit]

    # 2) Numbers are complete units and should never be chopped.
    for num in re.findall(r"\d+(?:\.\d+)?%?", compact):
        add_candidate(out, compact, num, limit)
        if len(out) >= limit:
            return out[:limit]

    # 3) Split at punctuation/fillers, then extract complete clause chunks.
    clauses = [c for c in re.split(r"[。！？；，、,.;:：]\s*", compact) if c]
    for clause in clauses:
        clause = re.sub(r"^(没错|是的|好的|对|嗯|那么|其实|报告指出|报告显示)", "", clause)
        # A 是 B -> prefer A and B separately, not A+是+B partials.
        if "是" in clause:
            left, right = clause.split("是", 1)
            add_candidate(out, compact, left[-6:], limit)
            add_candidate(out, compact, right[:6], limit)
        if "为" in clause:
            left, right = clause.split("为", 1)
            add_candidate(out, compact, left[-6:], limit)
            add_candidate(out, compact, right[:6], limit)
        for tail in TAIL_PATTERNS:
            for match in re.finditer(rf"[\u4e00-\u9fff]{{2,6}}{tail}", clause):
                add_candidate(out, compact, match.group(0), limit)
                if len(out) >= limit:
                    return out[:limit]
        for token in re.findall(r"[A-Za-z][A-Za-z0-9._-]{1,}|[\u4e00-\u9fff]{2,4}", clause):
            add_candidate(out, compact, token, limit)
            if len(out) >= limit:
                return out[:limit]
    return out[:limit]


def draw_highlighted_line_local(
    draw: Any,
    line: str,
    terms: list[str],
    font: Any,
    x: int,
    y: int,
    normal_fill: tuple[int, int, int],
    highlight_fill: tuple[int, int, int] = v2.ACCENT,
) -> None:
    """Draw highlights only when the full phrase fits inside this rendered line."""
    cleaned_terms: list[str] = []
    for raw in terms:
        term = v2.sanitize_sensitive_text(str(raw), "zh" if has_cjk(str(raw)) else "en")
        if not term or term not in line:
            continue
        if has_cjk(term) and is_awkward_partial(line, term):
            continue
        if term not in cleaned_terms:
            cleaned_terms.append(term)

    # If every supplied term was rejected as a partial, pick a complete phrase from this line.
    if not cleaned_terms and has_cjk(line):
        cleaned_terms = [t for t in fallback_zh_highlights(line, 2) if t in line]

    chunks: list[tuple[str, bool]] = [(line, False)]
    for term in sorted(set(cleaned_terms), key=len, reverse=True):
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

    cursor = x
    for chunk, marked in chunks:
        draw.text((cursor, y), chunk, font=font, fill=highlight_fill if marked else normal_fill)
        cursor += v2.text_size(draw, chunk, font)[0]


def apply_boundary_patch() -> None:
    v2.fallback_zh_highlights = fallback_zh_highlights
    v2.draw_highlighted_line_local = draw_highlighted_line_local


def main() -> int:
    apply_boundary_patch()
    return v2.main()


if __name__ == "__main__":
    raise SystemExit(main())
