#!/usr/bin/env python3
"""Deterministic editorial guardrails for generated WeChat Markdown.

DeepSeek supplies the prose, but public-facing structure must not depend on the
model following every instruction.  This module removes model-written CTA and
meta sections at both generation and upload time.
"""
from __future__ import annotations

import re


WECHAT_EDITOR_SYSTEM_PROMPT = (
    "你是资深中文研究导读编辑。你的工作是从人工撰写的机构报告中挑出最有信息量的证据，"
    "写成克制、具体、可直接发布的短导读。保持原文限定条件，不编造，不模拟个人经历，"
    "不写推广、未解问题栏目或写作过程说明。只输出最终 Markdown。"
)

WECHAT_EDITORIAL_GUARD_ZH = """
【DeepSeek 交稿硬约束】
1. 全文只服务一个主判断。不要按原报告目录逐段摘要，也不要把多个结论平铺成清单。
2. 开头直接使用原文中最有辨识度的事实、数字、对比或矛盾切入；禁止用“在……背景下”“随着……”“近年来……”空泛起笔。
3. 正文至少使用三个原文锚点：一个可核验的数字或日期、一个具体主体/项目/制度名、一个比较或因果关系。判断必须紧挨证据，保留“可能、样本显示、报告认为”等限定词。
4. 句子长短要自然变化。大多数段落写 2-4 句，允许用一句短句收住；不要连续使用“报告指出、这意味着、换句话说、真正重要的是、值得注意的是”等模板转折。每个段落都必须以完整句结束，不得停在逗号、分号、冒号、连接词或半句话上。
5. KC评论只写一条具体、平白的解释或提醒，标签必须严格写成“KC评论”，不能写“编辑评论”；不能复述正文，不能提推广、原文领取、完整报告、读者行动或网站。
6. 禁止单独设置“该报告未解决的问题、报告尚未回答、研究留白、开放问题、报告局限、还需追问”等小节，也禁止用问句收尾。若原报告明确写了限制，只能在相关正文中用一句客观陈述自然带过。
7. 最后一段必须仍是实质内容或 KC评论。不要添加总结、结语、延伸阅读、继续阅读、关注引导、社群、扫码、网站或任何 CTA；系统会统一处理文末固定信息。
8. 不要虚构“我读完后”“我们采访了”等个人经历，不要故意口语化或加入情绪。人工编辑感来自具体证据、准确取舍和自然节奏。
9. 输出前逐段朗读核对：标题与导语不重复；主标题、小标题和每个正文段落都是完整句意，不得出现被截断的主谓宾或“。，”“，。”等标点；没有元话语、推广语和未解问题栏目。只输出最终 Markdown，不输出核对过程。
""".strip()


