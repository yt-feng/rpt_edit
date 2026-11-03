const BUSY_STATES = new Set([
  "requested", "dispatching", "accepted", "queued", "pending", "waiting",
  "in_progress", "running", "unknown", "dispatch_unknown",
]);
const POLL_MS = 30000;
const MAX_POLLS = 240;

function refreshPresentation(data = {}) {
  const run = data.run || {};
  const state = String(data.state || "idle");
  const runStatus = String(run.status || "");
  const conclusion = String(run.conclusion || "");
  const completed = runStatus === "completed";
  const success = completed ? conclusion === "success" : state === "success";
  const failed = completed ? Boolean(conclusion && conclusion !== "success")
    : ["failed", "failure", "cancelled", "timed_out", "action_required"].includes(state);
  const busy = !success && !failed && (BUSY_STATES.has(state)
    && !(["unknown", "dispatch_unknown"].includes(state) && data.can_refresh === true)
    || ["queued", "pending", "waiting", "in_progress", "requested"].includes(runStatus));
  const label = success ? "Reports 刷新已完成。"
    : failed ? "本次刷新未完成，请检查任务状态后重试。"
    : runStatus === "in_progress" || ["running", "in_progress"].includes(state)
      ? "正在从 Dropbox 同步 Reports，完成后会更新网站。"
      : busy ? "刷新请求已受理，任务排队或执行中；完成后才会更新网站。"
        : "可从 Dropbox 手工同步最新 Reports。";
  return { success, failed, busy, label };
}

function formatBeijingTime(value) {
  if (!value) return "";
  const date = new Date(value);
  if (!Number.isFinite(date.getTime())) return "";
  return new Intl.DateTimeFormat("zh-CN", {
    timeZone: "Asia/Shanghai", year: "numeric", month: "2-digit", day: "2-digit",
    hour: "2-digit", minute: "2-digit", second: "2-digit", hour12: false,
  }).format(date);
}

