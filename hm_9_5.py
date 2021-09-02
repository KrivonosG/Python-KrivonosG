class Stationery:
    title: str
    _message = "Запуск отрисовки."

    def draw(self):
        print(self._message)


class Pen(Stationery):
    title = 'Ручка'
    _message = f"{title}: для важных записей."


class Pencil(Stationery):
    title = 'Карандаш'
    _message = f"{title}: для пометок на полях."


class Handle(Stationery):
    title = 'Маркер'
    _message = f"{title}: для подчёркивания важного."


items = [Pen(), Pencil(), Handle()]

for item in items:
    item.draw()