HEADING_RE = re.compile(r"^\s*(#{1,6})\s+(.+?)\s*$")
STANDALONE_LABEL_RE = re.compile(r"^\s*(?:[-*]\s*)?(?:\*\*|__)?(.+?)(?:\*\*|__)?\s*[：:]?\s*$")
FORBIDDEN_META_HEADING_RE = re.compile(
    r"(?:"
    r"(?:该|本|这份)?报告.{0,8}(?:尚未|仍未|还未|未能|没有|没能|未)(?:解决|回答|覆盖|展开|说明|解释|说清|说透)|"
    r"(?:尚待|仍待|有待|还需)(?:回答|解决|验证|观察|追问)|"
    r"(?:未解|待解|开放性?)问题|"
    r"(?:报告|研究)(?:的)?(?:留白|空白|局限|不足)|"
    r"(?:报告|研究)(?:没有|没)(?:说清|说透|回答)|"
    r"(?:哪些|什么).{0,8}(?:问题|变量).{0,8}(?:未|没|待|追问)|"
    r"(?:继续|延伸|更多)(?:阅读|查看|了解)|"
    r"(?:如何|哪里)(?:获取|领取|查看).{0,8}(?:原文|报告)|"
    r"(?:为什么|为何).{0,8}(?:值得|需要).{0,8}(?:读|看).{0,8}(?:原文|报告)|"
    r"(?:关注我们|关注公众号|扫码(?:交流|加入|领取|查看)|设置?星标|加入(?:社群|交流群|知识星球)|更新信息参见)"
    r")",
    re.I,
)
MODEL_CTA_RE = re.compile(
    r"(?:"
    r"扫码(?:交流|加入|领取|查看)?|知识星球|加微信|朋友圈(?:查看|领取|更新)|设为星标|设置星标|关注并星标|"
    r"每日汇编|每天(?:我|我们)?会把|国际信源汇编|喂给\s*AI|人工快速扫|图表合集|"
    r"(?:欢迎|扫码|邀请).{0,8}加入.{0,12}(?:群|讨论|交流)|(?:加入|进入).{0,8}(?:社群|交流群)|"
    r"社群.{0,8}(?:扫码|加入|领取|获取|交流)|继续拆.{0,12}报告|"
    r"完整报告.{0,24}(?:获取|领取|查看|阅读|继续|扫码|加入|参见)|"
    r"(?:获取|领取|查看|阅读).{0,12}(?:原文|完整报告)|"
    r"更新信息参见|portal|k[cC]d[eE]sk(?:\.com)?|[ΚK][СC]ⅾ?е?ѕ?k|"
    r"如果你是从.{0,30}搜到这里|单篇文章只能解决|"
    r"(?:更多|后续).{0,16}(?:内容|报告|交流).{0,12}(?:关注|扫码|加入|查看)"
    r")",
    re.I,
)
PORTAL_IMAGE_TOKEN_RE = re.compile(r"\[\[PORTAL_IMAGE_\d{3}\]\]")
COMMENT_LABEL_LINE_RE = re.compile(
    r"^\s*(?:>\s*)?(?P<bold>\*\*|__)?\s*(?:编辑评论|KC评论)\s*[：:]\s*"
    r"(?(bold)(?P=bold)\s*)(?P<body>.*)$",
    re.I | re.M,
)
SENTENCE_RE = re.compile(r"[^。！？!?；;]+[。！？!?；;]?")


def _plain_label(value: str) -> str:
    text = re.sub(r"[*_`>#]", "", value or "")
    text = re.sub(r"^\s*(?:[一二三四五六七八九十\d]+[.、．])\s*", "", text)
    return re.sub(r"\s+", "", text).strip("：:，,。；;！？!?（）()[]【】")


def is_forbidden_meta_heading(value: str) -> bool:
    plain = _plain_label(value)
    return bool(plain and FORBIDDEN_META_HEADING_RE.search(plain))


def _standalone_forbidden_label(line: str) -> bool:
    match = STANDALONE_LABEL_RE.match(line)
    if not match:
        return False
    stripped = line.strip()
    label = _plain_label(match.group(1))
    explicitly_formatted = stripped.startswith(("**", "__")) or stripped.endswith(("：", ":"))
    section_noun = bool(
        re.match(
            r"^(?:(?:该|本|这份)?(?:报告|研究)|未解问题|待解问题|开放性?问题|尚待回答|还需追问)",
            label,
        )
    )
    return (
        2 <= len(label) <= 42
        and (explicitly_formatted or section_noun)
        and is_forbidden_meta_heading(label)
    )


def strip_forbidden_meta_sections(markdown: str) -> tuple[str, list[str]]:
    """Remove a forbidden heading and its complete Markdown section."""
    kept: list[str] = []
    changes: list[str] = []
    skip_level: int | None = None

    for raw in (markdown or "").splitlines():
        heading = HEADING_RE.match(raw)
        if skip_level is not None:
            if heading and len(heading.group(1)) <= skip_level:
                skip_level = None
            else:
                continue

        if heading:
            level = len(heading.group(1))
            if level >= 2 and is_forbidden_meta_heading(heading.group(2)):
                changes.append(f"removed_section:{_plain_label(heading.group(2))[:60]}")
                skip_level = level
                continue
        elif _standalone_forbidden_label(raw):
            changes.append(f"removed_section:{_plain_label(raw)[:60]}")
            skip_level = 6
            continue

        kept.append(raw)

    return "\n".join(kept), changes


