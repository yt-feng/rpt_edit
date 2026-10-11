// Customer delivery only: no caller-supplied object keys, URLs or bucket prefixes.
import { CustomerContentApiError } from "./customer-content-api.js";

export const CONTENT_DATA_PREFIX = "_customer-content-data/v1";
const REPORT_ID = /^[a-f0-9]{24}$/;
const HASH = /^[a-f0-9]{64}$/;
const KINDS = new Set(["text", "image", "chart", "metadata", "translation", "article", "pdf"]);
const TYPES = new Set(["text/plain", "text/markdown", "application/json", "application/pdf", "image/jpeg", "image/png", "image/webp"]);
const MAX_JSON = 16 * 1024 * 1024;
const failure = (status, code) => { throw new CustomerContentApiError(status, code); };
const text = (value, limit = 500) => String(value || "").slice(0, limit);

export function contentDate(value) {
  let raw = String(value || "").replaceAll("-", "");
  if (/^\d{6}$/.test(raw)) raw = `20${raw}`;
  if (!/^20\d{6}$/.test(raw)) return "";
  const date = `${raw.slice(0, 4)}-${raw.slice(4, 6)}-${raw.slice(6, 8)}`;
  const time = Date.parse(`${date}T00:00:00Z`);
  return Number.isFinite(time) && new Date(time).toISOString().slice(0, 10) === date ? date : "";
}

async function readJson(bucket, key, maximum = MAX_JSON) {
  const object = await bucket.get(key);
  if (!object) return null;
  if (!Number.isSafeInteger(object.size) || object.size > maximum) failure(503, "service_unavailable");
  const raw = await object.text();
  if (new TextEncoder().encode(raw).length > maximum) failure(503, "service_unavailable");
  try { return JSON.parse(raw); } catch { failure(503, "service_unavailable"); }
}

export function publicContentReport(report) {
  if (!report || !REPORT_ID.test(report.id)) return null;
  return {
    id: report.id, title: text(report.title || report.filename), title_zh: text(report.title_zh),
    title_en: text(report.title_en), institution: text(report.bank_name || report.institution, 160),
    date: contentDate(report.date || report.date_folder), page_count: Math.max(0, Math.floor(Number(report.page_count) || 0)),
    pdf_listed: report.available !== false && report.source !== "processed",
    ...(report.source === "processed" ? { pdf_available: false } : {}),
    source: report.source === "processed" ? "processed" : "catalog",
    ...(report.processed_updated_at ? { processed_updated_at: text(report.processed_updated_at, 64) } : {}),
  };
}

export function validateContentManifest(value, reportId) {
  if (!value || value.schema_version !== 1 || value.report_id !== reportId || !REPORT_ID.test(reportId)
    || !Array.isArray(value.artifacts) || value.artifacts.length > 2000) failure(503, "service_unavailable");
  const ids = new Set();
  for (const row of value.artifacts) {
    const match = String(row?.object_key || "").match(new RegExp(`^${CONTENT_DATA_PREFIX}/blobs/${reportId}/([a-f0-9]{64})\\.(txt|md|json|pdf|jpg|png|webp)$`));
    if (!row || !HASH.test(row.id) || ids.has(row.id) || !HASH.test(row.sha256) || !match || match[1] !== row.sha256
      || !KINDS.has(row.kind) || !TYPES.has(row.mime_type) || !/^(?:und|[a-z]{2,3}(?:-[A-Za-z0-9]{2,8})?)$/.test(row.language)
      || !Number.isSafeInteger(row.size) || row.size < 1 || row.size > 64 * 1024 * 1024) failure(503, "service_unavailable");
    ids.add(row.id);
  }
  return value;
}

function publicArtifact(row, reportId) {
  return { id: row.id, report_id: reportId, kind: row.kind, language: row.language,
    mime_type: row.mime_type, size: row.size, filename: text(row.filename, 200), sha256: row.sha256,
    ...(row.text_scope ? { text_scope: text(row.text_scope, 40) } : {}),
    ...(row.page_number ? { page_number: row.page_number } : {}) };
}

