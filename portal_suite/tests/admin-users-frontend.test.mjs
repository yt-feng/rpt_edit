import assert from 'node:assert/strict';
import { readFile } from 'node:fs/promises';
import test from 'node:test';
import vm from 'node:vm';

const app = await readFile(new URL('../site_src/assets/app.js', import.meta.url), 'utf8');
const source = await readFile(new URL('../site_src/assets/admin-users.js', import.meta.url), 'utf8');
function extract(name) {
  const start = app.indexOf(`function ${name}(`), begin = app.indexOf('{', app.indexOf(')', start));
  assert.ok(start >= 0);
  let depth = 0;
  for (let i = begin; i < app.length; i++) {
    if (app[i] === '{') depth++;
    if (app[i] === '}' && --depth === 0) return app.slice(app.slice(start - 6, start) === 'async ' ? start - 6 : start, i + 1);
  }
  throw new Error(name);
}
function runtime(extra = {}) {
  const context = vm.createContext({ AbortController, URL, Date, Map, Set, ...extra,
    setTimeout: (fn, ms) => ms === 500 ? (fn(), 1) : 1, clearTimeout() {},
  });
  vm.runInContext(source.replaceAll('export ', '') + '\nglobalThis.api = { fetchFreshAdminUsers, adminUserPage, renderAdminUserTable, saveAdminNewsfeed, mountAdminInlineEditor, closeAdminInlineEditor, adminNewsfeedLabel, bindNewsfeedEditor, fillAdminNewsfeedEditor };', context);
  return context;
}
const response = (body, status = 200) => ({ ok: status < 400, status, json: async () => body });
const user = (i) => ({ id: `user-${i}`, email: `user${i}@example.invalid`, username: `User ${i}` });

test('complete user collection reads all 624 users across seven bounded pages', async () => {
  const calls = [];
  const ctx = runtime({ async fetch(url, options) {
    const parsed = new URL(url); const page = Number(parsed.searchParams.get('cursor') || 0);
    assert.equal(parsed.searchParams.get('page_size'), page === 0 ? null : '100');
    if (page === 0) assert.equal(parsed.searchParams.get('view'), 'directory');
    assert.equal(options.cache, 'no-store');
    calls.push(page);
    return response({ verified: true, users: Array.from({ length: page === 6 ? 24 : 100 }, (_, i) => user(page * 100 + i)), complete: page === 6, has_more: page < 6, next_cursor: page < 6 ? String(page + 1) : '' });
  } });
  const result = await ctx.api.fetchFreshAdminUsers('https://worker.test', { Authorization: 'synthetic' });
  assert.equal(result.users.length, 624);
  assert.equal(result.users[623].email, 'user623@example.invalid');
  assert.deepEqual(calls, [0, 1, 2, 3, 4, 5, 6]);
});

test('transient page failure retries only that page, preserving earlier users', async () => {
  const calls = []; let failed = false;
  const ctx = runtime({ async fetch(url) {
    const page = new URL(url).searchParams.get('cursor') || 'first'; calls.push(page);
    if (page === 'second' && !failed) { failed = true; return response({}, 503); }
    return response({ verified: true, users: [user(page === 'first' ? 0 : 1)], complete: page === 'second', has_more: page === 'first', next_cursor: page === 'first' ? 'second' : '' });
  } });
  assert.equal((await ctx.api.fetchFreshAdminUsers('https://worker.test', {})).users.length, 2);
  assert.deepEqual(calls, ['first', 'second', 'second']);
});

test('incomplete or repeated user pages fail instead of returning a partial list', async () => {
  for (const fixture of [
    { verified: false, users: [], complete: true, has_more: false },
    { verified: true, users: [user(0)], complete: false, has_more: false },
    { verified: true, users: [user(0)], complete: false, has_more: true, next_cursor: 'loop' },
  ]) {
    const ctx = runtime({ fetch: async () => response(fixture) });
    await assert.rejects(ctx.api.fetchFreshAdminUsers('https://worker.test', {}));
  }
  let calls = 0;
  const denied = runtime({ fetch: async () => { calls++; return response({}, 403); } });
  await assert.rejects(denied.api.fetchFreshAdminUsers('https://worker.test', {}));
  assert.equal(calls, 1);
});

