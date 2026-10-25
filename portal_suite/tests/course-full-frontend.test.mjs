import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import vm from "node:vm";
import test from "node:test";

const source = await readFile(new URL("../site_src/assets/course-full.js", import.meta.url), "utf8");
const html = await readFile(new URL("../site_src/course-full.html", import.meta.url), "utf8");
const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const member = { user: { id: "example-member", email: "member@example.invalid" }, token: "test-member-token" };
const allowed = { allowed: true, since: "2026-08-01T00:00:00Z", eligible_at: "2026-10-01T00:00:00Z", reason: "eligible" };
const item = { id: "example-directory-id", name: "Example lesson.pdf", folders: ["Example folder", "Example module"], extension: "pdf", size_label: "1 MB", date: "2026-01-01" };
const directory = (items = [item], overrides = {}) => ({ items, total: items.length, page: 1, page_size: 30, has_more: false, facets: { folders: [{ name: "Example folder", count: 1 }], file_types: [{ name: "pdf", count: 1 }] }, generated_at: "2026-10-25T00:00:00Z", ...overrides });
const response = (body, status = 200) => new Response(JSON.stringify(body), { status });

function harness(t, initialSession = member, handler = (url) => url.endsWith("/access") ? response(allowed) : response(directory())) {
  class Element {
    constructor(tag) { this.tagName = tag; this.children = []; this.dataset = {}; this.handlers = new Map(); this.attributes = {}; this.value = ""; this.hidden = false; this.disabled = false; this.text = ""; }
    get textContent() { return this.text + this.children.map((child) => child.textContent).join(""); }
    set textContent(value) { this.text = String(value); this.children = []; }
    append(...children) { for (const child of children) { child.parentElement = this; this.children.push(child); } }
    replaceChildren(...children) { this.children = []; this.text = ""; this.append(...children); }
    setAttribute(name, value) { this.attributes[name] = value; }
    reportValidity() { return this.valid !== false; }
    focus() { this.focused = true; }
    addEventListener(name, callback) { this.handlers.set(name, callback); }
    removeEventListener(name, callback) { if (this.handlers.get(name) === callback) this.handlers.delete(name); }
    fire(name, data = {}) { return this.handlers.get(name)?.({ preventDefault() {}, target: this, ...data }); }
  }
  const elements = new Map();
  for (const match of html.matchAll(/id="courseFull(\w+)"/g)) elements.set(match[1], new Element("div"));
  const gate = new Element("section"); gate.append(elements.get("GateTitle"));
  const root = elements.get("App"); root.querySelector = (selector) => elements.get(selector.replace("#courseFull", ""));
  const documentEvents = new Map(), windowEvents = new Map(), dispatched = [], calls = [], analytics = [];
  const document = { readyState: "loading", createElement: (tag) => new Element(tag), getElementById: (id) => id === "courseFullApp" ? root : null,
    addEventListener(name, callback) { documentEvents.set(name, callback); }, removeEventListener(name) { documentEvents.delete(name); },
    dispatchEvent(event) { dispatched.push(event); documentEvents.get(event.type)?.(event); },
  };
  let stored = initialSession;
  const window = { document, location: { pathname: "/course-full.html", href: "https://kcdesk.com/course-full.html?private=omitted" },
    PortalSuiteAnalytics: { track(type, data) { analytics.push({ type, ...JSON.parse(JSON.stringify(data)) }); } },
    localStorage: { getItem() { return JSON.stringify(stored); } },
    setTimeout() { return 1; }, clearTimeout() {},
    addEventListener(name, callback) { windowEvents.set(name, callback); }, removeEventListener(name) { windowEvents.delete(name); },
    async fetch(url, options) { calls.push({ url, options }); return handler(url, options); },
  };
  vm.runInNewContext(source, { window, document, URLSearchParams, AbortController, Intl, CustomEvent: class { constructor(type, options) { this.type = type; this.detail = options.detail; } } });
  const instance = window.PortalCourseFull.mount();
  t.after(() => instance.destroy());
  return { window, calls, dispatched, gate, root, instance, analytics,
    el: (name) => elements.get(name),
    setSession(value, storage = false) { stored = value; return storage ? windowEvents.get("storage")?.({ key: "portal_auth_session" }) : documentEvents.get("portal-auth-change")?.(); },
    async settle() { await new Promise((resolve) => setImmediate(resolve)); },
    requestButton() { return elements.get("Items").children[0]?.children[1]; },
  };
}

