"""Conservative, local original-source support for numeric title additions.

This is deliberately a small recognizer, not an inference engine. An unsupported
shape remains unready. Source text never joins the selector's general token bag.
"""
from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
import hashlib
import re

POLICY = 'title-source-claim-v1'
MAX_SOURCE_BYTES = 16 * 1024 * 1024
MAX_SENTENCE = 600
NUMBER = r'[+−-]?\d+(?:,\d{3})*(?:\.\d+)?'
UNIT = (r'(?:percentage\s+points?|basis\s+points?|percent|billion|million|thousand|'
        r'万亿美元|亿美元|万美元|万亿元|亿元|万元|十亿|百万|千万|万亿|'
        r'个百分点|基点|美元|港元|人民币|欧元|日元|亿|万|年|倍|台|辆|片|颗|个|'
        r'bn|bps|bp|mn|mm|k|m|b|%|％|x)(?:\s*(?:USD|dollars?|units?|台|辆|片|颗|个))?')
CURRENCY = r'(?:US\$|HK\$|[$€¥])'
SEPARATOR = r'(?:[–—~～-]|至|到|to)'
# Repeated currency/endpoint units are kept as one opaque atom. This route
# refuses to infer shared currencies/scales, but must still never cut a range
# into one endpoint. Simple 30–40% ranges use the explicit normal parser below.
OPAQUE_RANGE = (
    rf'(?:[+−-]?\s*{CURRENCY}\s*{NUMBER}\s*(?:{UNIT})?\s*{SEPARATOR}\s*'
    rf'[+−-]?\s*{CURRENCY}\s*{NUMBER}\s*(?:{UNIT})?|'
    rf'[+−-]?\s*(?:{CURRENCY})?\s*{NUMBER}\s*{UNIT}\s*{SEPARATOR}\s*'
    rf'[+−-]?\s*(?:{CURRENCY})?\s*{NUMBER}\s*(?:{UNIT})?)')
QUANTITY_RE = re.compile(
    rf'(?<![A-Za-z0-9.+−$€¥(\-])(?:(?P<opaque>{OPAQUE_RANGE})|'
    rf'(?P<open>\()?\s*(?:(?P<prefix_sign>[+−-])\s*)?'
    rf'(?P<currency>US\$|HK\$|[$€¥])?\s*'
    rf'(?P<first>{NUMBER})(?P<range>\s*(?:[–—~～]|(?<=\d)-|至|到|to)\s*{NUMBER})?'
    rf'\s*(?P<unit>{UNIT})?(?P<close>\))?)(?![A-Za-z0-9]|\.\d)', re.I)


def quantities(text):
    # The initial whitespace belongs to layout, not to the numeric atom.
    return list(QUANTITY_RE.finditer(text or ''))


def quantity_key(match):
    """Exact value + range + sign + unit/scale identity; no unit guessing."""
    if match['opaque']:
        return None
    preceding = match.string[:match.start()]
    if ((not match['prefix_sign'] and re.search(r'[+−-]\s*$', preceding))
            or (not match['open'] and re.search(r'\(\s*$', preceding))):
        return None
    try:
        first = Decimal(match['first'].replace(',', '').replace('−', '-'))
        second = None
        if match['range']:
            tail = re.sub(r'^\s*(?:[–—~～-]|至|到|to)\s*', '', match['range'], flags=re.I)
            second = Decimal(tail.replace(',', '').replace('−', '-'))
    except InvalidOperation:
        return None
    if match['prefix_sign']:
        if match['first'].startswith(('+','−','-')):
            return None
        if match['prefix_sign'] in {'−','-'}:
            first = -first
    if bool(match['open']) != bool(match['close']):
        return None
    if match['open']:
        if match['prefix_sign'] or first < 0 or second is not None:
            return None
        first = -first
    unit = re.sub(r'\s+', ' ', match['unit'] or '').lower()
    aliases = {'％': '%', 'percent': '%', 'percentage point': 'pp', 'percentage points': 'pp',
        '基点': 'bp', 'bps': 'bp', 'basis point': 'bp', 'basis points': 'bp', '个百分点': 'pp',
        'billion': 'bn', 'million': 'mn', 'mm': 'mn', 'thousand': 'k', '倍': 'x'}
    unit = aliases.get(unit, unit)
    currency = (match['currency'] or '').upper()
    currency = 'USD' if currency in {'$', 'US$'} else currency
    # Calendar years are accepted only with an explicit year marker. A bare
    # 2027 is not silently treated as a year or a metric amount.
    return (str(first), str(second) if second is not None else None, currency, unit)