test('complete directory uses one request for 650 accounts and finds the last account from the first page', async () => {
  const rows = Array.from({ length: 650 }, (_, i) => user(i));
  const calls = [];
  const ctx = runtime({ async fetch(url, options) {
    assert.equal(options.cache, 'no-store');
    calls.push(new URL(url).searchParams.toString());
    return response({ verified: true, complete: true, has_more: false, total: rows.length, users: rows });
  } });
  const result = await ctx.api.fetchFreshAdminUsers('https://worker.test', {});
  assert.equal(result.users.length, 650);
  assert.deepEqual(calls, ['view=directory']);
  const first = ctx.api.adminUserPage(result.users, '', 0);
  assert.equal(first.rows.length, 25);
  assert.equal(first.matches, 650);
  assert.equal(first.totalPages, 26);
  const search = ctx.api.adminUserPage(result.users, ' ＵＳＥＲ６４９@example.invalid ', 8);
  assert.equal(search.matches, 1);
  assert.equal(search.rows[0].email, 'user649@example.invalid');
  assert.equal(ctx.api.adminUserPage(result.users, '', 0, user(649).email).page, 25,
    'refresh can keep an open editor with its row even if sort order changes');
});

test('a bulk fallback or malformed complete count still requires a complete verified cursor read', async () => {
  for (const bulk of [
    response({ code: 'use_user_cursor' }, 409),
    response({ verified: true, complete: true, has_more: false, total: 2, users: [user(99)] }),
    response({ verified: true, complete: true, has_more: false, total: 2, users: [user(99), user(99)] }),
  ]) {
    const queries = [];
    const ctx = runtime({ async fetch(url) {
      const parsed = new URL(url);
      queries.push(parsed.searchParams.toString());
      return parsed.searchParams.get('view') ? bulk
        : response({ verified: true, users: [user(0)], complete: true, has_more: false });
    } });
    const result = await ctx.api.fetchFreshAdminUsers('https://worker.test', {});
    assert.deepEqual(Array.from(result.users, (row) => row.id), ['user-0']);
    assert.deepEqual(queries, ['view=directory', 'page_size=100']);
  }
});

test('closing a user directory aborts its request and does not start fallback pages', async () => {
  let calls = 0;
  const controller = new AbortController();
  const ctx = runtime({ async fetch(_url, options) {
    calls++;
    return new Promise((resolve, reject) => options.signal.addEventListener('abort', () => reject(new Error('aborted'))));
  } });
  const pending = ctx.api.fetchFreshAdminUsers('https://worker.test', {}, controller.signal);
  controller.abort();
  await assert.rejects(pending, /aborted/u);
  assert.equal(calls, 1);
});

test('first full load keeps concurrent user creation and coalesces duplicate refreshes', async () => {
  let resolve, calls = 0, rendered = [];
  const ctx = vm.createContext({ fetchFreshAdminUsers() { calls++; return new Promise((done) => { resolve = done; }); },
    renderAdminUserTable(targets) { rendered.push([targets.userDirectory.size, targets.usersComplete]); },
  });
  vm.runInContext(extract('loadFreshAdminUsers'), ctx);
  const targets = { usersSection: { isConnected: true }, userDirectory: new Map(), usersComplete: false };
  const first = ctx.loadFreshAdminUsers('/api', targets), second = ctx.loadFreshAdminUsers('/api', targets);
  targets.userDirectory.set('new@example.invalid', { email: 'new@example.invalid' });
  resolve({ users: Array.from({ length: 624 }, (_, i) => user(i)) });
  await Promise.all([first, second]);
  assert.equal(calls, 1);
  assert.equal(targets.userDirectory.size, 625);
  assert.deepEqual(rendered, [[625, true]]);
});

