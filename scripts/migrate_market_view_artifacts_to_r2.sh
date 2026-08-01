#!/usr/bin/env bash
set -euo pipefail

: "${GH_TOKEN:?GH_TOKEN is required}"
: "${GITHUB_REPOSITORY:?GITHUB_REPOSITORY is required}"
: "${RUNNER_TEMP:?RUNNER_TEMP is required}"
: "${R2_ACCOUNT_ID:?R2_ACCOUNT_ID is required}"
: "${R2_ACCESS_KEY_ID:?R2_ACCESS_KEY_ID is required}"
: "${R2_SECRET_ACCESS_KEY:?R2_SECRET_ACCESS_KEY is required}"
: "${R2_BUCKET:?R2_BUCKET is required}"

if [[ "${CONFIRM_DELETE_LEGACY_ARTIFACTS:-}" != "MIGRATE_AND_DELETE" ]]; then
  echo "Legacy artifact cleanup requires CONFIRM_DELETE_LEGACY_ARTIFACTS=MIGRATE_AND_DELETE." >&2
  exit 2
fi

retry_command() {
  local attempt
  for attempt in 1 2 3 4; do
    if "$@"; then
      return 0
    fi
    if [[ "$attempt" -eq 4 ]]; then
      echo "Command failed after $attempt attempts: $*" >&2
      return 1
    fi
    sleep $((attempt * 5))
  done
}

cleanup_artifact_dir() {
  local target="$1"
  case "$target" in
    "$RUNNER_TEMP"/market-artifact.*)
      rm -rf -- "$target"
      ;;
    *)
      echo "Refusing to clean unexpected temporary path: $target" >&2
      return 1
      ;;
  esac
}

artifact_rows() {
  gh api --paginate "repos/$GITHUB_REPOSITORY/actions/artifacts?per_page=100" \
    --jq '.artifacts[] | select((.expired | not) and (.name | startswith("market-views-pdf-"))) | [.id, .workflow_run.id, .name, .created_at] | @tsv' \
    | sort -t $'\t' -k4,4r -k1,1nr
}

artifact_count=0
pdf_count=0
artifact_snapshot="$(artifact_rows)"
while IFS=$'\t' read -r artifact_id run_id artifact_name created_at; do
  [[ -n "$artifact_id" && -n "$run_id" && -n "$artifact_name" ]] || continue
  artifact_count=$((artifact_count + 1))
  artifact_dir="$(mktemp -d "$RUNNER_TEMP/market-artifact.${artifact_id}.XXXXXX")"
  echo "Migrating artifact $artifact_id ($artifact_name, $created_at)."

  retry_command gh run download "$run_id" \
    --repo "$GITHUB_REPOSITORY" \
    --name "$artifact_name" \
    --dir "$artifact_dir"

  artifact_pdf_count=0
  while IFS= read -r -d '' pdf_path; do
    date_folder="$(basename "$(dirname "$pdf_path")")"
    filename="$(basename "$pdf_path")"
    if [[ ! "$date_folder" =~ ^([0-9]{6}|[0-9]{8})$ || "$filename" != "market_views_${date_folder}.pdf" ]]; then
      echo "Skipping a PDF outside the canonical Market Views layout: $pdf_path"
      continue
    fi
    python scripts/upload_market_view_to_r2.py \
      --date "$date_folder" \
      --pdf "$pdf_path" \
      --if-absent
    artifact_pdf_count=$((artifact_pdf_count + 1))
    pdf_count=$((pdf_count + 1))
  done < <(find "$artifact_dir" -type f -name 'market_views_*.pdf' -print0 | sort -z)

  echo "Artifact $artifact_id preserved $artifact_pdf_count PDF(s) in private R2; deleting the legacy public artifact."
  retry_command gh api --method DELETE "repos/$GITHUB_REPOSITORY/actions/artifacts/$artifact_id"
  cleanup_artifact_dir "$artifact_dir"
done <<< "$artifact_snapshot"

remaining="$(artifact_rows | wc -l | tr -d ' ')"
if [[ "$remaining" != "0" ]]; then
  echo "$remaining legacy Market Views artifact(s) remain after migration." >&2
  exit 1
fi

echo "Migrated and deleted $artifact_count legacy artifact(s); uploaded $pdf_count retained PDF copy/copies to private R2."
