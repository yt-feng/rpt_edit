(function () {
  const page = document.body.dataset.page;

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

  function matchesQuery(haystack, query) {
    if (!query) return true;
    if (haystack.includes(query)) return true;
    const tokens = query.split(" ").filter(Boolean);
    return tokens.length > 1 && tokens.every((token) => haystack.includes(token));
  }

  async function loadJson(path) {
    const response = await fetch(path, { cache: "no-store" });
    if (!response.ok) {
      throw new Error(`Could not load ${path}: ${response.status}`);
    }
    return response.json();
  }

  function formatSize(bytes) {
    const size = Number(bytes || 0);
    if (!size) return "";
    if (size >= 1024 * 1024) return `${(size / 1024 / 1024).toFixed(1)} MB`;
    if (size >= 1024) return `${Math.round(size / 1024)} KB`;
    return `${size} B`;
  }

  function displayDate(value) {
    const text = String(value || "");
    if (/^\d{6}$/.test(text)) {
      return `20${text.slice(0, 2)}-${text.slice(2, 4)}-${text.slice(4, 6)}`;
    }
    if (/^\d{8}$/.test(text)) {
      return `${text.slice(0, 4)}-${text.slice(4, 6)}-${text.slice(6, 8)}`;
    }
    return text || "-";
  }

  function resultRow(item) {
    const bank = item.bank_code || "Other";
    const size = formatSize(item.size_bytes);
    return `
      <button class="report-row" type="button" data-id="${escapeHtml(item.id)}">
        <span class="pill">${escapeHtml(bank)}</span>
        <span class="date-text">${escapeHtml(displayDate(item.date_folder))}</span>
        <span class="title-text">${escapeHtml(item.title)}</span>
        <span class="size-text">${escapeHtml(size)}</span>
      </button>
    `;
  }

  async function initIndex() {
    const catalog = await loadJson("data/catalog.json");
    const input = document.getElementById("searchInput");
    const results = document.getElementById("results");
    const count = document.getElementById("resultCount");
    const meta = document.getElementById("catalogMeta");
    const items = Array.isArray(catalog.items) ? catalog.items : [];
    const metadataById = new Map(items.map((item) => [
      item.id,
      normalize([
        item.title,
        item.filename,
        item.bank_code,
        item.bank_name,
        item.date_folder,
        (item.date_folders || []).join(" "),
      ].join(" ")),
    ]));
    const searchTextById = new Map();
    let searchIndexLabel = " | Full-text loading";

    function updateMeta() {
      meta.textContent = `${items.length} reports`;
      if (catalog.updated_at_bjt) {
        meta.textContent += ` | Updated ${catalog.updated_at_bjt}`;
      }
      meta.textContent += searchIndexLabel;
    }

    function render() {
      const query = normalize(input.value);
      const filtered = items.filter((item) => {
        if (!query) return true;
        const metadata = metadataById.get(item.id) || "";
        const fullText = searchTextById.get(item.id) || "";
        return matchesQuery(metadata, query) || matchesQuery(fullText, query);
      });

      count.textContent = `${filtered.length} item${filtered.length === 1 ? "" : "s"}`;
      if (!filtered.length) {
        results.innerHTML = '<div class="empty-state">No matching reports.</div>';
        return;
      }
      results.innerHTML = filtered.map(resultRow).join("");
    }

    input.addEventListener("input", render);
    results.addEventListener("click", (event) => {
      const row = event.target.closest(".report-row");
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
        searchIndexLabel = ` | Full-text ${searchTextById.size} reports`;
        updateMeta();
        render();
      })
      .catch((error) => {
        console.warn(error);
        searchIndexLabel = " | Full-text unavailable";
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

  function renderDetail(item, config) {
    const detail = document.getElementById("detail");
    const workerUrl = String(config.worker_base_url || "").replace(/\/$/, "");
    const setupWarning = workerUrl
      ? ""
      : '<div class="setup-warning">Download worker is not configured yet. Set the KC_DESK_WORKER_URL repository variable before deploying Pages.</div>';

    detail.innerHTML = `
      <div>
        <h1 class="detail-title">${escapeHtml(item.title)}</h1>
        <p class="subtle">PDF preview is disabled. Password unlock requests are handled by the private Worker.</p>
      </div>
      <div class="detail-grid">
        ${field("Bank", item.bank_code || item.bank_name)}
        ${field("Date", displayDate(item.date_folder))}
        ${field("Size", formatSize(item.size_bytes))}
        ${field("Status", item.available === false ? "Not mirrored yet" : "Available")}
      </div>
      ${setupWarning}
      <form class="unlock-box" id="unlockForm">
        <h3>Unlock PDF</h3>
        <p class="subtle">Enter the report password to request the private PDF as an attachment.</p>
        <div class="password-row">
          <input id="passwordInput" type="password" autocomplete="current-password" placeholder="Password" required>
          <button class="primary" type="submit">Unlock</button>
        </div>
        <div id="downloadStatus" class="status-line" aria-live="polite"></div>
      </form>
    `;

    const form = document.getElementById("unlockForm");
    const input = document.getElementById("passwordInput");
    const status = document.getElementById("downloadStatus");
    const button = form.querySelector("button");

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      status.className = "status-line";
      if (!workerUrl) {
        status.textContent = "Worker endpoint is not configured.";
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
          let message = `Download failed (${response.status}).`;
          try {
            const errorData = await response.json();
            if (errorData.error) message = errorData.error;
          } catch (_err) {
            // Ignore non-JSON errors.
          }
          throw new Error(message);
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
        status.textContent = "Unlocked. Download started.";
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
    const [catalog, config] = await Promise.all([
      loadJson("data/catalog.json"),
      loadJson("data/config.json"),
    ]);
    const item = (catalog.items || []).find((entry) => entry.id === id);
    if (!item) {
      document.getElementById("detail").innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }
    document.title = `${item.title} | KC Desk Notes`;
    renderDetail(item, config);
  }

  const boot = page === "report" ? initReport : initIndex;
  boot().catch((error) => {
    const target = page === "report" ? document.getElementById("detail") : document.getElementById("results");
    if (target) target.innerHTML = `<div class="error-state">${escapeHtml(error.message)}</div>`;
  });
}());
