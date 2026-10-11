/** Customer API authorization and bounded delivery. Content is supplied only by
 * trusted catalog/manifest adapters; this module never accepts an object key.
 * R2 writes use conditional ETags so limits and revocation survive concurrency.
 */
const PREFIX = "_customer-content-api/v1";
const SCOPES = ["reports:read", "reports:download", "artifacts:read"];
const DAY = 86400000;
const MAX_JSON = 128 * 1024;
const MAX_DOWNLOAD = 256 * 1024 * 1024;
const ID = /^[A-Za-z0-9][A-Za-z0-9_-]{0,127}$/u;
const ARTIFACT_ID = /^[A-Za-z0-9][A-Za-z0-9_-]{0,159}$/u;
const KEY_PATTERN = /^kcd_live_([a-f0-9]{24})\.([a-f0-9]{64})$/u;
const LIMITS = {
  requests_per_minute: [30, 1, 600],
  daily_requests: [1000, 1, 100000],
  daily_bytes: [1024 ** 3, 1, 100 * 1024 ** 3],
};
const ERROR_CODES = new Set([
  "authentication_required", "admin_required", "api_permission_denied", "key_invalid", "key_expired",
  "scope_denied", "report_denied", "rate_limited", "daily_request_limit", "daily_byte_limit",
  "invalid_request", "content_not_found", "service_unavailable", "method_not_allowed",
  "key_limit", "membership_required", "download_limit_reached", "account_disabled",
]);

export class CustomerContentApiError extends Error {
  constructor(status, code) {
    code = ({ content_unavailable: "service_unavailable", not_found: "content_not_found",
      invalid_date: "invalid_request", invalid_cursor: "invalid_request", access_denied: "membership_required",
      download_allowance_exhausted: "download_limit_reached" })[code] || code;
    super(ERROR_CODES.has(code) ? code : "service_unavailable");
    this.status = Number.isInteger(status) && status >= 400 && status <= 599 ? status : 503;
    this.code = ERROR_CODES.has(code) ? code : "service_unavailable";
  }
}

