const CACHE_TTL_MS = 5 * 60 * 1000;
const DEFAULT_R2_PREFIX = "reports";
const CONTACT_WECHAT = "macroGate";
const ADMIN_TOKEN_TTL_SECONDS = 180 * 24 * 60 * 60;
const USER_TOKEN_TTL_SECONDS = 30 * 24 * 60 * 60;
const CAPTCHA_TTL_SECONDS = 10 * 60;
const PASSWORD_ITERATIONS = 120000;
const GENERATED_EMAIL_DOMAIN = "users.kcdesk.com";
const USERNAME_PATTERN = /^[a-z0-9][a-z0-9_.-]{2,31}$/;
const EMAIL_PATTERN = /^[^@\s]+@[^@\s]+\.[^@\s]+$/;
const ACTIVE_STATUSES = new Set(["active", "trialing"]);
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
    "Access-Control-Allow-Headers": "Content-Type, Authorization, Paddle-Signature",
    "Access-Control-Expose-Headers": "Content-Disposition",
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

async function hashUserPassword(password) {
  const salt = randomHex(16);
  const digest = await pbkdf2Digest(password, salt, PASSWORD_ITERATIONS);
  return {
    password_salt: salt,
    password_hash: `pbkdf2_sha256$${PASSWORD_ITERATIONS}$${digest}`,
  };
}

