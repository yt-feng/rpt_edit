# KC Desk Notes Password Rules

`password_rules.json` is the repo-side password group table used by KC Desk Notes.

The Worker validates a password by computing:

```text
sha256(PASSWORD_SECRET + ':' + plain_password)
```

Then it compares the result with the `password_sha256` value for the report's assigned password group. `PASSWORD_SECRET` should be configured as a Cloudflare Worker secret. The plain password should not be placed in this repo unless the repo and Pages setup are intentionally treated as non-sensitive.

Generate a hash locally with:

```bash
python scripts/hash_kc_desk_notes_password.py --secret "$PASSWORD_SECRET" --password "your password"
```

Assignment rules are matched top to bottom. The first rule whose `date_folder`, `bank_code`, and optional `title_contains` match a report assigns that report's `password_group`.
