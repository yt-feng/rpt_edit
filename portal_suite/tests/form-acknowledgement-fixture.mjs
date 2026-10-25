import assert from "node:assert/strict";

export const ACK_TAG = "portal-form-acknowledgement";
export const ACK_SENDER = ["info", "@", "kc", "desk", ".com"].join("");

export function assertAcknowledgement(email, recipient) {
  assert.deepEqual(email.tags, [ACK_TAG]);
  assert.equal(email.sender.email, ACK_SENDER);
  assert.equal(email.to.length, 1);
  if (recipient) assert.deepEqual(email.to, [{ email: recipient }]);
  assert.match(email.subject, /[\u3400-\u9fff]/u);
  assert.match(email.subject, /received/iu);
  for (const content of [email.textContent, email.htmlContent]) {
    assert.match(content, /任何疑问.*微信.*macroGate/u);
    assert.match(content, /questions.*WeChat.*macroGate/iu);
    assert.match(content, /WhatsApp.*\+1 \(740\) 875-3400/u);
  }
  assert.equal(email.cc, undefined);
  assert.equal(email.bcc, undefined);
}

// Existing owner-notification tests keep their exact owner assertions. This
// separate recipient is validated here and exercised end-to-end in its suite.
export async function withOwnerNotificationMock(mock, callback) {
  const original = globalThis.fetch;
  globalThis.fetch = async (url, init = {}) => {
    const body = String(url) === "https://api.brevo.com/v3/smtp/email"
      ? JSON.parse(String(init.body || "{}")) : null;
    if (body?.tags?.includes(ACK_TAG)) {
      assertAcknowledgement(body);
      return new Response(JSON.stringify({ messageId: "acknowledgement-fixture" }), { status: 201 });
    }
    return mock(url, init);
  };
  try { return await callback(); } finally { globalThis.fetch = original; }
}
