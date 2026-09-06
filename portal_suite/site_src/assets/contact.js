(function (root) {
  const REQUEST_KINDS = new Set(["membership", "support", "privacy", "refund", "access"]);
  const PUBLIC_ACCOUNT_EMAIL = "info@kcdesk.com";
  // Reviewed multilingual copy is serialized local data, not input for the
  // build-time JavaScript translator. No request is made by this dictionary.
  const PUBLIC_ACCOUNT_COPY = Object.freeze(JSON.parse(JSON.stringify({
    "zh-Hans": "开通账号联系",
    ko: "계정 개설 문의",
    ja: "アカウント開設のお問い合わせ",
    ar: "لفتح حساب، تواصل مع",
  })));

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

  function contentLocale() {
    const html = root.document && root.document.documentElement;
    const language = String(html && (html.lang || html.getAttribute && html.getAttribute("lang")) || "")
      .trim().replace(/_/g, "-");
    if (/^ko(?:-|$)/i.test(language)) return "ko";
    if (/^ja(?:-|$)/i.test(language)) return "ja";
    if (/^ar(?:-|$)/i.test(language)) return "ar";
    return "zh-Hans";
  }

  function hydratePublicAccountContact() {
    const doc = root.document;
    if (!doc || typeof doc.querySelector !== "function" || typeof doc.createElement !== "function") return;
    // Locale HTML already includes this contact in its static help strip.
    // Repeated hydration or loading the script twice must not duplicate it.
    if (doc.querySelector("[data-kc-public-account-contact]")) return;
    const footer = doc.querySelector(".legal-footer");
    if (!footer) return;
    const locale = contentLocale();
    const contact = doc.createElement("span");
    contact.className = "public-account-contact";
    contact.setAttribute("data-kc-public-account-contact", "");
    contact.setAttribute("lang", locale);
    contact.appendChild(doc.createTextNode(`${PUBLIC_ACCOUNT_COPY[locale]} `));
    const link = doc.createElement("a");
    link.href = `mailto:${PUBLIC_ACCOUNT_EMAIL}`;
    link.textContent = PUBLIC_ACCOUNT_EMAIL;
    link.setAttribute("dir", "ltr");
    contact.appendChild(link);
    footer.appendChild(contact);
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
    hydratePublicAccountContact();
  }

  root.PortalSuiteContact = {
    firstLanguage,
    languageIsChinese,
    isChineseBrowser,
    requestKind,
    requestHref,
    detailsForLanguages,
    details,
    contentLocale,
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
