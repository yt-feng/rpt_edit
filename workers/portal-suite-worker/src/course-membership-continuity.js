// Continuity is evidence about server-observed membership, never account age.
// The current entitlement must still be checked independently on every read.
const BJT_OFFSET_MS = 8 * 60 * 60 * 1000;
const FINGERPRINT = /^[a-f0-9]{64}$/u;
const EVIDENCE = new Set(["issued", "observed", "verified"]);

function continuityError(message, code = "CONTINUITY_UNAVAILABLE") {
  const error = new Error(message);
  error.code = code;
  return error;
}

function instant(value) {
  return typeof value === "string" && value ? Date.parse(value) : NaN;
}

export function membershipEligibleAt(since) {
  const start = instant(since);
  if (!Number.isFinite(start)) throw continuityError("Invalid membership start.");
  const local = new Date(start + BJT_OFFSET_MS);
  const year = local.getUTCFullYear();
  const month = local.getUTCMonth() + 2;
  const lastDay = new Date(Date.UTC(year, month + 1, 0)).getUTCDate();
  const anniversary = Date.UTC(
    year, month, Math.min(local.getUTCDate(), lastDay),
    local.getUTCHours(), local.getUTCMinutes(), local.getUTCSeconds(), local.getUTCMilliseconds(),
  );
  return new Date(anniversary - BJT_OFFSET_MS).toISOString();
}

export function validateContinuityVerification(value, nowMs = Date.now()) {
  const raw = String(value && value.since || "").trim();
  const since = /^\d{4}-\d{2}-\d{2}$/u.test(raw) ? `${raw}T00:00:00+08:00` : raw;
  const time = instant(since);
  const parts = since.match(/^(\d{4})-(\d{2})-(\d{2})T(\d{2}):(\d{2}):(\d{2})/u);
  const calendarValid = parts && Number(parts[2]) >= 1 && Number(parts[2]) <= 12
    && Number(parts[3]) >= 1 && Number(parts[3]) <= new Date(Date.UTC(Number(parts[1]), Number(parts[2]), 0)).getUTCDate()
    && Number(parts[4]) < 24 && Number(parts[5]) < 60 && Number(parts[6]) < 60;
  const reason = String(value && value.audit_reason || "").replace(/\s+/gu, " ").trim();
  const actor = String(value && value.actor || "").trim();
  // Require an explicit timezone for a timestamp; a date is a Beijing date.
  if (!/^\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}(?:\.\d{1,3})?(?:Z|[+-]\d{2}:\d{2})$/u.test(since)
    || !calendarValid || !Number.isFinite(time) || time < 0 || time > nowMs
    || (/^\d{4}-\d{2}-\d{2}$/u.test(raw) && new Date(time + BJT_OFFSET_MS).toISOString().slice(0, 10) !== raw)
    || reason.length < 5 || reason.length > 500 || !actor || actor.length > 254) {
    throw continuityError("请填写有效的连续会员起始时间和 5–500 字核验依据。", "CONTINUITY_INVALID_VERIFICATION");
  }
  return { since: new Date(time).toISOString(), audit_reason: reason, actor };
}

function validateMembership(value) {
  if (!value || !FINGERPRINT.test(String(value.fingerprint || "")) || typeof value.active !== "boolean"
    || (value.active && value.covered_until !== null && !Number.isFinite(instant(value.covered_until)))) {
    throw continuityError("Membership evidence could not be verified.");
  }
  return value;
}

function validateRecord(row) {
  if (!row || row.schema_version !== 1 || !FINGERPRINT.test(String(row.authority_fingerprint || ""))
    || typeof row.active !== "boolean" || !String(row.revision || "")
    || !Number.isFinite(instant(row.updated_at))
    || (row.active && (!Number.isFinite(instant(row.since)) || !EVIDENCE.has(row.evidence)
      || (row.covered_until !== null && !Number.isFinite(instant(row.covered_until)))
      || instant(row.since) > instant(row.updated_at)
      || (row.covered_until !== null && instant(row.covered_until) <= instant(row.since))))
    || (!row.active && (row.since !== null || row.covered_until !== null))) {
    throw continuityError("Membership continuity record could not be verified.");
  }
  return row;
}

async function readRecord(bucket, key) {
  const object = await bucket.get(key);
  if (!object) return { record: null, etag: "" };
  if (!object.etag) throw continuityError("Membership continuity version is unavailable.");
  return { record: validateRecord(JSON.parse(await object.text())), etag: String(object.etag) };
}

function covers(record, time) {
  return Boolean(record && record.active && instant(record.since) <= time
    && (record.covered_until === null || instant(record.covered_until) >= time));
}

export function publicMembershipContinuity(record, membership, nowMs = Date.now()) {
  validateMembership(membership);
  if (!membership.active) return { allowed: false, since: null, eligible_at: null, reason: membership.reason || "membership_inactive" };
  if (!record || record.authority_fingerprint !== membership.fingerprint || !covers(record, nowMs)) {
    return { allowed: false, since: null, eligible_at: null, reason: "needs_history_verification" };
  }
  const eligibleAt = membershipEligibleAt(record.since);
  const allowed = nowMs >= instant(eligibleAt);
  return {
    allowed,
    since: record.since,
    eligible_at: eligibleAt,
    reason: allowed ? "eligible" : record.evidence === "observed" ? "needs_history_verification" : "tenure_incomplete",
  };
}

