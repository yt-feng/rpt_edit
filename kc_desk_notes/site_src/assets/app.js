(function () {
  const page = document.body.dataset.page;
  const CONTACT_WECHAT = "macroGate";
  const ADMIN_TOKEN_KEY = "kcdesk_admin_token";
  const ADMIN_COOKIE_NAME = "kcdesk_admin_token";
  const ADMIN_COOKIE_MAX_AGE = 180 * 24 * 60 * 60;

  const INDUSTRY_RULES = [
    ["Macro / FX / Rates", /\b(macro|fx|foreign exchange|currency|cny|yuan|dollar|usd|rate|rates|yield|fed|ecb|boj|inflation|cpi|pmi|gdp|economy|economic|recession|treasury|bond|nominal|real rate)\b/],
    ["Equity Strategy", /\b(strategy|equity strategy|market strategy|asset allocation|portfolio|index|earnings revision|valuation|eps|target price)\b/],
    ["Tech / AI / Semis", /\b(ai|artificial intelligence|semiconductor|semis|chip|chips|memory|dram|nand|hbm|gpu|server|software|cloud|data center|datacenter|robot|robotics)\b/],
    ["Internet / Media", /\b(internet|media|gaming|game|music|streaming|advertising|ecommerce|e-commerce|platform|social|takeaway|food delivery|new media)\b/],
    ["Autos / EV / Batteries", /\b(auto|autos|automotive|vehicle|ev|bev|battery|batteries|lithium|ess|adas|mobility|tesla|byd)\b/],
    ["Energy / Utilities", /\b(energy|oil|gas|lng|solar|wind|power|utility|utilities|renewable|coal|electricity|grid)\b/],
    ["Metals / Mining", /\b(metal|metals|mining|copper|aluminum|aluminium|steel|iron ore|gold|silver|nickel|commodity|commodities)\b/],
    ["Healthcare / Biotech", /\b(healthcare|health care|biotech|pharma|pharmaceutical|drug|medical|hospital|medtech|vaccine|therapy)\b/],
    ["Consumer / Retail", /\b(consumer|retail|apparel|luxury|brand|restaurant|food|beverage|travel retail|staples|discretionary)\b/],
    ["Banks / Financials", /\b(bank|banks|banking|insurance|broker|brokerage|asset manager|fintech|exchange|financials|payment)\b/],
    ["Real Estate", /\b(real estate|property|housing|developer|reit|mortgage|homebuilder|construction)\b/],
    ["Industrials / Capex", /\b(industrial|industrials|machinery|automation|capex|capital goods|aerospace|defense|rail|shipping|logistics|transport)\b/],
    ["Policy / Geopolitics", /\b(policy|politics|geopolitic|geopolitical|tariff|trade war|election|sanction|iran|russia|taiwan|strait|security)\b/],
    ["ESG / Climate", /\b(esg|climate|carbon|decarbon|emission|sustainable|sustainability|green|transition)\b/],
  ];

  const STOPWORDS = new Set([
    "the", "and", "for", "with", "from", "this", "that", "into", "after", "before", "report", "reports",
    "global", "china", "asia", "update", "updates", "note", "notes", "research", "sector", "market",
    "markets", "equity", "earnings", "preview", "review", "takeaways", "anchor", "model", "projection",
    "slightly", "likely", "better", "pricing", "daily", "weekly", "monthly", "nom", "jpm", "ubs", "citi",
    "bofa", "barc", "jef", "jpmorgan", "morgan", "stanley", "goldman", "sachs", "nomura",
  ]);

  function escapeHtml(value) {
    return String(value || "")
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;");
  }

  function normalize(value) {
    return String(value || "")
      .normalize("NFKC")
      .toLowerCase()
      .replace(/[^\p{L}\p{N}]+/gu, " ")
      .replace(/\s+/g, " ")
      .trim();
  }

  function queryTokens(value) {
    return normalize(value).split(" ").filter(Boolean);
  }

  function textMatches(text, query) {
    if (!query) return true;
    if (text.includes(query)) return true;
    const tokens = query.split(" ").filter(Boolean);
    return tokens.length > 0 && tokens.every((token) => text.includes(token));
  }

  function scoreText(text, query, weight) {
    if (!query) return 0;
    let score = 0;
    if (text.includes(query)) score += 10 * weight;
    for (const token of query.split(" ").filter(Boolean)) {
      if (text.includes(token)) score += weight;
    }
    return score;
  }

  async function loadJson(path) {
    const response = await fetch(path, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Could not load ${path}: ${response.status}`);
    }
    return response.json();
  }

  async function loadOptionalJson(path, fallback) {
    try {
      return await loadJson(path);
    } catch (error) {
      console.warn(error);
      return fallback;
    }
  }

  function getCookie(name) {
    const prefix = `${name}=`;
    return document.cookie
      .split(";")
      .map((part) => part.trim())
      .find((part) => part.startsWith(prefix))
      ?.slice(prefix.length) || "";
  }

  function setCookie(name, value, maxAge) {
    document.cookie = `${name}=${encodeURIComponent(value)}; Max-Age=${maxAge}; Path=/; SameSite=Lax; Secure`;
  }

  function clearCookie(name) {
    document.cookie = `${name}=; Max-Age=0; Path=/; SameSite=Lax; Secure`;
  }

  function getAdminToken() {
    try {
      const stored = localStorage.getItem(ADMIN_TOKEN_KEY);
      if (stored) {
        const data = JSON.parse(stored);
        if (!data.expiresAt || Date.parse(data.expiresAt) > Date.now()) return data.token || "";
      }
    } catch (_error) {
      // Fall back to the cookie below.
    }
    return decodeURIComponent(getCookie(ADMIN_COOKIE_NAME) || "");
  }

  function setAdminToken(token, expiresAt) {
    const value = String(token || "");
    if (!value) return;
    try {
      localStorage.setItem(ADMIN_TOKEN_KEY, JSON.stringify({ token: value, expiresAt: expiresAt || "" }));
    } catch (_error) {
      // Cookie still keeps the device remembered.
    }
    setCookie(ADMIN_COOKIE_NAME, value, ADMIN_COOKIE_MAX_AGE);
    document.dispatchEvent(new CustomEvent("kcdesk-admin-change"));
  }

  function clearAdminToken() {
    try {
      localStorage.removeItem(ADMIN_TOKEN_KEY);
    } catch (_error) {
      // Ignore localStorage access errors.
    }
    clearCookie(ADMIN_COOKIE_NAME);
    document.dispatchEvent(new CustomEvent("kcdesk-admin-change"));
  }

  function workerBaseUrl(config) {
    return String((config && config.worker_base_url) || "").replace(/\/$/, "");
  }

  function adminModalMarkup() {
    return `
      <div class="admin-modal" id="adminModal" role="dialog" aria-modal="true" aria-labelledby="adminModalTitle">
        <div class="admin-dialog">
          <button class="admin-close" id="adminClose" type="button" aria-label="Close">&times;</button>
          <h3 id="adminModalTitle">Private tools</h3>
          <form id="adminLoginForm">
            <label class="search-box">
              <span>Key</span>
              <input id="adminKeyInput" type="password" autocomplete="current-password" required>
            </label>
            <button class="primary" type="submit">Unlock</button>
            <div id="adminLoginStatus" class="status-line" aria-live="polite"></div>
          </form>
        </div>
      </div>
    `;
  }

  function showAdminLogin(workerUrl) {
    if (!workerUrl) {
      window.alert("Private tools are not configured.");
      return Promise.resolve("");
    }

    const existing = document.getElementById("adminModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", adminModalMarkup());

    const modal = document.getElementById("adminModal");
    const form = document.getElementById("adminLoginForm");
    const input = document.getElementById("adminKeyInput");
    const status = document.getElementById("adminLoginStatus");
    const close = document.getElementById("adminClose");
    const button = form.querySelector("button");
    input.focus();

    return new Promise((resolve) => {
      function finish(token) {
        modal.remove();
        resolve(token || "");
      }

      close.addEventListener("click", () => finish(""));
      modal.addEventListener("click", (event) => {
        if (event.target === modal) finish("");
      });
      form.addEventListener("submit", async (event) => {
        event.preventDefault();
        button.disabled = true;
        status.className = "status-line";
        status.textContent = "Checking...";
        try {
          const response = await fetch(`${workerUrl}/admin/login`, {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ key: input.value }),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok) throw new Error(data.error || "Private key is incorrect.");
          setAdminToken(data.token, data.expires_at);
          finish(data.token);
        } catch (error) {
          status.textContent = error.message || "Unlock failed.";
          status.classList.add("error");
        } finally {
          button.disabled = false;
        }
      });
    });
  }

  function initAdminGate(workerUrl) {
    const gate = document.getElementById("adminGate");
    if (!gate) return;
    function update() {
      gate.classList.toggle("is-unlocked", Boolean(getAdminToken()));
    }
    update();
    document.addEventListener("kcdesk-admin-change", update);
    gate.addEventListener("click", () => {
      showAdminLogin(workerUrl);
    });
  }

  function formatSize(bytes) {
    const size = Number(bytes || 0);
    if (!size) return "";
    if (size >= 1024 * 1024 * 1024) return `${(size / 1024 / 1024 / 1024).toFixed(1)} GB`;
    if (size >= 1024 * 1024) return `${(size / 1024 / 1024).toFixed(1)} MB`;
    if (size >= 1024) return `${Math.round(size / 1024)} KB`;
    return `${size} B`;
  }

  function isoDateFromValue(value) {
    const text = String(value || "");
    if (/^\d{6}$/.test(text)) {
      return `20${text.slice(0, 2)}-${text.slice(2, 4)}-${text.slice(4, 6)}`;
    }
    if (/^\d{8}$/.test(text)) {
      return `${text.slice(0, 4)}-${text.slice(4, 6)}-${text.slice(6, 8)}`;
    }
    const iso = text.match(/^(\d{4})-(\d{2})-(\d{2})/);
    return iso ? `${iso[1]}-${iso[2]}-${iso[3]}` : "";
  }

  function displayDate(value) {
    return isoDateFromValue(value) || String(value || "") || "-";
  }

  function itemDate(item) {
    return isoDateFromValue(item.date_folder) || isoDateFromValue(item.client_modified) || "";
  }

  function dateSortValue(item) {
    return Number(itemDate(item).replace(/-/g, "")) || 0;
  }

  function bankKey(item) {
    return String(item.bank_code || item.bank_name || "Other").trim() || "Other";
  }

  function bankLabel(item) {
    const code = String(item.bank_code || "").trim();
    const name = String(item.bank_name || "").trim();
    if (code && name && normalize(code) !== normalize(name)) return `${code} · ${name}`;
    return code || name || "Other";
  }

  function titleText(item) {
    return String(item.title || item.filename || "Untitled report").trim() || "Untitled report";
  }

  function titleZhText(item) {
    return String(item.title_zh || "").trim();
  }

  function inferIndustry(item) {
    const explicit = item.industry || item.sector || item.category;
    if (explicit) return String(explicit);
    const text = normalize([item.title, item.title_zh, item.filename].join(" "));
    for (const [label, pattern] of INDUSTRY_RULES) {
      if (pattern.test(text)) return label;
    }
    return "Other";
  }

  function isPdfAvailable(item) {
    return item.available !== false;
  }

  function metadataText(item) {
    return normalize([
      item.title,
      item.title_zh,
      item.filename,
      item.bank_code,
      item.bank_name,
      inferIndustry(item),
      item.date_folder,
      (item.date_folders || []).join(" "),
      item.client_modified,
      item.server_modified,
    ].join(" "));
  }

  function selectedSearchText(item, queryScope, metadataById, searchTextById) {
    const title = normalize([item.title, item.title_zh, item.filename].join(" "));
    const catalog = metadataById.get(item.id) || "";
    const fullText = searchTextById.get(item.id) || "";
    if (queryScope === "title") return { title, catalog: "", fullText: "", combined: title };
    if (queryScope === "catalog") return { title: "", catalog, fullText: "", combined: catalog };
    if (queryScope === "fulltext") return { title: "", catalog: "", fullText, combined: fullText };
    return { title, catalog, fullText, combined: `${title} ${catalog} ${fullText}` };
  }

  function scoreItem(item, query, queryScope, metadataById, searchTextById) {
    if (!query) return 0;
    const selected = selectedSearchText(item, queryScope, metadataById, searchTextById);
    if (!textMatches(selected.combined, query)) return -1;
    return (
      scoreText(selected.title, query, 12) +
      scoreText(selected.catalog, query, 5) +
      scoreText(selected.fullText, query, 2)
    );
  }

  function resultRow(item) {
    const bank = item.bank_code || item.bank_name || "Other";
    const size = formatSize(item.size_bytes);
    const industry = inferIndustry(item);
    const available = isPdfAvailable(item);
    const status = available ? size : "Text only";
    const zh = titleZhText(item);
    return `
      <button class="report-row report-link${available ? "" : " is-archived"}" type="button" data-id="${escapeHtml(item.id)}">
        <span class="pill">${escapeHtml(bank)}</span>
        <span class="date-text">${escapeHtml(displayDate(item.date_folder))}</span>
        <span class="title-text">
          <span class="title-en">${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="industry-text">${escapeHtml(industry)}</span>
        <span class="size-text${available ? "" : " archived"}">${escapeHtml(status)}</span>
      </button>
    `;
  }

  function relatedRow(item) {
    const available = isPdfAvailable(item);
    const zh = titleZhText(item);
    return `
      <button class="related-row report-link${available ? "" : " is-archived"}" type="button" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(bankLabel(item))} · ${escapeHtml(displayDate(item.date_folder))} · ${escapeHtml(inferIndustry(item))}${available ? "" : " · Text only"}</span>
      </button>
    `;
  }

  function setOptions(select, options, allLabel) {
    const current = select.value;
    const rows = [`<option value="">${escapeHtml(allLabel)}</option>`];
    for (const option of options) {
      rows.push(`<option value="${escapeHtml(option.value)}">${escapeHtml(option.label)}</option>`);
    }
    select.innerHTML = rows.join("");
    if ([...select.options].some((option) => option.value === current)) {
      select.value = current;
    }
  }

  function optionSummary(map) {
    return [...map.entries()]
      .sort((a, b) => a[0].localeCompare(b[0]))
      .map(([value, data]) => ({
        value,
        label: `${data.label} (${data.count})`,
      }));
  }

  async function initIndex() {
    const [catalog, config] = await Promise.all([
      loadJson("data/catalog.json"),
      loadOptionalJson("data/config.json", {}),
    ]);
    const input = document.getElementById("searchInput");
    const results = document.getElementById("results");
    const count = document.getElementById("resultCount");
    const meta = document.getElementById("catalogMeta");
    const bankFilter = document.getElementById("bankFilter");
    const industryFilter = document.getElementById("industryFilter");
    const startDate = document.getElementById("startDate");
    const endDate = document.getElementById("endDate");
    const scopeFilter = document.getElementById("scopeFilter");
    const availabilityFilter = document.getElementById("availabilityFilter");
    const clearFilters = document.getElementById("clearFilters");
    const activeFilters = document.getElementById("activeFilters");
    const prevPage = document.getElementById("prevPage");
    const nextPage = document.getElementById("nextPage");
    const pageInfo = document.getElementById("pageInfo");
    const pageSize = document.getElementById("pageSize");
    const items = Array.isArray(catalog.items) ? catalog.items : [];
    const metadataById = new Map(items.map((item) => [item.id, metadataText(item)]));
    const searchTextById = new Map();
    let searchIndexLabel = "Text index loading";
    let currentPage = 1;

    initAdminGate(workerBaseUrl(config));

    const bankOptions = new Map();
    const industryOptions = new Map();
    for (const item of items) {
      const bKey = bankKey(item);
      const b = bankOptions.get(bKey) || { label: bankLabel(item), count: 0 };
      b.count += 1;
      bankOptions.set(bKey, b);

      const industry = inferIndustry(item);
      const i = industryOptions.get(industry) || { label: industry, count: 0 };
      i.count += 1;
      industryOptions.set(industry, i);
    }
    setOptions(bankFilter, optionSummary(bankOptions), "All institutions");
    setOptions(industryFilter, optionSummary(industryOptions), "All industries");

    function updateMeta() {
      const availableBytes = catalog.total_size_bytes || (catalog.storage && catalog.storage.total_size_bytes);
      meta.textContent = `${items.length} reports`;
      const totalSize = formatSize(availableBytes);
      const limitSize = formatSize(catalog.storage_limit_bytes || (catalog.storage && catalog.storage.limit_bytes));
      if (totalSize && limitSize) {
        meta.textContent += ` | ${totalSize} / ${limitSize} PDF storage`;
      } else if (totalSize) {
        meta.textContent += ` | ${totalSize} PDF storage`;
      }
      if (catalog.updated_at_bjt) {
        meta.textContent += ` | Updated ${catalog.updated_at_bjt}`;
      }
      meta.textContent += ` | ${searchIndexLabel}`;
    }

    function passesFilters(item) {
      if (bankFilter.value && bankKey(item) !== bankFilter.value) return false;
      if (industryFilter.value && inferIndustry(item) !== industryFilter.value) return false;
      if (availabilityFilter.value === "available" && !isPdfAvailable(item)) return false;
      if (availabilityFilter.value === "textOnly" && isPdfAvailable(item)) return false;
      const date = itemDate(item);
      if (startDate.value && (!date || date < startDate.value)) return false;
      if (endDate.value && (!date || date > endDate.value)) return false;
      return true;
    }

    function updateActiveFilters() {
      const labels = [];
      if (bankFilter.value) labels.push(bankFilter.options[bankFilter.selectedIndex].text.replace(/\s+\(\d+\)$/, ""));
      if (industryFilter.value) labels.push(industryFilter.value);
      if (startDate.value || endDate.value) labels.push(`${startDate.value || "start"} to ${endDate.value || "today"}`);
      if (availabilityFilter.value === "available") labels.push("PDF available");
      if (availabilityFilter.value === "textOnly") labels.push("Text only");
      if (scopeFilter.value !== "all") labels.push(scopeFilter.options[scopeFilter.selectedIndex].text);
      activeFilters.textContent = labels.length ? labels.join(" · ") : "No filters";
    }

    function render(options = {}) {
      if (options.resetPage) currentPage = 1;
      const query = normalize(input.value);
      const scoped = items
        .filter(passesFilters)
        .map((item) => ({
          item,
          score: scoreItem(item, query, scopeFilter.value, metadataById, searchTextById),
        }))
        .filter((entry) => !query || entry.score >= 0);

      scoped.sort((a, b) => {
        if (query && b.score !== a.score) return b.score - a.score;
        return dateSortValue(b.item) - dateSortValue(a.item);
      });

      count.textContent = `${scoped.length} of ${items.length} reports`;
      updateActiveFilters();
      const rowsPerPage = Math.max(1, Number(pageSize.value) || 50);
      const pageCount = Math.max(1, Math.ceil(scoped.length / rowsPerPage));
      currentPage = Math.min(Math.max(currentPage, 1), pageCount);
      const start = (currentPage - 1) * rowsPerPage;
      const visible = scoped.slice(start, start + rowsPerPage);
      pageInfo.textContent = scoped.length
        ? `Page ${currentPage} / ${pageCount}`
        : "Page 0 / 0";
      prevPage.disabled = currentPage <= 1 || !scoped.length;
      nextPage.disabled = currentPage >= pageCount || !scoped.length;

      if (!scoped.length) {
        results.innerHTML = '<div class="empty-state">No matching reports.</div>';
        return;
      }
      results.innerHTML = visible.map((entry) => resultRow(entry.item)).join("");
      results.scrollTop = 0;
    }

    function clearAllFilters() {
      input.value = "";
      bankFilter.value = "";
      industryFilter.value = "";
      startDate.value = "";
      endDate.value = "";
      scopeFilter.value = "all";
      availabilityFilter.value = "";
      render({ resetPage: true });
    }

    input.addEventListener("input", () => render({ resetPage: true }));
    [bankFilter, industryFilter, startDate, endDate, scopeFilter, availabilityFilter].forEach((control) => {
      control.addEventListener("change", () => render({ resetPage: true }));
    });
    pageSize.addEventListener("change", () => render({ resetPage: true }));
    prevPage.addEventListener("click", () => {
      currentPage -= 1;
      render();
    });
    nextPage.addEventListener("click", () => {
      currentPage += 1;
      render();
    });
    clearFilters.addEventListener("click", clearAllFilters);
    results.addEventListener("click", (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      window.location.href = `report.html?id=${encodeURIComponent(row.dataset.id)}`;
    });

    loadJson("data/search_index.json")
      .then((searchIndex) => {
        const searchItems = Array.isArray(searchIndex.items) ? searchIndex.items : [];
        searchItems.forEach((entry) => {
          if (entry.id && entry.text) {
            searchTextById.set(entry.id, String(entry.text));
          }
        });
        searchIndexLabel = `Text index ${searchTextById.size} reports`;
        if (searchIndex.text_pruned_dates && searchIndex.text_pruned_dates.length) {
          searchIndexLabel += " (recent text)";
        }
        updateMeta();
        render();
      })
      .catch((error) => {
        console.warn(error);
        searchIndexLabel = "Text index unavailable";
        updateMeta();
      });

    updateMeta();
    render();
  }

  function filenameFromDisposition(disposition, fallback) {
    const header = String(disposition || "");
    const utfMatch = header.match(/filename\*=UTF-8''([^;]+)/i);
    if (utfMatch) return decodeURIComponent(utfMatch[1]);
    const plainMatch = header.match(/filename="?([^";]+)"?/i);
    if (plainMatch) return plainMatch[1];
    return fallback || "report.pdf";
  }

  function field(label, value) {
    return `
      <div class="detail-field">
        <span>${escapeHtml(label)}</span>
        <strong>${escapeHtml(value || "-")}</strong>
      </div>
    `;
  }

  function importantTokens(text) {
    const counts = new Map();
    for (const token of queryTokens(text)) {
      if (token.length < 3 || STOPWORDS.has(token) || /^\d+$/.test(token)) continue;
      counts.set(token, (counts.get(token) || 0) + 1);
    }
    return [...counts.entries()]
      .sort((a, b) => b[1] - a[1])
      .slice(0, 16)
      .map(([token]) => token);
  }

  function relatedReports(current, items, searchTextById) {
    const currentIndustry = inferIndustry(current);
    const currentBank = bankKey(current);
    const currentDate = dateSortValue(current);
    const keywords = importantTokens(`${current.title} ${current.title_zh || ""} ${(searchTextById.get(current.id) || "").slice(0, 6000)}`);

    const scored = items
      .filter((item) => item.id !== current.id)
      .map((item) => {
        let score = 0;
        if (inferIndustry(item) === currentIndustry) score += 34;
        if (bankKey(item) === currentBank) score += 18;
        if (dateSortValue(item) === currentDate) score += 5;

        const title = normalize(`${item.title || ""} ${item.title_zh || ""}`);
        const text = searchTextById.get(item.id) || "";
        for (const token of keywords) {
          if (title.includes(token)) score += 8;
          if (text.includes(token)) score += 2;
        }
        return { item, score };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return dateSortValue(b.item) - dateSortValue(a.item);
      });

    return scored.slice(0, 6).map((entry) => entry.item);
  }

  function downloadErrorMessage(status, message, data) {
    const text = String(message || "");
    if (
      data && data.archived ||
      status === 404 && /pdf|object|mirrored|archived|not found/i.test(text)
    ) {
      return `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`;
    }
    if (/password/i.test(text)) return text;
    if (/configured/i.test(text)) return "PDF download is not configured.";
    return text || "Download failed.";
  }

  function adminPanelMarkup() {
    return `
      <section class="admin-panel" id="adminPanel" hidden>
        <div class="admin-panel-heading">
          <h3>Delivery link</h3>
          <span>Private</span>
        </div>
        <div class="delivery-row">
          <button class="primary" id="generateDeliveryLink" type="button">Generate</button>
          <input id="deliveryLinkInput" type="text" readonly aria-label="Delivery link">
          <button id="copyDeliveryLink" type="button">Copy</button>
        </div>
        <div id="deliveryStatus" class="status-line" aria-live="polite"></div>
      </section>
    `;
  }

  function reportPageUrl(id) {
    const url = new URL("report.html", window.location.href);
    url.searchParams.set("id", id);
    return url.toString();
  }

  function deliveryPageUrl(id, password) {
    const url = new URL("delivery.html", window.location.href);
    url.searchParams.set("id", id);
    url.searchParams.set("password", password);
    return url.toString();
  }

  async function requestReportPassword(workerUrl, id) {
    const token = getAdminToken();
    if (!token) throw new Error("Private tools are locked.");
    const response = await fetch(`${workerUrl}/admin/report-password`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ id, token }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      if (response.status === 401) clearAdminToken();
      throw new Error(data.error || "Could not generate delivery link.");
    }
    return data;
  }

  function initDetailAdmin(item, workerUrl) {
    const panel = document.getElementById("adminPanel");
    const generate = document.getElementById("generateDeliveryLink");
    const linkInput = document.getElementById("deliveryLinkInput");
    const copy = document.getElementById("copyDeliveryLink");
    const status = document.getElementById("deliveryStatus");
    if (!panel || !generate || !linkInput || !copy || !status) return;

    function refresh() {
      panel.hidden = !getAdminToken();
    }

    refresh();
    document.addEventListener("kcdesk-admin-change", refresh);

    generate.addEventListener("click", async () => {
      status.className = "status-line";
      status.textContent = "Generating...";
      generate.disabled = true;
      try {
        const data = await requestReportPassword(workerUrl, item.id);
        linkInput.value = deliveryPageUrl(item.id, data.password);
        status.textContent = "Delivery link generated.";
        status.classList.add("ok");
      } catch (error) {
        linkInput.value = "";
        status.textContent = error.message || "Could not generate delivery link.";
        status.classList.add("error");
      } finally {
        generate.disabled = false;
      }
    });

    copy.addEventListener("click", async () => {
      if (!linkInput.value) return;
      try {
        await navigator.clipboard.writeText(linkInput.value);
        status.className = "status-line ok";
        status.textContent = "Copied.";
      } catch (_error) {
        linkInput.select();
        status.className = "status-line";
        status.textContent = "Select and copy the link.";
      }
    });
  }

  function detailTitleMarkup(item) {
    const zh = titleZhText(item);
    return `
      <div>
        <h1 class="detail-title">${escapeHtml(titleText(item))}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">Indexed report record with password-protected PDF access when available.</p>
      </div>
    `;
  }

  function renderDetail(item, config, catalogItems, searchTextById) {
    const detail = document.getElementById("detail");
    const workerUrl = String(config.worker_base_url || "").replace(/\/$/, "");
    const available = isPdfAvailable(item);
    const setupWarning = workerUrl || !available
      ? ""
      : '<div class="setup-warning">PDF download is not configured.</div>';
    const archiveNotice = available
      ? ""
      : `<div class="archive-notice">PDF storage for this report is currently archived, but the text record remains searchable. Contact WeChat: <strong>${escapeHtml(CONTACT_WECHAT)}</strong>.</div>`;
    const related = relatedReports(item, catalogItems, searchTextById);
    const relatedMarkup = related.length
      ? `
        <section class="related-section" aria-labelledby="relatedTitle">
          <div class="related-heading">
            <h3 id="relatedTitle">Related Reports</h3>
          </div>
          <div class="related-list">${related.map(relatedRow).join("")}</div>
        </section>
      `
      : "";
    const unlockMarkup = available
      ? `
        ${setupWarning}
        <form class="unlock-box" id="unlockForm">
          <h3>PDF Download</h3>
          <p class="subtle">Enter the report password to download the PDF.</p>
          <div class="password-row">
            <input id="passwordInput" type="password" autocomplete="current-password" placeholder="Password" required>
            <button class="primary" type="submit">Download</button>
          </div>
          <div id="downloadStatus" class="status-line" aria-live="polite"></div>
        </form>
      `
      : archiveNotice;

    detail.innerHTML = `
      ${detailTitleMarkup(item)}
      <div class="detail-grid">
        ${field("Institution", bankLabel(item))}
        ${field("Industry", inferIndustry(item))}
        ${field("Date", displayDate(item.date_folder))}
        ${field("PDF", available ? formatSize(item.size_bytes) || "Available" : "Text only")}
      </div>
      ${unlockMarkup}
      ${workerUrl ? adminPanelMarkup() : ""}
      ${relatedMarkup}
    `;

    detail.addEventListener("click", (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      window.location.href = `report.html?id=${encodeURIComponent(row.dataset.id)}`;
    });

    initDetailAdmin(item, workerUrl);

    if (!available) return;

    const form = document.getElementById("unlockForm");
    const input = document.getElementById("passwordInput");
    const status = document.getElementById("downloadStatus");
    const button = form.querySelector("button");

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      status.className = "status-line";
      if (!workerUrl) {
        status.textContent = "PDF download is not configured.";
        status.classList.add("error");
        return;
      }

      button.disabled = true;
      status.textContent = "Checking password...";
      try {
        const response = await fetch(`${workerUrl}/download`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            id: item.id,
            password: input.value,
            password_group: item.password_group || "default",
          }),
        });

        if (!response.ok) {
          let data = {};
          let message = `Download failed (${response.status}).`;
          try {
            data = await response.json();
            if (data.error) message = data.error;
          } catch (_err) {
            // Ignore non-JSON errors.
          }
          throw new Error(downloadErrorMessage(response.status, message, data));
        }

        const blob = await response.blob();
        const objectUrl = URL.createObjectURL(blob);
        const link = document.createElement("a");
        link.href = objectUrl;
        link.download = filenameFromDisposition(response.headers.get("Content-Disposition"), item.filename);
        document.body.appendChild(link);
        link.click();
        link.remove();
        URL.revokeObjectURL(objectUrl);
        status.textContent = "Download started.";
        status.classList.add("ok");
      } catch (error) {
        status.textContent = error.message || "Download failed.";
        status.classList.add("error");
      } finally {
        button.disabled = false;
      }
    });
  }

  async function initReport() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const [catalog, config, searchIndex] = await Promise.all([
      loadJson("data/catalog.json"),
      loadJson("data/config.json"),
      loadOptionalJson("data/search_index.json", { items: [] }),
    ]);
    const workerUrl = workerBaseUrl(config);
    initAdminGate(workerUrl);
    const items = Array.isArray(catalog.items) ? catalog.items : [];
    const item = items.find((entry) => entry.id === id);
    if (!item) {
      document.getElementById("detail").innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }
    const searchTextById = new Map();
    for (const entry of Array.isArray(searchIndex.items) ? searchIndex.items : []) {
      if (entry.id && entry.text) searchTextById.set(entry.id, String(entry.text));
    }
    document.title = `${titleText(item)} | KC Desk Notes`;
    renderDetail(item, config, items, searchTextById);
  }

  async function initDelivery() {
    const params = new URLSearchParams(window.location.search);
    const id = params.get("id");
    const password = params.get("password") || "";
    const target = document.getElementById("delivery");
    if (!id || !password) {
      target.innerHTML = '<div class="error-state">Delivery link is incomplete.</div>';
      return;
    }

    const catalog = await loadJson("data/catalog.json");
    const items = Array.isArray(catalog.items) ? catalog.items : [];
    const item = items.find((entry) => entry.id === id);
    if (!item) {
      target.innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }

    const available = isPdfAvailable(item);
    const zh = titleZhText(item);
    document.title = `Delivery | ${titleText(item)}`;
    target.innerHTML = `
      <div>
        <h1 class="detail-title">${escapeHtml(titleText(item))}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">Report delivery details.</p>
      </div>
      <div class="detail-grid">
        ${field("Institution", bankLabel(item))}
        ${field("Date", displayDate(item.date_folder))}
        ${field("Industry", inferIndustry(item))}
        ${field("PDF", available ? formatSize(item.size_bytes) || "Available" : "Text only")}
      </div>
      <div class="delivery-card">
        <span>Report password</span>
        <strong>${escapeHtml(password)}</strong>
      </div>
      ${available ? "" : `<div class="archive-notice">PDF storage for this report is currently archived. Contact WeChat: <strong>${escapeHtml(CONTACT_WECHAT)}</strong>.</div>`}
      <div class="delivery-actions">
        <a class="primary-link" href="${escapeHtml(reportPageUrl(item.id))}">Open report page</a>
        <button id="copyDeliveryPassword" type="button">Copy password</button>
      </div>
      <div id="deliveryCopyStatus" class="status-line" aria-live="polite"></div>
    `;

    document.getElementById("copyDeliveryPassword").addEventListener("click", async () => {
      const status = document.getElementById("deliveryCopyStatus");
      try {
        await navigator.clipboard.writeText(password);
        status.className = "status-line ok";
        status.textContent = "Copied.";
      } catch (_error) {
        status.className = "status-line";
        status.textContent = "Password can be selected from the box above.";
      }
    });
  }

  const boot = page === "report" ? initReport : page === "delivery" ? initDelivery : initIndex;
  boot().catch((error) => {
    const target = page === "report"
      ? document.getElementById("detail")
      : page === "delivery"
        ? document.getElementById("delivery")
        : document.getElementById("results");
    if (target) target.innerHTML = `<div class="error-state">${escapeHtml(error.message)}</div>`;
  });
}());
