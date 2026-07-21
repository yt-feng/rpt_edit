#!/usr/bin/env python3
"""Compliance-oriented sensitive-content guard for generated notes.

This script is designed for generated marketing/publication materials only. It:
1. Applies local compliance-safe replacements for risky finance/marketing wording.
2. Checks text with the free-api sensitive-word endpoint when enabled.
3. If the endpoint flags content, asks DeepSeek to rewrite it into safer wording.

The goal is not to bypass platform moderation, but to reduce overclaiming,
financial-advice language, direct engagement bait, and sensitive phrasing before
publishing public-facing notes.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import time
from pathlib import Path
from typing import Any

import requests

TARGET_FILENAMES = {
    "note.md",
    "wechat_article.md",
    "wechat_article_en.md",
    "zhihu_article.md",
    "xianyu_note.md",
    "podcast_script_zh.md",
    "podcast_script_en.md",
    "podcast_zh.md",
    "podcast_en.md",
}
SKIP_NAMES = {
    "source_mineru.md",
    "prompt_for_xianyu.md",
    "prompt_for_zhihu.md",
    "prompt_for_market_views.md",
}

SAFE_XHS_TAGS = ["#学习笔记", "#研究笔记", "#学习研究", "#研报解读"]
DISALLOWED_XHS_TAGS_RE = re.compile(r"#(?:投资学习|财经|金融|股票|基金|理财|小红书笔记|笔记分享|干货分享)\b")
SAFE_XIANYU_TAGS = ["#学习资料", "#研究笔记", "#学习笔记", "#行业研究", "#研报资料", "#资料整理", "#报告学习", "#案例研究"]
DISALLOWED_XIANYU_TAGS_RE = re.compile(r"#(?:财经|投资|股票|基金|理财|暴富|内幕|买入|卖出|稳赚|保本)\b")
WECHAT_STOCK_ARTICLE_FILENAMES = {"wechat_article.md", "wechat_article_en.md"}
EN_RATING_PATTERN = (
    r"(?<![A-Za-z])(?:strong\s+buy|buy|sell|overweight|underweight|outperform|underperform|"
    r"equal-?weight|market\s+perform|neutral|hold)(?![A-Za-z])"
)
EN_PRICE_TOKEN_PATTERN = r"(?<![A-Za-z])(?:PT|TP|PO)(?![A-Za-z])"
WECHAT_STOCK_TARGET_CLAUSE_RE = re.compile(
    r"(?:(?:上调|下调|维持|重申|给予|首予|首次覆盖|恢复|raise|raised|lower|lowered|maintain|"
    r"maintained|initiate|initiated|resume|resumed)\s*)?"
    r"[^，。；;\n]{0,24}"
    r"(?:目标价|目标价格|价格目标|目标估值|target\s+price|price\s+target|price\s+objective)"
    r"[^，。；;\n]{0,70}"
    rf"|(?:(?:new|raise|raised|lower|lowered|maintain|maintained)\s+)?{EN_PRICE_TOKEN_PATTERN}"
    r"[^，。；;\n]{0,45}",
    re.I,
)
WECHAT_STOCK_PAREN_RE = re.compile(
    r"[（(][^()（）\n]{0,90}(?:目标价|目标价格|target\s+price|price\s+target|"
    rf"{EN_PRICE_TOKEN_PATTERN}|买入|卖出|增持|减持|强烈推荐|推荐|荐股|"
    rf"{EN_RATING_PATTERN})[^()（）\n]{{0,90}}[）)]",
    re.I,
)
WECHAT_STOCK_CONTEXT_RE = re.compile(
    r"(?:评级|目标价|目标价格|价格目标|荐股|股票|股价|个股|券商|报告|研究覆盖|"
    rf"target\s+price|price\s+target|{EN_PRICE_TOKEN_PATTERN}|{EN_RATING_PATTERN})",
    re.I,
)
WECHAT_STOCK_FORBIDDEN_RE = re.compile(
    r"(?:目标价|目标价格|价格目标|目标估值|target\s+price|price\s+target|price\s+objective|"
    r"买入评级|卖出评级|增持评级|减持评级|强烈买入|推荐买入|建议买入|建议卖出|"
    r"强烈推荐|荐股|投资建议|操作建议|买卖建议|推荐|"
    rf"{EN_RATING_PATTERN})",
    re.I,
)

LOCAL_REPLACEMENTS: list[tuple[str, str]] = [
    (r"不构成任何投资建议", "仅为个人阅读分享"),
    (r"投资建议", "研究交流"),
    (r"投资参考", "研究参考"),
    (r"投资价值", "研究价值"),
    (r"投资机会", "研究线索"),
    (r"投资逻辑", "研究逻辑"),
    (r"投资者", "读者"),
    (r"适合投资", "适合研究"),
    (r"买入评级", "报告评级"),
    (r"卖出评级", "报告评级"),
    (r"强烈买入", "报告较为积极"),
    (r"推荐买入", "报告观点偏积极"),
    (r"马上上车", "可以继续跟踪"),
    (r"抄底", "底部观察"),
    (r"必涨", "存在上行假设"),
    (r"稳赚", "确定性仍需验证"),
    (r"翻倍", "弹性较高"),
    (r"暴涨", "明显走强"),
    (r"暴跌", "明显回落"),
    (r"收益率", "回报表现"),
    (r"保证收益", "不承诺结果"),
    (r"保本", "风险自担"),
    (r"内幕", "资料"),
    (r"内部资料", "资料"),
    (r"独家", "整理版"),
    (r"原版", "电子版"),
    (r"无水印", "清晰版"),
    (r"全网最低", "价格友好"),
    (r"关注点赞收藏", "欢迎交流收藏"),
    (r"点赞收藏关注", "欢迎交流收藏"),
    (r"关注\s*[、,，和]*\s*点赞", "欢迎交流"),
    (r"点赞\s*[、,，和]*\s*关注", "欢迎交流"),
    (r"点个关注", "欢迎交流"),
    (r"求关注", "欢迎交流"),
    (r"求点赞", "欢迎交流"),
    (r"点赞", "收藏"),
    (r"评论区见", "欢迎讨论"),
    (r"评论区留言", "可以一起讨论"),
    (r"必看", "值得看看"),
    (r"必读", "值得读"),
    (r"爆款", "吸引人的"),
    (r"震惊", "值得注意"),
    (r"全网首发", "整理分享"),
    (r"唯一", "相对少见"),
    (r"顶级", "高质量"),
    (r"最全", "较完整"),
    (r"最强", "较强"),
    (r"绝对", "相对"),
]

WECHAT_STOCK_REPLACEMENTS: list[tuple[str, str]] = [
    (r"(?:投资建议|操作建议|买卖建议)", "研究交流"),
    (r"(?:荐股|推荐标的|推荐个股)", "公司研究"),
    (r"(?:强烈推荐|推荐买入|建议买入|建议卖出)", "报告观点"),
    (r"(?:维持|重申|给予|首予|首次覆盖|恢复|上调|下调)\s*(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)\s*(?:评级|建议|观点)?", "更新公司观点"),
    (rf"(?:维持|重申|给予|首予|首次覆盖|恢复|上调|下调)\s*{EN_RATING_PATTERN}\s*(?:rating|rated|recommendation)?", "公司观点更新"),
    (r"(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)\s*(?:评级|建议)", "公司观点"),
    (r"评级\s*(?:上调|下调|维持|重申|恢复)?\s*(?:至|为)?\s*(?:买入|卖出|增持|减持|持有|中性|跑赢大市|跑输大市|优于大市|弱于大市)", "公司观点更新"),
    (rf"{EN_RATING_PATTERN}\s*(?:rating|rated|recommendation)?", "报告观点"),
    (r"(?:上调|下调|维持|重申|恢复)\s*评级", "更新公司观点"),
    (r"推荐", "提到"),
]

WECHAT_STRICT_WORD_REPLACEMENTS: list[tuple[str, str]] = [
    (r"世界经济论坛", "WEF"),
    (r"中国经济", "中国宏观环境"),
    (r"国内经济", "国内宏观环境"),
    (r"全球经济", "全球宏观环境"),
    (r"世界经济", "全球宏观环境"),
    (r"经济体", "地区"),
    (r"经济", "宏观环境"),
    (r"投资银行", "国际机构"),
    (r"投行", "国际机构"),
    (r"投研", "研究"),
    (r"投资者", "读者"),
    (r"投资人", "参与者"),
    (r"投资组合", "组合观察"),
    (r"投资回报", "回报表现"),
    (r"投资收益", "回报表现"),
    (r"投资周期", "研究周期"),
    (r"投资启示", "观察提示"),
    (r"投资", "研究"),
    (r"财经", "研究"),
    (r"金融机构", "机构"),
    (r"金融市场", "市场"),
    (r"金融条件", "资金条件"),
    (r"金融", "资金"),
    (r"A股|港股", "相关市场"),
    (r"股票市场|股市", "市场"),
    (r"股票|个股", "公司"),
    (r"股价", "报价"),
    (r"证券", "标的"),
    (r"券商", "机构"),
    (r"基金经理", "组合负责人"),
    (r"基金", "产品"),
    (r"理财", "资金规划"),
    (r"收益率", "回报表现"),
    (r"资产定价", "市场定价"),
    (r"风险", "不确定性"),
    (r"危机", "扰动"),
    (r"不好|不行", "需要继续观察"),
    (r"疲弱|乏力|低迷", "仍在调整"),
    (r"恶化", "出现变化"),
    (r"衰退|萎缩|收缩", "调整"),
    (r"通缩", "价格变化"),
    (r"崩盘|崩溃|暴跌", "明显波动"),
    (r"下行|放缓", "节奏变化"),
    (r"压力", "不确定性"),
    (r"拖累", "影响"),
    (r"负面", "谨慎"),
    (r"唱衰", "谨慎讨论"),
]

WECHAT_CHINA_NEUTRAL_REPLACEMENTS: list[tuple[str, str]] = [
    (
        r"((?:中国|国内|内地|大陆|人民币|A股|港股)[^。；;\n]{0,16})"
        r"(?:不好|不行|疲弱|乏力|低迷|恶化|危机|衰退|萎缩|收缩|通缩|崩盘|崩溃|"
        r"暴跌|下行|放缓|压力|拖累|负面|唱衰)",
        r"\1仍在调整",
    ),
    (r"中国不好|中国不行|唱衰中国", "相关表述需要中性处理"),
]

WECHAT_DIRECT_FORBIDDEN_RE = re.compile(
    r"(?:经济|投资|投行|投研|财经|金融|股票|个股|股价|股市|A股|港股|炒股|理财|证券|券商|基金|收益率|资产定价|风险)"
)
WECHAT_CHINA_NEGATIVE_CONTEXT_RE = re.compile(
    r"(?:中国|国内|内地|大陆|人民币|A股|港股)[^。；;\n]{0,20}"
    r"(?:不好|不行|疲弱|乏力|低迷|恶化|危机|衰退|萎缩|收缩|通缩|崩盘|崩溃|"
    r"暴跌|下行|放缓|压力|拖累|负面|唱衰)"
)

WECHAT_BLOCKED_TITLE_RULES: list[tuple[str, re.Pattern[str]]] = [
    (
        "military_or_defense",
        re.compile(
            r"(?:军用|军事|军队|国防|防务|战备|军工|武器|导弹|弹药|作战|战场|战争|"
            r"空军|海军|陆军|核武|航母)"
            r"|\b(?:defen[cs]e|military|armed\s+forces?|weapons?|missiles?|munitions?|"
            r"combat|warfare|battlefield|army|navy|air\s+force|nuclear\s+weapons?)\b"
            r"|\b(?:defen[cs]e|military|combat)\b.{0,40}\breadiness\b"
            r"|\breadiness\b.{0,40}\b(?:defen[cs]e|military|combat)\b",
            re.I,
        ),
    ),
    (
        "politically_sensitive",
        re.compile(
            r"(?:政治|政党|选举|议会|政变|地缘政治|制裁|主权争端|领土争端|台海|"
            r"台湾问题|台独|新疆|疆独|西藏|藏独|港独|人权指控|颜色革命|"
            r"习近平|特朗普|拜登|普京|泽连斯基|政府|国务院|当局|政策|监管|改革|"
            r"外管局|管制|暂停令|反恐|恐怖主义|关税|税收|税制|消费税|征税|征收|"
            r"贸易战|出口管制|台湾)"
            r"|\b(?:geopolitic(?:s|al)?|political\s+part(?:y|ies)|elections?|parliament|"
            r"coup|sanctions?|sovereignty\s+disputes?|territorial\s+disputes?|"
            r"Taiwan\s+Strait|Xinjiang|Tibet|human\s+rights\s+allegations?|Xi\s+Jinping|"
            r"Trump|Biden|Putin|Zelensky|government|polic(?:y|ies)|regulat(?:ion|ory)|"
            r"reforms?|tariffs?|tax(?:es|ation)?|trade\s+war|export\s+controls?|"
            r"counter[- ]terroris(?:m|t)|terroris(?:m|t)|Taiwan)\b",
            re.I,
        ),
    ),
]

# Public-account titles should describe a topic, not judge whether it is good,
# bad, right, wrong, safe, dangerous, winning, or losing.  This deliberately
# includes positive framing too: replacing one strong opinion with its opposite
# is not neutralization.
WECHAT_TITLE_EVALUATIVE_RE = re.compile(
    r"(?:不好|不行|负面|唱衰|风险|危机|警告|问题|挑战|困境|压力|冲击|拖累|"
    r"疲弱|乏力|低迷|恶化|衰退|崩盘|崩溃|暴跌|下行|放缓|收缩|萎缩|通缩|"
    r"失业|违约|债务|赤字|亏损|泡沫|过剩|瓶颈|缺口|短缺|限制|封锁|担忧|差异|分歧|"
    r"不确定|不及预期|低于预期|未达|落后|弱于|受损|去杠杆|杠杆|失败|受挫|"
    r"下滑|下降|下跌|减少|走弱|走低|回落|降温|缩水|挤出|吃掉|负增长|"
    r"高估|低估|误判|悖论|分水岭|触底|反而|不是|而是|未兑现|痛点|暴露|"
    r"考验|谨慎|质疑|侵蚀|紧张|警报|爆发|回调|退潮|折扣|更弱|偏弱|较弱|"
    r"疑虑|脱节|疲软|受限|不足|差距|断崖|中断|损害|威胁|争议|争论|抛售|"
    r"恐慌|波动|未获|未对齐|不改|不稳|不佳|趋弱|走软|动能减弱|按兵不动|"
    r"管制|暂停|激进|收紧|转负|大降|大涨|加剧|"
    r"真正|意外|赢家|输家|健康重置|利好|向好|改善|修复|回升|复苏|强劲|"
    r"亮眼|超预期|高于预期|领先|胜出|红利|机遇|机会|突破|创新高|创纪录|"
    r"稳健|韧性|乐观|积极|增长|上升|上涨|增加|走高|正增长|受益|支撑|"
    r"驱动|催化|盈利|净利润|超配|领先|引领|成功|护城河|巩固|增值|潜力|"
    r"最具|强于|优于|符合预期|达标|可控|可期|加速|扩张|扩大|上修|下修|上调|下调|"
    r"恢复|提高|降低|有限|偏少|较少|高企|升至|降至|上涨空间|下行空间|上行空间|"
    r"惊喜|吸睛|崛起|发力|跑赢|看好|看空|多头|空头|入场点|势在必行|"
    r"赋能|完好|强化|重构|重塑|推动|关键|支持|底部|涨幅|英雄|自我造血|"
    r"全球首发|新前沿|先求稳再求快|时机已到|冷静|沉着|从容|"
    r"是否|为什么|为何|何时|何处|如何|怎么|怎样|能否|会否|谁将|"
    r"需要关注|值得关注|实为|但|却|然而|vs\.?|VS\.?|"
    r"(?:(?:同比|环比)?(?:增|降)(?=\d))|"
    r"\b(?:risk|crisis|warning|problem|challenge|pressure|shock|drag|weak(?:ness)?|"
    r"recession|collapse|crash|slowdown|contraction|deflation|default|debt|deficit|"
    r"loss|bubble|overcapacity|bottleneck|shortage|restriction|concern|uncertain|"
    r"underperform|overperform|deleverag(?:e|ing)|failure|winner|loser|mispricing|"
    r"undervalued|overvalued|recovery|rebound|resilient|positive|negative|strong|"
    r"beat|miss|upside|downside|benefit|surprise|opportunit(?:y|ies)|threat|"
    r"improv(?:e|ement)|growth|decline|fall|rise|increase|decrease)\b)",
    re.I,
)
WECHAT_TITLE_CHINA_TOPIC_RE = re.compile(
    r"(?:中国|国内|内地|大陆|人民币|A股|港股|\bChina\b|\bChinese\b|\bMainland\b|"
    r"\bRMB\b|\bCNY\b)",
    re.I,
)
WECHAT_TITLE_SYSTEMIC_TOPIC_RE = re.compile(
    r"(?:宏观|权益策略|市场策略|人民币|汇率|货币|信贷|债务|债券|杠杆|财政|监管|政策|"
    r"地产|房地产|房价|楼市|就业|资本流动|资金流动|A股|港股|"
    r"\bmacro\b|\bequit(?:y|ies)\b|\bcurrency\b|\bforex\b|\bFX\b|\bcredit\b|"
    r"\bdebt\b|\bbonds?\b|\bleverag(?:e|ing)\b|\bfiscal\b|\bregulat(?:ion|ory)\b|\bpolicy\b|"
    r"\bproperty\b|\breal estate\b|\bemployment\b|\bcapital flows?\b)",
    re.I,
)

NEUTRAL_TITLE_TECH_TERMS = (
    "AI",
    "AGI",
    "ASIC",
    "CCL",
    "CPI",
    "CPO",
    "CPU",
    "CSRD",
    "DRAM",
    "EBO",
    "ESS",
    "GPU",
    "HBM",
    "HDD",
    "HDI",
    "IGBT",
    "LLM",
    "MLCC",
    "NAND",
    "NEV",
    "NPU",
    "PCB",
    "IC",
    "SaaS",
    "SSD",
    "TPU",
    "VDC",
    "WAIC",
)


def wechat_title_neutrality_issues(title: str) -> list[str]:
    """Return deterministic reasons why a title needs neutral rewriting."""
    normalized = re.sub(r"\s+", " ", title or "").strip()
    if not normalized:
        return []
    issues: list[str] = []
    blocked_reason = blocked_wechat_title_reason(normalized)
    if blocked_reason:
        issues.append(blocked_reason)
    if WECHAT_TITLE_EVALUATIVE_RE.search(normalized):
        issues.append("evaluative_or_adversarial_wording")
    if re.search(r"[?？]", normalized):
        issues.append("question_framing")
    if WECHAT_TITLE_CHINA_TOPIC_RE.search(normalized) and WECHAT_TITLE_SYSTEMIC_TOPIC_RE.search(normalized):
        issues.append("china_systemic_topic")
    return list(dict.fromkeys(issues))


def _split_wechat_title(title: str, institution_name: str = "") -> tuple[str, str]:
    normalized = re.sub(r"\s+", " ", title or "").replace(":", "：").strip(" ，,。；;：:、-—")
    prefix = institution_name.strip(" ：:，,、-—")
    body = normalized
    if "：" in normalized:
        head, tail = normalized.split("：", 1)
        if len(head) <= 16:
            if not prefix:
                prefix = head.strip()
            body = tail.strip()
    return prefix, body.strip(" ，,。；;：:、-—")


def _neutral_title_subject(body: str) -> str:
    match = re.match(
        r"^([\u4e00-\u9fffA-Za-z0-9.·&]{2,16}?)(?=(?:"
        r"20\d{2}年?(?:第?[一二三四1-4]季度|[上下]半年)?|"
        r"[1-4]Q\d{2}|Q[1-4]|[12]H\d{2}|[1-4]季度|"
        r"第?[一二三四]季度|上半年|下半年|"
        r"(?:[一二三四五六七八九十\d]+重)?护城河|"
        r"AI需求|PCB|CCL|HBM|DRAM|NAND|储能|零售|竞争性定价|先进封装|"
        r"研发|风险|更新|回应|善举|引领|打造|激进|先求稳|自我造血|全球首发|"
        r"盈利|业绩|财报|收入|营收|订单|业务|"
        r"产品|需求|供应|利润|数据|表现|增长|下降|回升|"
        r"走弱|改善|估值|周期))",
        body,
        flags=re.I,
    )
    subject = match.group(1).strip() if match else ""
    if not subject:
        first_clause = re.split(r"[，,；;\-—]", body, maxsplit=1)[0].strip()
        company_like = re.search(
            r"(?:集团|科技|电源|汽车|电信|外科|办公|电路|电器|银行|保险|软件|"
            r"股份|控股|国际|山泉|茅台|黄金|产品|体育|电子|公司)$",
            first_clause,
        )
        short_brand = re.fullmatch(
            r"(?:3M|GSK|SAP|IBM|AMD|ARM|ASML|LVMH|SK|LG|BYD)",
            first_clause,
            flags=re.I,
        )
        if 2 <= len(first_clause) <= 16 and (company_like or short_brand):
            subject = first_clause
    if not subject:
        return ""
    if "与" in subject:
        return ""
    if re.search(
        r"(?:策略|市场|行业|宏观|月度|周度|追踪|监测|展望|更新|分析|观察|预览|主题|"
        r"报告|简报|图表|全景|三件事|系列|生产率|资本支出|市场化计划)",
        subject,
        flags=re.I,
    ):
        return ""
    if subject in {
        "化工",
        "半导体",
        "电池",
        "储能",
        "消费",
        "医疗",
        "能源",
        "材料",
        "基础材料",
        "稀土",
        "生物制药",
        "创业成本",
    } or subject.endswith(("公用事业", "成本")):
        return ""
    if re.search(r"(?:美国|全球|亚洲|欧洲|日本|韩国|美洲)", subject) or re.match(
        r"^中国(?!中免|燃气|联通)", subject
    ):
        return ""
    if WECHAT_TITLE_EVALUATIVE_RE.search(subject):
        return ""
    if WECHAT_TITLE_SYSTEMIC_TOPIC_RE.fullmatch(subject) or blocked_wechat_title_reason(subject):
        return ""
    if subject.startswith("中国") and re.search(
        r"(?:家电|汽车|半导体|芯片|零售|消费|能源|软件|医药|医疗|房地产|市场)$",
        subject,
    ):
        return ""
    return subject


def _neutral_title_topic(body: str) -> str:
    """Build a complete, factual fallback without asking a model to improvise."""
    compact = re.sub(r"\s+", "", body or "")
    has = lambda pattern: re.search(pattern, compact, flags=re.I) is not None

    if has(r"(?:军用|军事|国防|防务|战备|军工|武器|战争|defen[cs]e|military|warfare)"):
        if has(r"(?:飞机|航空|aircraft|aviation)"):
            return "航空运维与AI技术应用观察" if has(r"AI|人工智能") else "航空运维与技术应用观察"
        return "技术应用与行业运营观察"
    if has(r"(?:反洗钱|反恐融资|anti.?money.?laundering|counter.?terrorist.?financ)"):
        return "合规治理与组织流程观察"
    if has(r"(?:关税|贸易战|出口管制|tariff|tradewar|exportcontrol)"):
        return "跨境贸易与行业变化观察"
    if has(r"(?:消费税|征税|征收|税收|(?<![A-Za-z])tax(?:es|ation)?(?![A-Za-z]))"):
        return "行业规则与相关数据观察"
    if has(r"(?:政策|监管|改革|polic(?:y|ies)|regulat(?:ion|ory)|reforms?)"):
        return "行业规则与主题变化观察"
    if has(r"(?:政治|政党|选举|议会|地缘政治|制裁|台海|新疆|西藏|人权|习近平|"
           r"特朗普|拜登|普京|泽连斯基|政府|国务院|当局|politic|election|geopolitic|"
           r"sanction|Taiwan|Xinjiang|Tibet|Trump|Biden|Putin|Zelensky|government)"):
        if has(r"(?:外管局|外汇|人民币|汇率|forex|currency)"):
            return "货币市场与相关指标观察"
        if has(r"(?:债券|债务|bond|debt)"):
            return "公共部门资金与相关数据观察"
        if has(r"AI|人工智能|GenAI"):
            return "AI技术与组织应用观察"
        return "区域环境与行业变化观察"

    if has(r"(?:人民币|汇率|货币|外汇|currency|forex|\bFX\b|\bRMB\b|\bCNY\b)"):
        if has(r"(?:估值|定价|valuation|pricing)"):
            return "货币定价框架与相关指标观察"
        return "货币市场与相关指标观察"
    if has(r"(?:中国宏观|国内宏观|China.?macro)") and has(r"(?:信贷|预期|credit|expectation)"):
        return "近期数据与市场预期比较观察"
    if has(r"(?:中国宏观|国内宏观|China.?macro)"):
        return "近期数据与市场变化观察"
    if has(r"(?:权益策略|A股|港股|equity)") and has(r"AI|人工智能"):
        return "AI主题与市场结构变化观察"
    if has(r"(?:通胀|价格|inflation)") and has(r"(?:公司|企业|corporate|business)"):
        return "企业经营与价格数据观察"
    if has(r"(?:通胀|价格|inflation)") and has(
        r"(?:基础材料|金属|钢铁|铁矿石|铜|铝|materials?|metals?|steel|ironore)"
    ):
        return "基础材料行业与价格数据观察"
    if has(r"(?:通胀|价格|inflation)"):
        return "价格数据与市场变化观察"
    if has(r"(?:(?<![A-Za-z])ETF(?![A-Za-z])|基金|AUM|产品新规)"):
        return "相关产品规则与数据观察"
    if has(r"(?:信贷|债务|杠杆|credit|debt|leverage)"):
        return "资金结构与相关数据观察"
    if has(r"(?:债券|bond)"):
        return "资金工具与相关数据观察"
    if has(r"(?:房地产|房价|楼市|地产|property|realestate)"):
        return "城市与住房数据变化观察"
    if has(r"(?:家电|homeappliance)") and has(r"(?:零售|retail)"):
        month = re.search(r"(?:^|[^\d])(1[0-2]|0?[1-9])月", compact)
        return f"家电零售{month.group(1)}月数据观察" if month else "家电零售与月度数据观察"
    if has(r"(?:月度|季度|[1-4]Q\d{2}|[12]H\d{2})") and has(r"(?:数据|追踪|同比|环比)"):
        return "月度与季度数据变化观察"
    if has(r"(?:可持续|sustainab)") and has(r"(?:生产率|productivity)"):
        return "可持续生产率衡量方法观察"
    if has(r"(?:老龄化|人口结构|aging)") and has(r"(?:银行业|banking)"):
        return "人口结构与银行服务观察"
    if has(r"(?:统计|核算|GDP|statistics?|accounting)"):
        return "统计方法与相关数据观察"

    technical_matches: list[tuple[int, str]] = []
    for term in NEUTRAL_TITLE_TECH_TERMS:
        match = re.search(rf"(?<![A-Za-z]){re.escape(term)}(?![A-Za-z])", body, re.I)
        if not match and term == "AI":
            match = re.search(r"AI(?=[\u4e00-\u9fff])", body, re.I)
        if match:
            technical_matches.append((match.start(), term))
    technical = [term for _position, term in sorted(technical_matches)][:2]
    subject = _neutral_title_subject(compact)
    if subject:
        period = "季度" if has(r"(?:[1-4]Q\d{2}|季度|quarter)") else "近期"
        if technical:
            return f"{subject}与{'、'.join(technical)}及{period}数据观察"
        return f"{subject}业务与{period}数据观察"

    topic_mappings = (
        (r"可持续|CSRD|sustainab", "可持续报告流程"),
        (r"基础材料|金属|钢铁|铁矿石|稀土|铜|铝|materials?|metals?|steel|ironore", "基础材料行业"),
        (r"半导体|芯片|semiconductor", "半导体行业"),
        (r"存储|memory|DRAM|NAND|SSD|HDD", "存储行业"),
        (r"电池|储能|battery|ESS", "电池储能"),
        (r"光模块|光互连|通信设备|数据中心|telecom|optical|datacenter", "数字基础设施"),
        (r"网络|网安|cyber", "网络安全"),
        (r"汽车|新能源车|automotive|vehicle", "汽车行业"),
        (r"小鹏|理想汽车|优步|网约车|共享出行|Uber|rideshar", "出行服务"),
        (r"家电|homeappliance", "家电行业"),
        (r"机器人|robot", "机器人行业"),
        (r"电商|零售|retail|e-commerce", "零售行业"),
        (r"能源|原油|天然气|电气化|energy|oil|gas|electrification", "能源行业"),
        (r"供应链|supplychain", "供应链"),
        (r"企业软件|软件|software|SaaS", "软件行业"),
        (r"旅游|tourism|travel", "旅游行业"),
        (r"医药|医疗|生物制药|biotech|healthcare", "医疗行业"),
        (r"保险|养老金|养老|insurance|pension", "保险与养老服务"),
        (r"资金流|capitalflow|fundflow", "资金流向"),
        (r"奢侈品|腕表|珠宝|服装|体育用品|luxury|watch|apparel", "消费品牌"),
        (r"食品|饮料|啤酒|白酒|消费品|food|beverage|consumer", "消费行业"),
        (r"大宗商品|commodity", "大宗商品"),
        (r"生产率|劳工|劳动力|竞业|productivity|labor", "组织管理与生产率"),
        (r"创业|初创|entrepreneur|startup", "创业与企业发展"),
        (r"统计|核算|GDP|statistics?|accounting", "统计方法"),
        (r"脱碳|碳信用|气候|decarbon|climate|carbon", "气候与产业转型"),
        (r"航运|港口|shipping|port", "运输与供应链"),
        (r"认证|标准|accredit|certif|standards?", "认证与标准体系"),
        (r"进口|出口|跨境贸易|imports?|exports?|trade", "跨境贸易"),
    )
    parts: list[str] = []
    for pattern, label in topic_mappings:
        if has(pattern) and label not in parts:
            parts.append(label)
        if len(parts) >= 2:
            break
    if technical and parts:
        return f"{'、'.join(technical)}与{parts[0]}技术应用观察"
    if technical:
        return f"{'、'.join(technical)}技术与行业应用观察"
    if parts:
        if parts[:2] == ["半导体行业", "存储行业"]:
            return "半导体与存储行业数据观察"
        primary = parts[0]
        return f"{primary}数据与主题变化观察"

    # Never perform word-by-word substitutions here. They can leave fragments
    # such as "X变化Y" or retain a contentious premise around the removed word.
    # A closed, grammatical fallback is less specific but always publishable;
    # the full report and article body remain available to the reader.
    return "研究主题与行业变化观察"


def neutralize_wechat_title(title: str, institution_name: str = "") -> tuple[str, list[str]]:
    """Rewrite a contentious title into a neutral one without dropping its article."""
    prefix, body = _split_wechat_title(title, institution_name)
    normalized = f"{prefix}：{body}" if prefix and body else (body or prefix)
    issues = wechat_title_neutrality_issues(normalized)
    if not issues:
        return normalized, []

    neutral_body = _neutral_title_topic(body)
    neutralized = f"{prefix}：{neutral_body}" if prefix else neutral_body
    # The fallback vocabulary above is intentionally closed. Keep this final
    # guard anyway so future regex additions cannot accidentally leave a
    # non-neutral title in the public draft.
    if wechat_title_neutrality_issues(neutralized):
        neutralized = f"{prefix}：研究主题与行业变化观察" if prefix else "研究主题与行业变化观察"
    return neutralized, [f"neutralized:{issue}" for issue in issues]

PROTECTED_TERMS = {
    "投研": "__PROTECT_TOUYAN__",
    "投行": "__PROTECT_TOUHANG__",
    "投顾": "__PROTECT_TOUGU__",
    "投资银行": "__PROTECT_IBANK__",
}


def log(message: str) -> None:
    print(message, flush=True)


def blocked_wechat_title_reason(title: str) -> str | None:
    """Return the legacy reason code that triggers a public-title rewrite."""
    normalized = re.sub(r"\s+", " ", title or "").strip()
    if not normalized:
        return None
    for reason, pattern in WECHAT_BLOCKED_TITLE_RULES:
        if pattern.search(normalized):
            return reason
    return None


def apply_local_guard(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    protected = text
    for key, token in PROTECTED_TERMS.items():
        protected = protected.replace(key, token)
    for pattern, repl in LOCAL_REPLACEMENTS:
        new_text, n = re.subn(pattern, repl, protected, flags=re.IGNORECASE)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
        protected = new_text
    new_text, n = re.subn(r"投资", "研究", protected)
    if n:
        changes.append(f"投资->研究 x{n}")
    for key, token in PROTECTED_TERMS.items():
        protected = protected.replace(token, key)
    protected = re.sub(r"\n{4,}", "\n\n\n", protected)
    return protected, changes


def sanitize_wechat_strict_wording(text: str) -> tuple[str, list[str]]:
    """Neutralize public-account wording that is too direct for finance-adjacent posts."""
    changes: list[str] = []
    cleaned = text or ""
    for pattern, repl in WECHAT_CHINA_NEUTRAL_REPLACEMENTS + WECHAT_STRICT_WORD_REPLACEMENTS:
        cleaned, n = re.subn(pattern, repl, cleaned, flags=re.I)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
    cleanup_pairs = [
        (r"宏观环境环境", "宏观环境"),
        (r"资金资金", "资金"),
        (r"研究研究", "研究"),
        (r"产品产品", "产品"),
        (r"市场市场", "市场"),
        (r"公司公司", "公司"),
        (r"(仍在调整){2,}", "仍在调整"),
        (r"((?:中国|国内|内地|大陆)宏观环境)不确定性仍在调整", r"\1仍在调整"),
        (r"仍在调整影响", "仍在调整，并影响"),
        (r"仍在调整相关市场", "仍在调整，相关市场"),
        (r"不确定性自担", "请自行判断"),
        (r"不确定性提示", "观察提示"),
        (r"研究建议", "观察提示"),
        (r"操作提示", "观察提示"),
    ]
    for pattern, repl in cleanup_pairs:
        cleaned, n = re.subn(pattern, repl, cleaned, flags=re.I)
        if n:
            changes.append(f"{pattern}->{repl} x{n}")
    return cleaned, changes


def sanitize_wechat_stock_language(
    text: str,
    strict_wording: bool = True,
    strict_h1_wording: bool | None = None,
) -> tuple[str, list[str]]:
    """Remove broker calls; optionally neutralize broader finance-adjacent wording."""
    changes: list[str] = []
    out_lines: list[str] = []
    for raw in (text or "").splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if stripped.startswith("![") or re.fullmatch(r"\[\[KC_IMAGE_\d{3}\]\]", stripped):
            out_lines.append(line)
            continue

        original_line = line
        heading_prefix = ""
        marker = re.match(r"^(\s*#{1,6}\s+)(.*)$", line)
        if marker:
            heading_prefix = marker.group(1)
            line = marker.group(2)
        is_heading = bool(heading_prefix)
        target_repl = "公司情况更新" if is_heading else ""
        line, n = WECHAT_STOCK_PAREN_RE.subn("", line)
        if n:
            changes.append(f"remove_stock_parenthetical x{n}")
        line, n = WECHAT_STOCK_TARGET_CLAUSE_RE.subn(target_repl, line)
        if n:
            changes.append(f"remove_target_price_clause x{n}")

        stock_context = bool(WECHAT_STOCK_CONTEXT_RE.search(original_line))
        for pattern, repl in WECHAT_STOCK_REPLACEMENTS:
            if pattern == "推荐" or stock_context or re.search(pattern, line, flags=re.I):
                line, n = re.subn(pattern, repl, line, flags=re.I)
                if n:
                    changes.append(f"{pattern}->{repl} x{n}")

        if stock_context:
            for word, repl in [("买入", "观点偏积极"), ("卖出", "观点偏谨慎"), ("增持", "观点偏积极"), ("减持", "观点偏谨慎")]:
                line, n = re.subn(word, repl, line)
                if n:
                    changes.append(f"{word}->{repl} x{n}")

        line = re.sub(r"\s{2,}", " ", line)
        line = re.sub(r"\s*([，。；;,:：])\s*", r"\1", line)
        line = re.sub(r"[，,；;]\s*(?:并)?(?:报告观点|公司观点|更新公司观点|公司观点更新)\s*(?:该股|该公司)?", "", line)
        line = re.sub(r"(?:[，,；;]\s*){2,}", "，", line)
        line = re.sub(r"[，,；;：:]\s*(?=$)", "", line)
        line = re.sub(r"(公司情况更新){2,}", "公司情况更新", line)
        line_strict_wording = strict_wording
        if marker and len(marker.group(1).strip()) == 1 and strict_h1_wording is not None:
            line_strict_wording = strict_h1_wording
        if line_strict_wording:
            line, strict_changes = sanitize_wechat_strict_wording(line)
            changes.extend(strict_changes)
        line = re.sub(r"\s*([，。；;,:：])\s*", r"\1", line)
        line = re.sub(r"[，,]+([。；;])", r"\1", line)
        line = re.sub(r"(?:[，,；;]\s*){2,}", "，", line)
        line = re.sub(r"[，,；;：:]\s*(?=$)", "", line)
        if re.fullmatch(r"[\s，,。；;]*(?:并)?(?:报告观点|公司观点|公司观点更新|更新公司观点|观点偏积极|观点偏谨慎|该股|该公司)+[。.]?", line):
            line = ""
        if is_heading:
            heading = line.strip(" ：:，,；;")
            heading = re.sub(r"[，,]?(?:更新公司观点|公司观点更新|公司观点|报告观点)$", "", heading).strip(" ：:，,；;")
            if not heading:
                heading = "公司情况更新"
            elif len(heading) < 6:
                heading = (heading + "：公司情况更新").strip("：")
            line = heading_prefix + heading
        if line != original_line:
            changes.append("sanitize_wechat_stock_line")
        out_lines.append(line)
    cleaned = "\n".join(out_lines)
    cleaned = re.sub(r"(仍在调整){2,}", "仍在调整", cleaned)
    cleaned = re.sub(r"\n{4,}", "\n\n\n", cleaned)
    return cleaned, changes


def contains_wechat_stock_forbidden_language(text: str) -> bool:
    return bool(WECHAT_STOCK_FORBIDDEN_RE.search(text or ""))


def contains_wechat_strict_forbidden_language(text: str) -> bool:
    return bool(WECHAT_DIRECT_FORBIDDEN_RE.search(text or "") or WECHAT_CHINA_NEGATIVE_CONTEXT_RE.search(text or ""))


def normalize_xhs_note_tags(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    original = text
    text = DISALLOWED_XHS_TAGS_RE.sub("", text)
    text = re.sub(r"(?:^|\n)\s*(?:#[^\n#\s]+\s*)+\s*$", "", text, flags=re.MULTILINE).strip()
    text = text + "\n\n" + " ".join(SAFE_XHS_TAGS) + "\n"
    text = re.sub(r"\n{3,}", "\n\n", text)
    if text != original:
        changes.append("normalize_xhs_note_tags")
    return text, changes


def normalize_xianyu_note(text: str) -> tuple[str, list[str]]:
    changes: list[str] = []
    original = text
    hashtag_candidates: list[str] = []
    kept_lines: list[str] = []
    for raw in text.splitlines():
        line = raw.rstrip()
        stripped = line.strip()
        if re.match(r"^(?:建议价格|价格建议|参考价格)\s*[:：]", stripped):
            changes.append("remove_xianyu_price_line")
            continue
        keyword_match = re.match(r"^(?:搜索关键词|搜索词|关键词)\s*[:：]\s*(.*)$", stripped)
        if keyword_match:
            keyword_text = keyword_match.group(1)
            parts = [p.strip(" #，,、/|;；") for p in re.split(r"[\s，,、/|;；]+", keyword_text) if p.strip(" #，,、/|;；")]
            for part in parts:
                if not re.search(r"财经|投资|股票|基金|理财|暴富|内幕|买入|卖出|稳赚|保本", part):
                    hashtag_candidates.append("#" + part.lstrip("#"))
            changes.append("convert_search_keywords_to_hashtag")
            continue
        hashtag_match = re.match(r"^(?:Hashtag|hashtag|标签)\s*[:：]\s*(.*)$", stripped)
        if hashtag_match:
            tag_text = DISALLOWED_XIANYU_TAGS_RE.sub("", hashtag_match.group(1))
            hashtag_candidates.extend(re.findall(r"#[^\s#，,、/|;；]+", tag_text))
            changes.append("normalize_existing_xianyu_hashtag_line")
            continue
        kept_lines.append(line)
    tags: list[str] = []
    for tag in hashtag_candidates + SAFE_XIANYU_TAGS:
        tag = tag.strip()
        if not tag.startswith("#"):
            tag = "#" + tag
        if DISALLOWED_XIANYU_TAGS_RE.search(tag):
            continue
        if tag not in tags:
            tags.append(tag)
        if len(tags) >= 10:
            break
    text = "\n".join(kept_lines).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    text = text + "\n\nHashtag：" + " ".join(tags) + "\n"
    if text != original:
        changes.append("normalize_xianyu_note")
    return text, changes


def chunks(text: str, max_chars: int = 650) -> list[str]:
    paras = re.split(r"(\n\n+)", text)
    out: list[str] = []
    buf = ""
    for part in paras:
        if len(buf) + len(part) <= max_chars:
            buf += part
        else:
            if buf.strip():
                out.append(buf.strip())
            if len(part) > max_chars:
                for i in range(0, len(part), max_chars):
                    piece = part[i:i + max_chars].strip()
                    if piece:
                        out.append(piece)
                buf = ""
            else:
                buf = part
    if buf.strip():
        out.append(buf.strip())
    return out


def free_api_check(text: str, api_url: str, max_chunks: int = 20) -> dict[str, Any]:
    hits: list[dict[str, Any]] = []
    errors: list[str] = []
    for idx, chunk in enumerate(chunks(text)[:max_chunks], 1):
        try:
            response = requests.get(api_url, params={"msg": chunk}, timeout=12)
            data = response.json()
            if str(data.get("num")) == "1":
                hits.append({"chunk_index": idx, "ci": data.get("ci", ""), "desc": data.get("desc", "存在敏感词")})
        except Exception as exc:
            errors.append(str(exc)[:200])
            break
        time.sleep(0.1)
    return {"hit": bool(hits), "hits": hits, "errors": errors}


def deepseek_rewrite(text: str, detected_hits: list[dict[str, Any]], model: str, base_url: str) -> str:
    api_key = os.getenv("DEEPSEEK_API_KEY")
    if not api_key:
        raise RuntimeError("Missing DEEPSEEK_API_KEY")
    prompt = f"""
