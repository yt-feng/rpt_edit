const CONTEXT = ["page", "referrer", "session_id", "session_started_at", "client_ts", "first_seen_at", "is_returning",
  "landing_path", "utm_source", "utm_medium", "utm_campaign", "utm_term", "utm_content", "language", "screen",
  "navigation_type", "device_type", "bot_hint"];
const ACTIONS = {
  course_full: ["access_start", "access_result", "directory_start", "directory_result", "login_click", "verify_click", "request_submit", "request_result"],
  feedback: ["open", "form_start", "submit", "result"],
  report_discussion: ["load_result", "login_click", "form_start", "comment_submit", "comment_result", "delete_result"],
  english_commentary: ["read_click", "login_required", "read_request", "read_success", "read_error", "read_resume"],
};
export function journeyAnalyticsPayload(payload) {
  const type = String(payload?.type || payload?.data?.type || "").trim().toLowerCase();
  if (!["journey_interaction", "form_confirmation"].includes(type)) return payload;
  const input = payload.data || {}, context = {};
  for (const key of CONTEXT) context[key] = input[key];
  const choose = (name, values) => values.includes(input[name]) ? input[name] : "";
  const placement = choose("placement", Object.keys(ACTIONS));
  const count = (name) => typeof input[name] === "number" && Number.isFinite(input[name]) && input[name] >= 0
    ? Math.min(1000000, Math.floor(input[name])) : null;
  const server = type === "form_confirmation";
  return { type, visitor_id: payload.visitor_id, session_id: payload.session_id,
    client_ts: payload.client_ts, path: payload.path, data: {
      ...context, placement,
      measurement_version: choose("measurement_version", ["journey-v1"]),
      action: choose("action", server ? ["provider_result"] : ACTIONS[placement] || []),
      status: choose("status", ["pending", "guest", "success", "error", "denied", "deduplicated", "provider_accepted", "failed", "outcome_unknown", "unavailable", "no_email"]),
      error: choose("error", ["auth", "quota", "forbidden", "network", "timeout", "server", "validation", "unavailable", "unknown"]),
      access_state: choose("access_state", ["allowed", "tenure_incomplete", "needs_history_verification", "not_full_member", "unauthenticated", "membership_inactive", "account_disabled", "eligible"]),
      request_kind: choose("request_kind", ["registration", "report", "course", "membership", "research", "newsfeed", "feedback", "unknown"]),
      acknowledgement_status: choose("acknowledgement_status", ["provider_accepted", "not_accepted", "unknown"]),
      deduplicated: input.deduplicated === true,
      report_id: ["report_discussion", "english_commentary"].includes(placement) && /^[A-Za-z0-9_.:-]{1,120}$/.test(input.report_id || "") ? input.report_id : "",
      source: choose("source", ["catalog", "external", "hot", "thinktank", "authority", "report-a"]),
      result_count: count("result_count"), count: count("count"), duration_ms: count("duration_ms"),
    } };
}