async function verifyUserPassword(password, salt, storedHash) {
  let algorithm = "pbkdf2_sha256";
  let iterations = PASSWORD_ITERATIONS;
  let digest = String(storedHash || "");
  const parts = digest.split("$");
  if (parts.length === 3) {
    [algorithm, iterations, digest] = [parts[0], Number(parts[1]), parts[2]];
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
  return {
    id: user.id || "",
    username: user.username || "",
    email,
    email_is_generated: Boolean(user.email_is_generated) || isGeneratedEmail(email),
    created_at: user.created_at || "",
    updated_at: user.updated_at || "",
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

async function r2PutJson(env, key, payload) {
  await accountBucket(env).put(key, JSON.stringify(payload), {
    httpMetadata: { contentType: "application/json; charset=utf-8" },
  });
  return payload;
}

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

function queryString(params) {
  const search = new URLSearchParams();
  Object.entries(params).forEach(([key, value]) => search.set(key, value));
  return search.toString();
}

async function findSiteUserByUsername(env, username) {
  if (!hasSupabaseConfig(env)) {
    return r2GetJson(env, accountKey("users", "username", username));
  }
  const query = queryString({ username: `eq.${username}`, limit: "1" });
  const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
  return Array.isArray(rows) && rows.length ? rows[0] : null;
}

async function findSiteUserByEmail(env, email) {
  if (!hasSupabaseConfig(env)) {
    return r2GetJson(env, accountKey("users", "email", email));
  }
  const query = queryString({ email: `eq.${email}`, limit: "1" });
  const rows = await supabaseRequest(env, "GET", `/rest/v1/site_users?${query}`);
  return Array.isArray(rows) && rows.length ? rows[0] : null;
}

async function createSiteUser(env, fields) {
  if (!hasSupabaseConfig(env)) {
    const id = crypto.randomUUID ? crypto.randomUUID() : randomHex(16);
    const user = { ...fields, id };
    await r2PutJson(env, accountKey("users", "id", id), user);
    await r2PutJson(env, accountKey("users", "username", user.username), user);
    await r2PutJson(env, accountKey("users", "email", user.email), user);
    return user;
  }
  const rows = await supabaseRequest(env, "POST", "/rest/v1/site_users?select=*", fields, { preferReturn: true });
  return Array.isArray(rows) && rows.length ? rows[0] : fields;
}

async function updateSiteUser(env, userId, fields) {
  if (!hasSupabaseConfig(env)) {
    const existing = await r2GetJson(env, accountKey("users", "id", userId));
    const user = { ...(existing || {}), ...fields, id: userId, updated_at: new Date().toISOString() };
    if (user.username) await r2PutJson(env, accountKey("users", "username", user.username), user);
    if (user.email) await r2PutJson(env, accountKey("users", "email", user.email), user);
    await r2PutJson(env, accountKey("users", "id", userId), user);
    return user;
  }
  const query = queryString({ id: `eq.${userId}`, select: "*" });
  const rows = await supabaseRequest(env, "PATCH", `/rest/v1/site_users?${query}`, {
    ...fields,
    updated_at: new Date().toISOString(),
  }, { preferReturn: true });
  return Array.isArray(rows) && rows.length ? rows[0] : fields;
}

async function currentUserFromRequest(env, request) {
  const token = bearerToken(request);
  if (!token) throw new Error("Please log in.");
  const payload = await verifyAccountPayload(env, token, "user");
  const user = await findSiteUserByUsername(env, normalizeUsername(payload.username));
  if (!user) throw new Error("Account not found.");
  return user;
}

async function findEntitlement(env, email) {
  if (!hasSupabaseConfig(env)) {
    return r2GetJson(env, accountKey("entitlements", email));
  }
  const query = queryString({ email: `eq.${email}`, order: "updated_at.desc", limit: "1" });
  const rows = await supabaseRequest(env, "GET", `/rest/v1/user_entitlements?${query}`);
  return Array.isArray(rows) && rows.length ? rows[0] : null;
}

async function saveEntitlement(env, email, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) {
    const existing = await findEntitlement(env, email);
    return r2PutJson(env, accountKey("entitlements", email), {
      ...(existing || {}),
      ...fields,
      email,
      id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
      updated_at: now,
      created_at: existing && existing.created_at || now,
    });
  }
  const existing = await findEntitlement(env, email);
  const payload = { ...fields, email, updated_at: now };
  if (existing && existing.id) {
    const query = queryString({ id: `eq.${existing.id}`, select: "*" });
    const rows = await supabaseRequest(env, "PATCH", `/rest/v1/user_entitlements?${query}`, payload, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : payload;
  }
  const rows = await supabaseRequest(env, "POST", "/rest/v1/user_entitlements?select=*", {
    ...payload,
    created_at: now,
  }, { preferReturn: true });
  return Array.isArray(rows) && rows.length ? rows[0] : payload;
}

async function findReportPurchase(env, email, reportId, source) {
  if (!hasSupabaseConfig(env)) {
    return r2GetJson(env, accountKey("purchases", source, reportId, email));
  }
  const query = queryString({
    email: `eq.${email}`,
    report_id: `eq.${reportId}`,
    source: `eq.${source}`,
    order: "updated_at.desc",
    limit: "1",
  });
  const rows = await supabaseRequest(env, "GET", `/rest/v1/report_purchases?${query}`);
  return Array.isArray(rows) && rows.length ? rows[0] : null;
}

async function saveReportPurchase(env, fields) {
  const now = new Date().toISOString();
  if (!hasSupabaseConfig(env)) {
    const existing = await findReportPurchase(env, fields.email, fields.report_id, fields.source);
    return r2PutJson(env, accountKey("purchases", fields.source, fields.report_id, fields.email), {
      ...(existing || {}),
      ...fields,
      id: existing && existing.id || (crypto.randomUUID ? crypto.randomUUID() : randomHex(16)),
      purchased_at: existing && existing.purchased_at || now,
      created_at: existing && existing.created_at || now,
      updated_at: now,
    });
  }
  const existing = await findReportPurchase(env, fields.email, fields.report_id, fields.source);
  const payload = { ...fields, updated_at: now };
  if (existing && existing.id) {
    const query = queryString({ id: `eq.${existing.id}`, select: "*" });
    const rows = await supabaseRequest(env, "PATCH", `/rest/v1/report_purchases?${query}`, payload, { preferReturn: true });
    return Array.isArray(rows) && rows.length ? rows[0] : payload;
  }
  const rows = await supabaseRequest(env, "POST", "/rest/v1/report_purchases?select=*", {
    ...payload,
    purchased_at: now,
    created_at: now,
  }, { preferReturn: true });
  return Array.isArray(rows) && rows.length ? rows[0] : payload;
}

async function insertUsageEvent(env, email, eventType, metadata = {}) {
  if (!hasSupabaseConfig(env)) {
    const key = accountKey("usage", email, `${Date.now()}-${randomHex(4)}.json`);
    await r2PutJson(env, key, {
      id: crypto.randomUUID ? crypto.randomUUID() : randomHex(16),
      email,
      event_type: eventType,
      units: 1,
      metadata,
      created_at: new Date().toISOString(),
    });
    return;
  }
  await supabaseRequest(env, "POST", "/rest/v1/usage_events", {
    email,
    event_type: eventType,
    units: 1,
    metadata,
  });
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

async function reportAccessForUser(env, user, reportId, source) {
  const email = normalizeEmail(user.email);
  if (!email) return { can_download: false, entitlement: publicEntitlement(null), purchase: null };
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
      if (existing) return jsonResponse(request, env, 409, { detail: "用户名已被注册。" });
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
      if (existingEmail) return jsonResponse(request, env, 409, { detail: "用户名或邮箱已被注册。" });
      const now = new Date().toISOString();
      const passwordFields = await hashUserPassword(password);
      const user = await createSiteUser(env, {
        username,
        email,
        email_is_generated: emailIsGenerated,
        ...passwordFields,
        created_at: now,
        updated_at: now,
        last_login_at: now,
      });
      return jsonResponse(request, env, 201, {
        token: await createUserToken(env, user),
        user: publicUser(user),
      });
    }

    const user = await findSiteUserByUsername(env, username);
    const ok = user && await verifyUserPassword(password, String(user.password_salt || ""), String(user.password_hash || ""));
    if (!ok) return jsonResponse(request, env, 401, { detail: "用户名或密码不正确。" });
    const updated = user.id ? await updateSiteUser(env, user.id, { last_login_at: new Date().toISOString() }) : user;
    const merged = { ...user, ...updated };
    return jsonResponse(request, env, 200, {
      token: await createUserToken(env, merged),
      user: publicUser(merged),
    });
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

function paddleConfig(env) {
  const cnyCentPrice = cleanEnv(env.PADDLE_PRICE_CNY_CENT);
  return {
    PADDLE_ENV: cleanEnv(env.PADDLE_ENV) || "production",
    PADDLE_CLIENT_TOKEN: cleanEnv(env.PADDLE_CLIENT_TOKEN),
    PADDLE_PRICE_CNY_CENT: cnyCentPrice,
    PADDLE_PRICE_REPORT_CNY_CENT: cleanEnv(env.PADDLE_PRICE_REPORT_CNY_CENT) || cnyCentPrice,
    PADDLE_PRICE_YEARLY: cleanEnv(env.PADDLE_PRICE_YEARLY) || cnyCentPrice,
  };
}

function handlePaddleConfig(request, env) {
  const config = paddleConfig(env);
  const missing = ["PADDLE_CLIENT_TOKEN", "PADDLE_PRICE_REPORT_CNY_CENT", "PADDLE_PRICE_YEARLY"]
    .filter((key) => !config[key]);
  return jsonResponse(request, env, 200, { config, missing });
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
  } else if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }

  try {
    await verifyAdminToken(env, token);
  } catch (error) {
    return jsonResponse(request, env, 401, { error: error.message || "Admin session is invalid." });
  }

  if (source === "external") {
    try {
      return jsonResponse(request, env, 200, {
        id,
        source: "external",
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

export default {
  async fetch(request, env) {
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

    if (pathname === "/external/search" && request.method === "GET") {
      return handleExternalSearch(request, env);
    }

    if (pathname === "/external/pdf" && (request.method === "GET" || request.method === "POST")) {
      return handleExternalPdf(request, env);
    }

    if (pathname === "/external/status" && request.method === "GET") {
      return handleExternalStatus(request, env);
    }

    return jsonResponse(request, env, 404, { error: "Not found." });
  },
};
