"""Bounded, content-free HTML difference evidence; never an acceptance policy."""
from collections import Counter
from difflib import SequenceMatcher
import hashlib
from html.parser import HTMLParser
import json
import re

MAX_HTML_BYTES = 1024 * 1024
MAX_EVENTS = 4000
MAX_DIFFERENCES = 40
MAX_EVENT_SAMPLES = 4


def fingerprint(value):
    raw = value.encode() if isinstance(value, str) else json.dumps(
        value, ensure_ascii=False, separators=(',', ':')).encode()
    return hashlib.sha256(raw).hexdigest()


def safe_name(value):
    return value if re.fullmatch(r'[a-z][a-z0-9:_-]{0,63}', value) else 'unusual-name-' + fingerprint(value)[:16]


def value_facts(value, *, attribute=''):
    if value is None:
        return {'type': 'boolean', 'sha256': fingerprint(None)}
    kind = ('empty' if not value else 'url' if attribute in {'src', 'href', 'data-src'}
            else 'style' if attribute == 'style' else 'decimal' if re.fullmatch(r'\d+(?:\.\d+)?', value)
            else 'text')
    facts = {'type': kind, 'chars': len(value), 'bytes': len(value.encode()), 'sha256': fingerprint(value)}
    if kind == 'style':
        # Property names describe the shape; every value remains hashed.
        facts['property_names'] = [safe_name(part.split(':', 1)[0].strip().lower())
                                   for part in value.split(';') if ':' in part]
    return facts


class Events(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.events = []

    def add(self, row):
        if len(self.events) >= MAX_EVENTS:
            raise ValueError('html_event_bound')
        self.events.append(row)

    def handle_starttag(self, tag, attrs):
        self.add(('start', tag, tuple(attrs)))

    def handle_startendtag(self, tag, attrs):
        self.add(('self_closing', tag, tuple(attrs)))

    def handle_endtag(self, tag):
        self.add(('end', tag))

    def handle_data(self, data):
        self.add(('text', data))

    def handle_comment(self, data):
        self.add(('comment', data))

    def handle_decl(self, data):
        self.add(('declaration', data))

    def handle_pi(self, data):
        self.add(('processing_instruction', data))

    def unknown_decl(self, data):
        self.add(('unknown_declaration', data))


def parse(content):
    if not isinstance(content, str) or len(content.encode()) > MAX_HTML_BYTES:
        raise ValueError('html_byte_bound_or_type')
    parser = Events()
    parser.feed(content)
    parser.close()
    return parser.events


def normalized_events(events):
    # For diagnostics only: sorting retains all duplicate attributes/values.
    # Duplicate-name order may be meaningful and is separately reported.
    return [(row[0], row[1], tuple(sorted(row[2], key=lambda pair: (pair[0], pair[1] or ''))))
            if row[0] in {'start', 'self_closing'} else row for row in events]


def event_facts(row):
    facts = {'type': row[0], 'sha256': fingerprint(row)}
    if row[0] in {'start', 'self_closing', 'end'}:
        facts['tag'] = safe_name(row[1])
        if len(row) == 3:
            facts['attributes'] = [{'name': safe_name(name), **value_facts(value, attribute=name)}
                                   for name, value in row[2]]
    else:
        facts['value'] = value_facts(row[1])
    return facts


def inventory(events):
    tags, attrs, duplicates = Counter(), Counter(), 0
    for row in events:
        if row[0] not in {'start', 'self_closing'}:
            continue
        tags[safe_name(row[1])] += 1
        names = [name for name, _value in row[2]]
        attrs.update(safe_name(name) for name in names)
        duplicates += len(names) - len(set(names))
    return {'event_count': len(events), 'event_sha256': fingerprint(events),
            'tag_counts': dict(sorted(tags.items())), 'attribute_counts': dict(sorted(attrs.items())),
            'duplicate_attribute_count': duplicates}


def compare_html(expected, actual):
    left, right = parse(expected), parse(actual)
    normalized_left, normalized_right = normalized_events(left), normalized_events(right)
    differences = []
    for operation, i, j, a, b in SequenceMatcher(a=normalized_left, b=normalized_right, autojunk=False).get_opcodes():
        if operation == 'equal':
            continue
        differences.append({'operation': operation, 'expected_range': [i, j], 'actual_range': [a, b],
                            'expected_events': [event_facts(row) for row in normalized_left[i:min(j, i + MAX_EVENT_SAMPLES)]],
                            'actual_events': [event_facts(row) for row in normalized_right[a:min(b, a + MAX_EVENT_SAMPLES)]],
                            'samples_truncated': j - i > MAX_EVENT_SAMPLES or b - a > MAX_EVENT_SAMPLES})
    left_text = [row[1] for row in left if row[0] == 'text']
    right_text = [row[1] for row in right if row[0] == 'text']
    left_tags = [(row[0], row[1]) for row in left if row[0] in {'start', 'self_closing', 'end'}]
    right_tags = [(row[0], row[1]) for row in right if row[0] in {'start', 'self_closing', 'end'}]
    return {'diagnostic_only': True, 'acceptance_policy_changed': False,
            'raw_equal': expected == actual,
            'expected': {'bytes': len(expected.encode()), 'sha256': fingerprint(expected), **inventory(left)},
            'actual': {'bytes': len(actual.encode()), 'sha256': fingerprint(actual), **inventory(right)},
            'parsed_events_equal': left == right,
            'attribute_order_normalized_events_equal': normalized_left == normalized_right,
            'all_text_events_equal': left_text == right_text,
            'concatenated_text_equal': ''.join(left_text) == ''.join(right_text),
            'expected_text_sha256': fingerprint(''.join(left_text)),
            'actual_text_sha256': fingerprint(''.join(right_text)),
            'tag_sequence_equal': left_tags == right_tags,
            'difference_count': len(differences), 'differences': differences[:MAX_DIFFERENCES],
            'differences_truncated': len(differences) > MAX_DIFFERENCES}


def article_content_diagnostics(data, source):
    from push_portal_translated_to_wechat_drafts import (
        article_prose_text, wechat_editorial_contract_check, wechat_media_contract_check)
    rows = data.get('news_item') if isinstance(data, dict) else None
    if not isinstance(rows, list) or len(rows) != 3 or any(not isinstance(row, dict) for row in rows):
        return {'diagnostic_only': True, 'error_category': 'live_draft_count_or_shape_mismatch'}
    output = []
    for index, (expected, actual) in enumerate(zip(source['articles'], rows)):
        row = {'index': index}
        try:
            row['content'] = compare_html(expected.get('content'), actual.get('content'))
        except (ValueError, TypeError, UnicodeError):
            row['error_category'] = 'html_diagnostic_bound_or_parse_failure'
        row['non_content_fields'] = {safe_name(key): {'matches': actual.get(key) == value,
                                                     'expected_sha256': fingerprint(value),
                                                     'actual_sha256': fingerprint(actual.get(key))}
                                     for key, value in expected.items() if key != 'content'}
        row['existing_contract_checks'] = {
            'prose_equal': article_prose_text(actual.get('content')) == article_prose_text(expected.get('content')),
            'editorial_matches': wechat_editorial_contract_check(actual, expected)['matches'],
            'media': wechat_media_contract_check(actual, expected),
        }
        output.append(row)
    return {'diagnostic_only': True, 'acceptance_policy_changed': False, 'articles': output}
