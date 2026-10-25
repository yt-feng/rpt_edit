import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFile } from "node:fs/promises";
import test from "node:test";
import { assertAcknowledgement } from "./form-acknowledgement-fixture.mjs";
import worker from "../../workers/portal-suite-worker/src/index.js";
import {
  membershipEligibleAt,
  reconcileMembershipContinuity,
  validateContinuityVerification,
} from "../../workers/portal-suite-worker/src/course-membership-continuity.js";

class MemoryR2 {
  rows = new Map();
  version = 0;
  failPrefix = "";
  conflictKey = "";
  reads = [];
  seed(key, value) { this.rows.set(key, { text: JSON.stringify(value), etag: `v${++this.version}` }); }
  json(key) { return this.rows.has(key) ? JSON.parse(this.rows.get(key).text) : null; }
  async get(key) {
    this.reads.push(key);
    const row = this.rows.get(key);
    return row ? { etag: row.etag, text: async () => row.text, json: async () => JSON.parse(row.text) } : null;
  }
  async put(key, body, options = {}) {
    if (this.failPrefix && key.startsWith(this.failPrefix)) throw new Error("injected storage failure");
    if (this.conflictKey === key) return null;
    const current = this.rows.get(key);
    if (options.onlyIf?.etagMatches && current?.etag !== options.onlyIf.etagMatches) return null;
    if (options.onlyIf?.etagDoesNotMatch === "*" && current) return null;
    const etag = `v${++this.version}`;
    this.rows.set(key, { text: String(body), etag });
    return { etag };
  }
  async list({ prefix = "" } = {}) {
    return { objects: [...this.rows.keys()].filter((key) => key.startsWith(prefix)).map((key) => ({ key })), truncated: false };
  }
}

// Exercise legacy server mutation hooks without reopening the disabled payment route.
const workerUrl = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
let internalSource = await readFile(workerUrl, "utf8");
internalSource = internalSource.replace(/from "\.\/([^"]+)"/gu, (_match, relative) => `from "${new URL(relative, workerUrl).href}"`);
internalSource += "\nexport { handlePaddleWebhook, applyVid2PptGift };";
const internal = await import(`data:text/javascript;base64,${Buffer.from(internalSource).toString("base64")}`);

const iso = (value) => new Date(value).toISOString();
const fingerprint = (n) => n.toString(16).padStart(64, "0");
const active = (n, end = "2030-01-01T00:00:00.000Z") => ({ fingerprint: fingerprint(n), active: true, covered_until: end });
const inactive = (n) => ({ fingerprint: fingerprint(n), active: false, covered_until: null });

test("eligibility uses two Beijing calendar months with the same local instant and month-end clamping", () => {
  assert.equal(membershipEligibleAt("2026-12-31T15:30:20.123Z"), "2027-02-28T15:30:20.123Z");
  assert.equal(membershipEligibleAt("2023-12-31T00:01:00.000+08:00"), "2024-02-28T16:01:00.000Z");
  assert.equal(membershipEligibleAt("2026-01-30T16:00:00.000Z"), "2026-03-30T16:00:00.000Z");
});

test("legacy membership begins observed evidence now and unlocks exactly at its anniversary", async () => {
  const bucket = new MemoryR2();
  let now = Date.parse("2026-08-25T16:00:00Z");
  const options = { bucket, key: "continuity/member", loadMembership: async () => active(1), now: () => now };
  const first = await reconcileMembershipContinuity(options);
  assert.deepEqual(first.access, { allowed: false, since: iso(now), eligible_at: "2026-10-25T16:00:00.000Z", reason: "needs_history_verification" });
  now = Date.parse(first.access.eligible_at) - 1;
  assert.equal((await reconcileMembershipContinuity(options)).access.allowed, false);
  now += 1;
  assert.equal((await reconcileMembershipContinuity(options)).access.allowed, true);
  assert.equal(bucket.rows.size, 2, "ordinary reads do not rewrite evidence or audit events");
});

test("linked renewals preserve continuity but lapse and revoke/regrant reset it", async () => {
  const bucket = new MemoryR2();
  let now = Date.parse("2026-01-01T00:00:00Z");
  let membership = active(1, "2026-02-01T00:00:00Z");
  const options = { bucket, key: "continuity/member", loadMembership: async () => membership, now: () => now };
  const first = await reconcileMembershipContinuity({ ...options, transition: { before: inactive(0), after: membership } });
  assert.equal(first.record.evidence, "issued");
  const before = membership;
  now = Date.parse("2026-01-31T00:00:00Z");
  membership = active(2, "2026-03-01T00:00:00Z");
  assert.equal((await reconcileMembershipContinuity({ ...options, transition: { before, after: membership } })).record.since, first.record.since);
  now = Date.parse("2026-03-01T00:00:00.001Z");
  const expired = membership;
  membership = active(3, "2026-04-01T00:00:00Z");
  const lapsed = await reconcileMembershipContinuity({ ...options, transition: { before: expired, after: membership } });
  assert.equal(lapsed.record.since, iso(now));
  const beforeRevoke = membership;
  membership = inactive(4);
  const revoked = await reconcileMembershipContinuity({ ...options, transition: { before: beforeRevoke, after: membership } });
  assert.equal(revoked.record.since, null);
  now += 1000;
  const beforeRegrant = membership;
  membership = active(5);
  assert.equal((await reconcileMembershipContinuity({ ...options, transition: { before: beforeRegrant, after: membership } })).record.since, iso(now));
});

