import assert from "node:assert/strict";
import path from "node:path";
import test from "node:test";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const { default: worker } = await import(path.join(root, "workers/portal-suite-worker/src/index.js"));
const restrictedCourseMarkers = [
  ["W", "SP"],
  ["W", "SO"],
  ["股", "道场"],
  ["并", "购圈"],
  ["Fundamental", " Edge"],
  ["Wall Street", " Prep"],
  ["Wall Street", " Oasis"],
  ["Breaking", " into VC"],
  ["Breaking", "_into_VC"],
  ["Breaking Into", " Wallstreet"],
  ["BI", "WS"],
  ["梧桐", "课堂"],
  ["职", "未来"],
  ["和", "君"],
  ["青年", "金融家"],
  ["i", "banker"],
  ["优", "塾"],
  ["万法", "通"],
  ["法", "询"],
  ["基小", "律"],
  ["林立", "军"],
  ["肖", "星"],
  ["清", "华"],
  ["Wi", "nd"],
  ["Bloom", "berg"],
  ["罗兰", "贝格"],
  ["埃森", "哲"],
  ["MS", " Training"],
  ["101", " primer"],
].map((parts) => parts.join(""));

class MemoryR2 {
  constructor() {
    this.rows = new Map();
    this.version = 0;
    this.jsonReadKeys = [];
    this.textReadKeys = [];
    this.rangeReadKeys = [];
    this.textOnlyKeys = new Set();
    this.failPutPrefixOnce = "";
    this.failGetAfterPutExact = "";
    this.failNextGetExact = "";
  }

  seed(key, value) {
    this.version += 1;
    this.rows.set(key, { value: typeof value === "string" ? value : JSON.stringify(value), etag: `v${this.version}` });
  }

  seedBytes(key, value) {
    this.version += 1;
    this.rows.set(key, { value: new Uint8Array(value), etag: `v${this.version}`, binary: true });
  }

  async get(key, options = {}) {
    if (this.failNextGetExact && key === this.failNextGetExact) {
      this.failNextGetExact = "";
      throw new Error("injected R2 read failure");
    }
    const row = this.rows.get(key);
    if (!row) return null;
    const range = options && options.range;
  const rangedValue = range && Number.isInteger(range.offset) && Number.isInteger(range.length)
      ? (row.binary ? row.value : new TextEncoder().encode(row.value)).slice(range.offset, range.offset + range.length)
      : null;
    if (range) this.rangeReadKeys.push(key);
    if (range && (!Number.isInteger(range.offset) || !Number.isInteger(range.length)
      || range.offset < 0 || range.length < 0
      || rangedValue.byteLength !== range.length)) return null;
    if (row.binary) {
      const value = rangedValue || row.value;
      return {
        etag: row.etag,
        body: value,
        size: value.byteLength,
        async arrayBuffer() { return value.buffer.slice(value.byteOffset, value.byteOffset + value.byteLength); },
        async text() { return new TextDecoder().decode(value); },
      };
    }
    const bucket = this;
    const object = {
      etag: row.etag,
      body: new TextEncoder().encode(row.value),
      size: new TextEncoder().encode(row.value).byteLength,
      async text() {
        bucket.textReadKeys.push(key);
        return row.value;
      },
    };
    if (!this.textOnlyKeys.has(key)) {
      object.json = async () => {
        bucket.jsonReadKeys.push(key);
        return JSON.parse(row.value);
      };
    }
    return object;
  }

  async put(key, value, options = {}) {
    if (this.failPutPrefixOnce && key.startsWith(this.failPutPrefixOnce)) {
      this.failPutPrefixOnce = "";
      throw new Error("injected R2 write failure");
    }
    const current = this.rows.get(key);
    const onlyIf = options.onlyIf || {};
    if (onlyIf.etagMatches && (!current || current.etag !== onlyIf.etagMatches)) return null;
    if (onlyIf.etagDoesNotMatch === "*" && current) return null;
    this.version += 1;
    const text = value instanceof Uint8Array ? new TextDecoder().decode(value) : String(value);
    const row = { value: text, etag: `v${this.version}` };
    this.rows.set(key, row);
    if (this.failGetAfterPutExact && key === this.failGetAfterPutExact) {
      this.failNextGetExact = key;
      this.failGetAfterPutExact = "";
    }
    return { etag: row.etag };
  }
}

