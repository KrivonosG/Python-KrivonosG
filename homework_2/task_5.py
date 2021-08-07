my_list = [78.86, 34.34, 12.9, 99.5, 11.8, 25.25, 100.5, 57.8, 46.51, 97, 59.68]


def print_prices(arg):
    for k in map(lambda x: tuple(map(int, str(x).split('.'))), arg):
        rubles = 0
        kopeks = 0
        if len(k) > 1:
            rubles = k[0]
            kopeks = k[1]
        else:
            rubles = k[0]

        print(f'Цена: {str(rubles)} руб {int(kopeks):02d} коп')


# A:
print_prices(my_list)
# B:
print_prices(sorted(my_list))
# C:
my_list_copy = my_list.copy()
my_list_copy.sort(reverse=True)
# D:
print_prices(my_list_copy)
print_prices(my_list_copy[:5])
