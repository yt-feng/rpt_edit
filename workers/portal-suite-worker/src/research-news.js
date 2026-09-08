// Fixed feeds are linked by the publishers' official RSS directories:
// https://www.eia.gov/tools/rssfeeds/
// https://www.federalreserve.gov/feeds/feeds.htm
// Both use RSS 2.0 item/title/link/description/pubDate. Only descriptions are
// evidence; neither a DOC search title nor an invented summary is accepted.
const FEEDS = Object.freeze([
  Object.freeze({ url: "https://www.eia.gov/rss/todayinenergy.xml", host: "eia.gov", publisher: "U.S. Energy Information Administration" }),
  Object.freeze({ url: "https://www.federalreserve.gov/feeds/feds_notes.xml", host: "federalreserve.gov", publisher: "Federal Reserve Board" }),
]);
const MAX_RESPONSE_BYTES = 256 * 1024; // Two requests together are <= 512 KiB.
const MAX_SOURCES = 4;
const MAX_ITEMS_PER_FEED = 100;
const MAX_DESCRIPTION_CHARS = 2400;
const MAX_AGE_MS = 90 * 24 * 60 * 60 * 1000;
const STAGE = "research-news-rss";

class NewsEvidenceError extends Error {
  constructor(code) { super(code); this.code = code; }
}

function result(status, reason, sources = []) {
  return { status, reason, provider: "official-rss", sources };
}

