import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import path from "node:path";
import test from "node:test";
import vm from "node:vm";
import { fileURLToPath } from "node:url";

const root = path.resolve(path.dirname(fileURLToPath(import.meta.url)), "../..");
const source = await readFile(path.join(root, "portal_suite/site_src/assets/report-chat.js"), "utf8");

class FakeElement {
  constructor(id = "") {
    this.id = id;
    this.value = "";
    this.textContent = "";
    this.innerHTML = "";
    this.className = "";
    this.disabled = false;
    this.hidden = false;
    this.removed = false;
    this.style = {};
    this.attributes = new Map();
    this.listeners = new Map();
    this.childrenBySelector = new Map();
    this.submitButton = null;
    this.insertedElement = null;
    this.classList = {
      add: (value) => {
        const values = new Set(this.className.split(/\s+/u).filter(Boolean));
        values.add(value);
        this.className = [...values].join(" ");
      },
      remove: (value) => {
        this.className = this.className.split(/\s+/u).filter((item) => item && item !== value).join(" ");
      },
      contains: (value) => this.className.split(/\s+/u).includes(value),
    };
  }

  addEventListener(type, listener) {
    const values = this.listeners.get(type) || [];
    values.push(listener);
    this.listeners.set(type, values);
  }

  async dispatch(type, event = {}) {
    const normalized = { preventDefault() {}, target: this, ...event };
    return Promise.all((this.listeners.get(type) || []).map((listener) => listener(normalized)));
  }

  querySelector(selector) {
    if (selector === "button[type=submit]") return this.submitButton;
    if (!this.childrenBySelector.has(selector)) this.childrenBySelector.set(selector, new FakeElement(selector));
    return this.childrenBySelector.get(selector);
  }

  insertAdjacentElement(_position, element) {
    this.insertedElement = element;
    return element;
  }

  setAttribute(name, value) {
    this.attributes.set(name, String(value));
  }

  getAttribute(name) {
    return this.attributes.get(name) || null;
  }

  remove() {
    this.removed = true;
  }
}

function createScheduler() {
  let nextId = 1;
  const timeouts = new Map();
  const intervals = new Map();
  return {
    setTimeout(callback, delay) {
      const id = nextId++;
      timeouts.set(id, { callback, delay });
      return id;
    },
    clearTimeout(id) { timeouts.delete(id); },
    setInterval(callback, delay) {
      const id = nextId++;
      intervals.set(id, { callback, delay });
      return id;
    },
    clearInterval(id) { intervals.delete(id); },
    runTimeout(delay) {
      const entry = [...timeouts.entries()].find(([, value]) => value.delay === delay);
      assert.ok(entry, `missing timeout scheduled for ${delay}ms`);
      timeouts.delete(entry[0]);
      entry[1].callback();
    },
  };
}

function createHarness() {
  const form = new FakeElement("homeChatForm");
  const button = new FakeElement("homeChatSubmit");
  button.textContent = "开始查找";
  form.submitButton = button;
  const input = new FakeElement("homeChatInput");
  input.value = "最近的 AI 数据中心报告";
  const status = new FakeElement("homeChatStatus");
  const messages = new FakeElement("homeChatMessages");
  const recommendations = new FakeElement("homeChatRecommendations");
  messages.innerHTML = "旧答案";
  recommendations.innerHTML = "旧推荐";
  const elements = { homeChatForm: form, homeChatInput: input, homeChatStatus: status, homeChatMessages: messages, homeChatRecommendations: recommendations };
  const scheduler = createScheduler();
  const fetches = [];
  const fetch = (_url, options) => new Promise((resolve, reject) => {
    const request = {
      options,
      resolve(payload, init = {}) {
        resolve({ ok: init.ok !== false, status: init.status || 200, json: async () => payload });
      },
    };
    options.signal.addEventListener("abort", () => reject(new DOMException("Aborted", "AbortError")), { once: true });
    fetches.push(request);
  });
  const document = {
    readyState: "complete",
    getElementById(id) { return elements[id] || null; },
    createElement() { return new FakeElement(); },
    addEventListener() {},
  };
  const window = {
    setTimeout: scheduler.setTimeout,
    clearTimeout: scheduler.clearTimeout,
    setInterval: scheduler.setInterval,
    clearInterval: scheduler.clearInterval,
  };
  const localStorage = {
    getItem() { return JSON.stringify({ token: "session-token", user: { email: "reader@example.com" } }); },
  };
  vm.runInNewContext(source, {
    AbortController,
    Date,
    DOMException,
    Event,
    console,
    document,
    encodeURIComponent,
    fetch,
    localStorage,
    window,
  }, { filename: "report-chat.js" });
  return { button, fetches, form, messages, recommendations, scheduler, status };
}

