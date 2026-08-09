import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.version = 0;
    this.failPutPrefixOnce = "";
    this.failGetAfterPutExact = "";
    this.failNextGetExact = "";
  }

  seed(key, value) {
    this.version += 1;
    this.rows.set(key, { value: typeof value === "string" ? value : JSON.stringify(value), etag: `v${this.version}` });
  }

  async get(key) {
    if (this.failNextGetExact && key === this.failNextGetExact) {
      this.failNextGetExact = "";
      throw new Error("injected R2 read failure");
    }
    const row = this.rows.get(key);
    if (!row) return null;
    return {
      etag: row.etag,
      body: new TextEncoder().encode(row.value),
      async text() { return row.value; },
    };
  }

  async put(key, value, options = {}) {
    if (this.failPutPrefixOnce && key.startsWith(this.failPutPrefixOnce)) {
      this.failPutPrefixOnce = "";
      throw new Error("injected R2 write failure");
    }
    const current = this.rows.get(key);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && (!current || current.etag !== onlyIf.etagMatches)) return null;
    if (onlyIf.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const text = value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value);
    const row = { value: text, etag: `v${this.version}` };
    this.rows.set(key, row);
    if (this.failGetAfterPutExact && key === this.failGetAfterPutExact) {
      this.failNextGetExact = key;
      this.failGetAfterPutExact = "";
    }
    return { etag: row.etag };
  }
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY: "test-master-key",
    PASSWORD_SECRET: "test-password-secret",
    CATALOG_URL: "https://static.example.invalid/catalog.json",
    STATIC_DATA_PREFIX: "edge-static/runtime-data",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  };
}

async function jsonRequest(env, pathName, options = {}) {
  const response = await worker.fetch(new Request(`https://worker.test${pathName}`, options), env, { waitUntil() {} });
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

async function register(env) {
  const captcha = await jsonRequest(env, "/captcha");
  assert.equal(captcha.response.status, 200);
  const svg = Buffer.from(String(captcha.data.image).split(",", 2)[1], "base64").toString("utf8");
  const equation = svg.match(/>(\d+) \+ (\d+) = \?</u);
  assert.ok(equation, "captcha equation must be readable in the fixture");
  const answer = String(Number(equation[1]) + Number(equation[2]));
  const auth = await jsonRequest(env, "/auth", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      action: "register",
      username: "reward-reader",
      email: "reward-reader@example.com",
      password: "test-pass-123",
      captcha_token: captcha.data.token,
      captcha_answer: answer,
    }),
  });
  assert.equal(auth.response.status, 201);
  assert.ok(auth.data.token);
  return auth.data.token;
}

function bearer(token) {
  return { Authorization: `Bearer ${token}` };
}