test("a missed hook or stale hook cannot bridge an unobserved revoke and regrant", async () => {
  const bucket = new MemoryR2();
  let now = Date.parse("2026-01-01T00:00:00Z");
  let membership = active(1);
  const options = { bucket, key: "continuity/member", loadMembership: async () => membership, now: () => now };
  await reconcileMembershipContinuity(options);
  now = Date.parse("2026-04-01T00:00:00Z");
  membership = active(3);
  const result = await reconcileMembershipContinuity({ ...options, transition: { before: active(1), after: inactive(2) } });
  assert.equal(result.record.since, iso(now));
  assert.equal(result.access.allowed, false);
});

test("admin verification requires a valid dated assertion and durable audit before access", async () => {
  const bucket = new MemoryR2();
  const now = Date.parse("2026-10-25T00:00:00Z");
  const membership = active(1);
  for (const invalid of [
    { since: "2026-11-01", audit_reason: "checked original ledger" },
    { since: "2026-02-30", audit_reason: "checked original ledger" },
    { since: "2026-02-30T00:00:00Z", audit_reason: "checked original ledger" },
    { since: "2026-01-01T00:00:00", audit_reason: "checked original ledger" },
    { since: "2026-01-01", audit_reason: "" },
  ]) assert.throws(() => validateContinuityVerification({ ...invalid, actor: "administrator" }, now));
  const verification = { ...validateContinuityVerification({ since: "2026-08-01", audit_reason: "Checked uninterrupted payment ledger", actor: "administrator" }, now), fingerprint: membership.fingerprint };
  const options = { bucket, key: "continuity/member", loadMembership: async () => membership, now: () => now, verification };
  bucket.failPrefix = "continuity/member/events/";
  await assert.rejects(reconcileMembershipContinuity(options));
  assert.equal(bucket.json("continuity/member"), null);
  bucket.failPrefix = "";
  const result = await reconcileMembershipContinuity(options);
  assert.equal(result.access.allowed, true);
  assert.equal(result.record.evidence, "verified");
  const audit = bucket.json(`continuity/member/events/${result.record.revision}.json`);
  assert.equal(audit.audit_reason, verification.audit_reason);
  assert.equal(audit.actor, "administrator");
  assert.deepEqual(Object.keys(result.access).sort(), ["allowed", "eligible_at", "reason", "since"]);
  bucket.conflictKey = "continuity/member";
  await assert.rejects(reconcileMembershipContinuity(options), { code: "CONTINUITY_CONFLICT" });
});

test("concurrent first observations converge and corrupt evidence never authorizes", async () => {
  const bucket = new MemoryR2();
  const options = { bucket, key: "continuity/member", loadMembership: async () => active(1), now: () => Date.parse("2026-01-01T00:00:00Z") };
  const results = await Promise.all([reconcileMembershipContinuity(options), reconcileMembershipContinuity(options)]);
  assert.equal(results[0].record.revision, results[1].record.revision);
  bucket.seed(options.key, { ...results[0].record, since: "1900-01-01", authority_fingerprint: "wrong" });
  await assert.rejects(reconcileMembershipContinuity(options));
});

const member = { id: "member-id", username: "member", email: "member@example.com" };
const admin = { id: "admin-id", username: "admin-a", email: "admin-a@users.portal.example.invalid" };
const key = (...parts) => ["_account", ...parts.map(encodeURIComponent)].join("/");
const continuityKey = key("membership-continuity", "v1", member.email);

function fixture(t, at = "2026-10-25T00:00:00Z") {
  t.mock.timers.enable({ apis: ["Date"], now: new Date(at) });
  const bucket = new MemoryR2();
  for (const identity of [member, admin]) {
    const user = { ...identity, password_salt: "salt", password_hash: `hmac_sha256$${"a".repeat(64)}`, email_is_generated: false, created_at: "2020-01-01T00:00:00Z", updated_at: "2020-01-01T00:00:00Z" };
    for (const field of ["id", "username", "email"]) bucket.seed(key("users", field, user[field]), user);
  }
  return { bucket, env: { REPORT_BUCKET: bucket, ACCOUNT_STORE_MODE: "r2", MASTER_KEY: "fixture-master", PASSWORD_SECRET: "fixture-password", ALLOWED_ORIGIN: "https://portal.example.invalid", PADDLE_WEBHOOK_SECRET: "fixture-paddle", PADDLE_PRICE_YEARLY: "pri_annual_fixture" } };
}

function token(user) {
  const body = Buffer.from(JSON.stringify({ kind: "user", sub: user.id, username: user.username, email: user.email, session_epoch: "", iat: Math.floor(Date.now() / 1000), exp: Math.floor(Date.now() / 1000) + 3600 })).toString("base64url");
  return `${body}.${createHmac("sha256", "fixture-password").update(`portal:account-token:v1:${body}`).digest("base64url")}`;
}

async function request(env, pathname, { user = member, body, headers = {} } = {}) {
  const response = await worker.fetch(new Request(`https://worker.test${pathname}`, {
    method: body ? "POST" : "GET", headers: { ...(user ? { Authorization: `Bearer ${token(user)}` } : {}), "content-type": "application/json", Origin: "https://portal.example.invalid", ...headers },
    ...(body ? { body: JSON.stringify(body) } : {}),
  }), env, { waitUntil() {} });
  return { response, data: await response.json() };
}

function seedGrant(bucket, changes = {}) {
  const row = { id: "grant-id", email: member.email, access_mode: "all", status: "active", lifetime: false, current_period_end: "2027-12-31T00:00:00Z", duration_value: "12", download_limit: 0, download_count: 0, download_items: [], institutions: [], industries: [], page_ranges: [], created_at: "2020-01-01T00:00:00Z", updated_at: "2026-01-01T00:00:00Z", change_id: "initial-grant", ...changes };
  bucket.seed(key("access", member.email), row);
  return row;
}

