const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");
const webcrypto = require("node:crypto").webcrypto;

const root = path.resolve(__dirname, "..");
const modulePath = path.join(root, "workers/portal-suite-worker/src/locale-report-detail.js");
const source = fs.readFileSync(modulePath, "utf8");
globalThis.crypto = webcrypto;

class Bucket {
  constructor() { this.rows = new Map(); this.serial = 0; this.gets = 0; this.puts = 0; }
  async get(key) {
    this.gets += 1;
    if (this.failGet?.(key)) throw new Error("secret storage exception");
    const row = this.rows.get(key);
    if (!row) return null;
    return { etag: row.etag, size: Buffer.byteLength(row.text), body: new Response(row.text).body };
  }
  async put(key, text, options) {
    this.puts += 1;
    assert.equal(options.httpMetadata.cacheControl, "private, no-store");
    if (this.failPut?.(key)) throw new Error("secret storage write exception");
    if (this.conflict?.(key)) return null;
    const existing = this.rows.get(key);
    const condition = options.onlyIf;
    assert.ok(condition, "all writes must use durable compare-and-swap");
    if (condition.etagMatches && existing?.etag !== condition.etagMatches) return null;
    if (condition.etagDoesNotMatch === "*" && existing) return null;
    const etag = `etag-${++this.serial}`;
    this.rows.set(key, { etag, text });
    return { etag };
  }
  matching(part) { return [...this.rows.entries()].filter(([key]) => key.includes(part)); }
}

