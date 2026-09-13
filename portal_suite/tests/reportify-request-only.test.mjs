import assert from 'node:assert/strict';
import { createHash, createHmac } from 'node:crypto';
import test from 'node:test';
import worker from '../../workers/portal-suite-worker/src/index.js';

const ID = '1295384700889731072';
const HOT_ID = 'hot:7e1f2757f1b831ed';
const ORIGIN = 'https://portal.example.invalid';
const TITLE = "China's Next Industrial Revolution";
const digest = createHash('sha256').update(`portal-contact-report:v1:external:${ID}`).digest('hex');
const targetKey = `_contact-reports/v1/targets/${digest}.json`;

class MemoryR2 {
  constructor() { this.rows = new Map(); this.reads = []; this.version = 0; }
  object(row) {
    return row ? { ...row, body: row.bytes.slice(), text: async () => new TextDecoder().decode(row.bytes) } : null;
  }
  async get(key) { this.reads.push(key); return this.object(this.rows.get(key)); }
  async head(key) { this.reads.push(key); return this.object(this.rows.get(key)); }
  async put(key, value, options = {}) {
    const existing = this.rows.get(key);
    if (options.onlyIf?.etagDoesNotMatch === '*' && existing) return null;
    if (options.onlyIf?.etagMatches && existing?.etag !== options.onlyIf.etagMatches) return null;
    const bytes = typeof value === 'string' ? new TextEncoder().encode(value) : new Uint8Array(value);
    const row = { bytes, size: bytes.length, etag: `v${++this.version}`, customMetadata: options.customMetadata || {} };
    this.rows.set(key, row);
    return this.object(row);
  }
  async list({ prefix = '' } = {}) {
    return { objects: [...this.rows].filter(([key]) => key.startsWith(prefix)).map(([key, row]) => ({ key, ...row })), truncated: false };
  }
  async delete(key) { this.rows.delete(key); }
  async json(key, value) { return this.put(key, JSON.stringify(value)); }
}
function envFor(bucket) {
  return { REPORT_BUCKET: bucket, MASTER_KEY: 'request-only-secret', AUTH_SECRET: 'request-only-secret', ACCOUNT_STORE_MODE: 'r2', ALLOWED_ORIGIN: ORIGIN,
    NEWSFEED_EMAIL_PROVIDER: 'brevo', BREVO_API_KEY: 'test-key', BREVO_SENDER_EMAIL: 'sender@example.invalid' };
}

const SUPER_USER = { id: 'super-id', username: 'admin-a', email: 'admin-a@users.portal.example.invalid' };
function accountKey(...parts) { return ['_account', ...parts.map((part) => encodeURIComponent(String(part || '')))].join('/'); }
function superToken() {
  const now = Math.floor(Date.now() / 1000);
  const body = Buffer.from(JSON.stringify({ kind: 'user', sub: SUPER_USER.id, username: SUPER_USER.username, email: SUPER_USER.email, iat: now, exp: now + 3600 })).toString('base64url');
  const signature = createHmac('sha256', 'request-only-secret').update(`portal:account-token:v1:${body}`).digest('base64url');
  return `${body}.${signature}`;
}
async function seedSuper(bucket) {
  const user = { ...SUPER_USER, site_origin: 'portal', registered_site: 'portal', source_site: 'portal', session_epoch: '' };
  for (const key of [accountKey('users', 'id', user.id), accountKey('users', 'username', user.username), accountKey('users', 'email', user.email)]) {
    await bucket.json(key, user);
  }
  return { Authorization: `Bearer ${superToken()}` };
}
function call(env, pathname, body, headers = {}) {
  return worker.fetch(new Request(`${ORIGIN}${pathname}`, body === undefined ? { headers } : {
    method: 'POST', headers: { Origin: ORIGIN, 'Content-Type': 'application/json', ...headers }, body: JSON.stringify(body),
  }), env, { waitUntil(promise) { promise.catch(() => null); } });
}
async function withFetch(mock, run) {
  const old = globalThis.fetch; globalThis.fetch = mock;
  try { return await run(); } finally { globalThis.fetch = old; }
}
function assertLead(item) {
  assert.equal(item.available, false);
  assert.equal(item.contact_only, true);
  assert.equal(item.availability, 'contact_only');
  assert.equal(item.download_url || '', '');
  for (const field of ['summary', 'url_pdf', 'pdf_url', 'has_pdf']) assert.equal(item[field], undefined);
}
async function seedHot(bucket) {
  await bucket.json(`_hot-reports/items/${HOT_ID.slice(4)}.json`, {
    id: HOT_ID, title: TITLE, origin_source: 'external', origin_report_id: ID,
    retention_state: 'active', filename: 'old-preview.pdf', size_bytes: 180307, description: 'old summary',
  });
  await bucket.put(`_hot-reports/pdfs/${HOT_ID.slice(4)}.pdf`, '%PDF- old cover only');
}

