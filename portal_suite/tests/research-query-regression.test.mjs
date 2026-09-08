import assert from "node:assert/strict";
import { createHash } from "node:crypto";
import { readFile } from "node:fs/promises";
import { fileURLToPath, pathToFileURL } from "node:url";
import path from "node:path";
import test from "node:test";

// Exercise the production functions without exposing a new public Worker API.
const workerFile = fileURLToPath(new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url));
let source = await readFile(workerFile, "utf8");
source = source.replace(/from "\.\/([^"]+)"/gu, (_match, relative) => `from "${pathToFileURL(path.join(path.dirname(workerFile), relative)).href}"`);
source += "\nexport { reportResearchDeterministicPlan, sanitizeReportResearchPlan, reportResearchMatchedGroupTerms, reportResearchChartTokenMatches, reportResearchCharts, normalizeText };";
const functions = await import(`data:text/javascript;base64,${Buffer.from(source).toString("base64")}`);
const { reportResearchDeterministicPlan: planFor, sanitizeReportResearchPlan: enrich, reportResearchMatchedGroupTerms: matchGroup, reportResearchChartTokenMatches: matchTerm, reportResearchCharts: chartsFor, normalizeText } = functions;
const question = "中国AI数据中心的功率容量和用电需求未来会如何增长？请结合2025-2030预测图表，说明电力供给瓶颈与算力基础设施的约束。";
const imageId = (title) => createHash("sha256").update(title).digest("hex");
const chart = (title, fields = {}) => ({
  id: imageId(title).slice(0, 32), image_id: imageId(title), analysis_version: "chart-search-v2",
  title, content_kind: "chart", quality_score: 90, chart_type: "line",
  description: title, trend_summary: "", metrics: [], entities: [], periods: [], geographies: [], units: [], keywords: [], ...fields,
});
const gallery = (reports) => ({ REPORT_BUCKET: { async get(key) {
  assert.equal(key, "_chart-search/v1/index.json");
  return { async text() { return JSON.stringify({ schema_version: 1, reports }); } };
} } });
const report = (title, charts, report_id = "") => ({ title, report_id, date_folder: "260905", charts });

// Public gallery fields observed in production; no report body excerpts are fixtures.
const powerForecast = chart("Data center power capacity and consumption forecast (2025E–2030E)", {
  description: "左侧为新AI数据中心设施总功率(MW)，右侧为已安装数据中心电力消耗(rhs)。",
  metrics: ["Total facility power_new AIDCs (MW)", "Power consumption of data center_installed (rhs)"],
  entities: ["AIDCs", "data center"], periods: ["2025E", "2026E", "2030E"], units: ["MW", "rhs"],
  keywords: ["数据中心", "电力消耗", "AI数据中心", "新AIDC", "power consumption", "facility power"],
});
const chinaCapacity = chart("中国数据中心容量、需求与利用率(2017–2030E)", {
  description: "中国数据中心容量和需求持续增长，图中区分容量、需求与利用率。",
  metrics: ["Data Center Live Capacity (GW)", "Data Center Demand (GW)", "Utilization rate"],
  periods: ["2017", "2030E"], geographies: ["China"], units: ["GW", "%"],
});
const usShortfall = chart("Potential Shortfall in Power for US Data Centers, 2026-28", {
  description: "US data center power needed exceeds available or contracted grid capacity.",
  metrics: ["US Power Needed", "US DCs Under Construction", "Available/Contracted US Grid Capacity", "Potential Shortfall"],
  periods: ["2026", "2028"], geographies: ["US"],
});

function observedGallery(extra = []) {
  return gallery([
    report("JPM-China AI Infra Ecosystem: growth and constraints", [powerForecast]),
    report("GS-China Data Centers: fastest growing AI computing clusters", [chinaCapacity]),
    report("MS-US Thematics: Power Struggle, Data Center Pushback", [usShortfall]),
    ...extra,
  ]);
}

