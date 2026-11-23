import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
const settingsKey = "_newsfeed/settings/reader%40example.com.json";
const originalSettings = {
  user_key: "reader%40example.com", digest_email: "reader@example.com",
  digest_email_enabled: true, newsletter_topic_id: "tech", digest_timezone: "UTC",
  digest_send_time: "14:20", digest_language: "en", digest_last_sent_date: "",
};

function functionSource(name) {
  const start = source.indexOf(`async function ${name}(`);
  assert.notEqual(start, -1);
  const next = source.slice(start + 1).search(/\n(?:async )?function \w+\(/u);
  assert.notEqual(next, -1);
  return source.slice(start, start + 1 + next).trim();
}

function memoryBucket(initial = originalSettings) {
  let stored = initial ? structuredClone(initial) : null;
  let version = 1;
  const bucket = {
    writes: [], beforeWrite: null,
    value() { return structuredClone(stored); },
    update(value) { stored = structuredClone(value); version += 1; },
    async get(key) {
      assert.equal(key, settingsKey);
      if (!stored) return null;
      const text = JSON.stringify(stored);
      return { etag: `v${version}`, async text() { return text; } };
    },
    async put(key, value, options) {
      assert.equal(key, settingsKey);
      bucket.writes.push(options);
      if (bucket.beforeWrite) await bucket.beforeWrite(bucket);
      if (!stored || options.onlyIf.etagMatches !== `v${version}`) return null;
      bucket.update(JSON.parse(value));
      return { etag: `v${version}` };
    },
  };
  return bucket;
}

function harness(overrides = {}) {
  const emails = [];
  const errors = [];
  const context = {
    NEWSFEED_SETTINGS_PREFIX: "_newsfeed/settings",
    normalizeEmail: (value) => String(value || "").trim().toLowerCase(),
    accountBucket: (env) => env.REPORT_BUCKET,
    fetchNewsfeedDigestPayload: async () => ({ headlines: [{ title: "Fresh report", url: "https://example.com/report" }] }),
    sendNewsfeedEmail: async (_env, message) => { emails.push(message); return { sent: true, messageId: "accepted-1" }; },
    newsfeedEmailSubject: () => "Daily brief",
    newsfeedEmailHtml: () => "<p>Daily brief</p>",
    newsfeedEmailText: () => "Daily brief",
    console: { error(message) { errors.push(message); } },
    ...overrides,
  };
  vm.runInNewContext([
    functionSource("r2GetJsonObjectStrict"),
    functionSource("attemptNewsfeedDigestEmail"),
    functionSource("recordNewsfeedEmailAttempt"),
    "this.api = { attemptNewsfeedDigestEmail, recordNewsfeedEmailAttempt };",
  ].join("\n"), context);
  return { api: context.api, emails, errors };
}

test("empty or missing digest stories never call the email provider", async () => {
  for (const payload of [null, {}, { headlines: [] }]) {
    const { api, emails } = harness({ fetchNewsfeedDigestPayload: async () => payload });
    const { result } = await api.attemptNewsfeedDigestEmail({}, originalSettings, { dateKey: "2026-11-23" });
    assert.equal(result.sent, false);
    assert.equal(result.code, "NEWSFEED_CONTENT_EMPTY");
    assert.equal(emails.length, 0);
  }
});

test("nonempty digest uses the account recipient and reports provider acceptance", async () => {
  const { api, emails } = harness();
  const { result } = await api.attemptNewsfeedDigestEmail({}, originalSettings, { dateKey: "2026-11-23" });
  assert.equal(result.sent, true);
  assert.equal(emails.length, 1);
  assert.equal(emails[0].to, originalSettings.digest_email);
});

test("recording delivery preserves a subscription disabled or edited during sending", async () => {
  const bucket = memoryBucket({ ...originalSettings, digest_email_enabled: false, newsletter_topic_id: "", digest_timezone: "Asia/Shanghai", digest_language: "zh-CN" });
  const { api } = harness();
  const result = await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(result.digest_state_saved, true);
  assert.equal(bucket.value().digest_email_enabled, false);
  assert.equal(bucket.value().newsletter_topic_id, "");
  assert.equal(bucket.value().digest_timezone, "Asia/Shanghai");
  assert.equal(bucket.value().digest_language, "zh-CN");
  assert.equal(bucket.value().digest_last_sent_date, "2026-11-23");
  assert.equal(bucket.writes[0].httpMetadata.cacheControl, "private, no-store");
});

test("a settings write racing the first CAS is reread and preserved on retry", async () => {
  const bucket = memoryBucket();
  bucket.beforeWrite = () => {
    bucket.beforeWrite = null;
    bucket.update({ ...originalSettings, newsletter_topic_id: "new-topic", digest_send_time: "19:45" });
  };
  const { api } = harness();
  const result = await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(result.digest_state_saved, true);
  assert.equal(bucket.writes.length, 2);
  assert.equal(bucket.value().newsletter_topic_id, "new-topic");
  assert.equal(bucket.value().digest_send_time, "19:45");
});

test("deleted settings are never resurrected after the email provider responds", async () => {
  const bucket = memoryBucket(null);
  const { api } = harness();
  const result = await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(result.digest_last_send_result, "sent");
  assert.equal(result.digest_state_saved, false);
  assert.equal(bucket.value(), null);
  assert.equal(bucket.writes.length, 0);
});

test("preview and failed attempts do not consume a scheduled delivery date", async () => {
  for (const [sent, options] of [[true, { test: true }], [false, {}]]) {
    const bucket = memoryBucket();
    const { api } = harness();
    await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent, detail: "No stories yet." }, { dateKey: "2026-11-23" }, options);
    assert.equal(bucket.value().digest_last_sent_date, "");
    assert.equal(bucket.value().digest_last_send_result, sent ? "sent" : "failed");
  }
});

