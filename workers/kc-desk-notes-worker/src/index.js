const CACHE_TTL_MS = 5 * 60 * 1000;
const DEFAULT_R2_PREFIX = "reports";
const CONTACT_WECHAT = "MacroGate";
const ADMIN_TOKEN_TTL_SECONDS = 180 * 24 * 60 * 60;
const USER_TOKEN_TTL_SECONDS = 30 * 24 * 60 * 60;
const CAPTCHA_TTL_SECONDS = 10 * 60;
const PASSWORD_ITERATIONS = 120000;
const GENERATED_EMAIL_DOMAIN = "users.kcdesk.com";
const USERNAME_PATTERN = /^[a-z0-9][a-z0-9_.-]{2,31}$/;
const EMAIL_PATTERN = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const ACTIVE_STATUSES = new Set(["active", "trialing"]);
const SUPER_ACCOUNT_USERNAMES = new Set(["twotigers"]);
const SUPER_ACCOUNT_EMAILS = new Set(["twotigers@users.kcdesk.com"]);
const DEFAULT_GITHUB_REPO = "yt-feng/rpt_edit";
const DEFAULT_GITHUB_REF = "main";
const BBG_SHOW_REPO = "yt-feng/bbg-show";
const BBG_SHOW_PREFIX = "rendered-clips";
const GITHUB_CACHE_PREFIX = "_account/github-cache";
const GITHUB_CACHE_RETENTION_MS = 3 * 24 * 60 * 60 * 1000;
const PADDLE_HANDLED_EVENTS = new Set([
  "transaction.completed",
  "subscription.created",
  "subscription.updated",
  "subscription.canceled",
  "subscription.past_due",
  "subscription.paused",
  "subscription.resumed",
]);

// External report integration. Search/detail endpoints are public; PDF access
// still requires a password.
const EXTERNAL_HOST = "report" + "ify.cn";
const EXTERNAL_API = `https://api.${EXTERNAL_HOST}`;
const EXTERNAL_SITE = `https://${EXTERNAL_HOST}`;
const EXTERNAL_R2_PREFIX = "report" + "ify";
const EXTERNAL_STATUS_PREFIX = "report" + "ify-status";
const EXTERNAL_SEARCH_PAGE_SIZE = 20;
const EXTERNAL_UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/124.0 Safari/537.36";

// High-authority foreign-report metadata. Search endpoints are public; this
// integration intentionally does not download PDFs.
const AUTHORITY_HOST = ["www", "na" + "sh-ai", "cn"].join(".");
const AUTHORITY_ORIGIN = `https://${AUTHORITY_HOST}`;
const AUTHORITY_SOURCE = "authority";
const AUTHORITY_SEARCH_PAGE_SIZE = 20;
const AUTHORITY_UA = "KCDeskAuthoritySearch/1.0";
const AUTHORITY_KINDS = {
  "foreign": {
    endpoint: "/reports/foreign/search",
    referer: `${AUTHORITY_ORIGIN}/foreign.html`,
    price_cents: 2600,
    label: "普通外文",
  },
  "foreign-rt": {
    endpoint: "/reports/foreign-rt/search",
    referer: `${AUTHORITY_ORIGIN}/foreign-rt.html`,
    price_cents: 4600,
    label: "实时外文",
  },
};

const HIBOR_ORIGIN = "https://www.hibor.com.cn";
const HIBOR_SOURCE = "report-a";
const HIBOR_SEARCH_PAGE_SIZE = 30;
const HIBOR_UA =
  "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 " +
  "(KHTML, like Gecko) Chrome/137.0 Safari/537.36";

let catalogCache = null;
let catalogFetchedAt = 0;
let rulesCache = null;
let rulesFetchedAt = 0;

function allowedOrigin(request, env) {
  const requestOrigin = request.headers.get("Origin") || "";
  const configured = String(env.ALLOWED_ORIGIN || "")
    .split(",")
    .map((origin) => {
      const trimmed = origin.trim();
      try {
        return new URL(trimmed).origin;
      } catch (_error) {
        return trimmed;
      }
    })
    .filter(Boolean);

  if (!configured.length) return requestOrigin || "*";
  if (configured.includes(requestOrigin)) return requestOrigin;
  return configured[0];
}

function corsHeaders(request, env) {
  return {
    "Access-Control-Allow-Origin": allowedOrigin(request, env),
    "Access-Control-Allow-Methods": "GET, POST, OPTIONS",
    "Access-Control-Allow-Headers": "Content-Type, Authorization, Paddle-Signature, Range",
    "Access-Control-Expose-Headers": "Content-Disposition, Content-Length, Content-Range, Accept-Ranges",
    "Vary": "Origin",
  };
}

function jsonResponse(request, env, status, body) {
  return new Response(JSON.stringify(body), {
    status,
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/json; charset=utf-8",
      "Cache-Control": "no-store",
    },
  });
}

async function fetchJson(url) {
  const response = await fetch(url, { headers: { "Accept": "application/json" } });
  if (!response.ok) {
    throw new Error(`Could not fetch ${url}: ${response.status}`);
  }
  return response.json();
}

async function loadCatalog(env) {
  const now = Date.now();
  if (catalogCache && now - catalogFetchedAt < CACHE_TTL_MS) return catalogCache;
  if (!env.CATALOG_URL) throw new Error("CATALOG_URL is not configured");
  catalogCache = await fetchJson(env.CATALOG_URL);
  catalogFetchedAt = now;
  return catalogCache;
}

async function loadRules(env) {
  const now = Date.now();
  if (rulesCache && now - rulesFetchedAt < CACHE_TTL_MS) return rulesCache;
  if (!env.PASSWORD_RULES_URL) throw new Error("PASSWORD_RULES_URL is not configured");
  rulesCache = await fetchJson(env.PASSWORD_RULES_URL);
  rulesFetchedAt = now;
  return rulesCache;
}

function findReport(catalog, id) {
  return (catalog.items || []).find((item) => item.id === id);
}

function findPasswordGroup(rules, groupId) {
  const target = groupId || rules.default_group || "default";
  return (rules.groups || []).find((group) => group.id === target && group.active !== false);
}

function normalizePassword(value) {
  return String(value || "").trim().toLowerCase();
}

function base32NoPadding(bytes) {
  const alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567";
  let output = "";
  let buffer = 0;
  let bitsLeft = 0;
  for (const byte of bytes) {
    buffer = (buffer << 8) | byte;
    bitsLeft += 8;
    while (bitsLeft >= 5) {
      output += alphabet[(buffer >> (bitsLeft - 5)) & 31];
      bitsLeft -= 5;
    }
  }
  if (bitsLeft > 0) {
    output += alphabet[(buffer << (5 - bitsLeft)) & 31];
  }
  return output;
}

function base64UrlEncodeBytes(bytes) {
  let binary = "";
  for (const byte of bytes) {
    binary += String.fromCharCode(byte);
  }
  return btoa(binary).replace(/\+/g, "-").replace(/\//g, "_").replace(/=+$/g, "");
}

function base64UrlEncodeText(value) {
  return base64UrlEncodeBytes(new TextEncoder().encode(value));
}

function base64UrlDecodeText(value) {
  const base64 = String(value || "").replace(/-/g, "+").replace(/_/g, "/");
  const padded = base64 + "=".repeat((4 - base64.length % 4) % 4);
  const binary = atob(padded);
  const bytes = new Uint8Array(binary.length);
  for (let index = 0; index < binary.length; index += 1) {
    bytes[index] = binary.charCodeAt(index);
  }
  return new TextDecoder().decode(bytes);
}

function constantTimeEqual(left, right) {
  const a = String(left || "");
  const b = String(right || "");
  const length = Math.max(a.length, b.length);
  let diff = a.length ^ b.length;
  for (let index = 0; index < length; index += 1) {
    diff |= (a.charCodeAt(index) || 0) ^ (b.charCodeAt(index) || 0);
  }
  return diff === 0;
}

async function hmacSha256Bytes(secret, message) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign("HMAC", key, encoder.encode(message));
  return new Uint8Array(signature);
}

function adminTokenSecret(env) {
  return String(env.PASSWORD_SECRET || env.MASTER_KEY || "");
}

async function signAdminToken(env, payload) {
  const secret = adminTokenSecret(env);
  if (!secret) throw new Error("Admin token secret is not configured");
  const body = base64UrlEncodeText(JSON.stringify(payload));
  const signature = base64UrlEncodeBytes(await hmacSha256Bytes(secret, body));
  return `${body}.${signature}`;
}

async function verifyAdminToken(env, token) {
  const secret = adminTokenSecret(env);
  if (!secret) throw new Error("Admin token secret is not configured");
  const [body, signature] = String(token || "").split(".");
  if (!body || !signature) throw new Error("Admin session is invalid");
  const expected = base64UrlEncodeBytes(await hmacSha256Bytes(secret, body));
  if (!constantTimeEqual(signature, expected)) throw new Error("Admin session is invalid");

  let payload;
  try {
    payload = JSON.parse(base64UrlDecodeText(body));
  } catch (_error) {
    throw new Error("Admin session is invalid");
  }
  const now = Math.floor(Date.now() / 1000);
  if (!payload || Number(payload.exp || 0) < now) throw new Error("Admin session has expired");
  return payload;
}

async function derivedReportPassword(env, id) {
  if (!env.PASSWORD_SECRET) throw new Error("PASSWORD_SECRET is not configured");
  const cleanId = String(id || "").trim().toLowerCase();
  const digest = await hmacSha256Bytes(env.PASSWORD_SECRET, `kc-desk-notes:${cleanId}`);
  const code = base32NoPadding(digest).slice(0, 12);
  return `KC-${code.slice(0, 4)}-${code.slice(4, 8)}-${code.slice(8, 12)}`;
}

async function derivedPasswordMatches(env, id, password) {
  return normalizePassword(password) === normalizePassword(await derivedReportPassword(env, id));
}

async function sha256Hex(value) {
  const data = new TextEncoder().encode(value);
  const digest = await crypto.subtle.digest("SHA-256", data);
  return Array.from(new Uint8Array(digest))
    .map((byte) => byte.toString(16).padStart(2, "0"))
    .join("");
}

async function hmacSha256Hex(secret, message) {
  const digest = await hmacSha256Bytes(secret, message);
  return Array.from(digest).map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function randomInt(min, max) {
  const span = max - min + 1;
  const buffer = new Uint32Array(1);
  crypto.getRandomValues(buffer);
  return min + (buffer[0] % span);
}

function randomHex(byteLength) {
  const bytes = new Uint8Array(byteLength);
  crypto.getRandomValues(bytes);
  return Array.from(bytes).map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function pbkdf2Digest(password, salt, iterations) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(password),
    "PBKDF2",
    false,
    ["deriveBits"],
  );
  const bits = await crypto.subtle.deriveBits(
    {
      name: "PBKDF2",
      salt: encoder.encode(salt),
      iterations,
      hash: "SHA-256",
    },
    key,
    256,
  );
  return base64UrlEncodeBytes(new Uint8Array(bits));
}

async function hashUserPassword(env, password) {
  const salt = randomHex(16);
  const digest = await hmacSha256Hex(accountSecret(env), `user-password:${salt}:${password}`);
  return {
    password_salt: salt,
    password_hash: `hmac_sha256$${digest}`,
  };
}

async function verifyUserPassword(env, password, salt, storedHash) {
  let algorithm = "pbkdf2_sha256";
  let iterations = PASSWORD_ITERATIONS;
  let digest = String(storedHash || "");
  const parts = digest.split("$");
  if (parts.length === 2) {
    [algorithm, digest] = [parts[0], parts[1]];
  }
  if (parts.length === 3) {
    [algorithm, iterations, digest] = [parts[0], Number(parts[1]), parts[2]];
  }
  if (algorithm === "hmac_sha256") {
    if (!digest) return false;
    const actual = await hmacSha256Hex(accountSecret(env), `user-password:${salt}:${password}`);
    return constantTimeEqual(actual, digest);
  }
  if (algorithm !== "pbkdf2_sha256" || !Number.isFinite(iterations) || !digest) return false;
  const actual = await pbkdf2Digest(password, salt, iterations);
  return constantTimeEqual(actual, digest);
}

function normalizeUsername(value) {
  return String(value || "").trim().toLowerCase().replace(/^@+/, "");
}

function normalizeEmail(value) {
  const email = String(value || "").trim().toLowerCase();
  return EMAIL_PATTERN.test(email) ? email : "";
}

function isSuperAccount(user) {
  if (!user) return false;
  const username = normalizeUsername(user.username);
  const email = normalizeEmail(user.email);
  return SUPER_ACCOUNT_USERNAMES.has(username) || SUPER_ACCOUNT_EMAILS.has(email);
}

function generatedEmailForUsername(username) {
  return `${username}@${GENERATED_EMAIL_DOMAIN}`;
}

function isGeneratedEmail(email) {
  return String(email || "").trim().toLowerCase().endsWith(`@${GENERATED_EMAIL_DOMAIN}`);
}

