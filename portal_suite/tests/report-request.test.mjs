import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const { default: worker } = await import(workerPath);

const PORTAL_ORIGIN = "https://portal.example.invalid";
const EXPECTED_CONTACT = ["info", "@", "kc", "desk", ".com"].join("");

class MemoryR2 {
  constructor() {
    this.data = new Map();
    this.version = 0;
  }

  async get(key) {
    const row = this.data.get(key);
    if (!row) return null;
    return {
      etag: row.etag,
      async text() { return row.value; },
    };
  }

  async put(key, value, options = {}) {
    const current = this.data.get(key);
    const condition = options.onlyIf || {};
    if (condition.etagMatches && (!current || current.etag !== condition.etagMatches)) return null;
    if (condition.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const stored = {
      value: typeof value === "string" ? value : new TextDecoder().decode(value),
      etag: `etag-${this.version}`,
    };
    this.data.set(key, stored);
    return { etag: stored.etag };
  }

  jsonRows(prefix) {
    return [...this.data.entries()]
      .filter(([key]) => key.startsWith(prefix))
      .map(([key, row]) => ({ key, value: JSON.parse(row.value) }));
  }
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    MASTER_KEY: "report-request-test-secret",
    ALLOWED_ORIGIN: PORTAL_ORIGIN,
    NEWSFEED_EMAIL_PROVIDER: "brevo",
    BREVO_API_KEY: "brevo-test-key",
    BREVO_SENDER_EMAIL: "sender@example.invalid",
    BREVO_SENDER_NAME: "Test Sender",
  };
}

function requestBody(overrides = {}) {
  return {
    report_id: "report-001",
    title: "Global market outlook",
    source: "catalog",
    institution: "Example Research",
    page_path: "/report.html?id=report-001",
    requester_email: "reader@example.net",
    honeypot: "",
    ...overrides,
  };
}

async function postReportRequest(env, body, options = {}) {
  const headers = {
    "Content-Type": "application/json",
    ...(options.origin === false ? {} : { "Origin": options.origin || PORTAL_ORIGIN }),
    ...(options.headers || {}),
  };
  const request = new Request("https://worker.example.invalid/report-request", {
    method: "POST",
    headers,
    body: options.rawBody === undefined ? JSON.stringify(body) : options.rawBody,
  });
  const response = await worker.fetch(request, env, { waitUntil() {} });
  const data = await response.json().catch(() => ({}));
  return { response, data };
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

function brevoSuccess(messageId = "message-1") {
  return new Response(JSON.stringify({ messageId }), {
    status: 201,
    headers: { "Content-Type": "application/json" },
  });
}

test("registration has no Email Routing side effect and deployment runs the report request test", async () => {
  const source = await readFile(workerPath, "utf8");
  const workflow = await readFile(path.join(root, ".github/workflows/portal-worker-emergency-deploy.yml"), "utf8");
  assert.doesNotMatch(source, /requestCloudflareDestinationVerification|email_destination|CLOUDFLARE_EMAIL_ROUTING/u);
  assert.doesNotMatch(workflow, /CLOUDFLARE_EMAIL_ROUTING/u);
  assert.match(workflow, /node --test portal_suite\/tests\/\*\.test\.mjs/u);
});

async function accountToken(secret, user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    session_epoch: "",
    iat: now,
    exp: now + 3600,
  })).toString("base64url");
  const key = await crypto.subtle.importKey(
    "raw",
    new TextEncoder().encode(secret),
    { name: "HMAC", hash: "SHA-256" },
    false,
    ["sign"],
  );
  const signature = await crypto.subtle.sign(
    "HMAC",
    key,
    new TextEncoder().encode(`portal:account-token:v1:${body}`),
  );
  return `${body}.${Buffer.from(signature).toString("base64url")}`;
}

test("report request enforces same-origin, bounded JSON, guest email and honeypot validation", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess();
  }, async () => {
    const foreign = await postReportRequest(env, requestBody(), { origin: "https://foreign.example" });
    assert.equal(foreign.response.status, 403);

    const missingOrigin = await postReportRequest(env, requestBody(), { origin: false });
    assert.equal(missingOrigin.response.status, 403);

    const malformed = await postReportRequest(env, null, { rawBody: "{" });
    assert.equal(malformed.response.status, 400);

    const oversized = await postReportRequest(env, null, { rawBody: JSON.stringify({ title: "x".repeat(9000) }) });
    assert.equal(oversized.response.status, 413);

    const missingTitle = await postReportRequest(env, requestBody({ title: "" }));
    assert.equal(missingTitle.response.status, 400);

    const invalidEmail = await postReportRequest(env, requestBody({ requester_email: "not-an-email" }));
    assert.equal(invalidEmail.response.status, 400);

    const trapped = await postReportRequest(env, requestBody({ honeypot: "filled-by-bot" }));
    assert.equal(trapped.response.status, 202);
    assert.equal(trapped.data.ok, true);
  });
  assert.equal(sends, 0);
  assert.equal(bucket.data.size, 0, "rejected and honeypot submissions must not be persisted");
});

