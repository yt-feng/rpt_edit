#!/usr/bin/env bash
set -euo pipefail

ROOT_DIR="$(cd "$(dirname "$0")/.." && pwd)"
SCRIPT_PATH="$ROOT_DIR/scripts/push_main_with_rebase_retry.sh"
TEST_ROOT="$(mktemp -d "${TMPDIR:-/tmp}/push-main-rebase-test.XXXXXX")"
REMOTE_DIR="$TEST_ROOT/remote.git"
SEED_DIR="$TEST_ROOT/seed"
CLEANUP_DIR="$TEST_ROOT/cleanup"
CONCURRENT_DIR="$TEST_ROOT/concurrent"

cleanup() {
  rm -rf -- "$TEST_ROOT"
}
trap cleanup EXIT

git init --bare -q "$REMOTE_DIR"
git init -q -b main "$SEED_DIR"
mkdir -p "$SEED_DIR/generated/260730"
printf 'old\n' > "$SEED_DIR/generated/260730/result.txt"
printf 'seed\n' > "$SEED_DIR/README.md"
git -C "$SEED_DIR" add .
git -C "$SEED_DIR" -c user.name=test -c user.email=test@example.com commit -q -m seed
git -C "$SEED_DIR" remote add origin "$REMOTE_DIR"
git -C "$SEED_DIR" push -q -u origin main
git --git-dir="$REMOTE_DIR" symbolic-ref HEAD refs/heads/main

git clone -q "$REMOTE_DIR" "$CLEANUP_DIR"
git clone -q "$REMOTE_DIR" "$CONCURRENT_DIR"

rm -rf -- "$CLEANUP_DIR/generated/260730"
git -C "$CLEANUP_DIR" add -A generated
git -C "$CLEANUP_DIR" -c user.name=test -c user.email=test@example.com commit -q -m cleanup

printf 'concurrent\n' > "$CONCURRENT_DIR/concurrent.txt"
git -C "$CONCURRENT_DIR" add concurrent.txt
git -C "$CONCURRENT_DIR" -c user.name=test -c user.email=test@example.com commit -q -m concurrent
git -C "$CONCURRENT_DIR" push -q origin HEAD:main

(
  cd "$CLEANUP_DIR"
  bash "$SCRIPT_PATH" 3
)

remote_paths="$(git --git-dir="$REMOTE_DIR" ls-tree -r --name-only main | sort)"
if ! grep -q '^concurrent.txt$' <<< "$remote_paths"; then
  echo "The concurrent main update was lost."
  exit 1
fi
if grep -q '^generated/260730/result.txt$' <<< "$remote_paths"; then
  echo "The cleanup deletion did not reach main."
  exit 1
fi

set +e
invalid_output="$(bash "$SCRIPT_PATH" 0 2>&1)"
invalid_status=$?
set -e
if [ "$invalid_status" -ne 2 ] || ! grep -q "positive integer" <<< "$invalid_output"; then
  echo "$invalid_output"
  echo "Invalid retry counts must fail with exit 2."
  exit 1
fi

echo "push_main_with_rebase_retry.sh checks passed."