function accountSecret(env) {
  const secret = String(env.AUTH_SECRET || env.PASSWORD_SECRET || env.MASTER_KEY || "").trim();
  if (!secret || secret === "unconfigured") throw new Error("Account service is temporarily unavailable.");
  return secret;
}

async function signAccountPayload(env, payload) {
  const body = base64UrlEncodeText(JSON.stringify(payload));
  const signature = base64UrlEncodeBytes(await hmacSha256Bytes(accountSecret(env), body));
  return `${body}.${signature}`;
}

async function verifyAccountPayload(env, token, expectedKind) {
  const [body, signature] = String(token || "").split(".");
  if (!body || !signature) throw new Error("Session is invalid.");
  const expected = base64UrlEncodeBytes(await hmacSha256Bytes(accountSecret(env), body));
  if (!constantTimeEqual(signature, expected)) throw new Error("Session is invalid.");
  let payload;
  try {
    payload = JSON.parse(base64UrlDecodeText(body));
  } catch (_error) {
    throw new Error("Session is invalid.");
  }
  if (payload.kind !== expectedKind) throw new Error("Session is invalid.");
  const now = Math.floor(Date.now() / 1000);
  if (Number(payload.exp || 0) < now) throw new Error("Session has expired.");
  return payload;
}

async function createUserToken(env, user) {
  const now = Math.floor(Date.now() / 1000);
  return signAccountPayload(env, {
    kind: "user",
    sub: String(user.id || ""),
    username: String(user.username || ""),
    email: String(user.email || ""),
    iat: now,
    exp: now + USER_TOKEN_TTL_SECONDS,
  });
}

function publicUser(user) {
  const email = String(user.email || "");
  const superAccount = isSuperAccount(user);
  return {
    id: user.id || "",
    username: user.username || "",
    email,
    email_is_generated: Boolean(user.email_is_generated) || isGeneratedEmail(email),
    created_at: user.created_at || "",
    updated_at: user.updated_at || "",
    role: superAccount ? "super" : "user",
    is_super: superAccount,
  };
}

function bearerToken(request) {
  const header = request.headers.get("Authorization") || request.headers.get("authorization") || "";
  return header.toLowerCase().startsWith("bearer ") ? header.slice(7).trim() : "";
}

function supabaseBaseUrl(env) {
  const url = String(env.SUPABASE_URL || "").trim().replace(/\/+$/, "");
  if (!url || url === "unconfigured") throw new Error("Account database is not configured.");
  return url;
}

function supabaseServiceKey(env) {
  const key = String(env.SUPABASE_SERVICE_ROLE_KEY || "").trim();
  if (!key || key === "unconfigured") throw new Error("Account database is not configured.");
  return key;
}

async function supabaseRequest(env, method, path, payload = null, options = {}) {
  const key = supabaseServiceKey(env);
  const headers = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": `Bearer ${key}`,
    "apikey": key,
  };
  if (options.prefer) headers.Prefer = options.prefer;
  else if (options.preferReturn) headers.Prefer = "return=representation";
  const response = await fetch(`${supabaseBaseUrl(env)}${path}`, {
    method,
    headers,
    body: payload === null ? undefined : JSON.stringify(payload),
  });
  const text = await response.text();
  if (!response.ok) {
    throw new Error(`Account database error ${response.status}: ${text.slice(0, 300)}`);
  }
  return text ? JSON.parse(text) : null;
}

function hasSupabaseConfig(env) {
  return cleanEnv(env.SUPABASE_URL) && cleanEnv(env.SUPABASE_SERVICE_ROLE_KEY);
}

function accountBucket(env) {
  if (!env.REPORT_BUCKET) throw new Error("Account storage is temporarily unavailable.");
  return env.REPORT_BUCKET;
}

async function r2GetJson(env, key) {
  const object = await accountBucket(env).get(key);
  if (!object) return null;
  try {
    return JSON.parse(await object.text());
  } catch (_error) {
    return null;
  }
}

async function safeR2GetJson(env, key) {
  try {
    return await r2GetJson(env, key);
  } catch (_error) {
    return null;
  }
}