test("standalone Course page reuses the established account bootstrap and has no static inventory", () => {
  assert.match(html, /data-page="course-full"/);
  assert.match(html, /name="robots" content="noindex,nofollow,noarchive"/);
  assert.match(html, /id="courseFullDirectory"[^>]*hidden/);
  assert.match(app, /page === "course-full"[\s\S]{0,100}initContentAccount/);
  assert.doesNotMatch(html, /Example lesson|directory_item_id|source_filename|_course-directory/);
  assert.doesNotMatch(source, /\.innerHTML\s*=|createObjectURL|\.blob\(|window\.open\(|location\.assign/);
});

test("anonymous users load no private data and login opens the existing account control", async (t) => {
  const h = harness(t, null); await h.settle();
  assert.equal(h.calls.length, 0);
  assert.equal(h.el("Directory").hidden, true);
  assert.equal(h.el("Login").hidden, false);
  h.el("Login").fire("click");
  assert.equal(h.dispatched[0].type, "portal-open-auth");
  assert.equal(h.dispatched[0].detail.mode, "login");
  assert.equal(h.dispatched[0].detail.placement, "course_full");
  assert.deepEqual(h.analytics.map(({ action, status }) => [action, status]), [["access_start", "guest"], ["login_click", ""]]);
});

test("unverified history and incomplete tenure show dates without fetching the directory", async (t) => {
  for (const reason of ["needs_history_verification", "tenure_incomplete", "membership_inactive"]) {
    const h = harness(t, member, () => response({ ...allowed, allowed: false, reason })); await h.settle();
    assert.equal(h.calls.length, 1);
    assert.equal(h.calls[0].url, "/api/course/full/access");
    assert.equal(h.el("Directory").hidden, true);
    assert.equal(h.el("Verify").hidden, false);
    assert.match(h.el("Dates").textContent, /北京时间/);
    if (reason === "needs_history_verification") assert.match(h.el("GateTitle").textContent, /历史需要核验/);
    if (reason === "tenure_incomplete") assert.match(h.el("GateTitle").textContent, /尚未满两个月/);
    assert.equal(h.analytics.at(-1).action, "access_result");
    assert.equal(h.analytics.at(-1).status, "denied");
    assert.equal(h.analytics.at(-1).access_state, reason);
  }
});

test("authorized users receive plain original names and server-driven filters and pages", async (t) => {
  const unusual = { ...item, name: '<img src=x onerror=alert(1)> Original & name.pdf', folders: ["Folder <A>", "原始目录"] };
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : response(directory([unusual], { total: 42, page: Number(new URL(url, "https://kcdesk.com").searchParams.get("page")), has_more: true })));
  await h.settle();
  assert.equal(h.calls.length, 2);
  assert.equal(h.calls[1].options.headers.Authorization, "Bearer test-member-token");
  assert.equal(h.calls[1].options.cache, "no-store");
  assert.equal(h.el("Directory").hidden, false);
  assert.match(h.el("Items").textContent, /<img src=x onerror=alert\(1\)> Original & name\.pdf/);
  assert.match(h.el("Items").textContent, /Folder <A> \/ 原始目录/);
  assert.equal(h.el("Items").children[0].children[0].children[0].tagName, "h3");
  h.el("Search").value = "cash & debt"; h.el("Folder").value = "Folder <A>"; h.el("Type").value = "pdf";
  await h.el("Filters").fire("submit"); await h.settle();
  const filtered = new URL(h.calls.at(-1).url, "https://kcdesk.com");
  assert.equal(filtered.searchParams.get("q"), "cash & debt");
  assert.equal(filtered.searchParams.get("folder"), "Folder <A>");
  assert.equal(filtered.searchParams.get("file_type"), "pdf");
  h.el("Next").fire("click"); await h.settle();
  assert.match(h.calls.at(-1).url, /page=2/);
  assert.equal(h.el("PageLabel").textContent, "第 2 页");
  assert.deepEqual(h.analytics.slice(0, 4).map(({ action, status }) => [action, status]), [
    ["access_start", "pending"], ["access_result", "success"], ["directory_start", "pending"], ["directory_result", "success"],
  ]);
  assert.equal(h.analytics.at(-1).result_count, 1);
  assert.ok(h.analytics.every((event) => event.type === "journey_interaction" && event.placement === "course_full" && event.measurement_version === "journey-v1"));
  assert.doesNotMatch(JSON.stringify(h.analytics), /Example|Original & name|原始目录|Folder <A>|cash & debt|member@example|test-member-token|private=|directory_item_id|"query"|"folder"/);
});

test("missing catalog is explicitly unavailable and never presented as a complete empty inventory", async (t) => {
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : response({ error: "catalog_unavailable" }, 503));
  await h.settle();
  assert.match(h.el("Status").textContent, /暂时不可用/);
  assert.doesNotMatch(h.el("Status").textContent, /没有匹配|找到 0|完整/);
  assert.equal(h.el("Items").children.length, 0);
  assert.equal(h.el("Pagination").hidden, true);
  assert.equal(h.analytics.at(-1).action, "directory_result");
  assert.equal(h.analytics.at(-1).status, "error");
  assert.equal(h.analytics.at(-1).error, "unavailable");
});

