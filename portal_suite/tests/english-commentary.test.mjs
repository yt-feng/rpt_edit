import assert from "node:assert/strict";
import { createHash, webcrypto } from "node:crypto";
import test from "node:test";
import { readFile } from "node:fs/promises";
import { ENGLISH_COMMENTARY_POLICY as policy, ENGLISH_PREFIX as prefix, consumeEnglishRead,
  handleEnglishCommentary, validateEnglishBody, validateEnglishLedger } from "../../workers/portal-suite-worker/src/english-commentary.js";
import worker from "../../workers/portal-suite-worker/src/index.js";

if (!globalThis.crypto) globalThis.crypto = webcrypto;
const hash = (raw) => createHash("sha256").update(raw).digest("hex");
const siteRelease = "c".repeat(32);

function seedRelease(bucket, ledger, release = siteRelease) {
  const raw = JSON.stringify(ledger), ledger_sha256 = hash(raw);
  bucket.seed(`${prefix}/ledgers/${ledger_sha256}.json`, raw);
  bucket.seed(`${prefix}/releases/${release}/manifest.json`, {
    schema_version: 1, policy, status: "approved", site_release: release, ledger_sha256,
  });
  return ledger_sha256;
}
const id = (index = 1) => `20261001-${index.toString(16).padStart(16, "0")}`;

class MemoryR2 {
  data = new Map(); reads = []; writes = []; revision = 0; denied = false; conflict = false;
  seed(key, value) {
    const raw = typeof value === "string" ? value : JSON.stringify(value);
    this.data.set(key, { raw, etag: `v${++this.revision}` });
  }
  async get(key) {
    this.reads.push(key);
    if (this.denied) throw new Error("storage permission denied");
    const row = this.data.get(key);
    return row ? { etag: row.etag, size: Buffer.byteLength(row.raw), text: async () => row.raw } : null;
  }
  async put(key, raw, options) {
    this.writes.push(key);
    if (this.denied) throw new Error("storage permission denied");
    const current = this.data.get(key), condition = options.onlyIf;
    assert.equal(options.httpMetadata.cacheControl, "private, no-store");
    if (this.conflict || condition.etagMatches && current?.etag !== condition.etagMatches
      || condition.etagDoesNotMatch === "*" && current) return null;
    this.seed(key, raw); return { etag: this.data.get(key).etag };
  }
}

function fixture() {
  const bucket = new MemoryR2(), items = [];
  for (let index = 1; index <= 5; index += 1) {
    const body = { schema_version: 1, policy, locale: "en", content_kind: "secondary-commentary", id: id(index),
      title: `An editorial interpretation ${index}`, preview: "Our short interpretation preview.", datePublished: "2026-10-01",
      editorial_sha256: "a".repeat(64), blocks: [{ tag: "p", text: `Our own secondary analysis of developments ${index}.` }] };
    const raw = JSON.stringify(body), body_sha256 = hash(raw);
    bucket.seed(`${prefix}/bodies/${body_sha256}.json`, raw);
    const { id: articleId, title, preview, datePublished, editorial_sha256 } = body;
    items.push({ id: articleId, title, preview, datePublished, editorial_sha256, body_sha256 });
  }
  const ledger = { schema_version: 1, policy, locale: "en", status: "approved", release_id: "b".repeat(64), items };
  seedRelease(bucket, ledger);
  const adapters = {
    respond: (_request, _env, status, value) => new Response(JSON.stringify(value), { status }),
    currentUser: async () => ({ id: "account-1" }), membership: async () => false,
    activeRelease: async () => siteRelease,
  };
  return { bucket, ledger, adapters, env: { REPORT_BUCKET: bucket } };
}

async function read(state, articleId = id(), patch = {}) {
  const response = await handleEnglishCommentary(new Request("https://example.invalid/api/english/commentary/read", {
    method: "POST", body: JSON.stringify({ id: articleId }), ...patch,
  }), state.env, state.adapters);
  return { status: response.status, value: await response.json() };
}

test("public preview exposes no private body, keys, original fields or charts", async () => {
  const state = fixture();
  const response = await handleEnglishCommentary(new Request("https://example.invalid/api/english/commentary?id=" + id()), state.env, state.adapters);
  const value = await response.json();
  assert.equal(response.status, 200); assert.equal(value.free_reads, 3);
  for (const forbidden of ["blocks", "body_sha256", "editorial_sha256", "report", "charts", "original_text"]) assert.equal(Object.hasOwn(value, forbidden), false);
  assert.equal(state.bucket.reads.length, 2); assert.equal(state.bucket.writes.length, 0);
});

