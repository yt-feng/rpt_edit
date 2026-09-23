"""Canonical, model-supported languages for offline SEO/GEO builds.

A supported language is NOT a published locale. Builders select an explicit
cohort; only complete accepted pages receive alternates or sitemap entries.
The current production default remains ko/ja/ar. No paid backend is selected.
"""
from __future__ import annotations

from dataclasses import dataclass
import argparse
import json
import re
from typing import Iterable

MODEL_CARD_URL = "https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF"
REGISTRY_VERSION = 1
DEFAULT_LOCALES = ("ko", "ja", "ar")

@dataclass(frozen=True)
class Language:
    code: str
    language_name: str
    native_name: str
    direction: str
    og_locale: str
    intl_locale: str
    script: str

_ROWS = (
    ('zh', 'Chinese', '中文', 'ltr', 'zh_CN', 'zh-CN', 'han'),
    ('ko', 'Korean', '한국어', 'ltr', 'ko_KR', 'ko-KR', 'hangul'),
    ('ja', 'Japanese', '日本語', 'ltr', 'ja_JP', 'ja-JP', 'japanese'),
    ('ar', 'Arabic', 'العربية', 'rtl', 'ar_AE', 'ar', 'arabic'),
    ('en', 'English', 'English', 'ltr', 'en_US', 'en', 'latin'),
    ('zh-Hant', 'Traditional Chinese', '繁體中文', 'ltr', 'zh_TW', 'zh-Hant', 'han'),
    ('fr', 'French', 'Français', 'ltr', 'fr_FR', 'fr', 'latin'),
    ('pt', 'Portuguese', 'Português', 'ltr', 'pt_PT', 'pt', 'latin'),
    ('es', 'Spanish', 'Español', 'ltr', 'es_ES', 'es', 'latin'),
    ('tr', 'Turkish', 'Türkçe', 'ltr', 'tr_TR', 'tr', 'latin'),
    ('ru', 'Russian', 'Русский', 'ltr', 'ru_RU', 'ru', 'cyrillic'),
    ('th', 'Thai', 'ไทย', 'ltr', 'th_TH', 'th', 'thai'),
    ('it', 'Italian', 'Italiano', 'ltr', 'it_IT', 'it', 'latin'),
    ('de', 'German', 'Deutsch', 'ltr', 'de_DE', 'de', 'latin'),
    ('vi', 'Vietnamese', 'Tiếng Việt', 'ltr', 'vi_VN', 'vi', 'latin'),
    ('ms', 'Malay', 'Bahasa Melayu', 'ltr', 'ms_MY', 'ms', 'latin'),
    ('id', 'Indonesian', 'Bahasa Indonesia', 'ltr', 'id_ID', 'id', 'latin'),
    ('tl', 'Filipino', 'Filipino', 'ltr', 'tl_PH', 'fil', 'latin'),
    ('hi', 'Hindi', 'हिन्दी', 'ltr', 'hi_IN', 'hi', 'devanagari'),
    ('pl', 'Polish', 'Polski', 'ltr', 'pl_PL', 'pl', 'latin'),
    ('cs', 'Czech', 'Čeština', 'ltr', 'cs_CZ', 'cs', 'latin'),
    ('nl', 'Dutch', 'Nederlands', 'ltr', 'nl_NL', 'nl', 'latin'),
    ('km', 'Khmer', 'ខ្មែរ', 'ltr', 'km_KH', 'km', 'khmer'),
    ('my', 'Burmese', 'မြန်မာ', 'ltr', 'my_MM', 'my', 'myanmar'),
    ('fa', 'Persian', 'فارسی', 'rtl', 'fa_IR', 'fa', 'arabic'),
    ('gu', 'Gujarati', 'ગુજરાતી', 'ltr', 'gu_IN', 'gu', 'gujarati'),
    ('ur', 'Urdu', 'اردو', 'rtl', 'ur_PK', 'ur', 'arabic'),
    ('te', 'Telugu', 'తెలుగు', 'ltr', 'te_IN', 'te', 'telugu'),
    ('mr', 'Marathi', 'मराठी', 'ltr', 'mr_IN', 'mr', 'devanagari'),
    ('he', 'Hebrew', 'עברית', 'rtl', 'he_IL', 'he', 'hebrew'),
    ('bn', 'Bengali', 'বাংলা', 'ltr', 'bn_BD', 'bn', 'bengali'),
    ('ta', 'Tamil', 'தமிழ்', 'ltr', 'ta_IN', 'ta', 'tamil'),
    ('uk', 'Ukrainian', 'Українська', 'ltr', 'uk_UA', 'uk', 'cyrillic'),
    ('bo', 'Tibetan', 'བོད་ཡིག', 'ltr', 'bo_CN', 'bo', 'tibetan'),
    ('kk', 'Kazakh', 'Қазақша', 'ltr', 'kk_KZ', 'kk', 'cyrillic'),
    ('mn', 'Mongolian', 'Монгол', 'ltr', 'mn_MN', 'mn', 'cyrillic'),
    ('ug', 'Uyghur', 'ئۇيغۇرچە', 'rtl', 'ug_CN', 'ug', 'arabic'),
    ('yue', 'Cantonese', '粵語', 'ltr', 'yue_HK', 'yue', 'han'),
)
LANGUAGES = {row[0]: Language(*row) for row in _ROWS}
MIRROR_CODES = tuple(code for code in LANGUAGES if code != "zh")
EXPANSION_CODES = tuple(code for code in MIRROR_CODES if code not in DEFAULT_LOCALES)
LOCALE_PATTERN = "|".join(re.escape(code) for code in sorted(MIRROR_CODES, key=len, reverse=True))
SCRIPT_PATTERNS = {
    "han": r"[\u3400-\u9fff]", "latin": r"[A-Za-z\u00c0-\u024f\u1e00-\u1eff]",
    "hangul": r"[\u1100-\u11ff\u3130-\u318f\uac00-\ud7af]",
    "japanese": r"[\u3040-\u30ff\u31f0-\u31ff\u3400-\u9fff]",
    "arabic": r"[\u0621-\u063a\u0641-\u064a\u066e-\u06d3\u06fa-\u06ff\u0750-\u077f\u08a0-\u08c9]",
    "cyrillic": r"[\u0400-\u052f]", "thai": r"[\u0e01-\u0e5b]",
    "devanagari": r"[\u0904-\u0939\u0958-\u0961]", "khmer": r"[\u1780-\u17b3]",
    "myanmar": r"[\u1000-\u102a\u1050-\u1055]", "gujarati": r"[\u0a85-\u0ab9]",
    "telugu": r"[\u0c05-\u0c39]", "hebrew": r"[\u05d0-\u05ea]",
    "bengali": r"[\u0985-\u09b9]", "tamil": r"[\u0b85-\u0bb9]",
    "tibetan": r"[\u0f40-\u0f6c]",
}
TARGET_SCRIPT_PATTERNS = {code: SCRIPT_PATTERNS[row.script] for code, row in LANGUAGES.items()}