async function directLookupFixture(items, tokenPostings, options = {}) {
  const bucketCount = options.bucketCount || 64;
  const prefix = options.prefix || "_report-chat/v2/releases/test";
  const buildPart = async (entries, name) => {
    const buckets = Array.from({ length: bucketCount }, () => []);
    for (const [key, value] of entries) {
      const digest = new Uint8Array(await crypto.subtle.digest("SHA-256", new TextEncoder().encode(key)));
      const bucket = Number(new DataView(digest.buffer).getBigUint64(0, false) % BigInt(bucketCount));
      buckets[bucket].push([key, value]);
    }
    const table = new Uint8Array(bucketCount * 12);
    const chunks = [];
    let offset = 0;
    for (let bucket = 0; bucket < bucketCount; bucket += 1) {
      const entriesInBucket = buckets[bucket].sort((left, right) => left[0].localeCompare(right[0]));
      if (!entriesInBucket.length) continue;
      const bytes = new TextEncoder().encode(JSON.stringify(entriesInBucket));
      const view = new DataView(table.buffer, bucket * 12, 12);
      view.setBigUint64(0, BigInt(offset), false);
      view.setUint32(8, bytes.byteLength, false);
      chunks.push(bytes);
      offset += bytes.byteLength;
    }
    const data = new Uint8Array(offset);
    let cursor = 0;
    for (const chunk of chunks) {
      data.set(chunk, cursor);
      cursor += chunk.byteLength;
    }
    return {
      table,
      data,
      manifest: {
        table_key: `${prefix}/${name}.tbl`,
        data_key: `${prefix}/${name}.dat`,
        bucket_count: bucketCount,
        slot_size: 12,
        data_bytes: data.byteLength,
      },
    };
  };
  const tokenPart = await buildPart(Object.entries(tokenPostings), "tokens");
  const itemPart = await buildPart(items.map((item) => [item.id, item]), "items");
  return { tokenPart, itemPart };
}

async function seedReportChatLookup(bucket, items, tokenPostings, defaults = items.slice(0, 12)) {
  const { tokenPart, itemPart } = await directLookupFixture(items, tokenPostings);
  bucket.seedBytes(tokenPart.manifest.table_key, tokenPart.table);
  bucket.seedBytes(tokenPart.manifest.data_key, tokenPart.data);
  bucket.seedBytes(itemPart.manifest.table_key, itemPart.table);
  bucket.seedBytes(itemPart.manifest.data_key, itemPart.data);
  bucket.seed("_report-chat/v2/manifest.json", {
    schema_version: 2,
    index_kind: "report-chat-random-access",
    hash: "sha256-first8-be",
    token_table: tokenPart.manifest,
    item_table: itemPart.manifest,
    default_items: defaults,
  });
}

async function seedCourseChatLookup(bucket, items, tokenPostings, defaults = items.slice(0, 12)) {
  const prefix = "_course-directory/v2/chat-lookup/test";
  const { tokenPart, itemPart } = await directLookupFixture(items, tokenPostings, { prefix });
  bucket.seedBytes(tokenPart.manifest.table_key, tokenPart.table);
  bucket.seedBytes(tokenPart.manifest.data_key, tokenPart.data);
  bucket.seedBytes(itemPart.manifest.table_key, itemPart.table);
  bucket.seedBytes(itemPart.manifest.data_key, itemPart.data);
  bucket.seed("_course-directory/v2/chat-lookup/manifest.json", {
    schema_version: 2,
    format: "course-chat-direct-bucket-v2",
    token_index: { ...tokenPart.manifest, hash: "sha256-first64-be-mod" },
    item_index: { ...itemPart.manifest, hash: "sha256-first64-be-mod" },
    default_items: defaults,
  });
}

function envFor(bucket) {
  return {
    REPORT_BUCKET: bucket,
    ACCOUNT_STORE_MODE: "r2",
    MASTER_KEY: "test-master-key",
    PASSWORD_SECRET: "test-password-secret",
    CATALOG_URL: "https://static.example.invalid/catalog.json",
    STATIC_DATA_PREFIX: "edge-static/runtime-data",
    ALLOWED_ORIGIN: "https://portal.example.invalid",
    COURSE_DIRECTORY_REDACT_TERMS: restrictedCourseMarkers.join("\n"),
  };
}

async function jsonRequest(env, pathName, options = {}) {
  const response = await worker.fetch(new Request(`https://worker.test${pathName}`, options), env, { waitUntil() {} });
  const data = await response.json().catch(() => ({}));
  return { response, data };
}

async function register(env) {
  const captcha = await jsonRequest(env, "/captcha");
  assert.equal(captcha.response.status, 200);
  const svg = Buffer.from(String(captcha.data.image).split(",", 2)[1], "base64").toString("utf8");
  const equation = svg.match(/>(\d+) \+ (\d+) = \?</u);
  assert.ok(equation, "captcha equation must be readable in the fixture");
  const answer = String(Number(equation[1]) + Number(equation[2]));
  const auth = await jsonRequest(env, "/auth", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({
      action: "register",
      username: "reward-reader",
      email: "reward-reader@example.com",
      password: "test-pass-123",
      captcha_token: captcha.data.token,
      captcha_answer: answer,
    }),
  });
  assert.equal(auth.response.status, 201);
  assert.ok(auth.data.token);
  return auth.data.token;
}

function bearer(token) {
  return { Authorization: `Bearer ${token}` };
}

