import assert from "node:assert/strict";
import test from "node:test";
import { wakeDailyReportSource, DAILY_SOURCE_WAKEUP_STATE_KEY } from "../../workers/portal-suite-worker/src/daily-source-wakeup.js";
import worker from "../../workers/portal-suite-worker/src/index.js";
import independentClock, { DAILY_SOURCE_CLOCK_CHECK_KEY } from "../../workers/daily-source-wakeup/src/index.js";

const NOW = Date.parse("2026-11-17T01:00:00Z");
const HOUR = 60 * 60 * 1000;
const REPO = "owner/reports";
const WORKFLOW = "daily-report-source-wakeup.yml";

class Bucket {
  constructor() { this.rows = new Map(); this.serial = 0; }
  async get(key) {
    const row = this.rows.get(key);
    return row ? { etag: row.etag, text: async () => row.value } : null;
  }
  async put(key, value, { onlyIf = {} } = {}) {
    const row = this.rows.get(key);
    if (onlyIf.etagDoesNotMatch === "*" && row) return null;
    if (onlyIf.etagMatches && row?.etag !== onlyIf.etagMatches) return null;
    const etag = String(++this.serial);
    this.rows.set(key, { value, etag });
    return { etag };
  }
  read() { return JSON.parse(this.rows.get(DAILY_SOURCE_WAKEUP_STATE_KEY).value); }
}

function run(overrides = {}) {
  return {
    id: 42, path: `.github/workflows/${WORKFLOW}`, head_branch: "main", head_repository: { full_name: REPO },
    status: "completed", event: "schedule", created_at: new Date(NOW - 2 * HOUR).toISOString(), ...overrides,
  };
}

function fixture(options = {}) {
  const bucket = options.bucket || new Bucket();
  const env = { GH_REPO: REPO, GH_DISPATCH_TOKEN: "private-dispatch-token", GH_READ_TOKEN: "private-read-token", REPORT_BUCKET: bucket };
  const calls = [];
  const runs = options.runs || [run()];
  const deps = {
    repository: (config) => config.GH_REPO, now: () => NOW,
    fetchWithTimeout: async (url, init = {}) => {
      calls.push({ url, ...init });
      if (init.method === "POST") {
        if (options.acceptedRun) runs.push(options.acceptedRun);
        if (options.unknownPost) throw new Error("private provider failure");
        return new Response(null, { status: options.postStatus || 204 });
      }
      if (options.failRead || (options.rejectRead && init.headers.Authorization === "Bearer private-read-token")) {
        return new Response(null, { status: options.failRead || 403 });
      }
      const params = new URL(url).searchParams;
      const rows = runs.filter((item) => (!params.has("event") || item.event === params.get("event"))
        && (!params.has("status") || item.status === params.get("status")))
        .sort((a, b) => Date.parse(b.created_at) - Date.parse(a.created_at));
      return Response.json(options.invalidInventory || { total_count: rows.length, workflow_runs: rows.slice(0, 1) });
    },
  };
  return { bucket, env, deps, calls, runs, invoke: () => wakeDailyReportSource(env, deps), posts: () => calls.filter((call) => call.method === "POST") };
}

test("stale schedule dispatches only the metadata workflow on main and stores its receipt", async () => {
  const f = fixture();
  assert.equal((await f.invoke()).state, "accepted");
  assert.equal(f.posts().length, 1);
  assert.equal(f.posts()[0].url, `https://api.github.com/repos/${REPO}/actions/workflows/${WORKFLOW}/dispatches`);
  assert.deepEqual(JSON.parse(f.posts()[0].body), { ref: "main" });
  assert.equal(f.bucket.read().state, "accepted");
  assert.equal(f.calls.length, 9);
});

test("recent scheduled or manually dispatched wake suppresses a new POST through half an hour", async () => {
  for (const event of ["schedule", "workflow_dispatch"]) {
    const f = fixture({ runs: [run({ event, created_at: new Date(NOW - HOUR / 2).toISOString() })] });
    assert.equal((await f.invoke()).state, "wake_recent");
    assert.equal(f.posts().length, 0);
  }
});

test("the half-hour stale threshold permits fallback while the one-hour dispatch lease remains independent", async () => {
  const f = fixture({ runs: [run({ created_at: new Date(NOW - HOUR / 2 - 1).toISOString() })] });
  assert.equal((await f.invoke()).state, "accepted");
  const cooling = fixture();
  await cooling.bucket.put(DAILY_SOURCE_WAKEUP_STATE_KEY, JSON.stringify({ state: "unknown", requested_at: new Date(NOW - 45 * 60 * 1000).toISOString() }));
  assert.equal((await cooling.invoke()).state, "dispatch_cooldown");
  assert.equal(cooling.posts().length, 0);
});

