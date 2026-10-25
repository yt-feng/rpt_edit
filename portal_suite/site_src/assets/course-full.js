(() => {
  "use strict";
  if (window.PortalCourseFull) return;
  const mounts = new WeakMap();
  function track(action, status = "", extra = {}) {
    try { window.PortalSuiteAnalytics?.track("journey_interaction", { measurement_version: "journey-v1", placement: "course_full", action, status, ...extra }); } catch (_) { /* Telemetry is best effort. */ }
  }

  function session() {
    try {
      const current = JSON.parse(window.localStorage.getItem("portal_auth_session") || "null");
      return current?.user?.id && typeof current.token === "string" && current.token.trim() ? current : null;
    } catch (_error) { return null; }
  }
  function dateLabel(value) {
    const date = new Date(value || "");
    return Number.isFinite(date.getTime()) ? new Intl.DateTimeFormat("zh-CN", {
      timeZone: "Asia/Shanghai", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hour12: false,
    }).format(date) : "";
  }
  function replyEmail(value) {
    const email = String(value || "").trim();
    return /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(email) && !/@users(?:\.portal)?\.example\.invalid$/i.test(email) ? email : "";
  }
  function accountEmail(current) {
    return current?.user?.email_is_generated ? "" : replyEmail(current?.user?.email);
  }
  function node(tag, text, className = "") {
    const element = document.createElement(tag);
    if (text !== undefined) element.textContent = String(text);
    if (className) element.className = className;
    return element;
  }
  function mount(root = document.getElementById("courseFullApp")) {
    if (!root) return null;
    if (mounts.has(root)) return mounts.get(root);
    const byId = (id) => root.querySelector(`#courseFull${id}`);
    const gate = byId("GateTitle").parentElement, title = byId("GateTitle"), message = byId("GateMessage"), dates = byId("Dates");
    const login = byId("Login"), retry = byId("Retry"), verify = byId("Verify"), directory = byId("Directory");
    const filters = byId("Filters"), search = byId("Search"), folder = byId("Folder"), fileType = byId("Type");
    const items = byId("Items"), status = byId("Status"), requestStatus = byId("RequestStatus"), updated = byId("Updated");
    const reply = byId("Reply"), email = byId("ReplyEmail");
    const pagination = byId("Pagination"), previous = byId("Previous"), next = byId("Next"), pageLabel = byId("PageLabel");
    const controllers = new Set(), pendingRequests = new Set(), submitted = new Map(), requestButtons = new Map();
    let revision = 0, listRevision = 0, allowed = false, page = 1, hasMore = false, identity = "", destroyed = false;
    function fingerprint(current) { return current ? `${current.user.id}:${current.token}` : ""; }
    function current(rev) { return !destroyed && rev === revision && fingerprint(session()) === identity; }
    function setStatus(target, text, state = "") { target.textContent = text; target.dataset.state = state; }
    function clearDirectory() {
      allowed = false; directory.hidden = true; items.replaceChildren(); requestButtons.clear(); pagination.hidden = true;
      status.textContent = ""; requestStatus.textContent = ""; updated.textContent = "";
    }
    function lock(heading, text, showLogin = false, showVerify = false) {
      clearDirectory(); title.textContent = heading; message.textContent = text;
      gate.dataset.state = "locked"; login.hidden = !showLogin; verify.hidden = !showVerify;
    }
    function setDates(data) {
      const since = dateLabel(data.since), eligible = dateLabel(data.eligible_at);
      dates.textContent = [since && `连续会员记录起点：${since}（北京时间）`, eligible && `满足两个月日期：${eligible}（北京时间）`].filter(Boolean).join("\n");
      dates.hidden = !dates.textContent;
    }
    async function api(path, options = {}) {
      const active = session();
      if (!active) throw Object.assign(new Error("请先登录账号。"), { status: 401 });
      const controller = new AbortController(); controllers.add(controller);
      const timer = window.setTimeout(() => controller.abort(), 20000);
      try {
        const response = await window.fetch(`/api/course/full/${path}`, {
          cache: "no-store", ...options,
          headers: { Authorization: `Bearer ${active.token}`, ...(options.body ? { "Content-Type": "application/json" } : {}) },
          signal: controller.signal,
        });
        const data = await response.json().catch(() => ({}));
        if (!response.ok) throw Object.assign(new Error(response.status === 503 ? "目录暂时不可用，请稍后重试。" : String(data.detail || "暂时无法完成请求，请重试。")), { status: response.status, data });
        return data;
      } finally { window.clearTimeout(timer); controllers.delete(controller); }
    }
    function denied(data = {}) {
      setDates(data);
      if (data.reason === "needs_history_verification") {
        lock("会员历史需要核验", "当前记录尚不足以确认连续会员已满两个自然月。如果你此前已连续开通会员，请联系我们核验历史记录。", false, true);
      } else if (data.reason === "tenure_incomplete") {
        lock("连续会员尚未满两个月", "在保持会员连续有效的情况下，到达下方日期后可重新核验并查看目录。", false, true);
      } else {
        lock("当前会员资格未满足", "此目录供当前有效、连续满两个自然月的会员使用。可在账号中查看会员状态，或联系我们核验。", false, true);
      }
    }
    function facets(select, values, allLabel) {
      const selected = select.value;
      const choices = [node("option", allLabel)]; choices[0].value = "";
      for (const row of Array.isArray(values) ? values : []) {
        if (!row || typeof row.name !== "string" || !row.name) continue;
        const count = Number.isFinite(Number(row.count)) ? Math.max(0, Number(row.count)) : 0;
        const option = node("option", `${row.name} (${count})`); option.value = row.name; choices.push(option);
      }
      if (selected && !choices.some((option) => option.value === selected)) {
        const option = node("option", selected); option.value = selected; choices.push(option);
      }
      select.replaceChildren(...choices); select.value = selected;
    }
    async function requestItem(item, button) {
      if (!allowed || pendingRequests.has(item.id) || submitted.has(item.id)) return;
      const rev = revision;
      if (!current(rev)) { await refresh(); return; }
      const needsReply = !accountEmail(session()), suppliedEmail = replyEmail(email.value);
      if (needsReply && (!suppliedEmail || !email.reportValidity())) {
        setStatus(requestStatus, "请填写可接收回复的邮箱。", "error"); email.focus(); return;
      }
      track("request_submit", "pending");
      pendingRequests.add(item.id); button.disabled = true; button.textContent = "正在提交…";
      setStatus(requestStatus, "正在提交索取申请…");
      try {
        const data = await api("directory-request", { method: "POST", body: JSON.stringify({
          directory_item_id: item.id, page_path: window.location.pathname, honeypot: "",
          ...(needsReply ? { requester_email: suppliedEmail } : {}),
        }) });
        if (!current(rev)) return;
        if (data.ok !== true) throw new Error("申请暂未确认，请稍后重试。");
        track("request_result", data.deduplicated ? "deduplicated" : "success", { deduplicated: data.deduplicated === true, acknowledgement_status: data.confirmation_email_sent === true ? "provider_accepted" : "unknown" });
        const label = data.deduplicated ? "申请已记录" : "申请已提交";
        submitted.set(item.id, label); button.textContent = label;
        const visibleButton = requestButtons.get(item.id);
        if (visibleButton) { visibleButton.textContent = label; visibleButton.disabled = true; }
        setStatus(requestStatus, "申请已收到，我们会通过邮箱与你联系。 / Request received. We will contact you by email.", "success");
      } catch (error) {
        if (!current(rev)) return;
        track("request_result", "error", { error: error.name === "AbortError" ? "timeout" : error.status === 401 ? "auth" : error.status === 403 ? "forbidden" : "unavailable" });
        if (error.status === 401 || error.status === 403) { await refresh(); return; }
        button.disabled = false; button.textContent = "重新申请";
        const visibleButton = requestButtons.get(item.id);
        if (visibleButton) { visibleButton.textContent = "重新申请"; visibleButton.disabled = false; }
        setStatus(requestStatus, error.name === "AbortError" ? "提交暂未确认，请稍后重试。" : error.message, "error");
      } finally { if (rev === revision) pendingRequests.delete(item.id); }
    }
    function renderItems(rows) {
      const rendered = []; requestButtons.clear();
      for (const item of Array.isArray(rows) ? rows : []) {
        if (!item || typeof item.id !== "string" || !item.id || typeof item.name !== "string") continue;
        const row = node("li", undefined, "course-full-file"), info = node("div");
        info.append(node("h3", item.name));
        const path = Array.isArray(item.folders) ? item.folders.filter((name) => typeof name === "string").join(" / ") : "";
        if (path) info.append(node("p", path, "course-full-folders"));
        const metadata = [item.extension, item.size_label, item.date].filter((value) => typeof value === "string" && value);
        if (metadata.length) info.append(node("p", metadata.join(" · "), "course-full-meta"));
        const button = node("button", submitted.get(item.id) || "申请索取", "secondary");
        button.type = "button"; button.disabled = submitted.has(item.id) || pendingRequests.has(item.id);
        button.setAttribute("aria-label", `申请索取：${item.name}`);
        button.addEventListener("click", () => requestItem(item, button));
        requestButtons.set(item.id, button);
        row.append(info, button); rendered.push(row);
      }
      items.replaceChildren(...rendered);
      return rendered.length;
    }
    async function loadDirectory(targetPage = 1) {
      const rev = revision, expectedList = ++listRevision;
      if (!allowed || !current(rev)) return;
      previous.disabled = true; next.disabled = true; items.replaceChildren(); pagination.hidden = true;
      setStatus(status, "正在加载目录…");
      track("directory_start", "pending");
      const params = new URLSearchParams({ q: search.value.trim(), folder: folder.value, file_type: fileType.value, page: String(targetPage), page_size: "30" });
      try {
        const data = await api(`directory?${params.toString()}`);
        if (!current(rev) || expectedList !== listRevision) return;
        if (!Array.isArray(data.items) || !Number.isInteger(data.total) || data.total < 0) throw new Error("目录暂时不可用，请稍后重试。");
        page = Number.isInteger(data.page) && data.page > 0 ? data.page : targetPage;
        hasMore = data.has_more === true;
        facets(folder, data.facets?.folders, "全部目录"); facets(fileType, data.facets?.file_types, "全部类型");
        const count = renderItems(data.items);
        track("directory_result", "success", { result_count: count });
        setStatus(status, count ? `找到 ${data.total} 项，当前显示 ${count} 项。` : "没有匹配的文件，请更换关键词或筛选条件。");
        const generated = dateLabel(data.generated_at); updated.textContent = generated ? `目录更新时间：${generated}（北京时间）` : "";
        pageLabel.textContent = `第 ${page} 页`;
        previous.disabled = page <= 1; next.disabled = !hasMore; pagination.hidden = page <= 1 && !hasMore;
      } catch (error) {
        if (!current(rev) || expectedList !== listRevision) return;
        track("directory_result", "error", { error: error.name === "AbortError" ? "timeout" : error.status === 401 ? "auth" : error.status === 403 ? "forbidden" : "unavailable" });
        if (error.status === 401) { lock("请重新登录", "登录状态已失效，请登录后重新核验。", true); return; }
        if (error.status === 403) { denied(error.data?.access || error.data); return; }
        setStatus(status, error.name === "AbortError" ? "目录加载超时，请点击搜索重试。" : error.message, "error");
      }
    }
    async function refresh() {
      if (destroyed) return;
      revision += 1; listRevision += 1;
      for (const controller of controllers) controller.abort();
      controllers.clear(); pendingRequests.clear(); submitted.clear();
      retry.disabled = false;
      clearDirectory(); dates.hidden = true; dates.textContent = "";
      email.value = ""; reply.hidden = true;
      search.value = ""; folder.replaceChildren(node("option", "全部目录")); folder.value = "";
      fileType.replaceChildren(node("option", "全部类型")); fileType.value = "";
      identity = fingerprint(session());
      const rev = revision;
      track("access_start", identity ? "pending" : "guest");
      if (!identity) { lock("登录后核验会员资格", "当前有效、连续满两个自然月的会员可查看原始目录。", true); return; }
      lock("正在核验会员资格", "请稍候。"); retry.disabled = true;
      try {
        const data = await api("access");
        if (!current(rev)) return;
        track("access_result", data.allowed === true ? "success" : "denied", { access_state: data.allowed === true ? "allowed" : data.reason });
        if (data.allowed !== true) { denied(data); return; }
        setDates(data); allowed = true; gate.dataset.state = "allowed";
        title.textContent = "会员资格已通过核验"; message.textContent = "可按原始目录查找资料，并逐项提交索取申请。";
        login.hidden = true; verify.hidden = true; directory.hidden = false;
        reply.hidden = Boolean(accountEmail(session()));
        await loadDirectory(1);
      } catch (error) {
        if (!current(rev)) return;
        track("access_result", "error", { error: error.name === "AbortError" ? "timeout" : error.status === 401 ? "auth" : "unavailable" });
        if (error.status === 401) lock("请重新登录", "登录状态已失效，请登录后重新核验。", true);
        else lock("暂时无法核验会员资格", "请稍后点击重新核验。", false, true);
      } finally { if (current(rev)) retry.disabled = false; }
    }
    function openLogin() { track("login_click"); document.dispatchEvent(new CustomEvent("portal-open-auth", { detail: { mode: "login", placement: "course_full" } })); }
    function filter(event) { event.preventDefault(); loadDirectory(1); }
    function storage(event) { if (event.key === "portal_auth_session") refresh(); }
    function back() { if (page > 1) loadDirectory(page - 1); }
    function forward() { if (hasMore) loadDirectory(page + 1); }
    function verifyClick() { track("verify_click"); }
    verify.addEventListener("click", verifyClick);
    login.addEventListener("click", openLogin); retry.addEventListener("click", refresh);
    filters.addEventListener("submit", filter); folder.addEventListener("change", filter); fileType.addEventListener("change", filter);
    previous.addEventListener("click", back); next.addEventListener("click", forward);
    document.addEventListener("portal-auth-change", refresh); window.addEventListener("storage", storage);
    const instance = { refresh, destroy() {
      destroyed = true; revision += 1; for (const controller of controllers) controller.abort();
      clearDirectory(); dates.textContent = ""; dates.hidden = true;
      document.removeEventListener("portal-auth-change", refresh); window.removeEventListener("storage", storage);
      verify.removeEventListener("click", verifyClick);
      login.removeEventListener("click", openLogin); retry.removeEventListener("click", refresh);
      filters.removeEventListener("submit", filter); folder.removeEventListener("change", filter); fileType.removeEventListener("change", filter);
      previous.removeEventListener("click", back); next.removeEventListener("click", forward); mounts.delete(root);
    } };
    mounts.set(root, instance); refresh(); return instance;
  }
  window.PortalCourseFull = { mount };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", () => mount(), { once: true }); else mount();
})();
