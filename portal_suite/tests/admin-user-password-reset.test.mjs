import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

const AUTH_SECRET = "admin-password-reset-test-secret";
const ADMIN = Object.freeze({
  id: "admin-id",
  username: "admin-a",
  email: "admin-a@users.portal.example.invalid",
});
const TARGET = Object.freeze({
  id: "target-id",
  username: "target-user",
  email: "target-user@example.invalid",
});

class MemoryR2 {
  constructor() {
    this.rows = new Map();
  }

  seed(key, value) {
    this.rows.set(key, typeof value === "string" ? value : JSON.stringify(value));
  }

  readJson(key) {
    const value = this.rows.get(key);
    return value === undefined ? null : JSON.parse(value);
  }

  async get(key) {
    const value = this.rows.get(key);
    if (value === undefined) return null;
    return {
      async text() { return value; },
    };
  }

  async put(key, value) {
    this.rows.set(key, String(value));
    return { key };
  }
}

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

function passwordFields(password, salt) {
  const digest = createHmac("sha256", AUTH_SECRET)
    .update(`user-password:${salt}:${password}`)
    .digest("hex");
  return {
    password_salt: salt,
    password_hash: `hmac_sha256$${digest}`,
  };
}

function seedUser(bucket, identity, password, options = {}) {
  const createdAt = options.created_at || "2026-08-01T00:00:00.000Z";
  const user = {
    ...identity,
    email_is_generated: false,
    site_origin: "portal",
    registered_site: "portal",
    source_site: "portal",
    ...passwordFields(password, options.salt || `${identity.id}-salt`),
    created_at: createdAt,
    updated_at: createdAt,
    last_login_at: options.last_login_at || "",
  };
  for (const [field, value] of [["id", user.id], ["username", user.username], ["email", user.email]]) {
    bucket.seed(accountKey("users", field, value), user);
  }
  return user;
}

function userToken(user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    iat: now,
    exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", AUTH_SECRET)
    .update(`portal:account-token:v1:${body}`)
    .digest("base64url");
  return `${body}.${signature}`;
}

function tokenPayload(token) {
  return JSON.parse(Buffer.from(String(token || "").split(".", 1)[0], "base64url").toString("utf8"));
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    AUTH_SECRET,
    PASSWORD_SECRET: "report-password-secret",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
  };
}

async function jsonRequest(env, pathname, options = {}) {
  const response = await worker.fetch(
    new Request(`https://worker.test${pathname}`, options),
    env,
    { waitUntil() {} },
  );
  return { response, data: await response.json().catch(() => ({})) };
}