function seedEntitlement(bucket, changes = {}) {
  const row = { id: "entitlement-id", email: member.email, plan: "annual", status: "active", lifetime: false, current_period_end: "2027-12-31T00:00:00Z", created_at: "2020-01-01T00:00:00Z", updated_at: "2026-01-01T00:00:00Z", ...changes };
  bucket.seed(key("entitlements", member.email), row);
  return row;
}

async function verify(env, since = "2026-08-01") {
  return request(env, "/account-admin/user-access", { user: admin, body: { action: "verify_membership_continuity", email: member.email, since, audit_reason: "Verified uninterrupted membership receipts" } });
}

function seedUserState(bucket, changes = {}) {
  const row = { user_id: member.id, email: member.email, disabled: false, updated_at: "2026-08-01T00:00:00Z", ...changes };
  for (const field of ["id", "email"]) bucket.seed(key("user-state", field, member[field]), row);
  return row;
}

async function loginAfterPasswordReset(env) {
  const captcha = await request(env, "/captcha", { user: null });
  assert.equal(captcha.response.status, 200);
  const svg = Buffer.from(captcha.data.image.split(",", 2)[1], "base64").toString("utf8");
  const equation = svg.match(/>(\d+) \+ (\d+) = \?</u);
  assert.ok(equation);
  const login = await request(env, "/auth", { user: null, body: {
    action: "login", username: member.username, password: "123456",
    captcha_token: captcha.data.token, captcha_answer: String(Number(equation[1]) + Number(equation[2])),
  } });
  assert.equal(login.response.status, 200);
  assert.ok(login.data.token);
  return { Authorization: `Bearer ${login.data.token}` };
}

async function grant(env, bucket, changes = {}) {
  const existing = bucket.json(key("access", member.email));
  return request(env, "/account-admin/user-access", { user: admin, body: { email: member.email, access_mode: "all", duration_months: "12", institutions: [], industries: [], page_ranges: [], confirm_scope_change: true, expected_change_id: existing?.change_id || "", expected_updated_at: existing?.updated_at || "", ...changes } });
}

test("full access is private, account age is insufficient, and only the existing super-admin path can attest history", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket);
  const anonymous = await request(env, "/course/full/access", { user: null });
  assert.equal(anonymous.response.status, 401);
  assert.equal(bucket.json(continuityKey), null);
  const legacy = await request(env, "/course/full/access");
  assert.equal(legacy.response.status, 200);
  assert.equal(legacy.data.reason, "needs_history_verification");
  assert.equal(legacy.data.allowed, false);
  assert.match(legacy.response.headers.get("cache-control"), /private.*no-store/u);
  const unprivileged = await request(env, "/account-admin/user-access", { body: { action: "verify_membership_continuity", email: member.email, since: "2020-01-01", audit_reason: "Self asserted history" } });
  assert.equal(unprivileged.response.status, 403);
  const verified = await verify(env);
  assert.equal(verified.response.status, 200, JSON.stringify(verified.data));
  assert.equal(verified.data.membership_continuity.allowed, true);
  const full = await request(env, "/course/full/access");
  assert.deepEqual(Object.keys(full.data).sort(), ["allowed", "eligible_at", "reason", "since"]);
  assert.equal(full.data.since, "2026-07-31T16:00:00.000Z");
  assert.equal(full.data.allowed, true);
  assert.equal(bucket.json(key("access", member.email)).change_id, "initial-grant", "verification does not change ordinary access");
});

for (const stateKind of ["missing", "legacy", "versioned"]) {
  for (const action of ["enable_noop", "password_reset"]) {
    test(`${stateKind} state ${action} preserves verified tenure, but subsequent disable/re-enable resets it`, async (t) => {
      const { bucket, env } = fixture(t);
      seedGrant(bucket);
      if (stateKind !== "missing") seedUserState(bucket, stateKind === "versioned" ? { membership_change_id: "fixture-existing-version" } : {});
      assert.equal((await verify(env)).response.status, 200);
      const before = bucket.json(continuityKey);
      t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
      const edited = action === "enable_noop"
        ? await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })
        : await request(env, "/account-admin/user-password-reset", { user: admin, body: { email: member.email, confirm_reset: true } });
      assert.equal(edited.response.status, 200);
      const state = bucket.json(key("user-state", "email", member.email));
      assert.ok(state.membership_change_id);
      assert.equal(bucket.json(key("user-state", "id", member.id)).membership_change_id, state.membership_change_id);
      const after = bucket.json(continuityKey);
      assert.equal(after.since, before.since);
      assert.equal(after.evidence, "verified");
      if (stateKind === "versioned") {
        assert.equal(state.membership_change_id, "fixture-existing-version");
        assert.equal(after.revision, before.revision);
      } else {
        assert.notEqual(after.authority_fingerprint, before.authority_fingerprint);
        const audit = bucket.json(`${continuityKey}/events/${after.revision}.json`);
        assert.equal(audit.previous_revision, before.revision);
        assert.equal(audit.audit_reason, "account_state_version_initialized");
      }
      let headers = {};
      if (action === "password_reset") {
        assert.equal((await request(env, "/course/full/access")).response.status, 401, "the old session epoch is rejected");
        headers = await loginAfterPasswordReset(env);
      }
      const access = await request(env, "/course/full/access", { headers });
      assert.equal(access.response.status, 200);
      assert.equal(access.data.allowed, true);
      assert.equal(access.data.since, before.since);

      assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: true } })).response.status, 200);
      const disabled = bucket.json(key("user-state", "email", member.email));
      assert.notEqual(disabled.membership_change_id, state.membership_change_id);
      assert.equal(bucket.json(continuityKey).since, null);
      assert.equal((await request(env, "/course/full/access", { headers })).response.status, 401);
      t.mock.timers.setTime(Date.parse("2026-10-26T00:00:01Z"));
      assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })).response.status, 200);
      assert.notEqual(bucket.json(key("user-state", "email", member.email)).membership_change_id, disabled.membership_change_id);
      const reenabled = await request(env, "/course/full/access", { headers });
      assert.equal(reenabled.response.status, 200);
      assert.equal(reenabled.data.allowed, false);
      assert.equal(reenabled.data.since, "2026-10-26T00:00:01.000Z");
    });
  }
}