test("public list is paginated previews only", async () => {
  const state = fixture();
  const response = await handleEnglishCommentary(new Request("https://example.invalid/api/english/commentary"), state.env, state.adapters);
  const value = await response.json(); assert.equal(value.total, 5); assert.equal(value.page_size, 24);
  assert.equal(value.items[0].id, id(5)); assert.equal(Object.hasOwn(value.items[0], "blocks"), false);
});

test("anonymous or disabled readers cannot fetch private text or consume quota", async () => {
  for (const currentUser of [async () => { throw new Error("login required"); }, async () => ({ id: "account-1", disabled: true })]) {
    const state = fixture(); state.adapters.currentUser = currentUser;
    const result = await read(state); assert.equal(result.status, 401);
    assert.equal(state.bucket.reads.length, 2); assert.equal(state.bucket.writes.length, 0);
  }
});

test("three distinct free comments; repeated reads are free; fourth requires membership", async () => {
  const state = fixture();
  assert.equal((await read(state, id(1))).value.remaining, 2);
  assert.equal((await read(state, id(1))).value.reused, true);
  assert.equal((await read(state, id(2))).value.remaining, 1);
  assert.equal((await read(state, id(3))).value.remaining, 0);
  const fourth = await read(state, id(4)); assert.equal(fourth.status, 402);
  assert.equal(fourth.value.error, "membership_required"); assert.equal(fourth.value.request_action.type, "membership_request");
  assert.equal(Object.hasOwn(fourth.value, "blocks"), false);
  assert.equal((await read(state, id(1))).status, 200);
});

test("active members read without touching the free allowance; revoked membership is re-evaluated", async () => {
  const state = fixture(); state.adapters.membership = async () => true;
  const result = await read(state, id(5)); assert.equal(result.status, 200); assert.equal(result.value.access, "member");
  assert.equal(result.value.remaining, null); assert.equal(state.bucket.writes.length, 0);
  state.adapters.membership = async () => false;
  assert.equal((await read(state, id(5))).value.remaining, 2);
});

test("concurrent requests never exceed three grants or lose a read", async () => {
  const bucket = new MemoryR2();
  const results = await Promise.all([1, 2, 3, 4, 5].map((index) => consumeEnglishRead(bucket, "concurrent-account", id(index))));
  assert.equal(results.filter((row) => row.allowed).length, 3);
  const quota = JSON.parse([...bucket.data.values()][0].raw); assert.equal(quota.reads.length, 3);
});

test("same-account same-article race is charged once", async () => {
  const bucket = new MemoryR2();
  const results = await Promise.all([1, 2, 3].map(() => consumeEnglishRead(bucket, "same-account", id())));
  assert.equal(results.every((row) => row.allowed && row.remaining === 2), true);
  assert.equal(results.filter((row) => !row.reused).length, 1);
});

test("different accounts have isolated hashed private quotas", async () => {
  const bucket = new MemoryR2();
  await consumeEnglishRead(bucket, "first-account", id()); await consumeEnglishRead(bucket, "second-account", id());
  assert.equal(bucket.data.size, 2);
  assert.equal([...bucket.data.keys()].every((key) => /\/accounts\/[a-f0-9]{64}\/reads\.json$/.test(key)), true);
});

test("missing or corrupt private body never spends a read or returns text", async () => {
  for (const replacement of [null, "corrupted"]) {
    const state = fixture(), key = `${prefix}/bodies/${state.ledger.items[0].body_sha256}.json`;
    if (replacement === null) state.bucket.data.delete(key); else state.bucket.seed(key, replacement);
    const result = await read(state); assert.equal(result.status, 503); assert.equal(state.bucket.writes.length, 0);
    assert.equal(Object.hasOwn(result.value, "blocks"), false);
  }
});

test("unapproved ledgers, unknown fields, originals, charts and malformed identities fail closed", () => {
  const state = fixture();
  for (const changes of [{ status: "candidate" }, { locale: "fr" }, { policy: "full-report" }, { original_text: "original" }, { release_id: "invalid" }]) {
    assert.throws(() => validateEnglishLedger({ ...state.ledger, ...changes }));
  }
  const item = state.ledger.items[0], body = JSON.parse(state.bucket.data.get(`${prefix}/bodies/${item.body_sha256}.json`).raw);
  for (const changes of [{ content_kind: "original-report" }, { original_text: "original" }, { charts: [] }, { source_url: "https://source.invalid/report" },
    { blocks: [{ tag: "img", text: "chart" }] }, { blocks: [{ tag: "blockquote", text: "quoted original" }] },
    { blocks: [{ tag: "p", text: "<img src='/charts/1'>" }] }, { blocks: [{ tag: "p", text: "![chart](/charts/1)" }] },
    { blocks: [{ tag: "p", text: "原文报告" }] }]) assert.throws(() => validateEnglishBody({ ...body, ...changes }, item));
});