function fail(status, code) { throw new CustomerContentApiError(status, code); }
function json(value, status = 200, headers = {}) {
  return new Response(JSON.stringify(value), { status, headers: {
    "content-type": "application/json; charset=utf-8", "cache-control": "no-store",
    "x-content-type-options": "nosniff", ...headers,
  } });
}
function randomHex(length) {
  return Array.from(crypto.getRandomValues(new Uint8Array(length)), byte => byte.toString(16).padStart(2, "0")).join("");
}
async function sha256(value) {
  return Array.from(new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value))),
    byte => byte.toString(16).padStart(2, "0")).join("");
}
function sameDigest(left, right) {
  if (typeof left !== "string" || typeof right !== "string" || left.length !== 64 || right.length !== 64) return false;
  let different = 0;
  for (let index = 0; index < 64; index++) different |= left.charCodeAt(index) ^ right.charCodeAt(index);
  return different === 0;
}
function plainObject(value) { return value !== null && typeof value === "object" && !Array.isArray(value); }
function cleanEmail(value) {
  if (typeof value !== "string" || value.length > 254) fail(400, "invalid_request");
  const email = value.trim().toLowerCase();
  if (!/^[^\s@]+@[^\s@]+\.[^\s@]+$/u.test(email)) fail(400, "invalid_request");
  return email;
}
function accountIdentity(user) {
  if (!plainObject(user) || typeof user.id !== "string" || !user.id || user.id.length > 256
    || typeof user.email !== "string") fail(401, "authentication_required");
  return { id: user.id, email: cleanEmail(user.email) };
}
function activeAccount(user) {
  if (user.disabled === true || user.account_disabled === true) fail(403, "account_disabled");
  return accountIdentity(user);
}
async function readBoundedJson(source, maximum) {
  const declared = Number(source.size ?? source.headers?.get("content-length"));
  if (Number.isFinite(declared) && declared > maximum) fail(400, "invalid_request");
  if (!source.body?.getReader) {
    const raw = await source.text();
    if (new TextEncoder().encode(raw).length > maximum) fail(400, "invalid_request");
    return JSON.parse(raw);
  }
  const reader = source.body.getReader(), chunks = [];
  let length = 0;
  try {
    for (;;) {
      const { value, done } = await reader.read();
      if (done) break;
      length += value.byteLength;
      if (length > maximum) { await reader.cancel(); fail(400, "invalid_request"); }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
  return JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes));
}
async function requestJson(request) {
  if (!/^application\/json(?:\s*;|$)/iu.test(request.headers.get("content-type") || "")) fail(400, "invalid_request");
  try {
    const value = await readBoundedJson(request, 16 * 1024);
    if (!plainObject(value)) fail(400, "invalid_request");
    return value;
  } catch (error) {
    if (error instanceof CustomerContentApiError) throw error;
    fail(400, "invalid_request");
  }
}
async function snapshot(bucket, path) {
  const object = await bucket.get(path);
  if (!object) return { value: null, etag: null };
  try {
    const value = await readBoundedJson(object, MAX_JSON);
    if (!plainObject(value) || value.schema_version !== 1 || !object.etag) fail(503, "service_unavailable");
    return { value, etag: object.etag };
  } catch { fail(503, "service_unavailable"); }
}
async function mutate(bucket, path, update) {
  for (let attempt = 0; attempt < 4; attempt++) {
    const current = await snapshot(bucket, path);
    const value = update(current.value);
    const result = await bucket.put(path, JSON.stringify(value), {
      onlyIf: current.etag ? { etagMatches: current.etag } : { etagDoesNotMatch: "*" },
      httpMetadata: { contentType: "application/json" },
    });
    if (result) return value;
  }
  fail(503, "service_unavailable");
}
function scopes(value, fallback = SCOPES) {
  const selected = value === undefined ? [...fallback] : value;
  if (!Array.isArray(selected) || !selected.length || selected.length > SCOPES.length
    || selected.some(scope => !SCOPES.includes(scope)) || new Set(selected).size !== selected.length) fail(400, "invalid_request");
  return [...selected];
}
function expiry(value, now, maximum = now + 366 * DAY) {
  if (typeof value !== "string" || !/^\d{4}-\d\d-\d\dT/u.test(value)) fail(400, "invalid_request");
  const millis = Date.parse(value);
  if (!Number.isFinite(millis) || millis <= now || millis > maximum) fail(400, "invalid_request");
  return new Date(millis).toISOString();
}
function disabledGrant() {
  return { enabled: false, access_mode: "membership", report_ids: [], scopes: [...SCOPES], expires_at: null,
    ...Object.fromEntries(Object.entries(LIMITS).map(([name, range]) => [name, range[0]])) };
}
function makeGrant(body, oldGrant, now) {
  if (typeof body.enabled !== "boolean") fail(400, "invalid_request");
  const result = { ...(oldGrant || disabledGrant()), enabled: body.enabled };
  if (body.access_mode !== undefined) result.access_mode = body.access_mode;
  if (!["membership", "granted_corpus"].includes(result.access_mode)) fail(400, "invalid_request");
  if (body.report_ids !== undefined) result.report_ids = body.report_ids;
  if (!Array.isArray(result.report_ids) || result.report_ids.length > 500 || result.report_ids.some(id => typeof id !== "string" || !ID.test(id))) fail(400, "invalid_request");
  result.report_ids = [...new Set(result.report_ids)];
  result.scopes = scopes(body.scopes, result.scopes);
  if (result.enabled) result.expires_at = expiry(body.expires_at ?? result.expires_at, now);
  for (const [name, [fallback, min, max]] of Object.entries(LIMITS)) {
    const value = body[name] ?? result[name] ?? fallback;
    if (!Number.isSafeInteger(value) || value < min || value > max) fail(400, "invalid_request");
    result[name] = value;
  }
  result.updated_at = new Date(now).toISOString();
  return result;
}
function checkGrant(grant, now) {
  if (!plainObject(grant) || grant.enabled !== true || !(Date.parse(grant.expires_at) > now)
    || !["membership", "granted_corpus"].includes(grant.access_mode)
    || !Array.isArray(grant.scopes) || !grant.scopes.length || grant.scopes.some(scope => !SCOPES.includes(scope))
    || !Array.isArray(grant.report_ids) || grant.report_ids.length > 500 || grant.report_ids.some(id => !ID.test(id))) fail(403, "api_permission_denied");
  for (const [name, [, min, max]] of Object.entries(LIMITS)) {
    if (!Number.isSafeInteger(grant[name]) || grant[name] < min || grant[name] > max) fail(403, "api_permission_denied");
  }
}
function stateFor(value, user) {
  if (value && (value.account_id !== user.id || value.email !== user.email || !Array.isArray(value.keys)
    || value.keys.length > 100 || !plainObject(value.grant))) fail(503, "service_unavailable");
  return value || { schema_version: 1, account_id: user.id, email: user.email, grant: disabledGrant(), keys: [] };
}
function publicKey(key) {
  return { id: key.id, name: key.name, scopes: key.scopes, created_at: key.created_at,
    expires_at: key.expires_at, ...(key.revoked_at ? { revoked_at: key.revoked_at } : {}) };
}
function publicState(state) { return { grant: state.grant, keys: state.keys.map(publicKey) }; }
function assertSameOrigin(request) {
  const origin = request.headers.get("origin");
  if (origin && origin !== new URL(request.url).origin) fail(403, "api_permission_denied");
}
function validQuery(url, allowed) {
  for (const name of url.searchParams.keys()) {
    if (!allowed.includes(name) || url.searchParams.getAll(name).length !== 1) fail(400, "invalid_request");
  }
}
function listQuery(url, artifacts = false) {
  validQuery(url, artifacts ? ["kind", "language", "cursor", "limit"] : ["date", "cursor", "limit"]);
  const rawLimit = url.searchParams.get("limit"), limit = rawLimit === null ? 25 : Number(rawLimit);
  if ((rawLimit !== null && !/^\d{1,3}$/u.test(rawLimit)) || !Number.isInteger(limit) || limit < 1 || limit > 100) fail(400, "invalid_request");
  const cursor = url.searchParams.get("cursor") || null;
  if (cursor && (cursor.length > 512 || !/^[A-Za-z0-9_.=-]+$/u.test(cursor))) fail(400, "invalid_request");
  const query = { limit, cursor };
  if (artifacts) {
    for (const name of ["kind", "language"]) {
      const value = url.searchParams.get(name);
      if (value !== null) {
        if (!/^[A-Za-z][A-Za-z0-9_-]{0,39}$/u.test(value)) fail(400, "invalid_request");
        query[name] = value;
      }
    }
  } else {
    const date = url.searchParams.get("date");
    if (date !== null) {
      if (!/^\d{4}-\d\d-\d\d$/u.test(date) || !Number.isFinite(Date.parse(date)) || new Date(date).toISOString().slice(0, 10) !== date) fail(400, "invalid_request");
      query.date = date;
    }
  }
  return query;
}
function reportAllowed(grant, id) { return ID.test(id) && (!grant.report_ids.length || grant.report_ids.includes(id)); }
function publicReport(row) {
  if (!plainObject(row) || typeof row.id !== "string" || !ID.test(row.id)) fail(503, "service_unavailable");
  const result = { id: row.id };
  for (const name of ["title", "title_zh", "title_en", "institution", "industry", "date", "date_folder", "language", "text_scope", "source", "processed_updated_at"])
    if (typeof row[name] === "string") result[name] = row[name].slice(0, 1000);
  for (const name of ["page_count", "artifact_count"])
    if (Number.isSafeInteger(row[name]) && row[name] >= 0) result[name] = row[name];
  for (const name of ["available", "partial_excerpt", "pdf_available", "pdf_listed"])
    if (typeof row[name] === "boolean") result[name] = row[name];
  if (Array.isArray(row.languages)) result.languages = row.languages.filter(value => typeof value === "string" && /^[a-zA-Z0-9-]{1,30}$/u.test(value)).slice(0, 40);
  return result;
}
function publicArtifact(row, reportId) {
  if (!plainObject(row) || typeof row.id !== "string" || !ARTIFACT_ID.test(row.id) || row.report_id !== reportId
    || (row.size !== null && (!Number.isSafeInteger(row.size) || row.size < 0 || row.size > MAX_DOWNLOAD))
    || typeof row.kind !== "string" || !/^[a-z][a-z0-9_-]{0,39}$/u.test(row.kind)
    || typeof row.mime_type !== "string" || row.mime_type.length > 120) fail(503, "service_unavailable");
  const result = { id: row.id, report_id: row.report_id, kind: row.kind,
    language: typeof row.language === "string" ? row.language.slice(0, 40) : "und", mime_type: row.mime_type, size: row.size };
  if (typeof row.filename === "string") result.filename = row.filename.replace(/[\u0000-\u001f\u007f/\\]/gu, "_").slice(0, 200);
  if (typeof row.sha256 === "string" && /^[a-f0-9]{64}$/u.test(row.sha256)) result.sha256 = row.sha256;
  if (typeof row.text_scope === "string") result.text_scope = row.text_scope.slice(0, 40);
  if (Number.isSafeInteger(row.page_number) && row.page_number > 0) result.page_number = row.page_number;
  return result;
}
function publicList(value, query, render) {
  if (!plainObject(value) || !Array.isArray(value.items) || value.items.length > query.limit
    || (value.next_cursor != null && value.next_cursor !== "" && (typeof value.next_cursor !== "string" || value.next_cursor.length > 512
      || !/^[A-Za-z0-9_.=-]+$/u.test(value.next_cursor)))) fail(503, "service_unavailable");
  return { ok: true, items: value.items.map(render).filter(Boolean), next_cursor: value.next_cursor || null };
}
async function cancelBody(response) { try { await response?.body?.cancel(); } catch { /* No response details in logs. */ } }
function boundedStream(body, maximum) {
  if (!body) return null;
  const reader = body.getReader();
  let received = 0;
  return new ReadableStream({
    async pull(controller) {
      try {
        const { value, done } = await reader.read();
        if (done) {
          if (received !== maximum) throw new Error("content_length_mismatch");
          controller.close(); return;
        }
        received += value.byteLength;
        if (received > maximum) throw new Error("content_length_mismatch");
        controller.enqueue(value);
      } catch {
        try { await reader.cancel(); } catch { /* Cancel best effort. */ }
        controller.error(new Error("content_unavailable"));
      }
    },
    cancel() { return reader.cancel(); },
  });
}