test("legacy migration cannot retain an already unmatched authority fingerprint", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket);
  seedUserState(bucket);
  assert.equal((await verify(env)).response.status, 200);
  // Simulate a prior status transition whose continuity hook was missed.
  seedUserState(bucket, { updated_at: "2026-10-25T00:00:00Z" });
  t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
  assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })).response.status, 200);
  const access = await request(env, "/course/full/access");
  assert.equal(access.data.allowed, false);
  assert.equal(access.data.since, "2026-10-26T00:00:00.000Z");
  assert.equal(bucket.json(continuityKey).evidence, "observed");
});

test("failed migration cannot preserve stale tenure or block a primary account disablement", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket);
  seedUserState(bucket);
  assert.equal((await verify(env)).response.status, 200);
  const before = bucket.json(continuityKey);
  t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
  bucket.failPrefix = continuityKey;
  assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })).response.status, 200);
  assert.ok(bucket.json(key("user-state", "email", member.email)).membership_change_id);
  assert.equal(bucket.json(continuityKey).revision, before.revision);
  bucket.failPrefix = "";
  const observed = await request(env, "/course/full/access");
  assert.equal(observed.data.allowed, false);
  assert.equal(observed.data.since, "2026-10-26T00:00:00.000Z");
  bucket.failPrefix = continuityKey;
  assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: true } })).response.status, 200);
  assert.equal(bucket.json(key("user-state", "email", member.email)).disabled, true);
  assert.equal((await request(env, "/course/full/access")).response.status, 401);
});

test("new grants are tracked at issuance, renewal retains tenure, narrowing and lapse reset it", async (t) => {
  const { bucket, env } = fixture(t, "2026-01-01T00:00:00Z");
  const created = await grant(env, bucket, { duration_months: "3" });
  assert.equal(created.response.status, 200, JSON.stringify(created.data));
  assert.equal(created.data.durability.continuity_saved, true);
  const since = bucket.json(continuityKey).since;
  t.mock.timers.setTime(Date.parse("2026-03-01T00:00:00Z"));
  assert.equal((await request(env, "/course/full/access")).data.allowed, true);
  const renewed = await grant(env, bucket, { duration_months: "3", renew: true });
  assert.equal(renewed.response.status, 200);
  assert.equal(bucket.json(continuityKey).since, since);
  const narrowed = await grant(env, bucket, { access_mode: "filters", institutions: ["Example Bank"], duration_months: "3" });
  assert.equal(narrowed.response.status, 200);
  assert.equal(bucket.json(continuityKey).since, null);
  t.mock.timers.setTime(Date.parse("2026-03-02T00:00:00Z"));
  assert.equal((await grant(env, bucket, { duration_months: "1" })).response.status, 200);
  assert.equal(bucket.json(continuityKey).since, "2026-03-02T00:00:00.000Z");
  t.mock.timers.setTime(Date.parse("2026-05-03T00:00:00Z"));
  assert.equal((await grant(env, bucket, { duration_months: "12", renew: true })).response.status, 200);
  assert.equal(bucket.json(continuityKey).since, "2026-05-03T00:00:00.000Z");
});

test("failed continuity storage cannot stop a revocation or silently restore earlier tenure", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  bucket.failPrefix = continuityKey;
  const revoked = await grant(env, bucket, { access_mode: "none" });
  assert.equal(revoked.response.status, 200);
  assert.equal(revoked.data.durability.continuity_saved, false);
  assert.equal(bucket.json(key("access", member.email)).status, "inactive");
  const whileUnavailable = await request(env, "/course/full/access");
  assert.equal(whileUnavailable.data.allowed, false);
  assert.equal(whileUnavailable.response.status, 503);
  bucket.failPrefix = "";
  assert.equal((await grant(env, bucket)).response.status, 200);
  assert.equal((await request(env, "/course/full/access")).data.allowed, false);
  assert.equal(bucket.json(continuityKey).since, new Date().toISOString());
});

test("limits, trials and account disablement cannot use full-course history", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket, { duration_value: "trial_3d", download_limit: 10 });
  assert.equal((await request(env, "/course/full/access")).data.allowed, false);
  assert.equal((await verify(env)).response.status, 400);
  seedGrant(bucket, { access_mode: "filters", institutions: ["Example"] });
  assert.equal((await verify(env)).response.status, 400);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: true } })).response.status, 200);
  assert.equal((await request(env, "/course/full/access")).data.allowed, false);
  assert.equal(bucket.json(continuityKey).active, false);
  t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
  assert.equal((await request(env, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })).response.status, 200);
  const enabled = await request(env, "/course/full/access");
  assert.equal(enabled.data.allowed, false);
  assert.equal(enabled.data.since, "2026-10-26T00:00:00.000Z");
});

