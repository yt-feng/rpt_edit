import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);
const workerSource = await readFile(workerPath, "utf8");

function extractFunction(source, name) {
  const markers = [`function ${name}(`, `async function ${name}(`];
  const start = markers.reduce((found, marker) => {
    const index = source.indexOf(marker);
    return index >= 0 && (found < 0 || index < found) ? index : found;
  }, -1);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
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

function brandContext(globals = {}) {
  const start = workerSource.indexOf("const PUBLIC_BRAND");
  const end = workerSource.indexOf("const ADMIN_TOKEN_TTL_SECONDS", start);
  assert.notEqual(start, -1);
  assert.notEqual(end, -1);
  const context = vm.createContext({ ...globals });
  vm.runInContext(`${workerSource.slice(start, end)}\nglobalThis.brandFns = { publicBrandText, publicSourceText };`, context);
  return context;
}

function addFunctions(context, names) {
  for (const name of names) {
    context[name] = vm.runInContext(`(${extractFunction(workerSource, name)})`, context);
  }
  return context;
}

const oldNotesBrand = ["KC", "Desk", "Notes"].join(" ");
const legacySourcePattern = new RegExp(
  ["Reportify", "Nash[\\s._-]*AI", "Macro[\\s._-]*Gate", "Support[\\s._-]*Contact", "Portal[\\s._-]+Suite", oldNotesBrand, "Two[\\s._-]*tigers", "慧博", "hibor\\.com\\.cn"].join("|"),
  "iu",
);

test("public report metadata removes aggregator brands while preserving real institutions", () => {
  const context = addFunctions(brandContext(), ["publicSearchItem", "publicSearchPayload", "reportAPublicText"]);
  const payload = context.publicSearchPayload("external", {
    items: [{
      id: "external-1",
      title: "Reportify | AI Infrastructure Outlook",
      title_cn: "NashAI：人工智能基础设施",
      institution: "Nash AI",
      channel_name: "Reportify",
      author: "Goldman Sachs Research",
      summary: "MacroGate - source summary",
    }],
    institutions: [
      { value: "NashAI", label: "NashAI", count: 1 },
      { value: "Morgan Stanley", label: "Morgan Stanley", count: 2 },
    ],
  });

  assert.equal(payload.items[0].title, "AI Infrastructure Outlook");
  assert.equal(payload.items[0].title_cn, "人工智能基础设施");
  assert.equal(payload.items[0].institution, "");
  assert.equal(payload.items[0].author, "Goldman Sachs Research");
  assert.equal(Object.hasOwn(payload.items[0], "channel_name"), false);
  assert.equal(payload.institutions.length, 1);
  assert.equal(payload.institutions[0].label, "Morgan Stanley");
  assert.doesNotMatch(JSON.stringify(payload), legacySourcePattern);
  assert.equal(context.brandFns.publicSourceText("HIBOR rises with funding costs"), "HIBOR rises with funding costs");
  assert.equal(context.brandFns.publicSourceText("Ｎａｓｈ\u200bＡＩ：Full-width source"), "Full-width source");
  assert.equal(context.reportAPublicText("HIBOR rises with funding costs"), "HIBOR rises with funding costs");
  assert.equal(context.reportAPublicText("慧博 | China rates outlook"), "China rates outlook");
  assert.equal(context.brandFns.publicSourceText("Nash\u200bAI: Hidden marker title"), "Hidden marker title");
  assert.equal(context.brandFns.publicSourceText("Portal.Suite: Dotted marker title"), "Dotted marker title");
  assert.equal(context.brandFns.publicSourceText("From reportify.cn · Clean title"), "Clean title");
});

test("fresh, stale and mirror search responses all pass the same public boundary", async () => {
  let cachedPayload = {
    items: [{ id: "fresh", title: "Reportify: Fresh title", institution: "NashAI" }],
  };
  let fresh = true;
  const context = addFunctions(brandContext({
    getSearchCache: async () => ({ cached_at: "2026-08-31T00:00:00.000Z", payload: cachedPayload }),
    cachedPayloadIsFresh: () => fresh,
    jsonResponse: (_request, _env, status, payload) => ({ status, payload }),
    putSearchCache: async () => {},
    searchPayloadHasItems: (payload) => Boolean(payload && payload.items && payload.items.length),
  }), ["publicSearchItem", "publicSearchPayload", "handleCachedSearch"]);

  const fetcher = async () => { throw new Error("upstream unavailable"); };
  const freshResponse = await context.handleCachedSearch({}, {}, "external", "AI", 1, { items: [] }, fetcher);
  assert.equal(freshResponse.payload.items[0].title, "Fresh title");
  assert.equal(freshResponse.payload.items[0].institution, "");

  fresh = false;
  cachedPayload = { items: [{ id: "stale", title: "NashAI - Stale title", institution: "Jefferies" }] };
  const staleResponse = await context.handleCachedSearch({}, {}, "external", "AI", 1, { items: [] }, fetcher);
  assert.equal(staleResponse.payload.cache_status, "stale");
  assert.equal(staleResponse.payload.items[0].title, "Stale title");
  assert.equal(staleResponse.payload.items[0].institution, "Jefferies");

  cachedPayload = { items: [] };
  const mirrorResponse = await context.handleCachedSearch(
    {},
    {},
    "authority",
    "AI",
    1,
    { items: [] },
    fetcher,
    async () => ({ items: [{ id: "mirror", title: `${oldNotesBrand}: Mirror title`, institution: "MacroGate" }] }),
  );
  assert.equal(mirrorResponse.payload.cache_status, "mirror");
  assert.equal(mirrorResponse.payload.items[0].title, "Mirror title");
  assert.equal(mirrorResponse.payload.items[0].institution, "");
  assert.doesNotMatch(JSON.stringify(mirrorResponse.payload), legacySourcePattern);
});

test("stored contact targets are sanitized again on every normalization", () => {
  const context = addFunctions(brandContext({
    CONTACT_REPORT_SOURCES: new Set(["report-a", "authority"]),
    HIBOR_SOURCE: "report-a",
    AUTHORITY_SOURCE: "authority",
    Date,
  }), [
    "cleanReportRequestText",
    "cleanPublicReportText",
    "cleanContactReportSource",
    "cleanContactReportOriginId",
    "normalizeHotReportDate",
    "normalizeContactReportTarget",
  ]);

  const target = context.normalizeContactReportTarget({
    source: "report-a",
    id: "report-a:legacy-1",
    title: "Reportify | Global AI Outlook",
    institution: "NashAI",
    author: "MacroGate",
    category: "Technology",
    date: "2026-08-31",
  }, "report-a", "report-a:legacy-1");
  assert.equal(target.title, "Global AI Outlook");
  assert.equal(target.institution, "");
  assert.equal(target.author, "");
  assert.equal(target.category, "Technology");
  assert.doesNotMatch(JSON.stringify(target), legacySourcePattern);
});

test("user-facing brand positions use the canonical public brand", () => {
  const context = brandContext();
  for (const oldBrand of ["Portal Suite", "Portal Alternate", "Portal 娱乐", "Support Contact", "MacroGate", "Twotigers"]) {
    assert.equal(context.brandFns.publicBrandText(oldBrand), "KC桌面");
  }
  assert.doesNotMatch(workerSource, /CONTACT_WECHAT|Contact WeChat|联系微信/u);
  assert.match(workerSource, /embedded-v2:/u);
  assert.doesNotMatch(workerSource, /embedded-v1:/u);
});

test("admin file labels are sanitized before the dashboard response", () => {
  const context = addFunctions(brandContext(), ["publicAdminFile"]);
  const row = context.publicAdminFile({
    label: "Portal 娱乐视频",
    name: "Portal Alternate clip.mp4",
    recommended_account: "Portal 娱乐",
    account_label_reason: "Portal 娱乐专属内容",
  });
  assert.equal(row.label, "KC桌面视频");
  assert.equal(row.name, "KC桌面 clip.mp4");
  assert.equal(row.recommended_account, "KC桌面");
  assert.equal(row.account_label_reason, "KC桌面专属内容");
});
