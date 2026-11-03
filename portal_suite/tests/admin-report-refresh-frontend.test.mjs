import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const source = await readFile(new URL("../site_src/assets/admin-report-refresh.js", import.meta.url), "utf8");
const app = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const { mountAdminReportRefresh } = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);

function element() {
  const listeners = new Map();
  return {
    disabled: false, hidden: false, className: "", textContent: "", innerHTML: "",
    addEventListener(name, fn) { listeners.set(name, fn); },
    removeEventListener(name, fn) { if (listeners.get(name) === fn) listeners.delete(name); },
    async emit(name) { return listeners.get(name)?.({}); },
  };
}
function fixture(responses, { hidden = false, existing = true } = {}) {
  const button = element(), check = element(), status = element(), updated = element(), doc = element();
  doc.hidden = hidden;
  const section = element();
  const parts = { accountAdminReportRefresh: button, accountAdminReportRefreshCheck: check,
    accountAdminReportRefreshStatus: status, accountAdminReportRefreshUpdated: updated };
  section.querySelector = (selector) => parts[selector.slice(1)] || null;
  let attached = existing;
  const anchor = { after(node) { assert.equal(node, section); attached = true; } };
  doc.createElement = (tag) => { assert.equal(tag, "section"); return section; };
  const root = { ownerDocument: doc, isConnected: true,
    querySelector: (selector) => selector === "#accountAdminReportRefreshSection" ? (attached ? section : null)
      : selector === "#accountAdminStatus" ? anchor : null };
  const calls = [], timers = new Map(); let timerId = 0;
  const scheduler = {
    setTimeout(fn, delay) { const id = ++timerId; timers.set(id, { fn, delay }); return id; },
    clearTimeout(id) { timers.delete(id); },
  };
  async function fetch(url, options) {
    calls.push({ url, options });
    const next = responses.shift();
    if (next instanceof Error) throw next;
    if (typeof next === "function") return next(options);
    assert.ok(next, "An unexpected network request was made");
    return { ok: next.httpStatus ? next.httpStatus < 400 : true, status: next.httpStatus || 200, json: async () => next };
  }
  const controls = mountAdminReportRefresh({ root, workerUrl: "/api", authHeaders: () => ({ Authorization: "Bearer admin-session" }),
    fetch, scheduler, formatDateTime: (value) => value ? `BJT:${value}` : "" });
  async function settle() { for (let i = 0; i < 12; i++) await Promise.resolve(); }
  async function poll() {
    const entry = [...timers].find(([, timer]) => timer.delay === 30000);
    assert.ok(entry, "Active refresh should have a bounded status timer");
    timers.delete(entry[0]); await entry[1].fn(); await settle();
  }
  return { button, check, status, updated, section, doc, root, calls, timers, controls, settle, poll };
}
const idle = { state: "idle", can_refresh: true, run: null };

