// A durable request receipt and conditional R2 write make repeated clicks safe
// across Worker isolates. Never retry a dispatch POST: a timeout can mean GitHub
// accepted it, so subsequent requests reconcile through the read-only run list.
export const REPORT_REFRESH_STATE_KEY = "_account/admin/report-refresh.json";
export const REPORT_REFRESH_EVENT = "portal-dropbox-report-refresh";
const WORKFLOW = "neutral-edge-cutover.yml";
const RECEIPT_COOLDOWN_MS = 15 * 60 * 1000;
const FAILURE_COOLDOWN_MS = 60 * 1000;
const ACTIVE = new Set(["queued", "pending", "in_progress", "waiting", "requested"]);

function value(input) { return String(input || "").trim(); }
function isToken(input) { return value(input) && value(input) !== "unconfigured"; }
function timestamp(input) { return Date.parse(value(input)) || 0; }

function publicRun(run, repo) {
  if (!run || !Number.isSafeInteger(Number(run.id)) || Number(run.id) <= 0) return null;
  return {
    id: Number(run.id),
    status: value(run.status),
    conclusion: value(run.conclusion),
    // Construct the URL rather than trusting an upstream response URL.
    url: `https://github.com/${repo}/actions/runs/${Number(run.id)}`,
    created_at: value(run.created_at),
    updated_at: value(run.updated_at),
  };
}

function stateForRun(run, repo, receipt, configured) {
  const visible = publicRun(run, repo);
  const common = { requested_at: value(receipt && receipt.requested_at), run: visible, can_refresh: configured && !ACTIVE.has(run.status) };
  if (run.status === "in_progress") return { ...common, state: "in_progress", message: "正在从 Dropbox 刷新 reports，完成校验后会自动更新网站。" };
  if (ACTIVE.has(run.status)) return { ...common, state: "pending", message: "已有 reports 刷新任务排队中，会在当前发布完成后执行。" };
  if (run.conclusion === "success") return { ...common, state: "completed", message: "最近一次 reports 刷新已完成。" };
  return { ...common, state: "failed", message: "最近一次 reports 刷新未完成，可以重新发起。" };
}

function reportStatusCore(runs, receipt, repo, configured, nowMs) {
  const active = runs.find((run) => run.status === "in_progress") || runs.find((run) => ACTIVE.has(run.status));
  if (active) return stateForRun(active, repo, receipt, configured);
  const requested = timestamp(receipt && receipt.requested_at);
  const observed = new Set(Array.isArray(receipt && receipt.observed_run_ids) ? receipt.observed_run_ids : []);
  const correlated = requested && runs.find((run) => run.event === "repository_dispatch" && !observed.has(run.id) && timestamp(run.created_at) >= requested - 5000);
  if (correlated) return stateForRun(correlated, repo, receipt, configured);
  if (receipt && requested) {
    const age = nowMs - requested;
    if (["dispatching", "accepted", "unknown"].includes(receipt.state) && age < RECEIPT_COOLDOWN_MS) {
      return {
        state: receipt.state === "unknown" ? "unknown" : "requested",
        message: receipt.state === "unknown"
          ? "刷新请求的接收结果正在核验，请稍后查看状态，暂时无需重复点击。"
          : "已提交 reports 刷新请求，正在等待任务进入队列。",
        requested_at: receipt.requested_at, run: null, can_refresh: false,
      };
    }
    if (receipt.state === "failed" && age < FAILURE_COOLDOWN_MS) {
      return { state: "failed", message: "刷新请求暂未提交成功，请稍后重试。", requested_at: receipt.requested_at, run: null, can_refresh: false };
    }
    if (["dispatching", "accepted", "unknown"].includes(receipt.state)) {
      return { state: "unknown", message: "尚未找到对应的刷新任务，可以重新发起并继续核验。", requested_at: receipt.requested_at, run: null, can_refresh: configured };
    }
  }
  // GitHub replaces the single pending automatic run when newer upstream
  // completions arrive. Those superseded queue entries are not refresh errors.
  const latest = runs.find((run) => !(run.event === "workflow_run" && run.conclusion === "cancelled")) || runs[0];
  if (latest) return stateForRun(latest, repo, receipt, configured);
  return { state: configured ? "idle" : "unavailable", message: configured ? "可手工从 Dropbox 刷新 reports。" : "手工刷新暂未配置，请联系管理员。", requested_at: value(receipt && receipt.requested_at), run: null, can_refresh: configured };
}

function reportStatus(runs, receipt, repo, configured, nowMs) {
  const successful = runs.find((run) => run.status === "completed" && run.conclusion === "success");
  return {
    ...reportStatusCore(runs, receipt, repo, configured, nowMs),
    last_success_at: value(successful && successful.updated_at),
  };
}

