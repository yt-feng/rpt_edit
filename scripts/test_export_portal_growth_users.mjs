import assert from "node:assert/strict";
import { mkdtemp, readFile, rm, stat, symlink } from "node:fs/promises";
import os from "node:os";
import path from "node:path";
import test from "node:test";
import { currentUserSnapshot, main, readOnlyBucket, readOnlySupabaseFetch, withCanonicalLoader, writePrivateSnapshot } from "./export_portal_growth_users.mjs";

const ORIGIN = "https://canonical-users.example.invalid";
const user = (index) => ({ id: `u${String(index).padStart(4, "0")}`, username: `fixture${index}`,
  email: `fixture${index}@example.invalid`, created_at: "2025-01-01T00:00:00Z", last_login_at: "2026-01-01T00:00:00Z" });
const accountKey = (...parts) => ["_account", ...parts.map(encodeURIComponent)].join("/");
const access = (who, overrides = {}) => ({ id: `access-${who.id}`, email: who.email, access_mode: "all", status: "active",
  lifetime: true, current_period_end: null, updated_at: "2026-01-01T00:00:00Z", ...overrides });
const entitlement = (who) => ({ id: `ent-${who.id}`, email: who.email, plan: "annual", status: "active", lifetime: true,
  current_period_end: null, updated_at: "2025-01-01T00:00:00Z" });

function fixtureBucket(objects, calls = []) {
  return readOnlyBucket(async (request) => {
    calls.push(request);
    assert.equal(request.op, "get", "Supabase identity authority must never scan stale R2 users");
    const value = objects.get(request.key);
    return value === undefined ? null : { etag: "fixture-etag", body_b64: Buffer.from(JSON.stringify(value)).toString("base64") };
  });
}

test("canonical loader reads beyond short Supabase pages and preserves current access precedence", async () => {
  const users = Array.from({ length: 125 }, (_, index) => user(index));
  users[6] = { ...users[6], username: "admin-a", email: "admin-a@users.portal.example.invalid" };
  const entitlements = [0, 1, 2, 3].map((index) => entitlement(users[index]));
  const objects = new Map([
    [accountKey("access", users[1].email), access(users[1], { access_mode: "none", status: "inactive", lifetime: false })],
    [accountKey("user-state", "email", users[2].email), { email: users[2].email, user_id: users[2].id, disabled: true, updated_at: "2025-01-01T00:00:00Z" }],
    [accountKey("user-state", "id", users[2].id), { email: users[2].email, user_id: users[2].id, disabled: false, updated_at: "2026-01-01T00:00:00Z" }],
    [accountKey("access", users[3].email), access(users[3], { lifetime: false, current_period_end: "2000-01-01T00:00:00Z" })],
    [accountKey("access", users[4].email), access(users[4], { lifetime: false, current_period_end: "2099-01-01T00:00:00Z", duration_value: "trial_3d", download_limit: 10 })],
    [accountKey("access", users[5].email), access(users[5], { access_mode: "filters", institutions: ["fixture bank"] })],
    [accountKey("users", "id", "stale-copy"), user(999)],
    [accountKey("access_backup", "latest", users[1].email), access(users[1])],
  ]);
  const queries = [];
  const originalFetch = globalThis.fetch;
  globalThis.fetch = readOnlySupabaseFetch(ORIGIN, async (request) => {
    const url = new URL(request.url);
    queries.push(url);
    const rows = url.pathname.endsWith("site_users") ? users : entitlements;
    const after = (url.searchParams.get("id") || "gt.").slice(3);
    return new Response(JSON.stringify(rows.filter((row) => row.id > after).slice(0, 37)));
  });
  const calls = [];
  try {
    const result = await withCanonicalLoader(async (load) => currentUserSnapshot(await load({
      ACCOUNT_STORE_MODE: "supabase", SUPABASE_URL: ORIGIN, SUPABASE_SERVICE_ROLE_KEY: "fixture-key",
      REPORT_BUCKET: fixtureBucket(objects, calls),
    }), "supabase"));
    assert.equal(result.complete, true);
    assert.equal(result.user_count, 125);
    assert.equal(result.source_mode, "supabase");
    const byId = new Map(result.users.map((row) => [row.id, row]));
    assert.equal(byId.get(users[0].id).effective_access.active, true);
    assert.equal(byId.get(users[1].id).effective_access.active, false, "later admin revocation overrides older entitlement and backup");
    assert.equal(byId.get(users[2].id).disabled, true, "either disabled mirror remains authoritative");
    assert.equal(byId.get(users[2].id).effective_access.source, "disabled");
    assert.equal(byId.get(users[3].id).effective_access.active, false, "expired later admin decision cannot revive older entitlement");
    assert.equal(byId.get(users[4].id).effective_access.download_limit, 10);
    assert.equal(byId.get(users[5].id).effective_access.access_mode, "filters");
    assert.equal(byId.get(users[6].id).role, "super");
    assert.equal(byId.get(users[6].id).effective_access.source, "role");
    assert.equal(result.users.some((row) => row.id === "stale-copy"), false);
    assert.equal(calls.some((request) => request.key.includes("access_backup")), false);
    assert.equal(queries.filter((url) => url.pathname.endsWith("site_users")).length, 5, "canonical empty page proves complete");
    assert.deepEqual(Object.keys(result.users[0]).sort(), ["id", "email", "created_at", "last_login_at", "disabled", "role", "effective_access"].sort());
    assert.equal(JSON.stringify(result).includes("fixture bank"), false, "filter details and internal account records are not projected");
  } finally { globalThis.fetch = originalFetch; }
});