test('completed refresh keeps concurrent permission edits but includes newly registered users', async () => {
  let resolve;
  const original = user(0);
  const ctx = vm.createContext({ fetchFreshAdminUsers: () => new Promise((done) => { resolve = done; }), renderAdminUserTable() {} });
  vm.runInContext(extract('loadFreshAdminUsers'), ctx);
  const targets = { userDirectory: new Map([[original.email, original]]), usersComplete: true };
  const task = ctx.loadFreshAdminUsers('/api', targets);
  const edited = { ...original, newsfeed: { enabled: true } };
  targets.userDirectory.set(original.email, edited);
  resolve({ users: [original, user(1)] }); await task;
  assert.equal(targets.userDirectory.get(original.email), edited);
  assert.equal(targets.userDirectory.size, 2);
});

class Node {
  constructor(tag = 'div') { this.tag = tag; this.children = []; this.dataset = {}; this.className = ''; this.attrs = {}; this.hidden = false; this.listeners = {}; this.classList = { contains: (name) => this.className.split(' ').includes(name) }; }
  append(child) { child.remove(); child.parent = this; this.children.push(child); }
  after(child) { child.remove(); child.parent = this.parent; this.parent.children.splice(this.parent.children.indexOf(this) + 1, 0, child); }
  remove() { if (this.parent) this.parent.children.splice(this.parent.children.indexOf(this), 1); this.parent = null; }
  get firstElementChild() { return this.children[0]; }
  get nextElementSibling() { return this.parent?.children[this.parent.children.indexOf(this) + 1]; }
  get previousElementSibling() { return this.parent?.children[this.parent.children.indexOf(this) - 1]; }
  matches(selector) { return selector === 'tr[data-email]' ? this.tag === 'tr' && Boolean(this.dataset.email) : selector[0] === '.' ? this.classList.contains(selector.slice(1)) : selector === 'button[type="submit"]' && this.tag === 'button'; }
  querySelectorAll(selector) { return this.children.flatMap((child) => [ ...(child.matches(selector) ? [child] : []), ...child.querySelectorAll(selector) ]); }
  querySelector(selector) { return this.querySelectorAll(selector)[0] || null; }
  closest(selector) { return this.matches(selector) ? this : this.parent?.closest(selector); }
  setAttribute(key, value) { this.attrs[key] = value; }
  focus(options) { assert.equal(options.preventScroll, true); this.focused = true; }
  addEventListener(event, handler) { this.listeners[event] = handler; }
}

test('rendered directory keeps its full count but only creates one page of controls', () => {
  const ctx = runtime({ document: { activeElement: null } });
  const rows = Array.from({ length: 647 }, (_, i) => ({ ...user(i), role: 'user' }));
  const map = new Map(rows.map((row) => [row.email, row]));
  const targets = {
    usersComplete: true, users: { contains: () => false }, userSearch: { value: '' },
    userCount: {}, userPagination: {}, userPageLabel: {}, userPrevious: {}, userNext: {},
    content: { scrollTop: 124 }, passwordTools: { open: false },
  };
  const helpers = {
    PUBLIC_BRAND: '示例站', publicBrandText: (value) => value || '',
    accountRightUsageText: () => '', escapeHtml: (value) => String(value),
  };
  ctx.api.renderAdminUserTable(targets, map, helpers);
  assert.equal(targets.userCount.textContent, '全部 647 位用户');
  assert.equal((targets.users.innerHTML.match(/<tr data-email=/g) || []).length, 25);
  assert.equal(targets.userPageLabel.textContent, '1–25 / 647');
  assert.equal(targets.content.scrollTop, 124);
  targets.userSearch.value = 'user646@example.invalid';
  ctx.api.renderAdminUserTable(targets, map, helpers);
  assert.equal(targets.userCount.textContent, '匹配 1 / 647 位用户');
  assert.match(targets.users.innerHTML, /data-email="user646@example.invalid"/u);
  assert.equal(targets.userPagination.hidden, true);
});

