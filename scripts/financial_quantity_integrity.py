"""Reject changed financial quantities without breaking translation context.

This is a deterministic structural check, not a semantic translation judge.
Amounts are compared at their underlying scale and rates remain distinct from
percentage-point changes. Unsupported written-out quantities fail closed when
their numeric counterpart disappears.
"""
from __future__ import annotations

from collections import Counter
from datetime import date
from decimal import Decimal
import re
import unicodedata


# Keep a complete decimal indivisible. Otherwise a failed suffix match can
# backtrack USD1.2bn into USD1 plus a stray 2, hiding a changed magnitude.
NUMBER = r"(?>[+\-−]?\d+(?:[,٬]\d{3})*(?:[.٫,]\d+)?)"
SCALES = {
    "thousand": 10**3, "million": 10**6, "billion": 10**9, "trillion": 10**12,
    "k": 10**3, "m": 10**6, "b": 10**9, "t": 10**12,
    "mn": 10**6, "mln": 10**6, "mm": 10**6,
    "bn": 10**9, "bln": 10**9, "tn": 10**12, "trn": 10**12,
    "万": 10**4, "万元": 10**4, "十万": 10**5, "百万": 10**6,
    "千万": 10**7, "亿": 10**8, "亿元": 10**8, "十亿": 10**9,
    "百亿": 10**10, "千亿": 10**11, "万亿": 10**12,
    "만": 10**4, "천만": 10**7, "백만": 10**6, "억": 10**8,
    "십억": 10**9, "조": 10**12, "مليون": 10**6, "مليار": 10**9, "ألف": 10**3,
    # Common target-language inflections emitted by Hy-MT2.  Keep the
    # magnitude explicit so a localized unit cannot turn a preserved number
    # into an unscaled plain-number mismatch.
    "milliers": 10**3, "millions": 10**6, "milliard": 10**9, "milliards": 10**9,
    "billions": 10**12,
    "mil": 10**3, "miles": 10**3, "millón": 10**6, "millones": 10**6,
    "millardo": 10**9, "millardos": 10**9, "billón": 10**12, "billones": 10**12,
    "milhares": 10**3, "milhão": 10**6, "milhões": 10**6,
    "bilhão": 10**9, "bilhões": 10**9, "bilião": 10**12, "biliões": 10**12,
    "trilhão": 10**18, "trilhões": 10**18, "trilião": 10**18, "triliões": 10**18,
    "mille": 10**3, "mila": 10**3, "milione": 10**6, "milioni": 10**6,
    "miliardo": 10**9, "miliardi": 10**9, "bilione": 10**12, "bilioni": 10**12,
    "tausend": 10**3, "tausende": 10**3, "millionen": 10**6,
    "millionen": 10**6, "milliarde": 10**9, "milliarden": 10**9,
    "billionen": 10**12, "duizend": 10**3, "duizenden": 10**3,
    "miljoen": 10**6, "miljoenen": 10**6, "miljard": 10**9, "miljarden": 10**9,
    "biljoen": 10**12, "biljoenen": 10**12,
    "tysiąc": 10**3, "tysiące": 10**3, "tysięcy": 10**3,
    "milion": 10**6, "miliony": 10**6, "milionów": 10**6,
    "miliard": 10**9, "miliardy": 10**9, "miliardów": 10**9,
    "bilion": 10**12, "biliony": 10**12, "bilionów": 10**12,
    "tisíc": 10**3, "tisíce": 10**3, "miliony": 10**6, "miliardy": 10**9,
    "bin": 10**3, "milyon": 10**6, "milyar": 10**9, "trilyon": 10**12,
    "nghìn": 10**3, "ngàn": 10**3, "triệu": 10**6, "tỷ": 10**9, "tỉ": 10**9,
    "ribu": 10**3, "juta": 10**6, "miliar": 10**9, "milyar": 10**9, "triliun": 10**12,
    "libo": 10**3, "milyon": 10**6, "bilyon": 10**9, "trilyon": 10**12,
    "тысяча": 10**3, "тысячи": 10**3, "тысяч": 10**3,
    "миллион": 10**6, "миллиона": 10**6, "миллионов": 10**6,
    "миллиард": 10**9, "миллиарда": 10**9, "миллиардов": 10**9,
    "триллион": 10**12, "триллиона": 10**12, "триллионов": 10**12,
    "мільйон": 10**6, "мільйони": 10**6, "мільйонів": 10**6,
    "мільярд": 10**9, "мільярди": 10**9, "мільярдів": 10**9,
    "трильйон": 10**12, "трильйони": 10**12,
    "тыс": 10**3, "тыс.": 10**3, "млн": 10**6, "млрд": 10**9,
    "हज़ार": 10**3, "हजार": 10**3, "लाख": 10**5, "करोड़": 10**7,
    "मिलियन": 10**6, "बिलियन": 10**9, "अरब": 10**9, "ट्रिलियन": 10**12,
    "হাজার": 10**3, "লাখ": 10**5, "কোটি": 10**7, "মিলিয়ন": 10**6, "বিলিয়ন": 10**9,
    "тысяча": 10**3, "мільйон": 10**6,
    "천": 10**3, "백만": 10**6, "백억": 10**10,
    "千": 10**3, "百万": 10**6, "千万": 10**7, "十億": 10**9, "兆": 10**12,
    "พัน": 10**3, "ล้าน": 10**6, "พันล้าน": 10**9, "ล้านล้าน": 10**12,
    "ពាន់": 10**3, "លាន": 10**6, "ពាន់លាន": 10**9,
    "ထောင်": 10**3, "သန်း": 10**6, "ဘီလီယံ": 10**9, "ထရီလီယံ": 10**12,
    "هزار": 10**3, "میلیون": 10**6, "میلیارد": 10**9, "تریلیون": 10**12,
    "אלף": 10**3, "אלפים": 10**3, "מיליון": 10**6, "מיליונים": 10**6,
    "מיליארד": 10**9, "מיליארדים": 10**9, "טריליון": 10**12,
    "மில்லியன்": 10**6, "பில்லியன்": 10**9, "ஆயிரம்": 10**3, "லட்சம்": 10**5, "கோடி": 10**7,
}
SCALE = "(?:" + "|".join(re.escape(value) for value in sorted(SCALES, key=len, reverse=True)) + ")"
CURRENCIES = {
    "USD": ("USD", "US$", "$", "US dollars", "U.S. dollars", "US dollar", "U.S. dollar", "dollars", "dollar", "dólar", "dólares", "dólar americano", "dólares americanos", "dolar", "dolars", "Dollar", "Dollars", "доллар", "доллара", "долларов", "долар", "долари", "доларів", "doları", "dolar", "đô la", "долар أمريكي", "دولار أمريكي", "دولارات", "دولار", "долلار", "डॉलर", "ડોલર", "ডলার", "డాలర్", "டாலர்", "דולר", "دلار", "ドル", "달러", "美元", "美金"),
    "CNY": ("CNY", "RMB", "人民币", "元人民币", "元", "yuan", "yuans", "renminbi", "Chinese yuan", "Chinese renminbi", "人民币元", "위안", "юань", "юаней", "юань", "yuanes", "юанів", "युआन", "रॅन्मिन्बी"),
    "EUR": ("EUR", "€", "euros", "euro", "евро", "euro", "euros", "евро", "еврo", "欧元", "유로", "यूरो"),
    "GBP": ("GBP", "£", "pounds", "pound", "livre", "livres", "libra", "libras", "Pfund", "фунт", "фунтов", "英镑", "पाउंड"),
    "JPY": ("JPY", "日元", "円", "yen", "ienes", "iene", "иен", "иены", "иенов", "엔", "येन"),
    "HKD": ("HKD", "HK$", "港元", "港币", "Hong Kong dollar", "Hong Kong dollars", "доллар Гонконга", "हांगकांग डॉलर"),
}
ALIASES = {alias.casefold(): code for code, aliases in CURRENCIES.items() for alias in aliases}
CURRENCY = "(?:" + "|".join(re.escape(s) for s in sorted(ALIASES, key=len, reverse=True)) + ")"
MONTH_NAMES = "January February March April May June July August September October November December".split()
MONTHS = {name.casefold(): i for i, name in enumerate(MONTH_NAMES, 1)}
MONTHS.update({name[:3].casefold(): i for i, name in enumerate(MONTH_NAMES, 1)})
# Month names commonly emitted in localized dates.  They are aliases of the
# same calendar month, not free-form text accepted by the quantity gate.
MONTHS.update({
    'janvier':1, 'février':2, 'fevrier':2, 'mars':3, 'avril':4, 'mai':5,
    'juin':6, 'juillet':7, 'août':8, 'aout':8, 'septembre':9, 'octobre':10,
    'novembre':11, 'décembre':12, 'decembre':12,
    'janeiro':1, 'fevereiro':2, 'março':3, 'marco':3, 'abril':4, 'maio':5,
    'junho':6, 'julho':7, 'agosto':8, 'setembro':9, 'outubro':10,
    'novembro':11, 'dezembro':12,
    'enero':1, 'febrero':2, 'marzo':3, 'mayo':5, 'junio':6, 'julio':7,
    'septiembre':9, 'setiembre':9, 'diciembre':12,
    'gennaio':1, 'febbraio':2, 'aprile':4, 'maggio':5, 'giugno':6,
    'luglio':7, 'ottobre':10,
    'januar':1, 'februar':2, 'mär':3, 'maerz':3, 'märz':3, 'april':4,
    'juni':6, 'juli':7, 'august':8, 'oktober':10, 'dezember':12,
    'januari':1, 'februari':2, 'maart':3, 'mei':5, 'augustus':8,
    'januari':1,
    'ocak':1, 'şubat':2, 'subat':2, 'nisan':4, 'mayıs':5, 'mayis':5,
    'haziran':6, 'temmuz':7, 'ağustos':8, 'agustos':8, 'eylül':9, 'eylul':9,
    'ekim':10, 'kasım':11, 'kasim':11, 'aralık':12, 'aralik':12,
    'января':1, 'февраля':2, 'марта':3, 'апреля':4, 'мая':5, 'июня':6,
    'июля':7, 'августа':8, 'сентября':9, 'октября':10, 'ноября':11, 'декабря':12,
    'січня':1, 'лютого':2, 'березня':3, 'квітня':4, 'травня':5, 'червня':6,
    'липня':7, 'серпня':8, 'вересня':9, 'жовтня':10, 'листопада':11, 'грудня':12,
    'जनवरी':1, 'फ़रवरी':2, 'फरवरी':2, 'मार्च':3, 'अप्रैल':4, 'मई':5,
    'जून':6, 'जुलाई':7, 'अगस्त':8, 'सितंबर':9, 'सितम्बर':9, 'अक्टूबर':10,
    'नवंबर':11, 'दिसंबर':12,
})
MONTH = "(?:" + "|".join(sorted(MONTHS, key=len, reverse=True)) + r")\.?"
FIVE_YEAR_PERIOD_RE = re.compile(
    r"(?<![A-Za-z0-9])(\d+)(?:st|nd|rd|th)\s+Five[~\s-]+Year(?![A-Za-z0-9])", re.IGNORECASE)


