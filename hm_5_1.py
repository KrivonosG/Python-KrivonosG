def odd_generator(n):
    for x in range(1, n + 1, 2):
        yield x


g = odd_generator(15)
print(next(g))
print(next(g))
print(list(odd_generator(15)))

