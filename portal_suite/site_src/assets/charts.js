(() => {
  "use strict";

  const PAGE_SIZE = 24;
  const IMAGE_ID_RE = /^[0-9a-f]{64}$/;
  const VALID_KINDS = new Set(["chart", "table", "data_map", "flow_diagram", "data_visual"]);
  const INVALID_RE = /(?:\b(?:about\s+the\s+author|analyst\s+certification|biograph(?:y|ies)|contents|copyright|disclaimer|important\s+disclosures?|legal\s+notice|table\s+of\s+contents)\b|作者(?:介绍|简介)|分析师(?:介绍|简介|声明)|版权声明|免责声明|法律声明|目录页?|重要声明|风险提示)/i;
  const TYPE_LABELS = {
    bar: "柱状图",
    chart: "图表",
    data_map: "数据地图",
    data_visual: "数据可视化",
    flow: "流程图",
    flow_diagram: "流程图",
    line: "折线图",
    map: "数据地图",
    other: "其他图表",
    scatter: "散点图",
    table: "数据表",
  };

  const elements = {
    results: document.querySelector(".charts-results"),
    gallery: document.getElementById("chartGallery"),
    empty: document.getElementById("chartEmpty"),
    query: document.getElementById("chartQuery"),
    type: document.getElementById("chartTypeFilter"),
    date: document.getElementById("chartDateFilter"),
    clear: document.getElementById("chartClearFilters"),
    more: document.getElementById("chartLoadMore"),
    resultStatus: document.getElementById("chartResultStatus"),
    resultCount: document.getElementById("chartResultCount"),
    itemCount: document.getElementById("chartItemCount"),
    reportCount: document.getElementById("chartReportCount"),
    updatedAt: document.getElementById("chartUpdatedAt"),
  };

  if (!elements.gallery || !elements.query || !elements.type || !elements.date) return;

  const state = {
    rows: [],
    filtered: [],
    visible: PAGE_SIZE,
    workerBase: "/api",
    debounce: 0,
  };

  function clean(value, limit = 1200) {
    return String(value || "").replace(/\0/g, " ").replace(/\s+/g, " ").trim().slice(0, limit);
  }

  function folded(value) {
    return clean(value, 10_000).normalize("NFKC").toLocaleLowerCase("zh-CN");
  }

  function list(value) {
    return Array.isArray(value)
      ? value.map((item) => clean(item, 160)).filter(Boolean).slice(0, 20)
      : [];
  }

  function normalizedKind(chart) {
    const explicit = clean(chart && chart.content_kind, 60).toLowerCase().replace(/[-\s]+/g, "_");
    if (explicit) return explicit;
    const type = clean(chart && chart.chart_type, 60).toLowerCase().replace(/[-\s]+/g, "_");
    if (type === "table") return "table";
    if (type === "map") return "data_map";
    if (["flow", "flowchart", "flow_diagram"].includes(type)) return "flow_diagram";
    return "chart";
  }

  function isValidChart(chart) {
    if (!chart || typeof chart !== "object") return false;
    if (clean(chart.analysis_version, 60) !== "chart-search-v2") return false;
    if (!IMAGE_ID_RE.test(clean(chart.image_id, 80))) return false;
    const kind = normalizedKind(chart);
    if (!VALID_KINDS.has(kind)) return false;
    const score = chart.quality_score === undefined ? 100 : Number(chart.quality_score);
    if (!Number.isFinite(score) || score < 60) return false;
    const title = clean(chart.title, 300);
    const description = clean(chart.description);
    if (!title || !description || INVALID_RE.test(title + " " + description)) return false;
    const evidence = ["metrics", "entities", "periods", "geographies", "units"]
      .reduce((total, field) => total + list(chart[field]).length, 0);
    return evidence > 0;
  }

  function normalizeWorkerBase(value) {
    const configured = clean(value, 500).replace(/\/+$/, "") || "/api";
    try {
      const parsed = new URL(configured, window.location.href);
      if (!["http:", "https:"].includes(parsed.protocol)) return "/api";
    } catch (_error) {
      return "/api";
    }
    return configured;
  }

  function imageUrl(imageId) {
    return state.workerBase + "/charts/image?id=" + encodeURIComponent(imageId);
  }

  function reportSearchUrl(title) {
    const query = clean(title, 300);
    return "/?q=" + encodeURIComponent(query);
  }

  function reportUrl(reportId, preview = {}) {
    const params = new URLSearchParams({ id: String(reportId || "") });
    const previewKeys = [
      "title", "title_zh", "filename", "date_folder", "bank_code", "bank_name",
      "size_bytes", "available", "industry", "sector", "category", "pdf_archived",
      "page_count",
    ];
    previewKeys.forEach((key) => {
      const value = preview[key];
      if (value === undefined || value === null || value === "") return;
      params.set(key, typeof value === "boolean" ? (value ? "1" : "0") : String(value));
    });
    return `report.html?${params.toString()}`;
  }

  function sourceReportUrl(row) {
    return row.reportId
      ? reportUrl(row.reportId, row.reportPreview)
      : reportSearchUrl(row.reportTitle);
  }

  let lightbox = null;
  let lightboxOpener = null;

  function closeChartLightbox() {
    if (!lightbox || lightbox.hidden) return;
    lightbox.hidden = true;
    document.body.classList.remove("chart-lightbox-open");
    const opener = lightboxOpener;
    lightboxOpener = null;
    if (opener && typeof opener.focus === "function") opener.focus();
  }

  function ensureChartLightbox() {
    if (lightbox) return lightbox;
    lightbox = document.createElement("div");
    lightbox.id = "chartLightbox";
    lightbox.className = "chart-lightbox";
    lightbox.hidden = true;
    lightbox.setAttribute("role", "dialog");
    lightbox.setAttribute("aria-modal", "true");
    lightbox.setAttribute("aria-labelledby", "chartLightboxTitle");
    lightbox.setAttribute("aria-describedby", "chartLightboxDescription");

    const panel = document.createElement("section");
    panel.className = "chart-lightbox-panel";
    const header = document.createElement("header");
    header.className = "chart-lightbox-header";
    const heading = document.createElement("div");
    const kicker = document.createElement("span");
    kicker.textContent = "CHART PREVIEW";
    const title = document.createElement("h2");
    title.id = "chartLightboxTitle";
    heading.append(kicker, title);
    const close = document.createElement("button");
    close.type = "button";
    close.className = "chart-lightbox-close";
    close.setAttribute("aria-label", "关闭图表大图");
    close.textContent = "×";
    header.append(heading, close);

    const canvas = document.createElement("div");
    canvas.className = "chart-lightbox-canvas";
    const image = document.createElement("img");
    image.alt = "";
    image.decoding = "async";
    image.referrerPolicy = "no-referrer";
    canvas.append(image);
    const description = document.createElement("p");
    description.id = "chartLightboxDescription";
    description.className = "chart-lightbox-description";
    const source = document.createElement("a");
    source.className = "chart-lightbox-source";
    source.textContent = "查看来源报告 ↗";
    panel.append(header, canvas, description, source);
    lightbox.append(panel);
    document.body.append(lightbox);

    close.addEventListener("click", closeChartLightbox);
    lightbox.addEventListener("click", (event) => {
      if (event.target === lightbox) closeChartLightbox();
    });
    document.addEventListener("keydown", (event) => {
      if (event.key === "Escape" && !lightbox.hidden) closeChartLightbox();
    });
    return lightbox;
  }

  function openChartLightbox(row, opener) {
    const overlay = ensureChartLightbox();
    const image = overlay.querySelector(".chart-lightbox-canvas img");
    const title = overlay.querySelector("#chartLightboxTitle");
    const description = overlay.querySelector("#chartLightboxDescription");
    const source = overlay.querySelector(".chart-lightbox-source");
    image.src = imageUrl(row.imageId);
    image.alt = row.title;
    title.textContent = row.title;
    description.textContent = row.description || row.trend || "";
    description.hidden = !description.textContent;
    source.href = sourceReportUrl(row);
    source.setAttribute("aria-label", "打开来源报告：" + row.reportTitle);
    source.textContent = row.reportId ? "查看来源报告 ↗" : "在首页搜索来源报告 ↗";
    lightboxOpener = opener || null;
    overlay.hidden = false;
    document.body.classList.add("chart-lightbox-open");
    overlay.querySelector(".chart-lightbox-close").focus();
  }

  function dateLabel(value) {
    const digits = clean(value, 16).replace(/\D/g, "");
    if (digits.length === 6) return "20" + digits.slice(0, 2) + "-" + digits.slice(2, 4) + "-" + digits.slice(4, 6);
    if (digits.length === 8) return digits.slice(0, 4) + "-" + digits.slice(4, 6) + "-" + digits.slice(6, 8);
    return clean(value, 16);
  }

  function updatedLabel(value) {
    const timestamp = Date.parse(value);
    if (!Number.isFinite(timestamp)) return "—";
    return new Intl.DateTimeFormat("zh-CN", {
      month: "2-digit",
      day: "2-digit",
      hour: "2-digit",
      minute: "2-digit",
      hour12: false,
    }).format(new Date(timestamp));
  }

  function displayType(row) {
    const type = clean(row.chartType || row.contentKind, 60).toLowerCase();
    return TYPE_LABELS[type] || TYPE_LABELS[row.contentKind] || "图表";
  }

  function searchableText(row) {
    return folded([
      row.title,
      row.description,
      row.trend,
      row.reportTitle,
      row.chartType,
      row.contentKind,
      ...row.metrics,
      ...row.entities,
      ...row.periods,
      ...row.geographies,
      ...row.units,
      ...row.keywords,
    ].join(" "));
  }

  function flattenIndex(payload) {
    const rows = [];
    const reports = Array.isArray(payload && payload.reports) ? payload.reports : [];
    reports.forEach((report) => {
      if (!report || typeof report !== "object") return;
      const reportId = clean(report.report_id, 80);
      const reportTitle = clean(report.title, 300) || "来源报告";
      const dateFolder = clean(report.date_folder, 16);
      const reportPreview = {
        title: reportTitle,
        title_zh: clean(report.title_zh, 300),
        filename: clean(report.filename, 300),
        date_folder: dateFolder,
        bank_code: clean(report.bank_code, 120),
        bank_name: clean(report.bank_name, 120),
        industry: clean(report.industry, 160),
        sector: clean(report.sector, 160),
        category: clean(report.category, 160),
        available: typeof report.available === "boolean" ? report.available : undefined,
        pdf_archived: typeof report.pdf_archived === "boolean" ? report.pdf_archived : undefined,
        size_bytes: report.size_bytes !== undefined && report.size_bytes !== null && report.size_bytes !== ""
          && Number.isFinite(Number(report.size_bytes))
          ? Math.max(0, Number(report.size_bytes))
          : undefined,
        page_count: report.page_count !== undefined && report.page_count !== null && report.page_count !== ""
          && Number.isFinite(Number(report.page_count))
          ? Math.max(0, Number(report.page_count))
          : undefined,
      };
      const charts = Array.isArray(report.charts) ? report.charts : [];
      charts.forEach((chart) => {
        if (!isValidChart(chart)) return;
        const row = {
          id: clean(chart.id, 80),
          analysisVersion: clean(chart.analysis_version, 60),
          imageId: clean(chart.image_id, 80),
          ordinal: Math.max(0, Number(chart.ordinal) || 0),
          title: clean(chart.title, 300),
          contentKind: normalizedKind(chart),
          chartType: clean(chart.chart_type, 60).toLowerCase(),
          description: clean(chart.description),
          trend: clean(chart.trend_summary, 500),
          metrics: list(chart.metrics),
          entities: list(chart.entities),
          periods: list(chart.periods),
          geographies: list(chart.geographies),
          units: list(chart.units),
          keywords: list(chart.keywords),
          reportId,
          reportTitle,
          dateFolder,
          reportPreview,
        };
        row.searchText = searchableText(row);
        rows.push(row);
      });
    });
    rows.sort((left, right) => (
      right.dateFolder.localeCompare(left.dateFolder)
      || left.reportTitle.localeCompare(right.reportTitle, "zh-CN")
      || left.ordinal - right.ordinal
      || left.imageId.localeCompare(right.imageId)
    ));
    return rows;
  }

  function addOption(select, value, label) {
    const option = document.createElement("option");
    option.value = value;
    option.textContent = label;
    select.append(option);
  }

  function populateFilters() {
    const types = new Map();
    const dates = new Set();
    state.rows.forEach((row) => {
      const key = row.chartType || row.contentKind;
      types.set(key, displayType(row));
      if (row.dateFolder) dates.add(row.dateFolder);
    });
    Array.from(types.entries())
      .sort((left, right) => left[1].localeCompare(right[1], "zh-CN"))
      .forEach(([value, label]) => addOption(elements.type, value, label));
    Array.from(dates)
      .sort()
      .reverse()
      .slice(0, 120)
      .forEach((value) => addOption(elements.date, value, dateLabel(value)));
  }

  function chipsFor(row) {
    const seen = new Set();
    return [...row.entities, ...row.metrics, ...row.periods, ...row.geographies, ...row.units]
      .filter((value) => {
        const key = folded(value);
        if (!key || seen.has(key)) return false;
        seen.add(key);
        return true;
      })
      .slice(0, 8);
  }

  function appendTextElement(parent, tag, className, value) {
    if (!value) return null;
    const element = document.createElement(tag);
    if (className) element.className = className;
    element.textContent = value;
    parent.append(element);
    return element;
  }

  function createCard(row) {
    const article = document.createElement("article");
    article.className = "charts-card";
    const media = document.createElement("button");
    media.type = "button";
    media.className = "charts-card-media";
    media.setAttribute("aria-label", "放大图表：" + row.title);
    media.setAttribute("aria-haspopup", "dialog");
    const image = document.createElement("img");
    image.src = imageUrl(row.imageId);
    image.alt = row.title;
    image.loading = "lazy";
    image.decoding = "async";
    image.referrerPolicy = "no-referrer";
    image.addEventListener("error", () => article.classList.add("is-image-error"), { once: true });
    media.append(image);
    appendTextElement(media, "span", "charts-image-fallback", "图表预览暂不可用，识别结果仍可检索。");
    appendTextElement(media, "span", "charts-type", displayType(row));
    appendTextElement(media, "span", "chart-zoom-hint", "放大");
    media.addEventListener("click", () => openChartLightbox(row, media));
    article.append(media);

    const body = document.createElement("div");
    body.className = "charts-card-body";
    appendTextElement(body, "h3", "", row.title);
    appendTextElement(body, "p", "charts-card-summary", row.description);
    if (row.trend && row.trend !== row.description) {
      appendTextElement(body, "p", "charts-card-trend", "趋势：" + row.trend);
    }
    const chipValues = chipsFor(row);
    if (chipValues.length) {
      const chips = document.createElement("div");
      chips.className = "charts-chips";
      chipValues.forEach((value) => appendTextElement(chips, "span", "", value));
      body.append(chips);
    }
    const sourceLabel = (dateLabel(row.dateFolder) || "研报") + " · " + row.reportTitle;
    const link = document.createElement("a");
    link.className = "charts-report-link";
    link.href = sourceReportUrl(row);
    link.setAttribute(
      "aria-label",
      (row.reportId ? "打开来源报告：" : "在首页搜索来源报告：") + row.reportTitle,
    );
    const label = document.createElement("span");
    label.textContent = sourceLabel;
    link.append(label, document.createTextNode("↗"));
    body.append(link);
    article.append(body);
    return article;
  }

  function render() {
    const visibleRows = state.filtered.slice(0, state.visible);
    const fragment = document.createDocumentFragment();
    visibleRows.forEach((row) => fragment.append(createCard(row)));
    elements.gallery.replaceChildren(fragment);
    elements.empty.hidden = state.filtered.length > 0;
    elements.more.hidden = state.visible >= state.filtered.length;
    elements.resultCount.textContent = state.filtered.length ? state.filtered.length.toLocaleString("zh-CN") + " 条" : "";
    elements.resultStatus.textContent = state.filtered.length
      ? "当前显示 " + visibleRows.length.toLocaleString("zh-CN") + " 条经视觉模型复核的有效图表。"
      : "未找到匹配结果。";
    elements.results.setAttribute("aria-busy", "false");
  }

  function applyFilters() {
    const tokens = folded(elements.query.value).split(/\s+/).filter(Boolean);
    const type = elements.type.value;
    const date = elements.date.value;
    state.filtered = state.rows.filter((row) => (
      (!type || row.chartType === type || row.contentKind === type)
      && (!date || row.dateFolder === date)
      && tokens.every((token) => row.searchText.includes(token))
    ));
    state.visible = PAGE_SIZE;
    render();
  }

  async function loadJson(url, fallback) {
    try {
      const response = await fetch(url, { cache: "no-cache" });
      if (!response.ok) return fallback;
      const value = await response.json();
      return value && typeof value === "object" ? value : fallback;
    } catch (_error) {
      return fallback;
    }
  }

  async function start() {
    const [config, payload] = await Promise.all([
      loadJson("data/config.json", {}),
      loadJson("data/chart_search_index.json", null),
    ]);
    state.workerBase = normalizeWorkerBase(config.worker_base_url);
    if (!payload) {
      elements.resultStatus.textContent = "图表索引暂时无法读取，请稍后刷新。";
      elements.empty.hidden = false;
      elements.results.setAttribute("aria-busy", "false");
      return;
    }
    state.rows = flattenIndex(payload);
    state.filtered = state.rows.slice();
    elements.itemCount.textContent = state.rows.length.toLocaleString("zh-CN");
    elements.reportCount.textContent = new Set(state.rows.map((row) => row.reportId || row.reportTitle)).size.toLocaleString("zh-CN");
    elements.updatedAt.textContent = updatedLabel(payload.updated_at_bjt);
    populateFilters();
    render();
  }

  elements.query.addEventListener("input", () => {
    window.clearTimeout(state.debounce);
    state.debounce = window.setTimeout(applyFilters, 140);
  });
  elements.type.addEventListener("change", applyFilters);
  elements.date.addEventListener("change", applyFilters);
  elements.clear.addEventListener("click", () => {
    elements.query.value = "";
    elements.type.value = "";
    elements.date.value = "";
    applyFilters();
    elements.query.focus();
  });
  elements.more.addEventListener("click", () => {
    state.visible += PAGE_SIZE;
    render();
  });

  start();
})();