test("daily check-in is idempotent and grants exactly one catalog report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);

  const initial = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(initial.response.status, 200);
  assert.equal(initial.data.points, 0);
  assert.equal(initial.data.checked_in_today, false);

  const checkedIn = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(checkedIn.response.status, 200);
  assert.equal(checkedIn.data.points, 10);
  assert.equal(checkedIn.data.current_streak, 1);
  assert.equal(checkedIn.data.daily_available, true);

  const duplicateCheckin = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(duplicateCheckin.response.status, 200);
  assert.equal(duplicateCheckin.data.points, 10, "duplicate check-ins must not add points");

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);
  assert.equal(claimed.data.rewards.daily_claimed, true);

  const accessA = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessA.response.status, 200);
  assert.equal(accessA.data.can_download, true, "the reward must use the existing purchase entitlement path");

  const secondDaily = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(secondDaily.response.status, 200);
  assert.equal(secondDaily.data.claimed, false);
  assert.equal(secondDaily.data.already_claimed_today, true);

  const accessB = await jsonRequest(env, `/entitlement?report_id=${reportB}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessB.response.status, 200);
  assert.equal(accessB.data.can_download, false);

  const insufficient = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "points", report_id: reportB }),
  });
  assert.equal(insufficient.response.status, 409);
  assert.match(insufficient.data.detail, /积分不足/u);
});

test("failed purchase mirroring still grants exactly one report from reward state", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report C", filename: "c.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_available, false);
  assert.equal(status.data.daily_claimed, true);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true, "the atomic reward grant is authoritative when the mirror is unavailable");
});

test("concurrent daily claims grant at most one report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report D", filename: "d.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report E", filename: "e.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  const [left, right] = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  })));
  assert.deepEqual([left, right].map(({ data }) => Boolean(data.claimed)).sort(), [false, true]);
  const access = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(
    env,
    `/entitlement?report_id=${reportId}&source=catalog`,
    { headers: bearer(token) },
  )));
  assert.equal(access.filter(({ data }) => data.can_download).length, 1);
});

test("a committed reward never depends on a purchase readback", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failGetAfterPutExact = `_account/purchases/catalog/${reportA}/${encodeURIComponent("reward-reader@example.com")}`;

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const duplicate = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(duplicate.response.status, 200);
  assert.equal(duplicate.data.claimed, false);
  assert.equal(duplicate.data.already_claimed_today, true);

  const access = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.response.status, 200);
  assert.equal(access.data.can_download, true);
  assert.equal(access.data.reward_access_matched, true);
  assert.ok(bucket.failNextGetExact, "purchase readback should remain untouched because reward state authorizes directly");
});

test("same-report retry cannot restore a consumed daily slot when purchase mirroring fails", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";
  const requests = [1, 2].map(() => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  }));
  const results = await Promise.all(requests);
  assert.ok(results.every(({ response }) => response.status === 200));
  assert.equal(results.filter(({ data }) => data.claimed).length, 1);
  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_claimed, true);
  assert.equal(status.data.daily_available, false);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true);
});

test("course API enforces at least 30 remaining days on the server", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);
  const token = await register(env);
  const email = "reward-reader@example.com";
  const entitlementKey = `_account/entitlements/${encodeURIComponent(email)}`;

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const allowed = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(allowed.response.status, 200);
  assert.equal(allowed.data.can_access, true);
  assert.deepEqual(allowed.data.courses, ["WSO", "WSP", "Fundamental Edge"]);

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 29 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const denied = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(denied.response.status, 200);
  assert.equal(denied.data.can_access, false);
  assert.deepEqual(denied.data.courses, []);

  bucket.rows.delete(entitlementKey);
  const accessKey = `_account/access/${encodeURIComponent(email)}`;
  const accessBase = {
    id: "access-1",
    email,
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    duration_value: "1",
    institutions: [],
    industries: [],
    page_ranges: [],
    download_items: [],
    download_limit: 0,
    download_count: 0,
    note: "",
    source: "stored",
  };
  bucket.seed(accessKey, { ...accessBase, access_mode: "filters", institutions: ["NOM"] });
  const filtered = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(filtered.data.can_access, false, "a filtered report grant is not a membership");

  bucket.seed(accessKey, {
    ...accessBase,
    access_mode: "all",
    duration_value: "trial_3d",
    download_limit: 10,
  });
  const limited = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(limited.data.can_access, false, "a limited report grant is not a membership");
});

test("restricted course catalog and contact are absent from the unauthenticated static page", async () => {
  const { readFile } = await import("node:fs/promises");
  const html = await readFile(path.join(root, "portal_suite/site_src/courses.html"), "utf8");
  assert.doesNotMatch(html, /WSO|WSP|Fundamental Edge/u);
  assert.doesNotMatch(html, /Support Contact|support@portal\.example\.invalid|mailto:/u);
  assert.match(html, /id="courseCatalog"[^>]*hidden/u);
});

test("frontend distinguishes an already-used daily reward from a successful claim", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  assert.match(source, /if \(data\.already_claimed_today\)/u);
  assert.match(source, /if \(!data\.claimed\) throw new Error/u);
  const duplicateBranch = source.slice(
    source.indexOf("if (data.already_claimed_today)"),
    source.indexOf("if (data.already_owned)"),
  );
  assert.doesNotMatch(duplicateBranch, /portal-reward-change|status:\s*"success"/u);
});
