class Car:
    speed: int
    color: str
    name: str
    is_police: bool = False

    def __init__(self, speed: int, color: str, name: str) -> None:
        self.speed = speed
        self.color = color
        self.name = name

    def go(self):
        print(f"{self.name}: start")

    def stop(self):
        print(f"{self.name}: finish")

    def turn(self, direction: str):
        print(f"{self.name}: turn  {direction}")

    def show_speed(self):
        print(f"{self.name}: speed = {self.speed} km/h")


class TownCar(Car):
    def show_speed(self):
        super().show_speed() # super() - это функция, которая обращается к классу, от которого наследуется текущий
        if self.speed > 60:
            print(f"{self.name}: over speed")


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if self.speed > 40:
            print(f"{self.name}: over speed")


class PoliceCar(Car):
    is_police: bool = True


cars = [
    SportCar(205, 'brown', 'BMW'),
    TownCar(39, 'black', 'Priora 3'),
    WorkCar(70, 'blue', 'Niva'),
    PoliceCar(111, 'white', 'Audi'),
]

cars[3].go()
cars[3].turn('left')
cars[3].stop()
cars[0].go()
cars[0].turn('right')
cars[0].stop()
for car in cars:
    car.show_speed()