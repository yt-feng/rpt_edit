"""Bound the readable edition, retaining all original evidence outside the PDF."""
from __future__ import annotations

from copy import deepcopy
import re

MAX_MODULES = 10
MAX_PAGES = 70


def concise(value, limit):
    text = re.sub(r"\s+", " ", str(value or "")).strip()
    if len(text) <= limit:
        return text
    ends = [m.end() for m in re.finditer(r"[。！？;；](?:\s|$)?", text[:limit])]
    return text[:ends[-1] if ends and ends[-1] >= limit // 2 else limit].rstrip() + "…"


def bound_roundups(bank, supporting, *, module_chars=4200, figures_per_module=4):
    """Editorial display budget only; never mutate source JSON or source refs."""
    bank, supporting = deepcopy(bank), deepcopy(supporting)
    modules = bank.get("sections", [])
    # Keep source groups visible while fitting one combined module budget.
    supporting = [item for item in supporting if item.get("themes")]
    capacity = max(1, MAX_MODULES - len(supporting))
    if len(modules) > capacity:
        retained = modules[:capacity - 1]
        merged = {"heading": "跨市场与行业研究", "thesis": "相关研究的主要信号与条件差异。",
                  "references": [], "bank_views": [], "consensus": [], "divergences": [],
                  "data_points": [], "figure_ids": [], "catalysts": []}
        for item in modules[capacity - 1:]:
            for key in ("references", "bank_views", "consensus", "divergences", "data_points", "figure_ids", "catalysts"):
                merged[key].extend(item.get(key) or [])
        merged["references"] = list(dict.fromkeys(merged["references"]))
        modules = retained + [merged]
        bank["sections"] = modules
    for module in modules:
        module["heading"] = concise(module.get("heading"), 60)
        module["thesis"] = concise(module.get("thesis"), 450)
        for key, count, chars in (("consensus", 4, 260), ("divergences", 3, 260),
                                  ("data_points", 5, 160), ("catalysts", 3, 180)):
            module[key] = [concise(item, chars) for item in (module.get(key) or [])[:count]]
        views = module.get("bank_views") or []
        # Institutions remain attributed; use less detail per institution on
        # busy days instead of silently dropping a report's source binding.
        view_budget = max(90, min(500, module_chars // max(len(views), 1)))
        for view in views:
            view["bank"] = concise(view.get("bank"), 55)
            view["view"] = concise(view.get("view"), view_budget)
            view["data_points"] = [concise(item, 120) for item in (view.get("data_points") or [])[:1]]
            view["marginal_change"] = concise(view.get("marginal_change"), 140)
        module["figure_ids"] = list(dict.fromkeys(module.get("figure_ids") or []))[:figures_per_module]
    for group in supporting:
        themes = group.get("themes") or []
        # The group is one top-level module; preserve every theme's references.
        each = max(100, module_chars // max(len(themes), 1))
        for index, theme in enumerate(themes):
            theme["heading"] = concise(theme.get("heading"), 60)
            theme["thesis"] = concise(theme.get("thesis"), min(each, 400))
            theme["bullets"] = [concise(item, min(each // 2, 180)) for item in (theme.get("bullets") or [])[:2]]
            theme["figure_ids"] = (theme.get("figure_ids") or [])[:1] if index < 3 else []
    return bank, supporting