def safe_prefix_end(text, end):
    """Retreat before an indivisible number/range/unit instead of changing it."""
    for match in quantities(text):
        if match.start() < end < match.end():
            return match.start()
    return end


def boundary_observation(full, shortened):
    original = [quantity_key(match) for match in quantities(full)]
    current = [quantity_key(match) for match in quantities(shortened)]
    introduced = sum(key not in original for key in current)
    return {'quantity_count_before': len(original), 'quantity_count_after': len(current),
            'removed_whole_quantity_count': sum(key not in current for key in original),
            'introduced_or_changed_quantity_count': introduced,
            'invalid_quantity_count': sum(key is None for key in current),
            'preserves_quantity_atoms': introduced == 0 and all(key is not None for key in current)}


@dataclass(frozen=True)
class SourceContext:
    source_filename: str
    text: str
    sha256: str


def source_context(source_filename, text, *, expected_sha256=None):
    """Call with the same source bytes already authenticated by the producer."""
    if not isinstance(text, str) or not text or not isinstance(source_filename, str) or not source_filename:
        return None
    raw = text.encode('utf-8')
    if len(raw) > MAX_SOURCE_BYTES:
        return None
    digest = hashlib.sha256(raw).hexdigest()
    if expected_sha256 is not None and digest != expected_sha256:
        return None
    return SourceContext(source_filename, text, digest)


METRICS = {
    'revenue': r'营收|营业收入|收入|\brevenues?\b|\bsales\b',
    'profit': r'净利润|盈利|利润|\bprofits?\b|\bearnings\b|\bEPS\b',
    'shipments': r'出货|交付|\bshipments?\b|\bdeliveries\b',
    'capacity': r'产能|\bcapacity\b',
    'demand': r'需求|\bdemand\b',
    'investment': r'资本开支|资本支出|投资|\bcapex\b|\binvestment\b',
    'share': r'份额|\bmarket\s+share\b',
    'price': r'价格|售价|\bprices?\b|\bASP\b',
    'margin': r'利润率|毛利率|\bmargins?\b',
    'users': r'用户|订阅|\busers?\b|\bsubscribers?\b',
    'growth': r'增长|增速|\bgrowth\b|\bgrows?\b',
}
STATE_PATTERNS = {
    'negative': r'不|未|无|否认|否定|错误|\b(?:not|no|never|without|false|wrong|denied|denies|deny|rejected)\b|n[\'’]t\b',
    'up': r'增长|增加|上升|提升|上涨|\b(?:growth|grow\w*|increas\w*|ris\w*)\b',
    'down': r'下滑|下降|减少|下跌|\b(?:declin\w*|decreas\w*|fall\w*|drop\w*)\b',
    'forecast': r'预计|预测|预期|有望|将|\b(?:forecast\w*|expect\w*|project\w*|will|estimate\w*)\b',
    'uncertain': r'可能|或将|或许|潜在|有望|\b(?:may|might|could|would|can|should|potential\w*|possible|possibly|unlikely)\b',
    'conditional': r'若|如果|假设|\b(?:if|unless|assuming|scenario)\b',
    'yoy': r'同比|\byoy\b|\byear[ -]on[ -]year\b',
    'qoq': r'环比|\bqoq\b|\bquarter[ -]on[ -]quarter\b',
}
QUALIFIED_RE = re.compile(r'[≈≃~～<>≤≥]|大约|约|左右|附近|超过|超出|以上|以下|至少|至多|不足|接近|近\d|多达|最高|最低|不超过|不低于|'
    r'\b(?:about|around|approximately|roughly|nearly|almost|over|under|above|below|at\s+least|at\s+most|up\s+to|more\s+than|less\s+than)\b', re.I)
PERIOD_PATTERN = r'(?<![A-Za-z0-9])(?:(?:FY|CY)?\d{2,4}\s*Q[1-4]|(?:Q[1-4]|[1-4]Q)\s*\d{2,4}|FY\s*\d{2,4}|CY\s*\d{2,4}|20\d{2}年?|Q[1-4]|[1-4]Q|H[12])(?![A-Za-z0-9])|第[一二三四1-4]季度'


def periods(text):
    values = set()
    # Calendar and fiscal years stay distinct; quarters and growth bases cannot
    # disappear merely because the older numeric token helper skips FY/Q tokens.
    for match in re.finditer(PERIOD_PATTERN, text, re.I):
        value = re.sub(r'\s+', '', match.group()).lower()
        if value.startswith('第'):
            value = 'q' + str('一二三四'.index(value[1])+1) if value[1] in '一二三四' else 'q'+value[1]
        elif re.fullmatch(r'[1-4]q',value): value='q'+value[0]
        elif value.startswith('cy'): value='year'+value[2:]
        elif re.fullmatch(r'20\d{2}年?',value): value='year'+value.removesuffix('年')
        values.add(value)
    return values
