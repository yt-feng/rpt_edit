// English is a separate editorial product: never reports, originals or charts.
// Only the checksum-verified, approved private ledger can authorize a body.
export const ENGLISH_COMMENTARY_POLICY = "english-secondary-commentary-v1";
export const ENGLISH_FREE_READS = 3;
export const ENGLISH_PREFIX = "_english-commentary/v1";
const ID = /^\d{8}-[a-f0-9]{16}$/;
const HASH = /^[a-f0-9]{64}$/;
const BLOCK_TAGS = new Set(["h2", "h3", "h4", "p", "li"]);
const PRIVATE = { contentType: "application/json; charset=utf-8", cacheControl: "private, no-store" };

function requireValue(condition) {
  if (!condition) throw new Error("invalid_english_commentary");
}

function exactKeys(value, keys) {
  requireValue(value && typeof value === "object" && !Array.isArray(value));
  requireValue(Object.keys(value).length === keys.length && keys.every((key) => Object.hasOwn(value, key)));
}

function text(value, maximum) {
  requireValue(typeof value === "string" && value.trim().length > 0 && value.length <= maximum);
  // No HTML, Markdown images, embedded URLs, original-language prose or hidden
  // chart/PDF endpoints are admitted into the English text-only payload.
  requireValue(!/[<>\u3400-\u9fff\ufffd\ud800-\udfff]/u.test(value));
  requireValue(!/!\[|https?:\/\/|(?:data|javascript):/i.test(value));
  return value;
}

function date(value) {
  requireValue(typeof value === "string" && /^\d{4}-\d{2}-\d{2}$/.test(value));
  const parsed = new Date(value + "T00:00:00Z");
  requireValue(Number.isFinite(parsed.getTime()) && parsed.toISOString().slice(0, 10) === value);
  return value;
}

async function sha256(value) {
  const hash = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(value));
  return Array.from(new Uint8Array(hash), (byte) => byte.toString(16).padStart(2, "0")).join("");
}

async function readObject(bucket, key, maximum) {
  const object = await bucket.get(key);
  if (!object) return null;
  requireValue(object.etag && Number.isSafeInteger(object.size) && object.size > 0 && object.size <= maximum);
  const raw = await object.text();
  requireValue(new TextEncoder().encode(raw).length <= maximum);
  return { object, raw, value: JSON.parse(raw) };
}

async function boundedRequest(request) {
  const declared = Number(request.headers.get("content-length") || 0);
  if (declared > 2048) return null;
  if (!request.body) return "";
  const reader = request.body.getReader(), decoder = new TextDecoder();
  let bytes = 0, raw = "";
  try {
    while (true) {
      const part = await reader.read();
      if (part.done) return raw + decoder.decode();
      bytes += part.value.byteLength;
      if (bytes > 2048) return null;
      raw += decoder.decode(part.value, { stream: true });
    }
  } finally {
    await reader.cancel().catch(() => {}); reader.releaseLock();
  }
}

function previewRecord(item) {
  exactKeys(item, ["id", "title", "preview", "datePublished", "body_sha256", "editorial_sha256"]);
  requireValue(ID.test(item.id) && HASH.test(item.body_sha256) && HASH.test(item.editorial_sha256));
  text(item.title, 500); text(item.preview, 640); date(item.datePublished);
  requireValue(item.id.slice(0, 8) === item.datePublished.replaceAll("-", ""));
  return { id: item.id, title: item.title, preview: item.preview, datePublished: item.datePublished };
}

export function validateEnglishLedger(value) {
  exactKeys(value, ["schema_version", "policy", "locale", "status", "release_id", "items"]);
  requireValue(value.schema_version === 1 && value.policy === ENGLISH_COMMENTARY_POLICY && value.locale === "en");
  requireValue(value.status === "approved" && HASH.test(value.release_id));
  requireValue(Array.isArray(value.items) && value.items.length <= 5000);
  const ids = new Set();
  for (const item of value.items) {
    previewRecord(item); requireValue(!ids.has(item.id)); ids.add(item.id);
  }
  return value;
}

export function validateEnglishBody(value, item) {
  exactKeys(value, ["schema_version", "policy", "locale", "content_kind", "id", "title", "preview", "datePublished", "editorial_sha256", "blocks"]);
  requireValue(value.schema_version === 1 && value.policy === ENGLISH_COMMENTARY_POLICY && value.locale === "en");
  requireValue(value.content_kind === "secondary-commentary");
  for (const key of ["id", "title", "preview", "datePublished", "editorial_sha256"]) requireValue(value[key] === item[key]);
  requireValue(Array.isArray(value.blocks) && value.blocks.length > 0 && value.blocks.length <= 500);
  for (const block of value.blocks) {
    exactKeys(block, ["tag", "text"]);
    requireValue(BLOCK_TAGS.has(block.tag)); text(block.text, 12000);
  }
  return value;
}

async function approvedLedger(bucket) {
  const record = await readObject(bucket, `${ENGLISH_PREFIX}/active.json`, 2 * 1024 * 1024);
  return record ? validateEnglishLedger(record.value) : null;
}

