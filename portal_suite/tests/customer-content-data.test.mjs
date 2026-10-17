import assert from "node:assert/strict";
import test from "node:test";
import { createCustomerContentData, CONTENT_DATA_PREFIX as prefix, validateContentManifest } from "../../workers/portal-suite-worker/src/customer-content-data.js";

const reportId = "a".repeat(24), otherId = "b".repeat(24), sha = "c".repeat(64);
function fixture() {
  const rows = new Map(), reads = [];
  const bucket = { async get(key) {
    reads.push(key); const raw = rows.get(key); if (!raw) return null;
    const bytes = new TextEncoder().encode(raw);
    return { size: bytes.length, etag: "v1", text: async () => raw, body: new Response(bytes).body };
  } };
  let commit = 0;
  const deps = { bucket: () => bucket,
    loadCatalog: async () => ({ items: [{ id: reportId, title: "Energy outlook", date_folder: "261012", r2_key: "PRIVATE", password: "SECRET", available: true }] }),
    loadCharts: async () => ({ items: [{ report_id: reportId, image_id: sha, title: "Energy chart", date_folder: "261012" }] }),
    chartImagePrefix: "_chart-search/v1/images",
    allowedReports: async (_env, reports) => reports,
    loadText: async () => ({ text: "Known excerpt", text_scope: "partial_excerpt" }),
    pdfDescriptor: async () => ({ object_key: `reports/${reportId}.pdf`, filename: "report.pdf" }),
    commitDownload: async () => { commit++; },
  };
  const context = { user: { id: "user" }, grant: { report_ids: [], access_mode: "membership" } };
  return { rows, reads, context, deps, api: createCustomerContentData(deps), commits: () => commit };
}
function manifest(patch = {}) { return { schema_version: 1, report_id: reportId, artifacts: [{ id: "d".repeat(64),
  sha256: sha, kind: "translation", language: "zh", mime_type: "text/markdown", filename: "translated.md", size: 4,
  object_key: `${prefix}/blobs/${reportId}/${sha}.md`, ...patch }] }; }

test("catalog and report metadata never expose storage, password or provider locators", async () => {
  const { api, context } = fixture();
  const listed = await api.listReports({}, { limit: 10, date: "2026-10-12" }, context);
  assert.equal(listed.items[0].id, reportId);
  assert.doesNotMatch(JSON.stringify(listed), /PRIVATE|SECRET|r2_key|password/);
  assert.equal((await api.getReport({}, { reportId }, context)).title, "Energy outlook");
});

test("dedicated manifest bindings reject arbitrary account files and other report blobs", () => {
  assert.doesNotThrow(() => validateContentManifest(manifest(), reportId));
  for (const object_key of ["_account/users.json", `${prefix}/blobs/${otherId}/${sha}.md`, `${prefix}/blobs/${reportId}/../secret.md`])
    assert.throws(() => validateContentManifest(manifest({ object_key }), reportId));
});

test("artifacts enumerate stored translation, extracted excerpt and linked chart with safe public descriptors", async () => {
  const { api, context, rows } = fixture();
  rows.set(`${prefix}/reports/${reportId}/manifest.json`, JSON.stringify(manifest()));
  const result = await api.listArtifacts({}, { reportId, limit: 100 }, context);
  assert.equal(result.items.length, 5);
  assert.equal(result.items.find(row => row.id === "extracted-text").text_scope, "partial_excerpt");
  assert.equal(result.items.find(row => row.kind === "chart").size, null);
  assert.doesNotMatch(JSON.stringify(result), /object_key|_customer-content-data|_chart-search/);
  assert.equal((await api.listArtifacts({}, { reportId, limit: 10, kind: "translation", language: "zh" }, context)).items.length, 1);
});

test("artifact binary is report-bound and the caller commits download only after API accounting", async () => {
  const state = fixture();
  state.rows.set(`${prefix}/reports/${reportId}/manifest.json`, JSON.stringify(manifest()));
  state.rows.set(`${prefix}/blobs/${reportId}/${sha}.md`, "TEXT");
  const response = await state.api.downloadArtifact({}, { reportId, artifactId: "d".repeat(64) }, state.context);
  assert.equal(response.headers.get("content-length"), "4");
  assert.equal(await response.text(), "TEXT");
  assert.equal(state.commits(), 0);
  await state.context.commitDownload(); assert.equal(state.commits(), 1);
  await assert.rejects(state.api.downloadArtifact({}, { reportId, artifactId: "_account" }, state.context));
  assert.equal(state.reads.some(key => key.startsWith("_account")), false);
});

