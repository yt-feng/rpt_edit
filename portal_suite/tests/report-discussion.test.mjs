import assert from "node:assert/strict";
import test from "node:test";
import { createReportDiscussion, validateDiscussionStarter } from "../../workers/portal-suite-worker/src/report-discussion.js";

class Bucket {
  data = new Map(); version = 0;
  async get(key) {
    const row = this.data.get(key);
    return row ? { etag: row.etag, size: row.body.length, text: async () => row.body } : null;
  }
  async put(key, body, options = {}) {
    const current = this.data.get(key), condition = options.onlyIf || {};
    if (condition.etagDoesNotMatch === "*" && current) return null;
    if (condition.etagMatches && condition.etagMatches !== current?.etag) return null;
    const etag = String(++this.version); this.data.set(key, { body, etag }); return { etag };
  }
}
const source = "报告指出，企业盈利增长依赖需求恢复和单位成本下降。当前库存仍处在调整阶段，需求变化需要结合订单趋势判断。".repeat(8);
const generated = {
  body: "报告把盈利改善与需求恢复、成本下降联系起来，值得继续核验的是订单回升能否持续。库存调整也可能影响短期观察：你会优先跟踪哪些指标，来判断需求改善是否能够转化为盈利？",
  evidence_quote: "企业盈利增长依赖需求恢复和单位成本下降。当前库存仍处在调整阶段，需求变化需要结合订单趋势判断。",
};

function setup(overrides = {}) {
  const bucket = new Bucket(), calls = [];
  const deps = {
    bucket: () => bucket,
    resolveReport: async (_env, kind, id) => id === "missing" ? null : { id, source: kind, title: "企业盈利观察" },
    currentUser: async (_env, request) => ({ id: request.headers.get("authorization").slice(7), username: "读者" }),
    publicName: (user) => user.username,
    isAdmin: (user) => user.id === "admin",
    json: (_request, _env, status, body) => Response.json(body, { status }),
    originAllowed: (request) => request.headers.get("origin") === "https://example.invalid",
    readText: async () => ({ text: source, text_scope: "partial_excerpt" }),
    generateJson: async (_env, messages, options) => { calls.push({ messages, options }); return generated; },
    ...overrides,
  };
  return { bucket, calls, service: createReportDiscussion(deps) };
}

async function request(service, method = "GET", payload = {}, user = "", extraHeaders = {}) {
  const body = { source: "catalog", report_id: "report-one", ...payload };
  const headers = { origin: "https://example.invalid", "content-type": "application/json", ...(user ? { authorization: `Bearer ${user}` } : {}), ...extraHeaders };
  const url = "https://example.invalid/api/report-discussion" + (method === "GET" ? "?" + new URLSearchParams(body) : "");
  const response = await service.handle(new Request(url, { method, headers, ...(method !== "GET" ? { body: JSON.stringify(body) } : {}) }), {});
  return { status: response.status, body: await response.json() };
}

test("all historical reports expose discussion without generating an AI comment", async () => {
  const state = setup();
  const result = await request(state.service);
  assert.equal(result.status, 200);
  assert.deepEqual(result.body.comments, []);
  assert.equal(result.body.starter, null);
  assert.equal(state.calls.length, 0);
  assert.equal(state.bucket.data.size, 0);
  assert.deepEqual(await state.service.generate({}, { source: "catalog", report_id: "report-one" }), { generated: false, status: "not_authorized" });
});

test("registered readers post genuine comments and retry one submission without duplication", async () => {
  const { service } = setup();
  const payload = { body: "我更关注新增订单，库存是否存在季节性变化？", request_id: "request-one" };
  const first = await request(service, "POST", payload, "reader-one");
  assert.equal(first.status, 201);
  assert.equal(first.body.comment.kind, "user");
  assert.equal(first.body.comment.can_delete, true);
  const second = await request(service, "POST", payload, "reader-one");
  assert.equal(second.status, 200);
  assert.equal(second.body.deduplicated, true);
  assert.equal(second.body.comment.id, first.body.comment.id);
  const publicView = await request(service);
  assert.equal(publicView.body.comments.length, 1);
  assert.equal(publicView.body.comments[0].can_delete, false);
  assert.equal(JSON.stringify(publicView.body).includes("author_user_id"), false);
  assert.equal(JSON.stringify(publicView.body).includes("request_id"), false);
});

