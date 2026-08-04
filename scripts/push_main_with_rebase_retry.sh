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

for attempt in $(seq 1 "$max_attempts"); do
  echo "Push attempt $attempt/$max_attempts to origin/main."
  if git push origin HEAD:main; then
    exit 0
  fi

  if [ "$attempt" -eq "$max_attempts" ]; then
    echo "Unable to push origin/main after $max_attempts attempts." >&2
    exit 1
  fi

  echo "origin/main advanced; rebasing the cleanup commit before retrying."
  git fetch origin main
  git rebase origin/main
done
