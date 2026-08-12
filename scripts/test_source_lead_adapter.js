const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");

async function loadAdapter() {
  const sourcePath = path.join(__dirname, "..", "workers", "portal-suite-worker", "src", "source-lead-adapter.js");
  const source = fs.readFileSync(sourcePath, "utf8");
  return import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
}

class MockBucket {
  constructor() {
    this.rows = new Map();
  }

  async put(key, value, options) {
    this.rows.set(key, { value: String(value), options });
  }

  async get(key) {
    const row = this.rows.get(key);
    return row ? { text: async () => row.value } : null;
  }
}

function jsonResponse(payload) {
  return new Response(JSON.stringify(payload), {
    status: 200,
    headers: { "content-type": "application/json; charset=utf-8" },
  });
}

(async () => {
  const adapter = await loadAdapter();
  const bucket = new MockBucket();
  const env = {
    REPORT_BUCKET: bucket,
    SUPPLEMENTAL_SEARCH_URL: "https://search.example.invalid/api/find",
    SUPPLEMENTAL_SEARCH_HMAC_SECRET: "unit-test-secret-value",
    SUPPLEMENTAL_SEARCH_REDACT_TERMS: "PrivateSourceName",
  };

  let requestedUrl = "";
  const result = await adapter.searchSourceLeadMetadata({
    env,
    query: "mlcc",
    page: 2,
    now: "2026-08-09T00:00:00.000Z",
    fetchImpl: async (url) => {
      requestedUrl = url;
      return jsonResponse({
        total: 44,
        items: [{
          id: "https://search.example.invalid/reports/9812.html",
          title: "MLCC cycle update PrivateSourceName",
          published_at: "2026/08/08 09:20",
          publisher: "Example Research",
          pages: "31 pages",
          tags: ["MLCC", "components"],
          summary: "Contact analyst@example.invalid or visit https://search.example.invalid/about",
        }],
      });
    },
  });

  const upstream = new URL(requestedUrl);
  assert.equal(upstream.searchParams.get("q"), "mlcc");
  assert.equal(upstream.searchParams.get("kw"), "mlcc");
  assert.equal(upstream.searchParams.get("page"), "2");
  assert.equal(upstream.searchParams.get("p"), "1");
  assert.equal(result.total, 44);
  assert.equal(result.has_more, true);
  assert.equal(result.items.length, 1);
  assert.match(result.items[0].id, /^supplemental:[a-f0-9]{32}$/);
  assert.equal(result.items[0].source, "supplemental");
  assert.equal(result.items[0].page_count, 31);
  assert.equal(result.items[0].contact_only, true);
  assert.ok(!JSON.stringify(result).includes("search.example.invalid"));
  assert.ok(!JSON.stringify(result).includes("PrivateSourceName"));
  assert.ok(!JSON.stringify(result).includes("analyst@"));

  const key = adapter.sourceLeadStorageKey(result.items[0].id);
  const stored = await adapter.readStoredSourceLead(env, result.items[0].id);
  assert.ok(bucket.rows.has(key));
  assert.equal(stored.locator, "https://search.example.invalid/reports/9812.html");
  assert.equal(bucket.rows.get(key).options.httpMetadata.cacheControl, "private, no-store");
  const defensivePublicItem = adapter.publicSourceLeadItem({
    id: result.items[0].id,
    locator: "https://secret.example.invalid/item",
    metadata: {
      title: "Title https://secret.example.invalid/item",
      summary: "owner@example.invalid",
    },
  });
  assert.ok(!defensivePublicItem.title.includes("https://"));
  assert.ok(!defensivePublicItem.summary.includes("@"));

  const same = await adapter.searchSourceLeadMetadata({
    env,
    query: "other query",
    fetchImpl: async () => jsonResponse({
      items: [{ title: "Same report", url: "https://search.example.invalid/reports/9812.html" }],
    }),
  });
  assert.equal(same.items[0].id, result.items[0].id, "opaque IDs must be stable for one locator");

  const otherSecret = await adapter.searchSourceLeadMetadata({
    env: { ...env, SUPPLEMENTAL_SEARCH_HMAC_SECRET: "a-different-test-secret" },
    query: "other query",
    fetchImpl: async () => jsonResponse({
      items: [{ title: "Same report", url: "https://search.example.invalid/reports/9812.html" }],
    }),
  });
  assert.notEqual(otherSecret.items[0].id, result.items[0].id);

  let htmlRequestedUrl = "";
  const html = `<!doctype html>
    <p>Total: 21 reports</p>
    <article class="post excerpt">
      <header><h2><a href="/reports/2048.html">MLCC <em>pricing</em> tracker</a></h2></header>
      <time datetime="2026-08-07">August 7</time>
      <div class="meta"><span class="cat">\ue123Example Securities</span><span class="cat">18 pages</span></div>
      <div class="article-tags"><a>MLCC</a><a>pricing</a></div>
    </article>`;
  const htmlResult = await adapter.searchSourceLeadMetadata({
    env,
    query: "pricing",
    page: 1,
    fetchImpl: async (url) => {
      htmlRequestedUrl = url;
      return new Response(html, { status: 200, headers: { "content-type": "text/html" } });
    },
  });
  assert.equal(new URL(htmlRequestedUrl).searchParams.get("p"), "0");
  assert.equal(htmlResult.total, 21);
  assert.equal(htmlResult.items[0].title, "MLCC pricing tracker");
  assert.equal(htmlResult.items[0].date, "2026-08-07");
  assert.equal(htmlResult.items[0].institution, "Securities");
  assert.equal(htmlResult.items[0].page_count, 18);
  assert.deepEqual(htmlResult.items[0].tags, ["MLCC", "pricing"]);

  const fullHtmlPage = `<main>${Array.from({ length: 20 }, (_, index) => `
    <article class="excerpt"><header><h2><a href="/reports/${3000 + index}.html">Report ${index}</a></h2></header></article>
  `).join("")}</main>`;
  const fullHtmlResult = await adapter.searchSourceLeadMetadata({
    env,
    query: "report",
    page: 1,
    fetchImpl: async () => new Response(fullHtmlPage, { status: 200, headers: { "content-type": "text/html" } }),
  });
  assert.equal(fullHtmlResult.items.length, 20);
  assert.equal(fullHtmlResult.has_more, true, "a full HTML page must keep pagination available when total is absent");

  assert.equal(adapter.sourceLeadAdapterEnabled({}), false);
  await assert.rejects(
    adapter.searchSourceLeadMetadata({ env: {}, query: "mlcc" }),
    (error) => adapter.sanitizeSourceLeadError(error).code === "NOT_CONFIGURED",
  );
  const safe = adapter.sanitizeSourceLeadError(new Error("fetch https://secret.example.invalid failed"));
  assert.deepEqual(safe, {
    code: "UNAVAILABLE",
    message: "Supplemental search is temporarily unavailable.",
  });

  console.log("source lead adapter tests passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
