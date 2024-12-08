import math

class Figure:
    sides_count = 0

    def __init__(self, color, *sides):
        self.__color = list(color) if self.__is_valid_color(*color) else [0, 0, 0]
        self.__sides = list(sides) if self.__is_valid_sides(*sides) else [1] * self.sides_count
        self.filled = False

    def get_color(self):
        return self.__color

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_color(self, r, g, b):
        return all(isinstance(value, int) and 0 <= value <= 255 for value in (r, g, b))

    def get_sides(self):
        return self.__sides

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count and all(isinstance(s, int) and s > 0 for s in new_sides):
            self.__sides = list(new_sides)

    def __is_valid_sides(self, *sides):
        return len(sides) == self.sides_count and all(isinstance(s, int) and s > 0 for s in sides)

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self.get_sides()[0] / (2 * math.pi)

    def get_square(self):
        return math.pi * (self.__radius ** 2)


class Triangle(Figure):
    sides_count = 3

    def get_square(self):
        sides = self.get_sides()
        s = sum(sides) / 2
        return math.sqrt(s * (s - sides[0]) * (s - sides[1]) * (s - sides[2]))


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        side_length = sides[0] if len(sides) == 1 and isinstance(sides[0], int) and sides[0] > 0 else 1
        super().__init__(color, *[side_length] * self.sides_count)

    def get_volume(self):
        side_length = self.get_sides()[0]
        return side_length ** 3



circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)


circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())  # [55, 66, 77]
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())  # [222, 35, 130]


cube1.set_sides(5, 3, 12, 4, 5)
print(cube1.get_sides())
circle1.set_sides(15)
print(circle1.get_sides())  # [15]


print(len(circle1))  # 15


print(cube1.get_volume())  # 216
