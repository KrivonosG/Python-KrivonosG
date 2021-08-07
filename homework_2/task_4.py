import random
a = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']
b = []
for i in range(len(a)):
    b.append("Привет, {0}!".format(a[i].split(' ')[-1].title()))

print(b[random.randrange(0, len(b) - 1)])     # Приветствуем случайного человека из списка

# Or
print("Привет, {0}!".format(a[random.randint(0, len(a)-1)].split(' ')[-1].title()))   # Приветствуем случайного человека из списка