async function r2PutJson(env, key, payload) {
  await accountBucket(env).put(key, JSON.stringify(payload), {
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  return payload;
}

async function safeR2PutJson(env, key, payload) {
  try {
    await r2PutJson(env, key, payload);
    return true;
  } catch (_error) {
    return false;
  }
}

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

function queryString(params) {
  const search = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => search.set(key, value));
  return search.toString();
}

async function createSiteUserInR2(env, fields) {
  const id = crypto.randomUUID ? crypto.randomUUID() : randomHex(16);
  const user = { ...fields, id };
  return writeSiteUserIndexesInR2(env, user);
}

async function writeSiteUserIndexesInR2(env, user) {
  const now = new Date().toISOString();
  const normalized = {
    ...user,
    id: user.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    updated_at: user.updated_at || now,
  };
  const writes = [
    safeR2PutJson(env, accountKey("users", "id", normalized.id), normalized),
  ];
  if (normalized.username) writes.push(safeR2PutJson(env, accountKey("users", "username", normalized.username), normalized));
  if (normalized.email) writes.push(safeR2PutJson(env, accountKey("users", "email", normalized.email), normalized));
  const results = await Promise.all(writes);
  if (!results.some(Boolean)) throw new Error("Account storage is temporarily unavailable.");
  return normalized;
}

async function repairSiteUserIndexesInR2(env, user) {
  if (!user) return null;
  try {
    return await writeSiteUserIndexesInR2(env, user);
  } catch (_error) {
    return user;
  }
}

async function updateSiteUserInR2(env, userId, fields) {
  const existing = await safeR2GetJson(env, accountKey("users", "id", userId));
  const user = { ...(existing || {}), ...fields, id: userId, updated_at: new Date().toISOString() };
  if (user.username) await r2PutJson(env, accountKey("users", "username", user.username), user);
  if (user.email) await r2PutJson(env, accountKey("users", "email", user.email), user);
  await r2PutJson(env, accountKey("users", "id", userId), user);
  return user;
}

async function findSiteUserByUsername(env, username) {
  if (hasSupabaseConfig(env)) {
    try {
      const query = queryString({ username: `eq.${username}`, limit: "1" });
      const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
      if (Array.isArray(rows) && rows.length) return rows[0];
    } catch (_error) {
      // Fall through to account data persisted in R2.
    }
  }
  return repairSiteUserIndexesInR2(env, await safeR2GetJson(env, accountKey("users", "username", username)));
}

async function findSiteUserByEmail(env, email) {
  if (hasSupabaseConfig(env)) {
    try {
      const query = queryString({ email: `eq.${email}`, limit: "1" });
      const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
      if (Array.isArray(rows) && rows.length) return rows[0];
    } catch (_error) {
      // Fall through to account data persisted in R2.
    }
  }
  return repairSiteUserIndexesInR2(env, await safeR2GetJson(env, accountKey("users", "email", email)));
}

async function createSiteUser(env, fields) {
  if (!hasSupabaseConfig(env)) return createSiteUserInR2(env, fields);
  try {
    const rows = await supabaseRequest(env, "POST", "/rest/v1/site_users?select=*", fields, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : fields;
  } catch (_error) {
    return createSiteUserInR2(env, fields);
  }
}

async function updateSiteUser(env, userId, fields) {
  if (!hasSupabaseConfig(env)) return updateSiteUserInR2(env, userId, fields);
  try {
    const query = queryString({ id: `eq.${userId}`, select: "*" });
    const rows = await supabaseRequest(env, "PATCH", `/rest/v1/site_users?${query}`, {
      ...fields,
      updated_at: new Date().toISOString(),
    }, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : fields;
  } catch (_error) {
    return updateSiteUserInR2(env, userId, fields);
  }
}

async function currentUserFromRequest(env, request) {
  const token = bearerToken(request);
  if (!token) throw new Error("Please log in.");
  const payload = await verifyAccountPayload(env, token, "user");
  const user = await findSiteUserByUsername(env, normalizeUsername(payload.username));
  if (!user) throw new Error("Account not found.");
  return user;
}

async function siteUserPasswordMatches(env, user, password) {
  if (!user) return false;
  return verifyUserPassword(
    env,
    password,
    String(user.password_salt || ""),
    String(user.password_hash || ""),
  );
}

async function authSuccessResponse(request, env, status, user, extra = {}) {
  const repaired = await repairSiteUserIndexesInR2(env, user);
  return jsonResponse(request, env, status, {
    token: await createUserToken(env, repaired),
    user: publicUser(repaired),
    ...extra,
  });
}

async function recoverExistingUserResponse(request, env, user, password) {
  if (!await siteUserPasswordMatches(env, user, password)) return null;
  return authSuccessResponse(request, env, 200, user, { recovered: true });
}

async function findEntitlement(env, email) {
  if (hasSupabaseConfig(env)) {
    try {
      const query = queryString({ email: `eq.${email}`, order: "updated_at.desc", limit: "1" });
      const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
      if (Array.isArray(rows) && rows.length) return rows[0];
    } catch (_error) {
      // Fall through to account data persisted in R2.
    }
  }
  return safeR2GetJson(env, accountKey("entitlements", email));
}

async function saveEntitlementInR2(env, email, fields, now = new Date().toISOString()) {
  const existing = await safeR2GetJson(env, accountKey("entitlements", email));
  return r2PutJson(env, accountKey("entitlements", email), {
    ...(existing || {}),
    ...fields,
    email,
    id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    updated_at: now,
    created_at: existing && existing.created_at || now,
  });
}

async function saveEntitlement(env, email, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) return saveEntitlementInR2(env, email, fields, now);
  try {
    const query = queryString({ email: `eq.${email}`, order: "updated_at.desc", limit: "1" });
    const existingRows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
    const existing = Array.isArray(existingRows) && existingRows.length ? existingRows[0] : null;
    const payload = { ...fields, email, updated_at: now };
    if (existing && existing.id) {
      const patchQuery = queryString({ id: `eq.${existing.id}`, select: "*" });
      const rows = await supabaseRequest(env, "PATCH", `/rest/v1/user_entitlements?${patchQuery}`, payload, { preferReturn: true });
      return Array.isArray(rows) && rows.length ? rows[0] : payload;
    }
    const rows = await supabaseRequest(env, "POST", "/rest/v1/user_entitlements?select=*", {
      ...payload,
      created_at: now,
    }, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : payload;
  } catch (_error) {
    return saveEntitlementInR2(env, email, fields, now);
  }
}

async function findReportPurchase(env, email, reportId, source) {
  if (hasSupabaseConfig(env)) {
    const query = queryString({
      email: `eq.${email}`,
      report_id: `eq.${reportId}`,
      source: `eq.${source}`,
      order: "updated_at.desc",
      limit: "1",
    });
    try {
      const rows = await supabaseRequest(env, "GET", `/rest/v1/report_purchases?${query}`);
      if (Array.isArray(rows) && rows.length) return rows[0];
    } catch (_error) {
      // Fall through to account data persisted in R2.
    }
  }
  return safeR2GetJson(env, accountKey("purchases", source, reportId, email));
}

async function saveReportPurchaseInR2(env, fields, now = new Date().toISOString()) {
  const existing = await safeR2GetJson(env, accountKey("purchases", fields.source, fields.report_id, fields.email));
  return r2PutJson(env, accountKey("purchases", fields.source, fields.report_id, fields.email), {
    ...(existing || {}),
    ...fields,
    id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
    purchased_at: existing && existing.purchased_at || now,
    created_at: existing && existing.created_at || now,
    updated_at: now,
  });
}

async function saveReportPurchase(env, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) return saveReportPurchaseInR2(env, fields, now);
  try {
    const query = queryString({
      email: `eq.${fields.email}`,
      report_id: `eq.${fields.report_id}`,
      source: `eq.${fields.source}`,
      order: "updated_at.desc",
      limit: "1",
    });
    const existingRows = await supabaseRequest(env, "GET", `/rest/v1/report_purchases?${query}`);
    const existing = Array.isArray(existingRows) && existingRows.length ? existingRows[0] : null;
    const payload = { ...fields, updated_at: now };
    if (existing && existing.id) {
      const patchQuery = queryString({ id: `eq.${existing.id}`, select: "*" });
      const rows = await supabaseRequest(env, "PATCH", `/rest/v1/report_purchases?${patchQuery}`, payload, { preferReturn: true });
      return Array.isArray(rows) && rows.length ? rows[0] : payload;
    }
    const rows = await supabaseRequest(env, "POST", "/rest/v1/report_purchases?select=*", {
      ...payload,
      purchased_at: now,
      created_at: now,
    }, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : payload;
  } catch (_error) {
    return saveReportPurchaseInR2(env, fields, now);
  }
}

async function insertUsageEventInR2(env, email, eventType, metadata = {}) {
  const key = accountKey("usage", email, `${Date.now()}-${randomHex(4)}.json`);
  await r2PutJson(env, key, {
    id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
    email,
    event_type: eventType,
    units: 1,
    metadata,
    created_at: new Date().toISOString(),
  });
}

async function insertUsageEvent(env, email, eventType, metadata = {}) {
  if (!hasSupabaseConfig(env)) return insertUsageEventInR2(env, email, eventType, metadata);
  try {
    await supabaseRequest(env, "POST", "/rest/v1/usage_events", {
      email,
      event_type: eventType,
      units: 1,
      metadata,
    });
  } catch (_error) {
    await insertUsageEventInR2(env, email, eventType, metadata);
  }
}

function periodIsCurrent(value) {
  if (!value || typeof value !== "string") return false;
  const time = Date.parse(value);
  return Number.isFinite(time) && time > Date.now();
}

function publicEntitlement(row) {
  if (!row) {
    return {
      plan: "free",
      status: "inactive",
      lifetime: false,
      current_period_end: null,
      active: false,
    };
  }
  const status = String(row.status || "inactive");
  const lifetime = Boolean(row.lifetime);
  const currentPeriodEnd = row.current_period_end || null;
  const active = ACTIVE_STATUSES.has(status) && (lifetime || periodIsCurrent(currentPeriodEnd));
  return {
    email: row.email || "",
    plan: row.plan || "free",
    status,
    lifetime,
    current_period_end: currentPeriodEnd,
    active,
    updated_at: row.updated_at || "",
  };
}

function superEntitlement(user) {
  return {
    email: normalizeEmail(user && user.email) || "",
    plan: "super",
    status: "active",
    lifetime: true,
    current_period_end: null,
    active: true,
    updated_at: new Date().toISOString(),
  };
}

async function reportAccessForUser(env, user, reportId, source) {
  const email = normalizeEmail(user.email);
  if (!email) return { can_download: false, entitlement: publicEntitlement(null), purchase: null };
  if (isSuperAccount(user)) {
    return {
      can_download: true,
      entitlement: superEntitlement(user),
      purchase: null,
    };
  }
  const [entitlementRow, purchase] = await Promise.all([
    findEntitlement(env, email).catch(() => null),
    reportId ? findReportPurchase(env, email, reportId, source).catch(() => null) : Promise.resolve(null),
  ]);
  const entitlement = publicEntitlement(entitlementRow);
  const annual = entitlement.active && entitlement.plan === "annual";
  const purchased = purchase && ACTIVE_STATUSES.has(String(purchase.status || "active"));
  return {
    can_download: Boolean(annual || purchased),
    entitlement,
    purchase: purchased ? purchase : null,
  };
}

async function accountCanDownload(env, request, reportId, source) {
  try {
    const user = await currentUserFromRequest(env, request);
    const access = await reportAccessForUser(env, user, reportId, source);
    return access.can_download;
  } catch (_error) {
    return false;
  }
}

async function captchaAnswerHash(env, answer, nonce) {
  return hmacSha256Hex(accountSecret(env), `captcha:${nonce}:${answer}`);
}

function captchaSvg(question) {
  const rotate = randomInt(-5, 5);
  const lineA = randomInt(12, 28);
  const lineB = randomInt(84, 108);
  const dotA = randomInt(24, 132);
  const dotB = randomInt(18, 50);
  return `<svg xmlns="http://www.w3.org/2000/svg" width="180" height="64" viewBox="0 0 180 64" role="img" aria-label="captcha">
  <rect width="180" height="64" rx="14" fill="#f8fafc"/>
  <path d="M8 ${lineA} C52 2, 92 68, 172 ${lineB}" fill="none" stroke="#99f6e4" stroke-width="3" opacity=".8"/>
  <path d="M4 ${lineB} C48 70, 118 -4, 176 ${lineA}" fill="none" stroke="#bfdbfe" stroke-width="3" opacity=".8"/>
  <circle cx="${dotA}" cy="${dotB}" r="4" fill="#fbbf24" opacity=".75"/>
  <text x="90" y="42" text-anchor="middle" transform="rotate(${rotate} 90 32)" fill="#111827" font-size="28" font-family="ui-monospace, SFMono-Regular, Menlo, monospace" font-weight="900">${question}</text>
</svg>`;
}

async function createCaptchaChallenge(env) {
  const left = randomInt(2, 9);
  const right = randomInt(1, 9);
  const answer = String(left + right);
  const nonce = randomHex(12);
  const now = Math.floor(Date.now() / 1000);
  const token = await signAccountPayload(env, {
    kind: "captcha",
    nonce,
    answer_hash: await captchaAnswerHash(env, answer, nonce),
    iat: now,
    exp: now + CAPTCHA_TTL_SECONDS,
  });
  const svg = captchaSvg(`${left} + ${right} = ?`);
  return {
    token,
    image: `data:image/svg+xml;base64,${btoa(svg)}`,
    expires_in: CAPTCHA_TTL_SECONDS,
  };
}

async function verifyCaptchaResponse(env, token, answer) {
  try {
    const payload = await verifyAccountPayload(env, token, "captcha");
    const clean = String(answer || "").replace(/\D+/g, "");
    if (!clean || !payload.nonce || !payload.answer_hash) return false;
    const actual = await captchaAnswerHash(env, clean, payload.nonce);
    return constantTimeEqual(actual, payload.answer_hash);
  } catch (_error) {
    return false;
  }
}

async function passwordMatches(env, group, password) {
  const expected = String(group.password_sha256 || "");
  if (!expected || expected === "REPLACE_WITH_SHA256_HASH") {
    throw new Error(`Password hash is not configured for group: ${group.id}`);
  }
  if (!env.PASSWORD_SECRET) throw new Error("PASSWORD_SECRET is not configured");
  const actual = await sha256Hex(`${env.PASSWORD_SECRET}:${password}`);
  return actual === expected.toLowerCase();
}

async function defaultPasswordMatches(env, password) {
  const master = String(env.MASTER_KEY || "").trim();
  if (master && normalizePassword(password) === normalizePassword(master)) return true;

  try {
    const rules = await loadRules(env);
    const group = findPasswordGroup(rules, rules.default_group);
    return group ? await passwordMatches(env, group, password) : false;
  } catch (_error) {
    return false;
  }
}

async function sharedReportPasswordMatches(env, id, password) {
  if (!password) return false;
  try {
    if (await derivedPasswordMatches(env, id, password)) return true;
  } catch (_error) {
    // Fall through to the shared password.
  }
  return defaultPasswordMatches(env, password);
}

async function handleCaptcha(request, env) {
  try {
    return jsonResponse(request, env, 200, await createCaptchaChallenge(env));
  } catch (_error) {
    return jsonResponse(request, env, 503, { detail: "Account service is temporarily unavailable." });
  }
}

async function handleAuth(request, env) {
  if (request.method === "GET") {
    try {
      const user = await currentUserFromRequest(env, request);
      return jsonResponse(request, env, 200, {
        token: await createUserToken(env, user),
        user: publicUser(user),
      });
    } catch (error) {
      return jsonResponse(request, env, 401, { detail: error.message || "Please log in." });
    }
  }

  let payload = {};
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { detail: "Invalid JSON body." });
  }

  const action = String(payload.action || "login").trim().toLowerCase();
  const username = normalizeUsername(payload.username);
  const password = String(payload.password || "");
  if (!["login", "register"].includes(action)) {
    return jsonResponse(request, env, 400, { detail: "Unsupported auth action." });
  }
  if (!(await verifyCaptchaResponse(env, String(payload.captcha_token || ""), String(payload.captcha_answer || "")))) {
    return jsonResponse(request, env, 400, { detail: "验证码不正确或已过期。" });
  }
  if (!USERNAME_PATTERN.test(username)) {
    return jsonResponse(request, env, 400, { detail: "用户名需为 3-32 位小写字母、数字、点、短横线或下划线。" });
  }
  if (password.length < 4 || password.length > 128) {
    return jsonResponse(request, env, 400, { detail: "密码需为 4-128 位。" });
  }

  try {
    if (action === "register") {
      const existing = await findSiteUserByUsername(env, username);
      if (existing) {
        const recovered = await recoverExistingUserResponse(request, env, existing, password);
        if (recovered) return recovered;
        return jsonResponse(request, env, 409, { detail: "用户名已被注册。" });
      }
      const rawEmail = String(payload.email || "");
      let email = normalizeEmail(rawEmail);
      let emailIsGenerated = false;
      if (rawEmail.trim() && !email) {
        return jsonResponse(request, env, 400, { detail: "邮箱格式不正确，可以留空。" });
      }
      if (!email) {
        email = generatedEmailForUsername(username);
        emailIsGenerated = true;
      }
      const existingEmail = await findSiteUserByEmail(env, email);
      if (existingEmail) {
        const recovered = await recoverExistingUserResponse(request, env, existingEmail, password);
        if (recovered) return recovered;
        return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
      }
      const now = new Date().toISOString();
      const passwordFields = await hashUserPassword(env, password);
      const fields = {
        username,
        email,
        email_is_generated: emailIsGenerated,
        ...passwordFields,
        created_at: now,
        updated_at: now,
        last_login_at: now,
      };
      let user;
      try {
        user = await createSiteUser(env, fields);
      } catch (error) {
        const recovered = await recoverExistingUserResponse(request, env, await findSiteUserByUsername(env, username), password);
        if (recovered) return recovered;
        throw error;
      }
      return authSuccessResponse(request, env, 201, user);
    }

    const user = await findSiteUserByUsername(env, username);
    const ok = await siteUserPasswordMatches(env, user, password);
    if (!ok) return jsonResponse(request, env, 401, { detail: "用户名或密码不正确。" });
    const repaired = await repairSiteUserIndexesInR2(env, user);
    const updated = repaired.id ? await updateSiteUser(env, repaired.id, { last_login_at: new Date().toISOString() }) : repaired;
    const merged = { ...repaired, ...updated };
    return authSuccessResponse(request, env, 200, merged);
  } catch (error) {
    const text = String(error && error.message || "");
    if (/duplicate|409|unique/i.test(text)) {
      return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
    }
    return jsonResponse(request, env, 503, { detail: "Account service is temporarily unavailable." });
  }
}

async function handleEntitlement(request, env) {
  const url = new URL(request.url);
  try {
    const user = await currentUserFromRequest(env, request);
    const reportId = String(url.searchParams.get("report_id") || "").trim();
    const source = String(url.searchParams.get("source") || "catalog").trim() || "catalog";
    const access = await reportAccessForUser(env, user, reportId, source);
    return jsonResponse(request, env, 200, {
      user: publicUser(user),
      ...access,
    });
  } catch (error) {
    return jsonResponse(request, env, 401, { detail: error.message || "Please log in." });
  }
}

function cleanEnv(value) {
  const text = String(value || "").trim();
  return text === "unconfigured" ? "" : text;
}

function paddleClientToken(env) {
  const token = cleanEnv(env.PADDLE_CLIENT_TOKEN);
  return /^(live|test)_[A-Za-z0-9_-]+$/.test(token) ? token : "";
}

function paddleEnv(env, clientToken) {
  const configured = cleanEnv(env.PADDLE_ENV);
  if (clientToken.startsWith("test_")) return "sandbox";
  if (clientToken.startsWith("live_")) return "production";
  return configured || "production";
}

function paddleConfig(env) {
  const cnyCentPrice = cleanEnv(env.PADDLE_PRICE_CNY_CENT);
  const clientToken = paddleClientToken(env);
  return {
    PADDLE_ENV: paddleEnv(env, clientToken),
    PADDLE_CLIENT_TOKEN: clientToken,
    PADDLE_PRICE_CNY_CENT: cnyCentPrice,
    PADDLE_PRICE_REPORT_CNY_CENT: cleanEnv(env.PADDLE_PRICE_REPORT_CNY_CENT) || cnyCentPrice,
    PADDLE_PRICE_YEARLY: cleanEnv(env.PADDLE_PRICE_YEARLY) || cnyCentPrice,
  };
}

function handlePaddleConfig(request, env) {
  return jsonResponse(request, env, 200, {
    config: {},
    missing: ["ACCESS_CHANNEL_DISABLED"],
    disabled: true,
    message: `Self-serve access is paused. Contact WeChat: ${CONTACT_WECHAT}.`,
  });
}

function parsePaddleSignature(header) {
  let timestamp = "";
  const signatures = [];
  for (const part of String(header || "").split(";")) {
    const [key, value] = part.split("=");
    if (!key || !value) continue;
    if (key.trim() === "ts") timestamp = value.trim();
    if (key.trim() === "h1") signatures.push(value.trim());
  }
  return { timestamp, signatures };
}

async function verifyPaddleSignature(env, rawBody, signatureHeader) {
  const secret = cleanEnv(env.PADDLE_WEBHOOK_SECRET);
  if (!secret || !signatureHeader) return false;
  const { timestamp, signatures } = parsePaddleSignature(signatureHeader);
  if (!timestamp || !signatures.length) return false;
  const sentAt = Number(timestamp);
  if (!Number.isFinite(sentAt) || Math.abs(Math.floor(Date.now() / 1000) - sentAt) > 300) return false;
  const expected = await hmacSha256Hex(secret, `${timestamp}:${rawBody}`);
  return signatures.some((signature) => constantTimeEqual(signature, expected));
}

function asObject(value) {
  return value && typeof value === "object" && !Array.isArray(value) ? value : {};
}

function firstText(...values) {
  for (const value of values) {
    if (typeof value === "string" && value.trim()) return value.trim();
  }
  return "";
}

function collectPriceIds(value, found = []) {
  if (Array.isArray(value)) {
    value.forEach((child) => collectPriceIds(child, found));
  } else if (value && typeof value === "object") {
    Object.values(value).forEach((child) => collectPriceIds(child, found));
  } else if (typeof value === "string" && value.startsWith("pri_") && !found.includes(value)) {
    found.push(value);
  }
  return found;
}

function extractPaddleEmail(data, customData) {
  const customer = asObject(data.customer);
  const billing = asObject(data.billing_details);
  return normalizeEmail(firstText(
    customData.email,
    customData.customer_email,
    data.customer_email,
    data.email,
    customer.email,
    billing.email,
  ));
}

function transactionIdForEvent(eventType, data) {
  return eventType.startsWith("transaction.")
    ? firstText(data.id, data.transaction_id)
    : firstText(data.transaction_id);
}

function subscriptionIdForEvent(eventType, data) {
  return eventType.startsWith("subscription.")
    ? firstText(data.id, data.subscription_id)
    : firstText(data.subscription_id);
}

function resolvePaddleStatus(eventType, data) {
  if (eventType === "subscription.canceled") return "canceled";
  if (eventType === "subscription.paused") return "paused";
  if (eventType === "subscription.past_due") return "past_due";
  if (eventType === "subscription.resumed") return "active";
  if (eventType.startsWith("subscription.")) {
    const status = String(data.status || "active").toLowerCase();
    return ACTIVE_STATUSES.has(status) ? "active" : status;
  }
  return "active";
}

function futureIso(days) {
  return new Date(Date.now() + days * 24 * 60 * 60 * 1000).toISOString();
}

function paddlePeriodEnd(plan, data) {
  const period = asObject(data.current_billing_period);
  return firstText(period.ends_at, data.next_billed_at, data.billing_period_end) || (plan === "annual" ? futureIso(365) : null);
}

function requestedPaddlePlan(customData) {
  return firstText(customData.plan, customData.kc_plan, customData.order_plan);
}

async function processPaddleEvent(env, event) {
  const eventType = String(event.event_type || "");
  if (!PADDLE_HANDLED_EVENTS.has(eventType)) return { processed: false, event_type: eventType };

  const data = asObject(event.data);
  const customData = asObject(data.custom_data || data.customData);
  const email = extractPaddleEmail(data, customData);
  const priceIds = collectPriceIds(data);
  const config = paddleConfig(env);
  const reportPrice = config.PADDLE_PRICE_REPORT_CNY_CENT;
  const yearlyPrice = config.PADDLE_PRICE_YEARLY;
  const requestedPlan = requestedPaddlePlan(customData);
  const orderKind = firstText(customData.order_kind, customData.orderKind);

  if (!email) return { processed: false, event_type: eventType, detail: "missing email" };

  const isReportPurchase = eventType === "transaction.completed"
    && reportPrice
    && priceIds.includes(reportPrice)
    && (requestedPlan === "single_report" || orderKind === "report_purchase" || reportPrice !== yearlyPrice);
  if (isReportPurchase) {
    const reportId = firstText(customData.report_id, customData.reportId);
    const source = firstText(customData.source) || "catalog";
    if (!reportId) return { processed: false, event_type: eventType, detail: "missing report id" };
    const saved = await saveReportPurchase(env, {
      email,
      report_id: reportId,
      source,
      title: firstText(customData.title).slice(0, 500),
      status: "active",
      paddle_customer_id: firstText(data.customer_id, customData.paddle_customer_id),
      paddle_transaction_id: transactionIdForEvent(eventType, data),
    });
    await insertUsageEvent(env, email, "report_purchase.completed", {
      event_id: event.event_id,
      report_id: reportId,
      source,
      quantity: Number(customData.quantity || 0) || null,
      price_ids: priceIds,
    });
    return { processed: true, event_type: eventType, email, report_id: saved.report_id, source };
  }

  const isAnnualPurchase = yearlyPrice
    && priceIds.includes(yearlyPrice)
    && (
      requestedPlan === "annual"
      || orderKind === "membership"
      || eventType.startsWith("subscription.")
      || reportPrice !== yearlyPrice
    );
  if (isAnnualPurchase) {
    const status = resolvePaddleStatus(eventType, data);
    const saved = await saveEntitlement(env, email, {
      plan: "annual",
      status,
      lifetime: false,
      paddle_customer_id: firstText(data.customer_id, customData.paddle_customer_id),
      paddle_subscription_id: subscriptionIdForEvent(eventType, data),
      paddle_transaction_id: transactionIdForEvent(eventType, data),
      current_period_end: paddlePeriodEnd("annual", data),
    });
    await insertUsageEvent(env, email, eventType, {
      event_id: event.event_id,
      plan: "annual",
      status,
      quantity: Number(customData.quantity || 0) || null,
      price_ids: priceIds,
    });
    return { processed: true, event_type: eventType, email, plan: saved.plan, status: saved.status };
  }

  await insertUsageEvent(env, email, eventType, {
    event_id: event.event_id,
    processed: false,
    reason: "unrecognized price",
    price_ids: priceIds,
  }).catch(() => {});
  return { processed: false, event_type: eventType, detail: "unrecognized price" };
}

async function handlePaddleWebhook(request, env) {
  const rawBody = await request.text();
  const signatureHeader = request.headers.get("Paddle-Signature") || "";
  if (!(await verifyPaddleSignature(env, rawBody, signatureHeader))) {
    return jsonResponse(request, env, 401, { detail: "Invalid Paddle signature." });
  }
  try {
    const event = JSON.parse(rawBody || "{}");
    const result = await processPaddleEvent(env, event);
    return jsonResponse(request, env, 200, { ok: true, ...result });
  } catch (error) {
    return jsonResponse(request, env, 500, { detail: error.message || "Webhook processing failed." });
  }
}

function safeFilename(value) {
  const filename = String(value || "report.pdf")
    .replace(/[\r\n"\\/:*?<>|]+/g, " ")
    .replace(/\s+/g, " ")
    .trim();
  return filename || "report.pdf";
}

function asciiFilename(value) {
  return safeFilename(value).replace(/[^\x20-\x7e]+/g, "_");
}

function contentDisposition(filename) {
  const safe = safeFilename(filename);
  return `attachment; filename="${asciiFilename(safe)}"; filename*=UTF-8''${encodeURIComponent(safe)}`;
}

function objectKeyForReport(env, id) {
  const prefix = String(env.R2_OBJECT_PREFIX || DEFAULT_R2_PREFIX).replace(/^\/+|\/+$/g, "");
  return prefix ? `${prefix}/${id}.pdf` : `${id}.pdf`;
}

async function handleDownload(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const id = String(payload.id || "").trim();
  const password = String(payload.password || "");
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const accountAllowed = await accountCanDownload(env, request, id, "catalog");
  if (!password && !accountAllowed) {
    return jsonResponse(request, env, 402, { error: "Please log in, purchase this report, or enter the report password." });
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Download service is temporarily unavailable." });
  }

  const report = findReport(catalog, id);
  if (!report) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }
  if (report.available === false) {
    return jsonResponse(request, env, 404, {
      error: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`,
      archived: true,
      contact: CONTACT_WECHAT,
    });
  }

  if (!accountAllowed) {
    let derivedOk = false;
    try {
      derivedOk = await derivedPasswordMatches(env, id, password);
    } catch (_error) {
      derivedOk = false;
    }

    if (!derivedOk) {
      try {
        const rules = await loadRules(env);
        const group = findPasswordGroup(rules, report.password_group || rules.default_group);
        if (!group) {
          return jsonResponse(request, env, 503, { error: "Password validation failed." });
        }
        const ok = await passwordMatches(env, group, password);
        if (!ok) return jsonResponse(request, env, 401, { error: "Password is incorrect." });
      } catch (_error) {
        return jsonResponse(request, env, 503, { error: "Password validation failed." });
      }
    }
  }

  if (!env.REPORT_BUCKET) {
    return jsonResponse(request, env, 503, { error: "Download service is temporarily unavailable." });
  }

  const key = objectKeyForReport(env, id);
  const object = await env.REPORT_BUCKET.get(key);
  if (!object) {
    return jsonResponse(request, env, 404, {
      error: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.`,
      archived: true,
      contact: CONTACT_WECHAT,
    });
  }

  return new Response(object.body, {
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/pdf",
      "Content-Disposition": contentDisposition(report.filename || `${id}.pdf`),
      "Cache-Control": "no-store, private",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

async function handleCalculator(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  const key = String(url.searchParams.get("key") || "");
  if (!env.CALC_KEY) {
    return jsonResponse(request, env, 503, { error: "Calculator key is not configured." });
  }
  if (key !== env.CALC_KEY) {
    return jsonResponse(request, env, 401, { error: "Calculator key is incorrect." });
  }
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  try {
    return jsonResponse(request, env, 200, {
      id,
      password: await derivedReportPassword(env, id),
      rule: "KC-" + "base32(hmac_sha256(PASSWORD_SECRET, 'kc-desk-notes:' + report_id))[0:12] grouped 4-4-4",
    });
  } catch (error) {
    return jsonResponse(request, env, 503, { error: error.message || "Could not calculate password." });
  }
}

async function handleAdminLogin(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const submitted = String(payload.key || "").trim();
  const expected = String(env.MASTER_KEY || "").trim();
  if (!expected) {
    return jsonResponse(request, env, 503, { error: "Private tools are not configured." });
  }
  if (!submitted || !constantTimeEqual(submitted, expected)) {
    return jsonResponse(request, env, 401, { error: "Private key is incorrect." });
  }

  try {
    const now = Math.floor(Date.now() / 1000);
    const expires = now + ADMIN_TOKEN_TTL_SECONDS;
    const token = await signAdminToken(env, { v: 1, iat: now, exp: expires });
    return jsonResponse(request, env, 200, {
      ok: true,
      token,
      expires_in: ADMIN_TOKEN_TTL_SECONDS,
      expires_at: new Date(expires * 1000).toISOString(),
    });
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Private tools are not configured." });
  }
}

async function requireAdminOrSuperUser(request, env, token) {
  let tokenError = null;
  if (token) {
    try {
      await verifyAdminToken(env, token);
      return { kind: "master" };
    } catch (error) {
      tokenError = error;
    }
  }
  try {
    const user = await currentUserFromRequest(env, request);
    if (isSuperAccount(user)) return { kind: "super", user };
  } catch (_error) {
    // Use the token error below when an admin token was supplied.
  }
  if (tokenError) throw tokenError;
  throw new Error("Admin session is invalid.");
}

async function handleAdminReportPassword(request, env) {
  let payload;
  try {
    payload = await request.json();
  } catch (_error) {
    return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
  }

  const id = String(payload.id || "").trim();
  const token = String(payload.token || "");
  const source = String(payload.source || "catalog").trim().toLowerCase();
  if (source === "external") {
    if (!isExternalId(id)) {
      return jsonResponse(request, env, 400, { error: "Invalid report id." });
    }
  } else if (source === AUTHORITY_SOURCE) {
    if (!parseAuthorityId(id)) {
      return jsonResponse(request, env, 400, { error: "Invalid report id." });
    }
  } else if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }

  try {
    await requireAdminOrSuperUser(request, env, token);
  } catch (error) {
    return jsonResponse(request, env, 401, { error: error.message || "Admin session is invalid." });
  }

  if (source === AUTHORITY_SOURCE) {
    return jsonResponse(request, env, 403, {
      error: `高权报告仅提供检索线索，无法生成下载发货链接。请联系 WeChat: ${CONTACT_WECHAT}。`,
      contact: CONTACT_WECHAT,
    });
  }

  if (source === "external") {
    try {
      return jsonResponse(request, env, 200, {
        id,
        source,
        password: await derivedReportPassword(env, id),
      });
    } catch (_error) {
      return jsonResponse(request, env, 503, { error: "Could not calculate report password." });
    }
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Catalog is not configured." });
  }

  const report = findReport(catalog, id);
  if (!report) {
    return jsonResponse(request, env, 404, { error: "Report not found." });
  }

  try {
    return jsonResponse(request, env, 200, {
      id,
      title: report.title || "",
      title_zh: report.title_zh || "",
      available: report.available !== false,
      password: await derivedReportPassword(env, id),
    });
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Could not calculate report password." });
  }
}

async function requireSuperUser(request, env) {
  const user = await currentUserFromRequest(env, request);
  if (!isSuperAccount(user)) throw new Error("Only the admin account can access this area.");
  return user;
}

function adminVisibleUser(user, entitlementRow) {
  const publicInfo = publicUser(user);
  return {
    ...publicInfo,
    last_login_at: user.last_login_at || "",
    entitlement: isSuperAccount(user) ? superEntitlement(user) : publicEntitlement(entitlementRow),
  };
}

function normalizeText(value) {
  return String(value || "")
    .normalize("NFKC")
    .toLowerCase()
    .replace(/[^\p{L}\p{N}]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim();
}

function reportBankLabel(item) {
  const code = String(item.bank_code || "").trim();
  const name = String(item.bank_name || "").trim();
  return code && name && normalizeText(code) !== normalizeText(name) ? `${code} · ${name}` : (code || name || "Other");
}

function reportDisplayTitle(item) {
  return String(item.title_zh || item.title || item.filename || "Untitled report").trim();
}

function reportEnglishTitle(item) {
  return String(item.title || item.filename || "Untitled report").replace(/\.pdf$/i, "").trim();
}

function reportPageCount(item) {
  const pages = Number(item.page_count || 0);
  return Number.isFinite(pages) && pages > 0 ? pages : 0;
}

function reportIsLandscape(item) {
  if (item.first_page_landscape === true) return true;
  return String(item.first_page_orientation || "").toLowerCase() === "landscape";
}

function latestCatalogDateFolder(items) {
  return (items || [])
    .map((item) => String(item.date_folder || ""))
    .filter(Boolean)
    .sort((a, b) => dateScore(b) - dateScore(a) || b.localeCompare(a))[0] || "";
}

const DAILY_PICK_MACRO_KEYWORDS = [
  "macro", "global views", "global economics", "economics", "economic", "economy",
  "strategy", "asset allocation", "rates", "fx", "currency", "currencies", "cny",
  "dollar", "treasury", "bond", "yield", "central bank", "fed", "fomc", "ecb",
  "boj", "boe", "pboc", "inflation", "cpi", "pce", "pmi", "gdp", "recession",
  "policy", "fiscal", "monetary", "liquidity", "commodities", "commodity",
  "oil", "crude", "gold", "geopolitics", "tariff", "trade", "china economy",
  "asia insights", "global markets", "market outlook", "weekly", "monthly",
  "宏观", "央行", "货币政策", "财政", "利率", "汇率", "通胀", "经济", "增长",
  "衰退", "流动性", "大类资产", "资产配置", "地缘", "油价", "黄金", "贸易",
];

const DAILY_PICK_STOCK_PATTERNS = [
  /[（(][0-9]{4,6}\s*\.(?:hk|ss|sz|ch|us|jp|ks|tw|t)[）)]/i,
  /[（(][a-z]{1,6}\s*\.(?:us|o|n|ln|fp|gr|sw|ks|jp|t)[）)]/i,
  /\b(?:upgrade|downgrade|initiat(?:e|ion)|target price|price target|buy|sell|neutral|overweight|underweight)\b/i,
  /\b(?:results|earnings|investor day|valuation|eps|ebitda|revenue)\b/i,
  /公司|个股|目标价|评级|买入|卖出|增持|减持|业绩|财报|估值/,
];

const DAILY_PICK_SECTOR_PATTERN = /\b(?:shipbuilding|semiconductor|internet|media|technology|software|hardware|healthcare|property|real estate|autos?|automobile|retail|consumer|gaming|banks?|insurance|utilities|materials|chemicals?|pharma|biotech|airlines?|restaurants?|power equipment|capital goods|machinery)\b|造船|半导体|互联网|传媒|科技|地产|汽车|零售|消费|银行|保险|医药|航空|机械|电力设备/iu;

const DAILY_PICK_MACRO_ANCHOR_PATTERN = /\b(?:global views|global economics|economic outlook|economics|economy|macro|rates strategy|rates|fx|currency|currencies|central bank|fed|fomc|ecb|boj|boe|pboc|inflation|cpi|pce|pmi|gdp|recession|monetary|fiscal|asset allocation|global markets|market outlook)\b|宏观|央行|货币政策|财政|利率|汇率|通胀|经济展望|大类资产|资产配置|衰退|流动性/iu;

function dailyPickTopicTags(item) {
  const text = normalizeText(`${item.title || ""} ${item.title_zh || ""}`);
  const tags = [];
  const add = (tag) => {
    if (tag && !tags.includes(tag)) tags.push(tag);
  };
  if (/fed|fomc|ecb|boj|boe|pboc|central bank|央行|货币政策/.test(text)) add("央行政策");
  if (/oil|crude|commodity|commodities|gold|energy|油价|原油|黄金|大宗/.test(text)) add("大宗商品");
  if (/china|cny|pboc|中国|人民币/.test(text)) add("中国宏观");
  if (/fx|currency|dollar|usd|汇率|美元|外汇/.test(text)) add("汇率");
  if (/rates|treasury|bond|yield|利率|债券|国债/.test(text)) add("利率");
  if (/strategy|asset allocation|market outlook|global markets|大类资产|资产配置/.test(text)) add("资产配置");
  if (/inflation|cpi|pce|通胀/.test(text)) add("通胀");
  add("宏观趋势");
  const bank = String(item.bank_name || item.bank_code || "").replace(/\s+/g, "").trim();
  if (bank && bank.length <= 12) add(bank);
  return tags.slice(0, 4);
}

function dailyPickMacroScore(item) {
  const raw = `${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`;
  const text = normalizeText(raw);
  let score = 0;
  for (const keyword of DAILY_PICK_MACRO_KEYWORDS) {
    if (text.includes(normalizeText(keyword))) score += keyword.length > 8 ? 12 : 8;
  }
  if (/\b(?:global views|asia insights|economic|economics|macro|strategy)\b/i.test(raw)) score += 22;
  if (/宏观|经济|策略|大类资产|央行/.test(raw)) score += 18;
  if (DAILY_PICK_SECTOR_PATTERN.test(raw) && !DAILY_PICK_MACRO_ANCHOR_PATTERN.test(raw)) score -= 42;
  if (reportIsLandscape(item)) score += 120;
  const pages = reportPageCount(item);
  if (pages > 5) score += Math.min(28, pages);
  if (!pages) score -= 8;
  return score;
}

function isLikelySingleStockReport(item) {
  const text = `${item.title || ""} ${item.title_zh || ""} ${item.filename || ""}`;
  return DAILY_PICK_STOCK_PATTERNS.some((pattern) => pattern.test(text));
}

function dailyPickIntro(item, tags) {
  const bank = String(item.bank_name || item.bank_code || "机构").trim();
  const title = reportDisplayTitle(item);
  const topicText = tags.filter((tag) => tag !== bank && tag !== "宏观趋势").slice(0, 3).join("、") || "全球宏观趋势、政策变化与资产市场";
  const landscapeText = reportIsLandscape(item) ? "这份 PDF 为横屏呈现，适合直接做会议讨论或素材摘图。" : "";
  const pageText = reportPageCount(item) ? `报告共 ${reportPageCount(item)} 页，` : "";
  const tagLinks = tags
    .map((tag) => `[#${tag}](https://wx.zsxq.com/tags/${encodeURIComponent(tag)})`)
    .join("  ");
  return `${bank}报告《${title}》是对${topicText}的更新。${pageText}核心适合关注宏观主线、政策预期和市场定价变化的读者快速把握当日信息。${landscapeText}\n${tagLinks}`.trim();
}

function selectDailyPicks(catalog, maxItems = 5) {
  const items = Array.isArray(catalog && catalog.items) ? catalog.items : [];
  const latestDate = latestCatalogDateFolder(items);
  if (!latestDate) return [];
  const candidates = items
    .filter((item) => String(item.date_folder || "") === latestDate)
    .filter((item) => item && item.available !== false)
    .filter((item) => !isLikelySingleStockReport(item))
    .map((item) => {
      const score = dailyPickMacroScore(item);
      const pages = reportPageCount(item);
      const landscape = reportIsLandscape(item);
      const pageEligible = pages > 5 || pages === 0 || landscape;
      return { item, score, pages, landscape, pageEligible };
    })
    .filter((entry) => entry.pageEligible && (entry.landscape || entry.score > 0))
    .sort((a, b) => {
      if (a.landscape !== b.landscape) return a.landscape ? -1 : 1;
      if (b.score !== a.score) return b.score - a.score;
      if (b.pages !== a.pages) return b.pages - a.pages;
      return String(b.item.client_modified || b.item.server_modified || "").localeCompare(String(a.item.client_modified || a.item.server_modified || ""));
    })
    .slice(0, maxItems);

  return candidates.map(({ item, score, pages, landscape }) => {
    const tags = dailyPickTopicTags(item);
    return {
      id: String(item.id || ""),
      title: reportEnglishTitle(item),
      title_zh: String(item.title_zh || ""),
      display_title: reportDisplayTitle(item),
      filename: item.filename || `${reportEnglishTitle(item)}.pdf`,
      bank: reportBankLabel(item),
      date_folder: latestDate,
      page_count: pages,
      first_page_orientation: String(item.first_page_orientation || ""),
      first_page_landscape: landscape,
      size_bytes: Number(item.size_bytes || 0) || 0,
      score,
      tags,
      intro: dailyPickIntro(item, tags),
    };
  });
}

async function listR2JsonObjects(env, prefix, limit = 500) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return [];
  const rows = [];
  let cursor = undefined;
  while (rows.length < limit) {
    const listed = await env.REPORT_BUCKET.list({
      prefix,
      limit: Math.min(1000, Math.max(1, limit - rows.length)),
      cursor,
    });
    const objects = Array.isArray(listed && listed.objects) ? listed.objects : [];
    const batch = await Promise.all(objects.map(async (object) => safeR2GetJson(env, object.key)));
    for (const row of batch) {
      if (row && typeof row === "object") rows.push(row);
      if (rows.length >= limit) break;
    }
    if (!listed || !listed.truncated || !listed.cursor) break;
    cursor = listed.cursor;
  }
  return rows;
}

async function listSiteUsers(env) {
  if (hasSupabaseConfig(env)) {
    try {
      const query = queryString({
        select: "id,username,email,email_is_generated,created_at,updated_at,last_login_at",
        order: "updated_at.desc",
        limit: "500",
      });
      const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
      if (Array.isArray(rows)) return rows;
    } catch (_error) {
      // Fall through to the R2 mirror.
    }
  }
  const rows = await listR2JsonObjects(env, accountKey("users", "id", ""), 500);
  return rows.sort((a, b) => String(b.updated_at || "").localeCompare(String(a.updated_at || "")));
}

async function listEntitlementRows(env) {
  if (hasSupabaseConfig(env)) {
    try {
      const query = queryString({
        select: "email,plan,status,lifetime,current_period_end,updated_at",
        order: "updated_at.desc",
        limit: "1000",
      });
      const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
      if (Array.isArray(rows)) return rows;
    } catch (_error) {
      // Fall through to R2.
    }
  }
  return listR2JsonObjects(env, accountKey("entitlements", ""), 1000);
}

function entitlementMap(rows) {
  const mapped = new Map();
  for (const row of rows || []) {
    const email = normalizeEmail(row && row.email);
    if (email && !mapped.has(email)) mapped.set(email, row);
  }
  return mapped;
}

function githubRepo(env) {
  return cleanEnv(env.GH_REPO) || cleanEnv(env.GITHUB_REPO) || DEFAULT_GITHUB_REPO;
}

function githubRef(env, repo = githubRepo(env)) {
  if (repo === BBG_SHOW_REPO) return DEFAULT_GITHUB_REF;
  const configured = cleanEnv(env.GH_REF) || cleanEnv(env.GITHUB_BRANCH) || cleanEnv(env.GITHUB_REF);
  if (!configured) return DEFAULT_GITHUB_REF;
  return configured.startsWith("refs/heads/") ? configured.slice("refs/heads/".length) : configured;
}

function githubToken(env, repo = githubRepo(env)) {
  const readToken = cleanEnv(env.GH_READ_TOKEN) || cleanEnv(env.GITHUB_TOKEN) || cleanEnv(env.GH_TOKEN);
  if (readToken) return readToken;
  return repo === githubRepo(env) ? cleanEnv(env.GH_DISPATCH_TOKEN) : "";
}

function githubHeaders(env, extra = {}, repo = githubRepo(env)) {
  const token = githubToken(env, repo);
  const headers = {
    "Accept": "application/vnd.github+json",
    "User-Agent": "kc-desk-notes-worker",
    "X-GitHub-Api-Version": "2022-11-28",
    ...extra,
  };
  if (token) headers.Authorization = `Bearer ${token}`;
  return headers;
}

function encodeGithubPath(path) {
  return String(path || "").split("/").filter(Boolean).map(encodeURIComponent).join("/");
}

async function githubApiFetch(env, path, init = {}, repo = githubRepo(env)) {
  const response = await fetch(`https://api.github.com/repos/${repo}${path}`, {
    ...init,
    headers: githubHeaders(env, init.headers || {}, repo),
    redirect: init.redirect || "follow",
  });
  if (!response.ok) {
    const text = await response.text().catch(() => "");
    throw new Error(`GitHub API ${response.status}: ${text.slice(0, 200)}`);
  }
  return response;
}

async function githubApiJson(env, path, init = {}, repo = githubRepo(env)) {
  return (await githubApiFetch(env, path, init, repo)).json();
}

async function githubContents(env, path, repo = githubRepo(env), ref = githubRef(env, repo)) {
  const encoded = encodeGithubPath(path);
  const suffix = encoded ? `/contents/${encoded}` : "/contents";
  const query = `?ref=${encodeURIComponent(ref)}`;
  const data = await githubApiJson(env, `${suffix}${query}`, {}, repo);
  return Array.isArray(data) ? data : [];
}

function dateScore(value) {
  const text = String(value || "");
  const iso = text.match(/(20\d{2})-(\d{2})-(\d{2})/);
  if (iso) return Number(`${iso[1]}${iso[2]}${iso[3]}`);
  const match = text.match(/(\d{8}|\d{6})/);
  if (!match) return 0;
  const digits = match[1];
  return digits.length === 6 ? Number(`20${digits}`) : Number(digits);
}

function sortGithubDirsDesc(items) {
  return (items || [])
    .filter((item) => item && item.type === "dir")
    .sort((a, b) => {
      const score = dateScore(b.name || b.path) - dateScore(a.name || a.path);
      if (score) return score;
      return String(b.name || "").localeCompare(String(a.name || ""));
    });
}

function adminGithubFile(kind, label, item, date, note = "", repo = "") {
  return {
    type: "file",
    kind,
    label,
    name: item.name || item.path.split("/").pop(),
    path: item.path,
    size_bytes: Number(item.size || 0),
    date: date || "",
    note,
    repo,
  };
}

async function githubRecursiveTree(env, repo, ref = githubRef(env, repo)) {
  const data = await githubApiJson(env, `/git/trees/${encodeURIComponent(ref)}?recursive=1`, {}, repo);
  return Array.isArray(data && data.tree) ? data.tree : [];
}

async function latestMarketViewFiles(env, maxItems = 3) {
  const results = [];
  const dateDirs = sortGithubDirsDesc(await githubContents(env, "market_view_summaries"));
  for (const dateDir of dateDirs.slice(0, 20)) {
    const files = await githubContents(env, dateDir.path);
    const pdfs = files
      .filter((item) => item.type === "file" && /^market_views_.*\.pdf$/i.test(item.name || ""))
      .sort((a, b) => String(b.name || "").localeCompare(String(a.name || "")));
    for (const pdf of pdfs) {
      results.push(adminGithubFile("market-views", "Market Views PDF", pdf, dateDir.name));
      if (results.length >= maxItems) return results;
    }
  }
  return results;
}

function preferredVideoItem(items) {
  const files = (items || []).filter((item) => item.type === "file" && /\.mp4$/i.test(item.name || ""));
  const preferred = [
    "podcast_mixed_bilingual_explainer.mp4",
    "podcast_en_explainer.mp4",
    "podcast_zh_explainer.mp4",
  ];
  for (const name of preferred) {
    const item = files.find((file) => String(file.name || "").toLowerCase() === name);
    if (item) return item;
  }
  return files[0] || null;
}

function titleFromGeneratedPath(path) {
  const parts = String(path || "").split("/");
  const folder = parts.length >= 4 ? parts[3] : parts[parts.length - 2] || "";
  return folder.replace(/^\d{4}-/, "").replace(/[-_]+/g, " ").slice(0, 120);
}

function renderedClipDate(path) {
  const match = String(path || "").match(/^rendered-clips\/(20\d{2}-\d{2}-\d{2})\//);
  return match ? match[1] : "";
}

function renderedClipNote(path) {
  const parts = String(path || "").split("/");
  return parts.length > 3 ? parts.slice(2, -1).join(" / ").replace(/[-_]+/g, " ") : "";
}

async function latestBbgRenderedClipFiles(env, maxItems = 8) {
  const tree = await githubRecursiveTree(env, BBG_SHOW_REPO);
  const dated = tree
    .filter((item) => item && item.type === "blob" && /^rendered-clips\/20\d{2}-\d{2}-\d{2}\/.+\.mp4$/i.test(item.path || ""))
    .sort((a, b) => {
      const score = dateScore(b.path) - dateScore(a.path);
      if (score) return score;
      return String(b.path || "").localeCompare(String(a.path || ""));
    })
    .slice(0, maxItems);
  return dated.map((item) => adminGithubFile(
    "bbg-show",
    "BBG Show 视频",
    {
      name: String(item.path || "").split("/").pop(),
      path: item.path,
      size: item.size,
    },
    renderedClipDate(item.path),
    renderedClipNote(item.path),
    BBG_SHOW_REPO,
  ));
}

async function latestSiteVideoFiles(env, maxItems = 6) {
  const results = [];
  const dateDirs = sortGithubDirsDesc(await githubContents(env, "bilingual_podcast_videos"));
  for (const dateDir of dateDirs.slice(0, 12)) {
    const runDirs = sortGithubDirsDesc(await githubContents(env, dateDir.path))
      .sort((a, b) => Number(b.name || 0) - Number(a.name || 0));
    for (const runDir of runDirs.slice(0, 8)) {
      const reportDirs = sortGithubDirsDesc(await githubContents(env, runDir.path));
      for (const reportDir of reportDirs) {
        const files = await githubContents(env, reportDir.path);
        const video = preferredVideoItem(files);
        if (!video) continue;
        results.push(adminGithubFile("site-video", "站内视频", video, dateDir.name, titleFromGeneratedPath(video.path), githubRepo(env)));
        if (results.length >= maxItems) return results;
      }
    }
  }
  return results;
}

function adminGithubArtifact(artifact) {
  const name = String(artifact.name || "");
  let kind = "artifact";
  let label = "GitHub Artifact";
  if (/bilingual-podcast-videos/i.test(name)) {
    kind = "site-video";
    label = "站内视频 artifact";
  } else if (/market-views-pdf/i.test(name)) {
    kind = "market-views";
    label = "Market Views PDF artifact";
  }
  return {
    type: "artifact",
    kind,
    label,
    id: String(artifact.id || ""),
    name,
    size_bytes: Number(artifact.size_in_bytes || 0),
    date: String(artifact.created_at || "").slice(0, 10),
    note: "artifact zip",
  };
}

async function latestGithubArtifacts(env) {
  try {
    const data = await githubApiJson(env, "/actions/artifacts?per_page=60");
    const artifacts = Array.isArray(data && data.artifacts) ? data.artifacts : [];
    return artifacts
      .filter((artifact) => !artifact.expired && /bilingual-podcast-videos|market-views-pdf/i.test(String(artifact.name || "")))
      .map(adminGithubArtifact);
  } catch (_error) {
    return [];
  }
}

async function latestAdminGithubFiles(env) {
  const [bbg, market, siteVideos] = await Promise.all([
    latestBbgRenderedClipFiles(env).catch(() => []),
    latestMarketViewFiles(env).catch(() => []),
    latestSiteVideoFiles(env).catch(() => []),
  ]);
  const artifacts = await latestGithubArtifacts(env);
  const fallback = [];
  if (!market.length) fallback.push(...artifacts.filter((item) => item.kind === "market-views").slice(0, 3));
  if (!siteVideos.length) fallback.push(...artifacts.filter((item) => item.kind === "site-video").slice(0, 3));
  return [...bbg, ...market, ...fallback, ...siteVideos];
}

async function handleAccountAdminSummary(request, env, ctx = null) {
  try {
    const adminUser = await requireSuperUser(request, env);
    const [users, entitlements, files, catalog] = await Promise.all([
      listSiteUsers(env),
      listEntitlementRows(env),
      latestAdminGithubFiles(env),
      loadCatalog(env).catch(() => ({ items: [] })),
    ]);
    const entitlementsByEmail = entitlementMap(entitlements);
    const dailyPicks = selectDailyPicks(catalog);
    if (ctx && typeof ctx.waitUntil === "function") {
      ctx.waitUntil(warmAdminGithubCache(env, files).catch(() => null));
    }
    return jsonResponse(request, env, 200, {
      user: publicUser(adminUser),
      users: users.map((user) => adminVisibleUser(user, entitlementsByEmail.get(normalizeEmail(user.email)))),
      files,
      daily_picks: dailyPicks,
      repo: githubRepo(env),
      ref: githubRef(env),
      generated_at: new Date().toISOString(),
    });
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
}

async function handleAccountAdminReportPdf(request, env) {
  try {
    await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }

  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { detail: "Report id is invalid." });
  }
  if (!env.REPORT_BUCKET) {
    return jsonResponse(request, env, 503, { detail: "Report storage is unavailable." });
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { detail: "Catalog is unavailable." });
  }
  const report = findReport(catalog, id);
  if (!report) return jsonResponse(request, env, 404, { detail: "Report not found." });
  if (report.available === false) {
    return jsonResponse(request, env, 404, { detail: `PDF is not currently available. Contact WeChat: ${CONTACT_WECHAT}.` });
  }

  const object = await env.REPORT_BUCKET.get(objectKeyForReport(env, id));
  if (!object) return jsonResponse(request, env, 404, { detail: "Report PDF was not found in storage." });
  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": "application/pdf",
    "Content-Disposition": contentDisposition(report.filename || `${id}.pdf`),
    "Content-Length": String(object.size || ""),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
  };
  return new Response(object.body, { headers });
}

function githubFileRepo(env, file) {
  return normalizeGithubRepoParam(env, file && file.repo || "");
}

function fileDateScoreFromPath(path) {
  return dateScore(path);
}

function retentionCutoffDateScore(now = Date.now()) {
  return Number(new Date(now - GITHUB_CACHE_RETENTION_MS).toISOString().slice(0, 10).replace(/-/g, ""));
}

function normalizeGithubRepoParam(env, value) {
  const repo = String(value || githubRepo(env)).trim();
  if (repo === githubRepo(env) || repo === DEFAULT_GITHUB_REPO) return githubRepo(env);
  if (repo === BBG_SHOW_REPO) return BBG_SHOW_REPO;
  return "";
}

function isAllowedAdminGithubFile(env, repo, path) {
  const clean = String(path || "").replace(/^\/+/, "");
  if (clean.includes("..")) return false;
  if (repo === BBG_SHOW_REPO) return /^rendered-clips\/.+\.mp4$/i.test(clean);
  if (/^bilingual_podcast_videos\/.+\.mp4$/i.test(clean)) return true;
  if (/^market_view_summaries\/.+\.pdf$/i.test(clean)) return true;
  return false;
}

function contentTypeForGithubPath(path) {
  if (/\.mp4$/i.test(path)) return "video/mp4";
  if (/\.pdf$/i.test(path)) return "application/pdf";
  return "application/octet-stream";
}

async function githubCacheKey(repo, ref, path) {
  const digest = await sha256Hex(`github-file:${repo}:${ref}:${path}`);
  const filename = String(path || "").split("/").pop() || "download";
  return `${GITHUB_CACHE_PREFIX}/${digest}/${filename}`;
}

async function githubCacheExists(env, cacheKey) {
  if (!env.REPORT_BUCKET) return false;
  try {
    if (typeof env.REPORT_BUCKET.head === "function") {
      return Boolean(await env.REPORT_BUCKET.head(cacheKey));
    }
    return Boolean(await env.REPORT_BUCKET.get(cacheKey));
  } catch (_error) {
    return false;
  }
}

async function cacheGithubFile(env, file) {
  if (!env.REPORT_BUCKET || !file || file.type !== "file") return { ok: false, skipped: true };
  const repo = githubFileRepo(env, file);
  const path = String(file.path || "").replace(/^\/+/, "");
  if (!repo || !isAllowedAdminGithubFile(env, repo, path)) return { ok: false, skipped: true };
  const ref = githubRef(env, repo);
  const cacheKey = await githubCacheKey(repo, ref, path);
  if (await githubCacheExists(env, cacheKey)) return { ok: true, cached: true, key: cacheKey };

  const encodedPath = encodeGithubPath(path);
  const rawUrl = `https://raw.githubusercontent.com/${repo}/${encodeURIComponent(ref)}/${encodedPath}`;
  let response = await fetch(rawUrl, {
    headers: githubHeaders(env, { "Accept": "*/*" }, repo),
    redirect: "follow",
  });
  if (response.status === 404 && githubToken(env, repo)) {
    const metadata = await githubApiJson(env, `/contents/${encodedPath}?ref=${encodeURIComponent(ref)}`, {}, repo);
    const downloadUrl = String(metadata && metadata.download_url || "");
    if (downloadUrl) {
      response = await fetch(downloadUrl, {
        headers: githubHeaders(env, { "Accept": "*/*" }, repo),
        redirect: "follow",
      });
    }
  }
  if (!response.ok || !response.body) return { ok: false, status: response.status };

  await env.REPORT_BUCKET.put(cacheKey, response.body, {
    httpMetadata: {
      contentType: response.headers.get("Content-Type") || contentTypeForGithubPath(path),
      contentDisposition: contentDisposition(path.split("/").pop() || "download"),
    },
    customMetadata: {
      repo,
      ref,
      path: path.slice(0, 900),
      cached_at: new Date().toISOString(),
      file_date: String(file.date || renderedClipDate(path) || "").slice(0, 40),
    },
  });
  return { ok: true, cached: false, key: cacheKey };
}

async function pruneGithubCache(env, now = Date.now()) {
  if (!env.REPORT_BUCKET || typeof env.REPORT_BUCKET.list !== "function") return { deleted: 0 };
  const cutoffTime = now - GITHUB_CACHE_RETENTION_MS;
  const cutoffDate = retentionCutoffDateScore(now);
  let cursor = undefined;
  let deleted = 0;
  do {
    const listed = await env.REPORT_BUCKET.list({
      prefix: `${GITHUB_CACHE_PREFIX}/`,
      limit: 1000,
      cursor,
      include: ["customMetadata"],
    });
    const objects = Array.isArray(listed && listed.objects) ? listed.objects : [];
    for (const object of objects) {
      const metadata = object.customMetadata || {};
      const pathScore = fileDateScoreFromPath(metadata.path || object.key || "");
      const cachedAt = Date.parse(metadata.cached_at || object.uploaded || "");
      const tooOldByFileDate = pathScore && pathScore < cutoffDate;
      const tooOldByCacheDate = Number.isFinite(cachedAt) && cachedAt < cutoffTime;
      if (tooOldByFileDate || tooOldByCacheDate) {
        try {
          await env.REPORT_BUCKET.delete(object.key);
          deleted += 1;
        } catch (_error) {
          // Best-effort cleanup.
        }
      }
    }
    cursor = listed && listed.truncated ? listed.cursor : undefined;
  } while (cursor);
  return { deleted };
}

async function warmAdminGithubCache(env, files = null) {
  const targetFiles = Array.isArray(files) ? files : await latestAdminGithubFiles(env);
  const warmed = [];
  for (const file of targetFiles.filter((item) => item && item.type === "file").slice(0, 18)) {
    try {
      warmed.push(await cacheGithubFile(env, file));
    } catch (error) {
      warmed.push({ ok: false, error: String(error && error.message || error || "cache failed").slice(0, 200) });
    }
  }
  const cleanup = await pruneGithubCache(env).catch((error) => ({ deleted: 0, error: String(error && error.message || error || "") }));
  return {
    warmed,
    cleanup,
    generated_at: new Date().toISOString(),
  };
}

function cachedGithubResponse(request, env, object, path) {
  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": object.httpMetadata && object.httpMetadata.contentType || contentTypeForGithubPath(path),
    "Content-Disposition": contentDisposition(path.split("/").pop() || "download"),
    "Content-Length": String(object.size || ""),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
    "X-KCDesk-Cache": "R2",
  };
  return new Response(object.body, { headers });
}

async function fetchGithubRawFile(env, path, request, repo = githubRepo(env), ctx = null) {
  const ref = githubRef(env, repo);
  const encodedPath = encodeGithubPath(path);
  const cacheKey = await githubCacheKey(repo, ref, path);
  const range = request.headers.get("Range") || request.headers.get("range") || "";
  if (!range && env.REPORT_BUCKET) {
    try {
      const cached = await env.REPORT_BUCKET.get(cacheKey);
      if (cached) return cachedGithubResponse(request, env, cached, path);
    } catch (_error) {
      // Fall through to GitHub.
    }
  }

  const rawUrl = `https://raw.githubusercontent.com/${repo}/${encodeURIComponent(ref)}/${encodedPath}`;
  const headers = githubHeaders(env, { "Accept": "*/*" }, repo);
  if (range) headers.Range = range;
  let response = await fetch(rawUrl, { headers, redirect: "follow" });
  if (response.status === 404 && githubToken(env, repo)) {
    const metadata = await githubApiJson(env, `/contents/${encodedPath}?ref=${encodeURIComponent(ref)}`, {}, repo);
    const downloadUrl = String(metadata && metadata.download_url || "");
    if (downloadUrl) response = await fetch(downloadUrl, { headers, redirect: "follow" });
  }

  if (!range && response.ok && response.body && env.REPORT_BUCKET && ctx && typeof ctx.waitUntil === "function") {
    const [clientBody, cacheBody] = response.body.tee();
    const contentType = response.headers.get("Content-Type") || contentTypeForGithubPath(path);
    ctx.waitUntil(env.REPORT_BUCKET.put(cacheKey, cacheBody, {
      httpMetadata: {
        contentType,
        contentDisposition: contentDisposition(path.split("/").pop() || "download"),
      },
      customMetadata: {
        repo,
        ref,
        path: path.slice(0, 900),
        cached_at: new Date().toISOString(),
      },
    }).catch(() => null));
    return new Response(clientBody, {
      status: response.status,
      statusText: response.statusText,
      headers: response.headers,
    });
  }
  return response;
}

async function handleAccountAdminGithubFile(request, env, ctx = null) {
  try {
    await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  const url = new URL(request.url);
  const path = String(url.searchParams.get("path") || "").replace(/^\/+/, "");
  const repo = normalizeGithubRepoParam(env, url.searchParams.get("repo") || "");
  if (!repo || !isAllowedAdminGithubFile(env, repo, path)) {
    return jsonResponse(request, env, 400, { detail: "File path is not allowed." });
  }
  let upstream;
  try {
    upstream = await fetchGithubRawFile(env, path, request, repo, ctx);
  } catch (_error) {
    return jsonResponse(request, env, 502, { detail: "GitHub file download is unavailable." });
  }
  if (!upstream.ok && upstream.status !== 206) {
    return jsonResponse(request, env, upstream.status === 404 ? 404 : 502, { detail: "GitHub file was not found." });
  }

  const headers = {
    ...corsHeaders(request, env),
    "Content-Type": upstream.headers.get("Content-Type") || contentTypeForGithubPath(path),
    "Content-Disposition": contentDisposition(path.split("/").pop() || "download"),
    "Cache-Control": "no-store, private",
    "X-Content-Type-Options": "nosniff",
  };
  for (const name of ["Content-Length", "Content-Range", "Accept-Ranges"]) {
    const value = upstream.headers.get(name);
    if (value) headers[name] = value;
  }
  return new Response(upstream.body, {
    status: upstream.status,
    headers,
  });
}

async function handleAccountAdminGithubArtifact(request, env) {
  try {
    await requireSuperUser(request, env);
  } catch (error) {
    return jsonResponse(request, env, 403, { detail: error.message || "Admin access denied." });
  }
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!/^\d+$/.test(id)) return jsonResponse(request, env, 400, { detail: "Artifact id is invalid." });
  let upstream;
  try {
    upstream = await githubApiFetch(env, `/actions/artifacts/${encodeURIComponent(id)}/zip`, {
      headers: { "Accept": "application/vnd.github+json" },
      redirect: "follow",
    });
  } catch (_error) {
    return jsonResponse(request, env, 502, { detail: "GitHub artifact download is unavailable." });
  }
  return new Response(upstream.body, {
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/zip",
      "Content-Disposition": contentDisposition(`github-artifact-${id}.zip`),
      "Cache-Control": "no-store, private",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

// ---------------------------------------------------------------------------
// External report integration
// ---------------------------------------------------------------------------

function externalHeaders() {
  return {
    "User-Agent": EXTERNAL_UA,
    "Referer": `${EXTERNAL_SITE}/`,
    "Accept": "application/json",
  };
}

function externalObjectKey(id) {
  return `${EXTERNAL_R2_PREFIX}/${id}.pdf`;
}

function externalStatusKey(id) {
  return `${EXTERNAL_STATUS_PREFIX}/${id}.json`;
}

function isExternalId(value) {
  return /^[0-9]{6,25}$/.test(String(value || "").trim());
}

async function externalStoredStatus(env, id) {
  if (!env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(externalStatusKey(id));
    if (!object) return null;
    const data = JSON.parse(await object.text());
    return data && typeof data === "object" ? data : null;
  } catch (_error) {
    return null;
  }
}

async function externalPutStatus(env, id, status, message = "") {
  if (!env.REPORT_BUCKET) return;
  try {
    await env.REPORT_BUCKET.put(externalStatusKey(id), JSON.stringify({
      id,
      status,
      message: String(message || "").slice(0, 500),
      updated_at: new Date().toISOString(),
    }), {
      httpMetadata: {
        contentType: "application/json; charset=utf-8",
        cacheControl: "no-store",
      },
    });
  } catch (_error) {
    // Status files are best-effort; the PDF path remains the source of truth.
  }
}

function externalIsoDate(publishAt) {
  const ms = Number(publishAt || 0);
  if (!ms) return "";
  try {
    return new Date(ms).toISOString().slice(0, 10);
  } catch (_error) {
    return "";
  }
}

// Map a raw upstream report record to the slim shape the frontend renders.
function slimExternalItem(item) {
  const title = String(item.title || item.title_cn || "").trim();
  const summary = String(item.summary || "").replace(/\s+/g, " ").trim();
  return {
    id: String(item.report_id || ""),
    title: title || "Untitled report",
    title_cn: String(item.title_cn || "").trim(),
    institution: String(item.institution_name || item.channel_name || "").trim(),
    date: externalIsoDate(item.publish_at),
    file_type: String(item.file_type || "").trim(),
    summary: summary.length > 220 ? `${summary.slice(0, 220)}…` : summary,
  };
}

async function handleExternalSearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) {
    return jsonResponse(request, env, 200, { items: [], page: 1, total_page: 0 });
  }

  const target = new URL(`${EXTERNAL_API}/reports`);
  target.searchParams.set("query", query);
  target.searchParams.set("page_num", String(page));
  target.searchParams.set("page_size", String(EXTERNAL_SEARCH_PAGE_SIZE));

  let data;
  try {
    const upstream = await fetch(target.toString(), { headers: externalHeaders() });
    if (!upstream.ok) {
      return jsonResponse(request, env, 502, { error: "Search is unavailable." });
    }
    data = await upstream.json();
  } catch (_error) {
    return jsonResponse(request, env, 502, { error: "Search is unavailable." });
  }

  const items = Array.isArray(data.items) ? data.items.map(slimExternalItem).filter((it) => it.id) : [];
  return jsonResponse(request, env, 200, {
    items,
    page: Number(data.page_num || page),
    total_page: Number(data.total_page || 0),
  });
}

// Fetch the upstream detail and, if the report is directly readable, return its
// presigned PDF url. Returns "" when the PDF is gated (needs a browser grab).
async function externalDirectPdfUrl(id) {
  try {
    const resp = await fetch(`${EXTERNAL_API}/reports/${id}`, { headers: externalHeaders() });
    if (!resp.ok) return { url: "", title: "" };
    const data = await resp.json();
    const main = data.main || {};
    return { url: String(main.url_pdf || "").trim(), title: String(main.title || main.title_cn || "").trim() };
  } catch (_error) {
    return { url: "", title: "" };
  }
}

function externalPdfResponse(request, env, body, title, id) {
  return new Response(body, {
    headers: {
      ...corsHeaders(request, env),
      "Content-Type": "application/pdf",
      "Content-Disposition": contentDisposition(`${title || id}.pdf`),
      "Cache-Control": "no-store, private",
      "X-Content-Type-Options": "nosniff",
    },
  });
}

// Ask GitHub to run the external grab workflow for a gated report. Returns true
// when the dispatch was accepted (HTTP 204).
async function triggerExternalGrab(env, id) {
  const repo = String(env.GH_REPO || "").trim();
  const token = String(env.GH_DISPATCH_TOKEN || "").trim();
  if (!repo || !token || token === "unconfigured") return false;
  try {
    const resp = await fetch(`https://api.github.com/repos/${repo}/dispatches`, {
      method: "POST",
      headers: {
        "Authorization": `Bearer ${token}`,
        "Accept": "application/vnd.github+json",
        "Content-Type": "application/json",
        "User-Agent": "kc-desk-notes-worker",
        "X-GitHub-Api-Version": "2022-11-28",
      },
      body: JSON.stringify({ event_type: "report" + "ify-grab", client_payload: { id } }),
    });
    return resp.ok;
  } catch (_error) {
    return false;
  }
}

async function handleExternalPdf(request, env) {
  const url = new URL(request.url);
  let payload = {};
  if (request.method === "POST") {
    try {
      payload = await request.json();
    } catch (_error) {
      return jsonResponse(request, env, 400, { error: "Invalid JSON body." });
    }
  }
  const id = String(payload.id || url.searchParams.get("id") || "").trim();
  const password = String(payload.password || url.searchParams.get("password") || "");
  if (!isExternalId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  const accountAllowed = await accountCanDownload(env, request, id, "external");
  if (!password && !accountAllowed) {
    return jsonResponse(request, env, 402, { error: "Please log in, purchase this report, or enter the report password." });
  }
  if (!accountAllowed && !(await sharedReportPasswordMatches(env, id, password))) {
    return jsonResponse(request, env, 401, { error: "Password is incorrect." });
  }

  // 1) Directly readable reports expose a presigned PDF url - stream it (instant).
  const direct = await externalDirectPdfUrl(id);
  if (direct.url) {
    try {
      const pdf = await fetch(direct.url, { headers: { "User-Agent": EXTERNAL_UA } });
      if (pdf.ok) {
        return externalPdfResponse(request, env, pdf.body, direct.title, id);
      }
    } catch (_error) {
      // Fall through to the R2 / grab paths below.
    }
  }

  // 2) Already grabbed by the workflow and mirrored to R2.
  if (env.REPORT_BUCKET) {
    const object = await env.REPORT_BUCKET.get(externalObjectKey(id));
    if (object) {
      return externalPdfResponse(request, env, object.body, direct.title, id);
    }
  }

  // 3) Gated and not yet mirrored - request preparation and let the page poll.
  await externalPutStatus(env, id, "queued");
  const dispatched = await triggerExternalGrab(env, id);
  if (!dispatched) {
    await externalPutStatus(env, id, "failed", "dispatch failed");
    return jsonResponse(request, env, 503, {
      error: `文件准备服务暂时不可用，请联系 WeChat: ${CONTACT_WECHAT}。`,
    });
  }
  return jsonResponse(request, env, 202, {
    status: "pending",
    wait_seconds: 480,
  });
}

async function handleExternalStatus(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!isExternalId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  let ready = false;
  if (env.REPORT_BUCKET) {
    const head = await env.REPORT_BUCKET.head(externalObjectKey(id));
    ready = Boolean(head);
  }
  if (ready) return jsonResponse(request, env, 200, { ready, status: "ready" });

  const stored = await externalStoredStatus(env, id);
  if (stored && stored.status === "failed") {
    return jsonResponse(request, env, 200, {
      ready: false,
      status: "failed",
      message: `报告准备失败，请联系 ${CONTACT_WECHAT}。`,
      updated_at: String(stored.updated_at || ""),
    });
  }
  return jsonResponse(request, env, 200, {
    ready: false,
    status: stored && stored.status ? String(stored.status) : "pending",
    updated_at: stored && stored.updated_at ? String(stored.updated_at) : "",
  });
}

// ---------------------------------------------------------------------------
// Hibor metadata integration
// ---------------------------------------------------------------------------

function decodeHtmlEntities(value) {
  const named = {
    amp: "&",
    lt: "<",
    gt: ">",
    quot: "\"",
    apos: "'",
    nbsp: " ",
    middot: "·",
  };
  return String(value || "")
    .replace(/&#x([0-9a-f]+);/gi, (_all, hex) => {
      const code = Number.parseInt(hex, 16);
      return Number.isFinite(code) ? String.fromCodePoint(code) : "";
    })
    .replace(/&#(\d+);/g, (_all, digits) => {
      const code = Number.parseInt(digits, 10);
      return Number.isFinite(code) ? String.fromCodePoint(code) : "";
    })
    .replace(/&([a-z]+);/gi, (all, name) => named[String(name || "").toLowerCase()] || all);
}

function stripHtml(value) {
  return decodeHtmlEntities(String(value || "").replace(/<[^>]*>/g, " "));
}

function cleanHtmlText(value) {
  return stripHtml(value).replace(/\s+/g, " ").trim();
}

function reportAPublicText(value) {
  return String(value || "").replace(/慧博/g, "报告A").replace(/Hibor/gi, "报告A");
}

function hiborMetaField(block, label) {
  const match = String(block || "").match(new RegExp(`<span>\\s*${label}：([\\s\\S]*?)<\\/span>`, "i"));
  return match ? reportAPublicText(cleanHtmlText(match[1])) : "";
}

function hiborDateFromTitle(title) {
  const match = String(title || "").match(/-(\d{2})(\d{2})(\d{2})$/);
  if (!match) return "";
  return `20${match[1]}-${match[2]}-${match[3]}`;
}

function hiborInstitutionFromTitle(title) {
  const text = String(title || "").trim();
  const index = text.indexOf("-");
  return index > 0 ? text.slice(0, index).trim() : "";
}

function parseHiborItems(html) {
  const items = [];
  const rowRe = /<tr>\s*<td>([\s\S]*?)<\/td>\s*<\/tr>/gi;
  let match;
  while ((match = rowRe.exec(String(html || ""))) && items.length < HIBOR_SEARCH_PAGE_SIZE) {
    const block = match[1];
    if (!/tab_divttl/i.test(block)) continue;
    const link = block.match(/<div class="tab_divttl"[\s\S]*?<a\s+href="([^"]+)"[^>]*title="([^"]*)"[^>]*>([\s\S]*?)<\/a>/i);
    if (!link) continue;
    const href = decodeHtmlEntities(link[1]);
    const idMatch = href.match(/\/data\/([^/.]+)\.html/i);
    if (!idMatch) continue;
    const title = reportAPublicText(cleanHtmlText(link[2] || link[3]));
    if (!title) continue;
    const shareTime = hiborMetaField(block, "分享时间");
    const pageText = hiborMetaField(block, "页数");
    const pageMatch = pageText.match(/\d+/);
    items.push({
      id: `${HIBOR_SOURCE}:${idMatch[1]}`,
      source: HIBOR_SOURCE,
      title,
      institution: hiborInstitutionFromTitle(title),
      date: shareTime.slice(0, 10) || hiborDateFromTitle(title),
      share_time: shareTime,
      category: hiborMetaField(block, "栏目"),
      author: hiborMetaField(block, "作者"),
      rating: hiborMetaField(block, "评级"),
      page_count: pageMatch ? Number(pageMatch[0]) : 0,
      file_type: "pdf",
    });
  }
  return items;
}

async function handleHiborSearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) return jsonResponse(request, env, 200, { items: [], page: 1, total: 0 });

  const body = new URLSearchParams({
    hy1: "all",
    hy2: "all",
    ybbt: query,
  }).toString();
  const upstream = `${HIBOR_ORIGIN}/newweb/web/hangye?page=${encodeURIComponent(String(page))}`;
  const response = await fetch(upstream, {
    method: "POST",
    headers: {
      "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
      "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
      "Origin": HIBOR_ORIGIN,
      "Referer": `${HIBOR_ORIGIN}/newweb/web/hangye?page=1`,
      "User-Agent": HIBOR_UA,
    },
    body,
  });
  if (!response.ok) {
    return jsonResponse(request, env, 502, { error: `Report A search failed (${response.status}).` });
  }
  const html = await response.text();
  const items = parseHiborItems(html);
  return jsonResponse(request, env, 200, {
    items,
    page,
    total: 0,
    source: HIBOR_SOURCE,
  });
}

