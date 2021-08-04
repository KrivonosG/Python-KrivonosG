def sum_of_digits(num):
    s = 0
    while num > 0:
        digit = num % 10
        s = s + digit
        num = num // 10
    return s


def sum_is_good(num):
    return (sum_of_digits(num) % 7) == 0


def list_add(list, func):
    sum = 0
    for k in list:
        if func(k):
            sum = sum + k
    return sum


result_1 = list_add([x ** 3 for x in range(1, 1001) if x % 2 == 1], sum_is_good)
result_2 = list_add([x ** 3 + 17 for x in range(1, 1001) if x % 2 == 1], sum_is_good)

print("Сумма_1:", result_1, "Сумма_2:", result_2)