test("report request persists before sending to the fixed contact and escapes HTML", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const deliveries = [];
  const title = "Alpha <script>alert('x')</script> & Co";
  const result = await withMockFetch(async (_url, init) => {
    const pending = bucket.jsonRows("_report-requests/v1/items/");
    assert.equal(pending.length, 1, "request record must exist before the email call");
    assert.equal(pending[0].value.status, "pending");
    deliveries.push(JSON.parse(init.body));
    return brevoSuccess("fixed-contact-message");
  }, () => postReportRequest(env, requestBody({
    title,
    to: "attacker@example.net",
    recipient: "attacker@example.net",
  })));

  assert.equal(result.response.status, 202);
  assert.equal(result.data.ok, true);
  assert.equal(result.data.deduplicated, false);
  assert.equal(deliveries.length, 1);
  assert.deepEqual(deliveries[0].to, [{ email: EXPECTED_CONTACT }]);
  assert.deepEqual(deliveries[0].tags, ["portal-report-request"]);
  assert.match(deliveries[0].htmlContent, /Alpha &lt;script&gt;alert\('x'\)&lt;\/script&gt; &amp; Co/u);
  assert.doesNotMatch(deliveries[0].htmlContent, /<script>/u);
  const responseText = JSON.stringify(result.data);
  assert.doesNotMatch(responseText, new RegExp(EXPECTED_CONTACT.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "u"));
  assert.doesNotMatch(responseText, /attacker@example\.net/u);
  const saved = bucket.jsonRows("_report-requests/v1/items/");
  assert.equal(saved[0].value.status, "sent");
  assert.ok(saved[0].value.sent_at);
});

test("an authenticated request uses the account email instead of a client override", async () => {
  const bucket = new MemoryR2();
  const env = { ...envFor(bucket), ACCOUNT_STORE_MODE: "r2" };
  const user = {
    id: "user-1",
    username: "member-a",
    email: "member@example.net",
    password_salt: "unused",
    password_hash: "unused",
    created_at: new Date().toISOString(),
    updated_at: new Date().toISOString(),
  };
  await bucket.put(`_account/users/username/${user.username}`, JSON.stringify(user));
  const token = await accountToken(env.MASTER_KEY, user);
  let delivery = null;
  const result = await withMockFetch(async (_url, init) => {
    delivery = JSON.parse(init.body);
    return brevoSuccess("account-email-message");
  }, () => postReportRequest(env, requestBody({ requester_email: "spoofed@example.net" }), {
    headers: { "Authorization": `Bearer ${token}` },
  }));

  assert.equal(result.response.status, 202);
  assert.match(delivery.textContent, /申请邮箱：member@example\.net/u);
  assert.doesNotMatch(delivery.textContent, /spoofed@example\.net/u);
  const saved = bucket.jsonRows("_report-requests/v1/items/");
  assert.equal(saved[0].value.requester_email, user.email);
  assert.equal(saved[0].value.authenticated, true);
});

test("successful report requests deduplicate for 24 hours", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess(`message-${sends}`);
  }, async () => {
    const first = await postReportRequest(env, requestBody());
    const duplicate = await postReportRequest(env, requestBody({ page_path: "/other-page.html" }));
    assert.equal(first.response.status, 202);
    assert.equal(duplicate.response.status, 200);
    assert.equal(duplicate.data.ok, true);
    assert.equal(duplicate.data.deduplicated, true);
    assert.match(duplicate.data.detail, /24小时/u);
  });
  assert.equal(sends, 1);
});

test("report request applies a rolling per-email limit", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess(`rate-message-${sends}`);
  }, async () => {
    for (let index = 0; index < 6; index += 1) {
      const accepted = await postReportRequest(env, requestBody({
        report_id: `report-rate-${index}`,
        title: `Rate report ${index}`,
      }));
      assert.equal(accepted.response.status, 202);
    }
    const limited = await postReportRequest(env, requestBody({
      report_id: "report-rate-limited",
      title: "Rate report limited",
    }));
    assert.equal(limited.response.status, 429);
    assert.equal(limited.data.retryable, true);
  });
  assert.equal(sends, 6);
});

test("report request applies a rolling per-IP limit across guest emails", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  const headers = { "CF-Connecting-IP": "203.0.113.42" };
  await withMockFetch(async () => {
    sends += 1;
    return brevoSuccess(`ip-rate-message-${sends}`);
  }, async () => {
    for (let index = 0; index < 20; index += 1) {
      const accepted = await postReportRequest(env, requestBody({
        report_id: `report-ip-${index}`,
        title: `IP report ${index}`,
        requester_email: `reader-${index}@example.net`,
      }), { headers });
      assert.equal(accepted.response.status, 202);
    }
    const limited = await postReportRequest(env, requestBody({
      report_id: "report-ip-limited",
      title: "IP report limited",
      requester_email: "reader-limited@example.net",
    }), { headers });
    assert.equal(limited.response.status, 429);
    assert.equal(limited.data.retryable, true);
  });
  assert.equal(sends, 20);
});

test("a failed provider attempt stays retryable and only a later success deduplicates", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  let sends = 0;
  await withMockFetch(async () => {
    sends += 1;
    if (sends === 1) {
      return new Response(JSON.stringify({ message: "temporary failure" }), {
        status: 503,
        headers: { "Content-Type": "application/json" },
      });
    }
    return brevoSuccess("retry-success");
  }, async () => {
    const failed = await postReportRequest(env, requestBody());
    assert.equal(failed.response.status, 502);
    assert.equal(failed.data.retryable, true);
    assert.match(failed.data.detail, /稍后重试/u);

    const retried = await postReportRequest(env, requestBody());
    assert.equal(retried.response.status, 202);
    assert.equal(retried.data.ok, true);

    const duplicate = await postReportRequest(env, requestBody());
    assert.equal(duplicate.response.status, 200);
    assert.equal(duplicate.data.deduplicated, true);
  });
  assert.equal(sends, 2);
});
