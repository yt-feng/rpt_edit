#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_PATH="$ROOT_DIR/scripts/commit_output_dir.sh"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/kcdesk-commit-output-test.XXXXXX")"
REMOTE_DIR="$TEST_ROOT/remote.git"
REPO_DIR="$TEST_ROOT/repo"

cleanup() {
  rm -rf -- "$TEST_ROOT"
}
trap cleanup EXIT

git init --bare -q "$REMOTE_DIR"
git init -q -b main "$REPO_DIR"
mkdir -p "$REPO_DIR/generated output"
printf 'seed\n' > "$REPO_DIR/generated output/result.txt"
git -C "$REPO_DIR" add "generated output"
git -C "$REPO_DIR" -c user.name=test -c user.email=test@example.com commit -q -m seed
git -C "$REPO_DIR" remote add origin "$REMOTE_DIR"
git -C "$REPO_DIR" push -q -u origin main

printf '0123456789abcdef\n' > "$REPO_DIR/generated output/result.txt"
set +e
output="$({
  cd "$REPO_DIR" || exit 99
  GITHUB_MAX_FILE_BYTES=8 bash "$SCRIPT_PATH" "generated output" "oversized fixture" 1 true
} 2>&1)"
status=$?
set -e

if [ "$status" -ne 3 ]; then
  echo "$output"
  echo "Expected oversized staged content to stop with exit 3; got $status."
  exit 1
fi
if ! grep -q "exceeds GitHub's 8-byte limit" <<< "$output"; then
  echo "$output"
  echo "Expected the oversized-file diagnostic."
  exit 1
fi
if [ "$(git -C "$REPO_DIR" rev-list --count HEAD)" -ne 1 ]; then
  echo "The fail-fast check must run before creating a commit."
  exit 1
fi

set +e
invalid_output="$(GITHUB_MAX_FILE_BYTES=not-a-number bash "$SCRIPT_PATH" "generated output" 2>&1)"
invalid_status=$?
set -e
if [ "$invalid_status" -ne 2 ] || ! grep -q "must be a positive integer" <<< "$invalid_output"; then
  echo "$invalid_output"
  echo "Invalid size limits must fail with a configuration error."
  exit 1
fi

echo "commit_output_dir.sh size-limit checks passed."
