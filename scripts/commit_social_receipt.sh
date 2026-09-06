#!/usr/bin/env bash
set -euo pipefail

mode="${1:-}"
public_receipt="${2:-}"
encrypted_receipt="${3:-}"
commit_message="${4:-Record guarded social publication}"
max_attempts="${5:-8}"

if [[ "$mode" != "reserve" && "$mode" != "finalize" ]]; then
  echo "Usage: commit_social_receipt.sh reserve|finalize <public.json> <encrypted.json.enc-or-empty> [message] [attempts]" >&2
  exit 2
fi
if [[ ! "$public_receipt" =~ ^social_publish/receipts/[a-z0-9][a-z0-9._-]{7,79}\.json$ ]]; then
  echo "Public receipt path is not canonical" >&2
  exit 2
fi
if [[ "$mode" == "finalize" ]]; then
  if [[ "$encrypted_receipt" != "$public_receipt.enc" ]]; then
    echo "Encrypted receipt path must be the exact public receipt companion" >&2
    exit 2
  fi
elif [[ -n "$encrypted_receipt" ]]; then
  echo "Reserve mode does not accept an encrypted receipt" >&2
  exit 2
fi
if [[ ! -f "$public_receipt" ]]; then
  echo "Public receipt is missing" >&2
  exit 2
fi
if [[ "$mode" == "finalize" && ! -f "$encrypted_receipt" ]]; then
  echo "Encrypted receipt is missing" >&2
  exit 2
fi
if [[ ! "$max_attempts" =~ ^[1-9][0-9]*$ || "$max_attempts" -gt 12 ]]; then
  echo "Attempts must be an integer from 1 to 12" >&2
  exit 2
fi
: "${SOCIAL_GIT_TOKEN:?SOCIAL_GIT_TOKEN is required}"

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

temporary_dir="$(mktemp -d "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/social-receipt-commit.XXXXXX")"
trap 'rm -rf "$temporary_dir"' EXIT
script_dir="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd -P)"
askpass="$script_dir/social_git_askpass.sh"
if [[ ! -x "$askpass" ]]; then
  echo "Git askpass helper is unavailable" >&2
  exit 2
fi

remote_public="$temporary_dir/remote-public.json"
remote_encrypted="$temporary_dir/remote-encrypted.json.enc"

validate_final_transition() {
  python3 -B - "$public_receipt" "$remote_public" <<'PY'
import json
import sys
from pathlib import Path

local = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
remote = json.loads(Path(sys.argv[2]).read_text(encoding="utf-8"))
for key in ("schema_version", "content_id", "manifest_sha256", "run_id", "code_sha"):
    if local.get(key) != remote.get(key):
        raise SystemExit("Remote reservation does not match this final receipt")
if remote.get("state") not in {"reserved", "partial", "failed", "published"}:
    raise SystemExit("Remote receipt is not in a finalizable state")
if local.get("state") not in {"partial", "failed", "published"}:
    raise SystemExit("Local receipt is not final")
PY
}

for attempt in $(seq 1 "$max_attempts"); do
  echo "Social receipt commit attempt $attempt/$max_attempts ($mode)"
  git fetch --depth=1 origin main
  remote_public_exists="false"
  if git cat-file -e "FETCH_HEAD:$public_receipt" 2>/dev/null; then
    git show "FETCH_HEAD:$public_receipt" > "$remote_public"
    remote_public_exists="true"
  fi

  if [[ "$mode" == "reserve" ]]; then
    if [[ "$remote_public_exists" == "true" ]]; then
      if cmp -s "$public_receipt" "$remote_public"; then
        echo "Identical reservation is already durable."
        exit 0
      fi
      echo "A different receipt already exists for this content ID" >&2
      exit 4
    fi
  else
    if [[ "$remote_public_exists" != "true" ]]; then
      echo "The durable reservation is missing" >&2
      exit 4
    fi
    validate_final_transition
    remote_encrypted_exists="false"
    if git cat-file -e "FETCH_HEAD:$encrypted_receipt" 2>/dev/null; then
      git show "FETCH_HEAD:$encrypted_receipt" > "$remote_encrypted"
      remote_encrypted_exists="true"
      if ! cmp -s "$encrypted_receipt" "$remote_encrypted"; then
        echo "A different encrypted locator already exists" >&2
        exit 4
      fi
    fi
    if cmp -s "$public_receipt" "$remote_public" \
       && [[ "$remote_encrypted_exists" == "true" ]]; then
      echo "Identical final receipt is already durable."
      exit 0
    fi
  fi

  # Base the exact-path commit on current main without staging any other
  # working-tree differences or deletions.
  git reset --mixed FETCH_HEAD
  if [[ "$mode" == "reserve" ]]; then
    git add -- "$public_receipt"
  else
    git add -- "$public_receipt" "$encrypted_receipt"
  fi
  if git diff --cached --quiet; then
    echo "No exact receipt changes to commit."
    exit 0
  fi
  git commit -m "$commit_message"
  if GIT_ASKPASS="$askpass" GIT_TERMINAL_PROMPT=0 git push origin HEAD:main; then
    echo "Exact social receipt path(s) committed and pushed."
    exit 0
  fi
  delay=$((attempt * 5))
  if [[ "$delay" -gt 40 ]]; then
    delay=40
  fi
  echo "Push changed concurrently; retrying after ${delay}s."
  sleep "$delay"
done

echo "Could not make the social receipt durable after $max_attempts attempts" >&2
exit 1
