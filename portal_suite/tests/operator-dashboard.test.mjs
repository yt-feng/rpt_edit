import assert from "node:assert/strict";
import { createHmac } from "node:crypto";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const workerPath = path.join(root, "workers/portal-suite-worker/src/index.js");
const appPath = path.join(root, "portal_suite/site_src/assets/app.js");
const [{ default: worker }, app] = await Promise.all([
  import(workerPath),
  readFile(appPath, "utf8"),
]);

const AUTH_SECRET = "operator-dashboard-test-secret";
const CATALOG_URL = "https://catalog.operator-dashboard.test/catalog.json";
const SNAPSHOT_PREFIX = "_account/admin-snapshots";
const PICKS_KEY = `${SNAPSHOT_PREFIX}/picks-v3.json`;
const FILES_KEY = `${SNAPSHOT_PREFIX}/files.json`;
const FIXTURE_TIME = "2026-08-02T08:00:00.000Z";
const OPERATOR_A = {
  id: "operator-operator-a",
  username: "operator-a",
  email: "operator-a@users.portal.example.invalid",
  created_at: "2026-07-01T00:00:00.000Z",
  updated_at: FIXTURE_TIME,
  last_login_at: FIXTURE_TIME,
};
const CATALOG = {
  generated_at: FIXTURE_TIME,
  items: Array.from({ length: 6 }, (_value, index) => ({
    id: `operator-pick-${index + 1}`,
    title: `Global Macro Strategy ${index + 1}`,
    title_zh: `全球宏观策略 ${index + 1}`,
    filename: `global-macro-${index + 1}.pdf`,
    bank_code: index % 2 ? "GS" : "NOM",
    bank_name: index % 2 ? "高盛" : "野村",
    date_folder: "260802",
    page_count: 20 + index,
    first_page_landscape: index === 0,
    available: true,
  })),
};

globalThis.fetch = async (input) => {
  const url = input instanceof Request ? input.url : String(input);
  if (url === CATALOG_URL) {
    return new Response(JSON.stringify(CATALOG), {
      status: 200,
      headers: { "content-type": "application/json" },
    });
  }
  throw new Error(`Unexpected network request in operator test: ${url}`);
};

function accountKey(...parts) {
  return ["_account", ...parts.map((part) => encodeURIComponent(String(part || "")))].join("/");
}

class MemoryR2 {
  constructor({ failFirstGet = "" } = {}) {
    this.data = new Map();
    this.events = [];
    this.failFirstGet = failFirstGet;
    this.failedFirstGet = false;
  }

  seed(key, value) {
    this.data.set(key, typeof value === "string" || value instanceof Uint8Array ? value : JSON.stringify(value));
  }

  async get(key) {
    this.events.push({ op: "get", key });
    if (key === this.failFirstGet && !this.failedFirstGet) {
      this.failedFirstGet = true;
      throw new Error("transient R2 read failure");
    }
    if (!this.data.has(key)) return null;
    const value = this.data.get(key);
    const bytes = value instanceof Uint8Array ? value : new TextEncoder().encode(String(value));
    return {
      body: bytes,
      size: bytes.byteLength,
      etag: `etag-${key}`,
      async text() { return value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value); },
    };
  }

  async put(key, value) {
    this.events.push({ op: "put", key });
    this.seed(key, value);
    return { key, etag: `etag-${key}` };
  }

  async list({ prefix = "", limit = 1000 } = {}) {
    this.events.push({ op: "list", key: prefix });
    return {
      objects: [...this.data.keys()]
        .filter((key) => key.startsWith(prefix))
        .slice(0, limit)
        .map((key) => ({ key })),
      truncated: false,
    };
  }
}

function seedUser(bucket, user) {
  bucket.seed(accountKey("users", "id", user.id), user);
  bucket.seed(accountKey("users", "username", user.username), user);
  bucket.seed(accountKey("users", "email", user.email), user);
  return user;
}

