#!/usr/bin/env bash
# Run only on Linux Actions runners. Keep root-owned apt children within the
# timeout process group so a slow optional install cannot hold the next step's
# dpkg lock. The caller must allow at least 8 minutes for the 390-second budget.
set -euo pipefail

if [[ "${GITHUB_ACTIONS:-}" != true || "${RUNNER_OS:-}" != Linux ]]; then
  echo "::error::APT dependency setup is restricted to Linux GitHub Actions runners."
  exit 2
fi
if (( $# == 0 )); then
  echo "::error::Specify at least one APT package."
  exit 2
fi
for package in "$@"; do
  if [[ ! "$package" =~ ^[a-z0-9][a-z0-9+.-]*$ ]]; then
    echo "::error::Invalid APT package name."
    exit 2
  fi
done

apt_options=(
  -o DPkg::Lock::Timeout=60
  -o Acquire::Retries=2
  -o Acquire::http::Timeout=30
  -o Acquire::https::Timeout=30
)

run_apt() {
  local budget="$1"
  shift
  local status=0
  # timeout must run INSIDE sudo, without --foreground: it needs permission to
  # signal apt and its root-owned children, including the hard-kill fallback.
  sudo timeout --signal=TERM --kill-after=15s "$budget" \
    env DEBIAN_FRONTEND=noninteractive apt-get "${apt_options[@]}" "$@" || status=$?
  if (( status != 0 )); then
    echo "::error::Bounded APT dependency setup failed (exit $status)."
    return "$status"
  fi
}

# Do not install against partially refreshed indices or retry interrupted dpkg
# transactions. Optional callers can continue only after this helper has exited.
run_apt 120s -o APT::Update::Error-Mode=any update
run_apt 240s install -y --no-install-recommends "$@"