test("exact purchased reports use one per-report fallback but restricted API grants still deny", async () => {
  const state = fixture(); state.deps.allowedReports = async () => [];
  let lookups = 0; state.deps.canAccessReport = async () => { lookups++; return true; };
  const api = createCustomerContentData(state.deps);
  assert.equal((await api.listReports({}, { limit: 10 }, state.context)).items.length, 0);
  assert.equal(lookups, 0);
  assert.equal((await api.getReport({}, { reportId }, state.context)).id, reportId);
  assert.equal(lookups, 1);
  state.context.grant.report_ids = [otherId];
  await assert.rejects(api.getReport({}, { reportId }, state.context));
  assert.equal(lookups, 1);
});

test("processed-only reports are discoverable but cannot claim an original PDF", async () => {
  const state = fixture();
  state.rows.set(`${prefix}/index.json`, JSON.stringify({ schema_version: 1, items: [{ id: otherId, title: "New parsed report", date_folder: "261012" }] }));
  const rows = (await state.api.listReports({}, { limit: 10 }, state.context)).items;
  assert.equal(rows.find(row => row.id === otherId).pdf_available, false);
  await assert.rejects(state.api.downloadReport({}, { reportId: otherId }, state.context));
});

test("cursor carries filters and remains bounded across pages", async () => {
  const state = fixture();
  state.rows.set(`${prefix}/index.json`, JSON.stringify({ schema_version: 1, items: [{ id: otherId, title: "Other", date_folder: "261011" }] }));
  const first = await state.api.listReports({}, { limit: 1 }, state.context);
  const second = await state.api.listReports({}, { limit: 1, cursor: first.next_cursor }, state.context);
  assert.equal(first.items[0].id, reportId); assert.equal(second.items[0].id, otherId);
  await assert.rejects(state.api.listReports({}, { limit: 1, cursor: first.next_cursor, date: "2026-10-12" }, state.context));
});

test("report search matches normalized public titles and institutions within the authorized corpus", async () => {
  const state = fixture(), hiddenId = "e".repeat(24);
  state.deps.loadCatalog = async () => ({ items: [
    { id: reportId, title: "Ｅｎｅｒｇｙ　 Outlook", title_zh: "全球能源展望", title_en: "Energy outlook", bank_name: "示例研究院", date_folder: "261012" },
    { id: otherId, title: "Market strategy", title_en: "Allocation review", institution: "Example Research", date_folder: "261011" },
    { id: hiddenId, title: "Hidden energy outlook", institution: "Hidden Research", private_path: "private-energy-data", date_folder: "261013" },
  ] });
  state.context.grant = { access_mode: "granted_corpus", report_ids: [reportId, otherId] };
  const api = createCustomerContentData(state.deps);
  for (const q of ["  ENERGY  OUTLOOK  ", "全球能源", "示例研究院"]) {
    assert.deepEqual((await api.listReports({}, { q, limit: 10 }, state.context)).items.map(row => row.id), [reportId]);
  }
  for (const q of ["allocation", "EXAMPLE RESEARCH"]) {
    assert.deepEqual((await api.listReports({}, { q, limit: 10 }, state.context)).items.map(row => row.id), [otherId]);
  }
  for (const q of ["hidden", "private-energy-data", "not found"]) {
    assert.deepEqual(await api.listReports({}, { q, limit: 10 }, state.context), { items: [], next_cursor: "" });
  }
  assert.equal((await api.listReports({}, { q: "energy", date: "2026-10-11", limit: 10 }, state.context)).items.length, 0);
  assert.equal((await api.listReports({}, { q: "　 ", limit: 10 }, state.context)).items.length, 2);
  await assert.rejects(api.listReports({}, { q: "x".repeat(201), limit: 10 }, state.context), { code: "invalid_request" });
});

test("search cursors stay bounded and bind query, date, account and API authorization", async () => {
  const state = fixture(), query = "研".repeat(200);
  state.deps.loadCatalog = async () => ({ items: [
    { id: reportId, title: `${query}一`, date_folder: "261012" },
    { id: otherId, title: `${query}二`, date_folder: "261011" },
  ] });
  state.context.grant = { access_mode: "granted_corpus", report_ids: [], scopes: ["reports:read"] };
  const api = createCustomerContentData(state.deps);
  const first = await api.listReports({}, { q: query, limit: 1 }, state.context);
  assert.ok(first.next_cursor.length > 0 && first.next_cursor.length <= 512);
  const next = { q: `　${query} `, cursor: first.next_cursor, limit: 1 };
  assert.deepEqual((await api.listReports({}, next, state.context)).items.map(row => row.id), [otherId]);
  for (const changed of [{ q: "研" }, { q: "" }, { date: "2026-10-12" }]) {
    await assert.rejects(api.listReports({}, { ...next, ...changed }, state.context), { code: "invalid_request" });
  }
  for (const changed of [
    { user: { id: "another-account" } },
    { grant: { ...state.context.grant, report_ids: [otherId] } },
    { grant: { ...state.context.grant, scopes: ["reports:read", "artifacts:read"] } },
    { grant: { ...state.context.grant, access_mode: "membership" } },
  ]) {
    await assert.rejects(api.listReports({}, next, { ...state.context, ...changed }), { code: "invalid_request" });
  }
});