请把下面的中文营销/笔记文案改写为更稳妥的平台公开发布版本。

要求：
1. 保留原有信息结构、标题层级、Markdown 链接和图片链接。
2. 删除或替换金融操作建议、收益承诺、买卖暗示、极限词、夸张词、直接引导关注点赞等表达。
3. 不要用谐音、拆字、错别字或黑话绕过平台规则；要改成自然、合规、克制的表达。
4. 微信文章里不要直接输出“经济、投资、财经、金融、股票、股价、股市、理财、证券、券商、收益率、资产定价”等直白词；改成“宏观环境、研究、观察、资金、公司、报价、市场、回报表现、市场定价”等中性表达。
5. 不要新增事实、页数、价格、承诺、联系方式。
6. 小红书 note.md 的标签只能使用 #学习笔记 #研究笔记 #学习研究 #研报解读。
7. 闲鱼 xianyu_note.md 不要输出“建议价格”或“搜索关键词”，如需关键词请改成 Hashtag。
8. 涉及中国、国内、内地、大陆、人民币、A股、港股时，必须使用中性客观表达，不写“不好、不行、疲弱、低迷、恶化、危机、衰退、崩盘、放缓、压力、拖累、唱衰”等负面判断。
9. 知乎 zhihu_article.md 保持理性长文风格，不要写关注点赞或操作建议。
10. 只输出改写后的正文，不要解释。

