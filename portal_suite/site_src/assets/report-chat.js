(() => {
  "use strict";

  const AUTH_SESSION_KEY = "portal_auth_session";
  const CHAT_REQUEST_TIMEOUT_MS = 20 * 1000;
  const RESEARCH_REQUEST_TIMEOUT_MS = 60 * 1000;
  const REQUEST_RESEARCH_TIMEOUT_MS = 20 * 1000;
  const surfaces = [
    {
      context: "report",
      form: "homeChatForm",
      input: "homeChatInput",
      status: "homeChatStatus",
      messages: "homeChatMessages",
      recommendations: "homeChatRecommendations",
      popular: "homeChatPopular",
      popularList: "homeChatPopularList",
    },
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

  function analyticsApi() {
    return window.PortalSuiteAnalytics && typeof window.PortalSuiteAnalytics === "object"
      ? window.PortalSuiteAnalytics
      : null;
  }

  function visitorId() {
    const analytics = analyticsApi();
    if (!analytics || typeof analytics.visitorId !== "function") return "";
    try {
      return String(analytics.visitorId() || "").slice(0, 160);
    } catch (_error) {
      return "";
    }
  }

  function pagePath() {
    return String(window.location && window.location.pathname || "/").slice(0, 240);
  }

  function trackInteraction(action, data = {}) {
    const analytics = analyticsApi();
    if (!analytics || typeof analytics.track !== "function") return;
    const payload = {
      action: String(action || "interaction").slice(0, 80),
      context: String(data.context || "report").slice(0, 24),
    };
    const questionHash = String(data.question_hash || "").replace(/[^a-zA-Z0-9_-]/gu, "").slice(0, 128);
    if (questionHash) payload.question_hash = questionHash;
    for (const key of ["tier", "period", "popular_id", "status", "request_hint"]) {
      const value = String(data[key] || "").trim().slice(0, 120);
      if (value) payload[key] = value;
    }
    for (const key of ["limit", "remaining", "question_length", "item_count"]) {
      if (data[key] === null || data[key] === undefined || data[key] === "") continue;
      const value = Number(data[key]);
      if (Number.isFinite(value)) payload[key] = value;
    }
    try {
      const tracked = analytics.track("report_chat_interaction", payload);
      if (tracked && typeof tracked.catch === "function") tracked.catch(() => {});
    } catch (_error) {
      // Analytics is best effort and must never block research.
    }
  }

  function optionalAuthHeaders(auth, json = false) {
    return {
      ...(json ? { "Content-Type": "application/json" } : {}),
      ...(auth && auth.token ? { "Authorization": `Bearer ${auth.token}` } : {}),
    };
  }

  function responseQuestionHash(data) {
    return String(
      data && data.question_hash
      || data && data.response && data.response.question_hash
      || data && data.usage && data.usage.question_hash
      || "",
    ).replace(/[^a-zA-Z0-9_-]/gu, "").slice(0, 128);
  }

  function usageStatusText(usage) {
    if (!usage || typeof usage !== "object") return "";
    const tier = String(usage.tier || "").trim().toLowerCase();
    if (tier === "public_cache" || tier === "popular_cache") {
      return "热门问题 · 历史精选结果，不计使用次数。";
    }
    const tierLabels = {
      anonymous: "游客",
      visitor: "游客",
      guest: "游客",
      standard: "普通会员",
      basic: "普通会员",
      member: "普通会员",
      standard_member: "普通会员",
      registered: "注册用户",
      advanced: "高阶会员",
      premium: "高阶会员",
      advanced_member: "高阶会员",
      high_tier: "高阶会员",
      admin: "管理员",
    };
    const tierLabel = String(usage.tier_label || tierLabels[tier] || "当前权益").trim();
    const unlimited = usage.unlimited === true || tier === "admin" || usage.limit === null || usage.limit === "unlimited";
    if (unlimited) return `${tierLabel} · 不限次使用。`;
    const limit = usage.limit === null || usage.limit === undefined ? Number.NaN : Number(usage.limit);
    const remaining = usage.remaining === null || usage.remaining === undefined ? Number.NaN : Number(usage.remaining);
    const period = String(usage.period || "daily").trim().toLowerCase();
    const lifetimeLabel = ["anonymous", "visitor", "guest"].includes(tier) ? "当前设备" : "累计";
    const periodLabel = String(usage.period_label || ({
      day: "今日",
      daily: "今日",
      device: "当前设备",
      once: "当前设备",
      lifetime: lifetimeLabel,
    })[period] || "本周期");
    if (Number.isFinite(limit) && Number.isFinite(remaining)) {
      return `${tierLabel} · ${periodLabel}限 ${limit} 次，剩余 ${Math.max(0, remaining)} 次。`;
    }
    if (Number.isFinite(remaining)) return `${tierLabel} · ${periodLabel}剩余 ${Math.max(0, remaining)} 次。`;
    return tierLabel ? `${tierLabel}。` : "";
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

  function reportSearchUrl(title) {
    return `/?q=${encodeURIComponent(String(title || "").trim().slice(0, 300))}`;
  }

  function sourceReportUrl(id, item = {}) {
    return String(id || "").trim()
      ? reportUrl(id, item)
      : reportSearchUrl(item.report_title || item.title);
  }

  let chartLightbox = null;
  let chartLightboxOpener = null;

  function closeChartLightbox() {
    if (!chartLightbox || chartLightbox.hidden) return;
    chartLightbox.hidden = true;
    document.body.classList.remove("chart-lightbox-open");
    const opener = chartLightboxOpener;
    chartLightboxOpener = null;
    if (opener && typeof opener.focus === "function") opener.focus();
  }

  function ensureChartLightbox() {
    if (chartLightbox) return chartLightbox;
    chartLightbox = document.createElement("div");
    chartLightbox.id = "reportResearchChartLightbox";
    chartLightbox.className = "chart-lightbox";
    chartLightbox.hidden = true;
    chartLightbox.setAttribute("role", "dialog");
    chartLightbox.setAttribute("aria-modal", "true");
    chartLightbox.setAttribute("aria-labelledby", "reportResearchChartLightboxTitle");
    chartLightbox.setAttribute("aria-describedby", "reportResearchChartLightboxDescription");
    chartLightbox.innerHTML = `<section class="chart-lightbox-panel">
      <header class="chart-lightbox-header">
        <div><span>CHART EVIDENCE</span><h2 id="reportResearchChartLightboxTitle"></h2></div>
        <button class="chart-lightbox-close" type="button" aria-label="关闭图表大图">×</button>
      </header>
      <div class="chart-lightbox-canvas"><img alt="" decoding="async" referrerpolicy="no-referrer"></div>
      <p class="chart-lightbox-description" id="reportResearchChartLightboxDescription"></p>
      <a class="chart-lightbox-source">查看来源报告 ↗</a>
    </section>`;
    document.body.append(chartLightbox);
    chartLightbox.querySelector(".chart-lightbox-close").addEventListener("click", closeChartLightbox);
    chartLightbox.addEventListener("click", (event) => {
      if (event.target === chartLightbox) closeChartLightbox();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !chartLightbox.hidden) closeChartLightbox();
    });
    return chartLightbox;
  }

  function openChartLightbox(trigger) {
    const overlay = ensureChartLightbox();
    const image = overlay.querySelector(".chart-lightbox-canvas img");
    const title = String(trigger.getAttribute("data-chart-title") || "研究图表");
    const description = String(trigger.getAttribute("data-chart-description") || "");
    const sourceLabel = String(trigger.getAttribute("data-chart-source-label") || "来源报告");
    const sourceUrl = String(trigger.getAttribute("data-chart-source-url") || "/");
    image.src = String(trigger.getAttribute("data-chart-image-src") || "");
    image.alt = title;
    overlay.querySelector("#reportResearchChartLightboxTitle").textContent = title;
    const descriptionElement = overlay.querySelector("#reportResearchChartLightboxDescription");
    descriptionElement.textContent = description;
    descriptionElement.hidden = !description;
    const source = overlay.querySelector(".chart-lightbox-source");
    source.href = sourceUrl;
    source.textContent = `${sourceLabel} ↗`;
    chartLightboxOpener = trigger;
    overlay.hidden = false;
    document.body.classList.add("chart-lightbox-open");
    overlay.querySelector(".chart-lightbox-close").focus();
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

  function chartFigureHtml(item, sources) {
    const imageId = String(item.image_id || "");
    const reportId = String(item.report_id || "").trim();
    const chartReportTitle = String(item.report_title || "").trim();
    const report = sources.get(reportId) || {
      id: reportId,
      title: chartReportTitle || "图表所在报告",
      report_title: chartReportTitle || "图表所在报告",
      date_folder: String(item.date_folder || "").trim(),
    };
    const reportTitle = String(report.report_title || report.title || chartReportTitle || "图表所在报告").trim();
    const sourceUrl = sourceReportUrl(reportId, report);
    const sourceAction = reportId ? `来源报告 · ${reportTitle}` : `搜索来源报告 · ${reportTitle}`;
    const title = String(item.title || "研究图表").trim();
    const description = String(item.description || item.trend_summary || "").trim();
    const metrics = (Array.isArray(item.metrics) ? item.metrics : [])
      .map((value) => String(value || "").trim()).filter(Boolean).slice(0, 5).join(" · ");
    const imageSrc = `/api/charts/image?id=${imageId}`;
    return `<figure class="report-research-chart">
      <button class="report-research-chart-media" type="button" aria-label="放大图表：${escapeHtml(title)}" aria-haspopup="dialog"
        data-chart-lightbox data-chart-image-src="${escapeHtml(imageSrc)}" data-chart-title="${escapeHtml(title)}"
        data-chart-description="${escapeHtml(description)}" data-chart-source-url="${escapeHtml(sourceUrl)}"
        data-chart-source-label="${escapeHtml(sourceAction)}">
        <img src="${escapeHtml(imageSrc)}" alt="${escapeHtml(title)}" loading="lazy" decoding="async" referrerpolicy="no-referrer">
        <span class="chart-zoom-hint" aria-hidden="true">放大</span>
      </button>
      <figcaption><strong>${escapeHtml(title)}</strong>${description ? `<p>${escapeHtml(description)}</p>` : ""}${metrics ? `<span>${escapeHtml(metrics)}</span>` : ""}<a href="${escapeHtml(sourceUrl)}" target="_blank" rel="noopener noreferrer">${escapeHtml(sourceAction)}</a></figcaption>
    </figure>`;
  }

  function chartsByFinding(findings, charts, sources) {
    const grouped = findings.map(() => []);
    if (!grouped.length) return grouped;
    const findingSources = findings.map((item) => new Set(sourceIds(item.source_ids, sources)));
    charts.forEach((chart, chartIndex) => {
      const reportId = String(chart.report_id || "").trim();
      let findingIndex = reportId
        ? findingSources.findIndex((ids) => ids.has(reportId))
        : -1;
      if (findingIndex < 0) {
        findingIndex = grouped.reduce((best, rows, index) => (
          rows.length < grouped[best].length ? index : best
        ), chartIndex % grouped.length);
      }
      grouped[findingIndex].push(chart);
    });
    return grouped;
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
      return Boolean(String(item.report_id || item.report_title || "").trim());
    }).slice(0, 6);
    const findingCharts = chartsByFinding(findings, charts, sources);
    const sections = [];
    if (executiveSummary) {
      sections.push(`<section class="report-research-summary"><span>研究摘要</span><p>${escapeHtml(executiveSummary)}</p><div class="report-research-source-row">${sourceChipsHtml(data.summary_source_ids, sources)}</div></section>`);
    }
    if (findings.length) {
      sections.push(`<section class="report-research-section"><h3>主要发现</h3><div class="report-research-findings">${findings.map((item, index) => {
        const title = String(item.title || "核心发现").trim();
        const summary = String(item.summary || item.analysis || "").trim();
        const inlineCharts = findingCharts[index] || [];
        return `<article class="report-research-finding"><div class="report-research-finding-copy"><strong>${escapeHtml(title)}</strong><p>${escapeHtml(summary)}</p><div class="report-research-source-row">${sourceChipsHtml(item.source_ids, sources)}</div></div>${inlineCharts.length ? `<div class="report-research-inline-charts" aria-label="图表证据"><h4>图表证据</h4>${inlineCharts.map((chart) => chartFigureHtml(chart, sources)).join("")}</div>` : ""}</article>`;
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
    if (charts.length && !findings.length) {
      sections.push(`<section class="report-research-section"><h3>图表证据</h3><div class="report-research-chart-grid">${charts.map((item) => chartFigureHtml(item, sources)).join("")}</div></section>`);
    }
    return sections.join("");
  }

  function usageAnalyticsData(usage) {
    if (!usage || typeof usage !== "object") return {};
    return {
      tier: usage.tier,
      period: usage.period,
      limit: usage.limit,
      remaining: usage.remaining,
    };
  }

  function paintResponse(data, surface, messages, recommendations) {
    const researchHtml = surface.context === "report" && (
      data.mode === "research"
      || Array.isArray(data.findings)
      || Array.isArray(data.charts)
      || Array.isArray(data.data_points)
    ) ? researchResultHtml(data) : "";
    messages.innerHTML = researchHtml || `<article class="report-chat-answer"><span>AI 推荐</span><p>${escapeHtml(data.answer || "")}</p></article>`;
    const recommendationRows = surface.context === "report" && Array.isArray(data.sources)
      ? data.sources
      : data.recommendations;
    recommendations.innerHTML = (Array.isArray(recommendationRows) ? recommendationRows : [])
      .map(recommendationHtml).join("");
    return researchHtml;
  }

  function popularRows(data) {
    const rows = Array.isArray(data)
      ? data
      : Array.isArray(data && data.items)
        ? data.items
        : Array.isArray(data && data.popular_questions)
          ? data.popular_questions
          : Array.isArray(data && data.questions) ? data.questions : [];
    return rows.filter((item) => item && typeof item === "object"
      && String(item.id || "").trim()
      && String(item.question || item.title || "").trim()).slice(0, 12);
  }

  function popularResponse(data) {
    if (!data || typeof data !== "object") return {};
    return data.response && typeof data.response === "object"
      ? data.response
      : data.research && typeof data.research === "object"
        ? data.research
        : data.result && typeof data.result === "object"
          ? data.result
          : data.item && typeof data.item === "object" ? data.item : data;
  }

  function popularListHtml(rows) {
    return rows.map((item, index) => {
      const question = String(item.question || item.title || "").trim();
      return `<button class="report-chat-popular-question" type="button" data-popular-id="${escapeHtml(item.id)}" aria-label="查看热门研究：${escapeHtml(question)}">
        <span>${String(index + 1).padStart(2, "0")}</span><strong>${escapeHtml(question)}</strong><em>查看研究 →</em>
      </button>`;
    }).join("");
  }

  function limitRequestHtml(auth, usage) {
    const accountEmail = auth && auth.user ? String(auth.user.email || "").trim() : "";
    const emailHelp = accountEmail ? "将发送至当前登录账号邮箱" : "请填写接收后续回复的邮箱";
    return `<article class="report-chat-limit-card">
      <div class="report-chat-limit-copy"><span>本次额度已用完</span><h3>申请继续研究</h3><p>${escapeHtml(usageStatusText(usage) || "提交后，研究问题会通过邮件转交人工继续处理。")}</p></div>
      <form class="report-chat-limit-form" data-report-chat-request>
        <label><span>联系邮箱</span><input type="email" name="requester_email" value="${escapeHtml(accountEmail)}" placeholder="name@example.com" autocomplete="email" required${accountEmail ? " readonly" : ""}></label>
        <label class="report-chat-honeypot" aria-hidden="true">请勿填写<input type="text" name="honeypot" tabindex="-1" autocomplete="off"></label>
        <div class="report-chat-limit-actions"><button class="primary" type="submit">申请继续研究</button><button class="secondary-button" type="button" data-report-chat-request-dismiss>取消</button></div>
        <p class="report-chat-limit-help">${escapeHtml(emailHelp)}</p>
        <p class="status-line" data-report-chat-request-status role="status" aria-live="polite"></p>
      </form>
    </article>`;
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
    progress.hint.textContent = ({
      success: "推荐已更新",
      limit: "可以提交邮件申请继续研究",
      cancelled: "本次请求已停止",
      timeout: "可以点击重试",
      error: "可以修改问题后再试",
    })[kind] || "可以修改问题后再试";
    progress.bar.style.width = kind === "success" || kind === "limit" ? "100%" : "0%";
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
    const popular = surface.popular ? document.getElementById(surface.popular) : null;
    const popularList = surface.popularList ? document.getElementById(surface.popularList) : null;
    const history = [];
    const button = form.querySelector("button[type=submit]");
    if (!button) return;
    const idleButtonText = String(button.textContent || "").trim();
    let activeRequest = null;
    let activePopularRequest = null;
    let activeLimitRequest = null;
    let limitedQuestion = "";
    let limitedQuestionHash = "";
    let limitedArchiveId = "";
    let popularItems = new Map();
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
    messages.addEventListener("click", (event) => {
      const trigger = event.target.closest("[data-chart-lightbox]");
      if (trigger) {
        openChartLightbox(trigger);
        return;
      }
      const dismiss = event.target.closest("[data-report-chat-request-dismiss]");
      if (!dismiss) return;
      event.preventDefault();
      const requestForm = dismiss.closest("[data-report-chat-request]");
      if (activeLimitRequest && activeLimitRequest.form === requestForm) {
        activeLimitRequest.abortReason = "cancelled";
        activeLimitRequest.controller.abort();
        return;
      }
      requestForm?.closest(".report-chat-limit-card")?.remove();
      trackInteraction("limit_request_cancel", { context: surface.context, question_hash: limitedQuestionHash });
    });
    messages.addEventListener("submit", async (event) => {
      const requestForm = event.target.closest("[data-report-chat-request]");
      if (!requestForm) return;
      event.preventDefault();
      if (activeLimitRequest || !limitedQuestion) return;
      const emailInput = requestForm.querySelector("[name=requester_email]");
      const honeypotInput = requestForm.querySelector("[name=honeypot]");
      const requestStatus = requestForm.querySelector("[data-report-chat-request-status]");
      const requestButton = requestForm.querySelector("button[type=submit]");
      const requesterEmail = String(emailInput && emailInput.value || "").trim().slice(0, 254);
      if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/u.test(requesterEmail)) {
        requestStatus.textContent = "请填写有效的联系邮箱。";
        trackInteraction("limit_request_error", { context: surface.context, question_hash: limitedQuestionHash, status: "validation" });
        return;
      }
      const auth = session();
      const controller = new AbortController();
      const request = { abortReason: "", controller, form: requestForm };
      activeLimitRequest = request;
      requestButton.disabled = true;
      requestButton.textContent = "正在提交…";
      requestForm.setAttribute("aria-busy", "true");
      requestStatus.textContent = "正在把研究申请发送给 KCDesk。";
      trackInteraction("limit_request_submit", { context: surface.context, question_hash: limitedQuestionHash });
      const timeoutId = window.setTimeout(() => {
        if (activeLimitRequest !== request || request.abortReason) return;
        request.abortReason = "timeout";
        controller.abort();
      }, REQUEST_RESEARCH_TIMEOUT_MS);
      try {
        const response = await fetch("/api/report-chat/request", {
          method: "POST",
          cache: "no-store",
          signal: controller.signal,
          headers: optionalAuthHeaders(auth, true),
          body: JSON.stringify({
            archive_id: limitedArchiveId,
            question: limitedQuestion,
            requester_email: requesterEmail,
            visitor_id: visitorId(),
            page_path: pagePath(),
            honeypot: String(honeypotInput && honeypotInput.value || "").slice(0, 160),
          }),
        });
        const data = await response.json().catch(() => ({}));
        if (request.abortReason) throw new DOMException("Aborted", "AbortError");
        if (!response.ok) throw new Error(String(data.detail || "申请暂时未能发送，请稍后重试。"));
        const duplicate = String(data.status || "").toLowerCase() === "duplicate";
        requestStatus.textContent = duplicate
          ? "这条申请已经收到，无需重复提交。"
          : "申请已发送。KCDesk 会通过邮件继续处理。";
        requestButton.textContent = duplicate ? "已收到" : "已发送";
        trackInteraction("limit_request_success", {
          context: surface.context,
          question_hash: limitedQuestionHash || responseQuestionHash(data),
          status: duplicate ? "duplicate" : "sent",
        });
      } catch (error) {
        if (request.abortReason === "cancelled") {
          requestStatus.textContent = "已取消本次申请。";
          trackInteraction("limit_request_cancel", { context: surface.context, question_hash: limitedQuestionHash });
        } else if (request.abortReason === "timeout" || error && error.name === "AbortError") {
          requestStatus.textContent = "申请提交超过 20 秒，已停止等待，请重试。";
          trackInteraction("limit_request_timeout", { context: surface.context, question_hash: limitedQuestionHash });
        } else {
          requestStatus.textContent = `${error && error.message || "申请暂时未能发送。"} 请稍后重试。`;
          trackInteraction("limit_request_error", { context: surface.context, question_hash: limitedQuestionHash, status: "request_failed" });
        }
      } finally {
        window.clearTimeout(timeoutId);
        requestForm.setAttribute("aria-busy", "false");
        if (activeLimitRequest === request) activeLimitRequest = null;
        if (!requestButton.textContent.includes("已")) requestButton.textContent = "申请继续研究";
        if (!requestButton.textContent.includes("已")) requestButton.disabled = false;
      }
    });

    if (popular && popularList) {
      popularList.addEventListener("click", async (event) => {
        const popularButton = event.target.closest("[data-popular-id]");
        if (!popularButton || activeRequest || activePopularRequest) return;
        const popularId = String(popularButton.getAttribute("data-popular-id") || "").trim();
        const popularItem = popularItems.get(popularId);
        if (!popularId || !popularItem) return;
        const question = String(popularItem.question || popularItem.title || "").trim();
        const knownQuestionHash = responseQuestionHash(popularItem);
        trackInteraction("popular_click", {
          context: surface.context,
          popular_id: popularId,
          question_hash: knownQuestionHash,
        });
        input.value = question;
        popularButton.disabled = true;
        popularList.setAttribute("aria-busy", "true");
        status.textContent = "正在载入已生成的热门研究…";
        const request = {};
        activePopularRequest = request;
        try {
          const response = await fetch(`/api/report-chat/popular?id=${encodeURIComponent(popularId)}`, {
            method: "GET",
            cache: "no-store",
            headers: optionalAuthHeaders(session()),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(String(data.detail || "热门研究暂时无法载入。"));
          const cachedResearch = popularResponse(data);
          paintResponse(cachedResearch, surface, messages, recommendations);
          history.push(
            { role: "user", content: question },
            { role: "assistant", content: String(cachedResearch.answer || cachedResearch.executive_summary || "") },
          );
          while (history.length > 6) history.shift();
          status.textContent = "热门研究已载入，不消耗本次生成额度。";
          trackInteraction("popular_success", {
            context: surface.context,
            popular_id: popularId,
            question_hash: responseQuestionHash(data) || knownQuestionHash,
            status: data.cached === false ? "fresh" : "cached",
          });
          messages.scrollIntoView?.({ behavior: "smooth", block: "start" });
        } catch (_error) {
          status.textContent = "热门研究暂时无法载入，请稍后重试。";
          trackInteraction("popular_error", {
            context: surface.context,
            popular_id: popularId,
            question_hash: knownQuestionHash,
          });
        } finally {
          if (activePopularRequest === request) activePopularRequest = null;
          popularList.setAttribute("aria-busy", "false");
          popularButton.disabled = false;
        }
      });
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (activeRequest || activePopularRequest) {
        status.textContent = activeRequest
          ? "上一次查找仍在进行，可先取消后再试。"
          : "热门研究仍在载入，请稍候。";
        return;
      }
      const question = String(input.value || "").trim();
      if (question.length < 2) {
        status.textContent = "请输入公司、行业、主题、岗位或指标。";
        return;
      }
      const auth = session();
      if (!auth && surface.context === "course") {
        status.textContent = "请先点击右上角注册 / 登录，再使用资料 Chat。";
        document.getElementById("accountGate")?.click();
        return;
      }
      trackInteraction("submit", { context: surface.context, question_length: question.length });
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
      let responseMeta = {};
      try {
        const response = await fetch("/api/report-chat", {
          method: "POST",
          cache: "no-store",
          signal: controller.signal,
          headers: optionalAuthHeaders(auth, true),
          body: JSON.stringify({ question, history, context: surface.context, visitor_id: visitorId() }),
        });
        const data = await response.json().catch(() => ({}));
        responseMeta = {
          status: String(response.status || ""),
          request_hint: data.request_hint,
          question_hash: responseQuestionHash(data),
          ...usageAnalyticsData(data.usage),
        };
        if (request.abortReason) throw new DOMException("Aborted", "AbortError");
        if (response.status === 429 && surface.context === "report") {
          limitedQuestion = question;
          limitedQuestionHash = responseQuestionHash(data);
          limitedArchiveId = String(data.archive_id || "").trim().slice(0, 160);
          const previousMessages = String(messages.innerHTML || "")
            .replace(/<article class="report-chat-limit-card">[\s\S]*$/u, "");
          messages.innerHTML = `${previousMessages}${limitRequestHtml(auth, data.usage)}`;
          const usageText = usageStatusText(data.usage);
          status.textContent = `${usageText ? `${usageText} ` : ""}如需继续，可提交下方邮件申请。`;
          trackInteraction("limit_reached", { context: surface.context, ...responseMeta });
          finishProgress(progressCard, "limit", "本周期额度已用完");
          progressRemovalId = window.setTimeout(() => {
            if (progressCard === request.progress) {
              progressCard.card.remove();
              progressCard = null;
            }
          }, 1200);
          return;
        }
        if (!response.ok) {
          const detail = String(data.detail || "资料 Chat 请求失败，请稍后点击重试。");
          const stage = String(data.stage_code || "").replace(/[^A-Z0-9_-]/g, "").slice(0, 32);
          const hint = String(data.request_hint || "").replace(/[^A-Z0-9-]/gi, "").slice(0, 16);
          const diagnostics = [`HTTP ${response.status}`];
          if (stage) diagnostics.push(stage);
          if (hint) diagnostics.push(`请求 ${hint}`);
          throw new Error(`${detail}（${diagnostics.join(" · ")}）`);
        }
        history.push({ role: "user", content: question }, { role: "assistant", content: data.answer || data.executive_summary || "" });
        while (history.length > 6) history.shift();
        // Keep the previous answer visible until every part of the new response is ready.
        const researchHtml = paintResponse(data, surface, messages, recommendations);
        const followUps = Array.isArray(data.follow_up_questions) ? data.follow_up_questions : [];
        const statusParts = [usageStatusText(data.usage)];
        if (followUps.length) statusParts.push(`还可以继续问：${followUps.join("；")}`);
        status.textContent = statusParts.filter(Boolean).join(" ") || "研究已生成。";
        trackInteraction("success", { context: surface.context, ...responseMeta });
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
          trackInteraction("cancel", { context: surface.context, ...responseMeta });
          finishProgress(progressCard, "cancelled", "已取消");
        } else if (request.abortReason === "timeout" || error && error.name === "AbortError") {
          status.textContent = surface.context === "report"
            ? "研究请求超过 60 秒，已停止等待。上一次结果已保留，可点击重试。"
            : "资料 Chat 请求超过 20 秒，已停止等待。上一次结果已保留，可点击重试。";
          trackInteraction("timeout", { context: surface.context, ...responseMeta });
          finishProgress(progressCard, "timeout", "请求超时");
        } else {
          status.textContent = `${error && error.message || "资料 Chat 暂时不可用。"}；上一次结果已保留，请点击重试。`;
          trackInteraction("error", { context: surface.context, ...responseMeta });
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

    if (popular && popularList) {
      fetch("/api/report-chat/popular", {
        method: "GET",
        cache: "no-store",
        headers: optionalAuthHeaders(session()),
      }).then(async (response) => {
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error("popular_unavailable");
        const rows = popularRows(data);
        if (!rows.length) return;
        popularItems = new Map(rows.map((item) => [String(item.id).trim(), item]));
        popularList.innerHTML = popularListHtml(rows);
        popular.hidden = false;
        rows.forEach((item) => trackInteraction("popular_impression", {
          context: surface.context,
          popular_id: item.id,
          question_hash: responseQuestionHash(item),
          item_count: rows.length,
        }));
      }).catch(() => {
        popular.hidden = true;
        trackInteraction("popular_error", { context: surface.context, status: "list_unavailable" });
      });
    }
  }

  const boot = () => surfaces.forEach(setup);
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", boot, { once: true });
  else boot();
})();
