import assert from "node:assert/strict";
import { createHash } from "node:crypto";
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
    this.putKeys = [];
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
    this.putKeys.push(String(key));
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

function contactTargetKey(source, originId) {
  const digest = createHash("sha256")
    .update(`portal-contact-report:v1:${source}:${originId}`)
    .digest("hex");
  return `_contact-reports/v1/targets/${digest}.json`;
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
  assert.match(workflow, /for test_file in portal_suite\/tests\/\*\.test\.mjs; do/u);
  assert.match(workflow, /node --test "\$test_file"/u);
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

test("an id-only Report A detail self-heals canonical metadata and sends exactly one real provider request", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originId = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  const canonicalTitle = "申港证券-电子行业研究周报：MLCC开启新一轮涨价，关注订单溢出和国产替代-260802";
  let detailGets = 0;
  let detailPosts = 0;
  const deliveries = [];
  await withMockFetch(async (resource, init = {}) => {
    const url = String(resource);
    if (url === "https://www.hibor.com.cn/data/7272f7466fea33f5ca7e66afc23a0a90.html") {
      detailGets += 1;
      return new Response("<script>var ncid = '5c9d501d-2526-4379-b3a5-b0f1ed20886f';</script>", {
        status: 200,
        headers: {
          "Set-Cookie": "unrelated=ignore-me; Path=/, safedog-flow-item=flow_7272-A%2B; Path=/; HttpOnly, second=ignore-too; Path=/",
        },
      });
    }
    if (url === "https://www.hibor.com.cn/hiborweb/DocDetail/NewContent") {
      detailPosts += 1;
      assert.equal(init.method, "POST");
      assert.match(String(init.body || ""), /ncid=5c9d501d-2526-4379-b3a5-b0f1ed20886f/u);
      assert.equal(new Headers(init.headers).get("cookie"), "safedog-flow-item=flow_7272-A%2B");
      return new Response(`
        <h1>${canonicalTitle}</h1>
        <div class="doc-info">
          <span class="article-time">日期：2026-08-06 16:55:07</span>
          <span>研报出处：<a>申港证券</a></span>
        </div>
        <div class="doc-info-list">
          <span>研报栏目：<a>行业分析</a></span>
          <span class="author"><b></b><a>王伟</a></span>
          <span><img>&nbsp;<i>(PDF)</i></span>
          <span><i>10 页</i></span>
        </div>
      `, { status: 200 });
    }
    if (url === "https://api.brevo.com/v3/smtp/email") {
      deliveries.push(JSON.parse(init.body));
      return brevoSuccess("report-a-provider-message");
    }
    throw new Error(`unexpected fetch: ${url}`);
  }, async () => {
    const detailRequest = new Request(
      `https://worker.example.invalid/contact-report/item?source=report-a&id=${encodeURIComponent(originId)}`,
    );
    const detailResponse = await worker.fetch(detailRequest, env, { waitUntil() {} });
    assert.equal(detailResponse.status, 200);
    const detail = await detailResponse.json();
    assert.equal(detail.item.title, canonicalTitle);
    assert.equal(detail.item.institution, "申港证券");
    assert.equal(detail.item.date, "2026-08-06");
    assert.equal(detail.item.category, "行业分析");
    assert.equal(detail.item.author, "王伟");
    assert.equal(detail.item.page_count, 10);
    assert.ok(detail.item.request_token);
    assert.equal(bucket.jsonRows("_contact-reports/v1/targets/").length, 1);

    const secondDetail = await worker.fetch(detailRequest, env, { waitUntil() {} });
    assert.equal(secondDetail.status, 200);
    assert.equal(detailGets, 1, "the healed target must be served from R2 after the first lookup");
    assert.equal(detailPosts, 1);
    assert.equal(bucket.jsonRows("_contact-reports/v1/targets/").length, 1);

    const submitted = await postReportRequest(env, requestBody({
      report_id: originId,
      title: "FAKE CLIENT TITLE",
      source: "report-a",
      institution: "client supplied institution",
      requester_email: "report-a-reader@example.net",
      request_token: detail.item.request_token,
    }));
    assert.equal(submitted.response.status, 202);
    assert.equal(submitted.data.ok, true);
  });

  assert.equal(deliveries.length, 1, "one click must make exactly one Brevo send call");
  assert.deepEqual(deliveries[0].to, [{ email: EXPECTED_CONTACT }]);
  assert.match(deliveries[0].subject, new RegExp(canonicalTitle, "u"));
  assert.doesNotMatch(deliveries[0].subject, /FAKE CLIENT TITLE/u);
  assert.match(deliveries[0].textContent, /机构：申港证券/u);
  assert.doesNotMatch(deliveries[0].textContent, /client supplied institution/u);
  const saved = bucket.jsonRows("_report-requests/v1/items/");
  assert.equal(saved.length, 1);
  assert.equal(saved[0].value.title, canonicalTitle);
  assert.equal(saved[0].value.institution, "申港证券");
  assert.equal(saved[0].value.status, "sent");
  assert.equal(saved[0].value.message_id, "report-a-provider-message");
});

