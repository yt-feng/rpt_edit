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
          for (const key of ["item_count", "count", "total", "total_item_count"]) {
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
        detailTranslation: async () => null,
        readCatalogDetail: async () => null,
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
      detailTranslation: async (source, id, generation = "") => {
        const prefix = String(id || "").toLowerCase().replace(/[^a-z0-9]/g, "_").slice(0, 2).padEnd(2, "_");
        const kind = source === "catalog" ? `detail:${prefix}` : source === "hot" ? "hot-reports" : "";
        if (!kind) return null;
        try {
          const overlay = await loadOverlay(kind);
          if (source === "hot" && (!generation || overlay.sourceGeneration !== generation)) return null;
          const item = overlay.items[id];
          const title = item && item.title || overlay.titles[id];
          return title ? { ...(item || {}), title } : null;
        } catch (_) { return null; }
      },
      readCatalogDetail: async (id, translated) => {
        if (!/^[A-Za-z0-9_.:-]{1,256}$/.test(String(id || ""))) return null;
        const prefix = id.toLowerCase().replace(/[^a-z0-9]/g, "_").slice(0, 2).padEnd(2, "_");
        const [response, overlay] = await Promise.all([
          originalFetch(`/data/report_details/${prefix}.json`, { cache: "default" }),
          loadOverlay(`detail:${prefix}`).catch(() => ({ titles: {}, items: {} })),
        ]);
        if (!response.ok) return null;
        const payload = await response.json();
        const record = payload && payload.reports && payload.reports[id];
        if (!record || !record.item || record.item.id !== id) return null;
        const localized = localizePayload({ reports: { [id]: record } }, locale, overlay.titles,
          { ...overlay.items, [id]: translated }, { scoped: true });
        return localized.reports && localized.reports[id] || null;
      },
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
    // Recovery and language-navigation links intentionally leave this locale.
    // Preserve their full URL, including report id, query and fragment.
    if (anchor.getAttribute("data-kc-chinese-entry") !== null
      || /^zh(?:-|$)/i.test(String(anchor.getAttribute("hreflang") || "").trim())) return;
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

  const INDEX_UI = {
    ko: {
      labels: ["기관", "산업", "시작일", "종료일", "검색 범위", "표시 행 수"],
      clear: "초기화", previous: "이전", next: "다음", allIndustries: "전체 산업", allInstitutions: "전체 기관",
      scopes: ["전체 검색 (빠름)", "제목만", "목록 정보", "문서 본문 (대용량 색인)", "차트 텍스트"],
      industries: ["은행 / 금융", "에너지 / 유틸리티", "주식 전략", "헬스케어 / 바이오", "금속 / 광업"],
      reports: "개 보고서", page: "페이지", of: "/", updated: "업데이트", index: "본문 색인",
      ready: "제목 및 목록 검색 준비 완료", unavailable: "본문 색인을 사용할 수 없음", recent: "최근 본문",
      noFilters: "필터 없음",
    },
    ja: {
      labels: ["機関", "業種", "開始日", "終了日", "検索対象", "表示件数"],
      clear: "クリア", previous: "前へ", next: "次へ", allIndustries: "すべての業種", allInstitutions: "すべての機関",
      scopes: ["すべて検索（高速）", "タイトルのみ", "カタログ項目", "文書本文（大規模索引）", "グラフのテキスト"],
      industries: ["銀行 / 金融", "エネルギー / 公益事業", "株式戦略", "ヘルスケア / バイオ", "金属 / 鉱業"],
      reports: "件のレポート", page: "ページ", of: "/", updated: "更新", index: "本文索引",
      ready: "タイトル・カタログ検索の準備完了", unavailable: "本文索引を利用できません", recent: "最近の本文",
      noFilters: "フィルターなし",
    },
    ar: {
      labels: ["المؤسسة", "القطاع", "من تاريخ", "إلى تاريخ", "نطاق البحث", "عدد الصفوف"],
      clear: "مسح", previous: "السابق", next: "التالي", allIndustries: "جميع القطاعات", allInstitutions: "جميع المؤسسات",
      scopes: ["البحث في الكل (سريع)", "العنوان فقط", "حقول الفهرس", "نص المستند (فهرس كبير)", "نص الرسوم البيانية"],
      industries: ["البنوك / الخدمات المالية", "الطاقة / المرافق", "استراتيجية الأسهم", "الرعاية الصحية / التقنية الحيوية", "المعادن / التعدين"],
      reports: "تقرير", page: "الصفحة", of: "من", updated: "آخر تحديث", index: "فهرس النصوص",
      ready: "البحث في العناوين والفهرس جاهز", unavailable: "فهرس النصوص غير متاح", recent: "النصوص الحديثة",
      noFilters: "لا توجد عوامل تصفية",
    },
  };

  function installIndexUi(locale) {
    const words = INDEX_UI[locale];
    if (!words || typeof document.getElementById !== "function") return;
    const jobs = [];
    const setText = (node, value) => {
      if (node && node.textContent !== value) node.textContent = value;
    };
    const watch = (node, update) => {
      if (node) jobs.push({ node, update: () => update(node) });
    };
    ["bankFilter", "industryFilter", "startDate", "endDate", "scopeFilter", "pageSize"].forEach((id, index) => {
      const control = document.getElementById(id);
      const label = control && control.parentNode && control.parentNode.querySelector("span");
      watch(label, (node) => setText(node, words.labels[index]));
    });
    for (const [id, label] of [["clearFilters", words.clear], ["prevPage", words.previous], ["nextPage", words.next]]) {
      watch(document.getElementById(id), (node) => setText(node, label));
    }
    const industryNames = ["Banks / Financials", "Energy / Utilities", "Equity Strategy", "Healthcare / Biotech", "Metals / Mining"];
    watch(document.getElementById("industryFilter"), (node) => {
      for (const option of node.querySelectorAll("option")) {
        if (option.value === "") { setText(option, words.allIndustries); continue; }
        const match = option.textContent.match(/^(.*?)(\s+\([\d,]+\))?$/);
        const index = industryNames.indexOf(match ? match[1] : "");
        if (index >= 0) setText(option, words.industries[index] + (match[2] || ""));
      }
    });
    watch(document.getElementById("bankFilter"), (node) => {
      for (const option of node.querySelectorAll("option")) {
        if (option.value === "") setText(option, words.allInstitutions);
      }
    });
    watch(document.getElementById("scopeFilter"), (node) => {
      for (const option of node.querySelectorAll("option")) {
        const index = ["all", "title", "catalog", "fulltext", "charts"].indexOf(option.value);
        if (index >= 0) setText(option, words.scopes[index]);
      }
    });
    watch(document.getElementById("pageInfo"), (node) => {
      const match = node.textContent.trim().match(/^Page ([\d,]+) \/ ([\d,]+)$/);
      if (match) setText(node, `${words.page} ${match[1]} ${words.of} ${match[2]}`);
    });
    watch(document.getElementById("resultCount"), (node) => {
      const match = node.textContent.trim().match(/^([\d,]+) of ([\d,]+) reports$/);
      if (match) setText(node, `${match[1]} ${words.of} ${match[2]} ${words.reports}`);
    });
    watch(document.getElementById("activeFilters"), (node) => {
      if (node.textContent === "No filters") setText(node, words.noFilters);
    });
    watch(document.getElementById("catalogMeta"), (node) => {
      const text = node.textContent.split(" | ").map((part) => {
        if (part === "Title and catalog search ready") return words.ready;
        if (part === "Text index unavailable") return words.unavailable;
        if (part.startsWith("Updated ")) return `${words.updated} ${part.slice(8)}`;
        const count = part.match(/^([\d,]+) reports$/);
        if (count) return `${count[1]} ${words.reports}`;
        const index = part.match(/^Text index ([\d,]+) reports( \+)?( \(recent text\))?$/);
        return index ? `${words.index} ${index[1]} ${words.reports}${index[2] || ""}${index[3] ? ` (${words.recent})` : ""}` : part;
      }).join(" | ");
      setText(node, text);
    });
    jobs.forEach((job) => job.update());
    if (!jobs.length || typeof MutationObserver !== "function") return;
    const observer = new MutationObserver((records) => {
      // Observe only the named UI fields. Idempotent writes settle after one
      // update and never scan or translate report titles or institution names.
      for (const job of jobs) {
        if (records.some((record) => record.target === job.node || job.node.contains(record.target))) job.update();
      }
    });
    jobs.forEach(({ node }) => observer.observe(node, { childList: true, subtree: true, characterData: true }));
  }

  function switcherLabel(locale) {
    if (locale === "ko") return "언어 선택";
    if (locale === "ja") return "言語を選択";
    if (locale === "ar") return "اختيار اللغة";
    return "Language";
  }

  function installSwitcher(locale) {
    // The content locale controls this entry point, not the browser language.
    // Chinese pages never promote other languages; every locale keeps a way back.
    if (!LOCALIZED.has(locale)) return null;
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
      if (code === "zh-Hans") link.setAttribute("data-kc-chinese-entry", "");
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
    installIndexUi(contentLocale);
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
    detailTranslation: localizedFetch.detailTranslation,
    readCatalogDetail: localizedFetch.readCatalogDetail,
    localizePayload,
    rootPathname,
  });

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", start, { once: true });
  } else {
    start();
  }
})();
