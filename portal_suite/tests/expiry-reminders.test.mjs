import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";
import worker from "../../workers/portal-suite-worker/src/index.js";
import { createExpiryReminders, resolveExpiryMembership } from "../../workers/portal-suite-worker/src/expiry-reminders.js";

const DAY = 86400000;
const NOW = Date.parse("2030-01-10T02:00:00.000Z");
const iso = (n) => new Date(n).toISOString();
const key = (id) => `_account/expiry-reminders-v1/accounts/${encodeURIComponent(id)}`;
class Bucket {
  rows = new Map(); version = 0; writes = 0; afterPut = null;
  seed(key, value) { this.rows.set(key, { value: JSON.stringify(value), etag: String(++this.version) }); }
  value(key) { return JSON.parse(this.rows.get(key)?.value || "null"); }
  async get(key) { const row = this.rows.get(key); return row ? { etag: row.etag, async json() { return JSON.parse(row.value); }, async text() { return row.value; } } : null; }
  async put(key, value, options = {}) {
    const old = this.rows.get(key);
    if (options.onlyIf?.etagMatches && options.onlyIf.etagMatches !== old?.etag) return null;
    if (options.onlyIf?.etagDoesNotMatch === "*" && old) return null;
    this.seed(key, JSON.parse(value)); this.writes += 1;
    if (this.afterPut) await this.afterPut(key, JSON.parse(value));
    return { etag: this.rows.get(key).etag };
  }
  async list({ prefix, limit = 20, cursor = "" }) {
    const keys = [...this.rows.keys()].filter((key) => key.startsWith(prefix)).sort();
    const start = Number(cursor) || 0;
    return { objects: keys.slice(start, start + limit).map((key) => ({ key })), truncated: start + limit < keys.length, cursor: String(start + limit) };
  }
}
function fixture(end = NOW + 7 * DAY) {
  const user = { id: "reader", email: "reader@example.invalid", username: "reader" };
  return { user, disabled: false, generated: false, privileged: false,
    entitlement: { plan: "annual", status: "active", lifetime: false, current_period_end: iso(end), created_at: iso(NOW - 50 * DAY), authority_occurred_at: iso(NOW - 50 * DAY) }, admin: null, trial: null };
}
function harness(options = {}) {
  const bucket = new Bucket();
  let snapshot = options.snapshot || fixture();
  let now = NOW;
  const sent = [];
  const loads = [];
  const service = createExpiryReminders({ bucket: () => bucket, configured: () => true, now: () => now,
    load: async (_env, user, fresh) => { loads.push({ user, fresh }); return options.load ? options.load(user, fresh, snapshot) : structuredClone(snapshot); },
    send: async (_env, message) => { sent.push(message); return options.send ? options.send(message) : { sent: true }; },
    unsubscribeUrl: async () => "https://kcdesk.com/api/account/expiry-reminders/unsubscribe?token=fixture",
    list: options.list || (async () => ({ items: [], cursor: "" })),
  });
  return { bucket, service, sent, loads, user: snapshot.user, setSnapshot: (next) => { snapshot = next; }, setNow: (value) => { now = value; } };
}

test("preview is read-only and shows actual BJT expiry and contact details", async () => {
  const h = harness();
  const preview = await h.service.status({}, h.user, NOW);
  assert.equal(preview.reminder.next_stage, "before_7");
  assert.equal(preview.reminder.expires_bjt, "2030-01-17 10:00 北京时间");
  assert.ok(preview.preview.text.includes("info@kcdesk.com"));
  assert.match(preview.preview.text, /MacroGate/u);
  assert.doesNotMatch(preview.preview.text, /支付|RAG|payment/iu);
  assert.equal(h.bucket.writes, 0);
  assert.equal(h.sent.length, 0);
});

test("excluded identities, lifetime, revocation and authority precedence never become reminder candidates", () => {
  for (const field of ["disabled", "generated", "privileged"]) {
    assert.equal(resolveExpiryMembership({ ...fixture(), [field]: true }, NOW).eligible, false);
  }
  const base = fixture();
  base.entitlement.lifetime = true;
  assert.equal(resolveExpiryMembership(base, NOW).reason, "lifetime");
  const revoked = fixture();
  revoked.admin = { status: "inactive", access_mode: "none", updated_at: iso(NOW - DAY) };
  assert.equal(resolveExpiryMembership(revoked, NOW).eligible, false);
  revoked.entitlement.authority_occurred_at = iso(NOW);
  assert.equal(resolveExpiryMembership(revoked, NOW).eligible, true, "later purchase overrides older closure");
  revoked.admin = { status: "active", access_mode: "all", current_period_end: iso(NOW - DAY), updated_at: iso(NOW) };
  revoked.entitlement.authority_occurred_at = iso(NOW - 2 * DAY);
  assert.equal(resolveExpiryMembership(revoked, NOW).expires_at, iso(NOW - DAY), "expired administrator authority must still suppress older entitlement");
});

