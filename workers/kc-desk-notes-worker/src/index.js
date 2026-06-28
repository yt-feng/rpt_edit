const CACHE_TTL_MS = 5 * 60 * 1000;
const DEFAULT_R2_PREFIX = "reports";
const CONTACT_WECHAT = "macroGate";
const ADMIN_TOKEN_TTL_SECONDS = 180 * 24 * 60 * 60;

// Reportify (reportify.cn) integration. The reports search + detail endpoints are
// public (no login); only some PDFs are directly downloadable. See handleReportify*.
const REPORTIFY_API = "https://api.reportify.cn";
const REPORTIFY_SITE = "https://reportify.cn";
const REPORTIFY_R2_PREFIX = "reportify";
const REPORTIFY_SEARCH_PAGE_SIZE = 20;
const REPORTIFY_UA =
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
    "Access-Control-Allow-Headers": "Content-Type",
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

async function passwordMatches(env, group, password) {
  const expected = String(group.password_sha256 || "");
  if (!expected || expected === "REPLACE_WITH_SHA256_HASH") {
    throw new Error(`Password hash is not configured for group: ${group.id}`);
  }
  if (!env.PASSWORD_SECRET) throw new Error("PASSWORD_SECRET is not configured");
  const actual = await sha256Hex(`${env.PASSWORD_SECRET}:${password}`);
  return actual === expected.toLowerCase();
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
  if (!password) {
    return jsonResponse(request, env, 400, { error: "Password is required." });
  }

  let catalog;
  try {
    catalog = await loadCatalog(env);
  } catch (_error) {
    return jsonResponse(request, env, 503, { error: "Download service is not configured." });
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

  if (!env.REPORT_BUCKET) {
    return jsonResponse(request, env, 503, { error: "Download storage is not configured." });
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
  if (!/^[a-f0-9]{16,64}$/i.test(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }

  try {
    await verifyAdminToken(env, token);
  } catch (error) {
    return jsonResponse(request, env, 401, { error: error.message || "Admin session is invalid." });
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
// Reportify integration
// ---------------------------------------------------------------------------

function reportifyHeaders() {
  return {
    "User-Agent": REPORTIFY_UA,
    "Referer": `${REPORTIFY_SITE}/`,
    "Accept": "application/json",
  };
}

function reportifyObjectKey(id) {
  return `${REPORTIFY_R2_PREFIX}/${id}.pdf`;
}

function isReportifyId(value) {
  return /^[0-9]{6,25}$/.test(String(value || "").trim());
}

function reportifyIsoDate(publishAt) {
  const ms = Number(publishAt || 0);
  if (!ms) return "";
  try {
    return new Date(ms).toISOString().slice(0, 10);
  } catch (_error) {
    return "";
  }
}

// Map a raw reportify report record to the slim shape the frontend renders.
function slimReportifyItem(item) {
  const title = String(item.title || item.title_cn || "").trim();
  const summary = String(item.summary || "").replace(/\s+/g, " ").trim();
  return {
    id: String(item.report_id || ""),
    title: title || "Untitled report",
    title_cn: String(item.title_cn || "").trim(),
    institution: String(item.institution_name || item.channel_name || "").trim(),
    date: reportifyIsoDate(item.publish_at),
    file_type: String(item.file_type || "").trim(),
    summary: summary.length > 220 ? `${summary.slice(0, 220)}…` : summary,
  };
}

async function handleReportifySearch(request, env) {
  const url = new URL(request.url);
  const query = String(url.searchParams.get("q") || "").trim();
  const page = Math.max(1, Number(url.searchParams.get("page") || "1") || 1);
  if (!query) {
    return jsonResponse(request, env, 200, { items: [], page: 1, total_page: 0 });
  }

  const target = new URL(`${REPORTIFY_API}/reports`);
  target.searchParams.set("query", query);
  target.searchParams.set("page_num", String(page));
  target.searchParams.set("page_size", String(REPORTIFY_SEARCH_PAGE_SIZE));

  let data;
  try {
    const upstream = await fetch(target.toString(), { headers: reportifyHeaders() });
    if (!upstream.ok) {
      return jsonResponse(request, env, 502, { error: "Reportify search is unavailable." });
    }
    data = await upstream.json();
  } catch (_error) {
    return jsonResponse(request, env, 502, { error: "Reportify search is unavailable." });
  }

  const items = Array.isArray(data.items) ? data.items.map(slimReportifyItem).filter((it) => it.id) : [];
  return jsonResponse(request, env, 200, {
    items,
    page: Number(data.page_num || page),
    total_page: Number(data.total_page || 0),
  });
}

// Fetch the reportify detail and, if the report is directly readable, return its
// presigned PDF url. Returns "" when the PDF is gated (needs a browser grab).
async function reportifyDirectPdfUrl(id) {
  try {
    const resp = await fetch(`${REPORTIFY_API}/reports/${id}`, { headers: reportifyHeaders() });
    if (!resp.ok) return { url: "", title: "" };
    const data = await resp.json();
    const main = data.main || {};
    return { url: String(main.url_pdf || "").trim(), title: String(main.title || main.title_cn || "").trim() };
  } catch (_error) {
    return { url: "", title: "" };
  }
}

function reportifyPdfResponse(request, env, body, title, id) {
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

// Ask GitHub to run the reportify-grab workflow for a gated report. Returns true
// when the dispatch was accepted (HTTP 204).
async function triggerReportifyGrab(env, id) {
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
      body: JSON.stringify({ event_type: "reportify-grab", client_payload: { id } }),
    });
    return resp.ok;
  } catch (_error) {
    return false;
  }
}

async function handleReportifyPdf(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!isReportifyId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }

  // 1) Directly readable reports expose a presigned PDF url - stream it (instant).
  const direct = await reportifyDirectPdfUrl(id);
  if (direct.url) {
    try {
      const pdf = await fetch(direct.url, { headers: { "User-Agent": REPORTIFY_UA } });
      if (pdf.ok) {
        return reportifyPdfResponse(request, env, pdf.body, direct.title, id);
      }
    } catch (_error) {
      // Fall through to the R2 / grab paths below.
    }
  }

  // 2) Already grabbed by the workflow and mirrored to R2.
  if (env.REPORT_BUCKET) {
    const object = await env.REPORT_BUCKET.get(reportifyObjectKey(id));
    if (object) {
      return reportifyPdfResponse(request, env, object.body, direct.title, id);
    }
  }

  // 3) Gated and not yet grabbed - kick off the browser grab in GitHub Actions.
  const dispatched = await triggerReportifyGrab(env, id);
  if (dispatched) {
    return jsonResponse(request, env, 202, {
      status: "pending",
      wait_seconds: 120,
      source_url: `${REPORTIFY_SITE}/reports/${id}`,
    });
  }
  return jsonResponse(request, env, 503, {
    error: "This report needs a background download, which is not configured.",
    source_url: `${REPORTIFY_SITE}/reports/${id}`,
  });
}

async function handleReportifyStatus(request, env) {
  const url = new URL(request.url);
  const id = String(url.searchParams.get("id") || "").trim();
  if (!isReportifyId(id)) {
    return jsonResponse(request, env, 400, { error: "Invalid report id." });
  }
  let ready = false;
  if (env.REPORT_BUCKET) {
    const head = await env.REPORT_BUCKET.head(reportifyObjectKey(id));
    ready = Boolean(head);
  }
  return jsonResponse(request, env, 200, { ready });
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

    if (pathname === "/admin/login" && request.method === "POST") {
      return handleAdminLogin(request, env);
    }

    if (pathname === "/admin/report-password" && request.method === "POST") {
      return handleAdminReportPassword(request, env);
    }

    if (pathname === "/reportify/search" && request.method === "GET") {
      return handleReportifySearch(request, env);
    }

    if (pathname === "/reportify/pdf" && request.method === "GET") {
      return handleReportifyPdf(request, env);
    }

    if (pathname === "/reportify/status" && request.method === "GET") {
      return handleReportifyStatus(request, env);
    }

    return jsonResponse(request, env, 404, { error: "Not found." });
  },
};