test("daily check-in is idempotent and grants exactly one catalog report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);

  const initial = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(initial.response.status, 200);
  assert.equal(initial.data.points, 0);
  assert.equal(initial.data.checked_in_today, false);

  const checkedIn = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(checkedIn.response.status, 200);
  assert.equal(checkedIn.data.points, 10);
  assert.equal(checkedIn.data.current_streak, 1);
  assert.equal(checkedIn.data.daily_available, true);

  const duplicateCheckin = await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  assert.equal(duplicateCheckin.response.status, 200);
  assert.equal(duplicateCheckin.data.points, 10, "duplicate check-ins must not add points");

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);
  assert.equal(claimed.data.rewards.daily_claimed, true);

  const accessA = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessA.response.status, 200);
  assert.equal(accessA.data.can_download, true, "the reward must use the existing purchase entitlement path");

  const secondDaily = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(secondDaily.response.status, 200);
  assert.equal(secondDaily.data.claimed, false);
  assert.equal(secondDaily.data.already_claimed_today, true);

  const accessB = await jsonRequest(env, `/entitlement?report_id=${reportB}&source=catalog`, { headers: bearer(token) });
  assert.equal(accessB.response.status, 200);
  assert.equal(accessB.data.can_download, false);

  const insufficient = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "points", report_id: reportB }),
  });
  assert.equal(insufficient.response.status, 409);
  assert.match(insufficient.data.detail, /积分不足/u);
});

test("failed purchase mirroring still grants exactly one report from reward state", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report C", filename: "c.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_available, false);
  assert.equal(status.data.daily_claimed, true);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true, "the atomic reward grant is authoritative when the mirror is unavailable");
});

test("concurrent daily claims grant at most one report", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report D", filename: "d.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report E", filename: "e.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  const [left, right] = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  })));
  assert.deepEqual([left, right].map(({ data }) => Boolean(data.claimed)).sort(), [false, true]);
  const access = await Promise.all([reportA, reportB].map((reportId) => jsonRequest(
    env,
    `/entitlement?report_id=${reportId}&source=catalog`,
    { headers: bearer(token) },
  )));
  assert.equal(access.filter(({ data }) => data.can_download).length, 1);
});

test("a committed reward never depends on a purchase readback", async () => {
  const bucket = new MemoryR2();
  const reportA = "aaaaaaaaaaaaaaaaaaaaaaaa";
  const reportB = "bbbbbbbbbbbbbbbbbbbbbbbb";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [
      { id: reportA, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportA}.pdf` },
      { id: reportB, title: "Report B", filename: "b.pdf", available: true, r2_key: `reports/${reportB}.pdf` },
    ],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failGetAfterPutExact = `_account/purchases/catalog/${reportA}/${encodeURIComponent("reward-reader@example.com")}`;

  const claimed = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportA }),
  });
  assert.equal(claimed.response.status, 200, JSON.stringify(claimed.data));
  assert.equal(claimed.data.claimed, true);

  const duplicate = await jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportB }),
  });
  assert.equal(duplicate.response.status, 200);
  assert.equal(duplicate.data.claimed, false);
  assert.equal(duplicate.data.already_claimed_today, true);

  const access = await jsonRequest(env, `/entitlement?report_id=${reportA}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.response.status, 200);
  assert.equal(access.data.can_download, true);
  assert.equal(access.data.reward_access_matched, true);
  assert.ok(bucket.failNextGetExact, "purchase readback should remain untouched because reward state authorizes directly");
});

test("same-report retry cannot restore a consumed daily slot when purchase mirroring fails", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  bucket.seed("edge-static/runtime-data/catalog.json", {
    items: [{ id: reportId, title: "Report A", filename: "a.pdf", available: true, r2_key: `reports/${reportId}.pdf` }],
  });
  const env = envFor(bucket);
  const token = await register(env);
  await jsonRequest(env, "/rewards", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: "{}",
  });
  bucket.failPutPrefixOnce = "_account/purchases/";
  const requests = [1, 2].map(() => jsonRequest(env, "/rewards/claim", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ reward_kind: "daily", report_id: reportId }),
  }));
  const results = await Promise.all(requests);
  assert.ok(results.every(({ response }) => response.status === 200));
  assert.equal(results.filter(({ data }) => data.claimed).length, 1);
  const status = await jsonRequest(env, "/rewards", { headers: bearer(token) });
  assert.equal(status.data.daily_claimed, true);
  assert.equal(status.data.daily_available, false);
  const access = await jsonRequest(env, `/entitlement?report_id=${reportId}&source=catalog`, { headers: bearer(token) });
  assert.equal(access.data.can_download, true);
});

