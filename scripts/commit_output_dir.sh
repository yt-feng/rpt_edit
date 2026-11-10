#!/usr/bin/env bash
set -euo pipefail

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

case "$MAX_ATTEMPTS" in
  ''|*[!0-9]*|0) echo "ERROR: max_attempts must be a positive integer."; exit 2 ;;
esac

CODE_HEAD="$(git rev-parse --verify HEAD)"
repo_root="$(git rev-parse --show-toplevel)"
OUTPUT_DIR="$(python3 - "$repo_root" "$PWD" "$OUTPUT_DIR" <<'PY'
import os, sys
root, cwd, value = sys.argv[1:]
root = os.path.realpath(root)
path = os.path.abspath(os.path.join(os.path.realpath(cwd), value))
if os.path.commonpath((root, path)) != root:
    raise SystemExit('ERROR: Output path must belong to the current repository.')
relative = os.path.relpath(path, root)
if relative == '.git' or relative.startswith('.git' + os.sep):
    raise SystemExit('ERROR: Output path must not select Git metadata.')
print(relative)
PY
)"
cd "$repo_root"

# Repeated calls in one Actions job may evolve a previously acknowledged file.
# Retain only this producer's virtual tree; adopting the merged remote tree
# would turn remote-only records missing locally into later deletions.
baseline_ref=""
baseline_old=""
if [ "${GITHUB_ACTIONS:-false}" = true ]; then
  if [[ ! "${GITHUB_RUN_ID:-}" =~ ^[1-9][0-9]*$ ]] || [[ ! "${GITHUB_RUN_ATTEMPT:-}" =~ ^[1-9][0-9]*$ ]] || [ -z "${GITHUB_JOB:-}" ]; then
    echo "ERROR: Complete Actions producer identity is required."
    exit 2
  fi
  producer_key="$(printf '%s\n' "$CODE_HEAD" "${GITHUB_REPOSITORY:-}" "$GITHUB_RUN_ID" "$GITHUB_RUN_ATTEMPT" "$GITHUB_JOB" | git hash-object --stdin)"
  baseline_ref="refs/codex-output-producers/$producer_key"
elif [ -n "${OUTPUT_PRODUCER_ID:-}" ]; then
  producer_key="$(printf '%s\n' "$CODE_HEAD" "$OUTPUT_PRODUCER_ID" | git hash-object --stdin)"
  baseline_ref="refs/codex-output-producers/$producer_key"
fi
ORIGINAL_BASE="$CODE_HEAD"
if [ -n "$baseline_ref" ]; then
  baseline_old="$(git rev-parse --verify --quiet "$baseline_ref" || true)"
  if [ -n "$baseline_old" ]; then
    if ! git merge-base --is-ancestor "$CODE_HEAD" "$baseline_old"; then
      echo "ERROR: Producer baseline does not belong to this checkout."
      exit 2
    fi
    ORIGINAL_BASE="$baseline_old"
  fi
fi
ORIGINAL_TREE="$(git rev-parse "$ORIGINAL_BASE^{tree}")"
output_is_dir=false
if [ -d "$OUTPUT_DIR" ] || [ "$(git cat-file -t "$ORIGINAL_BASE:$OUTPUT_DIR" 2>/dev/null || true)" = tree ]; then
  output_is_dir=true
fi
if [ ! -e "$OUTPUT_DIR" ] && [ -z "$(git --literal-pathspecs ls-tree -r --name-only "$ORIGINAL_BASE" -- "$OUTPUT_DIR")" ]; then
  echo "Output path does not exist: $OUTPUT_DIR"
  if [ "$REQUIRE_PUSH_SUCCESS" = "true" ]; then
    exit 2
  fi
  exit 0
fi

capabilities="$(LC_ALL=C git merge-recursive -h 2>&1 || true)"
case "$capabilities" in *'usage: git merge-recursive'*) ;; *) echo "ERROR: Git with the merge-recursive plumbing command is required."; exit 2 ;; esac

scratch="$(mktemp -d "${TMPDIR:-/tmp}/portal-output-intent.XXXXXX")"
trap 'rm -rf -- "$scratch"' EXIT
# Do not change the caller's HEAD, index, working files or Git identity config.
# Freeze only the requested path's final working-tree state against its original
# checkout, so later remote-only files never become accidental local deletions.
export GIT_INDEX_FILE="$scratch/index"
git read-tree "$ORIGINAL_BASE"
if ! git --literal-pathspecs add -A -- "$OUTPUT_DIR"; then
  # A fresh alternate index in a sparse checkout can report an ignored tracked
  # PDF as ignored during add. Inspect the ignore rule independently of index
  # tracking; the separate opt-in below still admits only explicit PDF paths.
  if ! git check-ignore --no-index --quiet -- "$OUTPUT_DIR"; then
    echo "ERROR: Could not freeze generated output changes."
    exit 2
  fi
fi
if [ "$ALLOW_FORCE_PDFS" = "true" ]; then
  if [ -f "$OUTPUT_DIR" ]; then
    case "$OUTPUT_DIR" in *.pdf) git --literal-pathspecs add -f -- "$OUTPUT_DIR" ;; esac
  elif [ -d "$OUTPUT_DIR" ]; then
    while IFS= read -r -d '' pdf_path; do
      git --literal-pathspecs add -f -- "$pdf_path"
    done < <(find "$OUTPUT_DIR" -type f -name "*.pdf" -print0)
  fi
fi
INTENT_TREE="$(git write-tree)"
unset GIT_INDEX_FILE
if [ "$INTENT_TREE" = "$ORIGINAL_TREE" ]; then
  echo "No generated changes to commit for $OUTPUT_DIR."
  exit 0
fi

