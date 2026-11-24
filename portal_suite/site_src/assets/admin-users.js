function adminUserRow(user, helpers) {
  const { escapeHtml } = helpers;
  const view = adminUserViewModel(user, helpers);
  const email = view.email;
  const canEditAccess = user.role === "user";
  const canToggleStatus = user.role !== "super";
  const disabled = view.disabled;
  const status = `<span class="account-admin-user-status${disabled ? " is-disabled" : ""}">${escapeHtml(view.status)}</span>`;
  const details = [
    ["注册站点", view.registered_site || view.site_origin], ["账号", view.account], ["权限来源", view.access_source],
    ["注册", view.registered], ["最近登录", view.last_login],
  ].filter(([, value]) => value);
  return `
    <tr data-email="${escapeHtml(email)}"${disabled ? ' class="is-disabled-user"' : ""}>
      <td><strong>${escapeHtml(view.username)}</strong><span class="account-admin-mobile-user-status">${status}</span></td>
      <td>${escapeHtml(email)}</td>
      <td>${escapeHtml(view.registered_site || view.site_origin)}</td>
      <td>${status}</td>
      <td>${escapeHtml(view.account)}</td>
      <td title="${escapeHtml(view.access_source)}">${escapeHtml(view.access)}</td>
      <td>${escapeHtml(view.expiry)}</td>
      <td>${escapeHtml(view.access_source)}</td>
      <td>${escapeHtml(view.registered)}</td>
      <td>${escapeHtml(view.last_login)}</td>
      <td>${escapeHtml(adminNewsfeedLabel(user))}</td>
      <td>${canEditAccess || canToggleStatus ? `
        <div class="account-admin-row-actions">
          ${canEditAccess ? `<button class="secondary-button account-admin-edit-user" type="button" data-email="${escapeHtml(email)}" aria-expanded="false">报告权限</button><button class="secondary-button account-admin-newsfeed-user" type="button" data-email="${escapeHtml(email)}" aria-expanded="false">Newsfeed</button><button class="secondary-button account-admin-research-user" type="button" data-email="${escapeHtml(email)}" aria-expanded="false">AI / API</button>` : ""}
          ${canToggleStatus ? `<button class="secondary-button account-admin-toggle-user" type="button" data-email="${escapeHtml(email)}" data-disabled="${disabled ? "false" : "true"}">${disabled ? "启用" : "禁用"}</button>` : ""}
        </div>
      ` : ""}<details class="account-admin-mobile-user-details"><summary>账号详情</summary><dl>${details.map(([label, value]) => `<dt>${escapeHtml(label)}</dt><dd>${escapeHtml(value)}</dd>`).join("")}</dl></details></td>
    </tr>
  `;
}

function adminUserSortTimestamp(value) {
  const timestamp = Date.parse(String(value || ""));
  return Number.isFinite(timestamp) ? timestamp : 0;
}

export function compareAdminUsers(left, right) {
  const disabledDifference = Number(Boolean(left && left.disabled)) - Number(Boolean(right && right.disabled));
  if (disabledDifference) return disabledDifference;
  const leftRecent = adminUserSortTimestamp(left && (left.last_login_at || left.created_at));
  const rightRecent = adminUserSortTimestamp(right && (right.last_login_at || right.created_at));
  if (rightRecent !== leftRecent) return rightRecent - leftRecent;
  const leftLogin = adminUserSortTimestamp(left && left.last_login_at);
  const rightLogin = adminUserSortTimestamp(right && right.last_login_at);
  if (rightLogin !== leftLogin) return rightLogin - leftLogin;
  const leftCreated = adminUserSortTimestamp(left && left.created_at);
  const rightCreated = adminUserSortTimestamp(right && right.created_at);
  if (rightCreated !== leftCreated) return rightCreated - leftCreated;
  return String(left && left.email || "").localeCompare(String(right && right.email || ""));
}