test('inline editor moves below its own row and preserves its existing input state', () => {
  const ctx = runtime({ document: { createElement: (tag) => new Node(tag) } });
  const table = new Node('tbody'), home = new Node(), editor = new Node('form'); editor.className = 'account-admin-user-editor'; editor.draft = 'preserved'; home.append(editor);
  const rows = [0, 1].map((i) => { const row = new Node('tr'); row.dataset.email = user(i).email; const button = new Node('button'); button.className = 'account-admin-edit-user'; row.append(button); table.append(row); return row; });
  const targets = { users: table, editorHome: home, userEditor: editor };
  ctx.api.mountAdminInlineEditor(targets, editor, rows[1].dataset.email);
  assert.equal(rows[1].nextElementSibling.firstElementChild.firstElementChild, editor);
  assert.equal(rows[0].nextElementSibling, rows[1]);
  assert.equal(editor.draft, 'preserved');
  assert.equal(rows[1].firstElementChild.attrs['aria-expanded'], 'true');
  ctx.api.closeAdminInlineEditor(targets, editor);
  assert.equal(editor.parent, home); assert.equal(table.children.length, 2); assert.equal(editor.hidden, true);
});

test('Newsfeed grant submits independent expiry and optimistic version; dates include the Beijing end of day', async () => {
  let sent;
  const ctx = runtime({ fetch: async (_url, options) => { sent = JSON.parse(options.body); return response({ verified: true, user: user(1) }); } });
  const targets = { newsfeedEmail: { value: user(1).email }, newsfeedMode: { value: 'enabled' }, newsfeedExpiry: { value: '2026-12-23' }, newsfeedEditor: { dataset: { updatedAt: 'previous' } } };
  await ctx.api.saveAdminNewsfeed('/api', targets, {});
  assert.deepEqual(sent, { email: user(1).email, newsfeed_mode: 'enabled', newsfeed_expires_at: '2026-12-23T15:59:59.999Z', expected_updated_at: 'previous' });
  targets.newsfeedMode.value = 'auto'; await ctx.api.saveAdminNewsfeed('/api', targets, {}); assert.equal(sent.newsfeed_expires_at, '');
});

test('expired standalone Newsfeed grant label reflects the active membership fallback', () => {
  const ctx = runtime();
  const label = ctx.api.adminNewsfeedLabel({ newsfeed: { enabled: true, mode: 'enabled', source: 'membership', expires_at: '2026-01-01T00:00:00Z' }, effective_access: { current_period_end: '2026-12-23T15:59:59Z' } });
  assert.match(label, /会员可用.*2026-12-23/); assert.doesNotMatch(label, /2026-01-01|单独开通/);
});

test('late Newsfeed save keeps the newly selected user draft and feedback unchanged', async () => {
  const form = new Node('form'), submit = new Node('button'), close = new Node('button'); form.append(submit);
  let resolve, rendered = 0;
  const targets = { newsfeedEditor: form, newsfeedEmail: { value: user(0).email }, newsfeedMode: new Node('select'), newsfeedExpiry: new Node('input'), newsfeedStatus: { textContent: '' } };
  const ctx = runtime({ document: { getElementById: () => close } });
  ctx.api.bindNewsfeedEditor('/api', targets, { renderAdminUserTable() { rendered++; }, saveAdminNewsfeed() { return new Promise((done) => { resolve = done; }); } });
  const pending = form.listeners.submit({ preventDefault() {} });
  targets.newsfeedEmail.value = user(1).email;
  targets.newsfeedStatus.textContent = 'User 1 draft';
  resolve(user(0)); await pending;
  assert.equal(targets.newsfeedEmail.value, user(1).email);
  assert.equal(targets.newsfeedStatus.textContent, 'User 1 draft');
  assert.equal(rendered, 1);
});

