(() => {
  "use strict";

  const AUTH_SESSION_KEY = "portal_auth_session";
  const CHAT_REQUEST_TIMEOUT_MS = 20 * 1000;
  const surfaces = [
    { context: "report", form: "homeChatForm", input: "homeChatInput", status: "homeChatStatus", messages: "homeChatMessages", recommendations: "homeChatRecommendations" },
    { context: "course", form: "courseChatForm", input: "courseChatInput", status: "courseChatStatus", messages: "courseChatMessages", recommendations: "courseChatRecommendations" },
  ];

  function escapeHtml(value) {
    return String(value || "").replace(/[&<>"']/g, (character) => ({
      "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;",
    })[character]);
  }

  function session() {
    try {
      const value = JSON.parse(localStorage.getItem(AUTH_SESSION_KEY) || "null");
      return value && value.token && value.user && value.user.email ? value : null;
    } catch (_error) {
      return null;
    }
  }

  function reportUrl(id) {
    return `/report.html?id=${encodeURIComponent(String(id || ""))}`;
  }

  function recommendationHtml(item) {
    const stars = "★".repeat(Math.max(1, Math.min(5, Number(item.attraction_score) || 1)));
    if (item.kind === "course") {
      const meta = [item.course_title, item.category, item.extension ? String(item.extension).toUpperCase() : "", item.size_label, item.date]
        .map((value) => String(value || "").trim()).filter(Boolean).join(" · ");
      const entities = (Array.isArray(item.entities) ? item.entities : []).slice(0, 5).join(" · ");
      return `<a class="report-chat-card" href="#courseResourceDirectory" data-course-query="${escapeHtml(item.title)}">
        <span class="report-chat-score" aria-label="资料吸引力 ${escapeHtml(item.attraction_score)} 星">${stars}</span>
        <strong>${escapeHtml(item.title || "课程资料")}</strong>
        <span>${escapeHtml(meta)}</span>
        ${entities ? `<p>${escapeHtml(entities)}</p>` : ""}
        <em>在会员文件目录中查看</em>
      </a>`;
    }
    const meta = [item.institution, item.industry, item.date_folder, item.page_count ? `${item.page_count}页` : ""]
      .map((value) => String(value || "").trim()).filter(Boolean).join(" · ");
    return `<a class="report-chat-card" href="${escapeHtml(reportUrl(item.id))}" target="_blank" rel="noopener noreferrer">
      <span class="report-chat-score" aria-label="资料吸引力 ${escapeHtml(item.attraction_score)} 星">${stars}</span>
      <strong>${escapeHtml(item.title || "报告资料")}</strong>
      <span>${escapeHtml(meta)}</span>
    </a>`;
  }

  function setup(surface) {
    const form = document.getElementById(surface.form);
    const input = document.getElementById(surface.input);
    const status = document.getElementById(surface.status);
    const messages = document.getElementById(surface.messages);
    const recommendations = document.getElementById(surface.recommendations);
    if (!form || !input || !status || !messages || !recommendations) return;
    const history = [];
    recommendations.addEventListener("click", (event) => {
      const card = event.target.closest("[data-course-query]");
      if (!card) return;
      const directorySearch = document.getElementById("courseDirectorySearch");
      if (!directorySearch) return;
      event.preventDefault();
      directorySearch.value = card.getAttribute("data-course-query") || "";
      directorySearch.dispatchEvent(new Event("input", { bubbles: true }));
      document.getElementById("courseResourceDirectory")?.scrollIntoView({ behavior: "smooth", block: "start" });
    });
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      const question = String(input.value || "").trim();
      if (question.length < 2) {
        status.textContent = "请输入公司、行业、主题、岗位或指标。";
        return;
      }
      const auth = session();
      if (!auth) {
        status.textContent = "请先点击右上角注册 / 登录，再使用资料 Chat。";
        document.getElementById("accountGate")?.click();
        return;
      }
      const button = form.querySelector("button[type=submit]");
      button.disabled = true;
      status.textContent = surface.context === "course" ? "正在检索会员课程文件并生成推荐…" : "正在检索站内报告并生成推荐…";
      recommendations.innerHTML = "";
      const controller = new AbortController();
      const timeoutId = window.setTimeout(() => controller.abort(), CHAT_REQUEST_TIMEOUT_MS);
      try {
        const response = await fetch("/api/report-chat", {
          method: "POST",
          cache: "no-store",
          signal: controller.signal,
          headers: { "Authorization": `Bearer ${auth.token}`, "Content-Type": "application/json" },
          body: JSON.stringify({ question, history, context: surface.context }),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) {
          const detail = String(data.detail || "资料 Chat 请求失败，请稍后点击重试。");
          const stage = String(data.stage_code || "").replace(/[^A-Z0-9_-]/g, "").slice(0, 32);
          const hint = String(data.request_hint || "").replace(/[^A-Z0-9-]/gi, "").slice(0, 16);
          const diagnostics = [`HTTP ${response.status}`];
          if (stage) diagnostics.push(stage);
          if (hint) diagnostics.push(`请求 ${hint}`);
          throw new Error(`${detail}（${diagnostics.join(" · ")}）`);
        }
        history.push({ role: "user", content: question }, { role: "assistant", content: data.answer || "" });
        while (history.length > 6) history.shift();
        messages.innerHTML = `<article class="report-chat-answer"><span>AI 推荐</span><p>${escapeHtml(data.answer || "")}</p></article>`;
        recommendations.innerHTML = (Array.isArray(data.recommendations) ? data.recommendations : [])
          .map(recommendationHtml).join("");
        const followUps = Array.isArray(data.follow_up_questions) ? data.follow_up_questions : [];
        status.textContent = followUps.length ? `还可以继续问：${followUps.join("；")}` : `今日还可使用 ${Number(data.usage && data.usage.remaining || 0)} 次。`;
      } catch (error) {
        status.textContent = error && error.name === "AbortError"
          ? "资料 Chat 请求超过 20 秒，已停止等待。请点击重试。"
          : error && error.message || "资料 Chat 暂时不可用，请点击重试。";
      } finally {
        window.clearTimeout(timeoutId);
        button.disabled = false;
      }
    });
  }

  const boot = () => surfaces.forEach(setup);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})();