/**
 * All adapters are injected; no account tokens, raw artifacts, or provider
 * caches are discovered here. See docs/customer-content-api.md for the contract.
 */
export function createCustomerContentApi(adapters) {
  const now = () => adapters.now ? adapters.now() : Date.now();
  const bucketFor = env => {
    const bucket = adapters.bucket(env);
    if (!bucket?.get || !bucket?.put) fail(503, "service_unavailable");
    return bucket;
  };
  const statePath = async user => `${PREFIX}/accounts/${await sha256(user.id)}.json`;
  async function loggedIn(env, request) {
    let user;
    try { user = await adapters.currentUser(env, request); } catch { fail(401, "authentication_required"); }
    if (!user || user instanceof Response) fail(401, "authentication_required");
    activeAccount(user); return user;
  }
  async function admin(env, request) {
    let user;
    try { user = await adapters.requireAdmin(env, request); } catch { fail(403, "admin_required"); }
    if (!user || user instanceof Response) fail(403, "admin_required");
    return user;
  }
  async function reserve(context, bytes = 0, requestCount = 0) {
    const instant = now(), day = new Date(instant).toISOString().slice(0, 10), minute = Math.floor(instant / 60000);
    const path = `${PREFIX}/usage/${await sha256(context.user.id)}.json`;
    await mutate(context.bucket, path, previous => {
      const current = previous || { schema_version: 1 };
      for (const name of ["requests", "bytes", "minute_requests"]) {
        if (current[name] !== undefined && (!Number.isSafeInteger(current[name]) || current[name] < 0)) fail(503, "service_unavailable");
      }
      const requests = (current.day === day ? current.requests || 0 : 0) + requestCount;
      const totalBytes = (current.day === day ? current.bytes || 0 : 0) + bytes;
      const minuteRequests = (current.minute === minute ? current.minute_requests || 0 : 0) + requestCount;
      if (requests > context.grant.daily_requests) fail(429, "daily_request_limit");
      if (minuteRequests > context.grant.requests_per_minute) fail(429, "rate_limited");
      if (totalBytes > context.grant.daily_bytes) fail(429, "daily_byte_limit");
      return { schema_version: 1, day, minute, requests, bytes: totalBytes, minute_requests: minuteRequests };
    });
  }
  async function authenticate(env, request, requiredScope) {
    const header = request.headers.get("authorization") || "";
    const token = /^Bearer (\S+)$/u.exec(header)?.[1], match = KEY_PATTERN.exec(token || "");
    if (!match) fail(401, "key_invalid");
    const bucket = bucketFor(env), lookup = (await snapshot(bucket, `${PREFIX}/lookup/${match[1]}.json`)).value;
    if (!lookup || typeof lookup.account_id !== "string" || typeof lookup.email !== "string") fail(401, "key_invalid");
    const user = await adapters.findAccount(env, { id: lookup.account_id, email: lookup.email });
    if (!user || user instanceof Response) fail(401, "key_invalid");
    const identity = activeAccount(user);
    if (identity.id !== lookup.account_id || identity.email !== lookup.email) fail(401, "key_invalid");
    const state = stateFor((await snapshot(bucket, await statePath(identity))).value, identity);
    const key = state.keys.find(item => item.id === match[1]);
    if (!key || key.revoked_at || !sameDigest(key.hash, await sha256(token))) fail(401, "key_invalid");
    if (!(Date.parse(key.expires_at) > now())) fail(401, "key_expired");
    checkGrant(state.grant, now());
    if (!Array.isArray(key.scopes) || !key.scopes.includes(requiredScope) || !state.grant.scopes.includes(requiredScope)) fail(403, "scope_denied");
    const context = { user, grant: state.grant, key: publicKey(key), bucket };
    await reserve(context, 0, 1);
    return context;
  }
  async function manage(env, request, url) {
    const bucket = bucketFor(env);
    if (url.pathname === "/api/admin/content-api/grant") {
      await admin(env, request);
      let body;
      if (request.method === "GET") { validQuery(url, ["email"]); body = { email: url.searchParams.get("email") }; }
      else if (request.method === "POST") { validQuery(url, []); assertSameOrigin(request); body = await requestJson(request); }
      else fail(405, "method_not_allowed");
      const email = cleanEmail(body.email), found = await adapters.findAccount(env, { email });
      if (!found || found instanceof Response) fail(404, "content_not_found");
      const identity = accountIdentity(found);
      if (identity.email !== email) fail(404, "content_not_found");
      const path = await statePath(identity);
      if (request.method === "GET") return json({ ok: true, email, ...publicState(stateFor((await snapshot(bucket, path)).value, identity)) });
      if (body.enabled === true) activeAccount(found);
      const updated = await mutate(bucket, path, value => {
        const state = stateFor(value, identity), grant = makeGrant(body, state.grant, now());
        return { ...state, grant, keys: grant.enabled ? state.keys : state.keys.map(key => ({ ...key, revoked_at: key.revoked_at || new Date(now()).toISOString() })) };
      });
      return json({ ok: true, email, grant: updated.grant });
    }
    const user = await loggedIn(env, request), identity = accountIdentity(user), path = await statePath(identity);
    validQuery(url, []);
    if (url.pathname === "/api/account/content-api") {
      if (request.method !== "GET") fail(405, "method_not_allowed");
      return json({ ok: true, ...publicState(stateFor((await snapshot(bucket, path)).value, identity)) });
    }
    assertSameOrigin(request);
    if (url.pathname === "/api/account/content-api/keys") {
      if (request.method !== "POST") fail(405, "method_not_allowed");
      const body = await requestJson(request);
      if (typeof body.name !== "string" || !body.name.trim() || body.name.trim().length > 80 || /[\u0000-\u001f\u007f]/u.test(body.name)) fail(400, "invalid_request");
      const preliminary = stateFor((await snapshot(bucket, path)).value, identity);
      checkGrant(preliminary.grant, now());
      if (preliminary.keys.filter(key => !key.revoked_at && Date.parse(key.expires_at) > now()).length >= 5) fail(409, "key_limit");
      const requestedScopes = scopes(body.scopes, preliminary.grant.scopes);
      if (requestedScopes.some(scope => !preliminary.grant.scopes.includes(scope))) fail(403, "scope_denied");
      if (body.expires_at !== undefined) expiry(body.expires_at, now(), Math.min(Date.parse(preliminary.grant.expires_at), now() + 90 * DAY));
      const id = randomHex(12), secret = `kcd_live_${id}.${randomHex(32)}`, hash = await sha256(secret), created = now();
      // A lookup without a matching committed account key cannot authenticate.
      const inserted = await bucket.put(`${PREFIX}/lookup/${id}.json`, JSON.stringify({ schema_version: 1, account_id: identity.id, email: identity.email }),
        { onlyIf: { etagDoesNotMatch: "*" }, httpMetadata: { contentType: "application/json" } });
      if (!inserted) fail(503, "service_unavailable");
      let newKey;
      await mutate(bucket, path, value => {
        const state = stateFor(value, identity);
        checkGrant(state.grant, created);
        if (state.keys.filter(key => !key.revoked_at && Date.parse(key.expires_at) > created).length >= 5) fail(409, "key_limit");
        const selected = scopes(body.scopes, state.grant.scopes);
        if (selected.some(scope => !state.grant.scopes.includes(scope))) fail(403, "scope_denied");
        const maximum = Math.min(Date.parse(state.grant.expires_at), created + 90 * DAY);
        const expires = body.expires_at === undefined ? new Date(maximum).toISOString() : expiry(body.expires_at, created, maximum);
        newKey = { id, hash, name: body.name.trim(), scopes: selected, created_at: new Date(created).toISOString(), expires_at: expires };
        const keys = state.keys.length >= 100 ? state.keys.filter(key => !key.revoked_at && Date.parse(key.expires_at) > created) : state.keys;
        return { ...state, keys: [...keys, newKey] };
      });
      return json({ ok: true, key: publicKey(newKey), secret }, 201);
    }
    const match = /^\/api\/account\/content-api\/keys\/([a-f0-9]{24})$/u.exec(url.pathname);
    if (!match) fail(404, "content_not_found");
    if (request.method !== "DELETE") fail(405, "method_not_allowed");
    await mutate(bucket, path, value => {
      const state = stateFor(value, identity);
      if (!state.keys.some(key => key.id === match[1])) fail(404, "content_not_found");
      return { ...state, keys: state.keys.map(key => key.id === match[1] ? { ...key, revoked_at: key.revoked_at || new Date(now()).toISOString() } : key) };
    });
    return json({ ok: true });
  }
  async function deliver(response, context) {
    if (!(response instanceof Response)) fail(503, "service_unavailable");
    if (response.status !== 200) {
      await cancelBody(response);
      fail(response.status === 404 ? 404 : 503, response.status === 404 ? "content_not_found" : "service_unavailable");
    }
    const rawLength = response.headers.get("content-length"), size = Number(rawLength);
    if (rawLength === null || !/^\d+$/u.test(rawLength) || !Number.isSafeInteger(size) || size < 0 || size > MAX_DOWNLOAD
      || (size > 0 && !response.body) || response.headers.get("content-encoding")) {
      await cancelBody(response); fail(503, "service_unavailable");
    }
    try {
      await reserve(context, size);
      if (context.commitDownload) await context.commitDownload();
    } catch (error) { await cancelBody(response); throw error; }
    const headers = new Headers({ "cache-control": "private, no-store", "x-content-type-options": "nosniff", "content-length": String(size) });
    for (const name of ["content-type", "content-disposition", "etag"]) {
      if (response.headers.has(name)) headers.set(name, response.headers.get(name));
    }
    if (!headers.has("content-type")) headers.set("content-type", "application/octet-stream");
    if (!/^attachment(?:;|$)/iu.test(headers.get("content-disposition") || "")) headers.set("content-disposition", "attachment");
    return new Response(boundedStream(response.body, size), { status: 200, headers });
  }
  async function content(env, request, url) {
    if (request.method !== "GET") fail(405, "method_not_allowed");
    const match = /^\/api\/content\/v1\/reports(?:\/([A-Za-z0-9][A-Za-z0-9_-]{0,127})(?:\/(download|artifacts)(?:\/([A-Za-z0-9][A-Za-z0-9_-]{0,159}))?)?)?$/u.exec(url.pathname);
    if (!match) fail(404, "content_not_found");
    const reportId = match[1], operation = match[2], artifactId = match[3];
    if (operation === "download" && artifactId) fail(404, "content_not_found");
    const required = operation === "download" ? "reports:download" : operation === "artifacts" ? "artifacts:read" : "reports:read";
    const query = !reportId ? listQuery(url) : operation === "artifacts" && !artifactId ? { ...listQuery(url, true), reportId } : (validQuery(url, []), { reportId, ...(artifactId ? { artifactId } : {}) });
    const context = await authenticate(env, request, required);
    if (reportId && !reportAllowed(context.grant, reportId)) fail(403, "report_denied");
    if (!reportId) {
      const listed = await adapters.listReports(env, query, context);
      return json(publicList(listed, query, row => reportAllowed(context.grant, row.id) ? publicReport(row) : null));
    }
    if (operation === "download") return deliver(await adapters.downloadReport(env, query, context), context);
    if (artifactId) return deliver(await adapters.downloadArtifact(env, query, context), context);
    if (operation === "artifacts") return json(publicList(await adapters.listArtifacts(env, query, context), query, row => publicArtifact(row, reportId)));
    const report = await adapters.getReport(env, query, context);
    if (!report) fail(404, "content_not_found");
    if (report.id !== reportId) fail(503, "service_unavailable");
    return json({ ok: true, report: publicReport(report) });
  }
  function matches(path) {
    return path === "/api/admin/content-api/grant" || path === "/api/account/content-api"
      || path.startsWith("/api/account/content-api/") || path === "/api/content/v1/reports" || path.startsWith("/api/content/v1/reports/");
  }
  async function handle(request, env, _executionContext) {
    try {
      const url = new URL(request.url);
      if (!matches(url.pathname)) return null;
      return await (url.pathname.startsWith("/api/content/v1/") ? content(env, request, url) : manage(env, request, url));
    } catch (error) {
      const known = error instanceof CustomerContentApiError;
      const code = known ? error.code : "service_unavailable", status = known ? error.status : 503;
      return json({ ok: false, error: code }, status, status === 429 ? { "retry-after": code === "rate_limited" ? "60" : "86400" } : {});
    }
  }
  return { matches, handle };
}