检测命中：
{json.dumps(detected_hits, ensure_ascii=False)}

原文：
{text}
    """.strip()
    response = requests.post(
        base_url.rstrip("/") + "/chat/completions",
        headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
        json={
            "model": model,
            "temperature": 0.2,
            "messages": [
                {"role": "system", "content": "你是严谨的中文内容合规编辑，只做安全、自然、克制的改写。"},
                {"role": "user", "content": prompt},
            ],
        },
        timeout=240,
    )
    if response.status_code >= 400:
        raise RuntimeError(f"DeepSeek rewrite failed: HTTP {response.status_code}, {response.text[:500]}")
    data = response.json()
    return data["choices"][0]["message"]["content"].strip() + "\n"


def should_process(path: Path) -> bool:
    if path.name in SKIP_NAMES:
        return False
    if path.name in TARGET_FILENAMES:
        return True
    if path.suffix.lower() == ".md" and not path.name.startswith("prompt_") and "source" not in path.name.lower():
        return True
    return False


def guard_file(path: Path, args: argparse.Namespace) -> dict[str, Any]:
    original = path.read_text(encoding="utf-8", errors="ignore")
    local_text, local_changes = apply_local_guard(original)
    if path.name in WECHAT_STOCK_ARTICLE_FILENAMES:
        local_text, stock_changes = sanitize_wechat_stock_language(local_text)
        local_changes.extend(stock_changes)
    check = {"hit": False, "hits": [], "errors": []}
    final_text = local_text
    rewrite_error = ""
    if str(args.use_free_api).lower() in {"1", "true", "yes", "y", "on"}:
        check = free_api_check(local_text, args.sensitive_api_url, args.max_check_chunks)
    if check.get("hit"):
        try:
            rewritten = deepseek_rewrite(local_text, check.get("hits", []), args.model, args.deepseek_base_url)
            final_text, more_changes = apply_local_guard(rewritten)
            local_changes.extend(["after_deepseek:" + x for x in more_changes])
        except Exception as exc:
            rewrite_error = str(exc)
            log(f"DeepSeek sensitive rewrite failed for {path}: {exc}")
    if path.name == "note.md":
        final_text, tag_changes = normalize_xhs_note_tags(final_text)
        local_changes.extend(tag_changes)
    if path.name == "xianyu_note.md":
        final_text, xianyu_changes = normalize_xianyu_note(final_text)
        local_changes.extend(xianyu_changes)
    changed = final_text != original
    if changed:
        path.write_text(final_text, encoding="utf-8")
    return {
        "path": str(path),
        "changed": changed,
        "local_changes": local_changes[:80],
        "api_hit": bool(check.get("hit")),
        "api_hits": check.get("hits", []),
        "api_errors": check.get("errors", []),
        "rewrite_error": rewrite_error,
    }


def run_sensitive_guard(output_dir: Path, args: argparse.Namespace) -> list[dict[str, Any]]:
    results: list[dict[str, Any]] = []
    for path in sorted(output_dir.rglob("*")):
        if path.is_file() and should_process(path):
            try:
                results.append(guard_file(path, args))
            except Exception as exc:
                results.append({"path": str(path), "changed": False, "error": str(exc)})
    summary_path = output_dir / "sensitive_content_guard_summary.json"
    summary_path.write_text(json.dumps(results, ensure_ascii=False, indent=2), encoding="utf-8")
    changed = sum(1 for item in results if item.get("changed"))
    hits = sum(1 for item in results if item.get("api_hit"))
    log(f"Sensitive content guard processed {len(results)} files; changed={changed}, api_hits={hits}.")
    return results


def build_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()
    parser.add_argument("--output-dir", required=True)
    parser.add_argument("--model", default=os.getenv("DEEPSEEK_MODEL", "deepseek-chat"))
    parser.add_argument("--deepseek-base-url", default=os.getenv("DEEPSEEK_BASE_URL", "https://api.deepseek.com"))
    parser.add_argument("--sensitive-api-url", default=os.getenv("SENSITIVE_API_URL", "https://v.api.aa1.cn/api/api-mgc/index.php"))
    parser.add_argument("--use-free-api", default="true")
    parser.add_argument("--max-check-chunks", type=int, default=20)
    return parser


def main() -> int:
    parser = build_arg_parser()
    args = parser.parse_args()
    run_sensitive_guard(Path(args.output_dir), args)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