function validateQuota(value, identity) {
  exactKeys(value, ["schema_version", "policy", "identity", "reads"]);
  requireValue(value.schema_version === 1 && value.policy === ENGLISH_COMMENTARY_POLICY && value.identity === identity);
  requireValue(Array.isArray(value.reads) && value.reads.length <= ENGLISH_FREE_READS);
  requireValue(new Set(value.reads).size === value.reads.length && value.reads.every((id) => ID.test(id)));
  return value;
}

export async function consumeEnglishRead(bucket, userId, articleId) {
  requireValue(typeof userId === "string" && userId.length > 0 && userId.length <= 256 && ID.test(articleId));
  const identity = await sha256(`english-commentary-account-v1:${userId}`);
  const key = `${ENGLISH_PREFIX}/accounts/${identity}/reads.json`;
  for (let attempt = 0; attempt < 6; attempt += 1) {
    const previous = await readObject(bucket, key, 16384);
    const value = previous ? validateQuota(previous.value, identity)
      : { schema_version: 1, policy: ENGLISH_COMMENTARY_POLICY, identity, reads: [] };
    if (value.reads.includes(articleId)) return { allowed: true, remaining: ENGLISH_FREE_READS - value.reads.length, reused: true };
    if (value.reads.length >= ENGLISH_FREE_READS) return { allowed: false, remaining: 0 };
    const updated = { ...value, reads: [...value.reads, articleId] };
    const written = await bucket.put(key, JSON.stringify(updated), {
      onlyIf: previous ? { etagMatches: previous.object.etag } : { etagDoesNotMatch: "*" },
      httpMetadata: PRIVATE,
    });
    if (written) return { allowed: true, remaining: ENGLISH_FREE_READS - updated.reads.length, reused: false };
  }
  throw new Error("english_quota_contention");
}

export async function handleEnglishCommentary(request, env, adapters) {
  const respond = (status, value) => adapters.respond(request, env, status, value);
  const url = new URL(request.url);
  const full = url.pathname.endsWith("/english/commentary/read");
  if (request.method !== (full ? "POST" : "GET")) return respond(405, { error: "method_not_allowed" });
  try {
    const bucket = env.REPORT_BUCKET;
    if (!bucket) return respond(503, { error: "commentary_temporarily_unavailable" });
    const ledger = await approvedLedger(bucket);
    if (!ledger) return respond(404, { error: "commentary_not_published" });
    if (!full) {
      const id = url.searchParams.get("id");
      if (id !== null) {
        if (!ID.test(id)) return respond(400, { error: "invalid_article_id" });
        const item = ledger.items.find((row) => row.id === id);
        return item ? respond(200, { ...previewRecord(item), policy: ENGLISH_COMMENTARY_POLICY, free_reads: ENGLISH_FREE_READS })
          : respond(404, { error: "commentary_not_found" });
      }
      const page = Number(url.searchParams.get("page") || "1");
      if (!Number.isSafeInteger(page) || page < 1 || page > 250) return respond(400, { error: "invalid_page" });
      const items = [...ledger.items].sort((a, b) => b.id.localeCompare(a.id));
      return respond(200, { policy: ENGLISH_COMMENTARY_POLICY, total: items.length, page, page_size: 24,
        items: items.slice((page - 1) * 24, page * 24).map(previewRecord), free_reads: ENGLISH_FREE_READS });
    }
    const raw = await boundedRequest(request);
    if (raw === null) return respond(413, { error: "request_too_large" });
    let input;
    try { input = JSON.parse(raw); exactKeys(input, ["id"]); } catch (_) { return respond(400, { error: "invalid_request" }); }
    if (!ID.test(input.id)) return respond(400, { error: "invalid_article_id" });
    const item = ledger.items.find((row) => row.id === input.id);
    if (!item) return respond(404, { error: "commentary_not_found" });
    let user;
    try { user = await adapters.currentUser(env, request); } catch (_) { return respond(401, { error: "login_required" }); }
    if (!user?.id || user.disabled === true || user.account_status === "disabled") return respond(401, { error: "login_required" });
    // Existing website membership authority is reused. Storage/auth failures
    // must not silently become free access, and report trial quotas are untouched.
    const member = await adapters.membership(env, user);
    const stored = await readObject(bucket, `${ENGLISH_PREFIX}/bodies/${item.body_sha256}.json`, 512 * 1024);
    requireValue(stored && await sha256(stored.raw) === item.body_sha256);
    const body = validateEnglishBody(stored.value, item);
    const access = member ? { allowed: true, remaining: null, reused: false }
      : await consumeEnglishRead(bucket, String(user.id), item.id);
    if (!access.allowed) return respond(402, { error: "membership_required", remaining: 0, free_reads: ENGLISH_FREE_READS,
      request_action: { type: "membership_request", request_kind: "access" } });
    return respond(200, { ...previewRecord(item), blocks: body.blocks, policy: ENGLISH_COMMENTARY_POLICY,
      access: member ? "member" : "free", remaining: access.remaining, reused: access.reused });
  } catch (_) {
    // Never serialize object keys, raw editorial prose or credential errors.
    return respond(503, { error: "commentary_temporarily_unavailable" });
  }
}
