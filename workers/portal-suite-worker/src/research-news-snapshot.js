const KEY = "_research-news/v1/snapshot.json";
const MAX_BYTES = 2 * 1024 * 1024;
const CACHE = new WeakMap();

function text(value, limit = 800) {
  return String(value || "").normalize("NFKC").replace(/<[^>]*>/gu, " ")
    .replace(/[\u0000-\u001f\u007f]/gu, " ").replace(/\s+/gu, " ").trim().slice(0, limit);
}

export function researchNewsPublicUrl(value) {
  try {
    const url = new URL(value), host = url.hostname.toLowerCase();
    if (url.protocol !== "https:" || url.username || url.password || url.port
      || !/^[a-z0-9.-]+\.[a-z]{2,}$/u.test(host)
      || /(?:^|\.)(?:localhost|local|internal|invalid|test|example)$/u.test(host)) return "";
    return url.href;
  } catch { return ""; }
}

async function boundedJson(object) {
  if (Number(object.size) > MAX_BYTES) throw new Error("oversize");
  if (!object.body?.getReader) {
    const raw = await object.text();
    if (new TextEncoder().encode(raw).length > MAX_BYTES) throw new Error("oversize");
    return JSON.parse(raw);
  }
  const reader = object.body.getReader(), chunks = [];
  let length = 0;
  try {
    for (;;) {
      const { done, value } = await reader.read();
      if (done) break;
      length += value.byteLength;
      if (length > MAX_BYTES) { await reader.cancel(); throw new Error("oversize"); }
      chunks.push(value);
    }
  } finally { reader.releaseLock(); }
  const bytes = new Uint8Array(length);
  let offset = 0;
  for (const chunk of chunks) { bytes.set(chunk, offset); offset += chunk.byteLength; }
  return JSON.parse(new TextDecoder("utf-8", { fatal: true }).decode(bytes));
}

function matches(value, terms) {
  const normalized = value.toLowerCase().replace(/[-_]/gu, " ");
  return terms.some((term) => {
    const token = text(term, 100).toLowerCase().replace(/[-_]/gu, " ");
    return token && (/^[a-z0-9 ]+$/u.test(token) ? ` ${normalized.replace(/[^a-z0-9 ]/gu, " ")} `.includes(` ${token} `) : normalized.includes(token));
  });
}

function matchesGroup(value, group) {
  const terms = group.terms || [];
  if (terms.includes("datacenter") || (terms.includes("data") && terms.includes("center"))) {
    return /\bdata[\s-]*cent(?:er|re)s?\b|\bdatacenters?\b|\baidc\b|数据中心|算力中心/iu.test(value);
  }
  return matches(value, terms);
}

/** One bounded R2 read, with a short isolate cache; no upstream article fetches. */
export async function readResearchNewsSnapshot({ bucket, groups = [], now = Date.now(), consumeBudget } = {}) {
  const empty = (reason) => ({ status: reason === "no_matches" ? "empty" : "unavailable", reason, sources: [] });
  if (!bucket || !groups.length) return empty("not_configured");
  try {
    let snapshot = CACHE.get(bucket);
    if (!snapshot || snapshot.until < now) {
      if (consumeBudget && consumeBudget(1, "research-news-snapshot") === false) return empty("budget");
      const object = await bucket.get(KEY);
      if (!object) return empty("not_ready");
      const data = await boundedJson(object);
      if (data.schema_version !== 1 || !Array.isArray(data.items) || data.items.length > 1800) return empty("invalid_snapshot");
      snapshot = { until: now + 120000, data };
      CACHE.set(bucket, snapshot);
    }
    const age = now - Date.parse(snapshot.data.updated_at);
    if (!Number.isFinite(age) || age < -3600000 || age > 7 * 86400000) return empty("stale_snapshot");
    const core = groups.filter((group) => group.role === "core" && group.required !== false);
    const ranked = snapshot.data.items.map((row) => {
      const title = text(row.title, 350), summary = text(row.summary, 1200), url = researchNewsPublicUrl(row.source_url);
      const observed = Date.parse(row.observed_at), content = `${title} ${summary}`;
      if (!/^news:[a-f0-9]{64}$/u.test(row.id) || !url || !title || summary.length < 80
        || summary === title || !Number.isFinite(observed) || now - observed > 7 * 86400000 || observed - now > 3600000) return null;
      if (core.length && !core.every((group) => matchesGroup(content, group))) return null;
      const score = groups.reduce((sum, group) => sum + (matchesGroup(content, group) ? (group.role === "core" ? 3 : 1) : 0), 0);
      return score ? { row, title, summary, url, observed, score } : null;
    }).filter(Boolean).sort((a, b) => b.score - a.score || b.observed - a.observed);
    const sources = [], domains = new Set(), urls = new Set();
    for (const { row, title, summary, url } of ranked) {
      const domain = new URL(url).hostname.replace(/^www\./u, "");
      if (domains.has(domain) || urls.has(url)) continue;
      const digest = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(url));
      const id = `news:${Array.from(new Uint8Array(digest), (byte) => byte.toString(16).padStart(2, "0")).join("")}`;
      sources.push({ id, title, source_url: url, institution: text(row.institution || row.outlet || domain, 160),
        observed_at: new Date(row.observed_at).toISOString(), published_at: "", language: text(row.language, 20),
        provider: "gdelt-gal", evidence_kind: "news_description", text_scope: "publisher_description",
        evidence: [{ id, kind: "news_description", text: `${title}。${summary}` }] });
      domains.add(domain); urls.add(url);
      if (sources.length >= 4) break;
    }
    return sources.length ? { status: "success", reason: "matched", sources } : empty("no_matches");
  } catch { return empty("snapshot_unavailable"); }
}
