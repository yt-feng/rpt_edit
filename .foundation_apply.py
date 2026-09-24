"""One-use, bounded source patch for additional-language foundation only.
No R2 module, credentials, upload code, or production activation is included.
"""
import hashlib
import json
from pathlib import Path
import pprint
import re

EXPECTED = {
    '.github/actions/setup-offline-translation/action.yml': '0cb934286a52b633f4534d47e81843f428c90ab8',
    'scripts/assemble_portal_extended_locales.py': '0d3119b5f2e1e7732d3b370d355c4bf284551d2b',
    'scripts/build_portal_extended_locales.py': '3db12638bde316d782615d755d0ebfe1ecec46ec',
    'scripts/collect_portal_extended_sources.py': 'e051847079b534c4a5f33c7f3b85944a45a6411b',
    'scripts/compare_hymt_translation.py': '91bdf333d1869666f05538d8d2781e82e7919c9a',
    'scripts/hymt_offline_translation.py': '56c2c5e0b1a3d008250d00b24d793190be702bfa',
    'scripts/portal_extended_locales.py': '930d0676f1445155547c0746bea4c2bf84349482',
    'workers/edge-static-host/src/index.js': '5a8e88041c7ee28d1f36dfb0567a0e4d1dcd9688',
}
planned = {}
for name, expected in EXPECTED.items():
    raw = Path(name).read_bytes()
    actual = hashlib.sha1(f'blob {len(raw)}\0'.encode() + raw).hexdigest()
    if actual != expected:
        raise ValueError(f'Unexpected base blob: {name}; reconcile instead of overwriting')
    planned[name] = raw.decode()

def replace(name, before, after):
    if planned[name].count(before) != 1:
        raise ValueError(f'Ambiguous patch anchor: {name}')
    planned[name] = planned[name].replace(before, after, 1)

languages = json.loads(Path('scripts/portal_extended_language_inventory.json').read_text())
if len(languages) != 38 or not {'zh', 'en', 'ko', 'ja', 'ar', 'zh-Hant'} <= languages.keys():
    raise ValueError('Unexpected offline inventory')
latin = r'[A-Za-z\u00c0-\u024f\u1e00-\u1eff]'
patterns = dict.fromkeys(languages, latin)
for codes, pattern in (
    ('zh zh-Hant yue', r'[\u3400-\u9fff]'),
    ('ja', r'[\u3040-\u30ff\u3400-\u9fff]'),
    ('ko', r'[\uac00-\ud7af]'),
    ('ar fa ur ug', r'[\u0620-\u064a\u066e-\u06d3\u06fa-\u06fc]'),
    ('ru uk kk mn', r'[\u0400-\u052f]'),
    ('hi mr', r'[\u0900-\u097f]'),
    ('th', r'[\u0e01-\u0e5b]'), ('km', r'[\u1780-\u17ff]'),
    ('my', r'[\u1000-\u109f\uaa60-\uaa7f]'), ('gu', r'[\u0a80-\u0aff]'),
    ('te', r'[\u0c00-\u0c7f]'), ('he', r'[\u05d0-\u05ea]'),
    ('bn', r'[\u0980-\u09ff]'), ('ta', r'[\u0b80-\u0bff]'), ('bo', r'[\u0f00-\u0fff]'),
):
    for code in codes.split(): patterns[code] = pattern
name = 'scripts/compare_hymt_translation.py'
start = planned[name].index('LANGUAGES = '); end = planned[name].index('\n\ndef require_actions', start)
replacement = ('# Official model inventory; unsupported targets fail closed.\n'
               '# https://huggingface.co/tencent/Hy-MT2-1.8B-GGUF\n'
               'LANGUAGES = ' + pprint.pformat(languages, sort_dicts=False) + '\n'
               'SCRIPT_PATTERNS = ' + pprint.pformat(patterns, sort_dicts=False) + '\n'
               "# Preserve established gates for existing production callers.\n"
               "SCRIPT_PATTERNS.update({'en': r'[A-Za-z]', 'ar': r'[\\u0600-\\u06ff]'})\n")
