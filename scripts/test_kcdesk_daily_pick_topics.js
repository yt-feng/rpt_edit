const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.resolve(__dirname, "..");
const worker = fs.readFileSync(path.join(root, "workers/kc-desk-notes-worker/src/index.js"), "utf8");

function extractFunction(source, name) {
  const start = source.indexOf(`function ${name}(`);
  assert.ok(start >= 0, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  assert.ok(bodyStart >= 0, `${name} must have a body`);
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

function extractRange(source, startMarker, endMarker) {
  const start = source.indexOf(startMarker);
  const end = source.indexOf(endMarker, start);
  assert.ok(start >= 0, `${startMarker} must exist`);
  assert.ok(end > start, `${endMarker} must follow ${startMarker}`);
  return source.slice(start, end);
}

const topicRules = extractRange(
  worker,
  "const DAILY_PICK_KOREA_PATTERN",
  "function dailyPickPatternGroupHits",
);

const sandbox = {};
vm.runInNewContext(`
  ${extractFunction(worker, "normalizeText")}
  ${extractFunction(worker, "dailyPickSourceText")}
  ${extractFunction(worker, "dailyPickTitleText")}
  ${extractFunction(worker, "dailyPickBodyText")}
  ${extractFunction(worker, "textMatches")}
  ${extractFunction(worker, "addUnique")}
  ${topicRules}
  ${extractFunction(worker, "dailyPickPatternGroupHits")}
  ${extractFunction(worker, "dailyPickTopicProfile")}
  ${extractFunction(worker, "dailyPickTopicTags")}
  ${extractFunction(worker, "dailyPickThemes")}
  ${extractFunction(worker, "dailyPickBodyInsights")}
  ${extractFunction(worker, "chineseJoin")}
  function reportEnglishTitle(item) { return String(item.title || item.filename || "Untitled report"); }
  function reportPageCount(item) { return Number(item.page_count || 0) || 0; }
  function reportIsLandscape(item) { return item.first_page_landscape === true || item.first_page_orientation === "landscape"; }
  ${extractFunction(worker, "dailyPickIntro")}

  const koreaWeekly = {
    title: "GS-KOREA WEEKLY KICKSTART: KOSPI declined by 2% despite foreign inflows and Alphabet's AI capex boost",
    title_zh: "高盛-韩国每周启动：尽管外资流入，KOSPI仍下跌2%",
    filename: "GS-KOREA WEEKLY KICKSTART.pdf",
    bank_code: "GS",
    page_count: 20,
  };
  const incidentalBody = [
    "The report focuses on KOSPI positioning, foreign inflows and Korean equity performance.",
    "An appendix mentions energy once, commodities once, and lists the Middle East and Iran among global regions.",
  ].join(" ");
  const koreaWeeklyTags = dailyPickTopicTags(koreaWeekly, incidentalBody);
  result = {
    koreaWeeklyThemes: dailyPickThemes(koreaWeekly, koreaWeeklyTags, incidentalBody),
    koreaWeeklyTags,
    koreaWeeklyIntro: dailyPickIntro(koreaWeekly, koreaWeeklyTags, incidentalBody),
    koreaBokThemes: dailyPickThemes({
      title: "NOM-Asia Insights Korea: BOK delivers a unanimous decision for a 25bp hike",
      title_zh: "野村-亚洲洞察韩国：韩国央行一致决定加息25个基点",
      filename: "NOM-Asia Insights Korea.pdf",
    }, [], "The BOK raised its policy rate. Lower oil prices were mentioned once in the inflation discussion."),
    koreaBatteryThemes: dailyPickThemes({
      title: "MS-Asia Summer School: S. Korea Batteries",
      title_zh: "摩根士丹利-亚洲暑期学校：韩国电池",
      filename: "MS-Korea-Batteries.pdf",
    }, [], "Raw material costs rose. The appendix lists energy and the Middle East."),
    japanEnergyThemes: dailyPickThemes({
      title: "MS-Investor Presentation: Japan Summer School: Energy & Utilities",
      title_zh: "摩根士丹利-日本暑期学校：能源与公用事业",
      filename: "MS-Japan-Energy-Utilities.pdf",
    }, [], "Power demand, grid investment and renewable generation capacity are the main subjects."),
    oilIranThemes: dailyPickThemes({
      title: "Oil Market Outlook: Iran Supply Risk",
      title_zh: "原油市场展望：伊朗供应变化",
      filename: "Oil-Market-Outlook.pdf",
    }, [], "OPEC supply and crude inventories remain central to the outlook."),
    commodityThemes: dailyPickThemes({
      title: "Global Commodity Strategy: Copper, Gold and Iron Ore",
      title_zh: "全球大宗商品策略：铜、黄金与铁矿石",
      filename: "Global-Commodity-Strategy.pdf",
    }, [], "Mining supply and metal demand are the main drivers."),
    consumerPriceThemes: dailyPickThemes({
      title: "Consumer Prices and the Inflation Outlook",
      title_zh: "消费者价格与通胀展望",
      filename: "Consumer-Prices.pdf",
    }, [], "CPI and disinflation are the report's main subjects."),
    weakBodyThemes: dailyPickThemes({ title: "Asia Insights Weekly", filename: "Asia-Insights.pdf" }, [], "Oil was mentioned once."),
    strongBodyThemes: dailyPickThemes({ title: "Asia Insights Weekly", filename: "Asia-Insights.pdf" }, [], "Crude oil demand, OPEC supply and refinery inventories are the main focus."),
  };
`, sandbox);

const result = sandbox.result;
const koreaWeeklyThemes = Array.from(result.koreaWeeklyThemes);
const koreaWeeklyTags = Array.from(result.koreaWeeklyTags);
assert.equal(koreaWeeklyThemes[0], "韩国股票市场与资金流向", "Korea/KOSPI title must own the primary topic");
assert.ok(!koreaWeeklyThemes.some((theme) => /大宗商品|地缘政治/.test(theme)), "incidental body words must not become Korea-report themes");
assert.equal(koreaWeeklyTags[0], "韩国股市", "precise tags must precede the generic macro fallback");
assert.ok(!koreaWeeklyTags.includes("大宗商品"));
assert.match(result.koreaWeeklyIntro, /韩国股票市场与资金流向/);
assert.doesNotMatch(result.koreaWeeklyIntro, /大宗商品|地缘政治/);

assert.equal(Array.from(result.koreaBokThemes)[0], "韩国宏观与货币政策");
assert.ok(!Array.from(result.koreaBokThemes).slice(0, 3).some((theme) => /地缘政治|大宗商品/.test(theme)));
assert.ok(!Array.from(result.koreaBokThemes).some((theme) => /银行、保险/.test(theme)), "Bank of Korea must not be classified as a banking-industry report");
assert.equal(Array.from(result.koreaBatteryThemes)[0], "韩国汽车、电池与新能源产业");
assert.ok(!Array.from(result.koreaBatteryThemes).some((theme) => /大宗商品|地缘政治/.test(theme)));

assert.deepEqual(
  Array.from(result.japanEnergyThemes).slice(0, 2),
  ["能源与公用事业", "日本市场与政策趋势"],
  "country and industry evidence from the title must both survive in ranked order",
);
assert.deepEqual(
  Array.from(result.oilIranThemes).slice(0, 2),
  ["原油市场与供需", "地缘政治与贸易政策"],
  "oil and geopolitics should be separate only when both are explicit in the title",
);
assert.equal(Array.from(result.commodityThemes)[0], "大宗商品与金属矿业");
assert.equal(Array.from(result.consumerPriceThemes)[0], "通胀与价格路径");
assert.ok(!Array.from(result.consumerPriceThemes).some((theme) => /消费、零售/.test(theme)));
assert.ok(!Array.from(result.weakBodyThemes).some((theme) => /原油|大宗商品/.test(theme)), "one body mention must not classify a topic");
assert.equal(Array.from(result.strongBodyThemes)[0], "原油市场与供需", "multiple independent body anchors may classify the subject");

assert.match(worker, /daily_picks:\s*selectDailyPicks\(catalog, 5, searchIndex\)/, "the shared snapshot must use the corrected generator");
assert.match(worker, /const dailyPicks = Array\.isArray\(picksData\.daily_picks\)/, "management and operations dashboards must read the same pick snapshot");

console.log("KCdesk daily-pick topic checks passed.");