// ---------------------------------------------------------------------------
// Authority report integration
// ---------------------------------------------------------------------------

function parseAuthorityId(value) {
  const match = String(value || "").trim().match(/^(foreign|foreign-rt):([0-9]{1,25})$/);
  if (!match || !AUTHORITY_KINDS[match[1]]) return null;
  return {
    kind: match[1],
    upstreamId: match[2],
    compoundId: `${match[1]}:${match[2]}`,
    config: AUTHORITY_KINDS[match[1]],
  };
}

function authoritySearchPayload(query, page) {
  return {
    releaseDate: 0,
    startDate: "",
    endDate: "",
    minPages: 0,
    keyword: query,
    reportTypes: [],
    industries: [],
    pageNum: page,
    pageSize: AUTHORITY_SEARCH_PAGE_SIZE,
  };
}

function authoritySearchHeaders(kindConfig) {
  return {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Origin": AUTHORITY_ORIGIN,
    "Referer": kindConfig.referer,
    "User-Agent": AUTHORITY_UA,
  };
}

function slimAuthorityItem(kind, record) {
  const config = AUTHORITY_KINDS[kind];
  const id = String(record.id || "").trim();
  const title = String(record.title || "").replace(/\s+/g, " ").trim();
  const institution = String(record.securities || record.companyName || "").trim();
  if (!id) return { id: "" };
  return {
    id: `${kind}:${id}`,
    source: AUTHORITY_SOURCE,
    kind,
    kind_label: config.label,
    title: title || "Untitled report",
    institution,
    date: String(record.reDate || "").trim(),
    report_type: String(record.reportType || "").trim(),
    page_count: Number(record.page || record.pages || 0) || 0,
    language: String(record.lang || "").trim(),
    stock_code: String(record.stockCode || record.companycode || "").trim(),
    stock_name: String(record.stockName || record.companyName || "").trim(),
    author: String(record.author || record.authors || "").trim(),
    file_type: "pdf",
  };
}

