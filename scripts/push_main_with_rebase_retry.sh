#!/usr/bin/env bash
set -euo pipefail

max_attempts="${1:-5}"
case "$max_attempts" in
  ''|*[!0-9]*)
    echo "max_attempts must be a positive integer." >&2
    exit 2
    ;;
esac
if [ "$max_attempts" -lt 1 ]; then
  echo "max_attempts must be a positive integer." >&2
  exit 2
fi

stashed_worktree=false

stash_worktree() {
  if [ -n "$(git status --porcelain --untracked-files=all)" ]; then
    echo "Stashing generated workspace changes before rebase."
    git stash push --include-untracked -m "push-main-with-rebase-retry-$attempt"
    stashed_worktree=true
  fi
}

restore_worktree() {
  if [ "$stashed_worktree" = "true" ]; then
    echo "Restoring generated workspace changes after rebase."
    git stash pop --index
    stashed_worktree=false
  fi
}

for attempt in $(seq 1 "$max_attempts"); do
  echo "Push attempt $attempt/$max_attempts to origin/main."
  if git push origin HEAD:main; then
    restore_worktree
    exit 0
  fi

  if [ "$attempt" -eq "$max_attempts" ]; then
    restore_worktree
    echo "Unable to push origin/main after $max_attempts attempts." >&2
    exit 1
  fi

  echo "origin/main advanced; rebasing the cleanup commit before retrying."
  stash_worktree
  git fetch origin main
  git rebase origin/main
  restore_worktree
done