function listPage(rows, query, filter) {
  const limit = Math.min(100, Math.max(1, Number(query.limit) || 25));
  let after = "";
  if (query.cursor) {
    try {
      const parsed = JSON.parse(atob(String(query.cursor).replaceAll("-", "+").replaceAll("_", "/")));
      if (parsed.filter !== filter || typeof parsed.after !== "string" || parsed.after.length > 250) throw new Error();
      after = parsed.after;
    } catch { failure(400, "invalid_request"); }
  }
  const sorted = rows.map((row) => ({ row, key: `${row.date || ""}|${row.id}` })).sort((a, b) => b.key.localeCompare(a.key));
  const available = sorted.filter(({ key }) => !after || key < after);
  const items = available.slice(0, limit);
  const next = available.length > limit ? btoa(JSON.stringify({ filter, after: items.at(-1).key })).replaceAll("+", "-").replaceAll("/", "_").replace(/=+$/, "") : "";
  return { items: items.map(({ row }) => row), next_cursor: next };
}

function dataResponse(body, type, filename, size, etag = "") {
  const headers = { "Content-Type": type, "Content-Length": String(size), "Cache-Control": "private, no-store",
    "X-Content-Type-Options": "nosniff", "Content-Disposition": `attachment; filename*=UTF-8''${encodeURIComponent(filename)}` };
  if (etag) headers.ETag = etag;
  return new Response(body, { headers });
}

function generatedArtifact(reportId, id, kind, language, body, mimeType, filename, extra = {}) {
  const bytes = new TextEncoder().encode(body);
  return { public: { id, report_id: reportId, kind, language, mime_type: mimeType, size: bytes.length, filename, ...extra }, bytes };
}

