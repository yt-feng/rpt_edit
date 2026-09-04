import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appSource = await readFile(path.join(root, "portal_suite/site_src/assets/app.js"), "utf8");
const stylesSource = await readFile(path.join(root, "portal_suite/site_src/assets/styles.css"), "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.notEqual(start, -1, `missing ${name}`);
  const declarationEnd = source.indexOf(") {", start);
  assert.notEqual(declarationEnd, -1, `missing ${name} body`);
  const bodyStart = declarationEnd + 2;
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`unterminated ${name}`);
}

function policyHarness() {
  const events = [];
  const helpers = [
    "newsfeedSystemTopic",
    "newsfeedCustomTopics",
    "normalizeNewsfeedPolicy",
    "applyNewsfeedPolicy",
    "newsfeedCanCustomize",
    "newsfeedCanSubscribe",
    "newsfeedCanOpenAdd",
    "newsfeedCanCreateTopic",
    "newsfeedShouldShowRequest",
    "newsfeedVisibleTopics",
    "newsfeedTopicAnalyticsKey",
    "newsfeedTopicAnalyticsFields",
    "trackNewsfeedInteraction",
  ];
  const context = {
    events,
    isNewsfeedSession(session) {
      const user = session && session.user;
      return Boolean(user) && !user.disabled && user.account_status !== "disabled" && user.status !== "disabled";
    },
    isSuperSession(session) {
      const user = session && session.user;
      return Boolean(user && (user.role === "super" || user.is_super));
    },
    trackEvent(workerUrl, type, data) { events.push({ workerUrl, type, data }); },
  };
  const systemIds = appSource.match(/const NEWSFEED_SYSTEM_TOPIC_IDS = new Set\(\[[\s\S]*?\]\);/u);
  assert.ok(systemIds, "missing fixed General topic set");
  vm.runInNewContext(`
    ${systemIds[0]}
    ${helpers.map((name) => extractFunction(appSource, name)).join("\n")}
    this.newsfeedHelpers = { ${helpers.join(",")} };
  `, context, { filename: "newsfeed-policy-helpers.js" });
  return { events, helpers: context.newsfeedHelpers };
}

test("Newsfeed navigation is public on every primary page while Newsfeed stays noindex", async () => {
  const pages = ["index", "doc", "report", "charts", "courses", "newsfeed"];
  for (const page of pages) {
    const html = await readFile(path.join(root, `portal_suite/site_src/${page}.html`), "utf8");
    const nav = html.match(/<a\b[^>]*\bid="newsfeedNav"[^>]*>/u);
    assert.ok(nav, `${page}.html must expose Newsfeed navigation`);
    assert.doesNotMatch(nav[0], /\bhidden\b/u, `${page}.html must not hide Newsfeed navigation`);
    assert.match(nav[0], /href="newsfeed\.html"/u);
  }
  const newsfeed = await readFile(path.join(root, "portal_suite/site_src/newsfeed.html"), "utf8");
  assert.match(newsfeed, /<meta name="robots" content="noindex,nofollow,noarchive,max-image-preview:none">/u);
  assert.match(newsfeed, /<body\b[^>]*data-analytics-auto="manual"/u);
  assert.match(newsfeed, /General 公开话题正在加载/u);
  assert.doesNotMatch(newsfeed, /请登录已注册|id="newsfeedLogin"/u, "pre-JavaScript markup must not present a false login gate");
});

test("anonymous, member and admin policies normalize from final and compatibility contracts", () => {
  const { helpers } = policyHarness();
  const systemTopics = [
    { id: "global-daily", kind: "system" },
    { id: "tech-ai", kind: "system" },
    { id: "global-politics", kind: "system" },
    { id: "industries", kind: "system" },
    { id: "investment", kind: "system" },
  ];
  const anonymous = helpers.normalizeNewsfeedPolicy({
    tier: "general",
    authenticated: false,
    can_customize: false,
    can_subscribe: false,
    custom_topic_limit: 0,
    custom_topic_count: 0,
    custom_topic_remaining: 0,
  }, null, [...systemTopics, { id: "private-topic", kind: "custom" }]);
  assert.equal(anonymous.authenticated, false);
  assert.equal(anonymous.can_customize, false);
  assert.equal(anonymous.can_subscribe, false);
  assert.equal(anonymous.custom_topic_limit, 0);
  assert.equal(helpers.newsfeedVisibleTopics({ policy: anonymous }, [...systemTopics, { id: "private-topic" }]).length, 5);

  const memberState = {
    session: { user: { email: "member@example.test" } },
    topics: [...systemTopics, { id: "private-topic", kind: "custom" }],
  };
  const member = helpers.applyNewsfeedPolicy(memberState, {
    topic_policy: {
      tier: "member",
      authenticated: true,
      can_create_custom: false,
      can_subscribe: true,
    },
    custom_topics: { count: 3, limit: 3, remaining: 0 },
    request_available: true,
  });
  assert.equal(member.can_customize, true, "a positive server limit grants member customization even when using can_create_custom compatibility data");
  assert.equal(member.can_subscribe, true);
  assert.equal(member.custom_topic_count, 3);
  assert.equal(member.custom_topic_limit, 3);
  assert.equal(member.custom_topic_remaining, 0);
  assert.equal(member.request_allowed, true);
  assert.equal(helpers.newsfeedShouldShowRequest(memberState), true);

  const countedFree = helpers.normalizeNewsfeedPolicy({
    tier: "registered",
    authenticated: true,
    custom_topic_count: 2,
    custom_topic_limit: 0,
    custom_topic_remaining: 0,
  }, { user: { email: "free@example.test" } }, [{ id: "legacy-custom" }]);
  assert.equal(countedFree.can_customize, false, "observed custom topics alone must not grant member controls");
  assert.equal(countedFree.can_subscribe, false);

  const adminState = { session: null, topics: systemTopics };
  const admin = helpers.applyNewsfeedPolicy(adminState, {
    policy: { tier: "admin", authenticated: true },
    custom_topic_count: 8,
    custom_topic_limit: null,
    custom_topic_remaining: null,
  });
  assert.equal(admin.unlimited, true, "authenticated admin with an explicit null limit must be unlimited without a complete local session");
  assert.equal(admin.custom_topic_limit, null);
  assert.equal(admin.custom_topic_remaining, null);
  assert.equal(admin.can_customize, true);
  assert.equal(admin.can_subscribe, true);
});