test("each search page reapplies current membership without hashing the catalog into the cursor", async () => {
  const state = fixture();
  state.deps.loadCatalog = async () => ({ items: [
    { id: reportId, title: "Energy one", date_folder: "261012" },
    { id: otherId, title: "Energy two", date_folder: "261011" },
  ] });
  let visible = new Set([reportId, otherId]);
  state.deps.allowedReports = async (_env, reports) => reports.filter(row => visible.has(row.id));
  const api = createCustomerContentData(state.deps);
  const first = await api.listReports({}, { q: "Energy", limit: 1 }, state.context);
  visible = new Set([reportId]);
  const second = await api.listReports({}, { q: "ｅｎｅｒｇｙ", limit: 1, cursor: first.next_cursor }, state.context);
  assert.deepEqual(second.items, []);
});

test("published translation download and filtered listing do not depend on chart or fallback-text availability", async () => {
  const state = fixture();
  state.rows.set(`${prefix}/reports/${reportId}/manifest.json`, JSON.stringify(manifest()));
  state.rows.set(`${prefix}/blobs/${reportId}/${sha}.md`, "TEXT");
  let chartReads = 0, textReads = 0;
  state.deps.loadCharts = async () => { chartReads++; throw new Error("Synthetic chart outage"); };
  state.deps.loadText = async () => { textReads++; throw new Error("Synthetic text outage"); };
  const api = createCustomerContentData(state.deps);
  const response = await api.downloadArtifact({}, { reportId, artifactId: "d".repeat(64) }, state.context);
  assert.equal(await response.text(), "TEXT");
  const listed = await api.listArtifacts({}, { reportId, limit: 10, kind: "translation", language: "zh" }, state.context);
  assert.equal(listed.items.length, 1); assert.equal(listed.items[0].id, "d".repeat(64));
  const byLanguage = await api.listArtifacts({}, { reportId, limit: 10, language: "zh" }, state.context);
  assert.equal(byLanguage.items.length, 1);
  assert.equal(chartReads, 0); assert.equal(textReads, 0);
});

test("generated report metadata downloads without reading optional content manifests or indexes", async () => {
  const state = fixture();
  state.deps.loadCharts = async () => { throw new Error("Chart index must not be read"); };
  state.deps.loadText = async () => { throw new Error("Text index must not be read"); };
  state.rows.set(`${prefix}/reports/${reportId}/manifest.json`, "invalid optional manifest");
  const api = createCustomerContentData(state.deps);
  const response = await api.downloadArtifact({}, { reportId, artifactId: "report-metadata" }, state.context);
  assert.equal((await response.json()).id, reportId);
  assert.equal(state.reads.includes(`${prefix}/reports/${reportId}/manifest.json`), false);
});

test("metadata listing retains chart metadata and skips unrelated fallback text", async () => {
  const state = fixture();
  state.deps.loadText = async () => { throw new Error("Text index must not be read for metadata"); };
  const api = createCustomerContentData(state.deps);
  const listed = await api.listArtifacts({}, { reportId, limit: 10, kind: "metadata" }, state.context);
  assert.deepEqual(new Set(listed.items.map(row => row.id)), new Set(["report-metadata", `chart-meta-${sha}`]));
  assert.ok(listed.items.every(row => row.kind === "metadata"));
});

test("requested chart and fallback-text failures still propagate instead of silently returning missing content", async () => {
  const state = fixture();
  state.deps.loadCharts = async () => { throw new Error("Synthetic chart outage"); };
  state.deps.loadText = async () => { throw new Error("Synthetic text outage"); };
  const api = createCustomerContentData(state.deps);
  await assert.rejects(api.downloadArtifact({}, { reportId, artifactId: `chart-${sha}` }, state.context), /Synthetic chart outage/u);
  await assert.rejects(api.downloadArtifact({}, { reportId, artifactId: "extracted-text" }, state.context), /Synthetic text outage/u);
  await assert.rejects(api.listArtifacts({}, { reportId, limit: 10, kind: "metadata" }, state.context), /Synthetic chart outage/u);
  await assert.rejects(api.listArtifacts({}, { reportId, limit: 10, kind: "text" }, state.context), /Synthetic text outage/u);
});