export function createCustomerContentData(deps) {
  async function catalog(env, context) {
    if (context.contentCatalog) return context.contentCatalog;
    const [base, processed] = await Promise.all([deps.loadCatalog(env), readJson(deps.bucket(env), `${CONTENT_DATA_PREFIX}/index.json`)]);
    if (processed && (processed.schema_version !== 1 || !Array.isArray(processed.items))) failure(503, "service_unavailable");
    const mapped = new Map((base.items || []).filter((row) => REPORT_ID.test(row?.id)).map((row) => [row.id, row]));
    for (const row of processed?.items || []) {
      if (!REPORT_ID.test(row?.id)) failure(503, "service_unavailable");
      const previous = mapped.get(row.id);
      mapped.set(row.id, previous ? { ...previous, processed_updated_at: row.processed_updated_at }
        : { ...row, source: "processed", available: false });
    }
    context.contentCatalog = [...mapped.values()];
    return context.contentCatalog;
  }

  async function allowed(env, rows, context) {
    const ids = context.grant.report_ids || [];
    rows = rows.filter((row) => !ids.length || ids.includes(row.id));
    return context.grant.access_mode === "granted_corpus" ? rows : deps.allowedReports(env, rows, context);
  }

  async function report(env, query, context) {
    if (!REPORT_ID.test(query.reportId || "")) failure(404, "content_not_found");
    const row = (await catalog(env, context)).find((item) => item.id === query.reportId);
    if (!row) failure(404, "content_not_found");
    if (!(await allowed(env, [row], context)).length) {
      if (context.grant.report_ids?.length && !context.grant.report_ids.includes(row.id)) failure(404, "content_not_found");
      if (context.grant.access_mode !== "membership" || !deps.canAccessReport
        || !await deps.canAccessReport(env, row, context)) failure(404, "content_not_found");
    }
    return row;
  }

  async function artifactRows(env, row, context, selection = {}) {
    const wantedId = selection.wantedId || "";
    const matches = (item) => (!wantedId || item.id === wantedId)
      && (!selection.kind || item.kind === selection.kind)
      && (!selection.language || item.language === selection.language);
    const metadata = () => generatedArtifact(row.id, "report-metadata", "metadata", "und",
      JSON.stringify(publicContentReport(row), null, 2), "application/json", `${row.id}.json`);
    // Catalog metadata has no dependency on processed files or chart/text indexes.
    if (wantedId === "report-metadata") return [metadata()];
    const result = [];
    const manifest = await readJson(deps.bucket(env), `${CONTENT_DATA_PREFIX}/reports/${row.id}/manifest.json`, 4 * 1024 * 1024);
    const stored = manifest ? validateContentManifest(manifest, row.id).artifacts : [];
    for (const artifact of stored) {
      const publicRow = publicArtifact(artifact, row.id);
      if (matches(publicRow)) result.push({ public: publicRow, stored: artifact });
    }
    // Published artifact IDs are hashes. Resolve their exact binding without
    // asking unrelated retrieval systems to be available for this download.
    if (wantedId && (result.length || HASH.test(wantedId))) return result;
    const includeGenerated = !selection.language || selection.language === "und";
    if (includeGenerated && !wantedId && (!selection.kind || selection.kind === "metadata")) result.push(metadata());
    const chartMatch = wantedId.match(/^chart-(?:meta-)?([a-f0-9]{64})$/);
    const needCharts = includeGenerated && (wantedId ? Boolean(chartMatch)
      : !selection.kind || selection.kind === "chart" || selection.kind === "metadata");
    if (needCharts) {
      const charts = (await deps.loadCharts(env)).items.filter((chart) => chart.report_id === row.id
        && (!chartMatch || chart.image_id === chartMatch[1]));
      for (const chart of charts) {
        if (!HASH.test(chart.image_id)) continue;
        const image = { id: `chart-${chart.image_id}`, report_id: row.id, kind: "chart", language: "und", mime_type: "image/jpeg", size: null, filename: `${chart.image_id}.jpg` };
        if (matches(image)) result.push({ public: image, chart: chart.image_id });
        const chartMetadata = generatedArtifact(row.id, `chart-meta-${chart.image_id}`, "metadata", "und",
          JSON.stringify(chart, null, 2), "application/json", `${chart.image_id}.json`);
        if (matches(chartMetadata.public)) result.push(chartMetadata);
      }
    }
    // The research corpus can contain excerpts. Do not label these as full text,
    // or make unrelated translations/images depend on this optional retrieval.
    const needText = includeGenerated && (wantedId ? wantedId === "extracted-text" : !selection.kind || selection.kind === "text");
    if (needText && !stored.some((item) => item.kind === "text") && row.source !== "processed") {
      const extracted = await deps.loadText(env, row);
      if (extracted?.text) result.push(generatedArtifact(row.id, "extracted-text", "text", "und", extracted.text,
        "text/plain", `${row.id}.txt`, { text_scope: extracted.text_scope || "partial_excerpt" }));
    }
    return result;
  }

  return {
    async listReports(env, query, context) {
      if (query.date && !contentDate(query.date)) failure(400, "invalid_request");
      const date = contentDate(query.date);
      const search = text(query.q, 200).trim().toLowerCase();
      const rows = (await allowed(env, await catalog(env, context), context)).map(publicContentReport).filter(Boolean)
        .filter((row) => (!date || row.date === date) && (!search || [row.title, row.title_zh, row.title_en, row.institution].join(" ").toLowerCase().includes(search)));
      return listPage(rows, query, `reports:${date}:${encodeURIComponent(search)}`);
    },
    async getReport(env, query, context) { return publicContentReport(await report(env, query, context)); },
    async listArtifacts(env, query, context) {
      const row = await report(env, query, context);
      const rows = (await artifactRows(env, row, context, query)).map((item) => item.public);
      return listPage(rows, query, `artifacts:${row.id}:${query.kind || ""}:${query.language || ""}`);
    },
    async downloadArtifact(env, query, context) {
      const row = await report(env, query, context);
      const entry = (await artifactRows(env, row, context, { wantedId: query.artifactId })).find((item) => item.public.id === query.artifactId);
      if (!entry) failure(404, "content_not_found");
      // Apply existing account download accounting to all derived report material.
      if (context.grant.access_mode === "membership") context.commitDownload = () => deps.commitDownload(env, row, context);
      if (entry.bytes) return dataResponse(entry.bytes, entry.public.mime_type, entry.public.filename, entry.bytes.length);
      const key = entry.stored?.object_key || `${deps.chartImagePrefix}/${entry.chart}.jpg`;
      const object = await deps.bucket(env).get(key);
      if (!object) failure(404, "content_not_found");
      if (!Number.isSafeInteger(object.size) || object.size < 1 || object.size > 64 * 1024 * 1024
        || entry.stored && object.size !== entry.stored.size) failure(503, "service_unavailable");
      return dataResponse(object.body, entry.public.mime_type, entry.public.filename, object.size, object.etag);
    },
    async downloadReport(env, query, context) {
      const row = await report(env, query, context);
      if (row.source === "processed") failure(404, "content_not_found");
      const descriptor = await deps.pdfDescriptor(env, row);
      if (!descriptor) failure(404, "content_not_found");
      const object = await deps.bucket(env).get(descriptor.object_key);
      if (!object) failure(404, "content_not_found");
      if (!Number.isSafeInteger(object.size) || object.size < 1) failure(503, "service_unavailable");
      if (context.grant.access_mode === "membership") context.commitDownload = () => deps.commitDownload(env, row, context);
      return dataResponse(object.body, "application/pdf", descriptor.filename || `${row.id}.pdf`, object.size, object.etag);
    },
  };
}