planned[name] = planned[name][:start] + replacement + planned[name][end:]
name = 'scripts/hymt_offline_translation.py'
replace(name, 'LANGUAGES, request_json, require_actions', 'LANGUAGES, SCRIPT_PATTERNS, request_json, require_actions')
replace(name, "_LETTERS = re.compile(r'[A-Za-z\\u3400-\\u9fff\\u3040-\\u30ff\\uac00-\\ud7af\\u0600-\\u06ff]')", "_LETTERS = re.compile(r'[^\\W\\d_]', re.UNICODE)")
replace(name, '''    code = str(language).lower().replace('_', '-').split('-')[0]
    code = {'jp': 'ja', 'kr': 'ko', 'cn': 'zh'}.get(code, code)''', '''    value = str(language).strip().lower().replace('_', '-')
    # Traditional Chinese must retain a distinct target/cache namespace.
    if value in {'zh-hant', 'zh-tw', 'zh-hk', 'zh-mo'} or value.startswith('zh-hant-'):
        return 'zh-Hant'
    code = value.split('-')[0]
    code = {'jp': 'ja', 'kr': 'ko', 'cn': 'zh', 'fil': 'tl'}.get(code, code)''')
start = planned[name].index("        scripts = {'zh':")
end = planned[name].index("            raise OfflineTranslationValidationError('Hy-MT2 target script missing')", start)
planned[name] = planned[name][:start] + '        if target not in SCRIPT_PATTERNS or not re.search(SCRIPT_PATTERNS[target], clean):\n' + planned[name][end:]
name = '.github/actions/setup-offline-translation/action.yml'
replace(name, '  audit-suffix:\n', "  persist-audit:\n    description: Store the small public model receipt as an Actions artifact\n    default: 'true'\n  audit-suffix:\n")
start=planned[name].index('        if [[ ! "$TRANSLATION_TARGETS"')
end=planned[name].index("        manifest = json.loads(Path('scripts/hymt_translation_model_manifest.json')",start)
planned[name]=planned[name][:start]+'''        python - <<'PYCODE'
        import json, os, platform, sys
        from pathlib import Path
        sys.path.insert(0, 'scripts')
        from compare_hymt_translation import LANGUAGES
        targets = os.environ['TRANSLATION_TARGETS'].split(',')
        if not targets or len(targets) != len(set(targets)) or any(code not in LANGUAGES for code in targets):
            raise SystemExit('Unsupported or duplicate translation targets')
'''+planned[name][end:]
replace(name, '        PY\n', '        PYCODE\n')
replace(name, '    - name: Preserve model provenance\n', "    - name: Preserve model provenance\n      if: inputs.persist-audit == 'true'\n")
name = 'scripts/build_portal_extended_locales.py'
replace(name, "CHECKPOINT_VERSION = 'extended-static-v1'", "CHECKPOINT_VERSION = 'extended-static-v2'\n\n\ndef reject_symlinks(path: Path) -> None:\n    if any(item.is_symlink() for item in (path, *path.parents)):\n        raise ExpansionError('Symlink paths are forbidden for locale candidates/checkpoints')")
replace(name, "    if locale == 'en' and source_is_english: return", "    same_language = locale == 'en' and source_is_english")
replace(name, '    if source_key and source_key in translated_key and len(clean) > 12:', '    if not same_language and source_key and source_key in translated_key and len(clean) > 12:')
replace(name, '        self.path, self.locale, self.translator, self.deadline = path, locale, translator, deadline', '        reject_symlinks(path)\n        self.path, self.locale, self.translator, self.deadline = path, locale, translator, deadline')
replace(name, '    def save(self):\n        raw =', "    def save(self):\n        reject_symlinks(self.path)\n        reject_symlinks(self.path.with_suffix('.tmp'))\n        raw =")
replace(name, '    docs = validate_corpus(corpus, origin=origin)\n    if output.exists()', "    docs = validate_corpus(corpus, origin=origin)\n    if origin + '/' not in {doc['url'] for doc in docs}:\n        raise ExpansionError('A localized homepage source is required')\n    reject_symlinks(output)\n    reject_symlinks(checkpoint)\n    if output.exists()")
name = 'scripts/portal_extended_locales.py'
replace(name, "self.capture[0] in {'li', 'blockquote'}", "self.capture[0] in {'li', 'blockquote', 'tr'}")
replace(name, '    for doc in docs: validate_document(doc, origin=origin)', "    for doc in docs: validate_document(doc, origin=origin)\n    paths = [file_for_url(doc['url'], origin=origin).as_posix() for doc in docs]\n    if len(set(paths)) != len(paths):\n        raise ExpansionError('Source URLs collide on the same output file')")
name = 'scripts/assemble_portal_extended_locales.py'
replace(name, '    # Fresh per-locale candidates', "    if (root / 'data/extended-locales/assembly.json').exists():\n        raise ExpansionError('Require a fresh inactive tree and the complete approved locale set')\n    # Fresh per-locale candidates")
name = 'scripts/collect_portal_extended_sources.py'
replace(name, "'User-Agent': '" + 'KC' + "desk-public-locale-build/1.0'", "'User-Agent': 'Portal-public-locale-build/1.0'")
replace(name, "    core = [u for u in urls if urlsplit(u).path in {'/', '/about.html', '/reports/', '/blog/'}]", "    urls = sorted(set(urls))\n    core = [ORIGIN + path for path in ('/', '/reports/', '/blog/', '/about.html') if ORIGIN + path in urls]")
replace(name, '        if path.is_symlink(): continue', '        if any(item.is_symlink() for item in (path, *path.parents)): continue')
replace(name, '    docs = [document_from_html(url, by_url[url].read_bytes()) for url in select_urls(sorted(by_url), limit)]', "    docs = []\n    for url in select_urls(sorted(by_url), limit):\n        path = by_url[url]\n        if path.stat().st_size > MAX_DOCUMENT_BYTES:\n            raise ExpansionError('Local source exceeds byte limit')\n        docs.append(document_from_html(url, path.read_bytes()))")
name = 'workers/edge-static-host/src/index.js'
replace(name, '  ko: "ko",\n  ja: "ja",\n  ar: "ar",', json.dumps({code:code for code in languages if code != 'zh'}, indent=2)[2:-2])
replace(name, '''  const match = /^\\/(ko|ja|ar)(?=\\/|$)/.exec(String(pathname || ""));
  if (!match) return { prefix: "", pathname: String(pathname || "") };''', '''  const match = /^\\/([^/]+)(?=\\/|$)/.exec(String(pathname || ""));
  if (!match || !Object.hasOwn(LOCALE_CONTENT_LANGUAGES, match[1])) {
    return { prefix: "", pathname: String(pathname || "") };
  }''')
start=planned[name].index('  const localizedData = ')
end=planned[name].index('  const localized = localePath(contentPath);',start)
planned[name]=planned[name][:start]+'''  const localizedData = /^\\/data\\/i18n\\/([^/]+)(?=\\/|$)/.exec(contentPath);
  if (localizedData && Object.hasOwn(LOCALE_CONTENT_LANGUAGES, localizedData[1])) {
    return LOCALE_CONTENT_LANGUAGES[localizedData[1]];
  }
  const localizedSitemap = /^\\/sitemap-(?:extended-)?([A-Za-z-]+)\\.xml$/.exec(contentPath);
  if (localizedSitemap && Object.hasOwn(LOCALE_CONTENT_LANGUAGES, localizedSitemap[1])) {
    return LOCALE_CONTENT_LANGUAGES[localizedSitemap[1]];
  }
'''+planned[name][end:]
# Validate every Python module before writing any target file.
for name, text in planned.items():
    if name.endswith('.py'): compile(text, name, 'exec')
for name, text in planned.items(): Path(name).write_text(text, encoding='utf-8')
print(json.dumps({'patched_files': list(planned), 'deployment_performed': False}))
