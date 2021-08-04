def declination(num):
    a = " процент"
    b = " процента"
    c = " процентов"
    numbs = {11, 12, 13, 14}
    if num in numbs:
        return str(num) + c
    rem = num % 10
    if rem == 1:
        return str(num) + a
    elif 1 < rem < 5:
        return str(num) + b
    else:
        return str(num) + c


for i in range(1, 101):
    print(declination(i))