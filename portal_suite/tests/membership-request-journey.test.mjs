import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const accountServices = await readFile(new URL("../site_src/assets/account-services.js", import.meta.url), "utf8");

function functionSource(name) {
  const start = source.indexOf(`  async function ${name}(`) >= 0
    ? source.indexOf(`  async function ${name}(`)
    : source.indexOf(`  function ${name}(`);
  const end = source.indexOf("\n  }", start);
  assert.ok(start >= 0 && end > start, `${name} must exist`);
  return source.slice(start, end + 4);
}

function createHarness({ session = null, fetchResponse, authRefresh } = {}) {
  const elements = new Map();
  const requests = [];
  const events = [];
  const documentEvents = [];
  const documentListeners = new Map();
  const captchaLoads = [];
  const document = {
    activeElement: null,
    getElementById(id) { return elements.get(id) || null; },
    addEventListener(type, listener) {
      documentListeners.set(type, [...(documentListeners.get(type) || []), listener]);
    },
    removeEventListener(type, listener) {
      documentListeners.set(type, (documentListeners.get(type) || []).filter((value) => value !== listener));
    },
    dispatchEvent(event) {
      documentEvents.push(event);
      for (const listener of documentListeners.get(event.type) || []) listener(event);
    },
    body: {
      insertAdjacentHTML(_position, markup) {
        for (const match of markup.matchAll(/<([a-z][a-z0-9]*)\b([^>]*\bid="([^"]+)"[^>]*)>/gu)) {
          const [, tag, attrs, id] = match;
          const element = createElement(id, attrs);
          if (tag === "select") element.value = "";
          elements.set(id, element);
        }
      },
    },
  };
  function createElement(id, attrs = "") {
    const listeners = new Map();
    const attributes = new Map([...attrs.matchAll(/([\w-]+)="([^"]*)"/gu)].map((match) => [match[1], match[2]]));
    const classes = new Set((attributes.get("class") || "").split(/\s+/u));
    return {
      id,
      value: attributes.get("value") || "", textContent: "", placeholder: attributes.get("placeholder") || "", dataset: {}, style: {},
      hidden: /\shidden(?:\s|$)/u.test(attrs), disabled: false, readOnly: /\sreadonly(?:\s|$)/u.test(attrs),
      required: /\srequired(?:\s|$)/u.test(attrs), isConnected: true, tabIndex: 0,
      validity: { valid: true }, scrollTop: 0,
      classList: {
        add(value) { classes.add(value); }, remove(value) { classes.delete(value); },
        contains(value) { return classes.has(value); },
        toggle(value, force) { if (force ?? !classes.has(value)) classes.add(value); else classes.delete(value); },
      },
      setAttribute(name, value) { attributes.set(name, String(value)); },
      getAttribute(name) { return attributes.get(name) ?? null; },
      removeAttribute(name) { attributes.delete(name); },
      addEventListener(type, listener) {
        const entries = listeners.get(type) || [];
        entries.push(listener);
        listeners.set(type, entries);
      },
      removeEventListener(type, listener) {
        listeners.set(type, (listeners.get(type) || []).filter((value) => value !== listener));
      },
      async emit(type, details = {}) {
        const event = { target: this, preventDefault() {}, ...details };
        for (const listener of listeners.get(type) || []) await listener(event);
      },
      focus(options) { document.activeElement = this; this.focusOptions = options; },
      remove() { this.isConnected = false; elements.delete(id); },
      insertBefore() {}, querySelectorAll() { return []; },
      querySelector(selector) { return selector.startsWith("#") ? elements.get(selector.slice(1)) || null : null; },
    };
  }
  const trigger = createElement("originalRequestLink");
  document.activeElement = trigger;
  const context = vm.createContext({
    document, page: "index", URL, Set, AbortController, setTimeout, clearTimeout,
    CustomEvent: class { constructor(type, options = {}) { this.type = type; this.detail = options.detail; } },
    window: { alert() {}, clearInterval, setInterval, setTimeout, clearTimeout },
    MEMBERSHIP_REQUEST_KINDS: new Set(["membership", "support", "privacy", "refund", "access"]),
    loadAuthSession: () => session,
    authHeaders: () => session ? { Authorization: `Bearer ${session.token}` } : {},
    saveAuthSession: (value) => { session = value; }, clearAuthSession: () => { session = null; },
    authUserLabel: () => session?.user?.username || "登录", titleText: (item) => item.title || "",
    escapeHtml: (value) => String(value || "").replaceAll("&", "&amp;").replaceAll('"', "&quot;").replaceAll("<", "&lt;"),
    accessContactGuidanceHtml: () => "申请开通权限", journeyPageUrl: (name) => `/${name}`,
    registrationNoticeText: () => "账号提示", registrationCompleteText: () => "注册成功",
    localizedContactText: (value) => String(value || ""), currentAnalyticsPath: () => "/",
    isNewsfeedSession: () => true, isSuperSession: () => false, isOperatorSession: () => false,
    canOpenOperationsPanel: () => false, accountRightSummary: () => "",
    loadAccountCaptcha: async () => { captchaLoads.push(true); return "captcha-token"; },
    refreshAuthSession: async () => authRefresh ? authRefresh() : session,
    fetchRewardRequest: async () => ({ ok: true, json: async () => ({}) }),
    trackEvent: (_worker, type, payload) => events.push({ type, ...JSON.parse(JSON.stringify(payload)) }),
    fetch: async (url, options = {}) => {
      requests.push({ url, options });
      if (fetchResponse) return fetchResponse(url, options);
      return { ok: true, status: 200, json: async () => ({ ok: true }) };
    },
  });
  // Exercise the actual initializer with the real module already cached. The
  // admin runtime test separately verifies first-load script insertion.
  vm.runInContext(accountServices, context, { filename: "account-services.js" });
  vm.runInContext([
    "let accountServicesLoad = null;",
    functionSource("loadAccountServices"), functionSource("initLazyAccountServices"), functionSource("isAdminASession"),
    functionSource("membershipRequestKind"), functionSource("membershipRequestCopy"),
    functionSource("accountModalMarkup"), functionSource("showAccountModal"),
  ].join("\n"), context);
  return {
    document, trigger, requests, events, documentEvents, captchaLoads,
    getSession: () => session,
    setSession: (value) => { session = value; },
    get: (id) => elements.get(id),
    open: (options = { requestKind: "membership" }) => context.showAccountModal("/api", options),
    membershipEvents: () => events.filter((event) => event.type === "membership_request"),
    async edit(id, value) {
      const element = elements.get(id);
      element.value = value;
      await elements.get("membershipRequestForm").emit("input", { target: element });
    },
    async fill() {
      await this.edit("membershipRequesterEmail", "person@example.com");
      await this.edit("membershipContactChannel", "wechat");
      await this.edit("membershipContactValue", "private-contact-0123");
      await this.edit("membershipRequestMessage", "Private report interest");
    },
    submit: () => elements.get("membershipRequestForm").emit("submit"),
  };
}

test("explicit application starts at the public form and switches to login without losing the draft", async () => {
  const h = createHarness();
  await h.open();
  assert.equal(h.get("accountModalTitle").textContent, "申请加入会员");
  assert.equal(h.get("accountAuthForm").hidden, true);
  assert.equal(h.get("accountSummary").hidden, true);
  assert.equal(h.get("membershipRequestForm").hidden, false);
  assert.equal(h.get("membershipRequestIntro").hidden, false);
  assert.equal(h.get("membershipRequestLogin").hidden, false);
  assert.equal(h.document.activeElement.id, "membershipRequesterEmail");
  assert.equal(h.captchaLoads.length, 0, "public applications must not need an authentication captcha");
  assert.equal(h.requests.length, 0);
  assert.deepEqual(h.membershipEvents().map(({ action }) => action), ["form_impression", "form_open"]);
  assert.equal(h.events.some(({ type }) => type === "account_auth"), false, "application exposure must not inflate login exposure");
  await h.fill();
  await h.get("membershipRequestLogin").emit("click");
  assert.equal(h.get("accountAuthForm").hidden, false);
  assert.equal(h.get("membershipRequestCard").hidden, true);
  assert.equal(h.get("accountModalTitle").textContent, "登录 KC桌面");
  assert.equal(h.document.activeElement.id, "accountUsername");
  assert.equal(h.captchaLoads.length, 1);
  await h.get("membershipRequestBack").emit("click");
  assert.equal(h.get("accountAuthForm").hidden, true);
  assert.equal(h.get("membershipRequesterEmail").value, "person@example.com");
  assert.equal(h.get("membershipContactValue").value, "private-contact-0123");
  assert.equal(h.document.activeElement.id, "membershipContactChannel");
  assert.equal(h.membershipEvents().filter(({ action }) => action === "form_impression").length, 1);
  assert.equal(h.membershipEvents().filter(({ action }) => action === "form_start").length, 1);
  await h.get("accountModal").emit("keydown", { key: "Escape" });
  assert.equal(h.get("accountModal"), undefined);
  assert.equal(h.document.activeElement, h.trigger);
  assert.equal(h.trigger.focusOptions.preventScroll, true);
  assert.equal(h.membershipEvents().filter(({ action }) => action === "form_abandon").length, 1);
});

test("ordinary login keeps its existing primary form and does not count unseen applications", async () => {
  const h = createHarness();
  await h.open({ mode: "login", placement: "navigation" });
  assert.equal(h.get("accountAuthForm").hidden, false);
  assert.equal(h.get("membershipRequestForm").hidden, true);
  assert.equal(h.document.activeElement.id, "accountUsername");
  assert.equal(h.captchaLoads.length, 1);
  assert.equal(h.membershipEvents().length, 0);
  await h.get("membershipRequestToggle").emit("click");
  assert.equal(h.get("membershipRequestForm").hidden, false);
  assert.equal(h.get("accountAuthForm").hidden, true, "choosing an application inside the account dialog also makes it primary");
  assert.equal(h.get("accountModalTitle").textContent, "申请加入会员");
  assert.equal(h.document.activeElement.id, "membershipRequesterEmail");
  assert.deepEqual(h.membershipEvents().map(({ action }) => action), ["form_impression", "form_open"]);
  await h.get("membershipRequestLogin").emit("click");
  assert.equal(h.get("membershipRequestBack").hidden, false);
  assert.equal(h.get("accountAuthForm").hidden, false);
  await h.get("membershipRequestBack").emit("click");
  assert.equal(h.get("membershipRequestForm").hidden, false);
  await h.get("accountClose").emit("click");
  assert.equal(h.membershipEvents().some(({ action }) => action === "form_abandon"), false, "opening alone is not form abandonment");
});

test("validation attempts are measured and preserve values without sending a request", async () => {
  const h = createHarness();
  await h.open();
  await h.submit();
  assert.equal(h.requests.length, 0);
  assert.equal(h.document.activeElement.id, "membershipRequesterEmail");
  await h.edit("membershipRequesterEmail", "person@example.com");
  await h.submit();
  assert.equal(h.requests.length, 0);
  assert.equal(h.document.activeElement.id, "membershipContactChannel");
  assert.equal(h.get("membershipRequesterEmail").value, "person@example.com");
  assert.deepEqual(h.membershipEvents().filter(({ action }) => action === "form_error").map(({ error }) => error), ["validation_email", "validation_contact"]);
  assert.equal(h.membershipEvents().filter(({ action }) => action === "form_submit").length, 2);
});

test("a real form submission preserves the server contract, is single-flight, and never puts personal fields into analytics", async () => {
  let resolveRequest;
  const h = createHarness({ fetchResponse: () => new Promise((resolve) => { resolveRequest = resolve; }) });
  await h.open({ requestKind: "membership", requestPlacement: "unexpected person@example.com" });
  await h.fill();
  const pending = h.submit();
  assert.equal(h.get("membershipRequestSubmit").disabled, true);
  await h.submit();
  assert.equal(h.requests.length, 1);
  assert.equal(h.requests[0].url, "/api/membership/request");
  assert.deepEqual(JSON.parse(h.requests[0].options.body), {
    requester_email: "person@example.com", contact_channel: "wechat", contact_value: "private-contact-0123",
    note: "Private report interest", request_kind: "membership", page_path: "/", honeypot: "",
  });
  resolveRequest({ ok: true, status: 200, json: async () => ({ ok: true }) });
  await pending;
  assert.equal(h.get("membershipRequestSubmit").textContent, "申请已提交");
  assert.equal(h.get("membershipRequestSubmit").disabled, true);
  await h.submit();
  assert.equal(h.requests.length, 1, "a completed application cannot be resent from the same form");
  assert.deepEqual(h.membershipEvents().map(({ action }) => action), ["form_impression", "form_open", "form_start", "form_submit", "submitted"]);
  for (const event of h.membershipEvents()) {
    assert.equal(event.measurement_version, "membership-v1");
    assert.equal(event.placement, "membership");
    assert.deepEqual(Object.keys(event).sort(), ["action", "measurement_version", "placement", "request_kind", "status", "type"]);
  }
  assert.doesNotMatch(JSON.stringify(h.membershipEvents()), /person@example|private-contact|Private report/);
  await h.get("accountClose").emit("click");
  assert.equal(h.membershipEvents().some(({ action }) => action === "form_abandon"), false);
});

test("server and network failures stay retryable and measure only fixed error classes", async () => {
  let attempt = 0;
  const h = createHarness({ fetchResponse: async () => {
    attempt += 1;
    if (attempt === 1) throw new Error("person@example.com transport details");
    if (attempt === 2) return { ok: false, status: 503, json: async () => ({ detail: "private-contact-0123 server details" }) };
    return { ok: true, status: 200, json: async () => ({ ok: true, deduplicated: true }) };
  } });
  await h.open({ requestKind: "access", requestPlacement: "deep_link" });
  assert.equal(h.get("accountModalTitle").textContent, "申请开通或调整权限");
  await h.fill();
  for (let i = 0; i < 2; i += 1) {
    await h.submit();
    assert.equal(h.get("membershipRequestSubmit").disabled, false);
    assert.equal(h.get("membershipContactValue").value, "private-contact-0123");
  }
  await h.submit();
  assert.equal(h.get("membershipRequestSubmit").textContent, "申请已记录");
  assert.deepEqual(h.membershipEvents().filter(({ action }) => action === "form_error").map(({ error }) => error), ["network", "server"]);
  assert.equal(h.membershipEvents().filter(({ action }) => action === "deduplicated").length, 1);
  assert.doesNotMatch(JSON.stringify(h.membershipEvents()), /person@example|private-contact|Private report/);
});

test("signed-in applications focus the contact selector and defer account-only requests", async () => {
  const h = createHarness({ session: { token: "member", user: { id: "1", email: "member@example.com" } } });
  await h.open();
  assert.equal(h.get("membershipRequesterEmail").value, "member@example.com");
  assert.equal(h.get("membershipRequesterEmail").readOnly, true);
  assert.equal(h.document.activeElement.id, "membershipContactChannel");
  assert.equal(h.get("accountSummary").hidden, true);
  assert.equal(h.requests.length, 0);
});

test("temporary account verification failures retain the session; explicit authentication refusal clears it", async () => {
  for (const outcome of ["network", "invalid-json", 503, 401, 403, 200]) {
    let session = { token: "old", user: { id: "user-1" } };
    let clears = 0;
    const context = vm.createContext({
      authSessionRefreshes: new Map(), AbortController, setTimeout, clearTimeout,
      loadAuthSession: () => session, clearAuthSession: () => { clears += 1; session = null; },
      saveAuthSession: (value) => { session = value; },
      fetch: async () => {
        if (outcome === "network") throw new Error("temporary outage");
        return { ok: outcome === 200 || outcome === "invalid-json", status: typeof outcome === "number" ? outcome : 200,
          json: async () => { if (outcome === "invalid-json") throw new SyntaxError("bad JSON"); return { token: "new", user: { id: "user-1" } }; } };
      },
    });
    vm.runInContext(`${functionSource("authSessionRequestKey")}\n${functionSource("refreshAuthSession")}`, context);
    await context.refreshAuthSession("/api");
    assert.equal(clears, outcome === 401 || outcome === 403 ? 1 : 0, String(outcome));
    assert.equal(session?.token || null, outcome === 401 || outcome === 403 ? null : outcome === 200 ? "new" : "old", String(outcome));
  }
});

test("the account contact verification path does not undo transient-session preservation", async () => {
  const session = { token: "member", user: { id: "1", email: "member@example.com" } };
  const h = createHarness({ session, authRefresh: async () => null });
  await h.open({});
  await new Promise((resolve) => setImmediate(resolve));
  assert.equal(h.get("accountAuthForm").hidden, true);
  assert.equal(h.get("accountSummary").hidden, false);
  assert.equal(h.get("accountContactQrToggle").hidden, false);
  assert.match(h.get("accountContactQrStatus").textContent, /暂时无法验证/u);
  assert.equal(h.requests.some(({ url }) => url.endsWith("/membership/contact-card")), false);
});


test("an expired request token preserves the draft and allows an explicit guest retry", async () => {
  const h = createHarness({
    session: { token: "expired-token", user: { id: "old-user", email: "person@example.com" } },
    fetchResponse: async (_url, options) => options.headers.Authorization
      ? { ok: false, status: 401, json: async () => ({ detail: "Session expired" }) }
      : { ok: true, status: 200, json: async () => ({ ok: true }) },
  });
  await h.open();
  await h.fill();
  await h.submit();
  assert.equal(h.requests.length, 1, "an authentication rejection must never automatically resend a POST");
  assert.equal(h.getSession(), null);
  assert.equal(h.get("membershipRequesterEmail").readOnly, false);
  assert.equal(h.get("membershipRequesterEmail").value, "person@example.com");
  assert.equal(h.get("membershipContactValue").value, "private-contact-0123");
  assert.equal(h.get("membershipRequestMessage").value, "Private report interest");
  assert.equal(h.get("membershipRequestSubmit").disabled, false);
  assert.match(h.get("membershipRequestStatus").textContent, /已保留申请内容.*重新提交/u);
  await h.submit();
  assert.equal(h.requests.length, 2);
  assert.equal(h.requests[1].options.headers.Authorization, undefined);
  assert.equal(h.get("membershipRequestSubmit").textContent, "申请已提交");
  assert.deepEqual(JSON.parse(h.requests[1].options.body), JSON.parse(h.requests[0].options.body));
});

test("a late rejected application token cannot clear a newer login", async () => {
  let resolveRequest;
  const h = createHarness({
    session: { token: "old-token", user: { id: "old-user", email: "person@example.com" } },
    fetchResponse: () => new Promise((resolve) => { resolveRequest = resolve; }),
  });
  await h.open();
  await h.fill();
  const pending = h.submit();
  h.setSession({ token: "new-token", user: { id: "new-user", email: "new@example.com" } });
  resolveRequest({ ok: false, status: 401, json: async () => ({ detail: "Session expired" }) });
  await pending;
  assert.equal(h.getSession().token, "new-token");
  assert.equal(h.requests.length, 1);
  assert.equal(h.get("membershipRequesterEmail").value, "person@example.com");
  assert.equal(h.get("membershipContactValue").value, "private-contact-0123");
  assert.equal(h.get("membershipRequestSubmit").disabled, false);
  assert.match(h.get("membershipRequestStatus").textContent, /账号状态已更新/u);
});


test("an authenticated session with a redacted email submits using the account email", async () => {
  const h = createHarness({ session: { token: "member-token", user: { id: "member-1", email: "" } } });
  await h.open();
  assert.equal(h.get("membershipRequesterEmail").readOnly, true);
  assert.equal(h.get("membershipRequesterEmail").required, false);
  assert.equal(h.get("membershipRequesterEmail").placeholder, "使用当前账号邮箱");
  assert.equal(h.get("membershipAccountEmailHint").hidden, false);
  assert.equal(h.document.activeElement.id, "membershipContactChannel");
  await h.edit("membershipContactChannel", "telegram");
  await h.edit("membershipContactValue", "private-handle");
  await h.submit();
  assert.equal(h.requests.length, 1);
  assert.equal(h.requests[0].options.headers.Authorization, "Bearer member-token");
  assert.equal(JSON.parse(h.requests[0].options.body).requester_email, "");
  assert.equal(h.get("membershipRequestSubmit").textContent, "申请已提交");
  assert.equal(h.membershipEvents().some(({ error }) => error === "validation_email"), false);
});

test("a rejected redacted-email session becomes an editable guest form with required email", async () => {
  const h = createHarness({
    session: { token: "expired-token", user: { id: "member-1", email: "" } },
    fetchResponse: async () => ({ ok: false, status: 401, json: async () => ({}) }),
  });
  await h.open();
  await h.edit("membershipContactChannel", "telegram");
  await h.edit("membershipContactValue", "private-handle");
  await h.submit();
  assert.equal(h.requests.length, 1);
  assert.equal(h.get("membershipRequesterEmail").readOnly, false);
  assert.equal(h.get("membershipRequesterEmail").required, true);
  assert.equal(h.get("membershipAccountEmailHint").hidden, true);
  assert.equal(h.get("membershipContactValue").value, "private-handle");
  await h.submit();
  assert.equal(h.requests.length, 1, "a guest retry must require a valid email before sending");
  assert.equal(h.document.activeElement.id, "membershipRequesterEmail");
  assert.equal(h.membershipEvents().at(-1).error, "validation_email");
});

for (const entry of ["direct_application", "research_login"]) {
  test(`login success returns to the pending application from ${entry}`, async () => {
    const h = createHarness({ fetchResponse: async (url) => ({
      ok: true, status: 200,
      json: async () => url.endsWith("/auth")
        ? { token: "new-member-token", user: { id: "member-1", username: "researcher", email: "person@example.com" } }
        : { ok: true },
    }) });
    if (entry === "direct_application") await h.open({ requestKind: "membership" });
    else {
      await h.open({ mode: "login", placement: "research_limit", resumeIntent: true });
      await h.get("membershipRequestToggle").emit("click");
    }
    await h.fill();
    await h.get("membershipRequestLogin").emit("click");
    h.get("accountUsername").value = "researcher";
    h.get("accountPassword").value = "sample-password";
    h.get("accountCaptchaAnswer").value = "3";
    await h.get("accountAuthForm").emit("submit");
    assert.ok(h.get("accountModal"), "successful login must not close an unfinished application");
    assert.equal(h.get("accountAuthForm").hidden, true);
    assert.equal(h.get("membershipRequestCard").hidden, false);
    assert.equal(h.get("membershipRequestForm").hidden, false);
    assert.equal(h.get("accountModalTitle").textContent, "申请加入会员");
    assert.equal(h.get("membershipRequesterEmail").value, "person@example.com");
    assert.equal(h.get("membershipContactValue").value, "private-contact-0123");
    assert.equal(h.get("membershipRequestMessage").value, "Private report interest");
    assert.equal(h.document.activeElement.id, "membershipContactChannel");
    assert.equal(h.documentEvents.find(({ type }) => type === "portal-auth-complete").detail.resumeIntent, false);
    assert.equal(h.events.some(({ action }) => action === "intent_resumed"), false);
  });
}

test("ordinary research login still resumes its original intent", async () => {
  const h = createHarness({ fetchResponse: async (url) => ({
    ok: true, status: 200,
    json: async () => url.endsWith("/auth")
      ? { token: "new-member-token", user: { id: "member-1", username: "researcher", email: "person@example.com" } }
      : { ok: true },
  }) });
  await h.open({ mode: "login", placement: "research_limit", resumeIntent: true });
  h.get("accountUsername").value = "researcher";
  h.get("accountPassword").value = "sample-password";
  h.get("accountCaptchaAnswer").value = "3";
  await h.get("accountAuthForm").emit("submit");
  assert.equal(h.get("accountModal"), undefined);
  assert.equal(h.documentEvents.find(({ type }) => type === "portal-auth-complete").detail.resumeIntent, true);
  assert.equal(h.events.some(({ action }) => action === "intent_resumed"), true);
});


for (const clearedAt of ["before_submit", "before_response"]) {
  test(`an independent auth check clearing the session ${clearedAt} restores the guest email field`, async () => {
    let resolveRejectedRequest;
    const h = createHarness({
      session: { token: "expired-token", user: { id: "member-1", email: "" } },
      fetchResponse: async (_url, options) => {
        if (options.headers.Authorization) return new Promise((resolve) => { resolveRejectedRequest = resolve; });
        return { ok: true, status: 200, json: async () => ({ ok: true }) };
      },
    });
    await h.open();
    await h.edit("membershipContactChannel", "telegram");
    await h.edit("membershipContactValue", "private-handle");
    await h.edit("membershipRequestMessage", "Saved draft");
    if (clearedAt === "before_submit") {
      h.setSession(null);
      await h.submit();
      assert.equal(h.requests.length, 0);
    } else {
      const pending = h.submit();
      h.setSession(null);
      resolveRejectedRequest({ ok: false, status: 401, json: async () => ({}) });
      await pending;
      assert.equal(h.requests.length, 1, "an independent logout must not trigger an automatic POST retry");
    }
    assert.equal(h.get("membershipRequesterEmail").readOnly, false);
    assert.equal(h.get("membershipRequesterEmail").required, true);
    assert.equal(h.get("membershipAccountEmailHint").hidden, true);
    assert.equal(h.get("membershipContactValue").value, "private-handle");
    assert.equal(h.get("membershipRequestMessage").value, "Saved draft");
    await h.edit("membershipRequesterEmail", "guest@example.com");
    await h.submit();
    assert.equal(h.requests.at(-1).options.headers.Authorization, undefined);
    assert.equal(h.get("membershipRequestSubmit").textContent, "申请已提交");
  });
}