test("course API enforces at least 30 remaining days on the server", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const env = envFor(bucket);

  const anonymous = await jsonRequest(env, "/course/access");
  assert.equal(anonymous.response.status, 401);
  assert.equal(Object.hasOwn(anonymous.data, "courses"), false);
  assert.equal(Object.hasOwn(anonymous.data, "course_catalog"), false);

  const token = await register(env);
  const email = "reward-reader@example.com";
  const entitlementKey = `_account/entitlements/${encodeURIComponent(email)}`;

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const allowed = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(allowed.response.status, 200);
  assert.equal(allowed.data.can_access, true);
  assert.equal(allowed.data.courses.length, 43);
  assert.equal(allowed.data.course_catalog.length, 43);
  assert.deepEqual(
    allowed.data.courses,
    allowed.data.course_catalog.map((course) => course.title),
    "the legacy title array must stay compatible with the structured catalog",
  );
  assert.equal(new Set(allowed.data.course_catalog.map((course) => course.id)).size, 43);
  for (const course of allowed.data.course_catalog) {
    assert.deepEqual(Object.keys(course).sort(), ["audience", "category", "id", "summary", "title"]);
    for (const field of ["id", "category", "title", "summary", "audience"]) {
      assert.equal(typeof course[field], "string");
      assert.ok(course[field].trim(), `${field} must be populated`);
    }
  }
  const serializedCatalog = JSON.stringify(allowed.data.course_catalog).toLowerCase();
  for (const marker of restrictedCourseMarkers) {
    assert.equal(serializedCatalog.includes(marker.toLowerCase()), false, `restricted marker leaked: ${marker}`);
  }

  bucket.seed(entitlementKey, {
    id: "entitlement-1",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 29 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const denied = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(denied.response.status, 200);
  assert.equal(denied.data.can_access, false);
  assert.deepEqual(denied.data.courses, []);
  assert.deepEqual(denied.data.course_catalog, []);

  bucket.rows.delete(entitlementKey);
  const accessKey = `_account/access/${encodeURIComponent(email)}`;
  const accessBase = {
    id: "access-1",
    email,
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    duration_value: "1",
    institutions: [],
    industries: [],
    page_ranges: [],
    download_items: [],
    download_limit: 0,
    download_count: 0,
    note: "",
    source: "stored",
  };
  bucket.seed(accessKey, { ...accessBase, access_mode: "filters", institutions: ["NOM"] });
  const filtered = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(filtered.data.can_access, false, "a filtered report grant is not a membership");
  assert.deepEqual(filtered.data.courses, []);
  assert.deepEqual(filtered.data.course_catalog, []);

  bucket.seed(accessKey, {
    ...accessBase,
    access_mode: "all",
    duration_value: "trial_3d",
    download_limit: 10,
  });
  const limited = await jsonRequest(env, "/course/access", { headers: bearer(token) });
  assert.equal(limited.data.can_access, false, "a limited report grant is not a membership");
  assert.deepEqual(limited.data.courses, []);
  assert.deepEqual(limited.data.course_catalog, []);
});

test("course directory stays private, searchable, paginated, and strips storage locators", async () => {
  const bucket = new MemoryR2();
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  const hiddenMarker = restrictedCourseMarkers[0];
  bucket.seed("_course-directory/v1/directory.json", {
    schema_version: 1,
    generated_at: "2026-08-10T12:00:00+08:00",
    items: [
      {
        id: "file-00000001",
        course_id: "cap-03",
        name: "中国证监会 IPO 审核规则与案例",
        folders: ["IPO 上市实务", "监管审核"],
        extension: "pdf",
        size_label: "12.4 MB",
        date: "2026-08-10",
        entities: ["中国证监会", "上交所", "深交所"],
        source_path: "must/not/leave/private/storage",
        object_key: "private-object-key",
        locator: "private-locator",
      },
      {
        id: "file-00000002",
        course_id: "res-02",
        name: "摩根大通全球利率与外汇策略",
        folders: ["全球宏观", "利率与外汇"],
        extension: "pdf",
        size_label: "8.1 MB",
        date: "2026-08-09",
        entities: ["摩根大通", "高盛", "美银", "瑞银"],
      },
      {
        id: "file-00000003",
        course_id: "law-01",
        name: "资本市场尽职调查工作底稿",
        folders: ["非诉项目", "尽职调查"],
        extension: "docx",
        size_label: "980 KB",
        date: "2026-08-08",
        entities: ["金杜", "中伦", "君合", "国浩"],
      },
      {
        id: "file-00000004",
        course_id: "fin-01",
        name: `${hiddenMarker} provider material`,
        folders: ["估值"],
        extension: "xlsx",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000005",
        course_id: "fin-01",
        name: "课程咨询 private.user@example.com",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000006",
        course_id: "fin-01",
        name: "估值案例",
        folders: ["资料 private.example.com"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000007",
        course_id: "fin-01",
        name: "估值案例讲解",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: ["微信 abc123", "13800138000"],
      },
      {
        id: "file-00000008",
        course_id: "fin-01",
        name: "估值资料 private.example.edu",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000009",
        course_id: "fin-01",
        name: "估值资料 ftp : / /private.example.edu",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000010",
        course_id: "fin-01",
        name: "估值资料",
        folders: ["www . private.example.edu"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000011",
        course_id: "fin-01",
        name: "联系abc@example.com资料",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
      {
        id: "file-00000012",
        course_id: "fin-01",
        name: "网址private.example.edu资料",
        folders: ["估值"],
        extension: "pdf",
        size_label: "2 MB",
        date: "2026-08-07",
        entities: [],
      },
    ],
  });
  const env = envFor(bucket);

  const anonymous = await jsonRequest(env, "/course/directory");
  assert.equal(anonymous.response.status, 401);
  assert.equal(Object.hasOwn(anonymous.data, "items"), false);
  assert.equal(Object.hasOwn(anonymous.data, "facets"), false);

  const token = await register(env);
  const email = "reward-reader@example.com";
  const entitlementKey = `_account/entitlements/${encodeURIComponent(email)}`;
  bucket.seed(entitlementKey, {
    id: "entitlement-course-directory",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });

  const redactionTerms = env.COURSE_DIRECTORY_REDACT_TERMS;
  delete env.COURSE_DIRECTORY_REDACT_TERMS;
  const missingRedactionConfig = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(missingRedactionConfig.response.status, 503);
  assert.equal(Object.hasOwn(missingRedactionConfig.data, "items"), false);
  env.COURSE_DIRECTORY_REDACT_TERMS = redactionTerms;

  const firstPage = await jsonRequest(env, "/course/directory?page=1&page_size=2", { headers: bearer(token) });
  assert.equal(firstPage.response.status, 200);
  assert.equal(firstPage.data.total, 3, "records containing redaction markers or private contacts must be omitted");
  assert.equal(firstPage.data.items.length, 2);
  assert.equal(firstPage.data.has_more, true);
  assert.ok(bucket.jsonReadKeys.includes("_course-directory/v1/directory.json"));
  assert.equal(bucket.textReadKeys.includes("_course-directory/v1/directory.json"), false);
  assert.equal(firstPage.response.headers.get("cache-control"), "private, no-store, max-age=0");
  assert.ok(firstPage.data.facets.courses.some((entry) => entry.id === "cap-03" && entry.count === 1));
  assert.ok(firstPage.data.facets.top_entities.some((entry) => entry.name === "中国证监会"));
  const serialized = JSON.stringify(firstPage.data);
  assert.equal(serialized.includes("must/not/leave"), false);
  assert.equal(serialized.includes("private-object-key"), false);
  assert.equal(serialized.includes("private-locator"), false);
  assert.deepEqual(
    Object.keys(firstPage.data.items[0]).sort(),
    ["category", "course_id", "date", "entities", "extension", "folders", "id", "name", "size_label"],
  );

  const institutionSearch = await jsonRequest(
    env,
    `/course/directory?q=${encodeURIComponent("摩根大通 高盛")}&file_type=pdf`,
    { headers: bearer(token) },
  );
  assert.equal(institutionSearch.response.status, 200);
  assert.equal(institutionSearch.data.total, 1);
  assert.equal(institutionSearch.data.items[0].name, "摩根大通全球利率与外汇策略");
  assert.deepEqual(institutionSearch.data.items[0].entities, ["摩根大通", "高盛", "美银", "瑞银"]);

  const lawCourse = await jsonRequest(env, "/course/directory?course_id=law-01&category=%E8%B5%84%E6%9C%AC%E5%B8%82%E5%9C%BA%E6%B3%95%E5%BE%8B", {
    headers: bearer(token),
  });
  assert.equal(lawCourse.data.total, 1);
  assert.equal(lawCourse.data.items[0].extension, "docx");

  bucket.seed(entitlementKey, {
    id: "entitlement-course-directory",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 29 * 24 * 60 * 60 * 1000).toISOString(),
    paddle_last_event_id: "",
    paddle_last_occurred_at: "",
    updated_at: new Date().toISOString(),
  });
  const expiredSoon = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(expiredSoon.response.status, 403);
  assert.equal(Object.hasOwn(expiredSoon.data, "items"), false);
  assert.equal(Object.hasOwn(expiredSoon.data, "facets"), false);
});

test("course directory falls back to text parsing when the R2 body has no json method", async () => {
  const bucket = new MemoryR2();
  const directoryKey = "_course-directory/v1/directory.json";
  bucket.seed("edge-static/runtime-data/catalog.json", { items: [] });
  bucket.seed(directoryKey, {
    schema_version: 1,
    generated_at: "2026-08-10T12:00:00+08:00",
    items: [{
      id: "file-fallback-01",
      course_id: "cap-03",
      name: "交易所上市审核问答",
      folders: ["上市实务"],
      extension: "pdf",
      size_label: "1 MB",
      date: "2026-08-10",
      entities: ["上交所"],
    }],
  });
  bucket.textOnlyKeys.add(directoryKey);
  const env = envFor(bucket);
  const token = await register(env);
  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-directory-fallback",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });
  const response = await jsonRequest(env, "/course/directory", { headers: bearer(token) });
  assert.equal(response.response.status, 200);
  assert.equal(response.data.total, 1);
  assert.ok(bucket.textReadKeys.includes(directoryKey));
  assert.equal(bucket.jsonReadKeys.includes(directoryKey), false);
});

test("registered users can use grounded report chat and anonymous users cannot", async () => {
  const bucket = new MemoryR2();
  const reportId = "aaaaaaaaaaaaaaaaaaaaaaaa";
  await seedReportChatLookup(bucket, [{
      id: reportId,
      title: "JPM-AI data center power constraints-260811",
      title_zh: "摩根大通：AI 数据中心电力瓶颈",
      institution: "摩根大通",
      date_folder: "260811",
      page_count: 28,
      available: true,
      attraction_score: 5,
    }], { ai: [reportId], 数据中心: [reportId], 电力: [reportId] });
  const env = envFor(bucket);
  const anonymous = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json" },
    body: JSON.stringify({ question: "AI 数据中心电力瓶颈" }),
  });
  assert.equal(anonymous.response.status, 401);
  const token = await register(env);
  const oversized = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI".repeat(9000) }),
  });
  assert.equal(oversized.response.status, 413);
  const result = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "找最近半年AI数据中心电力瓶颈相关的顶级投行报告" }),
  });
  assert.equal(result.response.status, 200, JSON.stringify(result.data));
  assert.equal(result.data.recommendations[0].id, reportId);
  assert.equal(result.data.recommendations[0].attraction_score, 5);
  assert.match(result.data.answer, /摩根大通/u);
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("tokens.tbl")));
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("items.tbl")));
  assert.equal(bucket.jsonReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
  assert.equal(bucket.jsonReadKeys.includes("edge-static/runtime-data/search_index.json"), false);
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/search_index.json"), false);
  assert.equal(Object.hasOwn(result.data.recommendations[0], "excerpt"), false);
  assert.equal(result.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("report chat retrieves from random-access lookup before enforcing the Beijing-day limit", async () => {
  const bucket = new MemoryR2();
  await seedReportChatLookup(bucket, [{ id: "limit-test-report", title: "Limit Test", attraction_score: 2 }], { ai: ["limit-test-report"] });
  const env = envFor(bucket);
  const token = await register(env);
  const date = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
  bucket.seed(`_account/report-chat-v2/${encodeURIComponent("reward-reader@example.com")}/${date}`, {
    email: "reward-reader@example.com",
    date,
    count: 30,
    updated_at: new Date().toISOString(),
  });
  bucket.textReadKeys.length = 0;
  const limited = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心" }),
  });
  assert.equal(limited.response.status, 429);
  assert.equal(limited.data.stage_code, "DAILY_LIMIT");
  assert.match(limited.data.request_hint, /^[A-Z0-9]{10}$/u);
  assert.ok(bucket.rangeReadKeys.some((key) => key.endsWith("tokens.tbl")));
  assert.equal(bucket.textReadKeys.includes("edge-static/runtime-data/catalog.json"), false);
});

