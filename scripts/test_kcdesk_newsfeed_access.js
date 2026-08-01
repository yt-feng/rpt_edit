const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "kc_desk_notes/site_src/assets/app.js"), "utf8");

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  assert.ok(bodyStart >= 0, `${name} must have a body`);
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

const sandbox = { api: null };
vm.runInNewContext(`
  const NEWSFEED_EMAIL_DEFAULT_TIME = "09:00";
  const NEWSFEED_EMAIL_DEFAULT_TIMEZONE = "Asia/Shanghai";
  const NEWSFEED_SETTINGS_PREFIX = "_newsfeed/settings";
  function normalizeEmail(value) {
    const email = String(value || "").trim().toLowerCase();
    return /^[^@\\s]+@[^@\\s]+\\.[^@\\s]+$/.test(email) ? email : "";
  }
  function normalizeUsername(value) { return String(value || "").trim().toLowerCase(); }
  function accountDisabled(user) {
    return Boolean(user && (user.disabled || user.account_status === "disabled" || user.status === "disabled"));
  }
  function disabledAccountMessage() { return "Account disabled."; }
  function normalizeNewsfeedTime(value) { return String(value || "09:00"); }
  function normalizeNewsfeedTimezone(value) { return String(value || "Asia/Shanghai"); }
  function normalizeNewsfeedLanguage(value) { return String(value || "en"); }
  function normalizeNewsfeedRegions(value) { return Array.isArray(value) ? value : ["global"]; }
  async function currentUserFromRequest(env) {
    if (env.authError) throw env.authError;
    return env.user;
  }
  async function loadNewsfeedTopics(env, user) {
    return env.topicsByEmail[normalizeEmail(user.email)] || [];
  }
  ${extractFunction(worker, "isNewsfeedAccount")}
  ${extractFunction(worker, "requireNewsfeedUser")}
  ${extractFunction(worker, "newsfeedUserKey")}
  ${extractFunction(worker, "newsfeedSettingsKey")}
  ${extractFunction(worker, "defaultNewsfeedSettings")}
  ${extractFunction(worker, "hasOwnField")}
  ${extractFunction(worker, "nextNewsfeedSettingsFromPayload")}
  ${extractFunction(worker, "findNewsfeedTopic")}
  ${extractFunction(worker, "validateNewsfeedNewsletterSelection")}
  api = {
    isNewsfeedAccount,
    requireNewsfeedUser,
    newsfeedSettingsKey,
    defaultNewsfeedSettings,
    nextNewsfeedSettingsFromPayload,
    validateNewsfeedNewsletterSelection,
  };
`, sandbox);

const api = sandbox.api;
const reader = { id: "user-a", username: "reader", email: "reader@example.com" };
const other = { id: "user-b", username: "other", email: "other@example.com" };

assert.equal(api.isNewsfeedAccount(reader), true, "every active registered user gets Newsfeed access");
assert.equal(api.isNewsfeedAccount({ ...reader, disabled: true }), false, "disabled users stay blocked");

(async () => {
  await assert.rejects(
    api.requireNewsfeedUser({}, { authError: new Error("Please log in.") }),
    /Please log in/,
    "anonymous requests must be rejected",
  );
  assert.equal(
    await api.requireNewsfeedUser({}, { user: reader }),
    reader,
    "an ordinary registered user must be accepted",
  );
  await assert.rejects(
    api.requireNewsfeedUser({}, { user: { ...reader, disabled: true } }),
    /disabled/i,
    "disabled users must be rejected even if a stale session reaches the Newsfeed guard",
  );

  const topicsByEmail = {
    [reader.email]: [
      { id: "global-daily", title: "Global Daily" },
      { id: "reader-topic", title: "Reader topic" },
    ],
    [other.email]: [
      { id: "global-daily", title: "Global Daily" },
      { id: "other-topic", title: "Other topic" },
    ],
  };
  const env = { topicsByEmail };
  const initial = api.defaultNewsfeedSettings(reader);
  const subscribed = api.nextNewsfeedSettingsFromPayload(initial, reader, {
    digest_email_enabled: true,
    digest_email: other.email,
    newsletter_topic_id: "reader-topic",
    user_key: "other-account",
  });
  assert.equal(subscribed.digest_email, reader.email, "a request cannot subscribe another person's email");
  assert.equal(subscribed.user_key, encodeURIComponent(reader.email), "settings remain bound to the signed-in account");
  assert.equal(subscribed.newsletter_topic_id, "reader-topic", "one selected newsletter is stored as a scalar");
  assert.equal(
    (await api.validateNewsfeedNewsletterSelection(env, reader, subscribed)).newsletter_topic_id,
    "reader-topic",
    "a user can select one newsletter available to their own account",
  );

  const replaced = api.nextNewsfeedSettingsFromPayload(subscribed, reader, {
    digest_email_enabled: true,
    newsletter_topic_id: "global-daily",
  });
  assert.equal(replaced.newsletter_topic_id, "global-daily", "selecting a new newsletter replaces the old one");

  const canceled = api.nextNewsfeedSettingsFromPayload(replaced, reader, {
    digest_email_enabled: false,
    newsletter_topic_id: "reader-topic",
  });
  assert.equal(canceled.newsletter_topic_id, "", "turning the subscription off removes the newsletter selection");

  await assert.rejects(
    api.validateNewsfeedNewsletterSelection(env, reader, { ...subscribed, newsletter_topic_id: "other-topic" }),
    /not available/i,
    "a user cannot subscribe to another account's private topic",
  );
  await assert.rejects(
    api.validateNewsfeedNewsletterSelection(env, reader, { ...subscribed, newsletter_topic_id: ["reader-topic", "global-daily"] }),
    /not available/i,
    "multiple newsletter ids are rejected",
  );
  assert.notEqual(
    api.newsfeedSettingsKey(reader),
    api.newsfeedSettingsKey(other),
    "different accounts must never share a settings object",
  );

  assert.doesNotMatch(app, /NEWSFEED_ACCOUNT_(?:USERNAMES|EMAILS)/, "the frontend must not retain an account allowlist");
  assert.match(app, /function isNewsfeedSession[\s\S]*?Boolean\(user\)/, "the frontend exposes Newsfeed to registered sessions");
  assert.match(app, /id="newsNewsletterTopic"/, "the UI exposes the single-newsletter selector");
  assert.match(app, /id="newsEmailInput"[\s\S]*?readonly/, "the newsletter recipient is fixed to the account email");
  const settingsHandler = extractFunction(worker, "handleNewsfeedSettings");
  assert.match(settingsHandler, /requireNewsfeedUser\(request, env\)/, "settings routes require the current user");
  assert.match(settingsHandler, /validateNewsfeedNewsletterSelection\(env, user, next\)/, "newsletter choices are checked against that user's topics");
  const emailHandler = extractFunction(worker, "handleNewsfeedEmailSend");
  assert.match(emailHandler, /validateNewsfeedNewsletterSelection\(env, user, next\)/, "manual sends use the same one-newsletter guard");
  const scheduledSender = extractFunction(worker, "sendDueNewsfeedDigestEmails");
  assert.match(scheduledSender, /newsfeedUserForStoredSettings\(env, settings\)/, "scheduled delivery revalidates account ownership and status");

  console.log("kcdesk Newsfeed access/newsletter tests passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