async function paddleEvent(env, { type = "subscription.canceled", eventId = "a", end = "2027-12-31T00:00:00Z" } = {}) {
  const body = { event_id: `evt_${eventId.repeat(26)}`, occurred_at: new Date().toISOString(), event_type: type, data: { id: `sub_${"s".repeat(26)}`, customer_id: `ctm_${"c".repeat(26)}`, status: type === "subscription.canceled" ? "canceled" : "active", current_billing_period: { starts_at: new Date().toISOString(), ends_at: end }, items: [{ price: { id: "pri_annual_fixture" } }] } };
  const timestamp = String(Math.floor(Date.now() / 1000));
  const signature = createHmac("sha256", env.PADDLE_WEBHOOK_SECRET).update(`${timestamp}:${JSON.stringify(body)}`).digest("hex");
  const response = await internal.handlePaddleWebhook(new Request("https://worker.test/paddle-webhook", {
    method: "POST", headers: { "Paddle-Signature": `ts=${timestamp};h1=${signature}` }, body: JSON.stringify(body),
  }), env);
  return { response, data: await response.json() };
}

test("Paddle revocation preserves independently active admin coverage and renewal preserves remaining coverage", async (t) => {
  const { bucket, env } = fixture(t);
  seedGrant(bucket);
  const entitlement = seedEntitlement(bucket, { paddle_customer_id: `ctm_${"c".repeat(26)}`, paddle_subscription_id: `sub_${"s".repeat(26)}` });
  bucket.seed(key("paddle_binding", "customer", entitlement.paddle_customer_id), entitlement);
  assert.equal((await verify(env)).response.status, 200);
  const since = bucket.json(continuityKey).since;
  const canceled = await paddleEvent(env);
  assert.equal(canceled.response.status, 200, JSON.stringify(canceled.data));
  assert.equal(canceled.data.processed, true);
  assert.equal(bucket.json(continuityKey).since, since);
  assert.equal((await request(env, "/course/full/access")).data.allowed, true);
  t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
  const resumed = await paddleEvent(env, { type: "subscription.resumed", eventId: "b" });
  assert.equal(resumed.data.processed, true, JSON.stringify(resumed.data));
  assert.equal(bucket.json(continuityKey).since, since);
  const duplicate = await paddleEvent(env, { type: "subscription.resumed", eventId: "b" });
  assert.equal(duplicate.data.processed, false);
  assert.equal(bucket.json(continuityKey).since, since);
});

test("sole Paddle membership revoked then resumed starts a fresh continuous interval", async (t) => {
  const { bucket, env } = fixture(t);
  const entitlement = seedEntitlement(bucket, { paddle_customer_id: `ctm_${"c".repeat(26)}`, paddle_subscription_id: `sub_${"s".repeat(26)}` });
  bucket.seed(key("paddle_binding", "customer", entitlement.paddle_customer_id), entitlement);
  assert.equal((await verify(env)).response.status, 200);
  assert.equal((await paddleEvent(env)).data.processed, true);
  assert.equal(bucket.json(continuityKey).active, false);
  t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00Z"));
  assert.equal((await paddleEvent(env, { type: "subscription.resumed", eventId: "b" })).data.processed, true);
  const result = await request(env, "/course/full/access");
  assert.equal(result.data.allowed, false);
  assert.equal(result.data.since, "2026-10-26T00:00:00.000Z");
});

function seedGrantAudit(bucket, row, overrides = {}) {
  const suffix = `${row.updated_at}-${row.change_id}`.replace(/[^0-9A-Za-z_-]+/gu, "-");
  const audit = {
    type: "user_access_update", email: member.email, updated_at: row.updated_at,
    next: { ...row, active: true }, ...overrides,
  };
  bucket.seed(key("access_audit", member.email, suffix), audit);
}

test("an exact current immutable grant audit proves a conservative legacy starting date", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(bucket, row);
  const recovered = await request(env, "/course/full/access");
  assert.equal(recovered.data.allowed, true);
  assert.equal(recovered.data.since, row.updated_at.replace("Z", ".000Z"));
  const record = bucket.json(continuityKey);
  assert.equal(record.evidence, "verified");
  assert.equal(bucket.json(`${continuityKey}/events/${record.revision}.json`).type, "membership_history_recovered");
  // Recovery is initial-only: later changes to historical material cannot
  // overwrite a continuity record already being tracked.
  seedGrantAudit(bucket, row, { updated_at: "2020-01-01T00:00:00Z" });
  assert.equal((await request(env, "/course/full/access")).data.since, recovered.data.since);
});