SUBJECT_STOP = set(('the a an and or of for in on at to with from by as is are be this that '
    'research report update outlook global sector industry market markets investor day group '
    'company companies product products solution solutions inc ltd plc corp corporation limited holdings notes note weekly monthly '
    'new more less only review technology technologies ai gpu cpu eps fy cy qoq yoy ms gs ubs '
    'jpm citi db bofa barclays bernstein').split())
AMBIGUOUS_RE = re.compile(r'\b(?:versus|vs|whereas|while|but|compared|respectively|and)\b|相比|分别|而|较|但|与|和|及', re.I)
CONTEXT_CAPITAL_WORDS = set(('the a an in at to by of for revenue revenues sales profit profits earnings '
    'shipments deliveries growth capacity demand investment capex share price prices margins users '
    'subscribers us usd hk hkd eur eps').split())


def categories(text, patterns):
    return {key for key, pattern in patterns.items() if re.search(pattern, text, re.I)}


def literal_subjects(candidate, filename, required_terms):
    body = candidate.split('：', 1)[-1]
    ignored = SUBJECT_STOP | {term.lower() for term in required_terms}
    # Literal overlap only. No model-produced aliases, translations or ticker
    # lookups can create a missing source entity during this recovery.
    tokens = {word.lower() for word in re.findall(r'[A-Za-z][A-Za-z0-9]{2,}', body)} - ignored
    tokens = {word for word in tokens if not categories(word, METRICS) and not categories(word, STATE_PATTERNS)}
    source_words = {word.lower() for word in re.findall(r'[A-Za-z][A-Za-z0-9]{2,}', filename)}
    subjects = sorted(tokens & source_words)
    # Chinese filenames have no safe universal tokenizer: require a complete
    # delimited Chinese name shared literally, rather than arbitrary bigrams.
    for word in re.findall(r'[\u4e00-\u9fff]{2,8}', filename):
        if word in body and not categories(word, METRICS) and not categories(word, STATE_PATTERNS):
            subjects.append(word)
    matches = {word: (literal_match(body, word), literal_match(filename, word)) for word in set(subjects)}
    ordered = sorted((word for word,(title_match,file_match) in matches.items() if title_match and file_match),
        key=lambda word: matches[word][0].start())
    filename_order = sorted(ordered, key=lambda word: matches[word][1].start())
    return ordered if filename_order == ordered else []


def literal_match(text, term):
    return re.search(r'(?<![A-Za-z0-9])' + re.escape(term) + r'(?![A-Za-z0-9])', text, re.I)


def contains_literal(text, term):
    return literal_match(text, term) is not None


def sentences(text):
    # No cross-sentence sliding windows or paragraph concatenation. Decimal dots
    # remain inside a sentence. Markdown tables/lists are intentionally rejected.
    for value in re.split(r'(?<!\d)[.!?](?:\s|$)|[。！？;；\n]+', text):
        value = value.strip()
        if 0 < len(value) <= MAX_SENTENCE and not re.search(r'[|\t]|^[-*#>]', value):
            yield value