function plannerPhrases(query) {
  const values = Array.isArray(query) ? query : [query];
  if (!values.length || values.length > 3) return [];
  const phrases = [];
  for (const value of values) {
    if (typeof value !== "string" || value.length > 100) return [];
    const phrase = value.trim().replace(/\s+/g, " ");
    // The caller supplies English core phrases, never raw user search syntax.
    if (!/^[A-Za-z][A-Za-z0-9 '\-]{1,99}$/.test(phrase)
      || /\b(?:OR|AND|NOT)\b/.test(phrase)
      || phrase.split(" ").length > 10) return [];
    phrases.push(phrase.toLowerCase());
  }
  return [...new Set(phrases)];
}

function decodeEntities(value) {
  const named = { amp: "&", lt: "<", gt: ">", quot: '"', apos: "'", nbsp: " ", ndash: "–", mdash: "—", rsquo: "’", lsquo: "‘", rdquo: "”", ldquo: "“" };
  return value.replace(/&(#x[0-9a-f]+|#\d+|[a-z]+);/gi, (whole, entity) => {
    const key = entity.toLowerCase();
    if (Object.hasOwn(named, key)) return named[key];
    if (!key.startsWith("#")) return " ";
    const number = Number.parseInt(key.slice(key.startsWith("#x") ? 2 : 1), key.startsWith("#x") ? 16 : 10);
    return number > 0 && number <= 0x10ffff && !(number >= 0xd800 && number <= 0xdfff) ? String.fromCodePoint(number) : " ";
  });
}

function plainText(value, limit) {
  let text = String(value || "").slice(0, 32000).replace(/<!\[CDATA\[([\s\S]*?)\]\]>/g, "$1");
  // Decode before removing markup, including common double-encoded fragments.
  for (let pass = 0; pass < 2; pass += 1) text = decodeEntities(text);
  return text.replace(/<!--[\s\S]*?-->/g, " ")
    .replace(/<(script|style|iframe|object)\b[^>]*>[\s\S]*?<\/\1\s*>/gi, " ")
    .replace(/<[^>]*>/g, " ").replace(/[<>]/g, " ")
    .replace(/[\u0000-\u001f\u007f\u200b-\u200f\u202a-\u202e\u2060-\u206f\ufeff]/g, " ")
    .replace(/\s+/g, " ").trim().slice(0, limit);
}

function tag(block, name) {
  return block.match(new RegExp(`<${name}\\b[^>]*>([\\s\\S]*?)<\\/${name}\\s*>`, "i"))?.[1] || "";
}

function publicSourceUrl(value, feed) {
  const raw = plainText(value, 2049);
  if (!raw || raw.length > 2048 || /[\s\\]/.test(raw)) return "";
  try {
    const url = new URL(raw);
    const host = url.hostname.toLowerCase();
    // Sources must stay at the fixed publisher, which also excludes IPs,
    // localhost, credentials, ports, and unrelated links injected into a feed.
    if (url.protocol !== "https:" || url.username || url.password || url.port
      || !(host === feed.host || host === `www.${feed.host}`)) return "";
    if (url.pathname === "/" || (url.pathname.endsWith("detail.php") && !url.searchParams.get("id"))) return "";
    url.hash = "";
    for (const key of [...url.searchParams.keys()]) {
      if (/^utm_/i.test(key) || /^(fbclid|gclid|msclkid)$/i.test(key)) url.searchParams.delete(key);
    }
    return url.href;
  } catch { return ""; }
}

function words(value) {
  return String(value).toLowerCase().replace(/\bartificial intelligence\b/g, "ai")
    .replace(/\bcentres?\b/g, "center").replace(/\bdata centres?\b/g, "data center")
    .match(/[a-z0-9]+/g)?.map((word) => word.length > 4 && word.endsWith("s") ? word.slice(0, -1) : word) || [];
}

function matchesPhrase(textWords, phrase) {
  return words(phrase).every((word) => textWords.has(word));
}

function parseFeed(xml, feed, phrases, nowMs) {
  if (/<!DOCTYPE|<!ENTITY/i.test(xml) || !/<rss\b/i.test(xml) || !/<\/rss\s*>/i.test(xml)) throw new NewsEvidenceError("invalid_xml");
  const candidates = [];
  const blocks = xml.match(/<item\b[^>]*>[\s\S]*?<\/item\s*>/gi) || [];
  for (const block of blocks.slice(0, MAX_ITEMS_PER_FEED)) {
    const title = plainText(tag(block, "title"), 420);
    const text = plainText(tag(block, "description"), MAX_DESCRIPTION_CHARS);
    const sourceUrl = publicSourceUrl(tag(block, "link"), feed);
    if (!title || !sourceUrl || text.length < 80 || (text.match(/[\p{L}\p{N}]/gu) || []).length < 60
      || text.toLowerCase() === title.toLowerCase()) continue;
    const allWords = new Set(words(`${title} ${text}`));
    const bodyWords = new Set(words(text));
    if (!phrases.every((phrase) => matchesPhrase(allWords, phrase))
      || !phrases.some((phrase) => matchesPhrase(bodyWords, phrase))) continue;
    const published = Date.parse(plainText(tag(block, "pubDate"), 100));
    if (Number.isFinite(published) && (published > nowMs + 5 * 60 * 1000 || published < nowMs - MAX_AGE_MS)) continue;
    candidates.push({
      title, source_url: sourceUrl, publisher: feed.publisher, institution: feed.publisher,
      observed_at: new Date(nowMs).toISOString(),
      published_at: Number.isFinite(published) ? new Date(published).toISOString() : "",
      evidence_kind: "news_snippet", text_scope: "rss_description", provider: "official-rss",
      evidence: [{ kind: "news_snippet", text }],
      score: phrases.reduce((sum, phrase) => sum + (matchesPhrase(new Set(words(title)), phrase) ? 2 : 1), 0),
    });
  }
  return candidates.sort((a, b) => b.score - a.score || b.published_at.localeCompare(a.published_at));
}

async function readBoundedXml(response, signal) {
  if (response.status >= 300 && response.status < 400) throw new NewsEvidenceError("redirect");
  if (!response.ok) throw new NewsEvidenceError(response.status === 429 ? "rate_limited" : "http_error");
  if (!/\b(?:xml|rss\+xml)\b/i.test(response.headers.get("content-type") || "")) throw new NewsEvidenceError("content_type");
  if (Number(response.headers.get("content-length")) > MAX_RESPONSE_BYTES) throw new NewsEvidenceError("response_too_large");
  if (!response.body || typeof response.body.getReader !== "function") throw new NewsEvidenceError("missing_stream");
  const reader = response.body.getReader();
  const chunks = [];
  let size = 0;
  const cancel = () => { void reader.cancel().catch(() => {}); };
  signal.addEventListener("abort", cancel, { once: true });
  try {
    while (true) {
      if (signal.aborted) throw new NewsEvidenceError("timeout");
      const { done, value } = await reader.read();
      if (done) break;
      size += value.byteLength;
      if (size > MAX_RESPONSE_BYTES) { cancel(); throw new NewsEvidenceError("response_too_large"); }
      chunks.push(value);
    }
    if (signal.aborted) throw new NewsEvidenceError("timeout");
    const bytes = new Uint8Array(size);
    let offset = 0;
    for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
    const declaration = new TextDecoder().decode(bytes.subarray(0, 200));
    const encoding = declaration.match(/<\?xml\b[^>]*\bencoding=["']([^"']+)/i)?.[1] || "utf-8";
    if (/^(iso-8859-1|latin1)$/i.test(encoding)) {
      let xml = "";
      for (const byte of bytes) xml += String.fromCharCode(byte);
      return xml;
    }
    if (!/^utf-?8$/i.test(encoding)) throw new NewsEvidenceError("unsupported_encoding");
    return new TextDecoder("utf-8", { fatal: true }).decode(bytes);
  } finally {
    signal.removeEventListener("abort", cancel);
    try { reader.releaseLock(); } catch { /* A cancelled read may still settle. */ }
  }
}

async function fetchFeed(feed, fetchImpl, consumeBudget, timeoutMs) {
  try {
    if (consumeBudget && consumeBudget(1, STAGE) === false) return { error: "budget_exhausted" };
  } catch { return { error: "budget_exhausted" }; }
  const controller = new AbortController();
  let timer;
  try {
    return await Promise.race([
      (async () => {
        const response = await fetchImpl(feed.url, { method: "GET", redirect: "manual", signal: controller.signal, headers: { Accept: "application/rss+xml,application/xml,text/xml" } });
        if (controller.signal.aborted) { void response.body?.cancel().catch(() => {}); throw new NewsEvidenceError("timeout"); }
        const xml = await readBoundedXml(response, controller.signal);
        return { xml, feed };
      })(),
      new Promise((_, reject) => {
        timer = setTimeout(() => { controller.abort(); reject(new NewsEvidenceError("timeout")); }, timeoutMs);
      }),
    ]);
  } catch (error) {
    controller.abort();
    return { error: error instanceof NewsEvidenceError ? error.code : "fetch_failed" };
  } finally { clearTimeout(timer); }
}

/**
 * English planner core phrases -> <= 2 fixed publisher RSS requests.
 * No GDELT Context parser is shipped until an official JSON fixture is verified.
 * No cache reads/writes or source-page fetches occur. Every feed request spends
 * consumeBudget(1, "research-news-rss") before it starts; false/throw refuses it.
 * observed_at is our RSS retrieval time, not a claimed publication timestamp.
 */
export async function researchNewsEvidence({ query, fetchImpl = globalThis.fetch, now = Date.now(), consumeBudget = null, timeoutMs = 5500 } = {}) {
  const phrases = plannerPhrases(query);
  if (!phrases.length) return result("empty", "invalid_query");
  const nowMs = now instanceof Date ? now.getTime() : typeof now === "number" ? now : Date.parse(now);
  if (!Number.isFinite(nowMs)) return result("unavailable", "invalid_clock");
  const boundedTimeout = Math.max(1, Math.min(6000, Number(timeoutMs) || 5500));
  const feeds = await Promise.all(FEEDS.map((feed) => fetchFeed(feed, fetchImpl, consumeBudget, boundedTimeout)));
  const candidates = [];
  let parsed = 0;
  for (const response of feeds) {
    if (response.error) continue;
    try { candidates.push(...parseFeed(response.xml, response.feed, phrases, nowMs)); parsed += 1; }
    catch (error) { response.error = error instanceof NewsEvidenceError ? error.code : "invalid_xml"; }
  }
  if (!parsed) return result("unavailable", feeds.find((feed) => feed.error)?.error || "no_feed");
  const seenUrls = new Set();
  const seenPublishers = new Set();
  const sources = [];
  try {
    for (const candidate of candidates.sort((a, b) => b.score - a.score || b.published_at.localeCompare(a.published_at))) {
      if (seenUrls.has(candidate.source_url) || seenPublishers.has(candidate.publisher)) continue;
      const hash = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(candidate.source_url));
      const id = `news:${[...new Uint8Array(hash)].map((value) => value.toString(16).padStart(2, "0")).join("")}`;
      const { score, ...source } = candidate;
      sources.push({ id, ...source });
      seenUrls.add(source.source_url); seenPublishers.add(source.publisher);
      if (sources.length >= MAX_SOURCES) break;
    }
  } catch { return result("unavailable", "normalization_failed"); }
  return result(sources.length ? "success" : "empty", sources.length ? (parsed < FEEDS.length ? "partial_feeds" : "matched") : "no_matching_snippets", sources);
}