test("storage permission or membership lookup failures never grant free or member text", async () => {
  const denied = fixture(); denied.bucket.denied = true; assert.equal((await read(denied)).status, 503);
  const state = fixture(); state.adapters.membership = async () => { throw new Error("private failure"); };
  const result = await read(state); assert.equal(result.status, 503); assert.equal(state.bucket.writes.length, 0);
});

test("invalid and oversized requests do not access full text or consume a read", async () => {
  const state = fixture();
  for (const [body, status] of [["not JSON", 400], [JSON.stringify({ id: "../../private" }), 400],
    [JSON.stringify({ id: id(), original: "x" }), 400], ["x".repeat(2049), 413]]) {
    assert.equal((await read(state, id(), { body })).status, status);
  }
  assert.equal(state.bucket.writes.length, 0); assert.equal(state.bucket.reads.some((key) => key.includes("/bodies/")), false);
});

test("contention is bounded and malformed quota cannot reset the allowance", async () => {
  const state = fixture(); state.bucket.conflict = true;
  assert.equal((await read(state)).status, 503); assert.equal(state.bucket.writes.length, 6);
  state.bucket.conflict = false; state.bucket.writes = [];
  await read(state);
  const key = state.bucket.writes[0]; state.bucket.seed(key, { schema_version: 1, reads: [] });
  assert.equal((await read(state, id(2))).status, 503);
});

test("actual Worker routes retain authentication, private headers and existing membership authority", async () => {
  const state = fixture();
  state.env.STATIC_DATA_STATE_URL = "https://english-runtime-test.invalid/.well-known/edge-state";
  const previousFetch = globalThis.fetch;
  globalThis.fetch = async (url) => {
    assert.equal(String(url), state.env.STATIC_DATA_STATE_URL + "?runtime-data=1");
    return new Response(JSON.stringify({ schema_version: 1, slot: "a", release_id: siteRelease }));
  };
  try {
    const response = await worker.fetch(new Request("https://example.invalid/api/english/commentary/read", { method: "POST", body: JSON.stringify({ id: id() }) }), state.env, {});
    assert.equal(response.status, 401); assert.match(response.headers.get("cache-control"), /private, no-store/);
    assert.equal(state.bucket.writes.length, 0);
  } finally { globalThis.fetch = previousFetch; }
  const source = await readFile(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url), "utf8");
  assert.match(source, /currentUser: currentUserFromRequest/); assert.match(source, /await marketViewMembershipAccessForUser\(runtime, user\)/);
  assert.match(source, /activeRelease: activeRuntimeDataRelease/);
});

test("English release selection follows active site cutover and rollback without a mutable fallback", async () => {
  const state = fixture(), secondRelease = "d".repeat(32);
  const secondLedger = { ...state.ledger, release_id: "e".repeat(64), items: [state.ledger.items[4]] };
  seedRelease(state.bucket, secondLedger, secondRelease);
  const get = () => handleEnglishCommentary(new Request("https://example.invalid/api/english/commentary?id=" + id(1)), state.env, state.adapters);
  assert.equal((await get()).status, 200);
  state.adapters.activeRelease = async () => secondRelease;
  assert.equal((await get()).status, 404);
  assert.equal((await read(state, id(1))).status, 404); assert.equal(state.bucket.writes.length, 0);
  state.adapters.activeRelease = async () => siteRelease;
  assert.equal((await get()).status, 200);
  assert.equal(state.bucket.reads.some((key) => key.endsWith("/active.json")), false);
});

test("missing active state, unapproved or cross-release manifest and ledger checksum fail closed before quota", async () => {
  for (const active of ["", "../../private", null]) {
    const state = fixture(); state.adapters.activeRelease = async () => active;
    assert.equal((await read(state)).status, 503); assert.equal(state.bucket.writes.length, 0);
  }
  for (const changes of [{ status: "candidate" }, { site_release: "f".repeat(32) }, { original_text: "SECRET" }]) {
    const state = fixture(), key = `${prefix}/releases/${siteRelease}/manifest.json`;
    state.bucket.seed(key, { ...JSON.parse(state.bucket.data.get(key).raw), ...changes });
    assert.equal((await read(state)).status, 503); assert.equal(state.bucket.writes.length, 0);
  }
  const state = fixture(), sha = seedRelease(state.bucket, state.ledger);
  state.bucket.seed(`${prefix}/ledgers/${sha}.json`, { ...state.ledger, items: [] });
  assert.equal((await read(state)).status, 503); assert.equal(state.bucket.writes.length, 0);
});
