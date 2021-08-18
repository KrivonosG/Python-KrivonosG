# 4. Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]


def gen_aux(prev, it):
    for x in it:
        if prev < x:
            yield x
        prev = x


def gen(it):
    return gen_aux(1000, it)


def fun(arg):
    return [number for i, number in enumerate(arg) if i > 0 and arg[i] > arg[i - 1]]


print(fun(src))
print(fun([1, 2, 3, 4, 5, 6]))
print(fun([234, 234234, 2, 1, 222, 34]))
print(list(gen(src)))
