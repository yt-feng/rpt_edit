#!/usr/bin/env bash
set -euo pipefail

: "${PORTAL_PRIVATE_ASSET_KEY:?PORTAL_PRIVATE_ASSET_KEY is required}"
: "${PORTAL_PRIVATE_PUBLISH_ASSET_KEY:?PORTAL_PRIVATE_PUBLISH_ASSET_KEY is required}"

workspace="$(pwd -P)"
site_root="${1:-portal_suite/site_src}"
if [[ "$site_root" != /* ]]; then
  site_root="$workspace/$site_root"
fi
site_root="$(cd "$site_root" && pwd -P)"
case "$site_root/" in
  "$workspace/"*) ;;
  *)
    echo "asset target must stay inside the repository" >&2
    exit 2
    ;;
esac

ciphertext="$workspace/portal_suite/private_assets/contact-card.jpg.enc"
brand_ciphertext="$workspace/portal_suite/private_assets/app-mark.svg.enc"
target="$site_root/assets/contact-card.jpg"
brand_target="$site_root/assets/app-mark.svg"
if [[ ! -f "$ciphertext" ]]; then
  echo "encrypted asset bundle is missing" >&2
  exit 2
fi
if [[ ! -f "$brand_ciphertext" ]]; then
  echo "encrypted brand asset bundle is missing" >&2
  exit 2
fi

temporary="$(mktemp "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/portal-private-asset.XXXXXX")"
brand_temporary="$(mktemp "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/portal-private-brand.XXXXXX")"
trap 'rm -f "$temporary" "$brand_temporary"' EXIT
umask 077

openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 \
  -in "$ciphertext" \
  -out "$temporary" \
  -pass env:PORTAL_PRIVATE_ASSET_KEY
openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 \
  -in "$brand_ciphertext" \
  -out "$brand_temporary" \
  -pass env:PORTAL_PRIVATE_PUBLISH_ASSET_KEY

magic="$(LC_ALL=C od -An -tx1 -N3 "$temporary" | tr -d ' \n')"
if [[ "$magic" != "ffd8ff" ]]; then
  echo "decrypted asset failed validation" >&2
  exit 2
fi
if [[ "$(LC_ALL=C head -c 4 "$brand_temporary")" != "<svg" ]]; then
  echo "decrypted brand asset failed validation" >&2
  exit 2
fi

mkdir -p "$(dirname "$target")"
install -m 0600 "$temporary" "$target"
install -m 0600 "$brand_temporary" "$brand_target"
echo "private deployment assets materialized"
