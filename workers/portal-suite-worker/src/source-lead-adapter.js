const SOURCE_LEAD_SOURCE = "supplemental";
const SOURCE_LEAD_PAGE_SIZE = 20;
const SOURCE_LEAD_MAX_QUERY_LENGTH = 160;
const SOURCE_LEAD_MAX_TEXT_LENGTH = 1200;
const SOURCE_LEAD_MAX_ITEMS = 50;
const SOURCE_LEAD_TIMEOUT_MS = 15000;
const SOURCE_LEAD_ID_PATTERN = /^supplemental:[a-f0-9]{32}$/;
const SOURCE_LEAD_R2_PREFIX = "_source-leads/items";

class SourceLeadAdapterError extends Error {
  constructor(code, message) {
    super(message);
    this.name = "SourceLeadAdapterError";
    this.code = code;
  }
}

function compactText(value, maxLength = SOURCE_LEAD_MAX_TEXT_LENGTH) {
  return String(value == null ? "" : value)
    .replace(/[\u0000-\u001f\u007f]+/g, " ")
    .replace(/[\u200b-\u200d\u2060\ufeff\ue000-\uf8ff]+/gu, " ")
    .replace(/\s+/g, " ")
    .trim()
    .slice(0, maxLength);
}

function decodeHtmlEntities(value) {
  const named = {
    amp: "&",
    apos: "'",
    gt: ">",
    hellip: "…",
    ldquo: "“",
    lt: "<",
    nbsp: " ",
    quot: '"',
    rdquo: "”",
  };
  return String(value || "").replace(/&(#x?[0-9a-f]+|[a-z]+);/gi, (match, entity) => {
    const normalized = String(entity).toLowerCase();
    if (Object.prototype.hasOwnProperty.call(named, normalized)) return named[normalized];
    if (!normalized.startsWith("#")) return " ";
    const radix = normalized.startsWith("#x") ? 16 : 10;
    const digits = normalized.slice(radix === 16 ? 2 : 1);
    const codePoint = Number.parseInt(digits, radix);
    if (!Number.isFinite(codePoint) || codePoint <= 0 || codePoint > 0x10ffff) return " ";
    try {
      return String.fromCodePoint(codePoint);
    } catch (_error) {
      return " ";
    }
  });
}

function stripHtml(value) {
  return compactText(decodeHtmlEntities(String(value || "")
    .replace(/<script\b[\s\S]*?<\/script>/gi, " ")
    .replace(/<style\b[\s\S]*?<\/style>/gi, " ")
    .replace(/<[^>]+>/g, " ")));
}