function renderAdminPasswordResetOptions(select, rows, escapeHtml) {
  if (!select) return;
  const current = select.value;
  const resettable = (rows || []).filter((user) => String(user && user.role || "user") === "user");
  select.innerHTML = [
    '<option value="">选择用户</option>',
    ...resettable.map((user) => {
      const email = String(user && user.email || "");
      const username = String(user && user.username || email);
      const suffix = user && user.disabled ? " · 已禁用" : "";
      return `<option value="${escapeHtml(email)}">${escapeHtml(`${username} · ${email}${suffix}`)}</option>`;
    }),
  ].join("");
  if ([...select.options].some((option) => option.value === current)) select.value = current;
  const submit = select.form && select.form.querySelector('button[type="submit"]');
  if (submit) submit.disabled = !select.value;
}


function adminUserTableRow(targets, email) {
  return [...targets.users.querySelectorAll("tr[data-email]")].find((item) => item.dataset.email === email);
}

export function revealAdminInlineEditor(targets, heading) {
  heading?.focus({ preventScroll: true });
  // On phones the editor often opens just below the selected card. Keep the
  // existing position if its heading already fits between toolbar and bottom.
  if (!heading || !targets.content || !window.matchMedia("(max-width: 820px)").matches) return;
  const bounds = heading.getBoundingClientRect();
  const limit = targets.content.getBoundingClientRect().bottom;
  const toolbarBottom = targets.userToolbar.getBoundingClientRect().bottom;
  if (bounds.bottom > limit - 12 || bounds.top < toolbarBottom) {
    targets.content.scrollTop += bounds.top - toolbarBottom - 12;
  }
}

export function mountAdminInlineEditor(targets, editor, email) {
    if (!targets || !editor) return;
    if (editor.dataset.email && editor.dataset.email !== email) closeAdminInlineEditor(targets, editor);
    const row = adminUserTableRow(targets, email);
    if (!row) {
      editor.hidden = true;
      targets.editorHome.append(editor);
      return;
    }
    let detail = row.nextElementSibling;
    if (!detail || !detail.classList.contains("account-admin-editor-row")) {
      detail = document.createElement("tr");
      detail.className = "account-admin-editor-row";
      const cell = document.createElement("td");
      cell.colSpan = 12;
      detail.append(cell);
      row.after(detail);
    }
    editor.dataset.email = email;
    editor.hidden = false;
    detail.firstElementChild.append(editor);
    const selector = editor === targets.newsfeedEditor ? ".account-admin-newsfeed-user" : editor === targets.researchEditor ? ".account-admin-research-user" : ".account-admin-edit-user";
    row.querySelector(selector)?.setAttribute("aria-expanded", "true");
  }

export function closeAdminInlineEditor(targets, editor) {
    if (!targets || !editor) return;
    const row = editor.closest(".account-admin-editor-row");
    const trigger = row?.previousElementSibling?.querySelector(editor === targets.newsfeedEditor ? ".account-admin-newsfeed-user" : editor === targets.researchEditor ? ".account-admin-research-user" : ".account-admin-edit-user");
    editor.hidden = true;
    targets.editorHome.append(editor);
    if (row && !row.querySelector(".account-admin-user-editor")) row.remove();
    trigger?.setAttribute("aria-expanded", "false");
    trigger?.focus({ preventScroll: true });
  }