export function mountAdminReportRefresh(options) {
  const { root, workerUrl, authHeaders, formatDateTime = formatBeijingTime,
    fetch: fetcher = globalThis.fetch, scheduler = globalThis } = options;
  let section = root.querySelector("#accountAdminReportRefreshSection");
  if (!section) {
    const anchor = root.querySelector("#accountAdminStatus");
    if (!anchor) return { close() {} };
    section = (root.ownerDocument || globalThis.document).createElement("section");
    section.id = "accountAdminReportRefreshSection";
    anchor.after(section);
  }
  section.className = "account-admin-section";
  section.innerHTML = `
    <div class="account-admin-heading"><strong>Reports 同步</strong></div>
    <p class="subtle">Dropbox 内容就绪后可手工同步。任务在后台运行，完成后更新网站。</p>
    <div class="account-access-actions">
      <button class="primary" id="accountAdminReportRefresh" type="button" disabled>从 Dropbox 刷新 Reports</button>
      <button class="secondary-button" id="accountAdminReportRefreshCheck" type="button">检查进度</button>
    </div>
    <div id="accountAdminReportRefreshStatus" class="status-line" aria-live="polite">正在检查 Reports 同步状态…</div>
    <p id="accountAdminReportRefreshUpdated" class="subtle"></p>`;
  const button = section.querySelector("#accountAdminReportRefresh");
  const check = section.querySelector("#accountAdminReportRefreshCheck");
  const status = section.querySelector("#accountAdminReportRefreshStatus");
  const updated = section.querySelector("#accountAdminReportRefreshUpdated");
  const doc = root.ownerDocument || globalThis.document;
  let closed = false, pending = false, timer = null, controller = null, polls = 0;
  let last = null, uncertainPost = false;

  function visible() { return !closed && root.isConnected !== false && !doc.hidden; }
  function stopTimer() {
    if (timer !== null) scheduler.clearTimeout(timer);
    timer = null;
  }
  function paint(data) {
    last = data;
    const view = refreshPresentation(data);
    const denied = data.can_refresh === false;
    button.disabled = pending || denied || view.busy || uncertainPost;
    button.textContent = view.busy || uncertainPost ? "Reports 同步中…" : "从 Dropbox 刷新 Reports";
    status.className = `status-line${view.success ? " ok" : view.failed ? " error" : ""}`;
    status.textContent = String(data.message || view.label);
    const successAt = formatDateTime(data.last_success_at || "");
    const catalogAt = data.catalog_updated_at_bjt || formatDateTime(data.catalog_updated_at || "");
    const checkedAt = formatDateTime(new Date().toISOString());
    updated.textContent = [
      catalogAt ? `网站报告更新时间（北京时间）：${catalogAt}` : "",
      successAt ? `最近刷新成功（北京时间）：${successAt}` : "",
      checkedAt ? `最近检查（北京时间）：${checkedAt}` : "",
    ].filter(Boolean).join(" · ");
    return view;
  }
  function schedule() {
    stopTimer();
    if (!visible() || !last || (!refreshPresentation(last).busy && !uncertainPost)) return;
    if (polls >= MAX_POLLS) {
      status.textContent += " 自动检查已暂停，可点击“检查进度”继续。";
      return;
    }
    timer = scheduler.setTimeout(() => { timer = null; polls += 1; readStatus(); }, POLL_MS);
  }
  async function request(method) {
    controller = new AbortController();
    const requestController = controller;
    const timeout = scheduler.setTimeout(() => requestController.abort(), 15000);
    try {
      const response = await fetcher(`${workerUrl}/account-admin/report-refresh`, {
        method, cache: "no-store", headers: { ...authHeaders(), ...(method === "POST" ? { "Content-Type": "application/json" } : {}) },
        ...(method === "POST" ? { body: "{}" } : {}), signal: requestController.signal,
      });
      const data = await response.json().catch(() => ({}));
      if (!response.ok) {
        const error = new Error(data.message || data.detail || "Reports 同步状态暂时无法读取，请稍后检查进度。");
        error.status = response.status;
        error.data = data;
        throw error;
      }
      return data;
    } finally {
      scheduler.clearTimeout(timeout);
      if (controller === requestController) controller = null;
    }
  }
  async function readStatus() {
    if (pending || !visible()) return;
    pending = true; check.disabled = true; button.disabled = true;
    try {
      const data = await request("GET");
      if (closed) return;
      // A timed-out POST may still have been accepted. Only an observed request
      // or task resolves that uncertainty; a transient empty read does not.
      if (data.requested_at || data.run || data.state && data.state !== "idle") uncertainPost = false;
      paint(data);
    } catch (error) {
      if (closed) return;
      if (error.status === 401 || error.status === 403) {
        section.hidden = true; closed = true; stopTimer();
      } else if (error.data && (error.data.state || error.data.run)) {
        paint(error.data);
      } else {
        status.className = "status-line";
        status.textContent = "暂时无法读取同步进度。请点击“检查进度”；已提交的任务会继续运行。";
      }
    } finally {
      pending = false;
      if (!closed) {
        check.disabled = false;
        button.disabled = uncertainPost || !last || last.can_refresh === false || refreshPresentation(last).busy;
        schedule();
      }
    }
  }
  async function startRefresh() {
    if (pending || button.disabled || !visible()) return;
    stopTimer(); pending = true; button.disabled = true; check.disabled = true;
    status.className = "status-line";
    status.textContent = "正在提交 Dropbox Reports 刷新请求…";
    try {
      const data = await request("POST");
      if (closed) return;
      uncertainPost = false; polls = 0; paint(data);
    } catch (error) {
      if (closed) return;
      if (error.status === 401 || error.status === 403) {
        section.hidden = true; closed = true;
      } else if (error.data && (error.data.state || error.data.run)) {
        paint(error.data);
      } else {
        // Never repeat a POST on a transport failure: GitHub may have accepted it.
        uncertainPost = true;
        status.className = "status-line";
        status.textContent = "请求结果正在确认，请点击“检查进度”。系统不会重复提交刷新。";
      }
    } finally {
      pending = false;
      if (!closed) {
        check.disabled = false;
        button.disabled = uncertainPost || !last || last.can_refresh === false || refreshPresentation(last).busy;
        schedule();
      }
    }
  }
  function onVisibility() {
    stopTimer();
    if (visible()) readStatus();
  }
  function onCheck() { polls = 0; stopTimer(); readStatus(); }
  button.addEventListener("click", startRefresh);
  check.addEventListener("click", onCheck);
  doc.addEventListener("visibilitychange", onVisibility);
  button.disabled = true;
  readStatus();
  return {
    close() {
      closed = true; stopTimer(); controller?.abort();
      button.removeEventListener("click", startRefresh);
      check.removeEventListener("click", onCheck);
      doc.removeEventListener("visibilitychange", onVisibility);
    },
  };
}
