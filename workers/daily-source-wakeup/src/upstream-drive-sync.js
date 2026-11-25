const WORKFLOW = "sync.yml";
const ACTIVE = new Set(["queued", "pending", "in_progress", "waiting", "requested"]);
const REQUEST_STATES = new Set(["dispatching", "accepted", "unknown", "rejected"]);
const DAY_MS = 24 * 60 * 60 * 1000;
const RETRY_DELAY_MS = 30 * 60 * 1000;
const MAX_ATTEMPTS = 2;
export const UPSTREAM_SYNC_RECEIPT_KEY = "_account/ops/drive-source-clock-dispatch.json";
export const UPSTREAM_SYNC_CHECK_KEY = "_account/ops/drive-source-clock-check.json";

function syncWindow(now) {
  const beijing = new Date(now + 8 * 60 * 60 * 1000);
  const today = beijing.toISOString().slice(0, 10);
  if (now >= Date.parse(`${today}T23:43:00+08:00`)) return null;
  const previousDay = new Date(beijing.getTime() - DAY_MS).toISOString().slice(0, 10);
  const due = Date.parse(`${previousDay}T23:43:00+08:00`);
  return { day: previousDay.slice(2).replaceAll("-", ""), due };
}

function validId(value) {
  return Number.isSafeInteger(value) && value > 0;
}

function validReceipt(row) {
  return row && typeof row.date_folder === "string" && /^[0-9]{6}$/.test(row.date_folder)
    && REQUEST_STATES.has(row.state) && Number.isFinite(Date.parse(row.requested_at))
    && Number.isInteger(row.attempts) && row.attempts >= 1 && row.attempts <= MAX_ATTEMPTS
    && (row.run_id === undefined || validId(row.run_id));
}

async function readRuns(fetchWithTimeout, base, headers, repo, due, sleep) {
  // Include runs from the preceding day so a still-active earlier sync also blocks a duplicate.
  const query = new URLSearchParams({
    branch: "main", per_page: "50", created: ">=" + new Date(due - DAY_MS).toISOString(),
  });
  for (let attempt = 0; attempt < 3; attempt += 1) {
    if (attempt) await sleep(attempt * 1000);
    let response;
    try {
      response = await fetchWithTimeout(`${base}/runs?${query}`, { headers, redirect: "manual" }, 5500);
    } catch {
      continue;
    }
    if (!response.ok) {
      await response.body?.cancel().catch(() => {});
      if (response.status === 429 || response.status >= 500) continue;
      throw new Error("upstream_inventory_unavailable");
    }
    const data = await response.json().catch(() => null);
    if (!Array.isArray(data?.workflow_runs) || !Number.isSafeInteger(data.total_count)
        || data.total_count !== data.workflow_runs.length || data.total_count > 50) continue;
    const rows = data.workflow_runs;
    const ids = new Set(rows.map((run) => run?.id));
    if (ids.size !== rows.length || !rows.every((run) => run && validId(run.id)
      && run.head_branch === "main" && run.path === `.github/workflows/${WORKFLOW}`
      && run.head_repository?.full_name === repo
      && ["schedule", "workflow_dispatch"].includes(run.event)
      && (ACTIVE.has(run.status) || run.status === "completed")
      && typeof run.display_title === "string" && Date.parse(run.created_at) >= due - DAY_MS)) {
      throw new Error("upstream_inventory_invalid");
    }
    return rows;
  }
  throw new Error("upstream_inventory_unavailable");
}

