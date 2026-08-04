#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -eq 0 ]; then
  echo "Usage: $0 <generated-root> [<generated-root> ...]" >&2
  exit 2
fi

tracked_roots=()
for root in "$@"; do
  if git ls-files --error-unmatch -- "$root" >/dev/null 2>&1; then
    tracked_roots+=("$root")
  else
    echo "Skip generated root with no tracked entries: $root"
  fi
done

if [ "${#tracked_roots[@]}" -eq 0 ]; then
  echo "No tracked generated roots are present."
  exit 0
fi

git add -A -- "${tracked_roots[@]}"
printf 'Staged tracked generated roots:'
printf ' %s' "${tracked_roots[@]}"
printf '\n'
