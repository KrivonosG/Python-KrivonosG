from itertools import zip_longest
import types

tutors = [
    'Иван', 'Анастасия', 'Петр', 'Сергей',
    'Дмитрий', 'Борис', 'Елена', 'Патрикей', 'Евлампий'
]
klasses = [
    '9А', '7В', '9Б', '9В', '8Б', '10А', '10Б', '9А'
]


def generate_a_pair(a, b):
    for k in zip_longest(a, b):
        yield k


print("Is it a generator ?", isinstance(generate_a_pair([], []), types.GeneratorType))
print(list(generate_a_pair(tutors, klasses)))
