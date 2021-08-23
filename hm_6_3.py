import sys
from itertools import zip_longest

# Написать код, загружающий данные из обоих файлов и формирующий из них словарь:
# ключи — ФИО, значения — данные о хобби.


name = open('users.csv', encoding="utf-8")
names = []
hobbies = []
for line in name:
    names.append(line.strip().replace(',', ' '))
name.close()
hobby = open('hobby.csv', encoding="utf-8")
for line in hobby:
    hobbies.append(line.strip())
hobby.close()

if len(hobbies) > len(names):
    sys.exit(1)

res = dict(zip_longest(names, hobbies))

for k in res:
    print(f'{k}: {res[k]}')
f = open('result.txt', 'w')
for k, v in res.items():
    f.write(f'{k}: {v}\n')
f.close()
