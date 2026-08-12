import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);
const workerPath = new URL("../../workers/portal-suite-worker/src/index.js", import.meta.url);

function extractNamedFunction(source, name) {
  const marker = `async function ${name}`;
  const start = source.indexOf(marker);
  assert.notEqual(start, -1, `${name} is missing`);
  const signatureEnd = source.indexOf(") {", start);
  assert.notEqual(signatureEnd, -1, `${name} has no function body`);
  const bodyStart = signatureEnd + 2;
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    if (source[index] !== "}") continue;
    depth -= 1;
    if (depth === 0) return source.slice(start, index + 1);
  }
  throw new Error(`${name} has no closing brace`);
}

async function rewardFetchHelper(fakeFetch) {
  const source = await readFile(appPath, "utf8");
  const declaration = extractNamedFunction(source, "fetchRewardRequest");
  return Function("fetch", "window", "AbortController", `${declaration}; return fetchRewardRequest;`)(
    fakeFetch,
    { setTimeout, clearTimeout },
    AbortController
  );
}

test("reward center explains the D1 and D3 ramp instead of promising a report every day", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /首签立即得 1 张报告券，第 3 天再得 1 张/);
  assert.match(source, /70 分可兑换 1 份报告/);
  assert.match(source, /id="accountRewardCredits"/);
  assert.match(source, /data\.next_milestone/);
  assert.doesNotMatch(source, /每日签到可领取一份报告/);
});

test("check-in and claims show immediate elapsed progress without a wait cursor", async () => {
  const [source, styles, worker] = await Promise.all([
    readFile(appPath, "utf8"),
    readFile(stylesPath, "utf8"),
    readFile(workerPath, "utf8"),
  ]);
  assert.match(source, /const actionToken = beginRewardAction\(rewardCheckin, "正在签到…"\)/);
  assert.match(source, /const actionToken = beginRewardAction\(button, kind === "daily" \? "正在使用报告券…" : "正在兑换报告…"\)/);
  assert.match(source, /已用时 \$\{seconds\.toFixed\(1\)\} 秒/);
  assert.match(source, /data-reward-elapsed aria-hidden="true"/);
  assert.match(source, /window\.setInterval\(update, 1_000\)/);
  assert.doesNotMatch(source, /window\.setInterval\(update, 250\)/);
  assert.match(source, /finishRewardAction\(actionToken\)/);
  assert.match(worker, /ctx\.waitUntil\(guarded\)/);
  assert.doesNotMatch(styles, /cursor:\s*wait/);
});

test("reward actions are single-flight and stale GET responses cannot unlock controls", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /let rewardActionToken = 0;/);
  assert.match(source, /let rewardActionActive = false;/);
  assert.match(source, /if \(rewardActionActive\) return 0;/);
  assert.match(source, /if \(!actionToken\) return;/);
  assert.match(source, /rewardRefreshRequest \+= 1;/);
  assert.match(source, /if \(request !== rewardRefreshRequest \|\| rewardActionActive\) return currentRewardState;/);
  assert.match(source, /if \(!rewardActionActive \|\| options\.forceControls\)/);
  assert.match(source, /if \(!rewardActionActive \|\| token !== rewardActionToken\) return;/);
});

test("reward action cleanup restores the pre-action labels when no state is available", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /rewardActionRestore = \[rewardCheckin, rewardDailyClaim, rewardPointsClaim\]/);
  assert.match(source, /disabled: control\.disabled/);
  assert.match(source, /text: control\.textContent/);
  assert.match(source, /function restoreRewardControls\(\)/);
  assert.match(source, /control\.disabled = disabled;/);
  assert.match(source, /control\.textContent = text;/);
  assert.match(source, /restoreRewardControls\(\);\s*if \(currentRewardState\)/);
});

test("reward requests enforce an 18-second AbortController deadline on GET, check-in, and claim", async () => {
  const source = await readFile(appPath, "utf8");
  assert.match(source, /async function fetchRewardRequest\([\s\S]*timeoutMs = 18_000\)/);
  assert.match(source, /fetchRewardRequest\(\s*`\$\{workerUrl\}\/rewards`[\s\S]*签到状态读取超时，请重试。/);
  assert.match(source, /fetchRewardRequest\(\s*`\$\{workerUrl\}\/rewards\/claim`[\s\S]*报告领取请求超时，请重试。/);
  assert.match(source, /fetchRewardRequest\(\s*`\$\{workerUrl\}\/rewards`[\s\S]*签到请求超时，请重试。/);
  assert.match(source, /controller\.abort\(\)/);
  assert.match(source, /Promise\.race/);
});

test("reward request rejects a fetch that never resolves and exposes a retryable timeout", async () => {
  const fetchRewardRequest = await rewardFetchHelper(() => new Promise(() => {}));
  await assert.rejects(
    fetchRewardRequest("/rewards", {}, "签到状态读取超时，请重试。", 10),
    (error) => error.name === "RewardTimeoutError" && error.message === "签到状态读取超时，请重试。"
  );
});

test("reward request normalizes AbortError into the same retryable timeout message", async () => {
  const fetchRewardRequest = await rewardFetchHelper(() => Promise.reject(Object.assign(new Error("aborted"), { name: "AbortError" })));
  await assert.rejects(
    fetchRewardRequest("/rewards/claim", {}, "报告领取请求超时，请重试。", 10),
    (error) => error.name === "RewardTimeoutError" && error.message === "报告领取请求超时，请重试。"
  );
});
