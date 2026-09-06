"""Exact locale-only detail hooks; the authoritative Chinese sources are untouched."""
from __future__ import annotations

import json
import re

LOCALES = ("ko", "ja", "ar")
MARKER = "// kc-locale-detail-hooks-v1"
_COPY = {
    "ko": ("번역을 준비하고 있습니다…", "이 페이지를 불러오지 못했습니다. 위의 중국어 링크를 이용하거나 다시 시도해 주세요.", "다시 시도"),
    "ja": ("翻訳を準備しています…", "このページを読み込めませんでした。上の中国語リンクを使うか、再試行してください。", "再試行"),
    "ar": ("جارٍ إعداد الترجمة…", "تعذر تحميل هذه الصفحة. استخدم الرابط الصيني أعلاه أو أعد المحاولة.", "إعادة المحاولة"),
}


def _once(source: str, old: str, new: str) -> str:
    if source.count(old) != 1:
        raise ValueError(f"Locale detail hook requires one source anchor: {old[:90]}")
    return source.replace(old, new, 1)


def _namespace_cache_key(source: str, name: str, locale: str) -> str:
    # Deployment materialization may rename a cache's literal value before the
    # locale build. The stable contract is its declaration, not its public name.
    declarations = re.findall(r"\b(?:const|let|var)\s+" + re.escape(name) + r"\b", source)
    literal = re.compile(
        r"^([ \t]*const " + re.escape(name) + r"[ \t]*=[ \t]*)"
        r"(?P<quote>[\"'])(?P<key>[A-Za-z0-9][A-Za-z0-9_.:-]{0,127})(?P=quote)"
        r"(?P<end>[ \t]*;[ \t]*)$",
        re.M,
    )
    matches = list(literal.finditer(source))
    if len(declarations) != 1 or len(matches) != 1:
        # Never echo materialized values or malformed initializer contents.
        raise ValueError(f"Locale detail hook requires one literal cache declaration: {name}")
    match = matches[0]
    namespaced = f"{match.group('key')}:{locale}"
    replacement = match.group(1) + match.group("quote") + namespaced + match.group("quote") + match.group("end")
    return source[:match.start()] + replacement + source[match.end():]


def inject_locale_detail_hooks(source: str, asset_name: str, locale: str) -> str:
    if locale not in LOCALES or asset_name != "app.js" or MARKER in source:
        return source
    # Small test/non-portal app fixtures do not implement these detail screens.
    if "const CONTENT_LOCALE =" not in source and "async function initReport()" not in source:
        return source
    source = _once(source, "  async function initReport() {", "  async function initReport() {")
    source = _once(source, "  async function initExternalDetail() {", "  async function initExternalDetail() {")
    pending, failed, retry = (json.dumps(text, ensure_ascii=False) for text in _COPY[locale])
    helper = f'''  {MARKER}
  async function requireLocaleDetail(target) {{
    if (target) {{ target.textContent = {pending}; target.setAttribute("role", "status"); }}
    if (window.PortalLocaleDetail) return window.PortalLocaleDetail;
    const module = await new Promise((resolve) => {{
      let timer;
      const finish = () => {{
        window.removeEventListener("kc-locale-detail-ready", finish);
        window.clearTimeout(timer);
        resolve(window.PortalLocaleDetail || null);
      }};
      window.addEventListener("kc-locale-detail-ready", finish);
      timer = window.setTimeout(finish, 8000);
      if (window.PortalLocaleDetail) finish();
    }});
    if (!module && target) {{
      target.textContent = {failed};
      const retry = document.createElement("button");
      retry.type = "button"; retry.textContent = {retry};
      retry.addEventListener("click", () => window.location.reload());
      target.append(retry);
    }}
    return module;
  }}
'''
    source = _once(source, "(function () {\n", "(function () {\n" + helper)
    for name in ("DOC_ITEM_CACHE_KEY", "REPORT_PREVIEW_CACHE_KEY"):
        source = _namespace_cache_key(source, name, locale)
    source = _once(source,
        '  async function initReport() {\n    const params = new URLSearchParams(window.location.search);\n    const id = params.get("id");',
        '  async function initReport() {\n    const params = new URLSearchParams(window.location.search);\n    const id = params.get("id");\n'
        '    const target = document.getElementById("detail");\n'
        '    const localeDetail = await requireLocaleDetail(target);\n'
        '    if (!localeDetail || !await localeDetail.prepare({ source: "catalog", id }, target, initReport)) return;')
    source = _once(source, '    const previewItem = reportPreviewFromParams(params, id) || cachedReportPreview(id);',
                   '    const previewItem = null; // Never first-paint unverified URL or browser-cache text.')
    source = _once(source, '    const detailRecord = await loadReportDetailRecord(id);',
        '    const detailRecord = await localeDetail.catalogRecord(id);\n'
        '    if (!detailRecord) { localeDetail.failed(target, initReport); return; }')
    source = _once(source, '    renderExternalDetailFirstPaint(item, target);',
        '    const localeDetail = await requireLocaleDetail(target);\n'
        '    if (!localeDetail || !await localeDetail.prepare(item, target, initExternalDetail)) return;\n'
        '    item = localeDetail.apply(item);\n'
        '    renderExternalDetailFirstPaint(item, target);')
    source = _once(source, '    item = await fetchDocDetailItem(workerUrl, item);',
                   '    item = localeDetail.apply(await fetchDocDetailItem(workerUrl, item));')
    related = "  async function initExternalRelated(item, workerUrl, catalogItems, searchTextById, catalogItemsPromise = null) {"
    source = _once(source, related, related + '\n    workerUrl = ""; // Keep published catalog recommendations; do not render untranslated remote lists.')
    return source


def defer_unverified_report_preview(source: str, locale: str) -> str:
    if locale not in LOCALES:
        return source
    scripts = re.compile(r"(<script\b[^>]*>)(.*?)(</script\s*>)", re.I | re.S)
    named = re.compile(r'\sid\s*=\s*([\'"])reportPreviewBootstrap\1(?=\s|>)')
    if sum(bool(named.search(match.group(1))) for match in scripts.finditer(source)) > 1:
        raise ValueError("Duplicate locale report preview bootstrap")
    def replace(match: re.Match[str]) -> str:
        opening, script, closing = match.groups()
        if not named.search(opening):
            return match.group(0)
        marker = "// kc-locale-detail-awaits-verified-fields"
        if marker not in script:
            script = _once(script, '"use strict";', f'"use strict";\n        return; {marker}')
        return opening + script + closing
    return scripts.sub(replace, source)
