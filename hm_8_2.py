import re

WSP, QUOTED_STRING, DATE, RAW, NO_DATA = range(5)

RULES = [
    ('\s+', WSP),
    ('-|"-"', NO_DATA),
    ('"([^"]+)"', QUOTED_STRING),
    ('\[([^\]]+)\]', DATE),
    ('([^\s]+)', RAW),
    ]

def parse(line):
    prepared = [(re.compile(regexp), token_type) for regexp, token_type in RULES]
    ll = len(line)
    i = 0
    result = str()
    while i < ll:
        for pattern, token_type in prepared:
            match = pattern.match(line, i)
            if match is None:
                continue
            result += match.group()
            i = match.end()
    return result

parsed = []
with open("nginx_logs.txt") as f:
    for k in f:
        parsed.append(parse(k))

for p in parsed:
    print(p)