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


num = str(input("english digit : "))
