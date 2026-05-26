# KC Desk Notes Password Rules

`password_rules.json` is the repo-side password group table used by KC Desk Notes.

The Worker validates a password by computing:

```text
sha256(PASSWORD_SECRET + ':' + plain_password)
```

Then it compares the result with the `password_sha256` value for the report's assigned password group. `PASSWORD_SECRET` should be configured as a GitHub Actions secret and is forwarded to the Cloudflare Worker during deployment.

The repo can keep `REPLACE_WITH_SHA256_HASH` in `password_rules.json`. During the KC Desk Notes Pages workflow, `scripts/build_kc_desk_notes_site.py` automatically replaces the placeholder in the Pages artifact when both GitHub Actions secrets are present:

```text
PASSWORD_SECRET
KC_DESK_DOWNLOAD_PASSWORD
```

The plain download password should not be committed to this repo unless the repo and Pages setup are intentionally treated as non-sensitive.

The Worker also accepts a deterministic per-report pseudo-password, so a separate password table is not required for normal use:

```text
KC-<first 8 chars of report id>-<last 4 chars of report id>
```

For report id `ff028dc03bb041a90f516174`, the pseudo-password is `KC-ff028dc0-6174`.

Generate a hash locally with:

```bash
python scripts/hash_kc_desk_notes_password.py --secret "$PASSWORD_SECRET" --password "your password"
```

Assignment rules are matched top to bottom. The first rule whose `date_folder`, `bank_code`, and optional `title_contains` match a report assigns that report's `password_group`.