async function authoritySearchOne(kind, query, page) {
  const config = AUTHORITY_KINDS[kind];
  const response = await fetch(`${AUTHORITY_ORIGIN}${config.endpoint}`, {
    method: "POST",
    headers: authoritySearchHeaders(config),
    body: JSON.stringify(authoritySearchPayload(query, page)),
  });
  if (!response.ok) throw new Error(`HTTP ${response.status}`);
  const raw = await response.json();
  const data = raw && raw.data && typeof raw.data === "object" ? raw.data : null;
  if (raw.code !== 200 || !data || !Array.isArray(data.records)) throw new Error("bad response");
  return {
    kind,
    page: Number(data.pageNum || page),
    total: Number(data.total || 0),
    items: data.records.map((record) => slimAuthorityItem(kind, record)).filter((item) => item.id && item.title),
  };
}

async function handleAuthoritySearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  const requestedKind = String(url.searchParams.get("kind") || "both").trim();
  if (!query) {
    return jsonResponse(request, env, 200, { items: [], page: 1, total: 0 });
  }

  const kinds = AUTHORITY_KINDS[requestedKind] ? [requestedKind] : Object.keys(AUTHORITY_KINDS);
  const results = await Promise.allSettled(kinds.map((kind) => authoritySearchOne(kind, query, page)));
  const fulfilled = results
    .filter((result) => result.status === "fulfilled")
    .map((result) => result.value);
  const items = fulfilled.flatMap((result) => result.items)
    .sort((a, b) => String(b.date || "").localeCompare(String(a.date || "")));
  if (!fulfilled.length && results.length) {
    return jsonResponse(request, env, 502, { error: "Authority search is unavailable." });
  }
  return jsonResponse(request, env, 200, {
    items,
    page,
    total: fulfilled.reduce((sum, result) => sum + result.total, 0),
    sources: fulfilled.map((result) => ({ kind: result.kind, total: result.total })),
  });
}

