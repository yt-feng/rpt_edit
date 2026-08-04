#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_PATH="$ROOT_DIR/scripts/stage_pruned_generated_paths.sh"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/stage-pruned-generated-paths-test.XXXXXX")"
REPO_DIR="$TEST_ROOT/repo"

cleanup() {
  rm -rf -- "$TEST_ROOT"
}
trap cleanup EXIT

git init -q -b main "$REPO_DIR"
mkdir -p \
  "$REPO_DIR/bank_report_catalogs/260730" \
  "$REPO_DIR/bank_report_catalogs/260731" \
  "$REPO_DIR/legacy_generated/260730"
printf 'old\n' > "$REPO_DIR/bank_report_catalogs/260730/catalog.json"
printf 'new\n' > "$REPO_DIR/bank_report_catalogs/260731/catalog.json"
printf 'legacy\n' > "$REPO_DIR/legacy_generated/260730/result.txt"
printf 'seed\n' > "$REPO_DIR/README.md"
git -C "$REPO_DIR" add .
git -C "$REPO_DIR" -c user.name=test -c user.email=test@example.com commit -q -m seed

rm -rf -- \
  "$REPO_DIR/bank_report_catalogs/260730" \
  "$REPO_DIR/legacy_generated"
printf 'unrelated working-tree edit\n' >> "$REPO_DIR/README.md"

(
  cd "$REPO_DIR"
  bash "$SCRIPT_PATH" \
    xhs_notes/dropbox \
    bank_report_catalogs \
    legacy_generated \
    never_tracked
)

staged_paths="$(git -C "$REPO_DIR" diff --cached --name-only | sort)"
expected_paths=$'bank_report_catalogs/260730/catalog.json\nlegacy_generated/260730/result.txt'
if [ "$staged_paths" != "$expected_paths" ]; then
  echo "Unexpected staged paths:"
  printf '%s\n' "$staged_paths"
  exit 1
fi

if git -C "$REPO_DIR" diff --cached --name-only | grep -q '^README.md$'; then
  echo "Unrelated tracked edits must not be staged."
  exit 1
fi
if ! git -C "$REPO_DIR" diff --name-only | grep -q '^README.md$'; then
  echo "The unrelated README edit should remain unstaged."
  exit 1
fi

empty_output="$(
  cd "$REPO_DIR"
  git reset -q
  bash "$SCRIPT_PATH" xhs_notes/dropbox never_tracked
)"
if ! grep -q "No tracked generated roots are present" <<< "$empty_output"; then
  echo "$empty_output"
  echo "Expected an explicit no-op diagnostic when every root is untracked."
  exit 1
fi

echo "stage_pruned_generated_paths.sh checks passed."