test("the longest concurrent valid access avoids an early expired notice", () => {
  const data = fixture();
  data.admin = { status: "active", access_mode: "filters", current_period_end: iso(NOW + 50 * DAY), updated_at: iso(NOW - DAY) };
  assert.equal(resolveExpiryMembership(data, NOW).expires_at, iso(NOW + 50 * DAY));
});

test("concurrent cron attempts atomically reserve one provider send and never repeat a sent stage", async () => {
  const h = harness();
  const results = await Promise.all(Array.from({ length: 8 }, () => h.service.attempt({}, h.user, NOW)));
  assert.equal(results.filter((row) => row.attempted).length, 1);
  assert.equal(h.sent.length, 1);
  assert.equal(h.bucket.value(key(h.user.id)).last_status, "sent");
  await h.service.attempt({}, h.user, NOW + DAY);
  assert.equal(h.sent.length, 1);
});

test("three-stage cadence enforces minimum 48h and maximum three attempts per expiry", async () => {
  const h = harness();
  for (const offset of [0, 5, 8, 9, 10]) {
    h.setNow(NOW + offset * DAY);
    await h.service.attempt({}, h.user, NOW + offset * DAY);
  }
  assert.equal(h.sent.length, 3);
  const stages = h.bucket.value(key(h.user.id)).cycles[iso(NOW + 7 * DAY)];
  assert.deepEqual(Object.keys(stages), ["before_7", "before_2", "after_1"]);
  const times = Object.values(stages).map((row) => Date.parse(row.attempted_at));
  assert.ok(times.slice(1).every((time, i) => time - times[i] >= 2 * DAY));
});

test("late catch-up does not stack notices, and a changed expiry starts a new cycle without losing the gap", async () => {
  const h = harness();
  h.setNow(NOW + 4 * DAY);
  await h.service.attempt({}, h.user, NOW + 4 * DAY);
  h.setNow(NOW + 5 * DAY);
  await h.service.attempt({}, h.user, NOW + 5 * DAY);
  assert.equal(h.sent.length, 1);
  h.setSnapshot(fixture(NOW + 12 * DAY));
  await h.service.attempt({}, h.user, NOW + 5 * DAY);
  assert.equal(h.sent.length, 1);
  h.setNow(NOW + 6 * DAY);
  await h.service.attempt({}, h.user, NOW + 6 * DAY);
  assert.equal(h.sent.length, 2);
});

test("short trials receive only one pre-expiry notice, including after trial expiry", async () => {
  const snapshot = fixture(NOW + DAY);
  snapshot.entitlement = null;
  snapshot.trial = { status: "active", access_mode: "all", duration_value: "trial_3d", current_period_end: iso(NOW + DAY), created_at: iso(NOW - 2 * DAY) };
  const h = harness({ snapshot });
  assert.equal((await h.service.status({}, h.user, NOW)).reminder.next_stage, "trial_before");
  for (const offset of [0, 1, 2, 3]) { h.setNow(NOW + offset * DAY); await h.service.attempt({}, h.user, NOW + offset * DAY); }
  assert.equal(h.sent.length, 1);
});

test("renewal, disablement or opt-out between reserve and send cancels the old notice", async () => {
  for (const change of ["renew", "disable", "unsubscribe"]) {
    let h;
    h = harness({ load: async (_user, fresh, snapshot) => {
      if (!fresh) return snapshot;
      if (change === "renew") return fixture(NOW + 90 * DAY);
      if (change === "disable") return { ...snapshot, disabled: true };
      await h.service.preferences({}, h.user, false);
      return snapshot;
    } });
    const result = await h.service.attempt({}, h.user, NOW);
    assert.equal(result.status, "cancelled");
    assert.equal(h.sent.length, 0);
  }
});

test("provider failure, unknown outcome and a lost marker acknowledgement are never retried", async () => {
  for (const failure of ["failed", "unknown", "pending"]) {
    const h = harness({ send: async () => {
      if (failure === "unknown") throw new Error("PRIVATE PROVIDER RESPONSE");
      return { sent: failure !== "failed", detail: "PRIVATE EMAIL" };
    } });
    if (failure === "pending") h.bucket.afterPut = async (_key, value) => { if (value.last_status === "pending") { h.bucket.afterPut = null; throw new Error("lost commit acknowledgement"); } };
    await h.service.attempt({}, h.user, NOW).catch(() => null);
    await h.service.attempt({}, h.user, NOW + 60000);
    assert.equal(h.sent.length, failure === "pending" ? 0 : 1);
    assert.equal(h.bucket.value(key(h.user.id)).last_status, failure);
    assert.doesNotMatch(JSON.stringify([...h.bucket.rows.values()]), /PRIVATE/u);
  }
});