async function main() {
  const api = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
  const handle = api.handleLocaleReportDetail;
  let passed = 0;
  const test = async (name, body) => { await body(); passed += 1; process.stdout.write(`ok ${passed} - ${name}\n`); };
  const input = { source: "catalog", id: "a".repeat(24), locale: "ja" };
  const request = (body = input, method = "POST") => method === "GET"
    ? new Request(`https://portal.example.invalid/api/locale/report-detail?${new URLSearchParams(body)}`)
    : new Request("https://portal.example.invalid/api/locale/report-detail", { method, headers: { "Content-Type": "application/json" }, body: JSON.stringify(body) });
  function harness(extra = {}) {
    const bucket = new Bucket();
    const tasks = [];
    const counts = { resolve: 0, translate: 0 };
    const clock = { value: Date.parse("2026-09-06T01:00:00Z") };
    const env = { REPORT_BUCKET: bucket, LOCALE_DETAIL_TRANSLATION_ENABLED: "true", DEEPSEEK_API_KEY: "test-placeholder-only", ...extra };
    const deps = {
      validId: (sourceName, id) => sourceName === "catalog" && /^[a-f0-9]{24}$/.test(id),
      now: () => clock.value,
      resolve: async () => { counts.resolve += 1; return { title: "中文报告", institution: "公开机构", summary: "公开摘要", filename: "原始文件名.pdf", pdf_url: "PRIVATE", password: "PRIVATE", text: "MEMBER BODY" }; },
      translate: async (_env, messages, options) => {
        counts.translate += 1;
        assert.equal(options.timeout, 18000);
        assert.equal(options.maxResponseBytes, 65536);
        assert.ok(options.maxTokens <= 6000);
        const payload = JSON.parse(messages[1].content);
        assert.ok(["ko", "ja", "ar"].includes(payload.locale));
        assert.match(payload.target_language, /Korean|Japanese|Arabic/);
        const fields = payload.fields;
        assert.deepEqual(Object.keys(fields), ["title", "institution", "summary"]);
        assert.doesNotMatch(messages[1].content, /PRIVATE|MEMBER|password|pdf_url|filename|原始文件名/);
        return Object.fromEntries(Object.keys(fields).map((key) => [key, `日本語の${key}`]));
      },
    };
    return { bucket, tasks, counts, clock, env, deps, ctx: { waitUntil: (task) => tasks.push(task) }, async drain() { await Promise.all(tasks.splice(0)); } };
  }

  await test("disabled and Chinese requests never resolve, read storage or translate", async () => {
    const h = harness({ LOCALE_DETAIL_TRANSLATION_ENABLED: "false" });
    assert.equal((await (await handle(request(), h.env, h.ctx, h.deps)).json()).code, "disabled");
    h.env.LOCALE_DETAIL_TRANSLATION_ENABLED = "true";
    for (const locale of ["zh", "zh-CN", "en", ["ja"], "__proto__"]) {
      assert.equal((await handle(request({ ...input, locale }), h.env, h.ctx, h.deps)).status, 400);
    }
    assert.deepEqual(h.counts, { resolve: 0, translate: 0 });
    assert.equal(h.bucket.gets + h.bucket.puts, 0);
  });

  await test("rejects arbitrary text, URLs, credentials, duplicate query and oversized body", async () => {
    const h = harness();
    for (const body of [{ ...input, text: "translate me" }, { ...input, rt: "token" }, { ...input, password: "private" }, { ...input, id: "https://portal.example.invalid/report" }, { ...input, source: "pdf" }, { ...input, id: "x".repeat(2000) }]) {
      assert.equal((await handle(request(body), h.env, h.ctx, h.deps)).status, 400);
    }
    assert.equal((await handle(new Request(`${request(input, "GET").url}&locale=ar`), h.env, h.ctx, h.deps)).status, 400);
    assert.equal(h.counts.resolve + h.bucket.gets, 0);
  });

  await test("one POST becomes pending then ready; polling and subsequent POST are free", async () => {
    const h = harness();
    assert.equal((await handle(request(input, "GET"), h.env, h.ctx, h.deps)).status, 404);
    assert.equal(h.counts.translate, 0);
    assert.equal(h.bucket.puts, 0);
    assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 202);
    await h.drain();
    for (const method of ["GET", "POST"]) {
      const result = await handle(request(input, method), h.env, h.ctx, h.deps);
      assert.equal(result.status, 200);
      const body = await result.json();
      assert.equal(body.status, "ready");
      assert.equal(body.cached, true);
      assert.match(body.source_hash, /^[a-f0-9]{64}$/);
      assert.deepEqual(Object.keys(body.fields).sort(), [...api.LOCALE_DETAIL_FIELDS].sort());
      assert.equal(body.fields.title_cn, body.fields.title);
      assert.equal(body.fields.title_zh, body.fields.title);
      assert.equal(body.fields.description, "");
      assert.equal(body.fields.filename, "", "operational filename never enters translation output");
      assert.doesNotMatch(JSON.stringify(body), /中文|公开|PRIVATE|MEMBER|test-placeholder/);
    }
    assert.equal(h.counts.translate, 1);
    const budget = JSON.parse(h.bucket.matching("/budget/")[0][1].text);
    assert.equal(budget.count, 1);
    assert.ok(budget.chars > 0);
  });

  await test("parallel duplicates share one durable lease and provider call", async () => {
    const h = harness();
    let release;
    h.deps.translate = async () => { h.counts.translate += 1; return new Promise((resolve) => { release = resolve; }); };
    const results = await Promise.all(Array.from({ length: 12 }, () => handle(request(), h.env, h.ctx, h.deps)));
    assert.ok(results.every((result) => result.status === 202));
    assert.equal(h.counts.translate, 1);
    release({ title: "日本語", institution: "機関", summary: "概要" });
    await h.drain();
    assert.equal(JSON.parse(h.bucket.matching("/budget/")[0][1].text).count, 1);
  });

  await test("R2 cache read errors and malformed cache never count as a miss", async () => {
    for (const malformed of [false, true]) {
      const h = harness();
      if (malformed) {
        await handle(request(), h.env, h.ctx, h.deps); await h.drain();
        const [key, row] = h.bucket.matching("/cache/")[0];
        h.bucket.rows.set(key, { ...row, text: "null" });
        h.counts.translate = 0;
      } else h.bucket.failGet = () => true;
      const result = await handle(request(), h.env, h.ctx, h.deps);
      assert.equal(result.status, 503);
      assert.equal(h.counts.translate, 0);
      assert.doesNotMatch(await result.text(), /secret|exception/);
    }
  });

  await test("budget read/write errors never call provider", async () => {
    for (const operation of ["failGet", "failPut"]) {
      const h = harness(); h.bucket[operation] = (key) => key.includes("/budget/");
      assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 503);
      assert.equal(h.counts.translate, 0);
      assert.equal(h.tasks.length, 0);
    }
  });

  await test("unconfigured provider sentinel never reserves quota or calls provider", async () => {
    const h = harness({ DEEPSEEK_API_KEY: " unconfigured " });
    const result = await handle(request(), h.env, h.ctx, h.deps);
    assert.equal((await result.json()).code, "provider_unavailable");
    assert.equal(h.bucket.puts + h.counts.translate, 0);
    assert.equal(h.tasks.length, 0);
  });

  await test("durable count quota caps concurrent distinct reports across contexts", async () => {
    const h = harness({ LOCALE_DETAIL_DAILY_MAX_REQUESTS: "1" });
    const results = await Promise.all(["a", "b"].map((letter) => handle(request({ ...input, id: letter.repeat(24) }), h.env, h.ctx, h.deps)));
    assert.deepEqual(results.map((value) => value.status).sort(), [202, 429]);
    await h.drain();
    assert.equal(h.counts.translate, 1);
    assert.equal(JSON.parse(h.bucket.matching("/budget/")[0][1].text).count, 1);
    const newContext = { waitUntil: (task) => h.tasks.push(task) };
    assert.equal((await handle(request({ ...input, id: "c".repeat(24) }), h.env, newContext, h.deps)).status, 429);
    assert.equal(h.counts.translate, 1);
  });

  await test("character quota, zero quota and malformed budget fail closed", async () => {
    for (const settings of [{ LOCALE_DETAIL_DAILY_MAX_CHARS: "1" }, { LOCALE_DETAIL_DAILY_MAX_REQUESTS: "0" }, { LOCALE_DETAIL_DAILY_MAX_REQUESTS: "bad" }]) {
      const h = harness(settings);
      assert.ok([429, 503].includes((await handle(request(), h.env, h.ctx, h.deps)).status));
      assert.equal(h.counts.translate, 0);
    }
    const h = harness();
    h.bucket.rows.set("_locale/report-detail/v1/budget/2026-09-06.json", { etag: "bad", text: JSON.stringify({ version: "public-detail-v1", day: "2026-09-06", count: -1, chars: 0 }) });
    assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 503);
    assert.equal(h.counts.translate, 0);
  });

  await test("UTC daily budgets roll over without discarding paid cached results", async () => {
    const h = harness({ LOCALE_DETAIL_DAILY_MAX_REQUESTS: "1" });
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    h.clock.value += 86400000;
    assert.equal((await handle(request({ ...input, id: "b".repeat(24) }), h.env, h.ctx, h.deps)).status, 202);
    await h.drain();
    delete h.env.DEEPSEEK_API_KEY;
    assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 200);
    assert.equal(h.counts.translate, 2);
    assert.equal(h.bucket.matching("/budget/").length, 2);
    assert.ok(h.bucket.matching("/budget/").every(([, row]) => JSON.parse(row.text).count === 1));
  });

  await test("provider failure is cached, redacted, TTL limited, and retains quota debit", async () => {
    const h = harness();
    h.deps.translate = async () => { h.counts.translate += 1; throw new Error("secret provider key"); };
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    for (const method of ["POST", "GET"]) {
      const result = await handle(request(input, method), h.env, h.ctx, h.deps);
      assert.equal(result.status, 503);
      assert.doesNotMatch(await result.text(), /secret|provider key/);
    }
    assert.equal(h.counts.translate, 1);
    h.clock.value += 600001;
    assert.equal((await handle(request(input, "GET"), h.env, h.ctx, h.deps)).status, 404);
    assert.equal(h.counts.translate, 1);
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    assert.equal(h.counts.translate, 2);
    assert.equal(JSON.parse(h.bucket.matching("/budget/")[0][1].text).count, 2);
  });

  await test("missing output fields, excess keys, HTML and oversized output never become ready", async () => {
    for (const result of [null, { title: "日本語" }, { title: "日本語", institution: "機関", summary: "概要", pdf_url: "BAD" }, { title: "<script>bad</script>", institution: "機関", summary: "概要" }, { title: "x".repeat(2000), institution: "機関", summary: "概要" }]) {
      const h = harness(); h.deps.translate = async () => result;
      await handle(request(), h.env, h.ctx, h.deps); await h.drain();
      assert.equal((await handle(request(input, "GET"), h.env, h.ctx, h.deps)).status, 503);
      assert.equal(JSON.parse(h.bucket.matching("/budget/")[0][1].text).count, 1);
    }
  });

  await test("real Japanese canary rejects Chinese prose once, with no paid retry", async () => {
    const h = harness();
    const canary = { source: "external", id: "1289771588484468736", locale: "ja" };
    h.deps.validId = (sourceName, id) => sourceName === "external" && id === canary.id;
    h.deps.resolve = async () => ({ title: "Initiating at Buy: Capturing AI server and CPO growth through optical semiconductor photodiodes-20260825" });
    h.deps.translate = async (_env, messages) => {
      h.counts.translate += 1;
      assert.match(messages[0].content, /必ず自然な日本語/);
      assert.match(messages[0].content, /中国語で回答したり/);
      assert.equal(JSON.parse(messages[1].content).target_language, "Japanese (日本語)");
      assert.equal(JSON.parse(messages[1].content).locale, "ja");
      return { title: "买入评级启动：通过光半导体光电二极管把握AI服务器与CPO增长机遇-20260825" };
    };
    assert.equal((await handle(request(canary), h.env, h.ctx, h.deps)).status, 202);
    await h.drain();
    for (const method of ["GET", "POST", "GET"]) {
      const result = await handle(request(canary, method), h.env, h.ctx, h.deps);
      assert.equal(result.status, 503);
      const body = await result.json();
      assert.equal(body.status, "failed");
      assert.equal(body.code, "translation_unavailable");
      assert.equal(body.retry_after, 600);
      assert.equal(body.fields, undefined);
    }
    assert.equal(h.counts.translate, 1);
    assert.equal(JSON.parse(h.bucket.matching("/budget/")[0][1].text).count, 1);
  });

  await test("all-kanji Japanese titles and official English institution names remain valid", async () => {
    for (const title of ["中国経済展望", "半導体産業動向", "世界経済及国際金融市場長期展望調査報告", "買い推奨で調査開始：光半導体フォトダイオードを通じてAIサーバーとCPOの成長機会を捉える-20260825"]) {
      const h = harness();
      h.deps.translate = async () => ({ title, institution: "Morgan Stanley Research", summary: "世界経済展望" });
      await handle(request(), h.env, h.ctx, h.deps); await h.drain();
      const result = await handle(request(input, "GET"), h.env, h.ctx, h.deps);
      assert.equal(result.status, 200);
      const body = await result.json();
      assert.equal(body.fields.title, title);
      assert.equal(body.fields.institution, "Morgan Stanley Research");
    }
  });

  await test("native Korean and Arabic prompts retain their own display prose", async () => {
    for (const [locale, title, expectedPrompt] of [["ko", "AI 서버와 CPO의 성장 기회를 활용하는 광반도체 기업", /반드시 자연스러운 한국어/], ["ar", "اغتنام فرص نمو خوادم الذكاء الاصطناعي والتقنيات الضوئية", /إلى عربية طبيعية/]]) {
      const h = harness();
      h.deps.translate = async (_env, messages) => {
        assert.match(messages[0].content, expectedPrompt);
        return { title, institution: "Morgan Stanley", summary: title };
      };
      const target = { ...input, locale };
      await handle(request(target), h.env, h.ctx, h.deps); await h.drain();
      assert.equal((await handle(request(target, "GET"), h.env, h.ctx, h.deps)).status, 200);
    }
  });

  await test("prompt version bypasses old bad cache while preserving v1 daily ledger and old objects", async () => {
    const h = harness({ LOCALE_DETAIL_DAILY_MAX_REQUESTS: "2" });
    const hash = (value) => require("node:crypto").createHash("sha256").update(JSON.stringify(value)).digest("hex");
    const sourceHash = hash({ title: "中文报告", institution: "公开机构", summary: "公开摘要" });
    const oldIdentity = hash({ ...input, model: "deepseek-v4-flash", version: "public-detail-v1", source_hash: sourceHash });
    const oldKey = `_locale/report-detail/v1/cache/${oldIdentity}.json`;
    const oldFields = Object.fromEntries(api.LOCALE_DETAIL_FIELDS.map((key) => [key, ""]));
    for (const key of ["title", "title_cn", "title_zh", "display_title"]) oldFields[key] = "买入评级启动：通过光半导体把握AI服务器增长机遇";
    const oldRow = { etag: "old-paid-cache", text: JSON.stringify({ version: "public-detail-v1", identity: oldIdentity, status: "ready", fields: oldFields }) };
    h.bucket.rows.set(oldKey, oldRow);
    const budgetKey = "_locale/report-detail/v1/budget/2026-09-06.json";
    h.bucket.rows.set(budgetKey, { etag: "existing-budget", text: JSON.stringify({ version: "public-detail-v1", day: "2026-09-06", count: 1, chars: 100 }) });
    assert.equal((await handle(request(input, "GET"), h.env, h.ctx, h.deps)).status, 404);
    assert.equal(h.counts.translate, 0);
    assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 202);
    await h.drain();
    const ready = await handle(request(), h.env, h.ctx, h.deps);
    assert.equal(ready.status, 200);
    assert.equal(h.counts.translate, 1);
    assert.equal(h.bucket.rows.get(oldKey), oldRow, "prior paid cache is preserved verbatim");
    const budget = JSON.parse(h.bucket.rows.get(budgetKey).text);
    assert.equal(budget.version, "public-detail-v1");
    assert.equal(budget.count, 2);
    assert.equal(h.bucket.matching("/budget/").length, 1);
    assert.equal(h.bucket.matching("/cache/").length, 2);
    assert.equal((await handle(request({ ...input, id: "b".repeat(24) }), h.env, h.ctx, h.deps)).status, 429);
    assert.equal(h.counts.translate, 1);
  });

  await test("source, locale and model version changes have separate cache identities", async () => {
    const h = harness();
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    h.env.DEEPSEEK_MODEL = "test-model-v2";
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    await handle(request({ ...input, locale: "ko" }), h.env, h.ctx, h.deps); await h.drain();
    await handle(request({ ...input, locale: "ar" }), h.env, h.ctx, h.deps); await h.drain();
    h.deps.resolve = async () => ({ title: "新版报告", institution: "机构", summary: "摘要" });
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    assert.equal(h.counts.translate, 5);
    assert.equal(h.bucket.matching("/cache/").length, 5);
  });

  await test("source failures, missing records and oversized source do not spend quota", async () => {
    for (const resolver of [async () => { throw new Error("private source"); }, async () => null, async () => ({ title: "x".repeat(641) })]) {
      const h = harness(); h.deps.resolve = resolver;
      assert.ok([404, 503].includes((await handle(request(), h.env, h.ctx, h.deps)).status));
      assert.equal(h.counts.translate + h.bucket.puts, 0);
    }
  });

  await test("expired workers cannot overwrite newer lease and missing cache writes are not success", async () => {
    const h = harness();
    let finishProvider;
    h.deps.translate = async () => new Promise((resolve) => { finishProvider = resolve; });
    await handle(request(), h.env, h.ctx, h.deps);
    const [key, stored] = h.bucket.matching("/cache/")[0];
    const row = JSON.parse(stored.text); row.token = "new-worker";
    h.bucket.rows.set(key, { etag: "new-etag", text: JSON.stringify(row) });
    finishProvider({ title: "日本語", institution: "機関", summary: "概要" }); await h.drain();
    assert.equal(JSON.parse(h.bucket.rows.get(key).text).token, "new-worker");
    assert.equal(JSON.parse(h.bucket.rows.get(key).text).status, "pending");
  });

  await test("failed result persistence stays pending, never returns uncached success", async () => {
    const h = harness();
    h.deps.translate = async () => {
      h.counts.translate += 1;
      h.bucket.failPut = (key) => key.includes("/cache/");
      return { title: "日本語", institution: "機関", summary: "概要" };
    };
    await handle(request(), h.env, h.ctx, h.deps); await h.drain();
    assert.equal((await handle(request(input, "GET"), h.env, h.ctx, h.deps)).status, 202);
    assert.equal((await handle(request(), h.env, h.ctx, h.deps)).status, 202);
    assert.equal(h.counts.translate, 1);
  });

  await test("provider stream is bounded and its timeout covers body reading", async () => {
    const previousFetch = globalThis.fetch;
    try {
      globalThis.fetch = async () => new Response("x".repeat(100));
      await assert.rejects(api.localeDetailProviderPayload("https://provider.example.invalid", {}, { timeout: 100, maxResponseBytes: 10 }), /body_limit/);
      globalThis.fetch = async (_url, init) => new Response(new ReadableStream({ start(controller) {
        init.signal.addEventListener("abort", () => controller.error(new Error("mock timeout")));
      } }));
      await assert.rejects(api.localeDetailProviderPayload("https://provider.example.invalid", {}, { timeout: 5, maxResponseBytes: 10 }), /mock timeout/);
    } finally { globalThis.fetch = previousFetch; }
  });

  await test("actual Worker route loads module only for opt-in endpoint; health advertises disabled state", async () => {
    let importCalls = 0;
    const workerSource = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
    assert.match(workerSource, /if \(pathname === "\/locale\/report-detail"\) \{\s*const \{ handleLocaleReportDetail \} = await import\("\.\/locale-report-detail\.js"\)/);
    const code = workerSource.replace(/^import\s*\{[\s\S]*?\}\s*from\s*["']\.\/source-lead-adapter\.js["'];\s*/m,
      "function publicSourceLeadItem() {} async function readStoredSourceLead() {} async function searchSourceLeadMetadata() {} function sourceLeadAdapterEnabled() { return false; }\n")
      .replaceAll('await import("./locale-report-detail.js")', "await __loadLocale()")
      .replace("export default {", "globalThis.worker = {");
    const context = vm.createContext({ crypto: webcrypto, Request, Response, URL, URLSearchParams, TextEncoder, TextDecoder, Headers, AbortController, setTimeout, clearTimeout, console,
      fetch: async () => { throw new Error("network forbidden in test"); },
      __loadLocale: async () => { importCalls += 1; return api; },
    });
    vm.runInContext(code, context);
    const h = harness();
    assert.equal((await context.worker.fetch(new Request("https://portal.example.invalid/no-such-route"), {}, h.ctx)).status, 404);
    const health = await context.worker.fetch(new Request("https://portal.example.invalid/api/health"), {}, h.ctx);
    const healthBody = await health.json();
    assert.equal(healthBody.locale_detail_translation_v1.enabled, false);
    assert.equal(healthBody.capabilities.locale_detail_translation_v1, true);
    assert.equal(importCalls, 0);
    const invalid = await context.worker.fetch(request({ ...input, locale: "zh-CN" }), h.env, h.ctx);
    assert.equal(invalid.status, 400);
    assert.equal(importCalls, 1);
    assert.equal(h.bucket.gets + h.bucket.puts, 0);
    for (const [name, id] of [["catalog", "a".repeat(24)], ["external", "123456"], ["hot", `hot:${"a".repeat(16)}`], ["thinktank", "thinktank:abc123"], ["report-a", "report-a:abc123"], ["authority", "foreign:123456"], ["authority", `supplemental:${"a".repeat(32)}`]]) {
      assert.equal(context.validLocaleDetailId(name, id), true, `${name} canonical identity`);
      assert.equal(context.validLocaleDetailId(name, `${id}/private.pdf`), false);
    }
    context.loadCatalog = async () => ({ items: [{ id: input.id, title: "公开标题", title_zh: "公开标题", bank_name: "银行", industry: "行业", password: "PRIVATE", text: "MEMBER BODY", pdf_url: "PRIVATE", summary: "公开摘要" }] });
    const catalog = await context.resolveLocaleDetailPublicItem({}, "catalog", input.id);
    assert.doesNotMatch(JSON.stringify(catalog), /PRIVATE|MEMBER|password|pdf_url/);
    assert.equal(catalog.summary, "公开摘要");
    assert.equal(await context.resolveLocaleDetailPublicItem({}, "catalog", "b".repeat(24)), null);
    const previousFetch = globalThis.fetch;
    try {
      for (const payload of [{}, { main: {} }, { main: { title: " " } }]) {
        globalThis.fetch = async () => new Response(JSON.stringify(payload));
        assert.equal(await context.resolveLocaleDetailPublicItem({}, "external", "123456"), null, "upstream placeholders are not billable records");
      }
      globalThis.fetch = async () => new Response(JSON.stringify({ main: { title: "Public metadata", url_pdf: "PRIVATE" } }));
      const external = await context.resolveLocaleDetailPublicItem({}, "external", "123456");
      assert.equal(external.title, "Public metadata");
      assert.doesNotMatch(JSON.stringify(external), /PRIVATE|url_pdf/);
    } finally { globalThis.fetch = previousFetch; }
    context.findHotReportRow = async () => ({ row: { private: "PRIVATE" }, item: { title: "Hot metadata" } });
    assert.equal((await context.resolveLocaleDetailPublicItem({}, "hot", `hot:${"a".repeat(16)}`)).title, "Hot metadata");
    context.findThinkTankRow = async () => ({ title: "Thinktank metadata", local_filename: "report_abcdef.pdf", pdf_url: "PRIVATE", bytes: 42 });
    assert.doesNotMatch(JSON.stringify(await context.resolveLocaleDetailPublicItem({}, "thinktank", "thinktank:abcdef")), /PRIVATE|pdf_url/);
    let recovered = 0;
    context.readContactReportBinding = async () => null;
    context.recoverHiborContactReportTarget = async () => { recovered += 1; return null; };
    h.bucket.failGet = () => true;
    await assert.rejects(context.resolveLocaleDetailPublicItem(h.env, "report-a", "report-a:123"), /secret storage exception/);
    assert.equal(recovered, 0, "target storage errors cannot become paid source recovery");
  });

  process.stdout.write(`locale detail server: ${passed} tests passed (mock only)\n`);
}

main().catch((error) => { console.error(error); process.exitCode = 1; });