test('legacy external PDF/status routes cannot read cached covers, dispatch jobs, or accept passwords', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket);
  await bucket.put(`reportify/${ID}.pdf`, '%PDF- cover only');
  await bucket.json(`reportify-status/${ID}.json`, { status: 'ready' });
  await withFetch(async () => { assert.fail('No upstream PDF, account, or dispatch request is permitted'); }, async () => {
    for (const [pathname, body] of [
      [`/external/pdf?id=${ID}&password=old-password`, undefined],
      ['/external/pdf', { id: ID, password: 'old-password' }],
      [`/contact-report/pdf?source=external&id=${ID}`, undefined],
    ]) {
      const response = await call(env, pathname, body);
      assert.equal(response.status, 403);
      assert.equal((await response.json()).request_required, true);
    }
    const response = await call(env, `/external/status?id=${ID}`);
    assert.equal(response.status, 200);
    assert.deepEqual(await response.json(), {
      id: ID, source: 'external', ready: false, status: 'contact_only', availability: 'contact_only',
      contact_only: true, request_required: true, message: '完整报告需要另行提交申请。',
    });
  });
  assert.equal(bucket.reads.some(key => key.startsWith('reportify')), false);
  assert.equal(bucket.rows.size, 2);
});

test('legacy numeric detail links recover canonical metadata and signed requests ignore client titles', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket); let sends = 0;
  await withFetch(async (url, options) => {
    if (String(url) === `https://api.reportify.cn/reports/${ID}`) return Response.json({ main: {
      report_id: ID, title: TITLE, institution_name: 'Example Research', document_total_page: 212,
      summary: 'Do not publish this summary', url_pdf: 'https://example.invalid/cover.pdf', file_type: 'pdf',
    } });
    assert.match(String(url), /brevo/);
    sends += 1;
    assert.match(JSON.parse(options.body).textContent, /China's Next Industrial Revolution/);
    assert.doesNotMatch(JSON.parse(options.body).textContent, /CLIENT OVERRIDE/);
    return Response.json({ messageId: 'mock-message' }, { status: 201 });
  }, async () => {
    const detailResponse = await call(env, `/external/item?id=${ID}`);
    assert.equal(detailResponse.status, 200);
    const { item } = await detailResponse.json();
    assertLead(item); assert.equal(item.page_count, 212); assert.ok(item.request_token);
    assert.ok(bucket.rows.has(targetKey));
    const unsigned = await call(env, '/report-request', { source: 'external', report_id: ID, title: TITLE, requester_email: 'reader@example.net' });
    assert.equal(unsigned.status, 400);
    const response = await call(env, '/report-request', {
      source: 'external', report_id: ID, title: 'CLIENT OVERRIDE', institution: 'CLIENT OVERRIDE',
      requester_email: 'reader@example.net', request_token: item.request_token,
    });
    assert.equal(response.status, 202);
  });
  assert.equal(sends, 1);
  const record = [...bucket.rows].find(([key]) => key.startsWith('_report-requests/v1/items/'));
  assert.equal(JSON.parse(new TextDecoder().decode(record[1].bytes)).target_verified, true);
});

test('fresh search, cached search, and legacy mirror results expose title leads with signed proof', async () => {
  for (const mirror of [false, true]) {
    const bucket = new MemoryR2(); const env = envFor(bucket);
    if (mirror) await bucket.json('_search-mirror/external/latest.json', { generated_at: new Date().toISOString(), items: [{
      id: ID, title: TITLE, source: 'external', file_type: 'pdf', summary: 'private summary',
      url_pdf: 'https://example.invalid/cover.pdf', available: true, has_pdf: true,
    }] });
    await withFetch(async () => {
      if (mirror) throw new Error('upstream unavailable');
      return Response.json({ items: [{ report_id: ID, title: TITLE, file_type: 'pdf', summary: 'private summary' }], page_num: 1, total_page: 1 });
    }, async () => {
      for (let attempt = 0; attempt < 2; attempt += 1) {
        const response = await call(env, '/external/search?q=Industrial');
        assert.equal(response.status, 200);
        const data = await response.json();
        assert.equal(data.items.length, 1); assertLead(data.items[0]); assert.ok(data.items[0].request_token);
      }
    });
  }
});

test('historical hot aliases stay request-only, sign original identity, and cannot expose archived PDF', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket); await seedHot(bucket);
  await withFetch(async () => { assert.fail('hot title metadata must recover locally'); }, async () => {
    const response = await call(env, `/hot-reports/item?id=${HOT_ID}`);
    const { item } = await response.json();
    assert.equal(response.status, 200); assertLead(item);
    assert.equal(item.id, HOT_ID); assert.equal(item.source, 'hot');
    assert.equal(item.request_report_id, ID); assert.equal(item.request_source, 'external');
    assert.equal(item.description, ''); assert.equal(item.filename, ''); assert.equal(item.size_bytes, 0);
    const claims = JSON.parse(Buffer.from(item.request_token.split('.')[0], 'base64url').toString());
    assert.equal(claims.source, 'external'); assert.equal(claims.origin_id, ID);
    bucket.reads = [];
    const pdf = await call(env, `/hot-reports/pdf?id=${HOT_ID}&password=old-password`);
    assert.equal(pdf.status, 403); assert.equal((await pdf.json()).request_required, true);
    assert.equal(bucket.reads.some(key => key.startsWith('_hot-reports/pdfs/')), false);
    const direct = await call(env, `/contact-report/item?source=external&id=${ID}`);
    assert.equal((await direct.json()).item.title, TITLE);
  });
});

