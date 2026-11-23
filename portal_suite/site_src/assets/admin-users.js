export function mountAdminInlineEditor(targets, editor, email) {
    if (!targets || !editor) return;
    if (editor.dataset.email && editor.dataset.email !== email) closeAdminInlineEditor(targets, editor);
    const row = Array.from(targets.users.querySelectorAll("tr[data-email]")).find((item) => item.dataset.email === email);
    if (!row) return;
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

export async function fetchFreshAdminUsers(workerUrl, headers) {
    const users = new Map(), cursors = new Set();
    let cursor = "", generatedAt = "";
    for (let page = 0; page < 1000; page += 1) {
      let data;
      for (let attempt = 0; attempt < 2; attempt += 1) {
        const controller = new AbortController();
        const timer = setTimeout(() => controller.abort(), 45000);
        try {
          const response = await fetch(`${workerUrl}/account-admin/users?page_size=100${cursor ? `&cursor=${encodeURIComponent(cursor)}` : ""}`, {
            cache: "no-store", headers, signal: controller.signal,
          });
          data = await response.json().catch(() => ({}));
          if (!response.ok) throw Object.assign(new Error(data.detail || `用户读取失败 (${response.status})。`), { status: response.status });
          if (!data.verified || !Array.isArray(data.users)) throw new Error("用户数据未完整核验，请刷新重试。");
          break;
        } catch (error) {
          if (attempt || (error.status && error.status < 500)) throw error;
          await new Promise((resolve) => setTimeout(resolve, 500));
        } finally { clearTimeout(timer); }
      }
      for (const user of data.users) {
        const email = String(user.email || "").toLowerCase();
        if (!email || users.has(email)) throw new Error("用户目录在读取期间发生变化，请刷新重新读取完整列表。");
        users.set(email, user);
      }
      generatedAt = data.generated_at || generatedAt;
      if (data.complete === true && data.has_more === false) return { users: [...users.values()], verified: true, complete: true, generated_at: generatedAt };
      const next = String(data.next_cursor || "");
      if (!data.has_more || !next || cursors.has(next)) throw new Error("用户分页未完成，请刷新重试。");
      cursors.add(next); cursor = next;
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

export function fillAdminNewsfeedEditor(user, targets) {
    const access = user.newsfeed || {};
    targets.newsfeedEditor.hidden = false;
    targets.newsfeedEditor.dataset.updatedAt = access.updated_at || "";
    targets.newsfeedEmail.value = user.email;
    targets.newsfeedTitle.textContent = `Newsfeed：${user.username || user.email}`;
    targets.newsfeedState.textContent = `当前状态：${adminNewsfeedLabel(user)}。`;
    targets.newsfeedMode.value = access.mode || "auto";
    const expiry = access.expires_at || (user.effective_access || user.access || {}).current_period_end;
    targets.newsfeedExpiry.value = expiry ? new Date(expiry).toLocaleDateString("sv-SE", { timeZone: "Asia/Shanghai" }) : "";
    targets.newsfeedExpiry.disabled = targets.newsfeedMode.value !== "enabled";
    targets.newsfeedStatus.textContent = "";
    mountAdminInlineEditor(targets, targets.newsfeedEditor, user.email);
    targets.newsfeedTitle.focus({ preventScroll: true });
  }

export function renderAdminUserTable(targets, accountAdminUsersByEmail, helpers) {
    const { compareAdminUsers, adminUserRow, renderAdminPasswordResetOptions, renderAdminUsersVerificationState } = helpers;
    if (!targets || !targets.users) return;
    if (targets.usersComplete === false) {
      renderAdminUsersVerificationState(targets, "正在读取全部用户及最新权限，完成后显示总人数…");
      return;
    }
    const allRows = [...accountAdminUsersByEmail.values()].sort(compareAdminUsers);
    const query = String(targets.userSearch && targets.userSearch.value || "").normalize("NFKC").trim().toLowerCase();
    const rows = allRows.filter((user) => !query || `${user.username || ""} ${user.email || ""}`.normalize("NFKC").toLowerCase().includes(query));
    if (targets.userCount) targets.userCount.textContent = query ? `${rows.length} / ${allRows.length} 个用户` : `${allRows.length} 个用户 · 已完整读取`;
    const dialog = targets.users.closest(".account-admin-dialog");
    const scrollTop = dialog && dialog.scrollTop;
    const editors = [targets.userEditor, targets.newsfeedEditor, targets.researchEditor].filter(Boolean);
    editors.forEach((editor) => { if (targets.editorHome) targets.editorHome.append(editor); });
    targets.users.innerHTML = rows.length
      ? rows.map(adminUserRow).join("")
      : `<tr><td colspan="12">${query ? "未找到匹配用户，请检查用户名或邮箱。" : "暂无用户。"}</td></tr>`;
    editors.forEach((editor) => { if (!editor.hidden) mountAdminInlineEditor(targets, editor, editor.dataset.email); });
    if (dialog) dialog.scrollTop = scrollTop;
    renderAdminPasswordResetOptions(allRows);
  }

export function bindNewsfeedEditor(workerUrl, targets, dependencies) {
    const { userSearch, newsfeedEditor, newsfeedEmail, newsfeedMode, newsfeedExpiry, newsfeedStatus } = targets;
    const { renderAdminUserTable, saveAdminNewsfeed } = dependencies;
    if (userSearch) userSearch.addEventListener("input", () => renderAdminUserTable(targets));
    document.getElementById("accountAdminNewsfeedClose")?.addEventListener("click", () => closeAdminInlineEditor(targets, newsfeedEditor));
    newsfeedMode?.addEventListener("change", () => { newsfeedExpiry.disabled = newsfeedMode.value !== "enabled"; });
    newsfeedEditor?.addEventListener("submit", async (event) => {
      event.preventDefault();
      const selectedEmail = newsfeedEmail.value;
      const submit = newsfeedEditor.querySelector('button[type="submit"]');
      submit.disabled = true;
      newsfeedStatus.className = "status-line";
      newsfeedStatus.textContent = "正在保存并核验 Newsfeed 权限…";
      try {
        const user = await saveAdminNewsfeed(workerUrl, targets);
        renderAdminUserTable(targets);
        if (!newsfeedEditor.hidden && newsfeedEmail.value === selectedEmail) {
          fillAdminNewsfeedEditor(user, targets);
          newsfeedStatus.className = "status-line ok";
          newsfeedStatus.textContent = "Newsfeed 权限已保存并读回确认。";
        }
      } catch (error) {
        if (newsfeedEmail.value === selectedEmail) {
          newsfeedStatus.className = "status-line error";
          newsfeedStatus.textContent = error.message;
        }
      } finally { submit.disabled = false; }
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
