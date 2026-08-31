import assert from "node:assert/strict";
import { readFile } from "node:fs/promises";
import test from "node:test";

const stylesPath = new URL("../site_src/assets/styles.css", import.meta.url);
const appPath = new URL("../site_src/assets/app.js", import.meta.url);
const responsiveMarker = "/* Account admin responsive workspace */";
const darkMarker = "/* Automatic device dark mode */";

const [styles, app] = await Promise.all([
  readFile(stylesPath, "utf8"),
  readFile(appPath, "utf8"),
]);

const responsiveStart = styles.indexOf(responsiveMarker);
const darkStart = styles.indexOf(darkMarker, responsiveStart);
assert.notEqual(responsiveStart, -1, "responsive admin marker should exist");
assert.notEqual(darkStart, -1, "responsive rules should precede dark overrides");
const responsive = styles.slice(responsiveStart, darkStart);

function mediaSection(source, query) {
  const start = source.indexOf(query);
  assert.notEqual(start, -1, `missing ${query}`);
  let depth = 0;
  let opened = false;
  for (let index = start; index < source.length; index += 1) {
    if (source[index] === "{") {
      depth += 1;
      opened = true;
    } else if (source[index] === "}") {
      depth -= 1;
      if (opened && depth === 0) return source.slice(start, index + 1);
    }
  }
  assert.fail(`unclosed ${query}`);
}