test('only a verified manual binding can enable external download and hot-alias availability', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket); await seedHot(bucket);
  const uploadId = 'f6236162-045c-4f17-a775-6b15d6636867';
  const pdfKey = `_contact-reports/v1/pdfs/${digest}.pdf`;
  const object = await bucket.put(pdfKey, '%PDF- verified full report', { customMetadata: {
    source: 'contact-report-upload', target_source: 'external', origin_id: ID, upload_id: uploadId,
  } });
  const binding = { version: 1, source: 'external', origin_id: ID, title: TITLE, filename: 'complete.pdf',
    object_key: pdfKey, size_bytes: object.size, etag: object.etag, upload_id: uploadId, uploaded_at: new Date().toISOString() };
  await bucket.json(`_contact-reports/v1/items/${digest}.json`, binding);
  await withFetch(async () => { assert.fail('manual binding must never fetch source PDF'); }, async () => {
    for (const pathname of [`/external/item?id=${ID}`, `/hot-reports/item?id=${HOT_ID}`]) {
      const response = await call(env, pathname); const { item } = await response.json();
      assert.equal(item.available, true); assert.equal(item.contact_only, false); assert.equal(item.filename, 'complete.pdf');
      assert.equal(item.download_url, `/api/contact-report/pdf?source=external&id=${ID}`);
    }
    const gated = await call(env, `/external/pdf?id=${ID}&password=old-password`);
    assert.equal(gated.status, 401, 'manual fulfillment uses the existing membership gate; old password cannot grant it');
    object.customMetadata.target_source = 'authority';
    const rejected = await call(env, `/external/pdf?id=${ID}`);
    assert.equal(rejected.status, 403, 'mismatched target metadata cannot enable download');
  });
});

test('twotigers super account keeps the Reportify PDF path while ordinary users remain request-only', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket);
  await bucket.put(`reportify/${ID}.pdf`, '%PDF-1.7 full report');
  const adminHeaders = await seedSuper(bucket);
  await withFetch(async (url) => {
    if (String(url) === `https://api.reportify.cn/reports/${ID}`) return Response.json({ main: {
      report_id: ID, title: TITLE, document_total_page: 212, file_type: 'pdf', url_pdf: null,
    } });
    assert.fail(`unexpected upstream request: ${url}`);
  }, async () => {
    const ordinary = await call(env, `/external/pdf?id=${ID}`);
    assert.equal(ordinary.status, 403);
    assert.equal((await ordinary.json()).request_required, true);
    bucket.reads = [];
    const admin = await call(env, `/external/pdf?id=${ID}`, undefined, adminHeaders);
    assert.equal(admin.status, 200);
    assert.equal(admin.headers.get('content-type'), 'application/pdf');
    assert.match(await admin.text(), /^%PDF-1\.7/u);
    assert.ok(bucket.reads.includes(`reportify/${ID}.pdf`));
  });
});

test('twotigers can request a real Reportify login QR and complete token handoff', async () => {
  const bucket = new MemoryR2(); const env = envFor(bucket); const adminHeaders = await seedSuper(bucket);
  let pollCount = 0;
  await withFetch(async (url) => {
    if (String(url) === 'https://api.reportify.cn/auth/wechat/qrcode') {
      return Response.json({ qrcode_url: 'http://weixin.qq.com/q/test-qr', qrcode_id: '13577092886088710' });
    }
    if (String(url).startsWith('https://api.reportify.cn/auth/wechat/qrcode/login')) {
      pollCount += 1;
      return Response.json(pollCount > 1 ? { token: 'reportify-session-token' } : { token: null, is_bind_phone: false });
    }
    assert.fail(`unexpected upstream request: ${url}`);
  }, async () => {
    const qr = await call(env, '/external/login-qr', undefined, adminHeaders);
    assert.equal(qr.status, 200);
    const qrData = await qr.json();
    assert.equal(qrData.qrcode_id, '13577092886088710');
    assert.match(qrData.qr_image_url, /api\.qrserver\.com/u);
    const waiting = await call(env, '/external/login-qr/status?qrcode_id=13577092886088710', undefined, adminHeaders);
    assert.equal((await waiting.json()).ready, false);
    const ready = await call(env, '/external/login-qr/status?qrcode_id=13577092886088710', undefined, adminHeaders);
    assert.deepEqual(await ready.json(), { status: 'authenticated', ready: true });
    assert.ok(bucket.rows.has('reportify-auth/session.json'));
  });
});
