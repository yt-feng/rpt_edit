import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";
import vm from "node:vm";

const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const appSource = await readFile(appPath, "utf8");

function extractFunction(source, name) {
  const marker = `function ${name}(`;
  const start = source.indexOf(marker);
  assert.notEqual(start, -1, `${name} must exist`);
  const bodyStart = source.indexOf("{", source.indexOf(")", start));
  let depth = 0;
  for (let index = bodyStart; index < source.length; index += 1) {
    if (source[index] === "{") depth += 1;
    else if (source[index] === "}") {
      depth -= 1;
      if (depth === 0) return source.slice(start, index + 1);
    }
  }
  throw new Error(`${name} body is incomplete`);
}

test("admin users sort active accounts by recent login or registration and disabled accounts last", () => {
  const context = vm.createContext({ Date, String, Number, Boolean });
  vm.runInContext(`
    ${extractFunction(appSource, "adminUserSortTimestamp")}
    ${extractFunction(appSource, "compareAdminUsers")}
    globalThis.compare = compareAdminUsers;
  `, context);
  const users = [
    { email: "disabled@example.invalid", disabled: true, last_login_at: "2026-08-24T10:00:00Z", created_at: "2026-08-24T10:00:00Z" },
    { email: "old@example.invalid", disabled: false, last_login_at: "2026-06-01T00:00:00Z", created_at: "2026-05-01T00:00:00Z" },
    { email: "new@example.invalid", disabled: false, last_login_at: "", created_at: "2026-08-23T00:00:00Z" },
    { email: "recent@example.invalid", disabled: false, last_login_at: "2026-08-24T00:00:00Z", created_at: "2026-01-01T00:00:00Z" },
  ];
  users.sort(context.compare);
  assert.deepEqual(users.map((user) => user.email), [
    "recent@example.invalid",
    "new@example.invalid",
    "old@example.invalid",
    "disabled@example.invalid",
  ]);
});

test("admin password reset UI selects a user and sends only an explicit confirmation", () => {
  assert.match(appSource, /id="accountAdminPasswordResetEmail"/u);
  assert.match(appSource, /重置为 123456/u);
  const resetRequest = extractFunction(appSource, "resetAdminUserPassword");
  assert.match(resetRequest, /account-admin\/user-password-reset/u);
  assert.match(resetRequest, /JSON\.stringify\(\{ email, confirm_reset: true \}\)/u);
  assert.doesNotMatch(resetRequest, /password\s*:/u);
  assert.match(appSource, /确认把 \$\{email\} 的密码重置为 123456/u);
});
