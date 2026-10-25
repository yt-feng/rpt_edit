(function (root) {
  "use strict";
  const mounted = new WeakMap();
  function element(tag, className, text) {
    const node = document.createElement(tag);
    if (className) node.className = className;
    if (text) node.textContent = text;
    return node;
  }

  function mount(container, options) {
    if (!container || !options.workerUrl || !options.item?.id) return;
    if (mounted.has(container)) mounted.get(container)();
    const section = element("section", "report-discussion");
    const heading = element("div", "report-discussion-heading");
    const title = element("h3", "", "报告讨论");
    const count = element("span", "report-discussion-count");
    heading.append(title, count);
    const starter = element("div", "report-discussion-starter");
    const list = element("div", "report-discussion-list");
    const login = element("button", "secondary-button", "登录后参与讨论");
    login.type = "button";
    const form = element("form", "report-discussion-form");
    const label = element("label", "", "你的看法");
    const body = element("textarea", "");
    body.rows = 4; body.maxLength = 1200; body.required = true;
    body.placeholder = "你赞同哪些判断？有哪些不同证据或值得跟踪的变化？";
    label.append(body);
    const actions = element("div", "report-discussion-actions");
    const limit = element("span", "", "最多 1200 字");
    const submit = element("button", "primary", "发布评论");
    submit.type = "submit";
    actions.append(limit, submit); form.append(label, actions);
    const status = element("div", "status-line");
    status.setAttribute("aria-live", "polite");
    section.append(heading, starter, list, login, form, status);
    container.append(section);
    const identity = { source: options.source || options.item.source || "catalog", report_id: options.item.id };
    const endpoint = options.workerUrl.replace(/\/+$/, "") + "/report-discussion";
    let alive = true, pendingId = "", pendingBody = "", loadSequence = 0;

    function auth() {
      const signedIn = Boolean(options.getSession?.());
      login.hidden = signedIn; form.hidden = !signedIn;
    }
    function setStatus(text, error) {
      if (!alive) return;
      status.textContent = text || "";
      status.className = error ? "status-line error" : "status-line";
    }
    function row(comment) {
      const article = element("article", "report-discussion-comment");
      const meta = element("div", "report-discussion-meta");
      meta.append(element("strong", "", comment.display_name || "用户"));
      const date = new Date(comment.created_at);
      if (Number.isFinite(date.getTime())) meta.append(element("time", "", date.toLocaleString("zh-CN", { timeZone: "Asia/Shanghai", dateStyle: "medium", timeStyle: "short" })));
      if (comment.can_delete) {
        const remove = element("button", "report-discussion-delete", "删除");
        remove.type = "button";
        remove.addEventListener("click", async () => {
          remove.disabled = true;
          try {
            const response = await fetch(endpoint, { method: "DELETE", headers: { "Content-Type": "application/json", ...options.authHeaders?.() }, body: JSON.stringify({ ...identity, comment_id: comment.id }) });
            const data = await response.json();
            if (!response.ok) throw new Error(data.detail || "删除失败。");
            await load();
          } catch (error) { setStatus(error.message, true); remove.disabled = false; }
        });
        meta.append(remove);
      }
      article.append(meta, element("p", "report-discussion-body", comment.body));
      return article;
    }
    async function load() {
      const sequence = ++loadSequence;
      try {
        const response = await fetch(endpoint + "?" + new URLSearchParams(identity), { cache: "no-store", headers: { ...options.authHeaders?.() } });
        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || "讨论读取失败。");
        if (!alive || sequence !== loadSequence) return;
        starter.replaceChildren();
        if (data.starter?.kind === "ai") {
          const ai = element("article", "report-discussion-ai");
          const aiHeader = element("div", "report-discussion-meta");
          aiHeader.append(element("strong", "report-discussion-ai-badge", "AI 导读"), element("span", "", data.starter.text_scope === "partial_excerpt" ? "基于已提取的报告节选" : "基于报告内容"));
          ai.append(aiHeader, element("p", "report-discussion-body", data.starter.body));
          starter.append(ai);
        }
        const comments = Array.isArray(data.comments) ? data.comments : [];
        count.textContent = comments.length ? comments.length + " 条评论" : "";
        list.replaceChildren(...comments.map(row));
        if (!comments.length) list.append(element("p", "report-discussion-empty", "还没有读者评论，欢迎留下你的判断。"));
        setStatus(""); auth();
      } catch (error) { if (sequence === loadSequence) setStatus(error.message, true); }
    }
    login.addEventListener("click", () => options.onLogin?.());
    form.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (!options.getSession?.()) { options.onLogin?.(); return; }
      const text = body.value.trim();
      if (!text) return;
      if (!pendingId || pendingBody !== text) { pendingId = crypto.randomUUID(); pendingBody = text; }
      submit.disabled = true; setStatus("正在发布评论…");
      try {
        const response = await fetch(endpoint, { method: "POST", headers: { "Content-Type": "application/json", ...options.authHeaders?.() }, body: JSON.stringify({ ...identity, body: text, request_id: pendingId }) });
        const data = await response.json();
        if (!response.ok) throw new Error(data.detail || "评论发布失败。");
        body.value = ""; pendingId = ""; pendingBody = "";
        await load();
      } catch (error) { setStatus(error.message, true); }
      finally { submit.disabled = false; }
    });
    const authChange = () => { auth(); load(); };
    document.addEventListener("portal-auth-change", authChange);
    const cleanup = () => {
      if (!alive) return;
      alive = false; document.removeEventListener("portal-auth-change", authChange); section.remove(); mounted.delete(container);
    };
    mounted.set(container, cleanup);
    auth(); load();
    return cleanup;
  }
  root.PortalDiscussion = { mount };
}(window));
