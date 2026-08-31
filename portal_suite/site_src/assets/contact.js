(function (root) {
  const REQUEST_KINDS = new Set(["membership", "support", "privacy", "refund", "access"]);

  function firstLanguage(languages) {
    if (Array.isArray(languages)) {
      return String(languages.find((value) => String(value || "").trim()) || "").trim();
    }
    return String(languages || "").split(",", 1)[0].trim();
  }

  function languageIsChinese(languages) {
    return /^zh(?:[-_]|$)/i.test(firstLanguage(languages));
  }

  function browserLanguages() {
    if (root.navigator && Array.isArray(root.navigator.languages) && root.navigator.languages.length) {
      return root.navigator.languages;
    }
    return [root.navigator && root.navigator.language || ""];
  }

  function isChineseBrowser() {
    return languageIsChinese(browserLanguages());
  }

  function requestKind(value) {
    const kind = String(value || "").trim().toLowerCase();
    return REQUEST_KINDS.has(kind) ? kind : "membership";
  }

  function requestHref(value) {
    return `/?request=${encodeURIComponent(requestKind(value))}`;
  }

  function detailsForLanguages(languages) {
    const isChinese = languageIsChinese(languages);
    return {
      isChinese,
      channel: "request",
      value: "申请加入会员",
      label: "站内申请",
      href: requestHref("membership"),
    };
  }

  function details() {
    return detailsForLanguages(browserLanguages());
  }

  function hydrate(scope) {
    const target = scope || root.document;
    if (!target || typeof target.querySelectorAll !== "function") return;
    const isChinese = isChineseBrowser();
    target.querySelectorAll("[data-portal-chinese-only]").forEach((element) => {
      element.hidden = !isChinese;
    });
    target.querySelectorAll("[data-portal-non-chinese-only]").forEach((element) => {
      element.hidden = isChinese;
    });
    if (target.documentElement) {
      target.documentElement.dataset.contactChannel = "request";
    }
  }

  root.PortalSuiteContact = {
    firstLanguage,
    languageIsChinese,
    isChineseBrowser,
    requestKind,
    requestHref,
    detailsForLanguages,
    details,
    hydrate,
  };

  if (root.document) {
    if (root.document.readyState === "loading") {
      root.document.addEventListener("DOMContentLoaded", () => hydrate(root.document));
    } else {
      hydrate(root.document);
    }
  }
}(window));