test("report chat shows immediate staged feedback and atomically replaces old results on success", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");

  assert.equal(harness.fetches.length, 1);
  assert.equal(harness.button.disabled, true);
  assert.equal(harness.button.textContent, "正在查找…");
  assert.equal(harness.form.getAttribute("aria-busy"), "true");
  assert.equal(harness.form.insertedElement.getAttribute("aria-live"), null);
  assert.match(source, /data-chat-progress-label role="status" aria-live="polite"/u);
  assert.match(source, /data-chat-progress-time aria-hidden="true"/u);
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-label]").textContent, "检索目录");
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-bar]").style.width, "24%");
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");

  await harness.form.dispatch("submit");
  assert.equal(harness.fetches.length, 1, "a duplicate submit must not start another request");
  assert.match(harness.status.textContent, /仍在进行/u);

  harness.fetches[0].resolve({
    answer: "新答案",
    recommendations: [
      { id: "report-1", title: "新报告", attraction_score: 5, available: false },
      { id: "report-2", title: "状态待确认报告", attraction_score: 4 },
    ],
    usage: { remaining: 2 },
  });
  await submit;

  assert.match(harness.messages.innerHTML, /新答案/u);
  assert.match(harness.recommendations.innerHTML, /新报告/u);
  assert.match(harness.recommendations.innerHTML, /available=false/u);
  const unknownHref = harness.recommendations.innerHTML.match(/href="([^"]*id=report-2[^"]*)"/u);
  assert.ok(unknownHref);
  assert.doesNotMatch(unknownHref[1], /available=/u);
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-label]").textContent, "推荐已生成");
  assert.equal(harness.form.insertedElement.querySelector("[data-chat-progress-bar]").style.width, "100%");
  assert.equal(harness.button.textContent, "开始查找");
  assert.equal(harness.button.disabled, false);
  assert.equal(harness.form.getAttribute("aria-busy"), "false");
});

test("report chat cancellation aborts the request and preserves old results", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  const cancel = harness.form.insertedElement.querySelector("[data-chat-cancel]");

  await cancel.dispatch("click");
  await submit;

  assert.equal(harness.fetches[0].options.signal.aborted, true);
  assert.match(harness.status.textContent, /已取消本次查找/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.button.textContent, "开始查找");
});

test("report chat distinguishes a 20 second timeout and allows retry", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");

  harness.scheduler.runTimeout(20_000);
  await submit;

  assert.match(harness.status.textContent, /超过 20 秒/u);
  assert.match(harness.status.textContent, /点击重试/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.button.disabled, false);
});

test("report chat shows server diagnostics without discarding the previous result", async () => {
  const harness = createHarness();
  const submit = harness.form.dispatch("submit");
  harness.fetches[0].resolve({ detail: "上游服务暂时不可用", stage_code: "MODEL", request_hint: "ABC123" }, { ok: false, status: 503 });
  await submit;

  assert.match(harness.status.textContent, /上游服务暂时不可用/u);
  assert.match(harness.status.textContent, /HTTP 503/u);
  assert.match(harness.status.textContent, /点击重试/u);
  assert.equal(harness.messages.innerHTML, "旧答案");
  assert.equal(harness.recommendations.innerHTML, "旧推荐");
  assert.equal(harness.form.insertedElement.getAttribute("data-state"), "error");
});

test("report chat source contains all three visible progress stages and no wait cursor", () => {
  assert.match(source, /检索目录/u);
  assert.match(source, /整理候选/u);
  assert.match(source, /生成推荐/u);
  assert.doesNotMatch(source, /cursor\s*:\s*wait/u);
});