test("Report A self-healing uses one deadline across the detail and content bodies", async () => {
  const originId = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  const startedAt = Date.now();
  await withMockFetch(async (resource) => {
    const url = String(resource);
    if (url.includes("/data/7272f7466fea33f5ca7e66afc23a0a90.html")) {
      await new Promise((resolve) => setTimeout(resolve, 15));
      return new Response("<script>var ncid='5c9d501d-2526-4379-b3a5-b0f1ed20886f';</script>");
    }
    if (url.includes("/hiborweb/DocDetail/NewContent")) return new Promise(() => {});
    throw new Error(`unexpected fetch: ${url}`);
  }, async () => {
    await assert.rejects(
      worker.__reportRequestTest.recoverHiborContactReportTarget(originId, 35),
      (error) => error && error.name === "TimeoutError",
    );
  });
  assert.ok(Date.now() - startedAt < 250, "the second body may only use the first stage's remaining deadline");
});

test("Report A recovery fails closed for empty or title-less detail content", async () => {
  const originId = "report-a:7272f7466fea33f5ca7e66afc23a0a90";
  let contentAttempt = 0;
  await withMockFetch(async (resource, init = {}) => {
    const url = String(resource);
    if (url.includes("/data/7272f7466fea33f5ca7e66afc23a0a90.html")) {
      return new Response("<script>var ncid='5c9d501d-2526-4379-b3a5-b0f1ed20886f';</script>", {
        headers: { "Set-Cookie": "safedog-flow-item=strict-cookie-1; Path=/" },
      });
    }
    if (url.includes("/hiborweb/DocDetail/NewContent")) {
      assert.equal(new Headers(init.headers).get("cookie"), "safedog-flow-item=strict-cookie-1");
      contentAttempt += 1;
      return new Response(contentAttempt === 1 ? "" : "<div>metadata without an h1 title</div>");
    }
    throw new Error(`unexpected fetch: ${url}`);
  }, async () => {
    assert.equal(await worker.__reportRequestTest.recoverHiborContactReportTarget(originId), null);
    assert.equal(await worker.__reportRequestTest.recoverHiborContactReportTarget(originId), null);
  });
});

test("signed target metadata stays within the detail URL bound and survives URL roundtrip", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originId = "foreign:33860973";
  const metadata = {
    id: originId,
    source: "authority",
    title: `${"题".repeat(318)}：终`,
    institution: "机".repeat(160),
    date: "2026-08-21",
    kind: "类".repeat(40),
    kind_label: "标".repeat(80),
    report_type: "型".repeat(120),
    language: "语".repeat(40),
    category: "栏".repeat(120),
    author: "作".repeat(250),
    rating: "评".repeat(80),
    page_count: 7,
  };
  const token = await worker.__reportRequestTest.createContactReportTargetToken(
    env,
    "authority",
    originId,
    metadata,
  );
  assert.ok(token);
  assert.ok(token.length <= 4096, `proof is ${token.length} characters`);
  const url = new URL("https://portal.example.invalid/doc.html");
  url.searchParams.set("rt", token);
  const roundTripped = new URL(url.href).searchParams.get("rt");
  assert.equal(roundTripped, token);
  const proof = await worker.__reportRequestTest.inspectContactReportTargetToken(
    env,
    roundTripped,
    "authority",
    originId,
  );
  assert.equal(proof.valid, true);
  assert.equal(proof.target.title, metadata.title);
  assert.equal(proof.target.institution, metadata.institution);
  assert.equal(proof.target.page_count, 7);
});

