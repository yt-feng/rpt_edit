(() => {
  "use strict";
  if (window.PortalDownloadInvitation) return;
  const instances = new WeakMap();
  const sessionState = new Map();
  const escapeHtml = (value) => String(value || "").replace(/[&<>"']/g, (character) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[character]));

  function safeReportHref(value) {
    try {
      if (!String(value || "").trim()) return "";
      const url = new URL(String(value), window.location.href);
      if (!/^https?:$/.test(url.protocol) || url.origin !== window.location.origin || url.username || url.password) return "";
      // Related cards only need report identity. Never carry download passwords,
      // access tokens, preview payloads or other query-string state into links.
      for (const key of [...url.searchParams.keys()]) if (!["id", "source", "origin_id", "lang"].includes(key)) url.searchParams.delete(key);
      url.hash = "";
      return `${url.pathname}${url.search}`;
    } catch (_error) { return ""; }
  }

  function readState(key) {
    if (sessionState.has(key)) return sessionState.get(key);
    try { return window.sessionStorage.getItem(key) || ""; } catch (_error) { return ""; }
  }
  function saveState(key, value) {
    sessionState.set(key, value);
    try { window.sessionStorage.setItem(key, value); } catch (_error) { /* In-memory dedupe still applies. */ }
  }

  function show(options = {}) {
    const { container, item, getSession, onRegister, track } = options;
    const source = String(options.source || "catalog");
    const reportId = String(item && item.id || "");
    if (!container || !reportId) return null;
    const key = `portal_download_invitation_v1:${encodeURIComponent(source)}:${encodeURIComponent(reportId)}`;
    const previous = instances.get(container);
    if (previous && previous.key === key) return previous.api;
    if (previous) previous.api.destroy();
    if (readState(key)) return null;

    const related = [], seen = new Set([reportId]);
    for (const row of Array.isArray(options.related) ? options.related : []) {
      const id = String(row && row.id || ""), title = String(row && row.title || "").trim().slice(0, 220);
      const href = safeReportHref(row && row.href);
      if (!id || seen.has(id) || !title || !href) continue;
      seen.add(id); related.push({ id, title, href });
      if (related.length === 3) break;
    }
    const card = document.createElement("section");
    card.className = "download-invitation";
    card.setAttribute("aria-label", "下载后继续阅读与研究");
    card.tabIndex = -1;
    let destroyed = false, signingUp = false, signupClicked = false, registeredTracked = false;
    let lastSignedIn = null;
    const currentSession = () => { try { return typeof getSession === "function" ? getSession() : null; } catch (_error) { return null; } };
    const emit = (action, data = {}) => { try { if (typeof track === "function") track(action, { report_id: reportId, source, ...data }); } catch (_error) { /* Analytics must not interrupt reading. */ } };
    const localePrefix = window.location.pathname.match(/^\/(en|ko|ja|ar|zh-Hant)(?:\/|$)/i)?.[0].replace(/\/$/, "") || "";
    const researchHref = `${localePrefix}/research.html`;
    const readingHref = document.getElementById("detail") ? "#detail" : "#externalDetail";

    function render() {
      if (destroyed) return;
      const signedIn = Boolean(currentSession());
      lastSignedIn = signedIn;
      const actions = signedIn
        ? `<a class="download-invitation-primary" href="${readingHref}">继续阅读</a>${document.getElementById("reportDiscussionHost") ? '<a class="download-invitation-secondary" href="#reportDiscussionHost">参与讨论</a>' : ""}<a class="download-invitation-secondary" href="${researchHref}">继续 AI 研究</a>`
        : '<button class="download-invitation-primary" type="button" data-invitation-register>免费注册，继续探索</button><a class="download-invitation-secondary" href="' + readingHref + '">继续阅读</a>';
      card.innerHTML = `
        <div class="download-invitation-top"><p class="download-invitation-received" role="status">PDF已接收并交给浏览器保存。</p><button class="download-invitation-dismiss" type="button" data-invitation-dismiss aria-label="关闭下载后提示 / Dismiss">×</button></div>
        <h3>${signedIn ? "继续这一轮研究" : "把这份报告作为研究的起点"}</h3>
        <p class="download-invitation-copy">${signedIn ? "读一读相关报告，交流你的看法，或用 AI 延伸研究。" : "免费创建账号，使用账号 AI 研究额度、每日签到与报告券。全文下载以账号权益为准。"}</p>
        <div class="download-invitation-actions">${actions}</div>
        <p class="download-invitation-status" role="status" aria-live="polite"></p>
        ${related.length ? `<div class="download-invitation-related"><h4>接着读 / Related reports</h4><ul>${related.map((row, index) => `<li><a href="${escapeHtml(row.href)}" target="_blank" rel="noopener noreferrer" data-invitation-related="${index}">${escapeHtml(row.title)}</a></li>`).join("")}</ul></div>` : ""}`;
    }
    function refresh() {
      if (Boolean(currentSession()) !== lastSignedIn) render();
    }
    function authCompleted(event) {
      if (destroyed || !signupClicked || !currentSession()) return;
      const detail = event.detail || {};
      if (detail.placement !== "post_download") return;
      if (detail.action === "register" && !registeredTracked) {
        registeredTracked = true;
        emit("registered");
      }
      render();
    }
    async function clicked(event) {
      const target = event.target && typeof event.target.closest === "function" ? event.target : null;
      if (!target || destroyed) return;
      const dismiss = target.closest("[data-invitation-dismiss]");
      if (dismiss) {
        event.preventDefault(); saveState(key, "dismissed"); emit("dismiss"); api.destroy(); return;
      }
      const link = target.closest("[data-invitation-related]");
      if (link) {
        const relatedItem = related[Number(link.dataset.invitationRelated)];
        if (relatedItem) emit("related_open", { report_id: relatedItem.id, parent_report_id: reportId });
        return;
      }
      const button = target.closest("[data-invitation-register]");
      if (!button || signingUp) return;
      event.preventDefault();
      if (currentSession()) { refresh(); return; }
      if (typeof onRegister !== "function") return;
      signingUp = true; signupClicked = true; button.disabled = true;
      emit("signup_click");
      try {
        await onRegister({ item, source, mode: "register", placement: "post_download", resumeIntent: true });
        if (!destroyed) {
          refresh();
          if (currentSession()) { card.scrollIntoView?.({ block: "nearest", behavior: "smooth" }); card.focus?.({ preventScroll: true }); }
        }
      } catch (_error) {
        if (!destroyed) {
          const status = card.querySelector(".download-invitation-status");
          if (status) status.textContent = "账号窗口暂未打开，请稍后重试。";
        }
      } finally {
        signingUp = false;
        if (!destroyed) { const currentButton = card.querySelector("[data-invitation-register]"); if (currentButton) currentButton.disabled = false; }
      }
    }
    const api = {
      destroy() {
        if (destroyed) return;
        destroyed = true;
        card.removeEventListener("click", clicked);
        document.removeEventListener("portal-auth-change", refresh);
        document.removeEventListener("portal-auth-complete", authCompleted);
        card.remove();
        if (instances.get(container)?.api === api) instances.delete(container);
      },
    };
    instances.set(container, { key, api });
    render(); container.append(card);
    card.addEventListener("click", clicked);
    document.addEventListener("portal-auth-change", refresh);
    document.addEventListener("portal-auth-complete", authCompleted);
    saveState(key, "shown"); emit("shown");
    return api;
  }
  window.PortalDownloadInvitation = { show };
})();
