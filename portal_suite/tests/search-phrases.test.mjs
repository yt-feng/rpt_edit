import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const source = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");
const context = { CONTENT_INTL_LOCALE: "zh-CN" };
vm.createContext(context);
vm.runInContext(source.slice(source.indexOf("  function localeSearchText("),
  source.indexOf("  async function loadJson(")), context);
const { normalize, textMatches, scoreText } = context;
const title = "Bernstein-European Capital Goods Future of Tech-AI Data Centers to unlock Solid-State Transformation-260325";

test("reported full title, middle phrases, case and dash variants all match", () => {
  for (const query of ["AI Data Centers to unlock Solid-State Transformation", "unlock solid",
    "UNLOCK SOLID", "Solid–State Transformation", "Data Centers", "固态 转型"]) {
    assert.equal(textMatches(normalize(title + " AI数据中心将开启固态转型"), normalize(query)), true, query);
  }
});

test("pasted long titles tolerate missing connective words but require all subject terms", () => {
  const indexed = normalize("AI Data Centers unlock Solid-State Transformation");
  assert.equal(textMatches(indexed, normalize("AI Data Centers to unlock Solid-State Transformation")), true);
  assert.equal(textMatches(indexed, normalize("AI Data Centers to unlock Battery Transformation")), false);
  assert.equal(textMatches(indexed, normalize("AI Data Centers not unlock Solid-State Transformation")), false);
  assert.equal(textMatches(indexed, normalize("AI Data Centers 2027")), false);
  assert.equal(textMatches(indexed, "to"), false);
});

test("PDF copy invisible separators do not split a search word", () => {
  assert.equal(normalize("Transfor\u00admation Data\u200b Centers"), "transformation data centers");
  assert.equal(textMatches(normalize(title), normalize("Transfor\u00admation")), true);
});

test("exact middle phrases rank above scattered keywords", () => {
  assert.ok(scoreText(normalize(title), "unlock solid", 12)
    > scoreText("solid state markets may unlock growth", "unlock solid", 12));
  assert.equal(textMatches("other report", "unlock solid"), false);
});

test("the search box explains full-title and middle-phrase search accessibly", async () => {
  const html = await readFile(new URL("../site_src/index.html", import.meta.url), "utf8");
  assert.match(html, /aria-describedby="searchHelp"/);
  assert.match(html, /不用限定关键词个数/);
  assert.match(html, /unlock solid/);
});