test("legacy tenure is recovered before the first renewal or no-op account-state migration", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(bucket, row);
  assert.equal(bucket.json(continuityKey), null);
  assert.equal((await grant(env, bucket, { renew: true })).response.status, 200);
  const renewed = await request(env, "/course/full/access");
  assert.equal(renewed.data.allowed, true);
  assert.equal(renewed.data.since, "2026-08-01T00:00:00.000Z");

  const other = new MemoryR2();
  for (const [storageKey, value] of bucket.rows) if (storageKey.startsWith("_account/users/")) other.rows.set(storageKey, value);
  const legacy = seedGrant(other, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(other, legacy);
  const otherEnv = { ...env, REPORT_BUCKET: other };
  assert.equal((await request(otherEnv, "/account-admin/user-status", { user: admin, body: { email: member.email, disabled: false } })).response.status, 200);
  const migrated = await request(otherEnv, "/course/full/access");
  assert.equal(migrated.data.allowed, true);
  assert.equal(migrated.data.since, "2026-08-01T00:00:00.000Z");

  const resetBucket = new MemoryR2();
  for (const [storageKey, value] of bucket.rows) if (storageKey.startsWith("_account/users/")) resetBucket.rows.set(storageKey, value);
  const resetLegacy = seedGrant(resetBucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(resetBucket, resetLegacy);
  const resetEnv = { ...env, REPORT_BUCKET: resetBucket };
  assert.equal((await request(resetEnv, "/account-admin/user-password-reset", { user: admin, body: { email: member.email, confirm_reset: true } })).response.status, 200);
  const headers = await loginAfterPasswordReset(resetEnv);
  const reset = await request(resetEnv, "/course/full/access", { headers });
  assert.equal(reset.data.allowed, true);
  assert.equal(reset.data.since, "2026-08-01T00:00:00.000Z");
});

function seedRenewalChain(bucket, changes = {}) {
  const oldest = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z", change_id: "august", current_period_end: "2026-09-02T00:00:00Z", ...changes.oldest });
  const previous = { ...oldest, updated_at: "2026-09-01T00:00:00Z", change_id: "september", current_period_end: "2026-10-02T00:00:00Z", ...changes.previous };
  const current = seedGrant(bucket, { updated_at: "2026-10-01T00:00:00Z", change_id: "october" });
  seedGrantAudit(bucket, oldest);
  if (!changes.missingPrevious) seedGrantAudit(bucket, previous, { previous: { ...oldest, active: true }, ...changes.previousAudit });
  seedGrantAudit(bucket, current, { previous: { ...previous, active: true, ...changes.previousLink } });
  return { current, previous, oldest };
}

test("exact uninterrupted legacy renewal audits recover tenure and stop once two months are proven", async (t) => {
  const { bucket, env } = fixture(t);
  const { oldest } = seedRenewalChain(bucket);
  // An older predecessor is deliberately absent: eligible evidence is enough.
  seedGrantAudit(bucket, oldest, { previous: { ...oldest, updated_at: "2026-07-01T00:00:00Z", change_id: "unneeded-july", active: true } });
  const result = await request(env, "/course/full/access");
  assert.equal(result.data.allowed, true);
  assert.equal(result.data.since, "2026-08-01T00:00:00.000Z");
  assert.equal(bucket.reads.filter((storageKey) => storageKey.startsWith("_account/access_audit/")).length, 3);
});

test("missing, tampered, inactive or gapped legacy links cannot extend the verified lower bound", async (t) => {
  const { env } = fixture(t);
  for (const changes of [
    { missingPrevious: true },
    { previousAudit: { email: "different@example.com" } },
    { previousAudit: { next: { ...member, active: true } } },
    { previousLink: { note: "tampered snapshot" } },
    { previousLink: { active: false } },
    { previousLink: { access_mode: "filters" } },
    { previousLink: { download_limit: 10 } },
    { previousLink: { duration_value: "trial_3d" } },
    { previous: { current_period_end: "2026-09-30T23:59:59Z" } },
    { previous: { updated_at: "2026-10-02T00:00:00Z" } },
  ]) {
    const bucket = new MemoryR2();
    for (const [storageKey, value] of env.REPORT_BUCKET.rows) if (storageKey.startsWith("_account/users/")) bucket.rows.set(storageKey, value);
    seedRenewalChain(bucket, changes);
    const result = await request({ ...env, REPORT_BUCKET: bucket }, "/course/full/access");
    assert.equal(result.data.allowed, false, JSON.stringify(changes));
    assert.equal(result.data.since, "2026-10-01T00:00:00.000Z", JSON.stringify(changes));
  }
});

test("legacy renewal recovery stops at an account-state boundary and is bounded to 24 audits", async (t) => {
  const { bucket, env } = fixture(t);
  seedRenewalChain(bucket);
  seedUserState(bucket, { updated_at: "2026-09-15T00:00:00Z" });
  const limited = await request(env, "/course/full/access");
  assert.equal(limited.data.allowed, false);
  assert.equal(limited.data.since, "2026-09-15T00:00:00.000Z");

  const other = new MemoryR2();
  for (const [storageKey, value] of bucket.rows) if (storageKey.startsWith("_account/users/")) other.rows.set(storageKey, value);
  let previous;
  for (let day = 1; day <= 25; day += 1) {
    const current = seedGrant(other, { updated_at: `2026-10-${String(day).padStart(2, "0")}T00:00:00Z`, change_id: `daily-${day}` });
    seedGrantAudit(other, current, previous ? { previous: { ...previous, active: true } } : {});
    previous = current;
  }
  const bounded = await request({ ...env, REPORT_BUCKET: other }, "/course/full/access");
  assert.equal(bounded.data.allowed, false);
  assert.equal(bounded.data.since, "2026-10-02T00:00:00.000Z");
  assert.equal(other.reads.filter((storageKey) => storageKey.startsWith("_account/access_audit/")).length, 24);
});

test("failed first legacy recovery cannot block a primary revocation", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(bucket, row);
  bucket.failPrefix = continuityKey;
  const revoked = await grant(env, bucket, { access_mode: "none" });
  assert.equal(revoked.response.status, 200);
  assert.equal(revoked.data.durability.continuity_saved, false);
  assert.equal(bucket.json(key("access", member.email)).status, "inactive");
  assert.equal(bucket.json(continuityKey), null);
});

