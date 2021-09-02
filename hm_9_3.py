
"""Реализовать базовый класс Worker (работник): определить атрибуты: name, surname, position (должность), income (доход);
последний атрибут должен быть защищённым и ссылаться на словарь,
 содержащий элементы «оклад» и «премия», например, {"wage": wage, "bonus": bonus};
создать класс Position (должность) на базе класса Worker;
в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода
                                                                   с учётом премии (get_total_income);
проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные,
проверить значения атрибутов, вызвать методы экземпляров.
"""

class Money:

    def __init__(self, money : (int, int)):
        self.dollars = money[0]
        self.cents = money[1]

    def __str__(self):
        return f'{str(self.dollars)} bucks and {str(self.cents)} cents'
    def __add__(self, other):
        new_cents = self.cents + other.cents
        new_dollars = self.dollars + other.dollars
        if (new_cents > 100):
            new_dollars += 1
            new_cents -= 100
        return Money((new_dollars, new_cents))

class Worker:
    name: str
    surname: str
    position: str
    _income: dict

    def __init__(self, name: str, surname: str, position: str, wage: (int, int), bonus: (int, int)):

        self.name = name
        self.surname = surname
        self.position = position
        self._income = {
            'wage': Money(wage),
            'bonus': Money(bonus)
        }

class Position(Worker):
    def get_full_name(self):
        return f'{self.name} {self.surname}'

    def get_total_income(self):
        result = Money((0, 0))
        for k in self._income.values():
            result += k
        return result


ivan = Position('Ivan', 'Krivonos', 'Arhitect', wage = (14200, 25), bonus = (750, 50))
print(ivan.get_full_name(), ivan.get_total_income())

galina = Position('Galina', 'Krivonos', 'Developer', wage = (10500, 55), bonus = (555, 55))
print(galina.get_full_name(), galina.get_total_income())