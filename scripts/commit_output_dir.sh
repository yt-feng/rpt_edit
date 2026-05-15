#!/usr/bin/env bash
set -u

OUTPUT_DIR="${1:-}"
COMMIT_MESSAGE="${2:-Commit generated outputs}"
MAX_ATTEMPTS="${3:-8}"

if [ -z "$OUTPUT_DIR" ]; then
  echo "Usage: scripts/commit_output_dir.sh <output_dir> [commit_message] [max_attempts]"
  exit 2
fi

if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Output directory does not exist: $OUTPUT_DIR"
  exit 0
fi

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  echo "Commit attempt $attempt/$MAX_ATTEMPTS for $OUTPUT_DIR"

  # Always rebase our local working tree onto the latest remote branch first.
  # reset --mixed keeps generated files in the working tree while moving HEAD/index
  # to the latest origin/main, so the next commit is based on the current remote tip.
  git fetch origin main
  git reset --mixed origin/main

  git add "$OUTPUT_DIR"
  # Force-add binary PDFs in case repo/global ignore rules skip them.
  find "$OUTPUT_DIR" -type f -name "*.pdf" -print0 | xargs -0 -r git add -f

  echo "Files staged for commit:"
  git diff --cached --name-status || true

  if git diff --cached --quiet; then
    echo "No generated changes to commit for $OUTPUT_DIR."
    exit 0
  fi

  git commit -m "$COMMIT_MESSAGE"
  if git push origin HEAD:main; then
    echo "Committed and pushed $OUTPUT_DIR."
    exit 0
  fi

  echo "Push rejected, likely because another shard pushed first. Retrying after refresh."
  sleep $((attempt * 8))
done

# Do not fail the whole shard if generation succeeded but a parallel commit lost the race.
# The workflow still uploads the artifact, and a later run can re-commit if needed.
echo "WARNING: Could not push $OUTPUT_DIR after $MAX_ATTEMPTS attempts. Artifact upload still contains outputs."
exit 0