test("mismatched audit and newly renewed grants never borrow the earlier account age", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(bucket, row, { next: { ...row, access_mode: "filters", active: true } });
  assert.equal((await request(env, "/course/full/access")).data.reason, "needs_history_verification");
  const other = new MemoryR2();
  for (const [storageKey, value] of bucket.rows) if (storageKey.startsWith("_account/users/")) other.rows.set(storageKey, value);
  const renewed = seedGrant(other, { updated_at: "2026-10-01T00:00:00Z", change_id: "renewed" });
  seedGrantAudit(other, renewed);
  const result = await request({ ...env, REPORT_BUCKET: other }, "/course/full/access");
  assert.equal(result.data.allowed, false);
  assert.equal(result.data.since, "2026-10-01T00:00:00.000Z");
});

test("legacy inference stops at a more recent account status transition", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-08-01T00:00:00Z" });
  seedGrantAudit(bucket, row);
  bucket.seed(key("user-state", "id", member.id), { user_id: member.id, email: member.email, disabled: false, updated_at: "2026-10-01T00:00:00Z" });
  const result = await request(env, "/course/full/access");
  assert.equal(result.data.allowed, false);
  assert.equal(result.data.since, "2026-10-01T00:00:00.000Z");
});

test("an expired audited grant cannot lend its history to a newer unrelated entitlement", async (t) => {
  const { bucket, env } = fixture(t);
  const row = seedGrant(bucket, { updated_at: "2026-01-01T00:00:00Z", current_period_end: "2026-04-01T00:00:00Z" });
  seedGrantAudit(bucket, row);
  seedEntitlement(bucket, { updated_at: "2026-10-24T00:00:00Z", paddle_last_event_id: `evt_${"b".repeat(26)}`, paddle_last_occurred_at: "2026-10-24T00:00:00Z" });
  const result = await request(env, "/course/full/access");
  assert.equal(result.data.allowed, false);
  assert.equal(result.data.reason, "needs_history_verification");
  assert.equal(result.data.since, "2026-10-25T00:00:00.000Z");
});

test("legacy gift issuance and uninterrupted renewal use the continuity hook without reopening payment routes", async (t) => {
  const { bucket, env } = fixture(t, "2026-01-01T00:00:00Z");
  await internal.applyVid2PptGift(env, { email: member.email, planCode: "NOVA-Q", requestId: "gift-1", completedAt: new Date().toISOString() });
  const since = bucket.json(continuityKey).since;
  assert.equal(bucket.json(continuityKey).evidence, "issued");
  t.mock.timers.setTime(Date.parse("2026-03-01T00:00:00Z"));
  await internal.applyVid2PptGift(env, { email: member.email, planCode: "NOVA-Q", requestId: "gift-2", completedAt: new Date().toISOString() });
  assert.equal(bucket.json(continuityKey).since, since);
  assert.equal((await request(env, "/course/full/access")).data.allowed, true);
  assert.equal((await request(env, "/paddle-webhook", { user: null, body: {} })).response.status, 410);
});

const fullDirectoryKey = "_course-directory/full-v1/directory.json";
function seedFullDirectory(bucket) {
  const items = [
    { id: "full-file-01", name: "Wall Street Prep 原始名称 & <案例>.pdf", folders: ["WSP 原始目录", "建模"], extension: "pdf", size_label: "1 MB", date: "2026-08-01" },
    { id: "full-file-02", name: "第二讲 财务预测.mp4", folders: ["WSP 原始目录", "建模"], extension: "mp4", size_label: "2 GB", date: "" },
    { id: "full-file-03", name: "法律案例.zip", folders: ["法规课程"], extension: "zip", size_label: "3 MB", date: "" },
  ];
  bucket.seed(fullDirectoryKey, { schema_version: 1, variant: "original_names", complete: true, item_count: items.length, generated_at: "2026-10-25T00:00:00Z", items });
  return items;
}

test("original directory gate runs before private metadata reads and rejects sanitized fallback", async (t) => {
  const { bucket, env } = fixture(t);
  seedFullDirectory(bucket);
  seedGrant(bucket);
  for (const options of [{ user: null }, {}]) {
    bucket.reads.length = 0;
    const denied = await request(env, "/course/full/directory", options);
    assert.ok([401, 403].includes(denied.response.status));
    assert.equal(denied.data.items, undefined);
    assert.equal(bucket.reads.includes(fullDirectoryKey), false);
  }
  assert.equal((await verify(env)).response.status, 200);
  bucket.rows.delete(fullDirectoryKey);
  bucket.seed("_course-directory/v1/directory.json", { items: [{ name: "sanitized fallback forbidden" }] });
  const unavailable = await request(env, "/course/full/directory");
  assert.equal(unavailable.response.status, 503);
  assert.equal(unavailable.data.items, undefined);
  assert.equal(bucket.reads.includes("_course-directory/v1/directory.json"), false);
});

test("original filenames and nested labels remain intact with bounded search/filter/pagination", async (t) => {
  const { bucket, env } = fixture(t);
  const items = seedFullDirectory(bucket);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  const first = await request(env, "/course/full/directory?page_size=1");
  assert.equal(first.response.status, 200);
  assert.deepEqual(first.data.items, [items[0]]);
  assert.equal(first.data.total, 3);
  assert.equal(first.data.has_more, true);
  assert.match(first.response.headers.get("cache-control"), /private.*no-store/u);
  assert.deepEqual(first.data.facets.file_types.map((item) => item.name), ["archive", "pdf", "video"]);
  const filtered = await request(env, `/course/full/directory?q=${encodeURIComponent("财务 建模")}&folder=${encodeURIComponent("WSP 原始目录")}&file_type=video`);
  assert.deepEqual(filtered.data.items, [items[1]]);
  const capped = await request(env, "/course/full/directory?page_size=99999");
  assert.equal(capped.data.page_size, 100);
  assert.equal(bucket.reads.filter((key) => key === fullDirectoryKey).length, 1, "private parsed catalog cached independently of permission checks");
  assert.equal((await grant(env, bucket, { access_mode: "none" })).response.status, 200);
  const revoked = await request(env, "/course/full/directory");
  assert.equal(revoked.response.status, 403);
  assert.equal(revoked.data.items, undefined);
});

