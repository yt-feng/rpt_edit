import assert from "node:assert/strict";
import { createHash, createHmac } from "node:crypto";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));

class MemoryR2 {
  constructor() {
    this.data = new Map();
  }

  async get(key) {
    if (!this.data.has(key)) return null;
    const value = this.data.get(key);
    return { async text() { return value; } };
  }

  async put(key, value) {
    this.data.set(key, String(value));
  }

  seed(key, value) {
    this.data.set(key, JSON.stringify(value));
  }

  json(key) {
    return JSON.parse(this.data.get(key));
  }
}

function alertStateKey(dedupeKey) {
  return `_ops/alerts/${createHash("sha256").update(dedupeKey).digest("hex")}.json`;
}

function alertEnv(bucket) {
  return {
    REPORT_BUCKET: bucket,
    OPS_ALERT_SIGNING_KEY: "ops-alert-test-secret",
    OPS_ALERT_EMAIL: "owner@example.invalid",
    NEWSFEED_EMAIL_PROVIDER: "brevo",
    BREVO_API_KEY: "brevo-test-key",
    BREVO_SENDER_EMAIL: "sender@example.invalid",
  };
}

async function postAlert(env, payload) {
  const body = JSON.stringify(payload);
  const timestamp = String(Math.floor(Date.now() / 1000));
  const signature = createHmac("sha256", env.OPS_ALERT_SIGNING_KEY)
    .update(`${timestamp}.${body}`)
    .digest("hex");
  const request = new Request("https://worker.example.invalid/ops/alerts/email", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      "X-Portal-Timestamp": timestamp,
      "X-Portal-Signature": `sha256=${signature}`,
    },
    body,
  });
  const response = await worker.fetch(request, env, { waitUntil() {} });
  return { response, data: await response.json() };
}

async function withMockFetch(mock, callback) {
  const original = globalThis.fetch;
  globalThis.fetch = mock;
  try {
    return await callback();
  } finally {
    globalThis.fetch = original;
  }
}

test("operations alerts retain the 24-hour default and persist the selected window", async () => {
  const bucket = new MemoryR2();
  const env = alertEnv(bucket);
  const result = await withMockFetch(
    async () => new Response(JSON.stringify({ messageId: "message-1" }), { status: 201 }),
    () => postAlert(env, {
      subject: "Workflow failed",
      text: "Open the run log.",
      dedupe_key: "default-window",
      severity: "warning",
    }),
  );

  assert.equal(result.response.status, 200);
  assert.equal(result.data.sent, true);
  assert.equal(result.data.dedupe_window_hours, 24);
  assert.equal(bucket.json(alertStateKey("default-window")).dedupe_window_hours, 24);
});

test("operations alerts use the requested capped window when checking previous state", async () => {
  const bucket = new MemoryR2();
  const env = alertEnv(bucket);
  const dedupeKey = "custom-window";
  const stateKey = alertStateKey(dedupeKey);
  bucket.seed(stateKey, {
    sent: true,
    sent_at: new Date(Date.now() - (25 * 60 * 60 * 1000)).toISOString(),
    provider: "brevo",
  });

  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return new Response(JSON.stringify({ messageId: `message-${sends}` }), { status: 201 });
  }, async () => {
    const capped = await postAlert(env, {
      subject: "Workflow failed",
      text: "Open the run log.",
      dedupe_key: dedupeKey,
      dedupe_window_hours: 999,
    });
    assert.equal(capped.data.deduplicated, true);
    assert.equal(capped.data.dedupe_window_hours, 720);
    assert.equal(sends, 0);

    const short = await postAlert(env, {
      subject: "Workflow failed",
      text: "Open the run log.",
      dedupe_key: dedupeKey,
      dedupe_window_hours: 0,
    });
    assert.equal(short.data.sent, true);
    assert.equal(short.data.deduplicated, undefined);
    assert.equal(short.data.dedupe_window_hours, 1);
    assert.equal(sends, 1);
    assert.equal(bucket.json(stateKey).dedupe_window_hours, 1);
  });
});