def _strip_cta_sentences(line: str) -> tuple[str, bool]:
    # ``PORTAL_IMAGE`` is also the renderer's exact image-placeholder syntax.
    # Mask complete placeholders while looking for prose CTAs so the broad
    # ``portal`` brand guard cannot delete a legitimate image line.
    def contains_model_cta(value: str) -> bool:
        masked = PORTAL_IMAGE_TOKEN_RE.sub("IMAGE_PLACEHOLDER", value or "")
        return bool(MODEL_CTA_RE.search(masked))

    if not contains_model_cta(line):
        return line, False
    sentences = SENTENCE_RE.findall(line)
    kept = [sentence for sentence in sentences if sentence.strip() and not contains_model_cta(sentence)]
    return "".join(kept).strip(), True


def strip_model_cta(markdown: str) -> tuple[str, list[str]]:
    kept: list[str] = []
    changes: list[str] = []
    for raw in (markdown or "").splitlines():
        cleaned, changed = _strip_cta_sentences(raw)
        if changed:
            changes.append("removed_model_cta")
        if cleaned.strip():
            kept.append(cleaned)
        elif not raw.strip() and kept and kept[-1].strip():
            kept.append("")
    return "\n".join(kept), changes


def sanitize_wechat_article_markdown(markdown: str) -> tuple[str, list[str]]:
    """Apply idempotent public-facing cleanup to generated article Markdown."""
    text = re.sub(r"```(?:markdown)?\s*", "", markdown or "", flags=re.I)
    text = text.replace("```", "")
    text, section_changes = strip_forbidden_meta_sections(text)
    text, cta_changes = strip_model_cta(text)
    text, comment_label_changes = COMMENT_LABEL_LINE_RE.subn(
        lambda match: f"> **KC评论：** {match.group('body').strip()}",
        text,
    )
    text = re.sub(r"。\s*[，,]", "。", text)
    text = re.sub(r"[，,；;：:]\s*。", "。", text)
    text = re.sub(r"([。！？!?；;])\1+", r"\1", text)
    text = re.sub(r"[ \t]+\n", "\n", text)
    text = re.sub(r"\n{3,}", "\n\n", text).strip()
    changes = [*section_changes, *cta_changes]
    if comment_label_changes:
        changes.append("normalized_comment_label")
    return (text + "\n" if text else ""), changes


def audit_wechat_article_markdown(markdown: str) -> list[str]:
    """Return deterministic issues that should never reach WeChat."""
    issues: list[str] = []
    for raw in (markdown or "").splitlines():
        heading = HEADING_RE.match(raw)
        if heading and len(heading.group(1)) >= 2 and is_forbidden_meta_heading(heading.group(2)):
            issues.append("forbidden_meta_section")
            break
    masked = PORTAL_IMAGE_TOKEN_RE.sub("IMAGE_PLACEHOLDER", markdown or "")
    if MODEL_CTA_RE.search(masked):
        issues.append("model_cta")
    if re.search(r"(?:编辑评论)\s*[：:]", markdown or "", flags=re.I):
        issues.append("legacy_comment_label")
    if re.search(r"(?:。\s*[，,]|[，,；;：:]\s*。)", markdown or ""):
        issues.append("punctuation_artifact")
    if not re.search(r"^#\s+\S", markdown or "", flags=re.M):
        issues.append("missing_h1")
    if not re.search(r"^##\s+\S", markdown or "", flags=re.M):
        issues.append("missing_h2")
    return issues