test("full-directory Request uses canonical private names, fixed owner, bilingual acknowledgement and 24h dedupe", async (t) => {
  const { bucket, env } = fixture(t);
  env.BREVO_API_KEY = "fixture-brevo";
  const items = seedFullDirectory(bucket);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  const sent = [];
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (url, init) => {
    assert.equal(String(url), "https://api.brevo.com/v3/smtp/email");
    sent.push(JSON.parse(init.body));
    return new Response(JSON.stringify({ messageId: `message-${sent.length}` }), { status: 201 });
  };
  const submit = (changes = {}) => request(env, "/course/full/directory-request", { body: {
    directory_item_id: items[0].id, resource_title: "forged title", requester_email: "attacker@example.net", recipient: "attacker@example.net", page_path: "/course-full.html?secret=discarded", ...changes,
  } });
  try {
    const [first, concurrent] = await Promise.all([submit(), submit()]);
    assert.equal(first.response.status, 202);
    assert.equal(concurrent.response.status, 202);
    assert.equal(sent.length, 2);
    const owner = sent.find((item) => item.tags.includes("portal-course-full-directory-request"));
    const ack = sent.find((item) => item.tags.includes("portal-form-acknowledgement"));
    assert.deepEqual(owner.to, [{ email: "info@kcdesk.com" }]);
    assert.ok(owner.textContent.includes(items[0].name));
    assert.ok(owner.htmlContent.includes("&lt;案例&gt;"));
    assert.doesNotMatch(JSON.stringify(owner), /forged title|attacker@example|secret=discarded/u);
    assertAcknowledgement(ack, member.email);
    assert.equal((await submit()).data.deduplicated, true);
    assert.equal(sent.length, 2);
    assert.equal((await submit({ directory_item_id: "full-file-99" })).response.status, 404);
    assert.equal((await request(env, "/course/full/directory-request", { headers: { Origin: "https://attacker.example" }, body: { directory_item_id: items[0].id } })).response.status, 403);
    const records = [...bucket.rows.keys()].filter((key) => key.startsWith("_course-full-directory-requests/v1/items/"));
    assert.equal(records.length, 1);
    assert.equal(bucket.json(records[0]).resource_title, items[0].name);
    assert.equal(bucket.json(records[0]).page_path, "/course-full.html");
    for (const [storageKey, value] of bucket.rows) {
      if (storageKey.includes("analytics")) assert.equal(value.text.includes(items[0].name), false, "raw names stay out of analytics");
    }
    t.mock.timers.setTime(Date.parse("2026-10-26T00:00:00.001Z"));
    assert.equal((await submit()).data.deduplicated, false);
    assert.equal(sent.length, 4);
    assert.equal((await grant(env, bucket, { access_mode: "none" })).response.status, 200);
    assert.equal((await submit()).response.status, 403, "dedupe never bypasses current eligibility");
    assert.equal(sent.length, 4);
  } finally { globalThis.fetch = originalFetch; }
});

test("full-directory Request retries failed owner notification and survives acknowledgement failure", async (t) => {
  const { bucket, env } = fixture(t);
  env.BREVO_API_KEY = "fixture-brevo";
  seedFullDirectory(bucket);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  const sent = [];
  const originalFetch = globalThis.fetch;
  let ownerFails = true;
  globalThis.fetch = async (_url, init) => {
    const message = JSON.parse(init.body);
    sent.push(message);
    const fail = message.tags.includes("portal-form-acknowledgement") || ownerFails;
    return new Response(JSON.stringify(fail ? { message: "temporary failure" } : { messageId: "accepted" }), { status: fail ? 503 : 201 });
  };
  try {
    const submit = () => request(env, "/course/full/directory-request", { body: { directory_item_id: "full-file-01" } });
    assert.equal((await submit()).response.status, 502);
    assert.equal(sent.length, 1);
    ownerFails = false;
    assert.equal((await submit()).response.status, 202);
    assert.equal(sent.length, 3);
    assert.equal((await submit()).data.deduplicated, true);
    assert.equal(sent.length, 3);
  } finally { globalThis.fetch = originalFetch; }
});

test("legacy generated accounts provide a real reply email while dedupe remains bound to the account", async (t) => {
  const { bucket, env } = fixture(t);
  env.BREVO_API_KEY = "fixture-brevo";
  seedFullDirectory(bucket);
  seedGrant(bucket);
  assert.equal((await verify(env)).response.status, 200);
  for (const field of ["id", "username", "email"]) {
    const userKey = key("users", field, member[field]);
    bucket.seed(userKey, { ...bucket.json(userKey), email_is_generated: true });
  }
  const sent = [];
  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (_url, init) => {
    sent.push(JSON.parse(init.body));
    return new Response(JSON.stringify({ messageId: "accepted" }), { status: 201 });
  };
  try {
    const submit = (email) => request(env, "/course/full/directory-request", { body: { directory_item_id: "full-file-01", requester_email: email } });
    assert.equal((await submit("")).response.status, 400);
    assert.equal((await submit("placeholder@users.example.invalid")).response.status, 400);
    assert.equal((await submit("reply@example.com")).response.status, 202);
    assertAcknowledgement(sent[1], "reply@example.com");
    assert.equal((await submit("another@example.com")).data.deduplicated, true);
    assert.equal(sent.length, 2);
  } finally { globalThis.fetch = originalFetch; }
});
