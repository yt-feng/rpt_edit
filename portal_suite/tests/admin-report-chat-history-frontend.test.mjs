import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appUrl = new URL("../site_src/assets/app.js", import.meta.url);
const app = await readFile(appUrl, "utf8");

function extractFunction(source, name) {
  const starts = [`async function ${name}(`, `function ${name}(`]
    .map((needle) => source.indexOf(needle))
    .filter((index) => index >= 0);
  assert.ok(starts.length, `${name} must exist`);
  const start = Math.min(...starts);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  let quote = "";
  let escaped = false;
  for (let index = bodyStart; index < source.length; index += 1) {
    const char = source[index];
    if (escaped) {
      escaped = false;
      continue;
    }
    if (quote && char === "\\") {
      escaped = true;
      continue;
    }
    if (quote) {
      if (char === quote) quote = "";
      continue;
    }
    if (["'", '"', "`"].includes(char)) {
      quote = char;
      continue;
    }
    if (char === "{") depth += 1;
    else if (char === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

function escapeHtml(value) {
  return String(value ?? "")
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&#39;");
}

function installArchiveHelpers(sandbox = {}) {
  vm.createContext(sandbox);
  vm.runInContext(`
    ${extractFunction(app, "adminReportChatCollectionCount")}
    ${extractFunction(app, "adminReportChatPreviewText")}
    ${extractFunction(app, "normalizeAdminReportChatArchive")}
    ${extractFunction(app, "adminReportChatAnswerDetails")}
    ${extractFunction(app, "adminReportChatArchiveRow")}
    ${extractFunction(app, "renderAdminReportChatArchives")}
    ${extractFunction(app, "fetchAdminReportChatHistory")}
    ${extractFunction(app, "loadAdminReportChatHistory")}
    ${extractFunction(app, "curateAdminReportChatArchive")}
  `, sandbox);
  return sandbox;
}

test("RAG archive section is rendered only for the super-admin management view", () => {
  const markup = vm.runInNewContext(`(${extractFunction(app, "accountAdminModalMarkup")})`, {
    escapeHtml,
  });
  const superMarkup = markup({ showReportChatArchives: true });
  const operatorMarkup = markup({ showReportChatArchives: false });
  const sectionPattern = /<section[^>]*id="accountAdminReportChatArchiveSection"[^>]*>/u;
  const superSection = superMarkup.match(sectionPattern)?.[0] || "";
  const operatorSection = operatorMarkup.match(sectionPattern)?.[0] || "";

  assert.match(superMarkup, /RAG 问答档案/u);
  assert.doesNotMatch(superSection, /\bhidden\b/u);
  assert.match(operatorSection, /\bhidden\b/u);
  assert.match(app, /showReportChatArchives:\s*canManageUsers/u);
  assert.match(app, /if \(canManageUsers\) \{\s*loadAdminHotReports\(workerUrl, targets\);\s*loadAdminReportChatHistory\(workerUrl, targets\);/u);
});

test("RAG history loader accepts legacy and current API shapes and renders counts and curation state", async () => {
  const calls = [];
  const sandbox = installArchiveHelpers({
    escapeHtml,
    formatAdminDateTime(value) { return `time:${value}`; },
    authHeaders() { return { Authorization: "Bearer super" }; },
    async fetch(url, options) {
      calls.push({ url: String(url), options });
      return {
        ok: true,
        async json() {
          return {
            total: 2,
            items: [
              {
                id: "legacy-1",
                question: "Legacy <question>",
                created_at: "2026-08-29T12:00:00Z",
                tier: "guest",
                status: "completed",
                sources: [{}, {}],
                charts: { first: {} },
                published: false,
                public_id: "public-legacy",
              },
              {
                archive_id: "current-2",
                query: "Current question",
                ts: "2026-08-30T09:00:00Z",
                actor: { kind: "account", role: "user" },
                policy: { tier: "advanced" },
                answer_status: "failed",
                response: {
                  sources: [{}, {}, {}],
                  charts: [{}, {}],
                  executive_summary: "Executive <img src=x onerror=alert(1)>",
                  findings: [{
                    title: "Finding <one>",
                    summary: "Evidence & interpretation",
                  }],
                  data_points: [{
                    label: "Revenue <2026>",
                    value: "100 & rising",
                    context: "FY <full year>",
                  }],
                },
                published: false,
              },
            ],
          };
        },
      };
    },
  });
  const targets = {
    canManageUsers: true,
    reportChatArchiveSection: {},
    reportChatArchiveList: { innerHTML: "" },
    reportChatArchiveStatus: { className: "", textContent: "" },
    reportChatArchiveRefresh: { disabled: false },
  };

  const items = await sandbox.loadAdminReportChatHistory("/api", targets);

  assert.equal(items.length, 2);
  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, "/api/account-admin/report-chat-history?limit=50");
  assert.equal(calls[0].options.cache, "no-store");
  assert.equal(calls[0].options.headers.Authorization, "Bearer super");
  assert.match(targets.reportChatArchiveList.innerHTML, /Legacy &lt;question&gt;/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /time:2026-08-29T12:00:00Z · guest · completed · 来源 2 · 图表 1 · 已公开/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /data-report-chat-curation="unpublish"/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /data-archive-id="legacy-1"/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /Current question/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /advanced · failed · 来源 3 · 图表 2 · 未公开/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /data-report-chat-curation="publish"/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /data-archive-id="current-2"/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /<details class="account-admin-report-chat-details"><summary>查看回答内容<\/summary>/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /Executive &lt;img src=x onerror=alert\(1\)&gt;/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /Finding &lt;one&gt;/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /Evidence &amp; interpretation/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /Revenue &lt;2026&gt;/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /100 &amp; rising/u);
  assert.match(targets.reportChatArchiveList.innerHTML, /FY &lt;full year&gt;/u);
  assert.doesNotMatch(targets.reportChatArchiveList.innerHTML, /<img src=x/u);
  const answerFallback = sandbox.normalizeAdminReportChatArchive({
    archive_id: "answer-fallback",
    question: "Fallback",
    response: { answer: "Fallback answer" },
  });
  assert.match(sandbox.adminReportChatArchiveRow(answerFallback), /Fallback answer/u);
  assert.equal(targets.reportChatArchiveRefresh.disabled, false);
  assert.equal(targets.reportChatArchiveStatus.className, "status-line ok");
});

test("RAG history loader skips non-super views and exposes empty and error states", async () => {
  let mode = "empty";
  let fetchCount = 0;
  const sandbox = installArchiveHelpers({
    escapeHtml,
    formatAdminDateTime(value) { return value; },
    authHeaders() { return {}; },
    async fetch() {
      fetchCount += 1;
      if (mode === "error") {
        return { ok: false, async json() { return { detail: "后台读取失败" }; } };
      }
      return { ok: true, async json() { return { history: [], total: 0 }; } };
    },
  });
  const targets = {
    canManageUsers: false,
    reportChatArchiveSection: {},
    reportChatArchiveList: { innerHTML: "unchanged" },
    reportChatArchiveStatus: { className: "", textContent: "" },
    reportChatArchiveRefresh: { disabled: false },
  };

  assert.equal((await sandbox.loadAdminReportChatHistory("/api", targets)).length, 0);
  assert.equal(fetchCount, 0);
  assert.equal(targets.reportChatArchiveList.innerHTML, "unchanged");

  targets.canManageUsers = true;
  await sandbox.loadAdminReportChatHistory("/api", targets);
  assert.equal(fetchCount, 1);
  assert.match(targets.reportChatArchiveList.innerHTML, /还没有 RAG 问答存档/u);
  assert.equal(targets.reportChatArchiveStatus.className, "status-line ok");

  mode = "error";
  await sandbox.loadAdminReportChatHistory("/api", targets);
  assert.equal(fetchCount, 2);
  assert.match(targets.reportChatArchiveList.innerHTML, /暂时无法读取/u);
  assert.equal(targets.reportChatArchiveStatus.className, "status-line error");
  assert.equal(targets.reportChatArchiveStatus.textContent, "后台读取失败");
  assert.equal(targets.reportChatArchiveRefresh.disabled, false);
});

test("RAG curation posts the exact archive action and the UI refreshes after success", async () => {
  const calls = [];
  const sandbox = installArchiveHelpers({
    escapeHtml,
    formatAdminDateTime(value) { return value; },
    authHeaders() { return { Authorization: "Bearer super" }; },
    async fetch(url, options) {
      calls.push({ url: String(url), options });
      return { ok: true, async json() { return { ok: true }; } };
    },
  });

  await sandbox.curateAdminReportChatArchive("/api", "archive-42", "publish");
  assert.equal(calls.length, 1);
  assert.equal(calls[0].url, "/api/account-admin/report-chat-curation");
  assert.equal(calls[0].options.method, "POST");
  assert.equal(calls[0].options.cache, "no-store");
  assert.equal(calls[0].options.headers.Authorization, "Bearer super");
  assert.equal(calls[0].options.headers["Content-Type"], "application/json");
  assert.deepEqual(JSON.parse(calls[0].options.body), {
    archive_id: "archive-42",
    published: true,
  });
  await sandbox.curateAdminReportChatArchive("/api", "archive-42", "unpublish");
  assert.deepEqual(JSON.parse(calls[1].options.body), {
    archive_id: "archive-42",
    published: false,
  });
  await assert.rejects(
    sandbox.curateAdminReportChatArchive("/api", "archive-42", "delete"),
    /问答存档操作无效/u,
  );
  assert.equal(calls.length, 2, "invalid actions are rejected before transport");
  assert.match(app, /await curateAdminReportChatArchive\(workerUrl, archiveId, action\);[\s\S]*?await loadAdminReportChatHistory\(workerUrl, targets\);/u);
});

test("analytics labels cover RAG, RAG interactions, and course material requests", () => {
  assert.match(app, /report_chat:\s*"RAG 研究问答"/u);
  assert.match(app, /report_chat_interaction:\s*"RAG 问答交互"/u);
  assert.match(app, /course_material_request:\s*"课程材料索取"/u);
});