async function handleAuthorityPdf(request, env) {
  return jsonResponse(request, env, 403, {
    error: `高权报告仅提供检索线索，无法直接下载。请联系 WeChat: ${CONTACT_WECHAT}。`,
    contact: CONTACT_WECHAT,
  });
}

export default {
  async fetch(request, env, ctx) {
    const url = new URL(request.url);
    const pathname = url.pathname.startsWith("/api/")
      ? url.pathname.slice(4) || "/"
      : url.pathname;

    if (request.method === "OPTIONS") {
      return new Response(null, { status: 204, headers: corsHeaders(request, env) });
    }

    if (pathname === "/health") {
      return jsonResponse(request, env, 200, { ok: true });
    }

    if (pathname === "/calc" && request.method === "GET") {
      return handleCalculator(request, env);
    }

    if (pathname === "/download" && request.method === "POST") {
      return handleDownload(request, env);
    }

    if (pathname === "/captcha" && request.method === "GET") {
      return handleCaptcha(request, env);
    }

    if (pathname === "/auth" && (request.method === "GET" || request.method === "POST")) {
      return handleAuth(request, env);
    }

    if (pathname === "/entitlement" && request.method === "GET") {
      return handleEntitlement(request, env);
    }

    if (pathname === "/paddle-config" && request.method === "GET") {
      return handlePaddleConfig(request, env);
    }

    if (pathname === "/paddle-webhook" && request.method === "POST") {
      return handlePaddleWebhook(request, env);
    }

    if (pathname === "/admin/login" && request.method === "POST") {
      return handleAdminLogin(request, env);
    }

    if (pathname === "/admin/report-password" && request.method === "POST") {
      return handleAdminReportPassword(request, env);
    }

    if (pathname === "/account-admin/summary" && request.method === "GET") {
      return handleAccountAdminSummary(request, env, ctx);
    }

    if (pathname === "/account-admin/github-file" && request.method === "GET") {
      return handleAccountAdminGithubFile(request, env, ctx);
    }

    if (pathname === "/account-admin/github-artifact" && request.method === "GET") {
      return handleAccountAdminGithubArtifact(request, env);
    }

    if (pathname === "/account-admin/report-pdf" && request.method === "GET") {
      return handleAccountAdminReportPdf(request, env);
    }

    if (pathname === "/external/search" && request.method === "GET") {
      return handleExternalSearch(request, env);
    }

    if (pathname === "/external/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleExternalPdf(request, env);
    }

    if (pathname === "/external/status" && request.method === "GET") {
      return handleExternalStatus(request, env);
    }

    if (pathname === "/report-a/search" && request.method === "GET") {
      return handleHiborSearch(request, env);
    }

    if (pathname === "/authority/search" && request.method === "GET") {
      return handleAuthoritySearch(request, env);
    }

    if (pathname === "/authority/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleAuthorityPdf(request, env);
    }

    return jsonResponse(request, env, 404, { error: "Not found." });
  },

  async scheduled(_event, env, ctx) {
    ctx.waitUntil(warmAdminGithubCache(env).catch(() => null));
  },
};
