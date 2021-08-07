a = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']


def check_sign(x):
    if x[0] in '+-':
        return x[0]


n = 0
while n < len(a):
    sign = check_sign(a[n])
    if a[n].isdigit() or (sign and a[n][1:].isdigit()):
        if sign:
            a[n] = sign + a[n][1:].zfill(2)
        else:
            a[n] = a[n].zfill(2)

        a.insert(n, '"')
        a.insert(n + 2, '"')
        n += 2

    n += 1
delimiter = ' '
single_str = delimiter.join(a)
print(' {0}'.format(single_str))