export async function reconcileUpstreamDriveSync(env, {
  fetchWithTimeout, now = Date.now, sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms)),
}) {
  const nowMs = now();
  const window = syncWindow(nowMs);
  if (!window) return { state: "outside_source_window" };
  const { day, due } = window;
  const baseState = { date_folder: day };
  const repo = String(env.REPORT_UPSTREAM_SYNC_REPO || "").trim();
  const credential = String(env.GH_DISPATCH_TOKEN || "").trim();
  const bucket = env.REPORT_BUCKET;
  if (!/^[A-Za-z0-9_.-]+\/[A-Za-z0-9_.-]+$/.test(repo) || !credential || credential === "unconfigured" || !bucket) {
    return { ...baseState, state: "unconfigured" };
  }
  const base = `https://api.github.com/repos/${repo}/actions/workflows/${WORKFLOW}`;
  const headers = {
    Authorization: `Bearer ${credential}`, Accept: "application/vnd.github+json",
    "Content-Type": "application/json", "User-Agent": "portal-daily-source-clock",
    "X-GitHub-Api-Version": "2026-03-10",
  };
  let runs;
  try {
    runs = await readRuns(fetchWithTimeout, base, headers, repo, due, sleep);
  } catch {
    return { ...baseState, state: "inspection_unavailable" };
  }
  const active = runs.find((run) => ACTIVE.has(run.status));
  if (active) return { ...baseState, state: "sync_active", run_id: active.id };

  const title = `GDrive to Dropbox Sync [clock ${day}]`;
  const dueRuns = runs.filter((run) => Date.parse(run.created_at) >= due);
  const clockRuns = dueRuns.filter((run) => run.event === "workflow_dispatch" && run.display_title === title);
  const completed = dueRuns.find((run) => run.conclusion === "success"
    && (run.event === "schedule" || clockRuns.includes(run)));
  if (completed) return { ...baseState, state: "sync_completed", run_id: completed.id };

  let saved;
  let prior;
  try {
    saved = await bucket.get(UPSTREAM_SYNC_RECEIPT_KEY);
    if (saved) {
      const data = JSON.parse(await saved.text());
      if (!saved.etag || !validReceipt(data)) throw new Error("upstream_receipt_invalid");
      if (data.date_folder === day) prior = data;
    }
  } catch {
    return { ...baseState, state: "receipt_unavailable" };
  }

  const lastRequestAt = prior ? Date.parse(prior.requested_at) : 0;
  if (prior && prior.state !== "rejected" && !clockRuns.some((run) =>
    prior.run_id ? run.id === prior.run_id : Date.parse(run.created_at) >= Math.floor(lastRequestAt / 1000) * 1000)) {
    // A lost acknowledgement never proves that the first dispatch failed. The
    // next tick reconciles the exact batch in GitHub before another POST.
    return { ...baseState, state: "awaiting_dispatch_readback", ...(prior.run_id ? { run_id: prior.run_id } : {}) };
  }
  const attempts = Math.max(prior?.attempts || 0, clockRuns.length);
  if (attempts >= MAX_ATTEMPTS) return { ...baseState, state: "retry_limit" };
  const lastAttemptAt = Math.max(lastRequestAt, ...clockRuns.map((run) => Date.parse(run.created_at)));
  if (nowMs - lastAttemptAt < RETRY_DELAY_MS) return { ...baseState, state: "sync_retry_wait" };

  const next = { ...baseState, state: "dispatching", requested_at: new Date(nowMs).toISOString(), attempts: attempts + 1 };
  const httpMetadata = { contentType: "application/json", cacheControl: "private, no-store" };
  let claim;
  try {
    claim = await bucket.put(UPSTREAM_SYNC_RECEIPT_KEY, JSON.stringify(next), {
      onlyIf: saved ? { etagMatches: saved.etag } : { etagDoesNotMatch: "*" },
      httpMetadata,
    });
  } catch {
    return { ...baseState, state: "receipt_unavailable" };
  }
  if (!claim) return { ...baseState, state: "dispatch_claimed" };

  try {
    const response = await fetchWithTimeout(`${base}/dispatches`, {
      method: "POST", headers, redirect: "manual",
      body: JSON.stringify({ ref: "main", inputs: { clock_sync_date: day } }),
    }, 8000);
    next.state = response.ok ? "accepted" : (response.status >= 500 ? "unknown" : "rejected");
    if (response.status === 200) {
      const accepted = await response.json().catch(() => null);
      if (validId(accepted?.workflow_run_id)) next.run_id = accepted.workflow_run_id;
    } else {
      await response.body?.cancel().catch(() => {});
    }
  } catch {
    next.state = "unknown";
  }
  try {
    await bucket.put(UPSTREAM_SYNC_RECEIPT_KEY, JSON.stringify(next), {
      onlyIf: { etagMatches: claim.etag }, httpMetadata,
    });
  } catch {
    // The initial claim still blocks a second dispatch without GitHub evidence.
  }
  return next;
}

export async function runUpstreamSyncClock(env, fetchWithTimeout) {
  const result = await reconcileUpstreamDriveSync(env, { fetchWithTimeout });
  if (result.state === "outside_source_window") return;
  const check = { state: result.state, checked_at: new Date().toISOString() };
  if (result.date_folder) check.date_folder = result.date_folder;
  if (result.run_id) check.run_id = result.run_id;
  try {
    await env.REPORT_BUCKET?.put(UPSTREAM_SYNC_CHECK_KEY, JSON.stringify(check), {
      httpMetadata: { contentType: "application/json", cacheControl: "private, no-store" },
    });
  } catch {
    // A diagnostic write cannot change dispatch ownership or cause another POST.
  }
  console.log("Upstream Drive sync check", JSON.stringify(check));
}
