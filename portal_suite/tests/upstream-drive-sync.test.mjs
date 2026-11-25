import assert from "node:assert/strict";
import test from "node:test";
import {
  reconcileUpstreamDriveSync, UPSTREAM_SYNC_RECEIPT_KEY,
} from "../../workers/daily-source-wakeup/src/upstream-drive-sync.js";

const MIDNIGHT = Date.parse("2026-11-24T16:00:00Z");
const DUE = "2026-11-24T15:43:00Z";
const DAY = "261124";
const REPO = "source/report-sync";

function run(changes = {}) {
  return {
    id: 10, event: "schedule", status: "completed", conclusion: "success",
    head_branch: "main", path: ".github/workflows/sync.yml", head_repository: { full_name: REPO },
    display_title: "GDrive to Dropbox Sync", created_at: DUE, ...changes,
  };
}

function clockRun(changes = {}) {
  return run({ id: 12, event: "workflow_dispatch", display_title: `GDrive to Dropbox Sync [clock ${DAY}]`, ...changes });
}

function fixture({ runs = [], tick = MIDNIGHT, http = 200, mismatch = false, failWrite = false } = {}) {
  const records = new Map();
  const calls = [];
  let etag = 0;
  const env = {
    REPORT_UPSTREAM_SYNC_REPO: REPO, GH_DISPATCH_TOKEN: "clock-credential",
    REPORT_BUCKET: {
      async get(k) {
        const item = records.get(k);
        return item && { etag: item.etag, text: () => item.body };
      },
      async put(k, body, opts) {
        if (failWrite) throw new Error("storage down");
        const current = records.get(k);
        if (opts.onlyIf.etagDoesNotMatch && current
          || opts.onlyIf.etagMatches && current?.etag !== opts.onlyIf.etagMatches) return null;
        const item = { body, etag: String(++etag) };
        records.set(k, item);
        return item;
      },
    },
  };
  const deps = {
    now: () => tick, sleep: async () => {},
    async fetchWithTimeout(url, options) {
      calls.push({ url: new URL(url), options });
      if (options.method !== "POST") {
        return Response.json({ total_count: runs.length + Number(mismatch), workflow_runs: runs });
      }
      if (http === "lost") throw new Error("transport failure");
      return http === 200 ? Response.json({ workflow_run_id: 12 })
        : new Response(null, { status: http });
    },
  };
  return {
    env, runs, calls, records,
    posts: () => calls.filter(({ options }) => options.method === "POST"),
    tick: (set) => { tick = set; },
    invoke: () => reconcileUpstreamDriveSync(env, deps),
  };
}

test("at midnight an absent sync is dispatched for the previous Beijing batch", async () => {
  const f = fixture();
  assert.deepEqual(await f.invoke(), {
    date_folder: DAY, state: "accepted", requested_at: new Date(MIDNIGHT).toISOString(), attempts: 1, run_id: 12,
  });
  const [read, post] = f.calls;
  assert.equal(read.url.searchParams.get("created"), ">=2026-11-23T15:43:00.000Z");
  assert.equal(read.url.searchParams.get("branch"), "main");
  assert.equal(post.url.pathname, "/repos/source/report-sync/actions/workflows/sync.yml/dispatches");
  assert.equal(post.options.redirect, "manual");
  assert.deepEqual(JSON.parse(post.options.body), { ref: "main", inputs: { clock_sync_date: DAY } });
});

test("the clock gives GitHub the 23:43 to midnight window", async () => {
  const f = fixture({ tick: MIDNIGHT - 1 });
  assert.equal((await f.invoke()).state, "outside_source_window");
  f.tick(MIDNIGHT + (23 * 60 + 43) * 60 * 1000);
  assert.equal((await f.invoke()).state, "outside_source_window");
  assert.equal(f.calls.length, 0);
});

test("a live native or manual sync and successful due native or exact clock run each avoid duplication", async () => {
  for (const evidence of [
    [run({ status: "in_progress", conclusion: null }), "sync_active"],
    [run({ event: "workflow_dispatch", status: "queued", conclusion: null }), "sync_active"],
    [run(), "sync_completed"], [clockRun(), "sync_completed"],
  ]) {
    const f = fixture({ runs: [evidence[0]] });
    assert.equal((await f.invoke()).state, evidence[1]);
    assert.equal(f.posts().length, 0);
  }
});

test("a previous-day run and a completed notify-only run never mask a missed full sync", async () => {
  const f = fixture({ runs: [
    run({ created_at: "2026-11-24T15:42:59Z" }),
    clockRun({ display_title: `GDrive to Dropbox Sync [notify ${DAY}]` }),
  ] });
  assert.equal((await f.invoke()).state, "accepted");
  assert.equal(f.posts().length, 1);
});

test("untrusted or inconsistent inventories never authorize a POST", async () => {
  for (const options of [{ mismatch: true }, { runs: [run({ head_repository: { full_name: "foreign/repo" } })] }]) {
    const f = fixture(options);
    assert.equal((await f.invoke()).state, "inspection_unavailable");
    assert.equal(f.posts().length, 0);
  }
});

test("the R2 conditional claim authorizes a single POST from concurrent ticks", async () => {
  const f = fixture();
  const results = await Promise.all([f.invoke(), f.invoke()]);
  assert.deepEqual(results.map((r) => r.state).sort(), ["accepted", "dispatch_claimed"]);
  assert.equal(f.posts().length, 1);
  assert.equal(JSON.parse(f.records.get(UPSTREAM_SYNC_RECEIPT_KEY).body).run_id, 12);
  const broken = fixture({ failWrite: true });
  assert.equal((await broken.invoke()).state, "receipt_unavailable");
  assert.equal(broken.posts().length, 0);
});

test("ambiguous acknowledgements wait for dated Github readback, then retry only a known failure", async () => {
  const f = fixture({ http: "lost" });
  assert.equal((await f.invoke()).state, "unknown");
  f.tick(MIDNIGHT + 30 * 60 * 1000);
  assert.equal((await f.invoke()).state, "awaiting_dispatch_readback");
  f.runs.push(clockRun({ created_at: new Date(MIDNIGHT).toISOString(), conclusion: "failure" }));
  assert.equal((await f.invoke()).attempts, 2);
  f.tick(MIDNIGHT + 60 * 60 * 1000);
  f.runs.push(clockRun({ id: 13, created_at: new Date(MIDNIGHT + 30 * 60 * 1000).toISOString(), conclusion: "failure" }));
  assert.equal((await f.invoke()).state, "retry_limit");
  assert.equal(f.posts().length, 2);
});