test("opt-out persists across cycles; explicit opt-in restores only future eligible stages", async () => {
  const h = harness();
  await h.service.preferences({}, h.user, false);
  assert.equal((await h.service.status({}, h.user, NOW)).reminder.reason, "unsubscribed");
  await h.service.attempt({}, h.user, NOW);
  assert.equal(h.sent.length, 0);
  await h.service.preferences({}, h.user, true);
  await h.service.attempt({}, h.user, NOW);
  assert.equal(h.sent.length, 1);
});

test("window excludes night and noon; the exact final pre-send time is checked", async () => {
  const h = harness();
  for (const now of [NOW - 60000, NOW + 2 * 3600000]) await h.service.attempt({}, h.user, now);
  assert.equal(h.sent.length, 0);
  h.setNow(NOW + 2 * 3600000);
  assert.equal((await h.service.attempt({}, h.user, NOW)).status, "cancelled");
  assert.equal(h.sent.length, 0);
});

test("a scan over 500 users completes by durable pagination, and repeat cron skips the completed pass", async () => {
  const users = Array.from({ length: 521 }, (_, i) => ({ id: `id-${i}`, email: `u${i}@example.invalid` }));
  const visited = [];
  const h = harness({ list: async (_env, cursor, limit) => {
    const start = Number(cursor) || 0;
    return { items: users.slice(start, start + limit).map((user, i) => ({ user, cursor: String(start + i + 1) })), cursor: start + limit < users.length ? String(start + limit) : "" };
  }, load: async (user) => { visited.push(user.id); return { user, generated: true }; } });
  for (let i = 0; i < 27; i += 1) await h.service.scan({}, NOW + i * 60000);
  const result = await h.service.scanStatus({});
  assert.equal(result.complete, true);
  assert.equal(result.processed, 521);
  assert.equal(new Set(visited).size, 521);
  assert.deepEqual(await h.service.scan({}, NOW + 30 * 60000), { skipped: true });
  assert.equal(h.sent.length, 0);
});

test("incomplete scanning retains its cursor across days and provider attempts are bounded", async () => {
  const users = Array.from({ length: 25 }, (_, i) => ({ id: `id-${i}`, email: `u${i}@example.invalid` }));
  const h = harness({ list: async (_env, cursor, limit) => {
    const start = Number(cursor) || 0;
    return { items: users.slice(start, start + limit).map((user, i) => ({ user, cursor: String(start + i + 1) })), cursor: start + limit < users.length ? String(start + limit) : "" };
  }, load: async (user) => ({ ...fixture(), user }) });
  await h.service.scan({}, NOW);
  assert.equal(h.sent.length, 9);
  let progress = await h.service.scanStatus({});
  assert.equal(progress.pending, true);
  assert.equal(progress.complete, false);
  assert.equal(progress.processed, 9);
  h.setNow(NOW + DAY);
  await h.service.scan({}, NOW + DAY);
  assert.equal(h.sent.length, 18);
  assert.equal(h.sent[9].to, "u9@example.invalid");
});

