/** Membership-only renewal notices; no payments, API add-ons or research usage.
 * At most one provider attempt per cycle/stage. A durable pending marker is
 * committed before sending; unknown outcomes are deliberately never retried.
 * The daily scan is bounded and resumable, and exposes incomplete progress.
 */
const DAY = 86400000;
const GAP = 2 * DAY;
const PREFIX = "_account/expiry-reminders-v1/";
const SCAN_KEY = `${PREFIX}scan`;
const ACTIVE = new Set(["active", "trialing"]);
const iso = (ms) => new Date(ms).toISOString();
const ms = (value) => Date.parse(String(value || ""));
const day = (value) => Math.floor((value + 8 * 3600000) / DAY);
const atTen = (date) => date * DAY + 2 * 3600000;
const inWindow = (now) => now >= atTen(day(now)) && now < atTen(day(now)) + 2 * 3600000;
const key = (id) => `${PREFIX}accounts/${encodeURIComponent(String(id))}`;
const safeError = () => Object.assign(new Error("Reminder storage unavailable"), { code: "REMINDER_STORAGE" });
const escapeHtml = (value) => String(value).replace(/[&<>"']/gu, (c) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" }[c]));

export function resolveExpiryMembership(snapshot, now = Date.now()) {
  const user = snapshot.user || {};
  if (snapshot.disabled) return { eligible: false, reason: "disabled" };
  if (snapshot.privileged) return { eligible: false, reason: "privileged" };
  if (snapshot.generated || !user.email) return { eligible: false, reason: "no_email" };
  const admin = snapshot.admin;
  const validGrant = (row) => row && ACTIVE.has(row.status) && ["all", "filters"].includes(row.access_mode)
    && (row.lifetime || Number.isFinite(ms(row.current_period_end)));
  const adminActive = validGrant(admin) && (admin.lifetime || ms(admin.current_period_end) > now);
  const candidates = [];
  if (validGrant(admin)) candidates.push({ ...admin, kind: admin.duration_value === "trial_3d" ? "trial" : "membership" });
  const entitlement = snapshot.entitlement;
  const incoming = [];
  if (entitlement && entitlement.plan === "annual" && ACTIVE.has(entitlement.status)) {
    incoming.push({ ...entitlement, kind: entitlement.status === "trialing" ? "trial" : "membership", access_mode: "all" });
  }
  if (validGrant(snapshot.trial)) incoming.push({ ...snapshot.trial, kind: "trial" });
  for (const row of incoming) {
    // Match the owning access decision: an inactive/expired stored admin row
    // suppresses older authority rows, even when their dates look longer.
    if (admin && !adminActive && !(ms(row.authority_occurred_at) > ms(admin.updated_at))) continue;
    if (row.lifetime || Number.isFinite(ms(row.current_period_end))) candidates.push(row);
  }
  if (candidates.some((row) => row.lifetime)) return { eligible: false, reason: "lifetime" };
  const latest = candidates.sort((a, b) => ms(b.current_period_end) - ms(a.current_period_end))[0];
  if (!latest) return { eligible: false, reason: "no_membership" };
  const end = ms(latest.current_period_end);
  const duration = end - ms(latest.started_at || latest.created_at || latest.updated_at);
  // Unknown trial duration gets the quieter one-notice policy.
  const shortTrial = latest.kind === "trial" && (!Number.isFinite(duration) || duration <= 7 * DAY || latest.duration_value === "trial_3d");
  return { eligible: true, reason: "eligible", expires_at: iso(end),
    expires_bjt: new Intl.DateTimeFormat("sv-SE", { timeZone: "Asia/Shanghai", year: "numeric", month: "2-digit", day: "2-digit", hour: "2-digit", minute: "2-digit", hourCycle: "h23" }).format(new Date(end)) + " 北京时间",
    kind: latest.kind, short_trial: shortTrial };
}

function schedule(membership) {
  if (!membership.eligible) return [];
  const end = ms(membership.expires_at);
  const endDay = day(end);
  if (membership.short_trial) return [{ stage: "trial_before", at: atTen(endDay - 1), until: end }];
  return [
    { stage: "before_7", at: atTen(endDay - 7), until: atTen(endDay - 2) },
    { stage: "before_2", at: atTen(endDay - 2), until: end },
    { stage: "after_1", at: atTen(endDay + 1), until: atTen(endDay + 3) },
  ];
}

