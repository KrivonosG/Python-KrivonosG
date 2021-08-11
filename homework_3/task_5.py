def get_jokes(n, flag=True):
    jokes = []
    uniq = {}
    while len(jokes) < n:
        first = choice(nouns)
        second = choice(adverbs)
        third = choice(adjectives)
        if flag:
            if first in uniq or second in uniq or third in uniq:
                continue
            uniq[first] = None
            uniq[second] = None
            uniq[third] = None
        jokes.append(f'{first} {second} {third}')

    return jokes


