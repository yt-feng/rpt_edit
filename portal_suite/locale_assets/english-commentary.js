(function () {
  "use strict";
  const POLICY = "english-secondary-commentary-v1";
  const SESSION = "portal_auth_session";
  const TAGS = new Set(["p", "li", "h2", "h3", "h4"]);
  function session(raw) {
    try {
      const value = JSON.parse(raw || "null");
      return value && typeof value.token === "string" && value.token && value.user && value.user.id ? value : null;
    } catch (_) { return null; }
  }
  function validFull(value, id) {
    if (!value || value.id !== id || value.policy !== POLICY || !["member", "free"].includes(value.access)) return false;
    if (value.access === "member" ? value.remaining !== null : !Number.isInteger(value.remaining) || value.remaining < 0 || value.remaining > 3) return false;
    return Array.isArray(value.blocks) && value.blocks.length > 0 && value.blocks.length <= 500 && value.blocks.every((block) =>
      block && Object.keys(block).length === 2 && TAGS.has(block.tag) && typeof block.text === "string" && block.text.trim()
      && block.text.length <= 12000 && !/[<>\u3400-\u9fff\u3040-\u30ff\uac00-\ud7af\ufffd\ud800-\udfff]|!\[|https?:\/\/|(?:data|javascript):/iu.test(block.text));
  }
  function renderBlocks(container, blocks, doc) {
    const fragment = doc.createDocumentFragment();
    for (const block of blocks) {
      const node = doc.createElement(block.tag); node.textContent = block.text; fragment.append(node);
    }
    container.replaceChildren(fragment); container.hidden = false;
  }
  if (typeof module !== "undefined" && module.exports) module.exports = { session, validFull, renderBlocks };
  if (typeof document === "undefined") return;
  const button = document.getElementById("englishRead"), container = document.getElementById("englishFullCommentary");
  if (!button || !container) return;
  const status = document.getElementById("englishReadStatus"), membership = document.getElementById("englishMembership");
  let epoch = 0, controller = null, pendingLogin = false, resumeRead = false;
  const current = () => { try { return session(localStorage.getItem(SESSION)); } catch (_) { return null; } };
  let identity = current()?.user.id || "";
  function track(action, status = "", error = "") {
    try { window.PortalSuiteAnalytics?.track("journey_interaction", {
      measurement_version: "journey-v1", placement: "english_commentary", action, status, error,
      report_id: button.dataset.commentaryId,
    }); } catch (_) { /* Reading never depends on telemetry. */ }
  }
  function clear() {
    epoch += 1; if (controller) controller.abort(); controller = null;
    container.replaceChildren(); container.hidden = true; button.disabled = false; membership.hidden = true;
    status.textContent = "Only the preview is public. Select Read full commentary to continue.";
  }
  function authChanged() {
    const next = current()?.user.id || "";
    if (next === identity) return;
    const continueLogin = pendingLogin && !identity && next;
    clear(); identity = next; resumeRead = false;
    if (continueLogin) { pendingLogin = false; read("read_resume"); }
    else pendingLogin = false;
  }
  document.addEventListener("portal-auth-change", authChanged);
  document.addEventListener("portal-auth-complete", (event) => {
    if (pendingLogin && event.detail?.placement === "english_commentary" && current()) {
      pendingLogin = false; read("read_resume");
    }
  });
  window.addEventListener("storage", (event) => { if (event.key === SESSION) authChanged(); });
  function suspend() { resumeRead = resumeRead || !container.hidden || Boolean(controller); clear(); }
  function restore() {
    authChanged();
    if (resumeRead && current()) { resumeRead = false; read("read_resume"); }
  }
  window.addEventListener("pagehide", suspend);
  window.addEventListener("pageshow", restore);
  document.addEventListener("visibilitychange", () => { if (document.hidden) suspend(); else restore(); });
  function openLogin() {
    pendingLogin = true;
    document.dispatchEvent(new CustomEvent("portal-open-auth", { detail: {
      mode: "login", placement: "english_commentary", resumeIntent: true,
    } }));
  }
  async function read(action = "read_click") {
    clear(); track(action);
    const signedIn = current();
    if (!signedIn) {
      status.textContent = "Sign in to read full commentary. Your account includes 3 free full reads.";
      track("login_required", "guest"); openLogin(); return;
    }
    identity = signedIn.user.id;
    const expected = epoch;
    controller = new AbortController(); const activeController = controller;
    const timer = setTimeout(() => activeController.abort(), 20000);
    button.disabled = true; status.textContent = "Checking access…";
    track("read_request", "pending");
    try {
      const response = await fetch("/api/english/commentary/read", { method: "POST", cache: "no-store", credentials: "same-origin",
        headers: { "Content-Type": "application/json", "Authorization": `Bearer ${signedIn.token}` },
        body: JSON.stringify({ id: button.dataset.commentaryId }), signal: activeController.signal });
      const value = await response.json();
      if (expected !== epoch || current()?.user.id !== signedIn.user.id) return;
      if (response.status === 402) {
        membership.hidden = false; status.textContent = "Your free allowance is used. Join as a website member to read more commentary.";
        track("read_error", "denied", "quota"); return;
      }
      if (response.status === 401) {
        // A refreshed token supersedes the rejected request; never clear it.
        if (current()?.token !== signedIn.token) { read("read_resume"); return; }
        try { localStorage.removeItem(SESSION); } catch (_) { /* Storage may be unavailable. */ }
        document.dispatchEvent(new CustomEvent("portal-auth-change"));
        status.textContent = "Please sign in again to continue reading.";
        track("read_error", "denied", "auth"); openLogin(); return;
      }
      if (!response.ok || !validFull(value, button.dataset.commentaryId)) throw new Error("unavailable");
      renderBlocks(container, value.blocks, document);
      status.textContent = value.access === "member" ? "Member access."
        : `${value.remaining} free full reads remaining. Re-reading this commentary is free.`;
      track("read_success", "success");
    } catch (_) {
      if (expected === epoch) {
        status.textContent = "Full commentary is temporarily unavailable. Please try again.";
        track("read_error", "error", activeController.signal.aborted ? "timeout" : "unavailable");
      }
    } finally {
      clearTimeout(timer);
      if (expected === epoch) { button.disabled = false; controller = null; }
    }
  }
  button.addEventListener("click", () => read());
}());