test("desktop admin workspace is wide enough for the user table and editor", () => {
  assert.match(responsive, /\.account-admin-dialog\s*\{[\s\S]*?width:\s*min\(1480px,\s*calc\(100vw - 32px\)\)/u);
  assert.match(responsive, /max-height:\s*min\(92dvh,\s*1040px\)/u);
  assert.match(responsive, /#accountAdminUsersSection \.account-admin-table\s*\{[\s\S]*?min-width:\s*1120px/u);

  const wide = mediaSection(responsive, "@media (min-width: 1180px)");
  assert.match(wide, /#accountAdminUserEditor \.account-admin-form-grid\s*\{[\s\S]*?grid-template-columns:\s*repeat\(3,/u);
  assert.match(wide, /#accountAdminUserEditor \.account-admin-access-field\s*\{[\s\S]*?grid-column:\s*span 2/u);

  const desktop = mediaSection(responsive, "@media (min-width: 821px)");
  assert.match(desktop, /\.account-admin-row-actions\s*\{[\s\S]*?flex-wrap:\s*nowrap/u);
});

test("mobile admin modal becomes a full-height touch workspace", () => {
  const mobile = mediaSection(responsive, "@media (max-width: 820px)");
  assert.match(mobile, /\.account-admin-modal\s*\{[\s\S]*?place-items:\s*stretch;[\s\S]*?padding:\s*0/u);
  assert.match(mobile, /\.account-admin-dialog\s*\{[\s\S]*?min-height:\s*100dvh;[\s\S]*?max-height:\s*100dvh/u);
  assert.match(mobile, /\.account-admin-dialog > \.admin-close\s*\{[\s\S]*?position:\s*fixed/u);
  assert.match(mobile, /\.account-admin-top\s*\{[\s\S]*?position:\s*sticky;[\s\S]*?background:\s*var\(--panel\)/u);
  assert.match(mobile, /\.account-admin-user-editor-actions\s*\{[\s\S]*?position:\s*sticky;[\s\S]*?bottom:\s*0/u);
  assert.match(mobile, /\.account-admin-user-editor-actions \.primary\s*\{[\s\S]*?width:\s*100%/u);
});

test("mobile user table is a labeled card list with touch-sized actions", () => {
  const mobile = mediaSection(responsive, "@media (max-width: 820px)");
  assert.match(mobile, /#accountAdminUsersSection \.account-admin-table-wrap\s*\{[\s\S]*?overflow:\s*visible/u);
  assert.match(mobile, /#accountAdminUsersSection \.account-admin-table thead\s*\{[\s\S]*?clip-path:\s*inset\(50%\)/u);
  assert.match(mobile, /#accountAdminUsersSection \.account-admin-table tbody\s*\{[\s\S]*?display:\s*grid;[\s\S]*?gap:\s*12px/u);
  assert.match(mobile, /#accountAdminUsersSection \.account-admin-table tr\s*\{[\s\S]*?border-radius:\s*12px/u);
  assert.match(mobile, /\.account-admin-row-actions\s*\{[\s\S]*?repeat\(auto-fit,\s*minmax\(110px,\s*1fr\)\)/u);
  assert.match(mobile, /\.account-admin-row-actions \.secondary-button\s*\{[\s\S]*?min-height:\s*44px/u);
  assert.match(mobile, /td\[colspan\]:last-child::before\s*\{[\s\S]*?content:\s*none/u);
  assert.match(mobile, /td:last-child:empty\s*\{[\s\S]*?display:\s*none/u);
});

test("mobile labels stay aligned with the 11-column user DOM contract", () => {
  const modalStart = app.indexOf('id="accountAdminUsersSection"');
  const tableStart = app.indexOf('<table class="account-admin-table">', modalStart);
  const tableEnd = app.indexOf("</table>", tableStart);
  const headers = [...app.slice(tableStart, tableEnd).matchAll(/<th>([^<]+)<\/th>/gu)]
    .map((match) => match[1].trim());
  assert.deepEqual(headers, [
    "用户名",
    "邮箱",
    "注册站点",
    "状态",
    "账号",
    "实际下载权限",
    "到期",
    "权限来源",
    "注册",
    "最近登录",
    "操作",
  ]);

  const mobile = mediaSection(responsive, "@media (max-width: 820px)");
  const labels = [...mobile.matchAll(/td:nth-child\((\d+)\)::before\s*\{\s*content:\s*"([^"]+)";/gu)]
    .sort((left, right) => Number(left[1]) - Number(right[1]))
    .map((match) => match[2]);
  assert.deepEqual(labels, headers);

  const rowStart = app.indexOf("function adminUserRow(user)");
  const rowEnd = app.indexOf("function adminUserSortTimestamp", rowStart);
  assert.equal((app.slice(rowStart, rowEnd).match(/<td/gu) || []).length, 11);
});

test("responsive cards preserve disabled-user treatment in dark mode", () => {
  const combinedDark = mediaSection(styles, "@media (prefers-color-scheme: dark) and (max-width: 820px)");
  assert.match(combinedDark, /tr\.is-disabled-user\s*\{[\s\S]*?background:\s*var\(--dark-danger-bg\)/u);
  assert.match(combinedDark, /tr\.is-disabled-user td\s*\{[\s\S]*?background:\s*transparent/u);
});

test("secondary admin list dialogs are responsive, scroll-safe, and dark-mode ready", () => {
  for (const className of [
    "account-admin-more-button",
    "account-admin-list-modal",
    "account-admin-list-dialog",
    "account-admin-list-top",
    "account-admin-list-status",
    "account-admin-list-body",
  ]) {
    assert.ok(app.includes(className), `admin DOM should expose ${className}`);
    assert.ok(styles.includes(`.${className}`), `styles should cover ${className}`);
  }

  assert.match(responsive, /\.account-admin-list-dialog\s*\{[\s\S]*?grid-template-rows:\s*auto auto minmax\(0, 1fr\)/u);
  assert.match(responsive, /\.account-admin-list-dialog\s*\{[\s\S]*?width:\s*min\(980px,/u);
  assert.match(responsive, /\.account-admin-list-body\s*\{[\s\S]*?overflow-x:\s*hidden;[\s\S]*?overflow-y:\s*auto/u);

  const mobile = mediaSection(responsive, "@media (max-width: 820px)");
  assert.match(mobile, /\.account-admin-more-button\s*\{[\s\S]*?min-height:\s*44px/u);
  assert.match(mobile, /\.account-admin-list-dialog\s*\{[\s\S]*?min-height:\s*calc\(100dvh - 16px\);[\s\S]*?max-height:\s*calc\(100dvh - 16px\)/u);
  assert.match(mobile, /\.account-admin-list-body\.account-admin-files \.account-admin-file\s*\{[\s\S]*?grid-template-columns:\s*1fr/u);

  const automaticDark = styles.slice(darkStart);
  assert.match(automaticDark, /\.account-admin-list-dialog\s*\{[\s\S]*?background:\s*var\(--panel\)/u);
  assert.match(automaticDark, /\.account-admin-list-status\s*\{[\s\S]*?color:\s*var\(--muted\)/u);
});
