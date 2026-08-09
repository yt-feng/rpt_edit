(() => {
  "use strict";

  const STARTED_AT = Date.parse("2019-10-03T00:00:00+08:00");
  const SECOND = 1000;
  const DAY = 24 * 60 * 60 * SECOND;

  function runtimeParts(now) {
    const elapsed = Math.max(0, now - STARTED_AT);
    const days = Math.floor(elapsed / DAY);
    const remainder = elapsed - days * DAY;
    const hours = Math.floor(remainder / (60 * 60 * SECOND));
    const minutes = Math.floor((remainder % (60 * 60 * SECOND)) / (60 * SECOND));
    const seconds = Math.floor((remainder % (60 * SECOND)) / SECOND);
    return { days, hours, minutes, seconds };
  }

  function twoDigits(value) {
    return String(value).padStart(2, "0");
  }

  function createRuntimeBanner() {
    if (document.querySelector("[data-site-runtime]")) return null;
    const banner = document.createElement("section");
    banner.className = "site-runtime-banner";
    banner.dataset.siteRuntime = "";
    banner.setAttribute("aria-label", "平台累计运行时间");
    banner.innerHTML = `
      <span class="site-runtime-indicator" aria-hidden="true"></span>
      <span class="site-runtime-copy">
        <strong>自 2019 年 10 月 3 日持续运行</strong>
        <span>累计运行 <time datetime="2019-10-03T00:00:00+08:00" data-site-runtime-value>--</time></span>
      </span>
    `;
    const footer = document.querySelector(".legal-footer");
    if (footer) footer.before(banner);
    else document.body.append(banner);
    return banner;
  }

  function ensureCourseNavigation() {
    document.querySelectorAll(".topbar-actions").forEach((actions) => {
      if (actions.querySelector('a[href$="courses.html"]')) return;
      const link = document.createElement("a");
      link.className = "topbar-link";
      link.href = "/courses.html";
      link.textContent = "Course";
      if (/\/courses\.html$/i.test(window.location.pathname)) {
        link.classList.add("is-active");
        link.setAttribute("aria-current", "page");
      }
      const newsfeed = actions.querySelector('a[href$="newsfeed.html"]');
      if (newsfeed) actions.insertBefore(link, newsfeed);
      else {
        const account = actions.querySelector("#accountGate, .account-button");
        if (account) actions.insertBefore(link, account);
        else actions.append(link);
      }
    });
  }

  function startCounter() {
    ensureCourseNavigation();
    const banner = createRuntimeBanner() || document.querySelector("[data-site-runtime]");
    const value = banner && banner.querySelector("[data-site-runtime-value]");
    if (!value) return;
    const update = () => {
      const parts = runtimeParts(Date.now());
      value.textContent = `${parts.days.toLocaleString("zh-CN")} 天 ${twoDigits(parts.hours)}:${twoDigits(parts.minutes)}:${twoDigits(parts.seconds)}`;
    };
    update();
    window.setInterval(update, SECOND);
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", startCounter, { once: true });
  } else {
    startCounter();
  }
})();