def _normalized(text: str) -> str:
    text = unicodedata.normalize("NFKC", text).replace("−", "-").replace("٬", ",").replace("٫", ".")
    text = "".join(str(unicodedata.decimal(c)) if c.isdecimal() else c for c in text)
    return re.sub(r"__(?:KC_PH|HYMTPH)_\d+__", " ", text)


def _decimal(value: str) -> Decimal:
    value = value.replace("−", "-")
    if "," in value:
        # A sole non-thousands comma is a decimal separator; never use floats.
        if "." not in value and value.count(",") == 1 and len(value.rsplit(",", 1)[1]) != 3:
            value = value.replace(",", ".")
        else:
            value = value.replace(",", "")
    return Decimal(value)


def quantities(text: str) -> Counter:
    text = _normalized(text)
    found = Counter()

    def take(pattern: str, key) -> None:
        nonlocal text
        def consume(match):
            found[key(match)] += 1
            return " " * len(match.group())
        text = re.sub(pattern, consume, text, flags=re.IGNORECASE)

    def day_key(year, month, day):
        try:
            return ("date", date(int(year), int(month), int(day)).isoformat())
        except ValueError:
            return ("invalid_date", str((year, month, day)))

    take(r"(?<!\d)(\d{4})\s*(?:[-/]\s*|年\s*|년\s*)(\d{1,2})\s*(?:[-/]\s*|月\s*|월\s*)(\d{1,2})\s*(?:日|일)?(?!\d)",
         lambda m: day_key(m[1], m[2], m[3]))
    take(rf"\b({MONTH})\s+(\d{{1,2}})(?:st|nd|rd|th)?\s*,?\s*(\d{{4}})\b",
         lambda m: day_key(m[3], MONTHS[m[1].rstrip('.').casefold()], m[2]))
    take(rf"\b(\d{{1,2}})\s+(?:(?:de|del|of)\s+)?({MONTH})(?:\s+(?:de|del|of))?\s*,?\s*(\d{{4}})\b",
         lambda m: day_key(m[3], MONTHS[m[2].rstrip('.').casefold()], m[1]))
    take(rf"\b(\d{{1,2}})\s+({MONTH})\s*,?\s*(\d{{4}})\b",
         lambda m: day_key(m[3], MONTHS[m[2].rstrip('.').casefold()], m[1]))
    take(rf"\b({MONTH})\s+(\d{{4}})\b",
         lambda m: ("month", int(m[2]), MONTHS[m[1].rstrip('.').casefold()]))
    take(rf"\b({MONTH})\s*['’](\d{{2}})\b",
         lambda m: ("month", 2000 + int(m[2]), MONTHS[m[1].rstrip('.').casefold()]))
    take(r"(?<!\d)(\d{4})[-/](\d{1,2})(?![\d/-])",
         lambda m: ("month", int(m[1]), int(m[2])))
    take(r"(?<!\d)(\d{4})\s*(?:年|년)\s*(\d{1,2})\s*(?:月|월)",
         lambda m: ("month", int(m[1]), int(m[2])))
    # Reporting periods use both full and abbreviated years. Only a year
    # explicitly attached to a quarter/half is expanded; ordinary 26 remains 26.
    ordinals = {'一': 1, '二': 2, '三': 3, '四': 4, 'first': 1, 'second': 2, 'third': 3, 'fourth': 4}
    year = r"(?:\d{4}|\d{2})"
    def period_year(value):
        return int(value) + (2000 if len(value) == 2 else 0)
    take(rf"(?<!\d)({year})\s*年\s*第?([一二三四1-4])季度",
         lambda m: ("quarter", period_year(m[1]), ordinals.get(m[2], int(m[2]) if m[2].isdigit() else 0)))
    take(rf"\bQ([1-4])\s*[,'’\-]?\s*({year})\b", lambda m: ("quarter", period_year(m[2]), int(m[1])))
    take(rf"\b({year})\s*Q([1-4])\b", lambda m: ("quarter", period_year(m[1]), int(m[2])))
    take(rf"\b([1-4])Q\s*['’]?\s*({year})\b", lambda m: ("quarter", period_year(m[2]), int(m[1])))
    take(rf"\b(first|second|third|fourth)\s+quarter(?:\s+of)?\s+({year})\b",
         lambda m: ("quarter", period_year(m[2]), ordinals[m[1].casefold()]))
    take(rf"\bH([12])\s*['’]?\s*({year})\b", lambda m: ("half", period_year(m[2]), int(m[1])))
    take(rf"\b({year})\s*H([12])\b", lambda m: ("half", period_year(m[1]), int(m[2])))
    take(rf"\b([12])H\s*['’]?\s*({year})\b", lambda m: ("half", period_year(m[2]), int(m[1])))
    take(rf"\b(first|second)\s+half(?:\s+of)?\s+({year})\b",
         lambda m: ("half", period_year(m[2]), ordinals[m[1].casefold()]))
    take(rf"(?<!\d)({year})\s*年\s*([上下])半年", lambda m: ("half", period_year(m[1]), 1 if m[2] == '上' else 2))
    take(r"\b(?:Q([1-4])|([1-4])Q)\b", lambda m: ("quarter", None, int(m[1] or m[2])))
    take(r"第?([一二三四1-4])季度",
         lambda m: ("quarter", None, ordinals.get(m[1], int(m[1]) if m[1].isdigit() else 0)))
    take(r"\b(first|second|third|fourth)\s+quarter\b", lambda m: ("quarter", None, ordinals[m[1].casefold()]))
    take(r"\b(?:H([12])|([12])H)\b", lambda m: ("half", None, int(m[1] or m[2])))
    take(r"([上下])半年", lambda m: ("half", None, 1 if m[1] == '上' else 2))
    take(r"\b(first|second)\s+half\b", lambda m: ("half", None, ordinals[m[1].casefold()]))

    # A month/day title without a year stays distinct from a dated observation.
    take(rf"\b({MONTH})\s+(\d{{1,2}})(?:st|nd|rd|th)?\b",
         lambda m: ("month_day", MONTHS[m[1].rstrip('.').casefold()], int(m[2])))
    take(r"(?<!\d)(\d{1,2})\s*月\s*(\d{1,2})\s*日",
         lambda m: ("month_day", int(m[1]), int(m[2])))

    # Five-year-plan ordinals translate to 第十五个五年 or “十五五”. Limit
    # this equivalence to plan syntax: ordinary labels such as 第一段 also
    # translate to nonnumeric Korean/Japanese words and are not quantities.
    digits = dict(zip('零〇一二两三四五六七八九', (0, 0, 1, 2, 2, 3, 4, 5, 6, 7, 8, 9)))
    def chinese_ordinal(value):
        if value.isdigit():
            return int(value)
        if not any(char in value for char in '十百千'):
            return int(''.join(str(digits[char]) for char in value))
        total, current = 0, 0
        for char in value:
            if char in digits:
                current = digits[char]
            else:
                total += (current or 1) * {'十': 10, '百': 100, '千': 1000}[char]
                current = 0
        return total + current
    take(FIVE_YEAR_PERIOD_RE.pattern,
         lambda m: ("five_year_plan", int(m[1])))
    take(r"第?(\d+|[零〇一二两三四五六七八九十百千]+)(?:个)?五年",
         lambda m: ("five_year_plan", chinese_ordinal(m[1])))
    take(r"(?<=[“「『\"'])([一二三四五六七八九十]+)五(?=[”」』\"'])",
         lambda m: ("five_year_plan", chinese_ordinal(m[1])))
    take(r"([一二三四五六七八九十]+)五(?=规划|计划|时期|期间)",
         lambda m: ("five_year_plan", chinese_ordinal(m[1])))
    take(r"(?<!\d)(\d+)(?:वीं|वां|वाँ)?\s*पंचवर्षीय",
         lambda m: ("five_year_plan", int(m[1])))

    # Currency recognition comes before scaled plain numbers. Keep the unit
    # separate so USD120m can never match an unqualified 120 or CNY120m.
    def money(m):
        scale = (m['scale'] or '').casefold()
        return ("currency", ALIASES[m['currency'].casefold()], _decimal(m['number']) * SCALES.get(scale, 1))
    # Alphabetic boundaries avoid interpreting the suffix of e.g. "dollars".
    take(rf"(?<![A-Za-z])(?P<currency>{CURRENCY})\s*(?P<number>{NUMBER})\s*(?P<scale>{SCALE})?(?![\dA-Za-z])", money)
    take(rf"(?<![\dA-Za-z])(?P<number>{NUMBER})\s*(?P<scale>{SCALE})?\s*(?:(?:of|de|do|da|dos|das|des|d')\s*)?(?P<currency>{CURRENCY})(?![A-Za-z])", money)
    take(rf"({NUMBER})\s*(?:basis\s+points?|bps\b|基点|基點|points?\s+de\s+base|pontos?[- ]base|puntos?\s+básicos?|punti\s+base|Basispunkte?|procentpunt(?:en)?|punkty\s+procentowe|процентн(?:ых|ых)\s+пункт(?:ов)?|відсотков(?:их|і)\s+пункт(?:ів)?|yüzde\s+puan|điểm\s+cơ\s+bản|pontos?\s+base|आधार\s+अंक|बेसिस\s+पॉइंट्स?)",
         lambda m: ("percentage_points", _decimal(m[1]) / 100))
    take(rf"(?P<number>{NUMBER})\s*(?:percentage\s+points?|percent(?:age)?\s+points?|points?\s+de\s+pourcentage|points?\s+de\s+pourcent|pontos?\s+percentuais?|puntos?\s+porcentuales?|punti\s+percentuali|Prozentpunkte?|procentpunt(?:en)?|punkty\s+procentowe|процентн(?:ых|ых)\s+пункт(?:ов)?|відсотков(?:их|і)\s+пункт(?:ів)?|yüzde\s+puan|điểm\s+phần\s+trăm|个百分点|個百分點|パーセントポイント|퍼센트포인트|نقطة\s+مئوية|نقاط\s+مئوية|प्रतिशत\s+(?:अंक|बिंदु))",
         lambda m: ("percentage_points", _decimal(m['number'])))
    take(rf"(?P<number>{NUMBER})\s*(?:%|٪|percent(?:age)?(?![a-z])|per\s+cent(?![a-z])|pour\s*cent|pourcentage|por\s+ciento|por\s+cento|porcent(?:aje|agem|ual)?|per\s+cento|percentuale|Prozent|procent|procenten|procentowy|процент(?:а|ов)?|відсот(?:ок|ка|ків)?|yüzde|phần\s+trăm|persen|peratus|เปอร์เซ็นต์|ភាគរយ|ရာခိုင်နှုန်း|درصد|אחוז(?:ים)?|प्रतिशत|ટકા|শতাংশ|శాతం|சதவீதம்|パーセント|퍼센트|في\s+المائة|في\s+المئة)",
         lambda m: ("percent", _decimal(m['number'])))
    take(rf"百分之\s*({NUMBER})", lambda m: ("percent", _decimal(m[1])))
    take(rf"(?<![\dA-Za-z])({NUMBER})\s*({SCALE})(?![A-Za-z])",
         lambda m: ("number", _decimal(m[1]) * SCALES[m[2].casefold()]))
    take(NUMBER, lambda m: ("number", _decimal(m[0])))
    return found


def quantity_issues(source: str, translated: str, source_language: str = "", target_language: str = "") -> list[str]:
    before, after = quantities(source), quantities(translated)
    issues = []
    if any(key[0] == 'invalid_date' for key in before.keys() | after.keys()):
        issues.append("invalid_calendar_date")
    if before != after:
        issues.append("financial_quantity_changed_missing_or_added")
    return issues
