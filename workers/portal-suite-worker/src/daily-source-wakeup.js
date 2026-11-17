// Cloudflare's existing half-hour clock checks the metadata dispatcher when
// GitHub's own schedule has been silent. The dispatcher owns batch deduplication.
export const DAILY_SOURCE_WAKEUP_STATE_KEY = "_account/ops/daily-source-wakeup.json";
const WORKFLOW = "daily-report-source-wakeup.yml";
const STALE_MS = 30 * 60 * 1000;
const LEASE_MS = 60 * 60 * 1000;
const ACTIVE = ["queued", "pending", "in_progress", "waiting", "requested"];
const EVENTS = ["schedule", "workflow_dispatch"];

function token(value) {
  const text = String(value || "").trim();
  return text === "unconfigured" ? "" : text;
}

export async function wakeDailyReportSource(env, { repository, fetchWithTimeout, now = Date.now }) {
  const nowMs = now();
  const beijingHour = new Date(nowMs + 8 * 60 * 60 * 1000).getUTCHours();
  if (beijingHour < 2) return { state: "before_daily_start" };
  const repo = repository(env);
  const dispatchToken = token(env.GH_DISPATCH_TOKEN);
  const readToken = [env.GH_READ_TOKEN, env.GITHUB_TOKEN, env.GH_TOKEN, dispatchToken].map(token).find(Boolean);
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repo) || !dispatchToken || !readToken || !env.REPORT_BUCKET) {
    return { state: "unconfigured" };
  }
  const base = `https://api.github.com/repos/${repo}/actions/workflows/${WORKFLOW}`;
  const headers = (credential) => ({
    Authorization: `Bearer ${credential}`, Accept: "application/vnd.github+json",
    "Content-Type": "application/json", "User-Agent": "portal-suite-worker", "X-GitHub-Api-Version": "2022-11-28",
  });
  async function readRuns(filter) {
    const url = `${base}/runs?branch=main&per_page=1&${filter}`;
    let response = await fetchWithTimeout(url, { headers: headers(readToken) }, 5500);
    if ([401, 403].includes(response.status) && readToken !== dispatchToken) {
      await response.body?.cancel().catch(() => {});
      response = await fetchWithTimeout(url, { headers: headers(dispatchToken) }, 5500);
    }
    if (!response.ok) throw new Error("run_inventory_unavailable");
    const payload = await response.json();
    const rows = payload.workflow_runs;
    if (!Number.isSafeInteger(payload.total_count) || payload.total_count < 0 || !Array.isArray(rows)
        || rows.length !== Math.min(1, payload.total_count)) throw new Error("run_inventory_invalid");
    const query = new URLSearchParams(filter);
    for (const run of rows) {
      if (!Number.isSafeInteger(run.id) || run.id <= 0 || run.head_branch !== "main"
          || run.path !== `.github/workflows/${WORKFLOW}` || run.head_repository?.full_name !== repo
          || !EVENTS.includes(run.event) || !Number.isFinite(Date.parse(run.created_at))
          || (query.has("status") && run.status !== query.get("status"))
          || (query.has("event") && run.event !== query.get("event"))) throw new Error("run_identity_invalid");
    }
    return rows;
  }

  let current;
  let receipt;
  let runs;
  try {
    [current, runs] = await Promise.all([
      env.REPORT_BUCKET.get(DAILY_SOURCE_WAKEUP_STATE_KEY),
      Promise.all([...EVENTS.map((event) => `event=${event}`), ...ACTIVE.map((status) => `status=${status}`)].map(readRuns)),
    ]);
    receipt = current ? JSON.parse(await current.text()) : null;
    if (receipt && (!Number.isFinite(Date.parse(receipt.requested_at)) || !current.etag)) throw new Error("receipt_invalid");
  } catch (_error) {
    return { state: "inspection_unavailable" };
  }
  const observed = runs.flat();
  const active = observed.find((run) => ACTIVE.includes(run.status));
  if (active) return { state: "wake_active", run_id: active.id };
  const latest = observed.sort((a, b) => Date.parse(b.created_at) - Date.parse(a.created_at))[0];
  if (latest && nowMs - Date.parse(latest.created_at) <= STALE_MS) return { state: "wake_recent", run_id: latest.id };
  const latestDispatch = runs[1][0];
  const confirmed = receipt && latestDispatch && latestDispatch.status === "completed"
    && latestDispatch.id > (receipt.previous_dispatch_run_id || 0)
    && (!receipt.run_id || receipt.run_id === latestDispatch.id)
    && Date.parse(latestDispatch.created_at) >= Math.floor(Date.parse(receipt.requested_at) / 1000) * 1000;
  // A lost POST acknowledgement remains leased for an hour. Every subsequent
  // clock tick reads GitHub first. A confirmed completed wake instead follows
  // the normal stale interval, including when its first readback was delayed.
  if (receipt && !confirmed && nowMs - Date.parse(receipt.requested_at) <= LEASE_MS) return { state: "dispatch_cooldown" };

  const next = { requested_at: new Date(nowMs).toISOString(), state: "dispatching",
    previous_dispatch_run_id: latestDispatch?.id || 0 };
  let lease;
  try {
    lease = await env.REPORT_BUCKET.put(DAILY_SOURCE_WAKEUP_STATE_KEY, JSON.stringify(next), {
      onlyIf: current ? { etagMatches: current.etag } : { etagDoesNotMatch: "*" },
      httpMetadata: { contentType: "application/json", cacheControl: "private, no-store" },
    });
    if (!lease) return { state: "dispatch_claimed" };
  } catch (_error) {
    return { state: "receipt_unavailable" };
  }
  try {
    const response = await fetchWithTimeout(`${base}/dispatches`, {
      method: "POST", headers: headers(dispatchToken), body: JSON.stringify({ ref: "main" }),
    }, 5500);
    next.state = response.ok ? "accepted" : (response.status >= 500 ? "unknown" : "rejected");
    await response.body?.cancel().catch(() => {});
  } catch (_error) {
    next.state = "unknown";
  }
  try {
    // A single read also reconciles a timeout after GitHub accepted the POST.
    const accepted = (await readRuns("event=workflow_dispatch"))[0];
    if (accepted && accepted.id > next.previous_dispatch_run_id
        && Date.parse(accepted.created_at) >= Math.floor(nowMs / 1000) * 1000) {
      next.state = "observed";
      next.run_id = accepted.id;
    }
  } catch (_error) {
    // Keep the lease when acceptance cannot yet be read back.
  }
  try {
    await env.REPORT_BUCKET.put(DAILY_SOURCE_WAKEUP_STATE_KEY, JSON.stringify(next), {
      onlyIf: { etagMatches: lease.etag },
      httpMetadata: { contentType: "application/json", cacheControl: "private, no-store" },
    });
  } catch (_error) {
    // The initial dispatching receipt still suppresses another POST.
  }
  return next;
}
