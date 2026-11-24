import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import test from "node:test";

import { handleDropboxReady } from "../../workers/daily-source-wakeup/src/dropbox-ready.js";

const URL = "https://clock.example/dropbox-report-batch-ready";
const NOW = Date.parse("2026-11-24T02:00:00Z");
const proof = {
  date_folder: "261123", upstream_run_id: "45305004834", pdf_count: "48", manifest_sha256: "f".repeat(64),
};
const env = {
  GH_REPO: "downstream/reports",
  GH_DISPATCH_TOKEN: "test-destination-credential",
  REPORT_HANDOFF_SIGNING_KEY: "1a".repeat(32),
};

function request({
  inputs = proof, sentBody = JSON.stringify(inputs), signedBody = sentBody,
  url = URL, method = "POST", signed = true, timestamp = String(NOW / 1000),
  key = env.REPORT_HANDOFF_SIGNING_KEY,
} = {}) {
  const signature = createHmac("sha256", key).update(`${timestamp}\n${signedBody}`).digest("hex");
  return new Request(url, {
    method,
    headers: {
      "Content-Type": "application/json",
      ...(signed ? { Authorization: `ReportHMAC ${timestamp}.${signature}` } : {}),
    },
    ...(method === "POST" ? { body: sentBody } : {}),
  });
}

function fixture({ githubStatus = 204, lost = false } = {}) {
  const calls = [];
  return {
    calls,
    call(req, settings = env) {
      return handleDropboxReady(req, settings, {
        now: () => NOW,
        async fetchWithTimeout(url, options) {
          calls.push([url, options]);
          if (lost) throw new Error("transport timeout");
          return new Response(null, { status: githubStatus });
        },
      });
    },
  };
}

test("one signed request signals the fixed wake workflow with only its exact proof", async () => {
  const f = fixture();
  const response = await f.call(request());
  assert.equal(response.status, 202);
  assert.deepEqual(await response.json(), { state: "wake_accepted" });
  assert.equal(f.calls.length, 1);
  const [[dispatch, options]] = f.calls;
  assert.equal(dispatch, "https://api.github.com/repos/downstream/reports/actions/workflows/daily-report-source-wakeup.yml/dispatches");
  assert.equal(options.method, "POST");
  assert.equal(options.headers.Authorization, `Bearer ${env.GH_DISPATCH_TOKEN}`);
  assert.deepEqual(JSON.parse(options.body), { ref: "main", inputs: proof });
});

test("other routes, unsigned requests, malformed proof and oversized bodies cannot dispatch", async () => {
  const f = fixture();
  for (const [options, code] of [
    [{ url: "https://clock.example/" }, 404], [{ method: "GET" }, 405], [{ signed: false }, 401],
    [{ inputs: { ...proof, pdf_count: 48 } }, 400],
    [{ inputs: { ...proof, destination: "another/repo" } }, 400],
    [{ inputs: { ...proof, manifest_sha256: "a".repeat(1100) } }, 400],
  ]) assert.equal((await f.call(request(options))).status, code);
  assert.deepEqual(f.calls, []);
});

test("the signature covers the exact body, all fields, and a recent timestamp", async () => {
  const f = fixture();
  for (const options of [
    { key: "ad".repeat(32) },
    { signedBody: JSON.stringify({ ...proof, upstream_run_id: "1" }) },
    { signedBody: JSON.stringify(proof, null, 2) },
    { timestamp: String(NOW / 1000 - 301) },
    { timestamp: String(NOW / 1000 + 301) },
  ]) assert.equal((await f.call(request(options))).status, 401);
  assert.deepEqual(f.calls, []);
});

test("missing signing and dispatch credentials are unavailable without a dispatch", async () => {
  const f = fixture();
  for (const field of ["REPORT_HANDOFF_SIGNING_KEY", "GH_DISPATCH_TOKEN"]) {
    const response = await f.call(request(), { ...env, [field]: "" });
    assert.equal(response.status, 503);
    assert.deepEqual(await response.json(), { state: "dispatch_unconfigured" });
  }
  assert.deepEqual(f.calls, []);
});

test("failed and uncertain GitHub dispatches never cause a second POST", async () => {
  for (const [options, state] of [
    [{ githubStatus: 403 }, "wake_rejected"],
    [{ githubStatus: 503 }, "wake_outcome_unknown"],
    [{ lost: true }, "wake_outcome_unknown"],
  ]) {
    const f = fixture(options);
    const response = await f.call(request());
    assert.equal(response.status, 502);
    assert.deepEqual(await response.json(), { state });
    assert.equal(f.calls.length, 1);
  }
});