test("write validation blocks anonymous, foreign-origin, missing report and oversized messages", async () => {
  const { service } = setup();
  const payload = { body: "读者评论", request_id: "request-one" };
  assert.equal((await request(service, "POST", payload)).status, 401);
  assert.equal((await request(service, "POST", payload, "reader", { origin: "https://foreign.invalid" })).status, 403);
  assert.equal((await request(service, "POST", { ...payload, report_id: "missing" }, "reader")).status, 404);
  assert.equal((await request(service, "POST", { ...payload, body: "字".repeat(1201) }, "reader")).status, 400);
  assert.equal((await request(service, "POST", { ...payload, request_id: "bad" }, "reader")).status, 400);
  assert.equal((await request(service, "POST", payload, "reader", { "content-type": "text/plain" })).status, 400);
});

test("concurrent genuine posts preserve both comments and rate limits span report IDs", async () => {
  const { service } = setup();
  const replies = await Promise.all([1, 2].map((index) => request(service, "POST", { body: `观察 ${index}`, request_id: `request-${index}` }, "reader")));
  assert.deepEqual(replies.map((row) => row.status), [201, 201]);
  assert.equal((await request(service)).body.comments.length, 2);
  for (let index = 3; index <= 5; index += 1) {
    assert.equal((await request(service, "POST", { report_id: `report-${index}`, body: "另一个观察", request_id: `request-${index}` }, "reader")).status, 201);
  }
  assert.equal((await request(service, "POST", { report_id: "report-six", body: "频繁提交", request_id: "request-six" }, "reader")).status, 429);
});

test("only author or administrator can remove a reader comment", async () => {
  const { service } = setup();
  const posted = await request(service, "POST", { body: "有待核验", request_id: "request-one" }, "reader");
  const payload = { comment_id: posted.body.comment.id };
  assert.equal((await request(service, "DELETE", payload, "someone-else")).status, 403);
  assert.equal((await request(service, "DELETE", payload, "reader")).status, 200);
  const next = await request(service, "POST", { body: "新的观察", request_id: "request-two" }, "reader");
  assert.equal((await request(service, "DELETE", { comment_id: next.body.comment.id }, "admin")).status, 200);
  assert.equal((await request(service)).body.comments.length, 0);
});

test("publish-time AI generation reserves before a single bounded provider call and preserves private evidence", async () => {
  const state = setup();
  const input = { source: "catalog", report_id: "report-one" };
  const results = await Promise.all([state.service.generate({}, input, { authorizedNewReport: true }), state.service.generate({}, input, { authorizedNewReport: true })]);
  assert.equal(results.filter((row) => row.generated).length, 1);
  assert.equal(state.calls.length, 1);
  assert.equal(state.calls[0].options.maxTokens, 800);
  const publicView = await request(state.service);
  assert.equal(publicView.body.starter.kind, "ai");
  assert.equal(publicView.body.starter.display_name, "AI 导读");
  assert.equal(publicView.body.starter.text_scope, "partial_excerpt");
  assert.equal(publicView.body.starter.body, generated.body);
  assert.equal(JSON.stringify(publicView.body).includes("evidence_quote"), false);
  assert.equal(JSON.stringify(publicView.body).includes("source_sha256"), false);
  assert.equal((await state.service.generate({}, input, { authorizedNewReport: true })).deduplicated, true);
  assert.equal(state.calls.length, 1);
});

