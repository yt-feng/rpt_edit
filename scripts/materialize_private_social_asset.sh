#!/usr/bin/env bash
set -euo pipefail

: "${PORTAL_PRIVATE_PUBLISH_ASSET_KEY:?PORTAL_PRIVATE_PUBLISH_ASSET_KEY is required}"

workspace="$(pwd -P)"
prompt_root="${1:-prompts}"
if [[ "$prompt_root" != /* ]]; then
  prompt_root="$workspace/$prompt_root"
fi
prompt_root="$(cd "$prompt_root" && pwd -P)"
case "$prompt_root/" in
  "$workspace/"*) ;;
  *)
    echo "social asset target must stay inside the repository" >&2
    exit 2
    ;;
esac

ciphertext="$workspace/prompts/private_assets/social-card.jpg.enc"
target="$prompt_root/zsxq_img.jpg"
if [[ ! -f "$ciphertext" ]]; then
  echo "encrypted social asset bundle is missing" >&2
  exit 2
fi

temporary="$(mktemp "${RUNNER_TEMP:-${TMPDIR:-/tmp}}/portal-private-social.XXXXXX")"
trap 'rm -f "$temporary"' EXIT
umask 077

openssl enc -d -aes-256-cbc -pbkdf2 -md sha256 \
  -in "$ciphertext" \
  -out "$temporary" \
  -pass env:PORTAL_PRIVATE_PUBLISH_ASSET_KEY

magic="$(LC_ALL=C od -An -tx1 -N3 "$temporary" | tr -d ' \n')"
if [[ "$magic" != "ffd8ff" ]]; then
  echo "decrypted social asset failed validation" >&2
  exit 2
fi

install -m 0600 "$temporary" "$target"
echo "private social asset materialized"
