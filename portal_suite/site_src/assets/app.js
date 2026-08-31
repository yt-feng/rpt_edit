(function () {
  const page = document.body.dataset.page;
  const PUBLIC_BRAND = "KC桌面";
  const ADMIN_TOKEN_KEY = "portal_admin_token";
  const ADMIN_PLAIN_KEY = "portal_admin_plain_key";
  const ADMIN_COOKIE_NAME = "portal_admin_token";
  const ADMIN_COOKIE_MAX_AGE = 180 * 24 * 60 * 60;
  const DOWNLOAD_PASSWORD_KEY = "portal_download_password";
  const AUTH_SESSION_KEY = "portal_auth_session";
  const VISITOR_ID_KEY = "portal_visitor_id";
  const DOC_ITEM_CACHE_KEY = "portal_doc_item_cache_v2";
  const REPORT_PREVIEW_CACHE_KEY = "portal_report_preview_cache";
  const REPORT_PREVIEW_CACHE_MAX_ITEMS = 20;
  const REPORT_PREVIEW_CACHE_TTL_MS = 6 * 60 * 60 * 1000;
  const HOT_REPORT_FIRST_PAGE_CACHE_KEY = "portal_hot_report_first_page_v1";
  const HOT_REPORT_FIRST_PAGE_CACHE_VERSION = 1;
  const HOT_REPORT_FIRST_PAGE_CACHE_MAX_ITEMS = 24;
  const HOT_REPORT_FIRST_PAGE_CACHE_TTL_MS = 24 * 60 * 60 * 1000;
  const ADMIN_PDF_UPLOAD_SESSION_KEY = "portal_admin_pdf_upload_v1";
  const ADMIN_PDF_UPLOAD_SESSION_VERSION = 1;
  const ADMIN_PDF_UPLOAD_POLL_MS = 2500;
  const ADMIN_PDF_UPLOAD_POLL_LIMIT = 72;
  const ADMIN_PDF_UPLOAD_XHR_TIMEOUT_MS = 5 * 60 * 1000;
  const ADMIN_PDF_UPLOAD_STATUS_TIMEOUT_MS = 12000;
  const AUTHORITY_SOURCE = "authority";
  const REPORT_A_SOURCE = "report-a";
  const THINKTANK_SOURCE = "thinktank";
  const HOT_REPORT_SOURCE = "hot";
  const EXTERNAL_SOURCE = "external";
  const NEWSFEED_SYSTEM_TOPIC_IDS = new Set([
    "global-daily",
    "tech-ai",
    "global-politics",
    "industries",
    "investment",
  ]);
  const PDFJS_MODULE_URL = "/assets/vendor/pdfjs/pdf.mjs";
  const PDFJS_WORKER_URL = "/assets/vendor/pdfjs/pdf.worker.mjs";
  const APP_ASSET_VERSION = (() => {
    try {
      const script = document.currentScript;
      return script && script.src
        ? new URL(script.src, document.baseURI).searchParams.get("v") || ""
        : "";
    } catch (_error) {
      return "";
    }
  })();
  let accountAdminDailyPicks = new Map();
  let accountAdminMarketViews = new Map();
  let accountAdminHotReports = [];
  let accountAdminUsersByEmail = new Map();
  let accountAdminAccessOptions = {};
  let accountAdminLastSummary = null;
  let accountAdminLastSummaryOwner = "";
  let accountAdminRefreshTimer = null;
  let accountAdminListModalCleanup = null;
  let activeAdminPdfUpload = null;
  let pdfJsLoadPromise = null;
  const activeAdminButtonActions = new WeakMap();

  function versionedSiteAssetUrl(path) {
    const url = new URL(String(path || ""), document.baseURI);
    if (APP_ASSET_VERSION) url.searchParams.set("v", APP_ASSET_VERSION);
    return url.href;
  }

  const INDUSTRY_RULES = [
    ["Macro / FX / Rates", /\b(macro|fx|foreign exchange|currency|cny|yuan|dollar|usd|rate|rates|yield|fed|ecb|boj|inflation|cpi|pmi|gdp|economy|economic|recession|treasury|bond|nominal|real rate)\b/],
    ["Equity Strategy", /\b(strategy|equity strategy|market strategy|asset allocation|portfolio|index|earnings revision|valuation|eps|target price)\b/],
    ["Tech / AI / Semis", /\b(ai|artificial intelligence|semiconductor|semis|chip|chips|memory|dram|nand|hbm|gpu|server|software|cloud|data center|datacenter|robot|robotics)\b/],
    ["Internet / Media", /\b(internet|media|gaming|game|music|streaming|advertising|ecommerce|e-commerce|platform|social|takeaway|food delivery|new media)\b/],
    ["Autos / EV / Batteries", /\b(auto|autos|automotive|vehicle|ev|bev|battery|batteries|lithium|ess|adas|mobility|tesla|byd)\b/],
    ["Energy / Utilities", /\b(energy|oil|gas|lng|solar|wind|power|utility|utilities|renewable|coal|electricity|grid)\b/],
    ["Metals / Mining", /\b(metal|metals|mining|copper|aluminum|aluminium|steel|iron ore|gold|silver|nickel|commodity|commodities)\b/],
    ["Healthcare / Biotech", /\b(healthcare|health care|biotech|pharma|pharmaceutical|drug|medical|hospital|medtech|vaccine|therapy)\b/],
    ["Consumer / Retail", /\b(consumer|retail|apparel|luxury|brand|restaurant|food|beverage|travel retail|staples|discretionary)\b/],
    ["Banks / Financials", /\b(bank|banks|banking|insurance|broker|brokerage|asset manager|fintech|exchange|financials|payment)\b/],
    ["Real Estate", /\b(real estate|property|housing|developer|reit|mortgage|homebuilder|construction)\b/],
    ["Industrials / Capex", /\b(industrial|industrials|machinery|automation|capex|capital goods|aerospace|defense|rail|shipping|logistics|transport)\b/],
    ["Policy / Geopolitics", /\b(policy|politics|geopolitic|geopolitical|tariff|trade war|election|sanction|iran|russia|taiwan|strait|security)\b/],
    ["ESG / Climate", /\b(esg|climate|carbon|decarbon|emission|sustainable|sustainability|green|transition)\b/],
  ];

  const STOPWORDS = new Set([
    "the", "and", "for", "with", "from", "this", "that", "into", "after", "before", "report", "reports",
    "global", "china", "asia", "update", "updates", "note", "notes", "research", "sector", "market",
    "markets", "equity", "earnings", "preview", "review", "takeaways", "anchor", "model", "projection",
    "slightly", "likely", "better", "daily", "weekly", "monthly", "nom", "jpm", "ubs", "citi",
    "bofa", "barc", "jef", "jpmorgan", "morgan", "stanley", "goldman", "sachs", "nomura",
  ]);

  const PAGE_RANGE_FILTERS = [
    { value: "under5", label: "5页以下", matches: (pages) => pages > 0 && pages <= 5 },
    { value: "5_10", label: "5-10页", matches: (pages) => pages >= 5 && pages <= 10 },
    { value: "10_20", label: "10-20页", matches: (pages) => pages >= 10 && pages <= 20 },
    { value: "over20", label: "20页以上", matches: (pages) => pages >= 20 },
  ];

  const AUTHORITY_PAGE_RANGE_FILTERS = [
    { value: "under5", label: "≤5页", matches: (pages) => pages > 0 && pages <= 5 },
    { value: "5_10", label: "6-10页", matches: (pages) => pages >= 6 && pages <= 10 },
    { value: "10_20", label: "11-20页", matches: (pages) => pages >= 11 && pages <= 20 },
    { value: "over20", label: ">20页", matches: (pages) => pages > 20 },
  ];

  function recentMonthCutoff(months, now = Date.now()) {
    const count = Math.max(0, Number(months) || 0);
    const current = new Date(now);
    if (!count || !Number.isFinite(current.getTime())) return 0;
    const targetMonth = current.getUTCMonth() - count;
    const targetYear = current.getUTCFullYear() + Math.floor(targetMonth / 12);
    const normalizedMonth = ((targetMonth % 12) + 12) % 12;
    const lastDay = new Date(Date.UTC(targetYear, normalizedMonth + 1, 0)).getUTCDate();
    return Date.UTC(
      targetYear,
      normalizedMonth,
      Math.min(current.getUTCDate(), lastDay),
      0,
      0,
      0,
      0,
    );
  }

  function itemMatchesRecentMonths(item, months, now = Date.now()) {
    const count = Math.max(0, Number(months) || 0);
    if (!count) return true;
    const timestamp = Date.parse(String(item && item.date || "").trim());
    if (!Number.isFinite(timestamp)) return false;
    return timestamp >= recentMonthCutoff(count, now) && timestamp <= now + 24 * 60 * 60 * 1000;
  }

  function normalizeHotReportFirstPageCache(payload, now = Date.now()) {
    if (!payload || typeof payload !== "object" || Array.isArray(payload)) return null;
    if (Number(payload.version) !== HOT_REPORT_FIRST_PAGE_CACHE_VERSION) return null;
    const savedAt = Number(payload.saved_at || 0);
    const age = now - savedAt;
    if (!Number.isFinite(savedAt) || savedAt <= 0 || age < -5 * 60 * 1000 || age > HOT_REPORT_FIRST_PAGE_CACHE_TTL_MS) {
      return null;
    }
    const rawPage = payload.page;
    if (!rawPage || typeof rawPage !== "object" || Array.isArray(rawPage) || !Array.isArray(rawPage.items)) return null;
    if (rawPage.items.length > HOT_REPORT_FIRST_PAGE_CACHE_MAX_ITEMS) return null;
    const seen = new Set();
    const items = [];
    for (const rawItem of rawPage.items) {
      const id = String(rawItem && rawItem.id || "").trim().toLowerCase();
      if (!/^hot:[a-f0-9]{16}$/.test(id) || seen.has(id)) return null;
      seen.add(id);
      const size = Number(rawItem.size_bytes || 0);
      const sortOrder = Number(rawItem.sort_order || 0);
      const requiredMonths = Number(rawItem.required_months || 0);
      items.push({
        id,
        source: HOT_REPORT_SOURCE,
        title: publicBrandText(String(rawItem.title || "").trim().slice(0, 320), "近期热门报告"),
        title_cn: publicBrandText(String(rawItem.title_cn || "").trim().slice(0, 320)),
        institution: publicBrandText(String(rawItem.institution || "").trim().slice(0, 160)),
        date: String(rawItem.date || "").trim().slice(0, 10),
        description: publicBrandText(String(rawItem.description || "").trim().slice(0, 1600)),
        filename: publicBrandText(String(rawItem.filename || "").trim().slice(0, 320), "report.pdf", PUBLIC_BRAND),
        size_bytes: Number.isFinite(size) && size > 0 ? Math.floor(size) : 0,
        sort_order: Number.isSafeInteger(sortOrder) ? sortOrder : 0,
        created_at: String(rawItem.created_at || "").trim().slice(0, 64),
        updated_at: String(rawItem.updated_at || "").trim().slice(0, 64),
        required_plan: publicBrandText(String(rawItem.required_plan || "").trim().slice(0, 64)),
        required_months: Number.isFinite(requiredMonths) && requiredMonths > 0 ? Math.floor(requiredMonths) : 0,
      });
    }
    const rawTotal = rawPage.total;
    const total = rawTotal === null || rawTotal === undefined
      ? null
      : Number(rawTotal);
    if (total !== null && (!Number.isSafeInteger(total) || total < items.length)) return null;
    const nextCursor = String(rawPage.nextCursor || "").trim();
    const hasMore = rawPage.hasMore === true;
    if (nextCursor.length > 2048 || hasMore !== Boolean(nextCursor)) return null;
    return {
      items,
      nextCursor,
      hasMore,
      total,
      cachedAt: savedAt,
    };
  }

  function hotReportLocalStorage() {
    try {
      return window.localStorage;
    } catch (_error) {
      return null;
    }
  }

  function readHotReportFirstPageCache(storage, now = Date.now()) {
    if (!storage || typeof storage.getItem !== "function") return null;
    try {
      const parsed = JSON.parse(storage.getItem(HOT_REPORT_FIRST_PAGE_CACHE_KEY) || "null");
      const normalized = normalizeHotReportFirstPageCache(parsed, now);
      if (!normalized && typeof storage.removeItem === "function") storage.removeItem(HOT_REPORT_FIRST_PAGE_CACHE_KEY);
      return normalized;
    } catch (_error) {
      try {
        if (typeof storage.removeItem === "function") storage.removeItem(HOT_REPORT_FIRST_PAGE_CACHE_KEY);
      } catch (_removeError) {
        // Ignore unavailable browser storage.
      }
      return null;
    }
  }

  function writeHotReportFirstPageCache(page, storage, now = Date.now()) {
    if (!storage || typeof storage.setItem !== "function") return false;
    const normalized = normalizeHotReportFirstPageCache({
      version: HOT_REPORT_FIRST_PAGE_CACHE_VERSION,
      saved_at: now,
      page,
    }, now);
    if (!normalized) return false;
    try {
      storage.setItem(HOT_REPORT_FIRST_PAGE_CACHE_KEY, JSON.stringify({
        version: HOT_REPORT_FIRST_PAGE_CACHE_VERSION,
        saved_at: normalized.cachedAt,
        page: {
          items: normalized.items,
          nextCursor: normalized.nextCursor,
          hasMore: normalized.hasMore,
          total: normalized.total,
        },
      }));
      return true;
    } catch (_error) {
      return false;
    }
  }

  function recentDateBounds(months, now = Date.now()) {
    const count = Math.max(0, Number(months) || 0);
    const cutoff = recentMonthCutoff(count, now);
    const current = new Date(now);
    if (!count || !cutoff || !Number.isFinite(current.getTime())) {
      return { startDate: "", endDate: "" };
    }
    return {
      startDate: new Date(cutoff).toISOString().slice(0, 10),
      endDate: current.toISOString().slice(0, 10),
    };
  }

  function embeddedSearchRequestUrl(baseUrl, path, query, filters = {}, now = Date.now(), documentUrl = "") {
    const referenceUrl = documentUrl
      || (typeof window !== "undefined" && window.location && window.location.href)
      || "https://portal.example.invalid/";
    const base = new URL(`${String(baseUrl || "/api").replace(/\/$/, "")}/`, referenceUrl);
    const url = new URL(path, base);
    url.searchParams.set("q", String(query || "").trim());
    const bounds = recentDateBounds(filters.recentMonths, now);
    if (bounds.startDate) url.searchParams.set("start_date", bounds.startDate);
    if (bounds.endDate) url.searchParams.set("end_date", bounds.endDate);
    if (path === "external/search") {
      url.searchParams.set("include_html", filters.includeHtml ? "1" : "0");
    }
    if (path === "authority/search") {
      const institution = String(filters.institution || "").trim();
      const pageRange = String(filters.pageRange || "").trim();
      if (institution) url.searchParams.set("institution", institution);
      if (pageRange) url.searchParams.set("page_range", pageRange);
    }
    return url.toString();
  }

  function isExternalHtmlItem(item) {
    const fileType = String(item && item.file_type || "").trim().toLowerCase();
    return fileType === "html" || fileType === "htm" || /(?:^|[\s/.+-])html?(?:$|[\s/.+-])/.test(fileType);
  }

  function externalSearchView(items, filters = {}, now = Date.now()) {
    const rows = Array.isArray(items) ? items : [];
    const recentMonths = Math.max(0, Number(filters.recentMonths) || 0);
    const dateMatched = rows.filter((item) => itemMatchesRecentMonths(item, recentMonths, now));
    const nonHtml = dateMatched.filter((item) => !isExternalHtmlItem(item));
    const includeHtml = Boolean(filters.includeHtml);
    const htmlFallback = !includeHtml
      && Boolean(filters.allowHtmlFallback)
      && dateMatched.length > 0
      && nonHtml.length === 0;
    const visible = includeHtml || htmlFallback ? dateMatched : nonHtml;
    return {
      items: visible,
      dateMatchedCount: dateMatched.length,
      hiddenHtmlCount: Math.max(0, dateMatched.length - visible.length),
      htmlFallback,
    };
  }

  function authoritySearchView(items, filters = {}, now = Date.now()) {
    const institution = String(filters.institution || "").trim();
    const recentMonths = Math.max(0, Number(filters.recentMonths) || 0);
    const pageRange = authorityPageRangeForValue(String(filters.pageRange || ""));
    return (Array.isArray(items) ? items : []).filter((item) => {
      if (institution && String(item && item.institution || "").trim() !== institution) return false;
      if (!itemMatchesRecentMonths(item, recentMonths, now)) return false;
      if (pageRange && !pageRange.matches(reportPageCountValue(item))) return false;
      return true;
    });
  }

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  const LEGACY_SOURCE_WORDS = [
    ["report", "ify"],
    ["nash", "ai"],
    ["mai", "fu"],
  ];
  const LEGACY_SOURCE_DOMAIN_WORDS = [
    ["report", "ify", "cn"],
    ["nash", "ai", "cn"],
    ["hi", "bor", "com", "cn"],
  ];
  const LEGACY_CONTACT_WORDS = [
    ["macro", "gate"],
    ["support", "contact"],
    ["portal", "suite"],
    ["portal", "alternate"],
    ["portal", "娱乐"],
    ["kc", "desk", "notes"],
    ["two", "tigers"],
  ];

  function legacyBrandPattern(parts) {
    const escaped = parts.map((part) => String(part).replace(/[.*+?^${}()|[\]\\]/g, "\\$&"));
    return new RegExp(escaped.join("[\\s._-]*"), "gi");
  }

  function publicBrandInput(value) {
    return String(value || "")
      .replace(/[\u200b-\u200d\u2060\ufeff]/g, "")
      .replace(/[Ａ-Ｚａ-ｚ０-９]/g, (character) => String.fromCharCode(character.charCodeAt(0) - 0xfee0));
  }

  function publicBrandText(value, fallback = "", replacement = "") {
    const original = String(value || "");
    let text = publicBrandInput(original);
    for (const parts of LEGACY_SOURCE_DOMAIN_WORDS) {
      text = text.replace(legacyBrandPattern(parts), replacement);
    }
    for (const parts of [...LEGACY_SOURCE_WORDS, ...LEGACY_CONTACT_WORDS]) {
      text = text.replace(legacyBrandPattern(parts), replacement);
    }
    const legacyChineseSource = String.fromCharCode(0x6167, 0x535a);
    text = text.replace(new RegExp(legacyChineseSource, "g"), replacement);
    const legacyCourseBrand = String.fromCharCode(0x9ea6, 0x5e9c, 0x5b66, 0x5802);
    text = text.replace(new RegExp(legacyCourseBrand, "g"), replacement);
    const legacyCourseClassroom = String.fromCharCode(0x9ea6, 0x5e9c, 0x8bfe, 0x5802);
    text = text.replace(new RegExp(legacyCourseClassroom, "g"), replacement);
    const changed = text !== original;
    if (changed) {
      text = text
        .replace(/\(\s*\)|（\s*）|\[\s*\]|【\s*】/g, " ")
        .replace(/\s+([,.;:!?，。；：！？])/g, "$1")
        .replace(/([\[(（【])\s+/g, "$1")
        .replace(/\s{2,}/g, " ")
        .replace(/^[\s:：|·/\\,，;；\-–—_]+|[\s:：|·/\\,，;；\-–—_]+$/g, "")
        .trim();
    } else {
      text = text.trim();
    }
    if (changed && !replacement) {
      text = text
        .replace(/^(?:from|by|via|sourced?\s+from|source)\s*[:：|·/\\,，;；\-–—_]*\s*/i, "")
        .replace(/^(?:来源于?|来自)\s*[:：|·/\\,，;；\-–—_]*\s*/u, "")
        .replace(/\s+(?:from|by|via)\s*$/i, "")
        .replace(/^[\s:：|·/\\,，;；\-–—_]+|[\s:：|·/\\,，;；\-–—_]+$/g, "")
        .trim();
    }
    return text || String(fallback || "");
  }

  function publicMessageText(value, fallback = "") {
    let text = publicBrandInput(value);
    for (const parts of LEGACY_CONTACT_WORDS) {
      text = text.replace(legacyBrandPattern(parts), PUBLIC_BRAND);
    }
    for (const parts of LEGACY_SOURCE_DOMAIN_WORDS) {
      text = text.replace(legacyBrandPattern(parts), PUBLIC_BRAND);
    }
    for (const parts of LEGACY_SOURCE_WORDS) {
      text = text.replace(legacyBrandPattern(parts), PUBLIC_BRAND);
    }
    text = text.replace(new RegExp(String.fromCharCode(0x6167, 0x535a), "g"), PUBLIC_BRAND);
    text = text
      .replace(/Contact\s+WeChat\s*:\s*[^\s，。；;]+/gi, `Use the in-site request button to contact ${PUBLIC_BRAND}`)
      .replace(/WeChat\s*:\s*[^\s，。；;]+/gi, `contact ${PUBLIC_BRAND} through the in-site request button`)
      .replace(/(?:send\s+)?email(?:\s+to)?\s*[:：]?\s*[^\s，。；;]+/gi, `use the in-site request button`)
      .replace(/联系微信号?\s*[:：]?\s*[^\s，。；;]+/gi, `请通过站内申请入口联系${PUBLIC_BRAND}`)
      .replace(/联系微信\s+[^\s，。；;]+/gi, `请通过站内申请入口联系${PUBLIC_BRAND}`)
      .replace(/(?:请)?联系邮箱\s*[:：]?\s*[^\s，。；;]+/gi, `请通过站内申请入口联系${PUBLIC_BRAND}`);
    return publicBrandText(text, fallback, PUBLIC_BRAND);
  }

  function publicDocItem(value) {
    if (!value || typeof value !== "object") return value;
    const item = { ...value };
    for (const key of [
      "title", "title_cn", "title_zh", "institution", "institution_name", "bank_name",
      "bank_code", "description", "summary", "author", "category", "kind_label", "language",
      "filename", "report_type", "rating", "file_type",
    ]) {
      if (Object.prototype.hasOwnProperty.call(item, key)) item[key] = publicBrandText(item[key]);
    }
    if (Object.prototype.hasOwnProperty.call(item, "channel_name")) delete item.channel_name;
    return item;
  }

  function publicSearchItem(value, source = "") {
    const item = publicDocItem(value) || {};
    if (source === EXTERNAL_SOURCE) {
      item.institution = publicBrandText(item.institution || item.institution_name || "");
      delete item.institution_name;
      delete item.channel_name;
    }
    return item;
  }

  function publicDisplayName(value) {
    const clean = publicBrandText(value);
    return clean || `${PUBLIC_BRAND}用户`;
  }

  function accessContactGuidanceHtml() {
    return `如需开通或调整下载权限，<button class="inline-request-button" type="button" data-membership-request-open="access">提交站内申请</button>。`;
  }

  function requestKindForVisibleMessage(value) {
    const text = String(value || "");
    if (/权限|无权|解锁|体验下载已满|limit_exceeded|3\s*个月/iu.test(text)) return "access";
    if (/失败|未完成|异常|超时|不可用|超过预期|support|failed|failure|error|timed?\s*out|temporarily unavailable|could not|cannot|can't|稍后重试/iu.test(text)) return "support";
    return "";
  }

  function requestActionStatusHtml(value, requestedKind = "") {
    const text = publicMessageText(value);
    const kind = membershipRequestKind(requestedKind || requestKindForVisibleMessage(text));
    const label = kind === "access" ? "提交权限申请" : "提交支持请求";
    return `${escapeHtml(text)} <button class="inline-request-button" type="button" data-membership-request-open="${kind}">${label}</button>`;
  }

  function registrationNoticeText(mode = "login") {
    return mode === "register"
      ? "请填写常用邮箱。注册仅创建登录账号；注册后可在账户中心申请加入会员。"
      : "没有账号？请注册并填写常用邮箱，也可以直接提交会员申请。";
  }

  function registrationCompleteText() {
    return "注册成功。可在下方提交会员申请或查看会员联系方式。";
  }

  function localizedContactText(value) {
    return publicMessageText(value);
  }

  function normalize(value) {
    return String(value || "")
      .normalize("NFKC")
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function queryTokens(value) {
    return normalize(value).split(" ").filter(Boolean);
  }

  function textMatches(text, query) {
    if (!query) return true;
    if (text.includes(query)) return true;
    const tokens = query.split(" ").filter(Boolean);
    return tokens.length > 0 && tokens.every((token) => text.includes(token));
  }

  function scoreText(text, query, weight) {
    if (!query) return 0;
    let score = 0;
    if (text.includes(query)) score += 10 * weight;
    for (const token of query.split(" ").filter(Boolean)) {
      if (text.includes(token)) score += weight;
    }
    return score;
  }

  async function loadJson(path, options = {}) {
    // Static JSON is revisioned at the edge and has validators. Let the browser
    // reuse it across visits; API requests continue to opt into no-store at
    // their individual call sites.
    const response = await fetch(path, { cache: "default", ...options });
    if (!response.ok) {
      throw new Error(`Could not load ${path}: ${response.status}`);
    }
    return response.json();
  }

  async function fetchRewardRequest(input, init = {}, timeoutMessage = "请求超时，请重试。", timeoutMs = 18_000) {
    const controller = new AbortController();
    let timeoutId = 0;
    const timeoutError = () => {
      const error = new Error(timeoutMessage);
      error.name = "RewardTimeoutError";
      return error;
    };
    const timeoutPromise = new Promise((_, reject) => {
      timeoutId = window.setTimeout(() => {
        controller.abort();
        reject(timeoutError());
      }, timeoutMs);
    });
    try {
      return await Promise.race([
        fetch(input, { ...init, signal: controller.signal }),
        timeoutPromise,
      ]);
    } catch (error) {
      if (error && error.name === "AbortError") throw timeoutError();
      throw error;
    } finally {
      window.clearTimeout(timeoutId);
    }
  }

  async function loadOptionalJson(path, fallback) {
    try {
      return await loadJson(path);
    } catch (error) {
      console.warn(error);
      return fallback;
    }
  }

  function getCookie(name) {
    const prefix = `${name}=`;
    return document.cookie
      .split(";")
      .map((part) => part.trim())
      .find((part) => part.startsWith(prefix))
      ?.slice(prefix.length) || "";
  }

  function setCookie(name, value, maxAge) {
    document.cookie = `${name}=${encodeURIComponent(value)}; Max-Age=${maxAge}; Path=/; SameSite=Lax; Secure`;
  }

  function clearCookie(name) {
    document.cookie = `${name}=; Max-Age=0; Path=/; SameSite=Lax; Secure`;
  }

  function getAdminToken() {
    try {
      const stored = localStorage.getItem(ADMIN_TOKEN_KEY);
      if (stored) {
        const data = JSON.parse(stored);
        if (!data.expiresAt || Date.parse(data.expiresAt) > Date.now()) return data.token || "";
      }
    } catch (_error) {
      // Fall back to the cookie below.
    }
    return decodeURIComponent(getCookie(ADMIN_COOKIE_NAME) || "");
  }

  function setAdminToken(token, expiresAt) {
    const value = String(token || "");
    if (!value) return;
    try {
      localStorage.setItem(ADMIN_TOKEN_KEY, JSON.stringify({ token: value, expiresAt: expiresAt || "" }));
    } catch (_error) {
      // Cookie still keeps the device remembered.
    }
    setCookie(ADMIN_COOKIE_NAME, value, ADMIN_COOKIE_MAX_AGE);
    document.dispatchEvent(new CustomEvent("portal-admin-change"));
  }

  function setAdminPlainKey(value) {
    try {
      localStorage.setItem(ADMIN_PLAIN_KEY, String(value || ""));
    } catch (_error) {
      // Admin token still keeps the device unlocked.
    }
  }

  function getAdminPlainKey() {
    try {
      return localStorage.getItem(ADMIN_PLAIN_KEY) || "";
    } catch (_error) {
      return "";
    }
  }

  function clearAdminToken() {
    try {
      localStorage.removeItem(ADMIN_TOKEN_KEY);
      localStorage.removeItem(ADMIN_PLAIN_KEY);
    } catch (_error) {
      // Ignore localStorage access errors.
    }
    clearCookie(ADMIN_COOKIE_NAME);
    document.dispatchEvent(new CustomEvent("portal-admin-change"));
  }

  function workerBaseUrl(config) {
    const configured = String((config && config.worker_base_url) || "/api").replace(/\/$/, "");
    try {
      const url = new URL(configured, window.location.href);
      if (url.hostname.endsWith("workers.dev") && window.location.hostname.endsWith("portal.example.invalid")) {
        return "/api";
      }
    } catch (_error) {
      // Relative URLs are fine.
    }
    return configured || "/api";
  }

  function loadAuthSession() {
    try {
      const raw = localStorage.getItem(AUTH_SESSION_KEY);
      if (!raw) return null;
      const session = JSON.parse(raw);
      if (!session || !session.token || !session.user || !session.user.email) return null;
      return session;
    } catch (_error) {
      return null;
    }
  }

  function saveAuthSession(session) {
    try {
      localStorage.setItem(AUTH_SESSION_KEY, JSON.stringify(session));
    } catch (_error) {
      // Ignore storage errors; the current page still has the response.
    }
    document.dispatchEvent(new CustomEvent("portal-auth-change"));
  }

  function clearAuthSession() {
    try {
      localStorage.removeItem(AUTH_SESSION_KEY);
    } catch (_error) {
      // Ignore storage errors.
    }
    document.dispatchEvent(new CustomEvent("portal-auth-change"));
  }

  function authHeaders() {
    const session = loadAuthSession();
    return session && session.token ? { "Authorization": `Bearer ${session.token}` } : {};
  }

  function randomVisitorId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    return `v-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`;
  }

  function visitorId() {
    try {
      let value = localStorage.getItem(VISITOR_ID_KEY) || "";
      if (!value) {
        value = randomVisitorId();
        localStorage.setItem(VISITOR_ID_KEY, value);
      }
      return value;
    } catch (_error) {
      return "";
    }
  }

  function currentAnalyticsPath() {
    return String(window.location.pathname || "/").slice(0, 240);
  }

  function currentAnalyticsReferrer() {
    if (!String(document.referrer || "").trim()) return "";
    try {
      const url = new URL(String(document.referrer || ""), window.location.origin);
      if (!/^https?:$/.test(url.protocol)) return "";
      return `${url.origin}${url.pathname}`.slice(0, 320);
    } catch (_error) {
      return "";
    }
  }

  function trackEvent(workerUrl, type, data = {}) {
    if (window.PortalSuiteAnalytics && typeof window.PortalSuiteAnalytics.track === "function") {
      window.PortalSuiteAnalytics.track(type, { page, ...data });
      return;
    }
    if (!workerUrl) return;
    const payload = {
      type,
      visitor_id: visitorId(),
      path: currentAnalyticsPath(),
      data: {
        page,
        referrer: currentAnalyticsReferrer(),
        ...data,
      },
    };
    try {
      fetch(`${workerUrl}/analytics`, {
        method: "POST",
        cache: "no-store",
        keepalive: true,
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify(payload),
      }).catch(() => {});
    } catch (_error) {
      // Analytics should never block the user flow.
    }
  }

  function analyticsReportPayload(item, source = "catalog") {
    return {
      source,
      report_id: item && item.id || "",
      report_title: item ? publicBrandText(item.title || item.title_zh || item.filename || "") : "",
      institution: item ? publicBrandText(item.institution || item.bank_code || item.bank_name || "") : "",
    };
  }

  function authUserLabel(session) {
    const user = session && session.user;
    if (!user) return "登录";
    return "账户";
  }

  function accountRightLabel(row = {}) {
    if (!row || !row.active) return "";
    if (row.access_mode === "all") return "全站报告下载权限";
    if (row.access_mode === "filters") {
      const institutions = Array.isArray(row.institutions) ? row.institutions.map((value) => publicBrandText(value)).filter(Boolean) : [];
      const industries = Array.isArray(row.industries) ? row.industries.map((value) => publicBrandText(value)).filter(Boolean) : [];
      if (institutions.length === 1 && !industries.length && !(row.page_ranges || []).length) {
        return `${institutions[0]}报告下载权限`;
      }
      if (institutions.length) return `机构报告下载权限（${institutions.slice(0, 3).join("、")}）`;
      if (industries.length) return `行业报告下载权限（${industries.slice(0, 3).join("、")}）`;
      return "条件报告下载权限";
    }
    if (["vid2ppt_nova", "vid2ppt_atlas"].includes(row.source) || ["vid2ppt_nova", "vid2ppt_atlas"].includes(row.grant_source)) return "历史会员下载权益";
    if (row.plan === "annual") return "会员下载权限";
    if (row.plan === "super" || row.plan === "operator") return "账号下载权限";
    return "下载权限";
  }

  function accountRightDurationText(row = {}) {
    if (!row || !row.active || row.lifetime) return "";
    const value = String(row.duration_value || "").trim();
    if (value === "trial_3d") return "3天体验";
    const months = Number(value);
    if (!Number.isInteger(months) || months <= 0) return "";
    if (months % 12 === 0) return `${months / 12}年`;
    return `${months}个月`;
  }

  function accountRightExpiryText(row = {}) {
    if (!row || !row.active) return "";
    if (row.lifetime) return "长期有效";
    const end = String(row.current_period_end || "").slice(0, 10);
    return end ? `有效期至 ${end}` : "";
  }

  function accountRightUsageText(row = {}) {
    const limit = Number(row.download_limit || 0);
    if (!limit) return "";
    const count = Math.max(0, Number(row.download_count || 0));
    const remaining = Math.max(0, limit - count);
    return `体验剩余 ${remaining}/${limit} 篇`;
  }

  function accountRightSummary(data = {}) {
    const effective = data && data.effective_access;
    if (effective) {
      if (effective.source === "error") return "权限核验失败（已拒绝）";
      if (effective.active) {
        return [accountRightLabel(effective), accountRightDurationText(effective), accountRightExpiryText(effective), accountRightUsageText(effective)].filter(Boolean).join("，");
      }
      return "";
    }
    const access = data && data.access;
    if (access && access.active) {
      return [accountRightLabel(access), accountRightDurationText(access), accountRightExpiryText(access), accountRightUsageText(access)].filter(Boolean).join("，");
    }
    const entitlement = data && data.entitlement;
    if (entitlement && entitlement.active && (entitlement.plan === "annual" || entitlement.plan === "super" || entitlement.plan === "operator")) {
      return [accountRightLabel(entitlement), accountRightExpiryText(entitlement)].filter(Boolean).join("，");
    }
    return "";
  }

  function isSuperSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user && (user.role === "super" || user.is_super));
  }

  function isAdminASession(session = loadAuthSession()) {
    return isSuperSession(session);
  }

  function isOperatorSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user && (user.role === "operator" || user.is_operator));
  }

  function canOpenOperationsPanel(session = loadAuthSession()) {
    return isSuperSession(session) || isOperatorSession(session);
  }

  function isNewsfeedSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user) && !user.disabled && user.account_status !== "disabled" && user.status !== "disabled";
  }

  const MEMBERSHIP_REQUEST_KINDS = new Set(["membership", "support", "privacy", "refund", "access"]);

  function membershipRequestKind(value) {
    const kind = String(value || "").trim().toLowerCase();
    return MEMBERSHIP_REQUEST_KINDS.has(kind) ? kind : "membership";
  }

  function membershipRequestCopy(value) {
    const kind = membershipRequestKind(value);
    const copy = {
      membership: { title: "申请加入会员", button: "提交会员申请", note: "留下常用联系方式，KC桌面收到后会与你联系。" },
      support: { title: "联系 KC桌面", button: "提交联系请求", note: "请留下常用联系方式和需要协助的事项。" },
      privacy: { title: "提交隐私请求", button: "提交隐私请求", note: "请在备注中说明查询、更正或删除需求。" },
      refund: { title: "提交支持请求", button: "提交支持请求", note: "请在备注中说明账号、开通时间和需要协助的事项。" },
      access: { title: "申请开通或调整权限", button: "提交权限申请", note: "请留下常用联系方式，并在备注中说明需要的报告范围。" },
    };
    return { kind, ...copy[kind] };
  }

  function privateToolsUnlocked() {
    return Boolean(getAdminToken() || isSuperSession());
  }

  function canUseDeliveryTools(session = loadAuthSession()) {
    if (canOpenOperationsPanel(session)) return true;
    return !session && Boolean(getAdminToken());
  }

  async function refreshAuthSession(workerUrl) {
    const session = loadAuthSession();
    if (!session || !session.token || !workerUrl) return null;
    try {
      const response = await fetch(`${workerUrl}/auth`, {
        cache: "no-store",
        headers: authHeaders(),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "Session expired.");
      saveAuthSession({ token: data.token, user: data.user });
      return { token: data.token, user: data.user };
    } catch (_error) {
      clearAuthSession();
      return null;
    }
  }

  function initAccountGate(workerUrl) {
    const gate = document.getElementById("accountGate");
    if (gate) {
      function update() {
        const session = loadAuthSession();
        gate.textContent = authUserLabel(session);
        gate.classList.toggle("is-unlocked", Boolean(session));
      }
      update();
      document.addEventListener("portal-auth-change", update);
      gate.addEventListener("click", () => showAccountModal(workerUrl));
      refreshAuthSession(workerUrl).then(update);
    }

    document.addEventListener("click", (event) => {
      const trigger = event.target && event.target.closest
        ? event.target.closest("[data-membership-request-open]")
        : null;
      if (!trigger) return;
      event.preventDefault();
      showAccountModal(workerUrl, {
        requestKind: membershipRequestKind(trigger.getAttribute("data-membership-request-open")),
      });
    });

    const deepLinkKind = new URLSearchParams(window.location.search).get("request");
    if (deepLinkKind && MEMBERSHIP_REQUEST_KINDS.has(String(deepLinkKind).trim().toLowerCase())) {
      window.setTimeout(() => showAccountModal(workerUrl, { requestKind: membershipRequestKind(deepLinkKind) }), 0);
    }
  }

  function initNewsfeedNav() {
    const links = Array.from(document.querySelectorAll("#newsfeedNav"));
    if (!links.length) return;
    links.forEach((link) => {
      link.hidden = false;
    });
  }

  function accountModalMarkup(context = {}) {
    const session = loadAuthSession();
    const signedIn = Boolean(session);
    const requestCopy = membershipRequestCopy(context.requestKind);
    const requestExpanded = Boolean(context.requestKind);
    const requesterEmail = signedIn && session.user ? String(session.user.email || "").trim() : "";
    const reportTitle = context.item ? titleText(context.item) : "";
    const reportLine = reportTitle ? `<span>当前报告：${escapeHtml(reportTitle)}</span>` : "";
    const reportHelp = `<span>${accessContactGuidanceHtml()}</span>`;
    const reportContactCard = context.item ? `
      <div class="contact-card" id="accountContactCard">
        <strong>报告获取</strong>
        ${reportLine}
        ${reportHelp}
      </div>
    ` : "";
    const rewardReportActions = context.item && String(context.source || "catalog") === "catalog"
      ? `
        <div class="account-reward-claim" id="accountRewardClaim">
          <span>领取当前报告</span>
          <div class="account-modal-actions">
            <button class="secondary-button" id="accountRewardDailyClaim" type="button">使用报告券</button>
            <button class="secondary-button" id="accountRewardPointsClaim" type="button">使用 70 积分</button>
          </div>
        </div>
      `
      : "";
    return `
      <div class="admin-modal account-modal" id="accountModal" role="dialog" aria-modal="true" aria-labelledby="accountModalTitle">
        <div class="admin-dialog account-dialog">
          <button class="admin-close" id="accountClose" type="button" aria-label="Close">&times;</button>
          <h3 id="accountModalTitle">账号管理</h3>
          <form id="accountAuthForm" class="auth-form" ${signedIn ? "hidden" : ""}>
            <div class="auth-grid">
              <label>用户名<input id="accountUsername" type="text" autocomplete="username" placeholder="yourname" required></label>
              <label id="accountEmailLabel" hidden>常用邮箱（必填）<input id="accountEmail" type="email" autocomplete="email" inputmode="email" placeholder="you@example.com"></label>
              <label>密码<input id="accountPassword" type="password" autocomplete="current-password" placeholder="至少 4 位" required></label>
            </div>
            <p class="auth-registration-notice" id="accountRegistrationNotice">${escapeHtml(registrationNoticeText("login"))}</p>
            <label class="captcha-field">验证码
              <div class="captcha-row">
                <img id="accountCaptchaImage" alt="验证码">
                <button class="secondary-button" id="accountRefreshCaptcha" type="button">换一张</button>
              </div>
              <input id="accountCaptchaAnswer" type="text" inputmode="numeric" autocomplete="off" placeholder="输入结果" required>
            </label>
            <div class="account-modal-actions">
              <button class="primary" id="accountSubmit" type="submit">登录</button>
              <button class="secondary-button" id="accountModeToggle" type="button">注册新账号</button>
            </div>
          </form>
          <div id="accountSummary" class="account-summary" ${signedIn ? "" : "hidden"}>
            <span>当前账号</span>
            <strong id="accountName">${escapeHtml(authUserLabel(session))}</strong>
            <span id="accountEmailText">${escapeHtml(session && session.user ? session.user.email : "")}</span>
            <div class="account-modal-actions">
              <button class="secondary-button quiet-admin-button" id="accountAdminOpen" type="button" hidden>管理后台</button>
              <button class="secondary-button" id="accountLogout" type="button">退出登录</button>
            </div>
            <form id="accountPasswordForm" class="account-password-form">
              <span>需要改密码可以在这里更新。</span>
              <div class="account-password-grid">
                <input id="accountCurrentPassword" type="password" autocomplete="current-password" placeholder="当前密码" required>
                <input id="accountNewPassword" type="password" autocomplete="new-password" placeholder="新密码" required>
                <input id="accountNewPasswordConfirm" type="password" autocomplete="new-password" placeholder="确认新密码" required>
              </div>
              <button class="secondary-button" id="accountPasswordSubmit" type="submit">修改密码</button>
            </form>
            <section class="account-rewards" id="accountRewards" hidden>
              <div class="account-rewards-heading">
                <div>
                  <span>每日签到</span>
                  <strong><b id="accountRewardStreak">0</b> 天连续</strong>
                </div>
                <div>
                  <span>可用积分</span>
                  <strong><b id="accountRewardPoints">0</b> 分</strong>
                </div>
                <div>
                  <span>报告券</span>
                  <strong><b id="accountRewardCredits">0</b> 张</strong>
                </div>
              </div>
              <p id="accountRewardHint">首签立即得 1 张报告券，第 3 天再得 1 张；每日签到 +10 分，70 分可兑换 1 份报告。</p>
              <button class="primary" id="accountRewardCheckin" type="button">今日签到 +10</button>
              ${rewardReportActions}
              <div id="accountRewardStatus" class="status-line" aria-live="polite"></div>
            </section>
          </div>
          <section class="account-member-contact" id="accountMemberContact" hidden>
            <div>
              <strong>KC桌面会员联系</strong>
              <span>仅当前已登录的注册用户可查看联系二维码。</span>
            </div>
            <button class="secondary-button" id="accountContactQrToggle" type="button" hidden>重新加载二维码</button>
            <div class="account-contact-qr" id="accountContactQrPanel" hidden>
              <img id="accountContactQrImage" alt="KC桌面会员联系二维码">
            </div>
            <div id="accountContactQrStatus" class="status-line" aria-live="polite"></div>
          </section>
          <section class="membership-request-card" id="membershipRequestCard">
            <div class="membership-request-heading">
              <div>
                <strong id="membershipRequestTitle">${escapeHtml(requestCopy.title)}</strong>
                <span id="membershipRequestNote">${escapeHtml(requestCopy.note)}</span>
              </div>
              <button class="secondary-button" id="membershipRequestToggle" type="button">${requestExpanded ? "收起申请表" : requestCopy.title}</button>
            </div>
            <form id="membershipRequestForm" ${requestExpanded ? "" : "hidden"}>
              <input id="membershipRequestKind" type="hidden" value="${escapeHtml(requestCopy.kind)}">
              <div class="membership-request-grid">
                <label>常用邮箱
                  <input id="membershipRequesterEmail" name="requester_email" type="email" autocomplete="email" inputmode="email" value="${escapeHtml(requesterEmail)}" placeholder="name@example.com"${signedIn ? " readonly" : ""} required>
                </label>
                <label>首选即时联系方式
                  <select id="membershipContactChannel" name="contact_channel" required>
                    <option value="">请选择</option>
                    <option value="wechat">微信</option>
                    <option value="whatsapp">WhatsApp</option>
                    <option value="telegram">Telegram</option>
                  </select>
                </label>
                <label class="membership-contact-value">账号或手机号
                  <input id="membershipContactValue" name="contact_value" type="text" autocomplete="off" maxlength="160" placeholder="请填写对应账号或手机号" required>
                </label>
              </div>
              <label>备注（可选）
                <textarea id="membershipRequestMessage" name="note" rows="3" maxlength="600" placeholder="例如：希望开通的报告范围或需要协助的事项"></textarea>
              </label>
              <label class="membership-request-trap" aria-hidden="true">请勿填写
                <input id="membershipRequestWebsite" name="website" type="text" tabindex="-1" autocomplete="off">
              </label>
              <button class="primary" id="membershipRequestSubmit" type="submit">${escapeHtml(requestCopy.button)}</button>
              <div id="membershipRequestStatus" class="status-line" aria-live="polite"></div>
            </form>
          </section>
          ${reportContactCard}
          <div id="accountModalStatus" class="status-line" aria-live="polite"></div>
        </div>
      </div>
    `;
  }

  async function loadAccountCaptcha(workerUrl, status) {
    const image = document.getElementById("accountCaptchaImage");
    const refresh = document.getElementById("accountRefreshCaptcha");
    if (!image || !refresh) return "";
    refresh.disabled = true;
    try {
      const response = await fetch(`${workerUrl}/captcha`, { cache: "no-store" });
      const data = await response.json();
      if (!response.ok || !data.image || !data.token) throw new Error(data.detail || "验证码加载失败。");
      image.src = data.image;
      return data.token;
    } catch (error) {
      status.textContent = error.message || "验证码加载失败。";
      status.className = "status-line error";
      return "";
    } finally {
      refresh.disabled = false;
    }
  }

  async function showAccountModal(workerUrl, context = {}) {
    if (!workerUrl) {
      window.alert("Account service is temporarily unavailable.");
      return "";
    }
    const existing = document.getElementById("accountModal");
    if (existing && typeof existing.__portalCleanup === "function") existing.__portalCleanup();
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", accountModalMarkup(context));

    const modal = document.getElementById("accountModal");
    const close = document.getElementById("accountClose");
    const form = document.getElementById("accountAuthForm");
    const summary = document.getElementById("accountSummary");
    const username = document.getElementById("accountUsername");
    const emailLabel = document.getElementById("accountEmailLabel");
    const email = document.getElementById("accountEmail");
    const registrationNotice = document.getElementById("accountRegistrationNotice");
    const password = document.getElementById("accountPassword");
    const answer = document.getElementById("accountCaptchaAnswer");
    const refresh = document.getElementById("accountRefreshCaptcha");
    const submit = document.getElementById("accountSubmit");
    const toggle = document.getElementById("accountModeToggle");
    const logout = document.getElementById("accountLogout");
    const adminOpen = document.getElementById("accountAdminOpen");
    const passwordForm = document.getElementById("accountPasswordForm");
    const currentPassword = document.getElementById("accountCurrentPassword");
    const newPassword = document.getElementById("accountNewPassword");
    const newPasswordConfirm = document.getElementById("accountNewPasswordConfirm");
    const passwordSubmit = document.getElementById("accountPasswordSubmit");
    const contactCard = document.getElementById("accountContactCard");
    const memberContact = document.getElementById("accountMemberContact");
    const contactQrToggle = document.getElementById("accountContactQrToggle");
    const contactQrPanel = document.getElementById("accountContactQrPanel");
    const contactQrImage = document.getElementById("accountContactQrImage");
    const contactQrStatus = document.getElementById("accountContactQrStatus");
    const membershipRequestToggle = document.getElementById("membershipRequestToggle");
    const membershipRequestForm = document.getElementById("membershipRequestForm");
    const membershipRequestKindInput = document.getElementById("membershipRequestKind");
    const membershipRequesterEmail = document.getElementById("membershipRequesterEmail");
    const membershipContactChannel = document.getElementById("membershipContactChannel");
    const membershipContactValue = document.getElementById("membershipContactValue");
    const membershipRequestMessage = document.getElementById("membershipRequestMessage");
    const membershipRequestWebsite = document.getElementById("membershipRequestWebsite");
    const membershipRequestSubmit = document.getElementById("membershipRequestSubmit");
    const membershipRequestStatus = document.getElementById("membershipRequestStatus");
    const status = document.getElementById("accountModalStatus");
    const rewards = document.getElementById("accountRewards");
    const rewardPoints = document.getElementById("accountRewardPoints");
    const rewardStreak = document.getElementById("accountRewardStreak");
    const rewardCredits = document.getElementById("accountRewardCredits");
    const rewardHint = document.getElementById("accountRewardHint");
    const rewardCheckin = document.getElementById("accountRewardCheckin");
    const rewardDailyClaim = document.getElementById("accountRewardDailyClaim");
    const rewardPointsClaim = document.getElementById("accountRewardPointsClaim");
    const rewardStatus = document.getElementById("accountRewardStatus");
    let mode = "login";
    let captchaToken = "";
    let currentRewardState = null;
    let rewardActionTimer = 0;
    let rewardActionStartedAt = 0;
    let rewardActionToken = 0;
    let rewardActionActive = false;
    let rewardActionRestore = [];
    let rewardRefreshRequest = 0;
    let contactQrObjectUrl = "";
    let contactQrLoading = false;
    let contactQrRequest = 0;
    let membershipRequestActive = false;

    function setStatus(text, kind) {
      status.className = kind ? `status-line ${kind}` : "status-line";
      status.textContent = localizedContactText(text);
    }

    function setRewardStatus(text, kind) {
      if (!rewardStatus) return;
      rewardStatus.className = kind ? `status-line ${kind}` : "status-line";
      rewardStatus.textContent = text || "";
    }

    function setMembershipRequestStatus(text, kind) {
      if (!membershipRequestStatus) return;
      membershipRequestStatus.className = kind ? `status-line ${kind}` : "status-line";
      membershipRequestStatus.textContent = localizedContactText(text);
    }

    function setContactQrStatus(text, kind) {
      if (!contactQrStatus) return;
      contactQrStatus.className = kind ? `status-line ${kind}` : "status-line";
      contactQrStatus.textContent = localizedContactText(text);
    }

    function clearContactQrImage() {
      if (contactQrObjectUrl) URL.revokeObjectURL(contactQrObjectUrl);
      contactQrObjectUrl = "";
      if (contactQrImage && typeof contactQrImage.removeAttribute === "function") contactQrImage.removeAttribute("src");
      else if (contactQrImage) contactQrImage.src = "";
      if (contactQrPanel) contactQrPanel.hidden = true;
    }

    function revokeContactQr() {
      contactQrRequest += 1;
      contactQrLoading = false;
      clearContactQrImage();
      if (contactQrToggle) {
        contactQrToggle.disabled = false;
        contactQrToggle.hidden = true;
        contactQrToggle.textContent = "重新加载二维码";
        contactQrToggle.setAttribute("aria-expanded", "false");
      }
      setContactQrStatus("");
    }

    async function loadVerifiedContactQr() {
      if (!memberContact || !contactQrToggle || !contactQrPanel || !contactQrImage || contactQrLoading) return;
      const session = loadAuthSession();
      if (!session || !isNewsfeedSession(session)) return;
      const request = ++contactQrRequest;
      contactQrLoading = true;
      clearContactQrImage();
      memberContact.hidden = false;
      contactQrToggle.hidden = true;
      contactQrToggle.disabled = true;
      contactQrToggle.textContent = "重新加载二维码";
      setContactQrStatus("正在加载 KC桌面会员联系二维码…");
      try {
        const response = await fetch(`${workerUrl}/membership/contact-card`, {
          cache: "no-store",
          headers: authHeaders(),
        });
        if (request !== contactQrRequest || !modal.isConnected) return;
        if (!response.ok) {
          if (response.status === 401 || response.status === 403) {
            clearAuthSession();
            refreshUi({ statusOverride: "登录状态已失效，请重新登录。", skipContactVerification: true });
            return;
          }
          const data = await response.json().catch(() => ({}));
          throw new Error(data.detail || "当前登录状态无法查看联系二维码。");
        }
        const contentType = String(response.headers.get("Content-Type") || "").toLowerCase();
        if (!contentType.startsWith("image/")) throw new Error("联系二维码返回格式无效。");
        const blob = await response.blob();
        if (!blob || !blob.size) throw new Error("联系二维码暂时不可用。");
        const objectUrl = URL.createObjectURL(blob);
        if (request !== contactQrRequest || !modal.isConnected || !loadAuthSession()) {
          URL.revokeObjectURL(objectUrl);
          return;
        }
        contactQrObjectUrl = objectUrl;
        contactQrImage.src = objectUrl;
        contactQrPanel.hidden = false;
        contactQrToggle.setAttribute("aria-expanded", "true");
        setContactQrStatus("二维码仅在当前登录会话中显示。", "ok");
      } catch (error) {
        if (request !== contactQrRequest || !modal.isConnected) return;
        clearContactQrImage();
        contactQrToggle.hidden = false;
        setContactQrStatus(error.message || "联系二维码暂时不可用，请稍后重试。", "error");
      } finally {
        if (request === contactQrRequest) {
          contactQrLoading = false;
          contactQrToggle.disabled = false;
        }
      }
    }

    async function refreshVerifiedContactQr() {
      const localSession = loadAuthSession();
      if (!localSession) {
        if (memberContact) memberContact.hidden = true;
        revokeContactQr();
        return;
      }
      const request = ++contactQrRequest;
      contactQrLoading = false;
      clearContactQrImage();
      if (memberContact) memberContact.hidden = true;
      if (contactQrToggle) contactQrToggle.hidden = true;
      setContactQrStatus("");
      const verifiedSession = await refreshAuthSession(workerUrl);
      if (request !== contactQrRequest || !modal.isConnected) return;
      if (!verifiedSession || !isNewsfeedSession(verifiedSession)) {
        clearAuthSession();
        refreshUi({ statusOverride: "登录状态已失效，请重新登录。", skipContactVerification: true });
        return;
      }
      if (memberContact) memberContact.hidden = false;
      loadVerifiedContactQr();
    }

    function disposeAccountModal() {
      window.clearInterval(rewardActionTimer);
      rewardActionTimer = 0;
      revokeContactQr();
    }

    modal.__portalCleanup = disposeAccountModal;

    function formatRewardExpiry(value) {
      const timestamp = Date.parse(String(value || ""));
      if (!Number.isFinite(timestamp)) return "";
      const hours = Math.max(1, Math.ceil((timestamp - Date.now()) / 3_600_000));
      return hours < 24 ? `${hours} 小时后到期` : `${Math.ceil(hours / 24)} 天后到期`;
    }

    function beginRewardAction(button, label) {
      if (rewardActionActive) return 0;
      rewardActionActive = true;
      const token = ++rewardActionToken;
      rewardRefreshRequest += 1;
      window.clearInterval(rewardActionTimer);
      rewardActionStartedAt = Date.now();
      rewardActionRestore = [rewardCheckin, rewardDailyClaim, rewardPointsClaim]
        .filter(Boolean)
        .map((control) => ({
          control,
          disabled: control.disabled,
          text: control.textContent,
          loading: control.classList.contains("is-loading"),
        }));
      rewardActionRestore.forEach(({ control }) => {
        if (control) control.disabled = true;
      });
      if (button) {
        button.classList.add("is-loading");
        button.textContent = label;
      }
      rewardStatus.className = "status-line";
      rewardStatus.innerHTML = `<div class="async-action" role="status">
        <div class="async-action-meta"><strong>${escapeHtml(label)}</strong><span data-reward-elapsed aria-hidden="true">已用时 0.0 秒</span></div>
        <div class="async-action-track" aria-hidden="true"><span data-reward-progress style="width:16%"></span></div>
        <span>账号状态正在安全更新，页面可以继续浏览。</span>
      </div>`;
      const elapsedNode = rewardStatus.querySelector("[data-reward-elapsed]");
      const progressNode = rewardStatus.querySelector("[data-reward-progress]");
      const update = () => {
        if (!rewardActionActive || token !== rewardActionToken) return;
        const seconds = Math.max(0, (Date.now() - rewardActionStartedAt) / 1000);
        const width = Math.min(92, 16 + Math.floor((seconds / 18) * 76));
        if (elapsedNode) elapsedNode.textContent = `已用时 ${seconds.toFixed(1)} 秒`;
        if (progressNode) progressNode.style.width = `${width}%`;
      };
      update();
      rewardActionTimer = window.setInterval(update, 1_000);
      return token;
    }

    function restoreRewardControls() {
      rewardActionRestore.forEach(({ control, disabled, text, loading }) => {
        control.disabled = disabled;
        control.textContent = text;
        control.classList.toggle("is-loading", loading);
      });
    }

    function finishRewardAction(token) {
      if (!rewardActionActive || token !== rewardActionToken) return;
      window.clearInterval(rewardActionTimer);
      rewardActionTimer = 0;
      rewardActionActive = false;
      restoreRewardControls();
      if (currentRewardState) renderRewards(currentRewardState, { forceControls: true });
      rewardActionRestore = [];
    }

    function renderRewards(data, options = {}) {
      currentRewardState = data || {};
      if (rewardPoints) rewardPoints.textContent = String(Math.max(0, Number(data && data.points || 0)));
      if (rewardStreak) rewardStreak.textContent = String(Math.max(0, Number(data && data.current_streak || 0)));
      if (rewardCredits) rewardCredits.textContent = String(Math.max(0, Number(data && data.credits_available || 0)));
      if (!rewardActionActive || options.forceControls) {
        if (rewardCheckin) {
          rewardCheckin.disabled = Boolean(data && data.checked_in_today);
          rewardCheckin.textContent = data && data.checked_in_today ? "今日已签到" : "今日签到 +10";
        }
        if (rewardDailyClaim) {
          rewardDailyClaim.disabled = !data || !data.daily_available;
          rewardDailyClaim.textContent = data && data.daily_claimed ? "今日报告券已使用" : "使用报告券";
        }
        if (rewardPointsClaim) {
          const cost = Math.max(1, Number(data && data.points_report_cost || 70));
          rewardPointsClaim.disabled = !data || data.points_claimed_today || Number(data.points || 0) < cost;
          rewardPointsClaim.textContent = data && data.points_claimed_today ? "今日积分报告已领取" : `使用 ${cost} 积分`;
        }
      }
      if (rewardHint) {
        const milestone = data && data.next_milestone || {};
        const creditExpiry = formatRewardExpiry(data && data.next_credit_expiry);
        const creditCopy = Number(data && data.credits_available || 0) > 0
          ? `现有 ${Number(data.credits_available)} 张报告券${creditExpiry ? `，最近一张${creditExpiry}` : ""}。`
          : "";
        let milestoneCopy = "";
        if (milestone.type === "welcome_credit") milestoneCopy = "首次签到立即得 1 张 72 小时报告券。";
        else if (milestone.type === "d3_credit") milestoneCopy = `再连续 ${Number(milestone.days || 1)} 天，到第 3 天再得 1 张报告券。`;
        else if (milestone.type === "d7_freeze") milestoneCopy = `再连续 ${Number(milestone.days || 1)} 天完成 7 日里程碑。`;
        else if (milestone.type === "bonus_points") milestoneCopy = `再连续 ${Number(milestone.days || 1)} 天可得额外 ${Number(milestone.bonus_points || 0)} 分。`;
        rewardHint.textContent = `${creditCopy}${milestoneCopy} 每日 +10 分；70 分可兑换 1 份报告。`.trim();
      }
    }

    async function refreshRewards() {
      if (!rewards || !loadAuthSession()) return null;
      if (rewardActionActive) return currentRewardState;
      const request = ++rewardRefreshRequest;
      setRewardStatus("正在读取签到状态…");
      try {
        const response = await fetchRewardRequest(
          `${workerUrl}/rewards`,
          { cache: "no-store", headers: authHeaders() },
          "签到状态读取超时，请重试。"
        );
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "签到状态读取失败。");
        if (request !== rewardRefreshRequest || rewardActionActive) return currentRewardState;
        renderRewards(data);
        setRewardStatus(data.daily_available ? `有 ${Number(data.credits_available || 1)} 张报告券可用于当前目录报告。` : "");
        return data;
      } catch (error) {
        if (request !== rewardRefreshRequest || rewardActionActive) return currentRewardState;
        setRewardStatus(error.message || "签到状态读取失败。", "error");
        return null;
      }
    }

    async function claimReward(kind) {
      const item = context && context.item;
      if (!item || !item.id) return;
      const button = kind === "daily" ? rewardDailyClaim : rewardPointsClaim;
      const actionToken = beginRewardAction(button, kind === "daily" ? "正在使用报告券…" : "正在兑换报告…");
      if (!actionToken) return;
      try {
        const response = await fetchRewardRequest(
          `${workerUrl}/rewards/claim`,
          {
            method: "POST",
            headers: { "Content-Type": "application/json", ...authHeaders() },
            body: JSON.stringify({ reward_kind: kind, report_id: item.id }),
          },
          "报告领取请求超时，请重试。"
        );
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "报告领取失败。");
        if (data.rewards) renderRewards(data.rewards);
        if (data.already_claimed_today) {
          trackEvent(workerUrl, "reward_claim", {
            ...analyticsReportPayload(item, "catalog"),
            action: kind,
            status: "already_claimed_today",
          });
          setRewardStatus("今天的同类报告已经领取过，明天可以再领一份。", "error");
          return;
        }
        if (data.already_owned) {
          trackEvent(workerUrl, "reward_claim", {
            ...analyticsReportPayload(item, "catalog"),
            action: kind,
            status: "already_owned",
          });
          setRewardStatus("当前账号已经拥有这份报告。", "ok");
          return;
        }
        if (!data.claimed) throw new Error("报告未领取，请刷新签到状态后重试。");
        trackEvent(workerUrl, "reward_claim", {
          ...analyticsReportPayload(item, "catalog"),
          action: kind,
          status: "success",
        });
        setRewardStatus("领取成功，现在可直接账号下载。", "ok");
        document.dispatchEvent(new CustomEvent("portal-reward-change", { detail: { report_id: item.id, reward_kind: kind } }));
      } catch (error) {
        setRewardStatus(error.message || "报告领取失败。", "error");
        if (currentRewardState) renderRewards(currentRewardState);
      } finally {
        finishRewardAction(actionToken);
      }
    }

    function refreshUi(options = {}) {
      const statusOverride = String(options.statusOverride || "");
      const session = loadAuthSession();
      const signedIn = Boolean(session);
      form.hidden = signedIn;
      summary.hidden = !signedIn;
      if (rewards) rewards.hidden = !signedIn;
      if (contactCard) contactCard.hidden = false;
      if (memberContact) memberContact.hidden = true;
      if (membershipRequesterEmail) {
        if (signedIn) {
          membershipRequesterEmail.value = String(session.user.email || "").trim();
          membershipRequesterEmail.readOnly = true;
        } else {
          if (membershipRequesterEmail.readOnly) membershipRequesterEmail.value = "";
          membershipRequesterEmail.readOnly = false;
        }
      }
      if (signedIn) {
        document.getElementById("accountName").textContent = authUserLabel(session);
        document.getElementById("accountEmailText").textContent = session.user.email || "";
        if (adminOpen) {
          adminOpen.hidden = !canOpenOperationsPanel(session);
          adminOpen.textContent = isOperatorSession(session) && !isSuperSession(session)
            ? "运营后台"
            : "管理后台";
        }
        setStatus(statusOverride || (
          isSuperSession(session)
            ? "已登录，当前账号拥有管理员权限。"
            : (isOperatorSession(session) ? "已登录，当前账号拥有运营权限。" : "已登录。可在下方提交会员申请或查看会员联系方式。")
        ), "ok");
        fetch(`${workerUrl}/entitlement`, { cache: "no-store", headers: authHeaders() })
          .then((response) => response.json())
          .then((data) => {
            const summary = accountRightSummary(data);
            if (summary && !statusOverride) setStatus(`账号${summary}。`, "ok");
          })
          .catch(() => {});
        refreshRewards();
        if (!options.skipContactVerification) refreshVerifiedContactQr();
      } else {
        revokeContactQr();
        if (adminOpen) adminOpen.hidden = true;
        if (statusOverride) setStatus(statusOverride, "error");
        captchaToken = "";
        loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; });
      }
    }

    function setMode(nextMode) {
      mode = nextMode;
      emailLabel.hidden = mode !== "register";
      email.required = mode === "register";
      if (registrationNotice) registrationNotice.textContent = registrationNoticeText(mode);
      password.autocomplete = mode === "register" ? "new-password" : "current-password";
      submit.textContent = mode === "register" ? "注册并登录" : "登录";
      toggle.textContent = mode === "register" ? "已有账号，去登录" : "注册新账号";
      answer.value = "";
      loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; });
    }

    function finish() {
      disposeAccountModal();
      modal.__portalCleanup = null;
      modal.remove();
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    toggle.addEventListener("click", () => setMode(mode === "login" ? "register" : "login"));
    refresh.addEventListener("click", () => loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; }));
    if (contactQrToggle) contactQrToggle.addEventListener("click", refreshVerifiedContactQr);
    if (membershipRequestToggle && membershipRequestForm) {
      membershipRequestToggle.setAttribute("aria-expanded", String(!membershipRequestForm.hidden));
      membershipRequestToggle.addEventListener("click", () => {
        membershipRequestForm.hidden = !membershipRequestForm.hidden;
        membershipRequestToggle.setAttribute("aria-expanded", String(!membershipRequestForm.hidden));
        membershipRequestToggle.textContent = membershipRequestForm.hidden
          ? membershipRequestCopy(membershipRequestKindInput && membershipRequestKindInput.value).title
          : "收起申请表";
        if (!membershipRequestForm.hidden) {
          const target = membershipRequesterEmail && !membershipRequesterEmail.value
            ? membershipRequesterEmail
            : membershipContactChannel;
          if (target && typeof target.focus === "function") target.focus();
        }
      });
    }
    if (membershipRequestForm) {
      membershipRequestForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        if (membershipRequestActive) return;
        const requesterEmail = String(membershipRequesterEmail && membershipRequesterEmail.value || "").trim().slice(0, 254);
        const contactChannel = String(membershipContactChannel && membershipContactChannel.value || "").trim().toLowerCase();
        const contactValue = String(membershipContactValue && membershipContactValue.value || "").trim().slice(0, 160);
        const note = String(membershipRequestMessage && membershipRequestMessage.value || "").trim().slice(0, 600);
        const requestKind = membershipRequestKind(membershipRequestKindInput && membershipRequestKindInput.value);
        if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/u.test(requesterEmail)) {
          setMembershipRequestStatus("请填写有效的常用邮箱。", "error");
          membershipRequesterEmail?.focus();
          return;
        }
        if (!["wechat", "whatsapp", "telegram"].includes(contactChannel) || !contactValue) {
          setMembershipRequestStatus("请选择微信、WhatsApp 或 Telegram，并填写对应账号或手机号。", "error");
          (contactChannel ? membershipContactValue : membershipContactChannel)?.focus();
          return;
        }

        membershipRequestActive = true;
        membershipRequestSubmit.disabled = true;
        membershipRequestSubmit.textContent = "正在提交…";
        setMembershipRequestStatus("正在通知 KC桌面，请稍候…");
        try {
          const response = await fetch(`${workerUrl}/membership/request`, {
            method: "POST",
            cache: "no-store",
            headers: { "Content-Type": "application/json", ...authHeaders() },
            body: JSON.stringify({
              requester_email: requesterEmail,
              contact_channel: contactChannel,
              contact_value: contactValue,
              note,
              request_kind: requestKind,
              page_path: currentAnalyticsPath(),
              honeypot: String(membershipRequestWebsite && membershipRequestWebsite.value || "").slice(0, 160),
            }),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok || !data.ok) throw new Error(data.detail || "申请提交失败，请稍后重试。");
          membershipRequesterEmail.readOnly = true;
          membershipContactChannel.disabled = true;
          membershipContactValue.readOnly = true;
          membershipRequestMessage.readOnly = true;
          membershipRequestSubmit.textContent = data.deduplicated ? "申请已记录" : "申请已提交";
          setMembershipRequestStatus(
            data.detail || (data.deduplicated ? "这条申请已经收到，无需重复提交。" : "申请已提交，KC桌面会通过你留下的联系方式回复。"),
            "ok",
          );
          trackEvent(workerUrl, "membership_request", {
            action: data.deduplicated ? "deduplicated" : "submitted",
            request_kind: requestKind,
            contact_channel: contactChannel,
          });
        } catch (error) {
          membershipRequestSubmit.disabled = false;
          membershipRequestSubmit.textContent = membershipRequestCopy(requestKind).button;
          setMembershipRequestStatus(error.message || "申请提交失败，请稍后重试。", "error");
        } finally {
          membershipRequestActive = false;
        }
      });
    }
    if (logout) {
      logout.addEventListener("click", () => {
        const session = loadAuthSession();
        trackEvent(workerUrl, "account_auth", {
          target: authUserLabel(session),
          action: "logout",
          status: "success",
        });
        clearAuthSession();
        setStatus("已退出登录。");
        refreshUi();
      });
    }
    if (rewardCheckin) {
      rewardCheckin.addEventListener("click", async () => {
        const creditsBefore = Number(currentRewardState && currentRewardState.credits_available || 0);
        const actionToken = beginRewardAction(rewardCheckin, "正在签到…");
        if (!actionToken) return;
        try {
          const response = await fetchRewardRequest(
            `${workerUrl}/rewards`,
            {
              method: "POST",
              headers: { "Content-Type": "application/json", ...authHeaders() },
              body: "{}",
            },
            "签到请求超时，请重试。"
          );
          const data = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(data.detail || "签到失败。");
          renderRewards(data);
          trackEvent(workerUrl, "reward_checkin", { action: "daily", status: "success", current_streak: data.current_streak });
          const issuedCredit = Number(data.credits_available || 0) > creditsBefore;
          setRewardStatus(issuedCredit ? "签到成功，已解锁一张 72 小时报告券。" : "签到成功，积分和连续天数已更新。", "ok");
          rewards.classList.remove("reward-success-pop");
          void rewards.offsetWidth;
          rewards.classList.add("reward-success-pop");
        } catch (error) {
          setRewardStatus(error.message || "签到失败。", "error");
          if (currentRewardState) renderRewards(currentRewardState);
        } finally {
          finishRewardAction(actionToken);
        }
      });
    }
    if (rewardDailyClaim) rewardDailyClaim.addEventListener("click", () => claimReward("daily"));
    if (rewardPointsClaim) rewardPointsClaim.addEventListener("click", () => claimReward("points"));
    if (adminOpen) {
      adminOpen.addEventListener("click", () => showAccountAdminModal(workerUrl));
    }
    if (passwordForm) {
      passwordForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        if (!loadAuthSession()) {
          setStatus("请先登录。", "error");
          return;
        }
        if (newPassword.value !== newPasswordConfirm.value) {
          setStatus("两次输入的新密码不一致。", "error");
          return;
        }
        passwordSubmit.disabled = true;
        setStatus("正在修改密码…");
        try {
          const response = await fetch(`${workerUrl}/account/password`, {
            method: "POST",
            headers: { "Content-Type": "application/json", ...authHeaders() },
            body: JSON.stringify({
              current_password: currentPassword.value,
              new_password: newPassword.value,
            }),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "密码修改失败。");
          saveAuthSession({ token: data.token, user: data.user });
          trackEvent(workerUrl, "account_auth", {
            target: data.user.username || data.user.email || "",
            action: "password_change",
            status: "success",
          });
          currentPassword.value = "";
          newPassword.value = "";
          newPasswordConfirm.value = "";
          refreshUi();
          setStatus("密码已更新。", "ok");
        } catch (error) {
          trackEvent(workerUrl, "account_auth", {
            target: authUserLabel(loadAuthSession()),
            action: "password_change",
            status: "error",
            error: error && error.message || "password_change_failed",
          });
          setStatus(error.message || "密码修改失败。", "error");
        } finally {
          passwordSubmit.disabled = false;
        }
      });
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      submit.disabled = true;
      setStatus(mode === "register" ? "正在注册…" : "正在登录…");
      try {
        if (mode === "register" && (!email.value.trim() || !email.validity.valid)) {
          throw new Error("注册必须填写有效的常用邮箱。");
        }
        const response = await fetch(`${workerUrl}/auth`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            action: mode,
            username: username.value,
            password: password.value,
            email: mode === "register" ? email.value : "",
            captcha_token: captchaToken,
            captcha_answer: answer.value,
          }),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "账号请求失败。");
        saveAuthSession({ token: data.token, user: data.user });
        trackEvent(workerUrl, "account_auth", {
          target: data.user.username || data.user.email || username.value,
          action: data.recovered ? "login_recovered" : mode,
          status: "success",
        });
        password.value = "";
        answer.value = "";
        const registrationStatus = mode === "register" ? registrationCompleteText() : "";
        refreshUi({ statusOverride: registrationStatus });
      } catch (error) {
        trackEvent(workerUrl, "account_auth", {
          target: username.value,
          action: mode,
          status: "error",
          error: error && error.message || "account_request_failed",
        });
        setStatus(error.message || "账号请求失败。", "error");
        answer.value = "";
        captchaToken = await loadAccountCaptcha(workerUrl, status);
      } finally {
        submit.disabled = false;
      }
    });

    refreshUi();
    if (!loadAuthSession() && username) username.focus();
  }

  function newAdminPdfUploadId() {
    if (typeof crypto !== "undefined" && typeof crypto.randomUUID === "function") {
      return crypto.randomUUID();
    }
    return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, (token) => {
      const value = Math.floor(Math.random() * 16);
      return (token === "x" ? value : (value & 0x3) | 0x8).toString(16);
    });
  }

  function isAdminPdfUploadId(value) {
    const uploadId = String(value || "").trim();
    return /^[0-9a-f]{8}-[0-9a-f]{4}-[1-8][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$/i.test(uploadId)
      || /^upload-(?:[0-9a-f]{32}|[0-9a-f]{64})$/.test(uploadId);
  }

  function normalizeAdminPdfUploadSession(value) {
    if (!value || typeof value !== "object" || Array.isArray(value)) return null;
    if (Number(value.version) !== ADMIN_PDF_UPLOAD_SESSION_VERSION) return null;
    const uploadId = String(value.upload_id || "").trim();
    const mode = String(value.mode || "").trim();
    const state = String(value.state || "").trim();
    const startedAt = Number(value.started_at || 0);
    const fileSize = Math.max(0, Math.floor(Number(value.file_size || 0) || 0));
    const source = String(value.source || "").trim();
    const targetId = String(value.target_id || "").trim();
    if (!isAdminPdfUploadId(uploadId)) return null;
    if (!["hot-report", "text-only", "request"].includes(mode)) return null;
    if (!["uploading", "processing", "unknown"].includes(state)) return null;
    if (!Number.isFinite(startedAt) || startedAt <= 0) return null;
    if (source && !["catalog", "authority", "report-a"].includes(source)) return null;
    if (targetId.length > 240) return null;
    return {
      version: ADMIN_PDF_UPLOAD_SESSION_VERSION,
      upload_id: uploadId,
      mode,
      state,
      started_at: startedAt,
      file_size: fileSize,
      source,
      target_id: targetId,
    };
  }

  function readAdminPdfUploadSession() {
    try {
      return normalizeAdminPdfUploadSession(JSON.parse(sessionStorage.getItem(ADMIN_PDF_UPLOAD_SESSION_KEY) || "null"));
    } catch (_error) {
      return null;
    }
  }

  function writeAdminPdfUploadSession(value) {
    const normalized = normalizeAdminPdfUploadSession({
      version: ADMIN_PDF_UPLOAD_SESSION_VERSION,
      ...(value || {}),
    });
    try {
      if (normalized) sessionStorage.setItem(ADMIN_PDF_UPLOAD_SESSION_KEY, JSON.stringify(normalized));
      else sessionStorage.removeItem(ADMIN_PDF_UPLOAD_SESSION_KEY);
    } catch (_error) {
      // Upload still works when session storage is unavailable.
    }
    return normalized;
  }

  function clearAdminPdfUploadSession(uploadId = "") {
    const current = readAdminPdfUploadSession();
    if (uploadId && current && current.upload_id !== uploadId) return false;
    try {
      sessionStorage.removeItem(ADMIN_PDF_UPLOAD_SESSION_KEY);
    } catch (_error) {
      // Nothing else to clear.
    }
    return true;
  }

  function adminPdfUploadElapsedText(startedAt, now = Date.now()) {
    const elapsedSeconds = Math.max(0, Math.floor((Number(now) - Number(startedAt || now)) / 1000));
    if (elapsedSeconds < 60) return `${elapsedSeconds} 秒`;
    const minutes = Math.floor(elapsedSeconds / 60);
    const seconds = elapsedSeconds % 60;
    return `${minutes} 分 ${seconds} 秒`;
  }

  function adminPdfUploadProgressText(loaded, total, startedAt, now = Date.now()) {
    const safeLoaded = Math.max(0, Number(loaded || 0) || 0);
    const safeTotal = Math.max(0, Number(total || 0) || 0);
    const percent = safeTotal > 0 ? Math.min(100, Math.round(safeLoaded / safeTotal * 100)) : 0;
    const amount = safeTotal > 0
      ? `${formatSize(safeLoaded)} / ${formatSize(safeTotal)}`
      : `已上传 ${formatSize(safeLoaded)}`;
    return {
      percent,
      text: `正在上传 ${percent}% · ${amount} · 已用 ${adminPdfUploadElapsedText(startedAt, now)}`,
    };
  }

  function xhrAdminPdfUpload(url, formData, options = {}) {
    let request = null;
    const promise = new Promise((resolve, reject) => {
      request = new XMLHttpRequest();
      let uploadFinished = false;
      const fail = (message, name = "AdminPdfUploadError", upload = null) => {
        const error = new Error(message || "PDF 上传失败，请检查结果后重试。");
        error.name = name;
        error.status = Number(request && request.status || 0) || 0;
        error.uploadFinished = uploadFinished;
        if (upload && typeof upload === "object") error.upload = upload;
        reject(error);
      };
      request.open("POST", url, true);
      request.timeout = Math.max(1000, Number(options.timeoutMs || ADMIN_PDF_UPLOAD_XHR_TIMEOUT_MS) || ADMIN_PDF_UPLOAD_XHR_TIMEOUT_MS);
      const headers = options.headers && typeof options.headers === "object" ? options.headers : {};
      Object.entries(headers).forEach(([name, value]) => {
        if (value !== undefined && value !== null && String(value)) request.setRequestHeader(name, String(value));
      });
      request.upload.addEventListener("progress", (event) => {
        if (typeof options.onProgress === "function") {
          options.onProgress(event.loaded || 0, event.lengthComputable ? event.total : 0);
        }
      });
      request.upload.addEventListener("load", () => {
        uploadFinished = true;
        if (typeof options.onTransportComplete === "function") options.onTransportComplete();
      });
      request.addEventListener("load", () => {
        let data = {};
        try {
          data = request.response && typeof request.response === "object"
            ? request.response
            : JSON.parse(request.responseText || "{}");
        } catch (_error) {
          data = {};
        }
        if (request.status >= 200 && request.status < 300 && data && data.ok !== false) {
          resolve(data);
          return;
        }
        const failedUpload = data && data.upload && data.upload.status === "failed" ? data.upload : null;
        fail(
          data.detail || failedUpload && failedUpload.detail || `PDF 上传失败 (${request.status || "网络异常"})。`,
          failedUpload ? "AdminPdfUploadFailedError" : "AdminPdfUploadError",
          failedUpload,
        );
      });
      request.addEventListener("error", () => fail("连接中断，上传结果尚未确认。请先检查结果，不要重复上传。"));
      request.addEventListener("timeout", () => fail("等待服务器确认超时。请先检查结果，不要重复上传。", "TimeoutError"));
      request.addEventListener("abort", () => fail(
        uploadFinished
          ? "已停止等待，但服务器可能仍在处理。请检查结果，不要重复上传。"
          : "上传已取消。服务器可能已收到部分数据，请先检查结果。",
        "AbortError",
      ));
      request.responseType = "json";
      if (typeof options.onRequest === "function") options.onRequest(request);
      request.send(formData);
    });
    return { promise, get request() { return request; } };
  }

  function adminPdfUploadProgressMarkup(prefix) {
    return `
      <div class="account-admin-upload-progress" id="${escapeHtml(prefix)}Progress" hidden>
        <div class="account-admin-upload-progress-track" aria-hidden="true"><span></span></div>
        <div class="account-admin-upload-progress-copy">
          <strong id="${escapeHtml(prefix)}ProgressText">等待上传…</strong>
          <span id="${escapeHtml(prefix)}Elapsed"></span>
        </div>
      </div>
      <div class="account-admin-upload-recovery-actions">
        <button class="secondary-button account-admin-upload-cancel" id="${escapeHtml(prefix)}Cancel" type="button" hidden>取消传输</button>
        <button class="secondary-button account-admin-upload-check" id="${escapeHtml(prefix)}Check" type="button" hidden>检查上传结果</button>
      </div>
    `;
  }

  function adminPdfUploadUi(prefix) {
    const progress = document.getElementById(`${prefix}Progress`);
    return {
      progress,
      bar: progress && progress.querySelector(".account-admin-upload-progress-track span"),
      text: document.getElementById(`${prefix}ProgressText`),
      elapsed: document.getElementById(`${prefix}Elapsed`),
      cancel: document.getElementById(`${prefix}Cancel`),
      check: document.getElementById(`${prefix}Check`),
    };
  }

  function renderAdminPdfUploadUi(prefix, state = {}) {
    const ui = adminPdfUploadUi(prefix);
    if (!ui.progress) return;
    const percent = Math.max(0, Math.min(100, Number(state.percent || 0) || 0));
    ui.progress.hidden = state.hidden === true;
    ui.progress.dataset.state = String(state.state || "uploading");
    if (ui.bar) ui.bar.style.width = `${percent}%`;
    if (ui.text) ui.text.textContent = String(state.text || "等待上传…");
    if (ui.elapsed) ui.elapsed.textContent = state.startedAt
      ? `已用 ${adminPdfUploadElapsedText(state.startedAt)}`
      : "";
    if (ui.cancel) ui.cancel.hidden = state.canCancel !== true;
    if (ui.check) ui.check.hidden = state.canCheck !== true;
  }

  function restoredAdminPdfUploadMessage(session) {
    const label = session.mode === "hot-report"
      ? "新报告"
      : session.mode === "text-only"
        ? "Catalog 补齐"
        : "申请报告补齐";
    return `检测到一笔尚未确认的${label}上传（${formatSize(session.file_size)}，已用 ${adminPdfUploadElapsedText(session.started_at)}）。请先检查结果，不要重复上传。`;
  }

  function adminPdfUploadIdForFile(fileInput) {
    if (!fileInput) return newAdminPdfUploadId();
    const current = String(fileInput.dataset && fileInput.dataset.uploadId || "");
    if (isAdminPdfUploadId(current)) return current;
    const uploadId = newAdminPdfUploadId();
    if (fileInput.dataset) fileInput.dataset.uploadId = uploadId;
    return uploadId;
  }

  function resetAdminPdfUploadId(fileInput) {
    if (fileInput && fileInput.dataset) fileInput.dataset.uploadId = newAdminPdfUploadId();
  }

  async function adminPdfUploadFingerprint(kind, source, targetId, file) {
    const material = [
      String(kind || ""),
      String(source || ""),
      String(targetId || ""),
      String(file && file.name || ""),
      String(file && file.size || 0),
      String(file && file.lastModified || 0),
    ].join("\n");
    if (typeof crypto !== "undefined" && crypto.subtle && typeof crypto.subtle.digest === "function") {
      const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(material));
      return Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("");
    }
    // Format-preserving fallback for older browsers. The server uses this value
    // only to prevent one upload_id from being reused for a different file.
    let hash = 2166136261;
    for (let index = 0; index < material.length; index += 1) {
      hash ^= material.charCodeAt(index);
      hash = Math.imul(hash, 16777619) >>> 0;
    }
    const block = hash.toString(16).padStart(8, "0");
    return block.repeat(8);
  }

  async function fetchAdminPdfUploadStatus(workerUrl, uploadId) {
    const controller = new AbortController();
    const timer = window.setTimeout(() => controller.abort(), ADMIN_PDF_UPLOAD_STATUS_TIMEOUT_MS);
    try {
      const response = await fetch(
        `${workerUrl}/account-admin/upload-status?upload_id=${encodeURIComponent(uploadId)}`,
        { cache: "no-store", headers: authHeaders(), signal: controller.signal },
      );
      const data = await response.json().catch(() => ({}));
      if (response.status === 404) return null;
      if (!response.ok || !data.ok || !data.upload) {
        const error = new Error(data.detail || "上传状态暂时无法读取，请稍后再检查。");
        error.status = response.status;
        throw error;
      }
      return data;
    } catch (error) {
      if (error && error.name === "AbortError") {
        const timeout = new Error("上传状态检查超时，请稍后再次检查。当前不要重复上传。");
        timeout.name = "TimeoutError";
        throw timeout;
      }
      throw error;
    } finally {
      window.clearTimeout(timer);
    }
  }

  function completedAdminPdfUploadPayload(data) {
    const upload = data && data.upload && typeof data.upload === "object" ? data.upload : null;
    if (!upload || upload.status !== "completed") return null;
    const result = upload.result && typeof upload.result === "object" ? upload.result : {};
    return { ok: true, ...result, upload };
  }

  async function pollAdminPdfUploadStatus(workerUrl, uploadId, options = {}) {
    const limit = Math.max(1, Number(options.limit || ADMIN_PDF_UPLOAD_POLL_LIMIT) || 1);
    for (let attempt = 0; attempt < limit; attempt += 1) {
      if (typeof options.isCurrent === "function" && !options.isCurrent()) {
        const cancelled = new Error("上传状态检查已停止。");
        cancelled.name = "AbortError";
        throw cancelled;
      }
      try {
        const data = await fetchAdminPdfUploadStatus(workerUrl, uploadId);
        const upload = data && data.upload;
        if (upload && typeof options.onUpdate === "function") options.onUpdate(upload);
        const completed = completedAdminPdfUploadPayload(data);
        if (completed) return completed;
        if (upload && upload.status === "failed") {
          const error = new Error(upload.detail || "PDF 入库失败。请检查原因后再操作。");
          error.name = "AdminPdfUploadFailedError";
          error.upload = upload;
          throw error;
        }
      } catch (error) {
        if (error && error.name === "AdminPdfUploadFailedError") throw error;
        if (error && (error.status === 401 || error.status === 403)) throw error;
        if (attempt === limit - 1) throw error;
      }
      await new Promise((resolve) => window.setTimeout(resolve, ADMIN_PDF_UPLOAD_POLL_MS));
    }
    const pending = new Error("服务器仍在处理。请稍后点击“检查上传结果”，不要重复上传。");
    pending.name = "AdminPdfUploadPendingError";
    throw pending;
  }

  function adminPdfUploadStageText(upload) {
    const stage = String(upload && (upload.stage || upload.status) || "processing");
    const labels = {
      validating: "服务器正在校验 PDF…",
      uploading: "服务器正在接收 PDF…",
      stored: "PDF 已保存，正在核验对象…",
      indexing: "PDF 已保存，正在发布检索与下载入口…",
      completed: "PDF 已入库并发布。",
      failed: "PDF 入库失败。",
    };
    return labels[stage] || "文件已传完，服务器正在校验、保存和发布…";
  }

  async function runAdminPdfUpload(options = {}) {
    const file = options.file;
    const uploadId = String(options.uploadId || "").trim();
    if (!file || !uploadId) throw new Error("请选择 PDF 文件。");
    const unresolved = readAdminPdfUploadSession();
    if (unresolved) {
      throw new Error("上一笔 PDF 上传结果尚未确认。请先点击“检查上传结果”解决上一笔，再开始新上传。");
    }
    if (activeAdminPdfUpload && activeAdminPdfUpload.uploadId !== uploadId) {
      throw new Error("已有 PDF 正在上传。请先等待或检查上一笔结果。");
    }
    const startedAt = Date.now();
    const fingerprint = await adminPdfUploadFingerprint(
      options.kind || options.mode,
      options.source || "",
      options.targetId || "",
      file,
    );
    const sessionBase = {
      version: ADMIN_PDF_UPLOAD_SESSION_VERSION,
      upload_id: uploadId,
      mode: options.mode,
      started_at: startedAt,
      file_size: file.size,
      source: options.source || "",
      target_id: options.targetId || "",
    };
    writeAdminPdfUploadSession({ ...sessionBase, state: "uploading" });
    renderAdminPdfUploadUi(options.prefix, {
      percent: 0,
      text: `准备上传 ${formatSize(file.size)}…`,
      startedAt,
      canCancel: true,
      canCheck: false,
      state: "uploading",
    });
    if (typeof options.setStatus === "function") {
      options.setStatus("正在上传 PDF；可查看实时进度。请勿刷新或重复提交。", "");
    }

    let current = true;
    let transportComplete = false;
    let resolveTransport = null;
    const transportGate = new Promise((resolve) => { resolveTransport = resolve; });
    const elapsedTimer = window.setInterval(() => {
      const session = readAdminPdfUploadSession();
      if (!current || !session || session.upload_id !== uploadId) return;
      const ui = adminPdfUploadUi(options.prefix);
      if (ui.elapsed) ui.elapsed.textContent = `已用 ${adminPdfUploadElapsedText(startedAt)}`;
    }, 1000);

    const formData = options.formData;
    formData.set("upload_id", uploadId);
    formData.set("upload_fingerprint", fingerprint);
    const transfer = xhrAdminPdfUpload(options.url, formData, {
      headers: {
        ...authHeaders(),
        "X-Upload-ID": uploadId,
        "X-Upload-Fingerprint": fingerprint,
      },
      onRequest(request) {
        activeAdminPdfUpload = {
          uploadId,
          mode: options.mode,
          request,
          cancel() { request.abort(); },
        };
      },
      onProgress(loaded, total) {
        const progress = adminPdfUploadProgressText(loaded, total || file.size, startedAt);
        renderAdminPdfUploadUi(options.prefix, {
          ...progress,
          startedAt,
          canCancel: true,
          canCheck: false,
          state: "uploading",
        });
      },
      onTransportComplete() {
        transportComplete = true;
        writeAdminPdfUploadSession({ ...sessionBase, state: "processing" });
        renderAdminPdfUploadUi(options.prefix, {
          percent: 100,
          text: "文件已传完，服务器正在校验、保存和发布…",
          startedAt,
          canCancel: false,
          canCheck: true,
          state: "processing",
        });
        if (typeof options.setStatus === "function") {
          options.setStatus("文件已传到服务器，正在校验、保存并发布。此时无需重新上传。", "");
        }
        resolveTransport();
      },
    });

    const statusPromise = transportGate.then(() => pollAdminPdfUploadStatus(workerUrlFromUploadUrl(options.url), uploadId, {
      isCurrent: () => current,
      onUpdate(upload) {
        writeAdminPdfUploadSession({ ...sessionBase, state: "processing" });
        renderAdminPdfUploadUi(options.prefix, {
          percent: 100,
          text: adminPdfUploadStageText(upload),
          startedAt,
          canCancel: false,
          canCheck: true,
          state: "processing",
        });
      },
    }));
    // Prevent a late losing branch in Promise.race from becoming an unhandled rejection.
    statusPromise.catch(() => null);

    try {
      const transferOutcome = transfer.promise.then((data) => {
        const completed = completedAdminPdfUploadPayload(data);
        if (completed) return { ...data, ...completed };
        if (data && data.pending) return statusPromise;
        return data;
      }, (error) => {
        if (error && error.uploadFinished) return statusPromise;
        throw error;
      });
      const result = await Promise.race([transferOutcome, statusPromise]);
      clearAdminPdfUploadSession(uploadId);
      renderAdminPdfUploadUi(options.prefix, {
        percent: 100,
        text: "PDF 已入库并发布。",
        startedAt,
        canCancel: false,
        canCheck: false,
        state: "completed",
      });
      return result;
    } catch (error) {
      const failed = error && error.name === "AdminPdfUploadFailedError";
      if (failed) {
        clearAdminPdfUploadSession(uploadId);
        resetAdminPdfUploadId(options.fileInput);
        error.message = `${error.message || "PDF 入库失败。"} 已生成新的上传编号，修正后可重试。`;
      }
      else writeAdminPdfUploadSession({ ...sessionBase, state: "unknown" });
      renderAdminPdfUploadUi(options.prefix, {
        percent: transportComplete ? 100 : 0,
        text: failed
          ? (error.message || "PDF 入库失败，已生成新的上传编号，修正后可重试。")
          : "结果尚未确认。请先检查结果，不要重复上传。",
        startedAt,
        canCancel: false,
        canCheck: !failed,
        state: failed ? "failed" : "unknown",
      });
      throw error;
    } finally {
      current = false;
      window.clearInterval(elapsedTimer);
      if (activeAdminPdfUpload && activeAdminPdfUpload.uploadId === uploadId) activeAdminPdfUpload = null;
    }
  }

  function workerUrlFromUploadUrl(value) {
    return String(value || "").replace(/\/account-admin\/(?:hot-report|text-only-pdf|contact-report-pdf)(?:\?.*)?$/, "");
  }

  async function checkAdminPdfUploadResult(workerUrl, session, options = {}) {
    const normalized = normalizeAdminPdfUploadSession(session);
    if (!normalized) throw new Error("没有可检查的上传记录。");
    if (typeof options.setStatus === "function") options.setStatus("正在检查服务器记录…", "");
    renderAdminPdfUploadUi(options.prefix, {
      percent: normalized.state === "uploading" ? 0 : 100,
      text: "正在检查服务器记录…",
      startedAt: normalized.started_at,
      canCancel: false,
      canCheck: false,
      state: "processing",
    });
    const data = await fetchAdminPdfUploadStatus(workerUrl, normalized.upload_id);
    if (!data || !data.upload) {
      writeAdminPdfUploadSession({ ...normalized, state: "unknown" });
      const message = "服务器暂未找到这笔上传。可能仍在接收，请稍后再次检查；现在不要重复上传。";
      renderAdminPdfUploadUi(options.prefix, {
        percent: 0,
        text: message,
        startedAt: normalized.started_at,
        canCancel: false,
        canCheck: true,
        state: "unknown",
      });
      if (typeof options.setStatus === "function") options.setStatus(message, "error");
      return null;
    }
    const completed = completedAdminPdfUploadPayload(data);
    if (completed) {
      clearAdminPdfUploadSession(normalized.upload_id);
      renderAdminPdfUploadUi(options.prefix, {
        percent: 100,
        text: "PDF 已入库并发布。",
        startedAt: normalized.started_at,
        canCancel: false,
        canCheck: false,
        state: "completed",
      });
      if (typeof options.setStatus === "function") options.setStatus("PDF 已入库并发布。", "ok");
      if (typeof options.onComplete === "function") await options.onComplete(completed);
      return completed;
    }
    if (data.upload.status === "failed") {
      clearAdminPdfUploadSession(normalized.upload_id);
      resetAdminPdfUploadId(options.fileInput);
      const message = `${data.upload.detail || "PDF 入库失败。请核对原因后再操作。"} 已生成新的上传编号，修正后可重试。`;
      renderAdminPdfUploadUi(options.prefix, {
        percent: 100,
        text: message,
        startedAt: normalized.started_at,
        canCancel: false,
        canCheck: false,
        state: "failed",
      });
      if (typeof options.setStatus === "function") options.setStatus(message, "error");
      return data;
    }
    writeAdminPdfUploadSession({ ...normalized, state: "processing" });
    const message = `${adminPdfUploadStageText(data.upload)} 已用 ${adminPdfUploadElapsedText(normalized.started_at)}，请勿重复上传。`;
    renderAdminPdfUploadUi(options.prefix, {
      percent: 100,
      text: message,
      startedAt: normalized.started_at,
      canCancel: false,
      canCheck: true,
      state: "processing",
    });
    if (typeof options.setStatus === "function") options.setStatus(message, "");
    return data;
  }

  function adminReportChatCollectionCount(value) {
    if (Array.isArray(value)) return value.length;
    if (value && typeof value === "object") return Object.keys(value).length;
    const count = Math.trunc(Number(value || 0));
    return Number.isFinite(count) && count > 0 ? Math.min(count, 100000) : 0;
  }

  function adminReportChatPreviewText(value, maxLength = 1600) {
    const limit = Math.max(1, Math.min(4000, Math.trunc(Number(maxLength) || 1600)));
    return String(value || "").replace(/\s+/gu, " ").trim().slice(0, limit);
  }

  function normalizeAdminReportChatArchive(raw) {
    if (!raw || typeof raw !== "object" || Array.isArray(raw)) return null;
    const archiveId = String(raw.archive_id || raw.id || "").trim().slice(0, 240);
    const question = String(raw.question || raw.query || raw.prompt || "").replace(/\s+/gu, " ").trim().slice(0, 600);
    if (!archiveId || !question) return null;
    const identity = raw.identity && typeof raw.identity === "object" ? raw.identity : {};
    const user = raw.user && typeof raw.user === "object" ? raw.user : {};
    const actor = raw.actor && typeof raw.actor === "object" ? raw.actor : {};
    const policy = raw.policy && typeof raw.policy === "object" ? raw.policy : {};
    const answer = raw.response && typeof raw.response === "object" ? raw.response : {};
    const findings = (Array.isArray(answer.findings) ? answer.findings : []).map((item) => {
      if (!item || typeof item !== "object" || Array.isArray(item)) return null;
      const title = adminReportChatPreviewText(item.title, 180);
      const summary = adminReportChatPreviewText(item.summary || item.analysis, 1600);
      return title || summary ? { title, summary } : null;
    }).filter(Boolean).slice(0, 8);
    const dataPoints = (Array.isArray(answer.data_points) ? answer.data_points : []).map((item) => {
      if (!item || typeof item !== "object" || Array.isArray(item)) return null;
      const label = adminReportChatPreviewText(item.label || item.metric, 180);
      const value = adminReportChatPreviewText(item.value, 240);
      const context = adminReportChatPreviewText(item.context || item.period, 500);
      return label || value ? { label, value, context } : null;
    }).filter(Boolean).slice(0, 12);
    const publicId = String(raw.public_id || "").trim().slice(0, 240);
    const explicitPublished = raw.published;
    return {
      archiveId,
      question,
      createdAt: String(raw.created_at || raw.ts || raw.updated_at || "").trim().slice(0, 60),
      identityTier: String(
        raw.identity_tier || raw.tier || raw.member_tier || raw.user_tier
        || identity.tier || identity.level || policy.tier || user.tier || user.role || actor.role
        || (actor.kind === "device" || raw.authenticated === false ? "访客" : "已登录"),
      ).replace(/\s+/gu, " ").trim().slice(0, 80),
      status: String(raw.status || raw.answer_status || (raw.error ? "failed" : "completed"))
        .replace(/\s+/gu, " ").trim().slice(0, 80),
      sourceCount: adminReportChatCollectionCount(
        raw.source_count ?? raw.sources_count ?? raw.sources ?? answer.source_count ?? answer.sources,
      ),
      chartCount: adminReportChatCollectionCount(
        raw.chart_count ?? raw.charts_count ?? raw.charts ?? answer.chart_count ?? answer.charts,
      ),
      answerSummary: adminReportChatPreviewText(answer.executive_summary || answer.answer, 2400),
      findings,
      dataPoints,
      published: explicitPublished === true || explicitPublished === "true" || Boolean(publicId),
      publicId,
    };
  }

  function adminReportChatAnswerDetails(item) {
    const summary = item.answerSummary
      ? `<div><strong>回答摘要</strong><p>${escapeHtml(item.answerSummary)}</p></div>`
      : "";
    const findings = Array.isArray(item.findings) && item.findings.length
      ? `<div><strong>核心发现</strong><ul>${item.findings.map((finding) => `
          <li>
            ${finding.title ? `<strong>${escapeHtml(finding.title)}</strong>` : ""}
            ${finding.summary ? `<span>${escapeHtml(finding.summary)}</span>` : ""}
          </li>`).join("")}</ul></div>`
      : "";
    const dataPoints = Array.isArray(item.dataPoints) && item.dataPoints.length
      ? `<div><strong>数据点</strong><ul>${item.dataPoints.map((dataPoint) => `
          <li>
            ${dataPoint.label ? `<strong>${escapeHtml(dataPoint.label)}</strong>` : ""}
            ${dataPoint.value ? `<span>${escapeHtml(dataPoint.value)}</span>` : ""}
            ${dataPoint.context ? `<span>${escapeHtml(dataPoint.context)}</span>` : ""}
          </li>`).join("")}</ul></div>`
      : "";
    const content = summary || findings || dataPoints
      ? `${summary}${findings}${dataPoints}`
      : '<div class="empty-state">这条记录没有可展示的回答内容。</div>';
    return `<details class="account-admin-report-chat-details"><summary>查看回答内容</summary>${content}</details>`;
  }

  function adminReportChatArchiveRow(item) {
    const state = item.published ? "已公开" : "未公开";
    const action = item.published ? "unpublish" : "publish";
    const actionLabel = item.published ? "撤下公开展示" : "公开展示";
    const meta = [
      formatAdminDateTime(item.createdAt) || item.createdAt,
      item.identityTier,
      item.status,
      `来源 ${item.sourceCount}`,
      `图表 ${item.chartCount}`,
      state,
    ].filter(Boolean).join(" · ");
    return `
      <article class="account-admin-file" data-report-chat-archive="${escapeHtml(item.archiveId)}">
        <div>
          <strong>${escapeHtml(item.question)}</strong>
          <span>${escapeHtml(meta)}</span>
          ${adminReportChatAnswerDetails(item)}
        </div>
        <div class="account-admin-file-actions">
          <button class="secondary-button" type="button"
            data-report-chat-curation="${escapeHtml(action)}"
            data-archive-id="${escapeHtml(item.archiveId)}">${escapeHtml(actionLabel)}</button>
        </div>
      </article>`;
  }

  function renderAdminReportChatArchives(items) {
    return items.length
      ? items.map(adminReportChatArchiveRow).join("")
      : '<div class="empty-state">还没有 RAG 问答存档。</div>';
  }

  async function fetchAdminReportChatHistory(workerUrl) {
    const response = await fetch(`${workerUrl}/account-admin/report-chat-history?limit=50`, {
      cache: "no-store",
      headers: authHeaders(),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "RAG 问答档案读取失败。");
    const rows = Array.isArray(data.items)
      ? data.items
      : (Array.isArray(data.archives) ? data.archives : (Array.isArray(data.history) ? data.history : []));
    return {
      items: rows.map(normalizeAdminReportChatArchive).filter(Boolean).slice(0, 50),
      total: Math.max(0, Number(data.total || rows.length) || rows.length),
    };
  }

  async function loadAdminReportChatHistory(workerUrl, targets) {
    if (!targets || !targets.canManageUsers || !targets.reportChatArchiveSection
      || !targets.reportChatArchiveList || !targets.reportChatArchiveStatus) return [];
    targets.reportChatArchiveStatus.className = "status-line";
    targets.reportChatArchiveStatus.textContent = "正在读取 RAG 问答档案…";
    targets.reportChatArchiveList.innerHTML = '<div class="empty-state">正在读取问答存档…</div>';
    if (targets.reportChatArchiveRefresh) targets.reportChatArchiveRefresh.disabled = true;
    try {
      const data = await fetchAdminReportChatHistory(workerUrl);
      targets.reportChatArchiveList.innerHTML = renderAdminReportChatArchives(data.items);
      targets.reportChatArchiveStatus.className = "status-line ok";
      targets.reportChatArchiveStatus.textContent = data.items.length
        ? `已加载 ${data.items.length} 条问答存档${data.total > data.items.length ? `，共 ${data.total} 条` : ""}。`
        : "还没有 RAG 问答存档。";
      return data.items;
    } catch (error) {
      targets.reportChatArchiveList.innerHTML = '<div class="error-state">RAG 问答档案暂时无法读取，请稍后重试。</div>';
      targets.reportChatArchiveStatus.className = "status-line error";
      targets.reportChatArchiveStatus.textContent = error.message || "RAG 问答档案读取失败。";
      return [];
    } finally {
      if (targets.reportChatArchiveRefresh) targets.reportChatArchiveRefresh.disabled = false;
    }
  }

  async function curateAdminReportChatArchive(workerUrl, archiveId, action) {
    const normalizedAction = action === "unpublish" ? "unpublish" : (action === "publish" ? "publish" : "");
    if (!archiveId || !normalizedAction) throw new Error("问答存档操作无效。");
    const response = await fetch(`${workerUrl}/account-admin/report-chat-curation`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify({ archive_id: archiveId, published: normalizedAction === "publish" }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || data.ok === false) throw new Error(data.detail || "问答精选状态更新失败。");
    return data;
  }

  function accountAdminModalMarkup(options = {}) {
    const title = options.title || "管理后台";
    const showWechat = options.showWechat !== false;
    const showUsers = options.showUsers !== false;
    const showAnalytics = options.showAnalytics !== false;
    const showHotReports = options.showHotReports !== false;
    const showReportChatArchives = options.showReportChatArchives === true;
    const uploadProgressMarkup = typeof adminPdfUploadProgressMarkup === "function"
      ? adminPdfUploadProgressMarkup
      : () => "";
    return `
      <div class="admin-modal account-admin-modal" id="accountAdminModal" role="dialog" aria-modal="true" aria-labelledby="accountAdminTitle">
        <div class="admin-dialog account-admin-dialog">
          <button class="admin-close" id="accountAdminClose" type="button" aria-label="Close">&times;</button>
          <div class="account-admin-top">
            <h3 id="accountAdminTitle">${escapeHtml(title)}</h3>
            <button class="secondary-button" id="accountAdminRefresh" type="button">刷新</button>
          </div>
          <div id="accountAdminStatus" class="status-line" aria-live="polite">正在读取后台信息…</div>
          <section class="account-admin-section account-admin-picks-section">
            <div class="account-admin-heading">
              <strong>每日精选</strong>
              <span id="accountAdminPickCount"></span>
            </div>
            <div id="accountAdminPicksNotice" class="account-admin-module-notice" hidden></div>
            <div id="accountAdminPicks" class="account-admin-picks"></div>
          </section>
          <section class="account-admin-section account-admin-market-views-section" id="accountAdminMarketViewsSection">
            <div class="account-admin-heading">
              <strong>Market Views</strong>
              <span id="accountAdminMarketViewCount"></span>
              <button class="secondary-button account-admin-more-button" id="accountAdminMarketViewsMore" type="button" aria-haspopup="dialog" hidden>更多</button>
            </div>
            <div id="accountAdminMarketViewsNotice" class="account-admin-module-notice" hidden></div>
            <div id="accountAdminMarketViews" class="account-admin-files"></div>
          </section>
          <section class="account-admin-section account-admin-wechat-section" id="accountAdminWechatSection" ${showWechat ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>公众号发送时间</strong>
              <span id="accountAdminWechatCount"></span>
            </div>
            <div id="accountAdminWechatNotice" class="account-admin-module-notice" hidden></div>
            <div id="accountAdminWechatSchedule" class="account-admin-wechat-schedule"></div>
          </section>
          <section class="account-admin-section account-admin-hot-section" id="accountAdminHotReportsSection" ${showHotReports ? "" : "hidden"}>
            <div class="account-admin-heading account-admin-intake-heading">
              <strong>PDF 入库中心</strong>
              <span>统一处理新报告、缺失 PDF 与报告申请</span>
            </div>
            <p class="account-admin-intake-scope">当前可补齐：Text only、已声明有 PDF 但对象缺失或归档失效的 Catalog 报告、报告A、高权报告。External 与国际智库的临时准备失败不会被当作永久缺失。</p>
            <div class="account-admin-upload-recovery" id="accountAdminUploadRecovery" hidden>
              <strong>发现尚未确认的上传</strong>
              <p id="accountAdminUploadRecoveryText"></p>
              <button class="secondary-button" id="accountAdminUploadRecoveryCheck" type="button">检查上传结果</button>
            </div>
            <div class="account-admin-intake-tabs" role="tablist" aria-label="PDF 入库类型">
              <button class="is-active" id="accountAdminIntakeNewTab" type="button" role="tab" aria-selected="true" aria-controls="accountAdminIntakeNew" data-admin-intake-mode="new">新报告</button>
              <button id="accountAdminIntakeCatalogTab" type="button" role="tab" aria-selected="false" aria-controls="accountAdminIntakeCatalog" data-admin-intake-mode="catalog">补齐 Text only / 缺失 PDF</button>
              <button id="accountAdminIntakeRequestTab" type="button" role="tab" aria-selected="false" aria-controls="accountAdminIntakeRequest" data-admin-intake-mode="request">待满足申请</button>
            </div>
            <div class="account-admin-intake-panel" id="accountAdminIntakeNew" role="tabpanel" aria-labelledby="accountAdminIntakeNewTab">
              <form id="accountAdminHotReportForm" class="account-admin-hot-form" enctype="multipart/form-data">
                <div class="account-admin-form-grid">
                  <label>
                    <span>英文/主标题</span>
                    <input id="accountAdminHotReportTitle" name="title" type="text" maxlength="320" autocomplete="off" required>
                  </label>
                  <label>
                    <span>中文标题（可选）</span>
                    <input name="title_cn" type="text" maxlength="320" autocomplete="off">
                  </label>
                  <label>
                    <span>机构（可选）</span>
                    <input name="institution" type="text" maxlength="160" autocomplete="off">
                  </label>
                  <label>
                    <span>报告日期</span>
                    <input id="accountAdminHotReportDate" name="date" type="date" required>
                  </label>
                </div>
                <label class="account-admin-hot-description">
                  <span>简介（可选）</span>
                  <textarea name="description" rows="3" maxlength="1600" placeholder="显示在报告详情页"></textarea>
                </label>
                <label class="account-admin-hot-file">
                  <span>PDF 文件（最大 95 MB）</span>
                  <input id="accountAdminHotReportPdf" name="pdf" type="file" accept="application/pdf,.pdf" required>
                </label>
                ${uploadProgressMarkup("accountAdminHotReportUpload")}
                <div class="account-admin-hot-actions">
                  <span>3个月及以上会员可下载全文。</span>
                  <button class="primary" type="submit">上传到近期热门报告</button>
                </div>
              </form>
              <div id="accountAdminHotReportStatus" class="status-line" aria-live="polite"></div>
            </div>
            <div class="account-admin-intake-panel" id="accountAdminIntakeCatalog" role="tabpanel" aria-labelledby="accountAdminIntakeCatalogTab" hidden>
              <p class="subtle">先检索并选择原记录。系统只允许补齐 Text only 或经现场核验确实缺失的 PDF；有效 PDF 不能被覆盖。</p>
              <form id="accountAdminCatalogIntakeSearch" class="account-admin-intake-search" role="search">
                <label>
                  <span>报告标题或编号</span>
                  <input id="accountAdminCatalogIntakeQuery" type="search" autocomplete="off" placeholder="输入完整标题或报告编号" required>
                </label>
                <button class="secondary-button" type="submit">检索可补齐记录</button>
              </form>
              <div id="accountAdminCatalogIntakeStatus" class="status-line" aria-live="polite"></div>
              <div id="accountAdminCatalogIntakeResults" class="account-admin-intake-results"><div class="empty-state">输入标题后检索 Text only 或缺失 PDF 的 Catalog 记录。</div></div>
              <form id="accountAdminCatalogIntakeUpload" class="account-admin-intake-upload" enctype="multipart/form-data" hidden>
                <div class="account-admin-intake-selection" id="accountAdminCatalogIntakeSelection"></div>
                <label class="account-admin-hot-file">
                  <span>用于补齐的 PDF（最大 95 MB）</span>
                  <input id="accountAdminCatalogIntakePdf" name="pdf" type="file" accept="application/pdf,.pdf" required>
                </label>
                ${uploadProgressMarkup("accountAdminCatalogUpload")}
                <div class="account-admin-hot-actions">
                  <span>上传后保留原报告 ID、标题、索引和权限规则。</span>
                  <button class="primary" type="submit">补齐所选报告</button>
                </div>
              </form>
            </div>
            <div class="account-admin-intake-panel" id="accountAdminIntakeRequest" role="tabpanel" aria-labelledby="accountAdminIntakeRequestTab" hidden>
              <div class="account-admin-intake-request-top">
                <p class="subtle">选择高权报告或报告A申请记录，上传并绑定原报告；完成后原详情会切换为会员下载入口。</p>
                <button class="secondary-button" id="accountAdminRequestQueueRefresh" type="button">刷新申请队列</button>
              </div>
              <form id="accountAdminRequestQueueSearch" class="account-admin-intake-search" role="search">
                <label>
                  <span>筛选申请 / 主动检索原报告</span>
                  <input id="accountAdminRequestQueueQuery" type="search" autocomplete="off" placeholder="输入标题、机构或完整报告编号">
                </label>
                <button class="secondary-button" type="submit">搜索申请与原记录</button>
              </form>
              <div id="accountAdminRequestQueueStatus" class="status-line" aria-live="polite"></div>
              <div id="accountAdminRequestQueueResults" class="account-admin-intake-results"><div class="empty-state">正在读取待满足申请…</div></div>
              <form id="accountAdminRequestIntakeUpload" class="account-admin-intake-upload" enctype="multipart/form-data" hidden>
                <div class="account-admin-intake-selection" id="accountAdminRequestIntakeSelection"></div>
                <label class="account-admin-hot-file">
                  <span>用于满足申请的 PDF（最大 95 MB）</span>
                  <input id="accountAdminRequestIntakePdf" name="pdf" type="file" accept="application/pdf,.pdf" required>
                </label>
                ${uploadProgressMarkup("accountAdminRequestUpload")}
                <div class="account-admin-hot-actions">
                  <span>系统会绑定原报告来源和编号，不会创建无法追溯的重复线索。</span>
                  <button class="primary" type="submit">上传并绑定原报告</button>
                </div>
              </form>
            </div>
            <div class="account-admin-heading account-admin-hot-list-heading">
              <strong>近期热门报告</strong>
              <span id="accountAdminHotReportCount"></span>
              <button class="secondary-button account-admin-more-button" id="accountAdminHotReportsMore" type="button" aria-haspopup="dialog" hidden>更多</button>
            </div>
            <div id="accountAdminHotReportList" class="account-admin-hot-list"></div>
          </section>
          <section class="account-admin-section">
            <div class="account-admin-heading">
              <strong>每日文件</strong>
              <span>最近同步</span>
            </div>
            <div id="accountAdminFilesNotice" class="account-admin-module-notice" hidden></div>
            <div id="accountAdminFiles" class="account-admin-files"></div>
          </section>
          <section class="account-admin-section" id="accountAdminAnalyticsSection" ${showAnalytics ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>访问与搜索</strong>
              <span id="accountAdminAnalyticsCount"></span>
            </div>
            <div id="accountAdminAnalyticsNotice" class="account-admin-module-notice" hidden></div>
            <div id="accountAdminAnalytics" class="account-admin-analytics"></div>
          </section>
          <section class="account-admin-section" id="accountAdminReportChatArchiveSection" ${showReportChatArchives ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>RAG 问答档案</strong>
              <span>查看历史问答并选择首页公开内容</span>
              <button class="secondary-button" id="accountAdminReportChatArchiveRefresh" type="button">刷新问答档案</button>
            </div>
            <div id="accountAdminReportChatArchiveStatus" class="status-line" aria-live="polite"></div>
            <div id="accountAdminReportChatArchiveList" class="account-admin-files"><div class="empty-state">正在读取问答存档…</div></div>
          </section>
          <section class="account-admin-section" id="accountAdminUsersSection" ${showUsers ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>用户信息</strong>
              <span id="accountAdminUserCount"></span>
              <button class="secondary-button" id="accountAdminExportUsers" type="button">导出 Excel</button>
              <button class="secondary-button" id="accountAdminNewUser" type="button">新增用户</button>
            </div>
            <div id="accountAdminUsersNotice" class="account-admin-module-notice" hidden></div>
            <form id="accountAdminPasswordReset" class="account-admin-password-reset">
              <label>
                <span>重置用户密码</span>
                <select id="accountAdminPasswordResetEmail" required>
                  <option value="">选择用户</option>
                </select>
              </label>
              <button class="secondary-button" type="submit" disabled>重置为 123456</button>
              <small>重置后请通知该用户登录并自行修改密码。</small>
            </form>
            <form id="accountAdminUserCreator" class="account-admin-user-editor" hidden>
              <div class="account-admin-user-editor-head">
                <strong>新增用户</strong>
                <button class="secondary-button" id="accountAdminUserCreatorClose" type="button">关闭</button>
              </div>
              <div class="account-admin-form-grid">
                <label>
                  <span>用户名</span>
                  <input id="accountAdminNewUsername" type="text" autocomplete="off" placeholder="username">
                </label>
                <label>
                  <span>邮箱</span>
                  <input id="accountAdminNewEmail" type="email" autocomplete="off" placeholder="name@example.com">
                </label>
                <label>
                  <span>临时密码</span>
                  <input id="accountAdminNewPassword" type="text" autocomplete="off" placeholder="至少4位">
                </label>
              </div>
              <div class="account-admin-user-editor-actions">
                <button class="primary" type="submit">创建用户</button>
              </div>
            </form>
            <form id="accountAdminUserEditor" class="account-admin-user-editor" hidden>
              <div class="account-admin-user-editor-head">
                <strong id="accountAdminUserEditorTitle">编辑用户权限</strong>
                <button class="secondary-button" id="accountAdminUserEditorClose" type="button">关闭</button>
              </div>
              <input id="accountAdminAccessEmail" type="hidden">
              <div class="account-admin-form-grid">
                <label>
                  <span>权限范围</span>
                  <select id="accountAdminAccessMode"></select>
                </label>
                <label>
                  <span>开通时长</span>
                  <select id="accountAdminAccessDuration"></select>
                </label>
                <label>
                  <span>到期日期（可精确指定）</span>
                  <input id="accountAdminAccessExpiry" type="date">
                </label>
                <div class="account-admin-access-field">
                  <div class="account-admin-access-field-head">
                    <span>机构（可多选）</span>
                    <span id="accountAdminAccessInstitutionCount">已选 0</span>
                  </div>
                  <input id="accountAdminAccessInstitutionSearch" type="search" autocomplete="off" placeholder="搜索机构">
                  <div class="account-admin-access-checkboxes" id="accountAdminAccessInstitutions" role="group" aria-label="机构下载权限"></div>
                  <small>直接勾选多个机构（最多 60 项）；已有但不在当前目录中的授权会标为“历史授权”并继续保留。</small>
                </div>
                <label>
                  <span>Industry</span>
                  <select id="accountAdminAccessIndustries" multiple></select>
                </label>
              </div>
              <div class="account-admin-page-ranges" id="accountAdminAccessPageRanges"></div>
              <label class="account-admin-note-field">
                <span>备注</span>
                <input id="accountAdminAccessNote" type="text" placeholder="可选">
              </label>
              <label class="account-admin-renew-field">
                <span>续期</span>
                <span class="account-admin-renew-choice"><input id="accountAdminAccessRenew" type="checkbox"> 从今天按所选时长重新计算到期日</span>
                <small>不勾选时，只改范围不会自动延长；需要精确日期可直接修改上方到期日期。</small>
              </label>
              <div class="account-admin-user-editor-actions">
                <button class="primary" type="submit">保存权限</button>
              </div>
            </form>
            <div class="account-admin-table-wrap">
              <table class="account-admin-table">
                <thead>
                  <tr>
	                    <th>用户名</th>
	                    <th>邮箱</th>
	                    <th>注册站点</th>
	                    <th>状态</th>
                    <th>账号</th>
                    <th>实际下载权限</th>
                    <th>到期</th>
                    <th>权限来源</th>
                    <th>注册</th>
                    <th>最近登录</th>
                    <th>操作</th>
                  </tr>
                </thead>
                <tbody id="accountAdminUsers"></tbody>
              </table>
            </div>
          </section>
        </div>
      </div>
    `;
  }

  function adminUserEntitlementLabel(user) {
    if (user && user.role === "super") return "super";
    const entitlement = user && user.entitlement || {};
    if (entitlement.active) return entitlement.plan || "active";
    return "free";
  }

  function adminUserAccessLabel(user) {
    const access = user && (user.effective_access || user.access) || {};
    if (access.source === "disabled") return "账号已禁用（不可下载）";
    if (access.source === "error") return "权限读取失败（已拒绝）";
    if (!access.active) return "未开通";
    const suffix = accountRightUsageText(access);
    if (access.access_mode === "all") return suffix ? `全站报告 · ${suffix}` : "全站报告";
    if (access.access_mode === "filters") {
      const parts = [];
      if (Array.isArray(access.institutions) && access.institutions.length) parts.push(`机构 ${access.institutions.length}`);
      if (Array.isArray(access.industries) && access.industries.length) parts.push(`行业 ${access.industries.length}`);
      if (Array.isArray(access.page_ranges) && access.page_ranges.length) parts.push(`页数 ${access.page_ranges.length}`);
      const label = parts.length ? parts.join(" / ") : "条件报告";
      return suffix ? `${label} · ${suffix}` : label;
    }
    const label = access.access_mode || "active";
    return suffix ? `${label} · ${suffix}` : label;
  }

  function adminUserAccessExpiry(user) {
    const access = user && (user.effective_access || user.access) || {};
    if (access.source === "disabled") return "-";
    if (access.source === "error") return "核验失败";
    if (!access.active) return "-";
    if (access.lifetime) return "长期";
    return access.current_period_end ? String(access.current_period_end).slice(0, 10) : "-";
  }

  function adminUserAccessSource(user) {
    const access = user && (user.effective_access || user.access) || {};
    const entitlement = user && user.entitlement || {};
    if (access.source === "role") return "账号角色";
    if (access.source === "disabled") return "账号已禁用";
    if (["vid2ppt_nova", "vid2ppt_atlas"].includes(access.source)) return "历史会员权益";
    if (access.source === "entitlement+stored") return "会员权益 + 后台授权";
    if (access.source === "entitlement") {
      return ["vid2ppt_nova", "vid2ppt_atlas"].includes(entitlement.grant_source)
        ? "历史会员权益"
        : "会员权益";
    }
    if (access.source === "stored") return "后台授权";
    if (access.source === "error") return "核验失败（已拒绝）";
    return "未授权";
  }

  function adminUserViewModel(user) {
    const disabled = Boolean(user && user.disabled);
    const rawSiteOrigin = String(user && (user.site_origin || user.registered_site) || "portal");
    const rawRegisteredSite = String(user && (user.registered_site || user.site_origin) || "portal");
    const rawSourceSite = String(user && user.entitlement && user.entitlement.source_site || "");
    const rawGrantSource = String(user && user.entitlement && user.entitlement.grant_source || "");
    const historicalLinkedEntitlement = rawSourceSite === "vid2ppt" || ["vid2ppt_nova", "vid2ppt_atlas"].includes(rawGrantSource);
    const publicOriginLabel = (value) => {
      const text = String(value || "").trim();
      if (!text || text === "portal") return PUBLIC_BRAND;
      if (text === "vid2ppt") return "历史会员";
      return publicBrandText(text, PUBLIC_BRAND);
    };
    return {
      username: String(user && user.username || ""),
      email: String(user && user.email || ""),
      site_origin: publicOriginLabel(rawSiteOrigin),
      registered_site: publicOriginLabel(rawRegisteredSite),
      entitlement_source_site: historicalLinkedEntitlement ? "历史会员" : publicOriginLabel(rawSourceSite),
      entitlement_grant_source: historicalLinkedEntitlement ? "历史会员" : publicBrandText(rawGrantSource),
      entitlement_plan_code: historicalLinkedEntitlement ? "" : publicBrandText(user && user.entitlement && user.entitlement.source_plan_code),
      status: disabled ? "已禁用" : "正常",
      account: adminUserEntitlementLabel(user),
      access: adminUserAccessLabel(user),
      expiry: adminUserAccessExpiry(user),
      registered: String(user && user.created_at || "").slice(0, 10),
      last_login: String(user && user.last_login_at || "").replace("T", " ").slice(0, 16),
      access_source: adminUserAccessSource(user),
      access_updated: String(user && (user.effective_access || user.access) && (user.effective_access || user.access).updated_at || "").replace("T", " ").slice(0, 19),
      disabled,
    };
  }

  function adminUserRow(user) {
    const view = adminUserViewModel(user);
    const email = view.email;
    const canEditAccess = user.role === "user";
    const canToggleStatus = user.role !== "super";
    const disabled = view.disabled;
    return `
      <tr data-email="${escapeHtml(email)}"${disabled ? ' class="is-disabled-user"' : ""}>
        <td>${escapeHtml(view.username)}</td>
        <td>${escapeHtml(email)}</td>
        <td>${escapeHtml(view.registered_site || view.site_origin)}</td>
        <td><span class="account-admin-user-status${disabled ? " is-disabled" : ""}">${escapeHtml(view.status)}</span></td>
        <td>${escapeHtml(view.account)}</td>
        <td title="${escapeHtml(view.access_source)}">${escapeHtml(view.access)}</td>
        <td>${escapeHtml(view.expiry)}</td>
        <td>${escapeHtml(view.access_source)}</td>
        <td>${escapeHtml(view.registered)}</td>
        <td>${escapeHtml(view.last_login)}</td>
        <td>${canEditAccess || canToggleStatus ? `
          <div class="account-admin-row-actions">
            ${canEditAccess ? `<button class="secondary-button account-admin-edit-user" type="button" data-email="${escapeHtml(email)}">编辑</button>` : ""}
            ${canToggleStatus ? `<button class="secondary-button account-admin-toggle-user" type="button" data-email="${escapeHtml(email)}" data-disabled="${disabled ? "false" : "true"}">${disabled ? "启用" : "禁用"}</button>` : ""}
          </div>
        ` : ""}</td>
      </tr>
    `;
  }

  function adminUserSortTimestamp(value) {
    const timestamp = Date.parse(String(value || ""));
    return Number.isFinite(timestamp) ? timestamp : 0;
  }

  function compareAdminUsers(left, right) {
    const disabledDifference = Number(Boolean(left && left.disabled)) - Number(Boolean(right && right.disabled));
    if (disabledDifference) return disabledDifference;
    const leftRecent = adminUserSortTimestamp(left && (left.last_login_at || left.created_at));
    const rightRecent = adminUserSortTimestamp(right && (right.last_login_at || right.created_at));
    if (rightRecent !== leftRecent) return rightRecent - leftRecent;
    const leftLogin = adminUserSortTimestamp(left && left.last_login_at);
    const rightLogin = adminUserSortTimestamp(right && right.last_login_at);
    if (rightLogin !== leftLogin) return rightLogin - leftLogin;
    const leftCreated = adminUserSortTimestamp(left && left.created_at);
    const rightCreated = adminUserSortTimestamp(right && right.created_at);
    if (rightCreated !== leftCreated) return rightCreated - leftCreated;
    return String(left && left.email || "").localeCompare(String(right && right.email || ""));
  }

  function renderAdminPasswordResetOptions(rows) {
    const select = document.getElementById("accountAdminPasswordResetEmail");
    if (!select) return;
    const current = select.value;
    const resettable = (rows || []).filter((user) => String(user && user.role || "user") === "user");
    select.innerHTML = [
      '<option value="">选择用户</option>',
      ...resettable.map((user) => {
        const email = String(user && user.email || "");
        const username = String(user && user.username || email);
        const suffix = user && user.disabled ? " · 已禁用" : "";
        return `<option value="${escapeHtml(email)}">${escapeHtml(`${username} · ${email}${suffix}`)}</option>`;
      }),
    ].join("");
    if ([...select.options].some((option) => option.value === current)) select.value = current;
    const submit = select.form && select.form.querySelector('button[type="submit"]');
    if (submit) submit.disabled = !select.value;
  }

  function renderAdminUserTable(targets) {
    if (!targets || !targets.users) return;
    const rows = [...accountAdminUsersByEmail.values()].sort(compareAdminUsers);
    if (targets.userCount) targets.userCount.textContent = `${rows.length} users`;
    targets.users.innerHTML = rows.length
      ? rows.map(adminUserRow).join("")
      : '<tr><td colspan="11">暂无用户。</td></tr>';
    renderAdminPasswordResetOptions(rows);
  }

  function optionMarkup(options = [], selected = []) {
    const selectedSet = new Set((Array.isArray(selected) ? selected : []).map(String));
    return (options || []).map((option) => {
      const value = String(option.value || "");
      return `<option value="${escapeHtml(value)}"${selectedSet.has(value) ? " selected" : ""}>${escapeHtml(option.label || value)}</option>`;
    }).join("");
  }

  function setSelectValues(select, values = []) {
    const selected = new Set((Array.isArray(values) ? values : []).map(String));
    Array.from(select.options).forEach((option) => {
      option.selected = selected.has(option.value);
    });
  }

  function selectedSelectValues(select) {
    return Array.from(select.selectedOptions || []).map((option) => option.value).filter(Boolean);
  }

  function accessOptionKey(value) {
    return String(value || "").normalize("NFKC").replace(/\s+/g, " ").trim().toLowerCase();
  }

  function mergeAccessOptionRows(options = [], selected = []) {
    const rows = Array.isArray(options) ? options : [];
    const selectedValues = (Array.isArray(selected) ? selected : []).map(String).filter(Boolean);
    const optionsByKey = new Map();
    rows.forEach((option) => {
      const value = String(option && option.value || "");
      const key = accessOptionKey(value);
      if (key && !optionsByKey.has(key)) optionsByKey.set(key, option);
    });
    const used = new Set();
    const merged = [];
    selectedValues.forEach((value) => {
      const key = accessOptionKey(value);
      if (!key || used.has(key)) return;
      const current = optionsByKey.get(key);
      merged.push(current
        ? { ...current, value }
        : { value, label: `${value}（历史授权，保留）`, legacy: true });
      used.add(key);
    });
    rows.forEach((option) => {
      const value = String(option && option.value || "");
      const key = accessOptionKey(value);
      if (!key || used.has(key)) return;
      merged.push(option);
      used.add(key);
    });
    return merged;
  }

  function renderAccessCheckboxOptions(target, options = [], selected = []) {
    if (!target) return;
    const selectedKeys = new Set((Array.isArray(selected) ? selected : []).map(accessOptionKey).filter(Boolean));
    target.innerHTML = mergeAccessOptionRows(options, selected).map((option, index) => {
      const value = String(option && option.value || "");
      const label = String(option && option.label || value);
      const inputId = `accountAdminInstitutionOption${index}`;
      const checked = selectedKeys.has(accessOptionKey(value));
      const searchText = `${value} ${label}`.normalize("NFKC").toLowerCase();
      return `
        <label class="account-admin-access-checkbox${option && option.legacy ? " is-legacy" : ""}" data-access-search="${escapeHtml(searchText)}">
          <input id="${inputId}" type="checkbox" value="${escapeHtml(value)}"${checked ? " checked" : ""}>
          <span>${escapeHtml(label)}</span>
        </label>
      `;
    }).join("");
  }

  function selectedAccessCheckboxValues(target) {
    return Array.from(target && target.querySelectorAll("input[type='checkbox']:checked") || [])
      .map((input) => input.value)
      .filter(Boolean);
  }

  function updateAccessCheckboxCount(target, countTarget) {
    if (!countTarget) return;
    countTarget.textContent = `已选 ${selectedAccessCheckboxValues(target).length}`;
  }

  function filterAccessCheckboxOptions(target, query) {
    const normalized = String(query || "").normalize("NFKC").trim().toLowerCase();
    Array.from(target && target.querySelectorAll(".account-admin-access-checkbox") || []).forEach((row) => {
      row.hidden = Boolean(normalized) && !String(row.dataset.accessSearch || "").includes(normalized);
    });
  }

  function accessScopeSnapshot(access = {}) {
    return {
      access_mode: String(access.access_mode || "none"),
      institutions: (Array.isArray(access.institutions) ? access.institutions : []).map(String).filter(Boolean),
      industries: (Array.isArray(access.industries) ? access.industries : []).map(String).filter(Boolean),
      page_ranges: (Array.isArray(access.page_ranges) ? access.page_ranges : []).map(String).filter(Boolean),
    };
  }

  function accessScopeNeedsConfirmation(previous = {}, next = {}) {
    const before = accessScopeSnapshot(previous);
    const after = accessScopeSnapshot(next);
    if (before.access_mode !== after.access_mode) {
      return before.access_mode !== "none" || after.access_mode === "all";
    }
    if (before.access_mode !== "filters") return false;
    return ["institutions", "industries", "page_ranges"].some((field) => {
      const nextKeys = new Set(after[field].map(accessOptionKey));
      return before[field].some((value) => !nextKeys.has(accessOptionKey(value)));
    });
  }

  function accessScopeConfirmationText(previous = {}, next = {}) {
    if (String(next.access_mode || "") === "all") {
      return "确认把该用户改为“全站报告”吗？这会移除原有的机构、行业和页数限制。";
    }
    if (String(next.access_mode || "") === "none") return "确认关闭该用户的下载权限吗？";
    return "这次保存会移除部分已有机构、行业或页数权限。确认继续吗？";
  }

  function accessDurationPreviewDate(durationValue) {
    const value = String(durationValue || "");
    if (!value || value === "lifetime") return "";
    const date = new Date();
    if (value === "trial_3d") date.setUTCDate(date.getUTCDate() + 3);
    else {
      const months = Number(value);
      if (!Number.isFinite(months) || months <= 0) return "";
      date.setUTCMonth(date.getUTCMonth() + months);
    }
    return date.toISOString().slice(0, 10);
  }

  function prepareExpiredAccessRenewal(targets) {
    if (!targets || targets.accessMode.value === "none" || targets.accessDuration.value === "lifetime") return;
    if (targets.accessRenew) targets.accessRenew.checked = true;
    if (targets.accessExpiry) targets.accessExpiry.value = accessDurationPreviewDate(targets.accessDuration.value);
  }

  function fillUserAccessEditor(user, targets) {
    if (!user || !targets.userEditor) return;
    const access = user.access || {};
    const options = accountAdminAccessOptions || {};
    const username = user.username || user.email || "";
    targets.userEditor.hidden = false;
    targets.userEditor.dataset.expectedChangeId = String(access.change_id || "");
    targets.userEditor.dataset.expectedUpdatedAt = String(access.updated_at || "");
    targets.userEditor.dataset.originalAccessActive = access.active ? "true" : "false";
    targets.userEditor.dataset.originalAccessScope = JSON.stringify(accessScopeSnapshot(access));
    targets.accessEmail.value = user.email || "";
    targets.userEditorTitle.textContent = `编辑权限：${username}`;
    targets.accessMode.innerHTML = optionMarkup(options.modes || [], [access.access_mode || "none"]);
    targets.accessDuration.innerHTML = optionMarkup(options.durations || [], [access.lifetime ? "lifetime" : (access.duration_value || "12")]);
    if (targets.accessExpiry) targets.accessExpiry.value = String(access.current_period_end || "").slice(0, 10);
    renderAccessCheckboxOptions(targets.accessInstitutions, options.institutions || [], access.institutions || []);
    targets.accessIndustries.innerHTML = optionMarkup(
      mergeAccessOptionRows(options.industries || [], access.industries || []),
      access.industries || [],
    );
    setSelectValues(targets.accessIndustries, access.industries || []);
    if (targets.accessInstitutionSearch) targets.accessInstitutionSearch.value = "";
    filterAccessCheckboxOptions(targets.accessInstitutions, "");
    updateAccessCheckboxCount(targets.accessInstitutions, targets.accessInstitutionCount);
    const selectedRanges = new Set(access.page_ranges || []);
    targets.accessPageRanges.innerHTML = (options.page_ranges || []).map((option) => `
      <label>
        <input type="checkbox" name="adminAccessPageRange" value="${escapeHtml(option.value || "")}"${selectedRanges.has(option.value) ? " checked" : ""}>
        <span>${escapeHtml(option.label || option.value || "")}</span>
      </label>
    `).join("");
    targets.accessNote.value = access.note || "";
    const needsRenewal = access.access_mode !== "none" && !access.active && !access.lifetime;
    if (targets.accessRenew) targets.accessRenew.checked = needsRenewal;
    if (needsRenewal) prepareExpiredAccessRenewal(targets);
    targets.accessMode.dispatchEvent(new Event("change"));
    if (targets.status) {
      targets.status.className = "status-line ok";
      targets.status.textContent = needsRenewal
        ? `${username || "用户"} 的旧权限已过期；保存时将从今天按所选时长重新开通。`
        : `正在编辑 ${username || "用户"} 的下载权限。`;
    }
    requestAnimationFrame(() => {
      targets.userEditor.scrollIntoView({ block: "nearest", behavior: "smooth" });
      if (targets.accessMode) targets.accessMode.focus({ preventScroll: true });
    });
  }

  function updateUserAccessEditorMode(targets) {
    if (!targets || !targets.userEditor) return;
    const filters = targets.accessMode.value === "filters";
    const enabled = targets.accessMode.value !== "none";
    if (targets.accessDuration) targets.accessDuration.disabled = !enabled;
    if (targets.accessExpiry) targets.accessExpiry.disabled = !enabled || targets.accessDuration.value === "lifetime";
    if (targets.accessRenew) targets.accessRenew.disabled = !enabled || targets.accessDuration.value === "lifetime";
    targets.accessInstitutions.querySelectorAll("input").forEach((input) => {
      input.disabled = !filters;
    });
    if (targets.accessInstitutionSearch) targets.accessInstitutionSearch.disabled = !filters;
    targets.accessIndustries.disabled = !filters;
    targets.accessPageRanges.querySelectorAll("input").forEach((input) => {
      input.disabled = !filters;
    });
  }

  async function saveUserAccess(workerUrl, targets) {
    const email = targets.accessEmail.value || "";
    const mode = targets.accessMode.value || "none";
    const payload = {
      email,
      access_mode: mode,
      duration_months: mode === "none" ? "" : (targets.accessDuration.value || "12"),
      institutions: mode === "filters" ? selectedAccessCheckboxValues(targets.accessInstitutions) : [],
      industries: mode === "filters" ? selectedSelectValues(targets.accessIndustries) : [],
      page_ranges: mode === "filters"
        ? Array.from(targets.accessPageRanges.querySelectorAll("input:checked")).map((input) => input.value)
        : [],
      note: targets.accessNote.value || "",
      renew: Boolean(targets.accessRenew && targets.accessRenew.checked),
      expires_on: mode === "none" ? "" : (targets.accessExpiry && targets.accessExpiry.value || ""),
      expected_change_id: String(targets.userEditor.dataset.expectedChangeId || ""),
      expected_updated_at: String(targets.userEditor.dataset.expectedUpdatedAt || ""),
      confirm_scope_change: false,
    };
    if (mode === "filters" && !payload.institutions.length && !payload.industries.length && !payload.page_ranges.length) {
      throw new Error("按条件筛选至少要勾选一个机构、行业或页数条件。");
    }
    let originalScope = {};
    try {
      const originalScopeText = targets.userEditor.dataset.originalAccessScope || "";
      if (!originalScopeText) throw new Error("missing scope");
      originalScope = JSON.parse(originalScopeText);
    } catch (_error) {
      throw new Error("原权限状态无法核验，请关闭编辑框并重新打开。");
    }
    if (accessScopeNeedsConfirmation(originalScope, payload)) {
      if (!window.confirm(accessScopeConfirmationText(originalScope, payload))) return { cancelled: true };
      payload.confirm_scope_change = true;
    }
    const response = await fetch(`${workerUrl}/account-admin/user-access`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify(payload),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "保存权限失败。");
    if (!data.verified) throw new Error("权限保存后读回校验失败，请重试。");
    const savedAccess = data.access && typeof data.access === "object" ? data.access : {};
    targets.userEditor.dataset.expectedChangeId = String(savedAccess.change_id || "");
    targets.userEditor.dataset.expectedUpdatedAt = String(savedAccess.updated_at || "");
    targets.userEditor.dataset.originalAccessActive = savedAccess.active ? "true" : "false";
    targets.userEditor.dataset.originalAccessScope = JSON.stringify(accessScopeSnapshot(savedAccess));
    if (targets.accessExpiry) targets.accessExpiry.value = String(savedAccess.current_period_end || "").slice(0, 10);
    if (targets.accessRenew) targets.accessRenew.checked = false;
    const updated = data.user || null;
    if (updated && updated.email) accountAdminUsersByEmail.set(String(updated.email), updated);
    else {
      const existing = accountAdminUsersByEmail.get(email) || { email };
      accountAdminUsersByEmail.set(email, { ...existing, access: data.access });
    }
    return data;
  }

  async function loadAdminUserAccess(workerUrl, email) {
    const response = await fetch(`${workerUrl}/account-admin/user-access?email=${encodeURIComponent(email)}`, {
      method: "GET",
      cache: "no-store",
      headers: authHeaders(),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !data.user) throw new Error(data.detail || "读取最新用户权限失败。");
    if (data.access_options && typeof data.access_options === "object") {
      accountAdminAccessOptions = data.access_options;
    }
    return data.user;
  }

  async function createAdminUser(workerUrl, targets) {
    const payload = {
      username: targets.newUsername.value || "",
      email: targets.newEmail.value || "",
      password: targets.newPassword.value || "",
    };
    const response = await fetch(`${workerUrl}/account-admin/user`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify(payload),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "创建用户失败。");
    if (data.user && data.user.email) {
      accountAdminUsersByEmail.set(String(data.user.email), data.user);
    }
    return data;
  }

  async function updateAdminUserStatus(workerUrl, email, disabled) {
    const response = await fetch(`${workerUrl}/account-admin/user-status`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify({ email, disabled: Boolean(disabled) }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "账号状态更新失败。");
    if (data.user && data.user.email) {
      accountAdminUsersByEmail.set(String(data.user.email), data.user);
    }
    return data;
  }

  async function resetAdminUserPassword(workerUrl, email) {
    const response = await fetch(`${workerUrl}/account-admin/user-password-reset`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify({ email, confirm_reset: true }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "密码重置失败。");
    if (data.user && data.user.email) {
      accountAdminUsersByEmail.set(String(data.user.email), data.user);
    }
    return data;
  }

  function adminFileRow(file) {
    const key = file.type === "artifact" ? file.id : file.path;
    const endpointAttr = file.type === "artifact" ? "artifact" : "file";
    const note = file.note ? `<span>${escapeHtml(publicMessageText(file.note))}</span>` : "";
    const rawRecommendedAccount = String(file.recommended_account || "");
    const recommendedAccount = publicBrandText(rawRecommendedAccount, "", PUBLIC_BRAND);
    const accountClass = /娱乐/u.test(rawRecommendedAccount) || file.kind === "portal-entertain"
      ? "is-entertain"
      : (recommendedAccount === PUBLIC_BRAND ? "is-desktop" : "is-bias");
    const accountLabel = recommendedAccount
      ? `
        <div class="account-admin-file-label">
          <span class="${accountClass}">适合：${escapeHtml(recommendedAccount)}</span>
          <small>${escapeHtml(file.account_label_confidence || "低")}信心 · ${escapeHtml(publicMessageText(file.account_label_reason))}</small>
        </div>
      `
      : "";
    const repo = file.repo || "";
    return `
      <div class="account-admin-file">
        <div>
          <strong>${escapeHtml(publicMessageText(file.label || file.kind || "File"))}</strong>
          <span>${escapeHtml(file.date || "")} · ${escapeHtml(publicMessageText(file.name))}${file.size_bytes ? ` · ${escapeHtml(formatSize(file.size_bytes))}` : ""}</span>
          ${note}
          ${accountLabel}
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions">
          <button class="secondary-button account-admin-download" type="button"
            data-kind="${escapeHtml(endpointAttr)}"
            data-file-kind="${escapeHtml(file.kind || "")}"
            data-key="${escapeHtml(key || "")}"
            data-repo="${escapeHtml(repo)}"
            data-size-bytes="${escapeHtml(String(file.size_bytes || 0))}"
            data-name="${escapeHtml(publicBrandText(file.name, "download"))}">下载</button>
        </div>
      </div>
    `;
  }

  function adminItemDateTimestamp(item) {
    const candidates = [
      item && item.date,
      item && item.report_date,
      item && item.published_at,
      item && item.created_at,
      item && item.updated_at,
    ];
    for (const candidate of candidates) {
      const value = String(candidate || "").trim();
      if (!value) continue;
      const timestamp = Date.parse(/^\d{4}-\d{2}-\d{2}$/.test(value) ? `${value}T00:00:00Z` : value);
      if (Number.isFinite(timestamp)) return timestamp;
    }
    const compactDate = String(item && item.id || "").match(/(?:^|:)(\d{2})(\d{2})(\d{2})$/);
    if (compactDate) {
      return Date.UTC(2000 + Number(compactDate[1]), Number(compactDate[2]) - 1, Number(compactDate[3]));
    }
    return 0;
  }

  function adminDatedItemsNewestFirst(items) {
    return (Array.isArray(items) ? items : [])
      .map((item, index) => ({ item, index, timestamp: adminItemDateTimestamp(item) }))
      .sort((left, right) => right.timestamp - left.timestamp || left.index - right.index)
      .map((entry) => entry.item);
  }

  function adminCollectionPreview(items, limit = 3) {
    const all = adminDatedItemsNewestFirst(items);
    const visibleLimit = Math.max(0, Number(limit) || 0);
    return {
      all,
      preview: all.slice(0, visibleLimit),
      hasMore: all.length > visibleLimit,
    };
  }

  function accountAdminListModalMarkup(options = {}) {
    const title = String(options.title || "完整列表");
    const count = Math.max(0, Number(options.count) || 0);
    const listClass = options.listClass === "account-admin-hot-list"
      ? "account-admin-hot-list"
      : "account-admin-files";
    return `
      <div class="admin-modal account-admin-list-modal" id="accountAdminListModal" role="dialog" aria-modal="true" aria-labelledby="accountAdminListTitle">
        <div class="admin-dialog account-admin-list-dialog">
          <button class="admin-close" id="accountAdminListClose" type="button" aria-label="关闭">&times;</button>
          <div class="account-admin-top account-admin-list-top">
            <h3 id="accountAdminListTitle">${escapeHtml(title)}</h3>
            <span>${count} 条</span>
          </div>
          <div class="status-line account-admin-list-status" id="accountAdminListStatus" aria-live="polite"></div>
          <div class="account-admin-list-body ${listClass}" id="accountAdminListBody">${String(options.bodyHtml || "")}</div>
        </div>
      </div>
    `;
  }

  function openAccountAdminListModal(options = {}) {
    if (accountAdminListModalCleanup) accountAdminListModalCleanup();
    const trigger = options.trigger || document.activeElement;
    const parentModal = document.getElementById("accountAdminModal");
    const parentAriaHidden = parentModal ? parentModal.getAttribute("aria-hidden") : null;
    const parentWasInert = Boolean(parentModal && parentModal.inert);
    document.body.insertAdjacentHTML("beforeend", accountAdminListModalMarkup(options));
    const modal = document.getElementById("accountAdminListModal");
    const close = document.getElementById("accountAdminListClose");
    const body = document.getElementById("accountAdminListBody");
    const status = document.getElementById("accountAdminListStatus");
    if (!modal || !close || !body || !status) return null;

    let finished = false;
    function finish() {
      if (finished) return;
      finished = true;
      modal.remove();
      if (parentModal) {
        if (parentAriaHidden === null) parentModal.removeAttribute("aria-hidden");
        else parentModal.setAttribute("aria-hidden", parentAriaHidden);
        if ("inert" in parentModal) parentModal.inert = parentWasInert;
      }
      if (accountAdminListModalCleanup === finish) accountAdminListModalCleanup = null;
      if (trigger && trigger.isConnected !== false && typeof trigger.focus === "function") {
        trigger.focus({ preventScroll: true });
      }
    }

    function focusableElements() {
      return Array.from(modal.querySelectorAll(
        'a[href], button:not([disabled]), input:not([disabled]), select:not([disabled]), textarea:not([disabled]), [tabindex]:not([tabindex="-1"])',
      )).filter((element) => !element.hidden);
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    modal.addEventListener("keydown", (event) => {
      if (event.key === "Escape") {
        event.preventDefault();
        finish();
        return;
      }
      if (event.key !== "Tab") return;
      const focusable = focusableElements();
      if (!focusable.length) {
        event.preventDefault();
        close.focus({ preventScroll: true });
        return;
      }
      const first = focusable[0];
      const last = focusable[focusable.length - 1];
      if (event.shiftKey && document.activeElement === first) {
        event.preventDefault();
        last.focus({ preventScroll: true });
      } else if (!event.shiftKey && document.activeElement === last) {
        event.preventDefault();
        first.focus({ preventScroll: true });
      }
    });
    if (typeof options.onBodyClick === "function") body.addEventListener("click", options.onBodyClick);

    close.focus({ preventScroll: true });
    if (parentModal) {
      parentModal.setAttribute("aria-hidden", "true");
      if ("inert" in parentModal) parentModal.inert = true;
    }
    accountAdminListModalCleanup = finish;
    return { modal, body, status, close: finish };
  }

  function adminMarketViewRow(item) {
    const id = String(item && item.id || "");
    const name = publicBrandText(item && item.filename, `${id || "market-views"}.pdf`);
    const title = publicBrandText(item && item.title, "Market Views");
    return `
      <div class="account-admin-file" data-market-view-id="${escapeHtml(id)}">
        <div>
          <strong>${escapeHtml(title)}</strong>
          <span>${escapeHtml(item && item.date || "")}${item && item.size_bytes ? ` · ${escapeHtml(formatSize(item.size_bytes))}` : ""}</span>
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions">
          <button class="secondary-button account-admin-market-view-download" type="button"
            data-market-view-id="${escapeHtml(id)}"
            data-name="${escapeHtml(name)}">下载 PDF</button>
        </div>
      </div>
    `;
  }

  async function loadAccountAdminMarketViews(workerUrl, targets) {
    if (!targets.marketViews) return [];
    try {
      const response = await fetch(`${workerUrl}/market-views`, { cache: "no-store" });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.detail || "Market Views 读取失败。");
      const items = Array.isArray(data.items) ? data.items : [];
      const view = adminCollectionPreview(items);
      accountAdminMarketViews = new Map(view.all.map((item) => [String(item.id || ""), item]));
      if (targets.marketViewCount) targets.marketViewCount.textContent = view.all.length ? `${view.all.length} PDFs` : "";
      if (targets.marketViewsMore) targets.marketViewsMore.hidden = !view.hasMore;
      targets.marketViews.innerHTML = view.preview.length
        ? view.preview.map(adminMarketViewRow).join("")
        : '<div class="empty-state">Market Views PDF 正在准备中。</div>';
      if (targets.marketViewsNotice) {
        targets.marketViewsNotice.hidden = true;
        targets.marketViewsNotice.textContent = "";
      }
      return view.all;
    } catch (error) {
      if (targets.marketViewsNotice) {
        targets.marketViewsNotice.hidden = false;
        targets.marketViewsNotice.className = "account-admin-module-notice error";
        targets.marketViewsNotice.textContent = error.message || "Market Views 暂时无法读取。";
      }
      if (!accountAdminMarketViews.size) {
        targets.marketViews.innerHTML = '<div class="empty-state">Market Views 暂时无法读取，请点击刷新重试。</div>';
        if (targets.marketViewsMore) targets.marketViewsMore.hidden = true;
      }
      throw error;
    }
  }

  async function handleAccountAdminMarketViewDownload(event, workerUrl, status) {
    const button = event.target.closest(".account-admin-market-view-download");
    if (!button) return false;
    const id = String(button.dataset.marketViewId || "");
    const item = accountAdminMarketViews.get(id);
    if (!id || !item) return false;
    if (cancelActiveAdminButton(button)) {
      status.className = "status-line";
      status.textContent = "正在取消…";
      return true;
    }
    const row = button.closest(".account-admin-file");
    const progress = row && row.querySelector(".account-admin-progress");
    const controller = new AbortController();
    startAdminButtonAction(button, controller);
    resetDownloadProgress(progress);
    status.className = "status-line";
    status.textContent = "正在下载 Market Views PDF…";
    try {
      const response = await fetch(`${workerUrl}/market-views/pdf?id=${encodeURIComponent(id)}`, {
        cache: "no-store",
        headers: authHeaders(),
        signal: controller.signal,
      });
      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.detail || `PDF 下载失败 (${response.status})。`);
      }
      const blob = await responseBlobWithProgress(response, progress);
      triggerBlobDownload(blob, response.headers.get("Content-Disposition") || "", item.filename || button.dataset.name || "market-views.pdf");
      status.className = "status-line ok";
      status.textContent = "Market Views PDF 下载已开始。";
    } catch (error) {
      status.className = error && error.name === "AbortError" ? "status-line" : "status-line error";
      status.textContent = error && error.name === "AbortError" ? "下载已取消。" : (error.message || "PDF 下载失败。");
    } finally {
      finishAdminButtonAction(button);
    }
    return true;
  }

  function adminPickMeta(pick) {
    const parts = [
      publicBrandText(pick.bank),
      pick.date_folder,
      pick.page_count ? `${pick.page_count}页` : "页数待识别",
      pick.first_page_landscape ? "横屏PDF" : "",
      pick.size_bytes ? formatSize(pick.size_bytes) : "",
    ].filter(Boolean);
    return parts.join(" · ");
  }

  function adminDailyPickRow(pick) {
    const intro = publicBrandText(pick.intro);
    const publicTitle = publicBrandText(pick.title);
    const title = publicBrandText(pick.display_title || pick.title_zh || publicTitle, "Untitled report");
    const tags = Array.isArray(pick.tags) && pick.tags.length
      ? `<div class="account-admin-pick-tags">${pick.tags.map((tag) => publicBrandText(tag)).filter(Boolean).map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>`
      : "";
    return `
      <article class="account-admin-pick" data-id="${escapeHtml(pick.id || "")}">
        <div class="account-admin-pick-main">
          <div class="account-admin-pick-title">
            <strong>${escapeHtml(title)}</strong>
            ${publicTitle && publicTitle !== title ? `<span>${escapeHtml(publicTitle)}</span>` : ""}
          </div>
          <span class="account-admin-pick-meta">${escapeHtml(adminPickMeta(pick))}</span>
          ${tags}
          <textarea class="account-admin-pick-intro" readonly aria-label="介绍文字">${escapeHtml(intro)}</textarea>
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions account-admin-pick-actions">
          <button class="secondary-button account-admin-copy-intro" type="button">复制文案</button>
          <button class="secondary-button account-admin-report-download" type="button">下载报告</button>
          <button class="secondary-button account-admin-cover-save" type="button">保存首图</button>
        </div>
      </article>
    `;
  }

  function adminWechatArticleList(batch) {
    const articles = Array.isArray(batch.articles) ? batch.articles.slice(0, 9) : [];
    if (!articles.length) return `<div class="account-admin-wechat-empty">这个 batch 暂无标题明细。</div>`;
    return `
      <ol class="account-admin-wechat-articles">
        ${articles.map((article, index) => `
          <li>
            <span>${escapeHtml(publicBrandText(article.label, `${index + 1}条`))}</span>
            <strong>${escapeHtml(publicBrandText(article.title))}</strong>
          </li>
        `).join("")}
      </ol>
    `;
  }

  function adminWechatScheduleHeader(schedule) {
    if (!schedule || !schedule.date_folder) return "还没有找到公众号草稿 batch。";
    const dateText = schedule.date_iso || schedule.date_folder;
    return `${dateText} · 推荐发送窗口 · ${schedule.window || "08:00 - 次日 00:30"}`;
  }

  function adminWechatSourceDateNote(schedule) {
    const sourceDates = Array.isArray(schedule && schedule.source_dates) ? schedule.source_dates : [];
    if (!sourceDates.length) return "";
    const text = sourceDates
      .map((entry) => {
        const label = publicBrandText(entry.source_label, "来源");
        const date = entry.date_iso || entry.date_folder || "";
        return `${label}: ${date}${entry.is_today ? "" : "（最近可用）"}`;
      })
      .join(" · ");
    const prefix = sourceDates.some((entry) => !entry.is_today)
      ? "部分来源今天还没有新草稿，已补入各来源最近可用 batch。"
      : "素材日期：";
    return `<div class="account-admin-wechat-note">${escapeHtml(prefix)} ${escapeHtml(text)}</div>`;
  }

  function adminWechatBatchRow(batch) {
    const meta = [
      publicBrandText(batch.source_label),
      batch.source_date_iso ? `素材 ${batch.source_date_iso}${batch.source_is_today ? "" : "（最近可用）"}` : "",
      batch.article_count ? `${batch.article_count}篇` : "",
      batch.total_batches ? `第 ${batch.schedule_index}/${batch.total_batches} 个 batch` : "",
    ].filter(Boolean).join(" · ");
    return `
      <article class="account-admin-wechat-batch">
        <div class="account-admin-wechat-time">
          <strong>${escapeHtml(batch.scheduled_time || "")}</strong>
          <span>${escapeHtml(batch.day_label || "")}</span>
        </div>
        <div class="account-admin-wechat-main">
          <div class="account-admin-wechat-title">
            <strong>${escapeHtml(publicBrandText(batch.batch_label, `Batch ${batch.batch_no || ""}`))}</strong>
            <span>${escapeHtml(meta)}</span>
          </div>
          ${adminWechatArticleList(batch)}
        </div>
      </article>
    `;
  }

  function renderAdminWechatSchedule(schedule) {
    const batches = Array.isArray(schedule && schedule.batches) ? schedule.batches : [];
    if (!batches.length) {
      return `
        <div class="empty-state">
          ${escapeHtml(adminWechatScheduleHeader(schedule))}
        </div>
      `;
    }
    const sourceDateNote = adminWechatSourceDateNote(schedule);
    return `
      <div class="account-admin-wechat-summary">
        <strong>${escapeHtml(adminWechatScheduleHeader(schedule))}</strong>
        <span>${escapeHtml(`${schedule.total_batches || batches.length} 个 batch · ${schedule.total_articles || 0} 篇文章`)}</span>
      </div>
      ${sourceDateNote}
      ${batches.map(adminWechatBatchRow).join("")}
    `;
  }

  function analyticsTime(value) {
    return String(value || "").replace("T", " ").slice(0, 16);
  }

  function analyticsSourcesText(sources) {
    if (!sources || typeof sources !== "object") return "";
    return Object.entries(sources)
      .sort((a, b) => Number(b[1] || 0) - Number(a[1] || 0))
      .map(([source, count]) => `${source} ${count}`)
      .join(" · ");
  }

  function analyticsEventFilterText(event) {
    const filters = [];
    if (event.page_range_labels) filters.push(`页数: ${event.page_range_labels}`);
    if (event.bank) filters.push(`机构: ${event.bank}`);
    if (event.industry) filters.push(`行业: ${event.industry}`);
    if (event.start_date || event.end_date) filters.push(`日期: ${event.start_date || "开始"}-${event.end_date || "今天"}`);
    if (event.scope && event.scope !== "all") filters.push(`范围: ${event.scope}`);
    if (event.availability) filters.push(`PDF: ${event.availability}`);
    return filters.join(" · ");
  }

  function analyticsMetric(label, value) {
    return `
      <div class="account-admin-metric">
        <span>${escapeHtml(label)}</span>
        <strong>${escapeHtml(String(value || 0))}</strong>
      </div>
    `;
  }

  function renderAnalyticsTopSearches(searches) {
    const rows = Array.isArray(searches) ? searches.slice(0, 12) : [];
    if (!rows.length) return '<div class="empty-state">还没有搜索记录。</div>';
    return `
      <div class="account-admin-table-wrap">
        <table class="account-admin-table account-admin-analytics-table">
          <thead>
            <tr>
              <th>搜索词</th>
              <th>次数</th>
              <th>访客</th>
              <th>来源</th>
              <th>最近</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map((row) => `
              <tr>
                <td><strong>${escapeHtml(row.query || "")}</strong></td>
                <td>${escapeHtml(row.count || 0)}</td>
                <td>${escapeHtml(row.visitor_count || 0)}</td>
                <td>${escapeHtml(analyticsSourcesText(row.sources))}</td>
                <td>${escapeHtml(analyticsTime(row.last_at))}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function renderAnalyticsTopReports(reports) {
    const rows = Array.isArray(reports) ? reports.slice(0, 10) : [];
    if (!rows.length) return '<div class="empty-state">还没有报告点击记录。</div>';
    return `
      <div class="account-admin-files account-admin-analytics-list">
        ${rows.map((row) => `
          <div class="account-admin-file">
            <div>
              <strong>${escapeHtml(row.title || row.report_id || "")}</strong>
              <span>${escapeHtml(row.source || "")} · 打开 ${escapeHtml(row.opens || 0)} · 下载 ${escapeHtml(row.downloads || 0)} · ${escapeHtml(analyticsTime(row.last_at))}</span>
            </div>
          </div>
        `).join("")}
      </div>
    `;
  }

  function analyticsEventUserText(event) {
    if (event.user && (event.user.username || event.user.email)) {
      return `${event.user.username || ""}${event.user.email ? ` · ${event.user.email}` : ""}`;
    }
    const visitor = event.visitor_id || event.ip_hash || "";
    return visitor ? String(visitor).slice(0, 18) : "匿名";
  }

  function analyticsEventContentText(event) {
    if (event.query) return `${event.source || ""} 搜索：${event.query}`;
    return event.report_title || event.report_id || event.target || event.path || "";
  }

  function analyticsEventStatusText(event) {
    return [
      event.result_count ? `${event.result_count}条` : "",
      analyticsEventFilterText(event),
      event.action || "",
      event.cache_status || "",
      event.status || "",
      event.duration_ms ? `${event.duration_ms}ms` : "",
      event.error || "",
    ].filter(Boolean).join(" · ");
  }

  function renderAnalyticsRecentEvents(events, limit = 30) {
    const sourceRows = Array.isArray(events) ? events : [];
    const rows = limit > 0 ? sourceRows.slice(0, limit) : sourceRows;
    if (!rows.length) return '<div class="empty-state">还没有最近事件。</div>';
    return `
      <div class="account-admin-table-wrap">
        <table class="account-admin-table account-admin-analytics-table">
          <thead>
            <tr>
              <th>时间</th>
              <th>事件</th>
              <th>用户/访客</th>
              <th>内容</th>
              <th>状态</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map((event) => {
              return `
                <tr>
                  <td>${escapeHtml(analyticsTime(event.ts))}</td>
                  <td>${escapeHtml(event.type || "")}</td>
                  <td>${escapeHtml(analyticsEventUserText(event))}</td>
                  <td>${escapeHtml(analyticsEventContentText(event))}</td>
                  <td>${escapeHtml(analyticsEventStatusText(event))}</td>
                </tr>
              `;
            }).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function renderAccountAdminAnalytics(analytics) {
    if (!analytics || typeof analytics !== "object") {
      return '<div class="empty-state">还没有可用的访问数据。</div>';
    }
    return `
      <div class="account-admin-metrics">
        ${analyticsMetric("访客", analytics.visitor_count)}
        ${analyticsMetric("搜索", analytics.search_count)}
        ${analyticsMetric("报告打开", analytics.report_open_count)}
        ${analyticsMetric("下载", analytics.download_success_count)}
        ${analyticsMetric("发货链接", analytics.delivery_link_count)}
      </div>
      <p class="subtle">本卡片从近 ${Number(analytics.range_days || 7)} 天窗口抽样 ${Number(analytics.sample_event_count || analytics.event_count || 0).toLocaleString("zh-CN")} 条事件；完整日统计与来源落地明细请进入 Activity。</p>
      <div class="account-admin-analytics-grid">
        <section>
          <h4>站内热门搜索</h4>
          ${renderAnalyticsTopSearches(analytics.top_searches)}
        </section>
        <section>
          <h4>热门报告</h4>
          ${renderAnalyticsTopReports(analytics.top_reports)}
        </section>
      </div>
      <section>
        <div class="account-admin-analytics-heading">
          <h4>抽样事件</h4>
          <a class="secondary-button" href="activity.html" target="_blank" rel="noopener">查看全部已采集记录</a>
        </div>
        ${renderAnalyticsRecentEvents(analytics.recent_events)}
      </section>
    `;
  }

  const ANALYTICS_EVENT_LABELS = {
    page_view: "页面访问",
    search: "搜索",
    report_open: "打开报告",
    download_attempt: "尝试下载",
    download_success: "下载成功",
    download_error: "下载失败",
    download_pending: "等待报告",
    delivery_link_generate: "生成发货链接",
    account_auth: "账号操作",
    admin_user_update: "用户权限操作",
    daily_file_download: "每日文件下载",
    report_chat: "RAG 研究问答",
    report_chat_interaction: "RAG 问答交互",
    course_material_request: "课程材料索取",
  };

  function analyticsEventLabel(type) {
    const value = String(type || "");
    return ANALYTICS_EVENT_LABELS[value] || value || "其他事件";
  }

  function analyticsEventEnvironmentText(event) {
    return [
      event.country || "",
      event.colo ? `节点 ${event.colo}` : "",
      event.page ? `页面 ${event.page}` : "",
      event.source ? `内容源 ${event.source}` : "",
    ].filter(Boolean).join(" · ");
  }

  function analyticsEventDetailText(event) {
    return [
      event.path ? `路径：${event.path}` : "",
      event.referrer ? `来源页：${event.referrer}` : "",
      event.user_agent ? `设备：${event.user_agent}` : "",
      event.institution ? `机构：${event.institution}` : "",
      event.target ? `对象：${event.target}` : "",
      event.report_id ? `报告 ID：${event.report_id}` : "",
      event.parent_report_id ? `父报告 ID：${event.parent_report_id}` : "",
      event.placement ? `推荐位置：${event.placement}` : "",
      event.visitor_id ? `访客 ID：${event.visitor_id}` : "",
      event.ip_hash ? `IP Hash：${event.ip_hash}` : "",
    ].filter(Boolean).join("\n");
  }

  function renderAnalyticsHistoryEvents(events) {
    const rows = Array.isArray(events) ? events : [];
    if (!rows.length) {
      return '<div class="empty-state">当前区间没有匹配事件。</div>';
    }
    return `
      <div class="account-admin-table-wrap analytics-history-table-wrap">
        <table class="account-admin-table analytics-history-table">
          <thead>
            <tr>
              <th>时间</th>
              <th>事件</th>
              <th>用户 / 访客</th>
              <th>内容</th>
              <th>条件 / 状态</th>
              <th>环境</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map((event) => {
              const detail = analyticsEventDetailText(event);
              return `
                <tr>
                  <td class="analytics-history-time">${escapeHtml(analyticsTime(event.ts))}</td>
                  <td>
                    <strong>${escapeHtml(analyticsEventLabel(event.type))}</strong>
                    <small>${escapeHtml(event.type || "")}</small>
                  </td>
                  <td>
                    <strong>${escapeHtml(analyticsEventUserText(event))}</strong>
                    <small>${escapeHtml(event.user && event.user.role || "")}</small>
                  </td>
                  <td class="analytics-history-content">
                    <strong>${escapeHtml(analyticsEventContentText(event))}</strong>
                    <small>${escapeHtml(event.institution || event.report_id || event.path || "")}</small>
                  </td>
                  <td>${escapeHtml(analyticsEventStatusText(event))}</td>
                  <td>
                    <span>${escapeHtml(analyticsEventEnvironmentText(event))}</span>
                    ${detail ? `
                      <details class="analytics-event-details">
                        <summary>详细信息</summary>
                        <pre>${escapeHtml(detail)}</pre>
                      </details>
                    ` : ""}
                  </td>
                </tr>
              `;
            }).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  const ANALYTICS_HISTORY_EXPORT_MAX_PAGES = 12000;
  const ANALYTICS_HISTORY_EXPORT_MAX_ROWS = 1048575;
  const ANALYTICS_HISTORY_EXPORT_PAGE_SIZE = 50;
  const ANALYTICS_HISTORY_EXPORT_COLUMNS = [
    { header: "时间（ISO）", key: "ts", width: 25 },
    { header: "北京时间日期", key: "date", width: 14 },
    { header: "事件", key: "event_label", width: 16 },
    { header: "事件代码", key: "type", width: 24 },
    { header: "用户名", key: "username", width: 18 },
    { header: "邮箱", key: "email", width: 30 },
    { header: "账号角色", key: "role", width: 14 },
    { header: "访客 ID", key: "visitor_id", width: 28 },
    { header: "会话 ID", key: "session_id", width: 28 },
    { header: "会话开始时间", key: "session_started_at", width: 25 },
    { header: "首次访问", key: "first_seen_at", width: 25 },
    { header: "回访", key: "is_returning", width: 10 },
    { header: "会话落地页", key: "landing_path", width: 36 },
    { header: "IP Hash", key: "ip_hash", width: 28 },
    { header: "国家", key: "country", width: 10 },
    { header: "节点", key: "colo", width: 10 },
    { header: "页面", key: "page", width: 18 },
    { header: "路径", key: "path", width: 36 },
    { header: "内容来源", key: "source", width: 18 },
    { header: "搜索词", key: "query", width: 36 },
    { header: "机构", key: "institution", width: 24 },
    { header: "行业", key: "industry", width: 24 },
    { header: "开始日期", key: "start_date", width: 14 },
    { header: "结束日期", key: "end_date", width: 14 },
    { header: "范围", key: "scope", width: 16 },
    { header: "可用状态", key: "availability", width: 16 },
    { header: "页码范围", key: "page_ranges", width: 20 },
    { header: "页码标签", key: "page_range_labels", width: 24 },
    { header: "结果数", key: "result_count", width: 12 },
    { header: "总数", key: "total_count", width: 12 },
    { header: "缓存状态", key: "cache_status", width: 16 },
    { header: "报告 ID", key: "report_id", width: 28 },
    { header: "报告标题", key: "report_title", width: 48 },
    { header: "父报告 ID", key: "parent_report_id", width: 28 },
    { header: "推荐位置", key: "placement", width: 22 },
    { header: "对象", key: "target", width: 32 },
    { header: "动作", key: "action", width: 18 },
    { header: "状态", key: "status", width: 18 },
    { header: "耗时（ms）", key: "duration_ms", width: 14 },
    { header: "错误", key: "error", width: 36 },
    { header: "来源页", key: "referrer", width: 42 },
    { header: "来源域名", key: "referrer_host", width: 28 },
    { header: "UTM Source", key: "utm_source", width: 22 },
    { header: "UTM Medium", key: "utm_medium", width: 22 },
    { header: "UTM Campaign", key: "utm_campaign", width: 30 },
    { header: "UTM Term", key: "utm_term", width: 26 },
    { header: "UTM Content", key: "utm_content", width: 26 },
    { header: "设备", key: "device_type", width: 14 },
    { header: "机器人提示", key: "bot_hint", width: 18 },
    { header: "Bot Score", key: "bot_score", width: 12 },
    { header: "Verified Bot", key: "verified_bot", width: 14 },
    { header: "语言", key: "language", width: 14 },
    { header: "屏幕", key: "screen", width: 14 },
    { header: "导航类型", key: "navigation_type", width: 16 },
    { header: "User-Agent", key: "user_agent", width: 54 },
    { header: "事件 ID", key: "id", width: 38 },
  ];

  function analyticsHistoryExportRow(event) {
    const value = event && typeof event === "object" ? event : {};
    const user = value.user && typeof value.user === "object" ? value.user : {};
    return {
      ts: value.ts || "",
      date: value.date || "",
      event_label: analyticsEventLabel(value.type),
      type: value.type || "",
      username: user.username || "",
      email: user.email || "",
      role: user.role || "",
      visitor_id: value.visitor_id || "",
      session_id: value.session_id || "",
      session_started_at: value.session_started_at || "",
      first_seen_at: value.first_seen_at || "",
      is_returning: Boolean(value.is_returning),
      landing_path: value.landing_path || "",
      ip_hash: value.ip_hash || "",
      country: value.country || "",
      colo: value.colo || "",
      page: value.page || "",
      path: value.path || "",
      source: value.source || "",
      query: value.query || "",
      institution: value.institution || "",
      industry: value.industry || "",
      start_date: value.start_date || "",
      end_date: value.end_date || "",
      scope: value.scope || "",
      availability: value.availability || "",
      page_ranges: value.page_ranges || "",
      page_range_labels: value.page_range_labels || "",
      result_count: value.result_count || 0,
      total_count: value.total_count || 0,
      cache_status: value.cache_status || "",
      report_id: value.report_id || "",
      report_title: value.report_title || "",
      parent_report_id: value.parent_report_id || "",
      placement: value.placement || "",
      target: value.target || "",
      action: value.action || "",
      status: value.status || "",
      duration_ms: value.duration_ms || 0,
      error: value.error || "",
      referrer: value.referrer || "",
      referrer_host: value.referrer_host || "",
      utm_source: value.utm_source || "",
      utm_medium: value.utm_medium || "",
      utm_campaign: value.utm_campaign || "",
      utm_term: value.utm_term || "",
      utm_content: value.utm_content || "",
      device_type: value.device_type || "",
      bot_hint: value.bot_hint || "",
      bot_score: value.bot_score || 0,
      verified_bot: Boolean(value.verified_bot),
      language: value.language || "",
      screen: value.screen || "",
      navigation_type: value.navigation_type || "",
      user_agent: value.user_agent || "",
      id: value.id || "",
    };
  }

  function analyticsHistoryExportFilename() {
    const now = new Date();
    const pad = (value) => String(value).padStart(2, "0");
    return `${PUBLIC_BRAND}-activity-history-${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}-${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}.xlsx`;
  }

  async function collectAnalyticsHistoryPages(fetchPage, options = {}) {
    if (typeof fetchPage !== "function") throw new TypeError("fetchPage must be a function");
    const requestedMaxPages = Number(options.maxPages);
    const requestedMaxRows = Number(options.maxRows);
    const maxPages = Number.isFinite(requestedMaxPages) && requestedMaxPages > 0
      ? Math.floor(requestedMaxPages)
      : ANALYTICS_HISTORY_EXPORT_MAX_PAGES;
    const maxRows = Number.isFinite(requestedMaxRows) && requestedMaxRows > 0
      ? Math.floor(requestedMaxRows)
      : ANALYTICS_HISTORY_EXPORT_MAX_ROWS;
    const requestedMaxAttempts = Number(options.maxAttemptsPerPage);
    const maxAttemptsPerPage = Number.isFinite(requestedMaxAttempts) && requestedMaxAttempts > 0
      ? Math.floor(requestedMaxAttempts)
      : 1;
    const requestedRetryDelayMs = Number(options.retryDelayMs);
    const retryDelayMs = Number.isFinite(requestedRetryDelayMs) && requestedRetryDelayMs >= 0
      ? requestedRetryDelayMs
      : 800;
    const onProgress = typeof options.onProgress === "function" ? options.onProgress : () => {};
    const onPageStart = typeof options.onPageStart === "function" ? options.onPageStart : () => {};
    const onRetry = typeof options.onRetry === "function" ? options.onRetry : () => {};
    const sleep = typeof options.sleep === "function"
      ? options.sleep
      : (delay) => new Promise((resolve) => setTimeout(resolve, delay));
    const events = [];
    const seenEventIds = new Set();
    const requestedCursors = new Set();
    let cursor = "";
    let pageCount = 0;
    let scannedCount = 0;
    let duplicateCount = 0;
    let skippedCount = 0;

    while (true) {
      if (pageCount >= maxPages) {
        throw new Error(`导出已读取 ${maxPages} 批仍未结束，请联系管理员检查存档数量或分页状态。`);
      }
      if (requestedCursors.has(cursor)) {
        throw new Error("历史分页游标发生循环，导出已停止以避免生成不完整文件。");
      }
      requestedCursors.add(cursor);

      let data;
      let attempt = 0;
      while (attempt < maxAttemptsPerPage) {
        attempt += 1;
        onPageStart({
          pageNumber: pageCount + 1,
          attempt,
          maxAttempts: maxAttemptsPerPage,
          eventCount: events.length,
          scannedCount,
        });
        try {
          data = await fetchPage(cursor, pageCount + 1, attempt);
          break;
        } catch (error) {
          const statusCode = Number(error && error.status);
          const retryable = Boolean(error && error.retryable === true)
            || statusCode === 408
            || statusCode === 425
            || statusCode === 429
            || statusCode >= 500;
          if (!retryable || attempt >= maxAttemptsPerPage) throw error;
          const delayMs = retryDelayMs * (2 ** (attempt - 1));
          onRetry({
            pageNumber: pageCount + 1,
            attempt,
            nextAttempt: attempt + 1,
            maxAttempts: maxAttemptsPerPage,
            delayMs,
            status: statusCode || 0,
            eventCount: events.length,
            scannedCount,
            error,
          });
          await sleep(delayMs);
        }
      }
      if (!data || typeof data !== "object" || !Array.isArray(data.events)) {
        throw new Error("历史接口返回的数据格式不完整。");
      }
      pageCount += 1;
      const pageScannedCount = Number(data.scanned_count);
      if (Number.isFinite(pageScannedCount) && pageScannedCount > 0) scannedCount += pageScannedCount;
      const pageSkippedCount = Number(data.skipped_count);
      if (Number.isFinite(pageSkippedCount) && pageSkippedCount > 0) skippedCount += pageSkippedCount;

      for (const event of data.events) {
        const eventId = String(event && event.id || "").trim();
        if (eventId && seenEventIds.has(eventId)) {
          duplicateCount += 1;
          continue;
        }
        if (events.length >= maxRows) {
          throw new Error(`匹配记录超过 Excel 的 ${maxRows} 条上限，无法生成完整文件。`);
        }
        if (eventId) seenEventIds.add(eventId);
        events.push(event);
      }

      const nextCursor = String(data.next_cursor || "");
      if (data.has_more === true && !nextCursor) {
        throw new Error("历史接口提示还有记录，但没有返回下一页游标。");
      }
      if (data.has_more === false && nextCursor) {
        throw new Error("历史接口分页状态不一致，导出已停止。");
      }
      onProgress({
        pageCount,
        eventCount: events.length,
        scannedCount,
        duplicateCount,
        skippedCount,
        hasMore: Boolean(nextCursor),
      });
      if (!nextCursor) break;
      if (requestedCursors.has(nextCursor)) {
        throw new Error("历史分页游标发生循环，导出已停止以避免生成不完整文件。");
      }
      cursor = nextCursor;
    }

    return { events, pageCount, scannedCount, duplicateCount, skippedCount };
  }

  function analyticsHistoryExportResponseError(response, responseText, payload = {}) {
    const rawDetail = String(payload && payload.detail || responseText || "")
      .replace(/<[^>]*>/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 240);
    const status = Number(response && response.status) || 0;
    const statusText = String(response && response.statusText || "").trim();
    const ray = response && response.headers && typeof response.headers.get === "function"
      ? String(response.headers.get("cf-ray") || "").trim()
      : "";
    const diagnostic = rawDetail || statusText;
    const suffix = [diagnostic, ray ? `CF-Ray ${ray}` : ""].filter(Boolean).join("；");
    const error = new Error(`历史记录导出失败${status ? ` (${status})` : ""}${suffix ? `：${suffix}` : "。"}`);
    error.status = status;
    error.retryable = status === 0
      || status === 408
      || status === 425
      || status === 429
      || status >= 500;
    return error;
  }

  function analyticsHistoryFilterSnapshot(fields = {}) {
    const valueOf = (name) => String(fields[name] && fields[name].value || "").trim();
    const requestedPageSize = Math.floor(Number(valueOf("pageSize")) || 100);
    return {
      type: valueOf("type"),
      user: valueOf("user"),
      query: valueOf("query"),
      startDate: valueOf("startDate"),
      endDate: valueOf("endDate"),
      pageSize: Math.min(200, Math.max(1, requestedPageSize)),
    };
  }

  function analyticsHistoryFilterKey(filters = {}) {
    return [
      filters.type,
      filters.user,
      filters.query,
      filters.startDate,
      filters.endDate,
      filters.pageSize,
    ].map((value) => String(value || "")).join("\u001f");
  }

  function analyticsHistorySearchParams(filters = {}, options = {}) {
    const params = new URLSearchParams();
    if (filters.type) params.set("type", filters.type);
    if (filters.user) params.set("user", filters.user);
    if (filters.query) params.set("q", filters.query);
    if (filters.startDate) params.set("start_date", filters.startDate);
    if (filters.endDate) params.set("end_date", filters.endDate);
    const requestedPageSize = Math.floor(Number(options.pageSize) || Number(filters.pageSize) || 100);
    params.set("page_size", String(Math.min(200, Math.max(1, requestedPageSize))));
    const requestedCursor = String(options.cursor || "");
    if (requestedCursor) params.set("cursor", requestedCursor);
    return params;
  }

  const ANALYTICS_HISTORY_AUTO_SCAN_BATCH_LIMIT = 4;

  function shouldContinueAnalyticsHistoryAutoScan(options = {}) {
    if (!options.autoScan || !options.nextCursor) return false;
    if (Number(options.eventCount) > 0) return false;
    return Number(options.batchCount) < ANALYTICS_HISTORY_AUTO_SCAN_BATCH_LIMIT;
  }

  async function loadAnalyticsHistoryUserOptions(workerUrl, input, datalist) {
    if (!input || !datalist) return 0;
    const data = await fetchFreshAdminUsers(workerUrl);
    const users = Array.isArray(data.users) ? data.users : [];
    const values = new Map();
    for (const user of users) {
      const username = String(user && user.username || "").trim();
      const email = String(user && user.email || "").trim();
      const state = user && user.disabled ? "已禁用" : "正常";
      if (username && !values.has(username.toLowerCase())) {
        values.set(username.toLowerCase(), {
          value: username,
          label: email ? `${email} · ${state}` : state,
        });
      }
      if (email && !values.has(email.toLowerCase())) {
        values.set(email.toLowerCase(), {
          value: email,
          label: username ? `${username} · ${state}` : state,
        });
      }
    }
    const fragment = document.createDocumentFragment();
    [...values.values()]
      .sort((a, b) => a.value.localeCompare(b.value, "zh-CN", { sensitivity: "base" }))
      .forEach((entry) => {
        const option = document.createElement("option");
        option.value = entry.value;
        option.label = entry.label;
        fragment.appendChild(option);
      });
    datalist.replaceChildren(fragment);
    input.placeholder = `用户名或邮箱（${users.length} 个用户）`;
    return users.length;
  }

  function analyticsDaySummaryList(title, rows) {
    const items = Array.isArray(rows) ? rows : [];
    return `
      <section class="analytics-day-summary-list">
        <h3>${escapeHtml(title)}</h3>
        ${items.length
          ? `<ol>${items.map((row) => `<li><span>${escapeHtml(row.label || "unknown")}</span><strong>${Number(row.count || 0).toLocaleString("zh-CN")}</strong></li>`).join("")}</ol>`
          : '<p class="subtle">暂无数据</p>'}
      </section>
    `;
  }

  function renderAnalyticsAcquisitionLandings(rows) {
    const items = Array.isArray(rows) ? rows : [];
    if (!items.length) return '<p class="subtle">暂无可归因的首次落地会话。</p>';
    return `
      <div class="account-admin-table-wrap">
        <table class="account-admin-table analytics-history-table">
          <thead>
            <tr>
              <th>流量来源</th>
              <th>具体落地内容</th>
              <th>内容类型 / ID</th>
              <th>UTM</th>
              <th>会话</th>
            </tr>
          </thead>
          <tbody>
            ${items.map((row) => {
              const utm = [row.utm_medium, row.utm_campaign, row.utm_term, row.utm_content].filter(Boolean).join(" · ");
              return `
                <tr>
                  <td><strong>${escapeHtml(row.source || "direct / unknown")}</strong></td>
                  <td><strong>${escapeHtml(row.report_title || row.landing_path || "/")}</strong><small>${escapeHtml(row.landing_path || "/")}</small></td>
                  <td>${escapeHtml([row.page, row.report_id].filter(Boolean).join(" · ") || "-")}</td>
                  <td>${escapeHtml(utm || "-")}</td>
                  <td><strong>${Number(row.sessions || 0).toLocaleString("zh-CN")}</strong></td>
                </tr>
              `;
            }).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function renderAnalyticsDaySummary(target, data) {
    if (!target) return;
    const metrics = [
      ["唯一访客", data.unique_visitor_count],
      ["事件", data.event_count],
      ["页面访问", data.page_view_count],
      ["会话", data.unique_session_count],
    ];
    target.innerHTML = `
      <div class="analytics-day-summary-metrics">
        ${metrics.map(([label, value]) => `<div><span>${escapeHtml(label)}</span><strong>${Number(value || 0).toLocaleString("zh-CN")}</strong></div>`).join("")}
      </div>
      <section>
        <h3>来源 × 具体落地报告 / Blog</h3>
        <p class="subtle">按会话首次页面访问去重，表内展示会话数最多的前 50 种来源 × 落地组合；完整长尾可导出事件明细。Google/Bing 的外部搜索词需结合各自站长平台，UTM Term 仅在来源主动传递时显示。</p>
        ${data.acquisition_truncated ? '<p class="status-line">当日来源组合超过汇总上限；请导出完整事件明细查看其余记录。</p>' : ""}
        ${renderAnalyticsAcquisitionLandings(data.acquisition_landings)}
      </section>
      <div class="analytics-day-summary-lists">
        ${analyticsDaySummaryList("热门路径", data.top_paths)}
        ${analyticsDaySummaryList("来源域名（事件）", data.top_referrer_hosts)}
        ${analyticsDaySummaryList("国家/地区", data.countries)}
        ${analyticsDaySummaryList("设备", data.devices)}
        ${analyticsDaySummaryList("机器人提示", data.bot_hints)}
        ${analyticsDaySummaryList("UTM 来源（事件）", data.utm_sources)}
      </div>
    `;
  }

  async function initAnalyticsHistory() {
    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);

    const form = document.getElementById("analyticsHistoryFilters");
    const type = document.getElementById("analyticsHistoryType");
    const userFilter = document.getElementById("analyticsHistoryUser");
    const userOptions = document.getElementById("analyticsHistoryUserOptions");
    const query = document.getElementById("analyticsHistoryQuery");
    const startDate = document.getElementById("analyticsHistoryStartDate");
    const endDate = document.getElementById("analyticsHistoryEndDate");
    const pageSize = document.getElementById("analyticsHistoryPageSize");
    const reset = document.getElementById("analyticsHistoryReset");
    const refresh = document.getElementById("analyticsHistoryRefresh");
    const exportAll = document.getElementById("analyticsHistoryExportAll");
    const status = document.getElementById("analyticsHistoryStatus");
    const meta = document.getElementById("analyticsHistoryMeta");
    const results = document.getElementById("analyticsHistoryResults");
    const previous = document.getElementById("analyticsHistoryPrev");
    const next = document.getElementById("analyticsHistoryNext");
    const pageLabel = document.getElementById("analyticsHistoryPage");
    const coverage = document.getElementById("analyticsHistoryCoverage");
    const daySummaryDate = document.getElementById("analyticsDaySummaryDate");
    const daySummaryLoad = document.getElementById("analyticsDaySummaryLoad");
    const daySummaryRefresh = document.getElementById("analyticsDaySummaryRefresh");
    const daySummaryStatus = document.getElementById("analyticsDaySummaryStatus");
    const daySummaryResults = document.getElementById("analyticsDaySummaryResults");
    let cursor = "";
    let cursorStack = [];
    let nextCursor = "";
    let pageNumber = 1;
    let exportInProgress = false;
    let pageLoadInProgress = false;
    let activeFilters = null;
    let pageLoadSequence = 0;
    let pageLoadController = null;
    let daySummarySequence = 0;

    function setDaySummaryStatus(text, kind = "") {
      if (!daySummaryStatus) return;
      daySummaryStatus.className = kind ? `status-line ${kind}` : "status-line";
      daySummaryStatus.textContent = text || "";
    }

    async function loadDaySummary(options = {}) {
      const date = String(daySummaryDate && daySummaryDate.value || "");
      if (!/^\d{4}-\d{2}-\d{2}$/.test(date)) {
        setDaySummaryStatus("请选择日期。", "error");
        return;
      }
      const sequence = ++daySummarySequence;
      if (daySummaryLoad) daySummaryLoad.disabled = true;
      if (daySummaryRefresh) daySummaryRefresh.disabled = true;
      let jobId = "";
      let pageCount = 0;
      try {
        do {
          const params = new URLSearchParams({ date });
          if (jobId) params.set("job_id", jobId);
          else if (options.refresh) params.set("refresh", "1");
          const response = await fetch(`${workerUrl}/account-admin/analytics-day-summary?${params}`, {
            cache: "no-store",
            headers: authHeaders(),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(data.detail || "按日汇总读取失败。");
          if (sequence !== daySummarySequence) return;
          renderAnalyticsDaySummary(daySummaryResults, data);
          setDaySummaryStatus(data.complete
            ? `${date} 汇总完成，共扫描 ${Number(data.processed_count || 0).toLocaleString("zh-CN")} 条对象。`
            : `正在扫描 ${date}：已处理 ${Number(data.processed_count || 0).toLocaleString("zh-CN")} 条…`, data.complete ? "ok" : "");
          jobId = String(data.job_id || "");
          pageCount += 1;
          if (!data.has_more) break;
          if (!jobId || pageCount >= 500) throw new Error("按日汇总分页未能完成，请重新扫描。");
        } while (sequence === daySummarySequence);
      } catch (error) {
        if (sequence === daySummarySequence) setDaySummaryStatus(error.message || "按日汇总读取失败。", "error");
      } finally {
        if (sequence === daySummarySequence) {
          if (daySummaryLoad) daySummaryLoad.disabled = false;
          if (daySummaryRefresh) daySummaryRefresh.disabled = false;
        }
      }
    }

    if (daySummaryDate && !daySummaryDate.value) {
      daySummaryDate.value = new Date(Date.now() + 8 * 60 * 60 * 1000).toISOString().slice(0, 10);
    }
    if (daySummaryLoad) daySummaryLoad.addEventListener("click", () => loadDaySummary());
    if (daySummaryRefresh) daySummaryRefresh.addEventListener("click", () => loadDaySummary({ refresh: true }));

    function setStatus(message, kind = "") {
      status.className = kind ? `status-line ${kind}` : "status-line";
      status.textContent = message || "";
    }

    function resetPagination() {
      cursor = "";
      cursorStack = [];
      nextCursor = "";
      pageNumber = 1;
    }

    function currentHistoryFilters() {
      return analyticsHistoryFilterSnapshot({
        type,
        user: userFilter,
        query,
        startDate,
        endDate,
        pageSize,
      });
    }

    function historyFiltersChanged() {
      return Boolean(activeFilters)
        && analyticsHistoryFilterKey(currentHistoryFilters()) !== analyticsHistoryFilterKey(activeFilters);
    }

    function updateHistoryNavigation() {
      const unavailable = pageLoadInProgress || exportInProgress || historyFiltersChanged();
      previous.disabled = unavailable || cursorStack.length === 0;
      next.disabled = unavailable || !nextCursor;
    }

    function analyticsHistoryExportParams() {
      return new URLSearchParams({ page_size: String(ANALYTICS_HISTORY_EXPORT_PAGE_SIZE) });
    }

    function renderHistoryMeta(data) {
      const range = data.newest_date || data.oldest_date
        ? `${data.oldest_date || ""} 至 ${data.newest_date || ""}`
        : "暂无存档日期";
      meta.innerHTML = `
        <span>历史范围：<strong>${escapeHtml(range)}</strong></span>
        <span>已存档 ${escapeHtml((data.available_dates || []).length)} 天</span>
        <span>本页 ${escapeHtml((data.events || []).length)} 条</span>
        <span>扫描 ${escapeHtml(data.scanned_count || 0)} 条存档</span>
        <span><strong>${data.has_more ? "还有更早记录" : "已到最早记录"}</strong></span>
        <span>更新 ${escapeHtml(analyticsTime(data.generated_at))}</span>
      `;
      if (coverage) {
        coverage.textContent = data.oldest_date
          ? `原始埋点自 ${data.oldest_date} 开始保存；更早或当时未设置埋点的操作无法补录。记录按时间倒序分页，每页仅显示当前批次。`
          : "当前还没有原始埋点存档。";
      }
    }

    async function loadPage(options = {}) {
      if (exportInProgress) return;
      if (options.reset || !activeFilters) {
        resetPagination();
        activeFilters = currentHistoryFilters();
      }
      const loadFilters = { ...activeFilters };
      const loadCursor = cursor;
      const loadPageNumber = pageNumber;
      const loadSequence = pageLoadSequence + 1;
      pageLoadSequence = loadSequence;
      if (pageLoadController) pageLoadController.abort();
      const controller = typeof AbortController === "function" ? new AbortController() : null;
      pageLoadController = controller;
      pageLoadInProgress = true;
      refresh.disabled = true;
      if (exportAll) exportAll.disabled = true;
      updateHistoryNavigation();
      setStatus(`正在读取第 ${loadPageNumber} 页…`);
      try {
        const targetCount = loadFilters.pageSize;
        const autoScan = Boolean(
          loadFilters.type
          || loadFilters.user
          || loadFilters.query,
        );
        const events = [];
        const seenEventIds = new Set();
        const seenCursors = new Set();
        let requestCursor = loadCursor;
        let scannedCount = 0;
        let batchCount = 0;
        let firstData = null;
        let lastData = null;

        while (true) {
          if (seenCursors.has(requestCursor)) throw new Error("历史查询游标发生循环，已停止读取。");
          if (batchCount >= 1000) throw new Error("历史查询批次过多，已停止以避免返回不完整结果。");
          seenCursors.add(requestCursor);
          const remaining = Math.max(1, targetCount - events.length);
          if (autoScan) {
            setStatus(`正在查找第 ${loadPageNumber} 页：已扫描 ${scannedCount} 条，找到 ${events.length} 条…`);
          }
          const response = await fetch(`${workerUrl}/account-admin/analytics-events?${analyticsHistorySearchParams(loadFilters, {
            cursor: requestCursor,
            pageSize: remaining,
          })}`, {
            cache: "no-store",
            headers: authHeaders(),
            ...(controller ? { signal: controller.signal } : {}),
          });
          if (loadSequence !== pageLoadSequence) return;
          const batchData = await response.json().catch(() => ({}));
          if (loadSequence !== pageLoadSequence) return;
          if (!response.ok) throw new Error(batchData.detail || `历史记录读取失败 (${response.status})。`);
          if (!Array.isArray(batchData.events)) throw new Error("历史接口返回的数据格式不完整。");
          batchCount += 1;
          if (!firstData) firstData = batchData;
          lastData = batchData;
          const batchScanned = Number(batchData.scanned_count);
          if (Number.isFinite(batchScanned) && batchScanned > 0) scannedCount += batchScanned;
          for (const event of batchData.events) {
            const eventId = String(event && event.id || "").trim();
            if (eventId && seenEventIds.has(eventId)) continue;
            if (eventId) seenEventIds.add(eventId);
            events.push(event);
          }
          const batchNextCursor = String(batchData.next_cursor || "");
          if (batchData.has_more === true && !batchNextCursor) {
            throw new Error("历史接口提示还有记录，但没有返回下一页游标。");
          }
          if (!shouldContinueAnalyticsHistoryAutoScan({
            autoScan,
            batchCount,
            eventCount: events.length,
            nextCursor: batchNextCursor,
          })) break;
          requestCursor = batchNextCursor;
        }

        if (loadSequence !== pageLoadSequence) return;

        const data = {
          ...(firstData || {}),
          ...(lastData || {}),
          events,
          scanned_count: scannedCount,
        };
        nextCursor = String(data.next_cursor || "");
        results.innerHTML = renderAnalyticsHistoryEvents(events);
        renderHistoryMeta(data);
        if (!startDate.min && data.oldest_date) {
          startDate.min = data.oldest_date;
          startDate.max = data.newest_date || "";
          endDate.min = data.oldest_date;
          endDate.max = data.newest_date || "";
        }
        pageLabel.textContent = `第 ${loadPageNumber} 页`;
        setStatus(events.length
          ? (nextCursor
            ? `${autoScan ? `已自动扫描 ${scannedCount} 条存档，` : ""}找到 ${events.length} 条事件；还有更早记录。`
            : `${autoScan ? `已自动扫描 ${scannedCount} 条存档，` : ""}找到 ${events.length} 条事件，已到最早记录。`)
          : (nextCursor
            ? `已扫描 ${scannedCount} 条存档，当前页没有匹配事件；可继续查看更早记录。`
            : `已扫描 ${scannedCount} 条存档，全历史没有匹配事件。`), "ok");
      } catch (error) {
        if (loadSequence !== pageLoadSequence || (controller && controller.signal.aborted)) return;
        results.innerHTML = '<div class="empty-state">无法读取用户行为历史。</div>';
        meta.textContent = "";
        setStatus(error.message || "历史记录读取失败。", "error");
      } finally {
        if (loadSequence === pageLoadSequence) {
          pageLoadInProgress = false;
          if (pageLoadController === controller) pageLoadController = null;
          refresh.disabled = false;
          if (exportAll) exportAll.disabled = !isSuperSession();
          updateHistoryNavigation();
        }
      }
    }

    async function exportAllHistory() {
      if (!exportAll || exportInProgress || pageLoadInProgress) return;
      const exportButtonLabel = exportAll.textContent || "导出全部历史";
      exportInProgress = true;
      exportAll.disabled = true;
      exportAll.textContent = "正在准备…";
      refresh.disabled = true;
      updateHistoryNavigation();
      const exportParams = analyticsHistoryExportParams();
      setStatus("正在准备导出全部历史（不受当前页面筛选影响）…");
      try {
        const { buildXlsxWorkbook, downloadXlsx } = await import(versionedSiteAssetUrl("assets/xlsx-export.js"));
        const collected = await collectAnalyticsHistoryPages(async (batchCursor) => {
          const params = new URLSearchParams(exportParams);
          if (batchCursor) params.set("cursor", batchCursor);
          try {
            const response = await fetch(`${workerUrl}/account-admin/analytics-events-export?${params}`, {
              cache: "no-store",
              headers: authHeaders(),
            });
            const responseText = await response.text();
            let data = {};
            if (responseText.trim()) {
              try {
                data = JSON.parse(responseText);
              } catch (_error) {
                if (response.ok) {
                  throw analyticsHistoryExportResponseError(response, responseText, {
                    detail: "历史接口返回了非 JSON 数据。",
                  });
                }
              }
            }
            if (!response.ok) {
              throw analyticsHistoryExportResponseError(response, responseText, data);
            }
            return data;
          } catch (error) {
            if (!Number(error && error.status)) error.retryable = true;
            throw error;
          }
        }, {
          maxAttemptsPerPage: 4,
          retryDelayMs: 800,
          onPageStart(progress) {
            exportAll.textContent = `导出中 · ${progress.eventCount} 条`;
            if (progress.attempt === 1) {
              setStatus(`正在请求第 ${progress.pageNumber} 批；已保留 ${progress.eventCount} 条…`);
            }
          },
          onRetry(progress) {
            const reason = progress.status ? `HTTP ${progress.status}` : "网络中断";
            const seconds = Math.max(0.1, progress.delayMs / 1000).toFixed(1);
            setStatus(`第 ${progress.pageNumber} 批遇到 ${reason}，${seconds} 秒后进行第 ${progress.nextAttempt}/${progress.maxAttempts} 次尝试；已保留 ${progress.eventCount} 条。`);
          },
          onProgress(progress) {
            exportAll.textContent = `导出中 · ${progress.eventCount} 条`;
            const skippedNote = progress.skippedCount
              ? `，跳过 ${progress.skippedCount} 次主备均不可读的存档读取`
              : "";
            setStatus(`已完成 ${progress.pageCount} 批：收集 ${progress.eventCount} 条，扫描 ${progress.scannedCount} 条存档${skippedNote}；正在继续…`);
          },
        });
        exportAll.textContent = "正在生成 Excel…";
        setStatus(`数据读取完成，共 ${collected.events.length} 条；正在生成 Excel…`);
        const rows = [...collected.events]
          .sort((a, b) => String(b && b.ts || "").localeCompare(String(a && a.ts || "")))
          .map(analyticsHistoryExportRow);
        const blob = buildXlsxWorkbook({
          sheetName: "用户行为历史",
          columns: ANALYTICS_HISTORY_EXPORT_COLUMNS,
          rows,
        });
        downloadXlsx(blob, analyticsHistoryExportFilename());
        const duplicateNote = collected.duplicateCount
          ? `；已去除 ${collected.duplicateCount} 条重复事件`
          : "";
        const skippedNote = collected.skippedCount
          ? `；已跳过 ${collected.skippedCount} 次主备均不可读的存档读取`
          : "";
        setStatus(`Excel 已导出：全部历史共 ${rows.length} 条事件，读取 ${collected.pageCount} 批${duplicateNote}${skippedNote}。`, "ok");
      } catch (error) {
        setStatus(error.message || "全部历史导出失败。", "error");
      } finally {
        exportInProgress = false;
        exportAll.textContent = exportButtonLabel;
        exportAll.disabled = !isSuperSession();
        refresh.disabled = false;
        updateHistoryNavigation();
      }
    }

    form.addEventListener("submit", (event) => {
      event.preventDefault();
      loadPage({ reset: true });
    });
    form.addEventListener("input", updateHistoryNavigation);
    reset.addEventListener("click", () => {
      form.reset();
      loadPage({ reset: true });
    });
    refresh.addEventListener("click", () => loadPage({ reset: historyFiltersChanged() }));
    if (exportAll) exportAll.addEventListener("click", exportAllHistory);
    previous.addEventListener("click", () => {
      if (pageLoadInProgress || exportInProgress || !cursorStack.length || historyFiltersChanged()) return;
      cursor = cursorStack.pop() || "";
      pageNumber = Math.max(1, pageNumber - 1);
      loadPage();
    });
    next.addEventListener("click", () => {
      if (pageLoadInProgress || exportInProgress || !nextCursor || historyFiltersChanged()) return;
      cursorStack.push(cursor);
      cursor = nextCursor;
      pageNumber += 1;
      loadPage();
    });

    if (!isSuperSession()) {
      if (exportAll) exportAll.disabled = true;
      results.innerHTML = '<div class="empty-state">请先使用管理员账号登录。</div>';
      setStatus("当前账号没有查看用户行为历史的权限。", "error");
      return;
    }
    if (userFilter && userOptions) {
      loadAnalyticsHistoryUserOptions(workerUrl, userFilter, userOptions).catch(() => {
        userFilter.placeholder = "用户名或邮箱（可直接输入）";
      });
    }
    await loadPage({ reset: true });
  }

  function resetDownloadProgress(progress) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    if (bar) bar.style.width = "0%";
    if (text) text.textContent = "等待下载…";
    progress.hidden = true;
  }

  function setDownloadProgress(progress, loaded, total) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    progress.hidden = false;
    if (total > 0) {
      const percent = Math.min(100, Math.round((loaded / total) * 100));
      if (bar) bar.style.width = `${percent}%`;
      if (text) text.textContent = `${percent}% · ${formatSize(loaded)} / ${formatSize(total)}`;
    } else {
      if (bar) bar.style.width = "35%";
      if (text) text.textContent = `已下载 ${formatSize(loaded)}`;
    }
  }

  async function responseBlobWithProgress(response, progress) {
    const total = Number(response.headers.get("Content-Length") || 0);
    if (!response.body || !response.body.getReader) {
      const blob = await response.blob();
      setDownloadProgress(progress, blob.size || total, blob.size || total);
      return blob;
    }
    const reader = response.body.getReader();
    const chunks = [];
    let loaded = 0;
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
      loaded += value.byteLength || value.length || 0;
      setDownloadProgress(progress, loaded, total);
    }
    setDownloadProgress(progress, loaded, total || loaded);
    return new Blob(chunks, { type: response.headers.get("Content-Type") || "application/octet-stream" });
  }

  function contentRangeTotal(value) {
    const match = String(value || "").match(/^bytes\s+\d+-\d+\/(\d+)$/i);
    return match ? Number(match[1]) : 0;
  }

  function shouldUseSegmentedDownload(button) {
    const name = String(button && button.dataset.name || "");
    const size = Number(button && button.dataset.sizeBytes || 0) || 0;
    if (/\.mp4$/i.test(name)) return true;
    return size > 5 * 1024 * 1024 && /\.(mp4|pdf|zip)$/i.test(name);
  }

  function isVideoDownloadButton(button) {
    return /\.mp4$/i.test(String(button && button.dataset.name || ""));
  }

  function setDownloadMessage(progress, message, percent = 12) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    progress.hidden = false;
    if (bar) bar.style.width = `${Math.max(0, Math.min(100, percent))}%`;
    if (text) text.textContent = message || "";
  }

  function adminActionButtons(button) {
    const actions = button && button.closest(".account-admin-file-actions");
    return actions ? Array.from(actions.querySelectorAll("button")) : [];
  }

  function cancelActiveAdminButton(button) {
    const active = activeAdminButtonActions.get(button);
    if (!active) return false;
    active.controller.abort();
    return true;
  }

  function startAdminButtonAction(button, controller) {
    if (!button || !controller) return;
    if (!button.dataset.idleLabel) button.dataset.idleLabel = button.textContent.trim() || "下载";
    activeAdminButtonActions.set(button, { controller });
    adminActionButtons(button).forEach((other) => {
      other.disabled = other !== button;
    });
    button.disabled = false;
    button.classList.add("is-cancel");
    button.textContent = "取消";
  }

  function finishAdminButtonAction(button, label = "", restoreDelayMs = 0) {
    if (!button) return;
    activeAdminButtonActions.delete(button);
    adminActionButtons(button).forEach((other) => {
      other.disabled = false;
    });
    button.classList.remove("is-cancel");
    const idle = button.dataset.idleLabel || "下载";
    button.textContent = label || idle;
    if (label && restoreDelayMs > 0) {
      window.setTimeout(() => {
        if (!activeAdminButtonActions.has(button)) button.textContent = idle;
      }, restoreDelayMs);
    }
  }

  function withDownloadToken(endpoint) {
    const session = loadAuthSession();
    const url = new URL(endpoint, window.location.href);
    if (session && session.token) url.searchParams.set("download_token", session.token);
    return url.toString();
  }

  function triggerNativeDownload(url, fallbackName) {
    const link = document.createElement("a");
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.download = fallbackName || "download";
    document.body.appendChild(link);
    link.click();
    link.remove();
  }

  function timeoutSignal(parentSignal, ms) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), ms);
    const cleanup = () => clearTimeout(timer);
    controller.signal.addEventListener("abort", cleanup, { once: true });
    if (parentSignal) {
      if (parentSignal.aborted) controller.abort();
      else parentSignal.addEventListener("abort", () => controller.abort(), { once: true });
    }
    return controller.signal;
  }

  async function fetchRangeBlob(endpoint, start, end, signal) {
    const response = await fetch(endpoint, {
      headers: {
        ...authHeaders(),
        "Range": `bytes=${start}-${end}`,
      },
      signal,
    });
    if (response.status !== 206) {
      if (response.ok && start === 0) return { response, blob: await response.blob(), total: Number(response.headers.get("Content-Length") || 0), full: true };
      const data = await response.json().catch(() => ({}));
      throw new Error(data.detail || `分段下载失败 (${response.status})。`);
    }
    return {
      response,
      blob: await response.blob(),
      total: contentRangeTotal(response.headers.get("Content-Range")),
      full: false,
    };
  }

  async function segmentedAdminDownload(endpoint, fallbackName, progress, signal, options = {}) {
    const chunkSize = options.chunkSize || 4 * 1024 * 1024;
    const concurrency = options.concurrency || 4;
    const firstSignal = options.firstChunkTimeoutMs ? timeoutSignal(signal, options.firstChunkTimeoutMs) : signal;
    const first = await fetchRangeBlob(endpoint, 0, chunkSize - 1, firstSignal);
    if (first.full) {
      setDownloadProgress(progress, first.blob.size, first.total || first.blob.size);
      return first.blob;
    }
    const total = first.total;
    if (!total || total <= first.blob.size) {
      setDownloadProgress(progress, first.blob.size, first.blob.size || total);
      return first.blob;
    }
    const chunks = [];
    chunks[0] = first.blob;
    let loaded = first.blob.size;
    setDownloadProgress(progress, loaded, total);
    const ranges = [];
    for (let start = chunkSize; start < total; start += chunkSize) {
      ranges.push([start, Math.min(total - 1, start + chunkSize - 1), ranges.length + 1]);
    }
    let cursor = 0;
    async function worker() {
      while (cursor < ranges.length) {
        const [start, end, index] = ranges[cursor];
        cursor += 1;
        const part = await fetchRangeBlob(endpoint, start, end, signal);
        chunks[index] = part.blob;
        loaded += part.blob.size;
        setDownloadProgress(progress, loaded, total);
      }
    }
    await Promise.all(Array.from({ length: Math.min(concurrency, ranges.length) }, () => worker()));
    setDownloadProgress(progress, total, total);
    return new Blob(chunks, { type: first.response.headers.get("Content-Type") || contentTypeFromFilename(fallbackName) });
  }

  async function prepareSegmentedAdminDownload(workerUrl, button, signal, progress, options = {}) {
    const kind = String(button && button.dataset.kind || "");
    if (kind !== "file" && kind !== "artifact") return;
    const key = button.dataset.key || "";
    const repo = button.dataset.repo || "";
    const name = button.dataset.name || "download";
    const url = new URL(`${workerUrl}/account-admin/prepare-github-download`);
    url.searchParams.set("kind", kind);
    if (kind === "artifact") {
      url.searchParams.set("id", key);
      url.searchParams.set("name", name);
    } else {
      url.searchParams.set("path", key);
      if (repo) url.searchParams.set("repo", repo);
    }
    setDownloadProgress(progress, 1, 100);
    const response = await fetch(url.toString(), {
      cache: "no-store",
      headers: authHeaders(),
      signal: timeoutSignal(signal, options.timeoutMs || 25000),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !data.ok) {
      throw new Error(data.detail || "文件缓存准备失败，请稍后重试。");
    }
    setDownloadProgress(progress, 100, 100);
    return data;
  }

  function contentTypeFromFilename(name) {
    if (/\.mp4$/i.test(name)) return "video/mp4";
    if (/\.pdf$/i.test(name)) return "application/pdf";
    return "application/octet-stream";
  }

  function accountAdminReportEndpoint(workerUrl, id) {
    return `${workerUrl}/account-admin/report-pdf?id=${encodeURIComponent(id)}`;
  }

  async function fetchAccountAdminReportBlob(workerUrl, pick, progress, signal) {
    const response = await fetch(accountAdminReportEndpoint(workerUrl, pick.id), {
      headers: authHeaders(),
      signal,
    });
    if (!response.ok) {
      const data = await response.json().catch(() => ({}));
      throw new Error(data.detail || `报告读取失败 (${response.status})。`);
    }
    return responseBlobWithProgress(response, progress);
  }

  async function loadPdfJs() {
    if (!pdfJsLoadPromise) {
      pdfJsLoadPromise = import(PDFJS_MODULE_URL).then((pdfjs) => {
        pdfjs.GlobalWorkerOptions.workerSrc = PDFJS_WORKER_URL;
        return pdfjs;
      });
    }
    return pdfJsLoadPromise;
  }

  function downloadDataUrl(dataUrl, filename) {
    const link = document.createElement("a");
    link.href = dataUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
  }

  function imageFilenameForPick(pick) {
    const base = String(pick.display_title || pick.title_zh || pick.title || pick.id || "report")
      .replace(/[\r\n"\\/:*?<>|]+/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 120);
    return `${base || "report"}-page-1.png`;
  }

  async function saveFirstPageImageFromPdfBlob(blob, pick) {
    const pdfjs = await loadPdfJs();
    const data = new Uint8Array(await blob.arrayBuffer());
    const pdf = await pdfjs.getDocument({ data }).promise;
    const page = await pdf.getPage(1);
    const baseViewport = page.getViewport({ scale: 1 });
    const scale = Math.min(2.4, Math.max(1.2, 1600 / Math.max(baseViewport.width, baseViewport.height)));
    const viewport = page.getViewport({ scale });
    const canvas = document.createElement("canvas");
    canvas.width = Math.ceil(viewport.width);
    canvas.height = Math.ceil(viewport.height);
    const context = canvas.getContext("2d", { alpha: false });
    if (!context) throw new Error("浏览器无法创建图片画布。");
    await page.render({ canvasContext: context, viewport }).promise;
    downloadDataUrl(canvas.toDataURL("image/png"), imageFilenameForPick(pick));
    if (pdf && typeof pdf.destroy === "function") pdf.destroy();
  }

  function formatAdminDateTime(value) {
    const date = new Date(String(value || ""));
    if (!Number.isFinite(date.getTime())) return "";
    try {
      return new Intl.DateTimeFormat("zh-CN", {
        timeZone: "Asia/Shanghai",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false,
      }).format(date).replaceAll("/", "-");
    } catch (_error) {
      return String(value || "").replace("T", " ").slice(0, 19);
    }
  }

  function shanghaiDateInputValue(value = new Date()) {
    const date = value instanceof Date ? value : new Date(value);
    if (!Number.isFinite(date.getTime())) return "";
    try {
      const parts = new Intl.DateTimeFormat("en", {
        timeZone: "Asia/Shanghai",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
      }).formatToParts(date);
      const values = Object.fromEntries(parts.map((part) => [part.type, part.value]));
      return `${values.year}-${values.month}-${values.day}`;
    } catch (_error) {
      return date.toISOString().slice(0, 10);
    }
  }

  function mergeAccountAdminSummaryWithLast(data) {
    if (!accountAdminLastSummary) return data;
    const merged = { ...data, module_status: { ...(data.module_status || {}) } };
    const modules = [
      ["files", ["files"]],
      ["picks", ["daily_picks", "access_options"]],
      ["wechat", ["wechat_schedule"]],
      ["analytics", ["analytics"]],
      ["users", ["users"]],
    ];
    for (const [moduleName, fields] of modules) {
      const status = merged.module_status[moduleName];
      if (!status || status.has_data !== false) continue;
      for (const field of fields) {
        if (Object.prototype.hasOwnProperty.call(accountAdminLastSummary, field)) {
          merged[field] = accountAdminLastSummary[field];
        }
      }
      const previousStatus = accountAdminLastSummary.module_status && accountAdminLastSummary.module_status[moduleName];
      merged.module_status[moduleName] = {
        ...(previousStatus || {}),
        ...status,
        has_data: true,
        state: "updating",
        updated_at: previousStatus && previousStatus.updated_at || "",
      };
    }
    return merged;
  }

  function renderAdminModuleNotice(target, status) {
    if (!target) return;
    const state = String(status && status.state || "fresh");
    if (state === "fresh") {
      target.hidden = true;
      target.textContent = "";
      return;
    }
    const updated = formatAdminDateTime(status && status.updated_at);
    target.hidden = false;
    target.textContent = status && status.has_data
      ? `数据更新中，当前显示最近一次成功数据${updated ? `（北京时间 ${updated}）` : ""}。系统每 30 分钟自动刷新。`
      : "数据正在首次同步，请约半小时后重新进入。";
  }

  function renderAccountAdminSummary(data, targets) {
    const users = Array.isArray(data.users) ? data.users : [];
    const files = Array.isArray(data.files) ? data.files : [];
    const dailyPicks = Array.isArray(data.daily_picks) ? data.daily_picks : [];
    const wechatSchedule = data.wechat_schedule && typeof data.wechat_schedule === "object" ? data.wechat_schedule : {};
    const analytics = data.analytics && typeof data.analytics === "object" ? data.analytics : null;
    const moduleStatus = data.module_status && typeof data.module_status === "object" ? data.module_status : {};
    accountAdminUsersByEmail = new Map(users.map((user) => [String(user.email || ""), user]));
    if (data.access_options && typeof data.access_options === "object") accountAdminAccessOptions = data.access_options;
    const canViewUsers = data.can_view_users !== false;
    const canViewWechat = data.can_view_wechat !== false;
    const canViewAnalytics = data.can_view_analytics !== false;
    if (targets.title && data.dashboard_title) targets.title.textContent = data.dashboard_title;
    if (targets.usersSection) targets.usersSection.hidden = !canViewUsers;
    if (targets.wechatSection) targets.wechatSection.hidden = !canViewWechat;
    if (targets.analyticsSection) targets.analyticsSection.hidden = !canViewAnalytics;
    accountAdminDailyPicks = new Map(dailyPicks.map((pick) => [String(pick.id || ""), pick]));
    targets.pickCount.textContent = dailyPicks.length ? `${dailyPicks.length} reports` : "";
    targets.picks.innerHTML = dailyPicks.length
      ? dailyPicks.map(adminDailyPickRow).join("")
      : `<div class="empty-state">数据正在同步，请约半小时后重新进入。</div>`;
    renderAdminModuleNotice(targets.picksNotice, moduleStatus.picks);
    if (canViewWechat && targets.wechatCount && targets.wechatSchedule) {
      targets.wechatCount.textContent = wechatSchedule.total_batches ? `${wechatSchedule.total_batches} batches` : "";
      targets.wechatSchedule.innerHTML = renderAdminWechatSchedule(wechatSchedule);
      renderAdminModuleNotice(targets.wechatNotice, moduleStatus.wechat);
    }
    if (canViewUsers && targets.userCount && targets.users) {
      renderAdminUserTable(targets);
      renderAdminModuleNotice(targets.usersNotice, moduleStatus.users);
    }
    if (canViewAnalytics && targets.analytics && targets.analyticsCount) {
      targets.analyticsCount.textContent = analytics
        ? `近 ${analytics.range_days || 7} 天窗口 · ${analytics.sample_event_count || analytics.event_count || 0} 条事件抽样`
        : "";
      targets.analytics.innerHTML = analytics
        ? renderAccountAdminAnalytics(analytics)
        : `<div class="empty-state">数据正在同步，请约半小时后重新进入。</div>`;
      renderAdminModuleNotice(targets.analyticsNotice, moduleStatus.analytics);
    }
    targets.files.innerHTML = files.length
      ? files.map(adminFileRow).join("")
      : `<div class="empty-state">数据正在同步，请约半小时后重新进入。</div>`;
    renderAdminModuleNotice(targets.filesNotice, moduleStatus.files);
    const statuses = Object.values(moduleStatus).filter(Boolean);
    const updating = statuses.some((status) => String(status.state || "") !== "fresh");
    targets.status.className = "status-line ok";
    targets.status.textContent = updating
      ? "后台已打开，部分数据正在更新；现有内容会继续保留。"
      : `数据已同步：${formatAdminDateTime(data.generated_at)}`;
  }

  async function fetchAccountAdminSummary(workerUrl, options = {}) {
    let lastError = null;
    for (let attempt = 0; attempt < 2; attempt += 1) {
      const controller = new AbortController();
      const timer = setTimeout(() => controller.abort(), 22000);
      try {
        const endpoint = `${workerUrl}/account-admin/summary${options.forceRefresh ? "?refresh=1" : ""}`;
        const response = await fetch(endpoint, {
          cache: "no-store",
          headers: authHeaders(),
          signal: controller.signal,
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
          const error = new Error(data.detail || "后台读取失败。");
          error.status = response.status;
          throw error;
        }
        return data;
      } catch (error) {
        lastError = error;
        if (error && (error.status === 401 || error.status === 403)) break;
        if (attempt === 0) await new Promise((resolve) => setTimeout(resolve, 600));
      } finally {
        clearTimeout(timer);
      }
    }
    throw lastError || new Error("后台读取失败。");
  }

  async function loadAccountAdminSummary(workerUrl, targets, options = {}) {
    targets.status.className = "status-line";
    targets.status.textContent = accountAdminLastSummary
      ? "正在刷新，当前内容会继续保留…"
      : "正在读取最近一次成功数据…";
    targets.refresh.disabled = true;
    try {
      const fetched = await fetchAccountAdminSummary(workerUrl, options);
      const data = mergeAccountAdminSummaryWithLast(fetched);
      accountAdminLastSummary = data;
      renderAccountAdminSummary(data, targets);
      const statuses = Object.values(data.module_status || {}).filter(Boolean);
      if (!options.backgroundRetry && statuses.some((status) => String(status.state || "") !== "fresh")) {
        if (accountAdminRefreshTimer) clearTimeout(accountAdminRefreshTimer);
        accountAdminRefreshTimer = setTimeout(() => {
          accountAdminRefreshTimer = null;
          if (document.getElementById("accountAdminModal")) {
            loadAccountAdminSummary(workerUrl, targets, { backgroundRetry: true }).then(() => {
              if (targets.canManageUsers && targets.exportUsers && document.getElementById("accountAdminModal")) {
                return loadFreshAdminUsers(workerUrl, targets);
              }
              return null;
            }).catch(() => null);
          }
          }, 12000);
      }
      return data;
    } catch (error) {
      if (error && (error.status === 401 || error.status === 403)) {
        targets.status.textContent = "登录状态已失效，请重新登录后打开后台。";
        targets.status.className = "status-line error";
      } else if (accountAdminLastSummary) {
        renderAccountAdminSummary(accountAdminLastSummary, targets);
        targets.status.textContent = "数据更新中，当前显示最近一次成功内容；请稍后刷新。";
        targets.status.className = "status-line ok";
      } else {
        const message = "数据正在更新，请约半小时后重新进入。";
        targets.status.textContent = message;
        targets.status.className = "status-line";
        [targets.picks, targets.wechatSchedule, targets.files, targets.analytics].filter(Boolean).forEach((target) => {
          target.innerHTML = `<div class="empty-state">${message}</div>`;
        });
      }
      if (options.throwOnError) throw error;
      return null;
    } finally {
      targets.refresh.disabled = false;
    }
  }

  function adminHotReportRow(item) {
    const date = String(item && item.date || "");
    const institution = String(item && item.institution || "");
    const size = formatSize(item && item.size_bytes);
    const meta = [institution, date, size].filter(Boolean).join(" · ");
    const url = externalPageUrl({ ...item, source: HOT_REPORT_SOURCE }, "");
    return `
      <a class="account-admin-hot-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">
        <span>
          <strong>${escapeHtml(item && item.title || "近期热门报告")}</strong>
          ${item && item.title_cn ? `<small>${escapeHtml(item.title_cn)}</small>` : ""}
        </span>
        <span>${escapeHtml(meta || "已上传")}</span>
      </a>
    `;
  }

  function adminIntakeSourceLabel(source) {
    if (source === "authority") return "高权报告";
    if (source === "report-a") return "报告A";
    return "Catalog";
  }

  function adminIntakeAvailabilityLabel(item) {
    const availability = String(item && item.availability || "");
    if (availability === "text_only") return "Text only · 可补齐";
    if (availability === "missing") return "PDF 缺失 · 可修复";
    if (availability === "repaired") return "已补齐";
    if (availability === "available" || item && item.available === true) return "已有有效 PDF";
    return "待满足申请";
  }

  function adminIntakeResultMarkup(item, options = {}) {
    const uploadable = item && item.uploadable !== false && item.available !== true;
    const source = String(item && item.source || options.source || "catalog");
    const id = String(item && (item.report_id || item.origin_id || item.id) || "");
    const requestId = String(item && item.request_id || "");
    const meta = [
      adminIntakeSourceLabel(source),
      item && item.institution,
      item && (item.date || item.attempted_at && String(item.attempted_at).slice(0, 10)),
      id,
    ].filter(Boolean).join(" · ");
    const stateClass = uploadable ? "" : " is-blocked";
    return `
      <button class="account-admin-intake-result" type="button"
        data-source="${escapeHtml(source)}"
        data-id="${escapeHtml(id)}"
        data-request-id="${escapeHtml(requestId)}"${uploadable ? "" : " disabled"}>
        <span>
          <strong>${escapeHtml(item && (item.title || item.title_cn) || "未命名报告")}</strong>
          <small>${escapeHtml(meta)}</small>
        </span>
        <span class="account-admin-intake-state${stateClass}">${escapeHtml(adminIntakeAvailabilityLabel(item))}</span>
      </button>
    `;
  }

  function adminIntakeSelectionMarkup(item) {
    const source = String(item && item.source || "catalog");
    const id = String(item && (item.report_id || item.origin_id || item.id) || "");
    const meta = [adminIntakeSourceLabel(source), item && item.institution, item && item.date, id]
      .filter(Boolean)
      .join(" · ");
    return `
      <span>
        <strong>${escapeHtml(item && (item.title || item.title_cn) || "未命名报告")}</strong>
        <small>${escapeHtml(meta)}</small>
      </span>
      <span class="account-admin-intake-state">${escapeHtml(adminIntakeAvailabilityLabel(item))}</span>
    `;
  }

  async function fetchAdminPdfIntakeCandidates(workerUrl, source, query, options = {}) {
    const params = new URLSearchParams({
      source,
      q: String(query || "").trim(),
      page: String(Math.max(1, Number(options.page || 1) || 1)),
    });
    if (options.cursor) params.set("cursor", String(options.cursor));
    const response = await fetch(`${workerUrl}/account-admin/pdf-intake-search?${params.toString()}`, {
      cache: "no-store",
      headers: authHeaders(),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !Array.isArray(data.items)) {
      throw new Error(data.detail || "可补齐报告检索失败，请稍后重试。");
    }
    return data;
  }

  async function fetchAdminReportRequestQueue(workerUrl, query = "", options = {}) {
    const params = new URLSearchParams({ q: String(query || "").trim(), limit: "40" });
    if (options.cursor) params.set("cursor", String(options.cursor));
    const response = await fetch(`${workerUrl}/account-admin/report-requests?${params.toString()}`, {
      cache: "no-store",
      headers: authHeaders(),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !Array.isArray(data.items)) {
      throw new Error(data.detail || "申请队列读取失败。");
    }
    return {
      items: data.items,
      total: Number(data.total || data.items.length) || data.items.length,
      has_more: data.has_more === true,
      next_cursor: String(data.next_cursor || ""),
      index_rebuilding: data.index_rebuilding === true,
      migration_complete: data.migration_complete,
      repair_pending: data.repair_pending === true || data.index_repair_pending === true,
      partial_index: data.index_rebuilding === true
        || data.migration_complete === false
        || data.repair_pending === true
        || data.index_repair_pending === true,
    };
  }

  function contactReportDetailUrl(item) {
    const id = String(item && (item.origin_id || item.report_id || item.id) || "");
    const source = String(item && item.source || "");
    if (!id || !["authority", "report-a"].includes(source)) return "";
    return externalPageUrl({ ...item, id, source }, "");
  }

  function buildContactReportUploadFormData(item, pdf) {
    const source = String(item && item.source || "");
    const originId = String(item && (item.report_id || item.origin_id || item.id) || "");
    const requestId = String(item && item.request_id || "");
    const targetToken = String(item && item.target_token || "");
    if (!originId || !["authority", "report-a"].includes(source)) {
      throw new Error("原报告来源或编号无效，请重新搜索并选择。");
    }
    if (!requestId && !targetToken) {
      throw new Error("原报告验证信息已过期，请重新搜索并选择后再上传。");
    }
    if (!pdf) throw new Error("请选择 PDF 文件。");
    const formData = new FormData();
    formData.set("source", source);
    formData.set("origin_id", originId);
    formData.set("title", item && item.title || "");
    formData.set("institution", item && item.institution || "");
    formData.set("date", item && item.date || "");
    if (requestId) formData.set("request_id", requestId);
    if (targetToken) formData.set("target_token", targetToken);
    formData.set("pdf", pdf, pdf.name);
    return { formData, originId };
  }

  async function loadAdminHotReports(workerUrl, targets) {
    if (!targets.hotReportSection || targets.hotReportSection.hidden || !targets.hotReportList) return [];
    targets.hotReportStatus.className = "status-line";
    targets.hotReportStatus.textContent = "正在读取已上传报告…";
    try {
      async function loadCompleteCollection() {
        const itemsById = new Map();
        const seenCursors = new Set();
        const maxPages = Math.ceil(500 / 60);
        let cursor = "";
        let pagesRead = 0;
        let reportedTotal = null;
        while (itemsById.size < 500 && pagesRead < maxPages) {
          const params = new URLSearchParams({ limit: "60" });
          if (cursor) params.set("cursor", cursor);
          const response = await fetch(`${workerUrl}/hot-reports?${params.toString()}`, { cache: "no-store" });
          pagesRead += 1;
          const data = await response.json().catch(() => ({}));
          if (!response.ok) {
            const failure = new Error(data.detail || "近期热门报告读取失败。");
            failure.status = response.status;
            throw failure;
          }
          const hasReportedTotal = data.total !== null && data.total !== undefined && data.total !== "";
          const rawTotal = hasReportedTotal ? Number(data.total) : Number.NaN;
          if (hasReportedTotal && !Number.isSafeInteger(rawTotal)) {
            throw new Error("近期热门报告总数异常，请稍后重试。");
          }
          if (hasReportedTotal) {
            const pageTotal = rawTotal;
            if (pageTotal < 0 || pageTotal > 500) throw new Error("近期热门报告总数异常，请稍后重试。");
            if (reportedTotal !== null && reportedTotal !== pageTotal) {
              throw new Error("近期热门报告分页总数不一致，请稍后重试。");
            }
            reportedTotal = pageTotal;
          }
          const pageItems = Array.isArray(data.items) ? data.items : [];
          for (const item of pageItems) {
            const id = String(item && item.id || "");
            if (!id) throw new Error("近期热门报告分页数据不完整，请稍后重试。");
            if (!itemsById.has(id) && itemsById.size < 500) itemsById.set(id, item);
          }
          if (data.has_more !== true || itemsById.size >= 500) break;
          const nextCursor = String(data.next_cursor || "");
          if (!nextCursor) throw new Error("近期热门报告分页数据不完整，请稍后重试。");
          if (seenCursors.has(nextCursor)) throw new Error("近期热门报告分页状态异常，请稍后重试。");
          if (pagesRead >= maxPages) throw new Error("近期热门报告分页数量异常，请稍后重试。");
          seenCursors.add(nextCursor);
          cursor = nextCursor;
        }
        const items = [...itemsById.values()];
        if (reportedTotal !== null && items.length !== reportedTotal) {
          throw new Error("近期热门报告数量校验失败，请稍后重试。");
        }
        return { items, total: reportedTotal === null ? items.length : reportedTotal };
      }

      let collection = null;
      for (let attempt = 0; attempt < 2; attempt += 1) {
        try {
          collection = await loadCompleteCollection();
          break;
        } catch (error) {
          if (!(error && error.status === 409 && attempt === 0)) throw error;
          targets.hotReportStatus.textContent = "报告列表刚刚更新，正在从第一页重新读取…";
        }
      }
      if (!collection) throw new Error("近期热门报告读取失败。");
      const view = adminCollectionPreview(collection.items);
      accountAdminHotReports = view.all;
      targets.hotReportList.innerHTML = view.preview.length
        ? view.preview.map(adminHotReportRow).join("")
        : '<div class="empty-state">还没有上传近期热门报告。</div>';
      targets.hotReportCount.textContent = `${collection.total} 条`;
      if (targets.hotReportMore) targets.hotReportMore.hidden = !view.hasMore;
      targets.hotReportStatus.textContent = "";
      return view.all;
    } catch (error) {
      targets.hotReportList.innerHTML = '<div class="empty-state">暂时无法读取已上传报告。</div>';
      targets.hotReportCount.textContent = "";
      if (targets.hotReportMore) targets.hotReportMore.hidden = true;
      accountAdminHotReports = [];
      targets.hotReportStatus.className = "status-line error";
      targets.hotReportStatus.textContent = error.message || "近期热门报告读取失败。";
      return [];
    }
  }

  async function uploadAdminHotReport(workerUrl, targets) {
    const file = targets.hotReportPdf && targets.hotReportPdf.files && targets.hotReportPdf.files[0];
    if (!file) throw new Error("请选择 PDF 文件。");
    if (file.size <= 0 || file.size > 95 * 1024 * 1024) throw new Error("PDF 必须不超过 95 MB。");
    const formData = new FormData(targets.hotReportForm);
    const uploadId = adminPdfUploadIdForFile(targets.hotReportPdf);
    const data = await runAdminPdfUpload({
      workerUrl,
      url: `${workerUrl}/account-admin/hot-report`,
      formData,
      file,
      fileInput: targets.hotReportPdf,
      uploadId,
      kind: "hot-report",
      mode: "hot-report",
      prefix: "accountAdminHotReportUpload",
      setStatus(message, state) {
        targets.hotReportStatus.className = state ? `status-line ${state}` : "status-line";
        targets.hotReportStatus.textContent = message;
      },
    });
    const item = data && (data.item || data.hot_report || data.upload && data.upload.result && data.upload.result.item);
    if (!item) throw new Error("PDF 已处理，但报告结果读取不完整。请检查上传结果。");
    return { ...data, item };
  }

  function adminExportFilename() {
    const now = new Date();
    const pad = (value) => String(value).padStart(2, "0");
    return `${PUBLIC_BRAND}-users-${now.getFullYear()}-${pad(now.getMonth() + 1)}-${pad(now.getDate())}-${pad(now.getHours())}${pad(now.getMinutes())}${pad(now.getSeconds())}.xlsx`;
  }

  async function fetchFreshAdminUsers(workerUrl) {
    const response = await fetch(`${workerUrl}/account-admin/users-export`, {
      cache: "no-store",
      headers: authHeaders(),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || `用户读取失败 (${response.status})。`);
    if (!Array.isArray(data.users)) throw new Error("用户接口返回的数据格式不完整。");
    return data;
  }

  async function loadFreshAdminUsers(workerUrl, targets) {
    const data = await fetchFreshAdminUsers(workerUrl);
    accountAdminUsersByEmail = new Map(data.users.map((user) => [String(user.email || "").toLowerCase(), user]));
    if (accountAdminLastSummary) accountAdminLastSummary = { ...accountAdminLastSummary, users: data.users };
    if (targets.usersNotice) {
      targets.usersNotice.hidden = true;
      targets.usersNotice.textContent = "";
    }
    renderAdminUserTable(targets);
    return data;
  }

  function renderAdminUsersVerificationState(targets, message, kind = "") {
    const cachedCount = accountAdminUsersByEmail.size;
    if (targets.userCount) {
      targets.userCount.textContent = cachedCount
        ? `${cachedCount} users · ${kind === "error" ? "最近同步" : "核验中…"}`
        : (kind === "error" ? "未核验" : "核验中…");
    }
    // The summary already contains the latest verified snapshot. A transient
    // live refresh must not erase that useful table and leave the administrator
    // unable to inspect or select users. Only show the empty-state row when no
    // verified snapshot exists at all.
    if (targets.users && !cachedCount) {
      targets.users.innerHTML = `<tr><td colspan="11"><div class="empty-state">${escapeHtml(message)}</div></td></tr>`;
    }
    if (targets.usersNotice) {
      targets.usersNotice.hidden = false;
      targets.usersNotice.className = kind ? `account-admin-module-notice ${kind}` : "account-admin-module-notice";
      targets.usersNotice.textContent = message;
    }
  }

  async function exportAdminUsersToExcel(workerUrl, targets) {
    if (!targets.exportUsers) return;
    targets.exportUsers.disabled = true;
    targets.status.className = "status-line";
    targets.status.textContent = "正在现场读取全部用户最新状态并生成 Excel…";
    try {
      const data = await fetchFreshAdminUsers(workerUrl);
      const users = data.users;
      const rows = users.map(adminUserViewModel);
      const { buildXlsxWorkbook, downloadXlsx } = await import(versionedSiteAssetUrl("assets/xlsx-export.js"));
      const blob = buildXlsxWorkbook({
        sheetName: "用户状态",
        columns: [
          { header: "用户名", key: "username", width: 18 },
          { header: "邮箱", key: "email", width: 30 },
          { header: "注册站点", key: "registered_site", width: 14 },
          { header: "用户来源", key: "site_origin", width: 14 },
          { header: "状态", key: "status", width: 12 },
          { header: "账号", key: "account", width: 14 },
          { header: "实际下载权限", key: "access", width: 28 },
          { header: "到期", key: "expiry", width: 14 },
          { header: "注册", key: "registered", width: 14 },
          { header: "最近登录", key: "last_login", width: 20 },
          { header: "权限来源", key: "access_source", width: 20 },
          { header: "授权来源站点", key: "entitlement_source_site", width: 16 },
          { header: "授权来源类型", key: "entitlement_grant_source", width: 18 },
          { header: "授权代号", key: "entitlement_plan_code", width: 14 },
          { header: "权限最后更新", key: "access_updated", width: 22 },
        ],
        rows,
      });
      downloadXlsx(blob, adminExportFilename());
      targets.status.className = "status-line ok";
      targets.status.textContent = `Excel 已导出：${rows.length} 个用户（使用点击时最新状态）。`;
    } catch (error) {
      targets.status.className = "status-line error";
      targets.status.textContent = error.message || "Excel 导出失败。";
    } finally {
      targets.exportUsers.disabled = false;
    }
  }

  function showAccountAdminModal(workerUrl) {
    if (!workerUrl || !canOpenOperationsPanel()) return;
    const session = loadAuthSession();
    const isOperatorOnly = isOperatorSession(session) && !isSuperSession(session);
    const canManageUsers = !isOperatorOnly;
    const summaryOwner = String(session && session.user && (session.user.email || session.user.username) || "").toLowerCase();
    if (accountAdminLastSummaryOwner && accountAdminLastSummaryOwner !== summaryOwner) accountAdminLastSummary = null;
    accountAdminLastSummaryOwner = summaryOwner;
    const existing = document.getElementById("accountAdminModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", accountAdminModalMarkup({
      title: isOperatorOnly ? "运营后台" : "管理后台",
      showWechat: !isOperatorOnly,
      showUsers: canManageUsers,
      showAnalytics: !isOperatorOnly,
      showHotReports: !isOperatorOnly,
      showReportChatArchives: canManageUsers,
    }));

    const modal = document.getElementById("accountAdminModal");
    const title = document.getElementById("accountAdminTitle");
    const close = document.getElementById("accountAdminClose");
    const refresh = document.getElementById("accountAdminRefresh");
    const status = document.getElementById("accountAdminStatus");
    const pickCount = document.getElementById("accountAdminPickCount");
    const picks = document.getElementById("accountAdminPicks");
    const picksNotice = document.getElementById("accountAdminPicksNotice");
    const marketViewCount = document.getElementById("accountAdminMarketViewCount");
    const marketViews = document.getElementById("accountAdminMarketViews");
    const marketViewsMore = document.getElementById("accountAdminMarketViewsMore");
    const marketViewsNotice = document.getElementById("accountAdminMarketViewsNotice");
    const wechatCount = document.getElementById("accountAdminWechatCount");
    const wechatSchedule = document.getElementById("accountAdminWechatSchedule");
    const wechatNotice = document.getElementById("accountAdminWechatNotice");
    const wechatSection = document.getElementById("accountAdminWechatSection");
    const hotReportSection = document.getElementById("accountAdminHotReportsSection");
    const hotReportCount = document.getElementById("accountAdminHotReportCount");
    const hotReportMore = document.getElementById("accountAdminHotReportsMore");
    const hotReportForm = document.getElementById("accountAdminHotReportForm");
    const hotReportTitle = document.getElementById("accountAdminHotReportTitle");
    const hotReportDate = document.getElementById("accountAdminHotReportDate");
    const hotReportPdf = document.getElementById("accountAdminHotReportPdf");
    const hotReportStatus = document.getElementById("accountAdminHotReportStatus");
    const hotReportList = document.getElementById("accountAdminHotReportList");
    const intakeTabs = Array.from(modal.querySelectorAll("[data-admin-intake-mode]"));
    const intakePanels = {
      new: document.getElementById("accountAdminIntakeNew"),
      catalog: document.getElementById("accountAdminIntakeCatalog"),
      request: document.getElementById("accountAdminIntakeRequest"),
    };
    const uploadRecovery = document.getElementById("accountAdminUploadRecovery");
    const uploadRecoveryText = document.getElementById("accountAdminUploadRecoveryText");
    const uploadRecoveryCheck = document.getElementById("accountAdminUploadRecoveryCheck");
    const catalogIntakeSearch = document.getElementById("accountAdminCatalogIntakeSearch");
    const catalogIntakeQuery = document.getElementById("accountAdminCatalogIntakeQuery");
    const catalogIntakeStatus = document.getElementById("accountAdminCatalogIntakeStatus");
    const catalogIntakeResults = document.getElementById("accountAdminCatalogIntakeResults");
    const catalogIntakeUpload = document.getElementById("accountAdminCatalogIntakeUpload");
    const catalogIntakeSelection = document.getElementById("accountAdminCatalogIntakeSelection");
    const catalogIntakePdf = document.getElementById("accountAdminCatalogIntakePdf");
    const requestQueueRefresh = document.getElementById("accountAdminRequestQueueRefresh");
    const requestQueueSearch = document.getElementById("accountAdminRequestQueueSearch");
    const requestQueueQuery = document.getElementById("accountAdminRequestQueueQuery");
    const requestQueueStatus = document.getElementById("accountAdminRequestQueueStatus");
    const requestQueueResults = document.getElementById("accountAdminRequestQueueResults");
    const requestIntakeUpload = document.getElementById("accountAdminRequestIntakeUpload");
    const requestIntakeSelection = document.getElementById("accountAdminRequestIntakeSelection");
    const requestIntakePdf = document.getElementById("accountAdminRequestIntakePdf");
    const userCount = document.getElementById("accountAdminUserCount");
    const users = document.getElementById("accountAdminUsers");
    const usersSection = document.getElementById("accountAdminUsersSection");
    const exportUsers = document.getElementById("accountAdminExportUsers");
    const newUser = document.getElementById("accountAdminNewUser");
    const passwordReset = document.getElementById("accountAdminPasswordReset");
    const passwordResetEmail = document.getElementById("accountAdminPasswordResetEmail");
    const userCreator = document.getElementById("accountAdminUserCreator");
    const userCreatorClose = document.getElementById("accountAdminUserCreatorClose");
    const newUsername = document.getElementById("accountAdminNewUsername");
    const newEmail = document.getElementById("accountAdminNewEmail");
    const newPassword = document.getElementById("accountAdminNewPassword");
    const userEditor = document.getElementById("accountAdminUserEditor");
    const userEditorTitle = document.getElementById("accountAdminUserEditorTitle");
    const userEditorClose = document.getElementById("accountAdminUserEditorClose");
    const accessEmail = document.getElementById("accountAdminAccessEmail");
    const accessMode = document.getElementById("accountAdminAccessMode");
    const accessDuration = document.getElementById("accountAdminAccessDuration");
    const accessExpiry = document.getElementById("accountAdminAccessExpiry");
    const accessInstitutions = document.getElementById("accountAdminAccessInstitutions");
    const accessInstitutionSearch = document.getElementById("accountAdminAccessInstitutionSearch");
    const accessInstitutionCount = document.getElementById("accountAdminAccessInstitutionCount");
    const accessIndustries = document.getElementById("accountAdminAccessIndustries");
    const accessPageRanges = document.getElementById("accountAdminAccessPageRanges");
    const accessNote = document.getElementById("accountAdminAccessNote");
    const accessRenew = document.getElementById("accountAdminAccessRenew");
    const files = document.getElementById("accountAdminFiles");
    const filesNotice = document.getElementById("accountAdminFilesNotice");
    const analyticsCount = document.getElementById("accountAdminAnalyticsCount");
    const analytics = document.getElementById("accountAdminAnalytics");
    const analyticsNotice = document.getElementById("accountAdminAnalyticsNotice");
    const analyticsSection = document.getElementById("accountAdminAnalyticsSection");
    const reportChatArchiveSection = document.getElementById("accountAdminReportChatArchiveSection");
    const reportChatArchiveRefresh = document.getElementById("accountAdminReportChatArchiveRefresh");
    const reportChatArchiveStatus = document.getElementById("accountAdminReportChatArchiveStatus");
    const reportChatArchiveList = document.getElementById("accountAdminReportChatArchiveList");
    const usersNotice = document.getElementById("accountAdminUsersNotice");
    const targets = {
      title,
      status,
      refresh,
      pickCount,
      picks,
      picksNotice,
      marketViewCount,
      marketViews,
      marketViewsMore,
      marketViewsNotice,
      wechatCount,
      wechatSchedule,
      wechatNotice,
      wechatSection,
      hotReportSection,
      hotReportCount,
      hotReportMore,
      hotReportForm,
      hotReportTitle,
      hotReportDate,
      hotReportPdf,
      hotReportStatus,
      hotReportList,
      analyticsCount,
      analytics,
      analyticsNotice,
      analyticsSection,
      reportChatArchiveSection,
      reportChatArchiveRefresh,
      reportChatArchiveStatus,
      reportChatArchiveList,
      userCount,
      users,
      usersSection,
      exportUsers,
      newUser,
      passwordReset,
      passwordResetEmail,
      userCreator,
      userCreatorClose,
      newUsername,
      newEmail,
      newPassword,
      userEditor,
      userEditorTitle,
      userEditorClose,
      accessEmail,
      accessMode,
      accessDuration,
      accessExpiry,
      accessInstitutions,
      accessInstitutionSearch,
      accessInstitutionCount,
      accessIndustries,
      accessPageRanges,
      accessNote,
      accessRenew,
      files,
      filesNotice,
      usersNotice,
      canManageUsers,
    };

    const catalogIntakeItems = new Map();
    const requestIntakeItems = new Map();
    const requestIntakeByIdentity = new Map();
    let selectedCatalogIntake = null;
    let selectedRequestIntake = null;
    let requestQueueLoaded = false;
    let requestQueueCursor = "";
    let requestQueueHasMore = false;
    let requestQueueIndexBuilding = false;
    let requestSearchQuery = "";
    const requestSearchPage = { "report-a": 1, authority: 1 };
    const requestSearchHasMore = { "report-a": false, authority: false };
    let catalogIntakePage = 1;
    let catalogIntakeCursor = "";

    function intakeItemKey(item) {
      return [
        String(item && item.source || "catalog"),
        String(item && (item.report_id || item.origin_id || item.id) || ""),
        String(item && item.request_id || ""),
      ].join("\u001f");
    }

    function requestIntakeIdentity(item) {
      return [
        String(item && item.source || ""),
        String(item && (item.report_id || item.origin_id || item.id) || ""),
      ].join("\u001f");
    }

    function setIntakeStatus(target, message, state = "") {
      if (!target) return;
      target.className = state ? `status-line ${state}` : "status-line";
      target.textContent = String(message || "");
    }

    function setIntakeHtmlStatus(target, html, state = "") {
      if (!target) return;
      target.className = state ? `status-line ${state}` : "status-line";
      target.innerHTML = html || "";
    }

    function renderRequestIntakeResults() {
      requestIntakeItems.clear();
      Array.from(requestIntakeByIdentity.values()).forEach((item) => requestIntakeItems.set(intakeItemKey(item), item));
      const items = Array.from(requestIntakeByIdentity.values());
      const moreButtons = ["report-a", "authority"]
        .filter((source) => requestSearchHasMore[source])
        .map((source) => `<button class="secondary-button account-admin-intake-more" type="button" data-admin-intake-search-more="${source}">加载更多${adminIntakeSourceLabel(source)}原记录</button>`)
        .join("");
      const requestQueueMoreButton = requestQueueHasMore
        ? '<button class="secondary-button account-admin-intake-more" type="button" data-admin-intake-more="request">加载更多申请</button>'
        : "";
      requestQueueResults.innerHTML = items.length
        ? `${items.map((item) => adminIntakeResultMarkup(item)).join("")}${requestQueueMoreButton}${moreButtons}`
        : requestQueueIndexBuilding
          ? `<div class="empty-state">申请队列正在后台建立索引，已展示部分结果，请稍后刷新/加载。</div>${requestQueueMoreButton}`
          : '<div class="empty-state">当前没有匹配的待满足申请。</div>';
      return items;
    }

    function setIntakeMode(mode) {
      const next = ["new", "catalog", "request"].includes(mode) ? mode : "new";
      intakeTabs.forEach((tab) => {
        const active = tab.dataset.adminIntakeMode === next;
        tab.classList.toggle("is-active", active);
        tab.setAttribute("aria-selected", active ? "true" : "false");
        tab.tabIndex = active ? 0 : -1;
      });
      Object.entries(intakePanels).forEach(([name, panel]) => {
        if (panel) panel.hidden = name !== next;
      });
      if (next === "request" && !requestQueueLoaded) loadRequestQueue();
    }

    function renderCompletedIntake(mode, data) {
      const item = data && (data.item || data.hot_report || data.contact_report
        || data.upload && data.upload.result && (
          data.upload.result.item || data.upload.result.hot_report || data.upload.result.contact_report
        ));
      if (mode === "hot-report") {
        const titleText = String(item && item.title || "报告");
        setIntakeStatus(hotReportStatus, `已上传并发布：${titleText}`, "ok");
        loadAdminHotReports(workerUrl, targets).catch(() => null);
        return;
      }
      if (mode === "text-only") {
        const id = String(item && item.id || selectedCatalogIntake && selectedCatalogIntake.id || "");
        const href = id ? reportPageUrl(id, { preview: item || selectedCatalogIntake || { id } }) : "";
        setIntakeHtmlStatus(catalogIntakeStatus, href
          ? `PDF 已补齐并发布。<a href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">打开原报告详情</a>`
          : "PDF 已补齐并发布。", "ok");
        return;
      }
      const reportItem = item || selectedRequestIntake;
      const href = contactReportDetailUrl(reportItem);
      setIntakeHtmlStatus(requestQueueStatus, href
        ? `PDF 已绑定原报告并发布。<a href="${escapeHtml(href)}" target="_blank" rel="noopener noreferrer">打开原详情验证</a>`
        : "PDF 已绑定原报告并发布。", "ok");
      requestQueueLoaded = false;
    }

    function uploadUiPrefix(mode) {
      if (mode === "text-only") return "accountAdminCatalogUpload";
      if (mode === "request") return "accountAdminRequestUpload";
      return "accountAdminHotReportUpload";
    }

    function uploadStatusTarget(mode) {
      if (mode === "text-only") return catalogIntakeStatus;
      if (mode === "request") return requestQueueStatus;
      return hotReportStatus;
    }

    function guardUnresolvedIntakeUpload(statusTarget) {
      const saved = readAdminPdfUploadSession();
      if (!saved) return false;
      if (uploadRecovery) uploadRecovery.hidden = false;
      if (uploadRecoveryText) uploadRecoveryText.textContent = restoredAdminPdfUploadMessage(saved);
      setIntakeStatus(statusTarget, "上一笔 PDF 上传结果尚未确认。请先点击“检查上传结果”，不要重复上传。", "error");
      return true;
    }

    async function checkSavedUpload(session = readAdminPdfUploadSession()) {
      if (!session) {
        if (uploadRecovery) uploadRecovery.hidden = true;
        return null;
      }
      setIntakeMode(session.mode === "text-only" ? "catalog" : session.mode === "request" ? "request" : "new");
      if (uploadRecovery) uploadRecovery.hidden = false;
      if (uploadRecoveryText) uploadRecoveryText.textContent = restoredAdminPdfUploadMessage(session);
      if (uploadRecoveryCheck) uploadRecoveryCheck.disabled = true;
      try {
        const result = await checkAdminPdfUploadResult(workerUrl, session, {
          prefix: uploadUiPrefix(session.mode),
          fileInput: session.mode === "text-only" ? catalogIntakePdf : session.mode === "request" ? requestIntakePdf : hotReportPdf,
          setStatus(message, state) {
            setIntakeStatus(uploadStatusTarget(session.mode), message, state);
          },
          onComplete(data) {
            renderCompletedIntake(session.mode, data);
          },
        });
        if (!readAdminPdfUploadSession() && uploadRecovery) uploadRecovery.hidden = true;
        return result;
      } catch (error) {
        setIntakeStatus(uploadStatusTarget(session.mode), error.message || "上传状态读取失败，请稍后再检查。", "error");
        throw error;
      } finally {
        if (uploadRecoveryCheck) uploadRecoveryCheck.disabled = false;
      }
    }

    async function loadCatalogCandidates(options = {}) {
      const append = options.append === true;
      const query = String(catalogIntakeQuery && catalogIntakeQuery.value || "").trim();
      if (!query) {
        setIntakeStatus(catalogIntakeStatus, "请输入报告标题或编号。", "error");
        if (catalogIntakeQuery) catalogIntakeQuery.focus();
        return;
      }
      const page = append ? catalogIntakePage + 1 : 1;
      setIntakeStatus(catalogIntakeStatus, append ? "正在加载更多可补齐记录…" : "正在核验 Text only 与 PDF 对象状态…");
      if (catalogIntakeResults && !append) catalogIntakeResults.innerHTML = '<div class="empty-state">正在检索并核验对象…</div>';
      try {
        const data = await fetchAdminPdfIntakeCandidates(workerUrl, "catalog", query, {
          page,
          cursor: append ? catalogIntakeCursor : "",
        });
        if (!append) catalogIntakeItems.clear();
        data.items.forEach((item) => catalogIntakeItems.set(intakeItemKey(item), { ...item, source: "catalog" }));
        catalogIntakePage = page;
        catalogIntakeCursor = String(data.next_cursor || "");
        const hasMore = data.has_more === true || Boolean(data.next_page) || Boolean(catalogIntakeCursor);
        const allItems = Array.from(catalogIntakeItems.values());
        catalogIntakeResults.innerHTML = allItems.length
          ? `${allItems.map((item) => adminIntakeResultMarkup(item)).join("")}${hasMore ? '<button class="secondary-button account-admin-intake-more" type="button" data-admin-intake-more="catalog">加载更多</button>' : ""}`
          : '<div class="empty-state">没有找到可补齐记录。有效 PDF 不允许覆盖；可尝试更完整的标题或编号。</div>';
        setIntakeStatus(catalogIntakeStatus, allItems.length
          ? `已加载 ${allItems.length} 条记录${hasMore ? "，可继续加载更多" : ""}；请选择可补齐项。`
          : "未找到可补齐记录。", allItems.length ? "ok" : "");
      } catch (error) {
        catalogIntakeResults.innerHTML = '<div class="error-state">可补齐记录暂时无法读取，请稍后重试。</div>';
        setIntakeStatus(catalogIntakeStatus, error.message || "可补齐记录检索失败。", "error");
      }
    }

    async function loadRequestQueue(options = {}) {
      const append = options.append === true;
      requestQueueLoaded = true;
      if (!append) requestQueueIndexBuilding = false;
      const query = String(requestQueueQuery && requestQueueQuery.value || "").trim();
      setIntakeStatus(requestQueueStatus, append ? "正在加载下一页申请…" : "正在读取报告A与高权报告申请队列…");
      if (requestQueueResults && !append) requestQueueResults.innerHTML = '<div class="empty-state">正在读取申请队列…</div>';
      try {
        const tasks = [fetchAdminReportRequestQueue(workerUrl, query, { cursor: append ? requestQueueCursor : "" })];
        if (!append && query) {
          tasks.push(fetchAdminPdfIntakeCandidates(workerUrl, "report-a", query));
          tasks.push(fetchAdminPdfIntakeCandidates(workerUrl, "authority", query));
        }
        const results = await Promise.allSettled(tasks);
        const queueResult = results[0];
        if (queueResult.status === "rejected" && results.every((result) => result.status === "rejected")) {
          throw queueResult.reason || new Error("申请队列读取失败。");
        }
        if (!append) {
          requestIntakeItems.clear();
          requestIntakeByIdentity.clear();
          requestQueueCursor = "";
          requestQueueHasMore = false;
          requestSearchQuery = query;
          requestSearchPage["report-a"] = 1;
          requestSearchPage.authority = 1;
          requestSearchHasMore["report-a"] = false;
          requestSearchHasMore.authority = false;
        }
        if (queueResult.status === "fulfilled") {
          queueResult.value.items.forEach((item) => requestIntakeByIdentity.set(requestIntakeIdentity(item), item));
          requestQueueCursor = queueResult.value.next_cursor;
          requestQueueHasMore = queueResult.value.has_more && Boolean(requestQueueCursor);
          requestQueueIndexBuilding = queueResult.value.partial_index === true;
        }
        if (!append) {
          results.slice(1).forEach((result, index) => {
            if (result.status !== "fulfilled") return;
            const source = index === 0 ? "report-a" : "authority";
            requestSearchHasMore[source] = result.value.has_more === true;
            result.value.items.forEach((item) => {
              const normalized = { ...item, source: item.source || source };
              const identity = requestIntakeIdentity(normalized);
              if (!requestIntakeByIdentity.has(identity)) requestIntakeByIdentity.set(identity, normalized);
            });
          });
        }
        const items = renderRequestIntakeResults();
        const partial = results.some((result) => result.status === "rejected");
        if (requestQueueIndexBuilding) {
          setIntakeStatus(requestQueueStatus, "申请队列正在后台建立索引，已展示部分结果，请稍后刷新/加载。");
        } else {
          setIntakeStatus(requestQueueStatus, items.length
            ? `已加载 ${items.length} 条申请或原记录${requestQueueHasMore ? "，可按需加载下一页" : ""}${partial ? "；部分主动搜索暂未返回" : ""}。`
            : "当前没有匹配的待满足申请。", partial ? "" : "ok");
        }
      } catch (error) {
        requestQueueLoaded = false;
        requestQueueResults.innerHTML = '<div class="error-state">申请队列暂时无法读取，请稍后重试。</div>';
        setIntakeStatus(requestQueueStatus, error.message || "申请队列读取失败。", "error");
      }
    }

    async function loadMoreRequestSearch(source) {
      if (!["report-a", "authority"].includes(source) || !requestSearchHasMore[source] || !requestSearchQuery) return;
      const page = requestSearchPage[source] + 1;
      setIntakeStatus(requestQueueStatus, `正在加载更多${adminIntakeSourceLabel(source)}原记录…`);
      try {
        const data = await fetchAdminPdfIntakeCandidates(workerUrl, source, requestSearchQuery, { page });
        data.items.forEach((item) => {
          const normalized = { ...item, source: item.source || source };
          const identity = requestIntakeIdentity(normalized);
          if (!requestIntakeByIdentity.has(identity)) requestIntakeByIdentity.set(identity, normalized);
        });
        requestSearchPage[source] = page;
        requestSearchHasMore[source] = data.has_more === true;
        const items = renderRequestIntakeResults();
        setIntakeStatus(requestQueueStatus, `已加载 ${items.length} 条申请或原记录。`, "ok");
      } catch (error) {
        setIntakeStatus(requestQueueStatus, error.message || `${adminIntakeSourceLabel(source)}原记录加载失败。`, "error");
      }
    }

    intakeTabs.forEach((tab) => {
      tab.addEventListener("click", () => setIntakeMode(tab.dataset.adminIntakeMode));
    });
    if (catalogIntakeSearch) catalogIntakeSearch.addEventListener("submit", (event) => {
      event.preventDefault();
      loadCatalogCandidates();
    });
    if (catalogIntakeResults) catalogIntakeResults.addEventListener("click", (event) => {
      if (event.target.closest("[data-admin-intake-more='catalog']")) {
        loadCatalogCandidates({ append: true });
        return;
      }
      const button = event.target.closest("[data-source][data-id]");
      if (!button || button.disabled) return;
      const key = [button.dataset.source, button.dataset.id, button.dataset.requestId || ""].join("\u001f");
      selectedCatalogIntake = catalogIntakeItems.get(key) || null;
      if (!selectedCatalogIntake) return;
      catalogIntakeSelection.innerHTML = adminIntakeSelectionMarkup(selectedCatalogIntake);
      catalogIntakeUpload.hidden = false;
      resetAdminPdfUploadId(catalogIntakePdf);
      catalogIntakePdf.focus();
      setIntakeStatus(catalogIntakeStatus, "已选择记录。请选择对应 PDF；系统会再次检查，已有有效对象不会被覆盖。", "ok");
    });
    if (requestQueueRefresh) requestQueueRefresh.addEventListener("click", () => {
      requestQueueLoaded = false;
      loadRequestQueue();
    });
    if (requestQueueSearch) requestQueueSearch.addEventListener("submit", (event) => {
      event.preventDefault();
      requestQueueLoaded = false;
      loadRequestQueue();
    });
    if (requestQueueResults) requestQueueResults.addEventListener("click", (event) => {
      const searchMore = event.target.closest("[data-admin-intake-search-more]");
      if (searchMore) {
        loadMoreRequestSearch(String(searchMore.dataset.adminIntakeSearchMore || ""));
        return;
      }
      if (event.target.closest("[data-admin-intake-more='request']")) {
        loadRequestQueue({ append: true });
        return;
      }
      const button = event.target.closest("[data-source][data-id]");
      if (!button || button.disabled) return;
      const key = [button.dataset.source, button.dataset.id, button.dataset.requestId || ""].join("\u001f");
      selectedRequestIntake = requestIntakeItems.get(key) || null;
      if (!selectedRequestIntake) return;
      requestIntakeSelection.innerHTML = adminIntakeSelectionMarkup(selectedRequestIntake);
      requestIntakeUpload.hidden = false;
      resetAdminPdfUploadId(requestIntakePdf);
      requestIntakePdf.focus();
      setIntakeStatus(requestQueueStatus, "已选择申请记录。上传后会绑定原报告详情，不另建重复线索。", "ok");
    });
    [hotReportPdf, catalogIntakePdf, requestIntakePdf].filter(Boolean).forEach((input) => {
      input.addEventListener("change", () => resetAdminPdfUploadId(input));
    });
    ["accountAdminHotReportUpload", "accountAdminCatalogUpload", "accountAdminRequestUpload"].forEach((prefix) => {
      const cancel = document.getElementById(`${prefix}Cancel`);
      const check = document.getElementById(`${prefix}Check`);
      if (cancel) cancel.addEventListener("click", () => {
        if (activeAdminPdfUpload && typeof activeAdminPdfUpload.cancel === "function") activeAdminPdfUpload.cancel();
      });
      if (check) check.addEventListener("click", () => {
        checkSavedUpload().catch(() => null);
      });
    });
    if (uploadRecoveryCheck) uploadRecoveryCheck.addEventListener("click", () => {
      checkSavedUpload().catch(() => null);
    });

    if (catalogIntakeUpload) catalogIntakeUpload.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (guardUnresolvedIntakeUpload(catalogIntakeStatus)) return;
      const pdf = catalogIntakePdf && catalogIntakePdf.files && catalogIntakePdf.files[0];
      const submit = catalogIntakeUpload.querySelector("button[type='submit']");
      if (!selectedCatalogIntake) {
        setIntakeStatus(catalogIntakeStatus, "请先检索并选择原记录。", "error");
        return;
      }
      if (!pdf) {
        setIntakeStatus(catalogIntakeStatus, "请选择 PDF 文件。", "error");
        return;
      }
      if (pdf.size <= 0 || pdf.size > 95 * 1024 * 1024) {
        setIntakeStatus(catalogIntakeStatus, "PDF 必须不超过 95 MB。", "error");
        return;
      }
      const formData = new FormData();
      formData.set("id", selectedCatalogIntake.id);
      formData.set("pdf", pdf, pdf.name);
      if (submit) submit.disabled = true;
      catalogIntakePdf.disabled = true;
      try {
        const data = await runAdminPdfUpload({
          url: `${workerUrl}/account-admin/text-only-pdf`,
          formData,
          file: pdf,
          fileInput: catalogIntakePdf,
          uploadId: adminPdfUploadIdForFile(catalogIntakePdf),
          kind: "text-only-pdf",
          mode: "text-only",
          source: "catalog",
          targetId: selectedCatalogIntake.id,
          prefix: "accountAdminCatalogUpload",
          setStatus(message, state) { setIntakeStatus(catalogIntakeStatus, message, state); },
        });
        renderCompletedIntake("text-only", data);
        catalogIntakeUpload.reset();
        resetAdminPdfUploadId(catalogIntakePdf);
      } catch (error) {
        setIntakeStatus(catalogIntakeStatus, error.message || "PDF 补齐失败，请先检查结果。", "error");
      } finally {
        if (submit) submit.disabled = false;
        catalogIntakePdf.disabled = false;
      }
    });

    if (requestIntakeUpload) requestIntakeUpload.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (guardUnresolvedIntakeUpload(requestQueueStatus)) return;
      const pdf = requestIntakePdf && requestIntakePdf.files && requestIntakePdf.files[0];
      const submit = requestIntakeUpload.querySelector("button[type='submit']");
      if (!selectedRequestIntake) {
        setIntakeStatus(requestQueueStatus, "请先选择一条报告申请。", "error");
        return;
      }
      if (!pdf) {
        setIntakeStatus(requestQueueStatus, "请选择 PDF 文件。", "error");
        return;
      }
      if (pdf.size <= 0 || pdf.size > 95 * 1024 * 1024) {
        setIntakeStatus(requestQueueStatus, "PDF 必须不超过 95 MB。", "error");
        return;
      }
      let uploadPayload;
      try {
        uploadPayload = buildContactReportUploadFormData(selectedRequestIntake, pdf);
      } catch (error) {
        setIntakeStatus(requestQueueStatus, error.message || "原报告验证信息无效，请重新选择。", "error");
        return;
      }
      const { formData, originId } = uploadPayload;
      if (submit) submit.disabled = true;
      requestIntakePdf.disabled = true;
      try {
        const data = await runAdminPdfUpload({
          url: `${workerUrl}/account-admin/contact-report-pdf`,
          formData,
          file: pdf,
          fileInput: requestIntakePdf,
          uploadId: adminPdfUploadIdForFile(requestIntakePdf),
          kind: "contact-report-pdf",
          mode: "request",
          source: selectedRequestIntake.source,
          targetId: originId,
          prefix: "accountAdminRequestUpload",
          setStatus(message, state) { setIntakeStatus(requestQueueStatus, message, state); },
        });
        renderCompletedIntake("request", data);
        requestIntakeUpload.reset();
        resetAdminPdfUploadId(requestIntakePdf);
      } catch (error) {
        setIntakeStatus(requestQueueStatus, error.message || "报告绑定失败，请先检查结果。", "error");
      } finally {
        if (submit) submit.disabled = false;
        requestIntakePdf.disabled = false;
      }
    });

    const restoredUpload = readAdminPdfUploadSession();
    if (restoredUpload) {
      if (uploadRecovery) uploadRecovery.hidden = false;
      if (uploadRecoveryText) uploadRecoveryText.textContent = restoredAdminPdfUploadMessage(restoredUpload);
      setIntakeMode(restoredUpload.mode === "text-only" ? "catalog" : restoredUpload.mode === "request" ? "request" : "new");
      renderAdminPdfUploadUi(uploadUiPrefix(restoredUpload.mode), {
        percent: restoredUpload.state === "uploading" ? 0 : 100,
        text: "检测到未确认结果，请先检查，不要重复上传。",
        startedAt: restoredUpload.started_at,
        canCancel: false,
        canCheck: true,
        state: restoredUpload.state,
      });
    } else {
      setIntakeMode("new");
    }

    function finish() {
      if (accountAdminRefreshTimer) {
        clearTimeout(accountAdminRefreshTimer);
        accountAdminRefreshTimer = null;
      }
      if (accountAdminListModalCleanup) accountAdminListModalCleanup();
      modal.remove();
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    if (marketViewsMore) {
      marketViewsMore.addEventListener("click", () => {
        const items = Array.from(accountAdminMarketViews.values());
        const list = openAccountAdminListModal({
          title: "全部 Market Views",
          count: items.length,
          listClass: "account-admin-files",
          bodyHtml: items.map(adminMarketViewRow).join("") || '<div class="empty-state">Market Views PDF 正在准备中。</div>',
          trigger: marketViewsMore,
        });
        if (list) {
          list.body.addEventListener("click", (event) => {
            handleAccountAdminMarketViewDownload(event, workerUrl, list.status);
          });
        }
      });
    }
    if (hotReportMore) {
      hotReportMore.addEventListener("click", () => {
        openAccountAdminListModal({
          title: "全部近期热门报告",
          count: accountAdminHotReports.length,
          listClass: "account-admin-hot-list",
          bodyHtml: accountAdminHotReports.map(adminHotReportRow).join("") || '<div class="empty-state">还没有上传近期热门报告。</div>',
          trigger: hotReportMore,
        });
      });
    }
    refresh.addEventListener("click", async () => {
      await Promise.allSettled([
        loadAccountAdminSummary(workerUrl, targets, { forceRefresh: true }),
        loadAccountAdminMarketViews(workerUrl, targets),
        canManageUsers ? loadAdminHotReports(workerUrl, targets) : Promise.resolve([]),
        canManageUsers ? loadAdminReportChatHistory(workerUrl, targets) : Promise.resolve([]),
      ]);
      if (canManageUsers && exportUsers) {
        renderAdminUsersVerificationState(targets, "正在现场核验全部用户的最新权限…");
        targets.status.className = "status-line";
        targets.status.textContent = "正在同步读取最新用户状态…";
        try {
          const fresh = await loadFreshAdminUsers(workerUrl, targets);
          targets.status.className = "status-line ok";
          targets.status.textContent = `用户状态已同步：${fresh.users.length} 个用户。`;
        } catch (error) {
          const hasCachedUsers = accountAdminUsersByEmail.size > 0;
          renderAdminUsersVerificationState(
            targets,
            hasCachedUsers
              ? "现场核验暂时失败，当前继续显示最近一次成功数据；编辑单个用户时仍会重新读取最新权限。"
              : (error.message || "最新用户状态读取失败，请稍后重试。"),
            "error",
          );
          targets.status.className = hasCachedUsers ? "status-line ok" : "status-line error";
          targets.status.textContent = hasCachedUsers
            ? "后台已打开；用户表暂时显示最近一次成功数据。"
            : (error.message || "最新用户状态读取失败。");
        }
      }
    });
    if (canManageUsers && reportChatArchiveRefresh) {
      reportChatArchiveRefresh.addEventListener("click", () => loadAdminReportChatHistory(workerUrl, targets));
    }
    if (canManageUsers && reportChatArchiveList) {
      reportChatArchiveList.addEventListener("click", async (event) => {
        const button = event.target.closest("[data-report-chat-curation]");
        if (!button) return;
        const archiveId = String(button.dataset.archiveId || "").trim();
        const action = String(button.dataset.reportChatCuration || "").trim();
        button.disabled = true;
        reportChatArchiveStatus.className = "status-line";
        reportChatArchiveStatus.textContent = action === "unpublish" ? "正在撤下公开问答…" : "正在公开精选问答…";
        try {
          await curateAdminReportChatArchive(workerUrl, archiveId, action);
          reportChatArchiveStatus.className = "status-line ok";
          reportChatArchiveStatus.textContent = action === "unpublish" ? "问答已撤下，正在刷新…" : "问答已公开，正在刷新…";
          await loadAdminReportChatHistory(workerUrl, targets);
        } catch (error) {
          button.disabled = false;
          reportChatArchiveStatus.className = "status-line error";
          reportChatArchiveStatus.textContent = error.message || "问答精选状态更新失败。";
        }
      });
    }
    if (canManageUsers && exportUsers) {
      exportUsers.addEventListener("click", () => exportAdminUsersToExcel(workerUrl, targets));
    }
    if (hotReportDate) {
      hotReportDate.value = shanghaiDateInputValue();
    }
    if (hotReportPdf && hotReportTitle) {
      hotReportPdf.addEventListener("change", () => {
        const file = hotReportPdf.files && hotReportPdf.files[0];
        if (file && !hotReportTitle.value.trim()) {
          hotReportTitle.value = file.name.replace(/\.pdf$/i, "").replace(/[_-]+/g, " ").trim();
        }
      });
    }
    if (hotReportForm) {
      hotReportForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        if (guardUnresolvedIntakeUpload(hotReportStatus)) return;
        const submit = hotReportForm.querySelector("button[type='submit']");
        if (submit) submit.disabled = true;
        hotReportStatus.className = "status-line";
        hotReportStatus.textContent = "正在上传 PDF，请保持页面开启…";
        try {
          const { item } = await uploadAdminHotReport(workerUrl, targets);
          hotReportStatus.className = "status-line ok";
          hotReportStatus.textContent = `已上传：${item.title}`;
          hotReportForm.reset();
          resetAdminPdfUploadId(hotReportPdf);
          if (hotReportDate) hotReportDate.value = String(item.date || "");
          await loadAdminHotReports(workerUrl, targets);
          hotReportStatus.className = "status-line ok";
          hotReportStatus.textContent = `已上传并读回确认：${item.title}`;
        } catch (error) {
          hotReportStatus.className = "status-line error";
          hotReportStatus.textContent = error.message || "热门报告上传失败。";
        } finally {
          if (submit) submit.disabled = false;
        }
      });
    }
    if (accessMode) accessMode.addEventListener("change", () => {
      if (accessMode.value !== "none" && userEditor && userEditor.dataset.originalAccessActive !== "true") {
        prepareExpiredAccessRenewal(targets);
      }
      updateUserAccessEditorMode(targets);
    });
    if (accessDuration) accessDuration.addEventListener("change", () => {
      if (accessMode && accessMode.value !== "none" && accessDuration.value !== "lifetime") {
        prepareExpiredAccessRenewal(targets);
      }
      updateUserAccessEditorMode(targets);
    });
    if (accessInstitutionSearch) {
      accessInstitutionSearch.addEventListener("input", () => {
        filterAccessCheckboxOptions(accessInstitutions, accessInstitutionSearch.value);
      });
    }
    if (accessInstitutions) {
      accessInstitutions.addEventListener("change", (event) => {
        if (selectedAccessCheckboxValues(accessInstitutions).length > 60) {
          if (event.target && event.target.matches("input[type='checkbox']")) event.target.checked = false;
          status.className = "status-line error";
          status.textContent = "机构最多选择 60 项。";
        }
        updateAccessCheckboxCount(accessInstitutions, accessInstitutionCount);
      });
    }
    if (passwordResetEmail && passwordReset) {
      passwordResetEmail.addEventListener("change", () => {
        const submit = passwordReset.querySelector('button[type="submit"]');
        if (submit) submit.disabled = !passwordResetEmail.value;
      });
      passwordReset.addEventListener("submit", async (event) => {
        event.preventDefault();
        const email = String(passwordResetEmail.value || "");
        if (!email) return;
        if (!window.confirm(`确认把 ${email} 的密码重置为 123456？`)) return;
        const submit = passwordReset.querySelector('button[type="submit"]');
        if (submit) submit.disabled = true;
        status.className = "status-line";
        status.textContent = "正在重置用户密码…";
        try {
          await resetAdminUserPassword(workerUrl, email);
          renderAdminUserTable(targets);
          passwordResetEmail.value = "";
          status.className = "status-line ok";
          status.textContent = `已将 ${email} 的密码重置为 123456。`;
        } catch (error) {
          status.className = "status-line error";
          status.textContent = error.message || "密码重置失败。";
        } finally {
          if (submit) submit.disabled = !passwordResetEmail.value;
        }
      });
    }
    if (newUser && userCreator) {
      newUser.addEventListener("click", () => {
        userCreator.hidden = false;
        if (userEditor) userEditor.hidden = true;
        status.className = "status-line ok";
        status.textContent = "正在新增用户。";
        requestAnimationFrame(() => {
          userCreator.scrollIntoView({ block: "nearest", behavior: "smooth" });
          if (newUsername) newUsername.focus({ preventScroll: true });
        });
      });
    }
    if (userCreatorClose && userCreator) {
      userCreatorClose.addEventListener("click", () => {
        userCreator.hidden = true;
      });
    }
    if (userCreator) {
      userCreator.addEventListener("submit", async (event) => {
        event.preventDefault();
        const submit = userCreator.querySelector("button[type='submit']");
        if (submit) submit.disabled = true;
        status.className = "status-line";
        status.textContent = "正在创建用户…";
        try {
          await createAdminUser(workerUrl, targets);
          renderAdminUserTable(targets);
          if (newUsername) newUsername.value = "";
          if (newEmail) newEmail.value = "";
          if (newPassword) newPassword.value = "";
          status.textContent = "用户已创建。";
          status.classList.add("ok");
        } catch (error) {
          status.textContent = error.message || "创建用户失败。";
          status.classList.add("error");
        } finally {
          if (submit) submit.disabled = false;
        }
      });
    }
    if (userEditorClose) {
      userEditorClose.addEventListener("click", () => {
        if (userEditor) userEditor.hidden = true;
      });
    }
    if (users) {
      users.addEventListener("click", async (event) => {
        const toggle = event.target.closest(".account-admin-toggle-user");
        if (toggle) {
          const email = String(toggle.dataset.email || "");
          const disabled = toggle.dataset.disabled === "true";
          toggle.disabled = true;
          status.className = "status-line";
          status.textContent = disabled ? "正在禁用账号…" : "正在启用账号…";
          try {
            await updateAdminUserStatus(workerUrl, email, disabled);
            renderAdminUserTable(targets);
            status.textContent = disabled ? "账号已禁用。" : "账号已启用。";
            status.classList.add("ok");
          } catch (error) {
            status.textContent = error.message || "账号状态更新失败。";
            status.classList.add("error");
          } finally {
            toggle.disabled = false;
          }
          return;
        }
        const button = event.target.closest(".account-admin-edit-user");
        if (!button) return;
        const email = String(button.dataset.email || "");
        button.disabled = true;
        status.className = "status-line";
        status.textContent = "正在读取该用户的最新权限…";
        try {
          const user = await loadAdminUserAccess(workerUrl, email);
          accountAdminUsersByEmail.set(String(user.email || email), user);
          if (userCreator) userCreator.hidden = true;
          fillUserAccessEditor(user, targets);
        } catch (error) {
          status.className = "status-line error";
          status.textContent = error.message || "读取最新用户权限失败，请刷新后台后再试。";
        } finally {
          button.disabled = false;
        }
      });
    }
    if (userEditor) {
      userEditor.addEventListener("submit", async (event) => {
        event.preventDefault();
        const submit = userEditor.querySelector("button[type='submit']");
        if (submit) submit.disabled = true;
        status.className = "status-line";
        status.textContent = "正在保存用户权限…";
        try {
          const result = await saveUserAccess(workerUrl, targets);
          if (result && result.cancelled) {
            status.textContent = "已取消保存，用户权限没有变化。";
            return;
          }
          renderAdminUserTable(targets);
          status.textContent = "用户权限已保存，并已读回确认。";
          status.classList.add("ok");
        } catch (error) {
          status.textContent = error.message || "保存权限失败。";
          status.classList.add("error");
        } finally {
          if (submit) submit.disabled = false;
        }
      });
    }
    picks.addEventListener("click", async (event) => {
      const row = event.target.closest(".account-admin-pick");
      if (!row) return;
      const pick = accountAdminDailyPicks.get(String(row.dataset.id || ""));
      if (!pick) return;

      const copyButton = event.target.closest(".account-admin-copy-intro");
      if (copyButton) {
        const text = String(pick.intro || "");
        try {
          await navigator.clipboard.writeText(text);
          status.className = "status-line ok";
          status.textContent = "文案已复制。";
        } catch (_error) {
          const textarea = row.querySelector(".account-admin-pick-intro");
          if (textarea) textarea.select();
          status.className = "status-line";
          status.textContent = "已选中文案，可以手动复制。";
        }
        return;
      }

      const downloadButton = event.target.closest(".account-admin-report-download");
      const imageButton = event.target.closest(".account-admin-cover-save");
      if (!downloadButton && !imageButton) return;

      const button = downloadButton || imageButton;
      if (cancelActiveAdminButton(button)) {
        status.className = "status-line";
        status.textContent = "正在取消…";
        return;
      }
      const progress = row.querySelector(".account-admin-progress");
      const controller = new AbortController();
      startAdminButtonAction(button, controller);
      resetDownloadProgress(progress);
      status.className = "status-line";
      status.textContent = downloadButton ? "正在下载精选报告…" : "正在读取 PDF 并生成第一页图片…";
      try {
        const blob = await fetchAccountAdminReportBlob(workerUrl, pick, progress, controller.signal);
        if (downloadButton) {
          triggerBlobDownload(blob, "", pick.filename || `${pick.id}.pdf`);
          status.textContent = "报告下载已开始。";
        } else {
          await saveFirstPageImageFromPdfBlob(blob, pick);
          status.textContent = "第一页图片已保存。";
        }
        status.classList.add("ok");
      } catch (error) {
        if (error && error.name === "AbortError") {
          status.textContent = "操作已取消。";
        } else {
          status.textContent = error.message || "操作失败。";
          status.classList.add("error");
        }
      } finally {
        finishAdminButtonAction(button);
      }
    });
    if (marketViews) {
      marketViews.addEventListener("click", (event) => {
        handleAccountAdminMarketViewDownload(event, workerUrl, status);
      });
    }
    files.addEventListener("click", async (event) => {
      const button = event.target.closest(".account-admin-download");
      if (!button) return;
      const kind = button.dataset.kind;
      const key = button.dataset.key || "";
      const repo = button.dataset.repo || "";
      const name = button.dataset.name || "download";
      if (cancelActiveAdminButton(button)) {
        trackEvent(workerUrl, "daily_file_download", {
          target: name,
          source: kind,
          action: "download",
          status: "cancel_requested",
        });
        status.className = "status-line";
        status.textContent = "正在取消下载…";
        return;
      }
      const segmented = (kind === "file" || kind === "artifact") && shouldUseSegmentedDownload(button);
      const endpoint = kind === "artifact"
        ? `${workerUrl}/account-admin/github-artifact?id=${encodeURIComponent(key)}`
        : `${workerUrl}/account-admin/github-file?path=${encodeURIComponent(key)}${repo ? `&repo=${encodeURIComponent(repo)}` : ""}`;
      const row = button.closest(".account-admin-file");
      const progress = row && row.querySelector(".account-admin-progress");
      const controller = new AbortController();
      startAdminButtonAction(button, controller);
      resetDownloadProgress(progress);
      status.className = "status-line";
      status.textContent = segmented ? "正在准备高速缓存…" : "正在准备下载…";
      trackEvent(workerUrl, "daily_file_download", {
        target: name,
        source: kind,
        action: "download",
        status: "attempt",
      });
      let finalLabel = "";
      let finalDelay = 0;
      try {
        let blob;
        let disposition = "";
        if (segmented && isVideoDownloadButton(button)) {
          const directUrl = withDownloadToken(endpoint);
          try {
            status.textContent = "正在准备高速缓存，首次视频可能需要几十秒…";
            setDownloadMessage(progress, "正在准备高速缓存，首次视频可能需要几十秒…", 8);
            await prepareSegmentedAdminDownload(workerUrl, button, controller.signal, progress, { timeoutMs: 90000 });
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            status.textContent = "缓存准备较慢，正在尝试分段下载…";
          }
          try {
            status.textContent = "正在从高速缓存分段下载…";
            setDownloadMessage(progress, "正在从高速缓存分段下载…", 10);
            blob = await segmentedAdminDownload(endpoint, name, progress, controller.signal, { firstChunkTimeoutMs: 30000 });
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            setDownloadMessage(progress, "高速缓存仍未就绪，已切换浏览器下载。", 18);
            triggerNativeDownload(directUrl, name);
            trackEvent(workerUrl, "daily_file_download", {
              target: name,
              source: kind,
              action: "download",
              status: "browser_download_started",
            });
            status.textContent = "已切换浏览器下载。";
            status.classList.add("ok");
            finalLabel = "已切换";
            finalDelay = 1600;
            return;
          }
        } else if (segmented) {
          try {
            await prepareSegmentedAdminDownload(workerUrl, button, controller.signal, progress);
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            status.textContent = "高速缓存准备较慢，正在改用直接下载…";
          }
          status.textContent = "正在分段下载…";
          blob = await segmentedAdminDownload(endpoint, name, progress, controller.signal);
        } else {
          const response = await fetch(endpoint, { headers: authHeaders(), signal: controller.signal });
          if (!response.ok) {
            const data = await response.json().catch(() => ({}));
            throw new Error(data.detail || `下载失败 (${response.status})。`);
          }
          disposition = response.headers.get("Content-Disposition") || "";
          blob = await responseBlobWithProgress(response, progress);
        }
        triggerBlobDownload(blob, disposition, name);
        trackEvent(workerUrl, "daily_file_download", {
          target: name,
          source: kind,
          action: "download",
          status: "success",
        });
        status.textContent = "下载已开始。";
        status.classList.add("ok");
      } catch (error) {
        if (error && error.name === "AbortError") {
          trackEvent(workerUrl, "daily_file_download", {
            target: name,
            source: kind,
            action: "download",
            status: "cancelled",
          });
          status.textContent = "下载已取消。";
        } else {
          trackEvent(workerUrl, "daily_file_download", {
            target: name,
            source: kind,
            action: "download",
            status: "error",
            error: error && error.message || "download_failed",
          });
          status.textContent = error.message || "下载失败。";
          status.classList.add("error");
        }
      } finally {
        finishAdminButtonAction(button, finalLabel, finalDelay);
      }
    });

    loadAccountAdminSummary(workerUrl, targets).then(() => {
      if (canManageUsers && exportUsers && document.getElementById("accountAdminModal")) {
        renderAdminUsersVerificationState(targets, "正在现场核验全部用户的最新权限…");
        return loadFreshAdminUsers(workerUrl, targets).catch((error) => {
          const hasCachedUsers = accountAdminUsersByEmail.size > 0;
          renderAdminUsersVerificationState(
            targets,
            hasCachedUsers
              ? "现场核验暂时失败，当前继续显示最近一次成功数据；编辑单个用户时仍会重新读取最新权限。"
              : (error.message || "最新用户状态读取失败，请点击刷新重试。"),
            "error",
          );
          targets.status.className = hasCachedUsers ? "status-line ok" : "status-line error";
          targets.status.textContent = hasCachedUsers
            ? "后台已打开；用户表暂时显示最近一次成功数据。"
            : (error.message || "最新用户状态读取失败，请点击刷新重试。");
          return null;
        });
      }
      return null;
    }).catch(() => null);
    loadAccountAdminMarketViews(workerUrl, targets).catch(() => null);
    if (canManageUsers) {
      loadAdminHotReports(workerUrl, targets);
      loadAdminReportChatHistory(workerUrl, targets);
    }
  }

  function adminModalMarkup() {
    return `
      <div class="admin-modal" id="adminModal" role="dialog" aria-modal="true" aria-labelledby="adminModalTitle">
        <div class="admin-dialog">
          <button class="admin-close" id="adminClose" type="button" aria-label="Close">&times;</button>
          <h3 id="adminModalTitle">Private tools</h3>
          <form id="adminLoginForm">
            <label class="search-box">
              <span>Key</span>
              <input id="adminKeyInput" type="password" autocomplete="current-password" required>
            </label>
            <button class="primary" type="submit">Unlock</button>
            <div id="adminLoginStatus" class="status-line" aria-live="polite"></div>
          </form>
        </div>
      </div>
    `;
  }

  function showAdminLogin(workerUrl) {
    if (!workerUrl) {
      window.alert("Private tools are temporarily unavailable.");
      return Promise.resolve("");
    }

    const existing = document.getElementById("adminModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", adminModalMarkup());

    const modal = document.getElementById("adminModal");
    const form = document.getElementById("adminLoginForm");
    const input = document.getElementById("adminKeyInput");
    const status = document.getElementById("adminLoginStatus");
    const close = document.getElementById("adminClose");
    const button = form.querySelector("button");
    input.focus();

    return new Promise((resolve) => {
      function finish(token) {
        modal.remove();
        resolve(token || "");
      }

      close.addEventListener("click", () => finish(""));
      modal.addEventListener("click", (event) => {
        if (event.target === modal) finish("");
      });
      form.addEventListener("submit", async (event) => {
        event.preventDefault();
        button.disabled = true;
        status.className = "status-line";
        status.textContent = "Checking...";
        try {
          const response = await fetch(`${workerUrl}/admin/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ key: input.value }),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(data.error || "Private key is incorrect.");
          setAdminToken(data.token, data.expires_at);
          setAdminPlainKey(input.value);
          finish(data.token);
        } catch (error) {
          status.textContent = error.message || "Unlock failed.";
          status.classList.add("error");
        } finally {
          button.disabled = false;
        }
      });
    });
  }

  function getRememberedDownloadPassword(reportId = "") {
    reportId = String(reportId || "");
    try {
      if (reportId) {
        const scoped = localStorage.getItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`) || "";
        if (scoped) return scoped;
      }
      return localStorage.getItem(DOWNLOAD_PASSWORD_KEY) || "";
    } catch (_error) {
      return "";
    }
  }

  function setRememberedDownloadPassword(value, reportId = "") {
    reportId = String(reportId || "");
    const password = String(value || "");
    try {
      localStorage.setItem(DOWNLOAD_PASSWORD_KEY, password);
      if (reportId) localStorage.setItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`, password);
    } catch (_error) {
      // Ignore private browsing/localStorage restrictions.
    }
    try {
      if (reportId) sessionStorage.setItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`, password);
    } catch (_error) {
      // Ignore private browsing/sessionStorage restrictions.
    }
  }

  function clearRememberedDownloadPassword(reportId = "") {
    reportId = String(reportId || "");
    try {
      localStorage.removeItem(DOWNLOAD_PASSWORD_KEY);
      if (reportId) localStorage.removeItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`);
    } catch (_error) {
      // Ignore private browsing/localStorage restrictions.
    }
    try {
      if (reportId) sessionStorage.removeItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`);
    } catch (_error) {
      // Ignore private browsing/sessionStorage restrictions.
    }
  }

  function deliveryPasswordFromLocation(params) {
    const query = params || new URLSearchParams(window.location.search);
    const fromQuery = query.get("password") || "";
    if (fromQuery) return fromQuery;
    const hash = String(window.location.hash || "").replace(/^#\??/, "");
    return hash ? new URLSearchParams(hash).get("password") || "" : "";
  }

  function deliveryPasswordFromHistory(reportId) {
    const state = window.history.state;
    if (!state || typeof state !== "object") return "";
    const savedId = String(state.portalDeliveryReportId || "");
    if (savedId && reportId && savedId !== String(reportId)) return "";
    return String(state.portalDeliveryPassword || "");
  }

  function getRecoverableDownloadPassword(reportId, explicitPassword) {
    const direct = String(explicitPassword || deliveryPasswordFromLocation() || "");
    if (direct) return direct;
    const fromHistory = deliveryPasswordFromHistory(reportId);
    if (fromHistory) return fromHistory;
    try {
      const fromSession = sessionStorage.getItem(`${DOWNLOAD_PASSWORD_KEY}:${reportId}`) || "";
      if (fromSession) return fromSession;
    } catch (_error) {
      // Ignore private browsing/sessionStorage restrictions.
    }
    return getRememberedDownloadPassword(reportId);
  }

  function rememberDeliveryPassword(reportId, value) {
    const password = String(value || "");
    if (!password) return;
    setRememberedDownloadPassword(password, reportId);
    try {
      const current = window.history.state && typeof window.history.state === "object"
        ? window.history.state
        : {};
      window.history.replaceState({
        ...current,
        portalDeliveryReportId: String(reportId || ""),
        portalDeliveryPassword: password,
      }, "", window.location.href);
    } catch (_error) {
      // The URL remains the primary fallback when history state is unavailable.
    }
  }

  function initResilientPasswordInput(input, reportId, explicitPassword, setStatus) {
    if (!input) return "";
    const linkedPassword = String(explicitPassword || "");
    const initialPassword = getRecoverableDownloadPassword(reportId, linkedPassword);
    if (initialPassword) {
      input.value = initialPassword;
      rememberDeliveryPassword(reportId, initialPassword);
      setStatus(linkedPassword
        ? "Password filled from delivery link."
        : "Password restored on this device.");
    }

    const restoreIfEmpty = () => {
      if (!input.isConnected || input.value) return;
      const recovered = getRecoverableDownloadPassword(reportId, linkedPassword);
      if (!recovered) return;
      input.value = recovered;
      setStatus("Password restored from delivery link.");
    };

    window.addEventListener("pageshow", restoreIfEmpty);
    window.addEventListener("focus", restoreIfEmpty);
    document.addEventListener("visibilitychange", () => {
      if (!document.hidden) restoreIfEmpty();
    });
    [0, 250, 1200, 2500].forEach((delay) => window.setTimeout(restoreIfEmpty, delay));
    return initialPassword;
  }

  function initAdminGate(workerUrl) {
    const gate = document.getElementById("adminGate");
    if (!gate) return;
    function update() {
      const unlocked = isSuperSession();
      gate.hidden = !unlocked;
      gate.classList.toggle("is-unlocked", unlocked);
    }
    update();
    document.addEventListener("portal-admin-change", update);
    document.addEventListener("portal-auth-change", update);
    gate.addEventListener("click", () => {
      if (isSuperSession()) showAccountAdminModal(workerUrl);
    });
  }

  function formatSize(bytes) {
    const size = Number(bytes || 0);
    if (!size) return "";
    if (size >= 1024 * 1024 * 1024) return `${(size / 1024 / 1024 / 1024).toFixed(1)} GB`;
    if (size >= 1024 * 1024) return `${(size / 1024 / 1024).toFixed(1)} MB`;
    if (size >= 1024) return `${Math.round(size / 1024)} KB`;
    return `${size} B`;
  }

  function contactReportStorageMetaText(metadata) {
    if (!metadata || typeof metadata !== "object" || Array.isArray(metadata)) return "";
    const hasNumber = (key) => Object.prototype.hasOwnProperty.call(metadata, key)
      && Number.isFinite(Number(metadata[key]))
      && Number(metadata[key]) >= 0;
    const hasSize = hasNumber("contact_report_size_bytes");
    const hasLimit = hasNumber("contact_report_limit_bytes");
    const hasCount = hasNumber("contact_report_count");
    if (!hasSize && !hasLimit && !hasCount) return "";
    const sizeText = hasSize ? formatSize(metadata.contact_report_size_bytes) || "0 B" : "";
    const limitText = hasLimit ? formatSize(metadata.contact_report_limit_bytes) || "0 B" : "";
    const countText = hasCount ? `${Math.floor(Number(metadata.contact_report_count))} contact reports` : "";
    let archiveText = "";
    if (sizeText && limitText) archiveText = `${sizeText} / ${limitText} contact archive`;
    else if (sizeText) archiveText = `${sizeText} contact archive`;
    else if (limitText) archiveText = `${limitText} contact archive limit`;
    return [countText, archiveText].filter(Boolean).join(" · ");
  }

  function isoDateFromValue(value) {
    const text = String(value || "");
    if (/^\d{6}$/.test(text)) {
      return `20${text.slice(0, 2)}-${text.slice(2, 4)}-${text.slice(4, 6)}`;
    }
    if (/^\d{8}$/.test(text)) {
      return `${text.slice(0, 4)}-${text.slice(4, 6)}-${text.slice(6, 8)}`;
    }
    const iso = text.match(/^(\d{4})-(\d{2})-(\d{2})/);
    return iso ? `${iso[1]}-${iso[2]}-${iso[3]}` : "";
  }

  function displayDate(value) {
    return isoDateFromValue(value) || String(value || "") || "-";
  }

  function itemDate(item) {
    return isoDateFromValue(item.date_folder) || isoDateFromValue(item.client_modified) || "";
  }

  function dateSortValue(item) {
    return Number(itemDate(item).replace(/-/g, "")) || 0;
  }

  function bankKey(item) {
    return String(item.bank_code || item.bank_name || "Other").trim() || "Other";
  }

  function bankLabel(item) {
    const code = String(item.bank_code || "").trim();
    const name = String(item.bank_name || "").trim();
    if (code && name && normalize(code) !== normalize(name)) return publicBrandText(`${code} · ${name}`, "Other");
    return publicBrandText(code || name, "Other");
  }

  function titleText(item) {
    return publicBrandText(item.title || item.filename, "Untitled report");
  }

  function titleZhText(item) {
    return publicBrandText(item.title_zh);
  }

  function inferIndustry(item) {
    const explicit = item.industry || item.sector || item.category;
    if (explicit) return publicBrandText(explicit, "Other");
    const text = normalize([item.title, item.title_zh, item.filename].join(" "));
    for (const [label, pattern] of INDUSTRY_RULES) {
      if (pattern.test(text)) return label;
    }
    return "Other";
  }

  function isPdfAvailable(item) {
    return item.available !== false;
  }

  function mergeCatalogPdfOverrides(items, overrides) {
    const merged = (Array.isArray(items) ? items : []).map((item) => ({ ...item }));
    const byId = new Map(merged.map((item) => [String(item.id || ""), item]));
    for (const override of Array.isArray(overrides) ? overrides : []) {
      const id = String(override && override.id || "").trim();
      const item = byId.get(id);
      if (!item || item.available !== false || !override || override.available !== true) continue;
      const sizeBytes = Math.max(0, Number(override.size_bytes || 0) || 0);
      if (!sizeBytes) continue;
      Object.assign(item, {
        available: true,
        pdf_archived: false,
        archive_reason: "",
        manual_pdf: true,
        size_bytes: sizeBytes,
        pdf_uploaded_at: String(override.uploaded_at || ""),
      });
    }
    return merged;
  }

  async function loadCatalogPdfOverrides(workerUrl) {
    if (!workerUrl) return [];
    const controller = new AbortController();
    const timeout = window.setTimeout(() => controller.abort(), 6000);
    try {
      const response = await fetch(`${workerUrl}/catalog-pdf-overrides`, {
        cache: "no-store",
        signal: controller.signal,
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.detail || "PDF override status is unavailable.");
      return Array.isArray(data.items) ? data.items : [];
    } catch (_error) {
      return [];
    } finally {
      window.clearTimeout(timeout);
    }
  }

  function metadataText(item) {
    return normalize([
      item.title,
      item.title_zh,
      item.filename,
      item.bank_code,
      item.bank_name,
      inferIndustry(item),
      item.date_folder,
      (item.date_folders || []).join(" "),
      item.client_modified,
      item.server_modified,
    ].join(" "));
  }

  function selectedSearchText(item, queryScope, metadataById, searchTextById, chartTextById, titleSearchById) {
    const id = String(item && item.id || "");
    const title = titleSearchById && titleSearchById.get(id)
      || normalize([item.title, item.title_zh, item.filename].join(" "));
    const catalog = metadataById.get(id) || "";
    const fullText = searchTextById.get(id) || "";
    const chartText = chartTextById && chartTextById.get(id) || "";
    if (queryScope === "title") return { title, catalog: "", fullText: "", combined: title };
    if (queryScope === "catalog") return { title: "", catalog, fullText: "", combined: catalog };
    if (queryScope === "fulltext") return { title: "", catalog: "", fullText, combined: fullText };
    if (queryScope === "charts") return { title: "", catalog: "", fullText: chartText, combined: chartText };
    return { title, catalog, fullText, combined: `${title} ${catalog} ${fullText} ${chartText}` };
  }

  function scoreItem(item, query, queryScope, metadataById, searchTextById, chartTextById, titleSearchById) {
    if (!query) return 0;
    const selected = selectedSearchText(item, queryScope, metadataById, searchTextById, chartTextById, titleSearchById);
    if (!textMatches(selected.combined, query)) return -1;
    return (
      scoreText(selected.title, query, 12) +
      scoreText(selected.catalog, query, 5) +
      scoreText(selected.fullText, query, 2)
    );
  }

  function reportPageCountValue(item) {
    const pages = Number(item && item.page_count);
    return Number.isFinite(pages) && pages > 0 ? pages : 0;
  }

  function pageRangeForValue(value) {
    return PAGE_RANGE_FILTERS.find((range) => range.value === value) || null;
  }

  function authorityPageRangeForValue(value) {
    return AUTHORITY_PAGE_RANGE_FILTERS.find((range) => range.value === value) || null;
  }

  function pageRangeLabel(value) {
    const range = pageRangeForValue(value);
    return range ? range.label : "";
  }

  function itemMatchesPageRanges(item, selectedRanges) {
    if (!selectedRanges.length) return true;
    const pages = reportPageCountValue(item);
    if (!pages) return false;
    return selectedRanges.some((value) => {
      const range = pageRangeForValue(value);
      return range ? range.matches(pages) : false;
    });
  }

  function resultRow(item) {
    const bank = publicBrandText(item.bank_code || item.bank_name, "Other");
    const size = formatSize(item.size_bytes);
    const industry = inferIndustry(item);
    const available = isPdfAvailable(item);
    const pages = reportPageCountValue(item);
    const statusParts = [
      pages ? `${pages}页` : "",
      available ? size : "Text only",
    ].filter(Boolean);
    const status = statusParts.join(" · ");
    const zh = titleZhText(item);
    const url = reportPageUrl(item.id, { preview: item });
    return `
      <a class="report-row report-link${available ? "" : " is-archived"}" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="pill">${escapeHtml(bank)}</span>
        <span class="date-text">${escapeHtml(displayDate(item.date_folder))}</span>
        <span class="title-text">
          <span class="title-en">${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="industry-text">${escapeHtml(industry)}</span>
        <span class="size-text${available ? "" : " archived"}">${escapeHtml(status)}</span>
      </a>
    `;
  }

  function relatedRow(item) {
    const available = isPdfAvailable(item);
    const zh = titleZhText(item);
    const url = reportPageUrl(item.id, { preview: item });
    return `
      <a class="related-row report-link${available ? "" : " is-archived"}" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(bankLabel(item))} · ${escapeHtml(displayDate(item.date_folder))} · ${escapeHtml(inferIndustry(item))}${available ? "" : " · Text only"}</span>
      </a>
    `;
  }

  function externalMeta(item) {
    const meta = [item.institution, item.date, item.file_type]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
    return meta;
  }

  function hasMeaningfulDocTitle(item) {
    return [item && item.title, item && item.title_cn]
      .map((value) => String(value || "").trim())
      .some((value) => Boolean(value && !/^(?:report|报告)$/i.test(value)));
  }

  function mergeDocItemMetadata(...records) {
    const merged = {};
    for (const record of records) {
      if (!record || typeof record !== "object") continue;
      for (const [key, value] of Object.entries(publicDocItem(record))) {
        if (value === undefined || value === null) continue;
        if (typeof value === "string" && !value.trim()) continue;
        if ((key === "title" || key === "title_cn") && !hasMeaningfulDocTitle({ [key]: value })) continue;
        if (typeof value === "number" && !Number.isFinite(value)) continue;
        merged[key] = value;
      }
    }
    return merged;
  }

  function reportRequestTitle(item) {
    const title = [item && item.title, item && item.title_cn]
      .map((value) => publicBrandText(value))
      .find((value) => value && !/^(?:report|报告)$/i.test(value));
    if (title) return title;
    const source = isAuthorityItem(item) ? "高权报告" : (isReportAItem(item) ? "报告A" : "报告");
    const id = String(item && item.id || "").trim();
    return id ? `${source}（编号：${id}）` : source;
  }

  function docItemCacheKey(item) {
    return `${String(item && item.source || EXTERNAL_SOURCE)}:${String(item && item.id || "")}`;
  }

  function readDocItemCache() {
    try {
      const parsed = JSON.parse(localStorage.getItem(DOC_ITEM_CACHE_KEY) || "{}");
      return parsed && typeof parsed === "object" ? parsed : {};
    } catch (_error) {
      return {};
    }
  }

  function writeDocItemCache(cache) {
    try {
      localStorage.setItem(DOC_ITEM_CACHE_KEY, JSON.stringify(cache));
    } catch (_error) {
      // The detail page can still fetch by id from the Worker.
    }
  }

  function rememberDocItem(item) {
    if (!item || !item.id) return;
    item = publicDocItem(item);
    const cache = readDocItemCache();
    const cacheKey = docItemCacheKey(item);
    const previous = cache[cacheKey] && cache[cacheKey].item && typeof cache[cacheKey].item === "object"
      ? cache[cacheKey].item
      : null;
    const remembered = mergeDocItemMetadata(previous, item);
    cache[docItemCacheKey(item)] = {
      saved_at: Date.now(),
      item: {
        id: item.id,
        source: item.source || EXTERNAL_SOURCE,
        title: remembered.title || "",
        title_cn: remembered.title_cn || "",
        institution: remembered.institution || "",
        date: remembered.date || "",
        file_type: remembered.file_type || "",
        kind: remembered.kind || "",
        kind_label: remembered.kind_label || "",
        page_count: remembered.page_count || "",
        size_bytes: remembered.size_bytes || 0,
        report_type: remembered.report_type || "",
        language: remembered.language || "",
        category: remembered.category || "",
        author: remembered.author || "",
        rating: remembered.rating || "",
        description: remembered.description || "",
        filename: remembered.filename || "",
        required_plan: remembered.required_plan || "",
      },
    };
    const entries = Object.entries(cache)
      .filter(([, value]) => Date.now() - Number(value && value.saved_at || 0) < 7 * 24 * 60 * 60 * 1000)
      .sort((a, b) => Number(b[1].saved_at || 0) - Number(a[1].saved_at || 0))
      .slice(0, 80);
    writeDocItemCache(Object.fromEntries(entries));
  }

  function cachedDocItem(item) {
    if (!item || !item.id) return null;
    const cached = readDocItemCache()[docItemCacheKey(item)];
    if (!cached || Date.now() - Number(cached.saved_at || 0) > 7 * 24 * 60 * 60 * 1000) return null;
    return cached.item && typeof cached.item === "object" ? publicDocItem(cached.item) : null;
  }

  function authorityKindLabel(kind, kindLabel = "") {
    if (String(kindLabel || "").trim()) return publicBrandText(kindLabel);
    if (kind === "domestic-lead") return "国内报告线索";
    return kind === "foreign-rt" ? "实时外文" : "普通外文";
  }

  function authorityMeta(item) {
    const meta = [
      authorityKindLabel(item.kind, item.kind_label),
      item.institution,
      item.date,
      item.page_count ? `${item.page_count}页` : "",
      item.language,
    ]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
    return meta;
  }

  function externalRow(item) {
    item = publicSearchItem(item, EXTERNAL_SOURCE);
    const meta = externalMeta(item);
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    rememberDocItem({ ...item, source: EXTERNAL_SOURCE });
    const url = externalPageUrl(item, "");
    return `
      <a class="related-row external-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function thinkTankMeta(item) {
    return [
      item.institution,
      item.date,
      item.page_count ? `${item.page_count}页` : "",
      formatSize(item.size_bytes),
      item.file_type,
    ]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
  }

  function thinkTankRow(item) {
    item = publicSearchItem(item, THINKTANK_SOURCE);
    const meta = thinkTankMeta(item);
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    const docItem = { ...item, source: THINKTANK_SOURCE };
    rememberDocItem(docItem);
    const url = externalPageUrl(docItem, "");
    return `
      <a class="related-row thinktank-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function hotReportRow(item) {
    item = publicSearchItem(item, HOT_REPORT_SOURCE);
    const docItem = { ...item, source: HOT_REPORT_SOURCE };
    rememberDocItem(docItem);
    const url = externalPageUrl(docItem, "");
    const meta = [
      item.institution,
      item.date,
      formatSize(item.size_bytes),
      "3个月及以上会员",
    ].map((value) => String(value || "").trim()).filter(Boolean).join(" · ");
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    return `
      <a class="related-row hot-report-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title || "近期热门报告")}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function reportAMeta(item) {
    return [
      item.institution,
      item.date,
      item.category,
      item.page_count ? `${item.page_count}页` : "",
      item.author,
    ]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
  }

  function reportARow(item) {
    item = publicSearchItem(item, REPORT_A_SOURCE);
    const meta = reportAMeta(item);
    const docItem = { ...item, source: REPORT_A_SOURCE };
    rememberDocItem(docItem);
    const url = externalPageUrl(docItem, "");
    return `
      <a class="related-row report-a-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function authorityRow(item) {
    item = publicSearchItem(item, AUTHORITY_SOURCE);
    const meta = authorityMeta(item);
    const docItem = { ...item, source: AUTHORITY_SOURCE };
    rememberDocItem(docItem);
    const url = externalPageUrl(docItem, "");
    return `
      <a class="related-row authority-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function isNativeNewTabLink(row) {
    return row && row.tagName === "A" && row.getAttribute("target") === "_blank" && row.getAttribute("href");
  }

  function setOptions(select, options, allLabel) {
    const current = select.value;
    const rows = [`<option value="">${escapeHtml(allLabel)}</option>`];
    for (const option of options) {
      rows.push(`<option value="${escapeHtml(option.value)}">${escapeHtml(option.label)}</option>`);
    }
    select.innerHTML = rows.join("");
    if ([...select.options].some((option) => option.value === current)) {
      select.value = current;
    }
  }

  function optionSummary(map) {
    return [...map.entries()]
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([value, data]) => ({
        value,
        label: `${data.label} (${data.count})`,
      }));
  }

  async function initIndex() {
    const input = document.getElementById("searchInput");
    const results = document.getElementById("results");
    const count = document.getElementById("resultCount");
    const meta = document.getElementById("catalogMeta");
    const searchReadiness = document.getElementById("searchReadiness");
    const searchReadinessText = document.getElementById("searchReadinessText");
    const searchSourceProgress = document.getElementById("searchSourceProgress");
    const searchSourceProgressSummary = document.getElementById("searchSourceProgressSummary");
    const searchSourceProgressBar = document.getElementById("searchSourceProgressBar");
    const searchSourceProgressItems = document.getElementById("searchSourceProgressItems");
    const bankFilter = document.getElementById("bankFilter");
    const industryFilter = document.getElementById("industryFilter");
    const startDate = document.getElementById("startDate");
    const endDate = document.getElementById("endDate");
    const scopeFilter = document.getElementById("scopeFilter");
    const availabilityFilter = document.getElementById("availabilityFilter");
    const pageRangeInputs = Array.from(document.querySelectorAll('input[name="pageRange"]'));
    const externalDateFilter = document.getElementById("externalDateFilter");
    const externalIncludeHtml = document.getElementById("externalIncludeHtml");
    const authorityInstitutionFilter = document.getElementById("authorityInstitutionFilter");
    const authorityDateFilter = document.getElementById("authorityDateFilter");
    const authorityPageFilter = document.getElementById("authorityPageFilter");
    const clearFilters = document.getElementById("clearFilters");
    const activeFilters = document.getElementById("activeFilters");
    const prevPage = document.getElementById("prevPage");
    const nextPage = document.getElementById("nextPage");
    const pageInfo = document.getElementById("pageInfo");
    const pageSize = document.getElementById("pageSize");
    let earlyInputTouched = false;
    const captureEarlyInput = () => { earlyInputTouched = true; };
    if (input) input.addEventListener("input", captureEarlyInput, { passive: true });

    let fullCatalogError = null;
    const [previewCatalog, config] = await Promise.all([
      loadOptionalJson("data/catalog_preview.json", null),
      loadOptionalJson("data/config.json", {}),
    ]);
    let fullCatalogPromise = null;
    const startFullCatalogLoad = () => {
      if (!fullCatalogPromise) {
        fullCatalogPromise = loadJson("data/catalog.json").catch((error) => {
          fullCatalogError = error;
          return null;
        });
      }
      return fullCatalogPromise;
    };
    // The small preview owns first paint. On a normal home load the large
    // catalog starts only after the first hot-report request has been issued.
    let catalog = previewCatalog && Array.isArray(previewCatalog.items) && previewCatalog.items.length
      ? previewCatalog
      : await startFullCatalogLoad();
    if (!catalog || !Array.isArray(catalog.items)) {
      throw fullCatalogError || new Error("Report catalog is unavailable.");
    }
    let fullCatalogReady = !(previewCatalog && Array.isArray(previewCatalog.items) && previewCatalog.items.length);
    const workerUrl = workerBaseUrl(config);
    let items = mergeCatalogPdfOverrides(catalog.items, []);
    let catalogById = new Map(items.map((item) => [String(item.id || ""), item]));
    let metadataById = new Map(items.map((item) => [String(item.id || ""), metadataText(item)]));
    let titleSearchById = new Map(items.map((item) => [String(item.id || ""), normalize([item.title, item.title_zh, item.filename].join(" "))]));
    let dateSortById = new Map(items.map((item) => [String(item.id || ""), dateSortValue(item)]));
    let itemDateById = new Map(items.map((item) => [String(item.id || ""), itemDate(item)]));
    let bankKeyById = new Map(items.map((item) => [String(item.id || ""), bankKey(item)]));
    let pageCountById = new Map(items.map((item) => [String(item.id || ""), reportPageCountValue(item)]));
    let industryById = new Map(items.map((item) => [String(item.id || ""), inferIndustry(item)]));
    const searchTextById = new Map();
    const chartTextById = new Map();
    const chartSearchSection = document.getElementById("chartSearchSection");
    const chartSearchResults = document.getElementById("chartSearchResults");
    const chartSearchCount = document.getElementById("chartSearchCount");
    const chartSearchStatus = document.getElementById("chartSearchStatus");
    let chartSearchReports = [];
    let chartSearchPromise = null;
    let searchIndexLabel = "Title and catalog search ready";
    let currentPage = 1;
    let catalogAnalyticsTimer = 0;
    let lastCatalogAnalyticsKey = "";
    let showInternalStorageMetadata = false;
    let internalStorageMetadata = null;
    let internalStorageRequestId = 0;

    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();
    trackEvent(workerUrl, "page_view", { page: "home", report_count: items.length });

    const hotReportsSection = document.getElementById("hotReportsSection");
    const hotReportsResults = document.getElementById("hotReportsResults");
    const hotReportsCount = document.getElementById("hotReportsCount");
    const hotReportsStatus = document.getElementById("hotReportsStatus");
    const hotReportsPagination = document.getElementById("hotReportsPagination");
    const hotReportsPrev = document.getElementById("hotReportsPrev");
    const hotReportsNext = document.getElementById("hotReportsNext");
    const hotReportsPageInfo = document.getElementById("hotReportsPageInfo");
    const hotReportsRetry = document.getElementById("hotReportsRetry");
    const searchRecommendationsSection = document.getElementById("searchRecommendationsSection");
    const searchRecommendationsResults = document.getElementById("searchRecommendationsResults");
    const searchRecommendationsCount = document.getElementById("searchRecommendationsCount");
    const hotReportItems = new Map();
    const searchResultCounts = {
      catalog: 0,
      hot: workerUrl ? null : 0,
      thinktank: 0,
      external: 0,
      reportA: 0,
      authority: 0,
    };
    const HOT_REPORT_PAGE_SIZE = 24;
    let hotReportsLoaded = !workerUrl;
    let hotReportsLoading = false;
    let hotReportsFailed = false;
    let hotReportActiveQuery = "";
    let hotReportRequestedQuery = "";
    let hotReportPageIndex = 0;
    let hotReportPages = [];
    let hotReportSearchTimer = 0;
    let hotReportRequestVersion = 0;
    let hotReportRequestController = null;
    let hotReportRetryQuery = null;
    let fallbackRecommendations = items
      .filter((item) => isPdfAvailable(item))
      .slice()
      .sort((left, right) => dateSortValue(right) - dateSortValue(left))
      .slice(0, 6);

    function setHotReportsStatus(text, kind) {
      if (!hotReportsStatus) return;
      hotReportsStatus.className = kind ? `status-line ${kind}` : "status-line";
      hotReportsStatus.textContent = text || "";
    }

    function renderSearchRecommendations() {
      if (!searchRecommendationsSection || !searchRecommendationsResults) return;
      const query = String(input.value || "").trim();
      const counts = Object.values(searchResultCounts);
      const settled = (value) => Number.isFinite(value) || value === "error";
      const ready = counts.every(settled);
      const noMatches = ready && counts.every((value) => value === "error" || value === 0);
      if (!query || !noMatches || !fallbackRecommendations.length) {
        searchRecommendationsSection.hidden = true;
        searchRecommendationsResults.innerHTML = "";
        if (searchRecommendationsCount) searchRecommendationsCount.textContent = "";
        return;
      }
      searchRecommendationsSection.hidden = false;
      if (searchRecommendationsCount) searchRecommendationsCount.textContent = `${fallbackRecommendations.length} 条`;
      searchRecommendationsResults.innerHTML = fallbackRecommendations.map(relatedRow).join("");
    }

    function chartRecordText(chart) {
      const row = chart && typeof chart === "object" ? chart : {};
      return normalize([
        publicBrandText(row.title),
        publicBrandText(row.chart_type),
        publicBrandText(row.description),
        publicBrandText(row.trend_summary),
        ...(Array.isArray(row.metrics) ? row.metrics.map((value) => publicBrandText(value)) : []),
        ...(Array.isArray(row.entities) ? row.entities.map((value) => publicBrandText(value)) : []),
        ...(Array.isArray(row.periods) ? row.periods.map((value) => publicBrandText(value)) : []),
        ...(Array.isArray(row.geographies) ? row.geographies.map((value) => publicBrandText(value)) : []),
        ...(Array.isArray(row.units) ? row.units.map((value) => publicBrandText(value)) : []),
        ...(Array.isArray(row.keywords) ? row.keywords.map((value) => publicBrandText(value)) : []),
      ].filter(Boolean).join(" "));
    }

    function chartReportText(report) {
      const row = report && typeof report === "object" ? report : {};
      return normalize([
        publicBrandText(row.title),
        publicBrandText(row.search_text),
        ...(Array.isArray(row.charts) ? row.charts.map(chartRecordText) : []),
      ].filter(Boolean).join(" "));
    }

    function chartDetailChips(chart) {
      const values = [
        ...(Array.isArray(chart.metrics) ? chart.metrics : []),
        ...(Array.isArray(chart.entities) ? chart.entities : []),
        ...(Array.isArray(chart.periods) ? chart.periods : []),
        ...(Array.isArray(chart.geographies) ? chart.geographies : []),
        ...(Array.isArray(chart.units) ? chart.units : []),
      ].map((value) => publicBrandText(value)).filter(Boolean);
      return [...new Set(values)].slice(0, 8)
        .map((value) => `<span>${escapeHtml(value)}</span>`)
        .join("");
    }

    function chartSearchRow(report, chart) {
      const reportId = String(report.report_id || "");
      const catalogItem = catalogById.get(reportId);
      const reportTitle = publicBrandText(report.title || catalogItem && titleText(catalogItem), "图表所在报告");
      const title = publicBrandText(chart.title || chart.description, "报告图表");
      const summary = publicBrandText(chart.description || chart.trend_summary);
      const trend = publicBrandText(chart.trend_summary);
      const reportPreview = publicDocItem(catalogItem || { ...report, id: reportId, title: reportTitle });
      return `
        <a class="chart-search-card" href="${escapeHtml(reportPageUrl(reportId, { preview: reportPreview }))}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(reportId)}">
          <span class="chart-search-kicker">${escapeHtml(publicBrandText(chart.chart_type, "CHART"))}</span>
          <strong>${escapeHtml(title)}</strong>
          ${summary ? `<p>${escapeHtml(summary)}</p>` : ""}
          ${trend && trend !== summary ? `<p class="chart-search-trend">趋势：${escapeHtml(trend)}</p>` : ""}
          <span class="chart-search-report">来自：${escapeHtml(reportTitle)}</span>
          <span class="chart-search-chips">${chartDetailChips(chart)}</span>
        </a>
      `;
    }

    async function ensureChartSearchIndex() {
      if (chartSearchPromise) return chartSearchPromise;
      chartSearchPromise = loadOptionalJson("data/chart_search_index.json", { reports: [] })
        .then((payload) => {
          chartSearchReports = (Array.isArray(payload && payload.reports) ? payload.reports : [])
            .filter((report) => Boolean(String(report && report.report_id || "")));
          chartTextById.clear();
          chartSearchReports.forEach((report) => {
            const reportId = String(report && report.report_id || "");
            if (reportId) chartTextById.set(reportId, chartReportText(report));
          });
          return chartSearchReports;
        })
        .catch(() => {
          chartSearchReports = [];
          return chartSearchReports;
        });
      return chartSearchPromise;
    }

    function renderChartSearch(rawQuery) {
      if (!chartSearchSection || !chartSearchResults) return;
      const active = scopeFilter.value === "charts";
      chartSearchSection.hidden = !active;
      if (!active) {
        chartSearchResults.innerHTML = "";
        if (chartSearchCount) chartSearchCount.textContent = "";
        if (chartSearchStatus) chartSearchStatus.textContent = "";
        return;
      }
      const query = normalize(rawQuery);
      const tokens = queryTokens(query);
      if (tokens.length === 0) {
        chartSearchResults.innerHTML = '<div class="empty-state">输入公司、指标、时间、地区、单位或趋势开始检索图表。</div>';
        if (chartSearchCount) chartSearchCount.textContent = "";
        if (chartSearchStatus) {
          chartSearchStatus.className = "status-line";
          chartSearchStatus.textContent = chartSearchReports.length ? `已载入 ${chartSearchReports.length} 份报告的图表索引。` : "暂无可用图表索引。";
        }
        return;
      }
      const matches = [];
      chartSearchReports.forEach((report) => {
        if (!tokens.every((token) => chartReportText(report).includes(token))) return;
        const charts = (Array.isArray(report.charts) ? report.charts : [])
          .filter((chart) => tokens.every((token) => chartRecordText(chart).includes(token)));
        const visibleCharts = charts.length ? charts : (Array.isArray(report.charts) ? report.charts.slice(0, 1) : []);
        visibleCharts.slice(0, 3).forEach((chart) => matches.push({ report, chart }));
      });
      const visible = matches.slice(0, 60);
      chartSearchResults.innerHTML = visible.length
        ? visible.map(({ report, chart }) => chartSearchRow(report, chart)).join("")
        : '<div class="empty-state">暂无匹配的图表解读。</div>';
      if (chartSearchCount) chartSearchCount.textContent = matches.length ? `${matches.length} 条图表` : "";
      if (chartSearchStatus) {
        chartSearchStatus.className = "status-line";
        chartSearchStatus.textContent = matches.length > visible.length ? `显示前 ${visible.length} 条，请增加关键词缩小范围。` : "";
      }
    }

    function currentHotReportPage() {
      return hotReportPages[hotReportPageIndex] || null;
    }

    function renderHotReportPagination(page) {
      if (!hotReportsPagination || !hotReportsPrev || !hotReportsNext || !hotReportsPageInfo) return;
      const hasPrevious = hotReportPageIndex > 0;
      const hasCachedNext = Boolean(hotReportPages[hotReportPageIndex + 1]);
      const hasNext = hasCachedNext || Boolean(page && !page.cursorInvalidated && page.hasMore && page.nextCursor);
      hotReportsPagination.hidden = !page || (!hasPrevious && !hasNext);
      hotReportsPrev.disabled = hotReportsLoading || !hasPrevious;
      hotReportsNext.disabled = hotReportsLoading || !hasNext;
      const pageCount = Number.isFinite(page && page.total)
        ? Math.max(1, Math.ceil(page.total / HOT_REPORT_PAGE_SIZE))
        : 0;
      hotReportsPageInfo.textContent = pageCount
        ? `第 ${hotReportPageIndex + 1} / ${pageCount} 页`
        : `第 ${hotReportPageIndex + 1} 页`;
    }

    function renderHotReports() {
      if (!hotReportsSection || !hotReportsResults) return;
      if (!workerUrl) {
        hotReportsSection.hidden = true;
        searchResultCounts.hot = 0;
        renderSearchRecommendations();
        return;
      }
      const page = currentHotReportPage();
      const pageItems = page && Array.isArray(page.items) ? page.items : [];
      const queryChanging = hotReportsLoading && hotReportRequestedQuery !== hotReportActiveQuery;
      hotReportsSection.hidden = false;
      hotReportsResults.setAttribute("aria-busy", hotReportsLoading ? "true" : "false");
      if (!page && !hotReportsLoaded) {
        hotReportsResults.innerHTML = `
          <div class="loading-state">
            <span class="loading-spinner" aria-hidden="true"></span>
            <span>正在读取首批近期热门报告…</span>
          </div>
        `;
        if (hotReportsCount) hotReportsCount.textContent = "";
        searchResultCounts.hot = null;
        renderHotReportPagination(null);
        renderSearchRecommendations();
        return;
      }
      if (queryChanging) {
        searchResultCounts.hot = null;
      } else if (hotReportsFailed) {
        searchResultCounts.hot = "error";
      } else {
        searchResultCounts.hot = Number.isFinite(page && page.total) ? page.total : pageItems.length;
      }
      if (hotReportsCount) {
        if (Number.isFinite(page && page.total)) hotReportsCount.textContent = `${page.total} 条`;
        else hotReportsCount.textContent = pageItems.length ? `本页 ${pageItems.length} 条` : "";
      }
      if (pageItems.length) {
        hotReportsResults.innerHTML = pageItems.map(hotReportRow).join("");
      } else if (hotReportsFailed) {
        hotReportsResults.innerHTML = "";
      } else {
        hotReportsResults.innerHTML = `<div class="empty-state">${hotReportActiveQuery ? "近期热门报告中暂无匹配结果。" : "暂时没有近期热门报告。"}</div>`;
      }
      renderHotReportPagination(page);
      renderSearchRecommendations();
    }

    function hotReportRequestUrl(query, cursor = "") {
      const params = new URLSearchParams({ limit: String(HOT_REPORT_PAGE_SIZE) });
      if (query) params.set("q", query);
      if (cursor) params.set("cursor", cursor);
      return `${workerUrl}/hot-reports?${params.toString()}`;
    }

    async function requestHotReportPage({ query = "", cursor = "", pageIndex = 0, replace = false } = {}) {
      if (!workerUrl || !hotReportsSection || !hotReportsResults) return;
      const cleanQuery = String(query || "").trim().slice(0, 200);
      if (hotReportRequestController) hotReportRequestController.abort();
      const controller = new AbortController();
      const requestVersion = ++hotReportRequestVersion;
      hotReportRequestController = controller;
      hotReportRequestedQuery = cleanQuery;
      hotReportsLoading = true;
      hotReportsFailed = false;
      if (!currentHotReportPage()) hotReportsLoaded = false;
      if (hotReportsRetry) hotReportsRetry.hidden = true;
      setHotReportsStatus(
        currentHotReportPage()
          ? (replace ? "正在更新近期热门报告，当前结果可继续浏览…" : `正在读取第 ${pageIndex + 1} 页，当前页可继续浏览…`)
          : "",
      );
      renderHotReports();
      let deadlineReached = false;
      const timeoutId = window.setTimeout(() => {
        deadlineReached = true;
        controller.abort();
      }, 5_000);
      try {
        const response = await fetch(hotReportRequestUrl(cleanQuery, cursor), { signal: controller.signal });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
          const failure = new Error(data.detail || "近期热门报告读取失败。");
          failure.status = response.status;
          throw failure;
        }
        if (requestVersion !== hotReportRequestVersion) return;
        const responseItems = (Array.isArray(data.items) ? data.items : [])
          .filter((item) => item && item.id)
          .map((item) => publicSearchItem({ ...item, source: HOT_REPORT_SOURCE }, HOT_REPORT_SOURCE));
        const rawTotal = data.total === null || data.total === undefined || data.total === ""
          ? Number.NaN
          : Number(data.total);
        const nextPage = {
          items: responseItems,
          nextCursor: String(data.next_cursor || ""),
          hasMore: typeof data.has_more === "boolean" ? data.has_more : Boolean(data.next_cursor),
          total: Number.isFinite(rawTotal) && rawTotal >= 0 ? rawTotal : null,
        };
        if (replace) {
          hotReportPages = [nextPage];
          hotReportPageIndex = 0;
          hotReportActiveQuery = cleanQuery;
          hotReportItems.clear();
        } else {
          hotReportPages = hotReportPages.slice(0, pageIndex);
          hotReportPages[pageIndex] = nextPage;
          hotReportPageIndex = pageIndex;
        }
        responseItems.forEach((item) => hotReportItems.set(String(item.id), item));
        if (replace && pageIndex === 0 && !cleanQuery) {
          writeHotReportFirstPageCache(nextPage, hotReportLocalStorage());
        }
        hotReportsLoaded = true;
        hotReportsFailed = false;
        hotReportRetryQuery = null;
        setHotReportsStatus("");
        if (cleanQuery) {
          trackEvent(workerUrl, "search", {
            source: HOT_REPORT_SOURCE,
            query: cleanQuery,
            result_count: Number.isFinite(nextPage.total) ? nextPage.total : responseItems.length,
          });
        }
      } catch (error) {
        if (requestVersion !== hotReportRequestVersion) return;
        hotReportsLoaded = true;
        const retained = Boolean(currentHotReportPage());
        const retainedForSameQuery = retained && cleanQuery === hotReportActiveQuery;
        hotReportsFailed = replace && !retainedForSameQuery;
        hotReportRetryQuery = cleanQuery;
        const indexChanged = error && error.status === 409;
        if (indexChanged && !replace && currentHotReportPage()) currentHotReportPage().cursorInvalidated = true;
        const message = retainedForSameQuery
          ? (deadlineReached
            ? "近期热门报告更新较慢，当前为最近一次成功结果。"
            : "近期热门报告暂未完成更新，当前为最近一次成功结果。")
          : indexChanged
          ? "近期热门报告列表已更新，请从第一页重新加载。"
          : (deadlineReached
            ? "近期热门报告读取较慢，请重新加载。"
            : (error.message || "近期热门报告暂时无法读取。"));
        setHotReportsStatus(`${message}${retained && !retainedForSameQuery ? " 已保留当前结果。" : ""}`, "error");
        if (hotReportsRetry) hotReportsRetry.hidden = false;
      } finally {
        window.clearTimeout(timeoutId);
        if (requestVersion === hotReportRequestVersion) {
          hotReportRequestController = null;
          hotReportsLoading = false;
          renderHotReports();
        }
      }
    }

    function loadHotReports(query = "") {
      return requestHotReportPage({ query, pageIndex: 0, replace: true });
    }

    function scheduleHotReportSearch(query = "", delay = 300) {
      window.clearTimeout(hotReportSearchTimer);
      const cleanQuery = String(query || "").trim().slice(0, 200);
      if (hotReportsLoading && hotReportRequestedQuery !== cleanQuery) {
        hotReportRequestVersion += 1;
        if (hotReportRequestController) hotReportRequestController.abort();
        hotReportRequestController = null;
        hotReportRequestedQuery = cleanQuery;
        hotReportsLoading = false;
        setHotReportsStatus("");
        renderHotReports();
      }
      if (cleanQuery === hotReportActiveQuery && !hotReportsFailed) {
        renderHotReports();
        return;
      }
      hotReportSearchTimer = window.setTimeout(() => loadHotReports(cleanQuery), Math.max(0, delay));
    }

    let bankOptions = new Map();
    let industryOptions = new Map();

    function updateCatalogReadiness(text, state = "") {
      if (!searchReadiness || !searchReadinessText) return;
      searchReadiness.className = `search-readiness${state ? ` is-${state}` : ""}`;
      searchReadinessText.textContent = text;
    }

    function createCatalogDerivedState(nextCatalog, overrides = []) {
      return {
        catalog: nextCatalog,
        items: mergeCatalogPdfOverrides(nextCatalog.items, overrides),
        catalogById: new Map(),
        metadataById: new Map(),
        titleSearchById: new Map(),
        dateSortById: new Map(),
        itemDateById: new Map(),
        bankKeyById: new Map(),
        pageCountById: new Map(),
        industryById: new Map(),
        bankOptions: new Map(),
        industryOptions: new Map(),
        fallbackRecommendations: [],
      };
    }

    function addCatalogDerivedItem(state, item) {
        const id = String(item.id || "");
        state.catalogById.set(id, item);
        state.metadataById.set(id, metadataText(item));
        state.titleSearchById.set(id, normalize([item.title, item.title_zh, item.filename].join(" ")));
        state.dateSortById.set(id, dateSortValue(item));
        state.itemDateById.set(id, itemDate(item));
        state.pageCountById.set(id, reportPageCountValue(item));
        const bKey = bankKey(item);
        state.bankKeyById.set(id, bKey);
        const b = state.bankOptions.get(bKey) || { label: bankLabel(item), count: 0 };
        b.count += 1;
        state.bankOptions.set(bKey, b);
        const industry = inferIndustry(item);
        state.industryById.set(id, industry);
        const industryRow = state.industryOptions.get(industry) || { label: industry, count: 0 };
        industryRow.count += 1;
        state.industryOptions.set(industry, industryRow);
    }

    function finishCatalogDerivedState(state) {
      state.fallbackRecommendations = state.items
        .filter((item) => isPdfAvailable(item))
        .slice()
        .sort((left, right) => (state.dateSortById.get(String(right.id || "")) || 0) - (state.dateSortById.get(String(left.id || "")) || 0))
        .slice(0, 6);
      return state;
    }

    function applyCatalogDerivedState(state) {
      catalog = state.catalog;
      items = state.items;
      catalogById = state.catalogById;
      metadataById = state.metadataById;
      titleSearchById = state.titleSearchById;
      dateSortById = state.dateSortById;
      itemDateById = state.itemDateById;
      bankKeyById = state.bankKeyById;
      pageCountById = state.pageCountById;
      industryById = state.industryById;
      bankOptions = state.bankOptions;
      industryOptions = state.industryOptions;
      fallbackRecommendations = state.fallbackRecommendations;
      setOptions(bankFilter, optionSummary(bankOptions), "All institutions");
      setOptions(industryFilter, optionSummary(industryOptions), "All industries");
    }

    function rebuildCatalogDerived(nextCatalog, overrides = []) {
      const state = createCatalogDerivedState(nextCatalog, overrides);
      for (const item of state.items) addCatalogDerivedItem(state, item);
      applyCatalogDerivedState(finishCatalogDerivedState(state));
    }

    async function rebuildCatalogDerivedInChunks(nextCatalog, overrides = [], overrideVersion = catalogOverrideVersion) {
      const state = createCatalogDerivedState(nextCatalog, overrides);
      for (let index = 0; index < state.items.length; index += 1) {
        addCatalogDerivedItem(state, state.items[index]);
        if (index > 0 && index % 350 === 0) {
          // Yield between bounded chunks so the full catalog upgrade cannot
          // create a long task while a user is typing in the preview catalog.
          await new Promise((resolve) => window.setTimeout(resolve, 0));
        }
      }
      if (overrideVersion !== catalogOverrideVersion) {
        return rebuildCatalogDerivedInChunks(nextCatalog, catalogPdfOverrides, catalogOverrideVersion);
      }
      applyCatalogDerivedState(finishCatalogDerivedState(state));
    }

    rebuildCatalogDerived(catalog);
    updateCatalogReadiness(
      fullCatalogReady
        ? `完整目录已就绪，共 ${items.length} 份报告。`
        : `已先显示最新 ${items.length} 份报告，正在后台载入完整目录…`,
      fullCatalogReady ? "ready" : "searching",
    );

    function updateMeta() {
      const visibleTotal = Math.max(items.length, Number(catalog.total_item_count || 0));
      meta.textContent = `${visibleTotal} reports`;
      const totalSize = formatSize(internalStorageMetadata && internalStorageMetadata.total_size_bytes);
      const limitSize = formatSize(internalStorageMetadata && internalStorageMetadata.limit_bytes);
      const hotTotalSize = formatSize(internalStorageMetadata && internalStorageMetadata.hot_report_size_bytes);
      const hotLimitSize = formatSize(internalStorageMetadata && internalStorageMetadata.hot_report_limit_bytes);
      const contactStorageMeta = contactReportStorageMetaText(internalStorageMetadata);
      if (showInternalStorageMetadata && totalSize && limitSize) {
        meta.textContent += ` | ${totalSize} / ${limitSize} PDF storage`;
      } else if (showInternalStorageMetadata && totalSize) {
        meta.textContent += ` | ${totalSize} PDF storage`;
      }
      if (showInternalStorageMetadata && hotTotalSize && hotLimitSize) {
        meta.textContent += ` | ${hotTotalSize} / ${hotLimitSize} hot archive`;
      }
      if (showInternalStorageMetadata && contactStorageMeta) {
        meta.textContent += ` | ${contactStorageMeta}`;
      }
      if (catalog.updated_at_bjt) {
        meta.textContent += ` | Updated ${catalog.updated_at_bjt}`;
      }
      meta.textContent += ` | ${searchIndexLabel}`;
    }

    async function refreshInternalStorageMetadata() {
      const requestId = ++internalStorageRequestId;
      showInternalStorageMetadata = isAdminASession();
      internalStorageMetadata = null;
      updateMeta();
      if (!showInternalStorageMetadata || !workerUrl) return;
      try {
        const response = await fetch(`${workerUrl}/internal/pdf-storage`, {
          cache: "no-store",
          headers: authHeaders(),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "PDF storage metadata is unavailable.");
        if (requestId !== internalStorageRequestId || !isAdminASession()) return;
        internalStorageMetadata = data;
      } catch (_error) {
        if (requestId !== internalStorageRequestId) return;
        internalStorageMetadata = null;
      }
      updateMeta();
    }

    document.addEventListener("portal-auth-change", refreshInternalStorageMetadata);
    refreshInternalStorageMetadata();

    function passesFilters(item, filters) {
      const id = String(item.id || "");
      if (filters.bank && bankKeyById.get(id) !== filters.bank) return false;
      if (filters.industry && industryById.get(id) !== filters.industry) return false;
      if (filters.availability === "available" && !isPdfAvailable(item)) return false;
      if (filters.availability === "textOnly" && isPdfAvailable(item)) return false;
      if (filters.pageRanges.length) {
        const pages = pageCountById.get(id) || 0;
        if (!filters.pageRanges.some((value) => {
          const range = pageRangeForValue(value);
          return range && range.matches(pages);
        })) return false;
      }
      const date = itemDateById.get(id) || "";
      if (filters.start && (!date || date < filters.start)) return false;
      if (filters.end && (!date || date > filters.end)) return false;
      return true;
    }

    function selectedPageRangeValues() {
      return pageRangeInputs
        .filter((input) => input.checked)
        .map((input) => input.value);
    }

    function selectedPageRangeLabels() {
      return selectedPageRangeValues()
        .map(pageRangeLabel)
        .filter(Boolean);
    }

    function updateActiveFilters() {
      const labels = [];
      if (bankFilter.value) labels.push(bankFilter.options[bankFilter.selectedIndex].text.replace(/\s+\(\d+\)$/, ""));
      if (industryFilter.value) labels.push(industryFilter.value);
      if (startDate.value || endDate.value) labels.push(`${startDate.value || "start"} to ${endDate.value || "today"}`);
      if (availabilityFilter.value === "available") labels.push("PDF available");
      if (availabilityFilter.value === "textOnly") labels.push("Text only");
      const pageLabels = selectedPageRangeLabels();
      if (pageLabels.length) labels.push(`Pages: ${pageLabels.join(", ")}`);
      if (scopeFilter.value !== "all") labels.push(scopeFilter.options[scopeFilter.selectedIndex].text);
      activeFilters.textContent = labels.length ? labels.join(" · ") : "No filters";
    }

    function render(options = {}) {
      if (options.resetPage) currentPage = 1;
      const query = normalize(input.value);
      const rawQuery = input.value.trim();
      if (scopeFilter.value === "fulltext" && query && historyTextState === "loading" && searchTextById.size === 0) {
        // Keep the previous catalog rows visible until the first bounded text
        // shard is searchable. Replacing them with an empty result while the
        // index is in flight makes a healthy load look like a failed search.
        results.classList.add("is-updating");
        results.setAttribute("aria-busy", "true");
        updateActiveFilters();
        return;
      }
      const filters = {
        bank: bankFilter.value,
        industry: industryFilter.value,
        availability: availabilityFilter.value,
        pageRanges: selectedPageRangeValues(),
        start: startDate.value,
        end: endDate.value,
      };
      const scoped = items
        .filter((item) => passesFilters(item, filters))
        .map((item) => ({
          item,
          score: scoreItem(item, query, scopeFilter.value, metadataById, searchTextById, chartTextById, titleSearchById),
        }))
        .filter((entry) => !query || entry.score >= 0);

      scoped.sort((a, b) => {
        if (query && b.score !== a.score) return b.score - a.score;
        return (dateSortById.get(String(b.item.id || "")) || 0) - (dateSortById.get(String(a.item.id || "")) || 0);
      });

      count.textContent = `${scoped.length} of ${items.length} reports`;
      updateActiveFilters();
      const rowsPerPage = Math.max(1, Number(pageSize.value) || 50);
      const pageCount = Math.max(1, Math.ceil(scoped.length / rowsPerPage));
      currentPage = Math.min(Math.max(currentPage, 1), pageCount);
      const start = (currentPage - 1) * rowsPerPage;
      const visible = scoped.slice(start, start + rowsPerPage);
      pageInfo.textContent = scoped.length
        ? `Page ${currentPage} / ${pageCount}`
        : "Page 0 / 0";
      prevPage.disabled = currentPage <= 1 || !scoped.length;
      nextPage.disabled = currentPage >= pageCount || !scoped.length;
      searchResultCounts.catalog = scoped.length;
      renderChartSearch(rawQuery);
      renderSearchRecommendations();

      if (!scoped.length) {
        results.classList.remove("is-loading", "is-updating");
        results.setAttribute("aria-busy", "false");
        results.innerHTML = '<div class="empty-state">No matching reports.</div>';
        scheduleCatalogSearchAnalytics(rawQuery, scoped.length);
        return;
      }
      results.innerHTML = visible.map((entry) => resultRow(entry.item)).join("");
      results.classList.remove("is-loading", "is-updating");
      results.setAttribute("aria-busy", "false");
      results.scrollTop = 0;
      scheduleCatalogSearchAnalytics(rawQuery, scoped.length);
    }

    function activeFilterPayload() {
      return {
        bank: bankFilter.value,
        industry: industryFilter.value,
        start_date: startDate.value,
        end_date: endDate.value,
        scope: scopeFilter.value,
        availability: availabilityFilter.value,
        page_ranges: selectedPageRangeValues().join(","),
        page_range_labels: selectedPageRangeLabels().join(", "),
      };
    }

    function hasActiveFilters() {
      const filters = activeFilterPayload();
      return Object.values(filters).some(Boolean) && !(filters.scope === "all" && Object.values({ ...filters, scope: "" }).every((value) => !value));
    }

    function scheduleCatalogSearchAnalytics(rawQuery, resultCount) {
      const cleanQuery = String(rawQuery || "").trim();
      const filtersActive = hasActiveFilters();
      if (cleanQuery.length < 2 && !filtersActive) return;
      const payload = {
        source: "catalog",
        query: cleanQuery,
        result_count: resultCount,
        ...activeFilterPayload(),
      };
      const key = JSON.stringify(payload);
      if (key === lastCatalogAnalyticsKey) return;
      window.clearTimeout(catalogAnalyticsTimer);
      catalogAnalyticsTimer = window.setTimeout(() => {
        lastCatalogAnalyticsKey = key;
        trackEvent(workerUrl, "search", payload);
      }, 900);
    }

    function clearAllFilters() {
      bankFilter.value = "";
      industryFilter.value = "";
      startDate.value = "";
      endDate.value = "";
      scopeFilter.value = "all";
      availabilityFilter.value = "";
      pageRangeInputs.forEach((control) => {
        control.checked = false;
      });
      if (externalDateFilter) externalDateFilter.value = "";
      if (externalIncludeHtml) externalIncludeHtml.checked = false;
      if (authorityInstitutionFilter) authorityInstitutionFilter.value = "";
      if (authorityDateFilter) authorityDateFilter.value = "";
      if (authorityPageFilter) authorityPageFilter.value = "";
      render({ resetPage: true });
      renderExternalSearchResults();
      renderAuthoritySearchResults();
      scheduleHotReportSearch(input.value.trim(), 0);
      renderHotReports();
      scheduleExternalSearch();
    }

    let localSearchTimer = 0;
    let inputComposing = false;
    const scheduleLocalRender = (delay = 240) => {
      window.clearTimeout(localSearchTimer);
      if (inputComposing) return;
      results.classList.add("is-updating");
      results.setAttribute("aria-busy", "true");
      updateCatalogReadiness("正在更新结果；已保留当前列表供继续浏览…", "searching");
      localSearchTimer = window.setTimeout(() => {
        render({ resetPage: true });
        renderHotReports();
        updateCatalogReadiness(
          fullCatalogReady ? `搜索目录已就绪，共 ${items.length} 份报告。` : `正在后台补齐完整目录；当前先搜索最新 ${items.length} 份。`,
          fullCatalogReady ? "ready" : "searching",
        );
      }, Math.max(0, delay));
      scheduleExternalSearch();
    };
    input.addEventListener("compositionstart", () => {
      inputComposing = true;
      window.clearTimeout(localSearchTimer);
      window.clearTimeout(hotReportSearchTimer);
    });
    input.addEventListener("compositionend", () => {
      inputComposing = false;
      scheduleLocalRender(0);
      scheduleHotReportSearch(scopeFilter.value === "charts" ? "" : input.value.trim(), 0);
    });
    input.addEventListener("input", () => {
      if (inputComposing) return;
      scheduleLocalRender();
      scheduleHotReportSearch(scopeFilter.value === "charts" ? "" : input.value.trim());
    });
    input.removeEventListener("input", captureEarlyInput);
    [bankFilter, industryFilter, startDate, endDate, availabilityFilter, ...pageRangeInputs].forEach((control) => {
      control.addEventListener("change", () => scheduleLocalRender(0));
    });
    scopeFilter.addEventListener("change", async () => {
      if (scopeFilter.value === "charts") {
        if (chartSearchSection) chartSearchSection.hidden = false;
        if (chartSearchStatus) chartSearchStatus.textContent = "正在读取图表索引…";
        await ensureChartSearchIndex();
      } else if (scopeFilter.value === "fulltext") {
        updateCatalogReadiness("正在按需载入报告正文索引；当前列表可继续浏览…", "searching");
        startTextIndexLoad();
      }
      if (!(scopeFilter.value === "fulltext" && input.value.trim() && searchTextById.size === 0)) {
        render({ resetPage: true });
      }
      scheduleHotReportSearch(scopeFilter.value === "charts" ? "" : input.value.trim(), 0);
      renderHotReports();
      scheduleExternalSearch();
    });
    pageSize.addEventListener("change", () => render({ resetPage: true }));
    prevPage.addEventListener("click", () => {
      currentPage -= 1;
      render();
    });
    nextPage.addEventListener("click", () => {
      currentPage += 1;
      render();
    });
    clearFilters.addEventListener("click", clearAllFilters);
    results.addEventListener("click", (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      const item = catalogById.get(String(row.dataset.id || ""));
      if (item) rememberReportPreview(item);
      trackEvent(workerUrl, "report_open", analyticsReportPayload(item || { id: row.dataset.id }, "catalog"));
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      openReportPage(row.dataset.id);
    });
    if (chartSearchResults) {
      chartSearchResults.addEventListener("click", (event) => {
        const row = event.target.closest(".chart-search-card");
        if (!row) return;
        const item = catalogById.get(String(row.dataset.id || ""));
        if (item) rememberReportPreview(item);
        trackEvent(workerUrl, "report_open", analyticsReportPayload(item || { id: row.dataset.id }, "chart-search"));
      });
    }

    // --- 其他报告 integration ---------------------------------------------
    // Live search through the Worker proxy. Rows open the same password-gated
    // detail flow used by primary reports.
    const externalUrl = workerUrl;
    const thinkTankSection = document.getElementById("thinkTankSection");
    const thinkTankResults = document.getElementById("thinkTankResults");
    const thinkTankCount = document.getElementById("thinkTankCount");
    const thinkTankStatus = document.getElementById("thinkTankStatus");
    const externalSection = document.getElementById("externalSection");
    const externalResults = document.getElementById("externalResults");
    const externalCount = document.getElementById("externalCount");
    const externalStatus = document.getElementById("externalStatus");
    const reportASection = document.getElementById("reportASection");
    const reportAResults = document.getElementById("reportAResults");
    const reportACount = document.getElementById("reportACount");
    const reportAStatus = document.getElementById("reportAStatus");
    const authoritySection = document.getElementById("authoritySection");
    const authorityResults = document.getElementById("authorityResults");
    const authorityCount = document.getElementById("authorityCount");
    const authorityStatus = document.getElementById("authorityStatus");
    let externalTimer = 0;
    let thinkTankToken = 0;
    let externalToken = 0;
    let reportAToken = 0;
    let authorityToken = 0;
    let remoteSearchGeneration = 0;
    let authorityQuery = "";
    const remoteSearchControllers = new Map();
    const remoteSourceDeadlineMs = {
      thinktank: 18_000,
      external: 16_000,
      reportA: 18_000,
      authority: 18_000,
    };
    const remoteSourceStates = new Map();
    const remoteSourceLabels = {
      catalog: "站内目录",
      thinktank: "国际智库",
      external: "其他报告",
      reportA: "报告线索",
      authority: "高权报告",
    };
    const thinkTankItems = new Map();
    const externalItems = new Map();
    const reportAItems = new Map();
    const authorityItems = new Map();
    let externalResponseMeta = {
      warning: "",
      cacheStatus: "",
      filterPartial: false,
      htmlFallback: false,
      htmlFallbackUnconfirmed: false,
      hiddenHtmlCount: 0,
      scannedPages: [],
    };
    let authorityResponseMeta = { filterPartial: false, scannedCount: 0 };

    function renderRemoteSourceProgress(query = "") {
      if (!searchSourceProgress || !searchSourceProgressItems) return;
      const cleanQuery = String(query || "").trim();
      if (!cleanQuery) {
        searchSourceProgress.hidden = true;
        searchSourceProgressItems.innerHTML = "";
        return;
      }
      const rows = Object.keys(remoteSourceLabels).map((source) => ({
        source,
        label: remoteSourceLabels[source],
        state: remoteSourceStates.get(source) || (source === "catalog" ? "done" : "waiting"),
      }));
      const settled = rows.filter((row) => ["done", "error"].includes(row.state)).length;
      searchSourceProgress.hidden = false;
      if (searchSourceProgressSummary) {
        searchSourceProgressSummary.textContent = settled === rows.length
          ? "全部来源已完成"
          : `${settled}/${rows.length} 个来源完成，结果仍在补充`;
      }
      if (searchSourceProgressBar) searchSourceProgressBar.style.width = `${Math.round(settled / rows.length * 100)}%`;
      searchSourceProgressItems.innerHTML = rows.map((row) => {
        const suffix = row.state === "done" ? " ✓" : row.state === "error" ? " 暂不可用" : row.state === "searching" ? " 搜索中" : " 等待中";
        return `<span class="search-source-chip is-${escapeHtml(row.state)}">${escapeHtml(row.label + suffix)}</span>`;
      }).join("");
    }

    function setRemoteSourceState(source, state, query) {
      remoteSourceStates.set(source, state);
      renderRemoteSourceProgress(query);
    }

    function setThinkTankStatus(text, kind) {
      if (!thinkTankStatus) return;
      thinkTankStatus.className = kind ? `status-line ${kind}` : "status-line";
      thinkTankStatus.textContent = publicMessageText(text);
    }

    function hideThinkTankResults() {
      thinkTankToken += 1;
      if (thinkTankSection) thinkTankSection.hidden = true;
      if (thinkTankResults) thinkTankResults.innerHTML = "";
      thinkTankItems.clear();
      if (thinkTankCount) thinkTankCount.textContent = "";
      setThinkTankStatus("");
      searchResultCounts.thinktank = 0;
      renderSearchRecommendations();
    }

    function setExternalStatus(text, kind) {
      if (!externalStatus) return;
      externalStatus.className = kind ? `status-line ${kind}` : "status-line";
      externalStatus.textContent = publicMessageText(text);
    }

    function renderExternalSearchResults() {
      if (!externalResults) return;
      const rows = [...externalItems.values()];
      const view = externalSearchView(rows, {
        recentMonths: externalDateFilter && externalDateFilter.value,
        includeHtml: externalIncludeHtml && externalIncludeHtml.checked,
        allowHtmlFallback: externalResponseMeta.htmlFallback,
      });
      const sourceUnavailable = externalResponseMeta.cacheStatus === "miss" && rows.length === 0;
      searchResultCounts.external = sourceUnavailable ? "error" : view.items.length;
      if (externalCount) {
        externalCount.textContent = view.items.length
          ? `${externalResponseMeta.filterPartial ? "已显示 " : ""}${view.items.length} 条`
          : "";
      }
      externalResults.innerHTML = view.items.length
        ? view.items.map(externalRow).join("")
        : '<div class="empty-state">当前筛选条件下暂无匹配结果。</div>';
      const notes = [];
      if (externalResponseMeta.warning) notes.push(externalResponseMeta.warning);
      else if (sourceUnavailable) notes.push("其他报告来源暂时不可用，且没有可用的缓存结果。");
      const hiddenHtmlCount = Math.max(view.hiddenHtmlCount, externalResponseMeta.hiddenHtmlCount);
      if (hiddenHtmlCount) notes.push(`默认隐藏 ${hiddenHtmlCount} 条 HTML 结果。`);
      if (externalResponseMeta.htmlFallback && view.htmlFallback) {
        notes.push("已检查完整结果且未找到 PDF，现显示仅有的 HTML 结果。");
      }
      if (externalResponseMeta.htmlFallbackUnconfirmed) {
        const pageCount = externalResponseMeta.scannedPages.length;
        notes.push(`已检查前 ${pageCount || "若干"} 页，尚不能确认后续是否有 PDF；HTML 继续保持隐藏，可勾选“包含 HTML 结果”查看。`);
      } else if (externalResponseMeta.filterPartial) {
        const pageCount = externalResponseMeta.scannedPages.length;
        notes.push(`已筛选前 ${pageCount || "若干"} 页，结果仍可能继续；可增加日期条件缩小范围。`);
      }
      setExternalStatus(notes.join(" "), sourceUnavailable ? "error" : "");
      renderSearchRecommendations();
    }

    function setReportAStatus(text, kind) {
      if (!reportAStatus) return;
      reportAStatus.className = kind ? `status-line ${kind}` : "status-line";
      reportAStatus.textContent = publicMessageText(text);
    }

    function hideReportAResults() {
      reportAToken += 1;
      if (reportASection) reportASection.hidden = true;
      if (reportAResults) reportAResults.innerHTML = "";
      reportAItems.clear();
      if (reportACount) reportACount.textContent = "";
      setReportAStatus("");
      searchResultCounts.reportA = 0;
      renderSearchRecommendations();
    }

    function setAuthorityStatus(text, kind) {
      if (!authorityStatus) return;
      authorityStatus.className = kind ? `status-line ${kind}` : "status-line";
      authorityStatus.textContent = publicMessageText(text);
    }

    function authorityInstitutionOptions(itemsToRender) {
      const options = new Map();
      for (const item of itemsToRender || []) {
        const institution = String(item && item.institution || "").trim();
        if (!institution) continue;
        const row = options.get(institution) || { label: institution, count: 0 };
        row.count += 1;
        options.set(institution, row);
      }
      return optionSummary(options);
    }

    function renderAuthoritySearchResults() {
      if (!authorityResults) return;
      const rows = [...authorityItems.values()];
      const visible = authoritySearchView(rows, {
        institution: authorityInstitutionFilter && authorityInstitutionFilter.value,
        recentMonths: authorityDateFilter && authorityDateFilter.value,
        pageRange: authorityPageFilter && authorityPageFilter.value,
      });
      searchResultCounts.authority = visible.length;
      if (authorityCount) {
        authorityCount.textContent = visible.length
          ? `${authorityResponseMeta.filterPartial ? "已显示 " : ""}${visible.length} 条`
          : "";
      }
      authorityResults.innerHTML = visible.length
        ? visible.map(authorityRow).join("")
        : '<div class="empty-state">当前筛选条件下暂无匹配结果。</div>';
      const notes = [];
      if (rows.length && !visible.length) notes.push("可调整机构、日期或页数筛选查看其他结果。");
      if (authorityResponseMeta.filterPartial) {
        notes.push(`已对有界结果集进行服务端筛选（扫描 ${authorityResponseMeta.scannedCount || "若干"} 条），不代表全部结果。`);
      }
      setAuthorityStatus(notes.join(" "));
      renderSearchRecommendations();
    }

    function hideAuthorityResults() {
      authorityQuery = "";
      authorityToken += 1;
      if (authoritySection) authoritySection.hidden = true;
      if (authorityResults) authorityResults.innerHTML = "";
      authorityItems.clear();
      authorityResponseMeta = { filterPartial: false, scannedCount: 0 };
      if (authorityInstitutionFilter) setOptions(authorityInstitutionFilter, [], "全部机构");
      if (authorityCount) authorityCount.textContent = "";
      setAuthorityStatus("");
      searchResultCounts.authority = 0;
      renderSearchRecommendations();
    }

    function prepareRemoteSearch(query) {
      for (const source of ["thinktank", "external", "reportA", "authority"]) {
        searchResultCounts[source] = query && externalUrl ? null : 0;
      }
      renderSearchRecommendations();
    }

    function abortRemoteSearches() {
      for (const controller of remoteSearchControllers.values()) controller.abort();
      remoteSearchControllers.clear();
    }

    function remoteSourceBindings(source) {
      return {
        thinktank: [thinkTankResults, thinkTankCount, setThinkTankStatus],
        external: [externalResults, externalCount, setExternalStatus],
        reportA: [reportAResults, reportACount, setReportAStatus],
        authority: [authorityResults, authorityCount, setAuthorityStatus],
      }[source] || null;
    }

    function markRemoteSourceUnavailable(source, query, generation, message) {
      if (generation !== remoteSearchGeneration || query !== input.value.trim()) return;
      if (!["waiting", "searching"].includes(remoteSourceStates.get(source))) return;
      remoteSourceStates.set(source, "error");
      searchResultCounts[source] = "error";
      const bindings = remoteSourceBindings(source);
      if (bindings) {
        if (bindings[0]) bindings[0].innerHTML = "";
        if (bindings[1]) bindings[1].textContent = "";
        bindings[2](message, "error");
      }
      renderRemoteSourceProgress(query);
      renderSearchRecommendations();
    }

    async function runRemoteSearchWithDeadline(source, query, generation, search) {
      const controller = new AbortController();
      const deadlineMs = remoteSourceDeadlineMs[source] || 18_000;
      let deadlineReached = false;
      remoteSearchControllers.set(source, controller);
      const timeoutId = window.setTimeout(() => {
        deadlineReached = true;
        controller.abort();
      }, deadlineMs);
      try {
        await search(query, controller.signal, generation);
      } finally {
        window.clearTimeout(timeoutId);
        if (remoteSearchControllers.get(source) === controller) {
          remoteSearchControllers.delete(source);
        }
        if (deadlineReached) {
          const label = remoteSourceLabels[source] || "此来源";
          markRemoteSourceUnavailable(
            source,
            query,
            generation,
            `${label} 在 ${Math.round(deadlineMs / 1000)} 秒内未完成，可稍后重试。`,
          );
        }
      }
    }

    async function runThinkTankSearch(query, signal, generation = remoteSearchGeneration) {
      if (!thinkTankSection || !thinkTankResults) return;
      if (!externalUrl || !query) {
        hideThinkTankResults();
        return;
      }
      const token = ++thinkTankToken;
      const isCurrent = () => generation === remoteSearchGeneration
        && query === input.value.trim()
        && token === thinkTankToken;
      setRemoteSourceState("thinktank", "searching", query);
      thinkTankSection.hidden = false;
      if (thinkTankCount) thinkTankCount.textContent = "搜索中…";
      setThinkTankStatus("");
      thinkTankResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索国际智库…</span>
        </div>
      `;
      try {
        const response = await fetch(
          `${externalUrl}/thinktank/search?q=${encodeURIComponent(query)}`,
          { cache: "no-store", signal },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (!isCurrent()) return;
        const items = Array.isArray(data.items)
          ? data.items.map((item) => publicSearchItem(item, THINKTANK_SOURCE))
          : [];
        searchResultCounts.thinktank = items.length;
        thinkTankItems.clear();
        items.forEach((item) => thinkTankItems.set(String(item.id), item));
        if (thinkTankCount) thinkTankCount.textContent = items.length ? `${items.length} 条` : "";
        thinkTankResults.innerHTML = items.length
          ? items.map(thinkTankRow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
        trackEvent(workerUrl, "search", {
          source: THINKTANK_SOURCE,
          query,
          result_count: items.length,
          total_count: data.total || 0,
          cache_status: data.cache_status || "",
        });
        renderSearchRecommendations();
        setRemoteSourceState("thinktank", "done", query);
      } catch (error) {
        if (error && error.name === "AbortError") return;
        if (!isCurrent()) return;
        if (thinkTankCount) thinkTankCount.textContent = "";
        thinkTankResults.innerHTML = "";
        setThinkTankStatus(error.message || "搜索暂不可用。", "error");
        searchResultCounts.thinktank = "error";
        renderSearchRecommendations();
        setRemoteSourceState("thinktank", "error", query);
      }
    }

    async function runExternalSearch(query, signal, generation = remoteSearchGeneration) {
      if (!externalSection || !externalResults) return;
      if (!externalUrl || !query) {
        externalSection.hidden = true;
        externalResults.innerHTML = "";
        externalItems.clear();
        externalResponseMeta = {
          warning: "",
          cacheStatus: "",
          filterPartial: false,
          htmlFallback: false,
          htmlFallbackUnconfirmed: false,
          hiddenHtmlCount: 0,
          scannedPages: [],
        };
        if (externalCount) externalCount.textContent = "";
        setExternalStatus("");
        searchResultCounts.external = 0;
        renderSearchRecommendations();
        hideAuthorityResults();
        return;
      }
      const token = ++externalToken;
      const isCurrent = () => generation === remoteSearchGeneration
        && query === input.value.trim()
        && token === externalToken;
      setRemoteSourceState("external", "searching", query);
      externalSection.hidden = false;
      externalItems.clear();
      if (externalCount) externalCount.textContent = "搜索中…";
      externalResponseMeta = {
        warning: "",
        cacheStatus: "",
        filterPartial: false,
        htmlFallback: false,
        htmlFallbackUnconfirmed: false,
        hiddenHtmlCount: 0,
        scannedPages: [],
      };
      setExternalStatus("");
      externalResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索其他报告…</span>
        </div>
      `;
      try {
        const response = await fetch(
          embeddedSearchRequestUrl(externalUrl, "external/search", query, {
            recentMonths: externalDateFilter && externalDateFilter.value,
            includeHtml: externalIncludeHtml && externalIncludeHtml.checked,
          }),
          { cache: "no-store", signal },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (!isCurrent()) return; // a newer query superseded this one
        const items = Array.isArray(data.items)
          ? data.items.map((item) => publicSearchItem(item, EXTERNAL_SOURCE))
          : [];
        const sourceUnavailable = data.cache_status === "miss" && items.length === 0;
        externalItems.clear();
        items.forEach((item) => externalItems.set(String(item.id), item));
        externalResponseMeta = {
          warning: publicMessageText(data.warning),
          cacheStatus: String(data.cache_status || "").trim(),
          filterPartial: Boolean(data.filter_partial),
          htmlFallback: Boolean(data.html_fallback),
          htmlFallbackUnconfirmed: Boolean(data.html_fallback_unconfirmed),
          hiddenHtmlCount: Math.max(0, Number(data.hidden_html_count || 0) || 0),
          scannedPages: Array.isArray(data.scanned_pages) ? data.scanned_pages.slice(0, 3) : [],
        };
        renderExternalSearchResults();
        trackEvent(workerUrl, "search", {
          source: EXTERNAL_SOURCE,
          query,
          result_count: searchResultCounts.external === "error" ? 0 : searchResultCounts.external,
          unfiltered_result_count: items.length,
          total_count: data.total_count || data.total_page || 0,
          cache_status: data.cache_status || "",
        });
        setRemoteSourceState("external", sourceUnavailable ? "error" : "done", query);
      } catch (error) {
        if (error && error.name === "AbortError") return;
        if (!isCurrent()) return;
        if (externalCount) externalCount.textContent = "";
        externalResults.innerHTML = "";
        externalResponseMeta = {
          warning: "",
          cacheStatus: "",
          filterPartial: false,
          htmlFallback: false,
          htmlFallbackUnconfirmed: false,
          hiddenHtmlCount: 0,
          scannedPages: [],
        };
        setExternalStatus(error.message || "搜索暂不可用。", "error");
        searchResultCounts.external = "error";
        renderSearchRecommendations();
        setRemoteSourceState("external", "error", query);
      }
    }

    async function runReportASearch(query, signal, generation = remoteSearchGeneration) {
      if (!reportASection || !reportAResults) return;
      if (!externalUrl || !query) {
        hideReportAResults();
        return;
      }
      const token = ++reportAToken;
      const isCurrent = () => generation === remoteSearchGeneration
        && query === input.value.trim()
        && token === reportAToken;
      setRemoteSourceState("reportA", "searching", query);
      reportASection.hidden = false;
      if (reportACount) reportACount.textContent = "搜索中…";
      setReportAStatus("");
      reportAResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索报告A…</span>
        </div>
      `;
      try {
        const response = await fetch(
          `${externalUrl}/report-a/search?q=${encodeURIComponent(query)}`,
          { cache: "no-store", signal },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (!isCurrent()) return;
        const items = Array.isArray(data.items)
          ? data.items.map((item) => publicSearchItem(item, REPORT_A_SOURCE))
          : [];
        searchResultCounts.reportA = items.length;
        reportAItems.clear();
        items.forEach((item) => reportAItems.set(String(item.id), item));
        if (reportACount) reportACount.textContent = items.length ? `${items.length} 条` : "";
        reportAResults.innerHTML = items.length
          ? items.map(reportARow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
        trackEvent(workerUrl, "search", {
          source: REPORT_A_SOURCE,
          query,
          result_count: items.length,
          total_count: data.total || 0,
          cache_status: data.cache_status || "",
        });
        renderSearchRecommendations();
        setRemoteSourceState("reportA", "done", query);
      } catch (error) {
        if (error && error.name === "AbortError") return;
        if (!isCurrent()) return;
        if (reportACount) reportACount.textContent = "";
        reportAResults.innerHTML = "";
        setReportAStatus(error.message || "搜索暂不可用。", "error");
        searchResultCounts.reportA = "error";
        renderSearchRecommendations();
        setRemoteSourceState("reportA", "error", query);
      }
    }

    async function runAuthoritySearch(query, signal, generation = remoteSearchGeneration) {
      if (!authoritySection || !authorityResults) return;
      if (!externalUrl || !query) {
        hideAuthorityResults();
        return;
      }
      const token = ++authorityToken;
      const isCurrent = () => generation === remoteSearchGeneration
        && query === input.value.trim()
        && token === authorityToken;
      setRemoteSourceState("authority", "searching", query);
      authorityQuery = query;
      authoritySection.hidden = false;
      authorityItems.clear();
      if (authorityCount) authorityCount.textContent = "搜索中…";
      setAuthorityStatus("");
      authorityResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索高权报告…</span>
        </div>
      `;
      try {
        const response = await fetch(
          embeddedSearchRequestUrl(externalUrl, "authority/search", query, {
            institution: authorityInstitutionFilter && authorityInstitutionFilter.value,
            recentMonths: authorityDateFilter && authorityDateFilter.value,
            pageRange: authorityPageFilter && authorityPageFilter.value,
          }),
          { cache: "no-store", signal },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (!isCurrent()) return;
        const items = Array.isArray(data.items)
          ? data.items.map((item) => publicSearchItem(item, AUTHORITY_SOURCE))
          : [];
        authorityItems.clear();
        items.forEach((item) => authorityItems.set(String(item.id), item));
        if (authorityInstitutionFilter) {
          const currentInstitution = authorityInstitutionFilter.value;
          const institutionOptions = Array.isArray(data.institutions)
            ? data.institutions.map((option) => ({
              value: publicBrandText(option && option.value || option || ""),
              label: option && option.label
                ? `${publicBrandText(option.label)}${option.count ? ` (${option.count})` : ""}`
                : publicBrandText(option),
            })).filter((option) => option.value)
            : authorityInstitutionOptions(items);
          if (currentInstitution && !institutionOptions.some((option) => option.value === currentInstitution)) {
            institutionOptions.push({ value: currentInstitution, label: currentInstitution });
          }
          setOptions(authorityInstitutionFilter, institutionOptions, "全部机构");
        }
        authorityResponseMeta = {
          filterPartial: Boolean(data.filter_partial),
          scannedCount: Math.max(0, Number(data.scanned_count || 0) || 0),
        };
        renderAuthoritySearchResults();
        trackEvent(workerUrl, "search", {
          source: AUTHORITY_SOURCE,
          query,
          result_count: searchResultCounts.authority,
          unfiltered_result_count: items.length,
          total_count: data.total || 0,
          cache_status: data.cache_status || "",
        });
        setRemoteSourceState("authority", "done", query);
      } catch (error) {
        if (error && error.name === "AbortError") return;
        if (!isCurrent()) return;
        if (authorityCount) authorityCount.textContent = "";
        authorityResults.innerHTML = "";
        authorityResponseMeta = { filterPartial: false, scannedCount: 0 };
        setAuthorityStatus(error.message || "搜索暂不可用。", "error");
        searchResultCounts.authority = "error";
        renderSearchRecommendations();
        setRemoteSourceState("authority", "error", query);
      }
    }

    function scheduleExternalSearch() {
      window.clearTimeout(externalTimer);
      const generation = ++remoteSearchGeneration;
      abortRemoteSearches();
      const query = input.value.trim();
      if (scopeFilter.value === "charts" || !query) {
        hideThinkTankResults();
        runExternalSearch("");
        hideReportAResults();
        hideAuthorityResults();
        remoteSourceStates.clear();
        renderRemoteSourceProgress("");
        return;
      }
      remoteSourceStates.clear();
      remoteSourceStates.set("catalog", fullCatalogReady ? "done" : "searching");
      for (const source of ["thinktank", "external", "reportA", "authority"]) {
        remoteSourceStates.set(source, "waiting");
      }
      prepareRemoteSearch(query);
      renderRemoteSourceProgress(query);
      externalTimer = window.setTimeout(() => {
        if (generation !== remoteSearchGeneration || query !== input.value.trim()) return;
        Promise.allSettled([
          runRemoteSearchWithDeadline("thinktank", query, generation, runThinkTankSearch),
          runRemoteSearchWithDeadline("external", query, generation, runExternalSearch),
          runRemoteSearchWithDeadline("reportA", query, generation, runReportASearch),
          runRemoteSearchWithDeadline("authority", query, generation, runAuthoritySearch),
        ]).then(() => {
          if (generation !== remoteSearchGeneration || query !== input.value.trim()) return;
          for (const source of ["thinktank", "external", "reportA", "authority"]) {
            markRemoteSourceUnavailable(source, query, generation, "此来源未完成，可稍后重试。");
          }
        });
      }, 480);
    }

    [externalDateFilter, externalIncludeHtml].filter(Boolean).forEach((control) => {
      control.addEventListener("change", () => {
        const query = input.value.trim();
        if (!query || scopeFilter.value === "charts") {
          renderExternalSearchResults();
          return;
        }
        const active = remoteSearchControllers.get("external");
        if (active) active.abort();
        runRemoteSearchWithDeadline("external", query, remoteSearchGeneration, runExternalSearch);
      });
    });
    [authorityInstitutionFilter, authorityDateFilter, authorityPageFilter].filter(Boolean).forEach((control) => {
      control.addEventListener("change", () => {
        const query = input.value.trim();
        if (!query || scopeFilter.value === "charts") {
          renderAuthoritySearchResults();
          return;
        }
        const active = remoteSearchControllers.get("authority");
        if (active) active.abort();
        runRemoteSearchWithDeadline("authority", query, remoteSearchGeneration, runAuthoritySearch);
      });
    });
    if (thinkTankResults) {
      thinkTankResults.addEventListener("click", (event) => {
        const row = event.target.closest(".thinktank-row");
        if (!row) return;
        const item = thinkTankItems.get(String(row.dataset.id || ""));
        if (item) {
          rememberDocItem({ ...item, source: THINKTANK_SOURCE });
          trackEvent(workerUrl, "report_open", analyticsReportPayload(item, THINKTANK_SOURCE));
        }
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
        if (item) openInNewTab(externalPageUrl({ ...item, source: THINKTANK_SOURCE }, ""));
      });
    }
    externalResults.addEventListener("click", (event) => {
      const row = event.target.closest(".external-row");
      if (!row) return;
      const item = externalItems.get(String(row.dataset.id));
      if (item) {
        rememberDocItem({ ...item, source: EXTERNAL_SOURCE });
        trackEvent(workerUrl, "report_open", analyticsReportPayload(item, EXTERNAL_SOURCE));
      }
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      if (item) openInNewTab(externalPageUrl(item, ""));
    });
    if (reportAResults) {
      reportAResults.addEventListener("click", (event) => {
        const row = event.target.closest(".report-a-row");
        if (!row) return;
        const item = reportAItems.get(String(row.dataset.id || ""));
        if (item) {
          rememberDocItem({ ...item, source: REPORT_A_SOURCE });
          trackEvent(workerUrl, "report_open", analyticsReportPayload(item, REPORT_A_SOURCE));
        }
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
        if (item) openInNewTab(externalPageUrl({ ...item, source: REPORT_A_SOURCE }, ""));
      });
    }
    if (authorityResults) {
      authorityResults.addEventListener("click", (event) => {
        const row = event.target.closest(".authority-row");
        if (!row) return;
        const item = authorityItems.get(String(row.dataset.id));
        if (item) {
          rememberDocItem({ ...item, source: AUTHORITY_SOURCE });
          trackEvent(workerUrl, "report_open", analyticsReportPayload(item, AUTHORITY_SOURCE));
        }
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
        if (item) openInNewTab(externalPageUrl({ ...item, source: AUTHORITY_SOURCE }, ""));
      });
    }
    if (hotReportsResults) {
      hotReportsResults.addEventListener("click", (event) => {
        const row = event.target.closest(".hot-report-row");
        if (!row) return;
        const item = hotReportItems.get(String(row.dataset.id || ""));
        if (item) {
          rememberDocItem({ ...item, source: HOT_REPORT_SOURCE });
          trackEvent(workerUrl, "report_open", analyticsReportPayload(item, HOT_REPORT_SOURCE));
        }
      });
    }
    if (hotReportsPrev) {
      hotReportsPrev.addEventListener("click", () => {
        if (hotReportsLoading || hotReportPageIndex <= 0) return;
        hotReportPageIndex -= 1;
        hotReportsFailed = false;
        if (hotReportsRetry) hotReportsRetry.hidden = true;
        setHotReportsStatus("");
        renderHotReports();
        hotReportsSection.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
    if (hotReportsNext) {
      hotReportsNext.addEventListener("click", () => {
        if (hotReportsLoading) return;
        const page = currentHotReportPage();
        if (!page) return;
        if (hotReportPages[hotReportPageIndex + 1]) {
          hotReportPageIndex += 1;
          hotReportsFailed = false;
          if (hotReportsRetry) hotReportsRetry.hidden = true;
          setHotReportsStatus("");
          renderHotReports();
        } else if (page.hasMore && page.nextCursor) {
          requestHotReportPage({
            query: hotReportActiveQuery,
            cursor: page.nextCursor,
            pageIndex: hotReportPageIndex + 1,
          });
        }
        hotReportsSection.scrollIntoView({ behavior: "smooth", block: "start" });
      });
    }
    if (hotReportsRetry) {
      hotReportsRetry.addEventListener("click", () => {
        loadHotReports(hotReportRetryQuery !== null
          ? hotReportRetryQuery
          : (scopeFilter.value === "charts" ? "" : input.value.trim()));
      });
    }
    if (searchRecommendationsResults) {
      searchRecommendationsResults.addEventListener("click", (event) => {
        const row = event.target.closest(".report-link");
        if (!row) return;
        const item = catalogById.get(String(row.dataset.id || ""));
        if (item) rememberReportPreview(item);
        trackEvent(workerUrl, "report_open", analyticsReportPayload(item || { id: row.dataset.id }, "recommendation"));
      });
    }

    const initialQuery = new URLSearchParams(window.location.search).get("q");
    if (initialQuery && input) {
      input.value = initialQuery.slice(0, 200);
      prepareRemoteSearch(input.value.trim());
      scheduleExternalSearch();
    }

    let searchIndexPrunedText = false;
    let historyTextState = "idle";
    let textIndexRenderTimer = 0;
    const searchIndexStatusLabel = () => {
      let label = `Text index ${searchTextById.size} reports`;
      if (historyTextState === "loading") label += " +";
      if (searchIndexPrunedText) label += " (recent text)";
      return label;
    };
    const mergeSearchIndex = (searchIndex) => {
      const searchItems = Array.isArray(searchIndex.items) ? searchIndex.items : [];
      searchItems.forEach((entry) => {
        if (!entry.id || !entry.text) return;
        const existing = searchTextById.get(entry.id);
        searchTextById.set(entry.id, existing ? `${existing} ${entry.text}` : String(entry.text));
      });
      if (searchIndex.text_pruned_dates && searchIndex.text_pruned_dates.length) {
        searchIndexPrunedText = true;
      }
      searchIndexLabel = searchIndexStatusLabel();
      updateMeta();
    };
    const scheduleTextIndexRender = (immediate = false) => {
      if (scopeFilter.value !== "fulltext") return;
      window.clearTimeout(textIndexRenderTimer);
      textIndexRenderTimer = window.setTimeout(() => {
        render({ resetPage: true });
        updateCatalogReadiness(
          historyTextState === "loading"
            ? `已可搜索 ${searchTextById.size} 份报告正文，更多分片仍在后台载入…`
            : `报告正文索引已就绪，共 ${searchTextById.size} 份。`,
          historyTextState === "failed" ? "error" : (historyTextState === "loading" ? "searching" : "ready"),
        );
      }, immediate ? 0 : 100);
    };
    const loadSearchIndexShards = async (root) => {
      const manifest = await loadJson(`${root}/manifest.json`);
      if (manifest.text_pruned_dates && manifest.text_pruned_dates.length) {
        searchIndexPrunedText = true;
      }
      const shards = Array.isArray(manifest.shards) ? manifest.shards : [];
      for (const shard of shards) {
        if (!shard || !/^[a-zA-Z0-9._-]+\.json$/.test(String(shard.file || ""))) continue;
        mergeSearchIndex(await loadJson(`${root}/${shard.file}`));
        scheduleTextIndexRender(searchTextById.size > 0 && searchTextById.size === Number(shard.item_count || 0));
        // Parsing and indexing stay in bounded tasks even on lower-memory
        // mobile browsers; the former 90 MB monolith is never downloaded.
        await new Promise((resolve) => window.setTimeout(resolve, 30));
      }
      return manifest;
    };
    // The full text corpus is intentionally opt-in. It is much larger than the
    // title/catalog index and must never compete with typing or first paint.
    const startTextIndexLoad = () => {
      if (historyTextState !== "idle") return;
      historyTextState = "loading";
      (async () => {
        try {
          await loadSearchIndexShards("data/search_index_current");
        } catch (error) {
          console.warn(error);
        }
        try {
          await loadSearchIndexShards("data/search_index_history");
          historyTextState = "done";
        } catch (error) {
          console.warn(error);
          historyTextState = searchTextById.size ? "done" : "failed";
        }
        searchIndexLabel = searchTextById.size ? searchIndexStatusLabel() : "Text index unavailable";
        updateMeta();
        scheduleTextIndexRender(true);
      })();
    };
    updateMeta();
    render();
    const initialHotReportQuery = scopeFilter.value === "charts" ? "" : input.value.trim();
    if (!initialHotReportQuery) {
      const cachedFirstPage = readHotReportFirstPageCache(hotReportLocalStorage());
      if (cachedFirstPage) {
        hotReportPages = [cachedFirstPage];
        hotReportPageIndex = 0;
        hotReportActiveQuery = "";
        hotReportRequestedQuery = "";
        hotReportsLoaded = true;
        hotReportsFailed = false;
        cachedFirstPage.items.forEach((item) => hotReportItems.set(String(item.id), item));
      }
    }
    renderHotReports();
    loadHotReports(initialHotReportQuery);
    const backgroundFullCatalogPromise = startFullCatalogLoad();

    // The preview is useful immediately; the full catalog and the PDF override
    // overlay arrive independently and replace the derived indexes atomically.
    // No user input is lost while either request is in flight.
    let catalogPdfOverrides = [];
    let catalogOverrideVersion = 0;
    if (!fullCatalogReady) {
      backgroundFullCatalogPromise.then(async (fullCatalog) => {
        if (!fullCatalog || !Array.isArray(fullCatalog.items)) {
          updateCatalogReadiness("完整目录暂时未载入；当前可搜索最新报告和其他来源。", "error");
          remoteSourceStates.set("catalog", "error");
          renderRemoteSourceProgress(input.value.trim());
          return;
        }
        const previewRevision = String(catalog.updated_at_bjt || "");
        const fullRevision = String(fullCatalog.updated_at_bjt || "");
        const expectedTotal = Number(catalog.total_item_count || 0);
        if ((previewRevision && fullRevision && fullRevision < previewRevision)
          || (expectedTotal > 0 && Number(fullCatalog.item_count || 0) < expectedTotal)) {
          try {
            fullCatalog = await loadJson(`data/catalog.json?revision=${encodeURIComponent(previewRevision)}`, { cache: "reload" });
          } catch (error) {
            console.warn(error);
          }
        }
        if (!fullCatalog || !Array.isArray(fullCatalog.items)
          || (previewRevision && String(fullCatalog.updated_at_bjt || "") < previewRevision)
          || (expectedTotal > 0 && Number(fullCatalog.item_count || 0) < expectedTotal)) {
          updateCatalogReadiness("完整目录版本仍在同步；当前继续使用最新报告和其他来源。", "error");
          remoteSourceStates.set("catalog", "error");
          renderRemoteSourceProgress(input.value.trim());
          return;
        }
        updateCatalogReadiness("完整目录已下载，正在平滑建立本地检索索引…", "searching");
        await rebuildCatalogDerivedInChunks(fullCatalog, catalogPdfOverrides);
        fullCatalogReady = true;
        remoteSourceStates.set("catalog", "done");
        renderRemoteSourceProgress(input.value.trim());
        updateMeta();
        render({ resetPage: earlyInputTouched || Boolean(input.value.trim()) });
        renderHotReports();
        updateCatalogReadiness(`完整目录已就绪，共 ${items.length} 份报告。`, "ready");
      });
    }
    loadCatalogPdfOverrides(workerUrl).then((overrides) => {
      catalogPdfOverrides = Array.isArray(overrides) ? overrides : [];
      catalogOverrideVersion += 1;
      if (!catalogPdfOverrides.length) return;
      if (!fullCatalogReady) return;
      rebuildCatalogDerivedInChunks(catalog, catalogPdfOverrides, catalogOverrideVersion).then(() => {
        updateMeta();
        render({ resetPage: false });
      });
    });
    if (earlyInputTouched || input.value.trim()) scheduleLocalRender(0);
  }

  function filenameFromDisposition(disposition, fallback) {
    const header = String(disposition || "");
    const utfMatch = header.match(/filename\*=UTF-8''([^;]+)/i);
    if (utfMatch) return decodeURIComponent(utfMatch[1]);
    const plainMatch = header.match(/filename="?([^";]+)"?/i);
    if (plainMatch) return plainMatch[1];
    return fallback || "report.pdf";
  }

  function triggerBlobDownload(blob, disposition, fallbackName) {
    const objectUrl = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = objectUrl;
    link.download = filenameFromDisposition(disposition, fallbackName);
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(objectUrl);
  }

  function field(label, value) {
    return `
      <div class="detail-field">
        <span>${escapeHtml(label)}</span>
        <strong>${escapeHtml(value || "-")}</strong>
      </div>
    `;
  }

  function importantTokens(text) {
    const counts = new Map();
    for (const token of queryTokens(text)) {
      if (token.length < 3 || STOPWORDS.has(token) || /^\d+$/.test(token)) continue;
      counts.set(token, (counts.get(token) || 0) + 1);
    }
    return [...counts.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, 16)
      .map(([token]) => token);
  }

  function relatedReports(current, items, searchTextById) {
    const currentIndustry = inferIndustry(current);
    const currentBank = bankKey(current);
    const currentDate = dateSortValue(current);
    const keywords = importantTokens(`${current.title} ${current.title_zh || ""} ${(searchTextById.get(current.id) || "").slice(0, 6000)}`);

    const scored = items
      .filter((item) => item.id !== current.id)
      .map((item) => {
        let score = 0;
        if (inferIndustry(item) === currentIndustry) score += 34;
        if (bankKey(item) === currentBank) score += 18;
        if (dateSortValue(item) === currentDate) score += 5;

        const title = normalize(`${item.title || ""} ${item.title_zh || ""}`);
        const text = searchTextById.get(item.id) || "";
        for (const token of keywords) {
          if (title.includes(token)) score += 8;
          if (text.includes(token)) score += 2;
        }
        return { item, score };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return dateSortValue(b.item) - dateSortValue(a.item);
      });

    return scored.slice(0, 6).map((entry) => entry.item);
  }

  function docDateSortValue(item) {
    return Number((isoDateFromValue(item.date) || itemDate(item)).replace(/-/g, "")) || 0;
  }

  function relatedQueryForDoc(item) {
    const title = [item.title_cn, item.title].filter(Boolean).join(" ");
    const chunks = title
      .split(/[\s,，:：;；|｜/\\()[\]（）【】「」"'“”‘’]+/u)
      .map((part) => part.trim())
      .filter((part) => part.length >= 2 && part.length <= 32)
      .slice(0, 4);
    const tokens = importantTokens(`${title} ${item.institution || ""} ${item.category || ""} ${item.report_type || ""}`)
      .filter((token) => token.length <= 24)
      .slice(0, 5);
    const merged = [...chunks, ...tokens].filter(Boolean);
    const deduped = [];
    const seen = new Set();
    for (const value of merged) {
      const key = normalize(value);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      deduped.push(value);
    }
    return (deduped.join(" ") || title || item.institution || "").slice(0, 120).trim();
  }

  function catalogRelatedForDoc(current, items, searchTextById, limit = 4) {
    const currentIndustry = inferIndustry(current);
    const currentInstitution = normalize(current.institution || "");
    const currentDate = docDateSortValue(current);
    const keywords = queryTokens([
      relatedQueryForDoc(current),
      current.title,
      current.title_cn,
      current.institution,
      current.category,
      current.report_type,
    ].join(" "))
      .filter((token) => token.length >= 2 && !STOPWORDS.has(token) && !/^\d{1,3}$/.test(token))
      .slice(0, 18);

    return items
      .map((item) => {
        let score = 0;
        if (currentIndustry !== "Other" && inferIndustry(item) === currentIndustry) score += 30;
        if (currentInstitution && normalize(bankLabel(item)).includes(currentInstitution)) score += 20;
        if (currentDate && Math.abs(dateSortValue(item) - currentDate) <= 7) score += 4;

        const title = normalize(`${item.title || ""} ${item.title_zh || ""}`);
        const meta = normalize(metadataText(item));
        const text = searchTextById.get(item.id) || "";
        for (const token of keywords) {
          if (title.includes(token)) score += 10;
          if (meta.includes(token)) score += 4;
          if (text.includes(token)) score += 2;
        }
        return { item, score };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return dateSortValue(b.item) - dateSortValue(a.item);
      })
      .slice(0, limit)
      .map((entry) => entry.item);
  }

  async function fetchDocRelatedSource(workerUrl, endpoint, query, source, current, limit, timeoutMs = 2500) {
    if (!workerUrl || !query) return [];
    const controller = new AbortController();
    const timeoutId = window.setTimeout(() => controller.abort(), timeoutMs);
    try {
      const response = await fetch(`${workerUrl}/${endpoint}?q=${encodeURIComponent(query)}`, {
        cache: "no-store",
        signal: controller.signal,
      });
      if (!response.ok) return [];
      const data = await response.json().catch(() => ({}));
      const items = Array.isArray(data.items) ? data.items : [];
      return items
        .map((item) => publicSearchItem({ ...item, source: item.source || source }, item.source || source))
        .filter((item) => !(item.source === current.source && String(item.id) === String(current.id)))
        .slice(0, limit);
    } finally {
      window.clearTimeout(timeoutId);
    }
  }

  function hotReportCommentsMarkup() {
    return `
      <section class="hot-comments-section" id="hotReportComments" aria-labelledby="hotReportCommentsTitle">
        <div class="related-heading hot-comments-heading">
          <h3 id="hotReportCommentsTitle">评论</h3>
          <span id="hotReportCommentCount"></span>
        </div>
        <div id="hotReportCommentList" class="hot-comment-list"></div>
        <div id="hotReportCommentLogin" class="hot-comment-login" hidden>
          <span>注册或登录后即可评论。</span>
          <button class="secondary-button" id="hotReportCommentLoginButton" type="button">注册 / 登录</button>
        </div>
        <form id="hotReportCommentForm" class="hot-comment-form" hidden>
          <div id="hotReportCommentAdminAlias" class="hot-comment-admin-alias" hidden>
            <label>
              <span>管理员评论昵称</span>
              <input id="hotReportCommentAlias" type="text" maxlength="48" autocomplete="off" placeholder="随机用户名或自定义昵称">
            </label>
            <button class="secondary-button" id="hotReportRandomAlias" type="button">生成随机用户名</button>
          </div>
          <textarea id="hotReportCommentBody" rows="4" maxlength="1200" placeholder="写下你的评论…" required></textarea>
          <div class="hot-comment-form-actions">
            <span>最多 1200 字</span>
            <button class="primary" type="submit">发布评论</button>
          </div>
        </form>
        <div id="hotReportCommentStatus" class="status-line" aria-live="polite"></div>
      </section>
    `;
  }

  function randomHotCommentAlias() {
    const prefixes = ["山岚", "星河", "远帆", "青禾", "云杉", "海盐", "南风", "北辰", "纸鸢", "松果"];
    const suffixes = ["观察员", "研究者", "读报人", "分析室", "笔记本", "望远镜", "资料员", "思考者"];
    return `${prefixes[Math.floor(Math.random() * prefixes.length)]}${suffixes[Math.floor(Math.random() * suffixes.length)]}${Math.floor(10 + Math.random() * 90)}`;
  }

  function hotCommentTime(value) {
    const timestamp = Date.parse(value || "");
    if (!Number.isFinite(timestamp)) return "";
    return new Intl.DateTimeFormat("zh-CN", {
      year: "numeric",
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
      timeZone: "Asia/Shanghai",
    }).format(new Date(timestamp));
  }

  function hotCommentRow(comment, canOrder) {
    return `
      <article class="hot-comment" data-comment-id="${escapeHtml(comment.id)}">
        <div class="hot-comment-meta">
          <strong>${escapeHtml(publicDisplayName(comment.display_name))}</strong>
          <time>${escapeHtml(hotCommentTime(comment.created_at))}</time>
          ${canOrder ? `
            <span class="hot-comment-order-actions">
              <button class="secondary-button" type="button" data-action="comment-up" data-id="${escapeHtml(comment.id)}" aria-label="评论上移">↑</button>
              <button class="secondary-button" type="button" data-action="comment-down" data-id="${escapeHtml(comment.id)}" aria-label="评论下移">↓</button>
            </span>
          ` : ""}
        </div>
        <p>${escapeHtml(publicBrandText(comment.body))}</p>
      </article>
    `;
  }

  function initHotReportComments(item, workerUrl) {
    const section = document.getElementById("hotReportComments");
    const list = document.getElementById("hotReportCommentList");
    const count = document.getElementById("hotReportCommentCount");
    const login = document.getElementById("hotReportCommentLogin");
    const loginButton = document.getElementById("hotReportCommentLoginButton");
    const form = document.getElementById("hotReportCommentForm");
    const body = document.getElementById("hotReportCommentBody");
    const submit = form && form.querySelector("button[type='submit']");
    const adminAlias = document.getElementById("hotReportCommentAdminAlias");
    const alias = document.getElementById("hotReportCommentAlias");
    const randomAlias = document.getElementById("hotReportRandomAlias");
    const status = document.getElementById("hotReportCommentStatus");
    if (!section || !list || !form || !body || !submit || !status || !workerUrl) return;
    let comments = [];

    function setStatus(text, kind) {
      status.className = kind ? `status-line ${kind}` : "status-line";
      status.textContent = text || "";
    }

    function render() {
      const session = loadAuthSession();
      const canOrder = isSuperSession(session);
      if (count) count.textContent = comments.length ? `${comments.length} 条` : "";
      list.innerHTML = comments.length
        ? comments.map((comment) => hotCommentRow(comment, canOrder)).join("")
        : '<div class="empty-state">还没有评论，来写第一条吧。</div>';
      if (login) login.hidden = Boolean(session);
      form.hidden = !session;
      if (adminAlias) adminAlias.hidden = !canOrder;
    }

    async function loadComments() {
      setStatus("正在读取评论…");
      try {
        const response = await fetch(`${workerUrl}/hot-reports/comments?report_id=${encodeURIComponent(item.id)}`, { cache: "no-store" });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "评论读取失败。");
        comments = Array.isArray(data.comments) ? data.comments : [];
        setStatus("");
        render();
      } catch (error) {
        setStatus(error.message || "评论暂时无法读取。", "error");
      }
    }

    async function saveCommentOrder(nextComments) {
      setStatus("正在保存评论顺序…");
      const response = await fetch(`${workerUrl}/hot-reports/comments/order`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({
          report_id: item.id,
          ordered_ids: nextComments.map((comment) => comment.id),
        }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.detail || "评论排序保存失败。");
      comments = Array.isArray(data.comments) ? data.comments : nextComments;
      setStatus("评论顺序已保存。", "ok");
      render();
    }

    list.addEventListener("click", async (event) => {
      const button = event.target.closest("button[data-action]");
      if (!button || !isSuperSession()) return;
      const index = comments.findIndex((comment) => comment.id === button.dataset.id);
      const direction = button.dataset.action === "comment-up" ? -1 : 1;
      const destination = index + direction;
      if (index < 0 || destination < 0 || destination >= comments.length) return;
      const next = comments.slice();
      [next[index], next[destination]] = [next[destination], next[index]];
      button.disabled = true;
      try {
        await saveCommentOrder(next);
      } catch (error) {
        setStatus(error.message || "评论排序保存失败。", "error");
        await loadComments();
      }
    });

    if (loginButton) loginButton.addEventListener("click", () => showAccountModal(workerUrl, { item, source: HOT_REPORT_SOURCE }));
    if (randomAlias && alias) randomAlias.addEventListener("click", () => {
      if (!isSuperSession()) return;
      alias.value = randomHotCommentAlias();
      alias.focus();
    });
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (!loadAuthSession()) {
        showAccountModal(workerUrl, { item, source: HOT_REPORT_SOURCE });
        return;
      }
      const text = String(body.value || "").trim();
      if (!text) return;
      submit.disabled = true;
      setStatus("正在发布评论…");
      try {
        const response = await fetch(`${workerUrl}/hot-reports/comments`, {
          method: "POST",
          headers: { "Content-Type": "application/json", ...authHeaders() },
          body: JSON.stringify({
            report_id: item.id,
            body: text,
            author_alias: isSuperSession() && alias ? alias.value.trim() : "",
          }),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "评论发布失败。");
        body.value = "";
        setStatus("评论已发布。", "ok");
        await loadComments();
      } catch (error) {
        setStatus(error.message || "评论发布失败。", "error");
      } finally {
        submit.disabled = false;
      }
    });
    document.addEventListener("portal-auth-change", render);
    render();
    loadComments();
  }

  function externalRelatedMarkup() {
    return `
      <section class="related-section external-related-section" id="externalRelatedSection" hidden aria-labelledby="externalRelatedTitle">
        <div class="related-heading">
          <h3 id="externalRelatedTitle">Related Reports</h3>
        </div>
        <div id="externalRelatedStatus" class="status-line" aria-live="polite"></div>
        <div class="related-list" id="externalRelatedList"></div>
      </section>
    `;
  }

  function docRelatedRow(item) {
    let markup;
    if (item.source === HOT_REPORT_SOURCE) markup = hotReportRow(item);
    else if (item.source === EXTERNAL_SOURCE) markup = externalRow(item);
    else if (item.source === THINKTANK_SOURCE) markup = thinkTankRow(item);
    else if (item.source === REPORT_A_SOURCE) markup = reportARow(item);
    else if (item.source === AUTHORITY_SOURCE) markup = authorityRow(item);
    else markup = relatedRow(item);
    return markup.replace(
      "<a ",
      `<a data-recommendation-source="${escapeHtml(item.source || "catalog")}" `,
    );
  }

  async function initExternalRelated(item, workerUrl, catalogItems, searchTextById, catalogItemsPromise = null) {
    const section = document.getElementById("externalRelatedSection");
    const list = document.getElementById("externalRelatedList");
    const status = document.getElementById("externalRelatedStatus");
    if (!section || !list || !status) return;

    const query = relatedQueryForDoc(item);
    const sourceOrder = ["catalog", THINKTANK_SOURCE, EXTERNAL_SOURCE, REPORT_A_SOURCE, AUTHORITY_SOURCE];
    const rowsBySource = new Map(sourceOrder.map((source) => [source, []]));
    const seen = new Set();
    function append(sourceItems, source) {
      const bucket = rowsBySource.get(source) || [];
      if (!rowsBySource.has(source)) rowsBySource.set(source, bucket);
      for (const sourceItem of sourceItems) {
        const key = `${source}:${sourceItem.id}`;
        if (!sourceItem.id || seen.has(key)) continue;
        seen.add(key);
        bucket.push({ ...sourceItem, source });
      }
    }

    function replace(sourceItems, source) {
      for (const key of [...seen]) {
        if (key.startsWith(`${source}:`)) seen.delete(key);
      }
      rowsBySource.set(source, []);
      append(sourceItems, source);
    }

    function renderedRows() {
      return sourceOrder.flatMap((source) => rowsBySource.get(source) || []).slice(0, 14);
    }

    let usingProvisionalCatalog = false;
    let pendingSources = (workerUrl && query ? 4 : 0) + (catalogItemsPromise ? 1 : 0);
    function render() {
      const rendered = renderedRows();
      if (rendered.length) {
        section.hidden = false;
        status.className = "status-line";
        status.textContent = usingProvisionalCatalog
          ? (pendingSources ? "先显示近期报告；更相关结果仍在补充…" : "暂未找到更相关结果，已显示近期报告。")
          : (pendingSources ? "更多相关报告仍在补充…" : "");
        list.innerHTML = rendered.map(docRelatedRow).join("");
        return;
      }
      if (pendingSources) {
        section.hidden = false;
        status.className = "status-line";
        status.textContent = "正在推荐相关报告…";
        list.innerHTML = `
          <div class="loading-state">
            <span class="loading-spinner" aria-hidden="true"></span>
            <span>正在推荐相关报告…</span>
          </div>
        `;
        return;
      }
      section.hidden = true;
      status.textContent = "";
      list.innerHTML = "";
    }

    list.addEventListener("click", (event) => {
      const row = event.target.closest(".related-row");
      if (!row) return;
      const source = String(row.dataset.recommendationSource || "catalog");
      const relatedItem = (rowsBySource.get(source) || [])
        .find((candidate) => String(candidate.id || "") === String(row.dataset.id || ""));
      trackEvent(workerUrl, "report_open", {
        ...analyticsReportPayload(relatedItem || { id: row.dataset.id }, source),
        placement: "report_related",
        parent_report_id: String(item.id || ""),
      });
    });

    const previewRecommendations = catalogRelatedForDoc(item, catalogItems, searchTextById, 4);
    if (previewRecommendations.length) {
      append(previewRecommendations, "catalog");
    } else {
      const recentFallback = (Array.isArray(catalogItems) ? catalogItems : [])
        .filter((candidate) => candidate && candidate.id && String(candidate.id) !== String(item.id || ""))
        .slice(0, 4);
      if (recentFallback.length) {
        append(recentFallback, "catalog");
        usingProvisionalCatalog = true;
      }
    }
    render();

    if (catalogItemsPromise) {
      Promise.resolve(catalogItemsPromise).then((completeCatalogItems) => {
        const completeRecommendations = catalogRelatedForDoc(
          item,
          Array.isArray(completeCatalogItems) ? completeCatalogItems : [],
          searchTextById,
          4,
        );
        if (completeRecommendations.length) {
          replace(completeRecommendations, "catalog");
          usingProvisionalCatalog = false;
        }
      }).catch(() => {
        // Preview and remote recommendations remain available.
      }).finally(() => {
        pendingSources -= 1;
        render();
      });
    }

    const remoteSources = workerUrl && query ? [
      ["thinktank/search", THINKTANK_SOURCE, 4],
      ["external/search", EXTERNAL_SOURCE, 4],
      ["report-a/search", REPORT_A_SOURCE, 3],
      ["authority/search", AUTHORITY_SOURCE, 3],
    ] : [];
    await Promise.allSettled(remoteSources.map(async ([endpoint, source, limit]) => {
      try {
        const remoteItems = await fetchDocRelatedSource(workerUrl, endpoint, query, source, item, limit);
        if (remoteItems.length && usingProvisionalCatalog) {
          replace([], "catalog");
          usingProvisionalCatalog = false;
        }
        append(remoteItems, source);
      } catch (_error) {
        // One unavailable source must not clear recommendations already shown.
      } finally {
        pendingSources -= 1;
        render();
      }
    }));
  }

  function downloadErrorMessage(status, message, data) {
    const text = String(message || "");
    if (data && data.limit_exceeded) return localizedContactText(text || "3天体验下载已满 10 篇。");
    if (
      data && data.archived ||
      status === 404 && /pdf|object|mirrored|archived|not found/i.test(text)
    ) {
      return "PDF 暂不可用。";
    }
    if (/password/i.test(text)) return localizedContactText(text);
    if (/configured/i.test(text)) return "PDF download is temporarily unavailable. Please try again later.";
    return localizedContactText(text) || "Download failed.";
  }

  function maybeAlertDownloadLimit(message, workerUrl, context = {}) {
    const text = String(message || "");
    if (/体验下载已满|limit_exceeded/i.test(text) && /体验|limit_exceeded/i.test(text)) {
      showAccountModal(workerUrl, { ...context, requestKind: "access" });
      return true;
    }
    return false;
  }

  function adminPanelMarkup() {
    return `
      <section class="admin-panel" id="adminPanel" hidden>
        <div class="admin-panel-heading">
          <h3>Delivery link</h3>
          <span>Private</span>
        </div>
        <div class="delivery-row">
          <button class="primary" id="generateDeliveryLink" type="button">Generate</button>
          <input id="deliveryLinkInput" type="text" readonly aria-label="Delivery link">
          <button id="copyDeliveryLink" type="button">Copy</button>
        </div>
        <div id="deliveryStatus" class="status-line" aria-live="polite"></div>
      </section>
    `;
  }

  function textOnlyPdfUploadMarkup() {
    return `
      <section class="text-only-pdf-upload" id="textOnlyPdfUpload" hidden>
        <div class="admin-panel-heading">
          <h3>补传 PDF</h3>
          <span>仅 KC桌面管理员</span>
        </div>
        <p class="subtle">为当前 Text only 报告补充原始 PDF。上传成功后，原报告 id、标题、全文索引和权限规则保持不变。</p>
        <form id="textOnlyPdfUploadForm" class="text-only-pdf-upload-form">
          <input id="textOnlyPdfFile" name="pdf" type="file" accept="application/pdf,.pdf" required>
          <button class="primary" id="textOnlyPdfUploadButton" type="submit">上传 PDF</button>
        </form>
        ${adminPdfUploadProgressMarkup("textOnlyPdfUpload")}
        <div id="textOnlyPdfUploadStatus" class="status-line" aria-live="polite"></div>
      </section>
    `;
  }

  function textOnlySearchHref(item) {
    const query = titleText(item).slice(0, 200);
    return `./?q=${encodeURIComponent(query)}`;
  }

  function textOnlySearchGuidanceMarkup(item) {
    return `
      <aside class="text-only-search-guidance" aria-label="寻找可下载版本">
        <strong>先搜索同名可下载版本</strong>
        <p>约 90% 的 Text only 报告可在首页按完整标题找到可下载版本，建议继续查看“其他报告”等板块。</p>
        <a class="secondary-button" href="${escapeHtml(textOnlySearchHref(item))}">在首页搜索同名报告</a>
      </aside>
    `;
  }

  function textOnlyTextAccessMarkup() {
    return `
      <section class="text-only-text-access" id="textOnlyTextAccess">
        <div class="admin-panel-heading">
          <h3>原始文本（Text only）</h3>
          <span>1个月及以上 · 须在授权范围</span>
        </div>
        <p class="subtle">这份报告目前没有可下载 PDF。登录后，会员时长达到 1 个月且报告在账号授权范围内，即可分页查看已保存的提取文本。</p>
        <div class="text-only-text-actions">
          <button class="primary" id="viewTextOnlyText" type="button">查看原始文本</button>
        </div>
        <p class="subtle">${accessContactGuidanceHtml()}</p>
        <div id="textOnlyTextStatus" class="status-line" aria-live="polite"></div>
        <div id="textOnlyTextContent" class="text-only-text-content" hidden>
          <div id="textOnlyTextSource" class="text-only-text-source"></div>
          <pre id="textOnlyTextBody" tabindex="0"></pre>
          <button class="secondary-button" id="loadMoreTextOnlyText" type="button" hidden>继续加载</button>
        </div>
      </section>
    `;
  }

  function initTextOnlyTextAccess(item, workerUrl) {
    const panel = document.getElementById("textOnlyTextAccess");
    const openButton = document.getElementById("viewTextOnlyText");
    const status = document.getElementById("textOnlyTextStatus");
    const content = document.getElementById("textOnlyTextContent");
    const source = document.getElementById("textOnlyTextSource");
    const body = document.getElementById("textOnlyTextBody");
    const loadMore = document.getElementById("loadMoreTextOnlyText");
    if (!panel || !openButton || !status || !content || !source || !body || !loadMore || !workerUrl) return;

    let nextCursor = "";
    let requestGeneration = 0;
    let requestInProgress = false;
    let activeSessionIdentity = null;
    const loadedCursors = new Set();

    function sessionIdentity(session) {
      if (!session || !session.user) return "signed-out";
      const user = session.user;
      return [
        "signed-in",
        user.id,
        String(user.email || "").trim().toLowerCase(),
        String(user.username || "").trim().toLowerCase(),
        user.role,
        user.disabled === true ? "disabled" : "enabled",
      ].map((value) => String(value || "")).join("\u001f");
    }

    function paginationError(message) {
      const error = new Error(message);
      error.pagination = true;
      return error;
    }

    function resetText() {
      requestGeneration += 1;
      requestInProgress = false;
      nextCursor = "";
      loadedCursors.clear();
      content.hidden = true;
      source.textContent = "";
      body.textContent = "";
      loadMore.hidden = true;
      loadMore.disabled = false;
      openButton.disabled = false;
    }

    function refreshSession() {
      const session = loadAuthSession();
      const identity = sessionIdentity(session);
      const identityChanged = identity !== activeSessionIdentity;
      activeSessionIdentity = identity;
      if (identityChanged) resetText();
      openButton.textContent = session ? "查看原始文本" : "注册 / 登录后查看";
      if (identityChanged) {
        status.className = "status-line";
        status.textContent = session
          ? "点击后将核验这份报告的会员权限。"
          : "请先注册或登录；需至少 1 个月会员且报告在账号授权范围内。";
      }
    }

    async function loadText(cursor = "") {
      if (requestInProgress) return;
      const session = loadAuthSession();
      if (!session) {
        showAccountModal(workerUrl, { item, source: "catalog" });
        return;
      }
      const requestedCursor = String(cursor || "");
      if (requestedCursor && requestedCursor !== nextCursor) {
        status.className = "status-line error";
        status.textContent = "文本分页状态已变化，请重新点击“查看原始文本”。";
        return;
      }
      const generation = requestGeneration;
      const requestToken = String(session.token || "");
      requestInProgress = true;
      openButton.disabled = true;
      loadMore.disabled = true;
      status.className = "status-line";
      status.textContent = requestedCursor ? "正在继续加载文本…" : "正在核验权限并读取文本…";
      try {
        const params = new URLSearchParams({ report_id: String(item.id || "") });
        if (requestedCursor) params.set("cursor", requestedCursor);
        const response = await fetch(`${workerUrl}/report-text?${params.toString()}`, {
          cache: "no-store",
          headers: { "Authorization": `Bearer ${requestToken}` },
        });
        const data = await response.json().catch(() => ({}));
        if (generation !== requestGeneration) return;
        if (!response.ok) {
          if (response.status === 401) {
            const currentSession = loadAuthSession();
            if (String(currentSession && currentSession.token || "") === requestToken) {
              clearAuthSession();
              return;
            }
          }
          const fallback = response.status === 401
            ? "登录状态已更新，请重新点击查看。"
            : response.status === 403
              ? "当前账号无权查看这份原始文本；可能是会员时长不足，或报告 / 机构不在授权范围内。"
              : response.status === 404
                ? "这份报告暂时没有可读取的原始文本。"
                : response.status === 400
                  ? "文本分页已过期或无效，请重新点击“查看原始文本”。"
                  : "原始文本读取失败，请稍后重试。";
          const error = new Error([400, 401, 403, 404].includes(response.status) ? fallback : (data.detail || fallback));
          error.status = response.status;
          error.pagination = response.status === 400;
          throw error;
        }
        if (typeof data.text !== "string" || typeof data.has_more !== "boolean") {
          throw paginationError("原始文本接口返回的数据格式不完整。请重新点击查看。");
        }
        if (data.report_id !== undefined
          && data.report_id !== null
          && String(data.report_id) !== String(item.id || "")) {
          throw paginationError("原始文本接口返回的报告不匹配。请重新点击查看。");
        }
        const responseCursor = String(data.next_cursor || "");
        if (data.has_more && !responseCursor) {
          throw paginationError("文本尚未加载完成，但接口没有返回下一页游标。请重新点击查看。");
        }
        if (!data.has_more && responseCursor) {
          throw paginationError("原始文本分页状态不一致。请重新点击查看。");
        }
        if (responseCursor && (responseCursor === requestedCursor || loadedCursors.has(responseCursor))) {
          throw paginationError("原始文本分页游标发生循环。请重新点击查看。");
        }
        loadedCursors.add(requestedCursor);
        const chunk = data.text;
        body.textContent += chunk;
        source.textContent = String(data.source_label || "提取文本");
        nextCursor = responseCursor;
        content.hidden = false;
        loadMore.hidden = !Boolean(data.has_more && nextCursor);
        status.textContent = loadMore.hidden ? "文本已全部加载。" : "已加载部分文本，可继续加载。";
        status.classList.add("ok");
        trackEvent(workerUrl, "report_text_view", {
          ...analyticsReportPayload(item, "catalog"),
          action: requestedCursor ? "load_more" : "open",
          source_label: String(data.source_label || ""),
        });
      } catch (error) {
        if (generation !== requestGeneration) return;
        if (Number(error && error.status) === 403) {
          resetText();
        }
        if (error && error.pagination === true) {
          nextCursor = "";
          loadMore.hidden = true;
        }
        status.className = "status-line error";
        status.textContent = localizedContactText(error.message || "原始文本读取失败，请稍后重试。");
      } finally {
        if (generation === requestGeneration) {
          requestInProgress = false;
          openButton.disabled = false;
          loadMore.disabled = false;
        }
      }
    }

    openButton.addEventListener("click", () => {
      if (!loadAuthSession()) {
        showAccountModal(workerUrl, { item, source: "catalog" });
        return;
      }
      resetText();
      loadText();
    });
    loadMore.addEventListener("click", () => {
      if (nextCursor) loadText(nextCursor);
    });
    document.addEventListener("portal-auth-change", refreshSession);
    refreshSession();
  }

  function initTextOnlyPdfUpload(item, workerUrl) {
    const panel = document.getElementById("textOnlyPdfUpload");
    const form = document.getElementById("textOnlyPdfUploadForm");
    const fileInput = document.getElementById("textOnlyPdfFile");
    const button = document.getElementById("textOnlyPdfUploadButton");
    const status = document.getElementById("textOnlyPdfUploadStatus");
    if (!panel || !form || !fileInput || !button || !status || !workerUrl) return;

    function setStatus(message, state = "") {
      status.className = state ? `status-line ${state}` : "status-line";
      status.textContent = localizedContactText(message || "");
    }

    function completeUpload() {
      setStatus("PDF 已补齐并发布，正在刷新原报告状态…", "ok");
      window.setTimeout(() => window.location.reload(), 350);
    }

    function refreshVisibility() {
      panel.hidden = isPdfAvailable(item) || !isSuperSession();
    }

    refreshVisibility();
    document.addEventListener("portal-auth-change", refreshVisibility);
    fileInput.addEventListener("change", () => resetAdminPdfUploadId(fileInput));
    const cancel = document.getElementById("textOnlyPdfUploadCancel");
    const check = document.getElementById("textOnlyPdfUploadCheck");
    if (cancel) cancel.addEventListener("click", () => {
      if (activeAdminPdfUpload && typeof activeAdminPdfUpload.cancel === "function") activeAdminPdfUpload.cancel();
    });
    if (check) check.addEventListener("click", async () => {
      const saved = readAdminPdfUploadSession();
      if (!saved || saved.mode !== "text-only" || saved.target_id !== String(item.id || "")) {
        setStatus("没有这份报告可检查的上传记录。", "error");
        return;
      }
      check.disabled = true;
      try {
        await checkAdminPdfUploadResult(workerUrl, saved, {
          prefix: "textOnlyPdfUpload",
          fileInput,
          setStatus,
          onComplete: completeUpload,
        });
      } catch (error) {
        setStatus(error.message || "上传状态读取失败，请稍后再检查。", "error");
      } finally {
        check.disabled = false;
      }
    });

    const restored = readAdminPdfUploadSession();
    if (restored && restored.mode === "text-only" && restored.target_id === String(item.id || "")) {
      renderAdminPdfUploadUi("textOnlyPdfUpload", {
        percent: restored.state === "uploading" ? 0 : 100,
        text: "检测到未确认结果，请先检查，不要重复上传。",
        startedAt: restored.started_at,
        canCancel: false,
        canCheck: true,
        state: restored.state,
      });
      setStatus(restoredAdminPdfUploadMessage(restored));
    }
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const unresolved = readAdminPdfUploadSession();
      if (unresolved) {
        setStatus("上一笔 PDF 上传结果尚未确认。请先点击“检查上传结果”，不要重复上传。", "error");
        return;
      }
      const pdf = fileInput.files && fileInput.files[0];
      if (!isSuperSession()) {
        setStatus("请先登录 KC桌面管理员账号。", "error");
        refreshVisibility();
        return;
      }
      if (!pdf) {
        setStatus("请选择 PDF 文件。", "error");
        return;
      }
      if (pdf.size <= 0 || pdf.size > 95 * 1024 * 1024) {
        setStatus("PDF 必须不超过 95 MB。", "error");
        return;
      }
      const formData = new FormData();
      formData.set("id", item.id);
      formData.set("pdf", pdf, pdf.name);
      button.disabled = true;
      fileInput.disabled = true;
      try {
        await runAdminPdfUpload({
          url: `${workerUrl}/account-admin/text-only-pdf`,
          formData,
          file: pdf,
          fileInput,
          uploadId: adminPdfUploadIdForFile(fileInput),
          kind: "text-only-pdf",
          mode: "text-only",
          source: "catalog",
          targetId: item.id,
          prefix: "textOnlyPdfUpload",
          setStatus,
        });
        completeUpload();
      } catch (error) {
        setStatus(error.message || "PDF 上传失败，请先检查结果。", "error");
        button.disabled = false;
        fileInput.disabled = false;
      }
    });
  }

  function accountAccessMarkup(item = {}) {
    const contactReport = isContactOnlyItem(item);
    return `
      <section class="account-access" id="accountAccess" hidden>
        <h3>${contactReport ? "会员下载" : "Account access"}</h3>
        <p class="subtle" id="accountAccessHint">${contactReport ? "3个月及以上会员可下载全文。" : "登录后可查看账号下载权限。"}</p>
        <div class="account-access-actions">
          <button class="secondary-button" id="openAccountPanel" type="button">注册 / 登录</button>
          <button class="primary" id="accountDownloadReport" type="button" hidden>账号下载</button>
        </div>
        <div id="accountAccessStatus" class="status-line" aria-live="polite"></div>
        <div class="account-admin-progress" id="accountDownloadProgress" hidden>
          <div class="account-admin-progress-track"><span></span></div>
          <small>等待下载…</small>
        </div>
      </section>
    `;
  }

  function setLineStatus(target, text, kind) {
    if (!target) return;
    target.className = kind ? `status-line ${kind}` : "status-line";
    target.textContent = localizedContactText(text);
  }

  function setLineHtmlStatus(target, html, kind) {
    if (!target) return;
    target.className = kind ? `status-line ${kind}` : "status-line";
    target.innerHTML = html || "";
  }

  async function fetchReportAccess(workerUrl, item, source) {
    const session = loadAuthSession();
    if (!session) return null;
    const endpoint = source === HOT_REPORT_SOURCE
      ? `${workerUrl}/hot-reports/access?report_id=${encodeURIComponent(item.id)}`
      : `${workerUrl}/entitlement?report_id=${encodeURIComponent(item.id)}&source=${encodeURIComponent(source)}`;
    const response = await fetch(
      endpoint,
      { cache: "no-store", headers: authHeaders() },
    );
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      if (response.status === 401) clearAuthSession();
      throw new Error(data.detail || "账号状态读取失败。");
    }
    return data;
  }

  async function downloadCatalogWithAccount(workerUrl, item, statusTarget) {
    const progress = document.getElementById("accountDownloadProgress");
    resetDownloadProgress(progress);
    let waitingPercent = 6;
    setDownloadMessage(progress, "正在建立安全下载连接…", waitingPercent);
    statusTarget("正在检查账号权益并准备文件…");
    const waitingTimer = window.setInterval(() => {
      waitingPercent = Math.min(34, waitingPercent + 4);
      setDownloadMessage(progress, "正在准备文件，请稍候…", waitingPercent);
    }, 450);
    trackEvent(workerUrl, "download_attempt", {
      ...analyticsReportPayload(item, "catalog"),
      action: "account_download",
    });
    let response;
    try {
      response = await fetch(`${workerUrl}/download`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ id: item.id }),
      });
    } catch (error) {
      resetDownloadProgress(progress);
      throw error;
    } finally {
      window.clearInterval(waitingTimer);
    }
    if (!response.ok) {
      resetDownloadProgress(progress);
      const data = await response.json().catch(() => ({}));
      if (response.status === 401) clearAuthSession();
      trackEvent(workerUrl, "download_error", {
        ...analyticsReportPayload(item, "catalog"),
        action: "account_download",
        status: String(response.status),
        error: data.error || "Download failed.",
      });
      throw new Error(downloadErrorMessage(response.status, data.error || "Download failed.", data));
    }
    statusTarget("文件已就绪，正在下载…");
    const blob = await responseBlobWithProgress(response, progress);
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
    setDownloadMessage(progress, "下载完成，浏览器正在保存文件。", 100);
    trackEvent(workerUrl, "download_success", {
      ...analyticsReportPayload(item, "catalog"),
      action: "account_download",
      status: "ok",
    });
    statusTarget("下载已开始。", "ok");
  }

  function initReportAccessControls(item, workerUrl, source, downloadHandler) {
    const panel = document.getElementById("accountAccess");
    if (!panel || !workerUrl) return;
    const openAccount = document.getElementById("openAccountPanel");
    const accountDownload = document.getElementById("accountDownloadReport");
    const hint = document.getElementById("accountAccessHint");
    const status = document.getElementById("accountAccessStatus");
    const passwordForm = document.getElementById("unlockForm") || document.getElementById("externalDetailForm");
    const isHotReport = source === HOT_REPORT_SOURCE;
    const isThreeMonthReport = isHotReport || isContactOnlyItem(item);
    const context = { item, source };

    function statusTarget(text, kind) {
      const requestKind = kind === "error" ? requestKindForVisibleMessage(text) : "";
      if (requestKind) setLineHtmlStatus(status, requestActionStatusHtml(text, requestKind), kind);
      else setLineStatus(status, text, kind);
    }

    function statusTargetHtml(html, kind) {
      setLineHtmlStatus(status, html, kind);
    }

    async function refresh() {
      if (panel.isConnected === false) return;
      const session = loadAuthSession();
      panel.hidden = false;
      if (passwordForm) passwordForm.hidden = false;
      accountDownload.hidden = true;
      openAccount.hidden = false;
      openAccount.textContent = session ? "签到 / 领取" : "注册 / 登录";
      if (!session) {
        hint.innerHTML = isThreeMonthReport
          ? "登录后可查看下载权限；需至少 3 个月会员。"
          : "登录后可查看账号下载权限。";
        statusTargetHtml(`请先注册或登录。${accessContactGuidanceHtml()}`);
        return;
      }
      hint.textContent = `当前账号：${authUserLabel(session)}`;
      statusTarget("正在读取账号权益…");
      try {
        const access = await fetchReportAccess(workerUrl, item, source);
        const summary = accountRightSummary(access);
        if (access && access.can_download) {
          accountDownload.hidden = false;
          if (passwordForm) passwordForm.hidden = true;
          hint.textContent = summary ? `当前账号已开通此报告下载权限，${summary}。` : "当前账号已开通此报告下载权限。";
          statusTarget(summary ? `可直接使用账号下载；${summary}。` : "可直接使用账号下载。", "ok");
        } else {
          if (passwordForm) passwordForm.hidden = false;
          if (isThreeMonthReport) {
            statusTargetHtml(`当前权益未达到 3 个月。${accessContactGuidanceHtml()}`);
          } else {
            statusTargetHtml(summary
              ? `当前账号有${summary}，但不包含此报告。${accessContactGuidanceHtml()}`
              : `当前账号尚未解锁此报告。${accessContactGuidanceHtml()}`);
          }
        }
      } catch (error) {
        if (passwordForm) passwordForm.hidden = false;
        statusTarget(error.message || "账号状态读取失败。", "error");
      }
    }

    openAccount.addEventListener("click", () => showAccountModal(workerUrl, context));
    accountDownload.addEventListener("click", async () => {
      const idleLabel = accountDownload.textContent || "账号下载";
      accountDownload.disabled = true;
      accountDownload.textContent = "准备中…";
      try {
        await downloadHandler(statusTarget);
      } catch (error) {
        const message = error.message || "下载失败。";
        const openedRequest = maybeAlertDownloadLimit(message, workerUrl, context);
        if (!openedRequest) {
          const requestKind = requestKindForVisibleMessage(message);
          if (requestKind) statusTargetHtml(requestActionStatusHtml(message, requestKind), "error");
          else statusTarget(message, "error");
        }
      } finally {
        accountDownload.disabled = false;
        accountDownload.textContent = idleLabel;
      }
    });
    document.addEventListener("portal-auth-change", refresh);
    document.addEventListener("portal-reward-change", refresh);
    refresh();
  }

  function reportPageUrl(id, options = {}) {
    const url = new URL("report.html", window.location.href);
    url.searchParams.set("id", id);
    if (options.password) url.searchParams.set("password", options.password);
    const preview = options.password ? null : reportPreviewItem(options.preview);
    if (preview) {
      const previewKeys = [
        "title", "title_zh", "filename", "date_folder", "bank_code", "bank_name",
        "size_bytes", "available", "industry", "sector", "category", "pdf_archived",
        "page_count",
      ];
      for (const key of previewKeys) {
        if (preview[key] === undefined || preview[key] === null || preview[key] === "") continue;
        const value = typeof preview[key] === "boolean" ? (preview[key] ? "1" : "0") : String(preview[key]);
        url.searchParams.set(key, value);
      }
    }
    return url.toString();
  }

  function openInNewTab(url) {
    const opened = window.open(url, "_blank");
    if (opened) {
      opened.opener = null;
    }
  }

  function openReportPage(id) {
    openInNewTab(reportPageUrl(id));
  }

  function reportPreviewItem(item) {
    if (!item || !item.id) return null;
    const safeItem = publicDocItem(item);
    const keys = [
      "id", "title", "title_zh", "filename", "date_folder", "bank_code", "bank_name",
      "password_group", "size_bytes", "available", "industry", "sector", "category",
      "pdf_archived", "page_count",
    ];
    return Object.fromEntries(keys.filter((key) => safeItem[key] !== undefined).map((key) => [key, safeItem[key]]));
  }

  function rememberReportPreview(item) {
    const preview = reportPreviewItem(item);
    if (!preview) return;
    try {
      const parsed = JSON.parse(localStorage.getItem(REPORT_PREVIEW_CACHE_KEY) || "{}");
      const cache = parsed && typeof parsed === "object" && !Array.isArray(parsed) ? parsed : {};
      cache[String(preview.id)] = { stored_at: Date.now(), item: preview };
      const entries = Object.entries(cache)
        .sort((left, right) => Number(right[1] && right[1].stored_at || 0) - Number(left[1] && left[1].stored_at || 0))
        .slice(0, REPORT_PREVIEW_CACHE_MAX_ITEMS);
      localStorage.setItem(REPORT_PREVIEW_CACHE_KEY, JSON.stringify(Object.fromEntries(entries)));
    } catch (_error) {
      // The detail shard remains the source of truth when storage is unavailable.
    }
  }

  function cachedReportPreview(id) {
    try {
      const cache = JSON.parse(localStorage.getItem(REPORT_PREVIEW_CACHE_KEY) || "{}");
      const row = cache && cache[String(id || "")];
      if (!row || Date.now() - Number(row.stored_at || 0) > REPORT_PREVIEW_CACHE_TTL_MS) return null;
      const item = reportPreviewItem(row.item);
      return item && String(item.id) === String(id || "") ? item : null;
    } catch (_error) {
      return null;
    }
  }

  function reportPreviewFromParams(params, id) {
    const reportId = String(id || params.get("id") || "").trim();
    const title = String(params.get("title") || "").trim();
    if (!reportId || !title) return null;
    const item = { id: reportId, title };
    const stringKeys = [
      "title_zh", "filename", "date_folder", "bank_code", "bank_name",
      "industry", "sector", "category",
    ];
    for (const key of stringKeys) {
      const value = String(params.get(key) || "").trim();
      if (value) item[key] = value;
    }
    for (const key of ["size_bytes", "page_count"]) {
      const value = Number(params.get(key));
      if (Number.isFinite(value) && value >= 0) item[key] = value;
    }
    for (const key of ["available", "pdf_archived"]) {
      const value = params.get(key);
      if (value === "1" || value === "true") item[key] = true;
      if (value === "0" || value === "false") item[key] = false;
    }
    return reportPreviewItem(item);
  }

  function deliveryPageUrl(id, password, preview = null) {
    return reportPageUrl(id, { password, preview });
  }

  function externalPageUrl(item, password, options = {}) {
    item = publicDocItem(item) || {};
    const url = new URL("doc.html", window.location.href);
    url.searchParams.set("id", item.id);
    if (password) url.searchParams.set("password", password);
    if (password) return url.toString();
    const compact = options.compact === true;
    const requestToken = String(item && item.request_token || "").trim();
    if (!compact && ["authority", "report-a"].includes(String(item && item.source || "")) && requestToken) {
      url.searchParams.set("rt", requestToken.slice(0, 4096));
    }
    const previewKeys = compact
      ? ["source", "title", "title_cn", "institution", "date", "kind", "kind_label", "page_count", "category", "author"]
      : [
        "source", "title", "title_cn", "institution", "date", "file_type", "kind",
        "kind_label", "page_count", "size_bytes", "report_type", "language", "category",
        "author", "rating", "description", "filename", "required_plan",
      ];
    for (const key of previewKeys) {
      const value = item && item[key];
      if (value === undefined || value === null || value === "") continue;
      url.searchParams.set(key, String(value).slice(0, key.includes("title") ? 320 : 160));
    }
    return url.toString();
  }

  async function requestReportPassword(workerUrl, id) {
    const token = getAdminToken();
    if (!canUseDeliveryTools()) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ id, token }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        if (response.status === 401) clearAdminToken();
        const fallback = response.status >= 500 ? getAdminPlainKey() : "";
        if (fallback) return { id, password: fallback };
        throw new Error(data.error || "Could not generate delivery link.");
      }
      return data;
    } catch (error) {
      const fallback = getAdminPlainKey();
      if (fallback) return { id, password: fallback };
      throw error;
    }
  }

  async function requestExternalPassword(workerUrl, id, source = EXTERNAL_SOURCE) {
    const token = getAdminToken();
    if (!canUseDeliveryTools()) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ id, token, source }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        if (response.status === 401) clearAdminToken();
        const fallback = response.status >= 500 ? getAdminPlainKey() : "";
        if (fallback) return { id, password: fallback };
        throw new Error(data.error || "Could not generate delivery link.");
      }
      return data;
    } catch (error) {
      const fallback = getAdminPlainKey();
      if (fallback) return { id, password: fallback };
      throw error;
    }
  }

  function initDetailAdmin(item, workerUrl) {
    const panel = document.getElementById("adminPanel");
    const generate = document.getElementById("generateDeliveryLink");
    const linkInput = document.getElementById("deliveryLinkInput");
    const copy = document.getElementById("copyDeliveryLink");
    const status = document.getElementById("deliveryStatus");
    if (!panel || !generate || !linkInput || !copy || !status) return;

    function refresh() {
      panel.hidden = !canUseDeliveryTools();
    }

    refresh();
    document.addEventListener("portal-admin-change", refresh);
    document.addEventListener("portal-auth-change", refresh);

    generate.addEventListener("click", async () => {
      status.className = "status-line";
      status.textContent = "Generating...";
      generate.disabled = true;
      try {
        const data = await requestReportPassword(workerUrl, item.id);
        linkInput.value = deliveryPageUrl(item.id, data.password, item);
        trackEvent(workerUrl, "delivery_link_generate", analyticsReportPayload(item, "catalog"));
        status.textContent = "Delivery link generated.";
        status.classList.add("ok");
      } catch (error) {
        linkInput.value = "";
        status.textContent = localizedContactText(error.message || "Could not generate delivery link.");
        status.classList.add("error");
      } finally {
        generate.disabled = false;
      }
    });

    copy.addEventListener("click", async () => {
      if (!linkInput.value) return;
      try {
        await navigator.clipboard.writeText(linkInput.value);
        status.className = "status-line ok";
        status.textContent = "Copied.";
      } catch (_error) {
        linkInput.select();
        status.className = "status-line";
        status.textContent = "Select and copy the link.";
      }
    });
  }

  function detailTitleMarkup(item) {
    const zh = titleZhText(item);
    return `
      <div>
        <h1 class="detail-title">${escapeHtml(titleText(item))}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">Indexed report record with password-protected PDF access when available.</p>
      </div>
    `;
  }

  function reportDetailShardPrefix(id) {
    return String(id || "")
      .toLowerCase()
      .replace(/[^a-z0-9]/g, "_")
      .slice(0, 2)
      .padEnd(2, "_");
  }

  async function loadReportDetailRecord(id) {
    const reportId = String(id || "").trim();
    if (!reportId) return null;
    const prefix = reportDetailShardPrefix(reportId);
    let payload;
    try {
      payload = await loadJson(`data/report_details/${prefix}.json`);
    } catch (_error) {
      return null;
    }
    const reports = payload && payload.reports && typeof payload.reports === "object"
      ? payload.reports
      : null;
    const record = reports && Object.prototype.hasOwnProperty.call(reports, reportId)
      ? reports[reportId]
      : null;
    if (!record || typeof record !== "object" || !record.item || typeof record.item !== "object") return null;
    const itemId = String(record.item.id || reportId);
    if (itemId !== reportId) return null;
    const related = (Array.isArray(record.related) ? record.related : [])
      .filter((candidate) => candidate && typeof candidate === "object" && candidate.id && String(candidate.id) !== reportId);
    return {
      item: { ...record.item, id: reportId },
      related,
    };
  }

  function renderReportFirstPaint(item, relatedItems = []) {
    const detail = document.getElementById("detail");
    if (!detail || !item) return;
    const availabilityKnown = typeof item.available === "boolean";
    const available = isPdfAvailable(item);
    const related = Array.isArray(relatedItems) ? relatedItems : [];
    const relatedById = new Map(related.map((entry) => [String(entry.id || ""), entry]));
    const relatedMarkup = related.length
      ? `
        <section class="related-section" aria-labelledby="relatedTitle">
          <div class="related-heading">
            <h3 id="relatedTitle">Related Reports</h3>
          </div>
          <div class="related-list">${related.map(relatedRow).join("")}</div>
        </section>
      `
      : "";
    const availabilityMarkup = availabilityKnown && !available
      ? textOnlySearchGuidanceMarkup(item)
      : '<p class="subtle" aria-live="polite">下载权限正在后台补充…</p>';
    detail.innerHTML = `
      ${detailTitleMarkup(item)}
      <div class="detail-grid">
        ${field("Institution", bankLabel(item))}
        ${field("Industry", inferIndustry(item))}
        ${field("Date", displayDate(item.date_folder))}
        ${field("PDF", availabilityKnown ? (available ? formatSize(item.size_bytes) || "Available" : "Text only") : "正在确认")}
      </div>
      ${availabilityMarkup}
      ${relatedMarkup}
    `;
    detail.onclick = (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      const relatedItem = relatedById.get(String(row.dataset.id || ""));
      if (relatedItem) rememberReportPreview(relatedItem);
      trackEvent("", "report_open", {
        ...analyticsReportPayload(relatedItem || { id: row.dataset.id }, "catalog"),
        placement: "report_related",
        parent_report_id: String(item.id || ""),
      });
    };
  }

  function renderDetail(item, config, catalogItems, searchTextById, options = {}) {
    const detail = document.getElementById("detail");
    const workerUrl = workerBaseUrl(config);
    const catalogById = new Map((catalogItems || []).map((row) => [String(row.id || ""), row]));
    const available = isPdfAvailable(item);
    const setupWarning = workerUrl || !available
      ? ""
      : '<div class="setup-warning">PDF download is temporarily unavailable. Please try again later.</div>';
    const archiveNotice = available
      ? ""
      : `
        <div class="archive-notice">PDF 暂不可下载；符合条件的会员可在下方查看已保存的提取文本。</div>
        ${textOnlySearchGuidanceMarkup(item)}
      `;
    const related = Array.isArray(options.relatedItems)
      ? options.relatedItems
      : relatedReports(item, catalogItems, searchTextById);
    const relatedMarkup = related.length
      ? `
        <section class="related-section" aria-labelledby="relatedTitle">
          <div class="related-heading">
            <h3 id="relatedTitle">Related Reports</h3>
          </div>
          <div class="related-list">${related.map(relatedRow).join("")}</div>
        </section>
      `
      : "";
    const unlockMarkup = available
      ? `
        ${setupWarning}
        ${workerUrl ? accountAccessMarkup(item) : ""}
        <form class="unlock-box" id="unlockForm">
          <h3>PDF Download</h3>
          <p class="subtle">Enter the report password to download the PDF.</p>
          <div class="password-row">
            <input id="passwordInput" name="report-access-code" type="password" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="Password" required>
            <button class="primary" type="submit">Download</button>
          </div>
          <div id="downloadStatus" class="status-line" aria-live="polite"></div>
        </form>
      `
      : archiveNotice;
    const textOnlyUpload = !available && workerUrl ? textOnlyPdfUploadMarkup() : "";
    const textOnlyTextAccess = !available && workerUrl ? textOnlyTextAccessMarkup() : "";

    detail.innerHTML = `
      ${detailTitleMarkup(item)}
      <div class="detail-grid">
        ${field("Institution", bankLabel(item))}
        ${field("Industry", inferIndustry(item))}
        ${field("Date", displayDate(item.date_folder))}
        ${field("PDF", available ? formatSize(item.size_bytes) || "Available" : "Text only")}
      </div>
      ${unlockMarkup}
      ${textOnlyTextAccess}
      ${textOnlyUpload}
      ${workerUrl ? adminPanelMarkup() : ""}
      ${relatedMarkup}
    `;
    if (options.trackPageView !== false) {
      trackEvent(workerUrl, "page_view", {
        page: "report",
        ...analyticsReportPayload(item, "catalog"),
      });
    }

    detail.onclick = (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      const relatedItem = catalogById.get(String(row.dataset.id || ""));
      if (relatedItem) rememberReportPreview(relatedItem);
      trackEvent(workerUrl, "report_open", {
        ...analyticsReportPayload(relatedItem || { id: row.dataset.id }, "catalog"),
        placement: "report_related",
        parent_report_id: String(item.id || ""),
      });
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      openReportPage(row.dataset.id);
    };

    initDetailAdmin(item, workerUrl);
    initTextOnlyTextAccess(item, workerUrl);
    initTextOnlyPdfUpload(item, workerUrl);
    initReportAccessControls(item, workerUrl, "catalog", (statusTarget) => (
      downloadCatalogWithAccount(workerUrl, item, statusTarget)
    ));

    if (!available) return;

    const form = document.getElementById("unlockForm");
    const input = document.getElementById("passwordInput");
    const status = document.getElementById("downloadStatus");
    const button = form.querySelector("button");
    const deliveryPassword = String(options.password || "");
    initResilientPasswordInput(input, item.id, deliveryPassword, (message) => {
      status.textContent = message;
    });

    async function submitDownload(event) {
      if (event) event.preventDefault();
      status.className = "status-line";
      if (!workerUrl) {
        status.textContent = "PDF download is temporarily unavailable. Please try again later.";
        status.classList.add("error");
        return;
      }

      button.disabled = true;
      const session = loadAuthSession();
      const action = session ? "account_or_password_download" : "password_download";
      status.textContent = session ? "Checking account access..." : "Checking password...";
      let downloadErrorTracked = false;
      trackEvent(workerUrl, "download_attempt", {
        ...analyticsReportPayload(item, "catalog"),
        action,
      });
      try {
        const response = await fetch(`${workerUrl}/download`, {
          method: "POST",
          headers: { "Content-Type": "application/json", ...authHeaders() },
          body: JSON.stringify({
            id: item.id,
            password: input.value,
            password_group: item.password_group || "default",
          }),
        });

        if (!response.ok) {
          let data = {};
          let message = `Download failed (${response.status}).`;
          try {
            data = await response.json();
            if (data.error) message = data.error;
          } catch (_err) {
            // Ignore non-JSON errors.
          }
          if (response.status === 401) clearRememberedDownloadPassword(item.id);
          trackEvent(workerUrl, "download_error", {
            ...analyticsReportPayload(item, "catalog"),
            action,
            status: String(response.status),
            error: message,
          });
          downloadErrorTracked = true;
          throw new Error(downloadErrorMessage(response.status, message, data));
        }

        const blob = await response.blob();
        triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
        if (!session && input.value) rememberDeliveryPassword(item.id, input.value);
        trackEvent(workerUrl, "download_success", {
          ...analyticsReportPayload(item, "catalog"),
          action,
          status: "ok",
        });
        status.textContent = "Download started.";
        status.classList.add("ok");
      } catch (error) {
        if (!downloadErrorTracked) {
          trackEvent(workerUrl, "download_error", {
            ...analyticsReportPayload(item, "catalog"),
            action,
            status: "exception",
            error: error.message || "Download failed.",
          });
        }
        const message = error.message || "Download failed.";
        maybeAlertDownloadLimit(message, workerUrl, { item, source: "catalog" });
        status.innerHTML = requestActionStatusHtml(message, requestKindForVisibleMessage(message) || "support");
        status.classList.add("error");
      } finally {
        button.disabled = false;
      }
    }

    form.addEventListener("submit", submitDownload);
  }

  async function initReport() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const configPromise = loadJson("data/config.json").catch(() => ({}));
    initNewsfeedNav();
    const previewItem = reportPreviewFromParams(params, id) || cachedReportPreview(id);
    if (previewItem) {
      document.title = `${titleText(previewItem)} | ${PUBLIC_BRAND}`;
      renderReportFirstPaint(previewItem);
    }
    trackEvent("", "page_view", {
      page: "report",
      ...analyticsReportPayload(previewItem || { id }, "catalog"),
    });
    const detailRecord = await loadReportDetailRecord(id);
    let items;
    let item;
    let relatedItems = null;
    if (detailRecord) {
      item = detailRecord.item;
      relatedItems = detailRecord.related;
      items = [item, ...relatedItems];
    } else {
      const catalog = await loadJson("data/catalog.json");
      items = Array.isArray(catalog.items) ? catalog.items : [];
      item = items.find((entry) => entry.id === id);
    }
    if (!item) {
      document.getElementById("detail").innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }
    const searchTextById = new Map();
    rememberReportPreview(item);
    document.title = `${titleText(item)} | ${PUBLIC_BRAND}`;
    renderReportFirstPaint(item, relatedItems);
    const config = await configPromise;
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    renderDetail(item, config, items, searchTextById, {
      password: deliveryPasswordFromLocation(params),
      relatedItems,
      trackPageView: false,
    });
    loadCatalogPdfOverrides(workerUrl).then((overrides) => {
      if (!Array.isArray(overrides) || !overrides.length) return;
      const mergedItems = mergeCatalogPdfOverrides(items, overrides);
      const mergedById = new Map(mergedItems.map((entry) => [String(entry.id || ""), entry]));
      const nextItem = mergedById.get(String(item.id || "")) || item;
      const nextRelated = Array.isArray(relatedItems)
        ? relatedItems.map((entry) => mergedById.get(String(entry.id || "")) || entry)
        : null;
      const itemChanged = isPdfAvailable(nextItem) !== isPdfAvailable(item)
        || Number(nextItem.size_bytes || 0) !== Number(item.size_bytes || 0);
      if (itemChanged) {
        item = nextItem;
        document.title = `${titleText(item)} | ${PUBLIC_BRAND}`;
        renderDetail(item, config, mergedItems, searchTextById, {
          password: deliveryPasswordFromLocation(params),
          relatedItems: nextRelated,
          trackPageView: false,
        });
        return;
      }
      if (Array.isArray(nextRelated)) {
        refreshRelatedReports(item, mergedItems, searchTextById, nextRelated);
      } else {
        refreshRelatedReports(item, mergedItems, searchTextById);
      }
    });
    // The text index only improves related-report ranking, so load it after
    // the detail renders instead of blocking the page on a large download.
    // Related reports intentionally use catalog metadata only. Downloading the
    // complete text corpus here competed with the user's first download and
    // could exhaust memory on mobile browsers.
  }

  function refreshRelatedReports(item, catalogItems, searchTextById, relatedItems = null) {
    const detail = document.getElementById("detail");
    if (!detail) return;
    const related = Array.isArray(relatedItems)
      ? relatedItems
      : relatedReports(item, catalogItems, searchTextById);
    if (!related.length) return;
    let section = detail.querySelector(".related-section");
    if (!section) {
      section = document.createElement("section");
      section.className = "related-section";
      section.setAttribute("aria-labelledby", "relatedTitle");
      detail.appendChild(section);
    }
    section.innerHTML = `
      <div class="related-heading">
        <h3 id="relatedTitle">Related Reports</h3>
      </div>
      <div class="related-list">${related.map(relatedRow).join("")}</div>
    `;
  }

  function externalItemFromParams(params) {
    const id = String(params.get("id") || "").trim();
    const rawSource = params.get("source");
    const inferredSource = /^(?:foreign(?:-rt)?:|supplemental:[a-f0-9]{32}$)/.test(id)
      ? AUTHORITY_SOURCE
      : (/^report-a:/.test(id)
        ? REPORT_A_SOURCE
        : (/^thinktank:/.test(id)
          ? THINKTANK_SOURCE
          : (/^hot:[a-f0-9]{16}$/i.test(id) ? HOT_REPORT_SOURCE : EXTERNAL_SOURCE)));
    const source = rawSource === AUTHORITY_SOURCE
      ? AUTHORITY_SOURCE
      : (rawSource === REPORT_A_SOURCE
        ? REPORT_A_SOURCE
        : (rawSource === THINKTANK_SOURCE
          ? THINKTANK_SOURCE
          : (rawSource === HOT_REPORT_SOURCE ? HOT_REPORT_SOURCE : inferredSource)));
    return publicDocItem({
      id,
      source,
      title: params.get("title") || "",
      title_cn: params.get("title_cn") || "",
      institution: params.get("institution") || "",
      date: params.get("date") || "",
      file_type: params.get("file_type") || "",
      request_token: params.get("rt") || "",
      kind: params.get("kind") || "",
      kind_label: params.get("kind_label") || "",
      page_count: params.get("page_count") || "",
      size_bytes: Number(params.get("size_bytes") || 0) || 0,
      report_type: params.get("report_type") || "",
      language: params.get("language") || "",
      category: params.get("category") || "",
      author: params.get("author") || "",
      rating: params.get("rating") || "",
      description: params.get("description") || "",
      filename: params.get("filename") || "",
      required_plan: params.get("required_plan") || "",
    });
  }

  function renderExternalDetailFirstPaint(item, target) {
    if (!item || !target) return;
    item = publicDocItem(item);
    const hasTitle = hasMeaningfulDocTitle(item);
    const title = hasTitle ? reportRequestTitle(item) : "正在读取报告信息…";
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    target.innerHTML = `
      <div>
        <h1 class="detail-title">${escapeHtml(title)}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">下载权限与相关报告将在后台补充。</p>
      </div>
      <div class="detail-grid">
        ${field("Institution", item.institution || "正在读取")}
        ${field("Date", item.date || "正在读取")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "正在读取")}
        ${field("Source", docSourceLabel(item))}
      </div>
    `;
    if (hasTitle) document.title = `${item.title} | ${PUBLIC_BRAND}`;
  }

  function isAuthorityItem(item) {
    return item && item.source === AUTHORITY_SOURCE;
  }

  function isReportAItem(item) {
    return item && item.source === REPORT_A_SOURCE;
  }

  function isThinkTankItem(item) {
    return item && item.source === THINKTANK_SOURCE;
  }

  function isHotReportItem(item) {
    return item && item.source === HOT_REPORT_SOURCE;
  }

  function isContactOnlyItem(item) {
    return isAuthorityItem(item) || isReportAItem(item);
  }

  function docSourceLabel(item) {
    if (isAuthorityItem(item)) return "高权报告";
    if (isReportAItem(item)) return "报告A";
    if (isThinkTankItem(item)) return "国际智库";
    if (isHotReportItem(item)) return "近期热门报告";
    return "其他报告";
  }

  function docEndpoint(item) {
    if (isHotReportItem(item)) return "hot-reports";
    if (isThinkTankItem(item)) return "thinktank";
    if (isContactOnlyItem(item)) return "contact-report";
    return "external";
  }

  function validDocId(item) {
    if (isAuthorityItem(item)) return /^(?:(?:foreign|foreign-rt):[0-9]{1,25}|supplemental:[a-f0-9]{32})$/.test(item.id);
    if (isReportAItem(item)) return /^report-a:[A-Za-z0-9_-]{1,180}$/.test(item.id);
    if (isThinkTankItem(item)) return /^thinktank:[A-Za-z0-9._-]{3,220}$/.test(item.id);
    if (isHotReportItem(item)) return /^hot:[a-f0-9]{16}$/i.test(item.id);
    return /^[0-9]{6,25}$/.test(item.id);
  }

  async function fetchExternalPdf(workerUrl, item, password, statusTarget, options = {}) {
    statusTarget("正在获取报告…");
    trackEvent(workerUrl, "download_attempt", {
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
      action: options.auth ? "account_download" : "password_download",
    });
    const contactDownload = isContactOnlyItem(item);
    const contactParams = new URLSearchParams({ source: item.source, id: item.id });
    const response = await fetch(contactDownload
      ? `${workerUrl}/contact-report/pdf?${contactParams.toString()}`
      : `${workerUrl}/${docEndpoint(item)}/pdf`, contactDownload ? {
        method: "GET",
        headers: options.auth ? authHeaders() : {},
        cache: "no-store",
      } : {
        method: "POST",
        headers: { "Content-Type": "application/json", ...(options.auth ? authHeaders() : {}) },
        cache: "no-store",
        body: JSON.stringify({ id: item.id, password: password || "" }),
      });
    if (response.status === 202) {
      let data = {};
      try {
        data = await response.json();
      } catch (_error) {
        // Keep the generic pending state.
      }
      trackEvent(workerUrl, "download_pending", {
        ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
        action: "pending",
        status: "202",
      });
      return { pending: true, wait_seconds: Number(data.wait_seconds || 0) || 480 };
    }
    if (!response.ok) {
      let message = `下载失败 (${response.status})`;
      let data = {};
      try {
        data = await response.json();
        if (data.error) message = data.error;
      } catch (_error) {
        // Keep generic message.
      }
      if (response.status === 401) clearRememberedDownloadPassword(item.id);
      trackEvent(workerUrl, "download_error", {
        ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
        action: options.auth ? "account_download" : "password_download",
        status: String(response.status),
        error: message,
      });
      throw new Error(downloadErrorMessage(response.status, message, data));
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), `${item.id}.pdf`);
    rememberDeliveryPassword(item.id, password);
    trackEvent(workerUrl, "download_success", {
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
      action: options.auth ? "account_download" : "password_download",
      status: "ok",
    });
    statusTarget("下载已开始。", "ok");
    return { pending: false };
  }

  function pollExternalDetail(workerUrl, id, password, statusTarget, onReady) {
    let attempts = 0;
    const maxAttempts = 40; // 10 minutes at 15s intervals
    const startedAt = Date.now();
    statusTarget("报告正在准备，页面每 15 秒自动检测一次。准备好后会自动开始下载。");
    const timer = window.setInterval(async () => {
      attempts += 1;
      const elapsedSeconds = Math.max(15, Math.round((Date.now() - startedAt) / 1000));
      const elapsedText = elapsedSeconds >= 60
        ? `${Math.floor(elapsedSeconds / 60)} 分 ${elapsedSeconds % 60} 秒`
        : `${elapsedSeconds} 秒`;
      if (attempts > maxAttempts) {
        window.clearInterval(timer);
        statusTarget("报告准备时间超过预期。请保留这个页面，稍后再次点击下载；如果多次失败可提交支持请求。", "error");
        return;
      }
      try {
        statusTarget(`报告仍在准备中，已等待 ${elapsedText}。页面会继续自动检测。`);
        const response = await fetch(`${workerUrl}/external/status?id=${encodeURIComponent(id)}`, {
          cache: "no-store",
        });
        const data = await response.json();
        if (data.ready) {
          window.clearInterval(timer);
          statusTarget("报告已就绪，正在下载…", "ok");
          onReady();
        } else if (data.status === "failed") {
          window.clearInterval(timer);
          statusTarget(data.message || "报告准备失败，可提交支持请求。", "error");
        }
      } catch (_error) {
        // Keep polling while the background grab runs.
      }
    }, 15000);
  }

  async function downloadExternalWithAccount(workerUrl, item, statusTarget) {
    const result = await fetchExternalPdf(workerUrl, item, "", statusTarget, { auth: true });
    if (result.pending) {
      statusTarget("报告正在准备，通常约 3-8 分钟。页面会自动检测，准备好后开始下载。");
      pollExternalDetail(workerUrl, item.id, "", statusTarget, () => (
        downloadExternalWithAccount(workerUrl, item, statusTarget)
      ));
    }
  }

  async function fetchDocDetailItem(workerUrl, item) {
    const cached = cachedDocItem(item);
    let merged = mergeDocItemMetadata(cached, item);
    merged.id = item.id;
    merged.source = item.source;
    if (!workerUrl || !validDocId(merged)) return merged;
    let endpoint = "";
    if (isHotReportItem(merged)) endpoint = "hot-reports/item";
    else if (isThinkTankItem(merged)) endpoint = "thinktank/item";
    else if (isContactOnlyItem(merged)) endpoint = "contact-report/item";
    else if (merged.source === EXTERNAL_SOURCE) endpoint = "external/item";
    if (!endpoint) return merged;
    try {
      const params = new URLSearchParams({ id: merged.id });
      if (isContactOnlyItem(merged)) {
        params.set("source", merged.source);
        if (merged.request_token) params.set("request_token", merged.request_token);
      }
      const response = await fetch(`${workerUrl}/${endpoint}?${params.toString()}`, {
        cache: "no-store",
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok || !data.item || !data.item.id) return merged;
      if (String(data.item.id) !== String(merged.id)) return merged;
      merged = mergeDocItemMetadata(merged, data.item, { __detail_fetched: true });
      merged.id = item.id;
      merged.source = item.source;
      rememberDocItem(merged);
      return merged;
    } catch (_error) {
      return merged;
    }
  }

  function reportRequestMarkup(item) {
    const session = loadAuthSession();
    const defaultEmail = session && session.user ? String(session.user.email || "").trim() : "";
    const accountEmail = Boolean(defaultEmail);
    return `
      <form class="report-request-form" id="reportRequestForm">
        <p class="report-request-expectation">提交后无需打开邮件客户端。我们会在 <b>24 小时内</b>通过你填写的邮箱回复；如暂时无法提供，也会告知处理结果。</p>
        <div class="report-request-fields">
          <label class="report-request-email-label" for="reportRequesterEmail">
            <span>接收回复的邮箱${accountEmail ? "（账号邮箱）" : ""}</span>
            <input id="reportRequesterEmail" name="requester_email" type="email" autocomplete="email" inputmode="email" value="${escapeHtml(defaultEmail)}" placeholder="name@example.com"${accountEmail ? " readonly" : ""} required>
          </label>
          <button class="primary" id="reportRequestSubmit" type="submit">申请获取报告</button>
        </div>
        <label class="report-request-trap" aria-hidden="true">
          <span>Website</span>
          <input id="reportRequestWebsite" name="website" type="text" tabindex="-1" autocomplete="off">
        </label>
        <div id="reportRequestStatus" class="status-line" aria-live="polite"></div>
      </form>
    `;
  }

  function initReportRequest(workerUrl, item) {
    const form = document.getElementById("reportRequestForm");
    const email = document.getElementById("reportRequesterEmail");
    const website = document.getElementById("reportRequestWebsite");
    const submit = document.getElementById("reportRequestSubmit");
    const status = document.getElementById("reportRequestStatus");
    if (!form || !email || !submit || !status) return;
    let requestItem = mergeDocItemMetadata(item);
    let requestToken = String(requestItem.request_token || "");

    function setRequestStatus(message, state = "") {
      status.textContent = String(message || "");
      status.className = `status-line${state ? ` ${state}` : ""}`;
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const requesterEmail = String(email.value || "").trim();
      if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(requesterEmail)) {
        setRequestStatus("请填写有效邮箱。", "error");
        email.focus();
        return;
      }
      if (!workerUrl) {
        setRequestStatus("站内申请暂时不可用，请稍后重试。", "error");
        return;
      }

      submit.disabled = true;
      submit.textContent = "正在提交…";
      setRequestStatus("正在通知 KC桌面，请稍候…");
      try {
        if (["authority", "report-a"].includes(String(requestItem.source || ""))
          && (!requestToken || !hasMeaningfulDocTitle(requestItem))) {
          setRequestStatus("正在刷新报告验证信息…");
          const params = new URLSearchParams({ source: requestItem.source, id: requestItem.id });
          const tokenResponse = await fetch(`${workerUrl}/contact-report/item?${params.toString()}`, { cache: "no-store" });
          const tokenData = await tokenResponse.json().catch(() => ({}));
          if (tokenResponse.ok && tokenData.item && typeof tokenData.item === "object") {
            requestItem = mergeDocItemMetadata(requestItem, tokenData.item);
            requestItem.id = item.id;
            requestItem.source = item.source;
            requestToken = String(requestItem.request_token || requestToken);
          }
          if (!tokenResponse.ok || !requestToken || !hasMeaningfulDocTitle(requestItem)) {
            throw new Error("报告信息暂时未就绪，本次申请尚未发送，请稍后重试。");
          }
        }
        const response = await fetch(`${workerUrl}/report-request`, {
          method: "POST",
          cache: "no-store",
          headers: { "Content-Type": "application/json", ...authHeaders() },
          body: JSON.stringify({
            report_id: requestItem.id || "",
            title: reportRequestTitle(requestItem),
            source: requestItem.source || "",
            institution: requestItem.institution || requestItem.bank_name || requestItem.bank_code || "",
            page_path: currentAnalyticsPath(),
            requester_email: requesterEmail,
            request_token: requestToken,
            honeypot: website ? String(website.value || "") : "",
          }),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok || !data.ok) throw new Error(data.detail || "申请提交失败，请稍后重试。");

        email.readOnly = true;
        submit.textContent = data.deduplicated ? "申请已记录" : "申请已提交";
        setRequestStatus(
          data.detail || "申请已提交。我们会在24小时内通过邮箱回复，请勿重复提交。",
          "ok",
        );
        trackEvent(workerUrl, "report_request", {
          ...analyticsReportPayload(requestItem, requestItem.source || AUTHORITY_SOURCE),
          action: data.deduplicated ? "deduplicated" : "submitted",
        });
      } catch (error) {
        submit.disabled = false;
        submit.textContent = "重新提交申请";
        setRequestStatus(error && error.message || "申请提交失败，请稍后重试。", "error");
      }
    });
  }

  async function initExternalDetail() {
    const params = new URLSearchParams(window.location.search);
    let item = externalItemFromParams(params);
    const target = document.getElementById("externalDetail");
    if (!validDocId(item)) {
      target.innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }
    renderExternalDetailFirstPaint(item, target);
    trackEvent("", "page_view", {
      page: "doc",
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
    });

    let recommendationCatalogPromise = null;
    function recommendationCatalogAfterPaint() {
      if (recommendationCatalogPromise) return recommendationCatalogPromise;
      recommendationCatalogPromise = new Promise((resolve) => {
        const start = () => {
          loadOptionalJson("data/catalog_recommendations.json", { items: [] })
            .then((payload) => resolve(Array.isArray(payload.items) ? payload.items : []))
            .catch(() => resolve([]));
        };
        const startAfterPaint = () => window.setTimeout(start, 0);
        if (typeof window.requestAnimationFrame === "function") {
          window.requestAnimationFrame(startAfterPaint);
        } else {
          startAfterPaint();
        }
      });
      return recommendationCatalogPromise;
    }
    const [config, catalog] = await Promise.all([
      loadOptionalJson("data/config.json", {}),
      loadOptionalJson("data/catalog_preview.json", { items: [] }),
    ]);
    const workerUrl = workerBaseUrl(config);
    const catalogItems = Array.isArray(catalog.items) ? catalog.items : [];
    const searchTextById = new Map();
    const searchIndexPromise = Promise.resolve();
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();
    item = await fetchDocDetailItem(workerUrl, item);
    const passwordFromLink = deliveryPasswordFromLocation(params);
    const shortUrl = externalPageUrl(item, passwordFromLink, {
      compact: isContactOnlyItem(item) && item.__detail_fetched === true,
    });
    const currentHasTitle = hasMeaningfulDocTitle({ title: params.get("title") || "" });
    const shortHasTitle = hasMeaningfulDocTitle(item);
    if (shortUrl.length < window.location.href.length || (!currentHasTitle && shortHasTitle)) {
      window.history.replaceState({}, "", shortUrl);
    }

    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    const displayTitle = hasMeaningfulDocTitle(item) ? reportRequestTitle(item) : "报告详情";
    document.title = `${displayTitle} | ${PUBLIC_BRAND}`;
    const contactAvailable = isContactOnlyItem(item) && item.available === true;
    const detailFields = isAuthorityItem(item)
      ? `
        ${field("板块", docSourceLabel(item))}
        ${field("Category", authorityKindLabel(item.kind, item.kind_label))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "-")}
        ${contactAvailable ? field("PDF", formatSize(item.size_bytes) || "Available") : ""}
        ${contactAvailable ? field("全文权限", "3个月及以上会员") : ""}
      `
      : (isReportAItem(item) ? `
        ${field("板块", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Category", item.category || "-")}
        ${field("Author", item.author || "-")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "-")}
        ${contactAvailable ? field("PDF", formatSize(item.size_bytes) || "Available") : ""}
        ${contactAvailable ? field("全文权限", "3个月及以上会员") : ""}
      ` : (isHotReportItem(item) ? `
        ${field("板块", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("PDF", formatSize(item.size_bytes) || "Available")}
        ${field("全文权限", "3个月及以上会员")}
      ` : (isThinkTankItem(item) ? `
        ${field("板块", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "-")}
        ${field("PDF", formatSize(item.size_bytes) || "Available")}
      ` : `
        ${field("板块", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Type", item.file_type || "-")}
      `)));
    const detailHeader = `
      <div>
        <h1 class="detail-title">${escapeHtml(displayTitle)}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">${isContactOnlyItem(item)
          ? (contactAvailable ? "3个月及以上会员可下载全文。" : `${docSourceLabel(item)}检索线索。`)
          : (isHotReportItem(item) ? "3个月及以上会员可下载全文。" : "Password-protected report delivery.")}</p>
      </div>
      <div class="detail-grid">
        ${detailFields}
      </div>
    `;
    if (isContactOnlyItem(item)) {
      if (contactAvailable) {
        target.innerHTML = `
          ${detailHeader}
          <section class="unlock-box authority-contact-box contact-report-available-box">
            <h3>PDF 已补齐</h3>
            <p class="subtle">这份报告已绑定原检索记录。3个月及以上会员登录后可直接下载全文。</p>
          </section>
          ${workerUrl ? accountAccessMarkup(item) : ""}
          ${externalRelatedMarkup()}
        `;
        initReportAccessControls(item, workerUrl, item.source, (statusTarget) => (
          downloadExternalWithAccount(workerUrl, item, statusTarget)
        ));
        searchIndexPromise.then(() => initExternalRelated(
          item,
          workerUrl,
          catalogItems,
          searchTextById,
          recommendationCatalogAfterPaint(),
        ));
        return;
      }
      const hint = isAuthorityItem(item)
        ? "高权报告仅提供检索线索，无法在本站直接下载。"
        : "这份报告当前仅提供检索线索，无法在本站直接下载。";
      target.innerHTML = `
        ${detailHeader}
        <section class="unlock-box authority-contact-box">
          <h3>申请获取报告</h3>
          <p class="subtle">${escapeHtml(hint)}</p>
          ${reportRequestMarkup(item)}
        </section>
        ${externalRelatedMarkup()}
      `;
      initReportRequest(workerUrl, item);
      searchIndexPromise.then(() => initExternalRelated(
        item,
        workerUrl,
        catalogItems,
        searchTextById,
        recommendationCatalogAfterPaint(),
      ));
      return;
    }

    if (isHotReportItem(item)) {
      target.innerHTML = `
        ${detailHeader}
        ${item.description ? `<p class="hot-report-description">${escapeHtml(item.description)}</p>` : ""}
        ${workerUrl ? accountAccessMarkup(item) : ""}
        <form class="unlock-box" id="externalDetailForm">
          <h3>PDF Download</h3>
          <p class="subtle">Enter the report password to download the PDF.</p>
          <div class="password-row">
            <input id="externalDetailPassword" name="report-access-code" type="password" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="Password" required>
            <button class="primary" type="submit">Download</button>
          </div>
          <div id="externalDetailStatus" class="status-line" aria-live="polite"></div>
        </form>
        <section class="admin-panel external-admin-tools" hidden>
          <div class="admin-panel-heading">
            <h3>Delivery link</h3>
            <span>Private</span>
          </div>
          <div class="delivery-row">
            <button class="primary" id="generateExternalDetailDeliveryLink" type="button">Generate</button>
            <input id="externalDetailDeliveryLinkInput" type="text" readonly aria-label="Delivery link">
            <button id="copyExternalDeliveryLink" type="button">Copy</button>
          </div>
          <div id="externalDetailDeliveryStatus" class="status-line" aria-live="polite"></div>
        </section>
        ${hotReportCommentsMarkup()}
        ${externalRelatedMarkup()}
      `;
      const form = document.getElementById("externalDetailForm");
      const input = document.getElementById("externalDetailPassword");
      const button = form.querySelector("button");
      const status = document.getElementById("externalDetailStatus");
      const adminTools = target.querySelector(".external-admin-tools");
      const generate = document.getElementById("generateExternalDetailDeliveryLink");
      const linkInput = document.getElementById("externalDetailDeliveryLinkInput");
      const copy = document.getElementById("copyExternalDeliveryLink");
      const deliveryStatus = document.getElementById("externalDetailDeliveryStatus");

      function setStatus(text, kind) {
        status.className = kind ? `status-line ${kind}` : "status-line";
        const message = localizedContactText(text);
        const requestKind = kind === "error" ? requestKindForVisibleMessage(message) : "";
        if (requestKind) status.innerHTML = requestActionStatusHtml(message, requestKind);
        else status.textContent = message;
      }

      async function submitDownload(event) {
        if (event) event.preventDefault();
        if (!input.value) {
          setStatus("Password is required.", "error");
          return;
        }
        button.disabled = true;
        try {
          await fetchExternalPdf(workerUrl, item, input.value, setStatus);
        } catch (error) {
          const message = error.message || "下载失败。";
          maybeAlertDownloadLimit(message, workerUrl, { item, source: HOT_REPORT_SOURCE });
          setStatus(message, "error");
        } finally {
          button.disabled = false;
        }
      }

      function refreshAdmin() {
        adminTools.hidden = !canUseDeliveryTools();
      }

      form.addEventListener("submit", submitDownload);
      initReportAccessControls(item, workerUrl, HOT_REPORT_SOURCE, (statusTarget) => (
        downloadExternalWithAccount(workerUrl, item, statusTarget)
      ));
      document.addEventListener("portal-admin-change", refreshAdmin);
      document.addEventListener("portal-auth-change", refreshAdmin);
      refreshAdmin();
      generate.addEventListener("click", async () => {
        generate.disabled = true;
        linkInput.value = "";
        deliveryStatus.className = "status-line";
        deliveryStatus.textContent = "Generating...";
        try {
          const data = await requestExternalPassword(workerUrl, item.id, HOT_REPORT_SOURCE);
          const deliveryItem = data.id ? { ...item, id: data.id, source: HOT_REPORT_SOURCE } : item;
          linkInput.value = externalPageUrl(deliveryItem, data.password);
          trackEvent(workerUrl, "delivery_link_generate", analyticsReportPayload(item, HOT_REPORT_SOURCE));
          deliveryStatus.className = "status-line ok";
          deliveryStatus.textContent = "Delivery link generated.";
        } catch (error) {
          deliveryStatus.className = "status-line error";
          deliveryStatus.textContent = localizedContactText(error.message || "Could not generate delivery link.");
        } finally {
          generate.disabled = false;
        }
      });
      copy.addEventListener("click", async () => {
        if (!linkInput.value) return;
        try {
          await navigator.clipboard.writeText(linkInput.value);
          deliveryStatus.className = "status-line ok";
          deliveryStatus.textContent = "Copied.";
        } catch (_error) {
          linkInput.select();
          deliveryStatus.className = "status-line";
          deliveryStatus.textContent = "Select and copy the link.";
        }
      });
      initResilientPasswordInput(input, item.id, passwordFromLink, setStatus);
      initHotReportComments(item, workerUrl);
      searchIndexPromise.then(() => initExternalRelated(
        item,
        workerUrl,
        catalogItems,
        searchTextById,
        recommendationCatalogAfterPaint(),
      ));
      return;
    }

    target.innerHTML = `
      ${detailHeader}
      <form class="unlock-box" id="externalDetailForm">
        <h3>PDF Download</h3>
        <p class="subtle">Enter the report password to download the PDF.</p>
        <div class="password-row">
          <input id="externalDetailPassword" name="report-access-code" type="password" autocomplete="off" autocapitalize="none" spellcheck="false" placeholder="Password" required>
          <button class="primary" type="submit">Download</button>
        </div>
        <div class="external-wait" id="externalDetailWait" hidden>
          报告正在准备，通常约 3-8 分钟。这个页面会自动检测，文件准备好后会开始下载。
        </div>
        <div id="externalDetailStatus" class="status-line" aria-live="polite"></div>
      </form>
      ${workerUrl ? accountAccessMarkup(item) : ""}
      <section class="admin-panel external-admin-tools" hidden>
        <div class="admin-panel-heading">
          <h3>Delivery link</h3>
          <span>Private</span>
        </div>
        <div class="delivery-row">
          <button class="primary" id="generateExternalDetailDeliveryLink" type="button">Generate</button>
          <input id="externalDetailDeliveryLinkInput" type="text" readonly aria-label="Delivery link">
          <button id="copyExternalDeliveryLink" type="button">Copy</button>
        </div>
        <div id="externalDetailDeliveryStatus" class="status-line" aria-live="polite"></div>
      </section>
      ${externalRelatedMarkup()}
    `;
    searchIndexPromise.then(() => initExternalRelated(
      item,
      workerUrl,
      catalogItems,
      searchTextById,
      recommendationCatalogAfterPaint(),
    ));

    const form = document.getElementById("externalDetailForm");
    const input = document.getElementById("externalDetailPassword");
    const button = form.querySelector("button");
    const status = document.getElementById("externalDetailStatus");
    const wait = document.getElementById("externalDetailWait");
    const adminTools = target.querySelector(".external-admin-tools");
    const generate = document.getElementById("generateExternalDetailDeliveryLink");
    const linkInput = document.getElementById("externalDetailDeliveryLinkInput");
    const copy = document.getElementById("copyExternalDeliveryLink");
    const deliveryStatus = document.getElementById("externalDetailDeliveryStatus");

    function setStatus(text, kind) {
      status.className = kind ? `status-line ${kind}` : "status-line";
      const message = localizedContactText(text);
      const requestKind = kind === "error" ? requestKindForVisibleMessage(message) : "";
      if (requestKind) status.innerHTML = requestActionStatusHtml(message, requestKind);
      else status.textContent = message;
      wait.hidden = !/准备|等待|自动检测/.test(String(text || ""));
    }

    function refreshAdmin() {
      adminTools.hidden = !canUseDeliveryTools();
    }

    async function submitDownload(event) {
      if (event) event.preventDefault();
      if (!input.value) {
        setStatus("Password is required.", "error");
        return;
      }
      button.disabled = true;
      try {
        const result = await fetchExternalPdf(workerUrl, item, input.value, setStatus);
        if (result.pending) {
          rememberDeliveryPassword(item.id, input.value);
          setStatus("报告正在准备，通常约 3-8 分钟。页面会自动检测，准备好后开始下载。");
          pollExternalDetail(workerUrl, item.id, input.value, setStatus, () => submitDownload());
        }
      } catch (error) {
        const message = error.message || "下载失败。";
        maybeAlertDownloadLimit(message, workerUrl, { item, source: item.source });
        setStatus(message, "error");
      } finally {
        button.disabled = false;
      }
    }

    form.addEventListener("submit", submitDownload);
    document.addEventListener("portal-admin-change", refreshAdmin);
    document.addEventListener("portal-auth-change", refreshAdmin);
    refreshAdmin();
    initReportAccessControls(item, workerUrl, item.source, (statusTarget) => (
      downloadExternalWithAccount(workerUrl, item, statusTarget)
    ));

    generate.addEventListener("click", async () => {
      generate.disabled = true;
      linkInput.value = "";
      deliveryStatus.className = "status-line";
      deliveryStatus.textContent = "Generating...";
      try {
        const data = await requestExternalPassword(workerUrl, item.id, item.source);
        const deliveryItem = data.id ? { ...item, id: data.id, source: item.source } : item;
        linkInput.value = externalPageUrl(deliveryItem, data.password);
        trackEvent(workerUrl, "delivery_link_generate", analyticsReportPayload(item, item.source || EXTERNAL_SOURCE));
        deliveryStatus.className = "status-line ok";
        deliveryStatus.textContent = "Delivery link generated.";
      } catch (error) {
        deliveryStatus.className = "status-line error";
        deliveryStatus.textContent = localizedContactText(error.message || "Could not generate delivery link.");
      } finally {
        generate.disabled = false;
      }
    });

    copy.addEventListener("click", async () => {
      if (!linkInput.value) return;
      try {
        await navigator.clipboard.writeText(linkInput.value);
        deliveryStatus.className = "status-line ok";
        deliveryStatus.textContent = "Copied.";
      } catch (_error) {
        linkInput.select();
        deliveryStatus.className = "status-line";
        deliveryStatus.textContent = "Select and copy the link.";
      }
    });

    initResilientPasswordInput(input, item.id, passwordFromLink, setStatus);
  }

  function newsfeedLogoUrl(item) {
    if (item && item.logo_url) return item.logo_url;
    const domain = String(item && (item.domain || item.source_domain) || "").trim();
    return domain ? `https://www.google.com/s2/favicons?domain=${encodeURIComponent(domain)}&sz=64` : "";
  }

  function newsfeedTimeLabel(value) {
    const timestamp = Date.parse(value || "");
    if (!Number.isFinite(timestamp)) return "";
    const diff = Date.now() - timestamp;
    const minute = 60 * 1000;
    const hour = 60 * minute;
    const day = 24 * hour;
    if (diff >= 0 && diff < hour) return `${Math.max(1, Math.round(diff / minute))}m ago`;
    if (diff >= 0 && diff < day) return `${Math.max(1, Math.round(diff / hour))}h ago`;
    if (diff >= 0 && diff < 3 * day) return `${Math.max(1, Math.round(diff / day))}d ago`;
    return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }).format(new Date(timestamp));
  }

  function newsfeedSourceName(item) {
    return String(item && (item.source || item.source_name || item.domain) || "News").replace(/^GDELT\s*\/\s*/i, "");
  }

  const NEWSFEED_UI_COPY = {
    en: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    "zh-CN": {
      myFeed: "我的新闻",
      explore: "探索",
      addTopics: "添加话题",
      digestEmail: "邮件摘要",
      dailyDigest: "每日摘要",
      topHeadlines: "重点新闻",
      regions: "区域",
      language: "语言",
      outputLanguage: "输出语言",
      suggestedTopics: "热门话题",
      sendDailyDigest: "发送每日摘要",
      saveEmail: "保存邮箱",
      sendTestNow: "发送测试邮件",
      sendNewsletterNow: "立即发送 newsletter",
      newsletterTopic: "Newsletter 主题",
      noNewsletter: "不订阅",
      email: "邮箱",
      sendTime: "发送时间",
      timezone: "时区",
      noHeadlines: "暂无新闻。",
      loadingLatest: "正在加载最新新闻...",
      updating: "正在补全新闻流...",
      playBriefing: "播放简报",
      nowPlaying: "正在播放",
      playlist: "播放列表",
      readStory: "阅读新闻",
      addRegion: "添加区域",
      customRegion: "其他区域",
    },
    ja: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    ko: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      newsletterTopic: "Newsletter",
      noNewsletter: "Not subscribed",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
  };

  function newsfeedLanguageCode(value) {
    return ["en", "zh-CN", "ja", "ko"].includes(value) ? value : "en";
  }

  function newsfeedText(state, key) {
    const language = newsfeedLanguageCode(state && state.interfaceLanguage || "en");
    return (NEWSFEED_UI_COPY[language] && NEWSFEED_UI_COPY[language][key]) || NEWSFEED_UI_COPY.en[key] || key;
  }

  function newsfeedImageMarkup(item) {
    const image = String(item && item.image_url || "").trim();
    if (!image) return "";
    return `<img class="news-story-image" src="${escapeHtml(image)}" alt="">`;
  }

  function newsfeedLogoMarkup(item) {
    const logo = newsfeedLogoUrl(item);
    const label = newsfeedSourceName(item).slice(0, 1).toUpperCase() || "N";
    return logo
      ? `<img class="news-source-logo" src="${escapeHtml(logo)}" alt="">`
      : `<span class="news-source-logo news-source-fallback">${escapeHtml(label)}</span>`;
  }

  function newsfeedSourceStack(items = []) {
    const unique = [];
    const seen = new Set();
    for (const item of items) {
      const key = String(item.domain || item.source || item.source_name || item.id || "");
      if (!key || seen.has(key)) continue;
      seen.add(key);
      unique.push(item);
      if (unique.length >= 5) break;
    }
    if (!unique.length) return "";
    return `
      <div class="news-source-stack" aria-label="Sources">
        ${unique.map(newsfeedLogoMarkup).join("")}
      </div>
    `;
  }

  function newsfeedStoryMeta(item) {
    return [newsfeedTimeLabel(item && item.published_at), newsfeedSourceName(item), item && item.category]
      .filter(Boolean)
      .join(" · ");
  }

  function newsfeedStoryCard(item, index = 0, options = {}) {
    if (!item) return "";
    const id = String(item.id || "");
    const image = newsfeedImageMarkup(item);
    const summary = item.summary ? `<p>${escapeHtml(item.summary)}</p>` : "";
    const className = options.featured ? "news-story is-featured" : "news-story";
    return `
      <button class="${className}" type="button" data-action="open-article" data-id="${escapeHtml(id)}">
        <span class="news-story-rank">${index ? escapeHtml(index) : ""}</span>
        <span class="news-story-main">
          <strong>${escapeHtml(item.title || "Untitled")}</strong>
          ${summary}
          <span class="news-story-meta">${escapeHtml(newsfeedStoryMeta(item))}</span>
        </span>
        ${image}
        <span class="news-story-actions">${newsfeedLogoMarkup(item)}<span>···</span></span>
      </button>
    `;
  }

  function newsfeedSpinnerMarkup(label = "Loading") {
    return `
      <div class="newsfeed-loader" role="status" aria-live="polite">
        <span></span>
        <strong>${escapeHtml(label)}</strong>
      </div>
    `;
  }

  function newsfeedSkeletonMarkup(kind = "home", label = "Preparing Newsfeed") {
    const rows = Array.from({ length: kind === "article" ? 5 : 4 }).map(() => `
      <div class="news-skeleton-row">
        <span></span>
        <span></span>
      </div>
    `).join("");
    return `
      <section class="newsfeed-loading-panel">
        ${newsfeedSpinnerMarkup(label)}
        <div class="news-skeleton-block">
          ${rows}
        </div>
      </section>
    `;
  }

  function newsfeedDigestMarkup(digest = []) {
    const rows = digest.slice(0, 4).map((line) => `<li>${escapeHtml(line)}</li>`).join("");
    return rows || "<li>Fresh digest is loading.</li>";
  }

  function newsfeedTopicIcon(topic) {
    if (topic && topic.pinned) return "◆";
    if (topic && topic.kind === "custom") return "“";
    return "◇";
  }

  function newsfeedTopicRow(topic, state) {
    const id = String(topic && topic.id || "");
    const pin = newsfeedCanCustomize(state)
      ? `<button class="news-topic-pin" type="button" data-action="pin-topic" data-id="${escapeHtml(id)}" aria-label="Pin topic">${topic && topic.pinned ? "●" : "○"}</button>`
      : "";
    return `
      <div class="news-topic-row${pin ? "" : " is-readonly"}" data-topic-id="${escapeHtml(id)}">
        <button class="news-topic-open" type="button" data-action="open-topic" data-id="${escapeHtml(id)}">
          <span>${escapeHtml(newsfeedTopicIcon(topic))}</span>
          <strong>${escapeHtml(topic.title || "Topic")}</strong>
          <small>${escapeHtml(topic.last_updated_label || topic.description || "")}</small>
        </button>
        ${pin}
      </div>
    `;
  }

  function newsfeedShellMarkup(state) {
    return `
      <section class="newsfeed-layout">
        <aside class="newsfeed-sidebar" id="newsfeedSidebar">
          <div class="newsfeed-profile">
            <span class="newsfeed-avatar">KC</span>
            <strong>${escapeHtml(authUserLabel(loadAuthSession()))}</strong>
          </div>
          <div class="newsfeed-side-actions">
            <button type="button" data-action="show-feed">My feed</button>
            <button type="button" data-action="show-explore">Explore</button>
            <button type="button" data-action="show-email" data-newsfeed-capability="subscribe" hidden>Digest Email</button>
          </div>
          <div id="newsfeedPolicyNotice" class="newsfeed-policy-notice"></div>
          <div class="newsfeed-following">
            <div class="newsfeed-sidebar-heading">
              <span>Following</span>
              <strong id="newsfeedTopicCount">0 topics</strong>
            </div>
            <div id="newsfeedTopicList" class="newsfeed-topic-list"></div>
          </div>
          <button class="newsfeed-add-wide" type="button" data-action="show-add" data-newsfeed-capability="customize" hidden>+ Add Topics</button>
        </aside>
        <section class="newsfeed-main">
          <div class="newsfeed-command">
            <button class="news-icon-button" type="button" data-action="toggle-sidebar" aria-label="Topics">☰</button>
            <h1 id="newsfeedTitle">Daily Digest</h1>
            <div class="newsfeed-audio-actions">
              <button id="newsBriefingButton" class="news-icon-button is-wide" type="button" data-action="play-briefing" aria-label="Audio">▥ ▶</button>
            </div>
          </div>
          <div id="newsfeedPreferences" class="news-preference-bar" hidden></div>
          <div id="newsfeedStatus" class="newsfeed-status" aria-live="polite"></div>
          <div id="newsfeedContent" class="newsfeed-content"></div>
          <div id="newsBriefingPanel" class="news-briefing-panel" hidden></div>
          <nav class="newsfeed-bottom-tabs" aria-label="Newsfeed sections">
            <button type="button" data-action="show-feed" class="is-active"><span>▯</span>My feed</button>
            <button type="button" data-action="show-add" data-newsfeed-capability="customize" hidden><span>＋</span>Add topics</button>
            <button type="button" data-action="show-explore"><span>◇</span>Explore</button>
          </nav>
        </section>
      </section>
    `;
  }

  function renderNewsfeedBoot(app, message = "Checking Newsfeed access...") {
    app.innerHTML = `
      <section class="newsfeed-access is-loading">
        ${newsfeedSpinnerMarkup(message)}
        <p>We are preparing your private Newsfeed workspace.</p>
      </section>
    `;
  }

  async function newsfeedJson(workerUrl, path, options = {}) {
    const response = await fetch(`${workerUrl}${path}`, {
      cache: "no-store",
      ...options,
      headers: {
        ...(options.body ? { "Content-Type": "application/json" } : {}),
        ...authHeaders(),
        ...(options.headers || {}),
      },
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      const error = new Error(data.detail || data.error || "Newsfeed request failed.");
      error.status = response.status;
      error.code = String(data.code || data.stage_code || "");
      error.data = data;
      throw error;
    }
    return data;
  }

  function newsfeedSystemTopic(topic) {
    return NEWSFEED_SYSTEM_TOPIC_IDS.has(String(topic && topic.id || topic || ""));
  }

  function newsfeedCustomTopics(value) {
    return (Array.isArray(value) ? value : []).filter((topic) => topic && !newsfeedSystemTopic(topic));
  }

  function normalizeNewsfeedPolicy(raw = {}, session = null, topics = []) {
    const source = raw && typeof raw === "object" && !Array.isArray(raw) ? raw : {};
    const authenticated = Object.prototype.hasOwnProperty.call(source, "authenticated")
      ? Boolean(source.authenticated)
      : isNewsfeedSession(session);
    const tier = String(source.tier || (isSuperSession(session) ? "super" : authenticated ? "registered" : "anonymous"))
      .trim()
      .toLowerCase();
    const hasExplicitNullLimit = Object.prototype.hasOwnProperty.call(source, "custom_topic_limit")
      && source.custom_topic_limit === null;
    const unlimited = authenticated && (
      isSuperSession(session)
      || tier === "super"
      || tier === "admin"
      || source.custom_topic_limit === "unlimited"
      || hasExplicitNullLimit
    );
    const observedCount = newsfeedCustomTopics(topics).length;
    const rawCount = Number(source.custom_topic_count);
    const customTopicCount = Number.isFinite(rawCount) ? Math.max(0, Math.floor(rawCount)) : observedCount;
    const rawLimit = Number(source.custom_topic_limit);
    const customTopicLimit = unlimited ? null : Number.isFinite(rawLimit) ? Math.max(0, Math.floor(rawLimit)) : 0;
    const rawRemaining = Number(source.custom_topic_remaining);
    const customTopicRemaining = unlimited
      ? null
      : Number.isFinite(rawRemaining)
        ? Math.max(0, Math.floor(rawRemaining))
        : Math.max(0, customTopicLimit - customTopicCount);
    const hasMemberFeatures = authenticated && (unlimited || customTopicLimit > 0);
    return {
      tier,
      authenticated,
      can_customize: authenticated && (hasMemberFeatures || source.can_customize === true || source.can_create_custom === true),
      can_subscribe: authenticated && (hasMemberFeatures || source.can_subscribe === true),
      custom_topic_limit: customTopicLimit,
      custom_topic_count: customTopicCount,
      custom_topic_remaining: customTopicRemaining,
      request_allowed: authenticated && source.request_allowed === true,
      unlimited,
    };
  }

  function applyNewsfeedPolicy(state, payload = {}) {
    const declared = payload && (payload.policy || payload.topic_policy);
    const usage = payload && payload.custom_topics && typeof payload.custom_topics === "object"
      ? payload.custom_topics
      : {};
    const raw = declared && typeof declared === "object" ? { ...declared } : {};
    if (raw.can_customize === undefined && raw.can_create_custom !== undefined) raw.can_customize = raw.can_create_custom;
    if (raw.custom_topic_count === undefined) {
      raw.custom_topic_count = Object.prototype.hasOwnProperty.call(payload, "custom_topic_count")
        ? payload.custom_topic_count
        : usage.count;
    }
    if (raw.custom_topic_limit === undefined) {
      raw.custom_topic_limit = Object.prototype.hasOwnProperty.call(payload, "custom_topic_limit")
        ? payload.custom_topic_limit
        : usage.limit;
    }
    if (raw.custom_topic_remaining === undefined) {
      raw.custom_topic_remaining = Object.prototype.hasOwnProperty.call(payload, "custom_topic_remaining")
        ? payload.custom_topic_remaining
        : usage.remaining;
    }
    if (raw.request_allowed === undefined) raw.request_allowed = payload.request_available;
    const hasPolicyFields = Object.values(raw).some((value) => value !== undefined);
    if (!hasPolicyFields && state.policy) return state.policy;
    state.policy = normalizeNewsfeedPolicy(raw, state.session, state.topics);
    return state.policy;
  }

  function newsfeedCanCustomize(state) {
    return Boolean(state && state.policy && state.policy.can_customize);
  }

  function newsfeedCanSubscribe(state) {
    return Boolean(state && state.policy && state.policy.can_subscribe);
  }

  function newsfeedCanOpenAdd(state) {
    return Boolean(state && state.policy && (state.policy.can_customize || state.policy.request_allowed));
  }

  function newsfeedCanCreateTopic(state) {
    if (!newsfeedCanCustomize(state)) return false;
    return Boolean(state.policy.unlimited || Number(state.policy.custom_topic_remaining) > 0);
  }

  function newsfeedShouldShowRequest(state) {
    return Boolean(
      state
      && state.policy
      && state.policy.authenticated
      && state.policy.request_allowed
      && !newsfeedCanCreateTopic(state)
    );
  }

  function newsfeedVisibleTopics(state, topics = state && state.topics || []) {
    const rows = Array.isArray(topics) ? topics : [];
    if (state && state.policy && state.policy.authenticated && newsfeedCanCustomize(state)) return rows;
    return rows.filter(newsfeedSystemTopic).slice(0, NEWSFEED_SYSTEM_TOPIC_IDS.size);
  }

  function newsfeedTopicAnalyticsKey(value) {
    let hash = 2166136261;
    const text = String(value || "");
    for (let index = 0; index < text.length; index += 1) {
      hash ^= text.charCodeAt(index);
      hash = Math.imul(hash, 16777619);
    }
    return `topic-${(hash >>> 0).toString(36)}`;
  }

  function newsfeedTopicAnalyticsFields(topic) {
    const id = String(topic && topic.id || topic || "").trim();
    if (NEWSFEED_SYSTEM_TOPIC_IDS.has(id)) return { topic_kind: "system", topic_id: id };
    return id ? { topic_kind: "custom", topic_hash: newsfeedTopicAnalyticsKey(id) } : {};
  }

  function trackNewsfeedInteraction(state, action, details = {}) {
    const policy = state && state.policy || {};
    const safe = {
      action: String(action || "interaction").slice(0, 64),
      access_state: policy.authenticated ? "authenticated" : "anonymous",
      view: String(details.view || state && state.currentView || "feed").slice(0, 32),
      tier: String(policy.tier || (policy.authenticated ? "registered" : "anonymous")).slice(0, 32),
      count: Math.max(0, Math.floor(Number(policy.custom_topic_count) || 0)),
      limit: policy.unlimited || policy.custom_topic_limit === null
        ? null
        : Math.max(0, Math.floor(Number(policy.custom_topic_limit) || 0)),
      custom_topic_remaining: policy.unlimited || policy.custom_topic_remaining === null
        ? null
        : Math.max(0, Math.floor(Number(policy.custom_topic_remaining) || 0)),
    };
    for (const key of ["outcome", "category", "language", "provider", "reason", "latency_bucket"]) {
      if (details[key] !== undefined && details[key] !== null) safe[key] = String(details[key]).slice(0, 80);
    }
    for (const key of ["region_count", "item_count", "custom_topic_remaining"]) {
      if (details[key] !== undefined && details[key] !== null && Number.isFinite(Number(details[key]))) {
        safe[key] = Math.max(0, Math.floor(Number(details[key])));
      }
    }
    if (details.topic !== undefined) Object.assign(safe, newsfeedTopicAnalyticsFields(details.topic));
    if (details.requested_topic !== undefined) {
      safe.topic_kind = "custom";
      safe.topic_hash = newsfeedTopicAnalyticsKey(details.requested_topic);
      delete safe.topic_id;
    }
    trackEvent(state && state.workerUrl || "", "newsfeed_interaction", safe);
  }

  function newsfeedPolicyNoticeMarkup(state) {
    const policy = state && state.policy || normalizeNewsfeedPolicy();
    const count = policy.custom_topic_count || 0;
    if (!policy.authenticated) {
      return `
        <strong>General · 公开浏览</strong>
        <span>当前可浏览 5 个内置话题；自定义话题 0 个。</span>
        <button type="button" data-action="show-login">登录 / 查看会员权益</button>
      `;
    }
    if (policy.unlimited) return `<strong>自定义话题不限量</strong><span>已创建 ${escapeHtml(count)} 个。</span>`;
    if (newsfeedCanCustomize(state)) {
      return `<strong>自定义话题 ${escapeHtml(count)}/${escapeHtml(policy.custom_topic_limit || 0)}</strong><span>还可创建 ${escapeHtml(policy.custom_topic_remaining || 0)} 个。</span>`;
    }
    return `
      <strong>General · 会员功能未开启</strong>
      <span>当前自定义话题 0 个；升级后可创建话题并订阅邮件。</span>
      <button type="button" data-action="show-account">查看会员权益</button>
    `;
  }

  function renderNewsfeedAccess(app, workerUrl, message = "请登录已注册且状态正常的账号继续。") {
    app.innerHTML = `
      <section class="newsfeed-access">
        <h1>Newsfeed</h1>
        <p>${escapeHtml(message)}</p>
        <button id="newsfeedLogin" class="primary" type="button">登录 / 账号</button>
      </section>
    `;
    const login = document.getElementById("newsfeedLogin");
    if (login) login.addEventListener("click", () => showAccountModal(workerUrl));
  }

  function setNewsfeedStatus(text, kind) {
    const status = document.getElementById("newsfeedStatus");
    if (!status) return;
    status.className = kind ? `newsfeed-status ${kind}` : "newsfeed-status";
    status.textContent = text || "";
  }

  function renderNewsfeedContentLoading(label, kind = "home") {
    const content = document.getElementById("newsfeedContent");
    if (content) content.innerHTML = newsfeedSkeletonMarkup(kind, label);
    setNewsfeedStatus(label, "loading");
  }

  function setNewsfeedTitle(text) {
    const title = document.getElementById("newsfeedTitle");
    if (title) title.textContent = text || "Newsfeed";
  }

  function refreshNewsfeedChrome(state) {
    const sideFeed = document.querySelector(".newsfeed-side-actions [data-action='show-feed']");
    const sideExplore = document.querySelector(".newsfeed-side-actions [data-action='show-explore']");
    const sideEmail = document.querySelector(".newsfeed-side-actions [data-action='show-email']");
    if (sideFeed) sideFeed.textContent = newsfeedText(state, "myFeed");
    if (sideExplore) sideExplore.textContent = newsfeedText(state, "explore");
    if (sideEmail) sideEmail.textContent = newsfeedText(state, "digestEmail");
    const bottomFeed = document.querySelector(".newsfeed-bottom-tabs [data-action='show-feed']");
    const bottomAdd = document.querySelector(".newsfeed-bottom-tabs [data-action='show-add']");
    const bottomExplore = document.querySelector(".newsfeed-bottom-tabs [data-action='show-explore']");
    const addWide = document.querySelector(".newsfeed-add-wide[data-action='show-add']");
    const preferences = document.getElementById("newsfeedPreferences");
    const policyNotice = document.getElementById("newsfeedPolicyNotice");
    const bottomTabs = document.querySelector(".newsfeed-bottom-tabs");
    const sideActions = document.querySelector(".newsfeed-side-actions");
    const canOpenAdd = newsfeedCanOpenAdd(state);
    const canSubscribe = newsfeedCanSubscribe(state);
    if (bottomFeed) bottomFeed.innerHTML = `<span>▯</span>${escapeHtml(newsfeedText(state, "myFeed"))}`;
    if (bottomAdd) bottomAdd.innerHTML = `<span>＋</span>${escapeHtml(newsfeedText(state, "addTopics"))}`;
    if (bottomExplore) bottomExplore.innerHTML = `<span>◇</span>${escapeHtml(newsfeedText(state, "explore"))}`;
    if (sideEmail) sideEmail.hidden = !canSubscribe;
    if (bottomAdd) bottomAdd.hidden = !canOpenAdd;
    if (addWide) addWide.hidden = !canOpenAdd;
    if (bottomTabs) bottomTabs.classList.toggle("is-public", !canOpenAdd);
    if (sideActions) sideActions.classList.toggle("is-public", !canSubscribe);
    if (preferences) preferences.hidden = !(newsfeedCanCustomize(state) || canSubscribe);
    if (policyNotice) policyNotice.innerHTML = newsfeedPolicyNoticeMarkup(state);
    const audio = document.getElementById("newsBriefingButton");
    if (audio) {
      audio.setAttribute("aria-label", newsfeedText(state, "playBriefing"));
      audio.hidden = !(state.policy && state.policy.authenticated);
    }
    renderNewsfeedPreferences(state);
  }

  function updateNewsfeedTabs(view) {
    document.querySelectorAll(".newsfeed-bottom-tabs button").forEach((button) => {
      const action = button.dataset.action || "";
      button.classList.toggle(
        "is-active",
        (view === "feed" && action === "show-feed") ||
          (view === "add" && action === "show-add") ||
          (view === "explore" && action === "show-explore") ||
          (view === "email" && action === "show-email"),
      );
    });
  }

  function normalizeNewsfeedRegionsClient(value) {
    const raw = Array.isArray(value) ? value : String(value || "").split(",");
    const out = [];
    const seen = new Set();
    for (const item of raw) {
      const clean = String(item && (item.value || item) || "").trim().slice(0, 54);
      const key = clean.toLowerCase();
      if (!clean || seen.has(key)) continue;
      seen.add(key);
      out.push(clean);
      if (out.length >= 8) break;
    }
    return out.length ? out : ["global"];
  }

  function newsfeedRegionOptions(state) {
    const defaults = [
      { value: "global", label: "Global" },
      { value: "mena", label: "MENA" },
      { value: "china", label: "China" },
      { value: "usa", label: "USA" },
    ];
    const options = Array.isArray(state.regionOptions) && state.regionOptions.length ? state.regionOptions : defaults;
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const custom = selected
      .filter((value) => !options.some((item) => item.value === value))
      .map((value) => ({ value, label: value }));
    return [...options, ...custom];
  }

  function newsfeedRegionLabel(state, value) {
    const option = newsfeedRegionOptions(state).find((item) => item.value === value);
    return option ? option.label : value;
  }

  function newsfeedPreferenceQuery(state, options = {}) {
    const params = new URLSearchParams();
    if (options.force || state.preferencesReady) {
      normalizeNewsfeedRegionsClient(state.preferredRegions).forEach((region) => params.append("regions", region));
      params.set("language", newsfeedLanguageCode(state.interfaceLanguage || state.outputLanguage || "en"));
      const regions = params.getAll("regions");
      params.delete("regions");
      params.set("regions", regions.join(","));
    }
    return params.toString();
  }

  function applyNewsfeedSettings(state, settings = {}) {
    state.settings = settings || state.settings || {};
    state.interfaceLanguage = newsfeedLanguageCode(settings.interface_language || state.interfaceLanguage || "en");
    state.outputLanguage = newsfeedLanguageCode(settings.interface_language || state.outputLanguage || settings.digest_language || "en");
    state.preferredRegions = normalizeNewsfeedRegionsClient(settings.preferred_regions || state.preferredRegions || ["global"]);
    state.preferencesReady = true;
  }

  function newsfeedLanguageOptions(selected = "en") {
    const languages = [
      ["en", "English"],
      ["zh-CN", "中文"],
      ["ja", "日本語"],
      ["ko", "한국어"],
    ];
    return languages.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedTimezoneOptions(selected = "Asia/Shanghai") {
    const timezones = [
      ["Asia/Shanghai", "China / Singapore"],
      ["America/New_York", "New York"],
      ["Europe/London", "London"],
      ["UTC", "UTC"],
    ];
    return timezones.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedNewsletterOptions(state, selected = "") {
    const topics = Array.isArray(state.topics) ? state.topics : [];
    const options = [`<option value="">${escapeHtml(newsfeedText(state, "noNewsletter"))}</option>`];
    const seen = new Set();
    for (const topic of topics) {
      const id = String(topic && topic.id || "").trim();
      if (!id || seen.has(id)) continue;
      seen.add(id);
      options.push(`<option value="${escapeHtml(id)}" ${id === selected ? "selected" : ""}>${escapeHtml(topic.title || id)}</option>`);
    }
    return options.join("");
  }

  function newsfeedEmailPayloadFromForm(state) {
    const newsletterTopicId = document.getElementById("newsNewsletterTopic")?.value || "";
    return {
      digest_email_enabled: Boolean(newsletterTopicId && document.getElementById("newsEmailEnabled")?.checked),
      newsletter_topic_id: newsletterTopicId,
      digest_send_time: document.getElementById("newsEmailTime")?.value || "09:00",
      digest_timezone: document.getElementById("newsEmailTimezone")?.value || "Asia/Shanghai",
      digest_language: document.getElementById("newsEmailLanguage")?.value || state.outputLanguage || "en",
      interface_language: state.interfaceLanguage || "en",
      preferred_regions: state.preferredRegions || ["global"],
    };
  }

  function newsfeedEmailLastStatus(settings = {}) {
    const result = String(settings.digest_last_send_result || "").trim();
    if (!result) return "";
    const at = settings.digest_last_attempt_at || settings.digest_last_sent_at || "";
    const when = at ? newsfeedTimeLabel(at) : "";
    const detail = settings.digest_last_send_detail ? ` · ${settings.digest_last_send_detail}` : "";
    return `Last email attempt: ${result}${when ? ` · ${when}` : ""}${detail}`;
  }

  function renderNewsfeedPreferences(state) {
    const mount = document.getElementById("newsfeedPreferences");
    if (!mount) return;
    if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) {
      mount.hidden = true;
      mount.innerHTML = "";
      return;
    }
    mount.hidden = false;
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const selectedLabels = selected.map((value) => newsfeedRegionLabel(state, value)).join(", ");
    const options = newsfeedRegionOptions(state);
    mount.innerHTML = `
      <div class="news-region-picker">
        <button id="newsRegionToggle" type="button" data-action="toggle-region-menu" aria-expanded="false">
          <span>${escapeHtml(newsfeedText(state, "regions"))}</span>
          <strong>${escapeHtml(selectedLabels || "Global")}</strong>
          <span>▾</span>
        </button>
        <div id="newsRegionMenu" class="news-region-menu" hidden>
          ${options.map((item) => `
            <label>
              <input type="checkbox" data-action="region-checkbox" value="${escapeHtml(item.value)}" ${selected.includes(item.value) ? "checked" : ""}>
              <span>${escapeHtml(item.label)}</span>
            </label>
          `).join("")}
          <form id="newsCustomRegionForm" class="news-custom-region-form">
            <input id="newsCustomRegionInput" type="text" placeholder="${escapeHtml(newsfeedText(state, "customRegion"))}">
            <button type="submit">${escapeHtml(newsfeedText(state, "addRegion"))}</button>
          </form>
        </div>
      </div>
      <label class="news-inline-select">
        <span>${escapeHtml(newsfeedText(state, "language"))}</span>
        <select id="newsInterfaceLanguage">${newsfeedLanguageOptions(state.interfaceLanguage || "en")}</select>
      </label>
    `;
  }

  function renderNewsfeedEmailSettings(state) {
    if (!newsfeedCanSubscribe(state)) {
      return `<section class="newsfeed-policy-card">${newsfeedPolicyNoticeMarkup(state)}</section>`;
    }
    const settings = state.settings || {};
    const session = loadAuthSession();
    const fallbackEmail = session && session.user && !session.user.email_is_generated ? session.user.email : "";
    const email = settings.digest_email || fallbackEmail || "";
    const enabled = Boolean(settings.digest_email_enabled);
    const newsletterTopicId = enabled ? String(settings.newsletter_topic_id || "global-daily") : "";
    const providerNote = settings.email_provider_configured === false
      ? (state.interfaceLanguage === "zh-CN"
        ? "邮件服务还没配置好，请先配置 Brevo API key。"
        : "Email sender is not configured yet. Add the Brevo API key first.")
      : (settings.email_provider === "brevo"
        ? (state.interfaceLanguage === "zh-CN"
          ? "Brevo 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Brevo email is connected. Save, then send a newsletter now.")
        : (state.interfaceLanguage === "zh-CN"
          ? "Cloudflare 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Cloudflare email is connected. Save, then send a newsletter now."));
    const lastStatus = newsfeedEmailLastStatus(settings);
    return `
      <section class="news-email-settings">
        <div class="news-email-copy">
          <h2>${escapeHtml(newsfeedText(state, "digestEmail"))}</h2>
          <p>${state.interfaceLanguage === "zh-CN" ? "每天定点发送最新摘要到邮箱。" : "Send the latest Daily Digest to your inbox once a day."}</p>
        </div>
        <form id="newsEmailForm" class="news-email-form">
          <label>${escapeHtml(newsfeedText(state, "email"))}
            <input id="newsEmailInput" type="email" autocomplete="email" value="${escapeHtml(email)}" readonly aria-readonly="true">
          </label>
          <label>${escapeHtml(newsfeedText(state, "newsletterTopic"))}
            <select id="newsNewsletterTopic">${newsfeedNewsletterOptions(state, newsletterTopicId)}</select>
          </label>
          <label>${escapeHtml(newsfeedText(state, "sendTime"))}
            <input id="newsEmailTime" type="time" value="${escapeHtml(settings.digest_send_time || "09:00")}">
          </label>
          <label>${escapeHtml(newsfeedText(state, "timezone"))}
            <select id="newsEmailTimezone">${newsfeedTimezoneOptions(settings.digest_timezone || "Asia/Shanghai")}</select>
          </label>
          <label>${escapeHtml(newsfeedText(state, "language"))}
            <select id="newsEmailLanguage">${newsfeedLanguageOptions(settings.digest_language || state.outputLanguage || "en")}</select>
          </label>
          <label class="news-toggle-row">
            <input id="newsEmailEnabled" type="checkbox" ${enabled ? "checked" : ""}>
            <span>${escapeHtml(newsfeedText(state, "sendDailyDigest"))} · ${state.interfaceLanguage === "zh-CN" ? "每个账号最多订阅一个，可随时取消或替换" : "one newsletter per account; cancel or replace it anytime"}</span>
          </label>
          <button id="newsEmailSubmit" class="primary" type="submit">${escapeHtml(newsfeedText(state, "saveEmail"))}</button>
          <button id="newsEmailSend" class="primary news-email-test" type="button" data-action="send-email-now">${escapeHtml(newsfeedText(state, "sendNewsletterNow"))}</button>
          <button id="newsEmailTest" class="secondary-button news-email-test" type="button" data-action="send-email-test">${escapeHtml(newsfeedText(state, "sendTestNow"))}</button>
        </form>
        <div id="newsEmailStatus" class="status-line" aria-live="polite">${escapeHtml(lastStatus || providerNote)}</div>
      </section>
    `;
  }

  function rememberNewsfeedArticles(state, items = [], topic = null) {
    for (const item of items || []) {
      if (!item || !item.id) continue;
      const id = String(item.id);
      const outputLanguage = item.output_language || topic && topic.output_language || state.outputLanguage || "en";
      state.articles.set(id, item);
      if (state.articleLanguages) state.articleLanguages.set(id, outputLanguage);
    }
  }

  function renderNewsfeedSidebar(state) {
    const list = document.getElementById("newsfeedTopicList");
    const count = document.getElementById("newsfeedTopicCount");
    if (!list) return;
    const topics = [...newsfeedVisibleTopics(state)].sort((a, b) => Number(Boolean(b.pinned)) - Number(Boolean(a.pinned)));
    list.innerHTML = topics.map((topic) => newsfeedTopicRow(topic, state)).join("") || '<div class="newsfeed-empty">No topics yet.</div>';
    if (count) {
      const policy = state.policy || normalizeNewsfeedPolicy();
      count.textContent = policy.unlimited
        ? `${policy.custom_topic_count || 0} custom · unlimited`
        : `${policy.custom_topic_count || 0}/${policy.custom_topic_limit || 0} custom`;
    }
  }

  function renderNewsfeedHome(state) {
    const home = state.home || {};
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "dailyDigest"));
    updateNewsfeedTabs("feed");
    state.currentView = "feed";
    state.topics = newsfeedVisibleTopics(state, home.topics || state.topics || []);
    rememberNewsfeedArticles(state, home.highlights || []);
    rememberNewsfeedArticles(state, home.headlines || []);
    renderNewsfeedSidebar(state);
    const category = state.homeCategory || "Investment";
    const categories = home.categories || ["Investment", "Tech", "Politics", "Industries"];
    const filtered = (home.headlines || []).filter((item) => !category || item.category === category);
    const visible = filtered.length ? filtered : (home.headlines || []);
    content.innerHTML = `
      <section class="news-digest-panel">
        <div>
          <div class="news-section-kicker">${escapeHtml(newsfeedText(state, "dailyDigest"))} <span>${escapeHtml(String(home.digest_count || 0).padStart(2, "0"))}</span></div>
          <ul>${newsfeedDigestMarkup(home.daily_digest)}</ul>
        </div>
        ${newsfeedSourceStack(home.highlights || [])}
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>${escapeHtml(newsfeedText(state, "topHeadlines"))}</h2>
          <span>${escapeHtml(home.updated_label || "")}</span>
        </div>
        <div class="news-category-tabs">
          ${categories.map((item) => `
            <button type="button" data-action="home-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(item)}</button>
          `).join("")}
        </div>
        <div class="news-story-list">
          ${visible.slice(0, 12).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || `<div class="newsfeed-empty">${escapeHtml(newsfeedText(state, "noHeadlines"))}</div>`}
        </div>
      </section>
    `;
  }

  function renderNewsfeedAdd(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const home = state.home || {};
    const policy = state.policy || normalizeNewsfeedPolicy();
    const suggestions = home.suggested_topics || [];
    setNewsfeedTitle(newsfeedText(state, "addTopics"));
    updateNewsfeedTabs("add");
    state.currentView = "add";
    if (!newsfeedCanCreateTopic(state)) {
      const requestedTopic = String(state.pendingRequestedTopic || "").trim().slice(0, 600);
      const requestForm = policy.request_allowed ? `
        <form id="newsTopicRequestForm" class="news-topic-request-form">
          <label for="newsTopicRequestInput">希望继续追踪的话题</label>
          <textarea id="newsTopicRequestInput" rows="4" maxlength="600" required>${escapeHtml(requestedTopic)}</textarea>
          <label for="newsTopicRequestLanguage">输出语言</label>
          <select id="newsTopicRequestLanguage">${newsfeedLanguageOptions(state.outputLanguage || "en")}</select>
          <label class="news-topic-request-honeypot" aria-hidden="true">请勿填写<input id="newsTopicRequestHoneypot" type="text" tabindex="-1" autocomplete="off"></label>
          <label class="news-topic-request-confirm"><input id="newsTopicRequestConfirm" type="checkbox" required> 我确认提交此话题申请，由团队人工审核后处理。</label>
          <button id="newsTopicRequestSubmit" class="primary" type="submit">确认提交申请</button>
          <p id="newsTopicRequestStatus" class="status-line" role="status" aria-live="polite"></p>
        </form>
      ` : `<button class="primary" type="button" data-action="show-account">查看会员权益</button>`;
      content.innerHTML = `
        <section class="news-add-panel news-topic-limit-panel">
          <div class="news-add-meta">
            <strong>自定义话题额度已用完</strong>
            <span>已创建 ${escapeHtml(policy.custom_topic_count || 0)}/${escapeHtml(policy.custom_topic_limit || 0)} 个；不会自动提交申请。</span>
          </div>
          <p>如需继续创建，请确认具体话题后提交申请。</p>
          ${requestForm}
        </section>
      `;
      return;
    }
    content.innerHTML = `
      <section class="news-add-panel">
        <div class="news-add-meta">
          <strong>${policy.unlimited ? `${escapeHtml(policy.custom_topic_count || 0)} custom · unlimited` : `${escapeHtml(policy.custom_topic_count || 0)}/${escapeHtml(policy.custom_topic_limit || 0)} custom topics`}</strong>
          <span>${policy.unlimited ? escapeHtml(newsfeedText(state, "suggestedTopics")) : `还可创建 ${escapeHtml(policy.custom_topic_remaining || 0)} 个`}</span>
        </div>
        <div class="news-suggested-list">
          ${suggestions.map((topic) => `<button type="button" data-action="suggest-topic" data-topic="${escapeHtml(topic)}">${escapeHtml(topic)}</button>`).join("")}
        </div>
        <div class="news-language-row">
          <label for="newsTopicLanguage">${escapeHtml(newsfeedText(state, "outputLanguage"))}</label>
          <select id="newsTopicLanguage">
            ${newsfeedLanguageOptions(state.outputLanguage || "en")}
          </select>
        </div>
        <div id="newsTopicStatus" class="status-line" aria-live="polite"></div>
        <form id="newsTopicForm" class="news-topic-form">
          <textarea id="newsTopicInput" rows="4" placeholder="Type any topic you want to follow"></textarea>
          <button id="newsTopicSubmit" class="primary" type="submit" aria-label="Create topic">↑</button>
        </form>
        ${newsfeedCanSubscribe(state) ? renderNewsfeedEmailSettings(state) : ""}
      </section>
    `;
  }

  function renderNewsfeedExplore(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const explore = state.explore || {};
    const categories = explore.categories || ["Tech", "Industries", "Investment", "Politics"];
    const category = state.exploreCategory || categories[0] || "";
    const items = (explore.items || []).filter((item) => !category || item.category === category);
    rememberNewsfeedArticles(state, explore.items || []);
    setNewsfeedTitle(newsfeedText(state, "explore"));
    updateNewsfeedTabs("explore");
    state.currentView = "explore";
    content.innerHTML = `
      <section class="newsfeed-section">
        <div class="news-category-tabs news-category-tabs-large">
          ${categories.map((item) => `
            <button type="button" data-action="explore-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(item)}</button>
          `).join("")}
        </div>
        <div class="news-story-list news-story-list-cards">
          ${items.slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  function renderNewsfeedEmailView(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "digestEmail"));
    updateNewsfeedTabs("email");
    state.currentView = "email";
    content.innerHTML = renderNewsfeedEmailSettings(state);
  }

  function renderNewsfeedTopic(state, topic, items) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    rememberNewsfeedArticles(state, items || [], topic);
    setNewsfeedTitle(topic && topic.title || "Topic");
    updateNewsfeedTabs("topic");
    state.currentView = "topic";
    state.currentTopic = topic;
    state.currentTopicItems = items || [];
    content.innerHTML = `
      <section class="news-topic-hero">
        <div>
          <span class="news-topic-mark">“</span>
          <h2>${escapeHtml(topic && topic.title || "Topic")}</h2>
          <p>${escapeHtml(topic && topic.description || "")}</p>
        </div>
        <div class="news-topic-source-line">
          <span>Sources</span>
          ${newsfeedSourceStack(items || [])}
        </div>
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>Top Stories</h2>
          <span>${escapeHtml(topic && topic.updated_label || "")}</span>
        </div>
        <div class="news-story-list news-story-list-cards">
          ${(items || []).slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1, { featured: index === 0 })).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  async function renderNewsfeedArticle(state, article) {
    const content = document.getElementById("newsfeedContent");
    if (!content || !article) return;
    state.currentView = "article";
    setNewsfeedTitle("Story");
    updateNewsfeedTabs("article");
    content.innerHTML = `
      <article class="news-article-detail">
        <button class="news-icon-button" type="button" data-action="article-back" aria-label="Back">‹</button>
        <header>
          <div>
            <h2>${escapeHtml(article.title || "Untitled")}</h2>
            <p>${escapeHtml(newsfeedStoryMeta(article))}</p>
          </div>
          ${article.image_url ? `<img src="${escapeHtml(article.image_url)}" alt="">` : newsfeedLogoMarkup(article)}
        </header>
        <div class="news-article-source">
          ${newsfeedLogoMarkup(article)}
          <span>${escapeHtml(newsfeedSourceName(article))}</span>
          ${article.url ? `<a href="${escapeHtml(article.url)}" target="_blank" rel="noopener noreferrer">Source</a>` : ""}
        </div>
        <div class="news-article-tabs">
          <button type="button" class="is-active">Narrative</button>
          <button type="button">Structured</button>
        </div>
        <section class="news-article-stream">
          <h3>Summary</h3>
          <div id="newsArticleSummary" class="news-stream-text"></div>
          <h3>Narrative</h3>
          <div id="newsArticleNarrative" class="news-stream-text"></div>
        </section>
      </article>
    `;
    await streamNewsfeedArticle(state, article);
  }

  async function streamNewsfeedArticle(state, article) {
    const summary = document.getElementById("newsArticleSummary");
    const narrative = document.getElementById("newsArticleNarrative");
    if (!summary || !narrative) return;
    if (!(state.policy && state.policy.authenticated)) {
      summary.textContent = article.summary || "打开原始来源查看完整报道。";
      narrative.textContent = "登录并开通会员后，可生成结构化摘要与语音简报。";
      return;
    }
    summary.textContent = "Generating summary...";
    narrative.textContent = "Writing narrative...";
    try {
      const response = await fetch(`${state.workerUrl}/newsfeed/article`, {
        method: "POST",
        cache: "no-store",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ article }),
      });
      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.detail || "Could not load story.");
      }
      if (!response.body) {
        const data = await response.json();
        summary.textContent = data.summary || "";
        narrative.textContent = data.narrative || "";
        return;
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      summary.textContent = "";
      narrative.textContent = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";
        for (const line of lines) {
          if (!line.trim()) continue;
          const event = JSON.parse(line);
          if (event.type === "summary") summary.textContent += event.text || "";
          if (event.type === "narrative") narrative.textContent += event.text || "";
        }
      }
    } catch (error) {
      narrative.textContent = error.message || "Could not load story.";
    }
  }

  function newsfeedBriefingItems(state) {
    if (state.currentView === "topic") return state.currentTopicItems || [];
    if (state.currentView === "explore") return state.explore && state.explore.items || [];
    return state.home && state.home.headlines || [];
  }

  function renderNewsfeedBriefingPanel(state, options = {}) {
    const panel = document.getElementById("newsBriefingPanel");
    if (!panel) return;
    const items = newsfeedBriefingItems(state).slice(0, 5);
    const first = items[0] || {};
    const progress = Math.max(0, Math.min(100, options.progress || 0));
    panel.hidden = false;
    panel.innerHTML = `
      <div class="news-briefing-head">
        <div>
          <strong>${escapeHtml(options.countText || "0/5 stories listened today")}</strong>
          <span>${escapeHtml(options.status || newsfeedText(state, "playBriefing"))}</span>
        </div>
        <button class="news-icon-button" type="button" data-action="close-briefing" aria-label="Close">×</button>
      </div>
      <div class="news-briefing-now">
        <div>
          <span>${escapeHtml(newsfeedText(state, "nowPlaying"))}</span>
          <h2>${escapeHtml(first.title || newsfeedText(state, "dailyDigest"))}</h2>
          ${first.id ? `<button type="button" data-action="open-article" data-id="${escapeHtml(first.id)}">${escapeHtml(newsfeedText(state, "readStory"))}</button>` : ""}
        </div>
        ${first.image_url ? `<img src="${escapeHtml(first.image_url)}" alt="">` : newsfeedLogoMarkup(first)}
      </div>
      <div class="news-briefing-playlist">
        <h3>${escapeHtml(newsfeedText(state, "playlist"))}</h3>
        ${items.slice(0, 4).map((item) => `
          <button type="button" data-action="open-article" data-id="${escapeHtml(item.id || "")}">
            <span>${escapeHtml(item.title || "Story")}</span>
            ${item.image_url ? `<img src="${escapeHtml(item.image_url)}" alt="">` : ""}
          </button>
        `).join("")}
      </div>
      <div class="news-briefing-player">
        <div class="news-briefing-progress"><span style="width:${progress}%"></span></div>
        <div class="news-briefing-controls">
          <button type="button" data-action="briefing-prev">‹</button>
          <button type="button" data-action="play-briefing" class="is-primary">${options.playing ? "❚❚" : "▶"}</button>
          <button type="button" data-action="briefing-next">›</button>
        </div>
        <small>${escapeHtml(options.voiceLabel || "browser speech")}</small>
      </div>
    `;
  }

  function stopNewsfeedBriefing(state) {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (state.briefingTimer) window.clearInterval(state.briefingTimer);
    state.briefingTimer = null;
    state.briefingPlaying = false;
    const button = document.getElementById("newsBriefingButton");
    if (button) {
      button.classList.remove("is-playing", "is-loading");
      button.innerHTML = "▥ ▶";
    }
  }

  async function playNewsfeedBriefing(state) {
    const button = document.getElementById("newsBriefingButton");
    if (state.briefingPlaying) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: "Paused", progress: state.briefingProgress || 0 });
      return;
    }
    const items = newsfeedBriefingItems(state).slice(0, 8);
    if (!items.length) {
      renderNewsfeedBriefingPanel(state, { status: "No stories ready yet" });
      return;
    }
    if (button) {
      button.classList.add("is-loading");
      button.innerHTML = "▥ …";
    }
    renderNewsfeedBriefingPanel(state, { status: "Preparing audio briefing...", playing: true });
    try {
      const data = await newsfeedJson(state.workerUrl, "/newsfeed/briefing", {
        method: "POST",
        body: JSON.stringify({
          language: state.interfaceLanguage || state.outputLanguage || "en",
          digest: state.home && state.home.daily_digest || [],
          items,
        }),
      });
      const script = data.script || "";
      state.briefingScript = script;
      state.briefingProgress = 0;
      if (!("speechSynthesis" in window) || !script) {
        renderNewsfeedBriefingPanel(state, { status: script || "Audio is not available in this browser.", progress: 100 });
        return;
      }
      stopNewsfeedBriefing(state);
      const utterance = new SpeechSynthesisUtterance(script);
      utterance.lang = state.interfaceLanguage === "zh-CN" ? "zh-CN" : state.interfaceLanguage || "en-US";
      utterance.rate = state.interfaceLanguage === "zh-CN" ? 1.05 : 1.08;
      state.briefingPlaying = true;
      if (button) {
        button.classList.remove("is-loading");
        button.classList.add("is-playing");
        button.innerHTML = "▥ ❚❚";
      }
      const started = Date.now();
      state.briefingTimer = window.setInterval(() => {
        state.briefingProgress = Math.min(100, ((Date.now() - started) / 30000) * 100);
        renderNewsfeedBriefingPanel(state, {
          status: "Playing 30 sec briefing",
          progress: state.briefingProgress,
          playing: true,
          voiceLabel: data.provider || "browser speech",
        });
      }, 800);
      utterance.onend = () => {
        stopNewsfeedBriefing(state);
        state.briefingProgress = 100;
        renderNewsfeedBriefingPanel(state, { status: "Briefing complete", progress: 100 });
      };
      utterance.onerror = () => {
        stopNewsfeedBriefing(state);
        renderNewsfeedBriefingPanel(state, { status: script, progress: 100 });
      };
      window.speechSynthesis.speak(utterance);
    } catch (error) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: error.message || "Could not prepare briefing." });
    }
  }

  async function initNewsfeed() {
    const app = document.getElementById("newsfeedApp");
    if (app) renderNewsfeedBoot(app, "Checking account...");
    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();

    if (!app) return;
    let session = loadAuthSession();
    renderNewsfeedBoot(app, "Preparing General Newsfeed...");
    session = await refreshAuthSession(workerUrl);

    const state = {
      workerUrl,
      session,
      home: null,
      explore: null,
      settings: null,
      policy: normalizeNewsfeedPolicy({}, session, []),
      topics: [],
      articles: new Map(),
      articleLanguages: new Map(),
      currentView: "feed",
      lastListView: "feed",
      homeCategory: "Investment",
      exploreCategory: "Tech",
      outputLanguage: "en",
      interfaceLanguage: "en",
      preferredRegions: ["global"],
      preferencesReady: false,
      regionOptions: [],
      briefingPlaying: false,
      briefingProgress: 0,
      briefingTimer: null,
      requestEpoch: 0,
      pendingRequestedTopic: "",
      limitRequestExposed: false,
    };

    document.addEventListener("portal-auth-change", () => window.location.reload());
    app.innerHTML = newsfeedShellMarkup(state);
    refreshNewsfeedChrome(state);
    renderNewsfeedSidebar(state);
    trackEvent(workerUrl, "page_view", {
      page: "newsfeed",
      access_state: state.policy.authenticated ? "authenticated" : "anonymous",
    });

    function latencyBucket(startedAt) {
      const elapsed = Date.now() - startedAt;
      if (elapsed < 1000) return "lt_1s";
      if (elapsed < 4000) return "1_4s";
      if (elapsed < 15000) return "4_15s";
      return "gte_15s";
    }

    function nextRequestEpoch() {
      state.requestEpoch += 1;
      return state.requestEpoch;
    }

    function applyNewsfeedResponse(data = {}) {
      state.regionOptions = data.regions || state.regionOptions || [];
      state.topics = data.topics || state.topics || [];
      applyNewsfeedPolicy(state, data);
      state.topics = newsfeedVisibleTopics(state, state.topics);
      if (data.settings || state.settings) applyNewsfeedSettings(state, data.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      renderNewsfeedSidebar(state);
    }

    async function loadHome() {
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading(newsfeedText(state, "loadingLatest"), "home");
      const query = newsfeedPreferenceQuery(state);
      const fast = await newsfeedJson(workerUrl, `/newsfeed/home?fast=1&${query}`);
      if (epoch !== state.requestEpoch) return null;
      state.home = fast;
      applyNewsfeedResponse(fast);
      if (newsfeedShouldShowRequest(state)) {
        renderNewsfeedAdd(state);
        state.limitRequestExposed = true;
        trackNewsfeedInteraction(state, "topic_limit_exposure", { outcome: "initial" });
      } else {
        renderNewsfeedHome(state);
      }
      setNewsfeedStatus(fast.pending ? newsfeedText(state, "updating") : "", fast.pending ? "loading" : "");
      trackNewsfeedInteraction(state, "feed_load", {
        outcome: "success",
        item_count: (fast.headlines || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      newsfeedJson(workerUrl, `/newsfeed/home?${newsfeedPreferenceQuery(state)}`)
        .then((data) => {
          if (epoch !== state.requestEpoch) return;
          state.home = data;
          applyNewsfeedResponse(data);
          setNewsfeedStatus("");
          if (state.currentView === "feed") {
            if (newsfeedShouldShowRequest(state)) {
              renderNewsfeedAdd(state);
              if (!state.limitRequestExposed) {
                state.limitRequestExposed = true;
                trackNewsfeedInteraction(state, "topic_limit_exposure", { outcome: "initial" });
              }
            } else {
              renderNewsfeedHome(state);
            }
          }
        })
        .catch((error) => {
          if (epoch === state.requestEpoch) setNewsfeedStatus(error.message || "Newsfeed request failed.", "error");
        });
      return fast;
    }

    async function loadExplore(category = state.exploreCategory) {
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading("Loading explore...", "explore");
      const data = await newsfeedJson(workerUrl, `/newsfeed/explore?category=${encodeURIComponent(category || "")}&${newsfeedPreferenceQuery(state)}`);
      if (epoch !== state.requestEpoch) return null;
      state.explore = data;
      state.exploreCategory = category || (data.categories && data.categories[0]) || "";
      applyNewsfeedResponse(data);
      setNewsfeedStatus("");
      renderNewsfeedExplore(state);
      trackNewsfeedInteraction(state, "explore_load", {
        outcome: "success",
        category: state.exploreCategory,
        item_count: (data.items || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      return data;
    }

    async function loadTopic(id) {
      const cleanId = String(id || "").trim();
      if (!newsfeedSystemTopic(cleanId) && !newsfeedCanCustomize(state)) {
        setNewsfeedStatus("登录并开通会员后可查看自定义话题。", "error");
        return null;
      }
      const epoch = nextRequestEpoch();
      const startedAt = Date.now();
      renderNewsfeedContentLoading("Preparing topic package...", "topic");
      const data = await newsfeedJson(workerUrl, `/newsfeed/topic?id=${encodeURIComponent(cleanId)}&${newsfeedPreferenceQuery(state)}`);
      if (epoch !== state.requestEpoch) return null;
      applyNewsfeedResponse(data);
      setNewsfeedStatus("");
      renderNewsfeedTopic(state, data.topic, data.items || []);
      trackNewsfeedInteraction(state, "topic_load", {
        outcome: "success",
        topic: data.topic || cleanId,
        item_count: (data.items || []).length,
        latency_bucket: latencyBucket(startedAt),
      });
      return data;
    }

    async function reloadCurrentNewsfeed() {
      if (state.currentView === "explore") return loadExplore(state.exploreCategory);
      if (state.currentView === "topic" && state.currentTopic) return loadTopic(state.currentTopic.id);
      if (state.currentView === "email" && newsfeedCanSubscribe(state)) {
        nextRequestEpoch();
        renderNewsfeedEmailView(state);
        return null;
      }
      return loadHome();
    }

    async function saveNewsfeedPreferences(reload = true) {
      if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return null;
      state.preferencesReady = true;
      refreshNewsfeedChrome(state);
      const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
        method: "POST",
        body: JSON.stringify({
          preferred_regions: state.preferredRegions,
          interface_language: state.interfaceLanguage,
        }),
      });
      applyNewsfeedPolicy(state, data);
      applyNewsfeedSettings(state, data.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      trackNewsfeedInteraction(state, "preferences_save", {
        outcome: "success",
        language: state.interfaceLanguage,
        region_count: (state.preferredRegions || []).length,
      });
      if (reload) await reloadCurrentNewsfeed();
      return data;
    }

    function closeSidebar() {
      const sidebar = document.getElementById("newsfeedSidebar");
      if (sidebar) sidebar.classList.remove("is-open");
    }

    app.addEventListener("click", async (event) => {
      const control = event.target.closest("[data-action]");
      if (!control) return;
      const action = control.dataset.action;
      try {
        if (action === "show-login" || action === "show-account") {
          trackNewsfeedInteraction(state, "membership_cta", { outcome: "open" });
          showAccountModal(workerUrl);
          return;
        }
        if (action === "toggle-sidebar") {
          document.getElementById("newsfeedSidebar")?.classList.toggle("is-open");
          return;
        }
        if (action === "show-feed") {
          closeSidebar();
          trackNewsfeedInteraction(state, "view_feed");
          if (!state.home) await loadHome();
          else {
            nextRequestEpoch();
            renderNewsfeedHome(state);
          }
          return;
        }
        if (action === "show-add") {
          if (!newsfeedCanOpenAdd(state)) return;
          closeSidebar();
          nextRequestEpoch();
          renderNewsfeedAdd(state);
          trackNewsfeedInteraction(state, "view_add", { custom_topic_remaining: state.policy.custom_topic_remaining });
          return;
        }
        if (action === "show-explore") {
          closeSidebar();
          await loadExplore();
          return;
        }
        if (action === "show-email") {
          if (!newsfeedCanSubscribe(state)) return;
          closeSidebar();
          nextRequestEpoch();
          renderNewsfeedEmailView(state);
          trackNewsfeedInteraction(state, "view_email");
          return;
        }
        if (action === "send-email-test" || action === "send-email-now") {
          if (!newsfeedCanSubscribe(state)) return;
          const isTest = action === "send-email-test";
          const status = document.getElementById("newsEmailStatus");
          const button = document.getElementById(isTest ? "newsEmailTest" : "newsEmailSend");
          if (status) {
            status.className = "status-line";
            status.textContent = isTest ? "Sending test digest email..." : "Sending newsletter digest...";
          }
          if (button) {
            button.disabled = true;
            button.classList.add("is-loading");
            button.textContent = "Sending...";
          }
          trackNewsfeedInteraction(state, isTest ? "email_test" : "email_send", { outcome: "submit" });
          const data = await newsfeedJson(workerUrl, isTest ? "/newsfeed/email-test" : "/newsfeed/email-send", {
            method: "POST",
            body: JSON.stringify(newsfeedEmailPayloadFromForm(state)),
          });
          applyNewsfeedPolicy(state, data);
          applyNewsfeedSettings(state, data.settings || state.settings || {});
          renderNewsfeedEmailView(state);
          const nextStatus = document.getElementById("newsEmailStatus");
          if (nextStatus) {
            nextStatus.className = data.sent ? "status-line ok" : "status-line error";
            const idSuffix = data.message_id ? ` (${data.message_id})` : "";
            nextStatus.textContent = data.sent
              ? (isTest
                ? `Test digest accepted by ${data.provider || "email provider"}.${idSuffix}`
                : `Newsletter accepted by ${data.provider || "email provider"}.${idSuffix}`)
              : (data.detail || state.settings.digest_last_send_detail || (isTest ? "Test email was not sent." : "Newsletter email was not sent."));
          }
          trackNewsfeedInteraction(state, isTest ? "email_test" : "email_send", {
            outcome: data.sent ? "success" : "error",
            provider: data.provider || "",
          });
          return;
        }
        if (action === "toggle-region-menu") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          const menu = document.getElementById("newsRegionMenu");
          const toggle = document.getElementById("newsRegionToggle");
          if (menu) {
            const nextHidden = !menu.hidden;
            menu.hidden = nextHidden;
            if (toggle) toggle.setAttribute("aria-expanded", String(!nextHidden));
          }
          return;
        }
        if (action === "play-briefing") {
          if (!(state.policy && state.policy.authenticated)) return;
          trackNewsfeedInteraction(state, "briefing_toggle");
          await playNewsfeedBriefing(state);
          return;
        }
        if (action === "close-briefing") {
          stopNewsfeedBriefing(state);
          const panel = document.getElementById("newsBriefingPanel");
          if (panel) panel.hidden = true;
          return;
        }
        if (action === "briefing-prev" || action === "briefing-next") {
          renderNewsfeedBriefingPanel(state, {
            status: state.briefingScript || newsfeedText(state, "playBriefing"),
            progress: state.briefingProgress || 0,
            playing: state.briefingPlaying,
          });
          return;
        }
        if (action === "home-category") {
          state.homeCategory = control.dataset.category || "";
          renderNewsfeedHome(state);
          trackNewsfeedInteraction(state, "category_select", { category: state.homeCategory, view: "feed" });
          return;
        }
        if (action === "explore-category") {
          state.exploreCategory = control.dataset.category || "";
          renderNewsfeedExplore(state);
          trackNewsfeedInteraction(state, "category_select", { category: state.exploreCategory, view: "explore" });
          return;
        }
        if (action === "suggest-topic") {
          const input = document.getElementById("newsTopicInput");
          if (input) input.value = control.dataset.topic || "";
          trackNewsfeedInteraction(state, "topic_suggestion_select");
          return;
        }
        if (action === "open-topic") {
          const id = String(control.dataset.id || "");
          if (!newsfeedSystemTopic(id) && !newsfeedCanCustomize(state)) return;
          closeSidebar();
          trackNewsfeedInteraction(state, "topic_open", { topic: id });
          await loadTopic(id);
          return;
        }
        if (action === "pin-topic") {
          if (!newsfeedCanCustomize(state)) return;
          const id = control.dataset.id || "";
          const topic = (state.topics || []).find((item) => String(item.id) === id);
          const pinned = !(topic && topic.pinned);
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics/pin", {
            method: "POST",
            body: JSON.stringify({ id, pinned }),
          });
          applyNewsfeedPolicy(state, data);
          if (topic) topic.pinned = pinned;
          renderNewsfeedSidebar(state);
          trackNewsfeedInteraction(state, "topic_pin", { topic: id, outcome: pinned ? "pinned" : "unpinned" });
          return;
        }
        if (action === "open-article") {
          const id = String(control.dataset.id || "");
          const article = state.articles.get(id);
          state.lastListView = state.currentView === "article" ? state.lastListView : state.currentView;
          trackNewsfeedInteraction(state, "article_open", { topic: id });
          await renderNewsfeedArticle(state, article ? { ...article, output_language: state.articleLanguages.get(id) || state.outputLanguage || "en" } : article);
          return;
        }
        if (action === "article-back") {
          if (state.lastListView === "explore") renderNewsfeedExplore(state);
          else if (state.lastListView === "topic") renderNewsfeedTopic(state, state.currentTopic, state.currentTopicItems);
          else renderNewsfeedHome(state);
        }
      } catch (error) {
        trackNewsfeedInteraction(state, "ui_error", { outcome: "error", reason: error.code || "request_failed" });
        setNewsfeedStatus(error.message || "Newsfeed request failed.", "error");
      }
    });

    app.addEventListener("submit", async (event) => {
      if (event.target && event.target.id === "newsTopicForm") {
        event.preventDefault();
        if (!newsfeedCanCreateTopic(state)) {
          renderNewsfeedAdd(state);
          return;
        }
        const input = document.getElementById("newsTopicInput");
        const language = document.getElementById("newsTopicLanguage");
        const status = document.getElementById("newsTopicStatus");
        const submit = document.getElementById("newsTopicSubmit");
        const topic = input ? input.value.trim() : "";
        if (!topic) return;
        const outputLanguage = language ? language.value : "en";
        state.outputLanguage = outputLanguage || "en";
        if (status) {
          status.className = "status-line";
          status.textContent = "Creating topic package...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "…";
        }
        trackNewsfeedInteraction(state, "topic_create", { outcome: "submit", requested_topic: topic, language: outputLanguage });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics", {
            method: "POST",
            body: JSON.stringify({ topic, output_language: outputLanguage, preferred_regions: state.preferredRegions }),
          });
          state.topics = data.topics || state.topics || [];
          applyNewsfeedPolicy(state, data);
          state.topics = newsfeedVisibleTopics(state, state.topics);
          refreshNewsfeedChrome(state);
          renderNewsfeedSidebar(state);
          renderNewsfeedTopic(state, data.topic, data.items || []);
          setNewsfeedStatus(data.pending ? "Topic created. Stories are loading; open it again in a moment." : "", data.pending ? "ok" : "");
          trackNewsfeedInteraction(state, "topic_create", { outcome: "success", topic: data.topic || topic, language: outputLanguage });
        } catch (error) {
          if (error.status === 409 && error.code === "NEWSFEED_TOPIC_LIMIT") {
            state.pendingRequestedTopic = String(error.data && error.data.requested_topic || topic).trim().slice(0, 600);
            applyNewsfeedPolicy(state, error.data || {});
            refreshNewsfeedChrome(state);
            renderNewsfeedAdd(state);
            trackNewsfeedInteraction(state, "topic_create", { outcome: "limit", requested_topic: topic });
          } else if (status) {
            status.className = "status-line error";
            status.textContent = error.message || "Could not create topic.";
            trackNewsfeedInteraction(state, "topic_create", { outcome: "error", requested_topic: topic, reason: error.code || "request_failed" });
          }
        } finally {
          if (submit && submit.isConnected) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
            submit.textContent = "↑";
          }
        }
      }
      if (event.target && event.target.id === "newsTopicRequestForm") {
        event.preventDefault();
        if (!(state.policy && state.policy.request_allowed)) return;
        const topicInput = document.getElementById("newsTopicRequestInput");
        const language = document.getElementById("newsTopicRequestLanguage");
        const confirm = document.getElementById("newsTopicRequestConfirm");
        const honeypot = document.getElementById("newsTopicRequestHoneypot");
        const status = document.getElementById("newsTopicRequestStatus");
        const submit = document.getElementById("newsTopicRequestSubmit");
        const topic = topicInput ? topicInput.value.trim() : "";
        if (!topic || !confirm || !confirm.checked) {
          if (status) {
            status.className = "status-line error";
            status.textContent = "请填写话题并勾选确认后再提交。";
          }
          return;
        }
        const outputLanguage = language ? language.value : state.outputLanguage || "en";
        const body = {
          topic,
          output_language: outputLanguage,
          preferred_regions: state.preferredRegions || ["global"],
          page_path: currentAnalyticsPath(),
          honeypot: honeypot ? honeypot.value : "",
        };
        if (submit) {
          submit.disabled = true;
          submit.textContent = "提交中…";
        }
        if (status) {
          status.className = "status-line";
          status.textContent = "正在提交申请…";
        }
        trackNewsfeedInteraction(state, "topic_request", { outcome: "submit", requested_topic: topic, language: outputLanguage });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics/request", {
            method: "POST",
            body: JSON.stringify(body),
          });
          applyNewsfeedPolicy(state, data);
          if (status) {
            status.className = "status-line ok";
            status.textContent = data.detail || "申请已提交，我们会后续处理。";
          }
          if (submit) submit.textContent = "已提交";
          trackNewsfeedInteraction(state, "topic_request", { outcome: "success", requested_topic: topic });
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = error.message || "申请提交失败，请稍后重试。";
          }
          if (submit) {
            submit.disabled = false;
            submit.textContent = "确认提交申请";
          }
          trackNewsfeedInteraction(state, "topic_request", { outcome: "error", requested_topic: topic, reason: error.code || "request_failed" });
        }
      }
      if (event.target && event.target.id === "newsCustomRegionForm") {
        event.preventDefault();
        if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
        const input = document.getElementById("newsCustomRegionInput");
        const value = input ? input.value.trim() : "";
        if (!value) return;
        state.preferredRegions = normalizeNewsfeedRegionsClient([...(state.preferredRegions || []), value]);
        if (input) input.value = "";
        await saveNewsfeedPreferences(true);
      }
      if (event.target && event.target.id === "newsEmailForm") {
        event.preventDefault();
        if (!newsfeedCanSubscribe(state)) return;
        const status = document.getElementById("newsEmailStatus");
        const submit = document.getElementById("newsEmailSubmit");
        const payload = newsfeedEmailPayloadFromForm(state);
        if (status) {
          status.className = "status-line";
          status.textContent = "Saving digest email settings...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "Saving...";
        }
        trackNewsfeedInteraction(state, "email_subscription", { outcome: "submit" });
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
            method: "POST",
            body: JSON.stringify(payload),
          });
          state.settings = data.settings || state.settings || {};
          applyNewsfeedPolicy(state, data);
          if (status) {
            status.className = "status-line ok";
            status.textContent = state.settings.email_provider_configured === false
              ? "Settings saved. Email delivery starts after the email sender is configured."
              : (state.settings.digest_email_enabled
                ? "Newsletter subscription saved. It will be sent at the selected time."
                : "Newsletter subscription canceled.");
          }
          trackNewsfeedInteraction(state, "email_subscription", { outcome: state.settings.digest_email_enabled ? "enabled" : "disabled" });
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = error.message || "Could not save email settings.";
          }
          trackNewsfeedInteraction(state, "email_subscription", { outcome: "error", reason: error.code || "request_failed" });
        } finally {
          if (submit) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
            submit.textContent = newsfeedText(state, "saveEmail");
          }
        }
      }
    });

    app.addEventListener("change", async (event) => {
      const target = event.target;
      try {
        if (target && target.dataset && target.dataset.action === "region-checkbox") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          const selected = Array.from(document.querySelectorAll("[data-action='region-checkbox']:checked"))
            .map((item) => item.value);
          state.preferredRegions = normalizeNewsfeedRegionsClient(selected);
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsInterfaceLanguage") {
          if (!(newsfeedCanCustomize(state) || newsfeedCanSubscribe(state))) return;
          state.interfaceLanguage = newsfeedLanguageCode(target.value || "en");
          state.outputLanguage = state.interfaceLanguage;
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsTopicLanguage") {
          state.outputLanguage = newsfeedLanguageCode(target.value || "en");
        }
        if (target && target.id === "newsNewsletterTopic") {
          const enabled = document.getElementById("newsEmailEnabled");
          if (enabled) enabled.checked = Boolean(target.value);
        }
        if (target && target.id === "newsEmailEnabled" && target.checked) {
          const topic = document.getElementById("newsNewsletterTopic");
          if (topic && !topic.value) topic.value = "global-daily";
        }
      } catch (error) {
        trackNewsfeedInteraction(state, "preferences_save", { outcome: "error", reason: error.code || "request_failed" });
        setNewsfeedStatus(error.message || "Could not save preferences.", "error");
      }
    });

    await loadHome();
  }

  async function initDelivery() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const password = deliveryPasswordFromLocation(params);
    const target = document.getElementById("delivery");
    if (!id || !password) {
      target.innerHTML = '<div class="error-state">Delivery link is incomplete.</div>';
      return;
    }
    const targetUrl = deliveryPageUrl(id, password, reportPreviewFromParams(params, id));
    target.innerHTML = `
      <div>
        <h1 class="detail-title">Opening report...</h1>
        <p class="subtle">This delivery link now opens the report page directly.</p>
      </div>
      <div class="delivery-actions">
        <a class="primary-link" href="${escapeHtml(targetUrl)}">Open report</a>
      </div>
    `;
    window.location.replace(targetUrl);
  }

  function blogMarketViewDateLabel(value) {
    const text = String(value || "");
    const match = text.match(/^(20\d{2})-(\d{2})-(\d{2})$/);
    return match ? `${match[1]}-${match[2]}-${match[3]}` : text;
  }

  function blogMarketViewCard(item) {
    const date = blogMarketViewDateLabel(item && item.date);
    const size = formatSize(item && item.size_bytes);
    const title = publicBrandText(item && item.title, "Market Views");
    return `
      <article class="blog-market-view-card">
        <time datetime="${escapeHtml(date)}">${escapeHtml(date || "每日更新")}</time>
        <strong>${escapeHtml(title)}</strong>
        ${size ? `<span class="subtle">PDF · ${escapeHtml(size)}</span>` : '<span class="subtle">PDF</span>'}
        <button class="secondary-button blog-market-view-download" type="button" data-market-view-id="${escapeHtml(item && item.id || "")}">下载 PDF</button>
      </article>
    `;
  }

  async function initBlog() {
    const workerUrl = "/api";
    const list = document.getElementById("blogMarketViewsList");
    const accessStatus = document.getElementById("blogMarketViewsAccess");
    initAccountGate(workerUrl);
    if (!list || !accessStatus) return;

    function setAccessStatus(text, kind = "") {
      accessStatus.className = kind ? `status-line ${kind}` : "status-line";
      accessStatus.textContent = text || "";
    }

    async function refreshAccess() {
      if (!loadAuthSession()) {
        setAccessStatus("登录后可下载；开通时长至少 1 个月的任意会员均可使用。", "");
        return;
      }
      setAccessStatus("正在核验会员资格…", "");
      try {
        const response = await fetch(`${workerUrl}/market-views/access`, {
          cache: "no-store",
          headers: authHeaders(),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "会员资格核验失败。");
        setAccessStatus(data.can_download
          ? "当前账号可下载 Market Views PDF。"
          : "Market Views PDF 面向开通时长至少 1 个月的会员。", data.can_download ? "ok" : "");
      } catch (error) {
        setAccessStatus(error.message || "会员资格核验失败。", "error");
      }
    }

    async function loadMarketViews() {
      try {
        const response = await fetch(`${workerUrl}/market-views`, { cache: "no-store" });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "每日 PDF 读取失败。");
        const items = Array.isArray(data.items) ? data.items : [];
        list.innerHTML = items.length
          ? items.map(blogMarketViewCard).join("")
          : '<div class="empty-state">今日 Market Views PDF 正在准备中。</div>';
      } catch (error) {
        list.innerHTML = `<div class="error-state">${escapeHtml(error.message || "每日 PDF 暂时无法读取。")}</div>`;
      }
    }

    list.addEventListener("click", async (event) => {
      const button = event.target.closest("button[data-market-view-id]");
      if (!button) return;
      if (!loadAuthSession()) {
        setAccessStatus("请先注册或登录。", "error");
        showAccountModal(workerUrl);
        return;
      }
      const id = String(button.dataset.marketViewId || "");
      if (!id) return;
      button.disabled = true;
      setAccessStatus("正在准备 PDF…", "");
      try {
        const response = await fetch(`${workerUrl}/market-views/pdf?id=${encodeURIComponent(id)}`, {
          cache: "no-store",
          headers: authHeaders(),
        });
        if (!response.ok) {
          const data = await response.json().catch(() => ({}));
          throw new Error(data.detail || "PDF 下载失败。");
        }
        triggerBlobDownload(
          await response.blob(),
          response.headers.get("Content-Disposition"),
          `${id.replace(/[^a-z0-9-]+/gi, "-") || "market-views"}.pdf`,
        );
        setAccessStatus("PDF 下载已开始。", "ok");
      } catch (error) {
        setAccessStatus(error.message || "PDF 下载失败。", "error");
      } finally {
        button.disabled = false;
      }
    });

    document.addEventListener("portal-auth-change", refreshAccess);
    await Promise.all([loadMarketViews(), refreshAccess()]);
  }

  async function initCourse() {
    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    const gate = document.getElementById("courseGate");
    const title = document.getElementById("courseGateTitle");
    const message = document.getElementById("courseGateMessage");
    const login = document.getElementById("courseLoginButton");
    const catalog = document.getElementById("courseCatalog");
    const materials = document.getElementById("courseMaterials");
    const materialsTitle = document.getElementById("courseMaterialsTitle");
    const materialsDescription = document.getElementById("courseMaterialsDescription");
    const materialsTrack = document.getElementById("courseMaterialsTrack");
    const materialsPrevious = document.getElementById("courseMaterialsPrevious");
    const materialsNext = document.getElementById("courseMaterialsNext");
    const materialsPosition = document.getElementById("courseMaterialsPosition");
    const materialsStatus = document.getElementById("courseMaterialsStatus");
    let directoryEpoch = 0;
    let courseMaterialEpoch = 0;
    let courseMaterialAccess = false;
    let courseMaterialsInitialized = false;
    let courseMaterialCount = 0;
    const courseMaterialById = new Map();
    initAccountGate(workerUrl);
    initNewsfeedNav();
    if (!gate || !title || !message || !login || !catalog) return;

    function courseMaterialText(value, limit) {
      return String(value || "").replace(/\s+/gu, " ").trim().slice(0, limit);
    }

    function normalizeCourseMaterials(payload) {
      if (!payload || typeof payload !== "object" || Number(payload.schema_version) !== 1) return null;
      const rawCourse = payload.course && typeof payload.course === "object" ? payload.course : {};
      const course = {
        id: courseMaterialText(rawCourse.id, 80),
        category: publicBrandText(courseMaterialText(rawCourse.category, 80)),
        title: publicBrandText(courseMaterialText(rawCourse.title, 120)),
      };
      if (!course.id || !course.title) return null;
      const ids = new Set();
      const items = (Array.isArray(payload.items) ? payload.items : []).map((raw) => {
        if (!raw || typeof raw !== "object" || Array.isArray(raw)) return null;
        const id = courseMaterialText(raw.id, 80).toLowerCase();
        const cover = courseMaterialText(raw.cover, 180);
        const itemTitle = publicBrandText(courseMaterialText(raw.title, 160));
        const pages = Math.trunc(Number(raw.pages || 0));
        if (!/^[a-z0-9][a-z0-9-]{2,79}$/u.test(id) || ids.has(id) || !itemTitle) return null;
        if (!/^assets\/course-covers\/[a-z0-9][a-z0-9._-]*\.(?:avif|jpe?g|png|webp)$/iu.test(cover)) return null;
        if (!Number.isFinite(pages) || pages < 1 || pages > 2000) return null;
        ids.add(id);
        return {
          id,
          title: itemTitle,
          topic: publicBrandText(courseMaterialText(raw.topic, 80)) || "战略咨询",
          summary: publicBrandText(courseMaterialText(raw.summary, 260)),
          pages,
          cover,
          featured: raw.featured === true,
        };
      }).filter(Boolean).slice(0, 60);
      if (!items.length) return null;
      const featuredIndex = items.findIndex((item) => item.featured);
      if (featuredIndex > 0) items.unshift(...items.splice(featuredIndex, 1));
      return { course, items };
    }

    function setCourseMaterialStatus(text, state = "") {
      if (!materialsStatus) return;
      materialsStatus.textContent = text;
      materialsStatus.dataset.state = state;
    }

    function setCourseMaterialAccess(canAccess) {
      courseMaterialAccess = Boolean(canAccess);
      if (!materials) return;
      materials.hidden = !(courseMaterialAccess && courseMaterialsInitialized);
      if (!courseMaterialAccess) setCourseMaterialStatus("");
    }

    async function requestCourseMaterial(item, button) {
      if (!loadAuthSession()) {
        await showAccountModal(workerUrl);
        return;
      }
      if (!courseMaterialAccess) {
        setCourseMaterialStatus("当前账号需通过会员资格核验后才能索取。", "error");
        gate.scrollIntoView({ behavior: "smooth", block: "center" });
        return;
      }

      button.disabled = true;
      button.textContent = "正在提交…";
      setCourseMaterialStatus(`正在提交《${item.title}》的索取申请…`, "busy");
      let completed = false;
      let responseStatus = 0;
      try {
        const response = await fetch(`${workerUrl}/course/material-request`, {
          method: "POST",
          cache: "no-store",
          headers: { "Content-Type": "application/json", ...authHeaders() },
          body: JSON.stringify({
            material_id: item.id,
            page_path: currentAnalyticsPath(),
            honeypot: "",
          }),
        });
        responseStatus = Number(response.status || 0);
        const data = await response.json().catch(() => ({}));
        if (!response.ok || !data.ok) {
          if (response.status === 401) clearAuthSession();
          throw new Error(data.detail || "材料索取申请提交失败，请稍后重试。");
        }
        completed = true;
        button.dataset.requested = "true";
        button.textContent = data.deduplicated ? "申请已记录" : "申请已提交";
        setCourseMaterialStatus(
          data.detail || (data.deduplicated
            ? `《${item.title}》的申请已经记录，无需重复提交。`
            : `《${item.title}》的索取申请已提交，我们会通过账号邮箱回复。`),
          "ok",
        );
        trackEvent(workerUrl, "course_material_request", {
          action: data.deduplicated ? "deduplicated" : "submitted",
          material_id: item.id,
          material_title: item.title,
          page: currentAnalyticsPath(),
        });
      } catch (error) {
        setCourseMaterialStatus(error.message || "材料索取申请提交失败，请稍后重试。", "error");
        trackEvent(workerUrl, "course_material_request", {
          action: "failed",
          material_id: item.id,
          material_title: item.title,
          page: currentAnalyticsPath(),
          response_status: responseStatus,
        });
      } finally {
        if (!completed) {
          button.disabled = false;
          button.textContent = "重新索取";
          button.setAttribute("aria-label", `${button.dataset.materialTitle || "材料"} · 重新索取`);
        }
      }
    }

    async function setupCourseMaterials(expectedEpoch) {
      if (!materials || !materialsTitle || !materialsDescription || !materialsTrack
        || !materialsPrevious || !materialsNext || !materialsPosition || !materialsStatus) return;
      if (!courseMaterialAccess || expectedEpoch !== courseMaterialEpoch) return;
      if (courseMaterialsInitialized) {
        materials.hidden = false;
        setCourseMaterialStatus(`${courseMaterialCount} 份会员封面预览 · 每份材料需单独索取`);
        return;
      }
      const payload = await loadOptionalJson("data/course-materials.json", null);
      if (!courseMaterialAccess || expectedEpoch !== courseMaterialEpoch) return;
      const manifest = normalizeCourseMaterials(payload);
      if (!manifest) {
        materials.hidden = true;
        return;
      }
      const { course, items } = manifest;
      courseMaterialCount = items.length;
      courseMaterialById.clear();
      items.forEach((item) => courseMaterialById.set(item.id, item));
      materialsTitle.textContent = course.title;
      materialsDescription.textContent = `${course.category || "战略咨询"} · ${items.length} 份会员封面预览 · 每份单独索取`;
      materialsTrack.innerHTML = items.map((item, index) => {
        const priority = index === 0 && item.featured;
        return `
          <article
            class="course-material-card${item.featured ? " is-featured" : ""}"
            data-course-material-card="${escapeHtml(item.id)}"
            role="group"
            aria-roledescription="幻灯片"
            aria-label="${index + 1} / ${items.length} · ${escapeHtml(item.title)}"
          >
            <div class="course-material-cover">
              <img
                src="${escapeHtml(item.cover)}"
                alt="${escapeHtml(item.title)}封面"
                width="720"
                height="405"
                loading="${priority ? "eager" : "lazy"}"
                decoding="async"
                ${priority ? 'fetchpriority="high"' : ""}
              >
              <span>KC桌面${item.featured ? " · 精选" : "学堂"}</span>
            </div>
            <div class="course-material-copy">
              <p>${escapeHtml(item.topic)} · ${item.pages} 页</p>
              <h3>${escapeHtml(item.title)}</h3>
              ${item.summary ? `<span>${escapeHtml(item.summary)}</span>` : ""}
              <button
                class="course-material-open"
                type="button"
                data-course-material-request="${escapeHtml(item.id)}"
                data-material-title="${escapeHtml(item.title)}"
              >单独索取</button>
            </div>
          </article>`;
      }).join("");
      courseMaterialsInitialized = true;
      materials.hidden = false;
      setCourseMaterialStatus(`${courseMaterialCount} 份会员封面预览 · 每份材料需单独索取`);

      const cards = Array.from(materialsTrack.querySelectorAll("[data-course-material-card]"));
      const reducedMotion = window.matchMedia("(prefers-reduced-motion: reduce)");
      const COURSE_MATERIAL_AUTOPLAY_MS = 6000;
      let activeIndex = 0;
      let autoplayTimer = 0;
      let scrollTimer = 0;
      let ignoreScrollUntil = 0;
      let pointerPaused = false;
      let focusPaused = false;
      let isVisible = true;

      const updatePosition = () => {
        materialsPosition.textContent = `${activeIndex + 1} / ${cards.length}`;
        materialsPosition.setAttribute("aria-label", `当前第 ${activeIndex + 1} 份，共 ${cards.length} 份`);
      };
      const autoplayAllowed = () => cards.length > 1 && !reducedMotion.matches
        && !pointerPaused && !focusPaused && isVisible && !document.hidden;
      const scheduleAutoplay = () => {
        window.clearTimeout(autoplayTimer);
        autoplayTimer = 0;
        if (!autoplayAllowed()) return;
        autoplayTimer = window.setTimeout(() => {
          moveTo(activeIndex + 1, true);
        }, COURSE_MATERIAL_AUTOPLAY_MS);
      };
      const moveTo = (nextIndex, automatic = false) => {
        if (!cards.length) return;
        activeIndex = (nextIndex + cards.length) % cards.length;
        const firstOffset = cards[0].offsetLeft;
        ignoreScrollUntil = Date.now() + 800;
        materialsTrack.scrollTo({
          left: Math.max(0, cards[activeIndex].offsetLeft - firstOffset),
          behavior: reducedMotion.matches ? "auto" : "smooth",
        });
        updatePosition();
        if (!automatic) setCourseMaterialStatus(`${courseMaterialCount} 份会员封面预览 · 每份材料需单独索取`);
        scheduleAutoplay();
      };
      const syncFromScroll = () => {
        if (Date.now() < ignoreScrollUntil || !cards.length) return;
        const firstOffset = cards[0].offsetLeft;
        const current = materialsTrack.scrollLeft;
        const maxScroll = Math.max(0, materialsTrack.scrollWidth - materialsTrack.clientWidth);
        if (maxScroll - current <= 3) {
          activeIndex = cards.length - 1;
        } else {
          activeIndex = cards.reduce((best, card, index) => (
            Math.abs(card.offsetLeft - firstOffset - current)
              < Math.abs(cards[best].offsetLeft - firstOffset - current) ? index : best
          ), 0);
        }
        updatePosition();
        scheduleAutoplay();
      };

      materialsPrevious.disabled = cards.length < 2;
      materialsNext.disabled = cards.length < 2;
      materialsPrevious.addEventListener("click", () => moveTo(activeIndex - 1));
      materialsNext.addEventListener("click", () => moveTo(activeIndex + 1));
      materialsTrack.addEventListener("keydown", (event) => {
        if (event.key === "ArrowLeft" || event.key === "ArrowRight") {
          event.preventDefault();
          moveTo(activeIndex + (event.key === "ArrowRight" ? 1 : -1));
        } else if (event.key === "Home" || event.key === "End") {
          event.preventDefault();
          moveTo(event.key === "Home" ? 0 : cards.length - 1);
        }
      });
      materialsTrack.addEventListener("scroll", () => {
        window.clearTimeout(scrollTimer);
        scrollTimer = window.setTimeout(syncFromScroll, 120);
      }, { passive: true });
      materialsTrack.addEventListener("click", (event) => {
        const button = event.target.closest("[data-course-material-request]");
        if (!button) return;
        const item = courseMaterialById.get(String(button.dataset.courseMaterialRequest || ""));
        if (item) requestCourseMaterial(item, button);
      });
      materialsTrack.querySelectorAll("img").forEach((image) => {
        image.addEventListener("error", () => image.closest(".course-material-card")?.classList.add("is-cover-missing"));
      });
      materials.addEventListener("pointerenter", () => {
        pointerPaused = true;
        scheduleAutoplay();
      });
      materials.addEventListener("pointerleave", () => {
        pointerPaused = false;
        scheduleAutoplay();
      });
      materials.addEventListener("focusin", () => {
        focusPaused = true;
        scheduleAutoplay();
      });
      materials.addEventListener("focusout", () => {
        window.setTimeout(() => {
          focusPaused = materials.contains(document.activeElement);
          scheduleAutoplay();
        }, 0);
      });
      const handleMotionChange = () => scheduleAutoplay();
      if (typeof reducedMotion.addEventListener === "function") reducedMotion.addEventListener("change", handleMotionChange);
      else if (typeof reducedMotion.addListener === "function") reducedMotion.addListener(handleMotionChange);
      document.addEventListener("visibilitychange", scheduleAutoplay);
      if ("IntersectionObserver" in window) {
        const observer = new IntersectionObserver((entries) => {
          isVisible = entries.some((entry) => entry.isIntersecting);
          scheduleAutoplay();
        }, { threshold: 0.2 });
        observer.observe(materials);
      }
      updatePosition();
      scheduleAutoplay();
    }

    function locked(titleText, messageText, showLogin = false) {
      directoryEpoch += 1;
      courseMaterialEpoch += 1;
      setCourseMaterialAccess(false);
      gate.hidden = false;
      gate.classList.remove("is-unlocked");
      title.textContent = titleText;
      message.textContent = messageText;
      login.hidden = !showLogin;
      catalog.hidden = true;
      catalog.innerHTML = "";
    }


    function setupCourseDirectoryIndex(products) {
      const directory = catalog.querySelector("#courseResourceDirectory");
      if (!directory) return;

      const categorySelect = directory.querySelector("#courseDirectoryCategory");
      const productSelect = directory.querySelector("#courseDirectoryProduct");
      const queryInput = directory.querySelector("#courseDirectorySearch");
      const fileTypeSelect = directory.querySelector("#courseDirectoryFileType");
      const popular = directory.querySelector("#courseDirectoryPopular");
      const status = directory.querySelector("#courseDirectoryStatus");
      const breadcrumb = directory.querySelector("#courseDirectoryBreadcrumb");
      const results = directory.querySelector("#courseDirectoryResults");
      const pagination = directory.querySelector("#courseDirectoryPagination");
      const pageLabel = directory.querySelector("#courseDirectoryPageLabel");
      const previousButton = directory.querySelector("#courseDirectoryPrevious");
      const nextButton = directory.querySelector("#courseDirectoryNext");
      const expandButton = directory.querySelector("#courseDirectoryExpand");
      const collapseButton = directory.querySelector("#courseDirectoryCollapse");
      if (!categorySelect || !productSelect || !queryInput || !fileTypeSelect || !popular || !status
        || !breadcrumb || !results || !pagination || !pageLabel || !previousButton || !nextButton
        || !expandButton || !collapseButton) return;

      const instanceEpoch = ++directoryEpoch;
      let activeController = null;
      let searchTimer = 0;
      let facetCourses = products.map((product) => ({ ...product, count: 0 }));
      const state = {
        category: "",
        courseId: "",
        query: "",
        fileType: "",
        page: 1,
        pageSize: 36,
      };

      const integer = (value, fallback = 0) => {
        const parsed = Number.parseInt(String(value || ""), 10);
        return Number.isFinite(parsed) && parsed >= 0 ? parsed : fallback;
      };

      const normalizeEntity = (value) => {
        if (typeof value === "string") {
          const name = value.trim();
          return name ? { name, count: 0 } : null;
        }
        if (!value || typeof value !== "object" || Array.isArray(value)) return null;
        const name = String(value.name || value.title || "").trim();
        return name ? { name, count: integer(value.count, 0) } : null;
      };

      const normalizeCourseFacet = (value) => {
        if (!value || typeof value !== "object" || Array.isArray(value)) return null;
        const id = String(value.id || value.course_id || "").trim();
        const titleText = String(value.title || value.name || "").trim();
        if (!id || !titleText) return null;
        return {
          id,
          title: titleText,
          category: String(value.category || "专业课程").trim() || "专业课程",
          count: integer(value.count, 0),
        };
      };

      const normalizeItem = (value) => {
        if (!value || typeof value !== "object" || Array.isArray(value)) return null;
        const id = String(value.id || "").trim();
        const name = String(value.name || value.title || "").trim();
        if (!id || !name) return null;
        return {
          id,
          courseId: String(value.course_id || value.courseId || "").trim(),
          category: String(value.category || "").trim(),
          name,
          folders: (Array.isArray(value.folders) ? value.folders : [])
            .map((folder) => String(folder || "").trim())
            .filter(Boolean),
          extension: String(value.extension || value.ext || "").replace(/^\./, "").trim(),
          sizeLabel: String(value.size_label || value.display_size || "").trim(),
          date: String(value.date || value.modified_at || "").trim(),
          entities: (Array.isArray(value.entities) ? value.entities : [])
            .map(normalizeEntity)
            .filter(Boolean),
        };
      };

      const normalizeNamedFacets = (values, field = "name") => (Array.isArray(values) ? values : [])
        .map((value) => {
          if (typeof value === "string") return { name: value.trim(), count: 0 };
          if (!value || typeof value !== "object") return null;
          const name = String(value[field] || value.name || value.value || "").trim();
          return name ? { name, count: integer(value.count, 0) } : null;
        })
        .filter(Boolean);

      const normalizePayload = (value) => {
        const payload = value && typeof value === "object" ? value : {};
        const facets = payload.facets && typeof payload.facets === "object" ? payload.facets : {};
        const items = (Array.isArray(payload.items) ? payload.items : []).map(normalizeItem).filter(Boolean);
        const page = Math.max(1, integer(payload.page, state.page));
        const pageSize = Math.max(1, integer(payload.page_size, state.pageSize));
        const total = integer(payload.total, items.length);
        const pages = Math.max(1, integer(payload.pages, Math.ceil(total / pageSize) || 1));
        return {
          items,
          page,
          pageSize,
          total,
          pages,
          hasMore: Boolean(payload.has_more) || page < pages,
          facets: {
            courses: (Array.isArray(facets.courses) ? facets.courses : []).map(normalizeCourseFacet).filter(Boolean),
            categories: normalizeNamedFacets(facets.categories),
            fileTypes: normalizeNamedFacets(facets.file_types),
            topEntities: (Array.isArray(facets.top_entities) ? facets.top_entities : [])
              .map(normalizeEntity)
              .filter(Boolean),
          },
        };
      };

      const requestUrl = () => {
        const params = new URLSearchParams();
        if (state.query) params.set("q", state.query);
        if (state.courseId) params.set("course_id", state.courseId);
        if (state.category) params.set("category", state.category);
        if (state.fileType) params.set("file_type", state.fileType);
        params.set("page", String(state.page));
        params.set("page_size", String(state.pageSize));
        return `${workerUrl}/course/directory?${params.toString()}`;
      };

      const courseTitleById = () => new Map([
        ...products.map((product) => [product.id, product.title]),
        ...facetCourses.map((product) => [product.id, product.title]),
      ]);

      const entityHtml = (entities) => entities.length ? `
        <span class="course-directory-entities" aria-label="相关知名机构">
          ${entities.map((entity) => `<span>${escapeHtml(entity.name)}</span>`).join("")}
        </span>` : "";

      const fileHtml = (item, titles) => {
        const metadata = [];
        const courseTitle = titles.get(item.courseId);
        if (courseTitle) metadata.push(courseTitle);
        if (item.category) metadata.push(item.category);
        if (item.extension) metadata.push(item.extension.toUpperCase());
        if (item.sizeLabel) metadata.push(item.sizeLabel);
        if (item.date) metadata.push(item.date.slice(0, 10));
        return `
          <article class="course-directory-file" data-directory-file="${escapeHtml(item.id)}">
            <span class="course-directory-kind">${escapeHtml(item.extension ? item.extension.toUpperCase() : "文件")}</span>
            <span class="course-directory-item-copy">
              <strong>${escapeHtml(item.name)}</strong>
              ${item.folders.length ? `<span class="course-directory-path">${item.folders.map(escapeHtml).join(" / ")}</span>` : ""}
              <span class="course-directory-meta">${metadata.map((value) => `<span>${escapeHtml(value)}</span>`).join("")}</span>
              ${entityHtml(item.entities)}
            </span>
          </article>`;
      };

      const buildTree = (items) => {
        const root = { title: "", children: new Map(), files: [] };
        items.forEach((item) => {
          let node = root;
          item.folders.forEach((folder) => {
            if (!node.children.has(folder)) node.children.set(folder, { title: folder, children: new Map(), files: [] });
            node = node.children.get(folder);
          });
          node.files.push(item);
        });
        return root;
      };

      const nodeCount = (node) => node.files.length
        + Array.from(node.children.values()).reduce((sum, child) => sum + nodeCount(child), 0);

      const treeHtml = (node, titles) => {
        const folders = Array.from(node.children.values()).map((child) => `
          <details class="course-directory-tree" open>
            <summary>
              <span class="course-directory-kind is-folder">目录</span>
              <strong>${escapeHtml(child.title)}</strong>
              <span>${nodeCount(child)} 项</span>
              <span class="course-directory-toggle" aria-hidden="true">+</span>
            </summary>
            <div class="course-directory-tree-children">
              ${treeHtml(child, titles)}
            </div>
          </details>`).join("");
        return `${folders}${node.files.map((item) => fileHtml(item, titles)).join("")}`;
      };

      const renderProductOptions = () => {
        const available = facetCourses.filter((course) => !state.category || course.category === state.category);
        if (state.courseId && !available.some((course) => course.id === state.courseId)) state.courseId = "";
        productSelect.innerHTML = [
          '<option value="">全部产品</option>',
          ...available.map((course) => `<option value="${escapeHtml(course.id)}">${escapeHtml(course.title)}${course.count ? ` · ${course.count}` : ""}</option>`),
        ].join("");
        productSelect.value = state.courseId;
      };

      const updateFacets = (facets) => {
        if (facets.courses.length) facetCourses = facets.courses;
        const baseCategories = Array.from(new Set(products.map((product) => product.category)));
        const categoryCount = new Map(facets.categories.map((entry) => [entry.name, entry.count]));
        const categories = Array.from(new Set([...baseCategories, ...facets.categories.map((entry) => entry.name)]));
        categorySelect.innerHTML = [
          '<option value="">全部学习方向</option>',
          ...categories.map((name) => `<option value="${escapeHtml(name)}">${escapeHtml(name)}${categoryCount.get(name) ? ` · ${categoryCount.get(name)}` : ""}</option>`),
        ].join("");
        categorySelect.value = state.category;
        renderProductOptions();
        fileTypeSelect.innerHTML = [
          '<option value="">全部文件格式</option>',
          ...facets.fileTypes.map((entry) => `<option value="${escapeHtml(entry.name)}">${escapeHtml(entry.name.toUpperCase())}${entry.count ? ` · ${entry.count}` : ""}</option>`),
        ].join("");
        if (facets.fileTypes.some((entry) => entry.name === state.fileType)) fileTypeSelect.value = state.fileType;
        else state.fileType = "";
        popular.innerHTML = facets.topEntities.length ? `
          <span>热门机构与规则</span>
          <div>${facets.topEntities.map((entity) => `
            <button type="button" data-directory-entity="${escapeHtml(entity.name)}">${escapeHtml(entity.name)}${entity.count ? ` · ${entity.count}` : ""}</button>
          `).join("")}</div>` : "";
        popular.hidden = facets.topEntities.length === 0;
      };

      const renderBreadcrumb = () => {
        const selectedCourse = facetCourses.find((course) => course.id === state.courseId);
        const labels = ["全部文件"];
        if (state.category) labels.push(state.category);
        if (selectedCourse) labels.push(selectedCourse.title);
        if (state.query) labels.push(`搜索：${state.query}`);
        breadcrumb.innerHTML = labels.map((label, index) => `
          ${index ? '<span aria-hidden="true">/</span>' : ""}<span>${escapeHtml(label)}</span>
        `).join("");
      };

      const loadDirectory = async () => {
        if (instanceEpoch !== directoryEpoch) return;
        if (activeController) activeController.abort();
        activeController = new AbortController();
        const controller = activeController;
        directory.classList.add("is-loading");
        directory.setAttribute("aria-busy", "true");
        status.textContent = state.query ? "正在搜索会员文件目录…" : "正在加载会员文件目录…";
        results.innerHTML = '<p class="course-directory-loading">正在读取具体文件标题与目录层级…</p>';
        pagination.hidden = true;
        try {
          const response = await fetch(requestUrl(), { cache: "no-store", headers: authHeaders(), signal: controller.signal });
          const data = await response.json().catch(() => ({}));
          if (!response.ok) {
            if (response.status === 401) clearAuthSession();
            throw new Error(data.detail || data.error || "文件目录加载失败。");
          }
          if (instanceEpoch !== directoryEpoch || controller !== activeController) return;
          const payload = normalizePayload(data);
          state.page = payload.page;
          state.pageSize = payload.pageSize;
          updateFacets(payload.facets);
          renderBreadcrumb();
          const tree = buildTree(payload.items);
          results.innerHTML = payload.items.length
            ? treeHtml(tree, courseTitleById())
            : '<p class="course-directory-empty">没有匹配的文件，请更换产品、学习方向或关键词。</p>';
          const start = payload.total ? (payload.page - 1) * payload.pageSize + 1 : 0;
          const end = Math.min(payload.total, payload.page * payload.pageSize);
          status.textContent = `共 ${payload.total} 个具体文件，当前显示 ${start}–${end}`;
          pageLabel.textContent = `第 ${payload.page} / ${payload.pages} 页`;
          previousButton.disabled = payload.page <= 1;
          nextButton.disabled = !payload.hasMore;
          pagination.hidden = payload.pages <= 1;
        } catch (error) {
          if (error && error.name === "AbortError") return;
          if (instanceEpoch !== directoryEpoch || controller !== activeController) return;
          status.textContent = "文件目录暂时无法加载。";
          breadcrumb.innerHTML = "";
          results.innerHTML = `
            <div class="course-directory-error">
              <strong>${escapeHtml(error.message || "文件目录加载失败。")}</strong>
              <button class="secondary" type="button" data-directory-retry>重新加载</button>
            </div>`;
        } finally {
          if (controller === activeController) {
            directory.classList.remove("is-loading");
            directory.removeAttribute("aria-busy");
          }
        }
      };

      updateFacets({ courses: facetCourses, categories: [], fileTypes: [], topEntities: [] });
      categorySelect.addEventListener("change", () => {
        state.category = categorySelect.value;
        state.courseId = "";
        state.page = 1;
        renderProductOptions();
        loadDirectory();
      });
      productSelect.addEventListener("change", () => {
        state.courseId = productSelect.value;
        state.page = 1;
        loadDirectory();
      });
      queryInput.addEventListener("input", () => {
        window.clearTimeout(searchTimer);
        searchTimer = window.setTimeout(() => {
          state.query = queryInput.value.trim();
          state.page = 1;
          loadDirectory();
        }, 320);
      });
      fileTypeSelect.addEventListener("change", () => {
        state.fileType = fileTypeSelect.value;
        state.page = 1;
        loadDirectory();
      });
      previousButton.addEventListener("click", () => {
        state.page = Math.max(1, state.page - 1);
        loadDirectory();
      });
      nextButton.addEventListener("click", () => {
        state.page += 1;
        loadDirectory();
      });
      expandButton.addEventListener("click", () => {
        results.querySelectorAll("details.course-directory-tree").forEach((details) => { details.open = true; });
      });
      collapseButton.addEventListener("click", () => {
        results.querySelectorAll("details.course-directory-tree").forEach((details) => { details.open = false; });
      });
      directory.addEventListener("click", (event) => {
        const entityButton = event.target.closest("[data-directory-entity]");
        const retryButton = event.target.closest("[data-directory-retry]");
        if (entityButton) {
          state.query = entityButton.dataset.directoryEntity || "";
          queryInput.value = state.query;
          state.page = 1;
          loadDirectory();
        } else if (retryButton) {
          loadDirectory();
        }
      });
      loadDirectory();
    }

    function renderCourseCatalog(data) {
      const rawCatalog = Array.isArray(data && data.course_catalog) && data.course_catalog.length
        ? data.course_catalog
        : (Array.isArray(data && data.courses) ? data.courses : []);
      const products = rawCatalog.map((value, index) => {
        if (value && typeof value === "object" && !Array.isArray(value)) {
          const titleText = String(value.title || "").trim();
          if (!titleText) return null;
          return {
            id: String(value.id || `COURSE-${index + 1}`).trim(),
            category: String(value.category || "专业课程").trim() || "专业课程",
            title: titleText,
            summary: String(value.summary || "围绕该主题提供结构化课程与配套资料。").trim(),
            audience: String(value.audience || "相关岗位学习者").trim(),
          };
        }
        const titleText = String(value || "").trim();
        return titleText ? {
          id: `COURSE-${index + 1}`,
          category: "专业课程",
          title: titleText,
          summary: "围绕该主题提供结构化课程与配套资料。",
          audience: "相关岗位学习者",
        } : null;
      }).filter(Boolean).slice(0, 120);
      if (!products.length) throw new Error("课程目录暂时不可用。");
      const categories = Array.from(new Set(products.map((product) => product.category)));
      const groups = categories.map((category) => {
        const categoryProducts = products
          .map((product, index) => ({ product, index }))
          .filter(({ product }) => product.category === category);
        const cards = categoryProducts.map(({ product, index }) => `
          <article class="course-card" data-course-index="${index}">
            <div class="course-card-heading">
              <span>${escapeHtml(product.id)}</span>
              <span>主题课程</span>
            </div>
            <h3>${escapeHtml(product.title)}</h3>
            <p class="course-card-summary">${escapeHtml(product.summary)}</p>
            <p class="course-card-audience"><strong>适合</strong>${escapeHtml(product.audience)}</p>
          </article>
        `).join("");
        return `
          <section class="course-group" data-course-group data-course-category="${escapeHtml(category)}">
            <header class="course-group-heading">
              <div>
                <p>LEARNING PATH</p>
                <h2>${escapeHtml(category)}</h2>
              </div>
              <span data-course-group-count>${categoryProducts.length} 个主题</span>
            </header>
            <div class="course-grid">${cards}</div>
          </section>
        `;
      }).join("");
      const contactRows = `<button class="secondary-button" type="button" data-membership-request-open="support">咨询课程详情</button>`;
      catalog.innerHTML = `
        <section class="course-browser" aria-label="课程目录筛选">
          <div class="course-browser-copy">
            <p>MEMBER CATALOG</p>
            <strong>${products.length} 个主题化产品</strong>
            <span>按学习方向归类，便于检索技能、岗位与内容主题。</span>
          </div>
          <div class="course-browser-fields">
            <label>
              <span>搜索主题</span>
              <input id="courseSearchInput" type="search" placeholder="技能、岗位或关键词" autocomplete="off">
            </label>
            <label>
              <span>学习方向</span>
              <select id="courseCategoryFilter">
                <option value="">全部方向</option>
                ${categories.map((category) => `<option value="${escapeHtml(category)}">${escapeHtml(category)}</option>`).join("")}
              </select>
            </label>
          </div>
          <p class="course-browser-status" id="courseBrowserStatus" aria-live="polite"></p>
        </section>
        <section class="course-directory" id="courseResourceDirectory" aria-labelledby="courseDirectoryTitle">
          <header class="course-directory-heading">
            <div>
              <p>MEMBER FILE INDEX</p>
              <h2 id="courseDirectoryTitle">课程文件目录</h2>
              <span>浏览具体文件标题、资料层级与相关知名机构；目录内容仅在会员资格核验通过后加载。</span>
            </div>
          </header>
          <div class="course-directory-controls">
            <label>
              <span>学习方向</span>
              <select id="courseDirectoryCategory"></select>
            </label>
            <label>
              <span>产品</span>
              <select id="courseDirectoryProduct"></select>
            </label>
            <label class="course-directory-search-field">
              <span>搜索文件目录</span>
              <input id="courseDirectorySearch" type="search" placeholder="例如：机构、律所、监管规则或项目名称" autocomplete="off">
            </label>
            <label>
              <span>文件格式</span>
              <select id="courseDirectoryFileType"><option value="">全部文件格式</option></select>
            </label>
          </div>
          <div class="course-directory-popular" id="courseDirectoryPopular" hidden></div>
          <div class="course-directory-summary">
            <div>
              <p id="courseDirectoryStatus" role="status" aria-live="polite">准备加载会员文件目录…</p>
              <nav id="courseDirectoryBreadcrumb" aria-label="当前文件筛选"></nav>
            </div>
            <div class="course-directory-tree-actions">
              <button type="button" id="courseDirectoryExpand">展开全部</button>
              <button type="button" id="courseDirectoryCollapse">折叠全部</button>
            </div>
          </div>
          <div class="course-directory-results" id="courseDirectoryResults"></div>
          <footer class="course-directory-pagination" id="courseDirectoryPagination" hidden>
            <button class="secondary" id="courseDirectoryPrevious" type="button">上一页</button>
            <span id="courseDirectoryPageLabel"></span>
            <button class="secondary" id="courseDirectoryNext" type="button">下一页</button>
          </footer>
        </section>
        <div class="course-groups">${groups}</div>
        <aside class="course-contact">
          <div>
            <strong>咨询课程详情</strong>
            <span>可咨询内容范围、学习顺序与适配岗位。</span>
          </div>
          ${contactRows || "<p>请通过账号中心联系支持。</p>"}
        </aside>`;

      const searchInput = catalog.querySelector("#courseSearchInput");
      const categoryFilter = catalog.querySelector("#courseCategoryFilter");
      const browserStatus = catalog.querySelector("#courseBrowserStatus");
      const cards = Array.from(catalog.querySelectorAll("[data-course-index]"));
      const courseGroups = Array.from(catalog.querySelectorAll("[data-course-group]"));
      const applyFilters = () => {
        const query = String(searchInput && searchInput.value || "").trim().toLocaleLowerCase("zh-CN");
        const selectedCategory = String(categoryFilter && categoryFilter.value || "");
        let visibleCount = 0;
        cards.forEach((card) => {
          const index = Number(card.dataset.courseIndex);
          const product = Number.isInteger(index) ? products[index] : null;
          const searchable = product
            ? [product.id, product.category, product.title, product.summary, product.audience].join(" ").toLocaleLowerCase("zh-CN")
            : "";
          const visible = Boolean(
            product
            && (!selectedCategory || product.category === selectedCategory)
            && (!query || searchable.includes(query))
          );
          card.hidden = !visible;
          if (visible) visibleCount += 1;
        });
        courseGroups.forEach((group) => {
          const visibleCards = Array.from(group.querySelectorAll("[data-course-index]")).filter((card) => !card.hidden);
          group.hidden = visibleCards.length === 0;
          const counter = group.querySelector("[data-course-group-count]");
          if (counter) counter.textContent = `${visibleCards.length} 个主题`;
        });
        if (browserStatus) browserStatus.textContent = visibleCount
          ? `当前显示 ${visibleCount} 个主题`
          : "没有匹配主题，请更换关键词或方向。";
      };
      if (searchInput) searchInput.addEventListener("input", applyFilters);
      if (categoryFilter) categoryFilter.addEventListener("change", applyFilters);
      applyFilters();
      setupCourseDirectoryIndex(products);
    }

    async function refresh() {
      if (!loadAuthSession()) {
        locked("登录后查看 Course", "仅剩余有效期至少 30 天的会员可访问课程咨询入口。", true);
        return;
      }
      locked("正在核验会员资格…", "请稍候。", false);
      const expectedCourseMaterialEpoch = courseMaterialEpoch;
      try {
        const response = await fetch(`${workerUrl}/course/access`, { cache: "no-store", headers: authHeaders() });
        const data = await response.json().catch(() => ({}));
        if (expectedCourseMaterialEpoch !== courseMaterialEpoch) return;
        if (!response.ok) {
          if (response.status === 401) clearAuthSession();
          throw new Error(data.detail || "课程会员资格核验失败。");
        }
        if (!data.can_access) {
          const remaining = Math.max(0, Number(data.remaining_days || 0));
          locked(
            "当前会员有效期不足 30 天",
            remaining ? `当前约剩余 ${remaining} 天；续期后即可访问。` : "当前账号没有符合条件的会员有效期。",
            false,
          );
          return;
        }
        gate.hidden = false;
        gate.classList.add("is-unlocked");
        title.textContent = "Course 已解锁";
        message.textContent = data.lifetime ? "长期会员资格已通过核验。" : `会员资格已通过核验，当前约剩余 ${Number(data.remaining_days || 0)} 天。`;
        login.hidden = true;
        setCourseMaterialAccess(true);
        renderCourseCatalog(data);
        catalog.hidden = false;
        await setupCourseMaterials(expectedCourseMaterialEpoch);
      } catch (error) {
        if (expectedCourseMaterialEpoch !== courseMaterialEpoch) return;
        locked("暂时无法核验会员资格", error.message || "请稍后刷新重试。", false);
      }
    }

    login.addEventListener("click", () => showAccountModal(workerUrl));
    document.addEventListener("portal-auth-change", refresh);
    await refresh();
  }

  const boot = page === "report"
    ? initReport
    : page === "external"
      ? initExternalDetail
      : page === "delivery"
        ? initDelivery
        : page === "activity"
          ? initAnalyticsHistory
          : page === "newsfeed"
            ? initNewsfeed
            : page === "blog"
              ? initBlog
              : page === "course"
                ? initCourse
              : initIndex;
  boot().catch((error) => {
    const target = page === "report"
      ? document.getElementById("detail")
      : page === "external"
        ? document.getElementById("externalDetail")
        : page === "delivery"
          ? document.getElementById("delivery")
          : page === "activity"
            ? document.getElementById("analyticsHistoryResults")
            : page === "newsfeed"
              ? document.getElementById("newsfeedApp")
              : page === "blog"
                ? document.getElementById("blogMarketViewsList")
                : page === "course"
                  ? document.getElementById("courseGate")
              : document.getElementById("results");
    if (target) target.innerHTML = `<div class="error-state">${escapeHtml(error.message)}</div>`;
  });
}());
