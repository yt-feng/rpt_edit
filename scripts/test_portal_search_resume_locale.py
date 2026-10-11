"""Offline coverage for the small home-search additions in the locale build."""

import re
from pathlib import Path
import unittest

import build_portal_locales as builder


ROOT = Path(__file__).resolve().parents[1]
COPY = {
    "ko": {
        "继续上次搜索：": "지난 검색 계속하기:",
        "清除记录": "기록 지우기",
        "仅在此浏览器保留最近一次关键词，30 天后失效": "최근 검색어는 이 브라우저에만 저장되며 30일 후 만료됩니다",
        "当前目录未找到匹配报告。": "현재 목록에서 일치하는 보고서를 찾지 못했습니다.",
        "也可继续查看下方其他来源的搜索结果。": "아래 다른 출처의 검색 결과도 확인할 수 있습니다.",
        "保留关键词，清除筛选": "검색어를 유지하고 필터 지우기",
    },
    "ja": {
        "继续上次搜索：": "前回の検索を続ける：",
        "清除记录": "履歴を削除",
        "仅在此浏览器保留最近一次关键词，30 天后失效": "前回の検索語はこのブラウザーにのみ保存され、30日後に消去されます",
        "当前目录未找到匹配报告。": "現在のカタログには一致するレポートがありません。",
        "也可继续查看下方其他来源的搜索结果。": "下にある他の情報源の検索結果も確認できます。",
        "保留关键词，清除筛选": "検索語を残して絞り込みを解除",
    },
    "ar": {
        "继续上次搜索：": "متابعة البحث السابق:",
        "清除记录": "مسح السجل",
        "仅在此浏览器保留最近一次关键词，30 天后失效": "تُحفظ آخر كلمة بحث في هذا المتصفح فقط وتنتهي صلاحيتها بعد 30 يومًا",
        "当前目录未找到匹配报告。": "لم يتم العثور على تقارير مطابقة في الفهرس الحالي.",
        "也可继续查看下方其他来源的搜索结果。": "يمكنك أيضًا الاطلاع على نتائج البحث من المصادر الأخرى أدناه.",
        "保留关键词，清除筛选": "مسح عوامل التصفية مع الاحتفاظ بكلمة البحث",
    },
}


class SearchResumeLocaleTest(unittest.TestCase):
    def test_existing_locale_builder_translates_copy_and_preserves_controls(self):
        home = (ROOT / "portal_suite/site_src/index.html").read_text()
        app = (ROOT / "portal_suite/site_src/assets/app.js").read_text()
        fragment = re.search(r'<div class="search-resume".*?</div>', home, re.S).group()
        html = f'<!doctype html><html lang="zh-Hans"><head></head><body>{fragment}</body></html>'
        javascript = app[app.index("  function renderCatalogEmptyState("):app.index("  const INDUSTRY_RULES")]
        units = {}
        builder.collect_html_units(html, units)
        builder.collect_javascript_units(javascript, "app.js", units)
        for original in COPY["ja"]:
            protected = builder.protect_text(original).canonical
            self.assertTrue(any(protected in unit.source for unit in units.values()), original)
        for locale, translations in COPY.items():
            with self.subTest(locale=locale):
                cache = builder.empty_cache()
                for unit in units.values():
                    translated = unit.source
                    for original, replacement in translations.items():
                        translated = translated.replace(
                            builder.protect_text(original).canonical,
                            replacement.replace("30", "__KC_PH_000__") if "30" in original else replacement,
                        )
                    cache["locales"][locale][unit.key] = builder._translation_cache_row(unit, translated)
                localized_html = builder.render_localized_html(
                    html, locale=locale, cache=cache, site_url="https://example.invalid", discovery_markup="",
                )
                localized_js = builder.render_localized_javascript(javascript, "app.js", locale, cache)
                builder.validate_localized_javascript_residuals(javascript, localized_js, "app.js", locale, cache)
                for translated in translations.values():
                    self.assertIn(translated, localized_html + localized_js)
                self.assertIn('id="searchResume" hidden', localized_html)
                self.assertIn('<bdi id="lastSearchQuery"></bdi>', localized_html)
                self.assertIn('id="resumeLastSearch"', localized_html)
                self.assertIn('id="forgetLastSearch"', localized_html)
                self.assertIn('data-clear-catalog-filters', localized_js)
                self.assertIn('clear.addEventListener("click", onClearFilters)', localized_js)


if __name__ == "__main__":
    unittest.main()