// loadMembership always re-reads authoritative state. A missed/failed mutation
// hook invalidates its fingerprint, so a later read starts fresh observation.
// transition.before/after are snapshots around ONE accepted primary mutation.
export async function reconcileMembershipContinuity({
  bucket, key, loadMembership, transition = null, verification = null, inferLegacyStart = null, now = Date.now,
}) {
  for (let attempt = 0; attempt < 4; attempt += 1) {
    const membership = validateMembership(await loadMembership());
    const { record, etag } = await readRecord(bucket, key);
    const nowMs = now();
    if (membership.active && membership.covered_until !== null && instant(membership.covered_until) <= nowMs) {
      throw continuityError("Membership changed during verification.", "CONTINUITY_CONFLICT");
    }
    if (verification && (!membership.active || membership.fingerprint !== verification.fingerprint)) {
      throw continuityError("当前完整会员资格已变化，请刷新后核验。", "CONTINUITY_CONFLICT");
    }
    const unchanged = record && record.authority_fingerprint === membership.fingerprint
      && record.active === membership.active
      && (!membership.active || covers(record, nowMs));
    if (unchanged && !verification) {
      const checked = validateMembership(await loadMembership());
      if (checked.fingerprint !== membership.fingerprint || checked.active !== membership.active) continue;
      return { record, access: publicMembershipContinuity(record, checked, now()) };
    }
    const at = new Date(nowMs).toISOString();
    const linked = Boolean(transition && transition.before && transition.after
      && transition.before.fingerprint === record?.authority_fingerprint
      && transition.after.fingerprint === membership.fingerprint
      && covers(record, nowMs));
    const inferred = !record && membership.active && !verification && inferLegacyStart
      ? await inferLegacyStart(membership, nowMs) : null;
    if (inferred && (!Number.isFinite(instant(inferred.since)) || instant(inferred.since) > nowMs)) {
      throw continuityError("Legacy membership evidence could not be verified.");
    }
    const next = {
      schema_version: 1,
      revision: crypto.randomUUID(),
      authority_fingerprint: membership.fingerprint,
      active: membership.active,
      since: membership.active ? (verification?.since || inferred?.since || (linked ? record.since : at)) : null,
      covered_until: membership.active ? membership.covered_until : null,
      evidence: membership.active ? (verification || inferred ? "verified" : linked ? record.evidence
        : transition?.after?.fingerprint === membership.fingerprint && transition?.before?.active === false ? "issued" : "observed") : "observed",
      updated_at: at,
    };
    validateRecord(next);
    const audit = {
      schema_version: 1,
      type: verification ? "membership_continuity_verified" : inferred ? "membership_history_recovered" : transition ? "membership_changed" : "membership_observed",
      // An audit proposal is committed only when reachable from the current
      // record's revision chain; an abandoned CAS proposal grants nothing.
      proposed_at: at,
      previous_revision: record?.revision || null,
      next,
      actor: verification?.actor || "server",
      audit_reason: verification?.audit_reason || inferred?.audit_reason || transition?.reason || "current_membership_observation",
    };
    const auditKey = `${key}/events/${next.revision}.json`;
    const auditWritten = await bucket.put(auditKey, JSON.stringify(audit), {
      onlyIf: { etagDoesNotMatch: "*" }, httpMetadata: { contentType: "application/json; charset=utf-8" },
    });
    if (auditWritten === null) throw continuityError("Membership audit could not be stored.");
    // Recheck after the audit write: a stale hook must not bridge a revoke and
    // regrant that happened while it was waiting on storage.
    const checked = validateMembership(await loadMembership());
    if (checked.fingerprint !== membership.fingerprint || checked.active !== membership.active) {
      if (verification) throw continuityError("会员资格已变化，请刷新后核验。", "CONTINUITY_CONFLICT");
      transition = null;
      continue;
    }
    const written = await bucket.put(key, JSON.stringify(next), {
      onlyIf: etag ? { etagMatches: etag } : { etagDoesNotMatch: "*" },
      httpMetadata: { contentType: "application/json; charset=utf-8" },
    });
    if (written === null) {
      if (verification) throw continuityError("连续会员记录已变化，请刷新后核验。", "CONTINUITY_CONFLICT");
      continue;
    }
    const saved = (await readRecord(bucket, key)).record;
    const finalMembership = validateMembership(await loadMembership());
    if (!saved || saved.revision !== next.revision || finalMembership.fingerprint !== membership.fingerprint
      || finalMembership.active !== membership.active) {
      throw continuityError("Membership changed during verification.", "CONTINUITY_CONFLICT");
    }
    return { record: saved, access: publicMembershipContinuity(saved, finalMembership, now()) };
  }
  throw continuityError("Membership continuity changed concurrently.", "CONTINUITY_CONFLICT");
}