test("all active statuses suppress dispatch even when an active wake is older than recent completed runs", async () => {
  for (const status of ["queued", "pending", "in_progress", "waiting", "requested"]) {
    const f = fixture({ runs: [run(), run({ id: 7, status, created_at: new Date(NOW - 5 * HOUR).toISOString() })] });
    assert.deepEqual(await f.invoke(), { state: "wake_active", run_id: 7 });
    assert.equal(f.posts().length, 0);
  }
});

test("failed or malformed GitHub inspection never writes a lease or dispatches", async () => {
  for (const options of [{ failRead: 503 }, { invalidInventory: { total_count: 1, workflow_runs: [] } }, { runs: [run({ head_repository: { full_name: "other/reports" } })] }]) {
    const f = fixture(options);
    assert.equal((await f.invoke()).state, "inspection_unavailable");
    assert.equal(f.posts().length, 0);
    assert.equal(f.bucket.rows.size, 0);
  }
});

test("read permission rejection falls back to the existing dispatch credential", async () => {
  const f = fixture({ rejectRead: true });
  assert.equal((await f.invoke()).state, "accepted");
  assert.equal(f.posts().length, 1);
  assert.equal(f.posts()[0].headers.Authorization, "Bearer private-dispatch-token");
});

test("conditional R2 lease allows only one concurrent worker to POST", async () => {
  const f = fixture();
  const results = await Promise.all([f.invoke(), f.invoke()]);
  assert.deepEqual(results.map((result) => result.state).sort(), ["accepted", "dispatch_claimed"]);
  assert.equal(f.posts().length, 1);
});

test("unknown POST is read back and its lease prevents a second POST while visibility is delayed", async () => {
  const f = fixture({ unknownPost: true });
  assert.equal((await f.invoke()).state, "unknown");
  const afterDispatch = f.calls.length;
  assert.equal((await f.invoke()).state, "dispatch_cooldown");
  assert.equal(f.calls.length - afterDispatch, 7);
  assert.equal(f.posts().length, 1);
  assert.equal(f.bucket.read().state, "unknown");
});

test("a lost acknowledgement that GitHub accepted is identified by the subsequent read", async () => {
  const acceptedRun = run({ id: 99, event: "workflow_dispatch", status: "queued", created_at: new Date(NOW).toISOString() });
  const f = fixture({ unknownPost: true, acceptedRun });
  assert.deepEqual(await f.invoke(), { state: "observed", requested_at: new Date(NOW).toISOString(), previous_dispatch_run_id: 0, run_id: 99 });
  assert.deepEqual(await f.invoke(), { state: "wake_active", run_id: 99 });
  assert.equal(f.posts().length, 1);
});

test("confirmed completed wake allows the next stale check before the ambiguous one-hour lease expires", async () => {
  for (const unknownPost of [false, true]) {
    const f = fixture({ unknownPost });
    await f.invoke();
    f.runs.push(run({ id: 99, event: "workflow_dispatch", created_at: new Date(NOW + 1000).toISOString() }));
    f.deps.now = () => NOW + 31 * 60 * 1000;
    await f.invoke();
    assert.equal(f.posts().length, 2);
    assert.equal(f.bucket.read().previous_dispatch_run_id, 99);
  }
});

test("an existing manual wake cannot release the lease or be claimed as a new dispatch receipt", async () => {
  const f = fixture({ unknownPost: true, runs: [run({ id: 9, event: "workflow_dispatch" })] });
  await f.invoke();
  f.deps.now = () => NOW + 31 * 60 * 1000;
  assert.equal((await f.invoke()).state, "dispatch_cooldown");
  assert.equal(f.posts().length, 1);
  assert.equal(f.bucket.read().previous_dispatch_run_id, 9);
});

test("expired receipt allows another check only after successful current run inventory", async () => {
  const f = fixture();
  await f.bucket.put(DAILY_SOURCE_WAKEUP_STATE_KEY, JSON.stringify({ state: "unknown", requested_at: new Date(NOW - HOUR - 1).toISOString() }));
  assert.equal((await f.invoke()).state, "accepted");
  assert.equal(f.posts().length, 1);
  const blocked = fixture({ bucket: f.bucket, failRead: 503 });
  assert.equal((await blocked.invoke()).state, "inspection_unavailable");
  assert.equal(blocked.posts().length, 0);
});