async function resetPassword(env, token, email, confirmReset = true) {
  return jsonRequest(env, "/account-admin/user-password-reset", {
    method: "POST",
    headers: {
      authorization: `Bearer ${token}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({ email, confirm_reset: confirmReset }),
  });
}

async function authWithToken(env, token) {
  return jsonRequest(env, "/auth", {
    headers: { authorization: `Bearer ${token}` },
  });
}

async function updateUserStatus(env, token, email, disabled) {
  return jsonRequest(env, "/account-admin/user-status", {
    method: "POST",
    headers: {
      authorization: `Bearer ${token}`,
      "content-type": "application/json",
    },
    body: JSON.stringify({ email, disabled }),
  });
}

async function login(env, username, password) {
  const captcha = await jsonRequest(env, "/captcha");
  assert.equal(captcha.response.status, 200);
  const svg = Buffer.from(String(captcha.data.image).split(",", 2)[1], "base64").toString("utf8");
  const equation = svg.match(/>(\d+) \+ (\d+) = \?</u);
  assert.ok(equation, "captcha equation must be readable in the fixture");
  return jsonRequest(env, "/auth", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      action: "login",
      username,
      password,
      captcha_token: captcha.data.token,
      captcha_answer: String(Number(equation[1]) + Number(equation[2])),
    }),
  });
}

test("super admin resets a regular user's password to the server-side temporary password and verifies it", async () => {
  const bucket = new MemoryR2();
  const admin = seedUser(bucket, ADMIN, "admin-old-password", { salt: "admin-salt" });
  const originalLastLogin = "2026-08-20T09:30:00.000Z";
  const target = seedUser(bucket, TARGET, "target-old-password", {
    salt: "target-old-salt",
    last_login_at: originalLastLogin,
  });
  const env = envFor(bucket);
  const before = bucket.readJson(accountKey("users", "id", target.id));
  const adminToken = userToken(admin);
  const legacyTargetToken = userToken(target);

  const legacySession = await authWithToken(env, legacyTargetToken);
  assert.equal(legacySession.response.status, 200, JSON.stringify(legacySession.data));
  assert.equal(tokenPayload(legacySession.data.token).session_epoch, "");

  const reset = await resetPassword(env, adminToken, target.email);
  assert.equal(reset.response.status, 200, JSON.stringify(reset.data));
  assert.equal(reset.data.ok, true);
  assert.equal(reset.data.verified, true);
  assert.equal(reset.data.user.email, target.email);
  assert.equal(Object.hasOwn(reset.data.user, "password_hash"), false);
  assert.equal(Object.hasOwn(reset.data.user, "password_salt"), false);
  assert.equal(Object.hasOwn(reset.data.user, "session_epoch"), false);
  assert.doesNotMatch(JSON.stringify(reset.data), /123456|password_(?:hash|salt)|session_epoch/u);

  const after = bucket.readJson(accountKey("users", "id", target.id));
  assert.notEqual(after.password_salt, before.password_salt);
  assert.notEqual(after.password_hash, before.password_hash);
  assert.match(after.password_hash, /^hmac_sha256\$[a-f0-9]{64}$/u);
  assert.equal(after.last_login_at, originalLastLogin, "an admin reset must not be recorded as a user login");

  const firstEmailState = bucket.readJson(accountKey("user-state", "email", target.email));
  const firstIdState = bucket.readJson(accountKey("user-state", "id", target.id));
  assert.match(firstEmailState.session_epoch, /^[a-f0-9]{32}$/u);
  assert.equal(firstIdState.session_epoch, firstEmailState.session_epoch);
  const firstSessionEpoch = firstEmailState.session_epoch;

  const snapshot = bucket.readJson("_account/admin-snapshots/users.json");
  assert.ok(snapshot && snapshot.data && Array.isArray(snapshot.data.users));
  assert.doesNotMatch(JSON.stringify(snapshot), /session_epoch|password_(?:hash|salt)|123456/u);

  const primaryAudit = [...bucket.rows.entries()]
    .filter(([key]) => key.startsWith("_analytics/events/"))
    .map(([, value]) => JSON.parse(value));
  assert.equal(primaryAudit.length, 1);
  assert.equal(primaryAudit[0].type, "admin_user_update");
  assert.equal(primaryAudit[0].path, "/account-admin/user-password-reset");
  assert.equal(primaryAudit[0].target, target.email);
  assert.equal(primaryAudit[0].action, "password_reset");
  assert.equal(primaryAudit[0].status, "success");
  assert.doesNotMatch(JSON.stringify(primaryAudit[0]), /123456|password_(?:hash|salt)|session_epoch/u);

  const revokedLegacySession = await authWithToken(env, legacyTargetToken);
  assert.equal(revokedLegacySession.response.status, 401);

  const oldLogin = await login(env, target.username, "target-old-password");
  assert.equal(oldLogin.response.status, 401);
  const temporaryLogin = await login(env, target.username, "123456");
  assert.equal(temporaryLogin.response.status, 200, JSON.stringify(temporaryLogin.data));
  assert.ok(temporaryLogin.data.token);
  assert.equal(tokenPayload(temporaryLogin.data.token).session_epoch, firstSessionEpoch);
  const currentSession = await authWithToken(env, temporaryLogin.data.token);
  assert.equal(currentSession.response.status, 200, JSON.stringify(currentSession.data));

  const disabled = await updateUserStatus(env, adminToken, target.email, true);
  assert.equal(disabled.response.status, 200, JSON.stringify(disabled.data));
  assert.equal(
    bucket.readJson(accountKey("user-state", "email", target.email)).session_epoch,
    firstSessionEpoch,
  );
  const enabled = await updateUserStatus(env, adminToken, target.email, false);
  assert.equal(enabled.response.status, 200, JSON.stringify(enabled.data));
  assert.equal(
    bucket.readJson(accountKey("user-state", "email", target.email)).session_epoch,
    firstSessionEpoch,
  );
  const sessionAfterEnable = await authWithToken(env, temporaryLogin.data.token);
  assert.equal(sessionAfterEnable.response.status, 200, JSON.stringify(sessionAfterEnable.data));

  const secondReset = await resetPassword(env, adminToken, target.email);
  assert.equal(secondReset.response.status, 200, JSON.stringify(secondReset.data));
  const secondSessionEpoch = bucket.readJson(accountKey("user-state", "email", target.email)).session_epoch;
  assert.match(secondSessionEpoch, /^[a-f0-9]{32}$/u);
  assert.notEqual(secondSessionEpoch, firstSessionEpoch);
  const revokedFirstTemporarySession = await authWithToken(env, temporaryLogin.data.token);
  assert.equal(revokedFirstTemporarySession.response.status, 401);

  const secondTemporaryLogin = await login(env, target.username, "123456");
  assert.equal(secondTemporaryLogin.response.status, 200, JSON.stringify(secondTemporaryLogin.data));
  assert.equal(tokenPayload(secondTemporaryLogin.data.token).session_epoch, secondSessionEpoch);
  const secondCurrentSession = await authWithToken(env, secondTemporaryLogin.data.token);
  assert.equal(secondCurrentSession.response.status, 200, JSON.stringify(secondCurrentSession.data));

  const resetAudits = [...bucket.rows.entries()]
    .filter(([key]) => key.startsWith("_analytics/events/"))
    .map(([, value]) => JSON.parse(value))
    .filter((event) => event.action === "password_reset");
  assert.equal(resetAudits.length, 2);
  assert.doesNotMatch(JSON.stringify(resetAudits), /123456|password_(?:hash|salt)|session_epoch/u);
  assert.doesNotMatch(
    JSON.stringify(bucket.readJson("_account/admin-snapshots/users.json")),
    /session_epoch|password_(?:hash|salt)|123456/u,
  );
});

test("password reset requires a super user, explicit confirmation, and a non-reserved target", async () => {
  const bucket = new MemoryR2();
  const admin = seedUser(bucket, ADMIN, "admin-old-password", { salt: "admin-salt" });
  const target = seedUser(bucket, TARGET, "target-old-password", { salt: "target-salt" });
  const reserved = seedUser(bucket, {
    id: "reserved-id",
    username: "subscriber-a",
    email: "subscriber-a@example.invalid",
  }, "reserved-password", { salt: "reserved-salt" });
  const env = envFor(bucket);
  const before = bucket.readJson(accountKey("users", "id", target.id));

  const regularAttempt = await resetPassword(env, userToken(target), target.email);
  assert.equal(regularAttempt.response.status, 403);

  const unconfirmed = await resetPassword(env, userToken(admin), target.email, false);
  assert.equal(unconfirmed.response.status, 400);

  const superTarget = await resetPassword(env, userToken(admin), admin.email);
  assert.equal(superTarget.response.status, 400);
  assert.match(superTarget.data.detail, /系统角色/u);

  const reservedTarget = await resetPassword(env, userToken(admin), reserved.email);
  assert.equal(reservedTarget.response.status, 400);
  assert.match(reservedTarget.data.detail, /系统角色/u);

  const after = bucket.readJson(accountKey("users", "id", target.id));
  assert.equal(after.password_salt, before.password_salt);
  assert.equal(after.password_hash, before.password_hash);
  assert.equal(bucket.readJson(accountKey("user-state", "email", target.email)), null);
  assert.equal(bucket.readJson(accountKey("user-state", "id", target.id)), null);
  assert.equal(
    [...bucket.rows.keys()].filter((key) => key.startsWith("_analytics/events/")).length,
    0,
  );
});
