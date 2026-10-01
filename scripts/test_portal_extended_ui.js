const { test } = require('node:test');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const path = require('node:path');
const { normalize, selectRows } = require('../portal_suite/locale_assets/extended-locales.js');
const rows = [
  { position: 0, kind: 'blog', date: '2026-09-30', text: 'AI Data Centers to unlock Solid-State Transformation' },
  { position: 1, kind: 'reports', date: '2026-09-29', text: 'Économie et intelligence artificielle' },
  { position: 2, kind: 'blog', date: '', text: '经济分析 制造业' },
];
test('middle-of-title phrases, punctuation, casing and accents', () => {
  assert.equal(selectRows(rows, { query: 'unlock solid' })[0], rows[0]);
  assert.equal(selectRows(rows, { query: 'data centers to unlock solid-state' }).length, 1);
  assert.equal(selectRows(rows, { query: 'economie' })[0], rows[1]);
  assert.equal(selectRows(rows, { query: '经济' })[0], rows[2]);
  assert.equal(selectRows(rows, { query: '<script>bad</script>' }).length, 0);
});
test('type/date filtering and sort, including unknown date exclusion', () => {
  assert.deepEqual(selectRows(rows, { from: '2026-09-30', to: '2026-09-30' }), [rows[0]]);
  assert.deepEqual(selectRows(rows, { kind: 'reports' }), [rows[1]]);
  assert.deepEqual(selectRows(rows, { to: '2026-09-29' }), [rows[1]]);
  assert.equal(selectRows(rows, { sort: 'oldest', from: '2026-09-01' })[0], rows[1]);
  assert.equal(normalize('Solid–State'), 'solid state');
});

test('generated report and external-document links preserve existing locale behavior and source routes', () => {
  const source = fs.readFileSync(path.join(__dirname, '../portal_suite/site_src/assets/app.js'), 'utf8');
  const extract = name => {
    const start = source.indexOf(`  function ${name}(`);
    assert.ok(start >= 0);
    return source.slice(start, source.indexOf('\n  }', start) + 4);
  };
  for (const locale of ['', 'ko/', 'ja/', 'ar/', 'fr/', 'fa/', 'zh-Hant/']) {
    const extended = ['fr/', 'fa/', 'zh-Hant/'].includes(locale);
    const context = {
      URL, document: { body: { dataset: extended ? { extendedUi: 'portal-shared-v1' } : {} } },
      window: { location: { href: `https://kcdesk.com/${locale}` } },
      reportPreviewItem: item => item, publicDocItem: item => item,
    };
    vm.createContext(context);
    vm.runInContext(extract('reportPageUrl')+'\n'+extract('externalPageUrl'), context);
    const expected = extended ? '/' : '/'+locale;
    const report = new URL(context.reportPageUrl('id&1', { preview: { title: 'AI Data Centers', page_count: 22 } }));
    assert.equal(report.pathname, expected+'report.html');
    assert.equal(report.searchParams.get('id'), 'id&1');
    assert.equal(report.searchParams.get('title'), 'AI Data Centers');
    const external = new URL(context.externalPageUrl({ id: 'doc&2', title: 'Public title' }, 'test-token'));
    assert.equal(external.pathname, expected+'doc.html');
    assert.equal(external.searchParams.get('password'), 'test-token');
    assert.equal(external.searchParams.has('title'), false);
  }
});