test("one item request is authenticated, deduplicated in flight, and never downloads a file", async (t) => {
  let finish;
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : url.includes("directory?") ? response(directory()) : new Promise((resolve) => { finish = resolve; }));
  await h.settle();
  const button = h.requestButton(); const first = button.fire("click"); await h.settle();
  await button.fire("click");
  const requests = h.calls.filter((call) => call.options.method === "POST");
  assert.equal(requests.length, 1);
  assert.equal(requests[0].url, "/api/course/full/directory-request");
  assert.deepEqual(JSON.parse(requests[0].options.body), { directory_item_id: item.id, page_path: "/course-full.html", honeypot: "" });
  assert.equal(requests[0].options.headers.Authorization, "Bearer test-member-token");
  finish(response({ ok: true, deduplicated: true }, 202)); await first;
  assert.equal(button.textContent, "申请已记录"); assert.equal(button.disabled, true);
  assert.match(h.el("RequestStatus").textContent, /Request received/);
  await button.fire("click"); assert.equal(h.calls.length, 3);
  assert.equal(h.analytics.filter(({ action }) => action === "request_submit").length, 1);
  const result = h.analytics.find(({ action }) => action === "request_result");
  assert.equal(result.status, "deduplicated"); assert.equal(result.deduplicated, true);
  assert.equal(result.acknowledgement_status, "unknown");
  assert.doesNotMatch(JSON.stringify(h.analytics), /Example|example-directory-id|member@example|test-member-token|private=/);
});

test("request failures preserve a retry action, including a row rerendered while pending", async (t) => {
  let finish;
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : url.includes("directory?") ? response(directory()) : new Promise((resolve) => { finish = resolve; }));
  await h.settle();
  const first = h.requestButton().fire("click"); await h.settle();
  h.el("Filters").fire("submit"); await h.settle();
  assert.equal(h.requestButton().disabled, true);
  finish(response({ detail: "Please retry later." }, 502)); await first;
  assert.equal(h.requestButton().disabled, false);
  assert.equal(h.requestButton().textContent, "重新申请");
  assert.equal(h.el("RequestStatus").dataset.state, "error");
  assert.equal(h.analytics.at(-1).action, "request_result");
  assert.equal(h.analytics.at(-1).status, "error");
  assert.equal(h.analytics.at(-1).error, "unavailable");
  assert.doesNotMatch(JSON.stringify(h.analytics), /Please retry later/);
});

