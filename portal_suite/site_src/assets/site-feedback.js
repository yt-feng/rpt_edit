(() => {
  "use strict";
  if (window.PortalFeedback) return;

  function track(action, status = "", extra = {}) {
    try { window.PortalSuiteAnalytics?.track("journey_interaction", { measurement_version: "journey-v1", placement: "feedback", action, status, ...extra }); } catch (_) { /* Telemetry is best effort. */ }
  }

  function session() {
    try {
      const saved = JSON.parse(window.localStorage.getItem("portal_auth_session") || "null");
      return saved && saved.user && saved.user.id && typeof saved.token === "string" && saved.token.trim() ? saved : null;
    } catch (_error) { return null; }
  }

  function accountReplyEmail(current) {
    const user = current && current.user;
    const value = String(user && user.email || "").trim();
    return user && !user.email_is_generated && /^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(value)
      && !/@users(?:\.portal)?\.example\.invalid$/i.test(value) ? value : "";
  }

  function mount() {
    if (!document.body || document.getElementById("siteFeedbackDialog")) return;
    const container = document.createElement("div");
    container.className = "site-feedback";
    container.innerHTML = `
      <button class="site-feedback-launch" type="button" aria-haspopup="dialog" aria-controls="siteFeedbackDialog">意见反馈 / Feedback</button>
      <dialog class="site-feedback-dialog" id="siteFeedbackDialog" aria-labelledby="siteFeedbackTitle" aria-describedby="siteFeedbackIntro">
        <div class="site-feedback-heading"><h2 id="siteFeedbackTitle">意见反馈 / Feedback</h2><button class="site-feedback-close" type="button" aria-label="关闭 / Close">×</button></div>
        <p id="siteFeedbackIntro">遇到问题，或有改进建议？告诉我们。<br>Found a problem or have an idea? Let us know.</p>
        <form class="site-feedback-form">
          <label for="siteFeedbackEmail">回复邮箱 / Email</label>
          <input id="siteFeedbackEmail" name="requester_email" type="email" maxlength="254" autocomplete="email" required>
          <label for="siteFeedbackCategory">反馈类型 / Category</label>
          <select id="siteFeedbackCategory" name="category" required>
            <option value="bug">功能问题 / Bug</option><option value="content">内容问题 / Content</option>
            <option value="suggestion">改进建议 / Suggestion</option><option value="other">其他 / Other</option>
          </select>
          <label for="siteFeedbackMessage">反馈内容 / Message</label>
          <textarea id="siteFeedbackMessage" name="message" rows="5" minlength="5" maxlength="2000" required placeholder="请描述问题或建议（5–2000 字） / Tell us what happened (5–2000 characters)"></textarea>
          <div class="site-feedback-trap" aria-hidden="true"><label for="siteFeedbackWebsite">Website</label><input id="siteFeedbackWebsite" name="honeypot" type="text" tabindex="-1" autocomplete="off"></div>
          <p class="site-feedback-status" role="status" aria-live="polite"></p>
          <button class="site-feedback-submit" type="submit">提交反馈 / Send feedback</button>
        </form>
      </dialog>`;
    document.body.append(container);
    const byId = (id) => container.querySelector(`#${id}`);
    const launcher = container.querySelector(".site-feedback-launch");
    const dialog = byId("siteFeedbackDialog");
    const form = container.querySelector("form");
    const email = byId("siteFeedbackEmail");
    const category = byId("siteFeedbackCategory");
    const message = byId("siteFeedbackMessage");
    const honeypot = byId("siteFeedbackWebsite");
    const submit = container.querySelector(".site-feedback-submit");
    const status = container.querySelector(".site-feedback-status");
    let busy = false, controller = null, identity = "", revision = 0, started = false;
    let returnFocus = launcher;
    const setStatus = (text, error = false) => {
      status.textContent = text;
      status.dataset.state = error ? "error" : "ok";
    };
    function updateIdentity() {
      const current = session();
      const nextIdentity = current ? String(current.user.id) : "";
      if (nextIdentity !== identity) {
        revision += 1;
        if (controller) controller.abort();
        form.reset(); started = false;
        setStatus("");
      }
      identity = nextIdentity;
      const accountEmail = accountReplyEmail(current);
      const wasReadOnly = email.readOnly;
      email.readOnly = Boolean(accountEmail);
      if (accountEmail) email.value = accountEmail;
      else if (wasReadOnly) email.value = "";
    }
    function close() {
      if (typeof dialog.close === "function") dialog.close();
      else dialog.removeAttribute("open");
      returnFocus?.focus();
    }
    launcher.addEventListener("click", () => {
      track("open");
      returnFocus = document.activeElement || launcher;
      updateIdentity();
      if (typeof dialog.showModal === "function") dialog.showModal();
      else dialog.setAttribute("open", "");
      (email.readOnly ? message : email).focus();
    });
    container.querySelector(".site-feedback-close").addEventListener("click", close);
    dialog.addEventListener("close", () => returnFocus?.focus());
    dialog.addEventListener("click", (event) => {
      if (event.target !== dialog) return;
      const bounds = dialog.getBoundingClientRect();
      if (event.clientX < bounds.left || event.clientX > bounds.right || event.clientY < bounds.top || event.clientY > bounds.bottom) close();
    });
    dialog.addEventListener("keydown", (event) => {
      if (event.key === "Escape") { event.preventDefault(); close(); }
      // Native dialogs trap focus; retain this for browsers using the fallback.
      if (event.key === "Tab") {
        const controls = [...dialog.querySelectorAll("button, input, select, textarea")].filter((control) => !control.disabled && control.tabIndex !== -1);
        const first = controls[0], last = controls[controls.length - 1];
        if (event.shiftKey && document.activeElement === first) { event.preventDefault(); last?.focus(); }
        else if (!event.shiftKey && document.activeElement === last) { event.preventDefault(); first?.focus(); }
      }
    });
    document.addEventListener("portal-auth-change", updateIdentity);
    window.addEventListener("storage", (event) => { if (event.key === "portal_auth_session") updateIdentity(); });
    form.addEventListener("input", () => { if (!started) { started = true; track("form_start"); } });
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (busy || !form.reportValidity()) return;
      const current = session();
      const owner = current ? String(current.user.id) : "";
      if (owner !== identity) { updateIdentity(); setStatus("账号已变化，请检查内容后重新提交。 / Your account changed. Please review and submit again.", true); return; }
      const ticket = revision;
      busy = true; track("submit", "pending");
      [submit, email, category, message].forEach((control) => { control.disabled = true; });
      form.setAttribute("aria-busy", "true");
      submit.textContent = "提交中… / Sending…";
      setStatus("");
      controller = new AbortController();
      const activeController = controller;
      const timer = window.setTimeout(() => activeController.abort(), 40000);
      try {
        const response = await window.fetch("/api/feedback", {
          method: "POST", cache: "no-store", credentials: "same-origin", signal: activeController.signal,
          headers: { "Content-Type": "application/json", ...(current ? { Authorization: `Bearer ${current.token}` } : {}) },
          body: JSON.stringify({ category: category.value, message: message.value.trim(),
            requester_email: accountReplyEmail(current) || email.value.trim(),
            page_path: window.location.pathname, honeypot: honeypot.value }),
        });
        const result = await response.json().catch(() => ({}));
        if (ticket !== revision) return;
        if (!response.ok || !result.ok) throw new Error(result.detail || "提交暂未成功，请稍后重试。 / Please try again later.");
        track("result", result.deduplicated ? "deduplicated" : "success", { deduplicated: result.deduplicated === true, acknowledgement_status: result.confirmation_email_sent === true ? "provider_accepted" : "unknown" });
        started = false;
        setStatus("反馈已收到，感谢您的帮助。 / Thank you. Your feedback has been received.");
        message.value = "";
      } catch (error) {
        if (ticket === revision) track("result", "error", { error: error.name === "AbortError" ? "timeout" : "unavailable" });
        if (ticket === revision) setStatus(error.name === "AbortError"
          ? "提交结果暂未确认，可稍后重试。 / Delivery is not yet confirmed. You may retry later."
          : error.message || "提交暂未成功，请稍后重试。 / Please try again later.", true);
      } finally {
        window.clearTimeout(timer);
        if (controller === activeController) controller = null;
        busy = false;
        [submit, email, category, message].forEach((control) => { control.disabled = false; });
        submit.textContent = "提交反馈 / Send feedback";
        form.removeAttribute("aria-busy");
      }
    });
  }

  window.PortalFeedback = { mount };
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", mount, { once: true });
  else mount();
})();
