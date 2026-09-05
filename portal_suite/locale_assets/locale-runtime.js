(() => {
  "use strict";

  const LOCALES = Object.freeze({
    "zh-Hans": Object.freeze({ label: "中文", path: "", intlLocale: "zh-CN", direction: "ltr" }),
    ko: Object.freeze({ label: "한국어", path: "ko", intlLocale: "ko-KR", direction: "ltr" }),
    ja: Object.freeze({ label: "日本語", path: "ja", intlLocale: "ja-JP", direction: "ltr" }),
    ar: Object.freeze({ label: "العربية", path: "ar", intlLocale: "ar", direction: "rtl" }),
  });
  const LOCALIZED = new Set(["ko", "ja", "ar"]);
  const SHARED_PATH = /^\/(?:api|assets|data|\.well-known)(?:\/|$)|^\/favicon(?:\.|$)/i;
  const LOCAL_DATA_PATH = /^\/(?:ko|ja|ar)\/data\/course-materials\.json$/i;
  const CATALOG_OVERLAY_FILES = Object.freeze({
    preview: "catalog-preview.json",
    full: "catalog-titles.json",
    charts: "chart-content.json",
    "hot-reports": "hot-reports.json",
  });
  const CATALOG_OVERLAY_FIELDS = new Set(["title", "bank_name", "industry", "sector", "category"]);
  const HOT_REPORT_OVERLAY_FIELDS = new Set(["title", "title_cn", "institution", "description"]);
  const CHART_OVERLAY_FIELDS = new Set([
    "title", "description", "trend_summary",
    "metrics", "entities", "periods", "geographies", "units", "keywords",
  ]);
  const CHART_LIST_FIELDS = new Set(["metrics", "entities", "periods", "geographies", "units", "keywords"]);
  const HOT_REPORT_ID_PATTERN = /^hot:([a-f0-9]{16})$/;
  const HOT_REPORT_LOCALE_ID_LIMIT = 750;

  function normalizedLocale(value) {
    const text = String(value || "").trim();
    if (/^ko(?:-|$)/i.test(text)) return "ko";
    if (/^ja(?:-|$)/i.test(text)) return "ja";
    if (/^ar(?:-|$)/i.test(text)) return "ar";
    return "zh-Hans";
  }

  function isSimplifiedChineseUi(value) {
    const text = String(value || "").trim().toLowerCase();
    return text === "zh"
      || text === "zh-cn"
      || text === "zh-sg"
      || text === "zh-hans"
      || text.startsWith("zh-cn-")
      || text.startsWith("zh-sg-")
      || text.startsWith("zh-hans-");
  }

  function primaryBrowserLocale() {
    const languages = Array.isArray(navigator.languages) ? navigator.languages : [];
    // navigator.language is the browser UI's primary language. The ordered
    // content preference list may intentionally start with another language.
    return String(navigator.language || languages[0] || "");
  }

  function rootPathname(pathname) {
    const source = String(pathname || "/");
    const match = source.match(/^\/(?:ko|ja|ar)(?=\/|$)(.*)$/i);
    const root = match ? match[1] || "/" : source;
    return root.startsWith("/") ? root : `/${root}`;
  }

  function localePathname(pathname, locale) {
    const root = rootPathname(pathname);
    if (!LOCALIZED.has(locale)) return root || "/";
    return `/${locale}${root === "/" ? "/" : root}`;
  }

  function localeUrl(locale, source = window.location.href) {
    const url = new URL(source, window.location.href);
    url.pathname = localePathname(url.pathname, locale);
    return url.toString();
  }

  function dataRequestUrl(value, locale) {
    const text = String(value || "");
    if (/^(?:\.\/)?data\/course-materials\.json(?:[?#]|$)/i.test(text)) {
      return `/${locale}/${text.replace(/^\.\//, "")}`;
    }
    if (/^(?:\.\/)?data\//i.test(text)) return `/${text.replace(/^\.\//, "")}`;
    return value;
  }

  function localizePayload(value, locale, titleTranslations = {}, itemTranslations = {}, scope = {}) {
    if (!LOCALIZED.has(locale) || !value || typeof value !== "object") return value;
    const scoped = scope && scope.scoped === true;
    const removed = Symbol("unpublished locale content");
    const itemPositions = new Set(["items", "related", "item", "charts", "detail-record"]);
    const visit = (node, position = "") => {
      if (!node || typeof node !== "object") return node;
      if (Array.isArray(node)) {
        if (!scoped) {
          node.forEach((child) => visit(child, position));
          return node;
        }
        const retained = node.map((child) => visit(child, position)).filter((child) => child !== removed);
        retained.forEach((child, index) => { node[index] = child; });
        node.length = retained.length;
        return node;
      }
      const itemId = String(node.id || "").trim();
      const lookupKeys = [];
      const isChart = String(node.analysis_version || "") === "chart-search-v2" && itemId;
      if (isChart) {
        lookupKeys.push(`chart:${itemId}`);
      }
      const reportId = String(node.report_id || "").trim();
      const reportRef = String(node.report_ref || "").trim();
      if (reportId) lookupKeys.push(`report:${reportId}`);
      else if (reportRef) lookupKeys.push(`report-ref:${reportRef}`);
      if (itemId) lookupKeys.push(itemId);
      const overlayKey = lookupKeys.find((key) => (
        itemTranslations[key] && typeof itemTranslations[key] === "object"
      )) || "";
      const isGroup = ["items", "groups", "children"].some((key) => Array.isArray(node[key]));
      const isReport = (reportId || reportRef) && (typeof node.title === "string" || Array.isArray(node.charts));
      const isContentItem = Boolean(isChart || isReport || (itemId && itemPositions.has(position) && !isGroup));
      const requiredKey = isChart ? `chart:${itemId}`
        : itemId && itemPositions.has(position) ? itemId
        : reportId ? `report:${reportId}` : reportRef ? `report-ref:${reportRef}` : itemId;
      if (scoped && isContentItem && !(
        itemTranslations[requiredKey] && typeof itemTranslations[requiredKey] === "object"
        || requiredKey === itemId && String(titleTranslations[itemId] || "").trim()
      )) return removed;
      const localizedFields = overlayKey ? itemTranslations[overlayKey] : {};
      const localizedTitle = String(localizedFields.title || itemId && titleTranslations[itemId] || "").trim();
      if (localizedTitle) {
        const sourceTitle = String(node.title || "").trim();
        node.title = localizedTitle;
        node.title_zh = !scoped && sourceTitle && sourceTitle !== localizedTitle ? sourceTitle : "";
      }
      if (scoped && isContentItem && Object.prototype.hasOwnProperty.call(node, "title_zh")) node.title_zh = "";
      for (const field of ["title_cn", "institution", "bank_name", "industry", "sector", "category"]) {
        const translated = String(localizedFields[field] || "").trim();
        if (translated) node[field] = translated;
      }
      for (const field of ["description", "trend_summary"]) {
        const translated = String(localizedFields[field] || "").trim();
        if (translated) node[field] = translated;
      }
      for (const field of CHART_LIST_FIELDS) {
        const translated = localizedFields[field];
        if (Array.isArray(translated)) node[field] = translated.slice();
      }
      for (const [key, child] of Object.entries(node)) {
        if (["text", "content", "search_text", "extracted_text"].includes(key)) continue;
        if (child && typeof child === "object") {
          const childPosition = position === "report-map" ? "detail-record"
            : key === "reports" && !Array.isArray(child) ? "report-map" : key;
          const localized = visit(child, childPosition);
          if (localized === removed) {
            if (scoped && key === "item") return removed;
            delete node[key];
          }
        }
      }
      if (scoped) {
        if (Array.isArray(node.items)) {
          for (const key of ["item_count", "count", "total"]) {
            if (typeof node[key] === "number") node[key] = node.items.length;
          }
        }
        if (Array.isArray(node.charts) && typeof node.chart_count === "number") node.chart_count = node.charts.length;
        if (node.reports && typeof node.reports === "object") {
          const reports = Array.isArray(node.reports) ? node.reports : Object.values(node.reports);
          for (const key of ["item_count", "report_count"]) {
            if (typeof node[key] === "number") node[key] = reports.length;
          }
          if (typeof node.chart_count === "number") {
            node.chart_count = reports.reduce((sum, report) => sum + (Array.isArray(report.charts) ? report.charts.length : 0), 0);
          }
        }
      }
      return node;
    };
    return visit(value) === removed ? {} : value;
  }

  function catalogOverlayKind(value) {
    let url;
    try {
      url = new URL(String(value || ""), window.location.href);
    } catch (_error) {
      return "";
    }
    if (url.origin !== window.location.origin) return "";
    const pathname = url.pathname.replace(/^\/(?:ko|ja|ar)(?=\/data\/)/i, "");
    if (/^\/data\/catalog_preview\.json$/i.test(pathname)) return "preview";
    if (/^\/data\/chart_search_index\.json$/i.test(pathname)) return "charts";
    if (/^\/data\/catalog\.json$/i.test(pathname)) return "full";
    const detail = pathname.match(/^\/data\/report_details\/([a-z0-9_]{2})\.json$/i);
    if (detail) return `detail:${detail[1].toLowerCase()}`;
    return "";
  }

  function catalogOverlayFilename(kind) {
    if (CATALOG_OVERLAY_FILES[kind]) return CATALOG_OVERLAY_FILES[kind];
    const detail = String(kind || "").match(/^detail:([a-z0-9_]{2})$/);
    return detail ? `catalog-detail-${detail[1]}.json` : "";
  }

  function isAutoDirectionControl(node) {
    const tagName = String(node && node.tagName || "").toUpperCase();
    if (tagName === "TEXTAREA") return true;
    if (tagName !== "INPUT") return false;
    const type = String(node.getAttribute && node.getAttribute("type") || "text").toLowerCase();
    return type === "text" || type === "search";
  }

  function applyArabicInputDirection(locale, root = document) {
    if (locale !== "ar" || !root) return;
    if (isAutoDirectionControl(root)) root.setAttribute("dir", "auto");
    if (typeof root.querySelectorAll !== "function") return;
    root.querySelectorAll('input[type="text"], input[type="search"], textarea').forEach((control) => {
      control.setAttribute("dir", "auto");
    });
  }

  function normalizedOverlayPayload(payload, locale, kind) {
    if (!payload || payload.locale !== locale || (payload.kind && payload.kind !== kind)) {
      throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
    }
    if (payload.scoped !== undefined && typeof payload.scoped !== "boolean") {
      throw new Error(`Portal ${locale} ${kind} translation scope is invalid.`);
    }
    if (Array.isArray(payload.fields) && Array.isArray(payload.rows)) {
      const allowedFields = kind === "charts"
        ? CHART_OVERLAY_FIELDS
        : kind === "hot-reports" ? HOT_REPORT_OVERLAY_FIELDS : CATALOG_OVERLAY_FIELDS;
      if (!payload.fields.length || payload.fields.some((field) => !allowedFields.has(String(field)))) {
        throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
      }
      const titles = Object.create(null);
      const items = Object.create(null);
      for (const row of payload.rows) {
        if (!Array.isArray(row) || row.length !== payload.fields.length + 1) {
          throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
        }
        const itemId = String(row[0] || "").trim();
        if (!itemId || Object.prototype.hasOwnProperty.call(items, itemId)) {
          throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
        }
        const translatedFields = Object.create(null);
        payload.fields.forEach((field, index) => {
          const raw = row[index + 1];
          if (kind === "charts" && CHART_LIST_FIELDS.has(field)) {
            if (!Array.isArray(raw)) throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
            translatedFields[field] = raw.map((value) => String(value || "").trim()).filter(Boolean);
            return;
          }
          const translated = String(raw || "").trim();
          if (translated) translatedFields[field] = translated;
        });
        items[itemId] = translatedFields;
        if (translatedFields.title) titles[itemId] = translatedFields.title;
      }
      if (Number(payload.item_count) !== payload.rows.length) {
        throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
      }
      return {
        titles,
        items,
        scoped: payload.scoped === true,
        sourceGeneration: String(payload.source_generation || "").trim(),
      };
    }
    if (!payload.titles || typeof payload.titles !== "object") {
      throw new Error(`Portal ${locale} ${kind} translations are invalid.`);
    }
    return {
      titles: payload.titles,
      items: payload.items && typeof payload.items === "object" ? payload.items : {},
      scoped: payload.scoped === true,
      sourceGeneration: String(payload.source_generation || "").trim(),
    };
  }

  function foldHotReportLocaleText(value, locale) {
    let normalized = String(value || "").normalize("NFKC").toLocaleLowerCase(
      LOCALES[locale] && LOCALES[locale].intlLocale || locale,
    );
    if (locale === "ar") {
      normalized = normalized
        .replace(/\u0640/g, "")
        .replace(/[\u0610-\u061a\u064b-\u065f\u0670\u06d6-\u06ed]/g, "")
        .replace(/[إأآٱ]/g, "ا")
        .replace(/[ىئی]/g, "ي")
        .replace(/ؤ/g, "و");
    }
    return normalized
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function matchingHotReportLocaleIds(query, locale, items) {
    const tokens = foldHotReportLocaleText(query, locale).split(" ").filter(Boolean);
    if (!tokens.length) return [];
    const matches = [];
    for (const [itemId, fields] of Object.entries(items || {})) {
      const match = HOT_REPORT_ID_PATTERN.exec(String(itemId || "").trim());
      if (!match || !fields || typeof fields !== "object") continue;
      const searchable = foldHotReportLocaleText([
        fields.title,
        fields.title_cn,
        fields.institution,
        fields.description,
      ].join(" "), locale);
      if (tokens.every((token) => searchable.includes(token))) matches.push(match[1]);
      if (matches.length >= HOT_REPORT_LOCALE_ID_LIMIT) break;
    }
    return matches;
  }

  function pendingHotReportTranslation(payload) {
    const pending = payload && typeof payload === "object" && !Array.isArray(payload)
      ? { ...payload }
      : {};
    if (Array.isArray(pending.items)) {
      pending.items = [];
      pending.total = 0;
      pending.next_cursor = "";
      pending.has_more = false;
    }
    pending.locale_translation_pending = true;
    return pending;
  }

  function patchLocalizedFetch(locale) {
    if (!LOCALIZED.has(locale) || typeof window.fetch !== "function") {
      return {
        localizeHotReports: async (payload) => payload,
        matchHotReportLocaleIds: async () => null,
      };
    }
    const originalFetch = window.fetch.bind(window);
    const overlayPromises = new Map();
    const loadOverlay = (kind) => {
      const filename = catalogOverlayFilename(kind);
      if (!filename) {
        return Promise.reject(new Error(`Portal ${locale} catalog overlay kind is invalid.`));
      }
      if (!overlayPromises.has(kind)) {
        const request = originalFetch(`/data/i18n/${locale}/${filename}`, {
          cache: "default",
        }).then(async (response) => {
          if (!response || !response.ok) throw new Error(`Portal ${locale} ${kind} translations are unavailable.`);
          const payload = await response.json();
          return normalizedOverlayPayload(payload, locale, kind);
        }).catch((error) => {
          overlayPromises.delete(kind);
          throw error;
        });
        overlayPromises.set(kind, request);
      }
      return overlayPromises.get(kind);
    };
    window.fetch = async (input, init) => {
      let requestInput = input;
      if (typeof input === "string") {
        const mapped = dataRequestUrl(input, locale);
        requestInput = mapped;
      } else if (input instanceof Request) {
        const url = new URL(input.url, window.location.href);
        if (!LOCAL_DATA_PATH.test(url.pathname) && /^\/(?:ko|ja|ar)\/data\//i.test(url.pathname)) {
          url.pathname = url.pathname.replace(/^\/(?:ko|ja|ar)(?=\/data\/)/i, "");
          requestInput = new Request(url.toString(), input);
        }
      }
      const requestUrl = typeof requestInput === "string" ? requestInput : requestInput && requestInput.url;
      const overlayKind = catalogOverlayKind(requestUrl);
      const responsePromise = originalFetch(requestInput, init);
      const overlayResultPromise = overlayKind
        ? loadOverlay(overlayKind).then(
          (translations) => ({ translations, error: null }),
          (error) => ({ translations: null, error }),
        )
        : null;
      const response = await responsePromise;
      if (!overlayKind || !response || typeof response.json !== "function") return response;
      return new Proxy(response, {
        get(target, property) {
          if (property === "json") {
            return async () => {
              const [payload, overlayResult] = await Promise.all([
                target.json(),
                overlayResultPromise,
              ]);
              if (overlayResult.error) throw overlayResult.error;
              return localizePayload(
                payload,
                locale,
                overlayResult.translations.titles,
                overlayResult.translations.items,
                overlayResult.translations,
              );
            };
          }
          const result = Reflect.get(target, property, target);
          return typeof result === "function" ? result.bind(target) : result;
        },
      });
    };
    return {
      matchHotReportLocaleIds: async (query) => {
        try {
          const translations = await loadOverlay("hot-reports");
          return matchingHotReportLocaleIds(query, locale, translations.items);
        } catch (_error) {
          return null;
        }
      },
      localizeHotReports: async (payload) => {
        try {
          const translations = await loadOverlay("hot-reports");
          const sourceGeneration = String(payload && payload.generation || "").trim();
          if (!sourceGeneration || translations.sourceGeneration !== sourceGeneration) {
            return pendingHotReportTranslation(payload);
          }
          return localizePayload(payload, locale, translations.titles, translations.items, translations);
        } catch (_error) {
          return pendingHotReportTranslation(payload);
        }
      },
    };
  }

  function rewriteAnchor(anchor, locale) {
    if (!LOCALIZED.has(locale) || !anchor || !anchor.getAttribute) return;
    const raw = String(anchor.getAttribute("href") || "").trim();
    if (!raw || raw.startsWith("#") || /^(?:mailto|tel|javascript|data):/i.test(raw)) return;
    let url;
    try {
      url = new URL(raw, window.location.href);
    } catch (_error) {
      return;
    }
    if (url.origin !== window.location.origin || SHARED_PATH.test(url.pathname)) return;
    if (!/^\/(?:ko|ja|ar)(?:\/|$)/i.test(url.pathname)) {
      url.pathname = localePathname(url.pathname, locale);
      anchor.href = url.toString();
    }
  }

  function rewriteLocalizedLinks(locale, root = document) {
    if (!root || typeof root.querySelectorAll !== "function") return;
    root.querySelectorAll("a[href]").forEach((anchor) => rewriteAnchor(anchor, locale));
  }

  function watchLocalizedLinks(locale) {
    if (!LOCALIZED.has(locale) || typeof MutationObserver !== "function") return;
    const observer = new MutationObserver((records) => {
      for (const record of records) {
        for (const node of record.addedNodes || []) {
          if (!node || node.nodeType !== 1) continue;
          if (node.matches && node.matches("a[href]")) rewriteAnchor(node, locale);
          rewriteLocalizedLinks(locale, node);
          applyArabicInputDirection(locale, node);
        }
      }
    });
    observer.observe(document.documentElement, { childList: true, subtree: true });
  }

  function switcherLabel(locale) {
    if (locale === "ko") return "언어 선택";
    if (locale === "ja") return "言語を選択";
    if (locale === "ar") return "اختيار اللغة";
    return "Language";
  }

  function installSwitcher(locale) {
    if (isSimplifiedChineseUi(primaryBrowserLocale())) return null;
    if (document.querySelector("[data-kc-locale-switcher]")) return null;
    const nav = document.createElement("nav");
    nav.className = "kc-locale-switcher";
    nav.dataset.kcLocaleSwitcher = "";
    nav.setAttribute("aria-label", switcherLabel(locale));
    for (const [code, config] of Object.entries(LOCALES)) {
      const link = document.createElement("a");
      link.href = localeUrl(code);
      link.hreflang = code;
      link.lang = code;
      link.textContent = config.label;
      if (code === locale) {
        link.className = "is-current";
        link.setAttribute("aria-current", "page");
      }
      nav.append(link);
    }
    document.body.append(nav);
    return nav;
  }

  const contentLocale = normalizedLocale(document.documentElement.lang);
  const localeConfig = LOCALES[contentLocale];
  document.documentElement.classList.add(`kc-content-locale-${contentLocale.toLowerCase()}`);
  const localizedFetch = patchLocalizedFetch(contentLocale);

  function start() {
    rewriteLocalizedLinks(contentLocale);
    applyArabicInputDirection(contentLocale);
    installSwitcher(contentLocale);
    watchLocalizedLinks(contentLocale);
  }

  window.PortalLocale = Object.freeze({
    contentLocale,
    direction: localeConfig.direction,
    intlLocale: localeConfig.intlLocale,
    isSimplifiedChineseUi,
    localePathname,
    localeUrl,
    localizeHotReports: localizedFetch.localizeHotReports,
    matchHotReportLocaleIds: localizedFetch.matchHotReportLocaleIds,
    localizePayload,
    rootPathname,
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start, { once: true });
  } else {
    start();
  }
})();