def normalize_language(value: str) -> str:
    """Keep zh-Hant/yue distinct; normalize known regional aliases, never guess."""
    text = str(value).strip().replace("_", "-").lower()
    if text in {"zh-hant", "zh-tw", "zh-hk", "zh-mo"} or text.startswith("zh-hant-"):
        return "zh-Hant"
    if text in {"zh", "zh-hans", "zh-cn", "zh-sg", "cn"} or text.startswith("zh-hans-"):
        return "zh"
    code = text.split("-")[0]
    code = {"jp": "ja", "kr": "ko", "fil": "tl", "iw": "he"}.get(code, code)
    if code not in LANGUAGES:
        raise ValueError(f"Unsupported offline language: {value}")
    return code


def selected_locales(value: str | Iterable[str] | None = None) -> tuple[str, ...]:
    if value is None:
        return DEFAULT_LOCALES
    if isinstance(value, str):
        if value.strip() == "all":
            return MIRROR_CODES
        if value.strip() == "new":
            return EXPANSION_CODES
        value = value.split(",")
    rows = tuple(normalize_language(part) for part in value)
    if not rows or "zh" in rows or len(set(rows)) != len(rows):
        raise ValueError("Mirror targets must be unique, nonempty and exclude the Chinese root")
    return rows


def runtime_languages(codes: Iterable[str]) -> dict:
    result = {"zh-Hans": {"label": "中文", "path": "", "intlLocale": "zh-CN", "direction": "ltr"}}
    for code in selected_locales(codes):
        row = LANGUAGES[code]
        result[code] = {"label": row.native_name, "path": code, "intlLocale": row.intl_locale,
                        "direction": row.direction}
    return result


def manifest_locales(manifest: dict) -> tuple[str, ...]:
    codes = manifest.get("locales", list(DEFAULT_LOCALES))
    if not isinstance(codes, list) or not codes or not all(isinstance(code, str) for code in codes):
        raise ValueError("Invalid locale manifest languages")
    normalized = selected_locales(codes)
    if list(normalized) != codes:
        raise ValueError("Locale manifest must use canonical language codes")
    return normalized


# This safety/UI copy participates in the same validated translation cache as
# page text. New locales never borrow Korean/Arabic labels or English fallback.
UI_SOURCE = {
    "pending": "正在载入译文。",
    "failed": "译文未能载入，请重试或使用上方的中文链接。",
    "retry": "重试",
    "error": "本页部分内容未能载入，请使用上方的中文页面链接。",
    "equivalent": "查看本页中文版",
    "homepage": "中文首页",
    "account": "账户开通咨询",
    "email": "电子邮箱（必填）",
    "source": "来源",
    "language": "选择语言",
}
INDEX_UI_SOURCE = {
    "labels": ["研究机构", "行业", "开始日期", "结束日期", "搜索范围", "显示行数"],
    "clear": "清除", "previous": "上一页", "next": "下一页", "allIndustries": "所有行业",
    "allInstitutions": "所有研究机构",
    "scopes": ["搜索全部（快速）", "仅标题", "目录信息", "文档正文（较大索引）", "图表文本"],
    "industries": ["银行与金融", "能源与公用事业", "股票策略", "医疗与生物科技", "金属与矿业"],
    "reports": "报告", "page": "页", "of": "/", "updated": "更新时间", "index": "正文索引",
    "ready": "标题和目录搜索已就绪", "unavailable": "正文索引不可用", "recent": "近期正文",
    "noFilters": "未设置筛选条件",
}


def map_text(value, function):
    if isinstance(value, dict):
        return {key: map_text(item, function) for key, item in value.items()}
    if isinstance(value, list):
        return [map_text(item, function) for item in value]
    return function(value)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--targets", default="new")
    parser.add_argument("--matrix", action="store_true")
    parser.add_argument("--group-size", type=int, default=6)
    args = parser.parse_args()
    codes = selected_locales(args.targets)
    if not 1 <= args.group_size <= 12:
        parser.error("group size must be between 1 and 12")
    result = {"include": [{"group": index // args.group_size,
                           "targets": ",".join(codes[index:index+args.group_size])}
                          for index in range(0, len(codes), args.group_size)]} if args.matrix else {
        "supported_model_versions": len(LANGUAGES), "targets": list(codes),
        "production_defaults": list(DEFAULT_LOCALES), "translation_api_cost": 0,
    }
    print(json.dumps(result, ensure_ascii=False))
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
