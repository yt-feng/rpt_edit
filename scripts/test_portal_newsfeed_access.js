const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/portal-suite-worker/src/index.js"), "utf8");
const app = fs.readFileSync(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const localeCss = fs.readFileSync(path.join(root, "portal_suite/locale_assets/locale.css"), "utf8");

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

function newsfeedLocaleUi(locale, targetLanguage = "ar") {
  const localeSandbox = { result: null };
  vm.runInNewContext(`
    const CONTENT_LOCALE = ${JSON.stringify(locale)};
    const window = {
      PortalLocale: {
        localeUrl(locale) { return "https://portal.example.invalid/" + locale + "/newsfeed.html?q=markets#top"; },
      },
    };
    ${extractFunction(app, "isLocalizedContentPage")}
    ${extractFunction(app, "newsfeedLanguageCode")}
    ${extractFunction(app, "newsfeedFixedInterfaceLanguage")}
    ${extractFunction(app, "newsfeedInterfaceLocaleCode")}
    ${extractFunction(app, "newsfeedInterfaceNavigationUrl")}
    result = {
      fixed: newsfeedFixedInterfaceLanguage(),
      targetLocale: newsfeedInterfaceLocaleCode(${JSON.stringify(targetLanguage)}),
      targetUrl: newsfeedInterfaceNavigationUrl(${JSON.stringify(targetLanguage)}),
    };
  `, localeSandbox);
  return localeSandbox.result;
}

for (const locale of ["ko", "ja", "ar"]) {
  assert.equal(newsfeedLocaleUi(locale).fixed, locale, `${locale} Newsfeed UI must follow the URL locale`);
}
assert.equal(newsfeedLocaleUi("zh-Hans").fixed, "", "the Chinese root keeps its existing Newsfeed preference behavior");
assert.equal(newsfeedLocaleUi("ja", "zh-CN").targetLocale, "zh-Hans");
assert.equal(
  newsfeedLocaleUi("ja", "ko").targetUrl,
  "https://portal.example.invalid/ko/newsfeed.html?q=markets#top",
  "interface switching must reuse localeUrl and preserve the current URL state",
);

const settingsSandbox = { state: null };
vm.runInNewContext(`
  const CONTENT_LOCALE = "ja";
  function normalizeNewsfeedRegionsClient(value) { return value || ["global"]; }
  ${extractFunction(app, "isLocalizedContentPage")}
  ${extractFunction(app, "newsfeedLanguageCode")}
  ${extractFunction(app, "newsfeedFixedInterfaceLanguage")}
  ${extractFunction(app, "applyNewsfeedSettings")}
  state = { interfaceLanguage: "ja", outputLanguage: "en", preferredRegions: ["global"] };
  applyNewsfeedSettings(state, { interface_language: "ar", digest_language: "ko", preferred_regions: ["mena"] });
`, settingsSandbox);
assert.equal(settingsSandbox.state.interfaceLanguage, "ja", "saved settings cannot override a localized URL's interface language");
assert.equal(settingsSandbox.state.outputLanguage, "ko", "content output language remains independent of the interface locale");

const timeSandbox = { calls: [], result: "" };
vm.runInNewContext(`
  const CONTENT_LOCALE = "ja";
  const CONTENT_INTL_LOCALE = "ja-JP";
  const Intl = {
    RelativeTimeFormat: class {
      constructor(locale) { calls.push(["relative", locale]); this.locale = locale; }
      format(value, unit) { return this.locale + ":" + value + ":" + unit; }
    },
    DateTimeFormat: class {
      constructor(locale) { calls.push(["absolute", locale]); this.locale = locale; }
      format() { return this.locale + ":absolute"; }
    },
  };
  ${extractFunction(app, "isLocalizedContentPage")}
  ${extractFunction(app, "newsfeedTimeLabel")}
  result = newsfeedTimeLabel(${JSON.stringify(new Date(Date.now() - 5 * 60 * 1000).toISOString())});
`, timeSandbox);
assert.match(timeSandbox.result, /^ja-JP:-\d+:minute$/, "relative Newsfeed time must be formatted through the page locale");
assert.deepEqual(Array.from(timeSandbox.calls[0]), ["relative", "ja-JP"]);

const rootPresentationSandbox = { result: null };
vm.runInNewContext(`
  const CONTENT_LOCALE = "zh-Hans";
  ${extractFunction(app, "isLocalizedContentPage")}
  const NEWSFEED_SYSTEM_TOPIC_COPY = { "tech-ai": { title: "Technology news" } };
  const NEWSFEED_CATEGORY_COPY = { Tech: "Technology news" };
  const NEWSFEED_SUGGESTED_TOPIC_COPY = { "Original suggestion": "Localized suggestion" };
  ${extractFunction(app, "newsfeedTopicText")}
  ${extractFunction(app, "newsfeedCategoryText")}
  ${extractFunction(app, "newsfeedSuggestedTopicText")}
  result = {
    topic: newsfeedTopicText({ id: "tech-ai", title: "Tech" }),
    category: newsfeedCategoryText("Tech"),
    suggestion: newsfeedSuggestedTopicText("Original suggestion"),
  };
`, rootPresentationSandbox);
assert.deepEqual(
  JSON.parse(JSON.stringify(rootPresentationSandbox.result)),
  { topic: "Tech", category: "Tech", suggestion: "Original suggestion" },
  "localized presentation mappings must not change the Chinese root",
);

const rootTimeSandbox = { result: "" };
vm.runInNewContext(`
  const CONTENT_LOCALE = "zh-Hans";
  const CONTENT_INTL_LOCALE = "zh-CN";
  ${extractFunction(app, "isLocalizedContentPage")}
  ${extractFunction(app, "newsfeedTimeLabel")}
  result = newsfeedTimeLabel(${JSON.stringify(new Date(Date.now() - 5 * 60 * 1000).toISOString())});
`, rootTimeSandbox);
assert.match(rootTimeSandbox.result, /^\d+m ago$/, "the Chinese root keeps its established Newsfeed relative-time format");

assert.match(app, /if \(fixedInterfaceLanguage\) \{[\s\S]{0,260}newsfeedInterfaceNavigationUrl[\s\S]{0,160}window\.location\.href = nextUrl[\s\S]{0,80}return;/, "localized interface selection must navigate instead of mutating lang state");
assert.match(app, /data-action="home-category"[\s\S]{0,220}newsfeedCategoryText\(item\)/, "home category labels must be localized without changing category values");
assert.match(app, /data-action="explore-category"[\s\S]{0,220}newsfeedCategoryText\(item\)/, "explore category labels must be localized without changing category values");
assert.match(app, /newsfeedSuggestedTopicText\(topic\)/, "built-in suggested-topic labels must be localized");
assert.match(app, /const topicTitle = newsfeedTopicText\(topic\)[\s\S]{0,400}<h2>\$\{escapeHtml\(topicTitle\)\}/, "built-in topic pages must use localized title copy");
assert.match(app, /localizedServiceMessage\(data\.detail \|\| data\.error, "Newsfeed request failed\."\)/, "localized Newsfeed API errors must use generic translated copy");
assert.match(localeCss, /html\[dir="rtl"\] \.course-material-cover > span \{[\s\S]*?border-radius: 0 0 0 12px;/, "the Arabic course-cover badge must mirror its corner radius");

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

  console.log("portal Newsfeed access/newsletter tests passed");
})().catch((error) => {
  console.error(error);
  process.exitCode = 1;
});