test("report chat lookup failures return actionable private JSON and do not consume a turn", async () => {
  const bucket = new MemoryR2();
  const env = envFor(bucket);
  const token = await register(env);
  const date = new Intl.DateTimeFormat("en-CA", {
    timeZone: "Asia/Shanghai",
    year: "numeric",
    month: "2-digit",
    day: "2-digit",
  }).format(new Date());
  const usageKey = `_account/report-chat-v2/${encodeURIComponent("reward-reader@example.com")}/${date}`;
  const failed = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心" }),
  });
  assert.equal(failed.response.status, 503);
  assert.equal(failed.data.stage_code, "LOOKUP_MANIFEST");
  assert.match(failed.data.request_hint, /^[A-Z0-9]{10}$/u);
  assert.equal(bucket.rows.has(usageKey), false);
  assert.equal(failed.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("report chat random-access retrieval stays within the Worker subrequest budget", async () => {
  const bucket = new MemoryR2();
  const items = Array.from({ length: 20 }, (_, index) => ({
    id: `budget-report-${String(index).padStart(2, "0")}`,
    title: `AI data center report ${index}`,
    institution: index === 0 ? "摩根大通" : "Research",
    attraction_score: index === 0 ? 5 : 2,
  }));
  const ids = items.map((item) => item.id);
  await seedReportChatLookup(bucket, items, {
    ai: ids,
    数据中心: ids,
    数据: ids,
    中心: ids,
    电力: ids,
    瓶颈: ids,
    资本: ids,
    开支: ids,
  });
  const env = envFor(bucket);
  const token = await register(env);
  bucket.rangeReadKeys.length = 0;
  const result = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ question: "AI 数据中心 电力瓶颈 资本开支" }),
  });
  assert.equal(result.response.status, 200, JSON.stringify(result.data));
  assert.ok(result.data.recommendations.length <= 8);
  assert.ok(bucket.rangeReadKeys.length <= 32, `unexpected lookup range reads: ${bucket.rangeReadKeys.length}`);
});