test('pending Newsfeed save locks the shared controls and rejects duplicate submits', async () => {
  for (const fails of [false, true]) {
    const form = new Node('form'), submit = new Node('button'), close = new Node('button'); form.append(submit);
    let finish, calls = 0;
    const targets = { users: new Node('tbody'), editorHome: new Node(), newsfeedEditor: form, newsfeedEmail: { value: user(0).email }, newsfeedMode: new Node('select'), newsfeedExpiry: new Node('input'), newsfeedStatus: new Node(), newsfeedTitle: new Node(), newsfeedState: new Node() };
    const ctx = runtime({ document: { getElementById: () => close, createElement: (tag) => new Node(tag) } });
    const saved = { ...user(0), newsfeed: { mode: 'enabled', expires_at: '2026-12-23T15:59:59.999Z' } };
    const row = new Node('tr'); row.dataset.email = saved.email; targets.users.append(row);
    ctx.api.fillAdminNewsfeedEditor(saved, targets);
    ctx.api.bindNewsfeedEditor('/api', targets, { renderAdminUserTable() {}, saveAdminNewsfeed() { calls++; return new Promise((resolve, reject) => { finish = () => fails ? reject(new Error('retry later')) : resolve(saved); }); } });
    const pending = form.listeners.submit({ preventDefault() {} });
    assert.equal(submit.disabled, true);
    assert.equal(targets.newsfeedMode.disabled, true);
    assert.equal(targets.newsfeedExpiry.disabled, true);
    await form.listeners.submit({ preventDefault() {} });
    assert.equal(calls, 1);
    // Reopening the same row must not re-enable inputs while its save is pending.
    ctx.api.fillAdminNewsfeedEditor(saved, targets);
    assert.equal(targets.newsfeedMode.disabled, true);
    assert.equal(targets.newsfeedExpiry.disabled, true);
    finish(); await pending;
    assert.equal(submit.disabled, false);
    assert.equal(targets.newsfeedMode.disabled, false);
    assert.equal(targets.newsfeedExpiry.disabled, false);
    assert.equal(targets.newsfeedMode.value, 'enabled');
    assert.equal(targets.newsfeedExpiry.value, '2026-12-23');
    assert.equal(targets.newsfeedStatus.className, fails ? 'status-line error' : 'status-line ok');
  }
});

test('switching rows during a Newsfeed save keeps the new selection locked until completion', async () => {
  const form = new Node('form'), submit = new Node('button'); form.append(submit);
  let resolve;
  const targets = { users: new Node('tbody'), editorHome: new Node(), newsfeedEditor: form, newsfeedEmail: { value: user(0).email }, newsfeedMode: new Node('select'), newsfeedExpiry: new Node('input'), newsfeedStatus: new Node(), newsfeedTitle: new Node(), newsfeedState: new Node() };
  const ctx = runtime({ document: { getElementById: () => null } });
  ctx.api.bindNewsfeedEditor('/api', targets, { renderAdminUserTable() {}, saveAdminNewsfeed: () => new Promise((done) => { resolve = done; }) });
  const pending = form.listeners.submit({ preventDefault() {} });
  ctx.api.fillAdminNewsfeedEditor({ ...user(1), newsfeed: { mode: 'auto' } }, targets);
  assert.equal(targets.newsfeedMode.disabled, true);
  resolve(user(0)); await pending;
  assert.equal(targets.newsfeedEmail.value, user(1).email);
  assert.equal(targets.newsfeedMode.value, 'auto');
  assert.equal(targets.newsfeedMode.disabled, false);
  assert.equal(targets.newsfeedExpiry.disabled, true);
  assert.equal(targets.newsfeedStatus.textContent, '');
});

test('admin module URL stays at the site root from nested report and blog pages', () => {
  const loader = extract('loadAdminUserTools');
  const path = loader.match(/import\("([^"]+)"\)/)?.[1];
  assert.ok(path);
  for (const current of ['https://kcdesk.com/blog/article.html', 'https://kcdesk.com/reports/example/', 'https://kcdesk.com/en/report.html']) {
    assert.equal(new URL(path, current).pathname, '/assets/admin-users.js');
  }
});