test("missing text can become ready later, while unknown provider outcomes are never retried implicitly", async () => {
  let available = false;
  const state = setup({ readText: async () => available ? { text: source } : null, generateJson: async () => { throw new Error("timeout"); } });
  const input = { source: "catalog", report_id: "report-one" }, options = { authorizedNewReport: true };
  assert.equal((await state.service.generate({}, input, options)).status, "source_unavailable");
  assert.equal(state.bucket.data.size, 0);
  available = true;
  assert.equal((await state.service.generate({}, input, options)).status, "unknown");
  const next = await state.service.generate({}, input, options);
  assert.equal(next.status, "unknown"); assert.equal(next.deduplicated, true);
});

test("a final state write conflict never claims a published AI starter", async () => {
  const state = setup(), put = state.bucket.put.bind(state.bucket);
  state.bucket.put = async (key, value, options) => JSON.parse(value).status === "ready" ? null : put(key, value, options);
  const input = { source: "catalog", report_id: "report-one" }, options = { authorizedNewReport: true };
  const result = await state.service.generate({}, input, options);
  assert.equal(result.generated, false);
  assert.equal(result.status, "pending");
  const view = await request(state.service);
  assert.equal(view.body.starter, null);
  assert.equal(view.body.starter_status, "pending");
  assert.equal((await state.service.generate({}, input, options)).deduplicated, true);
  assert.equal(state.calls.length, 1);
});

test("pre-provider metadata and text read failures can retry when the same source becomes available", async () => {
  let metadataAvailable = false, textAvailable = false;
  const state = setup({
    resolveReport: async (_env, kind, id) => {
      if (!metadataAvailable) throw new Error("temporary catalog read failure");
      return { id, source: kind, title: "企业盈利观察" };
    },
    readText: async () => {
      if (!textAvailable) throw new Error("temporary source read failure");
      return { text: source };
    },
  });
  const input = { source: "catalog", report_id: "report-one" }, options = { authorizedNewReport: true };
  assert.equal((await state.service.generate({}, input, options)).status, "source_unavailable");
  metadataAvailable = true;
  assert.equal((await state.service.generate({}, input, options)).status, "source_unavailable");
  assert.equal(state.bucket.data.size, 0);
  assert.equal(state.calls.length, 0);
  textAvailable = true;
  assert.equal((await state.service.generate({}, input, options)).status, "ready");
  assert.equal(state.calls.length, 1);
});

test("AI starter validation requires actual evidence, open questions and report-supported numbers", () => {
  assert.ok(validateDiscussionStarter(generated, source));
  assert.equal(validateDiscussionStarter({ ...generated, evidence_quote: "报告里没有的连续证据".repeat(4) }, source), null);
  assert.equal(validateDiscussionStarter({ ...generated, body: generated.body + "预计增长 99%。" }, source), null);
  assert.equal(validateDiscussionStarter({ ...generated, body: generated.body.replace("？", "。") }, source), null);
  assert.equal(validateDiscussionStarter({ ...generated, body: generated.body + "<script>alert(1)</script>" }, source), null);
});

test("existing hot report comments stay in their legacy store and retried new comments are not duplicated", async () => {
  const legacy = [{ id: "comment:0123456789abcdef", display_name: "原有读者", body: "以前留下的真实评论", created_at: new Date().toISOString() }];
  let writes = 0;
  const state = setup({ listHotComments: async () => legacy, writeHotComment: async (incoming) => {
    writes += 1;
    const payload = await incoming.json();
    assert.equal(payload.author_alias, undefined);
    return Response.json({ ok: true, comment: { id: "legacy-new", body: payload.body } }, { status: 201 });
  } });
  const view = await request(state.service, "GET", { source: "hot" });
  assert.equal(view.body.comments[0].body, legacy[0].body);
  const payload = { source: "hot", body: "新读者的评论", request_id: "request-hot" };
  assert.equal((await request(state.service, "POST", payload, "reader")).status, 201);
  assert.equal((await request(state.service, "POST", payload, "reader")).status, 201);
  assert.equal(writes, 1);
});