test("course chat uses the compact private recommendation index, enforces membership, and returns no locators", async () => {
  const bucket = new MemoryR2();
  await seedCourseChatLookup(bucket, [{
      id: "file-course-chat-01",
      course_id: "fin-01",
      name: "摩根大通投行估值与建模案例",
      folders: ["投行面试", "估值建模"],
      extension: "xlsx",
      size_label: "4.2 MB",
      date: "2026-08-12",
      entities: ["摩根大通", "高盛"],
      source_path: "/private/course/source/file.xlsx",
      object_key: "private-course-object",
    }], { 摩根大通: ["file-course-chat-01"], 投行: ["file-course-chat-01"], 建模: ["file-course-chat-01"] });
  const env = envFor(bucket);
  const token = await register(env);
  const denied = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ context: "course", question: "摩根大通 投行 建模" }),
  });
  assert.equal(denied.response.status, 403);
  assert.equal(Object.hasOwn(denied.data, "recommendations"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v2/chat-lookup/manifest.json"), false);

  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-chat",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });
  bucket.jsonReadKeys.length = 0;
  const allowed = await jsonRequest(env, "/report-chat", {
    method: "POST",
    headers: { "content-type": "application/json", ...bearer(token) },
    body: JSON.stringify({ context: "course", question: "摩根大通 投行 建模" }),
  });
  assert.equal(allowed.response.status, 200, JSON.stringify(allowed.data));
  assert.equal(allowed.data.recommendations[0].id, "file-course-chat-01");
  assert.equal(allowed.data.recommendations[0].kind, "course");
  assert.equal(allowed.data.recommendations[0].attraction_score, 5);
  assert.equal(allowed.data.recommendations[0].title, "摩根大通投行估值与建模案例");
  assert.equal(allowed.data.recommendations[0].course_title, "财务建模与企业估值");
  assert.equal(allowed.data.recommendations[0].category, "金融建模");
  assert.equal(allowed.data.recommendations[0].file_type, "spreadsheet");
  const serialized = JSON.stringify(allowed.data);
  assert.equal(serialized.includes("/private/course"), false);
  assert.equal(serialized.includes("private-course-object"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v2/chat-lookup/manifest.json"), true);
  assert.equal(bucket.jsonReadKeys.includes("_course-directory/v1/chat-index.json"), false);
  assert.equal(bucket.textReadKeys.includes("_course-directory/v1/chat-index.json"), false);
  assert.equal(bucket.jsonReadKeys.includes("_course-directory/v1/directory.json"), false);
  assert.equal(allowed.response.headers.get("cache-control"), "private, no-store, max-age=0");
});

test("course chat falls back to grounded recommendations when DeepSeek is unavailable", async () => {
  const bucket = new MemoryR2();
  await seedCourseChatLookup(bucket, [{
      id: "file-course-chat-fallback-01",
      course_id: "fin-01",
      name: "高盛并购估值建模案例",
      folders: ["并购", "估值建模"],
      extension: "xlsx",
      size_label: "3.8 MB",
      date: "2026-08-12",
      entities: ["高盛"],
    }], { 高盛: ["file-course-chat-fallback-01"], 并购: ["file-course-chat-fallback-01"], 估值: ["file-course-chat-fallback-01"] });
  const env = { ...envFor(bucket), DEEPSEEK_API_KEY: "configured-test-key" };
  const token = await register(env);
  const email = "reward-reader@example.com";
  bucket.seed(`_account/entitlements/${encodeURIComponent(email)}`, {
    id: "entitlement-course-chat-fallback",
    email,
    plan: "annual",
    status: "active",
    lifetime: false,
    current_period_end: new Date(Date.now() + 31 * 24 * 60 * 60 * 1000).toISOString(),
    updated_at: new Date().toISOString(),
  });

  const originalFetch = globalThis.fetch;
  globalThis.fetch = async (input) => {
    assert.match(String(input), /^https:\/\/api\.deepseek\.com\/chat\/completions$/u);
    throw new Error("injected DeepSeek transport failure");
  };
  try {
    const result = await jsonRequest(env, "/report-chat", {
      method: "POST",
      headers: { "content-type": "application/json", ...bearer(token) },
      body: JSON.stringify({ context: "course", question: "高盛 并购 估值建模" }),
    });
    assert.equal(result.response.status, 200, JSON.stringify(result.data));
    assert.match(result.data.answer, /高盛并购估值建模案例/u);
    assert.equal(result.data.recommendations[0].id, "file-course-chat-fallback-01");
    assert.equal(result.data.recommendations[0].attraction_score, 5);
  } finally {
    globalThis.fetch = originalFetch;
  }
});

test("chart gallery exposes only opaque image ids and streams immutable images", async () => {
  const bucket = new MemoryR2();
  const imageId = "b".repeat(64);
  bucket.seed("_chart-search/v1/index.json", {
    schema_version: 1,
    updated_at_bjt: "2026-08-12T10:00:00+08:00",
    reports: [{
      report_id: "aaaaaaaaaaaaaaaaaaaaaaaa",
      title: "摩根大通 AI 数据中心报告",
      date_folder: "260812",
      charts: [{
        id: "chart-1",
        analysis_version: "chart-search-v2",
        image_id: imageId,
        title: "数据中心电力需求",
        content_kind: "chart",
        quality_score: 96,
        chart_type: "line",
        description: "2025-2030 年电力需求持续增长。",
        trend_summary: "上升",
        metrics: ["电力需求"],
        entities: ["摩根大通"],
        periods: ["2025-2030"],
        geographies: ["美国"],
        units: ["GW"],
        keywords: ["AI"],
        private_path: "/must/not/leak.jpg",
      }, {
        id: "legacy-chart",
        image_id: "c".repeat(64),
        title: "旧版未严格复核图片",
        chart_type: "other",
        description: "不应进入图表库。",
        entities: ["AI"],
      }],
    }],
  });
  bucket.seedBytes(`_chart-search/v1/images/${imageId}.jpg`, [255, 216, 255, 217]);
  const env = envFor(bucket);
  const gallery = await jsonRequest(env, "/charts?q=AI");
  assert.equal(gallery.response.status, 200);
  assert.equal(gallery.data.total, 1);
  assert.equal(gallery.data.items[0].image_id, imageId);
  assert.equal(Object.hasOwn(gallery.data.items[0], "private_path"), false);
  const image = await worker.fetch(new Request(`https://worker.test/charts/image?id=${imageId}`), env, { waitUntil() {} });
  assert.equal(image.status, 200);
  assert.equal(image.headers.get("content-type"), "image/jpeg");
  assert.match(image.headers.get("cache-control"), /immutable/u);
  const invalid = await jsonRequest(env, "/charts/image?id=../../private");
  assert.equal(invalid.response.status, 400);
});

test("restricted course catalog and contact are absent from the unauthenticated static page", async () => {
  const { readFile } = await import("node:fs/promises");
  const html = await readFile(path.join(root, "portal_suite/site_src/courses.html"), "utf8");
  const loweredHtml = html.toLowerCase();
  for (const marker of restrictedCourseMarkers) {
    assert.equal(loweredHtml.includes(marker.toLowerCase()), false, `restricted marker leaked: ${marker}`);
  }
  assert.doesNotMatch(html, /Support Contact|support@portal\.example\.invalid|mailto:/u);
  assert.match(html, /id="courseCatalog"[^>]*hidden/u);
});

test("course frontend renders the complete structured catalog with topic filters", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  const chatSource = await readFile(path.join(root, "portal_suite/site_src/assets/report-chat.js"), "utf8");
  const styles = await readFile(path.join(root, "portal_suite/site_src/assets/styles.css"), "utf8");
  assert.match(source, /data\.course_catalog/u);
  assert.match(source, /courseSearchInput/u);
  assert.match(source, /courseCategoryFilter/u);
  assert.match(source, /escapeHtml\(product\.title\)/u);
  assert.match(source, /escapeHtml\(product\.summary\)/u);
  assert.match(source, /escapeHtml\(product\.audience\)/u);
  assert.doesNotMatch(source, /filter\(Boolean\)\.slice\(0, 12\)/u);
  assert.match(styles, /\.course-grid\s*\{[\s\S]*?grid-template-columns:\s*repeat\(3,/u);
  assert.match(styles, /\.course-card\[hidden\]\s*\{[\s\S]*?display:\s*none/u);
  assert.match(chatSource, /context:\s*"course"/u);
  assert.match(chatSource, /data-course-query/u);
  assert.match(chatSource, /courseDirectorySearch/u);
  assert.match(chatSource, /AbortController/u);
  assert.match(chatSource, /HTTP \$\{response\.status\}/u);
  assert.match(chatSource, /stage_code/u);
  assert.match(chatSource, /请求超过 20 秒/u);
});

test("frontend distinguishes an already-used daily reward from a successful claim", async () => {
  const { readFile } = await import("node:fs/promises");
  const source = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
  assert.match(source, /if \(data\.already_claimed_today\)/u);
  assert.match(source, /if \(!data\.claimed\) throw new Error/u);
  const duplicateBranch = source.slice(
    source.indexOf("if (data.already_claimed_today)"),
    source.indexOf("if (data.already_owned)"),
  );
  assert.doesNotMatch(duplicateBranch, /portal-reward-change|status:\s*"success"/u);
});