function escapeRegExp(value) {
  return String(value || "").replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

function configuredRedactions(env, upstreamUrl) {
  const terms = compactText(env && env.SUPPLEMENTAL_SEARCH_REDACT_TERMS, 2000)
    .split(/[\n,;|]+/)
    .map((entry) => compactText(entry, 120))
    .filter((entry) => entry.length >= 2);
  try {
    const hostname = new URL(upstreamUrl).hostname.toLowerCase();
    terms.push(hostname);
    for (const label of hostname.split(".")) {
      if (label.length >= 4 && label !== "www") terms.push(label);
    }
  } catch (_error) {
    // The URL is validated before an upstream request is made.
  }
  return [...new Set(terms)];
}

function redactPublicText(value, redactions, maxLength = SOURCE_LEAD_MAX_TEXT_LENGTH) {
  let result = compactText(value, maxLength * 2)
    .replace(/\bhttps?:\/\/[^\s<>()]+/gi, " ")
    .replace(/\b[^\s@]+@[^\s@]+\.[^\s@]+\b/gi, " ");
  for (const term of redactions || []) {
    result = result.replace(new RegExp(escapeRegExp(term), "gi"), " ");
  }
  return compactText(result, maxLength);
}

function normalizeDate(value) {
  const text = compactText(value, 80);
  const match = text.match(/(20\d{2})[-/.年](\d{1,2})[-/.月](\d{1,2})/);
  if (!match) return text.slice(0, 32);
  return `${match[1]}-${match[2].padStart(2, "0")}-${match[3].padStart(2, "0")}`;
}

function normalizePageCount(value) {
  if (Number.isFinite(Number(value))) {
    const count = Math.floor(Number(value));
    return count > 0 && count <= 100000 ? count : null;
  }
  const match = compactText(value, 120).match(/(\d{1,6})\s*(?:pages?|页)/i);
  return match ? Number(match[1]) : null;
}

function normalizeTags(value, redactions) {
  const values = Array.isArray(value) ? value : String(value || "").split(/[,;|]/);
  return [...new Set(values
    .map((entry) => redactPublicText(entry, redactions, 80))
    .filter(Boolean))]
    .slice(0, 12);
}

function firstValue(row, keys) {
  for (const key of keys) {
    if (row && row[key] != null && row[key] !== "") return row[key];
  }
  return "";
}

function normalizeLocator(value, upstreamUrl) {
  const raw = compactText(value, 2048);
  if (!raw) return "";
  try {
    const resolved = new URL(raw, upstreamUrl);
    if (resolved.protocol !== "https:") return "";
    resolved.hash = "";
    return resolved.toString();
  } catch (_error) {
    return "";
  }
}

function normalizeRawItem(row, upstreamUrl, redactions) {
  if (!row || typeof row !== "object") return null;
  const locator = normalizeLocator(firstValue(row, [
    "locator", "url", "href", "link", "report_url", "detail_url",
  ]), upstreamUrl);
  const fallbackLocator = locator || normalizeLocator(
    firstValue(row, ["id", "report_id", "reportId"]),
    upstreamUrl,
  );
  const title = redactPublicText(firstValue(row, [
    "title", "name", "report_title", "reportTitle",
  ]), redactions, 500);
  if (!fallbackLocator || !title) return null;
  return {
    locator: fallbackLocator,
    title,
    date: normalizeDate(firstValue(row, ["date", "published_at", "publishedAt", "time"])),
    institution: redactPublicText(firstValue(row, [
      "institution", "publisher", "organization", "org", "agency",
    ]), redactions, 240).replace(/[\s·|,;/—–-]+$/g, ""),
    page_count: normalizePageCount(firstValue(row, [
      "page_count", "pageCount", "pages", "page_total",
    ])),
    tags: normalizeTags(firstValue(row, ["tags", "keywords", "topics"]), redactions),
    summary: redactPublicText(firstValue(row, [
      "summary", "description", "abstract", "excerpt",
    ]), redactions, 900),
  };
}

function pickJsonRows(payload) {
  if (Array.isArray(payload)) return payload;
  if (!payload || typeof payload !== "object") return [];
  for (const key of ["items", "results", "records", "data", "list"]) {
    if (Array.isArray(payload[key])) return payload[key];
    if (payload[key] && typeof payload[key] === "object") {
      for (const nested of ["items", "results", "records", "list"]) {
        if (Array.isArray(payload[key][nested])) return payload[key][nested];
      }
    }
  }
  return [];
}

function pickJsonTotal(payload, fallback) {
  if (!payload || typeof payload !== "object" || Array.isArray(payload)) return fallback;
  const candidates = [
    payload.total,
    payload.total_count,
    payload.count,
    payload.pagination && payload.pagination.total,
    payload.data && payload.data.total,
  ];
  for (const candidate of candidates) {
    const value = Number(candidate);
    if (Number.isFinite(value) && value >= 0) return Math.floor(value);
  }
  return fallback;
}

function htmlClassBlock(body, className, tagPattern = "[a-z0-9]+") {
  const pattern = new RegExp(
    `<(${tagPattern})\\b[^>]*class=["'][^"']*\\b${escapeRegExp(className)}\\b[^"']*["'][^>]*>([\\s\\S]*?)<\\/\\1>`,
    "i",
  );
  const match = String(body || "").match(pattern);
  return match ? match[2] : "";
}

function htmlClassBlocks(body, className, tagPattern = "[a-z0-9]+") {
  const pattern = new RegExp(
    `<(${tagPattern})\\b[^>]*class=["'][^"']*\\b${escapeRegExp(className)}\\b[^"']*["'][^>]*>([\\s\\S]*?)<\\/\\1>`,
    "gi",
  );
  const rows = [];
  let match;
  while ((match = pattern.exec(String(body || ""))) && rows.length < 40) rows.push(match[2]);
  return rows;
}

function attrValue(fragment, attribute) {
  const match = String(fragment || "").match(new RegExp(`\\b${escapeRegExp(attribute)}\\s*=\\s*["']([^"']+)["']`, "i"));
  return match ? decodeHtmlEntities(match[1]) : "";
}

function parseHtmlItems(body, upstreamUrl, redactions) {
  const items = [];
  const articlePattern = /<article\b([^>]*)>([\s\S]*?)<\/article>/gi;
  let articleMatch;
  while ((articleMatch = articlePattern.exec(String(body || ""))) && items.length < SOURCE_LEAD_MAX_ITEMS) {
    const opening = articleMatch[1] || "";
    if (!/\bexcerpt\b/i.test(attrValue(opening, "class"))) continue;
    const article = articleMatch[2] || "";
    const header = article.match(/<header\b[^>]*>([\s\S]*?)<\/header>/i);
    const titleScope = header ? header[1] : article;
    const heading = titleScope.match(/<h2\b[^>]*>([\s\S]*?)<\/h2>/i);
    const link = (heading ? heading[1] : titleScope).match(/<a\b([^>]*)>([\s\S]*?)<\/a>/i);
    if (!link) continue;

    const meta = htmlClassBlock(article, "meta");
    const categories = htmlClassBlocks(meta || article, "cat").map(stripHtml).filter(Boolean);
    const time = article.match(/<time\b([^>]*)>([\s\S]*?)<\/time>/i);
    const tagScope = htmlClassBlock(article, "article-tags");
    const tags = [];
    const tagPattern = /<a\b[^>]*>([\s\S]*?)<\/a>/gi;
    let tagMatch;
    while ((tagMatch = tagPattern.exec(tagScope)) && tags.length < 12) tags.push(stripHtml(tagMatch[1]));

    const institutionText = categories.find((value) => !/\d{1,6}\s*(?:pages?|页)/i.test(value)) || categories[0] || "";
    const pageText = categories.find((value) => /\d{1,6}\s*(?:pages?|页)/i.test(value)) || categories.join(" ");
    const normalized = normalizeRawItem({
      href: attrValue(link[1], "href"),
      title: stripHtml(link[2]),
      date: time ? attrValue(time[1], "datetime") || stripHtml(time[2]) : "",
      institution: institutionText.replace(/(?:\d{1,6}\s*(?:pages?|页)).*$/i, ""),
      pages: pageText,
      tags,
      summary: stripHtml(htmlClassBlock(article, "summary") || htmlClassBlock(article, "description")),
    }, upstreamUrl, redactions);
    if (normalized) items.push(normalized);
  }
  return items;
}

function parseHtmlTotal(body, fallback) {
  const text = stripHtml(body);
  for (const pattern of [
    /(?:total|共)\s*[:：]?\s*(\d{1,9})\s*(?:results?|records?|条|份|篇)?/i,
    /(\d{1,9})\s*(?:results?|records?|条结果|份报告)/i,
  ]) {
    const match = text.match(pattern);
    if (match) return Number(match[1]);
  }
  return fallback;
}

function parseHtmlHasMore(body, itemCount) {
  const html = String(body || "");
  if (/<a\b[^>]*(?:rel=["']next["']|class=["'][^"']*\bnext\b[^"']*["'])/i.test(html)) return true;
  if (/<a\b[^>]*>\s*(?:next|下一页|下页|后页|›|»)[\s\S]*?<\/a>/i.test(html)) return true;
  return Number(itemCount) >= SOURCE_LEAD_PAGE_SIZE;
}

function parseUpstreamPayload(body, contentType, upstreamUrl, redactions) {
  const trimmed = String(body || "").trim();
  if (/json/i.test(contentType || "") || /^[{[]/.test(trimmed)) {
    let payload;
    try {
      payload = JSON.parse(trimmed);
    } catch (_error) {
      throw new SourceLeadAdapterError("INVALID_RESPONSE", "Supplemental search returned an invalid response.");
    }
    const items = pickJsonRows(payload)
      .slice(0, SOURCE_LEAD_MAX_ITEMS)
      .map((row) => normalizeRawItem(row, upstreamUrl, redactions))
      .filter(Boolean);
    const total = pickJsonTotal(payload, items.length);
    const hasMore = Boolean(
      payload && (payload.has_more === true || payload.hasMore === true)
      || items.length >= SOURCE_LEAD_PAGE_SIZE && total > items.length,
    );
    return { items, total, has_more: hasMore };
  }
  const items = parseHtmlItems(trimmed, upstreamUrl, redactions);
  return {
    items,
    total: parseHtmlTotal(trimmed, items.length),
    has_more: parseHtmlHasMore(trimmed, items.length),
  };
}

function configuredSearchUrl(env) {
  const value = compactText(env && env.SUPPLEMENTAL_SEARCH_URL, 2048);
  if (!value) return null;
  try {
    const url = new URL(value);
    if (url.protocol !== "https:") return null;
    url.hash = "";
    return url;
  } catch (_error) {
    return null;
  }
}

function hmacSecret(env) {
  const secret = String(env && env.SUPPLEMENTAL_SEARCH_HMAC_SECRET || "").trim();
  return secret.length >= 16 ? secret : "";
}

function sourceLeadAdapterEnabled(env) {
  return Boolean(configuredSearchUrl(env) && hmacSecret(env) && env && env.REPORT_BUCKET);
}

function buildUpstreamSearchUrl(env, query, page) {
  const url = configuredSearchUrl(env);
  if (!url) throw new SourceLeadAdapterError("NOT_CONFIGURED", "Supplemental search is not configured.");
  const normalizedPage = Math.max(1, Math.floor(Number(page) || 1));
  url.searchParams.set("q", query);
  url.searchParams.set("kw", query);
  url.searchParams.set("page", String(normalizedPage));
  url.searchParams.set("p", String(normalizedPage - 1));
  url.searchParams.set("page_size", String(SOURCE_LEAD_PAGE_SIZE));
  return url;
}

async function hmacHex(secret, message) {
  const encoder = new TextEncoder();
  const key = await crypto.subtle.importKey(
    "raw",
    encoder.encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign("HMAC", key, encoder.encode(message));
  return [...new Uint8Array(signature)].map((byte) => byte.toString(16).padStart(2, "0")).join("");
}

function sourceLeadStorageKey(id) {
  if (!SOURCE_LEAD_ID_PATTERN.test(String(id || ""))) return "";
  return `${SOURCE_LEAD_R2_PREFIX}/${String(id).slice("supplemental:".length)}.json`;
}

function publicSourceLeadItem(stored) {
  const metadata = stored && stored.metadata && typeof stored.metadata === "object" ? stored.metadata : {};
  return {
    id: compactText(stored && stored.id, 80),
    source: SOURCE_LEAD_SOURCE,
    title: redactPublicText(metadata.title, [], 500),
    date: normalizeDate(metadata.date),
    institution: redactPublicText(metadata.institution, [], 240),
    page_count: normalizePageCount(metadata.page_count),
    tags: normalizeTags(metadata.tags, []),
    summary: redactPublicText(metadata.summary, [], 900),
    contact_only: true,
  };
}

async function persistSourceLead(env, rawItem, query, now) {
  const digest = await hmacHex(hmacSecret(env), rawItem.locator);
  const id = `supplemental:${digest.slice(0, 32)}`;
  const stored = {
    version: 1,
    id,
    locator: rawItem.locator,
    query: compactText(query, SOURCE_LEAD_MAX_QUERY_LENGTH),
    metadata: {
      title: rawItem.title,
      date: rawItem.date,
      institution: rawItem.institution,
      page_count: rawItem.page_count,
      tags: rawItem.tags,
      summary: rawItem.summary,
    },
    updated_at: now,
  };
  await env.REPORT_BUCKET.put(sourceLeadStorageKey(id), JSON.stringify(stored), {
    httpMetadata: {
      contentType: "application/json; charset=utf-8",
      cacheControl: "private, no-store",
    },
  });
  return publicSourceLeadItem(stored);
}

async function searchSourceLeadMetadata({ env, query, page = 1, fetchImpl = fetch, now = null } = {}) {
  const normalizedQuery = compactText(query, SOURCE_LEAD_MAX_QUERY_LENGTH);
  const normalizedPage = Math.max(1, Math.floor(Number(page) || 1));
  const empty = {
    source: SOURCE_LEAD_SOURCE,
    query: normalizedQuery,
    page: normalizedPage,
    page_size: SOURCE_LEAD_PAGE_SIZE,
    total: 0,
    has_more: false,
    items: [],
  };
  if (normalizedQuery.length < 2) return empty;
  if (!sourceLeadAdapterEnabled(env)) {
    throw new SourceLeadAdapterError("NOT_CONFIGURED", "Supplemental search is not configured.");
  }

  const upstreamUrl = buildUpstreamSearchUrl(env, normalizedQuery, normalizedPage);
  const controller = new AbortController();
  const timeout = setTimeout(() => controller.abort(), SOURCE_LEAD_TIMEOUT_MS);
  let response;
  try {
    response = await fetchImpl(upstreamUrl.toString(), {
      method: "GET",
      headers: {
        Accept: "application/json, text/html;q=0.9",
        "User-Agent": "SupplementalMetadataSearch/1.0",
      },
      redirect: "follow",
      signal: controller.signal,
    });
  } catch (_error) {
    throw new SourceLeadAdapterError("UPSTREAM_UNAVAILABLE", "Supplemental search is temporarily unavailable.");
  } finally {
    clearTimeout(timeout);
  }
  if (!response || !response.ok) {
    throw new SourceLeadAdapterError("UPSTREAM_UNAVAILABLE", "Supplemental search is temporarily unavailable.");
  }

  let body;
  try {
    body = await response.text();
  } catch (_error) {
    throw new SourceLeadAdapterError("INVALID_RESPONSE", "Supplemental search returned an invalid response.");
  }
  const redactions = configuredRedactions(env, upstreamUrl);
  const parsed = parseUpstreamPayload(body, response.headers && response.headers.get("content-type"), upstreamUrl, redactions);
  const timestamp = compactText(now || new Date().toISOString(), 64);
  const results = await Promise.allSettled(parsed.items.map((item) => persistSourceLead(
    env,
    item,
    normalizedQuery,
    timestamp,
  )));
  const items = results
    .filter((result) => result.status === "fulfilled")
    .map((result) => result.value);
  if (parsed.items.length > 0 && items.length === 0) {
    throw new SourceLeadAdapterError("STORAGE_UNAVAILABLE", "Supplemental search is temporarily unavailable.");
  }
  const knownTotal = Math.max(items.length, Number(parsed.total) || 0);
  const minimumTotal = (normalizedPage - 1) * SOURCE_LEAD_PAGE_SIZE + items.length;
  const hasMore = Boolean(parsed.has_more || normalizedPage * SOURCE_LEAD_PAGE_SIZE < knownTotal);
  return {
    ...empty,
    total: Math.max(knownTotal, minimumTotal + (hasMore ? 1 : 0)),
    has_more: hasMore,
    items,
  };
}

async function readStoredSourceLead(env, id) {
  const key = sourceLeadStorageKey(id);
  if (!key || !env || !env.REPORT_BUCKET) return null;
  try {
    const object = await env.REPORT_BUCKET.get(key);
    if (!object) return null;
    const stored = JSON.parse(await object.text());
    if (!stored || stored.id !== id || !stored.locator || !stored.metadata) return null;
    return stored;
  } catch (_error) {
    return null;
  }
}

function sanitizeSourceLeadError(error) {
  if (error instanceof SourceLeadAdapterError) {
    return { code: error.code, message: error.message };
  }
  return { code: "UNAVAILABLE", message: "Supplemental search is temporarily unavailable." };
}

export {
  SOURCE_LEAD_PAGE_SIZE,
  SOURCE_LEAD_SOURCE,
  SourceLeadAdapterError,
  buildUpstreamSearchUrl,
  parseUpstreamPayload,
  publicSourceLeadItem,
  readStoredSourceLead,
  sanitizeSourceLeadError,
  searchSourceLeadMetadata,
  sourceLeadAdapterEnabled,
  sourceLeadStorageKey,
};