test("NashAI search signs the live canonical sample, request ignores client tampering, and detail writes one target", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originId = "foreign:33860973";
  const canonicalTitle = "PACS Added: JEF H/C Svcs & Tech Conf (Nash 9/14-15) Featuring CMS COO & AI Head";
  const deliveries = [];
  await withMockFetch(async (resource, init = {}) => {
    const url = String(resource);
    if (url === "https://www.nash-ai.cn/reports/foreign/search") {
      assert.equal(init.method, "POST");
      return new Response(JSON.stringify({
        code: 200,
        data: {
          pageNum: 1,
          total: 1,
          records: [{
            id: 33860973,
            title: canonicalTitle,
            securities: "Jefferies",
            reDate: "2026-08-21",
            page: 7,
          }],
        },
      }), { headers: { "Content-Type": "application/json" } });
    }
    if (url === "https://api.brevo.com/v3/smtp/email") {
      deliveries.push(JSON.parse(init.body));
      return brevoSuccess("nash-canonical-message");
    }
    throw new Error(`unexpected fetch: ${url}`);
  }, async () => {
    const searchResponse = await worker.fetch(new Request(
      "https://worker.example.invalid/authority/search?q=PACS&page=1&kind=foreign",
    ), env, { waitUntil() {} });
    assert.equal(searchResponse.status, 200);
    const search = await searchResponse.json();
    assert.equal(search.items.length, 1);
    assert.equal(search.items[0].id, originId);
    assert.equal(search.items[0].title, canonicalTitle);
    assert.equal(search.items[0].institution, "Jefferies");
    assert.equal(search.items[0].date, "2026-08-21");
    assert.equal(search.items[0].page_count, 7);
    assert.ok(search.items[0].request_token);
    assert.equal(bucket.jsonRows("_contact-reports/v1/targets/").length, 0);
    assert.equal(bucket.putKeys.filter((key) => key.startsWith("_contact-reports/v1/targets/")).length, 0);

    const submitted = await postReportRequest(env, requestBody({
      report_id: originId,
      title: "FAKE NASH TITLE",
      source: "authority",
      institution: "Fake Institution",
      requester_email: "nash-reader@example.net",
      request_token: search.items[0].request_token,
    }));
    assert.equal(submitted.response.status, 202);
    assert.equal(bucket.jsonRows("_contact-reports/v1/targets/").length, 0, "request validation can use claims without a target write");

    await bucket.put(contactTargetKey("authority", originId), JSON.stringify({
      id: originId,
      origin_id: originId,
      source: "authority",
      title: "Stale cached Nash title",
      institution: "Stale Institution",
      date: "2025-01-01",
      page_count: 1,
      file_type: "pdf",
      verified_at: "2025-01-01T00:00:00.000Z",
    }));
    bucket.putKeys.length = 0;

    const detailResponse = await worker.fetch(new Request(
      `https://worker.example.invalid/contact-report/item?source=authority&id=${encodeURIComponent(originId)}&request_token=${encodeURIComponent(search.items[0].request_token)}`,
    ), env, { waitUntil() {} });
    assert.equal(detailResponse.status, 200);
    const detail = await detailResponse.json();
    assert.equal(detail.item.title, canonicalTitle);
    assert.equal(detail.item.institution, "Jefferies");
    assert.equal(detail.item.date, "2026-08-21");
    assert.equal(detail.item.page_count, 7);
    assert.equal(bucket.putKeys.filter((key) => key.startsWith("_contact-reports/v1/targets/")).length, 1);
    assert.equal(bucket.jsonRows("_contact-reports/v1/targets/")[0].value.title, canonicalTitle);

    const compactResponse = await worker.fetch(new Request(
      `https://worker.example.invalid/contact-report/item?source=authority&id=${encodeURIComponent(originId)}`,
    ), env, { waitUntil() {} });
    assert.equal(compactResponse.status, 200);
    assert.equal((await compactResponse.json()).item.title, canonicalTitle);
    assert.equal(bucket.putKeys.filter((key) => key.startsWith("_contact-reports/v1/targets/")).length, 1);
  });

  assert.equal(deliveries.length, 1);
  assert.match(deliveries[0].subject, new RegExp(canonicalTitle.replace(/[.*+?^${}()|[\]\\]/g, "\\$&"), "u"));
  assert.match(deliveries[0].textContent, /机构：Jefferies/u);
  assert.doesNotMatch(deliveries[0].textContent, /FAKE NASH TITLE|Fake Institution/u);
  const saved = bucket.jsonRows("_report-requests/v1/items/");
  assert.equal(saved.length, 1);
  assert.equal(saved[0].value.title, canonicalTitle);
  assert.equal(saved[0].value.institution, "Jefferies");
  assert.equal(saved[0].value.message_id, "nash-canonical-message");
});

