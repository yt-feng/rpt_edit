"""Localize only the report preview's fixed first-paint UI, without providers."""
from __future__ import annotations

import json
import re


_SCRIPTS = re.compile(r"(<script\b[^>]*>)(.*?)(</script\s*>)", re.IGNORECASE | re.DOTALL)
_PREVIEW_ID = re.compile(r"\sid\s*=\s*(['\"])reportPreviewBootstrap\1(?=\s|>)", re.IGNORECASE)
_GUIDANCE = "约 90% 的 Text only 报告可在首页按完整标题找到可下载版本，建议继续查看“其他报告”等板块。"
_SOURCE_LABELS = (
    "下载权限与相关报告将在后台补充。", "正在确认", "Institution", "Industry", "Date",
    "Available", "Text only", "先搜索同名可下载版本", _GUIDANCE, "在首页搜索同名报告",
)
_LABELS = {
    "ko": (
        "다운로드 권한과 관련 보고서는 백그라운드에서 불러옵니다.", "확인 중", "기관", "산업", "날짜",
        "이용 가능", "텍스트만", "먼저 같은 제목의 다운로드 가능한 버전을 검색하세요",
        "텍스트만 제공되는 보고서의 약 90%는 홈에서 전체 제목으로 검색하면 다운로드 가능한 버전을 찾을 수 있습니다. ‘기타 보고서’ 등의 섹션도 확인해 보세요.",
        "홈에서 같은 제목의 보고서 검색",
    ),
    "ja": (
        "ダウンロード権限と関連レポートはバックグラウンドで読み込まれます。", "確認中", "機関", "業種", "日付",
        "利用可能", "テキストのみ", "まず同じタイトルのダウンロード可能な版を検索してください",
        "テキストのみのレポートの約90%は、ホームで完全なタイトルを検索するとダウンロード可能な版を見つけられます。「その他のレポート」なども確認してください。",
        "ホームで同じタイトルのレポートを検索",
    ),
    "ar": (
        "سيتم تحميل صلاحيات التنزيل والتقارير ذات الصلة في الخلفية.", "جارٍ التحقق", "المؤسسة", "القطاع", "التاريخ",
        "متاح", "نص فقط", "ابحث أولاً عن نسخة قابلة للتنزيل بالعنوان نفسه",
        "يمكن العثور على نسخة قابلة للتنزيل لنحو 90% من تقارير «نص فقط» بالبحث عن العنوان الكامل في الصفحة الرئيسية. يُنصح أيضاً بمراجعة قسم «التقارير الأخرى» والأقسام المشابهة.",
        "ابحث عن التقرير بالعنوان نفسه في الصفحة الرئيسية",
    ),
}


def localize_report_preview(source: str, locale: str) -> str:
    """Replace reviewed string literals in the one named inline script only.

    Use after normal HTML localization. No source collection, cache update,
    external request, parameter rewriting or sanitizer change is performed.
    The Text-only display value and its equality check use the same mapping.
    """
    labels = _LABELS.get(locale)
    if labels is None:
        return source

    def localize(match: re.Match[str]) -> str:
        opening, script, closing = match.groups()
        if not _PREVIEW_ID.search(opening):
            return match.group(0)
        for original, translated in zip(_SOURCE_LABELS, labels, strict=True):
            script = script.replace(json.dumps(original, ensure_ascii=False), json.dumps(translated, ensure_ascii=False))
        return opening + script + closing

    return _SCRIPTS.sub(localize, source)
