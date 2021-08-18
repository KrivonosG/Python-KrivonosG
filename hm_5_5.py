list1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def fun(x):
    return [el for el in x if x.count(el) == 1]


def fun2(x):
    for k in x:
        if x.count(k) == 1:
            yield k


print(fun(list1))
print(fun([1, 56, 1, 78, 7, 9, 78]))
print(list(fun2(list1)))