function nextNotice(membership, state, now) {
  if (!membership.eligible || !state.enabled) return null;
  const attempted = state.cycles[membership.expires_at] || {};
  if (Object.keys(attempted).length >= (membership.short_trial ? 1 : 3)) return null;
  for (const row of schedule(membership)) {
    if (attempted[row.stage] || now >= row.until) continue;
    let next = Math.max(now, row.at, (ms(state.last_attempt_at) || 0) + GAP);
    if (!inWindow(next)) next = atTen(day(next) + (next >= atTen(day(next)) ? 1 : 0));
    if (next < row.until) return { ...row, next, due: inWindow(now) && now >= row.at && now >= (ms(state.last_attempt_at) || 0) + GAP };
  }
  return null;
}

function emailContent(membership, stage, unsubscribeUrl = "") {
  const expired = stage === "after_1";
  const subject = expired ? "KC桌面会员到期提醒" : "KC桌面会员即将到期提醒";
  const text = ["您好，", "", `您在 KC桌面的${membership.kind === "trial" ? "体验" : "会员"}访问权限${expired ? "已于" : "将于"} ${membership.expires_bjt} 到期。`,
    "如需续期或核对权限，请联系 info@kcdesk.com，或添加微信 MacroGate。", "如您已经续期，以账户中最新的权限状态为准。", "",
    unsubscribeUrl ? `不再接收到期邮件提醒：${unsubscribeUrl}` : "可在网站账户中的“到期邮件提醒”关闭此类邮件。"].join("\n");
  return { subject, text, html: `<div style="font-family:sans-serif;line-height:1.7;white-space:pre-wrap">${escapeHtml(text)}</div>` };
}

