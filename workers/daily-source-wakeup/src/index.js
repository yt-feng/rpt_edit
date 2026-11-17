import { wakeDailyReportSource } from "../../portal-suite-worker/src/daily-source-wakeup.js";

async function fetchWithTimeout(url, options, timeoutMs) {
  return fetch(url, { ...options, signal: AbortSignal.timeout(timeoutMs) });
}

export default {
  async scheduled(_event, env, ctx) {
    ctx.waitUntil(wakeDailyReportSource(env, {
      repository: (config) => String(config.GH_REPO || "").trim(),
      fetchWithTimeout,
    }).then((result) => console.log("Daily source wake-up", JSON.stringify(result))));
  },
};
