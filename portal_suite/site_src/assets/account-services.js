(() => {
  "use strict";
  // Loaded only from account tools; secrets remain in the current modal's DOM.
  window.PortalAccountServices = function createAccountServices(dependencies) {
    const { loadAuthSession, authHeaders, escapeHtml, isAdminASession } = dependencies;
  function accountToolError(code) {
    const messages = {
      authentication_required: "登录状态已失效，请重新登录。",
      api_permission_denied: "尚未开通 API 权限或权限已到期，请联系管理员。",
      key_invalid: "密钥已失效，请刷新列表。",
      key_expired: "密钥已到期，请生成新密钥。",
      scope_denied: "当前 API 权限不包含此操作。",
      rate_limited: "操作较频繁，请稍后再试。",
      key_limit: "最多可保留 5 个有效密钥，请先撤销不用的密钥。",
      invalid_request: "请检查名称、授权范围和未来的到期时间。",
      REMINDER_AUTH: "请重新登录后查看到期提醒。",
      REMINDER_FORBIDDEN: "当前账号不能查看该用户的到期提醒。",
      REMINDER_STORAGE: "提醒服务暂时不可用，请稍后刷新。",
      REMINDER_INVALID: "提醒设置未能保存，请刷新后重试。",
      CREDIT_AUTH: "请重新登录后查看 AI 研究次数。",
      CREDIT_STORAGE: "研究次数暂时无法读取，请稍后刷新。",
      CREDIT_BUSY: "额度正在更新，请稍后使用同一笔操作重试。",
      CREDIT_INVALID: "请填写 1–10000 的整数次数和添加说明。",
      CREDIT_OPERATION_CONFLICT: "这笔操作的内容已改变，请刷新并核对当前余额。",
      service_unavailable: "账号服务暂时不可用，请稍后刷新。",
    };
    return messages[code] || "操作未能确认完成，请先刷新当前状态再重试。";
  }

  async function accountToolRequest(workerUrl, path, options = {}) {
    const controller = new AbortController();
    const timer = setTimeout(() => controller.abort(), 20000);
    try {
      const response = await fetch(`${workerUrl}${path}`, {
        ...options, cache: "no-store", signal: controller.signal,
        headers: { "Content-Type": "application/json", ...authHeaders() },
      });
      const data = await response.json().catch(() => null);
      if (!response.ok || !data || data.ok !== true) {
        throw new Error(accountToolError(response.status === 401 ? "authentication_required" : data?.error || data?.code));
      }
      return data;
    } catch (error) {
      if (error.name === "AbortError" || error instanceof TypeError) {
        throw new Error("连接中断或等待超时，结果尚未确认。请先刷新状态，避免重复添加或生成。");
      }
      throw error;
    } finally { clearTimeout(timer); }
  }

  function apiAccessDate(value) {
    const date = new Date(value);
    return value && Number.isFinite(date.getTime()) ? date.toLocaleString("zh-CN") : "未设置";
  }

  function accountApiKeysMarkup(keys) {
    if (!keys.length) return '<p class="account-tool-note">还没有 API 密钥。</p>';
    return keys.map((key) => {
      const expired = Boolean(key.expires_at && Date.parse(key.expires_at) <= Date.now());
      const inactive = Boolean(key.revoked_at) || expired;
      return `<div class="account-api-key"><div><strong>${escapeHtml(key.name || "未命名密钥")}</strong><span>创建：${escapeHtml(apiAccessDate(key.created_at))} · 到期：${escapeHtml(apiAccessDate(key.expires_at))}</span><small>${escapeHtml((key.scopes || []).join(" · "))}</small></div>${inactive ? `<span>${key.revoked_at ? "已撤销" : "已到期"}</span>` : `<button class="secondary-button" type="button" data-api-revoke="${escapeHtml(key.id)}">撤销</button>`}</div>`;
    }).join("");
  }

  function initAccountApiControls(workerUrl, modal) {
    const byId = (id) => modal.querySelector(`#${id}`);
    const panel = byId("accountApiPanel");
    if (!panel) return { close() {} };
    const grantNode = byId("accountApiGrant");
    const list = byId("accountApiKeys");
    const form = byId("accountApiCreate");
    const name = byId("accountApiKeyName");
    const create = byId("accountApiCreateButton");
    const refresh = byId("accountApiRefresh");
    const status = byId("accountApiStatus");
    const secretPanel = byId("accountApiSecretPanel");
    const secretNode = byId("accountApiSecret");
    const copy = byId("accountApiCopy");
    let closed = false, busy = false, revision = 0, loaded = false;
    let grant = null, keys = [], secretId = "";
    const owner = () => String(loadAuthSession()?.token || "");
    let currentOwner = owner();
    const setStatus = (text, type = "") => { status.textContent = text; status.className = `status-line ${type}`; };
    function clearSecret() { secretNode.textContent = ""; secretId = ""; secretPanel.hidden = true; }
    function render() {
      const active = Boolean(grant?.enabled && Date.parse(grant.expires_at) > Date.now());
      create.disabled = busy || !active;
      name.disabled = busy || !active;
      refresh.disabled = busy;
      list.innerHTML = accountApiKeysMarkup(keys);
      list.querySelectorAll("[data-api-revoke]").forEach((button) => { button.disabled = busy; });
      if (grant) grantNode.textContent = active
        ? `API 已开通 · ${grant.access_mode === "granted_corpus" ? "单独授权的报告范围" : "沿用网站现有下载权限"} · ${apiAccessDate(grant.expires_at)} 到期。`
        : "API 未开通或已到期。请联系管理员开通后再生成密钥。";
    }
    function reset() {
      revision += 1; busy = false; loaded = false; grant = null; keys = [];
      clearSecret(); name.value = ""; grantNode.textContent = ""; list.innerHTML = ""; setStatus(""); render();
    }
    function valid(ticket, token) { return !closed && modal.isConnected !== false && ticket === revision && token && token === owner(); }
    async function perform(path, options, pending, done) {
      if (closed || busy || !owner()) return;
      const token = owner(), ticket = ++revision;
      busy = true; render(); setStatus(pending);
      try {
        const data = await accountToolRequest(workerUrl, path, options);
        if (valid(ticket, token)) done(data);
      } catch (error) {
        if (valid(ticket, token)) setStatus(error.message, "error");
      } finally {
        if (valid(ticket, token)) { busy = false; render(); }
      }
    }
    function load() {
      if (busy) return;
      clearSecret(); grant = null; loaded = false;
      return perform("/account/content-api", {}, "正在读取 API 权限与密钥…", (data) => {
        grant = data.grant; keys = Array.isArray(data.keys) ? data.keys : []; loaded = true;
        setStatus("API 权限与密钥已更新。", "ok");
      });
    }
    panel.addEventListener("toggle", () => {
      if (panel.open && !loaded) load();
      if (!panel.open) clearSecret();
    });
    refresh.addEventListener("click", load);
    form.addEventListener("submit", (event) => {
      event.preventDefault();
      if (busy || create.disabled) return;
      const label = name.value.trim();
      if (!label || label.length > 80) { setStatus("请填写 1–80 字的密钥名称。", "error"); return; }
      clearSecret();
      perform("/account/content-api/keys", { method: "POST", body: JSON.stringify({ name: label }) }, "正在生成密钥，请稍候…", (data) => {
        if (!data.secret || !data.key) { setStatus("密钥返回不完整。请刷新列表检查，必要时撤销后重新生成。", "error"); return; }
        keys.unshift(data.key); name.value = "";
        if (panel.open) { secretNode.textContent = data.secret; secretId = data.key.id; secretPanel.hidden = false; }
        setStatus(panel.open ? "密钥已生成，请立即保存。" : "密钥已生成，面板关闭后不会显示完整密钥；可撤销后重新生成。", "ok");
      });
    });
    list.addEventListener("click", (event) => {
      const button = event.target.closest("[data-api-revoke]");
      if (!button || busy) return;
      const id = button.dataset.apiRevoke;
      if (secretId === id) clearSecret();
      perform(`/account/content-api/keys/${encodeURIComponent(id)}`, { method: "DELETE" }, "正在撤销密钥…", () => {
        keys = keys.map((key) => key.id === id ? { ...key, revoked_at: new Date().toISOString() } : key);
        setStatus("密钥已撤销，不能再用于访问 API。", "ok");
      });
    });
    byId("accountApiDismiss").addEventListener("click", clearSecret);
    copy.addEventListener("click", async () => {
      const token = owner(), ticket = revision;
      if (!secretNode.textContent) return;
      try {
        await navigator.clipboard.writeText(secretNode.textContent);
        if (valid(ticket, token) && !secretPanel.hidden) setStatus("已复制密钥，请保存在你的服务端配置中。", "ok");
      } catch (_error) {
        if (valid(ticket, token)) setStatus("无法自动复制，请手动选中并复制上方密钥。", "error");
      }
    });
    function onAuthChange() {
      if (owner() === currentOwner) return;
      currentOwner = owner(); reset();
      if (panel.open && currentOwner) load();
    }
    document.addEventListener("portal-auth-change", onAuthChange);
    if (panel.open) load();
    return { close() { closed = true; reset(); document.removeEventListener("portal-auth-change", onAuthChange); } };
  }

  function renderExpiryReminderDetails(modal, prefix, data) {
    const summary = modal.querySelector(`#${prefix}Summary`);
    const subject = modal.querySelector(`#${prefix}Subject`);
    const text = modal.querySelector(`#${prefix}Text`);
    if (!data) { summary.textContent = ""; subject.textContent = ""; text.textContent = ""; return; }
    const reminder = data.reminder || {};
    const parts = [data.preferences?.enabled ? "到期邮件提醒已开启。" : "到期邮件提醒已关闭。"];
    if (reminder.expires_at) parts.push(`${reminder.kind === "trial" ? "试用" : "会员"}权益到期：${apiAccessDate(reminder.expires_at)}。`);
    if (data.preferences?.enabled && reminder.eligible && reminder.next_send_at) parts.push(`下一次计划提醒：${apiAccessDate(reminder.next_send_at)}。`);
    else if (data.preferences?.enabled && !reminder.eligible) {
      const reasons = { disabled: "账号已停用，当前不安排提醒。", privileged: "当前账号无需到期提醒。", no_email: "账号暂无可用收件邮箱。", lifetime: "当前权益长期有效，无需到期提醒。", no_membership: "当前没有会员或试用到期提醒。" };
      parts.push(reasons[reminder.reason] || "当前没有符合发送条件的到期提醒。");
    }
    if (reminder.short_trial) parts.push("此权益为短期试用，提醒安排以实际有效期为准。");
    if (reminder.last_attempt_at) {
      const statuses = { pending: "处理中，尚未确认", sent: "邮件服务已接受", failed: "发送失败", unknown: "结果尚未确认", cancelled: "已取消" };
      parts.push(`上次处理：${apiAccessDate(reminder.last_attempt_at)} · ${statuses[reminder.last_status] || "状态待确认"}（不代表邮件已送达）。`);
    }
    if (data.scan) parts.push(`提醒扫描：${data.scan.complete ? "已完成本轮" : "本轮尚未完成"}，已处理 ${Number(data.scan.processed || 0)} 个账号、尝试发送 ${Number(data.scan.attempted || 0)} 次。`);
    summary.textContent = parts.join(" ");
    subject.textContent = data.preview?.subject || "暂无可预览的提醒内容";
    text.textContent = data.preview?.text || "";
  }

  function initAccountReminderControls(workerUrl, modal) {
    const byId = (id) => modal.querySelector(`#${id}`);
    const panel = byId("accountReminderPanel");
    if (!panel) return { close() {} };
    const checkbox = byId("accountReminderEnabled");
    const refresh = byId("accountReminderRefresh");
    const status = byId("accountReminderStatus");
    let closed = false, busy = false, loaded = false, enabled = false, revision = 0;
    const owner = () => String(loadAuthSession()?.token || "");
    let currentOwner = owner();
    async function request(options = {}) {
      if (closed || busy || !owner()) return;
      const token = owner(), ticket = ++revision;
      busy = true; checkbox.disabled = true; refresh.disabled = true;
      status.className = "status-line"; status.textContent = options.method ? "正在保存提醒偏好…" : "正在读取到期提醒…";
      const valid = () => !closed && modal.isConnected !== false && ticket === revision && token === owner();
      try {
        const data = await accountToolRequest(workerUrl, "/account/expiry-reminders", options);
        if (!valid()) return;
        enabled = data.preferences?.enabled === true; loaded = true; checkbox.checked = enabled;
        renderExpiryReminderDetails(modal, "accountReminder", data);
        status.className = "status-line ok";
        status.textContent = options.method ? (enabled ? "到期提醒已开启。" : "到期提醒已关闭。") : "提醒状态已更新。";
      } catch (error) {
        if (valid()) { checkbox.checked = enabled; status.className = "status-line error"; status.textContent = error.message; }
      } finally {
        if (valid()) { busy = false; checkbox.disabled = !loaded; refresh.disabled = false; }
      }
    }
    checkbox.addEventListener("change", () => {
      if (busy || !loaded) return;
      request({ method: "POST", body: JSON.stringify({ enabled: checkbox.checked }) });
    });
    refresh.addEventListener("click", () => request());
    panel.addEventListener("toggle", () => { if (panel.open && !loaded) request(); });
    function reset() {
      revision += 1; busy = false; loaded = false; enabled = false;
      checkbox.checked = false; checkbox.disabled = true; refresh.disabled = false; status.textContent = "";
      renderExpiryReminderDetails(modal, "accountReminder", null);
    }
    function onAuthChange() {
      if (owner() === currentOwner) return;
      currentOwner = owner(); reset();
      if (panel.open && currentOwner) request();
    }
    document.addEventListener("portal-auth-change", onAuthChange);
    if (panel.open) request();
    return { close() { closed = true; reset(); document.removeEventListener("portal-auth-change", onAuthChange); } };
  }

  function initAccountCreditControls(workerUrl, modal) {
    const summary = modal.querySelector("#accountAiCreditsSummary");
    const refresh = modal.querySelector("#accountAiCreditsRefresh");
    const status = modal.querySelector("#accountAiCreditsStatus");
    if (!summary || !refresh || !status) return { close() {} };
    let closed = false, busy = false, revision = 0;
    const owner = () => String(loadAuthSession()?.token || "");
    let currentOwner = owner();
    async function load() {
      if (closed || busy || !owner()) return;
      const token = owner(), ticket = ++revision;
      busy = true; refresh.disabled = true; status.textContent = "正在读取 AI 研究次数…"; status.className = "status-line";
      const valid = () => !closed && modal.isConnected !== false && ticket === revision && owner() === token;
      try {
        const data = await accountToolRequest(workerUrl, "/account/ai-research-credits");
        if (!valid()) return;
        const usage = data.usage || {};
        const included = usage.tier === "admin" || usage.limit === null || usage.unlimited === true
          ? "当前账号不限次使用。"
          : Number.isFinite(usage.remaining) ? `${["daily", "day"].includes(usage.period) ? "今日" : "原有"}额度剩余 ${Math.max(0, usage.remaining)} 次。` : "原有额度以研究请求返回为准。";
        summary.textContent = `${included} 额外可用 ${Math.max(0, Number(data.credits?.balance || 0))} 次；原有额度用完后自动使用额外次数。`;
        status.textContent = "次数已更新。"; status.className = "status-line ok";
      } catch (error) { if (valid()) { status.textContent = error.message; status.className = "status-line error"; } }
      finally { if (valid()) { busy = false; refresh.disabled = false; } }
    }
    function onAuthChange() {
      if (owner() === currentOwner) return;
      currentOwner = owner(); revision += 1; busy = false; summary.textContent = ""; status.textContent = ""; refresh.disabled = false;
      if (currentOwner) load();
    }
    refresh.addEventListener("click", load);
    document.addEventListener("portal-auth-change", onAuthChange);
    load();
    return { close() { closed = true; revision += 1; summary.textContent = ""; document.removeEventListener("portal-auth-change", onAuthChange); } };
  }

  function apiGrantLocalDate(value) {
    const date = new Date(value || Date.now() + 30 * 86400000);
    if (!Number.isFinite(date.getTime())) return "";
    return new Date(date.getTime() - date.getTimezoneOffset() * 60000).toISOString().slice(0, 16);
  }

  function initAdminResearchAccessControls(workerUrl, modal) {
    const byId = (id) => modal.querySelector(`#${id}`);
    const panel = byId("accountAdminResearchAccess");
    if (!panel) return { close() {} };
    const creditForm = byId("accountAdminAiCreditForm");
    const creditCount = byId("accountAdminAiCreditCount");
    const creditReason = byId("accountAdminAiCreditReason");
    const creditBalance = byId("accountAdminAiCreditBalance");
    const creditStatus = byId("accountAdminAiCreditStatus");
    const apiForm = byId("accountAdminApiGrantForm");
    const apiStatus = byId("accountAdminApiGrantStatus");
    const apiState = byId("accountAdminApiGrantState");
    const reminderStatus = byId("accountAdminReminderStatus");
    const mode = byId("accountAdminApiMode");
    const expiry = byId("accountAdminApiExpiry");
    const ids = byId("accountAdminApiReportIds");
    const revoke = byId("accountAdminApiGrantRevoke");
    const refresh = byId("accountAdminResearchRefresh");
    const scopes = [...apiForm.querySelectorAll('input[type="checkbox"]')];
    let closed = false, busy = false, revision = 0, selectedEmail = "";
    let creditLoaded = false, apiLoaded = false, grant = null, creditOperation = null, trigger = null;
    const initialOwner = String(loadAuthSession()?.token || "");
    const setStatus = (node, text, type = "") => { node.textContent = text; node.className = `status-line ${type}`; };
    function valid(ticket) {
      return !closed && modal.isConnected !== false && revision === ticket && isAdminASession() && initialOwner === String(loadAuthSession()?.token || "");
    }
    function controls() {
      creditForm.querySelectorAll("input, button").forEach((node) => { node.disabled = busy || !creditLoaded; });
      apiForm.querySelectorAll("input, select, textarea, button").forEach((node) => { node.disabled = busy || !apiLoaded; });
      revoke.disabled = busy || !apiLoaded || !grant?.enabled;
      refresh.disabled = busy;
      byId("accountAdminResearchClose").disabled = busy;
    }
    function showCredits(data) {
      creditBalance.textContent = `当前额外可用 ${Number(data.credits?.balance || 0)} 次 · 累计添加 ${Number(data.credits?.total_granted || 0)} 次 · 已使用 ${Number(data.credits?.total_consumed || 0)} 次。先用账号原有额度，再使用添加的次数。`;
      creditLoaded = true;
    }
    function showGrant(data) {
      grant = data.grant || {};
      apiLoaded = true;
      mode.value = grant.access_mode === "granted_corpus" ? "granted_corpus" : "membership";
      expiry.value = apiGrantLocalDate(grant.expires_at);
      ids.value = (grant.report_ids || []).join("\n");
      const allowed = Array.isArray(grant.scopes) ? grant.scopes : ["reports:read", "reports:download", "artifacts:read"];
      scopes.forEach((node) => { node.checked = allowed.includes(node.value); });
      updateReportScopeHint();
      apiState.textContent = grant.enabled
        ? `API 已开通 · ${apiAccessDate(grant.expires_at)} 到期。${Date.parse(grant.expires_at) <= Date.now() ? "当前已过期。" : ""}`
        : "API 未开通。";
    }
    async function load(email) {
      if (closed || busy || !isAdminASession()) return;
      selectedEmail = email; creditLoaded = false; apiLoaded = false; grant = null;
      creditBalance.textContent = ""; apiState.textContent = "";
      renderExpiryReminderDetails(modal, "accountAdminReminder", null);
      byId("accountAdminResearchUser").textContent = `当前用户：${email}`;
      panel.hidden = false; busy = true; controls();
      const ticket = ++revision;
      setStatus(creditStatus, "正在读取 AI 研究次数…"); setStatus(apiStatus, "正在读取 API 权限…");
      setStatus(reminderStatus, "正在读取提醒计划与预览…");
      await Promise.allSettled([
        accountToolRequest(workerUrl, `/account-admin/ai-research-credits?email=${encodeURIComponent(email)}`).then((data) => {
          if (valid(ticket)) { showCredits(data); setStatus(creditStatus, "次数已更新。", "ok"); }
        }).catch((error) => { if (valid(ticket)) setStatus(creditStatus, error.message, "error"); }),
        accountToolRequest(workerUrl, `/admin/content-api/grant?email=${encodeURIComponent(email)}`).then((data) => {
          if (valid(ticket)) { showGrant(data); setStatus(apiStatus, "API 权限已更新。", "ok"); }
        }).catch((error) => { if (valid(ticket)) setStatus(apiStatus, error.message, "error"); }),
        accountToolRequest(workerUrl, `/account-admin/expiry-reminders?email=${encodeURIComponent(email)}`).then((data) => {
          if (valid(ticket)) { renderExpiryReminderDetails(modal, "accountAdminReminder", data); setStatus(reminderStatus, "已读取计划与内容预览，未发送邮件。", "ok"); }
        }).catch((error) => { if (valid(ticket)) setStatus(reminderStatus, error.message, "error"); }),
      ]);
      if (valid(ticket)) { busy = false; controls(); }
    }
    async function mutate(path, payload, node, pending, done) {
      if (closed || busy || !selectedEmail || !isAdminASession()) return;
      busy = true; controls(); const ticket = ++revision; setStatus(node, pending);
      try {
        const data = await accountToolRequest(workerUrl, path, { method: "POST", body: JSON.stringify(payload) });
        if (valid(ticket)) done(data);
      } catch (error) { if (valid(ticket)) setStatus(node, error.message, "error"); }
      finally { if (valid(ticket)) { busy = false; controls(); } }
    }
    function open(button) {
      if (closed || !button || !isAdminASession()) return;
      if (busy) { setStatus(apiStatus, "请等待当前读取或保存完成，再选择其他用户。"); return; }
      if (selectedEmail !== button.dataset.email) creditOperation = null;
      trigger = button;
      load(button.dataset.email);
      byId("accountAdminResearchTitle")?.focus?.({ preventScroll: true });
      panel.scrollIntoView({ block: "nearest", behavior: "smooth" });
    }
    modal.addEventListener("click", (event) => open(event.target.closest(".account-admin-research-user")));
    refresh.addEventListener("click", () => load(selectedEmail));
    byId("accountAdminResearchClose").addEventListener("click", () => {
      if (!busy) { panel.hidden = true; if (trigger?.isConnected !== false) trigger?.focus?.({ preventScroll: true }); }
    });
    function updateReportScopeHint() {
      byId("accountAdminApiReportIdsHint").textContent = mode.value === "granted_corpus"
        ? "留空表示单独授权全部报告；仅影响 API，不修改网站会员与下载权限。"
        : "留空沿用网站现有权限；填写 ID 会进一步缩小 API 范围。";
    }
    mode.addEventListener("change", updateReportScopeHint);
    creditForm.addEventListener("submit", (event) => {
      event.preventDefault();
      if (busy || !creditLoaded) return;
      const amount = Number(creditCount.value), reason = creditReason.value.trim();
      if (!Number.isInteger(amount) || amount < 1 || amount > 10000 || !reason || reason.length > 240) {
        setStatus(creditStatus, "请填写 1–10000 的整数次数和不超过 240 字的说明。", "error"); return;
      }
      const signature = JSON.stringify({ email: selectedEmail, amount, reason });
      if (!creditOperation || creditOperation.signature !== signature) creditOperation = { signature, id: window.crypto.randomUUID() };
      mutate("/account-admin/ai-research-credits", { email: selectedEmail, amount, reason, operation_id: creditOperation.id }, creditStatus, "正在添加 AI 研究次数…", (data) => {
        showCredits(data); creditOperation = null;
        setStatus(creditStatus, data.deduplicated ? "这笔添加已处理，当前余额已核对，没有重复添加。" : `已为当前用户添加 ${amount} 次 AI 研究。`, "ok");
      });
    });
    apiForm.addEventListener("submit", (event) => {
      event.preventDefault();
      if (busy || !apiLoaded) return;
      const timestamp = Date.parse(expiry.value);
      const reportIds = [...new Set(ids.value.split(/[\s,，]+/u).filter(Boolean))];
      const selectedScopes = scopes.filter((node) => node.checked).map((node) => node.value);
      if (!Number.isFinite(timestamp) || timestamp <= Date.now() || timestamp > Date.now() + 366 * 86400000) {
        setStatus(apiStatus, "请选择未来 366 天内的到期时间。", "error"); return;
      }
      if (!selectedScopes.length || reportIds.length > 500 || reportIds.some((id) => !/^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$/u.test(id))) {
        setStatus(apiStatus, "至少选择一项内容权限；报告 ID 最多 500 个，仅含字母、数字、短横线和下划线。", "error"); return;
      }
      mutate("/admin/content-api/grant", { ...grant, email: selectedEmail, enabled: true, access_mode: mode.value,
        report_ids: reportIds, scopes: selectedScopes, expires_at: new Date(timestamp).toISOString() }, apiStatus, "正在保存 API 权限…", (data) => {
        showGrant(data); setStatus(apiStatus, "API 权限已保存。用户可在账号面板自行生成密钥。", "ok");
      });
    });
    revoke.addEventListener("click", () => {
      if (!apiLoaded || !grant?.enabled) return;
      mutate("/admin/content-api/grant", { ...grant, email: selectedEmail, enabled: false }, apiStatus, "正在撤销 API 权限及旧密钥…", (data) => {
        showGrant(data); setStatus(apiStatus, "API 权限及旧密钥已撤销；再次开通后需生成新密钥。", "ok");
      });
    });
    function onAuthChange() {
      if (initialOwner !== String(loadAuthSession()?.token || "") || !isAdminASession()) {
        closed = true; revision += 1; panel.hidden = true; creditOperation = null;
      }
    }
    document.addEventListener("portal-auth-change", onAuthChange);
    return { open, close() { closed = true; revision += 1; creditOperation = null; document.removeEventListener("portal-auth-change", onAuthChange); } };
  }

    return { initAccountApiControls, initAccountReminderControls, initAccountCreditControls, initAdminResearchAccessControls };
  };
})();