export function createExpiryReminders(deps) {
  async function read(env, id) {
    const object = await deps.bucket(env).get(key(id));
    const value = object ? await object.json() : { version: 1, user_id: String(id), enabled: true, cycles: {}, last_attempt_at: "", last_status: "" };
    if (!value || value.version !== 1 || value.user_id !== String(id) || typeof value.enabled !== "boolean"
      || !value.cycles || typeof value.cycles !== "object" || Array.isArray(value.cycles)) throw safeError();
    return { value, etag: object?.etag || "" };
  }
  async function mutate(env, id, apply) {
    for (let i = 0; i < 8; i += 1) {
      const { value, etag } = await read(env, id);
      const result = apply(value);
      if (!result.changed) return { state: value, ...result };
      const written = await deps.bucket(env).put(key(id), JSON.stringify(value), {
        onlyIf: etag ? { etagMatches: etag } : { etagDoesNotMatch: "*" },
        httpMetadata: { contentType: "application/json; charset=utf-8", cacheControl: "private, no-store" },
      });
      if (written !== null) return { state: value, ...result };
    }
    throw safeError();
  }
  async function preferences(env, user, enabled) {
    if (typeof enabled !== "boolean") throw Object.assign(new Error("Invalid preference"), { code: "REMINDER_INVALID" });
    return mutate(env, user.id, (state) => { state.enabled = enabled; state.preferences_updated_at = iso(Date.now()); return { changed: true }; });
  }
  async function status(env, user, now = Date.now()) {
    const [snapshot, stored] = await Promise.all([deps.load(env, user, false), read(env, user.id)]);
    const membership = resolveExpiryMembership(snapshot, now);
    const next = nextNotice(membership, stored.value, now);
    return { ok: true, preferences: { enabled: stored.value.enabled }, reminder: {
      eligible: membership.eligible && stored.value.enabled,
      reason: !stored.value.enabled ? "unsubscribed" : membership.reason,
      expires_at: membership.expires_at || "", expires_bjt: membership.expires_bjt || "",
      kind: membership.kind || "", short_trial: Boolean(membership.short_trial),
      next_stage: next?.stage || "", next_send_at: next ? iso(next.next) : "",
      last_attempt_at: stored.value.last_attempt_at || "", last_status: stored.value.last_status || "",
    }, preview: next ? (({ subject, text }) => ({ subject, text }))(emailContent(membership, next.stage)) : null };
  }
  async function attempt(env, user, now = Date.now()) {
    if (!deps.configured(env) || !inWindow(now)) return { attempted: false, status: "not_due" };
    const initial = resolveExpiryMembership(await deps.load(env, user, false), now);
    let reserved;
    reserved = await mutate(env, user.id, (state) => {
      const due = nextNotice(initial, state, now);
      if (!due?.due) return { changed: false, reserved: false };
      const cycle = state.cycles[initial.expires_at] || {};
      state.cycles[initial.expires_at] = { ...cycle, [due.stage]: { status: "pending", attempted_at: iso(now) } };
      state.last_attempt_at = iso(now);
      state.last_status = "pending";
      return { changed: true, reserved: true, stage: due.stage };
    });
    if (!reserved.reserved) return { attempted: false, status: "not_due" };
    const stage = reserved.stage;
    let outcome = "unknown";
    try {
      // Recheck authoritative identity, entitlement, administrator precedence,
      // and preferences immediately before the single provider call.
      const fresh = await deps.load(env, user, true);
      const preference = await read(env, user.id);
      const checkedNow = Math.max(now, deps.now ? deps.now() : Date.now());
      const current = resolveExpiryMembership(fresh, checkedNow);
      const currentStage = schedule(current).find((row) => row.stage === stage);
      if (!preference.value.enabled || !current.eligible || current.expires_at !== initial.expires_at || current.kind !== initial.kind
        || !inWindow(checkedNow) || !currentStage || checkedNow >= currentStage.until) outcome = "cancelled";
      else {
        const unsubscribeUrl = await deps.unsubscribeUrl(env, fresh.user);
        const result = await deps.send(env, { to: fresh.user.email, ...emailContent(current, stage, unsubscribeUrl), tags: ["membership-expiry"] });
        outcome = result?.sent ? "sent" : "failed";
      }
    } catch (_error) { outcome = "unknown"; }
    // A failure here leaves pending, which is also terminal for automatic retry.
    await mutate(env, user.id, (state) => {
      const record = state.cycles[initial.expires_at]?.[stage];
      if (!record || record.status !== "pending") return { changed: false };
      record.status = outcome;
      record.finished_at = iso(now);
      if (state.last_attempt_at === iso(now)) state.last_status = outcome;
      return { changed: true };
    });
    return { attempted: true, status: outcome };
  }
  async function scanStatus(env) {
    const object = await deps.bucket(env).get(SCAN_KEY);
    const value = object ? await object.json() : {};
    return { date: String(value.date || ""), complete: Boolean(value.complete), processed: Number(value.processed) || 0,
      attempted: Number(value.attempted) || 0, errors: Number(value.errors) || 0,
      pending: Boolean(value.cursor), updated_at: String(value.updated_at || ""),
      capacity_per_tick: 20, max_provider_attempts_per_tick: 9 };
  }
  async function scan(env, now = Date.now()) {
    if (!inWindow(now) || !deps.configured(env)) return { skipped: true };
    const bucket = deps.bucket(env);
    const date = iso(now + 8 * 3600000).slice(0, 10);
    const owner = crypto.randomUUID();
    let claimed;
    for (let i = 0; i < 6; i += 1) {
      const object = await bucket.get(SCAN_KEY);
      const old = object ? await object.json() : {};
      if (ms(old.lease_until) > now || old.date === date && old.complete) return { skipped: true };
      // Carry an unfinished cursor across days instead of starving later users.
      const samePass = !old.complete;
      const next = { version: 1, date, cursor: samePass ? old.cursor || "" : "", complete: false,
        processed: samePass ? Number(old.processed) || 0 : 0, attempted: samePass ? Number(old.attempted) || 0 : 0,
        errors: samePass ? Number(old.errors) || 0 : 0, owner, lease_until: iso(now + 180000), updated_at: iso(now) };
      const result = await bucket.put(SCAN_KEY, JSON.stringify(next), { onlyIf: object?.etag ? { etagMatches: object.etag } : { etagDoesNotMatch: "*" } });
      if (result !== null) { claimed = next; break; }
    }
    if (!claimed) throw safeError();
    let providerAttempts = 0;
    try {
      const page = await deps.list(env, claimed.cursor, 20);
      let lastCursor = claimed.cursor;
      let done = true;
      for (const item of page.items) {
        if (providerAttempts >= 9) { done = false; break; }
        try {
          const result = await attempt(env, item.user, now);
          if (result.attempted) { providerAttempts += 1; claimed.attempted += 1; }
        } catch (_error) {
          claimed.errors += 1;
          // A post-send storage error may hide an attempted delivery. Count it
          // conservatively toward this invocation's external-request budget.
          providerAttempts += 1;
        }
        lastCursor = item.cursor;
        claimed.processed += 1;
      }
      claimed.cursor = done ? page.cursor || "" : lastCursor;
      claimed.complete = done && !page.cursor;
    } catch (_error) { claimed.errors += 1; }
    const object = await bucket.get(SCAN_KEY);
    const latest = object ? await object.json() : {};
    if (latest.owner === owner) {
      await bucket.put(SCAN_KEY, JSON.stringify({ ...claimed, owner: "", lease_until: "", updated_at: iso(now) }), { onlyIf: { etagMatches: object.etag } });
    }
    return scanStatus(env);
  }
  return { status, preferences, attempt, scan, scanStatus };
}