function userToken(user) {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({
    kind: "user",
    sub: user.id,
    username: user.username,
    email: user.email,
    iat: now,
    exp: now + 3600,
  })).toString("base64url");
  const signature = createHmac("sha256", AUTH_SECRET)
    .update(`portal:account-token:v1:${body}`)
    .digest("base64url");
  return `${body}.${signature}`;
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    AUTH_SECRET,
    CATALOG_URL,
    ALLOWED_ORIGIN: "https://portal.example.invalid",
    ACCOUNT_STORE_MODE: "r2",
  };
}

async function call(bucket, user, path, init = {}) {
  const response = await worker.fetch(new Request(`https://worker.test${path}`, {
    ...init,
    headers: {
      authorization: `Bearer ${userToken(user)}`,
      ...(init.headers || {}),
    },
  }), envFor(bucket), { waitUntil() {} });
  return response;
}

function seedDashboard(bucket, { picks = true } = {}) {
  bucket.seed(FILES_KEY, {
    version: 1,
    updated_at: FIXTURE_TIME,
    data: {
      files: [
        { type: "file", kind: "bbg-show", label: "Daily file", path: "rendered-clips/show/example.mp4", name: "example.mp4" },
        { type: "file", kind: "site-video", label: "站内视频", path: "bilingual_podcast_videos/example.mp4", name: "private.mp4" },
      ],
    },
  });
  if (picks) {
    bucket.seed(PICKS_KEY, {
      version: 1,
      updated_at: FIXTURE_TIME,
      data: { daily_picks: [CATALOG.items[0]], access_options: { institutions: ["NOM"] } },
    });
  }
  bucket.seed("_market-views/items/260802.json", {
    id: "market-view:260802",
    title: "Market Views · 2026-08-02",
    filename: "market_views_260802.pdf",
    size_bytes: 4,
    updated_at: FIXTURE_TIME,
  });
  bucket.seed("_market-views/pdfs/260802.pdf", new Uint8Array([0x25, 0x50, 0x44, 0x46]));
}

test("canonical operator-a receives Daily Picks and private Market Views", async () => {
  const bucket = new MemoryR2({ failFirstGet: PICKS_KEY });
  seedUser(bucket, OPERATOR_A);
  seedDashboard(bucket);

  const summaryResponse = await call(bucket, OPERATOR_A, "/account-admin/summary?refresh=1");
  assert.equal(summaryResponse.status, 200);
  const summary = await summaryResponse.json();
  assert.equal(summary.user.role, "operator");
  assert.equal(summary.dashboard_title, "运营后台");
  assert.equal(summary.daily_picks.length, 1, "a transient snapshot read must not empty Daily Picks");
  assert.equal(summary.files.length, 1, "operator keeps operational files but not site-only videos");
  assert.equal(summary.can_view_users, false);
  assert.equal(summary.can_view_wechat, false);
  assert.equal(summary.can_view_analytics, false);
  assert.deepEqual(summary.users, []);
  assert.equal(summary.wechat_schedule, null);
  assert.equal(summary.analytics, null);
  assert.equal(summary.access_options, null);

  const listResponse = await call(bucket, OPERATOR_A, "/market-views");
  assert.equal(listResponse.status, 200);
  const list = await listResponse.json();
  assert.equal(list.items.length, 1);
  assert.equal(list.items[0].id, "market-view:260802");

  const accessResponse = await call(bucket, OPERATOR_A, "/market-views/access");
  assert.equal(accessResponse.status, 200);
  const access = await accessResponse.json();
  assert.equal(access.user.role, "operator");
  assert.equal(access.can_download, true);

  const pdfResponse = await call(bucket, OPERATOR_A, "/market-views/pdf?id=market-view:260802");
  assert.equal(pdfResponse.status, 200);
  assert.equal(pdfResponse.headers.get("content-type"), "application/pdf");
  assert.equal((await pdfResponse.arrayBuffer()).byteLength, 4);
});