def direct_claim(text, atom, subjects, required_terms, metric):
    """Only a direct subject/topic → metric → quantity clause can authorize.

    Prefixes are complete literal token inventories, not co-occurrence tests.
    Unknown prepositions, reporting verbs, customers and additional subjects fail
    closed on both the title and source sides, regardless of capitalization.
    """
    matches = list(re.finditer(METRICS[metric], text, re.I))
    if len(matches) != 1 or matches[0].end() > atom.start():
        return False
    match = matches[0]
    prefix = text[:match.start()].strip()
    prefix = re.sub(r"(?<=[A-Za-z])['’]s\b", '', prefix)
    prefix = re.sub(r'^the\s+', '', prefix, flags=re.I)
    prefix = re.sub(r'\bproducts?\b|产品|的', ' ', prefix, flags=re.I)
    tokens = re.findall(r'[A-Za-z][A-Za-z0-9]*|[\u4e00-\u9fff]+', prefix)
    residue = re.sub(r'[A-Za-z][A-Za-z0-9]*|[\u4e00-\u9fff]+', '', prefix)
    if residue.strip() or [word.lower() for word in tokens] != [*subjects, *(term.lower() for term in required_terms)]:
        return False
    middle = re.sub(PERIOD_PATTERN, ' ', text[match.end():atom.start()], flags=re.I).strip()
    english_relation = (r'(?:(?:is|are|was|were|has|have|had|will|would|may|might|could|can|should|does|do|did|'
        r'not|be|been|being|to|of|at|by|in|for|expected|estimated|forecast|projected|potentially|possibly|'
        r'growth|increase|increases|increased|increasing|grow|grows|grew|growing|rise|rises|rose|rising|'
        r'decline|declines|declined|declining|decrease|decreases|decreased|decreasing|fall|falls|fell|falling|'
        r'drop|drops|dropped|reach|reaches|reached|amounts)\b\s*)*')
    chinese_relation = r'(?:(?:数量|量|在|为|是|达到|达|增至|降至|增长|增加|上升|下降|减少|下滑|预计|预测|预期|可能|将|会|不|未|无|至|到|同比|环比|了)\s*)*'
    if not (re.fullmatch(english_relation, middle, re.I) or re.fullmatch(chinese_relation, middle)):
        return False
    tail = re.sub(PERIOD_PATTERN, ' ', text[atom.end():], flags=re.I)
    for basis in ('yoy','qoq'):
        tail = re.sub(STATE_PATTERNS[basis], ' ', tail, flags=re.I)
    return bool(re.fullmatch(r'(?:(?:in|for|during|of)\b|[\s.。!?！？]|在|于)*', tail, re.I))


def _single_clause_support(candidate, missing_numbers, filename, required_terms, context):
    result = {'context_valid': False, 'missing_numeric_count': len(missing_numbers),
        'candidate_quantity_count': 0, 'subject_anchor_count': 0, 'metric_count': 0,
        'source_sentence_count': 0, 'quantity_matching_sentence_count': 0,
        'subject_matching_sentence_count': 0, 'topic_matching_sentence_count': 0,
        'metric_matching_sentence_count': 0, 'state_matching_sentence_count': 0,
        'period_matching_sentence_count': 0, 'qualified_quantity_sentence_count': 0,
        'candidate_direct_claim': False, 'direct_claim_matching_sentence_count': 0,
        'unambiguous_matching_sentence_count': 0, 'supported_numeric_count': 0,
        'candidate_qualified_quantity': bool(QUALIFIED_RE.search(candidate)),
        'candidate_state_flags': {key: key in categories(candidate, STATE_PATTERNS) for key in STATE_PATTERNS},
        'candidate_period_count': len(periods(candidate)),
        'supported': False, 'policy': POLICY}
    if (not isinstance(context, SourceContext) or context.source_filename != filename
            or not isinstance(context.text, str) or not context.text or len(context.text.encode('utf-8')) > MAX_SOURCE_BYTES
            or hashlib.sha256(context.text.encode('utf-8')).hexdigest() != context.sha256):
        return result
    result['context_valid'] = True
    subjects = literal_subjects(candidate, filename, required_terms)
    metrics = categories(candidate, METRICS)
    # Avoid double-counting the 'profit' substring in 'margin' and growth as the
    # primary metric when it merely qualifies revenue/shipments etc.
    if 'margin' in metrics: metrics.discard('profit')
    if len(metrics) > 1: metrics.discard('growth')
    result.update(subject_anchor_count=len(subjects), metric_count=len(metrics))
    atoms = [(match, quantity_key(match)) for match in quantities(candidate)]
    needed = [(match, key) for match, key in atoms if any(re.search(
        r'(?<![A-Za-z0-9])' + re.escape(number) + r'(?![\d.])', match.group()) for number in missing_numbers)]
    result['candidate_quantity_count'] = len(needed)
    covered = {number for number in missing_numbers if any(re.search(
        r'(?<![A-Za-z0-9])' + re.escape(number) + r'(?![\d.])', match.group()) for match, _ in needed)}
    if (not missing_numbers or covered != set(missing_numbers) or not subjects or len(metrics) != 1
            or not required_terms or not needed or result['candidate_qualified_quantity']):
        return result
    # A numeric amount without an explicit unit cannot be distinguished from an
    # arbitrary index, date or mention. Unsupported formats remain a blocker.
    if any(key is None or not (key[2] or key[3]) or (not key[2] and key[3] in {'bn', 'mn', 'k', 'm', 'b', '亿', '万', '万亿'})
           for _, key in needed):
        return result
    title_body = candidate.split('：',1)[-1]
    title_atoms = quantities(title_body)
    metric = next(iter(metrics))
    result['candidate_direct_claim'] = all(any(quantity_key(atom) == key
        and direct_claim(title_body,atom,subjects,required_terms,metric) for atom in title_atoms) for _,key in needed)
    if not result['candidate_direct_claim']:
        return result
    candidate_states = categories(candidate, STATE_PATTERNS)
    candidate_periods = {key for _, key in atoms if key and key[3] == '年'}
    supported = set()
    for sentence in sentences(context.text):
        result['source_sentence_count'] += 1
        source_matches = quantities(sentence)
        source_atoms = [quantity_key(match) for match in source_matches]
        if any(key is None for key in source_atoms): continue
        matched = {key for _, key in needed if key in source_atoms}
        if not matched: continue
        result['quantity_matching_sentence_count'] += 1
        if QUALIFIED_RE.search(sentence):
            result['qualified_quantity_sentence_count'] += 1
            continue
        if not all(contains_literal(sentence, word) for word in subjects): continue
        result['subject_matching_sentence_count'] += 1
        if not all(contains_literal(sentence, term) for term in required_terms): continue
        result['topic_matching_sentence_count'] += 1
        source_metrics = categories(sentence, METRICS)
        if 'margin' in source_metrics: source_metrics.discard('profit')
        if len(source_metrics) > 1: source_metrics.discard('growth')
        if source_metrics != metrics: continue
        result['metric_matching_sentence_count'] += 1
        if categories(sentence, STATE_PATTERNS) != candidate_states: continue
        if {key for key in source_atoms if key and key[3] == '年'} != candidate_periods: continue
        result['state_matching_sentence_count'] += 1
        if periods(sentence) != periods(candidate): continue
        result['period_matching_sentence_count'] += 1
        # Reject multi-quantity comparisons even when a convenient matching
        # number is present. Dates are separately matched above.
        amounts = {key for key in source_atoms if key and key[3] != '年'}
        candidate_amounts = {key for _, key in atoms if key and key[3] != '年'}
        if AMBIGUOUS_RE.search(sentence) or amounts != candidate_amounts: continue
        allowed_names = set(subjects) | {term.lower() for term in required_terms} | CONTEXT_CAPITAL_WORDS
        proper_words = {word.lower() for word in re.findall(r'\b[A-Z][A-Za-z]{1,}\b', sentence)}
        if proper_words - allowed_names: continue
        if any(sentence.lower().count(word.lower()) != 1 for word in subjects): continue
        result['unambiguous_matching_sentence_count'] += 1
        direct = {key for key in matched if any(quantity_key(atom) == key
            and direct_claim(sentence,atom,subjects,required_terms,metric) for atom in source_matches)}
        if direct != matched: continue
        result['direct_claim_matching_sentence_count'] += 1
        supported |= matched
    result['supported_numeric_count'] = sum(key in supported for _, key in needed)
    result['supported'] = len(supported) == len({key for _, key in needed})
    return result


