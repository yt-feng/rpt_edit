#!/usr/bin/env node

const assert = require("node:assert/strict");
const cryptoModule = require("node:crypto");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const workerPath = path.join(root, "workers", "portal-suite-worker", "src", "index.js");
const adapterPath = path.join(root, "workers", "portal-suite-worker", "src", "source-lead-adapter.js");
const appPath = path.join(root, "portal_suite", "site_src", "assets", "app.js");
const workerSource = fs.readFileSync(workerPath, "utf8");
const adapterSource = fs.readFileSync(adapterPath, "utf8");
const appSource = fs.readFileSync(appPath, "utf8");
const importPattern = /^import\s*\{[\s\S]*?\}\s*from\s*["']\.\/source-lead-adapter\.js["'];\s*/m;
assert.match(workerSource, importPattern, "Worker must statically import the supplemental adapter");

const runnableAdapter = adapterSource.replace(/\nexport\s*\{[\s\S]*?\};\s*$/m, "\n");
assert.notEqual(runnableAdapter, adapterSource, "adapter exports must be removed for the VM harness");
const runnableWorker = workerSource
  .replace(importPattern, "")
  .replace(/\bexport default\s*\{/, "globalThis.__workerExport = {");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.ok(start >= 0, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

const appSandbox = { URLSearchParams };
vm.createContext(appSandbox);
vm.runInContext(`
  const AUTHORITY_SOURCE = "authority";
  const REPORT_A_SOURCE = "report-a";
  const THINKTANK_SOURCE = "thinktank";
  const HOT_REPORT_SOURCE = "hot";
  const EXTERNAL_SOURCE = "external";
  ${extractFunction(appSource, "externalItemFromParams")}
  ${extractFunction(appSource, "isAuthorityItem")}
  ${extractFunction(appSource, "isReportAItem")}
  ${extractFunction(appSource, "isThinkTankItem")}
  ${extractFunction(appSource, "isHotReportItem")}
  ${extractFunction(appSource, "validDocId")}
  ${extractFunction(appSource, "authorityKindLabel")}
  const item = externalItemFromParams(new URLSearchParams("id=supplemental%3A0123456789abcdef0123456789abcdef"));
  globalThis.__appResult = {
    item,
    valid: validDocId(item),
    explicitLabel: authorityKindLabel("domestic-lead", "国内报告线索"),
    fallbackLabel: authorityKindLabel("domestic-lead"),
  };
`, appSandbox, { filename: appPath });
assert.equal(appSandbox.__appResult.item.source, "authority");
assert.equal(appSandbox.__appResult.valid, true);
assert.equal(appSandbox.__appResult.explicitLabel, "国内报告线索");
assert.equal(appSandbox.__appResult.fallbackLabel, "国内报告线索");
assert.match(appSource, /kind_label:\s*(?:item|remembered)\.kind_label\s*\|\|\s*""/);
assert.match(
  extractFunction(appSource, "fetchDocDetailItem"),
  /isContactOnlyItem\(merged\)[\s\S]*?endpoint = "contact-report\/item"/,
);
assert.match(
  extractFunction(appSource, "fetchDocDetailItem"),
  /isContactOnlyItem\(merged\)[\s\S]*?params\.set\("source", merged\.source\)/,
);

class MockBucket {
  constructor() {
    this.rows = new Map();
  }

  async put(key, value, options = {}) {
    this.rows.set(String(key), { value: String(value), options });
  }

  async get(key) {
    const row = this.rows.get(String(key));
    return row ? { text: async () => row.value } : null;
  }
}

let supplementalShouldFail = false;
const fetchMock = async (input, options = {}) => {
  const target = new URL(String(input));
  if (target.hostname === "search.example.invalid") {
    if (supplementalShouldFail) throw new Error("private endpoint details must not escape");
    return new Response(JSON.stringify({
      total: 1,
      items: [{
        url: "https://search.example.invalid/reports/9101.html",
        title: "Domestic MLCC channel inventory",
        date: "2026-08-08",
        institution: "Domestic Research",
        page_count: 18,
        tags: ["MLCC", "inventory"],
        summary: "Distributor inventory is normalizing.",
      }],
    }), { status: 200, headers: { "content-type": "application/json" } });
  }
  assert.equal(options.method, "POST");
  const kind = target.pathname.includes("foreign-rt") ? "foreign-rt" : "foreign";
  return new Response(JSON.stringify({
    code: 200,
    data: {
      pageNum: 1,
      total: 1,
      records: [{
        id: kind === "foreign-rt" ? 2002 : 1001,
        title: `${kind} MLCC outlook`,
        securities: "Example Securities",
        reDate: "2026-08-07",
        page: 12,
      }],
    },
  }), { status: 200, headers: { "content-type": "application/json" } });
};

const sandbox = {
  AbortController,
  ArrayBuffer,
  Blob,
  DOMException,
  FormData,
  Headers,
  Request,
  Response,
  TextDecoder,
  TextEncoder,
  URL,
  URLSearchParams,
  Uint8Array,
  atob,
  btoa,
  clearTimeout,
  console,
  crypto: cryptoModule.webcrypto,
  fetch: fetchMock,
  setTimeout,
};
vm.createContext(sandbox);
vm.runInContext(`${runnableAdapter}\n${runnableWorker}`, sandbox, { filename: workerPath });
const worker = sandbox.__workerExport;
assert.ok(worker && typeof worker.fetch === "function");

const bucket = new MockBucket();
const env = {
  ALLOWED_ORIGIN: "https://portal.example.invalid",
  AUTH_SECRET: "source-lead-integration-account-secret",
  REPORT_BUCKET: bucket,
  SUPPLEMENTAL_SEARCH_URL: "https://search.example.invalid/api/search",
  SUPPLEMENTAL_SEARCH_HMAC_SECRET: "integration-test-secret",
  SUPPLEMENTAL_SEARCH_REDACT_TERMS: "Private Source",
};
const ctx = { waitUntil() {} };

(async () => {
  const response = await worker.fetch(new Request(
    "https://portal.example.invalid/api/authority/search?q=mlcc&page=1&kind=both",
  ), env, ctx);
  assert.equal(response.status, 200);
  const payload = await response.json();
  assert.equal(payload.items.length, 3);
  const lead = payload.items.find((item) => item.kind === "domestic-lead");
  assert.ok(lead, "supplemental metadata must be merged into authority results");
  assert.match(lead.id, /^supplemental:[a-f0-9]{32}$/);
  assert.equal(lead.source, "authority");
  assert.equal(lead.kind_label, "国内报告线索");
  assert.equal(lead.contact_only, true);
  assert.match(String(lead.request_token || ""), /^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]{43}$/);
  assert.ok(!JSON.stringify(lead).includes("search.example.invalid"));
  assert.ok(!Object.prototype.hasOwnProperty.call(lead, "locator"));
  assert.deepEqual(
    payload.sources.map((source) => source.kind).sort(),
    ["domestic-lead", "foreign", "foreign-rt"],
  );
  assert.equal(
    [...bucket.rows.keys()].filter((key) => key.startsWith("_contact-reports/v1/targets/")).length,
    0,
    "authority search must not persist every signed target",
  );

  const privateRows = [...bucket.rows.entries()]
    .filter(([key]) => key.startsWith("_source-leads/items/"));
  assert.equal(privateRows.length, 1);
  assert.ok(privateRows[0][1].value.includes("https://search.example.invalid/reports/9101.html"));

  const itemResponse = await worker.fetch(new Request(
    `https://portal.example.invalid/api/authority/item?id=${encodeURIComponent(lead.id)}`,
  ), env, ctx);
  assert.equal(itemResponse.status, 200);
  const itemPayload = await itemResponse.json();
  assert.equal(itemPayload.item.id, lead.id);
  assert.equal(itemPayload.item.source, "authority");
  assert.equal(itemPayload.item.kind, "domestic-lead");
  assert.ok(!JSON.stringify(itemPayload).includes("search.example.invalid"));
  assert.ok(!Object.prototype.hasOwnProperty.call(itemPayload.item, "locator"));

  supplementalShouldFail = true;
  const degradedResponse = await worker.fetch(new Request(
    "https://portal.example.invalid/api/authority/search?q=capacitors&page=1&kind=both",
  ), env, ctx);
  assert.equal(degradedResponse.status, 200);
  const degraded = await degradedResponse.json();
  assert.equal(degraded.items.length, 2, "supplemental failure must not remove existing authority results");
  assert.ok(degraded.items.every((item) => ["foreign", "foreign-rt"].includes(item.kind)));
  assert.ok(!JSON.stringify(degraded).includes("private endpoint"));

  const pdfResponse = await worker.fetch(new Request(
    `https://portal.example.invalid/api/authority/pdf?id=${encodeURIComponent(lead.id)}`,
  ), env, ctx);
  assert.equal(pdfResponse.status, 403, "authority PDF access must remain contact-only");

  const foreignSearchItem = payload.items.find((item) => item.id === "foreign:1001");
  assert.ok(foreignSearchItem && foreignSearchItem.request_token);
  const targetRowsBeforeForeign = [...bucket.rows.keys()]
    .filter((key) => key.startsWith("_contact-reports/v1/targets/")).length;
  const foreignItem = await worker.fetch(new Request(
    `https://portal.example.invalid/api/authority/item?id=foreign%3A1001&request_token=${encodeURIComponent(foreignSearchItem.request_token)}`,
  ), env, ctx);
  assert.equal(foreignItem.status, 200, "a NashAI search proof must hydrate its child page");
  const foreignItemPayload = await foreignItem.json();
  assert.equal(foreignItemPayload.item.title, "foreign MLCC outlook");
  assert.equal(foreignItemPayload.item.institution, "Example Securities");
  assert.match(String(foreignItemPayload.item.request_token || ""), /^[A-Za-z0-9_-]+\.[A-Za-z0-9_-]{43}$/);
  assert.equal(
    [...bucket.rows.keys()].filter((key) => key.startsWith("_contact-reports/v1/targets/")).length,
    targetRowsBeforeForeign + 1,
    "opening one NashAI result persists one target",
  );

  const compactForeignItem = await worker.fetch(new Request(
    "https://portal.example.invalid/api/authority/item?id=foreign%3A1001",
  ), env, ctx);
  assert.equal(compactForeignItem.status, 200, "the compact id-only child URL works after the first hydrated fetch");
  assert.equal((await compactForeignItem.json()).item.title, "foreign MLCC outlook");

  console.log("Portal Suite source-lead integration checks passed.");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
