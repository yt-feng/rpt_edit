import assert from 'node:assert/strict';
import { readFileSync } from 'node:fs';
import test from 'node:test';
import vm from 'node:vm';
const source = readFileSync(new URL('../src/index.js', import.meta.url), 'utf8');
const inventory = JSON.parse(readFileSync(new URL('../../../scripts/portal_extended_language_inventory.json', import.meta.url), 'utf8'));
const preamble = source.slice(0, source.indexOf('function safeRelativePath('));
const scope = { Response, Headers, URL };
vm.runInNewContext(preamble + '\nthis.api={localePath,contentLanguage,canonicalPath,canonicalPathForResolved};', scope);
for (const code of Object.keys(inventory).filter(code => code !== 'zh')) {
  test(`explicit locale route and Content-Language: ${code}`, () => {
    assert.equal(scope.api.contentLanguage(`/${code}/reports/example.html`), code);
    assert.equal(scope.api.canonicalPath(`/${code}`), `/${code}/`);
    assert.equal(scope.api.canonicalPath(`/${code}/index.html`), `/${code}/`);
    assert.equal(scope.api.contentLanguage(`/sitemap-extended-${code}.xml`), code);
    assert.equal(scope.api.contentLanguage(`/data/i18n/${code}/catalog.json`), code);
  });
}
test('root and unsupported prefix boundaries remain unchanged', () => {
  for (const path of ['/reports/a.html', '/french/a.html', '/france/a.html', '/__proto__/a.html']) {
    assert.equal(scope.api.contentLanguage(path), 'zh-Hans');
  }
  assert.equal(scope.api.canonicalPath('/reports'), '/reports/');
});