def contextual_numeric_support(candidate, missing_numbers, filename, required_terms, context):
    """Bind every missing number to its own title clause, never another subject."""
    if not missing_numbers:
        return _single_clause_support(candidate, missing_numbers, filename, required_terms, context)
    atoms = quantities(candidate)
    cuts = [match.start() for match in re.finditer(r'[，,；;。！？!?]', candidate)
            if not any(atom.start() <= match.start() < atom.end() for atom in atoms)]
    parts = []
    start = 0
    for end in [*cuts, len(candidate)]:
        clause = candidate[start:end]
        owned = {number for number in missing_numbers if re.search(
            r'(?<![A-Za-z0-9])' + re.escape(number) + r'(?![\d.])', clause)}
        if owned:
            parts.append((owned, _single_clause_support(clause, owned, filename, required_terms, context)))
        start = end + 1
    if not parts:
        return _single_clause_support(candidate, missing_numbers, filename, required_terms, context)
    combined = dict(parts[0][1])
    count_keys = [key for key in combined if key.endswith('_count') and key != 'missing_numeric_count']
    for key in count_keys:
        combined[key] = sum(row[key] for _, row in parts)
    combined['missing_numeric_count'] = len(missing_numbers)
    combined['candidate_qualified_quantity'] = any(row['candidate_qualified_quantity'] for _,row in parts)
    combined['candidate_state_flags'] = {key:key in categories(candidate,STATE_PATTERNS) for key in STATE_PATTERNS}
    combined['candidate_direct_claim'] = all(row['candidate_direct_claim'] for _,row in parts)
    combined['supported'] = (set().union(*(owned for owned, _ in parts)) == set(missing_numbers)
        and all(row['supported'] for _, row in parts))
    return combined
