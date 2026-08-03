(function (root) {
  const WECHAT = "Support Contact";
  const EMAIL = "support@portal.example.invalid";

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

  function detailsForLanguages(languages) {
    const isChinese = languageIsChinese(languages);
    return {
      isChinese,
      channel: isChinese ? "wechat" : "email",
      value: isChinese ? WECHAT : EMAIL,
      label: isChinese ? "微信" : "邮箱",
      href: isChinese ? "" : `mailto:${EMAIL}`,
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
      target.documentElement.dataset.contactChannel = isChinese ? "wechat" : "email";
    }
  }

  root.PortalSuiteContact = {
    WECHAT,
    EMAIL,
    firstLanguage,
    languageIsChinese,
    isChineseBrowser,
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