test("legacy accounts can supply a reply email while real account emails remain authoritative", async (t) => {
  for (const address of ["legacy@users.portal.example.invalid", "legacy@users.example.invalid", ""]) {
    const legacy = { ...member, user: { ...member.user, email: address } };
    const h = harness(t, legacy, (url) => url.endsWith("/access") ? response(allowed) : url.includes("directory?") ? response(directory()) : response({ ok: true }, 202));
    await h.settle(); assert.equal(h.el("Reply").hidden, false);
    await h.requestButton().fire("click"); assert.equal(h.calls.length, 2);
    h.el("ReplyEmail").value = "reply@example.net";
    await h.requestButton().fire("click");
    assert.equal(JSON.parse(h.calls.at(-1).options.body).requester_email, "reply@example.net");
    assert.equal(h.requestButton().textContent, "申请已提交");
    assert.equal(h.analytics.at(-1).action, "request_result");
    assert.equal(h.analytics.at(-1).status, "success");
    assert.doesNotMatch(JSON.stringify(h.analytics), /reply@example|legacy@|Example lesson|example-directory-id/);
  }
  const h = harness(t); await h.settle();
  assert.equal(h.el("Reply").hidden, true);
});

test("an unsuccessful response body cannot produce a submitted claim", async (t) => {
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : url.includes("directory?") ? response(directory()) : response({ ok: false }));
  await h.settle(); await h.requestButton().fire("click");
  assert.equal(h.requestButton().disabled, false);
  assert.equal(h.requestButton().textContent, "重新申请");
  assert.match(h.el("RequestStatus").textContent, /暂未确认/);
});

test("logout clears private content and stale directory results cannot repopulate it", async (t) => {
  let finish;
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : new Promise((resolve) => { finish = resolve; }));
  await h.settle();
  assert.equal(h.calls.length, 2);
  h.setSession(null, true); await h.settle();
  finish(response(directory())); await h.settle();
  assert.equal(h.el("Items").children.length, 0);
  assert.equal(h.el("Directory").hidden, true);
  assert.equal(h.el("Login").hidden, false);
  assert.equal(h.el("Retry").disabled, false);
  assert.equal(h.calls[1].options.signal.aborted, true);
});

test("expired sessions and a later access denial clear directory data", async (t) => {
  const expired = harness(t, member, () => response({ detail: "Expired" }, 401)); await expired.settle();
  assert.equal(expired.calls.length, 1); assert.equal(expired.el("Login").hidden, false);
  let deny = false;
  const h = harness(t, member, (url) => url.endsWith("/access") ? response(allowed) : deny ? response({ ...allowed, allowed: false, reason: "membership_inactive" }, 403) : response(directory()));
  await h.settle(); assert.equal(h.el("Items").children.length, 1);
  deny = true; h.el("Filters").fire("submit"); await h.settle();
  assert.equal(h.el("Directory").hidden, true); assert.equal(h.el("Items").children.length, 0);
});

test("mounting twice adds no duplicate fetch or listeners", async (t) => {
  const h = harness(t); await h.settle();
  assert.equal(h.window.PortalCourseFull.mount(h.root), h.instance);
  assert.equal(h.calls.length, 2);
  h.el("Verify").fire("click");
  assert.equal(h.analytics.filter(({ action }) => action === "verify_click").length, 1);
  h.instance.destroy(); h.el("Verify").fire("click");
  assert.equal(h.analytics.filter(({ action }) => action === "verify_click").length, 1);
  const next = h.window.PortalCourseFull.mount(h.root); t.after(() => next.destroy());
  h.el("Verify").fire("click");
  assert.equal(h.analytics.filter(({ action }) => action === "verify_click").length, 2);
});
