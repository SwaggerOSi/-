import random

class Animal:
    live = True
    sound = None
    _DEGREE_OF_DANGER = 0
    _cords = [0, 0, 0]
    _speed = None

    def __init__(self, speed):
        self._speed = speed

    def Move(self, dx, dy, dz):
        self._cords[0] += self._speed * dx
        self._cords[1] += self._speed * dy
        if dz < 0:
            print("It's too deep, I can't dive :(")
        else:
            self._cords[2] += self._speed * dz

    def Get_cords(self):
        return f"X: {self._cords[0]} Y: {self._cords[1]} Z: {self._cords[2]}"

    def Attack(self):
        if self._DEGREE_OF_DANGER < 5:
            return "Sorry, I'm peaceful."
        else:
            return "Be careful, I'm attacking you! 0_0"


class Bird(Animal):
    beak = True

    def Lay_eggs(self):
        return f"Here are {random.randint(1, 4)} egg(s) for you."


class AquaticAnimal(Animal):
    _DEGREE_OF_DANGER = 3

    def Dive_in(self, dz):
        self._speed /= 2
        self._cords[2] -= dz * self._speed


class PoisonusAnimal(Animal):
    _DEGREE_OF_DANGER = 8


class Duckbill(PoisonusAnimal, Bird, AquaticAnimal):
    sound = "click click click"


# Тестирование
db = Duckbill(10)
print(db.live)  # True
print(db.beak)  # True
print(db.sound)  # "click click click"
print(db.Attack())  # "Be careful, I'm attacking you! 0_0"

db.Move(1, 2, 3)
print(db.Get_cords())  # "X: 10 Y: 20 Z: 30"

db.Dive_in(6)
print(db.Get_cords())  # Уменьшение координаты Z с учетом скорости

print(db.Lay_eggs())  # "Here are X egg(s) for you."