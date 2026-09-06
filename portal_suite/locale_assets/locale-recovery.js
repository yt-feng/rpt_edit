(() => {
  "use strict";

  // The static help links remain usable even when this script cannot execute.
  const match = /^\/(ko|ja|ar)(?:\/|$)/.exec(window.location.pathname);
  if (!match || window.PortalLocaleRecovery) return;
  const locale = match[1];
  const copy = {
    ko: "이 페이지의 일부 내용을 불러오지 못했습니다. 위의 중국어 페이지 링크를 이용해 주세요.",
    ja: "このページの一部を読み込めませんでした。上の中国語ページへのリンクをご利用ください。",
    ar: "تعذر تحميل بعض محتويات هذه الصفحة. يمكنك استخدام رابط الصفحة الصينية أعلاه.",
  };
  const queryKeys = (
    "id q source title title_zh title_cn bank_code bank_name institution industry sector category " +
    "date date_folder start_date end_date page page_size page_range sort kind kind_label " +
    "file_type report_type language author rating filename page_count size_bytes available " +
    "pdf_archived include_html hot_report_generation"
  ).split(" ");
  const detailSelector = "#detail, #externalDetail, #delivery, [data-kc-locale-detail]";
  const api = { locale, status: "ready", reason: "", check };
  window.PortalLocaleRecovery = api;
  let banner;
  let errorBox;
  let scopes = [];
  let details = [];
  let observer;
  let timer;
  let started = false;

  function syncChineseLinks() {
    const current = new URL(window.location.href);
    for (const link of banner.querySelectorAll("a[data-kc-chinese-equivalent]")) {
      try {
        const target = new URL(link.getAttribute("href"), current);
        // Never copy query data to another host, a locale page, or credentials.
        if (target.origin !== current.origin || target.protocol !== "https:" || target.username || target.password ||
            /^\/(?:ko|ja|ar)(?:\/|$)/.test(target.pathname)) continue;
        for (const key of queryKeys) {
          if (current.searchParams.has(key)) target.searchParams.set(key, current.searchParams.get(key));
        }
        link.setAttribute("href", target.href);
      } catch (_) {
        // A malformed entry must not prevent the other static links from working.
      }
    }
  }

  function show(reason) {
    if (api.status !== "error") api.reason = reason;
    api.status = "error";
    if (!errorBox) return;
    errorBox.textContent = copy[locale];
    errorBox.hidden = false;
    errorBox.setAttribute("role", "status");
    errorBox.setAttribute("aria-live", "polite");
    errorBox.setAttribute("lang", locale);
    errorBox.setAttribute("dir", locale === "ar" ? "rtl" : "ltr");
    errorBox.setAttribute("data-kc-locale-reason", api.reason);
    banner.setAttribute("data-kc-locale-status", "error");
    if (observer) observer.disconnect();
    if (timer !== undefined) window.clearTimeout(timer);
  }

  function visible(node) {
    if (node.closest('[hidden], [aria-hidden="true"]')) return false;
    for (let element = node; element; element = element.parentElement) {
      if (window.getComputedStyle) {
        const style = window.getComputedStyle(element);
        if (style.display === "none" || style.visibility === "hidden") return false;
      }
    }
    return true;
  }

  function check() {
    if (api.status === "error") return api.status;
    for (const scope of scopes) {
      const errors = scope.matches(".error-state") ? [scope] : scope.querySelectorAll(".error-state");
      if (Array.from(errors).some(visible)) {
        show("error-state");
        break;
      }
    }
    return api.status;
  }

  function placeholder(text) {
    const value = String(text || "").trim();
    return value.length < 180 && /^(?:(?:loading|opening)(?: (?:report|delivery details))?|正在(?:打开|加载)(?:报告|交付详情)?|加载中|読み込み中|(?:レポート|配信詳細)(?:を)?(?:読み込み中|読み込んでいます|開いています)|(?:보고서|전달 정보)(?:를|을)?\s*(?:불러오는|여는|로드하는)\s*중|로딩\s*중|جار[ٍي]?\s*(?:تحميل|فتح)(?:\s*(?:التقرير|تفاصيل التسليم))?)[\s.…。!！]*$/iu.test(value);
  }

  function stillLoading(detail) {
    if (!visible(detail)) return false;
    const heading = detail.querySelector("h1, .detail-title");
    // A real report title wins over stale loading classes or secondary status UI.
    if (heading && heading.textContent.trim() && !placeholder(heading.textContent)) return false;
    if (!detail.textContent.trim() || placeholder(detail.textContent)) return true;
    if (heading && placeholder(heading.textContent)) return true;
    if (detail.matches('[aria-busy="true"], .is-loading, .loading, [data-loading="true"]')) return true;
    return Array.from(detail.querySelectorAll('[role="status"], .subtle, [aria-busy="true"], .is-loading, .loading'))
      .some((node) => visible(node) && placeholder(node.textContent));
  }

  function boot() {
    if (started) return;
    started = true;
    banner = document.querySelector("[data-kc-locale-help]");
    if (!banner) return;
    errorBox = banner.querySelector("[data-kc-locale-error]");
    syncChineseLinks();
    banner.setAttribute("data-kc-locale-status", api.status);
    if (api.status === "error") { show(api.reason); return; }
    details = Array.from(document.querySelectorAll(detailSelector));
    scopes = details.length ? details : Array.from(document.querySelectorAll("main"));
    const page = document.body && document.body.getAttribute("data-page");
    if (page === "404" || page === "not-found") show("error-state");
    check();
    if (api.status === "error") return;
    if (window.MutationObserver && scopes.length) {
      observer = new window.MutationObserver(check);
      for (const scope of scopes) observer.observe(scope, {
        childList: true, subtree: true, characterData: true, attributes: true,
        attributeFilter: ["class", "hidden", "aria-hidden", "style"],
      });
    }
    if (details.length) timer = window.setTimeout(() => {
      check();
      if (api.status !== "error" && details.some(stillLoading)) show("loading-timeout");
    }, 9000);
  }

  // Capture also receives resource errors, which do not bubble.
  window.addEventListener("error", (event) => {
    const target = event.target;
    if (target && target !== window) {
      if (String(target.tagName).toLowerCase() === "script") show("script-error");
      return;
    }
    show("runtime-error");
  }, true);
  window.addEventListener("unhandledrejection", () => show("unhandled-rejection"));
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})();