export async function handleReportRefresh(request, env, dependencies) {
  const { authorize, respond, repository, fetchWithTimeout } = dependencies;
  try {
    await authorize(request, env);
  } catch (_error) {
    return respond(request, env, 403, { detail: "只有管理员可以刷新 reports。" });
  }
  const repo = repository(env);
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repo)) {
    return respond(request, env, 503, { state: "unavailable", message: "手工刷新暂未配置。", requested_at: "", run: null, can_refresh: false });
  }
  const dispatchToken = value(env.GH_DISPATCH_TOKEN);
  const readToken = isToken(dispatchToken) ? dispatchToken : value(env.GH_READ_TOKEN || env.GITHUB_TOKEN || env.GH_TOKEN);
  const configured = Boolean(isToken(dispatchToken));
  if (!isToken(readToken) || !env.REPORT_BUCKET) {
    return respond(request, env, 503, { state: "unavailable", message: "手工刷新暂未配置。", requested_at: "", run: null, can_refresh: false });
  }
  const headers = (token) => ({
    Authorization: `Bearer ${token}`, Accept: "application/vnd.github+json",
    "Content-Type": "application/json", "User-Agent": "portal-suite-worker", "X-GitHub-Api-Version": "2022-11-28",
  });
  const baseUrl = `https://api.github.com/repos/${repo}`;
  let current;
  let runs;
  try {
    // A long-running refresh can be older than thirty recent upstream-triggered
    // runs. Query every active status independently; a capped recent history
    // must never be used as proof that no refresh is running or queued.
    const queries = ["", ...ACTIVE];
    const [object, inventories] = await Promise.all([
      env.REPORT_BUCKET.get(REPORT_REFRESH_STATE_KEY),
      Promise.all(queries.map(async (status) => {
        const query = status ? `branch=main&per_page=1&status=${status}` : "branch=main&per_page=30";
        const response = await fetchWithTimeout(`${baseUrl}/actions/workflows/${WORKFLOW}/runs?${query}`, { headers: headers(readToken) }, 5500);
        if (!response.ok) throw new Error("Run status unavailable");
        const payload = await response.json();
        if (!Array.isArray(payload.workflow_runs)) throw new Error("Invalid run status");
        return payload.workflow_runs.filter((run) => run && run.head_branch === "main" && (!status || run.status === status));
      })),
    ]);
    // Status-specific reads override potentially older history entries.
    runs = [...new Map(inventories.flat().map((run) => [run.id, run])).values()]
      .sort((a, b) => timestamp(b.created_at) - timestamp(a.created_at));
    current = object ? { object, receipt: JSON.parse(await object.text()) } : null;
  } catch (_error) {
    // A failed read must never be interpreted as no active refresh.
    return respond(request, env, 503, { state: "unavailable", message: "暂时无法核验刷新状态，请稍后重试。", requested_at: "", run: null, can_refresh: false });
  }
  const receipt = current && current.receipt;
  const nowMs = Date.now();
  const status = reportStatus(runs, receipt, repo, configured, nowMs);
  if (request.method === "GET" || !status.can_refresh) return respond(request, env, 200, status);

  const next = {
    schema_version: 1, request_id: crypto.randomUUID(), requested_at: new Date(nowMs).toISOString(),
    state: "dispatching", observed_run_ids: runs.map((run) => run.id),
  };
  let lease;
  try {
    // R2 conditional writes serialize clicks across concurrent Worker isolates.
    lease = await env.REPORT_BUCKET.put(REPORT_REFRESH_STATE_KEY, JSON.stringify(next), {
      onlyIf: current ? { etagMatches: value(current.object.etag) } : { etagDoesNotMatch: "*" },
      httpMetadata: { contentType: "application/json; charset=utf-8", cacheControl: "private, no-store" },
    });
    if (!lease) return respond(request, env, 202, { state: "requested", message: "刷新请求正在提交，请稍后查看状态。", requested_at: next.requested_at, run: null, can_refresh: false });
  } catch (_error) {
    return respond(request, env, 503, { state: "unavailable", message: "刷新请求暂时无法保存，请稍后重试。", requested_at: "", run: null, can_refresh: false });
  }

  let response;
  try {
    response = await fetchWithTimeout(`${baseUrl}/dispatches`, {
      method: "POST", headers: headers(dispatchToken),
      body: JSON.stringify({ event_type: REPORT_REFRESH_EVENT, client_payload: { request_id: next.request_id, requested_at: next.requested_at } }),
    }, 5500);
  } catch (_error) {
    // Acceptance is ambiguous. Keep the durable receipt and reconcile only with
    // GETs; never send a second POST automatically.
    next.state = "unknown";
  }
  if (response) next.state = response.ok ? "accepted" : (response.status >= 500 ? "unknown" : "failed");
  try {
    await env.REPORT_BUCKET.put(REPORT_REFRESH_STATE_KEY, JSON.stringify(next), {
      onlyIf: { etagMatches: value(lease.etag) },
      httpMetadata: { contentType: "application/json; charset=utf-8", cacheControl: "private, no-store" },
    });
  } catch (_error) {
    // The initial receipt remains sufficient to suppress duplicate dispatches.
    if (next.state === "accepted") next.state = "unknown";
  }
  const result = reportStatus(runs, next, repo, configured, nowMs);
  return respond(request, env, next.state === "failed" ? 503 : 202, result);
}