test("public initialization has optional auth, epoch protection and auth-change re-layering", () => {
  const init = extractFunction(appSource, "initNewsfeed");
  const request = extractFunction(appSource, "newsfeedJson");
  assert.doesNotMatch(init, /renderNewsfeedAccess/u, "anonymous Newsfeed must not stop at the old login gate");
  assert.doesNotMatch(init, /if\s*\(\s*!isNewsfeedSession/u, "anonymous Newsfeed must load General directly");
  assert.match(request, /\.\.\.authHeaders\(\)/u, "Authorization must remain optional");
  assert.match(init, /trackEvent\(workerUrl, "page_view"/u, "anonymous and authenticated visits must both be recorded");
  assert.match(init, /document\.addEventListener\("portal-auth-change", \(\) => window\.location\.reload\(\)\)/u, "login and logout must re-layer the page immediately");
  assert.ok((init.match(/epoch !== state\.requestEpoch/gu) || []).length >= 3, "home, explore and topic responses must all reject stale epochs");
  assert.match(init, /newsfeedShouldShowRequest\(state\)[\s\S]*?renderNewsfeedAdd\(state\)/u, "an initially exhausted account must see the explicit request form");
  assert.doesNotMatch(appSource, /const\s+NEWSFEED_TOPIC_LIMIT|10,?000\s+custom|10000\s*个/u, "the retired 10,000-topic frontend quota must not return");
});

test("localized Newsfeed defaults and controls include Arabic without changing the root default", () => {
  const languageCode = extractFunction(appSource, "newsfeedLanguageCode");
  const defaultLanguage = extractFunction(appSource, "newsfeedDefaultLanguage");
  const defaultFor = (contentLocale) => {
    const context = {
      window: contentLocale ? { PortalLocale: { contentLocale } } : {},
    };
    vm.runInNewContext(`
      ${languageCode}
      ${defaultLanguage}
      this.value = newsfeedDefaultLanguage();
    `, context, { filename: "newsfeed-default-language.js" });
    return context.value;
  };

  assert.equal(defaultFor(undefined), "en");
  assert.equal(defaultFor("zh-Hans"), "en");
  assert.equal(defaultFor("ko"), "ko");
  assert.equal(defaultFor("ja"), "ja");
  assert.equal(defaultFor("ar"), "ar");

  const copyBlock = appSource.match(/const NEWSFEED_UI_COPY = (\{[\s\S]*?\n  \});/u);
  assert.ok(copyBlock, "missing Newsfeed UI copy table");
  const copyContext = {};
  vm.runInNewContext(`${copyBlock[0]}\nthis.copy = NEWSFEED_UI_COPY;`, copyContext, {
    filename: "newsfeed-ui-copy.js",
  });
  assert.equal(copyContext.copy.ar.language, "اللغة");
  assert.equal(copyContext.copy.ar.playBriefing, "تشغيل الموجز الصوتي");

  const optionsFor = (contentLocale, selected) => {
    const optionsContext = {};
    vm.runInNewContext(`
      const CONTENT_LOCALE = ${JSON.stringify(contentLocale)};
      function escapeHtml(value) { return String(value); }
      ${extractFunction(appSource, "isLocalizedContentPage")}
      ${extractFunction(appSource, "newsfeedLanguageOptions")}
      this.options = newsfeedLanguageOptions(${JSON.stringify(selected)});
    `, optionsContext, { filename: "newsfeed-language-options.js" });
    return optionsContext.options;
  };
  assert.match(optionsFor("ar", "ar"), /value="ar" selected>العربية<\/option>/u);
  assert.doesNotMatch(optionsFor("zh-Hans", "en"), /value="ar"/u, "the Chinese root keeps its existing output-language choices");

  const init = extractFunction(appSource, "initNewsfeed");
  assert.match(init, /const defaultLanguage = newsfeedDefaultLanguage\(\)/u);
  assert.match(init, /outputLanguage:\s*defaultLanguage/u);
  assert.match(init, /interfaceLanguage:\s*defaultLanguage/u);
});

test("topic-limit request is confirmation-only and sends the server-owned contract", () => {
  const init = extractFunction(appSource, "initNewsfeed");
  const requestStart = init.indexOf('if (event.target && event.target.id === "newsTopicRequestForm")');
  const requestEnd = init.indexOf('if (event.target && event.target.id === "newsCustomRegionForm")', requestStart);
  assert.ok(requestStart >= 0 && requestEnd > requestStart, "missing topic request submit handler");
  const requestBlock = init.slice(requestStart, requestEnd);
  assert.match(requestBlock, /!confirm\.checked/u, "request must require an explicit checkbox confirmation");
  assert.match(requestBlock, /"\/newsfeed\/topics\/request"/u);
  const body = requestBlock.match(/const body = \{([\s\S]*?)\n\s*\};/u);
  assert.ok(body, "missing topic request body");
  for (const field of ["topic", "output_language", "preferred_regions", "page_path", "honeypot"]) {
    assert.match(body[1], new RegExp(`\\b${field}\\b`, "u"), `missing ${field}`);
  }
  assert.doesNotMatch(body[1], /\b(?:recipient|requester_email|email|tier|limit)\b/u, "client must not forge routing or entitlement fields");

  const createStart = init.indexOf('if (event.target && event.target.id === "newsTopicForm")');
  const createBlock = init.slice(createStart, requestStart);
  assert.match(createBlock, /error\.status === 409 && error\.code === "NEWSFEED_TOPIC_LIMIT"/u);
  assert.match(createBlock, /renderNewsfeedAdd\(state\)/u);
  assert.doesNotMatch(createBlock, /\/newsfeed\/topics\/request/u, "409 handling must never auto-send the request");
});

test("Newsfeed interaction analytics includes tier usage but never raw custom content", () => {
  const { events, helpers } = policyHarness();
  const secretTopic = "Confidential acquisition target";
  const state = {
    workerUrl: "/api",
    currentView: "add",
    policy: {
      authenticated: true,
      tier: "admin",
      custom_topic_count: 7,
      custom_topic_limit: null,
      custom_topic_remaining: null,
      unlimited: true,
    },
  };
  helpers.trackNewsfeedInteraction(state, "topic_request", { outcome: "submit", requested_topic: secretTopic });
  assert.equal(events.length, 1);
  assert.equal(events[0].type, "newsfeed_interaction");
  assert.equal(events[0].data.tier, "admin");
  assert.equal(events[0].data.count, 7);
  assert.equal(events[0].data.limit, null);
  assert.equal(events[0].data.custom_topic_remaining, null);
  assert.equal(events[0].data.topic_kind, "custom");
  assert.match(events[0].data.topic_hash, /^topic-[a-z0-9]+$/u);
  assert.doesNotMatch(JSON.stringify(events[0]), new RegExp(secretTopic, "u"));
  const tracker = extractFunction(appSource, "trackNewsfeedInteraction");
  assert.doesNotMatch(tracker, /details\.(?:title|url|email)|details\[(?:"|')(?:title|url|email)/u);
});

test("email controls remain inside a 390px viewport", () => {
  assert.match(stylesSource, /\.news-email-settings\s*\{[\s\S]*?min-width:\s*0;[\s\S]*?max-width:\s*100%;/u);
  assert.match(stylesSource, /\.news-email-settings \.status-line\s*\{[\s\S]*?min-width:\s*0;[\s\S]*?overflow-wrap:\s*anywhere;[\s\S]*?word-break:\s*break-word;/u);
  assert.match(stylesSource, /@media \(max-width: 760px\)[\s\S]*?\.news-email-form\s*\{[\s\S]*?grid-template-columns:\s*minmax\(0, 1fr\);[\s\S]*?width:\s*100%;/u);
  assert.match(stylesSource, /@media \(max-width: 760px\)[\s\S]*?\.news-email-settings,[\s\S]*?\.news-email-copy,[\s\S]*?\.news-email-form\s*\{\s*grid-template-columns:\s*minmax\(0, 1fr\);/u);
  assert.match(stylesSource, /\.news-email-form input,[\s\S]*?\.news-email-form select\s*\{[\s\S]*?width:\s*100%;[\s\S]*?min-width:\s*0;/u);
  assert.match(stylesSource, /\.newsfeed-bottom-tabs\.is-public\s*\{\s*grid-template-columns:\s*repeat\(2, minmax\(0, 1fr\)\);/u);
});
