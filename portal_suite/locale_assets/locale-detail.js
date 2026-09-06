(() => {
  "use strict";
  const match = /^\/(ko|ja|ar)\/(report|doc)\.html$/.exec(window.location.pathname);
  if (!match || window.PortalLocaleDetail) return;
  const locale = match[1];
  const copy = {
    ko: ["번역을 준비하고 있습니다…", "번역을 불러오지 못했습니다. 다시 시도하거나 위의 중국어 링크를 이용해 주세요.", "다시 시도"],
    ja: ["翻訳を準備しています…", "翻訳を読み込めませんでした。再試行するか、上の中国語リンクをご利用ください。", "再試行"],
    ar: ["جارٍ إعداد الترجمة…", "تعذر تحميل الترجمة. أعد المحاولة أو استخدم الرابط الصيني أعلاه.", "إعادة المحاولة"],
  }[locale];
  const fields = ("title title_cn title_zh display_title institution institution_en institution_cn bank_name industry sector category " +
    "kind_label report_type language description summary author rating filename").split(" ");
  const patterns = {
    catalog: /^[A-Za-z0-9_.:-]{1,256}$/,
    external: /^[0-9]{6,25}$/,
    hot: /^hot:[a-f0-9]{16}$/i,
    thinktank: /^thinktank:[A-Za-z0-9._-]{3,220}$/,
    "report-a": /^report-a:[A-Za-z0-9_-]{1,180}$/,
    authority: /^(?:(?:foreign|foreign-rt):[0-9]{1,25}|supplemental:[a-f0-9]{32})$/,
  };
  const ready = new Map();
  const pending = new Map();
  const fetcher = window.fetch.bind(window);
  const endpoint = "/api/locale/report-detail";
  const identity = (item) => ({ source: String(item && item.source || "catalog"), id: String(item && item.id || ""), locale });
  const keyFor = ({ source, id }) => `${source}:${id}`;

  function valid(identity) {
    const currentId = new URL(window.location.href).searchParams.get("id");
    return patterns[identity.source] && patterns[identity.source].test(identity.id) && currentId === identity.id
      && (match[2] === "report" ? identity.source === "catalog" : identity.source !== "catalog");
  }

  function message(target, failed, retry) {
    if (!target) return;
    target.textContent = copy[failed ? 1 : 0];
    target.setAttribute("role", "status");
    target.setAttribute("lang", locale);
    target.setAttribute("dir", locale === "ar" ? "rtl" : "ltr");
    target.setAttribute("data-kc-locale-translation", failed ? "failed" : "pending");
    if (failed && typeof retry === "function") {
      const button = document.createElement("button");
      button.type = "button"; button.textContent = copy[2];
      button.addEventListener("click", () => { button.disabled = true; retry(); });
      target.append(button);
    }
  }

  function completeFields(value) {
    if (!value || typeof value !== "object" || Array.isArray(value)) throw new Error("Invalid translation fields");
    const result = {};
    for (const field of fields) {
      if (typeof value[field] !== "string" || value[field].length > 16000) throw new Error("Invalid translation field");
      result[field] = value[field];
    }
    if (!result.title.trim()) throw new Error("Missing translated title");
    return result;
  }

  function overlayFields(value) {
    if (!value || !String(value.title || "").trim()) return null;
    const result = Object.fromEntries(fields.map((field) => [field, typeof value[field] === "string" ? value[field] : ""]));
    for (const field of ["title_cn", "title_zh", "display_title"]) result[field] = result.title;
    return result;
  }

  async function request(method, item, deadline) {
    const remaining = deadline - Date.now();
    if (remaining <= 0) throw new Error("Translation deadline");
    const controller = new AbortController();
    const timer = window.setTimeout(() => controller.abort(), Math.min(8000, remaining));
    try {
      const url = method === "GET" ? `${endpoint}?${new URLSearchParams(item)}` : endpoint;
      const response = await fetcher(url, {
        method, credentials: "omit", cache: "no-store", signal: controller.signal,
        ...(method === "POST" ? { headers: { "Content-Type": "application/json" }, body: JSON.stringify(item) } : {}),
      });
      const text = await response.text();
      if (text.length > 65536) throw new Error("Translation response too large");
      const payload = JSON.parse(text);
      if (![200, 202].includes(response.status) || !payload || !["ready", "pending"].includes(payload.status)) throw new Error("Translation unavailable");
      if (payload.status === "ready") {
        if (response.status !== 200 || payload.locale !== locale || payload.source !== item.source || payload.id !== item.id
          || !/^[a-f0-9]{64}$/.test(String(payload.source_hash || ""))) throw new Error("Translation identity mismatch");
        return { status: "ready", fields: completeFields(payload.fields) };
      }
      return { status: "pending", retry_after: Math.max(1, Math.min(5, Number(payload.retry_after) || 3)) };
    } finally { window.clearTimeout(timer); }
  }

  async function resolve(item, original) {
    const key = keyFor(item);
    if (ready.has(key)) return ready.get(key);
    const runtime = window.PortalLocale;
    if (runtime && typeof runtime.detailTranslation === "function") {
      const translated = overlayFields(await runtime.detailTranslation(item.source, item.id, original.hot_report_generation));
      if (translated) { ready.set(key, translated); return translated; }
    }
    const deadline = Date.now() + 25000;
    let result = await request("POST", item, deadline);
    for (let attempt = 0; result.status === "pending" && attempt < 5; attempt++) {
      const delay = result.retry_after * 1000;
      if (Date.now() + delay >= deadline) break;
      await new Promise((resolve) => window.setTimeout(resolve, delay));
      result = await request("GET", item, deadline);
    }
    if (result.status !== "ready") throw new Error("Translation pending");
    ready.set(key, result.fields);
    return result.fields;
  }

  async function prepare(original, target, retry) {
    message(target, false);
    const item = identity(original);
    if (!valid(item)) { message(target, true, retry); return false; }
    const key = keyFor(item);
    try {
      if (!pending.has(key)) pending.set(key, resolve(item, original).finally(() => pending.delete(key)));
      await pending.get(key);
      if (target) target.removeAttribute("data-kc-locale-translation");
      return true;
    } catch (_) { message(target, true, retry); return false; }
  }

  function apply(item) {
    const translated = ready.get(keyFor(identity(item)));
    if (!translated) throw new Error("Locale detail translation is not ready");
    // Download fallback names are transport metadata, never translated UI.
    return { ...item, ...translated, filename: item.filename };
  }

  async function catalogRecord(id) {
    try {
      const translated = ready.get(keyFor({ source: "catalog", id }));
      if (!translated || !window.PortalLocale || typeof window.PortalLocale.readCatalogDetail !== "function") return null;
      const record = await window.PortalLocale.readCatalogDetail(id, translated);
      return record && record.item ? { ...record, item: apply(record.item) } : null;
    } catch (_) { return null; }
  }

  window.PortalLocaleDetail = Object.freeze({ prepare, apply, catalogRecord, failed: (target, retry) => message(target, true, retry) });
  window.dispatchEvent(new Event("kc-locale-detail-ready"));
})();
