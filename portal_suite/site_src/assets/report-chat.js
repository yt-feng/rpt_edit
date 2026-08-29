(() => {
  "use strict";

  const AUTH_SESSION_KEY = "portal_auth_session";
  const CHAT_REQUEST_TIMEOUT_MS = 20 * 1000;
  const RESEARCH_REQUEST_TIMEOUT_MS = 60 * 1000;
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

  function reportUrl(id, item = {}) {
    const params = [["id", String(id || "")]];
    const preview = {
      title: item.title,
      title_zh: item.title_zh,
      bank_name: item.bank_name || item.institution,
      industry: item.industry,
      date_folder: item.date_folder || item.date,
      page_count: item.page_count,
      size_bytes: item.size_bytes,
      available: item.available,
    };
    for (const [key, value] of Object.entries(preview)) {
      if (value !== undefined && value !== null && value !== "") params.push([key, String(value)]);
    }
    return `/report.html?${params.map(([key, value]) => (
      `${encodeURIComponent(key)}=${encodeURIComponent(value)}`
    )).join("&")}`;
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
    return `<a class="report-chat-card" href="${escapeHtml(reportUrl(item.id, item))}" target="_blank" rel="noopener noreferrer">
      <span class="report-chat-score" aria-label="资料吸引力 ${escapeHtml(item.attraction_score)} 星">${stars}</span>
      <strong>${escapeHtml(item.title || "报告资料")}</strong>
      <span>${escapeHtml(meta)}</span>
    </a>`;
  }

  function sourceIds(value, sources) {
    if (!Array.isArray(value)) return [];
    const seen = new Set();
    return value.map((id) => String(id || "").trim()).filter((id) => {
      if (!id || seen.has(id) || !sources.has(id)) return false;
      seen.add(id);
      return true;
    }).slice(0, 8);
  }

  function sourceChipsHtml(value, sources) {
    return sourceIds(value, sources).map((id) => {
      const item = sources.get(id);
      return `<a class="report-research-source-chip" href="${escapeHtml(reportUrl(id, item))}" target="_blank" rel="noopener noreferrer">来源 · ${escapeHtml(item.institution || item.title || id)}</a>`;
    }).join("");
  }

  function researchResultHtml(data) {
    const sourceRows = (Array.isArray(data.sources) ? data.sources : Array.isArray(data.recommendations) ? data.recommendations : [])
      .filter((item) => item && typeof item === "object" && String(item.id || "").trim());
    const sources = new Map(sourceRows.map((item) => [String(item.id).trim(), item]));
    const executiveSummary = String(data.executive_summary || data.answer || "").trim();
    const findings = (Array.isArray(data.findings) ? data.findings : []).filter((item) => item && typeof item === "object").slice(0, 8);
    const dataPoints = (Array.isArray(data.data_points) ? data.data_points : []).filter((item) => item && typeof item === "object").slice(0, 12);
    const charts = (Array.isArray(data.charts) ? data.charts : []).filter((item) => {
      if (!item || typeof item !== "object" || !/^[0-9a-f]{64}$/u.test(String(item.image_id || ""))) return false;
      return sources.has(String(item.report_id || "").trim());
    }).slice(0, 6);
    const sections = [];
    if (executiveSummary) {
      sections.push(`<section class="report-research-summary"><span>研究摘要</span><p>${escapeHtml(executiveSummary)}</p><div class="report-research-source-row">${sourceChipsHtml(data.summary_source_ids, sources)}</div></section>`);
    }
    if (findings.length) {
      sections.push(`<section class="report-research-section"><h3>主要发现</h3><div class="report-research-findings">${findings.map((item) => {
        const title = String(item.title || "核心发现").trim();
        const summary = String(item.summary || item.analysis || "").trim();
        return `<article><strong>${escapeHtml(title)}</strong><p>${escapeHtml(summary)}</p><div class="report-research-source-row">${sourceChipsHtml(item.source_ids, sources)}</div></article>`;
      }).join("")}</div></section>`);
    }
    if (dataPoints.length) {
      sections.push(`<section class="report-research-section"><h3>关键数据</h3><div class="report-research-data-grid">${dataPoints.map((item) => {
        const label = String(item.label || item.metric || "数据").trim();
        const value = String(item.value || "").trim();
        const context = String(item.context || item.period || "").trim();
        return `<article><span>${escapeHtml(label)}</span><strong>${escapeHtml(value)}</strong>${context ? `<p>${escapeHtml(context)}</p>` : ""}<div class="report-research-source-row">${sourceChipsHtml(item.source_ids, sources)}</div></article>`;
      }).join("")}</div></section>`);
    }
    if (charts.length) {
      sections.push(`<section class="report-research-section"><h3>相关 Charts</h3><div class="report-research-chart-grid">${charts.map((item) => {
        const imageId = String(item.image_id);
        const reportId = String(item.report_id || "").trim();
        const report = sources.get(reportId);
        const description = String(item.description || item.trend_summary || "").trim();
        const metrics = (Array.isArray(item.metrics) ? item.metrics : []).map((value) => String(value || "").trim()).filter(Boolean).slice(0, 5).join(" · ");
        return `<figure class="report-research-chart"><img src="/api/charts/image?id=${imageId}" alt="${escapeHtml(item.title || "研究图表")}" loading="lazy" decoding="async"><figcaption><strong>${escapeHtml(item.title || "研究图表")}</strong>${description ? `<p>${escapeHtml(description)}</p>` : ""}${metrics ? `<span>${escapeHtml(metrics)}</span>` : ""}<a href="${escapeHtml(reportUrl(reportId, report))}" target="_blank" rel="noopener noreferrer">来源报告 · ${escapeHtml(report.report_title || report.title || reportId)}</a></figcaption></figure>`;
      }).join("")}</div></section>`);
    }
    return sections.join("");
  }

  function createProgressCard(form, context) {
    const card = document.createElement("div");
    card.className = "async-action report-chat-async-action";
    card.setAttribute("role", "region");
    card.setAttribute("aria-label", "资料查找进度");
    card.innerHTML = `<div class="async-action-meta">
        <strong data-chat-progress-label role="status" aria-live="polite" aria-atomic="true">检索目录</strong>
        <span data-chat-progress-time aria-hidden="true">已用时 0.0 秒</span>
      </div>
      <div class="async-action-track" aria-hidden="true"><span data-chat-progress-bar></span></div>
      <div class="async-action-meta">
        <span data-chat-progress-hint>${context === "course" ? "正在匹配会员资料" : "正在匹配站内报告"}</span>
        <button class="secondary-button" type="button" data-chat-cancel>取消</button>
      </div>`;
    form.insertAdjacentElement("afterend", card);
    return {
      card,
      label: card.querySelector("[data-chat-progress-label]"),
      elapsed: card.querySelector("[data-chat-progress-time]"),
      bar: card.querySelector("[data-chat-progress-bar]"),
      hint: card.querySelector("[data-chat-progress-hint]"),
      cancel: card.querySelector("[data-chat-cancel]"),
    };
  }

  function updateProgress(progress, startedAt, context) {
    const elapsedMs = Math.max(0, Date.now() - startedAt);
    const elapsedSeconds = (elapsedMs / 1000).toFixed(1);
    progress.elapsed.textContent = `已用时 ${elapsedSeconds} 秒`;
    if (elapsedMs < 1800) {
      progress.label.textContent = context === "report" ? "检索证据" : "检索目录";
      progress.hint.textContent = context === "report" ? "正在跨报告查找正文、数据与 Charts" : "正在查找最匹配的资料";
      progress.bar.style.width = "24%";
    } else if (elapsedMs < 5500) {
      progress.label.textContent = context === "report" ? "交叉验证" : "整理候选";
      progress.hint.textContent = context === "report" ? "正在对照多份报告并绑定来源" : "正在排序并校验实际候选";
      progress.bar.style.width = "58%";
    } else {
      progress.label.textContent = context === "report" ? "生成研究" : "生成推荐";
      progress.hint.textContent = context === "report" ? "证据已就绪，正在形成综合结论" : "候选已就绪，正在组织答案";
      progress.bar.style.width = "84%";
    }
  }

  function finishProgress(progress, kind, message) {
    progress.label.textContent = message;
    progress.hint.textContent = kind === "success" ? "推荐已更新" : "可以修改问题后再试";
    progress.bar.style.width = kind === "success" ? "100%" : "0%";
    progress.cancel.hidden = true;
    progress.card.setAttribute("data-state", kind);
  }

  function setup(surface) {
    const form = document.getElementById(surface.form);
    const input = document.getElementById(surface.input);
    const status = document.getElementById(surface.status);
    const messages = document.getElementById(surface.messages);
    const recommendations = document.getElementById(surface.recommendations);
    if (!form || !input || !status || !messages || !recommendations) return;
    const history = [];
    const button = form.querySelector("button[type=submit]");
    if (!button) return;
    const idleButtonText = String(button.textContent || "").trim();
    let activeRequest = null;
    let progressCard = null;
    let progressRemovalId = 0;
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
      if (activeRequest) {
        status.textContent = "上一次查找仍在进行，可先取消后再试。";
        return;
      }
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
      if (progressRemovalId) window.clearTimeout(progressRemovalId);
      if (progressCard) progressCard.card.remove();
      progressCard = createProgressCard(form, surface.context);
      const controller = new AbortController();
      const request = { controller, abortReason: "", progress: progressCard };
      activeRequest = request;
      const startedAt = Date.now();
      button.disabled = true;
      button.textContent = "正在查找…";
      button.classList.add("is-loading");
      form.setAttribute("aria-busy", "true");
      status.textContent = "已提交，下方会实时显示查找进度。";
      updateProgress(progressCard, startedAt, surface.context);
      const progressId = window.setInterval(() => updateProgress(progressCard, startedAt, surface.context), 1000);
      progressCard.cancel.addEventListener("click", () => {
        if (activeRequest !== request || request.abortReason) return;
        request.abortReason = "cancelled";
        progressCard.label.textContent = "正在取消…";
        progressCard.hint.textContent = "正在停止本次查找";
        progressCard.cancel.disabled = true;
        controller.abort();
      });
      const timeoutId = window.setTimeout(() => {
        if (activeRequest !== request || request.abortReason) return;
        request.abortReason = "timeout";
        controller.abort();
      }, surface.context === "report" ? RESEARCH_REQUEST_TIMEOUT_MS : CHAT_REQUEST_TIMEOUT_MS);
      try {
        const response = await fetch("/api/report-chat", {
          method: "POST",
          cache: "no-store",
          signal: controller.signal,
          headers: { "Authorization": `Bearer ${auth.token}`, "Content-Type": "application/json" },
          body: JSON.stringify({ question, history, context: surface.context }),
        });
        const data = await response.json().catch(() => ({}));
        if (request.abortReason) throw new DOMException("Aborted", "AbortError");
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
        // Keep the previous answer visible until every part of the new response is ready.
        const researchHtml = surface.context === "report" && (data.mode === "research" || Array.isArray(data.findings) || Array.isArray(data.charts))
          ? researchResultHtml(data)
          : "";
        messages.innerHTML = researchHtml || `<article class="report-chat-answer"><span>AI 推荐</span><p>${escapeHtml(data.answer || "")}</p></article>`;
        const recommendationRows = surface.context === "report" && Array.isArray(data.sources) ? data.sources : data.recommendations;
        recommendations.innerHTML = (Array.isArray(recommendationRows) ? recommendationRows : [])
          .map(recommendationHtml).join("");
        const followUps = Array.isArray(data.follow_up_questions) ? data.follow_up_questions : [];
        status.textContent = followUps.length ? `还可以继续问：${followUps.join("；")}` : `今日还可使用 ${Number(data.usage && data.usage.remaining || 0)} 次。`;
        finishProgress(progressCard, "success", surface.context === "report" && researchHtml ? "研究已生成" : "推荐已生成");
        progressRemovalId = window.setTimeout(() => {
          if (progressCard === request.progress) {
            progressCard.card.remove();
            progressCard = null;
          }
        }, 1200);
      } catch (error) {
        if (request.abortReason === "cancelled") {
          status.textContent = "已取消本次查找，上一次结果仍保留。";
          finishProgress(progressCard, "cancelled", "已取消");
        } else if (request.abortReason === "timeout" || error && error.name === "AbortError") {
          status.textContent = surface.context === "report"
            ? "研究请求超过 60 秒，已停止等待。上一次结果已保留，可点击重试。"
            : "资料 Chat 请求超过 20 秒，已停止等待。上一次结果已保留，可点击重试。";
          finishProgress(progressCard, "timeout", "请求超时");
        } else {
          status.textContent = `${error && error.message || "资料 Chat 暂时不可用。"}；上一次结果已保留，请点击重试。`;
          finishProgress(progressCard, "error", "查找未完成");
        }
      } finally {
        window.clearTimeout(timeoutId);
        window.clearInterval(progressId);
        form.setAttribute("aria-busy", "false");
        button.classList.remove("is-loading");
        button.textContent = idleButtonText;
        button.disabled = false;
        if (activeRequest === request) activeRequest = null;
      }
    });
  }

  const boot = () => surfaces.forEach(setup);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})();