check_sizes() {
  local before_tree="$1" after_tree="$2" staged_path staged_size oversized_files=0
  git diff-tree -r --no-renames --no-commit-id --name-only --diff-filter=ACMR -z "$before_tree" "$after_tree" > "$scratch/changed-paths"
  while IFS= read -r -d '' staged_path; do
    if ! staged_size="$(git cat-file -s "$after_tree:$staged_path")"; then
      echo "ERROR: Could not inspect staged object size: $staged_path"
      exit 2
    fi
    if [ "$staged_size" -gt "$GITHUB_MAX_FILE_BYTES" ]; then
      echo "ERROR: Staged file exceeds GitHub's ${GITHUB_MAX_FILE_BYTES}-byte limit: $staged_path ($staged_size bytes)"
      oversized_files=$((oversized_files + 1))
    fi
  done < "$scratch/changed-paths"
  if [ "$oversized_files" -gt 0 ]; then
    echo "ERROR: Stopping without retrying. Split or prune the generated file first."
    exit 3
  fi
}

check_sizes "$ORIGINAL_TREE" "$INTENT_TREE"
echo "Frozen producer output delta:"
git diff-tree -r --no-commit-id --name-status "$ORIGINAL_TREE" "$INTENT_TREE"
make_commit() {
  git -c user.name='github-actions[bot]' -c user.email='41898282+github-actions[bot]@users.noreply.github.com' \
    commit-tree "$1" -p "$2" -m "$COMMIT_MESSAGE"
}
INTENT_COMMIT="$(make_commit "$INTENT_TREE" "$ORIGINAL_BASE")"

acknowledge_intent() {
  if [ -n "$baseline_ref" ]; then
    if ! git update-ref "$baseline_ref" "$INTENT_COMMIT" "$baseline_old"; then
      echo "ERROR: Output was acknowledged but its producer baseline changed concurrently."
      exit 1
    fi
  fi
}

fail_handoff() {
  echo "WARNING: $1 Generated files remain in the caller's working tree."
  if [ "$REQUIRE_PUSH_SUCCESS" = "true" ]; then
    echo "ERROR: A downstream job requires $OUTPUT_DIR from origin/main; failing this handoff."
    exit 1
  fi
  exit 0
}

merge_number=0
merge_latest() {
  if ! git fetch --no-tags --depth=1 origin main; then
    return 1
  fi
  REMOTE_HEAD="$(git rev-parse --verify FETCH_HEAD)"
  REMOTE_TREE="$(git rev-parse "$REMOTE_HEAD^{tree}")"
  merge_number=$((merge_number + 1))
  local merge_index="$scratch/merge-$merge_number.index"
  local merge_worktree="$scratch/merge-$merge_number.worktree"
  mkdir "$merge_worktree"
  GIT_INDEX_FILE="$merge_index" git -c core.sparseCheckout=false read-tree "$REMOTE_HEAD"
  # This longstanding plumbing also supports the deployed Git 2.34 runner.
  # An empty private worktree materializes only files touched by the merge,
  # never a second checkout of the repository. Explicit base works with shallow
  # CI history. A conflict must not produce a commit, even for optional callers.
  if ! GIT_INDEX_FILE="$merge_index" GIT_WORK_TREE="$merge_worktree" \
      git -c core.sparseCheckout=false merge-recursive "$ORIGINAL_BASE" -- "$REMOTE_HEAD" "$INTENT_COMMIT"; then
    fail_handoff "Generated output conflicts with current main; no commit was pushed."
  fi
  MERGED_TREE="$(GIT_INDEX_FILE="$merge_index" git write-tree)"
  if [ "$(git cat-file -t "$MERGED_TREE")" != tree ]; then
    echo "ERROR: Git did not produce a verified merged tree."
    exit 2
  fi
  git diff-tree -r --no-renames --no-commit-id --name-only -z "$REMOTE_TREE" "$MERGED_TREE" > "$scratch/merged-paths"
  while IFS= read -r -d '' merged_path; do
    if [ "$OUTPUT_DIR" = . ] || [ "$merged_path" = "$OUTPUT_DIR" ]; then
      continue
    fi
    if [ "$output_is_dir" = true ]; then
      case "$merged_path" in "$OUTPUT_DIR"/*) continue ;; esac
    fi
    fail_handoff "Merge would change a path outside the requested output; no commit was pushed."
  done < "$scratch/merged-paths"
  check_sizes "$REMOTE_TREE" "$MERGED_TREE"
  return 0
}

for attempt in $(seq 1 "$MAX_ATTEMPTS"); do
  echo "Commit attempt $attempt/$MAX_ATTEMPTS for $OUTPUT_DIR"
  if merge_latest; then
    if [ "$MERGED_TREE" = "$REMOTE_TREE" ]; then
      acknowledge_intent
      echo "Generated output delta is already present on origin/main."
      exit 0
    fi
    CANDIDATE_COMMIT="$(make_commit "$MERGED_TREE" "$REMOTE_HEAD")"
    if git push origin "$CANDIDATE_COMMIT:refs/heads/main"; then
    acknowledge_intent
    echo "Committed and pushed $OUTPUT_DIR."
    exit 0
    fi
  fi
  if [ "$attempt" -lt "$MAX_ATTEMPTS" ]; then
    echo "Git fetch or push did not finish successfully; refreshing the same frozen output delta."
    sleep $((attempt * 8))
  fi
done

# One bounded readback resolves a push accepted before its acknowledgement was
# lost, including on the last attempt. It never starts another write attempt.
if merge_latest && [ "$MERGED_TREE" = "$REMOTE_TREE" ]; then
  acknowledge_intent
  echo "Verified generated output delta on origin/main after the uncertain push."
  exit 0
fi
fail_handoff "Could not push $OUTPUT_DIR after $MAX_ATTEMPTS attempts."