test("operator self-heals only the lightweight picks snapshot when caches are absent", async () => {
  const bucket = new MemoryR2();
  seedUser(bucket, OPERATOR_A);
  seedDashboard(bucket, { picks: false });

  const response = await call(bucket, OPERATOR_A, "/account-admin/summary?refresh=1");
  assert.equal(response.status, 200);
  const summary = await response.json();
  assert.equal(summary.daily_picks.length, 5);
  const snapshotWrites = bucket.events
    .filter((event) => event.op === "put" && event.key.startsWith(`${SNAPSHOT_PREFIX}/`))
    .map((event) => event.key);
  assert.deepEqual(snapshotWrites, [PICKS_KEY], "operator must not start files/users/wechat/analytics refreshes");
});

test("partial privileged identities never become operators", async () => {
  for (const user of [
    { ...OPERATOR_A, id: "wrong-email", email: "other@example.com" },
    { ...OPERATOR_A, id: "wrong-username", username: "other" },
  ]) {
    const bucket = new MemoryR2();
    seedUser(bucket, user);
    const response = await call(bucket, user, "/market-views/access");
    assert.equal(response.status, 200);
    const body = await response.json();
    assert.equal(body.user.role, "user");
    assert.equal(body.can_download, false);
  }
});

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
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

test("operator modal renders Daily Picks and Market Views while super-only sections stay hidden", async () => {
  const markup = vm.runInNewContext(`(${extractFunction(app, "accountAdminModalMarkup")})`, {
    escapeHtml(value) { return String(value || ""); },
  })({
    title: "运营后台",
    showWechat: false,
    showUsers: false,
    showAnalytics: false,
    showHotReports: false,
  });
  assert.match(markup, /<strong>每日精选<\/strong>/u);
  assert.match(markup, /id="accountAdminMarketViewsSection"/u);
  assert.match(markup, /id="accountAdminMarketViewsMore"[^>]*aria-haspopup="dialog"[^>]*hidden/u);
  assert.doesNotMatch(markup, /id="accountAdminMarketViewsSection"[^>]*hidden/u);
  for (const section of ["accountAdminWechatSection", "accountAdminHotReportsSection", "accountAdminAnalyticsSection", "accountAdminUsersSection"]) {
    assert.match(markup, new RegExp(`id="${section}"[^>]*hidden`, "u"));
  }

  const requested = [];
  const sandbox = {
    accountAdminMarketViews: new Map(),
    fetch: async (url) => {
      requested.push(String(url));
      return new Response(JSON.stringify({ items: [{
        id: "market-view:260802",
        title: "Market Views · 2026-08-02",
        filename: "market_views_260802.pdf",
        date: "2026-08-02",
        size_bytes: 2048,
      }] }), { status: 200, headers: { "content-type": "application/json" } });
    },
    escapeHtml(value) { return String(value || ""); },
    formatSize(value) { return `${value} bytes`; },
  };
  vm.runInNewContext(`
    ${extractFunction(app, "adminItemDateTimestamp")}
    ${extractFunction(app, "adminDatedItemsNewestFirst")}
    ${extractFunction(app, "adminCollectionPreview")}
    ${extractFunction(app, "adminMarketViewRow")}
    ${extractFunction(app, "loadAccountAdminMarketViews")}
  `, sandbox);
  const targets = {
    marketViewCount: { textContent: "" },
    marketViews: { innerHTML: "" },
    marketViewsMore: { hidden: true },
    marketViewsNotice: { hidden: true, textContent: "", className: "" },
  };
  const rows = await sandbox.loadAccountAdminMarketViews("/api", targets);
  assert.equal(rows.length, 1);
  assert.deepEqual(requested, ["/api/market-views"]);
  assert.equal(targets.marketViewCount.textContent, "1 PDFs");
  assert.equal(targets.marketViewsMore.hidden, true);
  assert.match(targets.marketViews.innerHTML, /Market Views · 2026-08-02/u);
  assert.match(targets.marketViews.innerHTML, /account-admin-market-view-download/u);
});
