def num_translate(num):
    try:
        nums = {'zero': 'ноль',
                'one': 'один',
                'two': 'два',
                'three': 'три',
                'four': 'четыре',
                'five': 'пять',
                'six': 'шесть',
                'seven': 'семь',
                'eight': 'восемь',
                'nine': 'девять',
                'ten': 'десять'}
        return nums[num]

    except KeyError:
        return None


def num_translate_adv(w):
    cap = str(w[0]).isupper()
    res = num_translate(w.lower())
    if cap and res is not None:
        res = res.capitalize()
    return res


num = str(input("english digit : "))
