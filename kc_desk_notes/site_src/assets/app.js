(function () {
  const page = document.body.dataset.page;
  const CONTACT_WECHAT = "MacroGate";
  const ADMIN_TOKEN_KEY = "kcdesk_admin_token";
  const ADMIN_PLAIN_KEY = "kcdesk_admin_plain_key";
  const ADMIN_COOKIE_NAME = "kcdesk_admin_token";
  const ADMIN_COOKIE_MAX_AGE = 180 * 24 * 60 * 60;
  const DOWNLOAD_PASSWORD_KEY = "kcdesk_download_password";
  const AUTH_SESSION_KEY = "kcdesk_auth_session";
  const AUTHORITY_SOURCE = "authority";
  const REPORT_A_SOURCE = "report-a";
  const EXTERNAL_SOURCE = "external";
  const PDFJS_MODULE_URL = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.mjs";
  const PDFJS_WORKER_URL = "https://cdn.jsdelivr.net/npm/pdfjs-dist@4.10.38/build/pdf.worker.mjs";
  let accountAdminDailyPicks = new Map();
  let pdfJsLoadPromise = null;

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
    "slightly", "likely", "better", "daily", "weekly", "monthly", "nom", "jpm", "ubs", "citi",
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

  function setAdminPlainKey(value) {
    try {
      localStorage.setItem(ADMIN_PLAIN_KEY, String(value || ""));
    } catch (_error) {
      // Admin token still keeps the device unlocked.
    }
  }

  function getAdminPlainKey() {
    try {
      return localStorage.getItem(ADMIN_PLAIN_KEY) || "";
    } catch (_error) {
      return "";
    }
  }

  function clearAdminToken() {
    try {
      localStorage.removeItem(ADMIN_TOKEN_KEY);
      localStorage.removeItem(ADMIN_PLAIN_KEY);
    } catch (_error) {
      // Ignore localStorage access errors.
    }
    clearCookie(ADMIN_COOKIE_NAME);
    document.dispatchEvent(new CustomEvent("kcdesk-admin-change"));
  }

  function workerBaseUrl(config) {
    const configured = String((config && config.worker_base_url) || "/api").replace(/\/$/, "");
    try {
      const url = new URL(configured, window.location.href);
      if (url.hostname.endsWith("workers.dev") && window.location.hostname.endsWith("kcdesk.com")) {
        return "/api";
      }
    } catch (_error) {
      // Relative URLs are fine.
    }
    return configured || "/api";
  }

  function loadAuthSession() {
    try {
      const raw = localStorage.getItem(AUTH_SESSION_KEY);
      if (!raw) return null;
      const session = JSON.parse(raw);
      if (!session || !session.token || !session.user || !session.user.email) return null;
      return session;
    } catch (_error) {
      return null;
    }
  }

  function saveAuthSession(session) {
    try {
      localStorage.setItem(AUTH_SESSION_KEY, JSON.stringify(session));
    } catch (_error) {
      // Ignore storage errors; the current page still has the response.
    }
    document.dispatchEvent(new CustomEvent("kcdesk-auth-change"));
  }

  function clearAuthSession() {
    try {
      localStorage.removeItem(AUTH_SESSION_KEY);
    } catch (_error) {
      // Ignore storage errors.
    }
    document.dispatchEvent(new CustomEvent("kcdesk-auth-change"));
  }

  function authHeaders() {
    const session = loadAuthSession();
    return session && session.token ? { "Authorization": `Bearer ${session.token}` } : {};
  }

  function authUserLabel(session) {
    const user = session && session.user;
    if (!user) return "登录";
    return user.username || user.email || "账号";
  }

  function isSuperSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user && (user.role === "super" || user.is_super));
  }

  function privateToolsUnlocked() {
    return Boolean(getAdminToken() || isSuperSession());
  }

  async function refreshAuthSession(workerUrl) {
    const session = loadAuthSession();
    if (!session || !session.token || !workerUrl) return null;
    try {
      const response = await fetch(`${workerUrl}/auth`, {
        cache: "no-store",
        headers: authHeaders(),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "Session expired.");
      saveAuthSession({ token: data.token, user: data.user });
      return { token: data.token, user: data.user };
    } catch (_error) {
      clearAuthSession();
      return null;
    }
  }

  function initAccountGate(workerUrl) {
    const gate = document.getElementById("accountGate");
    if (!gate) return;
    function update() {
      const session = loadAuthSession();
      gate.textContent = authUserLabel(session);
      gate.classList.toggle("is-unlocked", Boolean(session));
    }
    update();
    document.addEventListener("kcdesk-auth-change", update);
    gate.addEventListener("click", () => showAccountModal(workerUrl));
    refreshAuthSession(workerUrl).then(update);
  }

  function accountModalMarkup(context = {}) {
    const session = loadAuthSession();
    const signedIn = Boolean(session);
    const reportTitle = context.item ? titleText(context.item) : "";
    const reportLine = reportTitle ? `<span>当前报告：${escapeHtml(reportTitle)}</span>` : "";
    return `
      <div class="admin-modal account-modal" id="accountModal" role="dialog" aria-modal="true" aria-labelledby="accountModalTitle">
        <div class="admin-dialog account-dialog">
          <button class="admin-close" id="accountClose" type="button" aria-label="Close">&times;</button>
          <h3 id="accountModalTitle">账号管理</h3>
          <form id="accountAuthForm" class="auth-form" ${signedIn ? "hidden" : ""}>
            <div class="auth-grid">
              <label>用户名<input id="accountUsername" type="text" autocomplete="username" placeholder="yourname" required></label>
              <label id="accountEmailLabel" hidden>邮箱（可选）<input id="accountEmail" type="email" autocomplete="email" placeholder="you@example.com"></label>
              <label>密码<input id="accountPassword" type="password" autocomplete="current-password" placeholder="至少 4 位" required></label>
            </div>
            <label class="captcha-field">验证码
              <div class="captcha-row">
                <img id="accountCaptchaImage" alt="验证码">
                <button class="secondary-button" id="accountRefreshCaptcha" type="button">换一张</button>
              </div>
              <input id="accountCaptchaAnswer" type="text" inputmode="numeric" autocomplete="off" placeholder="输入结果" required>
            </label>
            <div class="account-modal-actions">
              <button class="primary" id="accountSubmit" type="submit">登录</button>
              <button class="secondary-button" id="accountModeToggle" type="button">注册新账号</button>
            </div>
          </form>
          <div id="accountSummary" class="account-summary" ${signedIn ? "" : "hidden"}>
            <span>当前账号</span>
            <strong id="accountName">${escapeHtml(authUserLabel(session))}</strong>
            <span id="accountEmailText">${escapeHtml(session && session.user ? session.user.email : "")}</span>
            <div class="account-modal-actions">
              <button class="secondary-button quiet-admin-button" id="accountAdminOpen" type="button" hidden>管理后台</button>
              <button class="secondary-button" id="accountLogout" type="button">退出登录</button>
            </div>
          </div>
          <div class="contact-card" id="accountContactCard">
            <strong>报告获取</strong>
            ${reportLine}
            <span>开通账号权限或获取报告，请联系微信 <b>${escapeHtml(CONTACT_WECHAT)}</b>。</span>
          </div>
          <div id="accountModalStatus" class="status-line" aria-live="polite"></div>
        </div>
      </div>
    `;
  }

  async function loadAccountCaptcha(workerUrl, status) {
    const image = document.getElementById("accountCaptchaImage");
    const refresh = document.getElementById("accountRefreshCaptcha");
    if (!image || !refresh) return "";
    refresh.disabled = true;
    try {
      const response = await fetch(`${workerUrl}/captcha`, { cache: "no-store" });
      const data = await response.json();
      if (!response.ok || !data.image || !data.token) throw new Error(data.detail || "验证码加载失败。");
      image.src = data.image;
      return data.token;
    } catch (error) {
      status.textContent = error.message || "验证码加载失败。";
      status.className = "status-line error";
      return "";
    } finally {
      refresh.disabled = false;
    }
  }

  async function showAccountModal(workerUrl, context = {}) {
    if (!workerUrl) {
      window.alert("Account service is temporarily unavailable.");
      return "";
    }
    const existing = document.getElementById("accountModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", accountModalMarkup(context));

    const modal = document.getElementById("accountModal");
    const close = document.getElementById("accountClose");
    const form = document.getElementById("accountAuthForm");
    const summary = document.getElementById("accountSummary");
    const username = document.getElementById("accountUsername");
    const emailLabel = document.getElementById("accountEmailLabel");
    const email = document.getElementById("accountEmail");
    const password = document.getElementById("accountPassword");
    const answer = document.getElementById("accountCaptchaAnswer");
    const refresh = document.getElementById("accountRefreshCaptcha");
    const submit = document.getElementById("accountSubmit");
    const toggle = document.getElementById("accountModeToggle");
    const logout = document.getElementById("accountLogout");
    const adminOpen = document.getElementById("accountAdminOpen");
    const status = document.getElementById("accountModalStatus");
    let mode = "login";
    let captchaToken = "";

    function setStatus(text, kind) {
      status.className = kind ? `status-line ${kind}` : "status-line";
      status.textContent = text || "";
    }

    function refreshUi() {
      const session = loadAuthSession();
      const signedIn = Boolean(session);
      form.hidden = signedIn;
      summary.hidden = !signedIn;
      if (signedIn) {
        document.getElementById("accountName").textContent = authUserLabel(session);
        document.getElementById("accountEmailText").textContent = session.user.email || "";
        if (adminOpen) adminOpen.hidden = !isSuperSession(session);
        setStatus(isSuperSession(session) ? "已登录，当前账号拥有管理员权限。" : `已登录。如需开通下载权限，请联系微信 ${CONTACT_WECHAT}。`, "ok");
        fetch(`${workerUrl}/entitlement`, { cache: "no-store", headers: authHeaders() })
          .then((response) => response.json())
          .then((data) => {
            const entitlement = data && data.entitlement;
            if (entitlement && entitlement.active && (entitlement.plan === "annual" || entitlement.plan === "super")) {
              setStatus(`账号下载权限有效${entitlement.current_period_end ? `至 ${entitlement.current_period_end.slice(0, 10)}` : ""}。`, "ok");
            }
          })
          .catch(() => {});
      } else {
        if (adminOpen) adminOpen.hidden = true;
        captchaToken = "";
        loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; });
      }
    }

    function setMode(nextMode) {
      mode = nextMode;
      emailLabel.hidden = mode !== "register";
      password.autocomplete = mode === "register" ? "new-password" : "current-password";
      submit.textContent = mode === "register" ? "注册并登录" : "登录";
      toggle.textContent = mode === "register" ? "已有账号，去登录" : "注册新账号";
      answer.value = "";
      loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; });
    }

    function finish() {
      modal.remove();
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    toggle.addEventListener("click", () => setMode(mode === "login" ? "register" : "login"));
    refresh.addEventListener("click", () => loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; }));
    if (logout) {
      logout.addEventListener("click", () => {
        clearAuthSession();
        setStatus("已退出登录。");
        refreshUi();
      });
    }
    if (adminOpen) {
      adminOpen.addEventListener("click", () => showAccountAdminModal(workerUrl));
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      submit.disabled = true;
      setStatus(mode === "register" ? "正在注册…" : "正在登录…");
      try {
        const response = await fetch(`${workerUrl}/auth`, {
          method: "POST",
          headers: { "Content-Type": "application/json" },
          body: JSON.stringify({
            action: mode,
            username: username.value,
            password: password.value,
            email: mode === "register" ? email.value : "",
            captcha_token: captchaToken,
            captcha_answer: answer.value,
          }),
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "账号请求失败。");
        saveAuthSession({ token: data.token, user: data.user });
        password.value = "";
        answer.value = "";
        refreshUi();
      } catch (error) {
        setStatus(error.message || "账号请求失败。", "error");
        answer.value = "";
        captchaToken = await loadAccountCaptcha(workerUrl, status);
      } finally {
        submit.disabled = false;
      }
    });

    refreshUi();
    if (!loadAuthSession() && username) username.focus();
  }

  function accountAdminModalMarkup() {
    return `
      <div class="admin-modal account-admin-modal" id="accountAdminModal" role="dialog" aria-modal="true" aria-labelledby="accountAdminTitle">
        <div class="admin-dialog account-admin-dialog">
          <button class="admin-close" id="accountAdminClose" type="button" aria-label="Close">&times;</button>
          <div class="account-admin-top">
            <h3 id="accountAdminTitle">管理后台</h3>
            <button class="secondary-button" id="accountAdminRefresh" type="button">刷新</button>
          </div>
          <div id="accountAdminStatus" class="status-line" aria-live="polite">正在读取后台信息…</div>
          <section class="account-admin-section account-admin-picks-section">
            <div class="account-admin-heading">
              <strong>每日精选</strong>
              <span id="accountAdminPickCount"></span>
            </div>
            <div id="accountAdminPicks" class="account-admin-picks"></div>
          </section>
          <section class="account-admin-section">
            <div class="account-admin-heading">
              <strong>每日文件</strong>
              <span>GitHub latest</span>
            </div>
            <div id="accountAdminFiles" class="account-admin-files"></div>
          </section>
          <section class="account-admin-section">
            <div class="account-admin-heading">
              <strong>用户信息</strong>
              <span id="accountAdminUserCount"></span>
            </div>
            <div class="account-admin-table-wrap">
              <table class="account-admin-table">
                <thead>
                  <tr>
                    <th>用户名</th>
                    <th>邮箱</th>
                    <th>权限</th>
                    <th>注册</th>
                    <th>最近登录</th>
                  </tr>
                </thead>
                <tbody id="accountAdminUsers"></tbody>
              </table>
            </div>
          </section>
        </div>
      </div>
    `;
  }

  function adminUserEntitlementLabel(user) {
    if (user && user.role === "super") return "super";
    const entitlement = user && user.entitlement || {};
    if (entitlement.active) return entitlement.plan || "active";
    return "free";
  }

  function adminUserRow(user) {
    return `
      <tr>
        <td>${escapeHtml(user.username || "")}</td>
        <td>${escapeHtml(user.email || "")}</td>
        <td>${escapeHtml(adminUserEntitlementLabel(user))}</td>
        <td>${escapeHtml(String(user.created_at || "").slice(0, 10))}</td>
        <td>${escapeHtml(String(user.last_login_at || "").replace("T", " ").slice(0, 16))}</td>
      </tr>
    `;
  }

  function adminFileRow(file) {
    const key = file.type === "artifact" ? file.id : file.path;
    const endpointAttr = file.type === "artifact" ? "artifact" : "file";
    const note = file.note ? `<span>${escapeHtml(file.note)}</span>` : "";
    const repo = file.repo || "";
    return `
      <div class="account-admin-file">
        <div>
          <strong>${escapeHtml(file.label || file.kind || "File")}</strong>
          <span>${escapeHtml(file.date || "")} · ${escapeHtml(file.name || "")}${file.size_bytes ? ` · ${escapeHtml(formatSize(file.size_bytes))}` : ""}</span>
          ${note}
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions">
          <button class="secondary-button account-admin-download" type="button"
            data-kind="${escapeHtml(endpointAttr)}"
            data-key="${escapeHtml(key || "")}"
            data-repo="${escapeHtml(repo)}"
            data-name="${escapeHtml(file.name || "download")}">下载</button>
          <button class="secondary-button account-admin-cancel" type="button" hidden>取消</button>
        </div>
      </div>
    `;
  }

  function adminPickMeta(pick) {
    const parts = [
      pick.bank,
      pick.date_folder,
      pick.page_count ? `${pick.page_count}页` : "页数待识别",
      pick.first_page_landscape ? "横屏PDF" : "",
      pick.size_bytes ? formatSize(pick.size_bytes) : "",
    ].filter(Boolean);
    return parts.join(" · ");
  }

  function adminDailyPickRow(pick) {
    const intro = String(pick.intro || "").trim();
    const title = pick.display_title || pick.title_zh || pick.title || "Untitled report";
    const tags = Array.isArray(pick.tags) && pick.tags.length
      ? `<div class="account-admin-pick-tags">${pick.tags.map((tag) => `<span>${escapeHtml(tag)}</span>`).join("")}</div>`
      : "";
    return `
      <article class="account-admin-pick" data-id="${escapeHtml(pick.id || "")}">
        <div class="account-admin-pick-main">
          <div class="account-admin-pick-title">
            <strong>${escapeHtml(title)}</strong>
            ${pick.title && pick.title !== title ? `<span>${escapeHtml(pick.title)}</span>` : ""}
          </div>
          <span class="account-admin-pick-meta">${escapeHtml(adminPickMeta(pick))}</span>
          ${tags}
          <textarea class="account-admin-pick-intro" readonly aria-label="介绍文字">${escapeHtml(intro)}</textarea>
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions account-admin-pick-actions">
          <button class="secondary-button account-admin-copy-intro" type="button">复制文案</button>
          <button class="secondary-button account-admin-report-download" type="button">下载报告</button>
          <button class="secondary-button account-admin-cover-save" type="button">保存首图</button>
          <button class="secondary-button account-admin-cancel" type="button" hidden>取消</button>
        </div>
      </article>
    `;
  }

  function resetDownloadProgress(progress) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    if (bar) bar.style.width = "0%";
    if (text) text.textContent = "等待下载…";
    progress.hidden = true;
  }

  function setDownloadProgress(progress, loaded, total) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    progress.hidden = false;
    if (total > 0) {
      const percent = Math.min(100, Math.round((loaded / total) * 100));
      if (bar) bar.style.width = `${percent}%`;
      if (text) text.textContent = `${percent}% · ${formatSize(loaded)} / ${formatSize(total)}`;
    } else {
      if (bar) bar.style.width = "35%";
      if (text) text.textContent = `已下载 ${formatSize(loaded)}`;
    }
  }

  async function responseBlobWithProgress(response, progress) {
    const total = Number(response.headers.get("Content-Length") || 0);
    if (!response.body || !response.body.getReader) {
      const blob = await response.blob();
      setDownloadProgress(progress, blob.size || total, blob.size || total);
      return blob;
    }
    const reader = response.body.getReader();
    const chunks = [];
    let loaded = 0;
    while (true) {
      const { done, value } = await reader.read();
      if (done) break;
      chunks.push(value);
      loaded += value.byteLength || value.length || 0;
      setDownloadProgress(progress, loaded, total);
    }
    setDownloadProgress(progress, loaded, total || loaded);
    return new Blob(chunks, { type: response.headers.get("Content-Type") || "application/octet-stream" });
  }

  function accountAdminReportEndpoint(workerUrl, id) {
    return `${workerUrl}/account-admin/report-pdf?id=${encodeURIComponent(id)}`;
  }

  async function fetchAccountAdminReportBlob(workerUrl, pick, progress, signal) {
    const response = await fetch(accountAdminReportEndpoint(workerUrl, pick.id), {
      headers: authHeaders(),
      signal,
    });
    if (!response.ok) {
      const data = await response.json().catch(() => ({}));
      throw new Error(data.detail || `报告读取失败 (${response.status})。`);
    }
    return responseBlobWithProgress(response, progress);
  }

  async function loadPdfJs() {
    if (!pdfJsLoadPromise) {
      pdfJsLoadPromise = import(PDFJS_MODULE_URL).then((pdfjs) => {
        pdfjs.GlobalWorkerOptions.workerSrc = PDFJS_WORKER_URL;
        return pdfjs;
      });
    }
    return pdfJsLoadPromise;
  }

  function downloadDataUrl(dataUrl, filename) {
    const link = document.createElement("a");
    link.href = dataUrl;
    link.download = filename;
    document.body.appendChild(link);
    link.click();
    link.remove();
  }

  function imageFilenameForPick(pick) {
    const base = String(pick.display_title || pick.title_zh || pick.title || pick.id || "report")
      .replace(/[\r\n"\\/:*?<>|]+/g, " ")
      .replace(/\s+/g, " ")
      .trim()
      .slice(0, 120);
    return `${base || "report"}-page-1.png`;
  }

  async function saveFirstPageImageFromPdfBlob(blob, pick) {
    const pdfjs = await loadPdfJs();
    const data = new Uint8Array(await blob.arrayBuffer());
    const pdf = await pdfjs.getDocument({ data }).promise;
    const page = await pdf.getPage(1);
    const baseViewport = page.getViewport({ scale: 1 });
    const scale = Math.min(2.4, Math.max(1.2, 1600 / Math.max(baseViewport.width, baseViewport.height)));
    const viewport = page.getViewport({ scale });
    const canvas = document.createElement("canvas");
    canvas.width = Math.ceil(viewport.width);
    canvas.height = Math.ceil(viewport.height);
    const context = canvas.getContext("2d", { alpha: false });
    if (!context) throw new Error("浏览器无法创建图片画布。");
    await page.render({ canvasContext: context, viewport }).promise;
    downloadDataUrl(canvas.toDataURL("image/png"), imageFilenameForPick(pick));
    if (pdf && typeof pdf.destroy === "function") pdf.destroy();
  }

  async function loadAccountAdminSummary(workerUrl, targets) {
    targets.status.className = "status-line";
    targets.status.textContent = "正在读取后台信息…";
    targets.refresh.disabled = true;
    try {
      const response = await fetch(`${workerUrl}/account-admin/summary`, {
        cache: "no-store",
        headers: authHeaders(),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) throw new Error(data.detail || "后台读取失败。");
      const users = Array.isArray(data.users) ? data.users : [];
      const files = Array.isArray(data.files) ? data.files : [];
      const dailyPicks = Array.isArray(data.daily_picks) ? data.daily_picks : [];
      accountAdminDailyPicks = new Map(dailyPicks.map((pick) => [String(pick.id || ""), pick]));
      targets.pickCount.textContent = dailyPicks.length ? `${dailyPicks.length} reports` : "";
      targets.picks.innerHTML = dailyPicks.length
        ? dailyPicks.map(adminDailyPickRow).join("")
        : `<div class="empty-state">还没有可用精选。新 PDF 同步后会自动根据宏观/页数/横屏规则筛选。</div>`;
      targets.userCount.textContent = `${users.length} users`;
      targets.users.innerHTML = users.length
        ? users.map(adminUserRow).join("")
        : '<tr><td colspan="5">暂无用户。</td></tr>';
      targets.files.innerHTML = files.length
        ? files.map(adminFileRow).join("")
        : `<div class="empty-state">还没有找到最新文件。可以稍后刷新，或检查 GitHub workflow 是否已完成。</div>`;
      targets.status.textContent = `已更新：${String(data.generated_at || "").replace("T", " ").slice(0, 19)}`;
      targets.status.classList.add("ok");
    } catch (error) {
      targets.status.textContent = error.message || "后台读取失败。";
      targets.status.classList.add("error");
    } finally {
      targets.refresh.disabled = false;
    }
  }

  function showAccountAdminModal(workerUrl) {
    if (!workerUrl || !isSuperSession()) return;
    const existing = document.getElementById("accountAdminModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", accountAdminModalMarkup());

    const modal = document.getElementById("accountAdminModal");
    const close = document.getElementById("accountAdminClose");
    const refresh = document.getElementById("accountAdminRefresh");
    const status = document.getElementById("accountAdminStatus");
    const pickCount = document.getElementById("accountAdminPickCount");
    const picks = document.getElementById("accountAdminPicks");
    const userCount = document.getElementById("accountAdminUserCount");
    const users = document.getElementById("accountAdminUsers");
    const files = document.getElementById("accountAdminFiles");
    const targets = { status, refresh, pickCount, picks, userCount, users, files };

    function finish() {
      modal.remove();
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    refresh.addEventListener("click", () => loadAccountAdminSummary(workerUrl, targets));
    picks.addEventListener("click", async (event) => {
      const row = event.target.closest(".account-admin-pick");
      if (!row) return;
      const pick = accountAdminDailyPicks.get(String(row.dataset.id || ""));
      if (!pick) return;

      const copyButton = event.target.closest(".account-admin-copy-intro");
      if (copyButton) {
        const text = String(pick.intro || "");
        try {
          await navigator.clipboard.writeText(text);
          status.className = "status-line ok";
          status.textContent = "文案已复制。";
        } catch (_error) {
          const textarea = row.querySelector(".account-admin-pick-intro");
          if (textarea) textarea.select();
          status.className = "status-line";
          status.textContent = "已选中文案，可以手动复制。";
        }
        return;
      }

      const downloadButton = event.target.closest(".account-admin-report-download");
      const imageButton = event.target.closest(".account-admin-cover-save");
      if (!downloadButton && !imageButton) return;

      const button = downloadButton || imageButton;
      const progress = row.querySelector(".account-admin-progress");
      const cancel = row.querySelector(".account-admin-cancel");
      const controller = new AbortController();
      button.disabled = true;
      if (cancel) {
        cancel.hidden = false;
        cancel.disabled = false;
        cancel.onclick = () => controller.abort();
      }
      resetDownloadProgress(progress);
      status.className = "status-line";
      status.textContent = downloadButton ? "正在下载精选报告…" : "正在读取 PDF 并生成第一页图片…";
      try {
        const blob = await fetchAccountAdminReportBlob(workerUrl, pick, progress, controller.signal);
        if (downloadButton) {
          triggerBlobDownload(blob, "", pick.filename || `${pick.id}.pdf`);
          status.textContent = "报告下载已开始。";
        } else {
          await saveFirstPageImageFromPdfBlob(blob, pick);
          status.textContent = "第一页图片已保存。";
        }
        status.classList.add("ok");
      } catch (error) {
        if (error && error.name === "AbortError") {
          status.textContent = "操作已取消。";
        } else {
          status.textContent = error.message || "操作失败。";
          status.classList.add("error");
        }
      } finally {
        button.disabled = false;
        if (cancel) {
          cancel.hidden = true;
          cancel.onclick = null;
        }
      }
    });
    files.addEventListener("click", async (event) => {
      const button = event.target.closest(".account-admin-download");
      if (!button) return;
      const kind = button.dataset.kind;
      const key = button.dataset.key || "";
      const repo = button.dataset.repo || "";
      const name = button.dataset.name || "download";
      const endpoint = kind === "artifact"
        ? `${workerUrl}/account-admin/github-artifact?id=${encodeURIComponent(key)}`
        : `${workerUrl}/account-admin/github-file?path=${encodeURIComponent(key)}${repo ? `&repo=${encodeURIComponent(repo)}` : ""}`;
      const row = button.closest(".account-admin-file");
      const progress = row && row.querySelector(".account-admin-progress");
      const cancel = row && row.querySelector(".account-admin-cancel");
      const controller = new AbortController();
      button.disabled = true;
      if (cancel) {
        cancel.hidden = false;
        cancel.disabled = false;
        cancel.onclick = () => controller.abort();
      }
      resetDownloadProgress(progress);
      status.className = "status-line";
      status.textContent = "正在准备下载…";
      try {
        const response = await fetch(endpoint, { headers: authHeaders(), signal: controller.signal });
        if (!response.ok) {
          const data = await response.json().catch(() => ({}));
          throw new Error(data.detail || `下载失败 (${response.status})。`);
        }
        const blob = await responseBlobWithProgress(response, progress);
        triggerBlobDownload(blob, response.headers.get("Content-Disposition"), name);
        status.textContent = "下载已开始。";
        status.classList.add("ok");
      } catch (error) {
        if (error && error.name === "AbortError") {
          status.textContent = "下载已取消。";
        } else {
          status.textContent = error.message || "下载失败。";
          status.classList.add("error");
        }
      } finally {
        button.disabled = false;
        if (cancel) {
          cancel.hidden = true;
          cancel.onclick = null;
        }
      }
    });

    loadAccountAdminSummary(workerUrl, targets);
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
      window.alert("Private tools are temporarily unavailable.");
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
          setAdminPlainKey(input.value);
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

  function getRememberedDownloadPassword() {
    try {
      return localStorage.getItem(DOWNLOAD_PASSWORD_KEY) || "";
    } catch (_error) {
      return "";
    }
  }

  function setRememberedDownloadPassword(value) {
    try {
      localStorage.setItem(DOWNLOAD_PASSWORD_KEY, String(value || ""));
    } catch (_error) {
      // Ignore private browsing/localStorage restrictions.
    }
  }

  function clearRememberedDownloadPassword() {
    try {
      localStorage.removeItem(DOWNLOAD_PASSWORD_KEY);
    } catch (_error) {
      // Ignore private browsing/localStorage restrictions.
    }
  }

  function initAdminGate(workerUrl) {
    const gate = document.getElementById("adminGate");
    if (!gate) return;
    function update() {
      gate.classList.toggle("is-unlocked", privateToolsUnlocked());
    }
    update();
    document.addEventListener("kcdesk-admin-change", update);
    document.addEventListener("kcdesk-auth-change", update);
    gate.addEventListener("click", () => {
      if (isSuperSession()) showAccountAdminModal(workerUrl);
      else showAdminLogin(workerUrl);
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
    const url = reportPageUrl(item.id);
    return `
      <a class="report-row report-link${available ? "" : " is-archived"}" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="pill">${escapeHtml(bank)}</span>
        <span class="date-text">${escapeHtml(displayDate(item.date_folder))}</span>
        <span class="title-text">
          <span class="title-en">${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="industry-text">${escapeHtml(industry)}</span>
        <span class="size-text${available ? "" : " archived"}">${escapeHtml(status)}</span>
      </a>
    `;
  }

  function relatedRow(item) {
    const available = isPdfAvailable(item);
    const zh = titleZhText(item);
    const url = reportPageUrl(item.id);
    return `
      <a class="related-row report-link${available ? "" : " is-archived"}" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(titleText(item))}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(bankLabel(item))} · ${escapeHtml(displayDate(item.date_folder))} · ${escapeHtml(inferIndustry(item))}${available ? "" : " · Text only"}</span>
      </a>
    `;
  }

  function externalMeta(item) {
    const meta = [item.institution, item.date, item.file_type]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
    return meta;
  }

  function authorityKindLabel(kind) {
    return kind === "foreign-rt" ? "实时外文" : "普通外文";
  }

  function authorityMeta(item) {
    const meta = [
      authorityKindLabel(item.kind),
      item.institution,
      item.date,
      item.page_count ? `${item.page_count}页` : "",
      item.language,
    ]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
    return meta;
  }

  function externalRow(item) {
    const meta = externalMeta(item);
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    const url = externalPageUrl(item, "");
    return `
      <a class="related-row external-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function externalTitleMatchesQuery(item, query) {
    const cleanQuery = normalize(query);
    if (!cleanQuery) return false;
    return textMatches(normalize([item.title, item.title_cn].join(" ")), cleanQuery);
  }

  function reportAMeta(item) {
    return [
      item.institution,
      item.date,
      item.category,
      item.page_count ? `${item.page_count}页` : "",
      item.author,
    ]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
  }

  function reportARow(item) {
    const meta = reportAMeta(item);
    const url = externalPageUrl({ ...item, source: REPORT_A_SOURCE }, "");
    return `
      <a class="related-row report-a-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function authorityRow(item) {
    const meta = authorityMeta(item);
    const url = externalPageUrl({ ...item, source: AUTHORITY_SOURCE }, "");
    return `
      <a class="related-row authority-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
      </a>
    `;
  }

  function isNativeNewTabLink(row) {
    return row && row.tagName === "A" && row.getAttribute("target") === "_blank" && row.getAttribute("href");
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

    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);

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
        maybeRunAuthoritySearch(input.value.trim());
        return;
      }
      results.innerHTML = visible.map((entry) => resultRow(entry.item)).join("");
      results.scrollTop = 0;
      maybeRunAuthoritySearch(input.value.trim());
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
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      openReportPage(row.dataset.id);
    });

    // --- 其他报告 integration ---------------------------------------------
    // Live search through the Worker proxy. Rows open the same password-gated
    // detail flow used by primary reports.
    const externalUrl = workerUrl;
    const externalSection = document.getElementById("externalSection");
    const externalResults = document.getElementById("externalResults");
    const externalCount = document.getElementById("externalCount");
    const externalStatus = document.getElementById("externalStatus");
    const reportASection = document.getElementById("reportASection");
    const reportAResults = document.getElementById("reportAResults");
    const reportACount = document.getElementById("reportACount");
    const reportAStatus = document.getElementById("reportAStatus");
    const authoritySection = document.getElementById("authoritySection");
    const authorityResults = document.getElementById("authorityResults");
    const authorityCount = document.getElementById("authorityCount");
    const authorityStatus = document.getElementById("authorityStatus");
    let externalTimer = 0;
    let externalToken = 0;
    let reportAToken = 0;
    let authorityToken = 0;
    let externalSearchSettled = false;
    let externalTitleMatchCount = 0;
    let externalQuery = "";
    let authorityQuery = "";
    const externalItems = new Map();
    const authorityItems = new Map();

    function setExternalStatus(text, kind) {
      if (!externalStatus) return;
      externalStatus.className = kind ? `status-line ${kind}` : "status-line";
      externalStatus.textContent = text || "";
    }

    function setReportAStatus(text, kind) {
      if (!reportAStatus) return;
      reportAStatus.className = kind ? `status-line ${kind}` : "status-line";
      reportAStatus.textContent = text || "";
    }

    function hideReportAResults() {
      reportAToken += 1;
      if (reportASection) reportASection.hidden = true;
      if (reportAResults) reportAResults.innerHTML = "";
      if (reportACount) reportACount.textContent = "";
      setReportAStatus("");
    }

    function setAuthorityStatus(text, kind) {
      if (!authorityStatus) return;
      authorityStatus.className = kind ? `status-line ${kind}` : "status-line";
      authorityStatus.textContent = text || "";
    }

    function hideAuthorityResults() {
      authorityQuery = "";
      authorityToken += 1;
      if (authoritySection) authoritySection.hidden = true;
      if (authorityResults) authorityResults.innerHTML = "";
      authorityItems.clear();
      if (authorityCount) authorityCount.textContent = "";
      setAuthorityStatus("");
    }

    function maybeRunAuthoritySearch(query) {
      const cleanQuery = String(query || "").trim();
      if (!cleanQuery || externalQuery !== cleanQuery || !externalSearchSettled || externalTitleMatchCount > 0) {
        hideAuthorityResults();
        return;
      }
      if (authorityQuery === cleanQuery && authorityItems.size) return;
      runAuthoritySearch(cleanQuery);
    }

    async function runExternalSearch(query) {
      if (!externalSection || !externalResults) return;
      if (!externalUrl || !query) {
        externalQuery = "";
        externalSearchSettled = true;
        externalTitleMatchCount = 0;
        externalSection.hidden = true;
        externalResults.innerHTML = "";
        externalItems.clear();
        if (externalCount) externalCount.textContent = "";
        setExternalStatus("");
        hideAuthorityResults();
        return;
      }
      const token = ++externalToken;
      externalQuery = query;
      externalSearchSettled = false;
      externalTitleMatchCount = 0;
      hideAuthorityResults();
      externalSection.hidden = false;
      if (externalCount) externalCount.textContent = "搜索中…";
      setExternalStatus("");
      externalResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索其他报告…</span>
        </div>
      `;
      try {
        const response = await fetch(
          `${externalUrl}/external/search?q=${encodeURIComponent(query)}`,
          { cache: "no-store" },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (token !== externalToken) return; // a newer query superseded this one
        const items = Array.isArray(data.items) ? data.items : [];
        externalItems.clear();
        items.forEach((item) => externalItems.set(String(item.id), item));
        externalTitleMatchCount = items.filter((item) => externalTitleMatchesQuery(item, query)).length;
        externalSearchSettled = true;
        if (externalCount) externalCount.textContent = items.length ? `${items.length} 条` : "";
        externalResults.innerHTML = items.length
          ? items.map(externalRow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
        maybeRunAuthoritySearch(query);
      } catch (error) {
        if (token !== externalToken) return;
        externalTitleMatchCount = 0;
        externalSearchSettled = true;
        if (externalCount) externalCount.textContent = "";
        externalResults.innerHTML = "";
        setExternalStatus(error.message || "搜索暂不可用。", "error");
        maybeRunAuthoritySearch(query);
      }
    }

    async function runReportASearch(query) {
      if (!reportASection || !reportAResults) return;
      if (!externalUrl || !query) {
        hideReportAResults();
        return;
      }
      const token = ++reportAToken;
      reportASection.hidden = false;
      if (reportACount) reportACount.textContent = "搜索中…";
      setReportAStatus("");
      reportAResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索报告A…</span>
        </div>
      `;
      try {
        const response = await fetch(
          `${externalUrl}/report-a/search?q=${encodeURIComponent(query)}`,
          { cache: "no-store" },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (token !== reportAToken) return;
        const items = Array.isArray(data.items) ? data.items : [];
        if (reportACount) reportACount.textContent = items.length ? `${items.length} 条` : "";
        reportAResults.innerHTML = items.length
          ? items.map(reportARow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
      } catch (error) {
        if (token !== reportAToken) return;
        if (reportACount) reportACount.textContent = "";
        reportAResults.innerHTML = "";
        setReportAStatus(error.message || "搜索暂不可用。", "error");
      }
    }

    async function runAuthoritySearch(query) {
      if (!authoritySection || !authorityResults) return;
      if (!externalUrl || !query) {
        hideAuthorityResults();
        return;
      }
      const token = ++authorityToken;
      authorityQuery = query;
      authoritySection.hidden = false;
      if (authorityCount) authorityCount.textContent = "搜索中…";
      setAuthorityStatus("");
      authorityResults.innerHTML = `
        <div class="loading-state">
          <span class="loading-spinner" aria-hidden="true"></span>
          <span>正在搜索高权报告…</span>
        </div>
      `;
      try {
        const response = await fetch(
          `${externalUrl}/authority/search?q=${encodeURIComponent(query)}`,
          { cache: "no-store" },
        );
        if (!response.ok) throw new Error(`搜索失败 (${response.status})`);
        const data = await response.json();
        if (token !== authorityToken) return;
        const items = Array.isArray(data.items) ? data.items : [];
        authorityItems.clear();
        items.forEach((item) => authorityItems.set(String(item.id), item));
        if (authorityCount) authorityCount.textContent = items.length ? `${items.length} 条` : "";
        authorityResults.innerHTML = items.length
          ? items.map(authorityRow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
      } catch (error) {
        if (token !== authorityToken) return;
        if (authorityCount) authorityCount.textContent = "";
        authorityResults.innerHTML = "";
        setAuthorityStatus(error.message || "搜索暂不可用。", "error");
      }
    }

    function scheduleExternalSearch() {
      window.clearTimeout(externalTimer);
      const query = input.value.trim();
      externalTimer = window.setTimeout(() => {
        runExternalSearch(query);
        runReportASearch(query);
      }, 400);
    }

    input.addEventListener("input", scheduleExternalSearch);
    clearFilters.addEventListener("click", () => {
      runExternalSearch("");
      hideReportAResults();
      hideAuthorityResults();
    });
    externalResults.addEventListener("click", (event) => {
      const row = event.target.closest(".external-row");
      if (!row) return;
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      const item = externalItems.get(String(row.dataset.id));
      if (item) openInNewTab(externalPageUrl(item, ""));
    });
    if (authorityResults) {
      authorityResults.addEventListener("click", (event) => {
        const row = event.target.closest(".authority-row");
        if (!row) return;
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
        const item = authorityItems.get(String(row.dataset.id));
        if (item) openInNewTab(externalPageUrl({ ...item, source: AUTHORITY_SOURCE }, ""));
      });
    }

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

  function triggerBlobDownload(blob, disposition, fallbackName) {
    const objectUrl = URL.createObjectURL(blob);
    const link = document.createElement("a");
    link.href = objectUrl;
    link.download = filenameFromDisposition(disposition, fallbackName);
    document.body.appendChild(link);
    link.click();
    link.remove();
    URL.revokeObjectURL(objectUrl);
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

  function docDateSortValue(item) {
    return Number((isoDateFromValue(item.date) || itemDate(item)).replace(/-/g, "")) || 0;
  }

  function relatedQueryForDoc(item) {
    const title = [item.title_cn, item.title].filter(Boolean).join(" ");
    const chunks = title
      .split(/[\s,，:：;；|｜/\\()[\]（）【】「」"'“”‘’]+/u)
      .map((part) => part.trim())
      .filter((part) => part.length >= 2 && part.length <= 32)
      .slice(0, 4);
    const tokens = importantTokens(`${title} ${item.institution || ""} ${item.category || ""} ${item.report_type || ""}`)
      .filter((token) => token.length <= 24)
      .slice(0, 5);
    const merged = [...chunks, ...tokens].filter(Boolean);
    const deduped = [];
    const seen = new Set();
    for (const value of merged) {
      const key = normalize(value);
      if (!key || seen.has(key)) continue;
      seen.add(key);
      deduped.push(value);
    }
    return (deduped.join(" ") || title || item.institution || "").slice(0, 120).trim();
  }

  function catalogRelatedForDoc(current, items, searchTextById, limit = 4) {
    const currentIndustry = inferIndustry(current);
    const currentInstitution = normalize(current.institution || "");
    const currentDate = docDateSortValue(current);
    const keywords = queryTokens([
      relatedQueryForDoc(current),
      current.title,
      current.title_cn,
      current.institution,
      current.category,
      current.report_type,
    ].join(" "))
      .filter((token) => token.length >= 2 && !STOPWORDS.has(token) && !/^\d{1,3}$/.test(token))
      .slice(0, 18);

    return items
      .map((item) => {
        let score = 0;
        if (currentIndustry !== "Other" && inferIndustry(item) === currentIndustry) score += 30;
        if (currentInstitution && normalize(bankLabel(item)).includes(currentInstitution)) score += 20;
        if (currentDate && Math.abs(dateSortValue(item) - currentDate) <= 7) score += 4;

        const title = normalize(`${item.title || ""} ${item.title_zh || ""}`);
        const meta = normalize(metadataText(item));
        const text = searchTextById.get(item.id) || "";
        for (const token of keywords) {
          if (title.includes(token)) score += 10;
          if (meta.includes(token)) score += 4;
          if (text.includes(token)) score += 2;
        }
        return { item, score };
      })
      .filter((entry) => entry.score > 0)
      .sort((a, b) => {
        if (b.score !== a.score) return b.score - a.score;
        return dateSortValue(b.item) - dateSortValue(a.item);
      })
      .slice(0, limit)
      .map((entry) => entry.item);
  }

  async function fetchDocRelatedSource(workerUrl, endpoint, query, source, current, limit) {
    if (!workerUrl || !query) return [];
    const response = await fetch(`${workerUrl}/${endpoint}?q=${encodeURIComponent(query)}`, { cache: "no-store" });
    if (!response.ok) return [];
    const data = await response.json().catch(() => ({}));
    const items = Array.isArray(data.items) ? data.items : [];
    return items
      .map((item) => ({ ...item, source: item.source || source }))
      .filter((item) => !(item.source === current.source && String(item.id) === String(current.id)))
      .slice(0, limit);
  }

  function externalRelatedMarkup() {
    return `
      <section class="related-section external-related-section" id="externalRelatedSection" hidden aria-labelledby="externalRelatedTitle">
        <div class="related-heading">
          <h3 id="externalRelatedTitle">Related Reports</h3>
        </div>
        <div id="externalRelatedStatus" class="status-line" aria-live="polite"></div>
        <div class="related-list" id="externalRelatedList"></div>
      </section>
    `;
  }

  function docRelatedRow(item) {
    if (item.source === EXTERNAL_SOURCE) return externalRow(item);
    if (item.source === REPORT_A_SOURCE) return reportARow(item);
    if (item.source === AUTHORITY_SOURCE) return authorityRow(item);
    return relatedRow(item);
  }

  async function initExternalRelated(item, workerUrl, catalogItems, searchTextById) {
    const section = document.getElementById("externalRelatedSection");
    const list = document.getElementById("externalRelatedList");
    const status = document.getElementById("externalRelatedStatus");
    if (!section || !list || !status) return;

    const query = relatedQueryForDoc(item);
    const rows = [];
    const seen = new Set();
    function append(sourceItems, source) {
      for (const sourceItem of sourceItems) {
        const key = `${source}:${sourceItem.id}`;
        if (!sourceItem.id || seen.has(key)) continue;
        seen.add(key);
        rows.push({ ...sourceItem, source });
      }
    }

    section.hidden = false;
    status.className = "status-line";
    status.textContent = "正在推荐相关报告…";
    list.innerHTML = `
      <div class="loading-state">
        <span class="loading-spinner" aria-hidden="true"></span>
        <span>正在推荐相关报告…</span>
      </div>
    `;

    append(catalogRelatedForDoc(item, catalogItems, searchTextById, 4), "catalog");

    const [externalResult, reportAResult, authorityResult] = await Promise.allSettled([
      fetchDocRelatedSource(workerUrl, "external/search", query, EXTERNAL_SOURCE, item, 4),
      fetchDocRelatedSource(workerUrl, "report-a/search", query, REPORT_A_SOURCE, item, 3),
      fetchDocRelatedSource(workerUrl, "authority/search", query, AUTHORITY_SOURCE, item, 3),
    ]);

    if (externalResult.status === "fulfilled") append(externalResult.value, EXTERNAL_SOURCE);
    if (reportAResult.status === "fulfilled") append(reportAResult.value, REPORT_A_SOURCE);
    if (authorityResult.status === "fulfilled") append(authorityResult.value, AUTHORITY_SOURCE);

    const rendered = rows.slice(0, 14);
    if (!rendered.length) {
      section.hidden = true;
      return;
    }
    status.textContent = "";
    list.innerHTML = rendered.map(docRelatedRow).join("");
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
    if (/configured/i.test(text)) return "PDF download is temporarily unavailable. Please try again later.";
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

  function accountAccessMarkup(item = {}) {
    return `
      <section class="account-access" id="accountAccess" hidden>
        <h3>Account access</h3>
        <p class="subtle" id="accountAccessHint">登录后可查看账号下载权限；开通权限请联系微信 ${escapeHtml(CONTACT_WECHAT)}。</p>
        <div class="account-access-actions">
          <button class="secondary-button" id="openAccountPanel" type="button">登录 / 账号</button>
          <button class="primary" id="accountDownloadReport" type="button" hidden>账号下载</button>
        </div>
        <div id="accountAccessStatus" class="status-line" aria-live="polite"></div>
      </section>
    `;
  }

  function setLineStatus(target, text, kind) {
    if (!target) return;
    target.className = kind ? `status-line ${kind}` : "status-line";
    target.textContent = text || "";
  }

  async function fetchReportAccess(workerUrl, item, source) {
    const session = loadAuthSession();
    if (!session) return null;
    const response = await fetch(
      `${workerUrl}/entitlement?report_id=${encodeURIComponent(item.id)}&source=${encodeURIComponent(source)}`,
      { cache: "no-store", headers: authHeaders() },
    );
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      if (response.status === 401) clearAuthSession();
      throw new Error(data.detail || "账号状态读取失败。");
    }
    return data;
  }

  async function downloadCatalogWithAccount(workerUrl, item, statusTarget) {
    statusTarget("正在检查账号权益…");
    const response = await fetch(`${workerUrl}/download`, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify({ id: item.id }),
    });
    if (!response.ok) {
      const data = await response.json().catch(() => ({}));
      if (response.status === 401) clearAuthSession();
      throw new Error(downloadErrorMessage(response.status, data.error || "Download failed.", data));
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
    statusTarget("下载已开始。", "ok");
  }

  function initReportAccessControls(item, workerUrl, source, downloadHandler) {
    const panel = document.getElementById("accountAccess");
    if (!panel || !workerUrl) return;
    const openAccount = document.getElementById("openAccountPanel");
    const accountDownload = document.getElementById("accountDownloadReport");
    const hint = document.getElementById("accountAccessHint");
    const status = document.getElementById("accountAccessStatus");
    const context = { item, source };

    function statusTarget(text, kind) {
      setLineStatus(status, text, kind);
    }

    async function refresh() {
      const session = loadAuthSession();
      panel.hidden = false;
      hint.textContent = `登录后可查看账号下载权限；开通权限请联系微信 ${CONTACT_WECHAT}。`;
      accountDownload.hidden = true;
      if (!session) {
        statusTarget(`如需开通权限，请联系微信 ${CONTACT_WECHAT}。`);
        return;
      }
      statusTarget("正在读取账号权益…");
      try {
        const access = await fetchReportAccess(workerUrl, item, source);
        if (access && access.can_download) {
          accountDownload.hidden = false;
          statusTarget("当前账号已解锁此报告，可直接下载。", "ok");
        } else {
          statusTarget(`当前账号尚未解锁此报告。如需开通权限，请联系微信 ${CONTACT_WECHAT}。`);
        }
      } catch (error) {
        statusTarget(error.message || "账号状态读取失败。", "error");
      }
    }

    openAccount.addEventListener("click", () => showAccountModal(workerUrl, context));
    accountDownload.addEventListener("click", async () => {
      accountDownload.disabled = true;
      try {
        await downloadHandler(statusTarget);
      } catch (error) {
        statusTarget(error.message || "下载失败。", "error");
      } finally {
        accountDownload.disabled = false;
      }
    });
    document.addEventListener("kcdesk-auth-change", refresh);
    refresh();
  }

  function reportPageUrl(id, options = {}) {
    const url = new URL("report.html", window.location.href);
    url.searchParams.set("id", id);
    if (options.password) url.searchParams.set("password", options.password);
    return url.toString();
  }

  function openInNewTab(url) {
    const opened = window.open(url, "_blank");
    if (opened) {
      opened.opener = null;
    }
  }

  function openReportPage(id) {
    openInNewTab(reportPageUrl(id));
  }

  function deliveryPageUrl(id, password) {
    return reportPageUrl(id, { password });
  }

  function externalPageUrl(item, password, options = {}) {
    const url = new URL("doc.html", window.location.href);
    url.searchParams.set("id", item.id);
    if (item.source) url.searchParams.set("source", item.source);
    if (password) url.searchParams.set("password", password);
    if (item.title) url.searchParams.set("title", item.title);
    if (item.title_cn) url.searchParams.set("title_cn", item.title_cn);
    if (item.institution) url.searchParams.set("institution", item.institution);
    if (item.date) url.searchParams.set("date", item.date);
    if (item.file_type) url.searchParams.set("file_type", item.file_type);
    if (item.kind) url.searchParams.set("kind", item.kind);
    if (item.page_count) url.searchParams.set("page_count", item.page_count);
    if (item.report_type) url.searchParams.set("report_type", item.report_type);
    if (item.language) url.searchParams.set("language", item.language);
    if (item.category) url.searchParams.set("category", item.category);
    if (item.author) url.searchParams.set("author", item.author);
    if (item.rating) url.searchParams.set("rating", item.rating);
    return url.toString();
  }

  async function requestReportPassword(workerUrl, id) {
    const token = getAdminToken();
    if (!token && !isSuperSession()) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ id, token }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        if (response.status === 401) clearAdminToken();
        const fallback = response.status >= 500 ? getAdminPlainKey() : "";
        if (fallback) return { id, password: fallback };
        throw new Error(data.error || "Could not generate delivery link.");
      }
      return data;
    } catch (error) {
      const fallback = getAdminPlainKey();
      if (fallback) return { id, password: fallback };
      throw error;
    }
  }

  async function requestExternalPassword(workerUrl, id, source = EXTERNAL_SOURCE) {
    const token = getAdminToken();
    if (!token && !isSuperSession()) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ id, token, source }),
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        if (response.status === 401) clearAdminToken();
        const fallback = response.status >= 500 ? getAdminPlainKey() : "";
        if (fallback) return { id, password: fallback };
        throw new Error(data.error || "Could not generate delivery link.");
      }
      return data;
    } catch (error) {
      const fallback = getAdminPlainKey();
      if (fallback) return { id, password: fallback };
      throw error;
    }
  }

  function initDetailAdmin(item, workerUrl) {
    const panel = document.getElementById("adminPanel");
    const generate = document.getElementById("generateDeliveryLink");
    const linkInput = document.getElementById("deliveryLinkInput");
    const copy = document.getElementById("copyDeliveryLink");
    const status = document.getElementById("deliveryStatus");
    if (!panel || !generate || !linkInput || !copy || !status) return;

    function refresh() {
      panel.hidden = !privateToolsUnlocked();
    }

    refresh();
    document.addEventListener("kcdesk-admin-change", refresh);
    document.addEventListener("kcdesk-auth-change", refresh);

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

  function renderDetail(item, config, catalogItems, searchTextById, options = {}) {
    const detail = document.getElementById("detail");
    const workerUrl = workerBaseUrl(config);
    const available = isPdfAvailable(item);
    const setupWarning = workerUrl || !available
      ? ""
      : '<div class="setup-warning">PDF download is temporarily unavailable. Please try again later.</div>';
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
        ${workerUrl ? accountAccessMarkup(item) : ""}
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
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      openReportPage(row.dataset.id);
    });

    initDetailAdmin(item, workerUrl);
    initReportAccessControls(item, workerUrl, "catalog", (statusTarget) => (
      downloadCatalogWithAccount(workerUrl, item, statusTarget)
    ));

    if (!available) return;

    const form = document.getElementById("unlockForm");
    const input = document.getElementById("passwordInput");
    const status = document.getElementById("downloadStatus");
    const button = form.querySelector("button");
    const deliveryPassword = String(options.password || "");
    const rememberedPassword = deliveryPassword || getRememberedDownloadPassword();
    if (rememberedPassword) {
      input.value = rememberedPassword;
      if (deliveryPassword) {
        setRememberedDownloadPassword(deliveryPassword);
        status.textContent = "Password filled from delivery link.";
        const cleanUrl = new URL(window.location.href);
        cleanUrl.searchParams.delete("password");
        cleanUrl.searchParams.delete("deliver");
        window.history.replaceState({}, "", cleanUrl.toString());
      } else {
        status.textContent = "Password remembered on this device.";
      }
    }

    async function submitDownload(event) {
      if (event) event.preventDefault();
      status.className = "status-line";
      if (!workerUrl) {
        status.textContent = "PDF download is temporarily unavailable. Please try again later.";
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
          if (response.status === 401) clearRememberedDownloadPassword();
          throw new Error(downloadErrorMessage(response.status, message, data));
        }

        const blob = await response.blob();
        triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
        setRememberedDownloadPassword(input.value);
        status.textContent = "Download started.";
        status.classList.add("ok");
      } catch (error) {
        status.textContent = error.message || "Download failed.";
        status.classList.add("error");
      } finally {
        button.disabled = false;
      }
    }

    form.addEventListener("submit", submitDownload);
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
    initAccountGate(workerUrl);
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
    renderDetail(item, config, items, searchTextById, {
      password: params.get("password") || "",
    });
  }

  function externalItemFromParams(params) {
    const rawSource = params.get("source");
    const source = rawSource === AUTHORITY_SOURCE
      ? AUTHORITY_SOURCE
      : (rawSource === REPORT_A_SOURCE ? REPORT_A_SOURCE : EXTERNAL_SOURCE);
    return {
      id: String(params.get("id") || "").trim(),
      source,
      title: params.get("title") || "Report",
      title_cn: params.get("title_cn") || "",
      institution: params.get("institution") || "",
      date: params.get("date") || "",
      file_type: params.get("file_type") || "",
      kind: params.get("kind") || "",
      page_count: params.get("page_count") || "",
      report_type: params.get("report_type") || "",
      language: params.get("language") || "",
      category: params.get("category") || "",
      author: params.get("author") || "",
      rating: params.get("rating") || "",
    };
  }

  function isAuthorityItem(item) {
    return item && item.source === AUTHORITY_SOURCE;
  }

  function isReportAItem(item) {
    return item && item.source === REPORT_A_SOURCE;
  }

  function isContactOnlyItem(item) {
    return isAuthorityItem(item) || isReportAItem(item);
  }

  function docSourceLabel(item) {
    if (isAuthorityItem(item)) return "高权报告";
    if (isReportAItem(item)) return "报告A";
    return "其他报告";
  }

  function docEndpoint(item) {
    return isAuthorityItem(item) ? "authority" : "external";
  }

  function validDocId(item) {
    if (isAuthorityItem(item)) return /^(foreign|foreign-rt):[0-9]{1,25}$/.test(item.id);
    if (isReportAItem(item)) return /^report-a:[a-f0-9]{16,64}$/i.test(item.id);
    return /^[0-9]{6,25}$/.test(item.id);
  }

  async function fetchExternalPdf(workerUrl, item, password, statusTarget, options = {}) {
    statusTarget("正在获取报告…");
    const response = await fetch(`${workerUrl}/${docEndpoint(item)}/pdf`, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...(options.auth ? authHeaders() : {}) },
      cache: "no-store",
      body: JSON.stringify({ id: item.id, password: password || "" }),
    });
    if (response.status === 202) {
      let data = {};
      try {
        data = await response.json();
      } catch (_error) {
        // Keep the generic pending state.
      }
      return { pending: true, wait_seconds: Number(data.wait_seconds || 0) || 480 };
    }
    if (!response.ok) {
      let message = `下载失败 (${response.status})`;
      try {
        const data = await response.json();
        if (data.error) message = data.error;
      } catch (_error) {
        // Keep generic message.
      }
      if (response.status === 401) clearRememberedDownloadPassword();
      throw new Error(message);
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), `${item.id}.pdf`);
    setRememberedDownloadPassword(password);
    statusTarget("下载已开始。", "ok");
    return { pending: false };
  }

  function pollExternalDetail(workerUrl, id, password, statusTarget, onReady) {
    let attempts = 0;
    const maxAttempts = 40; // 10 minutes at 15s intervals
    const startedAt = Date.now();
    statusTarget("报告正在准备，页面每 15 秒自动检测一次。准备好后会自动开始下载。");
    const timer = window.setInterval(async () => {
      attempts += 1;
      const elapsedSeconds = Math.max(15, Math.round((Date.now() - startedAt) / 1000));
      const elapsedText = elapsedSeconds >= 60
        ? `${Math.floor(elapsedSeconds / 60)} 分 ${elapsedSeconds % 60} 秒`
        : `${elapsedSeconds} 秒`;
      if (attempts > maxAttempts) {
        window.clearInterval(timer);
        statusTarget(`报告准备时间超过预期。请保留这个页面，稍后再次点击下载；如果多次失败请联系 ${CONTACT_WECHAT}。`, "error");
        return;
      }
      try {
        statusTarget(`报告仍在准备中，已等待 ${elapsedText}。页面会继续自动检测。`);
        const response = await fetch(`${workerUrl}/external/status?id=${encodeURIComponent(id)}`, {
          cache: "no-store",
        });
        const data = await response.json();
        if (data.ready) {
          window.clearInterval(timer);
          statusTarget("报告已就绪，正在下载…", "ok");
          onReady();
        } else if (data.status === "failed") {
          window.clearInterval(timer);
          statusTarget(data.message || `报告准备失败，请联系 ${CONTACT_WECHAT}。`, "error");
        }
      } catch (_error) {
        // Keep polling while the background grab runs.
      }
    }, 15000);
  }

  async function downloadExternalWithAccount(workerUrl, item, statusTarget) {
    const result = await fetchExternalPdf(workerUrl, item, "", statusTarget, { auth: true });
    if (result.pending) {
      statusTarget("报告正在准备，通常约 3-8 分钟。页面会自动检测，准备好后开始下载。");
      pollExternalDetail(workerUrl, item.id, "", statusTarget, () => (
        downloadExternalWithAccount(workerUrl, item, statusTarget)
      ));
    }
  }

  async function initExternalDetail() {
    const params = new URLSearchParams(window.location.search);
    const item = externalItemFromParams(params);
    const target = document.getElementById("externalDetail");
    if (!validDocId(item)) {
      target.innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }

    const [config, catalog, searchIndex] = await Promise.all([
      loadOptionalJson("data/config.json", {}),
      loadOptionalJson("data/catalog.json", { items: [] }),
      loadOptionalJson("data/search_index.json", { items: [] }),
    ]);
    const workerUrl = workerBaseUrl(config);
    const catalogItems = Array.isArray(catalog.items) ? catalog.items : [];
    const searchTextById = new Map();
    for (const entry of Array.isArray(searchIndex.items) ? searchIndex.items : []) {
      if (entry.id && entry.text) searchTextById.set(entry.id, String(entry.text));
    }
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);

    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    document.title = `${item.title || "Report"} | KC Desk Notes`;
    const detailFields = isAuthorityItem(item)
      ? `
        ${field("Source", docSourceLabel(item))}
        ${field("Category", authorityKindLabel(item.kind))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "-")}
      `
      : (isReportAItem(item) ? `
        ${field("Source", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Category", item.category || "-")}
        ${field("Author", item.author || "-")}
        ${field("Pages", item.page_count ? `${item.page_count}页` : "-")}
      ` : `
        ${field("Source", docSourceLabel(item))}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Type", item.file_type || "-")}
      `);
    const detailHeader = `
      <div>
        <h1 class="detail-title">${escapeHtml(item.title || "Report")}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">${isContactOnlyItem(item) ? `${docSourceLabel(item)}检索线索。` : "Password-protected report delivery."}</p>
      </div>
      <div class="detail-grid">
        ${detailFields}
      </div>
    `;
    if (isContactOnlyItem(item)) {
      const hint = isAuthorityItem(item)
        ? "高权报告仅提供检索线索，无法在本站直接下载。"
        : "报告A仅提供检索线索，本站不直接展示原文或下载文件。";
      target.innerHTML = `
        ${detailHeader}
        <section class="unlock-box authority-contact-box">
          <h3>获取报告</h3>
          <p class="subtle">${escapeHtml(hint)}</p>
          <p class="contact-line">如需原文，请联系微信号：<strong>${escapeHtml(CONTACT_WECHAT)}</strong></p>
        </section>
        ${externalRelatedMarkup()}
      `;
      initExternalRelated(item, workerUrl, catalogItems, searchTextById);
      return;
    }

    const passwordFromLink = params.get("password") || "";
    target.innerHTML = `
      ${detailHeader}
      <form class="unlock-box" id="externalDetailForm">
        <h3>PDF Download</h3>
        <p class="subtle">Enter the report password to download the PDF.</p>
        <div class="password-row">
          <input id="externalDetailPassword" type="password" autocomplete="current-password" placeholder="Password" required>
          <button class="primary" type="submit">Download</button>
        </div>
        <div class="external-wait" id="externalDetailWait" hidden>
          报告正在准备，通常约 3-8 分钟。这个页面会自动检测，文件准备好后会开始下载。
        </div>
        <div id="externalDetailStatus" class="status-line" aria-live="polite"></div>
      </form>
      ${workerUrl ? accountAccessMarkup(item) : ""}
      <section class="admin-panel external-admin-tools" hidden>
        <div class="admin-panel-heading">
          <h3>Delivery link</h3>
          <span>Private</span>
        </div>
        <div class="delivery-row">
          <button class="primary" id="generateExternalDetailDeliveryLink" type="button">Generate</button>
          <input id="externalDetailDeliveryLinkInput" type="text" readonly aria-label="Delivery link">
          <button id="copyExternalDeliveryLink" type="button">Copy</button>
        </div>
        <div id="externalDetailDeliveryStatus" class="status-line" aria-live="polite"></div>
      </section>
      ${externalRelatedMarkup()}
    `;
    initExternalRelated(item, workerUrl, catalogItems, searchTextById);

    const form = document.getElementById("externalDetailForm");
    const input = document.getElementById("externalDetailPassword");
    const button = form.querySelector("button");
    const status = document.getElementById("externalDetailStatus");
    const wait = document.getElementById("externalDetailWait");
    const adminTools = target.querySelector(".external-admin-tools");
    const generate = document.getElementById("generateExternalDetailDeliveryLink");
    const linkInput = document.getElementById("externalDetailDeliveryLinkInput");
    const copy = document.getElementById("copyExternalDeliveryLink");
    const deliveryStatus = document.getElementById("externalDetailDeliveryStatus");

    function setStatus(text, kind) {
      status.className = kind ? `status-line ${kind}` : "status-line";
      status.textContent = text || "";
      wait.hidden = !/准备|等待|自动检测/.test(String(text || ""));
    }

    function refreshAdmin() {
      adminTools.hidden = !privateToolsUnlocked();
    }

    async function submitDownload(event) {
      if (event) event.preventDefault();
      if (!input.value) {
        setStatus("Password is required.", "error");
        return;
      }
      button.disabled = true;
      try {
        const result = await fetchExternalPdf(workerUrl, item, input.value, setStatus);
        if (result.pending) {
          setRememberedDownloadPassword(input.value);
          setStatus("报告正在准备，通常约 3-8 分钟。页面会自动检测，准备好后开始下载。");
          pollExternalDetail(workerUrl, item.id, input.value, setStatus, () => submitDownload());
        }
      } catch (error) {
        setStatus(error.message || "下载失败。", "error");
      } finally {
        button.disabled = false;
      }
    }

    form.addEventListener("submit", submitDownload);
    document.addEventListener("kcdesk-admin-change", refreshAdmin);
    document.addEventListener("kcdesk-auth-change", refreshAdmin);
    refreshAdmin();
    initReportAccessControls(item, workerUrl, item.source, (statusTarget) => (
      downloadExternalWithAccount(workerUrl, item, statusTarget)
    ));

    generate.addEventListener("click", async () => {
      generate.disabled = true;
      linkInput.value = "";
      deliveryStatus.className = "status-line";
      deliveryStatus.textContent = "Generating...";
      try {
        const data = await requestExternalPassword(workerUrl, item.id, item.source);
        linkInput.value = externalPageUrl(item, data.password);
        deliveryStatus.className = "status-line ok";
        deliveryStatus.textContent = "Delivery link generated.";
      } catch (error) {
        deliveryStatus.className = "status-line error";
        deliveryStatus.textContent = error.message || "Could not generate delivery link.";
      } finally {
        generate.disabled = false;
      }
    });

    copy.addEventListener("click", async () => {
      if (!linkInput.value) return;
      try {
        await navigator.clipboard.writeText(linkInput.value);
        deliveryStatus.className = "status-line ok";
        deliveryStatus.textContent = "Copied.";
      } catch (_error) {
        linkInput.select();
        deliveryStatus.className = "status-line";
        deliveryStatus.textContent = "Select and copy the link.";
      }
    });

    const initialPassword = passwordFromLink || getRememberedDownloadPassword();
    if (initialPassword) {
      input.value = initialPassword;
      if (passwordFromLink) {
        setRememberedDownloadPassword(passwordFromLink);
        setStatus("Password filled from delivery link.");
        const cleanUrl = new URL(window.location.href);
        cleanUrl.searchParams.delete("password");
        cleanUrl.searchParams.delete("deliver");
        window.history.replaceState({}, "", cleanUrl.toString());
      } else {
        setStatus("Password remembered on this device.");
      }
    }
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
    const targetUrl = deliveryPageUrl(id, password);
    target.innerHTML = `
      <div>
        <h1 class="detail-title">Opening report...</h1>
        <p class="subtle">This delivery link now opens the report page directly.</p>
      </div>
      <div class="delivery-actions">
        <a class="primary-link" href="${escapeHtml(targetUrl)}">Open report</a>
      </div>
    `;
    window.location.replace(targetUrl);
  }

  const boot = page === "report"
    ? initReport
    : page === "external"
      ? initExternalDetail
      : page === "delivery"
        ? initDelivery
        : initIndex;
  boot().catch((error) => {
    const target = page === "report"
      ? document.getElementById("detail")
      : page === "external"
        ? document.getElementById("externalDetail")
        : page === "delivery"
          ? document.getElementById("delivery")
          : document.getElementById("results");
    if (target) target.innerHTML = `<div class="error-state">${escapeHtml(error.message)}</div>`;
  });
}());