test("R2 writes and Supabase mutations, redirects, wrong origins and extra tables are blocked", async () => {
  let calls = 0;
  const bucket = readOnlyBucket(async () => { calls++; return null; });
  for (const name of ["put", "delete", "createMultipartUpload", "resumeMultipartUpload"]) await assert.rejects(bucket[name]("ignored", "ignored"));
  assert.equal(calls, 0);
  const fetch = readOnlySupabaseFetch(ORIGIN, async (request) => {
    calls++;
    assert.equal(request.redirect, "error");
    return new Response("[]");
  });
  for (const method of ["POST", "PATCH", "PUT", "DELETE"]) await assert.rejects(fetch(ORIGIN + "/rest/v1/site_users", { method }));
  for (const url of ["https://other.example.invalid/rest/v1/site_users", ORIGIN + "/auth/v1/users", ORIGIN + "/rest/v1/usage_events"]) await assert.rejects(fetch(url));
  for (const base of ["http://example.invalid", "https://user:pass@example.invalid", ORIGIN + "/rest/v1", ORIGIN + "?query=1"]) assert.throws(() => readOnlySupabaseFetch(base));
  assert.equal(calls, 0);
  await fetch(ORIGIN + "/rest/v1/site_users");
  assert.equal(calls, 1);
});

test("canonical read failures never become partial complete snapshots", async () => {
  await assert.rejects(withCanonicalLoader(async (load) => currentUserSnapshot(await load({
    ACCOUNT_STORE_MODE: "r2", REPORT_BUCKET: readOnlyBucket(async () => { throw new Error("private-storage-detail"); }),
  }), "r2")));
  await assert.rejects(main(["--output", "/unused/path"], {}), /private details omitted/);
});

test("private output starts at0600, refuses existing symlinks, and Worker source is unchanged", async () => {
  const source = new URL("../workers/portal-suite-worker/src/index.js", import.meta.url);
  const before = await readFile(source);
  await withCanonicalLoader(async (load) => assert.equal(typeof load, "function"));
  assert.deepEqual(await readFile(source), before);
  const directory = await mkdtemp(path.join(os.tmpdir(), "growth-private-output-test-"));
  try {
    const target = path.join(directory, "users.json");
    await writePrivateSnapshot(target, currentUserSnapshot([], "r2"));
    assert.equal((await stat(target)).mode & 0o777, 0o600);
    assert.equal(JSON.parse(await readFile(target)).complete, true);
    await assert.rejects(writePrivateSnapshot(target, {}), /EEXIST/);
    const link = path.join(directory, "link.json");
    await symlink(target, link);
    await assert.rejects(writePrivateSnapshot(link, {}), /EEXIST/);
  } finally { await rm(directory, { recursive: true, force: true }); }
});