test("the Reports tool is limited to the super-admin view and loaded on demand", () => {
  assert.match(app, /if \(isSuperSession\(session\)\) import\("\/assets\/admin-report-refresh\.js\?v=/);
  assert.match(app, /modal\.__reportRefreshControls\?\.close\(\)/);
  assert.match(source, /从 Dropbox 刷新 Reports/);
});

test("an accepted request stays busy until the actual workflow reports success", async () => {
  const f = fixture([idle,
    { state: "requested", can_refresh: false, requested_at: "2026-11-03T04:00:00Z", run: null },
    { state: "in_progress", can_refresh: false, run: { status: "in_progress", conclusion: null } },
    { state: "completed", can_refresh: true, run: { status: "completed", conclusion: "success" }, last_success_at: "2026-11-03T05:00:00Z" },
  ]);
  await f.settle();
  assert.equal(f.button.disabled, false);
  await f.button.emit("click");
  assert.equal(f.calls[1].options.method, "POST");
  assert.equal(f.calls[1].options.headers.Authorization, "Bearer admin-session");
  assert.equal(f.calls[1].options.body, "{}");
  assert.equal(f.button.disabled, true);
  assert.doesNotMatch(f.status.className, /\bok\b/);
  assert.match(f.status.textContent, /完成后/);
  await f.button.emit("click");
  assert.equal(f.calls.length, 2, "A second click must not submit another refresh");
  await f.poll();
  assert.match(f.status.textContent, /正在从 Dropbox/);
  assert.equal(f.button.disabled, true);
  await f.poll();
  assert.equal(f.status.className, "status-line ok");
  assert.match(f.status.textContent, /刷新已完成/);
  assert.match(f.updated.textContent, /最近刷新成功（北京时间）：BJT:2026-11-03T05:00:00Z/);
  assert.equal(f.button.disabled, false);
  assert.equal([...f.timers.values()].some((t) => t.delay === 30000), false);
  f.controls.close();
});

test("a POST transport failure is checked with GET and never automatically submitted again", async () => {
  const f = fixture([idle, new Error("connection closed"),
    { state: "idle", can_refresh: true, run: null },
    { state: "pending", can_refresh: false, requested_at: "now", run: { status: "queued", conclusion: null } },
  ]);
  await f.settle(); await f.button.emit("click");
  assert.equal(f.button.disabled, true);
  assert.match(f.status.textContent, /不会重复提交/);
  await f.poll();
  assert.equal(f.button.disabled, true, "An empty read does not prove that the POST was rejected");
  await f.button.emit("click");
  await f.check.emit("click");
  assert.equal(f.calls.filter((call) => call.options.method === "POST").length, 1);
  assert.equal(f.calls.filter((call) => call.options.method === "GET").length, 3);
  assert.equal(f.button.disabled, true);
  f.controls.close();
});

test("status reads pause while the page is hidden and clean up when the modal closes", async () => {
  const f = fixture([{ state: "pending", can_refresh: false, run: { status: "queued" } }], { hidden: true });
  await f.settle();
  assert.equal(f.calls.length, 0);
  f.doc.hidden = false; await f.doc.emit("visibilitychange"); await f.settle();
  assert.equal(f.calls.length, 1);
  f.doc.hidden = true; await f.doc.emit("visibilitychange");
  assert.equal(f.timers.size, 0);
  f.controls.close();
  f.doc.hidden = false; await f.doc.emit("visibilitychange");
  await f.button.emit("click"); await f.check.emit("click");
  assert.equal(f.calls.length, 1);
});

test("failed runs remain visibly failed and allow a deliberate retry", async () => {
  const f = fixture([{ state: "completed", can_refresh: true, run: { status: "completed", conclusion: "failure" } }]);
  await f.settle();
  assert.equal(f.status.className, "status-line error");
  assert.match(f.status.textContent, /未完成/);
  assert.equal(f.button.disabled, false);
  f.controls.close();
});

test("expired administrator access hides the tool instead of leaving a usable action", async () => {
  const f = fixture([{ httpStatus: 403, message: "Admin access denied" }]);
  await f.settle();
  assert.equal(f.section.hidden, true);
  assert.equal(f.button.disabled, true);
  assert.equal(f.timers.size, 0);
  f.controls.close();
});

test("a reconciled unknown result allows a deliberate retry only after the server enables it", async () => {
  const f = fixture([{ state: "unknown", can_refresh: false, requested_at: "earlier", run: null },
    { state: "unknown", can_refresh: true, requested_at: "earlier", run: null,
      message: "尚未找到对应的刷新任务，可以重新发起并继续核验。" },
  ]);
  await f.settle();
  assert.equal(f.button.disabled, true);
  await f.poll();
  assert.equal(f.button.disabled, false);
  assert.match(f.status.textContent, /可以重新发起/);
  assert.equal(f.calls.filter((call) => call.options.method === "POST").length, 0);
  f.controls.close();
});

test("the lazy tool inserts its controls at the top of the management content", async () => {
  const f = fixture([idle], { existing: false });
  await f.settle();
  assert.equal(f.root.querySelector("#accountAdminReportRefreshSection"), f.section);
  assert.equal(f.section.className, "account-admin-section");
  assert.match(f.section.innerHTML, /从 Dropbox 刷新 Reports/);
  assert.equal(f.button.disabled, false);
  f.controls.close();
});
