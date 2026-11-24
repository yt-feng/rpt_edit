import { wakeDailyReportSource } from "../../portal-suite-worker/src/daily-source-wakeup.js";

import { handleDropboxReady } from "./dropbox-ready.js";

export const DAILY_SOURCE_CLOCK_CHECK_KEY = "_account/ops/daily-source-clock-check.json";
const CHECK_STATES = new Set([
  "before_daily_start", "unconfigured", "inspection_unavailable", "wake_active", "wake_recent",
  "dispatch_cooldown", "dispatch_claimed", "receipt_unavailable", "dispatching", "accepted", "observed", "unknown", "rejected",
]);

async function fetchWithTimeout(url, options, timeoutMs) {
  return fetch(url, { ...options, signal: AbortSignal.timeout(timeoutMs) });
}

export default {
  fetch(request, env) {
    return handleDropboxReady(request, env, { fetchWithTimeout });
  },

  async scheduled(_event, env, ctx) {
    ctx.waitUntil((async () => {
      let result;
      try {
        result = await wakeDailyReportSource(env, {
          repository: (config) => String(config.GH_REPO || "").trim(),
          fetchWithTimeout,
        });
      } catch (_error) {
        result = { state: "inspection_unavailable" };
      }
      const check = {
        state: CHECK_STATES.has(result?.state) ? result.state : "inspection_unavailable",
        checked_at: new Date(Date.now()).toISOString(),
      };
      if (Number.isSafeInteger(result?.run_id) && result.run_id > 0) check.run_id = result.run_id;
      try {
        // Separate diagnostic evidence: never replace or release the dispatch
        // receipt/lease, including when this tick correctly skips a new wake.
        await env.REPORT_BUCKET?.put(DAILY_SOURCE_CLOCK_CHECK_KEY, JSON.stringify(check), {
          httpMetadata: { contentType: "application/json", cacheControl: "private, no-store" },
        });
      } catch (_error) {
        // Diagnostics must not prevent or retry the completed wake check.
      }
      console.log("Daily source clock check", JSON.stringify(check));
    })());
  },
};