test("canonical aliases survive CJK expansion and seven lookups keep the physical metrics", () => {
  const plan = planFor(question);
  const ai = plan.core.find((group) => group.terms.includes("ai"));
  assert.ok(ai.terms.includes("aidc"));
  assert.ok(ai.terms.includes("aidcs"));
  assert.equal(plan.lookup.length, 7);
  for (const term of ["power", "capacity", "consumption", "china"]) assert.ok(plan.terms.includes(term), term);
  assert.equal(plan.core.some((group) => ["增长", "功率容量", "用电"].includes(group.name)), false);
  assert.equal(plan.terms.some((term) => /^\d/u.test(term)), false);
});

test("mixed Chinese/Latin boundaries and plural AIDCs match without substring false positives", () => {
  const ai = planFor(question).core.find((group) => group.terms.includes("ai"));
  for (const text of ["新AI数据中心", "中国AI数据中心", "AIDCs", "AIDC"]) assert.ok(matchGroup(normalizeText(text), ai).length, text);
  for (const text of ["airline", "openai", "maintain", "saidc"]) assert.equal(matchTerm(text, "ai"), false);
  const dc = planFor(question).core.find((group) => group.terms.includes("datacenter"));
  assert.ok(matchGroup("aidcs", dc).length);
  assert.equal(planFor("AIDCs power capacity").core.filter((group) => group.required).length, 2);
});

test("model enrichment cannot merge core concepts or turn compound metrics into demand aliases", () => {
  const fallback = planFor(question);
  const plan = enrich({
    core: [{ name: "AI data center", terms: ["ai", "data", "center"] }],
    facets: [{ name: "power demand", terms: ["power", "demand", "capacity"] }],
    terms: ["ai", "data", "power", "capacity", "consumption", "china", "supply"],
  }, fallback);
  const ai = plan.core.find((group) => group.terms.includes("ai"));
  assert.equal(ai.terms.includes("data"), false);
  assert.equal(plan.core.filter((group) => group.required).length, 2);
  const power = plan.facets.find((group) => group.metric_kind === "electricity");
  assert.equal(power.terms.includes("demand"), false);
});

test("power capacity and electricity use reject HBM capacity or generic demand", () => {
  const plan = planFor(question);
  const capacity = plan.facets.find((group) => group.metric_kind === "power_capacity");
  const consumption = plan.facets.find((group) => group.metric_kind === "electricity_consumption");
  for (const group of [capacity, consumption, plan.facets.find((group) => group.metric_kind === "electricity")]) {
    for (const adjective of ["computing", "computational"]) assert.equal(matchGroup(`ai data center hbm memory capacity 80 gb and gpu demand grow as ${adjective} power capacity expands`, group).length, 0);
  }
  assert.ok(matchGroup(normalizeText("Data Center Live Capacity (GW)"), capacity).length);
  assert.ok(matchGroup("electricity demand grows", consumption).length);
  const mixed = normalizeText("AI data center HBM memory capacity is 80 GB. A server rack draws 10 kW. HBM demand grows.");
  assert.equal(matchGroup(mixed, capacity).length, 0);
  assert.equal(matchGroup(mixed, consumption).length, 0);
  assert.ok(matchGroup("capacity reaches 18 gw", capacity).length);
  assert.ok(matchGroup("demand 400 twh", consumption).length);
});

test("real chart schema retrieves physical forecasts ahead of HBM and preserves geographic scope", async () => {
  const hbm = Array.from({ length: 3 }, (_unused, index) => chart(`AI GPU and AI ASIC HBM demand ${index}`, {
    description: "AI data center memory capacity, supply and demand forecast for China; increasing HBM consumption.",
    metrics: ["HBM capacity", "HBM demand"], units: ["GB"], keywords: ["AI", "data center", "supply", "demand", "capacity", "China"],
    geographies: ["China"], quality_score: 100,
  }));
  const rows = await chartsFor(observedGallery([report("AI server memory demand", hbm)]), question, [], planFor(question));
  assert.equal(rows.length, 3);
  assert.ok(rows.some((row) => row.image_id === powerForecast.image_id));
  const china = rows.find((row) => row.image_id === chinaCapacity.image_id);
  assert.ok(china);
  assert.match(china.description, /AI关联来自所属报告/u);
  assert.deepEqual(china.units, ["GW", "%"]);
  const us = rows.find((row) => row.image_id === usShortfall.image_id);
  assert.match(us.description, /一般数据中心电力约束/u);
  assert.match(us.description, /原图地区：US/u);
  assert.match(us.description, /不代表中国预测/u);
  assert.deepEqual(us.periods, ["2026", "2028"]);
  assert.match(rows.find((row) => row.image_id === powerForecast.image_id).description, /未独立标明地区/u);
});