test("an old NashAI id-only link recovers exact metadata from the server mirror and mints valid proof", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const originId = "foreign:33860973";
  const canonicalTitle = "PACS Added: JEF H/C Svcs & Tech Conf (Nash 9/14-15) Featuring CMS COO & AI Head";
  await bucket.put("_search-mirror/authority/latest.json", JSON.stringify({
    generated_at: "2026-08-27T00:00:00.000Z",
    items: [{
      id: originId,
      source: "authority",
      kind: "foreign",
      kind_label: "普通外文",
      title: canonicalTitle,
      institution: "Jefferies",
      date: "2026-08-21",
      page_count: 7,
      file_type: "pdf",
    }],
  }));
  bucket.putKeys.length = 0;
  const deliveries = [];
  await withMockFetch(async (resource, init = {}) => {
    if (String(resource) === "https://api.brevo.com/v3/smtp/email") {
      deliveries.push(JSON.parse(init.body));
      return brevoSuccess("nash-mirror-message");
    }
    throw new Error(`unexpected fetch: ${resource}`);
  }, async () => {
    const detailResponse = await worker.fetch(new Request(
      `https://worker.example.invalid/contact-report/item?source=authority&id=${encodeURIComponent(originId)}`,
    ), env, { waitUntil() {} });
    assert.equal(detailResponse.status, 200);
    const detail = await detailResponse.json();
    assert.equal(detail.item.title, canonicalTitle);
    assert.equal(detail.item.institution, "Jefferies");
    assert.equal(detail.item.date, "2026-08-21");
    assert.equal(detail.item.page_count, 7);
    assert.ok(detail.item.request_token);
    assert.equal(bucket.putKeys.filter((key) => key.startsWith("_contact-reports/v1/targets/")).length, 1);

    const submitted = await postReportRequest(env, requestBody({
      report_id: originId,
      title: "CLIENT OVERRIDE",
      source: "authority",
      institution: "Client Override Institution",
      requester_email: "old-nash-reader@example.net",
      request_token: detail.item.request_token,
    }));
    assert.equal(submitted.response.status, 202);
  });
  assert.equal(deliveries.length, 1);
  assert.match(deliveries[0].subject, /PACS Added/u);
  assert.doesNotMatch(deliveries[0].textContent, /CLIENT OVERRIDE|Client Override Institution/u);
  const saved = bucket.jsonRows("_report-requests/v1/items/");
  assert.equal(saved[0].value.title, canonicalTitle);
  assert.equal(saved[0].value.institution, "Jefferies");
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
