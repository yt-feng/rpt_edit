#!/usr/bin/env bash
set -u

OUTPUT_DIR="${1:-}"
COMMIT_MESSAGE="${2:-Commit generated outputs}"
MAX_ATTEMPTS="${3:-8}"
REQUIRE_PUSH_SUCCESS="${4:-false}"
ALLOW_FORCE_PDFS="${5:-false}"
GITHUB_MAX_FILE_BYTES="${GITHUB_MAX_FILE_BYTES:-104857600}"

case "$GITHUB_MAX_FILE_BYTES" in
  ''|*[!0-9]*)
    echo "ERROR: GITHUB_MAX_FILE_BYTES must be a positive integer."
    exit 2
    ;;
esac
if [ "$GITHUB_MAX_FILE_BYTES" -le 0 ]; then
  echo "ERROR: GITHUB_MAX_FILE_BYTES must be a positive integer."
  exit 2
fi

case "$REQUIRE_PUSH_SUCCESS" in
  1|true|TRUE|True|yes|YES|Yes|y|Y|on|ON|On) REQUIRE_PUSH_SUCCESS="true" ;;
  *) REQUIRE_PUSH_SUCCESS="false" ;;
esac

case "$ALLOW_FORCE_PDFS" in
  1|true|TRUE|True|yes|YES|Yes|y|Y|on|ON|On) ALLOW_FORCE_PDFS="true" ;;
  *) ALLOW_FORCE_PDFS="false" ;;
esac

if [ -z "$OUTPUT_DIR" ]; then
  echo "Usage: scripts/commit_output_dir.sh <output_dir> [commit_message] [max_attempts] [require_push_success] [allow_force_pdfs]"
  exit 2
fi

if [ ! -d "$OUTPUT_DIR" ]; then
  echo "Output directory does not exist: $OUTPUT_DIR"
  if [ "$REQUIRE_PUSH_SUCCESS" = "true" ]; then
    exit 2
  fi
  exit 0
fi

git config user.name "github-actions[bot]"
git config user.email "41898282+github-actions[bot]@users.noreply.github.com"

for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  echo "Commit attempt $attempt/$MAX_ATTEMPTS for $OUTPUT_DIR"

  # Always rebase our local working tree onto the latest remote branch first.
  # reset --mixed keeps generated files in the working tree while moving HEAD/index
  # to the latest origin/main, so the next commit is based on the current remote tip.
  git fetch --depth=1 origin main
  git reset --mixed FETCH_HEAD

  git add "$OUTPUT_DIR" || true
  # Public repos must not silently force ignored source/generated PDFs into Git.
  # A caller must make that exceptional behavior explicit with argument 5.
  if [ "$ALLOW_FORCE_PDFS" = "true" ]; then
    find "$OUTPUT_DIR" -type f -name "*.pdf" -print0 | xargs -0 -r git add -f
  fi

  echo "Files staged for commit:"
  git diff --cached --name-status || true

  if git diff --cached --quiet; then
    echo "No generated changes to commit for $OUTPUT_DIR."
    exit 0
  fi

  oversized_files=0
  while IFS= read -r -d '' staged_path; do
    if ! staged_size="$(git cat-file -s ":$staged_path")"; then
      echo "ERROR: Could not inspect staged object size: $staged_path"
      exit 2
    fi
    if [ "$staged_size" -gt "$GITHUB_MAX_FILE_BYTES" ]; then
      echo "ERROR: Staged file exceeds GitHub's ${GITHUB_MAX_FILE_BYTES}-byte limit: $staged_path ($staged_size bytes)"
      oversized_files=$((oversized_files + 1))
    fi
  done < <(git diff --cached --name-only --diff-filter=ACMR -z)
  if [ "$oversized_files" -gt 0 ]; then
    echo "ERROR: This push would be rejected permanently; stopping without retrying. Split or prune the generated file first."
    exit 3
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
if [ "$REQUIRE_PUSH_SUCCESS" = "true" ]; then
  echo "ERROR: A downstream job requires $OUTPUT_DIR from origin/main; failing this handoff."
  exit 1
fi
exit 0
