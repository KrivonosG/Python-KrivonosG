contacts = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]


def thesaurus_adv(names):
    res = {}
    for name in names:
        key1 = name[0].capitalize()
        key2 = name.split(' ')[1][0].capitalize()
        if key2 not in res:
            res[key2] = {}
        if key1 not in res[key2]:
            res[key2][key1] = []
        res[key2][key1].append(name)
    return res