test("lease storage failure prevents POST and post-result storage failure retains the initial cooldown", async () => {
  const f = fixture();
  const write = f.bucket.put.bind(f.bucket);
  let count = 0;
  f.bucket.put = async (...args) => {
    count += 1;
    if (count === 2) throw new Error("storage unavailable");
    return write(...args);
  };
  assert.equal((await f.invoke()).state, "accepted");
  assert.equal(f.bucket.read().state, "dispatching");
  assert.equal((await f.invoke()).state, "dispatch_cooldown");
  assert.equal(f.posts().length, 1);
  const blocked = fixture();
  blocked.bucket.put = async () => { throw new Error("storage unavailable"); };
  assert.equal((await blocked.invoke()).state, "receipt_unavailable");
  assert.equal(blocked.posts().length, 0);
});

test("midnight gate and absent credentials perform no external requests", async () => {
  const f = fixture();
  f.deps.now = () => Date.parse("2026-11-16T17:00:00Z");
  assert.equal((await f.invoke()).state, "before_daily_start");
  f.deps.now = () => NOW;
  f.env.GH_DISPATCH_TOKEN = "unconfigured";
  assert.equal((await f.invoke()).state, "unconfigured");
  assert.equal(f.calls.length, 0);
});

test("normal half-hour scheduled entry runs the watchdog using existing environment bindings", async (t) => {
  const f = fixture();
  t.mock.method(Date, "now", () => NOW);
  t.mock.method(globalThis, "fetch", async (url, init) => {
    if (String(url).startsWith("https://api.github.com/")) return f.deps.fetchWithTimeout(String(url), init);
    throw new Error("unrelated scheduled fixture request");
  });
  const pending = [];
  await worker.scheduled({ cron: "*/30 * * * *" }, f.env, { waitUntil(promise) { pending.push(promise); } });
  await Promise.all(pending);
  assert.equal(f.posts().length, 1);
  assert.equal(f.bucket.read().state, "accepted");
});

test("isolated clock uses the same receipt and deduplication without a public HTTP entry", async (t) => {
  const f = fixture();
  t.mock.method(Date, "now", () => NOW);
  t.mock.method(globalThis, "fetch", (url, init) => f.deps.fetchWithTimeout(String(url), init));
  const pending = [];
  await independentClock.scheduled({ cron: "*/30 * * * *" }, f.env, {
    waitUntil(promise) { pending.push(promise); },
  });
  await Promise.all(pending);
  assert.equal(f.posts().length, 1);
  assert.equal(f.bucket.read().state, "accepted");
  assert.equal((await f.invoke()).state, "dispatch_cooldown");
  assert.equal(independentClock.fetch, undefined);
  assert.deepEqual(JSON.parse(f.bucket.rows.get(DAILY_SOURCE_CLOCK_CHECK_KEY).value), {
    state: "accepted", checked_at: new Date(NOW).toISOString(),
  });
});

test("isolated natural ticks record successful skips and failed reads without dispatching", async (t) => {
  t.mock.method(Date, "now", () => NOW);
  for (const [options, state, runId] of [
    [{ runs: [run({ created_at: new Date(NOW).toISOString() })] }, "wake_recent", 42],
    [{ runs: [run({ status: "in_progress" })] }, "wake_active", 42],
    [{ failRead: 503 }, "inspection_unavailable", undefined],
  ]) {
    const f = fixture(options);
    const fetchMock = t.mock.method(globalThis, "fetch", (url, init) => f.deps.fetchWithTimeout(String(url), init));
    const pending = [];
    await independentClock.scheduled({ cron: "*/30 * * * *" }, f.env, { waitUntil(promise) { pending.push(promise); } });
    await Promise.all(pending);
    const check = JSON.parse(f.bucket.rows.get(DAILY_SOURCE_CLOCK_CHECK_KEY).value);
    assert.deepEqual(check, { state, checked_at: new Date(NOW).toISOString(), ...(runId ? { run_id: runId } : {}) });
    assert.equal(f.posts().length, 0);
    assert.equal(f.bucket.rows.has(DAILY_SOURCE_WAKEUP_STATE_KEY), false);
    fetchMock.mock.restore();
  }
});

test("heartbeat write failure cannot change the dispatch receipt or issue another POST", async (t) => {
  const f = fixture();
  t.mock.method(Date, "now", () => NOW);
  t.mock.method(globalThis, "fetch", (url, init) => f.deps.fetchWithTimeout(String(url), init));
  const write = f.bucket.put.bind(f.bucket);
  f.bucket.put = async (key, ...args) => {
    if (key === DAILY_SOURCE_CLOCK_CHECK_KEY) throw new Error("private storage error");
    return write(key, ...args);
  };
  const pending = [];
  await independentClock.scheduled({ cron: "*/30 * * * *" }, f.env, { waitUntil(promise) { pending.push(promise); } });
  await Promise.all(pending);
  assert.equal(f.posts().length, 1);
  assert.equal(f.bucket.read().state, "accepted");
  assert.equal((await f.invoke()).state, "dispatch_cooldown");
  assert.equal(f.posts().length, 1);
});
