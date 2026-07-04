(function () {
  const page = document.body.dataset.page;
  const CONTACT_WECHAT = "MacroGate";
  const ADMIN_TOKEN_KEY = "kcdesk_admin_token";
  const ADMIN_PLAIN_KEY = "kcdesk_admin_plain_key";
  const ADMIN_COOKIE_NAME = "kcdesk_admin_token";
  const ADMIN_COOKIE_MAX_AGE = 180 * 24 * 60 * 60;
  const DOWNLOAD_PASSWORD_KEY = "kcdesk_download_password";
  const AUTH_SESSION_KEY = "kcdesk_auth_session";
  const VISITOR_ID_KEY = "kcdesk_visitor_id";
  const AUTHORITY_SOURCE = "authority";
  const REPORT_A_SOURCE = "report-a";
  const EXTERNAL_SOURCE = "external";
  const NEWSFEED_TOPIC_LIMIT = 10000;
  const NEWSFEED_ACCOUNT_USERNAMES = new Set(["jacob"]);
  const NEWSFEED_ACCOUNT_EMAILS = new Set(["jacob@bo-axis.com"]);
  const PDFJS_MODULE_URL = "/assets/vendor/pdfjs/pdf.mjs";
  const PDFJS_WORKER_URL = "/assets/vendor/pdfjs/pdf.worker.mjs";
  let accountAdminDailyPicks = new Map();
  let accountAdminUsersByEmail = new Map();
  let accountAdminAccessOptions = {};
  let pdfJsLoadPromise = null;
  const activeAdminButtonActions = new WeakMap();

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

  const PAGE_RANGE_FILTERS = [
    { value: "under5", label: "5页以下", matches: (pages) => pages > 0 && pages <= 5 },
    { value: "5_10", label: "5-10页", matches: (pages) => pages >= 5 && pages <= 10 },
    { value: "10_20", label: "10-20页", matches: (pages) => pages >= 10 && pages <= 20 },
    { value: "over20", label: "20页以上", matches: (pages) => pages >= 20 },
  ];

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

  function randomVisitorId() {
    if (window.crypto && typeof window.crypto.randomUUID === "function") {
      return window.crypto.randomUUID();
    }
    return `v-${Date.now().toString(36)}-${Math.random().toString(36).slice(2, 12)}`;
  }

  function visitorId() {
    try {
      let value = localStorage.getItem(VISITOR_ID_KEY) || "";
      if (!value) {
        value = randomVisitorId();
        localStorage.setItem(VISITOR_ID_KEY, value);
      }
      return value;
    } catch (_error) {
      return "";
    }
  }

  function currentAnalyticsPath() {
    return `${window.location.pathname}${window.location.search}`.slice(0, 240);
  }

  function trackEvent(workerUrl, type, data = {}) {
    if (!workerUrl) return;
    const payload = {
      type,
      visitor_id: visitorId(),
      path: currentAnalyticsPath(),
      data: {
        page,
        referrer: document.referrer || "",
        ...data,
      },
    };
    try {
      fetch(`${workerUrl}/analytics`, {
        method: "POST",
        cache: "no-store",
        keepalive: true,
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify(payload),
      }).catch(() => {});
    } catch (_error) {
      // Analytics should never block the user flow.
    }
  }

  function analyticsReportPayload(item, source = "catalog") {
    return {
      source,
      report_id: item && item.id || "",
      report_title: item ? (item.title || item.title_zh || item.filename || "") : "",
      institution: item ? (item.institution || item.bank_code || item.bank_name || "") : "",
    };
  }

  function authUserLabel(session) {
    const user = session && session.user;
    if (!user) return "登录";
    return user.username || user.email || "账号";
  }

  function accountRightLabel(row = {}) {
    if (!row || !row.active) return "";
    if (row.access_mode === "all") return "全站报告下载权限";
    if (row.access_mode === "filters") return "条件报告下载权限";
    if (row.plan === "annual") return "年度下载权限";
    if (row.plan === "super" || row.plan === "operator") return "账号下载权限";
    return "下载权限";
  }

  function accountRightExpiryText(row = {}) {
    if (!row || !row.active) return "";
    if (row.lifetime) return "长期有效";
    const end = String(row.current_period_end || "").slice(0, 10);
    return end ? `有效期至 ${end}` : "";
  }

  function accountRightSummary(data = {}) {
    const access = data && data.access;
    if (access && access.active) {
      return [accountRightLabel(access), accountRightExpiryText(access)].filter(Boolean).join("，");
    }
    const entitlement = data && data.entitlement;
    if (entitlement && entitlement.active && (entitlement.plan === "annual" || entitlement.plan === "super" || entitlement.plan === "operator")) {
      return [accountRightLabel(entitlement), accountRightExpiryText(entitlement)].filter(Boolean).join("，");
    }
    return "";
  }

  function isSuperSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user && (user.role === "super" || user.is_super));
  }

  function isOperatorSession(session = loadAuthSession()) {
    const user = session && session.user;
    return Boolean(user && (user.role === "operator" || user.is_operator));
  }

  function canOpenOperationsPanel(session = loadAuthSession()) {
    return isSuperSession(session) || isOperatorSession(session);
  }

  function isNewsfeedSession(session = loadAuthSession()) {
    const user = session && session.user;
    if (!user) return false;
    const username = String(user.username || "").trim().toLowerCase().replace(/^@+/, "");
    const email = String(user.email || "").trim().toLowerCase();
    return isSuperSession(session) || NEWSFEED_ACCOUNT_USERNAMES.has(username) || NEWSFEED_ACCOUNT_EMAILS.has(email);
  }

  function privateToolsUnlocked() {
    return Boolean(getAdminToken() || canOpenOperationsPanel());
  }

  function canUseDeliveryTools(session = loadAuthSession()) {
    if (canOpenOperationsPanel(session)) return true;
    return !session && Boolean(getAdminToken());
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

  function initNewsfeedNav() {
    const links = Array.from(document.querySelectorAll("#newsfeedNav"));
    if (!links.length) return;
    function update() {
      const visible = isNewsfeedSession();
      links.forEach((link) => {
        link.hidden = !visible;
      });
    }
    update();
    document.addEventListener("kcdesk-auth-change", update);
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
              <label id="accountEmailLabel" hidden>邮箱（注册必填）<input id="accountEmail" type="email" autocomplete="email" placeholder="you@example.com"></label>
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
            <form id="accountPasswordForm" class="account-password-form">
              <span>需要改密码可以在这里更新。</span>
              <div class="account-password-grid">
                <input id="accountCurrentPassword" type="password" autocomplete="current-password" placeholder="当前密码" required>
                <input id="accountNewPassword" type="password" autocomplete="new-password" placeholder="新密码" required>
                <input id="accountNewPasswordConfirm" type="password" autocomplete="new-password" placeholder="确认新密码" required>
              </div>
              <button class="secondary-button" id="accountPasswordSubmit" type="submit">修改密码</button>
            </form>
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
    const passwordForm = document.getElementById("accountPasswordForm");
    const currentPassword = document.getElementById("accountCurrentPassword");
    const newPassword = document.getElementById("accountNewPassword");
    const newPasswordConfirm = document.getElementById("accountNewPasswordConfirm");
    const passwordSubmit = document.getElementById("accountPasswordSubmit");
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
        if (adminOpen) {
          adminOpen.hidden = !canOpenOperationsPanel(session);
          adminOpen.textContent = isOperatorSession(session) && !isSuperSession(session) ? "运营后台" : "管理后台";
        }
        setStatus(
          isSuperSession(session)
            ? "已登录，当前账号拥有管理员权限。"
            : (isOperatorSession(session) ? "已登录，当前账号拥有运营权限。" : `已登录。如需开通下载权限，请联系微信 ${CONTACT_WECHAT}。`),
          "ok",
        );
        fetch(`${workerUrl}/entitlement`, { cache: "no-store", headers: authHeaders() })
          .then((response) => response.json())
          .then((data) => {
            const summary = accountRightSummary(data);
            if (summary) setStatus(`账号${summary}。`, "ok");
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
      email.required = mode === "register";
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
    if (passwordForm) {
      passwordForm.addEventListener("submit", async (event) => {
        event.preventDefault();
        if (!loadAuthSession()) {
          setStatus("请先登录。", "error");
          return;
        }
        if (newPassword.value !== newPasswordConfirm.value) {
          setStatus("两次输入的新密码不一致。", "error");
          return;
        }
        passwordSubmit.disabled = true;
        setStatus("正在修改密码…");
        try {
          const response = await fetch(`${workerUrl}/account/password`, {
            method: "POST",
            headers: { "Content-Type": "application/json", ...authHeaders() },
            body: JSON.stringify({
              current_password: currentPassword.value,
              new_password: newPassword.value,
            }),
          });
          const data = await response.json().catch(() => ({}));
          if (!response.ok || !data.token || !data.user) throw new Error(data.detail || "密码修改失败。");
          saveAuthSession({ token: data.token, user: data.user });
          currentPassword.value = "";
          newPassword.value = "";
          newPasswordConfirm.value = "";
          refreshUi();
          setStatus("密码已更新。", "ok");
        } catch (error) {
          setStatus(error.message || "密码修改失败。", "error");
        } finally {
          passwordSubmit.disabled = false;
        }
      });
    }

    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      submit.disabled = true;
      setStatus(mode === "register" ? "正在注册…" : "正在登录…");
      try {
        if (mode === "register" && !email.value.trim()) {
          throw new Error("注册需要绑定邮箱。");
        }
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
        if (mode === "register") {
          const destination = data.email_destination || {};
          if (destination.status === "verified") {
            setStatus("注册成功，邮箱已完成 Cloudflare 收件地址验证。", "ok");
          } else if (destination.status === "pending" && destination.requested) {
            setStatus("注册成功，Cloudflare 已向邮箱发送验证邮件，请在邮箱里点击 Verify email address。", "ok");
          } else if (destination.status === "pending") {
            setStatus("注册成功，邮箱已经在 Cloudflare 待验证列表里，请在邮箱里完成验证。", "ok");
          } else if (destination.status === "failed") {
            setStatus(`注册成功，邮箱已绑定；Cloudflare 验证邮件暂时没有发出：${destination.detail || "请稍后重试。"}`, "error");
          } else if (destination.status === "not_configured") {
            setStatus("注册成功，邮箱已绑定；后续可在 Cloudflare Destination Addresses 完成验证。", "ok");
          }
        }
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

  function accountAdminModalMarkup(options = {}) {
    const title = options.title || "管理后台";
    const showWechat = options.showWechat !== false;
    const showUsers = options.showUsers !== false;
    const showAnalytics = options.showAnalytics !== false;
    return `
      <div class="admin-modal account-admin-modal" id="accountAdminModal" role="dialog" aria-modal="true" aria-labelledby="accountAdminTitle">
        <div class="admin-dialog account-admin-dialog">
          <button class="admin-close" id="accountAdminClose" type="button" aria-label="Close">&times;</button>
          <div class="account-admin-top">
            <h3 id="accountAdminTitle">${escapeHtml(title)}</h3>
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
          <section class="account-admin-section account-admin-wechat-section" id="accountAdminWechatSection" ${showWechat ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>公众号发送时间</strong>
              <span id="accountAdminWechatCount"></span>
            </div>
            <div id="accountAdminWechatSchedule" class="account-admin-wechat-schedule"></div>
          </section>
          <section class="account-admin-section">
            <div class="account-admin-heading">
              <strong>每日文件</strong>
              <span>GitHub latest</span>
            </div>
            <div id="accountAdminFiles" class="account-admin-files"></div>
          </section>
          <section class="account-admin-section" id="accountAdminAnalyticsSection" ${showAnalytics ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>访问与搜索</strong>
              <span id="accountAdminAnalyticsCount"></span>
            </div>
            <div id="accountAdminAnalytics" class="account-admin-analytics"></div>
          </section>
          <section class="account-admin-section" id="accountAdminUsersSection" ${showUsers ? "" : "hidden"}>
            <div class="account-admin-heading">
              <strong>用户信息</strong>
              <span id="accountAdminUserCount"></span>
            </div>
            <form id="accountAdminUserEditor" class="account-admin-user-editor" hidden>
              <div class="account-admin-user-editor-head">
                <strong id="accountAdminUserEditorTitle">编辑用户权限</strong>
                <button class="secondary-button" id="accountAdminUserEditorClose" type="button">关闭</button>
              </div>
              <input id="accountAdminAccessEmail" type="hidden">
              <div class="account-admin-form-grid">
                <label>
                  <span>权限范围</span>
                  <select id="accountAdminAccessMode"></select>
                </label>
                <label>
                  <span>开通时长</span>
                  <select id="accountAdminAccessDuration"></select>
                </label>
                <label>
                  <span>Institution</span>
                  <select id="accountAdminAccessInstitutions" multiple></select>
                </label>
                <label>
                  <span>Industry</span>
                  <select id="accountAdminAccessIndustries" multiple></select>
                </label>
              </div>
              <div class="account-admin-page-ranges" id="accountAdminAccessPageRanges"></div>
              <label class="account-admin-note-field">
                <span>备注</span>
                <input id="accountAdminAccessNote" type="text" placeholder="可选">
              </label>
              <div class="account-admin-user-editor-actions">
                <button class="primary" type="submit">保存权限</button>
              </div>
            </form>
            <div class="account-admin-table-wrap">
              <table class="account-admin-table">
                <thead>
                  <tr>
                    <th>用户名</th>
                    <th>邮箱</th>
                    <th>账号</th>
                    <th>下载权限</th>
                    <th>到期</th>
                    <th>注册</th>
                    <th>最近登录</th>
                    <th>操作</th>
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

  function adminUserAccessLabel(user) {
    if (user && user.role === "super") return "全站报告";
    const access = user && user.access || {};
    if (!access.active) return "未开通";
    if (access.access_mode === "all") return "全站报告";
    if (access.access_mode === "filters") {
      const parts = [];
      if (Array.isArray(access.institutions) && access.institutions.length) parts.push(`机构 ${access.institutions.length}`);
      if (Array.isArray(access.industries) && access.industries.length) parts.push(`行业 ${access.industries.length}`);
      if (Array.isArray(access.page_ranges) && access.page_ranges.length) parts.push(`页数 ${access.page_ranges.length}`);
      return parts.length ? parts.join(" / ") : "条件报告";
    }
    return access.access_mode || "active";
  }

  function adminUserAccessExpiry(user) {
    const access = user && user.access || {};
    if (user && user.role === "super") return "长期";
    if (!access.active) return "-";
    if (access.lifetime) return "长期";
    return access.current_period_end ? String(access.current_period_end).slice(0, 10) : "-";
  }

  function adminUserRow(user) {
    const email = user.email || "";
    const editable = user.role !== "super";
    return `
      <tr data-email="${escapeHtml(email)}">
        <td>${escapeHtml(user.username || "")}</td>
        <td>${escapeHtml(email)}</td>
        <td>${escapeHtml(adminUserEntitlementLabel(user))}</td>
        <td>${escapeHtml(adminUserAccessLabel(user))}</td>
        <td>${escapeHtml(adminUserAccessExpiry(user))}</td>
        <td>${escapeHtml(String(user.created_at || "").slice(0, 10))}</td>
        <td>${escapeHtml(String(user.last_login_at || "").replace("T", " ").slice(0, 16))}</td>
        <td>${editable ? `<button class="secondary-button account-admin-edit-user" type="button" data-email="${escapeHtml(email)}">编辑</button>` : ""}</td>
      </tr>
    `;
  }

  function optionMarkup(options = [], selected = []) {
    const selectedSet = new Set((Array.isArray(selected) ? selected : []).map(String));
    return (options || []).map((option) => {
      const value = String(option.value || "");
      return `<option value="${escapeHtml(value)}"${selectedSet.has(value) ? " selected" : ""}>${escapeHtml(option.label || value)}</option>`;
    }).join("");
  }

  function setSelectValues(select, values = []) {
    const selected = new Set((Array.isArray(values) ? values : []).map(String));
    Array.from(select.options).forEach((option) => {
      option.selected = selected.has(option.value);
    });
  }

  function selectedSelectValues(select) {
    return Array.from(select.selectedOptions || []).map((option) => option.value).filter(Boolean);
  }

  function fillUserAccessEditor(user, targets) {
    if (!user || !targets.userEditor) return;
    const access = user.access || {};
    const options = accountAdminAccessOptions || {};
    const username = user.username || user.email || "";
    targets.userEditor.hidden = false;
    targets.accessEmail.value = user.email || "";
    targets.userEditorTitle.textContent = `编辑权限：${username}`;
    targets.accessMode.innerHTML = optionMarkup(options.modes || [], [access.access_mode || "none"]);
    targets.accessDuration.innerHTML = optionMarkup(options.durations || [], [access.lifetime ? "lifetime" : "12"]);
    targets.accessInstitutions.innerHTML = optionMarkup(options.institutions || [], access.institutions || []);
    targets.accessIndustries.innerHTML = optionMarkup(options.industries || [], access.industries || []);
    setSelectValues(targets.accessInstitutions, access.institutions || []);
    setSelectValues(targets.accessIndustries, access.industries || []);
    const selectedRanges = new Set(access.page_ranges || []);
    targets.accessPageRanges.innerHTML = (options.page_ranges || []).map((option) => `
      <label>
        <input type="checkbox" name="adminAccessPageRange" value="${escapeHtml(option.value || "")}"${selectedRanges.has(option.value) ? " checked" : ""}>
        <span>${escapeHtml(option.label || option.value || "")}</span>
      </label>
    `).join("");
    targets.accessNote.value = access.note || "";
    targets.accessMode.dispatchEvent(new Event("change"));
    if (targets.status) {
      targets.status.className = "status-line ok";
      targets.status.textContent = `正在编辑 ${username || "用户"} 的下载权限。`;
    }
    requestAnimationFrame(() => {
      targets.userEditor.scrollIntoView({ block: "nearest", behavior: "smooth" });
      if (targets.accessMode) targets.accessMode.focus({ preventScroll: true });
    });
  }

  function updateUserAccessEditorMode(targets) {
    if (!targets || !targets.userEditor) return;
    const filters = targets.accessMode.value === "filters";
    targets.accessInstitutions.disabled = !filters;
    targets.accessIndustries.disabled = !filters;
    targets.accessPageRanges.querySelectorAll("input").forEach((input) => {
      input.disabled = !filters;
    });
  }

  async function saveUserAccess(workerUrl, targets) {
    const email = targets.accessEmail.value || "";
    const mode = targets.accessMode.value || "none";
    const payload = {
      email,
      access_mode: mode,
      duration_months: mode === "none" ? "" : (targets.accessDuration.value || "12"),
      institutions: mode === "filters" ? selectedSelectValues(targets.accessInstitutions) : [],
      industries: mode === "filters" ? selectedSelectValues(targets.accessIndustries) : [],
      page_ranges: mode === "filters"
        ? Array.from(targets.accessPageRanges.querySelectorAll("input:checked")).map((input) => input.value)
        : [],
      note: targets.accessNote.value || "",
    };
    const response = await fetch(`${workerUrl}/account-admin/user-access`, {
      method: "POST",
      cache: "no-store",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify(payload),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || "保存权限失败。");
    const updated = data.user || null;
    if (updated && updated.email) accountAdminUsersByEmail.set(String(updated.email), updated);
    else {
      const existing = accountAdminUsersByEmail.get(email) || { email };
      accountAdminUsersByEmail.set(email, { ...existing, access: data.access });
    }
    return data;
  }

  function adminFileRow(file) {
    const key = file.type === "artifact" ? file.id : file.path;
    const endpointAttr = file.type === "artifact" ? "artifact" : "file";
    const note = file.note ? `<span>${escapeHtml(file.note)}</span>` : "";
    const accountClass = file.recommended_account === "KC桌面"
      ? "is-desktop"
      : (file.recommended_account === "KC娱乐" ? "is-entertain" : "is-bias");
    const accountLabel = file.recommended_account
      ? `
        <div class="account-admin-file-label">
          <span class="${accountClass}">适合：${escapeHtml(file.recommended_account)}</span>
          <small>${escapeHtml(file.account_label_confidence || "低")}信心 · ${escapeHtml(file.account_label_reason || "")}</small>
        </div>
      `
      : "";
    const repo = file.repo || "";
    return `
      <div class="account-admin-file">
        <div>
          <strong>${escapeHtml(file.label || file.kind || "File")}</strong>
          <span>${escapeHtml(file.date || "")} · ${escapeHtml(file.name || "")}${file.size_bytes ? ` · ${escapeHtml(formatSize(file.size_bytes))}` : ""}</span>
          ${note}
          ${accountLabel}
          <div class="account-admin-progress" hidden>
            <div class="account-admin-progress-track"><span></span></div>
            <small>等待下载…</small>
          </div>
        </div>
        <div class="account-admin-file-actions">
          <button class="secondary-button account-admin-download" type="button"
            data-kind="${escapeHtml(endpointAttr)}"
            data-file-kind="${escapeHtml(file.kind || "")}"
            data-key="${escapeHtml(key || "")}"
            data-repo="${escapeHtml(repo)}"
            data-size-bytes="${escapeHtml(String(file.size_bytes || 0))}"
            data-name="${escapeHtml(file.name || "download")}">下载</button>
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
        </div>
      </article>
    `;
  }

  function adminWechatArticleList(batch) {
    const articles = Array.isArray(batch.articles) ? batch.articles.slice(0, 9) : [];
    if (!articles.length) return `<div class="account-admin-wechat-empty">这个 batch 暂无标题明细。</div>`;
    return `
      <ol class="account-admin-wechat-articles">
        ${articles.map((article, index) => `
          <li>
            <span>${escapeHtml(article.label || `${index + 1}条`)}</span>
            <strong>${escapeHtml(article.title || "")}</strong>
          </li>
        `).join("")}
      </ol>
    `;
  }

  function adminWechatScheduleHeader(schedule) {
    if (!schedule || !schedule.date_folder) return "还没有找到公众号草稿 batch。";
    const dateText = schedule.date_iso || schedule.date_folder;
    return `${dateText} · 推荐发送窗口 · ${schedule.window || "08:00 - 次日 00:30"}`;
  }

  function adminWechatSourceDateNote(schedule) {
    const sourceDates = Array.isArray(schedule && schedule.source_dates) ? schedule.source_dates : [];
    if (!sourceDates.length) return "";
    const text = sourceDates
      .map((entry) => {
        const label = entry.source_label || "来源";
        const date = entry.date_iso || entry.date_folder || "";
        return `${label}: ${date}${entry.is_today ? "" : "（最近可用）"}`;
      })
      .join(" · ");
    const prefix = sourceDates.some((entry) => !entry.is_today)
      ? "部分来源今天还没有新草稿，已补入各来源最近可用 batch。"
      : "素材日期：";
    return `<div class="account-admin-wechat-note">${escapeHtml(prefix)} ${escapeHtml(text)}</div>`;
  }

  function adminWechatBatchRow(batch) {
    const meta = [
      batch.source_label,
      batch.source_date_iso ? `素材 ${batch.source_date_iso}${batch.source_is_today ? "" : "（最近可用）"}` : "",
      batch.article_count ? `${batch.article_count}篇` : "",
      batch.total_batches ? `第 ${batch.schedule_index}/${batch.total_batches} 个 batch` : "",
    ].filter(Boolean).join(" · ");
    return `
      <article class="account-admin-wechat-batch">
        <div class="account-admin-wechat-time">
          <strong>${escapeHtml(batch.scheduled_time || "")}</strong>
          <span>${escapeHtml(batch.day_label || "")}</span>
        </div>
        <div class="account-admin-wechat-main">
          <div class="account-admin-wechat-title">
            <strong>${escapeHtml(batch.batch_label || `Batch ${batch.batch_no || ""}`)}</strong>
            <span>${escapeHtml(meta)}</span>
          </div>
          ${adminWechatArticleList(batch)}
        </div>
      </article>
    `;
  }

  function renderAdminWechatSchedule(schedule) {
    const batches = Array.isArray(schedule && schedule.batches) ? schedule.batches : [];
    if (!batches.length) {
      return `
        <div class="empty-state">
          ${escapeHtml(adminWechatScheduleHeader(schedule))}
        </div>
      `;
    }
    const sourceDateNote = adminWechatSourceDateNote(schedule);
    return `
      <div class="account-admin-wechat-summary">
        <strong>${escapeHtml(adminWechatScheduleHeader(schedule))}</strong>
        <span>${escapeHtml(`${schedule.total_batches || batches.length} 个 batch · ${schedule.total_articles || 0} 篇文章`)}</span>
      </div>
      ${sourceDateNote}
      ${batches.map(adminWechatBatchRow).join("")}
    `;
  }

  function analyticsTime(value) {
    return String(value || "").replace("T", " ").slice(0, 16);
  }

  function analyticsSourcesText(sources) {
    if (!sources || typeof sources !== "object") return "";
    return Object.entries(sources)
      .sort((a, b) => Number(b[1] || 0) - Number(a[1] || 0))
      .map(([source, count]) => `${source} ${count}`)
      .join(" · ");
  }

  function analyticsEventFilterText(event) {
    const filters = [];
    if (event.page_range_labels) filters.push(`页数: ${event.page_range_labels}`);
    if (event.bank) filters.push(`机构: ${event.bank}`);
    if (event.industry) filters.push(`行业: ${event.industry}`);
    if (event.start_date || event.end_date) filters.push(`日期: ${event.start_date || "开始"}-${event.end_date || "今天"}`);
    if (event.scope && event.scope !== "all") filters.push(`范围: ${event.scope}`);
    if (event.availability) filters.push(`PDF: ${event.availability}`);
    return filters.join(" · ");
  }

  function analyticsMetric(label, value) {
    return `
      <div class="account-admin-metric">
        <span>${escapeHtml(label)}</span>
        <strong>${escapeHtml(String(value || 0))}</strong>
      </div>
    `;
  }

  function renderAnalyticsTopSearches(searches) {
    const rows = Array.isArray(searches) ? searches.slice(0, 12) : [];
    if (!rows.length) return '<div class="empty-state">还没有搜索记录。</div>';
    return `
      <div class="account-admin-table-wrap">
        <table class="account-admin-table account-admin-analytics-table">
          <thead>
            <tr>
              <th>搜索词</th>
              <th>次数</th>
              <th>访客</th>
              <th>来源</th>
              <th>最近</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map((row) => `
              <tr>
                <td><strong>${escapeHtml(row.query || "")}</strong></td>
                <td>${escapeHtml(row.count || 0)}</td>
                <td>${escapeHtml(row.visitor_count || 0)}</td>
                <td>${escapeHtml(analyticsSourcesText(row.sources))}</td>
                <td>${escapeHtml(analyticsTime(row.last_at))}</td>
              </tr>
            `).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function renderAnalyticsTopReports(reports) {
    const rows = Array.isArray(reports) ? reports.slice(0, 10) : [];
    if (!rows.length) return '<div class="empty-state">还没有报告点击记录。</div>';
    return `
      <div class="account-admin-files account-admin-analytics-list">
        ${rows.map((row) => `
          <div class="account-admin-file">
            <div>
              <strong>${escapeHtml(row.title || row.report_id || "")}</strong>
              <span>${escapeHtml(row.source || "")} · 打开 ${escapeHtml(row.opens || 0)} · 下载 ${escapeHtml(row.downloads || 0)} · ${escapeHtml(analyticsTime(row.last_at))}</span>
            </div>
          </div>
        `).join("")}
      </div>
    `;
  }

  function renderAnalyticsRecentEvents(events) {
    const rows = Array.isArray(events) ? events.slice(0, 30) : [];
    if (!rows.length) return '<div class="empty-state">还没有最近事件。</div>';
    return `
      <div class="account-admin-table-wrap">
        <table class="account-admin-table account-admin-analytics-table">
          <thead>
            <tr>
              <th>时间</th>
              <th>事件</th>
              <th>用户/访客</th>
              <th>内容</th>
              <th>状态</th>
            </tr>
          </thead>
          <tbody>
            ${rows.map((event) => {
              const user = event.user && (event.user.username || event.user.email)
                ? `${event.user.username || ""}${event.user.email ? ` · ${event.user.email}` : ""}`
                : (event.visitor_id ? event.visitor_id.slice(0, 12) : "匿名");
              const content = event.query
                ? `${event.source || ""} 搜索：${event.query}`
                : (event.report_title || event.report_id || event.path || "");
              const status = [
                event.result_count ? `${event.result_count}条` : "",
                analyticsEventFilterText(event),
                event.cache_status || "",
                event.status || "",
                event.error || "",
              ].filter(Boolean).join(" · ");
              return `
                <tr>
                  <td>${escapeHtml(analyticsTime(event.ts))}</td>
                  <td>${escapeHtml(event.type || "")}</td>
                  <td>${escapeHtml(user)}</td>
                  <td>${escapeHtml(content)}</td>
                  <td>${escapeHtml(status)}</td>
                </tr>
              `;
            }).join("")}
          </tbody>
        </table>
      </div>
    `;
  }

  function renderAccountAdminAnalytics(analytics) {
    if (!analytics || typeof analytics !== "object") {
      return '<div class="empty-state">还没有可用的访问数据。</div>';
    }
    return `
      <div class="account-admin-metrics">
        ${analyticsMetric("访客", analytics.visitor_count)}
        ${analyticsMetric("搜索", analytics.search_count)}
        ${analyticsMetric("报告打开", analytics.report_open_count)}
        ${analyticsMetric("下载", analytics.download_success_count)}
        ${analyticsMetric("发货链接", analytics.delivery_link_count)}
      </div>
      <div class="account-admin-analytics-grid">
        <section>
          <h4>热门搜索</h4>
          ${renderAnalyticsTopSearches(analytics.top_searches)}
        </section>
        <section>
          <h4>热门报告</h4>
          ${renderAnalyticsTopReports(analytics.top_reports)}
        </section>
      </div>
      <section>
        <h4>最近事件</h4>
        ${renderAnalyticsRecentEvents(analytics.recent_events)}
      </section>
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

  function contentRangeTotal(value) {
    const match = String(value || "").match(/^bytes\s+\d+-\d+\/(\d+)$/i);
    return match ? Number(match[1]) : 0;
  }

  function shouldUseSegmentedDownload(button) {
    const name = String(button && button.dataset.name || "");
    const size = Number(button && button.dataset.sizeBytes || 0) || 0;
    if (/\.mp4$/i.test(name)) return true;
    return size > 5 * 1024 * 1024 && /\.(mp4|pdf|zip)$/i.test(name);
  }

  function isVideoDownloadButton(button) {
    return /\.mp4$/i.test(String(button && button.dataset.name || ""));
  }

  function setDownloadMessage(progress, message, percent = 12) {
    if (!progress) return;
    const bar = progress.querySelector(".account-admin-progress-track span");
    const text = progress.querySelector("small");
    progress.hidden = false;
    if (bar) bar.style.width = `${Math.max(0, Math.min(100, percent))}%`;
    if (text) text.textContent = message || "";
  }

  function adminActionButtons(button) {
    const actions = button && button.closest(".account-admin-file-actions");
    return actions ? Array.from(actions.querySelectorAll("button")) : [];
  }

  function cancelActiveAdminButton(button) {
    const active = activeAdminButtonActions.get(button);
    if (!active) return false;
    active.controller.abort();
    return true;
  }

  function startAdminButtonAction(button, controller) {
    if (!button || !controller) return;
    if (!button.dataset.idleLabel) button.dataset.idleLabel = button.textContent.trim() || "下载";
    activeAdminButtonActions.set(button, { controller });
    adminActionButtons(button).forEach((other) => {
      other.disabled = other !== button;
    });
    button.disabled = false;
    button.classList.add("is-cancel");
    button.textContent = "取消";
  }

  function finishAdminButtonAction(button, label = "", restoreDelayMs = 0) {
    if (!button) return;
    activeAdminButtonActions.delete(button);
    adminActionButtons(button).forEach((other) => {
      other.disabled = false;
    });
    button.classList.remove("is-cancel");
    const idle = button.dataset.idleLabel || "下载";
    button.textContent = label || idle;
    if (label && restoreDelayMs > 0) {
      window.setTimeout(() => {
        if (!activeAdminButtonActions.has(button)) button.textContent = idle;
      }, restoreDelayMs);
    }
  }

  function withDownloadToken(endpoint) {
    const session = loadAuthSession();
    const url = new URL(endpoint, window.location.href);
    if (session && session.token) url.searchParams.set("download_token", session.token);
    return url.toString();
  }

  function triggerNativeDownload(url, fallbackName) {
    const link = document.createElement("a");
    link.href = url;
    link.target = "_blank";
    link.rel = "noopener noreferrer";
    link.download = fallbackName || "download";
    document.body.appendChild(link);
    link.click();
    link.remove();
  }

  function timeoutSignal(parentSignal, ms) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), ms);
    const cleanup = () => clearTimeout(timer);
    controller.signal.addEventListener("abort", cleanup, { once: true });
    if (parentSignal) {
      if (parentSignal.aborted) controller.abort();
      else parentSignal.addEventListener("abort", () => controller.abort(), { once: true });
    }
    return controller.signal;
  }

  async function fetchRangeBlob(endpoint, start, end, signal) {
    const response = await fetch(endpoint, {
      headers: {
        ...authHeaders(),
        "Range": `bytes=${start}-${end}`,
      },
      signal,
    });
    if (response.status !== 206) {
      if (response.ok && start === 0) return { response, blob: await response.blob(), total: Number(response.headers.get("Content-Length") || 0), full: true };
      const data = await response.json().catch(() => ({}));
      throw new Error(data.detail || `分段下载失败 (${response.status})。`);
    }
    return {
      response,
      blob: await response.blob(),
      total: contentRangeTotal(response.headers.get("Content-Range")),
      full: false,
    };
  }

  async function segmentedAdminDownload(endpoint, fallbackName, progress, signal, options = {}) {
    const chunkSize = options.chunkSize || 4 * 1024 * 1024;
    const concurrency = options.concurrency || 4;
    const firstSignal = options.firstChunkTimeoutMs ? timeoutSignal(signal, options.firstChunkTimeoutMs) : signal;
    const first = await fetchRangeBlob(endpoint, 0, chunkSize - 1, firstSignal);
    if (first.full) {
      setDownloadProgress(progress, first.blob.size, first.total || first.blob.size);
      return first.blob;
    }
    const total = first.total;
    if (!total || total <= first.blob.size) {
      setDownloadProgress(progress, first.blob.size, first.blob.size || total);
      return first.blob;
    }
    const chunks = [];
    chunks[0] = first.blob;
    let loaded = first.blob.size;
    setDownloadProgress(progress, loaded, total);
    const ranges = [];
    for (let start = chunkSize; start < total; start += chunkSize) {
      ranges.push([start, Math.min(total - 1, start + chunkSize - 1), ranges.length + 1]);
    }
    let cursor = 0;
    async function worker() {
      while (cursor < ranges.length) {
        const [start, end, index] = ranges[cursor];
        cursor += 1;
        const part = await fetchRangeBlob(endpoint, start, end, signal);
        chunks[index] = part.blob;
        loaded += part.blob.size;
        setDownloadProgress(progress, loaded, total);
      }
    }
    await Promise.all(Array.from({ length: Math.min(concurrency, ranges.length) }, () => worker()));
    setDownloadProgress(progress, total, total);
    return new Blob(chunks, { type: first.response.headers.get("Content-Type") || contentTypeFromFilename(fallbackName) });
  }

  async function prepareSegmentedAdminDownload(workerUrl, button, signal, progress) {
    const kind = String(button && button.dataset.kind || "");
    if (kind !== "file" && kind !== "artifact") return;
    const key = button.dataset.key || "";
    const repo = button.dataset.repo || "";
    const name = button.dataset.name || "download";
    const url = new URL(`${workerUrl}/account-admin/prepare-github-download`);
    url.searchParams.set("kind", kind);
    if (kind === "artifact") {
      url.searchParams.set("id", key);
      url.searchParams.set("name", name);
    } else {
      url.searchParams.set("path", key);
      if (repo) url.searchParams.set("repo", repo);
    }
    setDownloadProgress(progress, 1, 100);
    const response = await fetch(url.toString(), {
      cache: "no-store",
      headers: authHeaders(),
      signal: timeoutSignal(signal, 25000),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !data.ok) {
      throw new Error(data.detail || "文件缓存准备失败，请稍后重试。");
    }
    setDownloadProgress(progress, 100, 100);
    return data;
  }

  function contentTypeFromFilename(name) {
    if (/\.mp4$/i.test(name)) return "video/mp4";
    if (/\.pdf$/i.test(name)) return "application/pdf";
    return "application/octet-stream";
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
      const wechatSchedule = data.wechat_schedule && typeof data.wechat_schedule === "object" ? data.wechat_schedule : {};
      const analytics = data.analytics && typeof data.analytics === "object" ? data.analytics : null;
      accountAdminUsersByEmail = new Map(users.map((user) => [String(user.email || ""), user]));
      accountAdminAccessOptions = data.access_options && typeof data.access_options === "object" ? data.access_options : {};
      const canViewUsers = data.can_view_users !== false;
      const canViewWechat = data.can_view_wechat !== false;
      const canViewAnalytics = data.can_view_analytics !== false;
      if (targets.title && data.dashboard_title) targets.title.textContent = data.dashboard_title;
      if (targets.usersSection) targets.usersSection.hidden = !canViewUsers;
      if (targets.wechatSection) targets.wechatSection.hidden = !canViewWechat;
      if (targets.analyticsSection) targets.analyticsSection.hidden = !canViewAnalytics;
      accountAdminDailyPicks = new Map(dailyPicks.map((pick) => [String(pick.id || ""), pick]));
      targets.pickCount.textContent = dailyPicks.length ? `${dailyPicks.length} reports` : "";
      targets.picks.innerHTML = dailyPicks.length
        ? dailyPicks.map(adminDailyPickRow).join("")
        : `<div class="empty-state">还没有可用精选。新 PDF 同步后会自动根据宏观/页数/横屏规则筛选。</div>`;
      if (canViewWechat && targets.wechatCount && targets.wechatSchedule) {
        targets.wechatCount.textContent = wechatSchedule.total_batches ? `${wechatSchedule.total_batches} batches` : "";
        targets.wechatSchedule.innerHTML = renderAdminWechatSchedule(wechatSchedule);
      }
      if (canViewUsers && targets.userCount && targets.users) {
        targets.userCount.textContent = `${users.length} users`;
        targets.users.innerHTML = users.length
          ? users.map(adminUserRow).join("")
          : '<tr><td colspan="8">暂无用户。</td></tr>';
      }
      if (canViewAnalytics && targets.analytics && targets.analyticsCount) {
        targets.analyticsCount.textContent = analytics ? `近 ${analytics.range_days || 30} 天 · ${analytics.event_count || 0} events` : "";
        targets.analytics.innerHTML = renderAccountAdminAnalytics(analytics);
      }
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
    if (!workerUrl || !canOpenOperationsPanel()) return;
    const session = loadAuthSession();
    const isOperatorOnly = isOperatorSession(session) && !isSuperSession(session);
    const existing = document.getElementById("accountAdminModal");
    if (existing) existing.remove();
    document.body.insertAdjacentHTML("beforeend", accountAdminModalMarkup({
      title: isOperatorOnly ? "运营后台" : "管理后台",
      showWechat: !isOperatorOnly,
      showUsers: !isOperatorOnly,
      showAnalytics: !isOperatorOnly,
    }));

    const modal = document.getElementById("accountAdminModal");
    const title = document.getElementById("accountAdminTitle");
    const close = document.getElementById("accountAdminClose");
    const refresh = document.getElementById("accountAdminRefresh");
    const status = document.getElementById("accountAdminStatus");
    const pickCount = document.getElementById("accountAdminPickCount");
    const picks = document.getElementById("accountAdminPicks");
    const wechatCount = document.getElementById("accountAdminWechatCount");
    const wechatSchedule = document.getElementById("accountAdminWechatSchedule");
    const wechatSection = document.getElementById("accountAdminWechatSection");
    const userCount = document.getElementById("accountAdminUserCount");
    const users = document.getElementById("accountAdminUsers");
    const usersSection = document.getElementById("accountAdminUsersSection");
    const userEditor = document.getElementById("accountAdminUserEditor");
    const userEditorTitle = document.getElementById("accountAdminUserEditorTitle");
    const userEditorClose = document.getElementById("accountAdminUserEditorClose");
    const accessEmail = document.getElementById("accountAdminAccessEmail");
    const accessMode = document.getElementById("accountAdminAccessMode");
    const accessDuration = document.getElementById("accountAdminAccessDuration");
    const accessInstitutions = document.getElementById("accountAdminAccessInstitutions");
    const accessIndustries = document.getElementById("accountAdminAccessIndustries");
    const accessPageRanges = document.getElementById("accountAdminAccessPageRanges");
    const accessNote = document.getElementById("accountAdminAccessNote");
    const files = document.getElementById("accountAdminFiles");
    const analyticsCount = document.getElementById("accountAdminAnalyticsCount");
    const analytics = document.getElementById("accountAdminAnalytics");
    const analyticsSection = document.getElementById("accountAdminAnalyticsSection");
    const targets = {
      title,
      status,
      refresh,
      pickCount,
      picks,
      wechatCount,
      wechatSchedule,
      wechatSection,
      analyticsCount,
      analytics,
      analyticsSection,
      userCount,
      users,
      usersSection,
      userEditor,
      userEditorTitle,
      userEditorClose,
      accessEmail,
      accessMode,
      accessDuration,
      accessInstitutions,
      accessIndustries,
      accessPageRanges,
      accessNote,
      files,
    };

    function finish() {
      modal.remove();
    }

    close.addEventListener("click", finish);
    modal.addEventListener("click", (event) => {
      if (event.target === modal) finish();
    });
    refresh.addEventListener("click", () => loadAccountAdminSummary(workerUrl, targets));
    if (accessMode) accessMode.addEventListener("change", () => updateUserAccessEditorMode(targets));
    if (userEditorClose) {
      userEditorClose.addEventListener("click", () => {
        if (userEditor) userEditor.hidden = true;
      });
    }
    if (users) {
      users.addEventListener("click", (event) => {
        const button = event.target.closest(".account-admin-edit-user");
        if (!button) return;
        const user = accountAdminUsersByEmail.get(String(button.dataset.email || ""));
        if (user) {
          fillUserAccessEditor(user, targets);
        } else {
          status.className = "status-line error";
          status.textContent = "没有找到这个用户，请刷新后台后再试。";
        }
      });
    }
    if (userEditor) {
      userEditor.addEventListener("submit", async (event) => {
        event.preventDefault();
        const submit = userEditor.querySelector("button[type='submit']");
        if (submit) submit.disabled = true;
        status.className = "status-line";
        status.textContent = "正在保存用户权限…";
        try {
          await saveUserAccess(workerUrl, targets);
          const updatedUsers = [...accountAdminUsersByEmail.values()];
          users.innerHTML = updatedUsers.length
            ? updatedUsers.map(adminUserRow).join("")
            : '<tr><td colspan="8">暂无用户。</td></tr>';
          status.textContent = "用户权限已保存。";
          status.classList.add("ok");
        } catch (error) {
          status.textContent = error.message || "保存权限失败。";
          status.classList.add("error");
        } finally {
          if (submit) submit.disabled = false;
        }
      });
    }
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
      if (cancelActiveAdminButton(button)) {
        status.className = "status-line";
        status.textContent = "正在取消…";
        return;
      }
      const progress = row.querySelector(".account-admin-progress");
      const controller = new AbortController();
      startAdminButtonAction(button, controller);
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
        finishAdminButtonAction(button);
      }
    });
    files.addEventListener("click", async (event) => {
      const button = event.target.closest(".account-admin-download");
      if (!button) return;
      if (cancelActiveAdminButton(button)) {
        status.className = "status-line";
        status.textContent = "正在取消下载…";
        return;
      }
      const kind = button.dataset.kind;
      const segmented = (kind === "file" || kind === "artifact") && shouldUseSegmentedDownload(button);
      const key = button.dataset.key || "";
      const repo = button.dataset.repo || "";
      const name = button.dataset.name || "download";
      const endpoint = kind === "artifact"
        ? `${workerUrl}/account-admin/github-artifact?id=${encodeURIComponent(key)}`
        : `${workerUrl}/account-admin/github-file?path=${encodeURIComponent(key)}${repo ? `&repo=${encodeURIComponent(repo)}` : ""}`;
      const row = button.closest(".account-admin-file");
      const progress = row && row.querySelector(".account-admin-progress");
      const controller = new AbortController();
      startAdminButtonAction(button, controller);
      resetDownloadProgress(progress);
      status.className = "status-line";
      status.textContent = segmented ? "正在准备高速缓存…" : "正在准备下载…";
      let finalLabel = "";
      let finalDelay = 0;
      try {
        let blob;
        let disposition = "";
        if (segmented && isVideoDownloadButton(button)) {
          const directUrl = withDownloadToken(endpoint);
          try {
            setDownloadMessage(progress, "正在准备高速缓存…", 8);
            await prepareSegmentedAdminDownload(workerUrl, button, timeoutSignal(controller.signal, 8000), progress);
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            status.textContent = "缓存准备较慢，正在尝试高速下载…";
          }
          try {
            status.textContent = "正在高速下载…";
            setDownloadMessage(progress, "正在高速下载…", 10);
            blob = await segmentedAdminDownload(endpoint, name, progress, controller.signal, { firstChunkTimeoutMs: 8000 });
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            setDownloadMessage(progress, "高速通道无响应，已切换浏览器下载。", 18);
            triggerNativeDownload(directUrl, name);
            status.textContent = "已切换浏览器下载。";
            status.classList.add("ok");
            finalLabel = "已切换";
            finalDelay = 1600;
            return;
          }
        } else if (segmented) {
          try {
            await prepareSegmentedAdminDownload(workerUrl, button, controller.signal, progress);
          } catch (error) {
            if (error && error.name === "AbortError" && controller.signal.aborted) throw error;
            status.textContent = "高速缓存准备较慢，正在改用直接下载…";
          }
          status.textContent = "正在分段下载…";
          blob = await segmentedAdminDownload(endpoint, name, progress, controller.signal);
        } else {
          const response = await fetch(endpoint, { headers: authHeaders(), signal: controller.signal });
          if (!response.ok) {
            const data = await response.json().catch(() => ({}));
            throw new Error(data.detail || `下载失败 (${response.status})。`);
          }
          disposition = response.headers.get("Content-Disposition") || "";
          blob = await responseBlobWithProgress(response, progress);
        }
        triggerBlobDownload(blob, disposition, name);
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
        finishAdminButtonAction(button, finalLabel, finalDelay);
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
      if (canOpenOperationsPanel()) showAccountAdminModal(workerUrl);
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

  function reportPageCountValue(item) {
    const pages = Number(item && item.page_count);
    return Number.isFinite(pages) && pages > 0 ? pages : 0;
  }

  function pageRangeForValue(value) {
    return PAGE_RANGE_FILTERS.find((range) => range.value === value) || null;
  }

  function pageRangeLabel(value) {
    const range = pageRangeForValue(value);
    return range ? range.label : "";
  }

  function itemMatchesPageRanges(item, selectedRanges) {
    if (!selectedRanges.length) return true;
    const pages = reportPageCountValue(item);
    if (!pages) return false;
    return selectedRanges.some((value) => {
      const range = pageRangeForValue(value);
      return range ? range.matches(pages) : false;
    });
  }

  function resultRow(item) {
    const bank = item.bank_code || item.bank_name || "Other";
    const size = formatSize(item.size_bytes);
    const industry = inferIndustry(item);
    const available = isPdfAvailable(item);
    const pages = reportPageCountValue(item);
    const statusParts = [
      pages ? `${pages}页` : "",
      available ? size : "Text only",
    ].filter(Boolean);
    const status = statusParts.join(" · ");
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
      <a class="related-row report-a-row" href="${escapeHtml(url)}" target="_blank" rel="noopener noreferrer" data-id="${escapeHtml(item.id)}">
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
    const pageRangeInputs = Array.from(document.querySelectorAll('input[name="pageRange"]'));
    const clearFilters = document.getElementById("clearFilters");
    const activeFilters = document.getElementById("activeFilters");
    const prevPage = document.getElementById("prevPage");
    const nextPage = document.getElementById("nextPage");
    const pageInfo = document.getElementById("pageInfo");
    const pageSize = document.getElementById("pageSize");
    const items = Array.isArray(catalog.items) ? catalog.items : [];
    const catalogById = new Map(items.map((item) => [String(item.id || ""), item]));
    const metadataById = new Map(items.map((item) => [item.id, metadataText(item)]));
    const searchTextById = new Map();
    let searchIndexLabel = "Text index loading";
    let currentPage = 1;
    let catalogAnalyticsTimer = 0;
    let lastCatalogAnalyticsKey = "";

    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();
    trackEvent(workerUrl, "page_view", { page: "home", report_count: items.length });

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
      if (!itemMatchesPageRanges(item, selectedPageRangeValues())) return false;
      const date = itemDate(item);
      if (startDate.value && (!date || date < startDate.value)) return false;
      if (endDate.value && (!date || date > endDate.value)) return false;
      return true;
    }

    function selectedPageRangeValues() {
      return pageRangeInputs
        .filter((input) => input.checked)
        .map((input) => input.value);
    }

    function selectedPageRangeLabels() {
      return selectedPageRangeValues()
        .map(pageRangeLabel)
        .filter(Boolean);
    }

    function updateActiveFilters() {
      const labels = [];
      if (bankFilter.value) labels.push(bankFilter.options[bankFilter.selectedIndex].text.replace(/\s+\(\d+\)$/, ""));
      if (industryFilter.value) labels.push(industryFilter.value);
      if (startDate.value || endDate.value) labels.push(`${startDate.value || "start"} to ${endDate.value || "today"}`);
      if (availabilityFilter.value === "available") labels.push("PDF available");
      if (availabilityFilter.value === "textOnly") labels.push("Text only");
      const pageLabels = selectedPageRangeLabels();
      if (pageLabels.length) labels.push(`Pages: ${pageLabels.join(", ")}`);
      if (scopeFilter.value !== "all") labels.push(scopeFilter.options[scopeFilter.selectedIndex].text);
      activeFilters.textContent = labels.length ? labels.join(" · ") : "No filters";
    }

    function render(options = {}) {
      if (options.resetPage) currentPage = 1;
      const query = normalize(input.value);
      const rawQuery = input.value.trim();
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
        scheduleCatalogSearchAnalytics(rawQuery, scoped.length);
        maybeRunAuthoritySearch(input.value.trim());
        return;
      }
      results.innerHTML = visible.map((entry) => resultRow(entry.item)).join("");
      results.scrollTop = 0;
      scheduleCatalogSearchAnalytics(rawQuery, scoped.length);
      maybeRunAuthoritySearch(input.value.trim());
    }

    function activeFilterPayload() {
      return {
        bank: bankFilter.value,
        industry: industryFilter.value,
        start_date: startDate.value,
        end_date: endDate.value,
        scope: scopeFilter.value,
        availability: availabilityFilter.value,
        page_ranges: selectedPageRangeValues().join(","),
        page_range_labels: selectedPageRangeLabels().join(", "),
      };
    }

    function hasActiveFilters() {
      const filters = activeFilterPayload();
      return Object.values(filters).some(Boolean) && !(filters.scope === "all" && Object.values({ ...filters, scope: "" }).every((value) => !value));
    }

    function scheduleCatalogSearchAnalytics(rawQuery, resultCount) {
      const cleanQuery = String(rawQuery || "").trim();
      const filtersActive = hasActiveFilters();
      if (cleanQuery.length < 2 && !filtersActive) return;
      const payload = {
        source: "catalog",
        query: cleanQuery,
        result_count: resultCount,
        ...activeFilterPayload(),
      };
      const key = JSON.stringify(payload);
      if (key === lastCatalogAnalyticsKey) return;
      window.clearTimeout(catalogAnalyticsTimer);
      catalogAnalyticsTimer = window.setTimeout(() => {
        lastCatalogAnalyticsKey = key;
        trackEvent(workerUrl, "search", payload);
      }, 900);
    }

    function clearAllFilters() {
      input.value = "";
      bankFilter.value = "";
      industryFilter.value = "";
      startDate.value = "";
      endDate.value = "";
      scopeFilter.value = "all";
      availabilityFilter.value = "";
      pageRangeInputs.forEach((control) => {
        control.checked = false;
      });
      render({ resetPage: true });
    }

    input.addEventListener("input", () => render({ resetPage: true }));
    [bankFilter, industryFilter, startDate, endDate, scopeFilter, availabilityFilter, ...pageRangeInputs].forEach((control) => {
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
      const item = catalogById.get(String(row.dataset.id || ""));
      trackEvent(workerUrl, "report_open", analyticsReportPayload(item || { id: row.dataset.id }, "catalog"));
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
    const reportAItems = new Map();
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
      reportAItems.clear();
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
        trackEvent(workerUrl, "search", {
          source: EXTERNAL_SOURCE,
          query,
          result_count: items.length,
          total_count: data.total_count || data.total_page || 0,
          cache_status: data.cache_status || "",
        });
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
        reportAItems.clear();
        items.forEach((item) => reportAItems.set(String(item.id), item));
        if (reportACount) reportACount.textContent = items.length ? `${items.length} 条` : "";
        reportAResults.innerHTML = items.length
          ? items.map(reportARow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
        trackEvent(workerUrl, "search", {
          source: REPORT_A_SOURCE,
          query,
          result_count: items.length,
          total_count: data.total || 0,
          cache_status: data.cache_status || "",
        });
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
        trackEvent(workerUrl, "search", {
          source: AUTHORITY_SOURCE,
          query,
          result_count: items.length,
          total_count: data.total || 0,
          cache_status: data.cache_status || "",
        });
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
      const item = externalItems.get(String(row.dataset.id));
      if (item) trackEvent(workerUrl, "report_open", analyticsReportPayload(item, EXTERNAL_SOURCE));
      if (isNativeNewTabLink(row)) return;
      event.preventDefault();
      event.stopPropagation();
      if (item) openInNewTab(externalPageUrl(item, ""));
    });
    if (reportAResults) {
      reportAResults.addEventListener("click", (event) => {
        const row = event.target.closest(".report-a-row");
        if (!row) return;
        const item = reportAItems.get(String(row.dataset.id || ""));
        if (item) trackEvent(workerUrl, "report_open", analyticsReportPayload(item, REPORT_A_SOURCE));
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
        if (item) openInNewTab(externalPageUrl({ ...item, source: REPORT_A_SOURCE }, ""));
      });
    }
    if (authorityResults) {
      authorityResults.addEventListener("click", (event) => {
        const row = event.target.closest(".authority-row");
        if (!row) return;
        const item = authorityItems.get(String(row.dataset.id));
        if (item) trackEvent(workerUrl, "report_open", analyticsReportPayload(item, AUTHORITY_SOURCE));
        if (isNativeNewTabLink(row)) return;
        event.preventDefault();
        event.stopPropagation();
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
    trackEvent(workerUrl, "download_attempt", {
      ...analyticsReportPayload(item, "catalog"),
      action: "account_download",
    });
    const response = await fetch(`${workerUrl}/download`, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...authHeaders() },
      body: JSON.stringify({ id: item.id }),
    });
    if (!response.ok) {
      const data = await response.json().catch(() => ({}));
      if (response.status === 401) clearAuthSession();
      trackEvent(workerUrl, "download_error", {
        ...analyticsReportPayload(item, "catalog"),
        action: "account_download",
        status: String(response.status),
        error: data.error || "Download failed.",
      });
      throw new Error(downloadErrorMessage(response.status, data.error || "Download failed.", data));
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
    trackEvent(workerUrl, "download_success", {
      ...analyticsReportPayload(item, "catalog"),
      action: "account_download",
      status: "ok",
    });
    statusTarget("下载已开始。", "ok");
  }

  function initReportAccessControls(item, workerUrl, source, downloadHandler) {
    const panel = document.getElementById("accountAccess");
    if (!panel || !workerUrl) return;
    const openAccount = document.getElementById("openAccountPanel");
    const accountDownload = document.getElementById("accountDownloadReport");
    const hint = document.getElementById("accountAccessHint");
    const status = document.getElementById("accountAccessStatus");
    const passwordForm = document.getElementById("unlockForm");
    const context = { item, source };

    function statusTarget(text, kind) {
      setLineStatus(status, text, kind);
    }

    async function refresh() {
      const session = loadAuthSession();
      panel.hidden = false;
      if (passwordForm) passwordForm.hidden = false;
      accountDownload.hidden = true;
      openAccount.hidden = Boolean(session);
      if (!session) {
        hint.textContent = `登录后可查看账号下载权限；开通权限请联系微信 ${CONTACT_WECHAT}。`;
        statusTarget(`如需开通权限，请联系微信 ${CONTACT_WECHAT}。`);
        return;
      }
      hint.textContent = `当前账号：${authUserLabel(session)}`;
      statusTarget("正在读取账号权益…");
      try {
        const access = await fetchReportAccess(workerUrl, item, source);
        const summary = accountRightSummary(access);
        if (access && access.can_download) {
          accountDownload.hidden = false;
          if (passwordForm) passwordForm.hidden = true;
          hint.textContent = summary ? `当前账号已开通此报告下载权限，${summary}。` : "当前账号已开通此报告下载权限。";
          statusTarget(summary ? `可直接使用账号下载；${summary}。` : "可直接使用账号下载。", "ok");
        } else {
          if (passwordForm) passwordForm.hidden = false;
          statusTarget(summary
            ? `当前账号有${summary}，但不包含此报告。如需调整权限，请联系微信 ${CONTACT_WECHAT}。`
            : `当前账号尚未解锁此报告。如需开通权限，请联系微信 ${CONTACT_WECHAT}。`);
        }
      } catch (error) {
        if (passwordForm) passwordForm.hidden = false;
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
    if (!canUseDeliveryTools()) throw new Error("Private tools are locked.");
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
    if (!canUseDeliveryTools()) throw new Error("Private tools are locked.");
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
      panel.hidden = !canUseDeliveryTools();
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
        trackEvent(workerUrl, "delivery_link_generate", analyticsReportPayload(item, "catalog"));
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
    const catalogById = new Map((catalogItems || []).map((row) => [String(row.id || ""), row]));
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
    trackEvent(workerUrl, "page_view", {
      page: "report",
      ...analyticsReportPayload(item, "catalog"),
    });

    detail.addEventListener("click", (event) => {
      const row = event.target.closest(".report-link");
      if (!row) return;
      const relatedItem = catalogById.get(String(row.dataset.id || ""));
      trackEvent(workerUrl, "report_open", analyticsReportPayload(relatedItem || { id: row.dataset.id }, "catalog"));
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
      const session = loadAuthSession();
      const action = session ? "account_or_password_download" : "password_download";
      status.textContent = session ? "Checking account access..." : "Checking password...";
      let downloadErrorTracked = false;
      trackEvent(workerUrl, "download_attempt", {
        ...analyticsReportPayload(item, "catalog"),
        action,
      });
      try {
        const response = await fetch(`${workerUrl}/download`, {
          method: "POST",
          headers: { "Content-Type": "application/json", ...authHeaders() },
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
          trackEvent(workerUrl, "download_error", {
            ...analyticsReportPayload(item, "catalog"),
            action,
            status: String(response.status),
            error: message,
          });
          downloadErrorTracked = true;
          throw new Error(downloadErrorMessage(response.status, message, data));
        }

        const blob = await response.blob();
        triggerBlobDownload(blob, response.headers.get("Content-Disposition"), item.filename);
        if (!session && input.value) setRememberedDownloadPassword(input.value);
        trackEvent(workerUrl, "download_success", {
          ...analyticsReportPayload(item, "catalog"),
          action,
          status: "ok",
        });
        status.textContent = "Download started.";
        status.classList.add("ok");
      } catch (error) {
        if (!downloadErrorTracked) {
          trackEvent(workerUrl, "download_error", {
            ...analyticsReportPayload(item, "catalog"),
            action,
            status: "exception",
            error: error.message || "Download failed.",
          });
        }
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
    initNewsfeedNav();
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
    trackEvent(workerUrl, "download_attempt", {
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
      action: options.auth ? "account_download" : "password_download",
    });
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
      trackEvent(workerUrl, "download_pending", {
        ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
        action: "pending",
        status: "202",
      });
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
      trackEvent(workerUrl, "download_error", {
        ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
        action: options.auth ? "account_download" : "password_download",
        status: String(response.status),
        error: message,
      });
      throw new Error(message);
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), `${item.id}.pdf`);
    setRememberedDownloadPassword(password);
    trackEvent(workerUrl, "download_success", {
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
      action: options.auth ? "account_download" : "password_download",
      status: "ok",
    });
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
    initNewsfeedNav();
    trackEvent(workerUrl, "page_view", {
      page: "doc",
      ...analyticsReportPayload(item, item.source || EXTERNAL_SOURCE),
    });

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
        : "联系 MacroGate 获取原文。";
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
      adminTools.hidden = !canUseDeliveryTools();
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
        trackEvent(workerUrl, "delivery_link_generate", analyticsReportPayload(item, item.source || EXTERNAL_SOURCE));
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

  function newsfeedLogoUrl(item) {
    if (item && item.logo_url) return item.logo_url;
    const domain = String(item && (item.domain || item.source_domain) || "").trim();
    return domain ? `https://www.google.com/s2/favicons?domain=${encodeURIComponent(domain)}&sz=64` : "";
  }

  function newsfeedTimeLabel(value) {
    const timestamp = Date.parse(value || "");
    if (!Number.isFinite(timestamp)) return "";
    const diff = Date.now() - timestamp;
    const minute = 60 * 1000;
    const hour = 60 * minute;
    const day = 24 * hour;
    if (diff >= 0 && diff < hour) return `${Math.max(1, Math.round(diff / minute))}m ago`;
    if (diff >= 0 && diff < day) return `${Math.max(1, Math.round(diff / hour))}h ago`;
    if (diff >= 0 && diff < 3 * day) return `${Math.max(1, Math.round(diff / day))}d ago`;
    return new Intl.DateTimeFormat("en", { month: "short", day: "numeric", hour: "2-digit", minute: "2-digit" }).format(new Date(timestamp));
  }

  function newsfeedSourceName(item) {
    return String(item && (item.source || item.source_name || item.domain) || "News").replace(/^GDELT\s*\/\s*/i, "");
  }

  const NEWSFEED_UI_COPY = {
    en: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    "zh-CN": {
      myFeed: "我的新闻",
      explore: "探索",
      addTopics: "添加话题",
      digestEmail: "邮件摘要",
      dailyDigest: "每日摘要",
      topHeadlines: "重点新闻",
      regions: "区域",
      language: "语言",
      outputLanguage: "输出语言",
      suggestedTopics: "热门话题",
      sendDailyDigest: "发送每日摘要",
      saveEmail: "保存邮箱",
      sendTestNow: "发送测试邮件",
      sendNewsletterNow: "立即发送 newsletter",
      email: "邮箱",
      sendTime: "发送时间",
      timezone: "时区",
      noHeadlines: "暂无新闻。",
      loadingLatest: "正在加载最新新闻...",
      updating: "正在补全新闻流...",
      playBriefing: "播放简报",
      nowPlaying: "正在播放",
      playlist: "播放列表",
      readStory: "阅读新闻",
      addRegion: "添加区域",
      customRegion: "其他区域",
    },
    ja: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
    ko: {
      myFeed: "My feed",
      explore: "Explore",
      addTopics: "Add topics",
      digestEmail: "Digest Email",
      dailyDigest: "Daily Digest",
      topHeadlines: "Top Headlines",
      regions: "Regions",
      language: "Language",
      outputLanguage: "Output language",
      suggestedTopics: "Suggested Topics",
      sendDailyDigest: "Send daily digest",
      saveEmail: "Save email",
      sendTestNow: "Send test now",
      sendNewsletterNow: "Send newsletter now",
      email: "Email",
      sendTime: "Send time",
      timezone: "Timezone",
      noHeadlines: "No headlines yet.",
      loadingLatest: "Loading latest news...",
      updating: "Updating full feed...",
      playBriefing: "Play briefing",
      nowPlaying: "Now Playing",
      playlist: "Playlist",
      readStory: "Read Story",
      addRegion: "Add region",
      customRegion: "Other region",
    },
  };

  function newsfeedLanguageCode(value) {
    return ["en", "zh-CN", "ja", "ko"].includes(value) ? value : "en";
  }

  function newsfeedText(state, key) {
    const language = newsfeedLanguageCode(state && state.interfaceLanguage || "en");
    return (NEWSFEED_UI_COPY[language] && NEWSFEED_UI_COPY[language][key]) || NEWSFEED_UI_COPY.en[key] || key;
  }

  function newsfeedImageMarkup(item) {
    const image = String(item && item.image_url || "").trim();
    if (!image) return "";
    return `<img class="news-story-image" src="${escapeHtml(image)}" alt="">`;
  }

  function newsfeedLogoMarkup(item) {
    const logo = newsfeedLogoUrl(item);
    const label = newsfeedSourceName(item).slice(0, 1).toUpperCase() || "N";
    return logo
      ? `<img class="news-source-logo" src="${escapeHtml(logo)}" alt="">`
      : `<span class="news-source-logo news-source-fallback">${escapeHtml(label)}</span>`;
  }

  function newsfeedSourceStack(items = []) {
    const unique = [];
    const seen = new Set();
    for (const item of items) {
      const key = String(item.domain || item.source || item.source_name || item.id || "");
      if (!key || seen.has(key)) continue;
      seen.add(key);
      unique.push(item);
      if (unique.length >= 5) break;
    }
    if (!unique.length) return "";
    return `
      <div class="news-source-stack" aria-label="Sources">
        ${unique.map(newsfeedLogoMarkup).join("")}
      </div>
    `;
  }

  function newsfeedStoryMeta(item) {
    return [newsfeedTimeLabel(item && item.published_at), newsfeedSourceName(item), item && item.category]
      .filter(Boolean)
      .join(" · ");
  }

  function newsfeedStoryCard(item, index = 0, options = {}) {
    if (!item) return "";
    const id = String(item.id || "");
    const image = newsfeedImageMarkup(item);
    const summary = item.summary ? `<p>${escapeHtml(item.summary)}</p>` : "";
    const className = options.featured ? "news-story is-featured" : "news-story";
    return `
      <button class="${className}" type="button" data-action="open-article" data-id="${escapeHtml(id)}">
        <span class="news-story-rank">${index ? escapeHtml(index) : ""}</span>
        <span class="news-story-main">
          <strong>${escapeHtml(item.title || "Untitled")}</strong>
          ${summary}
          <span class="news-story-meta">${escapeHtml(newsfeedStoryMeta(item))}</span>
        </span>
        ${image}
        <span class="news-story-actions">${newsfeedLogoMarkup(item)}<span>···</span></span>
      </button>
    `;
  }

  function newsfeedSpinnerMarkup(label = "Loading") {
    return `
      <div class="newsfeed-loader" role="status" aria-live="polite">
        <span></span>
        <strong>${escapeHtml(label)}</strong>
      </div>
    `;
  }

  function newsfeedSkeletonMarkup(kind = "home", label = "Preparing Newsfeed") {
    const rows = Array.from({ length: kind === "article" ? 5 : 4 }).map(() => `
      <div class="news-skeleton-row">
        <span></span>
        <span></span>
      </div>
    `).join("");
    return `
      <section class="newsfeed-loading-panel">
        ${newsfeedSpinnerMarkup(label)}
        <div class="news-skeleton-block">
          ${rows}
        </div>
      </section>
    `;
  }

  function newsfeedDigestMarkup(digest = []) {
    const rows = digest.slice(0, 4).map((line) => `<li>${escapeHtml(line)}</li>`).join("");
    return rows || "<li>Fresh digest is loading.</li>";
  }

  function newsfeedTopicIcon(topic) {
    if (topic && topic.pinned) return "◆";
    if (topic && topic.kind === "custom") return "“";
    return "◇";
  }

  function newsfeedTopicRow(topic) {
    const id = String(topic && topic.id || "");
    return `
      <div class="news-topic-row" data-topic-id="${escapeHtml(id)}">
        <button class="news-topic-open" type="button" data-action="open-topic" data-id="${escapeHtml(id)}">
          <span>${escapeHtml(newsfeedTopicIcon(topic))}</span>
          <strong>${escapeHtml(topic.title || "Topic")}</strong>
          <small>${escapeHtml(topic.last_updated_label || topic.description || "")}</small>
        </button>
        <button class="news-topic-pin" type="button" data-action="pin-topic" data-id="${escapeHtml(id)}" aria-label="Pin topic">${topic && topic.pinned ? "●" : "○"}</button>
      </div>
    `;
  }

  function newsfeedShellMarkup() {
    return `
      <section class="newsfeed-layout">
        <aside class="newsfeed-sidebar" id="newsfeedSidebar">
          <div class="newsfeed-profile">
            <span class="newsfeed-avatar">KC</span>
            <strong>${escapeHtml(authUserLabel(loadAuthSession()))}</strong>
          </div>
          <div class="newsfeed-side-actions">
            <button type="button" data-action="show-feed">My feed</button>
            <button type="button" data-action="show-explore">Explore</button>
            <button type="button" data-action="show-email">Digest Email</button>
          </div>
          <div class="newsfeed-following">
            <div class="newsfeed-sidebar-heading">
              <span>Following</span>
              <strong id="newsfeedTopicCount">0 topics</strong>
            </div>
            <div id="newsfeedTopicList" class="newsfeed-topic-list"></div>
          </div>
          <button class="newsfeed-add-wide" type="button" data-action="show-add">+ Add Topics</button>
        </aside>
        <section class="newsfeed-main">
          <div class="newsfeed-command">
            <button class="news-icon-button" type="button" data-action="toggle-sidebar" aria-label="Topics">☰</button>
            <h1 id="newsfeedTitle">Daily Digest</h1>
            <div class="newsfeed-audio-actions">
              <button id="newsBriefingButton" class="news-icon-button is-wide" type="button" data-action="play-briefing" aria-label="Audio">▥ ▶</button>
            </div>
          </div>
          <div id="newsfeedPreferences" class="news-preference-bar"></div>
          <div id="newsfeedStatus" class="newsfeed-status" aria-live="polite"></div>
          <div id="newsfeedContent" class="newsfeed-content"></div>
          <div id="newsBriefingPanel" class="news-briefing-panel" hidden></div>
          <nav class="newsfeed-bottom-tabs" aria-label="Newsfeed sections">
            <button type="button" data-action="show-feed" class="is-active"><span>▯</span>My feed</button>
            <button type="button" data-action="show-add"><span>＋</span>Add topics</button>
            <button type="button" data-action="show-explore"><span>◇</span>Explore</button>
          </nav>
        </section>
      </section>
    `;
  }

  function renderNewsfeedBoot(app, message = "Checking Newsfeed access...") {
    app.innerHTML = `
      <section class="newsfeed-access is-loading">
        ${newsfeedSpinnerMarkup(message)}
        <p>We are preparing your private Newsfeed workspace.</p>
      </section>
    `;
  }

  async function newsfeedJson(workerUrl, path, options = {}) {
    const response = await fetch(`${workerUrl}${path}`, {
      cache: "no-store",
      ...options,
      headers: {
        ...(options.body ? { "Content-Type": "application/json" } : {}),
        ...authHeaders(),
        ...(options.headers || {}),
      },
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) throw new Error(data.detail || data.error || "Newsfeed request failed.");
    return data;
  }

  function renderNewsfeedAccess(app, workerUrl, message = "请登录已开通的账号继续。") {
    app.innerHTML = `
      <section class="newsfeed-access">
        <h1>Newsfeed</h1>
        <p>${escapeHtml(message)}</p>
        <button id="newsfeedLogin" class="primary" type="button">登录 / 账号</button>
      </section>
    `;
    const login = document.getElementById("newsfeedLogin");
    if (login) login.addEventListener("click", () => showAccountModal(workerUrl));
  }

  function setNewsfeedStatus(text, kind) {
    const status = document.getElementById("newsfeedStatus");
    if (!status) return;
    status.className = kind ? `newsfeed-status ${kind}` : "newsfeed-status";
    status.textContent = text || "";
  }

  function renderNewsfeedContentLoading(label, kind = "home") {
    const content = document.getElementById("newsfeedContent");
    if (content) content.innerHTML = newsfeedSkeletonMarkup(kind, label);
    setNewsfeedStatus(label, "loading");
  }

  function setNewsfeedTitle(text) {
    const title = document.getElementById("newsfeedTitle");
    if (title) title.textContent = text || "Newsfeed";
  }

  function refreshNewsfeedChrome(state) {
    const sideFeed = document.querySelector(".newsfeed-side-actions [data-action='show-feed']");
    const sideExplore = document.querySelector(".newsfeed-side-actions [data-action='show-explore']");
    const sideEmail = document.querySelector(".newsfeed-side-actions [data-action='show-email']");
    if (sideFeed) sideFeed.textContent = newsfeedText(state, "myFeed");
    if (sideExplore) sideExplore.textContent = newsfeedText(state, "explore");
    if (sideEmail) sideEmail.textContent = newsfeedText(state, "digestEmail");
    const bottomFeed = document.querySelector(".newsfeed-bottom-tabs [data-action='show-feed']");
    const bottomAdd = document.querySelector(".newsfeed-bottom-tabs [data-action='show-add']");
    const bottomExplore = document.querySelector(".newsfeed-bottom-tabs [data-action='show-explore']");
    if (bottomFeed) bottomFeed.innerHTML = `<span>▯</span>${escapeHtml(newsfeedText(state, "myFeed"))}`;
    if (bottomAdd) bottomAdd.innerHTML = `<span>＋</span>${escapeHtml(newsfeedText(state, "addTopics"))}`;
    if (bottomExplore) bottomExplore.innerHTML = `<span>◇</span>${escapeHtml(newsfeedText(state, "explore"))}`;
    const audio = document.getElementById("newsBriefingButton");
    if (audio) audio.setAttribute("aria-label", newsfeedText(state, "playBriefing"));
    renderNewsfeedPreferences(state);
  }

  function updateNewsfeedTabs(view) {
    document.querySelectorAll(".newsfeed-bottom-tabs button").forEach((button) => {
      const action = button.dataset.action || "";
      button.classList.toggle(
        "is-active",
        (view === "feed" && action === "show-feed") ||
          (view === "add" && action === "show-add") ||
          (view === "explore" && action === "show-explore") ||
          (view === "email" && action === "show-email"),
      );
    });
  }

  function normalizeNewsfeedRegionsClient(value) {
    const raw = Array.isArray(value) ? value : String(value || "").split(",");
    const out = [];
    const seen = new Set();
    for (const item of raw) {
      const clean = String(item && (item.value || item) || "").trim().slice(0, 54);
      const key = clean.toLowerCase();
      if (!clean || seen.has(key)) continue;
      seen.add(key);
      out.push(clean);
      if (out.length >= 8) break;
    }
    return out.length ? out : ["global"];
  }

  function newsfeedRegionOptions(state) {
    const defaults = [
      { value: "global", label: "Global" },
      { value: "mena", label: "MENA" },
      { value: "china", label: "China" },
      { value: "usa", label: "USA" },
    ];
    const options = Array.isArray(state.regionOptions) && state.regionOptions.length ? state.regionOptions : defaults;
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const custom = selected
      .filter((value) => !options.some((item) => item.value === value))
      .map((value) => ({ value, label: value }));
    return [...options, ...custom];
  }

  function newsfeedRegionLabel(state, value) {
    const option = newsfeedRegionOptions(state).find((item) => item.value === value);
    return option ? option.label : value;
  }

  function newsfeedPreferenceQuery(state, options = {}) {
    const params = new URLSearchParams();
    if (options.force || state.preferencesReady) {
      normalizeNewsfeedRegionsClient(state.preferredRegions).forEach((region) => params.append("regions", region));
      params.set("language", newsfeedLanguageCode(state.interfaceLanguage || state.outputLanguage || "en"));
      const regions = params.getAll("regions");
      params.delete("regions");
      params.set("regions", regions.join(","));
    }
    return params.toString();
  }

  function applyNewsfeedSettings(state, settings = {}) {
    state.settings = settings || state.settings || {};
    state.interfaceLanguage = newsfeedLanguageCode(settings.interface_language || state.interfaceLanguage || "en");
    state.outputLanguage = newsfeedLanguageCode(settings.interface_language || state.outputLanguage || settings.digest_language || "en");
    state.preferredRegions = normalizeNewsfeedRegionsClient(settings.preferred_regions || state.preferredRegions || ["global"]);
    state.preferencesReady = true;
  }

  function newsfeedLanguageOptions(selected = "en") {
    const languages = [
      ["en", "English"],
      ["zh-CN", "中文"],
      ["ja", "日本語"],
      ["ko", "한국어"],
    ];
    return languages.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedTimezoneOptions(selected = "Asia/Shanghai") {
    const timezones = [
      ["Asia/Shanghai", "China / Singapore"],
      ["America/New_York", "New York"],
      ["Europe/London", "London"],
      ["UTC", "UTC"],
    ];
    return timezones.map(([value, label]) => `
      <option value="${escapeHtml(value)}" ${value === selected ? "selected" : ""}>${escapeHtml(label)}</option>
    `).join("");
  }

  function newsfeedEmailPayloadFromForm(state) {
    return {
      digest_email_enabled: Boolean(document.getElementById("newsEmailEnabled")?.checked),
      digest_email: document.getElementById("newsEmailInput")?.value || "",
      digest_send_time: document.getElementById("newsEmailTime")?.value || "09:00",
      digest_timezone: document.getElementById("newsEmailTimezone")?.value || "Asia/Shanghai",
      digest_language: document.getElementById("newsEmailLanguage")?.value || state.outputLanguage || "en",
      interface_language: state.interfaceLanguage || "en",
      preferred_regions: state.preferredRegions || ["global"],
    };
  }

  function newsfeedEmailLastStatus(settings = {}) {
    const result = String(settings.digest_last_send_result || "").trim();
    if (!result) return "";
    const at = settings.digest_last_attempt_at || settings.digest_last_sent_at || "";
    const when = at ? newsfeedTimeLabel(at) : "";
    const detail = settings.digest_last_send_detail ? ` · ${settings.digest_last_send_detail}` : "";
    return `Last email attempt: ${result}${when ? ` · ${when}` : ""}${detail}`;
  }

  function renderNewsfeedPreferences(state) {
    const mount = document.getElementById("newsfeedPreferences");
    if (!mount) return;
    const selected = normalizeNewsfeedRegionsClient(state.preferredRegions);
    const selectedLabels = selected.map((value) => newsfeedRegionLabel(state, value)).join(", ");
    const options = newsfeedRegionOptions(state);
    mount.innerHTML = `
      <div class="news-region-picker">
        <button id="newsRegionToggle" type="button" data-action="toggle-region-menu" aria-expanded="false">
          <span>${escapeHtml(newsfeedText(state, "regions"))}</span>
          <strong>${escapeHtml(selectedLabels || "Global")}</strong>
          <span>▾</span>
        </button>
        <div id="newsRegionMenu" class="news-region-menu" hidden>
          ${options.map((item) => `
            <label>
              <input type="checkbox" data-action="region-checkbox" value="${escapeHtml(item.value)}" ${selected.includes(item.value) ? "checked" : ""}>
              <span>${escapeHtml(item.label)}</span>
            </label>
          `).join("")}
          <form id="newsCustomRegionForm" class="news-custom-region-form">
            <input id="newsCustomRegionInput" type="text" placeholder="${escapeHtml(newsfeedText(state, "customRegion"))}">
            <button type="submit">${escapeHtml(newsfeedText(state, "addRegion"))}</button>
          </form>
        </div>
      </div>
      <label class="news-inline-select">
        <span>${escapeHtml(newsfeedText(state, "language"))}</span>
        <select id="newsInterfaceLanguage">${newsfeedLanguageOptions(state.interfaceLanguage || "en")}</select>
      </label>
    `;
  }

  function renderNewsfeedEmailSettings(state) {
    const settings = state.settings || {};
    const session = loadAuthSession();
    const fallbackEmail = session && session.user && !session.user.email_is_generated ? session.user.email : "";
    const email = settings.digest_email || fallbackEmail || "";
    const enabled = Boolean(settings.digest_email_enabled);
    const providerNote = settings.email_provider_configured === false
      ? (state.interfaceLanguage === "zh-CN"
        ? "邮件服务还没配置好，请先配置 Brevo API key。"
        : "Email sender is not configured yet. Add the Brevo API key first.")
      : (settings.email_provider === "brevo"
        ? (state.interfaceLanguage === "zh-CN"
          ? "Brevo 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Brevo email is connected. Save, then send a newsletter now.")
        : (state.interfaceLanguage === "zh-CN"
          ? "Cloudflare 邮件服务已连接；保存后可立即发送 newsletter。"
          : "Cloudflare email is connected. Save, then send a newsletter now."));
    const lastStatus = newsfeedEmailLastStatus(settings);
    return `
      <section class="news-email-settings">
        <div class="news-email-copy">
          <h2>${escapeHtml(newsfeedText(state, "digestEmail"))}</h2>
          <p>${state.interfaceLanguage === "zh-CN" ? "每天定点发送最新摘要到邮箱。" : "Send the latest Daily Digest to your inbox once a day."}</p>
        </div>
        <form id="newsEmailForm" class="news-email-form">
          <label>${escapeHtml(newsfeedText(state, "email"))}
            <input id="newsEmailInput" type="email" autocomplete="email" placeholder="you@example.com" value="${escapeHtml(email)}">
          </label>
          <label>${escapeHtml(newsfeedText(state, "sendTime"))}
            <input id="newsEmailTime" type="time" value="${escapeHtml(settings.digest_send_time || "09:00")}">
          </label>
          <label>${escapeHtml(newsfeedText(state, "timezone"))}
            <select id="newsEmailTimezone">${newsfeedTimezoneOptions(settings.digest_timezone || "Asia/Shanghai")}</select>
          </label>
          <label>${escapeHtml(newsfeedText(state, "language"))}
            <select id="newsEmailLanguage">${newsfeedLanguageOptions(settings.digest_language || state.outputLanguage || "en")}</select>
          </label>
          <label class="news-toggle-row">
            <input id="newsEmailEnabled" type="checkbox" ${enabled ? "checked" : ""}>
            <span>${escapeHtml(newsfeedText(state, "sendDailyDigest"))}</span>
          </label>
          <button id="newsEmailSubmit" class="primary" type="submit">${escapeHtml(newsfeedText(state, "saveEmail"))}</button>
          <button id="newsEmailSend" class="primary news-email-test" type="button" data-action="send-email-now">${escapeHtml(newsfeedText(state, "sendNewsletterNow"))}</button>
          <button id="newsEmailTest" class="secondary-button news-email-test" type="button" data-action="send-email-test">${escapeHtml(newsfeedText(state, "sendTestNow"))}</button>
        </form>
        <div id="newsEmailStatus" class="status-line" aria-live="polite">${escapeHtml(lastStatus || providerNote)}</div>
      </section>
    `;
  }

  function rememberNewsfeedArticles(state, items = [], topic = null) {
    for (const item of items || []) {
      if (!item || !item.id) continue;
      const id = String(item.id);
      const outputLanguage = item.output_language || topic && topic.output_language || state.outputLanguage || "en";
      state.articles.set(id, item);
      if (state.articleLanguages) state.articleLanguages.set(id, outputLanguage);
    }
  }

  function renderNewsfeedSidebar(state) {
    const list = document.getElementById("newsfeedTopicList");
    const count = document.getElementById("newsfeedTopicCount");
    if (!list) return;
    const topics = [...(state.topics || [])].sort((a, b) => Number(Boolean(b.pinned)) - Number(Boolean(a.pinned)));
    list.innerHTML = topics.map(newsfeedTopicRow).join("") || '<div class="newsfeed-empty">No topics yet.</div>';
    if (count) count.textContent = `${topics.length}/${NEWSFEED_TOPIC_LIMIT} topics`;
  }

  function renderNewsfeedHome(state) {
    const home = state.home || {};
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "dailyDigest"));
    updateNewsfeedTabs("feed");
    state.currentView = "feed";
    state.topics = home.topics || state.topics || [];
    rememberNewsfeedArticles(state, home.highlights || []);
    rememberNewsfeedArticles(state, home.headlines || []);
    renderNewsfeedSidebar(state);
    const category = state.homeCategory || "Investment";
    const categories = home.categories || ["Investment", "Tech", "Politics", "Industries"];
    const filtered = (home.headlines || []).filter((item) => !category || item.category === category);
    const visible = filtered.length ? filtered : (home.headlines || []);
    content.innerHTML = `
      <section class="news-digest-panel">
        <div>
          <div class="news-section-kicker">${escapeHtml(newsfeedText(state, "dailyDigest"))} <span>${escapeHtml(String(home.digest_count || 0).padStart(2, "0"))}</span></div>
          <ul>${newsfeedDigestMarkup(home.daily_digest)}</ul>
        </div>
        ${newsfeedSourceStack(home.highlights || [])}
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>${escapeHtml(newsfeedText(state, "topHeadlines"))}</h2>
          <span>${escapeHtml(home.updated_label || "")}</span>
        </div>
        <div class="news-category-tabs">
          ${categories.map((item) => `
            <button type="button" data-action="home-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(item)}</button>
          `).join("")}
        </div>
        <div class="news-story-list">
          ${visible.slice(0, 12).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || `<div class="newsfeed-empty">${escapeHtml(newsfeedText(state, "noHeadlines"))}</div>`}
        </div>
      </section>
    `;
  }

  function renderNewsfeedAdd(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const home = state.home || {};
    const suggestions = home.suggested_topics || [];
    setNewsfeedTitle(newsfeedText(state, "addTopics"));
    updateNewsfeedTabs("add");
    state.currentView = "add";
    content.innerHTML = `
      <section class="news-add-panel">
        <div class="news-add-meta">
          <strong>${escapeHtml(String((state.topics || []).length))}/${NEWSFEED_TOPIC_LIMIT} topics created</strong>
          <span>${escapeHtml(newsfeedText(state, "suggestedTopics"))}</span>
        </div>
        <div class="news-suggested-list">
          ${suggestions.map((topic) => `<button type="button" data-action="suggest-topic" data-topic="${escapeHtml(topic)}">${escapeHtml(topic)}</button>`).join("")}
        </div>
        <div class="news-language-row">
          <label for="newsTopicLanguage">${escapeHtml(newsfeedText(state, "outputLanguage"))}</label>
          <select id="newsTopicLanguage">
            ${newsfeedLanguageOptions(state.outputLanguage || "en")}
          </select>
        </div>
        <div id="newsTopicStatus" class="status-line" aria-live="polite"></div>
        <form id="newsTopicForm" class="news-topic-form">
          <textarea id="newsTopicInput" rows="4" placeholder="Type any topic you want to follow"></textarea>
          <button id="newsTopicSubmit" class="primary" type="submit" aria-label="Create topic">↑</button>
        </form>
        ${renderNewsfeedEmailSettings(state)}
      </section>
    `;
  }

  function renderNewsfeedExplore(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    const explore = state.explore || {};
    const categories = explore.categories || ["Tech", "Industries", "Investment", "Politics"];
    const category = state.exploreCategory || categories[0] || "";
    const items = (explore.items || []).filter((item) => !category || item.category === category);
    rememberNewsfeedArticles(state, explore.items || []);
    setNewsfeedTitle(newsfeedText(state, "explore"));
    updateNewsfeedTabs("explore");
    state.currentView = "explore";
    content.innerHTML = `
      <section class="newsfeed-section">
        <div class="news-category-tabs news-category-tabs-large">
          ${categories.map((item) => `
            <button type="button" data-action="explore-category" data-category="${escapeHtml(item)}" class="${item === category ? "is-active" : ""}">${escapeHtml(item)}</button>
          `).join("")}
        </div>
        <div class="news-story-list news-story-list-cards">
          ${items.slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1)).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  function renderNewsfeedEmailView(state) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    setNewsfeedTitle(newsfeedText(state, "digestEmail"));
    updateNewsfeedTabs("email");
    state.currentView = "email";
    content.innerHTML = renderNewsfeedEmailSettings(state);
  }

  function renderNewsfeedTopic(state, topic, items) {
    const content = document.getElementById("newsfeedContent");
    if (!content) return;
    rememberNewsfeedArticles(state, items || [], topic);
    setNewsfeedTitle(topic && topic.title || "Topic");
    updateNewsfeedTabs("topic");
    state.currentView = "topic";
    state.currentTopic = topic;
    state.currentTopicItems = items || [];
    content.innerHTML = `
      <section class="news-topic-hero">
        <div>
          <span class="news-topic-mark">“</span>
          <h2>${escapeHtml(topic && topic.title || "Topic")}</h2>
          <p>${escapeHtml(topic && topic.description || "")}</p>
        </div>
        <div class="news-topic-source-line">
          <span>Sources</span>
          ${newsfeedSourceStack(items || [])}
        </div>
      </section>
      <section class="newsfeed-section">
        <div class="newsfeed-section-heading">
          <h2>Top Stories</h2>
          <span>${escapeHtml(topic && topic.updated_label || "")}</span>
        </div>
        <div class="news-story-list news-story-list-cards">
          ${(items || []).slice(0, 24).map((item, index) => newsfeedStoryCard(item, index + 1, { featured: index === 0 })).join("") || '<div class="newsfeed-empty">No stories yet.</div>'}
        </div>
      </section>
    `;
  }

  async function renderNewsfeedArticle(state, article) {
    const content = document.getElementById("newsfeedContent");
    if (!content || !article) return;
    state.currentView = "article";
    setNewsfeedTitle("Story");
    updateNewsfeedTabs("article");
    content.innerHTML = `
      <article class="news-article-detail">
        <button class="news-icon-button" type="button" data-action="article-back" aria-label="Back">‹</button>
        <header>
          <div>
            <h2>${escapeHtml(article.title || "Untitled")}</h2>
            <p>${escapeHtml(newsfeedStoryMeta(article))}</p>
          </div>
          ${article.image_url ? `<img src="${escapeHtml(article.image_url)}" alt="">` : newsfeedLogoMarkup(article)}
        </header>
        <div class="news-article-source">
          ${newsfeedLogoMarkup(article)}
          <span>${escapeHtml(newsfeedSourceName(article))}</span>
          ${article.url ? `<a href="${escapeHtml(article.url)}" target="_blank" rel="noopener noreferrer">Source</a>` : ""}
        </div>
        <div class="news-article-tabs">
          <button type="button" class="is-active">Narrative</button>
          <button type="button">Structured</button>
        </div>
        <section class="news-article-stream">
          <h3>Summary</h3>
          <div id="newsArticleSummary" class="news-stream-text"></div>
          <h3>Narrative</h3>
          <div id="newsArticleNarrative" class="news-stream-text"></div>
        </section>
      </article>
    `;
    await streamNewsfeedArticle(state.workerUrl, article);
  }

  async function streamNewsfeedArticle(workerUrl, article) {
    const summary = document.getElementById("newsArticleSummary");
    const narrative = document.getElementById("newsArticleNarrative");
    if (!summary || !narrative) return;
    summary.textContent = "Generating summary...";
    narrative.textContent = "Writing narrative...";
    try {
      const response = await fetch(`${workerUrl}/newsfeed/article`, {
        method: "POST",
        cache: "no-store",
        headers: { "Content-Type": "application/json", ...authHeaders() },
        body: JSON.stringify({ article }),
      });
      if (!response.ok) {
        const data = await response.json().catch(() => ({}));
        throw new Error(data.detail || "Could not load story.");
      }
      if (!response.body) {
        const data = await response.json();
        summary.textContent = data.summary || "";
        narrative.textContent = data.narrative || "";
        return;
      }
      const reader = response.body.getReader();
      const decoder = new TextDecoder();
      let buffer = "";
      summary.textContent = "";
      narrative.textContent = "";
      while (true) {
        const { done, value } = await reader.read();
        if (done) break;
        buffer += decoder.decode(value, { stream: true });
        const lines = buffer.split("\n");
        buffer = lines.pop() || "";
        for (const line of lines) {
          if (!line.trim()) continue;
          const event = JSON.parse(line);
          if (event.type === "summary") summary.textContent += event.text || "";
          if (event.type === "narrative") narrative.textContent += event.text || "";
        }
      }
    } catch (error) {
      narrative.textContent = error.message || "Could not load story.";
    }
  }

  function newsfeedBriefingItems(state) {
    if (state.currentView === "topic") return state.currentTopicItems || [];
    if (state.currentView === "explore") return state.explore && state.explore.items || [];
    return state.home && state.home.headlines || [];
  }

  function renderNewsfeedBriefingPanel(state, options = {}) {
    const panel = document.getElementById("newsBriefingPanel");
    if (!panel) return;
    const items = newsfeedBriefingItems(state).slice(0, 5);
    const first = items[0] || {};
    const progress = Math.max(0, Math.min(100, options.progress || 0));
    panel.hidden = false;
    panel.innerHTML = `
      <div class="news-briefing-head">
        <div>
          <strong>${escapeHtml(options.countText || "0/5 stories listened today")}</strong>
          <span>${escapeHtml(options.status || newsfeedText(state, "playBriefing"))}</span>
        </div>
        <button class="news-icon-button" type="button" data-action="close-briefing" aria-label="Close">×</button>
      </div>
      <div class="news-briefing-now">
        <div>
          <span>${escapeHtml(newsfeedText(state, "nowPlaying"))}</span>
          <h2>${escapeHtml(first.title || newsfeedText(state, "dailyDigest"))}</h2>
          ${first.id ? `<button type="button" data-action="open-article" data-id="${escapeHtml(first.id)}">${escapeHtml(newsfeedText(state, "readStory"))}</button>` : ""}
        </div>
        ${first.image_url ? `<img src="${escapeHtml(first.image_url)}" alt="">` : newsfeedLogoMarkup(first)}
      </div>
      <div class="news-briefing-playlist">
        <h3>${escapeHtml(newsfeedText(state, "playlist"))}</h3>
        ${items.slice(0, 4).map((item) => `
          <button type="button" data-action="open-article" data-id="${escapeHtml(item.id || "")}">
            <span>${escapeHtml(item.title || "Story")}</span>
            ${item.image_url ? `<img src="${escapeHtml(item.image_url)}" alt="">` : ""}
          </button>
        `).join("")}
      </div>
      <div class="news-briefing-player">
        <div class="news-briefing-progress"><span style="width:${progress}%"></span></div>
        <div class="news-briefing-controls">
          <button type="button" data-action="briefing-prev">‹</button>
          <button type="button" data-action="play-briefing" class="is-primary">${options.playing ? "❚❚" : "▶"}</button>
          <button type="button" data-action="briefing-next">›</button>
        </div>
        <small>${escapeHtml(options.voiceLabel || "browser speech")}</small>
      </div>
    `;
  }

  function stopNewsfeedBriefing(state) {
    if (window.speechSynthesis) window.speechSynthesis.cancel();
    if (state.briefingTimer) window.clearInterval(state.briefingTimer);
    state.briefingTimer = null;
    state.briefingPlaying = false;
    const button = document.getElementById("newsBriefingButton");
    if (button) {
      button.classList.remove("is-playing", "is-loading");
      button.innerHTML = "▥ ▶";
    }
  }

  async function playNewsfeedBriefing(state) {
    const button = document.getElementById("newsBriefingButton");
    if (state.briefingPlaying) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: "Paused", progress: state.briefingProgress || 0 });
      return;
    }
    const items = newsfeedBriefingItems(state).slice(0, 8);
    if (!items.length) {
      renderNewsfeedBriefingPanel(state, { status: "No stories ready yet" });
      return;
    }
    if (button) {
      button.classList.add("is-loading");
      button.innerHTML = "▥ …";
    }
    renderNewsfeedBriefingPanel(state, { status: "Preparing audio briefing...", playing: true });
    try {
      const data = await newsfeedJson(state.workerUrl, "/newsfeed/briefing", {
        method: "POST",
        body: JSON.stringify({
          language: state.interfaceLanguage || state.outputLanguage || "en",
          digest: state.home && state.home.daily_digest || [],
          items,
        }),
      });
      const script = data.script || "";
      state.briefingScript = script;
      state.briefingProgress = 0;
      if (!("speechSynthesis" in window) || !script) {
        renderNewsfeedBriefingPanel(state, { status: script || "Audio is not available in this browser.", progress: 100 });
        return;
      }
      stopNewsfeedBriefing(state);
      const utterance = new SpeechSynthesisUtterance(script);
      utterance.lang = state.interfaceLanguage === "zh-CN" ? "zh-CN" : state.interfaceLanguage || "en-US";
      utterance.rate = state.interfaceLanguage === "zh-CN" ? 1.05 : 1.08;
      state.briefingPlaying = true;
      if (button) {
        button.classList.remove("is-loading");
        button.classList.add("is-playing");
        button.innerHTML = "▥ ❚❚";
      }
      const started = Date.now();
      state.briefingTimer = window.setInterval(() => {
        state.briefingProgress = Math.min(100, ((Date.now() - started) / 30000) * 100);
        renderNewsfeedBriefingPanel(state, {
          status: "Playing 30 sec briefing",
          progress: state.briefingProgress,
          playing: true,
          voiceLabel: data.provider || "browser speech",
        });
      }, 800);
      utterance.onend = () => {
        stopNewsfeedBriefing(state);
        state.briefingProgress = 100;
        renderNewsfeedBriefingPanel(state, { status: "Briefing complete", progress: 100 });
      };
      utterance.onerror = () => {
        stopNewsfeedBriefing(state);
        renderNewsfeedBriefingPanel(state, { status: script, progress: 100 });
      };
      window.speechSynthesis.speak(utterance);
    } catch (error) {
      stopNewsfeedBriefing(state);
      renderNewsfeedBriefingPanel(state, { status: error.message || "Could not prepare briefing." });
    }
  }

  async function initNewsfeed() {
    const app = document.getElementById("newsfeedApp");
    if (app) renderNewsfeedBoot(app, "Checking account...");
    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);
    initNewsfeedNav();

    if (!app) return;
    let session = loadAuthSession();
    if (!isNewsfeedSession(session)) {
      renderNewsfeedBoot(app, "Checking Newsfeed access...");
      session = await refreshAuthSession(workerUrl);
    }
    if (!isNewsfeedSession(session)) {
      renderNewsfeedAccess(app, workerUrl);
      return;
    }

    const state = {
      workerUrl,
      home: null,
      explore: null,
      settings: null,
      topics: [],
      articles: new Map(),
      articleLanguages: new Map(),
      currentView: "feed",
      lastListView: "feed",
      homeCategory: "Investment",
      exploreCategory: "Tech",
      outputLanguage: "en",
      interfaceLanguage: "en",
      preferredRegions: ["global"],
      preferencesReady: false,
      regionOptions: [],
      briefingPlaying: false,
      briefingProgress: 0,
      briefingTimer: null,
    };

    app.innerHTML = newsfeedShellMarkup();
    refreshNewsfeedChrome(state);
    trackEvent(workerUrl, "page_view", { page: "newsfeed" });

    async function loadHome() {
      renderNewsfeedContentLoading(newsfeedText(state, "loadingLatest"), "home");
      const query = newsfeedPreferenceQuery(state);
      const fast = await newsfeedJson(workerUrl, `/newsfeed/home?fast=1&${query}`);
      state.home = fast;
      state.regionOptions = fast.regions || state.regionOptions || [];
      state.topics = fast.topics || [];
      applyNewsfeedSettings(state, fast.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      renderNewsfeedHome(state);
      setNewsfeedStatus(fast.pending ? newsfeedText(state, "updating") : "", fast.pending ? "loading" : "");
      newsfeedJson(workerUrl, `/newsfeed/home?${newsfeedPreferenceQuery(state)}`)
        .then((data) => {
          state.home = data;
          state.regionOptions = data.regions || state.regionOptions || [];
          state.topics = data.topics || state.topics || [];
          applyNewsfeedSettings(state, data.settings || state.settings || {});
          refreshNewsfeedChrome(state);
          setNewsfeedStatus("");
          if (state.currentView === "feed") renderNewsfeedHome(state);
          else renderNewsfeedSidebar(state);
        })
        .catch((error) => setNewsfeedStatus(error.message || "Newsfeed request failed.", "error"));
    }

    async function loadExplore(category = state.exploreCategory) {
      renderNewsfeedContentLoading("Loading explore...", "explore");
      const data = await newsfeedJson(workerUrl, `/newsfeed/explore?category=${encodeURIComponent(category || "")}&${newsfeedPreferenceQuery(state)}`);
      state.explore = data;
      state.regionOptions = data.regions || state.regionOptions || [];
      state.exploreCategory = category || (data.categories && data.categories[0]) || "";
      state.topics = data.topics || state.topics || [];
      setNewsfeedStatus("");
      refreshNewsfeedChrome(state);
      renderNewsfeedSidebar(state);
      renderNewsfeedExplore(state);
    }

    async function loadTopic(id) {
      renderNewsfeedContentLoading("Preparing topic package...", "topic");
      const data = await newsfeedJson(workerUrl, `/newsfeed/topic?id=${encodeURIComponent(id)}&${newsfeedPreferenceQuery(state)}`);
      state.topics = data.topics || state.topics || [];
      setNewsfeedStatus("");
      refreshNewsfeedChrome(state);
      renderNewsfeedSidebar(state);
      renderNewsfeedTopic(state, data.topic, data.items || []);
    }

    async function reloadCurrentNewsfeed() {
      if (state.currentView === "explore") return loadExplore(state.exploreCategory);
      if (state.currentView === "topic" && state.currentTopic) return loadTopic(state.currentTopic.id);
      if (state.currentView === "email") {
        renderNewsfeedEmailView(state);
        return null;
      }
      return loadHome();
    }

    async function saveNewsfeedPreferences(reload = true) {
      state.preferencesReady = true;
      refreshNewsfeedChrome(state);
      const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
        method: "POST",
        body: JSON.stringify({
          preferred_regions: state.preferredRegions,
          interface_language: state.interfaceLanguage,
        }),
      });
      applyNewsfeedSettings(state, data.settings || state.settings || {});
      refreshNewsfeedChrome(state);
      if (reload) await reloadCurrentNewsfeed();
    }

    function closeSidebar() {
      const sidebar = document.getElementById("newsfeedSidebar");
      if (sidebar) sidebar.classList.remove("is-open");
    }

    app.addEventListener("click", async (event) => {
      const control = event.target.closest("[data-action]");
      if (!control) return;
      const action = control.dataset.action;
      try {
        if (action === "toggle-sidebar") {
          document.getElementById("newsfeedSidebar")?.classList.toggle("is-open");
          return;
        }
        if (action === "show-feed") {
          closeSidebar();
          if (!state.home) await loadHome();
          else renderNewsfeedHome(state);
          return;
        }
        if (action === "show-add") {
          closeSidebar();
          renderNewsfeedAdd(state);
          return;
        }
        if (action === "show-explore") {
          closeSidebar();
          await loadExplore();
          return;
        }
        if (action === "show-email") {
          closeSidebar();
          renderNewsfeedEmailView(state);
          return;
        }
        if (action === "send-email-test" || action === "send-email-now") {
          const isTest = action === "send-email-test";
          const status = document.getElementById("newsEmailStatus");
          const button = document.getElementById(isTest ? "newsEmailTest" : "newsEmailSend");
          if (status) {
            status.className = "status-line";
            status.textContent = isTest ? "Sending test digest email..." : "Sending newsletter digest...";
          }
          if (button) {
            button.disabled = true;
            button.classList.add("is-loading");
            button.textContent = "Sending...";
          }
          const data = await newsfeedJson(workerUrl, isTest ? "/newsfeed/email-test" : "/newsfeed/email-send", {
            method: "POST",
            body: JSON.stringify(newsfeedEmailPayloadFromForm(state)),
          });
          applyNewsfeedSettings(state, data.settings || state.settings || {});
          renderNewsfeedEmailView(state);
          const nextStatus = document.getElementById("newsEmailStatus");
          if (nextStatus) {
            nextStatus.className = data.sent ? "status-line ok" : "status-line error";
            const idSuffix = data.message_id ? ` (${data.message_id})` : "";
            nextStatus.textContent = data.sent
              ? (isTest
                ? `Test digest accepted by ${data.provider || "email provider"}.${idSuffix}`
                : `Newsletter accepted by ${data.provider || "email provider"}.${idSuffix}`)
              : (data.detail || state.settings.digest_last_send_detail || (isTest ? "Test email was not sent." : "Newsletter email was not sent."));
          }
          return;
        }
        if (action === "toggle-region-menu") {
          const menu = document.getElementById("newsRegionMenu");
          const toggle = document.getElementById("newsRegionToggle");
          if (menu) {
            const nextHidden = !menu.hidden ? true : false;
            menu.hidden = nextHidden;
            if (toggle) toggle.setAttribute("aria-expanded", String(!nextHidden));
          }
          return;
        }
        if (action === "play-briefing") {
          await playNewsfeedBriefing(state);
          return;
        }
        if (action === "close-briefing") {
          stopNewsfeedBriefing(state);
          const panel = document.getElementById("newsBriefingPanel");
          if (panel) panel.hidden = true;
          return;
        }
        if (action === "briefing-prev" || action === "briefing-next") {
          renderNewsfeedBriefingPanel(state, {
            status: state.briefingScript || newsfeedText(state, "playBriefing"),
            progress: state.briefingProgress || 0,
            playing: state.briefingPlaying,
          });
          return;
        }
        if (action === "home-category") {
          state.homeCategory = control.dataset.category || "";
          renderNewsfeedHome(state);
          return;
        }
        if (action === "explore-category") {
          state.exploreCategory = control.dataset.category || "";
          renderNewsfeedExplore(state);
          return;
        }
        if (action === "suggest-topic") {
          const input = document.getElementById("newsTopicInput");
          if (input) input.value = control.dataset.topic || "";
          return;
        }
        if (action === "open-topic") {
          closeSidebar();
          await loadTopic(control.dataset.id || "");
          return;
        }
        if (action === "pin-topic") {
          const id = control.dataset.id || "";
          const topic = (state.topics || []).find((item) => String(item.id) === id);
          const pinned = !(topic && topic.pinned);
          await newsfeedJson(workerUrl, "/newsfeed/topics/pin", {
            method: "POST",
            body: JSON.stringify({ id, pinned }),
          });
          if (topic) topic.pinned = pinned;
          renderNewsfeedSidebar(state);
          return;
        }
        if (action === "open-article") {
          const id = String(control.dataset.id || "");
          const article = state.articles.get(id);
          state.lastListView = state.currentView === "article" ? state.lastListView : state.currentView;
          await renderNewsfeedArticle(state, article ? { ...article, output_language: state.articleLanguages.get(id) || state.outputLanguage || "en" } : article);
          return;
        }
        if (action === "article-back") {
          if (state.lastListView === "explore") renderNewsfeedExplore(state);
          else if (state.lastListView === "topic") renderNewsfeedTopic(state, state.currentTopic, state.currentTopicItems);
          else renderNewsfeedHome(state);
        }
      } catch (error) {
        setNewsfeedStatus(error.message || "Newsfeed request failed.", "error");
      }
    });

    app.addEventListener("submit", async (event) => {
      if (event.target && event.target.id === "newsTopicForm") {
        event.preventDefault();
        const input = document.getElementById("newsTopicInput");
        const language = document.getElementById("newsTopicLanguage");
        const status = document.getElementById("newsTopicStatus");
        const submit = document.getElementById("newsTopicSubmit");
        const topic = input ? input.value.trim() : "";
        if (!topic) return;
        const outputLanguage = language ? language.value : "en";
        state.outputLanguage = outputLanguage || "en";
        if (status) {
          status.className = "status-line";
          status.textContent = "Creating topic package...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "…";
        }
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/topics", {
            method: "POST",
            body: JSON.stringify({ topic, output_language: outputLanguage, preferred_regions: state.preferredRegions }),
          });
          state.topics = data.topics || state.topics || [];
          renderNewsfeedSidebar(state);
          renderNewsfeedTopic(state, data.topic, data.items || []);
          setNewsfeedStatus(data.pending ? "Topic created. Stories are loading; open it again in a moment." : "", data.pending ? "ok" : "");
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = error.message || "Could not create topic.";
          }
        } finally {
          if (submit) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
          submit.textContent = "↑";
          }
        }
      }
      if (event.target && event.target.id === "newsCustomRegionForm") {
        event.preventDefault();
        const input = document.getElementById("newsCustomRegionInput");
        const value = input ? input.value.trim() : "";
        if (!value) return;
        state.preferredRegions = normalizeNewsfeedRegionsClient([...(state.preferredRegions || []), value]);
        if (input) input.value = "";
        await saveNewsfeedPreferences(true);
      }
      if (event.target && event.target.id === "newsEmailForm") {
        event.preventDefault();
        const status = document.getElementById("newsEmailStatus");
        const submit = document.getElementById("newsEmailSubmit");
        const payload = newsfeedEmailPayloadFromForm(state);
        if (status) {
          status.className = "status-line";
          status.textContent = "Saving digest email settings...";
        }
        if (submit) {
          submit.disabled = true;
          submit.classList.add("is-loading");
          submit.textContent = "Saving...";
        }
        try {
          const data = await newsfeedJson(workerUrl, "/newsfeed/settings", {
            method: "POST",
            body: JSON.stringify(payload),
          });
          state.settings = data.settings || state.settings || {};
          if (status) {
            status.className = "status-line ok";
            status.textContent = state.settings.email_provider_configured === false
              ? "Settings saved. Email delivery starts after the email sender is configured."
              : "Settings saved. Daily Digest will be sent at the selected time.";
          }
        } catch (error) {
          if (status) {
            status.className = "status-line error";
            status.textContent = error.message || "Could not save email settings.";
          }
        } finally {
          if (submit) {
            submit.disabled = false;
            submit.classList.remove("is-loading");
            submit.textContent = newsfeedText(state, "saveEmail");
          }
        }
      }
    });

    app.addEventListener("change", async (event) => {
      const target = event.target;
      try {
        if (target && target.dataset && target.dataset.action === "region-checkbox") {
          const selected = Array.from(document.querySelectorAll("[data-action='region-checkbox']:checked"))
            .map((item) => item.value);
          state.preferredRegions = normalizeNewsfeedRegionsClient(selected);
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsInterfaceLanguage") {
          state.interfaceLanguage = newsfeedLanguageCode(target.value || "en");
          state.outputLanguage = state.interfaceLanguage;
          await saveNewsfeedPreferences(true);
        }
        if (target && target.id === "newsTopicLanguage") {
          state.outputLanguage = newsfeedLanguageCode(target.value || "en");
        }
      } catch (error) {
        setNewsfeedStatus(error.message || "Could not save preferences.", "error");
      }
    });

    await loadHome();
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
        : page === "newsfeed"
          ? initNewsfeed
          : initIndex;
  boot().catch((error) => {
    const target = page === "report"
      ? document.getElementById("detail")
      : page === "external"
        ? document.getElementById("externalDetail")
        : page === "delivery"
          ? document.getElementById("delivery")
          : page === "newsfeed"
            ? document.getElementById("newsfeedApp")
            : document.getElementById("results");
    if (target) target.innerHTML = `<div class="error-state">${escapeHtml(error.message)}</div>`;
  });
}());
