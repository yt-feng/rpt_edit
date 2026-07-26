import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const appPath = path.join(root, "kc_desk_notes/site_src/assets/app.js");
const stylesPath = path.join(root, "kc_desk_notes/site_src/assets/styles.css");
const [app, styles] = await Promise.all([readFile(appPath, "utf8"), readFile(stylesPath, "utf8")]);

function extractFunction(source, name) {
  const functionStart = source.indexOf(`function ${name}(`);
  assert.ok(functionStart >= 0, `${name} must exist`);
  const start = source.slice(Math.max(0, functionStart - 6), functionStart) === "async "
    ? functionStart - 6
    : functionStart;
  const bodyStart = source.indexOf("{", source.indexOf(")", functionStart));
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

function fakeElement(options = {}) {
  const listeners = new Map();
  const element = {
    hidden: Boolean(options.hidden),
    disabled: false,
    textContent: "",
    className: "",
    href: "",
    addEventListener(type, listener) {
      const values = listeners.get(type) || [];
      values.push(listener);
      listeners.set(type, values);
    },
    trigger(type) {
      for (const listener of listeners.get(type) || []) {
        listener({ preventDefault() {} });
      }
    },
  };
  element.classList = {
    add(value) {
      const values = new Set(element.className.split(/\s+/u).filter(Boolean));
      values.add(value);
      element.className = [...values].join(" ");
    },
  };
  Object.defineProperty(element, "innerHTML", {
    set() { throw new Error("protected text must never use innerHTML"); },
  });
  return element;
}

function createHarness(initialSession = null) {
  const elements = {
    textOnlyTextAccess: fakeElement(),
    viewTextOnlyText: fakeElement(),
    openTextOnlySponsor: fakeElement(),
    textOnlyTextStatus: fakeElement(),
    textOnlyTextContent: fakeElement({ hidden: true }),
    textOnlyTextSource: fakeElement(),
    textOnlyTextBody: fakeElement(),
    loadMoreTextOnlyText: fakeElement({ hidden: true }),
  };
  const documentListeners = new Map();
  const pendingFetches = [];
  const fetchCalls = [];
  let session = initialSession;
  let clearedSessions = 0;
  let modalOpens = 0;

  const document = {
    getElementById(id) { return elements[id] || null; },
    addEventListener(type, listener) {
      const values = documentListeners.get(type) || [];
      values.push(listener);
      documentListeners.set(type, values);
    },
  };
  function emit(type) {
    for (const listener of documentListeners.get(type) || []) listener();
  }
  function fetch(url, options) {
    fetchCalls.push({ url: String(url), options });
    return new Promise((resolve) => pendingFetches.push(resolve));
  }
  function respond(body, status = 200) {
    const resolve = pendingFetches.shift();
    assert.ok(resolve, "a text request must be pending");
    resolve({
      ok: status >= 200 && status < 300,
      status,
      async json() { return body; },
    });
  }

  const sandbox = {
    URLSearchParams,
    document,
    fetch,
    loadAuthSession() { return session; },
    clearAuthSession() {
      clearedSessions += 1;
      session = null;
      emit("kcdesk-auth-change");
    },
    showAccountModal() { modalOpens += 1; },
    vid2pptSponsorUrlForSession(value) {
      return `https://vid2ppt.test/?email=${encodeURIComponent(value && value.user && value.user.email || "")}`;
    },
    localizedContactText(value) { return String(value || ""); },
    analyticsReportPayload() { return { report_id: "report-1" }; },
    trackEvent() {},
  };
  const init = vm.runInNewContext(`(${extractFunction(app, "initTextOnlyTextAccess")})`, sandbox);
  init({ id: "report-1" }, "https://worker.test");

  return {
    elements,
    fetchCalls,
    respond,
    emitAuthChange() { emit("kcdesk-auth-change"); },
    setSession(value) { session = value; },
    getSession() { return session; },
    get clearedSessions() { return clearedSessions; },
    get modalOpens() { return modalOpens; },
  };
}

async function flushAsyncWork() {
  await Promise.resolve();
  await new Promise((resolve) => setImmediate(resolve));
}

function session(token = "token-a", overrides = {}) {
  return {
    token,
    user: {
      id: "user-1",
      email: "member@example.com",
      username: "member",
      role: "free",
      ...overrides,
    },
  };
}

test("Text only clears on logout, ignores stale responses, and renders API strings as text", async () => {
  const harness = createHarness(session());
  const { elements } = harness;
  elements.viewTextOnlyText.trigger("click");
  assert.equal(harness.fetchCalls.length, 1);

  harness.setSession(null);
  harness.emitAuthChange();
  assert.equal(elements.textOnlyTextBody.textContent, "");
  assert.equal(elements.textOnlyTextContent.hidden, true);
  harness.respond({
    text: "<script>alert('stale')</script>",
    source_label: "<b>stale source</b>",
    has_more: false,
    next_cursor: "",
  });
  await flushAsyncWork();
  assert.equal(elements.textOnlyTextBody.textContent, "", "a response from the logged-out generation is ignored");

  harness.setSession(session());
  harness.emitAuthChange();
  elements.viewTextOnlyText.trigger("click");
  harness.respond({
    text: "<script>alert('shown only as text')</script>",
    source_label: "<b>提取来源</b>",
    has_more: false,
    next_cursor: "",
  });
  await flushAsyncWork();
  assert.equal(elements.textOnlyTextBody.textContent, "<script>alert('shown only as text')</script>");
  assert.equal(elements.textOnlyTextSource.textContent, "<b>提取来源</b>");
  assert.equal(elements.textOnlyTextContent.hidden, false);

  harness.setSession(session("token-refreshed"));
  harness.emitAuthChange();
  assert.equal(
    elements.textOnlyTextBody.textContent,
    "<script>alert('shown only as text')</script>",
    "refreshing the token for the same identity must not clear visible text",
  );
});

test("Text only handles stale 401, current 401, and 403 without leaking prior content", async () => {
  const harness = createHarness(session("token-a"));
  const { elements } = harness;
  elements.viewTextOnlyText.trigger("click");
  harness.setSession(session("token-b"));
  harness.emitAuthChange();
  harness.respond({ detail: "expired old token" }, 401);
  await flushAsyncWork();
  assert.equal(harness.getSession().token, "token-b", "an old 401 must not clear a newer session token");
  assert.equal(harness.clearedSessions, 0);
  assert.match(elements.textOnlyTextStatus.textContent, /登录状态已更新/u);

  elements.viewTextOnlyText.trigger("click");
  harness.respond({ text: "restricted page one", source_label: "source", has_more: true, next_cursor: "c1" });
  await flushAsyncWork();
  assert.equal(elements.textOnlyTextBody.textContent, "restricted page one");
  elements.loadMoreTextOnlyText.trigger("click");
  harness.respond({ detail: "forbidden" }, 403);
  await flushAsyncWork();
  assert.equal(elements.textOnlyTextBody.textContent, "", "403 revocation clears already displayed protected text");
  assert.equal(elements.textOnlyTextContent.hidden, true);
  assert.equal(harness.getSession().token, "token-b", "403 keeps the valid signed-in session");
  assert.match(elements.textOnlyTextStatus.textContent, /时长不足/u);
  assert.match(elements.textOnlyTextStatus.textContent, /报告 \/ 机构不在授权范围/u);

  elements.viewTextOnlyText.trigger("click");
  harness.respond({ detail: "expired" }, 401);
  await flushAsyncWork();
  assert.equal(harness.getSession(), null);
  assert.equal(harness.clearedSessions, 1);
  assert.match(elements.textOnlyTextStatus.textContent, /请先注册或登录/u);
});

test("Text only joins valid pages and rejects missing or looping cursors", async () => {
  const harness = createHarness(session());
  const { elements } = harness;
  elements.viewTextOnlyText.trigger("click");
  harness.respond({
    report_id: "report-1",
    text: "page-1",
    source_label: "source",
    has_more: true,
    next_cursor: "c1",
  });
  await flushAsyncWork();
  elements.loadMoreTextOnlyText.trigger("click");
  harness.respond({ text: "|page-2", source_label: "source", has_more: true, next_cursor: "c2" });
  await flushAsyncWork();
  elements.loadMoreTextOnlyText.trigger("click");
  harness.respond({ text: "|page-3", source_label: "source", has_more: false, next_cursor: "" });
  await flushAsyncWork();
  assert.equal(elements.textOnlyTextBody.textContent, "page-1|page-2|page-3");
  assert.equal(elements.loadMoreTextOnlyText.hidden, true);
  assert.match(elements.textOnlyTextStatus.textContent, /全部加载/u);

  const missing = createHarness(session());
  missing.elements.viewTextOnlyText.trigger("click");
  missing.respond({ text: "must-not-append", source_label: "source", has_more: true, next_cursor: "" });
  await flushAsyncWork();
  assert.equal(missing.elements.textOnlyTextBody.textContent, "");
  assert.equal(missing.elements.textOnlyTextContent.hidden, true);
  assert.match(missing.elements.textOnlyTextStatus.textContent, /没有返回下一页游标/u);

  const looping = createHarness(session());
  looping.elements.viewTextOnlyText.trigger("click");
  looping.respond({ text: "page-1", source_label: "source", has_more: true, next_cursor: "c1" });
  await flushAsyncWork();
  looping.elements.loadMoreTextOnlyText.trigger("click");
  looping.respond({ text: "duplicate", source_label: "source", has_more: true, next_cursor: "c1" });
  await flushAsyncWork();
  assert.equal(looping.elements.textOnlyTextBody.textContent, "page-1");
  assert.equal(looping.elements.loadMoreTextOnlyText.hidden, true);
  assert.match(looping.elements.textOnlyTextStatus.textContent, /游标发生循环/u);

  const mismatched = createHarness(session());
  mismatched.elements.viewTextOnlyText.trigger("click");
  mismatched.respond({
    report_id: "another-report",
    text: "must-not-append",
    source_label: "source",
    has_more: false,
    next_cursor: "",
  });
  await flushAsyncWork();
  assert.equal(mismatched.elements.textOnlyTextBody.textContent, "");
  assert.equal(mismatched.elements.textOnlyTextContent.hidden, true);
  assert.match(mismatched.elements.textOnlyTextStatus.textContent, /报告不匹配/u);
});

test("Text only markup and mobile styles expose a clear, responsive entry", () => {
  const markup = extractFunction(app, "textOnlyTextAccessMarkup");
  const init = extractFunction(app, "initTextOnlyTextAccess");
  assert.match(markup, /原始文本（Text only）/u);
  assert.match(markup, /没有可下载 PDF/u);
  assert.match(markup, /报告在账号授权范围内/u);
  assert.match(init, /body\.textContent \+= chunk/u);
  assert.match(init, /source\.textContent =/u);
  assert.doesNotMatch(init, /body\.innerHTML|source\.innerHTML|status\.innerHTML/u);
  assert.match(styles, /\.text-only-text-content pre \{[\s\S]*min-width: 0;[\s\S]*max-width: 100%;/u);
  assert.match(styles, /@media \(max-width: 760px\)[\s\S]*\.text-only-text-actions \{[\s\S]*flex-direction: column;/u);
});