function signed(user, kind = "user") {
  const body = Buffer.from(JSON.stringify({ kind, sub: user.id, username: user.username, email: user.email, session_epoch: "", exp: Math.floor(Date.now() / 1000) + 3600 })).toString("base64url");
  return `${body}.${createHmac("sha256", "test-secret").update(`portal:account-token:v1:${body}`).digest("base64url")}`;
}
test("Worker endpoints enforce auth, preview has no writes, and unsubscribe GET requires confirmation POST", async () => {
  const bucket = new Bucket();
  const env = { ACCOUNT_STORE_MODE: "r2", REPORT_BUCKET: bucket, PASSWORD_SECRET: "test-secret", ALLOWED_ORIGIN: "https://portal.example.invalid" };
  const reader = { id: "reader", username: "reader", email: "reader@example.invalid" };
  const admin = { id: "admin", username: "admin-a", email: "admin-a@users.portal.example.invalid" };
  for (const user of [reader, admin]) for (const field of ["id", "username", "email"]) bucket.seed(`_account/users/${field}/${encodeURIComponent(user[field])}`, user);
  bucket.seed(`_account/entitlements/${encodeURIComponent(reader.email)}`, { email: reader.email, status: "active", plan: "annual", lifetime: false, current_period_end: iso(Date.now() + 7 * DAY) });
  const request = (path, user, method = "GET", payload) => worker.fetch(new Request(`https://portal.example.invalid/api${path}`, { method,
    headers: { "Content-Type": "application/json", ...(user ? { Authorization: `Bearer ${signed(user)}` } : {}) }, ...(payload ? { body: JSON.stringify(payload) } : {}) }), env, { waitUntil() {} });
  assert.equal((await request("/account/expiry-reminders", null)).status, 401);
  assert.equal((await request(`/account-admin/expiry-reminders?email=${reader.email}`, reader)).status, 403);
  const preview = await request(`/account-admin/expiry-reminders?email=${reader.email}`, admin);
  assert.equal(preview.status, 200);
  assert.equal((await preview.json()).reminder.eligible, true);
  assert.equal(bucket.writes, 0);
  assert.equal((await request("/account/expiry-reminders", reader, "POST", { enabled: "yes" })).status, 400);
  assert.equal((await request("/account/expiry-reminders", reader, "POST", { enabled: false })).status, 200);
  assert.equal(bucket.value(key(reader.id)).enabled, false);
  await request("/account/expiry-reminders", reader, "POST", { enabled: true });
  const link = `/account/expiry-reminders/unsubscribe?token=${encodeURIComponent(signed(reader, "membership-reminder-unsubscribe"))}`;
  const confirmation = await request(link, null);
  assert.equal(confirmation.status, 200);
  assert.match(await confirmation.text(), /form method="post"/u);
  assert.equal(bucket.value(key(reader.id)).enabled, true);
  assert.equal((await request(link, null, "POST")).status, 200);
  assert.equal(bucket.value(key(reader.id)).enabled, false);
  assert.equal((await request(`/account/expiry-reminders/unsubscribe?token=${encodeURIComponent(signed(reader))}`, null, "POST")).status, 400);
});

test("scheduled Supabase scan stays at 48 external requests for 20 accounts and 9 provider attempts", async () => {
  const bucket = new Bucket();
  const users = Array.from({ length: 20 }, (_, i) => ({ id: `id-${String(i).padStart(2, "0")}`, username: `reader${i}`, email: `reader${i}@example.invalid` }));
  const env = { ACCOUNT_STORE_MODE: "supabase", REPORT_BUCKET: bucket, PASSWORD_SECRET: "test-secret",
    SUPABASE_URL: "https://database.example.invalid", SUPABASE_SERVICE_ROLE_KEY: "fixture-only",
    NEWSFEED_EMAIL_PROVIDER: "brevo", BREVO_API_KEY: "fixture-only" };
  const calls = { page: 0, identity: 0, entitlement: 0, provider: 0 };
  const originalFetch = globalThis.fetch;
  const originalNow = Date.now;
  Date.now = () => NOW;
  globalThis.fetch = async (input, init) => {
    const url = new URL(String(input));
    const json = (value) => new Response(JSON.stringify(value), { status: 200, headers: { "Content-Type": "application/json" } });
    if (url.hostname === "database.example.invalid" && url.pathname === "/rest/v1/site_users") {
      const id = url.searchParams.get("id");
      if (id?.startsWith("eq.")) { calls.identity += 1; return json(users.filter((user) => user.id === id.slice(3))); }
      assert.equal(url.searchParams.get("limit"), "20");
      calls.page += 1;
      return json(users);
    }
    if (url.hostname === "database.example.invalid" && url.pathname === "/rest/v1/user_entitlements") {
      calls.entitlement += 1;
      const email = url.searchParams.get("email").slice(3);
      const index = users.findIndex((user) => user.email === email);
      return json([{ email, status: "active", plan: "annual", lifetime: false,
        current_period_end: iso(NOW + (index < 11 ? 50 : 7) * DAY) }]);
    }
    if (url.hostname === "api.brevo.com" && url.pathname === "/v3/smtp/email") {
      calls.provider += 1;
      assert.equal(init.method, "POST");
      return json({ messageId: "fixture" });
    }
    throw new Error("Unexpected external request in fixture");
  };
  try {
    let completed;
    await worker.scheduled({ cron: "* 2-3 * * *" }, env, { waitUntil(promise) { completed = promise; } });
    await completed;
    assert.deepEqual(calls, { page: 1, identity: 9, entitlement: 29, provider: 9 });
    assert.equal(Object.values(calls).reduce((a, b) => a + b, 0), 48);
    const scan = bucket.value("_account/expiry-reminders-v1/scan");
    assert.equal(scan.processed, 20);
    assert.equal(scan.attempted, 9);
    assert.equal(scan.errors, 0);
  } finally { globalThis.fetch = originalFetch; Date.now = originalNow; }
});