export async function saveAdminNewsfeed(workerUrl, targets, headers) {
    const response = await fetch(`${workerUrl}/account-admin/user-newsfeed`, {
      method: "POST", cache: "no-store", headers: { "Content-Type": "application/json", ...headers },
      body: JSON.stringify({ email: targets.newsfeedEmail.value, newsfeed_mode: targets.newsfeedMode.value,
        expected_updated_at: targets.newsfeedEditor.dataset.updatedAt || "",
        newsfeed_expires_at: targets.newsfeedMode.value === "enabled" && targets.newsfeedExpiry.value
          ? new Date(`${targets.newsfeedExpiry.value}T23:59:59.999+08:00`).toISOString() : "" }),
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok || !data.verified || !data.user) throw new Error(data.detail || "Newsfeed 权限保存或读回失败，请重新读取后重试。");
    return data.user;
  }

async function requestAdminUsers(workerUrl, query, headers, parentSignal, timeout) {
  if (parentSignal?.aborted) throw parentSignal.reason || new Error("User directory request aborted.");
  const controller = new AbortController();
  const abort = () => controller.abort();
  const timer = setTimeout(abort, timeout);
  parentSignal?.addEventListener("abort", abort, { once: true });
  try {
    const response = await fetch(`${workerUrl}/account-admin/users?${query}`, {
      cache: "no-store", headers, signal: controller.signal,
    });
    const data = await response.json().catch(() => ({}));
    if (!response.ok) {
      throw Object.assign(new Error(data.detail || `用户读取失败 (${response.status})。`), {
        status: response.status, code: data.code,
      });
    }
    if (!data.verified || !Array.isArray(data.users)) throw new Error("用户数据未核验，请刷新重试。");
    return data;
  } finally {
    clearTimeout(timer);
    parentSignal?.removeEventListener("abort", abort);
  }
}

export async function fetchFreshAdminUsers(workerUrl, headers, signal) {
  const users = new Map();
  const ids = new Set();
  const appendUsers = (rows) => {
    for (const user of rows) {
      const email = String(user?.email || "").trim().toLowerCase();
      const id = String(user?.id || "").trim();
      if (!id || !email || ids.has(id) || users.has(email)) {
        throw new Error("用户目录在读取期间发生变化，请刷新重新读取完整列表。");
      }
      users.set(email, user);
      ids.add(id);
    }
  };
  let firstPage;
  try {
    const directory = await requestAdminUsers(workerUrl, "view=directory", headers, signal, 12000);
    if (directory.complete === true && directory.has_more === false && !directory.next_cursor
      && directory.total === directory.users.length) {
      appendUsers(directory.users);
      return { ...directory, users: [...users.values()] };
    }
    // Older Workers ignore view=directory and respond with the first cursor page.
    if (directory.total === undefined && directory.complete === false && directory.has_more === true) firstPage = directory;
  } catch (error) {
    if (signal?.aborted || (error.status && error.status < 500
      && error.status !== 404 && !(error.status === 409 && error.code === "use_user_cursor"))) throw error;
    users.clear();
    ids.clear();
  }
  const cursors = new Set();
  let cursor = "";
  let generatedAt = "";
  for (let page = 0; page < 1000; page += 1) {
    let data = page === 0 ? firstPage : null;
    const query = `page_size=100${cursor ? `&cursor=${encodeURIComponent(cursor)}` : ""}`;
    for (let attempt = 0; !data && attempt < 2; attempt += 1) {
      try {
        data = await requestAdminUsers(workerUrl, query, headers, signal, 45000);
      } catch (error) {
        if (signal?.aborted || attempt || (error.status && error.status < 500)) throw error;
        await new Promise((resolve) => setTimeout(resolve, 500));
      }
    }
    appendUsers(data.users);
    generatedAt = data.generated_at || generatedAt;
    if (data.complete === true && data.has_more === false && !data.next_cursor) {
      return { users: [...users.values()], verified: true, complete: true, generated_at: generatedAt };
    }
    const next = String(data.next_cursor || "");
    if (data.complete !== false || data.has_more !== true || !next || cursors.has(next)) {
      throw new Error("用户分页未完成，请刷新重试。");
    }
    cursors.add(next);
    cursor = next;
  }
  throw new Error("用户列表超过本次读取范围，请联系管理员。");
}

export function adminNewsfeedLabel(user) {
    const access = user && user.newsfeed;
    if (user && user.disabled) return "账号已禁用";
    if (!access) return "待核验";
    if (!access.enabled) return access.mode === "disabled" ? "已关闭" : access.mode === "enabled" ? "已到期" : "未开通";
    const expiry = access.source === "admin" ? access.expires_at : (user.effective_access || user.access || {}).current_period_end;
    return `${access.source === "admin" ? "单独开通" : "会员可用"}${expiry ? ` · 至 ${new Date(expiry).toLocaleDateString("sv-SE", { timeZone: "Asia/Shanghai" })}` : ""}`;
  }

export function fillAdminNewsfeedEditor(user, targets, reveal = true) {
    const access = user.newsfeed || {};
    targets.newsfeedEditor.hidden = false;
    targets.newsfeedEditor.dataset.updatedAt = access.updated_at || "";
    targets.newsfeedEmail.value = user.email;
    targets.newsfeedTitle.textContent = `Newsfeed：${user.username || user.email}`;
    targets.newsfeedState.textContent = `当前状态：${adminNewsfeedLabel(user)}。`;
    targets.newsfeedMode.value = access.mode || "auto";
    const expiry = access.expires_at || (user.effective_access || user.access || {}).current_period_end;
    targets.newsfeedExpiry.value = expiry ? new Date(expiry).toLocaleDateString("sv-SE", { timeZone: "Asia/Shanghai" }) : "";
    targets.newsfeedMode.disabled = Boolean(targets.newsfeedEditor.dataset.saving);
    targets.newsfeedExpiry.disabled = targets.newsfeedMode.disabled || targets.newsfeedMode.value !== "enabled";
    targets.newsfeedStatus.textContent = "";
    mountAdminInlineEditor(targets, targets.newsfeedEditor, user.email);
    if (reveal && !targets.newsfeedEditor.hidden) revealAdminInlineEditor(targets, targets.newsfeedTitle);
  }

const ADMIN_USERS_PER_PAGE = 25;

function userSearchText(value) {
  return String(value || "").normalize("NFKC").trim().toLowerCase();
}

export function adminUserPage(allRows, search, currentPage, anchorEmail = "") {
  const query = userSearchText(search);
  const matches = query ? allRows.filter((user) => userSearchText(`${user.username || ""} ${user.email || ""}`).includes(query)) : allRows;
  const totalPages = Math.max(1, Math.ceil(matches.length / ADMIN_USERS_PER_PAGE));
  const anchor = anchorEmail ? matches.findIndex((user) => user.email === anchorEmail) : -1;
  const page = anchor < 0 ? Math.max(0, Math.min(currentPage || 0, totalPages - 1)) : Math.floor(anchor / ADMIN_USERS_PER_PAGE);
  const start = page * ADMIN_USERS_PER_PAGE;
  return { rows: matches.slice(start, start + ADMIN_USERS_PER_PAGE), matches: matches.length, totalPages, page, start, query };
}

export function renderAdminUserTable(targets, accountAdminUsersByEmail, helpers) {
  if (!targets?.users || !targets.usersComplete) return;
  const allRows = targets.sortedUsers ||= [...accountAdminUsersByEmail.values()].sort(compareAdminUsers);
  const editors = [targets.userEditor, targets.newsfeedEditor, targets.researchEditor].filter(Boolean);
  const openEditor = editors.find((editor) => !editor.hidden);
  const { rows, matches, totalPages, page, start, query } = adminUserPage(
    allRows, targets.userSearch?.value, targets.userPage, openEditor?.dataset.email,
  );
  targets.userPage = page;
  targets.userCount.textContent = query ? `匹配 ${matches} / ${allRows.length} 位用户` : `全部 ${allRows.length} 位用户`;
  targets.userPagination.hidden = totalPages <= 1;
  targets.userPageLabel.textContent = totalPages <= 1 ? "" : `${start + 1}–${start + rows.length} / ${matches}`;
  targets.userPrevious.disabled = page === 0;
  targets.userNext.disabled = page + 1 >= totalPages;
  const scrollTop = targets.content.scrollTop;
  const focused = targets.users.contains(document.activeElement) ? document.activeElement : null;
  const focusedRow = focused?.closest("tr[data-email]")?.dataset.email;
  const focusedClass = focused?.classList && [...focused.classList].find((name) => name.startsWith("account-admin-") && name.endsWith("-user"));
  editors.forEach((editor) => { if (!editor.hidden) targets.editorHome.append(editor); });
  targets.users.innerHTML = rows.length
    ? rows.map((user) => adminUserRow(user, helpers)).join("")
    : `<tr><td colspan="12">${query ? "未找到匹配用户，请检查用户名或邮箱。" : "暂无用户。"}</td></tr>`;
  editors.forEach((editor) => {
    if (!editor.hidden) {
      if (rows.some((user) => user.email === editor.dataset.email)) mountAdminInlineEditor(targets, editor, editor.dataset.email);
      else editor.hidden = true;
    }
  });
  if (focused?.isConnected) focused.focus({ preventScroll: true });
  else if (focusedRow && focusedClass) {
    adminUserTableRow(targets, focusedRow)?.querySelector(`.${focusedClass}`)?.focus({ preventScroll: true });
  }
  targets.content.scrollTop = scrollTop;
  if (targets.passwordTools.open && targets.passwordOptionsSource !== allRows) {
    renderAdminPasswordResetOptions(targets.passwordResetEmail, allRows, helpers.escapeHtml);
    targets.passwordOptionsSource = allRows;
  }
}

export function bindAdminUserDirectory(targets, { refresh, exportUsers, render }) {
  const { userEditor, newsfeedEditor, researchEditor, userSearch, usersStatus, content } = targets;
  function changePage(page, scrollToTop) {
    targets.editorRequest = (targets.editorRequest || 0) + 1;
    for (const editor of [userEditor, newsfeedEditor, researchEditor]) {
      if (editor && !editor.hidden) closeAdminInlineEditor(targets, editor);
    }
    targets.userPage = page;
    usersStatus.textContent = "";
    render();
    if (scrollToTop) {
      content.scrollTop = 0;
      // Keep keyboard users in the results without opening a phone keyboard.
      targets.userToolbar.focus({ preventScroll: true });
    }
  }
  targets.refreshUsers.addEventListener("click", refresh);
  targets.exportUsers.addEventListener("click", exportUsers);
  targets.userPrevious.addEventListener("click", () => changePage(targets.userPage - 1, true));
  targets.userNext.addEventListener("click", () => changePage(targets.userPage + 1, true));
  userSearch.addEventListener("input", (event) => { if (!event.isComposing) changePage(0, false); });
  userSearch.addEventListener("compositionend", () => changePage(0, false));
  targets.passwordTools.addEventListener("toggle", () => { if (targets.passwordTools.open) render(); });
}

export function bindNewsfeedEditor(workerUrl, targets, dependencies) {
    const { newsfeedEditor, newsfeedEmail, newsfeedMode, newsfeedExpiry, newsfeedStatus } = targets;
    const { renderAdminUserTable, saveAdminNewsfeed } = dependencies;
    document.getElementById("accountAdminNewsfeedClose")?.addEventListener("click", () => closeAdminInlineEditor(targets, newsfeedEditor));
    newsfeedMode?.addEventListener("change", () => { newsfeedExpiry.disabled = Boolean(newsfeedEditor.dataset.saving) || newsfeedMode.value !== "enabled"; });
    newsfeedEditor?.addEventListener("submit", async (event) => {
      event.preventDefault();
      if (newsfeedEditor.dataset.saving) return;
      const selectedEmail = newsfeedEmail.value;
      const submit = newsfeedEditor.querySelector('button[type="submit"]');
      newsfeedEditor.dataset.saving = "true";
      submit.disabled = true;
      newsfeedMode.disabled = true;
      newsfeedExpiry.disabled = true;
      newsfeedStatus.className = "status-line";
      newsfeedStatus.textContent = "正在保存并核验 Newsfeed 权限…";
      try {
        const user = await saveAdminNewsfeed(workerUrl, targets);
        renderAdminUserTable(targets);
        if (!newsfeedEditor.hidden && newsfeedEmail.value === selectedEmail) {
          fillAdminNewsfeedEditor(user, targets, false);
          newsfeedStatus.className = "status-line ok";
          newsfeedStatus.textContent = "Newsfeed 权限已保存并读回确认。";
        }
      } catch (error) {
        if (newsfeedEmail.value === selectedEmail) {
          newsfeedStatus.className = "status-line error";
          newsfeedStatus.textContent = error.message;
        }
      } finally {
        delete newsfeedEditor.dataset.saving;
        submit.disabled = false;
        newsfeedMode.disabled = false;
        newsfeedExpiry.disabled = newsfeedMode.value !== "enabled";
      }
    });
}

  function adminUserEntitlementLabel(user) {
    if (user && user.role === "super") return "super";
    const entitlement = user && user.entitlement || {};
    if (entitlement.active) return entitlement.plan || "active";
    return "free";
  }

  function adminUserAccessLabel(user, accountRightUsageText) {
    const access = user && (user.effective_access || user.access) || {};
    if (access.source === "disabled") return "账号已禁用（不可下载）";
    if (access.source === "error") return "权限读取失败（已拒绝）";
    if (!access.active) return "未开通";
    const suffix = accountRightUsageText(access);
    if (access.access_mode === "all") return suffix ? `全站报告 · ${suffix}` : "全站报告";
    if (access.access_mode === "filters") {
      const parts = [];
      if (Array.isArray(access.institutions) && access.institutions.length) parts.push(`机构 ${access.institutions.length}`);
      if (Array.isArray(access.industries) && access.industries.length) parts.push(`行业 ${access.industries.length}`);
      if (Array.isArray(access.page_ranges) && access.page_ranges.length) parts.push(`页数 ${access.page_ranges.length}`);
      const label = parts.length ? parts.join(" / ") : "条件报告";
      return suffix ? `${label} · ${suffix}` : label;
    }
    const label = access.access_mode || "active";
    return suffix ? `${label} · ${suffix}` : label;
  }

  function adminUserAccessExpiry(user) {
    const access = user && (user.effective_access || user.access) || {};
    if (access.source === "disabled") return "-";
    if (access.source === "error") return "核验失败";
    if (!access.active) return "-";
    if (access.lifetime) return "长期";
    return access.current_period_end ? String(access.current_period_end).slice(0, 10) : "-";
  }

  function adminUserAccessSource(user) {
    const access = user && (user.effective_access || user.access) || {};
    const entitlement = user && user.entitlement || {};
    if (access.source === "role") return "账号角色";
    if (access.source === "disabled") return "账号已禁用";
    if (["vid2ppt_nova", "vid2ppt_atlas"].includes(access.source)) return "历史会员权益";
    if (access.source === "entitlement+stored") return "会员权益 + 后台授权";
    if (access.source === "entitlement") {
      return ["vid2ppt_nova", "vid2ppt_atlas"].includes(entitlement.grant_source)
        ? "历史会员权益"
        : "会员权益";
    }
    if (access.source === "stored") return "后台授权";
    if (access.source === "error") return "核验失败（已拒绝）";
    return "未授权";
  }

export function adminUserViewModel(user, { PUBLIC_BRAND, publicBrandText, accountRightUsageText }) {
    const disabled = Boolean(user && user.disabled);
    const rawSiteOrigin = String(user && (user.site_origin || user.registered_site) || "portal");
    const rawRegisteredSite = String(user && (user.registered_site || user.site_origin) || "portal");
    const rawSourceSite = String(user && user.entitlement && user.entitlement.source_site || "");
    const rawGrantSource = String(user && user.entitlement && user.entitlement.grant_source || "");
    const historicalLinkedEntitlement = rawSourceSite === "vid2ppt" || ["vid2ppt_nova", "vid2ppt_atlas"].includes(rawGrantSource);
    const publicOriginLabel = (value) => {
      const text = String(value || "").trim();
      if (!text || text === "portal") return PUBLIC_BRAND;
      if (text === "vid2ppt") return "历史会员";
      return publicBrandText(text, PUBLIC_BRAND);
    };
    return {
      username: String(user && user.username || ""),
      email: String(user && user.email || ""),
      site_origin: publicOriginLabel(rawSiteOrigin),
      registered_site: publicOriginLabel(rawRegisteredSite),
      entitlement_source_site: historicalLinkedEntitlement ? "历史会员" : publicOriginLabel(rawSourceSite),
      entitlement_grant_source: historicalLinkedEntitlement ? "历史会员" : publicBrandText(rawGrantSource),
      entitlement_plan_code: historicalLinkedEntitlement ? "" : publicBrandText(user && user.entitlement && user.entitlement.source_plan_code),
      status: disabled ? "已禁用" : "正常",
      account: adminUserEntitlementLabel(user),
      access: adminUserAccessLabel(user, accountRightUsageText),
      expiry: adminUserAccessExpiry(user),
      registered: String(user && user.created_at || "").slice(0, 10),
      last_login: String(user && user.last_login_at || "").replace("T", " ").slice(0, 16),
      access_source: adminUserAccessSource(user),
      access_updated: String(user && (user.effective_access || user.access) && (user.effective_access || user.access).updated_at || "").replace("T", " ").slice(0, 19),
      disabled,
    };
  }