test("an older completion cannot move the last scheduled delivery date backwards", async () => {
  const bucket = memoryBucket({ ...originalSettings, digest_last_sent_date: "2026-11-24" });
  const { api } = harness();
  await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(bucket.value().digest_last_sent_date, "2026-11-24");
});

test("persistent CAS conflicts are bounded and retain the actual provider result", async () => {
  const bucket = memoryBucket();
  bucket.beforeWrite = () => bucket.update({ ...bucket.value(), digest_email_enabled: false });
  const { api } = harness();
  const result = await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(bucket.writes.length, 4);
  assert.equal(bucket.value().digest_email_enabled, false);
  assert.equal(bucket.value().digest_last_sent_date, "");
  assert.equal(result.digest_last_send_result, "sent");
  assert.equal(result.digest_state_saved, false);
});

test("a transient settings read failure does not overwrite the current subscription", async () => {
  const bucket = memoryBucket();
  bucket.get = async () => { throw new Error("temporary storage failure"); };
  const { api, errors } = harness();
  const result = await api.recordNewsfeedEmailAttempt({ REPORT_BUCKET: bucket }, originalSettings.user_key, originalSettings, { sent: true }, { dateKey: "2026-11-23" });
  assert.equal(bucket.writes.length, 0);
  assert.equal(result.digest_last_send_result, "sent");
  assert.equal(result.digest_state_saved, false);
  assert.equal(errors.length, 1);
});

test("all-day and legacy Newsfeed ticks deliver without running maintenance or expiry reminders", async () => {
  const start = source.lastIndexOf("  async scheduled(event, env, ctx) {");
  assert.notEqual(start, -1);
  const scheduledSource = source.slice(start, source.lastIndexOf("\n};"));
  for (const cron of ["*/10 * * * *", "*/10 0-3,5-6,17-18,23 * * *", "*/10 23 * * *", "11 15 * * MON"]) {
    const calls = [];
    const context = {
      warmNewsfeedCaches: async () => { calls.push("warm"); },
      sendDueNewsfeedDigestEmails: async () => { calls.push("send"); },
      expiryReminderService: async () => { throw new Error("unexpected expiry scan"); },
    };
    vm.runInNewContext(`this.worker = {${scheduledSource}};`, context);
    const pending = [];
    await context.worker.scheduled({ cron }, {}, { waitUntil(promise) { pending.push(promise); } });
    await Promise.all(pending);
    assert.deepEqual(calls, cron === "11 15 * * MON" ? [] : ["warm", "send"]);
  }
});