test("equal physical metrics rank the requested geography first", async () => {
  const china = chart("China AI data center electricity capacity", { metrics: ["Power capacity"], units: ["GW"], geographies: ["China"] });
  const us = chart("US AI data center electricity capacity", { metrics: ["Power capacity"], units: ["GW"], geographies: ["US"], quality_score: 100 });
  const rows = await chartsFor(gallery([report("China AI", [china]), report("US AI", [us])]), question, [], planFor(question));
  assert.equal(rows[0].image_id, china.image_id);
});

test("unlinked charts share the per-report cap and unrelated required subjects remain excluded", async () => {
  const duplicates = Array.from({ length: 4 }, (_unused, index) => chart(`AI data center power grid ${index}`, { description: "AI data center power demand rises", units: ["GW"] }));
  const unrelated = chart("AI software power usage", { description: "Enterprise software electricity demand rises" });
  const rows = await chartsFor(gallery([report("One shared report", duplicates), report("AI software", [unrelated])]), "AI data center power", [], planFor("AI data center power"));
  assert.equal(rows.length, 2);
  assert.ok(rows.every((row) => row.report_id === "" && row.source_id === `chart:${row.image_id}`));
  const required = planFor("AI semiconductor power");
  assert.equal((await chartsFor(observedGallery(), "AI semiconductor power", [], required)).length, 0);
});


test("explicit US chart geography cannot be overridden by China in a company title", async () => {
  const mixed = chart("China companies data center power capacity", {
    description: "US data center power capacity forecast; Chinese suppliers serve this market.",
    metrics: ["Power capacity"], units: ["GW"], geographies: ["US"],
  });
  const rows = await chartsFor(gallery([report("China companies", [mixed])]), question, [], planFor(question));
  assert.equal(rows.length, 1);
  assert.match(rows[0].description, /原图地区：US/u);
  assert.match(rows[0].description, /不代表中国预测/u);
});


test("HBM capacity and demand research retains complementary demand charts", async () => {
  const question = "半导体HBM产能与需求未来如何增长？";
  const demand = chart("Semiconductor HBM demand forecast", {
    description: "HBM demand from AI GPU and ASIC products rises through 2027.",
    metrics: ["HBM demand"], entities: ["semiconductor", "HBM"], units: ["GB"],
    keywords: ["半导体", "HBM", "需求"],
  });
  const capacity = chart("Semiconductor HBM production capacity", {
    description: "HBM capacity expands in semiconductor fabs.",
    metrics: ["HBM production capacity"], entities: ["semiconductor", "HBM"], units: ["wafers/month"],
    keywords: ["半导体", "HBM", "产能"],
  });
  const plan = planFor(question);
  assert.equal(plan.facets.find((group) => group.name === "容量").metric_kind, "");
  const rows = await chartsFor(gallery([report("HBM demand report", [demand]), report("HBM production report", [capacity])]), question, [], plan);
  assert.deepEqual(new Set(rows.map((row) => row.image_id)), new Set([demand.image_id, capacity.image_id]));
});

test("bank earnings and capex research retains both independent financial metrics", async () => {
  const question = "比较中国与美国银行盈利和资本开支";
  const earnings = chart("中国与美国银行盈利对比", {
    description: "中国银行与美国银行盈利增长和净息差变化。",
    metrics: ["银行利润", "earnings", "net interest margin"], geographies: ["China", "US"], keywords: ["银行", "盈利", "earnings"],
  });
  const capex = chart("中国与美国银行资本开支", {
    description: "中国与美国银行的资本开支变化。", metrics: ["Capital expenditure"], geographies: ["China", "US"], keywords: ["银行", "capex"],
  });
  const plan = planFor(question);
  assert.equal(plan.facets.find((group) => group.name === "资本开支").metric_kind, "");
  const rows = await chartsFor(gallery([report("Bank earnings", [earnings]), report("Bank capex", [capex])]), question, [], plan);
  assert.deepEqual(new Set(rows.map((row) => row.image_id)), new Set([earnings.image_id, capex.image_id]));
});
