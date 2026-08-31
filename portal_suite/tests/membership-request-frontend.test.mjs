import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appSource = await readFile(new URL("../site_src/assets/app.js", import.meta.url), "utf8");

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
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

test("account modal exposes a public in-site membership request form", () => {
  let session = null;
  const render = vm.runInNewContext(`(${extractFunction(appSource, "accountModalMarkup")})`, {
    loadAuthSession() { return session; },
    membershipRequestCopy(kind) {
      return { kind: kind || "membership", title: "申请加入会员", button: "提交会员申请", note: "留下联系方式" };
    },
    titleText() { return ""; },
    escapeHtml(value) { return String(value || ""); },
    accessContactGuidanceHtml() { return "提交站内申请"; },
    authUserLabel() { return "账户"; },
    registrationNoticeText() { return "账号提示"; },
  });

  const guestMarkup = render({ requestKind: "membership" });
  assert.match(guestMarkup, /id="membershipRequestForm"/u);
  assert.match(guestMarkup, /name="requester_email"[^>]*required/u);
  assert.match(guestMarkup, /name="contact_channel"[^>]*required/u);
  assert.match(guestMarkup, /value="wechat"/u);
  assert.match(guestMarkup, /value="whatsapp"/u);
  assert.match(guestMarkup, /value="telegram"/u);
  assert.match(guestMarkup, /name="contact_value"[^>]*required/u);
  assert.match(guestMarkup, /name="note"/u);
  assert.match(guestMarkup, /name="website"/u);
  assert.doesNotMatch(guestMarkup, /\/membership\/contact-card/u);
  assert.match(guestMarkup, /id="accountContactQrImage" alt="KC桌面会员联系二维码">/u);
  assert.doesNotMatch(guestMarkup, /id="accountContactQrImage"[^>]*\ssrc=/u);

  session = { token: "member-token", user: { email: "member@example.com" } };
  const memberMarkup = render({});
  assert.match(memberMarkup, /value="member@example\.com"[^>]* readonly/u);
});

test("membership request posts the bounded contact payload through the site", () => {
  const modalSource = extractFunction(appSource, "showAccountModal");
  assert.match(modalSource, /fetch\(`\$\{workerUrl\}\/membership\/request`/u);
  for (const field of [
    "requester_email", "contact_channel", "contact_value", "request_kind", "page_path", "honeypot",
  ]) {
    assert.match(modalSource, new RegExp(`\\b${field}:`, "u"));
  }
  assert.match(modalSource, /\bnote,/u);
  assert.match(modalSource, /\["wechat", "whatsapp", "telegram"\]\.includes\(contactChannel\)/u);
  assert.match(modalSource, /headers: \{ "Content-Type": "application\/json", \.\.\.authHeaders\(\) \}/u);
  assert.doesNotMatch(appSource, /mailto:/iu);
});

test("contact QR is server-verified, automatic for members, and revoked on teardown", () => {
  const modalSource = extractFunction(appSource, "showAccountModal");
  const verifyStart = modalSource.indexOf("async function refreshVerifiedContactQr()");
  const verifyEnd = modalSource.indexOf("function disposeAccountModal()", verifyStart);
  const verifySource = modalSource.slice(verifyStart, verifyEnd);
  assert.ok(verifyStart >= 0 && verifyEnd > verifyStart);
  assert.match(verifySource, /if \(!localSession\) \{[\s\S]*?return;/u);
  assert.ok(
    verifySource.indexOf("if (!localSession)") < verifySource.indexOf("refreshAuthSession(workerUrl)"),
    "guest flow must return before server session verification",
  );
  assert.match(verifySource, /const verifiedSession = await refreshAuthSession\(workerUrl\)/u);
  assert.match(verifySource, /memberContact\.hidden = false;[\s\S]*?loadVerifiedContactQr\(\);/u);

  const loaderStart = modalSource.indexOf("async function loadVerifiedContactQr()");
  const loaderEnd = modalSource.indexOf("async function refreshVerifiedContactQr()", loaderStart);
  const loaderSource = modalSource.slice(loaderStart, loaderEnd);
  assert.match(loaderSource, /\/membership\/contact-card/u);
  assert.match(loaderSource, /headers: authHeaders\(\)/u);
  assert.match(loaderSource, /URL\.createObjectURL\(blob\)/u);
  assert.match(loaderSource, /contactQrToggle\.hidden = false/u);
  assert.match(modalSource, /contactQrToggle\.addEventListener\("click", refreshVerifiedContactQr\)/u);
  assert.match(modalSource, /URL\.revokeObjectURL\(contactQrObjectUrl\)/u);
  assert.match(modalSource, /function disposeAccountModal\(\) \{[\s\S]*?revokeContactQr\(\);/u);
  assert.doesNotMatch(modalSource, /显示联系二维码/u);
});
