import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const app = (await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8")).replace(/^  /gm, "");

function fn(name) {
  const start = new RegExp(`^(?:async )?function ${name}\\(`, "m").exec(app);
  assert.ok(start, `missing ${name}`);
  const rest = app.slice(start.index);
  const next = /\n(?:async )?function \w+\(/.exec(rest);
  return next ? rest.slice(0, next.index) : rest;
}

function harness(initialSession = null, item = { id: "1300546606747226112", source: "external" }) {
  let session = initialSession;
  const listeners = new Map();
  const panel = { innerHTML: "" };
  const context = vm.createContext({
    EXTERNAL_SOURCE: "external", item, adminTools: {},
    loadAuthSession: () => session,
    canUseDeliveryTools: () => Boolean(session),
    isAuthorityItem: () => false, isReportAItem: () => false, isThinkTankItem: () => false, isHotReportItem: () => false,
    document: {
      getElementById: (id) => id === "externalAdminSource" ? panel : null,
      addEventListener: (name, listener) => listeners.set(name, listener),
    },
  });
  const detail = fn("initExternalDetail");
  const refresh = [...detail.matchAll(/^ {2}function refreshAdmin\(\) \{[\s\S]*?^ {2}\}/gm)].at(-1)?.[0];
  const bindings = detail.match(/ {2}document\.addEventListener\("portal-admin-change", refreshAdmin\);\n {2}document\.addEventListener\("portal-auth-change", refreshAdmin\);\n {2}refreshAdmin\(\);/)?.[0];
  assert.ok(refresh && bindings, "detail page must refresh admin controls on initial render and auth changes");
  vm.runInContext(`${fn("isSuperSession")}\n${fn("validDocId")}\n${fn("externalAdminSourceMarkup")}\n${refresh}\n${bindings}`, context);
  return {
    panel,
    changeSession(value) { session = value; listeners.get("portal-auth-change")(); },
  };
}

test("signed-in owner sees the canonical report source before any download or QR action", () => {
  const h = harness({ user: { username: "owner", role: "super" } });
  assert.match(h.panel.innerHTML, /href="https:\/\/reportify\.cn\/reports\/1300546606747226112"/);
  assert.match(h.panel.innerHTML, /target="_blank" rel="noopener noreferrer"/);
});

test("late login reveals the link and logout or loss of admin role removes the URL", () => {
  const h = harness();
  assert.equal(h.panel.innerHTML, "");
  h.changeSession({ user: { is_super: true } });
  assert.match(h.panel.innerHTML, /https:\/\/reportify\.cn\/reports\//);
  h.changeSession(null);
  assert.equal(h.panel.innerHTML, "");
  h.changeSession({ user: { role: "super" } });
  h.changeSession({ user: { role: "operator", username: "owner" } });
  assert.equal(h.panel.innerHTML, "");
});

test("ordinary members and a matching username without admin rights do not see the source link", () => {
  for (const role of ["user", "operator", ""]) {
    const h = harness({ user: { username: "owner", role } });
    assert.equal(h.panel.innerHTML, "");
  }
});

test("only valid external report IDs produce links and arbitrary metadata cannot select the destination", () => {
  const owner = { user: { role: "super" } };
  for (const item of [
    { id: "1300546606747226112", source: "hot" },
    { id: "1300546606747226112", source: "thinktank" },
    { id: "1300546606747226112" },
    { id: "123", source: "external" },
    { id: "1300546606747226112\" onclick=\"bad()", source: "external" },
  ]) {
    const h = harness(owner, item);
    assert.equal(h.panel.innerHTML, "");
  }
  const h = harness(owner, { id: "1300546606747226112", source: "external", source_url: "https://other.example/" });
  assert.match(h.panel.innerHTML, /https:\/\/reportify\.cn\/reports\//);
  assert.doesNotMatch(h.panel.innerHTML, /other\.example/);
});
