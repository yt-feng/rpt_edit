import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const analytics = await readFile(new URL("../site_src/assets/analytics.js", import.meta.url), "utf8");
const start = app.indexOf("  async function downloadCatalogWithAccount(");
const end = app.indexOf("\n  function initReportAccessControls(", start);
assert.ok(start > 0 && end > start);
const downloadFunction = app.slice(start, end);
const settle = () => new Promise((resolve) => setImmediate(resolve));

function harness(stage) {
  const posts = [], storage = new Map(), saves = [], notices = [];
  let resets = 0, clearedTimers = 0;
  const privateError = new Error("PRIVATE user@example.invalid https://private.example?token=secret");
  const document = {
    body: { dataset: { page: "report", analyticsAuto: "manual" } }, readyState: "complete", referrer: "",
    addEventListener() {}, getElementById() { return {}; },
  };
  const window = {
    document, location: { origin: "https://portal.example.invalid", pathname: "/report.html", search: "" },
    localStorage: { getItem: (key) => storage.get(key), setItem: (key, value) => storage.set(key, value) },
    navigator: { language: "en", userAgent: "test" },
    async fetch(url, init) {
      if (url === "/data/config.json") return { ok: true, json: async () => ({ worker_base_url: "/api" }) };
      posts.push(JSON.parse(init.body));
      return { ok: true };
    },
    setInterval() { return 123; }, clearInterval() { clearedTimers += 1; },
  };
  vm.runInNewContext(analytics, { window, URL, URLSearchParams, TextEncoder });
  const context = {
    window, document,
    resetDownloadProgress() { resets += 1; }, setDownloadMessage() {},
    trackEvent(_worker, type, data) { window.PortalSuiteAnalytics.track(type, data); },
    analyticsReportPayload(item, source) { return { report_id: item.id, source }; },
    authHeaders() { return {}; }, clearAuthSession() {},
    downloadErrorMessage(_status, message) { return message; },
    async fetch() {
      if (stage === "network") throw privateError;
      return { ok: stage !== "http", status: stage === "http" ? 403 : 200, json: async () => ({}), headers: { get() { return ""; } } };
    },
    async responseBlobWithProgress() { if (stage === "body") throw privateError; return "fixture-blob"; },
    triggerBlobDownload(blob) { saves.push(blob); },
    showDownloadInvitation() {},
  };
  vm.runInNewContext(`${downloadFunction}\nthis.download = downloadCatalogWithAccount;`, context);
  return {
    window, posts, saves, privateError, counts: () => ({ resets, clearedTimers }),
    run: () => context.download("/api", { id: "report-fixture", filename: "fixture.pdf" }, (...args) => notices.push(args)),
    events: () => posts.flatMap((post) => post.events || [post]),
  };
}

for (const stage of ["network", "body"]) {
  test(`account download ${stage} failure retains the original error and emits one fixed diagnostic`, async () => {
    const client = harness(stage);
    await assert.rejects(client.run(), (error) => error === client.privateError);
    await settle();
    const events = client.events();
    assert.equal(events.filter((event) => event.type === "download_attempt").length, 1);
    const errors = events.filter((event) => event.type === "download_error");
    assert.equal(errors.length, 1);
    assert.equal(errors[0].data.status, stage);
    assert.equal(errors[0].data.error, `${stage}_failed`);
    assert.equal(errors[0].data.report_id, "report-fixture");
    assert.equal(errors[0].data.action, "account_download");
    assert.equal(events.filter((event) => event.type === "download_success").length, 0);
    assert.doesNotMatch(JSON.stringify(events), /PRIVATE|user@example|token=secret|private\.example/);
    assert.deepEqual(client.saves, []);
    assert.equal(client.counts().clearedTimers, 1);
    assert.equal(client.counts().resets, 2);
  });
}

test("successful and HTTP-error downloads do not acquire duplicate diagnostics", async () => {
  const success = harness("success");
  await success.run();
  await settle();
  assert.deepEqual(success.events().map((event) => event.type), ["download_attempt", "download_success"]);
  assert.deepEqual(success.saves, ["fixture-blob"]);
  const denied = harness("http");
  await assert.rejects(denied.run());
  await settle();
  assert.deepEqual(denied.events().map((event) => event.type), ["download_attempt", "download_error"]);
  assert.equal(denied.events()[1].data.status, "403");
});

test("download diagnostic helper rejects arbitrary failure stages", async () => {
  const client = harness("success");
  for (const stage of ["PRIVATE@example.invalid", "network_failed", null, {}, "constructor"]) {
    assert.equal(client.window.PortalSuiteAnalytics.downloadError("report-fixture", stage), false);
  }
  await settle();
  assert.deepEqual(client.events(), []);
});
