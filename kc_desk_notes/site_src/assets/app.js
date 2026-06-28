(function () {
  const page = document.body.dataset.page;
  const CONTACT_WECHAT = "macroGate";
  const ADMIN_TOKEN_KEY = "kcdesk_admin_token";
  const ADMIN_PLAIN_KEY = "kcdesk_admin_plain_key";
  const ADMIN_COOKIE_NAME = "kcdesk_admin_token";
  const ADMIN_COOKIE_MAX_AGE = 180 * 24 * 60 * 60;
  const DOWNLOAD_PASSWORD_KEY = "kcdesk_download_password";
  const AUTH_SESSION_KEY = "kcdesk_auth_session";
  const PADDLE_SCRIPT_URL = "https://cdn.paddle.com/paddle/v2/paddle.js";
  const REPORT_PRICE_QUANTITY = 2000;
  let paddleConfigPromise = null;
  let paddleLoadPromise = null;
  let paddleInitialized = false;

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
    const reportCard = context.item
      ? `
        <div class="plan-card">
          <strong>单篇报告 ¥20</strong>
          <span>${escapeHtml(reportTitle)}</span>
          <button class="primary" id="accountBuyReport" type="button">购买本篇</button>
        </div>
      `
      : "";
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
              <button class="secondary-button" id="accountLogout" type="button">退出登录</button>
            </div>
          </div>
          <div class="plan-grid" id="accountPlanGrid" hidden>
            ${reportCard}
            <div class="plan-card">
              <strong>年度会员 ¥600</strong>
              <span>一年内下载大部分可用报告，适合高频使用。</span>
              <button class="primary" id="accountBuyAnnual" type="button">开通年度</button>
            </div>
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

  function windowPaddle() {
    return window.Paddle;
  }

  async function fetchPaddleConfig(workerUrl) {
    if (paddleConfigPromise) return paddleConfigPromise;
    paddleConfigPromise = fetch(`${workerUrl}/paddle-config`, { cache: "no-store" })
      .then(async (response) => {
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw new Error(data.detail || "支付配置接口异常。");
        return { ...(data.config || {}), __missing: data.missing || [] };
      });
    return paddleConfigPromise;
  }

  async function paymentReady(workerUrl) {
    try {
      const config = await fetchPaddleConfig(workerUrl);
      return !(config.__missing && config.__missing.length);
    } catch (_error) {
      return false;
    }
  }

  function loadPaddleScript() {
    if (windowPaddle()) return Promise.resolve();
    return new Promise((resolve, reject) => {
      const existing = document.querySelector(`script[src="${PADDLE_SCRIPT_URL}"]`);
      if (existing) {
        existing.addEventListener("load", () => resolve(), { once: true });
        existing.addEventListener("error", () => reject(new Error("Paddle.js 加载失败。")), { once: true });
        return;
      }
      const script = document.createElement("script");
      script.src = PADDLE_SCRIPT_URL;
      script.async = true;
      script.onload = () => resolve();
      script.onerror = () => reject(new Error("Paddle.js 加载失败。"));
      document.head.appendChild(script);
    });
  }

  async function ensurePaddle(workerUrl) {
    if (paddleLoadPromise) return paddleLoadPromise;
    paddleLoadPromise = Promise.all([fetchPaddleConfig(workerUrl), loadPaddleScript()]).then(([config]) => {
      const paddle = windowPaddle();
      if (!paddle) throw new Error("Paddle.js 未就绪。");
      if (config.__missing && config.__missing.length) {
        throw new Error("支付功能还没有配置完成。");
      }
      if (config.PADDLE_ENV === "sandbox" && paddle.Environment && paddle.Environment.set) {
        paddle.Environment.set("sandbox");
      }
      if (!paddleInitialized) {
        if (!config.PADDLE_CLIENT_TOKEN) throw new Error("支付配置缺少：PADDLE_CLIENT_TOKEN");
        paddle.Initialize({
          token: config.PADDLE_CLIENT_TOKEN,
          eventCallback: (event) => {
            const name = String(event && (event.name || event.eventName || event.type) || "");
            if (name === "checkout.completed") {
              document.dispatchEvent(new CustomEvent("kcdesk-checkout-complete"));
            }
          },
        });
        paddleInitialized = true;
      }
      return config;
    });
    return paddleLoadPromise;
  }

  async function requireAccount(workerUrl, context = {}) {
    let session = loadAuthSession();
    if (session) return session;
    if (!document.getElementById("accountModal")) showAccountModal(workerUrl, context);
    throw new Error("请先登录或注册账号。");
  }

  async function openCheckout(workerUrl, plan, context = {}, statusTarget) {
    const status = statusTarget || (() => {});
    const session = await requireAccount(workerUrl, context);
    status("正在打开支付窗口…");
    const config = await ensurePaddle(workerUrl);
    const paddle = windowPaddle();
    const item = context.item || {};
    const source = context.source || "catalog";
    const isReport = plan === "single_report";
    const priceId = isReport ? config.PADDLE_PRICE_REPORT_CNY_CENT : config.PADDLE_PRICE_YEARLY;
    if (!priceId) throw new Error(isReport ? "支付配置缺少单篇报告价格。" : "支付配置缺少年度价格。");
    paddle.Checkout.open({
      items: [{ priceId, quantity: isReport ? REPORT_PRICE_QUANTITY : 1 }],
      customer: { email: session.user.email },
      customData: {
        plan,
        order_kind: isReport ? "report_purchase" : "membership",
        email: session.user.email,
        username: session.user.username || "",
        account_id: session.user.id || "",
        report_id: isReport ? item.id || "" : "",
        source,
        title: isReport ? titleText(item).slice(0, 500) : "",
        quantity: isReport ? REPORT_PRICE_QUANTITY : 1,
      },
      settings: {
        displayMode: "overlay",
        theme: "light",
        successUrl: checkoutSuccessUrl(plan),
      },
    });
    status("支付窗口已打开。完成后页面会自动更新，也可以稍后刷新。", "ok");
  }

  function checkoutSuccessUrl(plan) {
    const url = new URL(window.location.href);
    url.searchParams.set("checkout", "success");
    url.searchParams.set("plan", plan);
    return url.toString();
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
    const buyReport = document.getElementById("accountBuyReport");
    const buyAnnual = document.getElementById("accountBuyAnnual");
    const status = document.getElementById("accountModalStatus");
    const planGrid = document.getElementById("accountPlanGrid");
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
        setStatus("已登录。", "ok");
        fetch(`${workerUrl}/entitlement`, { cache: "no-store", headers: authHeaders() })
          .then((response) => response.json())
          .then((data) => {
            const entitlement = data && data.entitlement;
            if (entitlement && entitlement.active && entitlement.plan === "annual") {
              setStatus(`年度会员有效${entitlement.current_period_end ? `至 ${entitlement.current_period_end.slice(0, 10)}` : ""}。`, "ok");
            }
          })
          .catch(() => {});
      } else {
        captchaToken = "";
        loadAccountCaptcha(workerUrl, status).then((token) => { captchaToken = token; });
      }
      paymentReady(workerUrl).then((ready) => {
        if (planGrid) planGrid.hidden = !ready;
        if (!ready && !signedIn) setStatus("付费功能正在配置中，暂时请使用报告密码或发货链接下载。");
      });
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

    if (buyReport) {
      buyReport.addEventListener("click", async () => {
        buyReport.disabled = true;
        try {
          await openCheckout(workerUrl, "single_report", context, setStatus);
        } catch (error) {
          setStatus(error.message || "支付窗口打开失败。", "error");
        } finally {
          buyReport.disabled = false;
        }
      });
    }

    buyAnnual.addEventListener("click", async () => {
      buyAnnual.disabled = true;
      try {
        await openCheckout(workerUrl, "annual", context, setStatus);
      } catch (error) {
        setStatus(error.message || "支付窗口打开失败。", "error");
      } finally {
        buyAnnual.disabled = false;
      }
    });

    refreshUi();
    if (!loadAuthSession() && username) username.focus();
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

  function externalMeta(item) {
    const meta = [item.institution, item.date, item.file_type]
      .map((value) => String(value || "").trim())
      .filter(Boolean)
      .join(" · ");
    return meta;
  }

  function externalRow(item) {
    const meta = externalMeta(item);
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    return `
      <button class="related-row external-row" type="button" data-id="${escapeHtml(item.id)}">
        <span class="related-title">
          <span>${escapeHtml(item.title)}</span>
          ${zh ? `<span class="related-title-zh">${escapeHtml(zh)}</span>` : ""}
        </span>
        <span class="related-meta">${escapeHtml(meta)}</span>
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
    let externalTimer = 0;
    let externalToken = 0;
    const externalItems = new Map();

    function setExternalStatus(text, kind) {
      if (!externalStatus) return;
      externalStatus.className = kind ? `status-line ${kind}` : "status-line";
      externalStatus.textContent = text || "";
    }

    async function runExternalSearch(query) {
      if (!externalSection || !externalResults) return;
      if (!externalUrl || !query) {
        externalSection.hidden = true;
        externalResults.innerHTML = "";
        externalItems.clear();
        if (externalCount) externalCount.textContent = "";
        setExternalStatus("");
        return;
      }
      const token = ++externalToken;
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
        if (externalCount) externalCount.textContent = items.length ? `${items.length} 条` : "";
        externalResults.innerHTML = items.length
          ? items.map(externalRow).join("")
          : '<div class="empty-state">暂无匹配结果。</div>';
      } catch (error) {
        if (token !== externalToken) return;
        if (externalCount) externalCount.textContent = "";
        externalResults.innerHTML = "";
        setExternalStatus(error.message || "搜索暂不可用。", "error");
      }
    }

    function scheduleExternalSearch() {
      window.clearTimeout(externalTimer);
      const query = input.value.trim();
      externalTimer = window.setTimeout(() => runExternalSearch(query), 400);
    }

    input.addEventListener("input", scheduleExternalSearch);
    clearFilters.addEventListener("click", () => runExternalSearch(""));
    externalResults.addEventListener("click", (event) => {
      const row = event.target.closest(".external-row");
      if (!row) return;
      const item = externalItems.get(String(row.dataset.id));
      if (item) openInNewTab(externalPageUrl(item, ""));
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

  function accountAccessMarkup() {
    return `
      <section class="account-access" id="accountAccess" hidden>
        <h3>Account access</h3>
        <p class="subtle" id="accountAccessHint">登录后可查看账号下载权限。</p>
        <div class="account-access-actions">
          <button class="secondary-button" id="openAccountPanel" type="button">登录 / 账号</button>
          <button class="primary" id="accountDownloadReport" type="button" hidden>会员下载</button>
          <button class="secondary-button" id="buySingleReport" type="button" hidden>单篇 ¥20</button>
          <button class="secondary-button" id="buyAnnualPlan" type="button" hidden>年度 ¥600</button>
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
    const buySingle = document.getElementById("buySingleReport");
    const buyAnnual = document.getElementById("buyAnnualPlan");
    const hint = document.getElementById("accountAccessHint");
    const status = document.getElementById("accountAccessStatus");
    const context = { item, source };
    let canPay = false;

    function statusTarget(text, kind) {
      setLineStatus(status, text, kind);
    }

    async function refresh() {
      const session = loadAuthSession();
      canPay = await paymentReady(workerUrl);
      panel.hidden = !session && !canPay;
      buyAnnual.hidden = !canPay;
      buySingle.hidden = !canPay;
      hint.textContent = canPay
        ? "登录后可购买单篇报告，或开通年度会员下载大部分可用报告。"
        : "登录后可查看账号下载权限。";
      accountDownload.hidden = true;
      if (!session) {
        if (canPay) statusTarget("登录后可购买单篇报告或开通年度会员。");
        else statusTarget("");
        return;
      }
      statusTarget("正在读取账号权益…");
      try {
        const access = await fetchReportAccess(workerUrl, item, source);
        if (access && access.can_download) {
          accountDownload.hidden = false;
          buySingle.hidden = true;
          statusTarget("当前账号已解锁此报告，可直接下载。", "ok");
        } else {
          buySingle.hidden = !canPay;
          statusTarget(canPay ? "当前账号尚未解锁此报告。" : "付费功能正在配置中，暂时请使用报告密码或发货链接下载。");
        }
      } catch (error) {
        statusTarget(error.message || "账号状态读取失败。", "error");
      }
    }

    openAccount.addEventListener("click", () => showAccountModal(workerUrl, context));
    buySingle.addEventListener("click", async () => {
      buySingle.disabled = true;
      try {
        await openCheckout(workerUrl, "single_report", context, statusTarget);
      } catch (error) {
        statusTarget(error.message || "支付窗口打开失败。", "error");
      } finally {
        buySingle.disabled = false;
      }
    });
    buyAnnual.addEventListener("click", async () => {
      buyAnnual.disabled = true;
      try {
        await openCheckout(workerUrl, "annual", context, statusTarget);
      } catch (error) {
        statusTarget(error.message || "支付窗口打开失败。", "error");
      } finally {
        buyAnnual.disabled = false;
      }
    });
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
    document.addEventListener("kcdesk-checkout-complete", refresh);
    refresh();
  }

  function reportPageUrl(id, options = {}) {
    const url = new URL("report.html", window.location.href);
    url.searchParams.set("id", id);
    if (options.password) url.searchParams.set("password", options.password);
    return url.toString();
  }

  function openInNewTab(url) {
    const opened = window.open(url, "_blank", "noopener,noreferrer");
    if (opened) {
      opened.opener = null;
      return;
    }
    window.location.href = url;
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
    if (password) url.searchParams.set("password", password);
    if (item.title) url.searchParams.set("title", item.title);
    if (item.title_cn) url.searchParams.set("title_cn", item.title_cn);
    if (item.institution) url.searchParams.set("institution", item.institution);
    if (item.date) url.searchParams.set("date", item.date);
    if (item.file_type) url.searchParams.set("file_type", item.file_type);
    return url.toString();
  }

  async function requestReportPassword(workerUrl, id) {
    const token = getAdminToken();
    if (!token) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
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

  async function requestExternalPassword(workerUrl, id) {
    const token = getAdminToken();
    if (!token) throw new Error("Private tools are locked.");
    try {
      const response = await fetch(`${workerUrl}/admin/report-password`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ id, token, source: "external" }),
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
        ${workerUrl ? accountAccessMarkup() : ""}
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
    return {
      id: String(params.get("id") || "").trim(),
      title: params.get("title") || "Report",
      title_cn: params.get("title_cn") || "",
      institution: params.get("institution") || "",
      date: params.get("date") || "",
      file_type: params.get("file_type") || "",
    };
  }

  async function fetchExternalPdf(workerUrl, id, password, statusTarget, options = {}) {
    statusTarget("正在获取报告…");
    const response = await fetch(`${workerUrl}/external/pdf`, {
      method: "POST",
      headers: { "Content-Type": "application/json", ...(options.auth ? authHeaders() : {}) },
      cache: "no-store",
      body: JSON.stringify({ id, password: password || "" }),
    });
    if (response.status === 202) return { pending: true };
    if (!response.ok) {
      let message = `下载失败 (${response.status})`;
      try {
        const data = await response.json();
        if (data.error) message = data.error;
      } catch (_error) {
        // Keep generic message.
      }
      if (response.status === 503 && /background|configured|prepar/i.test(message)) {
        return { pending: true };
      }
      if (response.status === 401) clearRememberedDownloadPassword();
      throw new Error(message);
    }
    const blob = await response.blob();
    triggerBlobDownload(blob, response.headers.get("Content-Disposition"), `${id}.pdf`);
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
        statusTarget("报告准备时间超过预期。请保留这个页面，稍后再次点击下载；如果多次失败请联系 macroGate。", "error");
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
        }
      } catch (_error) {
        // Keep polling while the background grab runs.
      }
    }, 15000);
  }

  async function downloadExternalWithAccount(workerUrl, item, statusTarget) {
    const result = await fetchExternalPdf(workerUrl, item.id, "", statusTarget, { auth: true });
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
    if (!/^[0-9]{6,25}$/.test(item.id)) {
      target.innerHTML = '<div class="error-state">Report not found.</div>';
      return;
    }

    const config = await loadOptionalJson("data/config.json", {});
    const workerUrl = workerBaseUrl(config);
    initAccountGate(workerUrl);
    initAdminGate(workerUrl);

    const passwordFromLink = params.get("password") || "";
    const meta = externalMeta(item);
    const zh = item.title_cn && item.title_cn !== item.title ? item.title_cn : "";
    document.title = `${item.title || "Report"} | KC Desk Notes`;
    target.innerHTML = `
      <div>
        <h1 class="detail-title">${escapeHtml(item.title || "Report")}</h1>
        ${zh ? `<p class="detail-title-zh">${escapeHtml(zh)}</p>` : ""}
        <p class="subtle">Password-protected report delivery.</p>
      </div>
      <div class="detail-grid">
        ${field("Source", "其他报告")}
        ${field("Institution", item.institution || "-")}
        ${field("Date", item.date || "-")}
        ${field("Type", item.file_type || "-")}
      </div>
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
      ${workerUrl ? accountAccessMarkup() : ""}
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
    `;

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
      adminTools.hidden = !getAdminToken();
    }

    async function submitDownload(event) {
      if (event) event.preventDefault();
      if (!input.value) {
        setStatus("Password is required.", "error");
        return;
      }
      button.disabled = true;
      try {
          const result = await fetchExternalPdf(workerUrl, item.id, input.value, setStatus);
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
    refreshAdmin();
    initReportAccessControls(item, workerUrl, "external", (statusTarget) => (
      downloadExternalWithAccount(workerUrl, item, statusTarget)
    ));

    generate.addEventListener("click", async () => {
      generate.disabled = true;
      linkInput.value = "";
      deliveryStatus.className = "status-line";
      deliveryStatus.textContent = "Generating...";
      try {
        const data = await requestExternalPassword(workerUrl, item.id);
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
